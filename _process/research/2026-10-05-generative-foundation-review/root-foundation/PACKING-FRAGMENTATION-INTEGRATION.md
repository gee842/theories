# Cellular packing and the missing descendant account

8 October 2026. AI-authored empirical reconstruction and author self-review for [The Theory of Evolution](../../../../theories/becoming/chapters/THE-THEORY-OF-EVOLUTION.md), especially completion requirements 2, 3 and 5. The previous goal turn restated the completion requirements and added no research evidence. This continuation supplies a reproducible physical correspondence and identifies a specific obstacle to treating that correspondence as a complete evolutionary life cycle.

**Result.** Reconstructing neighborhoods for 2,106 cells in 20 snowflake-yeast clusters closely recovers the published packing statistics: our shape parameter is 2.902 and cumulative-distribution error is 0.0216, compared with the paper's 2.88 and 0.02. This gives affirmative support for using the existing physical account within our relational explanation. The associated 10,020 census diameters, however, do not reproduce the published cell-count scale under the stated conversion. Neither dataset supplies identified fragmentation products followed into subsequent generations. The full evolutionary objective remains open.

**中文范围。** 已从20个群体的2,106个细胞位置重构空间邻域，近似恢复文献的堆积统计；这项常规物理解释获得实证信用。10,020项直径记录按所述公式换算后，与发表图的细胞数量尺度尚未对应。不能因此调一个比例直到吻合，也不能把局部受限概率直接当作已验证的完整适合度。新的缺口是具体的测量接线及断裂后继历史，不是一元关系解释已被否定。

## The physical connection and its source

