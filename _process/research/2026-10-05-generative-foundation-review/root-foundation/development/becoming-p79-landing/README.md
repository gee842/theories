# P79 landing package: the laws of one step are all the laws of one step

Under Ren's "move towards 100%" of 12 October 2026 ([source](../../../../../../sources/15-codex-theory-conversations/2026-10-12-move-towards-100.md)), the session "Current math core" [1c3084] claimed P79 on the [work board](../../../../../BECOMING-WORKBOARD.md): completeness in the strong sense for the laws of one step (`Becoming.Locality`, P48), as `tally_iff_counted` gave it for counting. The module was built by an Opus subagent of the session and checked by the session.

| Item | Module | Imports | Records |
|---|---|---|---|
| P79 one step | `Becoming.OneStep` | `Counting`, `Sampling` | laws-of-one-step-complete, one-step-missing-laws (F01) |

No existing module changes.

## Verified in scratch

The subagent's `mk.sh` build against the session's scratch copy of the core: 379 constants, no warning, no axiom (the constructor injection lemmas Lean generates, `*.injEq`, report `propext` as in other modules and are not declarations the checker audits). To be rebuilt against main with `scratch_build.py` before landing.

## Not covered

The number of relata giving to a family (`renewers` and its capacity law); runs on families chosen step by step. No independent review yet.
