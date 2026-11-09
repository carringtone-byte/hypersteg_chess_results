---
paper: "Zhang, Liu, Ke, Lei, Li, Zhang and Yang (2019)"
title: "Generative Steganography by Sampling"
doi: "10.1109/ACCESS.2019.2920313"
pmcid: "<PMC ID, if any>"
url: "IEEE Access, vol. 7, pp. 118586–118597, 2019 (published 31 May 2019)"
source_version: "published"
file: "literature/zhang_2018.pdf"
retrieved: "20261106"
verified_by: "Claude (Opus 5.5) subagent image1, quotes checked with verify_quotes.py (read-only run)"
# The six below are written by `verify_quotes.py --stamp` — do not hand-edit.
# They bind the ledger to the exact source/extract bytes AND its own quoted text
# (body_sha256) it was verified against, so a later quote edit is caught in CI.
source_sha256: "c0f64932b6fd8692f9485a95b2e6c091de80d2bb74ec3988b427f2b732fba72f"
extract_sha256: "ffed8fa4a55b550285d5e0044dd00c2609023cb4d5e86e0943905df2109bc3af"
body_sha256: "e5fc3553856d885a1780d83005cc3c25de7aa7462d790990bc7a5bd389a0d2c3"
verifier_version: "2"
verified_verdict: "pass"
verified_date: "20261106"
extract_source_sha256: "c0f64932b6fd8692f9485a95b2e6c091de80d2bb74ec3988b427f2b732fba72f"
---

# Verified Claims — Zhang, Liu, Ke, Lei, Li, Zhang and Yang (2019)

Each claim below was extracted by reading the downloaded paper file with the Read
tool, grepping for the specific content, and reading the surrounding context to
confirm the attribution is faithful.

