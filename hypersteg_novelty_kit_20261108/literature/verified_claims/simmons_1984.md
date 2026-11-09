---
paper: "Simmons (1984)"
title: "The Prisoners' Problem and the Subliminal Channel"
doi: "<DOI>"
pmcid: "<PMC ID, if any>"
url: "Advances in Cryptology: Proceedings of Crypto 83, ed. D. Chaum, Plenum Press, New York, 1984, pp. 51–67 (local scan, literature/simmons_1984.pdf)"
source_version: "published"
file: "literature/simmons_1984.pdf"
retrieved: "20261106"
verified_by: "Claude (Opus 5.5) subagent, quotes checked with verify_quotes.py (read-only run)"
# The six below are written by `verify_quotes.py --stamp` — do not hand-edit.
# They bind the ledger to the exact source/extract bytes AND its own quoted text
# (body_sha256) it was verified against, so a later quote edit is caught in CI.
source_sha256: "c47fb8a0e1437ebf846755970d71905aeef98658f1c0677570498cd46584ee96"
extract_sha256: "572c87c19f9e5da54c5fd77325590de8e7b30b4c359af02105158bdca96de689"
body_sha256: "6ff4a958a894688c0ab7fa1bc095477f0595b39407e3d2f5b55a582e43683014"
verifier_version: "2"
verified_verdict: "pass"
verified_date: "20261106"
extract_source_sha256: "c47fb8a0e1437ebf846755970d71905aeef98658f1c0677570498cd46584ee96"
---

# Verified Claims — Simmons (1984)

Each claim below was extracted by reading the extracted text of the paper with the Read
tool, grepping for the specific content, and reading the surrounding context to
confirm the attribution is faithful.

