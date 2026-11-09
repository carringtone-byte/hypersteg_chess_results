---
paper: "Ganea, Bécigneul and Hofmann (2018)"
title: "Hyperbolic Neural Networks"
doi: ""
pmcid: ""
url: "https://arxiv.org/abs/1805.09112 (arXiv HTML rendering of v2, 28 Jun 2018)"
source_version: "preprint"
file: "literature/ganea_2018.html"
retrieved: "20261105"
verified_by: "Claude (Opus 5.5) subagent, hyperbolic strand, quotes checked with verify_quotes.py (read-only run)"
# The six below are written by `verify_quotes.py --stamp` — do not hand-edit.
# They bind the ledger to the exact source/extract bytes AND its own quoted text
# (body_sha256) it was verified against, so a later quote edit is caught in CI.
source_sha256: "4ec49e96792c972c6c7530710f96dd700e26a615bb7be861b95b2112b7892bfe"
extract_sha256: "681434fd74d29001a4fdd3e2690c0a29de847dadad79d2f51199a70455fe28ad"
body_sha256: "c9d1b630b0b3a660a72f0603fffdbb6ebc48f7429a3167588ffbefd49fd5fcc8"
verifier_version: "2"
verified_verdict: "pass"
verified_date: "20261106"
extract_source_sha256: "4ec49e96792c972c6c7530710f96dd700e26a615bb7be861b95b2112b7892bfe"
---

# Verified Claims — Ganea, Bécigneul and Hofmann (2018)

Each claim below was extracted by reading the downloaded paper file with the Read
tool, grepping for the specific content, and reading the surrounding context to
confirm the attribution is faithful.

Source: arXiv:1805.09112v2 [cs.LG], HTML rendering. Authors: Octavian-Eugen Ganea, Gary
Bécigneul (equal contribution) and Thomas Hofmann, Department of Computer Science, ETH Zürich.
No DOI is printed in the extract. The extract does not print a venue; `yang_2024` cites the
paper at the Conference on Neural Information Processing Systems (NeurIPS). The extract carries the "Abstract" heading but no abstract
text, so claims are taken from the body. Locations are by section; the HTML has no page
numbers. This is a hyperbolic deep-learning paper, not a steganography paper. It is ledgered
because it supplies the exponential and logarithmic maps and the Möbius operations that
HyperSteg (`literature/verified_claims/agarwal_2023.md`) uses to blend message and carrier on
the Poincaré ball.

## Claim 1: Approach — generalise MLR, feed-forward and recurrent (GRU) networks to the Poincaré ball via gyrovector spaces

> "The  main contribution  of this paper is to bridge the gap between hyperbolic and Euclidean geometry in the context of neural networks and deep learning by generalizing in a principled manner both the basic operations as well as multinomial logistic regression (MLR), feed-forward (FFNN), simple and gated (GRU) recurrent neural networks (RNN) to the Poincaré model of the hyperbolic geometry."

> "We do it by connecting the theory of gyrovector spaces and generalized Möbius transformations introduced by"

> "with the Riemannian geometry properties of the manifold."

**ID:** approach-hyperbolic-neural-networks
**Location:** Section 1 "Introduction"
**Grep command used:** `Grep pattern="main contribution  of this paper|connecting the theory of gyrovector|Riemannian geometry properties of the manifold" path="literature/extracted/ganea_2018.txt"`

---

## Claim 2: Motivation — trees embed with low distortion in two hyperbolic dimensions but not in Euclidean space of any dimension

> "shows that arbitrary tree structures cannot be embedded with arbitrary low distortion (i.e. almost preserving their metric) in the Euclidean space with unbounded number of dimensions, but this task becomes surprisingly easy in the hyperbolic space with only 2 dimensions where the exponential growth of distances matches the exponential growth of nodes with the tree depth."

> "However, appropriate deep learning tools are needed to embed feature data in this space and use it in downstream tasks."

**ID:** tree-distortion-motivation
**Location:** Section 1 (the tree result is attributed to reference [10], De Sa, Gu, Ré and Sala, *Representation tradeoffs for hyperbolic embeddings*, ledgered as `sala_2018`)
**Grep command used:** `Grep pattern="arbitrary tree structures cannot be embedded|appropriate deep learning tools are needed" path="literature/extracted/ganea_2018.txt"`

---

## Claim 3: Built on Poincaré embeddings — the Poincaré ball is chosen following Nickel and Kiela, whose rescaled Riemannian gradient it reuses

> "Similarly as in  ( 21 )  and  ( 11 ) , we choose to work in the Poincaré ball."

> "However, optimization w.r.t. hyperbolic parameters is different (see below) and based on Riemannian gradients which are just rescaled Euclidean gradients when working in the conformal Poincaré model  ( 21 ) ."

**ID:** builds-on-poincare-embeddings
**Location:** Section 2.2 "Hyperbolic space: the Poincaré ball"; Section 4 "Models architecture" (reference [21] is Nickel and Kiela, *Poincaré embeddings for learning hierarchical representations*; [11] is Ganea, Bécigneul and Hofmann, *Hyperbolic entailment cones*)
**Grep command used:** `Grep pattern="we choose to work in the Poincaré ball|just rescaled Euclidean gradients" path="literature/extracted/ganea_2018.txt"`

