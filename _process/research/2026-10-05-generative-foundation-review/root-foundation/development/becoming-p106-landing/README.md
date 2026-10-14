# Landing package: what a learner can learn through its registration (P106)

经其识所能学者的落地包。分支 `p106-learnable` 已含模块、注册与文档；本目录只含落地时才能完成的两步（可判定性清点与记录绑定）。

Branch `p106-learnable` (from main `a04727a4`) holds everything except the steps that need the checker's receipt:

| On the branch | Path |
|---|---|
| core module `Becoming.Learnable` (17 theorems, 23 declarations; imports Identification and Seeking; changes no existing module) | `experiments/.../lean/becoming/Becoming/Learnable.lean` |
| root import and bullet; core list and scope sentence of the checker; Lean README row and import notes | `Becoming.lean`, `check_becoming.py`, `README.md` there |
| study section 116 and its English paragraph | `BECOMING-RENEWAL-READING.md` |
| chapter: a paragraph pair after Identification, one bullet in each language in “Part I stated whole”, the §9 module row | `THE-THEORY-OF-BECOMING.md` |

Scratch build (`scratch_build.py`) against main `a04727a4`: no error or warning, every axiom report empty, no forbidden token. Not a receipt.

## Landing, after the checker slot is released

1. Merge or rebase onto main. If batch 4 added study sections, renumber section 116 (heading, the chapter's link anchor, the English paragraph and `record_template.py`'s history note) before step 2.
2. `check_becoming.py`, then `check_correction_inquiry.py`, with `LEAN_TIMEOUT=3600`; confirm both passed.
3. `python3 -B inventory_edit.py W`, regenerate `DECIDABILITY-INVENTORY.py` on the checked bytes, then the landing kit's `zero_count.py W`.
4. `python3 -B land_record.py W RECEIPT_UTC REVIEWED_AT_UTC`: installs `learnable-through-registration` (schema 2, every proof source bound to the receipt) and advances `learning-by-refutation` (next step, a related link, a paired history note).
5. §9 totals and the theorem counts in the chapter from the receipt; reconcile the records whose reviewed hashes of the study and chapter drift (read the diff first; the landing kit's `repoint.py`); reading and Lean catalogues, `research.py render`, session-map capture, then `research.py check` and the catalogue, session-map and link checks.
6. Commit with explicit paths; mark the board row.

Nothing here runs Lean or commits.
