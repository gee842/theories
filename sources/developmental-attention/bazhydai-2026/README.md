# CuriGaze public source preservation

Original bytes from [OSF ndthz](https://osf.io/ndthz/), accompanying Bazhydai, Wong, Altmann, Jones and Westermann, [*No Evidence for Curiosity-Driven Information Selection Advantage in Infants’ Novel Word Learning*](https://onlinelibrary.wiley.com/doi/10.1111/desc.70101), Developmental Science 29(1), e70101 (2026; first published 28 November 2025). Retrieved 8 October 2026 for the [declared secondary analysis](../../../experiments/integrated-correction/general-framework/generative-basis/inquiry-correspondence/contingent-learning/PLAN.md).

[PROVENANCE.json](PROVENANCE.json) binds eight small original files to deposited SHA-256 hashes: six CSV summaries, the authors’ R script and README. Two original paginated file listings and node metadata are preserved. Public GET storage endpoints were used after canonical redirects returned rate limits. The R script was read, not executed. The standalone master log repeatedly returned HTTP 429 and was not acquired.

The inclusion file required by the R analysis is inside `Data.zip`. The archive was downloaded to temporary storage and verified against its deposited size and SHA-256. Only its original `Data/CuriGaze_log_Cleaned.csv` member was imported. [The archive/member receipt](cleaned-log-provenance.json) retains both hashes; the [extraction code](../../../experiments/integrated-correction/general-framework/generative-basis/inquiry-correspondence/contingent-learning/fetch_archive_log.py) reproduces that check. The large archive and raw trajectories are not copied into this repository.

The cleaned log selects 75 of the 77 participants in the earlier summary export. Membership supplies the primary inclusion population; the file does not establish individual exclusion reasons or identify yoking partners. The [analysis](../../../experiments/integrated-correction/general-framework/generative-basis/inquiry-correspondence/contingent-learning/README.md) preserves the complete export as sensitivity, without reporting individual demographic details. Fields named `LearnedHits` count gaze samples, not binary retention successes. Original terminology remains unchanged in the originals.

These public files are retained with attribution for reproducible research; no new license grant is asserted. Node/license metadata remain in their original API response. No source file was normalized or edited.

**来源范围。** 保留八个公开小文件的原始字节及存放哈希；另从已验证压缩包仅取出原始纳入名单。77人的导出与75人的正式纳入范围分开，未知排除原因和配对关系不补写。汇总层复算不等于从原始眼动轨迹复现整个处理流程。
