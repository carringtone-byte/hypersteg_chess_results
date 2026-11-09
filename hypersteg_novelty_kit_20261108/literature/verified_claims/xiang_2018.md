---
paper: "Xiang, Yu, Yang, Zeng and Shen (2018)"
title: "A Word-Embedding-Based Steganalysis Method for Linguistic Steganography via Synonym Substitution"
doi: "10.1109/ACCESS.2018.2878273"
pmcid: "<PMC ID, if any>"
url: "<source URL the file was fetched from>"
source_version: "published"
file: "literature/xiang_2018.pdf"
retrieved: "20261105"
verified_by: "Claude (Opus 5.5) subagent, quotes checked with verify_quotes.py (read-only run)"
# The six below are written by `verify_quotes.py --stamp` — do not hand-edit.
# They bind the ledger to the exact source/extract bytes AND its own quoted text
# (body_sha256) it was verified against, so a later quote edit is caught in CI.
source_sha256: "49ddadb569781dd49e345c55d9a97da7636c64f4b361eef06d9c63d68adb4ad1"
extract_sha256: "411e7e52d0dfda69791a58e8cf30033f4daad3bace7e1d37c6e49c346975d470"
body_sha256: "c566357fa60f781937e489f2c33117d75940e9afe2bc2ded6602cc7a097b2267"
verifier_version: "2"
verified_verdict: "pass"
verified_date: "20261106"
extract_source_sha256: "49ddadb569781dd49e345c55d9a97da7636c64f4b361eef06d9c63d68adb4ad1"
---

# Verified Claims — Xiang, Yu, Yang, Zeng and Shen (2018)

Each claim below was extracted by reading the downloaded paper file with the Read
tool, grepping for the specific content, and reading the surrounding context to
confirm the attribution is faithful.

Source: IEEE Access, vol. 6, 2018, pp. 64131 onwards (publisher PDF). The DOI is printed
on page 1 as "Digital Object Identifier 10.1 109/ACCESS.2018.2878273" (the space is a PDF
extraction artefact). This is a steganalysis (detection) paper against edit-based
synonym-substitution (SS) steganography; page numbers below are the journal page numbers.

## Claim 1: Attacked carrier and encoding — synonym substitution: interchangeable synonyms form a substitution set, and the choice among them carries the bits

> "It treats synonymous words as inter- changeable elements to form a substitution set. The alter- ations of the choice of synonyms in a substitution set can hide information and generate unsuspicious alternatives for a cover text."

> "Winstein [18] developed the ﬁrst practical SS-based steganographic system, called Tlex, which employed a multi-base coding method to encode synonyms extracted from WordNet."

**ID:** ss-carrier-substitution-sets
**Location:** Section I "Introduction", p. 64132
**Grep command used:** `Grep pattern="interchangeable elements|developed|Tlex, which employed" path="literature/extracted/xiang_2018.txt"`

---

## Claim 2: Prior SS schemes surveyed — vertex coding, matrix embedding and syndrome-trellis codes to reduce embedding distortion

> "Chang and Clark [19] proposed a sophisticate vertex coding method to encode collected synonyms into unrepeated bit string"

> "applied the matrix embedding to improve the embedding efﬁciency by reducing the number of synonym substitutions. Hu et al. [23] pro- pose a double-layered STC (Syndrome-trellis code) scheme to minimize statistical and linguistic distortion caused by synonym substitutions."

**ID:** ss-scheme-family
**Location:** Section I "Introduction", p. 64132
**Grep command used:** `Grep pattern="vertex coding method|matrix embedding|double-layered STC" path="literature/extracted/xiang_2018.txt"`

---

## Claim 3: Detection principle — the original word is the best fit for its context, so a substituted synonym has lower context fitness

> "In general, the original word in a normal text should be the most appropriate word for the current context, its context ﬁtness will be largest compared with those of its synonymous words."

