# Read-only RNA input audit

The [identification contract](../../../_process/research/2026-10-05-support-and-shared-generativity/completion/RNA-IDENTIFICATION-CONTRACT.md) defines the scientific scope. `audit.py` reads the preserved publisher workbook and pinned author notebook, verifies original hashes, reconstructs all 15 host-donor effective coefficients in supplementary Fig. S23, checks a conditional two-RNA joint-renewal boundary, and supplies an exact kinetic nonidentifiability witness. `audit.json` records source cells, descriptive values and limitations.

Run with the bundled Python runtime, which supplies openpyxl:

```sh
/Users/ren/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 experiments/shared-renewal-capability/rna-identification/audit.py
```

Only this directory's JSON result is written. The original workbook, PDFs and notebook are not changed or executed. Matrix values are recomputed from measured fold-change means and compared with a visual transcription of the numeric S23 table; no plot points are digitized. Parasite-donor zero rows are a model specification, not newly measured elementary rates.

The capacity boundary uses the published model's normalized units and central effective coefficients. Its observed-extrema sensitivity is not a confidence interval. No parameter fit, favorable outcome search, long simulation, held-out prediction test, physical time calibration, or identification with CF chemistry was performed.
