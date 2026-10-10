# P49 landing fragments (branch only)

The documentation of P49 (`Becoming.Testing`) waits for its place in the landing queue, after `Becoming.Locality`. Its study section number, the receipt, the counts and the review's ordinal are fixed only then. These are the fragments and the scripts that apply them:
- `docs/study_zh.md` and `docs/study_en.md`: the study section and its English summary paragraph;
- `docs/plan_rows.md`: the unification plan's row and bullet;
- `docs/chapter.py`: the chapter edits;
- `apply_docs.py`: applies all of these, filling the placeholders from the receipt;
- `make_records.py`: writes the two records and extends becoming-finite-horizon.

They live on the branch `p47-testing` so that the text is not only in a session scratchpad. At landing they are applied, and the applied text in the study, plan, chapter and records is canonical. This directory is not landed.
