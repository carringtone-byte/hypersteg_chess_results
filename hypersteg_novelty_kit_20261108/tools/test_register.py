# === SCRIPT: Project-wide register of every test, pilot, design round and agent ===
# INPUTS:  ../hypersteg_arena/runs/*/ (config.json, host/calls.jsonl, host/stage.jsonl)
#          ~/agent_handoffs/{hypersteg,swarmsteg-production}/ (INDEX.md, */run.jsonl)
#          ~/.claude/projects/<this project>/*/subagents/agent-*.{jsonl,meta.json}
#          prompts/reviews/round*_claude_attack_on_v*.md (verdicts)
#          audits/test_register_notes.tsv (hand-kept purpose, decision, result, record)
# OUTPUTS: audits/test_register.tsv (every row, every column)
#          TEST_REGISTER.md (live, readable) and an immutable snapshot under
#          audits/test_register_snapshots/
"""Build the single register of everything the project has run.

Each row is one test: a live game or pilot, a stub harness test, a Codex design
step, a Claude adversarial review, or another agent spawned for the project.
Counts, tokens and times are read from the run logs; purpose, decision and result
come from the hand-kept notes file and are never invented by this script.

Usage (from the hypersteg project root):
    CLAUDE_PROJECT_WRITE=1 python -m harness.test_register
"""

from __future__ import annotations

import csv
import json
import logging
import re
import sys
from collections import Counter
from dataclasses import asdict, dataclass, fields
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Iterator

PROJECT_ROOT = Path(__file__).resolve().parents[1]
ARENA_RUNS = PROJECT_ROOT.parent / "hypersteg_arena" / "runs"
HOST_RUNS = Path.home() / "Library" / "Application Support" / "swarmsteg-host" / "runs"
HANDOFF_ROOTS = (
    Path.home() / "agent_handoffs" / "hypersteg",
    *sorted((Path.home() / "agent_handoffs").glob("swarmsteg*")),
)
CLAUDE_LOGS = (
    Path.home() / ".claude" / "projects"
    / "-Users-mw21-Desktop-post-intermission-non-phd-songhai-hypersteg"
)
REVIEWS = PROJECT_ROOT / "prompts" / "reviews"
NOTES_TSV = PROJECT_ROOT / "audits" / "test_register_notes.tsv"
MANUAL_TSV = PROJECT_ROOT / "audits" / "test_register_manual.tsv"
SAFEGUARD_TSV = PROJECT_ROOT / "audits" / "safeguard_stops.tsv"
OUT_TSV = PROJECT_ROOT / "audits" / "test_register.tsv"
OUT_MD = PROJECT_ROOT / "TEST_REGISTER.md"
SNAPSHOTS = PROJECT_ROOT / "audits" / "test_register_snapshots"

EAT = timezone(timedelta(hours=3))
NOTE_COLUMNS = ("test_id", "purpose", "decided_by", "design_version", "result", "record")
OPTIONAL_NOTE_COLUMNS = ("kind",)
SEED = re.compile(r"\b20261\d{5}\b")
REVIEW_DESCRIPTION = re.compile(r"(attack|adversarial review).*\bv(\d+)\b", re.I)
STUB_PURPOSES = (
    ("canary_literature",
     "Isolation test: a canary planted in the literature must stop the run"),
    ("canary_white_private",
     "Isolation test: a canary planted in White's private store must stop the run"),
    ("lockhalt", "Lock-halt test: failure to lock a protocol must halt the run"),
    ("repair", "Repair test: a malformed agent answer must be repaired and marked"),
)

logger = logging.getLogger("test_register")


@dataclass
class Row:
    """One registered test. Empty strings mean the source does not record the value."""

    test_id: str
    kind: str
    title: str
    started_eat: str = ""
    ended_eat: str = ""
    duration_min: str = ""
    purpose: str = ""
    decided_by: str = ""
    design_version: str = ""
    actor: str = ""
    backend: str = ""
    model: str = ""
    reasoning_effort: str = ""
    cli_version: str = ""
    games: str = ""
    plies_per_game: str = ""
    teams_members: str = ""
    agent_roles: str = ""
    processes_spawned: str = ""
    model_calls: str = ""
    input_tokens: str = ""
    cached_input_tokens: str = ""
    output_tokens: str = ""
    audit_notes: str = ""
    safeguard_stops: str = ""
    seeded_figures: str = ""
    status: str = ""
    result: str = ""
    record: str = ""
    path: str = ""


