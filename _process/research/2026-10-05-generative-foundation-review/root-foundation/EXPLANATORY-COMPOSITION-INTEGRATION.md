# Contextual substitution, canonical factors and structural uniqueness

8 October 2026, Asia/Bangkok. AI-authored research under [Ren’s request for stronger structural uniqueness](../../../../sources/15-codex-theory-conversations/2026-10-08-generative-explanatory-necessity.md#更强的结构唯一性--stronger-structural-uniqueness). This continues the [matched structural comparison](EXPLANATORY-STRUCTURE-INTEGRATION.md) in its existing workspace. The [current theory](../../../../theories/becoming/chapters/EXPLANATORY-NECESSITY.md#23-从相同回答到可替换的片段) contains the Chinese account.

**Result:** for a fixed candidate-word language and concatenation, exact reduced presentations of all two-sided contextual answers have a canonical bijective matching preserving composition and the empty word. Composition on used codes is proved total, single-valued, associative and unital. A general exact reduced presentation exists; every exact presentation, even one with redundant distinctions, has a canonical surjective functional matching into it preserving the induced composition relation. The earlier one-event budget has exactly three contextual classes and a forced multiplication table. This is a relative structural uniqueness result, not unique ontology or a discovery of all truth.

**36 new Lean theorems and 74 inherited audits pass: 110 total.** New declarations: 15 empty dependency lists, 18 using only `propext`, and 3 using `propext` plus `Quot.sound`. With inherited declarations: 77 empty, 30 `propext` only, 3 with both. No custom axioms, proof holes or `Classical.choice`. The standard dependencies and the mathematical premises remain separate; the package is not called zero-axiom.

## 1. The bridge and its independently supplied target

The preceding theorem identified equal answer distinctions, but it did not show that a composition of codes existed or was preserved. We now ask about **replacement within a larger candidate realization**. In the formal model a word is a finite list of event labels. Prefix, inserted fragment and suffix are analytical positions in one composed word. They are not independently existing agent/environment, law/flow or subject/object domains. The [nondual method](../../../../theories/becoming/chapters/NONDUAL-METHOD.md) requires retaining the relationships that these positions expose and stating what the representation omits.

Supplied before choosing a presentation:

- a type `A` of labels and the candidate domain `List A`;
- list concatenation and the empty list;
- a predicate `L : List A → Prop`, specifying accepted candidate words;
- queries `(left, right)` ranging over **all** pairs of words, answered by `L (left ++ word ++ right)`.

Here acceptance is a specified realization/recognition target, not ethical goodness. Failed candidate words are included in the query domain. Formal concatenation is always defined even when the result is rejected by `L`. This interface does not yet model typed boundaries, concurrent joining, multiple outcomes, finite observational access or all actual physical processes. It also does not prove that the specified predicate is empirically correct.

Two fragments are context-equivalent when every such insertion question has the same answer. The new requirement is substantive: it strengthens the target from a fragment’s current result to its contribution within any declared composition. It is appropriate where that compositional behavior is the intended explanandum. It is not a definition of all sufficient explanation, and it would be unfair to impose it on a rival whose agreed target is only one local obstruction.

## 2. Substitution forces congruence and a code operation

`ContextEq L x y` is defined from the preceding `SameAnswers` interface. Reflexivity, symmetry and transitivity are checked. `context_append` proves:

> If `x` and `x'` agree in every two-sided context, and so do `y` and `y'`, then `x ++ y` and `x' ++ y'` agree in every context.

The proof replaces one fragment, then the other, using enlarged contexts. It does not assume that the presentation already preserves a binary operation. `context_stable` gives arbitrary prefix/suffix replacement. Conversely, `stable_relation_refines_context` proves that **every** relation stable under these insertions and respecting the standalone `L` answer refines contextual equivalence. Together with the equivalence laws and base-answer agreement, this characterizes the coarsest substitution-compatible equivalence retaining `L`.

For any presentation `p`, define `Compose p a b c` by witnesses `x,y` whose codes are `a,b` and whose concatenation has code `c`. This relation exists whether or not it is functional. If `p` is exact for the contextual target and reduced, `encoded_append_congr` makes the output independent of representatives. The resulting relation is total on used codes, single-valued, associative, and has `p.encode []` as left and right unit.

This is a monoid structure represented through its operation graph on used codes. We do not claim to have constructed a mathlib `Monoid` instance or a chosen function-valued `Equiv`; the checked relational laws and correspondence are the stated artifact. Unused code values remain outside the theorem.

## 3. From correspondence to structural uniqueness

The inherited `Matches p r` aligns two codes by a common candidate word. For two exact reduced presentations, the previous proof supplies a bijection on used codes. `matching_preserves_composition` now proves preservation **and reflection** of `Compose` under three aligned code pairs. `matching_preserves_identity` aligns the empty word. `structural_unique_correspondence` bundles those statements.

Thus, once candidate words and their contextual answers are fixed, reduced presentations carry isomorphic induced composition structures. The comparison does not assume a homomorphism field. The force comes from accurate answers to composition-sensitive questions and the separately stated reduction condition.

The uniqueness qualification matters. The inherited `unique_matching` establishes uniqueness **among functional correspondences aligning the encodings of every shared word**, restricted to used source codes. We do not assert that the bare algebra has no automorphisms when that alignment is forgotten. Nor do we infer a unique concrete mechanism, history, vocabulary or explanatory direction. The previous compact whole-constraint account survives: when it preserves the same contextual target, this theorem applies to it too.

## 4. General existence and the common factor without minimality

`canonicalSummary L` encodes a word by its complete contextual answer predicate and reads it by application. `canonical_exact` and `canonical_reduced` prove exactness and reduction for every supplied `L`; `reduced_presentation_exists` records the existence theorem. This removes the earlier existential gap at the mathematical level. It does not establish a finite representation or an algorithm for deciding, discovering or acquiring the answers. The complete answer profile is an existence witness, not independently an explanatory mechanism.

`canonical_factorization` weakens the demand on a rival: it needs only exactness, not reduction. Its used codes match uniquely onto used canonical profiles, every canonical profile is reached, and each induced composition is preserved. The inherited `unique_matching` fixes this factor among aligned functional matchings. The empty word also matches by `matching_preserves_identity`.

For a redundant presentation, its induced source `Compose` can be multi-valued. Accordingly this theorem is a **surjective functional matching preserving a relation**, not an unconditional monoid-homomorphism theorem about every exact code. With source reduction, the proved code monoid laws and inverse-functional matching upgrade the common factor to the preceding structural isomorphism.

This is the sharper necessity result: any accurate account of the entire declared contextual behavior must retain enough distinctions to recover the same minimal compositional content. It can retain more. This does not prove that every adequate explanation of an arbitrary target must answer this larger family.

The existence construction explicitly uses proposition and function extensionality. Lean’s actual audit includes `propext` and `Quot.sound` for `canonical_reduced`, `reduced_presentation_exists` and `canonical_factorization`. They are standard logical dependencies, not empirical or ontological postulates, but they must not be reported as empty dependency lists. No inverse is chosen with `Classical.choice`.

## 5. A concrete forced three-class structure

Return to the first study’s one-event budget: `L word` means that the word is empty or contains one event. The alphabet is `Unit`. Arbitrary candidate words divide into `empty`, `single`, and `overflow` (two or more). Exactness, reduction and the following operation are checked:

| Concatenate | empty | single | overflow |
|---|---|---|---|
| empty | empty | single | overflow |
| single | single | overflow | overflow |
| overflow | overflow | overflow | overflow |

`classify_append` proves the table’s correspondence with concatenation for **all finite words**, not only a sample. `budget_composition` identifies the table with the induced composition relation. Every bucket is used. An exact summary must distinguish the empty word, the single event and the double event (`three_distinctions_required`), even without assuming reduction. With reduction, `budget_kernel_characterization` proves that two codes are equal exactly when their buckets are equal. This gives exactly three used classes; the general structural theorem fixes their table up to word-aligned isomorphism.

Why must the first two differ when both are accepted? Appending one event keeps the empty fragment within budget and pushes the single-event fragment over budget. The distinction is forced by continuation behavior, not by a prescribed three-state code. The explicit three-state presentation is subsequently proved exact and reduced.

`overflow` describes rejected **candidate words**. It is not an additional reachable legal state in the earlier bounded-history process, whose admitted histories have at most one event. Keeping that distinction prevents an artificial violation of the original process law.

## 6. Matched counterexamples and substantive counterreview

For the independent target `L word := word = [true, false]`, two checked contrasts show why the extra contextual requirement does work.

- The empty word and `[true]` are both rejected now. Appending `[false]` rejects the first composite and accepts the second. Present rejection alone loses a compositional distinction.
- `[false]` and `[true,true]` remain rejected under **every suffix**. Prefixing `[true]` accepts the former and rejects the latter. Right-context equivalence therefore cannot generally stand in for two-sided fragment equivalence. It remains useful for deterministic automaton states and right extensions; we do not reject that different target.

| Objection | Result and remaining limit |
|---|---|
| The desired operation-preservation is hidden in the definition. | Concatenation and contextual questions are supplied; `Exact` and `Reduced` contain no homomorphism field. Congruence and preservation are proved. The underlying concatenation itself is not derived from reality. |
| Only minimal rivals are considered. | Canonical factorization now covers every exact contextual presentation. Reduction is required for bijection, not for necessary recoverable content. |
| The theorem may be vacuous because no reduced account exists. | A general mathematical existence witness is checked, and the budget has a finite explicit instance. Effective discovery and empirical acquisition remain open. |
| Accurate present answers should be sufficient. | The checked pattern cases show the specific information lost. They preserve the same base predicate and concatenation; no arbitrary verdict toggling is used. |
| The canonical profile explains why the accepted cases occur. | Not established. It packages all contextual answers; explanation, accessibility and formation require additional arguments. |
| An isomorphism makes our generative formulation uniquely fundamental. | Not established. Global, algebraic or process presentations preserving the target receive equal status. No priority or universal domain-admission argument is supplied. |
| This derives a favorable normative direction. | No. `L` supplies acceptance/realizability, not worth. The result can constrain factual distinctions in a practical account but does not replace G0 or explicit comparison commitments. |

This is substantive counterreview by the authoring agent, not an independent-agent review. The concrete counters test the actual strengthened target. We do not use freely adjustable predicates in a weakened model to refute the fuller one-process theory.

## 7. Prior mathematics and source assessment

This is an application and Lean reconstruction of a known syntactic-congruence route, not a novel discovery of that route. Read: Jiří Adámek, Stefan Milius and Henning Urbat, [A Categorical Approach to Syntactic Monoids](https://arxiv.org/html/1804.03011v2), introduction, Definition 3.6, Definition 3.13, Theorem 3.14 and its proof, and Example 3.15(1). Their two-sided congruence and quotient universal property provide the primary comparator. Their broader categorical results require their stated algebraic hypotheses; those generalizations are not proved here. Our artifact uses arbitrary predicate languages, explicit presentation/readout interfaces and relational operation graphs; its contribution here is integration with the explanation-necessity investigation, checked scope and the reused budget example.

Pin’s author-hosted [MPRI notes](https://www.irif.fr/~jep/PDF/MPRI/MPRI.pdf) and [Syntactic semigroups chapter](https://www.irif.fr/~jep/PDF/HandBook.pdf) were located in search, but direct retrieval timed out or was restricted. They are discovery pointers only, not full-text evidence. Access date: 8 October 2026 local time. All external sources remain link-only; no original bytes were imported or altered.

## 8. Complete proof inventory and validation

[ExplanatoryComposition.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/ExplanatoryComposition.lean), 36 new theorems:

| Group | Count | Declarations |
|---|---:|---|
| Contextual relation | 7 | `context_refl`, `context_symm`, `context_trans`, `context_agrees_here`, `context_append`, `context_stable`, `stable_relation_refines_context` |
| Induced operation | 7 | `encoded_append_congr`, `compose_encoded_iff`, `compose_total`, `compose_functional`, `compose_associative`, `compose_left_identity`, `compose_right_identity` |
| Structural correspondence | 5 | `matching_composes`, `matches_swap`, `matching_preserves_composition`, `matching_preserves_identity`, `structural_unique_correspondence` |
| General existence and factor | 4 | `canonical_exact`, `canonical_reduced`, `reduced_presentation_exists`, `canonical_factorization` |
| Missing-context counters | 2 | `suffix_tests_can_miss_left_context`, `current_answer_can_miss_composition` |
| Budget instance | 11 | `classify_representative`, `classify_append`, `accepted_classify`, `budget_exact`, `bucket_separated`, `budget_reduced`, `every_bucket_used`, `budget_composition`, `any_exact_summary_retains_buckets`, `three_distinctions_required`, `budget_kernel_characterization` |

Run `python3 experiments/integrated-correction/general-framework/generative-basis/lean/deeper/check_explanatory_composition.py` from the repository root. The [final immutable receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/explanatory-composition-checks/20261007T223124.386181Z/receipt.json) contains fresh Lean 4.29.1 compilation of six copied modules and the exact dependency lists. Sources and logs are frozen and hash-bound. The checker rejects proof holes, custom axioms, warnings and dependencies outside `propext`/`Quot.sound`. Standard dependencies are disclosed rather than conflated with supplied premises.

All 110 declaration audits pass: 36 new plus 74 inherited; 77 empty, 30 with only `propext`, and 3 with `propext` and `Quot.sound`. The general `structural_unique_correspondence` statement has an empty dependency list, but the operation-law and existence proofs do not all do so. No package-wide zero-dependency assertion follows. An earlier successful 29-theorem receipt is preserved as a development snapshot, not another result or validation of the later seven theorems. Prior modules and receipts are unchanged.

[Document and binding checks](EXPLANATORY-COMPOSITION-CHECKS.json) verify local links, frozen/current source agreement, proof inventories and owned paired rows. [Shared edit records](EXPLANATORY-COMPOSITION-INDEX-EDITS.json) preserve other entries and surrounding shared-file bytes. They do not recertify other sessions’ substantive work.

## 9. Integration and the next unresolved bridge

The research chain now distinguishes: target answers → contextual substitution → induced associative composition → general canonical existence and a common factor → reduced structural uniqueness. This answers the previous composition question in the fixed word-language interface. It supplies a necessary common structural content for **all exact accounts of that interface**; that is stronger than a bijection among arbitrary answer codes.

The next universal inference to test is whether the relevant composition interface itself can be justified from the target’s joint realization conditions, without presupposing one total linear concatenation model. Begin with boundary-sensitive partial joining: derive which replacements remain composable from the same relations used to specify the target, and require local/global rivals to preserve those boundary and failure conditions. A rival preserving the whole intended content but not the proposed composition would show a mischosen interface; verified reconstruction of the interface from independently motivated target questions would strengthen necessity. General concurrent joining, empirical identification, explanatory priority and universal ontology remain separate open obligations.

This continuation preserves the previous mathematical obstruction, evidence-acquisition and normative branches at their original scopes. It does not restart their completed conditional mechanisms or treat this structural bridge as universal ethical grounding.


## 10. Successive continuation: partial joining and recovered interfaces

Ren’s subsequent “继续然后再继续” authorized the [two-stage partial-joining study](EXPLANATORY-JOINING-INTEGRATION.md). It adds 54 checked theorems: empty-history probes recover interface information, and the ternary joining relation uniquely determines local-unit roles under explicit conditions. A partial budget refutes unconditional matching-unit sufficiency; an exact chain-completion criterion and the complete finite-trace realization are checked. The preceding 36-theorem package and its standard extensionality dependencies retain their original scope. The next target is supported separating tests for definedness and output content under shared conditions and concurrent conflicts.
