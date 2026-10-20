# Integration helpers for the general-laws plan (14 October 2026)

Scripts the integrating session used to land the plan's streams on main, kept as evidence of how
the records were merged and rebound. They are not shared infrastructure (no tests); read them
before reuse.

- `merge_records.py`: field-level three-way merge of record JSON between two branches
  (`history`/`text_versions` append-merged, `references`/`proof_bindings` keyed by path,
  aliases set-merged; `--renames renames.json` applies the rename table inside code spans,
  law declarations and counterexample witnesses).
- `rebind_batch.py`: one reconciliation pass after a landing batch — hashes the changed files
  listed in a notes file, re-points proof bindings to a receipt that binds the current source,
  and appends one paired history note per record. It does not add receipt references; a bound
  receipt must also be a hashed `references` entry with role `receipt`.
- `scope_batch2.py`: in-place replacement of receipt sentences in `validation_scope` for batch 2.
- `renames.json`: the old → new names of 14 October 2026 (the official table is in
  [the unification plan §10](../../../../history/root-foundation/BECOMING-UNIFICATION-PLAN.md#10-第一部分与第二部分--part-i-and-part-ii)).
- `notes-batch2.json`, `notes-batch3.json`, `notes-batch4.json`: the receipts and the per-file change
  notes used for the history entries of batches 2–4.
- Batch 4 of the open-issues plan (14 October 2026): `b4_bind.py` restores the six B1 records'
  general-law bindings and binds the new core modules' proof references before `rebind_batch.py`;
  `b4_receipt_refs.py` then makes every bound receipt a hashed receipt reference;
  `receipts-batch4.json` names the five runs.
