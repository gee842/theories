# Temporal inspection and correction

The [research integration](../../../../../../../_process/research/2026-10-05-generative-foundation-review/history/root-foundation/TEMPORAL-INSPECTION-INTEGRATION.md) records assumptions, theory, counterreview, source comparison and completion scope.

Run from this directory:

```sh
python3 check_temporal_inspection.py
```

[TemporalInspection.lean](TemporalInspection.lean) maintains paired possibilities for control arrangement and current fault through sequential reports and covered transitions. Its finite-history theorem connects retained actual configurations to current certificates and conditional command completion. The [finite runner](TemporalInspectionCases.lean) compares actual state changes and execution prefixes with a separately expressed Python reference.

Current [receipt](temporal-inspection-verification.json): **34 new theorems / 66 declaration audits / 35,486 matched records**. Thirty-two audits have no axioms; others use only `propext`, `Quot.sound` and `Classical.choice`. Seven inherited modules are freshly compiled but not recounted. Sources, compiler, signatures, dependencies and outputs are retained by hash; no prebuilt `.olean` files are trusted.

`runUntilBlocked` is the execution interface preserving earlier evidence and expenditure when a later operation cannot proceed. `run` specifies a complete successful trace. `auditRun` is an omniscient simulation-premise checker, separate from operational execution; it does not supply deployed detection of hidden changes. Their stated relationships are checked.

The examples include moving corruption producing five false reports with one active cause per read; conservative retention of uncertainty; actual control change, reinspection and shutdown in 23 units; failure with 22; blocked partial inspection; denied reorganization; and an understated transition that leaves an all-compromised certificate accepted. A zero-cost mobility marker represents an admitted exogenous change, not physically free recovery.

The comparison grid has 7,680 report updates, 2,048 predictions, 4,374 stable scans/executions, 20,736 change/reinspection budget-permission cases and 648 three-read mobility histories. This is same-author reference checking, not independent acceptance or empirical validation. Actual transition/report coverage, protected recording, current source behavior, mandate legitimacy and stable final command execution remain explicit conditions.
