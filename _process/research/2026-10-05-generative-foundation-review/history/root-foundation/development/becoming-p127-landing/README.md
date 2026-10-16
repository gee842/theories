# Landing package: where a run goes on (P127)

运行在何处延续的落地包。内容在分支 `p127-onward`；本目录保存内容的文本与写入它们的脚本。

[returning-where-the-course-branches](../../../../../../theories/becoming/results/records/returning-where-the-course-branches.md) (P81, `Becoming.Branching`) has one next step: “state the laws along runs for every configuration that can move without a choice (for instance for finite, decidable processes)”. [lifting-where-branching-is-finite](../../../../../../theories/becoming/results/records/lifting-where-branching-is-finite.md) (`Becoming.Lasting`) lists “a run without a selection (the boundary of dependent choice)”. The chapter's §8 lists, under when the course branches, “whether a run from every configuration that can move needs more than a choice”. This answers all three. It serves Ren's goal of 12 October 2026, “move towards 100% … don't stop until we are 100%” ([source](../../../../../../sources/15-codex-theory-conversations/2026-10-12-move-towards-100.md)). Current math core (fork 2) claimed this on the work board as P127.

## Content

One commit on branch `p127-onward`, on main `83081fe1`, after P126 (`Becoming.Tail`, study §160) landed.

- `Becoming/Onward.lean` is a new core module.
  - It sits in L4 and imports `Becoming.Parting`. It changes no existing module.
  - It has 28 theorems and 40 declarations.
  - `scratch_build.py` on `83081fe1` gives every axiom report empty, with no warnings.
  - The root `Becoming` compiles with its 126-module closure, so no names clash.
  - Both steps are stored in the shared cache.

  The module covers five parts:
  - **Within finitely many configurations, a run is a course into a return.** A course as long as the list of configurations repeats one, which returns (`returning_of_continues`); round the return, preceded by the course, is a run (`run_of_returning`, `run_of_reach`, `run_of_trace`). So a run starts exactly where a course as long as the list does, exactly where courses of every length do, and exactly where a course leads to a return (`run_iff_continues`, `run_iff_unbounded`, `run_iff_returning`). No decision and no selection is used. Where the successors are listed, whether a run starts is decided (`run_decided`). Where branching is infinite, courses of every length give no run (`fan_no_run`).
  - **A family that keeps moving** (`KeepsMoving`, `within`): within finitely many configurations a run starts at each member and stays in the family (`KeepsMoving.run`).
  - **The laws along runs, with no run given.** These are `Branching`'s `Lossless.returns`, `Lossless.no_rise`, `rise_not_lossless` and `Lossless.unlisted`, restated for every configuration from which the process can keep moving: `lossless_returns_iff`, `KeepsMoving.returns`, `lossless_no_rise`, `rise_needs_merge`, `lossless_unlisted`.
  - **Searched moves.** Where a test recognizes, among enumerated moves, a step that stays in the family (`Finds`), a run is built as data by search through accessibility (`search`, `searchFrom`, `acc_below`, `searchedRun`). This uses no axiom and no selection, and it compiles. Testing each enumerated move is such a test where the steps and the family are decided (`decidedTest`, `decidedTest_finds`).
  - **In general.** Asked of every process, a run from every member of every family that keeps moving is exactly dependent choice (`DependentSelection`, `runs_iff_selection`).
- `apply_docs.py` makes the following edits. It reads the bullet, scope entry, rows, paragraphs and clauses from `docs.json`, which `make_docs_json.py` writes.
  - `Becoming.lean`: the import after `Becoming.Parting`, and the module bullet after Parting's.
  - `check_becoming.py`: `Becoming.Onward` in the core list after `Becoming.Parting`, and a scope entry after Tail's.
  - The Lean README: one L4 row after Parting's, and the within-layer imports.
  - The theory chapter:
    - §1, the paragraph pair on when the course branches: in place of “not derived: a run from every configuration that can move (a choice)”, where a run goes on.
    - A paragraph pair "Where a run goes on (Part I)" after those paragraphs.
    - "Part I stated whole": one item after the item on returning where the course branches.
    - §8, the status row of when the course branches: the result.
    - §8, the further proofs under when the course branches: the run is given.
    - §9: one L4 row (28 theorems).
    - The glossary: rows "keeps moving (a family)" and "dependent choice" after "run".
