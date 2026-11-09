---
paper: "Cachin (1998)"
title: "An Information-Theoretic Model for Steganography"
doi: "<DOI>"
pmcid: "<PMC ID, if any>"
url: "Information Hiding, Second International Workshop, IH'98, ed. D. Aucsmith, LNCS 1525, Springer, 1998, pp. 306–318 (PDF pages 316–328 of literature/_books/lncs1525_information_hiding_1998.pdf)"
source_version: "published"
file: "literature/cachin_1998.pdf"
retrieved: "20261106"
verified_by: "Claude (Opus 5.5) subagent, quotes checked with verify_quotes.py (read-only run)"
# The six below are written by `verify_quotes.py --stamp` — do not hand-edit.
# They bind the ledger to the exact source/extract bytes AND its own quoted text
# (body_sha256) it was verified against, so a later quote edit is caught in CI.
source_sha256: "6b9287031cd3b3196dc4e1012224cd006dd2dfdae4e257871f9ee192e4cfb2ba"
extract_sha256: "91740f681bdb9c66b421d41707e28ab015c7949e52a4501bf5aa02abb1125aa6"
body_sha256: "6d2e4561e253b06f5921b4cfbbd348710d7d96ec3e532ae1f039509f271b421e"
verifier_version: "2"
verified_verdict: "pass"
verified_date: "20261106"
extract_source_sha256: "6b9287031cd3b3196dc4e1012224cd006dd2dfdae4e257871f9ee192e4cfb2ba"
---

# Verified Claims — Cachin (1998)

Each claim below was extracted by reading the extracted text of the paper with the Read
tool, grepping for the specific content, and reading the surrounding context to
confirm the attribution is faithful.

Source: David Aucsmith (ed.), Information Hiding 1998, LNCS 1525, pp. 306–318, Springer-Verlag
Berlin Heidelberg 1998 (publisher pages, cut from the proceedings volume). Single author:
Christian Cachin, MIT Laboratory for Computer Science. The DOI is not printed in the extract.
Mathematical symbols (epsilon, alpha, beta, Delta) are partly garbled in extraction; the quotes
below avoid them. Page numbers are the printed proceedings pages.

How this workshop version differs from the 2004 journal version (`literature/verified_claims/cachin_2004.md`):
- Affiliation is MIT LCS here; IBM Zurich in 2004.
- The universal stegosystem here is a modification of Willems' repetition-times compression
  algorithm that swaps a low-probability block for its neighbour in the repetition-time ranking;
  2004 instead uses universal compression to approximate the covertext distribution and embeds
  with a one-time pad.
- No capacity theorem: the 1998 paper states that asymptotic security holds and defers the formal
  statement to "the full version"; the 2004 bound of an l-bit message with l at most n H(X) is
  absent.
- Absent here: the Bible-verse codebook example and the NP-hardness of optimal embedding.
- Present here, as model extensions: covertext conditioned on external information Y (news,
  weather), and Simmons' authentication key Z.
- Both versions treat a passive adversary and define security by relative entropy D(PC||PS).

## Claim 1: Threat model — Simmons' Prisoners' Problem with a passive warden who observes all communication

> "Steganography with a passive adversary is perhaps best illustrated by Simmons’ “Prisoners’ Problem” [19]. Alice and Bob are in jail and wish to devise an escape plan."

> "All their communication is observed by the adversary (the warden), who will thwart their plan by transferring them to a high-security prison as soon as he detects any sign of a hidden message."

**ID:** prisoners-problem-passive
**Location:** p. 306, Section 1 "Introduction"
**Grep command used:** `/usr/bin/grep -n "best illustrated by Sim\|high-security prison" literature/extracted/cachin_1998.txt`

---

## Claim 2: Scope — passive adversary only; active-adversary hiding (watermarking, fingerprinting) is a different problem

> "Hiding information from active adversaries is a different problem since the existence of a hidden message is publicly known, such as in copyright protection schemes."

> "In this paper, we introduce an information-theoretic model for steganography with a passive adversary."

**ID:** passive-adversary-only
**Location:** pp. 306–307, Section 1 "Introduction"
**Grep command used:** `/usr/bin/grep -n "existence of a hidden message is publicly\|model for steganogra" literature/extracted/cachin_1998.txt`

---

## Claim 3: Security notion — detection is a hypothesis test; security is the relative entropy between covertext and stegotext distributions

> "The adversary’s task of distinguishing between an innocent cover message C and a modified message S containing a secret part is interpreted as a hypothesis testing problem."

