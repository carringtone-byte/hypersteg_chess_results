---
paper: "Mathew et al. (2024)"
title: "Hidden in Plain Text: Emergence & Mitigation of Steganographic Collusion in LLMs"
doi: "10.48550/arXiv.2410.03768"
pmcid: ""
url: "https://arxiv.org/abs/2410.03768v2"
source_version: "preprint"
file: "literature/mathew_2024.html"
retrieved: "20261105"
verified_by: "Claude (Opus 5.5) subagent, LLM-agents strand"
# The six below are written by `verify_quotes.py --stamp` — do not hand-edit.
# They bind the ledger to the exact source/extract bytes AND its own quoted text
# (body_sha256) it was verified against, so a later quote edit is caught in CI.
source_sha256: "28476e88e402db38fafe73a081dfa609e154742739cacbda3d80d432ef6119f9"
extract_sha256: "0191423bedb1ffcda8121a32fae5ea0ad8cf7e66aab8ca509c71cbca222d00e8"
body_sha256: "021417a02d4b685f1cd70247f3fd2fb6d9dca7124d47729f7d6552982b44a75c"
verifier_version: "2"
verified_verdict: "pass"
verified_date: "20261106"
extract_source_sha256: "28476e88e402db38fafe73a081dfa609e154742739cacbda3d80d432ef6119f9"
---

# Verified Claims — Mathew et al. (2024)

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

Identity: arXiv:2410.03768v2 [cs.CL], 02 Dec 2025 (first version 2024); authors Yohan Mathew,
Ollie Matthews, Robert McCarthy, Joan Velja, Christian Schroeder de Witt, Dylan Cope, Nandi
Schoots. The key's year follows the first arXiv version; the file read is v2. The DOI above is
the arXiv-assigned DOI for that identifier, not one printed in the paper.

## Claim 1: Framework — collusion team (sender, receiver) against a mitigation team (overseer, optional paraphraser)

> "We frame steganography as an adversarial relationship between two teams, a  collusion team  and a  mitigation team ."

> "It consists of an  overseer  and an optional  paraphraser . The paraphraser rewords the stegotext in an attempt to remove the payload. The overseer attempts to detect the presence of steganography by analysing stegotexts."

**ID:** framework-two-teams
**Location:** Section 3.1 Our Steganography Framework
**Grep command used:** `grep -n "adversarial relationship between two teams" literature/extracted/mathew_2024.txt`; `grep -n "The paraphraser rewords the stegotext" literature/extracted/mathew_2024.txt`

---

## Claim 2: Schemes are invented by optimisation (GBRL weight updates or ICRL natural-language strategies), not given

> "For GBRL, the weights of a pretrained LLM are modified by  gradient descent  via an RL algorithm. In ICRL, the behavior of each agent is defined by  strategies  (represented in natural language) within the context window that are improved over time, and the weights of the collusion team LLMs remain fixed."

> "An ICRL Learner is an LLM that devises steganography strategies for the sender and receiver to execute."

**ID:** schemes-from-optimisation
**Location:** Sections 3.3 and 3.3.2
**Grep command used:** `grep -n "represented in natural language) within the context window" literature/extracted/mathew_2024.txt`; `grep -n "devises steganography strategies for the sender and receiver" literature/extracted/mathew_2024.txt`

---

## Claim 3: Shared state — decentralised learners have no secret coordination channel; the centralised learner has one

> "Our GBRL and Decentralized ICRL Learners methods may act as realistic optimization pressures (as there is no secret coordination channels between the sender and receiver)"

> "Our Centralized ICRL Learner may act as a stronger optimization pressure to red-team mitigations (see Section  5.2 ); it is strengthened by the secret coordination channel between the sender and the receiver."

**ID:** coordination-channel-central-vs-decentral
**Location:** Section 3.3.3
**Grep command used:** `grep -n "no secret coordination channels between the sender and receiver" literature/extracted/mathew_2024.txt`; `grep -n "strengthened by the secret coordination channel" literature/extracted/mathew_2024.txt`

---

## Claim 4: Emergence — unintended steganographic collusion arises from misspecified reward

