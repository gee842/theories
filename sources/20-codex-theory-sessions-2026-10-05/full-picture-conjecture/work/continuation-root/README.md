# Evidence for protected continuation and recurring progress

Prepared 5 October 2026. This bundle accompanies `conditions-for-continued-generation.md`, `continuation-proof.md`, and `progress-proof.md` in the delivered outputs.

The proof work applies established safety, Büchi-game, and obligation-monitor mathematics. It claims no mathematical priority, proof-assistant certification, empirical universality, or proof of unlimited meaningful novelty. Reviews were performed by separate agents, not independent human researchers.

## Contents

- `formal-continuation.md`: finite safety theorem, arbitrary-set existence, finite-action horizon result, countermodels, and exact partial-observation recurrence construction.
- `progress-and-sources.md`: fully observed recurring-progress theorem and rank certificate, hidden-progress extension, primary-source locations, and novelty boundaries.
- `root-bridge-audit.md`: connection to the wider philosophical proposal and the distinctive claims not supplied by the transition schema.
- `formal_continuation_verify.py`, `progress-check.py`, `partial_progress_verify.py`, and their JSON results: separate finite constructions, exhaustive oracles, and concrete controller certificates.
- `TARGET_PROTOCOL.md`, `TARGET_SPEC.md`, the two freeze files, `target.py`, calibration JSON, `composed_predictor.py`, `frozen-predictions.json`, `target_evaluator.py`, and outcome/comparison files: the new synthetic queue challenge.
- Review files and `review-resolution.md`: exact scope and applied corrections.
- `manifest.json`: SHA-256 hashes for all other payload files.

## Reproduction

Use Python 3 with its standard library in an extracted copy of this bundle. The scripts rewrite result JSON in that copy; they do not modify the original archive or reference repositories. They do not access the network.

```
python3 formal_continuation_verify.py
python3 progress-check.py
python3 partial_progress_verify.py
python3 composed_predictor.py
python3 target_evaluator.py --run-after-freeze
python3 target_comparison_audit.py
```

The first three checks are independent and can run in parallel. The last three form a sequence: composed predictions, separate target evaluation, and comparison analysis. The already saved freeze files document the original order and hashes; rerunning in an extracted copy is a reproduction, not a new prospective freeze.

## What the target checks

The 864 prediction vectors were locally frozen before the integrated target policies ran. The source probabilities were exact synthetic component fixtures, not real-world measurements. All 6,048 registered outcome coordinates matched. The coarse deadline-free description was expected to fail. The result does not complete the earlier two-gate factorization study or establish an advantage over a conventional model with the same complete mechanisms.

The mathematical checks concern sure guarantees under specified transition and observation rules. The queue results concern finite-horizon probabilities for four registered policies. These are different claims, and their verification must not be exchanged.
