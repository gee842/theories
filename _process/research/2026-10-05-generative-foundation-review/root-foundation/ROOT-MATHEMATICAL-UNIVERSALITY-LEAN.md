# Mathematical universality: checked witness and equality results

7 October 2026, Asia/Bangkok. AI-authored correspondence record for Ren's request to pursue **“our root uniquely constitutes every mathematical truth”**, with all new mathematical proofs checked in Lean. Read with the [argument](ROOT-MATHEMATICAL-UNIVERSALITY-ARGUMENT.md), [counterreview](ROOT-MATHEMATICAL-UNIVERSALITY-REVIEW.md), [source assessment](ROOT-MATHEMATICAL-UNIVERSALITY-SOURCES.md) and [integration](ROOT-MATHEMATICAL-UNIVERSALITY-INTEGRATION.md).

**Validation:** the [new package](../../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/constitution/README.md) freshly compiled both modules under Lean **4.29.1**, importing only `Std`. The [receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/constitution/verification.json) records **43 named theorems and 84 source-level named declarations audited**. No custom axioms, proof holes or `native_decide` are used. The observed logical dependencies are `propext`, `Classical.choice` and `Quot.sound`; not every declaration uses every one. This record does not extend that check to historical prose proofs or other packages.

## 1. The new connection and its scope

This round addresses **independently specified generation → adequacy for every formula in a declared language**. It investigates how truth can be preserved without reproducing an entire carrier, and whether the proposed generation already presupposes the truth it purports to recover. It does not repeat the earlier [representation and truth-constitution results](MATHEMATICS-TRUTH-CONSTITUTION-MATH.md), [uniqueness audit](MATHEMATICS-UNIQUENESS-RESOLUTION.md), or the completeness/compactness route already discussed in [model admissibility](MATHEMATICS-MODEL-ADMISSIBILITY.md).

The formal structures are analytical articulations of operations, relations and interpretation within the investigated unfolding. An ambient structure supplied to a theorem is not thereby ontologically external. Its being supplied means precisely that the theorem does not derive its particular interpretation. The new results establish semantic preservation and a restricted decision procedure, leaving unique metaphysical constitution as an additional argument.

## 2. Full first-order witness criterion

[WitnessHull.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/constitution/formal/WitnessHull.lean), namespace `RootConstitution`, defines arbitrary finitary function and relation symbols, terms, and formulas in finite contexts `Fin n`. Equality, negation, conjunction and existential quantification are primitive. Universal quantification and disjunction are defined using these connectives, with checked semantic equivalences. Quantifier depth and finite context size are unrestricted.

`Embedding M N` supplies an injective map that preserves functions and preserves and reflects atomic relations. `Elementary M N e` requires agreement on every formula at every finite tuple from the smaller structure. `WitnessAdequate M N e` instead requires that an ambient existential assertion with internal parameters has a witness in the embedding's image, with the assertion still evaluated in the ambient structure. It does **not** define witness adequacy as formula agreement.

| Checked declaration | Exact contribution |
| --- | --- |
| `eval_embedding` | Function preservation extends to all terms. |
| `elementary_iff_witness` | Full formula agreement is equivalent to ambient existential witness adequacy. |
| `all_semantics`, `or_semantics` | Defined universal quantification and disjunction have their classical meanings. |

The criterion is proved by induction on actual syntax, including the quantified case. Its generality concerns finitary first-order languages, not second-order or infinitary quantification, and does not automatically cover every proposed mathematical semantics.

## 3. Least generated elementary hull

`WitnessSelectors M` supplies, for each formula and finite parameter tuple, a selected element satisfying that formula whenever a satisfying element exists in `M`. `classicalSelectors` constructs such a family noncomputably for a supplied nonempty ambient carrier. Its proof uses ambient satisfaction and classical choice; it is not an algorithm discovering mathematical truth.

`Hull M W Seed` is an inductively generated membership predicate. Its constructors admit seeds, original functions applied to finite tuples already admitted, and the supplied selector applied to such a tuple. `ClosedUnder` separately expresses these three closure obligations.

| Checked declaration | Exact contribution |
| --- | --- |
| `hull_closed` | Generated membership satisfies the specified closure requirements. |
| `hull_least`, `hull_iff_all_closed` | It is the least subset satisfying those requirements, for the fixed seeds and selectors. |
| `hullStructure`, `hullEmbedding` | The generated subtype has induced operations and relations and embeds into the ambient structure. |
| `hull_witnessAdequate`, `hull_elementary` | The inclusion preserves every first-order formula on internal parameters. |
| `hull_nonempty` | A nonempty seed gives a nonempty generated carrier. |

