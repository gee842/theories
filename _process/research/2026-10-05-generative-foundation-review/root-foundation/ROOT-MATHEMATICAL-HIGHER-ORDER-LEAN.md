# Checked relational second-order reconstruction

7 October 2026, Asia/Bangkok. AI-authored correspondence record for [SecondOrder.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/constitution/higher-order/formal/SecondOrder.lean), namespace `SecondOrderReconstruction`. This completes the specified conditional reconstruction of full relational second-order satisfaction through finite-tuple ideals. It does not establish an independent derivation of fullness or the root's exclusive metaphysical priority.

**Validation:** this module contains **25 named theorems and 57 explicitly named declarations**. The fresh Lean **4.29.1** [combined package receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/constitution/higher-order/verification.json) records **43 new theorems and 97 audited declarations** across this module and the separate `TypedTruth.lean` development. The inherited `IdealWarrant`, `CompletionRole` and `CompletionExamples` dependencies were freshly compiled from bytes matching their existing receipt. Only `propext`, `Classical.choice` and `Quot.sound` occur as audited logical dependencies; there are no custom axioms, proof holes or `native_decide`. The [counterreview](ROOT-MATHEMATICAL-HIGHER-ORDER-REVIEW.md) and [primary-source assessment](ROOT-MATHEMATICAL-HIGHER-ORDER-SOURCES.md) distinguish formal verification, mathematical antecedents and foundational interpretation.

## 1. Language and interpretation

`Formula n Γ` has a finite individual-variable context of size `n` and a finite list `Γ` recording the arities of its relation variables. `RelVar Γ k` is a typed variable of arity `k`. The constructors include:

- Individual equality and application of a relation variable to a tuple of individual variables.
- Equality of two relation variables of the same arity.
- Negation, conjunction, individual existential quantification and relation existential quantification.

Every finite arity is admitted, including zero, and quantifier nesting is unrestricted at finite depth. Derived individual and relation universal quantifiers have separately checked semantic clauses. Individual and relation binders update different contexts, so arbitrary alternations preserve the intended variable types.

The full predicate interpretation quantifies over every Lean predicate `(Fin k → A) → Prop` at arity `k`. The ideal interpretation quantifies over every nonempty directed lower ideal of the finite subsets of `Fin k → A`. Relation application reads membership in `unionContents`; relation equality compares the actual ideals. The individual carrier `A` remains the same in both interpretations. No first-order function symbols, function quantifiers or general simple-type hierarchy are part of **this module**; the separate typed development has its own scope.

These interpretations articulate the same relations in two forms within the local model. They do not posit two independent ontological domains. Their common carrier, quantifier ranges and logical background remain supplied to this reconstruction.

## 2. Inverse correspondence and full truth

The existing `CompletionExamples.partsOf` sends a predicate to the ideal of its finite parts; `unionContents` recovers the predicate from an ideal. Its previously checked inverse laws apply uniformly to the tuple carrier `Fin k → A`. No new argument restricted to unary predicates is used to stand in for higher arities.

| New checked declaration | Exact contribution |
| --- | --- |
| `decode_encode`, `encode_decode` | The two environment transformations are inverses. |
| `related_extend` | Corresponding relation environments remain related when a binder adds corresponding predicates and ideals. |
| `related_relation_eq` | Actual predicate equality is equivalent to ideal equality, using extensionality and the inverse laws. |
| `satisfaction_transport` | All formulas preserve satisfaction between matching selected predicate and ideal ranges. |
| `full_satisfaction_transport` | Specialization to the full predicate and ideal ranges. |
| `full_encode_truth`, `full_decode_truth` | Each interpretation reconstructs every formula of the other. |
| `full_sentence_reconstruction` | Closed sentences have the same truth in the two full interpretations. |

The main proof is induction on the formula syntax. In the relation-existential case, a predicate witness is sent to `partsOf`; conversely, an ideal witness is decoded by `unionContents`. This uses the full domains at the actual quantifier clauses. It does not merely prove agreement on atomic membership and assume agreement on quantification. `full_relation_exists` and `full_relation_forall` additionally expose the unrestricted predicate ranges directly.

## 3. Selected ranges and the fullness obligation

`PredicateDomain` and `IdealDomain` independently specify which relations are admitted at each arity. `DomainsRelated` requires admission to agree whenever a predicate and ideal have the same content. `representedIdeals` supplies the corresponding ideal range for any specified predicate range, and `selected_encode_truth` proves semantic preservation there.

These are general selected-range semantics, **not automatically Henkin models**: no comprehension or closure principle is assumed. The general theorem also permits arbitrary free relation environments; any requirement that a free assignment belong to an admitted range is a separate model condition. Closed-sentence reconstruction has no free-assignment issue.

`corresponding_fullness` proves that admitting every predicate is equivalent to admitting every ideal under this range correspondence. It transports the fullness obligation; it does not discharge it. The ideal type itself uses arbitrary membership predicates over the finite basis in the supplied Lean metatheory. Replacing “all predicates” with “all ideals” therefore does not independently explain unrestricted admission.

## 4. A concrete finite-range boundary

`finitePredicates` admits exactly those relations whose extensions are finite subsets of the appropriate tuple carrier. The actual sentence `totalUnarySentence` is

\[
\exists R\;\forall x\;R(x).
\]

`full_totalUnary` proves it true in full predicate semantics for any individual carrier. `finite_rejects_totalUnary` proves it false on the natural numbers when relation quantifiers range only over finite predicates. The proof uses the finite relation's list witness, bounds its unary entries, and obtains a contradiction at a larger natural number. `finite_not_full` separately checks the failure of full admission.

This preserves the same sentence and atomic membership interpretation while changing the actual quantifier range. It shows why retaining only finite formation pieces is insufficient for the intended full semantics. It does not refute a completion that genuinely admits all ideals, does not claim that the selected finite family satisfies comprehension, and does not independently refute the proposed root.

## 5. Reproduction and remaining claim

From the repository root:

```sh
python3 experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/constitution/higher-order/check.py
```

The [saved audit driver](../../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/constitution/higher-order/verification/KernelAudit.lean) prints dependencies of every explicitly named new declaration. The receipt binds source, inherited dependencies, toolchain, checker, driver and logs by SHA-256. The 57-declaration count for this module excludes automatically generated projections and recursors; its complete source is kernel checked.

The completed result is semantic reconstruction, with a precise range-sensitive boundary example. It supplies neither an algorithm deciding arbitrary second-order truth nor an explanation of why this metatheory's entire predicate range is independently warranted. The stronger claim that the generative root uniquely constitutes every mathematical truth still requires that admission argument and a substantive account of exclusive grounding.
