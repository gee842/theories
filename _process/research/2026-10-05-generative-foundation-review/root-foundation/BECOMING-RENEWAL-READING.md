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
| 逐步读法的 living 改为“活跃且不侵蚀” | `Web.UnderminingOn`、`Web.UnderminingAt`、`Web.valuation` | 事件侵蚀：它在某步汲取某条件，该步之后，一个当时或此前被满足的依存不被满足。只看事件所汲取的条件，这是“不消耗”的逐步对应，两种读法因而同型。见下面三个候选的比较 |
| 断裂与侵蚀 | `Web.BreakingOn`、`Web.BreakingAt`、`BreakingOn.undermining` | 断裂：在某步汲取，该步断裂一个依存（起点满足、终点不满足）。断裂是侵蚀的一种 |
| `RenewingAt` 保留为逐步的更新分类 | `RenewingAt.not_undermining`、`RenewingAt.not_breaking`、`Commons.broken_formation` | 它是 `RenewingIn` 的逐步对应。在更新之内的事件既不侵蚀也不断裂；被断裂者在断裂之步不在更新之内，但也不侵蚀。Q1 作为 `RenewingAt` 的性质保留 |
| 损失之后的汲取 | `Commons.pausing`、`Commons.drawing_after_loss` | 损失之后继续汲取不再断裂任何依存，却使条件回不来：同样的第一步之后若不再汲取，条件回到。这样的事件侵蚀而不断裂 |
| 两个方向的分歧保持，且两种读法都记入被断裂者 | `Commons.readings_differ`（扩展） | 加码运行第 0 步：逐步记入、整段不记入；短暂下降第 0 步：整段记入、逐步不记入；加码运行中维持者在断裂之步的事件：两种读法都记入 |
| 继承的“消耗”不要求依存曾被满足 | `Unmet.consumed_without_loss`；`Web.Consumed` 的说明 | Q2：一个从未被满足的依存使条件被消耗、汲取者成为消耗型，而没有任何断裂或丧失；汲取者在任何一步都不侵蚀。`RelationalRenewal` 是基础模块，其字节不改，在 [relational-renewal-classification](../../../../theories/becoming/results/records/relational-renewal-classification.md) 中披露。整段 living 读法仍用继承的 `ConsumingIn`，所以 Q2 对整段读法仍成立 |
| 关系层读法 | `Web.relations`、`Web.living_iff_relations`、`Mixed.one_event_two_relations` | 审查 2.2 指出的最直接的对手。主张取为一个形成在某步对某条件的关系；事件的逐步读法恰是它所参与关系的读法的合取；同一事件可以有一个活的关系和一个侵蚀的关系 |
| 模块说明与声明说明 | `Becoming.Dependence`、`Becoming.Metaethics` | 见 7.2 的第 2、4、6、10–16、18 项 |

**三个逐步候选。** 逐步 living 先后有三个候选，每一个都保留在核心中，连同使它不被采用的见证：

| 候选 | 问的是 | 不采用的理由 |
|---|---|---|
| 在更新之内（P6，`RenewingAt`） | 该步维持它所参与的每个条件上的每个依存 | 被断裂者在断裂之步不被记入（审查 Q1，`Commons.broken_formation`）；从未被满足的依存使所有参与者都不 living（审查 Q2） |
| 不断裂（审查 Q12） | 它不在断裂某个依存的那一步汲取 | 损失之后的汲取不再断裂任何东西，于是被记入，虽然它使条件回不来（`Commons.drawing_after_loss`）。这与 Ren 关于以消耗取胜的判决不合 |
| 不侵蚀（采用） | 它不在之后某个曾被满足的依存不被满足的那一步汲取 | 保留两个方向的分歧；记入被断裂者；不受从未被满足的依存影响；扣下断裂之步与损失之后的汲取。代价：`draws` 不带数量，所以在一个曾被满足而尚未恢复的依存之下，任何汲取都被扣下，哪怕取得很少 |

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
| 9 | 披露 Q1、Q2，权衡 Q12 | 采用 Q12 的方向（只看所汲取的条件），再改为“不侵蚀”，理由见 7.1；Q1、Q2 与 Q12 的缺口都作为定理保留；记录的反例已加 |
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

