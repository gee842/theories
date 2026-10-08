# Fixed exploratory plan: change bounds and stated response tolerances

8 October 2026. Saved before computing this analysis's rates or holdout outcomes. This is not external preregistration; earlier repository studies have examined these archives.

Use only the three distinct primary Summary MPC records already preserved: Physics, ARX and ANN. Preserve source bytes and verify TIMING-PROVENANCE hashes. Exclude the initialization row and ARX's known unacquired terminal row using the inspected source order. Do not count duplicate files as replication.

For each of two temperature channels and each run, split acquired observations chronologically into floor(n/2) calibration observations and the remaining test observations. Estimate a constant change-rate envelope from consecutive calibration readings: absolute temperature difference divided by recorded timestamp difference. Report both the calibration maximum and nearest-rank 95th percentile. No rate is updated after viewing test errors.

Evaluate retained-reading predictions at lags 1, 2 and 5 observations, with both endpoints wholly inside the test partition. Radius equals frozen rate times actual elapsed timestamp interval. Report interval counts, failures, coverage, maximum excess, typical radius and compatibility with the source's 0.2°C half-width. Also report a genuinely cross-record transfer: Physics calibration rates applied to the ARX and ANN test partitions. Separate this from each run's own chronological calibration. No test fit, outlier removal or choice of a winning envelope after results.

Recover the 0.2°C deadband from all three source scripts and verify its interpretation as an engineering target/slack objective, not a hard safety guarantee or true-temperature sensor calibration. Compare the sensor manufacturer's component specification at its declared grade/conditions; do not turn typical accuracy into a maximum guarantee or assume the full measurement chain meets the component specification.

Use exact decimal-rational arithmetic for analysis, then a separately implemented Decimal arithmetic cross-check on every interval and classification. Check chronological isolation by changing only test readings and confirming calibration rates stay unchanged. Preserve per-interval rows and source/code hashes. No new mathematical theorem is proposed; previous Lean results supply only their stated conditional interfaces.

These are recorded-readout changes under the original closed-loop commands, not a continuous physical derivative bound, future coverage theorem, counterfactual skip-sensing experiment, causal controller comparison or biological validation. The serial samples and overlapping horizons are dependent; report counts, not binomial confidence intervals. Complete the assessment even if all candidate guarantees fail, retaining the unmet evidence requirements explicitly.
