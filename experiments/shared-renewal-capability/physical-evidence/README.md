# Ceroni source-data audit

This is an exploratory secondary descriptive audit of the public Supplementary Data 3 workbook for Ceroni et al., *Burden-driven feedback control of gene expression* (2018), [DOI 10.1038/nmeth.4635](https://doi.org/10.1038/nmeth.4635). It is not a preregistered prediction, experimental replication, or recovery of missing data.

Run [ceroni_audit.py](ceroni_audit.py) with Python and `openpyxl`. In the current Codex environment, from the repository root:

```sh
/Users/ren/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 experiments/shared-renewal-capability/physical-evidence/ceroni_audit.py
```

The script locates the repository from its own location, opens the preserved workbook with `read_only=True` and `data_only=True`, and writes [ceroni_audit.json](ceroni_audit.json). `--output /path/to/result.json` selects another output location. It never saves the workbook. The script requires its fixed SHA-256 hash to match before reading, checks the provenance manifest, and verifies the same source hash afterward. All expected observations are asserted; a failed check raises an error.

The calculations reproduce:

- S14a columns C–F, rows 1, 6, 13 and 20: original headings, 24-hour OD, fluorescence/OD, total fluorescence, ratios against C/H2, and the product identity. The feedback variants' workbook labels conflict with the plotted figure; the script retains column identities and performs no relabeling. Ratios across the three feedback columns survive a permutation of those labels, conditional on that being the extent of the source discrepancy. They are not confidence bounds. The product identity is arithmetic, not independent causal confirmation.
- S8 induced columns E/I/J, rows 5 and 33: triplicate means for growth and GFP production, with sample standard deviations and checks against the corresponding provided summary values. These are net package effects, not separately measured controller energetic costs.
- S8 uninduced D32 versus summary E34, and G5 versus summary K6: the provided summaries disagree with recomputed raw-array means. The audit reports the disagreement without choosing which representation is correct.
- Exact equality of cached cell values in the two 81-row `Fig S9 mean & stdev` and `Fig S13 mean & stdev` sheets, and inequality of the two raw sheets. This includes strings and empty cells over their combined dimensions; it does not compare formatting, hidden objects, or formula expressions. Repeated data do not become independent evidence because they appear on different sheets.

The full methods, observation-model limitations, source ambiguities and interpretation are in [the primary-source review](../../../_process/research/2026-10-05-support-and-shared-generativity/completion/PHYSICAL-EVIDENCE-CERONI.md). The [source manifest](../../../_process/research/2026-10-05-support-and-shared-generativity/completion/evidence/ceroni-2018/MANIFEST.json) records the publisher URL, exact original bytes and hashes. No source corrections, metadata reconstruction or author confirmation are claimed.
