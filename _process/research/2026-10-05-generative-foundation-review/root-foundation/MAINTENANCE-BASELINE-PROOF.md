# Original maintenance content after an intervention changes support

8 October 2026. AI-authored formal application. **Four new Lean theorems / thirteen explicit declaration audits** check when a changed maintenance specification still certifies the original finite undertaking. The [protocol](MAINTENANCE-BASELINE-PROTOCOL.md) and [argument](MAINTENANCE-BASELINE-ARGUMENT.md) supply the interpretation; the [Lean source](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/MaintenanceBaseline.lean) states the exact hypotheses.

The new control identifies a misuse of an existing theorem: withdrawing old support, substituting its reduced current capacity into the target, and treating the resulting vacuous certificate as completion of the original task. The old theorem remains valid for its supplied target. Actual completed delivery before retirement provides the positive contrast. No new ethical axiom, generic controller criterion or literature novelty is claimed.

## What is reused

The module imports `ObservableContinuation` unchanged, including its existing imports. All are rebuilt and audited separately from the new contribution.

| Inherited module | Relevant content | Inherited count |
|---|---|---|
| `AlignmentInquiry` | Actual contingent execution and checked finite selection | 9 theorems / 17 audits |
| `ChanceAdequacy` | Target-event inclusion, fulfillment and common-positive-total event-mass bound | 8 theorems / 14 audits |
| `ObservableContinuation` | Actual route effects, budget consumption and a finite one-delivery support mechanism | 4 theorems / 24 audits |

The inherited total is **21 theorems / 55 audits**, not new results. The relevant proof notes are [chance adequacy](CHANCE-ADEQUACY-PROOF.md) and [observable continuation](OBSERVABLE-CONTINUATION-PROOF.md). The generic argument below is ordinary conditional transport plus the existing mass theorem. J3's account of withdrawal and discharge, the earlier [maintenance argument](CHANCE-ADEQUACY-ARGUMENT.md), and [risk-reference revision](JOINT-RISK-REVISION-INTEGRATION.md#17-a-local-allowance-cannot-renew-itself-by-changing-the-reference) already supply the normative precedent. The new application does not reopen them.

## Transport through completed work or a remaining requirement

`target_transport_with_completion_gives_bound` uses one represented domain and one natural event-weight function. It distinguishes the original target, the current target, a completion record and actual delivery. Its premises require:

1. Every original target event is either recorded as completed or retained by the current target.
2. Every represented completion record corresponds to actual delivery of this task.
3. Actual delivery fulfills the current target.
4. The common total event weight is positive.

The conclusion is original-target fulfillment together with the original target mass bounded by actual-delivery mass, itself bounded by the same total. The theorem does not manufacture the target correspondence, establish the record's truth, or justify the original undertaking. It permits a genuinely completed requirement to leave the current pending target; demanding unchanged pending requirements would wrongly forbid completion.

As in the imported theorem, the formal inequalities concern natural numerators under a common positive total, representing finite rational event laws. They are not a theorem about arbitrary real measures. Event weights are not ethical severity weights. Represented conditions must be adequately covered and paired from a warranted common origin; repeated list entries must not unintentionally count the same event twice. Nothing licenses choosing a convenient pairing from unrelated observed marginal frequencies.

## Actual delivery and retirement in the same finite process

`Frame` retains the preceding mechanism's connection mode, remaining budget and response effect, adding an old-line availability flag and a completed-delivery record. The original left route works in the false mode; an independent right route works in the true mode. Single-route execution costs one unit, and parallel execution costs two, using the unchanged `ObservableContinuation.respond` law.

`retire` disables the old line without changing resources or inventing delivery. The new `enabled` guard prevents either left or parallel execution after retirement, since parallel execution here includes the old line. Right remains independent. `deliver` first checks availability and then invokes the actual budget-checked response. From the specified initial frames, its retained `delivered` field is formed by the response's actual support effect. `deliverThenRetire` retires only after that response returns successfully. This is a concrete causal construction, not a freely assigned ethical label or a release flag.

`demand = !delivered` represents **one specified delivery still pending**. Its decrease after successful delivery does not model an arbitrary disappearance of need. A retained completion record is evidence of the represented past delivery, not a claim that support remains available after retirement.

