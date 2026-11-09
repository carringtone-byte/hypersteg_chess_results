---
generated: 2026-11-08T20:09:54+03:00
---

# Approach map — image-generative-coverless

Built by `tools/build_approach_map.py` from `C:\Users\user\Documents\GitHub\hypersteg_chess\hypersteg_novelty_kit_20261108\literature\verified_claims`, the features table `C:\Users\user\Documents\GitHub\hypersteg_chess\hypersteg_novelty_kit_20261108\maps\approach_features.tsv` and the technique taxonomy `C:\Users\user\Documents\GitHub\hypersteg_chess\hypersteg_novelty_kit_20261108\maps\technique_taxonomy.tsv`. View: `both`. Overview: [approach_map.md](approach_map.md).

- approaches: 17
- techniques: 11

```mermaid
flowchart LR
  subgraph fam_image_generative_coverless_g["image-generative-coverless"]
    fam_image_generative_coverless("image-generative-coverless")
    tech_igc_attribute_mapping{{"Attribute mapping (cover selection)"}}
    tech_igc_diffusion_inversion{{"Diffusion inversion translation"}}
    tech_igc_generative_synthesis{{"Generative synthesis"}}
    tech_igc_grille_inpainting{{"Grille and inpainting"}}
    tech_igc_hash_mapping{{"Image-hash mapping"}}
    tech_igc_latent_mapping{{"Message-to-latent mapping"}}
    tech_igc_latent_search{{"Latent search"}}
    tech_igc_model_database{{"Generator-model database"}}
    tech_igc_patch_retrieval{{"Partial-duplicate patch retrieval"}}
    tech_igc_secret_conditioned_generator{{"Secret-conditioned generator"}}
    tech_igc_visual_word_mapping{{"Visual-word mapping"}}
    n_hu_2018_approach_dcgan_swe["Method — map secret bits into the noise vector of a trained…<br/>hu_2018"]
    n_qin_2019_surveyed_average_pixel_dictionary["average pixel values of sub-images, with a Chinese-sentence…<br/>qin_2019"]
    n_qin_2019_surveyed_bow_visual_words["bag-of-words visual words mapped to text keywords<br/>qin_2019"]
    n_qin_2019_surveyed_dcgan_noise_vector["secret mapped to a DCGAN noise vector; the sender holds the…<br/>qin_2019"]
    n_qin_2019_surveyed_dct_lda["DCT DC-coefficient feature sequences within LDA topic class…<br/>qin_2019"]
    n_qin_2019_surveyed_densenet_block_matching["block matching with DenseNet features and DC-coefficient ha…<br/>qin_2019"]
    n_qin_2019_surveyed_gif_attributes["GIF extension attributes classified and mapped to bits<br/>qin_2019"]
    n_qin_2019_surveyed_gray_hash_selection["gray-value hash, inverted index, cover selection<br/>qin_2019"]
    n_qin_2019_surveyed_hog_hash["HOG-based block hashes, with a shared block position shifte…<br/>qin_2019"]
    n_qin_2019_surveyed_partial_duplicates["partial-duplicate images retrieved per patch; patch locatio…<br/>qin_2019"]
    n_qin_2019_surveyed_sift_robust_hash["SIFT-orientation hash of 18 bits, with side information hid…<br/>qin_2019"]
    n_qin_2019_surveyed_wgan_model_database["a WGAN model database turns the secret image into an unrela…<br/>qin_2019"]
    n_wei_2022_approach_gsn["Method — a generator synthesises stego images straight from…<br/>wei_2022"]
    n_yu_2023_approach_cross["Method — coverless image steganography by invertible diffus…<br/>yu_2023"]
    n_zhang_2018_approach_cardan_grille_inpainting["Practical instance — a digital Cardan grille marks where th…<br/>zhang_2018"]
    n_zhang_2018_approach_gss["Method — the stego image is sampled by a trained generator;…<br/>zhang_2018"]
    n_zhang_2021b_surveyed_synthesis_generative["synthesis (generative, modification-free) steganography: th…<br/>zhang_2021b"]
    paper_zhang_2018(["zhang_2018<br/>(paper)"])
  end
  subgraph other_families["other families"]
    paper_cachin_1998(["cachin_1998<br/>(paper)<br/>family: foundations-theory"])
  end
  fam_image_generative_coverless --- tech_igc_attribute_mapping
  tech_igc_generative_synthesis --- tech_igc_diffusion_inversion
  fam_image_generative_coverless --- tech_igc_generative_synthesis
  tech_igc_generative_synthesis --- tech_igc_grille_inpainting
  tech_igc_attribute_mapping --- tech_igc_hash_mapping
  tech_igc_generative_synthesis --- tech_igc_latent_mapping
  tech_igc_generative_synthesis --- tech_igc_latent_search
  tech_igc_generative_synthesis --- tech_igc_model_database
  tech_igc_attribute_mapping --- tech_igc_patch_retrieval
  tech_igc_generative_synthesis --- tech_igc_secret_conditioned_generator
  tech_igc_attribute_mapping --- tech_igc_visual_word_mapping
  tech_igc_latent_mapping --- n_hu_2018_approach_dcgan_swe
  tech_igc_hash_mapping --- n_qin_2019_surveyed_average_pixel_dictionary
  tech_igc_visual_word_mapping --- n_qin_2019_surveyed_bow_visual_words
  tech_igc_latent_mapping --- n_qin_2019_surveyed_dcgan_noise_vector
  tech_igc_hash_mapping --- n_qin_2019_surveyed_dct_lda
  tech_igc_patch_retrieval --- n_qin_2019_surveyed_densenet_block_matching
  tech_igc_hash_mapping --- n_qin_2019_surveyed_gif_attributes
  tech_igc_hash_mapping --- n_qin_2019_surveyed_gray_hash_selection
  tech_igc_hash_mapping --- n_qin_2019_surveyed_hog_hash
  tech_igc_patch_retrieval --- n_qin_2019_surveyed_partial_duplicates
  tech_igc_hash_mapping --- n_qin_2019_surveyed_sift_robust_hash
  tech_igc_model_database --- n_qin_2019_surveyed_wgan_model_database
  tech_igc_secret_conditioned_generator --- n_wei_2022_approach_gsn
  tech_igc_diffusion_inversion --- n_yu_2023_approach_cross
  tech_igc_grille_inpainting --- n_zhang_2018_approach_cardan_grille_inpainting
  tech_igc_latent_search --- n_zhang_2018_approach_gss
  tech_igc_latent_mapping --- n_zhang_2021b_surveyed_synthesis_generative
  n_qin_2019_surveyed_dcgan_noise_vector <-->|Restates| n_hu_2018_approach_dcgan_swe
  paper_zhang_2018 -->|Refines| paper_cachin_1998
  linkStyle 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27 stroke:#9e9e9e,stroke-width:1px
  linkStyle 28 stroke:#00838f,stroke-width:2.5px,color:#00838f
  linkStyle 29 stroke:#1565c0,stroke-width:2.5px,color:#1565c0
  classDef stub fill:#f5f5f5,stroke:#9e9e9e,stroke-dasharray:4 3,color:#424242
  class paper_cachin_1998 stub
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
| `igc-attribute-mapping` | — | Attribute mapping (cover selection) | Unmodified natural images are chosen because their own attributes map to the message under an agreed rule. | `qin_2019:coverless-definition` | 9 |
| `igc-diffusion-inversion` | igc-generative-synthesis | Diffusion inversion translation | A diffusion model inverts a secret image and regenerates it under another condition as the container, and the receiver inverts back. | `yu_2023:approach-cross` | 1 |
| `igc-generative-synthesis` | — | Generative synthesis | A shared generator produces the container image directly from the message, so no cover is modified. | `zhang_2021b:surveyed-synthesis-generative` | 8 |
| `igc-grille-inpainting` | igc-generative-synthesis | Grille and inpainting | The message is written at positions marked by a shared mask and a generator inpaints the rest of the image. | `zhang_2018:approach-cardan-grille-inpainting` | 1 |
| `igc-hash-mapping` | igc-attribute-mapping | Image-hash mapping | A hash of low-level features (grey values, HOG, SIFT, DCT, deep features, file attributes) is matched to message segments through an index. | `qin_2019:surveyed-gray-hash-selection` | 6 |
| `igc-latent-mapping` | igc-generative-synthesis | Message-to-latent mapping | Message bits are mapped to the generator's input noise and a trained extractor recovers them from the image. | `hu_2018:approach-dcgan-swe` | 3 |
| `igc-latent-search` | igc-generative-synthesis | Latent search | The generator's latent space is searched for a code whose output carries the message. | `zhang_2018:approach-gss` | 1 |
| `igc-model-database` | igc-generative-synthesis | Generator-model database | A database of generator models turns a secret image into an unrelated-looking image and back. | `qin_2019:surveyed-wgan-model-database` | 1 |
| `igc-patch-retrieval` | igc-attribute-mapping | Partial-duplicate patch retrieval | Patches of a secret image are matched by retrieved natural images and stitched back at the receiver. | `qin_2019:surveyed-partial-duplicates` | 2 |
| `igc-secret-conditioned-generator` | igc-generative-synthesis | Secret-conditioned generator | A module inside the generator writes the secret into its feature maps during image generation. | `wei_2022:approach-gsn` | 1 |
| `igc-visual-word-mapping` | igc-attribute-mapping | Visual-word mapping | Visual words found in images are mapped to text keywords so selected images express a text message. | `qin_2019:surveyed-bow-visual-words` | 1 |

## Lineage edges (2)

| source | kind | target | lifted_from | ledger line |
| --- | --- | --- | --- | --- |
| `paper:zhang_2018` | Refines | `paper:cachin_1998` | `zhang_2018:js-epsilon-security`, `cachin_1998:relative-entropy-security` | zhang_2018.md:92 |
| `qin_2019:surveyed-dcgan-noise-vector` | Restates | `hu_2018:approach-dcgan-swe` | — | qin_2019.md:216 |

## Approaches

| address | name | family | technique | channel | key | access | capacity | mechanism | landable | mechanism_evidence | carrier | acquisition |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `hu_2018:approach-dcgan-swe` | Method — map secret bits into the noise vector of a trained DCGAN generator; no embedding | image-generative-coverless | igc-latent-mapping | latent-generative | shared-model | training | σ bits per noise value, 3×\|z\| bits per image; 9.16e-3 bytes/pixel; recovery accuracy about 0.89–0.96, not 100% | m-latent-mapping | yes | own | generated images (generator noise vector) | weight-trained |
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
| `wei_2022:approach-gsn` | Method — a generator synthesises stego images straight from secret data, with no cover | image-generative-coverless | igc-secret-conditioned-generator | latent-generative | shared-model | training | 1–8 bpp; extraction accuracy 97.5% at 1 bpp, about 59–61% at 8 bpp | m-secret-conditioned-generator | yes | own | generated images (generator feature maps) | weight-trained |
| `yu_2023:approach-cross` | Method — coverless image steganography by invertible diffusion translation, with no training | image-generative-coverless | igc-diffusion-inversion | latent-generative | shared-key | weights | one secret image per container image | m-diffusion-translation | yes | own | generated container images | specified |
| `zhang_2018:approach-cardan-grille-inpainting` | Practical instance — a digital Cardan grille marks where the message is written; semantic inpainting fills the rest | image-generative-coverless | igc-grille-inpainting | pixel-spatial | shared-key | training | recovery above 70% at bit plane 7; higher bit planes more stable | m-grille-inpainting | yes | own | pixels at grille positions of an inpainted image | weight-trained |
| `zhang_2018:approach-gss` | Method — the stego image is sampled by a trained generator; no explicit cover | image-generative-coverless | igc-latent-search | latent-generative | shared-key | training | 1.49e-3 to 1.10e-2 bytes per pixel, to be multiplied by the extraction rate | m-latent-search | yes | own | generated images (searched latent code) | weight-trained |
| `zhang_2021b:surveyed-synthesis-generative` | synthesis (generative, modification-free) steganography: the container is generated from the message by a shared generator and extractor | image-generative-coverless | igc-latent-mapping | latent-generative | shared-model | training | — | m-latent-mapping | yes | own | generated images | weight-trained |
