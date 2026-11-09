---
generated: 2026-11-08T20:09:54+03:00
---

# Approach map — mechanism class key-establishment

Built by `tools/build_approach_map.py` from `C:\Users\user\Documents\GitHub\hypersteg_chess\hypersteg_novelty_kit_20261108\literature\verified_claims`, the features table `C:\Users\user\Documents\GitHub\hypersteg_chess\hypersteg_novelty_kit_20261108\maps\approach_features.tsv` and the mechanism taxonomy `C:\Users\user\Documents\GitHub\hypersteg_chess\hypersteg_novelty_kit_20261108\maps\mechanism_taxonomy.tsv`. Mechanism overview: [approach_map_mechanisms.md](approach_map_mechanisms.md). Each approach leaf names its paper family.

- mechanisms: 3
- approaches: 2
- families: 2 (foundations-theory, llm-generative-text)

```mermaid
flowchart TD
  subgraph cls_key_establishment_g["key-establishment"]
    cls_key_establishment("key-establishment")
    mech_m_key_establishment{{"Covert key establishment without a pre-shared secret"}}
    mech_m_public_key_block_parity{{"Public-key ciphertext as block parity"}}
    mech_m_sampled_lattice_key_exchange{{"Lattice key exchange in honest samples"}}
    n_anderson_1998_approach_public_key_steganography["public-key steganography: encrypt under the recipient's pub…<br/>anderson_1998<br/>family: foundations-theory"]
    n_pang_2026_approach_codetta_key_exchange["Codetta's keyless steganographic key exchange, MLWE ciphert…<br/>pang_2026<br/>family: llm-generative-text"]
  end
  cls_key_establishment --- mech_m_key_establishment
  mech_m_key_establishment --- mech_m_public_key_block_parity
  mech_m_key_establishment --- mech_m_sampled_lattice_key_exchange
  mech_m_public_key_block_parity --- n_anderson_1998_approach_public_key_steganography
  mech_m_sampled_lattice_key_exchange --- n_pang_2026_approach_codetta_key_exchange
  linkStyle 0,1,2,3,4 stroke:#9e9e9e,stroke-width:1px
```

## Mechanisms

| mechanism | parent | class | name | definition | grounded by | landing | approaches |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `m-key-establishment` | — | key-establishment | Covert key establishment without a pre-shared secret | Ciphertext under the recipient's public key, such as a session key, is carried in the cover, so parties who share no secret can still communicate covertly. | `anderson_1998:approach-public-key-steganography` | yes | 2 |
| `m-public-key-block-parity` | m-key-establishment | key-establishment | Public-key ciphertext as block parity | The message is encrypted under the recipient's public key and embedded as the parities of successive cover blocks. | `anderson_1998:approach-public-key-steganography` | yes | 1 |
| `m-sampled-lattice-key-exchange` | m-key-establishment | key-establishment | Lattice key exchange in honest samples | MLWE ciphertext coefficients are carried as small displacements in blocks that are honest samples from the sender's model, so that independently deployed agents agree a key. | `pang_2026:mlwe-steganographic-key-exchange` | yes | 1 |

## Approaches

| address | name | family | technique | channel | key | access | capacity | mechanism | landable | mechanism_evidence | carrier | acquisition |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `anderson_1998:approach-public-key-steganography` | public-key steganography: encrypt under the recipient's public key and embed as block parities; every recipient tries to decrypt, and against an active warden a one-time key permutes the cover bits | foundations-theory | ft-public-key-steganography; ft-keyed-parity | other (parity of successive cover blocks) | none | — | — | m-public-key-block-parity | yes | own | parity of successive cover blocks | specified |
| `pang_2026:approach-codetta-key-exchange` | Codetta's keyless steganographic key exchange, MLWE ciphertexts carried over honest model samples | llm-generative-text | lgt-public-key-sampling | distributional-sampling | none | sender: logits; receiver: logits of the public draft model | about 80k visible tokens per 128-bit key (640 tokens per key bit) | m-sampled-lattice-key-exchange | yes | own | token sampling in agent messages | specified |
