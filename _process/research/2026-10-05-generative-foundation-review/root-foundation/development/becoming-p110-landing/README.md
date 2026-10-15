# Landing package: readings decided on Ren's delegation (P110), where novelty's gain comes from (P111), when readings in context glue (P112)

依 Ren 的交托决定的读法、新的增益从哪里来、语境中的读法何时粘合的落地说明。内容在分支 `p110-frontier`，已合并 main `a5406334`（I4b-3 落地之后）。

Ren, 15 October 2026: “What's the best choices to make? please make best of your judgement, and push the frontier of completeness” ([source](../../../../../../sources/15-codex-theory-conversations/2026-10-15-delegated-choices.md)). Claimed on the work board as P110, P111 and P112 by the session “Overall progress and claims” (the rows name it [d8df1a]; it now runs as [6a12d4]).

## Content

Branch `p110-frontier`, merged with main `a5406334`. No statement, proof or name in an existing Lean module changes.

### P110: readings decided on the delegation

- [DELEGATED-CHOICES](../../DELEGATED-CHOICES.md): decisions D1–D39, each with its reasons and what would change it. Section 10 lists what is not within the delegation.
  - D34: Ren's own words decide two of its items. The first is “situationally” (Ren, 15 October). The second is the finite name: Ren took it as an analogy on 16 October (“take 2”).
  - D39: decides P115's readings, which P115's owner left “to Ren or this delegation”.
- The source entry [2026-10-15-delegated-choices](../../../../../../sources/15-codex-theory-conversations/2026-10-15-delegated-choices.md) and its line in the directive register.
- The theory chapter:
  - §8: “Ren's choices” becomes “Readings decided on Ren's delegation” and “What stays Ren's”. The identification item carries Ren's clarification of 16 October and the readings Ren took.
  - Readings formerly marked pending Ren elsewhere in the chapter now carry their decision numbers.
  - The D39 lines.
- Records: 101 records each gain one paired, dated history note (study section 146). Next steps asking for Ren's judgment on a decided reading are removed.
  - Specific rewrites are in `p110_specific.py`, with decision numbers in `DNUM`.
  - `EXCLUDE` keeps five records as they are. Their readings were posed after Ren's reply of 15 October, or after the delegation, or Ren took them: identification-where-runs-part, typicality-by-counting, every-origin-passes-the-gate, weights-count-situations, what-a-finite-history-refutes.
  - identification-where-bounded:
    - reading 1 is dropped (D34);
    - the finite name is labelled as Ren's (“take 2”);
    - the judgment on “situationally” with its qualification stays in next_delta for P119's owner, who holds that record's next step.
- Lean, comments only: `fold_docstrings.py` folds the decisions into the docstrings of 51 modules and the root.
  - For every file, the code outside comments is asserted unchanged.
  - Each changed paragraph is refilled at 100 columns, and the words are asserted unchanged.
  - `KEEP_LINES` leaves the lines naming `Parting` and `Typicality` alone, since P116's readings stay Ren's.
  - The Lean README's rows are folded the same way.

### P111: `Becoming.Gain`

- `Becoming/Gain.lean`: L3, imports `Becoming.Novelty`; 30 theorems, 35 declarations.
- New schema-2 record where-novelty-gain-comes-from. Its proof references are hashed from the branch, `proof_bindings` is empty, and it reads “receipt bound at landing”.
- related links added in returning-novelty-forgetting-on-levels, continued-change-needs-openness and where-a-move-is-formed, each with a dated note.

### P112: `Becoming.Gluing`

- `Becoming/Gluing.lean`: L3, imports `Becoming.Context` and `Becoming.Population`; 81 theorems, 113 declarations.
  - It also has one anonymous instance, `ParitySystem.instDecidableSupport`, which the audit does not list and the decidability inventory counts.
  - Contents: the parity law (an obstruction certificate, exactly one of two by elimination), the Bell-type bound m − 1 of m, Specker, CHSH and Mermin–Peres as instances, and the cycle law.
  - The cycle law (`Cycle.met_iff_even`) is the periphery's `CorrectionRelations.cycle_compatible_iff_even` in core form, as the I4b row leaves it with P112. The correspondence theorem between the two is not written; it is in the record's next_delta.
