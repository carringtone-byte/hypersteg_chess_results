---
paper: "McIlroy-Young et al. (2020)"
title: "Aligning Superhuman AI with Human Behavior: Chess as a Model System"
doi: "10.1145/3394486.3403219"
pmcid: "<PMC ID, if any>"
url: "https://arxiv.org/abs/2006.01855v3"
source_version: "preprint"
file: "literature/mcilroyyoung_2020.html"
retrieved: "20261105"
verified_by: "Claude (Opus 5.5) subagent, quotes checked with verify_quotes.py (read-only run)"
# The six below are written by `verify_quotes.py --stamp` — do not hand-edit.
# They bind the ledger to the exact source/extract bytes AND its own quoted text
# (body_sha256) it was verified against, so a later quote edit is caught in CI.
source_sha256: "43258196a6d4f3222511e9b29c8905c9e017145a158e9c7e579b8d005a8a7495"
extract_sha256: "4f04f25dc7864812bb99b8e6fea16a656d2d99b0a30d87184aeab97812b8e654"
body_sha256: "33233b4599caaa84addbd334469a185e581292e4e2fa780ee951c8495a5dfe71"
verifier_version: "2"
verified_verdict: "pass"
verified_date: "20261106"
extract_source_sha256: "43258196a6d4f3222511e9b29c8905c9e017145a158e9c7e579b8d005a8a7495"
---

# Verified Claims — McIlroy-Young et al. (2020)

Each claim below was extracted by reading the downloaded paper file with the Read
tool, grepping for the specific content, and reading the surrounding context to
confirm the attribution is faithful.

Source note: the file is the arXiv HTML rendering of arXiv:2006.01855v3 (14 July 2020),
the KDD '20 paper. Not a steganography method: Maia is a model of human move choice by
rating band, usable either as a warden's model of clean play or as the cover
distribution a move-selection encoder samples from.

**Rules:**
- Every entry must contain a DIRECT QUOTE from the paper (in blockquote).
- The quote must be locatable by grepping the downloaded file.
- "Location" = the heading/section (HTML) or page number (PDF) where the quote appears.
- Never paraphrase from memory — if you cannot find the quote, do not write the entry.
- Primary sources only — the source that made the claim, not a secondary write-up of it. What
  counts as primary depends on the project's declared `source_types` (papers, official reports, a
  recorded debate, …; see `spec/EXTRACTION.md`); for a paper project that is peer-reviewed
  literature, not a news article about it.

## Claim 1: Maia — AlphaZero-style network trained on human games, predicting human moves at a target skill level

> "We develop and introduce Maia, a customized version of AlphaZero trained on human chess games, that predicts human moves at a much higher accuracy than existing engines, and can achieve maximum accuracy when predicting decisions made by players at a specific skill level in a tuneable way."

**ID:** maia-human-move-model
**Location:** Abstract
**Grep command used:** `Grep pattern="We develop and introduce Maia" path="literature/extracted/mcilroyyoung_2020.txt"`

---

## Claim 2: Depth-limited Stockfish does not target lower-skill human play

> "We find that each version of Stockfish has a prediction accuracy that rises monotonically with the skill level of the players it is predicting, implying that it is not specifically targeting and matching moves made by players of lower skill levels."

**ID:** stockfish-depth-not-human
**Location:** Section 1 "Introduction"
**Grep command used:** `Grep pattern="rises monotonically" path="literature/extracted/mcilroyyoung_2020.txt"`

---

## Claim 3: Leela's move-matching is flat across skill levels

> "Leela ordinal rating 2700 matches human moves 40% of the time, no matter whether they are played by humans rated 1100, 1500, or 1900, and therefore it doesn't characterize human play at any particular level."

**ID:** leela-flat-accuracy
**Location:** Section 4.2 "Evaluating chess engines"
**Grep command used:** `Grep pattern="Leela ordinal rating 2700" path="literature/extracted/mcilroyyoung_2020.txt"`

---

## Claim 4: Maia predicts without tree search, because search degrades human-move prediction

