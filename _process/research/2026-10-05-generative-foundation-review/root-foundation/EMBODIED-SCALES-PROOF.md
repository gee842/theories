# Embodied choices across scales — checked correspondence

8 October 2026. [Current account](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/RELATIONS-ACROSS-SCALES.md) · [integration and counterreview](EMBODIED-SCALES-INTEGRATION.md) · [Lean source](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/systems-complexity/analysis/EmbodiedChoiceScales.lean) · [receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/systems-complexity/analysis/embodied-scales-verification.json).

## Mathematical interface

`X` represents the selected joint relations, including those realizing cognitive activity; `Y` represents a proposed description of them. Neither is asserted to be a complete universe state. Both descriptions share action type `A`. Supplied maps `p t`, laws `F t`, `G t` and policies `act t`, `representAct t` are time-dependent. The retained cognitive relations may be represented in `X` and `Y`; their formation is not a theorem hypothesis disguised as a conclusion.

The pseudometric is on `Y`. At each reached pair, `defect` bounds the difference between the projected next detailed state and the same-action represented next state. `propagation` bounds the effect of current state error under that same action. `changedAction` bounds the represented effects of the two selected actions at the same represented state. Two applications of the triangle inequality give the one-step bound. Induction and nonnegative `L t` give `E(t+1) = ε(t) + σ(t) + L(t) E(t)` over `n ≤ N`. Initial error and all reached-pair bounds are explicit hypotheses, not fitted automatically.

No action metric, global Lipschitz hypothesis or globally finite state space is required. Equal selected actions remove the action-effect term. It need not be positive merely because action labels differ. Claimed predictive application beyond an observed path requires evidence for the applicable counterfactual bounds, not merely inspection of one fitted trajectory. No conclusion follows about correctness or ethical warrant of the policies themselves.

## Declaration map

| Lean theorem | Exact scope |
|---|---|
| `controlled_one_step` | Three supplied discrepancy bounds imply the one-step bound. |
| `closed_loop_horizon` | Supplied policy-dependent histories and local bounds imply the finite-horizon recurrence bound. |
| `equal_actions_remove_action_error` | Equal actions at the same represented state give zero effect discrepancy. |
| `upper_margin_preserves_choice` | Nonnegative error, calibration and an inclusive upper margin preserve two true choices. |
| `lower_margin_preserves_choice` | The corresponding strict lower margin preserves two false choices. |
| `arbitrarily_small_score_error_changes_effect` | For each positive δ, scores −δ and δ differ by 2δ but select unit-separated effects at threshold zero. |
| `computed_history_is_actual` | Every computed finite event history is a trace of the existing `Generative.Process`. |
| `event_conserves_shared_support` | Each declared event preserves the sum of the three support stores. |
| `history_conserves_shared_support` | Every finite event list preserves that sum. |
| `acquired_signal_selects_effective_activity` | The specified sensing–response history acquires the shared unit. |
| `sensory_intervention_changes_choice_and_effect` | At equal initial support, the clamped sensor changes response and acquisition in the stated witness. |
| `bodily_amount_does_not_determine_choice` | Two reachable states have equal bodily amount and different retained choices. |
| `intervening_participation_defeats_retained_plan` | Another participant consumes after sensing; the selected attempt persists but cannot acquire the absent unit. |
| `response_does_not_create_unavailable_support` | With zero shared support, response cannot increase bodily support. |

## Finite episode correspondence and omissions

The joint `Episode` has three natural-number stores (`bodily`, `otherLiving`, `shared`) plus a sensor flag and a retained Boolean. All stores count the same declared abstract unit. `sense` updates the retained value from sensor availability and shared support; `choice` reads the retained value. A `respond` event transfers one available unit only when the retained choice is true; either outcome clears retention. `otherConsumes` transfers an available unit to the other store. Event order is supplied in a list; no universal fair scheduler or autonomous origin of the episodes is claimed.

The two states in the information-loss witness arise by the same sensing operation with the same support but different sensor availability. The changed choice is therefore linked to a changed causal channel in the declared process, not to freely toggling an ethical predicate. The successful and defeated plans share their initial acquisition history and differ by an intervening consumption event.

The sensor flag is not a cell; the bodily store is not an organ model. No anatomy, biochemical kinetics, metabolic consumption, sensor production, retention cost, reproduction or renewal is supplied. Conserving this support count is a property of this law, not universal thermodynamics or a claim that living processes operate for free. The witness explains a causal distinction and a representation failure; it cannot estimate biological effects. The general metric results and this discrete witness are separate checked constructions, not silently one calibrated application.

## Actual check and dependencies

`check_embodied_scales.py` rebuilt four local modules from their source bytes with Lean **4.30.0-rc2**, against the already installed Mathlib cache pinned at `ea11ccc0c5c7c4c562742e918fe2e0b2814a58aa`. **14 new theorem audits and 63 inherited audits passed**, without compiler warnings, proof holes, custom axioms or `native_decide`. Inherited audits belong to `GenerativeCore`, `SystemsOrganization` and `RelationsAcrossScales`; they are not new results.

The six real-valued results use `propext`, `Quot.sound` and `Classical.choice`. Five finite trace/witness results have empty dependencies; two conservation results use `propext` and `Quot.sound`; the final unavailable-support result uses `propext`. Standard logical dependencies are disclosed; they are not new ethical axioms. The upstream Mathlib cache was reused, not rebuilt. Compiler, checker, toolchain, manifest, source snapshots and logs have hashes in the receipt.

Reproduce from the repository root:

```sh
python3 experiments/integrated-correction/general-framework/generative-basis/lean/systems-complexity/analysis/check_embodied_scales.py
```

The [document check](EMBODIED-SCALES-CHECK.py) verifies local references and current/frozen proof bindings without repeating Lean. Formal checking establishes these implications under their supplied hypotheses. The [evidence assessment](EMBODIED-SCALES-EVIDENCE.md) separately evaluates biological correspondence.
