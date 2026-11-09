---
generated: 2026-11-08T20:09:54+03:00
---

# Approach map — mechanisms

Built by `tools/build_approach_map.py` from `C:\Users\user\Documents\GitHub\hypersteg_chess\hypersteg_novelty_kit_20261108\literature\verified_claims`, the features table `C:\Users\user\Documents\GitHub\hypersteg_chess\hypersteg_novelty_kit_20261108\maps\approach_features.tsv` and the mechanism taxonomy `C:\Users\user\Documents\GitHub\hypersteg_chess\hypersteg_novelty_kit_20261108\maps\mechanism_taxonomy.tsv`. Derived: edit the ledgers or the tables, never this file. A mechanism class groups approaches by how they hide bits, across paper families; each class's approaches are in its own file, listed below. Family overview: [approach_map.md](approach_map.md).

- mechanism classes: 18
- mechanism nodes: 165 (50 non-landing)
- approaches with a mechanism placement: 195
- landable approaches: 117
- approaches with no mechanism: 0
- mechanism nodes shared across families: 8
- mechanisms with no approaches: 2
- landing leaves with no published evidence: 0

```mermaid
flowchart LR
  subgraph cls_collusion_signal_g["collusion-signal (6)"]
    mech_m_authenticate_then_act["Authenticate, then act (1)"]
    mech_m_collusion_signal["Collusion signals (6)"]
    mech_m_focal_magic_number["Focal magic numbers (1)"]
    mech_m_input_trigger["Input-feature trigger (1)"]
    mech_m_output_signal["Output signal (3)"]
    mech_m_payoff_anchored_symbols["Payoff-anchored numeric signals (1)"]
  end
  subgraph cls_coordination_g["coordination (4)"]
    mech_m_coordination["Coordination without a message (4)"]
    mech_m_emergent_convention["Conventions emerging in interaction (2)"]
    mech_m_learned_tacit_collusion["Learned tacit collusion (1)"]
    mech_m_schelling_choice["Schelling-point choice of scheme (1)"]
  end
  subgraph cls_cover_modification_g["cover-modification (3)"]
    mech_m_adversarial_costs["Steganalyser-gradient cost adjustment (1)"]
    mech_m_cost_based_embedding["Cost-based embedding (1)"]
    mech_m_cover_modification["Cover modification (3)"]
    mech_m_keyed_parity["Keyed-set parity (1)"]
    mech_m_repetition_rank_exchange["Repetition-rank block exchange (1)"]
  end
  subgraph cls_cover_selection_g["cover-selection (10)"]
    mech_m_authentic_record_selection["Authentic-record selection (1)"]
    mech_m_cover_selection["Cover selection (10)"]
    mech_m_feature_hash_selection["Feature-hash selection (4)"]
    mech_m_file_attribute_mapping["File-attribute category mapping (1)"]
    mech_m_patch_retrieval["Partial-duplicate patch retrieval (2)"]
    mech_m_visual_word_mapping["Visual-word mapping (1)"]
  end
  subgraph cls_detection_g["detection (13)"]
    mech_m_activation_probe["Activation probes (2)"]
    mech_m_active_warden["Active-warden defences (3)"]
    mech_m_adversary_decoding["Adversary decoding attempts (0)"]
    mech_m_concept_lens["Concept-lens readout (2)"]
    mech_m_detection["Detectors, monitors and defences (13)"]
    mech_m_feature_steganalysis["Statistical feature steganalysis (2)"]
    mech_m_game_record_inference["Game-record inference (1)"]
    mech_m_game_statistics["Game-statistics attacks (1)"]
    mech_m_likelihood_ratio_forensics["Hypothesis-comparison forensics (1)"]
    mech_m_llm_classifier["LLM classifiers (2)"]
    mech_m_non_text_statistical_detection["Entropy of non-text messages (0)"]
    mech_m_prompted_llm_monitor["Prompted LLM monitor (1)"]
    mech_m_text_feature_steganalysis["Text feature steganalysis (1)"]
    mech_m_utility_gap["Decision-theoretic utility gap (1)"]
  end
  subgraph cls_evaluation_g["evaluation (22)"]
    mech_m_agentic_construction_eval["Agentic stegosystem construction (1)"]
    mech_m_collusion_benchmark["Collusion audits and benchmarks (2)"]
    mech_m_control_evaluation["Control evaluations (1)"]
    mech_m_coordination_eval["Focal-point evaluations (2)"]
    mech_m_encoded_reasoning_task["Encoded reasoning task (1)"]
    mech_m_eval_framework["Evaluation frameworks (2)"]
    mech_m_evaluation["Evaluations, benchmarks and elicitation conditions (22)"]
    mech_m_focality_prompt["Focality prompts (3)"]
    mech_m_message_passing_task["Encoded message-passing task (3)"]
    mech_m_risk_taxonomy["Risk taxonomies (1)"]
    mech_m_scheme_discovery_condition["Scheme-discovery condition (2)"]
    mech_m_stateless_subversion_eval["Stateless subversion evaluation (1)"]
    mech_m_training_elicitation["Training-based elicitation (3)"]
  end
  subgraph cls_foundation_g["foundation (36)"]
    mech_m_chess_language_models["Chess language models and datasets (3)"]
    mech_m_commentary_evaluation["Commentary evaluation (1)"]
    mech_m_commentary_generation["Commentary generation (2)"]
    mech_m_coordination_learning["Symmetry-robust coordination learning (1)"]
    mech_m_engine_benchmark_assessment["Engine-match assessment (4)"]
    mech_m_foundation["Non-steganographic foundations (36)"]
    mech_m_human_move_models["Models of human move choice (11)"]
    mech_m_hyperbolic_embeddings["Hyperbolic embeddings and measurement (8)"]
    mech_m_hyperbolic_networks["Hyperbolic network layers and agents (6)"]
    mech_m_intrinsic_rating["Intrinsic rating models (4)"]
    mech_m_llm_chess_play["LLM chess play (1)"]
    mech_m_neural_human_move["Neural human-move predictors (3)"]
    mech_m_opening_and_engine_analysis["Engine and opening analysis (3)"]
  end
  subgraph cls_generative_synthesis_g["generative-synthesis (10)"]
    mech_m_decoder_finetune_mark["Fine-tuned decoder mark (1)"]
    mech_m_diffusion_translation["Diffusion translation (1)"]
    mech_m_generation_time_watermark["Generation-time watermark (2)"]
    mech_m_generative_synthesis["Generative synthesis of media (10)"]
    mech_m_generator_model_database["Generator-model database (1)"]
    mech_m_grille_inpainting["Grille and inpainting (1)"]
    mech_m_initial_noise_mark["Initial-noise mark (1)"]
    mech_m_latent_mapping["Message-to-latent mapping (3)"]
    mech_m_latent_search["Latent search (1)"]
    mech_m_secret_conditioned_generator["Secret-conditioned generator (1)"]
  end
  subgraph cls_key_establishment_g["key-establishment (2)"]
    mech_m_key_establishment["Covert key establishment without a pre-shared secret (2)"]
    mech_m_public_key_block_parity["Public-key ciphertext as block parity (1)"]
    mech_m_sampled_lattice_key_exchange["Lattice key exchange in honest samples (1)"]
  end
  subgraph cls_media_embedding_g["media-embedding (14)"]
    mech_m_adversarial_text_editing["Adversarially trained text editing (1)"]
    mech_m_adversarial_training["Adversarially trained hiding (3)"]
    mech_m_attack_simulated_training["Attack-simulated training (4)"]
    mech_m_cover_conditioned_encoder["Cover-conditioned encoder (2)"]
    mech_m_hyperbolic_blending["Hyperbolic blending (1)"]
    mech_m_invertible_encoder["Invertible encoder-decoder (1)"]
    mech_m_media_embedding["Learned media embedding (14)"]
    mech_m_physical_channel_training["Physical-channel training (2)"]
    mech_m_residual_encoder["Residual encoder (1)"]
    mech_m_spectral_audio_hiding["Spectral speech hiding (2)"]
    mech_m_universal_perturbation["Cover-independent (universal) encoding (1)"]
  end
  subgraph cls_overt_encoding_g["overt-encoding (8)"]
    mech_m_byte_encoding["Byte encodings (5)"]
    mech_m_letter_substitution_cipher["Letter rotation and substitution ciphers (4)"]
    mech_m_overt_encoding["Overt encodings and ciphers (8)"]
    mech_m_partial_word_cipher["Partial word-level cipher (1)"]
  end
  subgraph cls_sampling_g["sampling (23)"]
    mech_m_balanced_partition["Near-equiprobable partition (3)"]
    mech_m_coupling["Coupling codes (3)"]
    mech_m_distribution_copies["Distribution copies (1)"]
    mech_m_feedback_coding["Feedback (posterior-matching) coding (1)"]
    mech_m_fixed_bins["Fixed shared bins (1)"]
    mech_m_huffman_every_step["Huffman at every step (1)"]
    mech_m_huffman_patient["Thresholded (patient) Huffman (1)"]
    mech_m_hyperplane_buckets["Hyperplane buckets (1)"]
    mech_m_interval_adaptive_truncation["Interval coding with per-step truncation (1)"]
    mech_m_interval_coding["Interval (range or arithmetic) coding (4)"]
    mech_m_interval_keyed_randomness["Keyed sampling-randomness embedding (1)"]
    mech_m_interval_plain["Plain range partition over a fixed model (2)"]
    mech_m_maximal_coupling_public_draft["Maximal coupling through a public draft model (1)"]
    mech_m_min_entropy_coupling["Minimum-entropy coupling (1)"]
    mech_m_partition_codes["Partition codes (5)"]
    mech_m_prefix_codes["Prefix-code (Huffman) sampling (2)"]
    mech_m_pseudorandom_watermark_code["Key-correlated sampling randomness (1)"]
    mech_m_recursive_balanced_grouping["Recursive near-equiprobable grouping (1)"]
    mech_m_rejection_keyed_stateful["Keyed, bounded rejection sampling (1)"]
    mech_m_rejection_public_unbiased["Rejection sampling with a public unbiased function (1)"]
    mech_m_rejection_sampling["Rejection sampling (2)"]
    mech_m_robust_feature_function["Keyed function of a robust document feature (1)"]
    mech_m_sampling["Distribution-steered sampling codes (23)"]
    mech_m_shared_sample_robust["Shared-sample robust coding (1)"]
    mech_m_token_partition_watermark["Token-partition (red-green) watermark codes (2)"]
    mech_m_universal_estimate_and_sample["Estimate-and-sample universal stegosystem (1)"]
  end
  subgraph cls_selection_g["selection (24)"]
    mech_m_codebook["Codebook choice (11)"]
    mech_m_combinatorial_subset_index["Combinatorial subset index (1)"]
    mech_m_engine_ranked_index["Engine-ranked index (2)"]
    mech_m_entity_tree_class["Ontology-entity semantic space (1)"]
    mech_m_equivalent_choice["Equivalent-alternative choice (2)"]
    mech_m_free_task_choice["Free choices within a task (1)"]
    mech_m_insertion_parameters["Optional-insertion parameters (1)"]
    mech_m_item_inclusion_bits["Item in/out bits (1)"]
    mech_m_keyed_play_convention["Signalling keyed by private knowledge (1)"]
    mech_m_keyed_strategy_set_index["Keyed strategy-set coding (1)"]
    mech_m_keyword_set_index["Keyword-set index (1)"]
    mech_m_mixed_radix_index["Mixed-radix index over all legal options (1)"]
    mech_m_ordered_choice_index["Move-choice indexing (ordered alternatives) (5)"]
    mech_m_phrase_codebook["Phrase codebook (4)"]
    mech_m_pointer_code["Pointer (book-cipher) code (1)"]
    mech_m_policy_identity["Policy identity (1)"]
    mech_m_reasoning_behaviour_choice["Reasoning-behaviour choice (1)"]
    mech_m_reference_code["Reference code into shared data (3)"]
    mech_m_selection["Enumerated-choice codes (24)"]
    mech_m_semantic_content["Semantic-content choice (3)"]
    mech_m_stated_value_code["Stated-value code (1)"]
    mech_m_uniform_reference["Reference to equally likely items (1)"]
    mech_m_utterance_category_code["Utterance-category code (1)"]
  end
  subgraph cls_side_signal_g["side-signal (2)"]
    mech_m_acoustic_signal["Acoustic signal (1)"]
    mech_m_orientation_signal["Orientation signal (1)"]
    mech_m_side_signal["Out-of-band physical signals (2)"]
  end
  subgraph cls_substitution_g["substitution (9)"]
    mech_m_associated_term_substitution["Associated-term substitution (1)"]
    mech_m_character_variant["Character-variant substitution (1)"]
    mech_m_codeword_substitution["Codeword substitution (4)"]
    mech_m_substitution["Substitution codes (9)"]
    mech_m_synonym_matrix_embedding["Matrix embedding over synonyms (1)"]
    mech_m_synonym_multibase["Multi-base synonym coding (1)"]
    mech_m_synonym_stc["Syndrome-trellis-coded synonym substitution (1)"]
    mech_m_synonym_substitution["Synonym substitution (3)"]
    mech_m_synonym_vertex_coding["Vertex coding of synonyms (1)"]
  end
  subgraph cls_surface_rule_g["surface-rule (9)"]
    mech_m_count_code["Count codes (2)"]
    mech_m_initial_class["Initial-class codes (1)"]
    mech_m_length_parity["Word-length parity (1)"]
    mech_m_letter_position["Letter-position codes (acrostics) (6)"]
    mech_m_literal_payload_name["Literal payload as a name or acronym (1)"]
    mech_m_punctuation_symbol["Punctuation and special-character codes (1)"]
    mech_m_surface_formatting["Surface-formatting codes (1)"]
    mech_m_surface_rule["Surface-feature rule codes (9)"]
  end
  subgraph cls_theory_g["theory (6)"]
    mech_m_capacity_laws["Capacity laws (2)"]
    mech_m_complexity_theoretic_security["Complexity-theoretic security (1)"]
    mech_m_informal_limits["Informal limits and terminology (1)"]
    mech_m_information_theoretic_security["Information-theoretic security (2)"]
    mech_m_theory["Security definitions, limits and capacity laws (6)"]
  end
  subgraph cls_timing_g["timing (2)"]
    mech_m_move_timing["Move timing (1)"]
    mech_m_timing["Timing channels (2)"]
  end
  mech_m_side_signal --- mech_m_acoustic_signal
  mech_m_detection --- mech_m_activation_probe
  mech_m_detection --- mech_m_active_warden
  mech_m_cost_based_embedding --- mech_m_adversarial_costs
  mech_m_media_embedding --- mech_m_adversarial_text_editing
  mech_m_media_embedding --- mech_m_adversarial_training
  mech_m_detection --- mech_m_adversary_decoding
  mech_m_evaluation --- mech_m_agentic_construction_eval
  mech_m_substitution --- mech_m_associated_term_substitution
  mech_m_media_embedding --- mech_m_attack_simulated_training
  mech_m_cover_selection --- mech_m_authentic_record_selection
  mech_m_collusion_signal --- mech_m_authenticate_then_act
  mech_m_partition_codes --- mech_m_balanced_partition
  mech_m_overt_encoding --- mech_m_byte_encoding
  mech_m_theory --- mech_m_capacity_laws
  mech_m_substitution --- mech_m_character_variant
  mech_m_foundation --- mech_m_chess_language_models
  mech_m_selection --- mech_m_codebook
  mech_m_substitution --- mech_m_codeword_substitution
  mech_m_evaluation --- mech_m_collusion_benchmark
  mech_m_selection --- mech_m_combinatorial_subset_index
  mech_m_foundation --- mech_m_commentary_evaluation
  mech_m_foundation --- mech_m_commentary_generation
  mech_m_theory --- mech_m_complexity_theoretic_security
  mech_m_detection --- mech_m_concept_lens
  mech_m_evaluation --- mech_m_control_evaluation
  mech_m_evaluation --- mech_m_coordination_eval
  mech_m_foundation --- mech_m_coordination_learning
  mech_m_cover_modification --- mech_m_cost_based_embedding
  mech_m_surface_rule --- mech_m_count_code
  mech_m_sampling --- mech_m_coupling
  mech_m_media_embedding --- mech_m_cover_conditioned_encoder
  mech_m_generation_time_watermark --- mech_m_decoder_finetune_mark
  mech_m_generative_synthesis --- mech_m_diffusion_translation
  mech_m_sampling --- mech_m_distribution_copies
  mech_m_coordination --- mech_m_emergent_convention
  mech_m_evaluation --- mech_m_encoded_reasoning_task
  mech_m_human_move_models --- mech_m_engine_benchmark_assessment
  mech_m_ordered_choice_index --- mech_m_engine_ranked_index
  mech_m_semantic_content --- mech_m_entity_tree_class
  mech_m_ordered_choice_index --- mech_m_equivalent_choice
  mech_m_evaluation --- mech_m_eval_framework
  mech_m_cover_selection --- mech_m_feature_hash_selection
  mech_m_detection --- mech_m_feature_steganalysis
  mech_m_sampling --- mech_m_feedback_coding
  mech_m_cover_selection --- mech_m_file_attribute_mapping
  mech_m_partition_codes --- mech_m_fixed_bins
  mech_m_output_signal --- mech_m_focal_magic_number
  mech_m_evaluation --- mech_m_focality_prompt
  mech_m_selection --- mech_m_free_task_choice
  mech_m_detection --- mech_m_game_record_inference
  mech_m_feature_steganalysis --- mech_m_game_statistics
  mech_m_generative_synthesis --- mech_m_generation_time_watermark
  mech_m_generative_synthesis --- mech_m_generator_model_database
  mech_m_generative_synthesis --- mech_m_grille_inpainting
  mech_m_prefix_codes --- mech_m_huffman_every_step
  mech_m_prefix_codes --- mech_m_huffman_patient
  mech_m_foundation --- mech_m_human_move_models
  mech_m_media_embedding --- mech_m_hyperbolic_blending
  mech_m_foundation --- mech_m_hyperbolic_embeddings
  mech_m_foundation --- mech_m_hyperbolic_networks
  mech_m_partition_codes --- mech_m_hyperplane_buckets
  mech_m_theory --- mech_m_informal_limits
  mech_m_theory --- mech_m_information_theoretic_security
  mech_m_surface_rule --- mech_m_initial_class
  mech_m_generation_time_watermark --- mech_m_initial_noise_mark
  mech_m_collusion_signal --- mech_m_input_trigger
  mech_m_selection --- mech_m_insertion_parameters
  mech_m_interval_coding --- mech_m_interval_adaptive_truncation
  mech_m_sampling --- mech_m_interval_coding
  mech_m_interval_coding --- mech_m_interval_keyed_randomness
  mech_m_interval_coding --- mech_m_interval_plain
  mech_m_human_move_models --- mech_m_intrinsic_rating
  mech_m_media_embedding --- mech_m_invertible_encoder
  mech_m_free_task_choice --- mech_m_item_inclusion_bits
  mech_m_cover_modification --- mech_m_keyed_parity
  mech_m_selection --- mech_m_keyed_play_convention
  mech_m_ordered_choice_index --- mech_m_keyed_strategy_set_index
  mech_m_semantic_content --- mech_m_keyword_set_index
  mech_m_generative_synthesis --- mech_m_latent_mapping
  mech_m_generative_synthesis --- mech_m_latent_search
  mech_m_coordination --- mech_m_learned_tacit_collusion
  mech_m_count_code --- mech_m_length_parity
  mech_m_surface_rule --- mech_m_letter_position
  mech_m_overt_encoding --- mech_m_letter_substitution_cipher
  mech_m_detection --- mech_m_likelihood_ratio_forensics
  mech_m_surface_rule --- mech_m_literal_payload_name
  mech_m_foundation --- mech_m_llm_chess_play
  mech_m_detection --- mech_m_llm_classifier
  mech_m_coupling --- mech_m_maximal_coupling_public_draft
  mech_m_evaluation --- mech_m_message_passing_task
  mech_m_coupling --- mech_m_min_entropy_coupling
  mech_m_selection --- mech_m_mixed_radix_index
  mech_m_timing --- mech_m_move_timing
  mech_m_human_move_models --- mech_m_neural_human_move
  mech_m_feature_steganalysis --- mech_m_non_text_statistical_detection
  mech_m_foundation --- mech_m_opening_and_engine_analysis
  mech_m_selection --- mech_m_ordered_choice_index
  mech_m_side_signal --- mech_m_orientation_signal
  mech_m_collusion_signal --- mech_m_output_signal
  mech_m_letter_substitution_cipher --- mech_m_partial_word_cipher
  mech_m_sampling --- mech_m_partition_codes
  mech_m_cover_selection --- mech_m_patch_retrieval
  mech_m_collusion_signal --- mech_m_payoff_anchored_symbols
  mech_m_codebook --- mech_m_phrase_codebook
  mech_m_attack_simulated_training --- mech_m_physical_channel_training
  mech_m_reference_code --- mech_m_pointer_code
  mech_m_selection --- mech_m_policy_identity
  mech_m_sampling --- mech_m_prefix_codes
  mech_m_detection --- mech_m_prompted_llm_monitor
  mech_m_sampling --- mech_m_pseudorandom_watermark_code
  mech_m_key_establishment --- mech_m_public_key_block_parity
  mech_m_surface_rule --- mech_m_punctuation_symbol
  mech_m_semantic_content --- mech_m_reasoning_behaviour_choice
  mech_m_balanced_partition --- mech_m_recursive_balanced_grouping
  mech_m_codebook --- mech_m_reference_code
  mech_m_rejection_sampling --- mech_m_rejection_keyed_stateful
  mech_m_rejection_sampling --- mech_m_rejection_public_unbiased
  mech_m_sampling --- mech_m_rejection_sampling
  mech_m_cover_modification --- mech_m_repetition_rank_exchange
  mech_m_media_embedding --- mech_m_residual_encoder
  mech_m_evaluation --- mech_m_risk_taxonomy
  mech_m_sampling --- mech_m_robust_feature_function
  mech_m_key_establishment --- mech_m_sampled_lattice_key_exchange
  mech_m_coordination --- mech_m_schelling_choice
  mech_m_evaluation --- mech_m_scheme_discovery_condition
  mech_m_generative_synthesis --- mech_m_secret_conditioned_generator
  mech_m_selection --- mech_m_semantic_content
  mech_m_sampling --- mech_m_shared_sample_robust
  mech_m_media_embedding --- mech_m_spectral_audio_hiding
  mech_m_codebook --- mech_m_stated_value_code
  mech_m_evaluation --- mech_m_stateless_subversion_eval
  mech_m_surface_rule --- mech_m_surface_formatting
  mech_m_synonym_substitution --- mech_m_synonym_matrix_embedding
  mech_m_synonym_substitution --- mech_m_synonym_multibase
  mech_m_synonym_substitution --- mech_m_synonym_stc
  mech_m_substitution --- mech_m_synonym_substitution
  mech_m_synonym_substitution --- mech_m_synonym_vertex_coding
  mech_m_feature_steganalysis --- mech_m_text_feature_steganalysis
  mech_m_sampling --- mech_m_token_partition_watermark
  mech_m_evaluation --- mech_m_training_elicitation
  mech_m_reference_code --- mech_m_uniform_reference
  mech_m_sampling --- mech_m_universal_estimate_and_sample
  mech_m_media_embedding --- mech_m_universal_perturbation
  mech_m_detection --- mech_m_utility_gap
  mech_m_codebook --- mech_m_utterance_category_code
  mech_m_cover_selection --- mech_m_visual_word_mapping
  linkStyle 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146 stroke:#9e9e9e,stroke-width:1px
  classDef nonlanding fill:#eeeeee,stroke:#bdbdbd,stroke-dasharray:2 2,color:#9e9e9e
  class mech_m_activation_probe,mech_m_active_warden,mech_m_adversary_decoding,mech_m_agentic_construction_eval,mech_m_capacity_laws,mech_m_chess_language_models,mech_m_collusion_benchmark,mech_m_commentary_evaluation,mech_m_commentary_generation,mech_m_complexity_theoretic_security,mech_m_concept_lens,mech_m_control_evaluation,mech_m_coordination,mech_m_coordination_eval,mech_m_coordination_learning,mech_m_detection,mech_m_emergent_convention,mech_m_encoded_reasoning_task,mech_m_engine_benchmark_assessment,mech_m_eval_framework,mech_m_evaluation,mech_m_feature_steganalysis,mech_m_focality_prompt,mech_m_foundation,mech_m_game_record_inference,mech_m_game_statistics,mech_m_human_move_models,mech_m_hyperbolic_embeddings,mech_m_hyperbolic_networks,mech_m_informal_limits,mech_m_information_theoretic_security,mech_m_input_trigger,mech_m_intrinsic_rating,mech_m_learned_tacit_collusion,mech_m_likelihood_ratio_forensics,mech_m_llm_chess_play,mech_m_llm_classifier,mech_m_message_passing_task,mech_m_neural_human_move,mech_m_non_text_statistical_detection,mech_m_opening_and_engine_analysis,mech_m_prompted_llm_monitor,mech_m_risk_taxonomy,mech_m_schelling_choice,mech_m_scheme_discovery_condition,mech_m_stateless_subversion_eval,mech_m_text_feature_steganalysis,mech_m_theory,mech_m_training_elicitation,mech_m_utility_gap nonlanding
```

