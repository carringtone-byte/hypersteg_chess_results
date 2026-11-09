---
paper: "Rippin et al. (2026)"
title: "Tool Use Enables Undetectable Steganography in Multi-Agent LLM Systems"
doi: "10.48550/arXiv.2606.28425"
pmcid: ""
url: "https://arxiv.org/abs/2606.28425v1"
source_version: "preprint"
file: "literature/rippin_2026.html"
retrieved: "20261105"
verified_by: "Claude (Opus 5.5) subagent, LLM-agents strand"
# The six below are written by `verify_quotes.py --stamp` — do not hand-edit.
# They bind the ledger to the exact source/extract bytes AND its own quoted text
# (body_sha256) it was verified against, so a later quote edit is caught in CI.
source_sha256: "0db977955cf9e0ec109dccbaeabae48e7331306b6cf81d55c1e2daa8af24c0b9"
extract_sha256: "b60040ef097efc851d3734e098051555bc64b52cf9bcf78b84e487ae56a0ab1b"
body_sha256: "bc4a11ac3f92f8b5d6fd20dcf8810108d015bf70d260e852311d01856314a064"
verifier_version: "2"
verified_verdict: "pass"
verified_date: "20261106"
extract_source_sha256: "0db977955cf9e0ec109dccbaeabae48e7331306b6cf81d55c1e2daa8af24c0b9"
---

# Verified Claims — Rippin et al. (2026)

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

Identity: arXiv:2606.28425v1 [cs.CR], 25 Jun 2026; authors Jimmy Laurence Rippin, Simon C.
Marshall, David Demitri Africa, Christian Schroeder de Witt. The DOI above is the
arXiv-assigned DOI for that identifier, not one printed in the paper.

## Claim 1: Core result — tool-using coding agents build undetectable stegosystems; they adapt when ingredients are missing

> "we demonstrate that the complexity of these schemes is no longer a safety barrier, as agentic coding models can already produce undetectable stegosystems when given realistic tool usage, such as code execution or accessing research papers through web searches. Agents also adapt when key ingredients are missing, for example, by adding model-sampling components or implementing related keyed coding schemes."

**ID:** core-tool-use-stegosystems
**Location:** Abstract
**Grep command used:** `grep -n "agentic coding models can already produce undetectable stegosystems" literature/extracted/rippin_2026.txt`

---

## Claim 2: Carrier and key — keyed stegosystem over natural-language model output; security is indistinguishability for a keyless monitor

> "We focus on text-based steganographic channels, where the cover object is natural-language model output."

> "A keyed stegosystem consists of an encoder, a decoder, a payload space, a cover distribution, and a shared secret key."

> "The relevant security notion is not whether the text looks suspicious to a casual reader, but whether a monitor without the key can distinguish stego-objects from ordinary samples drawn from the cover distribution."

**ID:** keyed-stegosystem-carrier
**Location:** Section 2 Background and Problem Setup
**Grep command used:** `grep -n "A keyed stegosystem consists of an encoder" literature/extracted/rippin_2026.txt`; `grep -n "whether a monitor without the key can distinguish" literature/extracted/rippin_2026.txt`

---

## Claim 3: Threat model — the adversary has code execution, a log-probability sub-model and the Zamir (2024) paper; the monitor sees outputs only

> "Access to a sub-model (or API) that returns log probabilities for candidate next tokens, and the ability to call it."

> "Ability to find/derive an undetectable steganography scheme, given that the paper by  Zamir (2024)  is in their file system."

> "Monitor: The defender (human or AI) responsible for detecting and preventing covert channels. Has access to all agent outputs, but not the tool usage or intermediate artefacts."

**ID:** threat-model
**Location:** Section 3.1 Steganographic implementation
**Grep command used:** `grep -n "returns log probabilities for candidate next tokens" literature/extracted/rippin_2026.txt`; `grep -n "Has access to all agent outputs, but not the tool usage" literature/extracted/rippin_2026.txt`

---

## Claim 4: Monitor result — a hidden stegosystem in a multi-agent codebase went undetected by an Opus 4.6 monitor

> "The agent succeeded, although it implemented a different scheme than the one in the paper we gave it, and an Opus 4.6 monitor couldn’t detect the presence of a fully functional stegosystem."

**ID:** monitor-failed-mas
**Location:** Section 4.1 Agent implementations
**Grep command used:** `grep -n "an Opus 4.6 monitor couldn’t detect" literature/extracted/rippin_2026.txt`

---

## Claim 5: Tacit coordination framed as a focal-point problem over algorithms, keys and parameters; salience sources named

> "We treat this as a focal-point coordination problem, where the design space contains many possible steganographic schemes, but some are more salient because they are named in the prompt, present in a shared file system, easy to find on the web, or common in the training distribution."

**ID:** focal-point-salience
**Location:** Section 2, "Tacit coordination"
**Grep command used:** `grep -n "We treat this as a focal-point coordination problem" literature/extracted/rippin_2026.txt`

---

## Claim 6: Coordination result — broad scheme families converge; strict complete coordination on undetectable schemes is zero in their samples

> "Importantly, the models failed to register a non-zero CCI in any undetectable environment: coordination was typically avoided by the presence of some parameter that they never coordinated on"

> "This indicates that first-shot tacit coordination is limited less by choosing a broad scheme family than by matching every decoding-relevant parameter."