[Day et al. (2022)](https://doi.org/10.7554/eLife.72707) connect variable cellular placement to reproducible packing statistics and propose a weakest-link route to fragmentation. Their equations 3–4 integrate a shifted gamma distribution below a local confinement threshold and, assuming independence, assign an unfragmented probability of `(1 − p*)^N`. They explicitly omit the sizes and later fate of fragmentation products. The measured size distribution is a census of descendants of one isolate, not a collection of directly observed first-fracture events.

The [preserved original article and archives](../../../../sources/evolutionary-selection/day-2022/README.md) provide the full selected coordinate and diameter records. In our reconstruction, bonds, geometry, occupied space and later breakage are differentiated relations in the same developing cluster. Geometry is not an independent environment added to an otherwise self-contained organism. The existing [developmental-association construction](DEVELOPMENTAL-ASSOCIATION-INTEGRATION.md) supplies a local inherited attachment mechanism, but has no measured coordinates, elastic forces or fracture law. This study supplies evidence for those further relations without claiming that its empirical cells are the formal construction's exact states.

## Reconstructed packing

The [analysis](../../../../experiments/integrated-correction/general-framework/generative-basis/ecological-selection/packing/analyze_packing.py) centers each coordinate set, constructs its convex hull, and moves the hull vertices radially outward by 3 micrometers, following the article's methods. Each cell's nearest-center region is intersected with that boundary. The initial spherical boundary described in the paper does not clip this enlarged convex hull; our computation uses direct halfspace intersection instead of the original Voro++/Matlab wrapper.

All 20 reconstructed partitions conserve their bounding volume to a maximum relative numerical residual of `4.55 × 10⁻¹⁶`; computed vertices satisfy their halfspaces within the declared tolerance. An eight-octant unit-cube calculation checks the implementation on a known geometry. These are numerical checks, not formal proofs or independent reproduction of the geometry software.

Using the stated mean cellular volume of 17.44 cubic micrometers gives:

| Quantity | Reconstruction |
|---|---:|
| Cells / clusters | 2,106 / 20 |
| Mean neighborhood volume | 105.0473 cubic micrometers |
| Shifted gamma shape parameter | 2.90236 |
| CDF error using empirical midranks | 0.02163 |
| Model mass below the stated threshold `2.02 × 17.44` | 0.0263443 |
| Observed fraction below that threshold | 28 / 2,106 = 0.0132953 |

The close overall distributional correspondence gives the conventional mechanism credit. Its small-tail calibration still matters: the reconstructed model assigns about twice the empirical mass below the selected threshold. Cells within a cluster are dependent observations, and these intact-cluster samples are not a randomized collection of new-cell fracture trials. No binomial significance test or measured fracture hazard is asserted.

Boundary sensitivity also matters. With analyst-selected radial extensions of 1 and 5 micrometers, the same calculation gives threshold masses of 0.08336 and 0.04843, respectively. These choices are not confidence limits, and their nonmonotonic effect reflects changes in both the mean and shape. The stated 3 micrometer case remains primary; none of the alternatives is chosen to improve agreement with the census.

## The census conversion does not yet correspond

The two source workbooks each contain 5,010 diameter observations. Their unit row is micrometers. [Beckman Coulter's explanation](https://www.beckman.com/resources/technologies/coulter-principle/coulter-principle-short-course-chapter-1) supports interpreting the reported Coulter diameter as a volume-equivalent spherical diameter. Combining that interpretation with the article's stated `N = V / vc` yields the numerical conversion `N = π d³ / (6 × 17.44)`.

| Source file suffix | Mean estimated cells | Maximum estimated cells | Observations above 350 |
|---|---:|---:|---:|
| 01 | 194.6455 | 1,452.7378 | 817 / 5,010 |
| 02 | 196.0233 | 2,037.5734 | 840 / 5,010 |
| Combined | 195.3344 | 2,037.5734 | 1,657 / 10,020 |

The visually inspected published Figure 5C extends to approximately 350 cells, where its recorded counts are already small. The direct conversion puts 16.54% of the available observations beyond 350. Its approximately exponential decline is not enough to certify the published physical scale or prediction. We do not silently adjust cell volume, diameter, packing fraction or a plotting scale until the curves agree.

This is an unresolved correspondence, not a finding that the publication is wrong. Additional preprocessing, calibration, dataset selection or a different interpretation of the export may account for it. The existing source-code-4 package is a growth simulation with configurable defaults, not the complete diameter-to-Figure-5C analysis. The original workbooks and their full readings remain available for resolving the discrepancy. The paper's cellular-volume spread of 7.33 is not repurposed as a confidence interval for the mean or for this conversion.

![Packing reconstruction and direct source-data conversion](../../../../experiments/integrated-correction/general-framework/generative-basis/ecological-selection/packing/packing-correspondence.png)

The figure shows our reconstructed distribution and the stated conversion of the full diameter files. It does not digitize, redraw or claim to reproduce Figure 5C.

## Consequences for the evolutionary derivation

We can now include a supported intermediate explanation: inherited local development produces variable geometry whose aggregate packing statistics can be reproducible. Confinement supplies a physically motivated candidate for bond failure. Reproducible collective traits need not require an identical microscopic arrangement in every descendant. These contributions belong to the existing conventional account and can become parts of our connected explanation.

The next transition must follow actual fragments. A census mixes the consequences of growth, breakage, fragment production, loss and sampling. To connect it to evolutionary continuation, the account needs identified fragment sizes and states, their division and survival, inherited redevelopment, and the activity providing materials and support. A threshold probability and a good census fit alone do not provide those histories. The earlier 2013 retention cultures are a separate experiment; combining their ratios with these 2022 geometries would require an explicit cross-study correspondence.

This sharpens two tasks. First, retain the successfully reconstructed packing mechanism while resolving the source-data conversion or choosing a dataset with an explicit calibration. Second, compare a joint growth-and-fragmentation account against an equally informed conventional model, scoring descendants and retained production under the same transfer conditions. Support renewal must be represented through its actual supplying activity. It cannot be inserted as free resetting after each generation.

A newly identified [2026 preprint on division timing](https://doi.org/10.1101/2025.04.23.650085) is a relevant next source because its abstract reports lineage tracking and a connection from division timing through morphology to fragmentation. Only its primary abstract and indexed excerpts were assessed here; its full methods, code and data have not been evaluated. It does not yet close our missing connection or count as an independently verified result. A [7 October 2026 review](https://doi.org/10.1038/s41586-026-11038-w) also identifies formation, collective selection and differentiation as connected conventional research targets; its abstract is a scope check, not new mechanistic evidence.

For the normative programme, this study tests the formation and physical reliability of capacities for further living activity. It does not infer ethical authority from reproductive prevalence. G0 and the completed conditional practical-judgment scope remain intact.

## Author self-review and verification scope

The substantive counterreview is that our geometry reconstruction is already well described by the published account, the census-scale discrepancy may be in our correspondence, and neither cross-sectional dataset identifies a complete reproductive cycle. Therefore there is no demonstrated comparative superiority. The favorable result is a tested physical connection; the adverse result changes which quantities can responsibly be used for calibration.

[A second implementation](../../../../experiments/integrated-correction/general-framework/generative-basis/ecological-selection/packing/check_packing.py) parses every XLSX observation from XML without openpyxl, checks the derived reading edition and recomputes the main count statistics. It also recalculates pooled neighborhood moments and the threshold integral with a standard-library series. [The passing receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/ecological-selection/packing/verification.json) states that the geometry is internally checked, not independently reimplemented. No new theorem is claimed, so existing Lean proofs were not rerun. No independent agent review is claimed.

The [study checks](PACKING-FRAGMENTATION-CHECKS.json) bind the scientific files and record integration into the evolutionary map and bilingual chain. The six full completion requirements remain unchanged.
