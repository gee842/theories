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
| L3 | [`Becoming.Dependence`](Becoming/Dependence.lean) | 依存随步形成、维持、断裂与消解；活动需要当下支持时损失之后的结局（不穷尽、不互斥）；事件与关系的逐步读法 / dependence forms, holds, breaks and dissolves across steps; the outcomes of a loss where activity needs current support, neither exhaustive nor exclusive; stepwise readings of events and their relations |
| L3 | [`Becoming.Return`](Becoming/Return.lean) | 按回程时间给更新分级；消耗恰是不再回程的依存；周期层面的读法 / renewal graded by the time to return; consumption is exactly a dependence that never returns; readings over cycles |
| L3 | [`Becoming.Horizon`](Becoming/Horizon.lean) | 任何有限的一段运行都不决定其汲取在整段意义上是更新还是消耗，有无反馈都如此；按数量的读法逐步可判定 / no finite stretch of a run decides whether its drawing renews or consumes in the whole-run sense, with or without feedback; a reading of amounts is decided step by step |
| L3 | [`Becoming.Joint`](Becoming/Joint.lean) | 相对于所取动作的差别制造属于形成之间的共同活动；在一个形成的各事件之间，整段的结局由尾部决定，单步检验挑出断裂之步 / difference-making, relative to the move taken, belongs to the joint activity among formations; over a formation's events the run-level outcome is fixed by the tail, while the step-level test singles out the breaking event |
| L3 | [`Becoming.Substitution`](Becoming/Substitution.lean) | 支持门控定律中，能替代条件的消耗者持续，在整段读法下仍是消耗的，逐步读法在维持者失去支持之前记入它，此后到它转向为止扣下它 / in the support-gated law, a consumer that substitutes a condition persists and still consumes on the whole-run reading, while the stepwise reading credits it before the sustaining formation loses support and withholds it until it switches |
| L3 | [`Becoming.Generation`](Becoming/Generation.lean) | 形成生起；生起消耗一个有限条件家族时，不息的生成需要其更新复现；更新不蕴含生成；在不被更新的条件之间替代推迟终结；耗散使生成停止，封闭循环则不必 / formations arise; where arising depletes a finite family of conditions, unceasing generation needs their renewal to recur; renewal does not imply generation; substitution among unrenewed conditions defers the end; dissipation ends generation, while a closed cycle need not |
| L3 | [`Becoming.Flow`](Becoming/Flow.lean) | 条件作为形成取用与给予的数量；任意晚的步上有取用，就需要任意晚的步上有补充，取用的形成不息地生起与恒定的取用者都是其情形；不止地更多的生成需要没有界的补充，每个形成给予有限时需要没有界的更新者；不息的生成尚不是更多 / conditions as amounts that formations take and give; uptake at arbitrarily late steps needs replenishment at arbitrarily late steps, whether the takers arise without end or stay the same; generation more without end needs replenishment without bound and, with bounded capacity, renewers without bound; unceasing generation is not yet more |
| L3 | [`Becoming.Population`](Becoming/Population.lean) | 每步活跃的形成有多少；在活跃形成的普查之下、流中每个形成只列一次、只有活跃的形成取用时，不止地更多蕴含不息的生成，反之不然；每个前提都起作用 / how many formations are active; under a census of the active formations, with each formation listed once in the flow and only active formations taking, more without end implies unceasing generation, and not conversely; each premise does work |
| L3 | [`Becoming.Identity`](Becoming/Identity.lean) | 跨步的同一：标签不承载任何东西，名字跨步的模式承载同一；每一步的关系、每个条件的类与取用者的数目不依赖同一，形成的类、依存的任期、侵蚀与生起依赖它；单向的连续排除制造生起与去掉侵蚀，接续仍开放，双向的连续恰保持生起与侵蚀，跨过休眠的接续仍改变形成的类；在普查之下，更多在每种一对一的同一读法下蕴含不息，在每种没有分裂的延续下迫使生起，萌出的读法则不迫使 / identity across steps: labels carry nothing, while the pattern of names across steps carries identity; each step's relations, each condition's class and the number of takers do not depend on identity, while a formation's class, the tenure of a dependence, undermining and arising do; continuity read one way rules out making arising and removing undermining and leaves succession open, read both ways it preserves arising and undermining exactly, and joining across dormancy still changes a formation's class; under a census, more without end implies unceasing generation under every one-to-one reading of identity and forces arising under every continuation without splits, but not under budding |
| L3 | [`Becoming.Dissipation`](Becoming/Dissipation.lean) | 耗散：给予总使补充者所取的条件付出多于所给时，从某步起封闭的家族耗尽，取用不再复现；所以复现的取用、不止地更多与取用者的不息生起，需要与每个有限条件家族之外交换 / dissipation: when giving always costs the conditions the renewer takes from more than it gives, a family closed from some step runs down and taking from it stops; so recurring taking, more without end and the unceasing arising of takers need exchange beyond every finite family of conditions |
| L3 | [`Becoming.Roles`](Becoming/Roles.lean) | 形成与条件是一个关系项的两种角色，两类的读法就是没有形成作为条件的读法；一个关系项恰在活跃时作为条件时，依存于它的形成只在它活跃时活跃，它的终结终结每个依存链到达它的形成，它只经由另一个活跃形成的给予而生起；它的生起就是补充，所以在耗散之下，在有限家族中复现的生成需要与家族之外交换，有限个关系项就是全部时它不再复现 / formations and conditions are roles of one relatum, and the two-kind reading is the one in which no formation is a condition; where a relatum stands as a condition exactly while it is active, a formation depending on it is active only while it is, its ending ends every formation whose chain of dependence reaches it, and it arises only as another active formation gives to it; its arising is replenishment, so under dissipation generation recurring in a finite family needs exchange beyond it, and with finitely many relata in all it does not recur |
| L4 | [`Becoming.Metaethics`](Becoming/Metaethics.lean) | 普遍元伦理核心：前提卡、G0 刻画、极小性、普遍理由、C 与 L；整段、逐步与关系层面的关系读法 / the Universal Metaethical Core: premise card, G0's characterization, minimality, the universal reason, C and L; the relational readings over a whole run, stepwise and through relations |
| L4 | [`Becoming.Ranking`](Becoming/Ranking.lean) | C 在各读法下的排序：整段与逐步读法都把共享排在以消耗取胜之上，在二元定律族中把节制排在过度汲取之上；对在损失之前有被记入事件的过度汲取者，只有整段读法把它的不在场排在其在场之上 / what C ranks under each reading: both the whole-run and the stepwise reading rank sharing above winning by consumption and, in the two-part family, restraint above overdraw; for an overdrawing formation with a credited event before the loss, only the whole-run reading ranks its absence above its occurrence |
| L4 | [`Becoming.Correspondence`](Becoming/Correspondence.lean) | 哪些条件构成关系：在“一方汲取、另一方以正水平依存”这一对应纪律下，惰性条件不连通任何东西，经由一个条件的连通由它的活的使用造成；以一类关系项读时连通不变，承担自身的形成直接相关，无需第三个条件 / which conditions relate: under the discipline that a condition relates two events only when one draws on it and the other depends on it at a positive level, idle conditions connect nothing, and connection through a condition is made by its living use; read with one kind of relatum the connection is kept, and formations bearing on themselves relate directly, with no third condition |

