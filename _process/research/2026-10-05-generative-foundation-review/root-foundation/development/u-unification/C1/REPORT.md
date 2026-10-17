# Batch C1 report (agent, 17 October 2026)

Saved by the integrator from the agent's final message.

**Apart count for the nine source modules: 132 → 9** (roots 64 → 9). Measured by `apart_roots.py` with the tree overlaid, the whole spine goes from 1,019 to 894 apart. None of the 68 new theorems stands apart.

**Decisions for you:**
1. **Three new readings** to adopt, rename or move: `couplingProcess` and `retraceProcess` (in CouplingTraces) and `flowUnder` (in StrengthFlows, which may belong in `Runs` as `ExchangeLaw.flowUnder`). Also `chain_iff_trace`, a general process lemma other batches may need, which could go in `Frame` or `Unfolding`.
2. **One-way joins.** `part_policy`, `rest_policy` and `both_one_move` give only the forward direction of the source iffs; a run fixes `form` only at configurations it reaches. If one-way joins are unwanted, classify those three roots as `support`. `returns_trace` is also one-way.
3. **Partial joins.** `draw_loop` and `standing_no_loop_traces` restate only the loop conjuncts of their roots; the law-level conjuncts feed the base but are not restated on it.
4. **Thin joins** you may prefer to classify instead: `alike_of_readsAt_all`, `square_no_finite_strength`, `measure_alike_read`.

---

# U batch C1: report

17 October 2026. Source modules: Coupling, Propagation, Loops, Closing, Thresholds, Frequency, Remainder, Routes, Observation. Nothing was committed, landed or checked with `check_becoming.py`, and no existing file was edited.

## Modules written (all build clean, every declaration has an empty axiom report)

| Module | Theorems | Reading used |
|---|---|---|
| `Becoming/MoveRuns.lean` | 14 | A run's configurations and moves (`r.state`, `r.act`); the runs of a coupled whole (`Run.part`, `Run.rest`); runs of `closedBy` of the standard model of a course; witnesses as runs of the law a history shows (`Shown.run`). |
| `Becoming/CouplingTraces.lean` | 34 | New: `couplingProcess cs part k present : Process C Nat` steps from `d` to `c` by the step `u` at which a coupling acts. Exactness: `couples_iff_step`, `upstream_iff_reach` (Upstream = Reach), `onLoop_iff_trace` (a loop is a trace of one step or more back to its condition). New: `retraceProcess : Process (Nat × C) Nat` steps from the level of `c` at `t` back to the level a coupling acting before `t` reads. Exactness: `coupledIntoBy_iff_trace` (a chain in time order of `j` couplings is a trace of `j` steps back). Generic lemma `chain_iff_trace`: a sequence whose successive members are steps of a process is a trace of it, for every process. Also uses `FormedLoops.scheduleWorld` and `onsetWorld`. |
| `Becoming/StrengthFlows.lean` | 13 | New: `flowUnder law present l : Flow F C`, the flow a law gives under a level history. Exactness: `course_eq_flowUnder` (the course is the flow under the generated levels, rfl) and `flowUnder_follows`. Also flows following a law under their webs' levels (`Flow.Follows`), the worlds of two acts (`TwoActs`, `actWorld`) and `carriedWorld`. |
| `Becoming/RouteTraces.lean` | 7 | Traces of a process whose steps the counting weights read (`counting_transfer_iff`), and the self-loop's world (`FormedLoops.scheduleWorld`). |

## Roots covered (root → join theorem)

- **Coupling** (all 14 joined, in MoveRuns):
  - lumped_id → coupled_formed
  - lumped_of_finer → formed_of_finer
  - lumped_const_iff → formed_const_iff
  - partForms_iff → part_policy
  - restForms_iff → rest_policy
  - partForms_and_restForms_iff → both_one_move
  - rest_differs_of_varied → rest_differs
  - lumped_iff_singleValued → formed_iff_singleValued
  - reading_le → reading_le_run
  - lumped_upto_iff → formed_upto_iff
  - no_policy_upto_iff → MoveRuns.no_policy_upto_iff
  - ExchangeLaw.ofMoves_lumped_stage → ofMoves_formed_stage
  - Still.driven → still_driven
  - Parity.neither_alone → parity_neither_alone
- **Propagation** (6 of 9 joined, in StrengthFlows):
  - Nonanticipating.respondsWithin_later → exchange_alike_later
  - exchangeGap_le_shares → exchangeGap_le_shares_flows
  - sensitive_iff_strength → sensitive_iff_flows (with `respondsWithin_zero_iff_flows`)
  - RespondsWithin.mono → gap_le_carried_mono_worlds
  - Square.not_respondsWithin → square_no_finite_strength
  - carried_zero → carriedWorld_start
- **Loops** (both joined, in RouteTraces):
  - geomBound_eq → selfLoopWorld_geomBound
  - geomBound_mono → selfLoopWorld_mono
- **Closing** (all 5 joined, in CouplingTraces):
  - onLoop_iff_formed → loop_iff_formed
  - upstream_iff_formed → reach_iff_formed
  - forms_by_closing → loop_forms_by_closing
  - Onset.forms → onset_forms
  - Onset.not_formed → onset_not_formed
