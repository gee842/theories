# Batch C2 report (agent, 17 October 2026)

Saved by the integrator from the agent's final message.

| Module | Before (roots) | After (roots) |
|---|---|---|
| Typicality | 43 (4) | 1 (1) |
| Situations | 32 (9) | 0 |
| Gluing | 43 (13) | 1 (1) |
| Context | 18 (7) | 2 (1) |
| Quantum | 9 (5) | 9 (5) |
| Weighted | 16 (13) | 7 (6) |
| Courses | 1 (1) | 1 (1) |
| Readings | 2 (2) | 0 |
| **Total** | **164 (54)** | **21 (15)** |

The joins also make two Boundaries theorems and one Identification theorem feed the base. None of the 76 new theorems stands apart.

**Modules written**
- **`TypicalRuns`** (Typicality). A course of n steps is read as the record a run of free branching on two values shows over its first n steps. `mem_courses_iff` proves this exactly, and `courses_records` shows each record is listed once.
  - `sum_listing` / `total_listing` make every count the same for any repetition-free list holding the records.
  - The counts restated over records: `records_count`, `records_weight`, `histories_records`, `records_spread`, `records_typical`, `records_concentrated`, `records_few_far_ahead`. The record `typicality-by-counting` can now cite these.
- **`SituationTraces`** (Situations, plus `Interference.cancels`). Every count is now a count of traces of the finer law (a determined process):
  - `finer_traces` proves `Situations.finer` lists each trace once when moves and configurations are listed without repetition. `FinerTraces` had left this open.
  - The counts as traces: `traces_count`, `course_traces`, `traces_typical`, the three `event_traces_*`, `course_traces_listed`, `signed_traces`, `cancels_traces`, `cancels_counts`.
  - Weighted's `pair_*` lemmas now feed the base through `signed`.
- **`ContextualRuns`** (Gluing, Context). It reads a run three ways: the world of readings at a step, a context-free description of its configurations (`val`), and the readings it passes through, taken as a whole.
  - Bell-type bounds over any n steps of any run: `chsh_run_le`, `specker_run_le`, `square_run_le`, `cycle_run_le`.
  - Readings in context meet every context at every step, and are context-free at no step: `*_in_context`, `*_in_context_not_free`, `specker_not_free`.
  - Registrations respecting the possibilities are never context-free: `specker_respecting_not_free`, `square_respecting_not_free`, `noGlobal_run_iff`.
  - The cycle and the run's readings as a whole: `cycle_run_iff`, `chsh_wins_iff`, `passes_glued`, `passes_local`, `specker_not_passes`, `square_not_passes`.
- **`WeightedTraces`** (Weighted). Lumpability on processes (`lumped_iff`). Memory must be kept in the configuration (`memory_not_steps`), and it is kept by the law on configurations remembering the last move (`keptLaw`, `kept_traces`).
- **`BoundaryWorlds`** (Readings). The two Readings dichotomies stated for a world's affecting relation: `presupposition_iff_all`, `bounded_invariant_iff`.

**Classified roots** (`classification.json`)
- **Support:** `CrossSituational.distinct_iff`, `Typicality.total_congr_mem`, `Square.at_pos`, `Weights.truncation`, `counting_truncation_le`, `mass_lt_of_added`, `Interference.unseen_balanced`.
- **Model-witness:** the five Quantum matrix identities, `Lumping.loses`, `Interference.truncation_misses_cancellation`.
- **Restates:** `ParitySystem.glues_iff`, restated on the base by `ParitySystem.world_free_iff`.

Of the six apart theorems that are not roots, four are Quantum lemmas behind the Quantum roots, one is `Interference.unseen`, and one is `ChangingContext.ends`, which only the periphery uses.

**For the integrator to decide**
1. **Thin joins under standard 1:**
   - `*_in_context`: the registration is the same at every configuration, so the run enters only through `r.state t`. ParityReadings' `quantum_at` works the same way. The substance is in the `*_not_free` companions.
   - `chsh_wins_iff`: `CHSH.support_iff` at the run's description.
   - `passes_glued` and `passes_local`: general laws instanced at the run's readings.

   If you drop any of these, the matching roots go to `model-witness` or `support`.
2. **`BoundaryWorlds` relation:** it uses a world's affecting relation; `Shares` would also be admissible. If another batch joins Boundaries itself, the two Readings roots could instead be classed `restates`.
3. **`memory_not_steps` hypothesis:** it needs the process's steps read by a Boolean weight (the same hypothesis as `possibility_transfer_iff`). Without it the root can't be reached constructively.
4. **List lemmas:** listings use `CrossSituational.Distinct` (it works at every universe). `TypicalRuns` re-proves three membership-in-append lemmas that already exist under other names in `FinerTraces` and `Weighted`; it could import `FinerTraces` instead.
5. **Docstrings now out of date** (not edited):
   - `FinerTraces`' "What is not derived" paragraph says no theorem excludes repetition in `finer`; `finer_traces` now does.
   - `ParityReadings` says the cycle law has no base object without supplying one; `cycle_run_iff` and `cycle_run_le` state it of a run's context-free description, supplied as a hypothesis.
6. **Names:** none collide with main, C1 or the pilot.

Files are in `/Users/ren/theories/_process/research/2026-10-05-generative-foundation-review/root-foundation/development/u-unification/C2/`:
- `Becoming/TypicalRuns.lean`
- `Becoming/SituationTraces.lean`
- `Becoming/ContextualRuns.lean`
- `Becoming/WeightedTraces.lean`
- `Becoming/BoundaryWorlds.lean`
- `classification.json`
- `apart.json`
