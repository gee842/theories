# Recorded lineage continuation and evolved life-cycle switching

8 October 2026. AI-authored reanalysis, mathematical correspondence and author self-review for [The Theory of Evolution](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/THE-THEORY-OF-EVOLUTION.md). The preceding goal turn made progress through measured aggregation. This study advances the missing inherited-organization → realized reproduction connection using a different, explicitly identified bacterial experiment. It does not retrospectively turn the yeast geometry and aggregation datasets into one history.

**Result.** An original, publisher-checksummed archive supplies 3,808 non-missing phase/culture records and a mutation-reversion assay with directly matched cultures across two phases. In the matched-date assay, an evolved genotype completed the life cycle in **42/72** cultures, while its focal-mutation revertant completed it in **7/72**. The recorded genealogy traces all **44 viable terminal lineages** of the relevant evolution treatment through the focal ancestor 2-II-A5. Separately, measured joint first-phase success differs from the product of marginal component frequencies. Six new Lean theorems and six declaration audits check the associated rational identities and finite counts. This establishes a substantially stronger empirical connection at the experiment's scope, while crediting its conventional explanation and preserving supplied support and selection regimes.

**中文结论。** 新取得的原始档案有3,808项可用阶段／培养记录，并可在同一次遗传回复实验中逐管接续两个阶段：演化株42／72完成，回复株7／72完成。相应演化处理的44个末期存活谱系均有记录路径经过2-II-A5。另核查共同完成第一阶段与两个边际成功率相乘的差异，新增6项 Lean 定理／6项审计通过。该实验已提供有范围的遗传改变—实际后继连接，不再笼统声称所有实测接续都缺失；培养供给、实验选择规程、跨机制推广和充分比较优势仍未完成。

## The experiment and its supplied conditions

