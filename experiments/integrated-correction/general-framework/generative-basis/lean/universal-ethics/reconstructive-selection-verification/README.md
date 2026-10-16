# Checked selection through developmental reconstruction

Run `python3 check.py` from this directory, or invoke it by path. The script requires the existing `leanprover/lean4:v4.29.1` installation. It compiles the actual [module](../ReconstructiveSelection.lean) in a fresh temporary directory with an isolated Lean import path, then audits every top-level declaration. Original checked source snapshots and all compiler/axiom outputs are preserved here; [verification.json](verification.json) binds them with hashes.

The package has 28 new theorems and 40 audited declarations. Standard logical dependencies are explicitly reported. There are no custom axioms or proof placeholders. All biological laws are explicit model inputs despite kernel acceptance.

The [integration and counterreview](../../../../../../../_process/research/2026-10-05-generative-foundation-review/history/root-foundation/RECONSTRUCTIVE-SELECTION-INTEGRATION.md) explains the exact selection domain, cost ceiling, finite-history bound and observation limits. This is a rational expected-descendant recurrence under a supplied context; it is not a proof of stochastic fixation, indefinitely renewed provision, microscopic coefficient formation or superiority over an equally informed conventional model.
