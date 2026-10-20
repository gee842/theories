# Round 2 for A1 and A3, frozen 20 October 2026

Board item MQ1. AI-written. Frozen after round 1's results and verdicts were committed (see `results/FROZEN-AT` for both commits) and before any round-2 run. Round 1's verdicts stand as frozen. This round corrects two configuration errors that round 1 exposed. The predictions, classes and pass rules of A1, A1m and A3 are unchanged ([PREDICTIONS-2026-10-20.md](PREDICTIONS-2026-10-20.md)), and nothing else is rerun.

## What went wrong in round 1

**A1 and A1m were degenerate.** The frozen start x₀ = û + m̂/2 and harvest H = 1.5Ŷ put the first harvest beyond the margin in both dilution factors: H ≥ m₀ (DF 500: H = 114,071 against m₀ = 86,080; DF 750: 79,761 against 78,676). So the break came at day 0 in every replicate of every history, by construction, before any dynamics could carry history. A1 passed and A1m failed only in that sense: the test had no power either way. A2's applicability rule (H < m₀) would have excluded these cells; A1's configuration lacked that guard.

**A3 measured a different protocol from the one stated.** The prediction reads "the point of no return under a standing harvest H". The code (`survives` with `harvest_after`) grows the culture for one day without harvest before the standing harvest begins. That one free day lets cultures started below H, even below û + H, grow back to near the stable state. All six failed cells (DF 500 and 750) have a measured point of no return below H itself, which is impossible under harvesting from day 0.

## The changes (and only these)

- **A1, A1m:** x₀ = û + 0.75 m̂ and H = 1.25 Ŷ, chosen so that H < m₀ in both dilution factors (from round 1's `measure.json`: DF 500: H = 95,059 against m₀ = 129,120; DF 750: 66,468 against 118,014). Everything else as in round 1: histories, the memory variant, 400 replicates, the KS rules.
- **A3:** the standing harvest starts on day 0 (the first cycle is harvested too: `harvest_first = H`). Everything else as in round 1: the harvests 0.25, 0.5, 0.75 × Ŷ, 200 replicates, 60 days, alive and above û on day 60, bisection, and the pass rule (point of no return > û + H in every testable cell).

The round-2 seeds are the round-1 seeds shifted by 10⁶, so no replicate is reused. Outputs go to `results/round2/`. The measurement (`measure.json`) is round 1's and is not rerun.

## Learners in test bed B: not rerun

Round 1's learner failures (B3, B4, B5, B7) were traced to H2. The tabular learners deliver 5–7.75 against the best response's 9, and do worse where the lawn state varies more. A learner round was considered and dropped after a calibration on the reference variant V0 only ([`calibrate_learners.py`](calibrate_learners.py), output [`results/round2/calibration_learners.json`](results/round2/calibration_learners.json), 6 seeds per setting, no test variant run). No setting tried (constant or visit-count step sizes, 100,000–300,000 episodes, half or most episodes with exploring starts) reached the best response. Blind learners reached 7.3–8.2 deliveries and end-coupled ones 4.7–7.2. A learner round would test the same bridge failure again, so round 1's learner verdicts stand as the B result. The `visit_power` option added to `garden.q_learn` for this calibration defaults to off, so round 1's code paths are unchanged.
