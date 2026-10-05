# Reproducing the correction-access study

Start with [the readable report](report.md). The raw results describe 90,000 policy episodes, generated from 2,000 independent paired evaluation seeds across nine worlds and five policies. This folder is the second continuation; it does not replace the earlier experiment's data.

## Saved evidence

- `protocol.json` states the assumptions, candidate settings, endpoint definitions and primary comparisons before fresh development and evaluation.
- `results/development.json` records all candidate scores; `selected.json` records the chosen settings. Both surprise thresholds select the lowest tested value, 1.5.
- `results/freeze.json` records source and selection hashes taken before evaluation. It is a local freeze, not an external preregistration.
- `results/all-results.npz` stores episode metrics, every purchase/alarm/fast-update flag, seed metadata, and dimension names. Dimensions of metrics are nine worlds × five policies × 2,000 seeds × 22 metrics. Event arrays additionally have 60 steps. No-change delay/recovery metrics are NaN by design.
- Forty-five `trace-*.npy` files store all 60 steps of the prespecified example, seed 30000; column names are in the NPZ. Unpurchased reference values are NaN. These examples were not selected for success or failure.
- `summary.json` contains the six adjusted primary comparisons and descriptive results. `diagnostics.json` and the anchor-mechanism note add explicitly post-evaluation interpretations without retuning.
- The independent audit uses a separately written vectorized scalar replay. It reconstructs all 72,000 scalar episodes, but does not independently rerun every three-state episode. Separate filter tests compare Gaussian posterior updates with batch conditioning.

## Environment and checks

The executed environment used Python 3.11.2, NumPy 2.4.6 and Matplotlib 3.11.2. Exact installed plotting dependencies are recorded in `requirements.txt`. Other versions may work; exact reproduction should use the recorded versions. No external data, credentials or network calls are required by the scripts.

In this folder, with the dependencies installed:

```sh
python -m unittest discover -p 'test*.py' -v
python independent-audit.py
python check_formal.py
python check_anchor_mechanism.py
```

The audit writes `independent-audit.txt`; mathematical checks regenerate their corresponding JSON records. The code and selected parameters must match the saved freeze hashes. The reported verification is 18 tests plus 5,355 audit assertions and separately enumerated mathematical checks. Assertion counts are checks, not independent empirical observations.

To redraw the figures and regenerate descriptive diagnostics from the saved data:

```sh
python plot_results.py
python diagnostics.py
```

The plots use descriptive 95% intervals based on paired seed averages where worlds are mixed. Those intervals differ from the multiplicity-adjusted primary contrast intervals. Missing post-change acquisitions remain outside the acquisition curve; censoring times are never plotted as observed events.

## Repeating development and evaluation separately

Keep the saved `results/` intact. The runner accepts a separate destination:

```sh
python experiment.py development --folder replay
python experiment.py freeze --folder replay
python experiment.py evaluate --folder replay
python experiment.py summarize --folder replay
python independent-audit.py --folder replay
```

This repeats the declared development and evaluation seeds; it is a reproduction, not new independent evidence. The new freeze timestamp and compressed archive bytes may differ while numerical arrays agree. Code changes or new algorithms should use a new protocol and fresh held-out seeds, not silently reuse these evaluation cases for selection.

All computation is free in the objective. Recorded timing covers complete simulation, not isolated thought or policy runtime. The study does not measure human performance, physical computation delay, actual memory or energy use.
