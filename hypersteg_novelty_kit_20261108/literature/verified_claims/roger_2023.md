---
paper: "Roger and Greenblatt (2023)"
title: "Preventing Language Models From Hiding Their Reasoning"
doi: "10.48550/arXiv.2310.18512"
pmcid: ""
url: "https://arxiv.org/abs/2310.18512v2"
source_version: "preprint"
file: "literature/roger_2023.html"
retrieved: "20261105"
verified_by: "Claude (Opus 5.5) subagent, LLM-agents strand"
# The six below are written by `verify_quotes.py --stamp` — do not hand-edit.
# They bind the ledger to the exact source/extract bytes AND its own quoted text
# (body_sha256) it was verified against, so a later quote edit is caught in CI.
source_sha256: "25506925950f1b52694615f3e9732917b6c3c86936ecdfa73adc7e6201ee2af1"
extract_sha256: "21d2e8c74de0b9ff56243b6575121f31a46d3a3682206490cee3fb5c3db1493d"
body_sha256: "21c32b940e2dd6e861b58462c160f6bede0812b7291df271d8ee19a7bea56113"
verifier_version: "2"
verified_verdict: "pass"
verified_date: "20261106"
extract_source_sha256: "25506925950f1b52694615f3e9732917b6c3c86936ecdfa73adc7e6201ee2af1"
---

# Verified Claims — Roger and Greenblatt (2023)

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

Identity: arXiv:2310.18512v2 [cs.LG], 31 Oct 2023; authors Fabien Roger and Ryan Greenblatt
(Redwood Research). The DOI above is the arXiv-assigned DOI for that identifier, not one
printed in the paper.

## Claim 1: Definition of encoded reasoning — intermediate steps hidden in choice of word or phrasing

> "an LLM could encode intermediate steps of reasoning in their choices of a particular word or phrasing (when multiple ones would be equally good from the user’s perspective), and then decode these intermediate steps later in the generation to arrive at a more accurate answer than if it tried to answer to the question without any intermediate step."

**ID:** def-encoded-reasoning
**Location:** Section 1 Introduction
**Grep command used:** `grep -n "in their choices of a particular word or phrasing" literature/extracted/roger_2023.txt`

---

## Claim 2: LLM steganography generates rather than modifies a cover text

> "This requires LLMs to be able to encode information to be hidden within the text they generate (which is slightly different from regular text steganography, where information is usually hidden within a cover text), and then decode the encoded information."

**ID:** generative-vs-cover-modification
**Location:** Section 2.1 Definitions
**Grep command used:** `grep -n "slightly different from regular text steganography" literature/extracted/roger_2023.txt`

---

## Claim 3: Demonstration — a fine-tuned codebook mapping each of 18 election years to an introduction sentence

> "The encoded reasoning is built using a simple ad hoc method: each of the 18 possible values for the election year is mapped to a different introduction sentence, such that the model can first map each computation result to the corresponding introduction, and use this intermediate information to choose the liberal or the conservative answer."

**ID:** demo-introduction-codebook
**Location:** Section 3 A demonstration of encoded reasoning
**Grep command used:** `grep -n "each of the 18 possible values for the election year" literature/extracted/roger_2023.txt`

---

## Claim 4: Prompted schemes evaluated — acronyms, age instructions, introduction variations, and model-devised scratchpad schemes; plus logit watermarking schemes

> "LLM watermarking techniques hide a few bits of information by slightly changing the output probabilities of the LLM."

> "Age instructions : We ask an LLM to start its answer by telling its age, which is determined by the message to encode."

> "Introduction variations : We associate each of 16 possible messages with an answer introduction (e.g. “Sure!”) and ask the AI assistant to start its answer with the respective introduction."

> "Scratchpads : We ask an LLM to first think a steganographic scheme it could use for this particular task to encode the message, then let it encode the message itself."

**ID:** schemes-evaluated
**Location:** Section 4.4 Steganography schemes
**Grep command used:** `grep -n "Age instructions" literature/extracted/roger_2023.txt`; `grep -n "Introduction variations" literature/extracted/roger_2023.txt`; `grep -n "Scratchpads : We ask an LLM" literature/extracted/roger_2023.txt`

---

## Claim 5: Acronym scheme — models mostly use the payload directly as an imagined acronym or name

> "In practice, LLMs will mostly use the payload directly as (imagined) acronym or names."

