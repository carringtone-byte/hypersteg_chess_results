---
paper: "Tomašev et al. (2020)"
title: "Assessing Game Balance with AlphaZero: Exploring Alternative Rule Sets in Chess"
doi: "arXiv:2009.04374"
pmcid: "<PMC ID, if any>"
url: "arXiv:2009.04374v2 [cs.AI], 15 Sep 2020 (arXiv HTML rendering)"
source_version: "preprint"
file: "literature/tomasev_2020.html"
retrieved: "20261105"
verified_by: "Claude (Opus 5.5) subagent, quotes checked with verify_quotes.py (read-only run)"
# The six below are written by `verify_quotes.py --stamp` — do not hand-edit.
# They bind the ledger to the exact source/extract bytes AND its own quoted text
# (body_sha256) it was verified against, so a later quote edit is caught in CI.
source_sha256: "028840fc4cd78ad1995487eb433416248750c487e0bdad58b64d4a93d59c9159"
extract_sha256: "144f3084eafa10a845a7e07f3a7cc9e7f2d70e76241a524770fb2a8c1b51b91f"
body_sha256: "97fda87cc1be12cd215d8ede584039c49be1c84d3f993be392e7ea1112cf0f18"
verifier_version: "2"
verified_verdict: "pass"
verified_date: "20261106"
extract_source_sha256: "028840fc4cd78ad1995487eb433416248750c487e0bdad58b64d4a93d59c9159"
---

# Verified Claims — Tomašev et al. (2020)

Each claim below was extracted by reading the downloaded paper file with the Read
tool, grepping for the specific content, and reading the surrounding context to
confirm the attribution is faithful.

Source: arXiv:2009.04374v2 [cs.AI], dated 15 Sep 2020, as printed in the extract after the arXiv
site boilerplate and a long table of contents; the title and byline begin near line 330 of the
extract. Authors: Nenad Tomašev, Ulrich Paquet and Demis Hassabis (DeepMind) with Vladimir
Kramnik. `literature/REGISTER.tsv` gives this key the title "1Introduction", a mis-parse; the
extract is the paper named above. The arXiv HTML has no page numbers, so locations are section
and table numbers. This is a carrier paper, not a steganography paper. Its value to the map is a
measured answer to how much choice a strong player actually has in the opening: the entropy of
AlphaZero's move prior over the first 20 plies, set against uniform choice among legal moves.

## Claim 1: Setting — AlphaZero trained from scratch on classical chess and nine rule variants, with the same hyperparameters

> "We trained AlphaZero from scratch for each of the rule alterations in Table 1 , with the same set of model hyperparameters. The models were trained for 1 million training steps, with a batch size of 4096"

> "Training self-play games were generated using 800 MCTS simulations per move."

**ID:** alphazero-variant-training
**Location:** Section 2.3 "Training and evaluation"
**Grep command used:** `Grep pattern="We trained AlphaZero from scratch|800 MCTS simulations per move" path="literature/extracted/tomasev_2020.txt"`

---

## Claim 2: AlphaZero's network gives a prior over moves; MCTS refines it and plays the most-visited move

> "The network outputs a vector of move probabilities"

> "The prior network 𝐩 \mathbf{p} assigns weights to candidate moves at a “first glance” of the board, yielding an order in which moves are searched with MCTS."

> "After a number of such MCTS simulations, the root move that was visited (or expanded) most is played."

**ID:** prior-and-mcts
**Location:** Section 2.2 "Key components of AlphaZero"
**Grep command used:** `Grep pattern="network outputs a vector of move probabilities|first glance|visited \(or expanded\) most is played" path="literature/extracted/tomasev_2020.txt"`

---

## Claim 3: AlphaZero is nearly deterministic; variety is injected only by sampling the first 20 plies from MCTS visit counts

> "As AlphaZero is approximately deterministic given the same MCTS depth and number of rollouts, we promote diversity in games by sampling the first 20 plies in each game proportional to the softmax of the MCTS visit counts, followed by playing the top moves for the rest of the game."

