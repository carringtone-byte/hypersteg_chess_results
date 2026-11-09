---
paper: "Anderson and Petitcolas (1998)"
title: "On the Limits of Steganography"
doi: "<DOI>"
pmcid: "<PMC ID, if any>"
url: "IEEE Journal on Selected Areas in Communications 16(4):474–481, May 1998; Publisher Item Identifier S 0733-8716(98)01112-3"
source_version: "published"
file: "literature/anderson_1998.pdf"
retrieved: "20261105"
verified_by: "Claude (Opus 5.5) subagent, quotes checked with verify_quotes.py (read-only run)"
# The six below are written by `verify_quotes.py --stamp` — do not hand-edit.
# They bind the ledger to the exact source/extract bytes AND its own quoted text
# (body_sha256) it was verified against, so a later quote edit is caught in CI.
source_sha256: "c140304a24ec752da73e65e10c6410d6ac4aa83fb521d42d3dd429519362c648"
extract_sha256: "53b3d7e7ef172c92499b447022c50d5c0f9b9bf078502d3a24fca019119fadcc"
body_sha256: "e40b6069609a7b09209fadbf871eb3cd01d6e5919ee9c5ba2fbb77539b1e99bd"
verifier_version: "2"
verified_verdict: "pass"
verified_date: "20261106"
extract_source_sha256: "c140304a24ec752da73e65e10c6410d6ac4aa83fb521d42d3dd429519362c648"
---

# Verified Claims — Anderson and Petitcolas (1998)

Each claim below was extracted by reading the downloaded paper file with the Read
tool, grepping for the specific content, and reading the surrounding context to
confirm the attribution is faithful.

Source: IEEE Journal on Selected Areas in Communications, vol. 16, no. 4, May 1998, pp. 474–481
(publisher PDF from IEEE Xplore). Authors: Ross J. Anderson and Fabien A. P. Petitcolas, Computer
Laboratory, University of Cambridge. The DOI is not printed in the extracted text, so the DOI
field is left unset; the publisher item identifier printed on page 474 is given in `url`.

## Claim 1: Threat model — Simmons' Prisoners' Problem with the warden Willie; Kerckhoffs: security rests only on a shared key

> "all their communications pass through the warden, Willie, and if Willie detects any encrypted messages, he will frustrate their plan by throwing them into solitary confinement."

> "we assume that the mechanism in use is known to the warden, and so the security must depend solely on a secret key that Alice and Bob have somehow managed to share."

**ID:** prisoners-kerckhoffs-shared-key
**Location:** Section I "Introduction", p. 474
**Grep command used:** `Grep pattern="pass through the warden, Willie|depend solely on a secret key" path="literature/extracted/anderson_1998.txt"`

---

## Claim 2: Historical precedent — a code ideogram at a prearranged place in a dispatch; grille systems

> "Kahn tells of a classical Chinese practice of embedding a code ideogram at a prearranged place in a dispatch; the same idea arose in medieval Europe with grille systems"

**ID:** prearranged-place-grille
**Location:** Section I "Introduction", p. 474
**Grep command used:** `Grep pattern="embedding a code ideogram" path="literature/extracted/anderson_1998.txt"`

---

## Claim 3: General model — transform the covertext, then tweak a key-selected subset of now-redundant bits

> "Alice embeds information by first applying a transform to the covertext, and then tweaking a subset of the bits of the transformed object that are now redundant."

> "can have their values altered without being detected easily or at all by an opponent who does not know which subset to examine."

**ID:** general-model-transform-redundancy
**Location:** Section III-C "A General Model", p. 477
**Grep command used:** `Grep pattern="first applying a transform to the covertext|does not know which subset to" path="literature/extracted/anderson_1998.txt"`

---

## Claim 4: Covertext model dependence — a warden who models the redundancy better removes the channel; no theory comparable to Shannon's

> "the warden may be willing to do even more work, and the apparent redundancy that we exploit will fall within his ability to model."

> "what makes the case of steganography more difficult than secrecy or authenticity is that we are critically dependent on our model of the covertext."

> "Yet we still have no comparable theory of steganography."

**ID:** covertext-model-dependence
**Location:** Section III-C, p. 477; Section IV "Theoretical Limits", p. 477
**Grep command used:** `Grep pattern="fall within his ability to model|critically dependent on our model|no comparable theory of steganography" path="literature/extracted/anderson_1998.txt"`

---

## Claim 5: Perfect compression — practical steganography is an issue only where compression is inefficient

> "Thus Alice could take an arbitrary ciphertext message that she wants to hide and run it through the decompressor."

