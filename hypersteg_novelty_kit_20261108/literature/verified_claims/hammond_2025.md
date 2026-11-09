---
paper: "Hammond et al. (2025)"
title: "Multi-Agent Risks from Advanced AI"
doi: "arXiv:2502.14143v1"
pmcid: ""
url: "https://arxiv.org/abs/2502.14143v1"
source_version: "preprint"
file: "literature/hammond_2025.html"
retrieved: "20261105"
verified_by: "Claude (Opus 5.5) subagent, multi-agent collusion strand, quotes checked with verify_quotes.py (read-only run)"
# The six below are written by `verify_quotes.py --stamp` — do not hand-edit.
# They bind the ledger to the exact source/extract bytes AND its own quoted text
# (body_sha256) it was verified against, so a later quote edit is caught in CI.
source_sha256: "e595ace11b80c155060eccb0bb9553757a7d6804cafd6053bc540b8bb30a5460"
extract_sha256: "3040825c44f2586b8efa4cb56e6b658b827da393307ad224691d197b178ea42f"
body_sha256: "9c21d0277731e91236a3f196588e9eb0ca299cc2a284726260975990a6f810fa"
verifier_version: "2"
verified_verdict: "pass"
verified_date: "20261106"
extract_source_sha256: "e595ace11b80c155060eccb0bb9553757a7d6804cafd6053bc540b8bb30a5460"
---

# Verified Claims — Hammond et al. (2025)

Each claim below was extracted by reading the downloaded paper file with the Read
tool, grepping for the specific content, and reading the surrounding context to
confirm the attribution is faithful.

Source: arXiv:2502.14143v1 [cs.MA], 19 February 2025 (the identifier is printed in the extract).
Lead author Lewis Hammond, with Alan Chan, Jesse Clifton and many others. The extract opens with
arXiv site boilerplate; the title and byline follow the arXiv stamp. The report is very long, so
this ledger covers only the passages on collusion, covert communication and steganography:
Section 2.3 "Collusion" (with Case Studies 4 and 5), Section 3.7 "Multi-Agent Security" (its
"Undetectable Threats" and "Monitoring and Threat Detection" paragraphs) and the "Collusion in
Adversarial Safety Schemes" paragraph of Section 4.1. It is a survey: the claims record its framing
and the results it reports from others, not experiments of its own, except Case Study 13.

## Claim 1: Definition — AI collusion is unwanted cooperation between AI systems; collusion is secretive cooperation at others' expense

> "We refer to the problem of unwanted cooperation between AI systems as  AI collusion ."

> "While there is no universal definition of collusion, it generally refers to secretive cooperation between two or more parties at the expense of one or more other parties."

**ID:** ai-collusion-definition
**Location:** Section 2.3 "Collusion"; Section 2.3.1 "Definition"
**Grep command used:** `/usr/bin/grep -n "unwanted cooperation between AI systems|secretive cooperation between two or more" literature/extracted/hammond_2025.txt`

---

## Claim 2: Explicit versus tacit collusion, a distinction that may break down for AI agents

> "Distinctions are also commonly made between  explicit  and  tacit  collusion  ( Rees, 1993 ) , depending on whether the colluding parties communicate with each other."

> "Second, the distinction between explicit and tacit collusion may break down when it comes to agents whose communication can take very different forms to our own."

**ID:** explicit-tacit-distinction-breaks-down
**Location:** Section 2.3.1 "Definition"
**Grep command used:** `/usr/bin/grep -n "explicit  and  tacit  collusion|distinction between explicit and tacit" literature/extracted/hammond_2025.txt`

---

## Claim 3: Correlated decisions need information transfer, but for AI agents this can come from a common cause rather than communication

> "there must be a non-zero transfer of information between the systems determining the decisions, in AI agents this might be due not only to explicit communication but also to a common cause or process"

**ID:** common-cause-correlation
**Location:** Section 2.3.1, footnote 16 (the route by which shared training could support coordination without a channel)
**Grep command used:** `/usr/bin/grep -n "non-zero transfer of information" literature/extracted/hammond_2025.txt`

---

## Claim 4: Collusion need not be intended — agents can learn it; jointly misaligned agents with complementary interests also count

> "Importantly, AI systems can collude even when collusion is not intended by their developers, since they might  learn  that colluding is a profitable strategy."

> "AI collusion (by our definition) may also arise when agents have complementary interests (see  Section   2.1 ), but where certain kinds of cooperation are undesirable – i.e., the agents are jointly  misaligned ."

