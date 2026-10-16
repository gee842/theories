# History batches H1-H7: exact move plans

Status: **applied 17 October 2026.** H1–H7 (commits 11308bad4 … 19c1acfa4) and H1-replace, H6-replace; receipts `_process/architecture/moves/<batch>.json`. The reconciliation batches RA–RE and RG followed (plans in `reconciliation/`). Originally: Produced for task A4 of the restructure (Ren, 17 Oct 2026; RESTRUCTURE-PLAN.md section 4.2). The move tool consumes the `H*.tsv` files; this page explains them.

## Files

| File | Contents |
|---|---|
| `H1.tsv` ... `H7.tsv` | `old_path<TAB>new_path<TAB>reason`. A path ending in `/` is a directory that moves whole (all tracked files below it). Every old path exists in `git ls-files`, no new path exists, no two entries nest or collide (checked). |
| `H1-replace.tsv`, `H6-replace.tsv` | Files whose **old path must receive a new file afterwards** (short MAP.md and GLOSSARY.md crosswalk; index READMEs for experiments). The moved original goes to the history path; **inbound links to the old path must not be rewritten** to the history copy. Same columns. |
| `H4-keep.txt` | The 32 chapters that stay in `theories/becoming/chapters/` (path, reason) plus the 3 pinned chapters. |
| `PINNED.tsv` | 84 files that would otherwise move but stay for now: `batch, old_path, would-be new path, why pinned`. Each can move once its pin is lifted (see "Pins"). |

## Totals

Entries are lines in the TSV; files are tracked files under them. The last column counts distinct files outside the batch that mention a moving name (live = not sources/, not frozen evidence).

| Batch | What | Entries | Files | Pinned (stay) | Live referrer files |
|---|---|---|---|---|---|
| H1 | Root/process corpus pages | 29 | 29 | 0 | 15 |
| H3 | Eight 10-04/05 studies and the specialist dossier | 234 | 426 | 31 | 469 |
| H4 | Superseded chapters, chapters/verification/, synthesis-*.md | 108 | 120 | 3 | 219 |
| H5 | root-foundation packets, spent kits, executed plans | 2387 | 3328 | 49 | 1080 |
| H6 | 5-Oct experiments, general-framework, generative-basis study files | 59 | 590 | 1 | 31 |
| H7 | Lean periphery run folders and lean/connected/ | 422 | 12772 | 0 | 550 |
| | **Total** | 3239 | 17265 | 84 | |

The "files" counts are tracked files that move; H7 is almost entirely run-folder content.

## Why things stay (rules applied)

Ren's rule: being linked or bound by a record is **not** a reason to stay, since the tool rewrites live links and record JSON paths and the moved bytes (hence record hashes) are unchanged. Things stay only in three classes.

1. Live current material: canonical chapter, OPENING, NONDUAL-METHOD, records, current studies' live files, latest reviews, work board, goals, directive register, tools, live landing tooling.
2. Pinned files: a freeze/preregistration manifest names the path with a hash (`protocol-freeze.json`, `FREEZE.json`, ...), a Python file outside the moving set hard-codes the path (`ROOT=parents[N]` style), or a receipt is bound by a record (proof bindings, `retained_run`). Moving these breaks a checker or invalidates a frozen manifest. Tool constants in `tools/research` that name a `.md` file are **retargeted**, not pinned.
3. `sources/`, always.

Process used for pins: read all `*.json` named freeze/prereg for repo paths they pin; grep all `.py`/Makefile/workflow text for the basename (two path components where the basename is ambiguous, and the study/experiment name as context); iterate until stable (a pinned script that itself moves is not a pin). 84 files pinned: hard-coded 69, freeze 9, read by an external checker as data 5, record-bound receipt 1.

## Exceptions kept in place, by batch

