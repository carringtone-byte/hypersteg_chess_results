---
paper: "Hernandez-Castro et al. (2006)"
title: "Steganography in games: A general methodology and its application to the game of Go"
doi: "10.1016/j.cose.2005.12.001"
pmcid: "<PMC ID, if any>"
url: "<source URL the file was fetched from>"
source_version: "published"
file: "literature/hernandezcastro_2006.pdf"
retrieved: "20261105"
verified_by: "Claude (Opus 5.5) subagent, quotes checked with verify_quotes.py (read-only run)"
# The six below are written by `verify_quotes.py --stamp` — do not hand-edit.
# They bind the ledger to the exact source/extract bytes AND its own quoted text
# (body_sha256) it was verified against, so a later quote edit is caught in CI.
source_sha256: "3a91e3b4e59953adaf0d5ae73c4b512b6c66dc194732d6d3394f52cf723607f4"
extract_sha256: "5ebce2787782ce9ec9853c2792e83c5109590735701e72676fd2935b972bb954"
body_sha256: "5786a091841d08e78c0788c616424fa08ee58162f1cb5b662bbab62d2f07fcc5"
verifier_version: "2"
verified_verdict: "pass"
verified_date: "20261106"
extract_source_sha256: "3a91e3b4e59953adaf0d5ae73c4b512b6c66dc194732d6d3394f52cf723607f4"
---

# Verified Claims — Hernandez-Castro et al. (2006)

Each claim below was extracted by reading the downloaded paper file with the Read
tool, grepping for the specific content, and reading the surrounding context to
confirm the attribution is faithful.

**Rules:**
- Every entry must contain a DIRECT QUOTE from the paper (in blockquote).
- The quote must be locatable by grepping the downloaded file.
- "Location" = the heading/section (HTML) or page number (PDF) where the quote appears.
- Never paraphrase from memory — if you cannot find the quote, do not write the entry.
- Primary sources only — the source that made the claim, not a secondary write-up of it. What
  counts as primary depends on the project's declared `source_types` (papers, official reports, a
  recorded debate, …; see `spec/EXTRACTION.md`); for a paper project that is peer-reviewed
  literature, not a news article about it.

## Claim 1: Carrier and coding — the move played is chosen from engine-ranked good moves, its rank encoding the bits

> "compute for each position played in the game all the movements which are over a certain threshold value T, and then codify in the selection of the actual played move some bits of the message we want to hide"

**ID:** move-choice-threshold
**Location:** Section 3.1 "Playing a new game", p. 67
**Grep command used:** `Grep pattern="over a certain" path="literature/extracted/hernandezcastro_2006.txt"`

---

## Claim 2: Coding — index into the evaluation-sorted move list; capacity about log2(gm) bits per position

> "then sort them by their value (according to the evaluation function) and select the i-th move to codify the binary representation of the number i. In this way, in each position we will be able to hide around log"

**ID:** sorted-index-coding
**Location:** Section 3.1 "Playing a new game", p. 67
**Grep command used:** `Grep pattern="select the i-th move" path="literature/extracted/hernandezcastro_2006.txt"`

---

## Claim 3: Shared state — identical software, a common secret key and parameters so engine states are reproducible

> "Both parts of the communication channel should have access to exactly the same software, and share a common secret key (used for encrypting the hidden contents) and some other parameters (i.e. the board size, the software version, etc.) to assure that the software's internal states are reproducible by the two parties."

**ID:** shared-engine-and-key
**Location:** Section 3.1 "Playing a new game", p. 67
**Grep command used:** `Grep pattern="exactly the same software" path="literature/extracted/hernandezcastro_2006.txt"`

---

## Claim 4: Capacity is bounded by the number of strategies available at each stage, and decoding requires shared ordering

> "Note that the channel capacity is limited by the very nature of the game and, more specifically, by the amount of strategies available to players at each stage of the game. It is clear that for this scheme to properly operate, both players must have access to the structure of ordered strategies"

