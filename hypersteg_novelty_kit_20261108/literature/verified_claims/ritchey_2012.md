---
paper: "Ritchey and Rego (2012)"
title: "Covert Channels in Combinatorial Games"
doi: "10.4108/icst.simutools.2012.247733"
pmcid: "<PMC ID, if any>"
url: "<source URL the file was fetched from>"
source_version: "published"
file: "literature/ritchey_2012.pdf"
retrieved: "20261105"
verified_by: "Claude (Opus 5.5) subagent, quotes checked with verify_quotes.py (read-only run)"
# The six below are written by `verify_quotes.py --stamp` — do not hand-edit.
# They bind the ledger to the exact source/extract bytes AND its own quoted text
# (body_sha256) it was verified against, so a later quote edit is caught in CI.
source_sha256: "aab66d55172a690bb3ec8fdba6ec155b2a926eac8925118f7d877ecf28ab0cac"
extract_sha256: "14beb6bba6ca5f544c50f60e3e5925112e28a4b28732686b602eb61d4d648409"
body_sha256: "f23cd5c0892a1137734b1bc55bd8797a917b973e34b13ba211c8bb50576d89c1"
verifier_version: "2"
verified_verdict: "pass"
verified_date: "20261106"
extract_source_sha256: "aab66d55172a690bb3ec8fdba6ec155b2a926eac8925118f7d877ecf28ab0cac"
---

# Verified Claims — Ritchey and Rego (2012)

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

## Claim 1: Carrier — game play as a cover-generation method; the cover is the move sequence

> "The process of playing a game for the purpose of establishing covert communication can be viewed as a cover generation method. The cover being generated is a sequence of moves in a combinatorial game."

**ID:** cover-generation-moves
**Location:** Section 2 "Channel and Methodology", p. 2
**Grep command used:** `Grep pattern="cover gen" path="literature/extracted/ritchey_2012.txt"`

---

## Claim 2: Capacity — up to floor(log2 N) bits per move, N the number of moves available

> "In general, a player could send up to"

> "bits of data per move, where N is the number of possible moves available to the player for that move."

**ID:** floor-log2-capacity
**Location:** Section 2 "Channel and Methodology", p. 2
**Grep command used:** `Grep pattern="could send up to|bits of data per" path="literature/extracted/ritchey_2012.txt"`

---

## Claim 3: Coding and key — index into the set of best moves after a keyed random permutation (shared RNG and seed)

> "The set of best moves is randomly permuted using a shared random number generator and seed. The embedding is accomplished by extracting and consuming the correct number of bits from the secret and using them as the index value into the permuted set of best moves."

**ID:** permuted-best-move-index
**Location:** Section 3.3 "Algorithms", p. 4
**Grep command used:** `Grep pattern="randomly permuted using" path="literature/extracted/ritchey_2012.txt"`

---

## Claim 4: Key — the permutation acts as a variable-length substitution cipher; sparse use of the channel by shared RNG, like chaffing and winnowing

> "This provides an additional layer of security by acting as a variable length substitution cipher so that any given move does not always encode the same data. Another technique is to use the channel only occasionally, either on a game-by-game or move-by-move basis"

**ID:** substitution-and-sparse-use
**Location:** Section 2 "Channel and Methodology", p. 2
**Grep command used:** `Grep pattern="variable" path="literature/extracted/ritchey_2012.txt"`

---

## Claim 5: Capacity under perfect play — optimal play reduces capacity but leaves it non-zero

> "it turns out that Wendy's assumption that perfect play precludes covert communication is false; Alice and Bob can play perfectly and still have covert channel capacity available."

> "Experimental and analytical results on the capacity of the channel showed that playing optimally reduces, but does not eliminate the capacity of the channel."

**ID:** perfect-play-capacity
**Location:** Section 3.2.1 "Security", p. 3; Section 6 "Conclusion", p. 6
**Grep command used:** `Grep pattern="precludes covert|playing optimally re" path="literature/extracted/ritchey_2012.txt"`

