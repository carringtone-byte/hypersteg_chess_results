---
paper: "Agarwal et al. (2023)"
title: "HyperSteg: Hyperbolic Learning for Deep Steganography"
doi: "10.1109/ICASSP49357.2023.10096162"
pmcid: ""
url: "ICASSP 2023 - 2023 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP); downloaded by the user from IEEE Xplore"
source_version: "published"
file: "literature/agarwal_2023.pdf"
retrieved: "20261105"
verified_by: "Claude (Opus 5.5) subagent, collusion-and-control strand, quotes checked with verify_quotes.py (read-only run)"
# The six below are written by `verify_quotes.py --stamp` — do not hand-edit.
# They bind the ledger to the exact source/extract bytes AND its own quoted text
# (body_sha256) it was verified against, so a later quote edit is caught in CI.
source_sha256: "c54d09dd4046dbb4545966c628e12a265af657f646cd854758f506e91c7d3ecc"
extract_sha256: "5a44ffada1ace06040114804b489e0e2c95fd5834eefb15b5e4463739c06f65f"
body_sha256: "f6daa374990180a68e9c9020f90a3e0729f9d397a95277ad8a8737331e6a3233"
verifier_version: "2"
verified_verdict: "pass"
verified_date: "20261106"
extract_source_sha256: "c54d09dd4046dbb4545966c628e12a265af657f646cd854758f506e91c7d3ecc"
---

# Verified Claims — Agarwal et al. (2023)

Each claim below was extracted by reading the downloaded paper file with the Read
tool, grepping for the specific content, and reading the surrounding context to
confirm the attribution is faithful.

Source: ICASSP 2023, IEEE. Authors: Shivam Agarwal, Ritesh Soun, Rahul Shivani, Vishnu
Varanasi, Navroop Gill, Ramit Sawhney (Scaler; University of Illinois at Urbana-Champaign;
Sri Venkateswara College). The DOI is printed in the page footer of the extract. The paper is
four pages of text plus references; no page numbers are printed, so locations are by section.
HyperSteg is image and audio steganography with convolutional autoencoders; it involves no
text, no language models and no games. It gives the Hypersteg project its name and framing,
not its method.

## Claim 1: Aim — hide a message in a public carrier with minimal perceptual loss, by blending in hyperbolic space

> "Steganography is the art of hiding a secret message signal inside a publicly visible carrier with minimum perceptual loss in the carrier."

> "We propose HyperSteg: a novel steganography method in the hyperbolic space grounded in the hyperbolic properties of wave interference."

> "Through extensive experiments over image and audio datasets, we introduce HyperSteg as a practical, model and modality agnostic approach for information hiding."

**ID:** hypersteg-hyperbolic-blending-aim
**Location:** Abstract
**Grep command used:** `Grep pattern="publicly visible carrier|grounded in the hyperbolic|model and modality agnostic" path="literature/extracted/agarwal_2023.txt"`

---

## Claim 2: Motivation — Euclidean neural steganography is said to distort the hyperboloid message-carrier interference

> "Existing neural steganography methods [9, 10] represent these hyperboloid waveforms in the Euclidean space resulting in unwanted noises and distortions in their representations"

> "The hyperbolic space inherently better represents hierarchical and hyperboloid message-carrier waves making them more suitable for steganography"

**ID:** hypersteg-euclidean-distortion-motivation
**Location:** Section 1 "Introduction" (reference [9] is Baluja 2017, *Hiding images in plain sight: Deep steganography*; [10] is Kreuk et al. 2020, *Hide and speak*)
**Grep command used:** `Grep pattern="hyperboloid waveforms|inherently better represents" path="literature/extracted/agarwal_2023.txt"`

---

## Claim 3: Architecture — autoencoder with preparation, hiding and reveal networks, blending in the hyperbolic space

> "We use auto-encoders as a back-bone to define HyperSteg."

> "Our goal is to hide the message m inside carrier c to generate an augmented carrier c′, such that the augmented carrier c′ has minimal perceptual changes."

