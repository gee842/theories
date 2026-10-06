# When an acquired receipt identifies its target

6 October 2026. AI-authored internal evidence and comparator check for **actual action/receipt → justified inference → retained record under outages and changed conditions**. This extends the [acquired-record evidence](ACQUIRED-RECORD-EVIDENCE.md) at its stated boundary. It installs no new decoder, policy, reward, process law or primitive axiom. All empirical, selfhood and ethical-grounding claims remain outside this computation.

## Existing source and new check

The original [prediction implementation](../../../../experiments/shared-renewal-capability/regulation/retention/formation/selectors/updaters/prediction/model.py) issues an action without access to the hidden regime or availability. Its plant returns a packet exactly when availability is true and the action matches the regime. The existing decoder labels success with the executed action and failure with its opposite. That label reaches a paid register write when resources permit. The source [protocol](../../../../experiments/shared-renewal-capability/regulation/retention/formation/selectors/updaters/prediction/PROTOCOL.md) already states that outage can make this decoder wrong.

The [new exact checker](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/learning/construction/prediction/check_receipt_identification.py) compares that decoder with a certainty-level partial inference **as analysis only**. Its [result artifact](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/learning/construction/prediction/receipt-identification-results.json) retains input hashes, all eight truth cases, finite-record counts, adaptive counterexamples, replayed source witnesses and a fresh reversal witness. The script writes only this new result file.

The old source hashes match the original [prediction results](../../../../experiments/shared-renewal-capability/regulation/retention/formation/selectors/updaters/prediction/results.json). The saved runtime artifact hashes and the unchanged micro-interpreter match the prior [runtime verification receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/learning/stochastic-prediction/runtime-verification.json). No old law, test or scientific receipt was edited. The broad eight-case/eight-arm suite and Lean builds were not rerun by this evidence check.

## What one observation establishes

Write \(a\) for the executed Boolean action, \(z\) for the regime at that trial, \(v\) for availability, and \(r\) for its actual receipt. The **existing** plant gives

\[
r=v\land(a=z).
\]

With availability unobserved and either value possible, the candidate set inferred from action and receipt is

\[
C(a,r)=\{z:\exists v,\ r=v\land(a=z)\}
=\begin{cases}\{a\},&r=\mathsf{true},\\
\{\mathsf{false},\mathsf{true}\},&r=\mathsf{false}.
\end{cases}
\]

Consequently success identifies the **contemporaneous** regime. Failure alone does not: the action may mismatch, or may match during an outage. The source decoder is wrong exactly in the second case. The independent Boolean check covers all eight triples \((a,z,v)\); the old decoder fails in two of those cases. Those are truth-table cases, not equally likely observations or an estimated error rate.

The analytical partial decoder returns \(a\) on success and abstains on failure. Every issued value is correct in the checked truth table. If availability is independently known to be true **for that trial**, the original opposite-on-failure decoder is also exact. Knowing that availability has probability three quarters is a different premise from knowing the realized availability bit.

An exposure in which no trial occurs does not create an action/receipt pair. Source expiry, absent hardware or inability to pay work must not silently enter the learner as observed failure.

## More records require a temporal premise

The checker enumerates **87,381 action/receipt records of lengths zero through eight**. Under a single stable regime and unconstrained unobserved availability bits, it compares direct compatibility with the separate closed form:

- No successful receipt leaves both regimes possible, regardless of which actions failed.
- Successful receipts all bearing one action identify that regime.
- Successful receipts bearing both actions contradict the stable-regime account. An empty candidate set is a detected incompatibility, not permission to assert either value.

It also checks the corresponding known-available case, in which each success or failure fixes a candidate through the original decoder. These are finite channel records, not assertions that the finite paid predictor can execute every enumerated record.

Adaptation alone does not guarantee identification. For all **128 deterministic action policies of depth three**, an all-failure history can occur under either fixed regime with suitable availability bits; the all-outage assignment is one explicit witness. Actions and observations then coincide across the two regimes. This bounded check supplies counterexamples; it neither asserts that outage is typical nor substitutes a finite enumeration for a general theorem about every policy or horizon.

## Identification is stronger than probabilistic evidence

