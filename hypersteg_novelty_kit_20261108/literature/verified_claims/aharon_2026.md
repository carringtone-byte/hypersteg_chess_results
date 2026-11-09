---
paper: "Aharon et al. (2026)"
title: "Tacit Coordination of Large Language Models"
doi: "arXiv:2601.22184"
pmcid: ""
url: "https://arxiv.org/abs/2601.22184v2"
source_version: "preprint"
file: "literature/aharon_2026.html"
retrieved: "20261106"
verified_by: "Claude (Opus 5.5) subagent, multi-agent collusion strand, quotes checked with verify_quotes.py (read-only run)"
# The six below are written by `verify_quotes.py --stamp` — do not hand-edit.
# They bind the ledger to the exact source/extract bytes AND its own quoted text
# (body_sha256) it was verified against, so a later quote edit is caught in CI.
source_sha256: "c8dbfb77d3913290b5e4e910ca46aa1514feed215609607d22b5456e687e424b"
extract_sha256: "468338f2643fb59669f2f5b2e6978d8dc963d64f2a5d740de206a1624eb35be3"
body_sha256: "3b6e80c2ed44b8868eb507e91856361f684dc42cddd2e464efca175b1fb9fb4f"
verifier_version: "2"
verified_verdict: "pass"
verified_date: "20261106"
extract_source_sha256: "c8dbfb77d3913290b5e4e910ca46aa1514feed215609607d22b5456e687e424b"
---

# Verified Claims — Aharon et al. (2026)

Each claim below was extracted by reading the downloaded paper file with the Read
tool, grepping for the specific content, and reading the surrounding context to
confirm the attribution is faithful.

Source: arXiv:2601.22184v2 [cs.GT], 16 June 2026 (the identifier is printed in the extract).
Authors: Ido Aharon (Bar-Ilan University), Emanuele La Malfa (University of Oxford; Institute for
Decentralized AI), Michael Wooldridge (University of Oxford), Sarit Kraus (Bar-Ilan University).
The extract opens with arXiv HTML site boilerplate; the paper begins at the arXiv stamp. No
covert channel is studied: the paper measures coordination *without* communication through
Schelling focal points, which is the substrate a keyless scheme in Hypersteg would exploit.

## Claim 1: Setting — coordination without communication through focal points, across more than 20 LLMs

> "Humans often overcome the absence of communication through focal points: salient solutions that naturally stand out to all participants."

> "Across more than 20 open- and closed-source models, we find that LLMs exhibit a remarkable ability to coordinate without communication, often matching or outperforming humans."

**ID:** llm-focal-point-coordination
**Location:** Abstract
**Grep command used:** `/usr/bin/grep -n "absence of communication through focal points\|remarkable ability to coordinate without communication" literature/extracted/aharon_2026.txt`

---

## Claim 2: Known failure modes — numerical common sense and culturally nuanced salience

> "However, the same models consistently fail in tasks requiring numerical common sense or culturally nuanced notions of salience."

> "Our findings caution against assuming that LLMs share humans’ cultural and perceptual substrate when deployed in coordination settings."

**ID:** focal-failure-numerical-cultural
**Location:** Abstract
**Grep command used:** `/usr/bin/grep -n "numerical common sense\|cultural and perceptual substrate" literature/extracted/aharon_2026.txt`

---

## Claim 3: Two risks — divergent human/LLM salience and divergent salience between different LLMs

> "First, if LLM salience diverges from human salience, human–AI coordination may fail when communication is sparse."

> "Second, if different LLMs encode different notions of salience, AI–AI coordination may fail even when each agent is individually competent."

**ID:** salience-divergence-risks
**Location:** Section 1 "Introduction"
**Grep command used:** `/usr/bin/grep -n "if LLM salience diverges\|encode different notions of salience" literature/extracted/aharon_2026.txt`

---

## Claim 4: Formal definition — a focal point is the equilibrium maximising a salience function; uniqueness needs strong shared assumptions

