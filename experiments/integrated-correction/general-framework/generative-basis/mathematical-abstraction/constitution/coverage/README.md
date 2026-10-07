# Finite admission and named higher-order theory coverage

7 October 2026. The [verification receipt](verification.json) records a fresh Lean 4.29.1 build with **36 new named theorems and 66 declaration audits**. Only `propext`, `Quot.sound` and `Classical.choice` occur; no proof holes or custom axioms are accepted.

| Module | Theorems / audits | Result |
| --- | --- | --- |
| [FiniteAdmission.lean](formal/FiniteAdmission.lean) | 23 / 27 | One finite selection family covers all predicates on a finite carrier; empty/singleton/binary-union formation gives full admission. Function and predicate carriers remain finite through every declared finite type over a finite base. |
| [SignatureTruth.lean](formal/SignatureTruth.lean) | 13 / 39 | Arbitrary typed named signatures, formula comprehension, whole-theory satisfaction, satisfiability and semantic consequence transport through the earlier graph/ideal representation. |

The first result removes an infinitary completion premise only at its finite scopes. The second works over arbitrary supplied bases but retains full type domains and concrete symbol correspondence. Neither independently justifies all infinite mathematical domains or covers every mathematical foundation from the root.

The named natural-number addition example checks a concrete application. A Boolean example changes symbol meanings and changes equality truth; it shows why the correspondence premise matters, not a failure of the theorem under that premise.

From the repository root:

```sh
python3 experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/constitution/coverage/check.py
```

The checker copies frozen source bytes into a fresh directory, verifies six inherited source hashes against the existing completion, higher-order and admission receipts, recompiles those dependencies and the two new modules, then audits each named new declaration. Warnings, errors, proof holes and unapproved axioms fail the run. Inherited results are not counted as new.

Read the [integration](../../../../../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/ROOT-MATHEMATICAL-COVERAGE-INTEGRATION.md), [exact correspondence](../../../../../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/ROOT-MATHEMATICAL-COVERAGE-LEAN.md) and [critical review with source assessment](../../../../../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/ROOT-MATHEMATICAL-COVERAGE-REVIEW.md). Review was performed by the same agent; no independent review is claimed.
