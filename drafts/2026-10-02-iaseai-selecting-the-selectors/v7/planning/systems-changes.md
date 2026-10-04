# V7 systems/alignment repairs

Edited only the assigned source files `src/core/50_s5.md`, `src/core/60_s6.md`, `src/supp/05_S5.md`, and `src/supp/06_S6.md`. Reviewed §4/S4 for propagation; no changes were needed there. Stable key declarations in all six owned source files match V6.2 exactly.

- **SYS3-01 / `masked`:** retained the valid fixed-positive-tax, fixed-sanction-bound ceiling theorem. Stated that scope in the §6 claim box, core remark and S6. When the tax changes with capability, the relevant condition is `p_det(K) F_max < c_k(K)` eventually; detection tending to zero alone is insufficient. S6 gives the decreasing-tax counterexample and a path with divergent cumulative selection. Pointwise payoff comparisons are distinguished from limiting-share conclusions; a divergent integral is a sufficient condition under cumulative selection, not claimed necessary for every such selection rule. Added the corresponding fixed-gap / changing-gap scope to `nested`.
- **SYS3-02 / `masked` → `coverage`:** S6 now matches the core's distinction between failed assurance and actual residual hazard. It requires both `(coverage lags)` and `(residual floor)`, plus `(shared failure)` for the every-actor conclusion. Added the completely masked but summable-hazard counterexample. E2/E3 remain recommendations under the protection standard when another assurance case is absent.
- **SYS3-03 / `enough`:** bounded prize value bounds contest effort at fixed costs; it does not produce finite satiation or a stopping rule. Preserved the finite-exposure result conditional on hazardous variety actually stopping, and made its per-period upper hazard bound `<1` explicit. S5 uses the original example to show the positive limiting intensity `3/16`. §5's opening proportionality claim now says linear stakes. The §6 transition to `boundedopt` uses the same distinction.

## Verification

`python3 verification/systems_checks.py`: **6 tests pass** (standard library only). Tests include fixed-tax threshold/equality, both relative rates for a moving tax, independent numerical integration of the selection gap, an integrable-gap boundary, survival with and without a residual floor under identical failed detection, numerical optimization of the bounded-prize best response, and the finite-exposure positive case when hazardous variety actually stops. No claim is validated by searching the manuscript's wording.

## Downstream propagation for the root

- Registers/front matter/table summaries of `masked` should retain either fixed positive tax or the relative tax/detection condition, and distinguish a positive evasion payoff advantage from elimination along a changing path. C9 and C12 jointly determine the moving-path ceiling.
- Summaries of `enough` should not equate a bounded objective with finite satiation. Keep the actual stopping/cap premise separate from bounded contest effort; proportional intensity uses the linear-prize contest.
- Any supplemental or register claim deriving `(coverage lags)` or a residual floor from masking alone should follow the repaired core/S6 conditional assurance reading.
- Register `verification/systems_checks.py` in the V7 verification inventory. The existing numerical examples and stable keys remain intact; the previous detection-timing, capture-certificate and topology repairs were preserved.
