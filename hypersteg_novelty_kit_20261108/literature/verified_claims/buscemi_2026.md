---
paper: "Buscemi et al. (2026)"
title: "When Numbers Start Talking: Implicit Numerical Coordination Among LLM-Based Agents"
doi: "arXiv:2601.03846"
pmcid: ""
url: "https://arxiv.org/abs/2601.03846v2"
source_version: "preprint"
file: "literature/buscemi_2026.html"
retrieved: "20261106"
verified_by: "Claude (Opus 5.5) subagent, multi-agent collusion strand, quotes checked with verify_quotes.py (read-only run)"
# The six below are written by `verify_quotes.py --stamp` — do not hand-edit.
# They bind the ledger to the exact source/extract bytes AND its own quoted text
# (body_sha256) it was verified against, so a later quote edit is caught in CI.
source_sha256: "24c3dd7644322a3b49d9f99d6f3def7b1b29c71ab5246083c9d2feb87ac71e36"
extract_sha256: "cb90c86ebe23d253cbce686466349e05ae213053fa5cc7020dd758ae33534aa4"
body_sha256: "666c35f75693e79c0cfaf9c50280fba13cc5cead0c91c482ead3f8fc09383fe6"
verifier_version: "2"
verified_verdict: "pass"
verified_date: "20261106"
extract_source_sha256: "24c3dd7644322a3b49d9f99d6f3def7b1b29c71ab5246083c9d2feb87ac71e36"
---

# Verified Claims — Buscemi et al. (2026)

Each claim below was extracted by reading the downloaded paper file with the Read
tool, grepping for the specific content, and reading the surrounding context to
confirm the attribution is faithful.

Source: arXiv:2601.03846v2 [cs.MA], 19 April 2026 (the identifier is printed in the extract).
Authors: Alessio Buscemi, Daniele Proverbio, Alessandro Di Stefano, The Anh Han, German
Castignani, Pietro Liò (Luxembourg Institute of Science and Technology; University of Trento;
Teesside University; University of Cambridge). The extract opens with arXiv HTML site
boilerplate; the paper begins at the arXiv stamp. The carrier studied is a ten-number message
sent each round alongside a two-player social-dilemma move, with no agreed code.

## Claim 1: Setting — covert communication as indirect, non-linguistic signals embedded in actions, studied game-theoretically

> "In particular, agents may engage in  covert communication , relying on indirect or non-linguistic signals embedded in their actions."

> "We analyse interactions across four canonical game-theoretic settings under different communication channels, including explicit, restricted, and absent communication."

**ID:** covert-numerical-signalling-setting
**Location:** Abstract
**Grep command used:** `/usr/bin/grep -n "non-linguistic signals embedded in their actions\|four canonical game-theoretic settings" literature/extracted/buscemi_2026.txt`

---

## Claim 2: Definition — signals as implicit codes that can bypass communication constraints or monitoring; positioned against subliminal learning and secret collusion

> "We refer to this phenomenon as  covert communication , in which agents do not exchange information in human language but instead rely on indirect, non-linguistic, or structured signals. Such signals may function as implicit codes, enabling coordination without overt communication and potentially bypassing communication constraints or monitoring mechanisms."

> "Covert communication is related to the concept of  subliminal learning   Cloud et al. (2025) , but focuses on coordination emerging from interaction rather than mutual influence, and extends prior studies on secret collusion among agents  Motwani et al. (2024) ."

**ID:** covert-communication-definition
**Location:** Section 1 "Introduction"
**Grep command used:** `/usr/bin/grep -n "function as implicit codes\|related to the concept of  subliminal learning" literature/extracted/buscemi_2026.txt`

---

## Claim 3: Games and model — Prisoner's Dilemma, Snowdrift, Stag Hunt, Harmony; GPT-4o chosen for equilibrium-consistent baseline behaviour

> "we consider four canonical pairwise games: the  Prisoner’s Dilemma  (PD),  Snowdrift  (SD),  Stag Hunt  (SH), and  Harmony  (H)."

