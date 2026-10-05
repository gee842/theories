# Enumeration count correction

The parameter lists frozen in protocol `8a5bf6f` contain 3×3×2×3×3×3×2×2 = **1,944** combinations, not the 5,832 printed beside them. The printed product accidentally included an extra factor of three. No parameter list, outcome, or comparison was changed.

The first execution completed every one of the 1,944 declared cases under both operator environments and reversed ties, saved all rows to `results/grid.jsonl`, then failed its terminal assertion against the erroneous printed count. The corrected totals are **3,888 primary runs** plus **1,944 reversed-tie runs**. These are the same 5,832 solved games, not 5,832 independent environments.

To preserve the completed computation, `study.py --finalize-existing-grid` verifies every saved case number, parameter dictionary, and opening reserve against the full unchanged Cartesian sequence, recomputes the aggregate counts from those records, and runs the named controls. Its elapsed time is finalization time, not the original full-grid runtime. A fresh `python3 study.py` reproduces the complete grid with the corrected final count.
