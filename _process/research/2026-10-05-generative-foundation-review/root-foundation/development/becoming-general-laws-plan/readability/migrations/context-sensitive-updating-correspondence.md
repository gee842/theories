# Migration map: context-sensitive-updating-correspondence

Old record sha256 `f6253c93a1da6067ec635acd54f568e4fa230e7e1a6c12d514e2738e4420895f`; snapshot `_process/architecture/history/f6253c93a1da6067/context-sensitive-updating-correspondence.json`. Schema-2 readability migration (stream M2); documentary only, no claim, premise, status, dependency, reference or hash change.

| Old text | Type | New place |
|---|---|---|
| claim s1 "Reanalysis of 24 participants supports an increased perturbation contrast … its later finite-window effect is weaker." | statement of the result | `statement` (verbatim, both languages) |
| hypotheses[0..2] | premises | `hypotheses` (unchanged) |
| correspondence s1–s2 | correspondence | `correspondence` (unchanged) |
| dependencies[0] (reuses situated-recovery-empirical-correspondence) | link | `dependencies` (unchanged) |
| counterexamples[0] (cue-change interval includes zero; weaker later cue influence; alternatives) | adverse results | `counterexamples[0]` (unchanged) |
| limitations s1a "Does not identify a unique latent mechanism" | non-implication | `does_not_show[0]` |
| limitations s1b "… infinite convergence" | scope | `does_not_show[1]` |
| limitations s1c "… complete situational understanding, arbitrary new concepts, autonomous final goals" | correspondence | `does_not_show[2]` |
| limitations s1d "… or full cross-scale biological joint validation" | scope | `does_not_show[3]` ("does not provide"; zh 未提供 for 未识别, same meaning for a validation) |
| validation_scope s1–s2 | evidence | `validation_scope` (unchanged) |
| next_delta s1 | next step | `next_delta` (unchanged) |
| history[0] "extending the 16-person recovery study with complete 24-person updating correspondence …" | provenance + completed connection | `history[0]` (unchanged); the connection as `progress[0]`, anchored to the integration study §43 |

Counts: 8 old sentences or sentence parts outside history (1 claim, 4 limitation parts, 2 validation_scope, 1 next_delta; 2 correspondence kept). Destinations: statement 1, does_not_show 4, validation_scope 2, next_delta 1, correspondence 2 (unchanged); progress 1 anchored line from history[0]. Standard boundaries: none cited.
