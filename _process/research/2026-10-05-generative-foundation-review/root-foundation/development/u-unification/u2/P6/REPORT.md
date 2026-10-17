# Batch P6 report (agent, 17 October 2026)

Saved by the integrator from the agent's final message.

I wrote five join modules in `u2/P6/Becoming/`. All of them build with `"unclean": []`. The three pure modules have empty axiom reports, and the two `...Inherited` modules carry only the axioms their periphery theorems bring in. Nothing was committed, landed or edited outside my batch folder.

## Modules written

| Module | Theorems | Axioms |
|---|---|---|
| `SeedReachProcesses` | 21 | none |
| `MoveOutcomeProcesses` | 17 | none |
| `RuleNarrowingProcesses` | 15 | none |
| `RuleNarrowingProcessesInherited` | 6 | inherited only |
| `MoveOutcomeProcessesInherited` | 1 | inherited only |

All five import `Becoming.Bridge`, or the pure module they extend.

## Readings used and roots covered

**`SeedReachProcesses`** (WholeGroundCoverage, CutCoverageAudit, EvaluatorGrounding). The edges of a process are its moves (`Moves`), and the seed closure is what the process reaches from a seed (`FromSeed`; `reached_iff` and `cutReach_iff` make this exact). A local atlas is a process whose labels are its scopes (`atlasProcess`); one scope's edges alone are `scopeProcess`; a family of atlases indexed by histories is `historyProcess`.
- **WholeGroundCoverage, 11 roots.** Each becomes a law of the process:
  - reach from seeds is the least invariant (`fromSeed_iff_invariant`, `covers_iff_invariant`, `unreached_has_invariant`, `substitute_seeds`);
  - the atlas laws: `scope_reach_in_atlas`, `glued_on_reach`, `alternating_beyond_scopes`, `unconnected_coverage_insufficient`;
  - the history laws: `history_reach_keeps` (stated for whole paths, not single steps), `history_fromSeed_iff`, `history_sound_on_reach`.
- **CutCoverageAudit, all 3 roots.** `cut_iff_not_fromSeed`, `noCut_iff_fromSeed_of_decidable`, and `upgrade_iff_dne`: absence of a cut gives reach in every process exactly where double-negation elimination holds.
- **EvaluatorGrounding, 1 root.** `self_good_derives_reachable_g0` becomes `reachable_living_significance`: chains are read as reach in `edgeProcess step`, and the conclusion is the core's `G0` on `Frame.ofInventory`.

