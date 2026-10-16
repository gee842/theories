# Situated discovery with paid evidence and separate decision gates

This synthetic experiment implements the next step after the [two-frame model](../../sources/15-codex-theory-conversations/2026-10-05-formation-and-revision-of-frames.md): the learner constructs candidate contextual distinctions from records and tests proposed actions on fresh randomized cases. It is not given the simulator's hidden rule or a prevalidated correction.

The held-out evaluation used 256 independent seed clusters, fourteen institutional arms, and hazard-present/absent conditions: 7,168 paired trajectories, not 7,168 independent replications. The [research synthesis](../../sources/15-codex-theory-conversations/2026-10-05-discovery-before-demonstrated-returns.md) explains the results, exact budget constraint, controls, and limits.

In this selected benchmark, protected inquiry validated and deployed the useful contextual policy by block 24 in 256/256 hazard worlds. No-standing and no-authority arms had identical first validation evidence but no deployment. No policy was accepted in 256 absent-hazard protected runs; inquiry nevertheless cost 150.49 units per run. The severe funding control was mathematically unable to finish a test, while less severe schedules produced eventual but late evidence. A calendar cutoff defines timeliness; it is not physical irreversibility.

## Records

- [Protocol](PROTOCOL.md), including development decisions and scope corrections.
- [Frozen evaluation inputs and SHA256 manifest](evaluation-inputs/manifest.json).
- [Simulation](experiment.py), [mechanism tests](test_experiment.py), and [analysis](analyze.py).
- [Evaluation summary](results-evaluation/summary.json), [per-seed records](results-evaluation/runs.jsonl), and [audited analysis](results-evaluation/analysis.json).
- [Scientific figure](results-evaluation/discovery-results.png), also available as [SVG](results-evaluation/discovery-results.svg).
- [Initial development results](results-development-v1/summary.json) and [expanded development results](results-development/summary.json). Each development directory retains its exact simulation and protocol inputs.
- [Mathematical audit](../../_process/research/2026-10-04-integrated-evolution/candidate-discovery-math.md), [design review](../../_process/history/2026-10-04-integrated-evolution/candidate-discovery-design-review.md), and [prior art](../../_process/history/2026-10-04-integrated-evolution/candidate-discovery-prior-art.md).

## Reproduction

Python with numpy is sufficient for simulation and tests; analysis also uses scipy and matplotlib. The runtime used was `/private/tmp/meta-attractor-plot-env/bin/python`.

```sh
python -m unittest -v test_experiment.py
python experiment.py --phase evaluation
python analyze.py
```

Run evaluation in a fresh copy without generated `results-*` directories, retaining `evaluation-inputs`. The simulation checks frozen input hashes and refuses to overwrite an existing run file. The four tests exercise the 60 possible planted conjunctions on an exact diagnostic distribution, useful nonexact policies, the confirmation criterion, resource balances, record loss, and paired decision gates.

## Scope

The learner expands a model within a finite supplied grammar. Purposes and actions remain fixed. The environment has independent units and delayed reports, not accumulating physical damage. Funding follows a declared pre-validation calendar schedule; it is not a learned general budgeting rule. Retention expires unlinked metadata; linked records and models persist without further payment. Trial rights remain available under the deployment veto. Experimental design and code reviews were performed by AI agents and are not human peer review. No real institution or deployed AI was tested.
