---
paper: "Molinari and Bettineschi (2026)"
title: "Multi-Agent Collusion and the J-Space"
doi: "arXiv:2611.02153"
pmcid: ""
url: "https://arxiv.org/abs/2611.02153v1"
source_version: "preprint"
file: "literature/molinari_2026.html"
retrieved: "20261105"
verified_by: "Claude (Opus 5.5) subagent, multi-agent collusion strand, quotes checked with verify_quotes.py (read-only run)"
# The six below are written by `verify_quotes.py --stamp` — do not hand-edit.
# They bind the ledger to the exact source/extract bytes AND its own quoted text
# (body_sha256) it was verified against, so a later quote edit is caught in CI.
source_sha256: "c5ba4c6ccbb0c822dd9865fb36144b50dce70dc39b8898325af9b5abc3e48b0a"
extract_sha256: "a1d23f0d31aeee388bacaa87cda432bb1ee9e9b0c3ac63b498aa1c96f9382f8c"
body_sha256: "b22c74d206fb597b4421175d89de76521e0d1a1d0681cc321956b7999b3ce718"
verifier_version: "2"
verified_verdict: "pass"
verified_date: "20261106"
extract_source_sha256: "c5ba4c6ccbb0c822dd9865fb36144b50dce70dc39b8898325af9b5abc3e48b0a"
---

# Verified Claims — Molinari and Bettineschi (2026)

Each claim below was extracted by reading the downloaded paper file with the Read
tool, grepping for the specific content, and reading the surrounding context to
confirm the attribution is faithful.

Source: arXiv:2611.02153v1 [cs.CL], 1 November 2026, as printed in the extract. Authors: Marco
Molinari (London School of Economics) and Gabriele Bettineschi (EPFL). The arXiv identifier is
printed in the extract; no DOI is printed. Section names below are those of the arXiv HTML
rendering. The paper is a white-box (activation-level) detector of collusion, evaluated on
NARCBench (Rose et al. 2026, ledger `rose_2026`), whose Stego split is a card-counting covert
channel in public table talk.

## Claim 1: Motivation — text monitors can be beaten by covert signals in public messages; activation probes need labels for anticipated tactics

> "Text-based monitors can fail when public messages encode a covert signal  ( Motwani et al., 2024 ) . Activation probing has been proposed as a solution, as activations can’t be circumvented by covert communication channels"

> "However, probes need labels, which exist only for tactics someone anticipated, and the incidents above were not anticipated."

**ID:** text-monitors-fail-probes-need-labels
**Location:** Section 1 "Introduction"
**Grep command used:** `/usr/bin/grep -n "Text-based monitors can fail\|probes need labels" literature/extracted/molinari_2026.txt`

---

## Claim 2: Threat model — a designated subset of agents receives private instructions to coordinate against the intended task while taking part in public interaction

> "A collusion happens when some agents coordinate toward a goal different from the intended task"

> "In the collusion condition, a designated subset receives private instructions to coordinate against it while participating in the public interaction. An interesting goal is to distinguish the collusion and the control runs without accessing the private instructions."

**ID:** collusion-threat-model-private-instructions
**Location:** Section 2.1 "Multi-Agent Collusion"
**Grep command used:** `/usr/bin/grep -n "A collusion happens when\|designated subset receives private" literature/extracted/molinari_2026.txt`

---

## Claim 3: Covert channel studied — NARCBench Stego, where a sender signals a card-count range through public table talk, using a signal agreed in private

> "On Stego, a sender signals the count range (NEGATIVE, NEUTRAL or HOT) through public table talk, and the receiver bets on it."

> "After the upbeat remarks the pair agreed would signal HOT, the colluding receiver’s layer-25 readout at its response-start token contains “decode” in several forms and languages"

> "Left: the signal the pair agreed in private coordination. Middle: the sender’s public table talk."

**ID:** stego-card-count-table-talk
**Location:** Section 3 "Colluders’ J-Space Holds the Collusion", text and Figure 4 caption. Carrier: public table-talk text; message: one of three count ranges (about log2 3 bits per hand); shared secret: a signal mapping agreed in a private coordination channel.
**Grep command used:** `/usr/bin/grep -n "signals the count range\|upbeat remarks the pair agreed\|agreed in private coordination" literature/extracted/molinari_2026.txt`

---

## Claim 4: Method — the Jacobian lens reads intermediate activations as vocabulary tokens (the "J-space"), and the authors compare it across agents of one model

