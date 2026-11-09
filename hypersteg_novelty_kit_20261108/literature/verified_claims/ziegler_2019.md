---
paper: "Ziegler, Deng and Rush (2019)"
title: "Neural Linguistic Steganography"
doi: "10.48550/arXiv.1909.01496"
pmcid: "<PMC ID, if any>"
url: "<source URL the file was fetched from>"
source_version: "preprint"
file: "literature/ziegler_2019.html"
retrieved: "20261105"
verified_by: "Claude (Opus 5.5) subagent, quotes checked with verify_quotes.py (read-only run)"
# The six below are written by `verify_quotes.py --stamp` — do not hand-edit.
# They bind the ledger to the exact source/extract bytes AND its own quoted text
# (body_sha256) it was verified against, so a later quote edit is caught in CI.
source_sha256: "4f4e4312ab3f164241fc7a5954af07572b606af06987d53eb88c62a0a5df72d3"
extract_sha256: "7ccf10b657a66512a1dac8ca82c944a6469edc0782dc7f5fc3fe214ebaaa3e37"
body_sha256: "ad3a056415b17099eaec1dc08c4525ab12b3f5b9fd6d218a055bd819398f0646"
verifier_version: "2"
verified_verdict: "pass"
verified_date: "20261106"
extract_source_sha256: "4f4e4312ab3f164241fc7a5954af07572b606af06987d53eb88c62a0a5df72d3"
---

# Verified Claims — Ziegler, Deng and Rush (2019)

Each claim below was extracted by reading the downloaded paper file with the Read
tool, grepping for the specific content, and reading the surrounding context to
confirm the attribution is faithful.

Source: arXiv:1909.01496v1 [cs.CL], 3 Sep 2019 (arXiv HTML rendering). The
reference lists of Schroeder de Witt et al. and Ding et al. cite the EMNLP-IJCNLP 2019
version of the same paper.

## Claim 1: Coding — generative linguistic steganography by arithmetic coding over a large neural language model

> "We propose a steganography technique based on arithmetic coding with large-scale neural language models."

**ID:** arithmetic-coding-neural-lm
**Location:** Abstract
**Grep command used:** `Grep pattern="based on arithmetic coding with large-scale" path="literature/extracted/ziegler_2019.txt"`

---

## Claim 2: Carrier — generated text, as opposed to edits of human-chosen cover text

> "In edit-based methods, such as synonym substitution, the content of the cover text is selected by a human and slightly modified to encode information"

> "In generative methods an entire block of text is generated while encoding the message reversibly in the choice of tokens."

**ID:** generative-vs-edit-carrier
**Location:** Section 1 "Introduction"
**Grep command used:** `Grep pattern="In edit-based methods|In generative methods an entire block" path="literature/extracted/ziegler_2019.txt"`

---

## Claim 3: Key and shared model — the mapping and the exact same language model form the key; both sides use a predetermined context

> "Alice and Bob have both agreed on an invertible mapping"

> "Alice and Bob also both have access to the exact same language model"

> "Alice encodes bits into cover text via arithmetic coding with a predetermined context."

**ID:** key-is-shared-lm
**Location:** Section 2 "Linguistic steganography"; Section 4.4 "Qualitative results", step 2
**Grep command used:** `Grep pattern="agreed on an invertible mapping|exact same language model|with a predetermined context" path="literature/extracted/ziegler_2019.txt"`

---

## Claim 4: Security notion and capacity — security is a small KL divergence; capacity is the entropy of the induced distribution

> "From an information theoretic perspective the security objective of steganography is therefore to ensure a small"

> "the average number of bits that can be encoded is given by the entropy"

**ID:** kl-security-entropy-capacity
**Location:** Section 2 "Linguistic steganography"
**Grep command used:** `Grep pattern="security objective of steganography|average number of bits that can be encoded" path="literature/extracted/ziegler_2019.txt"`

---

## Claim 5: Coding — arithmetic coding run in reverse, over the conditional distributions of a pretrained language model (access to the full token distribution)

