---
name: «道源» 完全自指之道 完成 (2026-05-07)
description: Foundation/Wen/DaoSource.lean — 16-命受控文言之"道判"，五相俱（形/解/印/执/义）证毕
type: project
originSessionId: 858e08c8-dc07-40e1-b988-8bda67574672
---
On 2026-05-07 (same day as Phase 4 终章 landmark), `Foundation/Wen/DaoSource.lean` was added — the path-丙 收口 piece. Total project jobs: 2823 → 2833.

«道源» is a 16-instruction controlled-wenyan program that exercises all 12 字 of the YiInstr ISA and computes the same 是道非道 verdict as `daoJudgeProg` (天道 ↔ y3=y4).

**Why:** «微核源» (WenyanSelfHost) was a 4-相 PoC ("展练十二字"). «道源» upgrades to 5 相 by adding 义之自指 — the program's runtime semantics match a Lean-side propositional statement about hexagram structure.

**The 5 相 (all native_decide-witnessed):**
- 形: `«判型良» «道程» = true`
- 解: `«解程» «道源» = some «道程»`
- 印: `«印程» «道程» = «道源»`
- 执: `∀ h, runFuel 64 halts`
- 义: `∀ h, .cur.2 = 已 ↔ h.y3 = h.y4`

Plus: `«道程_eq_daoJudge»` anchors the program to BaguaTuring's daoJudge (核层); `«道源_文核同源»` lifts WenyanReflect's reflection identity to «道程». Top-level theorem `«道之自指»` bundles the 5-相 conjunction.

**How to apply:**
- This is the canonical "user wrote a 文 that exercises the full interpreter" piece. Treat it as the publication-worthy companion to «微核源».
- The program is cuo-equivariant by construction (every instruction it uses is) — consistent with the YiInstr ceiling memory.
- 0 sorry / 0 axiom in this file; full lake build still 0-sorry baseline.
- File location: `formal/SSBX/Foundation/Wen/DaoSource.lean`. Index entry in `formal/SSBX.lean` between `WenyanSelfHost` and `Demo`.
