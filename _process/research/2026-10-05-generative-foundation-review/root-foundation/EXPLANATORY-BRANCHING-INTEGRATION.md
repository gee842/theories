# Why explanatory adequacy can force branching structure

8 October 2026, Asia/Bangkok. AI-authored continuation of [Ren’s direct question](../../../../sources/15-codex-theory-conversations/2026-10-08-generative-explanatory-necessity.md#解释为何必须保留关系--why-preserve-relations). The [preceding universal attempt](EXPLANATORY-UNIVERSALITY-INTEGRATION.md) isolated target adequacy as the missing bridge. This round supplies a substantive scoped argument and checks its mathematical consequence, without defining explanation as agreement with the generative theory.

**Advance:** complete answers to finite compound questions about conditions and their possible continuation force a back-and-forth relation for image-finite processes. Determinism is no longer required. On reachable processes whose states are separated by these questions, the relation is a bijective structural correspondence preserving and reflecting steps. From any exact reduced answer encoding, a code-level process can be constructed; every finite code history lifts from every compatible native start. No transition decoder or homomorphism is a field of the initial explanation encoding.

**Limit:** the argument applies when the explanation claims to cover these compound continuation questions. It does not prove that every adequate local explanation has that scope, that all mathematical tests are physically available, or that all relevant processes are image-finite. Complete forward tests do not recover every actual formation history or arbitrary carrier identity. Universal unique ontology remains open.

**45 new checked theorems (18 + 18 + 9), 141 audits including 96 inherited.** The new package has 19 empty dependency lists and 26 nonempty standard lists: 3 `propext` only, 10 `propext` plus `Quot.sound`, and 13 additionally using `Classical.choice`. The complete run has 103 empty and 38 standard lists. No custom axioms or proof holes occur. In particular the general modal-to-branching converse uses classical reasoning; this package must not be called wholly “zero axiom.”

## 1. The affirmative argument and its independent scope

The defensible starting requirement is **fidelity to the claimed explanandum**: an account cannot erase a distinction that changes the answer to a question it claims to answer accurately. This requirement does not mention a favored generative ontology. A whole-constraint account, an algebraic account and a local process description face the same requirement.

A claim to explain *which conditions are formed and what they continue to make possible* concerns more than a list of eventual successes. It includes whether a particular occurrence leaves one further possibility, another, or both available at the **same reached condition**. These questions are motivated by the content being explained: capacity remaining, an option being lost, and whether apparent opportunities depend on mutually incompatible prior branches. An account that supplies two individually possible histories but cannot distinguish their incompatible conditions has not yet covered that richer target.

The argument proceeds through three distinct commitments:

1. The local conditions and occurrences mentioned by the question have independently warranted content and correspondence. This can be earned by construction or evidence; it is not universally an ungrounded input. Existing [effective-law and correspondence work](LAW-CORRESPONDENCE-INTEGRATION.md) retains its established scope.
2. The advertised explanation includes finite Boolean combinations and finite continuation of those questions. A correct account of *all such possibilities* cannot exempt a compound question merely because it distinguishes two candidate accounts.
3. In the selected model class, each condition/event has finitely many immediate successor states. This is a mathematical premise here, not a universal physical law.

The theorem derives structural matching from accurate answers under these commitments. Commitment 2 is not warranted for every adequate explanation of every topic: a parity proof, a selected endpoint explanation or an explicitly approximate account has a narrower task. Declaring that narrower task does not make it defective. Nor does the existence of a universal explanatory foundation imply that each local explanation must reproduce all its foundational detail.

This advances the universal programme at a precise point: *where the explanandum includes formation of later possibilities, branch correlation is necessary content, and a familiar finite question language can force structural recovery*. Whether every aspect of reality or every sufficient explanation falls within an appropriately generalized requirement is still a substantive universal inference. The formal theorem cannot establish its own unrestricted applicability.

## 2. Ordinary compound questions, not all predicates or named states

`Test A O` has five constructors:

| Constructor | Content |
|---|---|
| `top` | No further condition is required |
| `atom o` | The independently specified local condition `o` holds |
| `neg f` | `f` does not hold |
| `conj f g` | `f` and `g` hold at the same condition |
| `after a f` | There exists an admitted `a` occurrence reaching a condition satisfying `f` |

Every formula is finite, though the family of all formulas need not be finite. Event and condition symbols retain a fixed interpretation across the comparison. There are no singleton-state predicates or arbitrary predicates on the entire state carrier. The concrete branch witness even uses an empty atom vocabulary.

Conjunction expresses coexistence of truths at one condition. It does **not** assert that two destructive tests can both be executed on one specimen, that two events can occur simultaneously, or that selecting one option leaves the other intact. `after` describes admitted existence, not its probability or an ability to force the outcome. Semantic negation is not evidence of absence obtained by failing to observe an event. Actual acquisition, support and reliable negative evidence keep their existing separate scopes.

These analytical roles belong to one process. No external observer or passive world is added as an ontological primitive. A reading can itself be formed within that process, but the generic theorem neither constructs such an apparatus nor grants it access to all test answers.

## 3. Why the answers force branching

`Same m n s t` means agreement on every finite test. `Bisimulation` reuses the repository’s previously checked event-matching relation and adds agreement on the declared atomic conditions. The new result proves the converse of the familiar preservation direction:

> If each event has finitely many immediate successors, agreement on every finite test implies that each step can be matched by the other process, with the successor conditions again agreeing on every finite test; and conversely.

The key proof does real work. Suppose the first state can reach a successor that no successor of the second state matches. For each of the second state’s finitely many successors there is a separating finite question; negation orients it in favor of the first successor. Conjoin those finitely many questions, then ask whether the event can lead to that conjunction. The first state answers yes, the second no, contradicting their full agreement.

The finite conjunction step is separated from the classical proof extracting/orienting the distinguishing questions. Their exact dependencies appear below. There is no finite bound on history length or total state count. Image-finiteness is per state and event; the alphabet may also be infinite.

`exact_equal_codes_force_branch_matching` applies this directly to an ordinary `Presentation` with an encoding and answer reading. If it reads all these tests accurately, equal codes can only identify bisimilar native conditions. No native transition reading, step map, bisimulation proof or desired generative verdict is part of that presentation’s definition.

Bisimilarity does not by itself fix the number or names of observationally duplicate states. With reachability from matched roots and separation by the finite test family, `branching_structural_correspondence` gives total uniquely matched states in both directions. `correspondence_preserves_steps` preserves and reflects the native steps. This extends the preceding deterministic repair to nondeterministic, finitely branching models, at the cost of a genuinely richer question scope.

## 4. A matched target that exposes the missing correlation

The constructed comparison uses three events: `enter`, `left` and `right`.

- In the shared-condition version, `enter` reaches one condition from which either `left` or `right` remains possible.
- In the early-split version, `enter` reaches either a left-only or a right-only condition. No reached condition retains both options.

Both permit exactly the same finite words: the empty word, `enter`, `enter,left`, and `enter,right`. `root_words` and `same_all_words` prove this for every word; they do not check only a bounded enumeration.

The question

`after enter (after left top AND after right top)`

is true in the first version and false in the second. The conjunction is inside the scope of the same `enter` successor. Separate assertions that `enter,left` and `enter,right` are possible would lose that common-condition requirement. Thus the discrepancy is an actual difference of admitted continuation relationships, not an independently flipped predicate. `no_rooted_bisimulation` rules out every purported root-related bisimulation, regardless of node naming.

Both are valid explanations of the narrower feasible-word target. The early-split account cannot replace the shared-condition account for a target asking which options a particular reached condition retains. This supplies the independent meaning of the new question; it does not stipulate “accept generativity” as the right answer. The example is a formal construction, not a new physical experiment, and no additional minimum-state claim is made.

## 5. Derive the effective law and prevent fictitious histories

For an exact **reduced** encoding of the finite test answers, admit a code transition only when a native edge witnesses it. Reduction here means identifying states agreeing on every test; it is not merely minimizing the number of native states.

An existential projected edge alone can be misleading if consecutive edges rely on incompatible representatives. `code_step_lifts_from_every_representative` eliminates this issue: every coded edge can be realized from any native start carrying that source code, reaching a native successor carrying the destination code. Finite branching plus the test-equivalence theorem supplies the matched successor; exactness and reduction turn its equivalent answers into the correct destination code.

`code_trace_iff_native` extends the property to arbitrary finite histories. Every code history starting at an encoded native state lifts from that particular state, and every native history projects. This preserves valid sequential joining and avoids creating histories by silently switching representatives. It is not a general theorem about arbitrary parallel resource composition or all forms of concurrency.

The graph of the encoding is itself a bisimulation of the native and constructed code models, and the code model’s test semantics agrees with the given readings on used codes. Any competing code law with the same representative-wise exact one-step outcomes agrees on used source codes. If the native model is already separated by tests, the native edge relation is recovered exactly under the encoding; that last injectivity argument needs neither image-finiteness nor reduction in addition to exactness and native separation.

This is a generalization alongside the existing concrete effective-law study, not a replacement for it. There, summary sufficiency was proved from unchanged native branches. Here, the generic finite-test adequacy and image-finite hypotheses imply the sufficient correspondence. Neither result proves that a particular native architecture is the only one reality can have.

## 6. Formation history and carrier identity remain differentiated

The prior `RelationalDynamics` work already shows that static and toggling Boolean carriers can be bisimilar when no condition distinguishes the carrier labels. The new `static_toggle_same_all_tests` connects that established result to the entire finite test language. Forward relational questions do not automatically read the carrier’s equality or impose its state names as essential content. This preserves the nondual relational correction; it is not presented as a new independent refutation.

A separate concrete construction admits both a one-event and a two-event history from the same root to exactly the same endpoint. Every endpoint-based forward test agrees there. `actual_length_not_endpoint_readable` proves that no endpoint reading can return the length of every actual history reaching it. This is an actual information-loss witness, not merely the assertion that some unspecified past might differ.

Consequently a full account of future capacities can omit past distinctions that have no retained effect in its target. An explanation of *which past formation actually occurred* has a different obligation and needs relevant records, predecessor relations or other independently supported historical information. The present theorem does not recover actual provenance from future behavior. Existing historical/formed-record studies remain credited; they are not restarted or redescribed as wholly missing.

The literal unrestricted sentence “every sufficient explanation must recover every formation, branching and joining distinction” is therefore too strong as a requirement on all local explanation. The narrower necessary-content principle can be defended, and its branch-recovery consequence is now checked. This does not cancel the broader research goal of a universal generative foundation; it clarifies which stronger inference still needs argument.

## 7. Counterreview

| Challenge | Assessment |
|---|---|
| The conclusion is hidden in “accurate explanation.” | Exactness concerns finite compound answers. The step-by-step relation is derived, with finite branching explicitly needed by this proof; it is not a field of the explanation. Applicability of that answer scope is still a substantive premise. |
| Finite conjunction grants unlimited physical testing. | No. It combines semantic truths at one condition. It does not construct repeated trials, restoration, access, complete negative evidence or a measuring apparatus. |
| All finite tests means a completed finite experiment. | No. Individual tests are finite; the quantified family may be infinite. No finite-data certification of full accuracy is claimed. |
| The witness only changes an unrelated predicate. | It has no atoms. Actual available successors differ; the common-condition question exposes that difference while complete feasible-word answers agree. |
| Matching branches is already graph isomorphism. | Only up to bisimulation initially. Native state separation and reachability support the stronger bijective correspondence. Carrier-identity and history-loss witnesses remain. |
| Conjunction proves simultaneous joint realization. | No. Coavailable alternatives differ from jointly executed events or conserved shared resources. Only sequential representative-wise joining is checked here. |
| Every valid local explanation must answer all these questions. | Not established and generally too broad. The claim applies to accounts advertising the corresponding capacity/continuation coverage. Narrow mathematical explanations keep their valid scope. |
| A static holistic account is disqualified. | No. If it supplies the same answers, it inherits the same relational content. The proof does not privilege temporal notation or settle explanatory priority. |
| All new proofs remain zero axiom. | False. The general converse uses standard classical dependencies, disclosed below. No custom postulate was added; those are different claims. |
| The result establishes universal ethical authority. | No. It concerns factual explanatory content. The established G0/J route and other authorized branches retain their own scopes. |

This is authoring-agent counterreview. No independent agent was requested or used. Other studies’ independent reviews are not transferred to this package.

## 8. Primary-source assessment

Read Xu and Norrish, [Mechanised Modal Model Theory](https://trustworthy.systems/publications/full_text/Norrish_Xu_20.pdf), §§2 and 3.2, including Theorem 1. Their HOL4 treatment records equivalence between modal agreement and bisimilarity for image-finite models. The present event-indexed Lean construction follows this established Hennessy–Milner route and connects it to this repository’s exact presentations, native histories and explanatory-scope question. This is neither a new mathematical discovery nor the first mechanization of the theorem.

The PMC page was blocked by a browser challenge; the author/institution-hosted PDF was readable. The author-hosted PDF of Hennessy and Milner’s 1985 paper timed out; its bibliographic search result is a genealogy pointer, not a full-text reading claim. Accessed 8 October 2026 local time. No source bytes were imported; this is link-only assessment. The new results were checked locally rather than inferred from literature assertions.

## 9. Complete proof map and checks

[ExplanatoryBranching.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/ExplanatoryBranching.lean): **18 new theorems**. Finite test semantics, two-way branching characterization, exact-code consequence, trace lifting and separated structural correspondence.

`same_refl`; `same_symm`; `same_trans`; `bisimulation_preserves_tests`; `bisimulation_implies_same`; `finite_separating_test`; `not_same_has_separating_test`; `same_forces_successor_match`; `same_is_bisimulation`; `same_iff_bisimilar`; `exact_equal_codes_force_branch_matching`; `bisimulation_lifts_trace`; `same_functional`; `same_inverse_functional`; `same_total_on_reachable`; `branching_structural_correspondence`; `correspondence_preserves_steps`; `any_bisimulation_agrees`.

[ExplanatoryBranchingWitnesses.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/ExplanatoryBranchingWitnesses.lean): **18 new theorems**. Common-condition versus early-split witness, exact all-word characterization, old relational-identity connection and actual-history loss.

`can_nil`; `can_cons`; `fork_finitely_branching`; `finish_words`; `both_words`; `left_words`; `right_words`; `root_words`; `same_all_words`; `shared_condition_retains_alternatives`; `early_split_loses_shared_alternatives`; `trace_equivalence_misses_branching`; `no_rooted_bisimulation`; `unmarked_bisimulation`; `static_toggle_same_all_tests`; `two_actual_histories_same_endpoint`; `all_future_tests_agree_after_both_histories`; `actual_length_not_endpoint_readable`.

[ExplanatoryBranchingRecovery.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/ExplanatoryBranchingRecovery.lean): **9 new theorems**. Derived code law, lifting from every representative, all finite histories, test-faithful reconstruction and the separated native graph.

`native_step_projects`; `code_step_lifts_from_every_representative`; `native_trace_projects`; `code_trace_iff_native`; `code_graph_is_bisimulation`; `recovered_model_agrees_with_reading`; `exact_code_law_unique`; `separated_encoding_injective`; `separated_native_step_recovered`.

The [final immutable receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/explanatory-branching-checks/20261007T233522.275247Z/receipt.json) checks ten frozen modules with Lean 4.29.1. There are 45 new and 96 inherited declarations, 141 total. The complete dependency counts are 103 empty, 15 `propext`-only, 10 `propext`/`Quot.sound`, and 13 `propext`/`Quot.sound`/`Classical.choice`. Of those, the new counts are 19, 3, 10 and 13 respectively. All 13 three-dependency declarations trace to the classical modal-equivalence-to-successor argument; explicit mathematical premises remain separate from these logical audits.

Run `python3 experiments/integrated-correction/general-framework/generative-basis/lean/deeper/check_explanatory_branching.py`. It compiles an isolated copied import closure, records original hashes and logs, rejects proof holes/unsafe bypasses/new postulates/warnings, and audits the declared dependency inventory. The scanner allows the word “axiom” inside an inherited explanatory comment while still rejecting axiom/constant declarations and any unapproved dependencies. Earlier partial successes, scanner rejection of that comment and tactic/elaboration failures are preserved development records, not additional accepted results.

The [local integration check](EXPLANATORY-BRANCHING-CHECKS.json) binds every new theorem, frozen/current source and log, verifies local links and paired C30/F22 rendering, and records concurrent shared changes separately. [Owned edits](EXPLANATORY-BRANCHING-INDEX-EDITS.json) preserve prior unfolding, joining, effective-law and universal-counterexample content. No previous proof module was modified, no empirical experiment rerun, and no repository-wide audit claimed.

## 10. Integrated conclusion and next discriminating question

The new warranted connection is:

**claimed coverage of formed possibilities → correctness of common-condition continuation questions → finite-test equivalence → derived branch matching → faithful code histories and, with separation/reachability, structural uniqueness.**

The substantive first arrow is defended for its stated kind of explanandum and not asserted for every local explanation. Native event/condition correspondence, image-finiteness and the adequacy of the model’s retained relations must still be warranted in application. Existing evidence and concrete derivations can supply parts of that warrant; they are not automatically void because a generic theorem lists parameters.

The next universal question is whether a justified, sufficiently broad account of formation has analogous separating questions for non-discrete or infinitely branching possibilities and genuine concurrent joint realization, while retaining static, finite and destructive cases. Historical explanation needs its own independently warranted retained/predecessor content. This is a target-adequacy and generalization task; it is not solved by simply demanding all predicates, raw state identity or universal access to tests.