Muted, dashed nodes are marked not a landing node: they group the tree, and a novelty audit does not place a scheme at one. A child of such a node is one too unless its row says `landing: yes`.

## Mechanism classes

| class | mechanisms | approaches | families | file |
| --- | --- | --- | --- | --- |
| collusion-signal | 6 | 6 | llm-capability-eval, multi-agent-collusion | [approach_map_mech_collusion_signal.md](approach_map_mech_collusion_signal.md) |
| coordination | 4 | 4 | multi-agent-collusion | [approach_map_mech_coordination.md](approach_map_mech_coordination.md) |
| cover-modification | 5 | 3 | foundations-theory, image-classical | [approach_map_mech_cover_modification.md](approach_map_mech_cover_modification.md) |
| cover-selection | 6 | 10 | game-and-chess, image-generative-coverless | [approach_map_mech_cover_selection.md](approach_map_mech_cover_selection.md) |
| detection | 14 | 13 | steganalysis | [approach_map_mech_detection.md](approach_map_mech_detection.md) |
| evaluation | 13 | 22 | llm-capability-eval, llm-generative-text, multi-agent-collusion | [approach_map_mech_evaluation.md](approach_map_mech_evaluation.md) |
| foundation | 13 | 36 | multi-agent-collusion, non-steganography-foundation | [approach_map_mech_foundation.md](approach_map_mech_foundation.md) |
| generative-synthesis | 10 | 10 | image-generative-coverless, watermarking | [approach_map_mech_generative_synthesis.md](approach_map_mech_generative_synthesis.md) |
| key-establishment | 3 | 2 | foundations-theory, llm-generative-text | [approach_map_mech_key_establishment.md](approach_map_mech_key_establishment.md) |
| media-embedding | 11 | 14 | audio, hyperbolic, image-deep, watermarking | [approach_map_mech_media_embedding.md](approach_map_mech_media_embedding.md) |
| overt-encoding | 4 | 8 | llm-capability-eval, llm-generative-text | [approach_map_mech_overt_encoding.md](approach_map_mech_overt_encoding.md) |
| sampling | 26 | 23 | foundations-theory, linguistic-text, llm-generative-text | [approach_map_mech_sampling.md](approach_map_mech_sampling.md) |
| selection | 23 | 24 | foundations-theory, game-and-chess, llm-capability-eval, llm-generative-text, multi-agent-collusion | [approach_map_mech_selection.md](approach_map_mech_selection.md) |
| side-signal | 3 | 2 | game-and-chess | [approach_map_mech_side_signal.md](approach_map_mech_side_signal.md) |
| substitution | 9 | 9 | linguistic-text, llm-capability-eval, multi-agent-collusion | [approach_map_mech_substitution.md](approach_map_mech_substitution.md) |
| surface-rule | 8 | 9 | game-and-chess, llm-generative-text | [approach_map_mech_surface_rule.md](approach_map_mech_surface_rule.md) |
| theory | 5 | 6 | foundations-theory | [approach_map_mech_theory.md](approach_map_mech_theory.md) |
| timing | 2 | 2 | foundations-theory, game-and-chess | [approach_map_mech_timing.md](approach_map_mech_timing.md) |

