---
paper: "Sarkar (2011)"
title: "Low Distortion Delaunay Embedding of Trees in Hyperbolic Plane"
doi: "10.1007/978-3-642-25878-7_34"
pmcid: "<PMC ID, if any>"
url: "In Graph Drawing: 19th International Symposium, GD 2011, Eindhoven, Revised Selected Papers, LNCS 7034, Springer, pp. 355–366; peer-reviewed version from Edinburgh Research Explorer"
source_version: "accepted manuscript"
file: "literature/sarkar_2011.pdf"
retrieved: "20261106"
verified_by: "Claude (Opus 5.5) subagent, quotes checked with verify_quotes.py (read-only run)"
# The six below are written by `verify_quotes.py --stamp` — do not hand-edit.
# They bind the ledger to the exact source/extract bytes AND its own quoted text
# (body_sha256) it was verified against, so a later quote edit is caught in CI.
source_sha256: "172111d82d89de8a1917890de5f00e62f304e9e4d228fda872f7acb8d69220fd"
extract_sha256: "bf25a2ad4ce696aedef3c3fd14d1df5bdfafb2b08c3734742ac29c76405fa4aa"
body_sha256: "d61ca4dca31f9bb551b001f68e9c091b52adf236ddb03765dc19452bc0ab6ba8"
verifier_version: "2"
verified_verdict: "pass"
verified_date: "20261106"
extract_source_sha256: "172111d82d89de8a1917890de5f00e62f304e9e4d228fda872f7acb8d69220fd"
---

# Verified Claims — Sarkar (2011)

Each claim below was extracted by reading the downloaded paper file with the Read
tool, grepping for the specific content, and reading the surrounding context to
confirm the attribution is faithful.

Source: Graph Drawing (GD 2011), LNCS 7034, Springer, pp. 355–366, DOI
10.1007/978-3-642-25878-7_34. The file is the peer-reviewed version deposited in Edinburgh
Research Explorer, with a repository cover page. Author: Rik Sarkar, Institut für Informatik,
Freie Universität Berlin. This is a geometry paper with no steganography in it; it belongs to
the hyperbolic-learning foundations behind HyperSteg (`literature/agarwal_2023.pdf`), which
`CLAUDE.md` defers until after the hackathon. Section numbers below are the paper's own; the
manuscript carries no journal page numbers.

## Claim 1: Method — embed any tree in the hyperbolic plane as the Delaunay graph of its vertices

> "This paper considers the problem of embedding trees into the hyperbolic plane. We show that any tree can be realized as the Delaunay graph of its embedded vertices."

> "We construct a functionΦ that embeds the vertices of a tree T into H. Func-tion Φ is designed such that T is the Delaunay graph of the embdded vertices."

**ID:** approach-delaunay-tree-embedding
**Location:** Abstract; Section 3 "Delaunay Embedding of Trees"
**Grep command used:** `Grep pattern="considers the problem of embedding trees|embeds the vertices of a tree T into H" path="literature/extracted/sarkar_2011.txt"`

---

## Claim 2: Construction — disjoint cones rooted at each embedded vertex, one per edge

> "But we wish to make it more general and write in terms of cones rooted at the embedded vertices. This makes it easier to handle weighted trees and low distortion embedding in following sections."

> "Given any ﬁnite integer d we can always construct d mutually disjoint cones at P by taking d diﬀerent rays and cones of suitably small angles around them."

**ID:** cone-construction
**Location:** Section 3; Section 2 "Basics and notations", Observation 1
**Grep command used:** `Grep pattern="terms of cones rooted at the embedded|mutually disjoint cones at P" path="literature/extracted/sarkar_2011.txt"`

---

## Claim 3: Weighted trees — edge weights realised as hyperbolic distances, up to a global constant

> "Particularly, a weighted tree can be em-bedded such that the weight on each edge is realized as the hyperbolic distance between its embedded vertices. Thus the embedding preserves the metric information of the tree along with its topology."

> "The eﬀect of the constant is negligible: since it is same globally, once it has been computed we can scale our unit of length to eliminate the factor."

