---
paper: "Kreuk et al. (2019)"
title: "Hide and Speak: Towards Deep Neural Networks for Speech Steganography"
doi: "<DOI>"
pmcid: "<PMC ID, if any>"
url: "arXiv:1902.03083v2 [cs.SD], 27 July 2020 (arXiv HTML rendering)"
source_version: "preprint"
file: "literature/kreuk_2019.html"
retrieved: "20261105"
verified_by: "Claude (Opus 5.5) subagent, quotes checked with verify_quotes.py (read-only run)"
# The six below are written by `verify_quotes.py --stamp` — do not hand-edit.
# They bind the ledger to the exact source/extract bytes AND its own quoted text
# (body_sha256) it was verified against, so a later quote edit is caught in CI.
source_sha256: "42ec98713b2c0e30fc633fb59529a3503588ce34533f142cfda614a92c025815"
extract_sha256: "f893056b3839404559f25f7d3c01d0170892f200ef9a6cbbbd32cd967b276689"
body_sha256: "0ca828e162ade7491eaee140020846fcea1665cb481029090c8277dde7311243"
verifier_version: "2"
verified_verdict: "pass"
verified_date: "20261106"
extract_source_sha256: "42ec98713b2c0e30fc633fb59529a3503588ce34533f142cfda614a92c025815"
---

# Verified Claims — Kreuk et al. (2019)

Each claim below was extracted by reading the downloaded paper file with the Read
tool, grepping for the specific content, and reading the surrounding context to
confirm the attribution is faithful.

Source: arXiv:1902.03083v2, the arXiv HTML rendering saved as `literature/kreuk_2019.html`.
Authors: Felix Kreuk, Yossi Adi, Bhiksha Raj, Rita Singh and Joseph Keshet (Bar-Ilan University;
Facebook AI Research; Carnegie Mellon University). The DOI is not printed in the extract, so the
DOI field is left unset. References [1] and [2] in the quotes are Baluja 2017, *Hiding images in
plain sight: Deep steganography*, and Zhu et al. 2018, *HiDDeN*; neither has a ledger. Locations
below are section headings of the HTML.

## Claim 1: Approach — speech-in-speech steganography by an image-style encoder–decoder network with differentiable STFT and inverse-STFT layers

> "We build on the work by  [ 1 ,  2 ]  and propose a new model that includes the STFT and inverse-STFT as differentiable layers within the network, thus imposing a vital constraint on the network outputs."

> "Similarly to  [ 1 ,  2 ] , the proposed model is comprised of three parts. The first learns to encode a hidden message inside the carrier. The second component are differential STFT and inverse-STFT layers that simulate transformations between frequency and time domains. Lastly, the third component learns to decode a hidden message from a generated carrier."

**ID:** approach-hide-and-speak
**Location:** Section 1 "Introduction"
**Grep command used:** `Grep pattern="We build on the work by|the proposed model is comprised of three parts" path="literature/extracted/kreuk_2019.txt"`

---

## Claim 2: Security notion — perceptual: a human evaluator should not detect the hidden message; the message must be recoverable and intelligible

> "such that the following constraints are satisfied: (i) both ... should be perceptually similar to ... respectively, by a human evaluator; (ii) the message ... should be recoverable from the carrier ... and should be intelligible; and lastly (iii) a human evaluator should not be able to detect the presence of a hidden message embedded in"

**ID:** human-perceptual-security
**Location:** Section 2 "Notation and representation", Steganography notations (the ellipses stand for inline mathematics naming the carrier and message symbols)
**Grep command used:** `Grep pattern="following constraints are satisfied|perceptually similar to|a human evaluator should not be able to detect" path="literature/extracted/kreuk_2019.txt"`

---

## Claim 3: What it needs — learned, not hand-designed, redundancy; the trained networks are the means of hiding and recovery

> "Unlike traditional steganography methods  [ 3 ,  4 ] , in this line of work, the network  learns  to conceal a hidden message inside the carrier without manually specifying a particular redundancy to exploit."

> "Each of the above components is a neural network, where the parameters are found by minimizing the absolute error between the carrier and the embedded carrier and between the original message and the reconstructed message."

> "All models were trained using Adam for 80 epochs with an initial learning rate of  10 − 3 10^{-3}  and a decaying factor of 10 every 20 epochs."

