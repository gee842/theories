# P78 landing package: the step index, re-founded

Under Ren's "move towards 100%" of 12 October 2026 ([source](../../../../../../sources/15-codex-theory-conversations/2026-10-12-move-towards-100.md)), the session "Current math core" [1c3084] claimed P78 on the [work board](../../../../../BECOMING-WORKBOARD.md): examine the zero-premise plan's commitment to a shared discrete index of steps. The module was built by an Opus subagent of the session and checked by the session.

| Item | Module | Imports | Records |
|---|---|---|---|
| P78 order | `Becoming.Order` | `Sampling` | only-the-order-of-change-registers, exchanges-commute-unless-joined (F01) |

No existing module changes.

## What it contains

- `lean/Becoming/Order.lean`: stuttering (idle steps) and commutation of consecutive independent exchanges, with the witnesses `Expansion`, `Lapse`, `Crossing` and `Arising`. Pure term mode.
- `docs/records/`, `docs/study/`: record drafts and the study section.

One change from the subagent's file: the reading's last sentence is softened to "would then be a partial order of exchanges … the converse that would make this exact is not shown", since the converse is not proved.

## Verified in scratch

The subagent's `mk.sh` build against the session's scratch copy of the core: 338 constants, no warning, no axiom. It must be rebuilt against main with `scratch_build.py` before landing; main has since renamed P58b's lemmas, none of which `Order` uses.

## Not shown

Removing idle steps as a construction; the converse (Foata normal form) and the partial order as an object; activity needing support, only active relata giving, and the counts of arising and ceasing along repeated commutation; invariance of Part II's predicates; continuous time. No independent review yet.
