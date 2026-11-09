import json
from pathlib import Path

import pytest

from hypersteg.cli import run_chess_smoke, run_mock
from hypersteg.experiment import run_communication_experiment
from hypersteg.game import DEFAULT_FEN, board_from_fen, play_legal_plies, validate_uci
from hypersteg.state import RunState
from hypersteg.steg import protocol_for
from hypersteg.stores import append_private
from hypersteg.views import agent_view


def test_default_position_and_move_validation():
    board = board_from_fen(DEFAULT_FEN)
    assert board.is_valid()
    assert validate_uci(DEFAULT_FEN, next(iter(board.legal_moves)).uci())
    assert not validate_uci(DEFAULT_FEN, "e2e5")


def test_phase_machine_rejects_skip():
    state = RunState("C1")
    with pytest.raises(ValueError):
        state.advance("PUBLIC_1")


def test_team_views_do_not_leak_other_private_protocol(tmp_path):
    (tmp_path / "private").mkdir()
    append_private(tmp_path, "white", {"team": "white", "message": "WHITE_SENTINEL"})
    append_private(tmp_path, "black", {"team": "black", "message": "BLACK_SENTINEL"})
    white = json.dumps(agent_view(tmp_path, "white", "analyst", "PRIVATE_PROTOCOL", DEFAULT_FEN, include_private=True))
    black = json.dumps(agent_view(tmp_path, "black", "analyst", "PRIVATE_PROTOCOL", DEFAULT_FEN, include_private=True))
    assert "WHITE_SENTINEL" in white and "BLACK_SENTINEL" not in white
    assert "BLACK_SENTINEL" in black and "WHITE_SENTINEL" not in black


@pytest.mark.parametrize("condition", ["C0", "C1"])
def test_mock_run_completes_and_exports_metrics(tmp_path, condition):
    run_dir = run_mock(tmp_path, condition=condition, seed=7)
    state = json.loads((run_dir / "state.json").read_text())
    assert state["phase"] == "COMPLETE"
    assert (run_dir / "metrics.csv").exists()
    assert (run_dir / "events.jsonl").exists()


def test_illegal_fen_rejected():
    with pytest.raises(ValueError):
        board_from_fen("not a fen")


def test_five_full_moves_are_legal_and_exported(tmp_path):
    final_board, rows, pgn = play_legal_plies(plies=10)
    assert len(rows) == 10
    assert final_board.is_valid()
    assert "1." in pgn and "5." in pgn
    run_dir = run_chess_smoke(tmp_path, full_moves=5)
    summary = json.loads((run_dir / "summary.json").read_text())
    assert summary["plies_played"] == 10
    assert (run_dir / "moves.jsonl").exists()
    assert (run_dir / "game.pgn").exists()


def test_pgn_continuation_preserves_game_history(tmp_path):
    first = run_chess_smoke(tmp_path, full_moves=5)
    continued = run_chess_smoke(tmp_path, full_moves=2, continue_from=first)
    summary = json.loads((continued / "summary.json").read_text())
    assert summary["full_moves_played"] == 2
    assert summary["total_full_moves"] == 7
    assert len((continued / "moves.jsonl").read_text().splitlines()) == 4
    assert "7." in (continued / "game.pgn").read_text()
    assert summary["plies_played"] == 4


def test_private_lexical_protocol_round_trip():
    protocol = protocol_for("white", 1)
    for index in range(4):
        message = protocol.encode_index(index)
        assert protocol.decode_index(message) == index
        assert "[MOVE:" not in message


def test_paired_50_move_communication_experiment(tmp_path):
    c0, c1 = run_communication_experiment(tmp_path, full_moves=50, seed=11)
    c0_summary = json.loads((c0 / "summary.json").read_text())
    c1_summary = json.loads((c1 / "summary.json").read_text())
    assert c0_summary["run_id"] == c0.name and c1_summary["run_id"] == c1.name
    assert c0_summary["plies_played"] == c1_summary["plies_played"] == 100
    assert c0_summary["final_fen"] == c1_summary["final_fen"]
    assert c0_summary["protocol_revised"] is False
    assert c1_summary["protocol_revised"] is True
    assert c1_summary["team_recovery"]["white"]["rate"] == 1.0
    assert c1_summary["team_recovery"]["black"]["rate"] == 1.0
    public_messages = [json.loads(line) for line in (c1 / "public.jsonl").read_text().splitlines()]
    assert all("recommended_uci" not in item for item in public_messages)
    assert all("[MOVE:" not in item["message"] for item in public_messages)
