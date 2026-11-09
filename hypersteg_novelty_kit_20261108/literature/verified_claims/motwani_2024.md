---
paper: "Motwani et al. (2024)"
title: "Secret Collusion among AI Agents: Multi-Agent Deception via Steganography"
doi: "10.48550/arXiv.2402.07510"
pmcid: ""
url: "https://arxiv.org/abs/2402.07510v5"
source_version: "preprint"
file: "literature/motwani_2024.html"
retrieved: "20261105"
verified_by: "Claude (Opus 5.5) subagent, LLM-agents strand"
# The six below are written by `verify_quotes.py --stamp` — do not hand-edit.
# They bind the ledger to the exact source/extract bytes AND its own quoted text
# (body_sha256) it was verified against, so a later quote edit is caught in CI.
source_sha256: "6d55f0f0be8767313a098852126d9ea809db6232d35bf5d9ace0012b19a48ecc"
extract_sha256: "3c29d038433bc2beddca8d96611d005ec611b6f35445800d5a3b47068783f55e"
body_sha256: "f2c8f45aeb79b7b4823a3e76239652db915d9412cab20b3ce62833b1386424ad"
verifier_version: "2"
verified_verdict: "pass"
verified_date: "20261106"
extract_source_sha256: "6d55f0f0be8767313a098852126d9ea809db6232d35bf5d9ace0012b19a48ecc"
---

# Verified Claims — Motwani et al. (2024)

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

Identity: arXiv:2402.07510v5 [cs.AI], 25 Jul 2025 (first version 2024); authors Sumeet Ramesh
Motwani, Mikhail Baranchuk, Martin Strohmeier, Vijay Bolina, Philip H.S. Torr, Lewis Hammond,
Christian Schroeder de Witt. The key's year follows the first arXiv version; the file read is
v5. The DOI above is the arXiv-assigned DOI for that identifier, not one printed in the paper.

## Claim 1: Definition of secret collusion

> "Secret collusion  involves AI agents colluding with each other secretly by communicating through hidden channels that look like innocuous communication channels via the use of steganographic techniques."

**ID:** def-secret-collusion
**Location:** Section 3.1 Collusion and Secret Collusion
**Grep command used:** `grep -n "involves AI agents colluding with each other secretly" literature/extracted/motwani_2024.txt`

---

## Claim 2: Shared state — a subliminal channel needs agreed message space, encoder and decoder, established without communication; focal points as one route

> "To this end, both need to agree on a covert message space"

> "Otherwise, agents may be able to infer unique choices using reasoning techniques contained in"

> "One such common reasoning technique is establishing preferred common knowledge labels through  focal points  ( Schelling points ,"

**ID:** subliminal-channel-common-knowledge
**Location:** Section 3.3 Steganography, "Subliminal Channels"
**Grep command used:** `grep -n "both need to agree on a covert message space" literature/extracted/motwani_2024.txt`; `grep -n "establishing preferred common knowledge labels" literature/extracted/motwani_2024.txt`

---

## Claim 3: Taxonomy — covertext modification versus information-theoretic and complexity-theoretic steganography

> "In  covertext modification  approaches, arguably the oldest form of steganography, it is assumed that the covertext distribution is deterministic."

> "Covertext modification approaches seek to exploit suboptimalities of the adversary, including limitations to human perception and neural network vulnerabilities."

> "Provable security usually requires access to a shared stream cipher, or the existence of public keys"

**ID:** taxonomy-covertext-vs-it
**Location:** Section 3.3 Steganography
**Grep command used:** `grep -n "arguably the oldest form of steganography" literature/extracted/motwani_2024.txt`; `grep -n "Provable security usually requires access to a shared stream cipher" literature/extracted/motwani_2024.txt`

---

## Claim 4: Incentive argument — secret collusion is incentivised when collusion helps the primary goal and getting caught is punished; intent is not required

> "Importantly, secret collusion need not depend on any exotic assumptions about the agents’ ‘intent’ to deceive, but might arise merely due to optimisation directed towards a mis-specified objective"

**ID:** incentive-misspecified-objective
**Location:** Section 4, "Incentives for Collusion"
**Grep command used:** `grep -n "need not depend on any exotic assumptions" literature/extracted/motwani_2024.txt`

