# Access and attainable correction: reproduction materials

Second research cycle, 5 October 2026. This is a constructed finite-model study, not empirical evidence. The protocol was locally frozen before the main run; the analytical H2 witness was known before that run. No external preregistration is claimed.

The companion report and proof are delivered separately as `access-and-correction.md` and `access-proof.md`. The first-cycle evidence archive is separate and unchanged.

## Contents

- `work/access-study/PROTOCOL.md`, `protocol-freeze.json`: original frozen specification and its hash.
- `model.py`, `run_study.py`: exact-rational model and full main/control run.
- `inherited-model-snapshot.py`: provenance copy, not imported by the new computation.
- `results/inputs/` and `results/input-manifest.json`: exact main-run inputs and hashes.
- `results/main.json`: all 162 starting states and seven probe results, including exact metrics, first actions, and ledgers.
- `results/controls.json`: 30 control starts and seven probe results each.
- Other `results/*.json`: exact witness policies, partition comparisons, and run summary.
- `formal-access.md`, `formal_access_verify.py`, `formal_access_checks.json`: conditional proof, boundaries, and independent arithmetic checks.
- `implementation-audit.md`, `audit_*.py`, `audit_*results.json`: independent hidden-event oracle, comparison scripts, coverage and saved results.
- `plot_results.py` and `outputs/access-outcomes.{png,svg}`: optional scientific plot and rendered figures.
- `MANIFEST.json`: SHA-256 of each archived file except the manifest itself.

No remote paper body, task-local plotting libraries, environment, or cache is included. No reference-workspace access or network connection is needed for numerical reproduction. The provenance absolute path in the freeze record is descriptive only.

## Run

Extract into a fresh directory. Use Python 3.11 or later. All numerical scripts use the standard library. From `work/access-study/` run:

```sh
python3 run_study.py
python3 formal_access_verify.py
python3 audit_oracle.py
python3 audit_compare.py
python3 audit_controls.py
python3 audit_h4.py
python3 audit_no_output.py
python3 audit_summary.py
```

Scripts overwrite local result files in the extracted copy. Preserve the delivered archive to retain the original timestamps and checksums. The four deterministic main output files (`main.json`, `controls.json`, `partition-checks.json`, `two-period-witnesses.json`) should match byte for byte. Run durations, creation times, and thus hashes of run metadata can change. Audit scalar values and comparison counts should match; runtimes need not.

The main run contains 1,134 optimizations; controls contain 210. The independent oracle checks 4,536 H1/H2 base optima and 18 targeted H4 optima, not the entire H4 grid. It also checks control configurations across 5,184 states and independently optimizes 18,144 control H1 cases. `audit_summary.py` checks stored main scores and ledgers, partition counts, and access ordering; it does not independently reoptimize them.

Optional plotting requires Matplotlib (and its normal dependencies) in the Python environment. Run `python3 plot_results.py` from the extracted layout to regenerate the figures. The local `plot-libraries` preference is harmless when absent. The included output directory supplies the destination; no plot package is needed to reproduce numbers.

## Main interpretation

Equal total wealth fails to preserve the declared recovery problem under restricted access. Immediate pooling preserves operational laws under the assumptions proved in the formal memo, not merely because seven numeric probes agree. No selected main optimum buys a paid diagnostic, so this result concerns repair finance. Longer horizons, cross-domain transfer, and recognition/feedback studies remain unrun.
