# P78 landing package: the step index, re-founded (with P78b)

Under Ren's "move towards 100%" of 12 October 2026 ([source](../../../../../../sources/15-codex-theory-conversations/2026-10-12-move-towards-100.md)), the session "Current math core" [1c3084] claimed P78 and its extension P78b on the [work board](../../../../../BECOMING-WORKBOARD.md). The item examines the zero-premise plan's commitment to a shared discrete index of steps. Opus subagents of the session built the module in two rounds, and the session checked both.

| Item | Module | Imports | Records |
|---|---|---|---|
| P78 + P78b order | `Becoming.Order` | `Sampling` | only-the-order-of-change-registers, exchanges-commute-unless-joined, order-of-exchanges-is-the-invariant (F01) |

No existing module changes. P78 and P78b land together as one module.

## What it contains

`lean/Becoming/Order.lean` is pure term mode, with 266 theorems and 317 declarations by the checker's parser.
- **P78.** Stuttering, i.e. inserting idle steps, and the commutation of consecutive independent exchanges. Witnesses: `Expansion`, `Lapse`, `Crossing`, `Arising`.
- **P78b, the order as an object.** A footprint (`Footprinted`) gives the order of joined exchanges (`Precedes`), a strict partial order. Commuting unjoined exchanges keeps that order up to renumbering (`reorder_precedes`).
- **P78b, the converse.** Proved by constructive bubble sort, as Mazurkiewicz's theorem with footprints (`sorts_iff`, `converse`).
- **P78b, what carries along commutation.**
  - Along unjoined commutations, every premise carries (`reorder_premises`).
  - Along any `Reorders`, the counts of arising and ceasing carry (`Reorders.counts`).
  - Two witnesses show that joined commutations break activity needing support and only-active giving (`Crossing.reorders_joined`, `Arising.reorders_joined`).
- **P78b, removing idle steps.** This is a construction (`World.withoutIdle`). Every premise, the census, the totals and the counts are kept.

The reading's last sentence in P78 was softened while its converse was open. The converse is now proved, and it is cited in `order-of-exchanges-is-the-invariant`.

## Verified in scratch

`scratch_build.py` against main `66dc4450`: no error or warning, and the audit of `Becoming.Order` reports 266 theorems and 317 declarations with no axiom. The P78 part alone was 161 theorems and 191 declarations. A text scan found no name clash against the core, P69's `Unfolding` or the queued packages.

## Not shown

- The footprint is given; the least footprint would need being moved decided.
- No Foata normal form is built.
- The moving step of each read step is a hypothesis of the removal.
- The census along reorderings is not shown.
- Invariance of Part II's predicates is not shown.
- Continuous time is not covered.

No independent review yet.