**`MoveOutcomeProcesses`** (PracticalReach, and one PracticalJudgment root). A response relation is a process's step from a configuration (this builds on `guarantees_iff_completes`).
- `Ensures` means some single move completes the goal (the core's `Completes`).
- `Covers` is refinement between the moves of two processes at two configurations; `covers_iff` shows it is exactly preservation of every goal those moves complete.
- **General laws, 4 roots:** `completes_mono`, `common_goal`, `no_strict_gain_everywhere`, `covers_along`.
- **Models, 7 roots:** the four witness relations are processes on Bool: the constant law `toFalse` (`Law.process`), `free`, `setting` and `halted`; `steps_eq` shows they are exactly `fixed`, `uncontrolled`, `selectable` and `absent`. The seven model roots become: `free_wider_not_covering`, `law_covers_free_and_loses`, `setting_covers_and_gains`, `setting_covers_and_opens`, `setting_separate_not_joint`, `halted_ensures_nothing`, `summary_hides_loss`.
- **PracticalJudgment `robust_at_actual`** becomes `common_completes`.

**`RuleNarrowingProcesses`** (StandardsBridge). Learning is belief over rules narrowed by `After` on the pure observation process (`narrowed`). `mem_learn_iff` shows the learned list holds exactly the narrowed belief's rules; it builds on `revise_is_after`. A belief settles a question at a value (`Settles`) exactly where the answer procedure answers it (`answer_some`, `answer_none`, `answer_of_settles`). I proved these list facts here with empty axiom reports. 6 clean model roots are joined: `one_sample_settles_one`, `contrasting_settles_both`, `settled_differs_from_last`, `repeated_case_leaves_other`, `contradiction_settles_nothing`, `narrow_class_settles_wrongly`.

## Inherited-axiom modules

- **`RuleNarrowingProcessesInherited`** covers 5 StandardsBridge roots: `mem_revise`, `eliminated_rule_has_counterevidence`, `repetition_does_not_change_candidates`, `learning_transport`, `full_bool_repertoire_correct`. It also carries the non-root `mem_learn` as `narrowed_iff_fits`.
  - `narrow_once_iff`: `propext`
  - `narrowed_iff_fits`, `repeated_observation_idle`, `narrowing_transport`: `propext`, `Quot.sound`
  - `dropped_has_counterevidence`, `full_repertoire_settles_actual`: `propext`, `Classical.choice`, `Quot.sound`
- **`MoveOutcomeProcessesInherited`** covers PracticalReach's `failed_refinement_has_lost_goal`.
  - `lost_goal_of_not_covers`: `propext`, `Classical.choice`, `Quot.sound`

## Apart and root counts, before → after

Measured with `apart_roots.py` overlaying the batch folder.

| Module | Apart | Roots |
|---|---|---|
| StandardsBridge | 26 → 7 | 17 → 6 |
| PracticalJudgment | 30 → 29 | 15 → 14 |
| PracticalReach | 24 → 0 | 12 → 0 |
| WholeGroundCoverage | 27 → 1 | 12 → 1 |
| EvaluatorGrounding | 12 → 8 | 7 → 6 |
| CutCoverageAudit | 12 → 0 | 3 → 0 |
| **Total** | **131 → 45** | **66 → 27** |

All 27 remaining roots are in `classification.json`:
- **periphery-scope, 11:** StandardsBridge's answer-procedure laws (`answer_maximal`, `unique_maximal_safe`, `answer_transport`); PracticalJudgment's interfaces for requirement, allocation and due/done/released; `strict_indexed_rival_inconsistent`.
- **model-witness, 12:** the Bool repair and ceiling comparisons and `collective_duty_without_individual_duty`; the five-occurrence standpoint models; `alternating_domains_cover`; two StandardsBridge examples where no observation occurs.
- **restates, 2:** `robust_under_refinement` restates the core's `commonResponse_antitone`; `insufficient_support_retains_ambiguity` restates a conjunct of `one_sample_leaves_other_case_unsettled`.
- **support, 2:** `independent_choices_not_joint_capacity`, `uncertain_worlds_need_common_plan`.

None is classed `axiom-dependent`.

## Wrong or misplaced in the periphery modules

- **StandardsBridge** proves `mem_revise`, `mem_learn`, `answer_iff` and the transport laws with `simp` or classical reasoning. Clean proofs are easy: `RuleNarrowingProcesses` proves the needed answer facts with no axioms.
  - `eliminated_rule_has_counterevidence` uses `Classical.byContradiction`. Its conclusion is existential, so it cannot simply be rebuilt without it.
  - `insufficient_support_retains_ambiguity` duplicates the second conjunct of `one_sample_leaves_other_case_unsettled`.
- **EvaluatorGrounding**'s model definitions (`ownOcc`, `reachOcc`, `standpoint`) already carry `propext`, from pattern matching into `Prop`. So every model witness there inherits it.
- **PracticalJudgment**:
  - `independent_choices_not_joint_capacity` is a pure `omega` arithmetic fact carrying three axioms.
  - `finite_frontier` uses `Classical.choice`. The bridge's `Judgment.frontier_exists` is the clean version.

## For you to decide

1. **Registration:** the three pure modules go on the bridge side; the two `...Inherited` modules go in the periphery-join ring.
2. **Thin joins:** please judge whether `common_completes` (the definition of `CommonResponse` read through `robust_at_actual`) and `covers_along` (revisions instantiated at a process's step) clear your bar of "the base object plays a role". If not, reclassify them as `restates` and `periphery-scope`.
3. **Sequence-indexed interfaces:** I did not join PracticalJudgment's `Covered`, `Settled` and `Residual` by reading their time index along a run. I judged that reading decorative.

Files are in `/Users/ren/theories/_process/research/2026-10-05-generative-foundation-review/root-foundation/development/u-unification/u2/P6/`:
- `Becoming/SeedReachProcesses.lean`
- `Becoming/MoveOutcomeProcesses.lean`
- `Becoming/RuleNarrowingProcesses.lean`
- `Becoming/RuleNarrowingProcessesInherited.lean`
- `Becoming/MoveOutcomeProcessesInherited.lean`
- `classification.json`
- `apart.json`
