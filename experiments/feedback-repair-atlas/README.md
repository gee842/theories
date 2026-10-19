# Feedback and repair atlas

A worked application of the Becoming proofs: explore how different retained
histories, gradual supporting evidence, defensive lapses and retries interact
under explicitly supplied toy response laws.

Open [index.html](index.html) locally, or serve this directory:

```sh
python3 -m http.server 8000 --directory experiments/feedback-repair-atlas
```

The page is self-contained: no accounts, API calls, network assets, paid services,
or external JavaScript packages. Browser choices are stored locally when storage
is available. The trial is also [hosted for exploration](https://feedback-atlas.157-245-144-73.sslip.io/).

## Six levels, with the same episode selected

1. **Raw Lean:** inspect the actual imported components and application proofs.
2. **Abstraction:** inspect the exact history-to-tally projection.
3. **Two people:** replay exchanges, supporting experiences, setbacks and retries.
4. **Evidence and repair:** distinguish a task error from a personal attack.
5. **Team:** an explicitly unproved extension to coordination and repair practices.
6. **Society:** an explicitly unproved extension to institutions and wider effects.

The same course and completed-exchange count remain selected across levels.
Choose a preset or branch from any step using clarification, habit, or a defensive
lapse. Retry is an explicit control input; its availability is assumed.

## Premises and conclusions

Alex needs three supporting-evidence units before his own habitual response
changes; Maya needs two before offering specifics habitually. Supporting
experiences add one, defense subtracts two (six in the severe-setback course), and
unresolved experience preserves the tally. These are stipulated weights, not
measured trust, probabilities, psychological harm, or maturity scores. Receptivity,
credible engagement, capacity and safety to clarify remain separate assumptions.

An early lapse can re-enter the habitual defensive region. A new clarification
can restart repair when the required conditions hold. A later lapse can leave
Maya above threshold so her next cue permits Alex to engage before his own
expectation changes. Repeated or larger setbacks can remove that margin.

These are mathematical consequences of the supplied rules, not validated laws
of human behavior or obligations to tolerate mistreatment. Evidence of a task
error does not establish that delivery was nonpersonal. The team and society
levels are interpretation proposals and carry no inherited formal guarantee.

## Proof composition and boundaries

The unchanged application sources are in [model/](model/README.md):

- `FeedbackReadingTrial.lean`: observational ambiguity and evidence refinement.
- `InteractionHistoryTrial.lean`: coupled histories and an earlier one-exchange
  learning rule, retained at its original scope.
- `GradualInteractionTrial.lean`: accumulated evidence, thresholds, setbacks,
  retry, and exact abstraction for every finite response plan.

The gradual application imports `wholeNext`, `Readout.foldl_semiconj`,
`ExchangeLaw.sub_add_back`, and `Copying.le_sub_of_add`. It adds no core theorem,
result registration, or claim of empirical validity. This packages the earlier
uncommitted study trials into an executable experiment without changing their
Lean statements. No physical conservation law is imposed on human experience.

## Reproduce

Python 3's standard library builds the page. Node.js runs the browser-dynamics
tests. Lean 4.29.1 is required only to reproduce the formal application checks.
From the repository root:

```sh
LEAN=/absolute/path/to/lean python3 -B experiments/feedback-repair-atlas/model/verify.py
LEAN=/absolute/path/to/lean python3 -B experiments/feedback-repair-atlas/model/verify_interaction.py
LEAN=/absolute/path/to/lean python3 -B experiments/feedback-repair-atlas/model/verify_gradual.py
python3 -B experiments/feedback-repair-atlas/build.py
python3 -B experiments/feedback-repair-atlas/build.py --check
node --test experiments/feedback-repair-atlas/tests/dynamics.test.cjs
python3 -B -m unittest discover -s experiments/feedback-repair-atlas/tests -p 'test_*.py'
```

The local checks compile the imported closure, reject compiler warnings, and
audit axiom dependencies of every source declaration in each application. They
are not the package's full environment/purity audit. Source-bound receipts live
beside the model, with build artifacts ignored under `.build/`.

`components.json` binds displayed source excerpts by path, line range and SHA-256.
`build.py` rejects changed source, changed verifier scripts, invalid receipts,
or stale transitive hashes. After reviewing and checking a source change, update
the affected excerpt binding and rebuild. Do not refresh hashes to silence a
failure. `src/dynamics.js` supplies the executable interpretation; tests compare
its courses with the Lean examples and exercise absent conditions and retained
history. They do not establish a formal Lean-to-JavaScript compilation theorem.

The static page is generated from `src/atlas.fragment.html`, `src/dynamics.js`,
`src/shell.html`, component bindings, and verified source excerpts. No Codex
plugin, local visualization folder, or particular user's home path is needed.

The path-filtered `Feedback atlas` CI job checks the deterministic page, source
and receipt bindings, and executable dynamics. It does not install Lean or rerun
the formal compiler; reproduce those checks explicitly with the commands above.