---

## Claim 6: Security — the warden detects by checking moves against her model of play (Greedy or Optimal Wendy)

> "That is, Wendy will test whether the moves Alice and Bob make agree with her model of how the game should be played."

**ID:** warden-play-model
**Location:** Section 3.2.1 "Security", p. 3
**Grep command used:** `Grep pattern="her model of how the game" path="literature/extracted/ritchey_2012.txt"`

---

## Claim 7: Security result — detection depends entirely on whose model of the cover space is better

> "When Alice and Bob have a model of the cover-object space which is as good as or better than Wendy's model, then they can sneak hidden information past her without any problems. When Wendy has the better model, Alice and Bob are easily defeated."

**ID:** model-quality-decides
**Location:** Section 4.2 "Security Results", p. 5
**Grep command used:** `Grep pattern="sneak hidden information" path="literature/extracted/ritchey_2012.txt"`

---

## Claim 8: Robustness — not addressed beyond a trusted channel with a passive adversary

> "Thus, robustness becomes a mute point and can be safely skipped, for now."

**ID:** robustness-skipped
**Location:** Section 3.2 "Properties of the Channel", p. 3
**Grep command used:** `Grep pattern="robustness" path="literature/extracted/ritchey_2012.txt"`

---

## Claim 9: Builds on — Hernandez-Castro et al.'s ordered-strategy approach; claims prior chess and Go work ignored natural-looking play

> "In [5], Hernandez-Castro et al. describe an approach to hiding data in games which is built upon in this work."

> "However, these papers do not address the possibilty that the games can be played naturally (as if by a human) and still transmit information."

**ID:** builds-on-hernandezcastro
**Location:** Section 2, p. 2; Section 1 "Introduction", p. 1
**Grep command used:** `Grep pattern="built upon in this work|played naturally" path="literature/extracted/ritchey_2012.txt"`

---

## Claim 10: Approach — a general framework for covert channels in combinatorial games: the sender generates the cover by playing, assigns bit strings to the moves her strategies allow, and plays the move whose string matches the next data; shown on Tic-Tac-Toe, said to carry to Chess and Go

> "A general framework for exploiting covert channels in combinatorial games is presented. The framework is applicable to all combinatorial games, including Chess and Go, but is applied to the game of Tic-Tac-Toe for ease of experimental analysis."

> "At each step, Alice uses her set of strategies to construct a set of moves. To each of these moves, she assigns a bit string and selects the move whose bit string matches the next piece of data she wants to send."

> "The board is updated and sent to Bob who can reverse Alice’s last move to figure out what she sent."

> "The framework presented in this paper is applicable to these games and supports schemes which are substantially similar to those presented in the previous work on this topic."

**ID:** approach-combinatorial-game-framework
**Location:** Abstract, p. 1; Section 2 "Channel and Methodology", p. 2; Section 5 "Other Games", p. 5
**Grep command used:** `Grep pattern="general framework for exploiting covert|assigns a bit string and selects|reverse Alice’s last move|substantially similar to those" path="literature/extracted/ritchey_2012.txt"`

**Refines:** hernandezcastro_2006:approach-ranked-move-choice (grounded by #builds-on-hernandezcastro)

---

## Claim 11: Builds on — the Prisoners' Problem as the standard framework for the channel

> "For ease of exposition, a standard framework for studying covert channels, known as the Prisoners’ Problem [12] is drawn upon."

**ID:** builds-on-prisoners-problem
**Location:** Section 1 "Introduction", last paragraph before Section 2 (the extract runs the first page's copyright block into the introduction, so whether this falls on p. 1 or p. 2 is not settled from the text; reference [12] is G. J. Simmons, "The prisoner's problem and the subliminal channel", CRYPTO '83, ledgered as `simmons_1984`)
**Grep command used:** `Grep pattern="standard framework for studying covert" path="literature/extracted/ritchey_2012.txt"`

**Depends-on:** simmons_1984:approach-subliminal-channel (grounded by #builds-on-prisoners-problem)
