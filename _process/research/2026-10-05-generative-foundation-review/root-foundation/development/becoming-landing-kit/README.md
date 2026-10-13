# Shared Becoming landing scripts

This kit completes the P76/P81 landing draft preserved at `1860d9e3`, and is also used by the following batch. It does not run Lean, classify decidability, commit, or declare a package accepted. The integrator runs one checker at a time in the work-board order. All paths below are relative to the checkout root; `RUN` is a package configuration directory and `W` the landing checkout.

## Interface

1. `python3 -B land_lean.py RUN W` copies the configured source modules and registers them in the root, checker and Lean README. Each package's optional `layer` defaults to `L3`; it must match its root-module bullet.
2. Run `check_becoming.py` and then `check_correction_inquiry.py`, with incremental reuse and `LEAN_TIMEOUT=3600`. Read both receipts and confirm success. Regenerate and, where necessary, explicitly classify the decidability inventory on those checked bytes. `python3 -B zero_count.py W` then updates the bilingual inventory totals in the zero-premise plan.
3. After reviewing the affected chapter and reading entry, `python3 -B land_docs.py RUN W S BASE` adds study sections from `S`, the plan and chapter text, the reading entry, totals, the current periphery receipt and the study's range of unreviewed integration text. The reading entry must match the chapter at `BASE`, the pre-landing commit, before its hash is refreshed.
4. `python3 -B make_records.py RUN W REVIEWED_AT_UTC S` builds source-bound records from passed receipts and runs the configured deltas. It advances `reviewed_at_utc` for records whose documentary content the deltas changed. The timestamp uses the form `2026-10-13T00:00:00+00:00`.
5. After reviewing this landing's source changes, `python3 -B repoint.py RUN W BASE` updates existing receipt scopes, periphery closure counts and source hashes. Only hashes equal to the source at `BASE` are refreshed; other drift is reported and left untouched. New records are already bound by step 4 and are skipped. The repoint operation does not change documentary review dates.
6. Run the reading and Lean catalogue generators, `make research-render`, and the session-map capture. Reconcile any remaining drift, then repeat the guarded repoint operation and render if generated references changed. Run `make research-check` and the catalogue, session-map, generativity-chain and added-link checks. A failed check must be understood before landing.

The mutation steps use exact anchors and normally fail when rerun on a checkout to which they were already applied. Keep `BASE` fixed throughout one landing. Read generated-page guard failures and preserve concurrent prose before regenerating; do not bypass a guard.

## Configuration

`PACKAGES` contains `module`, `package`, `key`, `prefix`, `after`, `scope_before`, `bullet`, `scope`, `readme_zh`, `readme_en`, `imports_zh`, `imports_en`, and optionally `layer`. An optional `study_heading` prepends a numbered heading to an original Chinese study snippet that has none. The named `after` module must already be registered; packages may follow one another. `PLAN_ZH`, `PLAN_EN`, `CHAPTER_EDITS`, `READING` and optional `VALUES` supply bilingual documentation. Study snippets and Lean files remain in their original package directories.

`RECORDS` maps stable IDs to `package` keys, source section headings, checked declaration names, exact `builds_on` declarations and provenance paths. `HISTORY` supplies the authored history. `DELTAS` lists scripts called with `W S`. Optional `LABEL` names the landing in receipt-repoint history. The record writer checks names and sections against the actual receipt; synthetic dry-run receipts are only for disposable documentation rehearsals and must never be landed as proof evidence.

No new scientific claim is introduced by this kit. Source assertions, supplied hypotheses, review limits and remaining questions belong to the package drafts and canonical records.

A package may supply `study_suffix_zh` and `study_suffix_en` to append source-bound integration notes to preserved study snippets before placeholders are filled. They default to empty strings. `study_heading` supplies a missing numbered Chinese study heading without altering the original package snippet.
