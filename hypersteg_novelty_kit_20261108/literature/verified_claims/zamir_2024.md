---
paper: "Zamir (2024)"
title: "Excuse me, sir? Your language model is leaking (information)"
doi: "10.48550/arXiv.2401.10360"
pmcid: "<PMC ID, if any>"
url: "<source URL the file was fetched from>"
source_version: "preprint"
file: "literature/zamir_2024.html"
retrieved: "20261105"
verified_by: "Claude (Opus 5.5) subagent, quotes checked with verify_quotes.py (read-only run)"
# The six below are written by `verify_quotes.py --stamp` — do not hand-edit.
# They bind the ledger to the exact source/extract bytes AND its own quoted text
# (body_sha256) it was verified against, so a later quote edit is caught in CI.
source_sha256: "085bf00419374f38e90942468c77ea13d3eb4dfe33d8c8d8b9f97122a317cc6c"
extract_sha256: "f9b0a475456a19c7c686eb017be64305347b1e39cc71e00d634af8948c03d50a"
body_sha256: "2378c960d04322bcf74d797c0751d0e970fadae69486243d60d6378c76166949"
verifier_version: "2"
verified_verdict: "pass"
verified_date: "20261106"
extract_source_sha256: "085bf00419374f38e90942468c77ea13d3eb4dfe33d8c8d8b9f97122a317cc6c"
---

# Verified Claims — Zamir (2024)

Each claim below was extracted by reading the downloaded paper file with the Read
tool, grepping for the specific content, and reading the surrounding context to
confirm the attribution is faithful.

Source: arXiv:2401.10360v1 [cs.CR], 18 Jan 2024 (arXiv HTML rendering). Single author: Or
Zamir, Tel Aviv University.

## Claim 1: Carrier and goal — an arbitrary secret payload hidden in an LLM's response; extraction needs a secret key

> "We introduce a cryptographic method to hide an arbitrary secret payload in the response of a Large Language Model (LLM). A secret key is required to extract the payload from the model’s response"

**ID:** payload-in-llm-response
**Location:** Abstract
**Grep command used:** `Grep pattern="hide an arbitrary secret payload" path="literature/extracted/zamir_2024.txt"`

---

## Claim 2: Security notion — computational undetectability, even under many adaptive queries

> "without the key it is provably impossible to distinguish between the responses of the original LLM and the LLM that hides a payload."

> "are indistinguishable even to a user allowed to make many adaptive queries."

**ID:** undetectable-adaptive-queries
**Location:** Abstract; Section 2.4 "Steganography for LLMs"
**Grep command used:** `Grep pattern="provably impossible to distinguish|many adaptive queries\." path="literature/extracted/zamir_2024.txt"`

---

## Claim 3: Builds on — the Christ–Gunn–Zamir (CGZ) undetectable watermark, which correlates the sampling randomness with the key

> "Our approach extends a recent result of Christ, Gunn and Zamir (2023) who introduced an undetectable watermarking scheme for LLMs."

> "planting a watermark not by changing the model’s distribution, but by correlating the randomness used by the model with the secret key."

**ID:** builds-on-cgz
**Location:** Abstract; Section 3 "Overview of the CGZ Watermark"
**Grep command used:** `Grep pattern="extends a recent result of Christ|correlating the randomness used by the model" path="literature/extracted/zamir_2024.txt"`

---

## Claim 4: Coding — a dynamic error-correcting code with feedback; chunk boundaries set by the detection score itself

> "The main technical tool we use to transform the CGZ scheme from watermarking to embedding a message, is incorporating a dynamic variant of Error Correcting Codes with feedback."

> "We solve this problem by implicitly defining the partition to chunks using the detection score itself"

**ID:** dynamic-ecc-feedback
**Location:** Section 1 "Introduction"; Section 4 "High-Level Overview of Our Scheme"
**Grep command used:** `Grep pattern="dynamic variant of Error Correcting Codes|partition to chunks using the detection score" path="literature/extracted/zamir_2024.txt"`

---

## Claim 5: Access — the channel distribution is unknown to the decoder; retrieval uses the key and the response, not the prompt or model

> "The unique property of our setting, though, is that in the case of LLM responses the distribution of the channel is unknown."

> "In particular, the process of decoding the message must be agnostic to the distribution of responses."

