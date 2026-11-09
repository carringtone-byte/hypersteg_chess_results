---
paper: "Kolasani et al. (2025)"
title: "LLM Chess: Benchmarking Reasoning and Instruction-Following in LLMs through Chess"
doi: "arXiv:2512.01992"
pmcid: "<PMC ID, if any>"
url: "arXiv:2512.01992v1 [cs.AI], 01 Dec 2025 (arXiv HTML rendering)"
source_version: "preprint"
file: "literature/kolasani_2025.html"
retrieved: "20261105"
verified_by: "Claude (Opus 5.5) subagent, quotes checked with verify_quotes.py (read-only run)"
# The six below are written by `verify_quotes.py --stamp` — do not hand-edit.
# They bind the ledger to the exact source/extract bytes AND its own quoted text
# (body_sha256) it was verified against, so a later quote edit is caught in CI.
source_sha256: "a92649978999e7e8feb2de21718e91238e64b582757db93f2dd20e2d5eefb9b1"
extract_sha256: "8bc30e25fc85227a51ef0e27d2b18f598b926b8b4bd9fa757e93ebb225c3ebb6"
body_sha256: "f102c539b0b33b336dfe1264a847ec85389cb39b453626d464321245b27d4d24"
verifier_version: "2"
verified_verdict: "pass"
verified_date: "20261106"
extract_source_sha256: "a92649978999e7e8feb2de21718e91238e64b582757db93f2dd20e2d5eefb9b1"
---

# Verified Claims — Kolasani et al. (2025)

Each claim below was extracted by reading the downloaded paper file with the Read
tool, grepping for the specific content, and reading the surrounding context to
confirm the attribution is faithful.

Source: arXiv:2512.01992v1 [cs.AI], dated 01 Dec 2025, as printed in the extract after the arXiv
site boilerplate. Authors: Sai Kolasani, Maxim Saplin, Nicholas Crispino, Kyle Montgomery, Jared
Quincy Davis, Matei Zaharia, Chi Wang and Chenguang Wang (UC Berkeley, UC Santa Cruz, Stanford,
Google DeepMind, independent). The arXiv HTML has no page numbers, so locations are section and
table numbers. This is a carrier paper on how LLMs play chess, not a steganography paper. It
bears on the arena design (tool-based move submission, legality checks, no move history) and on
how much playing strength an LLM has to spare: a hidden-move scheme spends move quality, and
these models have little of it.

## Claim 1: Harness — one conversation per ply, three tools (get_current_board, get_legal_moves, make_move), moves in UCI

> "At each ply, we initiate a conversation with the end goal of outputting a valid chess move. We format all moves in Universal Chess Interface (UCI) format"

> "We offer three actions to the LLM: 1) get_current_board , which fetches and presents the state of the current board using a unicode board, 2) get_legal_moves , which fetches a list of legal moves in UCI format, and 3) make_move"

**ID:** per-ply-tool-harness
**Location:** Section 2.1 "Design"
**Grep command used:** `Grep pattern="At each ply, we initiate a conversation|We offer three actions to the LLM" path="literature/extracted/kolasani_2025.txt"`

---

## Claim 2: Limits and memory — 100 moves per game, 10 turns per ply, 3 attempts per turn; no game history, so each ply is independent

> "We cap each game at 100 moves (200 plys), have a max of 10 conversation turns per ply, and allow a max of 3 attempts per conversation turn for the LLM to provide a legal action or move."

> "The LLMs view each ply as independent of all others, as we do not provide any game history."

**ID:** game-caps-no-history
**Location:** Section 2.1 "Design"
**Grep command used:** `Grep pattern="We cap each game at 100 moves|view each ply as independent" path="literature/extracted/kolasani_2025.txt"`

---

## Claim 3: Opponents — a uniform random legal-move agent (30 games per model), then Komodo Dragon 1 at skill levels mapped to chess.com Elo

> "We benchmark over 50 models by playing 30 games as black against a random agent, defined as a player who always chooses a move at random from all legal moves."

> "As an estimate, skill 1 is around Elo 250, then each subsequent skill level is a 125 boost in Elo based on chess.com games"

**ID:** random-and-dragon-opponents
**Location:** Section 2.1 "Random Agent" and "Chess Engine"
**Grep command used:** `Grep pattern="playing 30 games as black against a random agent|skill 1 is around Elo 250" path="literature/extracted/kolasani_2025.txt"`

---

## Claim 4: Move-quality metric — Lichess Win% from Stockfish centipawns; blunder, mistake and inaccuracy at Win% drops of 30, 20 and 10

> "After the LLM calls make_move in each ply, we calculate the Win% (Equation ( 1 )), the chance of winning a game from the given position as defined by Lichess"

> "we can calculate Blunders, Mistakes, and Inaccuracies, common classifications of moves used by online chess platforms, following the Lichess cutoffs"

> "We note that since our Win% scores are based on centipawns, these metrics can depend on the hyperparameters of Stockfish."

**ID:** win-percent-move-quality
**Location:** Section 2.2 "Metrics", Per-ply, equations (1)–(2)
**Grep command used:** `Grep pattern="we calculate the Win%|following the Lichess cutoffs|depend on the hyperparameters of Stockfish" path="literature/extracted/kolasani_2025.txt"`

---

## Claim 5: Most models cannot reliably beat a random player; only reasoning models exceed 50% Win/Loss

> "Most notably, we find that most models are not able to consistently beat a random agent; in fact, only models with reasoning abilities are able to perform better than 50%."

**ID:** random-opponent-results
**Location:** Section 3.1 "LLMs vs. Random"; Figure 2
**Grep command used:** `Grep pattern="most models are not able to consistently beat a random agent" path="literature/extracted/kolasani_2025.txt"`

