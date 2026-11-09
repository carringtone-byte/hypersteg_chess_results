# Hypersteg Chess Results and Reproduction

This repository contains recorded experiment data, figures, the novelty kit, and the Python harnesses used to initialize and validate Hypersteg Chess runs. Research reports are excluded.

- `results/`: JSON/JSONL telemetry, PGN games, CSV metrics, and PNG figures.
- `hypersteg_novelty_kit_20261108/`: literature claim ledgers, mechanism/approach taxonomies, network HTML maps, images, and generation/audit tools.
- `harness/`: pinned Python environment metadata, harness source, prompts, configuration, and validation tests.

## Reproduce the harness environment

Requires Python 3.11.9 (recorded as `.python-version`). From PowerShell:

```powershell
cd harness
py -3.11 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-lock.txt
$env:PYTHONPATH = "src"
.\.venv\Scripts\python.exe -m hypersteg.cli smoke
.\.venv\Scripts\python.exe -m pytest
```

The installed `python-chess`, `chess`, and pytest dependency versions are pinned in `requirements-lock.txt`.

## Initialize the bounded 20-ply harness

This is the controlled 10-full-move protocol (20 plies), with a hard stop after Black's tenth move. It initializes a fresh run package; the CLI does not invoke models.

```powershell
$env:PYTHONPATH = "src"
.\.venv\Scripts\python.exe -m hypersteg.cli init-live-10 --output ..\results
```

## Initialize the full-game harness

This harness continues until a chess-rule ending and records review checkpoints every 20 plies. The command initializes the run and does not itself call agents or play moves.

```powershell
$env:PYTHONPATH = "src"
.\.venv\Scripts\python.exe -m hypersteg.cli init-live-full --checkpoint-plies 20 --output ..\results
```

Both live harnesses require an external/manual agent orchestrator to follow `src/hypersteg/live_protocol.py`. No model-provider adapter is included. The historical live games are preserved as data, but exact LLM outputs cannot be regenerated: some original prompts and provider sampling metadata were not recorded. The deterministic mock harness and the event-gate code can be rerun; live-run telemetry can be audited but is not bit-for-bit reproducible.

The two novelty-network pages are in `hypersteg_novelty_kit_20261108/maps/`; open either HTML file in a browser, keeping `haki_logo.png` in the same directory.

This repository is local until a GitHub remote is configured and pushed.
