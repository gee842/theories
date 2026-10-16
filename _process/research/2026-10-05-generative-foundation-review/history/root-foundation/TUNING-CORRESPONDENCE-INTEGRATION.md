# Candidate generation, objective correction and residual-transfer correspondence

8 October 2026. AI-authored continuation of the active three-part request: **compose existing results, explain a supplied premise, and establish real-world correspondence**. The previous goal turn made verified progress by deriving recurrent memory bounds and obtaining independent acceptance. This study follows the stated next inference: the actual archived tuning procedure and the warrant for its response comparisons. It retains the original source bytes, the successful physical runs, the metric discrepancy and the earlier proof scopes.

## What is now established

The published candidate gains can be recovered under a pinned modern reproduction of the archived fitting/search contracts. Correcting signed movement to absolute movement **does not change the winning gains in that reconstructed source setting**: both select `Kc=10, tauI=55`. The metric discrepancy nevertheless reverses 8,454 of 32,640 pairwise candidate rankings. Thus a genuine source error need not invalidate the reported selected gains or their observed physical improvement.

The more consequential supplied premise is the transfer of fitted residuals to altered actions. A family of two-lag response models, each paired with a compensating output sequence, fits the original record exactly but selects different candidate gains. Lean proves the relevant identification limit through the same two-lag recurrence. Separately recorded physical validation runs do not support treating the original residual sequence as an exact reusable correction. This narrows the comparison claim instead of pretending that a model minimum is a guaranteed practical optimum.

## Source, software and actual fitting route

The [source-contract inspection](../../../../experiments/integrated-correction/general-framework/generative-basis/inquiry-correspondence/tuning-source-contract.json) binds the original archive and optimizer script. Its training `data.txt` is byte-identical to the already preserved initial PI run; it is not another experiment. The source fits two outputs against two recorded commands with order two, initial shifting, no range scaling and `pred='model'`, then reuses its output residuals during the gain search. The second recorded heater command is zero throughout that training file.

