# Full admission and function-graph reconstruction

7 October 2026. This package tests the remaining admission premise after the [higher-order semantic reconstruction](../higher-order/README.md). It combines an exact fullness characterization, a proper symmetric comparison family, and reconstruction of functions through completed finite graphs. It does not derive unrestricted admission or exclusive metaphysical root dependence.

- [Admission.lean](formal/Admission.lean): full predicate admission iff all finite predicates are admitted and every ambient nonempty directed union is admitted. Finite/cofinite predicates obey finite Boolean operations, arbitrary bijective relabeling and every finite membership pattern, yet exclude parity on the natural numbers. **34 theorems, 50 declaration audits.**
- [FunctionGraphs.lean](formal/FunctionGraphs.lean): full functions correspond to total functional finite-graph ideals; functionality has an exact finite-member criterion, while totality remains explicit. Recursive predicate and arrow reconstruction preserves every formula of the earlier finite simple-type language. Admission of all Boolean-function true fibers is equivalent to full predicate admission. **18 theorems, 36 declaration audits.**

The [integrated argument and result](../../../../../../../_process/research/2026-10-05-generative-foundation-review/history/root-foundation/ROOT-MATHEMATICAL-ADMISSION-INTEGRATION.md), [admission correspondence](../../../../../../../_process/research/2026-10-05-generative-foundation-review/history/root-foundation/ROOT-MATHEMATICAL-ADMISSION-LEAN.md), [function correspondence](../../../../../../../_process/research/2026-10-05-generative-foundation-review/history/root-foundation/ROOT-MATHEMATICAL-ADMISSION-FUNCTIONS.md) and [review](../../../../../../../_process/research/2026-10-05-generative-foundation-review/history/root-foundation/ROOT-MATHEMATICAL-ADMISSION-REVIEW.md) retain the exact scopes.

## Reproduce

```sh
python3 experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/constitution/admission/check.py
```

Run from the repository root with Lean 4.29.1 and Python 3 installed. The checker builds frozen source bytes in a fresh temporary directory, first compiling the unchanged `IdealWarrant`, `CompletionRole`, `CompletionExamples` and `TypedTruth` imports after matching their prior receipt hashes. It then checks both new modules and the saved [audit driver](verification/KernelAudit.lean).

The [receipt](verification.json) records **52 new named theorems and 86 explicitly named declaration audits**, with only `propext`, `Quot.sound` and `Classical.choice`. No custom axioms, proof holes, unsafe bypasses or `native_decide` are used. Automatically generated declarations are compiled with their module but not separately counted. Imported theorems are not counted as new.

## Assumptions that remain visible

Directed-union closure quantifies over all ambient predicate families; the finite-parts family used to recover a target predicate is itself selected using that target. The finite/cofinite example refutes sufficiency of the displayed weaker formation conditions, not a generative root that independently warrants full completion. It is not advertised as a Henkin model or a replacement for an independently specified full subject.

The function reconstruction admits all total functional graph ideals. Its decoder uses classical choice; totality is a condition over every input. The completed type grammar is the earlier finite `base`/`arr`/`pred` grammar, with no dependent types or internal universe. An ideal can have infinitely many finite members and need not have an effective presentation. All-formula semantic equivalence does not supply a truth decision procedure.