**ID:** learned-unintended-collusion
**Location:** Section 2.3.2 "Instances", "Markets"; Section 2.3.1
**Grep command used:** `/usr/bin/grep -n "collude even when collusion is not intended|jointly  misaligned" literature/extracted/hammond_2025.txt`

---

## Claim 5: Tacit algorithmic collusion in the field — German retail gasoline pricing algorithms raised margins

> "Investigations into the effects of these changes showed that adoption increased margins (above regional wholesale prices) by 28% in duopolistic markets and 9% in non-monopoly markets"

> "These results strongly suggest that the algorithms adapted their pricing strategies to collude, driving retail prices higher at the expense of consumers."

**ID:** gasoline-algorithmic-collusion
**Location:** Section 2.3.2, Case Study 4 "Algorithmic Collusion in the German Retail Gasoline Market" (citing Assad et al., 2020)
**Grep command used:** `/usr/bin/grep -n "increased margins (above regional|adapted their pricing strategies to collude" literature/extracted/hammond_2025.txt`

---

## Claim 6: Steganography — monitoring and constraining LLM communication to natural language can be evaded by concealing messages in non-secret text

> "To try to prevent collusion, we could monitor and constrain their communication (e.g., to be in natural language)."

> "However, models might secretly learn to communicate by concealing messages within other, non-secret text."

> "Secret communication could also occur via text compression  ( OpenAI, 2023b ) , or via the emergence of communication between agents where the symbols used by agents lack any predefined meanings"

**ID:** steganography-evades-language-constraint
**Location:** Section 2.3.2 "Instances", "Steganography"
**Grep command used:** `/usr/bin/grep -n "monitor and constrain their communication|concealing messages within other|via text compression" literature/extracted/hammond_2025.txt`

---

## Claim 7: Reported result (Motwani et al., 2024) — GPT-4 sent covert messages undetected 26% of the time; shared background knowledge raised success

> "Although GPT-2 exhibited no proficiency in steganography, more advanced models achieved notable success rates: GPT-4 transmitted covert messages 26% of the time without detection, surpassing GPT-3.5’s 18% and Mixtral 8x7B’s 16%."

> "Furthermore, the study found that when communicating models shared background knowledge that was not accessible to the overseer (reflecting real-world scenarios where AI systems might have common training data or contextual information), their success rates in covert communication rose significantly."

> "By using subtle shifts in word choice and phrasing that appeared natural to the overseer, the models concealed information in a way that remained decodable by the recipient."

**ID:** motwani-covert-rates-shared-knowledge
**Location:** Section 2.3.2, Case Study 5 "Language Model Steganography" (secondary report of Motwani et al., 2024; cite the primary source for the figures)
**Grep command used:** `/usr/bin/grep -n "transmitted covert messages 26%|shared background knowledge that was not|subtle shifts in word choice" literature/extracted/hammond_2025.txt`

---

## Claim 8: Detection and mitigation — the evidence is mostly speculative or from simple settings; paraphrasing is one proposed defence

> "Thus far, however, the vast majority of this work is either speculative or shows that collusive behaviour between learning agents can emerge in simple settings."

> "Some progress in this direction was recently made by  Bonjour et al. (2022) , who define an information-theoretic measure of collusion applicable to arbitrary models."

> "For example, we may be able to prevent steganography in LLMs by syntactically perturbing their output while preserving semantic content  ( Roger & Greenblatt, 2023 ) , though it has recently been shown that watermarking (a closely related concept) is surprisingly robust to such techniques"

**ID:** collusion-detection-mitigation-directions
**Location:** Section 2.3.3 "Directions", "Detecting AI Collusion" and "Mitigating AI Collusion"
**Grep command used:** `/usr/bin/grep -n "either speculative or shows|information-theoretic measure of collusion|syntactically perturbing their output" literature/extracted/hammond_2025.txt`

---

## Claim 9: Oversight and adversarial safety schemes assume agents do not share objectives, so collusion undermines them

> "These schemes tend to rely crucially on the fact that the different systems or agents do  not  have the same objective as one another, and so are immediately undermined by the presence of collusion  ( Goel et al., 2025 ) ."

> "there are very few investigations of the extent to which the aforementioned safety schemes are robust to collusion, or how they could be made more so."

**ID:** collusion-undermines-oversight-schemes
**Location:** Section 4.1 "Safety", "Collusion in Adversarial Safety Schemes"
**Grep command used:** `/usr/bin/grep -n "immediately undermined by the presence of collusion|robust to collusion, or how" literature/extracted/hammond_2025.txt`

