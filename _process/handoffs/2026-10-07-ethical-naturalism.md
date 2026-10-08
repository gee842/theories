# Handoff: ethical naturalism from the generative process (伦理自然主义)

7 October 2026. AI-authored handoff from the project thread "用生成理论证明伦理自然主义", written at Ren's request at the end of the round. Ren asked for the work to be committed on the branch only, not merged, with instructions an agent without this thread's context can use to merge it.

## To merge (for an agent with no context)

- **Branch:** `claude/ethical-naturalism-i6vvv6`.
- **What the branch adds to main:** one file, this handoff. Every proof and note from the thread was merged into main earlier; the last of them is `f91475e` (6 October). Before this commit the branch was fast-forwarded to main at `a823d4db`. The branch's head commit is the one that adds this file; `git log -1 origin/claude/ethical-naturalism-i6vvv6` shows its hash.
- **Merge:**
  ```sh
  git fetch origin main claude/ethical-naturalism-i6vvv6
  git checkout main && git merge --ff-only origin/main
  git merge origin/claude/ethical-naturalism-i6vvv6   # fast-forward if main has not moved
  ```
- **Conflicts foreseen:** none. The only new path is `_process/handoffs/2026-10-07-ethical-naturalism.md`. A conflict can arise only if another session adds a file with the same name.
- **Verification:** a handoff alone needs no rebuild. To confirm the package on the merged tree, see "Build and audit" below.

## Build and audit

Requirements: core Lean 4.29.1 on `PATH`, with no Mathlib and no lake project. Elan's release host returns 403 in the cloud container. In this session Lean was installed from the GitHub release tarball `lean-4.29.1-linux.tar.zst` into `/opt/lean/lean-4.29.1-linux`.

```sh
export PATH=/opt/lean/lean-4.29.1-linux/bin:$PATH
cd experiments/integrated-correction/general-framework/generative-basis/lean/naturalism
python3 check.py                  # about 1 minute
python3 check_actual_recovery.py  # about 15 seconds
```

**Expected output, rerun on `a823d4db` on 7 October 2026:**

| Checker | Status | Modules | New audits | Empty axiom reports |
|---|---|---|---|---|
| `check.py` | passed | 14 | 147 | 147 |
| `check_actual_recovery.py` | passed | ActualRecovery plus its closure | 21 | 21 |

`check_actual_recovery.py` also runs an independent enumeration, which reports 303 cases.

**What the checkers do:**

- Each builds every module fresh in a temporary directory.
- Each rejects `sorry`, warnings and any axiom in a new declaration (`ALLOWED_AXIOMS = set()`). This covers `propext`, `Quot.sound` and `Classical.choice`.
- Each requires every new theorem to have a `#print axioms` audit.
- Each rewrites its receipt (`verification.json`, `actual-recovery-verification.json`). If no Lean source changed, only the timestamp and platform fields change. In that case discard the receipts with `git checkout --`, rather than committing churn.

**One foreseeable failure.** `check.py` pins the SHA-256 of five inherited modules: `GenerativeCore`, `DynamicUnderdetermination`, `DynamicSymmetry`, `DynamicConsequences` and `EthicalOrientation`. The pins must equal `../verification.json`. The integrator thread owns `GenerativeCore`. If it rewrites that module, the checker stops with a hash mismatch. To fix it:

1. Rebuild.
2. Confirm the 147 audits are still empty.
3. Update `INHERITED_SHA256` in `check.py` to the new values in `../verification.json`.

Do not edit the inherited modules from this package.

## What the study answers

Ren's root message (preserved verbatim in [the source](../../sources/15-codex-theory-conversations/2026-10-06-ethical-naturalism-arguments.md)) lists:

- the four arguments for ethical naturalism: supervenience (Jackson), parsimony (Mackie), epistemology, and explanatory role (Cornell realism);
- the three identity candidates: welfare, Railton and Foot.

Ren says all of them can eventually be proved. The study note is [ETHICAL-NATURALISM.md](../research/2026-10-05-generative-foundation-review/root-foundation/ETHICAL-NATURALISM.md), in Chinese, §§0–11 with a formal index.

**What the round established:**

- The arguments' formal features hold for one candidate natural property: whole-history non-loss of realizable activities.
- Those features do not select the orientation. They hold for every step relation; this is the formal open question (§5.1).
- The orientation, the whole scope and the individuation of activities are inputs, and each is proved necessary (`PremiseNecessity`, §8).
- Supervenience and identity are derived, not posed between two kinds. Evaluation is modelled as a record inside the same process (`EmbeddedEvaluation`, §9).
- From the core alone, with finitely many states: an evaluating activity persists exactly when it can reach a regenerated state where it stays realizable (`RegeneratingPersistence`, §10).

Two later threads continued in this package:

- **`EnactedOrientation`** (27 results): at the level of eventual realizability the generative orientation is derived for what is enacted indefinitely. Handoff: [enacted-orientation](2026-10-07-enacted-orientation.md); study note §11.
- **`ActualRecovery`** (21 results): reducing the comparison to eventual realizability fails, because actual interruption survives restoration. Study note: [ETHICAL-NATURALISM-ACTUAL-RECOVERY.md](../research/2026-10-05-generative-foundation-review/root-foundation/ETHICAL-NATURALISM-ACTUAL-RECOVERY.md).

