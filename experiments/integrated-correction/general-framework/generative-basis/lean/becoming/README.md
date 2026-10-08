# Becoming：生成之论的形式核心 / The formal core of the Theory of Becoming

一个关系展开，只陈述一次。本目录是 Lean 包 `Becoming`。理论叙述见[正典章节 §9](../../../../../../theories/becoming/chapters/THE-THEORY-OF-BECOMING.md#9-形式脊柱--the-formal-spine)，方向与阶段见[统一计划](../../../../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-UNIFICATION-PLAN.md)。

One relational unfolding, stated once. This directory is the Lean package `Becoming`. The canonical chapter gives the account; the unification plan gives the direction and phases.

## 三环 / Three rings

| 环 / Ring | 内容 / Contents | 约束 / Constraint |
|---|---|---|
| 核心 / Core | 基础 `GenerativeCore`、`InquirySufficiency`、`RelationalRenewal`，加包内四层 | 只导入自身；每条声明公理报告为空；只用 Lean 内置前导即可编译 |
| 桥接 / Bridge | [`Becoming.Bridge`](Becoming/Bridge.lean) | 导入既有模块，证明它们的接口就是核心的概念；公理报告为空；核心不导入它 |
| 外围 / Periphery | 既有伦理与动力学模块、Mathlib 叶子及其桥接 [`CorrectionInquiry`](../universal-ethics/generative-capacity/CorrectionInquiry.lean)、Python 实验 | 可用任何合适的工具；依存方向指向核心 |

Core purity is [Ren's requirement](../../../../../../sources/15-codex-theory-conversations/2026-10-09-pure-core.md). The checker enforces all three conditions on every run.

## 四层 / Four layers

`import Becoming` 导入全部四层。 / `import Becoming` brings in all four.

| 层 | 模块 / Module | 讲什么 / What it states |
|---|---|---|
| L0 | `GenerativeCore`（基础 / foundation） | 过程、轨迹及其组合与传递 / processes, traces, composition and transport |
| L1 | [`Becoming.Frame`](Becoming/Frame.lean) | 框架：过程加上每个配置实现的主张；运行、可达、不变量、新实现 / a frame is a process with realized claims; runs, reach, invariants, novel realization |
| L2 | [`Becoming.Inquiry`](Becoming/Inquiry.lean) | 探究的所见范围由实际执行给出，可靠策略在其上确保目标；判断即一步探究 / an inquiry's visible scope is what its actual executions reach, where a sound policy secures its goal; a judgment is a one-step inquiry |
| L3 | [`Becoming.Renewal`](Becoming/Renewal.lean) | 经条件读出的运行是一个关系展开；更新与消耗属于运行 / a run read through conditions is one relational unfolding; renewal and consumption belong to the run |
| L3 | [`Becoming.Dependence`](Becoming/Dependence.lean) | 依存随步形成、维持、断裂与消解；损失有终止、转化、恢复三条去路，损失本身不决定去路；逐步读法 / dependence forms, holds, breaks and dissolves across steps; a loss is ended, transformed or restored, and the loss does not decide which; a stepwise reading |
| L4 | [`Becoming.Metaethics`](Becoming/Metaethics.lean) | 普遍元伦理核心：前提卡、G0 刻画、极小性、普遍理由、C 与 L；整段与逐步的关系读法 / the Universal Metaethical Core: premise card, G0's characterization, minimality, the universal reason, C and L; the relational reading over a whole run and stepwise |

每层只导入它下面的层（L3 的 `Becoming.Dependence` 导入 `Becoming.Renewal`）。L1–L3 不含伦理谓词；L4 的每项规范前提都是具名定义或假设，不藏在类型或定义里。

Each layer imports only those below it (within L3, `Becoming.Dependence` imports `Becoming.Renewal`). L1–L3 contain no ethical predicate; every normative premise in L4 is a named definition or hypothesis.

## 检查 / Verification

```bash
python3 -B experiments/integrated-correction/general-framework/generative-basis/lean/becoming/check_becoming.py
```

[`check_becoming.py`](check_becoming.py) 解析导入闭包，核对每个继承模块的当前字节与其已通过回执一致，按依赖顺序用 Lean 4.29.1 编译，逐条审计公理，并核对核心的三项纯净条件。结果写入 [`becoming-verification.json`](becoming-verification.json)，每次运行的原始输出保留在 `becoming-checks/`。

The checker resolves the import closure, requires inherited modules to match passed receipts, compiles in dependency order with Lean 4.29.1, audits every declaration's axioms and checks the core's three purity conditions. The receipt records the result; each run's raw output is kept in `becoming-checks/`.

## 扩展 / Extending

- 新的形式结果陈述在这里。核心表达不了时扩展核心，不另建模型。 / State new formal results here; extend the core rather than build another model.
- 既有模块保持原范围，经 `Becoming.Bridge` 中的实例或等价定理连到核心。 / Existing modules keep their scope and connect through instance or equivalence theorems in `Becoming.Bridge`.
- 需要 Mathlib 或其他库的结果放在外围，导入核心；核心永不导入它们。`CorrectionInquiry` 是这样的例子：它用 Lean 4.30.0-rc2 与 Mathlib 检查（[`check_correction_inquiry.py`](../universal-ethics/generative-capacity/check_correction_inquiry.py)），核心在那里同样编译通过。 / Results needing Mathlib or other libraries live in the periphery and import the core, never the reverse. `CorrectionInquiry` is one, checked with Lean 4.30.0-rc2 and Mathlib; the core compiles there too.

## 名称 / Names

模块按所述之事命名。声明名都在命名空间 `Becoming` 下，改名前后不变，因此记录中的别名仍然有效。

Modules are named for what they state. Declaration names, all in namespace `Becoming`, did not change, so record aliases remain valid.

| 旧模块 / Former module | 现模块 / Module | 改名理由 / Why |
|---|---|---|
| `BecomingFrame` | `Becoming.Frame` | 包结构 / package structure |
| `BecomingModal` | `Becoming.Inquiry` | 它讲探究的所见范围，不是模态逻辑 / it states the scope of inquiry, not modal logic |
| `BecomingRenewal` | `Becoming.Renewal` | 包结构 / package structure |
| `MetaethicalCore` | `Becoming.Metaethics` | 核心是整个包，不只是这一层 / the core is the whole package, not this layer alone |
| `BecomingInstances` | `Becoming.Bridge` | 它是核心与外围之间的桥 / it bridges core and periphery |

基础模块保留历史命名空间 `Generative`。它的过程是任何生成／变化，包括维持与退化，不只是生成性的变化。

The foundation keeps its historical namespace `Generative`. Its processes are any becoming, including maintenance and degeneration, not only generative change.
