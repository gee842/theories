# Control of encounters and later learning

8 October 2026. Exploratory secondary analysis for the continuing cognition objective. Reuse `encounter-selection-and-revision` and `naming-attention-coverage`; no new local updater is proposed.

## Question before data inspection

Does control of naming encounters yield greater later label recognition in the public CuriGaze data accompanying Bazhydai et al., [DOI 10.1111/desc.70101](https://doi.org/10.1111/desc.70101), [OSF ndthz](https://osf.io/ndthz/)? The published methods/results are already known; CSV values have not been inspected. This is not blinded analysis or preregistration. The added contribution is uncertainty and reconstruction of the measured selection-to-later-use contrast, not an inference that gaze control equals curiosity or reciprocal social understanding.

## Fixed analysis

1. Preserve the nine small public source files (six summary CSVs, the analysis R script, laboratory log and README), plus paginated API metadata and hashes. The three large raw/trajectory files are not required for the declared summary-level analysis and will not be downloaded by default. Inspect the author's code as source material; do not execute it automatically.
2. Audit participant identifiers, condition labels, inclusion criteria, finite/missing values and row units. Trace the participant baseline-corrected target-looking measure into the trial summaries. Inspect the laboratory log for exclusions and assignment history without reporting individual child details. Retain source bytes unchanged.
3. Primary outcome: per-participant mean change in target-looking proportion after versus before the test label, using the authors' supplied summaries. Report group means, SDs and 95% Student-t intervals. Recompute the reported one-way ANOVA as a check on aggregation, not as an equality proof.
4. Primary contrasts: Curiosity minus Yoked and Curiosity minus Random. Report unadjusted 95% Welch intervals, group sample sizes and assumptions. These are secondary descriptive comparisons, not new confirmatory tests or guaranteed sequential-design confidence coverage. No equivalence margin is chosen after seeing results; an interval containing zero is not proof of no effect.
5. Assess the observed within-condition outcome relative to zero using one-sample t statistics, retaining the three-comparison Bonferroni adjustment if reporting significance. Do not equate that outcome with full comprehension, long-term memory or correctly learned labels for every child.
6. Use trial summaries and the participant inclusion list to reconcile the participant outcome and count available trials. If definitions differ, report rather than silently repair them. Binary label/trial files can clarify their unit and denominator; do not substitute them for the primary outcome or run a pseudo-replicated trial analysis.
7. Read the comparison's assignment and selection limits. A condition named Random randomizes the presentation sequence, not necessarily participant allocation. The active condition was collected before its controls; do not claim a randomized treatment effect without additional evidence. Investigate yoking identifiers before assuming pairs or dependence; absent identifiers limit paired inference.

## Comparative interpretation

Compare this non-social display task with Begus, Gliga and Southgate (2014), [DOI 10.1371/journal.pone.0108817](https://doi.org/10.1371/journal.pone.0108817), which tests an adult response to a child's pointing and later action reproduction. Read methods, controls and limits before linking them. Different ages, tasks, delays and social relations prevent treating cross-study differences as an isolated social-interaction effect. Do not infer lack of all attention mechanisms from a null group contrast or memory formation from look duration alone.

The theoretical target is to distinguish control of exposure, effective coordination, retained modification and later use within one interaction history. Evidence that these come apart sharpens the required producer-to-consumer connection. It cannot by itself finish cognition, affect, consciousness or evolutionary psychology. No new mathematical theorem is claimed; existing checked conditional results retain their scope.

## Verification

Independently reconstruct participant means and elementary ANOVA quantities from original CSV fields using decimal arithmetic; use a standard statistical library for distribution functions. Preserve exact exclusions, discrepancies and assumptions. Record source/code/output hashes and substantive author counterreview. Integrate into the existing acquired-segmentation study and current cognition chapter.

## Schema-audit amendment before group-outcome aggregation

The deposited summary has 77 participants (26 Curiosity, 25 Random, 26 Yoked), while the article analyzes 75. The author's R script merges the trial table with `Data/CuriGaze_log_Cleaned.csv` before the reported participant analyses. The standalone master-log download repeatedly returned HTTP 429 after bounded waits. The cleaned log is therefore a required inclusion source. Retrieve `Data.zip` into temporary storage if available, verify its deposited hash, inspect its member names and preserve only the relevant original log bytes with archive/member provenance. Do not infer exclusions by selecting the rows that reproduce a desired published result. Keep the complete 77-person export as a sensitivity if the 75-person population can be identified from the log. This amendment changes acquisition scope, not the chosen outcome or contrasts.