1. **条件的对应纪律。** 一条排除惰性或虚设条件的规则，并证明在声明的类中连通仍成立。开放。
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
       but-for 差别制造在多重决定下与关系参与分离，在形成之间，也在一个形成的各事件之间；
       在既有的支持门控定律中，能替代条件的消耗者以转化依存的方式持续，仍是消耗的
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
| `RenewingInWithin`、`UnderminingFor` | 周期层面的两种读法：形成在 `p` 步周期内更新（它参与的每个条件都在 `p` 步内更新）；事件侵蚀 `p` 步（它在某步汲取某条件，一个当时或此前被满足的依存此后 `p` 步都不被满足） |
| `RenewingIn.within_one`、`undermining_for_one`、`RenewingInWithin.mono`、`UnderminingFor.anti`、`RenewingInWithin.not_consuming`、`RenewingInWithin.not_undermining_for` | 周期读法扩展逐步读法：更新即一步周期内更新，侵蚀即侵蚀一步；周期越长记入越多；在任何周期内更新的形成不消耗，它的事件也不侵蚀该周期 |
| `Commons.dip_within_two`、`Dip.renewing_within_two` | 两步周期下，短暂下降被记入：形成在两步周期内更新，事件不侵蚀两步，虽然它在断裂之步汲取；维持者在两步周期内更新，虽然它不在每步更新 |
| `Commons.escalation_undermines_for_every_cycle` | 加码之后条件不再回来：加码事件对每个周期都侵蚀，此前的事件不侵蚀 |

**解读。** “更新与消耗互斥但不穷尽”留下的中间区域，现在按回程时间分级：每步都维持、在有界周期内回到、终会回到但无界、以及不再回到（消耗）。`consumed_iff` 说明这一阶梯在消耗一端是精确的：不被消耗的条件，恰是没有哪个依存永不回程的条件。最后一个例子对应生态学中所谓“临界变慢”：系统接近转折点时，受扰后的恢复越来越慢（作者据先前知识，本次未新读文献）。这里只给出形式上的区分：回程无界变慢的条件仍不是被消耗的条件；它是否预示损失，是经验问题。

### 8.2 有限的历史不决定分类

[Becoming.Horizon](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Horizon.lean)（L3）：

| 声明 | 内容 |
|---|---|
| `Run.cons`、`Run.AgreeUpTo` | 在一次运行之前加一步；两次运行在 `h` 之前的配置与动作都相同 |
| `Commons.prefix_does_not_decide` | 对每个视界 `h`，同一过程的两次运行在 `h` 之前完全相同：每一步都超出更新地汲取，焦点形成的每个事件都在更新之内。此后一次在更新之内汲取，焦点形成是更新的；另一次继续超出，焦点形成是消耗的 |
| `Commons.finite_reading_credits_consumption` | 任何由前 `h` 步决定、并记入每次更新运行的读法，必记入某次消耗运行 |

**解读。** `class_belongs_to_the_run` 说分类不是初始配置的函数；这里更强：分类不是任何有限前缀的函数。逐步读法与周期读法都由有限的步决定，所以在条件还满足依存时，它们记入渐进的耗竭。要把一段汲取判为消耗，需要知道运行往哪里去，也就是对其继续的说明，不只是对过去的观察。这把评价与探究连在一起：L2 的所见范围由实际执行给出，而这里所需的正是对继续的探究。

### 8.3 共同活动中的差别制造

[Becoming.Joint](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Joint.lean)（L3）：

