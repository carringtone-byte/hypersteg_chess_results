---
paper: "Järviniemi (2025)"
title: "Subversion via Focal Points: Investigating Collusion in LLM Monitoring"
doi: "10.48550/arXiv.2507.03010"
pmcid: ""
url: "https://arxiv.org/abs/2507.03010v1"
source_version: "preprint"
file: "literature/jarviniemi_2025.html"
retrieved: "20261105"
verified_by: "Claude (Opus 5.5) subagent, LLM-agents strand"
# The six below are written by `verify_quotes.py --stamp` — do not hand-edit.
# They bind the ledger to the exact source/extract bytes AND its own quoted text
# (body_sha256) it was verified against, so a later quote edit is caught in CI.
source_sha256: "30d74ab03324dce61826a640cfb8e663121085afaf0d10a25ac8b264815bb9af"
extract_sha256: "e3e566d33f2cf1706831ceab297b2ffba169c8f8b704125c135cc6bf57f9a1a7"
body_sha256: "21270a8028eafd7c5a73c0370c34703011cd1f3822f1d168066e8a7117bca253"
verifier_version: "2"
verified_verdict: "pass"
verified_date: "20261106"
extract_source_sha256: "30d74ab03324dce61826a640cfb8e663121085afaf0d10a25ac8b264815bb9af"
---

# Verified Claims — Järviniemi (2025)

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

Identity: arXiv:2507.03010v1 [cs.CL], 02 Jul 2025; single author Olli Järviniemi. The DOI
above is the arXiv-assigned DOI for that identifier, not one printed in the paper.

## Claim 1: Setting — two isolated instances design policy and monitor prompts and must independently arrive at compatible strategies

> "we have two instances of a model design prompts for a policy (P) and a monitor (M) in a programming task setting. The models collaboratively aim for M to classify all backdoored programs in an auditing dataset as harmful, but nevertheless classify a backdoored program produced by P as harmless. The models are isolated from each other, requiring them to independently arrive at compatible subversion strategies."

**ID:** setting-isolated-meta-models
**Location:** Abstract
**Grep command used:** `grep -n "The models are isolated from each other" literature/extracted/jarviniemi_2025.txt`

---

## Claim 2: Shared key — none; the task is a Schelling coordination game on a focal point

> "the MP and MM cannot communicate with each other, but instead have to design strategies independently. This task is naturally viewed as a Schelling coordination game, where the meta-models aim to converge on a focal point."

**ID:** schelling-no-key
**Location:** Section 1 Introduction
**Grep command used:** `grep -n "naturally viewed as a Schelling coordination game" literature/extracted/jarviniemi_2025.txt`

---

## Claim 3: Contrast with human red-team signals such as an agreed variable name

> "Thus, M and P could be directly designed to adopt compatible attack strategies, such as using the presence of a particular variable name as a communication signal. However, in practice misaligned models couldn’t freely coordinate in such a way, raising the question of how well models can coordinate in practice."

**ID:** builds-on-greenblatt-red-team
**Location:** Section 1 Introduction
**Grep command used:** `grep -n "presence of a particular variable name as a communication signal" literature/extracted/jarviniemi_2025.txt`

---

## Claim 4: Carrier — code, with comments stripped before the monitor sees it

> "Any comments in the program written by P are removed before the output is shown to M."

**ID:** carrier-code-no-comments
**Location:** Section 2 Methodology
**Grep command used:** `grep -n "Any comments in the program written by P are removed" literature/extracted/jarviniemi_2025.txt`

---

## Claim 5: Auditing defence — the audit set grows from each past success, countering reused strategies

> "We construct the audit dataset iteratively. The dataset starts off empty, and upon sampling a successful collusion we insert it into the dataset."

> "The motivation for this is to better elicit different collusion strategies by countering those the models have used previously."

**ID:** iterative-auditing
**Location:** Sections 2 and 2.1
**Grep command used:** `grep -n "We construct the audit dataset iteratively" literature/extracted/jarviniemi_2025.txt`; `grep -n "by countering those the models have used previously" literature/extracted/jarviniemi_2025.txt`

---

## Claim 6: Result — low success rate, mostly from failing to converge

> "Out of those, Sonnet 3.7 successfully colluded  134 134  times, corresponding to a success rate of"