### H1
* `_process/reading-notes/out-*.md` (10) and `README.md`: cited about 355 times by theory READMEs; the plan keeps them. Inputs `hb-*`, `cb-*` (10 files, 3.6 MB, duplicates of sources/12 and sources/14) move.
* `_process/architecture/` (`start-state.json`, `validation.json`, `rename-2026-10-09.json`, `check_rename.py`): the plan's H1 row relocates the repair evidence to `_process/architecture/repairs/`. It is **not in the A4 brief**, and `check_rename.py` (must keep passing) re-derives from fixed paths and its add-commit, so I left it for whoever owns the checker. No rows.
* Live governance (`BRIEF.md`, `RESEARCH-DIRECTIVES.md`, `RESULT-WORKFLOW.md`, `research-config.json`, `goals/`).
* **`_process/LOST-ARTIFACTS.md` moves (as the brief lists it) but it is an open action list only Ren can close** (claude.ai artifacts never saved). Decision for Ren/integrator: either drop that row or leave a pointer in `_process/README`. `H1.tsv` marks it in the reason.
* MAP.md and GLOSSARY.md: see `H1-replace.tsv`. GLOSSARY.md (189 KB, 192 headwords, "canonical" in its own words) is replaced by a short crosswalk to chapter section 10; MAP.md by a short map.

### H3
* `2026-10-05-concern-theory/`: `experiments/recipient-value-learning/protocol-freeze.json` pins `reward-association/IDENTIFICATION.md` by path and sha256 and neighbours are hashed by receipts. Whole study stays.
* `2026-10-05-repository-reconciliation/whole-repo-review-2026-10-16/` (the latest review and the restructure plan) and `.../verification.json` (receipt of the preservation verifier, never overwritten).
* `2026-10-05-generative-foundation-review/foundation-assessment/`: not in the H3 brief; MARKET-INTERNET-DEGENERATION.md is bound by five records and its MARKET-* checkers are depth-bound (`ROOT=HERE.parents[3]`). Its README is a stack of status paragraphs, so a later decision should retire most of it.
* Hard-coded in `experiments/shared-renewal-capability` checkers (31 files, `PINNED.tsv`): support-and-shared-generativity `completion/` files, integrated-evolution `*-math.md`, causal-foundations `outputs/formal-results.md`, generative-health `DISCOVERY-MATH.md`, revisable-concern settlement/formal files, `completion/evidence/ceroni-2018` (xlsx hash in `ceroni_audit.py`). These move once the checkers' paths are retargeted (the checkers are in experiments, outside H3).
* The other 8 studies move whole; 234 entries because pinned files split their directories.

### H4
* 32 chapters stay (`H4-keep.txt`, one-line reason each): the canonical chapter, method, active section-11 studies, statement sources of records and open targets, and the Chinese-classics cluster. The plan expected about 30-60.
* Pinned (3): ALIGNMENT-COMPLETION.md (hard-coded in `foundation-assessment/FRONTIER-CHECK.py`), FORMAL-CORE.md and FORMAL-SPECIFICATION.md (hard-coded in `shared-renewal-capability/discovery/exact_check.py`).
* `chapters/CLAIMS.md` stays (generated stub via `navigation.py`).
* Everything else (about 100 chapters, `verification/`, three `synthesis-*.md`) moves. Heavy rewriting: the generated catalogues (`source-index.json`, `generativity-chain.json`, `ARGUMENTS-*`) cite chapter paths; the tool rewrites them, but they must be regenerated afterwards (see prerequisites).

### H5
* Kept (not in `H5.tsv`): spine reviews `BECOMING-*-REVIEW.md` (cited by core records), the study log `BECOMING-RENEWAL-READING.md` (158 records bind it), `BECOMING-UNIFICATION-PLAN.md`, `ZERO-PREMISE-PLAN.md`, `DELEGATED-CHOICES.md`, `MODULE-CLASSIFICATION.md`, `THEOREM-CONNECTIVITY.*`, `DECIDABILITY-INVENTORY.*`, `SPINE-INTEGRATION.py`, `README.md` (generated), `RESULTS-CATALOGUE-RECORD.md` (hard-coded at `reading_catalogue.py:178`), `GENERATIVITY-CHAIN-INDEX-RECORD.md`, the `build_*.py` compatibility wrappers, `SESSION-*` (tool data read by `session_map.py`, data must stay in place), and every file whose last change is 2026-10-10 or later.
* Kept under `development/`: the live landing tools (`rebind_batch.py`, `merge_records.py`, `renames.json`, integration `README.md`), `integration-i4a/`, `make_checker.py`, the readability drafts read by `test_schema2.py`, the latest reports (`i5-checker-reproducible`, `p129-review-fixes`, `p130-frontier-on-base`, review probes).
* Pinned (49, `PINNED.tsv`): files named by freezes (`agentdojo-evidence-boundary/independent-code-freeze.json`, the EVALUATIVE-PLASTICITY set, SELECTIVE-HANDOFF-*), files hard-coded by experiment checkers (e.g. `check_integration.py`), and `BECOMING-INSTANCE-CHECKS.json` (record-bound receipt).
* Moved: the 5-9 Oct packets (flat files), evidence folders of the 5-Oct root package and recipient line, `reason-action-evidence/` (apart from `experiment4-preview.tsv`, pinned), the 10-06 working set, spent landing kits and executed plans under `development/` (299 entries at the top level of `development/`).

