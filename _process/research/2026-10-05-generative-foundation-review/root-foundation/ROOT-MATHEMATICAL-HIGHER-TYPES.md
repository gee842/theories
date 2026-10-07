# Conditional reconstruction through finite higher types

7 October 2026, Asia/Bangkok. AI-authored formal contribution to Ren's authorized conditional higher-order reconstruction. **Result: checked truth transport for the exact finite-simple-type language below, with a concrete ideal-completion interpretation at every predicate type.** This does not establish unrestricted mathematical coverage or unique metaphysical grounding.

The owned [TypedTruth module](../../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/constitution/higher-order/formal/TypedTruth.lean) imports the existing finite-subset completion through `CompletionExamples`. A fresh local dependency compilation, module compilation and audit were performed with Lean 4.29.1. Eighteen theorems and forty named declarations were checked. The only reported logical axioms are the standard `propext`, `Quot.sound` and, for the derived universal-quantifier/eta corollaries, `Classical.choice`. There are no proof holes, custom axioms or `native_decide` uses. The parent integration supplies the combined reproducible receipt.

## 1. Exact reconstructed domain

The type grammar is finite and inductive:

- `base` is a supplied carrier;
- `arr s t` is the full function space from the interpretation of `s` to that of `t`;
- `pred s` is a full predicate space over the interpretation of `s`.

Every individual type has finite construction depth, with no fixed maximum imposed by the grammar. Function arguments and results can themselves be functions or predicates. Predicates can concern predicates and other higher types. There is no internal universe type, dependent type former or self-applicable unrestricted truth predicate.

The direct interpretation uses a supplied carrier `A`, full external function spaces, and predicates into `Prop`. The completed interpretation uses a supplied carrier `B`, full external function spaces, and, at each `pred s`, **ideals of finite subsets of the recursively completed carrier for `s`**. Thus a predicate of predicates is interpreted through a further finite-subset ideal completion over the preceding completed predicate carrier. It is not silently replaced by a predicate only about base elements.

`BiMap A B` supplies an actual bijection of the base carriers, with both inverse identities. It does not assume formula truth preservation. The identity bijection provides a same-base reconstruction when no carrier change is desired.

## 2. Structural correspondence is constructed before truth transport

| Declaration | Exact contribution |
|---|---|
| `predicateMap` | Builds the predicate/ideal bijection using `partsOf`, `unionContents` and the earlier inverse theorems. |
| `predicateMap_membership` | Checks membership under that concrete completion correspondence. |
| `arrowMap` | Transports a full function by conjugating with the argument and result bijections; proves both inverse identities. |
| `typeMap` | Recursively supplies the bijection for every finite type, including mixed function and predicate types. |
| `term_transport` | Preserves evaluation of variables, applications and lambda abstractions under the recursively mapped environment. |
| `formula_transport` | Preserves every formula in the declared grammar, with arbitrary free typed parameters transported through `typeMap`. |
| `sentence_transport` | Specializes to closed formulas. |

The predicate correspondence is specifically the existing ideal completion of finite subsets. It is not an uninterpreted equivalence postulated for whichever higher-order objects are wanted. The function correspondence is also explicit: transport the argument backward, apply the original function, then transport the result forward. Both inverse identities are needed for quantification over full higher-type ranges.

The formula grammar contains equality of two terms of any common type, predicate membership, negation, conjunction and existential quantification at **any** finite type. Universal quantification is derived through classical negation and existence, with its ordinary semantics checked. Equality at function and predicate types uses the extensional identities of the given Lean semantics and the established type bijections.

The existential step does not merely preserve selected witnesses. Forward and backward bijections match every inhabitant of the interpreted type. This is what supports full higher-type quantification. No hypothesis directly states that the original formula or all formulas already have matching truth values.

## 3. Comprehension and an explicit mixed-type sentence

`formula_comprehension` checks that the extension of any formula with one additional variable has an ideal presentation at that variable's type. The formula may itself quantify over higher types. Its membership agrees with the completed interpretation of the formula for every completed argument.

This is semantic comprehension under the supplied full predicate interpretation. It is not a finite procedure for discovering the extension: the direct predicate used in the proof is the formula's semantic extension. Nor does the syntax add a formula-to-term comprehension constructor. The theorem records the conditional existence and correspondence the full completion warrants, not an algorithm or a new primitive whose justification has disappeared.

The closed formula `etaSentence s t` quantifies over functions from `s` to `t` and asserts that lambda-expanding application of that function equals the original function. `higher_eta_completed` instantiates its argument type as predicates on the base and its result type as predicates on those predicates. The checked interpretation therefore exercises typed quantification, lambda binding, application and equality across nested ideal-completion layers. It is an explicit higher-type consequence of the general reconstruction.

## 4. Scope and remaining premises

The language has no primitive named constants or relations beyond equality and predicate membership. A chosen operation or relation can be supplied as a free typed parameter and transported by the theorem's environment map. A theorem that a particular independently interpreted named signature satisfies that correspondence would be a further application, not something silently assumed here.

This is also not a claim to implement every expression of Church simple type theory or a particular HOL prover: the grammar has no truth-value type whose formulas are terms. Its finite types, lambda/application terms and separately specified formulas are the precise covered language. That language already supports genuine higher-type quantification and nested predicates.

Full external function and predicate spaces, the base carrier and its bijection, finite-subset ideal existence, and the stated logical interpretation remain supplied foundational resources. These resources are differentiated relationships within the generative account; being locally supplied does not place them outside it. The proof reconstructs their higher-type presentation and consequences. It does not derive their universal availability from finite physical generation, provide an effective decision algorithm for higher-order truth, or establish the root's uniquely necessary ontology.

The accomplished conditional connection is consequently precise: **from a base correspondence and the explicit full-type interpretation, concrete predicate completion and function conjugation preserve every term and formula at every finite type in the declared language**. No further truth-preservation assumption is required. That completes this module's reconstruction obligation while retaining the wider foundation's independent scope and premise questions.