> "HyperSteg consists of a preparation network used to embed the message m followed by blending the message and carrier c in the hyperbolic space."

> "the hiding network is used to reconstruct the carrier c′ from the blended features and the reveal network is used to decode the message m′ from the transmitted carrier c′."

**ID:** hypersteg-autoencoder-architecture
**Location:** Section 2.2 "HyperSteg: Hyperbolic Steganography"
**Grep command used:** `Grep pattern="auto-encoders as a back|preparation network used to embed|reveal network is used to decode" path="literature/extracted/agarwal_2023.txt"`

---

## Claim 4: Blending step — exponential map onto the Poincaré ball, then Poincaré β-concatenation of message and carrier features

> "We define HyperSteg on the Poincaré ball model"

> "We first map the message hidden state hm and the carrier c to the hyperbolic space via the exponential mapping"

> "These features are then concatenated in the tangent space, and mapped to the Poincarè ball"

**ID:** hypersteg-poincare-beta-concatenation
**Location:** Sections 2.1 "Hyperbolic Geometry" and 2.2 (Eqs. 4–5; the β-concatenation follows reference [16], Shimizu et al. 2021, *Hyperbolic neural networks++*; the extract garbles the accent as "Poincar ´e")
**Grep command used:** `Grep pattern="Poincar|via the exponential mapping|concatenated in the tangent space" path="literature/extracted/agarwal_2023.txt"`

---

## Claim 5: Training objective — weighted sum of carrier and message MSE, trained end to end

> "We use mean squared error (MSE) to optimize HyperSteg using a combination of carrier loss"

> "We use a weighted MSE to optimize in an end-to-end fashion"

**ID:** hypersteg-weighted-mse-loss
**Location:** Section 2.2 (loss L = Lc + ζLm, ζ a loss-balancing parameter; optimised with Riemannian Adam, Section 3)
**Grep command used:** `Grep pattern="mean squared error \(MSE\) to optimize|weighted MSE to optimize" path="literature/extracted/agarwal_2023.txt"`

---

## Claim 6: Data, baselines and metrics — ImageNet and ESC-50, against HUGO, HiDDeN and DeepStego

> "Following [9] we evaluate image steganography on ImageNet [23] and audio steganography on ESC-50 [24]."

> "We include universal image quality metric (UIQ) [25] for images similarity and Acoustid Chromaprint distance (ACD) [26] for audio fingerprint distance."

> "We note large improvements ( p < 0.01) on using hyperbolic learning for steganography"

**ID:** hypersteg-datasets-baselines-results
**Location:** Section 3 "Experimental Setup" and Section 4.1 "Performance Comparison", Table 1 (combined loss: HyperSteg 0.040 on ImageNet and 0.065 on ESC50, against DeepStego 0.153 and 0.073; mean of 10 runs)
**Grep command used:** `Grep pattern="evaluate image steganography on|Acoustid Chromaprint|large improvements" path="literature/extracted/agarwal_2023.txt"`

---

## Claim 7: Ablation — replacing the β-concatenation with Euclidean concatenation hides worse

> "we replace the Poincare β − concat with conventional Euclidean concatenation. We observe that hyperbolic learning significantly ( p <0.01) outperforms the Euclidean model."

**ID:** hypersteg-euclidean-ablation
**Location:** Section 4.2 "Impact of Hyperbolic Learning", Fig. 2
**Grep command used:** `Grep pattern="conventional Euclidean concatenation" path="literature/extracted/agarwal_2023.txt"`

---

## Claim 8: Adversarial robustness — white-box FGSM and I-FGSM attacks

> "We note that on average HyperSteg is 32.2 % more robust compared to its Euclidean counterpart over FGSM and I-FGSM"

**ID:** hypersteg-adversarial-robustness
**Location:** Section 4.3 "Impact of Adversarial Attack", Table 2 (the robustness here is to adversarially perturbed inputs to the model, not to a steganalyst)
**Grep command used:** `Grep pattern="32.2" path="literature/extracted/agarwal_2023.txt"`

