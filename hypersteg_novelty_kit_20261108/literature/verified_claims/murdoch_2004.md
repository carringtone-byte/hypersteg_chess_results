---
paper: "Murdoch and Zieliński (2004)"
title: "Covert Channels for Collusion in Online Computer Games"
doi: "<DOI>"
pmcid: "<PMC ID, if any>"
url: "In J. Fridrich (Ed.), Information Hiding 2004 (IH 2004), LNCS 3200, Springer, pp. 355–369; extracted from literature/_books/lncs3200_information_hiding_2004.pdf, PDF pages 364–379"
source_version: "published"
file: "literature/murdoch_2004.pdf"
retrieved: "20261105"
verified_by: "Claude (Opus 5.5) subagent, quotes checked with verify_quotes.py (read-only run)"
# The six below are written by `verify_quotes.py --stamp` — do not hand-edit.
# They bind the ledger to the exact source/extract bytes AND its own quoted text
# (body_sha256) it was verified against, so a later quote edit is caught in CI.
source_sha256: "b556773180befe34268e58bf1465203eca48b4a18a562ae2300616901898f425"
extract_sha256: "f3fdcafa4f1c7e0bea21fdd11ff71c568cde4d6e51a07585166d8cbaee1196b7"
body_sha256: "40e0fef88b90d82f5e78bf9bd84a78bbe02a6b772ff881bec6cad8fdeb49ac14"
verifier_version: "2"
verified_verdict: "pass"
verified_date: "20261106"
extract_source_sha256: "b556773180befe34268e58bf1465203eca48b4a18a562ae2300616901898f425"
---

# Verified Claims — Murdoch and Zieliński (2004)

Each claim below was extracted by reading the downloaded paper file with the Read
tool, grepping for the specific content, and reading the surrounding context to
confirm the attribution is faithful.

Source: Information Hiding, 6th International Workshop (IH 2004), LNCS 3200, Springer 2004,
pp. 355–369. `literature/murdoch_2004.pdf` holds PDF pages 364–379 of the proceedings volume
`literature/_books/lncs3200_information_hiding_2004.pdf`; the extract also carries the
volume's author index from the last of those pages, which is not part of the paper. Authors:
Steven J. Murdoch and Piotr Zieliński, University of Cambridge Computer Laboratory. The DOI is
not printed in the extract, so the DOI field is left unset. Page numbers below are the
proceedings page numbers printed in the extract.

## Claim 1: Setting — collusion among independent players, not team-mates, to reach a result none can reach alone

> "In this paper, a different type of collusion is discussed, where the parties colluding are not part of one team, but instead are multiple independent players, acting together in order to achieve a result that none of them are capable of achieving by themselves."

**ID:** independent-player-collusion
**Location:** Abstract, p. 355
**Grep command used:** `Grep pattern="multiple independent players, acting together" path="literature/extracted/murdoch_2004.txt"`

---

## Claim 2: Bridge precedent — legal signalling between partners, encoded in the cards played, with a shared secret acting as a key

> "These schemes typically provide a means by which one player can encode information about his hand in the cards that he plays."

> "However, the two members of a team do share a secret, e.g. if one player holds all the aces then he knows that his partner holds none, but the opposing team does not know this [3]."

> "If this secret is used as a key, then it is legal for the recipient of the information to only tell what the bid"

> "He does not need to tell his opponent what the bid means when combined with the knowledge of the player’s own hand."

**ID:** bridge-shared-secret-key
**Location:** Section 1 "Introduction", pp. 355–356 (the sentence runs across the page break; reference [3] is Winkler 1983, *The advent of cryptology in the game of Bridge*)
**Grep command used:** `Grep pattern="encode information about his hand|holds all the aces|If this secret is used as a" path="literature/extracted/murdoch_2004.txt"`

---

## Claim 3: Carrier — choice among equivalent moves; ranking the n outcome-equivalent moves and playing the r-th sends r

> "An alternative to this is to encode the authentication data in the moves themselves."

> "At a stage in the game, if there is more than one move which can be shown to not change the outcome of the game when compared to the best move, then this fact can be used to transmit information."

> "After receiving a move from its opponent, a player can identify which move, out of the opponents possible moves, was chosen and hence identify r."

