# Interrupted controlled change and recovery

The [existing study continuation](../../../../../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/MEDIATED-CONTROL-INTEGRATION.md#9-interrupted-change-and-recovery--中断改变与恢复) records the exact delta, inherited results, relational interpretation, counterreview and source assessment.

```sh
python3 check_recoverable_control.py
```

[RecoverableControl.lean](RecoverableControl.lean) stages the existing mediated overwrite program. A protected durable pending description precedes actual writes. Ordinary use is blocked while pending; crashes retain effects and consumption, reset progress for replay and add a supplied delay. An uninterrupted suffix with sufficient work and time publishes after the remaining writes plus one step. `Safe` means evidence coherence, not general harmlessness or guaranteed corrective access.

[Current receipt](recoverable-control-verification.json): **22 new Lean theorems / 48 explicit declaration audits / 27,888 finite matches**. Nine inherited proof modules and one inherited case helper are freshly compiled but not recounted. Standard axiom dependencies are recorded for each declaration. Sources, compiler, scanner, signatures and finite outputs are frozen by hash. The earlier 21-theorem run and subsequent syntax-failed attempt are retained as provenance, not additional results.

The [case runner](RecoverableControlCases.lean) compares 4,716 prefix/replay records, 20,736 interrupted-and-resumed histories, 1,464 permission/generation preparations and 972 marker-loss states with a separately expressed Python reference. This is same-author verification, not independent acceptance or a hardware test.

The executor retains the state of an interrupted or blocked prefix. Its Boolean means requested events were processed, not that shutdown completed. Successful shutdown uses 22 units without interruption or 23 units/24 steps with the worked crash. Underfunding and delay remain actual failures. With only nine units, recovery is pending and the activity remains running while ordinary shutdown is blocked. Deleting the marker can instead expose a false certificate.

Preparation and each microstep still have specified atomic/protected primitives; the module does not implement persistence barriers, physical isolation, arbitrary external effects, a reliable emergency stop, or independent authority revision during recovery. Use the exact hypotheses of `interrupted_history_preserves_safety` and `funded_suffix_publishes`, not a blanket crash-safety claim.
