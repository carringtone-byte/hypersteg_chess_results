---
generated: 2026-11-08T20:09:54+03:00
---

# Approach map — mechanism class detection

Built by `tools/build_approach_map.py` from `C:\Users\user\Documents\GitHub\hypersteg_chess\hypersteg_novelty_kit_20261108\literature\verified_claims`, the features table `C:\Users\user\Documents\GitHub\hypersteg_chess\hypersteg_novelty_kit_20261108\maps\approach_features.tsv` and the mechanism taxonomy `C:\Users\user\Documents\GitHub\hypersteg_chess\hypersteg_novelty_kit_20261108\maps\mechanism_taxonomy.tsv`. Mechanism overview: [approach_map_mechanisms.md](approach_map_mechanisms.md). Each approach leaf names its paper family.

- mechanisms: 14
- approaches: 13
- families: 1 (steganalysis)

```mermaid
flowchart TD
  subgraph cls_detection_g["detection"]
    cls_detection("detection")
    mech_m_activation_probe{{"Activation probes"}}
    mech_m_active_warden{{"Active-warden defences"}}
    mech_m_adversary_decoding{{"Adversary decoding attempts"}}
    mech_m_concept_lens{{"Concept-lens readout"}}
    mech_m_detection{{"Detectors, monitors and defences"}}
    mech_m_feature_steganalysis{{"Statistical feature steganalysis"}}
    mech_m_game_record_inference{{"Game-record inference"}}
    mech_m_game_statistics{{"Game-statistics attacks"}}
    mech_m_likelihood_ratio_forensics{{"Hypothesis-comparison forensics"}}
    mech_m_llm_classifier{{"LLM classifiers"}}
    mech_m_non_text_statistical_detection{{"Entropy of non-text messages"}}
    mech_m_prompted_llm_monitor{{"Prompted LLM monitor"}}
    mech_m_text_feature_steganalysis{{"Text feature steganalysis"}}
    mech_m_utility_gap{{"Decision-theoretic utility gap"}}
    n_anwar_2026_approach_steganographic_gap["a decision-theoretic view of steganography, detected and qu…<br/>anwar_2026<br/>family: steganalysis"]
    n_bai_2024b_approach_generative_llm_steganalysis["generation-based linguistic steganalysis: an LLM fine-tuned…<br/>bai_2024b<br/>family: steganalysis"]
    n_boonstra_2024_approach_bayesian_hidden_code_forensics["a Bayesian forensic framework for alleged hidden codes in s…<br/>boonstra_2024<br/>family: steganalysis"]
    n_greenblatt_2023_approach_untrusted_monitoring_signal_jamming["untrusted monitoring guarded by signal jamming<br/>greenblatt_2023<br/>family: steganalysis"]
    n_hernandezcastro_2006_approach_game_steganalysis["statistical attacks on game length, playing level and resul…<br/>hernandezcastro_2006<br/>family: steganalysis"]
    n_molinari_2026_approach_j_pact["J-PACT, unsupervised pairwise collusion detection from shar…<br/>molinari_2026<br/>family: steganalysis"]
    n_molinari_2026_approach_j_space_steering["causal steering of steganographic decoding by swapping J-le…<br/>molinari_2026<br/>family: steganalysis"]
    n_roger_2023_approach_paraphrase_defence["a conservative evaluation of paraphrasing as a defence agai…<br/>roger_2023<br/>family: steganalysis"]
    n_rose_2026_approach_helios["HELIOS, group-level collusion detection from per-agent acti…<br/>rose_2026<br/>family: steganalysis"]
    n_tang_2024_approach_lsgc["LSGC, linguistic steganalysis by a LoRA-fine-tuned LLM, in …<br/>tang_2024<br/>family: steganalysis"]
    n_westphal_2026_approach_probe_detection_recontextualisation["mechanistic probe detection, extended from ridge to a held-…<br/>westphal_2026<br/>family: steganalysis"]
    n_xiang_2018_approach_wes["WES, word-embedding steganalysis: context fitness of each s…<br/>xiang_2018<br/>family: steganalysis"]
    n_yan_2010_approach_inference_engine_collusion_detector["an inference engine over complete game records that flags b…<br/>yan_2010<br/>family: steganalysis"]
  end
  mech_m_detection --- mech_m_activation_probe
  mech_m_detection --- mech_m_active_warden
  mech_m_detection --- mech_m_adversary_decoding
  mech_m_detection --- mech_m_concept_lens
  cls_detection --- mech_m_detection
  mech_m_detection --- mech_m_feature_steganalysis
  mech_m_detection --- mech_m_game_record_inference
  mech_m_feature_steganalysis --- mech_m_game_statistics
  mech_m_detection --- mech_m_likelihood_ratio_forensics
  mech_m_detection --- mech_m_llm_classifier
  mech_m_feature_steganalysis --- mech_m_non_text_statistical_detection
  mech_m_detection --- mech_m_prompted_llm_monitor
  mech_m_feature_steganalysis --- mech_m_text_feature_steganalysis
  mech_m_detection --- mech_m_utility_gap
  mech_m_utility_gap --- n_anwar_2026_approach_steganographic_gap
  mech_m_llm_classifier --- n_bai_2024b_approach_generative_llm_steganalysis
  mech_m_likelihood_ratio_forensics --- n_boonstra_2024_approach_bayesian_hidden_code_forensics
  mech_m_prompted_llm_monitor --- n_greenblatt_2023_approach_untrusted_monitoring_signal_jamming
  mech_m_active_warden --- n_greenblatt_2023_approach_untrusted_monitoring_signal_jamming
  mech_m_game_statistics --- n_hernandezcastro_2006_approach_game_steganalysis
  mech_m_active_warden --- n_hernandezcastro_2006_approach_game_steganalysis
  mech_m_concept_lens --- n_molinari_2026_approach_j_pact
  mech_m_concept_lens --- n_molinari_2026_approach_j_space_steering
  mech_m_active_warden --- n_roger_2023_approach_paraphrase_defence
  mech_m_activation_probe --- n_rose_2026_approach_helios
  mech_m_llm_classifier --- n_tang_2024_approach_lsgc
  mech_m_activation_probe --- n_westphal_2026_approach_probe_detection_recontextualisation
  mech_m_text_feature_steganalysis --- n_xiang_2018_approach_wes
  mech_m_game_record_inference --- n_yan_2010_approach_inference_engine_collusion_detector
  linkStyle 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28 stroke:#9e9e9e,stroke-width:1px
  classDef nonlanding fill:#eeeeee,stroke:#bdbdbd,stroke-dasharray:2 2,color:#9e9e9e
  class mech_m_activation_probe,mech_m_active_warden,mech_m_adversary_decoding,mech_m_concept_lens,mech_m_detection,mech_m_feature_steganalysis,mech_m_game_record_inference,mech_m_game_statistics,mech_m_likelihood_ratio_forensics,mech_m_llm_classifier,mech_m_non_text_statistical_detection,mech_m_prompted_llm_monitor,mech_m_text_feature_steganalysis,mech_m_utility_gap nonlanding
```