Source: Advances in Cryptology: Proceedings of Crypto 83 (D. Chaum, ed.), Plenum Press, New
York, 1984, pp. 51–67 (scanned publisher pages). Single author: Gustavus J. Simmons, Sandia
National Laboratories. The extract is OCR of a scan: some characters are garbled (e.g. "will
he" for "will be", "~" for Greek letters), and the quotes below reproduce the extract as it
stands. The DOI is not printed in the extract. Page numbers are the printed proceedings pages.

## Claim 1: Prisoners' framing — two prisoners in separate cells communicate only through the warden's agents

> "Two accomplices in a crime have been arrested and are about to be locked in widely separated cells. Their only means of communication after they are locked up will he by way of messages conveyed for them by trustees -- who are known to be agents of the warden."

**ID:** prisoners-framing
**Location:** p. 51, "Introduction"
**Grep command used:** `/usr/bin/grep -n "Two accomplices in a crime\|known to be agents of the" literature/extracted/simmons_1984.txt`

---

## Claim 2: Threat model — an active warden who reads every message and tries to deceive the prisoners with forged or modified messages

> "The warden is willing to allow the prisoners to exchange messages in the hope that he can deceive at least one of them into accepting as a genuine communication from the other either a fraudulent message created by the warden himself or else a modification by him of a genuine message."

> "Even in the most general scheme, the opponent has only these two types of deceit available as his options; (a) impersonation or (b) substitution."

**ID:** active-warden-impersonation-substitution
**Location:** p. 51, "Introduction"; p. 55
**Grep command used:** `/usr/bin/grep -n "deceive at least one of them\|types of deceit available" literature/extracted/simmons_1984.txt`

---

## Claim 3: Channel condition — the warden permits exchange only if message content is fully open to him; the prisoners insist on authentication

> "the warden will only permit the exchanges to occur if the information contained in the messages is completely open to him -- and presumably innocuous."

> "Since they anticipate that the warden will try to deceive them by introducing fraudulent messages, ... they will only exchange messages if they are permitted to authenticate them."

**ID:** open-content-authenticated-channel
**Location:** pp. 51–52, "Introduction" (the second quote runs across the page break; the ellipsis marks the footnotes and running head the extract places between its halves)
**Grep command used:** `/usr/bin/grep -n "completely open to him\|introducing fraudulent messages\|permitted to authenti" literature/extracted/simmons_1984.txt`

---

## Claim 4: Subliminal channel — secret communication in full view of the warden, not by coded selection of messages or prearranged code words

> "To do this they will have to deceive the warden by finding a way of communicating secretly in the exchanges, i.e., of establishing a 'subliminal channel' between them in full view of the warden, even though the messages themselves contain no secret (to the warden) information"

> "this description is strictly true, i.e., the secret communication is not by way of a coded selection of messages or of prearranged code words appearing in a message, etc."

**ID:** subliminal-channel-definition
**Location:** p. 51, "Introduction" and its footnote (marked * in the extract)
**Grep command used:** `/usr/bin/grep -n "in full view of\|coded selection of messages" literature/extracted/simmons_1984.txt`

---

## Claim 5: Subliminal channel in authentication — a subversion by the prisoners of an authentication-without-secrecy channel

> "the subliminal channel is actually a subversion (by the transmitter/receiver), of the authentication channel."

> "Authentication depends on the transmitter introducing prearranged redundant information into the messages, the presence of which in a decrypted cipher will be interpreted by the receiver as indicating that the communication is genuine."

**ID:** subversion-of-authentication
**Location:** p. 52, "Authentication Without Secrecy"
**Grep command used:** `/usr/bin/grep -n "actually a subversion\|introducing pre" literature/extracted/simmons_1984.txt`

---

## Claim 6: Warden's check — the host verifies that the cipher decrypts to exactly the message he expected

> "the host to the communication channel verifies that nothing has been concealed by decrypting the ciphers and verifying that the resulting message is precisely what he expected based on a foreknowledge of the message."

**ID:** warden-verifies-expected-message
**Location:** p. 53, "Authentication Without Secrecy", point (b)
**Grep command used:** `/usr/bin/grep -n "verifies that noth\|foreknowledge of the message" literature/extracted/simmons_1984.txt`

---

## Claim 7: Capacity — the prisoners trade authentication capacity bit for bit for subliminal capacity

> "Conceivably the transmitter/receiver could give up some of their ability to authenticate -- without the host being aware of this -- and use the resulting information capacity, say Hs bits, to communicate secretly."

> "the transmitter/receiver can exchange -- unbeknown to the host -- part or all of this ability to authenticate for a corresponding bit-for-bit capability of subliminal communication."

**ID:** capacity-bit-for-bit-from-authentication
**Location:** p. 54, "The Subliminal Channel"; p. 66, "Conclusion"
**Grep command used:** `/usr/bin/grep -n "give up some of their\|bit-for-bit" literature/extracted/simmons_1984.txt`

---

## Claim 8: What is shared — a secret key chosen by the prisoners, in secret from the warden, from a key list partitioning the message space that both sides agreed in advance

> "what the warden and the prisoners would have agreed to in advance would be a key list or in actual practice an equivalent functional description of a partitioning of the message space by keys"

> "After the prisoners have been locked up, having selected in secret from the warden one of the sixteen possible keys, there are two ways the warden might attempt to deceive one of them."

**ID:** shared-secret-key-from-key-list
**Location:** p. 54; p. 55
**Grep command used:** `/usr/bin/grep -n "agreed to in advance would be a key list\|selected in secret" literature/extracted/simmons_1984.txt`

---

## Claim 9: Detectability through feedback — repeated deception attempts with success feedback would reveal the weakened authentication

> "if he could make sufficiently many attempts at deception with this scheme, with feedback on each attempt as to whether he had succeeded or not, he could quickly infer that something was amiss"

> "This is not a problem in actual applications through since the probability of success is chosen to be very very small so that it is infeasible to estimate it by testing of the channel."

**ID:** detection-by-success-rate-feedback
**Location:** p. 58
**Grep command used:** `/usr/bin/grep -n "sufficiently\|very very small" literature/extracted/simmons_1984.txt`

---

## Claim 10: Security notion — computational: the channel's existence is as hard to detect as factoring a product of three primes

> "a single bit subliminal channel that is as cryptosecure as a product of three large primes is difficult to factor, and whose existence is as hard to detect as the associated factoring problem."

> "They do not tell the host that the modulus is the product of three primes -- a fact that is as hard for him to verify as it would be for him to factor n."

**ID:** computational-undetectability-factoring
**Location:** p. 60; p. 63
**Grep command used:** `/usr/bin/grep -n "as cryptosecure as\|hard for him to verify" literature/extracted/simmons_1984.txt`

---

## Claim 11: Mechanism — the choice between authentic square roots carries the subliminal bit

> "selects the pair that satisfy the authentication criteria and then sends the smaller of these roots to communicate a subliminal 0 or the larger to communicate a 1."

> "it is feasible to design cryptoalgorithms in which several ciphers decrypt to the same message, and hence in which it is possible to communicate some side information, over and above that in the message itself, by way of the identity of the particular cipher used."

**ID:** cipher-choice-carries-bit
**Location:** p. 64; p. 66, "Conclusion"
**Grep command used:** `/usr/bin/grep -n "sends the\|several ciphers decrypt to the same" literature/extracted/simmons_1984.txt`

---

## Claim 12: Limitation — the warden cannot detect the channel but can forge accepted messages by forward search

> "Although the warden can't detect that the prisoners are exchanging a secret bit in each message, he can with probability as close to 1 as he wishes deceive one of them into accepting a forgery as an authentic message."

**ID:** forward-search-forgery
**Location:** p. 65
**Grep command used:** `/usr/bin/grep -n "can't detect that the" literature/extracted/simmons_1984.txt`

---

## Claim 13: Approach — the subliminal channel: authentication schemes in which several ciphers decrypt to the same message, so the choice of cipher carries side information as hard to detect as the cryptoalgorithm is to break

> "In this paper we describe one way to realize such a subliminal channel, i.e., a solution to the prisoners' problem."

> "A simplified statement of this conclusion is that it is feasible to design cryptoalgorithms in which several ciphers decrypt to the same message, and hence in which it is possible to communicate some side information, over and above that in the message itself, by way of the identity of the particular cipher used."

> "it was shown that such a subliminal channel can be made just as difficult to detect as the underlying cryptoalgorithm is difficult to break."

**ID:** approach-subliminal-channel
**Location:** Introduction, p. 52; concluding section, p. 66 (the closing summary sits just before the References)
**Grep command used:** `/usr/bin/grep -n "one way to realize such\|several ciphers decrypt\|difficult to detect as the underlying" literature/extracted/simmons_1984.txt`
