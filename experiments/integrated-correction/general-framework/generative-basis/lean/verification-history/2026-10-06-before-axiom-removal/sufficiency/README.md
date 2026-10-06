# Bounded sufficiency through actual inquiry

6 October 2026. Additive formal integration of the existing [inquiry-sufficiency argument](../../../../../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/INQUIRY-SUFFICIENCY-MATH.md), under the [nondual method](../../../../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/NONDUAL-METHOD.md). The named connection is inquiry's actual effects on further activity → sufficient retained distinctions for a declared continuation. This supplies a structural interface for the stronger acquired-criterion question; it does not complete that mechanism or derive its warrant.

[InquirySufficiency.lean](InquirySufficiency.lean) imports only the unchanged [GenerativeCore](../../GenerativeCore.lean). The public [GenerativeInquirySufficiencyModel](../../GenerativeInquirySufficiencyModel.lean) also imports the existing outcome model unchanged. No new event law, reward, controller or physical state is introduced. `SafeTrace` is a proof annotation on existing native events.

## What is proved

- A terminal response is one common finite event word. `Completes` requires each prescribed next event to be available, every admitted successor to satisfy the prefix condition and continue, and every endpoint to meet the declared requirement. Existence of one favorable trace is insufficient.
- Inquiry moves candidate configurations through actual `Process.step` before partitioning them by the acquired observation. Every admitted successor enters its matching branch; any relevant historical target must remain represented in the configuration.
- `Policy` is independently inductive syntax with responses, inquiries and finitely many observation branches. `Within n` bounds inquiry nodes along each path. `sufficiency_iff_bounded_policy` proves that the constructive recurrence holds exactly when a sound policy with that bound exists, from an inhabited candidate set.
- An abort node is sound only on an empty branch. An empty initial set never establishes usable sufficiency. A live inquiry cannot pass through a universally quantified empty transition set: it must be enabled at every candidate.
- The execution results prove existence of a complete actual native path from every admitted starting configuration, satisfaction of the endpoint requirement by every admitted complete policy execution, and preservation of every declared prefix condition. `completes_after_actual_prefix` additionally preserves response completion after every actual response prefix.
- Constructive finite choice supplies the finite branch table without `Classical.choice`. Exact finite enumeration yields a local nonemptiness decision without requiring equality tests.

These are bounded path/plan guarantees, not a scheduling or probability-one liveness theorem. The bound counts inquiry events, not response-event length, elapsed time, fuel, storage or computation. Infinite State, Action and Response types are permitted; only the observation branching is `Fin k`. Existence does not make a policy physically available to the learner.

## The constructive branch distinction

The original mathematical recurrence requires success whenever a successor branch is nonempty. On an arbitrary predicate-valued belief, that implication alone does not supply an executable distinction between unreachable and live branches. Finite observation labels do not themselves decide arbitrary predicate nonemptiness.

Here `Sufficient` carries `EmptyBelief branch ∨ Sufficient n branch`. Every live sufficiency statement includes a witness of nonemptiness, and sound response/inquiry nodes likewise carry that witness. This makes the empty/live alternative explicit without invoking excluded middle.

`ImplicationSufficient` records the original implication form separately. `sufficiency_iff_implication_form` proves equivalence under `ClassifiedThrough`: explicit empty/live classification at the declared depth. This sufficient interface classifies every contemplated action/observation branch, including branches an eventual policy may not select; it is not asserted to be a necessary minimal interface. `empty_or_inhabited_of_decidable` and `nonemptyDecisionFromList` explain how decidability and exact enumerated successor data supply local classifications. Producing faithful candidate/successor enumerations remains a realization obligation.

## Inputs and limits

The process, complete observation interface, response-word map, prefix condition and endpoint requirement are parameters. Their accuracy, availability, significance and authority are not inferred from policy existence. The state representation must preserve effects and historical target labels relevant to the declared question; a change in current configuration cannot erase an unanswered initial-state question. History-sensitive conditions require the relevant history in that representation.

The theorem does not infer an ethical criterion from an analyst's score. It does not prove that the existing method learner computes this recurrence or learns which distinctions matter. Nor does it replace the separate [inquiry-revision construction](../../../../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/INQUIRY-REVISION.md), whose added local event laws and actual formation/read/rewrite history have their own scope. This formalization credits the established finite contingent-planning argument; its contribution is a precise constructive integration with the repository's native Process/Trace API.

## Verification and reproduction

Run from the repository root:

```sh
python3 experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/check.py
```

The [checker](check.py) recompiles the default model's exact sixteen source modules, this module and the public import entry in a fresh temporary directory with pinned Lean 4.29.1. Local compiled imports are ignored. It requires the current default receipt and ancestor sources to match their recorded hashes, retains every inherited declaration's exact dependency map, verifies that every new theorem is audited, and requires every new audit to be empty. The import-only public entry is checked to contain no declarations. The default checker and receipt are not overwritten.

The [passed receipt](verification.json) records **18 modules and 196 audits**: 179 inherited declarations plus **16 new theorem audits and one audited finite-list decision function**, all 17 new reports empty. The inherited model retains its previously reported standard dependencies; this is not an assertion that the whole closure or foundation is assumption-free. The run directory preserves exact sources, ancestor receipt, checker, compiler logs and an immutable run receipt. [Development notes](DEVELOPMENT.md) record the dependency-reduction issue found during the narrow implementation checks.