### H6
* `experiments/integrated-correction/selective-handoff`, the freeze-pinned empirical experiments (`agentdojo-evidence-boundary`, `recipient-value-learning`, `recipient-harm-valuation`, `recipient-cue-grounding`, `motor-learning-cost`, `learned-claim-agents`), `shared-renewal-capability` (44 freeze manifests pin files inside), `market-generativity`, `valuation-development` (10 records, spine instances), the live generative-basis packages (`mathematical-abstraction`, `noninstrumental-concern`, `ecological-selection`, `inquiry-correspondence`, `biological-scale-correspondence`, `semantic-evidence`, `situated-kitchen-evidence`, `necessity-symmetry`), and the whole Lean root.
* `circular-construction` and `guardian-anarchy`: not Becoming experiments (a separate project; gitlink without `.gitmodules`). Outside history; **needs Ren**.
* Pinned (1): `closure-study/external-test/results-unfiltered/matched_rows.csv` is read by `foundation-assessment/benchmark/analyze.py`.
* Moved: 12 synthetic exact-finite cycle experiments (4-5 Oct; 0 records; no Lean), the 5-Oct financial specialisation, the general-framework proposal studies (`closure-study`, `gap-resolution`, `reproduction-test`, `review`), generative-basis study files outside `lean/`, and `endogenous-continuation` (misfiled checks of the revisable-concern settlement study).

### H7
* Not moved: `lean/becoming/becoming-checks/` and `fallible-inquiry-checks/` (evidence-store task, excluded), `lean/verification-history/`, `verification-runs/`, `legacy-replays/`, `verification/` (hard-coded archive paths; already history-like), every run folder named by `retained_run`, `proof_bindings`, record non-history fields or non-list receipt fields.
* Moved: `lean/connected/` whole (frozen 6-Oct builds; 0 records; its 4 checkers no longer pass against the live sources), and run folders in tiers, shown in the reason of each row:
  * T0 (177 rows): the timestamp id appears nowhere (no record, receipt or doc).
  * T1 and other (19 rows): named only in prose (docs, record history text, development reports), plus the `connected/` directory.
  * T2 (226 rows): named only inside generated `inherited_receipts` / `lean_steps.reused` lists of other receipts. Those lists are regenerated by the next checker run, but until then they carry the old path. **If the tool does not rewrite receipts, reconsider T2 or accept regeneration.** All 23 inherited spine modules keep a receipt under the Lean root (checked), because history stays below `<lean-root>`.

## Notes for the integrator

1. **Receipts interpretation.** I treated receipts (`*-verification.json`, `*-CHECKS.json`) as pinned only when a record binds them. Unbound receipts in moving directories move with their packet. Their internal sha256 entries keep working because bytes do not change, but any receipt that lists repo-relative paths will list old paths; the 10-09 rename precedent (manifests) covers them.
2. **H5 depth.** Files go from `.../2026-10-05-generative-foundation-review/root-foundation/X` to `.../2026-10-05-generative-foundation-review/history/root-foundation/X`, one level deeper than before, so relative `../` links inside moved files gain a level and `ROOT=parents[N]` scripts that move need N+1. The brief's "sibling at the same depth" is met at the `root-foundation` level (the history root is a sibling of `root-foundation/`). Run the link checker per batch.
3. **H6 and H7 targets** follow the same `history` sibling rule. Lean history stays under the Lean root so `passed_receipts` (`LEAN_ROOT.rglob('*.json')`) finds it; other tools skip `history` parts.

