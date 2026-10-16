# Review of the retrospective motor-learning cost audit

6 October 2026. AI-authored independent internal review. **Accepted as a bounded, independently reproduced secondary analysis and an identification-limit study.** This acceptance does not certify a changed biological updater, the paper's unreplicated model fits, or the complete generative foundation. No new experiment was performed.

The named connection is consequences and their costs → changed responses during learning → warranted identification of an operative updater. The [evidence account](MOTOR-LEARNING-COST-EVIDENCE.md) makes the first empirical connection at a limited observable level. The [identification analysis](UPDATER-IDENTIFICATION-MATH.md) establishes why a stronger mechanism claim requires additional observations and interventions. They must be read together.

## Design review before calculation

I read the [primary article](https://pmc.ncbi.nlm.nih.gov/articles/PMC8501785/) and the draft [analysis protocol](../../../../experiments/motor-learning-cost/PROTOCOL.md) before the new contrasts. Experiment 2 reverses both target-side coherence assignments at trial 951. The opposite side is therefore not an untreated within-person control. Experiment 1 is a separate no-switch cohort. The initial mistaken control description was corrected before calculation and remains recorded.

The article describes amplitude relative to each condition's baseline. Within a fixed series, subtracting pre from post cancels that fixed baseline offset. It does not establish that a series preserves physical-side identity after the switch. The public LARGE/SMALL labels and experimental description do not independently supply raw side tags or a post-switch grouping dictionary. The secure estimand is the literal source-series contrast; the opposed-physical-switch interpretation remains conditional. Neither curve continuity nor agreement with a published conclusion can resolve that uncertainty.

The initial nine-bin adjacent windows were amended before calculation. The fixed mean-coordinate guard excludes BH and BI around trial 951, leaving eight pre bins, eight early bins and nine late bins. The [original draft](../../../../experiments/motor-learning-cost/development/PROTOCOL-before-boundary-guard.md) is preserved. This is a cautious boundary choice, not proof that unreported individual bin membership never crosses the switch. Equal weighting of published bin means also does not reconstruct trial-weighted means when valid-trial counts are unavailable.

The analysis is prospective only relative to these new calculations: the published findings were already known. It is not a preregistration. No window, subgroup, sign convention or primary endpoint was changed after the numerical results appeared. CONT1 remains an inventoried source block, not an added outcome analysis.

## What was checked

I reviewed both estimators and the final comparison program. The producer reads the workbook through `openpyxl`; the separately fixed estimator reads original XLSX XML. The producer obtains Student-t quantiles through a high-precision incomplete-beta calculation, while the independent estimator uses SciPy. Both implement the declared subject-level differences and independent-cohort Welch intervals.

All 20 IDs are retained within each analyzed cohort, with pairing only within that cohort. The two cohorts are not paired by matching ID numerals. Literal numeric zero remains data; missing or nonfinite selected cells would stop analysis. There are no exclusions or imputations in the 2,000 selected amplitude cells. This does not establish that no trials were excluded before the public bins were created; the workbook does not expose that history.

The final independent comparison checks:

- 2,000 original amplitude values and 2,000 repeated trial-coordinate occurrences;
- 240 participant/series/window means, 160 component changes and 80 paired contrasts;
- 112 aggregate fields, including interval endpoints and critical values.

Agreement is within the declared absolute/relative tolerance of `1e-12`; the maximum absolute difference is approximately `7.1e-15`. Coordinate occurrences and bins are not additional independent participants. The statistical unit is the participant, with 20 paired contrasts per cohort and window.

I matched the six preserved source-file sizes and hashes, the frozen protocol and producer program, every saved producer output, and all eight files bound by the independent receipt. The separate synthetic identification check's source hash also matches its receipt. No scientific pipeline was rerun merely for this review.

## The uncertain primary remains primary

The primary EXP2 early literal-series contrast is **−0.181722°**, with a 95% Student-t interval **[−0.453318, 0.089873]**. Its component changes are −0.398970° for SMALL and −0.217248° for LARGE. The estimate points in the predicted direction under the conditional fixed-side interpretation, but its interval includes zero. It establishes neither a clear signed primary difference at this interval level nor equivalence to zero.

The fixed secondary EXP2 late contrast is −0.340414° [−0.593631, −0.087197]. The early and late EXP2-minus-EXP1 contrasts are −0.388056° [−0.727942, −0.048171] and −0.592923° [−0.959680, −0.226166]. They remain secondary; their stronger separation from zero cannot replace the planned primary result. The evidence note and package README report all six fixed contrasts, including both EXP1 results.

These are marginal sampling-model intervals, not simultaneous coverage or causal certificates. A causal interpretation of the cohort comparison needs an adequate assignment/exchangeability and counterfactual-trend argument; the workbook does not establish it. The paired temporal comparison also does not eliminate carryover, nonlinear readaptation, changing sensory demands or latent-memory effects. Its uncertainty does not refute the paper's mixed-model and state-space analyses, which this audit did not reproduce. Nonsignificant reported control or retention effects cannot be promoted to equality claims.

## The mechanism boundary is substantive

The identification note correctly separates observable response contrasts, fitted error sensitivity within a specified model, and intervention on a retained updater. Its fixed augmented-state representation is an exact rewriting of the same process, not evidence against operative revision. Its input-rescaling countermodel gives pathwise equality between condition-dependent gain and fixed gain with changed delivered input. The binary writing gate gives a conditional-mean equality, with a different variance; it does not claim full distributional equivalence. The hidden-memory example correctly shows why matching current output need not match acquired state.

The exact-rational script checks 18,432 synthetic input-encoding histories, 480 gate-mean equalities and the stated intervention/exclusion examples. It does not analyze participants, reproduce neuroscience fits or add Lean theorem audits. The general claims rest on the displayed algebra and stated intervention-preserving hypotheses; finite enumeration is supporting verification.

No blocking overidentification remains in the final evidence account. Opportunity cost is not a measured metabolic bill; binned amplitude change is not a measured trial-level update gain; a fitted gain is not an observed newly built learning apparatus. The result adds external evidence with a bounded and partly uncertain interpretation instead of treating a synthetic construction as its own empirical validation.

## What follows and what would change the claim

The first source-identification improvement is a grouping dictionary or raw side-tagged export. Raw error and timing records could support an independently specified sensitivity/retention analysis and constrain writing/input alternatives. Those additions would still not locate a retained physical updater. That stronger claim needs an identified component and selective intervention or rescue under adequate memory, delivered-evidence, writing-opportunity and readout controls, retaining incomplete histories and costs.

If side labels were found to regroup after the switch, the numerical source-series contrast would remain reproducible while its fixed-side interpretation would need revision. If an intervention acted through input encoding or readout, the mechanism attribution would change without erasing cost-sensitive behavior. Such possibilities are constraints on the next study, not reasons to search the present workbook for a more favorable endpoint.

The round advances the governing foundation's empirical-identification requirement. It leaves the origin and maintenance of calibrated sensing, the construction and retention of learning mechanisms, shared evaluative grounds and broader empirical scope open.

## Frozen evidence

| Artifact | SHA256 |
|---|---|
| [Original workbook](../../../../sources/29-motor-learning-cost-2026-10-06/cost_of_error_data.xlsx) | `0cd6ae5b0f159531f2442f49a474c5ecfda23a1fcf0965598da99df5d84891cc` |
| [Protocol](../../../../experiments/motor-learning-cost/PROTOCOL.md) | `070940c7933c4aaf4115254b931230eeb50e7c08bffd214a20d3fe4ad3c28594` |
| [Producer receipt](../../../../experiments/motor-learning-cost/verification.json) | `6b18308130fe153e0f788c12e5b7dffa54178f5364710a25c69bb843519ecfad` |
| [Independent receipt](../../../../experiments/motor-learning-cost/independent-verification.json) | `75a89151b362f299ec2b75cbe787aaaea461e2f4d1587fa10d83921bcf496a85` |
| [Results](../../../../experiments/motor-learning-cost/results.json) | `19ce7e39c60525fdcce94888aa9d70fb69701a48c30ce924e37182768b078ec0` |

This is collaborating-AI internal review of an independently reproduced calculation, not independent human peer review or new clinical evidence.
