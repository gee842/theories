# Acquired correction: reproduction

Run `python3 check_acquired_correction.py` from this directory (or pass its full path). The checker uses installed Lean 4.29.1, builds a fresh temporary closure and stores frozen sources, signatures, axiom reports and comparison logs in `acquired-correction-checks/`. It updates `acquired-correction-verification.json` only with that run's result.

The new source is [AcquiredCorrection.lean](AcquiredCorrection.lean); [AcquiredCorrectionCases.lean](AcquiredCorrectionCases.lean) emits finite comparisons against the separately written iterative reference in the checker. `AlignmentInquiry` and `EffectiveCommand` are inherited dependencies and are not recounted as new results. There are 24 new theorem statements and 45 explicit-declaration audits, including 21 with no axioms. The remaining reports contain only standard Lean axioms.

The 25,284 matched records comprise 1,470 searches on 147 depth-two trees and 23,814 acquisition/dispatch configurations. These are same-author finite checks, not measured deployment reliability or independent review. General results come from the kernel-checked proofs.

Read the [integration, assumptions and counterreview](../../../../../../../_process/research/2026-10-05-generative-foundation-review/history/root-foundation/ACQUIRED-CORRECTION-INTEGRATION.md) before interpreting the result. Faithful fixed finite inspection, authorized reads, inherited endpoint operation and an atomic dispatch are explicit premises. Search and revalidation charge declared inspection units, not full CPU or physical costs. Technical authentication does not establish legitimate authority or defeat capture of the credential process.
