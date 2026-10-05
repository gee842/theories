# Rat cue-grounding evidence: originals and a verified preview

Preserved 6 October 2026 for the investigation of acquired cues, recipient interpretation and effective provision. Source authors: Nina Gerber, Manon K. Schweinfurth and Michael Taborsky (2020), *The smell of cooperation: rats increase helpful behaviour when receiving odour cues of a conspecific performing a cooperative task*. [Primary article](https://pmc.ncbi.nlm.nih.gov/articles/PMC7739497/), DOI `10.1098/rspb.2020.2327`; [Dryad dataset](https://datadryad.org/dataset/doi:10.5061/dryad.h18931zjd), version identifier `93077`.

This directory joins two evidence routes without duplicating previously preserved files. **The supplementary PDF is an original download. The experiment-4 TSV is a derived reading edition of a browser preview; no original experimental CSV has been retrieved or byte-verified.**

## Original supplement

[The supplementary PDF](supplement/rspb20202327_si_001.pdf) and [exact Figshare API response](supplement/figshare-article-13213518.json) were retrieved through the public API's listed download link. The API identifies supplementary article `13213518`, version 2, DOI [`10.6084/m9.figshare.13213518.v2`](https://doi.org/10.6084/m9.figshare.13213518.v2), and the license as **CC BY 4.0**. Its PDF download address is recorded in the [supplement manifest](supplement/manifest.json). Preserved PDF size: 1,491,554 bytes; SHA256: `cf0ec691c7699fbbadb12e2c06edce4c03fb4ef0ad82717b571b8b2dc9ed1fa4`.

The [portable text](supplement/supplement-portable.txt) is a labeled, generated extraction. It omits diagram/layout information and does not replace the PDF. All ten pages were read as text; pages 4 and 6–9 were also rendered and visually checked. The manifest records the retrieval, source URLs, license, file hashes and inspection scope.

## Existing Dryad preservation, linked without copying

The earlier study preserved [dataset metadata](../../_process/research/2026-10-05-generative-foundation-review/root-foundation/reason-action-evidence/dataset-metadata.json), [version metadata](../../_process/research/2026-10-05-generative-foundation-review/root-foundation/reason-action-evidence/version-metadata.json) and [file metadata](../../_process/research/2026-10-05-generative-foundation-review/root-foundation/reason-action-evidence/files-metadata.json). Its [retrieval receipt](../../_process/research/2026-10-05-generative-foundation-review/root-foundation/reason-action-evidence/metadata-receipt.json) records their exact API URLs, byte lengths and SHA256 hashes. The dataset metadata identifies the license as **CC0**. These original metadata bytes are retained at those paths and are not re-imported here.

The file list describes four experiment CSVs and `Readme.rtf`; listing an original file is not retrieval of its contents. Direct website file requests returned HTTP 403, the API download route returned HTTP 401, and browser download attempts did not yield original CSV bytes. No authentication or access control was bypassed. These are observations about attempted routes, not proof that the originals are unavailable through every possible route.

## Experiment-4 preview verification

The existing [experiment-4 TSV](../../_process/research/2026-10-05-generative-foundation-review/root-foundation/reason-action-evidence/experiment4-preview.tsv) preserves the displayed preview's cell strings, with its blank first header renamed `preview_row`. Its [original reading-edition notes](../../_process/research/2026-10-05-generative-foundation-review/root-foundation/reason-action-evidence/README.md) and [bounded integrity receipt](../../_process/research/2026-10-05-generative-foundation-review/root-foundation/reason-action-evidence/preview-check.json) remain at their original location. They describe a derived table rather than an original CSV.

The root agent subsequently read the visible DOM table independently. [The new verification receipt](preview-verification.json) records 49 rows including the header, 10 cells per row, and agreement after canonicalizing the cell arrays to compact ASCII JSON: 3,119 bytes, FNV-1a64 `df8ebe2256185e27`. The associated TSV SHA256 is `4a2a9b660cfd9920a8d1bdcc7830507341e6c58ff08b239398dd6daebb82adbd`. The canonicalization fingerprint checks agreement between displayed cells and the reading edition; the SHA256 identifies the saved edition's bytes. Neither is an authentication claim about the original experiment data.

The original `experiment4.csv` is listed separately as 2,348 bytes with SHA256 `5875db96822a78ce91708f8cb385b4941ecf689d6bfa999177e02a3aebdfab29`. Those original bytes have not been retrieved, so that manifest digest has **not** been verified. Complete reading of the displayed table does not prove that the display contains every original row or preserves all original values, types and encodings.

Experiment 3's visible preview was truncated during row 74. That partial display is not usable as the complete experiment, is not substituted for a full file, and is not included in experiment-4 calculations. The downloadable readme was also not retrieved; field meanings must remain constrained by the article and observed display. The 24 paired identifiers in the experiment-4 preview do not by themselves resolve the article's reported analysis sample of 23.

## Scope of this preservation

The [top-level manifest](manifest.json) hashes the local originals and verification records and links to the already preserved metadata and reading edition. It labels original, derived and generated files separately. Hash verification establishes preservation of these particular bytes; it does not resolve reporting discrepancies, validate a mechanism or establish recipient welfare.

The [methods audit](../../_process/research/2026-10-05-generative-foundation-review/root-foundation/CUE-GROUNDING-METHODS.md) reconstructs the experimental design and records its limitations. The [candidate audit](../../_process/research/2026-10-05-generative-foundation-review/root-foundation/REASON-ACTION-EMPIRICAL-CANDIDATES.md) provides the research context. Any computation using the preview must identify that source boundary and retain the unresolved original-file and sample-size questions. Supplement preservation, preview transcription verification and substantive empirical analysis are distinct achievements.