COLUMNS = [f.name for f in fields(Row)]


def to_eat(stamp: str | None) -> datetime | None:
    """Parse an ISO time stamp (any offset, or Z) and convert it to EAT."""
    if not stamp:
        return None
    parsed = datetime.fromisoformat(stamp.replace("Z", "+00:00"))
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=EAT)
    return parsed.astimezone(EAT)


def fmt(moment: datetime | None) -> str:
    """Format an EAT time for the register, or '' when unknown."""
    return moment.strftime("%Y-%m-%d %H:%M") if moment else ""


def minutes(start: datetime | None, end: datetime | None) -> str:
    """Duration in whole minutes, or '' when either end is unknown."""
    if not start or not end:
        return ""
    return str(round((end - start).total_seconds() / 60))


def read_jsonl(path: Path) -> Iterator[dict[str, Any]]:
    """Yield each JSON object in a JSONL file, logging and skipping broken lines."""
    with path.open(encoding="utf-8") as handle:
        for number, line in enumerate(handle, 1):
            line = line.strip()
            if not line:
                continue
            try:
                yield json.loads(line)
            except json.JSONDecodeError:
                logger.warning("[WARNING] %s line %d is not JSON; skipped", path, number)


def usage_dict(raw: Any) -> dict[str, Any]:
    """Return a call's usage as a dict, whether logged as a dict or as its repr."""
    if isinstance(raw, dict):
        return raw
    if isinstance(raw, str) and raw.strip().startswith("{"):
        try:
            return json.loads(raw.replace("'", '"').replace("None", "null"))
        except json.JSONDecodeError:
            return {}
    return {}


def stub_purpose(run_id: str) -> str:
    """Name what a stub run tested, from the naming convention of the test runs."""
    for key, text in STUB_PURPOSES:
        if key in run_id:
            return text
    return "Stage 0 harness check with stub agents (no model calls)"


