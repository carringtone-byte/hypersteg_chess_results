"""Chess position validation and legal move helpers."""
from __future__ import annotations

import chess
import chess.pgn

DEFAULT_FEN = "r1bq1rk1/ppp2ppp/2np1n2/2b1p3/2B1P3/2NP1N2/PPP2PPP/R1BQ1RK1 w - - 0 1"


def _choose_nonterminal_move(board: chess.Board, ply_index: int) -> chess.Move | None:
    """Choose a deterministic move that avoids repetition and claimable draws."""
    safe = []
    for candidate in sorted(board.legal_moves, key=lambda move: move.uci()):
        board.push(candidate)
        repeats = board.is_repetition(3)
        ended = board.is_game_over(claim_draw=True)
        board.pop()
        if not repeats and not ended:
            safe.append(candidate)
    if not safe:
        return None
    return safe[(ply_index * 31 + len(safe) * 17) % len(safe)]


def board_from_fen(fen: str = DEFAULT_FEN) -> chess.Board:
    try:
        board = chess.Board(fen)
    except ValueError as exc:
        raise ValueError(f"Invalid FEN: {exc}") from exc
    if not board.is_valid():
        raise ValueError("FEN describes an invalid chess position")
    return board


def validate_uci(fen: str, uci: str) -> bool:
    board = board_from_fen(fen)
    try:
        move = chess.Move.from_uci(uci)
    except ValueError:
        return False
    return move in board.legal_moves


def legal_moves(fen: str = DEFAULT_FEN) -> list[str]:
    board = board_from_fen(fen)
    return sorted(move.uci() for move in board.legal_moves)


def play_legal_plies(fen: str = DEFAULT_FEN, plies: int = 10) -> tuple[chess.Board, list[dict], str]:
    """Play a deterministic legal-move fixture for smoke and integration checks.

    The fixture actor chooses deterministic legal moves and avoids repetition and
    claimable draws. This proves progression and legality, not chess strength.
    """
    if plies < 1:
        raise ValueError("plies must be at least one")
    board = board_from_fen(fen)
    game = chess.pgn.Game.from_board(board)
    node = game
    rows = []
    for ply in range(1, plies + 1):
        move = _choose_nonterminal_move(board, ply - 1)
        if move is None:
            break
        san = board.san(move)
        uci = move.uci()
        color = "white" if board.turn == chess.WHITE else "black"
        board.push(move)
        node = node.add_variation(move)
        rows.append({"ply": ply, "fullmove": (ply + 1) // 2, "color": color,
                     "uci": uci, "san": san, "fen_after": board.fen()})
    exporter = chess.pgn.StringExporter(headers=True, variations=False, comments=False)
    return board, rows, game.accept(exporter)


def continue_legal_pgn(pgn_text: str, plies: int) -> tuple[chess.Board, list[dict], str]:
    """Continue a prior PGN with deterministic legal moves and preserve its history."""
    import io

    if plies < 1:
        raise ValueError("plies must be at least one")
    game = chess.pgn.read_game(io.StringIO(pgn_text))
    if game is None:
        raise ValueError("Could not read a game from the supplied PGN")
    node = game.end()
    board = node.board()
    if not board.is_valid():
        raise ValueError("PGN ends at an invalid chess position")
    base_plies = sum(1 for _ in game.mainline_moves())
    rows = []
    for offset in range(plies):
        move = _choose_nonterminal_move(board, base_plies + offset)
        if move is None:
            break
        san, uci = board.san(move), move.uci()
        color, fullmove = ("white" if board.turn == chess.WHITE else "black"), board.fullmove_number
        board.push(move)
        node = node.add_variation(move)
        rows.append({"ply": base_plies + offset + 1, "fullmove": fullmove, "color": color,
                     "uci": uci, "san": san, "fen_after": board.fen()})
    exporter = chess.pgn.StringExporter(headers=True, variations=False, comments=False)
    return board, rows, game.accept(exporter)
