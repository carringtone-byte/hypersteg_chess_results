---
paper: "Zhang et al. (2021b)"
title: "A Brief Survey on Deep Learning Based Data Hiding"
doi: "<DOI>"
pmcid: "<PMC ID, if any>"
url: "arXiv:2103.01607v2 [cs.CR], 19 April 2022 (arXiv HTML rendering)"
source_version: "preprint"
file: "literature/zhang_2021b.html"
retrieved: "20261105"
verified_by: "Claude (Opus 5.5) subagent, quotes checked with verify_quotes.py (read-only run)"
# The six below are written by `verify_quotes.py --stamp` — do not hand-edit.
# They bind the ledger to the exact source/extract bytes AND its own quoted text
# (body_sha256) it was verified against, so a later quote edit is caught in CI.
source_sha256: "0a211f8b0f9c5f7253e57d65ad864d95909a6ce82713f79cddafff1cd8fcaf7b"
extract_sha256: "9c8a3481f0b2120ec0b7c92d8d115dde0f2ee4c143b7e48b89df5420f7dd8345"
body_sha256: "f26846794da9858ae726ab2086795f9af4d609dec72dfd6a25adcb7ed0d16649"
verifier_version: "2"
verified_verdict: "pass"
verified_date: "20261106"
extract_source_sha256: "0a211f8b0f9c5f7253e57d65ad864d95909a6ce82713f79cddafff1cd8fcaf7b"
---

# Verified Claims — Zhang et al. (2021b)

Each claim below was extracted by reading the downloaded paper file with the Read
tool, grepping for the specific content, and reading the surrounding context to
confirm the attribution is faithful.

Source: arXiv:2103.01607v2, the arXiv HTML rendering saved as `literature/zhang_2021b.html`.
Authors: Chaoning Zhang, Chenguo Lin, Philipp Benz, Kejiang Chen, Weiming Zhang and In So Kweon
(KAIST; Sichuan University; University of Science and Technology of China). The DOI is not printed
in the extract, so the DOI field is left unset. The paper is a survey, centred on images as the
carrier; its approach claims are therefore `surveyed-*`, one per family of schemes it describes,
and each records the survey's account, not the original paper's. Locations below are section
headings of the HTML.

## Claim 1: Framing — data hiding is judged on capacity, security (undetectability by steganalysis) and robustness, which trade off against each other

> "Data hiding schemes can be characterized by three requirements: i)  capacity , regarding the embedded payload; ii)  security , in terms of being undetectable by steganalysis; iii)  robustness , against distortions in the transmission channel."

> "For example, a large-capacity hiding algorithm is often subject to low security and weak robustness."

**ID:** capacity-security-robustness
**Location:** Section 1 "Introduction"
**Grep command used:** `Grep pattern="characterized by three requirements|large-capacity hiding algorithm is often subject" path="literature/extracted/zhang_2021b.txt"`

---

## Claim 2: Security notion — a steganalyser as third party, defeated when it does no better than a random guess

> "In  secure data hiding , there is a new participant who plays as an adversary of Alice and Bob by distinguishing containers from covers by a steganalyzer ... An effective algorithm with high security is expected to confuse ... such that it cannot perform better than a random guess,"

> "In  robust data hiding , the adversary perturbs containers with distortions to destroy secret information within them."

**ID:** steganalyser-random-guess
**Location:** Section 2 "Problem Formulation" (the ellipses stand for inline mathematics naming the steganalyser)
**Grep command used:** `Grep pattern="there is a new participant who plays as an adversary|cannot perform better than a random guess|the adversary perturbs containers" path="literature/extracted/zhang_2021b.txt"`

---

## Claim 3: Surveyed — cover-dependent deep hiding with a preparation network (Baluja): a full image hidden in another, at 24 bpp, and easily detected

> "The first deep learning based framework for hiding data in large capacity is proposed by Baluja  Baluja (2017) ;  Baluja (2019) , which places a full-size color image within another image of the same size."

