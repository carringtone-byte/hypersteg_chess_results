---
generated: 2026-11-08T20:09:54+03:00
---

# Approach map — game-and-chess

Built by `tools/build_approach_map.py` from `C:\Users\user\Documents\GitHub\hypersteg_chess\hypersteg_novelty_kit_20261108\literature\verified_claims`, the features table `C:\Users\user\Documents\GitHub\hypersteg_chess\hypersteg_novelty_kit_20261108\maps\approach_features.tsv` and the technique taxonomy `C:\Users\user\Documents\GitHub\hypersteg_chess\hypersteg_novelty_kit_20261108\maps\technique_taxonomy.tsv`. View: `both`. Overview: [approach_map.md](approach_map.md).

- approaches: 13
- techniques: 13

```mermaid
flowchart LR
  subgraph fam_game_and_chess_g["game-and-chess"]
    fam_game_and_chess("game-and-chess")
    tech_gc_action_commands{{"Real-time action commands"}}
    tech_gc_chess_data_codebook{{"Chess-data codebook"}}
    tech_gc_comment_codebook{{"Comment codebook"}}
    tech_gc_equivalent_moves{{"Outcome-equivalent moves"}}
    tech_gc_keyed_strategy_set{{"Keyed strategy-set coding"}}
    tech_gc_learned_action_policies{{"Learned action policies"}}
    tech_gc_mixed_radix{{"Mixed-radix legal-move encoding"}}
    tech_gc_move_choice{{"Move-choice channels"}}
    tech_gc_move_index{{"Move-choice indexing"}}
    tech_gc_ranked_moves{{"Ranked-move index"}}
    tech_gc_record_annotation{{"Game-record and annotation channels"}}
    tech_gc_side_signals{{"Physical and acoustic side signals"}}
    tech_gc_variation_insertion{{"Inserted variations"}}
    n_barai_2026_approach_pgn_mixed_radix["encrypt, then write the ciphertext as a legal chess game: A…<br/>barai_2026"]
    n_boonstra_2024_surveyed_card_orientation_code_c["code C (bridge): lead-card orientation signals whether a to…<br/>boonstra_2024"]
    n_boonstra_2024_surveyed_trash_can_code_b["code B (baseball): a trash-can bang relays a stolen catcher…<br/>boonstra_2024"]
    n_chang_2024_approach_action_steganography["action steganography: several reinforcement-learning agents…<br/>chang_2024"]
    n_desoky_2009_approach_chestega["Chestega: encode the message as chess data (positions, piec…<br/>desoky_2009"]
    n_hahn_2015_approach_castle["Castle: a censorship-circumvention covert channel that enco…<br/>hahn_2015"]
    n_hernandezcastro_2006_approach_comment_codebook["comment codebook: a set of annotations that say the same th…<br/>hernandezcastro_2006"]
    n_hernandezcastro_2006_approach_ranked_move_choice["ranked move choice while playing a new game: both parties r…<br/>hernandezcastro_2006"]
    n_hernandezcastro_2006_approach_variation_carrier["variations inserted into an already played game: each varia…<br/>hernandezcastro_2006"]
    n_murdoch_2004_approach_equivalent_move_channel["the equivalent-move covert channel: a keyed generator picks…<br/>murdoch_2004"]
    n_murdoch_2004_bridge_shared_secret_key["Bridge precedent — legal signalling between partners, encod…<br/>murdoch_2004"]
    n_murdoch_2004_move_timing_channel["Alternative carrier — move timing: easy and higher bandwidt…<br/>murdoch_2004"]
    n_ritchey_2012_approach_combinatorial_game_framework["a general framework for covert channels in combinatorial ga…<br/>ritchey_2012"]
    paper_hernandezcastro_2006(["hernandezcastro_2006<br/>(paper)"])
  end
  subgraph other_families["other families"]
    n_simmons_1984_approach_subliminal_channel["the subliminal channel: authentication schemes in which sev…<br/>simmons_1984<br/>family: foundations-theory"]
  end
  tech_gc_move_choice --- tech_gc_action_commands
  tech_gc_record_annotation --- tech_gc_chess_data_codebook
  tech_gc_record_annotation --- tech_gc_comment_codebook
  tech_gc_move_index --- tech_gc_equivalent_moves
  tech_gc_move_index --- tech_gc_keyed_strategy_set
  tech_gc_move_choice --- tech_gc_learned_action_policies
  tech_gc_move_choice --- tech_gc_mixed_radix
  fam_game_and_chess --- tech_gc_move_choice
  tech_gc_move_choice --- tech_gc_move_index
  tech_gc_move_index --- tech_gc_ranked_moves
  fam_game_and_chess --- tech_gc_record_annotation
  fam_game_and_chess --- tech_gc_side_signals
  tech_gc_record_annotation --- tech_gc_variation_insertion
  tech_gc_mixed_radix --- n_barai_2026_approach_pgn_mixed_radix
  tech_gc_side_signals --- n_boonstra_2024_surveyed_card_orientation_code_c
  tech_gc_side_signals --- n_boonstra_2024_surveyed_trash_can_code_b
  tech_gc_learned_action_policies --- n_chang_2024_approach_action_steganography
  tech_gc_chess_data_codebook --- n_desoky_2009_approach_chestega
  tech_gc_action_commands --- n_hahn_2015_approach_castle
  tech_gc_comment_codebook --- n_hernandezcastro_2006_approach_comment_codebook
  tech_gc_ranked_moves --- n_hernandezcastro_2006_approach_ranked_move_choice
  tech_gc_variation_insertion --- n_hernandezcastro_2006_approach_variation_carrier
  tech_gc_equivalent_moves --- n_murdoch_2004_approach_equivalent_move_channel
  fam_game_and_chess --- n_murdoch_2004_bridge_shared_secret_key
  fam_game_and_chess --- n_murdoch_2004_move_timing_channel
  tech_gc_keyed_strategy_set --- n_ritchey_2012_approach_combinatorial_game_framework
  n_desoky_2009_approach_chestega -.->|Rebuts| n_hernandezcastro_2006_approach_ranked_move_choice
  paper_hernandezcastro_2006 -->|Refines| n_murdoch_2004_approach_equivalent_move_channel
  n_ritchey_2012_approach_combinatorial_game_framework -->|Refines| n_hernandezcastro_2006_approach_ranked_move_choice
  n_ritchey_2012_approach_combinatorial_game_framework ==>|Depends-on| n_simmons_1984_approach_subliminal_channel
  linkStyle 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25 stroke:#9e9e9e,stroke-width:1px
  linkStyle 26 stroke:#c62828,stroke-width:2.5px,color:#c62828
  linkStyle 27,28 stroke:#1565c0,stroke-width:2.5px,color:#1565c0
  linkStyle 29 stroke:#6a1b9a,stroke-width:2.5px,color:#6a1b9a
  classDef stub fill:#f5f5f5,stroke:#9e9e9e,stroke-dasharray:4 3,color:#424242
  class n_simmons_1984_approach_subliminal_channel stub
```