## Top referrers the tool will rewrite

"Referrer" = a tracked file outside the batch that names a moving path. Excluded: sources/, frozen evidence (`/history/`, `/before/`, snapshots, run folders, `-EDITS.json`, receipts, whole-repo-review, `/development/` except landing tools), which keep their old paths. For files with ambiguous basenames (130 entries) matching uses the last two path components; others use the basename; counts are therefore upper bounds. For H7 only T0-T2 run ids are counted.

### H1  (29 entries, 29 files)

Live referrer files: 15 (other theories 8, governance/root 5, generated catalogues/views 1, studies 1). Frozen-evidence referrers left alone: 32; sources/ referrers left alone: 9.

| Rewrites | Referrer |
|---|---|
| 6 | `theories/drives-narrative-attractors-and-mind/README.md` |
| 5 | `MAP.md` |
| 4 | `_process/reading-notes/README.md` |
| 4 | `theories/becoming/results/data/source-index.json` |
| 2 | `theories/selfishness-spiral-and-narrative-value-frames/README.md` |
| 2 | `theories/spirit-space-token-and-yi-substrate/README.md` |
| 2 | `theories/memories-and-working-style/README.md` |
| 1 | `GLOSSARY.md` |

### H3  (234 entries, 426 files)

Live referrer files: 469 (experiments 235, studies 78, records 68, chapters 25, other theories 22, governance/root 19, generated catalogues/views 18, tools 4). Frozen-evidence referrers left alone: 333; sources/ referrers left alone: 452.

| Rewrites | Referrer |
|---|---|
| 46 | `theories/becoming/results/data/source-index.json` |
| 29 | `theories/becoming/chapters/FORMAL-SPECIFICATION.md` |
| 17 | `theories/becoming/results/data/arguments-m-z.json` |
| 17 | `theories/becoming/results/ARGUMENTS-M-Z.md` |
| 16 | `_process/research/2026-10-05-generative-foundation-review/root-foundation/SESSION-PROOF-OVERLAP.json` |
| 15 | `theories/becoming/results/data/lean-index.json` |
| 9 | `theories/becoming/results/ARGUMENTS-A-L.md` |
| 9 | `theories/becoming/results/data/arguments-a-l.json` |

### H4  (108 entries, 120 files)

Live referrer files: 219 (studies 94, experiments 67, chapters 25, generated catalogues/views 17, governance/root 7, other theories 6, records 2, tools 1). Frozen-evidence referrers left alone: 84; sources/ referrers left alone: 72.

| Rewrites | Referrer |
|---|---|
| 104 | `theories/becoming/results/data/generativity-chain.json` |
| 99 | `theories/becoming/results/data/source-index.json` |
| 55 | `theories/becoming/results/ARGUMENTS-A-L.md` |
| 55 | `theories/becoming/results/data/arguments-a-l.json` |
| 50 | `theories/becoming/results/data/arguments-m-z.json` |
| 50 | `theories/becoming/results/ARGUMENTS-M-Z.md` |
| 33 | `theories/becoming/results/GENERATIVITY-CHAIN.md` |
| 27 | `theories/becoming/results/LEAN-INDEX.md` |

### H5  (2387 entries, 3328 files)

Live referrer files: 1080 (experiments 413, records 392, studies 140, other theories 44, chapters 35, generated catalogues/views 25, governance/root 23, tools 8). Frozen-evidence referrers left alone: 646; sources/ referrers left alone: 604.

