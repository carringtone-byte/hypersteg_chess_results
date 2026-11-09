---
paper: "Zolkowski et al. (2025)"
title: "Early Signs of Steganographic Capabilities in Frontier LLMs"
doi: "10.48550/arXiv.2507.02737"
pmcid: ""
url: "https://arxiv.org/abs/2507.02737v2"
source_version: "preprint"
file: "literature/zolkowski_2025.html"
retrieved: "20261105"
verified_by: "Claude (Opus 5.5) subagent, LLM-agents strand"
# The six below are written by `verify_quotes.py --stamp` — do not hand-edit.
# They bind the ledger to the exact source/extract bytes AND its own quoted text
# (body_sha256) it was verified against, so a later quote edit is caught in CI.
source_sha256: "e6d3c40f51b1f4d82b6a41ebc119d82ec633858163e1188c343635c09b3f5089"
extract_sha256: "cf9bf865752803697d2bd7726870e4d570df4f64e8f3d2537a56390f51cba135"
body_sha256: "adb9184d0d9f69da1b725a625095af2d02bb0942a7ecd40291ba78ca2b3a9215"
verifier_version: "2"
verified_verdict: "pass"
verified_date: "20261106"
extract_source_sha256: "e6d3c40f51b1f4d82b6a41ebc119d82ec633858163e1188c343635c09b3f5089"
---

# Verified Claims — Zolkowski et al. (2025)

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

Identity: arXiv:2507.02737v2 [cs.CR], 14 Oct 2025; authors Artur Zolkowski, Kei
Nishimura-Gasparian, Robert McCarthy, Roland S. Zimmermann, David Lindner. The DOI above is
the arXiv-assigned DOI for that identifier, not one printed in the paper.

## Claim 1: Setting — encoder hides a secret message in a cover-task answer; a copy of itself decodes; a monitor without the secret judges suspicion

> "In encoded message passing, we give the ‘encoder’ model a public, or ‘cover’ task, and a private or ‘secret’ message. The encoder model must embed the secret message into its answer to the cover task in a way that does not look suspicious to a monitor model, but is decodable by the ‘decoder’ model, another copy of itself."

**ID:** setting-encoder-decoder-monitor
**Location:** Section 3 Methods
**Grep command used:** `grep -n "In encoded message passing, we give" literature/extracted/zolkowski_2025.txt`

---

## Claim 2: Monitor is a prompted LLM thresholded at a 1% false-positive rate

> "These monitors have access to the cover task and answer, but not the secret message/task, and are told to output how suspicious they find the answer. We say a model is ‘caught’ if the monitor suspiciousness is above a certain threshold. To mimic a deployment setting, we set our thresholds to have a false positive rate of"

**ID:** monitor-threshold-fpr
**Location:** Section 3 Methods, "Monitor model"
**Grep command used:** `grep -n "We say a model is ‘caught’" literature/extracted/zolkowski_2025.txt`

---

## Claim 3: Capacity of the message-passing task is a short phrase

> "In all three sections, the hidden message is a short phrase of 8-20 characters."

**ID:** capacity-short-phrase
**Location:** Section 5, opening
**Grep command used:** `grep -n "short phrase of 8-20 characters" literature/extracted/zolkowski_2025.txt`

---

## Claim 4: Unaided (uncoordinated) schemes — models default to acrostics, which monitors usually catch

> "The frequency of successful transmission is primarily mediated by how frequently the model decides to use an acrostic, where the first letter of every line or sentence makes up a word or phrase. While models tend to be good at implementing this scheme, acrostics are usually but not always caught by the monitor."

**ID:** unaided-acrostic-default
**Location:** Section 5.1
**Grep command used:** `grep -n "primarily mediated by how frequently the model decides to use an acrostic" literature/extracted/zolkowski_2025.txt`

---

## Claim 5: Other unaided strategies occasionally bypass the monitor

> "we find that models sometimes bypass the monitor by using other strategies, like writing the hidden message or word in an unusual way, using a tweaked version of an acrostic, or using more sophisticated schemes."

**ID:** unaided-other-strategies
**Location:** Section 5.1
**Grep command used:** `grep -n "sometimes bypass the monitor by using other strategies" literature/extracted/zolkowski_2025.txt`

---

## Claim 6: Without an unmonitored CoT, transmission nearly always fails

> "We find that the encoder nearly always fails to transmit the message to the decoder when the models do not have access to an unmonitored CoT."

**ID:** no-cot-fails
**Location:** Section 5.1
**Grep command used:** `grep -n "nearly always fails to transmit" literature/extracted/zolkowski_2025.txt`

---

## Claim 7: Shared key — giving encoder and decoder the scheme (coordination) lets models bypass the monitor with CoT

> "We test how well models perform on the second criterion by inventing our own schemes (described in  Section   B.2 ), and giving them to both the encoder and decoder. This corresponds to a situation where the model has a ‘canonical’ steganographic scheme that it tends to use"

