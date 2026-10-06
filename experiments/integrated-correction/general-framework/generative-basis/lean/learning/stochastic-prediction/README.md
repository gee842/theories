# Exact stochastic prediction exposures

This package connects the actual [prediction exposure program](../../../../../../shared-renewal-capability/regulation/retention/formation/selectors/updaters/prediction/model.py) to a finite weighted Lean law that retains failed opportunities, optional writes and actual successor resources. It discharges this program's probability/completion interface; it does not establish reliable learning, renew its source or construct the supplied learning circuit.

The [formal protocol](PROTOCOL.md) was frozen before implementation. The independent [runtime checking protocol](CHECK-PROTOCOL.md) and its receipts preserve a separate prospective specification. The brief protocol was accidentally overwritten during ownership coordination, then restored byte-for-byte to its original recorded hash; the numerical protocol was preserved separately before numerical execution.

## What the formal law covers

[Exposure.lean](Exposure.lean) includes all eight existing arms and the complete callable exposure: gate assembly, base formation and prior, retrofit, rent, failed-rent reset, no-work exit, action, receipt, optional paid or sham write, and wear/renewal. Its operational state retains fuel, gate kind/lifetime, assembly stage/predictor lifetime, score, last command and written flag. Historical `prelearn`, `stale`, `corrected` and `witness` fields affect diagnostic reports only. The independent runtime check also compares those fields and every increment; the Lean operational projection does not silently present them as proved coordinates.

A no-work exposure still loses its scheduled source packet. An unaffordable write retains the actual continuing carrier, changes its last-action register and lifetimes, and can be followed by productive work. Neither outcome becomes an artificial absorbing death.

[FiniteExposureKernel.lean](FiniteExposureKernel.lean) gives each exposure two fair formation bits and availability weight `k/N`. Unused bits are summed rather than discarded. Its eight weighted tape outcomes total `4N`; a finite schedule of length `m` has total weight `(4N)^m`. Probabilities are these natural weights divided by that positive denominator. The proofs retain every actual intermediate state, establish the account on every supported history, and compose any supplied inherited mixture without dropping its unsuccessful states. Given at least `m` initially provisioned packets, the closed account is

`final common + remaining packets × packet size + all spent + all waste = initial common + initial packets × packet size`.

This is a finite independently sampled tape law with a supplied external regime schedule. It is not a theorem about arbitrary adaptive sampling or unknown physical randomness. The generic equality lemma preserves literal weighted-list equality; it is sufficient for measure equality, not a new theorem about all duplicate-merged quotient kernels.

The broader natural-number account permits parameters and states outside the Python source domain. Runtime correspondence requires its positive tariffs, bounded scores/lifetimes/stages, and coherent live gates: positive gate lifetime implies gate code 0 or 1. Absent gate code 2 maps to Python −1 and is not permitted as a live updater. [ExposureExamples.lean](ExposureExamples.lean) names these separate source restrictions and proves coherence is preserved. Finite checks do not assert universal refinement of arbitrary Python inputs.

## Relationship to the previous trial proof

[PredictionOverlap.lean](PredictionOverlap.lean) imports the unchanged [PredictionAction](../../../../../../shared-renewal-capability/regulation/retention/formation/selectors/updaters/prediction/formal/PredictionAction.lean). On installed machinery, availability true and the old rent/work/write/finish guards, it proves equality of the operational successor, actual receipt, spent/waste and one-packet debit. Both matched and mismatched commands are covered. A failed capture may end with zero lifetime when the pre-finish guard held. The old state has no written flag; its separately supplied augmentation becomes true after the actual paid write.

The new law is not globally identical to that old phase relation. Checked counterexamples show that the old law stays observed when writing is blocked, and retains its source packet when work cannot begin. The callable exposure returns a worn continuing state in the first case and expires the scheduled packet in the second.

With common fuel 8, write price 6 and availability 1/2, a first miss leaves fuel 4 without a write; a later receipt pays the write and leaves fuel 2. The two-call law gives second-capture probability 1/2. Keeping only histories whose first write succeeded leaves probability 1/4 for that event. Score remains zero throughout this witness: it demonstrates productive continuation and later paid writing, not changed prediction. This formal fixture also illustrates write-conditioned receipt selection. The independent runtime's fuel-4/write-1 selection fixture is a separate case with the same selection problem.

## Verification and scope

[verification.json](verification.json) records the pinned Lean 4.29.1 fresh build, frozen dependency sources, compiler/checker/log hashes and axiom audits. Every theorem newly declared in this package is audited; inherited modules retain their recorded audit sets. The proofs use Std and inherited repository modules, with no custom axioms, unfinished proofs or native decision shortcut. Standard kernel-checked `decide` evaluates finite examples.

[check_runtime.py](check_runtime.py), written independently of the Lean transition implementation, compares complete 12-field Python successors, all 17 increment coordinates and exact branch masses. It also compares all 64 inherited case/arm endpoint laws and weighted cumulative first moments, retaining failed preparations. Its [runtime receipt](runtime-verification.json) records 15,985 distinct calls, including 9,600 prescribed guard calls and 7,702 reachable invocations (overlapping coverage categories). All 38,412 distinct positive-weight operational tape fixtures agree with the compiled Lean evaluator. The source-bound [results](runtime-results.json), compressed calls/fixtures and prefix traces preserve this finite coverage. These checks establish no empirical validation or universal Python-language theorem.

Run `python3 check.py` here for the formal build. Run the separately documented runtime checker only when its source/dependency changes or an unresolved concern warrants repeating it. The final receipts distinguish mathematical proof, finite compiled correspondence, and source-audited projection.

The supplied costs, construction repertoire, action/receipt channel, primitive gate/prior sampling and source schedule remain premises. Outage can make the controller's negative receipt label wrong. A preserved distribution does not make that decoder correct or the acquired samples iid; no concern coefficient, ethical objective or favorable long-run direction is inferred here.
