# Naming audit notes (scratch)

Base for "since 2026-10-12": main first-parent 355ca27b (last main commit before 10-12 00:00 +0700).
Lean: 62 files changed, 39 added. Records: 51 new, 71 modified (no title changed among the modified).
decls.tsv: added declaration names (from diff). vocab.txt: word frequency in those names.
counts.txt: reference counts per candidate (Lean / becoming-checks / records / chapters / _process).

Ren evidence for the financial cluster: sources/15-codex-theory-conversations/2026-10-06-nondual-core-tree-continuation.md
("付费记录"? 这个词选的很诡异，太市场了，不够基本) in addition to the 10-10 naming sources.
Ren's own words used as names: "make sense" (2026-10-12-framing-and-pairs.md l.22) -> Lean MakesSense;
"find the boundary condition for 无明" (2026-10-10-truth-exists-opening.md l.62) -> record title seeking-boundary;
"hijacked" (same file l.60) -> zh module-table lead 劫持 for Becoming.Capture.

Checkers: check_becoming.py (core + bridge incl. RepairComparison), check_fallible_inquiry.py (FallibleInquiry, Mathlib).
Probes in checkers do not reference any candidate name (only prose word "own").
Record bindings: source + receipt + /source_sha256/<module>; any byte change => re-point bindings to new receipt.
P36 precedent: aliases/proof names replaced outright; old names live only in history notes + plan §10 table + historical receipts.
