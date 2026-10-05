# Review of the Lean candidate core

6 October 2026. AI-authored internal adversarial review by a separate reviewing agent. This is a conceptual and mathematical source review, not independent human peer review or empirical validation. Compilation and theorem-dependency verification are recorded separately by the implementation's validator.

Reviewed sources: [GenerativeCore.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/GenerativeCore.lean), [RootRealization.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/RootRealization.lean), [BoundaryModels.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/BoundaryModels.lean), and [Depletion.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/Depletion.lean).

## Accepted mathematical scope

The core declares discrete, action-labelled transition possibilities. It places changed conditions and selection settings within the state of one process. It does not assume an objective, positive direction, finite state space or external chooser. This is a coherent interface for the proposed activity–conditions relation. The transition rules, state boundary and physical interpretation remain supplied.

`trace_append_iff` and `feasible_append_iff` correctly retain the actual intermediate state. The latter permits a suffix only from a state reached by its prefix. It does not infer concatenated feasibility from separate feasibility at unrelated starts. No hidden reset appears in the definitions or proofs.

`local_exact_iff_trace_exact` correctly equates local projected-step exactness with endpoint-sensitive exactness of all finite traces. The local obligation lifts each abstract step from **every specified concrete starting state**, not merely from some representative of its abstract class. This avoids the familiar error of combining incompatible edges from different representatives. `feasible_difference_implies_projection_difference` then gives a meaningful necessity result: a summary preserving feasible future words must retain every distinction witnessed by such a word.

`trace_product_iff` correctly characterizes the declared synchronous product. Its factors share an action word and their local constraints must both hold. This does not establish compatibility of separately authored real mechanisms. Shared resources, incompatible timing and cross-component dependence need explicit representation in a suitable joint law.

The depletion results supply a substantive conditional obstruction: if every permitted transition strictly decreases a natural-number reserve, trace length is bounded by its initial value, and no nonempty return cycle or infinite execution exists. The minimum decrement is essential. Finite real-valued resources with successively smaller expenditures do not by themselves satisfy this premise.

The five-phase realization supplies reachable witnesses, rather than merely two unrelated states. Activity changes later admissibility; a supplied revision is enabled after depletion; the same initial state and event law admit a supported recurrent branch and a terminal branch. Continuing external provision is explicit and its removal disables restoration. The model therefore does not obtain infinite work from a closed finite reserve.

## Findings and required interpretation

1. **The fixed-selector counterexample initially used an inert coordinate; repaired.** In the first reviewed version, `advance` copied the selector without consulting it. That established an unchanged named field, weaker than an unchanged operative selection rule. The reviewer requested that the selector actually determine the update mode, or that the claim be narrowed accordingly. The revised source passes the semantic reinspection recorded below.

2. **Revision is represented, not derived.** In the five-phase realization, `selector` is a phase-derived setting. The added coordinate-uniqueness theorem establishes that support and selector together identify every phase; the exact restoration guard makes the selector operative for admissibility at fixed support. This improves the evidence beyond a coincident change of an arbitrary label. It remains a supplied phase-dependent rule change, not a derivation of a learner, performance improvement, a physically implemented intervention on a controller, or the origin of its revision rule. The source comments preserve the principal qualification.

3. **The formal boundary is narrower than universal causal adequacy.** Finite existential action traces do not establish probabilities, observable-state labels, implementable policies under partial information, ethical standing or general infinite-behavior equivalence. A changing state field does not by itself establish learning. The interface can host richer models, but their meaning and laws require further work.

## Conclusion

With the selector finding resolved, and subject to the separately recorded compiler validation, the package supports a **verified realization of the candidate's stated core commitments**, exact finite-continuation bookkeeping, and informative constraints and counterexamples. Its witnesses establish that those commitments can be realized together under the declared mathematical interface, relative to the proof system's foundational assumptions. They do not establish unique minimality, novel mathematical primitives, empirical universality, or the completed derivation from organization to significance, learning and concern.

No other blocking issue was found in the reviewed proofs' stated mathematical scope. A proof that an authored record satisfies a predicate named `Candidate` would add little; the present package's value lies in its explicit witnesses, projection theorem and depletion obstruction.

## Resolution record

Reinspected the revised sources on 6 October 2026. `FixedSelector.advance` now consults the selector: one value selects alternation, the other holds the current phase. `selector_changes_next_phase` varies that setting at a common current phase and proves different successors. `selector_unchanged_at_every_time` and `recurrent_process_with_fixed_selector` retain a nonconstant recurrent trajectory with that operative selector fixed. The requested non-implication is now accepted: recurrence alone does not require revision of an operative selector. It is still not a theorem defining or classifying every form of learning.

`RootRealization.phase_determined_by_support_and_selector` and `restoration_guard` were also reinspected. Together with the reachable depleted-to-revised transition they establish the finite coordinate and permission claims described above. Their supplied mechanisms, external-support premise and finite action repertoire remain explicit. No unresolved blocking issue remains in this source review's stated scope.

The appended exact-summary examples were subsequently reviewed. `decoratedProcess` adds a Boolean coordinate that toggles at each step without constraining the phase transition. `decoration_local_exact` provides a lift from each decorated starting state, and `decoration_trace_exact` soundly instantiates the general theorem to discard this non-injectively encoded coordinate while preserving every finite event word and projected phase endpoint. This does not preserve observations of the discarded coordinate itself. Conversely, `support_alone_is_incomplete` correctly rules out every proposed process on the specified Boolean support summaries that would preserve all finite feasible words: the reachable depleted and revised phases have equal support but disagree on the one-event restoration word. These two examples establish an actual dispensable distinction and an actual indispensable distinction relative to the declared continuation contract, rather than merely asserting a generic exactness criterion. No new blocking finding arose.
