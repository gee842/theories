# Published biological measurements across scales

Read-only extraction and descriptive reanalysis of the original eLife 65935 Figure 2B/4C workbooks. [Source manifest](../../../../../sources/biological-scale-correspondence/elife-65935/manifest.json) preserves provenance and hashes. [Interpretation](../../../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/ORGANIZED-SCALES-EVIDENCE.md) states biological limits.

Run `extract_measurements.mjs SOURCE_DIRECTORY OUTPUT_DIRECTORY` with the bundled Node runtime and artifact-tool. A temporary copy can be placed beside a `node_modules` symlink to the bundled dependencies; no dependency installation is needed in this repository. Use `extracted` here as the output directory. Then run `analyze_measurements.py` with the bundled Python runtime containing openpyxl and NumPy.

The saved extraction retains every cell, including blanks. The analysis compares all cells to a second read-only extraction, computes group means/sample SDs and compares those calculations with NumPy. [results.json](results.json) contains 268 diameter and 135 occupancy measurements' summaries with cell references. The oxygen comparison is a difference of means, with no asserted pairing or new significance test. These records do not fit or validate the Lean mechanism.
