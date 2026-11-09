---
generated: 2026-11-08T20:09:54+03:00
---

# Approach map — overview

Built by `tools/build_approach_map.py` from `C:\Users\user\Documents\GitHub\hypersteg_chess\hypersteg_novelty_kit_20261108\literature\verified_claims`, the features table `C:\Users\user\Documents\GitHub\hypersteg_chess\hypersteg_novelty_kit_20261108\maps\approach_features.tsv` and the technique taxonomy `C:\Users\user\Documents\GitHub\hypersteg_chess\hypersteg_novelty_kit_20261108\maps\technique_taxonomy.tsv`. View: `both`; inferred links: `off`. Derived: edit the ledgers or the tables, never this file. Family and technique nodes only; each family's approaches are in its own file, listed below.

- approaches: 195
- families: 14
- techniques: 142
- lineage edges drawn: 88 (11 inside a single node, drawn in the family files)
- of which lifted from a non-approach claim: 68
- paper nodes: 13
- unclassified approaches: 0
- edges not placed, no approach claim in the ledger: 0
- edges not placed, unresolved: 0
- edges whose ends lift onto one approach: 0

```mermaid
flowchart LR
  subgraph fam_audio_g["audio (2)"]
    tech_au_deep_speech_hiding["Deep speech-in-speech hiding (2)"]
  end
  subgraph fam_foundations_theory_g["foundations-theory (20)"]
    fam_foundations_theory("foundations-theory: 2 direct")
    tech_ft_balanced_partition["Balanced partition (2)"]
    tech_ft_capacity_laws["Capacity laws (2)"]
    tech_ft_complexity_theoretic["Complexity-theoretic security (1)"]
    tech_ft_constructions["Constructions with stated security (12)"]
    tech_ft_informal_limits["Informal limits and terminology (1)"]
    tech_ft_information_theoretic["Information-theoretic security (2)"]
    tech_ft_keyed_feature_function["Keyed function of a robust feature (1)"]
    tech_ft_keyed_parity["Keyed parity embedding (2)"]
    tech_ft_public_key_steganography["Public-key steganography (1)"]
    tech_ft_rejection_sampling["Rejection sampling (2)"]
    tech_ft_security_models["Security models (4)"]
    tech_ft_shared_sample_robust_code["Shared-sample robust code (1)"]
    tech_ft_subliminal_channel["Subliminal channels (1)"]
    tech_ft_uniform_cover["Uniform-cover schemes (1)"]
    tech_ft_universal_compression["Universal-compression stegosystems (2)"]
  end
  subgraph fam_game_and_chess_g["game-and-chess (13)"]
    fam_game_and_chess("game-and-chess: 2 direct")
    tech_gc_action_commands["Real-time action commands (1)"]
    tech_gc_chess_data_codebook["Chess-data codebook (1)"]
    tech_gc_comment_codebook["Comment codebook (1)"]
    tech_gc_equivalent_moves["Outcome-equivalent moves (1)"]
    tech_gc_keyed_strategy_set["Keyed strategy-set coding (1)"]
    tech_gc_learned_action_policies["Learned action policies (1)"]
    tech_gc_mixed_radix["Mixed-radix legal-move encoding (1)"]
    tech_gc_move_choice["Move-choice channels (6)"]
    tech_gc_move_index["Move-choice indexing (3)"]
    tech_gc_ranked_moves["Ranked-move index (1)"]
    tech_gc_record_annotation["Game-record and annotation channels (3)"]
    tech_gc_side_signals["Physical and acoustic side signals (2)"]
    tech_gc_variation_insertion["Inserted variations (1)"]
  end
  subgraph fam_hyperbolic_g["hyperbolic (1)"]
    tech_hy_hyperbolic_hiding["Hyperbolic-space hiding (1)"]
  end
  subgraph fam_image_classical_g["image-classical (1)"]
    tech_ic_adversarial_costs["Adversarially adjusted costs (1)"]
    tech_ic_distortion_minimisation["Distortion-minimising embedding (1)"]
  end
  subgraph fam_image_deep_g["image-deep (8)"]
    tech_id_adversarial_training["Adversarially trained hiding (3)"]
    tech_id_cover_dependent["Cover-dependent deep hiding (2)"]
    tech_id_deep_hiding["Learned encoder-decoder hiding (8)"]
    tech_id_physical_channel["Physical-channel hiding (2)"]
    tech_id_universal["Universal deep hiding (1)"]
  end
  subgraph fam_image_generative_coverless_g["image-generative-coverless (17)"]
    fam_image_generative_coverless("image-generative-coverless: 0 direct")
    tech_igc_attribute_mapping["Attribute mapping (cover selection) (9)"]
    tech_igc_diffusion_inversion["Diffusion inversion translation (1)"]
    tech_igc_generative_synthesis["Generative synthesis (8)"]
    tech_igc_grille_inpainting["Grille and inpainting (1)"]
    tech_igc_hash_mapping["Image-hash mapping (6)"]
    tech_igc_latent_mapping["Message-to-latent mapping (3)"]
    tech_igc_latent_search["Latent search (1)"]
    tech_igc_model_database["Generator-model database (1)"]
    tech_igc_patch_retrieval["Partial-duplicate patch retrieval (2)"]
    tech_igc_secret_conditioned_generator["Secret-conditioned generator (1)"]
    tech_igc_visual_word_mapping["Visual-word mapping (1)"]
  end
  subgraph fam_linguistic_text_g["linguistic-text (3)"]
    fam_linguistic_text("linguistic-text: 2 direct")
    tech_lt_markov_generation["Markov-model generation with range partition (1)"]
  end
  subgraph fam_llm_capability_eval_g["llm-capability-eval (17)"]
    fam_llm_capability_eval("llm-capability-eval: 2 direct")
    tech_lce_agentic_construction["Agentic stegosystem construction (1)"]
    tech_lce_codeword_substitution["Codeword substitution (1)"]
    tech_lce_control_evaluations["Control evaluations (1)"]
    tech_lce_coordination_evals["Coordination-without-communication evaluations (1)"]
    tech_lce_encoded_reasoning["Prompted encoded reasoning (1)"]
    tech_lce_eval_frameworks["Evaluation frameworks and decompositions (2)"]
    tech_lce_message_passing["Encoded message passing (3)"]
    tech_lce_overt_encodings["Overt encodings as capabilities (1)"]
    tech_lce_partial_encoding["Graded partial encoding (1)"]
    tech_lce_prompted_elicitation["Prompted elicitation (6)"]
    tech_lce_rl_learned_codes["Codes learned under RL pressure (2)"]
    tech_lce_scheme_discovery["Scheme-discovery condition (0)"]
    tech_lce_stateless_subversion["Stateless protocol subversion (1)"]
    tech_lce_taught_schemes["Taught schemes (2)"]
    tech_lce_trained_elicitation["Training-induced steganography (4)"]
  end
  subgraph fam_llm_generative_text_g["llm-generative-text (38)"]
    fam_llm_generative_text("llm-generative-text: 2 direct")
    tech_lgt_bins["Fixed bins (1)"]
    tech_lgt_byte_encodings["Byte encodings (5)"]
    tech_lgt_count_state_codes["Count and state-tracking codes (2)"]
    tech_lgt_coupling["Coupling-based codes (2)"]
    tech_lgt_coupling_public_draft["Maximal coupling through a public draft model (1)"]
    tech_lgt_distribution_copies["Distribution copies (1)"]
    tech_lgt_entity_keyword_mapping["Entity and keyword mapping (2)"]
    tech_lgt_enumerated_openers["Enumerated openers (2)"]
    tech_lgt_feedback_coding["Feedback (posterior-matching) coding (1)"]
    tech_lgt_finetuned_encoders["Encoders trained into the weights (1)"]
    tech_lgt_grouping["Probability grouping (1)"]
    tech_lgt_huffman["Per-step Huffman codes (2)"]
    tech_lgt_huffman_patient["Thresholded (patient) Huffman (1)"]
    tech_lgt_initial_class_codes["Initial-class codes (1)"]
    tech_lgt_interval_adaptive_truncation["Interval coding with per-step truncation (1)"]
    tech_lgt_interval_coding["Interval (arithmetic) coding (3)"]
    tech_lgt_interval_keyed_randomness["Keyed sampling-randomness embedding (1)"]
    tech_lgt_letter_position_codes["Letter-position codes (acrostics) (5)"]
    tech_lgt_literal_payload_names["Literal payload as a name (1)"]
    tech_lgt_overt_encodings["Overt encodings and ciphers (7)"]
    tech_lgt_prompted_rule_codes["Prompted pre-agreed rule codes (17)"]
    tech_lgt_public_key_sampling["Keyless key exchange in samples (1)"]
    tech_lgt_reasoning_strategy_choice["Reasoning-strategy choice (1)"]
    tech_lgt_sampling_codes["Distribution-preserving sampling codes (9)"]
    tech_lgt_semantic_choice["Black-box semantic-choice schemes (3)"]
    tech_lgt_substitution_ciphers["Substitution ciphers (3)"]
    tech_lgt_surface_formatting["Surface-formatting codes (2)"]
    tech_lgt_task_choice_codes["Free task-choice codes (1)"]
    tech_lgt_vocabulary_codes["Bin and Huffman codes (3)"]
    tech_lgt_watermark_codes["Watermark-derived multi-bit codes (3)"]
    tech_lgt_watermark_pseudorandom["Pseudorandom undetectable watermark codes (1)"]
    tech_lgt_watermark_token_partition["Token-partition (red-green) watermark codes (2)"]
  end
  subgraph fam_multi_agent_collusion_g["multi-agent-collusion (22)"]
    fam_multi_agent_collusion("multi-agent-collusion: 1 direct")
    tech_mac_authenticated_throwing["Authenticate, then throw games (1)"]
    tech_mac_collusion_audits["Collusion audits and taxonomies (3)"]
    tech_mac_collusion_benchmarks["Collusion benchmarks (2)"]
    tech_mac_covertext_codebooks["Natural-language covertext codebooks (3)"]
    tech_mac_emergent_codes["Emergent codes in interaction (2)"]
    tech_mac_focality_prompts["Focality prompts (3)"]
    tech_mac_gradient_rl["Gradient-based RL (2)"]
    tech_mac_in_context_rl["In-context RL (1)"]
    tech_mac_input_triggers["Input triggers (1)"]
    tech_mac_learned_codes["Codes learned by optimisation (5)"]
    tech_mac_learned_tacit["Learned tacit collusion (1)"]
    tech_mac_output_signals["Output signals (1)"]
    tech_mac_pre_agreed_codes["Pre-agreed codes and signals (6)"]
    tech_mac_risk_taxonomies["Risk taxonomies (1)"]
    tech_mac_schelling_prompted["Prompted Schelling coordination (5)"]
    tech_mac_tacit_coordination["Tacit coordination (7)"]
    tech_mac_trigger_signals["Collusion trigger signals (2)"]
    tech_mac_zero_shot_conventions["Symmetry-robust conventions (1)"]
  end
  subgraph fam_non_steganography_foundation_g["non-steganography-foundation (35)"]
    fam_non_steganography_foundation("non-steganography-foundation: 0 direct")
    tech_nsf_chess_language["Chess language and commentary (6)"]
    tech_nsf_chess_language_models["Chess language models and datasets (3)"]
    tech_nsf_commentary_evaluation["Commentary evaluation (1)"]
    tech_nsf_commentary_generation["Commentary generation (2)"]
    tech_nsf_engine_and_opening_analysis["Engine and opening-tree analysis (3)"]
    tech_nsf_engine_benchmark_assessment["Engine-benchmarked skill assessment (6)"]
    tech_nsf_human_move_models["Models of human move choice (11)"]
    tech_nsf_hyperbolic_embeddings["Hyperbolic embeddings and measurement (8)"]
    tech_nsf_hyperbolic_networks["Hyperbolic network layers and agents (6)"]
    tech_nsf_intrinsic_rating["Intrinsic rating models (2)"]
    tech_nsf_llm_chess_play["LLM chess play (1)"]
    tech_nsf_neural_human_move["Neural human-move predictors (3)"]
  end
  subgraph fam_steganalysis_g["steganalysis (13)"]
    fam_steganalysis("steganalysis: 0 direct")
    tech_sa_activation_probes["Activation probes (2)"]
    tech_sa_active_warden["Active-warden defences (2)"]
    tech_sa_concept_lens["Concept-lens readout and intervention (2)"]
    tech_sa_game_record_inference["Game-record inference (1)"]
    tech_sa_game_statistics["Game-statistics attacks (1)"]
    tech_sa_internal_states["Internal-state detection (4)"]
    tech_sa_likelihood_ratio_forensics["Likelihood-ratio forensics (1)"]
    tech_sa_llm_classifiers["LLM-based classifiers (2)"]
    tech_sa_prompted_llm_monitors["Prompted LLM monitors (1)"]
    tech_sa_statistical_features["Statistical and feature steganalysis (3)"]
    tech_sa_text_features["Text feature steganalysis (1)"]
    tech_sa_utility_gap["Decision-theoretic utility gap (1)"]
  end
  subgraph fam_watermarking_g["watermarking (5)"]
    tech_wm_decoder_finetune["Fine-tuned decoder (1)"]
    tech_wm_generative_model["Watermarks in the generator (2)"]
    tech_wm_initial_noise["Initial-noise pattern (1)"]
    tech_wm_learned_post_hoc["Learned post-hoc watermarks (3)"]
  end
  tech_ft_constructions --- tech_ft_balanced_partition
  tech_ft_security_models --- tech_ft_complexity_theoretic
  tech_ft_security_models --- tech_ft_informal_limits
  tech_ft_security_models --- tech_ft_information_theoretic
  tech_ft_constructions --- tech_ft_keyed_feature_function
  tech_ft_constructions --- tech_ft_keyed_parity
  tech_ft_constructions --- tech_ft_public_key_steganography
  tech_ft_constructions --- tech_ft_rejection_sampling
  tech_ft_constructions --- tech_ft_shared_sample_robust_code
  tech_ft_constructions --- tech_ft_subliminal_channel
  tech_ft_constructions --- tech_ft_uniform_cover
  tech_ft_constructions --- tech_ft_universal_compression
  tech_gc_move_choice --- tech_gc_action_commands
  tech_gc_record_annotation --- tech_gc_chess_data_codebook
  tech_gc_record_annotation --- tech_gc_comment_codebook
  tech_gc_move_index --- tech_gc_equivalent_moves
  tech_gc_move_index --- tech_gc_keyed_strategy_set
  tech_gc_move_choice --- tech_gc_learned_action_policies
  tech_gc_move_choice --- tech_gc_mixed_radix
  tech_gc_move_choice --- tech_gc_move_index
  tech_gc_move_index --- tech_gc_ranked_moves
  tech_gc_record_annotation --- tech_gc_variation_insertion
  tech_ic_distortion_minimisation --- tech_ic_adversarial_costs
  tech_id_deep_hiding --- tech_id_adversarial_training
  tech_id_deep_hiding --- tech_id_cover_dependent
  tech_id_deep_hiding --- tech_id_physical_channel
  tech_id_deep_hiding --- tech_id_universal
  tech_igc_generative_synthesis --- tech_igc_diffusion_inversion
  tech_igc_generative_synthesis --- tech_igc_grille_inpainting
  tech_igc_attribute_mapping --- tech_igc_hash_mapping
  tech_igc_generative_synthesis --- tech_igc_latent_mapping
  tech_igc_generative_synthesis --- tech_igc_latent_search
  tech_igc_generative_synthesis --- tech_igc_model_database
  tech_igc_attribute_mapping --- tech_igc_patch_retrieval
  tech_igc_generative_synthesis --- tech_igc_secret_conditioned_generator
  tech_igc_attribute_mapping --- tech_igc_visual_word_mapping
  tech_lce_prompted_elicitation --- tech_lce_agentic_construction
  tech_lce_prompted_elicitation --- tech_lce_encoded_reasoning
  tech_lce_prompted_elicitation --- tech_lce_message_passing
  tech_lce_prompted_elicitation --- tech_lce_overt_encodings
  tech_lce_overt_encodings --- tech_lce_partial_encoding
  tech_lce_trained_elicitation --- tech_lce_rl_learned_codes
  tech_lce_prompted_elicitation --- tech_lce_scheme_discovery
  tech_lce_coordination_evals --- tech_lce_stateless_subversion
  tech_lce_trained_elicitation --- tech_lce_taught_schemes
  tech_lgt_vocabulary_codes --- tech_lgt_bins
  tech_lgt_overt_encodings --- tech_lgt_byte_encodings
  tech_lgt_prompted_rule_codes --- tech_lgt_count_state_codes
  tech_lgt_sampling_codes --- tech_lgt_coupling
  tech_lgt_coupling --- tech_lgt_coupling_public_draft
  tech_lgt_sampling_codes --- tech_lgt_distribution_copies
  tech_lgt_semantic_choice --- tech_lgt_entity_keyword_mapping
  tech_lgt_prompted_rule_codes --- tech_lgt_enumerated_openers
  tech_lgt_sampling_codes --- tech_lgt_feedback_coding
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
  tech_lgt_sampling_codes --- tech_lgt_public_key_sampling
  tech_lgt_semantic_choice --- tech_lgt_reasoning_strategy_choice
  tech_lgt_overt_encodings --- tech_lgt_substitution_ciphers
  tech_lgt_prompted_rule_codes --- tech_lgt_surface_formatting
  tech_lgt_watermark_codes --- tech_lgt_watermark_pseudorandom
  tech_lgt_watermark_codes --- tech_lgt_watermark_token_partition
  tech_mac_pre_agreed_codes --- tech_mac_authenticated_throwing
  tech_mac_collusion_audits --- tech_mac_collusion_benchmarks
  tech_mac_pre_agreed_codes --- tech_mac_covertext_codebooks
  tech_mac_learned_codes --- tech_mac_emergent_codes
  tech_mac_schelling_prompted --- tech_mac_focality_prompts
  tech_mac_learned_codes --- tech_mac_gradient_rl
  tech_mac_learned_codes --- tech_mac_in_context_rl
  tech_mac_trigger_signals --- tech_mac_input_triggers
  tech_mac_tacit_coordination --- tech_mac_learned_tacit
  tech_mac_trigger_signals --- tech_mac_output_signals
  tech_mac_collusion_audits --- tech_mac_risk_taxonomies
  tech_mac_tacit_coordination --- tech_mac_schelling_prompted
  tech_mac_pre_agreed_codes --- tech_mac_trigger_signals
  tech_mac_tacit_coordination --- tech_mac_zero_shot_conventions
  tech_nsf_chess_language --- tech_nsf_chess_language_models
  tech_nsf_chess_language --- tech_nsf_commentary_evaluation
  tech_nsf_chess_language --- tech_nsf_commentary_generation
  tech_nsf_human_move_models --- tech_nsf_engine_benchmark_assessment
  tech_nsf_human_move_models --- tech_nsf_intrinsic_rating
  tech_nsf_human_move_models --- tech_nsf_neural_human_move
  tech_sa_internal_states --- tech_sa_activation_probes
  tech_sa_internal_states --- tech_sa_concept_lens
  tech_sa_statistical_features --- tech_sa_game_statistics
  tech_sa_statistical_features --- tech_sa_likelihood_ratio_forensics
  tech_sa_statistical_features --- tech_sa_text_features
  tech_wm_generative_model --- tech_wm_decoder_finetune
  tech_wm_generative_model --- tech_wm_initial_noise
  fam_foundations_theory ==>|Depends-on ×3| tech_ft_subliminal_channel
  fam_foundations_theory <-->|Restates| tech_ft_balanced_partition
  fam_foundations_theory --x|Supersedes| tech_ft_information_theoretic
  fam_game_and_chess -->|Refines| tech_gc_equivalent_moves
  fam_image_generative_coverless -->|Refines| fam_foundations_theory
  fam_llm_capability_eval ==>|Depends-on| tech_lgt_coupling
  fam_llm_capability_eval -.->|Qualifies| tech_lce_encoded_reasoning
  fam_llm_capability_eval -.->|Qualifies| tech_lce_rl_learned_codes
  fam_llm_capability_eval -->|Refines| fam_multi_agent_collusion
  fam_llm_capability_eval -->|Refines| tech_lce_eval_frameworks
  fam_llm_capability_eval -->|Refines| tech_mac_gradient_rl
  fam_llm_capability_eval -->|Supports| tech_lce_encoded_reasoning
  fam_multi_agent_collusion -.->|Qualifies| tech_sa_active_warden
  fam_multi_agent_collusion -->|Refines| tech_lce_eval_frameworks
  fam_non_steganography_foundation -->|Refines| tech_nsf_hyperbolic_networks
  fam_steganalysis ==>|Depends-on| tech_mac_collusion_benchmarks
  fam_steganalysis -.->|Qualifies| tech_sa_activation_probes
  tech_ft_capacity_laws ==>|Depends-on| tech_ft_information_theoretic
  tech_ft_complexity_theoretic ==>|Depends-on| tech_ft_subliminal_channel
  tech_ft_complexity_theoretic -.->|Qualifies| tech_ft_information_theoretic
  tech_ft_rejection_sampling <-->|Restates| tech_ft_balanced_partition
  tech_ft_rejection_sampling <-->|Restates ×2| tech_ft_informal_limits
  tech_gc_chess_data_codebook -.->|Rebuts| tech_gc_ranked_moves
  tech_gc_keyed_strategy_set ==>|Depends-on| tech_ft_subliminal_channel
  tech_gc_keyed_strategy_set -->|Refines| tech_gc_ranked_moves
  tech_hy_hyperbolic_hiding ==>|Depends-on| tech_nsf_hyperbolic_networks
  tech_lce_agentic_construction ==>|Depends-on| tech_lgt_watermark_pseudorandom
  tech_lce_eval_frameworks -.->|Qualifies ×2| tech_lce_message_passing
  tech_lce_eval_frameworks -.->|Qualifies| tech_mac_gradient_rl
  tech_lce_eval_frameworks -.->|Qualifies| tech_mac_in_context_rl
  tech_lce_stateless_subversion -->|Refines| tech_lce_control_evaluations
  tech_lgt_coupling ==>|Depends-on| tech_ft_information_theoretic
  tech_lgt_coupling --x|Supersedes| tech_lgt_grouping
  tech_lgt_coupling --x|Supersedes| tech_lgt_huffman_patient
  tech_lgt_coupling --x|Supersedes| tech_lgt_interval_coding
  tech_lgt_coupling --x|Supersedes| tech_lgt_interval_keyed_randomness
  tech_lgt_distribution_copies ==>|Depends-on| fam_foundations_theory
  tech_lgt_distribution_copies -.->|Qualifies| tech_lgt_interval_keyed_randomness
  tech_lgt_distribution_copies -.->|Rebuts| tech_lgt_grouping
  tech_lgt_entity_keyword_mapping -.->|Qualifies| tech_lgt_coupling
  tech_lgt_entity_keyword_mapping -.->|Qualifies| tech_lgt_distribution_copies
  tech_lgt_entity_keyword_mapping -.->|Qualifies| tech_lgt_huffman_patient
  tech_lgt_entity_keyword_mapping -.->|Qualifies| tech_lgt_interval_coding
  tech_lgt_entity_keyword_mapping -.->|Qualifies| tech_lgt_interval_keyed_randomness
  tech_lgt_feedback_coding ==>|Depends-on| tech_ft_information_theoretic
  tech_lgt_feedback_coding -.->|Qualifies| tech_lgt_coupling
  tech_lgt_feedback_coding -.->|Qualifies| tech_lgt_interval_coding
  tech_lgt_feedback_coding -.->|Qualifies| tech_lgt_interval_keyed_randomness
  tech_lgt_feedback_coding -->|Refines| tech_lgt_watermark_pseudorandom
  tech_lgt_grouping ==>|Depends-on| fam_foundations_theory
  tech_lgt_interval_adaptive_truncation ==>|Depends-on| tech_lgt_huffman_patient
  tech_lgt_interval_adaptive_truncation -->|Refines| tech_lgt_interval_coding
  tech_lgt_interval_keyed_randomness ==>|Depends-on| tech_lgt_interval_coding
  tech_lgt_interval_keyed_randomness -->|Refines| tech_ft_rejection_sampling
  tech_lgt_interval_keyed_randomness --x|Supersedes| tech_lgt_huffman_patient
  tech_lgt_interval_keyed_randomness --x|Supersedes| tech_lgt_interval_coding
  tech_lgt_reasoning_strategy_choice -.->|Qualifies| tech_sa_active_warden
  tech_mac_emergent_codes -->|Refines| tech_lce_eval_frameworks
  tech_mac_risk_taxonomies <-->|Restates| tech_mac_covertext_codebooks
  tech_mac_schelling_prompted -->|Refines| tech_sa_active_warden
  tech_mac_schelling_prompted -->|Supports| tech_lce_stateless_subversion
  tech_nsf_engine_benchmark_assessment <-->|Restates ×2| tech_nsf_intrinsic_rating
  tech_nsf_hyperbolic_embeddings ==>|Depends-on| tech_nsf_hyperbolic_networks
  tech_nsf_hyperbolic_networks ==>|Depends-on ×2| tech_nsf_hyperbolic_embeddings
  tech_sa_activation_probes -->|Refines| tech_lce_control_evaluations
  tech_sa_likelihood_ratio_forensics ==>|Depends-on| tech_nsf_intrinsic_rating
  tech_sa_llm_classifiers -.->|Qualifies| tech_lgt_distribution_copies
  tech_sa_llm_classifiers -.->|Qualifies| tech_lgt_grouping
  tech_sa_llm_classifiers -.->|Qualifies| tech_lgt_interval_coding
  tech_sa_utility_gap -.->|Qualifies| tech_ft_complexity_theoretic
  tech_sa_utility_gap -->|Refines| tech_ft_information_theoretic
  linkStyle 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96 stroke:#9e9e9e,stroke-width:1px
  linkStyle 97,102,112,114,115,120,122,123,128,133,141,146,147,149,159,160,162 stroke:#6a1b9a,stroke-width:2.5px,color:#6a1b9a
  linkStyle 98,117,118,155,158 stroke:#00838f,stroke-width:2.5px,color:#00838f
  linkStyle 99,129,130,131,132,151,152 stroke:#4e342e,stroke-width:2.5px,color:#4e342e
  linkStyle 100,101,105,106,107,110,111,121,127,145,148,150,154,156,161,167 stroke:#1565c0,stroke-width:2.5px,color:#1565c0
  linkStyle 103,104,109,113,116,124,125,126,134,136,137,138,139,140,142,143,144,153,163,164,165,166 stroke:#ef6c00,stroke-width:2.5px,color:#ef6c00
  linkStyle 108,157 stroke:#2e7d32,stroke-width:2.5px,color:#2e7d32
  linkStyle 119,135 stroke:#c62828,stroke-width:2.5px,color:#c62828
  classDef nonlanding fill:#eeeeee,stroke:#bdbdbd,stroke-dasharray:2 2,color:#9e9e9e
  class tech_ft_capacity_laws,tech_ft_complexity_theoretic,tech_ft_informal_limits,tech_ft_information_theoretic,tech_ft_security_models,tech_lce_agentic_construction,tech_lce_control_evaluations,tech_lce_coordination_evals,tech_lce_encoded_reasoning,tech_lce_eval_frameworks,tech_lce_message_passing,tech_lce_prompted_elicitation,tech_lce_rl_learned_codes,tech_lce_scheme_discovery,tech_lce_stateless_subversion,tech_lce_taught_schemes,tech_lce_trained_elicitation,tech_mac_collusion_audits,tech_mac_collusion_benchmarks,tech_mac_emergent_codes,tech_mac_focality_prompts,tech_mac_input_triggers,tech_mac_learned_tacit,tech_mac_risk_taxonomies,tech_mac_schelling_prompted,tech_mac_tacit_coordination,tech_mac_zero_shot_conventions,tech_nsf_chess_language,tech_nsf_chess_language_models,tech_nsf_commentary_evaluation,tech_nsf_commentary_generation,tech_nsf_engine_and_opening_analysis,tech_nsf_engine_benchmark_assessment,tech_nsf_human_move_models,tech_nsf_hyperbolic_embeddings,tech_nsf_hyperbolic_networks,tech_nsf_intrinsic_rating,tech_nsf_llm_chess_play,tech_nsf_neural_human_move,tech_sa_activation_probes,tech_sa_active_warden,tech_sa_concept_lens,tech_sa_game_record_inference,tech_sa_game_statistics,tech_sa_internal_states,tech_sa_likelihood_ratio_forensics,tech_sa_llm_classifiers,tech_sa_prompted_llm_monitors,tech_sa_statistical_features,tech_sa_text_features,tech_sa_utility_gap nonlanding
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

## Families

| family | techniques | approaches | file |
| --- | --- | --- | --- |
| audio | 1 | 2 | [approach_map_audio.md](approach_map_audio.md) |
| foundations-theory | 15 | 20 | [approach_map_foundations_theory.md](approach_map_foundations_theory.md) |
| game-and-chess | 13 | 13 | [approach_map_game_and_chess.md](approach_map_game_and_chess.md) |
| hyperbolic | 1 | 1 | [approach_map_hyperbolic.md](approach_map_hyperbolic.md) |
| image-classical | 2 | 1 | [approach_map_image_classical.md](approach_map_image_classical.md) |
| image-deep | 5 | 8 | [approach_map_image_deep.md](approach_map_image_deep.md) |
| image-generative-coverless | 11 | 17 | [approach_map_image_generative_coverless.md](approach_map_image_generative_coverless.md) |
| linguistic-text | 1 | 3 | [approach_map_linguistic_text.md](approach_map_linguistic_text.md) |
| llm-capability-eval | 15 | 17 | [approach_map_llm_capability_eval.md](approach_map_llm_capability_eval.md) |
| llm-generative-text | 32 | 38 | [approach_map_llm_generative_text.md](approach_map_llm_generative_text.md) |
| multi-agent-collusion | 18 | 22 | [approach_map_multi_agent_collusion.md](approach_map_multi_agent_collusion.md) |
| non-steganography-foundation | 12 | 35 | [approach_map_non_steganography_foundation.md](approach_map_non_steganography_foundation.md) |
| steganalysis | 12 | 13 | [approach_map_steganalysis.md](approach_map_steganalysis.md) |
| watermarking | 4 | 5 | [approach_map_watermarking.md](approach_map_watermarking.md) |

## Approaches

| address | name | family | technique | channel | key | access | capacity | mechanism | landable | mechanism_evidence | carrier | acquisition |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `agarwal_2023:approach-hypersteg` | HyperSteg, an autoencoder that blends message and carrier features on the Poincaré ball, built on hyperbolic neural networks | hyperbolic | hy-hyperbolic-hiding | latent-generative | — | training | — | m-hyperbolic-blending | yes | sibling:hypersteg-poincare-beta-concatenation | image or audio carrier features | weight-trained |
| `aharon_2026:approach-focal-point-evaluation` | a large-scale study of focal points in LLMs, comparing tacit coordination with humans across cooperative and competitive games, and testing learning-free prompts that improve it | multi-agent-collusion | — | other (none: coordination without communication) | none | prompt | — | m-coordination-eval | no | own | — | — |
| `aharon_2026:surveyed-all-features-prompt` | the "all-features" prompt: reason over Kraus et al.'s focality principles (little effect) | multi-agent-collusion | mac-focality-prompts | other (none: tacit coordination) | none | prompt | — | m-focality-prompt | no | own | — | — |
| `aharon_2026:surveyed-culture-prompt` | the "culture" prompt: choose the option most culturally relevant to humans (lifts heterogeneous models to human level where culture is part of focality) | multi-agent-collusion | mac-focality-prompts | other (none: tacit coordination) | none | prompt | — | m-focality-prompt | no | own | — | — |
| `aharon_2026:surveyed-saliency-prompt` | the "saliency" prompt: choose the option most salient to humans (little effect) | multi-agent-collusion | mac-focality-prompts | other (none: tacit coordination) | none | prompt | — | m-focality-prompt | no | own | — | — |
| `anderson_1998:approach-limits-of-steganography` | a survey of what steganography can and cannot do, the obstacles to a Shannon-style theory, and the practical ideas that theory yields | foundations-theory | ft-informal-limits | other (general model: key-selected subset of redundant bits) | shared-key | — | upper bound: gap between lossy and lossless compression; safe rate may tend to zero as the warden sees more stegotext | m-informal-limits | no | own | — | — |
| `anderson_1998:approach-parity-embedding` | parity embedding: the selection channel argument leads to hiding each bit in the parity of a key-selected set of cover bits rather than in the data directly | foundations-theory | ft-keyed-parity | pixel-spatial | shared-key | — | — | m-keyed-parity | yes | own | parity of key-selected cover elements (e.g. image pixels) | specified |
| `anderson_1998:approach-public-key-steganography` | public-key steganography: encrypt under the recipient's public key and embed as block parities; every recipient tries to decrypt, and against an active warden a one-time key permutes the cover bits | foundations-theory | ft-public-key-steganography; ft-keyed-parity | other (parity of successive cover blocks) | none | — | — | m-public-key-block-parity | yes | own | parity of successive cover blocks | specified |
| `anderson_1998:selection-channel-book-cipher` | Selection channel — the shared pad that chooses which cover bits carry the message; the book cipher as a shared-codebook example | foundations-theory | — | — | codebook | — | lower for a repetitive book, since correlation attacks from the context limit the share of words usable | m-pointer-code | yes | own | pointers to words of a shared book | specified |
| `anwar_2026:approach-steganographic-gap` | a decision-theoretic view of steganography, detected and quantified by the steganographic gap over generalised V-information | steganalysis | sa-utility-gap | other (detection from downstream actions) | — | prompt | — | m-utility-gap | no | own | — | — |
| `anwar_2026:surveyed-codeword-codebook` | codeword schemes for coin-flip reasoning (Sun/Moon, and a larger codebook) | llm-capability-eval | lce-codeword-substitution | lexical | codebook | prompt | one binary state per codeword | m-codeword-substitution | yes | own | words in a reasoning trace | prompted |
| `anwar_2026:surveyed-rot13-partial-encoding` | word-level Rot13 encoding applied with probability p, as a graded steganography simulation | llm-capability-eval | lce-partial-encoding | lexical | codebook | prompt | — | m-partial-word-cipher | yes | own | words in a reasoning trace | specified |
| `bai_2024:approach-semantic-steganography` | semantic steganography: secret bits select a class in a semantic space built from ontology-entity trees, and an LLM writes a sentence of that class | llm-generative-text | lgt-entity-keyword-mapping | topic-semantic | shared-key | prompt | follows entity-distribution entropy; about 28 bit/sentence versus about 2.5 for AC on ChatGLM2-6B | m-entity-tree-class | yes | own | topic of generated sentences (entity class) | specified |
| `bai_2024b:approach-generative-llm-steganalysis` | generation-based linguistic steganalysis: an LLM fine-tuned with LoRA writes its verdict on a text as readable output, with no added classifier module | steganalysis | sa-llm-classifiers | other (detector of distributional-sampling stegos) | — | training | — | m-llm-classifier | no | own | — | — |
| `barai_2026:approach-pgn-mixed-radix` | encrypt, then write the ciphertext as a legal chess game: AES-256-GCM output, read as a large integer, is mapped deterministically to a sequence of legal moves in PGN, with variation trees for longer messages | game-and-chess | gc-mixed-radix | move choice | shared-key | — | about 4.3 bits per ply; about 430 bits per 100-move game | m-mixed-radix-index | yes | sibling:mixed-radix-legal-move-index | choice among all legal moves (PGN) | specified |
| `biswas_2015:approach-3p-framework` | a framework that separates Performance from Prediction and quantifies Profiling, for methods that judge the intrinsic merit of moves | non-steganography-foundation | nsf-engine-benchmark-assessment | move choice | — | — | — | m-human-move-models | no | own | — | — |
| `biswas_2015:surveyed-average-difference` | average difference (AD) and its scaled form (ASD): centipawns lost against the engine, scaled by the size of the advantage after Regan's finding | non-steganography-foundation | nsf-engine-benchmark-assessment | move choice | — | — | — | m-engine-benchmark-assessment | no | own | — | — |
| `biswas_2015:surveyed-move-matching` | move matching (MM) and equal-value matching (EV): agreement with the engine's choice; a cheater can lower the match rate cheaply | non-steganography-foundation | nsf-engine-benchmark-assessment | move choice | — | — | — | m-engine-benchmark-assessment | no | own | — | — |
| `biswas_2015:surveyed-skilloscopy` | Skilloscopy (SK): Bayesian updating of belief over benchmark players of defined competence, move by move | non-steganography-foundation | nsf-engine-benchmark-assessment | move choice | — | — | — | m-engine-benchmark-assessment | no | own | — | — |
| `biswas_2015:surveyed-sr-all-depths` | SR over all search depths (SRA): a move that ranks top early in the search is likelier to be played | non-steganography-foundation | nsf-engine-benchmark-assessment | move choice | — | — | — | m-engine-benchmark-assessment; m-intrinsic-rating | no | own;own | — | — |
| `biswas_2015:surveyed-statistical-regression` | statistical regression (SR): fit the stochastic benchmark player whose competence best explains the moves; frequentist, with z-scores | non-steganography-foundation | nsf-engine-benchmark-assessment | move choice | — | — | — | m-intrinsic-rating | no | own | — | — |
| `blasius_2009:approach-opening-fragmentation-model` | a measured opening-popularity law and its generating model: opening frequencies are power-law with depth-dependent exponent, pooled weights obey Zipf's law, and a random multiplicative fragmentation of the game tree with arcsine branching ratios reproduces both | non-steganography-foundation | nsf-engine-and-opening-analysis | other (not a hiding channel; opening-popularity statistics) | — | — | — | m-opening-and-engine-analysis | no | own | — | — |
| `boonstra_2024:approach-bayesian-hidden-code-forensics` | a Bayesian forensic framework for alleged hidden codes in sport: weigh the likelihood of the observed events under a named code against their likelihood under no code | steganalysis | sa-likelihood-ratio-forensics | other (detector of pre-agreed side-channel codes) | none | — | — | m-likelihood-ratio-forensics | no | sibling:likelihood-ratio-detector | — | — |
| `boonstra_2024:surveyed-card-orientation-code-c` | code C (bridge): lead-card orientation signals whether a top honour is held, and the opposing declarer is unaware of the signal | game-and-chess | gc-side-signals | other (physical card orientation) | codebook | — | one bit per lead | m-orientation-signal | yes | own | orientation of the lead card | negotiated |
| `boonstra_2024:surveyed-trash-can-code-b` | code B (baseball): a trash-can bang relays a stolen catcher's sign for any non-fastball, silence for a fastball | game-and-chess | gc-side-signals | other (acoustic signal) | codebook | — | one bit per pitch | m-acoustic-signal | yes | own | trash-can bangs | negotiated |
| `buscemi_2026:approach-numeric-covert-games` | numeric covert communication in canonical games, where agents exchange ten numbers a round with no given code | multi-agent-collusion | mac-emergent-codes | numeric-annotation | none | prompt | ten numbers per round | m-emergent-convention; m-payoff-anchored-symbols | yes | own;sibling:payoff-anchored-decimal-code | ten-number messages each round | focal;negotiated |
| `cachin_1998:approach-balanced-partition` | the balanced-partition stegosystem: split the covertext alphabet into two parts of near-equal probability and let a one-bit shared key choose which part carries each message bit | foundations-theory | ft-balanced-partition | distributional-sampling | shared-key | — | one bit per covertext | m-balanced-partition | yes | own | choice of covertext from a near-equiprobable half | specified |
| `cachin_1998:approach-information-theoretic-model` | an information-theoretic model of steganography against a passive adversary, with security measured as relative entropy between cover and stego distributions | foundations-theory | ft-information-theoretic | other (model, any channel) | shared-key | — | — | m-information-theoretic-security | no | own | — | — |
| `cachin_1998:approach-universal-repetition-times` | the universal stegosystem: Willems' repetition-times compressor, modified to swap a low-probability block for its neighbour in the repetition-time ranking, so no covertext statistics are needed | foundations-theory | ft-universal-compression | other (swap of low-probability block with its rank neighbour) | shared-key | — | — | m-repetition-rank-exchange | yes | own | source blocks of a repetition-times compressor | specified |
| `cachin_2004:approach-balanced-partition` | the balanced-partition stegosystem for arbitrary known distributions: a one-bit key chooses which of two near-equiprobable halves of the covertext space carries the bit | foundations-theory | ft-balanced-partition | distributional-sampling | shared-key | — | one bit per covertext | m-balanced-partition | yes | own | choice of covertext from a near-equiprobable half | specified |
| `cachin_2004:approach-information-theoretic-model` | an information-theoretic model of steganography against a passive adversary; detection is hypothesis testing and a stegosystem is perfect when cover and stego distributions have zero relative entropy | foundations-theory | ft-information-theoretic | other (model, any channel) | shared-key | — | — | m-information-theoretic-security | no | own | — | — |
| `cachin_2004:approach-uniform-cover-schemes` | perfectly secure stegosystems for uniform covertext: a key-shifted Bible-verse reference, and the one-time pad on uniformly random bits | foundations-theory | ft-uniform-cover | other (key-shifted choice of a reference into a shared book) | shared-key | — | — | m-uniform-reference | yes | own | reference to an equally likely item (a Bible verse) | specified |
| `cachin_2004:approach-universal-stegosystem` | the universal stegosystem: approximate the covertext distribution by universal compression, then generate stegotext from private randomness with the message one-time-padded into the encoder output | foundations-theory | ft-universal-compression | distributional-sampling | shared-key | — | message of up to n H(X) bits | m-universal-estimate-and-sample | yes | own | covertext sampled from an estimated distribution | specified |
| `cetin_2022:approach-hyperbolic-rl-srym` | deep RL agents whose latent state representations live in hyperbolic space, stabilised by S-RYM | non-steganography-foundation | nsf-hyperbolic-networks | — | — | training | — | m-hyperbolic-networks | no | own | — | — |
| `chang_2024:approach-action-steganography` | action steganography: several reinforcement-learning agents each stand for one message symbol, and the receiver decodes by identifying which agent produced the observed episode | game-and-chess | gc-learned-action-policies | move choice | shared-key | training | one bit per trajectory (two agents) | m-policy-identity | yes | own | agent episodes (trajectories in a labyrinth) | rl-trained |
| `chen_2021:approach-poincare-probe` | a Poincaré probe that projects BERT embeddings into a Poincaré subspace with explicit hierarchies | non-steganography-foundation | nsf-hyperbolic-embeddings | — | — | weights, training | — | m-hyperbolic-embeddings | no | own | — | — |
| `chen_2023:approach-wavmark` | WavMark, an invertible-network audio watermark of 32 bits per 1-second segment, with encoder and decoder sharing parameters | watermarking | wm-learned-post-hoc | transform-domain | shared-model | training | 32 bits per 1-second segment (32 bps); 10 of 32 bits spent on pattern bits for locating | m-invertible-encoder | yes | own | audio waveform (1-second segments) | weight-trained |
| `dai_2019:approach-patient-huffman` | patient-Huffman, per-step Huffman coding of the LM distribution that encodes only at steps where the Huffman distribution is close enough to the LM's | llm-generative-text | lgt-huffman-patient | distributional-sampling | shared-key | logits | — | m-huffman-patient | yes | own | token sampling in generated text | specified |
| `dai_2019:surveyed-bins` | Bins (Fang et al. 2017), a shared random partition of the vocabulary into equal bins, the bin carrying a block of ciphertext | llm-generative-text | lgt-bins | lexical | shared-key | logits | — | m-fixed-bins | yes | own | token choice in generated text | specified |
| `dai_2019:surveyed-vlc-huffman` | VLC (Yang et al. 2018), a Huffman code over the vocabulary rebuilt at each step, walked by the ciphertext bits | llm-generative-text | lgt-huffman | distributional-sampling | shared-model | logits | — | m-huffman-every-step | yes | own | token sampling in generated text | specified |
| `desoky_2009:approach-chestega` | Chestega: encode the message as chess data (positions, pieces, moves, tournaments, players) inside a chess-related document, preferably authentic games or tool-generated analysis, with a public method and an agreed configuration instead of a key | game-and-chess | gc-chess-data-codebook | other (chess-data content: target squares, pieces, players' initials, via an agreed codebook) | codebook | — | example: 7 bits per move as a target-square index; 4-bit slices as letters via player initials | m-reference-code; m-authentic-record-selection; m-letter-position | yes | partial;sibling:target-square-index;sibling:player-initial-codebook | chess data (squares, pieces, players) in chess-related text | specified |
| `ding_2023:approach-discop` | Discop, sampling from one of several rotated "distribution copies" chosen by the message, so the model's distribution is kept exactly; with KL measured against Meteor and ADG | llm-generative-text | lgt-distribution-copies | distributional-sampling | shared-key | logits | 3.48 to 5.76 bits per token, about 0.92 to 0.95 of the entropy limit | m-distribution-copies | yes | own | token sampling (also image and speech generation) | specified |
| `feng_2023:approach-chess-language-benchmark` | a chess game-and-language dataset with an evaluation framework, as a benchmark for policy and language together | non-steganography-foundation | nsf-chess-language-models | other (not a hiding channel; dataset and benchmark) | — | — | — | m-chess-language-models | no | own | — | — |
| `feng_2023:approach-chessclip` | ChessCLIP, contrastive training on board-history/move and annotation pairs to align policy and language | non-steganography-foundation | nsf-chess-language-models | other (not a hiding channel; policy-language alignment) | — | training | — | m-chess-language-models | no | own | — | — |
| `feng_2023:approach-chessgpt` | ChessGPT, a GPT-like model trained by causal language modelling on all the chess game and language data | non-steganography-foundation | nsf-chess-language-models | other (not a hiding channel; chess language model) | — | training | — | m-chess-language-models | no | own | — | — |
| `fernandez_2023:approach-stable-signature` | Method — fine-tune the latent decoder of an LDM so that every generated image carries a binary signature | watermarking | wm-decoder-finetune | latent-generative | shared-key | training | 48-bit signature | m-decoder-finetune-mark | yes | own | images from a latent diffusion model | weight-trained |
| `ganea_2018:approach-hyperbolic-neural-networks` | generalise MLR, feed-forward and recurrent (GRU) networks to the Poincaré ball via gyrovector spaces | non-steganography-foundation | nsf-hyperbolic-networks | — | — | training | — | m-hyperbolic-networks | no | own | — | — |
| `greenblatt_2023:approach-action-collusion-code-signal` | action collusion, a one-bit signal written into the code (variable name or while loop) | multi-agent-collusion | mac-output-signals | structural-format | codebook | prompt | one bit per solution | m-output-signal | yes | own | a feature of the submitted code (variable name, loop form) | prompted |
| `greenblatt_2023:approach-control-evaluation` | control evaluations, in which a red team's attack policy stands in for the untrusted model | llm-capability-eval | lce-control-evaluations | — | — | prompt | — | m-control-evaluation | no | own | — | — |
| `greenblatt_2023:approach-input-collusion` | input collusion on a shared feature of the problem, a focal point needing no message | multi-agent-collusion | mac-input-triggers | other (shared input feature, focal point) | codebook | prompt | no message sent; a shared trigger | m-input-trigger | no | own | a feature of the problem statement (no message sent) | prompted |
| `greenblatt_2023:approach-untrusted-monitoring-signal-jamming` | untrusted monitoring guarded by signal jamming | steganalysis | sa-active-warden; sa-prompted-llm-monitors | other (active-warden redaction and paraphrase) | — | prompt | — | m-prompted-llm-monitor; m-active-warden | no | own;own | — | — |
| `guo_2026:approach-bam-feedback-coding` | BAM (Burnashev Adaptive Posterior Matching): black-box LLM steganography recast as communication over a channel with causal, noiseless feedback, coded by posterior matching with a decode-and-confirm phase | llm-generative-text | lgt-feedback-coding | distributional-sampling | shared-key | sender: logits; receiver: no model access | 8-bit payload in under 50 tokens at most 0.1% message error; chess moves average 5.0 coded bits | m-feedback-coding; m-coupling | yes | own;sibling:ot-coupling-sampler | token sampling in agent conversation | specified |
| `hahn_2015:approach-castle` | Castle: a censorship-circumvention covert channel that encodes data as real-time-strategy player actions, executed by desktop automation and carried by the game's own network protocol, adaptable across games of one genre | game-and-chess | gc-action-commands | other (player action commands: k-of-n unit selection and target map location) | — | — | 50 to 200 B/s generally; about 190 B/s on 0 A.D.; over 400 B/s with tuning | m-combinatorial-subset-index | yes | partial | unit selections and commands in a real-time strategy game | specified |
| `hammond_2025:approach-multi-agent-risk-taxonomy` | a taxonomy of multi-agent risks: three failure modes and seven risk factors | multi-agent-collusion | mac-risk-taxonomies | — | — | — | — | m-risk-taxonomy | no | own | — | — |
| `hammond_2025:surveyed-algorithmic-pricing-collusion` | tacit algorithmic pricing collusion, as in the German retail gasoline market | multi-agent-collusion | mac-learned-tacit | other (price signals, tacit) | none | — | — | m-learned-tacit-collusion | no | own | market prices | — |
| `hammond_2025:surveyed-compression-emergent-communication` | secret communication by text compression or by emergent symbols without predefined meaning | multi-agent-collusion | mac-emergent-codes | other (compression or emergent code) | — | — | — | m-emergent-convention | no | own | agent messages | negotiated |
| `hammond_2025:surveyed-llm-covertext-steganography` | covertext steganography between LLMs, reported from Motwani et al. (2024) | multi-agent-collusion | mac-covertext-codebooks | lexical | codebook | prompt | — | m-substitution | yes | own | word choice and phrasing in text | prompted |
| `he_2024:approach-hierarchy-transformer` | re-train transformer encoders as Hierarchy Transformer encoders (HiTs) in a Poincaré ball with curvature set by dimension | non-steganography-foundation | nsf-hyperbolic-embeddings | — | — | weights, training | — | m-hyperbolic-embeddings | no | own | — | — |
| `hernandezcastro_2006:approach-comment-codebook` | comment codebook: a set of annotations that say the same thing (eight here, so three bits), open to any text-steganography technique, easy to strip | game-and-chess | gc-comment-codebook | lexical | codebook | — | three bits per comment from a set of eight | m-phrase-codebook | yes | own | annotation comments in a game record | specified |
| `hernandezcastro_2006:approach-game-steganalysis` | statistical attacks on game length, playing level and result, and stripping variations and comments; countered by encryption, raised komi and both sides embedding | steganalysis | sa-game-statistics | move choice | none | — | — | m-game-statistics; m-active-warden | no | own;own | — | — |
| `hernandezcastro_2006:approach-ranked-move-choice` | ranked move choice while playing a new game: both parties run the same engine with a shared key, list the moves scoring above a threshold T, sort them by evaluation and play the i-th to send i | game-and-chess | gc-ranked-moves | move choice | shared-key | — | about log2 of the number of good moves per position; three bits per move in StegoGo | m-engine-ranked-index | yes | own | choice among engine-ranked moves | specified |
| `hernandezcastro_2006:approach-variation-carrier` | variations inserted into an already played game: each variant encodes bits by where it starts, how long it runs and, move by move, the ranked-choice rule | game-and-chess | gc-variation-insertion | structural-format | shared-key | — | — | m-insertion-parameters; m-engine-ranked-index | yes | own;own | variations inserted into a played game record | specified |
| `hopper_2002:approach-complexity-theoretic-steganography` | complexity-theoretic steganography: secrecy and robustness defined by computational indistinguishability, with secure protocols built from one-way functions; positioned against Simmons' problem and the information-theoretic models | foundations-theory | ft-complexity-theoretic | other (any channel) | shared-key | — | one hidden bit per channel block | m-complexity-theoretic-security | no | own | — | — |
| `hopper_2002:approach-robust-text-shingling` | Construction 4, robust protocol for text-like channels: a keyed PRF picks the maximising n-shingle of each document and an unbiased function of it carries the bit, surviving edits that preserve shingle overlap | foundations-theory | ft-keyed-feature-function | other (keyed function of the maximising n-shingle of a document) | shared-key | — | — | m-robust-feature-function | yes | partial | choice of document, read through its maximising shingle | specified |
| `hopper_2002:approach-stateful-rejection-sampling` | Construction 1, stateful rejection sampling: for each encoded bit, draw up to two channel blocks until a keyed PRF of block and counter equals the bit; taken from Anderson and Petitcolas | foundations-theory | ft-rejection-sampling | distributional-sampling | shared-key | — | one bit per block; some failure probability per bit, absorbed by an error-correcting code | m-rejection-keyed-stateful | yes | own | choice among channel samples | specified |
| `hopper_2002:approach-stateless-unbiased-function` | Construction 2, stateless: encrypt with an IND$-CPA cipher, then rejection-sample each block until a public function unbiased on the channel yields the next ciphertext bit; Cachin gave an information-theoretic version | foundations-theory | ft-rejection-sampling | distributional-sampling | shared-key | — | — | m-rejection-public-unbiased | yes | own | choice among channel samples | specified |
| `hopper_2002:approach-universally-robust` | Construction 3, universally robust: channel draws from shared pseudorandom inputs stand in for two shared secret blocks, each bit repeated n times, robust against any bounded warden but impractical | foundations-theory | ft-shared-sample-robust-code | distributional-sampling | shared-key | — | — | m-shared-sample-robust | yes | own | channel draws from shared pseudorandom inputs | specified |
| `hopper_2002:timestamped-channel` | Channel — a distribution on timestamped bit sequences, general enough to include timing-only channels | foundations-theory | — | — | — | — | — | m-timing | yes | partial | timing of emails | unknown |
| `hu_2018:approach-dcgan-swe` | Method — map secret bits into the noise vector of a trained DCGAN generator; no embedding | image-generative-coverless | igc-latent-mapping | latent-generative | shared-model | training | σ bits per noise value, 3×\|z\| bits per image; 9.16e-3 bytes/pixel; recovery accuracy about 0.89–0.96, not 100% | m-latent-mapping | yes | own | generated images (generator noise vector) | weight-trained |
| `hu_2020:approach-other-play` | other-play, self-play against symmetry-relabelled copies of the partner, so that no agent can rely on an arbitrary way of breaking symmetry | multi-agent-collusion | mac-zero-shot-conventions | other (convention formation in cooperative play: hints and actions) | none | training | — | m-coordination-learning | no | own | — | — |
| `jarviniemi_2025:approach-meta-model-focal-collusion` | meta-models that independently design policy and monitor prompts, set in Greenblatt et al.'s untrusted monitoring | multi-agent-collusion | mac-schelling-prompted | numeric-annotation | none | prompt | one bit (collude or not) | m-schelling-choice; m-focal-magic-number | yes | sibling:schelling-no-key;sibling:coding-magic-numbers | features of Python code (comments stripped) | focal |
| `jhamtani_2018:approach-gac` | GAC, an end-to-end neural generator that selects salient board features and decodes commentary with an LSTM | non-steganography-foundation | nsf-commentary-generation | other (not a hiding channel; commentary generator and corpus) | — | training | — | m-commentary-generation | no | own | — | — |
| `kaptchuk_2021:approach-meteor` | Meteor: a symmetric-key, stateful, provably secure scheme that embeds message bits in the sampling randomness of a generative model, at a rate that follows the instantaneous entropy | llm-generative-text | lgt-interval-keyed-randomness | distributional-sampling | shared-key | logits | throughput proportional to channel entropy; bits per token depend strongly on the model | m-interval-keyed-randomness | yes | sibling:fresh-prg-mask | token sampling in generated text | specified |
| `karpov_2025:approach-colours-rl` | the colours experiment, an RL-learnt unkeyed mapping without step-by-step reasoning | llm-capability-eval | lce-rl-learned-codes | lexical | none | training | — | m-codeword-substitution | yes | partial | proper names in short generated text | rl-trained |
| `karpov_2025:approach-indirect-guess-game` | the indirect guess game, in which an assistant may hide letters to help one team past an overseer | llm-capability-eval | lce-message-passing | other (model-chosen) | none | prompt | — | m-message-passing-task | no | own | — | — |
| `karpov_2025:approach-prompted-stego-eval` | prompted evaluation of frontier models in direct, instructed, coordinated and game scenarios | llm-capability-eval | lce-message-passing | lexical | — | prompt | — | m-message-passing-task | no | own | — | — |
| `karpov_2025:approach-rloo-summary-stego` | RLOO fine-tuning of sender and receiver to carry a payload in a news summary under an overseer | multi-agent-collusion | mac-gradient-rl | topic-semantic | none | training | about 3 bits of entropy; ~20% gain in undetected accuracy | m-associated-term-substitution | yes | sibling:capacity-semantic-association | wording of a news summary | rl-trained |
| `karpov_2025:synonym-scheme-given` | Prompted schemes — synonym-substitution algorithm given to encoder and decoder, not the overseer | llm-capability-eval | — | — | — | — | — | m-synonym-substitution | yes | partial | synonym choice in covertext | prompted |
| `ker_2007:approach-batch-square-root-capacity` | the batch capacity theorem: across many covers, secure capacity grows only as the square root of their number, proved under the shift hypothesis with a security definition taken from Cachin | foundations-theory | ft-capacity-laws | other (any; capacity theorem) | — | — | secure capacity proportional to the square root of the number of covers | m-capacity-laws | no | own | — | — |
| `ker_2008:approach-square-root-law` | the square root law for a single cover: the batch capacity results are carried over to one object treated as a batch of near-independent regions, then tested on spatial and DCT-domain embedding | foundations-theory | ft-capacity-laws | other (pixel-spatial and transform-domain experiments) | — | — | secure capacity grows as the square root of cover size, counted in embedding changes | m-capacity-laws | no | own | — | — |
| `kim_2024:approach-ccc` | CCC, concept vectors from a chess expert model, prioritised by the move, handed to an LLM that writes the comment | non-steganography-foundation | nsf-commentary-generation | other (not a hiding channel; LLM commentary generator) | — | prompt | — | m-commentary-generation | no | own | — | — |
| `kim_2024:approach-gcc-eval` | GCC-Eval, G-Eval extended with expert-engine input to score chess commentary on four dimensions | non-steganography-foundation | nsf-commentary-evaluation | other (not a hiding channel; LLM-based commentary evaluator) | — | prompt | — | m-commentary-evaluation | no | own | — | — |
| `kolasani_2025:approach-llm-chess-benchmark` | LLM Chess: an agentic benchmark in which models play whole games through tool calls, ranked against a random opponent and, for the strongest, given an Elo against a configurable engine | non-steganography-foundation | nsf-llm-chess-play | — | — | — | — | m-llm-chess-play | no | own | — | — |
| `kreuk_2019:approach-hide-and-speak` | speech-in-speech steganography by an image-style encoder–decoder network with differentiable STFT and inverse-STFT layers | audio | au-deep-speech-hiding | transform-domain | shared-model | training | one to five speech messages in one speech carrier of unchanged dimension; quality falls as the count rises | m-spectral-audio-hiding | yes | own | speech audio (STFT magnitudes) | weight-trained |
| `maia2_2024:approach-maia2` | Maia-2, one model that fuses encoded skill levels and positions by skill-aware attention, built on Maia | non-steganography-foundation | nsf-neural-human-move | other (not a hiding channel; skill-conditioned model of human move choice) | — | training | — | m-neural-human-move | no | own | — | — |
| `mallen_2024:approach-subversion-strategy-eval` | Subversion Strategy Eval, eight environments and six affordance sets for stateless protocol subversion | llm-capability-eval | lce-stateless-subversion | other (acausal coordination on a shared trigger or signal phrase) | none | prompt | — | m-stateless-subversion-eval | no | own | — | — |
| `mallen_2024:subversion-untrusted-monitoring-output-collusion` | Untrusted-monitoring environment — one model plays generator and monitor; an output-collusion signal phrase is an optimal strategy | llm-capability-eval | — | — | — | — | — | m-output-signal | yes | own | a fixed comment string in submitted code | specified |
| `mathew_2024:approach-gbrl` | gradient-based reinforcement learning (GBRL) of a sender and receiver against an overseer | multi-agent-collusion | mac-gradient-rl | lexical | shared-model | training | — | m-codeword-substitution; m-codebook | yes | sibling:coding-lexical-stylistic;sibling:coding-lexical-stylistic | word and phrase choice in cover letters | rl-trained |
| `mathew_2024:approach-icrl` | in-context reinforcement learning (ICRL), with centralised and decentralised learners devising strategies in natural language | multi-agent-collusion | mac-in-context-rl | other (strategy chosen by learner; lexical and stylistic) | — | prompt | — | m-phrase-codebook | yes | sibling:coding-lexical-stylistic | phrase choice in cover letters | in-context-optimised |
| `mcilroyyoung_2020:approach-blunder-predictor` | blunder prediction, a residual CNN that labels a move a blunder when it costs 10 points of win probability | non-steganography-foundation | nsf-neural-human-move | other (not a hiding channel; mistake predictor) | — | training | — | m-neural-human-move | no | own | — | — |
| `mcilroyyoung_2020:approach-maia` | Maia, AlphaZero's architecture retrained on human games to predict the next human move, with no tree search | non-steganography-foundation | nsf-neural-human-move | other (not a hiding channel; model of human move choice, a cover distribution or warden model for move-choice channels) | — | training | — | m-neural-human-move | no | own | — | — |
| `molinari_2026:approach-j-pact` | J-PACT, unsupervised pairwise collusion detection from shared J-space concepts | steganalysis | sa-concept-lens | other (relational activation readout) | — | weights | — | m-concept-lens | no | own | — | — |
| `molinari_2026:approach-j-space-steering` | causal steering of steganographic decoding by swapping J-lens concept coordinates | steganalysis | sa-concept-lens | other (activation intervention) | — | weights | — | m-concept-lens | no | own | — | — |
| `moraldo_2014:approach-markov-range-partition` | Markov-chain text generation with probability-proportional range partitioning: the message, read as a number, picks at each word the outbound state whose subrange contains it, so the generated text keeps close to the chain's own transition probabilities | linguistic-text | lt-markov-generation | distributional-sampling | shared-model | — | encoded text about 6-7 times the data size (about 2 after compression) | m-interval-plain | yes | own | word choice in Markov-generated text | specified |
| `motwani_2024:approach-case-framework` | CASE, a framework for evaluating secret collusion in individual and group LLM settings | llm-capability-eval | lce-eval-frameworks | — | — | prompt | — | m-eval-framework | no | own | — | — |
| `motwani_2024:approach-common-knowledge-covertext` | group covertext steganography, hiding a secret word in common knowledge the overseer lacks | multi-agent-collusion | mac-covertext-codebooks | other (covertext modification against shared common knowledge) | codebook | prompt | one secret word per message | m-codebook | yes | partial | text over a public channel, keyed by shared common knowledge | prompted |
| `motwani_2024:surveyed-first-letter-acrostic` | instructed first-letter (acrostic) covertext scheme | llm-generative-text | lgt-letter-position-codes | lexical | codebook | prompt | one character per word | m-letter-position | yes | own | first letters of words in text | prompted |
| `motwani_2024:surveyed-standard-ciphers` | standard ciphers (Base64, Caesar) as an encoding capability | llm-generative-text | lgt-byte-encodings; lgt-substitution-ciphers | other (cipher encoding, not hidden) | codebook | prompt | — | m-byte-encoding; m-letter-substitution-cipher | yes | own;own | encoded string in text | prompted |
| `murdoch_2004:approach-equivalent-move-channel` | the equivalent-move covert channel: a keyed generator picks which of the outcome-equivalent moves to play, borrowing frequency hopping from low-probability-of-intercept radio, so colluders authenticate one another through the moves alone | game-and-chess | gc-equivalent-moves | move choice | shared-key | — | one bit (authentication) before the result is fixed; low capacity, high reliability | m-equivalent-choice | yes | sibling:equivalent-move-channel | choice among outcome-equivalent moves (Connect-4) | specified |
| `murdoch_2004:approach-league-collusion-strategy` | the league collusion strategy: once authenticated, colluders act on that knowledge so that one designated player wins, which guarantees victory when only one team colludes and the players are strong | multi-agent-collusion | mac-authenticated-throwing | other (strategic losing to authenticated colluders) | shared-key | — | — | m-authenticate-then-act | yes | own | moves in tournament games, then game results | specified |
| `murdoch_2004:bridge-shared-secret-key` | Bridge precedent — legal signalling between partners, encoded in the cards played, with a shared secret acting as a key | game-and-chess | — | move choice | shared-key | — | — | m-keyed-play-convention | yes | own | cards played | unknown |
| `murdoch_2004:move-timing-channel` | Alternative carrier — move timing: easy and higher bandwidth, but unreliable under jitter and removable by fixing move times | game-and-chess | — | — | — | — | relatively high bandwidth | m-move-timing | yes | own | delay before each move | unknown |
| `nakamura_2026:approach-colosseum` | Colosseum: cooperative tasks cast as DCOPs, collusion measured as coalition regret, with a secret channel opened between agents as a controlled probe | multi-agent-collusion | mac-collusion-benchmarks | other (explicit secret channel, as audit probe) | — | — | — | m-collusion-benchmark | no | own | — | — |
| `nickel_2017:approach-poincare-embeddings` | embed symbolic data in an n-dimensional Poincaré ball to capture hierarchy and similarity at once | non-steganography-foundation | nsf-hyperbolic-embeddings | — | — | training | — | m-hyperbolic-embeddings | no | own | — | — |
| `pang_2026:approach-codetta-key-exchange` | Codetta's keyless steganographic key exchange, MLWE ciphertexts carried over honest model samples | llm-generative-text | lgt-public-key-sampling | distributional-sampling | none | sender: logits; receiver: logits of the public draft model | about 80k visible tokens per 128-bit key (640 tokens per key bit) | m-sampled-lattice-key-exchange | yes | own | token sampling in agent messages | specified |
| `pang_2026:approach-codetta-keyed` | Codetta's keyed protocol, high-capacity asymmetric steganography through a public draft model and maximal coupling | llm-generative-text | lgt-coupling-public-draft | distributional-sampling | shared-key | sender: logits; receiver: logits of the public draft model | 0.45-0.57 bits per token (Ministral); 4.1-6.4x draft-free LDPC, 16-94x ARS; below 0.04 on low-entropy CTF text | m-maximal-coupling-public-draft | yes | own | token sampling in agent messages, files or wikis | specified |
| `qin_2019:surveyed-average-pixel-dictionary` | average pixel values of sub-images, with a Chinese-sentence dictionary | image-generative-coverless | igc-hash-mapping | other (cover selection by average-pixel hash with dictionary) | — | — | — | m-cover-selection | yes | own | selected natural images (sub-image average pixels) | specified |
| `qin_2019:surveyed-bow-visual-words` | bag-of-words visual words mapped to text keywords | image-generative-coverless | igc-visual-word-mapping | other (cover selection by visual words) | shared-key | — | — | m-visual-word-mapping | yes | own | selected natural images (visual words) | specified |
| `qin_2019:surveyed-dcgan-noise-vector` | secret mapped to a DCGAN noise vector; the sender holds the generator, the receiver the extractor | image-generative-coverless | igc-latent-mapping | latent-generative | shared-model | training | — | m-latent-mapping | yes | own | generated images (generator noise vector) | weight-trained |
| `qin_2019:surveyed-dct-lda` | DCT DC-coefficient feature sequences within LDA topic classes | image-generative-coverless | igc-hash-mapping | other (cover selection by DCT feature sequence) | — | — | — | m-feature-hash-selection | yes | own | selected natural images (DCT feature sequences) | specified |
| `qin_2019:surveyed-densenet-block-matching` | block matching with DenseNet features and DC-coefficient hashes | image-generative-coverless | igc-patch-retrieval | other (cover selection by block matching) | — | — | — | m-patch-retrieval | yes | own | selected natural images (matching blocks) | specified |
| `qin_2019:surveyed-gif-attributes` | GIF extension attributes classified and mapped to bits | image-generative-coverless | igc-hash-mapping | other (cover selection by GIF extension attributes) | — | — | — | m-file-attribute-mapping | yes | own | selected GIF files (extension attributes) | specified |
| `qin_2019:surveyed-gray-hash-selection` | gray-value hash, inverted index, cover selection | image-generative-coverless | igc-hash-mapping | other (cover selection by image hash) | — | — | 8 bits per image | m-feature-hash-selection | yes | own | selected natural images (grey-value hashes) | specified |
| `qin_2019:surveyed-hog-hash` | HOG-based block hashes, with a shared block position shifted one-time-pad style | image-generative-coverless | igc-hash-mapping | other (cover selection by HOG hash) | shared-key | — | — | m-feature-hash-selection | yes | own | selected natural images (HOG hashes) | specified |
| `qin_2019:surveyed-partial-duplicates` | partial-duplicate images retrieved per patch; patch locations are the shared key | image-generative-coverless | igc-patch-retrieval | other (cover selection by partial-duplicate patch retrieval) | shared-key | — | — | m-patch-retrieval | yes | own | selected natural images (partial duplicates) | specified |
| `qin_2019:surveyed-sift-robust-hash` | SIFT-orientation hash of 18 bits, with side information hidden by LSB | image-generative-coverless | igc-hash-mapping | other (cover selection by SIFT hash, plus LSB side channel) | — | — | 18 bits per image | m-feature-hash-selection | yes | own | selected natural images (SIFT hashes) | specified |
| `qin_2019:surveyed-wgan-model-database` | a WGAN model database turns the secret image into an unrelated-looking image and back | image-generative-coverless | igc-model-database | latent-generative | shared-model | training | — | m-generator-model-database | yes | own | generated images | weight-trained |
| `regan_2011:approach-intrinsic-rating-model` | an intrinsic-rating model of human move choice: engine evaluations of all reasonable moves give each move a probability set by sensitivity s and competence c, fitted to Elo by regression and usable to detect engine assistance | non-steganography-foundation | nsf-intrinsic-rating | other (not a hiding channel; model of human move choice) | — | — | — | m-intrinsic-rating | no | own | — | — |
| `regan_2012:approach-intrinsic-performance-ratings` | a refined Regan–Haworth model applied to whole populations: Intrinsic Performance Ratings from Multi-PV analysis, with their distribution used to test rating stability and drift between rating systems | non-steganography-foundation | nsf-intrinsic-rating | other (not a hiding channel; population-level move-quality distributions) | — | — | — | m-intrinsic-rating | no | own | — | — |
| `rippin_2026:approach-agentic-covert-channel-construction` | an agentic covert-channel construction benchmark, seeded with Zamir (2024) | llm-capability-eval | lce-agentic-construction | distributional-sampling | shared-key | logits | — | m-agentic-construction-eval | no | own | — | — |
| `rippin_2026:approach-tacit-stego-agreement-cci` | tacit steganographic agreement as Schelling coordination, measured by algorithm, hyperparameter and complete coordination indices | multi-agent-collusion | mac-schelling-prompted | other (choice of stegosystem and parameters) | — | prompt | — | m-coordination-eval | no | own | choice of stegosystem, key and parameters | focal |
| `ritchey_2012:approach-combinatorial-game-framework` | a general framework for covert channels in combinatorial games: the sender generates the cover by playing, assigns bit strings to the moves her strategies allow, and plays the move whose string matches the next data; shown on Tic-Tac-Toe, said to carry to Chess and Go | game-and-chess | gc-keyed-strategy-set | move choice | shared-key | — | up to floor(log2 N) bits per move; reduced but non-zero under perfect play | m-keyed-strategy-set-index | yes | sibling:permuted-best-move-index | choice among moves the sender's strategies allow | specified |
| `roger_2023:approach-finetuned-introduction-codebook` | fine-tuning GPT-3.5-Turbo to learn a simple encoding scheme for encoded reasoning | llm-capability-eval | lce-taught-schemes | structural-format | codebook | training | 18 values (one choice among 18 introductions) | m-training-elicitation; m-phrase-codebook | yes | own;sibling:demo-introduction-codebook | introduction sentence of an answer | weight-trained |
| `roger_2023:approach-paraphrase-defence` | a conservative evaluation of paraphrasing as a defence against steganography | steganalysis | sa-active-warden | other (active-warden paraphrase defence) | — | prompt | below about 2 bits per answer (3 bits per KB) survive paraphrasing | m-active-warden | no | own | — | — |
| `roger_2023:surveyed-acronyms` | prompted acronym scheme | llm-generative-text | lgt-literal-payload-names | lexical | — | prompt | 30 bits per answer | m-literal-payload-name | yes | sibling:acronym-literal-payload | an acronym or name in the answer text | prompted |
| `roger_2023:surveyed-age-instructions` | prompted age-instruction scheme | llm-generative-text | lgt-enumerated-openers | numeric-annotation | codebook | prompt | ages in [0,63] | m-stated-value-code | yes | own | a stated number (age) at the start of the answer | prompted |
| `roger_2023:surveyed-balanced-marking` | balanced-marking watermark used for steganography | llm-generative-text | lgt-watermark-token-partition | distributional-sampling | shared-key | logits | — | m-token-partition-watermark | yes | own | token sampling in generated text | specified |
| `roger_2023:surveyed-cycle-shifting-watermark` | cycle-shifting watermark used for steganography | llm-generative-text | lgt-watermark-token-partition | distributional-sampling | shared-key | logits | — | m-token-partition-watermark | yes | own | token sampling in generated text | specified |
| `roger_2023:surveyed-introduction-variations` | prompted introduction-variation scheme | llm-generative-text | lgt-enumerated-openers | structural-format | codebook | prompt | 16 messages | m-phrase-codebook | yes | own | introduction sentence of an answer | prompted |
| `roger_2023:surveyed-scratchpad-scheme` | scratchpad scheme in which the model devises its own encoding | llm-generative-text | — | other (model-chosen) | — | prompt | 30 bits per answer | m-scheme-discovery-condition | no | own | — | — |
| `rose_2026:approach-blackjack-table-talk` | the Stego tier's blackjack table-talk channel, with a scheme the colluders invent per shoe | multi-agent-collusion | mac-covertext-codebooks | topic-semantic | codebook | prompt | three count levels per hand | m-utterance-category-code | yes | partial | kind of remark in table talk | negotiated |
| `rose_2026:approach-helios` | HELIOS, group-level collusion detection from per-agent activation probes | steganalysis | sa-activation-probes | other (activation probing) | — | weights | — | m-activation-probe | no | own | — | — |
| `rose_2026:approach-narcbench` | NARCBench, a three-tier benchmark for collusion detection under distribution shift | multi-agent-collusion | mac-collusion-benchmarks | — | — | prompt | — | m-collusion-benchmark | no | own | — | — |
| `sala_2018:approach-combinatorial-construction` | a combinatorial construction that embeds a tree in hyperbolic space with arbitrarily low distortion, without optimisation | non-steganography-foundation | nsf-hyperbolic-embeddings | — | — | — | — | m-hyperbolic-embeddings | no | own | — | — |
| `sala_2018:approach-h-mds` | hyperbolic multidimensional scaling (h-MDS): exact recovery of points from distances via a non-standard mean | non-steganography-foundation | nsf-hyperbolic-embeddings | — | — | — | — | m-hyperbolic-embeddings | no | own | — | — |
| `sala_2018:approach-pytorch-sgd-pga` | an SGD algorithm in PyTorch, initialised by h-MDS, recovers the data's submanifold under noise and handles incomplete distances | non-steganography-foundation | nsf-hyperbolic-embeddings | — | — | training | — | m-hyperbolic-embeddings | no | own | — | — |
| `sarkar_2011:approach-delaunay-tree-embedding` | Method — embed any tree in the hyperbolic plane as the Delaunay graph of its vertices | non-steganography-foundation | nsf-hyperbolic-embeddings | other (not a channel: geometric embedding) | — | — | — | m-hyperbolic-embeddings | no | own | — | — |
| `schroederdewitt_2022:approach-imec` | minimum entropy coupling steganography (iMEC): encode by coupling uniform-looking ciphertext with the covertext distribution, which makes the procedure perfectly secure and maximally efficient under Cachin's model | llm-generative-text | lgt-coupling | distributional-sampling | shared-key | logits | maximal throughput iff minimum entropy coupling; encoding efficiency above baselines at 20-bit blocks | m-min-entropy-coupling | yes | own | token sampling (also audio and image generation) | specified |
| `schulz_2026:approach-formatting-and-knapsack-encodings` | six surface-formatting encodings and the knapsack cover, applicable programmatically to existing text | llm-generative-text | lgt-surface-formatting; lgt-task-choice-codes | structural-format | codebook | prompt | one symbol per word, whitespace run or sentence; one bit per knapsack item | m-surface-formatting; m-item-inclusion-bits | yes | own;own | formatting of answer text; item choices in a knapsack solution | prompted;rl-trained;weight-trained |
| `schulz_2026:approach-three-method-stego-elicitation` | eliciting messaging, encoded reasoning and steganographic reasoning by in-context learning, RL and SFT | llm-capability-eval | lce-taught-schemes | structural-format | codebook | training | — | m-training-elicitation | no | own | — | — |
| `shen_2020:approach-saac` | SAAC, arithmetic coding over a pretrained LM in which the top-K truncation is re-chosen at every step to meet a per-step bound | llm-generative-text | lgt-interval-adaptive-truncation | distributional-sampling | shared-model | logits | about 4.8 bits per word at delta 0.01 (4.862 on Drug); 15.3% more bits per word than the prior best | m-interval-adaptive-truncation | yes | own | token sampling in generated text | specified |
| `shimizu_2020:approach-hnn-plus-plus` | a parameter-reduced MLR, FC, convolutional and attention layers, all in the Poincaré ball under one interpretation | non-steganography-foundation | nsf-hyperbolic-networks | — | — | training | — | m-hyperbolic-networks | no | own | — | — |
| `shimizu_2020:approach-poincare-beta-concatenation` | Poincaré β-concatenation: map inputs to the tangent space, rescale by beta-function ratios, concatenate, map back | non-steganography-foundation | nsf-hyperbolic-networks | — | — | — | — | m-hyperbolic-networks | no | own | — | — |
| `simmons_1984:approach-subliminal-channel` | the subliminal channel: authentication schemes in which several ciphers decrypt to the same message, so the choice of cipher carries side information as hard to detect as the cryptoalgorithm is to break | foundations-theory | ft-subliminal-channel | other (choice among ciphers that decrypt to the same message) | shared-key | — | one bit per message in the three-prime example; authentication capacity traded bit for bit | m-equivalent-choice | yes | own | choice among ciphers that decrypt to the same message | specified |
| `skaf_2025:approach-cot-penalty-rl` | RL fine-tuning with an outcome reward minus a rule-based CoT penalty on task-critical strings | llm-capability-eval | lce-rl-learned-codes | lexical | none | training | — | m-training-elicitation; m-codeword-substitution; m-character-variant | yes | own;sibling:coinflip-arbitrary-codebook;sibling:arithmetic-semantic-substitutes | tokens in a chain-of-thought trace | rl-trained |
| `tailor_2026:approach-rolewise-decomposition` | rolewise decomposition: score what the encoder put in the text, what the decoder recovered and what a deterministic verifier can reconstruct, in place of end-to-end recovery alone | llm-capability-eval | lce-eval-frameworks | — | — | prompt | — | m-eval-framework | no | own | — | — |
| `tailor_2026:surveyed-alternating-sentence-initials` | alternating sentence initials (prescribed rule) | llm-generative-text | lgt-letter-position-codes | lexical | codebook | prompt | one letter per two sentences | m-letter-position | yes | own | first letters of alternate sentences | prompted |
| `tailor_2026:surveyed-base64` | Base64 (prescribed rule) | llm-generative-text | lgt-byte-encodings | other (literal Base64 string) | codebook | prompt | — | m-byte-encoding | yes | own | encoded string in text | prompted |
| `tailor_2026:surveyed-eight-bit-binary` | eight-bit binary (prescribed rule) | llm-generative-text | lgt-byte-encodings | other (literal binary string) | codebook | prompt | eight binary digits per character | m-byte-encoding | yes | own | encoded string in text | prompted |
| `tailor_2026:surveyed-fixed-letter-substitution` | fixed-letter substitution (prescribed rule) | llm-generative-text | lgt-substitution-ciphers | other (substitution-cipher letters) | codebook | prompt | — | m-letter-substitution-cipher | yes | own | enciphered letters in text | prompted |
| `tailor_2026:surveyed-hexadecimal` | hexadecimal (prescribed rule) | llm-generative-text | lgt-byte-encodings | other (literal hex string) | codebook | prompt | — | m-byte-encoding | yes | own | encoded string in text | prompted |
| `tailor_2026:surveyed-sentence-initials` | sentence initials (prescribed rule) | llm-generative-text | lgt-letter-position-codes | lexical | codebook | prompt | one letter per sentence | m-letter-position | yes | own | first letters of sentences | prompted |
| `tailor_2026:surveyed-word-length-parity-token-initials` | word-length parity and token initials (not prescribed; found in model outputs) | llm-generative-text | lgt-count-state-codes; lgt-initial-class-codes | lexical | none | prompt | word-length parity: one bit per word | m-length-parity; m-initial-class | yes | own;own | word lengths and initial letters in text | prompted+unprescribed |
| `tancik_2019:approach-stegastamp` | Method — a learned encoder/decoder that hides hyperlink bitstrings in photos, robust to printing and photography | image-deep | id-physical-channel | pixel-spatial | shared-model | training | 100 encoded bits per image; at least 56 bits after BCH error correction | m-physical-channel-training; m-residual-encoder | yes | own;sibling:residual-encoder | printed or displayed photographs, re-captured | weight-trained |
| `tang_2019:approach-adv-emb` | Method — ADV-EMB adjusts embedding costs by the gradients of a target CNN steganalyser | image-classical | ic-adversarial-costs | transform-domain | — | weights | 0.1 to 0.5 bpnzAC (JPEG); 0.4 bpp in the spatial extension | m-adversarial-costs | yes | own | JPEG coefficient modifications | specified |
| `tang_2024:approach-lsgc` | LSGC, linguistic steganalysis by a LoRA-fine-tuned LLM, in a generation mode that explains its verdict and a classification mode that reads features in one pass | steganalysis | sa-llm-classifiers | other (detector of generative text stego) | — | training | — | m-llm-classifier | no | own | — | — |
| `tomasev_2020:approach-insilico-variant-assessment` | in-silico assessment of chess variants, by training AlphaZero to near-optimal play under each rule set | non-steganography-foundation | nsf-engine-and-opening-analysis | other (not a hiding channel; game-balance assessment) | — | training | — | m-opening-and-engine-analysis | no | own | — | — |
| `tomasev_2020:approach-prior-entropy-diversity` | opening diversity measured as the entropy of the first 20 plies of the AlphaZero prior | non-steganography-foundation | nsf-engine-and-opening-analysis | other (not a hiding channel; carrier-capacity measure for move choice) | — | weights | classical chess 28.58 nats over the first 20 plies of the prior against 64.96 nats for uniform legal-move choice | m-opening-and-engine-analysis | no | own | — | — |
| `wei_2022:approach-gsn` | Method — a generator synthesises stego images straight from secret data, with no cover | image-generative-coverless | igc-secret-conditioned-generator | latent-generative | shared-model | training | 1–8 bpp; extraction accuracy 97.5% at 1 bpp, about 59–61% at 8 bpp | m-secret-conditioned-generator | yes | own | generated images (generator feature maps) | weight-trained |
| `wen_2023:approach-tree-ring` | Method — embed a key in the Fourier transform of the initial diffusion noise; detect by DDIM inversion | watermarking | wm-initial-noise | latent-generative | shared-key | weights | zero-bit (presence test); capacity for multiple keys stated as open | m-initial-noise-mark | yes | own | initial diffusion noise (Fourier space) | specified |
| `westphal_2026:approach-evasive-steganographic-trojan` | the evasive steganographic trojan: an LLM fine-tuned to encode prompt-borne secrets into ordinary completions, then adversarially fine-tuned against refitted ridge critics so that probes see little beyond base-model signal | llm-generative-text | lgt-finetuned-encoders | lexical | shared-model | training | 32 bits per 32-token completion (one bit per token) | m-hyperplane-buckets | yes | sibling:hyperplane-bucket-encoding | token choice in completions | weight-trained |
| `westphal_2026:approach-probe-detection-recontextualisation` | mechanistic probe detection, extended from ridge to a held-out two-layer MLP probe, and restored against evasive trojans by a recontextualisation dataset that removes the slack the secret is routed through | steganalysis | sa-activation-probes | other (detector) | — | weights | — | m-activation-probe | no | own | — | — |
| `wu_2024:approach-llm-stega` | LLM-Stega, black-box steganography through an LLM's user interface: keyword sets from the LLM, an encrypted index mapping, and prompts that write and read back the stego sentence | llm-generative-text | lgt-entity-keyword-mapping | lexical | shared-key | prompt | 64 bits per sentence; 5.93 bpw (Entertainment News) and 4.81 bpw (science-fiction reviews) | m-keyword-set-index | yes | sibling:augmented-keyword-index-mapping | keywords of generated sentences | specified |
| `xia_2026:approach-lapha` | LaPha, AlphaZero-like LLM agents trained in a root-centred Poincaré latent space | non-steganography-foundation | nsf-hyperbolic-networks | — | — | weights, training | — | m-hyperbolic-networks | no | own | — | — |
| `xiang_2018:approach-wes` | WES, word-embedding steganalysis: context fitness of each synonym, three features from it, and an SVM | steganalysis | sa-text-features | lexical | — | training | — | m-text-feature-steganalysis | no | own | — | — |
| `xiang_2018:ss-carrier-substitution-sets` | Attacked carrier and encoding — synonym substitution: interchangeable synonyms form a substitution set, and the choice among them carries the bits | linguistic-text | — | lexical | — | — | — | m-synonym-substitution; m-synonym-multibase | yes | own;own | choice among synonyms in a cover text | specified |
| `xiang_2018:ss-scheme-family` | Prior SS schemes surveyed — vertex coding, matrix embedding and syndrome-trellis codes to reduce embedding distortion | linguistic-text | — | lexical | — | — | matrix coding: k bits per 2^k - 1 cover synonyms | m-synonym-vertex-coding; m-synonym-matrix-embedding; m-synonym-stc | yes | own;own;own | choice among synonyms in a cover text | specified |
| `yan_2010:approach-inference-engine-collusion-detector` | an inference engine over complete game records that flags bids and plays too good for the information a player legitimately held | steganalysis | sa-game-record-inference | move choice | — | — | — | m-game-record-inference | no | own | — | — |
| `yang_2024:approach-hyplora` | HypLoRA, low-rank adaptation performed directly on the hyperbolic manifold | non-steganography-foundation | nsf-hyperbolic-networks | — | — | weights, training | — | m-hyperbolic-networks | no | own | — | — |
| `yang_2026:approach-hyperbolicity-atlas` | a Gromov-hyperbolicity atlas of prompt-token hidden states across scale, depth, family and domain | non-steganography-foundation | nsf-hyperbolic-embeddings | — | — | weights | — | m-hyperbolic-embeddings | no | own | — | — |
| `yu_2023:approach-cross` | Method — coverless image steganography by invertible diffusion translation, with no training | image-generative-coverless | igc-diffusion-inversion | latent-generative | shared-key | weights | one secret image per container image | m-diffusion-translation | yes | own | generated container images | specified |
| `zamir_2024:approach-undetectable-llm-stego` | undetectable LLM steganography: the CGZ undetectable watermark extended to carry a multi-bit payload, recovered with a secret key through a dynamic error-correcting code with feedback | llm-generative-text | lgt-watermark-pseudorandom | distributional-sampling | shared-key | sender: logits; receiver: no model access | linear in response length (asymptotically optimal), only for high-entropy responses | m-pseudorandom-watermark-code | yes | own | token sampling in an LLM response | specified |
| `zhang_2018:approach-cardan-grille-inpainting` | Practical instance — a digital Cardan grille marks where the message is written; semantic inpainting fills the rest | image-generative-coverless | igc-grille-inpainting | pixel-spatial | shared-key | training | recovery above 70% at bit plane 7; higher bit planes more stable | m-grille-inpainting | yes | own | pixels at grille positions of an inpainted image | weight-trained |
| `zhang_2018:approach-gss` | Method — the stego image is sampled by a trained generator; no explicit cover | image-generative-coverless | igc-latent-search | latent-generative | shared-key | training | 1.49e-3 to 1.10e-2 bytes per pixel, to be multiplied by the extraction rate | m-latent-search | yes | own | generated images (searched latent code) | weight-trained |
| `zhang_2019:approach-steganogan` | Method — an adversarially trained encoder hides an arbitrary bit tensor in a cover image; a decoder recovers it | image-deep | id-adversarial-training | pixel-spatial | shared-model | training | up to 4.4 RS-bpp (Reed–Solomon-corrected); 2 bpp while Ye-net auROC stays at or below 0.8 | m-adversarial-training; m-cover-conditioned-encoder | yes | own;own | cover image pixels | weight-trained |
| `zhang_2021:approach-adg` | ADG, equal-probability grouping of the vocabulary at each step, repeated recursively on the selected group, then sampling inside it | llm-generative-text | lgt-grouping | distributional-sampling | shared-model | logits | about 5.1 to 5.7 bits per word on LSTM models (Movie 5.147, News 5.650, Tweet 5.411) | m-recursive-balanced-grouping | yes | own | token sampling in generated text | specified |
| `zhang_2021b:surveyed-adversarial-architecture` | adversarial architecture: a steganalyser in the training loop, a three-player game; it does not guarantee resistance to an independently trained steganalyser | image-deep | id-adversarial-training | pixel-spatial | — | training | — | m-adversarial-training | yes | own | image pixels | weight-trained |
| `zhang_2021b:surveyed-adversarial-watermarking-transformer` | text watermarking by an adversarially trained encoder–decoder transformer (AWT), set apart from generative text methods | watermarking | wm-learned-post-hoc | other (unobtrusive modification of an input text; edit type not stated) | — | training | binary message | m-adversarial-text-editing | yes | own | edited text | weight-trained |
| `zhang_2021b:surveyed-ddh-with-preparation` | cover-dependent deep hiding with a preparation network (Baluja): a full image hidden in another, at 24 bpp, and easily detected | image-deep | id-cover-dependent | pixel-spatial | — | — | 24 bpp (a full-size colour image in another of the same size) | m-media-embedding | yes | own | image pixels | weight-trained |
| `zhang_2021b:surveyed-ddh-without-preparation` | cover-dependent deep hiding without preparation, the most common architecture | image-deep | id-cover-dependent | pixel-spatial | — | — | — | m-media-embedding | yes | own | image pixels | weight-trained |
| `zhang_2021b:surveyed-light-field-messaging` | light field messaging: hidden data sent screen-to-camera, with robustness rather than undetectability as the goal | image-deep | id-physical-channel | pixel-spatial | — | — | — | m-physical-channel-training | yes | own | images shown on a screen and photographed | weight-trained |
| `zhang_2021b:surveyed-noise-augmentation-watermarking` | robust watermarking by attack simulation during training (HiDDeN and successors); JPEG's non-differentiability is the chief obstacle | watermarking | wm-learned-post-hoc | pixel-spatial | — | training | — | m-attack-simulated-training | yes | own | image pixels | weight-trained |
| `zhang_2021b:surveyed-speech-in-speech` | speech hidden in speech (Kreuk et al.), the image framework carried over with differentiable STFT layers | audio | au-deep-speech-hiding | transform-domain | — | training | — | m-spectral-audio-hiding | yes | own | speech audio | weight-trained |
| `zhang_2021b:surveyed-synthesis-generative` | synthesis (generative, modification-free) steganography: the container is generated from the message by a shared generator and extractor | image-generative-coverless | igc-latent-mapping | latent-generative | shared-model | training | — | m-latent-mapping | yes | own | generated images | weight-trained |
| `zhang_2021b:surveyed-universal-deep-hiding` | universal deep hiding: the secret is encoded independently of the cover and can be added to any cover | image-deep | id-universal | pixel-spatial | — | — | — | m-universal-perturbation | yes | own | image pixels | weight-trained |
| `zhou_2026:approach-conceptual-steganography` | conceptual steganography: each chain-of-thought step carries a bit in which reasoning behaviour it shows, not in its words, so a content-preserving paraphrase leaves the bit in place | llm-generative-text | lgt-reasoning-strategy-choice | topic-semantic | codebook | — | about 4.4 to 6.4 bits per CoT | m-reasoning-behaviour-choice | yes | own | reasoning behaviour of chain-of-thought steps | prompted |
| `zhu_2018:approach-hidden` | Method — jointly trained encoder and decoder, an adversary, and optional noise layers between them | image-deep | id-adversarial-training | pixel-spatial | shared-model | training | 0.203 bpp (52 bits per 16×16 patch), bit error below 1e-5 | m-cover-conditioned-encoder; m-attack-simulated-training; m-adversarial-training | yes | own;own;partial | image pixels | weight-trained |
| `ziegler_2019:approach-arithmetic-coding` | arithmetic-coding steganography over a large neural language model: a uniform message is decoded into tokens so that the cover text follows the model's distribution | llm-generative-text | lgt-interval-coding | distributional-sampling | shared-model | logits | entropy of the induced distribution; humans fooled at 1 bit/word; minimum KL near 4 bits/word | m-interval-plain | yes | own | token sampling in generated text | specified |
| `zolkowski_2025:approach-encoded-message-passing-eval` | an evaluation suite for encoded message passing under graded affordances | llm-capability-eval | lce-message-passing | lexical | — | prompt | short phrase of 8-20 characters | m-message-passing-task | no | own | — | — |
| `zolkowski_2025:approach-encoded-reasoning-eval` | the first evaluations of encoded reasoning, on hidden tasks inside a cover task | llm-capability-eval | lce-encoded-reasoning | structural-format | — | prompt | — | m-encoded-reasoning-task | no | own | — | — |
| `zolkowski_2025:surveyed-byte-encodings` | byte-encoding schemes (Base64, UTF-8 binary, Hex and their variants) | llm-generative-text | lgt-byte-encodings | other (overt encoding) | codebook | prompt | — | m-byte-encoding | yes | own | encoded string in text | prompted |
| `zolkowski_2025:surveyed-letter-position-acrostics` | letter-position acrostic schemes given to encoder and decoder | llm-generative-text | lgt-letter-position-codes | lexical | codebook | prompt | — | m-letter-position | yes | own | first letters of sentences or words | prompted |
| `zolkowski_2025:surveyed-model-generated-subtlety` | model-generated encoding schemes at three degrees of subtlety | llm-generative-text | — | other (model-chosen) | none | prompt | — | m-scheme-discovery-condition | no | own | — | — |
| `zolkowski_2025:surveyed-rotation-substitution` | rotation and substitution ciphers | llm-generative-text | lgt-substitution-ciphers | other (overt cipher) | codebook | prompt | — | m-letter-substitution-cipher | yes | own | enciphered letters in text | prompted |
| `zolkowski_2025:surveyed-state-tracking-encodings` | state-tracking encodings by first letter, sentence length, special characters and terminal punctuation | llm-generative-text | lgt-count-state-codes; lgt-letter-position-codes; lgt-surface-formatting | syntactic | codebook | prompt | one state per sentence | m-letter-position; m-count-code; m-punctuation-symbol | yes | own;own;own | sentence initials, sentence lengths and punctuation in text | prompted |

## Lineage edges (88)

| source | kind | target | lifted_from | ledger line |
| --- | --- | --- | --- | --- |
| `agarwal_2023:approach-hypersteg` | Depends-on | `ganea_2018:approach-hyperbolic-neural-networks` | — | agarwal_2023.md:195 |
| `anwar_2026:approach-steganographic-gap` | Qualifies | `hopper_2002:approach-complexity-theoretic-steganography` | `anwar_2026:classical-shortcomings-generalised` | anwar_2026.md:188 |
| `anwar_2026:approach-steganographic-gap` | Refines | `cachin_2004:approach-information-theoretic-model` | `anwar_2026:classical-shortcomings-generalised` | anwar_2026.md:187 |
| `bai_2024:approach-semantic-steganography` | Qualifies | `ding_2023:approach-discop` | `bai_2024:entropy-bounds-provably-secure-named` | bai_2024.md:193 |
| `bai_2024:approach-semantic-steganography` | Qualifies | `kaptchuk_2021:approach-meteor` | `bai_2024:entropy-bounds-provably-secure-named` | bai_2024.md:191 |
| `bai_2024:approach-semantic-steganography` | Qualifies | `schroederdewitt_2022:approach-imec` | `bai_2024:entropy-bounds-provably-secure-named` | bai_2024.md:192 |
| `bai_2024b:approach-generative-llm-steganalysis` | Qualifies | `ding_2023:approach-discop` | `bai_2024b:general-steganalysis-discop` | bai_2024b.md:189 |
| `bai_2024b:approach-generative-llm-steganalysis` | Qualifies | `zhang_2021:approach-adg` | `bai_2024b:detects-ac-adg-near-zero-deviation` | bai_2024b.md:187 |
| `bai_2024b:approach-generative-llm-steganalysis` | Qualifies | `ziegler_2019:approach-arithmetic-coding` | `bai_2024b:detects-ac-adg-near-zero-deviation` | bai_2024b.md:188 |
| `biswas_2015:surveyed-average-difference` | Restates | `regan_2012:approach-intrinsic-performance-ratings` | `regan_2012:scaled-error` | biswas_2015.md:120 |
| `biswas_2015:surveyed-statistical-regression` | Restates | `regan_2011:approach-intrinsic-rating-model` | `regan_2011:sensitivity-competence` | biswas_2015.md:134 |
| `boonstra_2024:approach-bayesian-hidden-code-forensics` | Depends-on | `regan_2011:approach-intrinsic-rating-model` | `boonstra_2024:chess-extension-move-quality` | boonstra_2024.md:185 |
| `buscemi_2026:approach-numeric-covert-games` | Refines | `motwani_2024:approach-case-framework` | — | buscemi_2026.md:192 |
| `cetin_2022:approach-hyperbolic-rl-srym` | Depends-on | `ganea_2018:approach-hyperbolic-neural-networks` | `cetin_2022:hybrid-network-on-hnn` | cetin_2022.md:91 |
| `chen_2021:approach-poincare-probe` | Depends-on | `ganea_2018:approach-hyperbolic-neural-networks` | `chen_2021:probe-construction-on-hnn` | chen_2021.md:92 |
| `desoky_2009:approach-chestega` | Rebuts | `hernandezcastro_2006:approach-ranked-move-choice` | `desoky_2009:rebuts-hernandezcastro` | desoky_2009.md:167 |
| `ding_2023:approach-discop` | Depends-on | `paper:cachin_1998` | `ding_2023:cachin-kl-zero`, `cachin_1998:relative-entropy-security` | ding_2023.md:155 |
| `ding_2023:approach-discop` | Qualifies | `kaptchuk_2021:approach-meteor` | — | ding_2023.md:154 |
| `ding_2023:approach-discop` | Rebuts | `zhang_2021:approach-adg` | — | ding_2023.md:153 |
| `ganea_2018:approach-hyperbolic-neural-networks` | Depends-on | `nickel_2017:approach-poincare-embeddings` | `ganea_2018:builds-on-poincare-embeddings` | ganea_2018.md:75 |
| `guo_2026:approach-bam-feedback-coding` | Depends-on | `cachin_2004:approach-information-theoretic-model` | `guo_2026:security-after-cachin` | guo_2026.md:208 |
| `guo_2026:approach-bam-feedback-coding` | Qualifies | `kaptchuk_2021:approach-meteor` | `guo_2026:white-box-schemes-named` | guo_2026.md:206 |
| `guo_2026:approach-bam-feedback-coding` | Qualifies | `schroederdewitt_2022:approach-imec` | `guo_2026:white-box-schemes-named` | guo_2026.md:205 |
| `guo_2026:approach-bam-feedback-coding` | Qualifies | `ziegler_2019:approach-arithmetic-coding` | `guo_2026:white-box-schemes-named` | guo_2026.md:207 |
| `guo_2026:approach-bam-feedback-coding` | Refines | `zamir_2024:approach-undetectable-llm-stego` | `guo_2026:feedback-after-zamir` | guo_2026.md:204 |
| `hammond_2025:approach-multi-agent-risk-taxonomy` | Restates | `motwani_2024:approach-common-knowledge-covertext` | `hammond_2025:motwani-covert-rates-shared-knowledge` | hammond_2025.md:196 |
| `hopper_2002:approach-complexity-theoretic-steganography` | Depends-on | `simmons_1984:approach-subliminal-channel` | — | hopper_2002.md:188 |
| `hopper_2002:approach-complexity-theoretic-steganography` | Qualifies | `cachin_1998:approach-information-theoretic-model` | — | hopper_2002.md:189 |
| `hopper_2002:approach-stateful-rejection-sampling` | Restates | `anderson_1998:approach-limits-of-steganography` | — | hopper_2002.md:205 |
| `hopper_2002:approach-stateless-unbiased-function` | Restates | `anderson_1998:approach-limits-of-steganography` | — | hopper_2002.md:221 |
| `hopper_2002:approach-stateless-unbiased-function` | Restates | `cachin_1998:approach-balanced-partition` | — | hopper_2002.md:222 |
| `jarviniemi_2025:approach-meta-model-focal-collusion` | Refines | `greenblatt_2023:approach-untrusted-monitoring-signal-jamming` | — | jarviniemi_2025.md:158 |
| `jarviniemi_2025:approach-meta-model-focal-collusion` | Supports | `mallen_2024:approach-subversion-strategy-eval` | `jarviniemi_2025:compatible-with-mallen` | jarviniemi_2025.md:170 |
| `kaptchuk_2021:approach-meteor` | Depends-on | `ziegler_2019:approach-arithmetic-coding` | `kaptchuk_2021:codebase-builds-on-ziegler` | kaptchuk_2021.md:204 |
| `kaptchuk_2021:approach-meteor` | Refines | `hopper_2002:approach-stateful-rejection-sampling` | `kaptchuk_2021:prior-symmetric-entropy-gathering` | kaptchuk_2021.md:201 |
| `kaptchuk_2021:approach-meteor` | Supersedes | `dai_2019:approach-patient-huffman` | `kaptchuk_2021:nlp-constructions-named` | kaptchuk_2021.md:203 |
| `kaptchuk_2021:approach-meteor` | Supersedes | `ziegler_2019:approach-arithmetic-coding` | `kaptchuk_2021:nlp-constructions-named` | kaptchuk_2021.md:202 |
| `ker_2007:approach-batch-square-root-capacity` | Depends-on | `cachin_2004:approach-information-theoretic-model` | — | ker_2007.md:167 |
| `ker_2008:approach-square-root-law` | Refines | `ker_2007:approach-batch-square-root-capacity` | — | ker_2008.md:181 |
| `kim_2024:approach-ccc` | Depends-on | `jhamtani_2018:approach-gac` | `jhamtani_2018:commentary-corpus` | kim_2024.md:189 |
| `maia2_2024:approach-maia2` | Refines | `mcilroyyoung_2020:approach-maia` | — | maia2_2024.md:149 |
| `maia2_2024:approach-maia2` | Supersedes | `mcilroyyoung_2020:approach-maia` | `maia2_2024:supersedes-maia1` | maia2_2024.md:150 |
| `mallen_2024:approach-subversion-strategy-eval` | Refines | `greenblatt_2023:approach-control-evaluation` | `mallen_2024:builds-on-ai-control` | mallen_2024.md:219 |
| `paper:anderson_1998` | Depends-on | `simmons_1984:approach-subliminal-channel` | `anderson_1998:builds-on-simmons-prisoners` | anderson_1998.md:240 |
| `paper:cachin_1998` | Depends-on | `simmons_1984:approach-subliminal-channel` | `cachin_1998:prisoners-problem-passive` | cachin_1998.md:213 |
| `paper:cachin_2004` | Depends-on | `simmons_1984:approach-subliminal-channel` | `cachin_2004:prisoners-problem` | cachin_2004.md:203 |
| `paper:cachin_2004` | Restates | `cachin_1998:approach-balanced-partition` | `cachin_2004:preliminary-version-1998` | cachin_2004.md:235 |
| `paper:cachin_2004` | Supersedes | `cachin_1998:approach-information-theoretic-model` | `cachin_2004:preliminary-version-1998` | cachin_2004.md:202 |
| `paper:hernandezcastro_2006` | Refines | `murdoch_2004:approach-equivalent-move-channel` | `hernandezcastro_2006:prior-art-murdoch` | hernandezcastro_2006.md:173 |
| `paper:karpov_2025` | Refines | `mathew_2024:approach-gbrl` | `karpov_2025:extends-mathew-multibit` | karpov_2025.md:219 |
| `paper:mathew_2024` | Qualifies | `roger_2023:approach-paraphrase-defence` | `mathew_2024:builds-on` | mathew_2024.md:157 |
| `paper:mathew_2024` | Refines | `motwani_2024:approach-case-framework` | `mathew_2024:builds-on` | mathew_2024.md:156 |
| `paper:molinari_2026` | Depends-on | `rose_2026:approach-narcbench` | `molinari_2026:relation-rose-narcbench` | molinari_2026.md:212 |
| `paper:molinari_2026` | Qualifies | `rose_2026:approach-helios` | `molinari_2026:relation-rose-narcbench` | molinari_2026.md:213 |
| `paper:motwani_2024` | Depends-on | `schroederdewitt_2022:approach-imec` | `motwani_2024:builds-on-ai-stego` | motwani_2024.md:184 |
| `paper:rippin_2026` | Refines | `aharon_2026:approach-focal-point-evaluation` | `rippin_2026:builds-on` | rippin_2026.md:189 |
| `paper:schulz_2026` | Qualifies | `skaf_2025:approach-cot-penalty-rl` | `schulz_2026:relation-zolkowski-skaf` | schulz_2026.md:232 |
| `paper:schulz_2026` | Qualifies | `zolkowski_2025:approach-encoded-reasoning-eval` | `schulz_2026:relation-zolkowski-skaf` | schulz_2026.md:231 |
| `paper:schulz_2026` | Supports | `zolkowski_2025:approach-encoded-reasoning-eval` | `schulz_2026:relation-zolkowski-skaf` | schulz_2026.md:230 |
| `paper:shimizu_2020` | Refines | `ganea_2018:approach-hyperbolic-neural-networks` | `shimizu_2020:refines-hnn`, `shimizu_2020:concatenation-versus-hnn`, `ganea_2018:hyperbolic-concatenation` | shimizu_2020.md:76, shimizu_2020.md:134 |
| `paper:zhang_2018` | Refines | `paper:cachin_1998` | `zhang_2018:js-epsilon-security`, `cachin_1998:relative-entropy-security` | zhang_2018.md:92 |
| `paper:zolkowski_2025` | Refines | `motwani_2024:approach-case-framework` | `zolkowski_2025:contrast-prior-evals` | zolkowski_2025.md:202 |
| `qin_2019:surveyed-dcgan-noise-vector` | Restates | `hu_2018:approach-dcgan-swe` | — | qin_2019.md:216 |
| `regan_2012:approach-intrinsic-performance-ratings` | Refines | `regan_2011:approach-intrinsic-rating-model` | — | regan_2012.md:138 |
| `rippin_2026:approach-agentic-covert-channel-construction` | Depends-on | `zamir_2024:approach-undetectable-llm-stego` | — | rippin_2026.md:171 |
| `ritchey_2012:approach-combinatorial-game-framework` | Depends-on | `simmons_1984:approach-subliminal-channel` | `ritchey_2012:builds-on-prisoners-problem` | ritchey_2012.md:161 |
| `ritchey_2012:approach-combinatorial-game-framework` | Refines | `hernandezcastro_2006:approach-ranked-move-choice` | `ritchey_2012:builds-on-hernandezcastro` | ritchey_2012.md:149 |
| `rose_2026:approach-helios` | Refines | `greenblatt_2023:approach-control-evaluation` | — | rose_2026.md:217 |
| `schroederdewitt_2022:approach-imec` | Depends-on | `cachin_1998:approach-information-theoretic-model` | — | schroederdewitt_2022.md:163 |
| `schroederdewitt_2022:approach-imec` | Supersedes | `dai_2019:approach-patient-huffman` | `schroederdewitt_2022:builds-on-imec-supersedes-coding` | schroederdewitt_2022.md:166 |
| `schroederdewitt_2022:approach-imec` | Supersedes | `kaptchuk_2021:approach-meteor` | `schroederdewitt_2022:builds-on-imec-supersedes-coding` | schroederdewitt_2022.md:165 |
| `schroederdewitt_2022:approach-imec` | Supersedes | `zhang_2021:approach-adg` | `schroederdewitt_2022:adg-not-perfectly-secure` | schroederdewitt_2022.md:167 |
| `schroederdewitt_2022:approach-imec` | Supersedes | `ziegler_2019:approach-arithmetic-coding` | `schroederdewitt_2022:builds-on-imec-supersedes-coding` | schroederdewitt_2022.md:164 |
| `shen_2020:approach-saac` | Depends-on | `dai_2019:approach-patient-huffman` | `dai_2019:tvd-security-notion` | shen_2020.md:203 |
| `shen_2020:approach-saac` | Refines | `ziegler_2019:approach-arithmetic-coding` | `ziegler_2019:arithmetic-coding-neural-lm` | shen_2020.md:202 |
| `tailor_2026:approach-rolewise-decomposition` | Qualifies | `karpov_2025:approach-prompted-stego-eval` | `tailor_2026:prior-e2e-recovery-named` | tailor_2026.md:206 |
| `tailor_2026:approach-rolewise-decomposition` | Qualifies | `mathew_2024:approach-gbrl` | `tailor_2026:prior-e2e-recovery-named` | tailor_2026.md:204 |
| `tailor_2026:approach-rolewise-decomposition` | Qualifies | `mathew_2024:approach-icrl` | `tailor_2026:prior-e2e-recovery-named` | tailor_2026.md:205 |
| `tailor_2026:approach-rolewise-decomposition` | Qualifies | `motwani_2024:approach-case-framework` | `tailor_2026:prior-e2e-recovery-named` | tailor_2026.md:203 |
| `tailor_2026:approach-rolewise-decomposition` | Qualifies | `zolkowski_2025:approach-encoded-message-passing-eval` | `tailor_2026:prior-e2e-recovery-named` | tailor_2026.md:202 |
| `wu_2024:approach-llm-stega` | Qualifies | `dai_2019:approach-patient-huffman` | — | wu_2024.md:194 |
| `wu_2024:approach-llm-stega` | Qualifies | `ziegler_2019:approach-arithmetic-coding` | `ziegler_2019:arithmetic-coding-neural-lm` | wu_2024.md:193 |
| `xia_2026:approach-lapha` | Depends-on | `nickel_2017:approach-poincare-embeddings` | `xia_2026:transfers-poincare-insight` | xia_2026.md:92 |
| `yang_2024:approach-hyplora` | Depends-on | `cetin_2022:approach-hyperbolic-rl-srym` | `yang_2024:token-delta-hyperbolicity`, `cetin_2022:delta-hyperbolicity-diagnostic` | yang_2024.md:61 |
| `yang_2024:approach-hyplora` | Qualifies | `ganea_2018:approach-hyperbolic-neural-networks` | `yang_2024:tangent-space-cancellation` | yang_2024.md:93 |
| `zhang_2021:approach-adg` | Depends-on | `paper:cachin_1998` | `cachin_1998:relative-entropy-security` | zhang_2021.md:194 |
| `zhang_2021b:surveyed-speech-in-speech` | Restates | `kreuk_2019:approach-hide-and-speak` | — | zhang_2021b.md:169 |
| `zhou_2026:approach-conceptual-steganography` | Qualifies | `roger_2023:approach-paraphrase-defence` | `zhou_2026:paraphrase-defence-exploited` | zhou_2026.md:171 |

## Unclassified approaches (0)

None.

## Edges not placed

### No approach claim in the ledger (0)

None.

### Unresolved (0)

None.

### Both ends lift onto one approach (0)

None.

## Techniques with no approaches (1)

- `lce-scheme-discovery`

## Table warnings (3)

- aharon_2026:approach-focal-point-evaluation: technique 'lce-coordination-evals' belongs to family 'llm-capability-eval', not 'multi-agent-collusion'; not placed under it
- roger_2023:surveyed-scratchpad-scheme: technique 'lce-scheme-discovery' belongs to family 'llm-capability-eval', not 'llm-generative-text'; not placed under it
- zolkowski_2025:surveyed-model-generated-subtlety: technique 'lce-scheme-discovery' belongs to family 'llm-capability-eval', not 'llm-generative-text'; not placed under it
