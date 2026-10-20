# Batch A2 report (agent, 17 October 2026)

Saved by the integrator from the agent's final message.

# U, batch A2: report

All 8 modules build clean with `scratch_build.py` and import only spine modules.

## Apart count (`apart_roots.py` with this tree)

| module | apart before | apart after | roots before → after |
|---|---|---|---|
| Likeness | 24 | 4 | 6 → 4 |
| Copying | 17 | 1 | 8 → 1 |
| CrossSituational | 14 | 5 | 9 → 4 |
| Retrodiction | 6 | 0 | 3 → 0 |
| Readout | 5 | 2 | 3 → 1 |
| Contacts | 15 | 12 | 4 → 1 |
| Revision | 4 | 1 | 4 → 1 |
| ContinuingRevision | 11 | 0 | 9 → 0 |
| **total** | **96** | **25** | **46 → 12** |

The 12 roots left are classified: 4 logical-strength, 4 restates, 2 model-witness, 2 support.

## Modules, roots covered, readings

- **`ListedOutcomeFrames`** (Likeness). Reading: pairs of frames whose moves have listed outcomes.
  - `sameBranchingTests_fix_iff_llpoForDecided`: branching tests fix likeness in all such frames exactly under `LLPOForDecided`. This feeds `eitherThroughout_iff_llpoForDecided` and its whole chain.
  - `llpo_of_sameBranchingTests_fix` covers `LLPO.of_eitherThroughout`.
  - `alike_iff_sameBranchingTests_of_nowhereDecided` covers `EitherThroughout.of_nowhereDecided`.
- **`CopyCourses`** (Copying). Uses the readings already in `Courses`: the copy law with `steps_orbit`, `inspection`, `release`, and `doubling`.
  - `swap_course_iff` covers `batch_all_swap`.
  - `runs_draw_lt_iff` and `runs_draw_midpoint` cover `use_lt_iff` and `use_midpoint`. They work through `run_copies` and `run_drawn`, which state what a run of the copy law has drawn.
  - `inspection_step_matches_iff` covers `inspect_matches_iff`.
  - `inspection_course_keeps_counts` covers `inspect_keeps_counts`.
  - `inspection_course_keeps_template` covers `defects_zero_iff`, using new course-length lemmas.
  - `doubling_course_iff` covers `required_add`.
- **`CandidateRuns`** (CrossSituational). Records are a run's moves (`run.window 0 n`).
  - `run_step_bearing` and `run_step_other` cover `candidates_snoc_bearing` and `candidates_snoc_other`.
  - `run_resolved_is_target` covers `resolved_is_target`.
  - `run_omitted` covers both `Omitted` roots, stated on the first move of any run of a one-move process.
- **`RetrodictionRuns`** (Retrodiction). Covers `fits_iff_same`, `agreed_reading_actual`, and `change_unlocated` (as two runs of `Courses.anyChange`).
- **`ReducedRuns`** (Readout).
  - `runs_decoder_iff_of_section` covers `decodes_iff_of_section`, over `anyChange` and `Courses.reducedRun`.
  - `course_reduced` and `run_reduced` cover `foldl_semiconj`, through a new `trace_foldl` for `ofMap`.
- **`ContactCourses`** (Contacts). A revision rule is read as the process `ofMap ρ`, whose moves are failure reports.
  - `blind_answers_steps_iff` covers `blind_answers_iff`.
  - `finite_blind_answers_steps` covers `finite_blind_answers`.
  - `run_stays_iff` covers `References.stays_iff`, with the channel as a run's configuration.
- **`RevisionRuns`** (Revision).
  - `history_gains` covers `retained_gains`. It works through `history_retained_iff`: the history of a run's registrations through step 1 is the joint reading of steps 0 and 1.
  - `run_closed_cannot_select` covers `old_cannot_select_rebuild`.
  - `rebuild_opens_keeps` covers `opened_keeps`, as a law of every rebuild step of `Revising.P`.
- **`ContinuingRuns`** (ContinuingRevision). All 9 roots, stated of the infinite run `continuing` and of the processes `P 9` and `P 0`. Uses `run_at` (the configuration at date `7n + k`) and `run_of_trace` (the converse of the source's `run_trace`).

## For the integrator to decide

1. **Thin readings.** Accept these or reclassify their roots as model-witness:
   - `run_stays_iff` and `run_closed_cannot_select` are laws of a single configuration, read at a run's configurations (the "any sequence" reading the brief allows).
   - `run_omitted` and `finite_blind_answers_steps` state a witness on a run or a process, as the pilot does for `Captured`.
2. **Restates.** `Courses.run_narrows`, `no_run_judge_of_merged` and `course_resolves_every_iff` re-prove the source roots `narrows`, `no_judge_of_merged` and `reads_every_iff` instead of using them. Likewise `inspection_course_le` re-proves `scan_le`. Re-pointing those proofs would make the four roots feed the base, but that edits an existing file.
3. **`Repeated` witness.** If an empty record ("before a run's first move") counts as a natural run reading, its two roots can be joined the same way as `run_omitted`.
4. **Waiting on other batches.** These are not roots; they stay apart only because their users are apart elsewhere:
   - 8 in `Contacts` and 3 in `References`, used by `ReferencePlan`.
   - `Readout.reading_single_iff`, used by `lumped_iff_singleValued` in `Coupling`.
5. **Misplaced, not wrong.**
   - `run_of_trace` belongs beside `ContinuingRevision.run_trace` in the source module.
   - `none_ne_some` is a local helper, needed because in this Lean version `Option.noConfusion` takes an `HEq` argument.

   I found nothing wrong in the source modules.
