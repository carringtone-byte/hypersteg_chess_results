# === SCRIPT: Export the chess harness to a new swarmsteg folder ===
# INPUTS:  harness/, CK_REPRODUCIBILITY_SYSTEM_PROMPT.md, prompts/MW_SYSTEM_PROMPT_v12.md and v13.md
# OUTPUTS: <dest>/ — a new folder holding the shareable subset, a README, environment.yml and
#          .gitignore; the run refuses a destination that already exists
"""Export the shareable subset of the harness to a new folder for the swarmsteg repo.

The export never writes into an existing folder. To update the swarmsteg repo, export to a new
folder and compare it with the repo (`diff -r`), then apply the changes there by hand.

Usage (from the hypersteg project root):
    python tools/export_swarmsteg.py --dest ../swarmsteg
    python tools/export_swarmsteg.py --dest <scratch>/swarmsteg_20261106_1500
"""

from __future__ import annotations

import argparse
import json
import logging
import shutil
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
ROOT_FILES = ("CK_REPRODUCIBILITY_SYSTEM_PROMPT.md",)
PROMPT_FILES = ("prompts/MW_SYSTEM_PROMPT_v12.md", "prompts/MW_SYSTEM_PROMPT_v13.md")
HARNESS_EXCLUDED_NAMES = {"__pycache__", "canary_registry.jsonl", "test_register.py",
                          "CANARY_DO_NOT_READ.md", ".DS_Store"}
ARENA_DEFAULTS = ("harness/ck/params.py", "harness/mw/params.py")
USAGE_OLD = "from the hypersteg project root, conda env hypersteg_env"
USAGE_NEW = "from the repo root, conda env swarmsteg_env"
CANARY_LOCATIONS = {"project_root": ".", "prompts": "prompts", "arena_runs": "{arena_root}/runs"}

ENVIRONMENT_YML = """name: swarmsteg_env
channels:
  - conda-forge
dependencies:
  - python=3.12
  - python-chess=1.11
  - numpy=2.5
  - pyyaml=6.0
  - matplotlib=3.10
  - pytest=9.0
"""

GITIGNORE = """__pycache__/
*.pyc
.DS_Store
# Planted canaries and their registry are local to each machine.
harness/canary_registry.jsonl
CANARY_DO_NOT_READ.md
# Run outputs and logs stay out of git.
audits/
reports/
outputs/
plots/
"""

README = """# swarmsteg

Teams of LLM agents play chess and may hide messages in ordinary-sounding public commentary or
in their choice of move. Teammates try to decode; the opposing team tries to recover the
message from public information alone. This repo holds the host harness that runs those games
under isolation and records every call.

## Contents

- `CK_REPRODUCIBILITY_SYSTEM_PROMPT.md`: the CK baseline protocol, run by `harness/run_ck.py`.
- `prompts/MW_SYSTEM_PROMPT_v12.md`: the MW protocol the MW harness implements
  (`harness/run_mw.py`, pilots A3 and B20).
- `prompts/MW_SYSTEM_PROMPT_v13.md`: the latest MW protocol. **Draft: its review is not yet
  satisfied, and the harness does not implement it yet.**
- `harness/`: orchestrator, isolation layers, Stockfish engine wrapper, stores, reports and
  telemetry; `harness/mw/test_stub_runs.py` is the stub suite.

## Setup

1. `conda env create -f environment.yml && conda activate swarmsteg_env`
2. Install Stockfish (macOS: `brew install stockfish`). If it is not at
   `/opt/homebrew/bin/stockfish`, set `SWARMSTEG_STOCKFISH` to its path.
3. Install the Codex CLI and log in (`codex login`). Live agents run on your own OpenAI account:
   each agent gets a private `CODEX_HOME` that links only to `~/.codex/auth.json`.
4. The arena, where runs are written, defaults to `../swarmsteg_arena` next to this repo; set
   `SWARMSTEG_ARENA` to put it elsewhere. Create `<arena>/runs/` before the first run.
5. Plant your own canaries once: `python -m harness.canaries plant`. Each canary is a random
   string in a file agents are never shown; finding it in agent output proves a leak.

## Running

From the repo root:

    python -m harness.run_ck --backend stub                 # CK game, no model calls
    python -m harness.run_ck --backend codex --live         # one live CK game
    python -m harness.run_mw --pilot a3 --backend stub      # MW pilot A, no model calls
    python -m harness.run_mw --pilot a3 --backend codex --live --purpose "..."
    python -m pytest -q harness/mw/test_stub_runs.py        # stub suite

Live runs need both `--backend codex` and `--live`, and spend the account's quota. Each run
writes `<arena>/runs/<run_id>/` with a public PGN (commentary as PGN comments), a public and
a host HTML view, and the full call log.

## Limits

Isolation is procedural (per-call context, disabled tools, private Codex homes, canaries), not
cryptographic, and it cannot remove what a model learnt in training.
"""

logger = logging.getLogger(__name__)


def export(dest: Path) -> list[Path]:
    """Copy the shareable subset into `dest`, which must not exist yet."""
    if dest.exists():
        raise FileExistsError(f"Destination already exists: {dest}; export to a new folder")
    written: list[Path] = []
    ignore = shutil.ignore_patterns(*HARNESS_EXCLUDED_NAMES)
    shutil.copytree(PROJECT_ROOT / "harness", dest / "harness", ignore=ignore)
    written.extend(p for p in (dest / "harness").rglob("*") if p.is_file())
    (dest / "prompts").mkdir()
    for rel in ROOT_FILES + PROMPT_FILES:
        target = dest / rel
        shutil.copy2(PROJECT_ROOT / rel, target)
        written.append(target)
    for rel in ARENA_DEFAULTS:
        path = dest / rel
        text = path.read_text(encoding="utf-8")
        if text.count('"hypersteg_arena"') != 1:
            raise ValueError(f"Expected one arena default in {path}")
        path.write_text(text.replace('"hypersteg_arena"', '"swarmsteg_arena"'), encoding="utf-8")
    for path in (dest / "harness").rglob("*.py"):
        text = path.read_text(encoding="utf-8")
        if USAGE_OLD in text:
            path.write_text(text.replace(USAGE_OLD, USAGE_NEW), encoding="utf-8")
    locations = dest / "harness" / "canary_locations.json"
    locations.write_text(json.dumps(CANARY_LOCATIONS, indent=2) + "\n", encoding="utf-8")
    for name, content in (("README.md", README), ("environment.yml", ENVIRONMENT_YML),
                          (".gitignore", GITIGNORE)):
        target = dest / name
        with target.open("x", encoding="utf-8") as fh:
            fh.write(content)
        written.append(target)
    return written


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--dest", type=Path, required=True)
    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(message)s")
    dest = args.dest.resolve()
    written = export(dest)
    logger.info("Exported %d files to %s", len(written), dest)
    for path in sorted(written):
        logger.info("  %s", path.relative_to(dest))
    return 0


if __name__ == "__main__":
    sys.exit(main())
