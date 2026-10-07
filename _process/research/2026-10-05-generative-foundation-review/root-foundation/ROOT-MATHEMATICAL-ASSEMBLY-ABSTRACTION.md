# Relational assembly: identity and admission of a derived presentation

7 October 2026. AI-authored correspondence record for [RelationalAssembly.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/constitution/assembly/formal/RelationalAssembly.lean). Its **12 new theorems and 22 named declaration audits** form part of the package's **31-theorem, 48-audit** fresh Lean 4.29.1 [verification](../../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/constitution/assembly/verification.json).

The purpose is to test the identity mechanism proposed by the [affirmative argument](ROOT-MATHEMATICAL-ASSEMBLY-ARGUMENT.md). It does not derive availability of every indexed family. The [integration](ROOT-MATHEMATICAL-ASSEMBLY-INTEGRATION.md) records its foundational scope alongside the [independent review](ROOT-MATHEMATICAL-ASSEMBLY-REVIEW.md).

## 1. The supplied relation and its derivative object

For `I A : Type u` and `R : I → A → Prop`, `Witness R` consists of pairs `(i,a)` with evidence of `R i a`. These are occurrences in the supplied mathematical relation; their use does not claim that every occurrence has been physically realized.

`witnessSetoid` identifies witnesses precisely when their output values in `A` agree. `Assembly R` is its quotient. `Support R` is the subtype of values with some witness, and `Projection R a` states `∃ i, R i a`.

`output` maps an equivalence class to its witnessed value. `realize` chooses a witness of a support value and returns its class. The two inverse laws, injectivity and surjectivity are checked. Choosing a different witness cannot alter the class because the output is the same. The implementation of `realize` uses classical choice; no effective search algorithm follows.

`abstract_eq_iff` makes the identity condition exact. `projection_iff_output` characterizes projected membership by occurrence as a quotient output, and `projected_content_unique` proves that any predicate with exactly these outputs equals the projection. Thus the quotient retains the intended membership role and removes only distinctions between its witnesses.

`projection_reindex` shows that a supplied surjective change of index preserves the projection. Surjectivity matters: deleting witnesses without preserving coverage need not preserve the output.

## 2. Admission preserves the output role

The admission condition has type `(X : Type u) → (X → A) → Prop`. It concerns a presentation together with its output map into the fixed base. A bare carrier or a bijection ignoring those values would not suffice to preserve the mathematical subject.

`OutputAbstractionClosed` requires admission of the quotient presentation whenever the entire witness presentation is admitted. `CorrespondenceClosed` permits transport along inverse maps whose outputs commute. `support_admitted` concludes admission of `Support R` **with its inclusion into `A`**, given these two closure commitments and admission of the whole witness presentation.

The theorem does not justify those hypotheses. It also does not automatically assert admission of `Projection R` into a separately chosen predicate-quantifier family. Identifying the output-preserving presentation with an object in that family needs a declared correspondence and warrant. This is a conditional account of derived presentation admission, not an implicit full-comprehension principle.

## 3. Connection to the explicit recurrence

The companion [indexed module](ROOT-MATHEMATICAL-ASSEMBLY-LEAN.md) defines `parityStages` without an arbitrary target-predicate parameter. `parity_projection` identifies projection of its stage-membership relation with the even predicate. `parity_iff_output` then identifies even membership with output from the actual witness quotient for that recurrence.

This connects the positive formation example to the abstraction mechanism. The inherited natural numbers, arithmetic, interpretation of the whole recurrence, quotients and the admission interface remain explicit. The result does not establish that all subsets have such independently warranted formations.

## 4. Verification scope

The checker compiled frozen new sources and four receipt-matching inherited modules in an isolated directory, then audited every explicitly named new declaration. Only `propext`, `Quot.sound` and `Classical.choice` were reported. No custom axioms, proof holes or unsafe bypasses occur. Root and both collaborating proof/review agents read the final relational module; this is internal AI review, not external peer review.