Abstention is evaluated at the level of certainty from the specified fields. It does not show that failures carry no information. As a separate exact statistical illustration, suppose one stable regime has a fair prior, each of eight fixed action-0 trials is funded, and availability is independently sampled with known probability \(3/4\). Eight failures have likelihood \((1/4)^8\) under regime 0 and likelihood 1 under regime 1. Thus

\[
\Pr(z=0\mid\text{eight action-0 failures})=\frac1{65537},
\]

while both regimes remain in the logical support. The prior, sampling, stability and executed-trial conditions are explicit assumptions of this illustration, not additions to the generative process or hidden grounds for the partial decoder. Infinite evidence, source renewal and exploration would require further results. No superiority in learning, support acquisition or utility follows from making fewer categorical assertions.

## Reanalysis of saved operational outage histories

The checker selects the **830 distinct saved calls** tagged `inherited/outages/variable` from the existing compressed runtime-call artifact. Their availability parameter is \(3/4\). It replays the **6,640 positive-weight tape records** with the unchanged existing micro-interpreter and checks their complete saved successor states, all increments and status codes. This is a targeted reanalysis, not a new stochastic simulation or rerun of the broad suite.

| Quantity in this saved coverage set | Count |
| --- | ---: |
| Tape records containing an actual trial | 3,744 |
| Trial records with an ambiguous failed receipt | 2,532 |
| Actual paid write records | 3,664 |
| Paid writes based on an ambiguous failure | 2,452 |
| Paid writes using a label actually wrong about that trial's regime | 1,180 |
| Wrong decodes without a paid write | 32 |
| Successful receipts supporting a sound contemporaneous inference | 1,212 |

All 2,452 ambiguous paid writes changed the stored score, including all 1,180 writes using an actually wrong label. The other ambiguous writes happened to have the correct label; their accessible failure record alone did not certify it. The 2,896 no-trial tape records were excluded from the observation analysis. Concrete replay traces retain paid work, acquisition, write payment or refusal, actual score changes and later wear.

**These are coverage counts, not population frequencies or independent observations.** The saved calls are deduplicated by their input state and other call fields; their entrance probabilities are not carried in this artifact. Unused formation bits can also give repeated tape outcomes. We therefore do not divide the counts to report an error rate or sum per-call weights into a new expected whole-process result. The old all-history expected decoder-error count, \(174191759/603979776\) for the outage/variable case, is preserved separately with its original provenance; it is not estimated from these counts.

The partial inference would abstain on all 2,532 failed trial receipts, including correct but uncertain negative labels. It was not connected to an updater and its counterfactual resource trajectory was not run. Avoiding a false claim can leave learning blocked or postpone a useful response; the current check supplies no policy ranking.

## A true old success can become stale

The checker also replays an actual paid trial of the existing [typed predictor](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/learning/construction/prediction/check_model.py). Action true receives a packet, and the paid write raises its score from 2 to 3. The trial finishes. The existing `reverse` event then changes the regime from true to false while retaining that score and last command.

The earlier success still correctly identifies its own trial's regime. Treating its inferred bit as a fact about the current regime is now wrong. If the reversal and its semantics were independently known, negating the old bit would transport the inference; the existing controller is not given that knowledge. No contradiction in the old observation is required for its present applicability to fail.

## What this advances

The positive connection from actual writes to an acquired score remains valid as a causal statement. The new check determines an important missing qualification: **a causally acquired record need not be a sound inference, and a sound earlier inference need not still apply**. The underlying action, availability and regime distinctions must remain visible when joining acquisition to later action.

This is a bounded comparator for the common generative model and V7.3's evidence concerns. It does not contain strategic deception, concern, justified ends, general scientific discovery or an endogenous repair of the sensing architecture. The next construction must show how any availability evidence or change detection is actually obtained, paid for and used, without feeding the analyst's hidden regime or retrospective error label into the learner.

Reproduce from the repository root:

```sh
python3 experiments/integrated-correction/general-framework/generative-basis/lean/learning/construction/prediction/check_receipt_identification.py
```

All imported source and preserved artifact hashes are checked before analysis and checked again before writing the new result.