- **Thresholds** (all 5 joined):
  - In CouplingTraces:
    - onLoop_succ_reads → loop_succ_reads
    - self_coupling_reads → self_step_reads
    - ReadsBelow.standing_no_loop → standing_no_loop_traces
    - Draw.forms_at_break → draw_loop
  - In StrengthFlows:
    - Nonanticipating.readsAt_all → alike_of_readsAt_all
- **Frequency** (7 of 8 joined):
  - In CouplingTraces:
    - SelfLoop.couplesAt_iff → selfLoop_retrace_iff
    - SelfLoop.returns → selfLoop_returns (through `returns_trace`)
    - StopsBy.not_recurs → stops_not_recurs
    - settled_every_iff → settled_every_iff_steps (this brings the whole settling chain onto the base: settled_of_each, recurs_or_stops, settled_iff_recursOrStops, lpo_of_settled, Rows, First)
    - SelfLoop.always → scheduleWorld_always
    - SelfLoop.onset → scheduleWorld_onset
  - In RouteTraces:
    - count_le → scheduleWorld_le_always
- **Remainder** (6 of 7 joined, in CouplingTraces):
  - CoupledIntoBy.later → retrace_later
  - CoupledIntoBy.shorten → retrace_shorten
  - couplingRecurs_iff → recurs_iff_steps (with `settled_iff_steps`)
  - settledFrom_zero_of_always → settled_zero_of_always
  - Loops.Once.no_chain_of_two → once_no_retrace_of_two
  - Loops.Once.settled → once_settled
- **Routes** (3 of 6 joined, in RouteTraces):
  - counting_within_le_transfer → within_trace
  - Weights.Hom.within → possibility_within_trace
  - Routes.SelfLoop.within_exact → selfLoopWorld_full_order
- **Observation** (7 of 8 joined):
  - In CouplingTraces:
    - route_forms_by_closing → CouplingTraces.route_forms_by_closing
    - upstream_readCouplings → reach_readCouplings
    - Measure.downstream_before → measure_reach_before
    - Measure.no_loop_before → measure_no_loop_before
    - Measure.loop_at → measure_loop_at
  - In StrengthFlows:
    - Measure.readsInto → measure_alike_read
    - ReadsInto.restrict → gap_le_carried_into_worlds

Still apart, classified in `classification.json`:
- **support:** gap_le_iff, Propagation.distinct_two, Propagation.every_two, responded_zero, Routes.cond_zero_mul, counting_within_le_succ, routeSum_mono
- **logical-strength:** RecursOrStops.lpo
- **model-witness:** Observation.Measure.listed

## Apart count for the source modules

| Module | Before | After |
|---|---|---|
| Coupling | 19 | 0 |
| Propagation | 13 | 3 |
| Loops | 2 | 0 |
| Closing | 7 | 0 |
| Thresholds | 22 | 0 |
| Frequency | 37 | 1 |
| Remainder | 9 | 1 |
| Routes | 9 | 3 |
| Observation | 14 | 1 |
| **Total** | **132** | **9** |

Roots go from 64 to 9. Across the whole spine, apart goes from 1,019 to 894 and roots from 486 to 431; two Readout theorems also came onto the base through Coupling. None of the 68 new theorems stands apart.

## Problems in the source modules

- No source theorem looks wrong.
- `Loops.Once.no_chain_of_two`, `none_from_one` and `settled` sit in `Remainder.lean` under the namespace `Loops.Once`, so their names point to the wrong file.
- `Frequency.SelfLoop.always` and `SelfLoop.onset` are rfl identities between two witness arrays. I joined them as equalities of the worlds those arrays carry.
- In this toolchain `Nat.succ_ne_zero` brings in `propext`; `Nat.noConfusion h` is clean. Other batches may hit this.

## Decisions for the integrator

1. **New readings.** `couplingProcess` and `retraceProcess` (the retrace process is the support relation of Routes' route steps, without the source point), and `flowUnder` (natural home perhaps `Becoming.Runs` as `ExchangeLaw.flowUnder`). `chain_iff_trace` is a general process lemma that may belong in `Frame` or `Unfolding`.
2. **One-way joins.** `part_policy`, `rest_policy` and `both_one_move` give only the forward direction of the source iffs about `form`, because a run fixes `form` only at the configurations it reaches. If one-way joins are unwanted, classify partForms_iff, restForms_iff and partForms_and_restForms_iff as `support`. `returns_trace` is also one-way; `coupledIntoBy_iff_trace` is the exact form for chains in time order.
3. **Partial joins.** `draw_loop` restates only the third conjunct of `Draw.forms_at_break`, and `standing_no_loop_traces` only the second and third of `standing_no_loop`. Their law-level conjuncts feed the base but are not restated on it.
4. **Thin joins** that may be better classified: `alike_of_readsAt_all` (close to what being a law of what has stood already says), `square_no_finite_strength` (the root unfolded on `flowUnder`), `measure_alike_read`.
5. **Housekeeping.** `scratch_build.py` left `C1/.build/`, and `C1/apart.json` is the measurement output. Neither is a deliverable.

---

Files are in `/Users/ren/theories/_process/research/2026-10-05-generative-foundation-review/root-foundation/development/u-unification/C1`:
- `Becoming/MoveRuns.lean`
- `Becoming/CouplingTraces.lean`
- `Becoming/StrengthFlows.lean`
- `Becoming/RouteTraces.lean`
- `classification.json`
