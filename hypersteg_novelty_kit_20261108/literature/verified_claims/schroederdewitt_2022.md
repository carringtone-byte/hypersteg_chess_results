---
paper: "Schroeder de Witt et al. (2022)"
title: "Perfectly Secure Steganography Using Minimum Entropy Coupling"
doi: "10.48550/arXiv.2210.14889"
pmcid: "<PMC ID, if any>"
url: "<source URL the file was fetched from>"
source_version: "preprint"
file: "literature/schroederdewitt_2022.html"
retrieved: "20261105"
verified_by: "Claude (Opus 5.5) subagent, quotes checked with verify_quotes.py (read-only run)"
# The six below are written by `verify_quotes.py --stamp` — do not hand-edit.
# They bind the ledger to the exact source/extract bytes AND its own quoted text
# (body_sha256) it was verified against, so a later quote edit is caught in CI.
source_sha256: "e73d988f1874ede09973835b9de79b6b13a865463fcd9c9f4ac12715c6bd775e"
extract_sha256: "9cef6693d9a90935b0fcd0a3d8616d4fbd46e18091708174ac2ec60947037aaf"
body_sha256: "a3a4583f79275a3feb4387d53f41aa6609e27b41d6a6ccb32a2b1606df24306e"
verifier_version: "2"
verified_verdict: "pass"
verified_date: "20261106"
extract_source_sha256: "e73d988f1874ede09973835b9de79b6b13a865463fcd9c9f4ac12715c6bd775e"
---

# Verified Claims — Schroeder de Witt et al. (2022)

Each claim below was extracted by reading the downloaded paper file with the Read
tool, grepping for the specific content, and reading the surrounding context to
confirm the attribution is faithful.

Source: arXiv:2210.14889v4 [cs.CR], 30 Oct 2023 (arXiv HTML rendering). Authors:
Christian Schroeder de Witt, Samuel Sokota, J. Zico Kolter, Jakob Foerster, Martin
Strohmeier. The key's year is that of first arXiv posting; the file is the fourth version.

## Claim 1: Security result — perfect security is equivalent to being induced by a coupling

> "A steganographic encoding procedure is perfectly secure if and only if it is induced by a coupling."

**ID:** perfect-security-iff-coupling
**Location:** Section 3 "Steganography and Minimum Entropy Coupling", Theorem 1
**Grep command used:** `Grep pattern="perfectly secure if and only if it is induced by a coupling" path="literature/extracted/schroederdewitt_2022.txt"`

---

## Claim 2: Capacity result — among perfectly secure procedures, maximal throughput is equivalent to a minimum entropy coupling

> "among perfectly secure procedures, a procedure maximizes information throughput if and only if it is induced by a minimum entropy coupling."

**ID:** max-throughput-iff-mec
**Location:** Abstract (Theorem 2 in Section 3)
**Grep command used:** `Grep pattern="maximizes information throughput if and only if" path="literature/extracted/schroederdewitt_2022.txt"`

---

## Claim 3: Security notion — Cachin's KL divergence between covertext and stegotext; perfect security is zero divergence

> "Security is defined in terms of the KL divergence between the distribution of covertext and the distribution of stegotext."

> "A procedure is said to be perfectly secure if it guarantees a divergence of zero."

**ID:** cachin-kl-notion
**Location:** Section 1 "Introduction"
**Grep command used:** `Grep pattern="Security is defined in terms of the KL|guarantees a divergence of zero" path="literature/extracted/schroederdewitt_2022.txt"`

---

## Claim 4: Coding — iMEC (iterative minimum entropy coupling) couples uniform ciphertext with an autoregressive covertext distribution

> "so long as one of the distributions is uniform and the other can be specified autoregressively."

> "iMEC can be leveraged to perform steganography with arbitrary covertext distributions and plaintext messages."

**ID:** imec-coding
**Location:** Section 4 "A Minimum Entropy Coupling-Based Approach to Steganography"; Section 1 "Introduction"
**Grep command used:** `Grep pattern="specified autoregressively\.|iMEC can be leveraged" path="literature/extracted/schroederdewitt_2022.txt"`

---

## Claim 5: Key and access — shared private key; covertext distribution known to all parties; decoder reproduces the posterior

> "This private key is shared between the sender and receiver over a secure channel prior to the start of the stegoprocess and can be used to coordinate encryption and decryption."

> "is assumed to be known by the sender, the receiver, and the adversary."

> "decoding simply reproduces this posterior and selects the maximum a posteriori."

**ID:** key-and-known-distribution
**Location:** Section 2.1 "An Information-Theoretic Model for Steganography"; Section 4
**Grep command used:** `Grep pattern="shared between the sender and receiver over a secure channel|known by the sender, the receiver, and the adversary|selects the maximum a posteriori" path="literature/extracted/schroederdewitt_2022.txt"`

---

## Claim 6: Carriers — text (GPT-2), audio (WaveRNN) and images (Image Transformer)

> "we evaluate iMEC using GPT-2  ( Radford et al., 2019 )  (a language model), WaveRNN  ( Kalchbrenner et al., 2018 )  (an audio model), and Image Transfomer (an image model) as covertext distributions."

**ID:** carriers-text-audio-image
**Location:** Section 1 "Introduction"
**Grep command used:** `Grep pattern="we evaluate iMEC using GPT-2" path="literature/extracted/schroederdewitt_2022.txt"`

