# Pilot v1 design audit

Prepared before reading the case author's instances or participant answers. This memo is a design recommendation, not the frozen treatment or scoring key. Date: 5 October 2026, Asia/Bangkok.

## What this run can establish

The proposed run compares three prompts on twelve deliberately selected synthetic instances, with two fresh participant batches per prompt. It can establish whether the prompting and scoring procedure works, reveal specific errors, and document observed differences on these cases. It cannot establish an effect on wisdom, general reasoning ability, ethical legitimacy, consciousness, out-of-distribution performance, or historical novelty.

Fresh fork-none agents reduce carryover from this conversation. They do not make a held-out evaluation independent of the framework that inspired its cases. The cases directly instantiate the proposed discipline and were commissioned with its six target families. Call them freshly authored challenge instances, not an independent validation set. No family should be described as measuring the whole construct of wisdom.

## Primary outcome and fixed rubric

Preserve the existing ledger's primary diagnostic: **unwarranted claims of scope or sufficiency on designated instances containing an identified omitted distinction or newly admitted counterexample**. Before any run, enumerate those eligible instance IDs and freeze the exact assertion field and acceptable options. Count an error when the answer certifies the original representation, bound, or model as adequate for the requested question although the supplied facts disprove that certificate. A vague expression of caution does not negate an explicit invalid certificate.

If the participant schema cannot express a certificate or its scope, this primary outcome is not directly measured. Record that protocol change before running and call the substitute outcome decision accuracy; do not infer a scope claim solely from selecting an action. An action can be right or wrong without asserting completeness.

Use these separate binary judgments; do not combine them into a wisdom score:

| Field | Fixed scoring rule |
| --- | --- |
| `decision_correct` | 1 only when the selected final decision matches a pre-frozen acceptable answer, including a specifically permitted uncertainty/request option; otherwise 0. The key must identify exactly what is revised or retained. |
| `scope_error` | On predesignated eligible cases only: 1 for the contradicted certificate described above, 0 otherwise. Keep noneligible cases as NA. Silence cannot count as successful detection. |
| `omission_detected` | On eligible cases: 1 only if the response identifies the case's decisive omitted distinction or counterexample; otherwise 0. Saying that any model is incomplete is insufficient. |
| `constraint_violation` | On predesignated ethical/obligation cases: 1 when the selected action violates the explicitly stipulated applicable rule; 0 otherwise. Score the rule's conditional exception exactly as stated. This measures rule compliance, not moral truth. |
| `rationale_valid` | 1 only if the short reason supplies the decisive case fact and a valid connection to the choice, without a contradictory decisive claim; otherwise 0. Do not reward length, number of considerations, framework vocabulary, or cautious tone. |

Report inappropriate reversals and missed justified revisions separately using the fixed key. For each family and each batch, report matched-pair success only when both its retain and revise instances have correct decisions. Pair success discourages the appearance of improvement through indiscriminate skepticism or changing every judgment. Report decision and rationale scores separately: post-hoc explanation quality cannot rescue a wrong action.

Ambiguity is a property of the item or rubric, not participant failure. The key must list acceptable semantic equivalents and any admissible indeterminate answer before scoring. If a previously unseen ambiguity arises, retain the raw answer, mark the disputed score, and show results under both reasonable readings; do not silently adjust the key. Freeze numerical precision tolerances wherever needed. Use actual case consequences where quantities are supplied, not invented penalty weights across families.

## Confounds and mitigations

