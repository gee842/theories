# P79 landing package: the laws of one step are all the laws of one step

Under Ren's "move towards 100%" of 12 October 2026 ([source](../../../../../../sources/15-codex-theory-conversations/2026-10-12-move-towards-100.md)), the session "Current math core" [1c3084] claimed P79 on the [work board](../../../../../BECOMING-WORKBOARD.md): completeness in the strong sense for the laws of one step (`Becoming.Locality`, P48), as `tally_iff_counted` gave it for counting. Its extension P79b adds the givers, capacity and activity to the pattern, and families chosen step by step. Opus subagents of the session built the module in two rounds, and the session checked both; P79 and P79b land together as one module.

| Item | Module | Imports | Records |
|---|---|---|---|
| P79 + P79b one step | `Becoming.OneStep` | `Counting`, `Sampling` | laws-of-one-step-complete, one-step-missing-laws, runs-on-families-chosen-step-by-step (F01) |

No existing module changes.

## Verified in scratch

The subagent's `mk.sh` build against the session's scratch copy of the core: 379 constants, no warning, no axiom (the constructor injection lemmas Lean generates, `*.injEq`, report `propext` as in other modules and are not declarations the checker audits). Rebuilt 10-12 by `scratch_build.py` against main `66dc4450`: 118 theorems, 154 declarations, no axiom, no warning (P79 alone). With P79b (subagent's `mk.sh`: 872 constants): `scratch_build.py` against main reports 311 theorems and 401 declarations, no axiom, no warning; a text scan finds no name clash against the core, P69's `Unfolding` or the queued packages. P79b adds `Flow.CapacityAt`, `Flow.ActingAt`, `Flow.TakingAt` (one-step forms of the core's conditions, linked by `capacity_iff_at`, `acting_iff_at`, `taking_iff_at`) and two list lemmas at the top level (`total_steps_split`, `total_steps_shift`), which the integrator may move into the core.

## Not covered

- Counting active relata, or relata taking part without exchanging, would need activity decided.
- Capacity and activity are stated over one step, not over runs.
- Conditions covering only one side of a step are not treated for families chosen step by step.

No independent review yet.
