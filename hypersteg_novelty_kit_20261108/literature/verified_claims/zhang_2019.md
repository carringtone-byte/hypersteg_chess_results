---
paper: "Zhang, Cuesta-Infante, Xu and Veeramachaneni (2019)"
title: "SteganoGAN: High Capacity Image Steganography with GANs"
doi: "<DOI>"
pmcid: "<PMC ID, if any>"
url: "arXiv:1901.03892v2 [cs.CV], 30 January 2019 (arXiv HTML rendering)"
source_version: "preprint"
file: "literature/zhang_2019.html"
retrieved: "20261106"
verified_by: "Claude (Opus 5.5) subagent image1, quotes checked with verify_quotes.py (read-only run)"
# The six below are written by `verify_quotes.py --stamp` — do not hand-edit.
# They bind the ledger to the exact source/extract bytes AND its own quoted text
# (body_sha256) it was verified against, so a later quote edit is caught in CI.
source_sha256: "508ed9f6c497824801539f9452e4270333ec52e022fc35b50cee87b6dbb87702"
extract_sha256: "f2aeadf868d2273abfdd370f71bb1de3af4dcffddceada4a74107ccb795312a4"
body_sha256: "dc44cf4537b08638a978e75c2999e2ba6dd35bcb9afaa5c4b3a3e88d373cc663"
verifier_version: "2"
verified_verdict: "pass"
verified_date: "20261106"
extract_source_sha256: "508ed9f6c497824801539f9452e4270333ec52e022fc35b50cee87b6dbb87702"
---

# Verified Claims — Zhang, Cuesta-Infante, Xu and Veeramachaneni (2019)

Each claim below was extracted by reading the downloaded paper file with the Read
tool, grepping for the specific content, and reading the surrounding context to
confirm the attribution is faithful.

Source: arXiv:1901.03892v2, 30 January 2019, a preprint in ICML format. Authors: Kevin A. Zhang,
Lei Xu and Kalyan Veeramachaneni (MIT) and Alfredo Cuesta-Infante (Universidad Rey Juan Carlos).
The file is the arXiv HTML rendering, so the extract has no page numbers; locations below give
section, table and figure numbers. No DOI is printed in the extract.

**Which file.** This ledger cites `literature/zhang_2019.html`, the SteganoGAN paper.
`literature/zhang_2019.pdf` is a symbolic link to `literature/zhang_2018.pdf`, a different paper
(*Generative Steganography by Sampling*, ledgered as `zhang_2018`). The ledger's `file:` field
names the `.html` so that `extract_text.py` keeps extracting from the right source.

## Claim 1: Method — an adversarially trained encoder hides an arbitrary bit tensor in a cover image; a decoder recovers it

> "In this paper, we present steganogan , a generative adversarial network for hiding an arbitrary bit vector in a cover image. Our proposed architecture, shown in Figure 2 , consists of three modules: (1) an Encoder that takes a cover image and a data tensor, or message, and produces a steganographic image (Section 3.2.1 ); (2) a Decoder that takes the steganographic image and attempts to recover the data tensor (Section 3.2.2 ), and (3) a Critic that evaluates the quality of the cover and steganographic images (Section 3.2.3 )."

> "The encoder network takes a cover image C C and a message M ∈ { 0 , 1 } D × W × H M\in\{0,1\}^{D\times W\times H} . Hence M M is a binary data tensor of shape D × W × H D\times W\times H where D D is the number of bits that we will attempt to hide in each pixel of the cover image."

**ID:** approach-steganogan
**Location:** Section 3.2 "Architecture"; Section 3.2.1 "Encoder"
**Grep command used:** `Grep pattern="a generative adversarial network for hiding an arbitrary bit vector|The encoder network takes a cover image" path="literature/extracted/zhang_2019.txt"`

---

## Claim 2: Threat model — only sender and receiver should detect the message, even if the image is intercepted

> "In a typical scenario, the sender hides a secret message inside a cover image and transmits it to the receiver, who recovers the message. Even if the image is intercepted, no one besides the sender and receiver should be able to detect the presence of a message."

**ID:** interception-threat-model
**Location:** Section 1 "Introduction"
**Grep command used:** `Grep pattern="Even if the image is intercepted" path="literature/extracted/zhang_2019.txt"`

---

## Claim 3: Training objective — decoding cross-entropy, cover–stego mean squared error and critic realness, minimised together

> "To optimize the encoder-decoder network, we jointly optimize three losses: (1) the decoding accuracy using the cross-entropy loss"

> "(2) the similarity between steganographic image and the cover image using mean square error"

> "(3) and the realness of the steganographic image using the critic network"

**ID:** three-loss-objective
**Location:** Section 3.3 "Training"
**Grep command used:** `Grep pattern="we jointly optimize three losses|using mean square error|realness of the steganographic image" path="literature/extracted/zhang_2019.txt"`

---

## Claim 4: Capacity metric — Reed–Solomon bits per pixel, counting only bits that can be reliably recovered

> "It is tempting to just multiply the number of bits in the data tensor by the accuracy 1 − p 1-p and report that value as the relative payload. Unfortunately, that value is actually meaningless"

> "We refer to this metric as Reed-Solomon bits-per-pixel (RS-BPP), and note that it can be directly compared against traditional steganographic techniques since it represents the average number of bits that can be reliably transmitted in an image divided by the size of the image."

**ID:** rs-bpp-metric
**Location:** Section 4 "Evaluation Metrics"
**Grep command used:** `Grep pattern="It is tempting to just multiply|We refer to this metric as Reed-Solomon" path="literature/extracted/zhang_2019.txt"`

