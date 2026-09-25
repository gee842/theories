# 构建与核验

> Last verified: 2026-05-21. 具体 closed / scoped / open 状态见 [claim-status-ledger.md](claim-status-ledger.md) v0.8 (2026-05-21).

本页说明形式层如何读构建结果。机器事实以最新目标构建、full build、Lean 源文件与 `../_generated/` 为准；人工文档只给出核验口径。

## 当前口径

- full build 使用 `lake build SSBX`；发布前必须通过。
- 日常维护优先构建受影响目标，例如 `lake build +SSBX.Foundation.Wen.MetaInterp.TargetContract` 或 `lake build +SSBX.Core`。不要把裸 `lake build` 当作每次小改后的默认动作。
- full build 的 job 数、warning 数、live `sorry` / `admit` / `unsafe` 计数、axiom 列表与 partial boundary 列表请直接查 `../_generated/` 与构建输出，不在本页硬编码（数字会漂移）。
- 当前已知信任边界与 axiom 文件请见 [trust-boundaries.md](trust-boundaries.md) 与 ledger。

以上统计应以 [../_generated/trust-boundary.md](../_generated/trust-boundary.md) 与最新构建输出复核，不从散文段落读取最终数量。

## 建议核验顺序

1. 运行受影响模块的目标构建，例如 `lake build +SSBX.Foundation.Wen.MetaInterp.TargetContract`，先确认局部 Lean 层能通过。
2. 若改动跨越顶层聚合、信任边界、发布入口或多个簇，再运行 `lake build SSBX` 做 full build。
3. 若出现新增 warning，先判断它是否只是 unused `simp` argument 一类维护警告。
4. 查 [../_generated/lean-index.md](../_generated/lean-index.md)，确认模块是否被索引到。
5. 查 [../_generated/trust-boundary.md](../_generated/trust-boundary.md)，确认 axiom、opaque、partial def 没有扩张。
6. 查 [../_generated/claim-index.md](../_generated/claim-index.md)，区分 machineChecked、modelComputed、ledgerDependent。

## 通过不等于全闭合

构建通过只说明当前 Lean 文件在给定依赖与信任边界下类型检查成功。它不自动说明：

- ledgerDependent claim 已由 Lean 证明。
- 经验阈值、正邪判定或 Ω 类接口已经实证闭合。
- `kleene_recursion_axiom` 已被内部化。
- `YiState.run` 的所有执行都会返回。
- ledger 中 scoped / open / external-route 行已升格为 closed。

因此文档写法应使用「构建通过，仍有警告」「在该 axiom 下」「由 ledger 记录」「由模型计算」「scoped 下闭合」等口径，避免把工程状态扩大成哲学或经验结论。具体每条 claim 的状态请查 [claim-status-ledger.md](claim-status-ledger.md) v0.8。

## 警告处理

unused `simp` argument warnings 通常表示证明脚本里有多余的 simp 参数。处理它们可以提高可维护性，但不改变 theorem 的成立状态。

若新增 warning，应先判断它是否影响：

- theorem 是否仍能通过。
- 是否暴露了不可达、未使用或误命名声明。
- 是否改变生成索引中的模块覆盖。
- 是否改变信任边界扫描。

## 文档同步

构建事实写入人工文档时，只写稳定结论和路径。模块数、声明数、claim 数、算子数、pending 数等易漂移数据，引用 `../_generated/`，不要手动复刻。
