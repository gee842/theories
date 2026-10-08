# History-conditioned distinctions and the remaining self-formation bridge

6 October 2026. AI-written mechanism study and formal audit, not Ren's own formulation. The governing requirement remains [generated self and ethics](../../../../theories/becoming/chapters/GENERATED-SELF-AND-ETHICS.md) under the [no-assumptions directive](../../../../sources/15-codex-theory-conversations/2026-10-06-no-assumptions-directive.md).

## Result and exact scope

[GeneratedSelf.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/GeneratedSelf.lean) adds 23 constructively proved theorems over the existing `Process`, `Trace`, history realization and Boolean laws. It adds no primitive transition law, ownership labels, self predicate, reward function, global assumption or theorem axiom dependency. All 23 printed dependency audits are empty.

The named connection is **actual history → operationally consequential distinction → possible retained representation**. The final arrow is a representation criterion, not an endogenous learning theorem. It has not closed **organization → regulation → acquired self/world representation**, still less the realization of experience or ethical justification.

The positive structural result is that an exact representation of future finite feasibility must retain every distinction witnessed by different compatible continuations. The theorem `exact_summary_exists_iff` gives a constructive necessary-and-sufficient criterion for a proposed history record: some exact interpreter exists precisely when equal records never merge histories with differing continuation profiles. `profiles_extend` proves that a common event-history extension preserves profile equivalence, so the relation admits consistent updating without supplied me/world training labels. These are requirements of that exact finite-continuation contract; they are not requirements on every usable self-model.

## Construction from the unchanged process

For an initial state `s`, history `h` and proposed future `w`, define

`Residual P s h w := Feasible P s (h ++ w)`.

This is extracted from the declared transition relation. No primitive event is added. A profile compares these propositions for every finite future; it does not identify propositions by an extensionality axiom or construct a physical observer.

The module establishes the following connections:

- `residual_iff_actual_boundary` expresses the profile as an existential union of continuations from endpoints actually compatible with the history. It preserves the exact boundary-state constraint of the core. It gives no ability to select an endpoint.
- `actual_continuation_enters_residual` carries a particular reached endpoint's feasible continuation into that union. `residual_at_unique_endpoint` gives the converse under an explicitly supplied endpoint-uniqueness condition; nondeterministic histories cannot generally omit it.
- `residual_update` derives the history-extension rule by associativity of concatenation; `profiles_extend` proves its compatibility with the profile distinction.
- `residual_history_realization` connects the profile to the already-defined complete-history process. That mathematical realization stores an entire label history; it does not show that the original process stores one internally.
- `exact_summary_collision_profiles`, `exact_summary_distinguishes` and `exact_summary_exists_iff` characterize lossless representation for this contract. The constructed interpreter existentially pools histories carrying the same proposed record. It need not be decidable, finite, affordable, acquired or implemented.
- `residual_exact_projection` transports the result under the core's explicit transition-preservation and fibre-wise-lifting obligations. It supplies no new claim that arbitrary projections satisfy those obligations.

This is the strongest positive generic statement obtained here. Its interpretation as operational information is warranted by the continuation contract. Interpreting it as controllability, self-ownership, biological individuation or conscious perspective would add content absent from the theorem.

## Closed counterexamples and what they exclude

The already-existing `toggle` process supplies the main exact counterexample. The empty history reaches `false`; one event reaches `true`. Their residual profiles nevertheless agree on every future because every finite word remains feasible. `no_profile_only_toggle_state_decoder` proves that no readout constant on these profiles can recover both actual endpoint states. This is an explicit information-loss result inside the old model, with no newly designed dynamics.

It follows that the profile is not automatically a complete current-state model. It does not follow that a useful self-representation must track toggle phase: stable identity could deliberately ignore that coordinate. The counterexample rules out identifying this formal equivalence with an already demonstrated full self-model. The absence of a sensor, action-origin attribution, organization-maintenance criterion, acquisition mechanism and causal use remains independently visible in the root interface.

