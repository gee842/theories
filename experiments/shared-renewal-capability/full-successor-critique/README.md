# Independent reserve and turnover audit

The [mathematical note](../../../_process/research/2026-10-05-support-and-shared-generativity/completion/FULL-SUCCESSOR-CRITIQUE.md) proves an unbounded-reserve pump, a leakage-based probabilistic reserve bound, exact entry-truncation semantics and necessary wear/capture timing bounds.

[exact_check.py](exact_check.py) reconstructs all42 channels independently and checks material/work/mobile-pool increments, selected positive paths and rational tail bounds. [exact-check.json](exact-check.json) preserves the successful run and input hashes. These checks do not calculate the full successor probability or identify molecules.

Run `python3 experiments/shared-renewal-capability/full-successor-critique/exact_check.py` from the repository root to reproduce; it replaces only the record in this directory. No old numerical propagation is executed.
