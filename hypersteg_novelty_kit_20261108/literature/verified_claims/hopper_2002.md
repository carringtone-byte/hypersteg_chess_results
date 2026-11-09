---
paper: "Hopper et al. (2002)"
title: "Provably Secure Steganography"
doi: "<DOI>"
pmcid: "<PMC ID, if any>"
url: "CMU technical report CMU-CS-02-149, School of Computer Science, Carnegie Mellon University"
source_version: "preprint"
file: "literature/hopper_2002.pdf"
retrieved: "20261105"
verified_by: "Claude (Opus 5.5) subagent, quotes checked with verify_quotes.py (read-only run)"
# The six below are written by `verify_quotes.py --stamp` — do not hand-edit.
# They bind the ledger to the exact source/extract bytes AND its own quoted text
# (body_sha256) it was verified against, so a later quote edit is caught in CI.
source_sha256: "c1fabf983241d3c9860fe6f890734e1122a106b2d81ac9a4eefc95f4f7c974f6"
extract_sha256: "158a5d74fdb2a0d5af4fba4516b7f23c4c0e5e1471254cb8d1f4040cc1494998"
body_sha256: "c30da398cec58b744d22e71a1ef0a6321cf16701721878c57208d7bd9b407165"
verifier_version: "2"
verified_verdict: "pass"
verified_date: "20261106"
extract_source_sha256: "c1fabf983241d3c9860fe6f890734e1122a106b2d81ac9a4eefc95f4f7c974f6"
---

# Verified Claims — Hopper et al. (2002)

Each claim below was extracted by reading the downloaded paper file with the Read
tool, grepping for the specific content, and reading the surrounding context to
confirm the attribution is faithful.

Source: **the Carnegie Mellon technical report CMU-CS-02-149, dated 6 September 2002**, not the
CRYPTO 2002 proceedings version (LNCS 2442, pp. 77–92). The report is the longer version;
section numbers, construction numbers and wording below are the report's and may differ from
the CRYPTO paper. Cite it as the technical report. Authors: Nicholas J. Hopper, John Langford
and Luis von Ahn. The DOI field is left unset because the report has none; the locator is the
report number in `url`.

## Claim 1: Security notion — steganographic secrecy as computational indistinguishability; one-way functions suffice

> "We introduce definitions based on computational indistinguishability and we prove that the existence of one-way functions implies the existence of secure steganographic protocols."

> "Thus the existence of secure steganography is equivalent to the existence of one-way functions."

**ID:** computational-indistinguishability-owf
**Location:** Abstract; Section 5.3 "Complexity theoretic ramifications"
**Grep command used:** `Grep pattern="computational indistinguishability and we prove|equivalent to the" path="literature/extracted/hopper_2002.txt"`

---

## Claim 2: Threat model — Simmons' prisoners on a public channel monitored by the warden Ward; the goal is hiding existence, not content

> "The only way they can communicate with each other is through a public channel, which is carefully monitored by the warden of the prison, Ward."

> "steganography is about hiding the very existence of the secret messages."

**ID:** prisoners-ward-hide-existence
**Location:** Section 1 "Introduction"
**Grep command used:** `Grep pattern="carefully monitored by the warden|hiding the very existence" path="literature/extracted/hopper_2002.txt"`

---

## Claim 3: Channel — a distribution on timestamped bit sequences, general enough to include timing-only channels

> "A channel is a distribution on bit sequences where each bit is also timestamped with monotonically increasing time value."

> "it may be possible to do steganography over email using only the timing of the emails rather than the contents of the message."

**ID:** timestamped-channel
**Location:** Section 2.3 "Steganography", Definition of a channel
**Grep command used:** `Grep pattern="distribution on bit sequences where each bit|using only the timing of the" path="literature/extracted/hopper_2002.txt"`

---

## Claim 4: Channel access — the stegosystem only samples the channel through an oracle; it need not know the distribution

> "we assume that a stegosystem has very little knowledge of the channel distribution—SE andSD may only sample from an oracle according to the distribution."

> "for example, the oracle may be a human being, or a video camera focused on some complex scene."

**ID:** sampling-oracle-only
**Location:** Section 2.3, Comment after the rejection-sampling procedure
**Grep command used:** `Grep pattern="very little knowledge of the channel|oracle may be a human being" path="literature/extracted/hopper_2002.txt"`

---

## Claim 5: Weak point — security holds only for a perfect oracle; a human cannot make independent draws, and a warden would exploit that

> "In practice, this oracle is also the weakest point of all our constructions."

> "If the oracle is a human, the human may not be able to perform independent draws from the channel as is required by the function RS. A real world Warden would use this to his advantage."

