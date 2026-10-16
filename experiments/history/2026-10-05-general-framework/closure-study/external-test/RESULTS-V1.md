# External microbial prediction test: mixed primary evidence

5 October 2026. This is an actual analysis of independent experimental measurements, not a synthetic demonstration. Its findings are preliminary and narrow. **The prespecified primary comparison improves RMSE but slightly worsens MAE; it therefore does not supply the hoped-for consistent primary confirmation.** A prespecified source-holdout sensitivity gives stronger positive results. Neither test validates the complete proposed theory.

## Data and provenance

The source is Huisman, Dal Bello and Gore, [*Predictable shifts in microbial species composition lead to community-wide robustness to environmental stress*](https://www.nature.com/articles/s41564-026-02422-3), Nature Microbiology (2026), and the [authors' public data and code](https://github.com/JSHuisman/salinity/tree/f14abee9d5e2d015deead102c04ea4d3030a5788). Four natural source inocula were propagated at three salinities and two temperatures, with three replicate communities per condition. The experiment included repeated growth and dilution; this test does not measure response to a newly imposed shock.

The [protocol](PROTOCOL.md) was frozen before examining numerical biomass, mean copy number or diversity values. The paper and headline results were already known, so this is **post-selection exploratory secondary analysis**, not preregistration or a blind confirmation. [Provenance](data/provenance.json) records the pinned commit, file hashes and original protocol hash. The analysis made no outcome-driven change to the endpoint, predictors, folds or regularization.

The biomass CSV lacks replicate identifiers. We therefore averaged all three replicates within each source × salinity × temperature × cycle; we did not invent an individual biomass–sequencing pairing. Background subtraction follows the authors' published preprocessing. There are 24 condition trajectories and 72 matched current/next-cycle rows, with no missing matches or exclusions. Current cycles 1, 3 and 5 predict measured OD600 at cycles 2, 4 and 6. The authors' contaminated cycle 7 and unused cycle 8 are excluded.

Predictors are current biomass and experimental context, with or without current mean 16S copy number and Shannon diversity. Mean copy number is a composition summary, not a direct measurement of resource renewal. The target is independently measured OD600; the authors' composition-weighted computed growth rate is not used. Every fold keeps a complete experimental condition, or source, together. Scaling and ridge fitting use training rows only.

## Prespecified comparisons

All numbers below are out-of-fold errors in background-corrected OD600 units; smaller is better. Ridge alpha=1 is primary. Source-holdout is a different, prespecified sensitivity, not a replacement primary endpoint.

| Evaluation | Baseline RMSE | + Composition RMSE | Baseline MAE | + Composition MAE |
|---|---:|---:|---:|---:|
| Hold out each complete condition trajectory | 0.09369 | 0.08688 | 0.06868 | 0.06895 |
| Hold out each source inoculum | 0.09350 | 0.07751 | 0.06833 | 0.06000 |

For condition-holdout, RMSE falls 7.3%, while MAE worsens by 0.00027. Fourteen of 24 conditions improve in squared error. The descriptive source-block bootstrap 95% interval for RMSE gain is −0.00597 to 0.01628, crossing zero. With only four source blocks, this interval is coarse and is not reliable population-level significance evidence. The primary result suggests fewer large errors, not consistently lower error by both registered measures.

For source-holdout, RMSE falls 17.1% and MAE falls 12.2%. Sixteen of 24 condition groups improve in squared error. All four source RMSEs improve; Estuary MAE worsens. Its coarse source-block interval for RMSE gain is 0.00311 to 0.02540. It does not establish generality across independently sampled ecological systems.

| Source held out | Baseline RMSE | + Composition RMSE | Baseline MAE | + Composition MAE |
|---|---:|---:|---:|---:|
| Brackish / `charles` | 0.14072 | 0.11445 | 0.10779 | 0.09781 |
| Marine 2 / `fucus` | 0.06584 | 0.06154 | 0.05509 | 0.05254 |
| Estuary / `ica` | 0.06408 | 0.06216 | 0.04185 | 0.04459 |
| Marine 1 / `nahant` | 0.08201 | 0.05729 | 0.06858 | 0.04505 |

The persistence predictor, next biomass equal to current biomass, has RMSE 0.12121 and MAE 0.07667 on these rows. The informative baseline is already substantially better, making composition's additional contribution the relevant comparison.

## Sensitivities and negative controls

The prespecified alpha=10 sensitivity improves both measures in both split schemes: condition-holdout RMSE 0.08994 → 0.08266 and MAE 0.06535 → 0.06237; source-holdout RMSE 0.08914 → 0.07524 and MAE 0.06519 → 0.05656. This favorable sensitivity cannot erase the primary MAE result.

The fixed feature ablations show that adding mean copy number alone gives condition-holdout RMSE 0.08513 and MAE 0.06701; Shannon alone gives 0.09284 and 0.06978. The best ablation is not retrospectively promoted to the primary model.

Among 100 matched-size nuisance-feature controls, one beats the composition model's primary condition-holdout RMSE, while none beats its source-holdout RMSE. Their median RMSEs are 0.09498 and 0.09421 respectively. These controls test the convenience of adding two arbitrary features under this model; their counts are **not causal permutation-test p-values**, and they do not establish a biological mechanism. All control results, both regularization settings and ablations are retained in [analysis.json](results/analysis.json).

## What this does and does not establish

This analysis provides some external predictive evidence that measured composition can carry information beyond current biomass and recorded environmental conditions in this dataset. Its primary result is mixed; the source-holdout sensitivity is more favorable. It does not demonstrate a causal composition-to-regeneration edge, a feedback loop, a successor mechanism, self-maintaining correction, goal formation, universal attractors, or transfer to institutional and AI systems.

The 24 condition trajectories share four inocula and temperature-specific experimental conditions. They are not 24 independent samples from ecosystems. Aggregation suppresses replicate variation. Holding out a source means omitting its samples from regression training; it does not make that source an independently replicated population study. The baseline's linear and quadratic feature family may miss other ecological responses; these gains are relative to the fixed declared model class, not the best possible model without composition.

**A post-analysis preprocessing audit identifies an additional limitation:** the authors' [`norare` pipeline](https://github.com/JSHuisman/salinity/blob/f14abee9d5e2d015deead102c04ea4d3030a5788/code/1_community_experiment/process_asvs.R#L70-L84) removes taxa observed in only one sample across the complete sample set. Thus the deposited current-cycle summaries use current abundance measurements, but their retained taxon set depends on other samples, including later and held-out samples. This is unsupervised global preprocessing, not direct target fitting; nevertheless the complete raw-data pipeline is **not prospectively isolated by fold**. Only our regression feature scaling and fitting are. We did not reprocess raw sequencing within folds or quantify this effect, so the observed gains must not be presented as a verified deployment forecast. This limitation was recorded after execution without changing the frozen primary comparison.

The authors' published ecological result predates this analysis and is not a discovery attributable to our framework. The incremental contribution is a reproducible, limited external comparison with a recorded analysis plan and explicit adverse evidence. A stronger next test would independently manipulate the proposed maintenance or composition mechanism, use an actual perturbation/recovery endpoint, and evaluate on separately collected systems. That work has not been performed.

## Reproduction

Run `python analyze.py` from any location with NumPy installed. Only Python standard library and NumPy are required. The saved environment uses Python and NumPy versions recorded in [analysis.json](results/analysis.json). Downloads and exact SHA-256 hashes are in [provenance.json](data/provenance.json). The complete [matched rows](results/matched_rows.csv), [out-of-fold predictions](results/predictions.csv), [code](analyze.py) and [frozen protocol](PROTOCOL.md) remain available. The initial protocol SHA-256 is `0f73d5091378ecf9c29b10a0c875fdf3e2fb6a0b8a7a0f54bd65cac7b7ec1565`.

At the pinned commit, the public author repository declares no license through GitHub metadata and contains no LICENSE/COPYING file. We record availability and original attribution rather than assigning a new license to those data. The [source preprocessing audit](data/source_preprocessing_audit.json) records that check and the feature-processing limitation.