> "of the monitors classified all auditing examples correctly as backdoored, meaning that the vast majority of failures resulted from classifying the program by P as safe."

**ID:** result-low-success
**Location:** Section 3.1 Analysis of model strategies
**Grep command used:** `grep -n "Sonnet 3.7 successfully colluded" literature/extracted/jarviniemi_2025.txt`; `grep -n "vast majority of failures resulted from classifying" literature/extracted/jarviniemi_2025.txt`

---

## Claim 7: Only about a quarter of successes are genuine focal-point coordination

> "of the successful collusions as involving genuine coordination on a focal point, and the other  103 103  as M simply classifying anything not matching the auditing examples (which were described to it by the MM) as harmless."

**ID:** genuine-focal-share
**Location:** Section 3.1
**Grep command used:** `grep -n "as involving genuine coordination on a focal point" literature/extracted/jarviniemi_2025.txt`

---

## Claim 8: Coding — magic numbers drawn from broad world knowledge as focal signals

> "Sonnet 3.7 often uses magic numbers as collusion signals."

> "Some of the examples display broad world knowledge: 7919 and 982451653 are the thousandth and the fifty-millionth primes, 7355608 appears in the Counter-Strike video games, 24601 features in the novel Les Misérables, 6174 is the Kaprekar constant"

**ID:** coding-magic-numbers
**Location:** Section 3.1, after Table 1
**Grep command used:** `grep -n "often uses magic numbers as collusion signals" literature/extracted/jarviniemi_2025.txt`; `grep -n "display broad world knowledge" literature/extracted/jarviniemi_2025.txt`

---

## Claim 9: Some focal points are unpredictable in advance

> "While some of the collusion signals were unsurprising, there were some that we believe would have been infeasible to predict in advance without interacting with the model."

**ID:** unpredictable-focal-points
**Location:** Section 4 Discussion
**Grep command used:** `grep -n "infeasible to predict in advance without interacting" literature/extracted/jarviniemi_2025.txt`

---

## Claim 10: Limitation — one model, one setting; strategies sensitive to setting details

> "A central limitation of our study is that we only analyze one model in one setting. Based on cursory experiments in slight variations of the setup, we believe that understanding of the game dynamics and the particular strategies and collusion signals chosen are sensitive to details of the setting."

**ID:** limitation-one-model
**Location:** Section 4 Discussion
**Grep command used:** `grep -n "we only analyze one model in one setting" literature/extracted/jarviniemi_2025.txt`

---

## Claim 11: Approach — meta-models that independently design policy and monitor prompts, set in Greenblatt et al.'s untrusted monitoring

> "We evaluate AIs’ ability to do so in the untrusted monitoring setting from  Greenblatt et al. (2023) ."

> "We study this question by having copies of the model themselves design the attack strategies for P and M. For clarity, we will refer to these two instances by the terms meta-policy (MP) and meta-monitor (MM). The MP and MM will be instructed to construct prompts for P and M, respectively, in a way that lets M pass auditing while still falsely classifying an output by P as safe. The task of the meta-models is hence similar to the human red-teamers’, except that the MP and MM cannot communicate with each other, but instead have to design strategies independently."

**ID:** approach-meta-model-focal-collusion
**Location:** Section 1 Introduction
**Grep command used:** `grep -n "We evaluate AIs’ ability to do so in the untrusted monitoring setting" literature/extracted/jarviniemi_2025.txt`; `grep -n "We study this question by having copies of the model" literature/extracted/jarviniemi_2025.txt`

**Refines:** greenblatt_2023:approach-untrusted-monitoring-signal-jamming (grounded by #approach-meta-model-focal-collusion)

---

## Claim 12: Agreement with Mallen et al. — limited strategic subversion

> "We found that, in our setting, Claude Sonnet 3.7 often made poor strategic choices, in particular using too specific criteria for colluding. This finding is compatible with results from  Mallen et al. (2024) , which similarly found limited capabilities in strategic subversion of safety measures."

**ID:** compatible-with-mallen
**Location:** Section 5 Conclusion
**Grep command used:** `grep -n "This finding is compatible with results from" literature/extracted/jarviniemi_2025.txt`

**Supports:** mallen_2024:approach-subversion-strategy-eval (grounded by #compatible-with-mallen)