**ID:** near-deterministic-play
**Location:** Section 3.1 "Self-play games"
**Grep command used:** `Grep pattern="approximately deterministic given the same MCTS" path="literature/extracted/tomasev_2020.txt"`

---

## Claim 4: Measure of choice — entropy of the move prior, in nats (or bits with log base 2), and candidate moves as its exponential

> "represents the number of nats (or bits, if log 2 \log_{2} is used) that are needed to encode the weighted moves in position"

> "the number of uniformly weighted moves that could be encoded in the same number of nats"

> "number of candidate moves m ⁡ ( s t ) m(s_{t}) – the number that a top player would realistically consider – is much smaller than"

**ID:** prior-entropy-candidate-moves
**Location:** Section 3.5.1 "Average information content", equations (6)–(7)
**Grep command used:** `Grep pattern="needed to encode the weighted moves|uniformly weighted|top player would realistically consider" path="literature/extracted/tomasev_2020.txt"`

---

## Claim 5: Capacity figure — classical chess: 28.58 nats over the first 20 plies of the prior, against 64.96 nats for uniform legal-move choice

> "Classical 28.58 2.58 × 10 12 2.58\times 10^{12}"

> "Uniform random 64.96 1.63 × 10 28 1.63\times 10^{28}"

> "The average information content in nats in the first 20 plies of the AlphaZero prior for each chess variant. The uniform random baseline assumes an equal probability for each move in Classical chess"

Ledger arithmetic, not the authors': 28.58 nats over 20 plies is about 1.43 nats, or about 2.1
bits, per ply under the prior of a strong player; 64.96 nats is about 3.25 nats, or about 4.7
bits, per ply if every legal move were equally likely. The second figure is close to the 4.3
bits per ply that `literature/verified_claims/barai_2026.md` claims for uniform legal-move
encoding.

**ID:** opening-entropy-classical
**Location:** Section 3.5.1; Table 3
**Grep command used:** `Grep pattern="Classical 28.58|Uniform random|average information content in nats in the first 20" path="literature/extracted/tomasev_2020.txt"`

---

## Claim 6: Playable lines are about the square root of legal lines (Iida et al.'s objective freedom of choice)

> "The estimates in Table 3 for Classical chess and \"Uniform random Classical chess” corroborate the claim that the number of playable opening lines – a player’s objective freedom of choice – is roughly the square root of the number of legal opening lines"

> "It affords us a crude estimate of the number of possible classical openings, as opposed to the number of plausibly playable or candidate openings."

**ID:** square-root-playable-lines
**Location:** Section 3.5.1 "Average information content"
**Grep command used:** `Grep pattern="roughly the square root of the number of legal|crude estimate of the number of possible" path="literature/extracted/tomasev_2020.txt"`

---

## Claim 7: Choice depends on the line — 1. e4 is far more forcing than 1. Nf3 (23.72 against 29.54 nats over the next 20 plies)

> "Classical (e4) 23.72 2.00 × 10 10 2.00\times 10^{10}"

> "Classical (Nf3) 29.54 6.75 × 10 12 6.75\times 10^{12}"

> "Statistically, the AlphaZero prior after 1. e4 is much more forcing than after 1. Nf3 in Classical chess."

**ID:** e4-versus-nf3-entropy
**Location:** Section 3.5.2 "Classical vs. No-castling chess"; Table 4
**Grep command used:** `Grep pattern="Classical \(e4\)|Classical \(Nf3\)|much more forcing" path="literature/extracted/tomasev_2020.txt"`

---

## Claim 8: A single equalising line concentrates the prior — AlphaZero strongly prefers the Berlin Defence against 1. e4

> "In Classical chess AlphaZero has a strong preference for playing the Berlin Defence 1… e5 2. Nf3 Nc6 3. Bb5 Nf6 in response to 1. e4"

> "a known equalising line in the Berlin Defence, leading to drawish positions."

