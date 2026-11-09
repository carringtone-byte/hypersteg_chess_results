---
paper: "Schulz, Fülle and Fruengel (2026)"
title: "Learning Steganography Is Easy, Learning Steganographic Reasoning Is Hard"
doi: "10.48550/arXiv.2609.39838"
pmcid: "<PMC ID, if any>"
url: "<source URL the file was fetched from>"
source_version: "preprint"
file: "literature/schulz_2026.html"
retrieved: "20261105"
verified_by: "Claude (Opus 5.5) subagent, quotes checked with verify_quotes.py (read-only run)"
# The six below are written by `verify_quotes.py --stamp` — do not hand-edit.
# They bind the ledger to the exact source/extract bytes AND its own quoted text
# (body_sha256) it was verified against, so a later quote edit is caught in CI.
source_sha256: "c0644eeccd9b8d7679703a49983d9bca41ce6521c4b590021c1bed4b299c44af"
extract_sha256: "bfe27cf78e93354f646634bd80ee52d9100e209e54630e2cb0e4e1a39713a2ad"
body_sha256: "16ec08978e25d80ca276924ade25ac2c50354ea9b92d53724007af9b4a7dec79"
verifier_version: "2"
verified_verdict: "pass"
verified_date: "20261106"
extract_source_sha256: "c0644eeccd9b8d7679703a49983d9bca41ce6521c4b590021c1bed4b299c44af"
---

# Verified Claims — Schulz, Fülle and Fruengel (2026)

Each claim below was extracted by reading the downloaded paper file with the Read
tool, grepping for the specific content, and reading the surrounding context to
confirm the attribution is faithful.

Source: arXiv:2609.39838v1 [cs.AI], 30 Sep 2026 (arXiv HTML rendering); workshop paper,
Trustworthy AI for Good (AI4GOOD). Authors: Meridian Cambridge and SAIGE. The paper
measures whether models can learn steganography; it proposes no new channel.

## Claim 1: Three behaviours distinguished — steganographic messaging, encoded reasoning, and steganographic reasoning (computing inside text that looks like an answer to another task)

> "messaging hides given values in innocuous text; encoded reasoning computes step by step in an illegible but unconcealed format; steganographic reasoning computes inside text that looks like an innocuous answer to an unrelated task."

> "we define steganographic reasoning as using a scratchpad to reason about one topic while making the text look as though it reasons about another"

**ID:** three-behaviours
**Location:** Figure 1 caption; Section 1 "Introduction"
**Grep command used:** `Grep pattern="messaging hides given values|we define steganographic reasoning as" path="literature/extracted/schulz_2026.txt"`

---

## Claim 2: Headline result — messaging and encoded reasoning are learned under RL, in-context learning and SFT; steganographic reasoning mostly only under SFT, at 2.4 to 20 times the training

> "For most tasks, models learn steganographic reasoning only under SFT, while they learn steganographic messaging and encoded reasoning under all three elicitation methods."

> "under SFT it can be learned, but takes  2.4 2.4  to  20 20  times as many training steps as messaging where it succeeds, and for several model–task combinations it was never learned within our budgets."

**ID:** stego-reasoning-hard
**Location:** Abstract; Section 1 "Introduction"
**Grep command used:** `Grep pattern="models learn steganographic reasoning only under SFT|times as many training steps as messaging" path="literature/extracted/schulz_2026.txt"`

---

## Claim 3: Carriers and encodings — task-agnostic surface-formatting schemes (capitalisation, markdown, whitespace, per-sentence markers), one symbol per unit, meaning untouched; plus a knapsack cover

> "The six surface-formatting schemes encode one symbol per unit (word, whitespace run, or sentence) from the start of the answer and leave the meaning of the text untouched"

> "the in/out choices of its first items can encode a number in binary, one bit per item (the  knapsack cover )."

**ID:** formatting-and-knapsack-carriers
**Location:** Section 2.5 "Encoding schemes", Table 1; Section 2.4 "Main tasks"
**Grep command used:** `Grep pattern="The six surface-formatting schemes|one bit per item" path="literature/extracted/schulz_2026.txt"`

---

## Claim 4: Shared knowledge and access — the encoding scheme is given in the prompt (or designed by the model); for model-designed schemes a fresh instance of the same model, given the output and scheme description, decodes

> "RL on a given scheme.  We use GRPO  ( Shao et al., 2024 )  on Tinker  ( Thinking Machines Lab, 2025 )  with Qwen3.6-35B-A3B"

> "Such a scheme cannot be decoded programmatically, so the same model, in a fresh context given only the output and the scheme description, acts as decoder"

**ID:** shared-scheme-decoder
**Location:** Section 2.8 "Elicitation setups"
**Grep command used:** `Grep pattern="RL on a given scheme|in a fresh context given only the output" path="literature/extracted/schulz_2026.txt"`

