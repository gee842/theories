# Developmental life cycles and physical sorting

8 October 2026. AI-authored mechanism integration, numerical sensitivity analysis and author self-review for [The Theory of Evolution](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/THE-THEORY-OF-EVOLUTION.md), especially requirements 2, 3 and 5. The previous goal turn made progress through a packing reconstruction and census-conversion audit. This continuation investigates how developed organization acquires differential continuation through a specified physical sorting process.

**Result.** The newer division-timing preprint already supplies a conventional, conditional connection from division histories through fragmentation products to repeated simulated transfers. Our comparison must credit that scope. A material-accounting audit identifies a consequential correspondence choice in translating geometry into settling speed. On the same 20 measured cluster geometries, two declared density treatments reverse **33 of 190 pair rankings**. **Seven new Lean theorems and thirteen declaration audits pass**, checking the algebra and selected rational score comparisons. Neither the numerical comparison nor those proofs identify the true drag law, reproduce the author's simulations, or establish superior empirical prediction.

**中文结论。** 常规研究已把分裂时序、断裂产物及反复传代接成有条件的生命周期模型，比较时必须给予这项信用。相同20个群体的几何数据，在两种明确密度对应下出现33／190对沉降排序反转；7项 Lean 定理与13项声明审计检查其物质核算和代数范围。真实渗透性、阻力、后继选择和支持更新仍需对应，不能把敏感性结果冒称实际生物优势。

## The existing life cycle is a substantive comparator