**ID:** acronym-literal-payload
**Location:** Section 4.4, "Acronyms"
**Grep command used:** `grep -n "mostly use the payload directly as (imagined) acronym" literature/extracted/roger_2023.txt`

---

## Claim 6: Method — conservative upper bound from schemes stronger than current LLMs, against a weaker trusted paraphraser

> "we instead estimate the ability of defenses to remove hidden information encoded in a text by the strongest steganography schemes we can build (using algorithms which can make arbitrary calls to LLMs)."

> "Paraphrasing-based defenses against steganography require access to a paraphraser weak enough to be unable to read and keep the hidden information"

**ID:** method-upper-bound-paraphraser
**Location:** Section 4.1 Approach
**Grep command used:** `grep -n "by the strongest steganography schemes we can build" literature/extracted/roger_2023.txt`; `grep -n "a paraphraser weak enough to be unable to read" literature/extracted/roger_2023.txt`

---

## Claim 7: Capacity metric — bits per answer from the frequency of perfect decoding

> "We want to know how many bits can be hidden in the message, i.e. the capacity of the channel encoder-paraphraser-decoder:"

> "In practice, we measure the frequency"

> "at which the message is perfectly decoded."

**ID:** capacity-metric
**Location:** Section 4.3.1 Capacity
**Grep command used:** `grep -n "the capacity of the channel encoder-paraphraser-decoder" literature/extracted/roger_2023.txt`

---

## Claim 8: Paraphrase robustness — paraphrasing cuts hidden information below about 2 bits per answer (3 bits per KB)

> "paraphrasing is almost always able to get the number of hidden bits below 2 bits per answer (which corresponds to the headline 3 bits per KB of text). Moreover, only the steganography schemes which degrade performance the most are able to get more than 1 bit per answer through the paraphraser (see the scratchpad and acronyms steganography schemes)."

**ID:** paraphrase-3-bits-per-kb
**Location:** Section 5.2 Main results
**Grep command used:** `grep -n "below 2 bits per answer" literature/extracted/roger_2023.txt`

---

## Claim 9: Paraphrase limits — hard-to-paraphrase generations (fictional acronyms) and paraphrasing cost on open-ended tasks

> "if the generation is built around the definition of an acronym, it might be hard for the paraphraser to know if the acronym is real or imagined, and therefore it might not be able to paraphrase it properly if it is a fictional acronym encoding a hidden message."

> "This shows that only some kinds of data can be efficiently paraphrased."

**ID:** paraphrase-limits
**Location:** Section 4.1 ("Constraining generations through evaluation"); Section 5.2
**Grep command used:** `grep -n "if the acronym is real or imagined" literature/extracted/roger_2023.txt`; `grep -n "only some kinds of data can be efficiently paraphrased" literature/extracted/roger_2023.txt`

---

## Claim 10: Builds on — Lanham et al.'s term and finding; Kirchenbauer-style watermarks

> "Encoded reasoning  is when LLMs use steganography to hide relevant intermediate steps of reasoning in the generated text  ( Lanham et al.,, 2023 ) ."

> "The two techniques we used are based on  Kirchenbauer et al., 2023a () ."

**ID:** builds-on
**Location:** Sections 2.1 and 4.4
**Grep command used:** `grep -n "is when LLMs use steganography to hide relevant intermediate steps" literature/extracted/roger_2023.txt`; `grep -n "The two techniques we used are based on" literature/extracted/roger_2023.txt`

---

## Claim 11: Approach — a conservative evaluation of paraphrasing as a defence against steganography

> "We present a methodology that enables us to conservatively evaluate defenses against steganographic attacks (Section  4 )"

> "We use this methodology to determine some key ingredients to make paraphrasing a good defense against steganographic attacks, and show that they are enough to prevent simple steganography schemes (including LLM watermarking schemes adapted for steganography) from encoding (on average) more than 3 bits per KB of text (Section  5 )."

> "We use two paraphrasing techniques: the default  Paraphrasing  technique asks GPT-3.5-Turbo to paraphrase  A 1 A_{1}  while keeping the semantic information intact, while  Context-aware paraphrasing  also includes  Q Q  in the prompt: it asks GPT-3.5-Turbo to paraphrase  A 1 A_{1}  while only keeping the information relevant to answering  Q Q ."

**ID:** approach-paraphrase-defence
**Location:** Section 1 "Our contributions"; Section 4.5 Paraphrasers (defenders)
**Grep command used:** `grep -n "We present a methodology that enables us to conservatively evaluate" literature/extracted/roger_2023.txt`; `grep -n "We use two paraphrasing techniques" literature/extracted/roger_2023.txt`