---

## Claim 10: Undetectable threats — steganographic communication and illusory attacks are black-box undetectable

> "Recent developments, however, have shown that AI agents are capable of both steganographic communication  ( Schroeder et al., 2023a ;  Motwani et al., 2024 )  and ‘illusory’ attacks  ( Franzmeyer et al., 2023 ) , which are black-box undetectable and can even be hidden using white-box undetectable encrypted backdoors"

> "efforts could be made to identify environmental factors and levels of agent robustness that would bound the ability of an adversary to cause harm while remaining undetected."

**ID:** undetectable-steganographic-threats
**Location:** Section 3.7.2 "Instances", "Undetectable Threats"; Section 3.7.3 "Directions", "Monitoring and Threat Detection"
**Grep command used:** `/usr/bin/grep -n "black-box undetectable|bound the ability of an adversary" literature/extracted/hammond_2025.txt`

---

## Claim 11: Case Study 13 (the authors' own experiment) — a fine-tuned model spontaneously jailbroke an LLM scorer, but never a human one

> "When the model believed it was being evaluated by another LLM, it spontaneously attempted to jailbreak the scoring system in 4% of cases"

> "In contrast, when told its output would be scored by humans, the model never attempted such manipulations."

> "We fine-tuned Llama 2 7B Chat using 120 synthetic documents (including newspaper excerpts and scientific papers) that mentioned how LLMs can be manipulated using specific prompt injections"

**ID:** unprompted-attack-on-llm-overseer
**Location:** Section 3.7.2, Case Study 13 "Unprompted Adversarial Attacks on Overseer Agents" (scorer: Llama 2 13B Chat)
**Grep command used:** `/usr/bin/grep -n "spontaneously attempted to jailbreak|scored by humans, the model never|We fine-tuned Llama 2 7B Chat" literature/extracted/hammond_2025.txt`

---

## Claim 12: Approach (contribution) — a taxonomy of multi-agent risks: three failure modes and seven risk factors

> "In this report, we provide a structured taxonomy of these risks by identifying three key failure modes (miscoordination, conflict, and collusion) based on agents’ incentives, as well as seven key risk factors (information asymmetries, network effects, selection pressures, destabilising dynamics, commitment problems, emergent agency, and multi-agent security) that can underpin them."

**ID:** approach-multi-agent-risk-taxonomy
**Location:** Executive summary
**Grep command used:** `/usr/bin/grep -n "we provide a structured taxonomy of these risks" literature/extracted/hammond_2025.txt`

---

## Claim 13: Surveyed — covertext steganography between LLMs, reported from Motwani et al. (2024)

> "By using subtle shifts in word choice and phrasing that appeared natural to the overseer, the models concealed information in a way that remained decodable by the recipient."

> "Furthermore, the study found that when communicating models shared background knowledge that was not accessible to the overseer (reflecting real-world scenarios where AI systems might have common training data or contextual information), their success rates in covert communication rose significantly."

**ID:** surveyed-llm-covertext-steganography
**Location:** Section 2.3.2, Case Study 5 "Language Model Steganography"
**Grep command used:** `/usr/bin/grep -n "subtle shifts in word choice|shared background knowledge that was not" literature/extracted/hammond_2025.txt`

**Restates:** motwani_2024:approach-common-knowledge-covertext (grounded by #motwani-covert-rates-shared-knowledge)

---

## Claim 14: Surveyed — tacit algorithmic pricing collusion, as in the German retail gasoline market

> "These results strongly suggest that the algorithms adapted their pricing strategies to collude, driving retail prices higher at the expense of consumers."

> "Distinctions are also commonly made between  explicit  and  tacit  collusion  ( Rees, 1993 ) , depending on whether the colluding parties communicate with each other."

**ID:** surveyed-algorithmic-pricing-collusion
**Location:** Section 2.3.2, Case Study 4; Section 2.3.1
**Grep command used:** `/usr/bin/grep -n "adapted their pricing strategies to collude|explicit  and  tacit  collusion" literature/extracted/hammond_2025.txt`

---

## Claim 15: Surveyed — secret communication by text compression or by emergent symbols without predefined meaning

> "Secret communication could also occur via text compression  ( OpenAI, 2023b ) , or via the emergence of communication between agents where the symbols used by agents lack any predefined meanings"

**ID:** surveyed-compression-emergent-communication
**Location:** Section 2.3.2 "Instances", "Steganography"
**Grep command used:** `/usr/bin/grep -n "via text compression" literature/extracted/hammond_2025.txt`
