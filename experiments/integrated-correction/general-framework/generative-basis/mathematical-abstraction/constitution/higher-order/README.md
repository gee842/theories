# Higher-order truth through predicate completion

7 October 2026. This package completes the conditional higher-order semantic reconstruction requested by Ren. It proves truth preservation when predicates are represented as ideals of finite approximations, including recursive predicate types and full function types. It supplies neither an executable truth decision procedure nor a derivation of full domain admission from the generative root.

- [SecondOrder.lean](formal/SecondOrder.lean): arbitrary finite relation arities, mixed individual/relation quantifiers, individual and predicate equality, full and selected-domain satisfaction transport, corresponding fullness, and a finite-predicate counterexample. **25 named theorems, 57 declaration audits.**
- [TypedTruth.lean](formal/TypedTruth.lean): a supplied base bijection extended recursively through predicate completion and full function spaces; lambda/application transport, equality and membership, quantification at every finite simple type, all-formula truth preservation, semantic comprehension and a higher-type example. **18 named theorems, 40 declaration audits.**

The [integrated research result](../../../../../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/ROOT-MATHEMATICAL-HIGHER-ORDER-INTEGRATION.md), [second-order correspondence](../../../../../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/ROOT-MATHEMATICAL-HIGHER-ORDER-LEAN.md), [finite-type correspondence](../../../../../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/ROOT-MATHEMATICAL-HIGHER-TYPES.md) and [independent internal review](../../../../../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/ROOT-MATHEMATICAL-HIGHER-ORDER-REVIEW.md) state the exact hypotheses and philosophical limits.

## Scope

Second-order relation variables have types recording every finite arity, including zero. The formula language contains relation application to individual variables, equality, negation, conjunction and both individual and relation existential quantifiers. Universal quantifiers have checked derived semantics. Predicate and ideal domains may be restricted only under the explicit correspondence required by the selected-domain theorem. An arbitrary selected domain is not asserted to satisfy Henkin comprehension conditions.

The separate finite-type grammar is `base`, `arr s t` and `pred s`, with arbitrarily deep finite nesting. Its terms contain variables, application and lambda abstraction. Its formulas contain equality at any type, predicate membership, Boolean constructors and quantification at any represented type. Each predicate type is replaced by an ideal completion of finite subsets of its recursively interpreted carrier. Arrow types remain full function spaces; the construction does not derive them from finite function graphs. Types are not themselves objects of a quantified internal universe. Dependent types, a built-in truth-value object type and a formula-to-predicate term constructor are outside this grammar. `formula_comprehension` instead proves semantic realization of every formula-defined extension.

All predicates, ideals and full function spaces used by these semantics remain admitted in Lean's metatheory. A base bijection is supplied; the identity map gives reconstruction over the same base. The theorem covers the entire declared formula language, not a collection of sample formulas. Its truth-preservation proof is not a procedure deciding those truths.

## Reproduce

From the repository root with Python 3 and Lean 4.29.1 installed:

```sh
python3 experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/constitution/higher-order/check.py
```

The checker compiles frozen source bytes in a fresh temporary object directory. It first compiles the unchanged `IdealWarrant`, `CompletionRole` and `CompletionExamples` dependencies, checking their source hashes against the older completion receipt. It then builds both new modules and the saved [audit driver](verification/KernelAudit.lean).

The [receipt](verification.json) records **43 new named theorems and 97 explicitly named source-level declaration audits**. Every named definition, abbreviation, structure, inductive declaration and theorem in the two new modules is audited. Automatically generated projections and recursors are compiled with their module, but not separately counted. The only reported dependencies are the standard `propext`, `Quot.sound` and `Classical.choice`. No custom axioms, proof holes, unsafe declarations or `native_decide` are used. Inherited completion results are freshly compiled dependencies and are not counted again as new results.