**ID:** capacity-bound-strategies
**Location:** Section 2.2 "Information and channel capacity", p. 66
**Grep command used:** `Grep pattern="channel capacity is limited" path="literature/extracted/hernandezcastro_2006.txt"`

---

## Claim 5: Capacity–invisibility trade-off set by the threshold T

> "By increasing T, the channel capacity will grow, since we will have more gm to embed hidden bits. Alternatively, decreasing T will result in a higher invisibility of the hidden contents, for chosen strategies do not deviate significantly from optimal."

**ID:** threshold-tradeoff
**Location:** Section 3.1 "Playing a new game", p. 67
**Grep command used:** `Grep pattern="By increasing T" path="literature/extracted/hernandezcastro_2006.txt"`

---

## Claim 6: Second carrier — variations appended to an already played game, encoding by start point, length and moves

> "Each of these variants could embed bits by various means: choosing at what movement does the variant begin, the length of the variant, and obviously, in every move of the variant, just by using the same algorithm described above for codifying hidden data in moves."

**ID:** variation-carrier
**Location:** Section 3.2 "Inserting data into a game", p. 67
**Grep command used:** `Grep pattern="choosing at what" path="literature/extracted/hernandezcastro_2006.txt"`

---

## Claim 7: Third carrier — annotation comments as a synonym codebook (8 comments, three bits); higher capacity but low robustness

> "might be used to express the same and, simultaneously, codify three bits. Likewise, any other technique derived from the field of text steganography could be applied in this context."

> "it also has the important drawback of a much lower robustness: it suffices to delete all comments to erase the hidden data, but at the cost of severely decreasing the attractiveness and usefulness of the game file."

**ID:** comment-codebook
**Location:** Section 3.2 "Inserting data into a game", p. 67
**Grep command used:** `Grep pattern="codify three bits|much lower robustness" path="literature/extracted/hernandezcastro_2006.txt"`

---

## Claim 8: Proposed steganalysis — game length, game level and game result

> "The main game characteristics that might be sensible to these changes are the following"

> "the selection of moves other than the best in a certain position should produce games where one player (the one that codifies data) plays steadily worst than the other."

**ID:** steganalysis-length-level-result
**Location:** Section 4 "Steganalysis", p. 68
**Grep command used:** `Grep pattern="sensible to these changes|plays steadily worst" path="literature/extracted/hernandezcastro_2006.txt"`

---

## Claim 9: Implementation and detection result — StegoGo, three bits per move; one-sided embedding not detected at 100 games

> "This first version of the S TEGOGO program hides three bits of information per move, being capable of compressing"

> "This implies that more than 100 games would be needed to mount a successful steganalytic attack against S"

**ID:** stegogo-detection
**Location:** Section 5 "An implementation for Go", p. 69
**Grep command used:** `Grep pattern="three bits of in|more than 100 games" path="literature/extracted/hernandezcastro_2006.txt"`

---

## Claim 10: Countermeasure and builds-on — both players embedding defends against result-based steganalysis; builds on Murdoch and Zielinski's ranked equivalent moves

> "the best practice against steganalysis based on game result is for both players to hide data (even garbage) in their moves."

> "The idea is to order the aforementioned set of n equivalent moves by some prearranged criterion, then chose the rth move to send the value r."

**ID:** both-embed-and-prior-art
**Location:** Section 5, p. 70; Section 1 "Introduction", p. 65
**Grep command used:** `Grep pattern="even garbage|prearranged criterion" path="literature/extracted/hernandezcastro_2006.txt"`

---

## Claim 11: Approach — ranked move choice while playing a new game: both parties run the same engine with a shared key, list the moves scoring above a threshold T, sort them by evaluation and play the i-th to send i

> "In this work, we present and analyze a novel methodology that illustrates how games (such as Chess, Backgammon, Go, etc.) can be used to hide digital contents."

> "The main idea is to compute for each position played in the game all the movements which are over a certain threshold value T, and then codify in the selection of the actual played move some bits of the message we want to hide"

