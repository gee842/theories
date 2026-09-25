---
name: wen-4gaps-closed-2026-05-18
description: Wen 2.0 残余 4 gaps 全部 elegant 收口 (PR
metadata: 
  node_type: memory
  type: project
  originSessionId: 0d926a45-025f-4d63-a524-62d072e475ae
---

后 [[wen-2.0-complete-2026-05-17]] + [[wen-1.5-usable-interpreter-2026-05-17]] 的小尾巴,验证发现的 4 个 surface/kernel gap 全部收口。

## PRs (merged into main 2026-05-18)

| # | 内容 | 文件 | 关键改动 |
|---|---|---|---|
| #81 | REPL 用 NS_NAME wiring | REPL + Namespace | composed pipeline `wenyanCompileProgramWithDefsAndNamespaces` 串联 defs + namespaces |
| #82 | 定递 HM recursion | EndToEnd + UserDefsTests | parser pre-bind NAME at `recFixTyCandidates` (默 `Hex→Hex`) — 不是 HM zonk,根因是 parser `accIsFunctional` guard 拒 `.hex` 上的 `之 X` fold |
| #83 | 类 ctor 任意 CJK 字形 | Reading + EndToEnd + UserInductiveTests | context-aware resolver: `promoteUserCtor` 把 `.noReading / schoolNamespaceName / hexCompoundStarter` 类错误升 `.varName` (当 ctor 在 active list) |
| #84 | 执 Bool quote 支持 | WenDef + WenDefEval + Elaborate + PrettyPrint + REPL + QuoteEvalTests | kernel: `Tm.unquote q : Tm` → `Tm.unquote q (t : Ty) : Tm`; typecheck 返 `t` 而非 hard-coded `.hex`; surface elaborator 在 `执 「BODY」` 时 infer BODY 类型 |

## 关键 design 决策

- **#82**: 不是改 HM 而是改 parser binding。HM zonk 已经默认未约束 mvar → `.hex`,但 parser 的 `accIsFunctional` 拦在前面 — 它在外层 `者 甲` binder 试 `.hex` 时就拒了内部 `甲 之 ARG` 的 fold。换 binder context 让 parser 看到 `.arr .hex .hex` 才放行。
- **#83**: 不让 lexer/resolveOne 直接 context-aware (会广泛侵入),而是加一层 `promoteUserCtor` wrapper — 只在 ctor list 已知后才"事后补救"。catalogue op / hex const / ambiguous / cellOpUnsupported 等 pre-existing 读法仍正常 surface 自己的 diagnostic。
- **#84**: 没 redesign `Tm.quoted` (那要改 Ty 也跟着多一个 payloadTy 字段,cascade 太广)。只给 `Tm.unquote` 加 `t : Ty` 注解,quote 本身仍 opaque。surface 在 `执 「BODY」` 处 inspect BODY 的 inferred Ty。

## 残余约束 (未来工作)

- **类 ctor 仍需单 token**: `类 颜 = 赤橙 | 紫` 这种 multi-token ctor 仍被拒,因为 `bareVarName` 要求 lex 出单 token。
- **执 〈λ〉 仍受限**: `执` 在非 Hex/Bool 结果 (Cell, arr, prod, …) 时仍走默认 `.hex` annotation — 因为 surface elaborator 只能在 `.quote body` 静态可见时 infer。函数返 Quoted 的间接路径仍默 Hex。
- **0 sorry / 0 axiom invariant 维持**.

## REPL 现可做

```
≫ 用 名家；同 一 一                          → true : Bool         (gap-2 #81)
≫ 定递 甲 为 者 乙 甲 之 推 之 乙；甲 一       → <elaborated> : Hex  (gap-1 #82, fuel 耗尽)
≫ 定递 甲 为 者 乙 错 之 乙；甲 一              → «复» (100000) : Hex (gap-1 #82, 非发散)
≫ 类 颜 = 赤 | 橙 | 紫；赤                     → 赤 : 颜              (gap-3 #83)
≫ 执 「真」                                    → true : Bool         (gap-4 #84)
≫ 执 「错 之 错 之 乾」                        → «乾» (111111) : Hex (gap-4 #84, regression)
```

[[wen-by-example]] §3-10 全部 REPL-verified。
