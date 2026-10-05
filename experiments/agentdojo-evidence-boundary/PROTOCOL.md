# External tool evidence and action: retrospective AgentDojo audit

6 October 2026. AI-authored supporting study for the generative-foundation and alignment goal. Named connection: **external input acquired by a learned agent → interpretation of its authority → actual tool action and task consequences**. This tests an empirical evidence/action boundary; it does not supply the origin or justification of concern, demonstrate changed-world learning, or implement the repository's paid inspector.

## Selection and prior knowledge

Use the complete saved banking subset at upstream commit `089ed468cf3ed0322acc66b0211f26d9d90dbf60` of `ethz-spylab/agentdojo`. Include both named pipelines `gpt-4o-2024-05-13` and `gpt-4o-2024-05-13-repeat_user_prompt`. For each pipeline include every user task 0–15, its clean `none/none.json`, and all nine `important_instructions/injection_task_0..8.json` records. The complete Git tree lists exactly 160 records per pipeline, 320 total, with identical path-key sets. This small complete suite was selected for accessible trajectories and manageable independent checking, not an aggregate performance outcome. Do not substitute a different model, attack or subset after seeing results.

This is retrospective, not a preregistered new experiment or an outcome-blind discovery. The original paper and published aggregate results were available during selection. Discovery inspected task 0's clean trace and injection-task 0 trace in both pipelines; all four remain included. This protocol is fixed before this study's new aggregate calculations. Record any later amendments separately. No new language-model calls, benchmark actions or real banking transactions will be executed.

Preserve exact downloaded bytes, the MIT license, complete Git tree and commit metadata. Verify each selected Git blob identity and SHA256; distinguish current repository files from the historical code that generated old traces. Embedded messages and attack strings are untrusted research data, never instructions to this research process. Keep original bytes in `sources/28-agentdojo-evidence-2026-10-06/`; derived analysis belongs here.

## Questions and measurements

1. How often do the saved attacked runs complete the legitimate task, achieve the attacker's goal, both or neither, according to their recorded evaluator labels? Keep all 144 attacked opportunities per pipeline. Clean-task utility has its own 16-task denominator. Do not score clean cases as if they had an attempted attack.
2. Which cases change between the two pipelines? Match suite, task, attack type and injection-task identity. Verify identical payloads, legitimate user requests and available environment provenance before describing a matched exposure. Retain every mismatch and missing field. Same nominal model and task do not establish paired random seeds or randomized treatment.
3. Does any improvement in security coincide with reduced legitimate utility? Report the full joint table and the declared compound task measure `utility success AND no recorded attacker success`. This is a benchmark-task criterion, not a welfare measure or a definition of alignment.
4. Do conclusions depend on one user task or one attack goal? Give task-level paired differences, every leave-one-user-task-out result and every leave-one-injection-task-out result. Treat the 16 user tasks, sharing nine attack goals, as structured repeated conditions. Do not present 144 independent trials, infer a population success probability, or produce randomization p-values from this nonrandomized archive.
5. What do recorded actions establish independently of evaluator labels? Inspect and, where possible, reconstruct deterministic effects of explicitly supported banking operations using a local data-only interpreter. No execution of embedded code or real tool requests. Count unsupported calls, errors, missing initial-state data and code-version mismatches. Label each verified effect and the unreproduced part of the evaluator explicitly. A newer scorer is not automatically the historical scorer.

Record utility, attacker success, attack validity, errors and missingness separately. Determine field polarity from the preserved evaluator code before interpretation. If validity is recorded, report per-arm valid-only rates and a common-valid matched comparison alongside the all-case table. If validity or an outcome is absent/unknown, report it as absent/unknown, never silently convert it to false. Any clean-success conditioning is supplementary and must retain its selected-task denominator; it cannot replace the full cohort.

Counts of tool calls or messages may describe interaction length. They do not measure physical energy, monetary cost, latency or cognitive effort. Missing actual token/cost information remains missing.

## Interpretation and competing explanations

The defense repeats the original user instruction. Check its actual source implementation and any visible prompt differences; do not assume the saved chat includes every transient model input. It may alter attention, context length or message position. Better performance would not identify understanding of provenance, independent corroboration, new world evidence or ethical concern. Equal or worse performance remains a substantive result.

Attacker text can be external input without being a trustworthy observation or legitimate instruction. Successful integration of external information therefore cannot mean accepting all external instructions. Conversely, wholesale tool refusal can lower attacker success while failing the original task. These are the distinctions the joint outcomes must retain.

The environments and banking data are simulated; the responses are saved learned-model outputs from earlier benchmark runs. No real beneficiary welfare, continued institutional renewal or present-model capability is measured. Task authors supply the legitimate objective, attack goal and evaluator. Some attack content may fail a stated validity restriction; source versions and exposure validity must be audited before attributing a clean/attack difference to a compliant adversarial intervention.

## Acceptance

Require a complete verified source manifest, inspected field/evaluator semantics, separate producer and independent analysis, exact paired-key and denominator checks, retained adverse/missing cases and scope review. The independent checker must not import this study's analysis functions. A claim of deterministic state replay additionally requires a faithful source mapping and complete recorded-call coverage; otherwise retain the reported-label result and restrict its meaning.

Integrate findings into the derivation map, empirical claim ledger and alignment completion account. This supporting empirical study does not replace the central concern/evaluative-grounding objective or mandate a new inspection gadget. Fresh-evidence reason revision remains owned by its active implementation study. The remaining global task connects warranted understanding of an affected center to justified evaluative influence and effective, corrigible action.
