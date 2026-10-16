# Independent review: induction and collective formation

7 October 2026, Asia/Bangkok. AI-authored substantive review of the [induction argument](ROOT-MATHEMATICAL-INDUCTION-ARGUMENT.md), following the [families review](ROOT-MATHEMATICAL-FAMILIES-REVIEW.md). The governing question remains whether the root independently warrants mathematical domains and their full intended content. This review follows the [nondual method](../../../../theories/becoming/chapters/NONDUAL-METHOD.md). It adds no mathematical proof and makes no claim that infinite admission is impossible.

## 1. The affirmative explanation is substantive but conditional

The strongest argument is source exhaustiveness: an instance of the proposed subject must have a finite formation from its declared seed and constructor. A predicate preserved at every formation step therefore cannot acquire a counterinstance through that formation. This explains why induction fits the subject. It does not infer truth merely from causal production, and it need not assume that every abstract instance has actually occurred or remains physically recorded.

This is an improvement over demanding separate membership explanations for every number. One common formation rule can explain the relationships among instances. Treating the domain as the role of those formations also avoids introducing an unexplained bearer behind their identity. The favorable philosophical proposal is that generic constructor meaning warrants using the whole subject as a domain of quantification and interpretation.

The outstanding step is that last entitlement. Availability of each particular formation, permission to continue, and admission of one exhaustive domain are distinct commitments. A common rule need not be a mere summary of past activity; granting its generic meaning still leaves the scope of permissible collective use to justify. Source exhaustiveness gives an informative account of induction **if** that collective subject is warranted. Calling it the intended meaning can articulate the premise but does not independently discharge it.

The proposed root concerns one unfolding, including mathematical practice and its possibilities. A metatheoretic resource supplied to this local proof is not thereby an entity outside that unfolding. The limitation concerns the present explanation of its entitlement, not an established division between mathematical and generative realities.

## 2. The formal test separates coverage from identity

[InductiveDomain.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/constitution/induction/formal/InductiveDomain.lean) starts with a supplied carrier, a zero and a total successor. `Generated` means that an element is the result of some natural-number-indexed finite iteration; `NoJunk` requires this of every carrier element. `generated_least` proves invariant preservation by induction on that ambient iteration index. The proof correctly exposes its dependency on Lean's natural numbers and induction.

`fullInduction_iff_noJunk` characterizes coverage through induction over arbitrary metatheoretic predicates. Constructor separation is independent: successor must be injective and never equal zero. With both separation and coverage, `naturalEquivalence` supplies inverse maps preserving zero and successor; the inverse uses classical choice. `unique_recursion` establishes the unique constructor-preserving interpretation into any supplied target of its stated type. These are precise structural results, not an independent construction of the ambient natural-number resource.

The diagnostics preserve their weaker scope. The Boolean toggle is generated and satisfies full induction, but violates separation. The `Option Nat` construction preserves separation while `none` is an unreached fixed point, violating coverage. They identify what individual hypotheses do. Neither preserves the whole ordinary-number subject while refuting its intended constitutive explanation. A recurrent endpoint and a count of construction steps also answer different questions within the same process; their identities should not be conflated.

## 3. A genuine reduction in the predicate premise

`selected_iff_noJunk` is the most useful narrowing. It assumes a selected predicate family and admission of the generated-orbit predicate. Under that hypothesis, selected induction is equivalent to coverage. The forward direction applies induction to that one predicate; the reverse uses finite derivation to preserve any predicate in the selected family.

Thus this test does not require independent admission of every predicate as an object. The all-predicate elimination principle in the metatheory and a full internal powerset sort are different claims. Nor should the narrowing be overstated: it supplies neither the selected induction rule nor the generated orbit's availability from the root. The orbit has a common specification, but quantifies over ambient natural numbers.

The `OnlyGenerated` example makes the logical separation explicit. It admits precisely the generated predicate on ordinary naturals, satisfies selected induction and excludes the false predicate. It is a deliberately thin comparison, not a Henkin model, a comprehension-closed logical domain or a recommended admission policy. Its role is to rule out a mistaken dependency on full predicate admission, not to warrant the collective subject.

## 4. Initiality has an exact comparison range

[Initiality.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/constitution/induction/formal/Initiality.lean) defines initiality through unique constructor-preserving maps into every supplied zero/successor carrier in the same universe. `initial_iff_generated_separated` identifies it with coverage and separation.

The converse test is informative. `initial_noJunk` uses the generated subtype as a target and uniqueness of endomorphisms to show that its inclusion covers the carrier. `initial_nat_hom` tests the universe-lifted natural numbers; together with coverage, this forces constructor separation. These target objects are part of the quantified range. An account admitting only a smaller collection of targets has not supplied this same universal property.

The result checks a restricted instance of the earlier [iteration presentation](MATHEMATICS-GENERATIVE-PRESENTATIONS.md#a-universal-structure-for-iteration) and [no-junk/no-unforced-identity analysis](MATHEMATICS-CLOSURE-RESOLUTION.md#proposition-i3--no-junk-and-no-unforced-identity-are-equivalent-to-initiality). Those broader notes retain their historical hand-proof scope. This module does not migrate every signature, equation presentation or semantic result in them. It also characterizes an already supplied source carrier; it does not establish initial-object existence from a definition of the universal role.

## 5. The matched rival and next discriminating question

A substantive structural account can preserve the same natural numbers, constructors, induction, full mathematical targets and actual formation of mathematical practice within the whole. It treats the structural or inferential meaning of finite iteration as the reason particular construction activities instantiate arithmetic. The generative proposal instead seeks to explain that structural entitlement through the common organization of formation itself. This is a disagreement about explanatory priority and collective warrant, not a change of truth values or a free reassignment of a grounding label.

The generative proposal has explained something when it relates instances through their formation instead of assuming unrelated objects. The rival can accept those relationships. To establish unique root dependence, the next argument must show what in the rival's priority account fails, or establish an independently warranted equivalence of the full constitutive explanations. Both accounts owe an explanation of collective entitlement; neither wins merely by calling its rule structural or generative.

The present gain is consequently a narrower induction interface and a checked separation of formation coverage, constructor identity and universal interpretation. The unresolved infinite-domain warrant is explicit. Further initiality encodings using the same admitted iteration resource will not close it. A new meaning-based defense must explain why generic finite formation permits the intended whole-domain use, without silently importing that use. Even a successful defense would leave full predicate admission and universal mathematical coverage to address.

## 6. Verification and evidence status

Both modules were read in full. The frozen [verification receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/constitution/induction/verification.json) records a passed fresh isolated Lean 4.29.1 build: **28 named theorems and 47 declaration audits**, comprising `InductiveDomain` 24/38 and `Initiality` 4/9. The sources import only bundled `Std` and one another. Their reported dependencies are limited to `Classical.choice`, `Quot.sound` and `propext`, with no custom axioms or holes.

I independently recomputed all **eight** recorded file bindings; every hash matched. The source hashes are `3f18a6d422129f3fcc1195f6b142984cd03567d55d42a0ca1e701478469d90e4` and `d492efce5893d189a4d8c78c3adae0b15d4d41e1b315dd531096260d0af83b6d`, respectively. Thirty-four audited declarations have empty printed axiom lists, including the selected-induction equivalence. This does not remove the natural-number type, its induction principle, dependent types or the logical framework in which those declarations are checked.

The formal correspondence is accepted at the scopes above; no substantive blocker was found. No source files or earlier notes were edited for this review. The review uses the repository's recorded genealogy and the affirmative argument's credited source comparison; it has not independently retrieved a new primary source in this round.
