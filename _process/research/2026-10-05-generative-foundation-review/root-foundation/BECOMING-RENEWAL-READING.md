# 运行上的更新／消耗与生生的关系读法 / Renewal on runs and the relational reading

2026-10-09，Asia/Bangkok。AI（Claude）按 Ren 的指示“你自己全改了吧……先更新好计划，然后再一步步完整完成，保持代码和整体结构优雅”（[原话与解释](../../../../sources/15-codex-theory-conversations/2026-10-09-one-theory-unification.md)）完成[统一计划](BECOMING-UNIFICATION-PLAN.md)的 P3b。成果记录：[becoming-renewal-reading](../../../../theories/becoming/results/records/becoming-renewal-reading.md)。

## 1. 问题

Universal Metaethical Core 的前提卡里有三项对应：形成 E、连通、`living` 的读法。在 P2 中，`living` 和 `related` 是 `Valuation` 的外给参数，连通是假设。P3b 要回答的是：Becoming 层能否从展开本身给出这两项，从而让连通成为可以检查的动力学性质，而不是一条前提？

这里的“形成”和“条件”是同一展开中的分析角色：一个形成依存于某些条件，或从某些条件中汲取，或两者兼有。它们不是彼此独立的实体，也不是价值的所有者。在 Lean 中，它们是贯穿运行的固定索引类型，形成跨步的同一性由 `F` 规定；`draws` 只记录一个形成汲取某个条件，不记录汲取多少，水平的变化由过程给出。这两项省略在 §7 的审查后写明。

## 2. 结果

全部声明都在脊柱上，公理报告为空（[回执](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/becoming-verification.json)）。

**L3，[Becoming.Renewal](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Renewal.lean)：只讲动力学，不含伦理谓词。**

| 声明 | 内容 |
|---|---|
| `Conditions`、`Conditions.along` | 条件水平、活跃的形成、依存与汲取都是配置上的可观测量。经这些可观测量读出的运行，就是一个 `RelationalRenewal.Unfolding`，该模块的全部定理都适用于它 |
| `falls_finitely` | 一个从某步起不再上升的自然数可观测量，只能下降有限次 |
| `Run.not_of_depletion`、`no_execution_of_depletion` | 每步都降低储备，则没有运行。这正是 `Depletion` 的陈述，由上面的原则导出 |
| `Run.renewal_recurs` | 凡非更新之步都降低秩，则任何尾段都不会没有更新。这是 `ContinuationRenewal` 自然数秩形式的否定式 |
| `Conditions.drawdown_finite` | 沿运行的无更新汲取：活跃次数有限 |
| `Commons.class_belongs_to_the_run` | 同一过程、同一初始配置，两次运行中焦点形成每一步都活跃；一次在更新之内，另一次消耗维持者的条件，维持者随之终止 |

**L4 读法，[Becoming.Metaethics](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Metaethics.lean) 的“The relational reading”一节。**

| 声明 | 内容 |
|---|---|
| `Conditions.valuation` | 形成事件 `(形成, 步)` 的读法有两条：活跃且在该运行中不消耗者为 living；两个事件的形成共同参与某一条件，即为 related |
| `living_iff_relational`（在外围桥接 `Becoming.Bridge` 中） | 这一 `living` 就是已记录的[关系读法](../../../../theories/becoming/results/records/relational-reading-comparison.md) |
| `connected_of_common`、`significant_iff_of_common` | 如果每个活的形成都参与同一个条件，整体就是连通的；于是 G0 恰等于种子加 N_rel 加 N_std。连通由共同参与给出，但依赖什么算条件、什么算参与：没有这条对应纪律，加入一个人人在水平 0 依存的条件即可免费连通，而过粗的共同条件又使 living 变空（更正，见 §7） |
| `consumption_relates` | 消耗者与失去支持的形成共同参与被汲取的条件，因而它们的事件相关（更正，见 §7） |
| `valuing_consumption_reaches` | 在 N_rel 下，一个立场若珍视某个消耗者的活动，就必须珍视失去支持的形成的每个活的事件。传递沿共同参与进行，不用到消耗本身（更正，见 §7） |
| `Separate.not_connected` | 两个形成各自只参与自己的条件：两者都活着，也都不消耗，但没有关系把它们连起来 |

**分类。** [实例分类表](BECOMING-INSTANCE-CLASSIFICATION.md)中原本留给 P3b 的 `ContinuationRenewal` 与 `OpenFutureRevision`，现在归入“运行上的更新界”。

## 3. 与计划的对照

| 计划 P3b 的要求 | 结果 |
|---|---|
| 由 Run 可观测量构造 `RelationalRenewal` 的展开 | `Conditions.along` |
| `RenewalComparison` 的关系读法成为脊柱上 `living` 的读法 | `Conditions.valuation`、`living_iff_relational`，这是可用的读法。说它是生生的正确读法，仍是对应，不是 Lean 结果 |
| `Depletion`、`ContinuationRenewal` 的储备界作为同一分类的实例 | 两者的自然数形式都是 `falls_finitely` 的情形，`RelationalRenewal` 的汲取界也是。`ContinuationRenewal` 的良基形式更一般，不由此导出 |
| `related` 有动力学来源，连通可检查（`metaethical-core-characterization` 的下一步） | `related` 取为共同参与某一条件；有共同条件时连通成立，没有时可以不成立 |

## 4. 作者反审

**反驳 1：统一只是重新包装。** “可观测量不能无穷下降”是标准事实；把三条界写成它的情形，只是组织工作，不是新数学。

*回应。* 同意。数学上的新内容在第 2 节的后半：分类属于运行，消耗者与失去支持者共同参与同一条件，连通可由共同条件给出。统一的价值是让三条界落在同一个对象（运行）上，此后陈述不必再各建一个序列模型。

**反驳 2：`related` 太粗。** 任何两个从同一生物圈汲取的形成都“相关”，于是连通几乎自动成立，伦理内容全落到 N_rel 上。

*回应。* 粗细是读法的选择。这里如实公开，并没有证明它。

- `valuing_consumption_reaches` 用到的关系，只是“一方汲取、另一方依存于同一条件”，比共同参与更窄，在更细的读法下同样成立。
- 共同条件确实让连通变得容易，但这正是要公开的位置：拒绝 G0 的一方，现在必须拒绝 N_rel 或 N_std，即在边界内适用传递或共享，而不能声称两者无关。
- 生物圈、气候之类的条件是否真被所有活的形成共同参与，是经验对应，不在本结果之内。
- （审查后补充，§7）上面第二点不完整：争议同样落在“什么算条件、什么算参与”上。拒绝 G0 的一方可以接受 N_rel，同时否认对一个惰性或过粗条件的共同参与是 N_rel 所说的已形成关系。而且粗的共同条件正是其上依存会失败的条件，它使连通容易，也使 living 变空。

**反驳 3：消耗者自己的事件不算活的，这似乎预先判了它。** 关系读法把消耗者的事件排除在 living 之外，`valuing_consumption_reaches` 的前提（某立场珍视消耗者的活动）因而只能来自 S0 以外。

*回应（审查后更正，§7）。* 排除消耗者的事件是读法的阐释性规定，写在 `living` 的定义里，不是结论。要分开两件事：
- 有 Ren 原话支持的：用关系结构把更新与消耗分开，且生成与退化“不overlap”（[原话](../../../../sources/15-codex-theory-conversations/2026-10-09-renewing-consuming-without-axioms.md)）。
- AI 的阐释选择：以整个形成、整段运行为分类单位；消耗型形成的每个事件都不算 living；把“持续”读成在无穷运行中从不使依存者永久失去支持。

在这一规定下，S0 只要求珍视自己活的、进一步生成的内容；一个在关系读法下消耗的形成，其活动不在其中。如果某个立场仍珍视这一活动（例如赢者珍视赢），N_rel 就把意义传到失去支持者。这一读法与 C 连用时给出排序判决（[relational-reading-comparison](../../../../theories/becoming/results/records/relational-reading-comparison.md)），不只是沉默。

- 读法是整段运行上的分类，不是逐步的，继承自 `RenewalComparison`：消耗者在超出更新之前的事件，也不计为生成根据。
- 更细的逐步读法尚未确定。

**反驳 4：`class_belongs_to_the_run` 的模型太弱。** 公地过程没有反馈：更新不依赖条件水平。赢者运行里的损失之所以持续，只是因为汲取一直超出更新；若汲取停止，条件会恢复。

*回应。* 属实。该定理的用途只是说明，分类不是配置或焦点形成自身轨迹的函数。不可逆的损失需要更新依赖于被更新条件的反馈，这由 `RelationalRenewal` 的定律族给出，即 `no_return_below_support`，本结果不重复它。

**反驳 5：依存与汲取是静态的。** `requires`、`need`、`draws` 不随配置变化，而真实的依存会形成、转化和消失。

*回应。* 属实，这是从 `RelationalRenewal` 继承的限制。要放宽，需要让 `requires` 读取配置，并重做 `Renewed` 与 `Consumed` 的定义。这是下一步的形式工作，也正是 Theory of Becoming 要求解释“维持、转化、退化与消失”的地方。

**未解决。**
1. 关系读法是生生的正确读法，这是哲学论证，不是 Lean 结果。
2. 依存的动态化。（P6 完成，见 §6。）
3. 逐步读法。（P6 完成，见 §6。）
4. 共同条件的经验对应。
5. 独立反审：已由另一 agent 进行，见 [审查](BECOMING-RENEWAL-READING-REVIEW.md) 与 §7。

## 5. 边界

- 不证明 S0、N、A、C、L 或 J，不约束拒绝它们的立场，不推出义务、排序、认识或遵循。
- 可观测量与实际历史的对应，是每次应用的义务。

## 6. 动态依存与逐步读法（P6）

