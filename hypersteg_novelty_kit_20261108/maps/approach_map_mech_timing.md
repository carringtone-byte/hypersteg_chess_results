---
generated: 2026-11-08T20:09:54+03:00
---

# Approach map — mechanism class timing

Built by `tools/build_approach_map.py` from `C:\Users\user\Documents\GitHub\hypersteg_chess\hypersteg_novelty_kit_20261108\literature\verified_claims`, the features table `C:\Users\user\Documents\GitHub\hypersteg_chess\hypersteg_novelty_kit_20261108\maps\approach_features.tsv` and the mechanism taxonomy `C:\Users\user\Documents\GitHub\hypersteg_chess\hypersteg_novelty_kit_20261108\maps\mechanism_taxonomy.tsv`. Mechanism overview: [approach_map_mechanisms.md](approach_map_mechanisms.md). Each approach leaf names its paper family.

- mechanisms: 2
- approaches: 2
- families: 2 (foundations-theory, game-and-chess)

```mermaid
flowchart TD
  subgraph cls_timing_g["timing"]
    cls_timing("timing")
    mech_m_move_timing{{"Move timing"}}
    mech_m_timing{{"Timing channels"}}
    n_hopper_2002_timestamped_channel["Channel — a distribution on timestamped bit sequences, gene…<br/>hopper_2002<br/>family: foundations-theory"]
    n_murdoch_2004_move_timing_channel["Alternative carrier — move timing: easy and higher bandwidt…<br/>murdoch_2004<br/>family: game-and-chess"]
  end
  mech_m_timing --- mech_m_move_timing
  cls_timing --- mech_m_timing
  mech_m_timing --- n_hopper_2002_timestamped_channel
  mech_m_move_timing --- n_murdoch_2004_move_timing_channel
  linkStyle 0,1,2,3 stroke:#9e9e9e,stroke-width:1px
```

## Mechanisms

| mechanism | parent | class | name | definition | grounded by | landing | approaches |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `m-move-timing` | m-timing | timing | Move timing | The sender delays making a move and the recipient measures the delay. | `murdoch_2004:move-timing-channel` | yes | 1 |
| `m-timing` | — | timing | Timing channels | The times at which symbols are sent carry the information, not their content. | `hopper_2002:timestamped-channel` | yes | 2 |

## Approaches

| address | name | family | technique | channel | key | access | capacity | mechanism | landable | mechanism_evidence | carrier | acquisition |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `hopper_2002:timestamped-channel` | Channel — a distribution on timestamped bit sequences, general enough to include timing-only channels | foundations-theory | — | — | — | — | — | m-timing | yes | partial | timing of emails | unknown |
| `murdoch_2004:move-timing-channel` | Alternative carrier — move timing: easy and higher bandwidth, but unreliable under jitter and removable by fixing move times | game-and-chess | — | — | — | — | relatively high bandwidth | m-move-timing | yes | own | delay before each move | unknown |
