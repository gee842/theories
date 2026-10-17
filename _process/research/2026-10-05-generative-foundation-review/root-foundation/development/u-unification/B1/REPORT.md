# Batch B1 report (agent, 17 October 2026)

Saved by the integrator from the agent's final message.

### Modules
All in `/Users/ren/theories/_process/research/2026-10-05-generative-foundation-review/root-foundation/development/u-unification/B1/Becoming/`. Together they hold 48 theorems and one definition, and none of them is newly apart.
- **`RecurrenceRuns.lean`** (8 theorems, 1 definition):
  - `lossless_iff_returns` and `merges_loses`, read as laws of the process `Law.process next`.
  - The kept history: `kept_lossless`, `kept_never_returns`, `kept_loses_beginning`, `kept_unlisted`, `return_keeps_history`.
  - A new reading, `keptRun` (the history kept along a run), with `keptRun_present` making it exact: its present is the run's configuration.
- **`AttractionRuns.lean`** (15):
  - `returning_invariant`, `drawnInto_returning`, `drawn_iff_lost`, `drawn_not_keeps`, `lossless_iff_none_drawn`, `merges_draws`.
  - Counting on and counting down: `succ_drawn_lossless`, `pred_drawn_keeps`.
  - Ratchet read as a process: `ratchet_merges`, `ratchet_false_never_returns`, `ratchet_false_lost`, `ratchet_true_not_drawn`.
  - The three Branching roots, with Captured read as a process: `captured_rule_invariant`, `captured_state_drawn`, `captured_rule_drawn`.
- **`LastingRuns.lean`** (18, plus Viability's root):
  - On runs of the disturbed process: `lasts_iff_runs`, `guarded_upto_iff`, `guarded_none_iff`, `reaches_iff_runs`, `runs_iff_of_exact`, `reaches_trans_runs`, `search_runs_need_decision`.
  - On courses: `courses_iff_of_exact`, `drained_of_courses`, `collapse_leaves`.
  - On a determined law's courses: `determined_lasts_iff_courses`, `reaches_iff_not_lasts_courses`, `dual_needs_decision_courses`, `numeric_needs_decision_courses`, `reaches_excludes_courses`.
  - `stays_below_iff` on runs, and Viability's `needs_admissible` as `needs_admissible_runs`.
- **`CountdownCourses.lean`** (3): `not_done_before_course`, `slow_exits`, `slow_misses`, all on traces of `ofPartial`.
- **`HorizonWebs.lean`** (1): `prefix_does_not_decide`, stated on the two static webs.
- **`CounterfactualRuns.lean`** (3):
  - A new reading, `inputs_run_state`: a run of the standard model is the trajectory of its moves.
  - `course_runs`: every run of the course's standard model from the start is the generated history.
  - `courseWorld_level_zero`: the course world begins at the starting levels.

**Readings used:**
- A determined law as a process: `Law.process`, `Law.run`, `Branching.law_run_state`, Branching's `law_*_iff` bridges, and `Law.absorbing_iff_invariant`.
- From Courses:
  - the disturbed process's runs (`run_history`, `run_admissible`, `historyRun`, `lasts_iff_courses`, `Reaches.runs`);
  - a determined law's courses (`trace_orbit`, `orbit_trace`, `reach_iff_orbit`, `course_reaches_iff_orbit`);
  - `anyChange` and `anyRun`.
- Elsewhere: `Assurance.trace_ofPartial_iff`; `Web.static` with `static_renewingIn` and `static_consumingIn`; `inputs`; `ExchangeLaw.courseWorld`.

### Apart count
| module | apart before → after | roots before → after |
|---|---|---|
| Attraction | 35 → 4 | 13 → 1 |
| Recurrence | 26 → 8 | 11 → 4 |
| Branching | 9 → 0 | 3 → 0 |
| Lasting | 33 → 2 | 17 → 2 |
| Openness | 8 → 8 | 1 → 1 |
| Horizon | 7 → 0 | 1 → 0 |
| Countdown | 4 → 1 | 4 → 1 |
| Viability | 2 → 1 | 2 → 1 |
| Counterfactual | 2 → 0 | 2 → 0 |
| **total** | **126 → 24** | **54 → 10** |

`classification.json` classes the 10 roots still apart:
- **restates (7):** `Law.drawn_of_lost`, `Law.Lossless.unlisted`, `Law.lost_stays`, `Law.rise_not_lossless`, `not_marks`, `Lasting.fixed_avoids`, `Countdown.Advances.completes`.
- **support (2):** `Lasting.Reaches.mono`, `Viability.guardedStep_none`.
- **logical-strength (1):** `Listed.lpo_of_few`.

### For the integrator to decide
1. **The 7 `restates` roots.** The base already has each one's law, proved independently in Branching's general-process theorems and Courses' course forms; those proofs never cite the Law versions. These roots keep 9 helpers apart, such as `Law.lost_drawn`, `reachable_absorbing`, `Lossless.no_rise` and `Reachable.earlier`. Joining them would only duplicate theorems already on the base. The clean fix is for one side to cite the other, and that needs edits to existing files.
2. **`unheld_of_new` and `unlisted_of_new` are still apart only because the pilot isn't in my overlay.** They feed once `SeekingRuns.more_needs_open` lands.
3. **Openness:** classing `lpo_of_few` as logical-strength leaves its 7 `Few` helpers apart.
4. **Three decision-strength roots are joined, not classified:** `Search.histories_need_decision`, `dual_needs_decision` and `numeric_needs_decision`. Each is the boundary of a law already on the base. Reclassify them if you prefer to keep logical-strength roots apart.
5. **Readings that might be questioned:**
   - `stays_below_iff` reads "every sequence" as every run of `Courses.anyChange`.
   - `collapse_leaves` keeps the root's `Drains` conjunct, which is about the law that defines the process rather than the base object.
   - `HorizonWebs.prefix_does_not_decide` states agreement as equal levels of the shared condition up to `h`, proved from `Feedback.descending`. The root's equal-start and agreeing-schedule conjuncts are about the law, not the web, so I left them out.
   - `keptRun` and `inputs_run_state` are new reading declarations, each with the theorem that makes it exact.
6. **No source theorem looks wrong.** One wording point: the docstrings of `Branching.necessarilyDrawn_iff_not_returns` and `Branching.Lossless.returns` call them "the instance of" the Law theorem, but their proofs don't use it. That is why those Law roots stood apart.