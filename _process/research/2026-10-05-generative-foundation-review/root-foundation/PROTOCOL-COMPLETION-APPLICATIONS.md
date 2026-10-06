# Completion contracts for existing paid protocols

6 October 2026. AI-authored source audit and application of the general completion extension. No inherited sources or scientific experiment outcomes were changed. The additive [PredictionProtocolCompletion](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/learning/PredictionProtocolCompletion.lean) contributes thirteen theorem audits. The combined fresh Lean 4.29.1 [build receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/learning/protocol-completion-audit.json) passes 34 new and 244 inherited audits across fifteen modules; the bounded [independent internal review](PROTOCOL-COMPLETION-REVIEW.md) is accepted. Failed development attempts and the successful local compiler output are retained in its separate development directory.

## What the new result adds

[ProtocolComposition](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/learning/ProtocolComposition.lean) already proves completed-block realization and accounting, `block_length_bound`, `internal_trace_rank_bound` and `no_infinite_internal_execution`. These are deliberately insufficient to establish completion: a finite internal state may have no enabled continuation.

The useful extension combines an invariant, an actually enabled first event, internal nonblocking and strict descent on **every permitted internal successor**. It can establish finite completion for maximal committed executions and rule out both finite internal deadlock and an infinite internal event sequence. An arbitrary finite prefix may still stop early. A physical actor may still not be scheduled at all. Without a clock or a scheduling premise this is an event-count result, not a bound on elapsed time.

Initial boundary admission must be explicit: a first-return block is nonempty, although its starting state already satisfies the boundary predicate. Stopping immediately at that initial boundary cannot discharge the promised command. Conversely, completion does not imply that another command is affordable at the returned boundary.

## Strongest immediate application: the existing predictor trial

[PredictionProtocolBridge](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/learning/PredictionProtocolBridge.lean) supplies the exact existing instance:

- `trialProtocol p`: boundary is `phase = ready ∧ score ≤ 4`. Formation and reversal are excluded from this committed trial.
- `committed_event`: every enabled committed event is `nextEvent s.phase`.
- `cycle_enabled_iff_macroGuard`: the direct sequential affordability predicate is equivalent to `PredictionAction.CycleEnabled`.
- `blockPath_iff_cycle`: **if a block completes**, it has command `a = command s`, all four guards, word `[rent, work, write, finish]` and endpoint `cycleEnd p s`.
- `macro_trace_iff_realization`, `realization_event_count`, `realization_source_consumption` and `realized_prefix_ledger`: already compose completed trials through actual states and retain all source and expense accounts.

The application starts with `score ≤ 4`, `a = command s` and `macroGuard p s a`. Its phase rank is `ready ↦ 3`, `rented ↦ 2`, `observed ↦ 1`, `written ↦ 0`. The rank strictly decreases on each internal transition. `finish` returns to the boundary and need not decrease the rank.

A suitable internal invariant is the bounded score together with the remaining sequential guards and retained command:

| Phase | Additional continuing obligation |
| --- | --- |
| rented | `a = command s`; both leases positive; one packet available; work affordable; writing affordable after that actual work/receipt |
| observed | `a = physical.core.selector`; both leases positive; writing affordable |
| written | `a = physical.core.selector`; both leases positive |
| returned ready | No promise of another paid trial |

Rent preserves command, work records it in the existing selector, and writing can alter the **next** command without changing the executed selector. The inherited score theorem preserves the boundary's bound. These facts provide nonblocking for each internal phase. Together with forced event shape, the new result can establish completion in exactly four events for every maximal committed execution from the admitted state, rather than only constructing one four-event witness.

The implementation spells the internal obligations as `PredictionAction.Enabled` checks on the remaining actual phase successors, not as existence of a completed trace. Its ready `Live` branch includes the full initial guards. The generic contract preserves `Live` only at nonboundary successors, so it correctly does not require the returned ready state to satisfy that branch again. `maximal_admitted_trial_exact` gives the finite maximal-attempt word and actual `cycleEnd`; `admitted_no_internal_deadlock` and `admitted_no_infinite_internal_run` supply the complementary progress conclusions.

`macroGuard` tests writing after the actual return and refers to the deterministic plant's response. It is a mathematical sequential-affordability predicate, not proof that the actor possesses a sensor for a future hidden outcome or prepays every bill. `sufficient_initial_fuel_admits` proves the stronger sufficient guard available from the current stores: `fuel ≥ rent + work + writing`, positive leases and a packet, with maintenance no greater than packet value. Under that stronger guard both capture and mismatch leave enough to write. This sufficient condition does not replace the sharper existing guard, and does not install escrow or new sensing hardware. `unpaid_observed_state_not_live` and `completion_need_not_renew_admission` retain the shortage and exhausted-endpoint boundaries as exact finite statements.

