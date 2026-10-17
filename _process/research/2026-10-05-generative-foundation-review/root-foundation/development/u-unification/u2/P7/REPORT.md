# Batch P7 report (agent, 17 October 2026)

Saved by the integrator from the agent's final message.

Eight join modules build clean in scratch. `scratch_build.py` shows `"unclean": []`, there is no `sorry` and no Mathlib, and none of my own proofs use `simp`, `omega` or `decide`. Across the 12 periphery modules, apart theorems fell from **114 to 83** and roots from **69 to 52**. All 52 remaining roots are classified in `classification.json`.

## Modules written (in `u2/P7/Becoming/`)

**Pure ring (every axiom report empty):**
- **`StrictTransportRuns`** (GenerativeLossComparison). "No worse" is read off a frame: `t` realizes every claim `s` realizes. The feasible options are the configurations a process reaches from `s`.
  - `strict_above_along`: a strict anchor holds along a run that loses no claim (through `matched_loss_reduction_preserves_priority`).
  - `strict_below_along`: a strict rejection holds along a run that gains no claim (through `matched_loss_increase_preserves_rejection`).
  - `reachable_reason`: a strict comparison among reachable configurations supplies the reason (through `transported_comparison_supplies_reason`).
- **`ExtensionFrames`** (GenerativeComparison).
  - `extension_new_relevance`: under the continuation condition, a generative extension realizes new content that `Frame.relevance` counts as relevant. It goes through `new_realization_of_unrestricted`, so it also connects the non-root `new_realization_has_positive_relevance`.
  - `survives_iff_lifted`: exactness for a functional situation's one-step frame.
  - `restricted_survives`: restricting the responses keeps a survivor (through `feasible_restriction_preserves_survivor`). This holds only on a functional frame: on a frame where a response has several outcomes, removing outcomes can make a response extended.
- **`ExtendedClaimFrames`** (ConcernExtension). A frame whose claims are `Sum I J` (old claims and newly distinguished ones) realizes exactly `extend old fresh`. This module has the exactness lemmas and joins all 4 roots (`crossed_incomparable`, `gain_transfer_iff`, `fresh_gains_decide`, `fresh_basic_reverses`).
- **`ReachableFrames`**.
  - `carries_compose` and `complement_closed_no_extension` (JointContinuationClassification, on `Frame.continuations`). The second reads: where a frame's claims are closed under a complement on its reachable configurations, no reachable configuration generatively extends another.
  - `required_through_summary` (AlignmentDirection `revision_preserves_requirement`): a requirement over reachable configurations carries through a summary map whose steps map forward and lift back (`Reach.map` / `Reach.lift`).
  - `common_relative_on_scope` (JointInterpretation, on a policy's `Scope`).
- **`InterfaceTraces`** (a new reading). An `AlignmentInquiry.Interface` is a `Process S (Sum (Q × Bool) A)`, where a probe move carries its answer. Its exactness theorems are `run_iff_trace`, `passes_iff_completes` and `valid_iff`.

**Periphery-join ring (per the addendum):**
- **`InterfaceTracesInherited`**: `selected_iff_completes`, `none_selected_iff`, `selected_completes`. It inherits `propext` and `Quot.sound` from `chosen_exists_iff`, `no_listed_policy_iff` and `chosen_sound`. Its helper `false_iff_not` is pure.
- **`ClassifiedFramesInherited`**: `frame_two_extremes_suffice` and `frame_strict_growth_robust`. The basic contents are what the frame realizes, as in `CoursesBridge`. It inherits `propext`, `Classical.choice` and `Quot.sound` from `two_extremes_suffice` and `known_basic_improvement_is_robust`.
- **`ReachableFramesInherited`**: `certified_reason_on_scope`, which reads `certified_integral_supplies_contributory_reason` over a policy's scope with living significance on the frame. It inherits `propext` and `Quot.sound`.

## Apart / roots, before → after

| Module | Before | After |
|---|---|---|
| GenerativeLossComparison | 15/12 | 11/9 |
| GenerativeComparison | 11/9 | 9/8 |
| PositiveGroundUncertainty | 9/7 | 6/6 |
| ProtectionPriorityRival | 15/7 | 15/7 |
| AlignmentDirection | 9/6 | 8/5 |
| AlignmentInquiry | 9/6 | 5/4 |
| ClassificationRobustJudgment | 13/5 | 8/3 |
| PositionedPositiveReason | 10/4 | 10/4 |
| ChanceAdequacy | 8/4 | 8/4 |
| ConcernExtension | 8/4 | 0/0 |
| JointInterpretation | 5/3 | 3/2 |
| JointContinuationClassification | 2/2 | 0/0 |

None of my join theorems stands apart.

**How the 52 remaining roots are classified:**
- **model-witness, 38**: the Route controls, the profile example, the PositiveGroundUncertainty arrangement, the one ProtectionPriorityRival situation, the AlignmentDirection plans and times, the ClassificationRobustJudgment models, the positions example, the two-entry chance domain and `incompatibleRows`.
- **support, 6**: `ratio_bounded`, `repertoire_complete`, `empty_uncertainty_never_certifies`, `observational_obstruction`, `same_answer_same_selected_response` and `repair_adds_positive_new_protection`. The last is the core's `mass_lt_of_added`, which the core itself classifies as support.
- **restates, 6**:
  - `generative_extension_transitive` restates `Extension.trans`.
  - The three selection/reason roots of GenerativeComparison are the deterministic case of the Bridge's lifted laws on every frame.
  - The two ChanceAdequacy roots restate `every_weighting_iff` and `mass_mono`.
- **general-structure, 1**: `faithful_redescription_preserves_strict`.
- **periphery-scope, 1**: `route_reason_depends_only_on_access`; the core concept is `PositionedArticulation`.

No root is classified `axiom-dependent`.

## For the integrator
- **Restates or join?** I classified the four GenerativeComparison selection/reason roots as `restates` rather than joining them, because the Bridge already states the lifted laws on every frame. With `survives_iff_lifted` they could be joined through the roots on the situation frame instead, if you prefer that.
- **Shared interface reading.** P1's `InstallationTraces` re-derives `run_iff` and `passes_iff` for one specific interface. The general `InterfaceTraces.process` / `run_iff_trace` could serve it; that is your call.
- **Readings with no moves.** `ExtendedClaimFrames` and `ClassifiedFramesInherited` read contents off a frame's `realized` and use no moves, as `CoursesBridge` does. Please confirm that precedent is acceptable.
- **Nothing wrong found** in the periphery modules.
- **Scratch files.** `TREE/.build` and `TREE/apart.json` are scratch outputs left in the batch folder.
