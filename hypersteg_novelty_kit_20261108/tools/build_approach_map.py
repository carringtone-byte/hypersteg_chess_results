# === SCRIPT: Build the approach map — every published approach as one network ===
# Purpose: a derived, human-facing view of the approach claims in the corpus. An
#          approach is a claim whose **ID:** slug starts with `approach-` (a scheme a
#          paper proposes) or `surveyed-` (a scheme a survey describes), or any other
#          ledger claim a features-table row names, whatever its slug. Families and
#          techniques come from two tables, because the edge taxonomy has no "member
#          of family" edge: the features table places each approach in a family and,
#          optionally, under a technique; the technique taxonomy arranges techniques
#          as a tree within each family (family -> technique -> sub-technique, any
#          depth). Lineage edges are the existing in-band lines, parsed and resolved
#          by claim_graph, so this tool and the structure gate read one grammar.
#          Most edge lines sit under a claim that quotes the paper's "builds on"
#          sentence rather than under its approach claim, so an end that is not an
#          approach is lifted to its paper's approach (see collect_edges); the
#          lifted edges say so in a `lifted_from` column.
#          A project uses the map to audit whether a new scheme mimics a published
#          approach, improves on one, or falls outside all of them.
#          A family tree alone misleads that audit: a scheme's nearest published
#          neighbour may sit in another family. An optional mechanism taxonomy is a
#          second tree, across families, classed by how a scheme hides bits; the
#          features table's `mechanism` cell places each approach in it, and the
#          `neighbours` subcommand lists the landable approaches nearest a node.
# Views  : approach_map_view: lineage (paper-stated edges between approaches) |
#          techniques (the taxonomy tree, approaches as leaves) | both (the tree with
#          the lineage edges overlaid). inferred_links: on adds dashed links between
#          approaches sharing channel, key and access_needed; they are drawn only, and
#          never counted as edges.
# INPUTS : literature/verified_claims/<key>.md ledgers; `approach_features:` (default
#          maps/approach_features.tsv), `technique_taxonomy:` (default
#          maps/technique_taxonomy.tsv) and `mechanism_taxonomy:` (default
#          maps/mechanism_taxonomy.tsv, optional) from ledger.config.md.
# OUTPUTS: an overview at `approach_map_out:` (default maps/approach_map.md) holding
#          family and technique nodes only, and one <stem>_<family>.md per family with
#          the full tree and its approaches. With a mechanism taxonomy, also
#          <stem>_mechanisms.md and one <stem>_mech_<class>.md per mechanism class.
#          Each file is a live file plus a snapshot <name>_YYYYMMDD[a-z].md, written
#          only when its content changes.
#          Exit 0 = built, or nothing to build (stated as a warning); 1 = error.
# Run    : python3 tools/build_approach_map.py             # write the maps
#          python3 tools/build_approach_map.py --dry-run   # counts and target paths only
#          python3 tools/build_approach_map.py --out /path/to/approach_map.md
#          python3 tools/build_approach_map.py neighbours <mechanism_id> [...]
#          python3 tools/build_approach_map.py check-coverage   # exit 1 on an unevidenced leaf
from __future__ import annotations

import argparse
import csv
import datetime as dt
import re
import sys
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path

import claim_graph as cg
from build_graph import _mid
from check_citations import parse_config
from ledger_md import claim_blocks

REPO_ROOT = Path(__file__).resolve().parents[1]

APPROACH_PREFIXES = ("approach-", "surveyed-")
DEFAULT_FEATURES = "maps/approach_features.tsv"
DEFAULT_TAXONOMY = "maps/technique_taxonomy.tsv"
DEFAULT_MECHANISMS = "maps/mechanism_taxonomy.tsv"
DEFAULT_OUT = "maps/approach_map.md"
VIEWS = ("lineage", "techniques", "both")
DEFAULT_VIEW = "lineage"
FEATURE_COLUMNS = ("address", "approach", "family", "carrier_medium", "channel", "key",
                   "access_needed", "capacity", "security_notion", "robustness",
                   "pre_coordination", "builds_on", "evidence_slugs", "notes")
OPTIONAL_FEATURE_COLUMNS = ("technique", "mechanism", "mechanism_evidence", "carrier",
                            "acquisition")
TAXONOMY_COLUMNS = ("technique_id", "parent_id", "family", "name", "definition",
                    "grounded_by", "notes")
OPTIONAL_TAXONOMY_COLUMNS = ("landing",)
ACQUISITION_VALUES = ("prompted", "negotiated", "in-context-optimised", "rl-trained",
                      "weight-trained", "focal", "specified", "unknown")
# A qualifier any acquisition value may carry, as `<value>+unprescribed`.
ACQUISITION_QUALIFIERS = ("unprescribed",)
# A mechanism_evidence entry: the approach claim's own quotes evidence the mechanism,
# a sibling claim of the same ledger does (`sibling:<claim-slug>`), or only in part.
EVIDENCE_VALUES = ("own", "partial")
EVIDENCE_SIBLING = "sibling:"
UNKNOWN_EVIDENCE = "unknown"
VERDICT_OUTCOMES = ("mimics", "improves upon", "falls outside", "insufficient evidence")
BROAD_MATCH_NOTE = ("A broad match (distance 1 or more: under an ancestor or elsewhere in "
                    "the class) does not by itself support \"mimics\".")
NOT_LANDING = "not a landing node"
MECH_OVERVIEW_SUFFIX = "mechanisms"
MECH_FILE_INFIX = "mech_"
INFERRED_KEYS = ("channel", "key", "access_needed")
UNCLASSIFIED = "unclassified"
LABEL_MAX_CHARS = 60
LOG_LIST_MAX = 20

# Each lineage edge kind gets its own arrow and colour, so kinds stay distinct in a
# renderer that drops edge labels. Rebuts is dotted, as in build_graph.to_mermaid.
EDGE_STYLE: dict[str, tuple[str, str]] = {
    "supports": ("-->", "#2e7d32"),
    "rebuts": ("-.->", "#c62828"),
    "depends-on": ("==>", "#6a1b9a"),
    "refines": ("-->", "#1565c0"),
    "qualifies": ("-.->", "#ef6c00"),
    "restates": ("<-->", "#00838f"),
    "duplicate-of": ("o--o", "#757575"),
    "supersedes": ("--x", "#4e342e"),
}
SHAPES = {"box": ("[", "]"), "round": ("(", ")"), "hex": ("{{", "}}"),
          "stadium": ("([", "])")}
STUB_CLASS = "classDef stub fill:#f5f5f5,stroke:#9e9e9e,stroke-dasharray:4 3,color:#424242"
TREE_STYLE = "stroke:#9e9e9e,stroke-width:1px"
LINEAGE_WIDTH = "stroke-width:2.5px"
INFERRED_STYLE = "stroke:#ff8f00,stroke-width:1px,stroke-dasharray:6 4,color:#ff8f00"
INFERRED_LABEL = "inferred from features"
NON_LANDING_CLASS = ("classDef nonlanding fill:#eeeeee,stroke:#bdbdbd,"
                     "stroke-dasharray:2 2,color:#9e9e9e")

CLAIM_PREFIX_RE = re.compile(r"^##\s+claim\s*\d*\s*[:.—-]?\s*", re.IGNORECASE)
APPROACH_LEAD_RE = re.compile(r"^(approach|surveyed)\b[^—]*—\s*", re.IGNORECASE)
FRONTMATTER_RE = re.compile(r"\A---\n.*?\n---\n", re.DOTALL)
# A claim's own edge lines cite it as `(grounded by #slug)`; that names the source
# itself, not the approach the claim is about.
GROUNDING_CLAUSE_RE = re.compile(r"\(grounded by\s+#[\w-]+\)", re.IGNORECASE)


def log_info(msg: str) -> None:
    print(f"[INFO] {msg}")


def log_warning(msg: str) -> None:
    print(f"[WARNING] {msg}", file=sys.stderr)


def log_error(msg: str) -> None:
    print(f"[ERROR] {msg}", file=sys.stderr)


@dataclass(frozen=True)
class Approach:
    """One approach claim. `address` is canonical <key>:<approach-slug>."""
    address: str
    key: str
    slug: str
    name: str


@dataclass
class MapEdge:
    """A drawable lineage edge. Each end is an approach address or a paper node
    (`paper:<key>`). `lifted_from` names the claim(s) an end was lifted from, empty
    when both ends were already approach claims; `origin` is the ledger line."""
    edge_type: str
    source: str
    target: str
    lifted_from: list[str] = field(default_factory=list)
    origin: list[str] = field(default_factory=list)


@dataclass(frozen=True)
class Technique:
    """One taxonomy row, of either tree. `parent` is None for a top-level node in its
    family (in the mechanism tree, its class). `landing` is 'yes', 'no' or '' (inherit)."""
    technique_id: str
    parent: str | None
    family: str
    name: str
    definition: str
    grounded_by: str
    line_no: int
    landing: str = ""


@dataclass
class Taxonomy:
    techniques: dict[str, Technique] = field(default_factory=dict)
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    def children(self, parent: str | None, family: str) -> list[Technique]:
        return sorted((t for t in self.techniques.values()
                       if t.parent == parent and self.family_of(t.technique_id) == family),
                      key=lambda t: t.technique_id)

    def family_of(self, technique_id: str) -> str:
        """A technique's family is its root's: a subtree never spans two families."""
        tech = self.techniques[technique_id]
        seen = {technique_id}
        while tech.parent and tech.parent in self.techniques and tech.parent not in seen:
            seen.add(tech.parent)
            tech = self.techniques[tech.parent]
        return tech.family or UNCLASSIFIED

    def ancestors(self, technique_id: str) -> list[str]:
        out: list[str] = []
        current = self.techniques[technique_id].parent
        while current and current in self.techniques and current not in out:
            out.append(current)
            current = self.techniques[current].parent
        return out

    def descendants(self, technique_id: str) -> list[str]:
        return sorted(t for t in self.techniques if technique_id in self.ancestors(t))

    def is_landing(self, technique_id: str) -> bool:
        """The nearest explicit `landing` value on the node or its ancestors; yes when
        none says. A child of a `no` node is therefore `no` unless it says `yes`."""
        for node in [technique_id, *self.ancestors(technique_id)]:
            if self.techniques[node].landing in ("yes", "no"):
                return self.techniques[node].landing == "yes"
        return True

    def non_landing(self) -> list[str]:
        return sorted(t for t in self.techniques if not self.is_landing(t))

    def in_class(self, family: str) -> list[str]:
        return sorted(t for t in self.techniques if self.family_of(t) == family)

    def classes(self) -> list[str]:
        return sorted({self.family_of(t) for t in self.techniques})


def placed_under(tax: Taxonomy, placed: dict[str, tuple[str, ...]], node: str) -> list[str]:
    """Addresses with a placement at `node` or anywhere below it."""
    return sorted(a for a, ids in placed.items()
                  if any(t == node or node in tax.ancestors(t) for t in ids))


