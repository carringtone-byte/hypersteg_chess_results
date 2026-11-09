---
paper: "Zhang et al. (2021)"
title: "Provably Secure Generative Linguistic Steganography"
doi: "10.48550/arXiv.2106.02011"
pmcid: "<PMC ID, if any>"
url: "<source URL the file was fetched from>"
source_version: "preprint"
file: "literature/zhang_2021.html"
retrieved: "20261105"
verified_by: "Claude (Opus 5.5) subagent, quotes checked with verify_quotes.py (read-only run)"
# The six below are written by `verify_quotes.py --stamp` — do not hand-edit.
# They bind the ledger to the exact source/extract bytes AND its own quoted text
# (body_sha256) it was verified against, so a later quote edit is caught in CI.
source_sha256: "493014d865b5d27f879594085dd3c493da89f8426de3d16ac1e89eddbdbf2ddd"
extract_sha256: "eceded0a2cc700eb24cc85de656a478784b07d55588eacc034f045d3f377d1c4"
body_sha256: "5b7599c1c42e26fa6c83860028e17b56129f73874feed61c7de8541080b3df59"
verifier_version: "2"
verified_verdict: "pass"
verified_date: "20261106"
extract_source_sha256: "493014d865b5d27f879594085dd3c493da89f8426de3d16ac1e89eddbdbf2ddd"
---

# Verified Claims — Zhang et al. (2021)

Each claim below was extracted by reading the downloaded paper file with the Read
tool, grepping for the specific content, and reading the surrounding context to
confirm the attribution is faithful.

Source: arXiv:2106.02011v1 [cs.CL], 03 Jun 2021 (arXiv HTML rendering). Authors: Siyu
Zhang, Zhongliang Yang, Jinshuai Yang, Yongfeng Huang (Tsinghua University). Method
name: ADG (Adaptive Dynamic Grouping).

## Claim 1: Method — ADG: tokens grouped adaptively by their LM probability into near-equal-probability groups; the message selects the group

> "we present a novel provably secure generative linguistic steganographic method"

> "which recursively embeds secret information by"

> "of tokens according to their probability given by an off-the-shelf language model."

> "to adaptively group the vocabulary into multiple groups at each time step, so that each group is assigned approximately the same probability."

**ID:** adg-adaptive-dynamic-grouping
**Location:** Abstract; Section 4.1 "Steganography by Grouping"
**Grep command used:** `Grep pattern="novel provably secure generative linguistic|recursively embeds secret information by|according to their probability given by an off-the-shelf|adaptively group the vocabulary into multiple groups" path="literature/extracted/zhang_2021.txt"`

---

## Claim 2: Carrier — generated text, token by token, with no cover text

> "The generative linguistic steganography directly transform secret information into innocuous-looking steganographic text (stegotext) without any covertext."

> "secret information can be encoded in the selection of token at each time step autoregressively during the generation procedure"

**ID:** carrier-generated-tokens
**Location:** Section 1 "Introduction"
**Grep command used:** `Grep pattern="directly transform secret information into innocuous-looking|encoded in the selection of token at each time step" path="literature/extracted/zhang_2021.txt"`

---

## Claim 3: Encoding — a different route from lossless coding (Huffman, arithmetic): grouping; groups split recursively with pruning, then a token is sampled from the final group

> "Unlike previous works that encoded the conditional distribution by lossless coding algorithm, we achieve this goal in a novel way by grouping."

> "recursively grouping the new groups until it is impossible to be equally participated"

> "At last, we normalize the probability of the last selected group and sample a token to generate the stegotext."

> "In this manner, the amount of secret information embedded in each token is adjusted dynamically according to its probability distribution."

**ID:** grouping-not-coding-recursive
**Location:** Section 4 "ADG Methodology"; Section 4.2 "Recursion and Pruning"
**Grep command used:** `Grep pattern="encoded the conditional distribution by lossless coding|recursively grouping the new groups|normalize the probability of the last selected group|adjusted dynamically according to its probability" path="literature/extracted/zhang_2021.txt"`

---

## Claim 4: Practical approximation — group count from the top probability; a greedy suboptimal equal-grouping algorithm, deterministic so the receiver can repeat it

> "we determine the number of groups"

> "since the time complexity of solving the global optimal solution of equal grouping is unacceptable, we implement a suboptimal solution in ADG"

> "In practice, since the probability distribution is discrete, the probability of groups may not be absolutely equal."

**ID:** suboptimal-equal-grouping
**Location:** Section 4.1 (Algorithm 1, u = 2^floor(-log2 p_max))
**Grep command used:** `Grep pattern="determine the number of groups|we implement a suboptimal solution in ADG|probability of groups may not be absolutely equal" path="literature/extracted/zhang_2021.txt"`

---

## Claim 5: Shared and access — same LM, vocabulary and grouping algorithm; the full next-token distribution is needed (white-box)

> "For an exactly successful extraction, Alice and Bob have to share the same language model, vocabulary and grouping algorithm."

> "Bob is supposed to recursively operate the same grouping algorithm as Alice do, and then select the group contains the current token in the stegotext."

**ID:** shared-lm-vocab-grouping
**Location:** Section 4.3 "Information Extraction"
**Grep command used:** `Grep pattern="have to share the same language model, vocabulary and grouping|recursively operate the same grouping algorithm" path="literature/extracted/zhang_2021.txt"`

---

## Claim 6: Security — proof: KL between LM and stegosampling distribution is zero iff groups have equal probability (Jensen), meeting Cachin's definition; extended to the recursion by the authors' argument

> "takes the minimum value 0 when each component of"