def arena_rows() -> list[Row]:
    """Build one row per run folder in the arena: CK games, stub tests, MW pilots."""
    rows: list[Row] = []
    if not ARENA_RUNS.is_dir():
        logger.error("[ERROR] arena runs folder missing: %s", ARENA_RUNS)
        return rows
    for run_dir in sorted(p for p in ARENA_RUNS.iterdir() if p.is_dir()):
        config_path = run_dir / "config.json"
        if not config_path.is_file():
            logger.warning("[WARNING] %s has no config.json; skipped", run_dir.name)
            continue
        config = json.loads(config_path.read_text(encoding="utf-8"))
        calls_path = run_dir / "host" / "calls.jsonl"
        calls = list(read_jsonl(calls_path)) if calls_path.is_file() else []
        stage_path = run_dir / "host" / "stage.jsonl"
        stages = list(read_jsonl(stage_path)) if stage_path.is_file() else []

        backend = str(config.get("backend", ""))
        experiment = str(config.get("experiment", "CK"))
        live = backend not in ("stub", "")
        totals: Counter[str] = Counter()
        for call in calls:
            usage = usage_dict(call.get("usage"))
            for key in ("input_tokens", "cached_input_tokens", "output_tokens"):
                totals[key] += int(usage.get(key) or 0)
        start = to_eat(config.get("created")) or (to_eat(calls[0].get("ts")) if calls else None)
        end_stamp = stages[-1].get("ts") if stages else (calls[-1].get("ts") if calls else None)
        end = to_eat(end_stamp)
        last_stage = stages[-1] if stages else {}
        teams = config.get("teams") if isinstance(config.get("teams"), dict) else {}
        members = sum(len(v) if isinstance(v, list) else len(v.get("members", []))
                      for v in teams.values() if isinstance(v, (list, dict)))
        sessions = {c.get("session_id") for c in calls if c.get("session_id")}
        notes_path = run_dir / "host" / "audit_notes.jsonl"
        note_kinds = Counter(n.get("kind", "unnamed") for n in read_jsonl(notes_path)) \
            if notes_path.is_file() else Counter()
        note_summary = ", ".join(f"{k} x{v}" for k, v in sorted(note_kinds.items()))
        rows.append(Row(
            test_id=run_dir.name,
            kind="live_game" if live else "harness_test",
            title=f"{experiment} {'live game' if live else 'stub run'}",
            started_eat=fmt(start),
            ended_eat=fmt(end),
            duration_min=minutes(start, end),
            purpose=str(config.get("purpose") or ("" if live else stub_purpose(run_dir.name))),
            design_version=str(config.get("prompt_version") or experiment),
            actor="host harness",
            backend=backend,
            model=str(config.get("model", "")),
            reasoning_effort=str(config.get("reasoning_effort") or config.get("effort") or ""),
            cli_version=str(config.get("cli_version")
                            or (config.get("claude") or {}).get("pinned_version")
                            or ("unknown" if live else "none (stub)")),
            games=str(config.get("games", 1)),
            plies_per_game=str(config.get("total_plies", "")),
            teams_members=f"{len(teams)} teams, {members} members" if teams else "",
            agent_roles=str(len({c.get("agent_id") for c in calls if c.get("agent_id")})),
            processes_spawned=str(len(sessions) if live else 0),
            model_calls=str(len(calls) if live else 0),
            input_tokens=str(totals["input_tokens"]),
            cached_input_tokens=str(totals["cached_input_tokens"]),
            output_tokens=str(totals["output_tokens"]),
            audit_notes=note_summary,
            status=str(last_stage.get("stage", "no stage record")).lower(),
            result=f"last stage at ply {last_stage.get('ply')}" if last_stage else "",
            path=str(run_dir),
        ))
    logger.info("[INFO] arena runs registered: %d", len(rows))
    return rows


def read_tsv(path: Path) -> list[dict[str, str]]:
    """Rows of a tab-separated file with a header line, or [] when it is absent."""
    if not path.is_file():
        return []
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def host_rows() -> list[Row]:
    """Build one row per v17 run in the host root, which keeps its config outside the arena.

    Calls, tokens and stops come from the run's C8 export (`export/calls.tsv`); the
    terminal state comes from the journal (`host/events.jsonl`).
    """
    rows: list[Row] = []
    if not HOST_RUNS.is_dir():
        logger.error("[ERROR] host runs folder missing: %s", HOST_RUNS)
        return rows
    for run_dir in sorted(p for p in HOST_RUNS.iterdir() if p.is_dir()):
        config_path = run_dir / "config.json"
        if not config_path.is_file():
            logger.warning("[WARNING] %s has no config.json; skipped", run_dir.name)
            continue
        config = json.loads(config_path.read_text(encoding="utf-8"))
        if "registration" not in config:
            logger.info("[INFO] %s is not a v17 run; skipped", run_dir.name)
            continue
        journal_path = run_dir / "host" / "events.jsonl"
        journal = list(read_jsonl(journal_path)) if journal_path.is_file() else []
        calls = read_tsv(run_dir / "export" / "calls.tsv")
        live = bool(config.get("live"))
        totals: Counter[str] = Counter()
        unknown: Counter[str] = Counter()
        for call in calls:
            for key in ("input_tokens", "cached_input_tokens", "output_tokens"):
                value = call.get(key, "")
                if value.isdigit():
                    totals[key] += int(value)
                else:
                    unknown[key] += 1
        terminal = next((e for e in journal if e.get("event") == "run_terminal"), {})
        stops = [e for e in journal if e.get("event") == "provider_safeguard_stop"]
        stamps = [e.get("timestamp") for e in journal if e.get("timestamp")]
        start, end = to_eat(stamps[0]) if stamps else None, to_eat(stamps[-1]) if stamps else None
        logged = {r.get("stop_category", "") for r in read_tsv(SAFEGUARD_TSV)
                  if run_dir.name in (r.get("evidence") or "")} - {"", "TO_ASSESS", None}
        categories = ", ".join(sorted({str(e["stop_category"]) for e in stops
                                       if e.get("stop_category")} | logged)) or "not recorded"

        def token(key: str) -> str:
            return f"{totals[key]} ({unknown[key]} unknown)" if unknown[key] else str(totals[key])
        rows.append(Row(
            test_id=run_dir.name,
            kind="live_game" if live else "harness_test",
            title=f"{config['registration']} {'live game' if live else 'stub run'}",
            started_eat=fmt(start),
            ended_eat=fmt(end),
            duration_min=minutes(start, end),
            purpose=str(config.get("purpose") or ""),
            design_version=f"v17 ({str(config.get('prompt_sha256', ''))[:12]})",
            actor="host harness",
            backend=str(config.get("backend", "")),
            model=str(config.get("model", "")),
            reasoning_effort=str(config.get("effort", "")),
            cli_version=str(config.get("cli_version")
                            or (config.get("claude") or {}).get("pinned_version")
                            or ("unknown" if live else "none (stub)")),
            model_calls=str(len(calls)),
            input_tokens=token("input_tokens"),
            cached_input_tokens=token("cached_input_tokens"),
            output_tokens=token("output_tokens"),
            safeguard_stops=f"{len(stops)} ({categories})" if stops else "0",
            status=str(terminal.get("state", "no terminal record")).lower(),
            result=str(terminal.get("detail", "")),
            path=str(run_dir),
        ))
    logger.info("[INFO] host v17 runs registered: %d", len(rows))
    return rows


