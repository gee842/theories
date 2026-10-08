# 变化依存与描述的有效期 / Changing dependency and the useful lifetime of a description

8 October 2026. AI-authored continuation of [Ren's repeated direction](../../../../sources/15-codex-theory-conversations/2026-10-08-relations-across-scales.md). [Current account §14](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/RELATIONS-ACROSS-SCALES.md). The [prior inquiry comparison](INQUIRY-CHOICE-INTEGRATION.md) is credited at its constant-loss scope. This extension addresses **acquired evidence → validity through changed dependency → realizable response**. It supplies a calibration/implementation premise for practical judgment, not new ethical authority.

## Affirmative argument and hypotheses

A description is not adequate merely because it preserves the relevant coordinate at acquisition. Its relation to the consequence being judged must remain valid through the response horizon. Three checked general connections make this requirement precise:

1. Condition-estimation and loss-estimation errors add in predicting the next unassisted condition. Sensor error plus post-acquisition change likewise bounds current reading error. Any finite sequence of stage-error bounds supplies a cumulative bound.
2. Given forecast `r`, symmetric error bound `E`, target interval `[L,B]` and support `S`, the full-interval certificate is equivalent to `max(0,L-r+E)≤u≤min(S,B-r-E)`. It transfers to the actual outcome only when `|actual-r|≤E`. For physical interpretation require `E≥0`; the algebraic certificate equivalence itself does not require positivity.
3. Such a certificate requires `2E≤B-L`. For a supplied error growth model `E=sensor+rate*age`, its necessary budget is `2*rate*age≤B-L-2*sensor`. Nonnegative error and positive rate are interpretation premises for an expiry horizon; the source theorem is an algebraic implication. Support or one-sided intervention limits can preclude certification earlier. The sum bounds need not be tight.

The target and tolerances are explicit inputs. No scalar ethical ranking is encoded, and no uncertainty estimate is inferred merely from earlier success. When the represented uncertainty interval is conservative, failure to certify is weaker than actual impossibility. In the separate narrow-target witness, actual admissible endpoint histories do rule out one common early correction.

**关系上的推进：**认识在取得后仍参与变化；描述的适用性取决于这种关系能否持续到实际后果。需要说明哪些改变已经被界限包含，哪些使原对应失效。重新取得证据是同一活动的后续事件，并不把认识移到过程之外。

## One inherited state and explicit changed law

The model imports `InquiryChoice` and reuses `ScaleRevision.State`, `drift`, `probeBody`, `paid`, `workTotal`, and `InquiryChoice.deliverBody`. It is a new event law on the inherited state, not the old schedule with unstated altered meanings. A `shift` replaces the loss coordinate `b`; a read takes one drift stage and stores both the actual decrement and the second coordinate, allowing the current condition to be reconstructed as stored total minus stored second coordinate. These two scalar readout channels, exact calibration and their shared operation tariff are supplied. They are not claimed to be physically synthesized here.

Reading, dependency, response and support are differentiated roles in this one state. The supplied shift takes no modeled stage or operating work, representing a regime update before the next elapsed stage. It is not a formation explanation and the timestamp example depends on this event convention. The more general point is supported by the error formulas: even a sufficiently recent reading needs a bound on what changed, not a timestamp alone.

Each read or attempted intervention consumes 1044 inherited abstract work ticks. Waiting advances drift without an operating-work charge. The account conserves `fuel+spent` for every finite event history, including dependency shifts. This is bookkeeping under a supplied tariff, not physical energy conservation. Signed condition `a`, support source and work remain distinct. The source does not regenerate; the controller's stopped state stutters and does not assert that a body stops changing.

The main initial state has `a=12`, actual loss 1, support 5 and work 3132. After the first read: `a=11`, acquired loss 1, current stage 1. A shift to loss 3 keeps the timestamp but changes the actual next condition from predicted 10 to 8. Stale response projects the last loss across two remaining stages and chooses zero; it ends at 5. An early correction using upper loss 3 chooses 2 and ends at 7. Reading again before response also ends at 7 with correction 2 but uses 3132 rather than 2088 work. All finish at stage 3, with equal starting support and work. The broad target is `[7,11]`.

`bounded_response_covers_variable_losses` covers every pair of losses in `[1,3]`, not just constant loss. A generic theorem also transfers the preceding robust interval result to two unequal bounded stages by their mean; it does not require that the process actually be constant.

## Narrow targets, fresh-reading failure and repair

For target `[7,9]`, the two-stage unassisted possibilities 5 and 9 need incompatible early doses (at least 2 versus at most 0). This is a genuine common-response obstruction within the one-intervention repertoire. It does not exclude richer split-action or continuous-feedback repertoires.

A refresh under stable low or high loss reaches 9 or 7. A subsequent change from acquired loss 1 to loss 3 still happens to meet the target: forecast error does not always cause condition failure. But a refresh acquired at loss 2 followed by loss 3 reaches 6, even though both losses remain inside `[1,3]`. The exact-continuation response rule delivers zero; the accurate new reading does not certify the future. An additional witness with subsequent loss 4 preserves failure outside the earlier bound as well.

`refreshedBound` repairs the within-bound failure by retaining the possible remaining loss range. From acquired condition `11−first`, it chooses `max(0,7−(11−first)+3)=first−1` for `first∈[1,3]`. For all `first,second∈[1,3]`, the general theorem proves nonnegative source-bounded correction and terminal condition in `[7,9]`. The actual failed history (2 then 3) now delivers 1, ends at 7, leaves source 4 and consumes 3132 work. The repaired rule remains subject to truthful readout and the declared future bound. It does not identify a previously unknown safe bound or guarantee against loss 4.

## Theorem map and checked scope

All names below are in namespace `ChangingDependency` in [the source](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/systems-complexity/analysis/ChangingDependency.lean).

| Group | Names |
|---|---|
| Error propagation | `forecast_error`, `cumulative_error`, `acquired_error_after_change` |
| Variable dependency | `variable_two_stage_response` |
| Response certificates | `certificate_transfers`, `certificate_iff_interval`, `uncertainty_requires_tolerance`, `smaller_error_preserves_certificate`, `error_growth_budget` |
| Acquired readings and joint law | `read_obtains_condition_and_loss`, `run_is_core_trace`, `changed_dependency_keeps_timestamp`, `run_work_conserved` |
| Stale and bounded routes | `current_stamp_can_have_wrong_forecast`, `stale_response_misses_target`, `bounded_response_meets_target`, `bounded_response_covers_variable_losses` |
| Refresh cases | `refresh_meets_same_horizon`, `refresh_is_useful_when_loss_stays_low`, `changed_reading_can_still_meet_target`, `unbounded_change_defeats_refresh`, `within_bound_change_defeats_exact_refresh` |
| Narrow target and repair | `narrow_tolerance_defeats_old_bound`, `bounded_refresh_covers_variable_losses`, `bounded_refresh_repairs_actual_failure` |

The general certificates concern their stated algebra and correspondence; the exact charged executions concern the explicit finite schedules. There is no generic compiler correctness theorem from every certificate to every arbitrary event history. Reproduction: `python3 experiments/integrated-correction/general-framework/generative-basis/lean/systems-complexity/analysis/check_changing_dependency.py` from the repository root. [Formal receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/systems-complexity/analysis/changing-dependency-verification.json) and [document/source checks](CHANGING-DEPENDENCY-CHECKS.json) retain separate scopes.

The final formal package contains **25 new theorem audits**, with **161 inherited audits** replayed (18 core + 24 exact organization + 21 first scales + 43 remaining dependency + 27 scale revision + 28 inquiry choice). The seven local modules are freshly compiled under Lean 4.30.0-rc2 and pinned Mathlib `ea11ccc0c5c7c4c562742e918fe2e0b2814a58aa`. Upstream library caches are reused. Only standard `propext`, `Classical.choice`, `Quot.sound` occur in new axiom dependencies; no holes or custom axioms are admitted. Later additions strengthen the tested adversarial case and implement its bounded repair; prior successful source packages remain unchanged.

## Substantive counterreview by the same agent

- **Is a timestamp being unfairly represented?** The event law permits a zero-stage regime change. Therefore the witness concerns this timestamp convention, not all physical clocks. The general error certificate, rather than this convention alone, carries the broader argument.
- **Is bounded response preferable to inquiry?** Only for the broad target and supplied work law in this comparison. The narrow target has no common early dose. Reacquisition plus a future bound succeeds there; both routes have legitimate scopes.
- **Does a fresh accurate reading warrant exact continuation?** No. The within-bound 2-to-3 witness directly defeats that inference. The repair retains an independently supplied future bound instead of assuming stability.
- **Do larger margins always help?** No. The certificate includes the upper target and source constraints. Large error can eliminate the entire admissible interval; uncertainty is not converted into unlimited intervention.
- **Does this establish superiority over control theory?** No. A conventional controller retaining these readings, uncertainty bounds and support constraints can implement the same comparison. The contribution is integration and explicit failure scope within this repository's theory.
- **Has actual biological validity been established?** No. The loss shifts, channels, tariffs, thresholds and dynamics are declared. The omitted calibration is an application obligation; it is not evidence that the fuller relational theory fails or that all knowledge is unreliable.

This is same-agent counterreview, not independent verification by another agent. Mathematical checking is actual Lean execution; conceptual and empirical standing remain distinct.

## Primary-source comparison

Re-read the [author-hosted draft of Tabuada, *Event-Triggered Real-Time Scheduling of Stabilizing Control Tasks*](https://www.seas.ucla.edu/~tabuada/Papers/EventTriggered.pdf), pp. 1–3, especially §2's measurement-error definition and sampling/computation/actuation delay. The draft explicitly anticipates error growth during the interval before actuation and assumes a controller with stated stability properties. This supports crediting existing control research for temporally valid feedback. Our discrete finite law proves neither its scheduling nor stability theorems. This is a deeper reuse of an already cited source, not new independent evidence or an empirical test. No original publication bytes were imported; the final journal edition and complete proof were not assessed in this round.

## Integration and next test

This round removes constant dependency as an unnoticed interpretation of acquired evidence. It supplies bounds for changing relations, a common-deadline comparison, a real failure of exact continuation after a fresh reading and a checked bounded-change repair. The remaining substantive application is to warrant the change envelope and target tolerances from actual mechanism or records, and challenge them on later changes. The [organized-scales biological study](ORGANIZED-SCALES-INTEGRATION.md) retains its stronger correspondence task; none of its empirical results is claimed as validation of these numerical examples. The theory has gained a conditional temporal-validity connection, not complete coverage of systems theories or a universal normative proof.
