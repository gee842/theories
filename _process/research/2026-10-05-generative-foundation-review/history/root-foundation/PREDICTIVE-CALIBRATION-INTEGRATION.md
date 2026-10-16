# Retained dynamics, coupled descriptions and predictive uncertainty

8 October 2026. AI-authored continuation of Ren's “continue empirical validation” direction, preserved in the [conversation record](../../../../sources/15-codex-theory-conversations/2026-10-08-relations-across-scales.md). This extends the [actual-bound test](BOUND-CALIBRATION-INTEGRATION.md), where retaining the last reading produced intervals too wide for the chosen target. It reuses physical archives; it is not new laboratory replication.

**Result:** retaining local dynamics improves test RMSE over retaining the latest reading in all 18 within-run channel/horizon comparisons. The equally sized coupled-channel model loses to the local-history model in all 18 comparisons. Some residual-percentile intervals become narrower than ±0.2°C, but each such interval has later misses. Better prediction is established at this fixed empirical scope; a reliable narrow certificate is not.

**中文结论：** 动态历史确实改善了本次留出预测；同样参数数目的跨通道描述却没有自动胜出。细节是否值得保留，需要实际比较它在当前问题中携带的关系。预测平均误差改善，不等于误差界已经可靠；窄区间的真实失败继续保留。完整生物联合验证仍按独立的原目标推进。

## 1. The relation being tested

The connection is retained effects → prediction at a later horizon → warranted uncertainty for possible response. Heating, local temperature changes, inter-unit exchange, sensing, remembered commands and feedback computation remain relations within one thermal history. A local predictor can carry effects of coupling through its own recent history; omitting a separate other-channel coordinate does not posit an ontologically isolated subsystem.

This is a comparison among ordinary forecasting methods. It tests how the theory should judge the adequacy of a description. It neither establishes exclusive necessity of the theory's vocabulary nor derives normative warrant from prediction accuracy. Practical arguments still require the target's justification and actual consequence correspondence.

## 2. Design fixed before fitting

The [saved exploratory plan](../../../../experiments/integrated-correction/general-framework/generative-basis/inquiry-correspondence/PREDICTIVE-CALIBRATION-PLAN.md) specifies every model, split, penalty and horizon before this comparison's fits. Earlier rounds examined the same archives, so the final partition is isolated from this fit, not historically unseen by the research programme.

The three distinct Summary MPC records retain 299 Physics, 599 ARX and 299 ANN acquired rows after source-grounded exclusions. Split at floor(n/2) and floor(3n/4): Physics/ANN use 149 fitting, 75 calibration and 75 testing observations; ARX uses 299/150/150. Origins have three earlier acquired observations. Targets stay inside their origin's partition; past inputs may precede it. No duplicate file counts as another run.

Direct forecasts predict readout increments at 1, 2 and 5 observation steps. Every predictor input is available by the origin: no future reading, timestamp, command or setpoint is used. Command features are at least one logged row old, respecting the archived immediate/queued execution differences. Actual elapsed times are reported retrospectively, not supplied to predictions. Approximately one-second ARX steps differ from the approximately two-second Physics/ANN steps; step counts are not a universal physical deadline.

| Fixed predictor | Information retained |
|---|---|
| Persistence | Current reading; zero predicted increment |
| Trend | Current reading and latest one-step increment |
| Local3 | Own temperature, latest increment, previous own command |
| Local6 | Own temperature, latest and preceding increments, three previous own commands |
| Coupled6 | Both current temperatures, both latest increments, both previous commands |

The last three use ridge regression with an unpenalized intercept, fitting-only mean/standard-deviation scaling and fixed penalty 1. Local6 and Coupled6 each have six slopes and an intercept. Their comparison reallocates finite description capacity between longer local history and other-channel information; it does **not** add coupling while holding every local-history feature fixed. Local3/Coupled6 is a separate nested-information comparison, with unequal parameter counts. All five models are retained; no test-selected winner is refitted.

For each model, channel and horizon, the middle partition supplies maximum and nearest-rank 95th-percentile absolute residual radii. Both freeze before the final partition is evaluated. Physics-to-ANN transfer freezes the entire Physics model, scaler and radius; no target-run correction is fitted. Between-run calendar order is unknown. No ARX transfer treats its different cadence as equivalent.

## 3. Forecast outcomes and adverse comparisons

One-step held-out RMSE, °C:

| Run | Channel | Persistence | Trend | Local3 | Local6 | Coupled6 |
|---|---|---:|---:|---:|---:|---:|
| Physics | T1 | 0.336024 | 0.109365 | 0.124787 | **0.098523** | 0.155438 |
| Physics | T2 | 0.156538 | 0.158843 | 0.190763 | **0.137183** | 0.319392 |
| ARX | T1 | 0.191886 | 0.171582 | 0.148668 | **0.127611** | 0.154911 |
| ARX | T2 | 0.157659 | 0.236789 | 0.154072 | **0.151420** | 0.198004 |
| ANN | T1 | 0.347388 | 0.130886 | 0.136154 | **0.090617** | 0.156293 |
| ANN | T2 | 0.157887 | 0.170567 | 0.169577 | **0.126468** | 0.223746 |

Local6 also beats persistence and Coupled6 at both longer horizons in each run/channel: 18/18 comparisons against each. These share runs, channels and overlapping horizons; they are not 18 independent replications or a significance test. Trend can worsen T2 prediction, and Local3 also loses to persistence in some cases. A more elaborate description is not uniformly better.

The result changes the earlier pessimistic precision picture: a simple conventional history model materially reduces forecast error. It also constrains a possible overreading of relationality: explicitly including a second channel is not automatically the best finite description. Short records, transient covariate changes, regularization and feature allocation may affect this outcome; no isolated causal explanation of the ranking is established.

