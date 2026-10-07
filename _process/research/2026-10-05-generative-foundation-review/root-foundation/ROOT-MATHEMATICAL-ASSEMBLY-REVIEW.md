# Uniform indexed assembly: independent review

7 October 2026. AI-authored review under the [nondual method](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/NONDUAL-METHOD.md), continuing the [admission assessment](ROOT-MATHEMATICAL-ADMISSION-REVIEW.md). The intended full higher-order target is retained. Mathematical claims are attached to the new Lean modules; the proposed warrant for admission is philosophical. Final verification is recorded below.

## 1. A stronger bounded proposal

The [affirmative argument](ROOT-MATHEMATICAL-ASSEMBLY-ARGUMENT.md) advances beyond no-arbitrary-exclusion. Given an independently admitted index and whole relation `R(i,x)`, its projection retains whether some witness relates to `x` while omitting the witness's identity. The result's memberships require no independent choices beyond that relation. This supplies a concrete reason for admitting a derivative extensional role.

The crucial qualification is **relative**. Determinate membership does not by itself establish admission into every possible quantifier domain. The argument must defend abstraction of the specified relation and the resulting predicate's role. This need not posit a separate mathematical realm: knowing, representing, assembling and interpreting are differentiated relationships within the same unfolding. What remains supplied to this explanation is not thereby outside generative reality.

I accept this as a substantive bounded philosophical proposal supported by an explicit identity mechanism. I do not accept it as an already necessary rule of the minimal root or a derivation of arbitrary family availability.

## 2. The identity mechanism retains the actual output

[RelationalAssembly.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/constitution/assembly/formal/RelationalAssembly.lean) represents witness occurrences `(i,x)` satisfying `R`, then identifies occurrences exactly when their outputs `x` agree. `abstract_eq_iff` checks that identity. `output_realize` and `realize_output` establish inverse maps between this quotient and `Support R`, the subtype of outputs having a witness. `projection_iff_output` and `projected_content_unique` fix the precise resulting membership. `projection_reindex` preserves projection under a supplied surjective reindexing, not under arbitrary removal of indices.

The admission interface now retains a presentation's output map into the fixed base `A`. `CorrespondenceClosed` requires both inverse maps and a commuting output map. This matters: admission of an isomorphic carrier alone would omit the predicate's role over its base. `support_admitted` concludes admission of the support **with its inclusion into `A`**, conditional on admission of the whole witness presentation, output-abstraction closure and correspondence closure.

These are exact conditional resources. The theorem does not discharge them or automatically place the projection in a separately specified `PredicateAdmission` family. Relating this presentation-admission interface to the intended predicate quantifier domain remains part of the correspondence obligation. The construction uses supplied whole relations, quotient structure and classical witness choice; no effective recovery from finite observations is claimed.

## 3. Parity distinguishes independent formation from reconstruction

[IndexedAssembly.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/constitution/assembly/formal/IndexedAssembly.lean) supplies a useful calibration. `parityStages` starts empty and adds `2*n` at step `n+1`, without accepting an arbitrary target predicate as a parameter. `parity_stage_membership`, `parity_stages_increasing` and `parity_union` check the finite-stage content, increase and exact union. The earlier finite/cofinite family admits every stage and excludes that union.

This establishes more than reconstructing parity after selecting all its finite parts from a supplied predicate: the recurrence determines the family without asking for target membership answers. It still relies on the supplied natural numbers, arithmetic, recursive interpretation and union semantics. It is neither a proof that all physical stages occur nor an explanation of those foundational resources from nothing.

The modules are explicitly connected: `parity_projection` identifies projection of the actual stage-membership relation with parity, and `parity_iff_output` identifies parity membership with the output of a witness quotient for that same recurrence. This checks the proposed identity mechanism on the concrete formation rather than leaving the two results unrelated.