[Doulcier et al. (2025)](https://doi.org/10.1098/rspb.2024.1195) continue earlier Pseudomonas fluorescens life-cycle evolution. Wrinkly-spreader cells form a mat; smooth cells provide a dispersal phase from which mat-forming cells must reappear. A prior evolved lineage has a mutS-associated switching phenotype. An isogenic reversion removes that mutation, supplying the switch-negative starting comparison. Both are propagated for ten further life cycles in standard or larger microcosms. Each treatment has 48 cultures arranged in six blocks of eight.

Successful continuation requires mat endurance, production of smooth cells, and subsequent production of mat-forming cells. When a lineage fails, a randomly chosen viable lineage replaces it within the block; replacement from another block occurs after entire-block extinction. The researchers supply media, timing, phase transfer and this replacement procedure. These are actual activities maintaining the observed cycle, not consequences derived from the bacterial genotype. The resulting mechanism is conditional on that laboratory organization.

The source reports a new mutL L103R variant arising within the large-microcosm switch-negative treatment. Sequencing and genetic reversion support its role in renewed switching and improved cycle completion. Our reanalysis does not reproduce the sequence alignments or Bayesian placement of mutations. Its contribution is direct reconstruction of recorded parent relations and a linked assay that tests the reported phenotype consequence. [Original bytes and reading scope](../../../../sources/evolutionary-selection/doulcier-2025/README.md).

## Recorded ancestry and the limits of endpoint success

The genealogy workbook has 3,840 rows. Thirty-two explicitly marked `MISS` rows are retained separately and excluded from observed ancestry. The remaining 3,808 nodes identify a treatment, cycle, phase and culture, with extinction and replacement fields. For a new phase, the donor is the previous culture itself if not replaced, otherwise the replacement donor recorded in the preceding phase. Sixteen nodes after missing intervals have unresolved parents; no ancestry is invented across those gaps.

| Raw treatment | Non-missing phase/culture records | Viable cultures at final observed phase | Distinct initial-culture ancestors among those survivors |
|---|---:|---:|---:|
| WT-S: standard, switch-negative | 944 | 37 | 2 |
| WT-L: large, switch-negative | 944 | 44 | 1 |
| 17-S: standard, switch-positive | 960 | 48 | 22 |
| 17-L: large, switch-positive | 960 | 45 | 9 |

These are observed terminal survivors, before interpreting recorded replacement donors as another completed generation. They are not 174 independent evolutionary replicates. All 44 viable WT-L endpoints have recorded ancestry through 1-I-F8 → 1-II-A7 → 2-I-A3 → **2-II-A5**. The later common descent is not alone evidence that a particular mutation was beneficial: the imposed replacement lottery can amplify a surviving lineage by chance. The source addresses that concern with genotype assays and genetic reversion. Other condition flags remain attached to the source-labelled nodes; the reconstruction certifies the recorded relationships, not an independent historical observation or genomic identity at every node.

The [independent checker](../../../../experiments/integrated-correction/general-framework/generative-basis/ecological-selection/lineages/check_lineages.py) reads XLSX XML directly, verifies all 3,600 observed parent links and follows 174 terminal paths backward. It agrees with the separate forward reconstruction. Missing records, raw cycle-index inconsistencies confined to missing rows, and a treatment-label discrepancy in the published missing-data caption are preserved in the source README. They are not silently repaired to improve agreement.

## A directly linked, matched-date cycle

The raw fitness workbook contains multiple dates and assay designs. On **2 June 2020**, both `PE-2-WT-A5` and its `mutL` revertant have 72 initial cultures in nine racks. For each genotype, phase-II keys are exactly the phase-I survivors, using date, strain, size, rack and tube. All selected records have condition zero and no recorded replacements. Phase-I survival agrees with joint mat presence and positive smooth-cell counts; phase-II survival agrees with positive wrinkly-spreader counts.

| Genotype under the same dated assay | Initial cultures | Complete phase I | Complete phase II after surviving I | Complete observed cycle |
|---|---:|---:|---:|---:|
| Evolved `PE-2-WT-A5`, source-identified mutL variant | 72 | 47 | 42 | 58.33% |
| `PE-2-WT-A5 mutL`, source-identified reversion | 72 | 31 | 7 | 9.72% |

The observed difference is 35/72, or 48.61 percentage points; the ratio of completion fractions is six. Removing one rack from each genotype in all 81 combinations gives a descriptive difference range of 43.75–57.81 percentage points. This range is not a confidence interval. Rack labels do not establish matched independent mutation origins, randomization, or a biological-population effect distribution. The date was selected because it permits complete direct linkage for both genotypes, not because all assays were preregistered for this reanalysis. Other batches remain preserved and unpooled; some lack the requisite phase-II follow-up.

`PE-2-WT-A5` is the raw strain label; the author notebook displays it as the start of the following cycle, 3-I-A5. The genealogy's 2-II-A5 and that following assay name are therefore not two independent origins of the variant. This naming correspondence, and the source-reported isogenic reversion, are necessary to interpret the measured difference.

This supplies a concrete, inherited change → viable cycle completion connection. It is stronger than a morphological advantage or an inferred fitness score alone. It still does not establish the microscopic mutation rate: the paper explicitly says that rate was not directly measured. We therefore distinguish altered switching, lineage success, mutation accumulation and mutation-rate inference.

## Why component frequencies need their joint history

The author's fitness notebook multiplies mat success, smooth-cell production and later wrinkly-spreader production frequencies. The directly linked assay above supports a conditional stage calculation: 47/72 × 42/47 = 42/72, and 31/72 × 7/31 = 7/72. It does not require independent stages because the second denominator is the actual number of preceding survivors.

By contrast, multiplying two marginal success rates within the same first phase generally needs an additional correspondence. In the ancestral large-microcosm first-phase data, **183 complete observations** have the following table:

| | Smooth cells present | Smooth cells absent |
|---|---:|---:|
| Mat present | 28 | 22 |
| Mat absent | 130 | 3 |

The joint observed fraction is **28/183 = 0.1530**. Multiplying the marginal fractions gives **(50/183)(158/183) = 0.2359**. One additional contaminated record has a mat but an unknown smooth-cell count. Including it under either binary completion gives joint fractions 0.1522–0.1576 and marginal products 0.2380–0.2395; the discrepancy is not removed. The raw extinction field records 28 survivors among all 184 entries, but contamination and a missing count must not be converted into a known absent phenotype.

This is a measurement-correspondence finding, not a claim that the paper's main mutation effect disappears. In the matched-date focal assays, all phase-I cultures have smooth cells, so that particular marginal multiplication adds no discrepancy; the large reversion contrast survives direct tracing. An adequate conventional model retaining joint outcomes or conditional probabilities makes the same correction. Reproducing observed joint counts is not a held-out predictive victory for our whole theory.

## Checked mathematics and dependency scope

[LifecycleCorrespondence.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/LifecycleCorrespondence.lean) checks six results in a fresh, pinned Lean 4.29.1 build:

1. For counts `a,b,c,d` in the four joint cells, `a(a+b+c+d) − (a+b)(a+c) = ad − bc`.
2. Equality of those unnormalized joint and product numerators exactly when `ad = bc`.
3. Cancellation for conditional stage composition when the intermediate count is nonzero.
4. The complete-case source table's exact rational discrepancy.
5. Persistence of the discrepancy under both completions of the missing count.
6. Exact composition, difference and ratio for the linked 72-culture comparisons.

The first identities are rational algebra. Probability interpretation additionally requires valid nonnegative counts and a positive total; the empirical totals meet those conditions. The conditional composition theorem does not prove that two experimental phases are linked: matching source records supplies that separate evidence. The [formal receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/lifecycle-verification/verification.json) audits all six declarations and preserves compiler logs and source snapshots. Only standard logical dependencies are admitted; no custom axioms, proof holes or native-decision shortcuts are used. A [separate numerical receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/ecological-selection/lineages/verification.json) covers source extraction and observed histories.

## Derivation, comparison and next connection

The generative account now has a measured example in which a heritable change to developmental switching affects actual reconstruction of the collective life cycle and becomes associated with continued lineage representation. This advances requirements 2–4 and should be credited rather than repeatedly described as absent. The mechanism remains explained by ordinary mutation, developmental transitions, viability and stochastic replacement under specified conditions. Neither new vocabulary nor the same account's inclusion in our foundation makes it comparatively superior.

This also sharpens what “evolution changes its own conditions” can mean here: inherited changes alter the production of the states through which subsequent lineage continuation becomes possible. The genotype does not invent the experimenter's transfer rule or fresh medium. Formation of wider supporting organization, general recovery of mutation/drift/movement mechanisms and stronger comparative predictions remain unfinished. The yeast material/drag correspondence is a separate unresolved empirical case.

The next mechanistic comparison should compute descendant production from phase-transition histories under the recorded replacement rule, retaining chance, failures and supplied support, then test prediction on held-out genealogy segments or intervention batches. A conventional stage-structured lineage model receives the same information. Any proposed explanatory gain must survive that comparison. The source's own Bayesian lineage model already addresses inherited survival propensity and cannot be replaced by a deliberately weaker comparator.

For the normative programme, the evidence supports a conditional mechanism for changes in capacities that permit further life. It does not establish that elevated mutation, lineage fixation or longer continuation is ethically better. G0 and additional comparison commitments remain separate disclosed premises within the same relational account.

## Author self-review

The principal favorable result is a genuinely linked empirical cycle plus a source-reported causal genetic intervention, supported by recorded multigenerational ancestry. The strongest limitations are one focal mutation origin, a chosen directly traceable assay date, flags and gaps in the wider genealogy, and substantial laboratory organization. Preserving these does not erase the positive connection; it determines its scope. Shared ancestry and an experimental intervention answer different questions and must not be collapsed into one causal proof.

The marginal-product discrepancy provides a concrete correspondence correction, but conventional joint-probability accounting supplies it equally well. It does not establish broad theory superiority or refute the paper's genetic conclusion. This is author self-review, not an independent agent review. [Study checks](LINEAGE-CONTINUATION-CHECKS.json) preserve the scientific and integration boundaries; the full six-part evolutionary objective remains active.
