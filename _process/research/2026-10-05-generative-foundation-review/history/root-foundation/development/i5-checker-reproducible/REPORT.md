# I5 检查器加固与可复现构建 / Checker hardening and a reproducible build

基础设施，不是成果：Lean 源、定理、记录主张与范围均未改动。处理发布准备度审查 §1 的 C1–C4，以及 §6 与 §7 第 4 项中的可复现问题。

Infrastructure, not a result: no Lean source, theorem, record claim or scope changes. Branch `i5-checker-reproducible` (from main `1a78f978`), merged into main after R18. It addresses findings C1–C4 of §1 and the reproducibility items of §6 and §7 (item 4) of the [release-readiness review](../../../history/root-foundation/BECOMING-RELEASE-READINESS-REVIEW.md). Written by the I5 subagent (Opus 5.5) and saved by the lead, because the harness kept the subagent from writing report files.

Commits: `575289df` (untrack bytecode), `d65bbeaf` (scanner), `2db481ce` (checker), `eb11cee3` (README, Mathlib pin), `67fb3d93` (FallibleInquiry).

## Changes

1. **Bridge environment audit** (`lean/becoming/check_becoming.py`).
   - The existing `collectAxioms` driver runs a second time, over the bridge modules' own constants (`BridgeEnvironmentAudit.lean`).
   - Every constant must have an empty axiom report. The only exception is a generated `injEq` on `propext` that is not a source declaration.
   - Inherited modules keep their allowance: `propext`, `Quot.sound`, `Classical.choice`.
   - The core driver is unchanged, so its step is reused.
   - New receipt keys: `bridge_constants`, `bridge_generated_axiom_dependencies`.

2. **Declaration scanner** (`lean/universal-ethics/generative-capacity/check.py`).
   - `scan()` now reads declarations:
     - at any indentation inside `namespace`, `section` and `mutual`;
     - after `open … in`;
     - after attributes and modifiers (`private`, `protected`, `noncomputable`, `partial`, `nonrec`, `scoped`, `local`).
   - Names keep their primes (`foo'` was read as `foo`) and `_root_.`.
   - It still reads `code_only` text, so comments, docstrings and strings are skipped.
   - Private declarations and unnamed `instance :` cannot be audited by name, so they are returned separately. The receipt lists them under `not_audited_by_name`, together with the environment audit that covers them.
   - `declarations()` still returns the list that can be audited by name.

3. **Inherited receipts** (both checkers).
   - A receipt counts only where its top level is passed and it maps the module structurally to its current sha256.
   - Retained file copies (`artifact_sha256`) do not count.
   - The check is still informational, and still asserted.

4. **Toolchain resolution.**
   - `resolve_lean()` uses `LEAN` if it is set, else `elan which lean` in the package folder, else the old default path.
   - It asserts version 4.29.1, records and keys the binary's sha256, and records how Lean was found in `lean_resolution`.
   - New file: `lean/becoming/lean-toolchain`.
   - Used by the core checker, `check_fallible_inquiry.py` and `scratch_build.py`.

5. **Outside runs.** `BECOMING_OUT=<dir>` sends the run folder and the receipt to that directory. The default is unchanged. `BECOMING_LEAN_CACHE` is now documented.

6. **README.**
   - A bilingual section, 自行验证 / Verify it yourself.
   - A statement that the Mathlib periphery checkers depend on an external project.
   - `lean/periphery-mathlib-pin/` holds that project's `lakefile.lean` and `lake-manifest.json`, byte for byte, with a provenance README.

7. **Bytecode.** `git rm --cached` on 54 `.pyc` files in `__pycache__/`; they stay on disk. Three `.pyc` files under `sources/20-…` stay tracked: they are imported originals listed in that snapshot's manifest.

## The cache key is unchanged

- Unchanged: `step_key`, `module_keys`, `imports_of`, the context, and every existing driver text.
- Spine registries equal those in receipt `20261015T231055.702986Z`.
- Only the inherited `KnowledgeCorrespondence` gains a declaration (`decoder`).
- A scratch build of an unchanged `Onward.lean` reused all 54 steps.

