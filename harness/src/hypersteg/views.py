"""Role and team scoped prompt projections."""
from __future__ import annotations

from pathlib import Path

from .stores import read_jsonl


def agent_view(run_dir: Path, team: str, role: str, phase: str, fen: str, task: str = "", include_private: bool = False) -> dict:
    own = read_jsonl(run_dir / "private" / f"{team}.jsonl") if include_private else []
    public = read_jsonl(run_dir / "public.jsonl")
    if phase == "OPPONENT_ANALYSIS":
        opponent = "black" if team == "white" else "white"
        public = [message for message in public if message.get("team") == opponent]
    return {
        "team": team,
        "role": role,
        "phase": phase,
        "position_fen": fen,
        "task": task,
        "public_messages": public,
        "own_protocol_messages": own,
    }