> "We demonstrate, for the first time, that unintended steganographic collusion in LLMs can arise due to mispecified reward incentives during training."

**ID:** emergence-misspecified-reward
**Location:** Abstract
**Grep command used:** `grep -n "can arise due to mispecified reward incentives" literature/extracted/mathew_2024.txt`

---

## Claim 5: Coding by lexical and stylistic choice in cover letters

> "Strategies that seemed ‘subtle’ to us included referring to males as “individuals” and females as “candidates”, or using the phrase “and is also skilled in” for males and “and is able to” for females. Experiments with a paraphraser converged to writing 1st-person cover letters for the Good University and writing in 3rd-person for the Bad University."

> "An example "subtle" strategy learned by Claude (when there was no paraphraser) was to use different specific phrases, such as “innovative mindset” or “traditional approach” depending on the university."

**ID:** coding-lexical-stylistic
**Location:** Section 5.1, "GBRL Results" and "ICRL Results"
**Grep command used:** `grep -n "referring to males as" literature/extracted/mathew_2024.txt`; `grep -n "innovative mindset" literature/extracted/mathew_2024.txt`

---

## Claim 6: Oversight pushes strategies to become subtler rather than stopping them

> "From this initialized state, the collusion team learns to make their strategy increasingly hard to spot, eventually converging to a strategy that always bypasses the overseer"

> "This is further evidence that oversight is not always effective at preventing collusion, but can in-fact encourage collusion that is more subtle (with respect to the overseer)."

**ID:** oversight-encourages-subtlety
**Location:** Section 5.1, "Oversight Encourages Subtle Collusion"
**Grep command used:** `grep -n "learns to make their strategy increasingly hard to spot" literature/extracted/mathew_2024.txt`; `grep -n "can in-fact encourage collusion that is more subtle" literature/extracted/mathew_2024.txt`

---

## Claim 7: Capacity and paraphrase robustness — context-aware paraphrasing hampers multi-bit communication, but 1-bit survives

> "In  AQuA-RAT , the paraphrasers significantly reduce collusion success rates at higher payload sizes. In particular, the context-aware paraphraser makes multi-bit communication difficult. However, in all cases, the collusion team is able to maintain a decoding success of at least 90% on 1-bit payloads."

> "In  HumanEval , we find the collusion team is able to encode less information overall, but the coding paraphraser is not able to completely cut out communication."

**ID:** capacity-paraphrase-aquarat-humaneval
**Location:** Section 5.2, "Mitigation Effectiveness Across Payload Sizes"
**Grep command used:** `grep -n "context-aware paraphraser makes multi-bit communication difficult" literature/extracted/mathew_2024.txt`; `grep -n "coding paraphraser is not able to completely cut out" literature/extracted/mathew_2024.txt`

---

## Claim 8: Capacity on the Roger & Greenblatt benchmark

> "Training against our standard paraphraser with no overseer resulted in a 6-bit strategy, which achieved a channel capacity of 4.6 on the benchmark with standard paraphrasing, and 2.1 bits with context-aware paraphrasing. The 2-bit strategy obtained by training against our context-aware paraphraser achieves a lower un-paraphrased channel capacity, but channel capacity is only reduced by 24% when the context-aware paraphraser is applied."

**ID:** capacity-benchmark
**Location:** Section 5.2, "Verifying ICRL Strategies Against Text Steganography Benchmark"
**Grep command used:** `grep -n "resulted in a 6-bit strategy" literature/extracted/mathew_2024.txt`

---

## Claim 9: Overall verdict — standard mitigations are not robust when optimised against

> "Our experiments of both Section  5.1  and  5.2  show that standard steganography mitigations, including paraphrasing, are not fully robust when optimized against."

**ID:** conclusion-mitigations-not-robust
**Location:** Section 6 Conclusion
**Grep command used:** `grep -n "are not fully robust when optimized against" literature/extracted/mathew_2024.txt`

---

## Claim 10: Builds on Motwani et al. (2024) and Roger & Greenblatt (2023)

