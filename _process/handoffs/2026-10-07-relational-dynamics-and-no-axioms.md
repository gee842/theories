# Handoff: relational dynamics, no-axioms ledger, dependency map

7 October 2026 (UTC). Written by the AI session that worked on the dependency-map thread, at Ren's request to stop after this round. The text is AI-authored. Ren's directives are quoted from the source notes linked below.

## Where the work is

- Branch: `claude/project-thread-x1q9hl` on `yongxu/theories`, merged into `main` on 7 October 2026 (fast-forward to `ab995e9`, after merging main into the branch four times this round). The branch and `main` match as of this file's commit.
- Lean: 4.29.1 with no Mathlib. In the cloud it is at `/opt/lean-4.29.1-linux/bin`; put it on `PATH` and every checker named below runs. See the team memory `lean-build-in-cloud`.

## What is proved, and where

All paths are relative to `experiments/integrated-correction/general-framework/generative-basis/lean/`. Every audit listed is empty, meaning no axiom at all: no `propext`, no `Quot.sound` and no `Classical.choice`, per [Ren's rule](../../sources/15-codex-theory-conversations/2026-10-06-no-assumptions-no-axioms-rule.md).

| Result | Module | Check |
|---|---|---|
| U1/U2 conditional package and renewal examples, re-proved constructively | `conditional/ResourceContinuation.lean`, `conditional/RenewalExamples.lean` | `conditional/check.py`: 63 audits |
| The native port conserves held + enacted relative to arrived (U1 with equality) | `conditional/native-port/NativePortContinuation.lean` | `conditional/native-port/check.py`: 27 audits |
| Receipt calibration removed from the macro probe law; it uses the inversion the port acquires | `inquiry-root/sufficiency/CalibratedMacro.lean` | `inquiry-root/sufficiency/check_contact_formation.py`: 47 modules, 805 audits |
| Static and toggle are one dynamics under relational identity (bisimulation); every always-continuing single-event process is the one recurrence; "state unchanged" reads carrier equality; only idle versus continuing remains | `deeper/RelationalDynamics.lean` | `deeper/check_relational.py`: 13 audits |
| For any events, continuation (a self-renewing region) is bisimulation-invariant and gives histories of every length. Without supplied event identity, the continuing part of every process is the one recurrence (`core_erased_is_one_recurrence`). With event identity kept, a two-event counterexample is preserved (`labels_carry_remaining_difference`) | `deeper/RelationalContinuation.lean` | `deeper/check_relational.py`: 12 audits, with an empty closure |

Rerun after the merge with main: the contact-formation, renewal, naturalism, conditional, native-port and relational checkers all passed. When main's new code in `RevisingPort` was merged, two old names (`charge`/`.paid`, `.wasted`) were carried into the [renamed vocabulary](../../experiments/integrated-correction/general-framework/generative-basis/lean/verification-history/2026-10-06-before-vocabulary-rename/README.md). After the valuation thread's axiom-free rewrite, the contact-formation checker builds its new `AxiomFree` module. That module's one unused binder (`b` at line 41) became `_`, since the checker rejects warnings; no statement changed. The valuation thread's `LineageInProcess` still used the support package's old names (`AccountLaw`, `support_trace_balance` and others), so it would not have built once this branch reached main. It now uses the renamed ones with no change of statement. With the axiom-free support package and main's axiom-free renewal package, all 130 theorems of the valuation study now depend on no axioms (see the [valuation README](../../experiments/valuation-development/README.md)). The phase-period checker (11 modules) also passes.

## Ledgers

- [Dependency map](../research/2026-10-05-generative-foundation-review/root-foundation/PROCESS-LAW-ENTRY-DEPENDENCY-MAP.md): §7 is the no-assumptions ledger and §8 checks the splits against the one process. The rows on dynamics selection and on process and law are updated.
- [Context for the three open items](../research/2026-10-05-generative-foundation-review/root-foundation/PROCESS-LAW-OPEN-ITEMS-CONTEXT.md) is in Chinese. Item 1 now records both relational results. Shared copies are in `/mnt/project-files/dependency-map/`.

## What is open, and why

1. **Dynamics selection, now narrowed.** Once neither carrier identity nor event identity is supplied, a dynamics differs only in where continuation is kept or lost. Event identity is still a supplied distinction, and `labels_carry_remaining_difference` shows that continuation alone does not select among labelled dynamics. Reading "continuation is what generativity selects" is interpretation, not a theorem.
2. **Evaluation direction.** This belongs to the naturalism thread. On the merged tree, all 147 of its audits are empty.
3. **Lean's own logic.** It cannot be removed from inside Lean, because of Gödel's second incompleteness theorem. Possible mitigations are a minimal list of kernel rules or an independent checker.

## Exact next step

Prove whether event identity can itself be read relationally. Identify events by what follows them: a relation on labels that is preserved along steps, alongside the bisimulation on states. Then test it on the preserved counterexample in two ways:
- show that `onlyFirst` and `alternating` become one dynamics under that identity; or
- show that some relational difference survives, and name it.

Extend `deeper/RelationalContinuation.lean`, or add a module beside it with its own entry in `deeper/check_relational.py`. Then update ledger §7 and item 1 of the open-items context.
