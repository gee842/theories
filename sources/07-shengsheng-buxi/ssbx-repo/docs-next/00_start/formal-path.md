# 形式路径

适合想从 Lean 代码确认项目状态的读者。

## 顺序

1. 读 [`../10_formal_形式/claim-status-ledger.md`](../10_formal_形式/claim-status-ledger.md)（**v0.8 · 2026-05-21**，单页人类口径），先确认每条 claim 是 closed / scoped / schema / external route / sketch / placeholder / open。
2. 读 [`../10_formal_形式/trust-boundaries.md`](../10_formal_形式/trust-boundaries.md)，确认 axiom、opaque、partial boundary。当前仓库有 3 处工程 axiom：`Foundation/Doctrine/Instance/Quantum.lean` / `Foundation/Order/FrmMonoidal.lean` / `Foundation/Atlas/Yi/Classical/Diagonal/GodelLi.lean`，约 150-170 处 sorry。
3. 读 [`../10_formal_形式/build-and-verify.md`](../10_formal_形式/build-and-verify.md)，确认构建命令与 warning 口径。
4. 按模块簇定位文件，主入口：
   - R-hierarchy：[`Foundation/Hierarchy/RHierarchy.lean`](../../formal/SSBX/Foundation/Hierarchy/RHierarchy.lean) (umbrella) 与 `R0_Taiji.lean` … `R8_GuoHex.lean`
   - Cell carriers：[`Foundation/Atlas/Yi/Cell256.lean`](../../formal/SSBX/Foundation/Atlas/Yi/Cell256.lean) 与 [`Cell256Stratify.lean`](../../formal/SSBX/Foundation/Atlas/Yi/Cell256Stratify.lean)（旧 `Foundation/Bagua/` 路径已 retired）
   - Doctrine / FullGUT：[`Foundation/Doctrine/FullGUT.lean`](../../formal/SSBX/Foundation/Doctrine/FullGUT.lean), [`T_GUT.lean`](../../formal/SSBX/Foundation/Doctrine/T_GUT.lean)
   - 5 SMCC instances：[`Foundation/Doctrine/Instance/`](../../formal/SSBX/Foundation/Doctrine/Instance/)（Algebraic / Heyting / Topological / Witt / Quantum）
   - Wen / 文：[`Foundation/Wen/`](../../formal/SSBX/Foundation/Wen/)
   - Truth：[`Truth/SelfDescription.lean`](../../formal/SSBX/Truth/SelfDescription.lean)
5. 任一 claim 的强度，回头到 ledger 那一行确认。

## 不要这样读

- 不要从旧 README 的 job 数或 theorem 数判断当前状态。
- 不要把图谱节点看成已证明 claim。
- 不要把 ledger-dependent claim 当作 Lean theorem。
- 不要把 `universal_sayability`、`scoped_gut_a_closed`、`scoped_coordinate_full_gut`、`conditional_absolute_full_gut`、`T5_general` 等 headline 名字读作比 theorem 类型本身更强的语义；以 ledger v0.8 的逐行 "What must not be claimed yet" 列为口径。
- 不要相信 `_generated/` 下的 lean-index / claim-index 自动索引（当前未生成）。

> **形式现状（路径口径，2026-05-21）**：`Foundation/Bagua/` 已被 Phase γ 删除；其内容迁至 `Foundation/Atlas/Yi/`。`YiLegacy/` 子目录不存在（旧 memo 提及的 `YiLegacy/` 是 Phase γ 中间状态，已并入 `Atlas/Yi/`）。详见 [claim-status-ledger.md](../10_formal_形式/claim-status-ledger.md) v0.8（2026-05-21）。
