---
paper: "Shimizu, Mukuta and Harada (2020)"
title: "Hyperbolic Neural Networks++"
doi: ""
pmcid: ""
url: "https://arxiv.org/abs/2006.08210 (arXiv HTML rendering of v3, 17 Mar 2021)"
source_version: "preprint"
file: "literature/shimizu_2020.html"
retrieved: "20261105"
verified_by: "Claude (Opus 5.5) subagent, hyperbolic strand, quotes checked with verify_quotes.py (read-only run)"
# The six below are written by `verify_quotes.py --stamp` — do not hand-edit.
# They bind the ledger to the exact source/extract bytes AND its own quoted text
# (body_sha256) it was verified against, so a later quote edit is caught in CI.
source_sha256: "5eda3f4b14ff80ec7b4156fe17a0fa06f3c67e1dc3e68ceddee2e2a90c28a641"
extract_sha256: "bf39d54bb74b719ddfd3b0056e1eb5191222ff24badb43a7ec7fd226beebc49c"
body_sha256: "5d81f85b573791d1d1a1a661d424465ade91375c57a1e1fb082cf95cc70c8538"
verifier_version: "2"
verified_verdict: "pass"
verified_date: "20261106"
extract_source_sha256: "5eda3f4b14ff80ec7b4156fe17a0fa06f3c67e1dc3e68ceddee2e2a90c28a641"
---

# Verified Claims — Shimizu, Mukuta and Harada (2020)

Each claim below was extracted by reading the downloaded paper file with the Read
tool, grepping for the specific content, and reading the surrounding context to
confirm the attribution is faithful.

Source: arXiv:2006.08210v3 [cs.LG], HTML rendering. Authors: Ryohei Shimizu, Yusuke Mukuta and
Tatsuya Harada (The University of Tokyo; RIKEN AIP). No DOI or publication venue is printed in
the extract; `cetin_2022` and `yang_2024` both cite it as an arXiv preprint. Locations
are by section; the HTML has no page numbers. The extract renders section headings for the
contents list but drops several in the body, so some locations are given by the nearest
paragraph label. This is a hyperbolic deep-learning paper, not a steganography paper. It is
ledgered because HyperSteg (`literature/verified_claims/agarwal_2023.md`, Claim 4) blends
message and carrier features with the Poincaré β-concatenation defined here.

## Claim 1: Approach — a parameter-reduced MLR, FC, convolutional and attention layers, all in the Poincaré ball under one interpretation

> "In this study, we generalize the fundamental components of neural networks in a single hyperbolic geometry model, namely, the Poincaré ball model. This novel methodology constructs a multinomial logistic regression, fully-connected layers, convolutional layers, and attention mechanisms under a unified mathematical interpretation, without increasing the parameters."

> "Experiments show the superior parameter efficiency of our methods compared to conventional hyperbolic components, and stability and outperformance over their Euclidean counterparts."

**ID:** approach-hnn-plus-plus
**Location:** Abstract
**Grep command used:** `Grep pattern="we generalize the fundamental components|superior parameter efficiency" path="literature/extracted/shimizu_2020.txt"`

---

## Claim 2: Motivation — exponential volume growth lets hyperbolic space embed trees with arbitrarily low distortion

> "Hyperbolic spaces, which have the capacity to embed tree structures without distortion owing to their exponential volume growth, have recently been applied to machine learning to better capture the hierarchical nature of data."

> "a hyperbolic space has the capacity to continuously embed tree structures with arbitrarily low distortion  ( Krioukov et al., 2010 ;  Sala et al., 2018 ) ."

> "Compared to the Euclidean space, a hyperbolic space shows a higher embedding accuracy under fewer dimensions in such cases."

**ID:** exponential-volume-motivation
**Location:** Abstract; Section 1 "Introduction"
**Grep command used:** `Grep pattern="embed tree structures without distortion|arbitrarily low distortion|higher embedding accuracy under fewer" path="literature/extracted/shimizu_2020.txt"`

---