@dataclass
class ApproachMap:
    """Everything the renderer needs, plus the lists that keep nothing silent.
    `placement` maps an address to its family and its technique ids, in the order the
    features table lists them; `mechanisms` holds its mechanism ids the same way.
    `mechanism_taxonomy` is None when no mechanism taxonomy file was read."""
    approaches: dict[str, Approach]
    features: dict[str, dict[str, str]]
    taxonomy: Taxonomy
    placement: dict[str, tuple[str, tuple[str, ...]]] = field(default_factory=dict)
    by_key: dict[str, list[str]] = field(default_factory=dict)
    papers: set[str] = field(default_factory=set)
    edges: list[MapEdge] = field(default_factory=list)
    unplaced: list[str] = field(default_factory=list)
    unresolved: list[str] = field(default_factory=list)
    folded: list[str] = field(default_factory=list)
    feature_warnings: list[str] = field(default_factory=list)
    placement_warnings: list[str] = field(default_factory=list)
    inferred_groups: list[list[str]] = field(default_factory=list)
    mechanism_taxonomy: Taxonomy | None = None
    mechanisms: dict[str, tuple[str, ...]] = field(default_factory=dict)
    mechanism_warnings: list[str] = field(default_factory=list)
    columns: set[str] = field(default_factory=set)
    claims_dir: Path | None = None
    placement_errors: list[str] = field(default_factory=list)
    # address -> mechanism id -> own | sibling:<slug> | partial | unknown
    mechanism_evidence: dict[str, dict[str, str]] = field(default_factory=dict)

    def evidence(self, address: str, mechanism_id: str) -> str:
        return self.mechanism_evidence.get(address, {}).get(mechanism_id, UNKNOWN_EVIDENCE)

    def family(self, address: str) -> str:
        return self.placement[address][0]

    def techniques(self, address: str) -> tuple[str, ...]:
        return self.placement[address][1]

    def technique(self, address: str) -> str | None:
        """The first technique listed: the one lineage edges are summed onto in the
        overview, so an edge from a composite approach is counted once."""
        tids = self.techniques(address)
        return tids[0] if tids else None

    def mechanism_keyed(self) -> bool:
        """Whether the approach tables carry the mechanism and landable columns."""
        return self.mechanism_taxonomy is not None or "mechanism" in self.columns

    def landable(self, address: str) -> bool:
        mtax = self.mechanism_taxonomy
        return mtax is not None and any(mtax.is_landing(m)
                                        for m in self.mechanisms.get(address, ()))

    def mech_members(self, mech_class: str) -> list[str]:
        mtax = self.mechanism_taxonomy
        return sorted(a for a, mids in self.mechanisms.items()
                      if mtax and any(mtax.family_of(m) == mech_class for m in mids))

    def mech_count(self, mechanism_id: str) -> int:
        assert self.mechanism_taxonomy is not None
        return len(placed_under(self.mechanism_taxonomy, self.mechanisms, mechanism_id))

    def empty_mechanisms(self) -> list[str]:
        mtax = self.mechanism_taxonomy
        return [m for m in sorted(mtax.techniques) if not self.mech_count(m)] if mtax else []

    def unmechanised(self) -> list[str]:
        return sorted(a for a in self.approaches if not self.mechanisms.get(a))

    def shared_mechanisms(self) -> list[tuple[str, list[str]]]:
        """Mechanism nodes whose directly placed approaches come from two or more
        families: the cross-family neighbours a family tree alone would hide."""
        out = []
        for mid in sorted(self.mechanism_taxonomy.techniques if self.mechanism_taxonomy
                          else ()):
            fams = sorted({self.family(a) for a, mids in self.mechanisms.items()
                           if mid in mids})
            if len(fams) > 1:
                out.append((mid, fams))
        return out

    def families(self) -> list[str]:
        """Families in display order: named ones sorted, then unclassified."""
        fams = {self.family(a) for a in self.approaches}
        fams |= {self.taxonomy.family_of(t) for t in self.taxonomy.techniques}
        named = sorted(f for f in fams if f != UNCLASSIFIED)
        return named + ([UNCLASSIFIED] if UNCLASSIFIED in fams else [])

    def unclassified(self) -> list[str]:
        return sorted(a for a in self.approaches if self.family(a) == UNCLASSIFIED)

    def in_family(self, family: str) -> list[str]:
        return sorted(a for a in self.approaches if self.family(a) == family)

    def subtree_count(self, technique_id: str) -> int:
        """Approaches under this technique or any of its descendants."""
        placed = {a: self.techniques(a) for a in self.approaches}
        return len(placed_under(self.taxonomy, placed, technique_id))

    def empty_techniques(self) -> list[str]:
        return sorted(t for t in self.taxonomy.techniques if not self.subtree_count(t))

    def papers_in(self, family: str) -> list[str]:
        return sorted(p for p in self.papers if self.family(p) == family)

    def lifted(self) -> list[MapEdge]:
        return [e for e in self.edges if e.lifted_from]


def preview(items: list[str]) -> str:
    """A comma list for a log line, cut at LOG_LIST_MAX; the files hold the full list."""
    rest = len(items) - LOG_LIST_MAX
    return ", ".join(items[:LOG_LIST_MAX]) + (
        f", … and {rest} more (full list in the overview)" if rest > 0 else "")


def config_value(config: dict[str, str], key: str) -> str:
    """A config value with any inline comment removed; '' for a <placeholder>."""
    raw = config.get(key, "").split("#", 1)[0].strip()
    return "" if raw.startswith("<") else raw


def config_path_value(config: dict[str, str], key: str, default: str, root: Path) -> Path:
    """A path from ledger.config.md; a blank or placeholder value takes the default.
    Relative paths resolve against the project root; `~` expands."""
    path = Path(config_value(config, key) or default).expanduser()
    return path if path.is_absolute() else root / path


def config_choice(config: dict[str, str], key: str, choices: tuple[str, ...],
                  default: str) -> str:
    raw = config_value(config, key).lower()
    if raw and raw not in choices:
        log_warning(f"{key}: '{raw}' is not one of {' | '.join(choices)}; using {default}")
    return raw if raw in choices else default


def approach_name(header: str) -> str:
    """The claim header without `## Claim N:` and a leading `Approach —` label."""
    name = CLAIM_PREFIX_RE.sub("", header).strip()
    return APPROACH_LEAD_RE.sub("", name).strip() or name


def find_approaches(claims_dir: Path) -> tuple[dict[str, Approach], dict[tuple[str, str], str]]:
    """Every approach claim, and an alias index (key, slug-or-cN) -> approach address,
    so an edge that names the claim by ordinal or by a second **ID:** still lands on it."""
    approaches: dict[str, Approach] = {}
    aliases: dict[tuple[str, str], str] = {}
    if not claims_dir.is_dir():
        return approaches, aliases
    for ledger in sorted(claims_dir.glob("*.md")):
        if ledger.stem == "TEMPLATE":
            continue
        key = ledger.stem.lower()
        for block in claim_blocks(ledger):
            slugs = [m.group(1).lower() for m in block.fields(cg._ID_LINE_RE)]
            approach_slugs = [s for s in slugs if s.startswith(APPROACH_PREFIXES)]
            if not approach_slugs:
                continue
            address = f"{key}:{approach_slugs[0]}"
            approaches[address] = Approach(address, key, approach_slugs[0],
                                           approach_name(block.header))
            for alias in {f"c{block.ordinal}", *slugs}:
                aliases[(key, alias)] = address
    return approaches, aliases


def split_ids(cell: str) -> tuple[str, ...]:
    """The `;`-separated ids of a cell, lower-cased, blanks and repeats dropped."""
    return tuple(dict.fromkeys(p.strip().lower() for p in cell.split(";") if p.strip()))


def read_tsv(path: Path, label: str, required: tuple[str, ...], expected: tuple[str, ...],
             optional: tuple[str, ...] = ()
             ) -> tuple[list[tuple[int, dict[str, str]]], list[str]]:
    """(line number, stripped row) pairs and header warnings. Raises ValueError when a
    required column is missing: such a table cannot be read at all. A missing
    `optional` column raises no warning."""
    warnings: list[str] = []
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        header = [h.strip() for h in (reader.fieldnames or [])]
        missing_required = [c for c in required if c not in header]
        if missing_required:
            raise ValueError(f"{label} {path} lacks column(s) {', '.join(missing_required)}")
        missing = [c for c in expected if c not in header]
        extra = [c for c in header if c not in expected and c not in optional]
        if missing or extra:
            warnings.append(f"{label} header differs from the expected one — missing: "
                            f"{', '.join(missing) or 'none'}; extra: {', '.join(extra) or 'none'}")
        rows = [(line_no, {(k or "").strip(): (v or "").strip()
                           for k, v in raw.items() if k is not None})
                for line_no, raw in enumerate(reader, start=2)]
    return rows, warnings


def adopt_row_claim(address: str, approaches: dict[str, Approach],
                    aliases: dict[tuple[str, str], str], claims_dir: Path | None
                    ) -> tuple[str | None, str]:
    """The approach address a features row names, adopting the claim as an approach
    when it is a real ledger claim without an approach-/surveyed- slug: the row itself
    declares it an approach. Returns (address, '') for an approach, (canonical
    address, '') when the row names an approach by another of its ids, or (None,
    reason) when the address resolves to no claim."""
    if address in approaches:
        return address, ""
    parsed = cg.parse_address(address)
    if parsed.key is None or claims_dir is None:
        return None, "is not a key:slug address"
    known = aliases.get((parsed.key, parsed.slug))
    if known:
        return known, ""
    res = cg.resolve(parsed, parsed.key, claims_dir)
    if not res.exists or res.ledger_path is None:
        return None, f"names no claim — {res.reason}"
    for block in claim_blocks(res.ledger_path):
        slugs = [m.group(1).lower() for m in block.fields(cg._ID_LINE_RE)]
        if parsed.slug in (f"c{block.ordinal}", *slugs):
            approaches[address] = Approach(address, parsed.key, parsed.slug,
                                           approach_name(block.header))
            for alias in {f"c{block.ordinal}", *slugs}:
                aliases.setdefault((parsed.key, alias), address)
            return address, ""
    return None, f"names no claim in {res.ledger_path.name}"


