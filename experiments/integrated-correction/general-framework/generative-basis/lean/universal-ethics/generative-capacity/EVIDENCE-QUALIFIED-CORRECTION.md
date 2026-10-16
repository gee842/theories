# Evidence-qualified correction

8 October 2026. [Research argument, source assessment and counterreview](../../../../../../../_process/research/2026-10-05-generative-foundation-review/history/root-foundation/EVIDENCE-QUALIFIED-CORRECTION-INTEGRATION.md).

Run `python3 check_evidence_qualified_correction.py` from this directory. It builds frozen sources with Lean 4.29.1, audits the 47 explicit declarations in [EvidenceQualifiedCorrection.lean](EvidenceQualifiedCorrection.lean), and compares [the case runner](EvidenceQualifiedCorrectionCases.lean) with a separately expressed Python reference. The [current receipt](evidence-qualified-correction-verification.json) binds retained sources, compiler, helpers and logs.

The new count is 24 theorems, 47 declaration audits and 19,808 matched records. Twenty-three audits have empty dependencies; the remaining standard dependencies are disclosed in the receipt. Five inherited modules keep their earlier counts.

`pooled_certificate_sound` retains soundness across causal-model uncertainty. `evidence_qualified_completion` links faithful refinement to actual guarded correction. The costed executable uses the existing `AlignmentInquiry` planner, permits immediate sufficient certificates, and can finish with two causal descriptions unresolved. Counterexamples retain misleading evidence, unobserved reorganization, insufficient response capacity and empty candidate sets.

Candidate coverage, faithful permitted structural inspection, stable query/use conditions, current response laws and protected execution remain assumptions. The inspection is not adversarial behavioral certification, physical fault injection or a proof of legitimate authority. No new algorithmic optimality, empirical reliability or independent acceptance is claimed. 中文范围：保留不确定性、取得相关区别与实际纠正的有条件连接。
