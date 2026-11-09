---
paper: "Cetin et al. (2022)"
title: "Hyperbolic Deep Reinforcement Learning"
doi: ""
pmcid: ""
url: "https://arxiv.org/abs/2210.01542 (arXiv HTML rendering of v1, 04 Oct 2022)"
source_version: "preprint"
file: "literature/cetin_2022.html"
retrieved: "20261105"
verified_by: "Claude (Opus 5.5) subagent, hyperbolic strand, quotes checked with verify_quotes.py (read-only run)"
# The six below are written by `verify_quotes.py --stamp` — do not hand-edit.
# They bind the ledger to the exact source/extract bytes AND its own quoted text
# (body_sha256) it was verified against, so a later quote edit is caught in CI.
source_sha256: "8525f7c162d0400959ad1bb5a0a33cc403308187f7829bf6a14d59decaa8efae"
extract_sha256: "1249be95367a197b71f146f41ca4b697fe1903838989e8af2036d305f9c5bed0"
body_sha256: "e2150e378bbc826e48518981090ed51d20ed62cb3bddea4e71510dc37828f9b4"
verifier_version: "2"
verified_verdict: "pass"
verified_date: "20261106"
extract_source_sha256: "8525f7c162d0400959ad1bb5a0a33cc403308187f7829bf6a14d59decaa8efae"
---

# Verified Claims — Cetin et al. (2022)

Each claim below was extracted by reading the downloaded paper file with the Read
tool, grepping for the specific content, and reading the surrounding context to
confirm the attribution is faithful.

Source: arXiv:2210.01542v1 [cs.LG], HTML rendering. Authors: Edoardo Cetin (King's College
London; work done during a Twitter internship), Benjamin Chamberlain, Michael Bronstein and
Jonathan J Hunt (Twitter). No DOI is printed in the extract. Locations are by section or by
the paragraph label the extract keeps; the HTML has no page numbers. This is a reinforcement
learning paper, not a steganography paper. It is ledgered as a foundation of the hyperbolic
framing behind HyperSteg (`literature/verified_claims/agarwal_2023.md`), and because it applies
hyperbolic representations to agents playing video games (Procgen and Atari), with the state of
the game read as a tree of possible branches. `xia_2026` carries the same idea to LLM agents
searching over moves in an AlphaZero-like loop.

## Claim 1: Approach — deep RL agents whose latent state representations live in hyperbolic space, stabilised by S-RYM

> "We propose a new class of deep reinforcement learning (RL) algorithms that model latent representations in hyperbolic space."

> "In particular, we design  spectrally-regularized hyperbolic mappings  (S-RYM), a simple recipe combining scaling and spectral normalization  ( Miyato et al., 2018 )  that stabilizes the learned hyperbolic representations and enables their seamless integration with deep RL."

**ID:** approach-hyperbolic-rl-srym
**Location:** Abstract; Section 1 "Introduction"
**Grep command used:** `Grep pattern="We propose a new class of deep reinforcement|spectrally-regularized hyperbolic mappings  \(S-RYM\)" path="literature/extracted/cetin_2022.txt"`

---

## Claim 2: What the geometry represents — the evolution of an MDP's state as a tree of possible branches

> "The evolution of the state in a Markov decision process can be conceptualized as a tree, with the policy and dynamics determining the possible branches."

> "Consequently, we hypothesize that deep RL models should prioritize encoding precisely  hierarchically-structured  features to facilitate learning effective and generalizable policies."

> "In contrast, we note that non-evolving features, such as the aesthetic properties of elements in the environment, are often linked with spurious correlations, hindering generalization to new states"

**ID:** mdp-state-tree
**Location:** Section 1
**Grep command used:** `Grep pattern="conceptualized as a tree|prioritize encoding precisely|non-evolving features" path="literature/extracted/cetin_2022.txt"`

---

## Claim 3: Geometry — exponential volume growth makes hyperbolic space a continuous analogue of trees; geodesics pass near a shared parent

> "A defining property of hyperbolic space is  exponential volume growth , which enables the embedding of tree-like hierarchical data with low distortion using only a few dimensions  ( Sarkar, 2011 ) ."

> "From these characteristics, hyperbolic spaces can be viewed as a continuous analog of trees."

> "Visually, this makes geodesics between distinct points pass through some midpoint with lower magnitude, analogously to how tree geodesics between nodes (defined as the shortest path in their graph) must cross their closest shared parent"

**ID:** continuous-analogue-of-trees
**Location:** Section 1; Section 2 (hyperbolic geometry background), Figure 2
**Grep command used:** `Grep pattern="exponential volume growth , which enables|continuous analog of trees|closest shared parent" path="literature/extracted/cetin_2022.txt"`

---

## Claim 4: Built on HNN operations — gyrovector spaces following Ganea et al.; a hybrid network with an exponential map before hyperbolic affine heads

> "Following  Ganea et al. (2018) , we consider the framework of  gyrovector spaces   ( Ungar, 2008 )  to extend common vector operations to non-Euclidean geometries"

> "We use the exponential map from the origin of the Poincaré ball to map Euclidean input vectors"

> "we employ these operations to parameterize  hybrid  neural networks: we first process the input data"

**ID:** hybrid-network-on-hnn
**Location:** Section 2, "Key operations for learning"
**Grep command used:** `Grep pattern="Following  Ganea et al. \(2018\)|exponential map from the origin of the Poincaré ball|parameterize  hybrid  neural networks" path="literature/extracted/cetin_2022.txt"`

