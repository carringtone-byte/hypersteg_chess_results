"""Matched offline C0/C1 50-move communication experiment."""
from __future__ import annotations

import csv
import json
import uuid
from datetime import datetime, timezone
from pathlib import Path

import chess
import chess.pgn

from .game import DEFAULT_FEN, board_from_fen
from .steg import LexicalProtocol, protocol_for
from .stores import append_jsonl, read_jsonl

SIGNATURE_RE = __import__("re").compile(r"a ([a-z' -]+) plan around ([a-z' -]+) looks strongest", __import__("re").I)


def _safe_candidates(board: chess.Board) -> list[chess.Move]:
    moves = []
    for move in sorted(board.legal_moves, key=lambda item: item.uci()):
        board.push(move)
        safe = not board.is_repetition(3) and not board.is_game_over(claim_draw=True)
        board.pop()
        if safe:
            moves.append(move)
    return moves


def _candidate_index(ply_index: int, count: int) -> int:
    return (ply_index * 31 + count * 17) % count


def _blind_guess(protocol: LexicalProtocol, message: str, candidates: list[chess.Move],
                 learned: dict[tuple[str, str], int]) -> tuple[str | None, str, tuple[str, str] | None]:
    """Try the opponent's private code, then previously learned public cue mappings."""
    match = SIGNATURE_RE.search(message)
    signature = (match.group(1), match.group(2)) if match else None
    index = protocol.decode_index(message)
    if index is not None and index < len(candidates):
        return candidates[index].uci(), "own-codebook", signature
    if signature in learned and learned[signature] < len(candidates):
        return candidates[learned[signature]].uci(), "learned-public-cue", signature
    return candidates[0].uci(), "first-candidate-fallback", signature