def index_times(root: Path) -> dict[str, dict[str, datetime]]:
    """Read created / running / answered times per handoff folder from a root's INDEX.md."""
    times: dict[str, dict[str, datetime]] = {}
    index = root / "INDEX.md"
    if not index.is_file():
        logger.warning("[WARNING] no handoff index at %s", index)
        return times
    pattern = re.compile(r"^- (\d{4}-\d\d-\d\d \d\d:\d\d) · `([^`]+)` · (\w+)")
    for line in index.read_text(encoding="utf-8").splitlines():
        match = pattern.match(line)
        if match:
            moment = datetime.strptime(match[1], "%Y-%m-%d %H:%M").replace(tzinfo=EAT)
            times.setdefault(match[2], {}).setdefault(match[3], moment)
    return times


def codex_rows() -> list[Row]:
    """Build one row per Codex handoff folder."""
    rows: list[Row] = []
    folders: list[Path] = []
    times: dict[str, dict[str, datetime]] = {}
    for root in HANDOFF_ROOTS:
        if not root.is_dir():
            logger.warning("[WARNING] no handoffs folder at %s", root)
            continue
        times.update(index_times(root))
        folders.extend(sorted(p for p in root.iterdir() if p.is_dir()))
    for folder in folders:
        totals: Counter[str] = Counter()
        model, turns = "", 0
        run_log = folder / "run.jsonl"
        if run_log.is_file():
            for event in read_jsonl(run_log):
                if event.get("type") == "turn.completed":
                    turns += 1
                    for key in ("input_tokens", "cached_input_tokens", "output_tokens"):
                        totals[key] += int((event.get("usage") or {}).get(key) or 0)
                model = model or str(event.get("model") or "")
        answer = folder / "answer.md"
        stamps = times.get(folder.name, {})
        start = stamps.get("running") or stamps.get("created")
        end = stamps.get("answered") or (
            datetime.fromtimestamp(answer.stat().st_mtime, EAT) if answer.is_file() else None)
        version = re.search(r"_ck-v(\d+)-", folder.name)
        taxonomy = re.search(r"taxonomy(?:-v(\d+))?", folder.name)
        plan = re.search(r"harness-production-plan-v(\d+)", folder.name)
        build = re.search(r"_core-build-(.+)$", folder.name)
        kind = "design_review"
        if version:
            title, design = f"Codex writes MW v{version[1]}", f"v{version[1]}"
            kind = "design_write"
        elif taxonomy:
            tree = f"taxonomy v{taxonomy[1] or 1}"
            title, design = f"Codex reviews mechanism {tree}", tree
        elif plan:
            title, design = f"Codex writes harness plan v{plan[1]}", f"plan v{plan[1]}"
            kind = "design_write"
        elif build:
            title, design = f"Codex builds harness: {build[1]}", "plan v3"
            kind = "harness_build"
        elif "harness-readiness-review" in folder.name:
            title, design = "Codex reviews harness readiness", "swarmsteg d3160cb"
        else:
            title, design = "Codex reviews MW v1", "v1"
        rows.append(Row(
            test_id=folder.name,
            kind=kind,
            title=title,
            started_eat=fmt(start),
            ended_eat=fmt(end),
            duration_min=minutes(start, end),
            design_version=design,
            actor="Codex (codex exec)",
            backend="codex",
            model=model or "Codex default (not in run log)",
            cli_version="unknown (not in run log)",
            processes_spawned="1",
            model_calls=str(turns),
            input_tokens=str(totals["input_tokens"]),
            cached_input_tokens=str(totals["cached_input_tokens"]),
            output_tokens=str(totals["output_tokens"]),
            status="answered" if answer.is_file() else "no answer (superseded or stopped)",
            path=str(folder),
        ))
    logger.info("[INFO] Codex handoffs registered: %d", len(rows))
    return rows


