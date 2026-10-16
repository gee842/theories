# Empirical ecological retention

This analysis uses the [preserved Ratcliff 2013 survival table](../../../../../sources/evolutionary-selection/ratcliff-2013/README.md). It treats 30 cultures in six isolate/regime groups as the observations, retaining the one-lineage and prior-conditioning limitations in the [integration](../../../../../_process/research/2026-10-05-generative-foundation-review/history/root-foundation/ECOLOGICAL-SELECTION-INTEGRATION.md).

Run from the repository root using Python 3 and Node.js. Both scripts use only standard libraries:

```sh
python3 experiments/integrated-correction/general-framework/generative-basis/ecological-selection/analyze_survival.py
node experiments/integrated-correction/general-framework/generative-basis/ecological-selection/check_survival.mjs
```

The analysis verifies the input's published size and MD5, computes exact means and contrasts, enumerates all 252 label allocations per isolate, runs a seeded culture-level bootstrap, and compares ordinary mean predictors with balanced holdouts. The Node checker separately implements the arithmetic and holdout calculations. These are numerical empirical checks, not Lean theorems or independent biological replication.

[Results](survival-results.json) · [Verification receipt](verification.json). The source CSV is unchanged by either command. The experiment makes no network requests, assumes no row pairing, and makes no broad superiority claim. Bootstrap percentiles are exploratory with only five cultures per regime. The complete velocity/area dataset remains unavailable in this study.
