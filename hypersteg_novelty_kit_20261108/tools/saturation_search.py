#!/usr/bin/env python3
# === SCRIPT: saturation_search — a literature search run in rounds until it saturates ===
# Each round snowballs backward (references) and forward (citing papers) from every
# included paper, runs the registered queries in the first round, deduplicates against the
# register and every earlier round, and writes the new candidates for screening. The tool
# makes no judgement and calls no model: screening decisions arrive through screening.tsv,
# filled by a person or an agent against the inclusion criteria in ledger.config.md.
# The run stops, with an explicit status, when a fully completed round adds fewer than
# saturation_k includes (saturated) or when the round cap is reached (round_cap_reached).
# HONEST LIMIT: saturation means these three metadata sources stopped yielding new
# includes from these seeds; it does not prove the literature is exhausted.
# INPUTS : ledger.config.md (search_queries, inclusion_criteria, saturation_k,
#          search_request_cap, search_leads_file); literature/REGISTER.tsv; the leads file.
# OUTPUTS: literature/search/<run_id>/ — run.json, seeds.tsv, leads.tsv, cache/,
#          round_<n>/{candidates.tsv, screening.tsv, round.json}, PRISMA.md, included.tsv.
# Run    : python3 tools/saturation_search.py {init|round|status|report} --run <id>
from __future__ import annotations

import argparse
import csv
import difflib
import hashlib
import io
import json
import os
import re
import shlex
import subprocess
import sys
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Callable

sys.path.insert(0, str(Path(__file__).resolve().parent))
from check_citations import parse_config  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parents[1]
SEARCH_SUBDIR = Path("literature") / "search"
REGISTER_REL = Path("literature") / "REGISTER.tsv"
LADDER_REL = "literature/fetch_paper.sh"

USER_AGENT = "ledger-saturation-search"
DEFAULT_K = 3
DEFAULT_ROUNDS = 3
MAX_ROUNDS = 5
DEFAULT_REQUEST_CAP = 200
PAGE_SIZE = 100
QUERY_PAGE = 25
OPENALEX_BATCH = 50
LEAD_ROWS = 5
LEAD_ACCEPT = 0.90
LEAD_WEAK = 0.60
YEAR_MISMATCH_FACTOR = 0.85
MAX_RETRIES = 4
HTTP_TIMEOUT_S = 30
# Semantic Scholar's unauthenticated pool asks for about one request a second.
MIN_INTERVAL_S = {"openalex": 0.1, "s2": 1.1, "crossref": 0.1}
SOURCES = ("openalex", "s2", "crossref")

DECISIONS = ("include", "exclude", "unsure")
CANDIDATE_COLUMNS = ["id", "doi", "arxiv", "title", "citation", "year", "venue", "first_author",
                     "abstract", "found_via"]
SCREENING_COLUMNS = ["id", "decision", "criterion", "reason", "screener"]
SEED_COLUMNS = ["id", "doi", "arxiv", "title", "year", "first_author", "origin"]
LEAD_COLUMNS = ["line", "lead", "status", "score", "id", "doi", "arxiv", "title", "year",
                "first_author", "source", "note"]
INCLUDED_COLUMNS = ["id", "key", "doi", "arxiv", "title", "year", "first_author", "origin",
                    "fetch_command"]

OPENALEX_FIELDS = ("id,doi,title,publication_year,primary_location,authorships,"
                   "abstract_inverted_index")
S2_FIELDS = "title,year,venue,abstract,externalIds,authors"
CROSSREF_SELECT = "DOI,title,issued,container-title,abstract,author"

DOI_RE = re.compile(r"\b(10\.\d{4,9}/[^\s\"<>]+)", re.IGNORECASE)
ARXIV_RE = re.compile(r"(?:arxiv[:/ ]\s*|abs/)(\d{4}\.\d{4,5})(?:v\d+)?", re.IGNORECASE)
ARXIV_DOI_RE = re.compile(r"^10\.48550/arxiv\.(.+)$", re.IGNORECASE)
LEAD_YEAR_RE = re.compile(r"^(?P<head>.*?)\(?\b(?P<year>(?:19|20)\d{2})[a-z]?\b\)?"
                          r"[\s,.:;]*(?P<tail>.*)$")
RUN_ID_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_-]*$")
TAG_RE = re.compile(r"<[^>]+>")


def log_info(msg: str) -> None:
    print(f"[INFO] {msg}")


def log_warning(msg: str) -> None:
    print(f"[WARNING] {msg}", file=sys.stderr)


def log_error(msg: str) -> None:
    print(f"[ERROR] {msg}", file=sys.stderr)


# --- configuration -------------------------------------------------------------------

@dataclass
class SearchConfig:
    """The search keys of ledger.config.md, read and validated."""
    queries: list[str]
    criteria: dict[str, str]
    saturation_k: int
    request_cap: int
    leads_file: str
    problems: list[str] = field(default_factory=list)


def _value(config: dict[str, str], key: str) -> str:
    """A config value with any inline comment cut and a <placeholder> read as unset."""
    raw = config.get(key, "").split("#", 1)[0].strip()
    return "" if raw.startswith("<") else raw


def _positive_int(config: dict[str, str], key: str, default: int,
                  problems: list[str]) -> int:
    raw = _value(config, key)
    if not raw:
        return default
    if not raw.isdigit() or int(raw) < 1:
        problems.append(f"{key}: '{raw}' is not a whole number of at least 1")
        return default
    return int(raw)


def read_search_config(config: dict[str, str]) -> SearchConfig:
    """Lists are one line, items separated by '|'; a criterion is `id: text`."""
    problems: list[str] = []
    queries = [q.strip() for q in _value(config, "search_queries").split("|") if q.strip()]
    criteria: dict[str, str] = {}
    for item in _value(config, "inclusion_criteria").split("|"):
        if not item.strip():
            continue
        cid, sep, text = item.partition(":")
        cid = cid.strip().lower()
        if not sep or not cid or not text.strip() or not RUN_ID_RE.match(cid):
            problems.append(f"inclusion_criteria: '{item.strip()}' is not `id: text`")
        elif cid in criteria:
            problems.append(f"inclusion_criteria: '{cid}' is declared twice")
        else:
            criteria[cid] = text.strip()
    return SearchConfig(
        queries=queries,
        criteria=criteria,
        saturation_k=_positive_int(config, "saturation_k", DEFAULT_K, problems),
        request_cap=_positive_int(config, "search_request_cap", DEFAULT_REQUEST_CAP,
                                  problems),
        leads_file=_value(config, "search_leads_file"),
        problems=problems)


# --- identity and normalisation ------------------------------------------------------

def ascii_fold(text: str) -> str:
    normalised = unicodedata.normalize("NFKD", text or "")
    return "".join(c for c in normalised if not unicodedata.combining(c)).lower()