All formation rules use finite parameter tuples. Leastness is relative to the **fixed selector family**, not a theorem that all selector choices give the same carrier or that there is a least elementary substructure independent of those choices. The formal semantics permits empty carriers where its definitions make sense; the classical-selector construction explicitly assumes a nonempty ambient carrier. The nonempty-seed result is a sufficient nonemptiness condition, not a necessary one.

## 4. Exact informational cost of unrestricted selectors

The same module defines actual syntax for the tagged formula

\[
 (x=z\land\varphi)\lor(x=o\land\neg\varphi),
\]

where `z` and `o` are closed terms with distinct denotations and `φ` is a sentence. Renaming of terms and formulas into the extended context is explicit and its semantic correctness is proved.

`tagged_has_witness` establishes that this request always has a witness. **`selector_recovers_sentence`** establishes that a correct selector returns the denotation of `z` **if and only if** `φ` holds in the supplied structure. Consequently, unrestricted semantically correct witness selection carries information sufficient to recover every sentence's truth in this stated sense.

This is a precise dependency test, not a general theorem that selectors are noncomputable. It does not assume effective access to the selector or decidability of equality on its carrier. Some interpreted languages have effective selectors. The result shows why supplying arbitrary correct selectors is not by itself an independent derivation of their truth content.

## 5. Positive case: pure equality without a truth selector

[EqualityGenerativity.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/constitution/formal/EqualityGenerativity.lean), namespace `EqualityGenerativity`, treats only equality of variables, negation, conjunction and existential quantification, at arbitrary finite depth. `SamePattern` says that two finite parameter tuples have exactly the same equality relationships. `HasFresh A` requires an element outside each finite tuple in `A`.

| Checked declaration | Exact contribution |
| --- | --- |
| `truth_of_pattern` | Equal parameter patterns preserve every formula between carriers satisfying finite freshness. |
| `upper_succ_fresh`, `nat_hasFresh` | A number above a finite tuple's computed bound supplies a concrete fresh value. |
| `finite_witness_reduction` | Every existential request on a natural-number tuple reduces to its finitely many existing values or one fresh value. |
| `evaluate`, `evaluate_correct` | An executable recursive Boolean evaluator agrees with satisfaction for every formula and natural-number parameter tuple. |
| `sentence_evaluation` | The evaluator decides every sentence of this language for any carrier satisfying `HasFresh`. |
| `double_not_surjective`, `double_preserves_all_equality_formulas` | Doubling is a proper embedding preserving all formulas of this equality language, with transported parameters. |
| `every_nat_generated`, `generated_nat_least` | The zero/successor construction generates the natural-number carrier and has its declared induction property. |

The evaluator's existential branch searches the finite parameter list plus one fresh number; it does not query the formula's ambient semantic truth. This is a successful, explicitly limited reduction of unrestricted quantification to independently described witness cases.

`HasFresh`, the syntax, semantics, natural-number metatheory and logical background remain supplied. Zero and successor are construction rules in the last result, **not symbols of the interpreted equality language**. The module neither decides arithmetic nor proves that infinite carriers have the same cardinality or are identical mathematical subjects in richer languages.

## 6. A substantive quantified failure

The general module also interprets one language with a constant zero and unary successor, and no primitive relation symbols, on both natural numbers and integers. `naturalEmbedding` preserves the constant and successor. The sentence `∃x, successor(x) = zero` is false in the natural-number structure and true in the integer structure, as checked by `natural_predecessor_false` and `integer_predecessor_truth`.

`compositional_embedding_not_elementary` and `compositional_embedding_not_witnessAdequate` establish the failure of the stronger preservation claims for this actual embedding. The failure concerns a missing quantified witness while the named operations remain preserved; it is not obtained by freely switching a supplied predicate. Together with the equality result, this makes expressive scope consequential: an adequate account of one language cannot simply inherit adequacy for a richer one.

## 7. Reproduction and remaining foundational obligation

Run from the repository root:

```sh
python3 experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/constitution/check.py
```

The checker compiles both modules to a new temporary object directory using the pinned toolchain, then compiles a saved [audit driver](../../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/constitution/verification/KernelAudit.lean). The [full audit log](../../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/constitution/verification/KernelAudit.log) and receipt bind the checked sources, checker, toolchain, driver and logs by SHA-256. The audit covers every explicitly named source-level theorem, definition, structure and inductive declaration; the count does not purport to enumerate every automatically generated projection or recursor. The kernel checks the complete modules. There is no mathlib dependency or claim that the primary-source comparator was freshly compiled here.

The checked advance is therefore paired: a general semantic preservation construction with its exact informational dependence, and a narrow case where independently stated freshness operations support a complete formula evaluator. To establish the stronger root claim, the account still needs independently justified coverage beyond this language and an argument for the unique constitutive priority of the proposed root over rivals preserving the same mathematical content. Neither obligation is discharged by the source hashes, the theorem count, or giving a supplied semantic selector a generative name.