> "This yields a readout in the “J-space”, where each direction is a token in the vocabulary: a list of words an LLM is disposed to say at a certain layer."

> "Agents which are instances of one LLM operate in the same J-space, so their readouts can be compared."

**ID:** jacobian-lens-shared-j-space
**Location:** Section 1 "Introduction"; method detailed in Section 2.2 "The Jacobian Lens and the J-Space" (following Gurnee et al. 2026)
**Grep command used:** `/usr/bin/grep -n "yields a readout in the\|Agents which are instances of one LLM" literature/extracted/molinari_2026.txt`

---

## Claim 5: Colluders represent the collusion before replying, and the colluding pair shares those concepts exclusively

> "At the response-start token, 86 of the 100 Core colluders hold a collusive concept, against 33 of their honest counterfactuals"

> "In 35 of 50 collusion runs the colluding pair holds a concept of the groups that neither honest agent holds"

> "against 4 of 50 control runs, counting any of their six pairs"

**ID:** colluders-hold-collusion-in-j-space
**Location:** Section 3 "Colluders’ J-Space Holds the Collusion" (DeepSeek-V4-Flash, NARCBench Core)
**Grep command used:** `/usr/bin/grep -n "86 of the 100 Core colluders\|35 of 50 collusion runs" literature/extracted/molinari_2026.txt`

---

## Claim 6: The Stego receiver's internal state holds the hidden count; its honest counterfactual does not

> "At the last token of the sender’s message, the colluding receiver holds the signature of the true count range in 0.41 of NEGATIVE hands, 0.54 of NEUTRAL hands and 0.62 of HOT hands, more often than that of any other range, for every range"

> "Its honest counterfactual, reading the same table and message, holds a range’s signature in at most 0.10 of the hands of any range"

**ID:** receiver-holds-hidden-count
**Location:** Section 3, "The receiver holds the hidden count."
**Grep command used:** `/usr/bin/grep -n "colluding receiver holds the signature\|holds a range’s signature in at most" literature/extracted/molinari_2026.txt`

---

## Claim 7: Causal steering — swapping two J-lens coordinates redirects the count the receiver decodes; random swaps do not

> "Exchanging only the receiver’s  HOT  and  Negative  coordinates moves the range it decodes towards HOT"

> "It reads 0.57 of NEGATIVE hands as HOT at  α = 1.25 \alpha=1.25  and 0.30 at  α = 1 \alpha=1 , against 0.02 without the swap"

> "Swapping random token pairs reads at most 0.02 of NEGATIVE hands as HOT"

**ID:** j-space-swap-steers-decoding
**Location:** Section 4 "Steering Steganographic Decoding with the J-Space" (140 Stego hands, intervention at every position except the answer)
**Grep command used:** `/usr/bin/grep -n "Exchanging only the receiver\|It reads 0.57 of NEGATIVE\|Swapping random token pairs reads" literature/extracted/molinari_2026.txt`

---

## Claim 8: Detector — J-PACT scores each pair by the concepts it shares more strongly with each other than with the other agents at the table

> "A concept contributes to the score when two agents share it more strongly with each other than, on average, with the remaining agents. We average these contributions across layers and responses to score each pair. No training on collusion labels is needed."

> "a pair is compared with the other agents at the same table, who read the same messages in the same turns, so concepts that the task or the conversation places in every agent’s J-space cancel"

**ID:** j-pact-relational-score
**Location:** Section 6 "Related Work", "Relational detection."; the score is defined in Section 5 (Equations 4–7), with the run's score the maximum pair score
**Grep command used:** `/usr/bin/grep -n "A concept contributes to the score\|compared with the other agents at the same table" literature/extracted/molinari_2026.txt`

---

## Claim 9: Detection rates — unsupervised J-PACT reaches AUROC 0.921 on Core and matches the supervised probe on Stego

> "J-PACT reaches an AUROC of 0.921 on Core (mean of four models), which is 85% of the supervised NARCBench probe’s above-chance AUROC"

> "On the steganographic Stego split, where both detectors see every discussion round, J-PACT matches the probe (0.991 against 0.999) and separates every collusion run from every control one on three of four models (AUROC 1.000)."