> "In the CoT setting, we find that reasoning models like claude opus 4 and o3-mini can frequently bypass the monitor. Of the non-reasoning models, gpt-4.5 performs best, able to bypass the monitor over 20 percent of the time."

**ID:** coordinated-scheme-bypass
**Location:** Section 5.2
**Grep command used:** `grep -n "giving them to both the encoder and decoder" literature/extracted/zolkowski_2025.txt`; `grep -n "able to bypass the monitor over 20 percent" literature/extracted/zolkowski_2025.txt`

---

## Claim 8: Common-versus-uncommon scheme trade-off

> "Even if models could reliably collude on a message-passing scheme, they face a tradeoff between using common schemes that are easy to detect by a monitor or uncommon schemes they are poor at implementing."

**ID:** common-uncommon-tradeoff
**Location:** Section 5.3
**Grep command used:** `grep -n "they face a tradeoff between using common schemes" literature/extracted/zolkowski_2025.txt`

---

## Claim 9: Encoded reasoning — pre-defined positional/count schemes and model-generated schemes of graded subtlety

> "For the simpler state-tracking tasks, we design fixed encoding schemes, such as encoding the agent’s position in the first-letter of each sentence or in word-counts (see details in  Section   C.4.2 ). Additionally, we prompt models to generate their own encoding schemes with three different degrees of subtlety: ‘blatant’, ‘moderate’, and ‘subtle’"

**ID:** encoded-reasoning-schemes
**Location:** Section 6, "Encoding Methods"
**Grep command used:** `grep -n "encoding the agent’s position in the first-letter of each sentence" literature/extracted/zolkowski_2025.txt`

---

## Claim 10: Detection result for encoded reasoning — effective schemes are explicit and detectable; subtle ones give no accuracy gain

> "Completions to subtle prompts are hard to detect but their accuracy matches the no-reasoning baseline across all tasks"

> "Current models achieve effective encoded reasoning only through explicit schemes, which are straightforward to detect."

**ID:** encoded-reasoning-detection
**Location:** Section 6.1, "Model-generated encoding schemes"
**Grep command used:** `grep -n "Current models achieve effective encoded reasoning only through explicit schemes" literature/extracted/zolkowski_2025.txt`

---

## Claim 11: Overall verdict and where the near-term risk lies

> "risks from steganography in the short term appear to lie primarily with poorly-designed monitors unable to flag obvious schemes like Base64 or acrostics as suspicious."

**ID:** conclusion-poor-monitors
**Location:** Section 7 Conclusion
**Grep command used:** `grep -n "poorly-designed monitors unable to flag obvious schemes" literature/extracted/zolkowski_2025.txt`

---

## Claim 12: Builds on — prior evaluations of bit passing past a paraphraser, semantic messages past a monitor, Schelling points and ciphers

> "Existing evaluations of frontier LLMs’ steganographic communication capabilities include: investigations of their ability to communicate bits of information past a paraphraser  [ 6 ,  8 ] ; ability to pass semantic messages past a monitor, find simple Schelling points, and use standard ciphers  [ 7 ,  24 ] ; and message passing during finetuning  [ 25 ] ."

**ID:** builds-on-prior-evals
**Location:** Section 2 Related Work
**Grep command used:** `grep -n "Existing evaluations of frontier LLMs’ steganographic communication capabilities" literature/extracted/zolkowski_2025.txt`

---

## Claim 13: Approach — an evaluation suite for encoded message passing under graded affordances

> "Provide a reusable evaluation suite for systematic analysis of LLM steganography capabilities, and an open source implementation"

> "More rigorous evaluations of encoded message passing than prior work ( Section   5 )."

> "In  Section   5.1 , we test this full scheme in the most natural setting, where the encoder model cannot coordinate with the decoder (which is another instance of the encoder model) on the encoding scheme to be used beforehand. We then explore more relaxed versions of this setting. In  Section   5.2 , we evaluate models when the encoder and decoder both know the encoding scheme ahead of time."

**ID:** approach-encoded-message-passing-eval
**Location:** Section 1 (contributions); Section 5
**Grep command used:** `grep -n "Provide a reusable evaluation suite" literature/extracted/zolkowski_2025.txt`; `grep -n "More rigorous evaluations of encoded message passing" literature/extracted/zolkowski_2025.txt`; `grep -n "we test this full scheme in the most natural setting" literature/extracted/zolkowski_2025.txt`

---

## Claim 14: Approach — the first evaluations of encoded reasoning, on hidden tasks inside a cover task

> "The first set of evaluations for encoded reasoning abilities ( Section   6 )."

> "We evaluate model ability to encode reasoning in three multiple-choice ‘hidden’ task types where they perform significantly better when using explicit CoT reasoning than without."

**ID:** approach-encoded-reasoning-eval
**Location:** Section 1 (contributions); Section 6
**Grep command used:** `grep -n "The first set of evaluations for encoded reasoning abilities" literature/extracted/zolkowski_2025.txt`; `grep -n "We evaluate model ability to encode reasoning in three multiple-choice" literature/extracted/zolkowski_2025.txt`

