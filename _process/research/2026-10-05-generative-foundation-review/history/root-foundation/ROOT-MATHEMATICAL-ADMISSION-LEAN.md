# Predicate admission: exact closure strength and a proper finite comparison

7 October 2026, Asia/Bangkok. AI-authored correspondence record for [Admission.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/constitution/admission/formal/Admission.lean), namespace `PredicateAdmission`. This formalizes and refines the earlier [closure study's P2/P3 arguments](MATHEMATICS-CLOSURE-RESOLUTION.md), using the existing finite-subset construction. It does not claim new underlying mathematics or that a checked closure equivalence independently warrants full admission.

The module has **34 named theorems and 50 explicitly named declarations**. It imports the frozen `CompletionExamples` development. The package's final fresh Lean 4.29.1 build passed with **52 theorems and 86 audited declarations** across this module and the separate `FunctionGraphs.lean` development. Its [verification receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/constitution/admission/verification.json) binds the checked sources and reports only `propext`, `Classical.choice` and `Quot.sound` as logical dependencies. This record's scope is the module below; it does not retrospectively validate the older closure note's full definability and cardinality arguments.

## 1. The closure condition that actually yields fullness

A candidate admission family is `C : (A → Prop) → Prop`. `IncludesFinite C` requires admission of the membership predicate of every `FinitePart A`. `Full C` requires admission of every predicate on `A`.

`DirectedUnionClosed C` quantifies over **every ambient predicate family** `D : (A → Prop) → Prop`. If `D` is nonempty and directed under inclusion, and every member of `D` is admitted by `C`, its pointwise union must also be admitted. Directedness requires the common upper bound to belong to the same family. The families are nonempty; no assumption that the carrier `A` itself is nonempty is needed.

The central checked statements are:

| Declaration | Exact result |
| --- | --- |
| `full_iff_finite_directed` | Full admission is equivalent to finite admission plus closure under every ambient nonempty directed union. |
| `directed_iff_full_given_finite` | Given finite admission, that directed-union closure is equivalent to fullness. |
| `finiteProfiles_directed` | The finite parts lying within an arbitrary predicate form a nonempty directed family. |
| `union_finiteProfiles` | The union of those finite parts is exactly the given predicate. |

The proof's input accounting is visible in `FiniteProfiles S`. It uses the existing ideal `partsOf S`, selecting all its finite members. Every element of `S` is witnessed by its singleton; union of finite parts supplies directedness. Applying the closure hypothesis therefore admits `S`.

This supplies an exact sufficient principle and establishes its strength under finite admission. The arbitrary target `S` enters the ambient family specification. The theorem does not show that an independently restricted process can generate, identify or admit every such family. Restricting the family quantifier to internally available, definable or effective families changes the hypothesis. Calling the unrestricted family range “closure” does not remove its commitment.

## 2. A proper family satisfying substantial weaker conditions

`FiniteOrCofinite P` means that `P`, or its complement, has a finite-list witness. On the natural-number carrier it gives a concrete proper restriction, rather than a predicate whose interpretation is freely toggled.

The module proves admission of every finite predicate, the empty and universal predicates, and every singleton. `finiteOrCofinite_complement` and `finiteOrCofinite_union` establish complement and binary-union closure. `finiteOrCofinite_bijection_iff` proves that admission is preserved and reflected under the image of **any bijection**, including bijections between differently presented carriers. Its proof supplies an inverse using classical choice; no effective inverse is claimed.

`finiteOrCofinite_pattern` establishes an additional boundary: for any target predicate and any finite list of inspected elements, an admitted predicate has exactly the same membership answers on that list. The witness can be finite. Consequently this family passes every specified finite membership-pattern comparison while still being a proper restriction on the natural numbers. This is a statement about finite membership observations, not about every possible finitary sentence with unbounded quantifiers.

These properties preserve finite formation, Boolean operations and freedom of element naming. They do not include arbitrary directed-union closure. The mathematical comparison therefore tests what those weaker conditions actually supply; it is not a rival claiming to preserve the full second-order target while omitting some of its predicates.

## 3. Explicit parity obstruction

`Even n` is the concrete predicate `n % 2 = 0`. `even_not_finite` and `even_complement_not_finite` use a bound on any alleged finite list: a sufficiently large even number, or a sufficiently large odd number, lies beyond that bound. Thus `even_not_admitted` and `finiteOrCofinite_not_full` establish properness on `Nat`.

`parity_directed_failure` identifies the actual failed closure instance. The family of all finite parts of the evens is nonempty and directed, all of its members are finite-or-cofinite, and its union is the excluded even predicate. `finiteOrCofinite_not_directed_closed` also derives the general failure from the exact closure theorem.

This shows that finite admission, complement and union, bijection invariance and agreement with arbitrary finite membership patterns do not force full admission. It does not show that full admission is inconsistent or unwarrantable. Nor does it refute the complete generative root merely because a weaker representation permits this restricted family.

## 4. Relation to the completed higher-order reconstruction

The [higher-order correspondence](ROOT-MATHEMATICAL-HIGHER-ORDER-LEAN.md) already preserves full second-order truth when all predicates and all finite-tuple ideals are admitted. The present result identifies the extra admission contract in a directly testable form. It also supplies a nontrivial family satisfying several weaker generative and structural requirements while failing that contract.

The mathematical carrier, predicates and families are representations of selected relationships within the investigation. An ambient family quantifier is a metatheoretic resource supplied here, not evidence that the mathematical content exists outside the one unfolding. Equally, its place within that unfolding does not by itself establish why this unrestricted range must be admitted.

The remaining central obligation is to justify the full admission principle through the proposed root's independently specified content, and then establish its exclusive grounding priority against alternatives preserving that content. This module sharpens that obligation and verifies the comparison; it does not declare it discharged.

## 5. Reproduce

From the repository root:

```sh
python3 experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/constitution/admission/check.py
```

The package checker freshly compiles the inherited dependencies and this module, then audits explicitly named declarations. The receipt records the exact source bytes and logical dependencies. Automatically generated projections and recursors are checked with the full module but not separately included in the 50-declaration count. No custom axioms, proof holes, unsafe declarations or `native_decide` are used.