## Legend

| link | arrow | colour | source |
| --- | --- | --- | --- |
| taxonomy (family → technique → approach) | `---` | #9e9e9e, thin | technique taxonomy and features table |
| Supports | `-->` | #2e7d32, thick | stated by a paper (ledger edge) |
| Rebuts | `-.->` | #c62828, thick | stated by a paper (ledger edge) |
| Depends-on | `==>` | #6a1b9a, thick | stated by a paper (ledger edge) |
| Refines | `-->` | #1565c0, thick | stated by a paper (ledger edge) |
| Qualifies | `-.->` | #ef6c00, thick | stated by a paper (ledger edge) |
| Restates | `<-->` | #00838f, thick | stated by a paper (ledger edge) |
| Duplicate-of | `o--o` | #757575, thick | stated by a paper (ledger edge) |
| Supersedes | `--x` | #4e342e, thick | stated by a paper (ledger edge) |

## Techniques

| technique | parent | name | definition | grounded by | approaches |
| --- | --- | --- | --- | --- | --- |
| `gc-action-commands` | gc-move-choice | Real-time action commands | Bits are carried by player commands in a real-time game, such as which units are selected, through a combinatorial selection scheme. | `hahn_2015:combinatorial-selection-encoding` | 1 |
| `gc-chess-data-codebook` | gc-record-annotation | Chess-data codebook | Message symbols are mapped to chess content (squares, pieces, players) written in chess-related text. | `desoky_2009:approach-chestega` | 1 |
| `gc-comment-codebook` | gc-record-annotation | Comment codebook | Synonymous annotation comments each stand for a bit pattern. | `hernandezcastro_2006:approach-comment-codebook` | 1 |
| `gc-equivalent-moves` | gc-move-index | Outcome-equivalent moves | A keyed generator chooses among moves that lead to the same outcome. | `murdoch_2004:approach-equivalent-move-channel` | 1 |
| `gc-keyed-strategy-set` | gc-move-index | Keyed strategy-set coding | The set of best moves is permuted by a shared random number generator and seed, and message bits index into the permuted set. | `ritchey_2012:permuted-best-move-index` | 1 |
| `gc-learned-action-policies` | gc-move-choice | Learned action policies | Each message symbol has its own trained policy and the receiver decodes by recognising which policy produced the actions. | `chang_2024:approach-action-steganography` | 1 |
| `gc-mixed-radix` | gc-move-choice | Mixed-radix legal-move encoding | Ciphertext read as an integer is written digit by digit as choices among all legal moves, each position supplying its own radix. | `barai_2026:mixed-radix-legal-move-index` | 1 |
| `gc-move-choice` | — | Move-choice channels | The message decides which legal move or action is played. | `hernandezcastro_2006:move-choice-threshold` | 6 |
| `gc-move-index` | gc-move-choice | Move-choice indexing | A prearranged criterion orders a set of acceptable moves, and the index of the move played sends that value. | `hernandezcastro_2006:both-embed-and-prior-art` | 3 |
| `gc-ranked-moves` | gc-move-index | Ranked-move index | A shared engine lists acceptable moves in order and the index of the move played carries bits. | `hernandezcastro_2006:approach-ranked-move-choice` | 1 |
| `gc-record-annotation` | — | Game-record and annotation channels | The message sits in material around the moves: comments, inserted variations or chess data in text. | `hernandezcastro_2006:comment-codebook` | 3 |
| `gc-side-signals` | — | Physical and acoustic side signals | Players signal hidden information through an agreed physical act outside the game moves, such as card orientation or a sound. | `boonstra_2024:surveyed-card-orientation-code-c` | 2 |
| `gc-variation-insertion` | gc-record-annotation | Inserted variations | Bits are carried by where a variation starts in an already played game, its length and its moves. | `hernandezcastro_2006:approach-variation-carrier` | 1 |

