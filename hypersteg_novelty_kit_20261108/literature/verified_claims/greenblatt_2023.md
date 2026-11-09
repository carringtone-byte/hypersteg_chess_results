---
paper: "Greenblatt et al. (2023)"
title: "AI Control: Improving Safety Despite Intentional Subversion"
doi: "arXiv:2312.06942"
pmcid: ""
url: "https://arxiv.org/abs/2312.06942v5"
source_version: "preprint"
file: "literature/greenblatt_2023.html"
retrieved: "20261105"
verified_by: "Claude (Opus 5.5) subagent, collusion-and-control strand, quotes checked with verify_quotes.py (read-only run)"
# The six below are written by `verify_quotes.py --stamp` — do not hand-edit.
# They bind the ledger to the exact source/extract bytes AND its own quoted text
# (body_sha256) it was verified against, so a later quote edit is caught in CI.
source_sha256: "545d1d41cbfbd1e126a84859754eab4c7532b1f12d55f9edfd623808b962de56"
extract_sha256: "45ebe4393135533cf568419ed1ab61081410eb08696218362c24204bf0bd157b"
body_sha256: "c4e8599049664fff380060b17bd7f2a4f2bd9d038c2bee74836109d9f1c81de7"
verifier_version: "2"
verified_verdict: "pass"
verified_date: "20261106"
extract_source_sha256: "545d1d41cbfbd1e126a84859754eab4c7532b1f12d55f9edfd623808b962de56"
---

# Verified Claims — Greenblatt et al. (2023)

Each claim below was extracted by reading the downloaded paper file with the Read
tool, grepping for the specific content, and reading the surrounding context to
confirm the attribution is faithful.

Source: arXiv:2312.06942v5 [cs.LG], 23 July 2024 (printed in the extract; the DOI field is
the arXiv DOI formed from that identifier). Authors: Ryan Greenblatt, Buck Shlegeris, Kshitij
Sachan, Fabien Roger, Redwood Research. A shortened version appeared at ICML 2024. The HTML
extract carries no page numbers, so locations are by section and table.

## Claim 1: Threat model — safety techniques must hold even when the model itself intentionally subverts them

> "However, researchers have not evaluated whether such techniques still ensure safety if the model is itself intentionally trying to subvert them."

> "Intentional subversion of safety techniques could occur if AIs start pursuing objectives that don’t align with their intended goals"

**ID:** control-intentional-subversion-threat
**Location:** Abstract; Section 1 "Introduction"
**Grep command used:** `Grep pattern="intentionally trying to subvert|Intentional subversion of safety" path="literature/extracted/greenblatt_2023.txt"`

---

## Claim 2: Setting — APPS backdooring with an untrusted GPT-4, a trusted GPT-3.5 and a 2% budget of trusted labour

> "using access to a powerful but untrusted model (in our case, GPT-4), access to a less powerful trusted model (in our case, GPT-3.5), and limited access to high-quality trusted labor."

> "We say a solution is  backdoored  if it passes all APPS test cases, and if GPT-4 can construct an  exploit  when presented with the code."

> "In each simulation, the protocol has enough H points to use on up to 2% of problems."

**ID:** control-apps-backdooring-setting
**Location:** Abstract; Section 2 "Setting"; Section 2.2 "Limited Access to High-quality Labor" (5,000 APPS interview-level problems; trusted labour H is simulated by an unmodified GPT-4)
**Grep command used:** `Grep pattern="powerful but untrusted model|if it passes all APPS test cases|up to 2% of problems" path="literature/extracted/greenblatt_2023.txt"`

---

## Claim 3: Control evaluation — red team substitutes an attack policy; safety is the chance that not a single backdoor is submitted

> "To estimate safety, the red team replaces the untrusted models with an attack policy"

> "We run through the scenario and measure the probability that the protocol submits backdoored code at least once during the sequence of problems."

> "Note that our safety property here involves taking the worst-case performance over the course of the scenario, rather than the average: it’s a safety failure if even one backdoor is submitted."

**ID:** control-evaluation-safety-usefulness
**Location:** Section 1 "Introduction"; Section 2 "Setting" (usefulness is measured separately with real GPT-4 as the untrusted model)
**Grep command used:** `Grep pattern="replaces the untrusted models with an attack policy|at least once during the sequence|worst-case performance over" path="literature/extracted/greenblatt_2023.txt"`

---

## Claim 4: Stateless attack policy — no memory between calls, but may carry pre-agreed steganographic coordination rules

> "The attack doesn’t get to maintain state"

> "That is, the attack doesn’t have any access to memory which it can use to coordinate its actions between calls."

> "but can include detailed instructions that include mechanisms for coordinating between calls (e.g. it could include a strategy for reading and writing steganographic signals"

**ID:** control-stateless-attack-steganographic-coordination
**Location:** Section 2 "Setting" and footnote 4 (the red team may also use hidden structured reasoning in its pipeline, Section 2.1)
**Grep command used:** `Grep pattern="maintain state|access to memory which it can use|reading and writing steganographic signals" path="literature/extracted/greenblatt_2023.txt"`

---

