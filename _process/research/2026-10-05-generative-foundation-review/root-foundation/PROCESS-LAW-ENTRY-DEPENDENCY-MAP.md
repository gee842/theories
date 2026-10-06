# Dependency map for the derived process-law entry

6 October 2026 (UTC). AI-authored consolidation requested by Ren, who noted that the "consolidated derivation with a precise dependency map" proposed as the next deliverable did not yet exist. This document adds no proof, experiment or new claim. It classifies what the current Lean entry [GenerativeDerivedProcessLawModel.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/GenerativeDerivedProcessLawModel.lean) relies on, using the [assumption-elimination audit](ASSUMPTION-ELIMINATION-AUDIT.md), the [mechanism-status reconciliation](MECHANISM-STATUS-RECONCILIATION.md), the [process-law derivation](PROCESS-LAW-DERIVATION.md), [conditional universality](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/CONDITIONAL-UNIVERSALITY.md) and the [cloud handoff](../../../CLOUD-HANDOFF-2026-10-07.md). Each row was checked against the Lean source, not only the prose. Those documents are unchanged.

It follows the [nondual method](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/NONDUAL-METHOD.md). A law supplied to this model is a **local input to this representation**, not thereby something outside generative reality or unexplained anywhere in the theory. Where another branch already explains the same capacity, the map says so and states whether the interface to this entry has been proved.

## 1. Claim fixed before the audit

The map concerns one claim: **the effective one-packet inquiry law, and the inquiry results built on it, follow from the native contact, source-conversion and receipt-acquisition activity of the reconstructed diagnosis port.** It does not concern the stronger claims that reliable understanding necessarily forms wherever systems form, that the native mechanism is a physical system, or that any appraisal is ethically warranted. Those stronger claims appear in §5 only to record that this entry does not settle them.

## 2. Scope of the checked closure

The [process-law receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/process-law-runs/1791291483950888000/receipt.json) records 32 modules and 599 audits, all with empty axiom reports. After the vocabulary rename the closure was rebuilt on the cloud host with the same Lean release; the [current receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/process-law-verification.json) again records 32 modules and 599 empty audits.

**The conditional-universality package is not in this closure.** `conditional/ResourceContinuation.lean`, `SupportNecessity.lean` and `RenewalExamples.lean` import `GenerativeCore` but are built separately ([conditional README](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/README.md)). Of their 60 audits, 26 use Lean's standard `propext` and `Quot.sound`. When this map was first written, no theorem applied U1–U3 to the native packet process. **Update, same day:** [NativePortContinuation](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/native-port/README.md) now proves that connection in a separate build (§4, item 1). The 32-module closure and its all-empty audit policy are unchanged.

## 3. The map

Status key:

- **Derived:** proved in this closure from the stated inputs. The theorem is cited.
- **Universal over a class:** proved for every process or state satisfying stated conditions. Whether a system belongs to that class is a separate question.
- **Needs evidence:** the formal result holds, but applying it to an actual system requires correspondence or identification evidence.
- **Supplied here:** used by this entry without derivation in this closure. The last column says whether another branch explains it and whether that interface to this entry is proved.

### 3.1 Root interface

| Ingredient | Status | Lean evidence | Note |
|---|---|---|---|
| Relational process (`Process.step : State → Action → State → Prop`) and finite traces | Universal over a class | `GenerativeCore`: `trace_append_iff`, `feasible_append_iff`, `projection_exact_iff`, `local_exact_iff_trace_exact`, `trace_faithful_iff` | Applies to every relational process. It derives closure properties from a supplied dynamics. It does not derive the dynamics. |
| Which dynamics a carrier has | Supplied here (preserved counterexample) | `DynamicUnderdetermination.same_carrier_incompatible_laws`, `event_without_state_distinction`; `DynamicSymmetry.symmetric_dynamics_remain_underdetermined`; `DynamicClassification.symmetry_candidate_iff_descriptions` | Distinctions plus totality, determinism and renaming invariance do not select static versus toggle dynamics on Bool. This is a finite counterexample to one entailment. It does not show that no richer account could select a dynamics. |
| Admitted finite-history language → exact realization | Universal over a class | `HistoryRealization.process_language_exact_history_realization` | The prefix-closed language is an input. |
| Strict reserve decrease bounds continuation | Universal over a class | `Depletion.no_infinite_execution_under_depletion`, `trace_length_bound` | The condition is strict decrease on every step. Replenishment invalidates it. |
| Consequence-triggered rule revision and external provision in the root witness | Supplied here | `RootRealization.consequential_internal_revision`, `restoration_requires_external_provision`, `same_law_admits_renewal_and_loss` | This is a satisfiability witness. The `revise` event and the `supplied` flag are stipulated. |
| Organization, selectors and history residuals that do not by themselves yield learning or a self | Derived (non-implications) | `BoundaryModels.recurrent_process_with_fixed_selector`, `individual_feasibility_without_joint_feasibility`; `GeneratedSelf.exact_summary_exists_iff`, `no_profile_only_toggle_state_decoder` | These are limits, kept as counterexamples. |
| Evaluative direction | Supplied here (non-entailment proved) | `EthicalOrientation.opposed_coherent_annotation_invariant_orders`, `coherence_and_annotation_invariance_do_not_select_growth` | Coherent, renaming-invariant orders rank the same histories oppositely. Settling the direction needs philosophical argument (§5). |

