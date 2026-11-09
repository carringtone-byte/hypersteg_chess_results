---
paper: "Chang and Echizen (2024)"
title: "Steganography in Game Actions"
doi: "arXiv:2412.10442"
pmcid: "<PMC ID, if any>"
url: "arXiv:2412.10442v2 [cs.AI], 20 Apr 2025 (arXiv HTML rendering)"
source_version: "preprint"
file: "literature/chang_2024.html"
retrieved: "20261105"
verified_by: "Claude (Opus 5.5) subagent, quotes checked with verify_quotes.py (read-only run)"
# The six below are written by `verify_quotes.py --stamp` — do not hand-edit.
# They bind the ledger to the exact source/extract bytes AND its own quoted text
# (body_sha256) it was verified against, so a later quote edit is caught in CI.
source_sha256: "cf8e6822a26a3e316d4545147b190f61ac8efd4fe0cbf149571ad5ca86605314"
extract_sha256: "b5e003832dec9f79d43fc7e07dd3b4481a4d750ab290c7ab80526b86133ab334"
body_sha256: "588b59d61f98c742bea1690db6b89c1d2dec1dfc1da720f213dd80a139f454cc"
verifier_version: "2"
verified_verdict: "pass"
verified_date: "20261106"
extract_source_sha256: "cf8e6822a26a3e316d4545147b190f61ac8efd4fe0cbf149571ad5ca86605314"
---

# Verified Claims — Chang and Echizen (2024)

Each claim below was extracted by reading the downloaded paper file with the Read
tool, grepping for the specific content, and reading the surrounding context to
confirm the attribution is faithful.

Source: arXiv:2412.10442v2 [cs.AI], dated 20 Apr 2025 (first posted December 2024, per the
arXiv identifier), as printed in the extract after the arXiv site boilerplate. Authors:
Ching-Chun Chang and Isao Echizen, National Institute of Informatics, Tokyo. The arXiv HTML has
no page numbers, so locations are section numbers. The test bed is an 8 × 8 labyrinth, not
chess; the paper is mapped here as the reference case of learned action steganography with an
agent-identity code.

## Claim 1: Carrier — the episode (whole trajectory of states) of an agent acting in an environment

> "We propose a stego-system that encodes messages as the episodes of multiple agents, and decodes them by identifying the source of each observed episode."

> "An episode refers to a complete trajectory of states that starts from an initial state and ends at a terminal state."

**ID:** episode-trajectory-carrier
**Location:** Section I "Introduction"
**Grep command used:** `Grep pattern="encodes messages as the episodes|complete trajectory of states" path="literature/extracted/chang_2024.txt"`

---

## Claim 2: Encoding — one agent per message symbol; the decoder recovers the symbol by classifying which agent produced the episode

> "each agent learns to complete a given task within the environment while ensuring its episode is uniquely identifiable, whereas the observer learns to distinguish between the episodes of different agents."

> "the two steganographic agents embedded unique binary digits into their trajectories by incorporating steganographic feedback during training."

**ID:** agent-identity-codebook
**Location:** Section I; Section V-B "Visualisation of Policies"
**Grep command used:** `Grep pattern="ensuring its episode is uniquely identifiable|embedded unique binary digits" path="literature/extracted/chang_2024.txt"`

---

## Claim 3: Learning — multi-agent deep Q-learning shaped by a steganographic reward for being identifiable; observer is a bidirectional LSTM classifier

> "Steganographic Reward: Feedback, whether positive or negative, depends on the identifiability of the agent’s episode by the observer."

> "a steganographic reward of + 1.00 +1.00 is granted if the agent’s episode is identifiable by the observer"

> "This model utilises multi-layer bidirectional long short-term memory (LSTM) modules to capture both forward and backward temporal dependencies across sequences of states"

**ID:** stego-reward-marl-observer
**Location:** Section IV-E "Feedback Structure"; Section V-A 2 "Feedback Configuration"; Section IV-D
**Grep command used:** `Grep pattern="Steganographic Reward:|steganographic reward of|multi-layer bidirectional" path="literature/extracted/chang_2024.txt"`

---

## Claim 4: Pre-agreed — the stego-key is the shared hyper-parameters and random seeds, from which both sides rebuild identical agents and observer

> "Let 𝒦 \mathcal{K} be a stego-key, encapsulating a shared collective configuration of hyper-parameters and random seeds between Alice and Bob."

> "Since 𝒦 \mathcal{K} is shared between Alice and Bob, the resultant agents and observer should be identical"

**ID:** seed-hyperparameter-stego-key
**Location:** Section III-B "Agent & Observer"
**Grep command used:** `Grep pattern="encapsulating a shared collective configuration|resultant agents and observer should be identical" path="literature/extracted/chang_2024.txt"`

---

## Claim 5: Game-theoretic framing — a stag hunt between cooperating on distinguishable paths and defecting to optimal, overlapping ones

> "agents face decisions between cooperating to create distinguishable behavioural patterns or defecting to pursue individually optimal yet potentially overlapping episodic actions."

> "This framework models the strategic interplay between agents deciding whether to cooperate by creating distinguishable trajectories or to defect by prioritising optimal, potentially overlapping trajectories."

