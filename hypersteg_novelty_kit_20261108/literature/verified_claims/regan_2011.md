---
paper: "Regan and Haworth (2011)"
title: "Intrinsic Chess Ratings"
doi: "<DOI>"
pmcid: "<PMC ID, if any>"
url: "https://centaur.reading.ac.uk/19778/"
source_version: "preprint"
file: "literature/regan_2011.pdf"
retrieved: "20261105"
verified_by: "Claude (Opus 5.5) subagent, quotes checked with verify_quotes.py (read-only run)"
# The six below are written by `verify_quotes.py --stamp` — do not hand-edit.
# They bind the ledger to the exact source/extract bytes AND its own quoted text
# (body_sha256) it was verified against, so a later quote edit is caught in CI.
source_sha256: "dc61e20376518e06a5b717e194b00c4e8720f0fff3feaffee9b39b5ecbb3196b"
extract_sha256: "d27ca9c92ebb77a47844ff66d2d0736d8f32fd3f5fe816901690d9ad34941bb7"
body_sha256: "2922bc0c0c5c4da63c6b576bc020ae0bb6e67059c0486637f762301b45225789"
verifier_version: "2"
verified_verdict: "pass"
verified_date: "20261106"
extract_source_sha256: "dc61e20376518e06a5b717e194b00c4e8720f0fff3feaffee9b39b5ecbb3196b"
---

# Verified Claims — Regan and Haworth (2011)

Each claim below was extracted by reading the downloaded paper file with the Read
tool, grepping for the specific content, and reading the surrounding context to
confirm the attribution is faithful.

Source note: the file is the CentAUR accepted version of the AAAI-11 paper
(pp. 834–839); the extract's cover page records it as "Accepted Version". This paper
is not a steganography method: it supplies a model of human move choice that a warden
could use as the "clean cover" baseline for move-selection channels.

**Rules:**
- Every entry must contain a DIRECT QUOTE from the paper (in blockquote).
- The quote must be locatable by grepping the downloaded file.
- "Location" = the heading/section (HTML) or page number (PDF) where the quote appears.
- Never paraphrase from memory — if you cannot find the quote, do not write the entry.
- Primary sources only — the source that made the claim, not a secondary write-up of it. What
  counts as primary depends on the project's declared `source_types` (papers, official reports, a
  recorded debate, …; see `spec/EXTRACTION.md`); for a paper project that is peer-reviewed
  literature, not a news article about it.

## Claim 1: Purpose — rate strength by the quality of moves played, judged by a strong engine, rather than by results

> "This paper develops and tests formulas for representing playing strength at chess by the quality of moves played, rather than the results of games."

**ID:** intrinsic-quality
**Location:** Abstract, p. 1
**Grep command used:** `Grep pattern="quality of moves played" path="literature/extracted/regan_2011.txt"`

---

## Claim 2: The model uses only the spread of engine evaluations over the top moves, the move played and the position evaluation

> "The only game-specific information used by our methods is the spread, the actual move played, and the overall evaluation of the position ."

**ID:** spread-only-input
**Location:** Section 1 "Introduction", p. 2
**Grep command used:** `Grep pattern="game-speciﬁc information" path="literature/extracted/regan_2011.txt"`

---

## Claim 3: All relevant alternatives must be evaluated to model probabilistic move choice

> "it is necessary to evaluate all of the relevant available moves."

**ID:** evaluate-all-moves
**Location:** Section 1 "Introduction", p. 2
**Grep command used:** `Grep pattern="evaluate all of the relevant" path="literature/extracted/regan_2011.txt"`

---

## Claim 4: Move-choice probabilities follow a curve in the evaluation gap, with sensitivity s and competence c

> "Our key abstract concept is the probability"

> "Hence s governs a player's ability to discriminate moderately inferior moves, so we call it the sensitivity."

**ID:** sensitivity-competence
**Location:** Section 3 "Basic Model", p. 3; Section 4 "Possible Move-Choice Formulas", p. 5
**Grep command used:** `Grep pattern="key abstract concept|we call it the sensitivity" path="literature/extracted/regan_2011.txt"`

---

## Claim 5: Modelling assumption — choices at different turns are independent (acknowledged false for multi-move plans)

> "A player's choices at different game turns are independent, even for successive game turns."

> "Assumption (3) is intuitively false when a sequence of move choices constitutes a single plan."

**ID:** turn-independence
**Location:** Section 3 "Basic Model", p. 3–4
**Grep command used:** `Grep pattern="choices at different game turns|constitutes a single" path="literature/extracted/regan_2011.txt"`

---

## Claim 6: Result — a smooth relation between Elo and the fitted parameters

> "Our first major conclusion is that there is a fairly smooth relationship between the players' Elo rating and the intrinsic quality of the moves as measured by the chess program and the fitting."

**ID:** elo-correspondence
**Location:** Section 7 "Results", p. 10
**Grep command used:** `Grep pattern="fairly smooth relationship" path="literature/extracted/regan_2011.txt"`

---

## Claim 7: Detection use — distributional prediction to detect computer-assisted cheating; testing excess engine agreement

> "By modeling human players of various strengths, the model also enables distributional prediction to detect cheating by getting computer advice during games."

> "The result will be a model of move choice that is capable of testing allegations of whether players—of a given skill level—have been agreeing with computer evaluations more than chance would warrant."

**ID:** cheating-detection
**Location:** Abstract, p. 1; Section 8 "Conclusions and Further Directions", p. 10
**Grep command used:** `Grep pattern="detect cheating|more than chance would warrant" path="literature/extracted/regan_2011.txt"`

---

## Claim 8: Builds on and supersedes Guid and Bratko (2006), which evaluated only the played and preferred moves

> "evaluated only the played move and Crafty's preferred move, if different."

**ID:** supersedes-guid-bratko
**Location:** Section 1 "Introduction", p. 2
**Grep command used:** `Grep pattern="evaluated only the played move" path="literature/extracted/regan_2011.txt"`

---

## Claim 9: Approach (contribution) — an intrinsic-rating model of human move choice: engine evaluations of all reasonable moves give each move a probability set by sensitivity s and competence c, fitted to Elo by regression and usable to detect engine assistance

> "This paper develops and tests formulas for representing playing strength at chess by the quality of moves played, rather than the results of games."

> "Several formulas, each having intrinsic skill parameters s for “sensitivity” and c for “competence,” are argued theoretically and tested by regression on large sets of tournament games played by humans of varying strength as measured by the internationally standard Elo rating system."

> "The only game-specific information used by our methods is the spread, the actual"

> "“exponential decay” of probability in going from an optimal move to an inferior one."

**ID:** approach-intrinsic-rating-model
**Location:** Abstract, p. 1; Section 1 "Introduction", p. 2; Section 3 "Basic Model", p. 4 (page numbers from the accepted-version page footers in the extract)
**Grep command used:** `Grep pattern="develops and tests formulas|intrinsic skill parameters s|only game-speciﬁc information|exponential decay” of probability" path="literature/extracted/regan_2011.txt"`