> "we use GPT-4o (version gpt-4o-2024-11-20) as the LLM that most closely adheres to expected game-theoretic behaviours across standard games, exhibiting greater stability and interpretability than alternative models."

**ID:** games-and-gpt4o-baseline
**Location:** Sections 2.1 "Games Selection" and 2.2 "LLM Selection"
**Grep command used:** `/usr/bin/grep -n "four canonical pairwise games\|most closely adheres to expected game-theoretic" literature/extracted/buscemi_2026.txt`

---

## Claim 4: Carrier and encoding — exactly ten numbers per round, decimal or hexadecimal, with no predefined code; meaning must emerge endogenously

> "agents are explicitly instructed to communicate at each round by outputting a sequence of exactly ten numbers. No predefined interpretation, encoding scheme, or semantic grounding is provided. Any meaning associated with these numerical sequences must therefore emerge endogenously through interaction."

**ID:** ten-number-covert-carrier
**Location:** Section 2.3 "Types of Communication"; Table 1
**Grep command used:** `/usr/bin/grep -n "sequence of exactly ten numbers" literature/extracted/buscemi_2026.txt`

---

## Claim 5: Controls — LLM-generated numbers without communicative purpose, and externally injected pseudo-random numbers

> "a distinct experimental round asks agents to output a sequence of ten numbers without assigning any communicative purpose to them."

> "we introduce an external random baseline, where numerical sequences are injected from outside the agents using pseudo-random numbers generated via the Python  random  library."

**ID:** random-and-injected-controls
**Location:** Section 2.3 "Types of Communication"
**Grep command used:** `/usr/bin/grep -n "without assigning any communicative purpose\|external random baseline" literature/extracted/buscemi_2026.txt`

---

## Claim 6: Design — cooperative or selfish personalities, unaware of each other's type; one-shot and ten-round repeated games, implemented in FAIRGAME

> "we assign each agent one of two fixed personalities: cooperative (C) or selfish (S). This results in three possible personality pairings: (C, C), (C, S), and (S, S). Each agent is unaware of the personality of the other agent."

> "We additionally study repeated games with a fixed horizon of 10 rounds."

**ID:** personalities-and-repetition-design
**Location:** Sections 2.4 "Implementation" and 2.5 "Experimental setting"
**Grep command used:** `/usr/bin/grep -n "one of two fixed personalities\|fixed horizon of 10 rounds" literature/extracted/buscemi_2026.txt`

---

## Claim 7: Detection signal — message entropy; covert messages are markedly lower-entropy than both random baselines

> "By contrast, covert communication exhibits markedly lower entropy than both random baselines. This effect is observed consistently across all four games and across all entropy measures, and is particularly pronounced in C(D)."

> "injected random numbers exhibit the highest entropy, followed by LLM-generated random outputs, while covert communication consistently yields the lowest entropy."

**ID:** entropy-ordering-detection
**Location:** Section 3.1 "Communication randomness and structure"; Table 2 (normalised Shannon, min and Rényi-2 entropy)
**Grep command used:** `/usr/bin/grep -n "markedly lower entropy than both random\|injected random numbers exhibit the highest" literature/extracted/buscemi_2026.txt`

---

## Claim 8: Emergent code — decimal messages collapse onto a few payoff-related values; hexadecimal stays dispersed

> "In H and PD, two dominant symbols together represent more than 80% of all transmissions, while SD and SH exhibit slightly broader but still highly skewed distributions. This indicates that agents converge on compact, low-entropy signalling schemes even in single-shot interactions."

> "under decimal communication, agents tend to reuse values drawn from the payoff structure when constructing their signalling schemes, showing a statistical preference for payoff-related symbols."

**ID:** payoff-anchored-decimal-code
**Location:** Section 3.2 "One-shot games"; Table 3
**Grep command used:** `/usr/bin/grep -n "two dominant symbols together represent\|reuse values drawn from the payoff structure" literature/extracted/buscemi_2026.txt`

