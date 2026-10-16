# P83 landing package: identification, what a bounded record fixes

This continues the single relational spine after P70–P72 and P73. It reads states from the registered history, and asks what a finite record fixes when that history has a supplied bound on its states. It adds `Becoming.Identification`, importing `Becoming.Description`, at Description's layer (L4). No existing mathematical module is changed.

Ren's authorization is the [12 October framing and pairs exchange](../../../../../../sources/15-codex-theory-conversations/2026-10-12-framing-and-pairs.md); the [work board](../../../../../BECOMING-WORKBOARD.md) holds the claim and landing queue. This package was resumed on 13 October 2026 from the Claude handoff supplied by Ren. The current result is `identification-where-bounded`, with documentary deltas to `learning-by-refutation` and `wisdom-root-part-one`.

## Result and boundary

- Histories with at most N and N′ states are fixed by agreement before N + N′ − 1. The lower bound is proved for N = 1 and N = N′; exactness for arbitrary unequal bounds remains open.
- A lasso hypothesis within a supplied bound N that fits the record before 2N − 1 holds everywhere. The learner that knows the bound is right from that step; no universally unrefuted learner can always speak sooner when N ≥ 2 and two distinct values are available.
- P73's learner that does not know the bound is right at every step from N + (2N − 1)·tri N. This constructive bound strengthens the account beyond P73's preserved double-negation statement; it does not make that bound visible in the learner's record.
- Finite registered futures name the split that makes sense under a determined law on a closed list. Learners and deciding likeness require decidable equality of registered values. The bound and these representation conditions remain explicit hypotheses.

The bilingual study and record retain the exact theorem statements, inputs, counterexamples and open questions. “Situational truth” is an AI reading awaiting Ren; this result does not prove a universal zero-premise foundation.

## Existing evidence and review

The module's SHA-256 is `3bc3beb5afde6f1266d20926fd830b7a99f4a14c34f5a69225d6336ff05e5a10`. At takeover it was byte-identical to Claude's scratch source at `/private/tmp/claude-501/-Users-ren-theories/27ca9fd9-d3aa-4667-b205-3440a8b4e511/scratchpad/frontier/p83/tree/Becoming/Identification.lean`.

[claude-build7.out](evidence/claude-build7.out) preserves the original bytes of that scratch directory's `build7.out`. It reports 42 theorems, 54 declarations, an empty axiom map and no unclean build. This is retained scratch evidence, not a consolidated receipt or a new run by Codex. The landing still requires actual source-bound core and periphery checks.

Ren's supplied handoff reports that P73's owner reviewed the earlier version, requested the precise double-negation wording and suggested the constructive bounded rest step. Those corrections are present. The final 42-theorem version's independent review is unconfirmed; `docs/review.json` states this limited provenance.

**Takeover validation, 13 October 2026.** The integrator's actual core receipt `20261013T085153.061517Z` and periphery receipt `20261013T085221.613502Z` both pass; the core receipt binds the module hash above and lists 42 theorems / 54 declarations. Documentation and record integration use study §97 after the P70–P72 commit `6ef63a95`.

Separately, the documentation pipeline was exercised in a disposable worktree based on `6ef63a95`, using conspicuously marked stand-in receipts dated 2099. Module registration, all document anchors, current totals, guarded catalogue hashes, the new record, both P73 deltas, guarded receipt re-pointing, canonical rendering and focused metadata checking passed with no errors or drift. This dry run exercised no Lean checker and supplies no mathematical evidence. It exposed and fixed two packaging bugs: the receipt's `core` label is not the L4 layer, and the canonical reference scanner does not accept named instances as individual declarations (those remain audited in the receipt and full source binding).

## Landing

The driver commits nothing and runs no checker. Use it only in the integrator's assigned slot, after P70–P72 and P73. `BASE` is the pre-P83 commit and `S` the next free study section (97 directly after P70–P72).

1. `python3 -B land.py prepare ROOT` copies the unchanged module and registers it in `Becoming.lean` and the core checker.
2. Run `check_becoming.py`, then `check_correction_inquiry.py`, serially. Regenerate the decidability inventory; reconcile any new classification against the actual Lean definitions, then update the zero-premise plan's counts. Do not use stand-in receipts for landing.
3. `python3 -B land.py docs ROOT --section S --base BASE` applies the bilingual study, P73's requested cross-reference, plan, chapter, Lean README and guarded reading-catalogue update. It also updates only current verification totals; historical counts and review scopes stay intact.
4. After all source edits are read and final, `python3 -B land.py records ROOT --section S --base BASE` writes the new source-bound record, updates P73's documentary deltas and their review timestamp where content changes, and uses the shared guarded receipt re-pointing helper. Pre-existing unmatched drift is left for reconciliation.
5. Regenerate the reading and Lean catalogues, render canonical records, capture the session map, re-point any reviewed generated-source changes, render again, and run `make research-check`, the catalogue checks and relevant link checks. Commit only the reviewed landing and update the work board.

`totals.py ROOT` is also reusable for adjacent landings. The reading update is deliberately P83-specific. Scripts assert exact anchors and are not idempotent: investigate a failed stage before retrying. `make_records.py` may be rerun after rereading later source changes; it does not duplicate P73's history entries.
