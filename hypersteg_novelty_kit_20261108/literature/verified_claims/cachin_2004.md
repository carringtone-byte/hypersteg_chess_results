---
paper: "Cachin (2004)"
title: "An information-theoretic model for steganography"
doi: "10.1016/j.ic.2004.02.003"
pmcid: "<PMC ID, if any>"
url: "<source URL the file was fetched from>"
source_version: "published"
file: "literature/cachin_2004.pdf"
retrieved: "20261105"
verified_by: "Claude (Opus 5.5) subagent, quotes checked with verify_quotes.py (read-only run)"
# The six below are written by `verify_quotes.py --stamp` — do not hand-edit.
# They bind the ledger to the exact source/extract bytes AND its own quoted text
# (body_sha256) it was verified against, so a later quote edit is caught in CI.
source_sha256: "7b9bd3b9d430b65807cf45ff6199cd09cbfc99a40e48af14f6ab386e15e0fadc"
extract_sha256: "ba4da09f8e96090bdc51f730563401abf27ff24bed04c2df768cec6beea9c80e"
body_sha256: "829ac424d71e98c7ef8233506230d82bb95cc427f4207505d83c5a0af30c6df4"
verifier_version: "2"
verified_verdict: "pass"
verified_date: "20261106"
extract_source_sha256: "7b9bd3b9d430b65807cf45ff6199cd09cbfc99a40e48af14f6ab386e15e0fadc"
---

# Verified Claims — Cachin (2004)

Each claim below was extracted by reading the downloaded paper file with the Read
tool, grepping for the specific content, and reading the surrounding context to
confirm the attribution is faithful.

Source: Information and Computation 192 (2004) 41–56 (Elsevier publisher PDF). Single author:
Christian Cachin, IBM Zurich Research Laboratory. A preliminary version appeared at the Second
Information Hiding Workshop, 1998 (LNCS 1525). Mathematical symbols (epsilon, alpha, beta) were
lost in text extraction; the quotes below avoid them.

## Claim 1: Threat model — Simmons' Prisoners' Problem: a passive warden reads every message and thwarts any sign of conspiracy

> "is perhaps best illustrated by Simmons’ “Prisoners’ Problem” [1]: Alice and Bob are in jail, locked up in separate cells far apart from each other, and wish to devise an escape plan."

> "The couriers are agents of the warden Eve (the adversary) and will leak all communication to her. If Eve detects any sign of conspiracy, she will thwart the escape plans"

> "Alice and Bob succeed if they can exchange information allowing them to coordinate their escape and Eve does not become suspicious."

**ID:** prisoners-problem
**Location:** Section 1 "Introduction"
**Grep command used:** `Grep pattern="Prisoners’ Problem|agents of the warden Eve|coordinate their escape" path="literature/extracted/cachin_2004.txt"`

---

## Claim 2: Security notion — detection is a hypothesis test; security is the relative entropy between covertext and stegotext distributions

> "The adversary’s task of distinguishing between an innocent cover message C and a modified message S containing hidden information is interpreted as a hypothesis testing problem."

> "We define the security of a steganographic system in terms of the relative entropy (or discrimination) between the distributions of the covertext and the stegotext. A stegosystem is called perfect if this relative entropy is zero."

**ID:** relative-entropy-security
**Location:** Abstract; Section 1 "Introduction"
**Grep command used:** `Grep pattern="interpreted as a hypothesis testing problem|called perfect if this relative entropy" path="literature/extracted/cachin_2004.txt"`

---

## Claim 3: Bound on the warden — the binary relative entropy of the two error rates is at most the security parameter

> "that the adversary does not detect the presence of the embedded message and the probability"

> "In a perfectly secure system, we have D(PC∥PS) = 0 and therefore PC =PS ; thus, the observed message does not give Eve any information about whether Alice is active or not."

> "Because deciding betweenH0 andH1 is a special form of processing by abinary function, the type I and type II error probabilities"

**ID:** detection-bound-theorem1
**Location:** Section 3.1 "Hypothesis testing"; Section 3.2, Theorem 1
**Grep command used:** `Grep pattern="adversary does not detect the presence|In a perfectly secure system|special form of processing by" path="literature/extracted/cachin_2004.txt"`

---

## Claim 4: What is shared — a secret key chosen at random and exchanged over a secure channel before use

> "Alice’s embedding algorithm may access a private random source R and a secret keyK, which is shared by Alice and Bob."

> "The key has been chosen at random and communicated over a secure channel prior to the use of the stegosystem – in any case before the message E that Alice wants to communicate to Bob becomes known."