The separate theorem `parity_admitted` assumes **global** `FiniteChainClosed` and finite admission. Its antecedents already have full predicate strength on `Nat`. Consequently that theorem cannot justify a weaker local admission rule. The bounded positive argument instead combines the explicit recurrence and exact union with the separately defended relative abstraction principle.

## 4. Countable indexing does not reduce the full commitment

`FiniteChainClosed` ranges over every ambient increasing sequence of finite predicates. `full_iff_finite_chain` proves that, on `Nat`, this closure together with admission of every finite predicate is equivalent to fullness. `chain_iff_directed_given_finite` connects it to the previous all-directed-family principle under the same finite-admission premise.

`prefixChain S` makes the dependency visible: its stage membership is `S a ∧ a < n`. The arbitrary target selects the entire sequence, whose union recovers it. Calling the resulting family uniform because one formula describes its stages does not independently admit the parameter `S` or the whole relation that formula defines.

Thus the proposal has two different tasks: justify projection for admitted whole families, and justify every family needed for full coverage. The first does not finish the second. These equivalences concern `Nat`; no general reduction for arbitrary uncountable carriers is claimed. The earlier [closure resolution P2](MATHEMATICS-CLOSURE-RESOLUTION.md#proposition-p2--which-union-closure-yields-all-subsets) already states the increasing-sequence distinction as a hand argument. This round checks and sharpens its application rather than discovering it anew.

## 5. The strongest matched counteraccount

A structural account can retain the complete higher-order domains, actual arithmetic recurrence, witness relation, output quotient, projection and every established dependence of membership on those data. It need not pretend the instances are unrelated or move mathematics outside the unfolding. It explains the abstraction through the structural role of existential incidence and extensional identity, while leaving the ultimate status of full admission as a further structural principle.

The generative argument improves on a rival that simply lists unrelated instances: the common formation rule explains their relation. But the matched rival preserves that achievement. It disputes whether this explanation establishes the minimal root's unique priority or independently warrants every required family. It owes a justification for its own admission principle, so its survival is not a completed alternative foundation.

Finite/cofinite restriction is a diagnostic for weaker closure conditions, not this full-target rival. Likewise, refusing predicate reification in a restricted language can illustrate the difference between formulas and admitted objects, but cannot refute the intended full semantics while silently changing it.

## 6. Actionable result and verification

The useful next work is to identify an independently justified repertoire of whole relations and the admission of their output-preserving abstractions, then test whether a proposed general extension adds previously unexplained family resources. The parity construction calibrates that discipline. It does not make another arbitrary target-dependent prefix representation a new foundational explanation. Unique root dependence remains a separate comparison after full coverage is warranted.

The [focused source assessment](ROOT-MATHEMATICAL-ASSEMBLY-SOURCES.md) supplies a relevant primary example of explicit operation, definedness and argument-range accounting. It supplies neither our root's conclusion nor a universal impossibility result.

**Accepted and frozen.** Both formal modules and the [indexed correspondence](ROOT-MATHEMATICAL-ASSEMBLY-LEAN.md) have been reviewed. The [fresh isolated Lean 4.29.1 receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/constitution/assembly/verification.json) passes with **31 new named theorems and 48 declaration audits**: `IndexedAssembly.lean` contributes 19/26; `RelationalAssembly.lean` contributes 12/22. Dependencies are only `Classical.choice`, `Quot.sound` and `propext`, with no custom axioms or holes. Four inherited modules were rebuilt from prior-receipt-matching bytes.

This review independently matched all 18 recorded source, inherited-source, prior-receipt and support-file hashes, with no mismatch. Frozen source hashes are `209a9e161b5aacd740582e16da474df1fb4f4792b9315c6f307d25a3d1d9e020` and `2951d70f850649b9b89ab2d64adb3d47e8be27f9494d8169b36aaeddd08c0c66`, respectively. No unchanged successful compilation was repeated. The review adds no unverified mathematical theorem and finds no substantive blocker at this conditional scope.
