# From supplied feedback premises to physical records

8 October 2026. AI-authored continuation of the active objective: **“make sure: Compose existing results, Explain a supplied premise, Establish real-world correspondence are done.”** This report adds an actual archival correspondence study to the [existing formal connection](INQUIRY-JUDGMENT-INTEGRATION.md). It does not declare the whole objective complete.

## What is now established

The earlier inquiry/judgment construction used idealized readings, installed responses and abstract work. The present study reconstructs **measured temperature → retained integral → bounded heater command → subsequent recorded temperature** in a published physical experiment. This is a different physical realization of the common feedback relations, not a claim that the toy additive-dose law or its 1044-tick tariff describes a heater.

Three published physical runs contain **1,797 recorded samples and 1,794 subsequent issued commands**. Replaying the supplied PI equation with each recorded observation and elapsed interval reproduces every logged command in Python floating arithmetic. A separately written exact-rational implementation agrees within **7.43×10⁻¹⁴ percentage points**. The comparison keeps the original data, saturation and integral retention. It does not replay a hypothetical plant against changed actions.

**真实对应的新证据：** 三次已发表物理运行中的读数、保留的积分与实际发出命令逐项相符。时间变化、饱和、记录的命令暴露量和失败保留；这不是新做的硬件实验，也不把温控性能当成伦理价值。

## Primary sources and provenance