| New theorem | Checked result |
|---|---|
| `target_transport_with_completion_gives_bound` | The explicit completion-or-remaining-target correspondence yields original fulfillment and the inherited common-total mass bound |
| `retirement_can_erase_recomputed_target_without_fulfilling_origin` | Bare retirement makes current old support unavailable while demand remains and no delivery occurs. The recomputed current target is vacuously fulfilled; the original target is not. Original target mass is one and actual delivery mass is zero in the two equally weighted conditions |
| `actual_extended_delivery_survives_retirement` | Funded parallel execution actually delivers in both modes, consumes both units, and then retires the old line while retaining completion. The original task is fulfilled; its original success mass is one and actual delivery mass is two |
| `completed_single_delivery_allows_retirement` | Funded left execution consumes one unit and actually delivers in the false mode before retirement. It fulfills the original finite left-maintenance task; the completed false-mode task is no longer pending |

The parallel positive case completes an extended **single delivery before retirement**. It does not install a lasting successor or prove that a new route continues serving after the old route is closed. In the single-left case, the true-mode demand remains unserved; that condition was outside the original left-success target. Fulfillment of this specific undertaking neither erases that unmet need nor resolves every further G0/J/CP reason.

Three separately kernel-checked controls establish that retirement disables actual left and parallel execution, that the independent right route can still deliver in its working mode, and that the generic transport theorem accepts the independently checked completed-left record even though the retired current target is empty. They are application examples, not additional theorem counts.

## Limits of the application

The original task's warrant, period, content and permissible revision remain substantive premises. Natural failure, current inability, fulfilled work and legitimate discharge are distinct questions. Preserving the original comparison does not create missing resources, establish fault from causation alone, forbid justified withdrawal or require impossible performance. No arbitrary Boolean switch proves a legitimate release.

The scope is one delivery within the supplied window. There is no continuous-service guarantee, physical clock, new hardware installation, full failure-cost history or permission-acquisition theorem. The inherited route law and costs need actual correspondence before deployment. Although the negative control involves an intervention, it proves neither intentional deception nor a psychological motive.

The nondual account is preserved: delivery, consumption, withdrawal and the record used in evaluation are differentiated consequences of the same represented process. The precise universal-agency application is that an activity able to alter its support and assessment conditions must still correctly identify the undertaking it claims to have completed. The broader justification follows the existing G0/J argument; the Lean result checks this bounded application rather than proving all universal ethics or every adequate initial chance allocation.

## Actual verification and freeze

The [dedicated checker](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/check_maintenance_baseline.py) compiled frozen copies of all four modules in a fresh temporary import directory using **Lean 4.29.1**. It retained exact theorem signatures and axiom reports for every explicit declaration. The [passing receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/maintenance-baseline-verification.json) binds [run `20261008T121326.478309Z`](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/maintenance-baseline-checks/20261008T121326.478309Z/verification.json).

The run contains **4 new theorems / 13 new declaration audits**, **21 inherited theorems / 55 inherited audits**, **29 retained artifacts**, and the three checked application controls. Eleven new declarations have no axiom dependencies; the retirement counterexample uses `propext`; the generic transport uses `propext` and `Quot.sound`. No new custom axiom, `Classical.choice`, proof hole, unsafe/native proof shortcut or skipped kernel checking is used. Generated constructors, projections and deriving declarations are checked through compilation but not separately counted in the explicit registry.

The first compiler attempt passed; no failed attempt is claimed. Source and helper hashes were checked unchanged throughout the run. Independent counterreview is recorded in [the review](MAINTENANCE-BASELINE-REVIEW.md), separately from this compiler execution.

- Source SHA-256: `48d26515db6aa2a4e2692e22e1eea1586c95090b139d2a728a21031a8bd3ca77`.
- Dedicated checker SHA-256: `360814559168e7adc0defbab761d3910238c64656f68f8f8e5d3abb018c1a635`.
- Shared scanner SHA-256: `b9f56e1700c03f0019a486d0f3c097f70c2ce20414da9e7b231131b8ed4a8308`.

The source, checker and receipt are frozen. This closes the specified task-correspondence control without converting another finite implementation example into the remaining normative question.
