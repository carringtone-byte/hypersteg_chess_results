---
generated: 2026-11-08T20:09:54+03:00
---

# Approach map — mechanism class overt-encoding

Built by `tools/build_approach_map.py` from `C:\Users\user\Documents\GitHub\hypersteg_chess\hypersteg_novelty_kit_20261108\literature\verified_claims`, the features table `C:\Users\user\Documents\GitHub\hypersteg_chess\hypersteg_novelty_kit_20261108\maps\approach_features.tsv` and the mechanism taxonomy `C:\Users\user\Documents\GitHub\hypersteg_chess\hypersteg_novelty_kit_20261108\maps\mechanism_taxonomy.tsv`. Mechanism overview: [approach_map_mechanisms.md](approach_map_mechanisms.md). Each approach leaf names its paper family.

- mechanisms: 4
- approaches: 8
- families: 2 (llm-capability-eval, llm-generative-text)

```mermaid
flowchart TD
  subgraph cls_overt_encoding_g["overt-encoding"]
    cls_overt_encoding("overt-encoding")
    mech_m_byte_encoding{{"Byte encodings"}}
    mech_m_letter_substitution_cipher{{"Letter rotation and substitution ciphers"}}
    mech_m_overt_encoding{{"Overt encodings and ciphers"}}
    mech_m_partial_word_cipher{{"Partial word-level cipher"}}
    n_anwar_2026_surveyed_rot13_partial_encoding["word-level Rot13 encoding applied with probability p, as a …<br/>anwar_2026<br/>family: llm-capability-eval"]
    n_motwani_2024_surveyed_standard_ciphers["standard ciphers (Base64, Caesar) as an encoding capability<br/>motwani_2024<br/>family: llm-generative-text"]
    n_tailor_2026_surveyed_base64["Base64 (prescribed rule)<br/>tailor_2026<br/>family: llm-generative-text"]
    n_tailor_2026_surveyed_eight_bit_binary["eight-bit binary (prescribed rule)<br/>tailor_2026<br/>family: llm-generative-text"]
    n_tailor_2026_surveyed_fixed_letter_substitution["fixed-letter substitution (prescribed rule)<br/>tailor_2026<br/>family: llm-generative-text"]
    n_tailor_2026_surveyed_hexadecimal["hexadecimal (prescribed rule)<br/>tailor_2026<br/>family: llm-generative-text"]
    n_zolkowski_2025_surveyed_byte_encodings["byte-encoding schemes (Base64, UTF-8 binary, Hex and their …<br/>zolkowski_2025<br/>family: llm-generative-text"]
    n_zolkowski_2025_surveyed_rotation_substitution["rotation and substitution ciphers<br/>zolkowski_2025<br/>family: llm-generative-text"]
  end
  mech_m_overt_encoding --- mech_m_byte_encoding
  mech_m_overt_encoding --- mech_m_letter_substitution_cipher
  cls_overt_encoding --- mech_m_overt_encoding
  mech_m_letter_substitution_cipher --- mech_m_partial_word_cipher
  mech_m_partial_word_cipher --- n_anwar_2026_surveyed_rot13_partial_encoding
  mech_m_byte_encoding --- n_motwani_2024_surveyed_standard_ciphers
  mech_m_letter_substitution_cipher --- n_motwani_2024_surveyed_standard_ciphers
  mech_m_byte_encoding --- n_tailor_2026_surveyed_base64
  mech_m_byte_encoding --- n_tailor_2026_surveyed_eight_bit_binary
  mech_m_letter_substitution_cipher --- n_tailor_2026_surveyed_fixed_letter_substitution
  mech_m_byte_encoding --- n_tailor_2026_surveyed_hexadecimal
  mech_m_byte_encoding --- n_zolkowski_2025_surveyed_byte_encodings
  mech_m_letter_substitution_cipher --- n_zolkowski_2025_surveyed_rotation_substitution
  linkStyle 0,1,2,3,4,5,6,7,8,9,10,11,12 stroke:#9e9e9e,stroke-width:1px
```

## Mechanisms

| mechanism | parent | class | name | definition | grounded by | landing | approaches |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `m-byte-encoding` | m-overt-encoding | overt-encoding | Byte encodings | The message is written as Base64, UTF-8 binary or hexadecimal, possibly with bit swaps, rotations or repeated application. | `zolkowski_2025:surveyed-byte-encodings` | yes | 5 |
| `m-letter-substitution-cipher` | m-overt-encoding | overt-encoding | Letter rotation and substitution ciphers | Each letter is rotated by N places or replaced under a provided character mapping. | `zolkowski_2025:surveyed-rotation-substitution` | yes | 4 |
| `m-overt-encoding` | — | overt-encoding | Overt encodings and ciphers | The message is transformed by a standard encoding or cipher and written into the text, which hides its content but not that something is encoded. | `tailor_2026:surveyed-base64` | yes | 8 |
| `m-partial-word-cipher` | m-letter-substitution-cipher | overt-encoding | Partial word-level cipher | Rot13 is applied to each word independently with probability p, interpolating between legible and fully enciphered text. | `anwar_2026:surveyed-rot13-partial-encoding` | yes | 1 |

## Approaches

| address | name | family | technique | channel | key | access | capacity | mechanism | landable | mechanism_evidence | carrier | acquisition |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `anwar_2026:surveyed-rot13-partial-encoding` | word-level Rot13 encoding applied with probability p, as a graded steganography simulation | llm-capability-eval | lce-partial-encoding | lexical | codebook | prompt | — | m-partial-word-cipher | yes | own | words in a reasoning trace | specified |
| `motwani_2024:surveyed-standard-ciphers` | standard ciphers (Base64, Caesar) as an encoding capability | llm-generative-text | lgt-byte-encodings; lgt-substitution-ciphers | other (cipher encoding, not hidden) | codebook | prompt | — | m-byte-encoding; m-letter-substitution-cipher | yes | own;own | encoded string in text | prompted |
| `tailor_2026:surveyed-base64` | Base64 (prescribed rule) | llm-generative-text | lgt-byte-encodings | other (literal Base64 string) | codebook | prompt | — | m-byte-encoding | yes | own | encoded string in text | prompted |
| `tailor_2026:surveyed-eight-bit-binary` | eight-bit binary (prescribed rule) | llm-generative-text | lgt-byte-encodings | other (literal binary string) | codebook | prompt | eight binary digits per character | m-byte-encoding | yes | own | encoded string in text | prompted |
| `tailor_2026:surveyed-fixed-letter-substitution` | fixed-letter substitution (prescribed rule) | llm-generative-text | lgt-substitution-ciphers | other (substitution-cipher letters) | codebook | prompt | — | m-letter-substitution-cipher | yes | own | enciphered letters in text | prompted |
| `tailor_2026:surveyed-hexadecimal` | hexadecimal (prescribed rule) | llm-generative-text | lgt-byte-encodings | other (literal hex string) | codebook | prompt | — | m-byte-encoding | yes | own | encoded string in text | prompted |
| `zolkowski_2025:surveyed-byte-encodings` | byte-encoding schemes (Base64, UTF-8 binary, Hex and their variants) | llm-generative-text | lgt-byte-encodings | other (overt encoding) | codebook | prompt | — | m-byte-encoding | yes | own | encoded string in text | prompted |
| `zolkowski_2025:surveyed-rotation-substitution` | rotation and substitution ciphers | llm-generative-text | lgt-substitution-ciphers | other (overt cipher) | codebook | prompt | — | m-letter-substitution-cipher | yes | own | enciphered letters in text | prompted |