**ID:** shared-secret-key-precoordinated
**Location:** Section 2.2 "Stegosystems"
**Grep command used:** `Grep pattern="shared by Alice and Bob|communicated over a secure" path="literature/extracted/cachin_2004.txt"`

---

## Claim 5: Kerckhoffs — the warden knows the embedding function and all distributions; only the key is secret

> "The embedding function F and the distributions of all random variables are known to Eve. Hence, the model respects the prudent tradition known as “Kerckhoffs’ principle” in cryptology"

**ID:** kerckhoffs
**Location:** Section 2.2 "Stegosystems"
**Grep command used:** `Grep pattern="known to Eve. Hence, the model respects" path="literature/extracted/cachin_2004.txt"`

---

## Claim 6: Channel — a public channel to which the warden has perfect read-only access; the covertext is generated, not modified

> "Alice wishes to send an innocent-looking message with a hidden meaning over a public channel to Bob, such that the presence of hidden information goes unnoticed by a third party, the adversary Eve, who has perfect read-only access to the public channel."

> "Our model differs from the scenario sometimes considered for steganography, where Alice uses a covertext that is known to Eve and modifies it for embedding hidden information."

**ID:** public-channel-read-only
**Location:** Section 2.2 "Stegosystems"; Remark 3
**Grep command used:** `Grep pattern="perfect read-only access|Our model differs from the scenario" path="literature/extracted/cachin_2004.txt"`

---

## Claim 7: Shared-codebook example — a reference to a uniformly likely Bible verse, shifted by a shared key, is perfectly secure

> "suppose Alice and Bob both have a copy of the Bible in their cells. The adversary allows them to make a reference to any verse of the Bible in a message."

> "Since we assume the distribution of a verse reference to be uniform, covertext and stegotext distributions are equal."

**ID:** bible-verse-codebook
**Location:** Section 4.1, Example 1
**Grep command used:** `Grep pattern="copy of the Bible|distribution of a verse reference" path="literature/extracted/cachin_2004.txt"`

---

## Claim 8: Hardness — finding the optimal embedding for a known covertext distribution is NP-hard

> "In general, determining the optimal embedding function from a covertext distribution is an NP-hard combinatorial optimization problem."

**ID:** optimal-embedding-np-hard
**Location:** Section 4.2 "General distributions"
**Grep command used:** `Grep pattern="NP-hard combinatorial optimization" path="literature/extracted/cachin_2004.txt"`

---

## Claim 9: Universal stegosystem — no knowledge of the covertext distribution needed, only i.i.d. repetitions; built on universal compression and a one-time pad

> "A universal stegosystem is presented in this model that needs no knowledge of the covertext distribution, except that it is generated from independently repeated experiments."

> "Alice applies a universal data compression scheme to compute an approximation of the covertext distribution. She then produces stegotext with the approximate distribution of the covertext from her own randomness and embeds a message into the stegotext using the method of the one-time pad."

**ID:** universal-stegosystem
**Location:** Abstract; Section 5 "Universal stegosystems"
**Grep command used:** `Grep pattern="needs no knowledge of the covertext|universal data compression scheme to compute" path="literature/extracted/cachin_2004.txt"`

---

## Claim 10: Capacity — the universal system hides a message up to n times the covertext entropy, secure on average for large n

> "secure on average against passive adversaries and hides an ℓ-bit message withℓ⩽nH(X) , forn sufficiently large."

> "Eve may have complete knowledge of the covertext distribution, but as long as she is restricted to observe only a finite part of the covertext sequence, this stegosystem achieves perfect average security asymptotically."

**ID:** capacity-entropy-bound
**Location:** Section 5 "Universal stegosystems" (introduction); Section 5.3, Theorem 4
**Grep command used:** `Grep pattern="secure on average against passive adversaries and hides|restricted to observe only a" path="literature/extracted/cachin_2004.txt"`

---

## Claim 11: Limitation — the model rests on a probabilistic model of the covertext shared by users and warden

> "depends crucially on the assumption that there is a probabilistic model of the covertext."

> "A secure stegosystem requires that the users and the adversary share the same probabilistic model of the covertext."

> "But no reasonable warden would allow the prisoners to exchange randomly looking messages in the Prisoners’ Problem!"

**ID:** shared-covertext-model-limitation
**Location:** Section 6.1 "Limitations"
**Grep command used:** `Grep pattern="probabilistic model of the covertext|no reasonable warden" path="literature/extracted/cachin_2004.txt"`

---

## Claim 12: Robustness scope — passive adversary only; active-adversary watermarking is a different problem