> "when an original synonym in the cover text is replaced by its synonymous word for embedding information, the new word would not be very appropriate to the current context compared with the original word, leading to a relatively small context ﬁtness."

**ID:** context-fitness-principle
**Location:** Section III-D "Feature extraction", p. 64137
**Grep command used:** `Grep pattern="most appropriate word for the current context|leading to a relatively small" path="literature/extracted/xiang_2018.txt"`

---

## Claim 4: Detector — Skip-gram word embeddings; context fitness is cosine correlation with context words weighted by TF-IDF

> "With the continuous Skip- gram language model, each synonym and words in its context are represented as word embeddings"

> "we directly measure the correlation between a synonym and one of its context words by cosine distance between the corresponding word embeddings."

> "we use the TF-IDF method to assess the importance of a context word to the certain synonym."

**ID:** skipgram-tfidf-context-fitness
**Location:** Abstract; Section III-C "Context fitness calculation", p. 64136
**Grep command used:** `Grep pattern="continuous Skip|by cosine distance between|use the TF-IDF method" path="literature/extracted/xiang_2018.txt"`

---

## Claim 5: Features and classifier — three features (CFMR, CFMD, CFM) fed to an SVM with RBF kernel

> "three detection features: Context Fitness Maximum Rate (CFMR), Context Fitness Maximum Devia- tion (CFMD), and Context Fitness Mean(CFM)"

> "In a word, the cover text should have larger CFMR, CFM and smaller CFMD than the stego text."

> "WES utilizes SVM with RBF kernel as the classiﬁer. 5-fold cross validation is chosen for measuring classiﬁcation performance."

**ID:** cfmr-cfmd-cfm-svm
**Location:** Section III-D, pp. 64137–64138; Section IV-B, p. 64139
**Grep command used:** `Grep pattern="Context Fitness Maximum Rate|should have larger CFMR|SVM with RBF kernel" path="literature/extracted/xiang_2018.txt"`

---

## Claim 6: Detector access — needs only the text, a prepared synonym dictionary and embeddings learned from a public corpus; it is a supervised classifier trained on labelled stego and cover texts

> "By checking the words in a text using a prepared syn- onym dictionary, the synonyms are recognized."

> "so a large-scale training stego and cover texts should be prepared for training a classi- ﬁer in the training process."

**ID:** detector-access
**Location:** Section III-B, p. 64135; Section III-A, p. 64134
**Grep command used:** `Grep pattern="prepared syn|a large-scale training" path="literature/extracted/xiang_2018.txt"`

---

## Claim 7: Data — 5000 Gutenberg cover texts; stego from T-Lex at 25/50/75/100 % embedding rate, matrix coding (k = 3) and STC; 3000 + 3000 for training

> "5000 texts were selected randomly from our Gutenberg corpus as cover texts."

> "The T-Lex steganographic tool [18] is the only available SS steganography system on the Internet"

> "MC-based method must embed message with certain embedding rates, which should be k/(2k -1), ( k=2,3,...). Namely, every 2 k -1 cover syn- onyms are embedded into k bits secret message."

> "For each stego text set, 3000 stego texts are selected and combined with 3000 cover texts for training, and the remaining are used for testing."

**ID:** datasets-tlex-mc-stc
**Location:** Section IV-A-3 "The datasets for steganalysis task", p. 64138; Section IV-B, p. 64139
**Grep command used:** `Grep pattern="5000 texts were selected|only available SS steganography|certain embedding rates|3000 stego" path="literature/extracted/xiang_2018.txt"`

---

## Claim 8: Capacity unit of the attacked schemes — embedding rate as a fraction of synonyms; matrix coding carries k bits per 2^k − 1 synonyms

> "The ﬁrst stego text set denoted as Tlex-25% is gen- erated by using T-Lex to embed random secret mes- sage into each cover text with the embedding rate of 25%."

> "A steganalysis method always achieves stronger capability of detecting stego texts with high embedding rate than those with low embedding rate."