def review_verdict(version: str) -> tuple[str, str]:
    """Return the final VERDICT of the review of a version and its count of distinct seeds."""
    for review in REVIEWS.glob(f"round*_claude_attack_on_v{version}.md"):
        text = review.read_text(encoding="utf-8")
        verdicts = re.findall(r"VERDICT: ([A-Z ]+)", text)
        seeds = len(set(SEED.findall(text)))
        return (verdicts[-1].strip() if verdicts else "", str(seeds) if seeds else "")
    return "", ""


def subagent_rows() -> list[Row]:
    """Build one row per Claude subagent spawned in any session of this project."""
    rows: list[Row] = []
    for meta_path in sorted(CLAUDE_LOGS.glob("*/subagents/agent-*.meta.json")):
        meta = json.loads(meta_path.read_text(encoding="utf-8"))
        log = meta_path.with_name(meta_path.name.replace(".meta.json", ".jsonl"))
        usage_by_message: dict[str, dict[str, Any]] = {}
        stamps: list[datetime] = []
        versions: set[str] = set()
        efforts: set[str] = set()
        for entry in read_jsonl(log) if log.is_file() else iter(()):
            moment = to_eat(entry.get("timestamp"))
            if moment:
                stamps.append(moment)
            if entry.get("version"):
                versions.add(str(entry["version"]))
            if entry.get("effort"):
                efforts.add(str(entry["effort"]))
            message = entry.get("message") or {}
            if entry.get("type") == "assistant" and message.get("usage"):
                key = message.get("id") or str(len(usage_by_message))
                usage_by_message[key] = message["usage"]
        usages = usage_by_message.values()
        fresh = sum(int(u.get("input_tokens") or 0)
                    + int(u.get("cache_creation_input_tokens") or 0) for u in usages)
        cached = sum(int(u.get("cache_read_input_tokens") or 0) for u in usages)
        output = sum(int(u.get("output_tokens") or 0) for u in usages)
        description = str(meta.get("description", ""))
        review = REVIEW_DESCRIPTION.search(description)
        verdict, seeds = review_verdict(review[2]) if review else ("", "")
        start, end = (min(stamps), max(stamps)) if stamps else (None, None)
        rows.append(Row(
            test_id=f"claude_{log.stem.removeprefix('agent-')}",
            kind="design_review" if review else "support_agent",
            title=description,
            started_eat=fmt(start),
            ended_eat=fmt(end),
            duration_min=minutes(start, end),
            design_version=f"v{review[2]}" if review else "",
            actor=f"Claude subagent ({meta.get('agentType', '')})",
            backend="claude",
            model=str(meta.get("pickedEffortModel", "")),
            reasoning_effort=", ".join(sorted(efforts)) or "unknown",
            cli_version=", ".join(sorted(versions)) or "unknown",
            processes_spawned="1",
            model_calls=str(len(usage_by_message)),
            input_tokens=str(fresh + cached),
            cached_input_tokens=str(cached),
            output_tokens=str(output),
            seeded_figures=seeds,
            status="finished" if meta.get("finished") else "running",
            result=f"VERDICT: {verdict}" if verdict else "",
            path=str(log),
        ))
    logger.info("[INFO] Claude subagents registered: %d", len(rows))
    return rows