> "are equivalent and that achieves the optimal information-theoretic security defined by"

> "We have proved the security of equal grouping algorithm. Obviously, it can also be extended to the recursive manner of ADG, which means the proposed method is provably secure."

**ID:** proof-equal-groups-zero-kl
**Location:** Section 4.1, Assumption 1 and proof (Eqs. 2–7); Section 4.2
**Grep command used:** `Grep pattern="takes the minimum value 0 when each component|achieves the optimal information-theoretic security|extended to the recursive manner of ADG" path="literature/extracted/zhang_2021.txt"`

---

## Claim 7: Security scope — only the embedding distortion is addressed; LM bias is set aside

> "the distortion of generative linguistic steganography includes the bias of the language model"

> "The former is not our research priority."

> "In this paper, we mainly pay attention to the latter distortion."

**ID:** scope-embedding-distortion-only
**Location:** Section 4 "ADG Methodology"; Section 2.3 "Imperceptibility"
**Grep command used:** `Grep pattern="includes the bias of the language model|The former is not our research priority|mainly pay attention to the latter distortion" path="literature/extracted/zhang_2021.txt"`

---

## Claim 8: Capacity — embedding rate in bits per word; about 5.1–5.7 for ADG on LSTM models (Movie 5.147, News 5.650, Tweet 5.411)

> "It is the average amount of information that one single token can carry, and is in unit of"

> "we utilized LSTMs  Hochreiter and Schmidhuber (1997)  for word-level generation. We stacked 2 LSTM layers"

**ID:** capacity-embedding-rate
**Location:** Section 5.4 "Metrics" (ER); Section 5.2 "Implementation Details"; Tables 1–2 (ADG ER 5.147 / 5.650 / 5.411)
**Grep command used:** `Grep pattern="average amount of information that one single token can carry|utilized LSTMs" path="literature/extracted/zhang_2021.txt"`

---

## Claim 9: Detection evidence — measured KL near zero, and two trained steganalysers (FastText, TextCNN, 10-fold) near chance; 1,000 stegotexts against 1,000 test-set covertexts

> "we found that the proposed method ADG outperforms all baselines and it is very close to the optimal value 0 (stochastic sampling)"

> "we employed linguistic steganalysis approaches based on Fasttext"

> "We conducted 10-fold cross validation and reported the average accuracy. Closer to 50% is better."

> "The proposed method ADG outperforms all baselines on the three corpora and it is very close to the optimal value 0.5, which further confirms its imperceptibility."

> "In each case, we generated 1,000 stegotext. We randomly chose same amount of covertext from the test sets for further evaluation."

**ID:** steganalysis-near-chance
**Location:** Section 5.3 "Baselines"; Section 5.4 "Metrics"; Section 5.5 "Results and Analysis"; Table 1 (ADG KLD1 0.033 / 0.027 / 0.048); Table 2 (ADG Acc1 0.548 / 0.543 / 0.496; Acc2 0.544 / 0.519 / 0.497 on Movie / News / Tweet)
**Grep command used:** `Grep pattern="very close to the optimal value 0 \(stochastic|steganalysis approaches based on Fasttext|10-fold cross validation|very close to the optimal value 0.5|we generated 1,000 stegotext" path="literature/extracted/zhang_2021.txt"`

---

## Claim 10: Metric introduced — effective embedding rate discounts capacity by detection accuracy

> "It is a new metric we proposed to evaluate the comprehensive performance of steganographic algorithms."

> "meaning that if the stegotext has a certain probability of being detected, the average amount of secret information actually transmitted should be discounted accordingly."

**ID:** effective-embedding-rate
**Location:** Section 5.4 "Metrics" (Eq. 9, EER = 2 × (1 − Acc) × ER)
**Grep command used:** `Grep pattern="new metric we proposed to evaluate the comprehensive|should be discounted accordingly" path="literature/extracted/zhang_2021.txt"`

---

## Claim 11: Robustness — not tested; the authors assume text passes losslessly

> "Unlike digital images or digital audio which is sensitive to distortions like compression, cropping, blurring or pixel-wise dropout, text can usually be transmitted losslessly through different kinds of public channels."

**ID:** assumes-lossless-channel
**Location:** Section 1 "Introduction"
**Grep command used:** `Grep pattern="text can usually be transmitted losslessly" path="literature/extracted/zhang_2021.txt"`

---

## Claim 12: Approach — ADG, equal-probability grouping of the vocabulary at each step, repeated recursively on the selected group, then sampling inside it

> "We present  ADG  ( A daptive  D ynamic  G rouping), a novel generative linguistic steganographic method based on off-the-shelf language models, which groups the tokens adaptively in accordance with their probability at each time step to embed secret information dynamically in the generated stegotext."

> "To sum up, at each time step, the proposed ADG embedding algorithm first conducts the equal grouping algorithm adaptively according to the conditional distribution, and then recursively repeats the operation on the selected group dynamically according to the secret information, until it is indivisible."

> "in which case  p L ​ M \displaystyle p_{LM}  and  q \displaystyle q  are equivalent and that achieves the optimal information-theoretic security defined by  Cachin (1998) ."

**ID:** approach-adg
**Location:** Section 1 "Introduction" (contributions); Section 4.1 "Steganography by Grouping"; Section 4.2 "Recursion and Pruning"
**Grep command used:** `Grep pattern="We present  ADG|To sum up, at each time step|optimal information-theoretic security defined by" path="literature/extracted/zhang_2021.txt"`
**Depends-on:** cachin_1998:relative-entropy-security (grounded by #approach-adg)
