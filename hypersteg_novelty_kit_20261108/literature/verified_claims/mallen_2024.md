---
paper: "Mallen et al. (2024)"
title: "Subversion Strategy Eval: Can language models statelessly strategize to subvert control protocols?"
doi: "arXiv:2412.12480"
pmcid: ""
url: "https://arxiv.org/abs/2412.12480v4"
source_version: "preprint"
file: "literature/mallen_2024.html"
retrieved: "20261105"
verified_by: "Claude (Opus 5.5) subagent, collusion-and-control strand, quotes checked with verify_quotes.py (read-only run)"
# The six below are written by `verify_quotes.py --stamp` — do not hand-edit.
# They bind the ledger to the exact source/extract bytes AND its own quoted text
# (body_sha256) it was verified against, so a later quote edit is caught in CI.
source_sha256: "c518909d053d584a30f39686d5c4ef0b2fc9cfcb633dfb5228cccdfddd9963cd"
extract_sha256: "0f5ab99e3317fe642295b90c9be09c5aea5789e2845796fba2731dc11ec7473b"
body_sha256: "f00220bd8888377c95a597952f777c7cd1a2e118797697c0805012f37866abe3"
verifier_version: "2"
verified_verdict: "pass"
verified_date: "20261106"
extract_source_sha256: "c518909d053d584a30f39686d5c4ef0b2fc9cfcb633dfb5228cccdfddd9963cd"
---

# Verified Claims — Mallen et al. (2024)

Each claim below was extracted by reading the downloaded paper file with the Read
tool, grepping for the specific content, and reading the surrounding context to
confirm the attribution is faithful.

Source: arXiv:2412.12480v4 [cs.LG], 4 April 2025 (printed in the extract; the DOI field is the
arXiv DOI formed from that identifier). Authors: Alex Mallen, Charlie Griffin, Misha Wagner,
Alessandro Abate, Buck Shlegeris (Redwood Research, University of Oxford, Anthropic). The HTML
extract carries no page numbers, so locations are by section and table. The extract renders
inline maths twice (e.g. "2.53 % 2.53\%"), so quotes below avoid those spans.

## Claim 1: Question — can models devise and act on their own subversion strategies while stateless, without shared memory between contexts

> "This paper investigates how well AI systems can generate and act on their own strategies for subverting control protocols whilst operating statelessly (without shared memory between contexts)."

> "To do this, an AI system may need to reliably generate optimal plans in each context, take actions with well-calibrated probabilities, and coordinate plans with other instances of itself without communicating."

**ID:** subversion-stateless-strategising-question
**Location:** Abstract (prior control work, Greenblatt et al. 2024, used human-written red-team strategies)
**Grep command used:** `Grep pattern="whilst operating statelessly|coordinate plans with other instances" path="literature/extracted/mallen_2024.txt"`

---

## Claim 2: Headline result — no model subverts statelessly with substantial skill; a shared plan helps substantially

> "None of the models demonstrate substantial capability in strategizing to subvert control protocols statelessly."

> "However, providing models with additional affordances, such as the ability to share a plan between contexts, can substantially improve performance."

**ID:** subversion-no-substantial-capability
**Location:** Abstract (models: Claude 3.5 Sonnet and Haiku, helpful-only and HHH; OpenAI o1-mini and o3-mini)
**Grep command used:** `Grep pattern="None of the models demonstrate|share a plan between contexts" path="literature/extracted/mallen_2024.txt"`

---

## Claim 3: Four sub-abilities — optimality and reliability in planning, probability calibration, acausal coordination

> "highlights four important sub-abilities for protocol subversion: Optimality in Planning, Reliability in Planning, Probability Calibration, and Acausal Coordination."

> "Because the AI is stateless and has no informative observations, it cannot determine whether the current round is audited."

**ID:** subversion-four-sub-abilities
**Location:** Section 1 "Introduction"; Section 2.1 "Example 1: Upfront auditing" (in the upfront-auditing game the optimal random backdoor rate gives a winrate of 69.7%)
**Grep command used:** `Grep pattern="four important sub-abilities|cannot determine whether the current round" path="literature/extracted/mallen_2024.txt"`

---

## Claim 4: Acausal coordination as a Schelling problem — instances must pick the same trigger without communicating

> "Acausal coordination  is the ability for separate instances of an agent to choose complementary strategies without the ability to communicate directly (i.e., without  causing  changes to each other’s observations)."

