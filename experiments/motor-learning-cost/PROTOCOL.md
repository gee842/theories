# Retrospective audit of the cost-switch adaptation data

6 October 2026. AI-authored secondary analysis for Ren's generative-grounding research. **Prospective with respect to this repository's new numerical contrasts, retrospective with respect to the published experiment and its known conclusions.** It is not a preregistration or a new experiment.

## Question and scope

In the public participant-level **binned** saccade data, how does adaptation change following the opposed cost switches in Experiment 2, and how does that contrast compare with the separate no-switch Experiment 1 cohort? This measures changes in observable responses within participants. It does not identify replacement of a physical updater, a trial-level error sensitivity, a metabolic bill, or a consequence-selected learning architecture.

Primary article: Sedaghat-Nejad and Shadmehr (2021), [PNAS, DOI 10.1073/pnas.2101717118](https://www.pnas.org/doi/10.1073/pnas.2101717118). Data: [OSF H24J8](https://osf.io/h24j8/), file `cost_of_error_data.xlsx`, 348,982 bytes, SHA256 `0cd6ae5b0f159531f2442f49a474c5ecfda23a1fcf0965598da99df5d84891cc`. Exact bytes and metadata are preserved in [the source directory](../../sources/29-motor-learning-cost-2026-10-06/).

The paper imposes a 300-ms viewing period after a primary saccade. Corrective movements consume part of that period. Low versus high dot coherence changes the consequence of losing viewing time. Experiment 2 switches **both** target-side coherence assignments at trial 951. Control 1 instead starts its viewing timer after gaze reaches the image, removing that time competition. These are experimental opportunity costs, not measured energy reserves or rewiring costs.

**Precomputation correction:** an initial planning suggestion called the other side unchanged. The article says both sides reverse: initially SMALL COST becomes large, and initially LARGE COST becomes small. The primary estimator therefore compares **opposed switches**, not a treated side against an untreated within-person control. Experiment 1 supplies a separate no-switch cohort. This correction precedes numerical contrast calculations.

## Source mapping fixed before contrasts

The workbook has `ADAPTATION` (338 rows, 99 columns) and `DECISION` (146 rows, 78 columns). We analyze only the named `ADAPTATION` blocks below. Workbook labels are treated as the **initial** cost assignment throughout the recorded series, following the published switch design. This mapping is an interpretation of source labels and design, not additional raw metadata. The public listing contains no separate data dictionary or trial-side tags to independently confirm it. All outputs therefore retain literal source block labels; the opposed-switch biological interpretation is conditional on their representing initial side assignments. We will not infer labels from favorable curve shapes.

| Cohort | Initial condition | Header row | Block-number row | Mean trial-number row | Participant rows | IDs |
|---|---|---:|---:|---:|---|---|
| EXP1 / ASYMPTOTE | LARGE COST | 3 | 4 | 5 | 6–25 | 1–20 |
| EXP1 / ASYMPTOTE | SMALL COST | 27 | 28 | 29 | 30–49 | 1–20 |
| EXP2 / SWITCH | LARGE COST | 51 | 52 | 53 | 54–73 | 1–20 |
| EXP2 / SWITCH | SMALL COST | 75 | 76 | 77 | 78–97 | 1–20 |
| CONT1 | LOW COH | 147 | 148 | 149 | 150–169 | 1–20 |
| CONT1 | HIGH COH | 171 | 172 | 173 | 174–193 | 1–20 |

Column A codes condition 1/2; column B contains the participant ID. Pair conditions **within a cohort by ID**, never across cohorts. Matching numerals across experiments do not establish the same person. CONT1 is inventoried but excluded from numerical contrasts this round: its different cost law answers a different question, and we do not expand analyses after inspecting outcomes.

| Window | Nominal published trial interval | Workbook columns | Number of bin means | Block labels |
|---|---|---|---:|---|
| Pre-switch re-adaptation | Mean coordinate 801–931 | AZ:BG | 8 | 9 then first two bins of 10 |
| Early post-switch | Mean coordinate 971–1100 | BJ:BQ | 8 | last two bins of 10 then 11 |
| Late post-switch | Mean coordinate 1101–1250 | BR:BZ | 9 | 12 then 13 |

The source group mean trial coordinates, rather than unreported bin edges, select these windows. A 20-trial guard around trial 951 excludes source bins BH and BI before outcomes are computed. Exact coordinates are saved in an inventory and checked against these intervals. They are not the unreported participant-specific trial indices or bin edges. The figure caption states a bin size of eight trials, without a raw membership export; this audit equally weights the available bin means (eight in pre/early windows, nine in late). The guard reduces proximity to the intervention but cannot prove homogeneous treatment within any bin. Unequal valid raw trial counts and individual excluded trials cannot be recovered from this workbook. We do not turn 180 bin values into 180 independent participants.

## Locked estimators

Let `Y[i,c,w]` be the equal-weight mean of the specified source amplitude-change values for participant `i`, initial condition `c`, and window `w`. Preserve source sign. The article describes primary-saccade amplitude relative to baseline, in degrees. More negative values indicate greater gain-down adaptation; sign is not silently changed to a favorable score.

For each participant and post window `w`, compute:

`delta[i,c,w] = Y[i,c,w] - Y[i,c,pre]`

`C[i,w] = delta[i,initial-small,w] - delta[i,initial-large,w]`.

**Primary:** mean `C[i,early]` in EXP2. Negative values indicate that the initially small-cost side, which becomes costly, shortens its saccade more than the side whose cost falls. Report both component changes and every participant contrast, so this opposed-switch interpretation remains visible.

**Secondary, fixed now:** (a) the same EXP2 contrast in the late window; (b) the analogous early and late contrasts in EXP1; (c) EXP2 minus EXP1 contrast means, with participants independent across cohorts. This last comparison is a descriptive difference of within-person differences. It requires exchangeability/parallel counterfactual trends for a causal experiment-level interpretation, which the source workbook cannot establish. It is not a randomized difference-in-differences design demonstrated by this audit.

For within-cohort means report `n`, mean, sample SD, standard error and two-sided 95% Student-t confidence interval using `n−1` degrees of freedom. For the between-cohort differences use independent-sample standard errors and Welch–Satterthwaite degrees of freedom. These intervals express sampling-model uncertainty, not a proof of causality. No p-value threshold, model selection, trial-level learning gain, best window or responder subgroup will determine the conclusion. Report all fixed contrasts regardless of their sign or uncertainty.

## Missingness, checks and reproducibility

Before contrasts, validate exact source hashes, block labels, unique IDs, matching within-cohort ID sets, the declared number of finite numeric values in every specified window, and mean trial coordinates in the nominal interval. A missing/nonnumeric value stops the primary analysis; do not impute, silently drop a bin/participant or enlarge a window. Any amendment must preserve this protocol and document why it was needed. No participant is excluded by observed effect size.

Save a source-cell inventory, extracted binned values with sheet/cell provenance, participant window means/contrasts, aggregate results, source/program hashes and package versions. A separate reviewer will reconstruct the chosen estimator from original XLSX XML without inspecting this producer. Neither implementation should read the other's numerical output before fixing its estimator.

No MATLAB model-fit download or reanalysis is included. The accessible workbook does not preserve raw error sequences, saccade timing, subjective error, receptor state or a candidate updater intervention. Public stimulus/filter code and fitted-state files are catalogued in the preserved OSF listing, not treated as missing raw observations. The mechanistic interpretation must retain this data boundary.

**Precomputation amendment record:** the initial draft used adjacent nine-bin pre/early windows. Metadata review identified that mean coordinates do not determine raw bin support. The guarded windows above were fixed before any numerical contrast. The earlier draft is [preserved](development/PROTOCOL-before-boundary-guard.md). No outcome-driven selection occurred.