**Depends-on:** nickel_2017:approach-poincare-embeddings (grounded by #builds-on-poincare-embeddings)

---

## Claim 4: One framework indexed by curvature — Euclidean space is recovered as the curvature goes to zero

> "We smoothly parametrize basic operations and objects in all spaces of constant negative curvature using a unified framework that depends only on the curvature value. Thus, we show how Euclidean and hyperbolic spaces can be continuously deformed into each other."

> "i.e.  we recover Euclidean geometry in the limit"

**ID:** curvature-unified-framework
**Location:** Section 1; Section 2.3 "Gyrovector spaces", "Distance" (Eq. 8)
**Grep command used:** `Grep pattern="unified framework that depends only on the curvature|recover Euclidean geometry in the limit" path="literature/extracted/ganea_2018.txt"`

---

## Claim 5: Exponential and logarithmic maps — Möbius scalar multiplication is a scaling in the tangent space at the origin

> "The following lemma gives the closed-form derivation of exponential and logarithmic maps."

> "can actually be obtained by projecting"

> "in the tangent space at  0  with the logarithmic map, multiplying this projection by the scalar"

> "and then projecting it back on the manifold with the exponential map:"

**ID:** exp-log-maps-tangent-space
**Location:** Section 2.4, "Exponential and logarithmic maps" (Lemma 2) and "Möbius scalar multiplication using exponential and logarithmic maps" (Lemma 3)
**Grep command used:** `Grep pattern="closed-form derivation of exponential|in the tangent space at  0  with the logarithmic|back on the manifold with the exponential" path="literature/extracted/ganea_2018.txt"`

---

## Claim 6: Layers — the Möbius version of a map applies it in the tangent space; bias translation is what separates the model from a Euclidean one

> "we define the  Möbius version of"

> "This means that these operations can essentially be performed in Euclidean space. Therefore, it is the interposition between those with the bias translation of Eq. ( 28 ) which differentiates this model from its Euclidean counterpart."

> "Our neural network layers can be used in a plug-n-play manner exactly like standard Euclidean layers. They can also be combined with Euclidean layers."

**ID:** mobius-layers-bias-translation
**Location:** Section 3.2 "Hyperbolic feed-forward layers" (Definition 3.2, Eq. 26; "Bias translation", Eq. 28); Section 4 "Models architecture"
**Grep command used:** `Grep pattern="Möbius version of|differentiates this model from its Euclidean|plug-n-play manner" path="literature/extracted/ganea_2018.txt"`

---

## Claim 7: Concatenation of inputs generalised by Möbius addition of per-block products

> "We generalize this to hyperbolic spaces: if we are given"

> "Concatenation of multiple input vectors."

**ID:** hyperbolic-concatenation
**Location:** Section 3.2, "Concatenation of multiple input vectors" (the definition M ⊗c x := M₁ ⊗c x₁ ⊕c M₂ ⊗c x₂ is in notation the extract renders as maths; HyperSteg uses a later β-concatenation from Shimizu et al., not this one)
**Grep command used:** `Grep pattern="We generalize this to hyperbolic spaces|Concatenation of multiple input vectors" path="literature/extracted/ganea_2018.txt"`

---

## Claim 8: Hypothesis and test — gains should be largest when the data are closest to a tree; SNLI and a synthetic noisy-prefix task

> "We conjecture that the improvements of hyperbolic neural networks are more significant when the underlying data structure is closer to a tree. To test this, we design a proof-of-concept task of  detection of noisy prefixes"

> "We test hyperbolic networks on the biggest real dataset for this task, SNLI  ( 7 ) . It consists of 570K training, 10K validation and 10K test sentence pairs."

**ID:** tree-likeness-hypothesis-tasks
**Location:** Section 4 "Experiments", "SNLI task and dataset" and "PREFIX task and datasets" (embedding dimension 5, c = 1, Table 1)
**Grep command used:** `Grep pattern="We conjecture that the improvements|biggest real dataset for this task" path="literature/extracted/ganea_2018.txt"`

---

## Claim 9: Results — on par with or better than Euclidean models; no clear MLR gain on entailment, clear gain on WordNet subtree classification

> "Empirically we found that our models outperform or are on par with corresponding Euclidean architectures on sequential data with implicit hierarchical structure."

> "For the sentence entailment classification task we do not see a clear advantage of hyperbolic MLR compared to its Euclidean variant."

> "We can see that the hyperbolic MLR overpasses its Euclidean variants in almost all settings, sometimes by a large margin."

**ID:** results-on-par-or-better
**Location:** Section 5 "Conclusion"; Section 4 "MLR classification experiments", Table 2 and Figure 2
**Grep command used:** `Grep pattern="outperform or are on par|do not see a clear advantage|overpasses its Euclidean variants" path="literature/extracted/ganea_2018.txt"`

---

## Claim 10: Hyperbolic models use the ball's border — accuracy is higher when embeddings approach "infinity"

> "We observed that, in the hyperbolic setting, accuracy is often much higher when sentence embeddings can go close to the border (hyperbolic "infinity"), hence exploiting the hyperbolic nature of the space."

**ID:** embeddings-near-border
**Location:** Appendix F "More Experimental Investigations", Figures 3–5
**Grep command used:** `Grep pattern="accuracy is often much higher when sentence embeddings" path="literature/extracted/ganea_2018.txt"`

---

## Claim 11: Requirements and limits — Riemannian SGD for hyperbolic parameters (no Riemannian Adam), numerical clipping at the border, sensitivity to initialisation

> "Hyperbolic parameters cannot be updated with an equivalent method that keeps track of gradient history due to the absence of a Riemannian Adam. Thus, they are optimized using full Riemannian stochastic gradient descent (RSGD)"

> "are not defined when the hyperbolic argument vectors are on the ball border, i.e."

> "We do this because the highly non-convex spectrum of hyperbolic neural networks sometimes results in convergence to poor local minima, suggesting that initialization is very important."

**ID:** optimisation-numerics-limits
**Location:** Section 4, "Optimization", "Numerical errors" (projection to radius 1 − 10⁻⁵) and results paragraph before Table 1
**Grep command used:** `Grep pattern="absence of a Riemannian Adam|on the ball border|highly non-convex spectrum" path="literature/extracted/ganea_2018.txt"`