**ID:** berlin-defence-spike
**Location:** Section 3.5.2; Figure 6 caption
**Grep command used:** `Grep pattern="strong preference for playing the Berlin|known equalising line in the Berlin" path="literature/extracted/tomasev_2020.txt"`

---

## Claim 9: White usually has more candidate moves than Black, the gap narrowing as the first-move advantage fades

> "In Classical chess, White has more options than Black in both lines, the difference slowly diminishing over time as the first-move advantage decreases."

**ID:** candidate-moves-by-side
**Location:** Section 3.5.2; Figure 6(c)–(d)
**Grep command used:** `Grep pattern="White has more options than Black" path="literature/extracted/tomasev_2020.txt"`

---

## Claim 10: Wider opening trees go with more draws; the most decisive variants have the narrowest trees

> "The two variants that have the largest entropy and hence largest opening tree in Table 3 , Pawn-sideways and Pawn one square, also happen to be among the most drawish"

> "The two variants that have the smallest opening trees under our analysis, No-castling and Torpedo, are also the most decisive and give White some of the largest advantages"

**ID:** entropy-decisiveness-tradeoff
**Location:** Section 3.5.1
**Grep command used:** `Grep pattern="largest entropy and hence largest opening tree|smallest opening trees under our analysis" path="literature/extracted/tomasev_2020.txt"`

---

## Claim 11: Longer thinking means more draws; White's expected score in classical chess falls from 54.1% (training) to 50.8% at 1 minute per move

> "Across all variations the percentage of drawn games increases with longer thinking times."

> "Classical 54.1 % 54.1\% 51.8 % 51.8\% 50.8 % 50.8\%"

**ID:** draw-rate-with-thinking-time
**Location:** Section 3.1, Figure 2 caption; Section 3.2, Table 2
**Grep command used:** `Grep pattern="drawn games increases with longer thinking|Classical 54.1" path="literature/extracted/tomasev_2020.txt"`

---

## Claim 12: Limits of the evidence — no baselines for model strength, so the quantitative results are paired with Kramnik's qualitative assessment

> "The absence of baselines makes it hard to formally assess the strength of each model, which is why it was important to couple the quantitative analysis and metrics observed at training and test time with a qualitative assessment in collaboration with Vladimir Kramnik"

> "We hypothesise that the relative differences in AlphaZero’s win rates might translate to differences in human play, although this hypothesis would need to be practically validated in the future."

**ID:** evidence-limits-kramnik
**Location:** Section 2.3 "Training and evaluation"; Section 3.2 "Expected scores and draw rates"
**Grep command used:** `Grep pattern="absence of baselines makes it hard|might translate to differences in human play" path="literature/extracted/tomasev_2020.txt"`

---

## Claim 13: Approach — in-silico assessment of chess variants, by training AlphaZero to near-optimal play under each rule set

> "AlphaZero provides an alternative  in silico  means of game balance assessment."

> "In this study we use AlphaZero to creatively explore and design new chess variants."

> "By learning near-optimal strategies for each variant with AlphaZero, we determine what games between strong human players might look like if these variants were adopted."

**ID:** approach-insilico-variant-assessment
**Location:** Abstract (as printed after the byline in the extract)
**Grep command used:** `Grep pattern="in silico|creatively explore and design|learning near-optimal strategies for each variant" path="literature/extracted/tomasev_2020.txt"`

---

## Claim 14: Approach — opening diversity measured as the entropy of the first 20 plies of the AlphaZero prior

> "We use the average information content (entropy) of the first  T = 20 T=20  plies of play from each variant’s prior as a surrogate diversity measure."

> "An entropy of  zero  corresponds to there being one and only one forcing sequence of moves to be playable for White and Black, all other moves leading to substantially worse positions for each side. A higher entropy implies a wider and more balanced opening tree of variations, leading to a more diverse set of middlegame positions."

**ID:** approach-prior-entropy-diversity
**Location:** Section 3.5 "Diversity"
**Grep command used:** `Grep pattern="surrogate diversity measure|one and only one forcing sequence" path="literature/extracted/tomasev_2020.txt"`