> "while tree search is clearly important to strong chess-playing performance, we found that it degrades our performance at predicting human moves. As a result, we do not conduct any tree search to make a move prediction."

**ID:** no-tree-search
**Location:** Section 4.3 "Maia"
**Grep command used:** `Grep pattern="degrades our performance" path="literature/extracted/mcilroyyoung_2020.txt"`

---

## Claim 5: Move-matching accuracy — 46% at worst, over 52% at best

> "The lowest accuracy, when Maia trained on 1900-rated players predicts moves made by 1100-rated players, is 46%"

> "Maia's highest accuracy is over 52%."

**ID:** maia-accuracy
**Location:** Section 4.3 "Maia"
**Grep command used:** `Grep pattern="The lowest accuracy|highest accuracy is over" path="literature/extracted/mcilroyyoung_2020.txt"`

---

## Claim 6: Training data — nine rating bins of 12 million Lichess games each

> "This resulted in 9 training sets and 9 validation sets, one for each rating range between 1100 and 1900, with 12 million games and 120,000 games each, respectively"

**ID:** training-data
**Location:** Section 4.3 "Maia", Training
**Grep command used:** `Grep pattern="9 training sets" path="literature/extracted/mcilroyyoung_2020.txt"`

---

## Claim 7: Maia models agree with each other far more than with other engines

> "The highest inter-Maia agreement is 79%, far higher than the agreement of any Leela or Stockfish model with any other model."

**ID:** inter-maia-agreement
**Location:** Section 4.4 "Model comparisons"
**Grep command used:** `Grep pattern="inter-Maia agreement" path="literature/extracted/mcilroyyoung_2020.txt"`

---

## Claim 8: Blunder prediction — a network predicting whether a human will make a large mistake

> "For a dual task of predicting whether a human will make a large mistake on the next move, we develop a deep neural network that significantly outperforms competitive baselines."

**ID:** blunder-prediction
**Location:** Abstract
**Grep command used:** `Grep pattern="large mistake on the next move" path="literature/extracted/mcilroyyoung_2020.txt"`

---

## Claim 9: Supersedes — depth limiting as the standard attenuation method that the paper tests

> "The most natural method, which continues to be the main technique today, is limiting the depth of the game tree that engines are allowed to search, effectively imposing \"bounded rationality\" constraints on chess engines."

**ID:** depth-attenuation-prior
**Location:** Section 1 "Introduction"
**Grep command used:** `Grep pattern="The most natural method" path="literature/extracted/mcilroyyoung_2020.txt"`

---

## Claim 10: Approach — Maia, AlphaZero's architecture retrained on human games to predict the next human move, with no tree search

> "To accurately model granular human behavior in a tuneable way, we created a new deep neural network chess engine based on AlphaZero."

> "Since we are trying to explicitly model human behavior, our most fundamental change is to replace training on self-play games with training on human games."

> "Whereas the policy head in AlphaZero’s architecture tries to predict the best move, we tasked our neural network to predict the next move a human made."

> "We then trained separate models, one for each rating bin, to predict the next move a human would make (policy) and the probability that the active player will win the game (value)."

**ID:** approach-maia
**Location:** Section 4.3 "Maia"
**Grep command used:** `Grep pattern="we created a new deep neural network chess engine|most fundamental change|policy head in AlphaZero|separate models, one for each rating bin" path="literature/extracted/mcilroyyoung_2020.txt"`

---

## Claim 11: Approach — blunder prediction, a residual CNN that labels a move a blunder when it costs 10 points of win probability

> "We then label a move as a blunder if it worsens a player’s win probability by 10 percentage points or more."

> "Finally, we trained a residual CNN that we designed based on AlphaZero (full details are in the Supplement)."

> "This network’s performance demonstrates a significant improvement over the fully connected network, achieving up to 71.7% accuracy"

**ID:** approach-blunder-predictor
**Location:** Section 5.1 "Blunder Prediction"
**Grep command used:** `Grep pattern="label a move as a blunder|trained a residual CNN|up to 71.7% accuracy" path="literature/extracted/mcilroyyoung_2020.txt"`
