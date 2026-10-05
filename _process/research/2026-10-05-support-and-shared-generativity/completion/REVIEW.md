# Internal review of the completion specification

5 October 2026. Separate AI-assisted mathematical and conceptual review within this research team. This is not external peer review, empirical replication or a proof-assistant build.

## Scope and corrections

The mathematical reviewer read the complete new [formal specification](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/FORMAL-SPECIFICATION.md) and [completion plan](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/COMPLETION-PLAN.md). Three information/quantifier corrections were incorporated:

1. Sequential composition now requires one observation-adapted continuation rule with a uniform conditional success guarantee. It cannot choose a different controller for each hidden entry history.
2. The robust approximation proposition requires the same implementing protocol to correspond across the whole preparation-uncertainty set. A uniform error bound alone does not justify hidden-state-dependent protocol selection.
3. Future capability is explicitly based on the physically accessible record and its conditional preparation or continuation process. An analyst's hidden microstate is not free information for the actor.

The reviewer confirmed the two capability-transfer inclusions and the stated finite-step total-variation bound under their hypotheses. The plan retains the difference between specification, integrated proof, evidence and coverage. A separate conceptual review required preserving the original positive objective and not treating its refutation or a scoped theorem as completion of that objective; the plan incorporates this requirement.

A further interface correction requires compatible laws for protocol restriction and continuation, with the causal-composition rules of the declared physical realization. P1 now explicitly uses a stopping time and a success event measurable there. Assigning unrelated probability laws to a protocol and its prefix would not support its composition proof.

## Stochastic realization

The same mathematical reviewer subsequently read the complete [stochastic realization](STOCHASTIC-REALIZATION.md). The event propensities reproduce the existing deterministic drift and reduced work-equivalent ledger. The countable-state absorption argument was checked through the dominating immigration–death process, uniform positive-probability material-degradation trial, and nonoverlapping stopping-time repetition. No proof correction was requested. A clarification that incident power and energy are normalized by system size was added.

The theorem asserts almost-sure finite absorption for its supplied finite-material model; it provides neither an expected-lifetime bound nor a universal physical extinction law. Physical identification, thermodynamic validation, actual capability assays, and reduced transition rates remain open. Review did not add those results.

## Verification boundary

The [verification record](verification.json) checks local links and source hashes. It records the research index as mutable because the completion links were added after its initial inspection. Scientific source checks and earlier experiments were not rerun for document integration. Existing original reports and source genealogy remain intact.