Ren then narrowed the ethical use of `loss_then_persistence` (§11.1). The question is whether ending an activity can improve the whole continuation, not whether every activity is kept.

## Files this thread created (all on main)

**Lean**, in `experiments/integrated-correction/general-framework/generative-basis/lean/naturalism/`:

| Module | New audits |
|---|---|
| `WholeQualityNaturalism.lean` | 25 |
| `NaturalismIdentity.lean` | 20 |
| `NaturalismReview.lean` | 10 |
| `ProtectedScope.lean` | 35 |
| `ProtectedScopeLimits.lean` | 6 |
| `PremiseNecessity.lean` | 9 |
| `EmbeddedEvaluation.lean` | 5 |
| `RegeneratingPersistence.lean` | 10 |

The same directory also holds `check.py`, `README.md`, `lean-toolchain`, `verification.json`, `verification/` and `verification-history/2026-10-06-before-axiom-removal/`.

**Notes**, in `_process/research/2026-10-05-generative-foundation-review/root-foundation/`:

- [ETHICAL-NATURALISM.md](../research/2026-10-05-generative-foundation-review/root-foundation/ETHICAL-NATURALISM.md), §§0–10;
- [ETHICAL-NATURALISM-PROTECTED-SCOPE.md](../research/2026-10-05-generative-foundation-review/root-foundation/ETHICAL-NATURALISM-PROTECTED-SCOPE.md), the reviewed negative round on the protected scope.

**Index entries:**

- `RESEARCH.md`, the entry "Ethical naturalism, first round 6 October 2026";
- `theories/shengsheng-buxi-generative-existence/unified-2026-10-05/ETHICAL-FOUNDATION.md`, the paragraph "Metaethical placement".

**Source:** `sources/15-codex-theory-conversations/2026-10-06-ethical-naturalism-arguments.md`.

## Resume point

Nothing is half-finished and nothing is uncommitted. Ren's last message in the thread, "请继续" (6 October, 21:17 UTC), was not acted on before the wrap-up: the later threads above took the next steps.

## Next concrete step

Compare the actual whole continuations of retaining, transforming and ending one common undertaking, all inside one process. RESEARCH.md states this as the next step after §11.1.

**Method:**

- Use the `ActualRecovery` profile: losses, recoveries and interruptions counted at one level on the actual run.
- Include realization, burden and the later conditions of generation.
- Test any candidate criterion against the four preserved counterexamples: restraint, escape, exclusive commitment and the unrecovered fall (`ProtectedScope`, `ProtectedScopeLimits`, `NaturalismReview`). The [protected-scope note](../research/2026-10-05-generative-foundation-review/root-foundation/ETHICAL-NATURALISM-PROTECTED-SCOPE.md) §5 shows that a single-step existential "removes" relation cannot do this. The comparison has to read the whole history.

**What would change the account:** a criterion derived from the process that passes all four counterexamples, or a proof that none can.

**Smaller step, now unblocked.** The valuation package is 130/130 axiom-free on main (`ea3bbe1f`). The earlier bridge from `persists_iff_regenerating_return` to `valuation_keeping_theorem` (`experiments/valuation-development/lean/ValuationRenewal.lean:117`) can now be restated without axioms. That bridge was commit `7c9e4654`, removed in `6ee530b` because it inherited `propext`. The coordinator asked for a cited correspondence rather than a parallel proof. Put it in its own small module or checker, as before, so the main package checker keeps no external imports.

## Open items for Ren

1. Whether persistence, or "can be enacted indefinitely", is the measure of good. This is not proved. If it is introduced as a premise, it must be proved necessary under the no-axioms rule.
2. **Which level evaluation belongs to.** At the eventual level the orientation is derived. At the immediate level it is not. `ActualRecovery` shows the eventual level omits actual interruption.
3. **Decidable state equality.** The positive forms (`persists_iff_regenerating_return`, `recurring_enactment_keeps`) take it as model data. The bound theorems do not need it.
4. Which regenerating whole an actual history reaches. Nothing here selects the history.

## Conventions in force

- No axioms in new declarations.
- Monist and relational framing: evaluation is a relation inside the one unfolding; any split is derived with its scope.
- No market vocabulary (`RENAMES.md`).
- New Lean goes in new modules, and inherited sources stay unchanged.
- Ren's words and AI elaboration are kept distinct.

Ren's latest instruction for this wrap-up was to commit on the branch without merging.

## Spawning a successor

Start a thread with this brief:

> Continue the ethical-naturalism study from `_process/handoffs/2026-10-07-ethical-naturalism.md`, read together with `_process/handoffs/2026-10-07-enacted-orientation.md` and `ETHICAL-NATURALISM-ACTUAL-RECOVERY.md`. Do the next concrete step under the project rules: no axioms, monist framing, no market vocabulary, and Ren's current merge instruction.
