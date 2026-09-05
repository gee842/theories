# 形式化核心：检查了什么

对应白皮书第五、六、九、十一节。实现文件：[GenerativeCore.lean](GenerativeCore.lean)。完整检查记录：[verification.txt](verification.txt)。

本模块使用 **Lean 4.29.1**，仅导入 `Std`，没有使用 Mathlib，没有新增公理，也没有用 `sorry` 跳过证明。二十项定理均已编译，并逐项输出 `#print axioms`。部分结果使用 Lean 的标准命题外延、商类型和经典选择基础，具体依赖见检查记录；不存在 `sorryAx`。

## 对象与量词

```text
T x a y              x 执行 a 后，y 是模型内允许的后继
Preserves T K x a    a 至少有一个后继，而且所有后继都在 K 中
Invariant T S K     K 内每个状态满足 S，并有保持 K 的可执行行动
Viable T S x        x 属于某个这样的保持集合
AllProtected P x    对每个相关索引 i，P i x 都成立
Dominates p q       所有已选维度 p ≥ q，至少一个维度 p > q
```

安全谓词 S、受影响者索引、保护要求 P 和评价维度都是显式输入。机器检查没有自动确定这些输入的伦理内容，也没有判断输入与现实是否吻合。

T 使用非确定关系容纳模型内的扰动。`∀ y` 只覆盖 T 所承认的可能性。遗漏真实风险的 T，完全可能让形式上成立的结果无法用于现实。

## 二十项结果

| Lean 名称 | 含义 | 正文对应 |
| --- | --- | --- |
| `viable_safe` | 可延续状态满足当前保护条件 | F1、F5 |
| `viable_invariant` | 所有保持集合的并仍为保持集合 | F1 正向 |
| `invariant_subset_viable` | 任一保持集合包含于可延续集合 | V 的最大性 |
| `viable_predecessor` | 当前安全且能把后继全留在 V，则当前在 V | F1 反向 |
| `viable_iff_safe_step` | 当前在 V 当且仅当安全且有保持 V 的行动 | F1 |
| `outside_no_guaranteed_return` | 安全但在 V 外时，每个可执行行动都有后继在 V 外 | F3 |
| `invariant_run_safe` | 给定的实际路径一直采取保持行动，则全程安全 | F2 |
| `tighten_shrinks_viability` | 收紧保护条件不会扩大可延续集合 | §5.4 |
| `public_viability_protects_each` | 公共保护集合内每个索引均满足对应要求 | F5 |
| `constraint_reindexing` | 按满射重编号不改变所有要求的合取 | F5 |
| `finite_penalty_can_be_outbid` | 任意自然数惩罚都可被更大的自然数收益超过 | F4 的算术核心 |
| `racing_strictly_dominates` | 给定两方矩阵中竞赛严格占优 | A1 反例 |
| `obedient_racing_worse_for_both` | 双方竞赛差于双方克制 | A1 反例 |
| `good_viable` | 三状态模型中的 good 是可延续状态 | §5.3 反例 |
| `gamble_not_viable` | gamble 无法保证避开 dead | §5.3 反例 |
| `outside_can_reach_inside` | 在稳健集合外仍可能幸运地回到内部 | §5.3 反例 |
| `deterministic_cycle_viable` | 确定两状态循环可以满足保持条件 | §6.1 反例 |
| `dominates_irrefl` | 严格改进不可自反 | §11.2 |
| `dominates_trans` | 严格改进可传递 | §11.2 |
| `dominates_asymm` | 不可能互相严格改进 | §11.2 |

其中一些结果是定义的直接后果，另一些是结构证明或有限反例。数量不是理论深度的度量；列出二十项是为了使检查范围准确可追踪。

## 复现

安装所指定的 Lean 工具链并使 `lean` 和 Python 3 可用后，在此目录运行：

```bash
python3 verify.py
```

脚本会编译源码、核对工具链版本、检查每项定理均输出基础依赖，记录源码 SHA256，并重写 `verification.txt`。也可以只运行：

```bash
lean GenerativeCore.lean
```

`lean-toolchain` 固定为 `leanprover/lean4:v4.29.1`。本次核验使用本机已经安装的该版本。

## 没有由本模块证明的事项

- R1—R4 为什么应被接受，以及 N1—N4 的哲学论证。
- 哪些人或其他存在者具有什么具体保护要求。
- 生存、福利、自由与纠错之间所有可能冲突的解法。
- 信息价值、概率风险、资源微分／差分模型、特征值与反馈延迟的纸面推导。
- 现实是否满足任何一个给定模型，以及社会是否存在总体化。
- 无限时域与有限期限模型之间的所有对应关系。
- 一个可计算、可部署的完整 AI 安全算法。

特别地，`constraint_reindexing` 并没有从逻辑中产生平等伦理；`deterministic_cycle_viable` 也没有证明循环系统有意识或是善的。它们只确认正文明确指出的结构区别。