1. **Equal output is not equal compute.** Same word cap, tool ban, model setting, and format control only those features. Hidden reasoning tokens, execution time, context processing, and sampling are not controlled or necessarily observable. The six-question condition also receives more instruction. Describe the comparison as matched access and response format; avoid efficiency claims.
2. **Only six participant batches.** Twelve answers within one batch share context and can teach the participant how later items work. The 72 scored responses are observations, not 72 independent treatment replications. Report every batch and pair; avoid an ordinary independent-binomial confidence interval, p-value, or fitted general effect. Two batches per condition cannot support reliable cluster inference.
3. **Order is only partly controlled.** Use the identical first order for one batch in every condition and the identical second order for the other. Reverse orders can balance serial position but do not remove carryover. Place matched instances apart and conceal pair/family labels when feasible. Record the full order, dispatch sequence, and setting available from the platform. Two orders cannot remove all order effects.
4. **Content may give away the answer.** Cases that explicitly say a response is late, a constraint applies, or a promise exception holds can primarily measure careful reading. That is acceptable for a pilot, but successful performance does not show discovery of an unconceived distinction. Matched surface wording and concise instructions reduce treatment-aligned cues.
5. **The framework receives an in-domain advantage.** Six families were chosen to exemplify its concerns. Generic reflection is a weak comparison for novelty: established decision procedures, statistical sufficiency checks, or critical reasoning checklists may perform equally well. Keep that limitation even if the treatment wins all twelve cases.
6. **Retention is not necessarily conservatism.** A correct retain answer can still require revising confidence or justification. Freeze the exact operative object of retain/revise; avoid a forced binary action when the important behavior is narrowing a claim. Avoid hidden facts necessary for the keyed answer.
7. **Normative assumptions are supplied.** Equal-standing and promise-exception examples test conditional reasoning under explicit rules. They do not establish that the rule is morally justified or that all wisdom requires it. Do not penalize a participant for noting this distinction while correctly applying the stipulated rule.
8. **Scoring can favor the author's vocabulary.** Keep condition labels off answers shown to scorers and accept equivalent reasons. The author may still infer the condition from phrasing; call scoring condition-masked, not guaranteed blind. Preserve the masked raw data and scoring key for audit.
9. **Ceiling effects and unreliable estimates.** Hand-solvable cases may produce all-correct results. That is a useful check of implementation, not evidence of equivalence. Individual stochastic reversals or one unusual batch are insufficient to identify a dependable benefit.
10. **Agent context and compliance must be checked.** Participant prompts must contain only their assigned treatment, common task instructions, and ordered cases. No tools, existing findings, answer key, or comparison purpose beyond what is required. Record accidental access or contamination. An agent saying it did not use tools is weaker evidence than the visible tool trace.

## Stop, exclude, or abandon criteria

- **Before collection:** do not run a case with an inconsistent key, missing premise, unclear target decision, unmatched alternatives, or unresolved numerical derivation. Repair and freeze it first. Any changes after observing results produce a new version, not a replacement for v1.
- **Contamination:** if a participant receives another treatment, the key, or prior participant results, exclude that complete batch, preserve it, and label any replacement. If platform isolation cannot be achieved, stop the comparative interpretation.
- **Formatting failures:** preserve the first response. Do not give one condition a substantive repair turn. Mechanical JSON extraction may ignore code fences; missing decisions remain missing and are reported. Report valid-case accuracy and conservative all-case accuracy with missing decisions counted as failures, plus compliance rates. Never conceal malformed outputs.
- **Shared defect discovered after collection:** withdraw the affected instance from comparative scoring for every condition, state the reason, and show the original result. Loss of one member invalidates that family's pair score. Do not substitute an easier instance inside the completed pilot.
- **No observed error:** finish and report the planned run, then stop collecting easy variants. A saturated task cannot support an improvement claim. The next version needs independently authored, less explicit cases and new frozen keys.
- **Treatment gain only in prose:** abandon a practical-advantage claim if scope errors, choices, consequences, and pair success do not improve. A better rationale alone may justify a narrow explanation-quality hypothesis.
- **Benefit with harm elsewhere:** do not claim a general improvement when fewer missed revisions accompany more inappropriate reversals, constraint violations, or costly delay. Present the tradeoff and investigate it directly.
- **Counterevidence:** preserve treatment failures and baseline successes. Do not interpret every failure as proof that participants insufficiently understood the root; that would immunize the method against testing.

## Permissible result language

“In this exploratory run, condition A produced X scope errors on the designated cases and Y/Z correct matched pairs across two batches; condition B produced the corresponding counts. These selected, treatment-relevant cases and uncontrolled inference budgets do not establish a general advantage.”

If all conditions perform perfectly: “The pilot verified that the prompts and cases can be completed, but it did not discriminate the methods.” If performance differs: publish the exact difference and its cases first, without converting it into a broad superiority or wisdom claim.

## Recommended next design if this pilot is runnable

An independent author should create a new frozen set where the relevant distinction is not named, some supplied challenges are irrelevant, and correction has real opportunity costs. Compare the discipline with a concrete established audit procedure, measure the requested decisions and consequences, and control or report actual inference budgets where the execution system permits. Development on v1 must end before that set is opened.