> "Moreover, the hiding capacity of traditional steganography is often very low,  e . g ., HUGO  Pevnỳ et al. (2010)  hides  < 0.5 <0.5  bpp (bits per pixel), while that for deep steganography  Baluja (2017)  is 24bpp. Due to the trade-off between capacity and secrecy, most deep steganography can be relatively easily detected by some steganalysis algorithms."

**ID:** surveyed-ddh-with-preparation
**Location:** Section 3 "Deep Hiding Architectures"
**Grep command used:** `Grep pattern="The first deep learning based framework|while that for deep steganography" path="literature/extracted/zhang_2021b.txt"`

---

## Claim 4: Surveyed — cover-dependent deep hiding without preparation, the most common architecture

> "Despite being conducive to embedding analysis, preparation network"

> "As it is the most commonly adopted architecture for deep hiding, the methods mentioned later belong to  DDH without P  without special explanation."

**ID:** surveyed-ddh-without-preparation
**Location:** Section 3, "Cover-Dependent Deep Hiding without Preparation"
**Grep command used:** `Grep pattern="Despite being conducive to embedding analysis|the most commonly adopted architecture for deep hiding" path="literature/extracted/zhang_2021b.txt"`

---

## Claim 5: Surveyed — universal deep hiding: the secret is encoded independently of the cover and can be added to any cover

> "The key difference between UDH and DDH is that UDH disentangles the encoding of secret from cover,  i . e ., how the secret image is encoded is independent of the cover image."

> "The encoded secret image in UDH can be directly added to any random cover image to form a container, which enhances the flexibility of information hiding."

**ID:** surveyed-universal-deep-hiding
**Location:** Section 3, "Universal Deep Hiding"
**Grep command used:** `Grep pattern="UDH disentangles the encoding|directly added to any random cover image" path="literature/extracted/zhang_2021b.txt"`

---

## Claim 6: Steganalysis result — deep hiding evades classic tools but not a learned steganalyser; SRNet detects Baluja's scheme 99.58% of the time

> "Most of them can not be detected by classic steganalysis tools ( e . g ., StegExpose  Boehm (2014) , which combines several traditional steganalysis techniques), but fail when facing deep learning based steganalyzer."

> "To be specific, when facing one of the state-of-the-art steganalyzer SRNet  Boroumand et al. (2018) , the detection accuracy for  Baluja (2017) ,  Weng et al. (2019) ,  Lu et al. (2021)  and  Guan et al. (2022)  is 99.58%, 77.43%, 75.69% and 75.54%, respectively  Guan et al. (2022) ."

> "It is worth noting that the SRNet steganalysis accuracy for HiNet  Jing et al. (2021)  is reported as 55.86%,"

**ID:** srnet-detection-rates
**Location:** Section 4.2 "Secure Steganography"
**Grep command used:** `Grep pattern="can not be detected by classic steganalysis|is 99.58%, 77.43%|reported as 55.86%" path="literature/extracted/zhang_2021b.txt"`

---

## Claim 7: Surveyed — adversarial architecture: a steganalyser in the training loop, a three-player game; it does not guarantee resistance to an independently trained steganalyser

> "The core of an adversarial architecture lies in an adversarial model where containers and covers are fed in, and form a 3-player game."

> "However, this does not indicate that these methods can counter independently trained steganalyzers because the adversarial training strategy limits the effectiveness of the discriminator  Shang et al. (2020) ."

**ID:** surveyed-adversarial-architecture
**Location:** Section 4.2.1 "Adversarial Architecture"
**Grep command used:** `Grep pattern="form a 3-player game|counter independently trained steganalyzers" path="literature/extracted/zhang_2021b.txt"`

---

## Claim 8: Surveyed — synthesis (generative, modification-free) steganography: the container is generated from the message by a shared generator and extractor

> "Different from the embedding-based schemes mentioned above, there is no modification operated in synthesis technology, because containers are generated directly based on secret messages  Hu et al. (2018) ."

> "Finally, with the fixed generator and extractor from previous steps, Alice and Bob can have an undetectable secret communication by mapping secret messages into vectors prior to synthesis."

