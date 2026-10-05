# Evidence package for feedback and successor experiments

Task date 5 October 2026. The accompanying report explains the findings and limits. This package preserves the original experiment inputs and results. It contains actual AI task responses and constructed simulator outputs, not human observations.

## Contents

- live contains the locally frozen protocol, input generator, frozen scoring and analysis, 32 lineage folders, randomized assignments, all 128 submitted responses, the combined live results and audits.
- transport contains the separate queue service, its independent conventional predictor, local calibration, frozen predictions, all paired target seed data, the finite-path audit and a labeled post-run exact rank deduction.
- prior-designs preserves the human handoff proposal, transfer proposal and foundational audit that motivated these experiments, with their source paths and hashes.
- MANIFEST.json inventories the packaged files by SHA256. It does not authenticate the experiment independently of the orchestrator.

The live participant identities are an orchestrator record reconstructed from actual dispatches. They are not an independently authenticated platform log. Participants were instructed to access only their own prompt and response; no operating-system sandbox or full tool-trace forensic audit is claimed.

## Recompute saved live data

Run `python live/analyze.py` after extraction. Python's standard library is sufficient. The result regenerates live/results.json from all recorded responses and assignments. The code uses the package's location, so the original absolute participant prompt paths are not needed for scoring. The exact randomization inference treats the founder lineage as the unit.

The original model responses are data. Running new AI participants with the saved prompts would create a new experiment and may produce different responses. The historical generator, assignments and prompts should not be overwritten during reanalysis. A genuine rerun must preserve the old data and use a new output directory.

## Recompute the simulator

Follow transport/RESULTS.md in a fresh copy of the original source files. The experiment requires Python and NumPy; audit.py and the exact rational calculations use the standard library. The main experiment's source hashes were frozen before calibration, and predictions were frozen before the target run. No original code or acceptance threshold was changed after observing outcomes.

The post-run determinant certificate is a deduction from the predeclared finite software law. It is not an additional held-out prediction or a revised practical success criterion. The simple model passed the registered 7.5 percentage-point tolerance in all three regimes even though exact factorization fails in the shared-worker regimes.

All files remain research evidence for the stated tasks. They do not constitute external preregistration, independent human peer review, an institutional field trial or validation of a universal theory.