def normalise_title(title: str) -> str:
    return " ".join(re.sub(r"[^a-z0-9]+", " ", ascii_fold(TAG_RE.sub(" ", title))).split())


def normalise_doi(doi: str | None) -> str:
    if not doi:
        return ""
    doi = doi.strip().lower()
    for prefix in ("https://doi.org/", "http://doi.org/", "https://dx.doi.org/",
                   "http://dx.doi.org/", "doi:"):
        if doi.startswith(prefix):
            doi = doi[len(prefix):]
    return doi.rstrip(".")


def arxiv_from_doi(doi: str) -> str:
    match = ARXIV_DOI_RE.match(doi or "")
    return match.group(1).lower() if match else ""


def clean_text(text: str | None) -> str:
    """One TSV-safe line: tags stripped, whitespace collapsed."""
    return " ".join(TAG_RE.sub(" ", text or "").split())


@dataclass
class Work:
    """One paper as a metadata source describes it."""
    doi: str = ""
    arxiv: str = ""
    title: str = ""
    year: str = ""
    venue: str = ""
    first_author: str = ""
    abstract: str = ""
    citation: str = ""
    found_via: list[str] = field(default_factory=list)

    def __post_init__(self) -> None:
        self.doi = normalise_doi(self.doi)
        self.arxiv = (self.arxiv or arxiv_from_doi(self.doi)).lower()
        self.year = str(self.year or "")

    @property
    def title_key(self) -> str:
        norm = normalise_title(self.title)
        return f"{norm}|{self.year}" if norm else ""

    @property
    def id(self) -> str:
        if self.doi:
            return f"doi:{self.doi}"
        if self.arxiv:
            return f"arxiv:{self.arxiv}"
        return "title:" + normalise_title(self.title).replace(" ", "-")[:80] + f"-{self.year}"

    def keys(self) -> list[str]:
        """Dedup keys, strongest first: DOI, then arXiv id, then title and year."""
        found = []
        if self.doi:
            found.append(f"doi:{self.doi}")
        if self.arxiv:
            found.append(f"arxiv:{self.arxiv}")
        if self.title_key:
            found.append(f"title:{self.title_key}")
        return found

    def absorb(self, other: "Work") -> None:
        for name in ("doi", "arxiv", "title", "year", "venue", "first_author", "abstract",
                     "citation"):
            if not getattr(self, name) and getattr(other, name):
                setattr(self, name, getattr(other, name))
        for via in other.found_via:
            if via not in self.found_via:
                self.found_via.append(via)


class WorkIndex:
    """Works keyed by every identity they carry, so a later sighting by a weaker key
    still lands on the same record."""

    def __init__(self) -> None:
        self.by_key: dict[str, Work] = {}
        self.works: list[Work] = []

    def find(self, work: Work) -> Work | None:
        for key in work.keys():
            if key in self.by_key:
                return self.by_key[key]
        return None

    def add(self, work: Work) -> bool:
        """True when the work is new to the index; otherwise it is merged."""
        existing = self.find(work)
        if existing is None:
            self.works.append(work)
            existing = work
        else:
            existing.absorb(work)
        for key in existing.keys():
            self.by_key.setdefault(key, existing)
        return existing is work


# --- HTTP ------------------------------------------------------------------------------

Transport = Callable[[str], tuple[int, bytes, dict[str, str]]]


class CapReached(Exception):
    """The per-round request cap is spent."""


def urllib_transport(url: str) -> tuple[int, bytes, dict[str, str]]:
    """GET with a generic User-Agent and no credentials of any kind."""
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT,
                                                   "Accept": "application/json"})
    try:
        with urllib.request.urlopen(request, timeout=HTTP_TIMEOUT_S) as response:
            return response.status, response.read(), dict(response.headers)
    except urllib.error.HTTPError as exc:
        return exc.code, exc.read() or b"", dict(exc.headers or {})
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        return 0, str(exc).encode(), {}


@dataclass
class SourceStats:
    requests: int = 0
    cache_hits: int = 0
    ok: int = 0
    not_found: int = 0
    failures: int = 0
    works: int = 0
    last_error: str = ""


class Client:
    """Cached, capped, polite JSON GETs. Only network attempts count toward the cap, so a
    re-run served from the cache costs nothing."""

    def __init__(self, cache_dir: Path, cap: int, transport: Transport | None = None,
                 sleep: Callable[[float], None] = time.sleep,
                 clock: Callable[[], float] = time.monotonic) -> None:
        self.cache_dir = cache_dir
        self.cap = cap
        self.transport = transport or urllib_transport
        self.sleep = sleep
        self.clock = clock
        self.requests = 0
        self.stats: dict[str, SourceStats] = {s: SourceStats() for s in SOURCES}
        self._last: dict[str, float] = {}

    def _cache_path(self, source: str, url: str) -> Path:
        return self.cache_dir / f"{source}_{hashlib.sha256(url.encode()).hexdigest()[:32]}.json"

    def _pace(self, source: str) -> None:
        wait = MIN_INTERVAL_S.get(source, 0) - (self.clock() - self._last.get(source, -1e9))
        if wait > 0:
            self.sleep(wait)
        self._last[source] = self.clock()

    def get_json(self, source: str, url: str) -> dict | None:
        """The parsed body, or None for not-found. Raises CapReached before a network call
        the cap does not allow, and RuntimeError when the source fails after retries."""
        stats = self.stats[source]
        cached = self._cache_path(source, url)
        if cached.is_file():
            stats.cache_hits += 1
            stats.ok += 1
            return json.loads(cached.read_text(encoding="utf-8"))["body"]
        for attempt in range(MAX_RETRIES + 1):
            if self.requests >= self.cap:
                raise CapReached()
            self._pace(source)
            self.requests += 1
            stats.requests += 1
            status, body, headers = self.transport(url)
            if status == 200:
                try:
                    payload = json.loads(body.decode("utf-8"))
                except (UnicodeDecodeError, json.JSONDecodeError) as exc:
                    stats.failures += 1
                    stats.last_error = f"unparseable JSON: {exc}"
                    raise RuntimeError(stats.last_error) from exc
                self._store(cached, url, payload)
                stats.ok += 1
                return payload
            if status == 404:
                stats.not_found += 1
                return None
            if status in (429, 500, 502, 503, 504) and attempt < MAX_RETRIES:
                self.sleep(self._backoff(headers, attempt))
                continue
            stats.failures += 1
            stats.last_error = f"HTTP {status or 'no response'}: {body[:160]!r}"
            raise RuntimeError(stats.last_error)
        raise RuntimeError("unreachable")

    @staticmethod
    def _backoff(headers: dict[str, str], attempt: int) -> float:
        retry_after = {k.lower(): v for k, v in headers.items()}.get("retry-after", "")
        if retry_after.strip().isdigit():
            return min(float(retry_after), 60.0)
        return float(2 ** (attempt + 1))

    @staticmethod
    def _store(path: Path, url: str, payload: dict) -> None:
        """Write-once: an existing cache entry is never replaced."""
        path.parent.mkdir(parents=True, exist_ok=True)
        try:
            fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o644)
        except FileExistsError:
            return
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            json.dump({"url": url, "body": payload}, handle)