---

## Claim 5: Insider-trading case study — a codebook built from common knowledge unavailable to the overseer; safe topics as cover

> "We show that the LLM agent refuses to provide company-specific insider investment advice under any circumstances unless supplied with common knowledge that can be used to establish a steganographic codebook, and that is thought to be unavailable to the safety overseer system."

> "Concerningly, the resulting stegotext may appear innocuous if one suggests the LLM agent use safe topics (e.g. weather)."

**ID:** insider-trading-codebook
**Location:** Section 6, "Real-world Case Study: Insider Trading"
**Grep command used:** `grep -n "used to establish a steganographic codebook" literature/extracted/motwani_2024.txt`; `grep -n "use safe topics (e.g. weather)" literature/extracted/motwani_2024.txt`

---

## Claim 6: Detection result — GPT-4 group covertext steganography evades the overseer about a quarter of the time

> "covertext steg. can evade overseer to coordinate ca. 26% of the time."

**ID:** group-stego-26pct
**Location:** Section 5, Table 3 (GPT-4 capability evaluations)
**Grep command used:** `grep -n "can evade overseer to coordinate ca. 26% of the time" literature/extracted/motwani_2024.txt`

---

## Claim 7: Key findings — Schelling-point and cipher capabilities scale with model size; colluders may outpace equally capable overseers

> "Agreement rates on simple & complex Schelling points (demonstrating higher zero-shot coordination), cipher encoding-decoding, and capabilities related to generating minimum entropy coupling matrices are highly correlated with model benchmark performance. In group settings, as LLMs progress, the balance between colluding models and overseer models may shift in favor of the colluding models, leading to higher rates of undetected steganography even if the overseer is of equal capability."

> "Overall, LLMs perform well at simple Schelling point agreement, cipher encoding-decoding, and tool use, but poorly at complex zero-shot agreement and tasks such as logit simulation and generating minimum entropy couplings."

**ID:** key-findings-scaling
**Location:** Section 6, "Key Findings"
**Grep command used:** `grep -n "Agreement rates on simple & complex Schelling points" literature/extracted/motwani_2024.txt`; `grep -n "perform well at simple Schelling point agreement" literature/extracted/motwani_2024.txt`

---

## Claim 8: Paraphrase robustness — semantic entropy survives paraphrasing

> "paraphrasing cannot be used to entirely remove the usable entropy in communications for the simple reason that, particularly in coordination tasks, agents both have a choice over communication  semantics , and hence  semantic entropy  can be utilised for covert communications even if these are paraphrased  within the lexical subspace"

> "The subliminal channel capacity attainable under ideal paraphrasing is upper bounded by the semantic entropy"

**ID:** paraphrase-semantic-entropy
**Location:** Section 7.2, "Paraphrasing", Theorem 4
**Grep command used:** `grep -n "paraphrasing cannot be used to entirely remove the usable entropy" literature/extracted/motwani_2024.txt`; `grep -n "attainable under ideal paraphrasing is upper bounded" literature/extracted/motwani_2024.txt`

---

## Claim 9: Monitoring limits — covertext anomaly detection works only against distribution-modifying schemes; detection by grounding functions

> "Using information-theoretic hypothesis testing or by other means of anomaly detection,"

> "can in principle detect steganographic approaches that modify the covertext distribution. However, the advent of  perfectly-secure  steganography"

> "Steganography can be detected using grounding functions."

**ID:** monitoring-anomaly-grounding
**Location:** Section 7.1, "Covertext Anomaly Detection" and Theorem 1
**Grep command used:** `grep -n "can in principle detect steganographic approaches that modify the covertext distribution" literature/extracted/motwani_2024.txt`; `grep -n "Steganography can be detected using grounding functions" literature/extracted/motwani_2024.txt`

---

## Claim 10: Overall verdict on current models

> "we find that current generations of generative AI models do not have capabilities that allow for advanced steganographic techniques. As a consequence, we suggest that monitoring, together with standard security approaches, are likely effective in containing the risks of model collusion."

**ID:** conclusion-limited-capability
**Location:** Section 8 Conclusion and Future Work
**Grep command used:** `grep -n "do not have capabilities that allow for advanced steganographic techniques" literature/extracted/motwani_2024.txt`

