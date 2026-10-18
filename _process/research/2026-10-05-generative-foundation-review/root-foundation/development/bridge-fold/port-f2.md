# F2: the six leaf modules against the core

18 October 2026. Board item F2; Ren: "please, do them, reduce bridges and add more theory to the spine" ([source](../../../../../../sources/15-codex-theory-conversations/2026-10-18-reduce-bridges-add-theory.md)). The format is the [step-0 audit](RESTATEMENT-AUDIT.md)'s. Grades: **same**, the core states the theorem (up to a definition the core holds by definition); **step**, the theorem follows from the cited core theorem by a reading of the periphery's definitions or a line of logic. Under [PORT-PROGRAM](PORT-PROGRAM.md) rule 7, a module is ported when every theorem is graded same or step. All six are ported. F2 adds six core modules: four new (`SeedReach`, `ScopedReach`, `Irreversibility`, `SummaryFutures`) and two joins moved into the core with native proofs (`MoveOutcomeProcesses`, `ContextArrivalTraces`). It also moves the laws that need no periphery out of the join `SeedReachProcesses`. Every one of these declarations has an empty axiom report.

Readings used throughout:

- **Relations as one move of a process.** A relation `r : A → O → Prop` from responses to outcomes is the step of a process from a configuration (`⟨fun _ a o => r a o⟩` at any configuration). `Guarantees r a goal` is one-move `Completes` (`Bridge.guarantees_iff_completes`), `CanEnsure` is `MoveOutcomeProcesses.Ensures` (`canEnsure_iff`, now in `MoveOutcomeProcessesInherited`), and `Refines` is `MoveOutcomeProcesses.Covers`: the same body, `Live r a` being `Enabled`.
- **Closures as reach from seeds.** `Reached seed edge` and `CutCoverageAudit.Reach seed edge` are `SeedReach`'s `FromSeed (edgeProcess edge) seed`, by `fromSeed_iff_closure` and the joins' `reached_iff_closure` and `cutReach_iff_closure`. A reverse-closed cut avoiding the seeds is the complement of a separating invariant (`SeedReachProcesses.hasCut_iff_separated`).
- **An atlas as a process with scopes as labels.** A `LocalAtlas` is `SeedReachProcesses.atlasProcess`. One scope's edges are `ScopedReach.only` of it, and a ground on a scope's domain, given on the domain's subtype, is a ground on configurations taken where the domain holds. Every atlas edge stays in its scope's domain by its type, which is the `inside` hypothesis of `ScopedReach`.
- **`BecomingCompatibility`, `BecomingReversibility`, `DerivedHistoryLaw`.** Their definitions are the core's by definition (`Becoming.Context`; `oneWay` is `DeadEnd.law`, `twoWay` is `Irreversibility.flip`), or read by `Bridge.derived_same_steps` (`derivedProcess` is `Readout.image` of the admitted histories), with `singletonFalseCode` equal to `SummaryFutures.code` on every history.

## PracticalReach

24 theorems. **Ported** (24 of 24). Core module: `Becoming.MoveOutcomeProcesses` (all names `MoveOutcomeProcesses.…`).

| Theorem | Grade | Core counterpart |
|---|---|---|
| `guarantee_mono` | step | `completes_mono` |
| `cannot_ensure_false` | step | `not_ensures_false` |
| `ensure_true_iff_live_response` | step | `ensures_true_iff` |
| `refinement_preserves_goals` | step | `Covers.ensures` |
| `refinement_iff_all_goal_preservation` | step | `covers_iff` |
| `refinement_refl` | step | `covers_refl` |
| `refinement_trans` | step | `covers_trans` |
| `failed_refinement_has_lost_goal` | step | `lost_goal_of_not_covers_of_dne` (classical in the periphery; the core takes double-negation elimination as a hypothesis, and states the constructive form `not_covers_iff`) |
| `finite_revisions_preserve` | step | `covers_along` |
| `projected_goal_iff` | step | `summary_ensures_iff` |
| `no_strict_improvement_for_every_goal` | step | `no_strict_gain_everywhere` |
| `common_goal_prevents_everywhere_strict` | step | `common_goal` |
| `fixed_ensures_false` | step | `toFalse_ensures_false` |
| `uncontrolled_cannot_ensure_false` | step | `summary_hides_loss`, second conjunct |
| `possible_enlargement_without_control` | step | `free_wider_not_covering` |
| `selectable_retains_fixed` | step | `setting_covers_toFalse` |
| `guaranteed_control_can_remove_possibility` | step | `law_covers_free_and_loses` |
| `selectable_ensures_each` | step | `setting_ensures_each` |
| `fixed_cannot_ensure_true` | step | `setting_covers_and_gains`, third conjunct |
| `retained_control_and_strict_new_goal` | step | `setting_covers_and_gains` |
| `outcome_goal_preservation_can_defeat_closure_goal` | step | `setting_covers_and_opens` |
| `separate_guarantees_not_joint` | step | `setting_separate_not_joint` |
| `empty_response_does_not_guarantee` | step | `halted_ensures_nothing` |
| `projection_can_hide_loss` | step | `summary_hides_loss` |