def load_features(path: Path, approaches: dict[str, Approach],
                  aliases: dict[tuple[str, str], str] | None = None,
                  claims_dir: Path | None = None
                  ) -> tuple[dict[str, dict[str, str]], list[str]]:
    """Feature rows keyed by lower-cased address, and the warnings raised reading them.
    A missing table is a warning (every approach is then unclassified). With
    `claims_dir`, a row naming a real claim whatever its slug prefix makes that claim
    an approach (added to `approaches` and `aliases`), and a row naming an approach
    by another of its ids is keyed by the approach's address."""
    aliases = {} if aliases is None else aliases
    if not path.is_file():
        return {}, [f"features table not found: {path} — every approach is unclassified"]
    rows, warnings = read_tsv(path, "features table", ("address", "family"), FEATURE_COLUMNS,
                              OPTIONAL_FEATURE_COLUMNS)
    features: dict[str, dict[str, str]] = {}
    for line_no, row in rows:
        address = row.get("address", "").lower()
        if not address:
            warnings.append(f"features table line {line_no}: empty address, skipped")
            continue
        if address not in approaches:
            canonical, reason = adopt_row_claim(address, approaches, aliases, claims_dir)
            if canonical is None:
                warnings.append(f"features table line {line_no}: {address} names no "
                                f"approach claim ({reason})")
            elif canonical != address:
                warnings.append(f"features table line {line_no}: {address} names the "
                                f"approach {canonical} by another id; read as {canonical}")
                address = canonical
        if address in features:
            warnings.append(f"features table line {line_no}: duplicate row for "
                            f"{address}, first kept")
            continue
        for value in split_ids(row.get("acquisition", "")):
            if not acquisition_ok(value):
                warnings.append(f"features table line {line_no}: {address} acquisition "
                                f"'{value}' is not one of {', '.join(ACQUISITION_VALUES)}, "
                                "optionally with +" + " or +".join(ACQUISITION_QUALIFIERS))
        features[address] = row
    return features, warnings


def acquisition_ok(value: str) -> bool:
    """A vocabulary value, optionally qualified as `<value>+unprescribed`."""
    base, plus, qualifier = value.partition("+")
    return base in ACQUISITION_VALUES and (not plus or qualifier in ACQUISITION_QUALIFIERS)


def load_taxonomy(path: Path, claims_dir: Path, needed: bool,
                  noun: str = "technique") -> Taxonomy:
    """A taxonomy tree: the technique tree, or with noun="mechanism" the mechanism
    tree, which has the same columns. An unknown parent or a parent cycle is an
    error; a missing or unresolvable grounded_by, or a `landing` value other than
    yes or no, is a warning. A missing file is a warning only when `needed`."""
    tax = Taxonomy()
    if not path.is_file():
        if needed:
            consequence = ("hang directly under their family" if noun == "technique"
                           else f"are placed in no {noun}")
            tax.warnings.append(f"{noun} taxonomy not found: {path} — approaches "
                                + consequence)
        return tax
    rows, tax.warnings = read_tsv(path, f"{noun} taxonomy", ("technique_id", "family"),
                                  TAXONOMY_COLUMNS, OPTIONAL_TAXONOMY_COLUMNS)
    for line_no, row in rows:
        tid = row.get("technique_id", "").lower()
        if not tid:
            tax.warnings.append(f"{noun} taxonomy line {line_no}: empty technique_id, "
                                "skipped")
            continue
        if tid in tax.techniques:
            tax.warnings.append(f"{noun} taxonomy line {line_no}: duplicate "
                                f"technique_id {tid}, first kept")
            continue
        landing = row.get("landing", "").lower()
        if landing not in ("", "yes", "no"):
            tax.warnings.append(f"{noun} taxonomy line {line_no}: landing '{landing}' "
                                "is not yes or no; inherited from the parent")
            landing = ""
        tax.techniques[tid] = Technique(
            tid, row.get("parent_id", "").lower() or None, row.get("family", ""),
            row.get("name", "") or tid, row.get("definition", ""),
            row.get("grounded_by", ""), line_no, landing)

    for tech in tax.techniques.values():
        if tech.parent and tech.parent not in tax.techniques:
            tax.errors.append(f"{noun} {tech.technique_id} (line {tech.line_no}): "
                              f"unknown parent_id {tech.parent}")
    reported: set[frozenset[str]] = set()
    for tid in tax.techniques:
        path_ids = [tid]
        current = tax.techniques[tid].parent
        while current and current in tax.techniques:
            if current in path_ids:
                cycle = path_ids[path_ids.index(current):]
                if frozenset(cycle) not in reported:
                    reported.add(frozenset(cycle))
                    tax.errors.append("parent cycle: " + " -> ".join(cycle + [current]))
                break
            path_ids.append(current)
            current = tax.techniques[current].parent
    if tax.errors:
        return tax

    for tech in tax.techniques.values():
        root_family = tax.family_of(tech.technique_id)
        if tech.parent and tech.family and tech.family != root_family:
            tax.warnings.append(f"{noun} {tech.technique_id}: family '{tech.family}' "
                                f"differs from its root's '{root_family}'; drawn under the root's")
        if not tech.grounded_by:
            tax.warnings.append(f"{noun} {tech.technique_id}: no grounded_by claim")
            continue
        address = cg.parse_address(tech.grounded_by)
        if address.key is None:
            tax.warnings.append(f"{noun} {tech.technique_id}: grounded_by "
                                f"'{tech.grounded_by}' is not a key:slug address")
            continue
        res = cg.resolve(address, address.key, claims_dir)
        if not res.exists:
            tax.warnings.append(f"{noun} {tech.technique_id}: grounded_by "
                                f"'{tech.grounded_by}' does not resolve — {res.reason}")
    return tax


def place_approaches(amap: ApproachMap) -> None:
    """Each approach's (family, techniques). The `technique` cell may list several
    ids separated by `;`. The features row's family wins; a row with a technique but
    no family takes its first technique's family. An unknown technique, or one from
    another family, is dropped with a warning; with none left, the approach hangs
    directly under its family."""
    tax = amap.taxonomy
    for address in sorted(amap.approaches):
        row = amap.features.get(address, {})
        family = row.get("family", "")
        kept: list[str] = []
        for tid in split_ids(row.get("technique", "")):
            if tid not in tax.techniques:
                amap.placement_warnings.append(f"{address}: unknown technique_id '{tid}'")
                continue
            tech_family = tax.family_of(tid)
            if not family:
                family = tech_family
            elif family != tech_family:
                amap.placement_warnings.append(
                    f"{address}: technique '{tid}' belongs to family '{tech_family}', "
                    f"not '{family}'; not placed under it")
                continue
            kept.append(tid)
        amap.placement[address] = (family or UNCLASSIFIED, tuple(kept))


def place_mechanisms(amap: ApproachMap) -> None:
    """Each approach's mechanism ids, from the `;`-separated `mechanism` cell. Unlike
    techniques, mechanisms cross families, so any known id is kept; an unknown one is
    dropped with a warning."""
    mtax = amap.mechanism_taxonomy
    for address in sorted(amap.approaches):
        cell = amap.features.get(address, {}).get("mechanism", "")
        kept: list[str] = []
        for mid in split_ids(cell):
            if mtax is not None and mid not in mtax.techniques:
                amap.mechanism_warnings.append(f"{address}: unknown mechanism id '{mid}'")
                continue
            kept.append(mid)
        amap.mechanisms[address] = tuple(kept)
        if mtax is not None and kept and not any(mtax.is_landing(m) for m in kept):
            amap.mechanism_warnings.append(
                f"{address}: placed only at nodes marked {NOT_LANDING} "
                f"({'; '.join(kept)}); not landable")
        # A landable row must say how the scheme was obtained (`unknown` is allowed);
        # a row placed only at non-landing nodes may say or not.
        if (mtax is not None and amap.landable(address)
                and not split_ids(amap.features.get(address, {}).get("acquisition", ""))):
            amap.mechanism_warnings.append(
                f"{address}: has a landing mechanism but no acquisition; write "
                f"'{UNKNOWN_EVIDENCE}' when it is not known")
    place_evidence(amap)


def raw_entries(cell: str) -> list[str]:
    """The `;`-separated entries of a cell in order, lower-cased, repeats kept, so
    two aligned cells can be paired position by position."""
    return [p.strip().lower() for p in cell.split(";") if p.strip()]


def evidence_problem(amap: ApproachMap, address: str, entry: str) -> str:
    """Why a mechanism_evidence entry is not valid; '' when it is."""
    if entry in EVIDENCE_VALUES:
        return ""
    if not entry.startswith(EVIDENCE_SIBLING):
        return (f"'{entry}' is not one of {', '.join(EVIDENCE_VALUES)} or "
                f"{EVIDENCE_SIBLING}<claim-slug>")
    slug = entry[len(EVIDENCE_SIBLING):].strip()
    if not slug:
        return f"'{entry}' names no sibling claim"
    if amap.claims_dir is None or address not in amap.approaches:
        return ""
    res = cg.resolve(cg.Address(None, slug), amap.approaches[address].key, amap.claims_dir)
    return "" if res.exists else f"'{entry}' does not resolve — {res.reason}"


def place_evidence(amap: ApproachMap) -> None:
    """Each approach's mechanism_evidence, paired position by position with its
    mechanism cell. An absent column leaves every entry unknown, warned once; a row
    whose two cells differ in length is all unknown; a bad entry is unknown alone."""
    rows = {a: amap.features.get(a, {}) for a in sorted(amap.approaches)}
    with_mechanisms = [a for a, row in rows.items() if raw_entries(row.get("mechanism", ""))]
    if "mechanism_evidence" not in amap.columns:
        if with_mechanisms:
            amap.mechanism_warnings.append(
                "features table has no mechanism_evidence column; the evidence for "
                f"every mechanism placement is {UNKNOWN_EVIDENCE}")
        return
    for address in with_mechanisms:
        mids = raw_entries(rows[address].get("mechanism", ""))
        entries = raw_entries(rows[address].get("mechanism_evidence", ""))
        if not entries:
            amap.mechanism_warnings.append(
                f"{address}: no mechanism_evidence; every placement is {UNKNOWN_EVIDENCE}")
            continue
        if len(entries) != len(mids):
            amap.mechanism_warnings.append(
                f"{address}: mechanism_evidence has {len(entries)} entr"
                f"{'y' if len(entries) == 1 else 'ies'} for {len(mids)} mechanism(s); "
                f"not aligned, every placement is {UNKNOWN_EVIDENCE}")
            continue
        evidence: dict[str, str] = {}
        for mid, entry in zip(mids, entries):
            problem = evidence_problem(amap, address, entry)
            if problem:
                amap.mechanism_warnings.append(
                    f"{address}: mechanism_evidence for {mid} {problem}; "
                    f"read as {UNKNOWN_EVIDENCE}")
                entry = UNKNOWN_EVIDENCE
            evidence.setdefault(mid, entry)
        amap.mechanism_evidence[address] = evidence


def grounding_resolution(amap: ApproachMap, mechanism_id: str) -> "cg.Resolution | None":
    """The resolved grounded_by claim of a mechanism node; None when it has none or
    names no key:slug address."""
    mtax = amap.mechanism_taxonomy
    assert mtax is not None
    grounded_by = mtax.techniques[mechanism_id].grounded_by
    address = cg.parse_address(grounded_by) if grounded_by else None
    if address is None or address.key is None or amap.claims_dir is None:
        return None
    return cg.resolve(address, address.key, amap.claims_dir)