每层只导入它下面的层（L3 内：`Becoming.Dependence` 导入 `Becoming.Renewal`；`Return`、`Substitution` 导入 `Dependence`；`Horizon`、`Joint`、`Generation` 导入 `Return`；`Flow` 导入 `Generation`；`Population` 导入 `Flow`；`Identity` 导入 `Population`；`Dissipation` 导入 `Population` 与 `Horizon`；`Roles` 导入 `Dissipation`。L4 内：`Becoming.Ranking` 与 `Becoming.Correspondence` 导入 `Becoming.Metaethics`，`Correspondence` 另导入 `Roles`）。L1–L3 不含伦理谓词；L4 的每项规范前提都是具名定义或假设，不藏在类型或定义里。

Each layer imports only those below it (within L3, `Becoming.Dependence` imports `Becoming.Renewal`; `Return` and `Substitution` import `Dependence`; `Horizon`, `Joint` and `Generation` import `Return`; `Flow` imports `Generation`; `Population` imports `Flow`; `Identity` imports `Population`; `Dissipation` imports `Population` and `Horizon`; `Roles` imports `Dissipation`; within L4, `Becoming.Ranking` and `Becoming.Correspondence` import `Becoming.Metaethics`, and `Correspondence` also imports `Roles`). L1–L3 contain no ethical predicate; every normative premise in L4 is a named definition or hypothesis.

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

模块按所述之事命名。声明名都在命名空间 `Becoming` 下，模块改名时不变，因此记录中的别名仍然有效。

Modules are named for what they state. Declaration names, all in namespace `Becoming`, did not change when the modules were renamed, so record aliases remained valid.

| 旧模块 / Former module | 现模块 / Module | 改名理由 / Why |
|---|---|---|
| `BecomingFrame` | `Becoming.Frame` | 包结构 / package structure |
| `BecomingModal` | `Becoming.Inquiry` | 它讲探究的所见范围，不是模态逻辑 / it states the scope of inquiry, not modal logic |
| `BecomingRenewal` | `Becoming.Renewal` | 包结构 / package structure |
| `MetaethicalCore` | `Becoming.Metaethics` | 核心是整个包，不只是这一层 / the core is the whole package, not this layer alone |
| `BecomingInstances` | `Becoming.Bridge` | 它是核心与外围之间的桥 / it bridges core and periphery |

基础模块保留历史命名空间 `Generative`。它的过程是任何生成／变化，包括维持与退化，不只是生成性的变化。

The foundation keeps its historical namespace `Generative`. Its processes are any becoming, including maintenance and degeneration, not only generative change.

### 声明改名 / Declaration renames

P11b 依第四次独立审查（H1、H6、H13）和 Ren 对基础用语的纠正（“付费记录”太市场；“recipient, money, pay” 不是最好的选词）改了下列声明名，相关记录的别名同时更新。 / P11b renamed these declarations after the fourth independent review (H1, H6, H13) and Ren's corrections of foundational vocabulary; the affected records' aliases were updated with them.

| 旧名 / Former | 现名 / Now | 理由 / Why |
|---|---|---|
| `Web.MetSince` | `Web.MetAbove` | 改为最小形式：低于曾被满足的所需，也低于现在的所需 / the minimum form: below a need that was met and below the present need |
| `Web.Paid`, `paid_finitely` | `Web.Depletes`, `depletes_finitely` | 讲条件的消耗，不讲支付 / depletion of conditions, not payment |
| `conserved_ceases` | `dissipation_ceases` | 关键前提是耗散；对任意不上升的量陈述 / the premise that matters is dissipation; stated for any quantity that never rises |
| `Flow.load`, `Flow.supply` | `Flow.uptake`, `Flow.replenishment` | 取用与补充 / uptake and replenishment |
| `Flow.ledger`, `Flow.accumulates` | `Flow.Balances.over`, `Flow.Balances.accumulates` | 平衡，不是账目 / a balance, not a ledger |
| `takers_le_load`, `supply_le`, `More.supply_unbounded` | `takers_le_uptake`, `replenishment_le`, `More.replenishment_unbounded` | 同上 / as above |