Muted, dashed nodes are marked not a landing node: they group the tree, and a novelty audit does not place a scheme at one. A child of such a node is one too unless its row says `landing: yes`.

## Mechanisms

| mechanism | parent | class | name | definition | grounded by | landing | approaches |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `m-activation-probe` | m-detection | detection | Activation probes (not a landing node) | Probes on hidden states reconstruct the secret or read deception, calibrated to a false-positive rate. | `westphal_2026:probe-detector-all-layer-rule` | no | 2 |
| `m-active-warden` | m-detection | detection | Active-warden defences (not a landing node) | The overseer rewrites the message, for example by paraphrasing it while keeping its meaning, to destroy any payload instead of only detecting it. | `roger_2023:approach-paraphrase-defence` | no | 3 |
| `m-adversary-decoding` | m-detection | detection | Adversary decoding attempts (not a landing node) | Near-copies of the decoder, trained with minor variations, try to recover the message rather than just flag it. | `agarwal_2023:hypersteg-near-copy-decoders-fail` | no | 0 |
| `m-concept-lens` | m-detection | detection | Concept-lens readout (not a landing node) | Concepts read through a Jacobian lens are compared across agents to find colluding pairs. | `molinari_2026:approach-j-pact` | no | 2 |
| `m-detection` | — | detection | Detectors, monitors and defences (not a landing node) | Methods that detect, measure, remove or read hidden communication. | `hernandezcastro_2006:approach-game-steganalysis` | no | 13 |
| `m-feature-steganalysis` | m-detection | detection | Statistical feature steganalysis (not a landing node) | Statistical attacks detect significant deviations from a model of the cover caused by inserting hidden data. | `hernandezcastro_2006:approach-game-steganalysis` | no | 2 |
| `m-game-record-inference` | m-detection | detection | Game-record inference (not a landing node) | An inference engine analyses the bidding and play in complete game records to detect collusive play. | `yan_2010:approach-inference-engine-collusion-detector` | no | 1 |
| `m-game-statistics` | m-feature-steganalysis | detection | Game-statistics attacks (not a landing node) | Game length, playing level and result are tested for deviations caused by embedding. | `hernandezcastro_2006:approach-game-steganalysis` | no | 1 |
| `m-likelihood-ratio-forensics` | m-detection | detection | Hypothesis-comparison forensics (not a landing node) | The hypothesis that a specified method was used to transmit information is weighed against the hypothesis that it was not. | `boonstra_2024:likelihood-ratio-detector` | no | 1 |
| `m-llm-classifier` | m-detection | detection | LLM classifiers (not a landing node) | A fine-tuned LLM judges whether a text carries hidden data. | `tang_2024:approach-lsgc` | no | 2 |
| `m-non-text-statistical-detection` | m-feature-steganalysis | detection | Entropy of non-text messages (not a landing node) | Covert messages are detected by their lower entropy than random baselines. | `buscemi_2026:entropy-ordering-detection` | no | 0 |
| `m-prompted-llm-monitor` | m-detection | detection | Prompted LLM monitor (not a landing node) | A model given the cover task and answer, but not the secret, is told to rate suspicion, and a threshold set at a fixed false-positive rate decides. | `zolkowski_2025:monitor-threshold-fpr` | no | 1 |
| `m-text-feature-steganalysis` | m-feature-steganalysis | detection | Text feature steganalysis (not a landing node) | Semantic features of word choice, such as synonym context fitness, feed a classifier. | `xiang_2018:approach-wes` | no | 1 |
| `m-utility-gap` | m-detection | detection | Decision-theoretic utility gap (not a landing node) | Steganography is measured by comparing the downstream utility of a message to parties who can and cannot decode it. | `anwar_2026:approach-steganographic-gap` | no | 1 |

