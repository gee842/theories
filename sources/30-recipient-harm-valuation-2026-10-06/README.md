# Recipient harm valuation: preserved primary sources

Retrieved 6 October 2026. This collection supports a retrospective audit of **Hernandez-Lallement, Attah, Soyman, Pinhal, Gazzola and Keysers (2020), “Harm to Others Acts as a Negative Reinforcer in Rats,” Current Biology 30, 949–961.e7**, [DOI](https://doi.org/10.1016/j.cub.2020.01.017). Preservation is not replication or proof of other-directed concern.

## Originals and access

- [Institutional publisher PDF](original/hernandez2020.pdf), from [KNAW](https://pure.knaw.nl/ws/portalfiles/portal/13278204/hernandez2020.pdf): 4,060,957 bytes, SHA-256 `70e20bd121156af8ff409be41020cdceec9b4ce415b7f00caa7a4b0ffea9ce17`. Its institutional cover identifies the version of record and cites final pagination; the embedded article retains in-press pagination 1–13.e1–e7. The 22-page file includes institutional cover and graphical abstract. Use PDF page numbers to disambiguate citations.
- [TrialByTrialChoicesMainPaper.csv](original/TrialByTrialChoicesMainPaper.csv): 16,683 bytes, SHA-256 `6c594ee27eb186b47f90b511d6173eb44dad27f5bc68692b04a9095c1a0d8b44`, [OSF original](https://osf.io/download/q4hvf/).
- [dataMainPaper.xlsx](original/dataMainPaper.xlsx): 64,550 bytes, SHA-256 `dee91bd9bce910d80e5eca1d0cea74c9d0839bf7f6ebe1334a656ada0bb674ef`, [OSF original](https://osf.io/download/q6m2a/).
- [dataMainPaper.csv](original/dataMainPaper.csv): 28,171 bytes, SHA-256 `8ecbff58da5de5e52420cd8163951219b9472de0ff8cfce7aefb4447af6f50df`, [OSF original](https://osf.io/download/7sxdg/).
- [license.txt](original/license.txt): unchanged OSF license, [original](https://osf.io/download/4gt9c/). Its original encoding is not UTF-8; CP1252 gives a readable interpretation. No transcoding of the original was performed.

The [OSF project](https://osf.io/65j3g/) is explicitly linked in the paper's resources table and data-availability statement. Its public API identifies all four saved OSF files as version 1. Every downloaded file's SHA-256 matches the preserved OSF metadata. The root file listing also contains FigureS1 and FigureS2 folders; their contents were not downloaded. This is complete preservation of the four root files, not the complete project.

## Rights and provenance

**The article and dataset have different licenses.** The PDF declares CC BY 4.0. The OSF project API calls its license “Other” and directs readers to license.txt, which specifies **Creative Commons Attribution–NonCommercial–ShareAlike 4.0 International**. The project records copyright Christian Keysers, 2020. Apply the deposited data license to the CSV/workbook; do not relabel them CC BY or CC0.

[metadata/retrieval.json](metadata/retrieval.json) records exact request and resolved URLs, HTTP headers, times, lengths and hashes. Raw project, file-list, individual-file, version-list and license API responses are preserved under metadata. [manifest.json](manifest.json) binds the files. [schema.json](schema.json) records the source structure and identity mapping without new scientific outcome aggregates. [The portable text](reading/hernandez2020.txt) is a pypdf extraction with explicit PDF-page delimiters; it contains extraction artifacts and is subordinate to the original PDF.

Earlier browser reads of the institutional PDF timed out, and exploratory direct requests sometimes returned HTTP 403; the final ordinary public download succeeded. All selected data downloads succeeded via OSF's advertised public download links. The license's first attempted UTF-8 reading failed; the unchanged bytes were subsequently read as CP1252. No access restriction was bypassed.

## Reading and analysis scope

The trial CSV has two header rows, 78 actor rows, one entirely blank trailing row and 88 columns. It gives four phases of 20 free-choice slots. Its explicit codes are 2 for the baseline-preferred/shock lever, 1 for the other lever, and 0 for a nonperformed trial. Actor 70, Shock 3 trial 11 is blank, not zero; this is outside the primary equal-food comparison. The entire CSV matches the workbook's cached Choice sheet values in all 7,128 cells. The summary CSV contains 142 actors and supplies sex, group, cohort labels and local rat labels. No explicit cage dictionary or per-animal physical lever force is supplied.

Published findings were read during discovery. Initial schema inspection also displayed the first three NoHarm actors' rows before protocol freezing. This is a prospective specification of a **retrospective** audit, not an outcome-blind study or new experiment. No new outcome averages or inferential statistics were calculated for this preservation audit.

See the [source/design assessment](../../_process/research/2026-10-05-generative-foundation-review/root-foundation/RECIPIENT-VALUATION-EVIDENCE.md) and [analysis protocol](../../experiments/recipient-harm-valuation/PROTOCOL.md). The latter is owned separately and determines which comparisons are authorized for analysis.
