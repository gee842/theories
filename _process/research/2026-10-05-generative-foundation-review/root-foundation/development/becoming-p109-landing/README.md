# Landing package: where a move is formed (P109)

动作在哪里形成的落地包。内容在分支 `p109-coupling`；本目录保存内容的文本与写入它们的脚本。

The records of P69 and P80 ([process-and-frame-as-readings](../../../../../../theories/becoming/results/records/process-and-frame-as-readings.md), [counterfactual-is-the-course](../../../../../../theories/becoming/results/records/counterfactual-is-the-course.md)) left open when a move is formed within the unfolding rather than supplied from outside, and when it is the part's own. Ren had agreed that “there are no two realities” (12 October 2026, [source](../../../../../../sources/15-codex-theory-conversations/2026-10-12-no-two-realities.md)) and asked to “finish all” (14 October 2026, [source](../../../../../../sources/15-codex-theory-conversations/2026-10-14-relation-first-refounding.md)). Claimed on the work board as P109 by Current math core (fork 2) [6c0ec8].

## Content

One commit on branch `p109-coupling`, on main `fc76e49f` (after P107, P83b, I3b, P83c and Keeping). It changes no existing module.

- `Becoming/Coupling.lean`, a new core module (L4, imports `Becoming.Counterfactual` and `Becoming.Readout`): 51 theorems, 72 declarations. `scratch_build.py` on `fc76e49f` gives every axiom report empty, with no warnings, and the root `Becoming` compiles with its 108-module closure, so no names clash. The module is stated on the shared definitions: `Learning.Lumped` for "formed through a reading" and "along a course"; Readout's `Reading`, `SingleValued` and `Decodes` for the record. An earlier draft had parallel `FormedThrough`, `FormedAlong` and `shownPolicy`; they were replaced before packaging.
- `apply_docs.py` makes these edits, reading the bullet and rows from `docs.json`:
  - `Becoming.lean`: the import and the module bullet, after `Becoming.Readings`;
  - `check_becoming.py`: `Becoming.Coupling` in the core list, after `Becoming.Readings`;
  - the Lean README: one L4 row after `Becoming.Readings` and the within-layer imports;
  - the theory chapter: in §8, the further-proofs item for the relational starting point becomes "where a move is formed is given", and Ren's choices gain the readings of where a move is formed; in §9, one L4 row (51 theorems).
- The study: a section, provisionally numbered 131, and its English paragraph (`study.md`, `study-en.md`; `apply_study.py`). Main holds 126–128, and the integrator has reserved 129 for I3c's records and 130 for P83d; the integrator numbers the section at landing.
- `DECIDABILITY-INVENTORY.py` (`apply_inventory.py`):
  - `policyUpto` is a construction that tells configurations apart (`same`);
  - `lumped_upto_iff` uses decidedness only in its proof (`same`);
  - `no_policy_upto_iff` and `throughout_or_fails` use it only in their proofs, to find a step (`find`).
- Records:
  - the new schema-2 record where-a-move-is-formed (`make_record.py`), its proof references hashed from the branch, `proof_bindings` empty and "receipt bound at landing";
  - paired notes in process-and-frame-as-readings and counterfactual-is-the-course (`update_records.py`). Each drops the answered item from next_delta, links the new record in related and adds one history note.

From `fc76e49f` with `Coupling.lean` copied in, `apply_docs.py`, `apply_study.py`, `apply_inventory.py`, `update_records.py` and `make_record.py`, run in that order, write the content commit. Each asserts the text it replaces, so a second run fails.

## Landing

`W` is the landing checkout.

1. Renumber the study section: `python3 -B renumber_p109.py W N`. It changes the heading, the English paragraph, the record's scope and history, and the two paired notes.
2. Run the core checker, `check_becoming.py`. Only `Becoming.Coupling` and the root are new steps, and both passed scratch builds stored in the shared cache.
3. Regenerate the decidability page on the checked bytes. Then update the chapter's §9 totals and the Lean README totals from the receipt.
4. Bind the receipt to where-a-move-is-formed: one binding per proof reference, as in P107's `bind_p107.py`. Rehash the study and chapter references that this landing changed, with one reconciliation note per changed record.
5. Run `research.py render`, the generativity-chain review of the changed sources, the Lean and reading catalogues, then `research.py check` and `make research-test`.

`research.py check --ids where-a-move-is-formed process-and-frame-as-readings counterfactual-is-the-course` on the branch reports two errors, both expected before binding: "recorded-checked needs proof source and existing receipt" and "needs a source hash binding". Every other finding is study or chapter drift in records that hash those two documents, which step 4 reconciles. The repository's style lint finds nothing in the new record.

Nothing here runs Lean, edits the board or commits.

## History

- 15 October 2026: first prepared on `1a82808d` (head `c13dad6d`, kept in the branch's reflog). When main moved to `fc76e49f`, the branch was rebuilt on it with the scripts above, and the provisional section number moved from 127, which I3b had taken, to 131.
