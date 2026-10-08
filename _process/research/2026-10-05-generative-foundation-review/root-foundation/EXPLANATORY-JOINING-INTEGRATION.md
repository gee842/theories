# Partial joining, reconstructed interfaces and the completion boundary

8 October 2026, Asia/Bangkok. AI-authored research under [Ren’s instruction to continue through successive stages](../../../../sources/15-codex-theory-conversations/2026-10-08-generative-explanatory-necessity.md#连续推进--continue-and-continue). This follows [contextual composition](EXPLANATORY-COMPOSITION-INTEGRATION.md), preserving its 36 results and its explicitly supplied concatenation interface. The [current Chinese account](../../../../theories/becoming/chapters/EXPLANATORY-NECESSITY.md#32-把能否接合纳入结构本身) integrates both new stages.

**Result:** empty-history joining probes recover the interfaces and pairwise joinability of endpoint-sensitive finite fragments. Next, without a primitive boundary map, local units and associativity uniquely determine each fragment’s unit interfaces. A bijective preservation of the ternary joining relation automatically preserves these units. In the admitted finite-trace realization, the recovered unit collection is exactly the supplied state collection, with unique correspondence. Crucially, matching units alone need not make a composite exist: the one-event budget is a checked counterexample. A separately stated chain-completion law is exactly equivalent to the sufficiency of matching units under the other declared laws; finite endpoint traces satisfy it.

**54 new Lean theorems: 23 joining results, followed by 31 unit/reconstruction results.** The final seven-module run audits 128 declarations, including 74 inherited ones: **105 empty dependency lists and 23 using only standard `propext`**. The 54 new declarations comprise 43 empty and 11 `propext`-only audits. No custom axioms, `Classical.choice`, `Quot.sound` or proof holes occur in this new checked inventory. The previous general answer-profile existence theorem used `Quot.sound`; it retains that original audit and is neither reclassified nor counted as newly proved here.

## 1. The universal inference advanced and the representation retained

The preceding study supplied total word concatenation and asked all two-sided questions. The next question was whether the applicable interface can itself be recovered. This round separates two tasks: infer interface information from joining answers in a specified realization; and characterize interface roles internally to a partial joining structure. Neither task derives the universe of all possible processes or the correctness of a supplied process law from nothing.

The [nondual method](../../../../theories/becoming/chapters/NONDUAL-METHOD.md) guides the interpretation. Start, event word, finish, unit and composite are differentiated positions/roles in one admissibility account. They are not independently existing actor, passive world and external law. A supplied local transition law is not thereby external to the whole. A state records the conditions this model retains, including capacity in the concrete budget process.

The first representation is a finite candidate fragment `(start, word, finish)`. `Valid P f` means that the supplied process admits that finite endpoint trace. This records existential trace content, not each hidden intermediate route separately; multiple routes with the same word and endpoints can have the same fragment. No global initial state is fixed, so even an empty trace at a state unreachable from a separately chosen root remains in this mathematical candidate domain. That does not assert its physical availability to an experimenter.

`Joint P f g` requires both fragments to be valid and the actual finish of `f` to equal the start of `g`. `Joined P f g h` additionally identifies the composite’s word and endpoints. There is no legal product when the boundaries disagree. The old total concatenation remains a syntactic operation on words; it no longer silently stands for admitted joining.

The concurrent [unfolding-preservation study](UNFOLDING-PRESERVATION-INTEGRATION.md), read in full during integration, already connects exact native endpoint accounts to joining/substitution and supplies same-law acquisition, error and continuation contrasts (42 theorems / 64 new declaration audits in its own record). We also inspected its generic joining theorem statements/proofs. Those results and its independent review retain their own validation scope; they are not added to this study’s 54 or treated as an independent review of this package. The first stage here isolates empty-history probe identification and its lost-word limitation; the second reconstructs intrinsic unit roles and characterizes completion. Existing shared-chapter §§29–31 were preserved; this continuation occupies §§32–38.

## 2. First continuation: recoverability from joining probes

The empty-history fragment `idle s` is valid at every supplied state `s`. It denotes the zero-event trace, not an arbitrary positive-duration wait in which conditions cannot change.

The first proofs establish:

- a pair is joint exactly when it has a joined output; that output is unique and valid;
- admitted joining is relationally associative and has the appropriate left/right empty-history units;
- `idle s` can precede a fragment exactly when the fragment is valid and `s` is its start; it can follow exactly when it is valid and `s` is its finish.

Therefore two **valid** fragments agree on all such before/after probes exactly when they have the same endpoints. Exact code readings of these probes must retain their endpoint distinctions. More strongly, two arbitrary candidate fragments are joint exactly when some empty-history probe can follow the first and precede the second. `exact_reads_recover_joint` reconstructs that answer from any exact presentation/readout, without requiring the presentation to store named endpoints or have an assumed joining operator.

This is informational recovery relative to a supplied separating family of tests. The probes are independently identifiable empty traces in this model, but their identity and formal scope are still provided. The theorem does not claim that the endpoint labels or every probe were learned from finite evidence. Nor does it certify a device implementing them. Those are distinct formation/access/correspondence questions.

A precise limitation is checked: in a one-state process admitting both Boolean events, two different one-event loops have exactly the same boundary probes and different event words. Joinability information is enough for this interface question, but does not recover all internal word or outcome content. We preserve that counterexample rather than enlarging the agreed target without explanation.

## 3. Second continuation: recover interface roles from a ternary relation

Now take a carrier `F` and a relation `J a b c`, meaning that joining `a` then `b` yields `c`. No state type, start map, finish map or list operation occurs in the abstract definitions.

The assumptions are separate:

| Condition | Exact role |
|---|---|
| `Functional J` | A pair has at most one output; an output need not exist |
| `Associative J` | An output has a left-bracketed two-stage witness iff it has a right-bracketed witness |
| `Neutral J e` | Whenever `e` participates on either side, the output equals the other fragment |
| `HasUnits J` | Each fragment has an actually composable neutral fragment on each side |
| `ChainComplete J` | Whenever `a,b` and `b,c` are composable, a joined whole of the three exists |

`Neutral` alone can be vacuous at an isolated element; with `HasUnits`, `neutral_self_composes` rules out that issue for a neutral element by deriving its self-composition. Unit existence is an explicit premise and not a statement that all physical interactions have a neutral operation.

Associativity makes each fragment’s left unit unique and its right unit unique. With `HasUnits`, their existence and uniqueness are packaged without choosing global functions. `boundary_assignments_unique` shows pointwise agreement of any two proposed left/right assignments satisfying these roles. These are reconstructed **unit interfaces**, not a theorem identifying every physical boundary with a mathematical identity.

A further structural result uses a bijection of carriers preserving and reflecting `J`. `neutral_transport`, `left_unit_transport` and `right_unit_transport` derive preservation of the reconstructed units. They do not assume separate unit or endpoint preservation fields. The full composition-graph correspondence is an explicit premise; these theorems do not manufacture that premise from the weaker probes of the first stage.

This removes one form of arbitrary extra structure: once the admitted composition relation and unit roles are fixed, compatible unit interfaces cannot be assigned freely. It remains relative to that relational content and those laws.

## 4. A genuine failure: equal interfaces do not always suffice

Use the earlier one-event budget with a genuinely partial multiplication. There are two admitted fragments: empty (`false`) and one event (`true`). Empty joined with anything returns that fragment. One event joined with another event has **no admitted output**.

| Partial join | empty | one event |
|---|---|---|
| empty | empty | one event |
| one event | one event | undefined |

Lean checks functionality, relational associativity and local units. The one-event fragment has the empty fragment as both units, so its interfaces match itself. Nonetheless its self-composition is absent. `budget_matching_does_not_suffice` proves these facts together; `budget_not_chain_complete` identifies the failed completion condition.

This is the same capacity restriction as the prior at-most-one-event target, with the representation change explicit. The previous three-class total summary includes an `overflow` class for rejected candidate words. The present partial algebra excludes rejected outputs; it does not falsify the earlier total table or pretend that `overflow` was an admitted event history. It is also distinct from the endpoint-sensitive capacity process below.

The example is a substantive restriction on a universal category-shaped conclusion. Associativity, identity-like roles and defined units do not by themselves make every matching pair realizable. This exact small partial-monoid shape also appears in the prior mathematics credited below; we do not claim it as a new mathematical counterexample.

## 5. The missing condition is characterized, not concealed

From a joined pair one can derive a shared right/left unit using associativity and local-unit existence; matching units are therefore necessary under these conditions. To make them sufficient, `ChainComplete` explicitly requires whole-chain realization from adjacent composability.

The checked equivalence is:

> With relational associativity, functionality and local units, chain completion holds **if and only if** every common-unit pair has a composite.

`chain_complete_iff_unit_matching_suffices` proves both directions. This is an exact characterization of the additional structural commitment, not a proof that it holds for every generative situation. The budget counterexample prevents silently adding it to “sufficient explanation.” The product’s left unit comes from the first fragment and its right unit from the second (`left_unit_of_product`, `right_unit_of_product`); those transport laws support the converse direction.

A constraint or resource view preserving this failed composition remains a valid rival. A broad one-process theory can describe both completion and its failure; it cannot infer universal categorical completion merely by calling the relation generative.

## 6. The finite-trace realization satisfies the condition and recovers its states

Restrict the first module’s fragments to those satisfying `Valid`. On this carrier, `traceJoin` retains the full joined relation. The second module checks functionality, relational associativity, local units and chain completion for **every supplied process**. The chain result follows from exact intermediate-condition alignment and the inherited finite-trace concatenation theorem; no scalar objective, deterministic transition assumption or favorable direction is added.

In this representation, matching units do characterize composability. Moreover:

- `trace_left_unit_iff` and `trace_right_unit_iff` identify the unique units with the empty histories at the actual start and finish;
- `trace_neutral_iff_idle` proves that the entire recovered neutral collection consists exactly of those empty histories;
- `trace_idle_injective` and `recovered_boundary_unique` prove that each recovered unit corresponds to one and only one supplied state.

The state collection is thus recoverable from the admitted-fragment composition structure, not an independently variable addition once that whole structure is fixed. This is structural recovery, **not** derivation of the physical existence of those states or proof that the starting representation retains every relevant condition. Its quantification is over the given process interface, including all its candidate states.

The concrete one-event transition goes from `false` (capacity remains) to `true` (capacity spent). The spend fragment is valid, cannot self-join, and its two empty-history interfaces are distinguishable. Unlike the coarse two-element partial budget algebra, this endpoint-sensitive representation retains changing capacity in the interface. We do not claim the two algebras are isomorphic: merging the two empty-history interfaces loses exactly a distinction relevant to composability. The stronger trace representation and the weaker word-only target retain separate declared content.

## 7. Counterreview and interpretation

| Challenge | Assessment |
|---|---|
| The first module already names endpoints. | Correct. It proves their recoverability through formal joining tests in that realization, not their origin from unlabelled finite observations. The second module separately removes primitive boundary maps from the abstract formulation. |
| The second module assumes the whole joining relation. | Correct. Its advance is unique recovery of unit interfaces and a precise completion criterion. Recovering the full relation from independently accessible evidence remains unfinished. |
| Mere joinability recovers the entire process. | Refuted by the two distinct one-event loops with equal boundary probes. Output/internal-content questions require richer evidence. |
| Unit matching always guarantees realization. | Refuted by the checked partial budget despite its associativity and units. Whole-chain completion is additional. |
| The trace example settles the condition universally. | It settles it for endpoint traces of a supplied step relation. Adequacy of the state description, jointly shared capacities, concurrency and physical correspondence are separate. |
| Different unit sets are an ontological subject/object split. | They are distinguished roles recovered from the same joining relation. No separate observer or passive domain is introduced. |
| This proves one uniquely fundamental generative ontology. | No. Equivalent whole-constraint, algebraic and process descriptions retain the same standing. Formation and explanatory priority need their own arguments. |
| This supplies universal ethical authority. | No. The study concerns realizability and structural distinctions. It helps identify factual conditions relevant to practical comparison but does not supply G0 or a comparative normative commitment. |

This is counterreview by the authoring agent. No independent agent was requested or invoked. Failed claims and representation differences are part of the result, not discarded development noise.

## 8. Primary-source assessment and genealogy

Read James Cranch, Simon Doherty and Georg Struth, [Relational Semigroups and Object-Free Categories](https://arxiv.org/pdf/2001.11895), §§2–3, the object correspondence in §4 and examples 6.3–6.4. The paper distinguishes relational associativity, functionality, units and coherence; its Lemma 3.6 relates coherence to matching-unit composability. Example 6.4(1) has the same two-element partial-budget shape. Our `ChainComplete` and symmetric neutral-role formulation are stated explicitly and checked in Lean rather than identified by terminology alone. The endpoint-trace instantiation and integration with the earlier explanatory tests are the contribution to this repository; the abstract route and counterexample have prior mathematical standing.

The arXiv HTML request failed; the six-page PDF was readable. The abstract supplied metadata, and the named sections of the PDF supplied the substantive comparison. Accessed 8 October 2026 local time. The source remains link-only; no source bytes or adapted reading edition were imported. The preceding syntactic-congruence sources retain their original reading scopes; no whole-book or literature-exhaustiveness claim is made.

## 9. Complete Lean map and verification

[ExplanatoryJoining.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/ExplanatoryJoining.lean): **23 new theorems**.

| Group | Count | Declarations |
|---|---:|---|
| Valid joining and association | 9 | `idle_valid`, `joint_iff_joined`, `joined_functional`, `joint_merge_valid`, `joined_valid`, `merge_associative`, `joint_chain_left`, `joint_chain_right`, `joined_associative` |
| Empty-history probes and units | 4 | `idle_left_probe`, `idle_right_probe`, `joined_idle_left`, `joined_idle_right` |
| Recovery and replacement | 5 | `same_probes_iff_boundaries`, `probes_recover_joint`, `exact_codes_retain_boundaries`, `exact_reads_recover_joint`, `boundary_replacement_preserves_joint` |
| Concrete distinctions and loss | 5 | `spend_valid`, `spend_cannot_self_join`, `boundary_idles_distinguished`, `loop_valid`, `probes_miss_internal_word` |

[ExplanatoryLocalUnits.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/ExplanatoryLocalUnits.lean): **31 new theorems**.

| Group | Count | Declarations |
|---|---:|---|
| Unique unit roles | 4 | `left_unit_unique`, `right_unit_unique`, `neutral_self_composes`, `local_units_exist_uniquely` |
| Composition and exact completion criterion | 7 | `joined_common_unit`, `composable_common_unit`, `left_unit_of_product`, `right_unit_of_product`, `common_unit_suffices_when_complete`, `composable_iff_common_unit`, `chain_complete_iff_unit_matching_suffices` |
| Reconstructed boundary uniqueness and transport | 4 | `boundary_assignments_unique`, `neutral_transport`, `left_unit_transport`, `right_unit_transport` |
| Partial budget | 5 | `budget_functional`, `budget_associative`, `budget_has_units`, `budget_matching_does_not_suffice`, `budget_not_chain_complete` |
| Complete trace realization and state recovery | 11 | `trace_join_functional`, `trace_join_associative`, `trace_idle_neutral`, `trace_has_units`, `trace_chain_complete`, `trace_left_unit_iff`, `trace_right_unit_iff`, `trace_composable_iff_common_unit`, `trace_neutral_iff_idle`, `trace_idle_injective`, `recovered_boundary_unique` |

The [first-stage receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/explanatory-joining-checks/20261007T225110.058337Z/receipt.json) has 23 new / 97 total audits: 82 empty, 15 `propext` only. The [final combined receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/explanatory-local-units-checks/20261007T225438.405152Z/receipt.json) freshly compiles seven copied modules with Lean 4.29.1, checking all 54 new / 128 total declarations: 105 empty, 23 `propext` only. The first 23 are included in the 54, not counted twice.

Run `python3 experiments/integrated-correction/general-framework/generative-basis/lean/deeper/check_explanatory_local_units.py`. The runner binds current/copied source hashes and frozen logs, rejects proof holes, custom axioms, warnings and unlisted dependencies. The inherited runner allows `propext` and `Quot.sound`; the actual final inventory uses only `propext` among nonempty dependency lists. The document checker separately verifies that exact outcome. Explicit mathematical premises are not erased by an empty logical dependency audit. Boolean `decide` calls check the fixed budget cases inside Lean; the general uniqueness/completion proofs are symbolic, not inferred from finite tests.

The [local document/binding check](EXPLANATORY-JOINING-CHECKS.json) and [owned index record](EXPLANATORY-JOINING-INDEX-EDITS.json) connect this study to C30/F22. Source hashes record read versions and do not independently validate concurrent research. Development failures and the earlier 51-theorem successful snapshot remain historical receipts, not additional results. No existing proof module was changed.

## 10. Integrated result and next continuation

The two stages advance: supplied finite realization → tested interface distinctions → recovered joinability; then ternary composition → unique unit roles → exact completion criterion → reconstruction of the supplied state interfaces in the finite-trace realization. They establish more than an arbitrary relabelling of answer codes while making the missing information and structural assumptions visible.

The next generalization must preserve shared-capacity and concurrent conflicts rather than demand categorical completion everywhere. Investigate which independently specified joint-realization tests determine both **definedness and output distinctions** when tests themselves have support/access limits. Reuse the existing evidence-formation and calibration results at their scopes; do not restart them or assume that every distinguishing probe can be performed. A matched rival with the same available tests but different untested products would establish an identification limit; a reconstruction theorem under a justified separating family would strengthen structural necessity. Domain selection, formation, explanatory priority and universal ontology remain open.


## 11. Subsequent direct universal test

Ren’s later request redirects the immediate study to universal uniqueness until a substantive wall. The [61-theorem follow-up](EXPLANATORY-UNIVERSALITY-INTEGRATION.md) removes the special composition laws, characterizes relational recoverability, refutes unique minimal native realization from complete existential word answers, and proves the deterministic repair. The earlier shared-capacity/access proposal retains its local identification scope; it is not a prerequisite to acknowledging the checked universalization obstacle. This addition does not reclassify the 54 results or the concurrent unfolding-preservation review.
