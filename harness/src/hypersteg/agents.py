"""Deterministic fixture/mock actor. No network or model calls."""
from __future__ import annotations


def mock_action(team: str, role: str, phase: str, fen: str, message: str, recommended_uci: str | None = None) -> dict:
    prefix = "W" if team == "white" else "B"
    suffix = "Analyst" if role == "analyst" else "Captain"
    return {
        "team": team,
        "agent_id": f"{prefix}-{suffix}",
        "phase": phase,
        "action": "post_public",
        "message": message,
        "recommended_uci": recommended_uci,
    }


def validate_action(action: dict, expected_phase: str, team: str, allowed_action: str = "post_public") -> None:
    required = {"team", "agent_id", "phase", "action", "message", "recommended_uci"}
    if set(action) != required:
        raise ValueError("Action must contain exactly the required schema keys")
    if action["team"] != team or action["phase"] != expected_phase or action["action"] != allowed_action:
        raise ValueError("Action team, phase, or action type is invalid")
    if not isinstance(action["message"], str):
        raise ValueError("message must be a string")
