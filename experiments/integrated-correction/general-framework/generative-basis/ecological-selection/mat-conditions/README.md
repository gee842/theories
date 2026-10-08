# Mat conditions and source correspondence

This directory checks extraction of published oxygen-condition summaries for the [mat development study](../../../../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/MAT-CONDITIONS-INTEGRATION.md). It adds no simulated cultures or fitted survival model.

From the repository root:

```sh
python3 experiments/integrated-correction/general-framework/generative-basis/ecological-selection/mat-conditions/read_evidence.py
python3 experiments/integrated-correction/general-framework/generative-basis/ecological-selection/mat-conditions/check_evidence.py
```

`growth-summary.csv` contains eight **reported summaries**, not eight individual observations. `oxygen-summary.json` retains the two competitive-fitness summaries, their comparator and sample size. Fitness here is a ratio of logarithmic cell-count increases; it cannot be inserted as a phase-survival probability. Table growth compares SBW25 and WS; competition compares WS and SM-13. These distinct comparators are retained.

`verification.json` binds the unchanged source, extraction code and outputs. The checker uses a separate table extraction plus manually read values, checks condition ordering and labels, and preserves reported standard errors and grouping letters. It verifies transcription and correspondence, not the authors' statistical analyses. No new theorem is claimed, so there is no new Lean proof package.

The mechanical-interaction paper has a separate [link-only reading record](../../../../../../sources/evolutionary-selection/spiers-2005/README.md); it supplies qualitative constraints, not additional raw numerical rows.

`inspect_supplement.py` accepts the separately downloaded Doulcier Figshare ZIP as its argument, checks its published MD5, compares all common members against the preserved Zenodo archive, and inventories the extra exported-analysis bundle. The [inspection record](../../../../../../sources/evolutionary-selection/doulcier-2025/supplement/archive-comparison.json) keeps the four lineage tables' phase-index correspondence explicit. Neither their retrospective estimates nor their processed row counts replace the earlier raw data or chronological predictions.