The four relations `fixed`, `uncontrolled`, `selectable` and `absent` are the steps of `toFalse`, `free`, `setting` and `halted` (`MoveOutcomeProcesses.steps_eq`, `rfl`).

## CutCoverageAudit

12 theorems. **Ported** (12 of 12). Core module: `Becoming.SeedReach` (names `SeedReachProcesses.…`).

| Theorem | Grade | Core counterpart |
|---|---|---|
| `reach_avoids_reverse_closed_cut` | step | `fromSeed_iff_invariant` |
| `reachable_implies_no_cut` | step | `separated_iff_not_fromSeed` |
| `has_cut_implies_not_reachable` | step | `separated_iff_not_fromSeed` |
| `not_reachable_has_cut` | step | `unreached_has_invariant` |
| `has_cut_iff_not_reachable` | step | `separated_iff_not_fromSeed` |
| `no_cut_iff_double_negated_reachability` | step | `not_separated_iff` |
| `no_cut_to_reachable_of_decidable` | step | `fromSeed_iff_not_separated_of_decidable` |
| `no_cut_iff_reachable_of_decidable` | step | `fromSeed_iff_not_separated_of_decidable` |
| `singleton_reachability_iff` | step | `fromSeed_iff_seed_of_no_moves` |
| `double_negation_elimination_implies_universal_cut_upgrade` | step | `fromSeed_of_not_separated_iff_dne`, converse |
| `universal_cut_upgrade_implies_double_negation_elimination` | step | `fromSeed_of_not_separated_iff_dne`, forward |
| `universal_cut_upgrade_iff_double_negation_elimination` | step | `fromSeed_of_not_separated_iff_dne` (universe-polymorphic, as the original) |

**What the calibration says about the unfolding** (AGENTS.md, "Proof and naming"). That a configuration is reached is a path in the unfolding from a seed. That no invariant property separates it from the seeds refutes only that it is unreached; it does not produce the path. `fromSeed_of_not_separated_iff_dne` shows that getting the path from the failed separation, for every process, is exactly double-negation elimination. One process on two configurations already needs it: one step whose occurrence is a proposition `p` given only as not refuted (`SeedReach.conditional`). Where the reach is decided, the two agree (`fromSeed_iff_not_separated_of_decidable`). So a reach claim over the unfolding needs a path, or a decision of reach; an exhausted search for a separating invariant is not one.

## WholeGroundCoverage

27 theorems. **Ported** (27 of 27). Core modules: `Becoming.SeedReach` (names `SeedReachProcesses.…`) and `Becoming.ScopedReach` (names `ScopedReach.…`).

| Theorem | Grade | Core counterpart |
|---|---|---|
| `reason_inheritance` | step | `fromSeed_iff_invariant` |
| `reached_is_admissible` | step | `fromSeed_invariant` |
| `reached_iff_entails` | step | `fromSeed_iff_invariant` |
| `universal_target_coverage_iff` | step | `covers_iff_invariant` |
| `uncovered_has_admissible_omission` | step | `unreached_has_invariant` |
| `reached_mono` | step | `Reach.map` with `fromSeed_iff_closure` |
| `substitute_grounded_seeds` | step | `substitute_seeds` |
| `local_sound_iff_joined_sound` | step | `ScopedReach.invariant_iff_only` |
| `local_sound_gives_global_inheritance` | step | `fromSeed_iff_invariant` |
| `local_reach_in_joined` | step | `ScopedReach.only_reach` |
| `glued_ground_iff_local` | step | `ScopedReach.glued_iff_local` |
| `compatible_local_ground_transport_glues` | step | `ScopedReach.glued_invariant` |
| `jointly_grounded_scope_inheritance` | step | `ScopedReach.glued_on_reach` |
| `history_edge_preserves_history` | step | `ScopedReach.within_keeps` |
| `history_reach_projects` | step | `ScopedReach.fromSeed_within_iff`, forward |
| `history_reach_lifts` | step | `ScopedReach.fromSeed_within_iff`, converse |
| `history_reach_iff` | step | `ScopedReach.fromSeed_within_iff` |
| `history_local_sound_gives_global` | step | `ScopedReach.invariant_on_within_reach` |
| `alternating_domains_cover` | step | `ScopedReach.domain_covers` |
| `alternating_first_step` | step | `ScopedReach.alternating_steps`, first conjunct |
| `alternating_second_step` | step | `ScopedReach.alternating_steps`, second conjunct |
| `alternating_join_reaches_finish` | step | `ScopedReach.alternating_beyond_scopes`, first conjunct |
| `first_scope_reach_stays_inside` | step | `ScopedReach.first_scope_stays_inside` |
| `second_scope_reach_stays_at_seed` | step | `ScopedReach.second_scope_stays_at_seed` |
| `alternating_beyond_separate_closures` | step | `ScopedReach.alternating_beyond_scopes` |
| `unconnected_reach_is_seed` | step | `fromSeed_iff_seed_of_no_moves` |
| `local_domain_coverage_insufficient` | step | `ScopedReach.halted_coverage_insufficient` |