## Mechanisms

| mechanism | parent | class | name | definition | grounded by | landing | approaches |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `m-acoustic-signal` | m-side-signal | side-signal | Acoustic signal | A sound, or its absence, relays the information. | `boonstra_2024:surveyed-trash-can-code-b` | yes | 1 |
| `m-activation-probe` | m-detection | detection | Activation probes (not a landing node) | Probes on hidden states reconstruct the secret or read deception, calibrated to a false-positive rate. | `westphal_2026:probe-detector-all-layer-rule` | no | 2 |
| `m-active-warden` | m-detection | detection | Active-warden defences (not a landing node) | The overseer rewrites the message, for example by paraphrasing it while keeping its meaning, to destroy any payload instead of only detecting it. | `roger_2023:approach-paraphrase-defence` | no | 3 |
| `m-adversarial-costs` | m-cost-based-embedding | cover-modification | Steganalyser-gradient cost adjustment | Embedding costs are adjusted by the gradients of a target CNN steganalyser so that the stego image also fools it. | `tang_2019:approach-adv-emb` | yes | 1 |
| `m-adversarial-text-editing` | m-media-embedding | media-embedding | Adversarially trained text editing | A jointly and adversarially trained encoder-decoder transformer takes a text and a binary message and outputs the text unobtrusively modified. | `zhang_2021b:surveyed-adversarial-watermarking-transformer` | yes | 1 |
| `m-adversarial-training` | m-media-embedding | media-embedding | Adversarially trained hiding | Containers and covers are fed to an adversarial model, making training a three-player game. | `zhang_2021b:surveyed-adversarial-architecture` | yes | 3 |
| `m-adversary-decoding` | m-detection | detection | Adversary decoding attempts (not a landing node) | Near-copies of the decoder, trained with minor variations, try to recover the message rather than just flag it. | `agarwal_2023:hypersteg-near-copy-decoders-fail` | no | 0 |
| `m-agentic-construction-eval` | m-evaluation | evaluation | Agentic stegosystem construction (not a landing node) | A tool-using agent must build a working natural-language stegosystem. | `rippin_2026:approach-agentic-covert-channel-construction` | no | 1 |
| `m-associated-term-substitution` | m-substitution | substitution | Associated-term substitution | The payload is replaced by a closely associated term, such as the name of a product that implements it. | `karpov_2025:capacity-semantic-association` | yes | 1 |
| `m-attack-simulated-training` | m-media-embedding | media-embedding | Attack-simulated training | Containers are distorted by simulated attacks during training before they reach the reveal network, so the mark survives them. | `zhang_2021b:surveyed-noise-augmentation-watermarking` | yes | 4 |
| `m-authentic-record-selection` | m-cover-selection | cover-selection | Authentic-record selection | Moves from unaltered, authenticated real games are chosen so that their data carry the message. | `desoky_2009:target-square-index` | yes | 1 |
| `m-authenticate-then-act` | m-collusion-signal | collusion-signal | Authenticate, then act | Players covertly authenticate those they may collude with, then follow an algorithm that acts on the authentication so as to win the competition. | `murdoch_2004:approach-league-collusion-strategy` | yes | 1 |
| `m-balanced-partition` | m-partition-codes | sampling | Near-equiprobable partition | The cover space is split into parts of approximately equal probability mass and the message bit picks the part to sample from. | `cachin_1998:approach-balanced-partition` | yes | 3 |
| `m-byte-encoding` | m-overt-encoding | overt-encoding | Byte encodings | The message is written as Base64, UTF-8 binary or hexadecimal, possibly with bit swaps, rotations or repeated application. | `zolkowski_2025:surveyed-byte-encodings` | yes | 5 |
| `m-capacity-laws` | m-theory | theory | Capacity laws (not a landing node) | Under stated assumptions (covers of uniform capacity, a quantitative steganalyser) and asymptotically, secure capacity grows only as the square root of the number of covers. | `ker_2007:approach-batch-square-root-capacity` | no | 2 |
| `m-character-variant` | m-substitution | substitution | Character-variant substitution | A variant character, such as a Unicode variant of an asterisk, replaces a string that a monitor penalises. | `skaf_2025:arithmetic-semantic-substitutes` | yes | 1 |
| `m-chess-language-models` | m-foundation | foundation | Chess language models and datasets (not a landing node) | Models trained on chess games paired with chess text. | `feng_2023:approach-chessgpt` | no | 3 |
| `m-codebook` | m-selection | selection | Codebook choice | An agreed table maps message values to a finite set of expressions, so that the one used codifies the bits. | `hernandezcastro_2006:comment-codebook` | yes | 11 |
| `m-codeword-substitution` | m-substitution | substitution | Codeword substitution | Agreed codewords, which need not be synonyms, stand in for the hidden states. | `anwar_2026:surveyed-codeword-codebook` | yes | 4 |
| `m-collusion-benchmark` | m-evaluation | evaluation | Collusion audits and benchmarks (not a landing node) | Frameworks that audit collusion through outcome metrics and conversation logs. | `nakamura_2026:approach-colosseum` | no | 2 |
| `m-collusion-signal` | — | collusion-signal | Collusion signals | An agreed or salient feature of the input or of the output tells a colluding party when or how to act; often a one-bit message. | `greenblatt_2023:control-input-and-action-collusion` | yes | 6 |
| `m-combinatorial-subset-index` | m-selection | selection | Combinatorial subset index | A combinatorial number system converts the data into a choice of a set of units, and a target location for them can carry more. | `hahn_2015:combinatorial-selection-encoding` | yes | 1 |
| `m-commentary-evaluation` | m-foundation | foundation | Commentary evaluation (not a landing node) | An LLM evaluates chess commentary. | `kim_2024:approach-gcc-eval` | no | 1 |
| `m-commentary-generation` | m-foundation | foundation | Commentary generation (not a landing node) | Neural systems that generate commentary text for chess moves. | `jhamtani_2018:approach-gac` | no | 2 |
| `m-complexity-theoretic-security` | m-theory | theory | Complexity-theoretic security (not a landing node) | Security is computational indistinguishability; one-way functions suffice for secure steganography. | `hopper_2002:computational-indistinguishability-owf` | no | 1 |
| `m-concept-lens` | m-detection | detection | Concept-lens readout (not a landing node) | Concepts read through a Jacobian lens are compared across agents to find colluding pairs. | `molinari_2026:approach-j-pact` | no | 2 |
| `m-control-evaluation` | m-evaluation | evaluation | Control evaluations (not a landing node) | Protocols meant to stay safe despite intentional subversion are evaluated. | `greenblatt_2023:approach-control-evaluation` | no | 1 |
| `m-coordination` | — | coordination | Coordination without a message (not a landing node) | Parties collude or coordinate their actions, whether or not they communicate with each other; the distinction between explicit and tacit collusion may break down for agents. | `hammond_2025:explicit-tacit-distinction-breaks-down` | no | 4 |
| `m-coordination-eval` | m-evaluation | evaluation | Focal-point evaluations (not a landing node) | Studies of how, when and why focal points emerge in models, compared with humans. | `aharon_2026:approach-focal-point-evaluation` | no | 2 |
| `m-coordination-learning` | m-foundation | foundation | Symmetry-robust coordination learning (not a landing node) | Self-play against randomly relabelled, symmetry-equivalent copies of the partner, so agents coordinate with partners they have not met. | `hu_2020:other-play-objective` | no | 1 |
| `m-cost-based-embedding` | m-cover-modification | cover-modification | Cost-based embedding | Each modification of a cover element carries a cost, and the message is embedded under the conventional framework of distortion minimisation. | `tang_2019:approach-adv-emb` | yes | 1 |
| `m-count-code` | m-surface-rule | surface-rule | Count codes | The count of some unit in successive segments of text (words or characters per sentence, letters per word), taken modulo the number of states, carries each state. | `zolkowski_2025:surveyed-state-tracking-encodings` | yes | 2 |
| `m-coupling` | m-sampling | sampling | Coupling codes | Ciphertext that looks uniformly random is joined to the cover distribution by a coupling, so the published symbol follows the cover distribution. | `schroederdewitt_2022:approach-imec` | yes | 3 |
| `m-cover-conditioned-encoder` | m-media-embedding | media-embedding | Cover-conditioned encoder | The encoder takes the cover as well as the message, so the embedding depends on the cover; HiDDeN, for instance, concatenates the spatially replicated message to its intermediate representation of the cover. | `zhu_2018:approach-hidden` | yes | 2 |
| `m-cover-modification` | — | cover-modification | Cover modification | An existing cover is altered so that the alterations carry the message, exploiting limits of the warden such as human perception. | `motwani_2024:taxonomy-covertext-vs-it` | yes | 3 |
| `m-cover-selection` | — | cover-selection | Cover selection | An unmodified object is chosen because its own attributes map to the message under an agreed rule. | `qin_2019:coverless-definition` | yes | 10 |
| `m-decoder-finetune-mark` | m-generation-time-watermark | generative-synthesis | Fine-tuned decoder mark | The latent decoder of a diffusion model is fine-tuned so that every generated image carries a fixed binary signature. | `fernandez_2023:approach-stable-signature` | yes | 1 |
| `m-detection` | — | detection | Detectors, monitors and defences (not a landing node) | Methods that detect, measure, remove or read hidden communication. | `hernandezcastro_2006:approach-game-steganalysis` | no | 13 |
| `m-diffusion-translation` | m-generative-synthesis | generative-synthesis | Diffusion translation | A pre-trained conditional diffusion model, with different conditions in its forward and backward processes, translates a secret image into a container without additional training. | `yu_2023:approach-cross` | yes | 1 |
| `m-distribution-copies` | m-sampling | sampling | Distribution copies | Copies of the token distribution are made by rotating its intervals, and the message decides which copy the token is sampled from. | `ding_2023:distribution-copies` | yes | 1 |
| `m-emergent-convention` | m-coordination | coordination | Conventions emerging in interaction (not a landing node) | Agents exchange symbols with no predefined interpretation, and any meaning emerges endogenously through interaction. | `buscemi_2026:ten-number-covert-carrier` | no | 2 |
| `m-encoded-reasoning-task` | m-evaluation | evaluation | Encoded reasoning task (not a landing node) | Models are evaluated on encoding their reasoning. | `zolkowski_2025:approach-encoded-reasoning-eval` | no | 1 |
| `m-engine-benchmark-assessment` | m-human-move-models | foundation | Engine-match assessment (not a landing node) | Whether a player's move matches an engine's choice is counted, and this can detect or be gamed by cheaters. | `biswas_2015:surveyed-move-matching` | no | 4 |
| `m-engine-ranked-index` | m-ordered-choice-index | selection | Engine-ranked index | A shared engine lists the moves scoring above a threshold T, sorts them by evaluation, and playing the i-th sends i. | `hernandezcastro_2006:approach-ranked-move-choice` | yes | 2 |
| `m-entity-tree-class` | m-semantic-content | selection | Ontology-entity semantic space | A semantic space is built from ontology-entity trees and secret messages are mapped onto it, without altering how the model samples. | `bai_2024:approach-semantic-steganography` | yes | 1 |
| `m-equivalent-choice` | m-ordered-choice-index | selection | Equivalent-alternative choice | Among alternatives that can be shown not to change the outcome, the one played transmits information, and the receiver identifies which it was. | `murdoch_2004:equivalent-move-channel` | yes | 2 |
| `m-eval-framework` | m-evaluation | evaluation | Evaluation frameworks (not a landing node) | Software frameworks and decompositions that organise capability measurement. | `motwani_2024:approach-case-framework` | no | 2 |
| `m-evaluation` | — | evaluation | Evaluations, benchmarks and elicitation conditions (not a landing node) | Frameworks and conditions that measure or elicit hiding, or classify risks, rather than hide anything. | `motwani_2024:approach-case-framework` | no | 22 |
| `m-feature-hash-selection` | m-cover-selection | cover-selection | Feature-hash selection | Images in a database are indexed by hash sequences of their features, and images whose hashes equal the message segments are sent. | `qin_2019:surveyed-gray-hash-selection` | yes | 4 |
| `m-feature-steganalysis` | m-detection | detection | Statistical feature steganalysis (not a landing node) | Statistical attacks detect significant deviations from a model of the cover caused by inserting hidden data. | `hernandezcastro_2006:approach-game-steganalysis` | no | 2 |
| `m-feedback-coding` | m-sampling | sampling | Feedback (posterior-matching) coding | Every generated token is observed by both parties, so generation is a channel with noiseless feedback and each token guides the next embedding step. | `guo_2026:generation-as-feedback-channel` | yes | 1 |
| `m-file-attribute-mapping` | m-cover-selection | cover-selection | File-attribute category mapping | Values of a file attribute are divided into categories, each mapped to a secret message, and files are chosen by category. | `qin_2019:surveyed-gif-attributes` | yes | 1 |
| `m-fixed-bins` | m-partition-codes | sampling | Fixed shared bins | A shared random partition of the vocabulary into equal-sized bins lets the bin of each token carry a fixed-length block of ciphertext. | `dai_2019:surveyed-bins` | yes | 1 |
| `m-focal-magic-number` | m-output-signal | collusion-signal | Focal magic numbers | A number made salient by world knowledge (a famous prime, a constant from a novel or a game) serves as the signal. | `jarviniemi_2025:coding-magic-numbers` | yes | 1 |
| `m-focality-prompt` | m-evaluation | evaluation | Focality prompts (not a landing node) | A prompt tells the model which kind of salience to aim at. | `aharon_2026:surveyed-saliency-prompt` | no | 3 |
| `m-foundation` | — | foundation | Non-steganographic foundations (not a landing node) | Work on chess language, chess play, human move choice, hyperbolic geometry and coordination learning that hides nothing. | `feng_2023:approach-chess-language-benchmark` | no | 36 |
| `m-free-task-choice` | m-selection | selection | Free choices within a task | Choices a task leaves open, repetitive and supposedly arbitrary or unimportant ones such as variable names, serve as the carrier, the option taken carrying the information. | `schulz_2026:arbitrary-choice-covers` | yes | 1 |
| `m-game-record-inference` | m-detection | detection | Game-record inference (not a landing node) | An inference engine analyses the bidding and play in complete game records to detect collusive play. | `yan_2010:approach-inference-engine-collusion-detector` | no | 1 |
| `m-game-statistics` | m-feature-steganalysis | detection | Game-statistics attacks (not a landing node) | Game length, playing level and result are tested for deviations caused by embedding. | `hernandezcastro_2006:approach-game-steganalysis` | no | 1 |
| `m-generation-time-watermark` | m-generative-synthesis | generative-synthesis | Generation-time watermark | The mark is introduced while a generative model produces the image, through the model's parameters or its sampling input. | `fernandez_2023:approach-stable-signature` | yes | 2 |
| `m-generative-synthesis` | — | generative-synthesis | Generative synthesis of media | A shared generator produces the container directly from the message, so no cover is modified, and an extractor recovers the message. | `zhang_2021b:surveyed-synthesis-generative` | yes | 10 |
| `m-generator-model-database` | m-generative-synthesis | generative-synthesis | Generator-model database | A database of generative models turns a secret image into an unrelated-looking image and back. | `qin_2019:surveyed-wgan-model-database` | yes | 1 |
| `m-grille-inpainting` | m-generative-synthesis | generative-synthesis | Grille and inpainting | A shared mask (a digital Cardan grille) marks where the message is written and a generator completes the rest of the image. | `zhang_2018:approach-cardan-grille-inpainting` | yes | 1 |
| `m-huffman-every-step` | m-prefix-codes | sampling | Huffman at every step | A Huffman code over the vocabulary is rebuilt at every step and followed bit by bit from the root to a leaf token. | `dai_2019:surveyed-vlc-huffman` | yes | 1 |
| `m-huffman-patient` | m-prefix-codes | sampling | Thresholded (patient) Huffman | The Huffman code is used only at steps where its total variation distance from the model's distribution is small enough; otherwise the step samples from the model and waits. | `dai_2019:approach-patient-huffman` | yes | 1 |
| `m-human-move-models` | m-foundation | foundation | Models of human move choice (not a landing node) | Models of chess skill measured by the quality of the moves played. | `regan_2011:approach-intrinsic-rating-model` | no | 11 |
| `m-hyperbolic-blending` | m-media-embedding | media-embedding | Hyperbolic blending | Message and carrier features are mapped to the Poincare ball, concatenated in the tangent space and mapped back to the ball. | `agarwal_2023:hypersteg-poincare-beta-concatenation` | yes | 1 |
| `m-hyperbolic-embeddings` | m-foundation | foundation | Hyperbolic embeddings and measurement (not a landing node) | Data are embedded in hyperbolic space to represent hierarchy. | `nickel_2017:approach-poincare-embeddings` | no | 8 |
| `m-hyperbolic-networks` | m-foundation | foundation | Hyperbolic network layers and agents (not a landing node) | Neural network operations defined in hyperbolic geometry. | `ganea_2018:approach-hyperbolic-neural-networks` | no | 6 |
| `m-hyperplane-buckets` | m-partition-codes | sampling | Hyperplane buckets | A random hyperplane in the embedding space splits the vocabulary into two buckets, and each output token carries one bit by the bucket it falls in. | `westphal_2026:hyperplane-bucket-encoding` | yes | 1 |
| `m-informal-limits` | m-theory | theory | Informal limits and terminology (not a landing node) | A survey-level account of what steganography is and can do. | `anderson_1998:approach-limits-of-steganography` | no | 1 |
| `m-information-theoretic-security` | m-theory | theory | Information-theoretic security (not a landing node) | Detection is a hypothesis test, and security is the relative entropy between cover and stego distributions. | `cachin_2004:relative-entropy-security` | no | 2 |
| `m-initial-class` | m-surface-rule | surface-rule | Initial-class codes | The class of a token's initial letter (A-M against N-Z) carries a bit, rather than the letter itself. | `tailor_2026:surveyed-word-length-parity-token-initials` | yes | 1 |
| `m-initial-noise-mark` | m-generation-time-watermark | generative-synthesis | Initial-noise mark | A pattern is written into the Fourier transform of the initial noise vector used for sampling, with no change to the model. | `wen_2023:approach-tree-ring` | yes | 1 |
| `m-input-trigger` | m-collusion-signal | collusion-signal | Input-feature trigger (not a landing node) | Both colluders misbehave only when an agreed feature is present in the input, so no message passes between them. | `greenblatt_2023:approach-input-collusion` | no | 1 |
| `m-insertion-parameters` | m-selection | selection | Optional-insertion parameters | Optional material added to a record (a variation in a played game) carries bits by where it begins, how long it is, and the choices within it. | `hernandezcastro_2006:variation-carrier` | yes | 1 |
| `m-interval-adaptive-truncation` | m-interval-coding | sampling | Interval coding with per-step truncation | Arithmetic coding over a neural LM in which the number of candidate tokens kept, fixed in earlier work, is re-chosen at each step. | `shen_2020:approach-saac` | yes | 1 |
| `m-interval-coding` | m-sampling | sampling | Interval (range or arithmetic) coding | The message, read as a number, is decoded into symbols by partitioning a range in proportion to the model's probabilities: arithmetic coding run in reverse. | `ziegler_2019:reverse-arithmetic-coding` | yes | 4 |
| `m-interval-keyed-randomness` | m-interval-coding | sampling | Keyed sampling-randomness embedding | Message bits stand in for the random number used to sample each token, masked afresh at every sampling event by a generator keyed with state the two parties share. | `kaptchuk_2021:fresh-prg-mask` | yes | 1 |
| `m-interval-plain` | m-interval-coding | sampling | Plain range partition over a fixed model | At each step the range is partitioned to match the model's outbound probabilities and the symbol whose subrange contains the message number is emitted. | `moraldo_2014:approach-markov-range-partition` | yes | 2 |
| `m-intrinsic-rating` | m-human-move-models | foundation | Intrinsic rating models (not a landing node) | Formulas represent playing strength by the quality of moves played, fitted by regression. | `regan_2011:approach-intrinsic-rating-model` | no | 4 |
| `m-invertible-encoder` | m-media-embedding | media-embedding | Invertible encoder-decoder | An invertible network performs encoding and decoding as reciprocal processes with shared parameters. | `chen_2023:approach-wavmark` | yes | 1 |
| `m-item-inclusion-bits` | m-free-task-choice | selection | Item in/out bits | The in/out choices of the first items of a task solution encode a number in binary, one bit per item (the knapsack cover). | `schulz_2026:formatting-and-knapsack-carriers` | yes | 1 |
| `m-key-establishment` | — | key-establishment | Covert key establishment without a pre-shared secret | Ciphertext under the recipient's public key, such as a session key, is carried in the cover, so parties who share no secret can still communicate covertly. | `anderson_1998:approach-public-key-steganography` | yes | 2 |
| `m-keyed-parity` | m-cover-modification | cover-modification | Keyed-set parity | A pad or keystream selects a set of cover elements and each ciphertext bit is embedded as their parity. | `anderson_1998:approach-parity-embedding` | yes | 1 |
| `m-keyed-play-convention` | m-selection | selection | Signalling keyed by private knowledge | Partners encode information in the plays they choose, and a secret they share but opponents lack (what each holds) acts as a key. | `murdoch_2004:bridge-shared-secret-key` | yes | 1 |
| `m-keyed-strategy-set-index` | m-ordered-choice-index | selection | Keyed strategy-set coding | The set of best moves is permuted by a shared random number generator and seed, and message bits are consumed as an index into the permuted set. | `ritchey_2012:permuted-best-move-index` | yes | 1 |
| `m-keyword-set-index` | m-semantic-content | selection | Keyword-set index | Keyword sets are expanded by repeated sampling in proportion to probability, and the location index of each keyword in the expanded set encodes message bits. | `wu_2024:augmented-keyword-index-mapping` | yes | 1 |
| `m-latent-mapping` | m-generative-synthesis | generative-synthesis | Message-to-latent mapping | Secret bits are mapped to the generator's noise vector and a trained extractor recovers them from the generated image. | `hu_2018:approach-dcgan-swe` | yes | 3 |
| `m-latent-search` | m-generative-synthesis | generative-synthesis | Latent search | The generator's latent space is searched for the encoding whose output carries the message. | `zhang_2018:approach-gss` | yes | 1 |
| `m-learned-tacit-collusion` | m-coordination | coordination | Learned tacit collusion (not a landing node) | Algorithms adapt their strategies to collude through interaction, without the parties communicating. | `hammond_2025:surveyed-algorithmic-pricing-collusion` | no | 1 |
| `m-length-parity` | m-count-code | surface-rule | Word-length parity | The parity of each word's length carries one bit. | `tailor_2026:word-length-parity-capacity` | yes | 1 |
| `m-letter-position` | m-surface-rule | surface-rule | Letter-position codes (acrostics) | Message letters are placed at agreed positions, such as the first letter of each sentence, of alternate sentences or of every third word. | `zolkowski_2025:surveyed-letter-position-acrostics` | yes | 6 |
| `m-letter-substitution-cipher` | m-overt-encoding | overt-encoding | Letter rotation and substitution ciphers | Each letter is rotated by N places or replaced under a provided character mapping. | `zolkowski_2025:surveyed-rotation-substitution` | yes | 4 |
| `m-likelihood-ratio-forensics` | m-detection | detection | Hypothesis-comparison forensics (not a landing node) | The hypothesis that a specified method was used to transmit information is weighed against the hypothesis that it was not. | `boonstra_2024:likelihood-ratio-detector` | no | 1 |
| `m-literal-payload-name` | m-surface-rule | surface-rule | Literal payload as a name or acronym | The payload is written directly into the text as an imagined acronym or name. | `roger_2023:acronym-literal-payload` | yes | 1 |
| `m-llm-chess-play` | m-foundation | foundation | LLM chess play (not a landing node) | Benchmarks of how well language models play chess. | `kolasani_2025:approach-llm-chess-benchmark` | no | 1 |
| `m-llm-classifier` | m-detection | detection | LLM classifiers (not a landing node) | A fine-tuned LLM judges whether a text carries hidden data. | `tang_2024:approach-lsgc` | no | 2 |
| `m-maximal-coupling-public-draft` | m-coupling | sampling | Maximal coupling through a public draft model | A small public draft model that both parties run on the public transcript partitions the vocabulary into buckets, and a maximal coupling samples the published token exactly from the sender's private distribution. | `pang_2026:draft-buckets-maximal-coupling` | yes | 1 |
| `m-media-embedding` | — | media-embedding | Learned media embedding | Trainable networks hide data in an existing image or audio signal and recover it. | `zhu_2018:approach-hidden` | yes | 14 |
| `m-message-passing-task` | m-evaluation | evaluation | Encoded message-passing task (not a landing node) | An encoder hides a secret message in its answer to a cover task for a decoder copy of itself, while a monitor judges suspicion. | `zolkowski_2025:setting-encoder-decoder-monitor` | no | 3 |
| `m-min-entropy-coupling` | m-coupling | sampling | Minimum-entropy coupling | An iterative minimum-entropy coupling joins uniform ciphertext to an autoregressively specified cover distribution. | `schroederdewitt_2022:imec-coding` | yes | 1 |
| `m-mixed-radix-index` | m-selection | selection | Mixed-radix index over all legal options | Options at each position are sorted deterministically and each position is treated as a base-n digit, n being the number of options, until the message integer is consumed. | `barai_2026:mixed-radix-legal-move-index` | yes | 1 |
| `m-move-timing` | m-timing | timing | Move timing | The sender delays making a move and the recipient measures the delay. | `murdoch_2004:move-timing-channel` | yes | 1 |
| `m-neural-human-move` | m-human-move-models | foundation | Neural human-move predictors (not a landing node) | Networks trained on human games predict the move a human played. | `mcilroyyoung_2020:approach-maia` | no | 3 |
| `m-non-text-statistical-detection` | m-feature-steganalysis | detection | Entropy of non-text messages (not a landing node) | Covert messages are detected by their lower entropy than random baselines. | `buscemi_2026:entropy-ordering-detection` | no | 0 |
| `m-opening-and-engine-analysis` | m-foundation | foundation | Engine and opening analysis (not a landing node) | Engines and game databases measure opening diversity or variant balance. | `tomasev_2020:approach-prior-entropy-diversity` | no | 3 |
| `m-ordered-choice-index` | m-selection | selection | Move-choice indexing (ordered alternatives) | A prearranged criterion orders a set of acceptable alternatives, and the index of the one played sends that value. | `hernandezcastro_2006:both-embed-and-prior-art` | yes | 5 |
| `m-orientation-signal` | m-side-signal | side-signal | Orientation signal | The orientation in which an object is placed (a card led horizontally or vertically) carries the information. | `boonstra_2024:surveyed-card-orientation-code-c` | yes | 1 |
| `m-output-signal` | m-collusion-signal | collusion-signal | Output signal | The sender puts an agreed mark in its own output, such as a variable name or a loop form, so the receiver knows to act. | `greenblatt_2023:approach-action-collusion-code-signal` | yes | 3 |
| `m-overt-encoding` | — | overt-encoding | Overt encodings and ciphers | The message is transformed by a standard encoding or cipher and written into the text, which hides its content but not that something is encoded. | `tailor_2026:surveyed-base64` | yes | 8 |
| `m-partial-word-cipher` | m-letter-substitution-cipher | overt-encoding | Partial word-level cipher | Rot13 is applied to each word independently with probability p, interpolating between legible and fully enciphered text. | `anwar_2026:surveyed-rot13-partial-encoding` | yes | 1 |
| `m-partition-codes` | m-sampling | sampling | Partition codes | The symbol space is split into groups and the message chooses the group from which the next symbol is drawn. | `cachin_2004:approach-balanced-partition` | yes | 5 |
| `m-patch-retrieval` | m-cover-selection | cover-selection | Partial-duplicate patch retrieval | Natural images sharing patches with a secret image are retrieved and sent, and the receiver stitches the patches back together. | `qin_2019:surveyed-partial-duplicates` | yes | 2 |
| `m-payoff-anchored-symbols` | m-collusion-signal | collusion-signal | Payoff-anchored numeric signals | Numeric messages reuse values drawn from the payoff structure of the game both parties play, converging on a compact, low-entropy set of signalling symbols. | `buscemi_2026:payoff-anchored-decimal-code` | yes | 1 |
| `m-phrase-codebook` | m-codebook | selection | Phrase codebook | Each possible message is associated with a fixed phrase, such as an answer introduction, and the receiver finds which phrase was used. | `roger_2023:surveyed-introduction-variations` | yes | 4 |
| `m-physical-channel-training` | m-attack-simulated-training | media-embedding | Physical-channel training | The simulated distortions are those of real printing, display and photography. | `tancik_2019:approach-stegastamp` | yes | 2 |
| `m-pointer-code` | m-reference-code | selection | Pointer (book-cipher) code | Sender and receiver share a book and encipher the message as a series of pointers to its words. | `anderson_1998:selection-channel-book-cipher` | yes | 1 |
| `m-policy-identity` | m-selection | selection | Policy identity | Each message symbol has its own agent, and the receiver decodes by identifying which agent produced the observed episode. | `chang_2024:approach-action-steganography` | yes | 1 |
| `m-prefix-codes` | m-sampling | sampling | Prefix-code (Huffman) sampling | A prefix code built from the model's distribution at each step is walked by the message bits to choose a token. | `dai_2019:surveyed-vlc-huffman` | yes | 2 |
| `m-prompted-llm-monitor` | m-detection | detection | Prompted LLM monitor (not a landing node) | A model given the cover task and answer, but not the secret, is told to rate suspicion, and a threshold set at a fixed false-positive rate decides. | `zolkowski_2025:monitor-threshold-fpr` | no | 1 |
| `m-pseudorandom-watermark-code` | m-sampling | sampling | Key-correlated sampling randomness | The model's sampling randomness is correlated with a secret key instead of its distribution being changed, and the watermark is extended to carry a payload. | `zamir_2024:builds-on-cgz` | yes | 1 |
| `m-public-key-block-parity` | m-key-establishment | key-establishment | Public-key ciphertext as block parity | The message is encrypted under the recipient's public key and embedded as the parities of successive cover blocks. | `anderson_1998:approach-public-key-steganography` | yes | 1 |
| `m-punctuation-symbol` | m-surface-rule | surface-rule | Punctuation and special-character codes | The choice of terminal punctuation, or of special characters inserted into the text, carries each state. | `zolkowski_2025:surveyed-state-tracking-encodings` | yes | 1 |
| `m-reasoning-behaviour-choice` | m-semantic-content | selection | Reasoning-behaviour choice | Each reasoning step carries a bit in which high-level reasoning behaviour it shows rather than in its words. | `zhou_2026:approach-conceptual-steganography` | yes | 1 |
| `m-recursive-balanced-grouping` | m-balanced-partition | sampling | Recursive near-equiprobable grouping | At each step the vocabulary is grouped adaptively into groups of approximately equal probability, the message chooses a group, and the operation repeats within it. | `zhang_2021:adg-adaptive-dynamic-grouping` | yes | 1 |
| `m-reference-code` | m-codebook | selection | Reference code into shared data | Message values are sent as references to items of shared data both parties hold, such as pointers to the words of a shared book. | `anderson_1998:selection-channel-book-cipher` | yes | 3 |
| `m-rejection-keyed-stateful` | m-rejection-sampling | sampling | Keyed, bounded rejection sampling | For each bit, at most two channel blocks are drawn, looking for one whose keyed pseudorandom function value F_K(N, c) equals the bit; the protocol is stateful. | `hopper_2002:approach-stateful-rejection-sampling` | yes | 1 |
| `m-rejection-public-unbiased` | m-rejection-sampling | sampling | Rejection sampling with a public unbiased function | A public function, assumed unbiased on the channel, decides whether a sampled block carries the next bit; the assumption does not hold for every channel. | `hopper_2002:approach-stateless-unbiased-function` | yes | 1 |
| `m-rejection-sampling` | m-sampling | sampling | Rejection sampling | Channel samples are drawn until a keyed or public function of one equals the next message bit; in the bounded form at most a fixed number of draws is made, trying to find a match. | `hopper_2002:rejection-sampling-prf` | yes | 2 |
| `m-repetition-rank-exchange` | m-cover-modification | cover-modification | Repetition-rank block exchange | In the ranking of a repetition-times compressor, a low-probability source block is kept or swapped for the block immediately following it, depending on the embedded bit. | `cachin_1998:approach-universal-repetition-times` | yes | 1 |
| `m-residual-encoder` | m-media-embedding | media-embedding | Residual encoder | The encoder outputs a residual image that is added back to the cover; the message enters as an extra input channel. | `tancik_2019:residual-encoder` | yes | 1 |
| `m-risk-taxonomy` | m-evaluation | evaluation | Risk taxonomies (not a landing node) | Multi-agent risks are sorted into failure modes and risk factors. | `hammond_2025:approach-multi-agent-risk-taxonomy` | no | 1 |
| `m-robust-feature-function` | m-sampling | sampling | Keyed function of a robust document feature | A keyed function f picks the shingle of each document that maximises it, giving a protocol robust against a particular class of edits on text-like channels. | `hopper_2002:approach-robust-text-shingling` | yes | 1 |
| `m-sampled-lattice-key-exchange` | m-key-establishment | key-establishment | Lattice key exchange in honest samples | MLWE ciphertext coefficients are carried as small displacements in blocks that are honest samples from the sender's model, so that independently deployed agents agree a key. | `pang_2026:mlwe-steganographic-key-exchange` | yes | 1 |
| `m-sampling` | — | sampling | Distribution-steered sampling codes | The message is embedded in how each symbol is sampled from a model's distribution, for example in the random number used to sample, and the receiver recovers it from the distribution or the randomness. | `kaptchuk_2021:embed-in-sampling-randomness` | yes | 23 |
| `m-schelling-choice` | m-coordination | coordination | Schelling-point choice of scheme (not a landing node) | Of the many possible schemes, some are salient (named in the prompt, in a shared file system, common in training), and isolated parties converge on them. | `rippin_2026:focal-point-salience` | no | 1 |
| `m-scheme-discovery-condition` | m-evaluation | evaluation | Scheme-discovery condition (not a landing node) | The model is asked to think of a scheme for the task, use it, and later re-derive it to decode. | `roger_2023:surveyed-scratchpad-scheme` | no | 2 |
| `m-secret-conditioned-generator` | m-generative-synthesis | generative-synthesis | Secret-conditioned generator | A secret block inside the generator writes the secret data into its feature maps during image generation. | `wei_2022:approach-gsn` | yes | 1 |
| `m-selection` | — | selection | Enumerated-choice codes | At each decision point the sender's rule yields a set of admissible alternatives, a bit string is assigned to each, and the one whose string matches the next data appears. | `ritchey_2012:approach-combinatorial-game-framework` | yes | 24 |
| `m-semantic-content` | m-selection | selection | Semantic-content choice | The message selects what the generated text is about or does (its keywords, its semantic class, or the reasoning behaviour of a step) rather than its wording, and a model writes text with that content. | `bai_2024:approach-semantic-steganography` | yes | 3 |
| `m-shared-sample-robust` | m-sampling | sampling | Shared-sample robust coding | Channel draws made with pseudorandom inputs that sender and receiver share stand in for shared blocks and lower the decoding error, so that robust hiding is possible against any admissible warden relation. | `hopper_2002:approach-universally-robust` | yes | 1 |
| `m-side-signal` | — | side-signal | Out-of-band physical signals | An agreed physical act outside the moves of the game carries the information. | `boonstra_2024:surveyed-card-orientation-code-c` | yes | 2 |
| `m-spectral-audio-hiding` | m-media-embedding | media-embedding | Spectral speech hiding | STFT and inverse-STFT layers inside the network let speech be hidden in speech. | `kreuk_2019:approach-hide-and-speak` | yes | 2 |
| `m-stated-value-code` | m-codebook | selection | Stated-value code | The text states a number determined by the message, such as an age, and the receiver reads the integer and looks up its message. | `roger_2023:surveyed-age-instructions` | yes | 1 |
| `m-stateless-subversion-eval` | m-evaluation | evaluation | Stateless subversion evaluation (not a landing node) | Systems must generate and act on their own strategies for subverting control protocols without shared memory between contexts. | `mallen_2024:approach-subversion-strategy-eval` | no | 1 |
| `m-substitution` | — | substitution | Substitution codes | An agreed or commonly known stand-in replaces a word, phrase, string or symbol in otherwise ordinary text, and which stand-in appears carries the message. | `xiang_2018:ss-carrier-substitution-sets` | yes | 9 |
| `m-surface-formatting` | m-surface-rule | surface-rule | Surface-formatting codes | Each formatting unit (a word, a whitespace run or a sentence) carries one symbol from the start of the answer, leaving the meaning of the text untouched. | `schulz_2026:formatting-and-knapsack-carriers` | yes | 1 |
| `m-surface-rule` | — | surface-rule | Surface-feature rule codes | An explicit rule maps message symbols onto positional, countable or typographic features of the text, such as first letters, sentence lengths or punctuation. | `zolkowski_2025:surveyed-state-tracking-encodings` | yes | 9 |
| `m-synonym-matrix-embedding` | m-synonym-substitution | substitution | Matrix embedding over synonyms | Matrix embedding raises embedding efficiency by reducing the number of synonym substitutions needed. | `xiang_2018:ss-scheme-family` | yes | 1 |
| `m-synonym-multibase` | m-synonym-substitution | substitution | Multi-base synonym coding | Synonyms taken from WordNet are encoded by a multi-base coding method. | `xiang_2018:ss-carrier-substitution-sets` | yes | 1 |
| `m-synonym-stc` | m-synonym-substitution | substitution | Syndrome-trellis-coded synonym substitution | A double-layered syndrome-trellis code chooses the substitutions so as to minimise statistical and linguistic distortion. | `xiang_2018:ss-scheme-family` | yes | 1 |
| `m-synonym-substitution` | m-substitution | substitution | Synonym substitution | Interchangeable synonyms form substitution sets, and the choice among them in a cover text carries the bits. | `xiang_2018:ss-carrier-substitution-sets` | yes | 3 |
| `m-synonym-vertex-coding` | m-synonym-substitution | substitution | Vertex coding of synonyms | Collected synonyms are encoded into unrepeated bit strings by vertex coding. | `xiang_2018:ss-scheme-family` | yes | 1 |
| `m-text-feature-steganalysis` | m-feature-steganalysis | detection | Text feature steganalysis (not a landing node) | Semantic features of word choice, such as synonym context fitness, feed a classifier. | `xiang_2018:approach-wes` | no | 1 |
| `m-theory` | — | theory | Security definitions, limits and capacity laws (not a landing node) | Definitions of undetectability and results on how much can be hidden; no scheme is judged against them. | `cachin_2004:approach-information-theoretic-model` | no | 6 |
| `m-timing` | — | timing | Timing channels | The times at which symbols are sent carry the information, not their content. | `hopper_2002:timestamped-channel` | yes | 2 |
| `m-token-partition-watermark` | m-sampling | sampling | Token-partition (red-green) watermark codes | The message seeds or selects a split of tokens into favoured and disfavoured sets, biasing sampling, and the decoder picks the message whose split scores highest. | `roger_2023:surveyed-cycle-shifting-watermark` | yes | 2 |
| `m-training-elicitation` | m-evaluation | evaluation | Training-based elicitation (not a landing node) | RL fine-tuning against a task reward and a monitor penalty is used to induce or study hidden encoding. | `skaf_2025:approach-cot-penalty-rl` | no | 3 |
| `m-uniform-reference` | m-reference-code | selection | Reference to equally likely items | A reference to one of many items both parties hold, each assumed equally likely (a verse of a shared book), leaves the covertext and stegotext distributions equal. | `cachin_2004:bible-verse-codebook` | yes | 1 |
| `m-universal-estimate-and-sample` | m-sampling | sampling | Estimate-and-sample universal stegosystem | The unknown cover distribution is estimated and stegotext is sampled from the estimate using the sender's private randomness. | `cachin_2004:approach-universal-stegosystem` | yes | 1 |
| `m-universal-perturbation` | m-media-embedding | media-embedding | Cover-independent (universal) encoding | The secret is encoded independently of the cover image. | `zhang_2021b:surveyed-universal-deep-hiding` | yes | 1 |
| `m-utility-gap` | m-detection | detection | Decision-theoretic utility gap (not a landing node) | Steganography is measured by comparing the downstream utility of a message to parties who can and cannot decode it. | `anwar_2026:approach-steganographic-gap` | no | 1 |
| `m-utterance-category-code` | m-codebook | selection | Utterance-category code | The kind of remark made (a question, a complaint about the weather) stands for a message value, so the code is functional rather than lexical. | `rose_2026:bespoke-per-shoe-style-encoding` | yes | 1 |
| `m-visual-word-mapping` | m-cover-selection | cover-selection | Visual-word mapping | Visual words extracted from images express the text to be hidden, and images containing them are selected. | `qin_2019:surveyed-bow-visual-words` | yes | 1 |

