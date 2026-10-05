# Frozen transfer test: queued software service

Constructed runnable software/simulator evidence; no people or observed production system. All source, mapping and decisions were frozen before calibration, and all predictions were frozen before 1,024 paired held-out seed clusters per regime.

The transported predictor remains exactly `R[f,a] = p[f] * q[a]`. The serious comparison is an independently implemented FIFO departure-time model, using separately measured primitive component distributions. Both receive local calibration, neither sees held-out integrated recovery before its prediction freeze.

| Regime | Transport max error | Transport decision | Queue model max error | Queue model decision |
|---|---:|---|---:|---|
| reserved_control | 0.0150 | equivalent | 0.0163 | equivalent |
| shared_fifo | 0.0248 | equivalent | 0.0134 | equivalent |
| urgent_fifo | 0.0282 | equivalent | 0.0049 | equivalent |

Practical tolerance: ±0.075. Simultaneous nominal 95% band half-width over all 12 primary cell residuals: 0.0391; domain model: 0.0392. Exact-agreement rejection and full intervals are in results.json. Equivalence requires every interval to fit inside the tolerance; rejection requires an interval wholly outside it.

| Regime/cell | Frozen p×q | Frozen queue model | Observed recovery | p×q residual |
|---|---:|---:|---:|---:|
| reserved_control / f0a0 | 0.3053 | 0.3040 | 0.3203 | +0.0150 |
| reserved_control / f0a1 | 0.6062 | 0.6079 | 0.5918 | -0.0144 |
| reserved_control / f1a0 | 0.4065 | 0.4046 | 0.4141 | +0.0075 |
| reserved_control / f1a1 | 0.8073 | 0.8089 | 0.8135 | +0.0062 |
| shared_fifo / f0a0 | 0.1278 | 0.1296 | 0.1191 | -0.0086 |
| shared_fifo / f0a1 | 0.3389 | 0.3302 | 0.3379 | -0.0010 |
| shared_fifo / f1a0 | 0.2084 | 0.1970 | 0.1836 | -0.0248 |
| shared_fifo / f1a1 | 0.5529 | 0.5316 | 0.5381 | -0.0148 |
| urgent_fifo / f0a0 | 0.0363 | 0.0410 | 0.0459 | +0.0096 |
| urgent_fifo / f0a1 | 0.0555 | 0.0410 | 0.0459 | -0.0096 |
| urgent_fifo / f1a0 | 0.0868 | 0.0563 | 0.0586 | -0.0282 |
| urgent_fifo / f1a1 | 0.1325 | 0.1577 | 0.1562 | +0.0238 |

| Regime | Predicted interaction | Observed interaction | Residual simultaneous interval |
|---|---:|---:|---|
| reserved_control | 0.0998 | 0.1279 | [+0.0034, +0.0528] |
| shared_fifo | 0.1333 | 0.1357 | [-0.0223, +0.0271] |
| urgent_fifo | 0.0266 | 0.0977 | [+0.0464, +0.0958] |

## Interpretation

The reserved/batched control satisfies the source factorization assumptions by construction; its agreement is a sanity check, not discovery. The shared-worker regimes probe the candidate bridge: diagnosis timing and its correlation with backlog change which deployment can finish before the deadline. A pooled scalar q measured on standardized local recommendations can discard those distinctions. Failure rejects this registered transport application. It does not refute the conditional probability identity, and adding queue state afterward would be a new model. The original predictions are retained unmodified.

The domain model has eight fitted primitive probabilities per regime plus explicit queue/clock rules. The transported predictor has four displayed gate probabilities but also needs proposal-timing histograms for calibration; those histograms and supplied scheduling rules are not free information. No explanatory compression or new fundamental law is established by this experiment.

p used diagnosis-only trials. q used enactment-only trials with a forced correct recommendation at a release time from the balanced pooled p-trial timing distribution, and a fresh independently generated workload. There is no diagnostic job in q calibration. This deliberately frozen bridge preserves timing marginals but discards diagnosis-induced backlog and time/backlog dependence. Consequently the confidence analysis conditions on that measured mixing distribution.

The bootstrap treats each four-cell outcome vector as one cluster. Bands are nominal, not an exact finite-sample coverage theorem; domain calibration uses a first-order delta approximation. Exhaustive finite-law checking below independently resolves structural discrepancies without relying on those sampling approximations.

## Independent checks

The object/worker target and independent FIFO-time recurrence agreed on 24,192 enumerated paths. Audit status: passed. The audit also checks accounting, inclusive deadlines, authority exclusion from diagnosis, and exact primitive probability mass. It was run after held-out evaluation. No source edits occurred after freeze.

| Regime | Oracle p×q max discrepancy from true integrated software law |
|---|---:|
| reserved_control | 0.0000000000 |
| shared_fifo | 0.0220773181 |
| urgent_fifo | 0.0315529836 |

These oracle calculations are predeclared checks of the constructed program, not fitted replacements for the frozen predictions. The deadline-miss, good-response, spending, and conditional recovery-time outcomes are recorded separately in results.json.

## Reproduce

Use Python 3 with numpy. In a fresh copy containing only protocol.md, service.py, queue_model.py, experiment.py and audit.py, run:

```text
python experiment.py freeze
python experiment.py calibrate
python experiment.py evaluate
python experiment.py audit
python experiment.py report
```

SHA-256 records: freeze.json and prediction-freeze.json. Raw independent local estimates: calibration.json. Per-cluster primitive shocks and all intervention outcomes: target.json. Audit details: audit-results.json. All numerical summaries: results.json. Source protocol paths and their assumptions are recorded in protocol.md.
