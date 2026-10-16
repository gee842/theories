# Frozen exploratory external prediction protocol

5 October 2026. This protocol is written before numerical biomass, diversity or trait values are inspected or analyzed. The authors' paper and headline results have already been read. This is a post-selection secondary analysis, **not a preregistered independent confirmation**. Only CSV headers, treatment labels, row counts and the authors' preprocessing code were inspected before freezing this protocol.

## Data and question

Use the public author repository for Huisman, Dal Bello and Gore, *Predictable shifts in microbial species composition lead to community-wide robustness to environmental stress*, Nature Microbiology (2026), DOI 10.1038/s41564-026-02422-3. Pin repository `JSHuisman/salinity` to commit `f14abee9d5e2d015deead102c04ea4d3030a5788`.

Four source inocula, three salt conditions, two temperatures and three community replicates underwent repeated growth and 1:30 dilution. Ask a restricted predictive question: do current composition summaries improve held-out prediction of **measured biomass after the next standard growth/dilution cycle**, beyond present biomass and experimental context?

This outcome is neither recovery from an independently imposed shock nor the full capacity for regeneration. Do not use the paper's composition-weighted computed community growth rate as a target: predicting it from composition would be circular. No institutional, AI, legitimacy, succession or endogenous-safeguard conclusion follows from this dataset.

## Aggregation and exclusions

Use `all_od_data.csv`, `mcn_df_norare.csv` and `diversity_df_norare.csv`. Biomass CSV has no replicate identifier. Do **not** infer a sequencing-to-biomass replicate pairing from row order. Average all three biological replicates within each source × salt × temperature × cycle. This sacrifices individual-level resolution and keeps all biological replicates of a condition together for evaluation.

Subtract the mean of that cycle × temperature × salt's blank wells before averaging nonblank OD600, matching author preprocessing. Map `roomtemp` and `roomT` to the same 20°C condition, and `dN`/`DN` to cycle N. Current cycles 1, 3 and 5 predict observed OD at cycles 2, 4 and 6, respectively. Exclude cycle 7 because of the authors' documented contamination; cycle 8 is also unused. Use current-cycle mean 16S copy number (`mcn`) and mean Shannon diversity; other diversity metrics are unused. Report counts and any missingness. Drop incomplete matched rows rather than impute outcomes; if fewer than 18 complete condition trajectories remain, stop and report unsuitability.

## Fixed models and splits

All models predict raw background-corrected next-cycle OD600. Ridge regression uses alpha=1, an unpenalized intercept, and training-only standardization of all nonconstant columns. No hyperparameter selection from test outcomes. Alpha=10 is a prespecified sensitivity only.

Baseline features: current OD; numeric salt and salt squared; numeric temperature; current cycle and cycle squared; salt×temperature; source indicators; and source-indicator interactions with salt and temperature. This permits source-specific environmental responses and basic curvature without using composition.

Augmented model: identical baseline plus current mean `mcn` and Shannon diversity. Two-feature ablations use each summary separately. A persistence predictor simply predicts next OD equal to current OD.

Primary evaluation: leave one complete source × salt × temperature trajectory out (24 expected folds). Every current/next row and every replicate of that condition stays in the same fold. Secondary evaluation: leave one source inoculum out (four folds). Unknown source indicators in a held-out source are all zero; source effects cannot be learned for that source. Sources and temperature-specific plates are shared, so 24 conditions are **not 24 independently sampled ecosystems**.

Report out-of-fold pooled RMSE and MAE, each held-out-source result, per-condition paired squared-error differences, and a descriptive 2,000-resample source-block bootstrap interval for pooled RMSE gain, seeded 20261005. With four source blocks this interval is coarse and not a reliable population-level significance test.

Capacity control: compare the augmented model with 100 same-size models adding two independent Gaussian nuisance features, generated without reference to outcomes, using seeds 20261005 through 20261104. Report the distribution of their out-of-fold RMSE; do not interpret it as a causal permutation test. The primary positive signal would be lower held-out RMSE and MAE, not a favorable training fit. Null, worse or split-dependent performance must be reported directly.

## Interpretation and provenance

Feature improvement would support only incremental predictive value of these two measured summaries under these splits and model classes. A null could reflect genuinely redundant information, poor summaries, small data, restricted linear prediction, or measurement limitations; it would nevertheless fail to support this chosen operational prediction. No alternative endpoint or favorable subgroup will replace it after inspection.

Save exact downloaded files, SHA-256 hashes, code, matched rows, out-of-fold predictions and all results. Any repairs that change the design above must be documented before interpreting the revised result. No extra model or endpoint search is authorized by a disappointing result.
