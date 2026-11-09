---
paper: "Boonstra and Meester (2024)"
title: "A Bayesian framework for analyzing alleged cheating in sports through hidden codes, with applications to bridge and baseball"
doi: "arXiv:2409.08172"
pmcid: "<PMC ID, if any>"
url: "arXiv:2409.08172v4 [stat.AP], 03 Mar 2025 (arXiv HTML rendering)"
source_version: "preprint"
file: "literature/boonstra_2024.html"
retrieved: "20261105"
verified_by: "Claude (Opus 5.5) subagent, quotes checked with verify_quotes.py (read-only run)"
# The six below are written by `verify_quotes.py --stamp` — do not hand-edit.
# They bind the ledger to the exact source/extract bytes AND its own quoted text
# (body_sha256) it was verified against, so a later quote edit is caught in CI.
source_sha256: "cc5ea53adcbac4af3671de9009f07cd9a0c2d7c684770329decb1d782fddf972"
extract_sha256: "bb24c41eac26268e6022a0f94917ec84d7c8bcf0634c64f07569c09ae0e031ae"
body_sha256: "678bb914c80107d74e990ac49c1e393ae4ac08e6abab00ff60cc2fbcf19d5814"
verifier_version: "2"
verified_verdict: "pass"
verified_date: "20261106"
extract_source_sha256: "cc5ea53adcbac4af3671de9009f07cd9a0c2d7c684770329decb1d782fddf972"
---

# Verified Claims — Boonstra and Meester (2024)

Each claim below was extracted by reading the downloaded paper file with the Read
tool, grepping for the specific content, and reading the surrounding context to
confirm the attribution is faithful.

Source: arXiv:2409.08172v4 [stat.AP], dated 03 Mar 2025 (first posted September 2024, per the
arXiv identifier), as printed in the extract after the arXiv site boilerplate. Authors: Aafko
Boonstra and Ronald Meester, Department of Mathematics, Vrije Universiteit Amsterdam. The arXiv
HTML has no page numbers, so locations are section numbers. This is a detection (forensic
evidence) paper. The two channels it analyses are physical side channels outside the legal
game: card orientation in bridge and trash-can bangs in baseball. Both are one-bit-per-event
codes the alleged cheaters pre-agreed.

## Claim 1: Channel (bridge) — the orientation of the lead card, horizontal or vertical, outside the legal signalling channel of card spots

> "While signaling is permitted and plays a vital role in the game, it must be done through the spots on the played cards. Physical signaling, such as sounds, gestures, or card orientation, is strictly prohibited, whether disclosed or not."

> "the allegation was that the physical orientation of certain cards revealed information about the hand."

**ID:** card-orientation-channel
**Location:** Section 3.1 "The basics of contract bridge"; Section 1 "Introduction"
**Grep command used:** `Grep pattern="Physical signaling, such as sounds|physical orientation of certain cards" path="literature/extracted/boonstra_2024.txt"`

---

## Claim 2: Encoding (bridge) — code C: one bit per lead, horizontal denies a top honour in the suit, vertical promises one

> "If a card is led horizontally, this denies a top honor (ace, king or queen) in the lead suit. Conversely, if the card is lead vertically, this implies holding a top honor in that suit."

**ID:** code-c-top-honour-bit
**Location:** Section 3.2 "A Bayesian analysis"
**Grep command used:** `Grep pattern="denies a top honor" path="literature/extracted/boonstra_2024.txt"`

---

## Claim 3: Channel and encoding (baseball) — trash-can bangs relay the stolen catcher's sign; code B: bang for a non-fastball, none for a fastball

> "a player would bang a nearby trash can with a bat to communicate the upcoming pitch type to the batter."

> "If the catcher gives a sign for a fastball, that is, a four-seam fastball, a two-seam fastball, a cutter, a sinker or a split-finger fastball, no trash can is banged."

**ID:** trash-can-code-b
**Location:** Section 4.1 "The case" (quoting the MLB investigative report); code B as stated by the authors
**Grep command used:** `Grep pattern="bang a nearby trash can|If the catcher gives a sign for a fastball" path="literature/extracted/boonstra_2024.txt"`

---

## Claim 4: Detection method — a likelihood ratio between a named code hypothesis and a random-orientation hypothesis, not a p-value

> "In our context, the two hypotheses of interest are, firstly, the hypothesis that the defendants used a specified (illegal) method to transmit information, and secondly, the hypothesis that they did not."

> "The key issue is that a frequentist method yields answers that predict how (un)likely the data are under the assumption of innocence. This, however, is an answer to the wrong question."

**ID:** likelihood-ratio-detector
**Location:** Section 1 "Introduction"
**Grep command used:** `Grep pattern="used a specified \(illegal\) method|answer to the wrong question" path="literature/extracted/boonstra_2024.txt"`

---

## Claim 5: Model — under the code, each event matches with probability p (allowing mistakes); under randomness, a uniform-prior orientation rate q

> "we will allow for the possibility of making mistakes, and suggest a model in which every lead corresponds to the code with some (high) probability"

> "we think that it is reasonable to assume that both players have the same, fixed time-homogeneous probability"

**ID:** match-probability-model
**Location:** Section 3.2.2 "The models"
**Grep command used:** `Grep pattern="allow for the possibility of making mistakes|fixed time-homogeneous probability" path="literature/extracted/boonstra_2024.txt"`

---

## Claim 6: Detection result (bridge) — 83 of 85 leads match code C; likelihood ratio about 4 × 10^19 at p = 0.9

> "In the FN-case under consideration, we have n = 85 n=85 , m = 83 m=83 and h = 45 h=45"

> "This likelihood ratio is, therefore, extremely high, providing extremely strong support for"