---

## Claim 9: Near-copy decoders fail — models H1–H4, trained as minor variations of the base model, cannot recover the message (Table 3)

> "We trained four new models (H1-H4), with comparable losses, using minor variations in H0."

> "In H1, we use a different epoch from the same training cycle as our base model. We train H2 with random initialization of weights"

> "We observe high M.Loss for M1-M4 when compared with H0."

> "it would be a significant challenge to build a decoder that can recover secret information from the encoded messages even if the same training environment is replicated as that of our baseline model."

**ID:** hypersteg-near-copy-decoders-fail
**Location:** Section 4.4 "Steganalysis Robustness", Table 3 (message loss: H0 0.013; H1 1.101; H2 2.534; H3 2.921; H4 1.335. H3 varies ζ and H4 the sectional curvature κ. The "steganalysis" here is decoding by a near-copy of the receiver, the analogue of the opposing team; no detector of whether a carrier holds a message is tested)
**Grep command used:** `Grep pattern="four new models|different epoch from the same|high M.Loss|significant challenge to build a decoder" path="literature/extracted/agarwal_2023.txt"`

---

## Claim 10: Dissimilar carriers hide better — pairing each message with its farthest carrier in hyperbolic distance lowers loss (Table 4)

> "we blend the closest (most similar) sample and the farthest (most dissimilar) sample for every training instance as per their hyperbolic distance."

> "We observe that hiding messages in dissimilar carrier leads to significantly ( p < 0.01) better performance as compared to blending similar or random samples"

> "suggesting that it is easier to hide message bits in more dissimilar carriers."

**ID:** hypersteg-dissimilar-carriers-hide-better
**Location:** Section 4.5 "Impact of Hyperbolic Distance", Table 4 (combined loss, ImageNet / ESC50: Closest 0.043 / 0.111; Random 0.040 / 0.090; Farthest 0.034 / 0.079; mean of 10 runs, Wilcoxon signed-rank. "Better" means lower carrier-plus-message reconstruction loss, not lower detectability)
**Grep command used:** `Grep pattern="most dissimilar|dissimilar carrier leads|more dissimilar carriers" path="literature/extracted/agarwal_2023.txt"`

---

## Claim 11: Zero-shot cross-modal transfer — trained on images, used on audio

> "We evaluate Hypersteg’s ability to generalize across different modalities by training on ImageNet and use the same model to generate inferences on ESC50."

> "The zero-shot model successfully encodes and decodes the audio carrier and audio messages without any explicit training on audio datasets."

**ID:** hypersteg-zero-shot-transfer
**Location:** Section 4.6 "Zero Shot Transfer Learning", Table 5
**Grep command used:** `Grep pattern="generalize across different modalities|zero-shot model successfully" path="literature/extracted/agarwal_2023.txt"`

---

## Claim 12: Approach — HyperSteg, an autoencoder that blends message and carrier features on the Poincaré ball, built on hyperbolic neural networks

> "Building on classical physics [14] and advances in hy- perbolic learning [15], we propose HyperSteg: Hyperbolic Steganography Network."

> "HyperSteg is a data and model ag- nostic method that has consistent improvements with data that is less user invasive and can be used across a variety of steganography architecutues without any modification."

> "We first map the mes- sage hidden state hm and the carrier c to the hyperbolic space via the exponential mapping"

Reference [15] is Octavian Ganea et al., "Hyperbolic neural networks"; [16], the source of the
β-concatenation, is Shimizu et al., "Hyperbolic neural networks++", which has no ledger.

**ID:** approach-hypersteg
**Location:** Section 1 "Introduction"; Section 2.2 "HyperSteg: Hyperbolic Steganography"; References [15], [16]
**Grep command used:** `Grep pattern="Building on classical physics|data and model ag|via the exponential mapping" path="literature/extracted/agarwal_2023.txt"`
**Depends-on:** ganea_2018:approach-hyperbolic-neural-networks (grounded by #approach-hypersteg)
