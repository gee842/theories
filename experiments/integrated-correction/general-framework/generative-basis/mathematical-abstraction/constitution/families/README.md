# Dependent domains and whole-family admission

Lean 4.29.1 with its bundled standard library. **33 new theorems / 52 declaration audits**, checked from frozen source in a fresh isolated build.

| Module | Scope | Theorems / audits |
| --- | --- | --- |
| [FamilyAdmission.lean](formal/FamilyAdmission.lean) | Finite dependent sums and sections; relative full admission there; finite/subsingleton-fiber support iff full predicate admission; section existence and infinite-base boundaries. | 14 / 17 |
| [DependentCompletion.lean](formal/DependentCompletion.lean) | Total functional dependent-graph ideals, inverse section reconstruction, fixed-base fiberwise transport, predicate membership/binders and concrete empty/inhabited fiber examples. | 19 / 35 |

Run from the repository root:

```sh
python3 experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/constitution/families/check.py
```

The [receipt](verification.json) binds source bytes, rebuilt inherited sources, previous receipts and audit assets. The checker rejects warnings, proof holes and custom dependencies. Its allowed standard dependencies are `propext`, `Classical.choice` and `Quot.sound`.

The base and whole fiber assignment are supplied. Finite cover proofs use classical reasoning; dependent section coverage is not advertised as a new executable enumerator. Full predicate admission on finite resulting carriers requires the stated formation premises there. Arbitrary finite-fiber support admission already has the force of full predicate admission, because the whole assignment can encode an arbitrary predicate.

The completed representation retains all qualifying ideals and global totality. Fiber correspondence keeps the base fixed. Binder transport is scoped to its pointwise correspondence hypothesis. There is no full dependent object-language, internal-universe reconstruction or independent root-derived infinite-domain admission in this package.

Read the [integration and exact correspondence](../../../../../../../_process/research/2026-10-05-generative-foundation-review/history/root-foundation/ROOT-MATHEMATICAL-FAMILIES-INTEGRATION.md), [affirmative argument and source assessment](../../../../../../../_process/research/2026-10-05-generative-foundation-review/history/root-foundation/ROOT-MATHEMATICAL-FAMILIES-ARGUMENT.md), and [independent internal review](../../../../../../../_process/research/2026-10-05-generative-foundation-review/history/root-foundation/ROOT-MATHEMATICAL-FAMILIES-REVIEW.md).
