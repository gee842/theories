# Reproducing the integrated inquiry model

The numerical model, evaluator, and independent audits require Python 3.10 or later and only its standard library. Keep the delivered Python files in the same directory. The optional trajectory figure requires Matplotlib.

## Main evaluation

Run from the directory containing the delivered files:

```sh
python3 evaluate_integration.py --output reproduction
python3 audit_recorded_integration.py --records reproduction/integration-all-runs.jsonl.gz --output reproduction/integration-audit-results.json
```

The first command runs all 64 predeclared seed clusters, six scenarios, and five institutional policies: 1,920 runs. It writes summaries, a CSV, the first predeclared seed's traces, and all run records compressed as newline-delimited JSON. No parameter search occurs. The second command independently reads the saved records, reconstructs the comparisons' expected gains from the declared environment laws, and checks accounting and test arithmetic. That external truth is never given to the institution.

Each run has 700 requests per group. Primary failure counts are wrong completed services plus unserved requests, with both components retained. Means, ranges, and standard deviations describe simulation variation. They are not estimates of effects in human science.

## Implementation and governance checks

```sh
python3 audit_implementation.py
python3 check_purpose_policy.py > purpose-branch-checks.json
```

The implementation audit replays only development seed 1103 across the 30 scenario/policy combinations, instruments payment before acquisition and fitting, verifies transaction records, checks unavailable-capability and insufficient-funds boundaries, and compares behavior under normal and optimized Python. It writes `implementation-audit-results.json` next to itself. The second command exercises governance approval and rejection branches and saves its printed evidence.

Do not run these audit commands with `python -O`: their verification assertions are intended to execute. The production model's payments and decisions themselves were verified not to disappear under optimization.

## Figure

```sh
python3 plot_integration.py --records reproduction/integration-first-seed-traces.json --output reproduction/integration-trajectories
```

This writes PNG and SVG versions. Seed 800001 was designated before evaluation; the plotting program refuses a file containing a different seed. The figure displays three of the five policies for readability. The tables and recorded data include all policies.

## Files and evidence status

- `integration-freeze-manifest.json`: pre-evaluation hashes, parameters, scenario/policy list, seed list, outcome definition, and analysis plan. Its source names are preserved in the bundle.
- `protocol-v3.md` and `validation-plan.md`: final computational protocol and the earlier plan.
- `development-record.md`: corrections, constructed stress adjustments, and retained development failures.
- `integrated_model.py` and `purpose_policy.py`: executed community and council mechanisms.
- `evaluate_integration.py`: fixed evaluation and descriptive summaries.
- `audit_recorded_integration.py`: independent saved-record/statistical/financial audit.
- `audit_implementation.py`: instrumented payment and information-boundary audit.
- `integration-validation-results.json`, `integration-summary.csv`, and `integration-all-runs.jsonl.gz`: all evaluation evidence.
- `integration-first-seed-traces.json`: preselected example; includes full transaction ledgers for the full policy in all six environments. Other runs retain per-round intermediate minima, totals, and transaction hashes.
- `integration-audit-results.json`, `implementation-audit-results.json`, and `purpose-integration-checks.json`: audit evidence.

The complete bundle includes the development traces so the pre-freeze changes and failed expectations can be inspected. These traces are diagnostics, not part of the held-out evaluation.

Frozen numerical inputs were not changed after evaluation. Document writing and figure formatting followed inspection of the saved results. The final delivery manifest hashes the delivered files separately from the pre-evaluation source freeze.

The model's guarantee assumes independent draws from a stationary law during each atomic review. Deterministic hash-keyed pseudo-random streams make its simulated paths reproducible. Reproducing those paths verifies computation; it neither proves a deterministic tape is random nor validates the model as an empirical account of science.
