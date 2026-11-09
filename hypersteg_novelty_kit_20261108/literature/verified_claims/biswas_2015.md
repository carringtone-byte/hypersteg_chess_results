---
paper: "Haworth, Biswas and Regan (2015)"
title: "A Comparative Review of Skill Assessment: Performance, Prediction and Profiling"
doi: "10.1007/978-3-319-27992-3_13"
pmcid: "<PMC ID, if any>"
url: "In A. Plaat, J. van den Herik and W. Kosters (Eds.), Advances in Computer Games (ACG 2015), LNCS 9525, Springer, pp. 135–146; chapter held in the whole-volume file literature/biswas_2015.pdf, PDF pages 155–166"
source_version: "published"
file: "literature/biswas_2015.pdf"
retrieved: "20261105"
verified_by: "Claude (Opus 5.5) subagent, quotes checked with verify_quotes.py (read-only run)"
# The six below are written by `verify_quotes.py --stamp` — do not hand-edit.
# They bind the ledger to the exact source/extract bytes AND its own quoted text
# (body_sha256) it was verified against, so a later quote edit is caught in CI.
source_sha256: "6b22d5e3025e1aa32637350a3531a15d32b9efbc3983517f01b77df0b03b82b2"
extract_sha256: "003e5dc16daa32da2500e302b779ab8d5cae8d5092438e92c52e46172aa089b4"
body_sha256: "e1a4875480208b62a4a7f15e6c870eb67bff83b15e9695799e7718577c307b9f"
verifier_version: "2"
verified_verdict: "pass"
verified_date: "20261106"
extract_source_sha256: "6b22d5e3025e1aa32637350a3531a15d32b9efbc3983517f01b77df0b03b82b2"
---

# Verified Claims — Haworth, Biswas and Regan (2015)

Each claim below was extracted by reading the downloaded paper file with the Read
tool, grepping for the specific content, and reading the surrounding context to
confirm the attribution is faithful.