### 3.2 Native port: the ingredients named in the request

| Ingredient | Status | Lean evidence | Note |
|---|---|---|---|
| **Three-phase cycle** (`nextPhase`, `output` = 0,0,1) | Supplied here; partly derived elsewhere (§7) | Defined in `NativePacketProcess`. The port executes the learned machine saved by the [acquisition study](../../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/acquisition/README.md). | The world's cycle is the acquisition study's supplied target law. The learner's three-state model of it is acquired there, by a Python learner with hand proofs. The correspondence checker reuses that saved machine and does not relearn it. Acquisition of the model is therefore derived elsewhere at executable scope, but it is not part of this Lean closure. **Update:** [PhaseCycleDerivation](PHASE-CYCLE-DERIVATION.md) derives cyclicity from one distinction-retaining advance on a finite carrier, and proves 3 the least period meeting the protocol's requirements; period 5 also meets them, so 3 is not forced. |
| **Contact gate** `arrival = (x xor τ) ∧ ¬blocked` | Supplied here | Defined in `NativePacketProcess.arrivalAt`. From it, `PacketLawDerivation.raw_profiles` and `profile_equal_iff_target_equal` **derive** the A/B/C classes. | The gate is inherited from the Python port. Contact formation already exists in [InquiryRevision.lean](../../../../experiments/shared-renewal-capability/regulation/retention/formation/selectors/updaters/prediction/recipient-correction/identification/recording/reason-consumer/action/revision/evaluation/plasticity/formal/inquiry-revision/InquiryRevision.lean) (`staged_actual_connection`, `actual_change_in_access`), under different laws, and is not composed with this port. **Update:** the [contact-formation track](CONTACT-FORMATION-LAW.md) has landed. The contact coordinate now changes only through a formation event (`change_requires_formation`), formation draws on the port's own recorded failures, and the decision to form follows from an inquiry the port runs on itself (`decision_identifies_contact`). The gate's formula itself is still supplied (§7). |
| **Rates** (16,384 + peak drawn per support step, 655,360 arriving per conversion, 10 source units per probe, 2 temporary cells) | Supplied here | Numerals in `draw`, `arrivalAmount`, `convert`, `peak`. The theorems are not parametric in them. | The *form* of the completion guard is derived: `probeReady_exact`, `probe_complete_iff`, `alignment_guard_iff_native_guards`. The numbers are the Python port's default scale-one setting. **Port ∈ U1 is now proved structurally:** `NativePortContinuation.execute_conserves` and `port_sustain_law` hold without using the rate numerals. |
| **Fixed fault settings** (τ, σ, broken reset, blocked, receipt inversion, plus live, workspace and capacity) | Derived as constant; universal over values | `execute_retains_parameters`, `completed_retains_parameters` | Every theorem quantifies over all settings, so results hold for all 32 fault combinations. That execution never changes the settings is proved. How faults form, drift or get repaired is not represented. |
| Ordered completion law: interface support, then source check, conversion, arrival, then receipt support | Derived | `probe_complete_iff`, `probeReady_exact`, `probe_final_effects`, `probe_source_stops`, `probe_receipt_insufficient_stops`, `receipt_capacity_unreachable` | This is the core result of the process-law round. Failures after conversion are retained, not rolled back. |
| A/B/C transfer-response classes and the probe table | Derived | `profile_equal_iff_target_equal`, `native_gate_is_macro_receipt`, `blocked_representatives_retained` | The macro table is no longer an independent premise. |
| Macro probe step and its observation | Derived, conditional on three hypotheses | `completed_probe_projects`, `native_guard_realizes_macro_probe`, `aligned_probe_realizes_macro` | The hypotheses are the next three rows. |
| Calibration (`receiptFlip = false`) | Supplied here (theorem hypothesis) | `native_receipt_calibrated_iff`, `inverted_receipt_differs` | **Update:** for this port, `AcquiredContact.inquiry_calibrates_receipt` acquires the receipt inversion from the port's own record; the hypothesis in `aligned_probe_realizes_macro` is not yet discharged by composing the two. Acquired calibration also exists in [RecipeNative.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/acquisition/feedback/recipe-grounding/formal/RecipeNative.lean) (`actual_binder_matches_selected_decoder`), but not for this port's receipt channel. Experimental access distinguishes some faults at executable scope. A compensated sensor/readiness change stays indistinguishable through the sensor alone. |
| One-packet domain (`source = 10`) | Supplied here (scope restriction) | `projection_at_one_packet`; boundary: `two_packet_completion_retains_source`, `two_packet_state_outside_projection` | The projection is proved not to extend to larger stocks. |
| Known common phase for the alignment schedule | Supplied here | `common_phase_same_schedule`, `alignment_reaches_requested_output` | The schedule is computed from a phase the learner is assumed to know. Phase acquisition is not derived in this closure. |
| Permissive macro controls (`control o`) and denial after exhaustion | Supplied here, and shown to be more permissive than native execution | `OnePacketQuestions.all_actions_enabled`; `PacketLawDerivation.macro_denial_is_not_native_completion`, `exhausted_native_probe_cannot_complete` | This permissiveness strengthens the old negative results. It is not a native implementation of every control. |
| Python port ↔ Lean reconstruction | Needs evidence (finite check done) | `NativePacketCases`: 93 closed certificates for 5,928 original-command cases | This is finite source correspondence over phases, faults, source 0–20 and funding boundaries. It is not a universal refinement proof, and not physical identification. |