The exact failure boundary already exists in [PredictionOverlap](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/learning/stochastic-prediction/PredictionOverlap.lean): `unpaid_write_is_not_old_completed_cycle` uses initial fuel 4, primary tariffs and an actual mismatch. Rent and work spend the four units, leaving the old phase law observed with writing disabled. Positive initial rent/work affordability alone does not give the required invariant. `no_work_is_not_old_source_boundary` separately preserves a paid rent prefix with insufficient work fuel. The completion extension must not erase either state.

## Minimal positive and negative examples are already present

[ProtocolExamples](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/learning/ProtocolExamples.lean) supplies a transparent second instance. For `protocol false`, start at `ready (fuel+1) (source+1)`, pay one usable unit, then convert one actual source unit. Rank ready=1/busy=0, preservation of positive source while busy and `nonstall_busy_step_finishes` supply a two-event completion contract.

The same file already names the two independent obstructions:

1. `paid_deadlock_prefix` and `nonstall_exhausted_deadlock`: paying from ready fuel1/source0 reaches busy0/source0. Strict descent holds but internal nonblocking fails. Terminal net balance is not prepayment.
2. `infinite_committed_busy_run` and `busy_run_never_returns`: `protocol true` permits a busy self-loop even with available source. Nonblocking holds but descent fails. `completed_steps_agree` and `completed_histories_agree` show that identical completed macro histories do not identify completion behavior.

No additional invented process is needed to demonstrate why both hypotheses matter.

## The stochastic exposure already has a different completion boundary

The accepted [stochastic exposure package](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/learning/stochastic-prediction/README.md) defines a total `StochasticPrediction.exposure` function and a structurally finite `run` over a supplied list. `FiniteExposureKernel.exposure_mass`, `paths_mass`, `paths_realized` and `closed_source_account` retain all tape outcomes, actual successors and finite source expenses. Returning a `workedUnpaid`, `noWork`, `rentFailed` or inactive result completes that **call**; it does not complete the old payable write trial or guarantee useful learning.

In particular, the runtime exposure expires an unworked scheduled packet and returns the worn continuing carrier after an unpaid write. The old phase law does neither. `payable_cycle_overlap` requires the unchanged old `CycleEnabled`, availability true and maintenance bounded by the packet. No generic completion theorem can enlarge that proved overlap without a new correspondence contract. The new result should therefore instantiate the old four-event committed trial, while retaining the total exposure as its separately scoped stochastic client/comparator. It need not rebrand finite-list recursion as a new physical progress theorem.

## Why the accepted evaluator and successor do not become an automatic pipeline

The [accepted acquired evaluator](../../../../experiments/shared-renewal-capability/regulation/retention/formation/selectors/updaters/prediction/recipient-correction/identification/recording/reason-consumer/action/revision/evaluation/formal/README.md) proves guarded transitions, exact ledgers, a staged construction and a selected actual enabled history. In `AcquiredEvaluation`, `current_selected_trial_effect` assumes an actual trial trace, `PublicationBridge.Assured`, `Known`, supplied `G` through the assurance premise, and equality of recipient laws between observation and use. `EvaluationWitness.whole_actual_trace` and `actual_staged_composition` do not remove these premises or establish every scheduler's completion.

There is a direct obstruction to that stronger reading: `AcquiredEvaluation.Enabled` admits `.scope _`, `.permission _` and `.delivery _` unconditionally. This is not merely an enabled-event observation. For a fixed evaluator state `s`, choose `e = permission s.parent.parent.permission`. `AcquiredEvaluation.advance` routes it through `old`, then `FreshRevision.actionAdvance`, then `RecipientAction.advance (.setPermission v)`. The last operation changes **only** `permission` to `v`, and the two enclosing updates change only their nested `parent` fields. With `v` already equal to the stored permission, the entire evaluator state is unchanged. `AcquiredEvaluation.charge` assigns that event zero. Therefore the constant state sequence `s_n = s` and constant event sequence `e_n = e` form an infinite enabled zero-cost run. This conclusion follows from the actual update equations, not from `Enabled` alone.

Thus the complete unchanged event relation does not admit strict descent for all its events. A completing policy would have to state what commitment excludes or schedules those events. Permission denial, stale evidence, pending reads and finite replacement stock also retain their existing meanings; a completion theorem cannot turn an allowed abstention into obligatory delivery.

The [successor-learning proof](../../../../experiments/shared-renewal-capability/regulation/retention/formation/selectors/updaters/prediction/recipient-correction/successor-learning/formal/README.md) likewise distinguishes `allEnabled`/`enabled_list_is_trace`, `learning_events_are_enabled` and `joined_learning_and_recopy_trace` from unconditional execution. `corrective_use_threshold` and `revised_copy_threshold` condition on completed productive warmups and an ordered payment history. They do not supply missing components, source, calibrated correspondence, permissions or nonblocking after every possible failed prefix. Its executable outage/shortage branches extend beyond the formal fully paid noiseless relation.

The bounded advance is therefore precise: completed-history correspondence now has a reusable criterion guaranteeing a committed command's finite return on its admitted invariant domain. It does not imply full-pipeline termination, eventual success, calibrated learning, perpetual renewal or completion of the unified foundation.