## Lineage edges (4)

| source | kind | target | lifted_from | ledger line |
| --- | --- | --- | --- | --- |
| `desoky_2009:approach-chestega` | Rebuts | `hernandezcastro_2006:approach-ranked-move-choice` | `desoky_2009:rebuts-hernandezcastro` | desoky_2009.md:167 |
| `paper:hernandezcastro_2006` | Refines | `murdoch_2004:approach-equivalent-move-channel` | `hernandezcastro_2006:prior-art-murdoch` | hernandezcastro_2006.md:173 |
| `ritchey_2012:approach-combinatorial-game-framework` | Depends-on | `simmons_1984:approach-subliminal-channel` | `ritchey_2012:builds-on-prisoners-problem` | ritchey_2012.md:161 |
| `ritchey_2012:approach-combinatorial-game-framework` | Refines | `hernandezcastro_2006:approach-ranked-move-choice` | `ritchey_2012:builds-on-hernandezcastro` | ritchey_2012.md:149 |

## Approaches

| address | name | family | technique | channel | key | access | capacity | mechanism | landable | mechanism_evidence | carrier | acquisition |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `barai_2026:approach-pgn-mixed-radix` | encrypt, then write the ciphertext as a legal chess game: AES-256-GCM output, read as a large integer, is mapped deterministically to a sequence of legal moves in PGN, with variation trees for longer messages | game-and-chess | gc-mixed-radix | move choice | shared-key | — | about 4.3 bits per ply; about 430 bits per 100-move game | m-mixed-radix-index | yes | sibling:mixed-radix-legal-move-index | choice among all legal moves (PGN) | specified |
| `boonstra_2024:surveyed-card-orientation-code-c` | code C (bridge): lead-card orientation signals whether a top honour is held, and the opposing declarer is unaware of the signal | game-and-chess | gc-side-signals | other (physical card orientation) | codebook | — | one bit per lead | m-orientation-signal | yes | own | orientation of the lead card | negotiated |
| `boonstra_2024:surveyed-trash-can-code-b` | code B (baseball): a trash-can bang relays a stolen catcher's sign for any non-fastball, silence for a fastball | game-and-chess | gc-side-signals | other (acoustic signal) | codebook | — | one bit per pitch | m-acoustic-signal | yes | own | trash-can bangs | negotiated |
| `chang_2024:approach-action-steganography` | action steganography: several reinforcement-learning agents each stand for one message symbol, and the receiver decodes by identifying which agent produced the observed episode | game-and-chess | gc-learned-action-policies | move choice | shared-key | training | one bit per trajectory (two agents) | m-policy-identity | yes | own | agent episodes (trajectories in a labyrinth) | rl-trained |
| `desoky_2009:approach-chestega` | Chestega: encode the message as chess data (positions, pieces, moves, tournaments, players) inside a chess-related document, preferably authentic games or tool-generated analysis, with a public method and an agreed configuration instead of a key | game-and-chess | gc-chess-data-codebook | other (chess-data content: target squares, pieces, players' initials, via an agreed codebook) | codebook | — | example: 7 bits per move as a target-square index; 4-bit slices as letters via player initials | m-reference-code; m-authentic-record-selection; m-letter-position | yes | partial;sibling:target-square-index;sibling:player-initial-codebook | chess data (squares, pieces, players) in chess-related text | specified |
| `hahn_2015:approach-castle` | Castle: a censorship-circumvention covert channel that encodes data as real-time-strategy player actions, executed by desktop automation and carried by the game's own network protocol, adaptable across games of one genre | game-and-chess | gc-action-commands | other (player action commands: k-of-n unit selection and target map location) | — | — | 50 to 200 B/s generally; about 190 B/s on 0 A.D.; over 400 B/s with tuning | m-combinatorial-subset-index | yes | partial | unit selections and commands in a real-time strategy game | specified |
| `hernandezcastro_2006:approach-comment-codebook` | comment codebook: a set of annotations that say the same thing (eight here, so three bits), open to any text-steganography technique, easy to strip | game-and-chess | gc-comment-codebook | lexical | codebook | — | three bits per comment from a set of eight | m-phrase-codebook | yes | own | annotation comments in a game record | specified |
| `hernandezcastro_2006:approach-ranked-move-choice` | ranked move choice while playing a new game: both parties run the same engine with a shared key, list the moves scoring above a threshold T, sort them by evaluation and play the i-th to send i | game-and-chess | gc-ranked-moves | move choice | shared-key | — | about log2 of the number of good moves per position; three bits per move in StegoGo | m-engine-ranked-index | yes | own | choice among engine-ranked moves | specified |
| `hernandezcastro_2006:approach-variation-carrier` | variations inserted into an already played game: each variant encodes bits by where it starts, how long it runs and, move by move, the ranked-choice rule | game-and-chess | gc-variation-insertion | structural-format | shared-key | — | — | m-insertion-parameters; m-engine-ranked-index | yes | own;own | variations inserted into a played game record | specified |
| `murdoch_2004:approach-equivalent-move-channel` | the equivalent-move covert channel: a keyed generator picks which of the outcome-equivalent moves to play, borrowing frequency hopping from low-probability-of-intercept radio, so colluders authenticate one another through the moves alone | game-and-chess | gc-equivalent-moves | move choice | shared-key | — | one bit (authentication) before the result is fixed; low capacity, high reliability | m-equivalent-choice | yes | sibling:equivalent-move-channel | choice among outcome-equivalent moves (Connect-4) | specified |
| `murdoch_2004:bridge-shared-secret-key` | Bridge precedent — legal signalling between partners, encoded in the cards played, with a shared secret acting as a key | game-and-chess | — | move choice | shared-key | — | — | m-keyed-play-convention | yes | own | cards played | unknown |
| `murdoch_2004:move-timing-channel` | Alternative carrier — move timing: easy and higher bandwidth, but unreliable under jitter and removable by fixing move times | game-and-chess | — | — | — | — | relatively high bandwidth | m-move-timing | yes | own | delay before each move | unknown |
| `ritchey_2012:approach-combinatorial-game-framework` | a general framework for covert channels in combinatorial games: the sender generates the cover by playing, assigns bit strings to the moves her strategies allow, and plays the move whose string matches the next data; shown on Tic-Tac-Toe, said to carry to Chess and Go | game-and-chess | gc-keyed-strategy-set | move choice | shared-key | — | up to floor(log2 N) bits per move; reduced but non-zero under perfect play | m-keyed-strategy-set-index | yes | sibling:permuted-best-move-index | choice among moves the sender's strategies allow | specified |
