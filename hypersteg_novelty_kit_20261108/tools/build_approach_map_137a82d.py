# === SCRIPT: Build the approach map — every published approach as one network ===
# Purpose: a derived, human-facing view of the approach claims in the corpus. An
#          approach is a claim whose **ID:** slug starts with `approach-` (a scheme a
#          paper proposes) or `surveyed-` (a scheme a survey describes). Families and
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
# Views  : approach_map_view: lineage (paper-stated edges between approaches) |
#          techniques (the taxonomy tree, approaches as leaves) | both (the tree with
#          the lineage edges overlaid). inferred_links: on adds dashed links between
#          approaches sharing channel, key and access_needed; they are drawn only, and
#          never counted as edges.
# INPUTS : literature/verified_claims/<key>.md ledgers; `approach_features:` (default
#          maps/approach_features.tsv) and `technique_taxonomy:` (default
#          maps/technique_taxonomy.tsv) from ledger.config.md.
# OUTPUTS: an overview at `approach_map_out:` (default maps/approach_map.md) holding
#          family and technique nodes only, and one <stem>_<family>.md per family with
#          the full tree and its approaches. Each file is a live file plus a snapshot
#          <name>_YYYYMMDD[a-z].md, written only when its content changes.
#          Exit 0 = built, or nothing to build (stated as a warning); 1 = error.
# Run    : python3 tools/build_approach_map.py             # write the maps
#          python3 tools/build_approach_map.py --dry-run   # counts and target paths only
#          python3 tools/build_approach_map.py --out /path/to/approach_map.md
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
DEFAULT_OUT = "maps/approach_map.md"
VIEWS = ("lineage", "techniques", "both")
DEFAULT_VIEW = "lineage"
FEATURE_COLUMNS = ("address", "approach", "family", "carrier_medium", "channel", "key",
                   "access_needed", "capacity", "security_notion", "robustness",
                   "pre_coordination", "builds_on", "evidence_slugs", "notes")
OPTIONAL_FEATURE_COLUMNS = ("technique",)
TAXONOMY_COLUMNS = ("technique_id", "parent_id", "family", "name", "definition",
                    "grounded_by", "notes")
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
    """One taxonomy row. `parent` is None for a top-level technique in its family."""
    technique_id: str
    parent: str | None
    family: str
    name: str
    definition: str
    grounded_by: str
    line_no: int


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


@dataclass
class ApproachMap:
    """Everything the renderer needs, plus the lists that keep nothing silent."""
    approaches: dict[str, Approach]
    features: dict[str, dict[str, str]]
    taxonomy: Taxonomy
    placement: dict[str, tuple[str, str | None]] = field(default_factory=dict)
    by_key: dict[str, list[str]] = field(default_factory=dict)
    papers: set[str] = field(default_factory=set)
    edges: list[MapEdge] = field(default_factory=list)
    unplaced: list[str] = field(default_factory=list)
    unresolved: list[str] = field(default_factory=list)
    folded: list[str] = field(default_factory=list)
    feature_warnings: list[str] = field(default_factory=list)
    placement_warnings: list[str] = field(default_factory=list)
    inferred_groups: list[list[str]] = field(default_factory=list)

    def family(self, address: str) -> str:
        return self.placement[address][0]

    def technique(self, address: str) -> str | None:
        return self.placement[address][1]

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
        return sum(1 for a in self.approaches if (t := self.technique(a)) and
                   (t == technique_id or technique_id in self.taxonomy.ancestors(t)))

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


def read_tsv(path: Path, label: str, required: tuple[str, ...],
             expected: tuple[str, ...]) -> tuple[list[tuple[int, dict[str, str]]], list[str]]:
    """(line number, stripped row) pairs and header warnings. Raises ValueError when a
    required column is missing: such a table cannot be read at all."""
    warnings: list[str] = []
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        header = [h.strip() for h in (reader.fieldnames or [])]
        missing_required = [c for c in required if c not in header]
        if missing_required:
            raise ValueError(f"{label} {path} lacks column(s) {', '.join(missing_required)}")
        missing = [c for c in expected if c not in header]
        extra = [c for c in header if c not in expected and c not in OPTIONAL_FEATURE_COLUMNS]
        if missing or extra:
            warnings.append(f"{label} header differs from the expected one — missing: "
                            f"{', '.join(missing) or 'none'}; extra: {', '.join(extra) or 'none'}")
        rows = [(line_no, {(k or "").strip(): (v or "").strip()
                           for k, v in raw.items() if k is not None})
                for line_no, raw in enumerate(reader, start=2)]
    return rows, warnings


def load_features(path: Path, approaches: dict[str, Approach]
                  ) -> tuple[dict[str, dict[str, str]], list[str]]:
    """Feature rows keyed by lower-cased address, and the warnings raised reading them.
    A missing table is a warning (every approach is then unclassified)."""
    if not path.is_file():
        return {}, [f"features table not found: {path} — every approach is unclassified"]
    rows, warnings = read_tsv(path, "features table", ("address", "family"), FEATURE_COLUMNS)
    features: dict[str, dict[str, str]] = {}
    for line_no, row in rows:
        address = row.get("address", "").lower()
        if not address:
            warnings.append(f"features table line {line_no}: empty address, skipped")
            continue
        if address in features:
            warnings.append(f"features table line {line_no}: duplicate row for "
                            f"{address}, first kept")
            continue
        if address not in approaches:
            warnings.append(f"features table line {line_no}: {address} names no approach claim")
        features[address] = row
    return features, warnings


