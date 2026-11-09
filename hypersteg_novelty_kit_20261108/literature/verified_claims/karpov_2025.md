---
paper: "Karpov et al. (2025)"
title: "The Steganographic Potentials of Language Models"
doi: "10.48550/arXiv.2505.03439"
pmcid: ""
url: "https://arxiv.org/abs/2505.03439v1"
source_version: "preprint"
file: "literature/karpov_2025.html"
retrieved: "20261105"
verified_by: "Claude (Opus 5.5) subagent, LLM-agents strand"
# The six below are written by `verify_quotes.py --stamp` — do not hand-edit.
# They bind the ledger to the exact source/extract bytes AND its own quoted text
# (body_sha256) it was verified against, so a later quote edit is caught in CI.
source_sha256: "51c2f951feea93f74ee99bb9de7d957aef5d137cf2fe7c25888585349f044cbd"
extract_sha256: "3f3614d6eb88545ecc5d3d7373c597642fd9acf08a1ee9021bb3eb7cb08a9ae3"
body_sha256: "2bbbcdb693de6664bbfca48f53980030f958d1174bfa0baf8709f5724449ebba"
verifier_version: "2"
verified_verdict: "pass"
verified_date: "20261106"
extract_source_sha256: "51c2f951feea93f74ee99bb9de7d957aef5d137cf2fe7c25888585349f044cbd"
---

# Verified Claims — Karpov et al. (2025)

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

Identity: arXiv:2505.03439v1 [cs.AI], 06 May 2025; authors Artem Karpov, Tinuade Adeleke,
Seong Hah Cho, Natalia Pérez-Campanero Antolín (Apart Research). The DOI above is the
arXiv-assigned DOI for that identifier, not one printed in the paper.

## Claim 1: Scope — RL fine-tuning and prompting to develop, execute and spontaneously use steganography

> "We explore the steganographic capabilities of LLMs fine-tuned via reinforcement learning (RL) to: (1) develop covert encoding schemes, (2) engage in steganography when prompted, and (3) utilize steganography in realistic scenarios where hidden reasoning is likely, but not prompted."

**ID:** scope-rl-and-prompting
**Location:** Abstract
**Grep command used:** `grep -n "develop covert encoding schemes" literature/extracted/karpov_2025.txt`

---

## Claim 2: Colours experiment — unkeyed codebook (colour to proper name) learnt by RL with no hints

> "This represents pure steganography, as opposed to steganography involving symmetric or public keys."

> "Specifically, the encoder is given possible colors,"

> "We don’t give any hints about how to do such a mapping to encoder or decoder."

**ID:** colours-codebook-pure-stego
**Location:** Section 3.1 Colors Experiment
**Grep command used:** `grep -n "This represents pure steganography" literature/extracted/karpov_2025.txt`; `grep -n "We don’t give any hints" literature/extracted/karpov_2025.txt`

---

## Claim 3: Colours experiment did not converge

> "Our preliminary experiments did not converge even with a simplified setup involving only two colors and two names."

**ID:** colours-no-convergence
**Location:** Section 4.1
**Grep command used:** `grep -n "did not converge even with a simplified setup" literature/extracted/karpov_2025.txt`

---

## Claim 4: Direct steganography fine-tuning — payload hidden in a news summary under an overseer; all agents know the payload set

> "Here, the sender must summarize a news article from the Wikinews dataset  ( Mal,  )  while occasionally embedding a payload (e.g. a network protocol such as TCP or UDP), and the receiver must recover this payload, if present, using the same article and the sender’s message."

> "All agents—encoder, decoder, and overseer—are informed of the possible payloads via their prompts."

**ID:** direct-finetune-summary-carrier
**Location:** Section 3.2
**Grep command used:** `grep -n "summarize a news article from the Wikinews dataset" literature/extracted/karpov_2025.txt`; `grep -n "informed of the possible payloads" literature/extracted/karpov_2025.txt`

---

