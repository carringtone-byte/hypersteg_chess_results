"""Host-controlled append-only JSONL stores."""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path


def append_jsonl(path: Path, record: dict) -> dict:
    path.parent.mkdir(parents=True, exist_ok=True)
    enriched = dict(record)
    enriched.setdefault("timestamp", datetime.now(timezone.utc).isoformat())
    with path.open("a", encoding="utf-8") as stream:
        stream.write(json.dumps(enriched, ensure_ascii=False, sort_keys=True) + "\n")
    return enriched


def read_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with path.open(encoding="utf-8") as stream:
        return [json.loads(line) for line in stream if line.strip()]


def append_public(root: Path, record: dict) -> dict:
    return append_jsonl(root / "public.jsonl", record)


def append_private(root: Path, team: str, record: dict) -> dict:
    if team not in {"white", "black"}:
        raise ValueError("team must be white or black")
    return append_jsonl(root / "private" / f"{team}.jsonl", record)