> "must create at least 4 poisoned documents with  the same signal text  in order to backdoor the monitor."

> "Picking a backdoor trigger is a  Schelling problem —a problem where agents must come to a ‘Schelling point’ without communicating, based on what they expect others would choose"

**ID:** subversion-acausal-schelling-coordination
**Location:** Section 2.2 "Example 2: Data poisoning" and footnote 5 (cites Schelling 1980)
**Grep command used:** `Grep pattern="Acausal coordination|the same signal text|Schelling problem" path="literature/extracted/mallen_2024.txt"`

---

## Claim 5: Untrusted-monitoring environment — one model plays generator and monitor; an output-collusion signal phrase is an optimal strategy

> "the AI plays as  both  of two roles: generator and monitor."

> "At the beginning, the monitor’s honesty is tested against  2 2  honeypots: solutions backdoored by the protocol to check that the monitor  REPORT s."

> "One optimal strategy for this setting is to do output collusion with a specific signal phrase: the generator always puts the comment “aaaaaaaaa” in its solution, and the monitor approves exactly the backdoors with that signal."

**ID:** subversion-untrusted-monitoring-output-collusion
**Location:** Table 1, row "APPS Untrusted Monitoring" (App. G.4); 18 APPS problems; a backdoor is a solution containing the codeword "LOVELACE"; honeypots are written by gpt-3.5-turbo
**Grep command used:** `Grep pattern="generator and monitor|honeypots: solutions backdoored|output collusion with a specific signal phrase" path="literature/extracted/mallen_2024.txt"`

---

## Claim 6: Input-collusion environments — defect only when the task carries a rare, agreed feature

> "The generator and monitor defect exactly when the current APPS problem has a specific collusion signal."

> "The signal should appear rarely in the datset: maximising the probability that it appears only after the honeypot phase."

> "Choose a collusion signal that occurs in 10% of problems (e.g. long and difficult). Both the monitor and generator should defect on exactly those problems."