- New schema-2 record gluing-under-parity, with the same binding status as P111's.
- related links added in contextual-registration (whose next step this answers), unity-of-readings and separation-loses-the-relation.

### Shared

- `Becoming.lean`:
  - imports Gain and Gluing after `Becoming.Propagation`;
  - two L3 module bullets after Propagation's;
  - the folded bullets.
- `check_becoming.py`: both modules in the core list, before `Becoming.Relevance`.
- The Lean README: two L3 rows, and the within-layer imports in both languages.
- The study:
  - [sections 146, 147 and 148](../../BECOMING-RENEWAL-READING.md), before the English summary;
  - three English paragraphs at its end.
  - Main holds sections 142 to 145.
- `DECIDABILITY-INVENTORY.py`: Gluing's four elimination theorems use decided equality only in their proofs (`same`): `ParityConstraint.met_or_contradicts`, `ParitySystem.global_or_contradicts`, `ParitySystem.noGlobal_iff` and `ParitySystem.glues_iff`.
  - A scratch run on the branch bytes, with only the receipt check skipped, reports 0 unused rows.
  - Against main's page: proof-only rows 224 → 228; definitions and instances proving decidedness 136 → 137 (the instance above); the other classes unchanged.
- `scratch_build.py` on the merged tree:
  - 126 of 232 steps ran, because I4b-3 changed `Horizon` and everything after it recompiled; 106 were reused;
  - no warnings;
  - the audits of the 54 changed modules (the root included) are all empty;
  - every step is stored in the shared cache.

## P112's declaration names

- Top level (25): `addParity`, `oddOver`, `addParity_false`, `addParity_self`, `addParity_assoc`, `addParity_swap`, `addParity_and`, `addParity_solve`, `addParity_cancel`, `true_of_ne_false`, `cond_le_one`, `and_congr_of`, `oddOver_add`, `oddOver_and`, `oddOver_congr`, `oddOver_false`, `oddOver_swap`, `oddOver_map`, `image_of_mem_map`, `count_le_length`, `count_all`, `met_step`, `even_le_of_odd`, `ParityConstraint`, `ParitySystem`.
- `ParityConstraint` (13): `ParityConstraint.value`, `ParityConstraint.add`, `ParityConstraint.value_add`, `ParityConstraint.Contradicts`, `ParityConstraint.value_even`, `ParityConstraint.unmet_odd`, `ParityConstraint.eliminate`, `ParityConstraint.counts_after`, `ParityConstraint.eliminate_counts`, `ParityConstraint.met_after`, `ParityConstraint.pulled`, `ParityConstraint.pull_back`, `ParityConstraint.met_or_contradicts`.
- `ParitySystem` (18): `ParitySystem.constraint`, `ParitySystem.within`, `ParitySystem.value`, `ParitySystem.support`, `ParitySystem.met`, `ParitySystem.Contradicts`, `ParitySystem.local_`, `ParitySystem.contradicts_iff`, `ParitySystem.unmet_odd`, `ParitySystem.unmet_of_contradicts`, `ParitySystem.contradicts_noGlobal`, `ParitySystem.met_le`, `ParitySystem.mixture_le`, `ParitySystem.indexed_met`, `ParitySystem.lift_selection`, `ParitySystem.global_or_contradicts`, `ParitySystem.noGlobal_iff`, `ParitySystem.glues_iff`.
- `Specker` (9): `Specker.paritySystem`, `Specker.two_iff`, `Specker.two_iff_swap`, `Specker.support_iff`, `Specker.openings`, `Specker.openings_contradict`, `Specker.noGlobal_of_contradiction`, `Specker.mixture_le`, `Specker.indexed_met`.
- `CHSH` (12): `CHSH.Outcome`, `CHSH.outcomes`, `CHSH.same`, `CHSH.paritySystem`, `CHSH.two_iff`, `CHSH.support_iff`, `CHSH.pairs`, `CHSH.pairs_contradict`, `CHSH.mixture_le`, `CHSH.inPair`, `CHSH.inPair_support`, `CHSH.indexed_met`.
- `Square` (14): `Square.cells`, `Square.counts`, `Square.paritySystem`, `Square.lines`, `Square.three_iff`, `Square.not_beyond`, `Square.support_iff`, `Square.cells_even`, `Square.lines_contradict`, `Square.noGlobal_of_contradiction`, `Square.mixture_le`, `Square.inLine`, `Square.inLine_support`, `Square.indexed_met`.
- `Cycle` (22): `Cycle.down`, `Cycle.system`, `Cycle.edges`, `Cycle.polarity`, `Cycle.length_edges`, `Cycle.lt_of_mem_down`, `Cycle.shift`, `Cycle.cross`, `Cycle.returns`, `Cycle.eq_of_even`, `Cycle.beq_self`, `Cycle.beq_of_ne`, `Cycle.telescope`, `Cycle.counts_even`, `Cycle.contradicts`, `Cycle.mixture_le`, `Cycle.miss`, `Cycle.pick`, `Cycle.value_pair`, `Cycle.walk`, `Cycle.walk_meets`, `Cycle.met_iff_even`.