2026-10-09。Ren 在改名完成后指示：“and after it is elegantly completed, move on to pursue the theory of becoming, and prove the necessary proofs”（[原话](../../../../sources/15-codex-theory-conversations/2026-10-09-pure-core.md#rens-follow-up-finish-the-renames-then-continue-the-theory)）。本节完成第 4 节“未解决”的第 2、3 项，也就是[正典章节](../../../../theories/becoming/chapters/THE-THEORY-OF-BECOMING.md#8-开放纲领--open-programme) §8 的“动态依存”与“逐步读法”两行。成果记录：[becoming-dependence-dynamics](../../../../theories/becoming/results/records/becoming-dependence-dynamics.md)、[becoming-stepwise-reading](../../../../theories/becoming/results/records/becoming-stepwise-reading.md)。

```text
Result(s): 复用 becoming-renewal-reading、relational-renewal-classification、metaethical-core-characterization；
           新增 becoming-dependence-dynamics（L3）、becoming-stepwise-reading（L3 与 L4）
Delta: 依存、所需水平与汲取成为配置的可观测量；跨步读出维持、断裂、形成、消解与丧失；
       损失之后的终止、转化与恢复由定理互相约束，并在同一过程中都实际发生；逐步读法及其评价
Supplied premises / correspondence: 可观测量与实际历史的对应；living 取哪一种读法仍是公开的对应选择；
       G0 的前提（种子、N_rel、N_std）不由此证明
Evidence: Becoming.Dependence 29 项定理；Becoming.Metaethics 新增 6 项定理；合并检查器回执
       20261008T233313.422223Z，核心公理报告全空，仅用前导编译；外围桥接 20261008T233335.261411Z 通过
Boundary: 不建立整体演绎；不涉及差别制造归属、周期更新；独立反审未做
Integration: becoming-renewal-reading 的 next_delta 的前两项由新记录承接；
       relational-renewal-classification 的 Unfolding 由 static 精确复原
```

独立审查之后，本节的若干说法已更正；更正处标明，理由与全部更正见 §7。

### 6.1 依存属于展开

[Becoming.Dependence](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Dependence.lean)（L3）：只讲动力学，不含伦理谓词。

| 声明 | 内容 |
|---|---|
| `Dependence`、`Web`、`Dependence.along` | 条件水平、活跃、依存（及所需水平）与汲取都随配置变化。运行经这些可观测量读出为一个 `Web` |
| `Kept`、`Broken`、`Forms`、`Dissolves`、`Lost` | 跨一步读出。依存在该步起点和终点都被满足，为维持；起点满足而终点不满足，为断裂；依存出现，为形成；依存消失，为消解；断裂后再也不被满足，为丧失 |
| `static_supported` 等六条、`conditions_along` | 依存不变时，恰好复原 `RelationalRenewal` 的静态读法：支持、更新、消耗与形成的分类都一致 |
| `ceases_at_a_step`、`arises_at_a_step`、`dissolves_between`、`forms_between` | 变化发生在步上：某步成立、后来不成立的依存，在其间某一步消解；反过来，在其间某一步形成。陈述不用排中律：没有一段运行能避开这样的一步 |
| `kept_or_broken`、`kept_not_broken` | 每个被满足的依存，跨每一步恰为维持或断裂之一 |
| `renewed_not_consumed`、`renewing_not_consuming`、`renewing_keeps_support`、`lost_consumed` | 更新与消耗仍然互斥；更新使更新型形成每一步都有支持；丧失是消耗的一种 |

**一步之内的先后。** 一步之内依存改变与条件下降谁先谁后，单看一步无法区分。读法把下降算在该步起点的依存上，模块说明写明了这一点；更细的时间粒度要求细化运行，属于应用义务。

### 6.2 损失之后的三种结局

以下三条一般定理都以 `Dependent` 为前提：形成只在它当时所依存的条件支持它时活跃。这排除了缓冲、储备与滞后；前两条的内容就是这一前提的逆否（更正，见 §7）。

| 声明 | 内容 |
|---|---|
| `continuing_restores` | 在 `Dependent` 下，以不弱于先前的依存活跃，就意味着水平满足先前的所需 |
| `consumed_continues_transformed` | 在 `Dependent` 下，无回程的损失之后仍然活跃的形成，必已减弱或消解其依存 |
| `consumed_ends_when_fixed` | 在 `Dependent` 下，依存不变时，无回程的损失之后该形成不再活跃 |
| `Crossing.loss_does_not_decide` | 同一过程、同一配置，三次运行都在第一步断裂同一个依存（按步首约定读）。第一次：形成终止，损失无回程。第二次：旧依存消解，对另一条件的依存形成，形成始终活跃，损失无回程。第三次：形成蛰伏，条件得到更新，同一依存此后一直被维持。断裂的读法不决定后继配置；在这一见证中，去路由构成断裂的那一步动作 `fall m` 选定。按步末约定，只有恢复运行有断裂，终止运行中的依存也消解 |

**解读（审查后收窄，§7）。** 三种结局既不穷尽，也不互斥：恢复是关于条件的事实，终止与转化是关于形成的事实；同一断裂之后，一个形成可以转化、另一个终止，而条件随后恢复。一段历史是“转化”还是“终止加新形成”，由 `F` 规定的形成同一性决定。准确的说法是：在一个形成被给定、各字段除 `Dependent` 外彼此独立的表示中，几种变化方式可以由共同的可观测量定义，并由定理相互约束；终止与转化之分依赖所规定的形成同一性，形成本身的个体化没有被表示。

这与[正典章节 §1](../../../../theories/becoming/chapters/THE-THEORY-OF-BECOMING.md#1-生成同一展开--becoming-one-unfolding)“形成、维持、转化、退化与消解都是沿运行的关系变化，不是五个阶段”相容，但它是表示内的定义与约束，不是这一主张的证明。它也不完成[根基 §9](../../../../theories/becoming/chapters/BECOMING-FOUNDATION.md#9-the-content-of-the-whole-deduction)的整体演绎：共同纳入一个记录类型，加一条约束，正是那里说的不能代替根据的东西（[整体演绎的审查](GROUNDING-INFERENCE-AND-PRESENTATION.md#19-the-whole-deduction-and-the-passage-from-inclusion-to-relation)）。

### 6.3 逐步读法

L3，同一模块：

| 声明 | 内容 |
|---|---|
| `RenewingAt`、`renewing_at_active`、`not_renewing_at_of_broken` | 一个事件（形成，步）在更新之内，当它活跃，且该步维持它所参与的每个条件上的每个依存。整段运行的更新使每个活跃步都在更新之内；某步若断裂了它所参与条件上的依存，该事件就不在更新之内 |
| `Commons.stepwise_credits_before_escalation` | 先在更新之内汲取，后来超出：整段读法记为消耗；逐步读法记入第一步，不记第二步 |
| `Commons.dip_breaks_without_consuming` | 先超出一次，再停下等条件更新：整段读法不记为消耗；逐步读法不记入断裂的那一步 |
| `Dip.renewing_at_each_step_not_in_run` | 维持者在它自己的每个活跃步都在更新之内，整段却不更新：它不活跃时，另一个形成断裂了共同条件。整段更新不是自身各步的合取。维持者不汲取任何条件，两种 living 读法都记入它的活跃事件，所以这不是 living 读法的分歧（更正，见 §7） |

L4，[Becoming.Metaethics](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Metaethics.lean) 的“The stepwise reading”一节：

| 声明 | 内容 |
|---|---|
| `Web.valuation` | 逐步读法：两个事件的形成在各自的步上共同参与某一条件，即为 related。P6 原取“事件在更新之内”为 living；审查后改为“活跃且不侵蚀”，见 §7 |
| `Web.connected_of_common`、`Web.significant_iff_of_common` | 每个活的事件都参与的条件使整体连通，于是 G0 恰等于种子加 N_rel 加 N_std，与整段读法相同 |
| `Web.breaking_relates`、`Web.valuing_breaking_reaches` | 在断裂之步汲取的事件不是活的，并且与被断裂形成参与该条件的每个事件相关；断裂可以由别的形成参与造成。在 N_rel 下，珍视这一事件的立场，必珍视那些活的事件（措辞更正，见 §7） |
| `Conditions.stepwise_related`、`Commons.readings_differ` | 依存不变时，两种读法的 `related` 相同，只在 `living` 上不同；两个方向都有分歧 |

### 6.4 作者反审

**反驳 1：三种结局只是定义上的分情况。**

*回应。* 部分同意。`kept_or_broken` 与 `continuing_restores` 证明很短。内容在别处：
- 这些关系在依存可变的模型中成立，而静态模型表达不了转化；
- `loss_does_not_decide` 是存在性结果：三种结局在同一过程、同一配置下都可实现，所以断裂的读法不决定后继配置。（审查后更正，§7：原文说“去路由后续关系决定”，不对；在 `Crossing` 中，去路由构成断裂的那一步动作选定。）

**反驳 2：逐步读法偷偷带进了因果归属。** 维持者的事件被记入更新，即使维持条件的是别人。

*回应。* 逐步读法读的是事件所处的关系，不是它的因果贡献。整段读法也是如此：它追踪的是一个形成与某个条件最终命运的共同参与（审查 Q11）。差别制造的归属在 §8.3 处理。

**反驳 3：两种读法冲突，哪一个是生生？**

*回应。* 两者回答不同的问题。整段读法问：形成在整段运行中是否消耗。逐步读法问：一个事件所在的那一步是否维持其条件上的依存；审查后的 living 问：事件是否在之后某个曾被满足的依存不被满足的那一步汲取（§7）。`Commons.readings_differ` 证明两个方向都有分歧，所以不能把一个当作另一个的细化。但这样两者都不能单独是“生生的读法”（审查 2.7）；比较与判据见 §8.5。

**反驳 4：转化把所需水平降低也算进去，太宽。**

*回应。* 是的，依存减弱也算转化。应用若要区分减弱与替代，可以用 `Dissolves`／`Forms` 细分；`Crossing` 的转化运行是替代。

**反驳 5：逐步读法太严。** 条件因季节等原因自然下降时，下降那一步上的任何事件都不被记入。

*回应。* 属实，这是读法的严格性。审查后的读法只扣下在那一步汲取该条件的事件，不汲取的形成不受影响（§7）；但在依存恢复之前，任何汲取都被扣下。周期层面的读法见 §8.1。

**反驳 6：`Crossing` 是为结论构造的玩具。**

*回应。* 它的作用是可能性见证：在可以表达依存变化的最小过程里，同一步的断裂之后三种结局都可实现。它不说明实际系统中哪种结局常见；那是经验问题。

### 6.5 边界

- 不证明任何读法是生生的正确读法，也不证明 S0、N、A、C、L 或 J。
- 依存可观测量与实际历史的对应，是每次应用的义务。
- 差别制造归属、周期层面的更新与条件替代，见 §8。
- 整体演绎仍开放（见 6.2 的解读）。
- 独立反审：见 §7。

## 7. 独立审查与更正

2026-10-09。另一 agent（Claude Opus 5.5，未参与撰写）对 §§1–6、`Becoming.Dependence`、`Becoming.Metaethics` 的读法部分、正典章节与六条记录作了独立审查：[BECOMING-RENEWAL-READING-REVIEW](BECOMING-RENEWAL-READING-REVIEW.md)。它重新编译了核心，核对了 22 个源文件的哈希，并写了 13 组探针（Q1–Q13，全部无公理）。

| 问题 | 审查结论 |
|---|---|
| A. 关系读法的哲学根据 | 未确立，研究的表述过强 |
| B. `Becoming.Dependence` | 数学接受；三处散文须撤回；“形式实例”须收窄 |
| C. 形式复核 | 接受 |
| D. 对应与超出 | 20 项更正 |

### 7.1 形式上的更正

全部在核心上，公理报告为空（回执见 §8 的记录）。

| 更正 | 声明 | 理由 |
|---|---|---|
| 逐步读法的 living 改为“活跃且不侵蚀” | `Web.UnderminingOn`、`Web.UnderminingAt`、`Web.valuation` | 事件侵蚀：它在某步汲取某条件，该步之后，一个依存不被满足，而它在不间断成立期间曾以不小于现在的所需被满足（定义经 P7b、P9b 修正，§11、§12）。只看事件所汲取的条件，这是“不消耗”的逐步对应，两种读法因而同型。见下面三个候选的比较 |
| 断裂与侵蚀 | `Web.BreakingOn`、`Web.BreakingAt`、`BreakingOn.undermining` | 断裂：在某步汲取，该步断裂一个依存（起点满足、终点不满足）。断裂是侵蚀的一种 |
| `RenewingAt` 保留为逐步的更新分类 | `RenewingAt.not_undermining`、`RenewingAt.not_breaking`、`Commons.broken_formation` | 它是 `RenewingIn` 的逐步对应。在更新之内的事件既不侵蚀也不断裂；被断裂者在断裂之步不在更新之内，但也不侵蚀。Q1 作为 `RenewingAt` 的性质保留 |
| 损失之后的汲取 | `Commons.pausing`、`Commons.drawing_after_loss` | 损失之后继续汲取不再断裂任何依存，却使条件回不来：同样的第一步之后若不再取（动作为 0），条件回到。这样的事件侵蚀而不断裂。“回不来”只在公地见证中成立，那里更新在支持之下照常、失去者可以恢复；侵蚀读的是共同参与一个未恢复的短缺，不是对不回程的贡献（`Pinned.undermining_without_effect`，§11） |
| 两个方向的分歧保持，且两种读法都记入被断裂者 | `Commons.readings_differ`（扩展） | 加码运行第 0 步：逐步记入、整段不记入；短暂下降第 0 步：整段记入、逐步不记入；加码运行中维持者在断裂之步的事件：两种读法都记入 |
| 继承的“消耗”不要求依存曾被满足 | `Unmet.consumed_without_loss`；`Web.Consumed` 的说明 | Q2：一个从未被满足的依存使条件被消耗、汲取者成为消耗型，而没有任何断裂或丧失；汲取者在任何一步都不侵蚀。`RelationalRenewal` 是基础模块，其字节不改，在 [relational-renewal-classification](../../../../theories/becoming/results/records/relational-renewal-classification.md) 中披露。整段 living 读法仍用继承的 `ConsumingIn`，所以 Q2 对整段读法仍成立 |
| 关系层读法 | `Web.relations`、`Web.living_iff_relations`、`Mixed.one_event_two_relations` | 审查 2.2 指出的最直接的对手。主张取为一个形成在某步对某条件的关系；事件的逐步读法恰是它所参与关系的读法的合取；同一事件可以有一个活的关系和一个侵蚀的关系 |
| 模块说明与声明说明 | `Becoming.Dependence`、`Becoming.Metaethics` | 见 7.2 的第 2、4、6、10–16、18 项 |

**三个逐步候选。** 逐步 living 先后有三个候选，每一个都保留在核心中：前两个连同使它不被采用的见证，第三个连同它的代价：

| 候选 | 问的是 | 不采用的理由或代价 |
|---|---|---|
| 在更新之内（P6，`RenewingAt`） | 该步维持它所参与的每个条件上的每个依存 | 被断裂者在断裂之步不被记入（审查 Q1，`Commons.broken_formation`）；从未被满足的依存使所有参与者都不 living（审查 Q2） |
| 不断裂（审查 Q12） | 它不在断裂某个依存的那一步汲取 | 损失之后的汲取不再断裂任何东西，于是被记入，虽然在公地见证中它使条件回不来（`Commons.drawing_after_loss`）。这与 Ren 采纳的问题（以消耗取胜不是生生）不合 |
| 不侵蚀（工作候选，待 Ren 选择） | 它不在这样一步汲取：之后一个依存不被满足，而它在不间断成立期间曾以不小于现在的所需被满足 | 保留两个方向的分歧；记入被断裂者；在依存成立期间从未被满足的依存不使汲取者侵蚀，所需下降或增长时也如此（定义经 P7b、P9b 修正，`NewNeed.never_met_not_undermining`、`FallingNeed.never_met_not_undermining`、`RisingNeed.grown_need_not_met`）；扣下断裂之步与损失之后的汲取。代价：`draws` 不带数量，侵蚀也不涉及汲取的效果，所以在一个曾被满足而尚未恢复的依存之下，任何汲取都被扣下，哪怕恰取更新量（`Pool.within_share_undermines`），甚至不改变任何水平（`Pinned.undermining_without_effect`）；依存中断一步即开始新的一段，此前的满足不再计入（`Gap.lapse_starts_afresh`，§12），休眠或迁出是否表示为持续的依存，是应用义务 |

### 7.2 二十项更正的处理

| 项 | 内容 | 处理 |
|---|---|---|
| 1 | §4 反驳 3：排除消耗者是规定 | 已改；分开 Ren 原话支持的部分与 AI 的选择；写明与 C 连用给出排序 |
| 2 | “消耗本身是一种已形成的关系” | 改为共同参与，N_rel 沿共同参与传递：研究 §2、§4、英文摘要；章节 §4、§6.3；记录 becoming-renewal-reading；`consumption_relates`、`valuing_consumption_reaches` 与模块说明 |
| 3 | 连通“由展开给出” | 改为“在关于条件与参与的对应纪律下由共同条件给出”，并写明 Q4、Q10：章节前提卡与 §6.3；两条 `significant_iff_of_common` 的说明；记录 |
| 4 | `Becoming.Metaethics` 模块说明第 9–12 行 | 已改：`related` 与 `living` 是 Valuation 的输入；Becoming 层给出的读法更窄 |
| 5 | 前提卡 living 一行只列整段读法 | 已改：列出整段、逐步与关系层三种读法，选择开放 |
| 6 | 读法依赖运行 | 已写明：章节 §6.3–6.4、模块说明、metaethical-core-characterization 的记录；不依赖运行的构造列为下一步 |
| 7 | 读法里没有“继续生成” | 已写明：模块说明、章节前提卡与 §6.3、§8.5。生成的成分本身未加入，列为开放 |
| 8 | 对手读法的比较 | 见 §8.5：关系层、整体方向、周期层、差别制造、能力、自创生／代谢、热力学，以及有限可判定性；其中周期层、差别制造、关系层与有限可判定性有形式结果 |
| 9 | 披露 Q1、Q2，权衡 Q12 | 采用 Q12 的方向（只看所汲取的条件），再以“不侵蚀”为工作候选，理由见 7.1；Q1、Q2 与 Q12 的缺口都作为定理保留；记录的反例已加 |
| 10 | `Consumed` 的说明 | `Web.Consumed` 的说明已改；`Unmet.consumed_without_loss` 记下这一缺口；`RelationalRenewal` 在其记录中披露 |
| 11 | “三条去路” | 改为“定理联系起来的三种结局，既不穷尽也不互斥”：模块说明、记录标题与主张、章节 §1、研究 §6.2 与英文摘要 |
| 12 | 写出 `Dependent` | 已写出，并说明两条定理是其逆否 |
| 13 | “去路由后续关系决定” | 已删；改为“断裂的读法不决定后继配置，去路由构成断裂的那一步选定”：研究 §6.4、记录 |
| 14 | “同一个断裂”依赖步首约定 | 已写明：`loss_does_not_decide` 的说明、章节 §1、研究 §6.2、记录 |
| 15 | `Dip` 不是 living 的分歧 | 已移出：模块说明、记录、章节 §2、研究 §6.3。Q1 原是 living 上的真实分歧；改读法后不再是，作为 `RenewingAt` 的性质保留 |
| 16 | “断裂事件” | 改为“在断裂之步汲取的事件”，并注明断裂可由别者参与造成；改读法后，被断裂者在该步的事件在所达之列 |
| 17 | “形式实例”须收窄 | 已收窄：研究 §6.2、记录 becoming-dependence-dynamics、章节 §8 |
| 18 | 固定索引类型；`draws` 不带数量 | 已写明：研究 §1、模块说明、记录的 `correspondence` |
| 19 | `living_iff_relational` 的位置 | 已注明在 `Becoming.Bridge` |
| 20 | “已完成” | 章节 §8 与记录改为“已定义并比较，读法选择开放”，独立反审指向审查文件 |

### 7.3 仍开放

审查列出会改变其判断的四种结果：

1. **条件的对应纪律。** 一条排除惰性或虚设条件的规则，并证明在声明的类中连通仍成立。部分完成：§10 给出一条纪律并证明这一点；Q10 与人人以正水平依存、被使用一次的条件仍未解决（§12）。
2. **比较关系层读法与限于汲取的逐步读法，并论证哪一种是生生的读法。** 两者都已在核心上定义并比较（7.1）。论证见 §8.5，结论是选择须由 Ren 作出。
3. **不依赖运行的读法，并与 `universal_reason` 接通。** 开放。
4. **在 living 中加入继续生成的成分。** 开放。现有读法读出的是“不损”，即与他者依存相容的活动，不是生生的全部。

## 8. 回程、视界、共同活动与替代（P7）

2026-10-09。按同一指示继续（“prove the necessary proofs”）。本节承接三处的下一步：

- [relational-renewal-classification](../../../../theories/becoming/results/records/relational-renewal-classification.md)：周期层面的更新、条件之间的替代、共同消耗中的差别制造归属；
- [becoming-dependence-dynamics](../../../../theories/becoming/results/records/becoming-dependence-dynamics.md)：在既有形成机制中实现依存的替代，并检验分类是否保持；
- 审查 §2.6–2.7：对手读法的比较，以及读法的判据。

成果记录：[becoming-return-grades](../../../../theories/becoming/results/records/becoming-return-grades.md)、[becoming-finite-horizon](../../../../theories/becoming/results/records/becoming-finite-horizon.md)、[joint-difference-making](../../../../theories/becoming/results/records/joint-difference-making.md)、[substitution-preserves-consumption](../../../../theories/becoming/results/records/substitution-preserves-consumption.md)。

```text
Result(s): 复用 becoming-dependence-dynamics、becoming-stepwise-reading、relational-renewal-classification；
           新增 becoming-return-grades、becoming-finite-horizon、joint-difference-making、
           substitution-preserves-consumption（均为 L3）
Delta: 更新与消耗之间按回程时间分级，消耗恰是不再回程的依存；周期层面的读法；
       任何有限的一段运行都不决定其汲取是更新还是消耗；
       but-for 差别制造在多重决定下与关系参与分离，在形成之间；在一个形成的各事件之间，整段的结局由尾部决定；
       在既有的支持门控定律中，能替代条件的消耗者以转化依存的方式持续，在整段读法下仍是消耗的
Supplied premises / correspondence: 扣除一方的部分而其余不变，是建模义务；
       回程等级、视界与实际历史的对应，是经验问题
Evidence: Becoming.Return、Becoming.Horizon、Becoming.Joint、Becoming.Substitution；合并检查器回执（见记录）
Boundary: 不推出责任、义务或排序；读法的选择不由此决定
Integration: 支持门控定律的 overdraw_crosses_support、permanently_below、dependent_overdraw_ends_itself 直接复用；
       Commons 过程与 Becoming.Renewal 的 sharing、winning 直接复用
```

### 8.1 回程：按回到的时间给更新分级

[Becoming.Return](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Return.lean)（L3）：

| 声明 | 内容 |
|---|---|
| `ReturnsWithin`、`RenewedWithin`、`Returns` | 某步成立的依存在其后 `p` 步之内被满足，为在 `p` 步内回程；条件上每个依存都如此，为在 `p` 步周期内更新；每个依存都在某个以后的步被满足，为回程 |
| `renewed_within_one`、`RenewedWithin.mono`、`RenewedWithin.returns`、`Returns.not_consumed` | 等级有序：更新蕴含一步内更新；`p` 步内更新蕴含任何更长周期内更新，也蕴含回程；回程的条件不被消耗 |
| `consumed_iff` | 消耗恰是某个依存不再回程 |
| `seasonal_renewed_within_two` | `RelationalRenewal` 中既不更新也不消耗的季节性条件，在两步周期内更新，不在一步内更新 |
| `Slowing.slowing_recovery` | 恢复可以无界地变慢：间隔越来越长地被满足的条件，总会回程，从不被消耗，但没有任何周期长度能界定它的回程 |
| `RenewingInWithin`、`UnderminingFor` | 周期层面的两种读法：形成在 `p` 步周期内更新（它参与的每个条件都在 `p` 步内更新）；事件侵蚀 `p` 步（它在某步汲取某条件，一个在其成立期间曾被满足的依存此后 `p` 步都不被满足；定义经 P7b 修正） |
| `RenewingIn.within_one`、`undermining_for_one`、`RenewingInWithin.mono`、`UnderminingFor.anti`、`RenewingInWithin.not_consuming`、`RenewingInWithin.not_undermining_for` | 周期读法扩展逐步读法：更新蕴含一步周期内更新，侵蚀即侵蚀一步；周期越长记入越多；在任何周期内更新的形成不消耗，它的事件也不侵蚀该周期 |
| `LateMet.within_one_not_renewing` | 逆命题不成立：一个依存在其第 0 步不被满足、此后每步都被满足，形成在一步周期内更新，却不整段更新。`RenewedWithin` 不问依存在其自身之步是否被满足，`Renewed` 问（P7b） |
| `renewedWithin_zero`、`undermining_for_zero` | 周期长度 0 是退化的：零步内更新恰是无人依存；任何在曾被满足的依存之下的汲取都侵蚀零步，在更新的运行中也是。周期取 `p ≥ 1`（P7b） |
| `Commons.dip_within_two`、`Dip.renewing_within_two` | 两步周期下，短暂下降被记入：形成在两步周期内更新，事件不侵蚀两步，虽然它在断裂之步汲取；维持者在两步周期内更新，虽然它不在每步更新 |
| `Commons.escalation_undermines_for_every_cycle` | 加码之后条件不再回来：加码事件对每个周期都侵蚀（`p = 0` 是退化情形），此前的事件不侵蚀一步 |

**解读。** “更新与消耗互斥但不穷尽”留下的中间区域，现在按回程时间分级：每步都维持、在有界周期内回到、终会回到但无界、以及不再回到（消耗）。`consumed_iff` 说明这一阶梯在消耗一端是精确的：不被消耗的条件，恰是没有哪个依存永不回程的条件。顶端则是严格的：更新严格强于一步周期内更新（`LateMet`），因为周期读法不问依存在其自身之步是否被满足；这在阶梯顶端重现了审查 Q2 所见的、关于从未被满足的依存的不对称。`Slowing` 对应生态学中所谓“临界变慢”：系统接近转折点时，受扰后的恢复越来越慢（作者据先前知识，本次未新读文献）。这里只给出形式上的区分：回程无界变慢的条件仍不是被消耗的条件；它是否预示损失，是经验问题。

### 8.2 有限的历史不决定分类

[Becoming.Horizon](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Horizon.lean)（L3）：

| 声明 | 内容 |
|---|---|
| `Run.cons`、`Run.AgreeUpTo` | 在一次运行之前加一步；两次运行在 `h` 之前的配置与动作都相同 |
| `Commons.prefix_does_not_decide` | 对每个视界 `h`，同一过程的两次运行在 `h` 之前完全相同：每一步都超出更新地汲取，焦点形成的每个事件都在更新之内。此后一次在更新之内汲取，焦点形成是更新的；另一次继续超出，焦点形成是消耗的 |
| `Commons.finite_reading_credits_consumption` | 任何由前 `h` 步决定、并记入每次更新运行的读法，必记入某次消耗运行 |
| `Commons.whole_run_credits_overdraw` | 整段读法记入超出更新的汲取：对每个视界，那次更新运行在 `h` 之前每步都汲取两个单位，整段读法记入焦点形成的每个这样的事件（P7b） |
| `Commons.amount_reading` | 按数量的读法逃出视界结果：“该步所取不超过更新”由前 `t + 1` 步决定，记入共享运行的每个事件，扣下两次运行在 `h` 之前的每个事件；它只是不记入每次整段更新的运行。依存网上 `draws` 不带数量，这一读法在 `Web` 上不能表达（P7b） |
| `Commons.cycle_reading_not_finite` | 形成层面的周期读法（`RenewingInWithin p`，`p > 0`）不由任何有限前缀决定；由有限历史决定的只是事件层面的 `UnderminingFor p`（到 `t + p` 为止）（P7b） |
| `Feedback.prefix_does_not_decide` | 支持门控定律有反馈：越过支持阈值之后损失不回来。对每个视界，同一起点、`h` 之前每步都汲取两个单位：在 `h` 停止则更新，继续则消耗。停止的一次从不到达阈值，所以反馈不改变视界结果（P7b） |

**解读。** `class_belongs_to_the_run` 说分类不是初始配置的函数；这里更强：分类不是任何有限前缀的函数，有反馈时也如此（`Feedback.prefix_does_not_decide`）。事件层面的逐步与周期读法由有限的历史决定（`UnderminingAt` 要用到该步之后为止的全部过去，`UnderminingFor p` 到 `t + p` 为止），所以在条件还满足依存时，它们记入渐进的耗竭；形成层面的周期读法则不由有限前缀决定（`cycle_reading_not_finite`）。

这一结果的力量来自它的假设：读法须记入每次整段更新的运行。而那次更新运行在 `h` 之前每步都超出更新地汲取，整段读法记入这些事件（`whole_run_credits_overdraw`）。若把对 Ren 采纳的问题的判决读作关于“超出更新地汲取”这一活动，整段读法同样不满足它；若读作关于运行的最终结局，判断就需要对继续的说明。一个按数量的读法可由有限历史判定，并扣下每一次超出（`amount_reading`），它只是不记入每次整段更新的运行。所以下面 §8.5 的约束 1 相对于对判决的一种读法、以及不带数量的可观测量；它不是有限探究本身的界限。

在这些见证里，给定动作，动力学是确定的；有限前缀不决定的是此后的动作。所以“对继续的探究”部分地就是对将要做什么的审议。一个条件式读法（“继续这一步的汲取会消耗”）在这些见证中可由状态与定律判定；这一点只作论证，未形式化。这把评价与探究连在一起：L2 的所见范围由实际执行给出，而这里所需的正是对继续的探究与审议。

### 8.3 共同活动中的差别制造

[Becoming.Joint](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Joint.lean)（L3）：

| 声明 | 内容 |
|---|---|
| `Dependence.Keeps`、`Dependence.Breaks`、`along_kept`、`along_broken`、`keeps_not_breaks` | 配置之间的维持与断裂；沿运行恰是 `Becoming.Dependence` 的维持与断裂；两者互斥 |
| `BreaksBy`、`MakesDifference`、`Overdetermined`、`Overdetermined.no_difference` | but-for 检验，动作固定（P7b 修正）：由某配置以某动作的一步断裂依存，而扣除某一方的部分后以同一动作的每一步都维持它，则这一方的部分造成了差别。扣除任何单独一方的部分、以同一动作仍有断裂之步，为多重决定；此时没有哪一方单独造成差别 |
| `Shock.move_decides` | 动作属于“其余”：由同一配置，唯一汲取者的部分在平静的动作下造成差别；在外来冲击下损失被多重决定，它的部分不造成差别。所以检验须固定实际所取的动作（P7b） |
| `Pool.difference_belongs_to_the_joint` | 同一过程、同一水平、第一个汲取者取同样的量。另有一方汲取时，它的部分造成差别；另有两方汲取时，损失被多重决定，它的部分不造成差别，而扣除两方的部分则维持依存，差别由共同活动造成。两次运行中，关系读法都把它计为消耗；一个什么也不取的形成不计为消耗 |
| `Commons.overdraw_consumes` | 从某步起每步都汲取至少两个单位（每步更新一个），条件被消耗 |
| `Pool.within_share_undermines` | 逐步读法不追踪差别制造：第一个汲取者恰取更新量，第二个取两个；第二个的部分造成差别，第一个的不造成，但第一个在断裂之步的事件侵蚀（P7b） |
| `Commons.depletion_is_joint` | 一个形成的各事件之间：每步超出更新的汲取消耗条件；第一个事件那一步维持依存，对任何正长度的周期都不侵蚀；扣除任何一个事件的汲取，条件仍被消耗，在整段层面没有哪个事件单独造成差别 |
| `Commons.no_finite_segment_makes_difference`、`Commons.breaking_event_makes_step_difference` | 整段层面的结局由尾部决定：扣除任何一步之前的全部汲取，条件仍被消耗，没有哪个有限的事件集合造成整段的差别。步层面的检验挑出断裂事件：在断裂之步，由同一配置不汲取则依存被维持（P7b） |

**扣除留在展开之内。** 比较的对象是同一过程中的另一个配置或运行，即那一方或那一事件的部分不在的配置或运行。没有在过程之外另设一个比较世界。动作也属于其余的活动：检验固定实际所取的动作（`Shock`）。

**解读。** 差别制造不属于一方自身的活动，而属于它与其他部分以及所取动作的共同关系；正如分类属于运行，结局不由断裂的读法决定。多重决定的情形正是“我的一份无关紧要”这一推理的形式。在一个形成的各事件之间，须分开两种检验。整段层面：消耗由运行的尾部决定，没有哪个有限的事件集合造成差别（`no_finite_segment_makes_difference`），这与视界结果是同一事实。步层面：断裂事件造成那一次断裂的差别（`breaking_event_makes_step_difference`），逐步读法扣下它及其后的事件。所以“每一步的汲取单独都不造成差别”只对整段层面的检验成立。本仓库已有的散文论证说过“but-for 不可缺少性太强”（[整体过程实现审查](WHOLE-PROCESS-REALIZATION-REVIEW.md#three-inadequate-tests-and-the-stronger-identification)）与“冗余路线可以在去掉一条之后保持结果”（[展开保持审查](UNFOLDING-PRESERVATION-REVIEW.md#3-strong-rivals-and-the-distinctions-they-test)）；这里是这一点在依存网上的形式见证。关于集体伤害与过度决定的哲学讨论（如 Parfit 的“道德数学的错误”、Kagan 关于“我造成差别吗”的讨论）是重要对照，本次未新读，只作指引。

### 8.4 替代：消耗者以转化依存的方式持续

[Becoming.Substitution](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Substitution.lean)（L3）把替代放进既有的[支持门控定律](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/RelationalRenewal.lean)：共同条件由依存于它的维持者更新；汲取超出更新，更新本身随之终止，损失在定律内不会回来。

| 声明 | 内容 |
|---|---|
| `ceasing_step` | 对可判定的规定，停止成立的那一步可以找到（`ceases_at_a_step` 的可判定形式） |
| `Substitution.web`、`web_dependent` | 焦点形成在共同条件支持它时依存于它，否则依存于一个支持它的替代条件；共同条件的水平仍由原定律给出 |
| `Substitution.persists_consuming` | 从一开始就超出更新地汲取：能替代的焦点形成每步都活跃；它对共同条件的依存在一个可以找到的步上消解，对替代条件的依存同时形成；它在运行中是消耗的；维持者永久失去支持并终止 |
| `Substitution.extracting_persists_consuming` | 一个具体定律满足全部前提，上述结论不是空的 |
| `Substitution.extracting_low`、`Substitution.stepwise_credits_substitution` | 在这一具体定律中，共同条件从第 3 步起为 0；逐步读法记入焦点形成除第 2 步之外的每个事件：越过之前它的汲取使每个所需仍被满足，越过之后它在模型中不汲取任何条件（P7b） |
| `Substitution.slow`、`Substitution.slow_withheld_two_steps` | 在另一定律中，共同条件跌破维持者的支持之后仍支持焦点形成一步，它在第 2、3 步都被扣下（P9b，§12） |

**解读。** 在整段读法下，替代保持分类：一个以转化依存的方式熬过它参与造成的损失的形成，仍然是消耗的；它自身的持续不证明更新。这一保持几乎由定义给出：`ConsumingIn` 只要求曾在某步汲取一个被消耗的条件，此后做什么都不能改变它。在逐步读法下分类不保持：焦点形成在维持者失去支持之前被记入，此后到它转向替代条件为止被扣下，在这一具体定律中只有第 2 步（`stepwise_credits_substitution`），在 `slow` 中是第 2、3 步（§12）。“替代不证明更新”仍然成立，因为逐步的 living 不是更新。连同既有结果，这一定律族在无回程的损失之后实现了终止（`dependent_overdraw_ends_itself`）与转化（本结果）；恢复要求更新者重新得到支持，在这一定律内不发生，由[有支持的修复路线](../../../../theories/becoming/results/records/supported-renewal-recovery.md)在另一定律中给出。这也是“赢的元吸引子”的一个结构：靠消耗取胜的一方可以转向别处而持续，失去者不随之恢复；在逐步读法下，这样的胜者在失去者失去支持之前被记入，此后到它转向别处为止被扣下。

### 8.5 读法的比较

审查 §2.7 建议了五条判据。以下逐一对照本研究中已定义的读法。“是”“否”只在所述的范围内成立，括号内是依据。

| 判据 | 整段（不消耗） | 逐步（不侵蚀） | 周期 `p`（不侵蚀 `p` 步） | 关系层 | but-for 差别制造 |
|---|---|---|---|---|---|
| (a) 符合 Ren 采纳的问题（恶性增殖、以消耗取胜不是生生）与 Ren 所述的生成与退化不重叠；越过阈值之前的事件怎样判，是 AI 的延伸 | 部分：扣下消耗者的全部事件（relational-reading-comparison），但也记入一次更新运行中超出更新的汲取（`whole_run_credits_overdraw`）。判决若指最终结局，是；若指超出更新的汲取，否 | 部分：扣下断裂之步与损失之后的汲取（`broken_formation`、`drawing_after_loss`）；渐进耗竭在越过阈值之前被记入（`prefix_does_not_decide`）；替代的消耗者在维持者失去支持之前被记入，此后到转向为止被扣下（`stepwise_credits_substitution`、`slow_withheld_two_steps`） | 同逐步（`depletion_is_joint`） | 同逐步 | 否：多重决定下没有哪一方单独造成差别（`Pool`）；整段层面没有哪个有限的事件集合造成差别（`no_finite_segment_makes_difference`） |
| (b) 不因一个条件的命运判定未改变它的被断裂者或旁观者 | 否：较晚的断裂者使较早、在更新之内的汲取者不 living（审查 Q11） | 部分：被断裂者被记入（`readings_differ`、`broken_formation`）；但恰取更新量的汲取者在别者造成的断裂之步被扣下（`Pool.within_share_undermines`），不改变任何水平的汲取者在先前的损失之后被扣下（`Pinned.undermining_without_effect`） | 部分，同逐步 | 部分，同逐步；同一事件的不同关系分开（`Mixed`） | 是 |
| (c) 可由有限探究判定 | 否（`finite_reading_credits_consumption`） | 事件层面是：由到该步之后为止的历史决定 | 事件层面是：由到其后 `p` 步为止的历史决定；形成层面否（`cycle_reading_not_finite`） | 是 | 需要反事实模型，且须固定动作（`Shock`） |
| (d) 含有继续生成的成分 | 否 | 否 | 否 | 否 | 否 |
| (e) 加入惰性条件时判决不变 | 是（审查 Q4） | 是：所需为 0 的依存不会不被满足；加入从不被侵蚀的条件，living 不变（`adjoin_living`） | 是，同上 | 对已有主张是；但所需为 0 的条件为每个活跃形成新增活的关系主张，并经“同一条件或同一事件”免费连通整体（审查 Q4 在关系层重现） | 是 |

（a）（b）（c）（e）各行经 P7b 更正，见 §11。

**形式上的约束。** 两条结果限定了可能的选择，各有其范围（第二次独立审查 F2、F7）。

1. `finite_reading_credits_consumption`：任何由有限前缀决定、并记入整段读法判为更新的每次运行的读法，必记入它判为消耗的某次运行。有反馈的支持门控定律中同样如此（`Feedback.prefix_does_not_decide`）。它是否构成 (a) 与 (c) 的冲突，取决于两点：Ren 的判决是否要求越过阈值之前的事件按整段分类来判（这是诠释，§11 F11）；以及可观测量是否带数量。按数量的读法可由有限历史判定，并扣下每一次超出更新的汲取（`amount_reading`），它只是不记入每次整段更新的运行。
2. `Overdetermined.no_difference` 与 `no_finite_segment_makes_difference`：用单一部分的、整段层面的 but-for 检验代替参与，不能满足 (a)。多重决定时，每一方都可以说“我的一份无关紧要”；在一个形成的渐进耗竭中，整段的结局由尾部决定。步层面的检验挑出断裂事件（`breaking_event_makes_step_difference`）；NESS 一类检验（§8.6）是另外的对手。

所以，若“这段汲取是消耗”是关于整段结局的判断，有限的过去不能决定它。按数量的或条件式的读法能否给出 Ren 的判决，需要一个带数量与更新率的网，仍开放。

**对审查所列其余对手的处理。**

- **数量读法与条件式读法**（第二次独立审查）。“该步所取不超过该步的更新”由有限历史决定，扣下每一次超出（`amount_reading`）；它需要带数量与更新率的可观测量，在 `Web` 上不能表达。“继续这一步的汲取会消耗”在已知定律下可由状态判定，需要对过程定律的知识；未形式化。
- **整体方向读法。** Ren 的原话是“一种整体的……方向”。上面的约束说明，判断方向需要对运行之继续的说明。这一读法因此与比较原则 C 和实践判断的位置相合：它们比较的正是整段继续，而不是孤立的事件。但现有的 `living` 是事件或关系上的谓词，没有表示“更多”与多样性，这是 (d) 的缺口。
- **能力读法**（Sen、Nussbaum，先前知识）。它把 living 读作已实现并保持开放的功能能力，直接回应 (d)。仓库中已有[当前能力与最终可达](../../../../theories/becoming/results/records/effective-capacity-and-eventual-reachability.md)的区分，可作接口；本次没有把它接入 `living`。
- **自创生或代谢读法**（Maturana 与 Varela、Jonas、Thompson、Moreno 与 Mossio，先前知识）。活的组织靠汲取并转化条件来维持自身，汲取下降本身是生命的构成部分。这里的读法不把汲取本身判为不活：只有在之后某个曾被满足的依存不被满足的那一步汲取（逐步，定义见 §12），或汲取一个被消耗的条件（整段），才不记入。在更大关系的更新之内的代谢，在周期读法下被记入（`dip_within_two`）。但逐步读法有一个与代谢读法相冲突的代价：`draws` 不带数量，一个曾被满足而尚未恢复的依存之下，哪怕取得很少、甚至不改变任何水平的汲取也被扣下（7.1，`Pinned`）。
- **热力学读法**（Schrödinger、Nicolis 与 Prigogine，先前知识）。若每个形成都汲取这样的条件，而每个这样的条件最终都永久低于某个依存者的需要，整段读法在整个历史中都没有 living 事件。逐步读法保留损失之前各步；但一旦某个曾被满足的依存在其仍成立时永久不被满足，逐步读法扣下此后在该条件上的每个汲取事件。所以在一个逐渐耗尽的世界里，两种读法在损失之后都不记入任何汲取者，整段读法连损失之前也不记入。这是对无穷运行上“不息”的直接压力，也是 (c) 的另一面：整段读法的判决取决于无穷的未来。

**作者的候选分工（AI 论证，未经 Ren 确认）。** 一种分工能同时尊重这些约束：

- G0 所记入的“已实现的活”，取关系层或逐步的读法，即与他者依存相容、可由有限探究判定、不判定被断裂者的读法；
- “这一共同活动是更新还是消耗”的判断，属于对整段继续的比较，即 C 与实践判断的位置，并要求对继续的探究（§8.2）。

这一分工的代价必须写明。在逐步的 living 下，[relational-reading-comparison](../../../../theories/becoming/results/records/relational-reading-comparison.md) 中“去掉消耗者的继续是生成性扩展”的排序不再由 C 单独得出：消耗者在越过阈值之前的事件被记入，于是两次继续各有对方没有的活的内容，成为 C 不决定的混合情形，要靠更强的比较或 J 承诺。整段读法得到这一排序，代价是 (b) 与 (c)。这一段原是未形式化的论证；§9 已在核心上证明它，并发现共享对以消耗取胜的排序在逐步读法下仍然保持。第二次独立审查写明这一代价的条件：消耗者须在损失之前有被记入的事件（§9 的 `credited` 假设）；它并预期失去的只是与不在场的比较，不是与节制的比较；§9 在二元定律族中、对每步都满足所需的节制证明了这一点（`malignant_restraint`），有第三个形成共用条件时，与节制的比较也可以失去（`ThirdParty`，§12）。

哪一种读法，或哪一种组合，是生生的读法，是规范与诠释上的选择。它属于 Ren 的方向，本研究不替 Ren 作出。上表与两条形式约束是作出这一选择所需的材料。

### 8.6 作者反审

**反驳 1：but-for 检验太粗，现有理论早有更好的因果归属（NESS、结构方程中的实际因果）。**

*回应。* 同意，这里不提出因果理论。结果只表明，在多重决定下，单独的 but-for 差别制造与关系参与分离，并且前者取决于其他各方的部分。更精细的归属（例如 NESS 检验会把每个汲取者都算作某个充分集合的必要成员）可以作为另一种读法加入，届时需要它自己的定义和定理。

**反驳 2：扣除“其余不变”是虚构的。**

*回应。* 在 `Pool` 与 `withheld` 里，扣除只改动一方或一步的汲取量，过程本身给出由此到达的配置。一个应用中扣除是否让其余不变，是建模义务；模块说明写明了这一点。

**反驳 3：`prefix_does_not_decide` 用的是一个没有反馈的玩具过程。**

*回应。* 视界结果是一个存在性结果：只需一个过程就说明，有限前缀在一般意义上不决定分类。在有反馈的过程中，越过阈值之后的损失不会回来（`no_return_below_support`），但阈值之前的前缀仍可以与一次及时停止的运行相同。原回应说这在支持门控定律中是否也成立没有证明；P7b 已证明（`Feedback.prefix_does_not_decide`）：同一起点、`h` 之前每步汲取两个单位，停止的一次从不到达阈值，继续的一次消耗。反馈不是问题所在。

**反驳 4：替代例的依存是“按支持定义的”，不会被断裂。**

*回应。* 焦点形成对共同条件的依存在条件跌破所需的那一步仍按步起点计为断裂，同时消解，对替代条件的依存形成。按支持选择依存，是把“能替代”写进模型：它是建模选择，不是结论。结论是在这一选择下分类仍然保持。

**反驳 5：回程等级只是重新命名。**

*回应。* 定义很直接。内容在三处：`consumed_iff` 给出消耗端的精确刻画；季节性例子得到精确的等级；回程与有界回程之间有严格差别（`Slowing`），说明不被消耗并不意味着恢复的时间有界。

### 8.7 边界

- 不推出责任、义务或排序；关系读法与 but-for 读法都不是因果理论。
- 回程等级、视界与实际历史的对应，恢复变慢的经验意义，是应用与经验义务。
- `Pool`、`Slowing`、`depleting`、视界见证与 P7b 的见证（`NewNeed`、`Pinned`、`LateMet`、`Shock`、`Feedback`）都是最小见证。替代例中替代条件的水平不变，汲取替代条件的代价没有建模。
- 读法的选择、继续生成的成分、不依赖运行的读法与条件的对应纪律仍开放（§7.3）。
- 本节经第二次独立审查（[审查](BECOMING-P7-REVIEW.md)）：数学接受，侵蚀与 but-for 的定义已修正，十五项更正见 §11。

## 9. C 在各读法下的排序（P8）

2026-10-09。按同一指示继续。§8.5 的分工有一个只作了论证的代价：在逐步读法下，C 看来不再把过度汲取者的不在场排在其在场之上。本节在核心上证明它，并检验另一个排序（共享对以消耗取胜）是否保持。成果记录：[ranking-under-readings](../../../../theories/becoming/results/records/ranking-under-readings.md)。

```text
Result(s): 复用 relational-reading-comparison（整段读法的两个排序）、becoming-stepwise-reading（逐步读法）、
           relational-renewal-classification（支持门控定律）；新增 ranking-under-readings（L4）
Delta: 在核心上重述并比较两种读法下 C 的排序；不在场者扩展在场者，仅当读法扣下该形成的每个事件；
       逐步读法下对不在场的排序失去，对共享的排序保持
Supplied premises / correspondence: C 是公开的比较前提；“不在场”的继续与 relational-reading-comparison 相同
Evidence: Becoming.Ranking 15 项定理（P8 时；P7b 后 19 项，P9b 后 27 项）；Becoming.Bridge 的两条对应定理；合并检查器回执（见记录）
Boundary: 不推出责任或义务；不选择读法
Integration: §8.5 的代价由论证变为定理；relational-reading-comparison 的下一步部分承接
```

[Becoming.Ranking](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Ranking.lean)（L4）把两次继续（course）作为一个框架的配置，读法所记入的事件作为其实现的主张；C 就是这一框架上的 `Comparison`。

| 声明 | 内容 |
|---|---|
| `wholeRun`、`stepwise`、`stepwise_iff` | 两种读法：活跃且在该继续中不消耗；活跃且不侵蚀。后者恰是 `Web.valuation` 的 living |
| `withheld_of_extends` | 对任何只记入活跃事件的读法：不在场的继续扩展在场的继续，仅当读法扣下该形成的每个事件 |
| `whole_run_extends`、`whole_run_ranks` | 整段读法下，对支持门控定律族中每个超出更新地汲取的焦点形成，不在场扩展在场，每个满足 C 的比较都把不在场排得更高（核心上重述 relational-reading-comparison） |
| `credited_before_loss` | 焦点形成在某步活跃，而该步之后每个所需仍被满足，则逐步读法记入这一事件 |
| `stepwise_unranked`、`admits_occurrence`、`readings_rank_differently` | 逐步读法下，只要焦点形成有一个被记入的事件，两次继续互不扩展；于是有一个满足 C、非自反、传递的比较偏好在场的继续 |
| `malignant_ranking`、`winning_ranking` | 恶性增殖与以消耗取胜都是实例：整段读法下每个满足 C 的比较都偏好不在场；逐步读法下 C 不决定 |
| `sharing_credited`、`stepwise_contest` | 逐步读法下，胜者在损失之前的事件（第 0、1 步）被记入，第 2 步不被记入；共享的继续记入每个事件，所以它仍扩展以消耗取胜的继续 |
| `Restraint`、`stops_credited`、`restraint_ranks` | 节制：每个所需始终被满足的继续，两种读法都记入其每个事件；它扩展同一族中过度汲取使维持者失去支持的继续，所以两种读法下每个满足 C 的比较都把节制排得更高，即使过度汲取者在损失之前的事件被记入（P7b；只在二元定律族中，§12） |
| `malignant_restraint` | 恶性增殖与同一形成在第一步之后、越过阈值之前停止相比：第一步相同，两次继续中逐步读法都记入它；两种读法下 C 都把停止排在恶性增殖之上（P7b） |
| `Immediate`、`ThirdParty` | 没有被记入的焦点事件时，逐步读法同样把不在场排得更高；有第三个形成共用条件时，逐步读法不把节制排在过度汲取之上（P9b，§12） |

`Becoming.Bridge` 另证明核心的整段读法就是 `RenewalComparison.relationalInventory`（`Ranking.wholeRun_iff`），不在场继续的水平就是它的 `undisturbed`（`Ranking.undisturbed_eq`）。

**解读。** 两个排序在逐步读法下分道。共享对以消耗取胜：两次继续里胜者都在场，共享的继续记入胜者的全部事件，又多出被断裂者在损失之后的活，所以仍是扩展。不在场对在场：不在场的继续根本没有那个形成；焦点形成有一个使每个所需仍被满足的事件时，在场的继续里这一事件被记入，所以不在场不是扩展（没有这样的事件时，逐步读法同样把不在场排得更高，`Immediate`，§12）。`withheld_of_extends` 说明这不是逐步读法的偶然：任何记入该形成某个事件的读法，都使 C 单独不能把它的不在场排得更高。要得到关于恶性增殖的判决的比较形式（“没有它更好”，C 的 AI 形式路线），比较所用的读法必须扣下它在损失之前的事件，整段读法正是如此；或者在 C 之外加更强的比较，例如 J1 的基本条件优先。

与节制的比较不同（`restraint_ranks`、`malignant_restraint`，P7b）。同一形成在越过阈值之前停止的继续，记入它在两次继续中共有的早期事件，又多出维持者此后的活，所以在两种读法下都是扩展。在二元定律族中，逐步读法下 C 失去与不在场的比较，不失去与每步都满足所需的节制的比较（第二次独立审查 §3 的预期）；有第三个形成共用条件时，与节制的比较也可以失去（`ThirdParty`，§12）。

这使 §8.5 的选择更精确，但不替 Ren 作出：

- 若 G0 与 C 共用一种读法，逐步读法保持“共享优于以消耗取胜”，失去“没有恶性增殖更好”；整段读法两者都保持，代价是 (b) 与 (c)。
- 若 G0 的记入取逐步读法、C 的比较取整段读法（§8.5 的候选分工），两个排序都保持，但 G0 与 C 不再共用一种 living 读法。形式上两者各自以读法为参数，并不强制共用；但前提卡上 C 所说的“活的内容”就是 G0 的 living，分开取须在前提卡上公开。

**作者反审。**

*反驳 1：“不在场”的继续是虚构的比较世界。* 它与 relational-reading-comparison 用的是同一继续，水平由同一定律在焦点形成不出现时给出（`Ranking.undisturbed_eq`）。是否把它当作可行的选项，是实践判断的问题，这里只问 C 的排序。

*反驳 2：`preferOccurs` 是为结论构造的。* 它只表明 C 不决定：C 只要求扩展被排得更高，没有说别的。它不是任何人会采用的比较；结论是 C 单独不足，而不是在场更好。

*反驳 3：逐步读法下胜者的早期事件被记入，这本身就说明逐步读法错了。* 这正是读法选择的内容之一。在逐步读法下，那些事件在发生时与他者的依存相容；判它们为不活，需要知道运行此后怎样继续（`Becoming.Horizon`）。

**边界。** 只在支持门控定律族与三对比较继续中证明（§11、§12）；不涉及关系层读法（其焦点形成的第一个关系同样被记入，结论相同，但未单独形式化）；不推出责任、义务或可行性。本节经第三次独立审查，更正见 §12。

## 10. 条件的对应纪律（P9）

2026-10-09。按同一指示继续。第一次独立审查列出的、会改变其判断的第一种结果是：一条排除惰性或虚设条件的对应规则，并证明在声明的类中连通在这一规则下仍成立（§7.3 第 1 项）。本节在核心上给出一条，并写明它不解决什么。成果记录：[condition-correspondence-discipline](../../../../theories/becoming/results/records/condition-correspondence-discipline.md)。

```text
Result(s): 复用 becoming-stepwise-reading（逐步 living、共同参与与侵蚀）、metaethical-core-characterization（significant_iff）；
           新增 condition-correspondence-discipline（L4）
Delta: 一条条件的对应纪律：一方汲取、另一方以正水平依存，两个事件才经由该条件相关；
       惰性条件不再免费连通；在声明的类中连通仍成立；写明未解决的部分
Supplied premises / correspondence: 纪律本身是公开的对应选择；“每个形成都汲取并依存于某条件”一类主张是应用义务
Evidence: Becoming.Correspondence 21 项定理（P9 时；P9b 后 25 项）；合并检查器回执（见记录）
Boundary: 不改变 living；不处理时间次序；只对逐步读法陈述
Integration: §7.3 第 1 项部分承接；审查 Q4 在纪律下排除，Q5 只排除共同依存的一半、传递的一半仍在（§12），Q10 未解决
```

[Becoming.Correspondence](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Correspondence.lean)（L4）保留逐步读法的 living（活跃且不侵蚀），只把 `related` 从共同参与收窄为交互。

| 声明 | 内容 |
|---|---|
| `Bearing`、`Interacts`、`Idle` | 以正水平依存（条件能使之落空）；两个事件经由某条件交互：一方汲取，另一方以正水平依存，在任何步上；条件惰性：没有活动汲取它，或没有依存能落空 |
| `Web.interaction`、`interaction_narrows` | living 与 `Web.valuation` 相同，`related` 改为经由某条件交互；交互蕴含共同参与 |
| `Idle.not_interacts`、`Idle.not_undermining` | 惰性条件不构成任何关系，也不使任何事件侵蚀 |
| `adjoin`、`adjoin_living`、`adjoin_connected_iff` | 加入一个从不被侵蚀的条件，living 不变；加入惰性条件，关系与连通也不变 |
| `inert_connects` | 审查 Q4 在纪律下：加入人人在水平 0 依存、无人汲取的条件，living 不变，共同参与下每个网都连通，交互下连通不变 |
| `UnderminingOn.interacts`、`valuing_undermining_reaches` | 每个侵蚀关系都是交互；在 N_rel 下，珍视一个侵蚀事件的立场，必珍视被侵蚀形成在以正水平依存于该条件的每一步上的活的事件 |
| `connected_of_commons`、`significant_iff_of_commons` | 一个条件，每个活的事件都汲取它或以正水平依存于它，且有活的汲取者与活的依存者，使整体连通（任意两个活的事件至多经两次交互相连）；于是 G0 恰等于种子加 N_rel 加 N_std |
| `Shared.connection_by_living_use` | 两个形成依存于同一条件。条件的使用维持它们的支持时，二者经由这一使用连通；唯一的使用侵蚀它们时，二者不连通。共同参与在两次运行中都连通它们 |
| `universal_connects` | 未解决的部分：加入一个被更新、人人汲取并以正水平依存的条件，living 不变，每个网在交互下都连通 |
| `drawing_reaches`、`one_use_connects`、`Later`、`Pinned.drawing_interacts` | 传递由汲取承担；剩余的免费连通只需人人以正水平依存、一次使用；交互不排定时间，也不问效果（P9b，§12） |

**解读。**

- **免费的连通被排除。** 纪律把“什么算相关”从共同参与收窄为交互：一方汲取、另一方以正水平依存于同一条件，在任何步上。这是结构上的共现，还不是一方的汲取落在另一方的支持上（§12）。惰性条件上没有交互，所以 Q4 的免费连通不再成立；Q5 中“只共同依存也算相关”的一半不再成立，“珍视任何汲取者即达到每个依存者”的一半仍在（`drawing_reaches`）。
- **living 与 related 读同一种关系。** 逐步读法扣下一个事件，正是因为它与某个依存者有这种交互（`UnderminingOn.interacts`）。纪律下的关系不是另加的，而是 living 已经在读的关系。
- **连通由活的使用造成。** 经由一个条件的连通，需要一个活的汲取者与一个活的依存者。使一个条件连通整体的，是对它不侵蚀的使用。这与 Q10 相容：Q10 说粗的共同条件在其依存落空时使汲取它的事件不 living；纪律下，那样的条件本来就不能经由那些事件连通。
- **代价。** 在 `Shared` 中，唯一的使用侵蚀依存者时，依存者彼此不经由这一条件连通。在 N_rel 下，意义从一个依存者传到另一个，需要别的关系。G0 在那里仍可以直接采用，只是 `significant_iff` 的刻画所需的连通不由这一条件给出。侵蚀者与被侵蚀者之间有交互，所以珍视侵蚀者的立场仍达到被侵蚀者（`valuing_undermining_reaches`）。
- **纪律排除不了的。** 一个被更新、人人以正水平依存、被一个活的事件使用一次的条件，在网上与真实的共同条件（例如人人呼吸的空气）无法区分（`one_use_connects`；人人汲取的情形是 `universal_connects`）。它的内容是一个事实主张，即每个形成都实际以正水平依存于它，由应用检验，而不是免费得到。纪律把免费的连通变成了需要证据的连通。

**作者反审。**

*反驳 1：只共同依存于同一条件（例如两株植物依存于同一阳光），也是一种关系，纪律把它丢了。* 对：共同依存已是一种关系，即经由共同条件的共同构成；两株植物经同一阳光已经相关，遮光是另加的关系，不是第一种关系。纪律选择省略它，并没有表明它不是关系，省略的代价见 `Shared`；应用若要把它算作关系，须写出它。“没有形成汲取的条件，其水平不受任何形成的活动影响”是对应上的意图，不是 `Web` 的性质（§12）。纪律是公开的选择；共同参与这一选择及其后果 Q4 都保留在核心上。

*反驳 2：`draws` 不带数量，所以汲取本身也可以是虚设的。* 对。人人“汲取”、无人以正水平依存的条件是惰性的（`Idle` 的第二种情形），不构成关系；但人人以正水平依存、被使用一次的条件（`one_use_connects`）在网上排除不了。纪律排除的是结构上不能承载交互的条件，不是虚假的汲取或依存声明。

*反驳 3：被侵蚀者彼此不连通，是纪律的缺陷。* 这是纪律的代价，已证明并写明（`Shared`）。共同参与下它们连通，但同一选择使 Q4 免费。两种选择各有代价，由 Ren 选择。

*反驳 4：交互不管时间。* 与共同参与相同，本节没有处理。按时间次序的纪律（汲取不晚于依存）会使连通类更窄，列为开放。交互也不问汲取是否改变水平（`Later`、`Pinned.drawing_interacts`，§12）。

**边界。** 纪律只对逐步读法陈述；依存不变时，它经 `K.dependence.along r` 适用，整段读法可以取同一关系，这里没有做。纪律不改变 living，不处理时间次序，不解决 Q10 与剩余的免费连通（`universal_connects`、`one_use_connects`），不选择读法。纪律本身是公开的对应选择，不是展开的推论。本节经第三次独立审查，更正见 §12。

## 11. 第二次独立审查与更正（P7b）

2026-10-09。按同一指示继续。另一 agent（Claude Opus 5.5，未参与撰写）独立审查了 P7（§8）与 §7.1 对“不侵蚀”的选取，并读了 P8 中与读法比较相关的部分（[审查](BECOMING-P7-REVIEW.md)）。它在仓库之外重新编译全部 P7 模块，接受每条定理，公理报告为空；判定 `UnderminingOn` 与 `UnderminingFor` 的定义需修正、but-for 检验须固定动作；指出散文在七处强于 Lean，§8.5 的表在 (a)(b) 两行与 but-for 一栏上不公允。审查附有 23 条无公理的探针。本节记录逐项处理。更正都在核心上：探针的内容作为定理移入相应模块，公理报告为空。

```text
Result(s): 修正 becoming-stepwise-reading（侵蚀的定义）、becoming-return-grades、becoming-finite-horizon、
           joint-difference-making、substitution-preserves-consumption、ranking-under-readings、
           becoming-dependence-dynamics；不新增结果记录
Delta: “曾被满足”改为“在依存成立期间曾被满足”（MetSince）；but-for 检验固定动作；
       视界结果在有反馈的定律中成立；按数量的读法逃出视界结果；整段与步层面的差别制造分开；
       替代的“保持”只对整段读法成立；逐步读法下 C 仍把节制排在过度汲取之上
Supplied premises / correspondence: 不变；判据 (a) 的来源改写为 Ren 采纳的问题与 Ren 所述的不重叠
Evidence: Becoming.Dependence 39、Return 29、Horizon 14、Joint 16、Substitution 6、Ranking 19 项定理；
          合并检查器回执 20261009T013859.515931Z（236 项定理／451 项声明审计，公理报告全空）
Boundary: 读法的选择仍属 Ren；越过阈值之前的事件怎样判，Ren 的原话未定
Integration: 审查的 F1–F15 全部处理；它列出的会改变判断的结果中，第 1、4、5 项完成，第 2、3 项开放（第 1、5 项经第三次独立审查改为部分完成，§12）
```

### 11.1 逐项处理

| 项 | 审查所见 | 处理 |
|---|---|---|
| F1 | `UnderminingOn` 的“当时或此前被满足”只比较现在的所需与过去某步的水平，不要求依存当时成立：一个新来的依存者使此后每个汲取者都侵蚀 | 定义修正：`Web.MetSince t g c`，存在 `s ≤ t`，依存从 `s` 到 `t` 每步都成立，且 `t` 时的所需不超过 `s` 时的水平（P9b 再修正为：`s` 时的所需被满足，且 `t` 时的所需不超过 `s` 时的所需，§12）。`UnderminingOn`、`UnderminingFor` 与关系层读法都用它；原有见证的所需不变，按新定义重证，结论不变。审查的反例成为 `NewNeed.never_met_not_undermining`：旧子句成立而 `MetSince` 不成立，汲取者在任何一步都不侵蚀，而整段读法经继承的 `Consumed` 仍计它为消耗 |
| F2 | (a)(c) 的冲突依赖对 (a) 的一种读法与不带数量的可观测量，不依赖缺少反馈 | §8.5 约束 1 重述；新增 `Commons.whole_run_credits_overdraw`、`Commons.amount_reading`、`Feedback.prefix_does_not_decide`；§8.2 解读、§8.6 回应 3、章节 §2 与 §6.3、记录 becoming-finite-horizon 相应更正；“未知的是动作，不是动力学”作为论证写入 §8.2 |
| F3 | 替代之后，逐步读法记入消耗者 | `Substitution.stepwise_credits_substitution`；§8.4、模块说明、章节与记录改为“只对整段读法保持，几乎由定义给出”；加入 (a) 一行 |
| F4 | 逐步、周期与关系层读法不满足 (b) | `Pool.within_share_undermines`、`Pinned.undermining_without_effect`；(b) 一行改为“部分”；§7.1 的代价加上“甚至不改变任何水平” |
| F5 | 偏好“不侵蚀”的理由是反事实的，定义不是 | `Pinned` 表明侵蚀读的是共同参与一个未恢复的短缺，不是对不回程的贡献；“使条件回不来”限于公地见证：§7.1、`Dependence` 模块说明与热力学一条改写 |
| F6 | but-for 固定配置而不固定动作 | 定义修正：`Dependence.BreaksBy`，`MakesDifference` 与 `Overdetermined` 都相对于实际所取的动作；`Pool` 重证；`Shock.move_decides` 表明不固定动作时动作决定结果（P9b 补上“动作可取”，§12） |
| F7 | `depletion_is_joint` 是尾部不变性；步层面的 but-for 挑出断裂事件 | `Commons.no_finite_segment_makes_difference`、`Commons.breaking_event_makes_step_difference`；§8.3、§8.5 约束 2、章节与模块说明分开整段与步层面的检验 |
| F8 | “更新即一步周期内更新”只有一个方向 | `LateMet.within_one_not_renewing`；模块说明与 §8.1 改为“更新蕴含一步周期内更新” |
| F9 | 周期读法并非都由有限的步决定 | `Commons.cycle_reading_not_finite`；改为“事件层面的逐步与周期读法” |
| F10 | 周期长度 0 是退化的 | `Web.renewedWithin_zero`、`Web.undermining_for_zero`；写明周期取 `p ≥ 1` |
| F11 | 判据 (a) 的来源，以及“采用” | 在[来源](../../../../sources/15-codex-theory-conversations/2026-10-09-renewing-consuming-without-axioms.md)中，癌、军备竞赛与自我强化的“赢”这一列举是 AI 审查的文字；Ren 引用它，要求以关系结构分开两类形成、不需要任何 axiom，并说生成与退化不重叠。(a) 改为“Ren 采纳的问题与 Ren 所述的不重叠”，越过阈值之前事件的判决标为 AI 的延伸；“采用”改为“工作候选，待 Ren 选择”（§7.1、模块说明、章节、记录） |
| F12 | 热力学一条缺前提 | 加入“若每个形成都汲取这样的条件”，并补上损失之后的另一半 |
| F13 | 章节 §4 英文“Two spine facts”后面列了四条 | 改为“Four” |
| F14 | `drawing_after_loss` 的“draws nothing” | 改为“takes nothing (action 0)”，并注明公地的 `draws` 对数量盲，在 0 时也是 |
| F15 | 记录 | 五个记录按审查更正；relational-reading-comparison 中的“his”改为“Ren's” |

### 11.2 新的已检查声明

| 模块 | 声明 | 内容 |
|---|---|---|
| Dependence | `Web.MetSince`、`Web.MetSince.now` | 依存在成立期间曾被满足（定义经 P9b 修正，§12）；依存现在成立并被满足，即是 |
| Dependence | `NewNeed.never_met_not_undermining` | 见 F1 |
| Dependence | `Pinned.undermining_without_effect` | 外来的崩塌使水平在每一步之后都是 0。汲取与不汲取的两次运行水平处处相同；汲取的一次从第 1 步起每个事件都侵蚀，整段读法计它为消耗 |
| Return | `Web.renewedWithin_zero`、`Web.undermining_for_zero`、`LateMet.within_one_not_renewing` | 见 F8、F10 |
| Horizon | `Commons.whole_run_credits_overdraw`、`Commons.amount_reading`、`Commons.cycle_reading_not_finite` | 见 F2、F9 |
| Horizon | `Feedback.law`、`Feedback.prefix_does_not_decide` 及其引理 | 支持门控定律中的视界结果 |
| Joint | `Dependence.BreaksBy`、`Shock.move_decides` | 相对于动作的 but-for；不固定动作时动作决定结果 |
| Joint | `Pool.within_share_undermines` | 见 F4 |
| Joint | `Commons.no_finite_segment_makes_difference`、`Commons.breaking_event_makes_step_difference` | 见 F7 |
| Substitution | `Substitution.extracting_low`、`Substitution.stepwise_credits_substitution` | 见 F3 |
| Ranking | `Ranking.Restraint`、`stops_credited`、`restraint_ranks`、`malignant_restraint` | 节制：每个所需始终被满足的继续扩展过度汲取的继续，两种读法下 C 都把它排得更高；恶性增殖与在阈值之前停止相比也是如此（审查 §5 第 5 项） |

`Becoming.Horizon` 另证明 `le_of_add_le_add_right` 与 `add_right_cancel` 的无公理版本：Lean 4.29.1 中同名的核心引理依赖 `propext`。

### 11.3 审查列出的会改变判断的结果

1. 修正 `UnderminingOn` 并重证逐步定理：P7b 时部分完成（F1），只在所需不变时合乎其意；P9b 改为比较那一步的所需后完成（§12）。§7.1 对三个候选的比较成立。
2. Ren 的原话或决定：对以消耗取胜的判决是否覆盖越过阈值之前事件的整段分类。开放，属于 Ren。
3. 一个带数量与更新率的网，以及一个满足 Ren 所述的 (a)、可由有限历史判定的读法，或证明每个这样的读法都在某个有来源的情形中不满足 (a)。开放。`amount_reading` 在公地过程中给出前者的雏形，但不在 `Web` 上。
4. 相对于动作的 `MakesDifference` 并重证 `Pool`，以及渐进耗竭的步层面陈述：完成（F6、F7）；P9b 补上“动作可取”（§12）。
5. 证明逐步读法下 C 把在阈值之前的节制排在恶性过度汲取之上：部分：在二元定律族中完成（`malignant_restraint`），有第三个形成共用条件时不成立（`ThirdParty`，§12）。

### 11.4 作者反审

*反驳 1：修正 `UnderminingOn` 只是让定义合乎散文。* 修正使定义在所需不变时合乎它要表达的意思（对它的一个依存，在成立期间曾被满足）；所需变化时还不合乎，P9b 再修正（§12）。审查的反例由此成为定理，而不是被隐去：旧子句的行为保留在 `never_met_not_undermining` 的第三个合取项中。

*反驳 2：按数量的读法说明“不带数量”是表示的缺陷，应当先给 `Web` 加数量。* 同意它是表示所省略的关系，不是对理论的反驳。加数量与更新率会改变什么可表达，须连同新的反例一起做，列为开放（§11.3 第 3 项）。

*反驳 3：节制的结果太容易：停止的继续每一步都满足所需。* 定理本身简单；它的内容在于逐步读法下也成立，即使过度汲取者在损失之前的事件被记入。在二元定律族中，这把 §9 的代价限于与不在场的比较；有第三个形成共用条件时并非如此（§12）。

**边界。** 不改变读法选择的地位；不推出责任或义务；探针与新见证都是最小见证。P8（§9 的原有部分）、P9（§10）与本节当时尚未经独立审查；第三次独立审查及其更正见 §12。

## 12. 第三次独立审查与更正（P9b）

2026-10-09。按同一指示继续。另一 agent（Claude Opus 5.5，未参与撰写）独立审查了 P8（§9）、P9（§10）与 P7b 的更正（§11）（[审查](BECOMING-P8-P9-P7B-REVIEW.md)）。它在仓库之外从前导重新编译全部声明，公理报告为空，计数、哈希与别名都对，数学接受。问题在定义与散文的对应上，共十二项（G1–G12），附无公理的探针。审查没有发现替 Ren 作出的选择，也没有发现把 AI 文字当作 Ren 原话之处；它指出“没有它更好”被写成 Ren 所采纳的判决的形式（G11）。本节记录逐项处理。定义的修正都在核心上；探针的内容作为定理移入相应模块，公理报告为空。

```text
Result(s): 修正 becoming-stepwise-reading（MetSince）、joint-difference-making（MakesDifference）、ranking-under-readings、
           substitution-preserves-consumption、condition-correspondence-discipline、becoming-finite-horizon；
           becoming-dependence-dynamics 只改计数；不新增结果记录
Delta: MetSince 比较那一步的所需；依存中断一步即开始新的一段（披露）；MakesDifference 要求动作在扣除后可取，Determined 写明
       检验何时合乎其意；逐步读法失去与不在场的比较，须有被记入的事件；节制的结论限于二元定律族；替代者被扣下的不止一步；
       交互是结构上的共现，传递由汲取承担，剩余的免费连通只需一次使用
Supplied premises / correspondence: 新增披露：依存的一段须不间断；外来冲击写进动作，不写进步骤关系；共同依存是纪律所省略的关系
Evidence: Becoming.Dependence 51、Joint 20、Substitution 7、Ranking 27、Correspondence 25 项定理；
          合并检查器回执 20261009T025042.064543Z（265 项定理／502 项声明审计，公理报告全空）；外围桥接 20261009T025129.902360Z
Boundary: 读法的选择仍属 Ren；排定时间、对效果敏感的交互与二元定律族之外的节制定理开放
Integration: G1–G12 全部处理；审查列出的会改变判断的结果中，第 1、5 项完成，第 2 项披露，第 3、4 项开放，第 6 项属于 Ren
```

### 12.1 逐项处理

| 项 | 审查所见 | 处理 |
|---|---|---|
| G1 | `MetSince` 比较现在的所需与过去某步的水平。所需下降时，一个从未被满足的依存，因早先的水平足以覆盖现在较小的所需，被算作曾被满足；所需增长时，以较小所需的满足被算作满足了增长后的依存 | 按审查的第一种方案重定义：存在 `s ≤ t`，依存从 `s` 到 `t` 每步都成立，`s` 时的所需被满足，且 `t` 时的所需不超过 `s` 时的所需。`UnderminingOn`、`UnderminingFor` 与关系层读法都经它；原有见证的所需不变，增加的子句由 `Nat.le_refl` 给出，结论不变。探针成为 `FallingNeed.never_met_not_undermining` 与 `RisingNeed.grown_need_not_met`：两者中汲取者在任何一步都不侵蚀。§7.1、§11、章节、术语表与记录随之更正 |
| G2 | 依存中断一步即抹去此前的满足 | 披露为假设：依存的一段须不间断，休眠或迁出是否表示为持续的依存，是应用义务（记录 becoming-stepwise-reading、§7.1）。`Gap.lapse_starts_afresh`：中断时汲取者在任何一步都不侵蚀，而整段读法计它为消耗；依存连续时，它自第 3 步起每步都侵蚀。经有界缺席延续一段，列为开放 |
| G3 | 逐步读法“失去与不在场的比较”须有被记入的焦点事件，八处省去这一假设 | 各处补上“焦点形成有一个使每个所需仍被满足的事件时”（根模块、`Ranking` 模块说明、§9、章节 §6.5、记录标题与关联）。`Ranking.Immediate.stepwise_ranks_absence`：第一步就越过支持的形成，在两种读法下都排在其不在场之下 |
| G4 | “失去的只是与不在场的比较”只在二元定律族中、对每步都满足所需的节制证明 | 改为“在二元定律族中，失去与不在场的比较，保留与每步都满足所需的继续的比较”。`Ranking.ThirdParty.restraint_unranked_stepwise`：有第三个形成共用条件时，逐步读法下两次继续互不扩展，整段读法下节制仍扩展过度汲取。记录的限制改为三对比较继续；§11.3 第 5 项改为“部分” |
| G5 | 替代者“只在一步上不被记入”只对 `extracting` 成立 | 改为“维持者失去支持之前被记入，此后到它转向为止被扣下（`extracting` 中一步）”。`Substitution.slow_withheld_two_steps`：在 `slow` 中第 2、3 步都被扣下 |
| G6 | 相对于动作的 but-for 需要动作在扣除后可取，并在步骤是动作的函数时才准确；记录中“把外来冲击写进过程”恰会重新引入原问题 | `MakesDifference` 加入 `∃ t, P.step (withhold f s) a t`。新增 `Determined`（动作决定步骤），证明 `Shock.determined` 与 `Pool.determined`，所以 `Pool` 与 `Shock` 的结论照旧成立。探针成为 `Hidden.shock_in_the_step`（冲击写进步骤关系时，损失又被多重决定）与 `Tagged.move_unavailable`（动作在扣除后不可取时，没有“可取”一项则每一方都空洞地造成差别，有了它则没有哪一方造成差别）。记录的建模指示改为“把外来冲击写进动作，不写进步骤关系”；术语表的差别制造补上“同一动作”与“该动作可取” |
| G7 | 交互不排定时间、不问汲取的效果，却被说成“一方的汲取落在另一方的支持上” | 改为“一方汲取、另一方以正水平依存于同一条件，在任何步上”；排定时间、对效果敏感的版本列为开放。`Later.drawing_connects_earlier`：第 5 步的汲取与只在第 0 步成立的依存交互，并连通二者。`Pinned.drawing_interacts`：不改变任何水平的汲取也交互。§10 反驳 1 中关于水平的一句改为对应上的意图，不是 `Web` 的性质 |
| G8 | 剩余的免费连通只需一次使用 | `Web.one_use_connects`：对有一个活的事件的网，加入人人在水平 1 依存、只被该事件的形成在该步汲取一次的条件，条件被更新，living 不变，网在交互下连通。剩余部分改为“人人以正水平依存、被使用一次的条件” |
| G9 | “Q5 不再成立” | 改为“Q5 只排除共同依存的一半；传递的一半仍在：任何汲取都传递”（`Web.drawing_reaches`） |
| G10 | 把共同依存称为“处境的相关” | 改为“纪律所省略的关系（经由共同条件的共同构成）”；两株植物经同一阳光已经相关，遮光是另加的关系；`Shared` 显示省略它的代价 |
| G11 | “没有它更好”被写成 Ren 所采纳的判决的形式 | §9 改为“关于恶性增殖的判决的比较形式（“没有它更好”，C 的 AI 形式路线）”；joint-difference-making 改为“该结果所记录的 C 的排序，它们把 Ren 所采纳的问题形式化”；§8.2、章节 §6.3、英文 P7b 段与 becoming-finite-horizon 改用“Ren 所采纳的问题” |
| G12 | 计数与条目 | §9 写明各阶段的定理数；排序记录的限制与反例补齐；章节术语表补上交互、承担与惰性条件三条；§8.5 末段按 G4 收窄；becoming-stepwise-reading 的 P7b 历史条目保留原文，由新的历史条目更正 |

### 12.2 新的已检查声明

| 模块 | 声明 | 内容 |
|---|---|---|
| Dependence | `Web.MetSince`（修正） | 依存自某步起不间断成立，那一步的所需被满足，且现在的所需不超过那时的所需 |
| Dependence | `FallingNeed.web`、`FallingNeed.never_met_not_undermining` 及其引理 | 所需由 3 降到 1，依存每一步都不被满足；第 5 步起现在的所需不超过第 0 步的水平，但那不算；汲取者在任何一步都不侵蚀，整段读法计它为消耗 |
| Dependence | `RisingNeed.web`、`RisingNeed.grown_need_not_met` 及其引理 | 所需 1 在第 0–4 步被满足，自第 5 步增长为 2 而从未被满足，虽然第 0 步的水平足以覆盖它；汲取者在任何一步都不侵蚀 |
| Dependence | `Gap.away`、`Gap.held`、`Gap.lapse_starts_afresh` | 见 G2 |
| Joint | `Determined`、`Shock.determined`、`Pool.determined` | 动作决定步骤；两个原有过程满足它 |
| Joint | `Hidden.process`、`Hidden.shock_in_the_step`；`Tagged.process`、`Tagged.move_unavailable` | 见 G6 |
| Substitution | `Substitution.slow`、`Substitution.slow_withheld_two_steps` | 见 G5 |
| Ranking | `Immediate.law`、`Immediate.focal_withheld`、`Immediate.stepwise_ranks_absence` | 见 G3 |
| Ranking | `ThirdParty.courses`、`ThirdParty.focal_three`、`ThirdParty.restraint_unranked_stepwise` 及其引理 | 见 G4 |
| Correspondence | `Web.drawing_reaches` | 见 G9 |
| Correspondence | `Web.Condition.single`、`Web.one_use_connects` | 见 G8 |
| Correspondence | `Later.web`、`Later.drawing_connects_earlier`、`Pinned.drawing_interacts` | 见 G7 |

### 12.3 审查列出的会改变判断的结果

1. 重定义 `MetSince`，并以 `FallingNeed`、`RisingNeed` 为定理：完成（G1）。
2. 关于依存中断的规则：披露为应用义务（G2）；经有界缺席延续一段的定义开放。
3. 二元定律族之外的节制定理（有多个共用者，或带数量使不取者不侵蚀）：开放；`ThirdParty` 是它须面对的反例。
4. 排定时间、对效果敏感的交互，并重证 `connected_of_commons`：开放（G7、G8）。
5. `MakesDifference` 中的动作可取与动作决定步骤，并重证 `Pool` 与 `Shock`：完成（G6）。“动作可取”写进定义；“动作决定步骤”作为 `Determined` 陈述，原有过程满足它，但不作为定义的前提，因为非确定的过程可以把结果写进动作。
6. Ren 对读法的选择，以及 Ren 对越过阈值之前的事件、对“没有它更好”是否为 Ren 的判决的原话：属于 Ren。

### 12.4 作者反审

*反驳 1：修正 `MetSince` 又一次只是让定义合乎散文。* 这一次修正的是散文的意思中定义没有说出的部分：“曾被满足”是在那一步、以那时的所需被满足。所需增长时，以较小所需的满足是否算数，是一个读法选择；修正把它定为不算，并以 `RisingNeed` 写明，所以它是公开的选择，不是隐去的反例。

*反驳 2：依存中断即重开一段，对休眠与迁徙的生命不公平。* 同意这是一个有后果的表示选择。修正没有改变它，而是把它写成应用义务，并给出见证；若要经有界缺席延续，可以用 `ReturnsWithin p` 定义一段，列为开放。

*反驳 3：`ThirdParty` 说明逐步读法连节制都排不出，所以应当放弃逐步读法。* `ThirdParty` 的损失来自已披露的代价 (b)：节制者在第 3 步的事件被扣下，是因为第三者在那一步的汲取使它自己曾被满足的依存落空，而 `draws` 不带数量，节制者在那一步也算汲取。它表明代价 (b) 能达到节制的比较。是否因此放弃逐步读法，或给网加数量，是读法选择的材料，本节不作决定。

*反驳 4：交互既然不是“落在支持上”，纪律就没有根据。* 纪律原是公开的对应选择，它排除结构上不能承载交互的条件，这一点仍成立（`Idle`、`inert_connects`）。审查纠正的是解释：交互是共现，不是作用。排定时间、对效果敏感的版本会使纪律更接近这一解释，也会抬高剩余免费连通的价格。

**边界。** 不改变读法选择的地位；不推出责任或义务；探针与新见证都是最小见证。本节的更正尚未再经独立审查。

## 13. 继续生成：生起、不息与更新（P10）

2026-10-09。按同一指示继续（“prove the necessary proofs”）。第一次独立审查的判据 (d) 问读法是否含有继续生成的成分；§8.5 的表在每一栏都答“否”，§7.3 第 4 项把它列为开放。本节在核心上陈述生生的第二个“生”，并证明它与更新的关系。成果记录：[unceasing-generation-needs-renewal](../../../../theories/becoming/results/records/unceasing-generation-needs-renewal.md)。

Ren 的原话是：“我的答案是生生不息 - 一种整体的，不断创造更多生的方向，而这个方向产生的可能性，多样性越高，复杂性/复杂结构的复杂度可以不断的上升，就是一个好的方向”（[来源](../../../../sources/15-codex-theory-conversations/2026-10-07-shengsheng-ethical-direction.md)）。本节只形式化其中“不断…生”这一部分：生成在整体的继续中不止息。“更多”、可能性、多样性与复杂性不在这里。Ren 说的是整体的方向，所以这一成分陈述在整体的继续上，不陈述在单个事件上（这是作者的读法）。

```text
Result(s): 复用 becoming-renewal-reading（下降原则 falls_finitely、公地过程）、becoming-dependence-dynamics（依存网、形成与消解）、
           becoming-stepwise-reading（侵蚀）、becoming-return-grades（周期读法）；新增 unceasing-generation-needs-renewal（L3）
Delta: 生起与不息的生成；有限条件家族的总水平原则；在支付前提与“上升由形成造成”之下，不息的生成需要更新复现；
       更新不蕴含生成；以消耗进行的生成停止；替代推迟终结而不逃脱；总水平不升的有限家族不能维持不息的生成
Supplied premises / correspondence: 在没有条件上升之步，生起由家族中某个条件的下降支付；每次上升由某个活跃形成的更新造成；
       条件家族有限；renews 是应用给出的可观测量
Evidence: Becoming.Generation 18 项定理；合并检查器回执（见记录）
Boundary: 不含伦理谓词；不陈述“更多”、多样性与复杂性；生成成分没有加入 living 的读法
Integration: §7.3 第 4 项与判据 (d) 部分承接；substitution-preserves-consumption 的下一步（替代条件有代价时替代链的去向）由 Relay 部分承接
```

[Becoming.Generation](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Generation.lean)（L3）：

| 声明 | 内容 |
|---|---|
| `Arises`、`Unceasing` | 形成跨某步生起：此前不活跃，此后活跃。生成不息：某个形成在任意晚的步生起。同一形成可以再生起：不息的是生起，不是某一形式 |
| `Rises`、`Falls`、`Still`、`Paid`、`stock` | 条件跨某步上升或下降；一个有限条件家族在某步都不上升；事件在家族都不上升之步使其中某个条件下降，即由家族支付；家族的总水平 |
| `RenewedBy`、`Regenerating` | 每次上升都由某个活跃形成更新该条件造成：展开之外没有更新的来源，太阳或河流也是其中的形成。一个活跃形成更新家族中的某个条件 |
| `stock_le`、`stock_lt`、`paid_finitely` | 家族都不上升时总水平不升，再有一个下降则总水平下降；从某步起都不上升的有限家族，只能支付有限次事件。这是 `Becoming.Renewal` 的下降原则用于总水平 |
| `Unceasing.rises`、`Unceasing.regeneration_recurs` | 生起由有限家族支付时，不息的生成使家族中某个条件在任意晚的步上升；每次上升都由更新造成时，更新的活动在任意晚的步复现 |
| `substitution_defers` | 一个在每个活跃步都使家族中某个条件下降的形成，在家族不再上升之后只活跃有限次，无论它怎样在家族中转移依存 |
| `conserved_ceases` | 总水平从不上升的有限家族，不能维持每次生起都降低总水平的不息生成 |
| `Commons.renewal_without_generation` | 只取所更新之量：条件被更新，任何形成都不生起。更新不蕴含生成 |
| `Growth.ceases` | 形成在汲取一个不被更新的条件时接连生起，条件被消耗，生成停止 |
| `Relay.defers` | 消耗者从第一个来源转向第二个，依存转化，然后终结：两个来源都不被更新 |
| `Bloom.unceasing`、`Bloom.readings` | 一个形成在另一个形成（太阳）更新的条件上反复生起：全部前提成立，生成不息，更新复现。逐步读法扣下它的每一次开花，两步周期的读法记入它 |

**解读。**

- **生成与更新的关系。** 在所述前提下，不息的生成严格强于复现的更新：不息的生成需要更新复现（`Unceasing.regeneration_recurs`），更新复现却可以没有任何生起（`renewal_without_generation`）。这给判据 (d) 一个在整体继续上的位置：“不损”的读法读出更新这一侧，继续生成是另加的、更强的成分。
- **以消耗进行的生成不能不息。** 在不被更新的条件上，形成可以接连生起（`Growth`），这正是增长，但生成停止。在有限个不被更新的条件之间替代，只推迟终结（`Relay`）。这把 §8.4 的“替代不证明更新”推进一步：替代条件有代价时，替代链本身终结。它与 Ren 所说的生成与退化不重叠相合：在这些前提下，只有退化的一侧不能不息。但这是关于有限条件与支付的定理，不是由定义得出的不重叠。
- **不息属于更大的展开。** 一个总水平从不上升的有限家族，即每次更新都由它自身的下降支付，不能维持不息的生成（`conserved_ceases`）。`Bloom` 中太阳更新而不被扣减，是因为这一表示省略了太阳自身的条件。按非二元方法，这是表示所省略的关系，不是外在的实体；若把太阳的条件放进家族并照实支付，生成会停止。所以在这些前提下，任何有限部分都不能独自不息，不息属于更大的展开及其更新关系。这是作者对定理的诠释（AI 论证），也是 §8.5 热力学读法的另一面。
- **逐步读法与生成。** `Bloom` 的每次开花都把自己的条件取到所需之下，由太阳在下一次之前恢复。工作候选的逐步读法扣下每一次开花，两步周期的读法记入它。这是 §8.5 中自创生／代谢读法所指代价在生成一侧的见证：一个不息地再生起的形成，在逐步读法下没有一个活的开花事件。

**作者反审。**

*反驳 1：这些定理只是 `falls_finitely` 的推论。* 形式上是：总水平原则就是下降原则用于有限家族的总和，记录也这样写，不另算一条原则。新的是陈述的对象：生起与不息、更新由形成造成、替代链与总水平不升的家族，以及三个见证给出的严格分离。

*反驳 2：“生起由下降支付”是把结论写进模型。* 它是对应前提：生成不是无代价的，形成须从条件中取得。没有它，不息的生成可以不需要任何更新，例如一个形成无代价地反复出现。`Bloom` 与 `Growth` 显示前提可以满足，既可与不息的生成同时成立，也可与生成的停止同时成立。它的经验地位须由应用检验，例如开放系统中的能量流。

*反驳 3：“不息”只是无穷多次生起，太弱：一个形成忽隐忽现也算。* 对。所以“不息”须与支付前提同读：每次在没有更新之步的生起都付出条件，忽隐忽现也需要更新。Ren 原话中“更多生”的“更多”，以及可能性、多样性与复杂性的上升，这里没有陈述。

*反驳 4：把太阳当作展开中的一个形成，是在用形式变量偷渡“外部”。* 正相反：`RenewedBy` 要求每次上升都由展开中的某个活跃形成造成，排除了展开之外的来源；太阳在其中是一个形成。`conserved_ceases` 说明，把太阳自身的条件也照实计入时，有限的部分不能独自不息。

**边界。** 不含伦理谓词；不推出“不息更好”或任何排序；不陈述“更多”、多样性与复杂性；生成成分没有加入 living 的读法；见证都是最小见证；`renews` 与支付前提是应用义务。本节尚未经独立审查。

## English summary

P3b of the unification plan. The Becoming layer can now supply two correspondence items of the Universal Metaethical Core.

- **Runs carry the classification.** `Becoming.Renewal` reads any run through observables of conditions as a `RelationalRenewal` unfolding, so the renewing/consuming classification applies to every run of every process.
- **One principle.** The depletion, natural-rank recurrent-renewal and unrenewed-drawdown bounds are cases of one principle: an observable that never rises from some step on falls only finitely often.
- **The class belongs to the run.** In one process from one configuration, one run renews and another consumes.
- **The reading.** In `Becoming.Metaethics`, `Conditions.valuation` makes `living` the recorded relational reading and `related` participation in a common condition.
- **Connection.** Under a correspondence discipline for conditions and participation, a common condition discharges connection, so G0 there is exactly a seed with N_rel and N_std. Disjoint conditions can leave a whole unconnected. Without a discipline an inert or nominal condition connects everything (review Q4, Q10); one discipline is stated in §10.
- **Co-participation.** A consumer and what it consumes participate in a common condition. Under N_rel, valuing the consumer's activity therefore reaches the living events of what it consumes. This is relation by co-participation, not a claim that consumption is a further formed relation.

The author's counterreview (§4) concedes three points:

- the unification of bounds is organizational;
- the common-condition reading of `related` is coarse, a disclosed choice;
- the commons model lacks feedback.

It also records two inherited limits:

- dependence is static;
- the reading is whole-run, not stepwise.

Whether the relational reading is the right reading of 生生 remains a philosophical correspondence, not a Lean result.

**P6: dynamic dependence and the stepwise reading (§6).** At Ren's request to “pursue the theory of becoming, and prove the necessary proofs”, the two inherited limits are relaxed on the core.

- **Dependence belongs to the unfolding.** In `Becoming.Dependence`, which conditions a formation depends on, at what level, and which it draws on are observables of the configuration. Across each step a dependence is kept, broken, formed or dissolved. Constant dependence recovers the static reading exactly. Change is made at a step: a dependence that holds and later does not dissolved across some step between, stated without excluded middle.
- **Three outcomes of a loss.** The theorems connect three outcomes, which are neither exhaustive nor exclusive. Continuing with an unweakened dependence means the condition was restored. A formation still active after a loss without return has transformed its dependence; with fixed dependence it ends. In one process from one configuration, a dependence broken at the same step (under the convention that a step is read from its start) is followed by an ending, a transformation and a restoration. The reading of the break does not fix the next configuration; the move that makes the break selects the outcome.
- **Stepwise classification.** An event is within renewal when its step keeps every dependence on the conditions it participates in. Whole-run renewal credits every active step. A formation can be within renewal at each of its own steps without renewing in the run.
- **Evaluation.** As corrected after review (§7), `Web.valuation` reads `living` as active and not undermining (below).

The author's counterreview concedes that the dichotomies are short. The substantive content is that transformation becomes expressible and that the reading of a loss does not fix its outcome. The stepwise reading records relational situation, not causal contribution. Which reading of `living` to adopt remains a disclosed correspondence. The whole deduction remains open: modes distinguished by one structure in a representation do not establish the relational constitution of everything actual.

**Independent review and corrections (§7).** A separate Opus 5.5 agent that did not write the study reviewed §§1–6, the reading parts of `Becoming.Dependence` and `Becoming.Metaethics`, the chapter and six records ([review](BECOMING-RENEWAL-READING-REVIEW.md)). It accepted the mathematics, judged the philosophical warrant for the relational reading not established, and asked for twenty corrections, with thirteen axiom-free probes. The corrections are made in the core, the study, the chapter and the records. Three stepwise candidates for `living` are kept on the core with the witness that sets each aside:

- *within renewal* (`RenewingAt`, P6) withholds the formation whose dependence breaks at that step (`broken_formation`), and a requirement never met makes every participant not living;
- *not breaking* (review Q12) credits drawing after a loss, which breaks nothing further yet keeps the condition from returning (`drawing_after_loss`);
- *not undermining* (the working candidate in `Web.valuation`, pending Ren's choice): an event undermines when it draws on a condition at a step after which a dependence is unmet that was met, during its unbroken tenure, at a need no smaller than the present one (as corrected in P7b and P9b). Breaking is a case of undermining. This reading credits the broken formation, makes no drawer undermining through a dependence never met while it held, keeps both directions of divergence from the whole-run reading, and withholds the breaking step and drawing after a loss. Its cost: `draws` carries no amount and undermining does not ask what a draw does, so under a dependence once met and not yet restored any draw is withheld, however small, even one that changes no level.

A relation-level reading (`Web.relations`) is defined as well; the stepwise reading of an event is exactly the conjunction over its relations (`living_iff_relations`), and one event can have a living and an undermining relation (`Mixed`). The inherited `Consumed` admits requirements never met (`Unmet.consumed_without_loss`); this is disclosed in the foundation record without changing its bytes. Still open: a correspondence discipline for conditions (one is stated in §10), a run-independent reading connected to `universal_reason`, and a component of further generation in `living`.

**P7: return, horizon, joint activity and substitution (§8).**

- **Return grades** (`Becoming.Return`). Between renewal and consumption, renewal is graded by return time: kept every step, back within a bounded cycle, back eventually but without bound, and never back. `consumed_iff` shows that consumption is exactly a dependence that never returns. The seasonal condition of `RelationalRenewal` is renewed within two steps and not one; `Slowing` shows recovery can slow without bound while the condition is never consumed. Readings over cycles (`RenewingInWithin`, `UnderminingFor`) extend the stepwise ones, credit the dip over cycles of two, and withhold the escalation for every cycle.
- **Finite horizon** (`Becoming.Horizon`). For every horizon `h`, two runs of the same process agree before `h`, draw beyond renewal at every step and are within renewal at every step; afterwards one renews and the other consumes. Any reading fixed by the first `h` steps that credits every renewing run credits some consuming run. Judging a stretch of drawing as consumption, in the sense of its outcome, needs an account of how the run continues, not only observation of the past.
- **Joint difference-making** (`Becoming.Joint`). A but-for test within the process: withholding one party's part keeps the dependence. Under overdetermination no single part makes the difference, across formations (`Pool`) and, at the run level, across a formation's own events in gradual depletion (`depletion_is_joint`), while the relational reading still counts each drawer as consuming.
- **Substitution** (`Becoming.Substitution`). In the existing support-gated law, a consumer that can substitute another condition stays active, transforms its dependence at a step that can be found, and is still consuming on the whole-run reading; the sustaining formation ends. Its own continuation does not certify renewal.

The reading comparison (§8.5) shows two formal constraints, as scoped after the second review (§11): a reading fixed by a finite prefix that credits every whole-run-renewing run credits some consuming run, and single-part, run-level but-for difference-making cannot replace participation for criterion (a). The author proposes a split (an AI argument, not confirmed by Ren): the realized life credited by G0 takes a relation-level or stepwise reading, and whether a joint activity renews or consumes is a judgment about whole continuations, the place of comparison C and practical judgment. The split has a cost, now proved in §9. Which reading, or combination, is the reading of 生生 is a normative and interpretive choice in Ren's direction; this study does not make it on Ren's behalf. Section 8 was independently reviewed; the corrections are in §11.

**P8: what C ranks under each reading (§9).** `Becoming.Ranking` states comparison C over courses through a frame whose realized claims are the events a reading credits. The course without a formation extends the course with it only if the reading withholds every event of that formation (`withheld_of_extends`). Under the whole-run reading, for every law of the support-gated family in which the focal formation draws beyond renewal, every comparison satisfying C ranks the course without it higher, as relational-reading-comparison showed. Under the stepwise reading, when the formation has an event whose step leaves every need met, that event is credited, neither course extends the other, and an irreflexive, transitive comparison satisfying C prefers the course with it; malignant growth and winning by consumption are instances. When no focal event is credited, as when the first step already crosses support, the stepwise reading too ranks the absence higher (`Immediate`, §12). Sharing still extends winning by consumption under the stepwise reading, because sharing credits every event, the winner's included. So the two rankings part ways: a shared reading for G0 and C keeps "sharing is better than winning by consumption" under either reading, but "better without malignant growth" only under the whole-run reading or with a comparison stronger than C. The split of §8.5 keeps both, at the cost that G0 and C no longer share one reading of `living`; formally each takes its reading as a parameter, but the premise card reads C's "living content" as G0's, so a split must be disclosed there. The choice remains Ren's.

**P9: a correspondence discipline for conditions (§10).** `Becoming.Correspondence` keeps the stepwise reading of `living` and narrows `related` from co-participation to interaction: two events are related through a condition only when one draws on it and the other depends on it at a positive level, at any steps; this is a structural coincidence, not yet one's drawing bearing on the other's support (§12). A condition nothing draws on, or no dependence on which can fail, is idle. It relates nothing and undermines nothing, and adjoining one leaves `living`, the relation and connection unchanged. So the free connection of review Q4 is excluded, and co-dependence without interaction no longer counts as related, though valuing any drawing still reaches every dependent at a positive level (`drawing_reaches`, §12), so only half of Q5 is excluded. Every undermining relation is an interaction, so `living` and `related` now read the same relation, and under N_rel valuing an undermining event still reaches the formation it undermines. A condition on which every living event bears, with a living drawer and a living dependent, connects the whole, so G0 there is exactly a seed with N_rel and N_std. Connection through a condition is made by its living use: two dependents are connected through a use that keeps their support, and not when the only use undermines it, while co-participation connects them in both runs. What the discipline cannot exclude: a renewed condition on which every formation depends at a positive level, used once by a living event, connects any web without changing `living` (`one_use_connects`); its content is a factual claim that application must check. Q10 is not addressed, interaction does not order events in time, and the discipline is a disclosed choice, not a consequence of the unfolding. Section 10 was reviewed in the third independent review; its corrections are in §12.

**P7b: second independent review and corrections (§11).** A separate Opus 5.5 agent that did not write the work reviewed P7 and the choice of "not undermining" ([review](BECOMING-P7-REVIEW.md)). It recompiled every P7 module, accepted every theorem with empty axiom reports, and raised fifteen findings with 23 axiom-free probes. All are handled on the core.

- **Undermining is repaired.** "Met then or before" compared the present need with any past level, so a newly arrived dependent made every later drawer undermine. A dependence must now have been met at some step while it held (`MetSince`, refined in P9b to compare the need at that step); the old behaviour is the witness `NewNeed.never_met_not_undermining`.
- **But-for holds the move fixed.** `MakesDifference` and `Overdetermined` are relative to the move actually taken (`BreaksBy`); otherwise an exogenous shock decides them (`Shock.move_decides`).
- **The horizon result holds with feedback** (`Feedback.prefix_does_not_decide`), but the conflict between criteria (a) and (c) is scoped. The whole-run reading itself credits drawing beyond renewal in the renewing run (`whole_run_credits_overdraw`). A per-step amount reading is finitely decidable and withholds every overdraw (`amount_reading`); it escapes only by not crediting every whole-run-renewing run. Whether a verdict on the problem Ren adopted (winning by consumption) covers events before the threshold is interpretive: Ren adopted the problem and stated that generation and degeneration do not overlap; the verdict on pre-threshold events is an AI extension.
- **Run level and step level are distinct.** In gradual depletion no finite set of events makes the run-level difference (`no_finite_segment_makes_difference`), while the breaking event makes the step-level one (`breaking_event_makes_step_difference`).
- **Criterion (b) is only partly met** by the stepwise, cycle and relation readings: a drawer taking exactly the renewal undermines at a break another causes (`Pool.within_share_undermines`), and a drawer that changes no level undermines after an earlier loss (`Pinned.undermining_without_effect`). Undermining reads co-participation in an unrestored shortfall, not contribution to non-return.
- **Substitution preserves consumption on the whole-run reading only**, nearly by definition; the stepwise reading credits the substituting consumer before the sustaining formation loses support and withholds it until it switches, one step in `extracting` (`stepwise_credits_substitution`) and two in `slow` (§12).
- **Smaller corrections.** Renewal implies renewal within one step, not conversely (`LateMet`); cycle length 0 is degenerate; the formation-level cycle reading is not finitely decided; "adopted" becomes "working candidate, pending Ren's choice".
- **Restraint.** In the two-part family, under both readings C ranks a course in which every need stays met above overdraw, and malignant growth below the same formation stopping before the threshold (`restraint_ranks`, `malignant_restraint`). There the stepwise reading loses the comparison with the formation's absence; with a third formation sharing the condition the restraint comparison can be lost too (`ThirdParty`, §12).

Open: Ren's words on events before the threshold, and a web with amounts and renewal rates. P8, P9 and §11 were then not yet independently reviewed; the third review and its corrections are in §12.

**P9b: third independent review and corrections (§12).** A separate Opus 5.5 agent that did not write the work reviewed P8, P9 and the P7b corrections ([review](BECOMING-P8-P9-P7B-REVIEW.md)). It recompiled every declaration from the prelude with empty axiom reports, found the counts, hashes and aliases correct and accepted the mathematics. It raised twelve findings on the correspondence between definitions and prose, with axiom-free probes, and found no choice made on Ren's behalf and no AI text quoted as Ren's words. All findings are handled; the probes become core theorems.

- **Undermining compares the need then.** `MetSince` now asks that the need was met at some step of the unbroken tenure and that the present need is no greater than the need then. With a falling or a rising need, a dependence never met at its own need makes no drawer undermining (`FallingNeed`, `RisingNeed`). A one-step lapse starts a new tenure (`Gap`); whether dormancy is continuing dependence is an application duty.
- **But-for needs the move to be available.** `MakesDifference` requires the same move to be available from the withheld configuration (`Tagged`). It reads as intended when the move determines the step (`Determined`, which `Pool` and `Shock` satisfy); a shock written into the step relation makes the loss overdetermined again (`Hidden`). Exogenous shocks belong in the move.
- **The stepwise cost is scoped.** The comparison with absence is lost only for a formation with a credited event before the loss (`Immediate`). Restraint is kept only in the two-part family (`ThirdParty`). A substituting consumer is withheld from the sustaining formation's loss of support until it switches: one step in `extracting`, two in `slow`.
- **Interaction is a structural coincidence.** It ignores order and effect (`Later`, `Pinned.drawing_interacts`), so it is glossed as one drawing on a condition on which the other depends at a positive level, at any steps; an ordered, effect-sensitive version is open. Transmission is carried by drawing (`drawing_reaches`), so only half of Q5 is excluded, and the residual free connection needs only a condition everyone depends on at a positive level, used once (`one_use_connects`). Co-dependence is a relation the discipline omits, co-constitution through a common condition, not a mere correlation.
- **Provenance.** "Better without it" is the AI's comparative form of the problem Ren adopted (C's formal route), not Ren's verdict.

The core now has 265 theorems and 502 declaration audits, all with empty axiom reports. Open: a tenure through bounded absence, restraint beyond the two-part family, an ordered and effect-sensitive interaction, and Ren's choice of reading. These corrections have not been independently reviewed again.

**P10: continued generation (§13).** No reading of `living` includes further generation (criterion (d)). Ren's words name "a whole direction of unceasingly creating more 生"; `Becoming.Generation` states only its "unceasing" part, and states it on the whole's continuation. A formation arises across a step when it is inactive before and active after it; generation is unceasing when some formation arises at arbitrarily late steps. Suppose arising at a step where no condition of a finite family rises is paid by a fall in one of them. Then unceasing generation makes some condition of the family rise at arbitrarily late steps; and when every rise is made by some active formation renewing the condition, renewing activity recurs. Drawing exactly what is renewed keeps every dependence while nothing arises, so under these premises unceasing generation is strictly stronger than recurring renewal. Generation by consumption ceases (`Growth`); substitution among unrenewed conditions defers the end and does not escape it (`Relay`); and a finite family whose total never rises cannot sustain unceasing generation that lowers it, from which the author argues that no finite part is unceasing on its own. A bloom arising again and again on a condition the sun renews meets every premise; the stepwise working candidate withholds each of its blooms, and the reading over cycles of two credits it. "More", diversity and complexity are not stated, and the generation component has not been added to any reading of `living`. Section 13 has not been independently reviewed.
