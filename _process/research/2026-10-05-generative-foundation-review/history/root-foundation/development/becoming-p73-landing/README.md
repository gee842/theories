# P73–P75 landing package: learning, the learning correspondence and the root of wisdom

Ren, 12 October 2026, after the AI answered that none of the meta level, neural networks, cognition and the wisdom
about learning was completely explained, and proposed three steps: "please, fully complete, 我觉得理更像是对结构和变化的规律的建模
finish wisdom root, and resolve the undissolved"
([source](../../../../../../sources/15-codex-theory-conversations/2026-10-12-learning-wisdom-root-and-induction.md);
[directive register](../../../../../RESEARCH-DIRECTIVES.md)). Claimed on the [work board](../../../../../BECOMING-WORKBOARD.md)
as P73–P75 by the session "Meta-level explanation completeness". 理 is read as Ren reads it, the modeling of the laws
of structure and of change; every other reading is the AI's, pending Ren. Names carrying "unrefuted" mark a double
negation, following Ren's word through the integrator (12 October: the names stand for now, as long as the proof has
the exact meaning).

| Item | Module | Layer | Imports | Records |
|---|---|---|---|---|
| P73 learning: induction, generalization, training, the meta level | `Becoming.Learning` (core) | L4 | `Mechanism` (P66), `Selection` (P64) | learning-by-refutation, generalization-through-lumping (F11) |
| P74 the acquisition chain and the connectionist models as instances | `LearningCorrespondence` (periphery, Lean 4.30.0-rc2 + Mathlib) | periphery | `Becoming.Learning`, `CompositionalAcquisition`, `UpdaterConsequences` | in generalization-through-lumping |
| P75 the root of wisdom as far as Part I reaches | no Lean | — | — | wisdom-root-part-one (F11, argument, reviewed-scoped on the author's counterreview); wisdom-root and five records advanced |

No existing module changes. The root module gains one import, and the checker gains `Becoming.Learning` in `CORE`
with one scope sentence. `CorrectionInquiry` imports the root `Becoming`, so its checker reruns after the core run.

## Verified in scratch

Against main with P64–P68 landed (bca9695b; the five modules byte-identical to the package they came from):

- `Becoming.Learning` with `becoming/scratch_build.py` (the checker's 4.29.1 command, step keys and cache): no
  error or warning; the checker's parser lists 112 declarations (75 theorems), every axiom report empty. No `sorry`,
  `axiom`, `Classical`, `native_decide`, `omega` or `simp`.
- `LearningCorrespondence` with Lean 4.30.0-rc2 and Mathlib ea11ccc0, its closure from main with this Learning:
  19 declarations (15 theorems). The six acquisition declarations (`Uniform`, `encounters`, `acquire_exact`,
  `agree_at`, `uniform_determines`, `nonuniform_not_determined`) have empty reports; the network ones report only
  `propext`, `Classical.choice`, `Quot.sound`. The module keeps a file-level `noncomputable section` with no `end`,
  since the declaration scanner reads neither `noncomputable section` nor `noncomputable def`.
- Docstring correction (Learning a73c889e → 85798a66, comments only, rebuilt with `scratch_build.py`: 75 theorems /
  112 declarations, every report empty). Reviewing P83 showed that the old docstrings of the module bullet, the
  readings, `stable_unrefuted` and `rest_unrefuted` said the rest step is "fixed by no finite part of the course",
  which is false on a lasso course (its first i + q + 1 values fix it). They now say the step is not stated here,
  and that the learner's record never shows that it has come to rest (`no_record_fixes_next_finite`). The study
  and the records say the same, and that P83's two-period lemma appears to bound the step (an unchecked sketch,
  left to P83).
- Rename under P58c (Ren, 12 October, "agree with you": a statement of non-recurrence alone is named
  `…_not_recurring`): `refutations_not_unbounded` → `refutations_not_recurring`, statement unchanged (85798a66 →
  b5d869ba). The double negations `rest_unrefuted`, `held_rest_unrefuted` and `stable_unrefuted` are P58c's form (b)
  and keep "unrefuted". Rebuilt against main at 5c3b011b (P58b landed): 75 theorems / 112 declarations, every report
  empty, no warnings.

## Landed

In a worktree of main, after P69 (da8f75a7, §91), rebased onto 5359086d before the copy (the commits between touched
only the board and other packages' folders):

- consolidated receipt 20261012T012916.201078Z: passed, `Becoming.Learning` 75 theorems, 2970 theorems and 4334
  declaration audits over 57 package modules (core closure 59), every core axiom report empty, 12 Lean steps run;
- `CorrectionInquiry` receipt 20261012T013048.258651Z: passed (it imports the root);
- learning-bridge receipt 20261012T014649.248714Z: passed, 15 theorems / 19 declarations, the six acquisition
  declarations empty, the network ones only Mathlib's three standard axioms, 42 inherited modules;
- decidability inventory regenerated (`inventory_edit.py`): 153 statements depending on decidedness (63 count, 90
  built by deciding: 19 through the learner, 1 through `swapTo`), 88 proof-only (51 find, 25 tell same from
  different, 8, 3, 1); `eq_of_not_refuted` became visible once the skip list was narrowed; P80's `inventory_edit.py`
  and `zero_count.py` were run on the result in scratch and still apply;
- study §92 (P73, P74) and §93 (P75); records learning-by-refutation, generalization-through-lumping,
  wisdom-root-part-one; six advanced; 78 re-pointed; the two chapters' reading entries reread against this
  landing's diff and their hashes refreshed (`reading_entries.py`);
- `research.py check`, the Lean and reading catalogue checks and the session map check passed; the generative-chain
  check reports the same five unversioned-source errors as main without this landing; links on added lines: 391,
  none bad.

`land.sh` reruns every step after the checkers.

## Contents

- `lean/Becoming/Learning.lean` (sha256 b5d869ba…; a73c889e before the docstring correction and the rename below): to `experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/`.
- `periphery/LearningCorrespondence.lean` (15409ee4…) and `periphery/check_learning_correspondence.py`: to
  `…/lean/universal-ethics/evolution-connectionism/`. The checker follows `check_correction_inquiry.py`; it parses
  each declaration's axiom report, allows only Mathlib's three standard axioms and requires empty reports for the six
  acquisition declarations.
- `root_edits.py`: `core` adds the import, docstring bullet, `CORE` entry and scope sentence; `readmes` adds the
  spine row, the import note and the periphery ring entry to `becoming/README.md`, and the bridge paragraph to the
  evolution-connectionism README.
- `docs/study/p73_{zh,en}.md`, `docs/study/p75_{zh,en}.md`: the two study sections (P73 with P74, then P75) and their
  English summary entries, with placeholders.
- `docs/chapter.py`: edits to the canonical chapter (the learning paragraph before Knowledge; Ren's reading of 理 in
  place of the AI's; Part I stated whole; the open-hypotheses bullets; the status rows for the wisdom root and for
  learning; the empirical-correspondence bullets; the spine row; the glossary).
- `docs/cognition.py`: edits to `COGNITION-LEARNING-AND-EVOLUTION.md` (a §2 subsection, two disposition rows, a
  note in §4).
- `docs/plan_rows.md`: the unification plan's three rows and bullets.
- `docs/records/*.json`: the reviewed text of the three new records; `docs/advances.json`: next_delta, replacements
  and history for wisdom-root, testing-within-registration, experiment-needs-return, projection-carrying-a-law,
  selection-through-registration and scientific-inquiry-foundation, each with the text it was written against.
- `apply_docs.py`, `make_records.py`, `repoint.py`.
- `inventory_edit.py`: `edit` classifies Learning's decidability uses in `DECIDABILITY-INVENTORY.py` (the learner and
  `swapTo` as constructions in statements; `determines_lumped_iff` finds, four proofs tell values or inputs apart) and
  narrows the Lean side's skip list, which dropped every name beginning with `eq_` and so hid
  `Learning.eq_of_not_refuted` (it now skips only `eq_def`, `eq_unfold` and `eq_` followed by digits; no other core
  declaration so far named `eq_…` takes a decidability family); `zero` updates the zero-premise plan's sentence from the
  regenerated page, the counting/construction split included, and says that the learner's rest theorems depend on it.
- `reading_entries.py`: the reading-catalogue entries of the two edited chapters (one sentence added to the cognition
  entry; both hashes refreshed only where the entry was current with the chapter at HEAD).
- `land.sh W S PLAN_ZH_AFTER PLAN_EN_AFTER`: every step after the three checkers, on P80's pattern.

## Landing steps

In queue order, after P69 (the integrator's order: P58b, P69, P73, then P70–P72):

1. Copy the module, the bridge and its checker; `python3 -B root_edits.py ROOT core`.
2. Run the consolidated checker once; then `check_correction_inquiry.py` (it imports the root); then
   `check_learning_correspondence.py` (with a longer `LEAN_TIMEOUT`, e.g. 3600, on a loaded machine). After the core
   run: `python3 -B inventory_edit.py ROOT edit`, `python3 -B DECIDABILITY-INVENTORY.py` (in the root-foundation
   folder), `python3 -B inventory_edit.py ROOT zero`.
3. `python3 -B apply_docs.py ROOT S PLAN_ZH_AFTER PLAN_EN_AFTER`. `S` is the next free study section (P73 takes `S`,
   P75 `S+1`). The plan prefixes are the row and bullet these go after: after P69 lands, P69's; on bca9695b,
   `'| P67 吸引'` and `'- **P67:**'`.
4. `python3 -B make_records.py ROOT REVIEWED_AT_UTC S`, then `python3 -B repoint.py ROOT BASE`, then
   `python3 -B root_edits.py ROOT readmes`.
5. `make research-render`, `make research-check`; commit only these changes; mark the board.

## Dry run (before landing)

On a worktree of main at 6b9514a6 (P58b landed as §90, P69 not yet), with `S` = 91, the plan prefixes
`'| P58b P58 的确切名称'` and `'- **P58b:**'`, and stand-in receipts (the core receipt adds Learning, 75 theorems by the
parser, and the root's new hash; the periphery receipts carry the same hashes). Every anchor matched once. The
records script wrote the three records and advanced the six; repoint rewrote 77 records and left no stale reference.
`make research-render` and `make research-check` passed with no error and no drift. The links in the inserted text
resolve, anchors included (166 links in 94 files).

The bridge checker itself ran in that worktree (with Learning a73c889e) against the stand-in core receipt. It passed:
15 theorems / 19 declarations, the six acquisition declarations empty, the rest only Mathlib's standard axioms, 42
inherited modules matching passed receipts. On the loaded machine the axiom audit needed `LEAN_TIMEOUT=3600` (the
default 900 s timed out), so run the bridge checker at landing with a longer `LEAN_TIMEOUT`.

## Overlaps, settled with their owners

- `Learning.goAlike_iff_lumped` is, with `Lumped` unfolded, P70's `Law.goAlike_process_iff` (`Becoming.Description`), with the
  same proof; both were written independently. P73 lands first, so P70's package restates its theorem as this one's
  instance (`learning_patch.py`, checked by its owner against a73c889e; to be rebuilt against b5d869ba; the names it uses are unchanged), name and statement kept on both sides.
- The diagonal course is the learner's form of P71's gap (`Becoming.Diagonal`): a different object of the same form.
  P71's study section notes the relation; there is no instance theorem.
- `MakesSense` is P69's (`Becoming.Unfolding`); Learning does not use it.