def manual_rows() -> list[Row]:
    """Read tests that left no machine log (probes, suites, audits), one full row each."""
    if not MANUAL_TSV.is_file():
        logger.warning("[WARNING] no manual register at %s", MANUAL_TSV)
        return []
    with MANUAL_TSV.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        unknown = set(reader.fieldnames or []) - set(COLUMNS)
        if unknown:
            raise ValueError(f"{MANUAL_TSV} has columns the register lacks: {sorted(unknown)}")
        rows = [Row(**{c: (r.get(c) or "") for c in COLUMNS}) for r in reader if r.get("test_id")]
    logger.info("[INFO] manual rows registered: %d", len(rows))
    return rows


def safeguard_index() -> dict[str, list[str]]:
    """Map each logged safeguard stop to the agent or run its actor field names."""
    index: dict[str, list[str]] = {}
    if not SAFEGUARD_TSV.is_file():
        logger.warning("[WARNING] no safeguard log at %s", SAFEGUARD_TSV)
        return index
    with SAFEGUARD_TSV.open(encoding="utf-8", newline="") as handle:
        for stop in csv.DictReader(handle, delimiter="\t"):
            text = " ".join(stop.get(k) or "" for k in ("actor", "task", "evidence"))
            for agent in re.findall(r"\ba[0-9a-f]{16}\b", text):
                index.setdefault(f"claude_{agent}", []).append(stop["stop_id"])
            for run in re.findall(r"\b(?:ck|mw)_[a-z0-9_]+\b", text):
                index.setdefault(run, []).append(stop["stop_id"])
    return index


def load_notes() -> dict[str, dict[str, str]]:
    """Read the hand-kept notes; an empty value leaves the logged value in place."""
    if not NOTES_TSV.is_file():
        logger.warning("[WARNING] no notes file at %s; purposes and results stay blank",
                       NOTES_TSV)
        return {}
    with NOTES_TSV.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        missing = set(NOTE_COLUMNS) - set(reader.fieldnames or [])
        if missing:
            raise ValueError(f"{NOTES_TSV} lacks columns {sorted(missing)}")
        return {r["test_id"]: r for r in reader if r.get("test_id")}


def previous_rows() -> dict[str, dict[str, str]]:
    """Rows already in the register, kept even if their source has since gone."""
    if not OUT_TSV.is_file():
        return {}
    with OUT_TSV.open(encoding="utf-8", newline="") as handle:
        return {r["test_id"]: r for r in csv.DictReader(handle, delimiter="\t")}


def merge(rows: list[Row], notes: dict[str, dict[str, str]]) -> list[dict[str, str]]:
    """Apply notes to logged rows and keep any earlier row whose source is missing."""
    merged: dict[str, dict[str, str]] = {}
    stops = safeguard_index()
    for row in rows:
        record = asdict(row)
        if stops.get(row.test_id):
            record["safeguard_stops"] = ", ".join(sorted(set(stops[row.test_id])))
        for column in NOTE_COLUMNS[1:] + OPTIONAL_NOTE_COLUMNS:
            note = ((notes.get(row.test_id) or {}).get(column) or "").strip()
            if not note:
                continue
            joins_logged = column == "result" and record[column]
            record[column] = f"{record[column]}; {note}" if joins_logged else note
        merged[row.test_id] = record
    for test_id, old in previous_rows().items():
        if test_id not in merged:
            old["status"] = f"{old.get('status', '')} (source no longer on disk)"
            merged[test_id] = {c: old.get(c, "") for c in COLUMNS}
    unmatched = sorted(set(notes) - set(merged))
    if unmatched:
        logger.warning("[WARNING] notes name tests not found in any log: %s", unmatched)
    return sorted(merged.values(), key=lambda r: (r["started_eat"] or "9999", r["test_id"]))