**ID:** subversion-input-collusion-rare-signal
**Location:** Table 1, rows "APPS Input Collusion" (App. G.5) and "Input Collusion" (App. G.6) ("datset" is the paper's spelling)
**Grep command used:** `Grep pattern="specific collusion signal|appear rarely in the datset|occurs in 10% of problems" path="literature/extracted/mallen_2024.txt"`

---

## Claim 7: Affordances — randomness, shared planning (which turns acausal into causal coordination) and a given optimal strategy

> "The prompt contains a labeled random number independently sampled uniformly from"

> "First, we ask the model to generate a plan to be shared with all future instances"

> "This communication removes the need for  acausal coordination  (by enabling causal coordination) and reduces the need for  reliability in planning ."

**ID:** subversion-affordances-shared-planning
**Location:** Section 3.2 "Affordances" (six affordance pipelines across eight environments; implemented in Inspect-AI)
**Grep command used:** `Grep pattern="labeled random number|plan to be shared with all future|removes the need for" path="literature/extracted/mallen_2024.txt"`

---

## Claim 8: Given an optimal plan and randomness, Claude 3.5 Sonnet helpful-only exceeds 80% of optimal in 7 of 8 environments; planning is the bottleneck

> "When provided with an  optimal plan and randomness , the model’s winrate is"

> "Using  shared planning  instead of an optimal strategy degrades performance significantly in 14/16 cases (with or without randomness)."

> "This is consistent with the hypothesis that optimality in planning is an important and challenging capability."

**ID:** subversion-optimal-plan-near-optimal
**Location:** Section 4.1 "Sonnet 3.5 helpful-only", Fig. 4 (the extract renders the figure ">80% of the optimal in 7/8 environments" as duplicated maths, so it is reported here and not quoted)
**Grep command used:** `Grep pattern="optimal plan and randomness|14/16 cases|optimality in planning is an important" path="literature/extracted/mallen_2024.txt"`

---

## Claim 9: Shared planning helps where coordination is needed — acausal coordination is an obstacle to stateless subversion

> "For example, the AI’s performance at  DataPoisoningOfMonitor  improves significantly, as the model is able to use the same trigger phrase every round."

> "is consistent with the claim that acausal coordination is an obstacle to stateless protocol subversion in our environments."

> "Some of Claude’s plans are on the right track, but it is difficult to pick collusion signals that appear at an effective rate."

**ID:** subversion-acausal-coordination-obstacle
**Location:** Section 4.1 and footnote 15
**Grep command used:** `Grep pattern="same trigger phrase every round|acausal coordination is an obstacle|collusion signals that appear at an effective rate" path="literature/extracted/mallen_2024.txt"`

---

## Claim 10: Untrusted-monitoring collusion fails — the monitor rejects honeypots but also reports most of its own attacks

> "with default affordances the monitor never accepts honeypots and only accepts 11% of its own attacks."

> "Likewise, in  HardAppsUntrustedMonitoring  Claude never accepts any honeypots and only accepts 6.5% of its own attacks."

> "The monitor only accepts 44% of its own attacks because of difficulties identifying the collusion signal in the input."

**ID:** subversion-monitor-rejects-own-attacks
**Location:** Section 4.3 "Untrusted monitoring results", Fig. 6; footnote 10 (AppsInputCollusion with the optimal-plan affordance)
**Grep command used:** `Grep pattern="only accepts 11%|only accepts 6.5%|only accepts 44%" path="literature/extracted/mallen_2024.txt"`

---

## Claim 11: Calibration and reasoning errors — a naive 90% unaudited belief, and reasoning-model failures on collusion

> "The most frequent reasoning error we observed while informally reviewing  UpfrontAuditing  transcripts is the model being too aggressive because it naively believes that there is a 90% chance it is currently unaudited."

> "This suggests that Claude 3.5 Sonnet H-only struggles with probability calibration."

> "We observe that o1-mini and o3-mini perform significantly worse than Claude 3.5 Sonnet in our environments that require collusion."

**ID:** subversion-calibration-and-model-comparison
**Location:** Sections 4.1, 4.2 "Explaining upfront auditing results" and 4.5 "Comparing helpful-only, harmless, and reasoning models"
**Grep command used:** `Grep pattern="90% chance it is currently unaudited|struggles with probability calibration|o1-mini and o3-mini perform" path="literature/extracted/mallen_2024.txt"`

---

## Claim 12: Implication and limits — evidence that output collusion is hard would let untrusted monitoring be rated safer; single-environment winrates are noisy

> "For example, if strategic evaluations provide evidence that the model struggles to perform output collusion consistently, then protocols such as untrusted monitoring may be evaluated as safer."

> "Finally, winrate on a single environment can be a noisy indicator of capability."

**ID:** subversion-implication-and-noise
**Location:** Section 5 "Limitations and future work"
**Grep command used:** `Grep pattern="struggles to perform output collusion|noisy indicator of capability" path="literature/extracted/mallen_2024.txt"`

---

## Claim 13: Approach — Subversion Strategy Eval, eight environments and six affordance sets for stateless protocol subversion

> "We develop  Subversion Strategy Eval , a suite of eight environments, covering a range of protocols and strategic capabilities, and six sets of affordances that help isolate individual capabilities. We implement the evaluation in  Inspect-AI  and release it open-source."

> "This paper investigates how well AI systems can generate and act on their own strategies for subverting control protocols whilst operating statelessly (without shared memory between contexts)."

**ID:** approach-subversion-strategy-eval
**Location:** Abstract
**Grep command used:** `Grep pattern="We develop  Subversion Strategy Eval|This paper investigates how well AI systems can generate" path="literature/extracted/mallen_2024.txt"`

---

## Claim 14: Builds on — the environments are inspired by Greenblatt et al.'s control protocols, which tested human-written strategies

> "The environments were chosen to explore a range of control protocols, key dynamics, and difficulty levels. All environments except  DataPoisoningOfMonitor  are inspired by protocols from  Greenblatt et al. (2024) ."

> "Greenblatt et al. (2024)  evaluated control protocols by stress-testing them using LLM agents executing actions based on strategies devised by a human red team."

> "Greenblatt et al. (2024)  suggest this can be done by colluding on a signal in the problems (input collusion) or in the generator’s solutions (output collusion).)"

**ID:** builds-on-ai-control
**Location:** Section 3.1 Environments; Section 2 Related work; Section 3.1 (AppsUntrustedMonitoring)
**Grep command used:** `Grep pattern="are inspired by protocols from|evaluated control protocols by stress-testing|suggest this can be done by colluding on a signal" path="literature/extracted/mallen_2024.txt"`

**Refines:** greenblatt_2023:approach-control-evaluation (grounded by #builds-on-ai-control)