**ID:** perfect-oracle-assumption
**Location:** Section 2.3
**Grep command used:** `Grep pattern="weakest point of all our constructions|human may not be able to perform independent" path="literature/extracted/hopper_2002.txt"`

---

## Claim 6: Channel condition — a minimum-entropy constraint on every block

> "We will require that the channel satisfy a minimum entropy constraint for all blocks"

> "Construction 1 gives a stegosystem which is steganographically secret for any channel distribution C which has minimum entropy greater than 1, assuming the existence of a pseudorandom function family."

**ID:** min-entropy-constraint
**Location:** Section 2.3; Section 5.3
**Grep command used:** `Grep pattern="minimum entropy constraint for all blocks|minimum entropy greater than 1" path="literature/extracted/hopper_2002.txt"`

---

## Claim 7: Construction — rejection sampling: draw channel blocks until a keyed pseudorandom function of the block equals the next message bit

> "The function RS simply samples from the distribution provided by the sample oracle M until F(M) = x."

> "Then it draws blocks from the channel at most twice, trying to find a blockc1 such thatFK(N,c 1) =m1."

**ID:** rejection-sampling-prf
**Location:** Section 2.3 (Procedure RS); Section 3.1, Construction 1
**Grep command used:** `Grep pattern="RS simply samples from the distribution|draws blocks from the channel at most twice" path="literature/extracted/hopper_2002.txt"`

---

## Claim 8: What is shared — a secret key and a synchronised counter; history-dependent encoding

> "Let Alice and Bob share a secret key K∈{ 0, 1}k and a synchronized d bit counter N."

> "Note that the encoding procedure actually has some probability of failure per bit."

**ID:** shared-key-synchronised-counter
**Location:** Section 3.1 "Construction: Stateful Universal Steganographic Secrecy"
**Grep command used:** `Grep pattern="synchronized d bit counter|probability of failure per bit" path="literature/extracted/hopper_2002.txt"`

---

## Claim 9: Not new as protocols — the constructions follow earlier proposals; the novelty is the proof

> "This protocol is not new and can be found (up to small differences) in [1], for instance. The novel aspect is the proof of steganographic secrecy within our model."

**ID:** protocol-not-new-proof-is
**Location:** Section 3.1
**Grep command used:** `Grep pattern="This protocol is not new and" path="literature/extracted/hopper_2002.txt"`

---

## Claim 10: Robustness — an active warden bounded by a relation; without a bound he can destroy any hidden information

> "It will be important to state the limitations we impose on Ward, since otherwise he can replace all messages with a new draw from the channel distribution, effectively destroying any hidden information."

> "For several reasons, this stegosystem appears impractical but it serves as a proof that robust steganography is possible for any admissible relation."

**ID:** robustness-bounded-active-warden
**Location:** Section 4.1 "Definitions for Robust Steganography"; Section 4.2 "Universally Robust Stegosystem"
**Grep command used:** `Grep pattern="limitations we impose on Ward|appears impractical but it serves" path="literature/extracted/hopper_2002.txt"`

---

## Claim 11: Text channels — robustness against wardens who make small edits, measured by shingle overlap

> "it seems reasonable to suppose that a predominantly text-based channel might limit the power of an active warden by such a relation."

**ID:** text-channel-shingling
**Location:** Section 4.3 "Robust Steganography for text-like channels"
**Grep command used:** `Grep pattern="predominantly text-based channel" path="literature/extracted/hopper_2002.txt"`

---

## Claim 12: Capacity — expected rate of the constructions is one hidden bit per channel block

> "We can define the rate of a stegosystem S as the number of bits of plaintext divided by the number of bits in the covertexts. Ignoring the probability of failure and the use of error correcting codes, the expected rate of our constructions is 1/b."

**ID:** rate-one-over-b
**Location:** Section 5.1 "Rate and Efficiency"
**Grep command used:** `Grep pattern="expected rate of our constructions" path="literature/extracted/hopper_2002.txt"`

---

## Claim 13: Approach (contribution) — complexity-theoretic steganography: secrecy and robustness defined by computational indistinguishability, with secure protocols built from one-way functions; positioned against Simmons' problem and the information-theoretic models

> "The main goal of this paper is to put steganography on a solid complexity-theoretic foundation."

> "Our main result is a positive one: secret and robust steganographic protocols exist within our model, given that one-way functions exist."

> "The scientific study of steganography began in 1983 when Simmons [17] stated the problem in terms of communication in a prison."

> "A few papers have given information theoretic models for steganography [3, 13, 15, 19], but these are limited in the same way that information theoretic cryptography is limited."

