---
paper: "Regan, Macieja and Haworth (2012)"
title: "Understanding Distributions of Chess Performances"
doi: "10.1007/978-3-642-31866-5_20"
pmcid: "<PMC ID, if any>"
url: "https://centaur.reading.ac.uk/23800/"
source_version: "preprint"
file: "literature/regan_2012.pdf"
retrieved: "20261105"
verified_by: "Claude (Opus 5.5) subagent, quotes checked with verify_quotes.py (read-only run)"
# The six below are written by `verify_quotes.py --stamp` — do not hand-edit.
# They bind the ledger to the exact source/extract bytes AND its own quoted text
# (body_sha256) it was verified against, so a later quote edit is caught in CI.
source_sha256: "d6d1c9c3160918c5c944f07491744a0c1d63c17b71f81dabae4d7f4c59e480f6"
extract_sha256: "e1b9325030ae77496df5e88856c75da43e2f53acad2c1a203708b918f2e3a589"
body_sha256: "2492e46f233fc5c5771bea3e7109811c7cc330a56182506bc885da2b45dc3c16"
verifier_version: "2"
verified_verdict: "pass"
verified_date: "20261106"
extract_source_sha256: "d6d1c9c3160918c5c944f07491744a0c1d63c17b71f81dabae4d7f4c59e480f6"
---

# Verified Claims — Regan, Macieja and Haworth (2012)

Each claim below was extracted by reading the downloaded paper file with the Read
tool, grepping for the specific content, and reading the surrounding context to
confirm the attribution is faithful.

Source note: the file is the CentAUR accepted version (post-conference postprint) of
the Advances in Computer Games chapter, LNCS 7168, pp. 230–243. Not a steganography
method: it extends the intrinsic-rating model that a warden could use to say what
move choice at a given strength should look like, with confidence intervals.

**Rules:**
- Every entry must contain a DIRECT QUOTE from the paper (in blockquote).
- The quote must be locatable by grepping the downloaded file.
- "Location" = the heading/section (HTML) or page number (PDF) where the quote appears.
- Never paraphrase from memory — if you cannot find the quote, do not write the entry.
- Primary sources only — the source that made the claim, not a secondary write-up of it. What
  counts as primary depends on the project's declared `source_types` (papers, official reports, a
  recorded debate, …; see `spec/EXTRACTION.md`); for a paper project that is peer-reviewed
  literature, not a news article about it.

## Claim 1: Multi-PV analysis evaluates every reasonable option, not just the top move and the move played

> "Their main difference from [5–7] is the use of Multi-PV analysis to obtain uthor-itative values for all reasonable options, not just the top move(s) and the move played."

**ID:** multipv-full-context
**Location:** Section 5 "Intrinsic Ratings Over Time"
**Grep command used:** `Grep pattern="Multi-PV analysis to obtain" path="literature/extracted/regan_2012.txt"`

---

## Claim 2: The model runs in both directions — fitting skill from games, and generating a move distribution for a given skill

> "Models of this kind function in one direction by taking in game analyses and using statistical fitting to generate values of the skill parameters to indicate the intrinsic level of the games. They function in the other direction by taking pre-set values of the skill parameters and generating a probability distribution of next moves by an agent of that skill profile."

**ID:** two-direction-model
**Location:** Section 5 "Intrinsic Ratings Over Time"
**Grep command used:** `Grep pattern="function in one direction" path="literature/extracted/regan_2012.txt"`

---

## Claim 3: Projected standard deviations give confidence intervals for engine-match (MM) and average error (AE)

> "We also generate projected standard deviations, and hence projected confidence intervals, for AEe (and also the first-move match statistic MMe) as shown below."

**ID:** projected-confidence-intervals
**Location:** Section 5 "Intrinsic Ratings Over Time"
**Grep command used:** `Grep pattern="projected standard deviations" path="literature/extracted/regan_2012.txt"`

---

## Claim 4: Empirical modelling error — real deviations exceed the projections by up to 1.15 (MM) and 1.4 (AE)

> "suggest that the actual deviations in real-world data are bounded by a factor of 1.15 for the MM statistic and 1.4 for AE"

**ID:** modelling-error-factor
**Location:** Section 5 "Intrinsic Ratings Over Time"
**Grep command used:** `Grep pattern="bounded by a factor of" path="literature/extracted/regan_2012.txt"`

---

## Claim 5: Human error scales with the size of the advantage, motivating Scaled Average Error

> "Rather this seems to be evidence that human players perceive differences in value in proportion to the overall advantage for one side."

**ID:** scaled-error
**Location:** Section 4 "Average Error and Results by Tournament Categories"
**Grep command used:** `Grep pattern="perceive differences in value" path="literature/extracted/regan_2012.txt"`

---

## Claim 6: Error rises sharply approaching the move-40 time control

> "When AE is plotted against the turn number, sharply greater error for turns approaching the standard Move 40 time control is evident"

**ID:** time-control-error
**Location:** Section 4 "Average Error and Results by Tournament Categories"
**Grep command used:** `Grep pattern="sharply greater error" path="literature/extracted/regan_2012.txt"`

---

## Claim 7: Per-player Intrinsic Performance Ratings have large deviation

> "The IPR's have large deviation, and yet several TPR's fall outside even the 2.8-sigma range. This may constrain the usefulness of the IPR as an estimator of the TPR."

**ID:** ipr-large-deviation
**Location:** Section 6 "Distributions of Performances"
**Grep command used:** `Grep pattern="have large deviation" path="literature/extracted/regan_2012.txt"`

---

## Claim 8: Builds on — continues Haworth, DiFatta and Regan's intrinsic measurement of move quality

> "We continue work by Haworth, DiFatta, and Regan [1–4] on measuring performance 'in-trinsically' by the quality of moves chosen rather than the results of games."

**ID:** builds-on-intrinsic
**Location:** Section 1 "Introduction"
**Grep command used:** `Grep pattern="continue work by Haworth" path="literature/extracted/regan_2012.txt"`

---

## Claim 9: Approach (contribution) — a refined Regan–Haworth model applied to whole populations: Intrinsic Performance Ratings from Multi-PV analysis, with their distribution used to test rating stability and drift between rating systems

> "The distribution of the model’s Intrinsic Performance Ratings can hence be used to compare populations that have limited interaction, such as between players in a national chess federation and FIDE, and ascertain relative drift in their respective rating systems."

> "“Intrinsic Ratings” as judged from computer analysis have likewise remained relatively constant as a function of Elo rating over time—for this we refine the method of Regan and Haworth [4]."

> "The last item bolsters the Regan-Haworth model [4] as a reliable indicator of performance"

> "The work reported in [4] and this paper uses a method patterned on multinomial Bernoulli trials, and obtains a corresponding spectrum."

**ID:** approach-intrinsic-performance-ratings
**Location:** Abstract; Section 1 "Introduction"; Section 5 "Intrinsic Ratings Over Time" (reference [4] is K. Regan and G. Haworth, "Intrinsic chess ratings", AAAI 2011, ledgered as `regan_2011`)
**Grep command used:** `Grep pattern="Intrinsic Performance Ratings can hence|we reﬁne the method|bolsters the Regan-Haworth model|patterned on multinomial Bernoulli" path="literature/extracted/regan_2012.txt"`

**Refines:** regan_2011:approach-intrinsic-rating-model (grounded by #approach-intrinsic-performance-ratings)