**ID:** learned-redundancy-training
**Location:** Section 1 "Introduction"; Section 3 "Model"; Section 4 "Experimental results"
**Grep command used:** `Grep pattern="without manually specifying a particular redundancy|parameters are found by minimizing|trained using Adam for 80 epochs" path="literature/extracted/kreuk_2019.txt"`

---

## Claim 4: Vision models transferred directly to speech fail — low carrier error, but unintelligible messages after the time-domain round trip

> "Notice, while both  [ 1 ]  and  [ 2 ]  yield low carrier errors, their direct application to speech data produced unintelligible messages with a low SNR. This is due to the fact that these models were not constrained to retain the same carrier content after the conversion to time-domain and back."

**ID:** vision-models-fail-on-speech
**Location:** Section 4 "Experimental results"
**Grep command used:** `Grep pattern="yield low carrier errors" path="literature/extracted/kreuk_2019.txt"`

---

## Claim 5: Multiple messages for separate recipients in one carrier, at a cost in quality as the count rises

> "Additionally, we demonstrated for the first time, that the above scheme now permits us to hide  multiple  secret messages into a  single  carrier, each potentially with a different intended recipient who is the only person who can recover it."

> "An increase in the number of messages translates to higher loss values both for carrier and for messages. These results are to be expected as the model is forced to work at higher compression rates due to concealing and recovering more messages while keeping the carrier dimension the same."

**ID:** multiple-messages-recipients
**Location:** Section 1 "Introduction"; Section 4, "Multiple messages."
**Grep command used:** `Grep pattern="different intended recipient|An increase in the number of messages" path="literature/extracted/kreuk_2019.txt"`

---

## Claim 6: Detectability by ear — in ABX tests listeners told stego from clean carriers 51.2% of the time, against a chance rate of 50%

> "Only 51.2% (48.8% for TIMIT and 53.6% for YOHO) of the carriers embedded with hidden messages could be distinguished from the original ones by humans (the optimal ratio is 50%). Therefore we conclude that the modifications made by the steganographic function are not detectable by the human ear."

**ID:** abx-human-detectability
**Location:** Section 5.1 "Carrier ABX testing"
**Grep command used:** `Grep pattern="Only 51.2%" path="literature/extracted/kreuk_2019.txt"`

---

## Claim 7: Message quality — transcription error unchanged, and speaker identity largely preserved

> "The CER/WER measured on original and reconstructed messages were 5.1%/2.86% and 5.15%/2.78% respectively."

> "The Equal Error Rate (EER) of the system is 18% (82% accuracy) on the generated messages, and 15% EER (85% accuracy) on the original messages."

**ID:** intelligibility-speaker-identity
**Location:** Section 5.2 "Message intelligibility"; Section 5.3 "Speaker recognition"
**Grep command used:** `Grep pattern="CER/WER measured on original|Equal Error Rate \(EER\) of the system" path="literature/extracted/kreuk_2019.txt"`

---

## Claim 8: Robustness — survives down-sampling, MP3 and added noise, but not a cut in bit precision

> "Results suggest that our method is robust to carrier down-sampling, MP3 compression and noise addition. Contrarily, the model is sensitive to bit precision change, but this is to be expected as the message decoder relies on miniscule carrier modification in order to reconstruct the hidden message."

**ID:** channel-robustness
**Location:** Section 5.4 "Robustness to channel distortion"
**Grep command used:** `Grep pattern="robust to carrier down-sampling" path="literature/extracted/kreuk_2019.txt"`

---

## Claim 9: An adversarial loss improves the carrier at the cost of message accuracy

> "Similarly to the effect on images, when incorporating the adversarial loss, the carrier quality improved and contained less artifacts, however it comes with the cost of less accurate message reconstruction."

**ID:** adversarial-loss-tradeoff
**Location:** Section 4 "Experimental results"
**Grep command used:** `Grep pattern="when incorporating the adversarial loss" path="literature/extracted/kreuk_2019.txt"`

---

## Claim 10: Stated limit — no evaluation against steganalysis; evasion of detectors is left to future work

> "For future work we would like to explore the ability of such steganographic methods to evade detection by steganalysis algorithms, and incorporate such evasion capabilities as part of the training pipeline."

**ID:** no-steganalysis-evaluation
**Location:** Section 7 "Discussion and future work"
**Grep command used:** `Grep pattern="evade detection by steganalysis algorithms" path="literature/extracted/kreuk_2019.txt"`
