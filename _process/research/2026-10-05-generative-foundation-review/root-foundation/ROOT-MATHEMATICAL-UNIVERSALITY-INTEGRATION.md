# Pursuing unique mathematical constitution through generated witnesses

7 October 2026, Asia/Bangkok. AI-authored integration following [Ren's renewed instruction](../../../../sources/15-codex-theory-conversations/2026-10-07-pursue-unique-mathematical-constitution.md). **The target is directly the stronger claim: our root uniquely constitutes every mathematical truth.** The present round supplies a checked positive case, a general preservation construction and a precise test of its explanatory resources. It does not claim the universal and exclusive thesis proved.

The [affirmative argument](ROOT-MATHEMATICAL-UNIVERSALITY-ARGUMENT.md), [independent internal counterreview](ROOT-MATHEMATICAL-UNIVERSALITY-REVIEW.md), [source assessment](ROOT-MATHEMATICAL-UNIVERSALITY-SOURCES.md) and [formal correspondence](ROOT-MATHEMATICAL-UNIVERSALITY-LEAN.md) form this round. The [formal package](../../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/constitution/README.md) contains the exact statements. Its [receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/constitution/verification.json) determines the checked source version and dependencies. A fresh isolated Lean 4.29.1 build passed: **43 named theorems and 84 named declaration audits across two modules**, no custom axioms or proof holes. The reported standard dependencies are `propext`, `Quot.sound` and `Classical.choice`; the result is not described as assumption-free.

**本轮直接追求数学的更强构成主张：先找到不预先输入任意真值的生成规则，再证明它足以决定一个明确语言中的全部真理。相等与新差异的有限规则提供了一个已检验的正面实例；任意正确见证选择则可能已经包含全部句子真值。局部充分性、全部数学的覆盖和唯一的根本解释，仍须分别完成。**

## 1. The attempted advance

The earlier work already established relative truth determination, model admission and unique completion roles. It also examined natural-operation reconstruction and substantive structural rivals. The initial suggestion to use Henkin model construction was withdrawn as a new route after the reviewer located it in [the model-admissibility study](MATHEMATICS-MODEL-ADMISSIBILITY.md). Those historical results retain their original validation scope; this round does not silently migrate all of them into Lean.

The selected question is more discriminating: **can independently specified generative rules supply exactly the witnesses needed to determine every formula of a subject, without importing the complete truth relation into the rules?** This connects the root's proposed formation and identity content to quantified truth, rather than another learner's success or another name for a completed domain.

The formal decomposition preserves one account of mathematical activity and its content. An ambient structure supplies a local comparison target; it is not thereby outside generative reality. A finite-context language exposes which distinctions the theorem preserves. Neither locating semantics within the whole nor calling a rule generative discharges its explanatory commitments.

## 2. A positive case with an explicit truth evaluator

`EqualityGenerativity.lean` interprets finite first-order formulas built from variable equality, negation, conjunction and existential quantification. Other ordinary Boolean connectives and universal statements can be expressed using these constructors. It includes arbitrary nesting and finite parameter contexts, not merely a finite test set.

The independent structural requirement is finite freshness: for each finite tuple, another element distinct from every entry is available. To match a new witness across two contexts, either reuse the corresponding existing value or choose a fresh value. These choices inspect equality patterns, not arbitrary formula truth. `truth_of_pattern` proves that the resulting relationship preserves every formula of this language.

On the natural numbers, a fresh value is constructed by taking one more than an explicit upper bound for the finite tuple (zero for the empty tuple). `finite_witness_reduction` shows that an existential formula needs only the tuple's existing values and this one fresh representative. The recursive Boolean function `evaluate` performs exactly that finite search. `evaluate_correct` proves correctness for every formula and assignment. `sentence_evaluation` transports the computed sentence truth to every carrier satisfying the same freshness condition, including carriers in other Lean universes.

This is a genuine bounded explanatory reduction: a uniform finite recipe determines the entire sentence theory of the specified class, without a sentence-truth oracle. The natural-number construction rules are zero and successor; their least-generation property is also checked. These rules belong to the construction background, **not** to the interpreted equality language. The result is not an arithmetic truth algorithm.

`double_preserves_all_equality_formulas` and `double_not_surjective` supply a second precise result: mapping each natural number to twice itself preserves every formula with transported parameters in this language while omitting ambient elements. Thus full truth preservation at this scope does not require a surjective representation. No nonisomorphism or language-independent sameness is inferred from this example.

This gives the affirmative constitutive reading concrete content: a subject's complete interpreted truth can express the constraints of an independently described generative role, rather than require a list of truth answers or every possible carrier element. The theorem establishes semantic adequacy; identifying that adequate role as the subject's constitutive ground remains the philosophical interpretation under examination.

## 3. The general theorem and the price of unrestricted witnesses

`WitnessHull.lean` uses arbitrary finitary function and relation symbols, finite-context terms and formulas, equality, negation, conjunction and existential quantification. Its derived universal-quantifier semantics is checked. An embedding must preserve functions and preserve and reflect atomic relations.

`elementary_iff_witness` establishes the exact additional condition for preserving **every** formula with internal parameters: whenever an existential formula has an ambient witness, it has one in the embedding's image. This is the standard Tarski–Vaught criterion, now checked in this representation. `Hull` then closes seeds under the original operations and a supplied family of correct witness selectors. `hull_elementary` proves that its induced structure preserves every such formula; `hull_least` establishes leastness **under those fixed rules and selectors**. It is not a selector-independent least elementary domain.

The positive construction has a real dependency. Suppose the language has two closed terms with distinct values, called the first and second tags. For an arbitrary sentence, request a witness equal to the first tag when the sentence holds, or the second tag when it does not. `selector_recovers_sentence` proves that the correct selector returns the first tag exactly when that sentence is true. This uses the actual syntax and interpretation, not a detached grounding predicate.

Consequently, an unrestricted semantically correct selector carries enough information to recover every sentence's truth through the specified tag test. Renaming it a primitive generative operation would not by itself reduce that truth commitment. This is not a blanket noncomputability theorem: some theories are decidable, and no effective selector or effective tag comparison is inferred merely from semantic existence. The equality evaluator provides a concrete positive case where independently specified rules do earn the required adequacy.

The general module also checks a substantive failure case. Natural numbers embed into integers preserving zero and successor, yet only the integers satisfy the sentence asserting a predecessor of zero. The changed quantifier domain matters despite exact compositional embedding; no unrelated predicate has been switched. This shows what a proposed generated subdomain must account for, not that the two subjects should have the same truth.

## 4. What this does for unique constitution

The affirmative result removes one excessive demand: constituting all truth in a stated language need not mean retaining every carrier object. It adds a positive method: specify witness rules independently, prove their full semantic adequacy, and compare the resources used with those previously supplied. The selector test rejects an apparent reduction that merely packages full truth into an unrestricted instruction.

The strongest rival preserves the same unfolding, equality patterns, witness construction, logic and all checked consequences. It can treat the mathematical role as the subject while leaving the ultimate dependence of those structural and logical resources unsettled, or explaining them in another direction. Such a rival is not refuted by describing it as an external mathematical realm. If its account is only another articulation of the same constitutive relations, an explicit equivalence could absorb it; agreement on truth values alone does not establish that equivalence of explanation.

Two burdens therefore remain for the requested thesis:

1. **Universal coverage:** derive or independently justify adequate formation, identity, domain and interpretation principles beyond pure equality, without supplying each new subject's full truth content as a rule.
2. **Exclusive explanatory priority:** establish why those principles hold in virtue of this substantive root, or why every adequate rival instantiates the same constitutive dependence. A different vocabulary is not automatically a rival, and identical mathematical predictions do not determine explanatory direction.

Freshness, the natural-number background, finite syntax, classical interpretation and the selected language remain explicit inputs to this round. The general hull additionally supplies its ambient structure and correct selectors. The Lean metatheory is not derived from the process root. These are local explanatory commitments to investigate within the one unfolding, not evidence for separate ontological realms. Neither “no custom axioms” nor a checked conditional theorem meets the stronger no-assumptions aspiration by itself.

## 5. Review, primary evidence and the next reduction

Root and the internal reviewer read both complete Lean modules. The review preserves fixed-selector leastness, internal-parameter scope, two named distinct tags, the executable evaluator's restricted language, and the absence of a generic noncomputability claim. The affirmative note distinguishes no additional mathematical bearer from no additional foundational resource. This is internal collaborating-AI review, not external peer review.

The source investigator directly rechecked selected original Open Logic completeness material, the HoTT Book's universe-specific univalence passage, selected statements and limitations from *The Univalence Principle*, and the official mathlib elementary-substructure source and documentation. Root read the [assessment](ROOT-MATHEMATICAL-UNIVERSALITY-SOURCES.md), not those entire external works. The sources establish standard antecedents and scope, not the present metaphysical thesis. No external source bytes or new empirical evidence were imported.

The next substantive reduction is to a richer language whose existential witnesses follow from independently described structural operations. The new operation must be justified through its actual role, with a checked adequacy argument and a comparison against a matched structural explanation. Merely adding a correct selector for every formula fails the resource test. More advanced cases cannot be counted as universal coverage unless the common admission and interpretation scheme itself is justified.

The [document receipt](ROOT-MATHEMATICAL-UNIVERSALITY-CHECKS.json) checks the owned integration and links separately from the Lean build. The older completion package remains intact. This round advances the stronger claim through a positive reduction and a tested limit on unrestricted witness-based explanation; it does not replace the stronger objective with this fragment's success.