---

## Claim 5: Capacity result — 4.4 bits per pixel, which the authors put at ten times competing deep-learning methods

> "We present a novel approach that uses adversarial training to solve the steganography task and achieves a relative payload of 4.4 bits per pixel which is 10x higher than competing deep learning-based approaches with similar peak signal to noise ratios."

> "Traditional approaches to image steganography are only effective up to a relative payload of around 0.4 bits per pixel Pevný et al. (2010) ."

**ID:** capacity-4-4-bpp
**Location:** Section 1 "Introduction", contributions; Table 1 (Dense variant, COCO, D = 6, RS-BPP 4.40)
**Grep command used:** `Grep pattern="relative payload of 4.4 bits per pixel which|only effective up to a relative payload" path="literature/extracted/zhang_2019.txt"`

---

## Claim 6: Trade-off — more payload costs image similarity; the content of the cover matters

> "Note that there is an unavoidable tradeoff between the relative payload and the image quality measures; assuming we are already on the Pareto frontier, an increased relative payload would inevitably result in a decreased similarity."

> "Images from the Div2K dataset tend to contain open scenery, while images from the COCO dataset tend to be more cluttered and contain multiple objects, providing more surfaces and textures for our model to successfully embed data."

**ID:** payload-quality-tradeoff
**Location:** Section 5 "Results and Analysis"
**Grep command used:** `Grep pattern="unavoidable tradeoff|tend to contain open scenery" path="literature/extracted/zhang_2019.txt"`

---

## Claim 7: Statistical steganalysis — StegExpose reaches auROC 0.59 at up to 4.4 bpp

> "we note that the StegExpose tool is only slightly more effective than random guessing with an area under the ROC curve of 0.59 0.59 , even for payloads of up to 4.4 bits per pixel."

**ID:** stegexpose-auroc
**Location:** Section 6.1 "Statistical Steganalysis", Figure 5
**Grep command used:** `Grep pattern="only slightly more effective than random guessing" path="literature/extracted/zhang_2019.txt"`

---

## Claim 8: Neural steganalysis threat model — the detector knows the training algorithm but not the model weights

> "In a typical scenario, the party that is attempting to detect steganographic images has access to the algorithm used to create them - in our case, an instance of steganogan which is parameterized by the pretrained model weights but not the exact model."

> "If the external party does not know the specific model weights but does know the algorithm for generating models, can they detect steganographic images generated by steganogan ?"

**ID:** weights-as-secret
**Location:** Section 6.2 "Neural Steganalysis"
**Grep command used:** `Grep pattern="party that is attempting to detect|does not know the specific model weights" path="literature/extracted/zhang_2019.txt"`

---

## Claim 9: Neural steganalysis result — detection rises with payload; 2 bpp hides at auROC 0.8 or below

> "If we require our model to produce steganographic images such that the detection rate is at most 0.8 auROC, we find that our model can still hide up to 2 bits per pixel."

> "First, we note that the detector performance, as measured by the area under the receiver operating characteristic (auROC), increases as we increase the number of bits-per-pixel encoded in the image."

> "For a fixed detection error rate of 20%, we find that WOW is able to encode up to 0.3 bpp, S-UNIWARD is able to encode up to 0.4 bpp, HILL is able to encode up to 0.5 bpp, and steganogan is able to encode up to 2.0 bpp."

**ID:** ye-net-detection
**Location:** Section 1, contributions; Section 6.2, Figure 6
**Grep command used:** `Grep pattern="detection rate is at most 0.8 auROC|detector performance, as measured|fixed detection error rate of 20%" path="literature/extracted/zhang_2019.txt"`

---

## Claim 10: Stated limit of the comparison — the traditional baselines were measured on a different dataset

> "Note that these techniques are evaluated on different dataset and as such, the results are only approximate estimates of the actual relative payload achievable on a particular dataset."

**ID:** comparison-caveat
**Location:** Section 6.2
**Grep command used:** `Grep pattern="evaluated on different dataset" path="literature/extracted/zhang_2019.txt"`

---

## Claim 11: What the method needs — training on natural image sets; the released pre-trained models serve as encoder and decoder

> "We use the Div2k Agustsson & Timofte (2017) and COCO Lin et al. (2014) datasets to train and evaluate our model."

> "Our models are trained on GeForce GTX 1080 GPUs. The wall clock time per epoch is approximately 10 minutes for Div2K and 2 hours for COCO."

> "We are releasing a fully-maintained open-source library called steganogan"

**ID:** training-requirements
**Location:** Section 5; Section 1, contributions
**Grep command used:** `Grep pattern="We use the Div2k|wall clock time per epoch|fully-maintained open-source library" path="literature/extracted/zhang_2019.txt"`

---

## Claim 12: Position in the field — earlier deep methods fixed the image size, hid images rather than bits, or could not scale payload

> "However, they are also more limited than their traditional counterparts: they often impose special constraints on the size of the cover image (for example, Hayes & Danezis (2017) requires the cover images to be 32 x 32); they attempt to embed images inside images and not arbitrary messages or bit vectors; and finally, they do not explore the limits of how much information can be hidden successfully."

> "This design allows Zhu et al. (2018) to handle arbitrary sized images but cannot effectively scale to higher relative payloads."

**ID:** prior-deep-methods-limits
**Location:** Section 1; Section 7.2 "Deep Learning for Steganography"
**Grep command used:** `Grep pattern="more limited than their traditional counterparts|cannot effectively scale to higher" path="literature/extracted/zhang_2019.txt"`