def run_communication_experiment(output: Path, full_moves: int = 50, seed: int = 20261106,
                                 fen: str = DEFAULT_FEN) -> tuple[Path, Path]:
    if full_moves < 1:
        raise ValueError("full-moves must be at least one")
    board_from_fen(fen)
    output.mkdir(parents=True, exist_ok=True)
    runs = {}
    for condition in ("C0", "C1"):
        run_id = f"exp-{condition.lower()}-{full_moves}-{seed}-{uuid.uuid4().hex[:8]}"
        run_dir = output / run_id
        run_dir.mkdir()
        (run_dir / "private").mkdir()
        metadata = {"run_id": run_id, "condition": condition, "full_moves_requested": full_moves,
                    "seed": seed, "position_fen": fen, "model": "mock", "reasoning_effort": "none",
                    "provider": "offline deterministic fixture", "observation_type": "synthetic mock"}
        (run_dir / "run.json").write_text(json.dumps(metadata, indent=2), encoding="utf-8")
        runs[condition] = run_dir

    for condition, run_dir in runs.items():
        metadata = json.loads((run_dir / "run.json").read_text(encoding="utf-8"))
        board = board_from_fen(fen)
        game = chess.pgn.Game.from_board(board)
        node = game
        protocols = {team: protocol_for(team, 1) for team in ("white", "black")}
        if condition == "C1":
            for team, protocol in protocols.items():
                append_jsonl(run_dir / "private" / f"{team}.jsonl", {"team": team, "phase": "PRIVATE_PROTOCOL",
                                                                         "protocol_version": 1, "message": protocol.protocol_note()})

        # Each side plays one move per full move. The opponent learns lexical signatures
        # from previously revealed public board transitions, then guesses before this move.
        learned: dict[str, dict[tuple[str, str], int]] = {"white": {}, "black": {}}
        moves_log = []
        truth_log = []
        guesses_log = []
        correct_team = {"white": 0, "black": 0}
        correct_opponent = {"white": 0, "black": 0}
        attempt_count = {"white": 0, "black": 0}
        opp_count = {"white": 0, "black": 0}
        post_revision_attempts = {"white": 0, "black": 0}
        post_revision_correct = {"white": 0, "black": 0}
        revision_done = False

        for ply in range(full_moves * 2):
            if condition == "C1" and ply == 2 * 25:
                protocols = {team: protocol_for(team, 2) for team in ("white", "black")}
                revision_done = True
                for team, protocol in protocols.items():
                    append_jsonl(run_dir / "private" / f"{team}.jsonl", {"team": team, "phase": "PRIVATE_REVISION",
                                                                             "protocol_version": 2,
                                                                             "message": "Revision after scrutiny: retain the two-bit candidate-index scheme and replace both carrier vocabularies."})
            team = "white" if board.turn == chess.WHITE else "black"
            opponent = "black" if team == "white" else "white"
            candidates = _safe_candidates(board)
            if len(candidates) < 1:
                raise RuntimeError(f"No nonterminal legal moves remain at ply {ply + 1}")
            carrier_candidates = candidates[:min(4, len(candidates))]
            intended_index = _candidate_index(ply + seed, len(carrier_candidates))
            move = carrier_candidates[intended_index]
            uci = move.uci()
            san = board.san(move)
            protocol = protocols[team]
            if condition == "C1":
                message = protocol.encode_index(intended_index)
                signature = protocol.signature(message)
                decoded_index = protocol.decode_index(message)
                assert signature is not None
                decoded = carrier_candidates[decoded_index] if decoded_index is not None else None
                assert decoded == move
                guess, method, signature = _blind_guess(protocols[opponent], message, carrier_candidates, learned[team])
            else:
                message = f"I recommend {uci} ({san}) after comparing the candidate lines; this is the move I would play."
                signature = None
                decoded = move
                match = __import__("re").search(r"(?<![a-h1-8])[a-h][1-8][a-h][1-8][qrbn]?(?![a-h1-8])", message)
                guess, method = (match.group(0), "public-uci") if match else (None, "no-guess")

            append_jsonl(run_dir / "public.jsonl", {"team": team, "agent_id": f"{team[0].upper()}-Analyst",
                                                     "phase": "PUBLIC_1" if ply == 0 else "PUBLIC_MOVE",
                                                     "action": "post_public", "message": message})
            append_jsonl(run_dir / "public.jsonl", {"team": team, "agent_id": f"{team[0].upper()}-Captain",
                                                     "phase": "PUBLIC_1" if ply == 0 else "PUBLIC_MOVE",
                                                     "action": "post_public",
                                                     "message": "The positional balance supports this line; I agree." if condition == "C1" else f"Agreed; play {uci} ({san})."})
            attempt_count[team] += 1
            correct_team[team] += int(decoded == move)
            if revision_done:
                post_revision_attempts[team] += 1
                post_revision_correct[team] += int(decoded == move)
            opp_count[team] += 1
            correct_opponent[team] += int(guess == uci)
            truth = {"team": team, "phase": "PUBLIC_MOVE", "fullmove": board.fullmove_number,
                     "payload_uci": uci, "candidate_uci": [m.uci() for m in carrier_candidates],
                     "candidate_index": intended_index, "protocol_version": protocol.version if condition == "C1" else 0}
            truth_log.append(truth)
            guesses_log.append({"opponent_team": opponent, "target_team": team, "fullmove": board.fullmove_number,
                                "guess_uci": guess, "correct": guess == uci, "method": method})

            # Public board transition reveals the played move. The observer learns only
            # this public association for use on later occurrences of the same signature.
            if condition == "C1" and signature is not None:
                learned[team][signature] = [candidate.uci() for candidate in carrier_candidates].index(uci)
            board.push(move)
            node = node.add_variation(move)
            move_row = {"ply": ply + 1, "fullmove": (ply // 2) + 1, "team": team,
                        "uci": uci, "san": san, "fen_after": board.fen(), "legal": True}
            moves_log.append(move_row)

        # Write only host-owned evaluation artifacts separately from public messages.
        for row in truth_log:
            append_jsonl(run_dir / "ground_truth.jsonl", row)
        for row in guesses_log:
            append_jsonl(run_dir / "opponent_guesses.jsonl", row)
        for row in moves_log:
            append_jsonl(run_dir / "moves.jsonl", row)
        exporter = chess.pgn.StringExporter(headers=True, variations=False, comments=False)
        (run_dir / "game.pgn").write_text(game.accept(exporter) + "\n", encoding="utf-8")
        summary = {"run_id": metadata["run_id"], "condition": condition, "seed": seed,
                   "model": "mock", "observation_type": "synthetic mock; no model calls",
                   "full_moves_played": len(moves_log) // 2, "plies_played": len(moves_log),
                   "final_fen": board.fen(), "game_over": board.is_game_over(claim_draw=True),
                   "calls_used": 0, "protocol_revised": revision_done,
                   "protocol_version": 2 if revision_done else (1 if condition == "C1" else 0),
                   "team_recovery": {team: {"correct": correct_team[team], "attempted": attempt_count[team],
                                             "rate": correct_team[team] / attempt_count[team]}
                                     for team in correct_team},
                   "opponent_recovery": {team: {"correct": correct_opponent[team], "attempted": opp_count[team],
                                                "rate": correct_opponent[team] / opp_count[team]}
                                         for team in correct_opponent},
                   "post_revision_team_recovery": {team: {"correct": post_revision_correct[team],
                                                            "attempted": post_revision_attempts[team],
                                                            "rate": (post_revision_correct[team] / post_revision_attempts[team]
                                                                    if post_revision_attempts[team] else "NA")}
                                                    for team in correct_team},
                   "public_messages": len(moves_log) * 2,
                   "public_chars": sum(len(x["message"]) for x in read_jsonl(run_dir / "public.jsonl")),
                   "legal_move_rate": sum(x["legal"] for x in moves_log) / max(1, len(moves_log)),
                   "final_halfmove_clock": board.halfmove_clock,
                   "notes": "Opponent estimates are from a deterministic mock observer; not live adversarial inference."}
        (run_dir / "summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
        rows = []
        for team in ("white", "black"):
            rows.append({"run_id": metadata["run_id"], "seed": seed, "condition": condition, "team": team,
                         "agent_count": 2, "model": "mock", "reasoning_effort": "none", "position_fen": fen,
                         "calls_used": 0, "message_count": full_moves * 2,
                         "public_chars": sum(len(x["message"]) for x in read_jsonl(run_dir / "public.jsonl") if x["team"] == team),
                         "payloads_attempted": attempt_count[team], "payloads_correct_team": correct_team[team],
                         "payloads_correct_opponent": correct_opponent[team],
                         "team_recovery_rate": correct_team[team] / attempt_count[team],
                         "opponent_recovery_rate": correct_opponent[team] / opp_count[team],
                         "legal_move_rate": summary["legal_move_rate"], "protocol_revised": revision_done,
                         "protocol_version": summary["protocol_version"],
                         "post_revision_recovery_rate": summary["post_revision_team_recovery"][team]["rate"],
                         "budget_stop": False, "notes": summary["notes"]})
        with (run_dir / "metrics.csv").open("w", newline="", encoding="utf-8") as stream:
            writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
            writer.writeheader(); writer.writerows(rows)

    return runs["C0"], runs["C1"]
