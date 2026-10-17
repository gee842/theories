# Batch A1 report (agent, 17 October 2026)

Saved by the integrator from the agent's final message.

# U batch A1: Selection, Learning, Learnable, Identification, Description (REPORT.md)

17 October 2026. Join modules for the five source modules, built and audited in scratch with `scratch_build.py` (every module `"unclean": []`, `"with_axioms": {}`), measured with `apart_roots.py` over this tree (`apart.json`). Nothing has been committed or landed, and no existing file was edited.

## Modules

| Module | Theorems | Imports |
|---|---|---|
| `Becoming/SelectionRuns.lean` | 14 | `Becoming.Parting` |
| `Becoming/LearningRuns.lean` | 32 (+2 defs) | `Becoming.LearnableRuns`, `Becoming.Parting` |
| `Becoming/IdentificationRuns.lean` | 30 (+1 def) | `Becoming.LearningRuns`, `Becoming.Courses` |

## Apart count

As in the table above: 133 → 9 apart and 66 → 6 roots for the source modules; 1,019 → 887 apart and 486 → 426 roots across the spine.

## Readings used

- **A run's registered course:** `Parting.course reg r` for a run of any process (an existing reading). For runs of a determined law, `LearnableRuns.course`, `LearnableRuns.record_eq`, `restsFrom_iff`, `rests_iff` and `Branching.law_run_state`.
- **Every course is a run of free branching:** `Parting.free` and `Parting.freeRun` (existing). These carry the laws that quantify over all courses, or over all histories with at most `N` states: `record_short`, `withBound_earliest`, `rest_without_bound_refuted`, `learner_rest_cubic`, `record_fixes_no_next`.
- **Parting:** `Parting.PartAt` and `Parting.RightAt` (existing) state "same record, different value" and "right at a step" of runs.
- **Likeness:** `Law.alike_iff_sameFuture`. Two moments of a law's run are one state exactly where their configurations are alike in the frame (`IdentificationRuns.sameAhead_iff_alike`).
- **Reached wholes:** `Courses.reachedFrom` (existing) is the whole a law's courses reach. The separation laws are stated of it, and `Courses.copy_relates_course` gives the copying witness.
- **Options as moments** (Selection/Learning `Relabel`): the options are the moments of a run, and the selector's model is the run's registered course, `Parting.course reg r : Nat → V`. What matters is a target on configurations, read at each moment. Because the options are `Nat`, no `DecidableEq` hypothesis is needed.

New reading definitions, each with the theorem that makes it exact:
- **`LearningRuns.Courses P reg`:** the registered courses of the runs of `P`. `course_mem` shows every run's course is a member. With the moments before `t` as the data, it carries `Training.fit_right_iff`, `unselected_beyond_data` and `loss_through`, and `Determines (Courses (free V) id) (· < t) x` carries `every_determines_nothing`.
- **`LearningRuns.answerReg pred other x`:** the registration of the answering law `answerStep`. `answer_course` and `answer_record` show that its course along every run from `[]` is `Learning.diagonal`.
- **`IdentificationRuns.parity`:** the law setting a third part to the parity of the first two. `parity_reached_iff` shows that one move of it reaches exactly the `EvenThree` triples.

## Roots covered (root → join)

- **Selection** (into `SelectionRuns`):
  - `selected_alike_iff`, `valued_alike_iff`, `singled_iff_untied` → same names;
  - `EquivariantChoice.untied` → `choice_untied`;
  - `EquivariantChoice.withholds_of_full_tie` → `choice_withholds_of_constant`;
  - `EquivariantValue.full_tie` → `values_alike_of_constant`;
  - `EquivariantValue.level` → `value_level_alike`;
  - `share_rises_through` → `share_rises_along`.
- **Learning, model section** (into `SelectionRuns`):
  - `selects_through_lumping` → `selects_through_registration`;
  - `values_lumped`, `selects_not_right_of_parted`, `selects_right_of_reads`, `values_not_right_of_parted`, `values_right_of_reads` → same names.
