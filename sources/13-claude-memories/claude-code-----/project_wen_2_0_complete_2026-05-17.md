---
name: wen-2-0-complete-2026-05-17
description: Wen 2.0 完成 — 12 spec 项 implemented (PR
metadata: 
  node_type: memory
  type: project
  originSessionId: 0d926a45-025f-4d63-a524-62d072e475ae
---

Wen 2.0 全部 spec 项 implemented + merged to main on 2026-05-17 (1 day after Wen 1.5).

## Spec 项之 PR 表

| 项 | 名 | PR | Commit |
|---|---|---|---|
| ① | HM type inference | #52 | `4a78769` |
| ② | user-def recursion (定递) | #53 | `b08e937` |
| ③ | namespace (用 NS) | #46 | `2205411` |
| ④ | user inductive types (类 NAME = ...) | #57 | `f958bcc` |
| ⑤ | pattern matching (析 X 为 P → E ...) | #62 | `3e68e38` |
| ⑥+⑩ | 曰 + 「」 quote brackets | #47 | `a3a28c5` |
| ⑦ | 真名词化器 (者 as Set, 属 member-of) | #63 | `b3eb9e0` |
| ⑧ | 所…者 / 之所以 relative clauses | #65 | `5f20406` |
| ⑨ | subject ellipsis (其 + cross-stmt λ) | #60 | `d88256f` |
| ⑪ | 执 「X」 quote-eval | #58 | `a8f6708` |
| ⑫ | rewrite rules (定 LHS 等 RHS) | #56 | `bcd2112` |
| ⑬ | ~~cell-level / V₄ Shi binding~~ | #49 | **REMOVED** — V₄ Shi doctrine-out |

亦有 2 fix PR: #54/#58 内含 `REPL.tyStr` fix; #59 `Namespace.lean` build fix (双 let-rec + 错 count + Decidable).

## 关键 API/类型新增

### Kernel (`WenDef.lean`)
- `Ty.user String` (④), `Ty.set Ty` (⑦), `Ty.quoted` (⑥)
- `Tm.userCtor (typeName ctorName : String)` (④)
- `Tm.match (scrut : Tm) (arms : MatchArms)` + `MatchArms` mutual inductive (⑤)
- `Tm.setOf (pred : Tm)` + `Tm.memberOf (x s : Tm)` (⑦)
- `Tm.quote (body : Tm)` + `Tm.unquote (q : Tm)` (⑥, ⑪)
- `Tm.fix (n : String) (t : Ty) (body : Tm)` (②)

### Runtime (`WenDefEval.lean`)
- `Value.userCtorV`, `Value.setV`, `Value.fixV`, `Value.quoteV` 之新 cons
- `applyFuel` fuel-bounded eval for ②/⑪/⑫ 等

### Surface (`WenSurface/...`)
- HM constraint solver `MTy = Ty + .mvar Nat` + Robinson unification (①)
- `wenyanCompileProgramWithNamespaces / WithDefs / WithEllipsis` 累加器三件
- 23 new chunk-leading 关键词支持: `定` `定递` `用` `类` `析` (decl); `执` `所` `之所以` `属` `其` `者` `曰` (in-expr); 5 final particles 乎/矣/哉/兮/也

## 设计 highlights

- **V₄ Shi 完全 doctrine-out (2026-05-17 user directive)** — Cell256 = R₈ = R₄² 从 squaring tower 派生，不作独立 axis. 见 [[v4-shi-doctrine-out-2026-05-17]].
- **0 sorry / 0 axiom** hard invariant 全程保持
- **R-tower 派生 doctrine** — 所有 cardinality 来源 R_{k+1}=R_k² (R₀..R₈)
- **5 redundant evaluator 之候选已 prune** in Wen 1.0 restructure (PR #30-37)
- **错等变 ceiling 已破** (PR #37) — YiInstr 之 v2 ISA universal Hex→Hex

## 工程笔记

- 11 features 在 24 hours 内 merged，via 多 agent 并行 + isolation worktree
- 多次 agent stalled (rate limit / stream timeout), recovery 用:
  - 显式 "commit each step within 15min" 提示
  - 手 push + PR (代 stalled agent)
  - Rebase agents (cleanup 对 ④ #57, ⑦ #63, ⑧ #65 之 conflicts)
- 主 conflict source: `EndToEnd.lean` 之 chunk dispatch + `WenDef.lean` 之 Tm/Ty 同步加 cons
- Lake build 之 cold start 30-60min — 用 targeted `lake build SSBX.Foundation.Wen.WenSurface.<module>` 替代

## 后续 (Wen 3.0?)

未实现项 (spec Part IV "不在 2.0"):
- LLVM/WASM 后端 (用户排除)
- 韵律 / 对偶 / 排比 (诗经楚辞 surface)
- GC / async / concurrency (破 pure R8 doctrine)
- Compile-time macros (部分由 ⑪ quote/unquote 覆盖)

可能 Wen 3.0 内容: 完整 exhaustiveness check on `析` (⑤ v1 限制), `属` infix 精化, 之所以 之 因 builtin (⑧ 当前是 app 退化), 设 `Tm.setOf` 之 finite enumeration 以便 X²-256 universe 内 decidable membership.

## How to apply

- 回 Wen REPL / 工具相关问题时，当前 1.5 + 2.0 全套 production-style interpreter
- 见 `formal/SSBX/Foundation/Wen/WenSurface/{NominalizerTests,RelativeClauseTests,EllipsisTests,MatchTests,UserInductiveTests,QuoteEvalTests,RewriteRulesTests,UserDefsTests,TypeInferTests}.lean` 为各 feature 之 acceptance suite
- 见 [[wen-1-5-usable-interpreter-2026-05-17]] 为前一阶段, [[wen-restructure-complete-2026-05-17]] 为 Wen 1.0 重构