Park, Martin, Kelly and Hedengren, *Benchmark Temperature Microcontroller for Process Dynamics and Control*, Computers & Chemical Engineering 135 (2020), [DOI](https://doi.org/10.1016/j.compchemeng.2020.106736), supplies the physical benchmark, observations and controller code. Read author-preprint §§2, 3.1–3.5 and 4–4.1, including the device, separate model-fitting/validation experiments, controller and objective equations. The paper distinguishes physical runs from model simulation. Its sensor specifications are typical values, not deterministic worst-case certificates.

The original [author archive](https://github.com/APMonitor/arduino/blob/f36e65a70dd7122d1829883899e40e56bf6c4279/CACE_2020_source.zip) and preprint are preserved byte-for-byte under [sources/tclab-benchmark](../../../../sources/tclab-benchmark/README.md), pinned to repository revision `f36e65a70dd7122d1829883899e40e56bf6c4279`. [Provenance manifest](../../../../sources/tclab-benchmark/PROVENANCE.json) records hashes of the archive, paper and 14 selected unmodified members. Copies inside the archive and extracted members are not independent evidence. No upstream script was executed against hardware or a remote solver.

The paper supplies thermal/measuring organization and a retrospective explanation of retuning. The more specific numerical claims below come from our fresh reanalysis of its files, not from copying reported results. Publication is evidence of the claimed physical provenance; we have not independently observed those historical laboratory runs.

## Reconstructed physical correspondence

| Formal/analytical role | Actual record or source | What the correspondence establishes and excludes |
|---|---|---|
| Acquired temperature | `T1` in each physical log; source reads `a.T1` before calculating the command | Reading actually participates in command calculation. Absolute temperature truth is not measured against an independent reference here. |
| Intended engineering condition | `TSP1` changes through 50, 40 and 60 °C | A supplied experimental tracking task. It is not independently justified as a basic living claim. |
| Retained consequence | Integral update from previous retained integral, current error and recorded elapsed time | The exact sequence of retained states can be reconstructed. The integral is not an additional sensor. |
| Selected action | `Q1`; source clips output into 0–100% and withholds integral accumulation outside that interval | Commands in all three logs match. This does not certify every firmware instruction or analog PWM output. |
| Changed physical condition | Subsequent `T1` records and two separately archived validation runs | Observed closed-loop performance with changed gains. Different starting temperatures/ambient conditions prevent a randomized causal-effect claim. |
| Time | Logged wall-clock differences, not an assumed one-second grid | Actual recorded intervals range from 0.844 to 1.152 s across the runs. These are cycle intervals; they are not complete timestamped sensor-to-actuator latency measurements. |
| Support/expenditure | Commanded duty integrated over recorded intervals | Percent-seconds is an actuation-exposure proxy. Neither electrical energy nor the earlier abstract work account was measured. |

The control code has a comment saying Kelvin, while the values, targets and paper use Celsius. Interpretation follows the actual API/units and reported experiment, not that mistaken comment. No unit conversion is silently imposed.

## Reproduced measurements and a preserved discrepancy

The paper's engineering objective combines mean absolute tracking error and half the mean absolute command movement. This weighting belongs to that experiment and is not imported into G0 or J2.

| Run | Tracking error (°C, sample mean) | Absolute movement (% command, sample mean) | Combined objective | Change from initial |
|---|---:|---:|---:|---:|
| Initial gains | 5.73449 | 0.712674 | 6.090828 | — |
| Validation 1, changed gains | 5.31421 | 0.900749 | 5.764581 | 5.356% lower |
| Validation 2, same changed gains | 5.08195 | 0.952225 | 5.558066 | 8.747% lower |

This reproduces the paper's rounded 6.09→5.76 and 5.4% comparison in validation 1. The second archived validation is a separate run, not an independent laboratory replication. Both changed-gain runs have **more absolute command movement** despite their lower combined objective. Validation 1 also has higher integrated command exposure than the initial run; a lower tracking objective does not imply uniformly lower burden or resource use.

The preserved optimizer source instead contains `mv_obj += Q1[i]-Q1[i-1]`. That sums **signed** changes. Its later objective expression therefore does not implement the paper's absolute movement penalty. The signed sum only depends on the final minus initial command; large reversals can cancel. We preserve the source and disagreement. The observed improvement is reproducible, but the archive does not certify that its search chose a minimizer of the stated objective. No corrected simulated optimum is presented as physically tested.

An inspected but unused multivariate MPC log has a terminal row whose temperatures revert to initialization values while commands/targets continue. This round does not silently clean or use that file as validation; the selected PID files instead undergo complete controller replay. This is a provenance selection, not deletion of an inconvenient observation from the analyzed runs.

## Explaining the supplied action-error premise

The earlier [action-sensitive scale theorem](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/systems-complexity/analysis/EmbodiedChoiceScales.lean) required a bound on the consequence of changed action. Here an actual mechanism replaces an arbitrary command discrepancy: a PI response computes a raw command from acquired error and retained integral, then clips it to the actuator range.

For the same target and elapsed interval, the new checked theorem derives

\[
|u-u'|\le |K_P+K_I\Delta t|\,E+M,
\]

where `E` bounds the difference between readings and `M` bounds the difference between retained integrals. Clipping does not enlarge this difference. The parameters correspond to the actual archived controller; the empirical replay tests that correspondence. The observed code includes a nonaccumulating integral when the raw command saturates. The real-valued Lean abstraction proves both command bounds and that retention behavior.

This explains a formerly supplied action-error term through actual organization and recorded variables. It **does not derive sensor truth, retained-memory accuracy, thermal response sensitivity or future disturbance bounds**. Those are separate inputs. Given physical response sensitivity `B`, the proved command bound supplies the earlier scale theorem's action-effect term. A second theorem composes such terms through its existing finite-horizon error recurrence.

**前提解释的实质：** 原先给定的“行动差异”被展开为取得读数、历史积分、实际增益、时距与执行器饱和的关系。读数及记忆本身的误差、热响应敏感度和外来扰动仍需独立支持。把上层前提细化，不等于所有下层前提已经消失。

## Held-out prediction tests and actual failures

Two further physical-data files contain 600 records each, with different two-heater excitation schedules. We fit a fixed order-two ordinary least-squares ARX family on the designated initial file and evaluate all 598 eligible indices of the separate validation file. The model order comes from the authors' example; parameters are not tuned on the validation file. This is our numerical comparison, not a reproduction of the authors' GEKKO prediction-error fit. Initial-file index times are nominal seconds, not measured cycle timing.

| Forecast family | Held-out one-step RMSE (°C) | Free rollout RMSE (°C) |
|---|---:|---:|
| T1, first heater only | 0.22370 | 5.93346 |
| T1, both heater inputs | 0.22346 | 5.77756 |
| T2, first heater only | 0.19409 | 8.19073 |
| T2, both heater inputs | 0.16886 | 3.93389 |

One-step prediction receives the preceding measured temperatures. Free rollout receives only the first two temperatures and the recorded input schedule; subsequent temperatures are generated by its own recurrence. Reporting the former as an open-loop guarantee would conflate these information conditions. Including the second heater substantially improves T2 rollout in this comparison, consistent with the physical coupling account; it does not establish unique explanatory superiority over conventional systems theory.

For both T1 models, the maximum absolute training residual is exceeded at **two held-out indices**. All records, including those failures, are retained. The T2 models have zero such exceedances in this file; that is still not proof of a universal future bound. The standard-library arithmetic checker below covers controller replay and metrics. The subsequent independent agent review refits all four regressions with a separately written Householder QR solver using the standard library, rather than NumPy/SVD: coefficient differences are at most 4.76×10⁻¹⁴ and the reported metrics agree. The T1 bound exceedances remain at original indices 37 and 38. The numerical disagreement from solver rounding is reported, not treated as a new empirical uncertainty estimate.

## Lean verification and numerical evidence

- [New Lean source](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/systems-complexity/analysis/MeasuredFeedback.lean): **13 new theorems / 26 explicit declarations**, with **147 audits across the five-module source closure**. Fresh Lean 4.30.0-rc2 build passed without warnings. The earlier action-sensitive scale theorem is imported and used, not restated as an unrelated success predicate.
- [Proof receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/systems-complexity/analysis/measured-feedback-verification.json) and [reproducible checker](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/systems-complexity/analysis/check_measured_feedback.py) freeze current sources and rebuild all repository imports. Standard `propext`, `Classical.choice`, `Quot.sound` only; no new axioms or proof holes. Pinned Mathlib cache is reused and the executable hash is not a complete linked-runtime attestation.
- [Numerical producer](../../../../experiments/integrated-correction/general-framework/generative-basis/inquiry-correspondence/analyze_tclab.py) and [results](../../../../experiments/integrated-correction/general-framework/generative-basis/inquiry-correspondence/tclab-results.json) bind raw imports, models, failures and all metrics.
- [Separate exact-rational checker](../../../../experiments/integrated-correction/general-framework/generative-basis/inquiry-correspondence/check_tclab.py) and [receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/inquiry-correspondence/tclab-checks.json) reconstruct 1,794 commands and the engineering metrics without importing the producer or NumPy. This is an alternate implementation by the same research agent, not an independent-agent review or a second physical experiment.

The new Lean statements cover bounded commands, integral retention, command sensitivity, one-step and horizon composition, signed-sum telescoping and its exact bounded counterexample, and nonidentification from records shared by competing predictions. They formalize mathematical consequences of the model; the numerical replay separately assesses correspondence to the physical files. No verified compiler refinement from floating code to real arithmetic is claimed.

## Substantive counterreview and remaining work

A conventional feedback account explains these observations. The present theory earns a concrete correspondence and a traced premise explanation; it does not earn an exclusive discovery claim. Better weighted tracking can coexist with more movement and more support exposure. Published normal sensor behavior cannot exclude failures, and a residual maximum cannot justify discarding unseen error cases. Different trials cannot isolate every ambient cause. A historical source discrepancy requires correction or qualification, not smoothing away.

The [three-requirement completion audit](THREE-CONNECTIONS-COMPLETION-AUDIT.md) remains active. The immediate remaining work is to resolve what can be recovered from the archived policy-generation route and its movement-cost discrepancy, and carry justified uncertainty/calibration and physical timing into the practical comparison without equating tracking performance with living protection. The connected formal result, a mechanistic premise explanation and observed correspondence are now evidenced; their full integration at the governing goal's scope is not yet certified complete.

## Independent review

[Independent completion review of this addition](MEASURED-FEEDBACK-REVIEW.md) independently rebuilt all five modules and 147 audits, replayed all 1,794 commands with a separate rational-state representation, refitted all four models with Householder QR, and matched both remotely pinned original files to the preserved bytes. Its required wording repair replaces an implication of physical energy consumption with recorded command exposure. This accepts the local empirical/formal addition at its stated scope; the overall three-requirement goal remains active.
