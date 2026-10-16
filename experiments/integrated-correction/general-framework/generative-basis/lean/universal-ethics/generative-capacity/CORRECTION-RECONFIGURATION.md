# Causal fault envelopes and correction after reconfiguration

8 October 2026. See the [research integration](../../../../../../../_process/research/2026-10-05-generative-foundation-review/history/root-foundation/CORRECTION-RECONFIGURATION-INTEGRATION.md) for the argument, exact limits, primary sources and author counterreview.

Run from this directory:

```sh
python3 check_correction_reconfiguration.py
```

The checker uses the installed Lean 4.29.1 binary, builds frozen project dependencies in a temporary directory, rejects proof bypasses and warnings, audits all explicitly named new declarations, and compares the executable finite runner with a separately expressed Python reference. It retains source/compiler/helper hashes, source copies and logs under `correction-reconfiguration-checks/`; [the current receipt](correction-reconfiguration-verification.json) identifies the exact run.

[CorrectionReconfiguration.lean](CorrectionReconfiguration.lean) adds 28 theorems and 48 declaration audits. Twenty-eight audits are empty; the rest use standard Lean dependencies recorded in the receipt. [The runner](CorrectionReconfigurationCases.lean) supplies 33,648 comparisons. The four inherited modules retain their earlier result counts.

Main connection: `failure_monotone` and `outside_bound_survives` transport root-cause coverage into the computed reviewer envelope; `ready_iff_nonempty_separated` gives the admission criterion; `admitted_reform_completes` connects a funded atomic reconfiguration to actual guarded correction. Checked cases preserve shared-control failure, duplicate support, omitted causes, stale requests and inadequate post-review resources, alongside a completed shutdown after repair.

The formulas, root bounds, faithful response behavior, authorization and protected atomic monitor remain application premises. The declared cost is not a CPU or migration measurement. No distributed consensus, physical deployment, learned causal completeness, automatic mandate expansion or ethical warrant from signatures is proved. 中文范围：条件性组织改革与真实纠正相接，规范正当性及实际因果对应分别保留。
