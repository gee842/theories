# Exact RNA partial-identification checks

The [research note](../../../_process/research/2026-10-05-support-and-shared-generativity/completion/RNA-PARTIAL-IDENTIFICATION.md) separates an identified conventional-model target from microscopic nuisance ambiguity and genuinely missing joint observations.

`exact_check.py` produces [exact-check.json](exact-check.json) using integers and rational arithmetic. It verifies:

- A new two-RNA restriction with the source's normalized C=300, D=5, T=2 and independent Poisson(10) starting counts. All coefficients within the two printed S23 rounding intervals yield the same 299 successful initial states. An analytic bound gives their crossing times below 320/279; the retained joint probability lies strictly between `86626371255287543892294575296/10^30` and `86626371255287543892294575297/10^30`.
- Two same-marginal-trajectory alternatives with different joint replacement probabilities, 1/10 and zero, under independent one-fifth retention.
- Exact diagnostic constructions attaining the new sharp mean-and-capacity bounds; the general theorem is proved in the note.
- Three existing paired source rows reused from the frozen audit, with their bulk-assay and normalization limitations retained.

Run:

```sh
/Users/ren/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 experiments/shared-renewal-capability/rna-partial-identification/exact_check.py
```

The only output written is this directory's JSON. All eight original source hashes and the prior audit/producer hashes are checked; no workbook extraction or scientific source-audit calculation is rerun. There is no original-notebook execution, numerical ODE solve, random simulation, fit, new measured probability, physical clock calibration, or microscopic RNA identification. The new model prediction's rounding robustness is not experimental uncertainty coverage.

The primary inputs remain in [source record 24](../../../sources/24-rna-network-evidence-2026-10-05/identification-addition/README.md), with original URLs, hashes and licensing notes. This directory adds no imported source bytes. The prior [identification audit](../rna-identification/README.md) and all older notes are preserved unchanged.
