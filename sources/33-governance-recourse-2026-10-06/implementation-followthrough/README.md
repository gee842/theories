# Implementation follow-through: source reading package

Access date: 6 October 2026. This subpackage extends the historical Robodebt source audit with three later reports. It does not change the parent package's originals, reading editions, metadata or manifest.

**Preservation scope: selected web-reader text, not original PDF bytes.** One bounded local GET per report failed: the 2021 and 2022 Ombudsman sources returned HTTP403, and the annual-report request timed out after 25 seconds. No error body was saved as a report. The empty `original/` directory contains no source artifact. The reading editions retain selected complete reader lines, page labels and OCR artifacts; discontinuities are explicit.

| Report/version | Authoritative URL | Local edition |
|---|---|---|
| April 2021, report2/2021 | [Ombudsman PDF](https://www.ombudsman.gov.au/__data/assets/pdf_file/0014/112442/Services-Australias-Income-Compliance-Report.pdf) | [Scope, methods and Rec8](reading/ombudsman-2021-web-excerpts.txt) |
| October 2022, report04/2022 | [Ombudsman PDF](https://www.ombudsman.gov.au/__data/assets/pdf_file/0029/286517/Did-they-do-what-they-said-they-would-Volume-2.pdf) | [Methods, Rec4 and Rec8](reading/ombudsman-2022-web-excerpts.txt) |
| Services Australia Annual Report2022–23, official October2023 URL | [Agency PDF](https://www.servicesaustralia.gov.au/sites/default/files/2023-10/annual-report-2022-23.pdf) | [§§7.10, 8.1 and8.5](reading/services-australia-2022-23-web-excerpts.txt) |

The [evidence note](../../../_process/research/2026-10-05-generative-foundation-review/foundation-assessment/GOVERNANCE-NOTICE-EVIDENCE.md) owns the methodological interpretation and printed pinpoints. Original report dates differ from retrieval date. No current-law or current-completion inference is made. A separate [appendix search-reader description](reading/ombudsman-2022-appendix-search-description.txt) preserves the tool's indexed description of the September2022 agency letter at an alternate official URL. It is not a verified visual transcription; the attachment was not inspected. Identity of the two official PDF response bodies is unverified.

[Retrieval metadata](metadata/retrieval.json) records the local attempts; response headers are retained except `Set-Cookie`, whose omission is recorded. [Reader provenance](metadata/reading-provenance.json) identifies selections and access limitations. The source copyright/license pages were not preserved, and no redistribution license is inferred. These are attributed research reading editions rather than claimed official reproductions.

[Manifest](manifest.json) hashes all stable package payloads and the [verification receipt](metadata/verification.json). The receipt verifies the payload hashes, source-note links and unchanged pre-existing parent files against the [before snapshot](metadata/parent-snapshot-before.json). These checks establish local preservation integrity, not the truth of institutional claims or fidelity of unavailable PDF bytes.