**ID:** equivalent-move-channel
**Location:** Section 3.2 "Choice of Equivalent Moves", p. 360
**Grep command used:** `Grep pattern="authentication data in|not change the outcome of the game|out of the opponents possible moves" path="literature/extracted/murdoch_2004.txt"`

---

## Claim 4: Alternative carrier — move timing: easy and higher bandwidth, but unreliable under jitter and removable by fixing move times

> "One such channel would be to use the timing of moves to carry information by causing the sender to delay making a move and the recipient to measure this delay. Such schemes are easy to create and can have a relatively high bandwidth."

> "If this is done, then the move timing covert channel would be eliminated."

**ID:** move-timing-channel
**Location:** Section 3.1 "Timing", p. 359
**Grep command used:** `Grep pattern="timing of moves to carry information|move timing covert channel would be eliminated" path="literature/extracted/murdoch_2004.txt"`

---

## Claim 5: Capacity and reliability — one bit, sent before the result is fixed; low capacity, high reliability

> "the goal of the channel can be viewed as being able to transmit a single bit while the result of the game is still undetermined. While the required capacity of the channel is low, the reliability requirements are high"

**ID:** one-bit-high-reliability
**Location:** Section 3.3 "Analysis of Authentication Mechanisms", p. 360
**Grep command used:** `Grep pattern="transmit a single bit while the result" path="literature/extracted/murdoch_2004.txt"`

---

## Claim 6: Robustness — the move itself arrives intact, but independent players' moves act as noise the receiver cannot tell from signal

> "However, where the move itself carries the information it is reasonable to expect that the signal will be received intact."

> "However, this does not mean that the channel is noiseless, since the receiver cannot differentiate between the case where information is being sent, and the case where the moves carry no meaning"

> "The moves of independent players are analogous to noise in communications theory."

**ID:** move-channel-noise
**Location:** Section 3.3, pp. 360–361
**Grep command used:** `Grep pattern="received intact|channel is noiseless|analogous to noise in communications" path="literature/extracted/murdoch_2004.txt"`

---

## Claim 7: Pre-coordination — a shared key drives a frequency-hopping-style generator; the receiver checks that every move matched

> "In order to reliably transmit a single bit of information, a technique based on frequency-hopping can be used. For each move, the number sent is chosen according to a keyed generator. The receiver shares the key and so knows what move to expect from a colluding player."

> "For example r could simply be the result of a pseudorandom number generator (PRNG) seeded by a shared secret."

**ID:** keyed-generator-frequency-hopping
**Location:** Section 3.3, p. 361; Section 3.4 "Authentication Key", p. 361
**Grep command used:** `Grep pattern="technique based|seeded by a shared secret" path="literature/extracted/murdoch_2004.txt"`

---

## Claim 8: Threat model — opponents see only the moves and are not adaptive, so cryptanalysis is assumed unlikely; a fixed signal risks accidental matching

> "In the case of spread-spectrum radio the transmission is effectively public but in a game the moves are typically only seen by the opponent."

> "When coupled with the fact that other opponents are probably not aware of the collusion strategy, it is reasonable to assume that cryptanalytic attacks are unlikely."

> "However, it is feasible that an opponent could accidentally pick the same strategy."

**ID:** weak-threat-model
**Location:** Section 3.4 "Authentication Key", p. 361
**Grep command used:** `Grep pattern="only seen by the opponent|cryptanalytic attacks are unlikely|accidentally pick the same strategy" path="literature/extracted/murdoch_2004.txt"`

---

## Claim 9: Trade-off — confidence grows with more options per move and more moves, but waiting too long loses the chance to alter the result

> "The confidence level of the decision being correct can be increased by increasing the number of possibilities at each move or by increasing number of moves before a decision is made."

> "if the player waits too long, then by the time a decision is made, it is no longer possible to change the game result."

> "so as to optimise the bandwidth of the covert channel, the number of possible moves at each turn should be maximised."

**ID:** confidence-versus-deadline
**Location:** Section 3.3, p. 361; Section 4.3 "Game Strategy", p. 363
**Grep command used:** `Grep pattern="confidence level of the decision|waits too long|number of possible moves at each turn" path="literature/extracted/murdoch_2004.txt"`