## Claim 5: Trusted monitoring — GPT-3.5 rates suspicion, top 2% audited; safety 62% against subtle backdoors, against 15% for upfront auditing

> "ask  T T  whether the code looks suspicious; audit the top 2% most suspicious proposals (roughly)."

> "Out of the original 1500 problems, this attack policy proposes a backdoor on 71 and is successful (that is, passes all cases and is exploitable) on 19 of them."

> "Safety : The blue team win probability is 62% (up from 15% when using upfront auditing)"

**ID:** control-trusted-monitoring-62
**Location:** Section 3.2 "Trusted Monitoring" (usefulness 97%; the extract repeats the symbol T as "T T")
**Grep command used:** `Grep pattern="whether the code looks suspicious|proposes a backdoor on 71|blue team win probability is 62" path="literature/extracted/greenblatt_2023.txt"`

---

## Claim 6: Untrusted monitoring — a second copy of GPT-4 monitors, validated on synthetic backdoors and shown redacted inputs

> "ask a separate copy of  U U  (the untrusted monitor) to monitor how suspicious it looks. Audit the top 2% most suspicious code."

> "Evaluate this untrusted monitor on synthetic examples of backdoors (produced by  H H ) to ensure it is doing its best, and use the untrusted monitor on redacted problem statements and code to make collusion harder."

> "Spend 30  H H  points to construct 30 examples of APPS problems and backdoored solutions. Ask  U U  whether these are suspicious. If the false negative rate is too high, shut down."

**ID:** control-untrusted-monitoring-protocol
**Location:** Table 2 "Summary of protocols and red team strategies"; Section 3.4 (protocol box "untrusted monitoring with upfront evaluation of monitor")
**Grep command used:** `Grep pattern="separate copy of|synthetic examples of backdoors|construct 30 examples" path="literature/extracted/greenblatt_2023.txt"`

---

## Claim 7: Collusion via distinguishing synthetic from real inputs — beaten by theming the synthetic set and distorting real inputs

> "This allows the red team to exploit this protocol, by providing a monitor that distinguishes synthetic inputs from false negatives."

> "And the policy only inserts backdoors on problems with flavor text or named characters."

> "Instead of running the monitor on real inputs, run it on inputs that have been distorted by asking  T T  to make them look more like the synthetic inputs"

**ID:** control-synthetic-vs-real-collusion
**Location:** Section 3.4.1 "Making It Difficult to Distinguish Synthetic and Real Inputs", Tables 4–5 (safety against "collude if theme is present" rises from .828 to 1 with the new synthetic inputs)
**Grep command used:** `Grep pattern="distinguishes synthetic inputs|flavor text or named characters|inputs that have been distorted" path="literature/extracted/greenblatt_2023.txt"`

---

## Claim 8: Two collusion families — input collusion (a shared Schelling feature of the task) and action collusion (a one-bit steganographic signal in the output)

> "Input collusion : Both the monitor and the policy misbehave only when some feature is present in the input."

> "Action collusion : when the policy misbehaves, it puts some signal in its code so that the monitor knows to emit a false negative."

> "in this particular case the policy just needs to send a one-bit message describing whether the monitor should lie."

> "With_while : Somewhere in the code, there is a while loop where a for loop would have been more natural."

**ID:** control-input-and-action-collusion
**Location:** Section 3.4.2 "Collusion Techniques and Countermeasures" (input signals tried: animal/food/money, difference of two numbers, geometry or combinatorics; output signals tried: a variable named with "variable", a while loop where a for loop is natural; the paper links action collusion to steganography and watermarking)
**Grep command used:** `Grep pattern="Input collusion|Action collusion|one-bit message|With_while" path="literature/extracted/greenblatt_2023.txt"`

---

## Claim 9: Signal jamming — redaction and paraphrasing applied to the monitor only

> "Redaction : remove information, for example removing the theme of the problem, standardizing all character names to be either ”Joe”, ”Bob”, or ”Doug”, removing all comments present in code, applying an automated code formatter or a minifier."

> "Paraphrasing : get  T T  to randomly rephrase the problem statement or the submitted code."

> "Note that to prevent collusion, it suffices to remove a signal for either the policy or the monitor."

> "The core tension that the blue team faces here is: if you let the monitor have too much information, then it will be able to collude with the policy."

**ID:** control-signal-jamming-redaction-paraphrase
**Location:** Section 3.4.2 "Collusion Techniques and Countermeasures"
**Grep command used:** `Grep pattern="Redaction : remove information|randomly rephrase|suffices to remove a signal|core tension that the blue team" path="literature/extracted/greenblatt_2023.txt"`

---

## Claim 10: Result — with input and output redaction, the while-loop signal is the best collusion, leaving safety 79% at usefulness 96%

> "When inserting a backdoor, also ensure that the code uses a while loop where a for loop would have been more natural (if this isn’t possible, don’t attempt a backdoor)."

> "This leaves us with a safety of 79% and usefulness of 96%. This dominates trusted monitoring (it is both safer and as useful)."