Source: IEEE Access, vol. 7, 2019, pp. 118586–118597 (received 20 April 2019, published 31 May
2019). Authors: Zhuo Zhang (Rocket Force University of Engineering), Jia Liu, Yan Ke, Yu Lei,
Jun Li, Minqing Zhang and Xiaoyuan Yang (Engineering University of the People's Armed Police).
The extract prints the DOI as "10.1 109/ACCESS.2019.2920313", with a stray space; the DOI field
above removes it. Page numbers below are the journal page numbers printed in the extract.

**Key.** The file is `literature/zhang_2018.pdf`, so this ledger carries the key `zhang_2018`
to match the file and its extract. The paper itself is a 2019 publication. In
`literature/REGISTER.tsv` it sits under key `zhang_2019`, which belongs to a different paper
(SteganoGAN, Zhang, Cuesta-Infante, Xu and Veeramachaneni, ledgered as `zhang_2019` from
`literature/zhang_2019.html`). A collision-free key for this paper would be `zhang_2019b`; the
rename is left to the host. `literature/zhang_2019.pdf` is a symbolic link to this file.

## Claim 1: Method — the stego image is sampled by a trained generator; no explicit cover

> "In this paper, a novel data-driven information hiding scheme called ‘‘generative steganography by sampling’’ (GSS) is proposed. Unlike in traditional modiﬁcation-based steganography, in our method the stego image is directly sampled by a powerful generator: no explicit cover is used. Both parties share a secret key used for message embedding and extraction."

> "Given a trained generative model, we search for the closest encoding of the stego image in the latent image manifold using a message loss and a prior losses, which are introduced as constraints on the sampling conditions to penalize message extraction error and unrealistic images."

**ID:** approach-gss
**Location:** Abstract, p. 118586; Section I "Introduction", p. 118587
**Grep command used:** `Grep pattern="a novel data-driven information hiding|search for the closest encoding" path="literature/extracted/zhang_2018.txt"`

---

## Claim 2: Practical instance — a digital Cardan grille marks where the message is written; semantic inpainting fills the rest

> "Based on this new framework, a practical cover synthesis method is proposed that is based on a mask called digital Cardan grille and semantic image inpainting. The digital Cardan grille is used to determine the location in which to hide the message."

> "The receiver places the grille directly on the generated image to extract the secret message in the corresponding position."

**ID:** approach-cardan-grille-inpainting
**Location:** Section I, p. 118587; Section IV-C "Message Extraction", p. 118592. The inpainting step follows Yeh et al. [22] ("we use the image inpainting method proposed by Y eh et al. [22] based on DCGAN [13]", Section IV-B, p. 118591); neither Yeh et al. nor the authors' earlier digital Cardan grille (Liu et al. 2018, [21]) has a ledger, so no lineage line is given.
**Grep command used:** `Grep pattern="mask called digital Cardan grille|places the grille directly" path="literature/extracted/zhang_2018.txt"`

---

## Claim 3: Generative steganography conditions — Gen(m, k), Ext(s, k), and stego distribution equal to the real one

> "Ideally, a generative steganography scheme should satisfy the following three conditions, which we call the generative steganography conditions (GSC):"

> "Ideally, pstego= preal, this condition guarantees the statistical security of the communication channel, which is a key issue for a generator to be used for generative steganography."

> "Interestingly, if we assume that all these conditions are satisﬁed, then generative steganography can be treated as a cover selection method in which it is possible to construct a fake database of inﬁnite size in which every sample contains a secret message."

**ID:** generative-steganography-conditions
**Location:** Section III-A "Representation Formula", p. 118588
**Grep command used:** `Grep pattern="generative steganography conditions|guarantees the statistical security|fake database of" path="literature/extracted/zhang_2018.txt"`

---

## Claim 4: Security notion — ε-security restated with the Jensen–Shannon divergence, after Cachin

> "We are motivated by the notion of ε-secure steganography proposed by Cachin [30], in which the relative entropy (also called the KL divergence) between the cover and stego distributions is less than or equal to ε."

> "Similar to Cachin’s ε-security for steganography [30], we deﬁne the concept of ε- security for generative steganography system based on the JS divergence:"

> "Ideally, when the generator is optimal (i.e., ε= 0) the system can be regarded as perfectly statistically secure against steganalysis."

**ID:** js-epsilon-security
**Location:** Section III-B "A Measure of Security", pp. 118588–118589 (reference [30] is Cachin, *An information-theoretic model for steganography*, Information Hiding 1998)
**Grep command used:** `Grep pattern="motivated by the notion|Similar to Cachin|perfectly statistically secure" path="literature/extracted/zhang_2018.txt"`

**Refines:** cachin_1998:relative-entropy-security (grounded by #js-epsilon-security)

---

## Claim 5: Stated limit of the security measure — JS divergence chosen because DCGAN uses it, not because it is ideal

> "Admittedly, the JS divergence is also not an ideal choice."

> "However, since a DCGAN is used to generate stego images later in this paper and the JS divergence is used in DCGAN, we use the JS divergence as our standard for security evaluation in this paper. Nevertheless, it should be noted that this is not the only option in the context of generative steganography frameworks."

**ID:** js-not-ideal
**Location:** Section III-B, p. 118589
**Grep command used:** `Grep pattern="JS divergence is also not an ideal|we use the JS divergence as our standard" path="literature/extracted/zhang_2018.txt"`

---

## Claim 6: Key — the grille is the shared key; the scheme is claimed to follow Kerckhoffs

> "Ck is a key shared by both parties."

> "It is important to note that the structure and location of this Cardan grille in the corrupted image are shared by both parties."

> "Note that our scheme is also key-dependent and adheres to Kerckhoff’s principle."

**ID:** grille-shared-key
**Location:** Section IV-A "Message Preprocessing", p. 118591; Section III-C "Constrained Sampling", p. 118589
**Grep command used:** `Grep pattern="Ck is a key shared|structure and location of this Cardan|adheres to Kerckhoff" path="literature/extracted/zhang_2018.txt"`

---

## Claim 7: Carrier — message written in a chosen bit plane of the kept pixels; higher bit planes survive generation better

> "In this paper, the message is written into the uncorrupted image region that must be preserved in the corrupted image through bit-plane embedding"

> "Intuitively, we expect that the lower bits will be more strongly affected by pixel generation, while higher bits will have greater stability."

**ID:** bit-plane-carrier
**Location:** Section IV "Generative Steganography by Inpainting", p. 118590; Section IV-B-3 "Message Loss", p. 118592
**Grep command used:** `Grep pattern="through bit-plane embed|lower bits will be more strongly" path="literature/extracted/zhang_2018.txt"`

---

## Claim 8: What the method needs — a trained DCGAN and 1,000 back-propagation iterations per stego image

> "We trained the DCGAN for 200 epochs on each ot the two datasets, CelebA and LWF, for 2 days and 1 day, respectively."

> "We terminated the back-propagation process 1,000 iterations."

**ID:** training-and-sampling-cost
**Location:** Section V-A "Datasets and Settings", pp. 118592–118593
**Grep command used:** `Grep pattern="200 epochs on each|terminated the back-propagation" path="literature/extracted/zhang_2018.txt"`

---

## Claim 9: Recovery is imperfect — above 70% at bit plane 7, falling as more is embedded

> "Due to the nonconvexity of the models in the training scheme, we cannot guarantee that the generator will converge to a model that can enable perfect recovery the secret message"

> "As expected, the accuracy of message extraction increased as the BPI value increased. The receiver was able to recover more than 70% at BPI= 7."

> "Compared with our previous work reported in [21], the message extraction stability is improved."

**ID:** improves-own-cardan-grille
**Location:** Section V-C "Quantitative Analysis", pp. 118593–118594 (reference [21] is Liu et al., *Digital Cardan grille: A modern approach for information hiding*, arXiv:1803.09219, 2018)
**Grep command used:** `Grep pattern="cannot guarantee that the generator will converge|more than 70% at BPI|Compared with our previous work" path="literature/extracted/zhang_2018.txt"`

---

## Claim 10: Capacity — 1.49e-3 to 1.10e-2 bytes per pixel, discounted by the extraction rate

> "The relative capacity of our method is 1.49e-3∼1.10e-2 bytes per pixel, where the lower and upper ends of this range correspond to image corrupted rates of 0.99 to 0.91, respectively"

> "extraction accuracy will be very low, so the high embedding amount does not have practical value, the actual capacity should be calculated as:"

**ID:** capacity-range
**Location:** Section V-C, p. 118595
**Grep command used:** `Grep pattern="1.49e-3|does not have practical value" path="literature/extracted/zhang_2018.txt"`

---

## Claim 11: Steganalysis — SPAM and SCRMQ1 ensemble classifiers; competitive with HUGO and HILL at low rates

> "In this experiment, we used 686-dimensional SPAM features [25] and 5,404-dimensional SCRMQ1 features [26] with an ensemble classiﬁer [27] implemented based on random forests."

> "The results in Fig.12 show that steganography based on sampling can resist statistical steganographic analysis, mainly because the completed stego and normal images can be regarded as samples from the distribution pg."

> "As shown in Fig. 12, our method performs competitively with HUGO [28] and HILL [29] for cases with a low embedding rate."

**ID:** steganalysis-spam-scrm
**Location:** Section V-C, pp. 118595–118596; Figure 12 (payloads 0.01 to 0.05 bpp at BPI = 7)
**Grep command used:** `Grep pattern="686-dimensional SPAM|can resist statistical steganographic analysis|performs competitively with HUGO" path="literature/extracted/zhang_2018.txt"`

---

## Claim 12: Position in the field — cover selection, modification and synthesis; synthesis is flexible but hard to automate

> "In Fridrich’s groundbreaking work of modern steganography [1], the possible steganographic channel are divided into three categories: cover selection, cover modiﬁcation and cover synthesis."

> "In practice, however, cover synthesis is so difﬁcult to automate that almost all known practical systems use modiﬁcation-based methods instead."

**ID:** three-channel-taxonomy
**Location:** Section I, p. 118586
**Grep command used:** `Grep pattern="divided into three categories|so difﬁcult to automate" path="literature/extracted/zhang_2018.txt"`

---

## Claim 13: Stated limit — the generator is the weak point and must keep improving for the scheme to stay secure

> "However, the design of the generator, which is trained by an adversarial network, is still in its infancy. In this paper, we used a simple DCGAN for image synthesis."

> "The performance of the generator must be continually reﬁned to ensure the security of generative steganography."

**ID:** generator-limit
**Location:** Section VI "Conclusions and Future Work", p. 118596
**Grep command used:** `Grep pattern="still in its infancy|must be continually reﬁned" path="literature/extracted/zhang_2018.txt"`