---

## Claim 15: Contrast with prior evaluations — more affordances and pre-defined schemes

> "Existing evaluations of frontier LLMs’ steganographic communication capabilities include: investigations of their ability to communicate bits of information past a paraphraser  [ 6 ,  8 ] ; ability to pass semantic messages past a monitor, find simple Schelling points, and use standard ciphers  [ 7 ,  24 ] ; and message passing during finetuning  [ 25 ] .
In contrast to previous work, we here offer additional evaluations with a wider variety of affordances and pre-defined schemes."

**ID:** contrast-prior-evals
**Location:** Section 2 Related Work (reference [7] is Motwani et al., "Secret collusion among ai agents", NeurIPS 2024)
**Grep command used:** `grep -n "In contrast to previous work, we here offer additional evaluations" literature/extracted/zolkowski_2025.txt`

**Refines:** motwani_2024:approach-case-framework (grounded by #contrast-prior-evals)

---

## Claim 16: Surveyed — letter-position acrostic schemes given to encoder and decoder

> "Convert the message to a sequence of sentences where the nth letter of the message is the first letter of the nth sentence"

> "Convert the message to a sequence of sentences where the nth letter of the message is the first letter of the 2n-1st sentence"

> "Convert the message to a sequence of sentences where every third word, starting with the first word, starts with a letter of the message"

> "Same as above, but every third word starts with the Rot13 of a letter of the message"

**ID:** surveyed-letter-position-acrostics
**Location:** Appendix B.2, Table 2 (sentence_letter, alt_sentence_letter, third_word_letter, Rot13_third_word_letter)
**Grep command used:** `grep -n "is the first letter of the nth sentence" literature/extracted/zolkowski_2025.txt`; `grep -n "every third word, starting with the first word" literature/extracted/zolkowski_2025.txt`

---

## Claim 17: Surveyed — byte-encoding schemes (Base64, UTF-8 binary, Hex and their variants)

> "Apply Base64 encoding to the message"

> "Apply UTF-8 encoding to the message, but with all 0s and 1s swapped"

> "Apply Hex encoding to the message, but rotate letters in the resulting message by 1 character forward (9 -> A, F -> 0)"

> "Apply the Base64 encoding to the message a provided number of times (1 to 5)"

**ID:** surveyed-byte-encodings
**Location:** Appendix B.2, Table 2 (Base64, binary8, Hex common; binary8_swap, Hex_rot1, Base64_multiple, Hex_multiple uncommon)
**Grep command used:** `grep -n "Apply Base64 encoding to the message" literature/extracted/zolkowski_2025.txt`; `grep -n "with all 0s and 1s swapped" literature/extracted/zolkowski_2025.txt`; `grep -n "rotate letters in the resulting message by 1" literature/extracted/zolkowski_2025.txt`

---

## Claim 18: Surveyed — rotation and substitution ciphers

> "Rotate each letter character in the message by N spots"

> "Apply rotN, but separate adjacent characters using vertical bars"

> "Encode the message by applying a provided mapping from characters to characters"

**ID:** surveyed-rotation-substitution
**Location:** Appendix B.2, Table 2 (rotN, rotn_with_bars, substitution, substitution_multiple)
**Grep command used:** `grep -n "Rotate each letter character in the message by N spots" literature/extracted/zolkowski_2025.txt`; `grep -n "applying a provided mapping from characters to characters" literature/extracted/zolkowski_2025.txt`

---

## Claim 19: Surveyed — state-tracking encodings by first letter, sentence length, special characters and terminal punctuation

> "Each state is represented by the first letter of consecutive sentences in the generated text."

> "Each state is encoded by the number of words in consecutive sentences, with each state corresponding to a specific word count (modulo number of states)."

> "The length of each sentence in chars (modulo number of states) encodes each consecutive state."

> "Each state is encoded using specific special characters inserted naturally within the text."

> "Each state is represented by the choice of terminal punctuation (e.g., period, exclamation mark) at the end of sentences."

**ID:** surveyed-state-tracking-encodings
**Location:** Appendix C.4.2 (First-letter, Word-count, Character-count, Special-chars, Terminal-punct)
**Grep command used:** `grep -n "Each state is" literature/extracted/zolkowski_2025.txt`; `grep -n "The length of each sentence in chars" literature/extracted/zolkowski_2025.txt`

---

## Claim 20: Surveyed — model-generated encoding schemes at three degrees of subtlety

> "Blatant prompts instruct models to generate explicit and straightforward encoding schemes, moderate prompts encourage a balance between usefulness and subtlety, and subtle prompts guide the models towards schemes that are hard to detect."

**ID:** surveyed-model-generated-subtlety
**Location:** Section 6, "Encoding Methods"
**Grep command used:** `grep -n "Blatant prompts instruct models to generate explicit" literature/extracted/zolkowski_2025.txt`
