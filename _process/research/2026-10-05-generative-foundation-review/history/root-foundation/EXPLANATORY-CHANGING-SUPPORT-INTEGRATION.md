# Changing support, preserved readiness and actual completion

8 October 2026, Asia/Bangkok. AI-authored continuation of [Ren’s instruction](../../../../sources/15-codex-theory-conversations/2026-10-08-generative-explanatory-necessity.md#继续变化中的支持--continue-changing-support). The [preceding study](EXPLANATORY-GLOBAL-REALIZATION-INTEGRATION.md) connected complete support footprints to common holding under fixed access. This round advances **changing support → preservation or renewal of a joint-plan certificate → completion in the same transition law**.

**Result / 结果。** A certificate distinguishes already acquired supports that must remain held from pending requests that can be acquired directly. For explicit formation, withdrawal, acquisition and release updates, simple relevance guards characterize preservation of that certificate exactly. Any finite guarded history preserves readiness and has a completing suffix in the same physical change process. A natural-number-indexed permitted schedule preserves the certificate at every finite position. Completion is characterized by the number of scheduled plan-advance steps, not inferred from safety alone.

**Failure and renewal / 失败与恢复。** A competing acquisition leaves the available-support list and the plan unchanged, yet invalidates its certificate and blocks its next acquisition. Releasing that support restores readiness and permits completion. The successful formation witness uses an existing available, unoccupied seed to make a previously absent support available, then acquires it. Losing an already completed holding can invalidate the whole certificate even when every pending request remains feasible. A genuine infinite occupation/release schedule preserves readiness but never advances the target.

**42 new Lean theorems (13 + 15 + 14), 211 audits including 169 inherited.** New dependencies: 6 empty, 9 `propext` only, 27 `propext`/`Quot.sound`; none adds classical choice. The whole closure has 119 empty and 92 standard dependency lists. There are no custom postulates or proof holes. Supporting lemmas are included in the count; it is not a count of independent discoveries.

## 1. Fix the explanatory target before claiming necessity

The target here is a fixed finite request list with a stronger continuing promise: supports already acquired for that target remain held, and all pending requests can be acquired without first repairing missing or occupied support. This is **continuous readiness plus retained progress**, not merely eventual attainability after arbitrary repair.

The distinction matters. A competing acquisition can break readiness temporarily and then be released, after which the whole goal is achieved. Therefore the preservation guards are necessary and sufficient for the selected certificate at each step. They are not necessary for every eventually successful history, nor universal prohibitions on loss, release or transformation. An explanation of eventual realization may correctly include such temporary failures and their recovery.

Activity, support formation, occupation, release and the running plan are differentiated relations within one configuration. A change is called additional relative to its role in this specified plan, not because it comes from a fundamentally separate environment. The target and its bookkeeping are supplied for this inquiry; the proofs do not derive its ethical priority, formation of motivation or the origin of its selection.

This advances explanatory necessity by identifying a concrete omitted relation: an unchanged plan and available-support description can cease to warrant readiness because the actual shared occupation changed. An adequate account of the continuing promise must retain that relationship or an equivalent way to recover its consequence.

## 2. The shared change law and certificate

`Configuration` has available-support and occupied-support lists. Its local operations are:

| Operation | Enabled when | Effect |
|---|---|---|
| `form seed new` | Seed is available and unoccupied; new support is absent. | Add new support to availability; keep the seed and current occupation. |
| `withdraw a` | Support is available. | Remove it from both availability and occupation, allowing actual loss of a holding. |
| `take a` | Support is available and unoccupied. | Append it to occupation. |
| `release a` | Support is occupied. | Remove it from occupation while retaining availability. |

This is an explicit atomic model. Formation uses a declared catalytic rule, not an inferred physical recipe: the seed remains, no budget is consumed, and candidate identities lie in an already supplied type. It establishes formation of availability within that domain, not creation of a new ontology or a universal productivity law. Distinctness and occupied-support inclusion in availability are preserved from a well-formed initial configuration by every enabled update, including unguarded ones.

`Certificate configuration done remaining` says:

1. `done ++ remaining` has no repeated exclusive support;
2. every completed support is still occupied;
3. remaining requests are available, unoccupied and nonduplicated.

The third clause directly reuses the preceding `Admissible` criterion. No stored Boolean or old successful proof label is treated as proof of current validity. The concrete example below shows why the occupation relationship cannot simply be omitted.

## 3. Exact preservation conditions, rather than freezing the configuration

For an initially valid certificate, `change_preserves_iff_guard` proves:

| Update | Exact condition for retaining this certificate |
|---|---|
| Formation | Always preserves it, when that update is executed under its stated law. |
| Withdrawal | The withdrawn support is neither completed nor pending. |
| Additional acquisition | It does not occupy a pending support. |
| Release | It does not release a completed support. |

The same rule handles planned acquisition differently because its role differs. Advancing the plan acquires the head of `remaining`, appends that support to `done` and removes it from `remaining`. `advance_certificate` proves that this bookkeeping and physical acquisition preserve the certificate. It does not treat the very same pending request as an unrelated competing occupation.

`guarded_iff_preserves` establishes the exact characterization for each enabled raw plan step. The guards use request membership and event effects; their meaning is checked against the full post-state certificate. They permit unrelated formation, withdrawal, occupation and release, so preservation does not require the whole configuration to remain unchanged. These are target-relative conditions, not a proof of an independently justified right to enforce them on every other activity.

## 4. Close the implementation gap for this local process

A plan `Position` contains the physical configuration and the completed/pending lists. A change event invokes the corresponding native update; an advance event invokes the very same `take` update while moving the plan cursor.

`trace_has_native_history` projects every guarded plan history to a native configuration history of the same length. `guarded_trace_wellformed` preserves the physical consistency conditions. This closes the preceding arbitrary-model implementation gap **for this specified protocol**: the completion steps no longer rely on an unrelated acquisition semantics.

`trace_valid` and `trace_goal` preserve both the certificate and the original request list. `after_every_history_can_complete` proves that after every finite permitted history from a valid start, a suffix of plan advances completes all remaining requests and holds the entire original goal. `complete_by_advancing` constructs that suffix by induction, using exactly as many acquisitions as remaining requests.

`unbounded_schedule_certificate` establishes validity at every finite position of any natural-number-indexed schedule satisfying the guarded step law. It does not construct physical infinite time or ensure the scheduler chooses progress. The proof requires every relevant change to obey the admitted law, atomic checking/use of current conditions, and an initially valid certificate. Access to complete current occupation and enforcement of all relevant changes are supplied model conditions, not acquired observation or deployed synchronization results.

`native_plan_initial_certificate` connects the previous footprint plan to the new initial certificate at empty occupation. Thus the static result is reused and transported into the changing protocol rather than reopened.

## 5. Same snapshot, different current readiness

The ready position has available supports 0 and 1, no occupation, and requests `[0,1]`. A competing acquisition of 0 is physically enabled. It keeps the available list, completed list and pending list identical, but 0 is now occupied.

`competing_acquisition_invalidates` proves that the current certificate fails, and `stale_plan_cannot_advance` proves that its next planned acquisition is blocked. `static_snapshot_unchanged` and `no_snapshot_certificate_reader` show there is no exact certificate reader from just those three unchanged lists for all positions. This is an actual reachable-change counterexample to that projection, not an arbitrary flip of a readiness predicate.

The competing acquisition is excluded by the preservation protocol, as it should be for a promise of uninterrupted readiness. It remains part of the raw physical model. `release_restores` and `restored_plan_completes` exhibit recovery after that disruption. The negative result is therefore not that the original goal became permanently impossible.

A second example releases a support already listed as completed. The remaining request is still available and unoccupied, but the whole certificate fails. `pending_success_omits_completed_loss` makes precise why checking only what remains to be done can lose the common-holding target.

The formation example starts with available seed 0 and request 1. It lacks immediate readiness, but an enabled formation operation creates availability of 1 and establishes the certificate; a subsequent acquisition completes it. The original state already admits this dynamic formation history. It would be incorrect to describe the example as creation of possibility from an absolutely impossible state.

## 6. Readiness can persist forever without completion

`trace_progress_count` proves that final pending length plus the number of plan advances equals initial pending length along every guarded finite history. `completion_iff_progress_count` therefore characterizes when that history completes.

`never_finishing_schedule` constructs an actual infinite permitted schedule. Support 0 remains pending and free. The schedule repeatedly takes and releases unrelated support 1, and never schedules a plan advance. Every position remains certified; the goal never completes. The witness performs real updates rather than inserting a formal no-op.

This strengthens the scope distinction within the same model: a completing continuation exists after each finite position, while the selected actual continuation never completes. A further scheduling or progress premise is needed for inevitable completion. This is not a newly discovered safety/liveness distinction and does not imply an ethical duty to select this particular goal.

## 7. Counterreview, existing results and primary sources

| Challenge | Assessment |
|---|---|
| Exact guards merely restate validity. | The guard is a local membership condition per operation; the theorem derives equivalence with the full post-state certificate from the update equations. Its scope and initial validity remain explicit. |
| Excluding a competing acquisition is necessary for any eventual success. | False. The checked release-and-completion history succeeds after interruption. Necessity here is preservation of continuous readiness, not unrestricted eventual realization. |
| Completed supports are assumed to belong to independent owners. | No ownership or independent-agent type is supplied. `done` tracks this plan’s acquisitions within a shared history. The model proves holding membership, not unrestricted notions of property or personal identity. |
| Formation proves real-world creation without supplied means. | No. It is enabled by a free available seed under a supplied catalytic law. Costs, fabrication and identity provenance remain unresolved correspondence. |
| Passing a guard ensures trustworthy acquired evidence. | No. Guards use the model’s current state directly. Sensing, stale reads, non-atomic test/use and enforcement are not solved here. |
| Preserved readiness proves inevitable realization. | False, by the infinite competing-work schedule. Completion needs actual progress steps. |
| Guarding every relevant change is already a strong premise. | Correct. It identifies the precise protection needed in this protocol; it does not show that all real histories satisfy it. |
| All of this is new mathematics. | No. Invariant preservation, local reasoning, interference control and safety/liveness are established techniques. The contribution is their checked, explicitly scoped connection to this explanatory investigation. |

Read the repository’s [correction-handoff integration](CORRECTION-HANDOFF-INTEGRATION.md) in full. It already proves repeated protocol invariance, native probes, prescribed completion and the distinction from arbitrary scheduling. Those 23-theorem/45-audit results retain their scope. This round does not reopen them: it treats shared physical support, exact per-update certificate conditions, formation/repair and a projection that loses current occupation. It makes no new claim to solve corrigibility or dynamic authorization.

Read O’Hearn, [*Resources, Concurrency and Local Reasoning*](https://flint.cs.yale.edu/cs428/doc/concurrency.pdf), introduction and the returned portions of §2.1–2.3 on ownership and separation (PDF pp. 1–7). The paper develops local reasoning with changing resource partitions and discusses transfer, interference and the distinction between operational state and logical ownership. This is a clear precedent for stable reasoning through changes. The present model does not reproduce its concurrent proof system or soundness proof. The [Yale reading list](https://flint.cs.yale.edu/cs428/reading.html) supplied the paper link; the [Cambridge seminar abstract](https://www.cl.cam.ac.uk/research/ls/Talks/2004_05/2004-11-12.O_Hearn.html) was read for historical context. No source bytes were imported; no priority claim is made.

This is author counterreview, not independent-agent acceptance. No empirical experiment or external communication was performed.

## 8. Proof inventory and reproduction

| Source | New theorems | Scope |
|---|---:|---|
| [ExplanatoryChangingSupport.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/ExplanatoryChangingSupport.lean) | 13 | Change laws, exact certificate guards, advance and physical well-formedness. |
| [ExplanatoryStablePlans.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/ExplanatoryStablePlans.lean) | 15 | Same-law projection, arbitrary histories, unbounded certificate preservation, completing suffix and exact progress count. |
| [ExplanatorySupportChanges.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/ExplanatorySupportChanges.lean) | 14 | Reachable stale snapshot, lost completed support, actual formation/recovery and infinite noncompletion witness. |

The [immutable receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/explanatory-changing-support-checks/20261008T095528.481203Z/receipt.json) freezes fifteen modules and uses Lean 4.29.1. Run `python3 experiments/integrated-correction/general-framework/generative-basis/lean/deeper/check_explanatory_changing_support.py`. The isolated runner rejects holes, custom postulates, unsafe bypasses and warnings, then records source/log bindings and per-declaration dependencies. The 169 inherited audits remain unchanged: 113 empty and 56 standard. New 42: 6 empty, 36 standard; no new proof depends on classical choice. The full 211 audits retain inherited classical dependencies where present.

[Documentary checks](EXPLANATORY-CHANGING-SUPPORT-CHECKS.json) bind inventory, frozen/current sources and logs, inherited dependencies, links, chapter continuity and paired C30/F22 rows. [Owned edits](EXPLANATORY-CHANGING-SUPPORT-INDEX-EDITS.json) preserve old row content and the previously checked chapter/source bytes. Local passing checks do not certify concurrent full-table freshness.

## 9. Integrated conclusion and next discriminating question

**中文。** 充分解释变化中的共同实现，需要区分当前准备、已实现部分的保留、变化后的恢复，以及实际调度的完成。当前过程已把这些关系接入同一历史：可用清单不变而占用改变会使旧证书失效；释放和形成可以恢复或建立准备；保持准备仍不迫使实现。保存关系内容的必要性得到更具体的支持，但没有推出当前表述或生成本体的普遍唯一性。

**English.** The changing-support bridge is complete for a fully mediated atomic protocol with a supplied fixed target and formation law. Its next universal burden is warranted scope: when an explanation promises robust or eventual realization, which changes and progress conditions does that promise cover? A concrete next test may relax atomic test/use or the assumption that every relevant update follows the protocol. It must retain the current successful law and failure histories rather than restate a predicate named reliable. Goal revision, empirical formation and universal ontology remain distinct tasks; existing ethical grounding is not reopened.
