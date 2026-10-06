# Public access audit: agentic misalignment and training

Preserved 6 October 2026 for the generative-grounding alignment assessment. This is a bounded source snapshot and availability audit, **not a complete release of experiment data or an independent replication**.

## Originals

The [retrieval record](metadata/retrieval.json) binds every downloaded original to its requested and final URL, HTTP status, retrieval time, byte count and SHA-256. HTTP response headers are also retained. [manifest.json](manifest.json) binds all package files other than itself.

- [Agentic Misalignment in Summer 2026](original/summer-2026.html): [official article](https://alignment.anthropic.com/2026/agentic-misalignment-summer-2026/).
- [Teaching Claude Why](original/teaching-claude-why.html): [official article](https://alignment.anthropic.com/2026/teaching-claude-why/).
- [Viewer entry](original/viewer/index.html), [client JavaScript](original/viewer/assets/index-Ivi1Vlum.js), and [complete served manifest](original/viewer/static/manifest.json): from the article-linked [public viewer](https://www.aenguslynch.com/portfolio-transcript-viewer/). JavaScript was inspected as text, not executed.
- Two JSON schema exemplars, selected by manifest order: the first `mislabel-input-*` entry and first selected multi-turn motivated-mislabeling case. Their paths and exact schemas are recorded in [availability.json](metadata/availability.json). They are not a representative sample of outcomes.

The original HTML files may refer to remote styles, images or scripts. They are exact response bodies, not self-contained rendered editions. No remote image copies, complete site mirror, generated model calls or evaluated benchmark actions are included.

## What is available

The served viewer manifest has 440 distinct IDs, 439 entries with an `href`, and a `generated_at` value of `2026-05-28T19:23:05.966Z`. Its motivated-mislabelling section has 24 entries: 18 judge-input transcripts and six selected multi-turn cases. The input exemplar contains target messages and annotations; its notice explicitly excludes seed instructions, auditor scaffolding and full event/message logs. The selected multi-turn exemplar includes auditor messages.

**Neither the manifest nor these schemas exposes the repeated one-turn judge-output matrix** needed to compare 18 inputs × five calls × three consequence conditions for one model. The historical condition strings in input filenames identify the earlier process that produced those inputs; they must not be relabeled as the later judge experiment's condition assignments. `judge_highlights` are annotations, not a table of repeated judge-call outputs.

This conclusion concerns the verified public release. It does not prove that the authors lack the data or that no other release exists. The manifest's date precedes retrieval and the page's served last-modified date; it is not evidence that every later article experiment is represented. Published outcomes were already read during source discovery. No new scientific outcome aggregate has been computed.

## Access, rights and scope

The first plain Python `urllib` request to the viewer returned HTTP 403. The article was available through web reading, and the viewer/assets returned HTTP 200 using `curl` with a browser user agent. No credentials or access controls were bypassed.

No explicit dataset or source-code reuse license was located in these served files. Public availability is not a public-domain or open-license claim. Preserve attribution and original notices. The separate MIT license of the 2025 experiment repository is **not** applied to this 2026 material.

The [research availability note](../../_process/research/2026-10-05-generative-foundation-review/root-foundation/MOTIVATED-MISLABELING-AVAILABILITY.md) gives the identified comparison and its limits. Shared source and research indexes are maintained separately by the integrating session.
