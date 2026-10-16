# Selected source-data checks for acquired relationships

8 October 2026. This directory checks selected numerical results of Hart et al., eLife 2020, DOI [10.7554/eLife.59998](https://doi.org/10.7554/eLife.59998), for the [semantic-sufficiency investigation](../../../../../_process/research/2026-10-05-generative-foundation-review/history/root-foundation/SEMANTIC-SUFFICIENCY-INTEGRATION.md). This is a source-data reproduction, not a new experiment, a formal proof or a complete reanalysis of the paper.

## Inputs and transformations

Unmodified originals and their licenses/hashes are in [sources/knowledge-semantics](../../../../../sources/knowledge-semantics/README.md). [inspect_source.mjs](inspect_source.mjs) uses read-only Artifact Tool import, inspection and exact range getters. It neither recalculates nor exports the original workbook. [Extracted ranges](source-extracts/figure2.json) and [devaluation ranges](source-extracts/figure3.json) preserve cell values and locators.

The probe source is `'figure  2'!C57:X58` for 22 controls and `C61:W62` for 21 inhibited animals. Within-animal A-minus-C differences are compared between groups using a pooled-variance contrast; its squared t statistic is compared to the reported one-degree-of-freedom interaction F. The response is percentage of cue time in the food port minus its pre-cue baseline. Negative entries are valid and retained.

For devaluation, `'Figure 3'!C4:H6` holds six paired animals over three trial blocks; `C9:I11` holds seven unpaired animals. Calculate the group-by-block interaction with subject-within-group residuals. The block main effect uses equally weighted group marginal means and its corresponding effective sample size. This declared contrast matches the published rounding; that match does not establish exactly which settings the authors used. A sample-weighted block contrast is a different estimand and gives a different result. No search across analyses for a favorable significance claim is made.

The first block has mean responses 6.767% paired and 23.557% unpaired. These devaluation responses have **no baseline subtraction**, unlike the initial probe. Consumption cells `C22:I23` support the separate manipulation check. Columns are treated as the same animals across rows within a panel; no cross-figure identity mapping is asserted. Duplicated panels C/D and the repeated first-block display are checked as duplicates and never add observations.

## Results and limits

[verification.json](verification.json) records four selected statistic reproductions: probe interaction F=4.567, devaluation interaction F=4.576, block main-effect F=4.913 and absolute consumption t=4.946. All match the reported two-decimal values. The initial cue contrast differs by 14.461 percentage points between groups. The script checks every used numeric cell, group sizes, duplicate displays and original hashes.

Published p-values and multiplicity-adjusted post hoc comparisons are not recomputed. Equal-variance and repeated-measures assumptions are retained, not validated by matching statistics. Source summaries do not permit checking raw measurement, all exclusions, individual neural content or causal specificity. These comparisons cannot establish consciousness, propositional understanding, ethical warrant or the necessity of the generative theory. No new mathematical theorem is claimed and no Lean compiler run is required or represented as having occurred.

## Reproduction

Use the bundled workspace Node/Artifact Tool and Python/numpy dependencies. Place a byte-identical copy of `inspect_source.mjs` in a temporary directory with a `node_modules` symlink to the bundled packages, so dependencies remain outside the repository. Invoke it with the repository root and this directory's `source-extracts` as arguments. Then run `check_source_data.py` with the same two arguments. The checker records its own hash, extractor hash, extraction hashes, numpy version and original-source preservation. It does not fetch or refresh sources.
