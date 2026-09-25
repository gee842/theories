---
name: wen-1-5-usable-interpreter-2026-05-17
description: Wen 1.5 完成 — 5 PRs merged (PR
metadata: 
  node_type: memory
  type: project
  originSessionId: 0d926a45-025f-4d63-a524-62d072e475ae
---

Wen 1.5 (usable interpreter) 5 PRs 全 merged to main (2026-05-17, post-Wen-1.0 restructure):

| PR | Sub-plan | Commit | 内容 |
|---|---|---|---|
| #39 | 03 multi-statement | 2338a3a | `wenyanCompileProgram` + 「；」/「。」/`;` 分隔; +10 native_decide |
| #40 | 02 PrettyPrint | 44c5c34 | `prettyPrintTm : Tm → String`; 47 constructor cover + 18 examples |
| #42 | 04 ErrorRender | 491182e | `renderWenSurfaceErr` + caret + 40 examples; lake build SSBX 3859 jobs |
| #43 | 01 REPL | 2df6045 | `wen` CLI exe; `:help` `:quit` `:type` 命令; 1592 jobs build |
| #44 | 05 user-defs | 53cab3b | `定 NAME 为 BODY` decl; substitution-based; 18+13 examples |

## 关键 API 新增

```lean
-- multi-statement
wenyanCompileProgram : String → Except WenSurfaceErr (List TypedTm)
-- pretty printer
prettyPrintTm : Tm → String
-- error rendering
renderWenSurfaceErr : String → WenSurfaceErr → String
-- REPL exe
lake build wen   →  ./.lake/build/bin/wen
-- user defs
wenyanCompileProgramWithDefs : String → Except ProgramErrWithDefs (List Stmt)
-- syntax: 定 NAME 为 BODY  (CJK keyword 定, only chunk-leading)
```

## 设计 highlights

- **user-defs**: 纯 program-level pre-processor with textual substitution; 不改 SurfaceExpr/parser/elaborator (smallest blast radius). 递归/redef/catalogue-conflict 均 reject.
- **REPL**: `partial def main` (loop body), 0 sorry/axiom 维护; CJK hexagram lookup via 既有 `OperatorAnchors.hexagramOperatorAnchors`
- **PrettyPrint**: 不 round-trip guaranteed (parser cue resolve 可能选 alternate glyph); human-readable
- **ErrorRender**: codepoint-indexed col model (Lex 之 startCol); 5 个 err type 都覆盖 caret 渲染
- **multi-statement**: 仅顶层 separator (no bracket-aware splitting)

## 现状

Wen 现在是 **user-usable interpreter**:
- 可作 `wen` CLI 一行 prompt 试 `推 之 一`
- 可写多句程序 with `定` 宣告 + 复用
- 错误信息有 caret 指位
- 程序可 pretty-print 回 文言 prose

**Why**: 用户问「从一个解释器的角度来说还缺什么」, 列了 5 件「冰山上」工具; "开始吧" 触发. Phase 1 (4 parallel sub-plans 在 isolation worktree) + Phase 2 (1 sub-plan after Phase 1 merged) 完成.

**How to apply**:
- 回 Wen REPL / 工具相关问题时, 当前可作 production-style interpreter 介绍
- `定 NAME 为 BODY` 语法是 v1, 后续可加 `recursion / namespace / type-class` 等
- pretty-printer 不保 round-trip — 若用户问可改进
- ErrorRender 之 elab error 缺 span info (anchor at col 0), 后续可补
- 见 [[wen-restructure-complete-2026-05-17]] 为 Wen 1.0 之 8-PR 大重构 (上一阶段)

## Plan 文件夹

完整 plan: `/Users/ren/.claude/plans/wen-1.5-usable-interpreter/` (README + 01-05.md)
