# 统一白皮书的形式证明索引

适用：[统一白皮书 v1.1](../WHITEPAPER-v1.1.md)。v1.0 与 v1.1 的主要章号保持一致，以各版附录 A.4 的逐项索引为准。

三个 Lean 文件及既有成功检查日志保持原字节。旧 [README](README.md)、`OpenFuture.lean` 与 `ExistenceConditions.lean` 的头注记录其写作时对应的 v0.x 版本，旧节号并非统一版节号。

| 内容 | 统一版位置 | 模块 |
| --- | --- | --- |
| 最大保持区域与路径安全 | §5.1—§5.3 | GenerativeCore |
| 约束收紧与确定性循环 | §5.4 | GenerativeCore |
| 公共要求及索引对应 | §8.1 | GenerativeCore |
| 严格改进关系 | §8.2 | GenerativeCore |
| 有限惩罚反例的自然数核心 | §5.9 | GenerativeCore |
| 指定竞赛矩阵 | §9.1 | GenerativeCore |
| 相同观察的判断障碍 | §3.5、§5.6 | OpenFuture |
| 局部收益与保护冲突 | §4.11 | OpenFuture |
| 零和分数不必关闭共同未来 | §9.4 | OpenFuture |
| 累积亏损与控制观察障碍 | §2.4—§2.5 | ExistenceConditions |
| 独立组合与抽象实现 | §2.12 | ExistenceConditions |

原验证工具链为 `leanprover/lean4:v4.29.1`，只导入 Std。共 28 个命名定理包含定义后果、结构结果和反例；代码无 `sorry` 与新增用户公理，部分证明依赖标准逻辑基础。准确依赖见三个日志。

v1.1 以 SHA256 核对未改变的代码与成功日志，未重新运行 Lean。P1、P2、P4 是定义性推论；P3 和其他概率、动力学推导为纸面结果。§1.6 的再生产模型是新增条件示例，不在这 28 项机器检查内。代码不承担规范前提或现实模型的验证。
