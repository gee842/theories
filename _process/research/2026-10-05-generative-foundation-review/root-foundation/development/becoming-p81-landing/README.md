# P81 landing package: beyond determined laws

Under Ren's "move towards 100%" of 12 October 2026 ([source](../../../../../../sources/15-codex-theory-conversations/2026-10-12-move-towards-100.md)), the session "Current math core" [1c3084] claimed P81 on the [work board](../../../../../BECOMING-WORKBOARD.md): R6's and P67's laws for processes that are not determined, the theorems stated with `Determined` restated up to likeness, and Capture's rule region as an absorbing region. The module was built by an Opus subagent of the session and checked by the session.

| Item | Module | Imports | Records |
|---|---|---|---|
| P81 branching | `Becoming.Branching` | `Unfolding` (P69), `Attraction`, `Capture` | returning-where-the-course-branches, necessarily-drawn-is-not-returning, determinacy-up-to-likeness (F01) |

No existing module changes; `REGISTRATION.md` gives the root import, docstring bullet and `CORE` entry, and lists the theorems added to existing namespaces (`Run`, `Reach`, `Law`, `Twins`, `Coarse`, `Confound`, `Captured`). It lands after P69. On landing, the `next_delta`s of `attraction-is-not-returning`, `target-capture`, `recurrence-without-premise` and `configurations-alike-by-relation` are to be updated.

## Verified in scratch

The subagent's `mk.sh` build against the session's scratch core with P69's `Unfolding`: 308 constants, no warning, no axiom; also compiled together with P76's `Histories` with no name clash (P76's witness namespace is `Choosing`). Rebuilt 10-12 by `scratch_build.py` against main `66dc4450` with P69's `Unfolding` (byte-identical to the P69 landing): 119 theorems, 156 declarations, no axiom, no warning. For that build the five declarations written as `_root_.Becoming.Run.*` and `_root_.Becoming.Reach.of_dead_end` were moved into `namespace Run` and `namespace Reach` blocks (names and statements unchanged), since the checker's parser does not read `_root_`. No independent review yet.
