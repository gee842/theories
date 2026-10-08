# Karita et al. (2026): context-dependent establishment

Yuya Karita, Gisela T. Rodríguez-Sánchez, Elisa Brambilla, J. Carlos R. Hernandez-Beltran, Michael Schwarz and Paul B. Rainey, *Context-dependent adaptation in structured environments*, Proceedings of the Royal Society B 293:20252004, 4 February 2026. [Article DOI](https://doi.org/10.1098/rspb.2025.2004), [author-institution PDF](https://pure.mpg.de/rest/items/item_3655572_4/component/file_3698373/content).

The [manifest](manifest.json) preserves 14 unchanged files (9,510,048 bytes), retrieved 8 October 2026: article and supplement PDFs, repository metadata and selected original workbooks/code. The six selected Zenodo files match their publisher MD5 values; the supplementary PDF matches its Figshare MD5. Local SHA256 values bind all preserved files. The article prints CC BY 4.0; repository license metadata is retained. The article's DOI year component and 2025 data-deposit dates are not its publication year. Europe PMC's index date fields also differ from the explicit February 4 issue/publication record.

Primary deposits:

- [Zenodo 15735347](https://doi.org/10.5281/zenodo.15735347), explicitly cited by the final article. Six originals are preserved here: [pellicle success](Pellicle_success.xlsx), [colony areas](Collapsing_colony_size.xlsx), [surface-density observations](Surface_density_data.xlsx), [four-state notebook](4state-model.ipynb), [spatial code](Spatial_Model_LBOX500.c) and [spatial parameters](input.txt). Notebook sources were read; stored outputs are not evidence of a fresh run. Spatial code is preserved but not executed or fully audited.
- [Figshare supplementary collection](https://doi.org/10.6084/m9.figshare.c.8229719), supplying [supplement.pdf](supplement.pdf). Notes A–C and Tables S1–S3 were read, distinguishing empirical quantities from chosen model parameters.
- [BioImage Archive S-BIAD2117](https://doi.org/10.6019/S-BIAD2117). The preserved file-list metadata identifies 158 original microscopy files totalling 103,133,470,688 bytes. It includes named formation and rescue acquisitions. The initial study preserved the inventory only. [Targeted original CZI ranges](microscopy-metadata/README.md) now supply checked metadata for five acquisitions and two decoded complete image fields; the full files remain uncollected. The old preprint/data references in this deposit are retained unchanged.

## Reading and discrepancy scope

Article pages 1–9 cover the evidence and methods; pages 2 and 4 were rendered and visually inspected, including a higher-resolution check of Figure 1. The paper distinguishes a 24-hour low-inoculum establishment assay, measured microcolony collapse, fluorescence observations of later WS emergence, and a conceptual four-state model. These are not a single lineage followed through the later Doulcier six-day cycle.

The pellicle workbook contains 11 dated cohorts and 45 cultures. Its pooled counts reproduce Figure 1c: 3/3, 6/6, 12/12, 10/15 and 0/9 across increasing dilution. Dates remain separate; the 10^3.5 dilution has 1/3, 0/3 and 9/9 in different batches. Those differences cannot be assigned a physical cause from the count sheet.

The colony workbook contains 784 positive numeric areas, while Figure 1d names 769 colonies. Applying the paper's circular-equivalent diameter conversion gives exactly 769 values at or below 65 in the figure-reported scale, but this coincidence does not identify the authors' exclusion rule. All 784 rows are retained. The worksheet lacks explicit per-colony culture/image identifiers and a unit header; independent CZI calibration and nesting remain to be checked before a fitted physical collapse law.

The co-culture comparison is **2/9 successes versus 0/15 monocultures**, reported by the article, not contained as per-well rows in the preserved success sheet. Adding SM also increases total cell density; 12 control cultures preceded the plate containing three further controls and nine mixtures. This and the limited observations constrain causal/statistical interpretation. Microscopy and the model add mechanistic evidence, but the rescue fraction alone is not an isolated test of a special mechanical effect.

The source's spatial model chooses the 85% coverage endpoint arbitrarily and chooses a stability coefficient to match the observed collapse-size scale. Its physical contact-angle approximation and omitted wall/matrix complexities remain explicit. The later four-state model assumes rates, capacity and non-oxygen nutrient sufficiency. Neither simulation is an independently calibrated six-day mat-survival model.

[Reanalysis, code and numerical audit](../../../experiments/integrated-correction/general-framework/generative-basis/ecological-selection/contextual-establishment/README.md) and [integration](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/CONTEXTUAL-ESTABLISHMENT-INTEGRATION.md) preserve the conventional source's explanatory credit.