### 3.3 Inquiry layer

| Ingredient | Status | Lean evidence | Note |
|---|---|---|---|
| Sufficient inquiry ↔ bounded sound policy | Universal over a class | `InquirySufficiency.sufficiency_iff_bounded_policy`, `sound_execution_meets_goal`, `empty_belief_not_sufficient` | Holds for any process with declared `safe` and `goal` contracts. |
| `safe` and `goal` contracts | Supplied here, with one case derived | `OnePacketAdmissibility.probe_safe_iff_not_denied`, `attainable_iff_packet_safe` | For the packet case, `safe` is discharged by the native packet coordinate. Their meaning and authority in general stay declared. |
| Branch classification | Derived for finite carriers | `FiniteInquiryClassification.classifiedThrough`, `boolean_model_iff_bounded_policy` | Applies only with a faithful `Fin` representation. |
| Inquiry certificates (policy or refusal) | Derived | `DerivedInquiryCertificates.policyOption_certified`, `accepted_is_attainable`; `OnePacketInquirySynthesis.extracted_policy_native_certificate` | Computed rather than supplied. The transition and question relations remain model data. This does not install a physical planner. |
| Attainable questions and their composition | Derived | `AttainableQuestions.attainable_join_iff_shared_policy`, `attainable_by_continuing_inquiry`; `ReachedInquiryComposition.attainable_from_reached_continuations`, `global_preservation_fails` | Includes the exact one-packet obstruction `OnePacketQuestions.joint_answer_unattainable`. |

### 3.4 Conditional universal laws (separate build)

| Ingredient | Status | Lean evidence | Note |
|---|---|---|---|
| U1 local sustaining law | Universal over a class; membership is the condition | `ResourceContinuation.SustainLaw`, `sustain_law_pullback` | The law is permissive by design (all-zero quantities satisfy it). Its content comes from independent interpretation of held, enacted and arrived. |
| U2 prefix bound and its consequences | Derived from U1 | `support_trace_bound`, `unbounded_enactment_requires_unbounded_arrival`, `infinite_unit_execution_arrival_window`, `execution_interval_frequency_bound`, `repeat_supported_cycle` | Uses `propext`/`Quot.sound` where reported. |
| U3 support deadline: bounded lifetime, parent requirement, strict type rank | The conditions are a class definition (`EpisodeSystem` fields); the deadline is derived | `expiry_le_rank_deadline`, `no_alive_after_bounded_rank_deadline`; boundaries `renewing_has_no_strict_type_rank`, `infiniteChain_alive_at_every_time`, `external_arrivals_without_internal_parents` | Exceeding the deadline refutes the conjunction of conditions. It does not by itself identify a cycle. |
| Application to an actual system | Needs evidence | — | Requires showing that the quantities mean what the law says, without the conditions already containing the capacity being explained. |
| Application to the native port | Derived (separate build) | `NativePortContinuation.port_sustain_law`, `step_sustained_exact`, `port_history_bound`, `continuing_port_needs_arrivals`, `port_cannot_continue_indefinitely` | U1 holds with equality. Read as held (存), enacted (化) and arrived (来), not fuel/spent/income; the Lean port now uses these names directly. With only its own source, the port's continuation is bounded. A comparable interface was earlier proved for the formed-variant process in [FormationAccounts.lean](../../../../experiments/shared-renewal-capability/regulation/retention/formation/formal/FormationAccounts.lean) (`identified_account_laws`). |