> "depends on the key and on the response but not on the prompt, the model, or the distributions"

**ID:** decoder-distribution-agnostic
**Location:** Section 1 "Introduction"; Section 3 "Overview of the CGZ Watermark"
**Grep command used:** `Grep pattern="distribution of the channel is unknown|agnostic to the distribution of responses|not on the prompt, the model" path="literature/extracted/zamir_2024.txt"`

---

## Claim 6: Threat model — the LLM itself (or whoever controls its sampling) can covertly leak metadata or internal information

> "This implies, for example, that an LLM may secretly hide session-metadata (such as the user’s name, the time, or the prompt used) in the response it gives."

> "It also means that even an LLM running off-line may use the responses it gives to covertly leak internal information to those who will later be exposed to the seemingly-clean LLM responses."

**ID:** llm-covert-leak
**Location:** Section 1 "Introduction"
**Grep command used:** `Grep pattern="may secretly hide session-metadata|covertly leak internal information" path="literature/extracted/zamir_2024.txt"`

---

## Claim 7: Capacity — linear in response length (asymptotically optimal), but only for high-entropy responses

> "the amount of hidden bits our scheme can encode in an LLM output is linear in the length of the response, which is asymptotically optimal."

> "outputs with a very low empirical entropy (with respect to the security parameter) show up too frequently and thus can’t be modified while maintaining undetectability."

> "As expected, it is evident that the number of hidden bits grows linearly with the length of the response."

**ID:** capacity-linear-entropy-condition
**Location:** Section 1 "Introduction"; Section 2.4; Section 7 "Empirical Evaluation"
**Grep command used:** `Grep pattern="linear in the length of the response|very low empirical entropy|grows linearly with the length" path="literature/extracted/zamir_2024.txt"`

---

## Claim 8: Robustness — not very robust to edits; full rephrasing is expected to remove the signal

> "An open problem not addressed in this paper is that our encoding scheme is not very robust to edits of the generated text"

> "Intuitively, a complete rephrasing of the response, for example, is supposed to remove any watermark."

**ID:** not-robust-to-edits
**Location:** Section 1 "Introduction"; Section 8 "Limitations and Open Problems"
**Grep command used:** `Grep pattern="not very robust to edits|complete rephrasing of the response" path="literature/extracted/zamir_2024.txt"`

---

## Claim 9: Supersedes — earlier LLM message-embedding work alters the response distribution

> "embed messages in LLM responses, but do so by altering the distribution of responses, similar to the non-undetectable watermarking schemes."

**ID:** supersedes-distortion-embedding
**Location:** Section 1 "Introduction"
**Grep command used:** `Grep pattern="altering the distribution of responses" path="literature/extracted/zamir_2024.txt"`

---

## Claim 10: Evidence status — empirical evaluation is a proof of concept; the proofs are the contribution

> "Our empirical evaluation should be viewed merely as a proof-of-concept, while the theoretical parts and proof of undetectability are the main contributions of this paper."

**ID:** proof-of-concept-only
**Location:** Section 8 "Limitations and Open Problems"
**Grep command used:** `Grep pattern="merely as a proof-of-concept" path="literature/extracted/zamir_2024.txt"`

---

## Claim 11: Approach — undetectable LLM steganography: the CGZ undetectable watermark extended to carry a multi-bit payload, recovered with a secret key through a dynamic error-correcting code with feedback

> "We introduce a cryptographic method to hide an arbitrary secret payload in the response of a Large Language Model (LLM). A secret key is required to extract the payload from the model’s response, and without the key it is provably impossible to distinguish between the responses of the original LLM and the LLM that hides a payload. In particular, the quality of generated text is not affected by the payload."

> "Our approach extends a recent result of Christ, Gunn and Zamir (2023) who introduced an undetectable watermarking scheme for LLMs."

> "we introduce a simple dynamic error correcting code with feedback, which we later use as a building block."

**ID:** approach-undetectable-llm-stego
**Location:** Abstract; Section 1.1 "Organization of the paper"
**Grep command used:** `Grep pattern="We introduce a cryptographic method to hide|extends a recent result of Christ, Gunn and Zamir|dynamic error correcting code with feedback, which" path="literature/extracted/zamir_2024.txt"`