- **Learning, the rest** (into `LearningRuns`):
  - `claim_refuted_on_one` → `refuted_on_one_of_part`;
  - `no_record_fixes_next_finite` → `record_fixes_no_next`;
  - `learner_through_record`, `refuted_before`, `merged_bound`, `merged_unrested`, `held_learner_bounded`, `held_rest_unrefuted` → same names;
  - `lasso_of_rest` → `lasso_of_right`;
  - `determines_lumped_iff` → `determines_iff_registered_alike`;
  - `diagonal_open` → `answer_open`;
  - `swapTo_moves` → `answer_refutes`;
  - `not_moves` → `negation_never_rests`;
  - `Alternate.rests` → `alternate_rests`;
  - `Training.loss_through` → `loss_through_record`;
  - `Training.unselected_beyond_data` → `unselected_beyond_record`;
  - `Training.fit_right_iff` → `fit_right_iff_runs`.
  - Non-roots that only the Shift witnesses used, joined directly:
    - `lumped_right_iff` → `carried_right_iff`;
    - `lumped_world_right` → `world_carried_right`;
    - `every_determines_nothing` (with `every_free` and `free_determines_iff`) → `free_record_fixes_nothing`.
- **Learnable** (into `LearningRuns`):
  - `claim_not_right_on_both`, `refuted_on_one` → same names;
  - `Pair.first_not_rests` → `pair_first_not_rests`;
  - `Pair.not_lumped` → `pair_not_learnable`;
  - `Pair.whole_rests` → `pair_whole_rests`.
- **Identification** (into `IdentificationRuns`):
  - `record_fixes`, `record_short`, `withBound_holds`, `withBound_earliest`, `rest_without_bound_refuted`, `rests_of_lasso`, `learner_rest_cubic`, `answer_exceeds_bound`, `negation_derived`, `sameAhead_iff_below`, `sameAhead_iff_classes`, `sameAhead_iff_within` → same names;
  - `Law.sameFuture_classes_exact` → `classes_exact_runs`;
  - `Law.sameFuture_classes_unrefuted` → `classes_unrefuted_runs`.
- **Description** (into `IdentificationRuns`):
  - `sameAhead_orbit_iff` → `sameAhead_iff_alike`;
  - `Law.Returns.states` → `returns_states`;
  - `SameAhead.new_each` → `new_each`;
  - `finitely_many_states_iff_lasso` → `states_iff_lasso`;
  - `Negation.two_states` → `negation_two_states`;
  - `Negation.each_through_other` → `negation_each_through_other`;
  - `separated_of_whole` → `separated_of_reached`;
  - `separation_faithful_iff` → `separation_faithful_iff_reached`;
  - `separation_admits_extra` → `copy_separation_admits_extra`;
  - `whole_not_in_pairs` → `parity_whole_not_in_pairs`.

## For the integrator to decide

1. **Options as the moments of a run** (`SelectionRuns`). This reading is what joins the two `selection-through-a-model-of-the-options` records. The alternative is to take the options as configurations, with the registration as the model. That needs `[DecidableEq S]`, and I see no gain from it. Please confirm the reading or name the one you prefer.
2. **`share_rises_along`** reads each parent's level history as the states of a run of a process on `C → Nat`. That is a family of runs, one per parent, with the law about them. It is a thin join. You may prefer to classify `share_rises_through` as `restates` of `Capture.share_rises`, which is now on the base through it anyway.
3. **Two joins state weaker forms of theorems already on the base.** `held_rest_unrefuted`, a double negation, is weaker than `Identification.held_learner_rests`. `Law.sameFuture_classes_unrefuted` is weaker than `Law.sameFuture_iff_within`. I joined both because it cost little; classifying either as `restates` would be equally defensible.
4. **Two definitions of one reading on main.** `LearnableRuns.course` (runs of `Law.process next`) and `Parting.course` (runs of any process) are definitionally the same. I used `LearnableRuns.course` where a statement builds on `LearnableRuns`' `Rests` and `record_eq`, and `Parting.course` elsewhere. A later tidy-up could make one an abbreviation of the other.
5. **Possibly misplaced in the source modules** (no change needed for U):
   - `Relabel.EquivariantValue.const` is used nowhere.
   - `Selection.share_rises_through` is `Capture.share_rises` with a selection premise that is not used.
   - The `Learning.Shift` witnesses were the only users of five general lumping laws; those laws are now joined directly.

---

Files are in /Users/ren/theories/_process/research/2026-10-05-generative-foundation-review/root-foundation/development/u-unification/A1:
- Becoming/SelectionRuns.lean
- Becoming/LearningRuns.lean
- Becoming/IdentificationRuns.lean
- classification.json
- apart.json