## 4. Dependencies that remain, ranked by what would remove them

These are claim-specific missing interfaces in the sense of the reconciliation. They are not findings that the wider theory lacks the capacity.

1. **Port ∈ U1 class: closed.** [NativePortContinuation.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/native-port/NativePortContinuation.lean) proves that every native call, completed or interrupted, conserves `held + enacted` relative to `arrived`. The port therefore satisfies U1 with equality and inherits U2. It also proves that, with only its own source, a potential strictly decreases on every completed call, so the port has no infinite execution. The original wording of this item expected the result. [Ren rejected the fuel/spent/income vocabulary](../../../../sources/15-codex-theory-conversations/2026-10-07-market-names-and-continuation.md) as a market frame, and the new module reads the same coordinates as what is held, enacted and arrived.
2. **Contact formation → this gate: landed.** [The contact-formation track](CONTACT-FORMATION-LAW.md) composes with `arrivalAt` directly: formation clears `blocked` and the derived class changes from C to the class fixed by `tau`. What it still supplies is listed in §7.
3. **Calibration and phase acquisition → theorem hypotheses.** `receiptFlip = false` and the known common phase are hypotheses of `aligned_probe_realizes_macro`. Acquired calibration (RecipeNative) and acquired state models (acquisition study) exist at other scopes. Composing either with this port would remove a hypothesis. A compensated fault stays a real limit and must remain one.
4. **Three-phase cycle and fault settings.** The cycle is a supplied target law; the learner's model of it is acquired. Fault formation is not represented. For claims about this apparatus, these are legitimate local laws. Removing them requires an account of how such an apparatus forms and degrades, which is a different and larger claim.
5. **Permissive controls.** The native port already shows that the old `control o` grants are too generous. Replacing them with costed native control commands would tighten the positive results. It would not change the negative results.

## 5. What this entry does not settle

- **Selection of dynamics from distinctions alone.** This is unsupported, and the counterexamples in §3.1 are preserved. The active universal target is conditional (∀P, A(P) ⇒ G(P)), which does not require it.
- **The no-assumptions rule.** This is unmet and has not been waived. Ren made it a standing rule for all work on 6 October 2026 (§7). Empty axiom reports certify proof terms, not interpretations. Lean's own logic stays a visible framework presupposition. It is not declared discharged, nor shown to be impossible to discharge.
- **Physical identification.** This needs empirical evidence. No row in §3 supplies it.
- **Ethical warrant.** This needs philosophical justification. `EthicalOrientation` proves only that coherence and invariance do not choose the direction. The handoff's current frontier is ethical warrant itself, not another mechanism.

## 6. How to use and maintain this map

A round on this entry is finished when each dependency of its chosen claim has one of the four statuses and its counterexamples are kept. Under Ren's rule, it is not finished while §7 lists a dependency of that claim as still assumed. When a round lands, update the affected row, cite the new theorem, and leave the old status visible in history. A row should not move to "derived" because an interface became more convenient. It moves only when a proof in a stated closure supplies it.

## 7. No-assumptions ledger

On 6 October 2026 Ren made this a rule for all work: **no assumptions, no axioms.** He wrote it after a study listed what it still assumed: "This is a problem, we should have no assumption, no axioms", and "this should be a rule that every agent knows" ([source note](../../../../sources/15-codex-theory-conversations/2026-10-06-no-assumptions-no-axioms-rule.md)).

So every input a result relies on must reach one of two ends:

- **Derived:** proved in Lean from the process itself, with the theorem named.
- **Proved necessary:** a Lean counterexample shows the stated claim fails without it. The input is then part of the claim's scope, not a hidden premise.

Anything else is **still assumed**, and the claim that relies on it is not finished. The ledger below covers the process-law entry and the studies that now extend it. Update a row when a result lands; keep the old status in git history.

