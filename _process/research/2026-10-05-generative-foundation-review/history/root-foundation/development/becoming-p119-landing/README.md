# Landing package: the open proofs of parting and counting (P119)

分开与计数的开放证明的落地说明。内容在分支 `p119-open-proofs`，基于 main `d84868b7`（I4b-4 落地之后）。

Ren, 16 October 2026: “take 2, and do the open proofs” ([source](../../../../../../sources/15-codex-theory-conversations/2026-10-16-finite-name-and-open-proofs.md)). Claimed on the work board as P119 by Current math core (fork) [8277f2]. P110 (“Overall progress and claims”) records “take 2”, the finite name read as an analogy. This package does not touch that reading. In identification-where-bounded it changes only `next_delta`, as agreed with P110.

## Content

One commit on branch `p119-open-proofs`. Existing declarations do not change; new theorems and definitions are added.

- **Lean.** Three core modules gain theorems. `scratch_build.py` on `d84868b7` compiled them and the root `Becoming` with its closure: every axiom report is empty, there are no warnings and no names clash, and all steps are stored in the shared cache.

  | Module | Theorems | Declarations |
  |---|---|---|
  | `Becoming/Parting.lean` | 18 → 43 | 27 → 62 |
  | `Becoming/Typicality.lean` | 32 → 43 | 44 → 56 |
  | `Becoming/Situations.lean` | 13 → 38 | 19 → 54 |

  - **Parting:**
    - the rest step 2(T + N) − 1 where runs part only before step T (`late_right`);
    - the converse: for listed, decided processes, the learner given the world is right at a step on every run exactly where no two runs part there (`worldLearner`, `world_right_iff`, `some_right_iff`);
    - built on `Lasting.Continues` (I4b-4): where a list of N holds every configuration, a course of N steps makes its start `Lasting.Unbounded`, with no decidability (`unbounded_of_continues`). Parting now imports `Becoming.Lasting` (L2).
  - **Typicality:** exponential concentration, the counting Chernoff bound (`concentrated`, `few_far_ahead`).
  - **Situations:**
    - any number of values through an event (`sum_event`, `event_typical`, `event_concentrated`, `event_count`);
    - counting per course for every process (`situations_take`, `situations_of_course_listed`);
    - counting by situations in any weights (`sum_finer_weights`);
    - signed weights as pairs of counts of situations (`signed_counts`, `cancels_situations`).
- **`Becoming.lean`:** the three module bullets are extended. Imports are unchanged; `Parting.lean` gains `import Becoming.Lasting`, and the Lean README's within-L4 imports say so.
- **`check_becoming.py`:** the three scope paragraphs are extended. The core list is unchanged.
- **The Lean README:** the three L4 rows are extended in both languages.
- **The theory chapter:**
  - a new paragraph pair, "the open proofs of parting and counting", after "weights count situations", plus one sentence in that pair;
  - the theory stated in full: two bullets in each language, and the bound item;
  - §8: the two status rows, and the open item "When the course branches";
  - §9: three spine rows (43, 43, 38);
  - the glossary: one row, the learner given the world.
- **The study:** section 150, provisional, and an English paragraph at the end. The integrator lands I4b-4 as §146 and P110–P112 as §147–§149; renumber if needed.
- **`DECIDABILITY-INVENTORY.py`:** new definitions are classified:
  - `Parting.candidates`, `live`, `firstLive` and `worldLearner` go under a new kind, `reach`, which decides steps and tells registered values apart;
  - `Situations.occ` goes under `same`;
  - among proof-only theorems, `Parting.unparted_at_of_late` and `late_statesBelow` go under `same`, and `some_right_iff` under `reach`.

  A scratch run on the branch bytes, with only the receipt check skipped, reports 0 unused rows.
- **Records:**
  - **identification-where-runs-part:** three laws. The statement no longer says "settled only when taken", the AI's withdrawn reading. The first hypothesis, `does_not_show` (the converse and the rest step are proved) and `next_delta` are rewritten.
  - **typicality-by-counting:** one law, and the hypotheses, the scope item and `next_delta` rewritten.
  - **weights-count-situations:** three laws, and the hypotheses, `does_not_show` and `next_delta` rewritten. losses-of-the-sum-over-histories moves from related to dependencies, since `Interference.weight` and `cancels` are reused.
  - In all three, the Parting, Typicality and Situations references are rehashed with the new declarations listed, the study and chapter references are rehashed, the new source joins as provenance, `validation_scope` reads "receipt bound at landing", and a history note is added.
  - **identification-where-bounded:** `next_delta` only. Both judgments it asked of Ren are now made, so it names the proof left. One history note.

## Landing

`W` is the landing checkout.

1. Renumber study §150 if it is taken. Update:
   - the heading;
   - the chapter's link (`#150-…`);
   - the English paragraph;
   - the three records' `validation_scope` and history.
2. Run the core checker, `check_becoming.py`. The new steps are Parting, Typicality, Situations and the root. All passed scratch builds stored in the shared cache.
3. Regenerate the decidability page on the checked bytes. Then update the chapter's §9 totals and the Lean README totals from the receipt.
4. Rebind the receipt to identification-where-runs-part (Parting), typicality-by-counting (Typicality, Parting) and weights-count-situations (Situations, Typicality).
5. Rehash the study and chapter references this landing changed, with one reconciliation note per changed record.
6. Run `research.py render`, the generativity-chain review of the changed sources, and the Lean and reading catalogues. Then run `research.py check` and `make research-test`.

What `research.py check` reports on the branch:

- Five errors, all expected before binding, all "receipt does not bind the reviewed proof source":
  - identification-where-runs-part: once (Parting);
  - typicality-by-counting: twice (Typicality, Parting);
  - weights-count-situations: twice (Situations, Typicality).

  `make research-test` fails on these same five (two tests).
- Chapter drift in the records scoped to §3, §8, §9 and "Part I stated whole". Step 5 reconciles it.

The style lint finds nothing new in the four records. Nothing here edits the board.
