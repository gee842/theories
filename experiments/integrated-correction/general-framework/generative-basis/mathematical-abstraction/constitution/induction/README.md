# Collective induction and the universal recursion role

**28 new Lean theorems / 47 declaration audits.** Fresh isolated Lean 4.29.1 build; bundled `Std` only.

| Source | Theorems / audits | Scope |
| --- | --- | --- |
| [InductiveDomain.lean](formal/InductiveDomain.lean) | 24 / 38 | Induction iff generated coverage; selected variant assuming admission of the generated predicate; separated constructor reconstruction; unique recursion and boundary examples. |
| [Initiality.lean](formal/Initiality.lean) | 4 / 9 | Same-universe initiality iff generated coverage and constructor separation. |

Run from the repository root:

```sh
python3 experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/constitution/induction/check.py
```

The [receipt](verification.json) binds frozen source bytes, checker, toolchain, audit driver and logs. All named declarations are audited; warnings, proof holes and custom axioms fail the check. Standard dependencies are `propext`, `Classical.choice` and `Quot.sound`. Empty printed axiom lists do not mean that the ambient natural numbers, recursors and logical foundation have been independently justified.

The base carrier, seed, successor and metatheory remain supplied. The selected induction equivalence explicitly assumes `C (Generated z s)`; its thin `OnlyGenerated` example is not a Henkin model or a proposed full semantic range. Initiality quantifies over all seeded successor carriers in the same universe and uses the generated subtype and lifted `Nat` in the converse proof. The source constructs an inverse natural-number correspondence under generation and separation, using classical choice of indices.

This checks the exact mathematical contract of collective arithmetic formation. It does not derive infinity, full predicates or unique root constitution from no premises. Read the [integration and correspondence](../../../../../../../_process/research/2026-10-05-generative-foundation-review/history/root-foundation/ROOT-MATHEMATICAL-INDUCTION-INTEGRATION.md), [affirmative warrant argument](../../../../../../../_process/research/2026-10-05-generative-foundation-review/history/root-foundation/ROOT-MATHEMATICAL-INDUCTION-ARGUMENT.md) and [independent internal review](../../../../../../../_process/research/2026-10-05-generative-foundation-review/history/root-foundation/ROOT-MATHEMATICAL-INDUCTION-REVIEW.md).
