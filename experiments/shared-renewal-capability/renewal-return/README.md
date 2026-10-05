# Exact checks for physical repair and return

This experiment supports [Physical repair, succession and return after renewed capture](../../../_process/research/2026-10-05-support-and-shared-generativity/completion/RENEWAL-RETURN.md).

The [checker](exact_check.py) reuses the frozen, previously reviewed [allocation reaction implementation](../allocation/exact_check.py). It checks three specified physical return paths, the tagged original-Y replacement branch, their exact competing hazards, material and work accounting, and the full-turnover packet count. It also checks the stated entry fraction, damaged-state all-path upper bound and narrow C-path architecture ratio.

The saved [result](exact-check.json) passed. All probability fractions and ledger checks use exact rational arithmetic; floating-point values are display approximations only. This is a new path/accounting calculation using an existing event implementation, not an independent reconstruction of that implementation, a parameter search, or a simulation estimate.

To reproduce from the repository root:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 experiments/shared-renewal-capability/renewal-return/exact_check.py
```

Running rewrites only this directory's `exact-check.json`. The source implementation and checker hashes are recorded in the output. The script also disables imported bytecode creation.

The four-packet turnover bound belongs to the declared work ledger. The finite-time selected macrocycle bound is about **3.53 × 10⁻²⁶**, and does not estimate all possible turnover paths or establish likely renewal. The damaged-state upper bound **1/72** applies to all return paths from that specified damaged preparation. The architecture ratio **847** applies only to the narrow selected C-return path; the broader kernel comparison is proved analytically in the research note.