## Claim 3: Built on HNNs — Ganea et al.'s Poincaré-ball framework is the foundation, but its MLR doubles the parameters and it has no convolutional layers

> "One of the pioneers in this area is Hyperbolic Neural Networks (HNNs), which introduced an easy-to-interpret and highly analytical coordinate system of hyperbolic spaces, namely, the Poincaré ball model, with a corresponding gyrovector space to smoothly connect the fundamental functions common to neural networks into valid functions in a hyperbolic geometry  ( Ganea et al., 2018a ) ."

> "In terms of the network architectures, the current formulation of hyperbolic MLR  ( Ganea et al., 2018a )  requires almost twice the number of parameters compared to its Euclidean counterpart."

> "The lack of convolutional layers must also be mentioned, because their application is now ubiquitous and is no longer limited to the field of computer vision."

**ID:** refines-hnn
**Location:** Section 1 "Introduction"
**Grep command used:** `Grep pattern="One of the pioneers in this area|requires almost twice the number of parameters|lack of convolutional layers" path="literature/extracted/shimizu_2020.txt"`

**Refines:** ganea_2018:approach-hyperbolic-neural-networks (grounded by #refines-hnn)

---

## Claim 4: Contributions — reduced-parameter MLR, geodesic-aware FC layers, split and concatenation, convolution, centroid equivalence

> "We reformulate a hyperbolic MLR to reduce the number of parameters to the same level as a Euclidean version while maintaining the same range of representational properties."

> "We generalize the split and concatenation of coordinates to the Poincaré ball model by setting the invariance of the expected value of the vector norm as a criterion."

> "We prove the equivalence of the hyperbolic centroids defined in three different hyperbolic geometry models, and expand the condition of non-negative weights to entire real values."

**ID:** contributions-list
**Location:** Section 1, list of contributions
**Grep command used:** `Grep pattern="reduce the number of parameters to the same level|invariance of the expected value|equivalence of the hyperbolic centroids" path="literature/extracted/shimizu_2020.txt"`

---

## Claim 5: Why a new concatenation — naive split shrinks norms and naive concatenation leaves the ball; many inputs drift to the boundary

> "However, in the Poincaré ball model, merely splitting the coordinates lowers the norms of the output gyrovectors and limits the representational power, and concatenating them is invalid because the norm of the output can easily exceed the domain of the ball."

> "Moreover, as the number of inputs to be concatenated increases, the output gyrovector  approaches the boundary  of the ball even if the norm of each input is adequately small."

> "As an analogy, keeping the expected values of the norms constant is a worthy criterion in the Poincaré ball because the norm of any Möbius gyrovector is upper-bounded by the ball radius"

**ID:** concatenation-norm-problem
**Location:** Section 3.3 (Poincaré β-split and β-concatenation)
**Grep command used:** `Grep pattern="merely splitting the coordinates|approaches the boundary|keeping the expected values of the norms" path="literature/extracted/shimizu_2020.txt"`

---

## Claim 6: Approach — Poincaré β-concatenation: map inputs to the tangent space, rescale by beta-function ratios, concatenate, map back

> "To satisfy this criterion, we propose the following generalization scheme with a scalar coefficient"

> "are first properly scaled and concatenated in the tangent space, and then projected back to the Poincaré ball in the following manner:"

> "One can also confirm that the Poincaré  β \beta -concatenation is the inverse function of the Poincaré  β \beta -split."

> "The input gyrovectors  { 𝒙 i ∈ 𝔹 c n i } i = 1 N \{\bm{x}_{i}\in\mathbb{B}^{n_{i}}_{c}\}^{N}_{i=1}  are first scaled by certain coefficients and concatenated in the tangent space, and then projected back to the Poincaré ball as follows:"

**ID:** approach-poincare-beta-concatenation
**Location:** Section 3.3; Appendix D.4 (the coefficient is β_n = B(n/2, 1/2), B a beta function, and the scaling factors β_n β_{n_i}⁻¹ appear in maths the extract renders as LaTeX; the D.4 proof rests on a naive distributional assumption, Claim 11)
**Grep command used:** `Grep pattern="we propose the following generalization scheme|properly scaled and concatenated in the tangent space|is the inverse function of the Poincaré|scaled by certain coefficients and concatenated" path="literature/extracted/shimizu_2020.txt"`

---

## Claim 7: Against Ganea's concatenation — N − 1 sequential Möbius additions, unequal priority; the tangent-space version costs less and treats inputs fairly

> "generalized a vector concatenation under the premise that the output must be followed by an FC layer, but such an assumption possibly limits its usage."

> "which incurs a heavy computational cost and an unbalanced priority in each input gyrovector. Alternatively, our method with a pair of exponential and logarithmic maps has a lower computational cost  regardless of"

**ID:** concatenation-versus-hnn
**Location:** Section 3.3, "Discussion about the concatenation"
**Grep command used:** `Grep pattern="premise that the output must be followed|unbalanced priority in each input" path="literature/extracted/shimizu_2020.txt"`

**Refines:** ganea_2018:hyperbolic-concatenation (grounded by #concatenation-versus-hnn)

---

## Claim 8: Results — hyperbolic MLRs beat Euclidean ones on embedded subtree classification; the parameter-reduced MLR trains more stably

> "From the results, we can confirm the tendency of the hyperbolic MLRs to outperform the Euclidean version in all settings, which illustrates that MLR considering the hyperbolic geometry are better suited to the hyperbolic embeddings. In particular, our parameter-reduced approach obtains the same level of performance as a conventional hyperbolic MLR in a more stable training, as can be seen from the relatively narrower confidence intervals."

**ID:** mlr-results
**Location:** Section 4.1, Table 1 (F1 on test sets)
**Grep command used:** `Grep pattern="tendency of the hyperbolic MLRs to outperform|parameter-reduced approach obtains" path="literature/extracted/shimizu_2020.txt"`

---

## Claim 9: Results — Poincaré attention in Set Transformers; intrinsic normalisation and gains on hyperbolic data

> "For the Euclidean distribution, our models achieved  almost the  same performance as Set Transformers, while the training of those without Layer Normalization for the same conditioned comparison often failed under all settings. This result suggests the intrinsic normalization properties of our methods, which we attribute to the computation using vector norms."

> "For the hyperbolic distribution, our models outperformed the Euclidean counterparts with an order of magnitude smaller confidence intervals"

**ID:** set-transformer-results
**Location:** Section 4.2 "Amortized clustering of mixture of Gaussians with Set Transformers"
**Grep command used:** `Grep pattern="almost the  same performance as Set|intrinsic normalization properties|order of magnitude smaller confidence" path="literature/extracted/shimizu_2020.txt"`

---

## Claim 10: Results — convolutional sequence-to-sequence translation improves most in few dimensions

> "Finally, we experimented  with  the convolutional  sequence-to-sequence  modeling task for machine translation of WMT’17 English-German"

> "Our model demonstrates the significant improvements compared to the usual Euclidean models in the fewer dimensions, which reflects the immense embedding capacity of hyperbolic spaces."

**ID:** translation-results
**Location:** Section 4.3, Table 3 (BLEU-4 on newstest2013)
**Grep command used:** `Grep pattern="convolutional  sequence-to-sequence|significant improvements compared to the usual Euclidean" path="literature/extracted/shimizu_2020.txt"`

---

## Claim 11: What the method needs — Riemannian Adam for training; the β-concatenation proofs rest on a naive distributional assumption

> "We used the Riemannian Adam optimizer with"

> "In the Poincaré ball model, calculating such values without any postulate for the probabilistic distribution that the feature gyrovectors or tangent vectors follow is difficult owing to the nonlinear transformations in the exponential and logarithmic maps. Thus, we first make the following naive assumption:"

**ID:** requirements-and-assumptions
**Location:** Appendix (experimental settings); Appendix D.4 "Proof of the properties of Poincaré β-split and β-concatenation"
**Grep command used:** `Grep pattern="Riemannian Adam optimizer with|following naive assumption" path="literature/extracted/shimizu_2020.txt"`