## Regenerating the records

Run from the checkout root (`ROOT`):

1. Restore every record from main:

   ```bash
   for f in $(git ls-tree --name-only main theories/becoming/results/records/ | grep "\.json$"); do git show main:$f > $f; done
   ```
2. Reconcile: `python3 -B reconcile_records.py ROOT`. The sections come from `P110_SECTION`, `P111_SECTION` and `P112_SECTION` (defaults 146, 147, 148).
   - Add `--dry OUT` to write what would still be pending. 21 residuals are expected; they are what stays Ren's.
3. Regenerate the new records: `python3 -B make_records.py ROOT [SECTION_P111 SECTION_P112]` (defaults 147, 148).

The reconcile fails rather than guess:

- each specific replacement must match exactly once;
- a record changed only by the generic phrases and lacking a decision number stops the run. This is how records added after the delegation are caught: read the record and, where its readings are not within the delegation, add it to `EXCLUDE`;
- an earlier run's note (`MARK`) makes a record count as already reconciled.

After a merge, regenerate rather than resolve record conflicts by hand.

## The docstring fold

`fold_docstrings.py` has been applied on the branch and is not idempotent: its exactly-once assertions fail on folded text. To apply it again, restore the files it changed from `b7e453428`, the commit before the fold, and run it. Lean files a later main changes have to be merged by hand first. None of I4b-1, I4b-3 or P117 touched a folded module.

## Landing

`W` is the landing checkout.

1. Renumber the study sections if 146 to 148 are taken. Change the three headings, the cross-references in the sections and in the English paragraphs, and the kit's defaults, then regenerate the records as above.
2. Run the core checker, `check_becoming.py`. The new steps passed the scratch builds and are in the shared cache.
3. Regenerate the decidability page on the checked bytes. Then update the chapter's §9 totals and the Lean README totals from the receipt.
4. Bind the receipt to the two new records, one binding per proof reference.
5. Rebind the drift, with one reconciliation note per changed record:
   - 299 entries in 131 records come from the comment-only fold of 51 modules;
   - 67 entries in 67 records come from the chapter's reconciled sections and the study's English summary.
6. Run `research.py render`, the generativity-chain review of the changed sources, and the Lean and reading catalogues. Then run `research.py check` and `make research-test`.
   - The render writes the two new records' pages, which the chapter already links to. On the branch these six links are the only ones that do not resolve.

What `research.py check` reports on the branch:

- Four errors, all expected before binding:
  - “recorded-checked needs proof source and existing receipt”, once for each new record;
  - “needs a source hash binding”, once for each new record.
- Drift: 366 entries in 145 records. All of them come from files this branch changes, and step 5 reconciles them.

`make research-test` fails in two tests, both on those four expected errors. The style lint finds no error in the 103 changed records.