The [official GEKKO documentation](https://gekko.readthedocs.io/en/latest/model_methods.html) distinguishes output-error fitting from its measured-regressor alternative. The inspected installed `gekko.py` confirms the selected implementation and local solver path. This study uses **GEKKO 1.3.2, `remote=False`**, preserving package-source and solver-executable hashes, actual options, returned coefficients, predictions and solver log. That is a pinned modern reproduction; the archive does not specify its historical dependency environment. We do not claim to reproduce an unknown historical binary, certify a global nonlinear fitting optimum or replicate a physical trial.

[Fit runner](../../../../experiments/integrated-correction/general-framework/generative-basis/inquiry-correspondence/fit_tuning_model.py) · [fitted model and environment](../../../../experiments/integrated-correction/general-framework/generative-basis/inquiry-correspondence/tuning-model.json) · [actual solver log](../../../../experiments/integrated-correction/general-framework/generative-basis/inquiry-correspondence/tuning-fit-log.txt).

No original script was executed against hardware. The temporary GEKKO installation remains outside the repository; unique research code/results and dependency fingerprints are preserved here. The two-heater OLS study from the earlier turn remains separate: these are different fitting methods and data selections, with no retroactive upgrading of its claims.

For the first temperature, the returned order-two coefficients are approximately `a=(1.931478122, −0.931876179)`, `b=(−0.000835067, 0.001140576)` and `c=0.008446783`. These are numerical estimates, not exact physical constants. The negative leading input coefficient is retained rather than silently replaced by a monotone heating law. The direct recurrence reproduces returned training predictions within `3.994×10⁻⁶ °C`, a numerical difference that is reported rather than erased.

## Reconstructed candidate generation and corrected comparison

[Numerical search](../../../../experiments/integrated-correction/general-framework/generative-basis/inquiry-correspondence/analyze_tuning.py) · [complete grid scores and selected trajectories](../../../../experiments/integrated-correction/general-framework/generative-basis/inquiry-correspondence/tuning-results.json).

The source supplies a finite grid: both gains range from 5 through 80 in increments of 5, giving 256 candidates. Its order and last-tie rule are retained. Each candidate uses the already examined PI rule, retained integral and saturation logic. Its latent ARX temperature evolves without the fitted output residual; that residual is added to the readout delivered to the controller. It is not accidentally fed back into the latent ARX state as a process disturbance.

For the same 599 positions, the source sums absolute tracking loss and half the **signed** command movement. The corrected comparison uses half the **absolute** movement. Both divide by 599. These weights and targets are supplied engineering choices; they neither express G0 nor exhaust affected living claims.

| Model/timing contract | Signed-objective winner `(Kc,tauI)` | Absolute-objective winner | Corrected cost of corrected winner | Corrected excess from signed selection |
|---|---|---|---:|---:|
| Archived residual transfer, one-second PI interval | (10,55) | (10,55) | 5.606797 | 0 |
| Same residual, recorded intervals in PI | (10,55) | (10,55) | 5.606948 | 0 |
| No transferred residual | (25,80) | (10,60) | 5.553658 | 0.297542 |
| Compensated input gain ×0.8 | (10,50) | (10,50) | 5.529762 | 0 |
| Compensated input gain ×1.0 | (10,55) | (10,55) | 5.606797 | 0 |
| Compensated input gain ×1.2 | (20,80) | (5,80) | 5.606449 | 0.269610 |

This is **1,536 numerical candidate simulations**, not observed outcomes of 1,536 physical interventions. Six model contracts are not six independent estimates of the true plant. The ±20% gain changes are an explicit sensitivity construction, not an empirically calibrated uncertainty set. The residual-free case is an ablation; unlike the compensated family it does not exactly reconstruct the initial observations.

The recorded-interval variant changes the PI integral's interval while retaining the discrete ARX event model. It is not a variable-step physical discretization. The fitting run took about 5.27 seconds on the current host. That is an observed computational duration, not a worst-case bound or a measurement of the historical controller's end-to-end latency; source tuning was an offline procedure. No one-second deadline guarantee is inferred.

### Direct recurrence versus actual GEKKO runtime

[Runtime cross-check](../../../../experiments/integrated-correction/general-framework/generative-basis/inquiry-correspondence/check_tuning_runtime.py) · [retained full trajectories and receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/inquiry-correspondence/tuning-runtime-checks.json).

All 599 loop iterations were also advanced through GEKKO's actual ARX object for the four leading source-contract candidates `(10,50)`, `(10,55)`, `(10,60)` and `(10,65)`: 2,396 numerical solver steps plus initialization. Both runtime objectives retain `(10,55)` as the best of those four. The largest command difference against the direct recurrence is below `5.69×10⁻⁵` percentage points, and temperature difference below `4.62×10⁻⁶ °C`. The corrected winning runtime cost is 5.606796078 versus 5.607409757 for the nearest checked competitor. The remaining grid uses the disclosed recurrence; no claim of a full 256-candidate GEKKO runtime replay or a formal floating-program refinement is made.

## Why fitting the original record does not establish transfer

For each scaled input-gain model, we compute its output on the **original input history**, then retain the difference between that output and the observed temperature as its correction. Every such corrected model agrees with the original record. On a changed input history, however, the latent model's response changes with its input gain while its retained original correction does not.

The new Lean result follows the actual second-order recurrence, with the same initial values. It proves that the response difference between two input histories scales with the gain multiplier. Consequently the corrected prediction equals the original observation plus that scaled input-history effect. Two distinct gain multipliers disagree wherever that effect is nonzero, even though their corrected original records agree exactly.

This is a constructive nonidentification result in the disclosed model class, not a free toggle of a truth predicate and not a refutation of the fuller physical account. Additional heat-transfer evidence, disturbance constraints or interventions could distinguish the alternatives. Conversely, reproducing the original data by construction cannot provide that missing distinction. The candidate gain multipliers themselves are not established as physically admissible merely because the algebra allows them.

The numerical family uses the same two-lag model and initial training values; its exactly compensated members have zero reported training reconstruction error. The source-contract residual instead uses GEKKO's rounded returned predictions, explaining the small nonzero direct-recurrence discrepancy. Neither construction converts a fit residual into a known exogenous disturbance.

## Separate physical validation and a failed explanatory repair

The fitted coefficients are held fixed. Each validation trajectory is predicted using only its first two measured temperatures and its actual recorded commands; later measured temperatures enter the error assessment, not the recurrence. These are free output predictions conditional on known input records, not forecasts made before those inputs existed. The absolute fitted intercept is initially retained. No validation coefficients or model orders are tuned.

| Physical record | RMSE without transferred residual | RMSE after original residual transfer | Maximum error after transfer |
|---|---:|---:|---:|
| First validation | 0.255123°C | 0.295365°C | 0.869101°C |
| Second validation | 1.950707°C | 1.956103°C | 3.499902°C |

Residual transfer raises RMSE in both records. It slightly lowers MAE in the second, so it is not described as worsening every metric. These mismatches do not isolate a unique cause or prove that an output-disturbance model can never be useful. They do reject treating this transferred sequence as an exact correction for both inspected continuations. A residual maximum is still not a future error certificate.

A [post-hoc initial-reference diagnostic](../../../../experiments/integrated-correction/general-framework/generative-basis/inquiry-correspondence/tuning-reference-check.json), preserved with its [runner](../../../../experiments/integrated-correction/general-framework/generative-basis/inquiry-correspondence/check_initial_reference.py), tests whether shifting the equilibrium intercept according to the changed initial reading repairs the discrepancy. It improves the second run's residual-free RMSE to 1.707938°C but worsens the first to 1.056396°C. The initial reading is not certified ambient temperature. This failed general repair is retained, with its post-hoc status, rather than adopting the adjustment only where it helps.

## Checked composition into comparison and protection

[TuningCorrespondence.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/systems-complexity/analysis/TuningCorrespondence.lean) · [source-bound checker](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/systems-complexity/analysis/check_tuning_correspondence.py) · [successful receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/systems-complexity/analysis/tuning-correspondence-verification.json).

**10 new theorems / 14 declarations pass; 228 declaration audits across eight repository modules.** All imports are freshly rebuilt; pinned Mathlib cache and standard logical dependencies are disclosed. No proof hole, custom axiom, unchecked decision procedure or unsafe bypass is present. Numerical fitting and floating simulation remain distinct from exact Lean proofs.

| Checked result | Actual producer/consumer connection and remaining inputs |
|---|---|
| `tracking_error`, `objective_error` | Consumes the preceding exposure/movement results to carry temperature and command radii into the whole tracking-plus-movement objective. Common targets, horizon and weights explicit. The formal objective is the total; the numerical search divides every total by the same positive sample count. |
| `finite_model_minimum` | Directly consumes `PracticalJudgment.finite_frontier` under the stated scalar engineering order. Finite nonempty menu supplied; no global optimum or physical feasibility inferred. |
| `estimated_minimum_actual_regret` | An estimated winner is within the sum of its and a competitor's warranted error radii in actual cost. The radii are not proved by retrospective fitting. |
| `separated_model_comparison` | Directly uses the earlier interval-separation theorem. Only sufficiently separated warranted intervals certify strict comparison. |
| `arx_input_difference_scales`, `every_corrected_model_fits_record`, `corrected_arx_response`, `fitted_record_does_not_identify_transfer` | Derives the original-record equivalence and changed-input disagreement through a coherent two-lag law. Additional physical admissibility is not smuggled into “fit.” |
| `calibrated_protection_at_actual` | Combines the existing `Robust` actual-case theorem with indexed protected-condition margins. Actual-case inclusion and every relevant calibration remain required; a scalar engineering cost does not establish them. |

The three levels are now explicitly connected: a finite data-derived response procedure, a checked contract carrying trajectory error into comparison, and physical evidence testing the procedure's assumptions. The outcome is partly affirmative and partly restrictive. The selected gains survive the metric correction in the reconstructed source case; a future practical guarantee does not survive merely pointing to a good historical fit.

## Substantive counterreview and completion scope

**Have we disproved the published improvement?** No. Its actual recorded improvement remains supported. This reproduction recovers the same gains under both objective definitions. The source discrepancy changes many comparisons, but an inference that its reported choice must therefore be wrong would be unsupported.

**Did the response alternatives arise by an actual procedure?** Yes at this finite offline computational scope: the source grid is enumerated, the fitted recurrence supplies the consequences, and both disclosed metrics rank them. The grid bounds, step, model class, objective and available hardware remain supplied. This is not a derivation of every possible response or all reasonable inquiry schedules.

**Does fitting and grid enumeration prove physical optimality?** No. Modern fitting is numerical and local; a finite grid is incomplete; the transfer law and correspondence may fail; timing and actuator realizability require their actual contracts. Full runtime validation is four candidates, not the whole grid. These are material limits, not permission to relabel model values as observations.

**Does uncertainty defeat every practical conclusion?** No. The actual-case and separated-margin results give explicit sufficient conditions. The failure is claiming those conditions from evidence that does not warrant them. Practical comparison must retain actual burdens, deadlines and the independently defended G0/J application premises. Refusal to certify a particular optimum is not a proof that inquiry, action or care is impossible.

The governing [completion audit](THREE-CONNECTIONS-COMPLETION-AUDIT.md) remains active. This round resolves the source metric discrepancy's effect in the reproduced case and explains/test-restricts a supplied policy-generation premise. The next central inference is justified model/readout domains and actual timed feasibility → warranted common response. A newly fitted maximum or an arbitrarily chosen gain range cannot silently finish that inference.


[Independent completion review](TUNING-CORRESPONDENCE-REVIEW.md) rebuilt the eight-module Lean closure, reproduced every grid score, selected trajectory and validation/diagnostic metric with a separate implementation, returned identical coefficients and predictions from a fresh local fit, and checked one full 599-step runtime candidate. It identified no required repair. This acceptance concerns the disclosed local result and its limitations; the wider goal remains active.