> "When games admit multiple Nash equilibria, the theory alone does not predict which will occur. A key question is then how players choose independently so as to coordinate on the same equilibrium. We call this  tacit coordination ."

> "we need to make strong assumptions (i.e., same salience function, common monotone transform, common tie-breaking conventions) to guarantee the existence of a unique focal point in a game."

**ID:** focal-point-salience-function
**Location:** Section 3.1 "Nash Equilibria and Focal Points"
**Grep command used:** `/usr/bin/grep -n "We call this  tacit coordination\|common tie-breaking conventions" literature/extracted/aharon_2026.txt`

---

## Claim 5: Metric — the Coordination Index is the probability two random players pick the same strategy; NCI rescales it by the number of strategies

> "The CI is the probability that two randomly-chosen individuals choose the same strategy"

> "scales the Coordination Index with the number of strategies available to the players, and provides a measure of the concentration/dispersion of the strategy choices."

**ID:** coordination-index-metric
**Location:** Section 3.2 "Quantifying Tacit Coordination", Eq. (1)
**Grep command used:** `/usr/bin/grep -n "probability that two randomly-chosen\|concentration/dispersion" literature/extracted/aharon_2026.txt`

---

## Claim 6: Result — LLMs lead humans under "pick" but rely on order and surface cues, brittle where the focal point is cultural

> "LLMs outperform humans under “pick”, but the advantage narrows under “guess” and “coordinate”. They remain competitive in Amsterdam, whereas humans clearly outperform them in Nottingham."

> "LLMs instead rely more heavily on systematic cues such as option order, structural regularity, or surface salience. This makes them robust in some cases, but brittle when the focal point depends on subtle cultural context."

**ID:** llm-structural-salience-cues
**Location:** Section 4.1.1 "The Vanilla Amsterdam and Nottingham"
**Grep command used:** `/usr/bin/grep -n "LLMs outperform humans under\|systematic cues such as option order" literature/extracted/aharon_2026.txt`

---

## Claim 7: Result — more reasoning does not improve tacit coordination; long rationales collapse to positional heuristics

> "Surprisingly, more reasoning does not improve tacit coordination."

> "Log analysis shows that GPT-oss-120B often produces increasingly elaborate rationales that ultimately collapse to arbitrary positional heuristics, such as selecting the first option in a randomly permuted list."

**ID:** reasoning-does-not-help-coordination
**Location:** Section 4.1.1; Figure 4
**Grep command used:** `/usr/bin/grep -n "more reasoning does not improve tacit\|collapse to arbitrary positional heuristics" literature/extracted/aharon_2026.txt`

---

## Claim 8: Same-family models coordinate better; learning-free "culture" prompt lifts heterogeneous models to or above human level

> "Using models from the same family substantially improves NCI by reducing output diversity"

> "Figure  5  shows that “saliency” and “all-features” have little effect, whereas “culture” markedly improves NCI, matching or surpassing human performance in both Amsterdam and Nottingham."

**ID:** same-family-and-culture-prompt
**Location:** Section 4.1.2 "Improving Tacit Coordination"
**Grep command used:** `/usr/bin/grep -n "same family substantially improves NCI\|“culture” markedly improves NCI" literature/extracted/aharon_2026.txt`

---

## Claim 9: Focality profile — LLMs concentrate on centrality where humans use several principles

> "In Nottingham, humans use most focality dimensions except “uniqueness complement”, whereas LLMs concentrate on “centrality”."

> "the models select structurally central options even when human focality is driven by other cues."

**ID:** llm-centrality-bias
**Location:** Section 4.1.3 "Unique Focal Points and LLMs Saliency"; Figure 6
**Grep command used:** `/usr/bin/grep -n "whereas LLMs concentrate on\|select structurally central options" literature/extracted/aharon_2026.txt`

---

## Claim 10: Semi-competitive Bargaining Table — LLMs behave like cooperative agents; scale helps, reasoning level does not

