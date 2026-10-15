# Landing package: loops within what a law reads, and the break (P124)

回路在律所读之内，与断裂（P124）的落地包。内容在分支 `p124-thresholds`，已在其上应用；本目录保存写入它们的脚本，以便在移动的基上重做。

On 16 October 2026, asked whether to start joining loop formation with `Becoming.Runaway`'s policies, the item left open in how-a-carried-difference-grows, how-loops-form and runaway-distance-unregistered and in the chapter's reading of `Becoming.Loops`, Ren wrote "please" ([source](../../../../../../sources/15-codex-theory-conversations/2026-10-16-loop-formation-and-policies-go.md)). Overall progress and claims [6a12d4] claimed it on the work board as P124.

## Content

- `Becoming/Thresholds.lean`, a new core module in L4, imports `Becoming.Closing` and `Becoming.Runaway`: 38 theorems, 45 declarations. No existing module is changed. Scratch build on main c0fbc84b: empty axiom reports, no warnings; the root `Becoming` compiles with it. No decision on conditions is used: the stock is marked by a given `mark`, and only numbers are compared (`Thresholds.le_of_not_lt`).
- Decidability inventory: a scratch run, with only the receipt check skipped, reports 0 unused rows and no row for the new module. `DECIDABILITY-INVENTORY.py` is not edited.
- `apply_docs.py W [SECTION]`: the root import and bullet, the checker's core list and scope, the Lean README row and within-layer imports, the chapter (§2 paragraph, "Part I stated whole" item, §8 further proof, §9 row, two glossary rows) and the study section with its English paragraph (`study.md`, `study-en.md`; section 157 by default).
- `make_record.py ROOT [SECTION]`: the new schema-2 record loops-within-what-a-law-reads (laws partition every declaration; reused declarations checked; "receipt bound at landing"), and one paired note each in how-a-carried-difference-grows, how-loops-form and runaway-distance-unregistered. Run it after `apply_docs.py`.

## Order

1. Base: main. If the base moved, take `Thresholds.lean` and rerun `apply_docs.py W`, then `make_record.py W`, on the fresh base (renumber with SECTION if P123 lands first).
2. Landing (integrator): the core checker (only Thresholds and the root are new steps); the decidability page regenerated on the checked bytes (no new rows); chapter §9 and Lean README totals from the receipt; bind the receipt to the new record; rehash the study and chapter references this changes; `research.py render`, the chain review, `research.py check`, `make research-test`.
