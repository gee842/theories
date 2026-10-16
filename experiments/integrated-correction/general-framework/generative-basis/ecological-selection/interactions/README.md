# Measured interactions during settling

Read-only reanalysis of [Driscoll & Travisano 2017, Supplementary Data 5](../../../../../../sources/evolutionary-selection/driscoll-2017/README.md). The original contains 54 mean velocities from videos, grouped into six conditions and 18 explicitly technical replicates. It does not contain individual cluster geometry, neighbor measurements or descendant trajectories.

Run `analyze_interactions.py` with Python and openpyxl, then `python3 check_interactions.py`. The first exports a source-row-labelled CSV and descriptive results. The second uses only the standard library, reads original XLSX XML without openpyxl, verifies all original-file fingerprints, and computes exact-decimal rational means and contrasts. It checks 132 numerical values, agreeing within 3.56 × 10⁻¹⁵, including all 81 combinations of deleting one technical replicate from each of four density conditions. This is independent arithmetic, not an independent biological study or Lean proof.

`plot_interactions.py` requires matplotlib and writes [interaction-correspondence.png](interaction-correspondence.png), visually checked after rendering. All 54 video means are shown with their technical-replicate and condition means. No population confidence intervals are drawn. Dependencies remain outside the repository.

Outputs: [source-row reading](video-means.csv), [results](interaction-results.json), [verification](verification.json). Exact primary-supplement values are preserved in the original workbook; CSV is a separate reading edition. Equal video counts make equal-video and equal-technical-replicate condition means coincide. These are not means weighted by the number of tracked particles.

The stronger density response in K. lactis and the galactose/dextrose contrast survive removal of technical replicates. The S. cerevisiae density contrast is much less stable. Deletion ranges are descriptive sensitivity checks, not confidence intervals, randomization tests or estimates of independent evolutionary replication. Replicate number is not assumed to pair different treatments.

[Theory integration and counterreview](../../../../../../_process/research/2026-10-05-generative-foundation-review/history/root-foundation/AGGREGATION-SELECTION-INTEGRATION.md) gives the implications and limits. This evidence does not choose between the earlier density/drag approximations applied to a different geometry dataset.
