---
paper: "Blasius and Tönjes (2009)"
title: "Zipf law in the popularity distribution of chess openings"
doi: "arXiv:0704.2711"
pmcid: "<PMC ID, if any>"
url: "arXiv:0704.2711v2 [physics.soc-ph], 18 Nov 2009 (arXiv HTML rendering)"
source_version: "preprint"
file: "literature/blasius_2009.html"
retrieved: "20261105"
verified_by: "Claude (Opus 5.5) subagent, quotes checked with verify_quotes.py (read-only run)"
# The six below are written by `verify_quotes.py --stamp` — do not hand-edit.
# They bind the ledger to the exact source/extract bytes AND its own quoted text
# (body_sha256) it was verified against, so a later quote edit is caught in CI.
source_sha256: "94f8a19c911c635f505d870849bb14aaa9e2c5658ec29c7f13edb9dafe3f8626"
extract_sha256: "ceea08cbe0719f7e93dce328c406f74261787c425af26c7f20a2df23aa9afe5e"
body_sha256: "82f46cb5401b926dd5263dd9d7fc30e9bdb4fe6f77a734490b76aa819cde11a6"
verifier_version: "2"
verified_verdict: "pass"
verified_date: "20261106"
extract_source_sha256: "94f8a19c911c635f505d870849bb14aaa9e2c5658ec29c7f13edb9dafe3f8626"
---

# Verified Claims — Blasius and Tönjes (2009)

Each claim below was extracted by reading the downloaded paper file with the Read
tool, grepping for the specific content, and reading the surrounding context to
confirm the attribution is faithful.

Source: arXiv:0704.2711v2 [physics.soc-ph], dated 18 Nov 2009, as printed in the extract after
the arXiv site boilerplate. Authors: Bernd Blasius (ICBM, University of Oldenburg) and Ralf
Tönjes (Universität Potsdam; Ochanomizu University). A short letter with no section headings, so
locations are by figure, equation and footnote. This is a carrier paper, not a steganography
paper. It bears on how much freedom an opening move carries: in the opening, play concentrates
on a few popular lines, so a move off them is rare and may stand out. The paper itself says
nothing about steganography or bits.

## Claim 1: Data — ScidBase, 1.4 million games, each coded to 40 half-moves and grouped by shared move sequence

> "Here we present results based on ScidBase ( http://scid.sourceforge.net ) with N = 1.4 ⋅ 10 6 N=1.4\cdot 10^{6} recoreded games."

> "Each game was uniquely coded by a string (up to d = 40 d=40 half moves) and the game strings were sorted alphabetically"

**ID:** scidbase-opening-data
**Location:** Reference/footnote [6]
**Grep command used:** `Grep pattern="results based on ScidBase|uniquely coded by a string" path="literature/extracted/blasius_2009.txt"`

---

## Claim 2: Main result — opening popularities pooled over all depths follow Zipf's law with universal exponent 2

> "We find that the weighted game-tree of chess is self-similar and the frequencies S ⁡ ( n ) S(n) of weights follow a Zipf-Law"

> "A straight line fit (not shown) yields an exponent of α = 2.05 \alpha=2.05 with a goodness of fit"

**ID:** zipf-exponent-two
**Location:** Main text before equation (1); Figure 2A caption
**Grep command used:** `Grep pattern="weighted game-tree of chess is self-similar|yields an exponent of" path="literature/extracted/blasius_2009.txt"`

---

## Claim 3: At a fixed depth d the distribution is still power-law, but its exponent rises linearly with depth

> "The exponents α d \alpha_{d} are not universal, however, but increase linearly with d d (Fig. 2B, inset)."

> "The exponent α d \alpha_{d} is linearly increasing with the game depth d d and with a logarithmic finite size correction which is in excellent agreement with the chess database"

**ID:** depth-dependent-exponent
**Location:** Main text after equation (1); after equation (6)
**Grep command used:** `Grep pattern="are not universal, however|linearly increasing with the game depth" path="literature/extracted/blasius_2009.txt"`

---

## Claim 4: Branching ratios — the share of games taking each continuation follows the arcsine distribution, the same at every depth

> "is remarkably constant over most of the interval but diverges with exponent"

> "and is very well fitted by the parameterless arcsine-distribution"

> "We disregarded clusters with n d < 100 n_{d}<100 so that, in principle, a cluster could contribute to any of the bins. We found q ⁡ ( r ) q(r) to be depth-independent."