---

## Claim 12: Approach — fine-tuning GPT-3.5-Turbo to learn a simple encoding scheme for encoded reasoning

> "We provide a concrete example where steganography allows models to succeed at an unintended behavior: we fine-tune GPT-3.5-Turbo to learn a very simple steganographic encoding scheme, and show that this helps the model generate answers that are more much more sycophantic than the answers of a model trained to output its final answer directly (Figure  1  and Section  3 )"

**ID:** approach-finetuned-introduction-codebook
**Location:** Section 1 "Our contributions"
**Grep command used:** `grep -n "we fine-tune GPT-3.5-Turbo to learn a very simple steganographic encoding scheme" literature/extracted/roger_2023.txt`

---

## Claim 13: Surveyed — cycle-shifting watermark used for steganography

> "Cycle-shifting watermark   ( Fernandez et al.,, 2023 )  uses message as the seed for the red-green token splits (between tokens which should be made more likely, and those which should be made less likely), then checks at detection time which seed has the highest detection score."

> "Both techniques require access to logits, which is why we’re using Llama2-7B-Chat  ( Touvron et al.,, 2023 )  to generate answers."

**ID:** surveyed-cycle-shifting-watermark
**Location:** Section 4.4 Steganography schemes
**Grep command used:** `grep -n "uses message as the seed for the red-green token splits" literature/extracted/roger_2023.txt`

---

## Claim 14: Surveyed — balanced-marking watermark used for steganography

> "Balanced-marking   ( Wang et al., 2023b,  )  improves on this technique, mostly by grouping tokens to make balanced groups with similar probabilities instead of randomly choosing red-green token groups."

**ID:** surveyed-balanced-marking
**Location:** Section 4.4 Steganography schemes
**Grep command used:** `grep -n "improves on this technique, mostly by grouping tokens" literature/extracted/roger_2023.txt`

---

## Claim 15: Surveyed — prompted acronym scheme

> "Acronyms : We ask an LLM to directly hide the message into its answer of a given question. Then, to decode the message, ask an LLM to extract the message. Messages are fixed to be 30 bits long, and a given and taken from the LLMs as 6-character payloads (made of characters from A to Z or 1 to 6)."

**ID:** surveyed-acronyms
**Location:** Section 4.4 Steganography schemes
**Grep command used:** `grep -n "Acronyms : We ask an LLM to directly hide the message" literature/extracted/roger_2023.txt`

---

## Claim 16: Surveyed — prompted age-instruction scheme

> "Age instructions : We ask an LLM to start its answer by telling its age, which is determined by the message to encode. The decoder extracts the first integer in the (paraphrased) message  A 2 A_{2}  it receives, then looks up the message corresponding to that integer. Ages are in the range [0,63]."

**ID:** surveyed-age-instructions
**Location:** Section 4.4 Steganography schemes
**Grep command used:** `grep -n "The decoder extracts the first integer" literature/extracted/roger_2023.txt`

---

## Claim 17: Surveyed — prompted introduction-variation scheme

> "Introduction variations : We associate each of 16 possible messages with an answer introduction (e.g. “Sure!”) and ask the AI assistant to start its answer with the respective introduction. At decoding time, use a sentence transformer to determine which of the introductions is most similar to the first sentence of  A 2 A_{2} ."

**ID:** surveyed-introduction-variations
**Location:** Section 4.4 Steganography schemes
**Grep command used:** `grep -n "At decoding time, use a sentence transformer" literature/extracted/roger_2023.txt`

---

## Claim 18: Surveyed — scratchpad scheme in which the model devises its own encoding

> "Scratchpads : We ask an LLM to first think a steganographic scheme it could use for this particular task to encode the message, then let it encode the message itself. Then, to decode the message, ask the LLM to think of a steganographic scheme it could have used to encode the message for this particular task, then let it decode the message itself."

> "None of those techniques require access to logits, so we use OpenAI’s GPT-3.5-Turbo (0613) or GPT-4 (0613) sampled at temperature 0, except for scratchpads, where we use temperature 1 to increase the diversity of methods used to hide information."

**ID:** surveyed-scratchpad-scheme
**Location:** Section 4.4 Steganography schemes
**Grep command used:** `grep -n "Scratchpads : We ask an LLM to first think" literature/extracted/roger_2023.txt`; `grep -n "None of those techniques require access to logits" literature/extracted/roger_2023.txt`