---

## Claim 10: Result in practice — a Connect-4 tournament won by colluding programs; false-positive risk bounded by the number of move sequences

> "This was a online programming competition where contestants were required to write a program to playConnect-4 against the other programs entered."

> "point at which a decision was made) the number of possible move sequences ranged between 960 and 5760. Therefore, even if an opponent happened to choose an identical game strategy, the probability of a false positive was at least 1 in 960"

> "As intended, no players lost other than times when it was designed to lose against another colluding player."

> "only six Semi-Rabbits were entered by other participants and 28 Chicken/Roosters were entered by our group, so we won the competition with a safe margin of 30 points."

**ID:** connect4-competition-result
**Location:** Section 1, p. 356; Section 4.4 "Implementation", pp. 364–365; Section 4.7 "Results", p. 366
**Grep command used:** `Grep pattern="write a program to play|ranged between 960 and 5760|safe margin of 30 points" path="literature/extracted/murdoch_2004.txt"`

---

## Claim 11: Concealment from inspection — the winning programs carried no detection code; the loser bears the signal

> "one domain specific optimisation was to remove all detection code from the Foxes."

> "Additionally no evidence of collusion can then be found by inspecting the source code of the Foxes."

**ID:** no-evidence-in-winner
**Location:** Section 4.5 "Optimisation", p. 365
**Grep command used:** `Grep pattern="remove all detection code|no evidence of collusion can then be found" path="literature/extracted/murdoch_2004.txt"`

---

## Claim 12: Defences — collusion-resistant tournament design (STV-like elimination) and detection by experts looking for players who are exceptionally unlucky

> "In order to prevent collusion, the competition could be designed such that collusion provides no advantage."

> "an expert suspecting collusion would look for players being exceptionally unlucky. The expert could also monitor the games in progress looking for an suspicious changes in apparent skill."

> "We also introduce a covert channel built using only redundancy in the moves of a game and show how this can be used to authenticate colluding players."

**ID:** defences-design-and-detection
**Location:** Section 5.1 "Collusion Resistant Competitions", p. 367; Section 5.2 "Detecting Collusion", p. 368; Section 6 "Conclusion", p. 368
**Grep command used:** `Grep pattern="collusion provides no advantage|exceptionally unlucky|redundancy in the moves of a game" path="literature/extracted/murdoch_2004.txt"`

---

## Claim 13: Approach — the equivalent-move covert channel: a keyed generator picks which of the outcome-equivalent moves to play, borrowing frequency hopping from low-probability-of-intercept radio, so colluders authenticate one another through the moves alone

> "Techniques designed for low-probability-of-intercept spread spectrum radio and multilevel secure systems are also applied in developing covert channels suitable for use in games."

> "We also introduce a covert channel built using only redundancy in the moves of a game and show how this can be used to authenticate colluding players."

> "For each move, the number sent is chosen according to a keyed generator. The receiver shares the key and so knows what move to expect from a colluding player."

**ID:** approach-equivalent-move-channel
**Location:** Abstract, p. 355; Section 3.3 "Analysis of Authentication Mechanisms", p. 361; Section 6 "Conclusion", p. 368
**Grep command used:** `Grep pattern="low-probability-of-intercept spread spectrum|built using only redundancy|number sent is chosen according to a keyed" path="literature/extracted/murdoch_2004.txt"`

---

## Claim 14: Approach — the league collusion strategy: once authenticated, colluders act on that knowledge so that one designated player wins, which guarantees victory when only one team colludes and the players are strong

> "In this paper we explore how, in a tournament, a player may surreptitiously authenticate players who may be colluded with, what actions can be taken and what advantage this may gain him."

> "We present a simple algorithm for acting on the basis of authentication information which will guarantee winning a competition, assuming only one team is using a collusion strategy and the standard of players is good."

**ID:** approach-league-collusion-strategy
**Location:** Section 1 "Introduction", p. 355; Section 6 "Conclusion", p. 368
**Grep command used:** `Grep pattern="surreptitiously authenticate players|simple algorithm for acting on the basis" path="literature/extracted/murdoch_2004.txt"`