| Rewrites | Referrer |
|---|---|
| 1078 | `theories/becoming/results/data/source-index.json` |
| 968 | `theories/becoming/results/data/generativity-chain.json` |
| 603 | `_process/research/2026-10-05-generative-foundation-review/root-foundation/GENERATIVITY-CHAIN-INDEX-RECORD.md` |
| 441 | `theories/becoming/results/data/lean-index.json` |
| 402 | `_process/research/2026-10-05-generative-foundation-review/root-foundation/SESSION-PROOF-OVERLAP.json` |
| 276 | `theories/becoming/results/GENERATIVITY-CHAIN.md` |
| 214 | `theories/becoming/results/LEAN-INDEX.md` |
| 152 | `theories/becoming/results/data/arguments-m-z.json` |

### H6  (59 entries, 590 files)

Live referrer files: 31 (studies 18, experiments 7, generated catalogues/views 4, chapters 1, other theories 1). Frozen-evidence referrers left alone: 30; sources/ referrers left alone: 154.

| Rewrites | Referrer |
|---|---|
| 16 | `theories/becoming/results/data/source-index.json` |
| 13 | `experiments/README.md` |
| 7 | `experiments/integrated-correction/README.md` |
| 5 | `experiments/integrated-correction/general-framework/README.md` |
| 3 | `experiments/integrated-correction/general-framework/generative-basis/README.md` |
| 3 | `_process/research/2026-10-05-generative-foundation-review/foundation-assessment/MEASURED-COMPARISON.md` |
| 3 | `_process/research/2026-10-05-generative-foundation-review/foundation-assessment/DOCUMENT-CHECKS.json` |
| 3 | `_process/research/2026-10-05-generative-health/discovery/DISCOVERY-MATH.md` |

### H7  (422 entries, 12772 files)

Live referrer files: 550 (records 300, experiments 109, studies 61, other theories 28, chapters 21, generated catalogues/views 15, governance/root 14, tools 2). Frozen-evidence referrers left alone: 225; sources/ referrers left alone: 291.

| Rewrites | Referrer |
|---|---|
| 214 | `experiments/market-generativity/meta-attractor/versioned-task-instances-verification.json` |
| 213 | `experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/machine-instances-verification.json` |
| 201 | `experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/organization-correspondence-verification.json` |
| 196 | `experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/retrodiction-instances-verification.json` |
| 193 | `experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/evolution-connectionism/learning-correspondence-verification.json` |
| 188 | `experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/renewing-correspondence-verification.json` |
| 184 | `experiments/integrated-correction/general-framework/generative-basis/lean/deeper/substitution-correspondence-verification.json` |
| 183 | `experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/evolution-connectionism/transmission-correspondence-verification.json` |

## Tool prerequisites (before each batch)

* `generative_chain.py` discovery globs `root-foundation/*.md` plus known paths: add the history location or the chain loses its sources after H5.
* `registry.reviewed_version` uses `git log --no-renames`: a moved file's review version resets unless `--follow`/rename detection is used.
* `reading_catalogue` requires catalogue rows to equal `chapters/*.md` (H4), and `lean_catalogue` GROUPS and `path_role` name run folders (H7).
* `navigation.py:273` (FOUNDATION-COMPOSITION.md) and `:275` (MAP.md) must be retargeted (H1, H5).
* `session_map` data stays pinned in place.
* `check_rename.py` and `_process/architecture/rename-2026-10-09.json` must keep passing; frozen evidence and sources/ keep old paths and resolve through the manifests.
* Run each batch, then `research check`, link check and the move-receipt check, before the next.

## Pins: lifting them

Most pins disappear if the pinning script is retargeted in the same batch (for hard-coded `.py` paths) or if Ren agrees to re-freeze (for `FREEZE.json` files; the 10-09 rename already broke one once). I did not retarget anything: A4 only plans. `PINNED.tsv` gives each file's would-be destination so a follow-up batch (H3b/H5b/H6b) can be produced mechanically.

## Open decisions

1. LOST-ARTIFACTS.md: move (as briefed) or keep (open action list for Ren).
2. H7 T2 rows (226 run folders named only in generated receipt lists): move now (lists go stale until regeneration) or wait for the evidence-store task.
3. `circular-construction`, `guardian-anarchy`: separate project; where should they live?
4. `foundation-assessment/`: retire most of it (stack of status paragraphs) or keep as live.
5. `_process/architecture` repair evidence: plan H1 relocates it; left because check_rename.py is outside this task.
