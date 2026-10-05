# Repeated RNA renewal: source preservation and exact identification witnesses

This new read-only check supports [RNA-REPEATED-RENEWAL-EVIDENCE.md](../../../_process/research/2026-10-05-support-and-shared-generativity/completion/RNA-REPEATED-RENEWAL-EVIDENCE.md). It is neither a simulation nor a reanalysis of published image intensities.

`check.py` verifies all 11 original source files against the new source manifest, compares every pre-existing Source 24 file and nine named frozen physical-evidence notes to commit `e214ecf`, and checks the same bytes again before writing its own result. It also checks, using exact fractions, the small covariance witness and the stationary two-state kernels with different repeated-path probabilities. The original notebooks are never executed; large processed pickle files are never deserialized. No previous scientific calculation is rerun.

Run from the repository root with Python 3:

```
python3 experiments/shared-renewal-capability/rna-repeated-renewal/check.py
```

The saved [check.json](check.json) records the producer and manifest hashes, each verified source hash/size, frozen-file comparisons and exact algebraic values. The mixing bands and sample sizes in the note were manually transcribed from visually inspected primary PDF pages; this check does not falsely certify automated extraction or a statistical confidence interval. The source manifest separately records exact pinned addresses and hashes of large available-but-unused payloads.