**ID:** embedding-rate-capacity
**Location:** Section IV-A-3, p. 64138
**Grep command used:** `Grep pattern="denoted as Tlex-25%|stronger capability of detecting" path="literature/extracted/xiang_2018.txt"`

---

## Claim 9: Detection result — over 90 % F-value on every stego set; average F-value 11.01 % above PP and 4.8 % above NRF

> "For all stego text sets in the experiments, WES-Google-skip achieves over 90% F-value. It improves the average F-value of PP by 11.01%, that of NRF by 4.8%."

> "The performances of PP and NRF are not satisfactory when the embedding rate of Tlex stego texts is 25%."

**ID:** detection-f-value
**Location:** Section IV-B "Detection performance comparison for different steganographic methods", p. 64139
**Grep command used:** `Grep pattern="achieves over 90%|not satisfactory when the embedding rate" path="literature/extracted/xiang_2018.txt"`

---

## Claim 10: Generalisation across SS schemes — the choice of SS method has no significant effect on detection, including the distortion-minimising STC

> "different SS steganographic meth- ods do not have a signiﬁcant impact on our method, our method has good generalization."

> "STC-based method minimized distortion caused by synonym substitutions to achieve high secure level."

**ID:** generalises-across-ss
**Location:** Section IV-B, p. 64139; Section IV-A-3, p. 64138
**Grep command used:** `Grep pattern="do not have a signiﬁcant impact on our method|minimized distortion caused by synonym" path="literature/extracted/xiang_2018.txt"`

---

## Claim 11: Embedding corpus matters — embeddings learned from the cover's own domain (Gutenberg) beat GoogleNews; Skip-gram beats CBOW

> "WES-Gutenberg-skip outperforms WES-Google-skip by 0.2%, 0.87%, and 0.56% in terms of average precision, recall and F-value, respectively."

> "the detection performance of the proposed method can be further improved by using particular corpus to learn better word embeddings, whose derivation is consistent with the cover texts."

> "CBOW model does not perform better than Skip- gram model on the steganalysis task"

**ID:** domain-matched-embeddings
**Location:** Section IV-C "Detection performance comparison for different learned word embeddings", p. 64140
**Grep command used:** `Grep pattern="outperforms WES-Google-skip by|using particular corpus|CBOW model does not perform better" path="literature/extracted/xiang_2018.txt"`

---

## Claim 12: Relevance to edit-based carriers — fitting a word to its context is the signal an SS steganalyst exploits; word-frequency alone misjudges fitness

> "If there are much more synonyms in the detected text are in this case, then the detected text is a stego text with a very high probability."

> "It can be easy found that word embeddings can more accurately measure the context ﬁtness than using word frequencies."

**ID:** fitness-beats-frequency
**Location:** Section III-D, p. 64137
**Grep command used:** `Grep pattern="stego text with a very high probability|more accurately measure the context" path="literature/extracted/xiang_2018.txt"`

---

## Claim 13: Approach — WES, word-embedding steganalysis: context fitness of each synonym, three features from it, and an SVM

> "It extracts semantic features by using Neural Network Language Model (NNLM) to reveal the deep and implicit semantic relation- ships between a synonym and its context words, which are all represented to word embeddings. Based on this, the context ﬁtness measuring the suitability of a synonym in a certain context is modeled by using word embeddings and TF-IDF. Finally, three detection features are extracted by analyzing the context ﬁtness values of synonymous words and fed into a SVM classiﬁer to distinguish stego texts from cover ones."

> "we propose a linguistic steganalysis method to leverage the word-level semantics, correlations within word embeddings to aid us in modeling the changes caused by synonym sub- stitutions, and further enhance the detection performance against SS steganography."

**ID:** approach-wes
**Location:** Section I "Introduction", p. 64133; Section III, p. 64134
**Grep command used:** `Grep pattern="semantic features by using Neural Network|we propose a linguistic steganalysis method to leverage" path="literature/extracted/xiang_2018.txt"`
