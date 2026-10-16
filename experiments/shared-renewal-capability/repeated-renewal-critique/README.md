# Exact necessary bounds for repeated renewal

`exact_check.py` uses Python rational arithmetic only. It checks the new rate-derived bounds in [the accompanying derivation](../../../_process/history/2026-10-05-support-and-shared-generativity/completion/REPEATED-RENEWAL-CRITIQUE.md): eventual singleton-lineage limits, finite-deadline Erlang and fresh-capture Poisson bounds, exact necessary material thresholds, and the simple unpartitioned RNA-capacity obstruction.

Run `python3 experiments/shared-renewal-capability/repeated-renewal-critique/exact_check.py` from the repository root. The preserved `exact-check.json` records the base commit, source and code hashes, arithmetic method and outward decimal enclosures. A positive Taylor sum through order 240 bounds each required exponential below; its omitted positive terms are bounded above by a geometric series. All reported decimal bounds have integer numerator and denominator 10^30.

These are rigorous evaluations of **necessary upper-bound expressions**, not simulations, actual renewal probabilities, empirical data or sufficient design thresholds. The finite-deadline rows list the Erlang race bound, the capture-throughput bound, and their minimum. The joint event needs complete turnover and final reserve restoration; no independence is asserted. The general stochastic comparison proofs remain in the note.
