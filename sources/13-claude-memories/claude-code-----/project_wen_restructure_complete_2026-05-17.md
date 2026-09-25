---
name: wen-restructure-complete-2026-05-17
description: Wen 语言栈彻底 restructure 完成 — 8 PRs merged (PR
metadata: 
  node_type: memory
  type: project
  originSessionId: 0d926a45-025f-4d63-a524-62d072e475ae
---

8 个 PRs 全 merged to main (2026-05-17):

| PR | Sub-plan | Commit | 内容 |
|---|---|---|---|
| #30 | 02 stratum doc | 3d83093 | `docs-next/10_formal_形式/wen-strata-invariants.md` — CoreForm/Tm/R8Semantics 不可折叠 distinction monism doc |
| #31 | 03 deprecate Demo | 4e310d2 | RootRuleDemoInterpreter `@[deprecated]` (Lean 4.15+ syntax `since :=`); 5 个 `set_option linter.deprecated false in` 保 native_decide 通 |
| #32 | 06 C-class research | c0e9947 | `c-class-semantics-research.md` — 12 个 C-class op 分类 (5A / 5B / 2C-still) |
| #33 | 04 wenEval lemmas | 8cf235e | `wenEval_succ` + `wenEval_halted` 加进 WenEval.lean; 0 真 sorry (research agent 误判) |
| #34 | 01 A-class upgrade | a5071ff | D_5/D_6/D_7/K_4/F_12/Z_4 → 真 Stdlib body; `relationPredicateBoolOperatorIds` 重命名 `axiomInterfaceOperatorIds`; 324 → 331 / 46 → 40 |
| #35 | 05 postfix parser | 2b08a81 | `parsePostfixApplications` 加 postfix dispatch (前于 infix); S_14 也 作 demo postfix entry |
| #36 | 07 C1 final particles | 18a0880 | **S_21..S_24 (乎/矣/哉/兮)** 4 新 OperatorId; postfix fixity + boolMarkerBody; 全 371 → **375** pins 更新 (87 .lean + 25 .md); OperatorCellMap 375 × 256 = 96,000 |
| #37 | 08 B' universal ISA | 7cb62e7 | YiInstr 加 13th instr `branchYaoYang (i target)`; **错等变 ceiling 破** (doctrine v2); WenDefCompile 加 propagate-carry adder (26 instr/each for tui/sun); ISABridge 推/損 reverse → positive; 12 cuo-symmetry theorem 改为 `complementEquivariantInstr` subset 版 |
| #38 | 01b cleanup follow-up | 8ab64f3 | 5 C-class → A-class 升级 (R_3/R_4/C_3 → pairHBody, B_8 → hexIdBody, L_4 → tongBody); coreTheoremBacked 335 → **340**; axiomInterface 40 → **35**; Task 1 (OperatorCellMap 4×256) 验证 no-op; Task 3 (feedback_yiinstr_cuo_ceiling archive) memory only |

**所有 PRs 都过 `lake build SSBX` 3858 jobs / 0 sorry / 0 axiom**.

## 现状（4-步收顶进度更新）

| 步 | 状态 |
|---|---|
| ① catalogue → desugar 表 | ✅ 100% (PR #34: 6 A-class 升级; 余 30 B-class 显式 axiom interface, 10 C-class 待 01b) |
| ② Tm 立唯一 core (CoreForm/R8Semantics 折叠为 view) | ❌ 不应折叠 — 不同 stratum (PR #30 wen-strata-invariants.md 形式化此 doctrine) |
| ③ Bagua-ISA 作 Tm 后端 | ✅ universal (PR #37 doctrine v2; v1 错等变 ceiling 已破) |
| ④ 5 evaluator 收敛到 1 | ❌ 不应收敛 — 4/5 有独立职责，1 个 (RootRuleDemoInterpreter) 已 deprecate (PR #31) |

## 关键 doctrine 变化

- **「错等变 ceiling」从 invariant 变为 v1 subset 性质**: `complementEquivariantInstr : YiInstr → Bool` 谓词显式标识哪 12 个原语满足；新 `branchYaoYang` 不满足
- **`feedback_yiinstr_cuo_ceiling.md` 已过时** — ISA 现在 universal Hex→Hex compile 可表达 (含 «生»/.tui/.jia/«损»)
- **wen-substrate/03-operation-monism.md** 加 v2 doctrine 更新

## Plan 文件夹

完整 plan: `/Users/ren/.claude/plans/wen-restructure-2026-05-17/` (README + 01-08.md, 共 8 sub-plans)

## 下一可能工作

- **01b**: C-class 5 个 A-class 候选升级 (PR #32 研究产物: R_3/R_4/C_3→pairHBody, B_8→hexIdBody, L_4→tongBody)
- **OperatorCellMap 完整化**: 375 × 256 = 96,000 entry 中, 4 个新 op 的 cell 配对可能仍需 review (PR #36 加了占位)
- **Y_20 / Z_14 / Z_15 / LIJ_9 / Z_40 等 B-class** 升级需经典学派研究, 不在 standard restructure 范围
