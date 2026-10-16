# More retained evidence helps under a stable world and can mislead after change

5 October 2026. The [protocol](PROTOCOL.md) was fixed before these calculations. [Code](analyze.py) and [complete numerical results](analysis.json) enumerate the finite distributions without trajectory sampling or probability pruning. Twenty-six checks pass; maximum mass discrepancy is7.00×10⁻¹⁵. All procedures receive exactly60 query cases and60 record-work slots. This is a supplied-model comparison, not empirical validation of the model family or an autonomous governance system.

## Stationary evidence changes the error pattern

| Procedure | Correct retained declaration after60 cases | At least one wrong declaration during12 looks |
|---|---:|---:|
| Latest five-case batch, always replace |85.11075%|85.55182%|
| Cumulative evidence, always replace |99.999975%|16.70105%|
| Cumulative sequential certificate |99.999952%|0.842910%|

The latest-batch rule repeatedly discards usable evidence. Its isolated five-record accuracy stays.8511075, and repeated independent replacement makes an error somewhere very likely. Cumulative replacement becomes extremely accurate at the endpoint, but it still makes early mistakes. The certificate sharply reduces early false declarations by sometimes withholding a declaration: after the first five records,62.5875% of its probability mass remains undeclared. Withholding does not supply a safe response to pending cases.

The stationary theorem is stronger than this finite table: in the correctly specified four-hypothesis family, the chance of **ever** declaring a wrong expression is at mostδ=.05, sharpened here to3/81≈.03704 by the discrete likelihood ratios. The observed finite probability.00842910 is below that conservative bound. Cumulative maximum-likelihood replacement also has summable error probabilities under continuing stationary evidence, so only finitely many mistakes occur almost surely. These are distinct assurances: eventual correctness does not mean no early errors. The [formal note](FORMAL.md) proves both statements using established probability results.

## An unannounced reversal invalidates the pooling premise

In the second scenario the physical expression changes from X1 to1−X1 after case30. The procedures are not told. Every other parameter and the complete60-case work budget remain the same.

| Procedure | Correct retained declaration after60 cases | At least one wrong declaration over the run |
|---|---:|---:|
| Latest five-case batch, always replace |85.11075%|85.55182%|
| Cumulative evidence, always replace |17.14336%|99.999998%|
| Cumulative sequential certificate |7.06436%|99.96269%|

This is **not a counterexample to the stationary theorem**. There is no single true fixed hypothesis generating all pooled records after the reversal, so the likelihood-ratio martingale premise fails. The certificate can confidently restate an obsolete account and later select misleading alternative features. Greater accumulated confidence does not establish that the retained response family still describes the current situation.

The latest-batch procedure is more responsive in this particular abrupt-change test because its next full batch contains only post-change evidence. That does not make it universally preferable: the first table shows its persistent false-replacement burden in the stationary case. Neither procedure is tuned after seeing the reversal, and no change-aware method is claimed to have been tested.

## A stale declaration and a new false declaration are different events

The computation keeps separate event monitors that the decision rule cannot inspect.

- Immediately after the reversal, before any new record or declaration, the certificate's held label is wrong with probability99.96534%. Its historical probability of having made a false declaration is still only.84260%; the reversal does not retroactively make an earlier truthful statement false when it was made.
- At the first subsequent look, after case35, it **freshly certifies a currently wrong expression** with probability98.64185%. Another1.34067% merely retain a wrong expression without issuing a new certificate at that look;1.32618% are specifically holding a declaration that was correct when last made.
- At case60, a fresh wrong certificate occurs with probability49.35931%, and43.57628% hold a wrong expression without a new certificate. These sum to the92.93559% current wrong-declaration probability, apart from rounding.

Thus the post-change failure is not merely a stale-label bookkeeping artifact. Under its violated premise, the old likelihood model can actively justify new false assertions. The distinction also prevents interpreting silence as a fresh false certification.

## The data budget is equal; the supporting obligations are not erased

Every procedure consumes120 effort units:60 query cases plus60 record slots. Each randomized inquiry has expected physical harm.50 and action-1 use.50, so every arm incurs expected30 query harms and30 action-1 uses. A confidence certificate does not reduce these costs in this fixed-budget experiment. Early stopping savings were not credited.

Retaining two cumulative counts through60 cases requires12 counter bits versus6 for two five-case counts. These figures exclude the shared semantic labels, sample count/clock, computation, declaration and monitoring machinery. Reliable retention and arithmetic are explicit available-capacity assumptions, not demonstrated self-renewing services. Over an unbounded run, cumulative evidence requires growing counters and indefinitely supported inquiry unless the institution stops; stopping preserves a stationary certificate's validity but provides no warning of later change.

The original strict harm floors also expose a separate obstruction. Blind initial responses have opposite-group harms summing to1; they cannot both be below.50. Randomized query has harm.50 in every group. The original operating repertoire has no harmless abstention action. Consequently these procedures offer **epistemic assurance**, not whole-behavior safety or legitimate permission to conduct harmful experiments. Those obligations cannot be supplied by renaming uncertainty control “alignment.”

This result identifies an avoidable source of recurrent errors—discarding accumulated evidence—and an equally consequential limit—continuing to pool evidence after its generating conditions change. The next question is how an institution can maintain justified tests of its own retained assumptions, with paid time, detection delay, false alarms, and consequences for those subjected to investigation. No untested answer to that question is counted as a result here.