## Approaches

| address | name | family | technique | channel | key | access | capacity | mechanism | landable | mechanism_evidence | carrier | acquisition |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `anwar_2026:approach-steganographic-gap` | a decision-theoretic view of steganography, detected and quantified by the steganographic gap over generalised V-information | steganalysis | sa-utility-gap | other (detection from downstream actions) | — | prompt | — | m-utility-gap | no | own | — | — |
| `bai_2024b:approach-generative-llm-steganalysis` | generation-based linguistic steganalysis: an LLM fine-tuned with LoRA writes its verdict on a text as readable output, with no added classifier module | steganalysis | sa-llm-classifiers | other (detector of distributional-sampling stegos) | — | training | — | m-llm-classifier | no | own | — | — |
| `boonstra_2024:approach-bayesian-hidden-code-forensics` | a Bayesian forensic framework for alleged hidden codes in sport: weigh the likelihood of the observed events under a named code against their likelihood under no code | steganalysis | sa-likelihood-ratio-forensics | other (detector of pre-agreed side-channel codes) | none | — | — | m-likelihood-ratio-forensics | no | sibling:likelihood-ratio-detector | — | — |
| `greenblatt_2023:approach-untrusted-monitoring-signal-jamming` | untrusted monitoring guarded by signal jamming | steganalysis | sa-active-warden; sa-prompted-llm-monitors | other (active-warden redaction and paraphrase) | — | prompt | — | m-prompted-llm-monitor; m-active-warden | no | own;own | — | — |
| `hernandezcastro_2006:approach-game-steganalysis` | statistical attacks on game length, playing level and result, and stripping variations and comments; countered by encryption, raised komi and both sides embedding | steganalysis | sa-game-statistics | move choice | none | — | — | m-game-statistics; m-active-warden | no | own;own | — | — |
| `molinari_2026:approach-j-pact` | J-PACT, unsupervised pairwise collusion detection from shared J-space concepts | steganalysis | sa-concept-lens | other (relational activation readout) | — | weights | — | m-concept-lens | no | own | — | — |
| `molinari_2026:approach-j-space-steering` | causal steering of steganographic decoding by swapping J-lens concept coordinates | steganalysis | sa-concept-lens | other (activation intervention) | — | weights | — | m-concept-lens | no | own | — | — |
| `roger_2023:approach-paraphrase-defence` | a conservative evaluation of paraphrasing as a defence against steganography | steganalysis | sa-active-warden | other (active-warden paraphrase defence) | — | prompt | below about 2 bits per answer (3 bits per KB) survive paraphrasing | m-active-warden | no | own | — | — |
| `rose_2026:approach-helios` | HELIOS, group-level collusion detection from per-agent activation probes | steganalysis | sa-activation-probes | other (activation probing) | — | weights | — | m-activation-probe | no | own | — | — |
| `tang_2024:approach-lsgc` | LSGC, linguistic steganalysis by a LoRA-fine-tuned LLM, in a generation mode that explains its verdict and a classification mode that reads features in one pass | steganalysis | sa-llm-classifiers | other (detector of generative text stego) | — | training | — | m-llm-classifier | no | own | — | — |
| `westphal_2026:approach-probe-detection-recontextualisation` | mechanistic probe detection, extended from ridge to a held-out two-layer MLP probe, and restored against evasive trojans by a recontextualisation dataset that removes the slack the secret is routed through | steganalysis | sa-activation-probes | other (detector) | — | weights | — | m-activation-probe | no | own | — | — |
| `xiang_2018:approach-wes` | WES, word-embedding steganalysis: context fitness of each synonym, three features from it, and an SVM | steganalysis | sa-text-features | lexical | — | training | — | m-text-feature-steganalysis | no | own | — | — |
| `yan_2010:approach-inference-engine-collusion-detector` | an inference engine over complete game records that flags bids and plays too good for the information a player legitimately held | steganalysis | sa-game-record-inference | move choice | — | — | — | m-game-record-inference | no | own | — | — |