Read for the map: the branching ratio is the fraction of games at a node that take a given
continuation, so its distribution describes how unevenly popularity is split among the moves
actually played at each opening position.

**ID:** arcsine-branching-ratios
**Location:** Main text before equation (2); Figure 3A caption
**Grep command used:** `Grep pattern="remarkably constant over most|parameterless arcsine|to be depth-independent" path="literature/extracted/blasius_2009.txt"`

---

## Claim 5: Mechanism — Zipf's law follows from self-similar random fragmentation of the game tree, not from preferential attachment

> "the Zipf law arises from the self-similar nature of the game tree of chess."

> "The form of the branching ratio distribution suggests that in the case of chess there is no preferential growth process involved"

**ID:** fragmentation-mechanism
**Location:** Abstract; main text after equation (2)
**Grep command used:** `Grep pattern="arises from the self-similar nature|no preferential growth process involved" path="literature/extracted/blasius_2009.txt"`

---

## Claim 6: Concentration then dispersion — before a critical depth of about 15 half-moves most games sit in a few fashionable openings; after it rare lines dominate

> "in their initial phase ( d < d c ​ r ) (d<d_{cr}) the majority of chess games is distributed among a small number of fashionable openings"

> "80% of all games in the database are concentrated in about 23% of the most popular openings"

> "whereas beyond the critical game depth rarely used move sequences are dominating such that in aggregate they comprise the majority of all games"

**ID:** critical-depth-concentration
**Location:** Main text after equation (9); Figure 4
**Grep command used:** `Grep pattern="small number of fashionable openings|concentrated in about 23%|beyond the critical game depth" path="literature/extracted/blasius_2009.txt"`

---

## Claim 7: The critical depth depends on database size, and the crossover is statistical, not a change in how players play

> "the critical number d c ​ r d_{cr} of descisions at which this transition occurs depends logarithmically on the sample size"

> "Note, that this result arises from the statistics of iterated decisions and does not indicate a crossover of playing behavior with increasing game depth."

**ID:** critical-depth-is-statistical
**Location:** Main text before equation (9); after equation (9)
**Grep command used:** `Grep pattern="depends logarithmically on the sample size|does not indicate a crossover" path="literature/extracted/blasius_2009.txt"`

---

## Claim 8: Game-tree size — the average number of legal moves to the power of game length; actual play explores very little of it

> "the game tree complexity of chess, has roughly been estimated as the average number of legal moves in a chess position to the power of the length of a typical game"

> "But even during the first moves of a game, when the game complexity is still manageable, not all possibilities are explored equally often."

**ID:** game-tree-underexplored
**Location:** Introductory paragraphs (citing Shannon 1950)
**Grep command used:** `Grep pattern="average number of legal moves in a chess position|not all possibilities are explored equally" path="literature/extracted/blasius_2009.txt"`

---

## Claim 9: Robustness of the finding — across databases, other board games, depths, player levels and decades

> "similar power-laws could be observed in different databases and other board games, regardless of the considered game depth, constraints on player levels or the decade when the games were played."

> "Stretching over six orders of magnitude, the here reported distributions are one of the most precise examples for power-laws known today in social data sets."

**ID:** robust-across-databases
**Location:** Main text after equation (1)
**Grep command used:** `Grep pattern="similar power-laws could be observed|Stretching over six orders" path="literature/extracted/blasius_2009.txt"`

---

## Claim 10: Approach (contribution) — a measured opening-popularity law and its generating model: opening frequencies are power-law with depth-dependent exponent, pooled weights obey Zipf's law, and a random multiplicative fragmentation of the game tree with arcsine branching ratios reproduces both

> "We perform a quantitative analysis of extensive chess databases and show that the frequencies of opening moves are distributed according to a power-law with an exponent that increases linearly with the game depth, whereas the pooled distribution of all opening weights follows Zipf’s law with universal exponent."

> "We propose a simple stochastic process that is able to capture the observed playing statistics and show that the Zipf law arises from the self-similar nature of the game tree of chess."

> "we find excellent agreement between the weight frequencies"

> "in the chess database and direct simulations of the multiplicative process"

**ID:** approach-opening-fragmentation-model
**Location:** Abstract; main text after equation (5), the comparison with Fig. 3B
**Grep command used:** `Grep pattern="quantitative analysis of extensive chess|simple stochastic process that is able|excellent agreement between the weight|direct simulations of the multiplicative" path="literature/extracted/blasius_2009.txt"`