# --- parsers: one per API shape --------------------------------------------------------

def _inverted_abstract(index: dict | None) -> str:
    if not index:
        return ""
    positions = [(pos, word) for word, places in index.items() for pos in places]
    return " ".join(word for _, word in sorted(positions))


def parse_openalex(item: dict) -> Work | None:
    if not item or not item.get("title"):
        return None
    location = item.get("primary_location") or {}
    source = location.get("source") or {}
    authors = item.get("authorships") or []
    first = ((authors[0].get("author") or {}).get("display_name", "") if authors else "")
    return Work(doi=item.get("doi") or "", title=clean_text(item.get("title")),
                year=item.get("publication_year") or "",
                venue=clean_text(source.get("display_name")), first_author=first,
                abstract=clean_text(_inverted_abstract(item.get("abstract_inverted_index"))))


def parse_s2(item: dict) -> Work | None:
    if not item or not item.get("title"):
        return None
    ids = item.get("externalIds") or {}
    authors = item.get("authors") or []
    return Work(doi=ids.get("DOI") or "", arxiv=ids.get("ArXiv") or "",
                title=clean_text(item.get("title")), year=item.get("year") or "",
                venue=clean_text(item.get("venue")),
                first_author=(authors[0].get("name", "") if authors else ""),
                abstract=clean_text(item.get("abstract")))


def _crossref_year(item: dict) -> str:
    for key in ("issued", "published-print", "published-online"):
        parts = (item.get(key) or {}).get("date-parts") or [[None]]
        if parts and parts[0] and parts[0][0]:
            return str(parts[0][0])
    return ""


def parse_crossref(item: dict) -> Work | None:
    titles = item.get("title") or []
    if not titles:
        return None
    venues = item.get("container-title") or []
    authors = item.get("author") or []
    return Work(doi=item.get("DOI") or "", title=clean_text(titles[0]),
                year=_crossref_year(item), venue=clean_text(venues[0] if venues else ""),
                first_author=(authors[0].get("family", "") if authors else ""),
                abstract=clean_text(item.get("abstract")))


def parse_crossref_reference(ref: dict) -> Work | None:
    """A deposited reference. Publishers often deposit only a DOI and the free-text
    citation, kept as `citation` for the screener; a reference with neither a DOI nor a
    title cannot be deduplicated and is skipped."""
    if not ref.get("DOI") and not ref.get("article-title"):
        return None
    return Work(doi=ref.get("DOI") or "", title=clean_text(ref.get("article-title")),
                year=ref.get("year") or "", venue=clean_text(ref.get("journal-title")),
                first_author=ref.get("author") or "",
                citation=clean_text(ref.get("unstructured")))


# --- source operations -----------------------------------------------------------------

def _q(value: str) -> str:
    return urllib.parse.quote(value, safe="")


def _path(value: str) -> str:
    """A DOI or paper id inside a URL path: its '/' and ':' stay literal, because the
    APIs route on them."""
    return urllib.parse.quote(value, safe="/:")


def openalex_lookup_url(seed: Work) -> str | None:
    doi = seed.doi or (f"10.48550/arxiv.{seed.arxiv}" if seed.arxiv else "")
    if not doi:
        return None
    return (f"https://api.openalex.org/works/doi:{_path(doi)}"
            f"?select=id,doi,title,referenced_works")


def openalex_list_url(filter_expr: str, per_page: int) -> str:
    return (f"https://api.openalex.org/works?filter={_q(filter_expr)}"
            f"&per-page={per_page}&select={OPENALEX_FIELDS}")


def openalex_search_url(query: str, per_page: int = QUERY_PAGE) -> str:
    return (f"https://api.openalex.org/works?search={_q(query)}"
            f"&per-page={per_page}&select={OPENALEX_FIELDS}")


def s2_paper_id(seed: Work) -> str | None:
    if seed.doi and not arxiv_from_doi(seed.doi):
        return f"DOI:{seed.doi}"
    if seed.arxiv:
        return f"ARXIV:{seed.arxiv}"
    return None


def s2_edges_url(paper_id: str, direction: str) -> str:
    edge = "references" if direction == "backward" else "citations"
    return (f"https://api.semanticscholar.org/graph/v1/paper/{_path(paper_id)}/{edge}"
            f"?fields={S2_FIELDS}&limit={PAGE_SIZE}")


def s2_search_url(query: str) -> str:
    return (f"https://api.semanticscholar.org/graph/v1/paper/search?query={_q(query)}"
            f"&fields={S2_FIELDS}&limit={QUERY_PAGE}")


def crossref_work_url(doi: str) -> str:
    return f"https://api.crossref.org/works/{_path(doi)}"


def crossref_search_url(query: str, rows: int = QUERY_PAGE) -> str:
    return (f"https://api.crossref.org/works?query.bibliographic={_q(query)}"
            f"&rows={rows}&select={CROSSREF_SELECT}")


@dataclass
class TaskResult:
    works: list[Work]
    truncated: bool = False
    note: str = ""


def _openalex_work_id(seed: Work, client: Client) -> tuple[str, list[str]] | None:
    url = openalex_lookup_url(seed)
    if url is None:
        return None
    body = client.get_json("openalex", url)
    if not body:
        return None
    wid = (body.get("id") or "").rsplit("/", 1)[-1]
    refs = [r.rsplit("/", 1)[-1] for r in body.get("referenced_works") or []]
    return wid, refs


def openalex_backward(seed: Work, client: Client) -> TaskResult:
    found = _openalex_work_id(seed, client)
    if not found:
        return TaskResult([], note="not in OpenAlex")
    works: list[Work] = []
    refs = found[1]
    for start in range(0, len(refs), OPENALEX_BATCH):
        batch = refs[start:start + OPENALEX_BATCH]
        body = client.get_json("openalex", openalex_list_url(
            "openalex_id:" + "|".join(batch), OPENALEX_BATCH)) or {}
        works.extend(w for w in map(parse_openalex, body.get("results") or []) if w)
    return TaskResult(works)


def openalex_forward(seed: Work, client: Client) -> TaskResult:
    found = _openalex_work_id(seed, client)
    if not found or not found[0]:
        return TaskResult([], note="not in OpenAlex")
    body = client.get_json("openalex", openalex_list_url(f"cites:{found[0]}", PAGE_SIZE)) or {}
    results = body.get("results") or []
    total = (body.get("meta") or {}).get("count") or 0
    works = [w for w in map(parse_openalex, results) if w]
    return TaskResult(works, truncated=total > len(results))