## Scanner impact

- 188 tracked checkers import the scanner.
- Over all 23,030 tracked `.lean` files, no file the old scanner read now fails.
- 109 more files are read, and 108 change their declaration lists: primed names, `_root_` names, and attribute-prefixed or `noncomputable` declarations.
- In the Becoming closure, every unnamed instance is in a core module: Change 4, Resolution 4, Counting 3, Quantum 2, Identity 2, Population 1, Entropy 1, Gluing 1. The core environment audit covers all of them. The bridge has none.

## Inherited receipts

- All 78 inherited modules have structural matches, and so do all 43 FallibleInquiry imports.
- The substring test accepted 2,351 module–receipt pairs; 1,961 of them remain.
- Every structural match was also a substring match.

## Tests and runs

- `make research-test`: 101 tests pass, on the branch and again on main after the merge.
- Core checker, out of tree (`BECOMING_OUT` set), tree untouched: `passed`, `core_axioms: []`, 9,753 declaration audits, `bridge_constants: 851`, one generated `injEq` with an axiom (`RepairComparison.State.mk.injEq`, `propext`), `lean: elan which lean`, 3 steps run and 676 reused. Receipt `20261016T120140.024624Z`, not kept in the repo.
- FallibleInquiry: passed, with 31 theorems and 37 declaration audits using `propext` and `Quot.sound` only. Receipt `20261016T120403.241963Z` is committed with its run folder.
- Record `finite-fallible-inquiry-necessity` is reconciled. After reading the checker diff, its hash was updated and the new receipt added, with a history note. The claim is unchanged.

## Not done

- No `BECOMING_FRESH=1` run; the integrator does that at the end.
- No minimal lakefile for `lean/becoming/`.
- In inherited modules, private declarations and unnamed instances are not covered by name. None occur in the current closure.
- The external Mathlib project's git commit is not recorded, because worktree isolation prevented it. The file hashes are recorded instead.
- CI is unchanged. CI runs are blocked by GitHub billing, which Ren has to fix.

## Fresh run, on main `d21b311a` (lead, 16 October)

`BECOMING_FRESH=1` with `BECOMING_OUT` outside the tree, which was left untouched. Lean was found with `elan which lean`.
- **Result:** `passed`. All 703 Lean steps were run and none were reused, so nothing came from the shared cache.
- **Axioms:** `core_axioms: []`. Of the 851 bridge constants, one generated constant uses an axiom: `RepairComparison.State.mk.injEq`, on `propext`.
- **Audit:** 9,912 declaration audits, 7,214 theorems in spine and bridge, 6,918 of them in the core.
- **Receipt:** `20261016T130738.412710Z`, sha256 `faced25f…72834`, 2.4 MB, not kept. The checker's printed summary is kept as [fresh-run-20261016T130738.412710Z-summary.json](fresh-run-20261016T130738.412710Z-summary.json).

## Receipt preserved (17 October 2026)

The full fresh-run receipt was found in the session scratchpad that produced it and copied unchanged into tracked evidence: [`becoming-checks/20261016T130738.412710Z/verification.json`](../../../../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/becoming-checks/20261016T130738.412710Z/verification.json), sha256 `faced25fba227bbc0e9cab3cc7f23ecac1e864b8734f947f52a094426fe72834` (1,059 files in the run folder). Two other runs that existed only outside main were copied the same way: `20261011T170859.998618Z` (cited by the entropy landing; from worktree `jolly-pike-140c94`; verification sha256 `44a27d49c490421c56b160d0f17aed5267a1bfa5764531d670733be471c1d5ce`) and `20261016T112106.917817Z` (from `review-wt`; sha256 `ca2a3e19a1bdc80655fd0ba102dcdaa6763f681e5d416b838ea4f1dccfb77432`). No rerun.
