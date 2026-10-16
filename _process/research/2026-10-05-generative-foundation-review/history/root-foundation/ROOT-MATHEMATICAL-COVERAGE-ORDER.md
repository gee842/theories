# Checked coverage of dense linear order truth

7 October 2026, Asia/Bangkok. AI-authored mathematical contribution to Ren's request to complete both universal mathematical coverage and exclusive grounding. **This result advances coverage for a strictly richer language than pure equality; it does not complete either requested universal claim.** The governing target remains the complete claim, rather than this bounded case replacing it.

The [new order package](../../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/constitution/order/README.md) proves all-formula preservation, an executable sentence evaluator and a least generated elementary substructure using only before, after and between operations. Its [fresh Lean 4.29.1 receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/constitution/order/verification.json) records **33 named theorems, 58 named declarations audited**, and only the standard logical dependencies `propext`, `Classical.choice` and `Quot.sound`. The previous [43-theorem package](ROOT-MATHEMATICAL-UNIVERSALITY-LEAN.md) remains unchanged. The new source and receipt received independent mathematical correspondence review.

## 1. Exact target and independently stated inputs

The single [DenseOrder.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/constitution/order/formal/DenseOrder.lean) module imports only `Std`, in namespace `OrderGenerativity`. Its `DenseOrder A` supplies:

- A strict relation with irreflexivity, transitivity and trichotomy.
- A seed element, ensuring nonemptiness.
- Unary `before` and `after` operations, with strictly smaller and larger outputs.
- A binary `between` operation that produces a strictly intermediate element whenever its first argument is smaller than its second.

These are order properties and element-producing operations. Their specifications contain no formula satisfaction test. Density and the absence of endpoints are substantive inputs; their presence has not been derived from an unrestricted generative root. The concrete rational interpretation supplies the operations as `0`, `a − 1`, `a + 1` and `(a + b) / 2`, with checked laws.

The language has only equality and strict order on variables, negation, conjunction and existential quantification. Formulas have arbitrary finite contexts and unrestricted finite quantifier depth. Defined universal quantification and disjunction have checked semantic equivalences. The arithmetic in the rational witness implementation is not arithmetic in the interpreted language: no addition, multiplication, named constants or arbitrary predicates occur in its atomic formulas.

These representations isolate particular structural relationships within the same investigated unfolding. Treating order laws or interpretation as supplied identifies the explanatory scope of this construction; it does not make them external to generative reality. Locating them within the whole also does not explain their necessity or unique grounding.

## 2. From order relationships to complete formula coverage

`SamePattern` means that two finite tuples have exactly the same equality and strict-order relationships. For a proposed extra value, either its value matches an existing parameter, or it determines a cut through the tuple. Finite maximal lower and minimal upper parameters suffice to locate that cut. A corresponding witness is an existing value, an element before or after a parameter, an element between two parameters, or the seed when no parameter constrains it.

| Checked declarations | Contribution |
| --- | --- |
| `finite_max`, `finite_min` | Nonempty finite selections have the needed extreme parameter values. |
| `cut_realized`, `extend_pattern` | The displayed order operations extend every matched finite pattern. |
| `truth_of_pattern` | Matched patterns preserve every formula, including quantifiers. |
| `sentence_agreement` | All supplied dense orders without endpoints agree on every sentence of this language. |
| `finite_witness_reduction` | An existential assertion is equivalent to one of the finite displayed candidate cases satisfying its body. |
| `all_semantics`, `or_semantics` | The derived universal and disjunctive syntax has its declared meaning. |

The quantified step is a proof over actual syntax, not a stipulation that the structures agree. It uses pattern extension to supply the witness in each direction. The algorithm need not discover which cut a hypothetical satisfying value occupies: it checks all the finite candidate cases.

## 3. Executable truth evaluation

`evaluate` recursively computes a Boolean value. Atomic equality and order use their supplied decision procedures; negation and conjunction use Boolean operations; existential quantification checks the finite candidates enumerated by `anyWitness`. The chosen computational carrier must have decidable atomic equality and order. **The target carrier to which sentence truth is transported need not have supplied decision procedures.**

`evaluate_correct` proves agreement with satisfaction for every formula and every parameter tuple on the computational carrier. `sentence_evaluation` transports the result to every supplied `DenseOrder`, including carriers in other Lean universes. `rationalOrder` realizes the computational inputs using Lean's bundled rational arithmetic. `decideSentence_correct` consequently establishes a single executable evaluator for every sentence across this entire declared class.

The module also checks three actual reductions with `decide +kernel`: the density sentence evaluates to true, while the existence of a least or greatest element evaluates to false. These proofs use kernel reduction, not `native_decide`. The corresponding `density_truth`, `no_least_element_truth` and `no_greatest_element_truth` follow for every target order. These examples exercise the implementation; the universal correctness theorem, rather than the examples, establishes its full syntactic coverage.

Classical reasoning occurs in the proofs, including finite extremum selection. The audit also detects standard logical dependencies through the law proofs bundled into `rationalOrder`. Thus neither the package nor the rational evaluator's full declaration is described as axiom-free. Its computational operations are explicit arithmetic and finite searches; no arbitrary formula-truth selector is supplied.

## 4. A generated domain suffices

`Generated O` begins with `O.seed` and closes under the selected before, after and between operations. `generated_closed`, `generated_least` and `generated_iff_all_closed` prove that it is exactly the least subset satisfying those closure requirements. `generatedOrder` equips this subtype with the inherited strict order and the admitted operations. `generated_elementary` proves that the inclusion preserves every formula with parameters in the generated subtype. More generally, `orderEmbedding_elementary` establishes this for every order-preserving and order-reflecting injection between the supplied orders.

The leastness is relative to the selected operations. It is not a selector-independent least dense suborder, a unique ambient carrier, or a proof that different realizations have identical cardinality. `between` is a total function; its intermediate-value law is required only for ordered arguments. The finite search and generated closure may include outputs on other pairs. This can add points but does not undermine correctness: every candidate remains an actual domain element. The concrete rational operation is explicit on all pairs.

## 5. Contribution to the full request

This supplies a successful richer instance of the proposed route: a small family of independently stated witness operations, with checked structural laws, determines the full truth theory of an interpreted language. Unlike unrestricted semantic witness selection, the concrete operations do not contain a branch asking whether the queried sentence is true.

Universal coverage still requires an argument that adequate formation, identity, domain and interpretation principles extend across the intended mathematics, including cases outside dense order. This result does not cover arbitrary discrete orders, arithmetic or higher-order mathematics. Exclusive grounding additionally requires an account of why the adequate principles obtain in virtue of the proposed root rather than a rival preserving these same structural resources and truth conditions. The order theorem supplies no predicate or premise that settles that philosophical direction by definition.

These are limitations of the present explanatory bridge. They are not a proof that universal constitution is impossible, nor a license to declare it complete after accumulating local cases.

## 6. Reproduction

From the repository root:

```sh
python3 experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/constitution/order/check.py
```

The checker compiles the complete module to a fresh temporary object directory under the pinned toolchain, then compiles the saved [audit driver](../../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/constitution/order/verification/KernelAudit.lean). Every explicitly named theorem, definition, structure, inductive declaration and instance is audited. Automatically generated projection and recursor names are not separately counted; the full module is kernel checked. The [receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/constitution/order/verification.json) binds the source, checker, toolchain, driver and logs by SHA-256 and records each declaration's logical dependencies. No custom axioms, proof holes, unsafe declarations or `native_decide` are used, and no mathlib dependency was installed or compiled.