Source: Advances in Computer Games, 14th International Conference (ACG 2015), LNCS 9525, Springer
2015, pp. 135–146, DOI 10.1007/978-3-319-27992-3_13 (printed on the chapter's first page).
`literature/biswas_2015.pdf` is the whole proceedings volume (280 PDF pages); this ledger covers
only the chapter "A Comparative Review of Skill Assessment: Performance, Prediction and Profiling",
PDF pages 155–166, by Guy Haworth (University of Reading), Tamal Biswas and Ken Regan (University at
Buffalo). The key `biswas_2015` names the second author; Haworth is first. The volume contains no
chapter on steganography: "steganograph", "covert" and "watermark" occur nowhere in its extract,
and this is the only chapter with Biswas as an author. The chapter matters to the project as a
review of the detectors that would see a chess carrier: methods that score a player's moves
against an engine and flag play that is too good or, by the same measures, anomalous. Page
numbers below are the proceedings page numbers printed in the extract; quotes that cross a line
end are joined, with the line-end hyphen removed.

## Claim 1: Approach — a framework that separates Performance from Prediction and quantifies Profiling, for methods that judge the intrinsic merit of moves

> "The aim here is to introduce a framework for the discussion and analysis of assessment methods that evaluate the ‘intrinsic me rit’ of the subject’s decisions. It clearly separates the goals of metrics for Performance and Prediction, and quantiﬁes the use of Proﬁling."

> "Performance refers to quantitative measures that can be correlated with ELO ratings. Prediction means anticipating the distribution of some 100–300 move choices that a player might make in a tournament."

**ID:** approach-3p-framework
**Location:** Section 1 "Introduction", p. 135
**Grep command used:** `Grep pattern="The aim here is to introduce a framework|Performance refers to quantitative measures" path="literature/extracted/biswas_2015.txt"`

---

## Claim 2: Motivation — cheating and false accusations are both rising; a test must do more than catch a player who plays too well

> "The chess community needs to limit potential reputational damage by inhibiting cheating and unjustiﬁed accusations of cheating: there has been a recent rise in both."

> "Both recognise that strong players will ﬁnd better moves but anti-cheating tests have to do better than merely identify someone who is ‘playing too well’."

**ID:** cheating-motivation
**Location:** Abstract and Section 1 "Introduction", p. 135
**Grep command used:** `Grep pattern="potential reputational damage|anti-cheating tests have to do better" path="literature/extracted/biswas_2015.txt"`

---

## Claim 3: What the methods need — engine analysis of the alternative moves is the only input, and the engine itself is a fallible benchmark

> "All assessment research approaches now use computer-generated move analysis as the benchmark."

> "engines are fallible agents, even if the best are less fallible than human players."

> "Alternative-move evaluations are the only input to the benchmarking processes below."

**ID:** engine-benchmark-input
**Location:** Section 1.1 "The Chess Engine as Benchmarking Player", p. 136
**Grep command used:** `Grep pattern="computer-generated move analysis as the|engines are fallible agents|Alternative-move evaluations are the only input" path="literature/extracted/biswas_2015.txt"`

---

## Claim 4: Stated limits common to all methods — moves modelled as independent, engines sharing mistakes, and non-zero rates of missed cheats and false accusations

> "– move-choices stem from a plan but are modelled as independent events,"

> "– chess engines are not fully independent, tending to make the same mistakes,"

> "– there is a probability pfp > 0 that honest player HP will be accused of cheating."

**ID:** shared-method-limits
**Location:** Section 3 "Survey of Assessment Methods", p. 138
**Grep command used:** `Grep pattern="modelled as independent events|tending to make the same mistakes|honest player HP will be accused" path="literature/extracted/biswas_2015.txt"`

---

## Claim 5: Surveyed — move matching (MM) and equal-value matching (EV): agreement with the engine's choice; a cheater can lower the match rate cheaply

> "Observers of games commonly note whether the human player’s choice move matches that of some ‘k ibitzer-engine’ and compute a %-match MM."

> "– cheater CH can easily lower their MM(CH) at minimal cost,"

> "Equi-optimal moves are regarded as ‘matches’, requiring the engines to identify them all:"

**ID:** surveyed-move-matching
**Location:** Section 3.1 "Agreement Between AP and BP", pp. 138–139
**Grep command used:** `Grep pattern="Observers of games commonly note|cheater CH can easily lower|optimal moves are regarded as" path="literature/extracted/biswas_2015.txt"`

---

## Claim 6: Surveyed — average difference (AD) and its scaled form (ASD): centipawns lost against the engine, scaled by the size of the advantage after Regan's finding

> "AD: Average Diﬀerence. Note that we chose AD not AE (Average Error) as the error may come from the benchmarking computer BP rather than from AP"

> "The last caveat on the AD method anticipates a key ﬁnding by Regan [21, 22] that average-diﬀerence correlates with the absolute value of the position, see Fig. 1."

> "If pv = |position value|, AP’s ‘diﬀerence ad relative to BP’s choice is scaled to be ad/ln(1 + pv)."

**ID:** surveyed-average-difference
**Location:** Section 3.2 "‘Average Difference’ Methods", pp. 139–140 (reference [21] is Regan, Macieja and Haworth, *Understanding distributions of chess performances*, ACG 2011; [22] is Regan and Haworth, *Intrinsic chess ratings*, AAAI 2011)
**Grep command used:** `Grep pattern="AD: Average|anticipates a key|is scaled to be" path="literature/extracted/biswas_2015.txt"`

**Restates:** regan_2012:scaled-error (grounded by #surveyed-average-difference)

---

## Claim 7: Surveyed — statistical regression (SR): fit the stochastic benchmark player whose competence best explains the moves; frequentist, with z-scores

> "SR: Statistical Regression. This method, deployed by Regan [20–22] identiﬁes the BPi which best ﬁts the observed play: it is essentially frequentist."

> "The model also generates variances and hence provides z-scores for statistical tests employing the MM, EV, and AD/ASD measures."

**ID:** surveyed-statistical-regression
**Location:** Section 3.3 "‘Whole Context’ Analysis: Deepest Evaluations Only", p. 141
**Grep command used:** `Grep pattern="SR: Statistical Regression|provides z-scores for statistical tests" path="literature/extracted/biswas_2015.txt"`

**Restates:** regan_2011:sensitivity-competence (grounded by #surveyed-statistical-regression)

---

## Claim 8: Detection result — SR clears every historic 'false positive' game in the review's table; a z-score of 2.75 is needed before cheating is supported

> "We report here that SR, carried out to FIDE/ACP guidelines, comes to a negative rather than a positive conclusion on all the games of Table 1, and on the aggregate of Morphy’s moves."

> "the MM/EV ﬁgures’ z-scores are less than the minimum mark of 2.75 stated [10] as needed to register statistical support for any ‘positive’ conclusion about cheating likelihood."

**ID:** sr-false-positive-result
**Location:** Section 3.3, p. 141
**Grep command used:** `Grep pattern="We report here that SR|minimum mark of 2.75" path="literature/extracted/biswas_2015.txt"`

---

## Claim 9: Surveyed — Skilloscopy (SK): Bayesian updating of belief over benchmark players of defined competence, move by move

> "Skilloscopy is the name given to the assessment of skill by Bayesian Inference [1, 3, 5, 6, 15–18]."

> "An important advantage is that his simple formula can be used iteratively as each new observation arrives."

> "+ SK can combine the results of two independent, compatible computations,"

**ID:** surveyed-skilloscopy
**Location:** Section 3.3, pp. 141–142
**Grep command used:** `Grep pattern="Skilloscopy is the name given|used iteratively as each new observation|SK can combine the results" path="literature/extracted/biswas_2015.txt"`

---

## Claim 10: Surveyed — SR over all search depths (SRA): a move that ranks top early in the search is likelier to be played

> "The most recent addition to the spectrum of assessment methods [4] is labelled ‘SRA’ here, being SR but taking move-valuations from all depths of BP’s search."

> "It is clear that if a move takes and retains top ranking early in the search, it is more likely to be selected by AP than a move that emerges in the last iteration of the search."

**ID:** surveyed-sr-all-depths
**Location:** Section 3.4 "‘Whole Context’ Analysis: Evaluations at All Depths", p. 142 (reference [4] is Biswas and Regan, ICAART 2015)
**Grep command used:** `Grep pattern="labelled ‘SRA’|retains top ranking early in the search" path="literature/extracted/biswas_2015.txt"`

---

## Claim 11: Ranking of the methods — more information, better method; FIDE/ACP treats MM, EV and AD as screening only

> "Speciﬁcally, here, it is believed that MM 〈 EV 〈〈 AD 〈〈 ASD 〈〈 SR/SK 〈 SRA."

> "FIDE/ACP committee certainly regards MM/EV/AD as ‘screening methods’ but looks to more informed methods for deﬁnitive assessments [10]."

**ID:** method-ranking
**Location:** Section 6 "Summary and View Forward", p. 144
**Grep command used:** `Grep pattern="it is believed that MM|screening methods" path="literature/extracted/biswas_2015.txt"`

---

## Claim 12: Reproducibility standard — single-thread, non-learning engines with every UCI parameter stated

> "The reproducibility of computational experiments certainly requires single-thread mode [2], non-learning mode, and the full speciﬁcation of UCI parameters."

**ID:** reproducibility-standard
**Location:** Section 5 "Standards for a Research Community", p. 144
**Grep command used:** `Grep pattern="reproducibility of computational experiments certainly requires" path="literature/extracted/biswas_2015.txt"`