**Depends-on:** ganea_2018:approach-hyperbolic-neural-networks (grounded by #hybrid-network-on-hnn)

---

## Claim 5: Diagnostic — relative δ-hyperbolicity of learned representations, where 0 is tree-like and 1 is non-hyperbolic; performance tracks it

> "Thus, we can interpret  δ \delta -hyperbolicity as measuring the deviation of a given metric from an exact tree metric."

> "which can span values between 0 (hyperbolic hierarchical tree-like structure) and 1 (perfectly non-hyperbolic spaces)."

> "In line with our intuition, we show that performance improvements of RL algorithms correlate with the increasing  hyperbolicity  of the discrete space spanned by their latent representations."

**ID:** delta-hyperbolicity-diagnostic
**Location:** Section 1; Section 3 "Hyperbolic representations for reinforcement learning", "δ-hyperbolicity", Figure 4 (computed with the Fournier et al. 2015 algorithm, normalised by the diameter)
**Grep command used:** `Grep pattern="deviation of a given metric from an exact tree|perfectly non-hyperbolic spaces|correlate with the increasing" path="literature/extracted/cetin_2022.txt"`

---

## Claim 6: Failure of existing practice — naive hyperbolic RL is unstable because RL gradients are non-stationary and high-variance

> "However, applying existing methodologies from the hyperbolic deep learning literature leads to fatal optimization instabilities due to the non-stationarity and variance characterizing RL gradient estimators."

> "We attribute the observed optimization challenges from our naive hyperbolic PPO implementation to the high variance and non-stationarity characterizing RL."

**ID:** naive-integration-unstable
**Location:** Abstract; Section 3, "Naive integration", Figure 6
**Grep command used:** `Grep pattern="fatal optimization instabilities|We attribute the observed optimization challenges" path="literature/extracted/cetin_2022.txt"`

---

## Claim 7: S-RYM in detail — spectral normalisation in the Euclidean encoder only, plus rescaling by 1/√n

> "First, we apply SN only in the Euclidean encoder sub-network ( f E f_{E} ), leaving the final linear transformation in hyperbolic space ( f H f_{H} ) unregularized since our instabilities appear to occur in the gradients  from  the hyperbolic representations. Furthermore, we add a scaling term to preserve stability for different latent representation sizes."

> "To validate that these performance benefits are due to the hyperbolic geometry of the latent space, we also compare with another Euclidean ablation making use of SN, which fails to attain any improvement."

**ID:** srym-spectral-norm-ablation
**Location:** Section 3, "S-RYM" and "Results", Figure 7 (App. E.1: both SN and rescaling are needed)
**Grep command used:** `Grep pattern="we apply SN only in the Euclidean encoder|another Euclidean ablation making use of SN" path="literature/extracted/cetin_2022.txt"`

---

## Claim 8: Results — gains on 13 of 16 Procgen tasks with 32-dimensional representations and on 22 of 26 Atari 100K games

> "At the same time, reducing the size of the representations provides even further benefits with significant improvements in 13/16 tasks."

> "In particular, we record improvements on 22/26 Atari environments over the Euclidean baseline, almost doubling the final human normalized score."

**ID:** procgen-atari-results
**Location:** Section 4, "Generalization on Procgen", Table 1; "Sample-efficiency on Atari 100K", Figure 9 and Table 2 (PPO and Rainbow DQN; 5 seeds)
**Grep command used:** `Grep pattern="significant improvements in 13/16|improvements on 22/26 Atari" path="literature/extracted/cetin_2022.txt"`

---

## Claim 9: Interpretation — in two dimensions the representations form trees, and their magnitude rises as obstacles appear

> "We observe a recurring  cyclical  behavior, where the magnitude of the representations monotonically increases within subsets of the trajectory as more obstacles/enemies appear."

> "We observe the representations form tree-like structures, with the magnitudes in the on-policy states growing in the direction of the Value function’s  gyroplane ’s normal."

**ID:** magnitude-tracks-opportunity
**Location:** Section 4, "Representations interpretation", Figures 10 and 12
**Grep command used:** `Grep pattern="recurring  cyclical  behavior|representations form tree-like structures" path="literature/extracted/cetin_2022.txt"`

---

## Claim 10: Magnitude as uncertainty — on CIFAR10 the highest-magnitude representations are classified far more accurately

> "on CIFAR10 the test performance on the images with representations’s with the top 5% magnitudes is 97.17%, while for the bottom 5% is 79.64%."

> "it appears that the hyperbolic hierarchical structure serves to encode the degree of uncertainty to disambiguate between multiple image labels"

**ID:** magnitude-encodes-uncertainty
**Location:** Appendix (image classification with S-RYM, ResNet18), Figure 11
**Grep command used:** `Grep pattern="top 5% magnitudes is 97.17%|encode the degree of uncertainty" path="literature/extracted/cetin_2022.txt"`

---

## Claim 11: Known difficulties and limits — numerical issues near the origin and the border; S-RYM's regularisation may be more restrictive than needed

> "For instance, numerical issues and vanishing gradients occur as representations get too close to either the origin or the boundary of the Poincaré ball  ( Ganea et al., 2018 ) ."

> "These empirical insights could inform future improvements for S-RYM to retain the stability benefits of SN with less restrictive regularization."

**ID:** limits-numerics-regularisation
**Location:** Appendix (related work on stabilising hyperbolic representations; spectral normalisation in RL)
**Grep command used:** `Grep pattern="numerical issues and vanishing gradients occur|less restrictive regularization" path="literature/extracted/cetin_2022.txt"`