![Held-out error ratios](../../../../experiments/integrated-correction/general-framework/generative-basis/inquiry-correspondence/predictive-calibration-comparison.png)

## 4. Narrower intervals still fail

Only the following three model/transfer/horizon groups produce a calibrated radius at most 0.2°C, all using the 95th percentile:

| Fit → test | Channel / model / lag | Radius, °C | Test misses | Empirical coverage |
|---|---|---:|---:|---:|
| Physics → Physics | T1 / Local6 / 1 | 0.189626 | 6/74 | 91.89% |
| ANN → ANN | T1 / Local6 / 1 | 0.199301 | 5/74 | 93.24% |
| Physics → ANN | T1 / Local6 / 1 | 0.189626 | 6/74 | 91.89% |

No maximum-residual radius fits the target half-width. The Physics Local6 one-step maximum radius is 0.243548°C and is exceeded by 2/74 later Physics observations; it is also exceeded by 2/74 transferred ANN observations. Physics-to-ANN Local6 T1 RMSE is 0.094564°C, close to ANN's locally fitted 0.090617°C, but useful point prediction does not certify its radius. For T2, the transferred Coupled6 maximum envelope has 2/74 misses even though its radius is 0.528360°C.

The target width remains the archived controller's **soft final setpoint objective**, as established in the [previous source assessment](BOUND-CALIBRATION-INTEGRATION.md#4-primary-source-assessment-what-the-target-means). A narrow prediction-error interval is only a precision comparison. It need not be centered at the target, correspond to true temperature, or admit a physically realizable corrective command. No practical response certificate is inferred here.

## 5. Computation and correspondence checks

[Producer](../../../../experiments/integrated-correction/general-framework/generative-basis/inquiry-correspondence/analyze_predictive_calibration.py) · [frozen fits, radii and results](../../../../experiments/integrated-correction/general-framework/generative-basis/inquiry-correspondence/predictive-calibration-results.json) · [all forecasts](../../../../experiments/integrated-correction/general-framework/generative-basis/inquiry-correspondence/predictive-calibration-predictions.csv) · [separate checker](../../../../experiments/integrated-correction/general-framework/generative-basis/inquiry-correspondence/check_predictive_calibration.py) · [passing receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/inquiry-correspondence/predictive-calibration-checks.json).

The NumPy augmented-least-squares implementation makes **10,930 forecasts in 120 groups**, with 90 model/channel/horizon records including 54 ridge fits. A separately written 60-digit Decimal implementation parses original decimal values, constructs features, solves normal equations and reconstructs every forecast, calibration radius and grouped metric. Maximum numerical disagreement is below **1.15×10⁻¹³**. Uniqueness, all expected groups and counts, source hashes and 270 data-isolation assertions pass. Isolation includes perturbing all post-fit rows, perturbing post-calibration rows and deleting the future of a forecast origin.

A numerical convention was explicitly appended to the plan after the first calculation and before cross-checking: threshold equality allows 10⁻¹⁰°C rounding tolerance. Sixty error/radius comparisons fall within that neighborhood. Unadjusted errors, radii and excess magnitudes remain saved; this is not a physical allowance or post-test enlargement of the empirical envelope. Source decimals themselves have finite measurement precision. The separate implementation is by the same agent, not independent-agent review. No new theorem is claimed or unchanged Lean proof rerun.

Run the producer with Python and NumPy, and the checker with standard-library Python. The results record the NumPy version and all source/code hashes. [Plot source](../../../../experiments/integrated-correction/general-framework/generative-basis/inquiry-correspondence/plot_predictive_calibration.py) generates the PNG and [standalone SVG](../../../../experiments/integrated-correction/general-framework/generative-basis/inquiry-correspondence/predictive-calibration-comparison.svg) using Matplotlib; temporary dependency installations are outside the repository. An initial producer attempt lacked NumPy and produced no results; rerunning in the bundled numerical runtime succeeded. The plot similarly required a temporary plotting environment. These environment repairs did not change model selection.

## 6. Counterreview, biological continuity and the next test

The strongest rival is conventional temporal modeling with appropriate retained information; here it supplies the successful model. Closed-loop observational regressions do not isolate heater effects or identify what would occur under different future commands. A forecast at each new origin uses actual available readings, so this is neither a free-running simulation initialized once nor a skipped-sensing experiment. The coefficients are predictive, not identified thermal constants. Repeated origins and different horizons are dependent; no unsupported coverage theorem, p-value or population guarantee is attached.

The fixed quarter-based calibration is a stronger separation of parameter fitting and residual estimation than using training residuals. It still uses one calibration segment per run, and distribution changes remain. Previously examining these archives also limits confirmatory strength. Further tuning on this test partition would need a new evaluation set before claiming confirmation.

Concurrent [biological evidence integration](BIOLOGICAL-RENEWAL-INTEGRATION.md) now provides a held-out fluorescence/viable-count correspondence and finite activity–bacterial-growth–later-population evidence in distinct preparations. Credit those advances; do not repeat the earlier claim that finite ecological return is wholly unsupported. Their full joint validation remains specified in [the biological measurement document](BIOLOGICAL-JOINT-VALIDATION.md). Temperature forecasts do not complete it or transport their numerical error bounds to it.

**Completion scope:** this fixed predictive comparison, separate numerical reconstruction and theoretical integration are complete. The resulting empirical refinement is that retained local dynamics can improve prediction while uncertainty transport remains a separate, failure-prone relation. The next discriminating evidence is independently acquired runs under declared changed conditions, with actual unit-level calibration and timing, and the linked biological measurements already specified. These new observations are not available in this workspace. Existing records can support exploratory model development; they cannot become new replication by repeatedly changing the split.