> "tells us that practical steganography is only an issue where compression is inefficient. Where efficient compression is available, information hiding will usually be either trivial or impossible, depending on the context."

**ID:** perfect-compression-argument
**Location:** Section IV-A "What If Perfect Compression Existed?", pp. 477–478
**Grep command used:** `Grep pattern="run it through the decompressor|only an issue where" path="literature/extracted/anderson_1998.txt"`

---

## Claim 6: Capacity under observation — more stegotext lets the warden estimate the cover better, so the safe rate may tend to zero

> "But the more stegotext we give the warden, the better he may be able to estimate the statistics of the underlying covertext, and so the smaller the rate at which Alice will be able to tweak bits safely. The rate might even tend to zero"

**ID:** rate-may-tend-to-zero
**Location:** Section IV-B "Entropy", p. 478
**Grep command used:** `Grep pattern="the more stegotext we give the warden" path="literature/extracted/anderson_1998.txt"`

---

## Claim 7: Selection channel — the shared pad that chooses which cover bits carry the message; the book cipher as a shared-codebook example

> "when Alice and Bob use a shared one-time pad to decide which covertext bit will be marked with the next ciphertext bit, we can think of the pad as a selection channel."

> "The sender and receiver share a book and encipher a message as a series of pointers to words."

> "A repetitive book will have a lower capacity, as we will be able to use a smaller percentage of its words before correlation attacks from the context become possible."

**ID:** selection-channel-book-cipher
**Location:** Section IV-C "Selection Channel", p. 478
**Grep command used:** `Grep pattern="think of the pad as a selection|share a book and encipher|repetitive book will have a lower" path="literature/extracted/anderson_1998.txt"`

---

## Claim 8: Parity embedding — embed each bit as the parity of a key-selected set, changing whichever element is least obtrusive

> "We use our one-time pad (or keystream generator) to select not one pixel, but a set of them, and embed the ciphertext bit as their parity. This way, the information can be hidden by changing whichever of the pixels can be changed least obtrusively."

**ID:** parity-embedding
**Location:** Section IV-D "The Power of Parity", p. 478
**Grep command used:** `Grep pattern="embed the ciphertext bit as their parity" path="literature/extracted/anderson_1998.txt"`

---

## Claim 9: Text carrier — a keyed hash of each sentence yields one bit; the "Stego Turing Test" for undetectable natural-language alteration

> "Suppose Alice uses a keyed cryptographic hash function to derive one bit from each sentence of a document."

> "This alarm will go off about every other sentence, which she can then rewrite."

> "It is even an open question whether a computer can alter a natural language text in a way that is undetectable to a human"

> "the problem is commended to the research community as the “Stego Turing Test.”"

**ID:** sentence-hash-stego-turing-test
**Location:** Section IV-E "Equivalence Classes", p. 479
**Grep command used:** `Grep pattern="keyed cryptographic hash function to derive|go off about every other sentence|alter a natural language|Stego Turing Test" path="literature/extracted/anderson_1998.txt"`

---

## Claim 10: Equivalence classes — capacity bounded by the gap between lossy and lossless compression, an upper bound rather than a safety bound

> "Again, we get a bound on the stego channel capacity: it is the difference between lossy and lossless compression. Once more though, this is an upper bound rather than a safety bound, and is not much help against a powerful opponent."

**ID:** equivalence-class-capacity-bound
**Location:** Section IV-E "Equivalence Classes", p. 479
**Grep command used:** `Grep pattern="difference between lossy and lossless" path="literature/extracted/anderson_1998.txt"`

---

## Claim 11: Robustness — passive versus active wardens; an active warden with as good a model can replace the redundancy with noise

> "There is a critical distinction between passive wardens, who monitor traffic and signal to some process outside the system if unauthorized traffic is detected, and active wardens, who try to remove all possible covert messages from traffic that passes through their hands."

> "if an active warden’s model of the communication is as good as the communicating parties’ model, and the covertext information separates cleanly from the usable redundancy, then he can replace the latter with noise."

> "all Willie will be able to do is to cut the bandwidth of the channel by adding his own random marks"

**ID:** active-passive-wardens
**Location:** Section V "Active and Passive Wardens", pp. 479–480
**Grep command used:** `Grep pattern="critical distinction between passive wardens|as good as the communicating parties|cut the bandwidth of the channel" path="literature/extracted/anderson_1998.txt"`

---

## Claim 12: Pre-coordination — public-key steganography removes the need for a pre-shared secret, even with an active warden under a modified model

