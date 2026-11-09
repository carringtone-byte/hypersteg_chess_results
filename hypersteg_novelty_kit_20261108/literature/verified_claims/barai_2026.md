---
paper: "Barai (2026)"
title: "High-Capacity Steganographic Encoding Using Legal Chess PGN with Authenticated Encryption"
doi: "<DOI>"
pmcid: "<PMC ID, if any>"
url: "Independent preprint dated January 2026; no venue, DOI or URL is printed in the extract"
source_version: "preprint"
file: "literature/barai_2026.pdf"
retrieved: "20261105"
verified_by: "Claude (Opus 5.5) subagent, quotes checked with verify_quotes.py (read-only run)"
# The six below are written by `verify_quotes.py --stamp` — do not hand-edit.
# They bind the ledger to the exact source/extract bytes AND its own quoted text
# (body_sha256) it was verified against, so a later quote edit is caught in CI.
source_sha256: "369a8e657bcfe6c7544b128180ee014d478c039b30ef4cec2d51a041766b4656"
extract_sha256: "25d2c071232a8b06368c433b81dd0dec32c38a02abf95ebf4f0d9b7a708a6dec"
body_sha256: "4445a0b8113e09029195a8fc672661977bbde1406791393894e9d77d4c5f9374"
verifier_version: "2"
verified_verdict: "pass"
verified_date: "20261106"
extract_source_sha256: "369a8e657bcfe6c7544b128180ee014d478c039b30ef4cec2d51a041766b4656"
---

# Verified Claims — Barai (2026)

Each claim below was extracted by reading the downloaded paper file with the Read
tool, grepping for the specific content, and reading the surrounding context to
confirm the attribution is faithful.

Source: single-author preprint, Atharva Sen Barai, "Independent Researcher", dated January 2026.
The extract prints no venue, DOI, arXiv ID or page numbers, so locations below are section
numbers. The paper is not peer reviewed as far as the extract shows, and its security claims
rest on the author's own observation (see Claim 8). Its experimental table is internally
uneven: a 437-byte message is listed at 900 plies and a 500-byte message at 298 plies (Section
7.1); this ledger records the table, it does not reconcile it.

## Claim 1: Carrier — the move sequence of a legal chess game written as PGN, with variation trees for extra room

> "We present a novel steganographic system that embeds encrypted messages within legal chess game notation (PGN) using rule-constrained symbolic encoding."

> "When the mainline capacity is exhausted, the system utilizes chess variations to provide theoretically unbounded encoding capacity constrained by practical PGN size limits."

**ID:** pgn-move-sequence-carrier
**Location:** Abstract; Section 3 "System Overview"
**Grep command used:** `Grep pattern="embeds encrypted messages within|mainline capacity is exhausted" path="literature/extracted/barai_2026.txt"`

---

## Claim 2: Encoding — mixed-radix integer to moves: legal moves sorted by UCI string, each position a base-n digit

> "For each board position, legal moves are sorted lexicographically by their UCI (Universal Chess Interface) notation to ensure deterministic ordering across implementations."

> "This algorithm treats each chess position as a base-n number system where n equals the number of legal moves available. The encoding continues until the integer is fully consumed or the game reaches a terminal state."

**ID:** mixed-radix-legal-move-index
**Location:** Section 5.1 "Integer-to-Move Mapping"
**Grep command used:** `Grep pattern="sorted lexicographically|base-n number system" path="literature/extracted/barai_2026.txt"`

---

## Claim 3: Move quality plays no part — any legal move may be chosen, so the cover game is not constrained to plausible play

> "The deterministic move selection based on encrypted (random) data ensures that move frequencies and patterns remain consistent with natural chess play variations."

> "Games encoding megabytes of data would require thousands of moves, potentially appearing artificial."

**ID:** uniform-legal-move-selection
**Location:** Section 8.2 "Statistical Indistinguishability"; Section 9.1 "Scalability Constraints"
**Grep command used:** `Grep pattern="deterministic move selection based on encrypted|potentially appearing artificial" path="literature/extracted/barai_2026.txt"`

---

## Claim 4: Encrypt-then-embed — AES-256-GCM with optional PBKDF2 password layer; the ciphertext becomes the integer

> "The encoding process begins with optional password-based encryption using PBKDF2 key derivation, followed by AES-256-GCM authenticated encryption. The resulting ciphertext is converted to a large integer"

> "GCM mode was selected for its authenticated encryption properties, which detect any modification to the ciphertext without requiring separate integrity mechanisms."

**ID:** aes-gcm-encrypt-then-embed
**Location:** Section 3 "System Overview"; Section 4.1 "Encryption Layer"
**Grep command used:** `Grep pattern="optional password-based encryption|GCM mode was selected" path="literature/extracted/barai_2026.txt"`

---

## Claim 5: Pre-agreed — the key or password and the public algorithm; the threat model assumes the adversary may know the algorithm

