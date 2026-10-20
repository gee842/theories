# Batch P3 report (agent, 17 October 2026)

Saved by the integrator from the agent's final message.

After the second pass, 53 of the 63 starting roots are joined and the other 10 are classified. CompositionalTransmission has nothing left apart. All four modules build with `"unclean": []`. The three `...Inherited` modules carry only `propext` and `Quot.sound`, and no `Classical.choice`.

## Counts (apart / roots)

| Module | Start | After first pass | Now |
|---|---|---|---|
| CompositionalFormation | 37 / 25 | 35 / 23 | 1 / 1 |
| CompositionalAcquisition | 25 / 22 | 25 / 22 | 10 / 9 |
| CompositionalTransmission | 27 / 16 | 26 / 15 | 0 / 0 |

Across spine and periphery, the tool now reports 922 apart and 596 roots.

## Modules, all in `.../u-unification/u2/P3/Becoming/`

**1. `QueryTraces.lean`** (pure; empty axiom reports; 8 theorems)
- Reading: `queryProcess := Assurance.ofMap deliver`, where configurations are exchanges and moves are queries.
- `trace_iff` makes it exact: a course of the process is exactly a lesson.
- Joins `teacher_program_changes_received_evidence`, `old_record_can_admit_wrong_constructed_operation` and `asymmetric_composition_exposes_the_new_failure`.
- Change since the first pass: its two closed computations are now `rfl` instead of `decide`.

**2. `TrainingProcessesInherited.lean`** (periphery-join ring; 10 theorems, 11 declarations)
- Reading: `trainProcess := Assurance.ofMap (fun s c => train c s)`, where configurations are learners and moves are codes. `step_iff` makes it exact.
- Joins 11 roots as laws of one training step:
  - `step_records`, `step_installs`, `step_support` and `step_rests_when_short`.
  - `step_code_transfers`, which covers `actual_records_form_interpretation` and `acquired_all_expressions`.
  - `step_evidence`, which covers `actual_records_supply_evidence`.
  - `step_then_execute`, which covers `acquired_execution` and `acquired_execution_conserved`.
  - `novel_after_step` and `installed_without_execution`.
- Axioms:
  - `propext` on all 11 declarations.
  - `Quot.sound` as well on `step_installs`, `step_code_transfers` and `step_then_execute`.

**3. `FormationTracesInherited.lean`** (periphery-join ring; 26 theorems, 30 declarations)
- Reading: a new inductive `FormationMove` with six moves (place, inspect, discard, develop, encounter, reconsider). `formationStep` sends each move to the periphery's function for it, and `formationProcess := Assurance.ofMap formationStep`.
- `trace_iff` makes it exact: a course ends where its moves, taken in turn, take the start.
- Joins 22 roots:
  - **Conserved amounts:** every move and every course keeps support plus spent (`step_support`, `course_support`), through all six of the periphery's `*_preserves_support` theorems. A placing move keeps parts plus used parts (`place_parts`).
  - **Inspection-step laws:** `inspection_transfers`, `extended_inspection_transfers` and `inspection_installs_own`, through `accepted_generated_program_transfers`, `extra_probe_restores_transfer_for_generated_routes` and `correct_program_fits_actual_records`.
  - **Example witnesses as courses:** courses `[develop]` and `[develop, encounter collapsed novel, reconsider]` from the periphery's `prepared` configurations, through 17 `decide` witnesses (`develop_course_*`, `repair_course_*`, `training_alone_no_response`).
  - `develop_course_removed` reads `damaged` as removing the installed program from where the course ends, like the pilot's perturbed configurations.
- Axioms:
  - `propext` on all 27 audited declarations.
  - `Quot.sound` as well on `step_support`, `course_support`, `place_parts` and the three inspection theorems.

**4. `QueryTracesInherited.lean`** (periphery-join ring; 21 theorems)
- Readings:
  - A learner after a lesson (`learn`) is the formation move `develop` applied to the receiver where a query course ends.
  - Succession is the determined law `Law.process successor`. Its runs pass through the periphery's cohorts (`run_cohort` via `Branching.law_run_state`; `orbit_cohort` and `orbit_limited`).
- Joins all 15 Transmission roots plus the two Acquisition record roots:
  - **One query step:** `step_delivers` and `step_adds_nothing_without_response`.
  - **Conserved amount along courses:** `course_joint_support`.
  - **Learning after a course:** `learned_selective_funded`, `learned_selective_loses_distinction`, `learned_depends_on_course` and `learned_blocked_short`.
  - **Succession runs:** `succession_step_keeps`, `succession_keeps_correspondence`, `succession_keeps_lost_distinction`, `succession_stabilizes_change`, `formed_succession_teaches`, `formed_succession_second`, `budget_succession_blocked`, `peer_repair` and `peer_keeps_error`.
  - **Acquisition record roots:** `course_without_composite` and `course_reversed_composite`.
- Axioms:
  - `propext` on all 21 declarations.
  - `Quot.sound` as well on `course_joint_support`, `succession_step_keeps`, `succession_keeps_correspondence`, `succession_keeps_lost_distinction` and `succession_stabilizes_change`.

None of my proofs uses `simp`, `omega` or `decide`. They use `▸`, `trans`, `congrArg`, `if_pos`/`if_neg`, `rfl` and pattern matching. A few use `subst`, `rw` and `unfold`, which bring in no axioms. Each Inherited docstring ends by naming the axioms it inherits and the periphery theorems and definitions they come from.

## `classification.json` (10 roots)
- **`model-witness` (6):** `changed_motivation_preserves_acquired_content`, `changed_order_invalidates_transfer`, `nonuniform_matches_training`, `nonuniform_fails_transfer`, `novel_expression_not_a_training_item`, `unresolved_order_can_preserve_a_novel_answer`.
- **`periphery-scope` (4):**
  - `probe_readings`, `reencoding_preserves_content` and `indistinguishable_reversal_preserves_every_expression` concern how the grammar evaluates expressions, which has no evident process; there is no corresponding core concept.
  - `no_exact_order_without_composite_probe` concerns KnowledgeCorrespondence's resolution interface, which the bridge doesn't identify with any core concept.
- No root is left as `axiom-dependent`.

## Wrong or misplaced in the periphery
- Most of the periphery's own `propext` comes from list matches with overlapping wildcard patterns, starting at `readEvidence.match_1`. It then spreads through `interpretationFromRecords`, `train`, `develop`, `reconsider`, `learn`, `successor` and `cohort`.
- An exhaustive, non-overlapping version of `readEvidence` has an empty axiom report and still gives `readEvidence (trialRecords c) = some (observe c)` by `rfl`; I tested it in scratch.
- Rule 8 keeps the periphery files unchanged, so this is only for the record.

## For the integrator to decide
1. **Two record readings.** `course_without_composite` and `course_reversed_composite` read Acquisition's "missing" and "corrupted composite" records as records delivered by query courses. The second uses a sender whose composite response is reversed. Accept these readings, or move the two roots back to `model-witness`.
2. **New inductive.** `FormationMove` is a new reading definition: the six moves of the formation apparatus, each mapped to the periphery's function for it. Confirm it counts as the evident reading of that structure.
3. **Repeated docstrings.** The Inherited docstrings list the periphery theorems that contribute each axiom, so they are long. Trim them if the ring's convention is shorter.
