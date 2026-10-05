# External microbial prediction test, including preprocessing repair

5 October 2026. **The primary result is mixed after repair: composition reduces large prediction errors but slightly worsens average absolute error.** A prespecified source-holdout sensitivity improves both measures. This is preliminary external evidence for a restricted prediction question, not validation of the general theory.

## Data and design

The data are from Huisman, Dal Bello and Gore, [*Predictable shifts in microbial species composition lead to community-wide robustness to environmental stress*](https://www.nature.com/articles/s41564-026-02422-3), Nature Microbiology (2026), and the [authors' pinned public repository](https://github.com/JSHuisman/salinity/tree/f14abee9d5e2d015deead102c04ea4d3030a5788). Four source inocula, three salinities and two temperatures provided 24 condition trajectories, each with three community replicates.

The biomass CSV lacks replicate identifiers. We averaged all three replicates within condition instead of inventing individual biomass–sequencing pairings. All 72 current/next-cycle pairs are complete. Current cycles 1, 3 and 5 predict **measured OD600 at cycles 2, 4 and 6**, after ordinary growth and dilution. The contaminated cycle 7 is unused. This is not recovery from a novel shock. The authors' composition-computed growth rate is deliberately not a target.

The baseline includes current biomass, salinity, temperature, cycle and source, with fixed interactions and curvature. The augmented model adds current mean 16S copy number and Shannon diversity. Whole conditions or sources are held out; regression scaling and fitting use training rows only. The [protocol](PROTOCOL.md) was frozen before numerical outcomes were inspected, but after reading the paper. This remains post-selection exploratory secondary analysis, not preregistration or blind confirmation.

## Audit repair

The deposited summaries remove taxa found in only one sample across the entire experiment, creating dependence on later and held-out samples during unsupervised preprocessing. The [v1 report](RESULTS-V1.md) and [v1 outputs](results/analysis.json) are preserved.

A [repair protocol](PROTOCOL-REPAIR.md) was frozen before corrected features or predictions were computed. We reconstructed the source summaries from deposited count/taxonomy matrices and the fixed rrnDB reference, then removed global prevalence selection. Corrected summaries use each sample's own counts plus fixed taxonomic eligibility and reference rules. Every original MCN and Shannon value across 368 samples was reproduced to within **2.5×10⁻¹⁴** before repair, meeting the frozen 10⁻⁷ tolerance. No endpoint, model, split or tuning choice changed. See the [reconstruction audit](data/reconstruction_audit.json).

This removes the identified prevalence dependency. Upstream sequence denoising, chimera removal and taxonomy are still accepted as deposited; raw-read processing was not independently rerun. Both split schemes train on other trajectories' later cycles, so these test generalization across conditions or sources, not a past-only chronological forecast.

## Original and repaired results

Errors are out-of-fold, in background-corrected OD600 units; lower is better. Alpha=1 is primary.

| Split and feature version | Baseline RMSE | + Composition RMSE | Baseline MAE | + Composition MAE |
|---|---:|---:|---:|---:|
| Condition holdout, original | 0.09369 | 0.08688 | 0.06868 | 0.06895 |
| Condition holdout, repaired | 0.09369 | **0.08687** | 0.06868 | **0.06902** |
| Source holdout, original | 0.09350 | 0.07751 | 0.06833 | 0.06000 |
| Source holdout, repaired | 0.09350 | **0.07719** | 0.06833 | **0.05960** |

The repaired primary comparison reduces RMSE by 7.3% but worsens MAE by 0.00034. Fourteen of 24 conditions improve in squared error. The descriptive source-block bootstrap 95% interval for RMSE gain is **−0.00579 to 0.01608**, crossing zero. With only four source blocks, this interval is coarse and not reliable population-level significance evidence. The prespecified expectation of improvement on both measures is not met.

The repaired source-holdout sensitivity reduces RMSE by 17.4% and MAE by 12.8%; 16 of 24 conditions improve in squared error. All four source RMSEs improve, but Estuary MAE worsens. Its coarse interval for RMSE gain is 0.00340 to 0.02585. This favorable secondary result does not replace the mixed primary result.

| Source held out, repaired | Baseline RMSE | + Composition RMSE | Baseline MAE | + Composition MAE |
|---|---:|---:|---:|---:|
| Brackish / `charles` | 0.14072 | 0.11392 | 0.10779 | 0.09736 |
| Marine 2 / `fucus` | 0.06584 | 0.06139 | 0.05509 | 0.05260 |
| Estuary / `ica` | 0.06408 | 0.06173 | 0.04185 | 0.04347 |
| Marine 1 / `nahant` | 0.08201 | 0.05724 | 0.06858 | 0.04496 |

The persistence predictor has RMSE 0.12121 and MAE 0.07667. Thus the informative baseline already substantially improves on predicting unchanged biomass. The complete [paired per-condition squared-error differences](results-unfiltered/paired_condition_errors.csv) are retained, including worsening conditions.

## Prespecified sensitivities and controls

Repaired alpha=10 improves both measures: condition-holdout RMSE 0.08994 → 0.08254 and MAE 0.06535 → 0.06227; source-holdout RMSE 0.08914 → 0.07499 and MAE 0.06519 → 0.05625. This sensitivity does not erase the primary MAE result.

Mean-copy-number-only gives primary condition-holdout RMSE 0.08500 and MAE 0.06694; Shannon alone gives 0.09287 and 0.06983. The better ablation is not promoted to primary. Of 100 same-size nuisance-feature controls, one beats the augmented model's condition-holdout RMSE and none beats its source-holdout RMSE. Their medians are 0.09498 and 0.09421. These controls are **not causal permutation-test p-values**. All outputs are in [corrected analysis.json](results-unfiltered/analysis.json).

## Meaning and limits

There is some evidence that these composition summaries add predictive information beyond current biomass and recorded environment within the declared model class. The analysis does not identify a causal feedback loop, biological renewal investment, succession, self-maintaining correction, situated goal formation, universal attractors or institutional/AI transfer. Mean 16S copy number is a composition summary, not a direct measure of regeneration.

The 24 conditions share four inocula and temperature-specific experimental conditions; they are not 24 independent ecosystems. Aggregation suppresses individual variation. The baseline can miss nonlinear ecological responses. Holding out one source from fitting does not create an independently replicated ecological study. The authors' ecological findings predate this analysis and are not discoveries attributable to our framework.

The contribution here is a reproducible external-data check, detection and repair of a preprocessing dependency, and preservation of unfavorable evidence. Stronger tests would manipulate the proposed mechanism, measure actual perturbation/recovery and use separately collected systems. That work is not complete.

## Reproduction and source rights

Run `python analyze.py` for v1; then `python reconstruct_features.py` and `python analyze_repaired.py` for the corrected version. `python export_paired_errors.py` exports the per-condition comparison from both saved prediction files. The original analysis needs NumPy; reconstruction additionally needs `rdata` and its dependencies. Versions and hashes are recorded in JSON. [Original download provenance](data/provenance.json) and [repair provenance](data/repair_provenance.json) pin commit `f14abee9d5e2d015deead102c04ea4d3030a5788`. Corrected [matched rows](results-unfiltered/matched_rows.csv) and [predictions](results-unfiltered/predictions.csv) are retained beside v1.

The pinned author repository declares no license through GitHub metadata and contains no LICENSE/COPYING file. We retain original attribution and do not assign those data a new license. Original protocol SHA-256: `0f73d5091378ecf9c29b10a0c875fdf3e2fb6a0b8a7a0f54bd65cac7b7ec1565`. Repair protocol SHA-256: `61a945c5cc6394f2e26f0cb40d00aeb81dd38e4aabc03ff32362e202837eabcb`.