def coverage_gaps(amap: ApproachMap) -> list[str]:
    """Landing leaves of the mechanism tree with neither an approach placed at them
    nor a grounded_by claim that resolves. Each reads as false novelty to a judge,
    since the lookup finds nothing published there."""
    mtax = amap.mechanism_taxonomy
    if mtax is None:
        return []
    gaps = []
    for mid in sorted(mtax.techniques):
        if not mtax.is_landing(mid) or mtax.descendants(mid):
            continue
        if any(mid in mids for mids in amap.mechanisms.values()):
            continue
        res = grounding_resolution(amap, mid)
        if res is not None and res.exists:
            continue
        grounded_by = mtax.techniques[mid].grounded_by
        why = (f"grounded_by '{grounded_by}' does not resolve" if grounded_by
               else "no grounded_by claim")
        gaps.append(f"{mid}: landing leaf with no approach row and no grounding claim "
                    f"({why})")
    return gaps


def inferred_groups(amap: ApproachMap) -> list[list[str]]:
    """Groups of two or more approaches whose channel, key and access_needed are all
    filled and equal (case-insensitive)."""
    groups: dict[tuple[str, ...], list[str]] = {}
    for address in sorted(amap.approaches):
        row = amap.features.get(address, {})
        values = tuple(row.get(k, "").strip().lower() for k in INFERRED_KEYS)
        if all(values):
            groups.setdefault(values, []).append(address)
    return [members for members in groups.values() if len(members) > 1]


def lift_targets(approaches: dict[str, Approach]) -> dict[str, list[str]]:
    """Per ledger key, the approaches an edge end lifts to, in ledger order: its
    `approach-` claims, or when it has none, all its approaches (`surveyed-` claims and
    claims its features rows name)."""
    by_key: dict[str, list[str]] = {}
    for ap in approaches.values():
        by_key.setdefault(ap.key, []).append(ap.address)
    return {key: [a for a in addrs if approaches[a].slug.startswith("approach-")] or addrs
            for key, addrs in by_key.items()}


def quote_lines(body: str) -> set[str]:
    """The quoted text of each `> "…"` line, whitespace-collapsed and lower-cased."""
    out: set[str] = set()
    for line in body.splitlines():
        stripped = line.lstrip()
        idx = [i for i, ch in enumerate(stripped) if ch in '"“”']
        if stripped.startswith(">") and len(idx) >= 2 and idx[-1] > idx[0]:
            out.add(" ".join(stripped[idx[0] + 1:idx[-1]].split()).lower())
    return out


def names_approach(source_body: str, approach: Approach, approach_body: str) -> bool:
    """Whether the source claim names the approach by slug (outside its own **ID:**
    lines) or quotes a sentence the approach claim also quotes."""
    text = "\n".join(GROUNDING_CLAUSE_RE.sub("", line) for line in source_body.splitlines()
                     if not cg._ID_LINE_RE.match(line.strip()))
    if re.search(rf"(?<![\w-]){re.escape(approach.slug)}(?![\w-])", text, re.IGNORECASE):
        return True
    return bool(quote_lines(source_body) & quote_lines(approach_body))


def collect_edges(amap: ApproachMap, claims_dir: Path,
                  aliases: dict[tuple[str, str], str]) -> None:
    """Place every lineage edge on approaches. An end that is not an approach claim is
    lifted to its paper's approach: the only one; or, when the paper has several, those
    the source claim names or quotes; or else a paper node `paper:<key>` in the family
    of the paper's first approach. What cannot be placed is listed: an end in a ledger
    with no approach claim, an unresolved end, and an edge whose ends lift onto one
    approach."""
    bodies: dict[str, str] = {}

    def approach_body(address: str) -> str:
        if address not in bodies:
            ap = amap.approaches[address]
            ledger = cg.ledger_for_key(claims_dir, ap.key)
            bodies[address] = (cg.claim_body(ledger, ap.slug) or "") if ledger else ""
        return bodies[address]

    def lift(key: str, slug: str, source_body: str,
             source_self: str | None) -> tuple[list[str] | None, bool]:
        direct = aliases.get((key, slug))
        if direct:
            return [direct], False
        candidates = amap.by_key.get(key, [])
        if not candidates:
            return None, False
        if len(candidates) == 1:
            return candidates, True
        # A source that is itself one of the candidates shares its own quotes; it
        # does not thereby name itself.
        named = [a for a in candidates if a != source_self
                 and names_approach(source_body, amap.approaches[a], approach_body(a))]
        if named:
            return named, True
        paper = f"paper:{key}"
        amap.papers.add(paper)
        amap.placement[paper] = (amap.family(candidates[0]), ())
        return [paper], True

    edges: dict[tuple[str, str, str], MapEdge] = {}
    direct_keys: set[tuple[str, str, str]] = set()
    for e in cg.iter_edges(claims_dir):
        target_res, ground_res = cg.resolve_edge(e, claims_dir)
        origin = f"{e.originating_key}.md:{e.line_no}"
        source_addr = f"{e.originating_key}:{e.grounding or '?'}"
        target_addr = e.target.render(e.originating_key)
        line = f"{source_addr} --{e.edge_type}--> {target_addr} ({origin})"
        problems = []
        if not target_res.exists:
            problems.append(f"target: {target_res.reason}")
        if ground_res is None:
            problems.append("no (grounded by #slug) clause")
        elif not ground_res.exists:
            problems.append(f"grounding: {ground_res.reason}")
        if problems or ground_res is None or ground_res.ledger_path is None:
            amap.unresolved.append(f"{line} — {'; '.join(problems)}")
            continue
        source_body = cg.claim_body(ground_res.ledger_path, e.grounding) or ""
        source_self = aliases.get((e.originating_key, e.grounding))
        sources, source_lifted = lift(e.originating_key, e.grounding, source_body, None)
        targets, target_lifted = lift(target_res.key, e.target.slug, source_body,
                                      source_self)
        if sources is None or targets is None:
            missing = sorted({k for k, ends in ((e.originating_key, sources),
                                                (target_res.key, targets)) if ends is None})
            amap.unplaced.append(f"{line} — no approach claim in "
                                 + ", ".join(f"{k}.md" for k in missing))
            continue
        lifted_from = ([source_addr] if source_lifted else []) + \
            ([target_addr] if target_lifted else [])
        for source in sources:
            for target in targets:
                if source == target:
                    amap.folded.append(f"{line} — both ends lift to {source}")
                    continue
                key = (e.edge_type, source, target)
                edge = edges.setdefault(key, MapEdge(e.edge_type, source, target))
                edge.lifted_from += [a for a in lifted_from if a not in edge.lifted_from]
                edge.origin.append(origin)
                if not lifted_from:
                    direct_keys.add(key)
    for key in direct_keys:
        edges[key].lifted_from = []
    amap.edges = list(edges.values())


def placement_omissions(amap: ApproachMap) -> list[str]:
    """Features rows that resolve to a real ledger claim but are missing from the
    approaches or from mechanism placement. Each is checked by resolving its address
    afresh, not by trusting the adoption step, so a row dropped anywhere between the
    table and the lookup is an error: a dropped row reads as false novelty."""
    if amap.claims_dir is None:
        return []
    out = []
    for address in sorted(amap.features):
        parsed = cg.parse_address(address)
        if parsed.key is None:
            continue
        if not cg.resolve(parsed, parsed.key, amap.claims_dir).exists:
            continue
        if address not in amap.approaches:
            out.append(f"features row {address} resolves to a ledger claim but is not "
                       "an approach in the map")
        elif address not in amap.mechanisms:
            out.append(f"features row {address} resolves to a ledger claim but was left "
                       "out of mechanism placement")
    return out


def taxonomy_errors(amap: ApproachMap) -> list[str]:
    """Errors that stop the build: from either tree (mechanism ones say so), and
    resolving features rows left out of placement."""
    mtax = amap.mechanism_taxonomy
    return amap.taxonomy.errors + [f"mechanism taxonomy: {e}" for e in
                                   (mtax.errors if mtax else [])] + \
        [f"features table: {e}" for e in amap.placement_errors]


def mechanism_warnings(amap: ApproachMap) -> list[str]:
    mtax = amap.mechanism_taxonomy
    return (mtax.warnings if mtax else []) + amap.mechanism_warnings


def build_map(claims_dir: Path, features_path: Path, taxonomy_path: Path | None = None,
              view: str = DEFAULT_VIEW, inferred: bool = False,
              mechanism_path: Path | None = None) -> ApproachMap:
    """Collect approaches, features, both taxonomies, placements and every lineage
    edge that touches an approach. Check `taxonomy_errors(amap)` before rendering. The
    mechanism taxonomy is read only when its file exists; without it the map is
    exactly the family-and-technique map."""
    approaches, aliases = find_approaches(claims_dir)
    features, feature_warnings = load_features(features_path, approaches, aliases,
                                               claims_dir)
    uses_techniques = any(row.get("technique") for row in features.values())
    taxonomy = (load_taxonomy(taxonomy_path, claims_dir,
                              needed=view != "lineage" or uses_techniques)
                if taxonomy_path else Taxonomy())
    amap = ApproachMap(approaches, features, taxonomy, feature_warnings=feature_warnings,
                       claims_dir=claims_dir)
    amap.columns = {c for row in features.values() for c in row}
    if mechanism_path and mechanism_path.is_file():
        amap.mechanism_taxonomy = load_taxonomy(mechanism_path, claims_dir, needed=True,
                                                noun="mechanism")
    elif any(row.get("mechanism") for row in features.values()):
        amap.mechanism_warnings.append(
            f"mechanism taxonomy not found: {mechanism_path} — the features table's "
            "mechanism ids are shown but placed in no mechanism tree")
    if taxonomy_errors(amap):
        return amap
    place_approaches(amap)
    place_mechanisms(amap)
    amap.placement_errors = placement_omissions(amap)
    amap.by_key = lift_targets(approaches)
    collect_edges(amap, claims_dir, aliases)
    if inferred:
        amap.inferred_groups = inferred_groups(amap)
    return amap


# --- rendering ------------------------------------------------------------------

def _label(text: str) -> str:
    """A Mermaid-safe quoted label: entity-coded quotes and angle brackets."""
    return text.replace('"', "#quot;").replace("<", "#60;").replace(">", "#62;")


def _short(text: str) -> str:
    return text if len(text) <= LABEL_MAX_CHARS else text[:LABEL_MAX_CHARS - 1] + "…"


def _cell(text: str) -> str:
    return text.replace("|", "\\|").replace("\n", " ") or "—"


def _sid(prefix: str, text: str) -> str:
    return prefix + "".join(ch if ch.isalnum() else "_" for ch in text)


def family_node(family: str) -> str:
    return _sid("fam_", family)


def technique_node(technique_id: str) -> str:
    return _sid("tech_", technique_id)


