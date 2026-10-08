# Dependent families: independent coverage and admission review

7 October 2026. AI-authored independent-agent review of the finite coverage result and its dependent-family continuation, under the [nondual method](../../../../theories/becoming/chapters/NONDUAL-METHOD.md). No new proof is proposed in this note. Mathematical claims refer to the reviewed Lean declarations; philosophical appraisal is distinguished from their conditional conclusions.

## 1. Independent audit of the preceding coverage result

Both final sources of the [36-theorem coverage package](ROOT-MATHEMATICAL-COVERAGE-INTEGRATION.md), its correspondence, same-agent review and receipt were read. All **23** recorded source, inherited-source, prior-receipt and support-file hashes independently match the actual files. Its **36 named theorems and 66 declaration audits** are accepted at the recorded Lean 4.29.1 scope, without repeating an unchanged successful build. This is a later independent internal AI review; it does not rewrite the original report's honest statement that its initial review was by the implementing agent.

The finite-family construction is genuinely independent of a target predicate: `selections` generates all selections from a supplied covering list. Its proof of coverage uses classical cases and propositional extensionality, not a procedure deciding an arbitrary proposition. The base and finite cover remain supplied. Function assignments use classical equality and a seed when the function space is inhabited; empty cases are handled.

One scope qualification matters throughout the continuation: finite-type admission applies the empty, singleton and binary-union premises **at each resulting carrier**. The theorem does not derive a universal admission policy for all carriers from one policy on the base. The generic named-theory result likewise retains full interpreted types, compatible named values and a fixed metatheoretic universe. Backward interpretation supports its claimed model-class coverage. No hidden theorem flaw was found.

## 2. The actual new finite-family result

[FamilyAdmission.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/constitution/families/formal/FamilyAdmission.lean) separates a supplied base `A` from a supplied assignment `B a` of possible values at each base position. These are related roles within the represented organization: the total domain retains the index together with its value, and a section chooses a value of the appropriate fiber at every index. They need not be independent foundational kinds.

`sigma_finite` and `sections_finite` establish finite covering lists for dependent pairs and sections when the base and every fiber have finite covers. The sum construction uses classical choice of fiber covers. The section proof injects sections into an ordinary finite function carrier and classically chooses representatives; it does not implement an executable dependent enumerator. `finite_sigma_full_admission` and `finite_sections_full_admission` then apply the earlier finite-formation result to these carriers, with their own explicit formation premises.

Finiteness of fibers alone is insufficient for these conclusions. The module supplies two exact checked boundaries: singleton fibers over `Nat` have a nonfinite total dependent sum, and Boolean fibers over `Nat` have a nonfinite section carrier. These results identify the missing finite-base condition; they do not establish that infinite dependent domains are inadmissible.

This is useful domain-level coverage beyond the previous simple-type constructors. It is not yet a formal syntax and semantics for dependent type theory, and it does not add a new quotient treatment. The earlier [relational abstraction result](ROOT-MATHEMATICAL-ASSEMBLY-ABSTRACTION.md) retains its separate quotient scope.

## 3. Small fibers can already specify arbitrary support

The strongest admission boundary is `full_iff_subsingleton_support`, together with `full_iff_finite_support`. For a predicate-admission condition `C` on `A`, full predicate admission is equivalent to admitting the support of **every ambient** family `B : A → Type` with the respective fiber restriction. The small universe of the fibers does not remove this quantification over their entire assignment.

The proof explicitly forms `truthFibers P a = PLift (P a)` from arbitrary `P`. Such a fiber has at most one element and a finite cover; whether it has an element already follows the membership condition encoded by `P`. `support_truthFibers` recovers precisely `P`. `truthFamilyMap` additionally identifies its total dependent domain with the subtype selected by `P`, retaining the projection into `A` through `truthFamily_projection`.

The result therefore tests projected-support admission, not a claim that arbitrary dependent-product formation alone yields predicates. It shows where the content enters: the whole fiber assignment can encode all membership choices even when each fiber is extremely small. Local simplicity is not an independent warrant for the global assignment. This is a valid boundary theorem, not a circular mathematical proof or a refutation of a richer root that independently warrants those assignments.

`section_exists_iff` concerns a different question: one section exists precisely when every fiber is nonempty, in the stated classical setting. Its reverse direction invokes choice. It neither supplies the full section range from the root nor asserts that having a section admits its domain, all other sections, or every predicate on them.

