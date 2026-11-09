---
paper: "Anwar et al. (2026)"
title: "A Decision-Theoretic Formalisation of Steganography With Applications to LLM Monitoring"
doi: "10.48550/arXiv.2602.23163"
pmcid: ""
url: "https://arxiv.org/abs/2602.23163v3"
source_version: "preprint"
file: "literature/anwar_2026.html"
retrieved: "20261105"
verified_by: "Claude (Opus 5.5) subagent, LLM-agents strand"
# The six below are written by `verify_quotes.py --stamp` — do not hand-edit.
# They bind the ledger to the exact source/extract bytes AND its own quoted text
# (body_sha256) it was verified against, so a later quote edit is caught in CI.
source_sha256: "00674902495f2bd855834b61e9c9e5bdb499102b364524406aec6da7f0f0c8a2"
extract_sha256: "12f766fcc5d32765be9fdb8fa6b0efe73f05579d77d3a21231658ef05644d6e6"
body_sha256: "396270b8de4826cf324dfee1635c7bf0947efbfef7c236ca6d8875b0803b717c"
verifier_version: "2"
verified_verdict: "pass"
verified_date: "20261106"
extract_source_sha256: "00674902495f2bd855834b61e9c9e5bdb499102b364524406aec6da7f0f0c8a2"
---

# Verified Claims — Anwar et al. (2026)

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

Identity: arXiv:2602.23163v3 [cs.AI], 29 Apr 2026; authors Usman Anwar, Julianna Piskorz, David
D. Baek, David Africa, Jim Weatherall, Max Tegmark, Christian Schroeder de Witt, Mihaela van
der Schaar, David Krueger. The DOI above is the arXiv-assigned DOI for that identifier, not one
printed in the paper. This is a detection formalism, not a scheme; it matters to the map as a
monitor and audit method.

## Claim 1: Problem — classical definitions need a known reference distribution, which LLM reasoning lacks

> "Classical definitions of steganography, and detection methods based on them, require a known reference distribution of non-steganographic signals. For the case of steganographic reasoning in LLMs, knowing such a reference distribution is not feasible; this renders these approaches inapplicable."

**ID:** problem-no-reference-distribution
**Location:** Abstract
**Grep command used:** `grep -n "require a known reference distribution of non-steganographic signals" literature/extracted/anwar_2026.txt`

---

## Claim 2: Central insight — steganography creates an asymmetry in usable information, visible in actions

> "Our central insight is that steganography creates an asymmetry in usable information between agents who can and cannot decode the hidden content (present within a steganographic signal), and this otherwise latent asymmetry can be inferred from the agents’ observable actions."

**ID:** usable-information-asymmetry
**Location:** Abstract
**Grep command used:** `grep -n "creates an asymmetry in usable information" literature/extracted/anwar_2026.txt`

---

## Claim 3: Definition — the steganographic gap compares downstream utility for Receiver and Sentinel

> "We use this to define the  steganographic gap —a measure that quantifies steganography by comparing the downstream utility of the steganographic signal to agents that can and cannot decode the hidden content."

> "A message  Z Z  with a steganographic content should have higher utility for the Receiver, who knows the encoding scheme and thus can utilise the hidden content, than for the Sentinel (a trusted agent with similar capabilities as the Receiver, who does not know the encoding scheme)."

**ID:** steganographic-gap-definition
**Location:** Abstract; Figure 2 caption
**Grep command used:** `grep -n "quantifies steganography by comparing the downstream utility" literature/extracted/anwar_2026.txt`; `grep -n "should have higher utility for the Receiver" literature/extracted/anwar_2026.txt`

---

## Claim 4: Critique of LLM-as-judge monitoring — steganography can look normal and anomalies can be benign

> "These heuristics implicitly assume steganographic content will appear anomalous—deviating from some notion of “normal” text—and thus detectable. But this assumption fails in both directions: steganographic content can appear entirely normal"

> "while anomalous text may arise from benign training artefacts"

**ID:** critique-llm-judge
**Location:** Section 1 Introduction
**Grep command used:** `grep -n "implicitly assume steganographic content will appear anomalous" literature/extracted/anwar_2026.txt`; `grep -n "anomalous text may arise from benign training artefacts" literature/extracted/anwar_2026.txt`

---

## Claim 5: Claimed reach — detects perfectly secure and paraphrasing-resistant schemes

> "Compared to existing approaches, our approach is unique in being theoretically grounded, applicable to LLM monitoring and and capable of detecting otherwise hard-to-detect forms of steganography, such as paraphrasing-resistant and information-theoretically secure schemes."

> "This asymmetry may manifest through agent’s actions, making it possible to detect, and quantify, steganography even when detection based on the signal alone is not possible"

**ID:** detects-secure-and-paraphrase-resistant
**Location:** Table 1 caption; Section 1 Introduction
**Grep command used:** `grep -n "capable of detecting otherwise hard-to-detect forms" literature/extracted/anwar_2026.txt`; `grep -n "even when detection based on the signal alone is not possible" literature/extracted/anwar_2026.txt`

---

## Claim 6: Auditing task may differ from the generation task

> "The auditing task may coincide with the generation task, but need not—for instance, the generation task might be to solve a coding problem, while the auditing task tests whether the reasoning trace reveals information about bypassing certain checks."

**ID:** auditing-task
**Location:** Section 5 Quantifying Steganographic Reasoning in LLMs
**Grep command used:** `grep -n "The auditing task may coincide with the generation task" literature/extracted/anwar_2026.txt`

---

## Claim 7: Validation — gap rises with Rot13 encoding strength and with codebook mismatch (codeword schemes)

> "As shown in Figure  3 , the steganographic gap increases smoothly as the encoding probability"

> "uses two codewords:  Sun  for Heads and  Moon  for Tails."

