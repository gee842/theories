# Dependent families: wider reconstruction and an exact admission boundary

7 October 2026, Asia/Bangkok. AI-authored continuation of [Ren's request to finish mathematical admission and coverage](../../../../sources/15-codex-theory-conversations/2026-10-07-mathematical-admission-and-coverage.md). The [preceding package](ROOT-MATHEMATICAL-COVERAGE-INTEGRATION.md) established finite simple-type admission and named-theory transport. This round extends the domain reconstruction to dependent pairs and sections and tests whether pointwise finite formation can justify whole infinite families.

**The positive extension is checked; the proposed shortcut to full admission fails at its stated scope.** Finite bases with finite fibers have finite dependent-pair and section domains. Sections of arbitrary supplied families have exact finite-graph completion representations. But admitting the supports of every ambient family of finite fibers is already equivalent to full predicate admission. Pointwise smallness does not independently justify the whole assignment.

The [formal package](../../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/constitution/families/README.md) passes a fresh Lean 4.29.1 build with **33 new theorems and 52 declaration audits**. The [affirmative argument and primary-source assessment](ROOT-MATHEMATICAL-FAMILIES-ARGUMENT.md) and [independent internal review](ROOT-MATHEMATICAL-FAMILIES-REVIEW.md) are integrated here. This is internal AI collaboration, not external peer review or a claim of mathematical novelty.

**有限基底与有限纤维，足以把有限准入推广到依赖对和截面。任意给定依赖族的截面也有经过 Lean 检查的有限图理想重构。但“每个位置只有有限选择”并不独自说明整个族怎样获得根据；任意空／单点纤维的整体安排，已经可以携带任意谓词。普遍根基论证仍须说明这一整体安排的根据。**

## 1. What is a dependent family?

A family `B(a)` specifies the permitted values at each position `a`. The values can vary in type. For example, at natural number `n`, the family `Fin (n+1)` permits indices from zero through `n`. A dependent pair records a position and one value belonging there; a section selects a value at every position.

This distinction represents related roles within one configuration. It does not introduce independently existing index and value realities. The new correspondence retains the position belonging to each value and the evaluation of a section there; a bare bijection of total carriers would leave that relationship unspecified.

The example is calibrated in Lean: the constant-zero section of `Fin (n+1)` has the asserted graph membership and decoded value. The family `Fin n` admits no total graph because the fiber at zero is empty. Natural numbers and these families are supplied to these examples; their foundational admission is not derived by the examples.

## 2. Finite dependent coverage

`sigma_finite` combines a supplied finite base cover and finite covers for its fibers into a finite dependent-pair cover. `sections_finite` proves the complete section type finite under those same hypotheses, including empty cases. Its proof embeds sections into an ordinary finite function carrier and uses classical representative selection. This is a finite-cover theorem in the ambient classical type theory, not a new executable dependent enumerator or an assumption-free formation account.

`finite_sigma_full_admission` and `finite_sections_full_admission` then obtain full predicate admission from empty, singleton and binary-union admission **at the resulting carrier**. These formation conditions must be supplied there; admission on the initial base alone is not a rule admitting all subsequent domains.

The base finiteness hypothesis is material. Checked examples show that singleton fibers over `Nat` can have an infinite dependent sum, and Boolean fibers over `Nat` have an infinite section type. The earlier finite simple-type theorem therefore cannot simply be applied because every individual fiber is finite.

There is also a narrower useful result: a given section over a finite base has a finite graph even when its fibers are infinite. `finite_base_graph_admitted` admits that graph under finite-predicate admission on the dependent sum. This does not assert that the entire section carrier is finite.

## 3. Reconstruction beyond finite bases

For arbitrary supplied `A` and `B(a)`, `SectionIdeal B` consists of an ideal of finite subsets of the dependent sum, with functionality and totality. The new encoder and decoder are inverse. Membership in the completed graph agrees exactly with the decoded section's value.

`functional_iff_finite` checks functionality through the ideal's finite members. `total_iff_finite_coverage` retains a global quantifier over all base positions: each position must be covered by some finite member. These are different requirements; finite-local compatibility does not erase global coverage.

Given a correspondence between each old and new fiber over the same base, `sigmaMap` and `piMap` preserve dependent pairs and sections. `transported_evaluation` proves the value correspondence at each position. Predicates on pairs and sections have ideal representations with exact membership. Quantifier transport applies along the indicated correspondences; its general binder lemma assumes the displayed pointwise predicate relation. It is not a newly derived theorem for all formulas of a dependent language.

This is a domain-level extension beyond the earlier simple-type grammar. It does not add dependent object-language syntax, substitution laws, base-changing family transport, internal universes, or a foundation-wide model theorem. In particular, the earlier named-theory truth theorem has not silently been generalized to dependent syntax.

## 4. The exact whole-family obligation

For an arbitrary predicate `P`, define `truthFibers P a` to contain a lifted proof of `P(a)`. Each fiber has at most one element and is finite. The support of the family—the positions whose fibers are inhabited—is exactly `P`. The dependent total space corresponds to the subtype specified by `P`, preserving its projection to the base.

The two checked admission characterizations say:

- Full predicate admission is equivalent to admitting supports of **every ambient family with subsingleton fibers**.
- It is also equivalent to admitting supports of **every ambient family with finite fibers**.

The family quantifiers in these statements are explicitly over `B : A → Type`. They suffice even though each fiber is small. The assignment of empty versus inhabited fibers already uses the arbitrary predicate being reconstructed. This locates the missing explanatory commitment; it is not an independent warrant for that assignment.

Separately, `section_exists_iff` identifies existence of a section with pointwise nonemptiness in the classical metatheory, using choice in the reverse direction. Existence of one section and admission of the full section space must remain distinct. Neither is established from the minimal root here.

## 5. Integrated judgment and next substantive bridge

The affirmative case gains a real relational reconstruction: varying fiber types, their complete sections, and their evaluation are accounted for under exact supplied conditions. The finite case gains a wider conditional admission result. The counterreview preserves both achievements while rejecting an inference from small individual fibers to independently warranted whole-family admission.

A matched structural account can retain the same domains, sections, projection relationships and truths within one whole while treating their admission as a structural formation commitment. It still owes its own warrant. The present theorems do not decide the direction of ultimate dependence between that account and the proposed root. The limitation is an unresolved explanation, not evidence that the supplied relationships lie outside generative reality.

The [argument's next bridge](ROOT-MATHEMATICAL-FAMILIES-ARGUMENT.md#5-one-actionable-next-bridge) is to justify **collective inductive formation**: why specified constructors and their composable finite formations warrant a domain with induction and collective quantification. A universal property can assess the role of a domain once warranted; merely postulating that its role has a realization does not discharge the existence commitment. Existing initiality work keeps its historical proof scope and is not counted as a new checked result.

The focused Martin-Löf reading is assessed in the argument note. It provides a comparator for explaining formation and inference while retaining additional inductive commitments; it is not adopted as a replacement for the full classical target. The new formal evidence remains the checked modules. The next investigation must identify a premise actually justified, rather than offer another isomorphic presentation.

Thus obligation 1 has a stronger finite result and a sharper infinite-family boundary; obligation 2 has dependent-domain coverage, without a full dependent-language or universal-foundation theorem. Independent infinite-domain warrant and unique constitution of every mathematical truth remain unproved.

## 6. Exact proof and preservation record

| Module | New theorems / audits | Correspondence and supplied premises |
| --- | --- | --- |
| [FamilyAdmission.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/constitution/families/formal/FamilyAdmission.lean) | 14 / 17 | Finite base/fiber covers; per-carrier formation; all ambient small fiber assignments in support equivalences; classical choice for section existence. |
| [DependentCompletion.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/constitution/families/formal/DependentCompletion.lean) | 19 / 35 | Supplied dependent families, all qualifying finite-part ideals, global totality, fixed-base fiber correspondences and full predicate interpretation. |

The [fresh proof receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/constitution/families/verification.json) binds both frozen sources, seven rebuilt inherited sources, four inherited receipts, the checker, toolchain and audit logs. Only `propext`, `Classical.choice` and `Quot.sound` occur; no custom axioms, proof holes or compiler warnings pass the check. Inherited theorems are not added to the new counts.

The [document receipt](ROOT-MATHEMATICAL-FAMILIES-CHECKS.json) separately checks owned links, proof bindings and preservation of 85 earlier proof assets. Shared-file additions preserve preceding content and concurrent work. No commit or repository-wide retrospective audit is made.