def md_cell(value: str) -> str:
    """Escape a value for a Markdown table cell."""
    return value.replace("|", "\\|").replace("\n", " ")


def thousands(value: str) -> str:
    """Format an integer string with thousands separators; pass anything else through."""
    return f"{int(value):,}" if value.isdigit() else value


def md_table(rows: list[dict[str, str]], columns: list[tuple[str, str]]) -> list[str]:
    """Render rows as a Markdown table with the given (column, header) pairs."""
    lines = ["| " + " | ".join(h for _, h in columns) + " |",
             "|" + "---|" * len(columns)]
    for row in rows:
        cells = [thousands(row[c]) if c.endswith(("tokens", "calls")) else row[c]
                 for c, _ in columns]
        lines.append("| " + " | ".join(md_cell(c) for c in cells) + " |")
    return lines


def totals_line(rows: list[dict[str, str]]) -> str:
    """Sum calls and tokens over a group of rows."""
    def total(column: str) -> int:
        return sum(int(r[column]) for r in rows if r[column].isdigit())
    return (f"{len(rows)} rows; {total('model_calls'):,} model calls; "
            f"{total('input_tokens'):,} input tokens "
            f"({total('cached_input_tokens'):,} cached); "
            f"{total('output_tokens'):,} output tokens.")


SECTIONS = (
    ("live_game", "1. Live games and pilots", [
        ("test_id", "Test"), ("started_eat", "Started (EAT)"), ("duration_min", "Min"),
        ("purpose", "Why"), ("decided_by", "Decided by"), ("design_version", "Design"),
        ("backend", "Provider"), ("model", "Model"), ("reasoning_effort", "Effort"),
        ("cli_version", "CLI"), ("games", "Games"),
        ("plies_per_game", "Plies"), ("teams_members", "Teams"),
        ("agent_roles", "Agent roles"), ("processes_spawned", "Processes"),
        ("model_calls", "Calls"), ("input_tokens", "Input tokens"),
        ("output_tokens", "Output tokens"), ("audit_notes", "Audit notes"),
        ("safeguard_stops", "Stops"), ("status", "Status"), ("result", "Result"),
        ("record", "Record")]),
    ("live_probe", "2. Live probes and checks (single model calls outside a game)", [
        ("test_id", "Test"), ("started_eat", "Started (EAT)"), ("purpose", "Why"),
        ("decided_by", "Decided by"), ("backend", "Provider"), ("model", "Model"),
        ("reasoning_effort", "Effort"), ("cli_version", "CLI"), ("model_calls", "Calls"), ("input_tokens", "Input tokens"),
        ("output_tokens", "Output tokens"), ("result", "Result"), ("record", "Record"),
        ("path", "Evidence")]),
    ("design_write", "3. Design loop: each MW version written", [
        ("design_version", "Version"), ("test_id", "Test"), ("actor", "Writer"),
        ("started_eat", "Started (EAT)"), ("duration_min", "Min"), ("purpose", "Why"),
        ("decided_by", "Decided by"), ("model_calls", "Turns"),
        ("input_tokens", "Input tokens"), ("output_tokens", "Output tokens"),
        ("safeguard_stops", "Stops"), ("status", "Status"), ("result", "Result"),
        ("record", "Record")]),
    ("design_review", "4. Design loop: adversarial reviews and their simulations", [
        ("design_version", "Reviews"), ("test_id", "Test"), ("actor", "Reviewer"),
        ("started_eat", "Started (EAT)"), ("duration_min", "Min"), ("model", "Model"),
        ("reasoning_effort", "Effort"), ("cli_version", "CLI"),
        ("model_calls", "Calls"), ("input_tokens", "Input tokens"),
        ("output_tokens", "Output tokens"), ("seeded_figures", "Seeds cited"),
        ("safeguard_stops", "Stops"), ("result", "Result"), ("record", "Record")]),
    ("harness_suite", "5. Harness test suites (stub agents, no model calls)", [
        ("test_id", "Test"), ("started_eat", "Started (EAT)"), ("purpose", "What it tested"),
        ("result", "Result"), ("record", "Record"), ("path", "Script")]),
    ("harness_test", "6. Individual stub runs (no model calls)", [
        ("test_id", "Test"), ("started_eat", "Started (EAT)"), ("purpose", "What it tested"),
        ("design_version", "Design"), ("plies_per_game", "Plies"),
        ("audit_notes", "Audit notes"), ("status", "Outcome"), ("result", "Detail"),
        ("record", "Record")]),
    ("tooling_test", "7. Literature and tooling tests (ladder, ledgers, hooks)", [
        ("test_id", "Test"), ("started_eat", "Started (EAT)"), ("purpose", "Why"),
        ("decided_by", "Decided by"), ("result", "Result"), ("record", "Record"),
        ("path", "Evidence")]),
    ("analysis", "8. Analysis runs (telemetry, report rebuilds)", [
        ("test_id", "Test"), ("started_eat", "Started (EAT)"), ("purpose", "Why"),
        ("result", "Result"), ("record", "Record"), ("path", "Outputs")]),
    ("support_agent", "9. Other agents and sessions (literature, reading, reports, builds)", [
        ("title", "Task"), ("test_id", "Agent"), ("started_eat", "Started (EAT)"),
        ("duration_min", "Min"), ("model", "Model"), ("reasoning_effort", "Effort"),
        ("cli_version", "CLI"), ("model_calls", "Calls"),
        ("input_tokens", "Input tokens"), ("output_tokens", "Output tokens"),
        ("safeguard_stops", "Stops"), ("status", "Status")]),
)


