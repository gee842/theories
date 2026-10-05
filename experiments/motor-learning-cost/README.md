# Motor-learning cost: a bounded public-data audit

6 October 2026. Retrospective secondary analysis of Sedaghat-Nejad and Shadmehr's [PNAS experiment](https://www.pnas.org/doi/10.1073/pnas.2101717118), using its public [OSF workbook](https://osf.io/h24j8/). The original bytes and metadata are [preserved](../../sources/29-motor-learning-cost-2026-10-06/README.md). This is an empirical check of cost-sensitive adaptation, not evidence that a biological learning-rule component was replaced.

**Numerical status:** independently verified. The XML reconstruction matches 2,000 source values, 2,000 coordinate occurrences, 240 window means, 160 component changes, 80 participant contrasts and 112 aggregate fields; maximum absolute numerical discrepancy is 7.1×10⁻¹⁵. The [independent scope review](../../_process/research/2026-10-05-support-and-shared-generativity/completion/MOTOR-LEARNING-COST-REVIEW.md) also accepts this bounded analysis; neither review establishes a physical updater change. The [protocol](PROTOCOL.md) was fixed before the new contrasts, but after publication of the source and its conclusions. It is not a preregistration. The [freeze](protocol-freeze.json) and [earlier window draft](development/PROTOCOL-before-boundary-guard.md) preserve the precomputation correction and guard-band amendment.

## What was calculated

The `ADAPTATION` sheet contains repeated participant blocks. We pair IDs 1–20 within EXP1 and within EXP2; shared ID numerals do not pair people across experiments. The analysis uses 2,000 source values, forming 240 participant/series/window summaries and 40 participant pairs. No values are imputed and no participants excluded. CONT1 is inventoried only.

For each literal source series, average the eight published bins at columns AZ:BG (mean trial coordinates 801–931), eight at BJ:BQ (971–1100), and nine at BR:BZ (1101–1250). BH and BI are excluded by the fixed 20-trial center guard around trial 951. Equal bin weighting is not exact raw-trial weighting; the workbook does not supply bin membership or valid-trial counts.

For each participant and post window, the contrast is:

`C = (SMALL COST post − SMALL COST pre) − (LARGE COST post − LARGE COST pre)`.

The source sign is retained; units are degrees of baseline-relative primary-saccade amplitude. The means of each source-series change remain in [results.json](results.json), as do every participant's window means and contrasts.

EXP2 reverses both coherence-side assignments at trial 951. Thus it has no untreated opposite side. The secure numerical estimand is the **literal source-series contrast**. Reading LARGE/SMALL as the *initial physical sides* makes it an opposed-switch contrast, but this mapping is not independently verified by a raw side-tag dictionary. We do not infer it from the curve shape. EXP1 is a separate no-switch cohort, not a randomized within-person counterfactual for EXP2.

## Fixed results

All intervals below are two-sided 95% sampling-model intervals. Cohort intervals use paired participant contrasts and Student-t; between-cohort intervals use Welch–Satterthwaite degrees of freedom.

| Estimand | Mean (degrees) | 95% interval | Role |
|---|---:|---:|---|
| EXP2 early, n=20 | −0.181722 | [−0.453318, 0.089873] | **Primary** |
| EXP2 late, n=20 | −0.340414 | [−0.593631, −0.087197] | Secondary |
| EXP1 early, n=20 | 0.206334 | [−0.015941, 0.428609] | Secondary comparator |
| EXP1 late, n=20 | 0.252509 | [−0.029550, 0.534569] | Secondary comparator |
| EXP2 minus EXP1, early | −0.388056 | [−0.727942, −0.048171] | Secondary, between cohorts |
| EXP2 minus EXP1, late | −0.592923 | [−0.959680, −0.226166] | Secondary, between cohorts |

The primary estimate is negative but its interval includes zero. The later and between-cohort estimates are more clearly separated from zero under the declared sampling models; they do not replace the primary. These are response-trajectory contrasts. They neither estimate a trial-level learning gain nor establish a cost-only causal effect or a changed retained updater. A causal interpretation of the cohort difference would additionally require an adequate assignment/counterfactual design.

## Preserved computation

- [analyze.py](analyze.py): independent producer using `openpyxl`; checks exact source/protocol hashes, labels, IDs, coordinates and finite cells before analysis. It opens the workbook in memory and never saves it.
- [inventory.json](inventory.json): source block locations, literal labels, IDs, mean trial coordinates and guarded-out bins.
- [extracted.json](extracted.json): each analyzed value with sheet/cell provenance; no reconstructed raw trials.
- [results.json](results.json): participant and aggregate outputs.
- [verification.json](verification.json): producer source/output hashes, package versions and read-only source check.
- [independent_check.py](independent_check.py) and [independent-results.json](independent-results.json): separate XML-based estimator, fixed before comparing outcomes. The separate [comparison](compare_check.py) and [passed receipt](independent-verification.json) record the agreement and frozen hashes.
- [paired-contrasts.png](paired-contrasts.png) / [SVG](paired-contrasts.svg), [plot source](plot_results.py) and [figure receipt](figure-verification.json): participant contrasts and uncertainty intervals, including the uncertain primary.
- [identification_check.py](identification_check.py): separate synthetic exact-arithmetic identification countermodels, not data analysis or a reproduction of the paper's fitted gains.

The [requirements](requirements.txt) pin the verified scientific packages. The producer uses bundled Python 3.12.14, `openpyxl` 3.1.5 and `mpmath` 1.3.0. It computes Student-t quantiles by inverting a regularized incomplete-beta CDF with 50-digit arithmetic; the independent estimator uses SciPy 1.18.1. The figure uses Matplotlib 3.11.2 and NumPy 2.5.3. Temporary scientific dependencies live outside the repository. With those dependencies available:

```sh
python experiments/motor-learning-cost/analyze.py
```

For the runtime used in this record:

```sh
PYTHONPATH=/tmp/motor-cost-producer-deps /Users/ren/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 experiments/motor-learning-cost/analyze.py
```

The independent estimator and comparison can be rerun with `python experiments/motor-learning-cost/independent_check.py` and then `python experiments/motor-learning-cost/compare_check.py`. The scientific figure is generated by `python experiments/motor-learning-cost/plot_results.py`.

`--inventory-only` extracts and validates cells without calculating contrasts. Running the producer recalculates its outputs but does not overwrite the independent outputs. Scientific checks need rerunning only after a substantive source/code/protocol change or an unresolved discrepancy.

## What this advances

The [evidence audit](../../_process/research/2026-10-05-support-and-shared-generativity/completion/MOTOR-LEARNING-COST-EVIDENCE.md) connects actual behavioral data to the paid route-revision branch and states the remaining empirical gap. The [identification analysis](../../_process/research/2026-10-05-support-and-shared-generativity/completion/UPDATER-IDENTIFICATION-MATH.md) shows why changing a fitted gain, delivered input, available writing or hidden memory can produce similar observations. The concrete next mechanism claim requires an independently specified retained component and matched input/write/readout interventions; this workbook does not supply those measurements.
