---
name: wen-language-state-2026-05-17
description: Wen 语言栈现状 (post-PR
metadata: 
  node_type: memory
  type: project
  originSessionId: 0d926a45-025f-4d63-a524-62d072e475ae
---

PR #26/#27/#28/#29 (2026-05-17, 全 merged) 把 Wen 语言栈 4-步收顶推进到:

| 修法 | 状态 |
|---|---|
| catalogue 改 desugar 表 | ✅ 100% (371/371, `theorem theoremBackedOperatorIds_length` + `structuralCatalogueOperatorIds_length = 0` 见证, [Semantics.lean:1142-1153](formal/SSBX/Foundation/Wen/WenSurface/Semantics.lean)) |
| Tm 立唯一 core, CoreForm/R8 折叠为 view | ❌ 未启 |
| Bagua-ISA 作 Tm 后端 | ✅ 错等变子集 (PR #27, `WenSurface/ISABridge.lean`) |
| 5 evaluator 收敛到 1 | ❌ 未启 |

**关键事实**:
- `relationPredicateBoolOperatorIds` 46 个学派关系算子经 `relationPredicateBoolSemanticsFor?` 接到 `hexRelEqBody / hexPredTrueBody` 二个 placeholder body — 是 domain caveat, 不是 desugar gap
- `coreTheoremBackedSemanticsFor?` 末行 `| id => relationPredicateBoolSemanticsFor? id` 作 fallthrough; 量化时勿只数显式 case (否则得错的 88% 数)
- Bagua-ISA 受 「错等变」约束 `f(h.complement) = (f h).complement`, 故 `推/损/生` 等非 equivariant Tm 不可桥; 是 ISA 的代数刚性, 不是工程缺口

**Why**: 用户问 "Wen 离真古文还差多远", 答 30% 词汇覆盖 × 70% 句法裂痕. 之后 4 个 PR 把架构裂缝清掉一半 (desugar / 桥), 剩两个 doctrine-级决策 (C1 句末虚词 / B' 扩 ISA) 落作 `docs-next/10_formal_形式/wen-language-roadmap.md`.

**How to apply**:
- 回 Wen 相关问题先读 wen-language-roadmap.md, 不再用旧的 "88%" / "样本停在 ISA 层" / "5 个 parallel evaluator 待收敛" 等 narrative —— 这些都已被 PR #26-29 落地或归档
- 若用户要继续推 Wen, 触发条件已写在 roadmap: C1 Path B (~250 LOC parser + 371→375 长度定理) 或 B' (改 ISA doctrine + universal compile) — 两者都需用户明确授权
- 若量化 desugar 覆盖率, 读 `theorem theoremBackedOperatorIds_length` 而非自己 awk
- 见 [[feedback_minimal_builds]]: worktree 无 .lake cache, cold mathlib 30-60min; 每 PR 末 verify ONCE 即可