> "A stegosystem as defined above with covertext C and stegotext S is called"

> "If the covertext and stegotext distributions are equal and"

> "the stegosystem is perfectly secure and the adversary can have no advantage over merely guessing without even observing a message."

**ID:** relative-entropy-security
**Location:** Abstract; p. 307, Section 1; p. 311, Definition 1
**Grep command used:** `/usr/bin/grep -n "interpreted as a hypothesis testing\|is called\|no advantage" literature/extracted/cachin_1998.txt`

---

## Claim 4: Bound on the warden — the error probabilities of any detection rule are bounded by the security parameter

> "Lemma 1 imposes a bound on the achievable error probabilities by Eve."

> "probability that the adversary does not detect a hidden message and the probability that the adversary falsely detects a hidden message satisfy"

> "thus, Eve can obtain no information about whether Alice is active by observing the message."

**ID:** detection-bound-theorem1
**Location:** p. 312, Theorem 1 and the sentence introducing it
**Grep command used:** `/usr/bin/grep -n "imposes a bound on the achievable\|adversary does not detect a hidden\|Eve can obtain no information" literature/extracted/cachin_1998.txt`

---

## Claim 5: What is shared — a secret key shared by Alice and Bob; Eve knows everything else (Kerckhoffs)

> "it is assumed that the adversary Eve has complete information about the system except for a secret key shared by Alice and Bob that guarantees the security."

> "The probability distributions are assumed to be known to all parties if not stated otherwise. In addition, Bob knows whether Alice is active or not."

**ID:** shared-secret-key-kerckhoffs
**Location:** p. 307, Section 1; p. 310, Section 3
**Grep command used:** `/usr/bin/grep -n "complete information about the system\|known to all parties" literature/extracted/cachin_1998.txt`

---

## Claim 6: Channel — Eve observes the public channel; Alice either transforms a covertext or generates it herself; all messages count as one

> "If Alice is active, she transforms C to contain an embedded message E using a secret key K. (Alternatively, Alice could also generate C herself.)"

> "Repetition is not considered in this model; it encompasses everything sent from Alice to Bob."

> "The model of a secret-key stegosystem with passive adversary. It shows the embedded text E, the covertext C, the stegotext S, Alice’s private random source R, and the secret key K shared by Alice and Bob."

**ID:** public-channel-model
**Location:** p. 310, Section 3; p. 311, Fig. 1
**Grep command used:** `/usr/bin/grep -n "she transforms C\|Repetition is not considered\|secret-key stegosystem with passive" literature/extracted/cachin_1998.txt`

---

## Claim 7: External information — events such as news or weather may shape the covertext, and security is then conditioned on them

> "It may be the case that external events influence the covertext distribution; for example, news reports or the local weather if we think of the prisoners’ problem."

**ID:** external-information-conditioning
**Location:** p. 312, Section 3
**Grep command used:** `/usr/bin/grep -n "external events in" literature/extracted/cachin_1998.txt`

---

## Claim 8: Known-distribution schemes — the one-time pad is perfectly secure for uniform covertext; a balanced partition embeds one bit for any distribution

> "Thus, the one-time pad provides perfect steganographic security if the covertext is uniformly random."

> "Alice constructs the embedding function from a partition of C into two parts such that both parts are assigned approximately the same probability mass under C."

**ID:** known-distribution-schemes
**Location:** p. 313, Section 4 "Unconditionally Secure Stegosystems", Theorem 2
**Grep command used:** `/usr/bin/grep -n "perfect steganographic security\|constructs the embedding function" literature/extracted/cachin_1998.txt`

---

## Claim 9: Compression — deterministic post-processing cannot reduce security

> "To put it another way, data compression can never hurt the security of a stegosystem and make detection easier for the adversary."

**ID:** compression-cannot-hurt
**Location:** p. 314, Section 4
**Grep command used:** `/usr/bin/grep -n "can never hurt the security" literature/extracted/cachin_1998.txt`

---

## Claim 10: Universal stegosystem and capacity — Willems' repetition-times algorithm modified to swap low-probability blocks; asymptotic security claimed, formal statement deferred

> "Then we modify the algorithm to illustrate that a stegosystem can be constructed without knowledge of the covertext distribution."

> "the source statistics are only slightly altered. Information is only hidden in blocks with low probability"

> "The resulting stegosystem achieves asymptotically perfect security since the distance between the probabilities of the exchanged blocks vanishes. The formal statement of this will be given in the full version of the paper."