---

## Claim 7: Detection result — iMEC's KL at numerical precision; arithmetic coding and ADG many orders of magnitude above

> "iMEC’s KL divergence is upper bounded by numerical precision in every setting."

> "arithmetic coding and ADG possess divergences that are consistently many orders of magnitude above the precision of the data type."

**ID:** kl-results
**Location:** Section 5.2 "Results", "Covertext Divergence"
**Grep command used:** `Grep pattern="upper bounded by numerical precision|many orders of magnitude above the precision" path="literature/extracted/schroederdewitt_2022.txt"`

---

## Claim 8: Capacity — encoding efficiency (bit rate normalised by covertext entropy) superior to the baselines at 20-bit blocks

> "We say encoding efficiency to mean the bit rate normalized to the mean covertext entropy per token."

> "Surprisingly, despite its perfect security constraints, iMEC with a block size of 20 bits yields superior encoding efficiency to the baselines across all three of our realistic distributions."

**ID:** encoding-efficiency
**Location:** Section 5.2 "Results", "Encoding Efficiency"
**Grep command used:** `Grep pattern="We say encoding efficiency|block size of 20 bits yields superior" path="literature/extracted/schroederdewitt_2022.txt"`

---

## Claim 9: Robustness and access limits — passive adversary, unperturbed stegotext, white-box access to the covertext distribution

> "assumes that the adversary is passive and that the stegotext arrives to the receiver unperturbed."

> "assumes that white box access to the covertext distribution is available."

**ID:** passive-whitebox-limits
**Location:** Section 7 "Conclusion and Future Work"
**Grep command used:** `Grep pattern="adversary is passive and that the stegotext|white box access to the covertext distribution is available" path="literature/extracted/schroederdewitt_2022.txt"`

---

## Claim 10: Builds on and supersedes — Sokota et al.'s iMEC; prior Huffman and arithmetic-coding methods are not perfectly secure

> "recently introduced an iterative minimum entropy coupling approach, which we call iMEC"

> "Existing algorithms in this class are based on Huffman coding  ( Dai & Cai, 2019 )  and arithmetic coding  ( Ziegler et al., 2019 ;  Kaptchuk et al., 2021 ;  Chen et al., 2022 ) ."

> "they are not perfectly secure unless the covertext distribution is compressed exactly into the ciphertext distribution, which is not generally the case."

**ID:** builds-on-imec-supersedes-coding
**Location:** Section 1 "Introduction"; Section 6 "Related Work"
**Grep command used:** `Grep pattern="which we call iMEC|Existing algorithms in this class|compressed exactly into the ciphertext" path="literature/extracted/schroederdewitt_2022.txt"`

---

## Claim 11: Approach — minimum entropy coupling steganography (iMEC): encode by coupling uniform-looking ciphertext with the covertext distribution, which makes the procedure perfectly secure and maximally efficient under Cachin's model

> "In this work, we show that a steganography procedure is perfectly secure under  Cachin (1998) ’s information-theoretic model of steganography if and only if it is induced by a coupling."

> "These insights yield what are, to the best of our knowledge, the first steganography algorithms to achieve perfect security guarantees for arbitrary covertext distributions."

> "We show that, because ciphertext can be made to look uniformly random, and any distribution of covertext can be specified autoregressively, iMEC can be leveraged to perform steganography with arbitrary covertext distributions and plaintext messages."

**ID:** approach-imec
**Location:** Abstract; Section 1 "Introduction"
**Grep command used:** `Grep pattern="perfectly secure under  Cachin|first steganography algorithms to achieve perfect|iMEC can be leveraged to perform" path="literature/extracted/schroederdewitt_2022.txt"`

**Depends-on:** cachin_1998:approach-information-theoretic-model (grounded by #approach-imec)
**Supersedes:** ziegler_2019:approach-arithmetic-coding (grounded by #builds-on-imec-supersedes-coding)
**Supersedes:** kaptchuk_2021:approach-meteor (grounded by #builds-on-imec-supersedes-coding)
**Supersedes:** dai_2019:approach-patient-huffman (grounded by #builds-on-imec-supersedes-coding)
**Supersedes:** zhang_2021:approach-adg (grounded by #adg-not-perfectly-secure)

---

## Claim 12: Lineage — ADG (Zhang et al. 2021) is nearly but not perfectly secure, and the experiments confirm it for arithmetic coding, Meteor and ADG alike

> "Outside of coding-based methods,  Zhang et al. (2021)  describe another method that they call ADG, which, similarly to coding based approaches, possesses nearly perfect—but not perfect—security guarantees."

> "Our experiments confirm the lack of perfect security guarantees for these methods—indeed, we observed that arithmetic coding  ( Ziegler et al., 2019 ) , Meteor  ( Kaptchuk et al., 2021 ) , and ADG  ( Zhang et al., 2021 )  incurred KL divergences many orders of magnitude greater than the level of numerical precision we used."

**ID:** adg-not-perfectly-secure
**Location:** Section 6 "Related Work"
**Grep command used:** `Grep pattern="describe another method that they call ADG|Our experiments confirm the lack of perfect security" path="literature/extracted/schroederdewitt_2022.txt"`