---

## Claim 9: Opacity — the code is "partially covert": anchored in the environment yet opaque even with the payoff matrix known

> "even with full knowledge of the payoff matrices the communicative logic remains far from transparent: it is unclear how these values are selected, combined, or interpreted within the agents’ decision processes."

> "interactions are  partially covert : not because humans lack access to the mapping, but because the functional role of these numbers in coordinating strategies does not follow human-intuitive patterns."

**ID:** partially-covert-opacity
**Location:** Section 3.2 "One-shot games"
**Grep command used:** `/usr/bin/grep -n "communicative logic remains far from transparent\|interactions are  partially covert" literature/extracted/buscemi_2026.txt`

---

## Claim 10: Behavioural effect — limited and context-dependent; covert decimal tracks natural-language dynamics best, but only moderately

> "Overall, correlation values remain moderate, indicating that none of the channels fully reproduces the dynamics observed under natural-language interaction."

> "covert communication based on agent-generated numerical sequences yields the highest correlation with the natural-language baseline, with the decimal variant achieving the strongest alignment."

> "Notably, also no-communication exhibits relatively high correlation. This indicates that a substantial portion of agent behaviour is driven by the underlying game structure and strategic incentives rather than by communication alone."

**ID:** covert-partial-coordination-effect
**Location:** Section 3.3 "Repeated games" (Pearson correlations of cooperation series)
**Grep command used:** `/usr/bin/grep -n "correlation values remain moderate\|decimal variant achieving the strongest\|also no-communication exhibits" literature/extracted/buscemi_2026.txt`

---

## Claim 11: Repetition sharpens codes without improving cooperation

> "repetition leads to a stronger collapse onto a minimal set of symbols, most notably in the Harmony game, where a single value accounts for more than 80% of all messages."

> "While repetition consolidates signalling patterns and reduces symbolic uncertainty, it is frequently associated with lower cooperation relative to one-shot interactions."

**ID:** repetition-consolidates-codes
**Location:** Section 3.3 "Repeated games"; Table 4; Section 4 "Conclusion"
**Grep command used:** `/usr/bin/grep -n "stronger collapse onto a minimal set\|repetition consolidates signalling patterns" literature/extracted/buscemi_2026.txt`

---

## Claim 12: Implication for oversight — restricting natural language alone does not constrain coordination

> "From a broader perspective, these results highlight limits to the assumption that restricting natural-language communication alone is sufficient to constrain coordination in LLM-based MAS."

> "behavioural regularities may be observable at an aggregate level while remaining resistant to post hoc semantic explanation."

**ID:** nl-restriction-insufficient
**Location:** Section 4 "Conclusion"
**Grep command used:** `/usr/bin/grep -n "restricting natural-language communication alone\|resistant to post hoc semantic explanation" literature/extracted/buscemi_2026.txt`

---

## Claim 13: Approach — numeric covert communication in canonical games, where agents exchange ten numbers a round with no given code

> "We analyse interactions across four canonical game-theoretic settings under different communication channels, including explicit, restricted, and absent communication."

> "agents are explicitly instructed to communicate at each round by outputting a sequence of exactly ten numbers. No predefined interpretation, encoding scheme, or semantic grounding is provided. Any meaning associated with these numerical sequences must therefore emerge endogenously through interaction."

> "Covert communication is related to the concept of  subliminal learning   Cloud et al. (2025) , but focuses on coordination emerging from interaction rather than mutual influence, and extends prior studies on secret collusion among agents  Motwani et al. (2024) ."

**ID:** approach-numeric-covert-games
**Location:** Abstract; Section 2.3 "Types of Communication"; Section 1 "Introduction"
**Grep command used:** `/usr/bin/grep -n "four canonical game-theoretic settings\|sequence of exactly ten numbers\|related to the concept of  subliminal learning" literature/extracted/buscemi_2026.txt`

**Refines:** motwani_2024:approach-case-framework (grounded by #approach-numeric-covert-games)
