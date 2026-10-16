# Functions through completed finite graphs

7 October 2026. AI-authored mathematical correspondence for the admission continuation. [FunctionGraphs.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/constitution/admission/formal/FunctionGraphs.lean) connects the full-function input of the earlier higher-type reconstruction to completed relation graphs. Its **18 named theorems and 36 declaration audits** passed in the combined fresh [Lean receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/constitution/admission/verification.json), alongside the [admission module](ROOT-MATHEMATICAL-ADMISSION-LEAN.md).

## 1. Coherent finite graphs and the totality condition

A `GraphIdeal A B` is an ideal of finite subsets of `A × B`. Its union is a relation. `Functional` says that this relation assigns at most one output to each input. `functional_iff_finite` proves that the union is functional exactly when every finite member is functional. The nontrivial direction uses a common finite upper bound for two members of the same directed ideal, so conflicting outputs cannot hide in different pieces.

`Total` separately requires an output for every input. `total_iff_finite_coverage` states exactly how this appears in the representation: every input occurs in some finite member with an output. The quantifier over every input remains. Local compatibility alone does not imply it: `empty_functional` and `empty_not_total` check that the empty relation ideal is functional but not total on an inhabited input carrier.

`FunctionIdeal` records an ideal and proofs of these two conditions. This is a representation of total functions, not a claim that every compatible partial history already supplies an output everywhere. The graph interpretation describes relations within the same mathematical subject; it does not introduce an independent actor and passive object at the foundational level.

## 2. The exact function correspondence

`encodeFunction f` takes the ideal of finite parts of the graph of `f`. `decodeFunction` selects each input's uniquely determined output from a total functional ideal. Its use of `Classical.choose` is explicit; no executable reconstruction is asserted. `decode_mem` and `graph_decode` characterize the selected output, and `decode_encode` and `encode_decode` prove the maps inverse.

`functionMap` therefore gives an actual bijection between full functions and total functional graph ideals. All such ideals are admitted in the representation. The proof is not a derivation of their existence from finitely named graph pieces alone.

`functions_admitted_by_completion` connects this result to the new admission characterization: if a predicate family on `A × B` includes all finite predicates and is closed under every ambient nonempty directed union, it admits the graph of every function `A → B`. The closure hypothesis has the full strength identified by `Admission.lean`.

## 3. Predicates cannot be bypassed by full Boolean functions

`trueFiber f` is the predicate selecting inputs on which a Boolean-valued function returns true. `characteristic` constructs the characteristic function of an arbitrary supplied predicate, and `characteristic_fiber` proves recovery of that predicate.

`full_boolean_functions_iff_predicates` states the resulting admission test precisely: for one predicate-domain condition `C`, **admitting the true fibers of every function `A → Bool` is equivalent to admitting every predicate on `A`**. There is no independent function-domain condition in this theorem. It does not prove that an arbitrary function-admission rule entails predicate fullness without a fiber interpretation. It does show that replacing full predicates by full Boolean-valued functions, while retaining their true fibers, does not reduce the relevant admission commitment.

## 4. Complete higher-type semantic transport

The prior [finite-type module](ROOT-MATHEMATICAL-HIGHER-TYPES.md) completed predicates but left arrow types as full function carriers. `GraphCompleted` now interprets both non-base type constructors through ideals: predicates as finite-subset ideals, and arrows as total functional finite-graph ideals. The finite `base`/`arr`/`pred` grammar is unchanged.

`graphTypeMap` constructs the recursive bijection from the direct full-type interpretation. It composes the earlier function conjugation with the concrete graph correspondence. `graphEval` interprets application through graph decoding and lambda abstraction through graph encoding. `graph_term_transport` checks the interaction of these operations with corresponding environments.

`graph_formula_transport` and `graph_sentence_transport` preserve every formula and closed sentence of the declared language, including equality, membership and quantification at all represented finite types. The quantified step uses both directions of the constructed type map. `higher_eta_graph` carries the earlier mixed predicate/function example into this graph interpretation.

The grammar still has no internal universe, dependent types, named-signature extension theorem or distinguished truth-value object type. No new formula-to-term comprehension constructor is introduced. The theorem concerns semantic equivalence, not effective truth decision.

## 5. What has been reduced

The completed presentation no longer needs a separate full function carrier at each arrow type: it uses the same relation-completion framework plus functionality and totality. This is a constructive reduction of presentation resources and a checked extension of the earlier semantic correspondence.

The foundational resources have not disappeared. The proof's direct interpretation contains full function spaces; the completed interpretation admits all qualifying relation ideals. Its predicate-valued ideal membership and global totality are interpreted in Lean's supplied metatheory. The [affirmative admission argument](ROOT-MATHEMATICAL-ADMISSION-ARGUMENT.md) and [review](ROOT-MATHEMATICAL-ADMISSION-REVIEW.md) therefore retain the obligation to justify unrestricted admission and its constitutive dependence.

The fresh checker rebuilds the inherited completion modules and frozen `TypedTruth.lean`, then both new modules, from receipt-matching bytes in an isolated directory. Only the standard `propext`, `Quot.sound` and `Classical.choice` dependencies occur. This module and the admission module together contribute **52 new named theorems and 86 declaration audits**; imported results are not counted again.
