# Recurrent inquiry and inherited evidence

Two exact finite-model calculations investigate maintaining inquiry across changing conditions and transmitting evidence to a successor. The [research synthesis](../../sources/15-codex-theory-conversations/2026-10-05-recurrent-inquiry-and-inherited-evidence.md) explains the findings and scope.

Module A chooses paid diagnostics, upkeep, and rebuilding through finite-horizon dynamic programming. Its sufficient belief is retained for free. Module B prices one evidence handoff and correctly infers from public cues, delivered messages, and silence. They are separate modules, not an integrated model of recurrent paid archives or endogenous purposes.

The exact two-period example maintains capacity without testing now, reducing expected total loss from 2 to 1.9. Eight exploratory longer cases compare adaptive capacity against all 128 fixed calendars, including the optimal calendar lottery under a matched expected inquiry expenditure bound. Four limiting controls have no adaptive advantage, including a stationary state with a perfect diagnostic added during review. A stationary but unknown state still permits an advantage when diagnostics can fail. The handoff calculation covers 117 combinations of evidence age, cue quality, and delivery reliability.

## Reproduce

From this directory, using Python with numpy, scipy, and matplotlib:

```sh
python -m unittest -v test_model.py
python analyze.py
```

The runtime used was `/private/tmp/meta-attractor-plot-env/bin/python`. The analysis computes exact finite-horizon expectations numerically; it does not run sampled trials or require random seeds. These are exploratory conditional illustrations, not preregistered or held-out evidence. Rerunning analysis replaces the current result files.

## Records

- [Protocol and decision interface](PROTOCOL.md).
- [Model and calendar linear program](model.py), [five verification tests](test_model.py), and [analysis and plotting](analyze.py).
- [Complete results, traces, model parameters, runtime versions, and source hashes](results/analysis.json).
- [Final input snapshot manifest](results/inputs/manifest.json), with byte-identical code, tests, protocol, and analysis alongside it.
- [Scientific figure](results/recurrent-inquiry.png), also available as [SVG](results/recurrent-inquiry.svg).
- [Initial exploratory grid](development.json) and [first analysis version](results-v1/analysis.json), with its [exact input copies](results-v1/inputs/PROTOCOL.md). The later revision clarifies the randomization proof and information interface, adds the stationary perfect-diagnostic control suggested during review, and improves figure labeling and layout. Existing case results are unchanged.
- [Mathematical audit](../../_process/history/2026-10-04-integrated-evolution/recurrent-inquiry-math.md), [design and implementation review](../../_process/history/2026-10-04-integrated-evolution/recurrent-inquiry-design-review.md), and [primary-literature audit](../../_process/history/2026-10-04-integrated-evolution/recurrent-inquiry-prior-art.md).

The procurement cap covers inquiry, not operating responses; both expenses enter total loss. The controller does not observe realized untreated harm. Exposing that outcome would create additional information and change the model. No real institution, deployed AI, new candidate-generation process, or unrestricted concept formation is tested here.
