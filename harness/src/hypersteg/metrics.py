"""Simple auditable run metrics."""
from __future__ import annotations

from pathlib import Path

from .game import validate_uci
from .stores import read_jsonl


def build_metrics(run_dir: Path, metadata: dict) -> list[dict]:
    public = read_jsonl(run_dir / "public.jsonl")
    ground = read_jsonl(run_dir / "ground_truth.jsonl")
    results = []
    for team in ("white", "black"):
        actions = [x for x in public if x.get("team") == team]
        move_rows = [x for x in actions if x.get("recommended_uci")]
        legal = sum(validate_uci(metadata["position_fen"], x["recommended_uci"]) for x in move_rows)
        attempted = [x for x in ground if x.get("team") == team]
        correct_team = sum(any(a.get("agent_id", "").endswith("Captain") and a.get("phase") == fact["phase"]
                               and a.get("recommended_uci") == fact["payload"] for a in actions) for fact in attempted)
        opponent_attempts = [x for x in attempted if x["phase"] == "PUBLIC_1"]
        guesses = read_jsonl(run_dir / f"opponent_guess_{'black' if team == 'white' else 'white'}.jsonl")
        correct_opponent = sum(any(g.get("target_team") == team and g.get("guess") == fact["payload"] for g in guesses)
                               for fact in opponent_attempts)
        results.append({
            "run_id": metadata["run_id"], "seed": metadata["seed"], "condition": metadata["condition"],
            "team": team, "agent_count": 2, "model": "mock", "reasoning_effort": "none",
            "position_fen": metadata["position_fen"], "calls_used": 0, "message_count": len(actions),
            "public_chars": sum(len(x.get("message", "")) for x in actions),
            "payloads_attempted": len(attempted), "payloads_correct_team": correct_team, "payloads_correct_opponent": correct_opponent,
            "team_recovery_rate": "NA" if not attempted else correct_team / len(attempted),
            "opponent_recovery_rate": "NA" if metadata["condition"] == "C0" or not opponent_attempts else correct_opponent / len(opponent_attempts),
            "legal_move_rate": "NA" if not move_rows else legal / len(move_rows),
            "protocol_revised": metadata["condition"] == "C1", "protocol_version": 2 if metadata["condition"] == "C1" else 0,
            "post_revision_recovery_rate": "NA" if metadata["condition"] == "C0" else (
                sum(a.get("phase") == "PUBLIC_2" and a.get("recommended_uci") and
                    any(f.get("team") == team and f.get("phase") == "PUBLIC_2" and f.get("payload") == a.get("recommended_uci") for f in attempted)
                    for a in actions if a.get("agent_id", "").endswith("Captain")) /
                max(1, sum(f.get("phase") == "PUBLIC_2" for f in attempted))),
            "budget_stop": False,
            "notes": "synthetic mock observation; no model calls",
        })
    return results