> "May have knowledge of the encoding algorithm through source code analysis"

> "Does not possess the encryption keys or user passwords"

> "We assume the adversary cannot compromise the underlying cryptographic primitives (AES-256, PBKDF2) under standard cryptographic assumptions"

**ID:** kerckhoffs-threat-model
**Location:** Section 2 "Threat Model"
**Grep command used:** `Grep pattern="knowledge of the encoding algorithm|Does not possess the encryption keys|cannot compromise the underlying" path="literature/extracted/barai_2026.txt"`

---

## Claim 6: Deniability goal is set only against casual observation

> "Deniability: PGN appears as legitimate chess content to casual observation"

> "Can attempt statistical analysis of chess move patterns"

**ID:** deniability-casual-observer
**Location:** Section 2 "Threat Model"
**Grep command used:** `Grep pattern="legitimate chess content to casual|statistical analysis of chess move" path="literature/extracted/barai_2026.txt"`

---

## Claim 7: Capacity — about 4.3 bits per ply, from about 20 legal moves per position; about 430 bits for a 100-move game

> "Average legal moves per position: ~20"

> "100-move game capacity: ~430 bits (54 bytes)"

> "The system demonstrates efficient capacity utilization with an average encoding rate of 4.3 bits per chess ply, closely matching the theoretical maximum based on legal move availability."

**ID:** capacity-bits-per-ply
**Location:** Section 5.3 "Encoding Capacity Analysis"; Section 7.2 "Capacity Utilization"
**Grep command used:** `Grep pattern="Average legal moves per position|100-move game capacity|average encoding rate" path="literature/extracted/barai_2026.txt"`

---

## Claim 8: Security evidence — authors' empirical observation only; no detector, no rate, no formal proof

> "We do not claim information-theoretic steganographic security; indistinguishability claims are based on empirical observation rather than formal proof."

> "produces games that exhibit no observable statistical patterns correlating with the hidden message in conducted experiments."

**ID:** security-by-empirical-observation
**Location:** Section 8.2 "Statistical Indistinguishability"
**Grep command used:** `Grep pattern="We do not claim information|no observable statistical patterns" path="literature/extracted/barai_2026.txt"`

---

## Claim 9: Robustness — fragile by design: any change to the moves breaks decryption, which is read as tamper detection

> "Any modification to the PGN that changes the encoded integer will result in authentication failure during decryption, immediately alerting to potential tampering."

> "Variations in PGN format interpretation or chess engine implementations could potentially affect decoding reliability across different platforms."

**ID:** fragile-tamper-evident
**Location:** Section 6.2 "Tamper Detection"; Section 9.3 "Format Dependencies"
**Grep command used:** `Grep pattern="changes the encoded integer|Variations in PGN format interpretation" path="literature/extracted/barai_2026.txt"`

---

## Claim 10: Results — messages up to about 22 kB encoded, all decoded; the largest needs 42,416 plies and 1,149 variations

> "21,899 bytes 276,277 chars 42,416 plies 1,149 156.26 s"

> "All test cases achieved 100% successful decoding with perfect message reconstruction, demonstrating the deterministic nature of the encoding/decoding algorithms."

**ID:** encoding-results-table
**Location:** Section 7.1 "Encoding Performance" (table); Section 7.3 "Decoding Accuracy"
**Grep command used:** `Grep pattern="42,416 plies|All test cases achieved" path="literature/extracted/barai_2026.txt"`

---

## Claim 11: Acknowledged detection risk — long games and unusual variation patterns may draw behavioural analysis

> "extremely long games with unusual variation patterns might attract attention from sophisticated adversaries conducting behavioral analysis of chess content."

> "Analysis of potential detection methods and development of countermeasures to improve resistance against sophisticated statistical analysis."

**ID:** acknowledged-behavioural-detection
**Location:** Section 9.4 "Detection Through Analysis"; Section 12 "Future Work"
**Grep command used:** `Grep pattern="unusual variation patterns|Analysis of potential detection methods" path="literature/extracted/barai_2026.txt"`

---

## Claim 12: Approach — encrypt, then write the ciphertext as a legal chess game: AES-256-GCM output, read as a large integer, is mapped deterministically to a sequence of legal moves in PGN, with variation trees for longer messages

> "We present a novel steganographic system that embeds encrypted messages within legal chess game notation (PGN) using rule-constrained symbolic encoding. Our method combines AES-256-GCM authenticated encryption with a deterministic chess move selection algorithm that maps large integers to sequences of legal chess moves."

> "The system achieves theoretically unbounded capacity constrained by practical PGN size limits through chess variation trees while maintaining plausible deniability and tamper detection."

**ID:** approach-pgn-mixed-radix
**Location:** Abstract
**Grep command used:** `Grep pattern="We present a novel steganographic system that embeds|achieves theoretically unbounded capacity" path="literature/extracted/barai_2026.txt"`
