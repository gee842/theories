# Evidence for the assumption and universality investigation

Prepared 5 October 2026 for the report `proving-generative-theory.md` and its proof appendix `general-access-theorem.md` in the parent deliverables.

This bundle contains the mathematical derivation, assumption audit, primary-source proof-strategy memo, exact finite checker and its results, and independent agent reviews. It extends the previous access proof without modifying the original model, protocol, results, or archives. No mathematical novelty, full Lean build, empirical validation, or completed universal theory is claimed.

The general proof covers nonnegative real-valued funds and arbitrary finite schedule lengths under its specified rules. The finite checker separately covers 504,840 bounded integer schedules and 1,032,816 examined prefixes, stopping at a first infeasible payment. It checks greedy feasibility and maximum cash against exhaustive transfer choices and compares equivalent funding inequalities.

To reproduce the numerical check, use Python 3 from this directory:

```
python3 financial_schedule_verify.py
```

This uses only the standard library and rewrites `financial_schedule_checks.json`. It does not access the network or reference repositories. The saved result was reproduced byte for byte from a packaged copy during delivery verification.

`formal-assumptions.md` contains the detailed proof and its limits. `assumption-ledger.md` audits current and inherited claims without asserting that every inherited proof was rerun. `proof-strategy.md` records the broader proof obligations and locations in primary texts. Review files distinguish independent agent checking from independent human or empirical replication. `manifest.json` records hashes for the other bundle files.