def load_taxonomy(path: Path, claims_dir: Path, needed: bool) -> Taxonomy:
    """The technique tree. An unknown parent or a parent cycle is an error; a missing
    or unresolvable grounded_by is a warning. A missing file is a warning only when
    the view or the features table needs it."""
    tax = Taxonomy()
    if not path.is_file():
        if needed:
            tax.warnings.append(f"technique taxonomy not found: {path} — approaches "
                                "hang directly under their family")
        return tax
    rows, tax.warnings = read_tsv(path, "technique taxonomy", ("technique_id", "family"),
                                  TAXONOMY_COLUMNS)
    for line_no, row in rows:
        tid = row.get("technique_id", "").lower()
        if not tid:
            tax.warnings.append(f"technique taxonomy line {line_no}: empty technique_id, "
                                "skipped")
            continue
        if tid in tax.techniques:
            tax.warnings.append(f"technique taxonomy line {line_no}: duplicate "
                                f"technique_id {tid}, first kept")
            continue
        tax.techniques[tid] = Technique(
            tid, row.get("parent_id", "").lower() or None, row.get("family", ""),
            row.get("name", "") or tid, row.get("definition", ""),
            row.get("grounded_by", ""), line_no)

    for tech in tax.techniques.values():
        if tech.parent and tech.parent not in tax.techniques:
            tax.errors.append(f"technique {tech.technique_id} (line {tech.line_no}): "
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
            tax.warnings.append(f"technique {tech.technique_id}: family '{tech.family}' "
                                f"differs from its root's '{root_family}'; drawn under the root's")
        if not tech.grounded_by:
            tax.warnings.append(f"technique {tech.technique_id}: no grounded_by claim")
            continue
        address = cg.parse_address(tech.grounded_by)
        if address.key is None:
            tax.warnings.append(f"technique {tech.technique_id}: grounded_by "
                                f"'{tech.grounded_by}' is not a key:slug address")
            continue
        res = cg.resolve(address, address.key, claims_dir)
        if not res.exists:
            tax.warnings.append(f"technique {tech.technique_id}: grounded_by "
                                f"'{tech.grounded_by}' does not resolve — {res.reason}")
    return tax


def place_approaches(amap: ApproachMap) -> None:
    """Each approach's (family, technique). The features row's family wins; a row with
    a technique but no family takes the technique's family. An unknown technique, or
    one from another family, leaves the approach directly under its family."""
    tax = amap.taxonomy
    for address in sorted(amap.approaches):
        row = amap.features.get(address, {})
        family = row.get("family", "")
        tid = row.get("technique", "").lower() or None
        if tid and tid not in tax.techniques:
            amap.placement_warnings.append(f"{address}: unknown technique_id '{tid}'")
            tid = None
        if tid:
            tech_family = tax.family_of(tid)
            if not family:
                family = tech_family
            elif family != tech_family:
                amap.placement_warnings.append(
                    f"{address}: technique '{tid}' belongs to family '{tech_family}', "
                    f"not '{family}'; hung directly under '{family}'")
                tid = None
        amap.placement[address] = (family or UNCLASSIFIED, tid)


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
    `approach-` claims, or its `surveyed-` claims when it has no `approach-` claim."""
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
        amap.placement[paper] = (amap.family(candidates[0]), None)
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


def build_map(claims_dir: Path, features_path: Path, taxonomy_path: Path | None = None,
              view: str = DEFAULT_VIEW, inferred: bool = False) -> ApproachMap:
    """Collect approaches, features, the taxonomy, placements and every lineage edge
    that touches an approach. Check `amap.taxonomy.errors` before rendering."""
    approaches, aliases = find_approaches(claims_dir)
    features, feature_warnings = load_features(features_path, approaches)
    uses_techniques = any(row.get("technique") for row in features.values())
    taxonomy = (load_taxonomy(taxonomy_path, claims_dir,
                              needed=view != "lineage" or uses_techniques)
                if taxonomy_path else Taxonomy())
    amap = ApproachMap(approaches, features, taxonomy, feature_warnings=feature_warnings)
    if taxonomy.errors:
        return amap
    place_approaches(amap)
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
    return diagram.render(), folded


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
            tid = amap.technique(address)
            diagram.link(technique_node(tid) if tid else family_node(family), "---",
                         _mid(address), "", TREE_STYLE)
    for e in lineage:
        diagram.link(node_id(e.source), EDGE_STYLE[e.edge_type][0], node_id(e.target),
                     cg.EDGE_LABELS[e.edge_type], lineage_style(e.edge_type))
    for left, right in pairs:
        diagram.link(node_id(left), "-.-", node_id(right), "inferred", INFERRED_STYLE)
    rendered = diagram.render()
    if external:
        rendered += "\n  " + STUB_CLASS + "\n  class " + \
            ",".join(node_id(a) for a in external) + " stub"
    return rendered


def approach_table(amap: ApproachMap, addresses: list[str]) -> list[str]:
    out = ["| address | name | family | technique | channel | key | access | capacity |",
           "| --- | --- | --- | --- | --- | --- | --- | --- |"]
    for address in addresses:
        row = amap.features.get(address, {})
        out.append("| " + " | ".join(_cell(v) for v in (
            f"`{address}`", amap.approaches[address].name, amap.family(address),
            amap.technique(address) or "", row.get("channel", ""), row.get("key", ""),
            row.get("access_needed", ""), row.get("capacity", ""))) + " |")
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
    if techs:
        out += ["## Techniques", "",
                "| technique | parent | name | definition | grounded by | approaches |",
                "| --- | --- | --- | --- | --- | --- |"]
        for tid in techs:
            t = tax.techniques[tid]
            out.append("| " + " | ".join(_cell(v) for v in (
                f"`{tid}`", t.parent or "", t.name, t.definition,
                f"`{t.grounded_by}`" if t.grounded_by else "",
                str(amap.subtree_count(tid)))) + " |")
        out.append("")
    touching = [e for e in amap.edges if amap.family(e.source) == family
                or amap.family(e.target) == family]
    out += [f"## Lineage edges ({len(touching)})", ""] + edge_table(touching)
    out += ["## Approaches", ""] + approach_table(amap, members)
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


def family_files(live: Path, families: list[str]) -> dict[str, Path]:
    """<stem>_<family>.md beside the overview; a slug two families share gets a
    numeric suffix so neither file overwrites the other."""
    out: dict[str, Path] = {}
    used: set[str] = set()
    for family in families:
        slug = family_slug(family)
        candidate, n = slug, 2
        while candidate in used:
            candidate, n = f"{slug}_{n}", n + 1
        used.add(candidate)
        out[family] = live.with_name(f"{live.stem}_{candidate}.md")
    return out


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Render the approach map from the ledgers.")
    ap.add_argument("--root", default=str(REPO_ROOT),
                    help="project root; relative config paths resolve against it")
    ap.add_argument("--claims-dir", default=None,
                    help="override verified_claims/ (default <root>/literature/verified_claims)")
    ap.add_argument("--config", default=None,
                    help="override ledger.config.md (default <root>/ledger.config.md)")
    ap.add_argument("--features", default=None, help="override approach_features:")
    ap.add_argument("--taxonomy", default=None, help="override technique_taxonomy:")
    ap.add_argument("--view", choices=VIEWS, default=None, help="override approach_map_view:")
    ap.add_argument("--out", default=None, help="override approach_map_out:")
    ap.add_argument("--dry-run", action="store_true",
                    help="print counts and target paths; write nothing")
    args = ap.parse_args(argv)

    root = Path(args.root).expanduser().resolve()
    claims_dir = Path(args.claims_dir) if args.claims_dir else \
        root / "literature" / "verified_claims"
    config = parse_config(Path(args.config) if args.config else root / "ledger.config.md")
    features_path = Path(args.features).expanduser() if args.features else \
        config_path_value(config, "approach_features", DEFAULT_FEATURES, root)
    taxonomy_path = Path(args.taxonomy).expanduser() if args.taxonomy else \
        config_path_value(config, "technique_taxonomy", DEFAULT_TAXONOMY, root)
    live = Path(args.out).expanduser() if args.out else \
        config_path_value(config, "approach_map_out", DEFAULT_OUT, root)
    view = args.view or config_choice(config, "approach_map_view", VIEWS, DEFAULT_VIEW)
    inferred = config_choice(config, "inferred_links", ("off", "on"), "off") == "on"

    if not claims_dir.is_dir():
        log_error(f"claims directory not found: {claims_dir}")
        return 1
    try:
        amap = build_map(claims_dir, features_path, taxonomy_path, view, inferred)
    except (OSError, ValueError, csv.Error) as exc:
        log_error(f"approach map not built: {exc}")
        return 1

    tax = amap.taxonomy
    if tax.errors:
        for problem in tax.errors:
            log_error(problem)
        log_error(f"{len(tax.errors)} error(s) in the technique taxonomy {taxonomy_path} — "
                  "no map written.")
        return 1
    warnings = amap.feature_warnings + tax.warnings + amap.placement_warnings
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
    if warnings:
        log_warning(f"{len(warnings)} table warning(s), listed above and in the overview.")
    if unclassified:
        log_warning(f"{len(unclassified)} approach(es) have no family in {features_path}: "
                    + preview(unclassified))
    if empty:
        log_warning(f"{len(empty)} technique(s) have no approaches: " + preview(empty))
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
    generated = dt.datetime.now().astimezone().isoformat(timespec="seconds")
    today = dt.date.today().strftime("%Y%m%d")
    if args.dry_run:
        log_info(f"dry run — features table: {features_path}; taxonomy: {taxonomy_path}")
    try:
        for path, body in outputs:
            publish(path, body, generated, today, args.dry_run)
    except OSError as exc:
        log_error(f"approach map not written: {exc}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
