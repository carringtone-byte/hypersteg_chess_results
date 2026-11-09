---
paper: "Nakamura et al. (2026)"
title: "Colosseum: Auditing Collusion in Cooperative Multi-Agent Systems"
doi: "arXiv:2602.15198"
pmcid: ""
url: "https://arxiv.org/abs/2602.15198v2"
source_version: "preprint"
file: "literature/nakamura_2026.html"
retrieved: "20261105"
verified_by: "Claude (Opus 5.5) subagent, multi-agent collusion strand, quotes checked with verify_quotes.py (read-only run)"
# The six below are written by `verify_quotes.py --stamp` — do not hand-edit.
# They bind the ledger to the exact source/extract bytes AND its own quoted text
# (body_sha256) it was verified against, so a later quote edit is caught in CI.
source_sha256: "5da757ff4efbfcd459a7b10390c51c54ce7365d7998ffc50df07e8be62a1ca6d"
extract_sha256: "c00ff3804d21d5dc3b929f47663e799bbc13e2a8124bd2619f574c62356dd94f"
body_sha256: "c2249943c6a4c5847b63015f85e8a621f5332a96660504e5f5a1e8ddfd25787a"
verifier_version: "2"
verified_verdict: "pass"
verified_date: "20261106"
extract_source_sha256: "5da757ff4efbfcd459a7b10390c51c54ce7365d7998ffc50df07e8be62a1ca6d"
---

# Verified Claims — Nakamura et al. (2026)

Each claim below was extracted by reading the downloaded paper file with the Read
tool, grepping for the specific content, and reading the surrounding context to
confirm the attribution is faithful.

Source: arXiv:2602.15198v2 [cs.MA], 27 May 2026, as printed in the extract. Authors: Mason
Nakamura, Abhinav Kumar, Saswat Das (equal contribution), Sahar Abdelnabi, Saaduddin Mahmud,
Ferdinando Fioretto, Shlomo Zilberstein, Eugene Bagdasarian (University of Massachusetts
Amherst, University of Virginia, ELLIS Institute Tübingen, MPI for Intelligent Systems). The
arXiv identifier is printed in the extract; no DOI is printed. Section names follow the arXiv
HTML rendering. The paper studies collusion over an explicit private channel, not hidden
messages in a public one; it is relevant to Hypersteg as a model of what colluding teams do
once a side channel exists, and as a measure of how often a text judge misses it.

## Claim 1: Framing — prior LLM-collusion work studies tactics such as steganography; this paper audits behaviour

> "Recent work studying LLM collusion  ( Ren et al., 2025 ;  Motwani et al., 2024 )  focuses on collusion tactics (e.g., steganography) rather than model behavior, which is necessary for developing safe agents that are deployed in the real world."

> "Steganographic collusion uses covert messages on public or monitored channels to communicate with colluding parties while avoiding detection."

**ID:** behaviour-not-tactics-framing
**Location:** Section 1 "Introduction"; Section 2 "Background and Related Work", "Steganographic Collusion."
**Grep command used:** `/usr/bin/grep -n "focuses on collusion tactics\|Steganographic collusion uses covert messages" literature/extracted/nakamura_2026.txt`

---

## Claim 2: Formal setting — cooperative tasks as DCOPs, chosen because they make the objective explicit and allow cheap coalitional counterfactuals

> "First , it must make the intended cooperative objective explicit, so that any deviation we observe can be measured against a well-defined target."

> "Second , it must support computationally cheap coalitional counterfactuals: given an observed joint assignment, we need to ask what would have happened had a subset of agents acted differently, without re-simulating the entire trajectory."

**ID:** dcop-audit-formalism
**Location:** Section 3 "Problem Formulation" (DCOPs, Fioretto et al. 2018; definition in Section 3.1)
**Grep command used:** `/usr/bin/grep -n "make the intended cooperative objective explicit\|computationally cheap coalitional counterfactuals" literature/extracted/nakamura_2026.txt`

---

## Claim 3: Definition — collusion is a coalition steering a cooperative protocol away from the nominal objective, measured as a regret drop (Δ-collusion)

> "We define  collusion  as a multi-agent attack in which a subset of agents, or  coalition , coordinates to steer the system toward outcomes misaligned with the  nominal  DCOP objective, while still participating in an otherwise cooperative DCOP protocol."

