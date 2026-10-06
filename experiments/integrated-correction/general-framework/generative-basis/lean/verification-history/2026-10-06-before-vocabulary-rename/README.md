# Before the vocabulary rename, 6 October 2026

AI-assisted rename at [Ren's direction](../../../../../../../sources/15-codex-theory-conversations/2026-10-07-market-names-and-continuation.md): replace market and exchange names (fuel, spent, income, account, reserve, demand, credit, bill, charge, payment, funding) with names for what the activity does: held (存), enacted (化), arrived (来). The full old → new list is [RENAMES.md](RENAMES.md); the machine-readable map is [renames.json](renames.json).

## What is preserved

- `sources/`: the exact pre-rename bytes of every changed Lean, Python and JSON file, at their repository-relative paths.
- `receipts/`: the pre-rename `verification.json` and compiler logs of the conditional package and the native-port module.
- [before-audits.json](before-audits.json): `#print axioms` for every declaration in the 41 affected modules, built from the preserved sources.

## What the check shows

[check.py](check.py) rebuilds the current sources of the 41 modules (all modules whose identifiers changed plus their import closures) in a fresh temporary directory, with Lean 4.29.1. Every audited declaration must report exactly the axioms it reported before, under the declared renames, and every build must be warning-free. The [receipt](receipt.json) records: 41 modules, 800 audits, 44 renamed declarations, no mismatches. Statements and proofs are unchanged; only names and comments changed.

`SupportedRevision.lean` needs Mathlib and is not built here. Its change is four imported-name substitutions, visible by comparing it with the preserved source.

The package checkers (`conditional/check.py`, `native-port/check.py`, `inquiry-root/sufficiency/check_native_packet_correspondence.py`) were rerun on the renamed sources and pass. The native correspondence still has 5,928 cases with unchanged outcomes. Older run directories and checkers that pin pre-rename hashes are historical records and were not edited.

Run from this directory: `python3 check.py`.
