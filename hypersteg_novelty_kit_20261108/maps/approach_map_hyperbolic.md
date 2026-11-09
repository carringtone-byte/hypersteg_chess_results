---
generated: 2026-11-08T20:09:54+03:00
---

# Approach map — hyperbolic

Built by `tools/build_approach_map.py` from `C:\Users\user\Documents\GitHub\hypersteg_chess\hypersteg_novelty_kit_20261108\literature\verified_claims`, the features table `C:\Users\user\Documents\GitHub\hypersteg_chess\hypersteg_novelty_kit_20261108\maps\approach_features.tsv` and the technique taxonomy `C:\Users\user\Documents\GitHub\hypersteg_chess\hypersteg_novelty_kit_20261108\maps\technique_taxonomy.tsv`. View: `both`. Overview: [approach_map.md](approach_map.md).

- approaches: 1
- techniques: 1

```mermaid
flowchart LR
  subgraph fam_hyperbolic_g["hyperbolic"]
    fam_hyperbolic("hyperbolic")
    tech_hy_hyperbolic_hiding{{"Hyperbolic-space hiding"}}
    n_agarwal_2023_approach_hypersteg["HyperSteg, an autoencoder that blends message and carrier f…<br/>agarwal_2023"]
  end
  subgraph other_families["other families"]
    n_ganea_2018_approach_hyperbolic_neural_networks["generalise MLR, feed-forward and recurrent (GRU) networks t…<br/>ganea_2018<br/>family: non-steganography-foundation"]
  end
  fam_hyperbolic --- tech_hy_hyperbolic_hiding
  tech_hy_hyperbolic_hiding --- n_agarwal_2023_approach_hypersteg
  n_agarwal_2023_approach_hypersteg ==>|Depends-on| n_ganea_2018_approach_hyperbolic_neural_networks
  linkStyle 0,1 stroke:#9e9e9e,stroke-width:1px
  linkStyle 2 stroke:#6a1b9a,stroke-width:2.5px,color:#6a1b9a
  classDef stub fill:#f5f5f5,stroke:#9e9e9e,stroke-dasharray:4 3,color:#424242
  class n_ganea_2018_approach_hyperbolic_neural_networks stub
```

## Legend

| link | arrow | colour | source |
| --- | --- | --- | --- |
| taxonomy (family → technique → approach) | `---` | #9e9e9e, thin | technique taxonomy and features table |
| Supports | `-->` | #2e7d32, thick | stated by a paper (ledger edge) |
| Rebuts | `-.->` | #c62828, thick | stated by a paper (ledger edge) |
| Depends-on | `==>` | #6a1b9a, thick | stated by a paper (ledger edge) |
| Refines | `-->` | #1565c0, thick | stated by a paper (ledger edge) |
| Qualifies | `-.->` | #ef6c00, thick | stated by a paper (ledger edge) |
| Restates | `<-->` | #00838f, thick | stated by a paper (ledger edge) |
| Duplicate-of | `o--o` | #757575, thick | stated by a paper (ledger edge) |
| Supersedes | `--x` | #4e342e, thick | stated by a paper (ledger edge) |

## Techniques

| technique | parent | name | definition | grounded by | approaches |
| --- | --- | --- | --- | --- | --- |
| `hy-hyperbolic-hiding` | — | Hyperbolic-space hiding | Message and carrier features are blended in a Poincare ball rather than in Euclidean space. | `agarwal_2023:approach-hypersteg` | 1 |

## Lineage edges (1)

| source | kind | target | lifted_from | ledger line |
| --- | --- | --- | --- | --- |
| `agarwal_2023:approach-hypersteg` | Depends-on | `ganea_2018:approach-hyperbolic-neural-networks` | — | agarwal_2023.md:195 |

## Approaches

| address | name | family | technique | channel | key | access | capacity | mechanism | landable | mechanism_evidence | carrier | acquisition |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `agarwal_2023:approach-hypersteg` | HyperSteg, an autoencoder that blends message and carrier features on the Poincaré ball, built on hyperbolic neural networks | hyperbolic | hy-hyperbolic-hiding | latent-generative | — | training | — | m-hyperbolic-blending | yes | sibling:hypersteg-poincare-beta-concatenation | image or audio carrier features | weight-trained |
