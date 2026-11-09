---
paper: "Jhamtani et al. (2018)"
title: "Learning to Generate Move-by-Move Commentary for Chess Games from Large-Scale Social Forum Data"
doi: "10.18653/v1/P18-1154"
pmcid: "<PMC ID, if any>"
url: "<source URL the file was fetched from>"
source_version: "published"
file: "literature/jhamtani_2018.pdf"
retrieved: "20261105"
verified_by: "Claude (Opus 5.5) subagent, quotes checked with verify_quotes.py (read-only run)"
# The six below are written by `verify_quotes.py --stamp` — do not hand-edit.
# They bind the ledger to the exact source/extract bytes AND its own quoted text
# (body_sha256) it was verified against, so a later quote edit is caught in CI.
source_sha256: "2eb0a06061e37b3c77b48cc1d19bde88023de3182f46fffd4bb9b3994ea786b9"
extract_sha256: "30a7b5e3b2fcc8099bf2a11a885f1a8455ff87a6c81d7b64167ab6c0b8620928"
body_sha256: "4dd2a88ab6cd34e484acfa71f6326175ed0141ef3ed02024d0d74ceb093ab96a"
verifier_version: "2"
verified_verdict: "pass"
verified_date: "20261106"
extract_source_sha256: "2eb0a06061e37b3c77b48cc1d19bde88023de3182f46fffd4bb9b3994ea786b9"
---

# Verified Claims — Jhamtani et al. (2018)

Each claim below was extracted by reading the downloaded paper file with the Read
tool, grepping for the specific content, and reading the surrounding context to
confirm the attribution is faithful.

Source note: Proceedings of the 56th Annual Meeting of the ACL (Long Papers), pp.
1661–1671, Melbourne, 2018. Authors: Harsh Jhamtani, Varun Gangal, Eduard Hovy, Graham
Neubig, Taylor Berg-Kirkpatrick. Not a steganography method: it supplies a corpus of
real move-by-move commentary and a description of what such commentary contains, the
cover a commentary channel must imitate.

**Rules:**
- Every entry must contain a DIRECT QUOTE from the paper (in blockquote).
- The quote must be locatable by grepping the downloaded file.
- "Location" = the heading/section (HTML) or page number (PDF) where the quote appears.
- Never paraphrase from memory — if you cannot find the quote, do not write the entry.
- Primary sources only — the source that made the claim, not a secondary write-up of it. What
  counts as primary depends on the project's declared `source_types` (papers, official reports, a
  recorded debate, …; see `spec/EXTRACTION.md`); for a paper project that is peer-reviewed
  literature, not a news article about it.

## Claim 1: Corpus — 298K move/commentary pairs across about 11K games, from the gameknot.com forum

> "The introduced dataset consists of more than 298K chess move-commentary pairs across 11K chess games."

> "The data is collected from the online chess discussion forum gameknot.com, which features multiple games self-annotated with move-by-move commentary."

**ID:** commentary-corpus
**Location:** Abstract, p. 1661; Section 2 "Chess Commentary Dataset", p. 1662
**Grep command used:** `Grep pattern="298K chess move|gameknot" path="literature/extracted/jhamtani_2018.txt"`

---

## Claim 2: Commentary falls into six categories, from direct move description to general remarks

> "We classify the commentaries into 6 different categories using a classifier trained on some hand-labelled data"

> "Direct move description (MoveDesc3): Ex-plicitly or implicitly describe the current move."

**ID:** six-categories
**Location:** Section 2, Table 2, p. 1663
**Grep command used:** `Grep pattern="6 different cate|Direct move description" path="literature/extracted/jhamtani_2018.txt"`

---

## Claim 3: Commentators choose which aspect to discuss by pragmatic context, and vary it to avoid monotony

> "there are multiple aspects of the game state that can be talked about for a given move — the commentator's choice depends on the pragmatic context of the game."

> "a human commentator may introduce varia-tions in the aspects he or she chooses to talk about, in order to reduce monotony in the commentary."

**ID:** aspect-choice
**Location:** Section 1 "Introduction", p. 1662
**Grep command used:** `Grep pattern="multiple aspects of|reduce monotony" path="literature/extracted/jhamtani_2018.txt"`

---

## Claim 4: The generator conditions on move, threat and Stockfish score features from the boards before and after the move

> "Our method uses various semantic and pragmatic features of the move, including the location and type of piece being moved, which opposing team pieces attack the piece being moved before as well as after the move, the change in score by Stockfish UCI engine, etc."

**ID:** gac-features
**Location:** Section 3, Figure 3 caption, p. 1664
**Grep command used:** `Grep pattern="semantic and pragmatic features of the move" path="literature/extracted/jhamtani_2018.txt"`

---

## Claim 5: Template commentary lacks diversity, measured by n-gram entropy

> "outputs from rule based templates, which demonstrate low variety, may seem repetitive and boring."

> "we calculate the entropy (Shannon, 1951) of the distribution of unigrams, bigrams and trigrams of words in the predicted outputs"

**ID:** template-low-diversity
**Location:** Section 4.4 "Diversity In Generated Commentaries", p. 1667–1668
**Grep command used:** `Grep pattern="rule|calculate the entropy" path="literature/extracted/jhamtani_2018.txt"`

---

## Claim 6: Human judges rated generated move descriptions as good as human-written commentary

> "A human evaluation study judges outputs from the proposed methods to be as good as human written commentary texts for 'Move Description' subset of the data."

**ID:** human-parity
**Location:** Section 6 "Conclusions", p. 1669
**Grep command used:** `Grep pattern="judges outputs from the" path="literature/extracted/jhamtani_2018.txt"`

---

## Claim 7: About 30% of human-written commentary was judged not valid for its move

> "A more surprising observation is that around 30% of human written ground truth outputs were also marked as not valid for given board move."

**ID:** human-commentary-noise
**Location:** Section 4.5 "Human Evaluation Study", p. 1668
**Grep command used:** `Grep pattern="around 30% of human written" path="literature/extracted/jhamtani_2018.txt"`

---

## Claim 8: BLEU is low and correlates poorly with human judgement here

> "we often found the outputs to be good - though BLEU scores are low."

**ID:** bleu-low
**Location:** Section 4.5 "Human Evaluation Study", p. 1668
**Grep command used:** `Grep pattern="though" path="literature/extracted/jhamtani_2018.txt"`

---

## Claim 9: Builds on — earlier chess commentary generation was rule-based for lack of data

> "have explored chess commentary genera-tion, but for lack of large-scale training data their methods have been mainly rule-based."

**ID:** prior-rule-based
**Location:** Section 1 "Introduction", p. 1662
**Grep command used:** `Grep pattern="mainly rule-based" path="literature/extracted/jhamtani_2018.txt"`

---

## Claim 10: Approach — GAC, an end-to-end neural generator that selects salient board features and decodes commentary with an LSTM

> "We model this using an end-to-end trainable neural model, which models conjunctions of features using feature encoders. Our model employs a selection mechanism to select the salient features for a given chess move. Finally a LSTM recurrent neural network (Hochreiter and Schmidhuber, 1997) is used to generate the commentary text based on selected features from encoder."

> "For simplicity, we use only current board ( Ci) and previous board ( Ri) information from the game."

**ID:** approach-gac
**Location:** Section 3 "Game Aware Neural Commentary Generations (GAC)", p. 1663
**Grep command used:** `Grep pattern="end-to-end trainable|selection mechanism to select the salient" path="literature/extracted/jhamtani_2018.txt"`