**ID:** fantoni-nunes-likelihood-ratio
**Location:** Section 3.2.3 "The likelihood ratio", equation (3.1)
**Grep command used:** `Grep pattern="FN-case under consideration|extremely strong support for" path="literature/extracted/boonstra_2024.txt"`

---

## Claim 7: Detection result (baseball) — two Yankees games, 201 of 267 pitches match; likelihood ratio about 3.4 × 10^30 at p = 0.8

> "in the matches of June 31 and July 1 against the New York Yankees, we have n = 267 n=267 , m = 201 m=201 and b = 85 b=85"

> "is 3.4 nonillion times more likely under"

**ID:** astros-likelihood-ratio
**Location:** Section 4.2 "A Bayesian analysis", equation (4.1)
**Grep command used:** `Grep pattern="against the New York Yankees|nonillion times more likely" path="literature/extracted/boonstra_2024.txt"`

---

## Claim 8: Why a simple code is detectable — few codes are meaningful, so the prior on the alleged code is bounded below and data-driven hypotheses are handled by the prior

> "There are not so many useful codes (see Appendix B), so that a code fitting a random outcome of directions would typically have an extremely small prior probability"

> "the prior belief in C C can reasonably be bounded from below, because the way the codes have to be transmitted (orientation of cards, banging trash cans) do not allow for too many variations given that they should be useful."

**ID:** few-meaningful-codes-prior
**Location:** Section 3.2.4 "Prior and posterior odds"; Section 5 "Discussion and conclusions"
**Grep command used:** `Grep pattern="There are not so many useful codes|reasonably be bounded from below" path="literature/extracted/boonstra_2024.txt"`

---

## Claim 9: What makes a code "meaningful" — tangible advantage, realistic to implement, binary

> "The code provides a tangible advantage to the players;"

> "The code can be realistically implemented;"

> "The information is transmitted by leading either horizontally or vertically, that is, in a binary way."

**ID:** meaningful-code-criteria
**Location:** Appendix B "Meaningful codes"
**Grep command used:** `Grep pattern="tangible advantage to the players|realistically implemented|in a binary way" path="literature/extracted/boonstra_2024.txt"`

---

## Claim 10: Timing as further evidence — bangs fall between the sign and the pitch, which would raise the likelihood ratio further

> "Almost all bangs occur after the catcher’s signaling and just before the pitcher begins the pitch."

> "which in this hypothetical scenario would result in a factor of at least 5 for every bang towards the hypothesis of cheating."

**ID:** timing-evidence-not-modelled
**Location:** Section 4.2 "A Bayesian analysis"
**Grep command used:** `Grep pattern="Almost all bangs occur after|factor of at least 5 for every bang" path="literature/extracted/boonstra_2024.txt"`

---

## Claim 11: Small payloads matter — a tiny extra clue can cascade into much better decisions

> "One can imagine that one tiny extra clue can very well cause a cascade of new deductions, resulting in significantly better decisions."

**ID:** tiny-clue-large-advantage
**Location:** Appendix A "Impact of cheating with leads"
**Grep command used:** `Grep pattern="one tiny extra clue" path="literature/extracted/boonstra_2024.txt"`

---

## Claim 12: Extension to chess — engine-cheating evidence would combine move-quality models with the frequency of suspicious behaviour

> "In this case, the models need to involve two aspects: the quality of the chess moves and the frequency of the toilet use. There exist models that measure the performance based on the moves played"

**ID:** chess-extension-move-quality
**Location:** Section 5 "Discussion and conclusions"
**Grep command used:** `Grep pattern="quality of the chess moves" path="literature/extracted/boonstra_2024.txt"`

---

## Claim 13: Approach — a Bayesian forensic framework for alleged hidden codes in sport: weigh the likelihood of the observed events under a named code against their likelihood under no code

> "We develop a statistical framework to evaluate evidence of alleged cheating involving illegal signaling in sports from a forensic perspective. We explain why, instead of a frequentist procedure, a Bayesian approach is called for. We apply this framework to cases of alleged cheating in professional bridge and professional baseball. The diversity of these applications illustrates the generality of the method."

**ID:** approach-bayesian-hidden-code-forensics
**Location:** Abstract
**Grep command used:** `Grep pattern="We develop a statistical framework to evaluate evidence|The diversity of these applications" path="literature/extracted/boonstra_2024.txt"`

**Depends-on:** regan_2011:approach-intrinsic-rating-model (grounded by #chess-extension-move-quality)

---

## Claim 14: Surveyed — code C (bridge): lead-card orientation signals whether a top honour is held, and the opposing declarer is unaware of the signal

> "If a card is led horizontally, this denies a top honor (ace, king or queen) in the lead suit. Conversely, if the card is lead vertically, this implies holding a top honor in that suit. This rule does (naturally) not apply in case the lead card was a singleton"

> "Furthermore, an agreement like code C has the added benefit that declarer is unaware of the signaling"

**ID:** surveyed-card-orientation-code-c
**Location:** Section 3.1 "The basics of contract bridge"; Section 3.2 "A Bayesian analysis"
**Grep command used:** `Grep pattern="This rule does \(naturally\) not apply|an agreement like code C has the added benefit" path="literature/extracted/boonstra_2024.txt"`

---

## Claim 15: Surveyed — code B (baseball): a trash-can bang relays a stolen catcher's sign for any non-fastball, silence for a fastball

> "Vice versa, if the catcher gives a sign for any non-fastball, such as a breaking ball or a changeup, the trash can is banged."

> "We found very strong evidence for a slightly different but also very simple code"

**ID:** surveyed-trash-can-code-b
**Location:** Section 4.1 "The case"
**Grep command used:** `Grep pattern="sign for any non-fastball|very strong evidence for a slightly different" path="literature/extracted/boonstra_2024.txt"`
