# Remote social cue and recipient-directed food access

6 October 2026. Retrospective reanalysis of the complete public experiment-4 data preview from Gerber, Schweinfurth and Taborsky's *The smell of cooperation*. Across all 24 displayed focal-rat pairs, the cooperating-cue situation has **1.33 more pulls per seven-minute session** than the neutral situation. This measures a difference in recipient-directed food-access actions. It does not identify recipient-specific reasoning, an identity mistake, moral concern or a solution to alignment.

The [analysis](analysis.py) implements the [frozen local protocol](PROTOCOL.md), with its [freeze receipt](protocol-freeze.json). [Results](results.json) retain every source cell string, parsed value, pair, omission and coding diagnostic. The [independent checker](check_analysis.py) and its [verification receipt](independent-verification.json) accept the numerical reconstruction: all source cells, paired arithmetic, bootstrap replay and 50 exact reference calculations across the full sample and all omissions match. The [conceptual review](../../_process/research/2026-10-05-generative-foundation-review/history/root-foundation/CUE-GROUNDING-REVIEW.md) also accepts the scoped implementation and interpretation. The historical executable result keeps its original `computed_pending_independent_review` status; the separate receipt and review record this subsequent acceptance.

## Source and design

The [preserved TSV](../../_process/research/2026-10-05-generative-foundation-review/root-foundation/reason-action-evidence/experiment4-preview.tsv) is a reading edition of all 48 displayed data rows. Original CSV downloads failed, so original file bytes were not verified. The root independently checked every displayed DOM cell against the transcription: 3119 canonical ASCII bytes, FNV1a64 `df8ebe2256185e27`. This verifies the visible rendering, not the inaccessible original. The first blank header was renamed `preview_row`; other strings remain unchanged.

The focal rat faced a noncooperative recipient while receiving odor from another rat elsewhere. The same odor provider was compared while helping versus having no pulling-stick access. Experiment 4's cue was contemporaneous with action. The [primary article](https://pmc.ncbi.nlm.nih.gov/articles/PMC7739497/) and [methods audit](../../_process/research/2026-10-05-generative-foundation-review/history/root-foundation/CUE-GROUNDING-METHODS.md) supply design context. Donor/recipient IDs, treatment sequence and session dates are absent from this preview.

The published result uses n=23; the methods, supplement and complete displayed table support 24 available pairs. This is an unexplained sample-size discrepancy: no exclusion has been established, and a reporting or version mismatch is also possible. References to an "exclusion" in the frozen protocol and historical code/results describe an unverified possibility, not a determined cause. All 24 are retained, with every possible single-animal omission reported. Published findings and the prior preview descriptives were already known before this computational plan was frozen. This is not preregistration, an outcome-blind study or a reconstruction of the original fitted analysis.

## Paired count results

Each focal animal contributes one neutral and one cooperating session. Pulls within sessions are not additional independent subjects. Zero counts and zero differences remain in the primary analysis.

| Quantity | Result |
| --- | ---: |
| Complete focal-animal pairs | 24 |
| Neutral pulls, total / mean | 21 / 0.875 |
| Cooperating pulls, total / mean | 53 / 2.2083 |
| Mean paired difference | 1.3333 |
| Median paired difference | 1 |
| Sample SD of paired differences | 1.7110 |
| Increasing / decreasing / tied pairs | 17 / 4 / 3 |
| Zero-count neutral / cooperating sessions | 10 / 4 |
| Exploratory 95% animal-paired bootstrap interval for mean difference | [0.6667, 2.0000] |

The bootstrap resamples complete animals 20,000 times with `random.Random(20261006)`, lexicographically ordered focal IDs and linearly interpolated percentile limits. Its sampling interpretation assumes comparable independent animal units. Shared donors, common influences or dependence across animals could invalidate that assumption; the preview cannot estimate them. Historical selection and multiple reported endpoints are not adjusted for.

The exact equiprobable paired-sign reference calculation gives `24496 / 16777216 = 0.0014600754` for a two-sided absolute-sum tail, including equality and all zero-pair multiplicities. The secondary binomial sign reference gives `15094 / 2097152 = 0.0071973801` among 21 nontied pairs. These calculations are exact under their stated reference distributions. They are **not recovered assignment-exact randomization probabilities**: the allocation probabilities/restrictions, interference and carryover are unavailable. Sign symmetry or the corresponding sharp-null design assumptions require justification; a zero mean alone does not justify them. Neither numerical threshold determines conceptual acceptance.

## All single-animal omissions

All 24 omissions appear individually in [results](results.json). Their mean differences range from 1.1739 to 1.4783 additional pulls; paired-sign reference probabilities range from 0.00035095 to 0.00291824; binomial sign references range from 0.00257683 to 0.01181793. No omission is selected or treated as explaining the published sample size. These ranges describe sensitivity to one animal, not correction of the unresolved source discrepancy.

## Coding audit and interpretation limits

All required count/identity fields are present, with no duplicate or incomplete pair. Two `Pull6` cells, preview rows 39 and 41, are `NA`; they remain missing. All 14 zero-count sessions display first-pull timing 420; all 34 positive-count sessions have first timings from 6 to 389 seconds. No zero-count 420 is treated as an observed event. No latency treatment estimate is calculated. The main article's latency Wilcoxon p=.003 and supplementary Cox p=.048 remain an unresolved discrepancy.

The positive count contrast is compatible with sensitivity to the remote provider's assigned situation. That situation bundles cooperation with stick access, activity and other possible state changes. Cue-triggered helping, generalized reciprocity and richer recipient models remain possible. No delayed memory test or alternative-beneficiary choice occurs here. A fixed identity-only account is a narrower comparator because the odor provider's identity was held constant, but the contrast does not identify a unique cognitive mechanism.

Counts concern food-access actions, not independently verified ingestion, welfare, energy expenditure or survival. This study therefore constrains an interpretation of helpful behavior rather than deriving moral concern or governance. Experiment 3's incomplete preview is not analyzed numerically as a complete dataset.

## Reproduction

Run `python3 experiments/recipient-cue-grounding/analysis.py` from the repository root. Only the Python standard library is needed. The program verifies the preserved TSV and frozen protocol SHA-256 values and the DOM transcription receipt before computing. Invalid structure pauses numerical acceptance rather than excluding rows. The analysis/result hashes and exact integer probability numerators make independent checks possible; old source and candidate files are unchanged.