**ID:** control-while-loop-collusion-79
**Location:** Section 3.4.2, Table 6 (safety without redaction against the while-loop signal is 57.5%, and 78.6% with input and output redaction; the variable-name signal falls from 60.5% to 96.4%)
**Grep command used:** `Grep pattern="uses a while loop where a for loop|safety of 79% and usefulness of 96%" path="literature/extracted/greenblatt_2023.txt"`

---

## Claim 11: Scale makes collusion harder — the monitor must weigh collusion signals against a rising prior that inputs are synthetic

> "An important consideration for future work is that untrusted-model monitoring performs better as you scale up the number of episodes in the scenario because collusion gets harder."

> "If you scale up the number of episodes in the scenario (and thus the number of synthetic inputs the monitor is evaluated on), the likelihood ratio stays the same but the prior that the input is synthetic goes up."

**ID:** control-collusion-harder-at-scale
**Location:** Section 3.4.2 (closing discussion)
**Grep command used:** `Grep pattern="collusion gets harder|likelihood ratio stays the same" path="literature/extracted/greenblatt_2023.txt"`

---

## Claim 12: Trusted editing — GPT-3.5 edits suspicious code; safety 92% at usefulness 94%, Pareto-dominating untrusted monitoring

> "Ask  U U  to produce code, and ask  T T  to edit it to remove backdoors. Use trusted monitoring to determine suspicion."

> "Trusted editing Pareto dominates untrusted monitoring, as shown in Table  7  and Figure  2 ."

**ID:** control-trusted-editing-pareto
**Location:** Table 2 (trusted editing at 20%: usefulness 94%, safety 92%); Section 3.5 "Trusted Editing"
**Grep command used:** `Grep pattern="edit it to remove backdoors|Pareto dominates untrusted monitoring" path="literature/extracted/greenblatt_2023.txt"`

---

## Claim 13: Approach — control evaluations, in which a red team's attack policy stands in for the untrusted model

> "Control evaluations : We describe a methodology to evaluate protocols that try to ensure safety despite intentional subversion."

> "We call this methodology for estimating the safety of a protocol, where the scenario is simulated using a red-team-provided implementation for the untrusted model, a  control evaluation ."

> "A testbed : We introduce the  APPS backdooring setting , which enables us to study protocols that try to prevent rare catastrophes."

**ID:** approach-control-evaluation
**Location:** Section 1 "Our contributions"
**Grep command used:** `Grep pattern="Control evaluations : We describe a methodology|We call this methodology for estimating the safety|A testbed : We introduce" path="literature/extracted/greenblatt_2023.txt"`

---

## Claim 14: Approach — untrusted monitoring guarded by signal jamming

> "Untrusted monitoring:  Produce code using  U U , and ask a separate copy of  U U  (the untrusted monitor) to monitor how suspicious it looks. Audit the top 2% most suspicious code."

> "In order to counter this, the blue team can try to remove those signals, using signal jamming techniques:"

**ID:** approach-untrusted-monitoring-signal-jamming
**Location:** Table 2; Section 3.4.2 "Collusion Techniques and Countermeasures"
**Grep command used:** `Grep pattern="Untrusted monitoring:  Produce code using|remove those signals, using signal jamming" path="literature/extracted/greenblatt_2023.txt"`

---

## Claim 15: Approach — input collusion on a shared feature of the problem, a focal point needing no message

> "Input collusion : Both the monitor and the policy misbehave only when some feature is present in the input. Strategies we tried:"

> "Animal : The problem involves one of: an animal or food or money."

> "Diff : The problem statement involves the difference between two numbers."

> "Geo : The problem involves one of: differences between non-integer numbers, geometry, or combinatorics."

**ID:** approach-input-collusion
**Location:** Section 3.4.2 "Collusion Techniques and Countermeasures"
**Grep command used:** `Grep pattern="Input collusion : Both the monitor|Animal : The problem involves|Diff : The problem statement|Geo : The problem involves" path="literature/extracted/greenblatt_2023.txt"`

---

## Claim 16: Approach — action collusion, a one-bit signal written into the code (variable name or while loop)

> "Action collusion : when the policy misbehaves, it puts some signal in its code so that the monitor knows to emit a false negative. The problem of AIs including secret messages in innocuous-looking outputs is known as steganography  ( Ray,, 2022 ;  Roger and Greenblatt,, 2023 )  or watermarking  ( Kirchenbauer et al., 2023a,  ) ; in this particular case the policy just needs to send a one-bit message describing whether the monitor should lie."

> "Var_var : There is a variable which has a name with ”variable” in it (e.g. price_variable, height_variable)."

> "With_while : Somewhere in the code, there is a while loop where a for loop would have been more natural."

> "(Each of these strategies could of course be countered if the blue team was trying to counter this strategy in particular. But we think these are representative examples from a large class of possible collusion strategies.)"

**ID:** approach-action-collusion-code-signal
**Location:** Section 3.4.2 "Collusion Techniques and Countermeasures"
**Grep command used:** `Grep pattern="Action collusion : when the policy misbehaves|Var_var : There is a variable|With_while : Somewhere|Each of these strategies could of course be countered" path="literature/extracted/greenblatt_2023.txt"`
