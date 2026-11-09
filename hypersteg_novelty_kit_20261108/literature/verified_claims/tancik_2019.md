---
paper: "Tancik, Mildenhall and Ng (2019)"
title: "StegaStamp: Invisible Hyperlinks in Physical Photographs"
doi: "<DOI>"
pmcid: "<PMC ID, if any>"
url: "https://arxiv.org/abs/1904.05343 (arXiv:1904.05343v2, 26 Mar 2020; arXiv HTML rendering)"
source_version: "preprint"
file: "literature/tancik_2019.html"
retrieved: "20261106"
verified_by: "Claude (Opus 5.5) subagent, quotes checked with verify_quotes.py (read-only run)"
# The six below are written by `verify_quotes.py --stamp` — do not hand-edit.
# They bind the ledger to the exact source/extract bytes AND its own quoted text
# (body_sha256) it was verified against, so a later quote edit is caught in CI.
source_sha256: "2af31fba7e0312410c85ae1db379cca904267b0a5b7a4ab7d2f1d97a34966d07"
extract_sha256: "5bb8e72248cb45234d4f68d76f0aa2f7375f30f2d8aea1a23a87efec22624120"
body_sha256: "6aab94d55303c2519b5c47cd72c124c530500f7be9f6235d21681fddd3f9304a"
verifier_version: "2"
verified_verdict: "pass"
verified_date: "20261106"
extract_source_sha256: "2af31fba7e0312410c85ae1db379cca904267b0a5b7a4ab7d2f1d97a34966d07"
---

# Verified Claims — Tancik, Mildenhall and Ng (2019)

Each claim below was extracted by reading the downloaded paper file with the Read
tool, grepping for the specific content, and reading the surrounding context to
confirm the attribution is faithful.

Source: arXiv:1904.05343v2 (cs.CV, 26 March 2020), rendered as arXiv HTML. Authors: Matthew
Tancik, Ben Mildenhall and Ren Ng, University of California, Berkeley. The paper later
appeared at CVPR 2020; the extract does not print a DOI, so the DOI field is left unset.
`literature/tancik_2020.html` is byte-identical to `literature/tancik_2019.html` (same SHA-1,
same extract), so this one ledger covers both register rows. Section numbers below are the
paper's own.

## Claim 1: Method — a learned encoder/decoder that hides hyperlink bitstrings in photos, robust to printing and photography

> "Our key technical contribution is StegaStamp, a learned steganographic algorithm to enable robust encoding and decoding of arbitrary hyperlink bitstrings into photos in a manner that approaches perceptual invisibility."

> "StegaStamp comprises a deep neural network that learns an encoding/decoding algorithm robust to image perturbations approximating the space of distortions resulting from real printing and photography."

**ID:** approach-stegastamp
**Location:** Abstract
**Grep command used:** `Grep pattern="Our key technical contribution is StegaStamp|StegaStamp comprises a deep neural network" path="literature/extracted/tancik_2019.txt"`

---

## Claim 2: Building on learned steganography — differentiable corruptions inserted between encoder and decoder

> "We extend the traditional learned steganography framework by adding a set of differentiable pixelwise and spatial image corruptions between the encoder and decoder that successfully approximate the space of distortions resulting from “physical transmission” (i.e., real printing or display and subsequent image capture)."

> "HiDDeN introduces various types of noise between encoding and decoding to increase robustness but focuses only on the set of corruptions that would occur through digital image manipulations (e.g., JPEG compression and cropping)."

**ID:** extends-learned-steganography
**Location:** Section 1 "Introduction"; Section 2.1 "Steganography"
**Grep command used:** `Grep pattern="We extend the traditional learned steganography|HiDDeN introduces various types of noise" path="literature/extracted/tancik_2019.txt"`

---

## Claim 3: Channel architecture — the encoder outputs an RGB residual added to the cover; a 100-bit message enters as an extra channel

> "We use a U-Net  [ 39 ]  style architecture that receives a four channel  400 × 400 400\times 400  pixel input (input image RGB channels plus one for the message) and outputs a three channel RGB residual image."

> "The residual is calculated by the encoder network and added back to the original image to produce the encoded StegaStamp."

**ID:** residual-encoder
**Location:** Section 4.1 "Encoder"; Figure 2 caption
**Grep command used:** `Grep pattern="U-Net|The residual is calculated by the encoder network" path="literature/extracted/tancik_2019.txt"`

---

## Claim 4: What the method needs — jointly trained networks, a critic used as a perceptual loss, and a fine-tuned detector

> "As part of our total loss, we use a critic network that predicts whether a message is encoded in a image and is used as a perceptual loss for the encoder/decoder pipeline."

> "During training, we use images from the MIRFLICKR dataset  [ 23 ]  (resampled to  400 × 400 400\times 400  resolution) combined with randomly sampled binary messages."

> "We fine-tune an off-the-shelf semantic segmentation network BiSeNet  [ 48 ]  to segment areas of the image that are believed to contain StegaStamps."

