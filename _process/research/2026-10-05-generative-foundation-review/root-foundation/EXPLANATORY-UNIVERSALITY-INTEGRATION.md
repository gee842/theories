# Universal uniqueness: recoverability, minimal rivals and the exact stopping point

8 October 2026, Asia/Bangkok. AI-authored under [Ren’s request to try universal uniqueness until a wall is reached](../../../../sources/15-codex-theory-conversations/2026-10-08-generative-explanatory-necessity.md#推进到实际障碍--push-until-a-wall). This continues [joining and reconstructed interfaces](EXPLANATORY-JOINING-INTEGRATION.md); it does not reopen completed normative grounding or claim an independent agent review.

**Result:** a relation descends to exact reduced answer codes if and only if it is invariant under every answer-preserving replacement of its arguments. This works without assuming sequence concatenation, associativity, identities or total composition. However, complete successful-word behavior plus minimum state and transition counts does **not** determine a unique generating mechanism. Two explicit two-state, two-edge systems are trim, have no continuation-equivalent states and realize the same entire language, yet are not isomorphic. Deterministic, reachable and continuation-separated systems do recover uniqueness, without a finite-state assumption. Their root- and step-preserving maps are unique without separately stipulating word alignment.

**61 new checked theorems (13 + 31 + 17); 135 declaration audits including 74 inherited.** All 61 new dependency lists are empty. The complete run has 123 empty lists and 12 inherited `propext`-only lists. This is not “zero premises”: the targets, correspondence, separation, reachability and deterministic representation remain explicit. The original universal claim is **not proved or globally disproved**. A concrete inference to it is refuted, and the remaining target-selection/structural-adequacy requirement is identified.

## 1. Which universal claim was tested

Three strengths must be kept separate:

| Candidate | Status after this round |
|---|---|
| A fixed independently specified answer family determines its exact reduced answer content. | Retained from prior work; now an exact criterion says which further ternary relations it can recover. |
| Complete successful continuation answers and a genuinely smallest generating mechanism determine that mechanism up to isomorphism. | False for the stated class of relational finite-word realizations; checked minimum-state and minimum-edge rivals. |
| Every adequate explanation of reality must recover one uniquely fundamental generative structure. | Still unresolved. Neither choosing a fixed answer family nor requiring every predicate establishes its independent applicability to all explanation. |

The second is a substantive attempt to strengthen the first, not a definition of the third. Refuting it blocks that route; it does not refute the whole generative account. A full explanation of branching would have a richer explanandum than the matched success language. Its structural uniqueness requires its own argument.

The independently fixed concrete target is `L(w) := w ≠ []` for arbitrary finite repetitions of one event. The question is whether some admitted execution ends in a designated marked condition. The mark is supplied local relational content, not a favorable ethical verdict or an external observer. These are two exact realizations of this mathematical target, not an empirical assertion that both laws govern one identified physical situation.

The concurrent [effective-law study](LAW-CORRESPONDENCE-INTEGRATION.md), read during integration together with its Lean source, already proves a concrete summary’s representative independence and exact histories from the unchanged native mechanism (14 theorems / 18 new audits), and credits existing controller/oxygen evidence. Such local sufficiency and correspondence can be earned; they are not all permanently ungrounded inputs. Its independent review does not review our new results. Shared-chapter §§39–41 and both studies’ index contributions are preserved; this direct uniqueness attempt follows in §§42–47.

## 2. Remove the supplied composition laws

For any case type `M`, question type `Q` and target `T : M → Q → Prop`, write `m ~ n` when every target answer agrees. A presentation has an encoding and a fixed reading; `Exact` gives correct answers and `Reduced` identifies answer-equivalent cases. This semantic reduction differs from minimizing the number of states of a generating mechanism.

Take any ternary relation `J(a,b,c)`. It need not be functional, associative, total or equipped with units. Define its saturation condition:

> If `a ~ a′`, `b ~ b′` and `c ~ c′`, then `J(a,b,c) ↔ J(a′,b′,c′)`.

`relation_descends_iff_saturated` proves that, for an exact reduced presentation `p`, there exists a coded relation reading `K(p(a),p(b),p(c)) ↔ J(a,b,c)` **if and only if** saturation holds. The constructive lift uses witnesses of encoded source triples. Any two exact relational readings agree on used triples; unused codes are outside that uniqueness statement.

The directions have different premises. Exact answer readings plus saturation suffice to make the witness lift exact, even without reduction. Reduction plus any exact relational reading force saturation, even without separately invoking exactness of the question reading. Combining them yields the criterion. `separating_relation_blocks_descent` gives a direct failure certificate whenever actual answer-equivalent cases disagree on the relation.

This is a stronger general form than the earlier specialized word and unit results. It does not assert that every explanatory question family is saturating for every generative relation. That unproved implication is now visible as an exact mathematical obligation, rather than concealed in the phrase “adequate explanation.”

## 3. Two genuinely minimal mechanisms with the same complete target

Both mechanisms have states `0` and `1`, initial state `0`, marked state `1`, and a single event `a`. Only the listed edges exist:

| Mechanism | Event edges | Marked condition |
|---|---|---|
| Early marking | `0 → 1`, `1 → 1` | `1` |
| Late marking | `0 → 0`, `0 → 1` | `1` |

In early marking, the first event reaches the marked condition and later events remain there. In late marking, an admitted successful execution waits at `0` until its final event, then moves to `1`, which has no further event. Both reject the empty word and accept **every** nonempty word. Inductive Lean proofs cover all finite lengths, not an enumeration up to a bound. Both also admit at least one execution of every word when no final mark is requested.

The distinctions are not surplus unreachable or duplicate states:

- Each state is reachable and can participate in an accepted continuation. A marked state with no outgoing edge still accepts the empty continuation; it is not an empty/right-language-useless state.
- The two states inside each mechanism have different right languages, already distinguished by the empty continuation.
- Any realization of the same language, even with a different or infinite carrier and multiple initial states, has two distinct states. An accepting nonempty run begins at an unmarked initial state and ends at a marked state; equating them would accept the empty word. `two_state_lower_bound` constructs an injection from `Bool` into any such carrier.
- Any realization also has at least two distinct event edges: an accepting two-event trace whose consecutive edges coincide would make its start equal its marked end, again admitting the empty word. The displayed tables have exactly two edges each. The class is the supplied single-event `Process` interface, without silent transitions.

Nevertheless, there is not even an injective step-preserving map from late marking into early marking. Late marking has two different successors at `0`; early marking has a unique successor everywhere. An injective map preserving those steps would equate `0` and `1`. Thus they cannot be isomorphic as mechanisms, including under relabelling.

This is a checked obstruction to both “fewest states resolves it” and “also minimize the edge table.” It does not assert equal description length under every conceivable programming language or that every imaginable explanatory virtue ties. No such coding-invariant complexity claim was formalized.

The lost content is independently identifiable. After one event all early-marking executions are marked; a late-marking execution can remain unmarked. After arriving at the marked state, early marking can continue, while late marking cannot. `AllFinish` and `Enabled` check these differences directly. They are not a freely toggled predicate on an unchanged dynamics. They also mean the rivals cease to match when these stronger questions are part of the explanation target.

## 4. Try to repair uniqueness

The next attempt supplies an actual deterministic total successor function, a root and a marked-condition predicate, all as roles in one process representation. A run has one reached state per word. Require:

1. every supplied state is reachable from the root;
2. no two states agree on every finite marked continuation;
3. the two candidate systems accept the same word language.

`reachable_separated_unique` then constructs a total, single-valued correspondence in both directions. `matched_marks` preserves the mark and `matching_preserves_and_reflects_steps` recovers the entire step relation. There is **no finite-carrier or finite-alphabet assumption**.

Word alignment is not left as an unexplained extra field for candidate maps. `map_follows_run` derives it from preserving steps; with a preserved initial role, `rooted_map_automatically_aligned` follows. Reachability then gives `rooted_map_unique`: any two root- and step-preserving functions agree pointwise. The existence theorem uses a relational bijection, so no choice of inverse or classical-choice axiom is hidden in the implementation.

This is a real repair, but not a universal derivation of its premises. `determinism_not_language_invariant` proves that determinism cannot be extracted by any rule invariant under the original complete success answers: the two minimal rivals already disagree. Declaring the deterministic model canonically predictive is legitimate; declaring it the unique actual generating mechanism would add a substantive identification claim.

## 5. Try collective prediction, then every possible predicate

Nondeterministic realizations can retain full prediction through collections of reachable states. `collective_iff_appended` proves for any supplied machine that some reached state can realize a continuation exactly when the appended word is accepted. The two rival machines therefore have identical collective predictions after **every** past word and for **every** future word.

Yet `no_late_state_matches_early_success` proves that no individual late-marking state has the same continuation language as the early-marking successful state. The collective can represent a prediction that no single native state in the other mechanism represents. A canonical prediction does not force a one-to-one identification of native states. This gives a concrete reason why passing to deterministic prediction can preserve the target while changing the mechanism interpretation; the new proof does not construct a general powerset automaton or count it as a native-state isomorphism.

The last attempt is to eliminate question restriction altogether by taking every predicate on the supplied case type as a question. `all_predicates_separate` then gives `SameAnswers a b ↔ a = b`; any exact encoding is injective. Every ternary relation is saturated, recoverable, and exact presentations have the prior unique correspondence on used codes.

The price is explicit: these tests already retain every distinction of the **given** case domain, including singleton predicates. The theorem neither identifies which cases describe reality nor derives access to all those questions. It recovers any supplied relation, not a special priority for a relation because it is called generative. The inference that this does not yet establish universal explanatory priority is the philosophical scope assessment, not a separate Lean no-go theorem about every possible metaphysics.

## 6. The actual wall

The barrier is not an unfinished Lean tactic. The following route is now exhausted within its stated scope:

- Removing composition laws yields an exact recoverability condition, but does not make that condition automatic.
- Adding true cardinal and edge minimality does not select a unique mechanism.
- Requiring deterministic realization recovers uniqueness, but the original answers cannot themselves warrant that requirement.
- Keeping nondeterminism and moving to collective predictions preserves the target, but does not identify the native mechanism.
- Asking all predicates recovers all given structure, while presupposing the complete distinction domain it was supposed to ground.

To cross this wall, one must give an independent reason why the intended universal explanandum demands a particular separating collection of formation, branching, intervention and joining facts, and why its exact accounts satisfy the required recoverability conditions. That cannot be replaced by defining “sufficient” as already carrying our chosen relation. Nor may a matched holistic or static constraint account be rejected merely because its notation does not narrate a temporal generator.

**Stop this attempted universal inference here.** The broad conjecture remains open, the false minimal-mechanism strengthening is retained as false, and the positive conditional theorems remain results. Further work becomes justified by a new substantive target-adequacy argument or independently supported correspondence, not by iterating more equivalently conditional encodings. Shared-capacity and actual probe-access work remains a separately scoped identification programme from the preceding study; no automation is created.

## 7. Counterreview and nondual audit

| Objection | Resolution and remaining scope |
|---|---|
| The rival only pads a mechanism with redundant states. | False: trimness, state separation, the two-state lower bound and the two-edge lower bound are all checked. |
| Minimum states is the same as `Reduced` from the previous uniqueness theorem. | False. One minimizes realizations of a language; the other collapses exactly equal answers on one fixed case domain. The counterexample does not contradict prior uniqueness. |
| The two mechanisms preserve all reality-level facts. | False. They preserve the declared existential word target and differ on actual branch and continuation facts. This is a boundary for that route, not a whole-theory refutation. |
| The deterministic repair now selects reality. | No. It identifies the rooted deterministic continuation-separated realization within its class. Determinism is not forced by the matched answers. |
| Recoverability is already built into “generative.” | No. `Saturated` is separate and proved equivalent to descent. The source relation and adequate query scope remain supplied. |
| All predicates prove a universal empirical truth generator. | No. The type and questions are inputs; correctness, access, empirical adequacy and discovery are not produced. |
| The state, label, root or mark introduces independent ontological domains. | They are analytical roles in the same admitted unfolding. Labels omit branching detail; roots scope a history question; marks specify a local endpoint question. The omissions are stated and tested. No separate subject/world or fact/value ontology is inferred. |
| A state with no next step is always a failed or worthless state. | No. In this target it can be a marked accepted endpoint. No normative value or imperative is derived. |
| The study settles generative alignment or contradicts G0. | Neither. It tests factual structural identification. The authorized normative-axiom route and its completed results retain their distinct scope. |

This is an authoring-agent counterreview. The separate unfolding-preservation study and its independent review remain credited at their original scope; neither reviewed these new 61 theorems. No independent subagent was requested or invoked.

## 8. Primary-source assessment and genealogy

Read Janusz Brzozowski and Hellis Tamm, [Minimal Nondeterministic Finite Automata and Atoms of Regular Languages](https://arxiv.org/pdf/1301.5585), introduction and §2, with the initial §3 examples. The paper distinguishes trimness, state-language reduction and state-count minimality, records nonuniqueness of minimal nondeterministic realizations, and describes the unique quotient deterministic automaton. It provides the appropriate precedent for the distinction tested here.

The specific two-state pair and all stated lower-bound/reconstruction claims are checked in the repository; no mathematical novelty or exhaustive literature claim is made. Accessed 8 October 2026 local time. This is a link-only source assessment; no PDF bytes were imported. The previous syntactic-congruence and object-free-category sources retain their original reading and proof scopes.

## 9. Lean correspondence and verification

[ExplanatoryUniversality.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/ExplanatoryUniversality.lean): **13 new theorems**. Arbitrary ternary-relation descent, uniqueness on used codes, separating obstruction and the all-predicate limit.

`lift_contains`; `saturation_gives_exact_lift`; `exact_relation_forces_saturation`; `relation_descends_iff_saturated`; `lift_exact_iff_saturated`; `relational_reading_unique_on_used`; `separating_relation_blocks_descent`; `all_predicates_separate`; `all_predicates_force_injective`; `all_predicates_every_relation`; `all_predicates_relation_recoverable`; `all_predicates_automatically_reduced`; `all_predicates_unique_correspondence`.

[ExplanatoryMinimalModels.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/ExplanatoryMinimalModels.lean): **31 new theorems**. Matched complete languages, trimness/separation, state and edge lower bounds, nonisomorphism, richer target differences and collective prediction.

`right_nil`; `accepts_nil`; `early_nonempty_run`; `late_wait`; `late_nonempty_run`; `early_accepts`; `late_accepts`; `same_complete_language`; `any_realizer_needs_two_states`; `two_state_lower_bound`; `early_trim`; `late_trim`; `final_distinguishes_bool_states`; `early_separated`; `late_separated`; `early_deterministic`; `late_branches`; `late_not_deterministic`; `no_injective_step_preserving_map`; `same_possible_words`; `early_all_finish_after_one`; `late_not_all_finish_after_one`; `successful_continuation_differs`; `minimal_mechanism_uniqueness_fails`; `any_realizer_needs_two_edges`; `early_edges_exact`; `late_edges_exact`; `collective_iff_appended`; `same_collective_predictions`; `no_late_state_matches_early_success`; `determinism_not_language_invariant`.

[ExplanatoryDeterminism.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/ExplanatoryDeterminism.lean): **17 new theorems**. Unbounded deterministic runs, native trace correspondence, reduced exact presentations, structural bijection and uniquely derived root/word alignment.

`run_append`; `trace_iff_run`; `presentation_exact`; `presentation_exact_common`; `presentation_reduced`; `every_state_used`; `matched_initials`; `matched_next`; `matched_marks`; `matched_functional`; `matched_inverse_functional`; `reachable_separated_unique`; `matching_preserves_and_reflects_steps`; `unique_word_aligned_matching`; `map_follows_run`; `rooted_map_automatically_aligned`; `rooted_map_unique`.

The [final receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/explanatory-universality-checks/20261007T231550.347371Z/receipt.json) freshly compiles eight frozen modules with Lean 4.29.1: 61 new and 74 inherited declaration audits, 135 total; 123 empty and 12 inherited `propext`-only lists. All 61 new theorems have empty dependency lists; none uses custom axioms, `Classical.choice`, `Quot.sound` or proof holes. This does not remove explicit hypotheses or the foundations of Lean’s kernel.

Run `python3 experiments/integrated-correction/general-framework/generative-basis/lean/deeper/check_explanatory_universality.py`. The runner rejects holes, custom axioms, warnings, missing audits and unlisted dependencies, and preserves copied sources/logs. Only the final named receipt certifies the finished package. Earlier successful partial snapshots and failed decidability-elaboration attempts are development history, not additional results or accepted proofs. Those failures were repaired by exposing the concrete step definitions before finite Boolean `decide`; the general language/minimality/uniqueness results are inductive or symbolic proofs.

The [document and frozen-binding check](EXPLANATORY-UNIVERSALITY-CHECKS.json) verifies every new theorem’s audit, current/frozen source identity, receipt/log hashes, local links and owned table entries. The [index edit record](EXPLANATORY-UNIVERSALITY-INDEX-EDITS.json) preserves concurrent shared content and the separate unfolding-preservation contribution. Existing proof files and earlier receipts were not rewritten. No repository-wide theorem audit or global index-freshness certification is claimed.

## 10. What would change the conclusion

An independently warranted richer explanandum could exclude the two rivals as equivalent explanations and justify recovery of further relation content. A proof that all relevant explanations necessarily preserve such content would advance universality. Showing exact recovery only after assuming that preservation would remain conditional, even if useful. A matched full-content rival preserving those independently justified requirements would instead challenge the proposed universal structure more directly.

Current conclusion: **common recoverable content is stronger than before; unique smallest generating mechanism is not generally available; universal ontological priority is still unestablished.** The named wall concerns the inference from exact answers to uniquely necessary native structure, not a denial that generative relations can explain many domains.


## 11. Subsequent attempt at the adequacy bridge

Ren explicitly asked to try the remaining “why must adequate explanation preserve these distinctions?” inference. The [45-theorem continuation](EXPLANATORY-BRANCHING-INTEGRATION.md) gives a scoped affirmative argument for explanations of formed capacities, derives bisimulation from finite compound answers under finite branching, removes determinism from the structural-correspondence route and constructs faithful code histories. It also checks that actual provenance does not follow from forward adequacy. The previous minimal-mechanism counterexample and all 61 earlier proofs remain valid; the new question scope excludes that target mismatch rather than erasing it. General classical dependencies are disclosed separately from the earlier empty audits.