- The study gains a section and its English paragraph (`study.md`, `study-en.md`; `apply_study.py W [N]`).
  - The section is numbered 161 provisionally. Main holds §160 (P126).
  - `apply_study.py` renumbers the heading to N and refuses a number already taken.
- `apply_inventory.py` edits `DECIDABILITY-INVENTORY.py`.
  - One definition takes decisions: the test of each enumerated move (`Onward.decidedTest`), an indicator of a decided proposition (`indicate`). The statement mentioning it (`decidedTest_finds`) is classified through it.
  - `run_decided` proves a proposition decided and needs no classification.
  - A scratch run of the inventory on the branch bytes, with only the receipt check skipped, reports 0 unused rows.
  - Its totals: dependent statements 435 → 436; proof-only 241 (unchanged); definitions and theorems proving decidedness 145 → 146; decidability-taking definitions 116 → 117; `indicate` 49 → 50.
- Records:
  - `make_record.py ROOT [N]` writes the new schema-2 record where-a-run-goes-on.
    - Seven laws cover all 40 declarations.
    - Its proof references are hashed from the branch.
    - `proof_bindings` is empty, and the record reads "receipt bound at landing".
  - `update_records.py ROOT [N]` writes the paired notes:
    - returning-where-the-course-branches: its next step, now answered, becomes being drawn in within a bound, which its limitations name.
    - lifting-where-branching-is-finite: the item “a run without a selection” leaves its next step.
    - Both add the new record under related and gain one history note each. Statements, proofs, hypotheses, limitations and does_not_show are unchanged.

From main `83081fe1`, copy `Onward.lean` in. Then run `make_docs_json.py`, `apply_docs.py W`, `apply_study.py W N`, `apply_inventory.py W`, `update_records.py W N` and `make_record.py W N`, in that order, to write the content commit. Each script asserts the text it replaces, so a second run fails.

## Landing

`W` is the landing checkout.

1. If a landing before this one takes §161, rerun the kit on the new main with the next free N. `apply_study.py`, `update_records.py` and `make_record.py` take it as an argument.
2. Run the core checker, `check_becoming.py`. `Becoming.Onward` and the root are new steps, and both passed scratch builds stored in the shared cache.
3. Regenerate the decidability page on the checked bytes. Then update the chapter's §9 totals and the Lean README totals from the receipt.
4. Bind the receipt to where-a-run-goes-on, one binding per proof reference. Rehash the study and chapter references that this landing changed, with one reconciliation note per changed record.
5. Run `research.py render`, the generativity-chain review of the changed sources, and the Lean and reading catalogues. Then run `research.py check` and `make research-test`.

`research.py check --ids` on the three records, run on the branch, reports two errors. Both are expected before binding:
- "recorded-checked needs proof source and existing receipt";
- "recorded-checked needs a source hash binding in its existing receipt".

`make research-test` fails in the same two places before binding:
- `test_current_records_are_structurally_valid`;
- `test_drafts_validate_and_render`.

The other 99 tests pass.

Every other finding is chapter drift, which step 4 reconciles. It is scoped to the sections this changes (§1 and §8) and covers 18 records:
- continuous-time-as-tower, counts-exist-where-decided, determinacy-up-to-likeness, every-origin-passes-the-gate, how-loops-form, imbalance-as-relatum;
- laws-at-coarser-steps, laws-at-finer-units, lifting-where-branching-is-finite, necessarily-drawn-is-not-returning, orders-as-a-sum-over-histories, recurrence-without-decidedness;
- recurrence-without-premise, recurring-reference-revision, returning-where-the-course-branches, selection-through-a-model-of-the-options, what-a-finite-history-refutes, where-a-move-is-formed.

The lint finds nothing in the new record. Its 7 findings on returning-where-the-course-branches are the same as on main: lengths and round markers in its unchanged claim and validation scope.

Nothing here runs the checker, edits the board or commits.

## History

- 16 October 2026: claimed on the work board (`b7f909ae`) after P126 was handed over. The branch was moved to P126's landing (`83081fe1`) before any Lean was written.
- The first wording said that, where configurations are not bounded, each configuration being able to move "does not by itself give" a course without end. That is not proved; what is proved is that, asked of every process, it is exactly dependent choice. The readings now say only that.
- The first law of the record was split in two to stay within the lint's cap, and the statement was rephrased so it does not lead with a negation.
