"""Manual budget stop guard. Mock mode is always offline."""
from pathlib import Path


def is_stopped(run_dir: Path) -> bool:
    return (run_dir / "STOP_MODEL_CALLS").exists()


def require_live_allowed(run_dir: Path) -> None:
    if is_stopped(run_dir):
        raise RuntimeError("Budget stop flag is set; model provider launch blocked")
    raise RuntimeError("Live providers are not enabled in this offline pilot build")