def render_markdown(rows: list[dict[str, str]], built: datetime) -> str:
    """Render the readable register: one section per kind, each with its totals."""
    lines = [
        "# Hypersteg test register",
        "",
        f"Built {fmt(built)} EAT by `python -m harness.test_register` from the run logs. "
        "Counts, tokens and times come from the logs; why, who decided and the result come "
        "from `audits/test_register_notes.tsv`; tests that left no machine log are in "
        "`audits/test_register_manual.tsv`. Every column for every row is in "
        "`audits/test_register.tsv`. Times are EAT (UTC+3). Input tokens include cached "
        "input; a blank cell means the source does not record the value.",
        "",
        "Totals: " + totals_line(rows),
    ]
    for kind, heading, columns in SECTIONS:
        group = [r for r in rows if r["kind"] == kind]
        lines += ["", f"## {heading}", "", totals_line(group), ""]
        lines += md_table(group, columns) if group else ["None yet."]
    return "\n".join(lines) + "\n"


def write_outputs(rows: list[dict[str, str]]) -> list[Path]:
    """Write the TSV, the live Markdown and a new immutable Markdown snapshot."""
    built = datetime.now(EAT)
    OUT_TSV.parent.mkdir(parents=True, exist_ok=True)
    with OUT_TSV.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=COLUMNS, delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)
    markdown = render_markdown(rows, built)
    OUT_MD.write_text(markdown, encoding="utf-8")
    SNAPSHOTS.mkdir(parents=True, exist_ok=True)
    stem = f"TEST_REGISTER_{built:%Y%m%d_%H%M}"
    snapshot = SNAPSHOTS / f"{stem}.md"
    suffix = 0
    while snapshot.exists():
        suffix += 1
        snapshot = SNAPSHOTS / f"{stem}_{suffix}.md"
    with snapshot.open("x", encoding="utf-8") as handle:
        handle.write(markdown)
    return [OUT_TSV, OUT_MD, snapshot]


def main() -> int:
    """Collect every source, merge the notes and write the register."""
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    rows = arena_rows() + host_rows() + codex_rows() + subagent_rows() + manual_rows()
    if not rows:
        logger.error("[ERROR] no tests found in any source; nothing written")
        return 1
    merged = merge(rows, load_notes())
    for kind, count in sorted(Counter(r["kind"] for r in merged).items()):
        logger.info("[INFO] %s: %d", kind, count)
    for path in write_outputs(merged):
        logger.info("[INFO] wrote %s", path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
