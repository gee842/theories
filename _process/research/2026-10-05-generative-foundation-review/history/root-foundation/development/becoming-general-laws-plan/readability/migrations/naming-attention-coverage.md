# Migration map: naming-attention-coverage

Old record sha256 `45318e84ce3a2dd31b2094aaf40abe112dc7d394dc3987be97c3ae92993a74c3`; snapshot `_process/architecture/history/45318e84ce3a2dd3/naming-attention-coverage.json`. Schema-2 readability migration (stream M2); documentary only, no claim, premise, status, dependency, reference or hash change. Study: `ACQUIRED-SEGMENTATION-INTEGRATION.md` (§§17–29).

| Old text | Type | New place |
|---|---|---|
| claim s1–s2 "Among 1,508 public naming records … 35 infants show such cases. This limits automatic naming-to-target-gaze measurement correspondence." | statement of the result | `statement` (verbatim, both languages) |
| hypotheses[0..2] | premises | `hypotheses` (unchanged) |
| correspondence s1–s2 | correspondence | `correspondence` (unchanged) |
| dependencies[0] (encounter-selection-and-revision; conditional proof and failure cases preserved) | link | `dependencies` (unchanged) |
| counterexamples[0] (393 five-second windows; 45 zero/zero windows; publication/export binning unresolved) | adverse results | `counterexamples[0]` (unchanged) |
| limitations s1a "Does not identify mislearning" | correspondence | `does_not_show[0]` |
| limitations s1b "… a unique algorithm, developmental causation of coordination" | non-implication | `does_not_show[1]` |
| limitations s1c "… consciousness or evolutionary psychology" | scope | `does_not_show[2]` |
| limitations s2a "Not an exact replication of all published analyses" | kind of evidence | `validation_scope` (appended as its last sentence, both languages) |
| limitations s2b "… and does not change existing conditional theorems" | relation to another record | `dependencies[0].detail` ("preserving the conditional proof and failure cases"), unchanged; also `progress[1]` ("leaving this claim, proof and failures unchanged") |
| validation_scope s1–s3 | evidence | `validation_scope` (unchanged) |
| next_delta s1 "Preserve the completed conditional connections." | process instruction | `next_delta` opening clause ("Building on the preserved conditional connections"); the connections are listed in `progress` |
| next_delta s2 "Next identify how formed access and retained source/order information guide actual use …" | next step | `next_delta` (verbatim content) |
| next_delta s3 "Primary evidence constrains automatic transfer without identifying a unique mechanism or evolutionary history." | completed connection with its boundary | `progress[4]` (study §29) |
| history[0] "directly tested automatic gaze coverage … Specified the next connection through coordination cues, encounter admission/weighting and retained correction." | provenance + connection | `history[0]` (unchanged); `progress[0]` (study §18) |
| history[1] "reviewed added study sections 19–20. A later-retention measure adds an empirical constraint …" | provenance + connection | `history[1]` (unchanged); `progress[1]` (study §20) |
| history[2] "reviewed study sections 21–23. Acquired source relations now generate binding alternatives …" | provenance + connection | `history[2]` (unchanged); `progress[2]` (study §23) |
| history[3] "reviewed the same study's historical-applicability composition and counterreview …" | provenance + connection | `history[3]` (unchanged); `progress[3]` (study §26) |
| history[4] "reviewed the same study's added §§27–29, five primary-source correspondences …" | provenance + connection | `history[4]` (unchanged); `progress[4]` (study §29) |

Counts: 13 old sentences or sentence parts outside history and the unchanged correspondence (2 claim, 5 limitation parts, 3 validation_scope, 3 next_delta). Destinations: statement 2, does_not_show 3, validation_scope 3 kept + 1 moved in, dependency detail 1 (already present), next_delta 2, progress 1; in addition 5 history entries each gained an anchored progress line (history itself unchanged). Standard boundaries: none cited.
