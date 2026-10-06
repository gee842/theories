# Participation and consequence: two studies and a primary criticism

6 October 2026. Source preservation for the [supporting research note](../../_process/research/2026-10-05-generative-foundation-review/root-foundation/PARTICIPATION-CONSEQUENCE-COMPARATORS.md). This package contains three successfully retrieved primary documents, their derived reading editions and access metadata. It is not a new empirical dataset or replication. The published criticism was added after independent review of the initial two-source note; the initial originals and reading editions remain unchanged.

| Original | Primary source and byte identity |
|---|---|
| [Kramar–Alim PDF](original/kramar-alim-2021.pdf) | [Author-hosted TUM PDF](https://www.bpm.ph.tum.de/wp-content/uploads/2023/07/2021-PNAS-Memory-Hierarchy-Alim-Kramar.pdf), DOI [10.1073/pnas.2007815118](https://doi.org/10.1073/pnas.2007815118); 1,253,573 bytes; SHA-256 `1d3a504f89fa1c717287b65f0e4a63ce6161bdbcfb8507b84eddfefcfc89f8a2`. |
| [Sonoda et al. XML](original/sonoda-2012.xml) | [Europe PMC primary XML](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3391464/fullTextXML), DOI [10.1098/rsbl.2012.0085](https://doi.org/10.1098/rsbl.2012.0085); 36,170 bytes; SHA-256 `233239007e7ba72f428d691536d2b1741a9592eb6d7626ac5dd0eec13cbbfe4a`. |
| [Reiber–Nogueira Júnior HTML](original/reiber-nogueira-2021.html) | [Primary PMC response](https://pmc.ncbi.nlm.nih.gov/articles/PMC8433532/?report=xml), DOI [10.1073/pnas.2105928118](https://doi.org/10.1073/pnas.2105928118); 102,732 bytes; SHA-256 `9571bb31770aa01239b51d96266329ae606d92317ed9027c04b94585ce4680c3`. The successful response is HTML despite the query parameter. |

[Retrieval metadata](metadata/retrieval.json) preserves observed HTTP responses, dates, final URLs and headers. The failed Kramar–Alim XML request is recorded separately from successful originals. Direct PMC browser challenges did not yield preserved article originals. No claim of independently checked publisher-PDF byte equivalence is made.

[Criticism access and reply-search record](metadata/criticism-reading.json) records the failed XML request, successful alternate PMC response and bounded search. The [letter reading edition](reading/reiber-nogueira-2021.txt) is the article element extracted with Python's HTML parser; it is not original HTML. All four body paragraphs and references were read. No reply was identified in the bounded search; no claim of nonexistence is made. Set-Cookie headers are omitted throughout as irrelevant transient session state, with the omission explicitly recorded. Original document bytes are unchanged.

[Reading scope](metadata/reading-scope.json) distinguishes full main-text reading, visual Figure 5 inspection, XML-only figure captions and uninspected supplements. [PDF text](reading/kramar-alim-2021.txt) was extracted with `pypdf`; [XML body text](reading/sonoda-2012.txt) was extracted from XML sections. These are portable reading editions, not original document bytes or new observations. No model, controller or scientific analysis was run. The rendered page used for visual inspection is a reproducible scratch derivative and is not imported.

[Manifest](manifest.json) binds all ten other package files by SHA-256 and size. The study note states what the sources establish and which stronger interpretations remain unresolved.