> "Figure  7  shows that LLMs behave closest to cooperative agents: they achieve high payoff and high social welfare for both players."

> "By contrast, increasing reasoning level does not improve payoff or social welfare"

**ID:** bargaining-table-cooperative
**Location:** Section 4.2.1 "Results of the Bargaining Table"; Table 1
**Grep command used:** `/usr/bin/grep -n "behave closest to cooperative agents\|increasing reasoning level does not improve payoff" literature/extracted/aharon_2026.txt`

---

## Claim 11: Search and rescue — focal-point prompting helps only where the true endpoint is itself focal

> "No behaviour-aware prompt reliably improves the full set or the non-focal splits. Thus, focal-point prompting helps specifically when the missing person’s endpoint is plausibly tied to a salient terrain cue."

**ID:** sar-focal-prompting
**Location:** Section 4.3 "Focal Points in Search & Rescue Missions"
**Grep command used:** `/usr/bin/grep -n "No behaviour-aware prompt reliably improves" literature/extracted/aharon_2026.txt`

---

## Claim 12: Conclusion — the challenge is aligning what agents find salient, not making them reason more

> "Overall, LLM coordination is best understood as implicit social and spatial modelling. For mixed human–AI systems, the central challenge is not simply making agents reason more, but aligning what they find salient."

**ID:** align-salience-not-reasoning
**Location:** Section 5 "Discussion, Findings and Conclusions"
**Grep command used:** `/usr/bin/grep -n "implicit social and spatial modelling" literature/extracted/aharon_2026.txt`

---

## Claim 13: Approach (evaluation, not a steganographic method) — a large-scale study of focal points in LLMs, comparing tacit coordination with humans across cooperative and competitive games, and testing learning-free prompts that improve it

> "We present the first large-scale evaluation of how, when, and why focal points emerge in LLMs, comparing their behaviour with humans across cooperative and competitive games, including realistic search & rescue scenarios, demonstrating when focal points enable effective coordination."

> "We additionally evaluate simple learning-free strategies that substantially improve coordination both among LLMs and between humans and LLMs."

**ID:** approach-focal-point-evaluation
**Location:** Abstract
**Grep command used:** `Grep pattern="We present the first large-scale evaluation of how, when, and why focal points|simple learning-free strategies that substantially improve" path="literature/extracted/aharon_2026.txt"`

---

## Claim 14: Surveyed — the "saliency" prompt: choose the option most salient to humans (little effect)

> "The first prompt, “saliency”, asks the model to choose the option most salient to humans, approximating theory-theory accounts of Theory of Mind"

**ID:** surveyed-saliency-prompt
**Location:** Section 4.1.2 "Improving Tacit Coordination"
**Grep command used:** `Grep pattern="The first prompt, “saliency”, asks the model" path="literature/extracted/aharon_2026.txt"`

---

## Claim 15: Surveyed — the "all-features" prompt: reason over Kraus et al.'s focality principles (little effect)

> "The second, “all-features”, asks the model to reason over the focality principles of  Kraus et al. (2000) ."

**ID:** surveyed-all-features-prompt
**Location:** Section 4.1.2 "Improving Tacit Coordination"
**Grep command used:** `Grep pattern="The second, “all-features”, asks the model" path="literature/extracted/aharon_2026.txt"`

---

## Claim 16: Surveyed — the "culture" prompt: choose the option most culturally relevant to humans (lifts heterogeneous models to human level where culture is part of focality)

> "The third, “culture”, asks for the option most culturally relevant to humans, motivated by work on cultural representations in LLMs"

> "Thus, when culture is part of focality, a simple cultural prompt can make heterogeneous LLMs coordinate more human-like behaviourally"

**ID:** surveyed-culture-prompt
**Location:** Section 4.1.2 "Improving Tacit Coordination"
**Grep command used:** `Grep pattern="The third, “culture”, asks for the option|when culture is part of focality" path="literature/extracted/aharon_2026.txt"`