**ID:** weighted-tree-edge-lengths
**Location:** Abstract; Section 1.2 "Our Contributions"
**Grep command used:** `Grep pattern="weight on each edge is realized|The eﬀect of the constant is negligible" path="literature/extracted/sarkar_2011.txt"`

---

## Claim 4: Distortion — non-adjacent distances distorted by less than a (1 + ε) factor for any ε

> "Further, the distance distortion between non adjacent vertices can be made arbitrar-ily small – less than a (1 + ε) factor for any given ε."

> "Thus the tree can be seen as a hyperbolic spanner of the embedded vertices."

**ID:** one-plus-epsilon-distortion
**Location:** Abstract; Section 1.2 "Our Contributions"
**Grep command used:** `Grep pattern="distance distortion between non adjacent|hyperbolic spanner of the embedded" path="literature/extracted/sarkar_2011.txt"`

---

## Claim 5: Consequences — the tree is the minimum spanning tree, and greedy routing is guaranteed

> "The Delaunay character implies useful properties such as guaranteed greedy routing and realization as minimum spanning trees."

> "The ﬁrst overcomes the constant degree bound of Euclidean case, the second implies the result of [12]."

**ID:** mst-and-greedy-routing
**Location:** Abstract; Section 1.2 "Our Contributions"
**Grep command used:** `Grep pattern="guaranteed greedy routing and realization|overcomes the constant degree bound" path="literature/extracted/sarkar_2011.txt"`

---

## Claim 6: Building on Kleinberg — generalises a tiling-based Delaunay embedding

> "The embedding in [12] is a speciﬁc Delaunay embedding based on tiling of H by ideal regular d-gons, where d is the max degree. We generalize this to not depend on a tiling, which gives greater ﬂexibility needed to create the low distortion embeddings in sections 4 and 5."

> "The basic idea is not new, and has been used in [12, 5, 19]."

**ID:** generalises-kleinberg
**Location:** Section 1.2 "Our Contributions"; Section 3
**Grep command used:** `Grep pattern="based on tiling of H by ideal regular|The basic idea is not new" path="literature/extracted/sarkar_2011.txt"`

> Note: reference [12] is Kleinberg's greedy-routing paper (Section 1.1, "Hyperbolic Embeddings"); it has no ledger here.

---

## Claim 7: Why hyperbolic — the hyperbolic metric behaves like a tree

> "The hyperbolic metric behaves like a tree in many respects."

> "This suggests hyperbolic plane as a useful general target to investigate embedding questions."

**ID:** hyperbolic-tree-like
**Location:** Section 1.1 "Related Work"; Section 6 "Conclusion"
**Grep command used:** `Grep pattern="hyperbolic metric behaves like a tree|useful general target to investigate" path="literature/extracted/sarkar_2011.txt"`

---

## Claim 8: General metrics — tree-embedding bounds carry over to the hyperbolic plane

> "It is therefore possible to embed arbitrary metrics into hyperbolic metric with the same bounds, using the tree embedding as an intermediate step."

> "From [9] we have that for any metric, there is a distribution over embeddings in the hyperbolic plane with expected distor-tion O(logn)."

**ID:** general-metric-bounds
**Location:** Section 1.2 "Our Contributions"; Section 5
**Grep command used:** `Grep pattern="embed arbitrary metrics into hyperbolic|distribution over embeddings in the hyperbolic plane" path="literature/extracted/sarkar_2011.txt"`

---

## Claim 9: Stated limits — Poincaré-disk realisation omitted for space; further properties left open

> "Translating our algorithms to one of these models is fairly simple, based on M¨ obius transformations applied to the individual edges. We omit the detailed description for lack of space."

> "It remains to be seen what additional properties can be obtained in H, for the more general embedding questions."

> "Details of proofs can be found in the full version of the paper online [18]."

**ID:** stated-limitations
**Location:** Section 5 "Embedding into Euclidean Models"; Section 6 "Conclusion"; Section 1.2
**Grep command used:** `Grep pattern="We omit the detailed description for lack of space|It remains to be seen what additional|Details of proofs can be found" path="literature/extracted/sarkar_2011.txt"`
