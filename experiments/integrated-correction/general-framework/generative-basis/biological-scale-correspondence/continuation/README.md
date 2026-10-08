# Empirical continuation of the scale account

This completes the public-data prediction and feedback analyses selected on 8 October 2026. It adds no mathematical theorem and does not convert the existing conditional Lean model into a fitted biological model.

## Inputs and outputs

- [Analysis plan](analysis-plan.json): written before the new fits, after inspecting published conclusions. Exploratory, not preregistered.
- [Haley original sources](../../../../../../sources/biological-scale-correspondence/elife-103191/README.md): 198 mixed-density animals, 100 imputations, 172,463 conditional-encounter rows.
- [Anderson original sources](../../../../../../sources/biological-scale-correspondence/anderson-2018/README.md): 70 individual fluorescence measurements; separate strain-level avoidance percentages.
- [Analysis](analyze_continuation.py), [results](results.json), [per-worm held-out scores](worm-scores.csv), [figure](continuation-results.png), [figure code](plot_results.py).
- [Interpretation and completion audit](../../../../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/BIOLOGICAL-CONTINUATION-INTEGRATION.md).

The secondary strain summaries were added after the initial foraging results, following inspection of the pathogen study's rescue experiments. They are descriptive evidence checks, without new significance claims or outcome-based model selection. Their cell references and values are retained in the result.

## Reproduction

Python requires NumPy, SciPy and openpyxl; plotting also requires Matplotlib. Dependencies were installed only in `/tmp/scale-validation-env` because SciPy was missing from the bundled runtime. No dependencies or caches are added to the repository. Exact runtime versions are recorded in `results.json`.

```sh
OPENBLAS_NUM_THREADS=1 /tmp/scale-validation-env/bin/python experiments/integrated-correction/general-framework/generative-basis/biological-scale-correspondence/continuation/analyze_continuation.py
/tmp/scale-validation-env/bin/python experiments/integrated-correction/general-framework/generative-basis/biological-scale-correspondence/continuation/plot_results.py
```

The first command reads source workbooks without rewriting them. Independent raw worksheet XML decoding checks every analyzed number against openpyxl, including **2,242,019 numeric cells** in the foraging table. Published predictions are independently reconstructed from the frozen coefficients; summed log likelihoods match the published values. New logistic fits check finite objectives and maximum gradient below `1e-6`, use training-only scaling and hold all encounters/imputations for each worm in one fold.

Each worm receives equal weight; each available imputation within a worm receives equal weight, then its encounters are equally weighted. Three worm/imputation combinations contain no selected encounter, so the table contains 19,797, not 19,800, groups. Averaging across available groups is explicit. Simulation replicas are never treated as additional animals. The paired bootstrap only describes fixed-score variation across the 198 worms; it does not re-estimate classifier, plate, calibration or fitted-model uncertainty.

Published transfer evaluation and new within-preparation cross-validation answer different questions and are reported separately. The latter uses mixed-density training animals, whereas the original transfer predictor was trained on single-density conditions. Its lower loss cannot by itself show that our estimator beats the original model under equal training information.

The `density_satiety` and nonlinear models retain time since previous exploitation. They omit **prior food-density variables**, not every historical influence. Targets are GMM probabilities, and inclusion is based on QDA-derived sensing probabilities. This is conditional prediction given that analysis, not an independent prospective test of a complete sensing–choice–motion process. No residual maximum in this finite table is promoted to a universal error bound.
