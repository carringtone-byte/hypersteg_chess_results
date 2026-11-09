"""Export run metadata and CSV metrics."""
from __future__ import annotations

import csv
import json
from pathlib import Path

from .metrics import build_metrics


def export_run(run_dir: Path) -> Path:
    metadata = json.loads((run_dir / "run.json").read_text(encoding="utf-8"))
    rows = build_metrics(run_dir, metadata)
    output = run_dir / "metrics.csv"
    with output.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    return output