| 声明 | 内容 |
|---|---|
| `Dependence.Keeps`、`Dependence.Breaks`、`along_kept`、`along_broken`、`keeps_not_breaks` | 配置之间的维持与断裂；沿运行恰是 `Becoming.Dependence` 的维持与断裂；两者互斥 |
| `MakesDifference`、`Overdetermined`、`Overdetermined.no_difference` | but-for 检验：某步断裂依存，而扣除某一方的部分后每一步都维持它，则这一方的部分造成了差别。扣除任何单独一方的部分仍有断裂之步，为多重决定；此时没有哪一方单独造成差别 |
| `Pool.difference_belongs_to_the_joint` | 同一过程、同一水平、第一个汲取者取同样的量。另有一方汲取时，它的部分造成差别；另有两方汲取时，损失被多重决定，它的部分不造成差别，而扣除两方的部分则维持依存，差别由共同活动造成。两次运行中，关系读法都把它计为消耗；一个什么也不取的形成不计为消耗 |
| `Commons.overdraw_consumes` | 从某步起每步都汲取至少两个单位（每步更新一个），条件被消耗 |
| `Commons.depletion_is_joint` | 一个形成的各事件之间也是共同活动：每步超出更新的汲取消耗条件；第一个事件那一步维持依存，对任何周期都不侵蚀；扣除任何一个事件的汲取，条件仍被消耗，没有哪个事件单独造成差别 |

**扣除留在展开之内。** 比较的对象是同一过程中的另一个配置或运行，即那一方或那一事件的部分不在的配置或运行。没有在过程之外另设一个比较世界。