## Mechanism nodes shared across families

| mechanism | families |
| --- | --- |
| `m-attack-simulated-training` | image-deep, watermarking |
| `m-codeword-substitution` | llm-capability-eval, multi-agent-collusion |
| `m-equivalent-choice` | foundations-theory, game-and-chess |
| `m-interval-plain` | linguistic-text, llm-generative-text |
| `m-letter-position` | game-and-chess, llm-generative-text |
| `m-output-signal` | llm-capability-eval, multi-agent-collusion |
| `m-phrase-codebook` | game-and-chess, llm-capability-eval, llm-generative-text, multi-agent-collusion |
| `m-synonym-substitution` | linguistic-text, llm-capability-eval |

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

## Approaches with no mechanism (0)

None.

## Mechanisms with no approaches (2)

- `m-adversary-decoding`
- `m-non-text-statistical-detection`

## Landing leaves with no published evidence (0)

None.

## Table warnings (78)

- aharon_2026:approach-focal-point-evaluation: placed only at nodes marked not a landing node (m-coordination-eval); not landable
- aharon_2026:surveyed-all-features-prompt: placed only at nodes marked not a landing node (m-focality-prompt); not landable
- aharon_2026:surveyed-culture-prompt: placed only at nodes marked not a landing node (m-focality-prompt); not landable
- aharon_2026:surveyed-saliency-prompt: placed only at nodes marked not a landing node (m-focality-prompt); not landable
- anderson_1998:approach-limits-of-steganography: placed only at nodes marked not a landing node (m-informal-limits); not landable
- anwar_2026:approach-steganographic-gap: placed only at nodes marked not a landing node (m-utility-gap); not landable
- bai_2024b:approach-generative-llm-steganalysis: placed only at nodes marked not a landing node (m-llm-classifier); not landable
- biswas_2015:approach-3p-framework: placed only at nodes marked not a landing node (m-human-move-models); not landable
- biswas_2015:surveyed-average-difference: placed only at nodes marked not a landing node (m-engine-benchmark-assessment); not landable
- biswas_2015:surveyed-move-matching: placed only at nodes marked not a landing node (m-engine-benchmark-assessment); not landable
- biswas_2015:surveyed-skilloscopy: placed only at nodes marked not a landing node (m-engine-benchmark-assessment); not landable
- biswas_2015:surveyed-sr-all-depths: placed only at nodes marked not a landing node (m-engine-benchmark-assessment; m-intrinsic-rating); not landable
- biswas_2015:surveyed-statistical-regression: placed only at nodes marked not a landing node (m-intrinsic-rating); not landable
- blasius_2009:approach-opening-fragmentation-model: placed only at nodes marked not a landing node (m-opening-and-engine-analysis); not landable
- boonstra_2024:approach-bayesian-hidden-code-forensics: placed only at nodes marked not a landing node (m-likelihood-ratio-forensics); not landable
- cachin_1998:approach-information-theoretic-model: placed only at nodes marked not a landing node (m-information-theoretic-security); not landable
- cachin_2004:approach-information-theoretic-model: placed only at nodes marked not a landing node (m-information-theoretic-security); not landable
- cetin_2022:approach-hyperbolic-rl-srym: placed only at nodes marked not a landing node (m-hyperbolic-networks); not landable
- chen_2021:approach-poincare-probe: placed only at nodes marked not a landing node (m-hyperbolic-embeddings); not landable
- feng_2023:approach-chess-language-benchmark: placed only at nodes marked not a landing node (m-chess-language-models); not landable
- feng_2023:approach-chessclip: placed only at nodes marked not a landing node (m-chess-language-models); not landable
- feng_2023:approach-chessgpt: placed only at nodes marked not a landing node (m-chess-language-models); not landable
- ganea_2018:approach-hyperbolic-neural-networks: placed only at nodes marked not a landing node (m-hyperbolic-networks); not landable
- greenblatt_2023:approach-control-evaluation: placed only at nodes marked not a landing node (m-control-evaluation); not landable
- greenblatt_2023:approach-input-collusion: placed only at nodes marked not a landing node (m-input-trigger); not landable
- greenblatt_2023:approach-untrusted-monitoring-signal-jamming: placed only at nodes marked not a landing node (m-prompted-llm-monitor; m-active-warden); not landable
- hammond_2025:approach-multi-agent-risk-taxonomy: placed only at nodes marked not a landing node (m-risk-taxonomy); not landable
- hammond_2025:surveyed-algorithmic-pricing-collusion: placed only at nodes marked not a landing node (m-learned-tacit-collusion); not landable
- hammond_2025:surveyed-compression-emergent-communication: placed only at nodes marked not a landing node (m-emergent-convention); not landable
- he_2024:approach-hierarchy-transformer: placed only at nodes marked not a landing node (m-hyperbolic-embeddings); not landable
- hernandezcastro_2006:approach-game-steganalysis: placed only at nodes marked not a landing node (m-game-statistics; m-active-warden); not landable
- hopper_2002:approach-complexity-theoretic-steganography: placed only at nodes marked not a landing node (m-complexity-theoretic-security); not landable
- hu_2020:approach-other-play: placed only at nodes marked not a landing node (m-coordination-learning); not landable
- jhamtani_2018:approach-gac: placed only at nodes marked not a landing node (m-commentary-generation); not landable
- karpov_2025:approach-indirect-guess-game: placed only at nodes marked not a landing node (m-message-passing-task); not landable
- karpov_2025:approach-prompted-stego-eval: placed only at nodes marked not a landing node (m-message-passing-task); not landable
- ker_2007:approach-batch-square-root-capacity: placed only at nodes marked not a landing node (m-capacity-laws); not landable
- ker_2008:approach-square-root-law: placed only at nodes marked not a landing node (m-capacity-laws); not landable
- kim_2024:approach-ccc: placed only at nodes marked not a landing node (m-commentary-generation); not landable
- kim_2024:approach-gcc-eval: placed only at nodes marked not a landing node (m-commentary-evaluation); not landable
- kolasani_2025:approach-llm-chess-benchmark: placed only at nodes marked not a landing node (m-llm-chess-play); not landable
- maia2_2024:approach-maia2: placed only at nodes marked not a landing node (m-neural-human-move); not landable
- mallen_2024:approach-subversion-strategy-eval: placed only at nodes marked not a landing node (m-stateless-subversion-eval); not landable
- mcilroyyoung_2020:approach-blunder-predictor: placed only at nodes marked not a landing node (m-neural-human-move); not landable
- mcilroyyoung_2020:approach-maia: placed only at nodes marked not a landing node (m-neural-human-move); not landable
- molinari_2026:approach-j-pact: placed only at nodes marked not a landing node (m-concept-lens); not landable
- molinari_2026:approach-j-space-steering: placed only at nodes marked not a landing node (m-concept-lens); not landable
- motwani_2024:approach-case-framework: placed only at nodes marked not a landing node (m-eval-framework); not landable
- nakamura_2026:approach-colosseum: placed only at nodes marked not a landing node (m-collusion-benchmark); not landable
- nickel_2017:approach-poincare-embeddings: placed only at nodes marked not a landing node (m-hyperbolic-embeddings); not landable
- regan_2011:approach-intrinsic-rating-model: placed only at nodes marked not a landing node (m-intrinsic-rating); not landable
- regan_2012:approach-intrinsic-performance-ratings: placed only at nodes marked not a landing node (m-intrinsic-rating); not landable
- rippin_2026:approach-agentic-covert-channel-construction: placed only at nodes marked not a landing node (m-agentic-construction-eval); not landable
- rippin_2026:approach-tacit-stego-agreement-cci: placed only at nodes marked not a landing node (m-coordination-eval); not landable
- roger_2023:approach-paraphrase-defence: placed only at nodes marked not a landing node (m-active-warden); not landable
- roger_2023:surveyed-scratchpad-scheme: placed only at nodes marked not a landing node (m-scheme-discovery-condition); not landable
- rose_2026:approach-helios: placed only at nodes marked not a landing node (m-activation-probe); not landable
- rose_2026:approach-narcbench: placed only at nodes marked not a landing node (m-collusion-benchmark); not landable
- sala_2018:approach-combinatorial-construction: placed only at nodes marked not a landing node (m-hyperbolic-embeddings); not landable
- sala_2018:approach-h-mds: placed only at nodes marked not a landing node (m-hyperbolic-embeddings); not landable
- sala_2018:approach-pytorch-sgd-pga: placed only at nodes marked not a landing node (m-hyperbolic-embeddings); not landable
- sarkar_2011:approach-delaunay-tree-embedding: placed only at nodes marked not a landing node (m-hyperbolic-embeddings); not landable
- schulz_2026:approach-three-method-stego-elicitation: placed only at nodes marked not a landing node (m-training-elicitation); not landable
- shimizu_2020:approach-hnn-plus-plus: placed only at nodes marked not a landing node (m-hyperbolic-networks); not landable
- shimizu_2020:approach-poincare-beta-concatenation: placed only at nodes marked not a landing node (m-hyperbolic-networks); not landable
- tailor_2026:approach-rolewise-decomposition: placed only at nodes marked not a landing node (m-eval-framework); not landable
- tang_2024:approach-lsgc: placed only at nodes marked not a landing node (m-llm-classifier); not landable
- tomasev_2020:approach-insilico-variant-assessment: placed only at nodes marked not a landing node (m-opening-and-engine-analysis); not landable
- tomasev_2020:approach-prior-entropy-diversity: placed only at nodes marked not a landing node (m-opening-and-engine-analysis); not landable
- westphal_2026:approach-probe-detection-recontextualisation: placed only at nodes marked not a landing node (m-activation-probe); not landable
- xia_2026:approach-lapha: placed only at nodes marked not a landing node (m-hyperbolic-networks); not landable
- xiang_2018:approach-wes: placed only at nodes marked not a landing node (m-text-feature-steganalysis); not landable
- yan_2010:approach-inference-engine-collusion-detector: placed only at nodes marked not a landing node (m-game-record-inference); not landable
- yang_2024:approach-hyplora: placed only at nodes marked not a landing node (m-hyperbolic-networks); not landable
- yang_2026:approach-hyperbolicity-atlas: placed only at nodes marked not a landing node (m-hyperbolic-embeddings); not landable
- zolkowski_2025:approach-encoded-message-passing-eval: placed only at nodes marked not a landing node (m-message-passing-task); not landable
- zolkowski_2025:approach-encoded-reasoning-eval: placed only at nodes marked not a landing node (m-encoded-reasoning-task); not landable
- zolkowski_2025:surveyed-model-generated-subtlety: placed only at nodes marked not a landing node (m-scheme-discovery-condition); not landable