> "making collusion auditable as a measurable drop in  F n F_{n}  relative to a nominal reference outcome"

**ID:** delta-collusion-definition
**Location:** Section 4 "Using Colosseum to Audit Collusion"; Section 4.1, Definition 4.1 (Δ-Collusion)
**Grep command used:** `/usr/bin/grep -n "multi-agent attack in which a subset of agents\|making collusion auditable as a measurable drop" literature/extracted/nakamura_2026.txt`

---

## Claim 4: Partial compromise (λ-alignment) and the split between specified and empirical λ, giving emergent and attempted ("on paper") collusion

> "prompts, persuasive messages, and revealed private context all induce  partial  compromise that varies in strength across agents and across turns."

> "This decoupling of  λ \lambda  also offers incites into how instances of  attempted collusion  (i.e., collusion-on-paper)"

> "may be too difficult to optimize due to bad coordination, optimal collusive actions are infeasible, or collusion mitigation strategies are in place, preventing the colluders to influence their environment."

**ID:** lambda-alignment-emergent-attempted
**Location:** Section 4.1 "Misaligned Agents and λ-Alignment" (Equation 1); Section 4.2, Definition 4.2 (Emergent Collusion: λ_spec = 0 and λ_emp > 0)
**Grep command used:** `/usr/bin/grep -n "induce  partial  compromise\|collusion-on-paper\|too difficult to optimize due to bad coordination" literature/extracted/nakamura_2026.txt`

---

## Claim 5: Behavioural probe — an explicit secret channel between agents, as a controlled intervention

> "A secret communication channel allows agents to converse separately from the public communication channel that all agents are members of."

> "We do not assume that all deployments contain explicit secret channels; rather, secret channels operationalize a realistic class of private side channels and test whether cooperative agents exploit them to coordinate collusively."

**ID:** secret-channel-behavioural-probe
**Location:** Section 1 "Introduction"; Section 4.2 "Behavioral Probe."
**Grep command used:** `/usr/bin/grep -n "A secret communication channel allows agents\|secret channels operationalize a realistic class" literature/extracted/nakamura_2026.txt`

---

## Claim 6: Detection signals — action-level regret metrics (coalition advantage) alongside an LLM-as-a-judge on channel text

> "are computed using an LLM-as-a-judge that outputs a Likert-scale score (0-5) for collusion occurrence based on channel communications."

> "Throughout our experiments, we use  GPT-5.4  as our LLM-as-a-judge unless otherwise specified"

> "This motivates the analysis in Figure  1 , which shows that conversations or actions alone are insufficient: neither captures the full space of potential collusion types needed to understand model behavior."

**ID:** regret-plus-judge-monitoring
**Location:** Section 5.3 "Experimental Settings", "Metrics." (coalition advantage = non-coalition mean regret minus coalition mean regret; judge scores averaged over three prompts); Section 1 "Introduction"
**Grep command used:** `/usr/bin/grep -n "outputs a Likert-scale score\|as our LLM-as-a-judge unless\|conversations or actions alone are insufficient" literature/extracted/nakamura_2026.txt`

---

## Claim 7: Result — emergent collusion across nineteen models once a secret channel exists; most action-level collusion is missed by the judge (hidden collusion)

> "Across nineteen models, we observe emergent collusion in both actions, measured by coalition advantage, and conversations, measured by LLM-as-a-judge scores"

> "57.89 % 57.89\%  of models in Emergent and  78.95 % 78.95\%  of models in Prompted exhibited  Δ \Delta -Advantage greater than  0 0  (i.e., action-based collusion) while  10.53 % 10.53\%  of models in Emergent and  78.95 % 78.95\%  in Prompted had a  Δ \Delta -Judge  ≥ 1 \geq 1 , showing that Emergent elicits more hidden collusion whereas Prompted elicits more direct collusion."

**ID:** emergent-collusion-hidden-from-judge
**Location:** Section 1 "Introduction"; Section 5.4 "Emergent Collusion in Benign Settings", Figure 4 (ten seeds, two runs per seed)
**Grep command used:** `/usr/bin/grep -n "Across nineteen models\|of models in Emergent and" literature/extracted/nakamura_2026.txt`

---

## Claim 8: Higher coalition advantage goes with lower judge scores (weak inverse association), and judge-evasive communication styles are model-dependent

