---
name: V₄ Shi migration complete (2026-05-10)
description: Full codebase migrated Cell192→Cell256 (3-state→4-state Shi V₄), 13-issue doctrine alignment, lake build 3648/3648 jobs, 0 sorry added
type: project
originSessionId: dc179491-4360-455e-b86e-f377b6bf4de4
---
The doctrine-alignment refactor (plan: crystalline-sprouting-cocoa.md, 13 issues) landed across ~80 files in one parallel session on 2026-05-10.

**Commits**: `7de5064` (77 files, +6092/-2585) + `0003224` (Modern/* cascades, +10/-10).

**What changed structurally:**
- `Shi` extended from 3-ctor `{ji, jin, wei}` (Z/3 cyclic) → 4-ctor `{dao, ji, jin, wei}` (V₄ Klein four-group, `dao` = identity)
- `Cell192` (64×3) → `Cell256` (64×4) as the canonical R₈ atom layer
- `shiNext` Z/3 cycle → `Shi.cuo` V₄ involution (period 2, self-inverse). Order-3 lemmas become order-2.
- 印 (yin) / 投 (tou) atomic operators rewritten as XOR masks: `yin_mask = (qian, ji)`, `tou_mask = (qian, wei)`
- AddCommGroup-shape (`Add/Zero/Neg/Sub` + `SMul`) on Cell128/Cell256 with explicit Cayley `ι/ε` (no Mathlib typeclass dep)
- New `Foundation/Hierarchy/` subdirectory: `R5_Wuyao.lean`, `LiftProject.lean` (8 R-layer pairs + retract laws), `Operators/Atomic.lean`, `Operators/V4Outer.lean`
- New `Foundation/Notation/OXNotation.lean`: `OX["xxxxxxxx"]` 8-char string macro for 256-cell literals (`o`=yang, `x`=yin)

**Files touched by major bucket:**
- Phase A (Cell128/Cell256 algebraic spine)
- Phase F.1 (WenyanSelfInterp full migration: 1869 → 1084 LOC; **dropped legacy `dispatchProg` + `universalMetaInterp`** — base-192-specific routing; Phase 2.3 12/12 cur-effect simulation theorems retained)
- Phase F.2 (BaguaTuring), F.4 (GodelLi/KleeneInternal), F.5 (OperatorCellMap/Semantics)
- Phase F.x batches (F.x.0..F.x.5 ~25 files): Wen/*, Text/*, Modern/*, Wen/*Quine*
- Phase F.3 (MetaInterp/* 13 sub-files split into A/B/C; Dispatch tree restructured 4×3 → 3×4 = 16 instructions; SubDispatch_BranchShiEq extended 3→4-way)

**Verified**:
- `lake build SSBX` returns **3648/3648 jobs, 0 errors**
- `R8_complete` axiom audit: only `propext` + 3 `native_decide` axes (no new project axioms beyond pre-existing `kleene_recursion_axiom`)
- 0 sorry added (2 pre-existing in WenyanParserGeneral untouched)

**Still pending** (not blocking — separate phases):
- Re-derive base-256 `dispatchProg` + `universalMetaInterp` (F.1 dropped them)
- Phase B.1: YinBit/GuoBit dedup between Cell128 and Cell256
- Phase B.2: Shi → abbrev `Bool × Bool` decision (would simplify `Shi.toYinGuo` bijection)
- Phase F.6: delete `Cell192.lean` (only `SSBX.lean` still imports it)
- Phase C: move files into `Foundation/Hierarchy/` subdirectory layout
- Phase G: doctrine doc references to new Lean code paths

**How to apply:** any new code at the R₈ layer should use `Cell256` directly. Use `Cell256.shiCuo` for V₄ involution (NOT old `shiNext`). Use `OX["..."]` for cell literals. For new operators, decide if they're XOR-mask atomic (use `Cell256.yin/tou` pattern) or non-XOR V₄-outer (use `Cell256.zong/hu/cuoZong` pattern).
