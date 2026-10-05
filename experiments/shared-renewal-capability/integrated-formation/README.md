# Integrated formation and full carrier turnover

This experiment checks the selected path and rational certificate in [Formation and full carrier turnover](../../../_process/research/2026-10-05-support-and-shared-generativity/completion/INTEGRATED-FORMATION-RENEWAL.md).

The generator is the previously proposed N=4 material-fabricator model. All competing A0/A1 formation and copying, gate binding and wear, plant reactions and leakage are included in the event table. The parameter family is derived analytically; no simulation or parameter search is used.

The [checker](exact_check.py) validates the six formation events and 21 full-turnover events, including the tagged original-Y loss, all exit-rate polynomials, exact material/work accounting and the common-event branch bounds. The [saved result](exact-check.json) passed. Its floating-point value is only a display approximation; all inequalities use rational arithmetic.

To reproduce from the repository root:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 experiments/shared-renewal-capability/integrated-formation/exact_check.py
```

Running writes only this directory's `exact-check.json`. Source and checker hashes are recorded in that output.

The certificate uses eight fresh captures overall, six for full turnover, and deadline 27. The favorable-branch lower bound is about **1.24 × 10⁻²¹**. Its sufficient algebraic witness has **m ≈ 2.43 × 10²¹**, with some rates m³. This is a finite mathematical existence result with a strict comparison for the whole declared joint event. It is not a calibrated reaction system, reliable renewal demonstration, architecture-prevalence result or thermodynamic validation. The six-packet minimum belongs to the stated work ledger.