## Claim 5: Capacity — about 20% gain at 3 bits of entropy; coding by semantic association

> "models could improve their covert communication on a held-out validation dataset by about 20 % for 3 bits of entropy, but less in other cases."

> "random samples of successful transmissions indicate that the model often exploits a weakness in the overseer by replacing the payload with a closely associated term. For example, the payload ‘MQTT’ (an internet protocol name) might be embedded using the phrase ‘Mosquitto Paris,’ referencing Mosquitto—a popular MQTT implementation."

**ID:** capacity-semantic-association
**Location:** Section 4.2
**Grep command used:** `grep -n "by about 20 % for 3 bits of entropy" literature/extracted/karpov_2025.txt`; `grep -n "replacing the payload with a closely associated term" literature/extracted/karpov_2025.txt`

---

## Claim 6: Prompted schemes — synonym-substitution algorithm given to encoder and decoder, not the overseer

> "we modify the setup to include a set of instructions specifying the synonym-based encoding and decoding schemes (see Appendix  B ) as part of the common knowledge of the encoder and decoder but not the overseer."

**ID:** synonym-scheme-given
**Location:** Section 3.3, Direct Steganography
**Grep command used:** `grep -n "specifying the synonym-based encoding and decoding schemes" literature/extracted/karpov_2025.txt`

---

## Claim 7: Synonym scheme degrades with payload length because sender and receiver disagree on replaceable words

> "as the payload length increases (and consequently the covertext length grows), the encoder and decoder struggle to consistently agree on a set of replaceable words in the covertext."

**ID:** synonym-length-degrades
**Location:** Section 4.3
**Grep command used:** `grep -n "struggle to consistently agree on a set of replaceable words" literature/extracted/karpov_2025.txt`

---

## Claim 8: Unaided schemes — first letters of words

> "the gpt-4o and o1-preview models often embed their payloads in the first letters of words during encoding, enabling the decoder to retrieve the information while deceiving the overseer with the overall coherence of the message."

**ID:** unaided-first-letters
**Location:** Section 4.3
**Grep command used:** `grep -n "embed their payloads in the first letters of words" literature/extracted/karpov_2025.txt`

---

## Claim 9: Coordination by pre-exchange of messages, and indirect (unprompted) steganography in a game

> "the set-up is modified differently to allow for exchange of messages between the encoder and decoder prior to encoding and decoding payloads, enabling the coordination of their strategy."

> "o1-preview attempted steganography 215 times out of 500, across 100 games of five rounds each."

**ID:** coordination-and-game-intent
**Location:** Sections 3.3 and 4.3
**Grep command used:** `grep -n "allow for exchange of messages between the encoder and decoder" literature/extracted/karpov_2025.txt`; `grep -n "attempted steganography 215 times" literature/extracted/karpov_2025.txt`

---

## Claim 10: Paraphrase robustness — the paper cites others' finding that schemes fail under paraphrasing

> "Payload capacity is constrained, and encoding schemes are often brittle—as shown by failing under paraphrasing or text normalization in some studies"

**ID:** paraphrase-brittle-cited
**Location:** Section 5.1 Real-World Implications and Limitations
**Grep command used:** `grep -n "encoding schemes are often brittle" literature/extracted/karpov_2025.txt`

---

## Claim 11: Builds on — Simmons' prisoners' problem, Motwani et al., Roger & Greenblatt, Mathew et al.; extends to multi-bit payloads with RL on both roles

> "Unlike these studies, our work fine-tunes both sender and receiver on hidden messages with more than one bit of entropy."

> "This scenario, reminiscent of the prisoners’ problem  ( Simmons,  ) , requires the sender to summarize a news article while covertly embedding secret escape details."

**ID:** builds-on
**Location:** Section 2 Related Work; Section 3.2
**Grep command used:** `grep -n "fine-tunes both sender and receiver" literature/extracted/karpov_2025.txt`; `grep -n "reminiscent of the prisoners’ problem" literature/extracted/karpov_2025.txt`

