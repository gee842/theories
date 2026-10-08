# Settling correspondence sensitivity

Two declared velocity approximations are evaluated on the same 20 Day 2022 cluster geometries. One assigns cell density to a spherical envelope; the other accounts for cellular material and water-filled volume while retaining the same spherical drag. Their predicted pair order differs for 33 of 190 pairs. Neither approximation is certified as the actual velocity law for these clusters.

```sh
python3 analyze_settling.py
python3 check_settling.py
```

Both scripts use only the standard library. [Analysis](analyze_settling.py) computes centered coordinate moments with exact rational decimals. [The second implementation](check_settling.py) instead uses integer sums and sums of squares, recomputes every pair ordering, checks numerical bulk-density correspondence and binds the selected Lean witness to the source. [Results](settling-results.json) record all radii, cell counts, fractions, diagnostic speeds and rankings. [Verification](verification.json) states the limited numerical scope.

[Seven Lean theorems and thirteen declaration audits](../../lean/universal-ethics/settling-verification/verification.json) check rational material accounting, sphere-score correspondence, a drag sensitivity and selected rank reversal. Run their isolated compiler check with:

```sh
python3 ../../lean/universal-ethics/settling-verification/check.py
```

The toolchain is pinned to Lean 4.29.1. Only standard `propext`, `Classical.choice` and `Quot.sound` dependencies occur. Source snapshots and logs are retained beside the receipt. These proofs do not establish the physical drag law, a measured hydrodynamic radius, observed fitness or the formation of resources.

[The integration and author self-review](../../../../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/SETTLING-CORRESPONDENCE-INTEGRATION.md) state why this is relevant to connecting development, physical sorting and descendants. The [2026 preprint](../../../../../../sources/evolutionary-selection/cedeno-perez-2026/README.md) supplies the model correspondence under examination; the [2022 data](../../../../../../sources/evolutionary-selection/day-2022/README.md) supply a separate geometry sensitivity test. They are not a combined longitudinal dataset.
