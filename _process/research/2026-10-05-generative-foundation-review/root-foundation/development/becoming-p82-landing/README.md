# P82 landing package: weighted histories

Ren, 12 October 2026, asked of the laws that are not determined whether one can still integrate over their many patterns and loops, as with Feynman diagrams (Ren wrote "Fermi's diagrams"), how accurately, with what losses, and whether the theory is sound ([source](../../../../../../sources/15-codex-theory-conversations/2026-10-12-move-towards-100.md)). The session "Current math core" [1c3084] claimed the answer as P82 on the [work board](../../../../../BECOMING-WORKBOARD.md). Reading the message as a go for P82 is the AI's reading.

| Item | Module | Layer | Imports | Records |
|---|---|---|---|---|
| P82 weighted histories | `Becoming.Weighted` | L3 | `Capture` (for `mul_assoc_nat`), `Resolution` (for `add_mul_split`) | sum-over-histories-exact, losses-of-the-sum-over-histories (F01) |

No existing module changes. The module does not depend on P69 or P76, so it can land in any slot after them.

## What it contains

`lean/Becoming/Weighted.lean`: 35 theorems by the checker's parser (165 constants with compiler auxiliaries). The weights come with their laws as fields of a structure (`Weights`), and each theorem holds for every weighting and listing it names.

- **Exact.** `Weights.sum_courses` (the sum over the courses of `n` steps is `n` steps of the transfer); `Weights.Hom.transfer` (a reading keeping the laws commutes with the sum).
- **Possibility is the core's relation.** `possibility_transfer_iff` (the possibility transfer is `Trace`); `support`, `counting_transfer_iff` (counting refines possibility without loss).
- **Integrating out.** `Weights.lumped_iff` (exact at every horizon exactly where exact at one step); `Lumping.loses`.
- **Losses.** `Weights.truncation`, `counting_truncation_le`; `signed`, `Interference.cancels`, `Interference.truncation_misleads`, `Interference.unseen`, `Interference.unseen_balanced`; `Memory.not_of_steps`, `Memory.of_kept`; `Loop.courses_double`.

## Verified in scratch

`scratch_build.py` against main `ea49a4c8` (the shared cache, 25 modules reused): no error or warning; the audit of `Becoming.Weighted` reports 34 theorems and 54 declarations with no axiom at that build (one theorem, `Interference.unseen_balanced`, added after it and rechecked with the session's `mk.sh`: 165 constants, no axiom). No `sorry`, `axiom`, `Classical`, `native_decide`, `simp`, `omega` or `funext`; signed counts are pairs, not integers, since the core's `Int` lemmas use `propext`.

## Docs

- `docs/records/`: two record drafts in the shape `make_records.py` completes (the P69 package's script, adapted at landing).
- `docs/study/`: the study section, zh and en.

The landing scripts are written when its slot comes, from the P69 package's. No independent review yet.
