# Reproducing the finite research checks

These are constructed mathematical examples and selected checks of inherited results, not empirical data. Python 3 and its standard library are sufficient. No network or original reference workspace is required.

From the checks directory, run:

```sh
python3 formal_verify.py
python3 prior_checks.py
python3 core_counterexamples.py
python3 prior_schedule_guard.py
```

The first three scripts write their corresponding JSON result next to the script and print it. The schedule guard prints its JSON; compare it with prior_schedule_guard.json. Run in an extracted copy so the original archive stays unchanged.

The source snapshots are the user-provided prior research inputs captured for this session. Their manifest records original paths, capture time, and SHA256 digests. Links inside these frozen sources may refer to the original research workspace and are not rewritten. No remote primary texts or long extracts are bundled. Primary source URLs and findings are in the accompanying research record and synthesis.

The full simulator and cross-implementation experiment in next-test.md have not been run. These scripts are not replacements for that experiment.
