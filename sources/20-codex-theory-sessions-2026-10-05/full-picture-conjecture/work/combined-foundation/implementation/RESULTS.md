# Exact combined-process results

Every reachable support transition was enumerated; unsafe states were retained. These are exact results for the supplied finite process, not sampling estimates.

| Condition | States | Edges | All prefixes protected | Sure recurring ordinary service (both contexts) | Competent succession recurs |
|---|---:|---:|:---:|:---:|:---:|
| baseline | 486 | 506 | yes | yes | yes |
| record_loss | 204 | 220 | yes | no | yes |
| execution_blocked | 486 | 506 | yes | no | yes |
| no_renewal | 18 | 18 | yes | no | no |
| no_maintenance | 230 | 250 | yes | no | no |
| no_training | 230 | 250 | yes | no | no |
| score_capture | 315 | 331 | no | yes | no |
| misleading_calibration | 486 | 506 | no | no | yes |

The baseline has 486 reachable states and 506 actual transitions. Its smallest boundary balance is 2 and smallest balance immediately after a debit is 1. All six required events pass both the strict decreasing phase-rank certificate and an independent event-deleted cycle test. Each event therefore occurs at least once per 23 microsteps on every admitted infinite path. The initial evaluator actually changes after a failed fresh check; that judgment program then survives paid maintenance, training and transfer. Recurrent evaluator rewriting is neither needed nor claimed.

All conditions pass ledger and event-truth checks. Fail-closed conditions can remain protected while losing delivered service. Score capture and misleading calibration allow wrong ordinary responses and preserve the resulting public harm flag. The latter control gives internally consistent but physically false strict certificates, demonstrating the dependence on the stated reliable calibration premise.

The score-capture row is instructive: correct services in each context can recur while wrong services also occur. Recurring correct outcomes alone do not establish protection. Only the baseline passes protection together with all six required recurrence conditions. The earliest public violation in either unsafe control occurs after 17 microsteps. Archive maintenance and training remain operational in the record-loss control, so institutional succession alone does not guarantee the right acquired program.

Every decision is a function of the explicit Observation object, which excludes hidden truth and the assessment flag. The exhaustive hidden-field perturbation check covers 19640 cases. This checks implementation access; it does not show that this controller is optimal or that diagnosis is universally necessary.

Reproduce with `python3 verify.py`. Graph exports contain full state records, every edge, payments, receipts, spill, actual event labels, and initial states. `results.json` also records the shortest harmful prefix for each unsafe condition. See MODEL.md for the finite grammar, safe calibration, within-period stability, supplied productive inputs and all other scope assumptions.
