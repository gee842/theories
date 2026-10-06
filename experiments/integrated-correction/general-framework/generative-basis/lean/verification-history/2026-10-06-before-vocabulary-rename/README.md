# Before the vocabulary rename, 6 October 2026

AI-assisted rename at [Ren's direction](../../../../../../../sources/15-codex-theory-conversations/2026-10-07-market-names-and-continuation.md): replace market and exchange names (fuel, spent, income, account, reserve, demand, credit, bill, charge, payment, funding) with names for what the activity does: held (存), enacted (化), arrived (来). The full old → new list is [RENAMES.md](RENAMES.md); the machine-readable map is [renames.json](renames.json). Modules that reached main during the rename (contact formation, phase cycle, port valuation) were renamed when the branch was merged with main, and are covered by the same check.

## What is preserved

- `sources/`: the exact pre-rename bytes of every changed Lean and Python file and of the regenerated JSON data, at their paths below `experiments/`.
- `receipts/`: the pre-rename receipts and compiler logs of the conditional, native-port and renewal packages, and the process-law, contact-formation and phase-cycle receipts.
- [before-audits.json](before-audits.json): `#print axioms` for every declaration in the 48 affected modules, built from the preserved sources (`python3 check.py --record-before` rebuilds it).

## What the check shows

[check.py](check.py) rebuilds the current sources of the 48 modules (all modules whose identifiers changed plus their import closures) in a fresh temporary directory, with Lean 4.29.1. Every audited declaration must report exactly the axioms it reported before, under the declared renames, and every build must be warning-free. The [receipt](receipt.json) records: 48 modules, 963 audits, 48 renamed declarations, no mismatches. Statements and proofs are unchanged; only names and comments changed.

`SupportedRevision.lean` needs Mathlib and is not built here. Its change is four imported-name substitutions, visible by comparing it with the preserved source.

The package checkers were rerun on the renamed sources and pass: the conditional, native-port and renewal packages, the native correspondence, the 32-module process-law closure (599 audits, all empty, with a new run directory), contact formation and the phase cycle. Three checkers needed small changes to run here: `check_process_law.py` and `check_phase_cycle.py` now use the `lean` on `PATH` when the pinned Mac compiler or elan is absent, still requiring Lean 4.29.1 at the same commit and recording the binary used; `renewal/check.py` pins the renamed `SupportNecessity` hash. The native correspondence still has 5,928 cases with unchanged outcomes. Older run directories and checkers that pin pre-rename hashes are historical records and were not edited.

Run from this directory: `python3 check.py`.
