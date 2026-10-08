# 普遍唯一性的另一道实质边界 / A first-order wall for universal uniqueness

2026-10-08，Asia/Bangkok。Direction: Yongxu Ren; argument, formalization and counterreview: AI-authored. This is the independently authorized explanatory-uniqueness investigation, not a reopening of completed normative or support-maintenance results.

**Result:** 33 new Lean theorems establish that agreement on every finite first-order formula in the identity/step/joint signature, even through one coherent elementary embedding, does not force native isomorphism. The two explicit worlds are wholly root-reachable and have genuine joint triples. A positive repair is also checked: an elementary map is an isomorphism exactly when it covers the target carrier. That coverage does not follow from elementary truth preservation. This attempted route has reached a proved wall; universal generative necessity itself remains open.

[Current chapter §§77–82](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/EXPLANATORY-NECESSITY.md#77-回到普遍唯一性把解释语言加强到底) · [Ren’s instruction](../../../../sources/15-codex-theory-conversations/2026-10-08-generative-explanatory-necessity.md#延续普遍唯一性直到遇到实质边界--continue-universal-uniqueness-until-a-wall) · [Scoped integration checks](EXPLANATORY-FIRST-ORDER-WALL-CHECKS.json).

## 1. Which universal inference is being tested?

Earlier results recover a fixed native relation from sufficiently separating questions and prove relative uniqueness for exact/reduced presentations over an already specified common case domain. Branching, jointness and support studies identify concrete distinctions that stated explanatory promises require. They do not yet imply that two independently presented, fully reachable worlds must have the same carrier and native relational structure.

The attempted strengthening is:

> If all finite relational truths agree, including identity, nested branching, joint realization and whole-domain quantifiers, then a unique native structure follows up to isomorphism.

We test this claim in a richer language than the earlier finite modal joint tests. We do not identify it with “all possible truths” or define unrestricted sufficient explanation to mean first-order adequacy. The first-order restriction is exactly what the wall diagnoses.

## 2. Language, hypotheses and correspondence

`Formula n` allows equality, directed steps, ternary joint participation, negation, conjunction and existential quantification. Universal quantification and the other usual Boolean connectives are expressible. Every formula is finite, but there is no common bound on length, number of variables, nesting or quantifier depth. Quantifiers range over the entire native carrier, not an inspected finite sample. There are no function or primitive observation symbols; the event sort is Unit and the old observation sort Empty. This is a specified relational signature, not every possible vocabulary.

`completeModel X` has `step x y ↔ x ≠ y` and `joint x y z ↔ x ≠ y ∧ x ≠ z ∧ y ≠ z`. The carrier represents positions within a single relational unfolding. A root is a designated position; a parameter is a named position in the same world. Neither is a separate observer/substance/environment. Root and successor roles are relational; every position is reachable by zero or one step. The joint predicate records simultaneous distinct participation; it does not additionally encode the earlier exclusive-support acquisition law. The simple law is supplied for this rival, not derived as the universally necessary law of reality.

`Fresh X` says every finite tuple omits a position. `Matches` means two finite tuples have the same equality pattern. The proof extends such a correspondence in either direction: reuse a matched old position, or choose a position outside the finite tuple. Induction on the formula then preserves all its truth. This is finite-context back-and-forth, not the existence of a bijection on the entire worlds.

A checked translation embeds every earlier `Test Unit Empty` into the new language. Naming a partner also distinguishes actual unequal positions by an identity formula. Thus the counterexample is stronger than merely erasing branches or identity. It neither asserts that all positions are literally identical nor assumes a primitive atom predicate for each one.

## 3. Two generated worlds with the same answers

Take A = Nat and B = Nat → Bool. Both satisfy `Fresh`: a finite list of natural numbers has an upper bound, while a finite list of streams misses a stream obtained by changing its ith entry at coordinate i.

All sentences agree between the complete relational worlds A and B. All formulas with a designated root agree as well, using root 0 in A and `oneHot 0` in B. Every position of both worlds is generated from its root. Each root has joint partners. More strongly, the explicit injection

`oneHot n k = decide (k = n)`

preserves every formula for every finite parameter tuple taken from A. One map works for all these questions and all tuples. No independently chosen encoding per formula is needed. An arbitrary target position can still be matched locally against a finite tuple; that local matching is not a surjectivity claim about `oneHot`.

There is nevertheless no surjection from A to B. For any proposed enumeration f, the stream `d n = !(f n n)` differs from its nth listed stream at n. Therefore there is no bijection and no native relational isomorphism, regardless of how we choose a candidate map. The obstruction is not just that the particular oneHot map happens to miss something.

Every target position participates in the relations and is reachable. No unreachable component or inert padding is used. The difference concerns the size of the whole differentiated world, not an arbitrary extra predicate toggled while its intended constitutive relations are omitted.

## 4. Positive repair and the premise it exposes

For **any** two models of this Unit/Empty relational signature, `Elementary m q f` says f preserves and reflects every first-order formula with every finite source tuple. Equality yields injectivity. Atomic step and joint formulas yield exact preservation and reflection of those relations. If f is also onto, these conditions give an isomorphism.

Lean checks `Elementary f → (Isomorphism f ↔ onto f)`. This is an exact characterization for a supplied elementary map, not a minimal premise theorem among all possible reconstruction methods. The reverse implication under this hypothesis reads the coverage field of isomorphism; it does not derive coverage for free.

The oneHot example satisfies elementary preservation and fails coverage, while Cantor rules out every alternative covering map. Thus adding more formulas of the same first-order language, including unboundedly many of them, cannot recover the missing global correspondence. Coverage is a substantive additional requirement.

## 5. A real truth outside this explanatory language

`Enumerable X := ∃ f : Nat → X, ∀ x, ∃ n, f n = x` is true of A and false of B. This is a global mathematical property stated in the surrounding Lean type theory. It quantifies over functions, beyond the object language’s quantification over positions.

Lean proves that no sentence of the chosen object language expresses enumerability even just on this pair. A sentence true in A must be true in B, whereas enumerability differs. This checks the location of the missing expressive resource; it is not merely an informal cardinality observation.

If “sufficient explanation” is required to answer the enumeration question too, these two accounts are no longer equivalent in content. This saves the possibility of a stronger universality thesis, but does not establish it: one must independently justify which global questions belong to adequacy and why their preservation yields the intended structural correspondence. “All truths” cannot silently mean both first-order truth and unrestricted higher-order structure.

## 6. Author counterreview and the stopping point

| Objection | Result and remaining scope |
|---|---|
| Only a bounded number of questions was compared. | False of this construction: the theorem quantifies over every finite formula, with no fixed complexity bound. |
| The root cannot reach the extra positions. | Both full carriers are root-reachable by zero or one step. |
| Identity and fixed partners were erased. | Equality is primitive, partner separation is checked, and the oneHot map preserves all formulas with arbitrary finite source parameter tuples. |
| A different map could make the worlds isomorphic. | Cantor excludes every map onto B from A. |
| The worlds have no joint structure. | Both have joint triples; the old joint-modal language is correctly translated. These are not claims about arbitrary resource laws. |
| Different cardinality is irrelevant to the intended explanation. | Then content equivalence is an appropriate relative conclusion. Calling that equivalence “the same structure” does not establish native isomorphism. |
| The full theory includes relationships omitted here. | Correct as a possible response. The counterexample refutes the stated inference for this signature, not a reconstructed richer theory whose independently specified content includes those relationships. |
| The current generative foundation might still be a common necessary pattern. | Yes. Multiple nonisomorphic realizations are compatible with a common foundation. Uniqueness of a foundation, uniqueness of a presentation and uniqueness of a whole native realization are distinct. |

The real wall is the inference from complete finitary relational content to an exhaustive global structural correspondence. It is not a Lean failure. No amount of further lemmas from exactly these premises can prove that inference because its negation has an explicit witness. This run therefore stops that route, rather than substituting another maintenance model.

The governing open issue is now sharper: derive a justified global coverage/categoricity condition from an independently specified explanatory commitment, or state and defend a weaker equivalence under which a common foundation is unique. Neither has been established for all sufficient explanations. No unconditional impossibility of universal generative grounding is inferred.

## 7. Existing mathematics and primary-source assessment

This is an application and explicit formalization of established model theory and Cantor diagonalization, not a claim to discover new model theory. Rahim Moosa’s author-hosted [Set Theory and Model Theory notes](https://www.math.uwaterloo.ca/~rmoosa/modeltheory-notes-v5.pdf), Example 6.12 (PDF p. 72, printed p. 66), explain quantifier elimination for the theory of infinite sets; the discussion after Proposition 6.19 gives completeness. The retrieved portions also describe the finite exclusions argument. Our step/joint relations are equality-definable expansions; the Lean proof checks the needed instance directly.

Read scope: the retrieved passages around Example 6.12 and Proposition 6.19 and the language/example passages returned with that search. A later attempt to retrieve additional portions timed out. No claim to have reviewed the full 121-page notes, no PDF imported, and no reliance on search snippets from secondary sites. The local proof, not the web source, establishes the particular relational models, modal translation, reachability, embedding and cardinal obstruction. No general compactness or Löwenheim–Skolem theorem is formalized here.

## 8. Checked proof inventory and dependency audit

- [ExplanatoryFiniteLogic.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/ExplanatoryFiniteLogic.lean): 11 new theorems, finite-context extension, all-formula preservation, old-language translation, root reachability and joint existence.
- [ExplanatoryCardinalityWall.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/ExplanatoryCardinalityWall.lean): 22 new theorems, concrete freshness, Cantor obstruction, elementary preservation, coverage repair, partner separation and nondefinability.
- [Isolated runner](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/check_explanatory_first_order_wall.py) and [immutable receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/explanatory-first-order-wall-checks/20261008T120907.759727Z/receipt.json): Lean 4.29.1, 12 modules, 180 declaration audits. The 147 inherited audits retain their earlier scopes; 33 are new.

New dependencies: 2 empty; 16 only `propext`; 2 `propext` with `Quot.sound`; 13 additionally `Classical.choice`. Full closure: 113 empty, 67 with allowed standard dependencies. Classical reasoning appears in the generic old-or-fresh case split and root reachability and propagates through dependent results. No custom axioms, proof holes or unsafe proof shortcuts. This is not a claim of 33 empty-dependency proofs, absence of logical foundations or absence of stated model hypotheses.

Frozen source copies, compiler logs and per-declaration dependency names are retained in the receipt directory. The scoped documentary checker binds these to current source hashes and verifies prior chapter/source preservation, new theorem inventory, inherited inventory, paired C30/F22 additions and local links. It is an author check, not independent-agent acceptance or a repository-wide audit. Concurrent unrelated source reviews remain pending.

**中文结论。** 已证明：身份、生成步骤、共同接合的全部有限一阶真值，即使由同一个映射对所有有限参数一致保留，也不迫出原生结构同构。加入整个范围的覆盖性可以修复，而覆盖性本身不能由这些真值推出。这个反例把普遍唯一性的缺口定位到全局对应；它不否定不同实现可能共享必要生成基础，也没有把有限一阶充分性冒充对全部现实真理充分。