---

## Claim 11: Builds on — arithmetic coding (Ziegler et al.), provable security (Kaptchuk et al.), perfectly secure minimum-entropy-coupling steganography (Schroeder de Witt et al.)

> "One early attempt can be found in  Ziegler et al. (137) , which employs arithmetic coding. This approach was later refined to admit provable security guarantees by  Kaptchuk et al. (61) . In this paper, however, we consider the  perfectly secure  approach proposed by  Schroeder de Witt et al. (118)  as it offers both information-theoretic security and higher empirical transmission rates over its less secure alternatives."

**ID:** builds-on-ai-stego
**Location:** Section 2 Related Work, "AI-Generated Steganography"
**Grep command used:** `grep -n "which employs arithmetic coding" literature/extracted/motwani_2024.txt`

---

## Claim 12: Approach — CASE, a framework for evaluating secret collusion in individual and group LLM settings

> "We develop an evaluation framework,  CASE , for studying steganographic collusion and introduce benchmark scenarios for individual and group (multi-agent) LLM settings, including sandboxed real-world case studies."

> "We introduce CASE ( C ollusion  a nd  S teganographic  E valuation) as a comprehensive software framework for evaluating collusive capabilities. Our experiments here fall under CASE, which allows experiments of three key classes: individual model capability evaluations, group capability evaluations that involve LLMs communicating, often in the presence of monitoring systems, and novel qualitative real-world inspired evaluation settings. CASE allows for experiments to be performed with fine-tuning models and integrations with advanced information-theoretically secure steganography techniques as tools."

> "Furthermore, this framework provides insights into the empirical outcomes of utilizing iMEC in a simulated environment."

**ID:** approach-case-framework
**Location:** Section 1 Introduction; Section 5 "CASE Software Framework"; Appendix I
**Grep command used:** `grep -n "We develop an evaluation framework" literature/extracted/motwani_2024.txt`; `grep -n "We introduce CASE" literature/extracted/motwani_2024.txt`; `grep -n "empirical outcomes of utilizing iMEC" literature/extracted/motwani_2024.txt`

**Depends-on:** schroederdewitt_2022:approach-imec (grounded by #builds-on-ai-stego)

---

## Claim 13: Approach — group covertext steganography, hiding a secret word in common knowledge the overseer lacks

> "Secondly, we further expand the set-up such that  A A  and  B B  share additional common knowledge (in this setting, we use paragraphs from Wikipedia articles written in December 2023 on which LLMs haven’t been trained as shared common knowledge between the collusive models) which  E E  neither possess in-context nor as part of its training. Through this approach, our goal is to measure how often  A A  can hide a random secret word in an unrelated piece of common knowledge and how well the overseer  E E  can detect the secret versus how often  B B  can decode it."

**ID:** approach-common-knowledge-covertext
**Location:** Appendix G.2 "CASE Covertext Steganography Evaluations"
**Grep command used:** `grep -n "we further expand the set-up such that" literature/extracted/motwani_2024.txt`

---

## Claim 14: Surveyed — instructed first-letter (acrostic) covertext scheme

> "In our next approach, we directly measure the performance of models when using a narrower set of instructions specifying covertext modification-based encoding and decoding schemes. Note that these instructions are part of the common knowledge of  A A  and  B B  but not  E E . We tested how well models could encode and decode text while avoiding detection by hiding characters of  M M  as the first letters of each word in a message and provide detailed results in notebooks within CASE."

**ID:** surveyed-first-letter-acrostic
**Location:** Appendix G.2 "CASE Covertext Steganography Evaluations"
**Grep command used:** `grep -n "as the first letters of each word in a message" literature/extracted/motwani_2024.txt`

---

## Claim 15: Surveyed — standard ciphers (Base64, Caesar) as an encoding capability

> "We evaluated GPT-4’s capability to use a number of standard cipher schemes such as Base64 and Caesar cipher. GPT-4 was able to successfully encode and decode text using Base64 92% of the time and Caesar Cipher 54% of the time."

**ID:** surveyed-standard-ciphers
**Location:** Appendix F.3
**Grep command used:** `grep -n "We evaluated GPT-4’s capability to use a number of standard cipher schemes" literature/extracted/motwani_2024.txt`
