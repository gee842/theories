# Packing geometry and census correspondence

This numerical study reconstructs a physical input to the evolutionary life cycle from Day et al. (2022). It reads original source archives, computes bounded Voronoi neighborhoods for 20 clusters, and audits the diameter-to-cell-count conversion for 10,020 census observations. It adds no mathematical proof or independent biological replication.

Run with Python 3.12 and the versions recorded in [results](packing-results.json): NumPy 2.5.3, SciPy 1.18.1 and openpyxl 3.1.5. The plot additionally uses Matplotlib 3.11.2. Dependencies were installed in a temporary virtual environment outside the repository; no interpreter or package cache is preserved here.

```sh
python analyze_packing.py
python check_packing.py
python plot_packing.py
```

- [Analysis](analyze_packing.py) reconstructs the declared radial convex boundary and intersects nearest-center halfspaces. It checks a unit-cube partition, containment residuals and total volume for each cluster. The 1 and 5 micrometer extensions are sensitivity choices around the stated 3 micrometer method, not confidence limits.
- [Second implementation](check_packing.py) reads XLSX XML directly using only the standard library, checks every exported diameter/sequence/count, and recalculates selected moments and the gamma threshold probability by a convergent series. It does not independently reproduce the Voronoi geometry.
- [Verification](verification.json) binds code, source manifest and numerical outputs. A passing arithmetic check does not resolve the data-to-figure discrepancy.
- [Diameter reading edition](diameter-reading.csv) and [neighborhood reading edition](voronoi-reading.csv) are derived, source-indexed records. Original bytes remain in [sources](../../../../../../sources/evolutionary-selection/day-2022/README.md).
- [Figure](packing-correspondence.png) shows this analysis, not a redrawing or verified replication of the published Figure 5.

The [integration and author self-review](../../../../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/PACKING-FRAGMENTATION-INTEGRATION.md) credit the conventional packing mechanism and preserve the unresolved links to fragment production, descendant growth, survival and supporting activity.
