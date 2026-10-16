# Limits of a fixed universal representation

7 October 2026. This package checks a set/function form of Lawvere's diagonal theorem and its precise coverage consequences. It supports the [mathematical completion attempt](../../../../../../../_process/research/2026-10-05-generative-foundation-review/history/root-foundation/ROOT-MATHEMATICAL-COMPLETION-ATTEMPT.md); it does not refute a generative ontology or a stratified account of mathematics.

[CoverageBoundary.lean](formal/CoverageBoundary.lean) proves:

- If a family indexed by `A` represents every function `A → Y` pointwise, every endomorphism of `Y` has a fixed point.
- Boolean negation and propositional negation yield an explicitly missing diagonal for every same-carrier reading family.
- A family that includes this diagonal cannot also be completely represented by that same family. Full external predicate admission is sufficient for the contradiction but not necessary.
- Using the supplied predicate type as a larger description domain represents all predicates of a fixed lower carrier. Adding one new description can preserve all old readings while representing the old diagonal.

The obstruction concerns the exact coding/closure contract. It neither says that mathematical truth must be finitely coded nor excludes an external interpretation, hierarchy or non-effective root. The positive constructions expose their new description or predicate-domain resources rather than derive them from the root.

Run from the repository root:

```sh
python3 experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/constitution/global/check.py
```

The [receipt](verification.json) records a fresh isolated Lean 4.29.1 build: **14 theorems, 21 explicitly named source-level declaration audits, no reported axioms**. Source screening and the saved [audit driver](verification/KernelAudit.lean) reject proof holes, custom axioms and unapproved dependencies. Lean's kernel and type-theoretic background remain the verification basis; an empty axiom report is not an assumption-free ontology. No categorical-library formalization or general incompleteness theorem is claimed.