The family over histories in the core is a family of processes, one per history (`ScopedReach.within`); the periphery's is a family of atlases, each read as a process by `atlasProcess`.

## BecomingCompatibility

20 theorems. **Ported** (20 of 20). The 17 the step-0 audit graded same or step stand. The three it graded *unfolding* now have core counterparts in `Becoming.ContextArrivalTraces`, which states them of the core's `Arrives` and `evolvingLaw`. `Arrives` on a one-move word is `Advance` (`arrives_singleton`).

| Theorem | Grade | Core counterpart |
|---|---|---|
| `empty_support_cannot_advance` | step | `ContextArrivalTraces.empty_support_no_arrival` with `arrives_singleton` |
| `actual_step_supplies_advance` | step | `ContextArrivalTraces.step_arrives` with `arrives_singleton` |
| `changed_context_is_formed` | step | `ContextArrivalTraces.changed_context_arrives` with `arrives_singleton` |

## BecomingReversibility

10 theorems. **Ported** (10 of 10). The 7 the step-0 audit graded stand. Core module for the rest: `Becoming.Irreversibility`.

| Theorem | Grade | Core counterpart |
|---|---|---|
| `oneWay_no_return` | same | `Irreversibility.deadEnd_no_return` (`oneWay` is `DeadEnd.law`) |
| `same_occurring_change_different_return` | same | `Irreversibility.same_change_different_return` (`twoWay` is `flip`) |
| `incomplete_questions_can_hide_irreversibility` | step | `Irreversibility.constant_reading_hides_loss` (`Possible` unfolded, the constant observation as the summary `fun _ => ()`) |

## DerivedHistoryLaw

6 theorems. **Ported** (6 of 6). The 4 the step-0 audit graded stand. Core module for the rest: `Becoming.SummaryFutures`.

| Theorem | Grade | Core counterpart |
|---|---|---|
| `unrestricted_summary_exact` | step | `SummaryFutures.futures_through` at `code`, read through `derived_same_steps` and `admitted_feasible_iff` |
| `exact_futures_can_change_encoded_endpoint` | step | `SummaryFutures.endpoint_moved` with `futures_through` |

## The three joins

- **`Becoming.MoveOutcomeProcesses`**: core now, imports `Becoming.Inquiry` and `Becoming.Recurrence`. Every statement it held is unchanged. `Covers` has `PracticalReach.Refines`'s body written out, so `MoveOutcomeProcessesInherited.lost_goal_of_not_covers` still takes it. Three declarations whose statements name `PracticalReach` moved, names unchanged, to `MoveOutcomeProcessesInherited`: `canEnsure_iff`, `summary_iff` and `steps_eq`. `common_completes` is now the foundation's `CommonResponse` itself, not `PracticalJudgment.robust_at_actual`.
- **`Becoming.ContextArrivalTraces`**: core now, imports `Becoming.Context`. Its three theorems keep their names and now state laws of the core's `Arrives`, `evolvingLaw` and `ChangingContext.relation`, which `BecomingCompatibility`'s `Arrives`, `evolving` and `changingRelation` are by definition. `ContextArrivalTracesInherited` imports `BecomingCompatibility` itself now.
- **`Becoming.SeedReachProcesses`**: stays in the bridge ring.
  - `Moves`, `FromSeed`, `fromSeed_iff_invariant`, `covers_iff_invariant`, `unreached_has_invariant` and `substitute_seeds` moved, names and statements unchanged, to the core module `Becoming.SeedReach`, with proofs that no longer pass through `WholeGroundCoverage`.
  - `cut_iff_not_fromSeed`, `noCut_iff_fromSeed_of_decidable` and `upgrade_iff_dne` are now readings of the core's separation laws through `hasCut_iff_separated`, which is new.
  - What remains reads the periphery's closures, atlases and cuts.

Counts: see the study's section 8.
