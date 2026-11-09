---
paper: "Nickel and Kiela (2017)"
title: "Poincaré Embeddings for Learning Hierarchical Representations"
doi: ""
pmcid: ""
url: "https://arxiv.org/abs/1705.08039 (arXiv HTML rendering of v2, 26 May 2017)"
source_version: "preprint"
file: "literature/nickel_2017.html"
retrieved: "20261105"
verified_by: "Claude (Opus 5.5) subagent, hyperbolic strand, quotes checked with verify_quotes.py (read-only run)"
# The six below are written by `verify_quotes.py --stamp` — do not hand-edit.
# They bind the ledger to the exact source/extract bytes AND its own quoted text
# (body_sha256) it was verified against, so a later quote edit is caught in CI.
source_sha256: "1fc864f52cd63c89844ce75fc20f628c2f9aa129819f9993f93cc970eb1675e1"
extract_sha256: "4ff36ebaaf7337c30dbec75352ea625d7d45006b3f719539eb704bfbf01c70fe"
body_sha256: "d103663909415ad4c128774bad23c84bc25353b32776024ac0d5aee313d10a4c"
verifier_version: "2"
verified_verdict: "pass"
verified_date: "20261106"
extract_source_sha256: "1fc864f52cd63c89844ce75fc20f628c2f9aa129819f9993f93cc970eb1675e1"
---

# Verified Claims — Nickel and Kiela (2017)

Each claim below was extracted by reading the downloaded paper file with the Read
tool, grepping for the specific content, and reading the surrounding context to
confirm the attribution is faithful.

Source: arXiv:1705.08039v2 [cs.AI], HTML rendering. Authors: Maximilian Nickel and Douwe Kiela,
Facebook AI Research. No DOI is printed in the extract. The extract does not print a venue;
`he_2024` cites the paper in *Advances in Neural Information Processing Systems* 30, 2017. The HTML carries no page numbers, so
locations are by section. This is a hyperbolic representation-learning paper, not a
steganography paper: it hides nothing. It is ledgered because HyperSteg
(`literature/verified_claims/agarwal_2023.md`) rests on the Poincaré-ball geometry it popularised
for machine learning.

## Claim 1: Approach — embed symbolic data in an n-dimensional Poincaré ball to capture hierarchy and similarity at once

> "For this purpose, we introduce a new approach for learning hierarchical representations of symbolic data by embedding them into hyperbolic space – or more precisely into an"

> "Due to the underlying hyperbolic geometry, this allows us to learn parsimonious representations of symbolic data by simultaneously capturing hierarchy and similarity."

**ID:** approach-poincare-embeddings
**Location:** Abstract
**Grep command used:** `Grep pattern="learning hierarchical representations of symbolic data by embedding|parsimonious" path="literature/extracted/nickel_2017.txt"`

---

## Claim 2: Motivation — Euclidean embeddings are bounded by dimension; many datasets carry a latent hierarchy

> "Although embedding methods have proven successful in numerous applications, they suffer from a fundamental limitation: their ability to model complex patterns is inherently bounded by the dimensionality of the embedding space."

> "large datasets whose objects can be organized according to a latent hierarchy – a property that is inherent in many complex datasets."

> "Prominent examples of power-law distributed data include natural language (Zipf’s law"

**ID:** euclidean-dimension-bound
**Location:** Section 1 "Introduction"
**Grep command used:** `Grep pattern="fundamental limitation|organized according to a latent hierarchy|power-law distributed data" path="literature/extracted/nickel_2017.txt"`

---

## Claim 3: Geometry — hyperbolic space as a continuous tree; area and circumference grow exponentially with radius

> "Informally, hyperbolic space can be thought of as a continuous version of trees and as such it is naturally equipped to model hierarchical structures."

> "This type of construction is possible as hyperbolic disc area and circle length grow exponentially with their radius."

> "Due to the negative curvature of"

> "the distance of points increases exponentially (relative to their Euclidean distance) the closer they are to the boundary."

**ID:** hyperbolic-continuous-tree
**Location:** Section 1; Section 2 "Embeddings and Hyperbolic Geometry"; Figure 1 caption
**Grep command used:** `Grep pattern="continuous version of trees|grow exponentially with their|closer they are to the boundary" path="literature/extracted/nickel_2017.txt"`

---

## Claim 4: What the coordinates represent — hierarchy through the norm, similarity through the distance

> "For instance, by placing the root node of a tree at the origin of"

> "leaf nodes can be placed close to the boundary of the Poincaré ball as the distance grows very fast between points with a norm close to one."

> "the hierarchical organization of the space is solely determined by the distance of points to the origin."

> "learn embeddings that simultaneously capture the hierarchy of objects (through their norm) as well a their similarity (through their distance)."

**ID:** norm-encodes-hierarchy
**Location:** Section 3 "Poincaré Embeddings"
**Grep command used:** `Grep pattern="placing the root node|leaf nodes can be|solely determined by the distance|through their norm" path="literature/extracted/nickel_2017.txt"`

---

