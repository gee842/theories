# P76 landing package: law and history, and likeness, complete

Under Ren's "move towards 100%" of 12 October 2026 ([source](../../../../../../sources/15-codex-theory-conversations/2026-10-12-move-towards-100.md)), the session "Current math core" [1c3084] claimed P76 on the [work board](../../../../../BECOMING-WORKBOARD.md): completeness in the strong sense for law and history, and what tests fix of likeness.

| Item | Module | Imports | Records |
|---|---|---|---|
| P76 what histories fix | `Becoming.Histories` | `Unfolding` (P69) | histories-fix-law-up-to-dead-ends, tests-fix-likeness-where-determined (F01) |

No existing module changes. It lands after P69 (it imports `Becoming.Unfolding`) and, by the integrator's order, after P70–P72.

## What it contains

- `lean/Becoming/Histories.lean`: a family of histories is a law's exactly where it holds its splices (`family_iff`); histories fix a law up to its dead ends (`same_histories_iff`); with histories that stop no dead end remains (`same_finite_histories_iff`, `finite_family_iff`); tests fix likeness where branching is determined up to likeness (`alike_iff_sameTests`), and not otherwise (`Choosing.not_alike`).
- `docs/records/`, `docs/study/`: record drafts and the study section.

The witness namespace is `Choosing` (renamed from `Branching`, which P81's module `Becoming.Branching` also uses as a namespace).

## Verified in scratch

`mk.sh` against main `52feb7ef`'s core with P69's `Unfolding`: 162 constants, no warning, no axiom. Rebuilt 10-12 by `scratch_build.py` against main `66dc4450` with P69's `Unfolding` (byte-identical to the P69 landing): 27 theorems, 41 declarations, no axiom, no warning. No independent review yet.