> "Arithmetic coding traditionally maps a string of elements to a uniformly distributed binary string. To use such a coding for steganography we reverse the order: first a (uniformly sampled) message is selected, then the message is mapped to a sequence (words)."

> "In this work the probability distribution comes from the conditional distributions of a pretrained language model"

**ID:** reverse-arithmetic-coding
**Location:** Section 3 "Arithmetic coding"
**Grep command used:** `Grep pattern="we reverse the order|comes from the conditional distributions" path="literature/extracted/ziegler_2019.txt"`

---

## Claim 6: Builds on — Sallee (2004): arithmetic coding is optimal for steganography as for compression

> "show that just as arithmetic coding is optimal for data compression, it is also optimal for steganography."

**ID:** builds-on-sallee-2004
**Location:** Section 3 "Arithmetic coding"
**Grep command used:** `Grep pattern="it is also optimal for steganography" path="literature/extracted/ziegler_2019.txt"`

---

## Claim 7: Quality–security trade-off — temperature and top-k truncation, which introduce a small distributional mismatch

> "we introduce two parameters to trade off quality for compression: we modulate the LM distribution by a temperature"

> "comes from the slight distributional difference when the long tail is truncated."

**ID:** temperature-topk-tradeoff
**Location:** Section 3 "Arithmetic coding"; Section 4.3 "Quantitative results"
**Grep command used:** `Grep pattern="trade off quality for compression|long tail is truncated" path="literature/extracted/ziegler_2019.txt"`

---

## Claim 8: Supersedes — Block (Fang et al. 2017) and Huffman (Yang et al. 2019) target human eavesdroppers and are open to machine detection

> "The issue with these approaches is that they aim to fool human eavesdroppers for whom generation quality is most important; but are susceptible to machine-based eavesdroppers which can in principle identify statistical patterns in generations."

**ID:** supersedes-block-huffman
**Location:** Section 2 "Generative coding techniques"
**Grep command used:** `Grep pattern="susceptible to machine-based eavesdroppers" path="literature/extracted/ziegler_2019.txt"`

---

## Claim 9: Detection result (statistical) — lowest KL among methods; near-zero KL with the unmodulated model

> "arithmetic coding achieves the lowest KL, i.e. the distribution of the encoded texts is the most similar to the language model distribution"

> "distribution with a KL of 4e-8 nats."

**ID:** kl-results-gpt2
**Location:** Section 4.3 "Quantitative results"
**Grep command used:** `Grep pattern="achieves the lowest KL|KL of 4e-8 nats" path="literature/extracted/ziegler_2019.txt"`

---

## Claim 10: Detection result (human) and capacity — humans fooled at 1 bit/word; minimum KL near 4 bits/word

> "at 1 bit/word both methods lead to cover texts statistically indistinguishable from human-written sentences"

> "whereas the arithmetic approach reaches minimum KL around 4 bits/word with"

> "do the generations fool humans."

**ID:** human-eval-capacity
**Location:** Section 4.3 "Quantitative results"
**Grep command used:** `Grep pattern="at 1 bit/word both methods|minimum KL around 4 bits/word|do the generations fool humans" path="literature/extracted/ziegler_2019.txt"`

---

## Claim 11: Approach — arithmetic-coding steganography over a large neural language model: a uniform message is decoded into tokens so that the cover text follows the model's distribution

> "Advances in neural language models enable previously impractical generation-based techniques. We propose a steganography technique based on arithmetic coding with large-scale neural language models. We find that our approach can generate realistic looking cover sentences as evaluated by humans, while at the same time preserving security by matching the cover message distribution with the language model distribution."

> "To use such a coding for steganography we reverse the order: first a (uniformly sampled) message is selected, then the message is mapped to a sequence (words)."

**ID:** approach-arithmetic-coding
**Location:** Abstract; Section 3 "Arithmetic coding"
**Grep command used:** `Grep pattern="enable previously impractical generation-based|we reverse the order: first a" path="literature/extracted/ziegler_2019.txt"`
