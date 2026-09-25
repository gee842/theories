---
name: MetaInterp Phase C — partial (2026-05-08, C.0+C.A+C.C done)
description: Bounded UniversalInterpSpec + sub-dispatch trees + 11 dispatch routing proofs (~1500 LOC delivered, fetch architecture issue identified)
type: project
originSessionId: 54a0fbda-ac51-4eaf-976e-6e5ed0b8890c
---
2026-05-08：Phase C 之 C.0 / C.A / C.C 已完成并 push 到 `claude/nice-golick-d43a28`（commits 7cfb0b6 + 68ee71e on PR #13），共增 ~1500 LOC，0 sorry / 0 axiom。

## 已完成

**C.0 — Bounded UniversalInterpSpec**：[KleeneInternal.lean](formal/SSBX/Foundation/Bagua/KleeneInternal.lean) 加入 `JumpTargetsBoundedInstr` / `JumpTargetsBounded` / `ProgBounded` predicates 与 `UniversalInterpSpecBounded` / `UniversalInterpExistsBounded`（71 LOC）。**未做**：尚未把整条 `path_to_zero_axiom` 链改为 bounded 版（推迟到 C.F 一并做以减少 churn）。

**C.A — Sub-dispatch trees**（~1100 LOC）：
- [Dispatch.lean](formal/SSBX/Foundation/Wen/MetaInterp/Dispatch.lean) 之 `subDispatchSetShi_routes`（3-way Shi dispatch）+ 把 `subDispatchFlipYao` 从 2-instr placeholder 升级为 9-instr 6-way dispatch + `subDispatchFlipYao_routes`
- [SubDispatch_BranchShiEq.lean](formal/SSBX/Foundation/Wen/MetaInterp/SubDispatch_BranchShiEq.lean)（new file, 143 LOC）：4-instr outer 3-way Shi dispatcher + per-s routing proofs
- [SubDispatch_BranchYaoEq.lean](formal/SSBX/Foundation/Wen/MetaInterp/SubDispatch_BranchYaoEq.lean)（new file, 395 LOC）：9+9-instr 两层 36-way (i,j) dispatcher + 12 routing proofs

**C.C — 11 dispatch routing proofs**：`dispatchTree_routes_{nop,setShi,flipYao,hu,cuo,zong,branchYaoEq,branchShiEq,jump,push,pop}` 全数证（每个 fuel 3-7，simp-driven）。

## 关键 tactic 教训

`Fin n` 之 helper lemma 用 `∀ i : Fin n, ...` 形式 + `match v, hv with | k, _ => decide` 会触发 "Expected type must not contain free variables" — `_` proof 变 metavariable，`decide` 无法 reduce。**workaround**: 每个 literal 单独写一条 helper（`encFin6_0_y1_eq_y6 : (encFin6 (0 : Fin 6)).1.y1 = ...`），`(n : Fin 6)` 字面量配合 simp 之 view。

## 待做（C.B / C.D / C.E / C.F，~3000+ LOC）

**C.B — Fetch 完成（D1-D4）**：~600-900 LOC。**架构问题待决**：
- META.cur 在 fetch/dispatch 期间被借用承载 TAG cell；BlockPre 之 `μ.cur = sim.cur` 契约需在 block 入口前由某 mechanism 恢复。
- 候选设计：fetch 之第 1 条指令 push sim.cur 至 history 顶端，每个 block 入口加一条 pop 恢复 cur（每个 block +1 instr）。但 12 个 executeBlock 都需 prefix `pop` — 大改造。
- D1: counted-loop simulation 推广到 non-empty body（~300 LOC induction）
- D2: encProg-skip protocol 用 SkipInstr arity 表跳过 sim.pc 个指令（~200 LOC，需补 5 个 non-zero-arity opcode 之 dispatch 路径）
- D3: scratch unwind = D1 inverse（~200 LOC）
- D4: halt detection（~100 LOC）

**C.D — metaInterpProg 组装**：~250 LOC。等 C.B + 架构决策。

**C.E — UniversalInterpSpec 主定理**：~1200-1500 LOC。loop invariant + per-step simulation + by-induction-on-fuel 双向 iff。这是 Phase C 最大块。

**C.F — Discharge axiom**：~50 LOC mechanical。等 C.E。

## Phase C 资源观

原计划估 15-22 天 / ~3550 LOC。实际首日（5/8）落 ~1500 LOC（C.0+C.A+C.C 完整），节奏与计划相符。剩余 C.B+C.D+C.E+C.F 估约 2-3 周 focused work；C.E 主定理是关键瓶颈。

**Why:** 这是把 `kleene_recursion_axiom` 从 4 axioms 削减到 3 之工程项（universalInterpExists 由 axiom 派生为 theorem）。下游 Rice/不可判定结论不变，仅 axiom **scope** 收窄。

**How to apply:** 接续工作从 C.B 开始；首先决定 cur save/restore 架构（在 [Fetch.lean §0](formal/SSBX/Foundation/Wen/MetaInterp/Fetch.lean) 已有 D1-D4 deferred 注释）。Plan blueprint 见 [/Users/ren/.claude/plans/sparkling-floating-perlis.md](/Users/ren/.claude/plans/sparkling-floating-perlis.md)。
