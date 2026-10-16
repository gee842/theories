# Landing package: the apart modules read on the shared base (P114)

散立的模块在共同基底上陈述的落地包。内容在分支 `claude/bold-stonebraker-811bc3`；本目录保存在回执之后写入记录的脚本。

Ren asked on 15 October 2026, “so for our theories, they are proved in a dag order and can be all connected right?” The theorem-level measure ([THEOREM-CONNECTIVITY.md](../../THEOREM-CONNECTIVITY.md)) found that on main `c143e7d9`, 971 of 6136 spine theorems neither use the base (`Generative.Process`/`Trace`, `Becoming.Frame`/`Run`, `Becoming.World`/`Flow`/`Web`) nor are used by a theorem that does, and 26 records with spine aliases rest only on such theorems. Claimed on the work board as P114 by "Connect apart spine theorems", a side session of "Theory proof DAG ordering" [a50c0c]. Whether one family is defined from the other is not touched; that is Ren's.

## Content

One commit on the branch, on main `c143e7d9` (after P113). No existing module or definition changes.

- `Becoming/Courses.lean`, a new core module (L4): 87 theorems, 97 declarations. It imports Lasting, Countdown, Retrodiction, Copying, CrossSituational, Readout, Weighted, Description, Feedback, Decidedness and Metaethics, and states their main laws on the courses of a process, a frame's configurations or a web's conditions. There is no new premise. The identifications are themselves theorems:
  - a disturbed history is a run of the disturbed process (`run_history`, `historyRun`);
  - a determined law's orbit is the course of its process (`trace_orbit`, `orbit_trace`, `reach_iff_orbit`, `completes_units_iff`);
  - a partial law's run is a trace of its process;
  - a dated history is a run (`anyChange`, `anyRun`);
  - a reduction of a run is a run of the law read through it (`reducedRun`).
- `Becoming/CoursesBridge.lean`, a new bridge module (imports `Becoming.Bridge`): 3 theorems. It states `ClassificationRobustJudgment` on a frame's configurations. Along a generative extension, the comparison needs no excluded middle.
- `scratch_build.py` on `c143e7d9` builds both modules, the root and the seven other bridge modules, with empty axiom reports and no warnings, and stores every step in the shared cache.
- Docs:
  - `Becoming.lean`: the import and the module bullet, after Sensitivity;
  - `check_becoming.py`: `Becoming.Courses` in the core list after Sensitivity, and `Becoming.CoursesBridge` in the bridge list;
  - the Lean README: one L4 row and the within-layer imports;
  - the theory chapter's §9: one L4 row (87) and one bridge row (3). The totals line is left for the receipt.
- The study: section 138 and its English paragraph, numbered provisionally after main's 137.
- `DECIDABILITY-INVENTORY.py`:
  - `Courses.release` and `Courses.inspection` are classified as constructions that tell tokens apart (`same`);
  - the ten proof-only instances are classified as the laws they instantiate.

  A scratch run on the branch bytes, with only the receipt check skipped, reports 0 unused rows. Statements depending on decidedness go 347 → 363, proof-only 202 → 212, decidability-taking definitions 94 → 96.
- `THEOREM-CONNECTIVITY-DUMP.lean` (the measure of "Theory proof DAG ordering") imports `Becoming.CoursesBridge`. The measure asserts that the dump covers every spine module.
- `apply_p114.py`, this package's script.

Records are not edited on the branch, because their new references must bind to the landed receipt.

## Measure (`apply_p114.py --dry`, on the branch bytes)

| | `c143e7d9` | branch | branch, with the kit's aliases |
|---|---:|---:|---:|
| spine theorems | 6136 | 6226 | 6226 |
| apart (own vocabulary + prelude-only) | 971 (885 + 86) | 799 (736 + 63) | 799 |
| records resting only on apart theorems | 26 | 2 | 0 |
| records whose best alias is a statement on the Process family | 62 | 62 | 85 |
| records whose best alias is a statement on the World family | 67 | 67 | 70 |

On the branch, 24 of the 26 records already reach the base: their existing aliases are now used by theorems that do. The two left, fallible-witness-diagnosability and fulfillment-chance-floor, alias only `_by_core` theorems of `Becoming.Bridge`, which `Courses` does not use. Every record reaches a statement class once the kit adds its aliases.

## Landing

`W` is the landing checkout.

1. Renumber the study section if 138 is taken. The section text appears in the heading and in "Section 138" of the English paragraph; pass `--section N` to the script in step 4.
2. Run the core checker, `check_becoming.py`. Only `Becoming.Courses`, `Becoming.CoursesBridge`, the root and the bridge modules that import the root are new steps, and all of them passed scratch builds stored in the shared cache.
3. Regenerate the decidability page on the checked bytes: `python3 -B DECIDABILITY-INVENTORY.py`. Then update the chapter's §9 totals and the Lean README totals from the receipt.
4. From `W`, run `python3 -B <this folder>/apply_p114.py [--section N]`. It checks that the retained copy of the receipt passed for the current bytes of both modules and names every alias and declaration used here. Then, for each of the 26 records, it adds:
   - the module source as a proof reference with its declarations;
   - the retained receipt as a receipt reference;
   - one binding;
   - the aliases;
   - one bilingual history entry.

   Claims, hypotheses, Ren's words, dependencies and validation scope are unchanged. The script measures again; `records_resting_only_on_apart_theorems` must be empty.
5. Rehash the study and chapter references that this landing changed, with one reconciliation note per changed record, as usual.
6. Run `research.py render`, the generativity-chain review of the changed sources and the Lean and reading catalogues. Then run `research.py check` and `make research-test`.
7. Optionally, `THEOREM-CONNECTIVITY.py --write` refreshes the measure's JSON. Its page (THEOREM-CONNECTIVITY.md) belongs to "Theory proof DAG ordering" and is left to it.

Nothing here edits the board or commits.