> "uses a larger codebook: Heads may be denoted by either  Sun  or  East , and Tails by either  Moon  or  West ."

> "The gap is highest when the Sentinel lacks knowledge of the Receiver’s codewords."

**ID:** validation-encoding-codebook
**Location:** Sections 6.1 and 6.2; Table 2 caption
**Grep command used:** `grep -n "the steganographic gap increases smoothly" literature/extracted/anwar_2026.txt`; `grep -n "Sun  for Heads" literature/extracted/anwar_2026.txt`; `grep -n "Sentinel lacks knowledge of the Receiver’s codewords" literature/extracted/anwar_2026.txt`

---

## Claim 8: Sentinel capability matters — a weaker Sentinel yields negative gaps

> "However, when using a weaker Sentinel (Qwen2.5-3B-Instruct), we observe  negative  gaps at low encoding levels: the weaker model benefits from"

**ID:** weaker-sentinel-negative-gap
**Location:** Section 6.1
**Grep command used:** `grep -n "when using a weaker Sentinel" literature/extracted/anwar_2026.txt`

---

## Claim 9: Limitations — supervised (needs a labelled auditing task); elicitation; sandbagging by an adaptive Receiver

> "Our approach can be considered  supervised , in that it requires the Auditor to specify an auditing task with ground-truth labels."

> "An adaptive Receiver with the knowledge of our auditing scheme may attempt to evade detection by"

**ID:** limitations
**Location:** Section 7 Discussion; Section 7.1, "Adversarial Robustness"
**Grep command used:** `grep -n "requires the Auditor to specify an auditing task" literature/extracted/anwar_2026.txt`; `grep -n "An adaptive Receiver with the knowledge of our auditing scheme" literature/extracted/anwar_2026.txt`

---

## Claim 10: Builds on — Cachin and Hopper et al. indistinguishability; Xu et al. V-information

> "Existing formalisms define steganography in terms of statistical  ( Cachin, 2004 )  or computational  ( Hopper et al., 2002 )  indistinguishability between steganographic and benign signal."

> "an extension of the framework of ‘usable’ information introduced by  Xu et al. (2020)"

**ID:** builds-on
**Location:** Section 2 Related Works; Section 1 Contributions
**Grep command used:** `grep -n "Existing formalisms define steganography in terms of statistical" literature/extracted/anwar_2026.txt`; `grep -n "usable’ information introduced by  Xu et al. (2020)" literature/extracted/anwar_2026.txt`

---

## Claim 11: Approach — a decision-theoretic view of steganography, detected and quantified by the steganographic gap over generalised V-information

> "We propose an alternative,  decision-theoretic view of steganography ."

> "To formalise this perspective, we introduce generalised  𝒱 \mathcal{V} -information: a utilitarian framework for measuring the amount of usable information within some input."

> "We use this to define the  steganographic gap —a measure that quantifies steganography by comparing the downstream utility of the steganographic signal to agents that can and cannot decode the hidden content."

**ID:** approach-steganographic-gap
**Location:** Section 1 Introduction; Abstract
**Grep command used:** `grep -n "We propose an alternative,  decision-theoretic view" literature/extracted/anwar_2026.txt`; `grep -n "we introduce generalised" literature/extracted/anwar_2026.txt`; `grep -n "quantifies steganography by comparing the downstream utility" literature/extracted/anwar_2026.txt`

---

## Claim 12: Relation to the classical formalism — three shortcomings addressed; Cachin's security recovered as a special case

> "The classical formalism for steganographic security  ( Hopper et al., 2002 ;  Cachin, 2004 )  has three shortcomings that our work addresses."

> "First, it requires a known or characterisable reference distribution of non-steganographic signals. Both the definition of security and all detection methods derived from it depend on this."

> "In this appendix, we show that classical information-theoretic notions of steganographic security  ( Cachin, 2004 )  can be recovered as a special case of our decision-theoretic framework. This establishes that our formalism generalises, rather than replaces, existing theory."

**ID:** classical-shortcomings-generalised
**Location:** Appendix (classical formalism comparison); Appendix on recovering Cachin's ε-security
**Grep command used:** `grep -n "has three shortcomings that our work addresses" literature/extracted/anwar_2026.txt`; `grep -n "can be recovered as a special case of our decision-theoretic framework" literature/extracted/anwar_2026.txt`

**Refines:** cachin_2004:approach-information-theoretic-model (grounded by #classical-shortcomings-generalised)
**Qualifies:** hopper_2002:approach-complexity-theoretic-steganography (grounded by #classical-shortcomings-generalised)

---

## Claim 13: Surveyed — word-level Rot13 encoding applied with probability p, as a graded steganography simulation

> "We simulate varying degrees of steganography by independently applying a Rot13 encoding to each word in  Z Z  with probability  p ∈ [ 0 , 1 ] p\in[0,1] , before presenting it to  S S —interpolating between fully legible ( p = 0 p=0 ) and fully ciphered ( p = 1 p=1 ) traces."

**ID:** surveyed-rot13-partial-encoding
**Location:** Section 6.1
**Grep command used:** `grep -n "We simulate varying degrees of steganography by independently applying a Rot13" literature/extracted/anwar_2026.txt`

---

## Claim 14: Surveyed — codeword schemes for coin-flip reasoning (Sun/Moon, and a larger codebook)

> "uses two codewords:  Sun  for Heads and  Moon  for Tails."

> "uses a larger codebook: Heads may be denoted by either  Sun  or  East , and Tails by either  Moon  or  West ."

**ID:** surveyed-codeword-codebook
**Location:** Section 6.2
**Grep command used:** `grep -n "Sun  for Heads" literature/extracted/anwar_2026.txt`; `grep -n "uses a larger codebook" literature/extracted/anwar_2026.txt`
