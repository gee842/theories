# Landing package: the least registration with any number of conditions (P113)

任意多条件下最小的识的落地包。内容在分支 `p113-sensitivity`；本目录保存内容的文本与写入它们的脚本。

The record of P80 ([counterfactual-is-the-course](../../../../../../theories/becoming/results/records/counterfactual-is-the-course.md)) left open whether, with infinitely many conditions, sensitivity remains the least registration, or a counterexample; `Becoming.Counterfactual` lists it as not derived, and the theory chapter's §8 lists it among the further proofs under feedback and reach. Ren's goal of 12 October 2026: “move towards 100%, … pick the "What would move it most next" first” ([source](../../../../../../sources/15-codex-theory-conversations/2026-10-12-move-towards-100.md)). Claimed on the work board as P113 by Current math core (fork 2) [6c0ec8].

## Content

One commit on branch `p113-sensitivity`, on main `108e278e` (after I3e and P83g). It changes no existing module.

- `Becoming/Sensitivity.lean`, a new core module (L4, imports `Becoming.Counterfactual` only): 47 theorems, 58 declarations. `scratch_build.py` on `108e278e` gives every axiom report empty, with no warnings, and the root `Becoming` compiles with its 110-module closure, so no names clash. Both steps are stored in the shared cache. The module answers the question in three parts:
  - wherever a law reads finitely many conditions under each history (`ExchangeLaw.ReadsFinitely`, pointwise continuity), sensitivity is the least registration with any number of conditions (`ExchangeLaw.ReadsFinitely.least_registration`), and the comparison as the dynamics give follows;
  - given a decision of whether levels vanish eventually, the tail law is a counterexample (`tailLaw_no_least_registration`);
  - with the conditions numbered, every counterexample gives the weak limited principle of omniscience (`wlpo_of_not_through_sensitive`), and the decision of vanishing gives the limited one (`lpo_of_vanish_decided`).
- `apply_docs.py` makes these edits, reading the bullet and the rows from `docs.json`:
  - `Becoming.lean`: the import and the module bullet, after `Becoming.Coupling`;
  - `check_becoming.py`: `Becoming.Sensitivity` in the core list, after `Becoming.Coupling`;
  - the Lean README: one L4 row after `Becoming.Coupling` and the within-layer imports;
  - the theory chapter:
    - §9: one L4 row (47 theorems);
    - §8: the further proof under feedback and reach becomes "given", with the exact strength of a counterexample left open; the status row of the response as the dynamics give; Ren's choices for §6.10 gain the readings; the logical commitment gains the least registration beside `Web.lpo_of_ending` and `Listed.lpo_of_few`;
    - the paragraph of the response as the dynamics give: its "not derived" sentence now points to `Becoming.Sensitivity`. The same sentence still listed "nor when a move is the part's own", which P109 answered without editing this paragraph; it now points to `Becoming.Coupling`;
    - "Part I stated whole": the summary of the response as the dynamics give;
    - the glossary: the row "sensitive" is updated, and a row "reads finitely many conditions" is added.
- The study: a section, provisionally numbered 137, and its English paragraph (`study.md`, `study-en.md`; `apply_study.py`). Main holds 134–136 (I3d, I3e and P83g); the integrator numbers the section at landing.
- `DECIDABILITY-INVENTORY.py` (`apply_inventory.py`):
  - `vanishIndicator` and `tailLaw` build an indicator from the decision of vanishing (`indicate`);
  - the eight proof-only theorems of the least registration mix conditions in their proofs, as in `Becoming.Counterfactual` (`same`), with the same forms without a decision;
  - `lpo_of_vanish_decided` takes both cases of the decision (`split`).

  A scratch run of the inventory on the branch bytes, with only the receipt check skipped, reports 0 unused rows. Its totals are: statements depending on decidedness 331 → 347; proof-only 193 → 202; rows proving decidedness 132 → 136 (`WLPO.of_lpo`, `mixed_decides` and the two `wlpo_` theorems); decidability-taking definitions 92 → 94.
- Records:
  - the new schema-2 record sensitivity-is-the-least-registration (`make_record.py`). Its proof references are hashed from the branch, `proof_bindings` is empty, and it reads "receipt bound at landing";
  - a paired note in counterfactual-is-the-course (`update_records.py`): it drops the answered item from next_delta, links the new record in related and adds one history note. Its scope item saying this is not stated stays, because it still holds of that record's own theorems.

From `108e278e`, copy `Sensitivity.lean` in, then run `apply_docs.py`, `apply_study.py`, `apply_inventory.py`, `update_records.py` and `make_record.py` in that order to write the content commit. Each script asserts the text it replaces, so a second run fails.

Not changed here: the Lean README's Chinese within-layer imports lack `Distinguishing`, which the English has (since the P83e landing).

## Landing

`W` is the landing checkout.

1. Renumber the study section: `python3 -B renumber_p113.py W N`. This changes the heading, the English paragraph, the record's scope and history, and the paired note.
2. Run the core checker, `check_becoming.py`. Only `Becoming.Sensitivity` and the root are new steps, and both passed scratch builds stored in the shared cache.
3. Regenerate the decidability page on the checked bytes. Then update the chapter's §9 totals and the Lean README totals from the receipt.
4. Bind the receipt to sensitivity-is-the-least-registration, one binding per proof reference. Rehash the study and chapter references that this landing changed, with one reconciliation note per changed record.
5. Run `research.py render`, the generativity-chain review of the changed sources and the Lean and reading catalogues. Then run `research.py check` and `make research-test`.

`research.py check --ids sensitivity-is-the-least-registration counterfactual-is-the-course` on the branch reports two errors, both expected before binding:
- "recorded-checked needs proof source and existing receipt";
- "needs a source hash binding".

Every other finding is chapter drift, scoped to the sections this changes (§2, “Part I stated whole”, §8 and the glossary), in 11 records: comparison-where-the-rest-responds, continuous-time-as-tower, counterfactual-is-the-course, counts-exist-where-decided, imbalance-as-relatum, laws-at-coarser-steps, laws-at-finer-units, recurrence-without-decidedness, recurrence-without-premise, recurring-reference-revision and where-a-move-is-formed. Step 4 reconciles them; the added study section drifts no record. The style lint finds nothing in the new record. counterfactual-is-the-course keeps its two earlier correspondence length warnings.

Nothing here runs Lean, edits the board or commits.

## History

- 15 October 2026: prepared on `69336fa3`. Before the commit, main moved to `5225d441` (I3d landed with study §134, and I3e claimed §135). The scripts were rerun there, and the module and root rebuilt and the inventory rerun on the new bytes. P83g was then handed over with study §136, so the section is numbered 137 provisionally (`renumber_p113.py`); that commit, `9a5b9634`, is kept as branch `p113-sensitivity-on-5225d441`.
- 15 October 2026: I3e and P83g landed (`108e278e`, study §135–136). The branch was rebuilt on it with the scripts above; the module and root were rebuilt and the inventory rerun on the new bytes, with the numbers updated here.