**ID:** surveyed-synthesis-generative
**Location:** Section 4.2.2 "Synthesis Technology"
**Grep command used:** `Grep pattern="no modification operated in synthesis technology|with the fixed generator and extractor" path="literature/extracted/zhang_2021b.txt"`

---

## Claim 9: Surveyed — robust watermarking by attack simulation during training (HiDDeN and successors); JPEG's non-differentiability is the chief obstacle

> "Compared with capacity and security, digital watermarking prioritizes robustness."

> "Inspired by this, one intuitive and commonly used strategy to resist noise attack for robust watermarking is to simulate such distortions in the training process,  i . e ., distorting containers with the respective attacks before feeding them to the reveal network  Zhu et al. (2018) ."

> "However, it is a non-trivial task to improve the robustness against JPEG compression, because it is a non-differentiable operation, which hinders training"

**ID:** surveyed-noise-augmentation-watermarking
**Location:** Section 4.3 "Robust Watermarking"; Section 4.3.1 "Data Augmentation Approach"; Section 4.3.2
**Grep command used:** `Grep pattern="digital watermarking prioritizes robustness|simulate such distortions in the training process|non-differentiable operation, which hinders" path="literature/extracted/zhang_2021b.txt"`

---

## Claim 10: Surveyed — light field messaging: hidden data sent screen-to-camera, with robustness rather than undetectability as the goal

> "As a practical application for data hiding, light field messaging (LFM)  Wengrowski and Dana (2019)  describes the process of embedding, transmitting and receiving hidden information in an image displayed on a display  screen  and captured by a  camera ."

> "The LFM process is also often termed screen-camera communication  Cui et al. (2019)  or photographic steganography but has no concern of being detected by steganalysis."

**ID:** surveyed-light-field-messaging
**Location:** Section 4.4 "Light Field Messaging"
**Grep command used:** `Grep pattern="light field messaging \(LFM\)|has no concern of being detected by steganalysis" path="literature/extracted/zhang_2021b.txt"`

---

## Claim 11: Surveyed — speech hidden in speech (Kreuk et al.), the image framework carried over with differentiable STFT layers

> "Hiding audio in audio has been demonstrated in  Kreuk et al. (2019) . It has been found that the framework for hiding images in images is suitable for the audio domain but requires including a short-time Fourier transform and inverse-time transform as differentiable layers during the training."

**ID:** surveyed-speech-in-speech
**Location:** Section 5 "Hiding Data within Other Multimedia"
**Grep command used:** `Grep pattern="Hiding audio in audio has been demonstrated" path="literature/extracted/zhang_2021b.txt"`

**Restates:** kreuk_2019:approach-hide-and-speak (grounded by #surveyed-speech-in-speech)

---

## Claim 12: Surveyed — text watermarking by an adversarially trained encoder–decoder transformer (AWT), set apart from generative text methods

> "Different from those generative methods  Yang et al. (2018) ;  Yang et al. (2019b) , Abdelnabi  et al .  Abdelnabi and Fritz (2020)  introduce the Adversarial Watermarking Transformer (AWT) with a jointly trained encoder-decoder and adversarial training. With an input text and a binary message, the watermarking system can generate an output text that is unobtrusively modified with the given message."

**ID:** surveyed-adversarial-watermarking-transformer
**Location:** Section 5 "Hiding Data within Other Multimedia"
**Grep command used:** `Grep pattern="Adversarial Watermarking Transformer" path="literature/extracted/zhang_2021b.txt"`

---

## Claim 13: The reveal network responds to changes humans cannot see — the same misalignment that adversarial examples exploit

> "In essence, the container image is just a cover image with an imperceptible change. The reveal network is very sensitive to such small invisible changes. In other words, there is a misalignment between human vision and DNNs."

> "The reason for the misalignment has been attributed to the fact that DNNs are sensitive to high-frequency content  Zhang et al. (2021a)  with the observation that frequency is a key factor that influences the performance for both tasks."

**ID:** hiding-adversarial-link
**Location:** Section 6 "Link with Adversarial Attack"
**Grep command used:** `Grep pattern="The reveal network is very sensitive|DNNs are sensitive to high-frequency content" path="literature/extracted/zhang_2021b.txt"`