**解读。** 差别制造不属于一方自身的活动，而属于它与其他部分的共同关系；正如分类属于运行，结局不由断裂的读法决定。多重决定的情形正是“我的一份无关紧要”这一推理的形式。`depletion_is_joint` 显示它在时间中同样成立：渐进的耗竭里，每一步的汲取单独都不造成差别，共同造成了消耗。本仓库已有的散文论证说过“but-for 不可缺少性太强”（[整体过程实现审查](WHOLE-PROCESS-REALIZATION-REVIEW.md#three-inadequate-tests-and-the-stronger-identification)）与“冗余路线可以在去掉一条之后保持结果”（[展开保持审查](UNFOLDING-PRESERVATION-REVIEW.md#3-strong-rivals-and-the-distinctions-they-test)）；这里是这一点在依存网上的形式见证。关于集体伤害与过度决定的哲学讨论（如 Parfit 的“道德数学的错误”、Kagan 关于“我造成差别吗”的讨论）是重要对照，本次未新读，只作指引。

### 8.4 替代：消耗者以转化依存的方式持续

[Becoming.Substitution](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Substitution.lean)（L3）把替代放进既有的[支持门控定律](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/RelationalRenewal.lean)：共同条件由依存于它的维持者更新；汲取超出更新，更新本身随之终止，损失在定律内不会回来。

| 声明 | 内容 |
|---|---|
| `ceasing_step` | 对可判定的规定，停止成立的那一步可以找到（`ceases_at_a_step` 的可判定形式） |
| `Substitution.web`、`web_dependent` | 焦点形成在共同条件支持它时依存于它，否则依存于一个支持它的替代条件；共同条件的水平仍由原定律给出 |
| `Substitution.persists_consuming` | 从一开始就超出更新地汲取：能替代的焦点形成每步都活跃；它对共同条件的依存在一个可以找到的步上消解，对替代条件的依存同时形成；它在运行中是消耗的；维持者永久失去支持并终止 |
| `Substitution.extracting_persists_consuming` | 一个具体定律满足全部前提，上述结论不是空的 |

**解读。** 替代保持分类：一个以转化依存的方式熬过它参与造成的损失的形成，仍然是消耗的；它自身的持续不证明更新。连同既有结果，这一定律族在无回程的损失之后实现了终止（`dependent_overdraw_ends_itself`）与转化（本结果）；恢复要求更新者重新得到支持，在这一定律内不发生，由[有支持的修复路线](../../../../theories/becoming/results/records/supported-renewal-recovery.md)在另一定律中给出。这也是“赢的元吸引子”的一个结构：靠消耗取胜的一方可以转向别处而持续，失去者不随之恢复。

### 8.5 读法的比较

审查 §2.7 建议了五条判据。以下逐一对照本研究中已定义的读法。“是”“否”只在所述的范围内成立，括号内是依据。

| 判据 | 整段（不消耗） | 逐步（不侵蚀） | 周期 `p`（不侵蚀 `p` 步） | 关系层 | but-for 差别制造 |
|---|---|---|---|---|---|
| (a) 符合 Ren 有来源的判决：恶性增殖、以消耗取胜不是生生 | 是（relational-reading-comparison） | 部分：扣下断裂之步与损失之后的汲取（`broken_formation`、`drawing_after_loss`）；渐进耗竭在越过阈值之前被记入（`prefix_does_not_decide`） | 同逐步（`depletion_is_joint`） | 同逐步 | 否：多重决定下没有哪一方或哪一事件造成差别（`Pool`、`depletion_is_joint`） |
| (b) 不因一个条件的命运判定未改变它的被断裂者或旁观者 | 否：较晚的断裂者使较早、在更新之内的汲取者不 living（审查 Q11） | 是：被断裂者被记入（`readings_differ`、`broken_formation`）；只看事件所汲取的条件 | 是 | 是，且同一事件的不同关系分开（`Mixed`） | 是 |
| (c) 可由有限探究判定 | 否（`finite_reading_credits_consumption`） | 是：由到下一步为止的历史决定 | 是：由到其后 `p` 步为止的历史决定 | 是 | 需要反事实模型 |
| (d) 含有继续生成的成分 | 否 | 否 | 否 | 否 | 否 |
| (e) 加入惰性条件时判决不变 | 是（审查 Q4） | 是，由定义直接得出：所需为 0 的依存不会不被满足（未单独形式化） | 是，同上 | 是，同上 | 是 |

**形式上的约束。** 两条结果限定了可能的选择。

1. `finite_reading_credits_consumption`：(a) 与 (c) 在渐进耗竭上冲突。任何由有限前缀决定、又不扣下更新运行的读法，必记入某次消耗运行。所以没有一种可由有限历史判定的事件读法能扣下渐进耗竭的全部事件。
2. `Overdetermined.no_difference` 与 `depletion_is_joint`：用 but-for 差别制造代替参与，同样不能满足 (a)。多重决定时，每一方或每一事件都可以说“我的一份无关紧要”，而共同活动造成了消耗。

所以“这段汲取是消耗”是一个关于整段共同活动的判断，有限的过去不能决定它。

**对审查所列其余对手的处理。**

- **整体方向读法。** Ren 的原话是“一种整体的……方向”。上面的约束说明，判断方向需要对运行之继续的说明。这一读法因此与比较原则 C 和实践判断的位置相合：它们比较的正是整段继续，而不是孤立的事件。但现有的 `living` 是事件或关系上的谓词，没有表示“更多”与多样性，这是 (d) 的缺口。
- **能力读法**（Sen、Nussbaum，先前知识）。它把 living 读作已实现并保持开放的功能能力，直接回应 (d)。仓库中已有[当前能力与最终可达](../../../../theories/becoming/results/records/effective-capacity-and-eventual-reachability.md)的区分，可作接口；本次没有把它接入 `living`。
- **自创生或代谢读法**（Maturana 与 Varela、Jonas、Thompson、Moreno 与 Mossio，先前知识）。活的组织靠汲取并转化条件来维持自身，汲取下降本身是生命的构成部分。这里的读法不把汲取本身判为不活：只有在之后某个曾被满足的依存不被满足的那一步汲取（逐步），或汲取一个被消耗的条件（整段），才不记入。在更大关系的更新之内的代谢，在周期读法下被记入（`dip_within_two`）。但逐步读法有一个与代谢读法相冲突的代价：`draws` 不带数量，一个曾被满足而尚未恢复的依存之下，哪怕取得很少的汲取也被扣下（7.1）。
- **热力学读法**（Schrödinger、Nicolis 与 Prigogine，先前知识）。若每个条件最终都永久低于某个依存者的需要，整段读法在整个历史中都没有 living 事件；逐步读法保留此前各步。这是对无穷运行上“不息”的直接压力，也是 (c) 的另一面：整段读法的判决取决于无穷的未来。

**作者的候选分工（AI 论证，未经 Ren 确认）。** 一种分工能同时尊重这些约束：

- G0 所记入的“已实现的活”，取关系层或逐步的读法，即与他者依存相容、可由有限探究判定、不判定被断裂者的读法；
- “这一共同活动是更新还是消耗”的判断，属于对整段继续的比较，即 C 与实践判断的位置，并要求对继续的探究（§8.2）。

这一分工的代价必须写明（以下是作者的论证，没有形式化）。在关系层或逐步的 living 下，[relational-reading-comparison](../../../../theories/becoming/results/records/relational-reading-comparison.md) 中“去掉消耗者的继续是生成性扩展”的排序看来不再由 C 单独得出：消耗者在越过阈值之前的事件被记入，于是两次继续各有对方没有的活的内容，成为 C 不决定的混合情形，要靠更强的比较或 J 承诺。整段读法得到这一排序，代价是 (b) 与 (c)。把这一论证在核心上证明或否证，是下一步之一。

哪一种读法，或哪一种组合，是生生的读法，是规范与诠释上的选择。它属于 Ren 的方向，本研究不替 Ren 作出。上表与两条形式约束是作出这一选择所需的材料。

### 8.6 作者反审

**反驳 1：but-for 检验太粗，现有理论早有更好的因果归属（NESS、结构方程中的实际因果）。**

*回应。* 同意，这里不提出因果理论。结果只表明，在多重决定下，单独的 but-for 差别制造与关系参与分离，并且前者取决于其他各方的部分。更精细的归属（例如 NESS 检验会把每个汲取者都算作某个充分集合的必要成员）可以作为另一种读法加入，届时需要它自己的定义和定理。

**反驳 2：扣除“其余不变”是虚构的。**

*回应。* 在 `Pool` 与 `withheld` 里，扣除只改动一方或一步的汲取量，过程本身给出由此到达的配置。一个应用中扣除是否让其余不变，是建模义务；模块说明写明了这一点。

**反驳 3：`prefix_does_not_decide` 用的是一个没有反馈的玩具过程。**

*回应。* 视界结果是一个存在性结果：只需一个过程就说明，有限前缀在一般意义上不决定分类。在有反馈的过程中，越过阈值之后的损失不会回来（`no_return_below_support`），但阈值之前的前缀仍可以与一次及时停止的运行相同。这一点在支持门控定律中是否也成立，没有证明。

**反驳 4：替代例的依存是“按支持定义的”，不会被断裂。**

*回应。* 焦点形成对共同条件的依存在条件跌破所需的那一步仍按步起点计为断裂，同时消解，对替代条件的依存形成。按支持选择依存，是把“能替代”写进模型：它是建模选择，不是结论。结论是在这一选择下分类仍然保持。

**反驳 5：回程等级只是重新命名。**

*回应。* 定义很直接。内容在三处：`consumed_iff` 给出消耗端的精确刻画；季节性例子得到精确的等级；回程与有界回程之间有严格差别（`Slowing`），说明不被消耗并不意味着恢复的时间有界。

### 8.7 边界

- 不推出责任、义务或排序；关系读法与 but-for 读法都不是因果理论。
- 回程等级、视界与实际历史的对应，恢复变慢的经验意义，是应用与经验义务。
- `Pool`、`Slowing`、`depleting` 与视界见证都是最小见证。替代例中替代条件的水平不变，汲取替代条件的代价没有建模。
- 读法的选择、继续生成的成分、不依赖运行的读法与条件的对应纪律仍开放（§7.3）。
- 本节内容尚未经独立审查。

## English summary

P3b of the unification plan. The Becoming layer can now supply two correspondence items of the Universal Metaethical Core.

- **Runs carry the classification.** `Becoming.Renewal` reads any run through observables of conditions as a `RelationalRenewal` unfolding, so the renewing/consuming classification applies to every run of every process.
- **One principle.** The depletion, natural-rank recurrent-renewal and unrenewed-drawdown bounds are cases of one principle: an observable that never rises from some step on falls only finitely often.
- **The class belongs to the run.** In one process from one configuration, one run renews and another consumes.
- **The reading.** In `Becoming.Metaethics`, `Conditions.valuation` makes `living` the recorded relational reading and `related` participation in a common condition.
- **Connection.** Under a correspondence discipline for conditions and participation, a common condition discharges connection, so G0 there is exactly a seed with N_rel and N_std. Disjoint conditions can leave a whole unconnected. The discipline itself is not yet stated: an inert or nominal condition connects everything (review Q4, Q10).
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
- *not undermining* (adopted in `Web.valuation`): an event undermines when it draws on a condition at a step after which a dependence on it, met at or before that step, is unmet. Breaking is a case of undermining. This reading credits the broken formation, ignores never-met requirements, keeps both directions of divergence from the whole-run reading, and withholds the breaking step and drawing after a loss. Its cost: `draws` carries no amount, so under a dependence once met and not yet restored any draw is withheld, however small.

A relation-level reading (`Web.relations`) is defined as well; the stepwise reading of an event is exactly the conjunction over its relations (`living_iff_relations`), and one event can have a living and an undermining relation (`Mixed`). The inherited `Consumed` admits requirements never met (`Unmet.consumed_without_loss`); this is disclosed in the foundation record without changing its bytes. Still open: a correspondence discipline for conditions, a run-independent reading connected to `universal_reason`, and a component of further generation in `living`.

**P7: return, horizon, joint activity and substitution (§8).**

- **Return grades** (`Becoming.Return`). Between renewal and consumption, renewal is graded by return time: kept every step, back within a bounded cycle, back eventually but without bound, and never back. `consumed_iff` shows that consumption is exactly a dependence that never returns. The seasonal condition of `RelationalRenewal` is renewed within two steps and not one; `Slowing` shows recovery can slow without bound while the condition is never consumed. Readings over cycles (`RenewingInWithin`, `UnderminingFor`) extend the stepwise ones, credit the dip over cycles of two, and withhold the escalation for every cycle.
- **Finite horizon** (`Becoming.Horizon`). For every horizon `h`, two runs of the same process agree before `h`, draw beyond renewal at every step and are within renewal at every step; afterwards one renews and the other consumes. Any reading fixed by the first `h` steps that credits every renewing run credits some consuming run. Judging a stretch of drawing as consumption needs an account of how the run continues, not only observation of the past.
- **Joint difference-making** (`Becoming.Joint`). A but-for test within the process: withholding one party's part keeps the dependence. Under overdetermination no single part makes the difference, across formations (`Pool`) and across a formation's own events in gradual depletion (`depletion_is_joint`), while the relational reading still counts each drawer as consuming.
- **Substitution** (`Becoming.Substitution`). In the existing support-gated law, a consumer that can substitute another condition stays active, transforms its dependence at a step that can be found, and is still consuming; the sustaining formation ends. Its own continuation does not certify renewal.

The reading comparison (§8.5) shows two formal constraints. Criteria (a), matching Ren's sourced verdicts, and (c), decidability by finite inquiry, conflict on gradual depletion; and but-for difference-making cannot replace participation for (a). The author proposes a split (an AI argument, not confirmed by Ren): the realized life credited by G0 takes a relation-level or stepwise reading, and whether a joint activity renews or consumes is a judgment about whole continuations, the place of comparison C and practical judgment. The split has a cost, argued but not formalized: the ranking of continuations in relational-reading-comparison may no longer follow from C alone. Which reading, or combination, is the reading of 生生 is a normative and interpretive choice in Ren's direction; this study does not make it on Ren's behalf. Section 8 has not been independently reviewed.