> "This paper considers steganography with a passive adversary."

> "more general problem of hiding information with active adversaries in watermarking and fingerprinting applications. This is different from steganography because the existence of a hidden message is known publicly."

**ID:** passive-adversary-only
**Location:** Section 1 "Introduction"; Section 6.2 "Related work"
**Grep command used:** `Grep pattern="considers steganography with a passive|existence of a hidden message is" path="literature/extracted/cachin_2004.txt"`

---

## Claim 13: Journal version of the 1998 workshop paper

> "A preliminary version of this work was presented at the Second Workshop on Information Hiding, Portland, USA, 1998, and appears in the proceedings (D. Aucsmith (Ed.), Lecture Notes in Computer Science, vol. 1525, Springer)."

**ID:** preliminary-version-1998
**Location:** Title footnote, p. 41
**Grep command used:** `Grep pattern="preliminary version of this work" path="literature/extracted/cachin_2004.txt"`

---

## Claim 14: Approach (contribution) — an information-theoretic model of steganography against a passive adversary; detection is hypothesis testing and a stegosystem is perfect when cover and stego distributions have zero relative entropy

> "An information-theoretic model for steganography with a passive adversary is proposed."

> "Following the approach of information theory, we capture this knowledge by a probabilistic model, and view Eve’s task of detecting hidden messages as a problem of hypothesis testing."

> "A stegosystem is called perfect if this relative entropy is zero."

**ID:** approach-information-theoretic-model
**Location:** Abstract, p. 41; Section 1 "Introduction", p. 42
**Grep command used:** `Grep pattern="model for steganography with a passive adversary is proposed|view Eve’s task of detecting|called perfect if this relative entropy" path="literature/extracted/cachin_2004.txt"`

**Supersedes:** cachin_1998:approach-information-theoretic-model (grounded by #preliminary-version-1998)
**Depends-on:** simmons_1984:approach-subliminal-channel (grounded by #prisoners-problem)

---

## Claim 15: Approach — perfectly secure stegosystems for uniform covertext: a key-shifted Bible-verse reference, and the one-time pad on uniformly random bits

> "We assume in this section that the covertext distribution is known to the users Alice and Bob, and describe two basic stegosystems."

> "All verses are considered to occur equally likely in a conversation among prisoners and there is a publicly known way to associate codewords with Bible verses."

> "Likewise, the one-time pad is a perfectly secure stegosystem whenever the covertext consists of uniformly random bits. Assuming such a covertext would be rather unrealistic, but we describe it here briefly in order to illustrate the model."

**ID:** approach-uniform-cover-schemes
**Location:** Section 4 "Secure stegosystems" and 4.1 "Uniform covertext distributions", p. 48
**Grep command used:** `Grep pattern="describe two basic stegosystems|publicly known way to associate|perfectly secure stegosystem whenever" path="literature/extracted/cachin_2004.txt"`

---

## Claim 16: Approach — the balanced-partition stegosystem for arbitrary known distributions: a one-bit key chooses which of two near-equiprobable halves of the covertext space carries the bit

> "We now describe a system that embeds a one-bit message for arbitrary covertext distributions."

> "Given a covertext C, Alice constructs the embedding function from a binary partition of the covertext space"

> "Bob can decode the message because he knows that"

> "Note that the embedding provides perfect secrecy for E."

**ID:** approach-balanced-partition
**Location:** Section 4.2 "General distributions", Example 3, p. 49
**Grep command used:** `Grep pattern="embeds a one-bit message for arbitrary|constructs the embedding function from a binary partition|perfect secrecy for E" path="literature/extracted/cachin_2004.txt"`

**Restates:** cachin_1998:approach-balanced-partition (grounded by #preliminary-version-1998)

---

## Claim 17: Approach — the universal stegosystem: approximate the covertext distribution by universal compression, then generate stegotext from private randomness with the message one-time-padded into the encoder output

> "In this section, we describe a method for obtaining a universal stegosystem where such knowledge is not needed. It works for a covertext signal that is produced by a sequence of independent repetitions of the same experiment."

> "it works by estimating the distribution and then simulating a covertext by sampling a stegotext with a similar distribution."

> "Note that this stegosystem relies on Alice’s private random source in a crucial way."

**ID:** approach-universal-stegosystem
**Location:** Section 1 "Introduction", p. 42; Section 5 "Universal stegosystems", p. 50; Section 5.3 "A universal stegosystem", p. 52
**Grep command used:** `Grep pattern="method for obtaining a universal stegosystem|simulating a covertext by|private random source in a crucial way" path="literature/extracted/cachin_2004.txt"`