**ID:** approach-complexity-theoretic-steganography
**Location:** Section 1 "Introduction" and "Related Work" (reference [17] is G. J. Simmons, "The Prisoner's Problem and the Subliminal Channel"; [3] is C. Cachin, "An Information-Theoretic Model for Steganography", Information Hiding 1998 preproceedings)
**Grep command used:** `Grep pattern="solid complexity-theoretic foundation|main result is a positive one|began in 1983 when Simmons|information theoretic models for steganography" path="literature/extracted/hopper_2002.txt"`

**Depends-on:** simmons_1984:approach-subliminal-channel (grounded by #approach-complexity-theoretic-steganography)
**Qualifies:** cachin_1998:approach-information-theoretic-model (grounded by #approach-complexity-theoretic-steganography)

---

## Claim 14: Approach — Construction 1, stateful rejection sampling: for each encoded bit, draw up to two channel blocks until a keyed PRF of block and counter equals the bit; taken from Anderson and Petitcolas

> "We now show a stateful protocol which is universally steganographically secret. This protocol is not new and can be found (up to small differences) in [1], for instance."

> "First, the encoding algorithm splits m = Enc(m′) into single bits. Then it draws blocks from the channel at most twice, trying to find a blockc1 such thatFK(N,c 1) =m1."

> "The decoding algorithm simply applies"

**ID:** approach-stateful-rejection-sampling
**Location:** Section 3.1 "Construction: Stateful Universal Steganographic Secrecy", Construction 1 (reference [1] is R. J. Anderson and F. A. P. Petitcolas, "On The Limits of Steganography")
**Grep command used:** `Grep pattern="We now show a stateful protocol|splits m = Enc|decoding algorithm simply applies" path="literature/extracted/hopper_2002.txt"`

**Restates:** anderson_1998:approach-limits-of-steganography (grounded by #approach-stateful-rejection-sampling)

---

## Claim 15: Approach — Construction 2, stateless: encrypt with an IND$-CPA cipher, then rejection-sample each block until a public function unbiased on the channel yields the next ciphertext bit; Cachin gave an information-theoretic version

> "The following protocol also satisfies our definition for steganographic secrecy. Once again, this protocol (up to small differences) is not new and can be found in [1]; an information theoretic version of the protocol can also be found in [3]."

> "be a public function which is unbiased on C. Note that the assumption that there exists an f satisfying this definition does not hold for all channels."

> "Clearly, the assumption of an unbiased f is quite strong."

**ID:** approach-stateless-unbiased-function
**Location:** Section 3.2 "Stateless Steganographic Secrecy", Construction 2
**Grep command used:** `Grep pattern="information theoretic version of the protocol|public function which is unbiased|assumption of an unbiased" path="literature/extracted/hopper_2002.txt"`

**Restates:** anderson_1998:approach-limits-of-steganography (grounded by #approach-stateless-unbiased-function)
**Restates:** cachin_1998:approach-balanced-partition (grounded by #approach-stateless-unbiased-function)

---

## Claim 16: Approach — Construction 3, universally robust: channel draws from shared pseudorandom inputs stand in for two shared secret blocks, each bit repeated n times, robust against any bounded warden but impractical

> "Then Alice could send Bob the message bit"

> "Intuitively, Construction 3 simply extends this notion to multiple bits by replacing the"

> "by draws from M(·) with shared pseudorandom inputs; and reduces the probability of decoding error to"

> "For several reasons, this stegosystem appears impractical but it serves as a proof that robust steganography is possible for any admissible relation."

**ID:** approach-universally-robust
**Location:** Section 4.2 "Universally Robust Stegosystem", Construction 3 (symbols for the two blocks and the error bound are lost in extraction; the quotes stop around them)
**Grep command used:** `Grep pattern="could send Bob the message bit|simply extends this notion|shared pseudorandom inputs|appears impractical but" path="literature/extracted/hopper_2002.txt"`

---

## Claim 17: Approach — Construction 4, robust protocol for text-like channels: a keyed PRF picks the maximising n-shingle of each document and an unbiased function of it carries the bit, surviving edits that preserve shingle overlap

> "We provide a protocol which is steganographically robust against"

> "for a particular class of admissible relations R on particular channels."

> "Define the function max f(d) as the shingle in d which maximizes f"

> "Note that it is important that encryption and bit errors commute here which holds for only some encryption techniques."

**ID:** approach-robust-text-shingling
**Location:** Section 4.3 "Robust Steganography for text-like channels", Construction 4
**Grep command used:** `Grep pattern="steganographically robust against|particular class of admissible|shingle in d which maximizes|encryption and bit errors commute" path="literature/extracted/hopper_2002.txt"`