def s2_edges(seed: Work, client: Client, direction: str) -> TaskResult:
    paper_id = s2_paper_id(seed)
    if paper_id is None:
        return TaskResult([], note="no DOI or arXiv id")
    body = client.get_json("s2", s2_edges_url(paper_id, direction))
    if body is None:
        return TaskResult([], note="not in Semantic Scholar")
    side = "citedPaper" if direction == "backward" else "citingPaper"
    works = [w for w in (parse_s2(row.get(side) or {}) for row in body.get("data") or []) if w]
    return TaskResult(works, truncated=bool(body.get("next")))


def crossref_backward(seed: Work, client: Client) -> TaskResult:
    if not seed.doi or arxiv_from_doi(seed.doi):
        return TaskResult([], note="no Crossref DOI")
    body = client.get_json("crossref", crossref_work_url(seed.doi))
    if body is None:
        return TaskResult([], note="not in Crossref")
    refs = (body.get("message") or {}).get("reference") or []
    return TaskResult([w for w in map(parse_crossref_reference, refs) if w])


def run_query(source: str, query: str, client: Client) -> TaskResult:
    if source == "openalex":
        body = client.get_json("openalex", openalex_search_url(query)) or {}
        return TaskResult([w for w in map(parse_openalex, body.get("results") or []) if w])
    if source == "s2":
        body = client.get_json("s2", s2_search_url(query)) or {}
        return TaskResult([w for w in map(parse_s2, body.get("data") or []) if w])
    body = client.get_json("crossref", crossref_search_url(query)) or {}
    items = (body.get("message") or {}).get("items") or []
    return TaskResult([w for w in map(parse_crossref, items) if w])


def run_task(task: dict, seeds: dict[str, Work], client: Client) -> TaskResult:
    """Dispatch one (kind, source, target) task."""
    kind, source, target = task["kind"], task["source"], task["target"]
    if kind == "query":
        return run_query(source, target, client)
    seed = seeds[target]
    if source == "openalex":
        return openalex_backward(seed, client) if kind == "backward" \
            else openalex_forward(seed, client)
    if source == "s2":
        return s2_edges(seed, client, kind)
    return crossref_backward(seed, client)


def build_tasks(seed_ids: list[str], queries: list[str]) -> list[dict]:
    """Every seed in both directions on every source that offers it (Crossref has no
    open citing-paper index), then every query on every source."""
    tasks = []
    for sid in seed_ids:
        for source in SOURCES:
            tasks.append({"kind": "backward", "source": source, "target": sid})
            if source != "crossref":
                tasks.append({"kind": "forward", "source": source, "target": sid})
    for query in queries:
        for source in SOURCES:
            tasks.append({"kind": "query", "source": source, "target": query})
    return tasks


# --- leads -------------------------------------------------------------------------------

def lead_title_and_year(text: str) -> tuple[str, str]:
    """`Kirchenbauer et al. 2023, A watermark for large language models` -> the title
    after the year, and the year. With no year, the whole line is the title."""
    match = LEAD_YEAR_RE.match(text)
    if not match:
        return text.strip(" \"'"), ""
    tail = match.group("tail").strip(" \"'.")
    title = tail if len(tail.split()) >= 2 else match.group("head").strip(" \"',.")
    return title, match.group("year")


def lead_score(lead_title: str, lead_year: str, work: Work) -> float:
    score = difflib.SequenceMatcher(None, normalise_title(lead_title),
                                    normalise_title(work.title)).ratio()
    if lead_year and work.year and abs(int(lead_year) - int(work.year)) > 1:
        score *= YEAR_MISMATCH_FACTOR
    return round(score, 3)


def resolve_lead(text: str, client: Client) -> dict:
    """One leads-file line resolved to an identity, with its score and status:
    accepted (direct id, or score >= LEAD_ACCEPT), weak (flagged, never used as a seed),
    unresolved, or error (every source failed)."""
    doi = DOI_RE.search(text)
    arxiv = ARXIV_RE.search(text)
    if doi or arxiv:
        work = Work(doi=doi.group(1).rstrip(".,;)") if doi else "",
                    arxiv=arxiv.group(1) if arxiv else "")
        return {"status": "accepted", "score": 1.0, "work": work, "source": "direct",
                "note": "identifier given in the lead"}
    title, year = lead_title_and_year(text)
    best: tuple[float, Work | None, str] = (0.0, None, "")
    errors = []
    for source, url, parse, rows in (
            ("openalex", openalex_search_url(title, LEAD_ROWS), parse_openalex, "results"),
            ("crossref", crossref_search_url(text, LEAD_ROWS), parse_crossref, "items")):
        try:
            body = client.get_json(source, url) or {}
        except RuntimeError as exc:
            errors.append(f"{source}: {exc}")
            continue
        items = body.get(rows) or (body.get("message") or {}).get(rows) or []
        for work in filter(None, map(parse, items)):
            score = lead_score(title, year, work)
            if score > best[0]:
                best = (score, work, source)
    score, work, source = best
    if work is None:
        status = "error" if len(errors) == 2 else "unresolved"
        return {"status": status, "score": 0.0, "work": None, "source": "",
                "note": "; ".join(errors) or "no match returned"}
    status = ("accepted" if score >= LEAD_ACCEPT else
              "weak" if score >= LEAD_WEAK else "unresolved")
    note = "; ".join(errors)
    if status == "unresolved":
        note = (note + "; " if note else "") + \
            f"best match scored {score}, below the weak threshold {LEAD_WEAK}"
    if status == "weak":
        note = (note + "; " if note else "") + \
            "weak match: replace the lead with its DOI or arXiv id to accept it"
    return {"status": status, "score": score, "work": work, "source": source, "note": note}


# --- files --------------------------------------------------------------------------------

def read_tsv(path: Path) -> list[dict[str, str]]:
    if not path.is_file():
        return []
    with path.open(encoding="utf-8", newline="") as handle:
        return [{k: (v or "") for k, v in row.items()}
                for row in csv.DictReader(handle, delimiter="\t")]