## Claim 5: Unsupervised — the hierarchy is inferred, not supplied as ordered pairs

> "However, we do not assume that we have direct access to information about the hierarchy, e.g., via ordered input pairs. Instead, we consider the task of inferring the hierarchical relationships fully unsupervised, as is, for instance, necessary for text and network data."

**ID:** hierarchy-inferred-unsupervised
**Location:** Section 3
**Grep command used:** `Grep pattern="direct access to information about the" path="literature/extracted/nickel_2017.txt"`

---

## Claim 6: Model choice — the Poincaré ball because its distance is differentiable and only the norm constraint must be kept

> "base our approach on the Poincaré ball model, as it is well-suited for gradient-based optimization."

> "Hence, for this model, an optimization algorithm only needs to maintain the constraint that"

> "Other models of hyperbolic space however, would be more more difficult to optimize, either due to the form of their distance function or due to the constraints that they introduce."

**ID:** poincare-ball-for-optimisation
**Location:** Section 3 and its footnote 2
**Grep command used:** `Grep pattern="well-suited for gradient-based|only needs to maintain the constraint|more more difficult to optimize" path="literature/extracted/nickel_2017.txt"`

---

## Claim 7: Training — stochastic Riemannian optimisation, a rescaled Euclidean gradient with projection back into the ball

> "Since the Poincaré Ball has a Riemannian manifold structure, we can optimize"

> "via stochastic Riemannian optimization methods such as RSGD"

> "In combination with the Riemannian gradient, this corresponds then to the well-known natural gradient method"

> "we constrain the embeddings to remain within the Poincaré ball via the projection"

**ID:** riemannian-sgd-training
**Location:** Section 3.1 "Optimization" (update rule Eq. 5; ε = 10⁻⁵ in the projection)
**Grep command used:** `Grep pattern="Riemannian manifold structure, we can|stochastic Riemannian optimization methods|natural gradient method|remain within the Poincaré ball" path="literature/extracted/nickel_2017.txt"`

---

## Claim 8: Capacity — WordNet nouns embedded with better reconstruction than Euclidean embeddings an order of magnitude larger

> "The transitive closure of the  WordNet   noun hierarchy consists of 82,115 nouns and 743,241 hypernymy relations."

> "Poincaré embeddings are very successful in the embedding of large taxonomies – both with regard to their representation capacity and their generalization performance."

> "Poincaré embeddings show a greatly improved performance while using an embedding that is smaller by an order of magnitude."

**ID:** wordnet-capacity-result
**Location:** Section 4.1 "Embedding Taxonomies", Table 1 (rank and MAP; the comparison sentence is made against Translational embeddings)
**Grep command used:** `Grep pattern="82,115|very successful in the embedding of large|smaller by an order of" path="literature/extracted/nickel_2017.txt"`

---

## Claim 9: Generalisation — link prediction robust to dimension, attributed to a structural bias; low dimensions benefit most

> "the results of Poincaré embeddings in the link prediction task are very robust with regard to the embedding dimension. We attribute this result to the structural bias of Poincaré embeddings, what could lead to reduced overfitting on this kind of data with a clear latent hierarchy."

> "It can be seen that Poincaré embeddings perform again very well on these datasets and – especially in the low-dimensional regime – outperform Euclidean embeddings."

**ID:** structural-bias-generalisation
**Location:** Section 4.1; Section 4.2 "Network Embeddings", Table 2 (AstroPh, CondMat, GrQc, HepPh collaboration networks)
**Grep command used:** `Grep pattern="very robust with regard to the embedding|especially in the" path="literature/extracted/nickel_2017.txt"`

---

## Claim 10: Graded hierarchy — norms support graded lexical entailment on HyperLex without task-specific training

> "An interesting aspect of Poincaré embeddings is that they allow us to make graded assertions about hierarchical relationships as hierarchies are represented in a continuous space."

> "Note that these embeddings were not specifically trained for this task."

> "It can be seen that the ranking based on Poincaré embeddings clearly outperforms all state-of-the-art methods evaluated in"

**ID:** graded-lexical-entailment
**Location:** Section 4.3 "Lexical Entailment", Table 3 (Spearman's rank correlation on 2163 HyperLex noun pairs)
**Grep command used:** `Grep pattern="graded assertions about hierarchical|not specifically trained for this task|clearly outperforms" path="literature/extracted/nickel_2017.txt"`

---

## Claim 11: Stated limits and future work — general properties only; multi-relational data and full Riemannian optimisation left open

> "The main focus of this work was to evaluate the general properties of hyperbolic geometry for the embedding of symbolic data."

> "In future work, we intend, to both expand the applications of Poincaré embeddings – for instance to multi-relational data – and also to derive models that are tailored to specific applications such as word embeddings."

> "We expect that a full Riemannian optimization approach can further increase the quality of the embeddings and lead to faster convergence."

**ID:** limits-future-work
**Location:** Section 5 "Discussion and Future Work"
**Grep command used:** `Grep pattern="main focus of this work|In future work, we intend|full Riemannian optimization approach" path="literature/extracted/nickel_2017.txt"`
