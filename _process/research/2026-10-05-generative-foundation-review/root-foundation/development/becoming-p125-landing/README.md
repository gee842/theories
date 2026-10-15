# P125 landing kit: observation as a route from what is observed

Branch `p125-observation` (worktree `.claude/worktrees/p125`), on main 17edc6d2 (after P123). Everything here
is already applied and committed on the branch; the scripts are kept so a rebase can replay them.

- `apply_docs.py W [SECTION=159]`: root import and module bullet, checker core list and scope, Lean README row
  and within-layer imports; chapter §2 paragraph (after the Thresholds paragraph), "Part I stated whole" item,
  §8 further proof (how a formation comes to observe a stock, now given), §9 row, two glossary rows; study
  section and English paragraph. Follow-up for Ren's "agree in general" (16 October): the chapter's P124
  paragraph and study §157 mark P124's readings agreed by Ren.
- `make_record.py ROOT [SECTION=159]`: the record `observation-is-a-route` (laws partition all 32
  declarations of `Becoming/Observation.lean`); paired notes in `loops-within-what-a-law-reads` (readings
  agreed, rename `Thresholds.le_of_not_lt` → `Thresholds.le_of_not_not`, Thresholds proof reference rehashed,
  source added, next step trimmed, related) and `runaway-distance-unregistered` (next step trimmed, related).
- `study.md`, `study-en.md`: the study section and English paragraph (`{SECTION}` placeholder).

Edited directly in the module: `Becoming/Thresholds.lean` (rename, its docstring, readings marked agreed, the open
item pointing to `Becoming.Observation`).

Verified: `scratch_build.py` — Becoming.Observation 27 theorems / 32 declarations, Becoming.Thresholds 38 / 45,
axiom reports empty, no warnings; decidability inventory scratch run unchanged (no row for either module);
style lint clean. Focused record check: the only errors are the receipt bindings of `observation-is-a-route`
and `loops-within-what-a-law-reads` (Thresholds source changed), plus chapter/study drift, all for landing.