def write_new_tsv(path: Path, columns: list[str], rows: list[dict]) -> None:
    """Create a TSV that must not already exist."""
    with path.open("x", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns, delimiter="\t",
                                extrasaction="ignore", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def write_new_json(path: Path, payload: dict) -> None:
    with path.open("x", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2)
        handle.write("\n")


def work_row(work: Work) -> dict[str, str]:
    row = asdict(work)
    row["id"] = work.id
    row["found_via"] = " ; ".join(work.found_via)
    return row


def work_from_row(row: dict[str, str]) -> Work:
    via = [v.strip() for v in row.get("found_via", "").split(" ; ") if v.strip()]
    return Work(doi=row.get("doi", ""), arxiv=row.get("arxiv", ""),
                title=row.get("title", ""), year=row.get("year", ""),
                venue=row.get("venue", ""), first_author=row.get("first_author", ""),
                abstract=row.get("abstract", ""), citation=row.get("citation", ""),
                found_via=via)


def register_works(root: Path) -> list[tuple[str, Work]]:
    """(register key, work) for every register row."""
    out = []
    for row in read_tsv(root / REGISTER_REL):
        out.append((row.get("key", ""),
                    Work(doi=row.get("doi", ""), title=row.get("title", ""),
                         year=row.get("year", ""), first_author=row.get("first_author", ""))))
    return out


# --- run state ------------------------------------------------------------------------------

def run_dir(root: Path, run_id: str) -> Path:
    return root / SEARCH_SUBDIR / run_id


def round_dir(rdir: Path, n: int) -> Path:
    return rdir / f"round_{n}"


def existing_rounds(rdir: Path) -> list[int]:
    found = []
    for child in rdir.glob("round_*"):
        suffix = child.name.split("_", 1)[1]
        if child.is_dir() and suffix.isdigit():
            found.append(int(suffix))
    return sorted(found)


def read_screening(path: Path, candidate_ids: list[str],
                   criteria: dict[str, str]) -> tuple[dict[str, dict], list[str]]:
    """Decisions by candidate id, and every reason the screening is not yet complete."""
    problems: list[str] = []
    decisions: dict[str, dict] = {}
    wanted = set(candidate_ids)
    if not path.is_file():
        return {}, [f"{path} is missing"]
    for line, row in enumerate(read_tsv(path), 2):
        cid = row.get("id", "").strip()
        decision = row.get("decision", "").strip().lower()
        if cid not in wanted:
            problems.append(f"line {line}: '{cid}' is not a candidate of this round")
            continue
        if cid in decisions:
            problems.append(f"line {line}: '{cid}' is screened twice")
            continue
        if not decision:
            continue
        if decision not in DECISIONS:
            problems.append(f"line {line}: decision '{decision}' is not one of "
                            f"{' | '.join(DECISIONS)}")
            continue
        cited = [c.strip().lower() for c in row.get("criterion", "").split(",") if c.strip()]
        unknown = [c for c in cited if c not in criteria]
        if unknown:
            problems.append(f"line {line}: criterion {', '.join(unknown)} is not in "
                            f"inclusion_criteria ({', '.join(criteria) or 'none declared'})")
            continue
        if decision != "unsure" and not cited:
            problems.append(f"line {line}: '{cid}' is marked {decision} without a criterion")
            continue
        decisions[cid] = {**row, "decision": decision, "criterion": ",".join(cited)}
    undecided = [cid for cid in candidate_ids if cid not in decisions]
    if undecided:
        problems.append(f"{len(undecided)} of {len(candidate_ids)} candidates have no valid "
                        f"decision (first: {undecided[0]})")
    return decisions, problems


@dataclass
class RoundState:
    n: int
    meta: dict
    candidates: list[dict[str, str]]
    decisions: dict[str, dict]
    problems: list[str]

    def count(self, decision: str) -> int:
        return sum(1 for d in self.decisions.values() if d["decision"] == decision)

    @property
    def complete(self) -> bool:
        """Every planned request ran: no task was cut by the cap or lost to a failure."""
        return not self.meta.get("pending_tasks")


@dataclass
class RunState:
    run: dict
    rounds: list[RoundState]
    status: str
    reason: str


def evaluate(root: Path, run_id: str) -> RunState:
    """The run's status, derived from the files on disk every time it is asked for."""
    rdir = run_dir(root, run_id)
    run = json.loads((rdir / "run.json").read_text(encoding="utf-8"))
    criteria = read_search_config(parse_config(root / "ledger.config.md")).criteria
    rounds = []
    for n in existing_rounds(rdir):
        here = round_dir(rdir, n)
        meta = json.loads((here / "round.json").read_text(encoding="utf-8")) \
            if (here / "round.json").is_file() else {"pending_tasks": ["round.json missing"]}
        candidates = read_tsv(here / "candidates.tsv")
        decisions, problems = read_screening(here / "screening.tsv",
                                             [c["id"] for c in candidates], criteria)
        rounds.append(RoundState(n, meta, candidates, decisions, problems))
    k, cap = run["saturation_k"], run["rounds"]
    if not rounds:
        return RunState(run, rounds, "ready", "round 1 has not been run")
    last = rounds[-1]
    if last.problems:
        return RunState(run, rounds, "awaiting_screening",
                        f"round {last.n} screening is incomplete: " + "; ".join(last.problems))
    includes = last.count("include")
    if last.complete and includes < k:
        why = (f"round {last.n} added {includes} include(s), fewer than saturation_k = "
               f"{k}, with every planned task completed")
        first_page = len(last.meta.get("truncated_at_page_limit", []))
        if first_page:
            why += f"; {first_page} task(s) were read to their first page only"
        return RunState(run, rounds, "saturated", why)
    if last.n >= cap:
        why = (f"round {last.n} of {cap} is screened; {includes} include(s) in it")
        if not last.complete:
            why += (f", and {len(last.meta['pending_tasks'])} task(s) never completed, "
                    f"so saturation was not reached")
        return RunState(run, rounds, "round_cap_reached", why)
    if not last.complete:
        return RunState(run, rounds, "ready",
                        f"round {last.n} left {len(last.meta['pending_tasks'])} task(s) "
                        f"incomplete; they carry into round {last.n + 1}")
    return RunState(run, rounds, "ready",
                    f"round {last.n} added {includes} include(s) (saturation_k = {k})")


# --- commands ----------------------------------------------------------------------------------

def _load_config(root: Path) -> SearchConfig | None:
    config = read_search_config(parse_config(root / "ledger.config.md"))
    for problem in config.problems:
        log_error(f"ledger.config.md: {problem}")
    return None if config.problems else config


def cmd_init(root: Path, run_id: str, rounds: int, leads_path: str | None,
             dry_run: bool, transport: Transport | None = None,
             sleep: Callable[[float], None] = time.sleep) -> int:
    if not RUN_ID_RE.match(run_id):
        log_error(f"run id '{run_id}' must be letters, digits, '_' or '-'")
        return 2
    if not 1 <= rounds <= MAX_ROUNDS:
        log_error(f"--rounds must be between 1 and {MAX_ROUNDS}, got {rounds}")
        return 2
    config = _load_config(root)
    if config is None:
        return 1
    rdir = run_dir(root, run_id)
    if rdir.exists():
        log_error(f"{rdir} already exists; a run is initialised once. Choose a new --run id.")
        return 1
    if not config.criteria:
        log_warning("inclusion_criteria is empty: no candidate can be included or excluded "
                    "until criteria are declared in ledger.config.md")

    register = register_works(root)
    if not (root / REGISTER_REL).is_file():
        log_warning(f"{root / REGISTER_REL} not found: run literature/build_register.py. "
                    f"Seeds come from the leads file alone.")
    seeds = WorkIndex()
    for key, work in register:
        if work.doi or work.arxiv:
            work.found_via = [f"register:{key}"]
            seeds.add(work)
    log_info(f"register: {len(register)} row(s), {len(seeds.works)} with a DOI or arXiv id")

    lead_file = Path(leads_path or config.leads_file) if (leads_path or config.leads_file) \
        else None
    if lead_file and not lead_file.is_absolute():
        lead_file = root / lead_file
    leads = []
    if lead_file:
        if not lead_file.is_file():
            log_error(f"leads file {lead_file} not found")
            return 1
        leads = [(i, line.strip()) for i, line in
                 enumerate(lead_file.read_text(encoding="utf-8").splitlines(), 1)
                 if line.strip() and not line.lstrip().startswith("#")]
        log_info(f"leads: {len(leads)} line(s) in {lead_file}")
    if dry_run:
        log_info(f"[dry-run] would create {rdir} with {len(seeds.works)} register seed(s), "
                 f"resolve {len(leads)} lead(s), {len(config.queries)} query(ies), "
                 f"rounds cap {rounds}, saturation_k {config.saturation_k}, "
                 f"request cap {config.request_cap}/round. No request made, nothing written.")
        return 0

    rdir.mkdir(parents=True)
    client = Client(rdir / "cache", config.request_cap, transport, sleep)
    lead_rows = []
    for line, text in leads:
        try:
            result = resolve_lead(text, client)
        except CapReached:
            result = {"status": "error", "score": 0.0, "work": None, "source": "",
                      "note": "request cap reached before this lead"}
        work = result["work"]
        row = {"line": line, "lead": text, "status": result["status"],
               "score": result["score"], "source": result["source"], "note": result["note"]}
        if work is not None:
            row.update({k: v for k, v in work_row(work).items() if k in LEAD_COLUMNS})
        lead_rows.append(row)
        if result["status"] == "accepted":
            work.found_via = [f"lead:{line}"]
            seeds.add(work)
        elif result["status"] == "weak":
            log_warning(f"lead {line} matched weakly (score {result['score']}): "
                        f"'{text}' -> '{work.title}'. Not used as a seed.")
        else:
            log_warning(f"lead {line} {result['status']}: '{text}' ({result['note']})")
    write_new_tsv(rdir / "leads.tsv", LEAD_COLUMNS, lead_rows)
    seed_rows = [{**work_row(w), "origin": w.found_via[0]} for w in seeds.works]
    write_new_tsv(rdir / "seeds.tsv", SEED_COLUMNS, seed_rows)
    write_new_json(rdir / "run.json", {
        "run_id": run_id, "created": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
        "rounds": rounds, "saturation_k": config.saturation_k,
        "request_cap": config.request_cap, "queries": config.queries,
        "inclusion_criteria": config.criteria, "leads_file": str(lead_file or ""),
        "lead_thresholds": {"accept": LEAD_ACCEPT, "weak": LEAD_WEAK}})
    accepted = sum(1 for r in lead_rows if r["status"] == "accepted")
    weak = sum(1 for r in lead_rows if r["status"] == "weak")
    log_info(f"leads: {accepted} accepted, {weak} weak (flagged, not seeded), "
             f"{len(lead_rows) - accepted - weak} unresolved or failed")
    log_info(f"seeds: {len(seeds.works)}; queries: {len(config.queries)}; "
             f"lead requests: {client.requests}")
    log_info(f"wrote {rdir / 'run.json'}")
    log_info(f"wrote {rdir / 'seeds.tsv'}")
    log_info(f"wrote {rdir / 'leads.tsv'}")
    return 0


def _round_inputs(root: Path, state: RunState, n: int) -> tuple[dict[str, Work], list[dict]]:
    """Seeds and tasks for round n: the seeds file and the queries for round 1, then the
    previous round's includes plus any task it left incomplete."""
    rdir = run_dir(root, state.run["run_id"])
    seeds: dict[str, Work] = {}
    if n == 1:
        for row in read_tsv(rdir / "seeds.tsv"):
            seeds[row["id"]] = work_from_row(row)
        return seeds, build_tasks(list(seeds), state.run.get("queries", []))
    previous = state.rounds[-1]
    for row in previous.candidates:
        if previous.decisions.get(row["id"], {}).get("decision") == "include":
            seeds[row["id"]] = work_from_row(row)
    carried = list(previous.meta.get("pending_tasks", []))
    for task in carried:
        if task["kind"] != "query" and task["target"] not in seeds:
            seeds[task["target"]] = work_from_row(task["seed"])
    return seeds, build_tasks([s for s in seeds if s not in
                               {t["target"] for t in carried}], []) + \
        [{k: t[k] for k in ("kind", "source", "target")} for t in carried]


def known_index(root: Path, state: RunState) -> WorkIndex:
    """Everything already seen: the register, the seeds, and every earlier round."""
    index = WorkIndex()
    for _key, work in register_works(root):
        index.add(work)
    rdir = run_dir(root, state.run["run_id"])
    for row in read_tsv(rdir / "seeds.tsv"):
        index.add(work_from_row(row))
    for rnd in state.rounds:
        for row in rnd.candidates:
            index.add(work_from_row(row))
    return index


def cmd_round(root: Path, run_id: str, dry_run: bool, transport: Transport | None = None,
              sleep: Callable[[float], None] = time.sleep) -> int:
    rdir = run_dir(root, run_id)
    if not (rdir / "run.json").is_file():
        log_error(f"no run '{run_id}' at {rdir}: run `init --run {run_id}` first")
        return 1
    if _load_config(root) is None:
        return 1
    state = evaluate(root, run_id)
    if state.status in ("saturated", "round_cap_reached"):
        log_info(f"STATUS: {state.status} — {state.reason}. No further round runs.")
        return 0
    if state.status == "awaiting_screening":
        log_error(f"refusing to start a new round: {state.reason}")
        return 1
    n = len(state.rounds) + 1
    here = round_dir(rdir, n)
    if here.exists():
        log_error(f"{here} already exists but round {n} is not recorded; inspect it by hand")
        return 1
    seeds, tasks = _round_inputs(root, state, n)
    by_source = {s: sum(1 for t in tasks if t["source"] == s) for s in SOURCES}
    log_info(f"round {n}: {len(seeds)} seed(s), {len(tasks)} task(s) "
             f"({', '.join(f'{s} {c}' for s, c in by_source.items())}); "
             f"request cap {state.run['request_cap']}")
    if not tasks:
        log_error(f"round {n}: 0 candidates because there are no seeds: the register holds "
                  f"no paper with a DOI or arXiv id, no lead was accepted (see leads.tsv), "
                  f"and no search_queries are registered. Nothing written.")
        return 1
    if dry_run:
        log_info("[dry-run] no request made, nothing written")
        return 0

    client = Client(rdir / "cache", state.run["request_cap"], transport, sleep)
    known = known_index(root, state)
    fresh = WorkIndex()
    identified = within_dupes = already_known = 0
    pending: list[dict] = []
    truncated: list[str] = []
    for i, task in enumerate(tasks):
        label = f"{task['kind']}|{task['source']}|{task['target']}"
        try:
            result = run_task(task, seeds, client)
        except CapReached:
            pending.extend(tasks[i:])
            log_warning(f"request cap {client.cap} reached: {len(tasks) - i} task(s) "
                        f"carried into the next round")
            break
        except RuntimeError as exc:
            pending.append(task)
            log_warning(f"{label} failed: {exc}")
            continue
        if result.truncated:
            truncated.append(label)
        client.stats[task["source"]].works += len(result.works)
        for work in result.works:
            identified += 1
            work.found_via = [label]
            match = known.find(work)
            if match is not None:
                already_known += 1
                continue
            if not fresh.add(work):
                within_dupes += 1
    for task in pending:
        if task["kind"] != "query":
            task["seed"] = work_row(seeds[task["target"]])

    candidates = [work_row(w) for w in fresh.works]
    here.mkdir()
    write_new_tsv(here / "candidates.tsv", CANDIDATE_COLUMNS, candidates)
    write_new_tsv(here / "screening.tsv", SCREENING_COLUMNS,
                  [{"id": c["id"]} for c in candidates])
    failing = [s for s, st in client.stats.items() if st.failures and not st.ok]
    zero_reason = ""
    if not candidates:
        if client.requests and all(not st.ok and not st.not_found
                                   for st in client.stats.values()):
            zero_reason = "every API request failed"
        elif identified:
            zero_reason = (f"truly nothing new: all {identified} record(s) found were "
                           f"already in the register, the seeds or an earlier round")
        else:
            zero_reason = "the sources answered but returned no records for these seeds"
    write_new_json(here / "round.json", {
        "round": n, "seeds": list(seeds), "tasks": len(tasks),
        "identified": identified, "duplicates_within_round": within_dupes,
        "already_known": already_known, "candidates": len(candidates),
        "requests": client.requests, "sources": {s: asdict(st) for s, st in
                                                 client.stats.items()},
        "failing_sources": failing, "truncated_at_page_limit": truncated,
        "pending_tasks": pending, "zero_reason": zero_reason,
        "finished": time.strftime("%Y-%m-%dT%H:%M:%S%z")})

    for source, st in client.stats.items():
        log_info(f"{source}: {st.requests} request(s), {st.cache_hits} cached, "
                 f"{st.works} record(s), {st.not_found} not found, {st.failures} failed")
    for source in failing:
        log_warning(f"{source} failed every request it made: {client.stats[source].last_error}")
    if truncated:
        log_warning(f"{len(truncated)} task(s) returned only the first page of "
                    f"{PAGE_SIZE}; the rest were not fetched")
    log_info(f"round {n}: {identified} identified, {within_dupes} duplicate(s) within the "
             f"round, {already_known} already known, {len(candidates)} new candidate(s)")
    if zero_reason:
        (log_error if zero_reason.startswith("every") else log_warning)(
            f"0 candidates: {zero_reason}")
    log_info(f"wrote {here / 'candidates.tsv'}")
    log_info(f"wrote {here / 'screening.tsv'} — fill every decision before the next round")
    return 1 if zero_reason.startswith("every") else 0


def cmd_status(root: Path, run_id: str) -> int:
    if not (run_dir(root, run_id) / "run.json").is_file():
        log_error(f"no run '{run_id}' under {root / SEARCH_SUBDIR}")
        return 1
    state = evaluate(root, run_id)
    for rnd in state.rounds:
        log_info(f"round {rnd.n}: {len(rnd.candidates)} candidate(s); "
                 f"{len(rnd.decisions)} screened — {rnd.count('include')} include, "
                 f"{rnd.count('exclude')} exclude, {rnd.count('unsure')} unsure; "
                 f"{len(rnd.meta.get('pending_tasks', []))} task(s) incomplete")
    log_info(f"STATUS: {state.status} — {state.reason}")
    return 0


# --- report ------------------------------------------------------------------------------------

def prisma_rows(state: RunState) -> list[dict]:
    rows = []
    for rnd in state.rounds:
        meta = rnd.meta
        rows.append({
            "round": rnd.n, "identified": meta.get("identified", 0),
            "duplicates": meta.get("duplicates_within_round", 0),
            "already_known": meta.get("already_known", 0),
            "candidates": len(rnd.candidates), "screened": len(rnd.decisions),
            "included": rnd.count("include"), "excluded": rnd.count("exclude"),
            "unsure": rnd.count("unsure"),
            "undecided": len(rnd.candidates) - len(rnd.decisions)})
    return rows


def render_prisma(state: RunState) -> str:
    run = state.run
    lines = [f"# PRISMA flow — search run `{run['run_id']}`", "",
             f"**Status:** {state.status} — {state.reason}", "",
             f"Rounds cap {run['rounds']}; saturation_k {run['saturation_k']}; request cap "
             f"{run['request_cap']} per round. Sources: OpenAlex, Semantic Scholar Graph API, "
             f"Crossref (metadata only).", "",
             "| round | identified | duplicates removed | already known | screened "
             "| included | excluded | unsure | undecided |",
             "| --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for row in prisma_rows(state):
        lines.append(f"| {row['round']} | {row['identified']} | {row['duplicates']} | "
                     f"{row['already_known']} | {row['candidates']} | {row['included']} | "
                     f"{row['excluded']} | {row['unsure']} | {row['undecided']} |")
    lines += ["", "identified = duplicates removed + already known + screened; screened = "
              "included + excluded + unsure + undecided.", ""]
    for rnd in state.rounds:
        meta = rnd.meta
        lines.append(f"## Round {rnd.n}")
        lines.append("")
        lines.append(f"- seeds: {len(meta.get('seeds', []))}; tasks: {meta.get('tasks', 0)}; "
                     f"requests: {meta.get('requests', 0)}")
        for source, st in (meta.get("sources") or {}).items():
            lines.append(f"- {source}: {st['requests']} request(s), {st['cache_hits']} "
                         f"cached, {st['works']} record(s), {st['not_found']} not found, "
                         f"{st['failures']} failed")
        if meta.get("truncated_at_page_limit"):
            lines.append(f"- first page only ({PAGE_SIZE}) for "
                         f"{len(meta['truncated_at_page_limit'])} task(s)")
        if meta.get("pending_tasks"):
            lines.append(f"- incomplete tasks: {len(meta['pending_tasks'])}")
        if meta.get("zero_reason"):
            lines.append(f"- 0 candidates: {meta['zero_reason']}")
        lines.append("")
    stop = {"saturated": "saturated", "round_cap_reached": "round cap reached"}
    lines.append(f"**Stop reason:** {stop.get(state.status, 'not stopped (' + state.status + ')')}"
                 f" — {state.reason}")
    return "\n".join(lines) + "\n"


def _surname(name: str) -> str:
    parts = re.sub(r"[^a-z ]+", "", ascii_fold(name).replace("-", "")).split()
    return parts[-1] if parts else "anon"


def included_rows(root: Path, state: RunState) -> list[dict]:
    """Accepted lead seeds and every included candidate, each with a fresh literature key
    that collides with nothing in the register or on disk."""
    rdir = run_dir(root, state.run["run_id"])
    taken = {key for key, _w in register_works(root)}
    taken |= {p.stem for p in (root / "literature").glob("*") if p.is_file()}
    picked = []
    for row in read_tsv(rdir / "seeds.tsv"):
        if row.get("origin", "").startswith("lead:"):
            picked.append((row, row["origin"]))
    for rnd in state.rounds:
        for row in rnd.candidates:
            if rnd.decisions.get(row["id"], {}).get("decision") == "include":
                picked.append((row, f"round_{rnd.n}"))
    rows = []
    for row, origin in picked:
        base = f"{_surname(row.get('first_author', ''))}_{row.get('year') or 'nd'}"
        key = base
        for suffix in "abcdefghijklmnopqrstuvwxyz":
            if key not in taken:
                break
            key = base + suffix
        taken.add(key)
        command = [LADDER_REL, "--out", f"literature/{key}.html"]
        if row.get("doi"):
            command += ["--doi", row["doi"]]
        if row.get("arxiv"):
            command += ["--arxiv", row["arxiv"]]
        if row.get("title"):
            command += ["--title", row["title"]]
        rows.append({**row, "key": key, "origin": origin,
                     "fetch_command": shlex.join(command), "_argv": command})
    return rows


def write_derived(path: Path, text: str, sidecar: dict[str, str]) -> bool:
    """Replace a report the tool wrote earlier, but never one edited by hand since: the
    file's hash must still match the hash recorded when it was written."""
    if path.is_file():
        current = hashlib.sha256(path.read_bytes()).hexdigest()
        if current == hashlib.sha256(text.encode()).hexdigest():
            return True
        if sidecar.get(path.name) != current:
            log_error(f"{path} was changed after the tool wrote it; move it aside to "
                      f"regenerate it. Left untouched.")
            return False
    if not replace_atomically(path, text):
        return False
    sidecar[path.name] = hashlib.sha256(text.encode()).hexdigest()
    return True


def replace_atomically(path: Path, text: str) -> bool:
    """Stage through a sibling created exclusively, then swap. An occupied staging path
    is reported and left alone."""
    tmp = path.with_name(f".{path.name}.ledger-new")
    try:
        with tmp.open("x", encoding="utf-8") as handle:
            handle.write(text)
    except FileExistsError:
        log_error(f"staging path {tmp} is occupied; inspect it, move it aside, re-run")
        return False
    os.replace(tmp, path)
    return True


def cmd_report(root: Path, run_id: str, dry_run: bool, fetch: bool) -> int:
    rdir = run_dir(root, run_id)
    if not (rdir / "run.json").is_file():
        log_error(f"no run '{run_id}' under {root / SEARCH_SUBDIR}")
        return 1
    state = evaluate(root, run_id)
    prisma = render_prisma(state)
    rows = included_rows(root, state)
    handle = io.StringIO()
    writer = csv.DictWriter(handle, fieldnames=INCLUDED_COLUMNS, delimiter="\t",
                            extrasaction="ignore", lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    included_text = handle.getvalue()
    log_info(f"STATUS: {state.status} — {state.reason}")
    log_info(f"{len(rows)} paper(s) to download")
    for row in rows:
        print(row["fetch_command"])
    if dry_run:
        log_info("[dry-run] PRISMA.md and included.tsv not written")
        return 0
    sidecar_path = rdir / "report.sha256.json"
    sidecar = json.loads(sidecar_path.read_text(encoding="utf-8")) \
        if sidecar_path.is_file() else {}
    ok = write_derived(rdir / "PRISMA.md", prisma, sidecar) and \
        write_derived(rdir / "included.tsv", included_text, sidecar)
    ok = replace_atomically(sidecar_path, json.dumps(sidecar, indent=2) + "\n") and ok
    if not ok:
        return 1
    log_info(f"wrote {rdir / 'PRISMA.md'}")
    log_info(f"wrote {rdir / 'included.tsv'}")
    if fetch:
        return run_fetches(root, rows)
    return 0


def run_fetches(root: Path, rows: list[dict]) -> int:
    ladder = root / LADDER_REL
    if not ladder.is_file():
        log_error(f"{ladder} not found; run the printed commands from a Ledger project")
        return 1
    failed = 0
    for row in rows:
        log_info(f"fetching {row['key']}: {row.get('title', '')[:70]}")
        done = subprocess.run(["bash", *row["_argv"]], cwd=root)
        if done.returncode == 0:
            log_info(f"{row['key']}: downloaded")
        elif done.returncode == 3:
            log_warning(f"{row['key']}: BROWSER_REQUIRED — open the printed URLs in a browser")
            failed += 1
        else:
            log_warning(f"{row['key']}: the ladder found no copy (exit {done.returncode})")
            failed += 1
    log_info(f"fetch: {len(rows) - failed} of {len(rows)} downloaded")
    return 0 if not failed else 1


# --- CLI -------------------------------------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__ or "saturation literature search")
    parser.add_argument("--root", type=Path, default=REPO_ROOT,
                        help="project root holding ledger.config.md (default: this kit)")
    sub = parser.add_subparsers(dest="command", required=True)
    for name, help_text in (("init", "create a run: seeds from the register and leads"),
                            ("round", "run the next round"),
                            ("status", "print each round and the run's status"),
                            ("report", "write PRISMA.md and included.tsv")):
        cmd = sub.add_parser(name, help=help_text)
        cmd.add_argument("--run", required=True, help="run id")
        if name != "status":
            cmd.add_argument("--dry-run", action="store_true",
                             help="make no request and write nothing")
        if name == "init":
            cmd.add_argument("--rounds", type=int, default=DEFAULT_ROUNDS,
                             help=f"round cap, 1 to {MAX_ROUNDS} (default {DEFAULT_ROUNDS})")
            cmd.add_argument("--leads", help="leads file (default: search_leads_file)")
        if name == "report":
            cmd.add_argument("--fetch", action="store_true",
                             help="run the download ladder for each included paper")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    root = args.root.resolve()
    if args.command == "init":
        return cmd_init(root, args.run, args.rounds, args.leads, args.dry_run)
    if args.command == "round":
        return cmd_round(root, args.run, args.dry_run)
    if args.command == "status":
        return cmd_status(root, args.run)
    return cmd_report(root, args.run, args.dry_run, args.fetch)


if __name__ == "__main__":
    sys.exit(main())
