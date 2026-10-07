# Finite admission and named higher-order theories: checked correspondence

7 October 2026, Asia/Bangkok. AI-authored correspondence record for the [coverage package](../../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/constitution/coverage/README.md). The [fresh Lean 4.29.1 receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/constitution/coverage/verification.json) passes **36 new theorems and 66 named declaration audits**. Six inherited modules were freshly rebuilt from receipt-matching sources and are not counted as new. The reported dependencies are `propext`, `Quot.sound` and `Classical.choice`.

## 1. A common finite-family construction

[FiniteAdmission.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/constitution/coverage/formal/FiniteAdmission.lean) contains **23 theorems and 27 named declarations**. `FiniteCarrier A` requires a finite list covering every element of the supplied carrier. It permits repetitions and the empty carrier; no cardinality formula or efficient enumeration is claimed.

`selections` recursively forms a list of lists: for each new element, retain the previous selections and also the selections with that element included. The construction depends on the supplied list, not on a target predicate. `selection_represents` proves that every predicate's restriction to that list is represented by some selection. `finite_domain_family_complete` removes the restriction when the list covers the carrier.

This supplies a common finite family covering every extensional membership pattern. The construction itself does not query a predicate. The proof that an arbitrary predicate has a representative uses classical case distinctions and propositional extensionality; it is not a decision procedure for an arbitrary proposition supplied without a decision method.

## 2. Full admission from finite formation

`list_admitted` derives admission of each finite list's membership predicate from three explicit premises: admission of the empty predicate, admission of every singleton, and closure under binary union. `finite_admission_of_formation` therefore derives the previous `IncludesFinite` condition from those operations.

`full_of_finite_formation` concludes `Full C` on a supplied finite carrier. No directed-union or infinite-chain closure premise is needed. `full_iff_finite` gives the equivalent finite-admission characterization; `directed_closure_of_finite` shows that directed closure follows at this scope rather than being an additional assumption.

`graph_finite` proves that every function from a finite domain has a finite graph, even if the codomain is not finite. `function_graph_admitted` uses finite admission on the product to admit that graph. Availability of the codomain and finite predicates over that product remain explicit; the theorem does not enumerate all functions into an infinite codomain.

`bool_finite` supplies a concrete base case. `nat_not_finite` prevents applying the finite-carrier premise to `Nat`, using the inherited checked fact that the even predicate is not finite. This does not prove that no different principle can warrant admission on `Nat`.

## 3. Every declared finite type over a finite base

`predicates_finite` maps the fixed selection family to its membership predicates and proves coverage of the entire predicate carrier. `assignments` forms finite output assignments to a finite list of inputs. Its coverage proof and `functions_finite` establish that the full function carrier is finite when both input and output carriers are finite.

Function assignment uses classical equality; the proof handles an empty function carrier separately and, when one function exists, uses a fixed initial function for the assignment construction. No missing empty-domain or empty-codomain case is silently excluded.

`direct_type_finite` applies these two closure results recursively to the existing `base`/`arr`/`pred` type grammar. Every individual type has finite depth, with no fixed maximum imposed by that grammar. `finite_type_full_admission` then derives full predicate admission at each such carrier from the three finite-formation premises.

`finite_transport` carries a finite cover across a supplied inverse correspondence. Using the earlier `graphTypeMap`, `completed_type_finite` and `completed_type_full_admission` establish the corresponding results for the graph/ideal interpretation. These are results about each represented type, not a claim that the union of all type levels is a finite carrier or an internal universe.

## 4. Named operations and relations in the higher-order language

[SignatureTruth.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/constitution/coverage/formal/SignatureTruth.lean) contains **13 theorems and 39 named declarations**. A signature assigns symbols to each simple type. Symbols may name base elements, curried operations, predicates and higher-type values. The model interprets every symbol at its declared type.

The language adds symbol terms to the previous variable/application/lambda grammar. Formulas have typed equality, predicate membership, negation, conjunction and existential quantification at any represented type; universal quantification is a derived form. This remains a single-base finite simple-type language. It has no dependent types, internal universe or formula-to-predicate term constructor.

`Compatible e M N` states the concrete symbol correspondence along the previously established type maps. It does not assume formula truth preservation. `transportInterpretation` constructs such an interpretation from a direct model, while `backInterpretation` supplies a matching interpretation for any completed model. Both compatibility proofs are checked.

`term_transport`, `formula_transport` and `sentence_transport` establish the correspondence inductively, including arbitrary higher-type binders. `formula_comprehension` gives an ideal representing the extension of any named formula with parameters. This is semantic comprehension using the full predicate interpretation, not effective predicate synthesis or an independent admission theorem for infinite domains.

## 5. Whole theories, semantic consequence and satisfiability

`Theory S` is an arbitrary collection of closed formulas. `theory_transport` preserves and reflects satisfaction of the entire collection under the declared model correspondence. Neither the signature nor the theory is required to be finite.

`entailment_transport` ranges over every base carrier in a fixed metatheoretic universe and every interpretation of the signature. It proves equivalence of semantic consequence between the direct and completed presentations. `satisfiability_transport` proves equivalence of model existence for the same theory and model classes. The inverse interpretation is essential to cover all completed interpretations, rather than only a chosen forward image.

These are semantic results. No proof calculus, syntactic completeness theorem, decidability theorem, consistency proof or construction of a model for an arbitrary theory is provided. Empty base carriers are included when an interpretation of the signature exists. The same-universe model classes are part of the exact contract; a proper-class or unrestricted internal-universe semantics is not introduced.

## 6. Concrete application and boundary

`NatSymbols` names zero and addition. `nat_add_assoc_direct` verifies the actual universally quantified addition-associativity sentence using the supplied natural-number interpretation; `nat_add_assoc_completed` transports it to the graph/ideal interpretation. The natural numbers and addition are inputs to this example, not derived by the signature theorem.

`mismatched_symbols_change_truth` interprets two named elements equally on one Boolean presentation and differently on the other. Their equality sentence changes truth. This is a checked reason not to omit the symbol-correspondence condition. It changes the interpreted subject and is therefore not a counterexample to the full nondual root or to the theorem under its actual hypotheses.

The [integrated assessment](ROOT-MATHEMATICAL-COVERAGE-INTEGRATION.md) distinguishes these new results from the outstanding universal requests. The [review and evidence assessment](ROOT-MATHEMATICAL-COVERAGE-REVIEW.md) records the substantive counteraccount and source genealogy. All review in this round was conducted by the same agent; no independent reviewer is claimed.