**ID:** j-pact-detection-auroc
**Location:** Section 5 "J-PACT Detects Collusion", Table 1 (GPT-OSS-20B, Qwen3-32B, Llama-3.3-70B-IT, DeepSeek-V4-Flash, reading NARCBench's released transcripts)
**Grep command used:** `/usr/bin/grep -n "J-PACT reaches an AUROC of 0.921\|J-PACT matches the probe" literature/extracted/molinari_2026.txt`

---

## Claim 10: Localisation — a flagged run's top pair is the colluding pair or its complement in 99% of Core and 100% of Stego runs

> "The pair J-PACT predicts,  C ^ \widehat{C} , is the colluding pair  C C  or its complement  C ¯ \bar{C}  in 99% of Core and"

> "Picking by chance only selects one of these two pairs in 33% of runs with six candidate pairs"

**ID:** j-pact-localisation-up-to-complement
**Location:** Section 5, "J-PACT names the colluding pair up to its complement.", Table 3 (localisation scored at a 5% false-positive rate)
**Grep command used:** `/usr/bin/grep -n "is the colluding pair\|Picking by chance only selects" literature/extracted/molinari_2026.txt`

---

## Claim 11: Limits — J-PACT is at chance when honest agents are not exchangeable (Transfer), requires a shared model, and was steered on one model only

> "J-PACT assumes exchangeable honest agents; on Transfer, whose role-structured scenarios break this assumption and give one observation per agent, it is at chance"

> "Our interpretability and steering results are on one model, DeepSeek-V4-Flash, and one benchmark, NARCBench."

> "J-PACT (Section  5 ) requires that all agents of a run are instances of the same model, so that their activations share coordinates"

**ID:** j-pact-limitations
**Location:** Section 7 "Limitations"; Section 2.1 (same-model requirement). Transfer AUROC 0.519 against the probe's 0.729 (Section 1).
**Grep command used:** `/usr/bin/grep -n "J-PACT assumes exchangeable honest agents\|Our interpretability and steering results\|requires that all agents of a run" literature/extracted/molinari_2026.txt`

---

## Claim 12: Approach — J-PACT, unsupervised pairwise collusion detection from shared J-space concepts

> "We introduce J-PACT, an unsupervised method for detecting collusion among agents that share a model and role; across four open-weight models it retains 85% of the supervised probes’ above-chance AUROC on Core, matches them on Stego at equal observations, and locates colluding pairs up to their complement."

> "We introduce a way to distinguish representations of concepts that are shared between all agents as opposed to only within a certain (potentially colluding) pair."

**ID:** approach-j-pact
**Location:** Section 1 "Our contributions"; Section 5
**Grep command used:** `/usr/bin/grep -n "We introduce J-PACT, an unsupervised method\|We introduce a way to distinguish representations of concepts" literature/extracted/molinari_2026.txt`

---

## Claim 13: Approach — causal steering of steganographic decoding by swapping J-lens concept coordinates

> "We show causally that the Stego receiver decodes the covert signal through its J-space: swapping two of its concepts redirects the count it decodes."

> "Following  Gurnee et al. (2026) , we exchange two concepts by clamping their lens coordinates:"

**ID:** approach-j-space-steering
**Location:** Section 1 "Our contributions"; Section 4
**Grep command used:** `/usr/bin/grep -n "We show causally that the Stego receiver decodes\|we exchange two concepts by clamping" literature/extracted/molinari_2026.txt`

---

## Claim 14: Relation to Rose et al. (2026) — NARCBench used throughout; its supervised probes need labels and score only runs

> "Rose et al. (2026)  study probing on their benchmark NARCBench: agents get private instructions and a private communication channel, while the monitor sees only the public one. However, probes need labels, which exist only for tactics someone anticipated, and the incidents above were not anticipated. NARCBench also evaluates its probes only at the run level, not on which agents collude or why."

> "In the NARCBench benchmark, that we use in the following, each multi-agent task scenario is run in two conditions: collusion, and control."

> "We compare J-PACT with NARCBench probes as a supervised reference / ceiling."

**ID:** relation-rose-narcbench
**Location:** Section 1 "Introduction"; Section 2.1; Section 5
**Grep command used:** `/usr/bin/grep -n "study probing on their benchmark NARCBench\|that we use in the following\|We compare J-PACT with NARCBench probes" literature/extracted/molinari_2026.txt`

**Depends-on:** rose_2026:approach-narcbench (grounded by #relation-rose-narcbench)
**Qualifies:** rose_2026:approach-helios (grounded by #relation-rose-narcbench)
