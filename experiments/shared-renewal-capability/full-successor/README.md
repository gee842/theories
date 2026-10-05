# Complete first replacement across the actual formation ensemble

This continues the unchanged unit-coefficient CF law from R3,Y1,F2. The [result](../../../_process/research/2026-10-05-support-and-shared-generativity/completion/FULL-SUCCESSOR-RESULT.md) defines the whole-entrance first-turnover and reserve-restoring events. Both include unsuccessful formation and replacement. Entry-gate classes are outcomes within one law, not interventions.

The [protocol](PROTOCOL.md) records the targets, numerical cap refinement and execution-order deviation. [model.py](model.py) supplies the labelled carrier lift; [compute.py](compute.py) builds the complete intercepted-entrance and first-successor graph. [results.json](results.json) contains the floating H1,H3,H10 outputs, including successor gate types and entry reserves0–3. Its original protocol is preserved in [development](development/PROTOCOL-before-certification.md); the later directed calculation adds reserve4 for tighter error control without rerunning these floats.

[certify.py](certify.py), using [fixed.py](fixed.py), supplies directed H10 probabilities at 96-bit fixed-point precision. [certificate.json](certificate.json) records exact rational bounds for all relevant queries and their composition. The unconditioned gate0-minus-gate1 contrast is negative for complete turnover (about−1.748e−14) and positive for reserve-restoring turnover (about1.194e−15). The certificate includes free-packet overflow and omitted-entry mass. The complete event remains very rare, about1.84e−11 across both entry gates.

The [independent carrier check](carrier_check.py) and [record](carrier-check.json) verify all 42 channel projections and the already-worn-slot quotient by exact affine arithmetic. [Arithmetic checks](arithmetic-check.json) compare the limb division with independent arbitrary-precision scalar calculations in 4,200 boundary/random cases. Analytic audits supply the general carrier, tail and arithmetic arguments. These are distinct from empirical validation or an end-to-end Lean proof.

To reproduce from this directory with NumPy/SciPy available:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 carrier_check.py
PYTHONDONTWRITEBYTECODE=1 python3 arithmetic_check.py
PYTHONDONTWRITEBYTECODE=1 python3 compute.py
PYTHONDONTWRITEBYTECODE=1 python3 certify.py
```

Each command replaces its corresponding result record. The certifier also reads the frozen independent [reserve-bound record](../full-successor-critique/exact-check.json). It can take several minutes and reports progress. The original calculation and independent read-only reviews are described in the [review](../../../_process/research/2026-10-05-support-and-shared-generativity/completion/FULL-SUCCESSOR-REVIEW.md).

Restoring free reserve does not restore an external source, renew all supplied apparatus, or guarantee future operation after the first successor. The existing finite-source seven-capture certificate cannot automatically be applied to this unrestricted event. Physical identification, reliable repeated operation and broad capability direction remain open.