[Cedeño-Pérez et al., version 3, 28 May 2026](https://doi.org/10.1101/2025.04.23.650085), is a preprint. Its declared network model retains mother–daughter links, uses division-time distributions and cuts a crowded edge to produce two clusters. It then models repeated growth and settling transfers. A simulated control equalizes growth rates while retaining a settling advantage. Later lineage observations are consistent with loss of the initial division delay; the authors retain compensatory faster growth as an alternative explanation. The fracture-location rule is an approximation, calibrated using a reference strain. [Original XML and reading scope](../../../../sources/evolutionary-selection/cedeno-perez-2026/README.md).

This is stronger than a frequency recurrence that omits development. It already connects several relations our programme seeks to integrate. Our remaining task cannot be framed as inventing the first account of fragment descendants. It concerns justified physical correspondences, compatible inherited histories and accounted supporting activity, followed by a genuinely discriminating comparison. The underlying author code and lineage measurements were not available in the retrieved material, so the reported simulation outcome is source evidence rather than our verified replication.

## Material and drag must refer to the same configuration

The preprint's settling methods use a radius-of-gyration-derived diameter in Stokes' formula, with yeast-cell density and water properties. Our audit asks whether the corresponding envelope contains only cell material, or cells plus intervening liquid. This is a choice about the physical interpretation of one developed configuration, not independent organism and environment substances.

Let `M` be cellular material volume and `V` a surrounding envelope volume. Under the declared interpretation that the remaining volume is filled by the same liquid, the mass in that envelope is

`M ρcell + (V − M) ρfluid`.

After subtracting the displaced-fluid mass, its excess is

`M (ρcell − ρfluid)`.

The first Lean theorem checks this rational identity. If the cell density is instead assigned to the entire envelope, the excess mass is represented as `V (ρcell − ρfluid)`. For nonzero density contrast and the same positive spherical drag, those two correspondences coincide only for a filled envelope. This conclusion concerns the stated meanings of the terms; it does not establish the appropriate hydrodynamic envelope for an irregular porous cluster.

With a spherical radius proxy `R`, solid fraction `φ = M / V`, and the same impermeable-sphere drag, the material-accounted approximation is the uniform-cell-density approximation multiplied by `φ`. Equivalently, after omitting common dimensional factors, their scores are `M/R` and `c R²`, with `V = c R³`. The formal module treats the coefficient as a nonzero rational parameter and audits the cancellations; using `c = 4π/3` and real geometry is a declared physical interpretation, not an assertion that π is rational.

Permeability remains essential. If actual drag is `χ` times the spherical reference, the corresponding correction is `φ/χ`, not `φ` alone. A checked conditional identity shows that `χ = φ` offsets the density correction entirely. Thus the material-accounted sphere is a useful comparator, not an automatically correct replacement. Primary aggregate experiments also identify nonsphericity and flow through pores as limits of impermeable Stokes approximations; the [asphaltene study's abstract](https://doi.org/10.1021/ef0496707) supports that scope warning, not a yeast calibration.

## Matched geometry sensitivity

The [numerical analysis](../../../../experiments/integrated-correction/general-framework/generative-basis/ecological-selection/settling/analyze_settling.py) uses the complete [Day 2022 coordinate archive](../../../../sources/evolutionary-selection/day-2022/README.md). Cell counts and center coordinates are identical between the two calculations. Both use the same radius proxy, cell-volume mean, water properties and spherical drag. No fitting parameter is chosen to generate a rank reversal or to repair the earlier Coulter conversion problem.

The squared radius proxy is `5/3` times the mean squared distance of cell centers from their centroid. Exact exported decimals permit exact rational coordinate moments and comparisons of the squared material score `N²/R²`. The proxy omits each cell's internal mass distribution and has not been measured as a hydrodynamic radius. The calculation mixes no lineages: it applies declared formulae to one geometry dataset as a sensitivity analysis, not as a reproduction of the 2026 competition experiment.

| Quantity | Result under the stated approximations |
|---|---:|
| Clusters / cell centers | 20 / 2,106 |
| Unordered cluster pairs | 190 |
| Pairs whose predicted order reverses | 33 |
| Inferred solid-fraction range | 0.1569–0.3080 |
| Uniform-cell-density sphere speeds | 0.6097–3.2947 mm/min |
| Material-accounted sphere speeds | 0.1224–0.9042 mm/min |
| Maximum Reynolds number from the uniform calculation | 0.001632 |

Low computed Reynolds numbers are consistent with examining a viscous-flow approximation. They do not validate its radius, shape or permeability assumptions. No observed settling speeds, survival proportions or fitness estimates are produced by this analysis.

One source-bound comparison makes the consequence concrete:

| Coordinate file | Cells | Radius proxy | Uniform speed | Material-accounted speed |
|---|---:|---:|---:|---:|
| 01 | 128 | 13.1453 μm | 2.6634 mm/min | 0.6249 mm/min |
| 04 | 147 | 12.5723 μm | 2.4363 mm/min | 0.7503 mm/min |

The larger radius proxy ranks first under one correspondence; the denser, more cellular cluster ranks first under the other. `measured_geometry_scores_reverse` kernel-checks the exact rational squared-score comparison. [A second implementation](../../../../experiments/integrated-correction/general-framework/generative-basis/ecological-selection/settling/check_settling.py) obtains coordinate moments from integer sums and sums of squares, checks all 190 pair rankings, and binds the two Lean constants to the original files. Its [receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/ecological-selection/settling/verification.json) records the computational scope.

## Formal scope and dependencies

[SettlingCorrespondence.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/SettlingCorrespondence.lean) contains seven new results:

1. Excess mass from cellular material and intervening liquid.
2. Volume accounting after clearing a nonzero denominator.
3. The declared spherical density correction.
4. Equality of uniform and material scores precisely at a filled envelope, for nonzero radius.
5. Conditional cancellation by a matching relative-drag factor.
6. A finite idealized reversal at equal material volume and different radii.
7. The source-bound squared-score reversal for files 01 and 04.

The [isolated verification](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/settling-verification/verification.json) uses Lean 4.29.1, audits all thirteen definitions/theorems and retains exact source snapshots and compiler logs. Only `propext`, `Classical.choice` and `Quot.sound` occur. No custom axiom, admitted proof or native-decision shortcut is used. Exact rational proofs do not formalize fluid mechanics, validate the geometry extraction experimentally, or compose the earlier developmental graph with a calibrated settling law.

The physical inputs remain explicit: material volume, its correspondence to cell number, the radius proxy, fluid properties, a drag law and a sorting protocol. The former eight-carrier reconstruction law is not silently reused as a physical law for these clusters. G0 and ethical comparison commitments do not enter this calculation.

## Integration and next discriminating test

The positive connection is now clearer: inherited division schedules can alter bond topology and fragmentation products; the developed configuration also changes the material and fluid relations through which sorting occurs. Reproductive consequences require the combined history. A single monotone size-to-fitness map can omit physically relevant differences even after development is represented.

The next test should identify clusters before sorting, measure their cellular material, geometry and settling velocity under the actual medium and concentration, then follow surviving fragments into redevelopment. Compare the uniform-density, material-accounted and calibrated permeable-drag predictions on the same held-out cluster histories. Retained cell numbers and subsequent offspring must be distinguished from initial settling rank. Growth and medium replacement must have an actual material/support account, rather than a costless reset of carrying capacity.

This study advances the physical correspondence needed for that test. It neither completes the full life cycle nor supplies evidence of superior predictions. The two diagnostic approximations are conventional models receiving the same information. Their disagreement defines a consequential empirical choice; observations must decide which account survives. The earlier census-scale discrepancy is preserved as a separate unresolved correspondence and has not been repaired by these calculations.

## Author self-review

The strongest counterargument is that permeability or shape may make the uniform approximation a better effective predictor despite its incomplete literal density interpretation. The formal drag-offset result explicitly preserves that possibility. The 33 reversals also come from a different experiment than the 2026 modeled populations; they cannot be used to overturn the preprint's reported selection coefficients. The affirmative gain is a source-bound, checked account of what a physical sorting correspondence needs to preserve.

This is author self-review, not an independent agent review. [Study checks](SETTLING-CORRESPONDENCE-CHECKS.json) bind the numerical and formal evidence and the updated evolutionary entry. The six completion requirements remain unchanged and incomplete at the full goal's scope.