**ID:** stag-hunt-cooperation
**Location:** Abstract; Section III-D "Game-Theoretic Equilibria"
**Grep command used:** `Grep pattern="cooperating to create distinguishable|deciding whether to cooperate by creating" path="literature/extracted/chang_2024.txt"`

---

## Claim 6: Capacity — one bit per trajectory (two agents, labyrinth task)

> "This demonstrates the steganographic channel’s capacity to reliably transmit one bit of information through each trajectory."

**ID:** one-bit-per-trajectory
**Location:** Section V-D "Evaluation of Capacity"
**Grep command used:** `Grep pattern="reliably transmit one bit" path="literature/extracted/chang_2024.txt"`

---

## Claim 7: Distortion — stego agents complete the task almost as well as the baseline; one stego trajectory can equal the cover one

> "The results demonstrate that the steganographic agents achieved performance nearly identical to the baseline agent, with negligible deviations in time-steps and a small proportion of incomplete trajectories."

> "the cover trajectory and one of the stego trajectories were identical, demonstrating the indistinguishability of the steganographic channel."

**ID:** task-distortion-negligible
**Location:** Section V-C "Evaluation of Distortion"; Section V-B
**Grep command used:** `Grep pattern="performance nearly identical to the baseline|cover trajectory and one of the stego" path="literature/extracted/chang_2024.txt"`

---

## Claim 8: Threat model — Kerckhoffs: the adversary knows the system, not the key; passive Eve detects, active Trudy perturbs

> "We assume that the adversaries possess complete knowledge of the system, limiting the protection of the system solely to the secrecy of the key."

> "Eve can configure her own parameters to create shadow agents and build a detection mechanism to distinguish steganographic episodes from normal ones."

**ID:** kerckhoffs-eve-trudy
**Location:** Section III-C "Eavesdropper & Intruder"
**Grep command used:** `Grep pattern="possess complete knowledge of the system|create shadow agents" path="literature/extracted/chang_2024.txt"`

---

## Claim 9: Detection evidence — a steganalyser trained on shadow agents reaches 0.98 accuracy in training but 0.545 on unseen trajectories (AUC 0.5641)

> "the agents used to generate training data for the steganalyser were arbitrarily initialised."

> "In contrast, inference statistics show a notable decline, approaching random guessing (approximately 0.5), indicating the failure of the steganalyser to generalise"

> "F1 Score 0.9796 0.5646 AUC-ROC 0.9992 0.5641"

> "Accuracy (Stego) 0.96 0.59 Overall Accuracy 0.98 0.545"

In Table II the first figure in each row is the learning phase and the second the inference
phase on unseen trajectories; the detector is a steganalyser trained by the eavesdropper on
episodes from arbitrarily initialised shadow agents, so this is a measured detection rate, not
the authors' assertion.

**ID:** shadow-agent-steganalyser-result
**Location:** Section V-E "Evaluation of Secrecy against Eavesdropper"; Table II
**Grep command used:** `Grep pattern="arbitrarily initialised|approaching random guessing|Overall Accuracy|AUC-ROC" path="literature/extracted/chang_2024.txt"`

---

## Claim 10: Robustness — identifiability stays near 0.9 up to 0.4 forced-random-action rate and near 0.8 up to 0.7

> "Table III presents the performance metrics under varying levels of stochasticity, representing the probability that an agent is forced to deviate from its learnt policy to choose a random action."

> "Identifiability remains close to or above 0.9 under moderate stochasticity (up to 0.4) and close to or above 0.8 under high stochasticity (up to 0.7)."

**ID:** robustness-to-forced-random-actions
**Location:** Section V-F "Evaluation of Robustness against Intruder"; Table III
**Grep command used:** `Grep pattern="forced to deviate from its learnt policy|Identifiability remains close" path="literature/extracted/chang_2024.txt"`

---

## Claim 11: Scale of test — 100 labyrinths, 8 × 8 grid, fixed start and goal, optimal path fixed at 14 steps

> "We generated 100 labyrinth layouts for evaluations."

> "the optimal path length from the start to the goal remains fixed at 14 steps for every labyrinth."

**ID:** labyrinth-test-scale
**Location:** Section V-A 1 "Environmental Configuration"
**Grep command used:** `Grep pattern="100 labyrinth layouts|remains fixed at 14 steps" path="literature/extracted/chang_2024.txt"`

---

## Claim 12: Approach — action steganography: several reinforcement-learning agents each stand for one message symbol, and the receiver decodes by identifying which agent produced the observed episode

> "We propose a stego-system that encodes messages as the episodes of multiple agents, and decodes them by identifying the source of each observed episode."

> "The system comprises multiple agents and an observer: each agent learns to complete a given task within the environment while ensuring its episode is uniquely identifiable, whereas the observer learns to distinguish between the episodes of different agents. In essence, action steganography can be formulated as a multi-agent reinforcement learning framework"

> "As a proof of concept, we apply action steganography to the game of labyrinth, a navigation problem in which each agent steers towards a destination while encoding a message symbol into its episode."

**ID:** approach-action-steganography
**Location:** Section I "Introduction"
**Grep command used:** `Grep pattern="encodes messages as the episodes of multiple agents|each agent learns to complete a given task|we apply action steganography to the game of labyrinth" path="literature/extracted/chang_2024.txt"`
