---
name: Lean 4 CJK identifiers require «» (no bare-CJK)
description: Stock Lean 4 (incl. master nightly) cannot accept bare CJK identifiers; «» quoting is mandatory for all CJK names
type: feedback
originSessionId: 0e41811f-cbc6-4d9b-b2bf-291360840d4b
---
Stock Lean 4 (verified up to v4.30.0-rc2 and master) **cannot** parse bare CJK characters as identifiers. `Init/Meta/Defs.lean::isLetterLike` whitelists only Greek, Coptic, Polytonic Greek, the Letter-like block (ℕ/ℤ), Latin-1 supplement, Latin Extended-A, and math script. CJK Unified Ideographs (U+4E00–9FFF) and Lo-category chars are NOT in there. `Char.isAlpha` is ASCII-only (`'A'..'Z'`/`'a'..'z'`). So `def 道源` fails; `def «道源»` is the only working form.

**Why:** Investigated 2026-05-07 by user request "有没有办法把 lean 变量名直接改文字". Verified via `~/.elan/toolchains/leanprover--lean4---v4.30.0-rc2/src/lean/Init/Meta/Defs.lean` and master HEAD on github. Repo has 2645 «» occurrences across 94 .lean files — all forced by lexer, not stylistic.

**How to apply:**
- Never suggest stripping «» from CJK identifiers and rebuilding — it will not parse.
- The only ways to remove «» are: (a) fork lean4 + patch isLetterLike + rebuild from source (cost: ~4-7 hr first time because this repo's lakefile requires Mathlib master, whose precompiled olean cache is unusable on a patched toolchain → full mathlib rebuild), or (b) submit upstream RFC. User declined both 2026-05-07 — status quo accepted.
- When writing new CJK identifiers in this repo, always use «X» form. The full plan with patch sketch and tradeoffs is saved at `/Users/ren/.claude/plans/lean-snoopy-elephant.md`.