`recurrence_without_profile_differentiation` combines actual change, a two-event return and universal profile agreement. Thus activity, change and recurrence do not force this particular operational distinction. The statement is not that a regime-specific generative account of self formation is impossible. A generic process interface must also represent regimes without the capacities at issue; their existence does not by itself disprove the intended foundation.

`no_invariant_unique_toggle_center` rules out selecting one distinguished Boolean state from the unpointed symmetric law while respecting every law symmetry. This concerns an absolute single-center selection from those data. It does not exclude initial-state-relative perspectives, symmetry breaking through interaction/history, plural centers or locally organized selves. A local self can be generated without one uniquely privileged universal center.

## Existing embodied learning supplies a different, complementary result

[ConstructedPrediction.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/learning/construction/prediction/ConstructedPrediction.lean) already contains stronger local causal facts than an analyst's profile:

- `full_formation_prediction_corrected_action` carries the actual typed-material formation history through register installation to paid corrective action.
- `actual_replacement_retains_acquired_memory` retains an acquired score across a paid updater replacement.
- `material_backed_write_changes_future_command` changes the next command by an actual corrective write while retaining the already executed selector and material register.

Those results provide a route for physically retained information to affect subsequent process behavior. They supply the finite memory scheme, decoder and functional coupling as local recipes. Their header explicitly records that boundary. They neither derive those recipes from the root nor acquire an own/world distinction. This study inspects and connects their existing meaning; it does not rerun or upgrade their validation.

[PredictionProtocolObservation.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/learning/PredictionProtocolObservation.lean) further shows that an earlier consumed receipt can be recovered from old/new scores and an executed action within its bounded domain. Its header correctly says that this is an analyst's semantic reconstruction, not an installed endpoint sensor or proof that the old score is physically retained. That distinction must also govern the new history-profile theorem.

## Unresolved premises and the result that would change the account

The formal background, state/action carriers, primitive relation and chosen initial state remain supplied wherever a concrete process is studied. The root does not yet explain why actual dynamics have a particular law. Conditional theorem arguments remain conditional: endpoint uniqueness, totality, exact-summary behavior and faithful projection are not asserted globally. Empty Lean axiom reports do not meet the stronger philosophical demand for an assumption-free generative account.

The remaining formation bridge must account for acquired, revisable information distinguishing the organization's own production/regulation from relevant external processes, demonstrate its causal use and retain mistaken or unstable attribution regimes. Correct self/world labels, a hidden ownership reward, a supplied external spectator or a reconstruction available only to the analyst cannot complete that bridge. An adequate result could use an approximate or task-specific representation rather than exact finite-continuation preservation; its adequacy would need independent justification.

A mechanism showing endogenous acquisition and use from already justified generative dynamics would advance this connection. A demonstration that a proposed record merges distinctions necessary for its actual task, or that its apparent self-label derives from supplied supervision, would revise or reject that mechanism. The current exact-summary test can audit a claimed continuation contract; it is neither a complete specification nor a metaphysical necessity theorem for selfhood.

The ethical connection remains distinct. Nothing in these 23 theorems derives actual experience, adversity, relief, desire-independent reasons or an ethical direction. The project must still explain evaluative formation and justify evaluation without making a generated self's approval create all value.

## Verification

All six dependency/module sources were copied into a fresh `/tmp/generated-self-lean-qz09egkn` directory and compiled with installed Lean 4.29.1. Compilation succeeded. The ordered list of 23 theorem declarations matched the ordered `#print axioms` results, every new dependency list was empty, and source checks found no bypass or new primitive declaration. The module's SHA-256 at this audit is `96b5b5a71e465abbf6139bb230cecfa8b28bb48b58d519fd2a5c7cccdf165c6d`.

An independent semantic review requested and received two scope clarifications: the exact-summary contract is not a universal selfhood requirement, and endpoint-phase recovery is not required of every bodily/self representation. The shared integrated checker should preserve the final verification log with the rest of the model's records.