---

## Claim 5: Monitor and detection threshold — GPT-5-mini scores suspiciousness 1–10 on the cover text; "covert" means a score of at most 3

> "The monitor, GPT-5-mini (Table  S1 ), sees the cover text with the readout line stripped and assigns a suspiciousness score from  1 1  to  10 10"

> "We call an output  covert  when its suspiciousness is at most  3 3 , a threshold we justify in Appendix  E ."

**ID:** gpt5mini-monitor-covert
**Location:** Section 2.6 "Monitor and suspiciousness"
**Grep command used:** `Grep pattern="The monitor, GPT-5-mini|We call an output" path="literature/extracted/schulz_2026.txt"`

---

## Claim 6: How recovery is measured — encoding accuracy (fraction of intermediate values decodable), side-task answer accuracy against a no-CoT baseline, and error injection

> "Encoding accuracy  is the fraction of the side task’s intermediate values that can be correctly decoded from the model’s answer."

> "only side-task accuracy above that baseline shows that the computation went through the encoding channel rather than happening latently."

**ID:** recovery-metrics
**Location:** Section 2.7 "Metrics"
**Grep command used:** `Grep pattern="is the fraction of the side task|only side-task accuracy above that baseline" path="literature/extracted/schulz_2026.txt"`

---

## Claim 7: In-context learning — for messaging several model–scheme pairs are both covert and accurate; for steganographic reasoning a model is either covert or accurate, not both

> "For messaging, several model-scheme pairs are both covert and accurate (Figure  3 a); for steganographic reasoning, essentially none are (Figure  3 b): a model is either covert or accurate, not both."

> "under steganographic reasoning the first few values are encoded correctly and the rest are chance, while under messaging every position stays near 100%."

**ID:** icl-covert-or-accurate
**Location:** Section 3.1 "In-context learning"
**Grep command used:** `Grep pattern="several model-scheme pairs are both covert|the first few values are encoded correctly" path="literature/extracted/schulz_2026.txt"`

---

## Claim 8: Frontier success on the knapsack cover — GPT-5.5 alone of nine models reasons steganographically over 24 steps, 92 % side-task accuracy against a 46 % no-CoT baseline

> "Here GPT-5.5 succeeds, alone among the nine models: its per-position encoding accuracy stays at 100% across all 24 steps"

> "with side-task accuracy at 92% against a 46% no-CoT baseline (chance 50%,"

**ID:** gpt55-knapsack-success
**Location:** Section 3.1 "In-context learning"
**Grep command used:** `Grep pattern="Here GPT-5.5 succeeds|with side-task accuracy at 92%" path="literature/extracted/schulz_2026.txt"`

---

## Claim 9: Reinforcement learning — reward is decoded encoding accuracy discounted by monitor suspiciousness; messaging learned in about 100 steps, steganographic reasoning plateaus at 69 %

> "Each episode is rewarded for its programmatically decoded encoding accuracy, discounted linearly by monitor suspiciousness"

> "Encoded reasoning is learned almost immediately and messaging within about a hundred RL steps, both reaching near-perfect encoding accuracy"

> "Steganographic reasoning is never learned reliably: it plateaus at 69% encoding accuracy at its last evaluation, step 760"

**ID:** rl-results
**Location:** Section 2.8 "Elicitation setups"; Section 3.2 "Reinforcement learning"
**Grep command used:** `Grep pattern="Each episode is rewarded|messaging within about a hundred RL steps|plateaus at 69%" path="literature/extracted/schulz_2026.txt"`

---

## Claim 10: Outcome-only reward — with only the final bit rewarded, the larger Qwen3.5-397B-A17B adopts the encoding on its own as a means to the answer

> "the much larger Qwen3.5-397B-A17B reaches 100% final-answer accuracy by step 30, per-position encoding accuracy rising to 100% alongside it though never rewarded"

> "the model adopts the given encoding on its own as a means of getting the final bit right."

**ID:** outcome-only-rl-adoption
**Location:** Section 3.2 "Reinforcement learning"
**Grep command used:** `Grep pattern="reaches 100% final-answer accuracy by step 30|adopts the given encoding on its own" path="literature/extracted/schulz_2026.txt"`

---

## Claim 11: Model-designed schemes under RL — inventing the scheme does not change the picture

> "Letting the model design its own scheme does not change the picture: encoded reasoning and messaging are learned quickly, steganographic reasoning plateaus just above chance"

> "In a variant, the model first designs its own scheme and is then asked to follow it, this time in a complete answer."

**ID:** model-designed-schemes
**Location:** Section 3.2 "Reinforcement learning"; Section 2.8 "Elicitation setups"
**Grep command used:** `Grep pattern="Letting the model design its own scheme|the model first designs its own scheme" path="literature/extracted/schulz_2026.txt"`

---