---

## Claim 6: Instruction-following is the main failure for non-reasoning models — 71.9% of games lost that way, against 24.4% for reasoning models

> "Reasoning models have an average win rate of 45.4% with the top performers achieving close to 100%, whereas non-reasoning models have an average win rate of 0.7% with one of the top performers achieving only 3.3%."

> "This performance gap is further supported by a three-fold reduction in instruction-following errors: 71.9% for non-reasoning models vs 24.4% for reasoning models."

**ID:** instruction-following-failures
**Location:** Section 3.1; Table 1
**Grep command used:** `Grep pattern="average win rate of 45.4%|three-fold reduction in instruction-following" path="literature/extracted/kolasani_2025.txt"`

---

## Claim 7: Per-ply quality — o4-mini (medium) blunders 4.2% of plies and finds the best move 19.5%; GPT-4.1-mini blunders 31.3% and finds it 4.1%

> "For example, o4-mini (medium) blunders only 4.2% and mistakes 1.1% of the time per ply, compared to 31.3% blunders and 8.7% mistakes for GPT-4.1-mini. Furthermore, o4-mini (medium) selects the \"Best\" move 19.5% of the time versus just 4.1% for GPT-4.1-mini."

**ID:** per-ply-blunder-best-rates
**Location:** Section 3.1; Table 2 "Per Ply Classification Rates"
**Grep command used:** `Grep pattern="o4-mini \(medium\) blunders only 4.2%" path="literature/extracted/kolasani_2025.txt"`

---

## Claim 8: Playing strength — the strongest model, o3 (low), peaks at an adjusted Elo of about 758 against Dragon 1

> "even the strongest LLM in our study, o3 (low), peaks at an adjusted Elo of about 758, which remains only slightly above the average and far below the human master level"

> "we find the maximum-likelihood Elo rating"

**ID:** top-llm-elo-758
**Location:** Section 3.2 "LLMs vs. Chess Engine"; Figure 3; Section 2.2 (Elo method)
**Grep command used:** `Grep pattern="peaks at an adjusted Elo of about 758|maximum-likelihood Elo rating" path="literature/extracted/kolasani_2025.txt"`

---

## Claim 9: Test-time scaling — more reasoning effort helps (up to 20% Win/Loss from low to high); more proposers (mixture of agents) does not

> "we find scaling with more tokens improves performance on LLM Chess , with increases of up to 15% from low to medium, and 20% from low to high."

> "This suggests that scaling the number of proposed moves doesn’t yield significant improvements, unlike the benefits we see from scaling reasoning effort."

**ID:** reasoning-effort-scaling
**Location:** Section 3.3 "Exploring Test-time Scaling"; Figure 4
**Grep command used:** `Grep pattern="scaling with more tokens improves|scaling the number of proposed moves" path="literature/extracted/kolasani_2025.txt"`

---

## Claim 10: Fragility — results swing with harness format: offering only make_move or a FEN board lifts o4-mini (low) from 73.3 to 95–97

> "LLM Chess 61.7 73.3 Actions Always Board State 66.7 83.3 Always Legal Moves 68.3 93.3 Only make_move 71.7 96.7"

> "Performance with both an ASCII board and FEN is similar to our default setting for Grok 3 Mini (low), while for o4-mini (low) we see performance improve by over 15% in both cases, reaching 95% for FEN."

> "With these results, we see performance varies widely, showing the lack of robustness in reasoning in the chess setting."

Columns in Table 3 are Grok 3 Mini (low) and o4-mini (low), Win/Loss over 30 games against the
random agent; the first row is the default harness and the others change which tools the model
is offered.

**ID:** harness-format-sensitivity
**Location:** Section 3.4 "Ablations"; Table 3
**Grep command used:** `Grep pattern="LLM Chess 61.7|Only  make_move|performance varies widely|reaching 95% for FEN" path="literature/extracted/kolasani_2025.txt"`

---

## Claim 11: Move history — adding previous moves helps somewhat but not much; it was left out partly because it bloated the prompt

> "We also experiment with including the previous moves, finding that performance can increase but most often does not result in a substantial benefit."

> "During these experiments, including the history bloated the prompt and made some of the models struggle more with instruction-following, so we also chose this setting as a practical concern."

**ID:** move-history-ablation
**Location:** Section 3.4 "Ablations"; Appendix A (design justifications)
**Grep command used:** `Grep pattern="experiment with including the previous moves|including the history bloated the prompt" path="literature/extracted/kolasani_2025.txt"`

---

## Claim 12: Approach (evaluation, not a steganographic method) — LLM Chess: an agentic benchmark in which models play whole games through tool calls, ranked against a random opponent and, for the strongest, given an Elo against a configurable engine

> "We introduce  LLM Chess , an evaluation framework designed to probe the generalization of reasoning and instruction-following abilities in large language models (LLMs) through extended agentic interaction in the domain of chess."

> "We rank over 50 open and closed source models by playing against a random opponent using a range of behavioral metrics, including win and loss rates, move quality, move legality, hallucinated actions, and game duration."

> "Central to our benchmark is agentic interaction: by having LLMs play chess through autonomously selecting actions within a conversation, the difficulty comes not only in reasoning about the board and choosing the best move, but also how to formulate these choices."

**ID:** approach-llm-chess-benchmark
**Location:** Abstract; Section 1 "Introduction"
**Grep command used:** `Grep pattern="an evaluation framework designed to probe the generalization|We rank over 50 open and closed source|Central to our benchmark is agentic interaction" path="literature/extracted/kolasani_2025.txt"`
