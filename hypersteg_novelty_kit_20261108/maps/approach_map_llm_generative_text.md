---
generated: 2026-11-08T20:09:54+03:00
---

# Approach map — llm-generative-text

Built by `tools/build_approach_map.py` from `C:\Users\user\Documents\GitHub\hypersteg_chess\hypersteg_novelty_kit_20261108\literature\verified_claims`, the features table `C:\Users\user\Documents\GitHub\hypersteg_chess\hypersteg_novelty_kit_20261108\maps\approach_features.tsv` and the technique taxonomy `C:\Users\user\Documents\GitHub\hypersteg_chess\hypersteg_novelty_kit_20261108\maps\technique_taxonomy.tsv`. View: `both`. Overview: [approach_map.md](approach_map.md).

- approaches: 38
- techniques: 32

```mermaid
flowchart LR
  subgraph fam_llm_generative_text_g["llm-generative-text"]
    fam_llm_generative_text("llm-generative-text")
    tech_lgt_bins{{"Fixed bins"}}
    tech_lgt_byte_encodings{{"Byte encodings"}}
    tech_lgt_count_state_codes{{"Count and state-tracking codes"}}
    tech_lgt_coupling{{"Coupling-based codes"}}
    tech_lgt_coupling_public_draft{{"Maximal coupling through a public draft model"}}
    tech_lgt_distribution_copies{{"Distribution copies"}}
    tech_lgt_entity_keyword_mapping{{"Entity and keyword mapping"}}
    tech_lgt_enumerated_openers{{"Enumerated openers"}}
    tech_lgt_feedback_coding{{"Feedback (posterior-matching) coding"}}
    tech_lgt_finetuned_encoders{{"Encoders trained into the weights"}}
    tech_lgt_grouping{{"Probability grouping"}}
    tech_lgt_huffman{{"Per-step Huffman codes"}}
    tech_lgt_huffman_patient{{"Thresholded (patient) Huffman"}}
    tech_lgt_initial_class_codes{{"Initial-class codes"}}
    tech_lgt_interval_adaptive_truncation{{"Interval coding with per-step truncation"}}
    tech_lgt_interval_coding{{"Interval (arithmetic) coding"}}
    tech_lgt_interval_keyed_randomness{{"Keyed sampling-randomness embedding"}}
    tech_lgt_letter_position_codes{{"Letter-position codes (acrostics)"}}
    tech_lgt_literal_payload_names{{"Literal payload as a name"}}
    tech_lgt_overt_encodings{{"Overt encodings and ciphers"}}
    tech_lgt_prompted_rule_codes{{"Prompted pre-agreed rule codes"}}
    tech_lgt_public_key_sampling{{"Keyless key exchange in samples"}}
    tech_lgt_reasoning_strategy_choice{{"Reasoning-strategy choice"}}
    tech_lgt_sampling_codes{{"Distribution-preserving sampling codes"}}
    tech_lgt_semantic_choice{{"Black-box semantic-choice schemes"}}
    tech_lgt_substitution_ciphers{{"Substitution ciphers"}}
    tech_lgt_surface_formatting{{"Surface-formatting codes"}}
    tech_lgt_task_choice_codes{{"Free task-choice codes"}}
    tech_lgt_vocabulary_codes{{"Bin and Huffman codes"}}
    tech_lgt_watermark_codes{{"Watermark-derived multi-bit codes"}}
    tech_lgt_watermark_pseudorandom{{"Pseudorandom undetectable watermark codes"}}
    tech_lgt_watermark_token_partition{{"Token-partition (red-green) watermark codes"}}
    n_bai_2024_approach_semantic_steganography["semantic steganography: secret bits select a class in a sem…<br/>bai_2024"]
    n_dai_2019_approach_patient_huffman["patient-Huffman, per-step Huffman coding of the LM distribu…<br/>dai_2019"]
    n_dai_2019_surveyed_bins["Bins (Fang et al. 2017), a shared random partition of the v…<br/>dai_2019"]
    n_dai_2019_surveyed_vlc_huffman["VLC (Yang et al. 2018), a Huffman code over the vocabulary …<br/>dai_2019"]
    n_ding_2023_approach_discop["Discop, sampling from one of several rotated #quot;distribution …<br/>ding_2023"]
    n_guo_2026_approach_bam_feedback_coding["BAM (Burnashev Adaptive Posterior Matching): black-box LLM …<br/>guo_2026"]
    n_kaptchuk_2021_approach_meteor["Meteor: a symmetric-key, stateful, provably secure scheme t…<br/>kaptchuk_2021"]
    n_motwani_2024_surveyed_first_letter_acrostic["instructed first-letter (acrostic) covertext scheme<br/>motwani_2024"]
    n_motwani_2024_surveyed_standard_ciphers["standard ciphers (Base64, Caesar) as an encoding capability<br/>motwani_2024"]
    n_pang_2026_approach_codetta_key_exchange["Codetta's keyless steganographic key exchange, MLWE ciphert…<br/>pang_2026"]
    n_pang_2026_approach_codetta_keyed["Codetta's keyed protocol, high-capacity asymmetric steganog…<br/>pang_2026"]
    n_roger_2023_surveyed_acronyms["prompted acronym scheme<br/>roger_2023"]
    n_roger_2023_surveyed_age_instructions["prompted age-instruction scheme<br/>roger_2023"]
    n_roger_2023_surveyed_balanced_marking["balanced-marking watermark used for steganography<br/>roger_2023"]
    n_roger_2023_surveyed_cycle_shifting_watermark["cycle-shifting watermark used for steganography<br/>roger_2023"]
    n_roger_2023_surveyed_introduction_variations["prompted introduction-variation scheme<br/>roger_2023"]
    n_roger_2023_surveyed_scratchpad_scheme["scratchpad scheme in which the model devises its own encodi…<br/>roger_2023"]
    n_schroederdewitt_2022_approach_imec["minimum entropy coupling steganography (iMEC): encode by co…<br/>schroederdewitt_2022"]
    n_schulz_2026_approach_formatting_and_knapsack_encodings["six surface-formatting encodings and the knapsack cover, ap…<br/>schulz_2026"]
    n_shen_2020_approach_saac["SAAC, arithmetic coding over a pretrained LM in which the t…<br/>shen_2020"]
    n_tailor_2026_surveyed_alternating_sentence_initials["alternating sentence initials (prescribed rule)<br/>tailor_2026"]
    n_tailor_2026_surveyed_base64["Base64 (prescribed rule)<br/>tailor_2026"]
    n_tailor_2026_surveyed_eight_bit_binary["eight-bit binary (prescribed rule)<br/>tailor_2026"]
    n_tailor_2026_surveyed_fixed_letter_substitution["fixed-letter substitution (prescribed rule)<br/>tailor_2026"]
    n_tailor_2026_surveyed_hexadecimal["hexadecimal (prescribed rule)<br/>tailor_2026"]
    n_tailor_2026_surveyed_sentence_initials["sentence initials (prescribed rule)<br/>tailor_2026"]
    n_tailor_2026_surveyed_word_length_parity_token_initials["word-length parity and token initials (not prescribed; foun…<br/>tailor_2026"]
    n_westphal_2026_approach_evasive_steganographic_trojan["the evasive steganographic trojan: an LLM fine-tuned to enc…<br/>westphal_2026"]
    n_wu_2024_approach_llm_stega["LLM-Stega, black-box steganography through an LLM's user in…<br/>wu_2024"]
    n_zamir_2024_approach_undetectable_llm_stego["undetectable LLM steganography: the CGZ undetectable waterm…<br/>zamir_2024"]
    n_zhang_2021_approach_adg["ADG, equal-probability grouping of the vocabulary at each s…<br/>zhang_2021"]
    n_zhou_2026_approach_conceptual_steganography["conceptual steganography: each chain-of-thought step carrie…<br/>zhou_2026"]
    n_ziegler_2019_approach_arithmetic_coding["arithmetic-coding steganography over a large neural languag…<br/>ziegler_2019"]
    n_zolkowski_2025_surveyed_byte_encodings["byte-encoding schemes (Base64, UTF-8 binary, Hex and their …<br/>zolkowski_2025"]
    n_zolkowski_2025_surveyed_letter_position_acrostics["letter-position acrostic schemes given to encoder and decod…<br/>zolkowski_2025"]
    n_zolkowski_2025_surveyed_model_generated_subtlety["model-generated encoding schemes at three degrees of subtle…<br/>zolkowski_2025"]
    n_zolkowski_2025_surveyed_rotation_substitution["rotation and substitution ciphers<br/>zolkowski_2025"]
    n_zolkowski_2025_surveyed_state_tracking_encodings["state-tracking encodings by first letter, sentence length, …<br/>zolkowski_2025"]
  end
  subgraph other_families["other families"]
    n_bai_2024b_approach_generative_llm_steganalysis["generation-based linguistic steganalysis: an LLM fine-tuned…<br/>bai_2024b<br/>family: steganalysis"]
    n_cachin_1998_approach_information_theoretic_model["an information-theoretic model of steganography against a p…<br/>cachin_1998<br/>family: foundations-theory"]
    n_cachin_2004_approach_information_theoretic_model["an information-theoretic model of steganography against a p…<br/>cachin_2004<br/>family: foundations-theory"]
    n_hopper_2002_approach_stateful_rejection_sampling["Construction 1, stateful rejection sampling: for each encod…<br/>hopper_2002<br/>family: foundations-theory"]
    paper_cachin_1998(["cachin_1998<br/>(paper)<br/>family: foundations-theory"])
    paper_motwani_2024(["motwani_2024<br/>(paper)<br/>family: llm-capability-eval"])
    n_rippin_2026_approach_agentic_covert_channel_construction["an agentic covert-channel construction benchmark, seeded wi…<br/>rippin_2026<br/>family: llm-capability-eval"]
    n_roger_2023_approach_paraphrase_defence["a conservative evaluation of paraphrasing as a defence agai…<br/>roger_2023<br/>family: steganalysis"]
  end
  tech_lgt_vocabulary_codes --- tech_lgt_bins
  tech_lgt_overt_encodings --- tech_lgt_byte_encodings
  tech_lgt_prompted_rule_codes --- tech_lgt_count_state_codes
  tech_lgt_sampling_codes --- tech_lgt_coupling
  tech_lgt_coupling --- tech_lgt_coupling_public_draft
  tech_lgt_sampling_codes --- tech_lgt_distribution_copies
  tech_lgt_semantic_choice --- tech_lgt_entity_keyword_mapping
  tech_lgt_prompted_rule_codes --- tech_lgt_enumerated_openers
  tech_lgt_sampling_codes --- tech_lgt_feedback_coding
  fam_llm_generative_text --- tech_lgt_finetuned_encoders
  tech_lgt_sampling_codes --- tech_lgt_grouping
  tech_lgt_vocabulary_codes --- tech_lgt_huffman
  tech_lgt_huffman --- tech_lgt_huffman_patient
  tech_lgt_prompted_rule_codes --- tech_lgt_initial_class_codes
  tech_lgt_interval_coding --- tech_lgt_interval_adaptive_truncation
  tech_lgt_sampling_codes --- tech_lgt_interval_coding
  tech_lgt_interval_coding --- tech_lgt_interval_keyed_randomness
  tech_lgt_prompted_rule_codes --- tech_lgt_letter_position_codes
  tech_lgt_prompted_rule_codes --- tech_lgt_literal_payload_names
  tech_lgt_prompted_rule_codes --- tech_lgt_overt_encodings
  fam_llm_generative_text --- tech_lgt_prompted_rule_codes
  tech_lgt_sampling_codes --- tech_lgt_public_key_sampling
  tech_lgt_semantic_choice --- tech_lgt_reasoning_strategy_choice
  fam_llm_generative_text --- tech_lgt_sampling_codes
  fam_llm_generative_text --- tech_lgt_semantic_choice
  tech_lgt_overt_encodings --- tech_lgt_substitution_ciphers
  tech_lgt_prompted_rule_codes --- tech_lgt_surface_formatting
  fam_llm_generative_text --- tech_lgt_task_choice_codes
  fam_llm_generative_text --- tech_lgt_vocabulary_codes
  fam_llm_generative_text --- tech_lgt_watermark_codes
  tech_lgt_watermark_codes --- tech_lgt_watermark_pseudorandom
  tech_lgt_watermark_codes --- tech_lgt_watermark_token_partition
  tech_lgt_entity_keyword_mapping --- n_bai_2024_approach_semantic_steganography
  tech_lgt_huffman_patient --- n_dai_2019_approach_patient_huffman
  tech_lgt_bins --- n_dai_2019_surveyed_bins
  tech_lgt_huffman --- n_dai_2019_surveyed_vlc_huffman
  tech_lgt_distribution_copies --- n_ding_2023_approach_discop
  tech_lgt_feedback_coding --- n_guo_2026_approach_bam_feedback_coding
  tech_lgt_interval_keyed_randomness --- n_kaptchuk_2021_approach_meteor
  tech_lgt_letter_position_codes --- n_motwani_2024_surveyed_first_letter_acrostic
  tech_lgt_byte_encodings --- n_motwani_2024_surveyed_standard_ciphers
  tech_lgt_substitution_ciphers --- n_motwani_2024_surveyed_standard_ciphers
  tech_lgt_public_key_sampling --- n_pang_2026_approach_codetta_key_exchange
  tech_lgt_coupling_public_draft --- n_pang_2026_approach_codetta_keyed
  tech_lgt_literal_payload_names --- n_roger_2023_surveyed_acronyms
  tech_lgt_enumerated_openers --- n_roger_2023_surveyed_age_instructions
  tech_lgt_watermark_token_partition --- n_roger_2023_surveyed_balanced_marking
  tech_lgt_watermark_token_partition --- n_roger_2023_surveyed_cycle_shifting_watermark
  tech_lgt_enumerated_openers --- n_roger_2023_surveyed_introduction_variations
  fam_llm_generative_text --- n_roger_2023_surveyed_scratchpad_scheme
  tech_lgt_coupling --- n_schroederdewitt_2022_approach_imec
  tech_lgt_surface_formatting --- n_schulz_2026_approach_formatting_and_knapsack_encodings
  tech_lgt_task_choice_codes --- n_schulz_2026_approach_formatting_and_knapsack_encodings
  tech_lgt_interval_adaptive_truncation --- n_shen_2020_approach_saac
  tech_lgt_letter_position_codes --- n_tailor_2026_surveyed_alternating_sentence_initials
  tech_lgt_byte_encodings --- n_tailor_2026_surveyed_base64
  tech_lgt_byte_encodings --- n_tailor_2026_surveyed_eight_bit_binary
  tech_lgt_substitution_ciphers --- n_tailor_2026_surveyed_fixed_letter_substitution
  tech_lgt_byte_encodings --- n_tailor_2026_surveyed_hexadecimal
  tech_lgt_letter_position_codes --- n_tailor_2026_surveyed_sentence_initials
  tech_lgt_count_state_codes --- n_tailor_2026_surveyed_word_length_parity_token_initials
  tech_lgt_initial_class_codes --- n_tailor_2026_surveyed_word_length_parity_token_initials
  tech_lgt_finetuned_encoders --- n_westphal_2026_approach_evasive_steganographic_trojan
  tech_lgt_entity_keyword_mapping --- n_wu_2024_approach_llm_stega
  tech_lgt_watermark_pseudorandom --- n_zamir_2024_approach_undetectable_llm_stego
  tech_lgt_grouping --- n_zhang_2021_approach_adg
  tech_lgt_reasoning_strategy_choice --- n_zhou_2026_approach_conceptual_steganography
  tech_lgt_interval_coding --- n_ziegler_2019_approach_arithmetic_coding
  tech_lgt_byte_encodings --- n_zolkowski_2025_surveyed_byte_encodings
  tech_lgt_letter_position_codes --- n_zolkowski_2025_surveyed_letter_position_acrostics
  fam_llm_generative_text --- n_zolkowski_2025_surveyed_model_generated_subtlety
  tech_lgt_substitution_ciphers --- n_zolkowski_2025_surveyed_rotation_substitution
  tech_lgt_count_state_codes --- n_zolkowski_2025_surveyed_state_tracking_encodings
  tech_lgt_letter_position_codes --- n_zolkowski_2025_surveyed_state_tracking_encodings
  tech_lgt_surface_formatting --- n_zolkowski_2025_surveyed_state_tracking_encodings
  n_bai_2024_approach_semantic_steganography -.->|Qualifies| n_kaptchuk_2021_approach_meteor
  n_bai_2024_approach_semantic_steganography -.->|Qualifies| n_schroederdewitt_2022_approach_imec
  n_bai_2024_approach_semantic_steganography -.->|Qualifies| n_ding_2023_approach_discop
  n_bai_2024b_approach_generative_llm_steganalysis -.->|Qualifies| n_zhang_2021_approach_adg
  n_bai_2024b_approach_generative_llm_steganalysis -.->|Qualifies| n_ziegler_2019_approach_arithmetic_coding
  n_bai_2024b_approach_generative_llm_steganalysis -.->|Qualifies| n_ding_2023_approach_discop
  n_ding_2023_approach_discop -.->|Rebuts| n_zhang_2021_approach_adg
  n_ding_2023_approach_discop -.->|Qualifies| n_kaptchuk_2021_approach_meteor
  n_ding_2023_approach_discop ==>|Depends-on| paper_cachin_1998
  n_guo_2026_approach_bam_feedback_coding -->|Refines| n_zamir_2024_approach_undetectable_llm_stego
  n_guo_2026_approach_bam_feedback_coding -.->|Qualifies| n_schroederdewitt_2022_approach_imec
  n_guo_2026_approach_bam_feedback_coding -.->|Qualifies| n_kaptchuk_2021_approach_meteor
  n_guo_2026_approach_bam_feedback_coding -.->|Qualifies| n_ziegler_2019_approach_arithmetic_coding
  n_guo_2026_approach_bam_feedback_coding ==>|Depends-on| n_cachin_2004_approach_information_theoretic_model
  n_kaptchuk_2021_approach_meteor -->|Refines| n_hopper_2002_approach_stateful_rejection_sampling
  n_kaptchuk_2021_approach_meteor --x|Supersedes| n_ziegler_2019_approach_arithmetic_coding
  n_kaptchuk_2021_approach_meteor --x|Supersedes| n_dai_2019_approach_patient_huffman
  n_kaptchuk_2021_approach_meteor ==>|Depends-on| n_ziegler_2019_approach_arithmetic_coding
  paper_motwani_2024 ==>|Depends-on| n_schroederdewitt_2022_approach_imec
  n_rippin_2026_approach_agentic_covert_channel_construction ==>|Depends-on| n_zamir_2024_approach_undetectable_llm_stego
  n_schroederdewitt_2022_approach_imec ==>|Depends-on| n_cachin_1998_approach_information_theoretic_model
  n_schroederdewitt_2022_approach_imec --x|Supersedes| n_ziegler_2019_approach_arithmetic_coding
  n_schroederdewitt_2022_approach_imec --x|Supersedes| n_kaptchuk_2021_approach_meteor
  n_schroederdewitt_2022_approach_imec --x|Supersedes| n_dai_2019_approach_patient_huffman
  n_schroederdewitt_2022_approach_imec --x|Supersedes| n_zhang_2021_approach_adg
  n_shen_2020_approach_saac -->|Refines| n_ziegler_2019_approach_arithmetic_coding
  n_shen_2020_approach_saac ==>|Depends-on| n_dai_2019_approach_patient_huffman
  n_wu_2024_approach_llm_stega -.->|Qualifies| n_ziegler_2019_approach_arithmetic_coding
  n_wu_2024_approach_llm_stega -.->|Qualifies| n_dai_2019_approach_patient_huffman
  n_zhang_2021_approach_adg ==>|Depends-on| paper_cachin_1998
  n_zhou_2026_approach_conceptual_steganography -.->|Qualifies| n_roger_2023_approach_paraphrase_defence
  linkStyle 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74 stroke:#9e9e9e,stroke-width:1px
  linkStyle 75,76,77,78,79,80,82,85,86,87,102,103,105 stroke:#ef6c00,stroke-width:2.5px,color:#ef6c00
  linkStyle 81 stroke:#c62828,stroke-width:2.5px,color:#c62828
  linkStyle 83,88,92,93,94,95,101,104 stroke:#6a1b9a,stroke-width:2.5px,color:#6a1b9a
  linkStyle 84,89,100 stroke:#1565c0,stroke-width:2.5px,color:#1565c0
  linkStyle 90,91,96,97,98,99 stroke:#4e342e,stroke-width:2.5px,color:#4e342e
  classDef stub fill:#f5f5f5,stroke:#9e9e9e,stroke-dasharray:4 3,color:#424242
  class n_bai_2024b_approach_generative_llm_steganalysis,n_cachin_1998_approach_information_theoretic_model,n_cachin_2004_approach_information_theoretic_model,n_hopper_2002_approach_stateful_rejection_sampling,paper_cachin_1998,paper_motwani_2024,n_rippin_2026_approach_agentic_covert_channel_construction,n_roger_2023_approach_paraphrase_defence stub
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
| `lgt-bins` | lgt-vocabulary-codes | Fixed bins | A shared random partition of the vocabulary into equal bins lets each token's bin carry a fixed number of bits. | `dai_2019:surveyed-bins` | 1 |
| `lgt-byte-encodings` | lgt-overt-encodings | Byte encodings | The message is written as Base64, hexadecimal or binary strings. | `tailor_2026:surveyed-hexadecimal` | 5 |
| `lgt-count-state-codes` | lgt-prompted-rule-codes | Count and state-tracking codes | A state is carried by first letters, word or character counts modulo the number of states, or similar countable features. | `zolkowski_2025:surveyed-state-tracking-encodings` | 2 |
| `lgt-coupling` | lgt-sampling-codes | Coupling-based codes | Uniform-looking ciphertext is joined to the covertext distribution by a coupling, so the published token is drawn exactly from the cover distribution. | `schroederdewitt_2022:imec-coding` | 2 |
| `lgt-coupling-public-draft` | lgt-coupling | Maximal coupling through a public draft model | A small public draft model run by both parties partitions the vocabulary and a maximal coupling samples the token from the sender's private distribution. | `pang_2026:approach-codetta-keyed` | 1 |
| `lgt-distribution-copies` | lgt-sampling-codes | Distribution copies | Rotated copies of the token distribution are built at each step and the message chooses which copy to sample from. | `ding_2023:distribution-copies` | 1 |
| `lgt-entity-keyword-mapping` | lgt-semantic-choice | Entity and keyword mapping | Message bits index entries in a shared entity tree or keyword set, which the LLM is prompted to mention and the receiver reads back. | `bai_2024:approach-semantic-steganography` | 2 |
| `lgt-enumerated-openers` | lgt-prompted-rule-codes | Enumerated openers | The message selects one of a fixed list of openings or stated values with which the answer begins. | `roger_2023:surveyed-introduction-variations` | 2 |
| `lgt-feedback-coding` | lgt-sampling-codes | Feedback (posterior-matching) coding | Each generated token is seen by both parties and guides the next embedding step, as in coding over a channel with noiseless feedback. | `guo_2026:approach-bam-feedback-coding` | 1 |
| `lgt-finetuned-encoders` | — | Encoders trained into the weights | A model is fine-tuned so that it writes a secret from its prompt into ordinary completions, with the code held in its weights rather than in a sampling rule. | `westphal_2026:approach-evasive-steganographic-trojan` | 1 |
| `lgt-grouping` | lgt-sampling-codes | Probability grouping | The vocabulary is split into groups of near-equal probability and the message chooses a group, recursively, before a token is sampled within it. | `zhang_2021:adg-adaptive-dynamic-grouping` | 1 |
| `lgt-huffman` | lgt-vocabulary-codes | Per-step Huffman codes | A Huffman code is rebuilt from the model's distribution at every step and the message bits walk the code tree to a token. | `dai_2019:surveyed-vlc-huffman` | 2 |
| `lgt-huffman-patient` | lgt-huffman | Thresholded (patient) Huffman | The Huffman code is used only at steps where its distance from the model's distribution is below a threshold; other steps sample normally. | `dai_2019:approach-patient-huffman` | 1 |
| `lgt-initial-class-codes` | lgt-prompted-rule-codes | Initial-class codes | The class of a token's initial letter (A-M against N-Z) carries a bit, rather than the letter itself. | `tailor_2026:surveyed-word-length-parity-token-initials` | 1 |
| `lgt-interval-adaptive-truncation` | lgt-interval-coding | Interval coding with per-step truncation | The number of candidate tokens kept at each step is chosen adaptively so the truncated distribution stays within a divergence bound of the model's. | `shen_2020:approach-saac` | 1 |
| `lgt-interval-coding` | lgt-sampling-codes | Interval (arithmetic) coding | The message is read as a point in the unit interval and decoded into tokens by arithmetic coding run in reverse over the model's distributions. | `ziegler_2019:reverse-arithmetic-coding` | 3 |
| `lgt-interval-keyed-randomness` | lgt-interval-coding | Keyed sampling-randomness embedding | Pseudorandomly masked message bits stand in for the sampling random number, and the bits consumed per token follow the token's entropy. | `kaptchuk_2021:approach-meteor` | 1 |
| `lgt-letter-position-codes` | lgt-prompted-rule-codes | Letter-position codes (acrostics) | Message letters are placed at agreed positions, such as the first letters of sentences or words. | `tailor_2026:surveyed-sentence-initials` | 5 |
| `lgt-literal-payload-names` | lgt-prompted-rule-codes | Literal payload as a name | The payload is written directly into the text as an imagined acronym or name. | `roger_2023:acronym-literal-payload` | 1 |
| `lgt-overt-encodings` | lgt-prompted-rule-codes | Overt encodings and ciphers | The message is transformed by a standard encoding or cipher and written into the text, hiding its content but not its presence. | `tailor_2026:surveyed-base64` | 7 |
| `lgt-prompted-rule-codes` | — | Prompted pre-agreed rule codes | The model is told an explicit encoding rule and applies it while writing; the receiver applies the inverse rule. | `tailor_2026:six-encoding-rules` | 17 |
| `lgt-public-key-sampling` | lgt-sampling-codes | Keyless key exchange in samples | Public-key (lattice) ciphertext is carried in sampled text so two parties with no shared secret can agree a key covertly. | `pang_2026:approach-codetta-key-exchange` | 1 |
| `lgt-reasoning-strategy-choice` | lgt-semantic-choice | Reasoning-strategy choice | Each reasoning step carries a bit by realising or omitting an agreed reasoning strategy. | `zhou_2026:approach-conceptual-steganography` | 1 |
| `lgt-sampling-codes` | — | Distribution-preserving sampling codes | The message replaces or steers the randomness used to sample each token from a shared language model, so the stegotext follows the model's own distribution. | `kaptchuk_2021:embed-in-sampling-randomness` | 9 |
| `lgt-semantic-choice` | — | Black-box semantic-choice schemes | The message picks the keywords a generated sentence is built around (subject, predicate, object, emotion), and an LLM reached through prompts writes the sentence. | `wu_2024:carrier-keyword-sets` | 3 |
| `lgt-substitution-ciphers` | lgt-overt-encodings | Substitution ciphers | Each letter of the message is replaced by another under a fixed mapping. | `tailor_2026:surveyed-fixed-letter-substitution` | 3 |
| `lgt-surface-formatting` | lgt-prompted-rule-codes | Surface-formatting codes | Bits are carried by formatting choices such as capitalisation, markdown, whitespace runs or interjections. | `schulz_2026:approach-formatting-and-knapsack-encodings` | 2 |
| `lgt-task-choice-codes` | — | Free task-choice codes | The repetitive, supposedly arbitrary choices a task leaves open, such as variable names or items chosen, carry the information. | `schulz_2026:arbitrary-choice-covers` | 1 |
| `lgt-vocabulary-codes` | — | Bin and Huffman codes | The vocabulary is divided into shared disjoint bins, or another shared code over it, and the token chosen at each step carries a block of message bits. | `dai_2019:surveyed-bins` | 3 |
| `lgt-watermark-codes` | — | Watermark-derived multi-bit codes | A language-model watermark is extended to carry a message, which a keyed detector recovers from the generated text. | `zamir_2024:approach-undetectable-llm-stego` | 3 |
| `lgt-watermark-pseudorandom` | lgt-watermark-codes | Pseudorandom undetectable watermark codes | Keyed pseudorandom sampling makes the watermark, and so the payload, computationally undetectable without the key. | `zamir_2024:approach-undetectable-llm-stego` | 1 |
| `lgt-watermark-token-partition` | lgt-watermark-codes | Token-partition (red-green) watermark codes | The message seeds or selects a partition of tokens into favoured and disfavoured sets, and the decoder picks the message whose partition scores highest. | `roger_2023:surveyed-cycle-shifting-watermark` | 2 |

## Lineage edges (31)

| source | kind | target | lifted_from | ledger line |
| --- | --- | --- | --- | --- |
| `bai_2024:approach-semantic-steganography` | Qualifies | `ding_2023:approach-discop` | `bai_2024:entropy-bounds-provably-secure-named` | bai_2024.md:193 |
| `bai_2024:approach-semantic-steganography` | Qualifies | `kaptchuk_2021:approach-meteor` | `bai_2024:entropy-bounds-provably-secure-named` | bai_2024.md:191 |
| `bai_2024:approach-semantic-steganography` | Qualifies | `schroederdewitt_2022:approach-imec` | `bai_2024:entropy-bounds-provably-secure-named` | bai_2024.md:192 |
| `bai_2024b:approach-generative-llm-steganalysis` | Qualifies | `ding_2023:approach-discop` | `bai_2024b:general-steganalysis-discop` | bai_2024b.md:189 |
| `bai_2024b:approach-generative-llm-steganalysis` | Qualifies | `zhang_2021:approach-adg` | `bai_2024b:detects-ac-adg-near-zero-deviation` | bai_2024b.md:187 |
| `bai_2024b:approach-generative-llm-steganalysis` | Qualifies | `ziegler_2019:approach-arithmetic-coding` | `bai_2024b:detects-ac-adg-near-zero-deviation` | bai_2024b.md:188 |
| `ding_2023:approach-discop` | Depends-on | `paper:cachin_1998` | `ding_2023:cachin-kl-zero`, `cachin_1998:relative-entropy-security` | ding_2023.md:155 |
| `ding_2023:approach-discop` | Qualifies | `kaptchuk_2021:approach-meteor` | — | ding_2023.md:154 |
| `ding_2023:approach-discop` | Rebuts | `zhang_2021:approach-adg` | — | ding_2023.md:153 |
| `guo_2026:approach-bam-feedback-coding` | Depends-on | `cachin_2004:approach-information-theoretic-model` | `guo_2026:security-after-cachin` | guo_2026.md:208 |
| `guo_2026:approach-bam-feedback-coding` | Qualifies | `kaptchuk_2021:approach-meteor` | `guo_2026:white-box-schemes-named` | guo_2026.md:206 |
| `guo_2026:approach-bam-feedback-coding` | Qualifies | `schroederdewitt_2022:approach-imec` | `guo_2026:white-box-schemes-named` | guo_2026.md:205 |
| `guo_2026:approach-bam-feedback-coding` | Qualifies | `ziegler_2019:approach-arithmetic-coding` | `guo_2026:white-box-schemes-named` | guo_2026.md:207 |
| `guo_2026:approach-bam-feedback-coding` | Refines | `zamir_2024:approach-undetectable-llm-stego` | `guo_2026:feedback-after-zamir` | guo_2026.md:204 |
| `kaptchuk_2021:approach-meteor` | Depends-on | `ziegler_2019:approach-arithmetic-coding` | `kaptchuk_2021:codebase-builds-on-ziegler` | kaptchuk_2021.md:204 |
| `kaptchuk_2021:approach-meteor` | Refines | `hopper_2002:approach-stateful-rejection-sampling` | `kaptchuk_2021:prior-symmetric-entropy-gathering` | kaptchuk_2021.md:201 |
| `kaptchuk_2021:approach-meteor` | Supersedes | `dai_2019:approach-patient-huffman` | `kaptchuk_2021:nlp-constructions-named` | kaptchuk_2021.md:203 |
| `kaptchuk_2021:approach-meteor` | Supersedes | `ziegler_2019:approach-arithmetic-coding` | `kaptchuk_2021:nlp-constructions-named` | kaptchuk_2021.md:202 |
| `paper:motwani_2024` | Depends-on | `schroederdewitt_2022:approach-imec` | `motwani_2024:builds-on-ai-stego` | motwani_2024.md:184 |
| `rippin_2026:approach-agentic-covert-channel-construction` | Depends-on | `zamir_2024:approach-undetectable-llm-stego` | — | rippin_2026.md:171 |
| `schroederdewitt_2022:approach-imec` | Depends-on | `cachin_1998:approach-information-theoretic-model` | — | schroederdewitt_2022.md:163 |
| `schroederdewitt_2022:approach-imec` | Supersedes | `dai_2019:approach-patient-huffman` | `schroederdewitt_2022:builds-on-imec-supersedes-coding` | schroederdewitt_2022.md:166 |
| `schroederdewitt_2022:approach-imec` | Supersedes | `kaptchuk_2021:approach-meteor` | `schroederdewitt_2022:builds-on-imec-supersedes-coding` | schroederdewitt_2022.md:165 |
| `schroederdewitt_2022:approach-imec` | Supersedes | `zhang_2021:approach-adg` | `schroederdewitt_2022:adg-not-perfectly-secure` | schroederdewitt_2022.md:167 |
| `schroederdewitt_2022:approach-imec` | Supersedes | `ziegler_2019:approach-arithmetic-coding` | `schroederdewitt_2022:builds-on-imec-supersedes-coding` | schroederdewitt_2022.md:164 |
| `shen_2020:approach-saac` | Depends-on | `dai_2019:approach-patient-huffman` | `dai_2019:tvd-security-notion` | shen_2020.md:203 |
| `shen_2020:approach-saac` | Refines | `ziegler_2019:approach-arithmetic-coding` | `ziegler_2019:arithmetic-coding-neural-lm` | shen_2020.md:202 |
| `wu_2024:approach-llm-stega` | Qualifies | `dai_2019:approach-patient-huffman` | — | wu_2024.md:194 |
| `wu_2024:approach-llm-stega` | Qualifies | `ziegler_2019:approach-arithmetic-coding` | `ziegler_2019:arithmetic-coding-neural-lm` | wu_2024.md:193 |
| `zhang_2021:approach-adg` | Depends-on | `paper:cachin_1998` | `cachin_1998:relative-entropy-security` | zhang_2021.md:194 |
| `zhou_2026:approach-conceptual-steganography` | Qualifies | `roger_2023:approach-paraphrase-defence` | `zhou_2026:paraphrase-defence-exploited` | zhou_2026.md:171 |

## Approaches

| address | name | family | technique | channel | key | access | capacity | mechanism | landable | mechanism_evidence | carrier | acquisition |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `bai_2024:approach-semantic-steganography` | semantic steganography: secret bits select a class in a semantic space built from ontology-entity trees, and an LLM writes a sentence of that class | llm-generative-text | lgt-entity-keyword-mapping | topic-semantic | shared-key | prompt | follows entity-distribution entropy; about 28 bit/sentence versus about 2.5 for AC on ChatGLM2-6B | m-entity-tree-class | yes | own | topic of generated sentences (entity class) | specified |
| `dai_2019:approach-patient-huffman` | patient-Huffman, per-step Huffman coding of the LM distribution that encodes only at steps where the Huffman distribution is close enough to the LM's | llm-generative-text | lgt-huffman-patient | distributional-sampling | shared-key | logits | — | m-huffman-patient | yes | own | token sampling in generated text | specified |
| `dai_2019:surveyed-bins` | Bins (Fang et al. 2017), a shared random partition of the vocabulary into equal bins, the bin carrying a block of ciphertext | llm-generative-text | lgt-bins | lexical | shared-key | logits | — | m-fixed-bins | yes | own | token choice in generated text | specified |
| `dai_2019:surveyed-vlc-huffman` | VLC (Yang et al. 2018), a Huffman code over the vocabulary rebuilt at each step, walked by the ciphertext bits | llm-generative-text | lgt-huffman | distributional-sampling | shared-model | logits | — | m-huffman-every-step | yes | own | token sampling in generated text | specified |
| `ding_2023:approach-discop` | Discop, sampling from one of several rotated "distribution copies" chosen by the message, so the model's distribution is kept exactly; with KL measured against Meteor and ADG | llm-generative-text | lgt-distribution-copies | distributional-sampling | shared-key | logits | 3.48 to 5.76 bits per token, about 0.92 to 0.95 of the entropy limit | m-distribution-copies | yes | own | token sampling (also image and speech generation) | specified |
| `guo_2026:approach-bam-feedback-coding` | BAM (Burnashev Adaptive Posterior Matching): black-box LLM steganography recast as communication over a channel with causal, noiseless feedback, coded by posterior matching with a decode-and-confirm phase | llm-generative-text | lgt-feedback-coding | distributional-sampling | shared-key | sender: logits; receiver: no model access | 8-bit payload in under 50 tokens at most 0.1% message error; chess moves average 5.0 coded bits | m-feedback-coding; m-coupling | yes | own;sibling:ot-coupling-sampler | token sampling in agent conversation | specified |
| `kaptchuk_2021:approach-meteor` | Meteor: a symmetric-key, stateful, provably secure scheme that embeds message bits in the sampling randomness of a generative model, at a rate that follows the instantaneous entropy | llm-generative-text | lgt-interval-keyed-randomness | distributional-sampling | shared-key | logits | throughput proportional to channel entropy; bits per token depend strongly on the model | m-interval-keyed-randomness | yes | sibling:fresh-prg-mask | token sampling in generated text | specified |
| `motwani_2024:surveyed-first-letter-acrostic` | instructed first-letter (acrostic) covertext scheme | llm-generative-text | lgt-letter-position-codes | lexical | codebook | prompt | one character per word | m-letter-position | yes | own | first letters of words in text | prompted |
| `motwani_2024:surveyed-standard-ciphers` | standard ciphers (Base64, Caesar) as an encoding capability | llm-generative-text | lgt-byte-encodings; lgt-substitution-ciphers | other (cipher encoding, not hidden) | codebook | prompt | — | m-byte-encoding; m-letter-substitution-cipher | yes | own;own | encoded string in text | prompted |
| `pang_2026:approach-codetta-key-exchange` | Codetta's keyless steganographic key exchange, MLWE ciphertexts carried over honest model samples | llm-generative-text | lgt-public-key-sampling | distributional-sampling | none | sender: logits; receiver: logits of the public draft model | about 80k visible tokens per 128-bit key (640 tokens per key bit) | m-sampled-lattice-key-exchange | yes | own | token sampling in agent messages | specified |
| `pang_2026:approach-codetta-keyed` | Codetta's keyed protocol, high-capacity asymmetric steganography through a public draft model and maximal coupling | llm-generative-text | lgt-coupling-public-draft | distributional-sampling | shared-key | sender: logits; receiver: logits of the public draft model | 0.45-0.57 bits per token (Ministral); 4.1-6.4x draft-free LDPC, 16-94x ARS; below 0.04 on low-entropy CTF text | m-maximal-coupling-public-draft | yes | own | token sampling in agent messages, files or wikis | specified |
| `roger_2023:surveyed-acronyms` | prompted acronym scheme | llm-generative-text | lgt-literal-payload-names | lexical | — | prompt | 30 bits per answer | m-literal-payload-name | yes | sibling:acronym-literal-payload | an acronym or name in the answer text | prompted |
| `roger_2023:surveyed-age-instructions` | prompted age-instruction scheme | llm-generative-text | lgt-enumerated-openers | numeric-annotation | codebook | prompt | ages in [0,63] | m-stated-value-code | yes | own | a stated number (age) at the start of the answer | prompted |
| `roger_2023:surveyed-balanced-marking` | balanced-marking watermark used for steganography | llm-generative-text | lgt-watermark-token-partition | distributional-sampling | shared-key | logits | — | m-token-partition-watermark | yes | own | token sampling in generated text | specified |
| `roger_2023:surveyed-cycle-shifting-watermark` | cycle-shifting watermark used for steganography | llm-generative-text | lgt-watermark-token-partition | distributional-sampling | shared-key | logits | — | m-token-partition-watermark | yes | own | token sampling in generated text | specified |
| `roger_2023:surveyed-introduction-variations` | prompted introduction-variation scheme | llm-generative-text | lgt-enumerated-openers | structural-format | codebook | prompt | 16 messages | m-phrase-codebook | yes | own | introduction sentence of an answer | prompted |
| `roger_2023:surveyed-scratchpad-scheme` | scratchpad scheme in which the model devises its own encoding | llm-generative-text | — | other (model-chosen) | — | prompt | 30 bits per answer | m-scheme-discovery-condition | no | own | — | — |
| `schroederdewitt_2022:approach-imec` | minimum entropy coupling steganography (iMEC): encode by coupling uniform-looking ciphertext with the covertext distribution, which makes the procedure perfectly secure and maximally efficient under Cachin's model | llm-generative-text | lgt-coupling | distributional-sampling | shared-key | logits | maximal throughput iff minimum entropy coupling; encoding efficiency above baselines at 20-bit blocks | m-min-entropy-coupling | yes | own | token sampling (also audio and image generation) | specified |
| `schulz_2026:approach-formatting-and-knapsack-encodings` | six surface-formatting encodings and the knapsack cover, applicable programmatically to existing text | llm-generative-text | lgt-surface-formatting; lgt-task-choice-codes | structural-format | codebook | prompt | one symbol per word, whitespace run or sentence; one bit per knapsack item | m-surface-formatting; m-item-inclusion-bits | yes | own;own | formatting of answer text; item choices in a knapsack solution | prompted;rl-trained;weight-trained |
| `shen_2020:approach-saac` | SAAC, arithmetic coding over a pretrained LM in which the top-K truncation is re-chosen at every step to meet a per-step bound | llm-generative-text | lgt-interval-adaptive-truncation | distributional-sampling | shared-model | logits | about 4.8 bits per word at delta 0.01 (4.862 on Drug); 15.3% more bits per word than the prior best | m-interval-adaptive-truncation | yes | own | token sampling in generated text | specified |
| `tailor_2026:surveyed-alternating-sentence-initials` | alternating sentence initials (prescribed rule) | llm-generative-text | lgt-letter-position-codes | lexical | codebook | prompt | one letter per two sentences | m-letter-position | yes | own | first letters of alternate sentences | prompted |
| `tailor_2026:surveyed-base64` | Base64 (prescribed rule) | llm-generative-text | lgt-byte-encodings | other (literal Base64 string) | codebook | prompt | — | m-byte-encoding | yes | own | encoded string in text | prompted |
| `tailor_2026:surveyed-eight-bit-binary` | eight-bit binary (prescribed rule) | llm-generative-text | lgt-byte-encodings | other (literal binary string) | codebook | prompt | eight binary digits per character | m-byte-encoding | yes | own | encoded string in text | prompted |
| `tailor_2026:surveyed-fixed-letter-substitution` | fixed-letter substitution (prescribed rule) | llm-generative-text | lgt-substitution-ciphers | other (substitution-cipher letters) | codebook | prompt | — | m-letter-substitution-cipher | yes | own | enciphered letters in text | prompted |
| `tailor_2026:surveyed-hexadecimal` | hexadecimal (prescribed rule) | llm-generative-text | lgt-byte-encodings | other (literal hex string) | codebook | prompt | — | m-byte-encoding | yes | own | encoded string in text | prompted |
| `tailor_2026:surveyed-sentence-initials` | sentence initials (prescribed rule) | llm-generative-text | lgt-letter-position-codes | lexical | codebook | prompt | one letter per sentence | m-letter-position | yes | own | first letters of sentences | prompted |
| `tailor_2026:surveyed-word-length-parity-token-initials` | word-length parity and token initials (not prescribed; found in model outputs) | llm-generative-text | lgt-count-state-codes; lgt-initial-class-codes | lexical | none | prompt | word-length parity: one bit per word | m-length-parity; m-initial-class | yes | own;own | word lengths and initial letters in text | prompted+unprescribed |
| `westphal_2026:approach-evasive-steganographic-trojan` | the evasive steganographic trojan: an LLM fine-tuned to encode prompt-borne secrets into ordinary completions, then adversarially fine-tuned against refitted ridge critics so that probes see little beyond base-model signal | llm-generative-text | lgt-finetuned-encoders | lexical | shared-model | training | 32 bits per 32-token completion (one bit per token) | m-hyperplane-buckets | yes | sibling:hyperplane-bucket-encoding | token choice in completions | weight-trained |
| `wu_2024:approach-llm-stega` | LLM-Stega, black-box steganography through an LLM's user interface: keyword sets from the LLM, an encrypted index mapping, and prompts that write and read back the stego sentence | llm-generative-text | lgt-entity-keyword-mapping | lexical | shared-key | prompt | 64 bits per sentence; 5.93 bpw (Entertainment News) and 4.81 bpw (science-fiction reviews) | m-keyword-set-index | yes | sibling:augmented-keyword-index-mapping | keywords of generated sentences | specified |
| `zamir_2024:approach-undetectable-llm-stego` | undetectable LLM steganography: the CGZ undetectable watermark extended to carry a multi-bit payload, recovered with a secret key through a dynamic error-correcting code with feedback | llm-generative-text | lgt-watermark-pseudorandom | distributional-sampling | shared-key | sender: logits; receiver: no model access | linear in response length (asymptotically optimal), only for high-entropy responses | m-pseudorandom-watermark-code | yes | own | token sampling in an LLM response | specified |
| `zhang_2021:approach-adg` | ADG, equal-probability grouping of the vocabulary at each step, repeated recursively on the selected group, then sampling inside it | llm-generative-text | lgt-grouping | distributional-sampling | shared-model | logits | about 5.1 to 5.7 bits per word on LSTM models (Movie 5.147, News 5.650, Tweet 5.411) | m-recursive-balanced-grouping | yes | own | token sampling in generated text | specified |
| `zhou_2026:approach-conceptual-steganography` | conceptual steganography: each chain-of-thought step carries a bit in which reasoning behaviour it shows, not in its words, so a content-preserving paraphrase leaves the bit in place | llm-generative-text | lgt-reasoning-strategy-choice | topic-semantic | codebook | — | about 4.4 to 6.4 bits per CoT | m-reasoning-behaviour-choice | yes | own | reasoning behaviour of chain-of-thought steps | prompted |
| `ziegler_2019:approach-arithmetic-coding` | arithmetic-coding steganography over a large neural language model: a uniform message is decoded into tokens so that the cover text follows the model's distribution | llm-generative-text | lgt-interval-coding | distributional-sampling | shared-model | logits | entropy of the induced distribution; humans fooled at 1 bit/word; minimum KL near 4 bits/word | m-interval-plain | yes | own | token sampling in generated text | specified |
| `zolkowski_2025:surveyed-byte-encodings` | byte-encoding schemes (Base64, UTF-8 binary, Hex and their variants) | llm-generative-text | lgt-byte-encodings | other (overt encoding) | codebook | prompt | — | m-byte-encoding | yes | own | encoded string in text | prompted |
| `zolkowski_2025:surveyed-letter-position-acrostics` | letter-position acrostic schemes given to encoder and decoder | llm-generative-text | lgt-letter-position-codes | lexical | codebook | prompt | — | m-letter-position | yes | own | first letters of sentences or words | prompted |
| `zolkowski_2025:surveyed-model-generated-subtlety` | model-generated encoding schemes at three degrees of subtlety | llm-generative-text | — | other (model-chosen) | none | prompt | — | m-scheme-discovery-condition | no | own | — | — |
| `zolkowski_2025:surveyed-rotation-substitution` | rotation and substitution ciphers | llm-generative-text | lgt-substitution-ciphers | other (overt cipher) | codebook | prompt | — | m-letter-substitution-cipher | yes | own | enciphered letters in text | prompted |
| `zolkowski_2025:surveyed-state-tracking-encodings` | state-tracking encodings by first letter, sentence length, special characters and terminal punctuation | llm-generative-text | lgt-count-state-codes; lgt-letter-position-codes; lgt-surface-formatting | syntactic | codebook | prompt | one state per sentence | m-letter-position; m-count-code; m-punctuation-symbol | yes | own;own;own | sentence initials, sentence lengths and punctuation in text | prompted |