## Claim 12: Which covers are dangerous — tasks with many repetitive, arbitrary choices make steganographic reasoning feasible; such channels deserve monitor scrutiny

> "it points to the kind of cover on which steganographic reasoning is feasible: tasks with many repetitive, supposedly arbitrary or otherwise unimportant choices that can carry information."

> "Realistic agent transcripts are full of such choices, such as variable names, and these channels deserve particular scrutiny from monitors."

**ID:** arbitrary-choice-covers
**Location:** Section 4 "Discussion", Structured main tasks make steganography easier; Section 4.2 "Implications for CoT monitoring"
**Grep command used:** `Grep pattern="it points to the kind of cover|Realistic agent transcripts are full" path="literature/extracted/schulz_2026.txt"`

---

## Claim 13: Evidence the trace is used, and the bound's status — error injection propagates; results are upper bounds on capability, not deployment likelihood

> "Taken together, we see this as good, but not conclusive, evidence that the successful runs reason through their trace."

> "Our experiments estimate an upper bound on how much steganographic reasoning models can learn, not the likelihood of it arising in deployment."

**ID:** trace-use-and-upper-bound
**Location:** Section 4.1 "Is the encoded trace used for computation?"; Section 4.3 "Limitations"
**Grep command used:** `Grep pattern="good, but not conclusive, evidence|estimate an upper bound on how much" path="literature/extracted/schulz_2026.txt"`

---

## Claim 14: Approach — eliciting messaging, encoded reasoning and steganographic reasoning by in-context learning, RL and SFT

> "In-context learning.  We give the models the scheme description and few-shot examples of it applied:"

> "RL on a given scheme.  We use GRPO  ( Shao et al., 2024 )  on Tinker  ( Thinking Machines Lab, 2025 )  with Qwen3.6-35B-A3B (one comparison run uses Qwen3.5-397B-A17B), describing the scheme with a worked example in the prompt."

> "Supervised fine-tuning.  We fine-tune six models spanning 30B to 975B total parameters (Table  S1 ) on main-task completions with the side task inserted programmatically by our schemes, training only on the first tokens that encode side-task numbers."

**ID:** approach-three-method-stego-elicitation
**Location:** Section 2.8 "Elicitation setups"
**Grep command used:** `Grep pattern="In-context learning.  We give the models|RL on a given scheme|Supervised fine-tuning.  We fine-tune six models" path="literature/extracted/schulz_2026.txt"`

---

## Claim 15: Approach — six surface-formatting encodings and the knapsack cover, applicable programmatically to existing text

> "The six surface-formatting schemes encode one symbol per unit (word, whitespace run, or sentence) from the start of the answer and leave the meaning of the text untouched, so they are innocuous enough to serve as steganographic covers, with the partial exception of sentence-interjection (Appendix  E )."

> "All our schemes can be applied programmatically to existing text, giving reliable few-shot and SFT data.
This rules out schemes that reword the answer itself, such as the first-letter encodings of  Zolkowski et al. (2025) ."

> "Knapsack , used under all three elicitation methods, is narrower: the model attempts several packings of weighted items and takes the best, so each packing is a free choice, and the in/out choices of its first items can encode a number in binary, one bit per item (the  knapsack cover )."

**ID:** approach-formatting-and-knapsack-encodings
**Location:** Section 2.5 "Encoding schemes", Table 1 (capitalisation, markdown, whitespace, sentence-markdown, sentence-interjection, sentence-newline; word prefix for encoded reasoning only); Section 2.4
**Grep command used:** `Grep pattern="The six surface-formatting schemes encode|All our schemes can be applied programmatically|Knapsack , used under all three" path="literature/extracted/schulz_2026.txt"`

---

## Claim 16: Relation to Zolkowski et al. and Skaf et al. — the negative result reproduced, the small uplift doubted; RL-learned encodings stay legible

> "These experiments reproduce the largely negative result of  Zolkowski et al. (2025) , and our best replication suggests that the small uplift they report was probably not steganographic reasoning (Appendix  T )."

> "Skaf et al. (2025)  show that models trained against regular-expression CoT monitors learn to avoid the flagged words, but the reasoning stays legible rather than hidden in innocuous text."

**ID:** relation-zolkowski-skaf
**Location:** Section 3.1; Section 1 "Introduction"
**Grep command used:** `Grep pattern="reproduce the largely negative result of|show that models trained against regular-expression CoT monitors" path="literature/extracted/schulz_2026.txt"`

**Supports:** zolkowski_2025:approach-encoded-reasoning-eval (grounded by #relation-zolkowski-skaf)
**Qualifies:** zolkowski_2025:approach-encoded-reasoning-eval (grounded by #relation-zolkowski-skaf)
**Qualifies:** skaf_2025:approach-cot-penalty-rl (grounded by #relation-zolkowski-skaf)