> "We build upon  Motwani et al. (2024)  by providing more thorough investigations of emergence of steganographic collusion, including the use of stronger optimization pressures and, crucially, providing a first demonstration that this behaviour can indeed emerge unprompted due to optimization pressure. We build upon  Roger and Greenblatt (2023)"

> "by optimizing schemes against the paraphraser, finding that paraphrasing is not always robust in this setting."

**ID:** builds-on
**Location:** Section 2 Related Work
**Grep command used:** `grep -n "We build upon  Motwani et al. (2024)" literature/extracted/mathew_2024.txt`; `grep -n "by optimizing schemes against the paraphraser" literature/extracted/mathew_2024.txt`

**Refines:** motwani_2024:approach-case-framework (grounded by #builds-on)
**Qualifies:** roger_2023:approach-paraphrase-defence (grounded by #builds-on)

---

## Claim 11: Approach — gradient-based reinforcement learning (GBRL) of a sender and receiver against an overseer

> "When optimizing the collusion team via GBRL, we periodically switch between training of the sender and training of the receiver."

> "The receiver is a pretrained language model with a randomly initialized classification head.
It is trained using supervised fine-tuning (SFT) to take the stegotext generated by the sender and predict the label that maximizes the task reward.
The sender is a pretrained autoregressive LLM which takes the task description as input, and outputs stegotext to be passed to the receiver.
The sender is trained using a reinforcement learning (RL) algorithm to maximize a reward signal  r r  that accounts for task usefuleness and oversight."

> "We use proximal policy optimization (PPO)  ( Schulman et al., 2017 )  with low-rank adaptation (LoRA)  ( Hu et al., 2022 )  to update the  sender   ( Sokota et al., 2022 ) ."

**ID:** approach-gbrl
**Location:** Section 3.3.1 Gradient-based Reinforcement Learning (GBRL)
**Grep command used:** `grep -n "When optimizing the collusion team via GBRL" literature/extracted/mathew_2024.txt`; `grep -n "The receiver is a pretrained language model with a randomly initialized" literature/extracted/mathew_2024.txt`; `grep -n "We use proximal policy optimization (PPO)" literature/extracted/mathew_2024.txt`

---

## Claim 12: Approach — in-context reinforcement learning (ICRL), with centralised and decentralised learners devising strategies in natural language

> "An ICRL Learner is an LLM that devises steganography strategies for the sender and receiver to execute.
Once the sender and receiver execute the strategy (over a number of episodes), the ICRL Learner is fed the results in its context window, including details regarding the task reward  r task r_{\text{task}}  and suspiciousness penalty  r sus r_{\text{sus}}  received.
It then iterates upon the strategy, in order to maximize the reward signal."

> "We make use of two different variations of our ICRL method –  Centralized Learner  where the sender and receiver share a common ICRL Learner, and  Decentralized Learners  where the sender and receiver each have their own independent ICRL Learners."

> "The receiver learner analyzes the sender’s stegotexts from the episodes, and attempts to infer the strategy used by the sender."

**ID:** approach-icrl
**Location:** Section 3.3.2 In-context Reinforcement Learning (ICRL)
**Grep command used:** `grep -n "An ICRL Learner is an LLM that devises" literature/extracted/mathew_2024.txt`; `grep -n "We make use of two different variations of our ICRL method" literature/extracted/mathew_2024.txt`; `grep -n "The receiver learner analyzes the sender" literature/extracted/mathew_2024.txt`

---

## Claim 13: Contribution — elicitation methods that go beyond prompting predefined or self-devised codes

> "Prior work eliciting steganography from LLMs has been limited to prompting the model to follow predefined steganographic codes   ( Roger and Greenblatt, 2023 ;  Greenblatt et al., 2024 )  or to devise codes  ( Wu et al., 2024 ;  Motwani et al., 2024 ) .
We present two optimization methods for stronger automatic elicitation of steganography in LLMs."

**ID:** contribution-beyond-prompted-codes
**Location:** Section 1 Introduction, "Contribution 1"
**Grep command used:** `grep -n "Prior work eliciting steganography from LLMs has been limited" literature/extracted/mathew_2024.txt`