> "there exists an inverse association between coalition advantage and judge score (i.e., the higher the coalition advantage the lower the judge score)"

> "However, we note that this may not be a significantly strong relation and leave validating this claim to future work over more models"

> "It remains unclear which qualitative factors yield efficient yet non-collusive communication that the judge models are unable to detect."

**ID:** advantage-judge-inverse-association
**Location:** Section 5.4, Figure 4 and footnote 2 (Pearson r = −0.243 Emergent, −0.1429 Prompted, n = 19 models)
**Grep command used:** `/usr/bin/grep -n "inverse association between coalition advantage\|may not be a significantly strong relation\|judge models are unable to detect" literature/extracted/nakamura_2026.txt`

---

## Claim 9: Efficacy — coalitions holding a high-leverage role (resource provisioner) achieve covert objectives while keeping overall regret at baseline

> "coalitions containing the powerful resource provisioner agent reliably achieve their misalignment objectives (whether covert or destructive) due to control over shared resources and bottlenecks"

> "Covert  – adversaries maximize  F c F_{c}  while keeping overall joint reward unchanged to remain stealthy"

**ID:** high-leverage-coalitions-covert
**Location:** Section 5.5 "Objective Misalignment", Figure 5 caption (Hospital environment)
**Grep command used:** `/usr/bin/grep -n "powerful resource provisioner agent\|while keeping overall joint reward unchanged" literature/extracted/nakamura_2026.txt`

---

## Claim 10: Persuasion and misinformation — authority and reciprocity tactics, and volume effects in the network

> "Across all topologies, we also find that Authority Nudge and Reciprocity Trade have a higher likelihood of significantly increasing"

> "successful persuasion requires the coalition to use false claims that are hard to verify and that benefit the coalition, while maintaining minimal violations."

> "As the number of adversaries grows, the victim-focused misinformation belief typically increases approximately linearly across most topologies"

**ID:** persuasion-and-misinformation-efficacy
**Location:** Section 5.6 "Persuasion" (Jira); Section 5.7 "Network Influence" (Meeting, GPT-4.1-Mini agents)
**Grep command used:** `/usr/bin/grep -n "Authority Nudge and Reciprocity Trade have\|false claims that are hard to verify\|victim-focused misinformation belief" literature/extracted/nakamura_2026.txt`

---

## Claim 11: Mitigations and limits — audit private channels, restrict high-leverage agents, verify claims against shared state; homogeneous single-step tasks only

> "private communication should be audited because even a benign secret channel produced emergent action- or conversation-level collusion"

> "allocation-relevant claims should be verified against shared state rather than accepted from peer messages"

> "Most experiments also use homogeneous teams with a shared model backbone, leaving heterogeneous deployments with varied models, prompts, permissions, and tool access for future work."

**ID:** mitigations-and-limitations
**Location:** Section 5.8 "Mitigating Collusion"; Section 6 "Conclusion", "Limitations and Future Work."
**Grep command used:** `/usr/bin/grep -n "private communication should be audited\|verified against shared state\|homogeneous teams with a shared model backbone" literature/extracted/nakamura_2026.txt`

---

## Claim 12: Approach (audit framework, not a steganographic method) — Colosseum: cooperative tasks cast as DCOPs, collusion measured as coalition regret, with a secret channel opened between agents as a controlled probe

> "In this paper, we introduce  Colosseum , a framework for auditing collusion in cooperative LLM-based multi-agent systems, with a focus on evaluating agent behavior through regret-based metrics and conversation logs."

> "We introduce a novel behavioral probing mechanism  ( Yoon et al., 2022 )  that instantiates secret communication channels as controlled interventions for testing whether and to what extent models exhibit collusive behavior on these channels unprompted."

> "By casting coordination tasks as DCOPs,  Colosseum  makes the intended cooperative objective explicit and enables regret-based action metric"

**ID:** approach-colosseum
**Location:** Section 1 "Introduction"; Section 4.2 "Applications to LLM Agents"; Section 6 "Conclusion"
**Grep command used:** `Grep pattern="a framework for auditing collusion in cooperative LLM-based|instantiates secret communication channels as controlled interventions|By casting coordination tasks as DCOPs" path="literature/extracted/nakamura_2026.txt"`