---

## Claim 12: Approach — the colours experiment, an RL-learnt unkeyed mapping without step-by-step reasoning

> "We introduce the colors experiment to evaluate whether LLMs can learn steganography, during RL, that does not require explicit, step-by-step reasoning. Instead, the model acquires hidden cues that enable the rapid encoding and decoding of hidden messages (payloads)."

**ID:** approach-colours-rl
**Location:** Section 3.1 Colors Experiment
**Grep command used:** `grep -n "We introduce the colors experiment" literature/extracted/karpov_2025.txt`

---

## Claim 13: Approach — RLOO fine-tuning of sender and receiver to carry a payload in a news summary under an overseer

> "This experiment evaluates the model’s ability to embed and retrieve payloads using step-by-step reasoning under reinforcement learning pressure."

> "we fine-tune a model with RLOO to encode and decode a payload without explicit instructions for either process."

> "The overseer flags any suspicious message with a -1.0 score, while a successful decoding earns a score of 1.0. Summarization is evaluated separately, penalizing the encoder with -0.1 for an invalid summary."

**ID:** approach-rloo-summary-stego
**Location:** Section 3.2
**Grep command used:** `grep -n "embed and retrieve payloads using step-by-step reasoning" literature/extracted/karpov_2025.txt`; `grep -n "we fine-tune a model with RLOO" literature/extracted/karpov_2025.txt`

---

## Claim 14: Approach — prompted evaluation of frontier models in direct, instructed, coordinated and game scenarios

> "We evaluate current capabilities of LLMs to perform steganography without additional fine-tuning via prompting. We explore different steganography scenarios, including direct encoding with and without structured instructions, and indirect steganography in a competitive game context, as outlined below. For the overseer, we use GPT-4o-Mini and evaluate frontier models GPT-4o, Claude-3-5-sonnet, and o1 in both encoder and decoder roles (see Fig.  1 )."

**ID:** approach-prompted-stego-eval
**Location:** Section 3.3
**Grep command used:** `grep -n "We evaluate current capabilities of LLMs to perform steganography without additional fine-tuning" literature/extracted/karpov_2025.txt`

---

## Claim 15: Approach — the indirect guess game, in which an assistant may hide letters to help one team past an overseer

> "Steganography in a game scenario (Indirect Steganography)  To explore how steganographic behavior might emerge as an instrumental goal, we prompted LLMs with tasks using a plausible scenario where covert collusion would be advantageous."

> "The scenario is a game between Team A and B, where each team must guess a random sequence of letters. An AI assistant is tasked with the goal of helping Team A but not Team B. The AI has knowledge of the correct letters and the scores of both teams but is prohibited from directly sharing the letters with Team A. An overseer monitors all communications and penalizes Team A if it detects the AI sharing information."

**ID:** approach-indirect-guess-game
**Location:** Section 3.3, "Steganography in a game scenario"
**Grep command used:** `grep -n "To explore how steganographic behavior might emerge as an instrumental goal" literature/extracted/karpov_2025.txt`; `grep -n "The scenario is a game between Team A and B" literature/extracted/karpov_2025.txt`

---

## Claim 16: Extends Mathew et al. — both roles fine-tuned on payloads of more than one bit

> "In  Mathew et al. () , they found a gradient based method to elicit indirect steganography for transmitting 1 bit of information with SFT for a decoder (binary classifier) and RL (Proximal Policy Optimization) for an encoder. Here, they red team steganography mitigation strategies using the method based on in-context learning. Unlike these studies, our work fine-tunes both sender and receiver on hidden messages with more than one bit of entropy."

**ID:** extends-mathew-multibit
**Location:** Section 2 Related Work
**Grep command used:** `grep -n "they found a gradient based method to elicit indirect steganography" literature/extracted/karpov_2025.txt`

**Refines:** mathew_2024:approach-gbrl (grounded by #extends-mathew-multibit)