**ID:** training-and-critic
**Location:** Section 4.4 "Encoder/Decoder Training Procedure"; Section 4.3 "Detector"
**Grep command used:** `Grep pattern="we use a critic network|MIRFLICKR dataset|fine-tune an off-the-shelf" path="literature/extracted/tancik_2019.txt"`

---

## Claim 5: Capacity — 100 encoded bits, 56 bits after BCH error correction; a quality–accuracy trade-off with message length

> "We settle on a message length of 100 bits as it provides a good compromise between image quality and information transfer."

> "Given an estimate of at least 95% recovery accuracy, we can encode at least 56 error corrected bits using BCH codes"

> "Larger message are more difficult to encode and decode; as a result, there is a trade off between recovery accuracy and perceptual similarity."

> "The image degradation caused by encoding 150 or 200 bits is much more perceptible."

**ID:** capacity-100-bits-56-corrected
**Location:** Section 5.4 "Practical Message Length"
**Grep command used:** `Grep pattern="We settle on a message length|at least 56 error corrected bits|trade off between recovery accuracy|150 or 200 bits" path="literature/extracted/tancik_2019.txt"`

---

## Claim 6: Robustness — 98.7% mean bit-accuracy across 18 display/printer and camera combinations; robustness to partial occlusion

> "We evaluate our system in a controlled real world setting with 18 combinations of 6 different displays/printers and 3 different cameras. Across all settings combined (1890 captured images), we achieve a mean bit-accuracy of  98.7 %"

> "We also demonstrate a surprising level of robustness when portions of the StegaStamp are covered by other objects"

> "We conduct real and synthetic ablation studies with four different trained models to verify that our system is robust to each of the perturbations we apply during training and that omitting these augmentations significantly decreases performance."

**ID:** physical-robustness-results
**Location:** Section 5 "Real-World & Simulation-Based Evaluation"; Section 5.1 "In-the-Wild Robustness"
**Grep command used:** `Grep pattern="18 combinations of 6 different|surprising level of robustness|We conduct real and synthetic ablation" path="literature/extracted/tancik_2019.txt"`

---

## Claim 7: The modelled noise channel — perspective warp, blur, colour shifts, Gaussian noise and approximated JPEG

> "During training, we apply a set of differentiable image perturbations outlined in Figure  3  between the encoder and decoder to approximate the distortions caused by physically displaying and imaging the StegaStamps."

> "This rounding step is not differentiable, so we use the trick from Shin and Song"

> "We sample the JPEG quality uniformly within  [ 50,100 ]"

**ID:** differentiable-perturbation-pipeline
**Location:** Section 3 "Training for Real World Robustness"; Section 3.5 "JPEG Compression"
**Grep command used:** `Grep pattern="we apply a set of differentiable image perturbations|This rounding step is not differentiable|We sample the JPEG quality" path="literature/extracted/tancik_2019.txt"`

---

## Claim 8: Goal is robust transfer, not high bits-per-pixel; existing deep steganography fails under small corruptions

> "With the exception of HiDDeN  [ 54 ]  and Light Field Messaging (LFM)  [ 45 ] , small image manipulations or corruptions would render existing techniques useless, as their goal is encoding a large number of bits-per-pixel in the context of perfect digital transmission."

> "Additionally, adversarial attacks typically do not modify the decoder network, whereas we explicitly train our decoder to cooperate with our encoder for maximum information transferal."

**ID:** robustness-over-payload
**Location:** Section 2.1 "Steganography"; Section 2.4 "Robust Adversarial Image Attacks"
**Grep command used:** `Grep pattern="small image manipulations or corruptions would render|explicitly train our decoder to cooperate" path="literature/extracted/tancik_2019.txt"`

---

## Claim 9: Stated limits — the residual is sometimes visible in flat regions; the off-the-shelf detector is the bottleneck

> "Despite often being very subtle in high frequency textures, the residual added by the encoder network is sometimes perceptible in large low frequency regions of the image."

> "Additionally, we find our off-the-shelf detection network to be the bottleneck in our decoding performance during real world testing."

> "The current framework also assumes that the StegaStamps will be single, square images for the purpose of detection."

**ID:** stated-limitations
**Location:** Section 5.5 "Limitations"
**Grep command used:** `Grep pattern="sometimes perceptible in large low frequency|to be the bottleneck in our decoding|single, square images" path="literature/extracted/tancik_2019.txt"`

---

## Claim 10: Use case and positioning — an invisible replacement for barcodes, framed alongside watermarking

> "Another way to think about this is physical photographs that have unique QR codes invisibly embedded within them."

> "This method of data transmission has a long history in both the steganography and watermarking literatures."

> "We also show that our method is stable enough to be deployed in-the-wild as a replacement for existing barcodes that is less intrusive and more aesthetically pleasing."

**ID:** barcode-replacement-framing
**Location:** Abstract; Section 1 "Introduction"; Section 6 "Conclusion"
**Grep command used:** `Grep pattern="unique QR codes invisibly embedded|long history in both the steganography and watermarking|replacement for existing barcodes" path="literature/extracted/tancik_2019.txt"`

> Note: the paper reports no steganalysis evaluation. Its security notion is perceptual invisibility plus the critic loss of Claim 4, not undetectability against a warden.
