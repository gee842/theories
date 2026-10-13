# Migration map: encounter-control-and-retention

Old record sha256 `b2563eeef5041aa365dfea25cc3d8d8ceb5d64efcd00fb18e7f630d461c888f0`; snapshot `_process/architecture/history/b2563eeef5041aa3/encounter-control-and-retention.json`. Schema-2 readability migration (stream M2); documentary only, no claim, premise, status, dependency, reference or hash change. Study: `ACQUIRED-SEGMENTATION-INTEGRATION.md` (§§19–29).

| Old text | Type | New place |
|---|---|---|
| claim s1 "Reanalysis of the public CuriGaze inclusion sample, 75 participants and 451 trials, gives Curiosity−Yoked … [−10.38,+7.69]." | statement of the result | `statement` s1 (verbatim, both languages) |
| claim s2a "It establishes neither a retention advantage nor equivalence" | non-implication | `does_not_show[0]` (verbatim) |
| claim s2b "… constraining an automatic selection-to-learning-advantage correspondence." | statement of the result | `statement` s2 ("This constrains …"; zh 它约束… verbatim) |
| hypotheses[0..2] | premises | `hypotheses` (unchanged) |
| correspondence s1–s2 | correspondence | `correspondence` (unchanged) |
| dependencies[0], [1] | links | `dependencies` (unchanged) |
| counterexamples[0] | adverse results and disclosed discrepancies | `counterexamples[0]` (unchanged) |
| limitations s1a "Does not identify a unique psychological mechanism, social cause" | non-implication | `does_not_show[1]` |
| limitations s1b "… long-term memory, consciousness or evolutionary origin" | scope | `does_not_show[2]` |
| limitations s2a "The 75-person primary analysis and 77-person sensitivity remain separate" | premise (duplicate) | `hypotheses[0]` ("Retain the earlier 77-person export as sensitivity"), unchanged |
| limitations s2b "intervals have no sequential-design guarantee" | premise (duplicate) | `hypotheses[1]` ("sequential-design coverage is unproved"), unchanged |
| validation_scope s1–s3 | evidence | `validation_scope` (unchanged) |
| next_delta s1 "Preserve the completed conditional connections." | process instruction | `next_delta` opening clause ("Building on the preserved conditional connections"); the connections are listed in `progress` |
| next_delta s2 "Next identify how formed access and retained source/order information guide actual use …" | next step | `next_delta` (verbatim content) |
| next_delta s3 "Primary evidence constrains automatic transfer without identifying a unique mechanism or evolutionary history." | completed connection with its boundary | `progress[3]` (study §29) |
| history[0] "directly reconstructed later target looking … integrated with the existing study and full objective" | provenance + connection | `history[0]` (unchanged); `progress[0]` (study §20) |
| history[1] (study sections 21–23) | provenance + connection | `history[1]` (unchanged); `progress[1]` (study §23) |
| history[2] (historical-applicability composition and counterreview) | provenance + connection | `history[2]` (unchanged); `progress[2]` (study §26) |
| history[3] (§§27–29, five primary sources) | provenance + connection | `history[3]` (unchanged); `progress[3]` (study §29) |

Counts: 13 old sentences or sentence parts outside history and the unchanged correspondence (3 claim parts, 4 limitation parts, 3 validation_scope, 3 next_delta). Destinations: statement 2, does_not_show 3, hypotheses 2 (already present), validation_scope 3, next_delta 2, progress 1; in addition 4 history entries each gained an anchored progress line (history itself unchanged). Standard boundaries: none cited.
