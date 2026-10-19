# R20(c): tooling and repository health

Board item R20(c), 19 October 2026. It follows the open points of the [whole-repository review of 19 October](../whole-repo-review-2026-10-19.md) (sections 2, 4 and 5 and "Still open after R19"). Work was done on its own branch in a worktree. No Lean source, record, chapter, OPENING, README lead, research configuration or generated page was edited, and nothing was deleted. The Lean checker was not run, because the landing queue allows one checker run at a time.

## 1. Lean in CI

**Before.** `.github/workflows/research.yml` ran `make research-test` and `make research-check`. These check receipt bindings and never run Lean.

**Done.** [`.github/workflows/lean.yml`](../../../../.github/workflows/lean.yml) adds the job `becoming-core`, which runs the package's own checker, `check_becoming.py`.

- **Triggers.** It runs on push and pull request when anything under the Lean root changes, or when the workflow itself changes. It can be started by hand (`workflow_dispatch`, with a `fresh` option), and it runs weekly on a schedule with `BECOMING_FRESH=1`. It is a separate workflow so that pushes touching only prose do not start a Lean run. Path filters work only per workflow.
- **Checkout.** Depth 1, sparse, limited to the Lean root. The checker reads only that root: the sources, `universal-ethics/generative-capacity/check.py` and the passed receipts that bind the three foundation modules. LFS objects are not fetched.
- **Toolchain.** The step installs elan with its official installer (`--default-toolchain none`), then installs the toolchain named in `becoming/lean-toolchain` (`leanprover/lean4:v4.29.1`). It prints `elan which lean` and `lean --version`. The checker finds Lean by `elan which lean` in that folder and asserts version 4.29.1. The core needs no Mathlib, because it compiles from the prelude.
- **Run.** `BECOMING_OUT=$RUNNER_TEMP/becoming-out`, so the receipt and run folder go to the runner's temporary directory and nothing is written into the checkout. Further settings are `BECOMING_JOBS=$(nproc)`, `LEAN_TIMEOUT=1800` and `timeout-minutes: 120`.
- **Cache.** `~/.cache/becoming-lean` (the checker's step cache) is restored and saved with `actions/cache/restore` and `actions/cache/save`.
  - The key is the hash of `lean-toolchain`, then the hash of every `.lean` under the Lean root, `check_becoming.py` and `check.py`. The restore key is the toolchain prefix.
  - Reusing entries is safe. The checker's own `step_key` covers the toolchain, the Lean binary's sha256, the step and the bytes of the step's whole import closure. `reuse` returns an output only when its digest matches the entry. Only CI runs write this cache, because a pull request cannot write main's cache.
  - After a passed run, a short script keeps only the entries named in the receipt's `lean_steps.keys`, so the cache does not grow with every restore. The script was tested on a dummy cache.
- **Artifact.** The receipt and run folder are uploaded as the artifact `becoming-receipt`, kept for 30 days, whether the run passes or fails.
- **Run time.** The receipt of 19 October (`20261019T064004.300228Z`) lists 1,088 step keys, of which 17 ran and 1,071 were reused. From the workstation's cache timestamps, runs of 500–730 steps took 3–11 minutes. A fresh run on a 4-core runner has not been timed. The 120-minute limit leaves a wide margin.

**Portability of the checker.** No fix was needed, and `check_becoming.py` is unchanged.

- Its paths come from `__file__` or `Path.home()`, and `BECOMING_OUT` and `BECOMING_LEAN_CACHE` move them.
- `held_in_main` asks git for `main`. On a CI checkout that has no local `main` (a pull request, or a sparse shallow clone), it falls back to "nothing held", and the run folder then copies every source. That is expected under `BECOMING_OUT`.
- A dry import with `BECOMING_OUT` set (no Lean run) resolved the output paths into that directory. It found 272 modules in the closure and 745 passed receipts under the Lean root, and every source path and every receipt in `inherited_receipts` is tracked by git.

**Not verified.** No GitHub run has happened. `actionlint` is not installed; both workflow files parse with PyYAML 6.0.2, and their steps were read back from the parsed structure.

## 2. `experiments/guardian-anarchy`

**Findings.** It is a gitlink (mode 160000, `10678ce4d819e80c90b8c938e536717a2147f9e4`), and there is no `.gitmodules`.

- In the main checkout it is a local nested repository with two commits on `main`. Its HEAD is `10678ce4`, which matches the gitlink.
- It has **no remote**: its `.git/config` has no `[remote]` section.
- Its README says it is "Local only" by Ren's instruction of 4 October.
- It carries a zero-byte `.git/index.lock` dated 19 October 13:12. It was left untouched, and the next git command in that folder will report it if it is stale.
- Links point into it from `experiments/README.md`, from `drafts/2026-10-04-guardian-anarchy/README.md` (three links) and from `review-round-02/theory.md` (two links). `make research-links` lists them under `not_in_repository`.

**Done.** Nothing. There is no URL to put in `.gitmodules`, and a `.gitmodules` entry with a local or invented URL would make `git submodule update` fail in every clone.

**Options** (none applied):

1. **Keep as is.** Clones get an empty folder, and the six links stay `not_in_repository`.
2. **Untrack the gitlink, keep the folder.** Remove only the index entry with `git rm --cached experiments/guardian-anarchy`, which leaves the files on disk, and add the path to `.gitignore`. Replace the six links with plain text noting "local only", as R19 did for the private sources. `git submodule status` then works, and no clone is misled.
3. **Back it up, then decide.** First make `git -C experiments/guardian-anarchy bundle create <outside-the-pushed-tree>/guardian-anarchy.bundle --all`, as the [16 October restructure plan](../whole-repo-review-2026-10-16/RESTRUCTURE-PLAN.md) item 9 proposes. Then either option 2, or import the site under `drafts/2026-10-04-guardian-anarchy/site/`. Importing would publish it, which its "local only" status rules out until someone decides otherwise.
4. **Give it a private remote.** A `.gitmodules` entry with that URL. Clones without access would then fail `git submodule update`.

Option 2 is the smallest change consistent with "local only".

## 3. Strict freshness of generated pages

**Before.** `research.py check` lists directory indexes and catalogues that differ from a render under `stale_indexes` and exits 0. The Lean catalogue is not compared at all; its own `lean_catalogue.py --check` does that.

**Done.**

- `research.py check --strict-fresh` turns every entry of `stale_indexes` into an error. It also renders the Lean catalogue (`index_outputs(render=True)`) and compares it, so the check fails whenever a render would change a generated page. The flag belongs to `check` only. Local `make research-check` is unchanged.
- `make research-check-strict` runs the secret scan, then `check --strict-fresh`. CI (`research.yml`) now runs it instead of `research-check`. It installs ripgrep if it is missing, because the Lean catalogue discovers files with `rg`. The run takes about 60 s here, against about 20 s for the plain check.
- **A render is now a fixed point (bug found by the strict check).**
  - The Lean catalogue's `source-index.json` records the links in documentation pages, README among them. Render computed it before writing README.
  - So after a change to README's links (here, the new contributor section), one `make research-render` left `source-index.json` stale, and a second render was needed.
  - `check_or_render` now re-renders the Lean catalogue after writing, and writes it again through `navigation.write_views` (same guards) when it differs.
  - Verified: on a tree whose generated pages had been restored, one render followed by `make research-check-strict` gave exit 0. Before the fix, the same sequence failed on `theories/becoming/results/data/source-index.json`.
- Tests: [`tools/research/tests/test_strict_fresh.py`](../../../../tools/research/tests/test_strict_fresh.py), four tests.
  - By default a stale index is reported without failing, and the Lean catalogue is not compared.
  - With strict, the check fails, the error names the page, and the catalogue is compared.
  - One render writes the Lean catalogue a second time exactly when it changed.
  - `render --strict-fresh` is rejected.

A remaining difference between CI and a local render: the Lean catalogue's discovery includes untracked and ignored `.lean` files (`rg --no-ignore`). A render in a checkout that has such files can therefore commit pages that a clean CI checkout renders differently. Render in a clean worktree before landing. The current main passes the strict check in a clean worktree.

## 4. Hard-coded `/Users/ren` paths in tracked `.py`/`.sh` files

There are 46 tracked files. By path role (`tools/research/paths.py`), 16 are history, 13 are sources and 1 is evidence. All 30 of those keep their bytes. The other 16 are live:

| File | Change |
|---|---|
| `…/root-foundation/development/bridge-fold/tools/{cite,feat,inventory,meta,permods,tables}.py` | Repository root from `git rev-parse --show-toplevel`, run in the script's folder |
| `drafts/2026-10-02-iaseai-selecting-the-selectors/supporting-material/build_supporting_pdf.py` | Font folder `Path(Path.home(), '.cache/codex-runtimes/…')`; the same folder on this machine |
| `worldbuilding/artifacts/friends-worldbook/build.py`, `build-v2.py` … `build-v5.py` | Default `--font-dir` as `Path(Path.home(), …)`; the flag still overrides it |
| `tools/publishing/build_chiang_mai_canvas.py` | **Left.** Its sha256 is pinned by the move receipt `_process/architecture/moves/moves-2026-10-19-publishing-builders.json`. All 18 move receipts pass `move --check`, and editing the file would make this one report `sha256 differs`. The fix is one line, `ROOT = Path(__file__).resolve().parents[2]`, which is what its two sibling builders already use. It should be made together with a decision on whether move receipts pin live tools after a move. |
| `experiments/…/acquisition/applicability/formal/check_correspondence.py` | **Left.** Its sha256 is recorded in its passed run receipts (`runs/20261006T…/receipt.json`). The hard-coded path is the elan toolchain binary, `~/.elan/toolchains/…/bin/lean`. Change it to `Path.home()` with its next run. |
| `experiments/…/remaining-dependency/formal/check_consequence_inquiry.py` | **Left.** Same reason: its sha256 is in `consequence-inquiry/verification.json`. |
| `_process/research/…/foundation-assessment/benchmark/analyze.py` | **Left.** It is a frozen protocol script, and `verify_outputs.py` checks its `code_sha256` against `analysis.json`. |

No pinned hash matched the changed files: a ripgrep of their sha256 over the tree found none outside `becoming-checks`. The six bridge-fold tools parse, and `git rev-parse --show-toplevel` from their folder gives the worktree root.

## 5. Contributor page

`_process/navigation/REPOSITORY.md` (the `readme_repository` part of README and BRIEF) gains "Running the checks". It covers the prerequisites, the three commands, the checker's environment variables and where receipts go.

**Python version.**
- The shared tools use the standard library only.
- They parse with Python 3.8 grammar (`ast.parse(feature_version=(3, 8))`), and the modules that annotate with `X | None` import `annotations` from `__future__`.
- Verified with Python 3.9.6 (`/usr/bin/python3`): all 171 tests pass, `research.py check` exits 0, `lean_catalogue.py --check` matches, and `check_becoming.py` imports.
- Also verified with 3.11.2, the default `python3` here.
- The page therefore says "Python 3.9 or later". `lean_catalogue.py`'s docstring still says 3.10+, which is more than it needs.

**README and BRIEF were not committed.** They are generated pages. A render was used to verify the result: the section appears in README and BRIEF, and its links resolve (`research.py links`: 0 broken). The generated files were then restored. Until the next `make research-render`, `make research-check` on this branch reports `generated view differs` for `README.md` and `_process/BRIEF.md`. It also lists `_process/research/README.md` under `stale_indexes`, because this record adds a folder to the study. The strict check would flag that page and `theories/becoming/results/data/source-index.json` as well. One render at landing settles all of them; until then CI's strict step would fail on this branch.

No root `CONTRIBUTING.md` was added. The target tree in [REPOSITORY-LAYOUT](../../../REPOSITORY-LAYOUT.md) lists the root files, and `CONTRIBUTING.md` is not among them.

## 6. Large binaries and run folders (recommendations; nothing destructive done)

### (a) LFS for new large binaries

- **Before.** LFS is set up in this repository. `.gitattributes` named one file, `sources/situated-recovery/heald-2021/originals/memory_updating_participant24.mat` (185 MB, stored in LFS). The `filter.lfs.*` configuration is present, and `git-lfs/3.8.0` is installed. The other tracked `.mat` files (16, 421 MB) are plain git, and no `.pkl` is tracked (the three RNA `.pkl` files are kept as `.lfs-pointer.txt`).
- **Added to `.gitattributes`.** `*.mat` and `*.pkl` now go to LFS, so a new file of either kind is stored there.
  - The 16 existing plain `.mat` files are reset to unspecified attributes (`!filter !diff !merge !text`), so their storage does not change.
  - Verified: `git hash-object --path=…` equals the index blob for plain and LFS files (`evoked_recovery_participant1.mat`, `spontaneous_recovery_participant8.mat`, `memory_updating_participant24.mat`). `git check-attr` gives `lfs` for a new `.mat` or `.pkl` and `unspecified` for the existing plain ones. `git status` shows no change under `sources/`.
- **PDFs.** No `*.pdf` rule was added. `.gitattributes` cannot select by size, and of 84 tracked PDFs (263 MB) only 15 are over 5 MB. A blanket rule would also need 84 exceptions. Instead:
  - name a large new PDF by path in `.gitattributes` before adding it;
  - better, have `research.py secrets` or a new `research.py large` warn when a tracked file over 5 MB is not an LFS pointer.
- **External data.** The heald-2021 data's redistribution terms remain open (review §5). LFS does not settle them.

### (b) `becoming-checks/` run folders

**How the receipts are bound.**
- `research-check` binds each `recorded-checked` record to a receipt by **path**, through a `references[].path` with role `receipt`.
- `registry.validate` reads that `verification.json`. It checks the source sha256 at `sha256_pointer` and success at `success_pointer`, and reads the declaration names elaborated for the module.
- It reads no other file of a run.
- `check_becoming.py` (`passed_receipts`) reads every `*.json` under the Lean root to find receipts for inherited modules.
- 82 of the 231 runs are cited by records, through 1,182 receipt references.

**What takes the space.**
- 231 runs; 488 MB on disk.
- 339 MB of that is the `verification.json` receipts themselves (about 3 MB each in recent runs; `modules` is 1.5 MB of the current one). Those are the evidence.
- 171 runs already have a `RUN-INDEX.json` and objects in `_objects/` (56 MB).

**Recommended policy.** It keeps every receipt at its path, so every binding stays valid, and loses no byte.

1. **Pack, do not delete.**
   - `research.py evidence plan …/becoming-checks --bare receipt` (read-only, run for this record) would pack 228 runs.
   - Three runs stay whole: the two kept by default and the latest passed.
   - Tracked files go from 43,552 to 5,368: 38,412 duplicate working copies removed, and 4,241 first copies renamed into `_objects`. Every receipt stays in place.
   - With the default `--bare whole`, 203 runs stay whole, because their stamps are mentioned in prose.
   - `evidence restore <run>` rebuilds any run byte for byte.
   - The integrator should run it, between landings, with `pack --apply`. It changes many tracked paths, so it needs a quiet queue.
2. **Commit only landing runs.**
   - Dry runs and rehearsals use `BECOMING_OUT` outside the repository.
   - CI now re-derives the core on every Lean change, so a rehearsal receipt adds no evidence that CI does not give.
   - Each committed run adds about 3 MB of receipt.
3. **Retention class per run.** Keep in place:
   - every receipt;
   - every run a record, a current receipt or a link names;
   - the latest passed run;
   - the two newest runs.

   Every other run is packed, or after packing moved whole to `lean/history/becoming-checks/` with `research.py move`. The checker's receipt discovery still finds receipts there (layout: "History layout"). A move does not reduce size; packing does.
4. **Receipt size.** Not changed here, because records bind receipts by JSON pointer. If growth matters, the receipt could keep `modules[].declarations` in one sidecar per run, keyed by sha256, in a later format version. The `binds` and `elaborated` readers would have to follow it.

## Checks on this branch

| Check | Result |
|---|---|
| `make research-test` | 175 tests, OK (1 skipped); 171 before plus the 4 new ones |
| `make research-check` | Before the contributor section: exit 0, no errors, `stale_indexes` empty. Final state: exit 1, with `generated view differs` for `README.md` and `_process/BRIEF.md` only, and `_process/research/README.md` in `stale_indexes`. These are the expected consequences of editing the `readme_repository` source and adding this record without committing a render (section 5). |
| `make research-check-strict` | Exit 0 on the rendered tree after one render |
| Pre-existing, unchanged | 458 style warnings (352 `length`), `changed_outside_cited` 300, `reading_drift` 82 |
| `research.py links` on README, BRIEF and REPOSITORY.md (rendered) | 186 links, 0 broken |
| All 18 move receipts, `move --check` | 0 errors |
| Lean | Not run (rule: one checker at a time); CI will run it |
