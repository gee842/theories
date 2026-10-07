# Checked completion and admissibility proofs

7 October 2026. Lean 4.29.1 / `Std` formalization of the current [completion argument](../../../../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/GENERATIVE-MATHEMATICAL-ADMISSIBILITY.md), following [Ren’s proof requirement](../../../../../../../sources/15-codex-theory-conversations/2026-10-07-lean-proof-requirement.md).

The [integration and scope ledger](../../../../../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/COMPLETION-WARRANT-LEAN-INTEGRATION.md) maps the earlier A/W results to these generalized proofs. This package includes arbitrary ideal families and infinite traces, not only finite test instances. It adds no empirical experiment or claim of ethical/metaphysical necessity.

Run from the repository root:

```sh
python3 experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/completion/formal/check.py
```

The script uses the installed pinned Lean toolchain, compiles source snapshots in a fresh temporary directory, audits every named theorem and supporting definition/structure, rejects custom dependencies and proof holes, checks that source bytes stayed unchanged during compilation, and writes [verification.json](verification.json) with [compiler logs and generated audit](verification/CompletionAudit.lean). No research-package compiled object is reused. Lean’s ordinary `propext`, `Quot.sound` and `Classical.choice` dependencies are exposed separately from mathematical hypotheses. No claim of zero assumptions is made.

| Source | Mathematical coverage |
|---|---|
| [IdealWarrant.lean](IdealWarrant.lean) | Nonempty directed ideals; W1 classification, W2 least hull, W2a fixed prohibitions; lower-subtype correspondence. |
| [CompletionRole.lean](CompletionRole.lean) | A1 dcpo/compact basis; A2 unique continuous extension; A2a positive reading; A3 unique compact-generated completion. |
| [PrefixSafety.lean](PrefixSafety.lean) | W3 explicit prefix topology; W4/W5 global counterexamples; W6 finite-program diagonal and literal-prefix interface; finite proof of infinite recurrence. |
| [CompletionExamples.lean](CompletionExamples.lean) | A5 finite-subset/powerset correspondence; concrete countdown; finite joins; arbitrary-subset approximations; infinity and append counterexamples. |
| [HistoryIdeals.lean](HistoryIdeals.lean) | A4 full history-tree representation; finite/infinite order correspondence; exact W4/W5/W6 ideal-class bridges. |
| [FiniteBranching.lean](FiniteBranching.lean) | A4b arbitrary-depth finite-branching lift with finitely many initial states and a fixed label sequence. |
| [CompletionBoundaries.lean](CompletionBoundaries.lean) | Why compactness and generation cannot be dropped from the completion role. |

Application limits are explicit. Finite descriptions’ arbitrary output semantics do not constitute a verified universal-machine implementation. Lifting gives existence of a mathematical path under the represented law, not effective selection or actual physical infinity. Preserving a candidate norm requires a faithful interpretation of its complete content; these theorems do not justify the norm’s first ethical authority.

The original handwritten notes and historical receipts are preserved. This is the current proof package, with [independent statement review](../../../../../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/COMPLETION-WARRANT-LEAN-REVIEW.md); old “no Lean verification” statements describe their original checkpoints.