> "then sort them by their value (according to the evaluation function) and select the i-th move to codify the binary representation of the number i."

**ID:** approach-ranked-move-choice
**Location:** Abstract, p. 64; Section 3.1 "Playing a new game", p. 67
**Grep command used:** `Grep pattern="present and analyze a novel|The main idea is to compute|select the i-th move" path="literature/extracted/hernandezcastro_2006.txt"`

---

## Claim 12: Prior art described — Murdoch and Zielinski's ordered equivalent moves for authenticating colluders, the one notable experiment the paper sets its own general methodology against

> "A recent and notable experiment is described in Murdoch and Zielinski (2004) , where a team of researchers developed a number of different programs to play and collude in a Connect-4 variant online programming competition at Cambridge University."

> "authors cite and analyze the timing of moves (by purposely delaying the execution of certain moves) and the choice of equivalent moves, and chose the latter."

> "There are very few additional works that relate data hiding and games, and none in the way proposed in this article."

**ID:** prior-art-murdoch
**Location:** Section 1 "Introduction", p. 65 (Murdoch and Zielinski 2004, "Covert channels for collusion in online computer games", is ledgered as `murdoch_2004`)
**Grep command used:** `Grep pattern="notable experiment is described in Murdoch|choice of equivalent moves, and chose|none in the way proposed" path="literature/extracted/hernandezcastro_2006.txt"`

**Refines:** murdoch_2004:approach-equivalent-move-channel (grounded by #prior-art-murdoch)

---

## Claim 13: Approach — variations inserted into an already played game: each variant encodes bits by where it starts, how long it runs and, move by move, the ranked-choice rule

> "It simply consists in including variations and comments in already played games."

> "In this way, at certain positions in the game we would introduce variants of the main line played. Each of these variants could embed bits by various means: choosing at what movement does the variant begin, the length of the variant, and obviously, in every move of the variant, just by using the same algorithm described above for codifying hidden data in moves."

**ID:** approach-variation-carrier
**Location:** Section 3.2 "Inserting data into a game", p. 67
**Grep command used:** `Grep pattern="including variations and comments|introduce variants of the main line|choosing at what" path="literature/extracted/hernandezcastro_2006.txt"`

---

## Claim 14: Approach — comment codebook: a set of annotations that say the same thing (eight here, so three bits), open to any text-steganography technique, easy to strip

> "Another possible channel for embedding information is the inclusion of comments."

> "might be used to express the same and, simultaneously, codify three bits. Likewise, any other technique derived from the field of text steganography could be applied in this context."

> "it suffices to delete all comments to erase the hidden data, but at the cost of severely decreasing the attractiveness and usefulness of the game file."

**ID:** approach-comment-codebook
**Location:** Section 3.2 "Inserting data into a game", p. 67
**Grep command used:** `Grep pattern="possible channel for embedding information is the inclusion|codify three bits|delete all comments" path="literature/extracted/hernandezcastro_2006.txt"`

---

## Claim 15: Approach (steganalysis) — statistical attacks on game length, playing level and result, and stripping variations and comments; countered by encryption, raised komi and both sides embedding

> "Statistical attacks try to detect significant deviations, produced by the insertion of hidden data into the stego medium, from a given statistical model."

> "the codifying part would in general be playing at a lower level than the non-codifying part, and routinely making more mistakes (or less accurate moves)."

> "For the variation wherein we hide data into a game by inserting comments and variations, an obvious attack path is to erase all variations from a given game."

> "This will make the game more fair, shortening the strength differences derived from the codification of information, thus making this codification harder to detect."

**ID:** approach-game-steganalysis
**Location:** Section 4 "Steganalysis", p. 68; Section 4.1 "Countermeasures", p. 68
**Grep command used:** `Grep pattern="Statistical attacks try to detect|playing at a lower level|obvious attack path|make the game more fair" path="literature/extracted/hernandezcastro_2006.txt"`