def family_slug(family: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", family.lower()).strip("_") or "family"


class Diagram:
    """A Mermaid flowchart under construction. Links are kept with a style so the
    linkStyle indices always match the order the links were written in."""

    def __init__(self, direction: str) -> None:
        self.lines = [f"flowchart {direction}"]
        self.styles: list[str] = []

    def node(self, node_id: str, label: str, indent: int = 1, shape: str = "box",
             escaped: bool = False) -> None:
        """`escaped` labels are already Mermaid-safe, so a `<br/>` in them survives."""
        opening, closing = SHAPES[shape]
        text = label if escaped else _label(label)
        self.lines.append(f'{"  " * indent}{node_id}{opening}"{text}"{closing}')

    def link(self, source: str, arrow: str, target: str, label: str, style: str) -> None:
        text = f"|{_label(label)}|" if label else ""
        self.lines.append(f"  {source} {arrow}{text} {target}")
        self.styles.append(style)

    def render(self) -> str:
        by_style: dict[str, list[int]] = {}
        for index, style in enumerate(self.styles):
            by_style.setdefault(style, []).append(index)
        styled = [f"  linkStyle {','.join(map(str, idx))} {style}"
                  for style, idx in by_style.items()]
        return "\n".join(self.lines + styled)


def muted(node_ids: list[str]) -> str:
    """Mermaid lines giving non-landing nodes the muted style; '' when there are none."""
    if not node_ids:
        return ""
    return f"\n  {NON_LANDING_CLASS}\n  class {','.join(node_ids)} nonlanding"


def node_name(tax: Taxonomy, technique_id: str) -> str:
    """A node's name for a table, marked when it is not a landing node."""
    name = tax.techniques[technique_id].name
    return name if tax.is_landing(technique_id) else f"{name} ({NOT_LANDING})"


def non_landing_note(tax: Taxonomy | None) -> list[str]:
    if not tax or not tax.non_landing():
        return []
    return [f"Muted, dashed nodes are marked {NOT_LANDING}: they group the tree, and "
            "a novelty audit does not place a scheme at one. A child of such a node "
            "is one too unless its row says `landing: yes`.", ""]


def lineage_style(kind: str) -> str:
    colour = EDGE_STYLE[kind][1]
    return f"stroke:{colour},{LINEAGE_WIDTH},color:{colour}"


def approach_label(ap: Approach, *extra: str) -> str:
    """Name and paper key (and any extra line), escaped, one per line."""
    return "<br/>".join(_label(part) for part in (_short(ap.name), ap.key, *extra))


def is_paper(address: str) -> bool:
    return address.startswith("paper:")


def node_id(address: str) -> str:
    return _sid("paper_", address[len("paper:"):]) if is_paper(address) else _mid(address)


def draw_endpoint(diagram: "Diagram", amap: ApproachMap, address: str, *extra: str) -> None:
    """An approach as a box with name and key; a paper node as a stadium with its key."""
    if is_paper(address):
        label = "<br/>".join(_label(p) for p in (address[len("paper:"):], "(paper)", *extra))
        diagram.node(node_id(address), label, indent=2, shape="stadium", escaped=True)
    else:
        diagram.node(node_id(address), approach_label(amap.approaches[address], *extra),
                     indent=2, escaped=True)


def legend(view: str, inferred: bool) -> list[str]:
    out = ["## Legend", "", "| link | arrow | colour | source |", "| --- | --- | --- | --- |"]
    if view in ("techniques", "both"):
        out.append("| taxonomy (family → technique → approach) | `---` | #9e9e9e, thin | "
                   "technique taxonomy and features table |")
    if view in ("lineage", "both"):
        for kind, (arrow, colour) in EDGE_STYLE.items():
            out.append(f"| {cg.EDGE_LABELS[kind]} | `{arrow}` | {colour}, thick | "
                       "stated by a paper (ledger edge) |")
    if inferred:
        out.append(f"| {INFERRED_LABEL} | `-.-` | #ff8f00, dashed | shared channel, key "
                   "and access_needed; stated by no paper, counted as no edge |")
    return out + [""]


def render_overview_mermaid(amap: ApproachMap, view: str) -> tuple[str, int]:
    """Family subgraphs holding technique nodes (with approach counts) and a node for
    the approaches hung directly under the family. Under lineage or both, lineage
    edges are aggregated between those nodes. Returns (diagram, edges folded inside one node)."""
    diagram = Diagram("LR")
    tax = amap.taxonomy

    def group(address: str) -> str:
        tid = amap.technique(address)
        return technique_node(tid) if tid else family_node(amap.family(address))

    counts = Counter((group(e.source), e.edge_type, group(e.target)) for e in amap.edges) \
        if view in ("lineage", "both") else Counter()
    used = {n for (src, _kind, tgt) in counts for n in (src, tgt)}
    for family in amap.families():
        members = amap.in_family(family)
        sub_id = UNCLASSIFIED if family == UNCLASSIFIED else family_node(family) + "_g"
        diagram.lines.append(f'  subgraph {sub_id}["{_label(family)} ({len(members)})"]')
        direct = [a for a in members if not amap.technique(a)]
        has_techniques = any(tax.family_of(t) == family for t in tax.techniques)
        if direct or not has_techniques or family_node(family) in used:
            diagram.node(family_node(family), f"{family}: {len(direct)} direct", indent=2,
                         shape="round")
        for tid in sorted(t for t in tax.techniques if tax.family_of(t) == family):
            diagram.node(technique_node(tid),
                         f"{_short(tax.techniques[tid].name)} ({amap.subtree_count(tid)})",
                         indent=2)
        diagram.lines.append("  end")
    if view in ("techniques", "both"):
        for tid, tech in sorted(tax.techniques.items()):
            if tech.parent:
                diagram.link(technique_node(tech.parent), "---", technique_node(tid), "",
                             TREE_STYLE)

    folded = 0
    for (src, kind, tgt), n in sorted(counts.items()):
        if src == tgt:
            folded += n
            continue
        label = cg.EDGE_LABELS[kind] + (f" ×{n}" if n > 1 else "")
        diagram.link(src, EDGE_STYLE[kind][0], tgt, label, lineage_style(kind))
    return diagram.render() + muted([technique_node(t) for t in tax.non_landing()]), folded


def render_family_mermaid(amap: ApproachMap, family: str, view: str,
                          inferred: bool) -> str:
    """One family in full: the technique tree with approaches as leaves (techniques,
    both), and lineage and inferred links that touch it. An endpoint in another family
    is a stub node, labelled with its family, in an `other families` subgraph."""
    diagram = Diagram("TD" if view == "techniques" else "LR")
    tax = amap.taxonomy
    members = amap.in_family(family)
    member_set = set(members) | set(amap.papers_in(family))
    tree = view in ("techniques", "both")

    lineage = [e for e in amap.edges if e.source in member_set or e.target in member_set] \
        if view in ("lineage", "both") else []
    pairs: list[tuple[str, str]] = []
    if inferred:
        for group in amap.inferred_groups:
            if member_set & set(group):
                pairs += [(group[0], other) for other in group[1:]]
    external = sorted({a for e in lineage for a in (e.source, e.target)} - member_set
                      | {a for p in pairs for a in p} - member_set)

    diagram.lines.append(f'  subgraph {family_node(family)}_g["{_label(family)}"]')
    if tree:
        diagram.node(family_node(family), family, indent=2, shape="round")
        for tid in sorted(t for t in tax.techniques if tax.family_of(t) == family):
            diagram.node(technique_node(tid), tax.techniques[tid].name, indent=2,
                         shape="hex")
    for address in members:
        draw_endpoint(diagram, amap, address)
    for address in amap.papers_in(family):
        if any(address in (e.source, e.target) for e in lineage):
            draw_endpoint(diagram, amap, address)
    diagram.lines.append("  end")
    if external:
        diagram.lines.append('  subgraph other_families["other families"]')
        for address in external:
            draw_endpoint(diagram, amap, address, f"family: {amap.family(address)}")
        diagram.lines.append("  end")

    if tree:
        for tid in sorted(t for t in tax.techniques if tax.family_of(t) == family):
            parent = tax.techniques[tid].parent
            diagram.link(technique_node(parent) if parent else family_node(family), "---",
                         technique_node(tid), "", TREE_STYLE)
        for address in members:
            for parent in ([technique_node(t) for t in amap.techniques(address)]
                           or [family_node(family)]):
                diagram.link(parent, "---", _mid(address), "", TREE_STYLE)
    for e in lineage:
        diagram.link(node_id(e.source), EDGE_STYLE[e.edge_type][0], node_id(e.target),
                     cg.EDGE_LABELS[e.edge_type], lineage_style(e.edge_type))
    for left, right in pairs:
        diagram.link(node_id(left), "-.-", node_id(right), "inferred", INFERRED_STYLE)
    rendered = diagram.render()
    if external:
        rendered += "\n  " + STUB_CLASS + "\n  class " + \
            ",".join(node_id(a) for a in external) + " stub"
    if tree:
        rendered += muted([technique_node(t) for t in tax.non_landing()
                           if tax.family_of(t) == family])
    return rendered


def approach_table(amap: ApproachMap, addresses: list[str]) -> list[str]:
    """One row per approach. The mechanism and landable columns appear when the
    project keys mechanisms, and carrier and acquisition when the features table has
    those columns, so a table without them renders as it always has."""
    header = ["address", "name", "family", "technique", "channel", "key", "access",
              "capacity"]
    keyed = amap.mechanism_keyed()
    extras = [c for c in ("mechanism_evidence", "carrier", "acquisition")
              if c in amap.columns]
    header += (["mechanism", "landable"] if keyed else []) + extras
    out = ["| " + " | ".join(header) + " |", "| " + " | ".join("---" for _ in header) + " |"]
    for address in addresses:
        row = amap.features.get(address, {})
        values = [f"`{address}`", amap.approaches[address].name, amap.family(address),
                  "; ".join(amap.techniques(address)), row.get("channel", ""),
                  row.get("key", ""), row.get("access_needed", ""), row.get("capacity", "")]
        if keyed:
            values += ["; ".join(amap.mechanisms.get(address, ())),
                       "yes" if amap.landable(address) else "no"]
        values += [row.get(c, "") for c in extras]
        out.append("| " + " | ".join(_cell(v) for v in values) + " |")
    return out


def edge_table(edges: list[MapEdge]) -> list[str]:
    """Every drawn lineage edge; `lifted_from` names the claims an end was lifted from."""
    out = ["| source | kind | target | lifted_from | ledger line |",
           "| --- | --- | --- | --- | --- |"]
    for e in sorted(edges, key=lambda x: (x.source, x.edge_type, x.target)):
        out.append("| " + " | ".join(_cell(v) for v in (
            f"`{e.source}`", cg.EDGE_LABELS[e.edge_type], f"`{e.target}`",
            ", ".join(f"`{a}`" for a in e.lifted_from), ", ".join(e.origin))) + " |")
    return out + [""]


def bullet_section(title: str, items: list[str], code: bool = True) -> list[str]:
    out = [title.format(n=len(items)), ""]
    out += [f"- `{i}`" if code else f"- {i}" for i in items] or ["None."]
    return out + [""]


def render_overview(amap: ApproachMap, sources: str, view: str, inferred: bool,
                    family_files: dict[str, Path]) -> str:
    """The overview body, without its generation time, so two builds of the same
    corpus compare equal and produce no duplicate snapshot."""
    diagram, folded = render_overview_mermaid(amap, view)
    named = [f for f in amap.families() if f != UNCLASSIFIED]
    tax = amap.taxonomy
    out = [
        "# Approach map — overview", "",
        f"Built by `tools/build_approach_map.py` from {sources}. View: `{view}`; "
        f"inferred links: `{'on' if inferred else 'off'}`. Derived: edit the ledgers or "
        "the tables, never this file. Family and technique nodes only; each family's "
        "approaches are in its own file, listed below.", "",
        f"- approaches: {len(amap.approaches)}",
        f"- families: {len(named)}",
        f"- techniques: {len(tax.techniques)}",
        f"- lineage edges drawn: {len(amap.edges)}"
        + (f" ({folded} inside a single node, drawn in the family files)" if folded else ""),
        f"- of which lifted from a non-approach claim: {len(amap.lifted())}",
        f"- paper nodes: {len(amap.papers)}",
        f"- unclassified approaches: {len(amap.unclassified())}",
        f"- edges not placed, no approach claim in the ledger: {len(amap.unplaced)}",
        f"- edges not placed, unresolved: {len(amap.unresolved)}",
        f"- edges whose ends lift onto one approach: {len(amap.folded)}",
    ]
    if inferred:
        out.append(f"- inferred groups: {len(amap.inferred_groups)}")
    out += ["", "```mermaid", diagram, "```", ""]
    out += legend(view, inferred)
    out += ["## Families", "", "| family | techniques | approaches | file |",
            "| --- | --- | --- | --- |"]
    for family in amap.families():
        n_tech = sum(1 for t in tax.techniques if tax.family_of(t) == family)
        out.append(f"| {_cell(family)} | {n_tech} | {len(amap.in_family(family))} | "
                   f"[{family_files[family].name}]({family_files[family].name}) |")
    out += ["", "## Approaches", ""] + approach_table(amap, sorted(amap.approaches)) + [""]
    out += [f"## Lineage edges ({len(amap.edges)})", ""] + edge_table(amap.edges)
    out += bullet_section("## Unclassified approaches ({n})", amap.unclassified())
    out += ["## Edges not placed", ""]
    out += bullet_section("### No approach claim in the ledger ({n})", amap.unplaced)
    out += bullet_section("### Unresolved ({n})", amap.unresolved)
    out += bullet_section("### Both ends lift onto one approach ({n})", amap.folded)
    out += bullet_section("## Techniques with no approaches ({n})", amap.empty_techniques())
    if inferred:
        out += bullet_section("## Inferred groups ({n})",
                              [", ".join(g) for g in amap.inferred_groups])
    warnings = amap.feature_warnings + tax.warnings + amap.placement_warnings
    if amap.mechanism_taxonomy is None:
        warnings += amap.mechanism_warnings
    if warnings:
        out += bullet_section("## Table warnings ({n})", warnings, code=False)
    return "\n".join(out).rstrip("\n") + "\n"


def render_family(amap: ApproachMap, family: str, sources: str, view: str,
                  inferred: bool, overview: Path) -> str:
    tax = amap.taxonomy
    members = amap.in_family(family)
    techs = sorted(t for t in tax.techniques if tax.family_of(t) == family)
    out = [
        f"# Approach map — {family}", "",
        f"Built by `tools/build_approach_map.py` from {sources}. View: `{view}`. "
        f"Overview: [{overview.name}]({overview.name}).", "",
        f"- approaches: {len(members)}", f"- techniques: {len(techs)}", "",
        "```mermaid", render_family_mermaid(amap, family, view, inferred), "```", "",
    ]
    out += legend(view, inferred)
    if any(tax.family_of(t) == family for t in tax.non_landing()):
        out += non_landing_note(tax)
    if techs:
        out += ["## Techniques", "",
                "| technique | parent | name | definition | grounded by | approaches |",
                "| --- | --- | --- | --- | --- | --- |"]
        for tid in techs:
            t = tax.techniques[tid]
            out.append("| " + " | ".join(_cell(v) for v in (
                f"`{tid}`", t.parent or "", node_name(tax, tid), t.definition,
                f"`{t.grounded_by}`" if t.grounded_by else "",
                str(amap.subtree_count(tid)))) + " |")
        out.append("")
    touching = [e for e in amap.edges if amap.family(e.source) == family
                or amap.family(e.target) == family]
    out += [f"## Lineage edges ({len(touching)})", ""] + edge_table(touching)
    out += ["## Approaches", ""] + approach_table(amap, members)
    return "\n".join(out) + "\n"


# --- the mechanism tree -----------------------------------------------------------

def class_node(mech_class: str) -> str:
    return _sid("cls_", mech_class)


def mechanism_node(mechanism_id: str) -> str:
    return _sid("mech_", mechanism_id)


def mechanism_table(amap: ApproachMap, mechanism_ids: list[str]) -> list[str]:
    mtax = amap.mechanism_taxonomy
    assert mtax is not None
    out = ["| mechanism | parent | class | name | definition | grounded by | landing | "
           "approaches |", "| --- | --- | --- | --- | --- | --- | --- | --- |"]
    for mid in mechanism_ids:
        m = mtax.techniques[mid]
        out.append("| " + " | ".join(_cell(v) for v in (
            f"`{mid}`", m.parent or "", mtax.family_of(mid), node_name(mtax, mid),
            m.definition, f"`{m.grounded_by}`" if m.grounded_by else "",
            "yes" if mtax.is_landing(mid) else "no",
            str(amap.mech_count(mid)))) + " |")
    return out + [""]


def render_mechanism_overview_mermaid(amap: ApproachMap) -> str:
    """Class subgraphs holding mechanism nodes with approach counts, and the tree."""
    mtax = amap.mechanism_taxonomy
    assert mtax is not None
    diagram = Diagram("LR")
    for mech_class in mtax.classes():
        diagram.lines.append(f'  subgraph {class_node(mech_class)}_g["{_label(mech_class)} '
                             f'({len(amap.mech_members(mech_class))})"]')
        for mid in mtax.in_class(mech_class):
            diagram.node(mechanism_node(mid),
                         f"{_short(mtax.techniques[mid].name)} ({amap.mech_count(mid)})",
                         indent=2)
        diagram.lines.append("  end")
    for mid, m in sorted(mtax.techniques.items()):
        if m.parent:
            diagram.link(mechanism_node(m.parent), "---", mechanism_node(mid), "",
                         TREE_STYLE)
    return diagram.render() + muted([mechanism_node(m) for m in mtax.non_landing()])


def render_class_mermaid(amap: ApproachMap, mech_class: str) -> str:
    """One mechanism class: its tree, with every approach placed in it as a leaf under
    each of its nodes in the class. A leaf names its paper family, so leaves from
    different families under one node read as sharing a mechanism."""
    mtax = amap.mechanism_taxonomy
    assert mtax is not None
    nodes = mtax.in_class(mech_class)
    members = amap.mech_members(mech_class)
    diagram = Diagram("TD")
    diagram.lines.append(f'  subgraph {class_node(mech_class)}_g["{_label(mech_class)}"]')
    diagram.node(class_node(mech_class), mech_class, indent=2, shape="round")
    for mid in nodes:
        diagram.node(mechanism_node(mid), mtax.techniques[mid].name, indent=2, shape="hex")
    for address in members:
        diagram.node(_mid(address), approach_label(amap.approaches[address],
                                                   f"family: {amap.family(address)}"),
                     indent=2, escaped=True)
    diagram.lines.append("  end")
    for mid in nodes:
        parent = mtax.techniques[mid].parent
        diagram.link(mechanism_node(parent) if parent else class_node(mech_class), "---",
                     mechanism_node(mid), "", TREE_STYLE)
    for address in members:
        for mid in amap.mechanisms[address]:
            if mid in nodes:
                diagram.link(mechanism_node(mid), "---", _mid(address), "", TREE_STYLE)
    return diagram.render() + muted([mechanism_node(m) for m in mtax.non_landing()
                                     if m in nodes])


def render_mechanism_overview(amap: ApproachMap, sources: str,
                              class_files: dict[str, Path], overview: Path) -> str:
    mtax = amap.mechanism_taxonomy
    assert mtax is not None
    placed = [a for a in sorted(amap.approaches) if amap.mechanisms.get(a)]
    shared = amap.shared_mechanisms()
    out = [
        "# Approach map — mechanisms", "",
        f"Built by `tools/build_approach_map.py` from {sources}. Derived: edit the "
        "ledgers or the tables, never this file. A mechanism class groups approaches "
        "by how they hide bits, across paper families; each class's approaches are in "
        f"its own file, listed below. Family overview: [{overview.name}]({overview.name}).",
        "",
        f"- mechanism classes: {len(mtax.classes())}",
        f"- mechanism nodes: {len(mtax.techniques)} ({len(mtax.non_landing())} "
        "non-landing)",
        f"- approaches with a mechanism placement: {len(placed)}",
        f"- landable approaches: {sum(1 for a in amap.approaches if amap.landable(a))}",
        f"- approaches with no mechanism: {len(amap.unmechanised())}",
        f"- mechanism nodes shared across families: {len(shared)}",
        f"- mechanisms with no approaches: {len(amap.empty_mechanisms())}",
        f"- landing leaves with no published evidence: {len(coverage_gaps(amap))}",
        "", "```mermaid", render_mechanism_overview_mermaid(amap), "```", "",
    ]
    out += non_landing_note(mtax)
    out += ["## Mechanism classes", "",
            "| class | mechanisms | approaches | families | file |",
            "| --- | --- | --- | --- | --- |"]
    for mech_class in mtax.classes():
        members = amap.mech_members(mech_class)
        fams = sorted({amap.family(a) for a in members})
        name = class_files[mech_class].name
        out.append(f"| {_cell(mech_class)} | {len(mtax.in_class(mech_class))} | "
                   f"{len(members)} | {_cell(', '.join(fams))} | [{name}]({name}) |")
    out += ["", "## Mechanisms", ""] + mechanism_table(amap, sorted(mtax.techniques))
    out += ["## Mechanism nodes shared across families", "",
            "| mechanism | families |", "| --- | --- |"]
    out += [f"| `{mid}` | {_cell(', '.join(fams))} |" for mid, fams in shared] or ["None."]
    out += ["", "## Approaches", ""] + approach_table(amap, sorted(amap.approaches)) + [""]
    out += bullet_section("## Approaches with no mechanism ({n})", amap.unmechanised())
    out += bullet_section("## Mechanisms with no approaches ({n})", amap.empty_mechanisms())
    out += bullet_section("## Landing leaves with no published evidence ({n})",
                          coverage_gaps(amap), code=False)
    warnings = mechanism_warnings(amap)
    if warnings:
        out += bullet_section("## Table warnings ({n})", warnings, code=False)
    return "\n".join(out).rstrip("\n") + "\n"


def render_class(amap: ApproachMap, mech_class: str, sources: str, mech_overview: Path) -> str:
    mtax = amap.mechanism_taxonomy
    assert mtax is not None
    members = amap.mech_members(mech_class)
    fams = sorted({amap.family(a) for a in members})
    out = [
        f"# Approach map — mechanism class {mech_class}", "",
        f"Built by `tools/build_approach_map.py` from {sources}. Mechanism overview: "
        f"[{mech_overview.name}]({mech_overview.name}). Each approach leaf names its paper "
        "family.", "",
        f"- mechanisms: {len(mtax.in_class(mech_class))}",
        f"- approaches: {len(members)}",
        f"- families: {len(fams)}" + (f" ({', '.join(fams)})" if fams else ""), "",
        "```mermaid", render_class_mermaid(amap, mech_class), "```", "",
    ]
    if any(m in mtax.non_landing() for m in mtax.in_class(mech_class)):
        out += non_landing_note(mtax)
    out += ["## Mechanisms", ""] + mechanism_table(amap, mtax.in_class(mech_class))
    out += ["## Approaches", ""] + approach_table(amap, members)
    return "\n".join(out) + "\n"


# --- the novelty-audit lookup -----------------------------------------------------

@dataclass(frozen=True)
class GroundingRecord:
    """A mechanism node's grounded_by claim, listed beside the approach rows: the
    published evidence a node can have when no approach row sits at it. `quote` is
    the claim's quoted text when the ledger can be read; `problem` says why not."""
    node: str
    address: str
    quote: str = ""
    problem: str = ""


@dataclass
class NeighbourLevel:
    """What is newly reached at one step up from the queried node: the node's own
    subtree first, then each ancestor's, then the rest of its class. `approaches`
    are approach rows; `groundings` are the grounded_by claims of the landing nodes
    newly in scope, kept apart so a judge can tell the two kinds of record apart."""
    distance: int
    scope: str
    approaches: list[tuple[str, tuple[str, ...]]]
    groundings: list[GroundingRecord] = field(default_factory=list)


def grounding_record(amap: ApproachMap, mechanism_id: str) -> GroundingRecord | None:
    """The node's grounded_by claim as a record; None when the node names none."""
    mtax = amap.mechanism_taxonomy
    assert mtax is not None
    grounded_by = mtax.techniques[mechanism_id].grounded_by
    if not grounded_by:
        return None
    res = grounding_resolution(amap, mechanism_id)
    if res is None:
        return GroundingRecord(mechanism_id, grounded_by.lower(),
                               problem="not a key:slug address")
    address = f"{res.key}:{res.address.slug}"
    if not res.exists or res.ledger_path is None:
        return GroundingRecord(mechanism_id, address, problem=res.reason)
    quote = cg.claim_quote(res.ledger_path, res.address.slug)
    return GroundingRecord(mechanism_id, address, quote,
                           "" if quote else "the claim carries no quote")


def neighbours(amap: ApproachMap, mechanism_id: str) -> tuple[list[NeighbourLevel], int]:
    """The levels for one mechanism id, nearest first, each approach listed once at
    the nearest level where it has a landable placement, with the nodes it sits at,
    and each landing node's grounding claim listed once at the level that first
    takes the node in, the queried node's own first. Non-landing nodes contribute no
    grounding record, since a scheme is never judged against them. Also returns how
    many approaches were reached only through non-landing nodes."""
    mtax = amap.mechanism_taxonomy
    assert mtax is not None and mechanism_id in mtax.techniques
    chain = [mechanism_id, *mtax.ancestors(mechanism_id)]
    mech_class = mtax.family_of(mechanism_id)
    scopes = [(node, {node, *mtax.descendants(node)}) for node in chain]
    scopes.append((f"class {mech_class}", set(mtax.in_class(mech_class))))
    seen: set[str] = set()
    grounded: set[str] = set()
    reached_unlandable: set[str] = set()
    levels: list[NeighbourLevel] = []
    for distance, (scope, nodes) in enumerate(scopes):
        found = []
        for address in sorted(amap.mechanisms):
            inside = [m for m in amap.mechanisms[address] if m in nodes]
            at = tuple(m for m in inside if mtax.is_landing(m))
            if at and address not in seen:
                seen.add(address)
                found.append((address, at))
            elif inside and not at:
                reached_unlandable.add(address)
        new_nodes = sorted(nodes - grounded, key=lambda m: (m != scope, m))
        grounded |= nodes
        records = [grounding_record(amap, m) for m in new_nodes if mtax.is_landing(m)]
        levels.append(NeighbourLevel(distance, scope, found,
                                     [r for r in records if r is not None]))
    return levels, len(reached_unlandable - seen)


def render_neighbours(amap: ApproachMap, mechanism_ids: list[str]) -> str:
    mtax = amap.mechanism_taxonomy
    assert mtax is not None
    out: list[str] = []
    if len(mechanism_ids) > 1:
        out += [f"Component retrieval: {len(mechanism_ids)} mechanism ids, one section per "
                "component. This lookup does not assess the composition: a scheme that "
                "combines these components is not thereby covered by any one section.", ""]
    for mid in mechanism_ids:
        node = mtax.techniques[mid]
        note = "" if mtax.is_landing(mid) else f" — {NOT_LANDING}"
        out.append(f"## {mid} — {node.name} (class {mtax.family_of(mid)}){note}")
        levels, unlandable = neighbours(amap, mid)
        for level in levels:
            if level.distance == 0:
                where = f"at {mid} and below"
            elif level.scope.startswith("class "):
                where = f"elsewhere in {level.scope}"
            else:
                where = f"under ancestor {level.scope}"
            out.append(f"distance {level.distance}, {where}: {len(level.approaches)} "
                       f"approach row(s), {len(level.groundings)} grounding claim(s)")
            if level.approaches:
                out.append("  approach rows:")
            for address, at in level.approaches:
                row = amap.features.get(address, {})
                out.append("    " + " | ".join((
                    address, f"family: {amap.family(address)}",
                    f"carrier: {row.get('carrier', '') or '—'}",
                    f"acquisition: {row.get('acquisition', '') or '—'}",
                    f"at: {'; '.join(at)}",
                    f"evidence: {'; '.join(amap.evidence(address, m) for m in at)}")))
            if level.groundings:
                out.append("  grounding claims:")
            for rec in level.groundings:
                also = " (also an approach row)" if rec.address in amap.approaches else ""
                text = f'"{rec.quote}"' if rec.quote else f"quote not read: {rec.problem}"
                out.append(f"    {rec.address} | grounds: {rec.node}{also} | {text}")
        if unlandable:
            out.append(f"not listed: {unlandable} approach(es) placed here only at "
                       f"nodes marked {NOT_LANDING}")
        out.append("")
    out.append("Outcomes a novelty judge records: " + " · ".join(VERDICT_OUTCOMES)
               + ". This lookup names neighbours only and issues no verdict.")
    out.append(BROAD_MATCH_NOTE)
    return "\n".join(out) + "\n"


# --- live files and snapshots ---------------------------------------------------

def with_header(body: str, generated: str) -> str:
    return f"---\ngenerated: {generated}\n---\n\n{body}"


def strip_header(text: str) -> str:
    """The compared content of a map file: everything after the frontmatter."""
    return FRONTMATTER_RE.sub("", text, count=1).lstrip("\n")


def snapshot_re(stem: str) -> re.Pattern[str]:
    return re.compile(rf"^{re.escape(stem)}_(\d{{8}})([a-z]?)\.md$")


def newest_snapshot(live: Path) -> Path | None:
    """The latest <stem>_YYYYMMDD[a-z].md beside the live file, by date then suffix."""
    if not live.parent.is_dir():
        return None
    pattern = snapshot_re(live.stem)
    found = [(m.group(1), m.group(2), p) for p in live.parent.glob(f"{live.stem}_*.md")
             if (m := pattern.match(p.name))]
    return max(found)[2] if found else None


def snapshot_candidates(live: Path, today: str) -> list[Path]:
    """Today's free snapshot names in order: the bare date, then a…z after the
    highest suffix already used today."""
    pattern = snapshot_re(live.stem)
    used = [m.group(2) for p in live.parent.glob(f"{live.stem}_{today}*.md")
            if (m := pattern.match(p.name)) and m.group(1) == today] \
        if live.parent.is_dir() else []
    if not used:
        suffixes = [""] + [chr(c) for c in range(ord("a"), ord("z") + 1)]
    else:
        start = ord(max(used)) + 1 if max(used) else ord("a")
        suffixes = [chr(c) for c in range(start, ord("z") + 1)]
    return [live.with_name(f"{live.stem}_{today}{s}.md") for s in suffixes]


def write_snapshot(live: Path, text: str, today: str) -> Path:
    """Create the next free snapshot with mode 'x', so an existing one is never
    overwritten. Raises FileExistsError when today's names are exhausted."""
    for candidate in snapshot_candidates(live, today):
        try:
            with candidate.open("x", encoding="utf-8") as handle:
                handle.write(text)
            return candidate
        except FileExistsError:
            continue
    raise FileExistsError(f"no free snapshot name left for {today} beside {live}")


def snapshot_needed(live: Path, body: str) -> bool:
    newest = newest_snapshot(live)
    return newest is None or strip_header(newest.read_text(encoding="utf-8")) != body


def publish(live: Path, body: str, generated: str, today: str, dry_run: bool) -> None:
    """Write the live file if its content changed and a snapshot if the content
    differs from the newest one. Under dry_run, report what would happen."""
    live_changed = not (live.is_file()
                        and strip_header(live.read_text(encoding="utf-8")) == body)
    needs_snapshot = snapshot_needed(live, body)
    if dry_run:
        candidates = snapshot_candidates(live, today)
        snap = str(candidates[0]) if needs_snapshot and candidates else "none"
        log_info(f"dry run — {live} ({'would update' if live_changed else 'unchanged'}); "
                 f"snapshot: {snap}")
        return
    text = with_header(body, generated)
    live.parent.mkdir(parents=True, exist_ok=True)
    if live_changed:
        live.write_text(text, encoding="utf-8")
        log_info(f"wrote {live}")
    else:
        log_info(f"unchanged: {live}")
    if needs_snapshot:
        log_info(f"wrote snapshot {write_snapshot(live, text, today)}")


def family_files(live: Path, families: list[str], infix: str = "") -> dict[str, Path]:
    """<stem>_<infix><family>.md beside the overview; a slug two families share gets
    a numeric suffix so neither file overwrites the other. Mechanism classes use the
    infix `mech_`."""
    out: dict[str, Path] = {}
    used: set[str] = set()
    for family in families:
        slug = family_slug(family)
        candidate, n = slug, 2
        while candidate in used:
            candidate, n = f"{slug}_{n}", n + 1
        used.add(candidate)
        out[family] = live.with_name(f"{live.stem}_{infix}{candidate}.md")
    return out


def add_source_args(ap: argparse.ArgumentParser) -> None:
    ap.add_argument("--root", default=str(REPO_ROOT),
                    help="project root; relative config paths resolve against it")
    ap.add_argument("--claims-dir", default=None,
                    help="override verified_claims/ (default <root>/literature/verified_claims)")
    ap.add_argument("--config", default=None,
                    help="override ledger.config.md (default <root>/ledger.config.md)")
    ap.add_argument("--features", default=None, help="override approach_features:")
    ap.add_argument("--taxonomy", default=None, help="override technique_taxonomy:")
    ap.add_argument("--mechanisms", default=None, help="override mechanism_taxonomy:")


@dataclass
class Sources:
    root: Path
    claims_dir: Path
    config: dict[str, str]
    features: Path
    taxonomy: Path
    mechanisms: Path


def resolve_sources(args: argparse.Namespace) -> Sources:
    root = Path(args.root).expanduser().resolve()
    claims_dir = Path(args.claims_dir) if args.claims_dir else \
        root / "literature" / "verified_claims"
    config = parse_config(Path(args.config) if args.config else root / "ledger.config.md")

    def path_arg(value: str | None, key: str, default: str) -> Path:
        return Path(value).expanduser() if value else \
            config_path_value(config, key, default, root)

    return Sources(root, claims_dir, config,
                   path_arg(args.features, "approach_features", DEFAULT_FEATURES),
                   path_arg(args.taxonomy, "technique_taxonomy", DEFAULT_TAXONOMY),
                   path_arg(args.mechanisms, "mechanism_taxonomy", DEFAULT_MECHANISMS))


def report_errors(amap: ApproachMap, src: Sources) -> bool:
    """Log every taxonomy error; True when there was one and nothing may be written."""
    errors = taxonomy_errors(amap)
    for problem in errors:
        log_error(problem)
    if errors:
        mech_bad = bool(amap.mechanism_taxonomy and amap.mechanism_taxonomy.errors)
        where = [f"the technique taxonomy {src.taxonomy}"] if amap.taxonomy.errors else []
        where += [f"the mechanism taxonomy {src.mechanisms}"] if mech_bad else []
        where += [f"the features table {src.features}"] if amap.placement_errors else []
        log_error(f"{len(errors)} error(s) in {' and '.join(where)} — no map written.")
    return bool(errors)


def load_mechanism_map(src: Sources) -> ApproachMap | None:
    """The map for a lookup subcommand, its warnings logged; None (errors logged)
    when the claims, the mechanism taxonomy or the tables cannot be read."""
    if not src.claims_dir.is_dir():
        log_error(f"claims directory not found: {src.claims_dir}")
        return None
    if not src.mechanisms.is_file():
        log_error(f"mechanism taxonomy not found: {src.mechanisms}")
        return None
    try:
        amap = build_map(src.claims_dir, src.features, src.taxonomy,
                         mechanism_path=src.mechanisms)
    except (OSError, ValueError, csv.Error) as exc:
        log_error(f"approach map not read: {exc}")
        return None
    if report_errors(amap, src):
        return None
    for warning in amap.feature_warnings + mechanism_warnings(amap):
        log_warning(warning)
    return amap


def check_coverage_main(argv: list[str]) -> int:
    """`check-coverage`: exit 1 when a landing leaf of the mechanism tree has neither
    an approach row nor a grounding claim that resolves, 0 when every one has."""
    ap = argparse.ArgumentParser(
        prog="build_approach_map.py check-coverage",
        description="Fail when a landing leaf of the mechanism tree has no approach row "
                    "and no resolvable grounded_by claim: the lookup would find nothing "
                    "published there, which reads as false novelty.")
    add_source_args(ap)
    src = resolve_sources(ap.parse_args(argv))
    amap = load_mechanism_map(src)
    if amap is None:
        return 1
    mtax = amap.mechanism_taxonomy
    assert mtax is not None
    leaves = [m for m in mtax.techniques if mtax.is_landing(m) and not mtax.descendants(m)]
    gaps = coverage_gaps(amap)
    for gap in gaps:
        log_error(gap)
    if gaps:
        log_error(f"{len(gaps)} of {len(leaves)} landing leaf/leaves in {src.mechanisms} "
                  "have no published evidence in the map.")
        return 1
    log_info(f"all {len(leaves)} landing leaf/leaves in {src.mechanisms} have an approach "
             "row or a grounding claim.")
    return 0


def neighbours_main(argv: list[str]) -> int:
    """`neighbours <mechanism_id> [...]`: print the landable approaches nearest each
    node, for a novelty judge to name the nearest published approach."""
    ap = argparse.ArgumentParser(
        prog="build_approach_map.py neighbours",
        description="List the landable approaches under each mechanism node and its "
                    "ancestors, nearest first. Reports neighbours only; no verdict.")
    ap.add_argument("mechanism_ids", nargs="+", metavar="mechanism_id")
    add_source_args(ap)
    args = ap.parse_args(argv)
    src = resolve_sources(args)
    amap = load_mechanism_map(src)
    if amap is None:
        return 1
    mtax = amap.mechanism_taxonomy
    assert mtax is not None
    wanted = [m.lower() for m in args.mechanism_ids]
    unknown = [m for m in wanted if m not in mtax.techniques]
    if unknown:
        log_error(f"unknown mechanism id(s): {', '.join(unknown)} — not in {src.mechanisms}")
        return 1
    log_info(f"{len(amap.approaches)} approach claim(s); {len(mtax.techniques)} mechanism "
             f"node(s) in {src.mechanisms}")
    print(render_neighbours(amap, wanted), end="")
    return 0


def main(argv: list[str] | None = None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    if argv and argv[0] == "neighbours":
        return neighbours_main(argv[1:])
    if argv and argv[0] == "check-coverage":
        return check_coverage_main(argv[1:])
    ap = argparse.ArgumentParser(
        description="Render the approach map from the ledgers. "
                    "`neighbours <mechanism_id> [...]` runs the novelty-audit lookup; "
                    "`check-coverage` fails on a landing leaf with no published evidence.")
    add_source_args(ap)
    ap.add_argument("--view", choices=VIEWS, default=None, help="override approach_map_view:")
    ap.add_argument("--out", default=None, help="override approach_map_out:")
    ap.add_argument("--dry-run", action="store_true",
                    help="print counts and target paths; write nothing")
    args = ap.parse_args(argv)

    src = resolve_sources(args)
    root, claims_dir, config = src.root, src.claims_dir, src.config
    features_path, taxonomy_path = src.features, src.taxonomy
    live = Path(args.out).expanduser() if args.out else \
        config_path_value(config, "approach_map_out", DEFAULT_OUT, root)
    view = args.view or config_choice(config, "approach_map_view", VIEWS, DEFAULT_VIEW)
    inferred = config_choice(config, "inferred_links", ("off", "on"), "off") == "on"

    if not claims_dir.is_dir():
        log_error(f"claims directory not found: {claims_dir}")
        return 1
    try:
        amap = build_map(claims_dir, features_path, taxonomy_path, view, inferred,
                         src.mechanisms)
    except (OSError, ValueError, csv.Error) as exc:
        log_error(f"approach map not built: {exc}")
        return 1

    tax = amap.taxonomy
    mtax = amap.mechanism_taxonomy
    if report_errors(amap, src):
        return 1
    warnings = amap.feature_warnings + tax.warnings + amap.placement_warnings \
        + mechanism_warnings(amap)
    for warning in warnings:
        log_warning(warning)
    if not amap.approaches:
        log_warning(f"No approach claims found in {claims_dir} (no **ID:** slug starts "
                    f"with {' or '.join(APPROACH_PREFIXES)}) — no map written.")
        return 0

    unclassified = amap.unclassified()
    empty = amap.empty_techniques()
    log_info(f"view {view}; {len(amap.approaches)} approach claim(s) in "
             f"{len(amap.families())} family file(s), {len(tax.techniques)} technique(s), "
             f"{len(amap.edges)} lineage edge(s) drawn ({len(amap.lifted())} lifted from a "
             f"non-approach claim), {len(amap.papers)} paper node(s), "
             f"{len(unclassified)} unclassified; not placed: {len(amap.unplaced)} with no "
             f"approach claim in the ledger, {len(amap.unresolved)} unresolved, "
             f"{len(amap.folded)} lifting onto one approach"
             + (f"; {len(amap.inferred_groups)} inferred group(s)" if inferred else "") + ".")
    if mtax is not None:
        log_info(f"mechanisms: {len(mtax.classes())} class file(s), {len(mtax.techniques)} "
                 f"node(s) ({len(mtax.non_landing())} non-landing), "
                 f"{len(amap.unmechanised())} approach(es) with no mechanism.")
    if warnings:
        log_warning(f"{len(warnings)} table warning(s), listed above and in the overview.")
    if unclassified:
        log_warning(f"{len(unclassified)} approach(es) have no family in {features_path}: "
                    + preview(unclassified))
    if empty:
        log_warning(f"{len(empty)} technique(s) have no approaches: " + preview(empty))
    if mtax is not None and amap.empty_mechanisms():
        log_warning(f"{len(amap.empty_mechanisms())} mechanism(s) have no approaches: "
                    + preview(amap.empty_mechanisms()))
    gaps = coverage_gaps(amap)
    if gaps:
        log_warning(f"{len(gaps)} landing leaf/leaves have no approach row and no "
                    "grounding claim, so the lookup reads them as unpublished; "
                    "`check-coverage` fails on them: "
                    + preview([g.split(":", 1)[0] for g in gaps]))
    if amap.unplaced:
        log_warning(f"{len(amap.unplaced)} edge(s) end in a ledger with no approach claim; "
                    "listed in the overview.")
    if amap.unresolved:
        log_warning(f"{len(amap.unresolved)} edge(s) do not resolve; "
                    "listed in the overview.")

    sources = (f"`{claims_dir}`, the features table `{features_path}` and the technique "
               f"taxonomy `{taxonomy_path}`")
    files = family_files(live, amap.families())
    outputs = [(live, render_overview(amap, sources, view, inferred, files))]
    outputs += [(path, render_family(amap, family, sources, view, inferred, live))
                for family, path in files.items()]
    if mtax is not None:
        mech_sources = (f"`{claims_dir}`, the features table `{features_path}` and the "
                        f"mechanism taxonomy `{src.mechanisms}`")
        mech_live = live.with_name(f"{live.stem}_{MECH_OVERVIEW_SUFFIX}.md")
        class_files = family_files(live, mtax.classes(), MECH_FILE_INFIX)
        outputs.append((mech_live, render_mechanism_overview(amap, mech_sources,
                                                             class_files, live)))
        outputs += [(path, render_class(amap, mech_class, mech_sources, mech_live))
                    for mech_class, path in class_files.items()]
    clashes = sorted(p.name for p, n in Counter(p for p, _ in outputs).items() if n > 1)
    if clashes:
        log_error(f"two maps would share a file name: {', '.join(clashes)} — rename a "
                  "family or mechanism class; no map written.")
        return 1
    generated = dt.datetime.now().astimezone().isoformat(timespec="seconds")
    today = dt.date.today().strftime("%Y%m%d")
    if args.dry_run:
        log_info(f"dry run — features table: {features_path}; taxonomy: {taxonomy_path}"
                 + (f"; mechanism taxonomy: {src.mechanisms}" if mtax is not None else ""))
    try:
        for path, body in outputs:
            publish(path, body, generated, today, args.dry_run)
    except OSError as exc:
        log_error(f"approach map not written: {exc}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
