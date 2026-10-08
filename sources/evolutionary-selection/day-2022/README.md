# Day and colleagues 2022 source preservation

Original public files for Thomas C. Day et al., *Cellular organization in lab-evolved and extant multicellular species obeys a maximum entropy law*, eLife 11:e72707, published 21 February 2022. [Article and source links](https://doi.org/10.7554/eLife.72707). The article is distributed under CC BY 4.0; retain attribution when reusing it and its associated source material.

[The manifest](manifest.json) records direct download URLs, byte counts, SHA-256 hashes and archive-member hashes. These are local preservation hashes, not publisher-supplied checksums. Downloaded bytes were copied unchanged from temporary storage on 8 October 2026. ZIP files remain original source packages, rather than generated export bundles.

| File | Contents and scope |
|---|---|
| [day-2022.pdf](day-2022.pdf) | Published article from the University of Cambridge repository. Relevant figures/equations and methods were visually inspected on pages 10, 11 and 19, with methods on pages 15–18 read from extracted text. |
| [packing-data.zip](packing-data.zip) | Figure 1 data: 20 yeast-cluster center-coordinate files and six Volvox files, with original README files. The present analysis uses the 20 yeast files, totaling 2,106 cells. |
| [size-data.zip](size-data.zip) | Figure 5 source data: two XLSX files with 5,010 numeric diameter records each. The files have sequence and diameter columns, with micrometer units. File suffixes do not establish independent biological replication. |
| [snowflake-code.zip](snowflake-code.zip) | Source code 4, one original Matlab script. Inspected as source; not executed. Its defaults include a machine-specific working directory and disabled overlap/force checks, so it is not treated as a ready-made reproduction of Figure 5. |

[Research integration](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/PACKING-FRAGMENTATION-INTEGRATION.md) and [executable analysis](../../../experiments/integrated-correction/general-framework/generative-basis/ecological-selection/packing/README.md) distinguish a successful geometry correspondence from an unresolved census conversion. The original spreadsheets are neither edited nor silently rescaled. These observations are not linked individual histories of fracture, selection and descendants, and are not the same experiment as the preserved Ratcliff 2013 cultures.
