---
generated: 2026-11-08T20:09:54+03:00
---

# Approach map — non-steganography-foundation

Built by `tools/build_approach_map.py` from `C:\Users\user\Documents\GitHub\hypersteg_chess\hypersteg_novelty_kit_20261108\literature\verified_claims`, the features table `C:\Users\user\Documents\GitHub\hypersteg_chess\hypersteg_novelty_kit_20261108\maps\approach_features.tsv` and the technique taxonomy `C:\Users\user\Documents\GitHub\hypersteg_chess\hypersteg_novelty_kit_20261108\maps\technique_taxonomy.tsv`. View: `both`. Overview: [approach_map.md](approach_map.md).

- approaches: 35
- techniques: 12

```mermaid
flowchart LR
  subgraph fam_non_steganography_foundation_g["non-steganography-foundation"]
    fam_non_steganography_foundation("non-steganography-foundation")
    tech_nsf_chess_language{{"Chess language and commentary"}}
    tech_nsf_chess_language_models{{"Chess language models and datasets"}}
    tech_nsf_commentary_evaluation{{"Commentary evaluation"}}
    tech_nsf_commentary_generation{{"Commentary generation"}}
    tech_nsf_engine_and_opening_analysis{{"Engine and opening-tree analysis"}}
    tech_nsf_engine_benchmark_assessment{{"Engine-benchmarked skill assessment"}}
    tech_nsf_human_move_models{{"Models of human move choice"}}
    tech_nsf_hyperbolic_embeddings{{"Hyperbolic embeddings and measurement"}}
    tech_nsf_hyperbolic_networks{{"Hyperbolic network layers and agents"}}
    tech_nsf_intrinsic_rating{{"Intrinsic rating models"}}
    tech_nsf_llm_chess_play{{"LLM chess play"}}
    tech_nsf_neural_human_move{{"Neural human-move predictors"}}
    n_biswas_2015_approach_3p_framework["a framework that separates Performance from Prediction and …<br/>biswas_2015"]
    n_biswas_2015_surveyed_average_difference["average difference (AD) and its scaled form (ASD): centipaw…<br/>biswas_2015"]
    n_biswas_2015_surveyed_move_matching["move matching (MM) and equal-value matching (EV): agreement…<br/>biswas_2015"]
    n_biswas_2015_surveyed_skilloscopy["Skilloscopy (SK): Bayesian updating of belief over benchmar…<br/>biswas_2015"]
    n_biswas_2015_surveyed_sr_all_depths["SR over all search depths (SRA): a move that ranks top earl…<br/>biswas_2015"]
    n_biswas_2015_surveyed_statistical_regression["statistical regression (SR): fit the stochastic benchmark p…<br/>biswas_2015"]
    n_blasius_2009_approach_opening_fragmentation_model["a measured opening-popularity law and its generating model:…<br/>blasius_2009"]
    n_cetin_2022_approach_hyperbolic_rl_srym["deep RL agents whose latent state representations live in h…<br/>cetin_2022"]
    n_chen_2021_approach_poincare_probe["a Poincaré probe that projects BERT embeddings into a Poinc…<br/>chen_2021"]
    n_feng_2023_approach_chess_language_benchmark["a chess game-and-language dataset with an evaluation framew…<br/>feng_2023"]
    n_feng_2023_approach_chessclip["ChessCLIP, contrastive training on board-history/move and a…<br/>feng_2023"]
    n_feng_2023_approach_chessgpt["ChessGPT, a GPT-like model trained by causal language model…<br/>feng_2023"]
    n_ganea_2018_approach_hyperbolic_neural_networks["generalise MLR, feed-forward and recurrent (GRU) networks t…<br/>ganea_2018"]
    n_he_2024_approach_hierarchy_transformer["re-train transformer encoders as Hierarchy Transformer enco…<br/>he_2024"]
    n_jhamtani_2018_approach_gac["GAC, an end-to-end neural generator that selects salient bo…<br/>jhamtani_2018"]
    n_kim_2024_approach_ccc["CCC, concept vectors from a chess expert model, prioritised…<br/>kim_2024"]
    n_kim_2024_approach_gcc_eval["GCC-Eval, G-Eval extended with expert-engine input to score…<br/>kim_2024"]
    n_kolasani_2025_approach_llm_chess_benchmark["LLM Chess: an agentic benchmark in which models play whole …<br/>kolasani_2025"]
    n_maia2_2024_approach_maia2["Maia-2, one model that fuses encoded skill levels and posit…<br/>maia2_2024"]
    n_mcilroyyoung_2020_approach_blunder_predictor["blunder prediction, a residual CNN that labels a move a blu…<br/>mcilroyyoung_2020"]
    n_mcilroyyoung_2020_approach_maia["Maia, AlphaZero's architecture retrained on human games to …<br/>mcilroyyoung_2020"]
    n_nickel_2017_approach_poincare_embeddings["embed symbolic data in an n-dimensional Poincaré ball to ca…<br/>nickel_2017"]
    n_regan_2011_approach_intrinsic_rating_model["an intrinsic-rating model of human move choice: engine eval…<br/>regan_2011"]
    n_regan_2012_approach_intrinsic_performance_ratings["a refined Regan–Haworth model applied to whole populations:…<br/>regan_2012"]
    n_sala_2018_approach_combinatorial_construction["a combinatorial construction that embeds a tree in hyperbol…<br/>sala_2018"]
    n_sala_2018_approach_h_mds["hyperbolic multidimensional scaling (h-MDS): exact recovery…<br/>sala_2018"]
    n_sala_2018_approach_pytorch_sgd_pga["an SGD algorithm in PyTorch, initialised by h-MDS, recovers…<br/>sala_2018"]
    n_sarkar_2011_approach_delaunay_tree_embedding["Method — embed any tree in the hyperbolic plane as the Dela…<br/>sarkar_2011"]
    n_shimizu_2020_approach_hnn_plus_plus["a parameter-reduced MLR, FC, convolutional and attention la…<br/>shimizu_2020"]
    n_shimizu_2020_approach_poincare_beta_concatenation["Poincaré β-concatenation: map inputs to the tangent space, …<br/>shimizu_2020"]
    n_tomasev_2020_approach_insilico_variant_assessment["in-silico assessment of chess variants, by training AlphaZe…<br/>tomasev_2020"]
    n_tomasev_2020_approach_prior_entropy_diversity["opening diversity measured as the entropy of the first 20 p…<br/>tomasev_2020"]
    n_xia_2026_approach_lapha["LaPha, AlphaZero-like LLM agents trained in a root-centred …<br/>xia_2026"]
    n_yang_2024_approach_hyplora["HypLoRA, low-rank adaptation performed directly on the hype…<br/>yang_2024"]
    n_yang_2026_approach_hyperbolicity_atlas["a Gromov-hyperbolicity atlas of prompt-token hidden states …<br/>yang_2026"]
    paper_shimizu_2020(["shimizu_2020<br/>(paper)"])
  end
  subgraph other_families["other families"]
    n_agarwal_2023_approach_hypersteg["HyperSteg, an autoencoder that blends message and carrier f…<br/>agarwal_2023<br/>family: hyperbolic"]
    n_boonstra_2024_approach_bayesian_hidden_code_forensics["a Bayesian forensic framework for alleged hidden codes in s…<br/>boonstra_2024<br/>family: steganalysis"]
  end
  fam_non_steganography_foundation --- tech_nsf_chess_language
  tech_nsf_chess_language --- tech_nsf_chess_language_models
  tech_nsf_chess_language --- tech_nsf_commentary_evaluation
  tech_nsf_chess_language --- tech_nsf_commentary_generation
  fam_non_steganography_foundation --- tech_nsf_engine_and_opening_analysis
  tech_nsf_human_move_models --- tech_nsf_engine_benchmark_assessment
  fam_non_steganography_foundation --- tech_nsf_human_move_models
  fam_non_steganography_foundation --- tech_nsf_hyperbolic_embeddings
  fam_non_steganography_foundation --- tech_nsf_hyperbolic_networks
  tech_nsf_human_move_models --- tech_nsf_intrinsic_rating
  fam_non_steganography_foundation --- tech_nsf_llm_chess_play
  tech_nsf_human_move_models --- tech_nsf_neural_human_move
  tech_nsf_engine_benchmark_assessment --- n_biswas_2015_approach_3p_framework
  tech_nsf_engine_benchmark_assessment --- n_biswas_2015_surveyed_average_difference
  tech_nsf_engine_benchmark_assessment --- n_biswas_2015_surveyed_move_matching
  tech_nsf_engine_benchmark_assessment --- n_biswas_2015_surveyed_skilloscopy
  tech_nsf_engine_benchmark_assessment --- n_biswas_2015_surveyed_sr_all_depths
  tech_nsf_engine_benchmark_assessment --- n_biswas_2015_surveyed_statistical_regression
  tech_nsf_engine_and_opening_analysis --- n_blasius_2009_approach_opening_fragmentation_model
  tech_nsf_hyperbolic_networks --- n_cetin_2022_approach_hyperbolic_rl_srym
  tech_nsf_hyperbolic_embeddings --- n_chen_2021_approach_poincare_probe
  tech_nsf_chess_language_models --- n_feng_2023_approach_chess_language_benchmark
  tech_nsf_chess_language_models --- n_feng_2023_approach_chessclip
  tech_nsf_chess_language_models --- n_feng_2023_approach_chessgpt
  tech_nsf_hyperbolic_networks --- n_ganea_2018_approach_hyperbolic_neural_networks
  tech_nsf_hyperbolic_embeddings --- n_he_2024_approach_hierarchy_transformer
  tech_nsf_commentary_generation --- n_jhamtani_2018_approach_gac
  tech_nsf_commentary_generation --- n_kim_2024_approach_ccc
  tech_nsf_commentary_evaluation --- n_kim_2024_approach_gcc_eval
  tech_nsf_llm_chess_play --- n_kolasani_2025_approach_llm_chess_benchmark
  tech_nsf_neural_human_move --- n_maia2_2024_approach_maia2
  tech_nsf_neural_human_move --- n_mcilroyyoung_2020_approach_blunder_predictor
  tech_nsf_neural_human_move --- n_mcilroyyoung_2020_approach_maia
  tech_nsf_hyperbolic_embeddings --- n_nickel_2017_approach_poincare_embeddings
  tech_nsf_intrinsic_rating --- n_regan_2011_approach_intrinsic_rating_model
  tech_nsf_intrinsic_rating --- n_regan_2012_approach_intrinsic_performance_ratings
  tech_nsf_hyperbolic_embeddings --- n_sala_2018_approach_combinatorial_construction
  tech_nsf_hyperbolic_embeddings --- n_sala_2018_approach_h_mds
  tech_nsf_hyperbolic_embeddings --- n_sala_2018_approach_pytorch_sgd_pga
  tech_nsf_hyperbolic_embeddings --- n_sarkar_2011_approach_delaunay_tree_embedding
  tech_nsf_hyperbolic_networks --- n_shimizu_2020_approach_hnn_plus_plus
  tech_nsf_hyperbolic_networks --- n_shimizu_2020_approach_poincare_beta_concatenation
  tech_nsf_engine_and_opening_analysis --- n_tomasev_2020_approach_insilico_variant_assessment
  tech_nsf_engine_and_opening_analysis --- n_tomasev_2020_approach_prior_entropy_diversity
  tech_nsf_hyperbolic_networks --- n_xia_2026_approach_lapha
  tech_nsf_hyperbolic_networks --- n_yang_2024_approach_hyplora
  tech_nsf_hyperbolic_embeddings --- n_yang_2026_approach_hyperbolicity_atlas
  n_agarwal_2023_approach_hypersteg ==>|Depends-on| n_ganea_2018_approach_hyperbolic_neural_networks
  n_biswas_2015_surveyed_average_difference <-->|Restates| n_regan_2012_approach_intrinsic_performance_ratings
  n_biswas_2015_surveyed_statistical_regression <-->|Restates| n_regan_2011_approach_intrinsic_rating_model
  n_boonstra_2024_approach_bayesian_hidden_code_forensics ==>|Depends-on| n_regan_2011_approach_intrinsic_rating_model
  n_cetin_2022_approach_hyperbolic_rl_srym ==>|Depends-on| n_ganea_2018_approach_hyperbolic_neural_networks
  n_chen_2021_approach_poincare_probe ==>|Depends-on| n_ganea_2018_approach_hyperbolic_neural_networks
  n_ganea_2018_approach_hyperbolic_neural_networks ==>|Depends-on| n_nickel_2017_approach_poincare_embeddings
  n_kim_2024_approach_ccc ==>|Depends-on| n_jhamtani_2018_approach_gac
  n_maia2_2024_approach_maia2 -->|Refines| n_mcilroyyoung_2020_approach_maia
  n_maia2_2024_approach_maia2 --x|Supersedes| n_mcilroyyoung_2020_approach_maia
  n_regan_2012_approach_intrinsic_performance_ratings -->|Refines| n_regan_2011_approach_intrinsic_rating_model
  paper_shimizu_2020 -->|Refines| n_ganea_2018_approach_hyperbolic_neural_networks
  n_xia_2026_approach_lapha ==>|Depends-on| n_nickel_2017_approach_poincare_embeddings
  n_yang_2024_approach_hyplora ==>|Depends-on| n_cetin_2022_approach_hyperbolic_rl_srym
  n_yang_2024_approach_hyplora -.->|Qualifies| n_ganea_2018_approach_hyperbolic_neural_networks
  linkStyle 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46 stroke:#9e9e9e,stroke-width:1px
  linkStyle 47,50,51,52,53,54,59,60 stroke:#6a1b9a,stroke-width:2.5px,color:#6a1b9a
  linkStyle 48,49 stroke:#00838f,stroke-width:2.5px,color:#00838f
  linkStyle 55,57,58 stroke:#1565c0,stroke-width:2.5px,color:#1565c0
  linkStyle 56 stroke:#4e342e,stroke-width:2.5px,color:#4e342e
  linkStyle 61 stroke:#ef6c00,stroke-width:2.5px,color:#ef6c00
  classDef stub fill:#f5f5f5,stroke:#9e9e9e,stroke-dasharray:4 3,color:#424242
  class n_agarwal_2023_approach_hypersteg,n_boonstra_2024_approach_bayesian_hidden_code_forensics stub
  classDef nonlanding fill:#eeeeee,stroke:#bdbdbd,stroke-dasharray:2 2,color:#9e9e9e
  class tech_nsf_chess_language,tech_nsf_chess_language_models,tech_nsf_commentary_evaluation,tech_nsf_commentary_generation,tech_nsf_engine_and_opening_analysis,tech_nsf_engine_benchmark_assessment,tech_nsf_human_move_models,tech_nsf_hyperbolic_embeddings,tech_nsf_hyperbolic_networks,tech_nsf_intrinsic_rating,tech_nsf_llm_chess_play,tech_nsf_neural_human_move nonlanding
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

Muted, dashed nodes are marked not a landing node: they group the tree, and a novelty audit does not place a scheme at one. A child of such a node is one too unless its row says `landing: yes`.

## Techniques

| technique | parent | name | definition | grounded by | approaches |
| --- | --- | --- | --- | --- | --- |
| `nsf-chess-language` | — | Chess language and commentary (not a landing node) | Models and data that join chess positions and natural-language text. | `feng_2023:approach-chess-language-benchmark` | 6 |
| `nsf-chess-language-models` | nsf-chess-language | Chess language models and datasets (not a landing node) | Language models and contrastive models trained on games paired with chess text. | `feng_2023:approach-chessgpt` | 3 |
| `nsf-commentary-evaluation` | nsf-chess-language | Commentary evaluation (not a landing node) | LLM judges, given engine input, score commentary quality. | `kim_2024:approach-gcc-eval` | 1 |
| `nsf-commentary-generation` | nsf-chess-language | Commentary generation (not a landing node) | Systems that write commentary on moves from engine and game features. | `jhamtani_2018:approach-gac` | 2 |
| `nsf-engine-and-opening-analysis` | — | Engine and opening-tree analysis (not a landing node) | Engines and game databases are used to measure opening breadth, popularity or variant balance. | `tomasev_2020:approach-prior-entropy-diversity` | 3 |
| `nsf-engine-benchmark-assessment` | nsf-human-move-models | Engine-benchmarked skill assessment (not a landing node) | A player's moves are compared with an engine's choices, for example as the percentage that match, to measure skill or detect cheating. | `biswas_2015:surveyed-move-matching` | 6 |
| `nsf-human-move-models` | — | Models of human move choice (not a landing node) | Statistical or neural models of which move a human of given strength plays; candidate cover distributions or warden models for move-choice channels. | `regan_2011:approach-intrinsic-rating-model` | 11 |
| `nsf-hyperbolic-embeddings` | — | Hyperbolic embeddings and measurement (not a landing node) | Methods that place data or model states in hyperbolic space, or measure how hyperbolic they are. | `nickel_2017:approach-poincare-embeddings` | 8 |
| `nsf-hyperbolic-networks` | — | Hyperbolic network layers and agents (not a landing node) | Neural layers, adapters and RL agents that compute in hyperbolic space. | `ganea_2018:approach-hyperbolic-neural-networks` | 6 |
| `nsf-intrinsic-rating` | nsf-human-move-models | Intrinsic rating models (not a landing node) | Engine evaluations of the reasonable moves give each a probability, fitted to players' skill. | `regan_2011:approach-intrinsic-rating-model` | 2 |
| `nsf-llm-chess-play` | — | LLM chess play (not a landing node) | Benchmarks that measure how well language models play chess, with no hidden message. | `kolasani_2025:approach-llm-chess-benchmark` | 1 |
| `nsf-neural-human-move` | nsf-human-move-models | Neural human-move predictors (not a landing node) | Networks trained on human games predict the human move or mistake at a given rating. | `mcilroyyoung_2020:approach-maia` | 3 |

## Lineage edges (15)

| source | kind | target | lifted_from | ledger line |
| --- | --- | --- | --- | --- |
| `agarwal_2023:approach-hypersteg` | Depends-on | `ganea_2018:approach-hyperbolic-neural-networks` | — | agarwal_2023.md:195 |
| `biswas_2015:surveyed-average-difference` | Restates | `regan_2012:approach-intrinsic-performance-ratings` | `regan_2012:scaled-error` | biswas_2015.md:120 |
| `biswas_2015:surveyed-statistical-regression` | Restates | `regan_2011:approach-intrinsic-rating-model` | `regan_2011:sensitivity-competence` | biswas_2015.md:134 |
| `boonstra_2024:approach-bayesian-hidden-code-forensics` | Depends-on | `regan_2011:approach-intrinsic-rating-model` | `boonstra_2024:chess-extension-move-quality` | boonstra_2024.md:185 |
| `cetin_2022:approach-hyperbolic-rl-srym` | Depends-on | `ganea_2018:approach-hyperbolic-neural-networks` | `cetin_2022:hybrid-network-on-hnn` | cetin_2022.md:91 |
| `chen_2021:approach-poincare-probe` | Depends-on | `ganea_2018:approach-hyperbolic-neural-networks` | `chen_2021:probe-construction-on-hnn` | chen_2021.md:92 |
| `ganea_2018:approach-hyperbolic-neural-networks` | Depends-on | `nickel_2017:approach-poincare-embeddings` | `ganea_2018:builds-on-poincare-embeddings` | ganea_2018.md:75 |
| `kim_2024:approach-ccc` | Depends-on | `jhamtani_2018:approach-gac` | `jhamtani_2018:commentary-corpus` | kim_2024.md:189 |
| `maia2_2024:approach-maia2` | Refines | `mcilroyyoung_2020:approach-maia` | — | maia2_2024.md:149 |
| `maia2_2024:approach-maia2` | Supersedes | `mcilroyyoung_2020:approach-maia` | `maia2_2024:supersedes-maia1` | maia2_2024.md:150 |
| `paper:shimizu_2020` | Refines | `ganea_2018:approach-hyperbolic-neural-networks` | `shimizu_2020:refines-hnn`, `shimizu_2020:concatenation-versus-hnn`, `ganea_2018:hyperbolic-concatenation` | shimizu_2020.md:76, shimizu_2020.md:134 |
| `regan_2012:approach-intrinsic-performance-ratings` | Refines | `regan_2011:approach-intrinsic-rating-model` | — | regan_2012.md:138 |
| `xia_2026:approach-lapha` | Depends-on | `nickel_2017:approach-poincare-embeddings` | `xia_2026:transfers-poincare-insight` | xia_2026.md:92 |
| `yang_2024:approach-hyplora` | Depends-on | `cetin_2022:approach-hyperbolic-rl-srym` | `yang_2024:token-delta-hyperbolicity`, `cetin_2022:delta-hyperbolicity-diagnostic` | yang_2024.md:61 |
| `yang_2024:approach-hyplora` | Qualifies | `ganea_2018:approach-hyperbolic-neural-networks` | `yang_2024:tangent-space-cancellation` | yang_2024.md:93 |

## Approaches

| address | name | family | technique | channel | key | access | capacity | mechanism | landable | mechanism_evidence | carrier | acquisition |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `biswas_2015:approach-3p-framework` | a framework that separates Performance from Prediction and quantifies Profiling, for methods that judge the intrinsic merit of moves | non-steganography-foundation | nsf-engine-benchmark-assessment | move choice | — | — | — | m-human-move-models | no | own | — | — |
| `biswas_2015:surveyed-average-difference` | average difference (AD) and its scaled form (ASD): centipawns lost against the engine, scaled by the size of the advantage after Regan's finding | non-steganography-foundation | nsf-engine-benchmark-assessment | move choice | — | — | — | m-engine-benchmark-assessment | no | own | — | — |
| `biswas_2015:surveyed-move-matching` | move matching (MM) and equal-value matching (EV): agreement with the engine's choice; a cheater can lower the match rate cheaply | non-steganography-foundation | nsf-engine-benchmark-assessment | move choice | — | — | — | m-engine-benchmark-assessment | no | own | — | — |
| `biswas_2015:surveyed-skilloscopy` | Skilloscopy (SK): Bayesian updating of belief over benchmark players of defined competence, move by move | non-steganography-foundation | nsf-engine-benchmark-assessment | move choice | — | — | — | m-engine-benchmark-assessment | no | own | — | — |
| `biswas_2015:surveyed-sr-all-depths` | SR over all search depths (SRA): a move that ranks top early in the search is likelier to be played | non-steganography-foundation | nsf-engine-benchmark-assessment | move choice | — | — | — | m-engine-benchmark-assessment; m-intrinsic-rating | no | own;own | — | — |
| `biswas_2015:surveyed-statistical-regression` | statistical regression (SR): fit the stochastic benchmark player whose competence best explains the moves; frequentist, with z-scores | non-steganography-foundation | nsf-engine-benchmark-assessment | move choice | — | — | — | m-intrinsic-rating | no | own | — | — |
| `blasius_2009:approach-opening-fragmentation-model` | a measured opening-popularity law and its generating model: opening frequencies are power-law with depth-dependent exponent, pooled weights obey Zipf's law, and a random multiplicative fragmentation of the game tree with arcsine branching ratios reproduces both | non-steganography-foundation | nsf-engine-and-opening-analysis | other (not a hiding channel; opening-popularity statistics) | — | — | — | m-opening-and-engine-analysis | no | own | — | — |
| `cetin_2022:approach-hyperbolic-rl-srym` | deep RL agents whose latent state representations live in hyperbolic space, stabilised by S-RYM | non-steganography-foundation | nsf-hyperbolic-networks | — | — | training | — | m-hyperbolic-networks | no | own | — | — |
| `chen_2021:approach-poincare-probe` | a Poincaré probe that projects BERT embeddings into a Poincaré subspace with explicit hierarchies | non-steganography-foundation | nsf-hyperbolic-embeddings | — | — | weights, training | — | m-hyperbolic-embeddings | no | own | — | — |
| `feng_2023:approach-chess-language-benchmark` | a chess game-and-language dataset with an evaluation framework, as a benchmark for policy and language together | non-steganography-foundation | nsf-chess-language-models | other (not a hiding channel; dataset and benchmark) | — | — | — | m-chess-language-models | no | own | — | — |
| `feng_2023:approach-chessclip` | ChessCLIP, contrastive training on board-history/move and annotation pairs to align policy and language | non-steganography-foundation | nsf-chess-language-models | other (not a hiding channel; policy-language alignment) | — | training | — | m-chess-language-models | no | own | — | — |
| `feng_2023:approach-chessgpt` | ChessGPT, a GPT-like model trained by causal language modelling on all the chess game and language data | non-steganography-foundation | nsf-chess-language-models | other (not a hiding channel; chess language model) | — | training | — | m-chess-language-models | no | own | — | — |
| `ganea_2018:approach-hyperbolic-neural-networks` | generalise MLR, feed-forward and recurrent (GRU) networks to the Poincaré ball via gyrovector spaces | non-steganography-foundation | nsf-hyperbolic-networks | — | — | training | — | m-hyperbolic-networks | no | own | — | — |
| `he_2024:approach-hierarchy-transformer` | re-train transformer encoders as Hierarchy Transformer encoders (HiTs) in a Poincaré ball with curvature set by dimension | non-steganography-foundation | nsf-hyperbolic-embeddings | — | — | weights, training | — | m-hyperbolic-embeddings | no | own | — | — |
| `jhamtani_2018:approach-gac` | GAC, an end-to-end neural generator that selects salient board features and decodes commentary with an LSTM | non-steganography-foundation | nsf-commentary-generation | other (not a hiding channel; commentary generator and corpus) | — | training | — | m-commentary-generation | no | own | — | — |
| `kim_2024:approach-ccc` | CCC, concept vectors from a chess expert model, prioritised by the move, handed to an LLM that writes the comment | non-steganography-foundation | nsf-commentary-generation | other (not a hiding channel; LLM commentary generator) | — | prompt | — | m-commentary-generation | no | own | — | — |
| `kim_2024:approach-gcc-eval` | GCC-Eval, G-Eval extended with expert-engine input to score chess commentary on four dimensions | non-steganography-foundation | nsf-commentary-evaluation | other (not a hiding channel; LLM-based commentary evaluator) | — | prompt | — | m-commentary-evaluation | no | own | — | — |
| `kolasani_2025:approach-llm-chess-benchmark` | LLM Chess: an agentic benchmark in which models play whole games through tool calls, ranked against a random opponent and, for the strongest, given an Elo against a configurable engine | non-steganography-foundation | nsf-llm-chess-play | — | — | — | — | m-llm-chess-play | no | own | — | — |
| `maia2_2024:approach-maia2` | Maia-2, one model that fuses encoded skill levels and positions by skill-aware attention, built on Maia | non-steganography-foundation | nsf-neural-human-move | other (not a hiding channel; skill-conditioned model of human move choice) | — | training | — | m-neural-human-move | no | own | — | — |
| `mcilroyyoung_2020:approach-blunder-predictor` | blunder prediction, a residual CNN that labels a move a blunder when it costs 10 points of win probability | non-steganography-foundation | nsf-neural-human-move | other (not a hiding channel; mistake predictor) | — | training | — | m-neural-human-move | no | own | — | — |
| `mcilroyyoung_2020:approach-maia` | Maia, AlphaZero's architecture retrained on human games to predict the next human move, with no tree search | non-steganography-foundation | nsf-neural-human-move | other (not a hiding channel; model of human move choice, a cover distribution or warden model for move-choice channels) | — | training | — | m-neural-human-move | no | own | — | — |
| `nickel_2017:approach-poincare-embeddings` | embed symbolic data in an n-dimensional Poincaré ball to capture hierarchy and similarity at once | non-steganography-foundation | nsf-hyperbolic-embeddings | — | — | training | — | m-hyperbolic-embeddings | no | own | — | — |
| `regan_2011:approach-intrinsic-rating-model` | an intrinsic-rating model of human move choice: engine evaluations of all reasonable moves give each move a probability set by sensitivity s and competence c, fitted to Elo by regression and usable to detect engine assistance | non-steganography-foundation | nsf-intrinsic-rating | other (not a hiding channel; model of human move choice) | — | — | — | m-intrinsic-rating | no | own | — | — |
| `regan_2012:approach-intrinsic-performance-ratings` | a refined Regan–Haworth model applied to whole populations: Intrinsic Performance Ratings from Multi-PV analysis, with their distribution used to test rating stability and drift between rating systems | non-steganography-foundation | nsf-intrinsic-rating | other (not a hiding channel; population-level move-quality distributions) | — | — | — | m-intrinsic-rating | no | own | — | — |
| `sala_2018:approach-combinatorial-construction` | a combinatorial construction that embeds a tree in hyperbolic space with arbitrarily low distortion, without optimisation | non-steganography-foundation | nsf-hyperbolic-embeddings | — | — | — | — | m-hyperbolic-embeddings | no | own | — | — |
| `sala_2018:approach-h-mds` | hyperbolic multidimensional scaling (h-MDS): exact recovery of points from distances via a non-standard mean | non-steganography-foundation | nsf-hyperbolic-embeddings | — | — | — | — | m-hyperbolic-embeddings | no | own | — | — |
| `sala_2018:approach-pytorch-sgd-pga` | an SGD algorithm in PyTorch, initialised by h-MDS, recovers the data's submanifold under noise and handles incomplete distances | non-steganography-foundation | nsf-hyperbolic-embeddings | — | — | training | — | m-hyperbolic-embeddings | no | own | — | — |
| `sarkar_2011:approach-delaunay-tree-embedding` | Method — embed any tree in the hyperbolic plane as the Delaunay graph of its vertices | non-steganography-foundation | nsf-hyperbolic-embeddings | other (not a channel: geometric embedding) | — | — | — | m-hyperbolic-embeddings | no | own | — | — |
| `shimizu_2020:approach-hnn-plus-plus` | a parameter-reduced MLR, FC, convolutional and attention layers, all in the Poincaré ball under one interpretation | non-steganography-foundation | nsf-hyperbolic-networks | — | — | training | — | m-hyperbolic-networks | no | own | — | — |
| `shimizu_2020:approach-poincare-beta-concatenation` | Poincaré β-concatenation: map inputs to the tangent space, rescale by beta-function ratios, concatenate, map back | non-steganography-foundation | nsf-hyperbolic-networks | — | — | — | — | m-hyperbolic-networks | no | own | — | — |
| `tomasev_2020:approach-insilico-variant-assessment` | in-silico assessment of chess variants, by training AlphaZero to near-optimal play under each rule set | non-steganography-foundation | nsf-engine-and-opening-analysis | other (not a hiding channel; game-balance assessment) | — | training | — | m-opening-and-engine-analysis | no | own | — | — |
| `tomasev_2020:approach-prior-entropy-diversity` | opening diversity measured as the entropy of the first 20 plies of the AlphaZero prior | non-steganography-foundation | nsf-engine-and-opening-analysis | other (not a hiding channel; carrier-capacity measure for move choice) | — | weights | classical chess 28.58 nats over the first 20 plies of the prior against 64.96 nats for uniform legal-move choice | m-opening-and-engine-analysis | no | own | — | — |
| `xia_2026:approach-lapha` | LaPha, AlphaZero-like LLM agents trained in a root-centred Poincaré latent space | non-steganography-foundation | nsf-hyperbolic-networks | — | — | weights, training | — | m-hyperbolic-networks | no | own | — | — |
| `yang_2024:approach-hyplora` | HypLoRA, low-rank adaptation performed directly on the hyperbolic manifold | non-steganography-foundation | nsf-hyperbolic-networks | — | — | weights, training | — | m-hyperbolic-networks | no | own | — | — |
| `yang_2026:approach-hyperbolicity-atlas` | a Gromov-hyperbolicity atlas of prompt-token hidden states across scale, depth, family and domain | non-steganography-foundation | nsf-hyperbolic-embeddings | — | — | weights | — | m-hyperbolic-embeddings | no | own | — | — |