| Input | Where it is used | Status | What would close it |
|---|---|---|---|
| Which dynamics a carrier has | The relational core | Still assumed. Distinctions, totality, determinism and renaming invariance are proved **not** to select it (`same_carrier_incompatible_laws`) | A further root principle that selects dynamics, or a proof that every conditional claim is uniform over dynamics |
| Evaluative direction | Ethical claims | Still assumed. Coherence and invariance are proved not to select it (`coherence_and_annotation_invariance_do_not_select_growth`) | Outside Lean: philosophical warrant |
| `revise` event and `supplied` flag | Root satisfiability witness | Still assumed (stipulated witness) | Replace the witness by a derived instance, e.g. the port with formation |
| Cyclicity of the phase | Three-phase cycle | **Derived** from one distinction-retaining advance on a finite carrier (`retaining_change_closes_into_cycles`, carriers 1–4 in Lean) | Extend the Lean proof to every finite carrier |
| The advance retains distinctions; the carrier is finite | Three-phase cycle | Still assumed. Without retention the start may never return (`merging_change_leaves_transient`), so retention is **proved necessary** for return to the start | Derive retention from the port's own activity |
| Period 3 | Three-phase cycle | Periods 1, 2 and 4 **proved impossible** under R0–R2; period 5 also qualifies, so 3 is **not forced** | Derive the selection among admissible periods, or derive R0–R2 |
| R0–R2 requirements; arriving knowing both values; unknown start; cell count read from the Python source; the 3–8 bound | Phase-cycle study and its continuation | Still assumed (as listed by that study) | Derive each from the probe and inquiry they serve, or show the claim fails without it |
| Gate formula `arrival = (x xor tau) ∧ ¬blocked` | Native port | Still assumed. The classes derived from it are **derived** (`profile_equal_iff_target_equal`) | Derive the gate from contact and alignment activity |
| Changes of the contact | Contact formation | **Derived:** only formation changes it (`change_requires_formation`), and the decision to form is sound and complete (`decision_identifies_contact`) | Closed |
| Formation clears `blocked`; recovery of 10 dissipated units per pair; the draw used for formation; the inquiry schedule | Contact formation | Still assumed | Derive the formation step and the inquiry from the port's own operations |
| Rates (16,384 + peak, 655,360, 10 per probe, 2 cells) | Native port | Still assumed. Conservation is **derived without them** (`execute_conserves`) | Make the theorems parametric, or derive the numbers |
| Fault settings stay fixed during execution | Native port | **Derived** (`execute_retains_parameters`); every result holds for all 32 settings | How faults form is outside this claim |
| Completion order; A/B/C classes; probe table | Native port | **Derived** (`probe_complete_iff`, `native_gate_is_macro_receipt`) | Closed |
| Receipt calibration (`receiptFlip = false`) | `aligned_probe_realizes_macro` | Acquired in the contact track (`inquiry_calibrates_receipt`); **still a hypothesis** of the macro theorem | Compose the two theorems |
| Known common phase | Alignment schedule | Still assumed. The contact track's inquiry needs an intact reset; a broken reset leaves the phase unknown | Derive phase acquisition in Lean for this port |
| One packet (`source = 10`) | Macro projection | **Proved necessary:** the projection fails at two packets (`two_packet_state_outside_projection`) | Closed as scope |
| Permissive macro controls | Inquiry layer | Still assumed; proved more permissive than native execution | Replace with native control commands |
| Python port ↔ Lean port | Correspondence | Finite check of 5,928 cases; beyond them still assumed | A refinement proof, or treat Lean as primary |
| `safe` and `goal` contracts | Inquiry layer | Derived for the packet case (`probe_safe_iff_not_denied`); still assumed in general | Derive per application |
| Positive enactment per event | U2 necessity results | **Proved necessary:** a process that enacts nothing needs no arrival (`free_process_has_no_unit_enactment`) | Closed as scope |
| Lifetime, parent and rank conditions | U3 deadline | **Proved necessary** one by one (`renewing_has_no_strict_type_rank`, `infiniteChain_alive_at_every_time`, `external_arrivals_without_internal_parents`) | Closed as scope; each application must establish them |
| Lean's `propext` and `Quot.sound` | 124 audits in separate builds: conditional 26 of 60, native port 17 of 23, renewal 81 of 95 | Still assumed (axioms) | Re-prove constructively, as the 32-module closure and contact track already are (all audits empty) |
| Lean's logic itself | Everything | Framework presupposition; not declared discharged | — |