> "it was generally assumed that, in the presence of a capable motivated opponent, steganography required the pre-existence of a shared secret, so that the two communicating parties could decide which bits to tweak."

> "Now suppose that Alice and Bob did not have the opportunity to agree on a secret key before they were imprisoned, but that Bob has a public key that is known to Alice."

> "Each possible recipient will then simply try to decrypt every message he sees, and Bob alone will be successful."

> "we have shown that public key steganography may sometimes be possible in the presence of an active warden."

**ID:** public-key-steganography
**Location:** Section VI "Public Key Steganography", p. 480; Section VII "Conclusion", p. 481
**Grep command used:** `Grep pattern="pre-existence of a shared secret|did not have the opportu|Bob alone will be successful|sometimes be possible in the presence" path="literature/extracted/anderson_1998.txt"`

---

## Claim 13: Approach (contribution) — a survey of what steganography can and cannot do, the obstacles to a Shannon-style theory, and the practical ideas that theory yields

> "In this paper, we clarify what steganography is and what it can do."

> "This leads to a discussion of the formidable obstacles that lie in the way of a general theory of information hiding systems (in the sense that Shannon gave us a general theory of secrecy systems). However, theoretical considerations lead to ideas of practical value, such as the use of parity checks to amplify covertness and provide public key steganography."

> "We have explored the limits of steganographic theory and practice."

**ID:** approach-limits-of-steganography
**Location:** Abstract, p. 474; Section VII "Conclusion", p. 480
**Grep command used:** `Grep pattern="clarify what steganography is|formidable obstacles that lie|explored the limits of steganographic" path="literature/extracted/anderson_1998.txt"`

---

## Claim 14: Approach — parity embedding: the selection channel argument leads to hiding each bit in the parity of a key-selected set of cover bits rather than in the data directly

> "the “selection channel”—the bandwidth of the stego key—led us to suggest embedding information in parity checks rather than in the data directly. This approach gives improved efficiency, and also allows us to do public key steganography."

> "We use our one-time pad (or keystream generator) to select not one pixel, but a set of them, and embed the ciphertext bit as their parity."

> "When the warden is active, the more covertext bits we use in each parity check, the more easily he will be able to inject noise into our stegotext."

**ID:** approach-parity-embedding
**Location:** Section VII "Conclusion", p. 480; Section IV-D "The Power of Parity", p. 478; Section V "Active and Passive Wardens", p. 480
**Grep command used:** `Grep pattern="embedding information in parity checks|embed the ciphertext bit as their parity|more covertext bits we use in each parity" path="literature/extracted/anderson_1998.txt"`

---

## Claim 15: Approach — public-key steganography: encrypt under the recipient's public key and embed as block parities; every recipient tries to decrypt, and against an active warden a one-time key permutes the cover bits

> "She can take her covert message, encrypt it under his public key, and embed it as the parity of successive blocks."

> "In practice, the value encrypted under a public key could be a control block consisting of a session key plus some padding, and the session key would drive a conventional steganographic scheme."

> "our construction of public key steganography shows that they can also communicate covertly (if this is at all possible for people who already share a secret)."

> "We will now indicate how concealed public key communication may still be possible in the presence of an active warden provided that the model of the Prisoners’ Problem is changed slightly."

> "Alice can choose a short one-time key that selects some permutation of the covertext bits, and she hides a message as the parity of successive"

**ID:** approach-public-key-steganography
**Location:** Section VI-A "With a Passive Warden" and VI-B "With an Active Warden", p. 480 (the active-warden quote stops before a block length that the extract drops)
**Grep command used:** `Grep pattern="encrypt it under his public key|control block consisting of a|can also communicate covertly|changed slightly|short one-time key that selects" path="literature/extracted/anderson_1998.txt"`

---

## Claim 16: Builds on — Simmons' Prisoners' Problem is taken as the founding formulation of the subject

> "The study of this subject in the scientific literature may be traced to Simmons, who in 1983 formulated it as the “Prisoners’ Problem” [43]."

> "Simmons’ formulation of the Prisoners’ Problem was itself an instance of information hiding."

**ID:** builds-on-simmons-prisoners
**Location:** Section I "Introduction", p. 474 (reference [43] is G. J. Simmons, "The prisoners' problem and the subliminal channel")
**Grep command used:** `Grep pattern="may be traced to Simmons|formulation of the Prisoners" path="literature/extracted/anderson_1998.txt"`

**Depends-on:** simmons_1984:approach-subliminal-channel (grounded by #builds-on-simmons-prisoners)
