# Predictive calibration: fixed exploratory comparison

8 October 2026. Written before fitting this comparison. These archives have already been examined; this is exploratory reanalysis, not new preregistered replication.

Question: can a conventional dynamics-based forecast reduce the uncertainty of a retained-reading predictor, and does retaining the other thermal channel improve on a local description of equal size?

Use the three distinct Summary MPC records in TIMING-PROVENANCE, excluding the initialization row and unacquired ARX terminal row as in the previous bound analysis. Split acquired rows chronologically at floor(n/2) and floor(3n/4): fitting / residual calibration / testing. Every target must lie within its origin's partition. Past features may precede that partition, since they are available at the origin. Use origins with at least three preceding acquired observations.

Predict the increment in each temperature over 1, 2 and 5 observation steps, directly from origin features. Never use future timestamps, commands, setpoints or readouts as predictor inputs. Report elapsed time only retrospectively. All command features use at least the previous row, respecting both immediate and queued source implementations. The logged command is not measured delivered power.

Five fixed predictors:

- persistence: zero increment;
- trend: horizon times the latest one-step readout increment;
- local3: own current temperature, latest increment, previous own command;
- local6: own current temperature, latest and preceding increment, own commands at lags 1, 2 and 3;
- coupled6: own and other current temperatures, each latest increment, own and other commands at lag 1.

Fit the last three by ridge regression on fitting rows only, with training-mean/standard-deviation feature scaling, intercept unpenalized, and fixed coefficient penalty 1. Use augmented least squares; do not tune on calibration or test outcomes. Preserve all models. Compare local6 and coupled6 as equal-parameter descriptions; neither is a privileged theoretical implementation.

Calibrate each model/horizon/channel separately on the middle partition: constant symmetric radii given by the maximum and nearest-rank 95th percentile of absolute forecast residuals. Freeze both before testing the last partition. Report MAE, RMSE, largest error, empirical coverage, exceedance magnitude, and compatibility of radius with the chosen 0.2°C target half-width. No hard future guarantee or exchangeability-based coverage theorem is claimed.

Report within-run comparisons and Physics-to-ANN transfer of the entire frozen model, scaler and residual envelope. These two sources have approximately two-second cycles; cadence still varies. Do not transfer to ARX's approximately one-second cadence as if a step meant the same time. No fitted target-run adjustment on transfer. Preserve all elapsed times and test failures.

Save per-prediction values, coefficients, partitions, source/code/plan hashes and grouped results. Cross-check with separately implemented 60-digit Decimal normal-equation solves and raw-source feature construction; do not import the producer. Check data isolation by perturbing observations beyond fitting and calibration boundaries. Check that deleting the future of a forecast origin leaves its prediction unchanged. These are numerical/data-flow checks, not Lean proof claims.

Scope: observational forecasting under the originally executed closed-loop commands. Better prediction is neither identified causal coupling nor evidence that changing sensing or actuation would retain the same physical history. These data do not establish true-temperature calibration, an ethical tolerance or the missing joint biological loop.

Numerical amendment after the first computation, before the separate cross-check: classify threshold equality with 1e-10°C tolerance to avoid machine-rounding changes in decimal readout ties. Keep unadjusted errors, radii and excess magnitudes. This disclosed numerical convention is not an empirically estimated error allowance or a repaired physical bound. No model, split or envelope choice is changed.