**ID:** coordination-bottleneck
**Location:** Section 4.2 Coordination in multi-agent systems; Figure 3 caption
**Grep command used:** `grep -n "failed to register a non-zero CCI" literature/extracted/rippin_2026.txt`; `grep -n "limited less by choosing a broad scheme family" literature/extracted/rippin_2026.txt`

---

## Claim 7: Where the risk is most acute — shared artefacts, repeated interaction, tool-mediated search

> "We find substantial convergence on broad scheme families but limited strict one-shot coordination, suggesting that shared artefacts, repeated interaction, and tool-mediated search are the settings where covert communication risks are most acute."

**ID:** risk-settings
**Location:** Abstract
**Grep command used:** `grep -n "shared artefacts, repeated interaction, and tool-mediated search" literature/extracted/rippin_2026.txt`

---

## Claim 8: Mitigations — monitor tool use; crowd the common knowledge base to blunt Schelling sharpness

> "The most effective mitigation is to monitor tool usage and to move away from methods that skip permissions. Another effective but computationally expensive method is to crowd the common knowledge base with similar implementation descriptions, reducing the Schelling sharpness by introducing new, similarly salient Nash equilibria"

**ID:** mitigations
**Location:** Section 4.3 Mitigations
**Grep command used:** `grep -n "crowd the common knowledge base" literature/extracted/rippin_2026.txt`

---

## Claim 9: Limitations — small sample sizes; Anthropic models only

> "A key limitation of our implementation experiments is the very small sample size."

> "We also only used Anthropic models in these experiments; thus, our claims only apply directly to those"

**ID:** limitations
**Location:** Section 4.4 Limitations
**Grep command used:** `grep -n "very small sample size" literature/extracted/rippin_2026.txt`; `grep -n "We also only used Anthropic models" literature/extracted/rippin_2026.txt`

---

## Claim 10: Builds on — secret collusion (Motwani et al.), provably secure LLM stegosystems, Aharon et al. tacit coordination, strategic confinement hypothesis

> "This risk has been formalised as secret collusion among AI agents, where agents use covert communication to hide the true nature of their interaction from oversight  ( Motwani et al., 2025 ) ."

> "we estimate how often independent agents converge on compatible algorithms and parameters, building on prior work on tacit coordination in LLMs  ( Aharon et al., 2026 ) ."

> "Overall, our findings provide empirical grounding for the recent strategic confinement hypothesis  ( Schroeder de Witt, 2026 ) , a reinterpretation of Lampson’s confinement problem  ( Lampson, 1973 )  for strategic agents"

**ID:** builds-on
**Location:** Section 1 Introduction
**Grep command used:** `grep -n "formalised as secret collusion among AI agents" literature/extracted/rippin_2026.txt`; `grep -n "building on prior work on tacit coordination" literature/extracted/rippin_2026.txt`; `grep -n "reinterpretation of Lampson’s confinement problem" literature/extracted/rippin_2026.txt`

---

## Claim 11: Approach — an agentic covert-channel construction benchmark, seeded with Zamir (2024)

> "First, we introduce an  agentic covert-channel construction  benchmark, where a tool-using LLM must build a working natural-language stegosystem rather than merely describe one (Section  3.1 )."

> "Both the task and paper are contained in the file system accessible to the agent, along with a virtual environment containing the necessary packages, and a file containing model log probabilities with some example usage code."

> "In each experiment, the agent is provided with the paper by  Zamir (2024)  unless otherwise stated."

**ID:** approach-agentic-covert-channel-construction
**Location:** Section 1 (contributions); Section 4.1 Agent implementations
**Grep command used:** `grep -n "we introduce an  agentic covert-channel construction" literature/extracted/rippin_2026.txt`; `grep -n "Both the task and paper are contained in the file system" literature/extracted/rippin_2026.txt`; `grep -n "the agent is provided with the paper by  Zamir (2024)" literature/extracted/rippin_2026.txt`

**Depends-on:** zamir_2024:approach-undetectable-llm-stego (grounded by #approach-agentic-covert-channel-construction)

---

## Claim 12: Approach — tacit steganographic agreement as Schelling coordination, measured by algorithm, hyperparameter and complete coordination indices

> "Second, we frame  tacit steganographic agreement  as a Schelling-point coordination problem over algorithms, keys, and decoding-relevant parameters (Section  3.2.1 )."

> "Agents select identical stegosystems and hyperparameters. To obtain a good approximation with a small sample size, we calculate the rate of complete coordination by multiplying the rate of coordination on each hyperparameter for a given algorithm."

> "The CCI is our approximation of Schelling sharpness."

> "We adapt the code from  Aharon et al. (2026)  by adding a steganography planning experiment, where the agent is instructed to implement a steganographic system to communicate with a partner; agents are told the problem specification and to return their chosen scheme, including their exact hyper"

**ID:** approach-tacit-stego-agreement-cci
**Location:** Section 1 (contributions); Section 3.2; Section 4.2
**Grep command used:** `grep -n "we frame  tacit steganographic agreement" literature/extracted/rippin_2026.txt`; `grep -n "we calculate the rate of complete coordination" literature/extracted/rippin_2026.txt`; `grep -n "The CCI is our approximation of Schelling sharpness" literature/extracted/rippin_2026.txt`; `grep -n "We adapt the code from  Aharon et al. (2026)" literature/extracted/rippin_2026.txt`

**Refines:** aharon_2026:approach-focal-point-evaluation (grounded by #builds-on)