## 4. Dependent graph reconstruction and its exact semantics

[DependentCompletion.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/constitution/families/formal/DependentCompletion.lean) represents a section by an ideal of finite subsets of the total dependent domain. Functionality compares outputs in the **same** fiber. `functional_iff_finite` uses directedness to place conflicting outputs in a common finite member; totality separately requires some output at every index. Encoding and decoding are inverse, with classical choice in decoding.

`graph_finite` needs only a finite base to make each supplied section's graph finite; its fibers may be infinite. This does not make the full section carrier finite in that case or enumerate all its sections. `finite_base_graph_admitted` also retains finite-predicate admission on the total dependent domain.

Fiberwise inverse maps induce dependent-sum and section correspondences **over a fixed base**. Evaluation retains the appropriate fiber. The concrete predicate maps preserve membership on dependent pairs and sections. The general `bimap_quantifiers` and its section-predicate instance transport quantifiers under an explicit pointwise correspondence between their two predicates; that correspondence is not derived for a new dependent object-language. These statements must not become an all-formula theorem for dependent syntax, a change-of-base theorem or an internal-universe interpretation.

The examples use actual varying fibers: a zero section of `Fin (n+1)` has the stated graph and decoded value, while the empty fiber `Fin 0` prevents totality for the family `Fin n`. They connect the representation to both successful and impossible section formation without supplying a truth oracle. Whole families, all qualifying ideals and global totality remain explicit resources.

## 5. Foundational interpretation and matched criticism

The positive result is a broader common representation and finite admission argument, preserving how a value depends on its base position. It would be an error to replace this with a bare bijection between total carriers that forgets their projection. The actual fiberwise maps avoid that loss.

The remaining universal question concerns the admission of the whole assignment and its complete section range. A matched structural account can accept exactly the same bases, fibers, dependent pairs, sections, projections, graph ideals and local dependencies. It can also locate mathematical formation within the same unfolding. It regards full family admission as a structural formation commitment while disputing whether the minimal generative root independently explains it. This is an alternative account of the same relational content, not a freely switched grounding predicate or a restricted domain masquerading as the full target. It owes justification for that commitment too.

The support theorem sharpens this comparison: a universal defense cannot rest solely on each fiber being finite or having at most one inhabitant. It must justify their arbitrary pattern of availability. Conversely, it need not produce a separate finite description of every family member; the [whole-family reassessment](ROOT-MATHEMATICAL-FAMILY-WARRANT-REASSESSMENT.md) permits a common explanation of the full range.

The [affirmative argument](ROOT-MATHEMATICAL-FAMILIES-ARGUMENT.md) proposes collective admission of inductively formed finite objects as a more limited premise to investigate. Its distinction between the existence of that whole domain and a universal property's characterization of an already supplied domain is appropriate. The proposal has not yet discharged independent infinite admission; accepting an inductive collective would also leave arbitrary predicate and family ranges to justify. Its focused primary-source assessment is credited as that author's reading, not an additional independent retrieval by this review.

Further domain coding alone will not supply this missing warrant. A future dependent-language correspondence could close a genuine representational omission, but it must be identified as such. Neither that extension nor the present finite closure settles unique constitutive priority. No general impossibility conclusion follows.

## 6. Verification status

Both new sources were read in full. The final [verification receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/constitution/families/verification.json) records a passed fresh isolated build on Lean 4.29.1: **33 new named theorems and 52 named declaration audits**, comprising `FamilyAdmission` 14/17 and `DependentCompletion` 19/35. The only reported dependencies are `Classical.choice`, `Quot.sound` and `propext`; there are no custom axioms or holes. Seven inherited modules were rebuilt from bytes matching their earlier receipts.

I independently recomputed all **26** file bindings in this receipt, covering new sources, inherited sources, inherited receipts and supporting files; every hash matched. The two new source hashes are `932385b98b68ed960ed9fea04ec5df22714094690d9cbc02ebd055271aec45df` (`FamilyAdmission`) and `8b8688748f9cf7b5136c1e6eeef3d966f5b50cfc5d1462d7f901027d6924bef6` (`DependentCompletion`).

The source-to-claim correspondence is accepted at the scopes above. No substantive blocker was found. No source files or earlier research notes were edited for this review.