**ID:** universal-repetition-times
**Location:** pp. 315–316, Section 5 "Steganography with Universal Data Compression"
**Grep command used:** `/usr/bin/grep -n "constructed without knowledge of the covertext\|only hidden in blocks\|asymptotically perfect security" literature/extracted/cachin_1998.txt`

---

## Claim 11: Limitation — the model's validity depends on an accurate covertext model; a warden will not pass random-looking messages

> "But no warden would allow the prisoners to exchange random-looking messages! Thus, the crucial issue for the validity of a formal treatment of steganography is the accuracy of the model for real data."

> "the assumption of a fixed covertext distribution seems to render our model somewhat unrealistic for the practical purposes of steganography."

**ID:** covertext-model-limitation
**Location:** p. 307, Section 1; p. 317, Section 6 "Extensions"
**Grep command used:** `/usr/bin/grep -n "no warden would allow\|fixed covertext" literature/extracted/cachin_1998.txt`

---

## Claim 12: Simmons' authentication — part of the shared key may authenticate messages against a malicious warden, and Eve must detect against the marginal covertext distribution

> "Simmons’ original scenario of the prisoners’ problem includes authentication, that is, the secret key K shared by Alice and Bob can partially be used for authenticating Alice’s messages."

> "since the adversary Eve does not know Z, the covertext distribution to consider for detection is"

**ID:** authentication-extension
**Location:** p. 316, Section 6 "Extensions"
**Grep command used:** `/usr/bin/grep -n "original scenario of the prisoners\|does not know Z" literature/extracted/cachin_1998.txt`

---

## Claim 13: Approach (contribution) — an information-theoretic model of steganography against a passive adversary, with security measured as relative entropy between cover and stego distributions

> "An information-theoretic model for steganography with passive adversaries is proposed."

> "In this paper, we introduce an information-theoretic model for steganography with a passive adversary. We propose a security notion that is based on hypothesis testing"

> "If the covertext and stegotext distributions are equal and"

> "the stegosystem is perfectly secure and the adversary can have no advantage over merely guessing without even observing a message."

**ID:** approach-information-theoretic-model
**Location:** Abstract, p. 306; Section 1 "Introduction", p. 307 (the third and fourth quotes are split around the relative-entropy expression, which the extract garbles)
**Grep command used:** `/usr/bin/grep -n "model for steganography with pas\|introduce an information-theoretic model\|distributions are equal and\|no advantage" literature/extracted/cachin_1998.txt`

**Depends-on:** simmons_1984:approach-subliminal-channel (grounded by #prisoners-problem-passive)

---

## Claim 14: Approach — the balanced-partition stegosystem: split the covertext alphabet into two parts of near-equal probability and let a one-bit shared key choose which part carries each message bit

> "Alice constructs the embedding function from a partition of C into two parts such that both parts are assigned approximately the same probability mass under C."

> "Bob can decode the message because he knows that"

> "Thus, the one-time pad provides perfect steganographic security if the covertext is uniformly random."

**ID:** approach-balanced-partition
**Location:** p. 313, Section 4 "Unconditionally Secure Stegosystems" (before Theorem 2); the decoding condition after "knows that" is garbled in the extract and not quoted
**Grep command used:** `/usr/bin/grep -n "constructs the embedding function\|can decode the message because\|perfect steganographic security" literature/extracted/cachin_1998.txt`

---

## Claim 15: Approach — the universal stegosystem: Willems' repetition-times compressor, modified to swap a low-probability block for its neighbour in the repetition-time ranking, so no covertext statistics are needed

> "one of them is a universal information hiding scheme based on universal data compression techniques that requires no knowledge of the covertext statistics."

> "The stegosystem based on Willems’ algorithm exploits the fact that the average repetition time of a block"

> "the source statistics are only slightly altered. Information is only hidden in blocks with low probability"

> "is either equal to y or to the block immediately following"

> "in the average repetition time ranking, depending on the embedded bit."

**ID:** approach-universal-repetition-times
**Location:** Abstract, p. 306; Section 5 "Steganography with Universal Data Compression", pp. 315–316 (reference [22] is F. M. Willems, "Universal data compression and repetition times", which has no ledger)
**Grep command used:** `/usr/bin/grep -n "universal informa\|based on Willems\|only slightly altered\|block immediately following\|depending on the embedded bit" literature/extracted/cachin_1998.txt`
