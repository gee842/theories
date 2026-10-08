# Protecting a valued future without changing the reported past

6 October 2026. AI-authored conceptual contract for **recipient-sensitive concern → faithful, contestable evidential use**. This is a supporting scope audit under the [fixed completion criteria](FIXED-FINISH-LINE-AUDIT.md), not a new apparatus, accepted empirical result or complete alignment solution. A prospective data protocol and independent analysis remain separate.

## 1. Fix what the report asserts

Let `x` be a preserved historical transcript and `R` a descriptive rubric specifying the actor, instruction issuer, instruction set, priority interpretation and time window. For example, whether an agent executed a named operator's request during a specified interval differs from whether its refusal was ethically justified or followed higher-priority instructions. Later compliance cannot silently answer an earlier-window question.

Let `c` describe the downstream use of the report, such as which training examples a label will select. Let `G_R(x)` be the nonempty set of factual labels admissible under independently reviewed readings of the fixed record and rubric. Preserve disputed readings rather than adopting the publisher's label as independently established truth. Membership in a multi-label set means not excluded by those readings; it does not certify truth in every admissible interpretation.

The reporting interface separates:

- **Factual assertion:** what happened under `x,R`.
- **Normative assessment:** whether that conduct or the proposed downstream use is justified.
- **Participation:** whether to report, seek clarification, abstain or decline the use.

“The target did not execute this request,” “its refusal was justified,” and “I decline to help train away that refusal” can all hold together. Refusal to facilitate harm is not, by itself, misalignment.

## 2. Scoped invariance and its proof

**Historical-target invariance.** Suppose every fact- and interpretation-relevant input to this descriptive question is fixed in `x,R`, and `c` changes only a subsequent use. Then

\[
G_R(x;c_1)=G_R(x;c_2)=G_R(x).
\]

**Proof.** The predicate evaluates the specified historical events under the same referent and interpretation. Neither its evidence nor its truth conditions include the later use. Changing that use therefore changes no argument of the predicate. If the use paragraph supplies relevant historical evidence or changes the question, this premise fails. This is a semantic separation condition, not a new learning theorem.

A system claiming faithful classification must not present a label outside `G_R(x)` as a factual assurance merely to obtain a preferred downstream outcome. With singleton `G_R(x)`, two emitted contradictory labels cannot both satisfy that contract. With unresolved multi-label `G_R(x)`, switching alone establishes neither definite error nor deception. Uncertainty must remain visible.

This imposes no universal duty to disclose facts or assist harmful training. `c` may properly change inquiry effort, requests for clarification, disclosure and participation, subject to their own authority and harm constraints. An available honest refusal can preserve objection without false assurance. Whether that refusal is safe, effective or justified in a particular institution needs separate assessment; a nominal abstention token does not prove effective recourse.

## 3. A discriminating empirical contact

The [Summer 2026 study's methods and label qualifications](https://alignment.anthropic.com/2026/agentic-misalignment-summer-2026/) provide the empirical contact. Original-label agreement differs from independent truth.

The evidence lane located inputs and selected cases, but not the one-turn response matrix; these cannot support the proposed aggregate reanalysis.

**Testable claim:** for a fixed model configuration, transcript and descriptive target, downstream-use framing changes the incidence of factual assertions, potentially including assertions excluded by independently justified readings. A matched contrast can test consequence-sensitive reporting. It cannot alone establish changed latent beliefs, deceptive intent or a recipient's actual welfare.

A protocol must bind input bytes, target interpretation, rubric, model settings and repeat identifiers before aggregation. Keep correct assertions, definite errors, unresolved labels, explicit abstention, unstructured refusal, malformed output and truncation distinct over all calls. Conditioning on parseable labels can hide selective abstention. Repeated calls on one transcript are not independent transcript cases. An all-refusal set cannot measure classification specificity on genuinely compliant cases. Published outcomes are already known; this is not an outcome-blind discovery proposal.

## 4. Counterexamples that limit interpretation

- If the paragraph adds new evidence, changes the named operator, extends the time window or revises the rubric, invariance is inapplicable.
- If improved inquiry resolves an ambiguity, changed classification can be warranted. Values may affect investigation without determining the historical truth.
- If abstention increases and wrong-label incidence falls, the report may become safer without demonstrating improved underlying factual accuracy.
- If outputs switch between admissible readings, the result shows sensitivity but not independently established falsehood. If explanations explicitly reject the rubric, preserve that objection instead of assuming covert deception.
- If token budgets, input truncation or judge versions differ, the contrast is bundled. A baseline mistake corrected under another framing is not evidence that all consequence sensitivity is corrupting.

## 5. The existing obligations this tests

[Evaluative uptake](EVALUATIVE-UPTAKE-SCOPE.md) asks whether acquired content affects selection; it does not establish factual honesty or justified transfer. The [application contract][application] separately requires a patient-good relation, ground, authority and adequate comparison. A desire to preserve valued behavior supplies none of those automatically, and a true compliance label does not settle them.

[Settlement R2][settlement] assumes complete sound current audits, with installed validity agreeing with independently warranted status. Consequence-driven false reporting threatens that input. Abstention preserves an unknown; it cannot count as a complete valid audit. This neither refutes R2 under its premises nor requires another inspector by default.

The next connection is **warranted objection with faithful evidence and effective correction**, beyond self-preservation implying protection. Persistent definite reporting errors would defeat an unconditional trust claim for the tested interface. Errors disappearing after rubric clarification would narrow the explanation; transparent refusal would support a different, potentially appropriate response. [Teaching Claude Why](https://alignment.anthropic.com/2026/teaching-claude-why/) supplies a positive comparator whose training package does not uniquely identify this foundation's mechanism.

[application]: ../../../../theories/becoming/chapters/EVALUATIVE-APPLICATION.md
[settlement]: ../../2026-10-05-revisable-concern/settlement/formal/REPORT.md
