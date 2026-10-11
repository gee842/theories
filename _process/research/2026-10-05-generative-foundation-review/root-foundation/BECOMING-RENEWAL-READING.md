# 运行上的更新／消耗与生生的关系读法 / Renewal on runs and the relational reading

2026-10-09，Asia/Bangkok。AI（Claude）按 Ren 的指示“你自己全改了吧……先更新好计划，然后再一步步完整完成，保持代码和整体结构优雅”（[原话与解释](../../../../sources/15-codex-theory-conversations/2026-10-09-one-theory-unification.md)）完成[统一计划](BECOMING-UNIFICATION-PLAN.md)的 P3b。成果记录：[becoming-renewal-reading](../../../../theories/becoming/results/records/becoming-renewal-reading.md)。

## 1. 问题

Universal Metaethical Core 的前提卡里有三项对应：形成 E、连通、`living` 的读法。在 P2 中，`living` 和 `related` 是 `Valuation` 的外给参数，连通是假设。P3b 要回答的是：Becoming 层能否从展开本身给出这两项，从而让连通成为可以检查的动力学性质，而不是一条前提？

这里的“形成”和“条件”是同一展开中的分析角色：一个形成依存于某些条件，或从某些条件中汲取，或两者兼有。它们不是彼此独立的实体，也不是价值的所有者。在 Lean 中，它们是贯穿运行的固定索引类型，形成跨步的同一性由 `F` 规定（它在哪些读法中起作用，见 §16）；`draws` 只记录一个形成汲取某个条件，不记录汲取多少，水平的变化由过程给出。这两项省略在 §7 的审查后写明。两类的表示是一类关系项读法的特例，见 §18（P14）。

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

*回应。* 两者回答不同的问题。整段读法问：形成在整段运行中是否消耗。逐步读法问：一个事件所在的那一步是否维持其条件上的依存；审查后的 living 问：事件是否在这样一步汲取：之后条件既低于某个依存现在的所需，也低于它曾被满足的某个所需（§7，定义经 P11b 修正，§15）。`Commons.readings_differ` 证明两个方向都有分歧，所以不能把一个当作另一个的细化。但这样两者都不能单独是“生生的读法”（审查 2.7）；比较与判据见 §8.5。

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
| 逐步读法的 living 改为“活跃且不侵蚀” | `Web.UnderminingOn`、`Web.UnderminingAt`、`Web.valuation` | 事件侵蚀：它在某步汲取某条件，该步之后，条件既低于一个依存现在的所需，也低于该依存在不间断成立期间曾被满足的某个所需（定义经 P7b、P9b、P11b 修正，§11、§12、§15）。只看事件所汲取的条件，这是“不消耗”的逐步对应，两种读法因而同型。见下面三个候选的比较 |
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
| 不侵蚀（工作候选，待 Ren 选择） | 它不在这样一步汲取：之后条件既低于一个依存现在的所需，也低于该依存在不间断成立期间曾被满足的某个所需 | 保留两个方向的分歧；记入被断裂者；在依存成立期间从未以其所需被满足的依存不使汲取者侵蚀，只低于增长到从未被满足的所需也不算侵蚀，而所需增长之后低于曾被满足的所需的汲取侵蚀（定义经 P7b、P9b、P11b 修正，`NewNeed.never_met_not_undermining`、`FallingNeed.never_met_not_undermining`、`RisingNeed.grown_need_not_met`、`Stunted.stunting_undermines`）；扣下断裂之步与损失之后的汲取。代价：`draws` 不带数量，侵蚀也不涉及汲取的效果，所以在一个曾被满足而尚未恢复的依存之下，任何汲取都被扣下，哪怕恰取更新量（`Pool.within_share_undermines`），甚至不改变任何水平（`Pinned.undermining_without_effect`）；依存中断一步即开始新的一段，此前的满足不再计入（`Gap.lapse_starts_afresh`，§12），休眠或迁出是否表示为持续的依存，是应用义务 |

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

1. `finite_reading_credits_consumption`：任何由有限前缀决定、并记入整段读法判为更新的每次运行的读法，必记入它判为消耗的某次运行。有反馈的支持门控定律中同样如此（`Feedback.prefix_does_not_decide`）。它是否构成 (a) 与 (c) 的冲突，取决于两点：对 Ren 所采纳的问题的判决是否要求越过阈值之前的事件按整段分类来判（这是诠释，§11 F11）；以及可观测量是否带数量。按数量的读法可由有限历史判定，并扣下每一次超出更新的汲取（`amount_reading`），它只是不记入每次整段更新的运行。
2. `Overdetermined.no_difference` 与 `no_finite_segment_makes_difference`：用单一部分的、整段层面的 but-for 检验代替参与，不能满足 (a)。多重决定时，每一方都可以说“我的一份无关紧要”；在一个形成的渐进耗竭中，整段的结局由尾部决定。步层面的检验挑出断裂事件（`breaking_event_makes_step_difference`）；NESS 一类检验（§8.6）是另外的对手。

所以，若“这段汲取是消耗”是关于整段结局的判断，有限的过去不能决定它。按数量的或条件式的读法能否给出对 Ren 所采纳的问题的判决，需要一个带数量与更新率的网，仍开放。

**对审查所列其余对手的处理。**

- **数量读法与条件式读法**（第二次独立审查）。“该步所取不超过该步的更新”由有限历史决定，扣下每一次超出（`amount_reading`）；它需要带数量与更新率的可观测量，在 `Web` 上不能表达。“继续这一步的汲取会消耗”在已知定律下可由状态判定，需要对过程定律的知识；未形式化。
- **整体方向读法。** Ren 的原话是“一种整体的……方向”。上面的约束说明，判断方向需要对运行之继续的说明。这一读法因此与比较原则 C 和实践判断的位置相合：它们比较的正是整段继续，而不是孤立的事件。但现有的 `living` 是事件或关系上的谓词，没有表示“更多”与多样性，这是 (d) 的缺口。
- **能力读法**（Sen、Nussbaum，先前知识）。它把 living 读作已实现并保持开放的功能能力，直接回应 (d)。仓库中已有[当前能力与最终可达](../../../../theories/becoming/results/records/effective-capacity-and-eventual-reachability.md)的区分，可作接口；本次没有把它接入 `living`。
- **自创生或代谢读法**（Maturana 与 Varela、Jonas、Thompson、Moreno 与 Mossio，先前知识）。活的组织靠汲取并转化条件来维持自身，汲取下降本身是生命的构成部分。这里的读法不把汲取本身判为不活：只有在之后条件低于某个依存曾被满足的所需、也低于其现在所需的那一步汲取（逐步，定义见 §15），或汲取一个被消耗的条件（整段），才不记入。在更大关系的更新之内的代谢，在周期读法下被记入（`dip_within_two`）。但逐步读法有一个与代谢读法相冲突的代价：`draws` 不带数量，一个曾被满足而尚未恢复的依存之下，哪怕取得很少、甚至不改变任何水平的汲取也被扣下（7.1，`Pinned`）。
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

1. 重定义 `MetSince`，并以 `FallingNeed`、`RisingNeed` 为定理：完成（G1）。第四次独立审查指出所需增长之后的代价（H1），P11b 改为最小形式 `MetAbove`，见 §15。
2. 关于依存中断的规则：披露为应用义务（G2）；经有界缺席延续一段的定义开放。
3. 二元定律族之外的节制定理（有多个共用者，或带数量使不取者不侵蚀）：开放；`ThirdParty` 是它须面对的反例。
4. 排定时间、对效果敏感的交互，并重证 `connected_of_commons`：开放（G7、G8）。
5. `MakesDifference` 中的动作可取与动作决定步骤，并重证 `Pool` 与 `Shock`：完成（G6）。“动作可取”写进定义；“动作决定步骤”作为 `Determined` 陈述，原有过程满足它，但不作为定义的前提，因为非确定的过程可以把结果写进动作。
6. Ren 对读法的选择，以及 Ren 对越过阈值之前的事件、对“没有它更好”是否为 Ren 的判决的原话：属于 Ren。

### 12.4 作者反审

*反驳 1：修正 `MetSince` 又一次只是让定义合乎散文。* 这一次修正的是散文的意思中定义没有说出的部分：“曾被满足”是在那一步、以那时的所需被满足。所需增长时，以较小所需的满足是否算数，是一个读法选择；修正把它定为不算，并以 `RisingNeed` 写明，所以它是公开的选择，不是隐去的反例。（第四次独立审查指出，这一选择还有未披露的代价：所需增长之后，把水平压到曾被满足的旧所需之下的汲取也不算（`Stunted`）。P11b 改为最小形式，见 §15。）

*反驳 2：依存中断即重开一段，对休眠与迁徙的生命不公平。* 同意这是一个有后果的表示选择。修正没有改变它，而是把它写成应用义务，并给出见证；若要经有界缺席延续，可以用 `ReturnsWithin p` 定义一段，列为开放。

*反驳 3：`ThirdParty` 说明逐步读法连节制都排不出，所以应当放弃逐步读法。* `ThirdParty` 的损失来自已披露的代价 (b)：节制者在第 3 步的事件被扣下，是因为第三者在那一步的汲取使它自己曾被满足的依存落空，而 `draws` 不带数量，节制者在那一步也算汲取。它表明代价 (b) 能达到节制的比较。是否因此放弃逐步读法，或给网加数量，是读法选择的材料，本节不作决定。

*反驳 4：交互既然不是“落在支持上”，纪律就没有根据。* 纪律原是公开的对应选择，它排除结构上不能承载交互的条件，这一点仍成立（`Idle`、`inert_connects`）。审查纠正的是解释：交互是共现，不是作用。排定时间、对效果敏感的版本会使纪律更接近这一解释，也会抬高剩余免费连通的价格。

**边界。** 不改变读法选择的地位；不推出责任或义务；探针与新见证都是最小见证。本节的更正尚未再经独立审查。

## 13. 继续生成：生起、不息与更新（P10）

2026-10-09。按同一指示继续（“prove the necessary proofs”）。第一次独立审查的判据 (d) 问读法是否含有继续生成的成分；§8.5 的表在每一栏都答“否”，§7.3 第 4 项把它列为开放。本节在核心上陈述生起（变为活跃），作为生生第二个“生”的一种读法的形式载体（作者的读法；P11b 更正，§15），并证明它与更新的关系。成果记录：[unceasing-generation-needs-renewal](../../../../theories/becoming/results/records/unceasing-generation-needs-renewal.md)。

Ren 的原话是：“我的答案是生生不息 - 一种整体的，不断创造更多生的方向，而这个方向产生的可能性，多样性越高，复杂性/复杂结构的复杂度可以不断的上升，就是一个好的方向”（[来源](../../../../sources/15-codex-theory-conversations/2026-10-07-shengsheng-ethical-direction.md)）。本节只形式化其中“不断…生”这一部分：生成在整体的继续中不止息。“更多”、可能性、多样性与复杂性不在这里。Ren 说的是整体的方向，所以这一成分陈述在整体的继续上，不陈述在单个事件上（这是作者的读法）。

```text
Result(s): 复用 becoming-renewal-reading（下降原则 falls_finitely、公地过程）、becoming-dependence-dynamics（依存网、形成与消解）、
           becoming-stepwise-reading（侵蚀）、becoming-return-grades（周期读法）；新增 unceasing-generation-needs-renewal（L3）
Delta: 生起与不息的生成；有限条件家族的总水平原则；在消耗前提与“上升由形成造成”之下，不息的生成需要更新复现；
       更新不蕴含生成；以消耗为条件的生起停止；替代推迟终结而不逃脱；耗散使生成停止
       （P11b 更正用语与最后一项，原写作“总水平不升的有限家族不能维持不息的生成”，§15）
Supplied premises / correspondence: 在没有条件上升之步，生起时家族中某个条件下降（消耗前提，P11b 前称支付前提）；
       每次上升由某个活跃形成的更新造成；
       条件家族有限；renews 是应用给出的可观测量
Evidence: Becoming.Generation 18 项定理（P11b 之后 30 项，§15）；合并检查器回执（见记录）
Boundary: 不含伦理谓词；不陈述“更多”、多样性与复杂性；生成成分没有加入 living 的读法
Integration: §7.3 第 4 项与判据 (d) 部分承接；substitution-preserves-consumption 的下一步（替代条件有代价时替代链的去向）由 Relay 部分承接
```

[Becoming.Generation](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Generation.lean)（L3）：

| 声明 | 内容 |
|---|---|
| `Arises`、`Unceasing` | 形成跨某步生起：此前不活跃，此后活跃。生成不息：某个形成在任意晚的步生起。同一形成可以再生起：不息的是生起，不是某一形式 |
| `Rises`、`Falls`、`Still`、`Depletes`、`stock` | 条件跨某步上升或下降（净变化）；一个有限条件家族在某步都不上升；事件在家族都不上升之步使其中某个条件下降，即消耗家族（`depletes_iff`：这只说事件的每一步家族中有条件变化，与事件的关系不论）；家族的总水平 |
| `RenewedBy`、`Regenerating` | 每次上升都由某个活跃形成更新该条件造成：展开之外没有更新的来源，太阳或河流也是其中的形成。一个活跃形成更新家族中的某个条件 |
| `stock_le`、`stock_lt`、`depletes_finitely` | 家族都不上升时总水平不升，再有一个下降则总水平下降；从某步起都不上升的有限家族，只能被有限次事件消耗。这是 `Becoming.Renewal` 的下降原则用于总水平，总水平在这里只是下降的量度，与各条件的单位无关 |
| `Unceasing.rises`、`Unceasing.regeneration_recurs` | 生起消耗有限家族时，不息的生成使家族中某个条件在任意晚的步上升；每次上升都由更新造成时，更新的活动在任意晚的步复现 |
| `substitution_defers` | 一个在每个活跃步都使家族中某个条件下降的形成，在家族不再上升之后只活跃有限次，无论它怎样在家族中转移依存 |
| `dissipation_ceases` | 若一个量从不上升，而每次生起都使它下降（耗散），生成不是不息的。家族的总水平只在每次生起都使它下降时是这样的量（P11b 前为 `conserved_ceases`，只对总水平陈述） |
| `Commons.renewal_without_generation` | 只取所更新之量：条件被更新，任何形成都不生起。更新不蕴含生成 |
| `Growth.ceases` | 形成在汲取一个不被更新的条件时接连生起，条件被消耗，生成停止 |
| `Relay.defers` | 消耗者从第一个来源转向第二个，依存转化，然后终结：两个来源都不被更新 |
| `Bloom.unceasing`、`Bloom.readings` | 一个形成在另一个形成（太阳）更新的条件上反复生起：全部前提成立，生成不息，更新复现。逐步读法扣下它的每一次开花，两步周期的读法记入它 |

**解读。**

- **生成与更新的关系。** 在所述前提下，不息的生成严格强于复现的更新：不息的生成需要更新复现（`Unceasing.regeneration_recurs`），更新复现却可以没有任何生起（`renewal_without_generation`）。这给判据 (d) 一个在整体继续上的位置：“不损”的读法读出更新这一侧，继续生成是另加的、更强的成分。
- **以消耗为条件的生起不能不息。** 在不被更新的条件上，形成可以接连生起（`Growth`），这正是增长，但生起停止。在有限个不被更新的条件之间替代，只推迟终结（`Relay`）。这把 §8.4 的“替代不证明更新”推进一步：替代条件有代价时，替代链本身终结。在继续的层面，这与 Ren 所说的生成与退化不重叠相合（作者的读法）：在这些前提下，由不被更新的条件承担的生起不能不息。在单个事件的层面，`Arises` 包括以消耗为条件的生起；所以结果支持来源中 AI 修正说明的看法，即“持续形成新组织”的“持续”已排除消耗型。这是关于有限条件与消耗前提的定理，不是由定义得出的不重叠，也没有证明每个非消耗的样式都能不息（P11b 更正，§15）。
- **耗散与更大的展开。** 若一个量从不上升，而每次生起都使它下降（耗散），生成不能不息（`dissipation_ceases`）。`Bloom` 中太阳更新而不被扣减，是因为这一表示省略了太阳自身的条件。按非二元方法，这是表示所省略的关系，不是外在的实体。原文由此论证：把太阳的条件放进家族并照实计入，生成会停止，所以任何有限部分都不能独自不息。第四次独立审查指出这需要耗散前提：一个封闭循环的有限家族，总水平不变，可以维持不息的生成（`Recycle.closed_unceasing`）。所以论证只对每次生起都耗散的量成立，例如自由能；那是物理前提，不是定理的推论。家族的总水平还预设各条件的单位可公度（P11b 更正，§15）。在耗散之下，不息属于更大的展开及其更新关系。这是作者对定理的诠释（AI 论证），也是 §8.5 热力学读法的另一面。
- **逐步读法与生成。** `Bloom` 的每次开花都把自己的条件取到所需之下，由太阳在下一次之前恢复。工作候选的逐步读法扣下每一次开花，两步周期的读法记入它。这是 §8.5 中自创生／代谢读法所指代价在生成一侧的见证：一个不息地再生起的形成，在逐步读法下没有一个活的开花事件。

**作者反审。**

*反驳 1：这些定理只是 `falls_finitely` 的推论。* 形式上是：总水平原则就是下降原则用于有限家族的总和，记录也这样写，不另算一条原则。新的是陈述的对象：生起与不息、更新由形成造成、替代链与总水平不升的家族，以及三个见证给出的严格分离。

*反驳 2：“生起消耗家族”是把结论写进模型。* 它是对应前提：在没有补充之步，生起时家族中某个条件下降。（原文写作“生成不是无代价的，形成须从条件中取得”。`Depletes` 并不涉及生起的形成，`Tide` 中一个与之无关的潮落就满足它；P11b 删去此句，把前提系于生起的形成放在流的形式中，§15。）没有它，不息的生成可以不需要任何更新，例如一个形成无代价地反复出现。`Bloom` 与 `Growth` 显示前提可以满足，既可与不息的生成同时成立，也可与生成的停止同时成立。它的经验地位须由应用检验，例如开放系统中的能量流。

*反驳 3：“不息”只是无穷多次生起，太弱：一个形成忽隐忽现也算。* 对。所以“不息”须与消耗前提同读：在没有更新之步，每次生起时家族中都有条件下降，忽隐忽现也需要更新。Ren 原话中“更多生”的“更多”，以及可能性、多样性与复杂性的上升，这里没有陈述。

*反驳 4：把太阳当作展开中的一个形成，是在用形式变量偷渡“外部”。* 正相反：`RenewedBy` 要求每次上升都由展开中的某个活跃形成造成，排除了展开之外的来源；太阳在其中是一个形成。`dissipation_ceases` 说明，把太阳自身的条件也照实计入、并且每次生起都耗散时，有限的部分不能独自不息；没有耗散，封闭循环可以不息（`Recycle`，P11b 更正）。

**边界。** 不含伦理谓词；不推出“不息更好”或任何排序；不陈述“更多”、多样性与复杂性；生成成分没有加入 living 的读法；见证都是最小见证；`renews` 与消耗前提是应用义务。本节经第四次独立审查，更正见 §15。

## 14. 更多：流、供给与更新者（P11）

2026-10-09。§13 只形式化了 Ren 原话中的“不断…生”。本节陈述“更多”的一种读法，并证明它需要什么。成果记录：[more-needs-renewers](../../../../theories/becoming/results/records/more-needs-renewers.md)。

依存网只记录条件的水平。为了说“更多”，本节把条件读作数量：每一步参与的形成从条件取用多少、给予多少（流）。“更多”读作：对每个数，从某步起至少有那么多形成从一个有限的条件家族取用。这是作者的读法：更多的形成从同一组条件取用（P11b 更正：原写作“依赖同一组条件而活”；`More` 数的是流中的取用者，经 `Flow.Taking` 才与网中的活跃与汲取相连，§15）。可能性、多样性与复杂性的上升是“更多”的另外读法，这里不陈述。

```text
Result(s): 复用 unceasing-generation-needs-renewal（total、stock、RenewedBy、Arises、Unceasing、Bloom）、
           becoming-dependence-dynamics（依存网）；新增 more-needs-renewers（L3）
Delta: 条件作为形成取用与给予的数量；平衡的流使每次上升都由活跃的补充者造成，P10 的前提 RenewedBy 成为定理；
       消耗与补充的平衡在一步与任意一段上成立；不止地更多需要补充没有最终的界，每个形成给予有限时需要更新者的数目
       没有最终的界；不息的生成尚不是更多（P11b 更正用语，§15）
Supplied premises / correspondence: 流记录实际的取用与给予，present 每步只列每个参与的形成一次；
       “更多”读作从某步起取用者至少任意多；Capacity：每个形成每步给予家族的量有一个固定的上界；
       取用的量是自然数，所以每个取用者每步至少取用一个单位（P11b 写明）
Evidence: Becoming.Flow 28 项定理（P11b 之后 58 项，§15）；合并检查器回执（见记录）
Boundary: 不含伦理谓词；只读取用者的数目，不陈述多样性、复杂性与可能性；生成成分没有加入 living 的读法
Integration: unceasing-generation-needs-renewal 的下一步（陈述“更多”）部分承接
```

[Becoming.Flow](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Flow.lean)（L3）：

| 声明 | 内容 |
|---|---|
| `Flow`、`taken`、`given`、`Balances`、`Acting` | 每步参与的形成，以及每个形成从每个条件取用与给予的量。流平衡一个依存网：条件水平的每次变化恰是取用与给予之差。只有活跃的形成给予 |
| `count`、`steps`、`uptake`、`replenishment`、`takers`、`renewers` | 有限列表上的计数与连续的步（总和 `total` 来自 `Becoming.Generation`）；家族每步的取用与补充；从家族取用与补充家族的形成数目 |
| `Balances.over`、`Balances.accumulates` | 消耗与补充的平衡：一步之后家族的总水平加上取用，等于之前的总水平加上补充；对任意一段步也成立 |
| `Balances.renewedBy` | 平衡且只有活跃形成给予时，每次上升都由某个活跃的补充者造成：§13 的对应前提 `RenewedBy` 在这里成为定理 |
| `More`、`Capacity` | 不止地更多：对每个数，从某步起每一步至少有那么多形成从家族取用。每个形成每步给予家族的量至多一个固定量 |
| `More.replenishment_unbounded` | 不止地更多需要补充没有最终的界：没有一个从某步起成立的界，能界住家族所得的补充 |
| `More.renewers_unbounded` | 每个形成给予有限时，不止地更多需要补充者的数目没有最终的界 |
| `Garden.more` | 每一步都生起一个更新者和一个生长者：流平衡，只有活跃者给予，每个给予至多一单位，生成不息，并且不止地更多 |
| `Bloom.not_more` | §13 的开花反复生起，生成不息，流平衡，但至多一个形成取用：不息的生成尚不是更多 |

**解读。**

- **补充的层级，以及蕴含。** （P11b 更正。原文写作“构成一个层级，每一层需要的更新都比前一层多”与“给予者越来越多”。）在平衡的流中，三者各自所需的补充构成严格的层级：取用的形成不息地生起（`ArisesTaking`）需要补充在任意晚的步出现（`replenishment_recurs`）；不止地更多需要补充没有最终的界；`Bloom` 分开二者。三者本身只在所述对应之下按蕴含排列：复现的更新不蕴含不息的生成（`Tide.renewal_without_arising`），不息的生成不蕴含不止地更多（`Bloom.not_more`）；在活跃形成的普查之下、只有活跃的形成取用时，不止地更多蕴含不息的生成（`Flow.More.unceasing`），没有普查时不然（`Dormant`）。每个形成给予有限时，补充者的数目没有最终的界，并在平均的意义上越来越多（`Balances.renewers_over`），但可以在无穷多步上为零（`Pulse`）。
- **生生。** 由 `RenewedBy`，补充者是展开之内的形成。所以在 `Capacity` 之下，更多的取用需要补充更新的形成参与，其数目没有最终的界，在平均的意义上越来越多：生成的条件须由越来越多的形成补充。它们是否在展开中生起，定理没有陈述。这是作者对“生生”的一种结构读法（AI 论证），不替代 Ren 的原话，也不推出它是好的。若一个形成的给予可以无界地增长，更多可以由同一个补充者的增长承担；那也是一种“更多”，只是落在给予的量上。定理在 `Capacity` 下才把补充转为补充者的数目。读法的边界（P11b，§15）：补充者可以就是取用者自身（`Cycle.closed_more`），“补充的形成”不必是另一类；在 `Web` 与 `Flow` 中形成与条件是两类，一个形成本身作为另一个形成的条件（生作为生的条件）只能经由代理条件表示，这是表示所省略的关系（P14 更正：§18 以一类关系项读出这一关系）；每个取用者每步至少取用一个单位是前提，取用可以无限变小时，更多的取用者不需要更多的补充（论证，未形式化）。
- **持续的更多。** `More` 取的是持续的更多：从某步起一直至少那么多。只在个别步上任意多的情形，不受这一定理约束。
- **与 §13 的关系。** §13 中“每次上升都由形成的更新造成”是对应前提；在平衡的流中它是定理，前提移到了流本身：流须记录实际的取用与给予。`Garden` 的更新者凭空给予，与 `Bloom` 的太阳一样，是因为这一表示省略了它们自身的条件。若照实计入，它们也须被更新。原文接着写“更多的要求沿展开传递下去，没有一个有限的部分独自承担”；这需要耗散前提（每次给予都使补充者的条件付出多于所给），此处未陈述：在封闭循环中，补充者恰是取用者，家族的总量不变（`Cycle`，P11b 更正）。这与 §13 的 `dissipation_ceases` 是同一件事的两面。

**作者反审。**

*反驳 1：这只是平衡的恒等式。* `Balances.over` 与 `Balances.accumulates` 确是恒等式，由 `Balances` 的定义得出。新的是由它得出的必要条件：持续更多所需的补充与补充者没有最终的界，以及两个见证给出的严格分离。

*反驳 2：把“更多”读作取用者的数目太窄。* 是。更多种类、更复杂的结构、更多的可能性，都是“更多”的读法，这里都没有陈述。这里只读一种：更多的形成依赖同一组条件而活。

*反驳 3：`present` 中重复列出同一个形成会使计数失真。* 对。定理对列表条目成立；把条目读作形成，需要每步每个形成只列一次，这是应用义务，模块说明已写明。`Repeated`（P12b）表明这一前提是必要的。

*反驳 4：`Capacity` 是把结论写进前提。* 不是：没有 `Capacity`，`More.replenishment_unbounded` 仍然成立；`Capacity` 只把补充的无界转为补充者数目的无界。它是对应前提：一个形成的给予受它自身的大小与条件所限。

**边界。** 不含伦理谓词；不推出“更多更好”或任何排序；只读取用者的数目，不陈述多样性、复杂性与可能性；生成成分没有加入 living 的读法；见证都是最小见证；流与 `present` 的对应是应用义务。本节经第四次独立审查，更正见 §15。

## 15. 第四次独立审查与更正（P11b）

2026-10-09。按同一指示继续。另一 agent（Claude Opus 5.5，未参与撰写）独立审查了 P9b（§12）、P10（§13）与 P11（§14）（[审查](BECOMING-P9B-P10-P11-REVIEW.md)）。它在仓库之外从前导重新编译 17 个核心模块，公理报告为空；计数、回执、哈希与别名都对，数学接受。问题在定义、散文与对应之间，共十四项（H1–H14），附无公理的探针。审查没有发现替 Ren 选择 living 的读法；它指出两处来源问题（H7、H9），以及纯净核心中出现了 Ren 已纠正过的支付与账目用语（H13）。本节记录逐项处理。定义的修正都在核心上；探针的内容作为定理移入相应模块，公理报告为空。§6、§7、§12、§13 与 §14 中受影响的句子已就地更正并标明；原文见提交 `c48ec435`。

```text
Result(s): 修正 becoming-stepwise-reading（MetAbove）、becoming-return-grades、joint-difference-making（determined_dichotomy）、
           unceasing-generation-needs-renewal、more-needs-renewers、becoming-renewal-reading（一句）；
           新模块 Becoming.Population 的结果并入 more-needs-renewers；becoming-dependence-dynamics 只改计数；不新增结果记录
Delta: 侵蚀取最小形式（低于曾被满足的所需，也低于现在的所需）；Paid 改名 Depletes 并照实说明其内容；
       流的形式：取用的形成不息地生起需要补充复现；耗散前提写明，并对任意不上升的量陈述；
       在活跃形成的普查与 Taking 之下，不止地更多蕴含不息的生成，反之不然；补充的平均下界；
       补充者可以在无穷多步上为零；补充者可以就是取用者
Supplied premises / correspondence: 新增：耗散；每个取用者每步至少取用一个单位；Taking（只有活跃的形成取用，
       只从它汲取的条件取用）；活跃形成的普查（每步活跃的形成可列为有限且不重复的表，活跃可判定）；
       生起的形成在其第一个活跃步从家族取用（ArisesTaking）
Evidence: Becoming.Dependence 53、Joint 21、Generation 30、Flow 58、Population 20 项定理；
          合并检查器回执 20261009T042823.534750Z（376 项定理／688 项声明审计，核心闭包 18 个模块，公理报告全空）；
          外围桥接 20261009T042918.555373Z
Boundary: 新名称是审查的建议，最终由 Ren 定；第二个“生”与“更多”的范围、以消耗为条件的生起是否为生成，属于 Ren
Integration: H1–H14 全部处理；审查列出的会改变判断的结果中，第 1、2、4、5、7、8 项完成，第 3、6 项写为前提，第 9 项属于 Ren
```

### 15.1 逐项处理

| 项 | 审查所见 | 处理 |
|---|---|---|
| H1 | `MetSince` 在所需增长之后抹去曾被满足的水平：一次把水平压到曾被满足的旧所需之下的汲取既不断裂也不侵蚀（`Stunted`）。§12.4 把增长的选择说成没有代价 | 采用最小形式。`Web.MetAbove t g c m`：在依存不间断成立的某步 `s`，`s` 时的所需被满足，并且大于 `m`。`UnderminingOn` 要求汲取之后水平低于某个曾被满足的所需，也低于现在的所需；`UnderminingFor` 与关系层读法都经它。`Stunted.stunting_undermines` 成为定理：增长之后低于曾被满足的所需的汲取侵蚀，而不断裂。`NewNeed`、`FallingNeed`、`RisingNeed` 与 `Gap` 的结论不变，其余见证也不变。只低于增长到从未被满足的所需，仍不算侵蚀（`RisingNeed`）；这是公开的选择。`undermining_for_zero` 随之改为：零步内，对任何有依存者的条件的汲取都侵蚀。`MetSince` 改名为 `MetAbove`；§6、§7、§12、章节、术语表与记录随之更正 |
| H2 | 根模块说明把 `Determined` 写成定义的一部分；二分还需第三个条件 | 根模块说明改为“相对于扣除之后仍可取的动作，动作决定步骤时合乎其意”。`Joint` 说明加上：依存在扣除之后仍成立并被满足；扣除本身使依存落空时（那一部分是支持者），检验不作判断。`determined_dichotomy` 成为定理 |
| H3 | G8、G11 各留一处 | becoming-renewal-reading 的对应改为“每个形成都以正水平依存、由一个活的事件使用一次的被更新条件”；§8.5 两句改为“对 Ren 所采纳的问题的判决” |
| H4 | `Paid` 只说事件之步家族中有条件变化，与生起的形成无关（`Tide`）；正面见证 `Bloom` 只空洞地满足它 | 照实说明，并按 H13 改名为 `Depletes`：在事件的每一步，若家族中没有条件上升，则其中某个条件下降。`depletes_iff` 证明它恰说事件的每一步家族中有条件变化，与事件的关系不论。`Tide.unrelated_depletion` 与 `Bloom.arises_on_rise` 成为定理。§13 反驳 2 中“形成须从条件中取得”删去。把前提系于生起的形成，在流的形式中完成：`ArisesTaking`，即形成跨某步生起，并在其第一个活跃步从家族取用 |
| H5 | 严格性所引见证没有上升；P10 的更新是净上升，看不见同步的更新，`Garden` 不满足 `Paid` | 严格性改引 `Tide.renewal_without_arising`：潮水由月亮更新，在任意晚的步上升，而没有任何生起；`Commons` 改述为“依存保持，没有生起”。写明 `Rises` 是净上升，同步的补充看不见（`Garden.undepleted`）。流的形式成为定理：在平衡的流中，取用的形成在任意晚的步生起时，家族在任意晚的步得到补充（`replenishment_recurs`），补充者在任意晚的步出现（`renewing_recurs`）。`Garden.growers_take` 与 `Bloom.takes` 表明两者都满足这一前提 |
| H6 | “任何有限部分都不能独自不息”需要耗散前提：封闭循环的有限家族可以不息（`Recycle`） | `conserved_ceases` 改为 `dissipation_ceases`，对任意从不上升的量陈述：若每次生起都使它下降（耗散），生成不是不息的。写明三点：家族的总水平只在每次生起都使它下降时是这样的量，并预设各条件的单位可公度；物质循环不满足这一前提（`Recycle.closed_unceasing`）；对每次生起都耗散的量（例如自由能），前提是物理的，不是定理的推论。四处散文改写 |
| H7 | `Arises` 被称为“生生的第二个生”，`Growth` 被称为“以消耗进行的生成” | `Arises` 改述为“生起（变为活跃），生生第二个‘生’的一种读法的形式载体（作者的读法）”；“以消耗进行的生成”改为“以消耗为条件的生起”。记录写明：在继续的层面，这与 Ren 所说的生成与退化不重叠相合（作者的读法）；在单个事件的层面，`Arises` 包括以消耗为条件的生起。第二个“生”的范围留给 Ren |
| H8 | “严格的层级”作为蕴含不成立：不止地更多不蕴含不息（`more_without_arising`） | 两处都做。其一，新模块 `Becoming.Population` 证明 `Flow.More.unceasing`：在活跃形成的普查之下，流的 `present` 每步每个形成只列一次，只有活跃的形成取用（`Flow.Taking`），不止地更多就蕴含不息的生成。`Bloom.counted` 满足这些前提，不息而不更多，所以这一蕴含是严格的。前提各有作用：没有普查（`Dormant`）或没有 Taking（`Inactive`）时，不止地更多与“没有任何生起”同时成立。其二，散文改为：三者各自所需的补充构成严格的层级（任意晚、没有最终的界）；三者本身只在所述对应之下按蕴含排列 |
| H9 | `More` 数的是流中的取用者，不是活的或依存的形成（`more_without_living_takers`、`Crowd`） | 加对应前提 `Flow.Taking`：只有活跃的形成取用，并且只从它汲取的条件取用。其逆，即每个汲取者都在流中取用，是应用义务；`Crowd.drawing_without_taking` 表明它可以不成立。“更多的形成依赖同一组条件而活”改为“更多的形成从同一组条件取用”。Taking 之下，取用者是活跃的、汲取的形成；“活”是否读作 living 的某种读法，没有选定 |
| H10 | 每个取用者至少取一个单位，是未点明的前提 | 写入记录、§14 与章节：取用的量是自然数，所以每个取用者每步至少取用一个单位（取用有正的下限）。取用可以无限变小时，更多的取用者不需要更多的补充（论证，未形式化：核心只有自然数） |
| H11 | “给予者越来越多”强于定理（`Pulse`） | 两处都做。`Pulse.pulsed` 成为定理：补充者的数目没有最终的界，同时可以在无穷多步上为零。平均的形式也成为定理。`Balances.replenished_over`：在任意一段至少 K 个形成取用的步上，家族所得的补充每步至少 K，减去开始时的存量。`Balances.renewers_over`：每个形成给予有限时，补充者的数目在同一平均意义上增长。`More.replenishment_unbounded` 现在由前者推出。“越来越多”只在这一平均意义上保留 |
| H12 | “没有一个有限的部分独自承担”在封闭循环中不成立（`Cycle`） | 删去，并写明它需要耗散前提：每次给予都使给予者的条件付出多于所给。这一前提此处未陈述。`Cycle.closed_more` 成为定理：每个形成归还所取，总量不变，生成不止地更多，补充者恰是取用者。结构读法的边界加上“补充者可以就是取用者自身” |
| H13 | 纯净核心中出现 Ren 已纠正过的支付与账目用语 | 按审查的建议改名，名称最终由 Ren 定：`Paid`→`Depletes`，`paid_finitely`→`depletes_finitely`，支付前提→消耗前提，“生成不是无代价的”→“在没有补充之步，生起时家族中某个条件下降”，`ledger`→`Balances.over`（消耗与补充的平衡），`load`→`uptake`（取用），`supply`→`replenishment`（补充），给予者→补充者。`renewers` 与 `takers` 保留。包的 README 列出全部改名 |
| H14 | 形成与条件分为两类，省略了“生作为生的条件” | 写入结构读法的边界：在 `Web` 与 `Flow` 中形成与条件是两类，一个形成本身作为另一个形成的条件（生作为生的条件）只能经由代理条件表示。这是表示所省略的关系，不是反驳；P14 以一类关系项读出它（§18） |

### 15.2 新的已检查声明

| 模块 | 声明 | 内容 |
|---|---|---|
| Dependence | `Web.MetAbove`、`Web.MetAbove.now`；`UnderminingOn`（修正） | 依存在不间断成立的某步以那时的所需被满足，且那时的所需大于给定的水平；侵蚀即汲取之后水平低于某个这样的所需，也低于现在的所需 |
| Dependence | `Stunted.web`、`Stunted.stunting_undermines` | 所需从 1（被满足）增长到 2（从未被满足）；汲取把水平取到 0，不断裂，而侵蚀 |
| Return | `UnderminingFor`、`undermining_for_zero`（修正） | 周期读法经同一最小形式；零步内，对任何有依存者的条件的汲取都侵蚀 |
| Joint | `determined_dichotomy` | 动作决定步骤、在扣除后可取，依存在那里仍成立并被满足时：或者那一部分造成差别，或者同一动作仍断裂依存 |
| Generation | `Depletes`、`rises_or_still`、`depletes_iff`、`depletes_finitely`（改名） | 消耗前提及其内容：事件的每一步家族中有条件变化 |
| Generation | `dissipation_ceases` | 一个从不上升、每次生起都使它下降的量，使生成不是不息的 |
| Generation | `Tide.unrelated_depletion`、`Tide.renewal_without_arising` | 不依存、不汲取的闪现者不息地生起，每次都由无关的潮落满足消耗前提；没有闪现者时，潮水由月亮更新，在任意晚的步上升，没有任何生起 |
| Generation | `Recycle.closed_unceasing` | 一个单位在两个池之间循环，家族的总水平恒为一，全部前提成立，生成不息 |
| Generation | `Bloom.arises_on_rise` | 开花只在条件被恢复之时生起，即在上升之步 |
| Flow | `Taking`、`ArisesTaking` | 只有活跃的形成取用，且只从它汲取的条件取用；形成跨某步生起，并在其第一个活跃步从家族取用 |
| Flow | `replenishment_recurs`、`renewing_recurs` | 取用的形成在任意晚的步生起时，家族在任意晚的步得到补充，补充者在任意晚的步出现 |
| Flow | `Balances.replenished_over`、`Balances.renewers_over` | 补充与补充者数目的平均下界 |
| Flow | `Garden.growers_take`、`Garden.undepleted` | 花园满足 Taking 与流的形式的前提；它的水平从不上升，不满足净上升意义上的消耗前提 |
| Flow | `Bloom.takes` | 开花满足 Taking，并在其第一个活跃步取用 |
| Flow | `Cycle.closed_more` | 每个形成归还所取：总量不变，不息并且不止地更多，补充者恰是取用者 |
| Flow | `Pulse.pulsed` | 不止地更多，每个形成至多给予一单位，而在每个奇数步没有补充者 |
| Population | `Census`、`arises_of_more`、`unceasing_of_growth` | 每步活跃的形成列成不重复的表；活跃的形成变多时有形成生起；普查无界增长使生成不息 |
| Population | `Flow.More.unceasing` | 在普查之下，`present` 不重复、只有活跃的形成取用时，不止地更多蕴含不息的生成 |
| Population | `Bloom.counted`、`Dormant.more_without_arising`、`Inactive.more_without_arising`、`Crowd.drawing_without_taking` | 蕴含是严格的；没有普查或没有 Taking 时不成立；Taking 的逆可以不成立 |

### 15.3 审查列出的会改变判断的结果

1. 最小形式：完成（H1）。G1 关闭。
2. 把消耗系于生起的形成，或以流的形式重述 P10：以流的形式完成（`ArisesTaking`、`replenishment_recurs`），“不息的生成需要更新”覆盖 `Garden`（H4、H5）。
3. 耗散：前提写明，`dissipation_ceases` 对任意量陈述（H6、H12）。每次给予都使给予者付出多于所给的耗散流定理，开放。
4. 在普查对应下证明 `More → Unceasing`：完成（H8）。
5. Taking：完成（H9），其逆是应用义务。
6. 最小取用：写为前提（H10）。有理数量与下限的版本开放。
7. 平均的“越来越多”：完成（H11）。
8. 改名与 H14 的边界句：完成，名称最终由 Ren 定（H13、H14）。
9. Ren 对第二个“生”与“更多”的范围的选择，以及对以消耗为条件的生起是否为生成的原话：属于 Ren（H7、H9）。

### 15.4 作者反审

*反驳 1：最小形式又一次只是让定义合乎散文。* 它修正的是 P9b 未披露的代价。最小形式保留 P9b 的三个排除，并计入 `Stunted`。它仍是一个选择：只低于增长到从未被满足的所需，不算侵蚀（`RisingNeed`）。一个所需增长的幼体，在一次汲取后若仍不低于它曾被满足的所需，这次汲取不被扣下。这一选择是公开的。

*反驳 2：流的形式只是“取用为正，所以补充复现”，生起只是标出步。* （P12b 更正。原文写作“部分对”，并说 `ArisesTaking` 的内容正在于生起与取用的联系。）对：生起只经由它带来的取用起作用；`ArisesTaking` 把生起与取用连起来，使定理可以读作关于生成的定理，但定理所用的只是取用（`uptake_needs_replenishment`；恒定的取用者、没有任何生起，同样需要补充复现，`Steady`）。若不把取用系于生起的形成，生起只标出步，`Tide` 就是这样。它是对应前提，`Garden` 与 `Bloom` 满足它；一个不从家族取用的生起者，例如一个更新者，不受它约束。

*反驳 3：普查是强前提，实际展开中活跃的形成未必有限。* 对。`Dormant` 表明它的作用：没有普查时，一个从开始就活跃的无穷群体可以实现不止地更多而没有任何生起。普查读作：在所论的区域中，每步活跃的形成有限，并且能被列出。它是对应前提，不是定理的推论。

*反驳 4：把 `Paid` 改名为 `Depletes` 只是换词。* 换词依 Ren 对基础用语的纠正，而审查指出原名把一个普遍的正代价呈现为关于生成的事实。实质的部分是：`depletes_iff` 照实说出前提的内容；系于生起形成的版本在流的形式中。

*反驳 5：既然更多在对应之下蕴含不息，为什么还说“三者各自所需的补充构成层级”，而不直接说“三者构成蕴含的层级”？* 因为两个蕴含的前提不同。更多蕴含不息，需要普查与 Taking。不息蕴含补充复现，需要 `ArisesTaking`。复现的更新不蕴含不息（`Tide`）。没有一组前提把三者同时排成一条链，所以只在所述对应之下说蕴含。

**边界。** 不改变读法选择的地位；不推出责任、义务或任何排序；新名称是建议；探针与新见证都是最小见证。本节的更正经第五次独立审查，见 §19。


## 16. 跨步的同一：改名、改认与接续（P12）

2026-10-09。开放纲领“动态依存”一行把形成的个体化列为下一步；`Becoming.Dependence` 的说明也写明，形成跨步的同一由索引类型 `F` 规定，一个形成转化还是一个终结而另一个形成，取决于这一规定。本节证明这一规定在哪些读法中起作用，在哪些读法中不起作用，以及活动与依存的连续能把它确定到什么程度。成果记录：[identity-across-steps](../../../../theories/becoming/results/records/identity-across-steps.md)。

依存网用固定的索引类型给形成命名，所以一步的哪个形成与下一步的哪个形成相同，是由名字规定的；每一步的关系并不确定它。**改认**（`Reidentify`）在每一步把两种命名一一对应。改认之后的网在每一步有相同的水平、活动、依存与汲取，不同的只是哪一步的哪个形成延续前一步的哪个。每一步都相同的改认是**改名**。分裂与合并（一个形成延续为几个，或几个延续为一个）不是改认：它们改变延续关系，不改变任何一步形成的数目（P12b 更正；原文写作“分裂与合并改变形成的数目”）。§19 以延续关系表示它们。

```text
Result(s): 复用 becoming-dependence-dynamics（依存网、支持、保持、断裂、任期、侵蚀、形成与消解）、
           unceasing-generation-needs-renewal（生起、不息、Depletes）、more-needs-renewers（流、取用者、更多、普查与 Taking）；
           新增 identity-across-steps（L3）
Delta: 改名保持追随形成的读法（P12b 更正：检查了五种，原文作“全部读法”）；任何改认保持每一步的关系、每个条件的类、Dependent、每个事件是否在更新之内与是否断裂，
       以及流的取用与给予、取用者与补充者的数目、“更多”、活跃形成的普查与 Taking，所以在普查之下，更多在每个改认下蕴含不息；
       只改动谁延续谁，形成的类、侵蚀、转化与生起都改变；
       保持持续活动的改认不制造生起，保持持续依存的改认不去掉侵蚀；它们仍可把终结者与开始者接起来（接续），接续可以隐藏生起、增加侵蚀
Supplied premises / correspondence: 改认在每一步一一对应；连续读作活动与依存跨步持续时名字不变；
       接续怎样读不由本节给出
Evidence: Becoming.Identity 的定理；合并检查器回执（见记录）
Boundary: 不含伦理谓词；不处理分裂与合并；连续是一种同一的读法，不是同一的定义
Integration: 开放纲领“形成的个体化”部分承接；逐步读法与不息的边界由此陈述
```

[Becoming.Identity](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Identity.lean)（L3）：

| 声明 | 内容 |
|---|---|
| `Reidentify`、`Reidentify.rename`、`Web.reidentify`、`Flow.reidentify` | 两种命名在每一步一一对应；改名在每一步相同；改认后的依存网与流 |
| `reidentify_step`、`reidentify_renewed`、`reidentify_consumed`、`reidentify_lost`、`reidentify_dependent`、`reidentify_renewingAt`、`reidentify_breakingOn` | 任何改认都保持：每一步的支持、保持与断裂；每个条件的类（被更新、被消耗、失去）；活动是否需要支持；每个事件是否在更新之内、是否断裂 |
| `reidentify_amounts`、`reidentify_balances`、`reidentify_counts`、`reidentify_more` | 改认一个流，保持每步的取用与给予、消耗与补充的平衡、取用者与补充者的数目，因而保持不止地更多 |
| `Reidentify.new_injective`、`Reidentify.mem_map`、`mem_map_of`、`mem_of_map`、`distinct_map`、`Web.Census.reidentify`、`Flow.Taking.reidentify` | 改认保持活跃形成的普查（每步不重复地列出）与“只有活跃的形成取用，且只从它汲取的条件取用” |
| `Flow.More.unceasing_reidentified` | 在普查、present 不重复与 Taking 之下，不止地更多在每个改认下蕴含不息 |
| `rename_renewingIn`、`rename_consumingIn`、`rename_tenure`、`rename_undermining`、`rename_unceasing` | 标签不承载任何东西（P12b 更正，原文作“名字”）：改名保持形成的类、依存的任期（`MetAbove`）、侵蚀、形成与消解、生起与不息 |
| `Turnover.identified`、`Turnover.reidentified` | 每一奇数步交换名字，每一步的关系不变：一个形成更新、一个消耗，变成没有形成更新、两个消耗；汲取者在每一步侵蚀，变成第一步之后没有任何事件侵蚀；没有依存形成或消解、没有生起，变成一个形成跨第一步转化依存、每一奇数步都有形成生起，生成不息。这些生起不降低任何条件，`Depletes` 不成立。两个网中活动都只在有支持处 |
| `KeepsActive`、`KeepsTenure`、`Reidentify.steady` | 改认保持跨一步持续活动的形成的名字；保持跨一步持续依存于某条件的形成的名字。后者使一个形成在一段任期上只有一个名字 |
| `arises_of_keepsActive`、`unceasing_of_keepsActive` | 保持持续的活动，改认不制造生起：新名字下生起的，在旧名字下也生起；因而不制造不息 |
| `metAbove_of_keepsTenure`、`undermining_of_keepsTenure` | 保持持续的依存，改认保持在任期中满足过的依存，不去掉任何侵蚀 |
| `Lineage.readings` | 一个谱系的两个成员在交替的步活跃。分开命名，成员不息地生起；作为一个命名，谱系始终活跃，没有生起。合为一个命名保持持续的活动，因为没有成员在相继两步都活跃 |
| `Succession.readings` | （P12b 更正：原见证的继承者从不活跃，从第二步起需要池而从未被满足。）长者在第一步需要池；继承者在第二步活跃并以一单位被满足，自第三步起需要两单位，活动需要支持。分开命名，汲取者只在第一步侵蚀（断裂长者的依存）；继承者接续长者时，长者的任期在继承者中延续，汲取者自第三步起每一步都侵蚀。接续保持持续的活动与依存 |

**解读。**

- **标签不承载任何东西；名字跨步的模式承载同一。** （P12b 更正。原文写作“名字不承载本体。改名保持全部这些读法……这是方法要求‘不能以分别命名偷渡独立本体’在这一表示中的一个检查”。）改名保持由关系定义的这些读法（检查了五种）：标签的选择不起作用。名字跨步的模式承载同一：这是表示给出的对应前提，`Turnover` 表明它是实质的。方法要求“不能以分别命名偷渡独立本体”在这里的检查是这一披露，不是改名不变，因为改名按构造保持这一模式。
- **每一步与每个条件只由关系确定。** 支持、保持与断裂、条件的类、每个事件是否在更新之内，都只依赖每一步的关系，不依赖跨步的同一。消耗读的是一个依存在它成立时的样子，对照条件以后的水平；它不追随形成。“更多”读的是每步取用者的数目，也不依赖。在普查与 Taking 之下，它所迫使的不息在每种一对一的同一读法下也不依赖（`More.unceasing_reidentified`）：不息本身依赖同一（`Turnover`、`Lineage`），由“更多”迫使的不息却不依赖一一对应的命名。原因在 `arises_of_more`：下一步活跃的形成多于这一步时，无论怎样一一对应地命名，总有一个名字在这一步不活跃而在下一步活跃，数目的增长不能由改认吸收。（P12b 补充：在把新形成读作从既有形成萌出的读法下，数目的增长由分裂吸收；没有分裂时它仍迫使生起，见 §19。）
- **追随形成的读法依赖同一。** 形成在整段上的类、依存的任期（因而侵蚀与逐步读法的 `living`）、转化与“一个终结而另一个形成”的区别、生起（因而不息），都依赖跨步的同一。`Turnover` 只改动谁延续谁，这些就全部改变。所以 §5 中“分类属于运行，不属于形成自身的轨迹”还要补一句：形成的类还依赖哪些事件属于同一个形成。
- **连续排除什么，留下什么。** 把同一读作活动与依存的连续：跨一步持续活动的形成保持名字，跨一步持续依存的形成保持名字。这样的改认不制造生起，也不去掉侵蚀。它仍可以把在某步终结的形成与在该步或其后开始的形成接起来：开始者是否延续终结者，是接续的问题。接起来可以隐藏生起（`Lineage`），也可以增加侵蚀（`Succession`）。（P12b 更正。原文写作“两个定理各有一个方向，反方向的反例恰是接续”。）两个条件以旧命名为参照，是单向的：新命名可以制造连续（接起来），不能去掉连续（`Lineage.one_way`、`Succession.one_way`）。两向保持连续时，生起与侵蚀恰被保持；接续开放，是因为连续取单向的读法。两向保持连续，跨过休眠之步的接续仍改变形成的类（`Dormancy`）：连续不约束形成在整段上的类。
- **对生生的意义（AI 论证）。** （P12b 更正。原文把谱系的持续与成员的生起写成二选一，并说读作谱系的持续时“落在维持与更新上”；`Lineage` 没有任何条件，后一句没有见证。）谱系与成员是同一展开的两个层次：作为整体的谱系持续，正由成员不息地生起而成（`Layered`）；单一命名层次只能表示其一，部分与整体的关系是这一表示所省略的关系。把“生生不息”读到谱系、成员或两者的层次，不由每一步的关系决定；只读作谱系的持续，与 Ren 原话中的“不断创造”有张力。继承者是否继承长者的损失，决定此后的汲取是否侵蚀；这触及工作读法“不侵蚀”的一个选择：一个依存的任期能否经由接续延续。这两个选择属于 Ren。
- **对 P10 的影响。** `Unceasing` 依赖同一；在 `Turnover` 中，改认单独制造了不息。§13 的 `Unceasing.rises` 不受影响：它的结论（家族中某个条件在任意晚的步上升）只关乎条件，不依赖同一；（P12b 更正。原文另给第二个理由：`Turnover` 中单由改认制造的生起不降低任何条件，`Depletes` 不成立，定理不适用。那只是 `Turnover` 的性质。）`Depletes` 不系于生起的形成，不筛掉命名的产物：单由命名造成的生起可以满足全部前提（`TideFlip`）。定理不受影响，是因为结论只关乎条件；它的前提 `Unceasing` 依赖同一，要把它读作关于生成的定理，需要命名保持持续的活动（`arises_of_keepsActive`）。

**作者反审。**

*反驳 1：改名不变是平凡的。* 对按关系定义的谓词，改名不变是一条元定理：可定义的性质在同构下不变。这里在 Lean 中逐项检查，并与改认对照；值得注意的是改认改变什么、不改变什么。

*反驳 2：`Turnover` 的改认是荒谬的，没有人会这样认同。* 对：它破坏了活动与依存的连续。它只表明每一步的关系不决定同一。连续的定理说明，排除这类改认后剩下的是接续，包括跨过休眠的接续（P12b 更正；原文作“剩下的只有接续”）；而 `Lineage` 与 `Succession` 中的接续不荒谬：谱系、继承者、同一生态位上的接替都是实际的情形。

*反驳 3：改认要求每一步的形成一一对应，排除了分裂与合并。* 对。（P12b 更正。原文写作“分裂与合并改变形成的数目”。）分裂与合并不改变任何一步形成的数目，改变的是延续关系；本节只处理一一对应的延续，§19 以延续关系表示分裂与合并。

*反驳 4：把同一读作连续，是否预设了同一？* 连续在这里只用到每一步的关系与名字：一个形成在相继两步都活跃，或都依存于某条件。它不定义同一，只约束改认：在约束之下，改认不再能制造生起或去掉侵蚀，接续仍由读法决定。

*反驳 5：普查下的结论是不是只把同一换成了计数？* 是，这正是它的内容：“更多”只读每步的数目，普查把数目的增长与生起连起来。它不说哪个形成生起，只说总有某个形成生起；在 `Lineage` 那样数目不增长的展开中，它什么也不说。

**边界。** 不含伦理谓词；改认只处理每步形成一一对应的情形；连续是作者提出的一种同一的读法，不是同一的定义；接续怎样读、工作读法“不侵蚀”是否让任期经由接续延续，属于 Ren 的读法选择；从关系推出同一的完整说明（例如物质、信息或组织的连续）没有给出。本节经第五次独立审查，更正见 §19。

## 17. 耗散：复现的取用打开有限家族（P13）

（P16c 更正标题，原题“耗散：没有有限部分独自承担持续的取用”；见 §23 K1。）

2026-10-09。按同一指示继续。§14 的 `Cycle` 表明补充者可以就是取用者：封闭循环中每个形成归还所取，生成不止地更多。第四次独立审查（H6、H12）指出，“任何有限部分都不能独自不息”与“没有一个有限的部分独自承担”需要耗散前提；§15 把它们标为未陈述的前提。本节在流上陈述耗散，并证明它承担什么。成果记录：[no-finite-part-bears-taking](../../../../theories/becoming/results/records/no-finite-part-bears-taking.md)。

```text
Result(s): 复用 more-needs-renewers（流、平衡、取用者、补充、More、ArisesTaking、Cycle、Distinct）、
           becoming-renewal-reading（falls_finitely）、becoming-finite-horizon（le_of_add_le_add_right，只作算术）；
           新增 no-finite-part-bears-taking（L3）
Delta: 封闭（ClosedAt）与耗散（DissipatesOn、Dissipative）；平衡的流中，被耗散的家族跨一步至少下降其取用者的数目（runs_down），
       从某步起被耗散，此后取用者的总数不超过当时的存量（takers_within），取用不再复现（taking_ceases）；
       在耗散之下，取用在任意晚的步复现的有限家族，连同包含它的每个不重复的有限家族，在任意晚的步都不封闭（Dissipative.opens）；
       不止地更多与取用者的不息生起都是这样的取用（More.opens、opens_of_arising）；条件总共有限时，取用不再复现（finite_ceases）；
       Frontier 满足全部前提并且不止地更多
Supplied premises / correspondence: 流平衡依存网；耗散：每一步，每个在该步封闭的不重复家族上，每个参与的形成给予家族的不多于从家族所取，
       取用时更少；量是自然数，单位可公度；耗散是物理前提，不是定理
Evidence: Becoming.Dissipation 的定理；合并检查器回执（见记录）
Boundary: 只约束流中的取用，不约束不取用的生起（Tide 的闪现者）；“有限部分”指有限的条件家族，不是有限的形成集合；不含伦理谓词
Integration: 陈述第四次审查 H6、H12 所要求的前提；§13 的 dissipation_ceases 在依存网上陈述耗散，本节在流上陈述
```

[Becoming.Dissipation](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Dissipation.lean)（L3）：

| 声明 | 内容 |
|---|---|
| `Flow.ClosedAt`、`Flow.DissipatesOn`、`Flow.Dissipative` | 封闭：一步中没有参与的形成与家族之外的条件交换。耗散于家族：每个参与的形成给予家族的不多于从中所取，取用时更少。耗散的流：每一步，每个在该步封闭的不重复家族都被耗散 |
| `DissipatesOn.replenishment_takers`、`Balances.runs_down` | 被耗散时，家族的补充加取用者的数目不超过其取用；平衡的流中，家族跨一步至少下降其取用者的数目 |
| `Balances.takers_within`、`Balances.taking_ceases` | 从某步起被耗散，此后任一段步上取用者的总数不超过当时的存量；从家族的取用不再复现 |
| `takers_pos_of_sub` | 从一个家族取用的形成，也从包含它的每个家族取用 |
| `Dissipative.opens`、`More.takers_recur`、`takers_recur_of_arising`、`More.opens`、`opens_of_arising` | 在耗散之下，取用在任意晚的步复现的有限家族，连同包含它的每个不重复的有限家族，在任意晚的步都有参与的形成与其外的条件交换。不止地更多，以及在第一个活跃步取用的形成的不息生起，都是这样的取用 |
| `Dissipative.finite_ceases` | 若有限个条件就是全部，在耗散之下，从任何家族的取用都不再复现 |
| `Frontier.balances`、`Frontier.dissipative`、`Frontier.more`、`Frontier.frontier` | 太阳每步燃烧一份新的燃料，给池的少于所燃，越来越多的生长者从池取用：流平衡、耗散、不止地更多。所以包含池的每个有限家族在任意晚的步都不封闭，太阳所燃的燃料不在任何有限家族之内 |
| `pos_of_sign`、`sign_pos`、`eq_zero_of_not_pos`、`le_total_of_mem`、`total_eq_zero`、`total_le_at` | 有限和的辅助引理 |

**解读。**

- **耗散把要求传到每个有限部分之外。** 没有耗散，一个有限家族可以封闭地维持不止地更多（`Cycle`）。有耗散，任何有限家族，若取用在其上复现，都在任意晚的步与其外交换，包含它的每个有限家族也如此。这一交换可以与家族无关（`SprayHanding`）；家族从某步起被围住时，它汲入：在任意晚的步，有形成给予它而从其外取用（`taking_draws_in`）（P16c 更正，原文“所以持续的取用不由任何有限的条件家族承担”）。这把 §13 与 §14 中作者的论证“在耗散之下，任何有限部分都不能独自不息”变为定理，范围是流中的取用。
- **定量的界。** 被耗散的家族上，此后全部的取用事件不超过当时的存量（`takers_within`）：存量是取用能持续多久的上界。
- **物质可以循环，驱动循环的不能（AI 论证）。** 用自由能读耗散：物质在一个有限家族中可以封闭地循环（`Cycle`），驱动循环的自由能若被耗散，就需要越出每个有限家族的来源。`Frontier` 中太阳每步烧一份新燃料，表示一个没有尽头的来源；实际的来源是否如此，是经验问题。若有限个条件就是全部，取用终将停止（`finite_ceases`）。
- **与 §13 的关系。** `dissipation_ceases` 陈述在依存网上：一个量从不上升而每次生起都使它下降，生成就不是不息的。本节陈述在流上：耗散在每个封闭家族上成立，于是取用不再复现，除非与家族之外交换。两者都需要耗散前提；没有它，封闭循环可以不息并且更多。
- **对生生（作者的读法）。** Ren 的原话是“生生不息 - 一种整体的，不断创造更多生的方向”。在耗散之下，复现的取用，无论来自不止的更多、生成还是维持，使它复现的有限条件家族在任意晚的步不封闭，家族被围住时须从其外汲入：维持一个恒定的取用者已经如此（`Lone`，`Lone.draws_in`）（P16c 更正，原文“都不能由任何有限的条件家族独自承担，只能由越出每个有限部分的展开承担”；耗散空成立时，家族可以独自承担取用，见 §23 K1）。作者把这读作原话中“整体”的一种形式内容；不断的更多是其中的一种情形，不是它的全部内容（P16b 更正，原文只说不断的更多）。这是作者的诠释，不替代 Ren 的原话，也不推出它是好的。

**作者反审。**

*反驳 1：`Dissipative` 太强，排除了任何“免费”的补充者。* 只在有封闭的有限家族的步上如此（P16b 更正；原文“对，这正是前提的内容：补充者的代价须表示为它所取的条件”）。`Dissipative` 只约束在某步封闭的不重复家族；某个形成在一步中与无穷多个条件交换时，没有家族封闭，耗散对那一步什么也不说，补充者可以什么都不取而给予（`Spray`）。在有封闭的有限家族的步上（`Enclosed`；条件总共有限时每步都是），给予的形成在封闭家族上取得多于所给（`gives_less`），给予须以取用为条件（`giving_needs_uptake`）：太阳的燃料、植物所取的光都要作为条件出现。§14 的 `Garden` 与 `Bloom` 省略了来源，不满足 `Dissipative`（`witnesses_not_dissipative`，连同 `Cycle`、`Pulse`、`Steady` 与 `Repeated`）；那是表示所省略的关系，不是没有关系。另一方面，结论“在任意晚的步不封闭”可以由与家族无关的交换满足（`Spray` 的汇）。

*反驳 2：耗散只对某些量成立，例如自由能，对信息或组织不一定成立。* 对。本节只说：对满足耗散的量，持续的取用需要越出每个有限家族。信息的复制、组织的维持是否耗散，是对应问题；`Cycle` 表明不耗散的量可以封闭地循环。

*反驳 3：结论只约束取用，不约束生起。* 对。不取用的生起（`Tide` 的闪现者）不受约束；`opens_of_arising` 只说在第一个活跃步取用的形成的不息生起。（P15 补充：生起的关系项体现时，它的生起本身就是补充，在耗散之下同样使它复现的有限家族不封闭，家族被围住时汲入，见 §20；P16c 更正，原文“同样须与有限家族之外交换”。）（P16b 补充：`Frontier` 的生长者不依存于任何东西；`Rooted` 让它们以需要一依存于池，普查、`Dependent` 与不息同时成立，是 `opens_of_arising` 的见证。）

*反驳 4：“没有有限部分”是否等于需要无穷多条件？* 在形式上是：`Frontier` 用无穷多燃料，`finite_ceases` 说条件总共有限时取用不再复现。若实际的展开在这一意义上是有限的，定理说取用终将停止。把它与物理的热寂相比，是作者的类比，不是物理定律的证明。

*反驳 5：为什么要求家族不重复？* 列表重复同一条件时，量被重复计数，耗散可以被虚假地违反；`Dissipative` 只对不重复的家族陈述，`Frontier` 对每个这样的家族都证明了它。

**边界。** 不含伦理谓词；耗散是物理前提，单位可公度，只约束有封闭的有限家族的步（`Enclosed`，P16b 补充）；结论只约束流中的取用；“有限部分”指有限条件家族；表示中形成与条件仍是两类（§15，H14；一类关系项的读法见 §18，耗散之下见 §20）；`Frontier` 是最小见证。本节经第六次独立审查，更正见 §22。

## 18. 角色：生作为生的条件与经由给予的生起（P14）

2026-10-09。按同一指示继续。§1 写明“形成”和“条件”是同一展开中的分析角色，不是彼此独立的实体，但 `Web` 与 `Flow` 把它们表示为两个类型。第四次独立审查（H14）指出，这省略了“生作为生的条件”：父母之于后代、森林之于林下、群落之于学习者，只能经由代理条件表示；§15 把它写为表示所省略的关系。按非二元方法（先说明同一展开中的关系怎样形成、持续和改变，再说明行动者与承受者怎样在其中分化），本节把形成与条件读作一个关系项的两种角色，并证明这一读法承担什么。成果记录：[life-as-condition-of-life](../../../../theories/becoming/results/records/life-as-condition-of-life.md)。

```text
Result(s): 复用 becoming-dependence-dynamics（Web、支持、Dependent、更新、消耗、断裂、侵蚀、renewing_at_active）、
           unceasing-generation-needs-renewal（Arises、Unceasing、RenewedBy）、
           more-needs-renewers（流、平衡、Acting、取用者、补充者、More、Balances.renewedBy）、
           condition-correspondence-discipline（Interacts、interaction）、metaethical-core-characterization（Valuation、significant_iff）；
           新增 life-as-condition-of-life（L3 Becoming.Roles；L4 Becoming.Correspondence 新增一节）
Delta: 一类关系项的读法（Web.roles、Flow.roles）保持列出的全部读法与两种估值的连通，其中曾活跃的形成既不体现也不承担自身；
       体现（Embodied）与承担自身（SelfBearing）；在 Dependent 之下，依存于体现关系项的形成只在它活跃时活跃（active_of_bearing），
       活动沿依存链传递（active_along），不活跃的关系项终结每个依存链到达它的形成（coextinct）；
       在需要为一时消耗体现的关系项即终结它（ends_when_consumed）；在承担自身的体现关系项终结之步汲取它是断裂（ending_breaks）；
       在平衡且只有活跃形成给予的流中，体现的关系项只经由另一个活跃形成的给予而生起（arises_given）；
       汲取承担自身的关系项与它的每个活跃事件相互作用（SelfBearing.interacts）；Mutualism、Predation、Brood
Supplied premises / correspondence: Embodied、SelfBearing 与 Dependent 是对具体关系项的表示前提；arises_given 需要平衡与 Acting；
       估值的结果用逐步读法的 living 与公开的相互作用纪律
Evidence: Becoming.Roles 的 54 项定理与 Becoming.Correspondence 新增的 9 项定理；合并检查器回执（见记录）
Boundary: 遗骸与不活跃的条件不体现；一类读法不保持 Acting、Taking 与 Dissipative 的陈述（P16b 更正：不成立，它们也保持，见 §22）；
          Brood 只给予不取用；不含伦理谓词
Integration: 回答第四次审查 H14；§14、§15 与 §17 中“形成与条件是两类”的边界改为指向本节
```

[Becoming.Roles](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Roles.lean)（L3）与 [Becoming.Correspondence](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Correspondence.lean) 新增的一节（L4）：

| 声明 | 内容 |
|---|---|
| `Web.roles`、`Flow.roles` | 以一类关系项读出的依存网与流：一个形成在零水平上作为条件，没有谁依存、汲取、从它取用或向它给予；一个条件从不活跃，不依存、不汲取、不取用也不给予 |
| `roles_supported`、`roles_dependent`、`roles_renewed`、`roles_renewed_formation`、`roles_consumed`、`roles_renewingIn`、`roles_consumingIn`、`roles_undermining`、`roles_arises`、`roles_unceasing`、`roles_alive` | 一类读法保持支持、`Dependent`、条件的更新与消耗、形成的类、侵蚀、生起、不息与逐步读法的 living；作为条件的形成没有谁依存，所以被更新 |
| `roles_taken`、`roles_given`、`roles_taken_formation`、`roles_given_formation`、`roles_balances`、`roles_takers`、`roles_renewers`、`roles_more` | 流的一类读法保持取用与给予、平衡、家族的取用者与补充者，以及不止地更多 |
| `roles_event_injective`、`roles_event_onto`、`Valuation.connected_iff_of_map`、`roles_valuation_connected`、`roles_interaction_connected` | 形成的事件与一类读法中活的事件一一对应；共同参与与相互作用两种估值的连通都不变（后三项在 L4） |
| `Embodied`、`SelfBearing`、`SelfBearing.stands`、`roles_not_embodied`、`roles_not_selfBearing` | 体现：恰在活跃时以正的水平作为条件而在。承担自身：活跃时以正的需要依存于自身的水平；在 `Dependent` 之下，于是活跃时作为条件而在。两类读法中，曾活跃的形成既不体现也不承担自身 |
| `Embodied.active_of_bearing`、`bearing`、`active_along`、`coextinct` | 生作为生的条件：在 `Dependent` 之下，以正需要依存于体现关系项的形成只在它活跃时活跃；活动沿这样的依存链传递；一个在某步不活跃的关系项在该步终结每个依存链到达它的形成 |
| `Embodied.ends_when_consumed`、`Embodied.ending_breaks` | 在需要为一时消耗体现的关系项即终结它；在承担自身的体现关系项终结之步汲取它，断裂它自身的依存，不论是否另有形成依存于它，也不论是什么终结了它（P16b 补充，`Wilting`） |
| `Embodied.arises_given` | 经由另一个活跃者的给予而生起：在平衡且只有活跃形成给予的流中，体现的关系项只经由另一个活跃形成的给予而生起；给予它的形成不必体现（P16b 更正，原文“生由生给予”；`SunSeed`；P16c 用语，原文“给予者”） |
| `SelfBearing.interacts` | 汲取承担自身的关系项，与它的每个活跃事件相互作用（L4） |
| `Mutualism.web`、`dependent`、`embodied`、`selfBearing`、`renewing`、`alive`、`connected`、`significant_iff` | 蜜蜂与花各自依存于自身与对方，并汲取对方：彼此更新，每个事件都是 living；没有第三个条件，相互作用读法连通，G0 在那里恰为种子加两项中立 |
| `Mutualism.apart`、`apart_renewing`、`apart_alive`、`apart_not_selfBearing`、`apart_participates`、`apart_not_connected`、`apart_not_interacting` | 各自只依存于对方时，都不承担自身；共同参与与相互作用都不把蜜蜂与花关联起来 |
| `Predation.web`、`breaking`、`hare_ends`、`fox_ends` | 狐依存于自身与兔并汲取兔，兔与自身相依；兔跨第二步终结：狐在兔终结之步的汲取断裂兔自身的依存，所以不是 living（P16b 更正，原文“兔跨第二步被吃”；兔的终结是给定的时程，见证中没有流）；狐随兔一同终结（共灭） |
| `Brood.flow`、`Brood.web`、`Brood.arises`、`Brood.brood` | 一代代形成不止地生起，每一代由前一代给予：流平衡，只有活跃的世代给予，每代体现并承担自身，`Dependent`，生成不息 |
| `total_map`、`total_congr`、`Mutualism.other_cancel`、`Mutualism.other_ne`、`Predation.uneaten_late`、`Brood.grows`、`Brood.standing_self`、`Brood.standing_before` | 有限和与见证的辅助引理 |

**解读。**

- **两类嵌入一类（P16b 更正）。** 以两类陈述的列出的读法，以一类关系项读时都不变，两种估值的连通也不变（`roles_*`）；`Acting`、`Taking`、普查、present 不重复与耗散也不变（`roles_acting`、`roles_taking`、`roles_census`、`roles_distinct`、`roles_dissipative`）。两类读法中曾活跃的形成既不体现也不承担自身（`roles_not_embodied`、`roles_not_selfBearing`）。一类读法另需一个对应：哪个条件就是哪个形成。它由共同的索引给出，是表示的前提，两类读法检查不到它：把条件一侧到上地重新标号，`Dependent`、侵蚀、living 与两种估值的连通都不变，而体现与承担自身改变（`relabel_dependent`、`relabel_undermining`、`relabel_alive`、`relabel_valuation_connected`、`relabel_interaction_connected`、`Mutualism.apart_relabelled`、`Wilting.relabelled_not_embodied`）。体现与承担自身是在这一对应下的读法；两类的表示省略的是形成与条件的同一对应。原文写“所以两类的表示没有引入独立的本体”“它省略的正是体现”，把所给的对应当作了结果，与 §19 的 I7 是同一模式。
- **生作为生的条件。** 在活动需要支持（`Dependent`）之下，依存于体现关系项的形成只在它活跃时活跃，活动沿依存链传递，一个关系项的终结终结每个依存链到达它的形成（`coextinct`）。在生态中，这是专食者与宿主、寄生者与寄主的共灭；种子库、储备与休眠被 `Dependent` 排除，在它们之下共灭不必成立（P17 补充：`Dependent` 是零储备，有储备时共灭推迟而不消失，见 §24）。
- **经由另一个活跃者的给予而生起（P16b 更正，原题“生由生给予”）。** 在平衡且只有活跃形成给予的流中，体现的关系项只经由另一个活跃形成的给予而生起（`arises_given`）。定理不要求给予它的形成体现、承担自身或依存于任何东西：一个不体现、不依存的太阳可以是唯一给予种子的关系项（`SunSeed`）（P16c 用语，原文“给予者”）。所以它说的是一个体现关系项的生起由另一个活跃者的给予给出，不是由另一个体现关系项给出（P18b 用语，原文“一个生命的生起”“另一个生命”）。在只有体现的关系项给予这一表示前提下，给予它的关系项也体现，并在给予时作为条件而在（`arises_from_embodied`；P18b 用语，原文“给予者”）；这是对应，不是定理从平衡推出的。作者曾把“生由生给予”读作 Ren 原话“不断创造更多生”中两个“生”之间关系的一种形式内容（AI 论证）；这一读法需要上述前提，不替代原话，也不推出它是好的。`Brood` 表明前提与不息相容：一代代形成生起，每一代由前一代给予。
- **直接的关系。** 共同参与与相互作用都经由一个条件关联两个事件。各自只依存于对方的互利者，没有共同的条件，于是两种估值都不关联它们（`apart_not_connected`、`apart_not_interacting`）。承担自身时，一个形成对另一个的汲取就与那个形成的活动相互作用（`SelfBearing.interacts`），互利者直接相关，无需第三个条件（`Mutualism.connected`）。所以形成之间是否直接相关，取决于是否表示一个形成承担自身。体现本身不进入两种估值（P16b 补充）：估值只经由共同的条件关联事件；`apart` 中两者都体现、各自依存并汲取对方，仍不相关（`Mutualism.apart_embodied`）。只有承担自身把体现的关系项的活动接到汲取它的事件上；这是估值所省略的关系。一个把汲取者与它所汲取的体现关系项的事件直接关联的估值，是新的结果（P18 补充：以之为生与世系两种候选读法，见 §25）。
- **在一个体现关系项终结之步汲取它（P16b 更正，原题“终结另一个生命”；P18b 用语，原题“在一个生命终结之步汲取它”，本段的“生命”下同）。** 在一个承担自身的体现关系项终结之步汲取它，不论是什么终结了它，是断裂，所以不是 living（`ending_breaks`）；没有谁依存于它时也如此（`Predation` 中兔自身的依存）。这包括旁观的汲取者、自然的终结与该关系项自身的最后事件：花因自身的取用而凋，从不取用的蜜蜂在那一步的汲取，与花自己的最后一个事件，都是断裂（`Wilting`）。在 `Dependent` 与体现之下，自身依存恰在活跃时被满足（`SelfBearing.met_iff`）：它不记录活动之外的任何东西，作用是把终结读作断裂。定理不说汲取终结了它；因果的读法需要反事实的关系（例如 §8 `Joint` 的 but-for 检验），这里没有陈述。若被汲取者不承担自身、也没有谁依存于它，这样的汲取不侵蚀任何东西。是否把在终结之步的汲取计入不 living，以及对哪些汲取者（捕食者、旁观者、该关系项自身），属于 Ren 对生生的读法；本节只陈述两种表示各自的后果。

**作者反审。**

*反驳 1：`Embodied` 太强：遗骸、种子库与休眠的形成在活动之外仍作为条件。* 对。`Embodied` 是对具体关系项的前提，不是对所有关系项；遗骸可以表示为另一个关系项，它与原形成的关系是跨步同一的问题（§16）。

*反驳 2：`SelfBearing` 是否把想要的结论编进表示？* 它只说一个形成活跃时依存于自身的水平；与 `Dependent` 一起，这就是 `Embodied` 的一半（`SelfBearing.stands`）。它使在一个承担自身的体现关系项终结之步的汲取成为断裂（P16b 补充：不论是什么终结了它；P18b 用语，原文“在一个生命终结之步”），这是读法的后果，不是伦理前提；`Mutualism.apart` 与 `Predation` 并列陈述有与没有它的后果，是否采用属于 Ren。

*反驳 3：一类读法的嵌入是平凡的。* 嵌入本身是定义；它的内容是两类读法的每个列出的结果在一类读法中成立。一类读法另加的是形成与条件的同一对应，它由共同的索引给出，两类读法检查不到它（`relabel`），不是嵌入推出的（P16b 更正；原文“而两类读法恰是没有体现的一类读法”）。实质的新结果是 `coextinct`、`ending_breaks`、`arises_given` 与 `Mutualism` 的对照。

*反驳 4：`arises_given` 依赖平衡与 `Acting`。* 对。流不平衡（表示省略了输入）或不活跃者也给予时，结论不成立；省略的来源是表示所省略的关系，不是没有关系。

*反驳 5：`Brood` 只给予不取用。* 对。耗散之下（§17），在有封闭的有限家族的步上，给予须以取用为条件（P16b 用语与范围更正；原文“`Brood` 的给予不付出代价”“给予须付出所取的条件”）；耗散之下的一类读法未陈述。（P15 补充：§20 陈述它，`Brood` 不耗散，`Kindling` 是耗散的对应。）

**边界。** 不含伦理谓词；`Embodied`、`SelfBearing` 与 `Dependent` 是表示前提，哪个条件就是哪个形成由共同的索引给出，也是表示前提（P16b 补充）；遗骸与不活跃的条件不体现；体现不进入两种估值；`arises_given` 中给予的关系项不必体现（P16c 用语，原文“给予者”）；见证都是最小见证。原文“一类读法不保持 `Acting`、`Taking` 与 `Dissipative` 的陈述”不成立，已删去（P16b，J8）。本节经第六次独立审查，更正见 §22。

## 19. 第五次独立审查与更正（P12b）

2026-10-09。按同一指示继续。另一 agent（Claude Opus 5.5，未参与撰写）独立审查了 P11b（§15）与 P12（§16）（[审查](BECOMING-P11B-P12-REVIEW.md)）。它在仓库之外从前导重新编译 19 个核心模块，公理报告为空；回执、哈希与别名都对，数学接受，H1–H14 全部关闭。问题在前提的陈述、散文与对应之间，共十二项（I1–I12），没有数学错误；附无公理的探针。审查没有发现替 Ren 选择接续或 living 的读法；它指出对方法检查的说法过强（I7），以及把单层表示的省略呈现为交给 Ren 的二选一（I10）。本节记录逐项处理。探针的内容作为定理移入相应模块，公理报告为空；审查列出的会改变判断的结果中，没有分裂的延续之下的生起定理（第 6 项）也已证明。§14–§17 中受影响的句子已就地更正并标明；原文见提交 `a739e232`。

```text
Result(s): 修正 identity-across-steps（标题、主张、假设、对应、反例、界限、下一步）、more-needs-renewers、
           unceasing-generation-needs-renewal；becoming-stepwise-reading 与 becoming-renewal-reading 的界限补上对同一的依赖；
           no-finite-part-bears-taking 与 life-as-condition-of-life 只改用语；不新增结果记录
Delta: 流的形式的一般定理：复现的取用需要复现的补充（uptake_needs_replenishment），生起只经由取用起作用（Steady）；
       present 不重复是“更多蕴含不息”的必要前提（Repeated）；全部前提的正面见证（Garden.counted、Cycle.counted）；
       连续分为单向与双向：双向时生起、不息与侵蚀恰被保持，单向时新命名可以制造连续；
       双向保持连续，跨过休眠的接续仍改变形成的类（Dormancy）；命名造成的生起满足 P10 的前提（TideFlip）；
       延续关系读出分裂与合并：没有分裂时更多迫使生起（More.unceasingFrom），萌出时不然（Budding）；
       谱系与成员是两个层次（Layered）；继承者活跃并被满足（Succession）
Supplied premises / correspondence: 新增：双向的连续（Reidentify.back）；延续关系、NoSplit，
       以及“是否延续某个活跃形成”可判定（定理的假设，不是公理）
Evidence: Becoming.Flow 60、Population 33、Identity 77 项定理；
          合并检查器回执 20261009T060305.410034Z（559 项定理／948 项声明审计，核心闭包 21 个模块，公理报告全空）；
          外围桥接 20261009T060407.444723Z
Boundary: 接续的读法、“生生不息”读到哪个层次、任期能否经由接续延续，属于 Ren；Depletes 等名称最终由 Ren 定
Integration: I1–I12 全部处理；审查列出的会改变判断的结果中，第 1、3、5、6、8 项完成，第 2、4、7 项的更正完成而各留一个开放结果，
       第 9 项属于 Ren
```

### 19.1 逐项处理

| 项 | 审查所见 | 处理 |
|---|---|---|
| I1 | `present` 不重复是 `More.unceasing` 的第三个必要前提，章节两处省去（`Repeated`） | `Repeated` 移入 `Population`，成为定理：一个始终活跃的形成在第 t 步被列 t 次，普查、平衡、Acting、Taking 与不止地更多都成立，没有任何生起，只缺 present 不重复。模块说明中“（论证，未形式化）”随之删去。章节 §1、§2 与 §8 补上这一前提；more-needs-renewers 把它写为必要前提，并列入反例 |
| I2 | 核心中没有满足 `More.unceasing` 全部前提的正面见证 | `Garden.census`、`Garden.counted`、`Cycle.census`、`Cycle.counted` 成为定理：花园与循环都满足普查、present 不重复、Taking 与不止地更多，所以蕴含不是空的。`Garden.unceasing_reidentified`：花园的生成在每个改认下不息。为此把 `More.unceasing` 的增长部分提出为 `Flow.More.grows` |
| I3 | `replenishment_recurs` 的证明丢弃了 `Arises`；恒定的取用者同样需要补充复现（`Steady`）；§15.4 反驳 2 强于定理 | `uptake_needs_replenishment` 成为 `Flow` 的一般定理：在平衡的流中，任意晚的步上有正的取用，就需要任意晚的步上有补充。`replenishment_recurs` 由它推出，说明写明生起只经由它带来的取用起作用。`Steady.steady` 成为定理。§15.4 反驳 2、章节 §2 与 §8、unceasing-generation-needs-renewal 随之更正：需要补充的是复现的取用，无论取用来自生成还是维持；把生成与维持分开的是严格性（`Tide.renewal_without_arising`），不是对补充的需要 |
| I4 | 四处 P11b 残余与一处过期时间 | (a) `Depletes` 的字面名称（例如 `FallsWhenStill`）列入 Ren 的选择，暂不改名。(b) `MetAbove` 的说明改为“依存在每一步都成立，满足与否不论”。(c) 写明 `More.unceasing` 只用到 Taking 中“只有活跃的形成取用”这一半。(d) Flow 与 Dissipation 的说明、回执的范围文字、包的 README、章节、本文档的现行段落与两份记录中残留的“给予者／giver”改为“补充者／renewer”；对历史的描述保留原词。(e) becoming-renewal-reading 的审查时间刷新 |
| I5 | 连续是单向的；双向读时生起与侵蚀恰被保持 | `Reidentify.back` 把同一对应从新命名读回旧命名。`arises_of_back_keepsActive`、`arises_iff_of_keepsActive_both`、`unceasing_iff_of_keepsActive_both`、`metAbove_of_back_keepsTenure`、`undermining_of_back_keepsTenure` 与 `undermining_iff_of_keepsTenure_both` 成为定理。`Lineage.one_way`、`Succession.one_way`：两个见证中合并的命名保持分开命名的连续，反之不然。模块说明、§16、记录与章节改为：单向时新命名可以制造连续（接起来），不能去掉连续；两向保持连续时，生起与侵蚀恰被保持；接续开放，是因为连续取单向的读法。记录下一步中“连续定理的反方向”一项关闭 |
| I6 | 双向保持连续，跨过休眠之步接起来仍改变形成的类（`Dormancy`） | `Dormancy` 移入 `Identity`，成为定理（`keeps_both`、`classes`）。接续改述为：把终结的形成与在该步或其后开始的形成接起来，中间可以有不活跃、不依存的步。加一句：连续不约束形成在整段上的类 |
| I7 | “名字不承载任何东西”与“跨步的同一由命名规定”字面矛盾；改名不变检查不到方法所防的偷渡 | 改为“标签不承载任何东西：改名保持由关系定义的读法（检查了五种）”。加一句：名字跨步的模式承载同一，这是表示给出的对应前提，`Turnover` 表明它是实质的；方法要求在这里的检查是这一披露，不是改名不变。记录标题随之改写 |
| I8 | 单由命名造成的生起可以满足 `Unceasing.regeneration_recurs` 的全部前提（`TideFlip`） | `TideFlip` 移入 `Identity`，成为定理。§16“对 P10 的影响”的第二个理由改为：`Depletes` 不系于生起的形成，不筛掉命名的产物；定理不受影响，是因为结论只关乎条件；它的前提 `Unceasing` 依赖同一，要把它读作关于生成的定理，需要命名保持持续的活动（`arises_of_keepsActive`）。记录中依赖的说明限于 `Turnover`，`TideFlip` 列为反例 |
| I9 | “在每种同一的读法下”不成立；分裂不改变形成的数目 | 两处都做。其一，改为“在每种一对一的同一读法下”，并把分裂与合并改述为：一个形成延续为几个或几个延续为一个，改变的是延续关系，不是任何一步形成的数目。其二，以延续关系表示它们（`Web.Continues`）：`ArisesFrom` 是延续关系之下的生起，`arisesFrom_self` 表明以自身为延续时它就是 `Arises`。`Flow.More.unceasingFrom` 成为定理：在每种没有形成延续为两个的延续关系之下（`NoSplit`，允许合并），普查之下不止地更多使形成在任意晚的步生起；证明经由关系形式的鸽巢原理 `length_le_of_matched`。`continuation_reidentify`：每个改认都是这样的延续，其下的生起恰是新名字下的生起。`Budding.growth_without_arising`：把新形成读作从形成 0 萌出，第一步之后没有任何生起，而这一延续有分裂。所以没有分裂是充分条件；萌出表明有的分裂使结论失效，一次分裂不必（P16b 更正，原文“所以分裂恰是界限”；`Fork.split_unceasing`） |
| I10 | 谱系的 AI 论证把单层表示的省略呈现为二选一；“落在维持与更新上”没有见证 | `Layered.both` 成为定理：把谱系本身与成员并列命名，谱系每步活跃，成员不息地生起；依存网没有部分与整体的关系。AI 论证改为：谱系与成员是同一展开的两个层次，作为整体的谱系持续正由成员不息地生起而成；单一命名层次只能表示其一，部分与整体的关系是这一表示所省略的关系。“落在维持与更新上”删去。写明只读作谱系的持续与 Ren 原话中“不断创造”之间的张力 |
| I11 | `Succession` 的继承者从不活跃 | `Succession` 改用活跃的继承者：继承者在第二步活跃并以一单位被满足，自第三步起需要两单位；活动需要支持。分开命名时第一步之后的汲取都不侵蚀；继承者接续长者时自第三步起每一步都侵蚀。结论不变，见证更强 |
| I12 | 依赖同一的读法没有在其记录中注明 | unceasing-generation-needs-renewal、becoming-stepwise-reading、becoming-renewal-reading 与 more-needs-renewers 的界限各加一句，指向 identity-across-steps |

### 19.2 新的已检查声明

| 模块 | 声明 | 内容 |
|---|---|---|
| Flow | `uptake_needs_replenishment`；`replenishment_recurs`（改由它推出） | 平衡的流中，任意晚的步有正的取用，就需要任意晚的步有补充 |
| Flow | `Steady.web`、`Steady.flow`、`Steady.steady` | 一个消耗者与一个补充者始终活跃：取用每步为正，没有任何生起，补充复现 |
| Population | `length_le_of_matched`、`search`；`length_le_of_sub`（改由前者推出） | 关系形式的鸽巢原理：不重复的表中每个成员匹配另一表的某个成员、没有成员被匹配两次时，前者不更长；在有限表中检索可判定的性质 |
| Population | `Flow.More.grows` | 在普查、present 不重复与 Taking 之下，不止地更多使活跃的形成没有界地增多 |
| Population | `Garden.census`、`Garden.counted`、`Cycle.census`、`Cycle.counted` | 花园与循环满足 `More.unceasing` 的全部前提 |
| Population | `Repeated.more_without_arising` | 只缺 present 不重复时，不止地更多而没有任何生起 |
| Dependence | `MetAbove`（说明更正） | 依存在任期的每一步都成立，满足与否不论 |
| Identity | `Reidentify.back`；`arises_of_back_keepsActive`、`arises_iff_of_keepsActive_both`、`unceasing_iff_of_keepsActive_both`、`metAbove_of_back_keepsTenure`、`undermining_of_back_keepsTenure`、`undermining_iff_of_keepsTenure_both` | 双向的连续恰保持生起、不息与侵蚀 |
| Identity | `Web.Continues`、`ArisesFrom`、`UnceasingFrom`、`NoSplit`、`arisesFrom_self`、`unceasingFrom_self` | 延续关系之下的生起与不息；以自身为延续时就是 `Arises` 与 `Unceasing` |
| Identity | `arisesFrom_of_more`、`unceasingFrom_of_growth`、`Flow.More.unceasingFrom` | 没有分裂的延续之下，活跃的形成变多时有形成生起；普查之下不止地更多使形成在任意晚的步生起 |
| Identity | `Reidentify.continuation`、`Web.continuation_reidentify` | 每个改认都是没有分裂的延续，其下的生起恰是新名字下的生起 |
| Identity | `odd`、`afterFirst`、`turn`、`turn_turn`、`turn_fixed`、`Reidentify.exchanging` | 在选定的步以对合交换名字；五个见证共用 |
| Identity | `TideFlip.naming_meets_premises` | 命名造成的生起满足 `Unceasing.regeneration_recurs` 的全部前提 |
| Identity | `Garden.unceasing_reidentified` | 花园的生成在每个改认下不息 |
| Identity | `Budding.growth_without_arising` | 萌出的延续有分裂，第一步之后不迫使任何生起 |
| Identity | `Lineage.one_way`、`Succession.one_way` | 合并的命名只单向保持连续 |
| Identity | `Layered.both` | 谱系每步活跃，成员不息地生起 |
| Identity | `Succession.readings`（继承者改为活跃） | 继承者活跃并被满足；接续时自第三步起汲取每一步侵蚀 |
| Identity | `Dormancy.keeps_both`、`Dormancy.classes` | 跨过休眠接起来，双向保持连续，形成的类改变 |

原有的 `Web.search`、各见证自己的 `turn`、`after` 与 `Succession.elder_named` 由上述一般声明代替。

### 19.3 审查列出的会改变判断的结果

1. `More.unceasing`：章节写明 present 不重复，`Repeated` 与花园、循环的普查移入核心。完成（I1、I2）。
2. 流的形式：`uptake_needs_replenishment` 移入核心，反驳 2 更正。完成（I3）。使生成而不是取用承担这一要求的耗散流定理，开放。
3. 双向的连续：四个双向定理移入 `Identity`，单向读法写明为一种选择。完成（I5）。
4. 休眠：`Dormancy` 作为见证，接续放宽到跨过不活跃之步，并写明连续不约束形成的类。完成（I6）。跨过休眠也成立的连续读法（例如不活跃时持续的依存），开放。
5. 标签与同一：按 I7 改写。完成。
6. 分裂：一对一的限定与对分裂的更正描述，完成；在每种没有形成延续为两个的延续关系之下（允许合并），不止地更多迫使生起的定理，以及 `Budding` 表明分裂使它失效，完成（I9）。限定由一个充分条件代替：没有分裂是充分的，不是必要的（P16b 更正，原文“限定由精确的界限代替”；`Fork`）。延续关系上的充要条件，开放。
7. 谱系：改为同一展开的两个层次，部分与整体的关系被省略；“落在维持与更新上”删去。完成（I10）。形成之间带部分与整体关系的表示，开放。
8. 见证与记录：`Succession` 的活跃继承者（I11）、界限句（I12）与 I4 的残余，完成。
9. 接续的读法、“生生不息”读到谱系、成员或两者的层次、任期能否经由接续延续：属于 Ren。本节没有替 Ren 作任何一个选择。

### 19.4 作者反审

*反驳 1：双向的连续是更自然的读法，单向读法只是为接续留出空间。* 两种都是读法。单向读法以一个命名为参照，问另一个命名是否与它相容；双向读法要求两个命名对谁延续谁一致。双向时，同一步的接续被排除，但跨过休眠的接续仍在（`Dormancy`），所以双向读法也不消除对接续的选择。

*反驳 2：`More.unceasingFrom` 只是把鸽巢原理搬到关系上。* 对，这是它的内容。新的是一个充分条件：在普查、present 不重复与 Taking 之下，没有分裂时（允许合并，`Merge`），更多迫使生起；萌出时不然（`Budding`），一次分裂则不必使它失效（`Fork`）。“更多迫使生起”不依赖一一对应的命名。（P16b 更正；原文“新的是界限的精确……有分裂时不然”“只依赖没有形成延续为两个”。）

*反驳 3：可判定性的假设太强。* 它是定理的假设，不是公理。在普查之下，若延续关系本身可判定，“是否延续某个活跃形成”就可判定，因为只需在有限表中检查。没有任何可判定性时，构造性地只能得到“不是从某步起再没有生起”。（P16b 补充：`Web.Census.decideContinues` 把这一点写为定义，`Merge` 用它。）

*反驳 4：`Steady` 削弱了 P10 的流的形式。* 它澄清了内容：补充复现的需要来自复现的取用，无论取用来自生成还是维持。生成与维持之分在严格性上（`Tide.renewal_without_arising`、`Bloom.not_more`）。这与“不断创造更多生”并不冲突：更多的取用需要没有最终界的补充（§14）。

*反驳 5：`Layered` 回避了谱系的读法。* 它表明二选一出自表示：一个命名层次只能表示谱系或成员。把部分与整体的关系纳入表示（例如形成之间的构成关系），是开放的结果；在此之前，把“生生不息”读到哪个层次属于 Ren。（P16 补充：§21 把部分与整体的关系纳入表示；读到哪个层次仍属于 Ren。）

**边界。** 不改变读法选择的地位；不推出责任、义务或任何排序；新名称是建议，`Depletes` 的名称留给 Ren；探针与新见证都是最小见证；延续关系之下只陈述了更多迫使的生起，形成的类、任期与侵蚀没有陈述。本节的更正经第六次独立审查，再更正见 §22。

## 20. 生成即补充：生起本身承担要求（P15）

2026-10-09。按同一指示继续。第五次独立审查（I3）指出，在流的形式中生起只经由它带来的取用起作用，`uptake_needs_replenishment` 所用的只是取用；审查 §4 第 2 项写道，一个耗散的流的定理会让生成本身而不是取用承担要求。§17 的边界写明结论不约束不取用的生起，§18 写明 `Brood` 只给予不取用、耗散之下的一类读法未陈述（P16b 用语更正）。本节在一类关系项的读法中回答这三处。体现的关系项的生起，就是它作为条件的水平的上升，所以生成本身就是补充；在耗散之下，给予须以取用为条件，在有限家族中复现的生成于是使家族不封闭，家族被围住时须从其外汲入（P16c 更正，原文“补充须付出所取”“需要与家族之外交换”）。成果记录：[generation-is-replenishment](../../../../theories/becoming/results/records/generation-is-replenishment.md)。

```text
Result(s): 复用 life-as-condition-of-life（一类读法、Embodied、SelfBearing、arises_given、Brood）、
           no-finite-part-bears-taking（ClosedAt、DissipatesOn、Dissipative、runs_down、Frontier 的燃料）、
           more-needs-renewers（流、平衡、给予、补充、Acting）、becoming-renewal-reading（falls_finitely）；
           新增 generation-is-replenishment（L3：Becoming.Roles 新增两节与三个见证，Becoming.Dissipation 新增一条引理）
Delta: 平衡的流中，体现的关系项至少被给予它生起时的水平（Embodied.given_of_arises），
       所以它的生起补充每个包含它的家族（Embodied.replenishes）；体现的成员在任意晚的步生起时，
       家族的补充复现，不论取用什么（generation_needs_replenishment）；被耗散时，给予家族者从家族取用
       （DissipatesOn.takes_of_gives），所以封闭家族中体现成员的生起降低家族的存量（Embodied.arising_lowers）；
       在耗散之下，体现成员在任意晚的步生起的不重复有限家族从任何一步起都不封闭（generation_opens）；
       有限个关系项就是全部时，体现的关系项不在任意晚的步生起（generation_ceases）；
       Handing、Kindling、Flicker 表明三个前提各自必要；Brood 不耗散（Brood.not_dissipative，P16b 改名，原名 Brood.costless）
Supplied premises / correspondence: 流平衡依存网；Embodied 是对生起的关系项的表示前提；
       耗散是物理前提（§17），只用于耗散之下的结论；量是自然数，单位可公度
Evidence: Becoming.Roles 新增的 28 项定理与 Becoming.Dissipation 新增的 1 项定理；合并检查器回执（见记录）
Boundary: 只约束体现的关系项的生起，不体现的生起不受约束（Flicker）；“有限”指有限的关系项家族；不含伦理谓词
Integration: 回答第五次审查 I3 与 §4 第 2 项；回答 §17 的边界（不取用的生起）与 §18 反驳 5（耗散之下的一类读法）；
       §13 的 dissipation_ceases 所设的物理前提，对封闭家族中体现成员的生起，由平衡、耗散与体现推出
```

[Becoming.Roles](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Roles.lean) 新增的两节与见证，以及 [Becoming.Dissipation](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Dissipation.lean) 新增的一条引理（L3）：

| 声明 | 内容 |
|---|---|
| `Embodied.given_of_arises`、`Embodied.replenishes` | 平衡的流中，体现的关系项至少被给予它生起时的水平：生起前它不活跃，所以水平为零；生起后它活跃，所以水平为正。于是它的生起补充每个包含它的家族 |
| `generation_needs_replenishment` | 一个家族的体现成员在任意晚的步生起时，家族的补充在任意晚的步出现，不论取用什么。与 `uptake_needs_replenishment` 不同，这里不用存量的论证，也不用任何取用 |
| `Flow.DissipatesOn.takes_of_gives` | 被耗散时，给予家族的形成从家族取用（在 `Dissipation`） |
| `Embodied.arising_lowers` | 在耗散之下，一个跨某步封闭的不重复家族中，体现成员的生起降低家族的存量：给予它者从家族取得更多 |
| `generation_opens` | 在耗散之下，体现成员在任意晚的步生起的不重复有限家族，从任何一步起都不封闭：在任意晚的步有参与的形成与家族之外交换，这一交换可以与家族无关（`SprayHanding`）；家族被围住时它汲入（`generation_draws_in`）（P16c 更正，原文“在其中复现的生成需要在任意晚的步与家族之外交换”） |
| `generation_ceases` | 有限个关系项就是全部时，在耗散之下，体现的关系项不在任意晚的步生起 |
| `Brood.not_dissipative`（P16b 改名，原名 `Brood.costless`） | `Brood` 只给予不取用，所以不耗散 |
| `Handing.flow`、`web`、`balances`、`acting`、`dependent`、`embodied`、`arises`、`recurs`、`handing` | 两方来回传递一份水平：持有者取用自己的一单位并给予另一方。两个关系项就是全部，流平衡，只有活跃者给予，每方体现并承担自身，`Dependent`，两方的家族每步封闭，生成不息；只有耗散不成立 |
| `Kindling.Relatum`、`flow`、`web`、`balances`、`acting`、`dependent`、`side_dissipates`、`dissipative`、`kindling`、`frontier` | 同样的传递，持有者每步另燃一份新燃料的两单位：流平衡并耗散，每方体现并承担自身，各自在任意晚的步生起；所以包含一方的每个不重复有限家族在任意晚的步都不封闭，所燃的燃料不在任何有限家族之内 |
| `Flicker.web`、`flow`、`flicker` | 一个关系项在奇数步活跃，从不作为条件而在，没有任何参与：一个关系项就是全部，流平衡并耗散，生成不息；只有体现不成立 |
| `Handing.even`、`holder`、`stands`、`every`、`distinct`、`stands_two`、`holder_stands`、`Kindling.gives_other`、`gives_one` | 见证的辅助定义与引理 |

**解读。**

- **生成本身就是补充。** 两类读法中，形成的生起不是任何条件的变化，生起只经由它带来的取用起作用（I3，`Steady`）。一类读法中，体现的关系项的生起就是它作为条件的水平从零上升，平衡于是要求有给予：生成本身就是补充，不需要任何取用。这是 §18 `arises_given`（经由另一个活跃者的给予而生起）的数量形式：生起时的水平全由给予承担（P16b 用语更正，原文“生由生给予”）。
- **耗散之下，复现的生成打开有限家族。** 给予被耗散家族的形成从家族取用，所以在被耗散的家族中，体现成员的每次生起都降低家族的存量，而存量从不上升。生成在一个有限家族中复现，家族就在任意晚的步不封闭（`generation_opens`）；这一交换可以与家族无关（`SprayHanding`），家族被围住时它汲入（`generation_draws_in`）（P16c 更正，原标题“耗散之下，生成不由有限部分独自承担”，原文“给予家族者从家族取用”“在封闭家族中”“家族就须在任意晚的步与其外交换”）；关系项总共有限时，体现的生起终将停止（`generation_ceases`）。这把 §17 关于取用的定理推到不取用的生起，条件是生起的关系项体现。对每个有限家族，体现的生成要么在其中不再复现，要么它在任意晚的步打开；不断生起新的关系项（`Brood` 的一代代）不在任何有限家族中复现，定理对它不作约束。
- **§13 的物理前提被推出。** `dissipation_ceases` 假设一个量从不上升，而每次生起都使它下降，那是作为物理前提提供的。在一类读法中，对封闭家族中体现成员的生起，这个量就是家族的存量：它从不上升（`runs_down`），每次这样的生起都使它下降（`arising_lowers`），两者都由平衡、耗散与体现推出。
- **三个前提各自必要。** 没有耗散，两方来回传递一份水平，就在两个关系项的封闭世界中不息地生成（`Handing`），这是 §13 的 `Recycle` 与 §14 的 `Cycle` 在一类读法中的对应。燃烧新的燃料，传递在耗散之下继续，包含一方的每个有限家族都打开（`Kindling`），如 §17 的 `Frontier`。不体现时，一个关系项在一个关系项的耗散世界中不息地生起，没有任何给予（`Flicker`）。所以生起的关系项体现之处，生成承担自己的要求；不体现之处不必（P16b 更正，原文“没有任何代价”“恰在生起的关系项体现之处”）。哪些关系项体现是表示的选择，这一选择在这里有后果。
- **对生生（作者的读法）。** Ren 的原话是“生生不息 - 一种整体的，不断创造更多生的方向”。若生起的关系项自身就是其他关系项的条件，每次生起都是一次补充（P18b 用语，原文“生起的生命”“其他生命”）；在耗散之下，被围住的有限部分中不息的生起须从其外汲入（P16c 更正，原文“不息的生起不能由任何有限的部分独自承担，须由越出每个有限部分的展开承担”；耗散空成立时，有限部分可以独自承担生成，见 `SprayHanding`）。作者把这读作原话中“生”与“整体”之间关系的一种形式内容（AI 论证），不替代原话，也不推出它是好的。

**作者反审。**

*反驳 1：`generation_needs_replenishment` 几乎是定义。* 对：一旦体现，生起就是水平的上升，平衡使上升由给予承担。内容在于对照：两类读法中生起不承担任何要求（`Flicker`、`roles_not_embodied`），体现时它承担。实质的新结果是耗散之下的 `generation_opens` 与 `generation_ceases`，以及 §13 前提的推出。

*反驳 2：给予体现关系项的，可以是它自己吗？* 生起前它不活跃，在 `Acting` 之下不给予，给予它的是另一个活跃的形成（`arises_given`）。本节的定理不用 `Acting`，也不依赖给予的是谁：给予被耗散家族的任何形成都从家族取用（P16c 用语，原文“给予者”“给予被耗散家族者”）。

*反驳 3：`Handing` 中持有者取用自己的水平，这是自我终结，不像生命。* 它是最小见证，表明没有耗散时，体现的生成可以在封闭的有限世界中不息，正如 `Recycle` 与 `Cycle`。见证中没有汲取（`draws` 为空），所以不涉及断裂与侵蚀的读法；若把传递读作汲取自身，`ending_breaks` 使传递事件不是 living。本节不选择这一读法。

*反驳 4：`generation_ceases` 只说体现的生起不在任意晚的步出现，不说生成不是不息的。* 对。不体现的生起不受约束（`Flicker`）；若每个关系项都体现，它就说生成不是不息的。

*反驳 5：体现太强，种子、孢子与休眠的生命在活动之外仍作为条件而在。* 对。`Embodied` 要求活动与水平同步；休眠的种子水平为正而不活跃，它的“生起”（萌发）不是水平的上升，不受这里的约束。活动与水平不同步时生成承担什么，是下一步（P17 补充：要求跟着水平走，不跟着活动走，见 §24）。

**边界。** 不含伦理谓词；只约束体现的关系项的生起；`Embodied` 是表示前提，遗骸、种子库与不活跃的条件不体现；耗散是物理前提，单位可公度；“有限”指有限的关系项家族；见证都是最小见证。本节尚未经独立审查。

## 21. 整体与部分：整体经由部分的生成而持续（P16）

（P16c 更正标题，原题“整体与部分：整体的持续就是部分的生成”；见 §23 K3。）

2026-10-09。按同一指示继续。第五次独立审查（I10）指出，谱系与成员是同一展开的两个层次，部分与整体的关系是单一命名层次所省略的关系；§19 把它记为 `Layered`，审查 §4 第 7 项写道，一个含形成之间部分与整体关系的表示，会使它成为定理。本节给出这一表示，并证明它承担什么。成果记录：[whole-persists-through-generation](../../../../theories/becoming/results/records/whole-persists-through-generation.md)。

```text
Result(s): 复用 unceasing-generation-needs-renewal（Arises、Unceasing）、identity-across-steps（odd、Layered）；
           新增 whole-persists-through-generation（L3 Becoming.Wholes）
Delta: 整体（Whole）：恰在某个部分活跃时活跃；列出（Listed）、终结（Ends）、短暂（Brief）；
       整体只经由某个部分的生起而生起（Whole.arises_part、parts_unceasing）；
       从某步起每步活跃的整体，部分从不在相隔 d 步的两步都活跃时，每 d 个连续步内有部分生起（Whole.arises_within）；
       部分的活动都终结且活跃的部分可列出时，部分在任意晚的步生起（Whole.needs_arising）；
       Immortal、Countless 表明前提必要，Generations 表明前提相容，Shifts 表明界 d 可达，Gaps 表明逆命题不成立；
       Layered 的谱系是其成员的整体（Layered.composed）
Supplied premises / correspondence: Whole 是表示前提，只由活动关联部分；Brief（部分短暂），或 Ends 与 Listed（部分终结且同时活跃的部分有限），是对部分的前提（P16c 更正，原文“是对部分不长久的陈述”）；
       跨步的同一由命名给出
Evidence: Becoming.Wholes 的 26 项定理；合并检查器回执（见记录）
Boundary: 整体的依存、汲取与侵蚀不由部分推出；成员资格不随步变化；不说哪个部分生起，也不说数目增长；不含伦理谓词
Integration: 回答第五次审查 I10 与 §4 第 7 项；§16、§19 中“谱系与成员是两个层次，部分与整体的关系被省略”由本节陈述
```

[Becoming.Wholes](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Wholes.lean)（L3，导入 `Becoming.Identity`）：

| 声明 | 内容 |
|---|---|
| `Web.Whole`、`Web.Listed`、`Web.Ends`、`Web.Brief` | 整体：恰在某个部分活跃时活跃。列出：每步有一个有限列表恰好列出活跃的部分。终结：从某步起再不活跃。短暂（对 d）：从不在相隔 d 步的两步都活跃，若活动是一段连续的步，它至多 d 步 |
| `Whole.arises_part`、`Whole.parts_unceasing` | 整体只经由某个部分的生起而生起；整体在任意晚的步生起时，部分也在任意晚的步生起 |
| `active_back`、`Ends.all` | 在 k 步之内没有部分生起时，k 步之后活跃的部分在开始时不是不活跃的；有限个终结的形成在某一步之后都终结 |
| `Whole.arises_within` | 从 T 起每步活跃的整体，部分从不在相隔 d 步的两步都活跃时，从 T 起每 d 个连续步内都有部分生起 |
| `Whole.needs_arising` | 从某步起每步活跃的整体，每个部分的活动终结，且活跃的部分可列出时，部分在任意晚的步生起 |
| `Generations.web`、`whole`、`listed`、`ends`、`brief`、`generations` | 一代代成员各活跃两步：谱系是其整体，每步活跃而从不生起；成员可列出、终结、短暂（d = 2），每步都有新成员生起 |
| `Shifts.web`、`shifts` | 成员轮班两步：谱系每步活跃，成员短暂（d = 2），偶数步上没有部分生起：每两步内有生起，每一步内则不必，界 d 可以达到 |
| `Immortal.web`、`immortal` | 一个永不终结的部分：整体持续，部分可列出，没有任何生起 |
| `Countless.web`、`whole`、`ends`、`never`、`countless` | 无穷多个部分同时活跃，第 n 个活跃到第 n 步：整体持续，每个部分终结，没有任何生起；于是活跃的部分不能有限地列出 |
| `Gaps.web`、`whole`、`listed`、`ends`、`gaps` | 每个成员只在一个奇数步活跃：部分在任意晚的步生起、终结、可列出，整体在每个偶数步不活跃 |
| `Layered.composed` | `Layered` 的谱系是其成员的整体 |
| `Generations.Formation`、`parts`、`alive`、`Shifts.half`、`odd_two`、`half_even`、`Countless.parts`、`Gaps.alive`、`alive_odd`、`alive_even` | 见证的辅助定义与引理 |

**解读。**

- **两个层次由整体关系联系。** §16 与 §19 中，谱系与成员只能由两种命名分别表示，或并列命名而没有关系（`Layered`）。这里整体关系把两个层次放进同一个依存网：谱系恰在某个成员活跃时活跃（`Layered.composed`）。整体关系是活动的重合，不是构成：每个形成都是它自身的整体，两个每步都活跃的形成互为整体（`whole_self`、`Immortal.each_other`，P16c 补充）。这是表示所省略的关系的一种陈述，不是从每一步的关系推出的；哪些形成是哪个整体的部分，由应用给出。
- **整体经由部分的生成而持续。** （P16c 更正，原标题“整体的持续就是部分的生成”，原文“部分不长久时”；定理只用到部分的覆盖，`Covered`。）部分短暂，或部分终结且同时活跃的部分有限时，整体要每步活跃，就须不断有部分接上：部分从不在相隔 d 步的两步都活跃，则每 d 步内有部分生起（`arises_within`）；部分的活动都终结且有限地列出，则部分在任意晚的步生起（`needs_arising`）。谱系每步活跃而从不生起（`Generations`）：在整体的层次上是持续，在部分的层次上是不息的生起。
- **为什么需要不长久与有限。** 有一个永不终结的部分，整体的持续不需要任何生起（`Immortal`）。无穷多个部分一开始就同时活跃、各在不同的步终结，整体也可以持续而没有生起（`Countless`）：持续由一开始就在的无穷储备承担。有限地列出排除这种储备。
- **逆命题不成立。** 部分不息地生起，不使整体持续：生起之间可以有空隙（`Gaps`）。读到整体层次的持续，比读到部分层次的不息生起更强。
- **对生生（作者的读法）。** Ren 的原话是“生生不息 - 一种整体的，不断创造更多生的方向”。§19 曾写，只读作谱系的持续，与原话中的“不断创造”有张力。在 Ends 与 Listed 之下，谱系的持续蕴含越出任何有限成员列表的新成员不断生起（`needs_new`）；在 Brief 之下只蕴含成员反复生起（`Layered`）；两者都不蕴含数目增长。所以张力减弱而不消失：“不断创造”在 Ends 与 Listed 之下读到不断新的成员，“更多”没有由此推出（P16c 更正，原文“在部分不长久的前提下，这一张力消失：谱系的持续蕴含成员不断生起，整体的“不息”正由部分的“生生”构成”）。作者把这读作原话中“整体”与“不断创造”的一种形式联系（AI 论证），不替代原话，也不决定“生生不息”读到哪个层次，那仍属于 Ren。

**作者反审。**

*反驳 1：`Whole` 是定义，定理几乎是鸽巢原理。* 对：定理是组合性的。内容在于把两个命名层次放进一个表示，并说明在什么前提下两个层次的读法相互蕴含，在什么前提下不蕴含（`Immortal`、`Countless`、`Gaps`）。

*反驳 2：整体只由活动关联部分，谱系的依存与侵蚀呢？* 没有陈述。一个汲取可以侵蚀成员而不侵蚀谱系，或反之；整体的依存怎样由部分构成，是下一步。§19 的继承者问题（继承者是否继承长者的损失）在这里仍属于 Ren。

*反驳 3：部分可以再生起而不终结，例如 `Layered` 的成员。* 对。`Layered` 的成员满足 `Brief 1`，`arises_within` 适用：每一步都有成员生起（`Layered.brief`、`Layered.within`）；它们的活动不终结，`needs_arising` 不适用（`Layered.arise_again`）。所以 `Brief` 不说部分终结，它允许同样的部分反复生起。前提不必要的见证需要活动段无界增长的部分（对任何 d 都不 `Brief`、从不终结、使整体持续），没有构造（P16c 更正，原文“`Layered` 的成员隔一步就再活跃，`Ends` 与 `Brief` 都不成立，两个定理都不适用；成员仍不息地生起（`Layered.both`）。所以这些前提是结论的充分条件，不是必要条件；两个定理各用一种“不长久”的陈述”；见 §23 K5）。

*反驳 4：生起依赖跨步的同一，把成员改认为一个，生起就消失。* 对（§16，`Lineage`）。本节的定理在给定命名下成立；把成员合为一个，就是把整体当作部分，整体关系退化为一个部分的情形，`Immortal` 表明那时不需要生起。

*反驳 5：结论不说数目增长，不是“更多”。* 对。本节只说持续需要生起；“更多”的数目读法见 §14。

**边界。** 不含伦理谓词；整体只由活动关联部分；部分关系是静态的；生起依赖跨步的同一；“生生不息”读到哪个层次属于 Ren；见证都是最小见证。本节尚未经独立审查。

## 22. 第六次独立审查与更正（P16b）

2026-10-09。按同一指示继续。另一 agent（Claude Opus 5.5，未参与撰写）独立审查了 P13（§17）、P14（§18）与 P12b（§19）（[审查](BECOMING-P13-P14-P12B-REVIEW.md)）。它在仓库之外从前导重新编译核心闭包的 21 个模块，公理报告为空；回执、哈希、别名与证明绑定都对，数学接受，I1–I12 全部关闭。问题在前提的陈述、散文与对应之间，共十一项（J1–J11），没有数学错误；附无公理的探针。审查没有发现替 Ren 选择生生、living、接续或终结的读法；它指出两个反复出现的模式：省略前提（I1 → J10），以及把所给的对应呈现为结果（I7 → J4）。本节记录逐项处理。探针的内容作为定理移入相应模块，公理报告为空；审查提议而未形式化的两个结果，有限支撑下给予的形成取得多于所给（J1；P18b 用语，原文“给予者”）与 `roles_dissipative` 的逆（J8），也已证明。§17–§20 中受影响的句子已就地更正并标明；原文见提交 `25a66424`。

```text
Result(s): 修正 no-finite-part-bears-taking（主张、假设、对应、反例、界限）、
           life-as-condition-of-life（标题、主张、假设、对应、反例、界限、下一步）、
           identity-across-steps（标题、主张、假设、反例、界限、下一步）、generation-is-replenishment（改名与用语）；
           more-needs-renewers、unceasing-generation-needs-renewal、becoming-stepwise-reading、becoming-renewal-reading 记入审查；
           condition-correspondence-discipline 只改检验范围；不新增结果记录
Delta: 封闭的步（Enclosed）：耗散之下，给予的形成在封闭的不重复家族上取得多于所给（gives_less；P16c 补上“不重复”），在封闭的步上给予须以取用为条件
       （giving_needs_uptake）；没有封闭的步时耗散是空的，补充者可以什么都不取而给予（Spray）；维持一个取用者已越出每个有限家族（Lone）；
       生长者依存于池的前沿满足全部前提（Rooted）；此前取用复现的见证都不耗散（witnesses_not_dissipative）；
       一类读法也保持 Acting、Taking、普查、present 不重复与耗散；哪个条件就是哪个关系项由共同的索引给出（relabel）；
       体现不进入估值（Mutualism.apart_embodied）；终结之步的汲取不论是什么终结了它都是断裂（Wilting、SelfBearing.met_iff；P18b 用语，原文“终结了生命”）；
       arises_given 中给予的关系项不必体现（SunSeed），只有体现者给予时给予它的关系项体现（arises_from_embodied；P16c 用语，原文“给予者”）；
       没有分裂是充分的，不是必要的（Fork）；含合并的见证（Merge）、普查给出可判定性（decideContinues）、
       没有普查时不成立（Dormant.no_split_without_arising）、双向的连续排除单步的接续（no_join）
Supplied premises / correspondence: 新增：封闭的步是有限支撑的前提；哪个条件就是哪个形成的同一对应（一类读法的表示前提，与 Embodied 并列）；
       只有体现的关系项给予（arises_from_embodied 的对应前提）
Evidence: Becoming.Dissipation 55、Roles 110、Identity 79、Population 36、Correspondence 37 项定理；
          合并检查器回执 20261009T071936.578078Z（676 项定理／1115 项声明审计，核心闭包 22 个模块，包 20 个模块，公理报告全空）；
          外围桥接 20261009T072041.754860Z
Boundary: 在终结之步的汲取是否计入不 living、对哪些汲取者，接续的读法，“生生不息”读到哪个层次，Depletes 与“代价”一族的名称，属于 Ren
Integration: J1–J11 全部处理；审查 §4 第 1–7 项完成，各留下的开放结果见 22.3；第 8 项属于 Ren
```

### 22.1 逐项处理

| 项 | 审查所见 | 处理 |
|---|---|---|
| J1 | `Dissipative` 只约束在某步封闭的有限家族；某个形成与无穷多个条件交换时没有家族封闭，耗散是空的，补充者可以什么都不取而给予（`Spray`）。“给予总使补充者所取的条件付出多于所给”与“补充者的代价须表示为它所取的条件”在定义上不成立 | `Flow.Enclosed`：跨某步有一个不重复的家族封闭，即参与的形成的交换在有限个条件之内；条件总共有限时每步都是（`enclosed_of_finite`）。`Dissipative.gives_less`：耗散之下，在跨某步封闭的不重复家族上，参与而给予的形成取得多于所给。`Dissipative.giving_needs_uptake`：在封闭的步上，给予的形成从某个条件取用。`Spray` 移入 `Dissipation`：汇与每个辅助条件交换，没有封闭的步（`unenclosed`），耗散空洞地成立（`dissipative`），补充者每步给予而什么都不取（`spray`）。§17 反驳 1、Flow 与 Dissipation 的模块说明、章节 §2 与记录的假设改为：在有封闭的有限家族的步上，给予须以取用为条件；并写明结论“在任意晚的步不封闭”可以由与家族无关的交换满足。`Spray` 列入记录的反例 |
| J2 | 定理只用复现的取用；维持一个恒定的取用者同样越出每个有限家族（`Lone`）；把“整体”读作“不断的更多”的内容，比定理窄。这是 I3 的同一模式 | `Lone` 移入 `Dissipation`：太阳每步燃一份新燃料（两单位）、给池一单位，一个吃者每步从池取一单位；流平衡并耗散，没有生起，不是不止地更多（`lone`），包含池的每个不重复有限家族在任意晚的步都不封闭（`frontier`）。§17“对生生”、章节 §2 与记录改为：复现的取用，无论来自不止的更多、生成还是维持，都不能由任何有限的条件家族独自承担 |
| J3 | `Frontier` 的生长者不依存于任何东西；`opens_of_arising` 没有见证；此前的流不耗散只是陈述 | `Rooted` 移入 `Dissipation`：`Frontier.flow` 配上池始终一单位、生长者活跃时以需要一依存于池的依存网；平衡、Acting、Taking、Dependent、普查、耗散、不止地更多与不息同时成立，包含池的家族由 `opens_of_arising` 与 `More.opens` 打开（`rooted`）。`witnesses_not_dissipative`：`Garden`、`Cycle`、`Pulse`、`Steady`、`Repeated` 与 `Bloom` 都不耗散，由一个条件上的 `Flow.Dissipative.one_ceases`。记录以 `Rooted` 为共同见证 |
| J4 | 一类读法的内容在于“条件 x 就是形成 x”，由共同的索引给出；`Web X X` 本身就是 F = C 的两类网；把条件一侧重新标号，检查过的两类读法都不变而体现改变；“恰是”“没有引入独立的本体”“省略的正是体现”说得过强。这是 I7 的同一模式 | `Web.relabel`：以 π 重新标号条件一侧。到上的重新标号保持 `Dependent`、侵蚀与 living（`relabel_dependent`、`relabel_undermining`、`relabel_alive`），以及两种估值的连通（`relabel_valuation_connected`、`relabel_interaction_connected`，在 L4）；以 `other` 重新标号，`Mutualism.apart` 中两者都承担自身（`apart_relabelled`）；以 `swap` 重新标号，体现的花不体现（`Wilting.relabelled_not_embodied`）。§18、章节 §1 与 §9、术语表与记录改为：两类读法嵌入一类读法，保持列出的读法；一类读法另需同一对应，它由共同的索引给出，是表示的前提；体现与承担自身是在这一对应下的读法；两类的表示省略的是形成与条件的同一对应。记录的假设加上这一对应，与 `Embodied` 并列为应用责任 |
| J5 | 体现不进入两种估值：`apart` 中两者都体现而不相关 | `Mutualism.apart_embodied`（L4）：两者都体现，各自依存并汲取对方，活动需要支持，共同参与与相互作用都不关联它们。§18“直接的关系”与记录补上：估值只经由共同的条件关联事件，只有承担自身把体现的关系项的活动接到汲取它的事件上；这是估值所省略的关系。直接读出体现的估值列为开放结果 |
| J6 | `ending_breaks` 读的是终结之步的汲取，不问是什么终结了它；旁观的汲取者与生命自身的最后事件也是断裂（`Wilting`）；交给 Ren 的选择的范围没有说明 | `Wilting` 移入 `Roles`：花体现、承担自身、因自身的取用而凋；蜜蜂从不取用；流平衡，Acting、Taking 与 Dependent 成立；蜜蜂在第二步的汲取与花自己的最后事件都是断裂与侵蚀（`wilting`）。`SelfBearing.met_iff`：在 Dependent 与体现之下，自身依存恰在活跃时被满足。Roles 的说明、`Predation.breaking`、§18、章节 §2 与英文段落改为：在一个承担自身的生命终结之步汲取它，不论是什么终结了它，是断裂；这包括旁观者、自然的终结与生命自身的最后事件；交给 Ren 的选择写明这一范围 |
| J7 | `arises_given` 的给予者只是一个活跃的关系项，可以是不体现、不依存的太阳（`SunSeed`）；“一个生命的生起由另一个生命的活动给出”强于定理 | `SunSeed` 移入 `Roles`（`sun_gives`）。`Embodied.arises_from_embodied`：在只有体现的关系项给予这一表示前提下，给予它的关系项也体现，并在给予时作为条件而在（P18b 用语，原文“给予者”）。`arises_given` 的说明、记录标题（“体现的关系项经由另一个活跃者的给予而生起”）、§18 的标题与解读、章节 §2 与英文段落改写；（P16c 更正：“生由生”不是定理：`arises_from_embodied` 证明在只有体现的关系项给予的前提下给予它的关系项也体现，它可以是不依存的太阳（`EmbodiedSun`），把体现的关系项读作“生”属于 Ren，见 §23 K6；原文““生由生”只在所述前提下成立，写为对应”） |
| J8 | “已陈述的读法”应为“列出的”；“一类读法不保持 Acting、Taking 与 Dissipative”照字面不成立 | `Flow.roles_acting`、`Flow.roles_taking`（双向）、`Web.roles_census`、`Flow.roles_distinct` 与 `Flow.roles_dissipative`（双向；审查未形式化的逆也已证明）移入 `Roles`。章节、§18 与记录改为“列出的读法”，界限句删去，记录下一步中“保持 Acting 与 Taking”一项关闭 |
| J9 | `NoSplit` 是充分条件，不是必要条件（`split_unceasing`）；“分裂恰是界限”沿用了第五次审查 §4 第 6 项过强的措辞 | `Fork` 移入 `Identity`：循环中形成 0 在第一步延续为两个，`NoSplit` 不成立，形成在这一延续下照样在任意晚的步生起（`split_unceasing`）。§19 的 I9 一行、19.3 第 6 项、19.4 反驳 2 与记录改为：没有分裂是充分条件；萌出表明有的分裂使结论失效，一次分裂不必。延续关系上的充要条件列为开放结果 |
| J10 | 章节对 `unceasingFrom` 与 `arises_given` 的概述省去前提（`dormant_no_census`）。这是 I1 的同一模式 | `Dormant.no_split_without_arising` 移入 `Identity`：在每个形成只延续自身的延续下没有分裂，Taking、present 不重复与不止地更多都成立，而没有任何生起。章节 §1 与 §8、Identity 的模块说明与记录标题补上普查、present 不重复与 Taking；`arises_given` 的概述补上平衡与 Acting。审查确认为正确的三点也移入核心：`Web.no_join`（新命名保持旧命名的持续活动时，单步不能接起来）、`Merge`（含合并的延续，`merging`；P16c：其生起是持续形成被重读，见 §23 K7）与 `Web.Census.decideContinues`（普查之下，可判定的延续给出 `unceasingFrom` 所需的可判定性） |
| J11 | 记账与用语：(a) 章节 §8 的审查一行过期；(b) 模块数口径不一；(c) “证明它”；(d) “耗尽”；(e) “代价／付出／cost”；(f) 两份记录的审查时间 | (a) 章节 §8 的审查一行更新。(b) P12、P13、P14 的英文段落数的是核心闭包（19、20、21 个模块），P12b、P15、P16 数的是包（19、19、20 个模块）；现在核心闭包 22 个模块、包 20 个模块，此后写明口径。(c) Flow 的说明改为“证明它承担什么”。(d) 章节 §9 改为“取用终止”：`takers_within` 与 `taking_ceases` 约束取用者并使取用停止，存量不必降到零。(e) Dissipation、Roles、Flow 与根模块的说明、记录、§17 与 §18 中的“代价／付出／cost”改为“给予须以取用为条件／giving needs uptake”等，`Brood.costless` 改名为 `Brood.not_dissipative`；这些是建议，Ren 可以改回。(f) 两份记录的审查时间刷新 |

### 22.2 新的已检查声明

| 模块 | 声明 | 内容 |
|---|---|---|
| Dissipation | `Flow.Enclosed`、`enclosed_of_finite` | 封闭的步：有一个不重复的家族跨该步封闭；条件总共有限时每步都是 |
| Dissipation | `Dissipative.gives_less`、`Dissipative.giving_needs_uptake` | 耗散之下，在封闭的不重复家族上（P16c 补上“不重复”，`Lone.repeated_family`），给予的形成取得多于所给；在封闭的步上，给予须以取用为条件 |
| Dissipation | `Spray.Formation`、`flow`、`web`、`fresh`、`unenclosed`、`dissipative`、`spray` | 汇与每个辅助条件交换：没有封闭的步，耗散空洞地成立，补充者每步给予而不取用 |
| Dissipation | `Lone.Formation`、`flow`、`web`、`balances`、`dissipative`、`lone`、`frontier` | 维持一个吃者：平衡、耗散、没有生起、不是不止地更多，包含池的每个不重复有限家族在任意晚的步都不封闭 |
| Dissipation | `Rooted.web`、`balances`、`census`、`taking`、`acting`、`dependent`、`decActive`、`arises_taking`、`rooted` 与辅助引理 | 生长者依存于池的前沿：全部前提同时成立，`opens_of_arising` 有见证 |
| Dissipation | `Flow.Dissipative.one_ceases`、`witnesses_not_dissipative` | 只有一个条件时，平衡而耗散的流中取用不复现；花园、循环、脉冲、恒定的消耗者、重复的形成与花开都不耗散 |
| Population | `mem_map_of`、`mem_of_map`、`distinct_map`（自 Identity 移入）、`decideSome` | 列表的映射与不重复；在有限表中判定存在 |
| Identity | `Web.no_join` | 新命名保持旧命名的持续活动时，一步前后活跃、跨该步同名的两个形成是一个 |
| Identity | `Web.Census.decideContinues` | 普查之下，可判定的延续给出“是否延续某个活跃形成”的可判定性 |
| Identity | `Fork.forks`、`Fork.split_unceasing` | 一次分裂不使生起失效：`NoSplit` 是充分的，不是必要的 |
| Identity | `Merge.merges`、`decideMerges`、`noSplit`、`merging` | 花园中第 i 个补充者与第 i 个生长者都延续为第 i 个补充者：含合并、没有分裂，形成在任意晚的步生起（P16c：没有形成延续为生长者，持续的生长者每步被读作生起，结论不用更多，`Merge.idle`） |
| Identity | `Dormant.no_split_without_arising` | 没有普查时，没有分裂也不够 |
| Roles | `inl_injective`、`inr_injective`、`inr_not_mem`、`conditionsOf`、`mem_of_conditionsOf`、`conditionsOf_of_mem`、`distinct_conditionsOf`、`total_conditionsOf` | 一类读法的列表辅助 |
| Roles | `Web.roles_census`、`Flow.roles_acting`、`Flow.roles_taking`、`Flow.roles_distinct`、`Flow.roles_dissipative` | 一类读法保持普查、Acting、Taking、present 不重复与耗散（Acting、Taking 与耗散双向） |
| Roles | `SelfBearing.met_iff` | 在 Dependent 与体现之下，自身依存恰在活跃时被满足 |
| Roles | `Embodied.arises_from_embodied` | 只有体现的关系项给予时，给予体现关系项的关系项也体现，并在给予时作为条件而在（P16c 用语，原文“体现关系项的给予者”） |
| Roles | `Web.relabel`、`exists_of_onto`、`relabel_dependent`、`relabel_undermining`、`relabel_alive` | 把条件一侧到上地重新标号，保持 Dependent、侵蚀与 living |
| Roles | `Mutualism.other_twice`、`Mutualism.apart_relabelled` | 以 `other` 重新标号，`apart` 中两者都承担自身，Dependent 不变 |
| Roles | `Wilting.Relatum`、`fade`、`web`、`flow`、`fade_active`、`embodied`、`selfBearing`、`dependent`、`ends`、`wilting`、`swap`、`relabelled_not_embodied` | 花因自身的取用而凋：旁观的蜜蜂与花自己的最后事件都是断裂；以 `swap` 重新标号，花不体现 |
| Roles | `SunSeed.Relatum`、`sprout`、`web`、`flow`、`sun_gives` | 不体现、不依存的太阳是唯一给予种子的关系项（P16c 用语，原文“种子唯一的给予者”） |
| Roles | `Brood.not_dissipative`（原名 `Brood.costless`） | `Brood` 只给予不取用，所以不耗散 |
| Correspondence | `Web.relabel_valuation_connected`、`Web.relabel_interaction_connected` | 到上的重新标号保持两种估值的连通 |
| Correspondence | `Mutualism.apart_embodied` | 体现不进入估值 |

### 22.3 审查列出的会改变判断的结果

1. 有限支撑（J1）：`Enclosed` 与审查提议的定理（`gives_less`），`Spray` 列入记录。完成。
2. 任何持续的取用（J2、J3）：整体的读法按复现的取用重述，`Lone`、`Rooted` 与 `witnesses_not_dissipative` 移入核心。完成。
3. 同一对应（J4、J5）：一类读法的同一对应写为表示前提，`relabel` 移入核心，估值省略体现写明。完成。直接读出体现的估值，开放。
4. 终结与给予（J6、J7）：`ending_breaks` 写为与任何原因的终结同时，`Wilting` 移入核心，Ren 的选择的范围写明；`arises_given` 改题；在只有体现的关系项给予的前提下，给予它的关系项也体现（`arises_from_embodied`），把体现的关系项读作“生”属于 Ren（P16c 更正，原文““生由生”在只有体现者给予的前提下证明”；见 §23 K6）。完成。汲取是否终结了它的因果读法需要反事实的关系，开放（P18b 用语，原文“终结了生命”）。
5. 保持（J8）：五个 `roles_*` 移入核心，界限句删去，`roles_dissipative` 的逆也已证明。完成。
6. 分裂（J9、J10）：以“充分”代替“精确”，`split_unceasing` 列入记录，章节补上前提。完成。延续关系上的充要条件，开放。
7. 记账（J11）：六项完成；用语的最终选择属于 Ren。
8. Ren 的选择：在终结之步的汲取是否计入不 living、对哪些汲取者；接续的读法；“生生不息”读到哪个层次；名称（`Depletes` 与“代价”一族）。本节没有替 Ren 作任何一个选择。

### 22.4 作者反审

*反驳 1：`Enclosed` 是不是只为排除 `Spray` 的特设前提？* 它是有限支撑的陈述：一步中参与的形成只与有限个条件交换。条件总共有限时它自动成立（`enclosed_of_finite`），`Frontier`、`Rooted` 与 `Lone` 每步都满足它（P16c 证明：`Frontier.enclosed`、`Lone.enclosed`）。没有它，耗散的定义对那一步什么也不说，这正是 `Spray` 表明的；把它写为前提，是公开 §17 反驳 1 原来默认的东西。

*反驳 2：既然估值看不见体现，一类读法还有什么用？* 体现进入依存的动力学：`coextinct`、`ends_when_consumed`、`arises_given` 与 §20 的 `generation_opens` 都用它。估值看不见的是体现本身；它经由承担自身进入估值（`SelfBearing.interacts`）。两者是不同的后果，不冲突。

*反驳 3：`Wilting` 表明 `ending_breaks` 是一个坏的读法，应当改定义。* 本节不改：是否把在终结之步的汲取计入不 living、对哪些汲取者，属于 Ren。可供选择的读法至少有三种：照现在的读法计入全部汲取者，包括该关系项自身的最后事件；只计入其汲取使它终结者，这需要反事实的关系（P18b 用语，原文“生命自身”“使生命终结者”）；不让自身依存进入断裂，即不采用 `SelfBearing`，如 `Mutualism.apart`。本节只陈述各自的后果。

*反驳 4：把“代价”改为“给予须以取用为条件”，是不是只是换词？* 对，内容相同；理由是 Ren 在 2026-10-06 对支付一族用语的质疑。名称是建议，Ren 可以改回，`Brood.costless` 的改名同理。

*反驳 5：`relabel` 是不是表明一类读法与两类读法没有区别？* 不是。两类读法检查不到同一对应，这正说明同一对应是一类读法另加的内容。它由表示给出，与跨步的同一由命名给出（§16，I7）是同一类前提：标签不承载任何东西，标签的模式承载对应。

**边界。** 不改变读法选择的地位；不推出责任、义务或任何排序；新名称是建议；探针与新见证都是最小见证；同一对应、只有体现者给予与封闭的步是公开的前提；直接读出体现的估值、汲取是否终结它的因果读法、延续关系上的充要条件，开放。本节的更正经第七次独立审查，见 §23（P18b 补记，原文“本节的更正尚未再经独立审查”；用语原文“终结生命”）。

## 23. 第七次独立审查与更正（P16c）

2026-10-09。按同一指示继续。另一 agent（Claude Opus 5.5，未参与撰写）独立审查了 P15（§20）、P16（§21）与 P16b（§22）（[审查](BECOMING-P15-P16-P16B-REVIEW.md)）。它在仓库之外从前导重新编译核心闭包的 22 个模块，1185 条声明的公理报告全空；计数、回执、哈希、别名与证明绑定都对，数学全部接受。J1–J11 中八项关闭，J1 与 J7 关闭而有过强的表述，J11 关闭而有残余。问题共八项（K1–K8），都在前提的陈述、散文与对应之间，没有数学错误；附无公理的探针。审查没有发现替 Ren 选择生、living、接续、终结或“生生不息”的层次；它指出两个模式：耗散空成立时结论可以由无关的交换满足（省略前提，J1 的同一模式），以及把体现读作生命（替 Ren 选择了“生”的读法）。本节记录逐项处理。探针作为定理移入相应模块；审查列为未构造的一步，相等可判定时被封闭的步围住每个有限家族（`Enclosed.around`），也已证明。§17、§20–§22 中受影响的句子已就地更正并标明；原文见提交 `b24963f1`。

```text
Result(s): 修正 generation-is-replenishment（标题、主张、假设 3、对应、反例、界限、别名）、
           no-finite-part-bears-taking（标题、主张、对应、反例、界限、别名）、
           whole-persists-through-generation（标题、主张、假设 2、对应、反例、界限、别名）、
           life-as-condition-of-life（主张、假设、对应、反例、界限）、identity-across-steps（主张、反例、界限）；
           其余 Becoming 记录只改检验范围；不新增结果记录
Delta: 围住（Around：某个包含家族的不重复有限家族跨该步封闭）与只向内（Inward：给予家族的每个参与形成只从家族取用）；
       耗散之下，从某步起被围住而取用复现的家族汲入（taking_draws_in），体现成员的生成同样（generation_draws_in，
       经由 generation_ceases_on）；相等可判定时被封闭的步围住每个有限家族（Enclosed.around）；
       generation_opens 与 Dissipative.opens 的结论可以由与家族无关的交换满足（SprayHanding）；
       Frontier、Lone 与 Kindling 每步被封闭并汲入；给予未被耗散的家族不必取用（Frontier.gives_without_taking）；
       gives_less 需要不重复（Lone.repeated_family）；覆盖（Covered）是部分生成定理的主语，持续的整体被部分覆盖（Whole.covered），
       不断新的部分（needs_new）；整体是活动的重合（whole_self、Immortal.each_other）；Layered 的成员 Brief 1 而反复生起；
       给予它的体现关系项可以是不依存的太阳（EmbodiedSun；P17 用语，原文“体现的给予者”）；Merge 下的生起是持续形成被重读（Merge.idle），被合并者终结的合并（Confluence）
Supplied premises / correspondence: 新增：汲入的读法需要家族被围住，即每步的交换落在包含家族的有限个关系项之内；
       相等可判定时它由封闭的步给出
Evidence: Becoming.Dissipation 72、Roles 131、Wholes 36、Identity 83 项定理；
          合并检查器回执 20261009T083555.066952Z（728 项定理／1182 项声明审计，核心闭包 22 个模块，包 20 个模块，公理报告全空）；
          外围桥接 20261009T083732.465283Z
Boundary: “生”与 living 的读法（体现的关系项是否读作生在内）、接续的读法、在终结之步的汲取是否计入及对哪些汲取者、
          “生生不息”读到哪个层次、名称（Depletes、给予一族的用语、Brood.not_dissipative），属于 Ren
Integration: K1–K8 全部处理；审查 §4 第 1–5 项完成，各留下的开放结果见 23.3；第 6 项属于 Ren
```

### 23.1 逐项处理

| 项 | 审查所见 | 处理 |
|---|---|---|
| K1 | `generation_opens`（与 P13 的 `Dissipative.opens`）的结论“从某步起不封闭”可以由与家族无关的交换满足：`Dissipative` 只约束被封闭的步；一个汇与不断新的关系项交换时，没有一步被封闭，耗散空成立，两方的家族独自承担生成而没有任何东西流入（`SprayHanding`）。P13 的标题“没有有限部分独自承担持续的取用……须与其外交换”与 P15 的生成句子被它反驳 | 两种更正都做。核心新增围住（`Flow.Around`）与只向内（`Flow.Inward`）。`Dissipative.dissipatesOn_of_inward`：耗散之下，在被围住而只向内的步上家族被耗散。`taking_draws_in`：耗散之下，从某步起被围住、取用在任意晚的步复现的不重复有限家族，在任意晚的步有形成给予它而从其外取用。Roles 中 `Embodied.arising_lowers_on` 与 `generation_ceases_on`（从某步起被耗散的家族中体现成员不在任意晚的步生起）推出 `generation_opens` 与 `generation_draws_in`。审查列为未构造的一步也已证明：相等可判定时，被封闭的步围住每个有限家族（`Enclosed.around`，经由 `adjoin`）；条件总共有限时每步围住每个家族（`around_of_finite`）。`SprayHanding` 移入 `Roles`；`Kindling`、`Frontier` 与 `Lone` 是正面见证。两份记录的标题、generation-is-replenishment 的假设 3、两处对应、§17 与 §20 的标题与解读、章节、根模块与检查器的范围文字改为字面结论，加上被围住时的汲入 |
| K2 | “在耗散之下，给予家族者从家族取用”省去“被耗散的家族（封闭、不重复）”（`Frontier.gives_without_taking`） | §20 的解读、英文 P15 段落与章节 §2 补上“被耗散的家族”。`Frontier.gives_without_taking` 移入核心：流耗散，太阳每步给池而不从池取用，池的家族不封闭 |
| K3 | “整体的持续就是部分的生成”主张同一，`Gaps` 反驳它。`Whole` 是活动的重合（`whole_self`、`each_other`），两个定理只用到它的一个方向（`arises_within_of_cover`、`needs_arising_of_cover`）。在 `Brief` 之下生成可以是两个部分反复生起（`Layered`），在 `Ends` 与 `Listed` 之下须有新的部分（`needs_new`）。“张力消失”过强 | 覆盖（`Web.Covered`：从某步起每步有部分活跃）成为两个定理的主语：`Covered.arises_within`、`Covered.needs_arising` 与 `Covered.needs_new`。`Whole.covered` 把持续的整体接到覆盖上，`Whole.arises_within`、`Whole.needs_arising` 与新增的 `Whole.needs_new` 由此推出，陈述不变。`Web.whole_self` 与 `Immortal.each_other` 移入核心，Wholes 的说明改为“一种部分与整体的关系，活动的重合”。“就是”改为“经由／需要”，“构成”删去；§21 的“对生生”按前提重述：Ends 与 Listed 之下是不断新的成员，Brief 之下只是反复生起，两者都不是数目增长 |
| K4 | 记录标题、章节英文 §1、§9 的 Wholes 一行与术语表的“部分不长久”省去 `Listed`，`Countless` 表明它必要 | 记录标题、章节 §1（中英）、§9、术语表、Wholes 的标题与根模块写明“部分短暂，或部分终结且同时活跃的部分有限”；记录假设 2 写明 `Listed` 是有限性前提，不是对长久的陈述 |
| K5 | §21 反驳 3 说 `Layered` 的成员 `Brief` 不成立，这是错的（`layered_brief`、`layered_within`） | 反驳 3 就地改写：`Layered` 的成员 `Brief 1`，`arises_within` 适用；它们不终结，`needs_arising` 不适用；`Brief` 不说部分终结，允许同样的部分反复生起。`Layered.brief`、`Layered.within` 与 `Layered.arise_again` 移入 Wholes。前提不必要的见证（活动段无界增长的部分）没有构造，列为开放 |
| K6 | “生由生”被写为已证明，把体现读作生命；体现的给予者可以是一个只以水平作为条件而在、不依存于任何东西的太阳（`EmbodiedSun`） | `EmbodiedSun` 移入 `Roles`（`embodied_sun`）。§22.1 J7、§22.3 第 4 项、life-as-condition-of-life 的主张、假设、对应与界限，以及 `SunSeed` 的说明改为：在只有体现的关系项给予这一表示前提下，给予它的关系项也体现；体现是作为条件而在的表示，不是是生命的表示；把体现的关系项读作“生”是 AI 读法，属于 Ren。审查可选的局部前提（只要求在该步给予该关系项者体现）没有采用，全局前提照旧公开 |
| K7 | `Merge` 下的不息生起是虚假的：没有形成延续为生长者，持续的生长者每步被读作生起，结论不用更多（`merge_idle`） | `Merge.idle` 与 `Confluence` 移入 `Identity`：被合并的 `a` 在合并之后不活跃，没有分裂，合并下生起的恰是每步的新形成。`merging` 的说明改为“前提在含合并的延续下成立，结论空洞地满足”；Identity 的说明、检查器范围、§22 与记录改正。由更多做功的含合并普查见证与合并迫使重读的计数论证没有构造，列为开放 |
| K8 | 记账与用语八项 | (a) §20 引言的“补充须付出所取”改为“给予须以取用为条件”。(b) 计划的 P15 一行改为 `Brood.not_dissipative` 与字面结论。(c) “给予者／giver”在 Roles、根模块、检查器范围、记录与 §17–§22 的现行文字中改为“给予它的关系项／形成”，假设 `givers` 改名为 `gives_embodied`；引述与更正标记中的原文保留；用语最终属于 Ren。(d) Dissipation 的说明改为“某个参与的形成与无穷多个条件交换的步不被封闭”。(e) `gives_less` 在 §22 的 Delta 与 22.2 补上“不重复”，`Lone.repeated_family` 移入核心。(f) `Frontier.enclosed` 与 `Lone.enclosed` 移入核心，§22.4 反驳 1 有了证明。(g) whole-persists-through-generation 的审查时间与其余四份同时刷新。(h) 英文 P15、P16 段落的“core”改为“package” |

### 23.2 新的已检查声明

| 模块 | 声明 | 内容 |
|---|---|---|
| Dissipation | `Flow.Around`、`Flow.Inward` | 围住：某个包含家族的不重复有限家族跨该步封闭。只向内：给予家族的每个参与形成只从家族取用 |
| Dissipation | `around_of_finite`、`Flow.Enclosed.around` | 条件总共有限时每步围住每个家族；相等可判定时，被封闭的步围住每个有限家族 |
| Dissipation | `Dissipative.dissipatesOn_of_inward`、`Flow.taking_draws_in` | 耗散之下，被围住而只向内的步上家族被耗散；所以从某步起被围住、取用在任意晚的步复现的家族，在任意晚的步有形成给予它而从其外取用 |
| Dissipation | `total_le_of_support`、`decideMem`、`insertNew`、`insertNew_spec`、`adjoin`、`adjoin_spec` | 有限和与列表的辅助：不重复列表上的和不超过列出其正值处的任何列表上的和；相等可判定时列表成员可判定；把一个列表的成员不重复地并入另一个 |
| Dissipation | `Frontier.closed`、`pool_fuel_distinct`、`enclosed`、`around`、`draws_in`、`gives_without_taking` | 前沿每步被池与当步的燃料封闭，围住池，池的家族汲入燃料；太阳给池而不从池取用，池的家族不封闭 |
| Dissipation | `Lone.closed`、`enclosed`、`draws_in`、`repeated_family` | 恒定的取用者每步被封闭，池的家族汲入；列出池两次的家族上太阳所给与所取相等 |
| Roles | `Embodied.arising_lowers_on`、`generation_ceases_on`、`generation_draws_in` | 被耗散家族中体现成员的生起降低存量；从某步起被耗散的家族中体现成员不在任意晚的步生起；被围住的家族中复现的体现生成汲入。`arising_lowers` 与 `generation_opens` 由前两者推出 |
| Roles | `SprayHanding.Relatum`、`flow`、`web`、`sides`、`sides_distinct`、`bound`、`le_bound`、`fresh`、`balances`、`acting`、`dependent`、`unenclosed`、`dissipative`、`even_sum`、`spray_handing`、`opens_anyway`、`taking_opens_anyway` | 两方来回传递，一个汇每步从一个新的辅助关系项取一份又还给它：没有一步被封闭，耗散空成立，生成与取用在两方的家族中复现而没有东西流入，`generation_opens` 与 `Dissipative.opens` 的结论由汇满足，没有一步围住两方 |
| Roles | `Kindling.around`、`Kindling.draws_in` | 两方的家族每步被两方与所燃的燃料围住，在任意晚的步给予它的一方从燃料取用 |
| Roles | `EmbodiedSun.web`、`balances`、`acting`、`gives_embodied`、`embodied_sun` | 太阳的水平取一：`arises_from_embodied` 的全部前提成立而它命名不依存于任何东西的太阳 |
| Wholes | `Web.Covered`、`Covered.arises_within`、`Covered.needs_arising`、`Covered.needs_new`、`Whole.covered`、`Whole.needs_new` | 部分覆盖从某步起的每一步时，两个定理与不断新的部分；持续的整体被部分覆盖 |
| Wholes | `Web.whole_self`、`Immortal.each_other` | 每个形成是它自身的整体；两个每步都活跃的形成互为整体 |
| Wholes | `Layered.brief`、`Layered.within`、`Layered.arise_again`（`Layered.composed` 移入同一命名空间） | `Layered` 的成员 Brief 1，每步都有成员生起，每次生起是两者之一，它们的活动不终结 |
| Identity | `Merge.idle` | 合并下第一个生长者每步被读作生起，结论不用更多；每个形成只延续自身时它只在第零步生起 |
| Identity | `Confluence.Formation`、`web`、`continues`、`ended`、`noSplit`、`confluence` | 被合并的形成终结的合并：没有分裂，合并下生起的恰是每步的新形成 |

### 23.3 审查列出的会改变判断的结果

1. 汲入（K1、K2）：`Around` 与汲入定理移入核心，以 `Kindling` 与 `Frontier` 为见证；标题改为字面结论，`SprayHanding` 列入记录，假设 3 改正；“被耗散的家族”在三处补上。两种做法都完成。不以围住为前提的汲入（交换越出每个有限家族的步上）没有陈述，开放。
2. 整体（K3–K5）：“需要／经由”，`needs_new` 与覆盖形式，按前提重述“张力”，标题与术语表加入 `Listed`，反驳 3 改正，`Whole` 写为活动的重合。完成。前提不必要的见证，开放。
3. 给予（K6）：“生由生已证明”删去，写为“在只有体现的关系项给予这一前提下，给予它的关系项体现”，体现的关系项是否读作“生”留给 Ren。完成。
4. 合并（K7）：`Merge` 改正说明，`Confluence` 是被合并者终结的见证。完成。由更多做功的含合并普查见证，开放。
5. 记账（K8）：八项完成；用语的最终选择属于 Ren。
6. Ren 的选择：“生”与 living 的读法（体现的关系项是否读作生在内）、接续、“生生不息”读到哪个层次、在终结之步的汲取是否计入及对哪些汲取者、名称（`Depletes`、给予一族、`Brood.not_dissipative`）。本节没有替 Ren 作任何一个选择。

### 23.4 作者反审

*反驳 1：围住是不是又一个为排除反例而加的前提？* 它是 §22 的 `Enclosed` 对一个家族的形式：一步中参与的形成只与包含该家族的有限个条件交换。相等可判定时，任何被封闭的步都围住每个有限家族（`Enclosed.around`），所以它没有在“交换有限”之外多要求什么。`SprayHanding` 表明，没有它，“须从其外汲入”就不成立：耗散空成立时，有限家族可以独自承担生成，结论由与它无关的交换满足。

*反驳 2：既然 `Whole` 只是活动的重合，部分与整体的关系还有什么内容？* 内容在覆盖：部分在每步接上，整体才每步活跃。定理用到的正是覆盖（`Covered`），整体只是给覆盖一个名字。这也说明了为什么整体的依存与侵蚀没有从部分推出（§21 反驳 2）：活动的重合不承载依存。构成的关系需要别的表示，开放。

*反驳 3：“生生不息”在整体层次上读，是否就不再要求“不断创造”？* 看前提。部分终结且同时活跃的部分有限时，整体的持续要求不断有新的部分生起（`needs_new`），这是一种“不断创造”；部分只是短暂时，同样的部分反复生起就够了（`Layered`）。两者都不要求数目增长，所以“更多”没有由整体的持续推出。读到哪个层次，仍属于 Ren。

*反驳 4：既然 `arises_from_embodied` 不证明“生由生”，一类读法对生命还说了什么？* 它说的是关系项作为条件而在的结构：依存于体现关系项的形成只在它活跃时活跃（`active_of_bearing`、`coextinct`；P18b 更正，原文“生命以其他生命为条件”），体现的生起由另一个活跃者的给予承担（`arises_given`），在只有体现者给予的表示中给予它的也体现。哪些体现的关系项是生命，是对“生”的读法，属于 Ren；`EmbodiedSun` 表明这一读法不由定理给出。

**边界。** 不改变读法选择的地位；不推出责任、义务或任何排序；新名称是建议；探针与新见证都是最小见证；围住是汲入读法公开的前提；不以围住为前提的汲入、前提不必要的见证、由更多做功的含合并普查见证与构成的关系，开放。本节的更正经第八次独立审查，见 §27。

## 24. 储备：活动越过支持，水平越过活动（P17）

2026-10-09。按同一指示继续。开放纲领自 P6 起在“动态依存”一行列出“放宽 `Dependent`（缓冲、储备、滞后）”；§18 写明种子库、储备与休眠被 `Dependent` 排除，在它们之下共灭不必成立；§20 反驳 5 写明活动与水平不同步（种子、休眠）时生成承担什么是下一步。两处的共同点是所持之物：活动可以越过支持，靠所持的储备；水平可以越过活动，如休眠的种子。按非二元方法，在流与所持条件被表示的地方，储备不作为新的原语：它是形成所持的一个条件的水平；没有表示所持条件时，储备是给定的量（P18b 更正，原文“储备不作为新的原语：它是形成所持的一个条件的水平”；见 §27 L4）。本节陈述储备承担什么，并把 §20 与 §23 的结论推到它们实际用到的东西上：生起的关系项开始作为条件而在。成果记录：[reserve-defers-ending](../../../../theories/becoming/results/records/reserve-defers-ending.md)；[generation-is-replenishment](../../../../theories/becoming/results/records/generation-is-replenishment.md) 随之推广。

```text
Result(s): 复用 becoming-dependence-dynamics（Supported、Dependent、consumed_ends_when_fixed、arises_at_a_step）、
           becoming-renewal-reading（falls_finitely）、life-as-condition-of-life（Embodied、coextinct）、
           more-needs-renewers（流、平衡）；新增 reserve-defers-ending（L3 Becoming.Reserve）；
           推广 generation-is-replenishment（ComesToStand 移入 Flow 与 Dissipation，§20 与 §23 的体现定理改由它推出）
Delta: 储备（Carries）：不被支持时不上升，活跃时下降；零储备恰是 Dependent（carries_zero）；
       储备可以是所持条件的水平（Flow.carries_of_held；P18b 更正，原文“储备是”）；依存失效而活跃时储备为正（Carries.pos）；
       从某步起不被支持，只在有限多步活跃，次数不超过开始时的储备（active_finitely、lasts、lasts_within）；
       滞后的终结与滞后的共灭（consumed_lasts、coextinct_lasts）；不被支持时休眠只推迟生起（arising_finitely），储备在休眠中衰减时休眠在时间上有界（Decays、ends_within）；
       开始作为条件而在（Web.ComesToStand）：平衡的流中被给予新水平（Balances.standing_given），
       在家族中复现时补充复现（standing_needs_replenishment）；降低被耗散家族的存量，从某步起被耗散的家族中不复现
       （standing_lowers_on、standing_lowers、standing_ceases_on）；耗散之下在不重复有限家族中复现时，家族在任意晚的步不封闭，
       被围住时汲入（standing_opens、standing_draws_in），条件总共有限时不复现（standing_ceases）；
       体现的生起就是开始作为条件而在（Embodied.comesToStand、Embodied.coming）；
       活跃时作为条件而在的关系项，若先前某步不在，就在其间某步开始作为条件而在（came_to_stand）；
       见证 Seed、Viable、Famine（含依存转化的读法）、Sleeper、Provisioned
Supplied premises / correspondence: Carries 是表示前提，哪个条件是一个形成所持的由应用给出；carries_of_held 需要平衡、
       不被支持时没有给予所持条件、活跃时从中取用；Carries.lasts 需要活动可判定（定理的假设，不是公理）；Decays 是另设的表示前提，只用于 ends_within；物理内容是所持之物有限
Evidence: Becoming.Reserve 35 项定理；Flow 新增 4 项（含自 Dissipation 移入的 eq_zero_of_not_pos）、Dissipation 新增 6 项（移出 1 项）、Roles 新增 2 项；
          合并检查器回执 20261009T090231.312129Z（774 项定理／1257 项声明审计，核心闭包 23 个模块，包 21 个模块，公理报告全空）；
          外围桥接重跑 20261009T090346.438363Z
Boundary: 结论约束从某步起不被支持的形成，不约束支持是否回来；Carries 之下休眠不耗用储备，休眠的时间只在 Decays 之下有界；沿依存链的滞后没有陈述；
       不含伦理谓词
Integration: 回答开放纲领“放宽 Dependent（缓冲、储备、滞后）”、§18 共灭的范围与 §20 反驳 5；§20 与 §23 的体现定理成为
       开始作为条件而在的特例
```

[Becoming.Reserve](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Reserve.lean)（L3，导入 `Becoming.Roles`），以及 [Becoming.Flow](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Flow.lean)、[Becoming.Dissipation](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Dissipation.lean) 与 [Becoming.Roles](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Roles.lean) 新增的声明：

| 声明 | 内容 |
|---|---|
| `Web.Carries`、`carries_zero` | 储备：在形成不被支持的一步上不上升，若它在该步活跃则下降。零储备恰是 `Dependent` |
| `Flow.carries_of_held`、`Carries.pos` | 平衡的流中，持有者不被支持时没有给予、持有者活跃时被（参与的任何形成）取用的条件，以其水平承载持有者（P18b 更正，原文“活跃时被它取用”）。依存失效而仍活跃的形成储备为正 |
| `Carries.active_finitely`、`Carries.step`、`Carries.lasts`、`Carries.lasts_within`、`mark`、`mark_cases` | 从某步起不被支持的形成只在有限多步活跃；在任一段步上，活跃的次数加上结束时的储备不超过开始时的储备；容量为 k 时活跃至多 k 次 |
| `unsupported_after_loss`、`Carries.consumed_lasts` | 没有回程而依存不变的损失之后，形成不再被支持，靠储备只在有限多步活跃（滞后的终结） |
| `unsupported_after_end`、`Carries.coextinct_lasts` | 体现的关系项终结之后，以正需要依存于它的形成不再被支持，靠储备只在有限多步活跃（滞后的共灭） |
| `Carries.arising_finitely` | 从某步起不被支持的形成只在有限多步生起：休眠推迟终结而不逃脱 |
| `Web.Decays`、`Carries.decays_by`、`Carries.ends_within` | 储备衰减：在形成不被支持而储备为正的每一步都下降，不论形成是否活跃（种子的存活力）。从某步起不被支持，经过 n 步后储备已下降 n 或已耗尽；经过与开始时储备一样多的步之后，形成不再活跃：休眠在时间上也有界 |
| `Web.ComesToStand`、`Balances.standing_given`、`Balances.standing_replenishes`、`standing_needs_replenishment`（Flow） | 开始作为条件而在：此前水平为零，此后为正。平衡的流中至少被给予新的水平，于是补充每个包含它的家族；家族的成员在任意晚的步开始作为条件而在时，家族的补充复现，不论取用什么 |
| `standing_lowers_on`、`standing_lowers`、`standing_ceases_on`、`standing_opens`、`standing_draws_in`、`standing_ceases`（Dissipation） | 被耗散家族的成员开始作为条件而在，降低家族的存量（给予它的形成从家族取用更多）；耗散之下，跨该步封闭的不重复家族正是如此。从某步起被耗散的家族中，成员不在任意晚的步开始作为条件而在。耗散之下，成员在任意晚的步开始作为条件而在的不重复有限家族，从任何一步起都不封闭；从某步起被围住时，它汲入：在任意晚的步有形成给予它而从其外取用；条件总共有限时，没有条件在任意晚的步开始作为条件而在 |
| `Embodied.comesToStand`、`Embodied.coming`（Roles） | 体现的关系项在生起时开始作为条件而在；§20 与 §23 的 `given_of_arises`、`replenishes`、`generation_needs_replenishment`、`arising_lowers_on`、`generation_ceases_on`、`generation_opens`、`generation_draws_in` 与 `generation_ceases` 改由上述一般定理推出，陈述不变；`arising_lowers` 经由 `arising_lowers_on` |
| `came_to_stand` | 活跃时作为条件而在的关系项，在某步没有水平而在后来某步活跃，就在其间某步开始作为条件而在 |
| `Seed.web`、`dark`、`carries`、`seed` | 黑暗中的种子以需要一依存于光，在第 1 与第 3 步醒来：不满足 `Dependent`，储备承载它，它生起两次后不再活跃，醒着的次数恰等于开始时的储备 |
| `Seed.not_decays`、`Viable.viability`、`web`、`dark`、`carries`、`decays`、`viable` | `Seed` 的储备在休眠中保持，不衰减；存活力为三、每步下降的种子在黑暗中第 2 步醒来，第 3 步起不再活跃：不满足 `Dependent`，`ends_within` 的时间界可以达到 |
| `Famine.web`、`flow`、`hold`、`balances`、`carries`、`hare_embodied`、`transformed`、`transformed_dependent`、`famine` | 狐依存于体现的兔，兔在第 0 步之后终结；狐的脂肪是流中的条件，狐在第 1、2 步各燃一单位。流平衡，脂肪承载狐，狐恰好多活两步；把狐的依存读作在兔终结后转到脂肪上，同一展开满足 `Dependent` |
| `Sleeper.web`、`flow`、`sleeper` | 一个关系项始终以水平一作为条件而在，在奇数步醒来；流中没有形成参与，流平衡，耗散空成立，`Dependent` 成立，生成不息而没有任何给予；它不体现，也从不开始作为条件而在 |
| `Provisioned.web`、`flow`、`balances`、`acting`、`provisioned` | 父代在第 0 步给予种子一单位，种子休眠一步，从第 2 步起活跃：种子在休眠时开始作为条件而在，被给予它的水平；它在第 1 步生起时没有任何给予 |
| 其余（`Seed.wake`、`reserve`、`Famine.Relatum`、`hare`、`fat`、`eats`、`burns`、`present`、`source`、`supported_of_ne_fox`、`fed`、`Provisioned.Relatum`、`late`、`gift`） | 见证的辅助定义与引理；`eq_zero_of_not_pos` 自 Dissipation 移入 Flow |

**解读。**

- **`Dependent` 是零储备。** “活动只在有支持处”与“储备为零”是同一个陈述（`carries_zero`）。放宽它不是让活动离开依存，而是允许所持的储备。§6 以来依赖 `Dependent` 的结论（损失的三种结局、共灭、替代）都是零储备的情形；有储备时，它们推迟而不消失。
- **储备可以是所持的条件（P18b 更正，原题“储备是所持的条件”）。** 在平衡的流中，一个条件在持有者不被支持时没有给予、在持有者活跃时被取用，它的水平就是储备（`carries_of_held`）；没有表示所持条件时，储备是给定的量（§27 L4，`Seed.no_held`）。依存失效而仍活跃的形成，储备为正：对所持之物、需要为一的依存被满足。所以在所持条件承载它的地方有两种表示：依存于兔而有储备（不满足 `Dependent`），或依存在兔终结后转到脂肪上（满足 `Dependent`，`Famine.transformed_dependent`）。在那里，滞后就是依存转化到所持的条件上，这是 §6 `consumed_continues_transformed` 所说的转化的一种；它是对储备的重新描述，两种表示在 living 上不同（§27 L6）。缓冲不在依存之外。
- **推迟而不逃脱。** 从某步起不被支持的形成只在有限多步活跃，次数不超过开始时的储备（`lasts`）。没有回程的损失之后（`consumed_lasts`）与所依存的体现关系项终结之后（`coextinct_lasts`），形成在支持之外至多再活跃其储备那么多次；`Famine` 中狐恰好多活两步，即脂肪的两单位。这与 §13 的“替代推迟终结而不逃脱”（`substitution_defers`、`Relay`）是同一模式：所推迟的靠一个不再被补充的条件。休眠同样：不被支持时，醒来只有有限多次（`arising_finitely`、`Seed`）。`Carries` 只在活跃时耗用储备，所以休眠本身可以任意长；储备在休眠中也衰减时（种子的存活力），经过与储备一样多的步之后形成不再活跃（`ends_within`、`Viable`）。
- **生成承担补充，在开始作为条件而在之处。** §20 与 §23 用到的体现只有一点：水平跨生起之步上升，体现时从零上升（P18b 更正，原文“生起时水平从零上升”；见 §27 L7，一般的定理对任何上升陈述）。所以一般的定理在条件上：任何条件开始作为条件而在，在平衡的流中都被给予它的新水平；在耗散之下，在不重复有限家族中复现，家族就在任意晚的步不封闭（`standing_opens`），这一交换可以与家族无关（§23 的 `SprayHanding`），家族被围住时它汲入（`standing_draws_in`）。体现的关系项在生起时开始作为条件而在（`Embodied.comesToStand`），§20 与 §23 关于体现的九个定理都由此推出。这把要求放在它实际所在之处：不在活动的上升，而在水平的上升。
- **水平越过活动。** 活跃时作为条件而在的关系项，若先前某步不在，就在活跃之前开始作为条件而在（`came_to_stand`），可以早得多：种子在休眠时被父代给予它的水平，此后生起时没有任何给予（`Provisioned`）。从休眠中醒来是生起而不开始作为条件而在：一个始终作为条件而在的关系项可以不息地醒来，不需要任何给予（`Sleeper`；它的流中没有形成参与，耗散空成立，所以这里没有陈述耗散的世界中醒来会怎样）。所以对生起的约束在两头：开始作为条件而在需要补充；醒来若耗用所持的储备而没有支持，只有有限多次。两者都不约束靠回来的支持而醒来。
- **对生生（作者的读法）。** Ren 的原话是“生生不息 - 一种整体的，不断创造更多生的方向”。所持之物使一个形成越过它的支持延续，也使一个关系项在它的活动之前就已作为条件而在。这里读出的是：没有支持，所持之物只推迟终结；不断的生起若是关系项开始作为条件而在，就需要不断的补充。把这些形成与关系项读作“生”属于 Ren（§23 K6）。作者把这读作“不息”不能由所持之物独自承担的一种形式内容（AI 论证），不替代原话，不推出它是好的，也不决定生生读到哪个层次。

**作者反审。**

*反驳 1：`Carries` 只是把 `Dependent` 换成一个更弱的前提，没有说明什么。* 它说明 `Dependent` 是零储备，并给出储备的数量后果：延续至多是开始时的储备，界可以达到（`Seed`、`Famine`）。它也说明储备不是新的原语：它可以是流中所持条件的水平（`carries_of_held`）。

*反驳 2：依存转化的读法是否只是把结论编进表示？* 两种表示的水平、活动、汲取与流都相同，只是依存于什么不同。`Famine` 证明两种读法都成立；哪一种更合适，取决于应用把脂肪读作狐的一部分还是狐所依存的另一个条件。（P18b 更正，原文“两种表示描述同一展开”与“一般地构造转化的读法需要“是否被支持”可判定，这里只给出见证”：两种读法的 living 不同，狐在第 1 步的事件按原读法侵蚀、按转化的读法不侵蚀（`Famine.living_differs`），所以选择不是对估值中立的，是对应前提；一般的构造已给出（`Web.redirect_dependent`），它满足 `Dependent` 由构造给出，是对储备的重新描述。见 §27 L6。）

*反驳 3：休眠不耗用储备，这不太强了吗？* 是一个选择：`Carries` 只要求活跃时下降，所以只靠它，休眠可以任意长。衰减是另一个前提（`Decays`）：在它之下休眠的时间有界（`ends_within`），`Viable` 达到这个界；`Seed` 表明 `Carries` 不蕴含衰减（`Seed.not_decays`）。两者分开陈述，应用选择哪一个。

*反驳 4：`ComesToStand` 的推广是否平凡？* `standing_given` 几乎由平衡直接给出，就像 §20 的 `given_of_arises`。内容在于定位：§20 与 §23 的结论用到的不是体现，而是水平上升，体现时从零上升（P18b 更正，原文“水平从零上升”）；`Sleeper` 与 `Provisioned` 表明，活动与水平不同步时，要求跟着水平走，而不跟着活动走。§23 的更正（开放的交换可以无关，汲入须家族被围住）原样适用于开始作为条件而在。

*反驳 5：狐“多活两步”只是见证里写定的时程。* 对，见证写定了活动；定理说的是任何满足前提的展开都至多如此，`Famine` 表明界可以达到，`Seed` 表明在休眠与醒来交替时也如此。

*反驳 6：`Sleeper` 的耗散是空的，它没有说明耗散的世界中的休眠。* 对。`Sleeper` 只表明 §20 的结论不约束不开始作为条件而在的生起；没有支持时，醒来所耗用的是 `Carries` 陈述的储备，不是补充；储备与耗散的关系这里没有陈述。（P18b：反驳 5 与 6 的次序按编号排列。）

**边界。** 不含伦理谓词；`Carries` 与所持的条件是表示前提，物理内容是所持之物有限；结论约束从某步起不被支持的形成，不约束支持是否回来；`Carries` 之下休眠不耗用储备，休眠的时间只在另设 `Decays` 时有界；开放与汲入沿用 §23 的形式：开放可以由无关的交换满足，汲入须家族被围住；沿依存链的滞后共灭没有陈述（P18b 更正，原文“沿依存链的滞后共灭、一般的转化读法没有陈述”：一般的转化读法见 §27 L6）；见证都是最小见证。本节经第八次独立审查，见 §27。

## 25. 世系：关系项经由所依与所给直接相关（P18）

2026-10-09。按同一指示继续。§18 记下：两种估值只经由共同的条件关联事件，所以体现不进入估值；只依存于对方的蜂与花都体现、互相依存，却不相关（`Mutualism.apart_embodied`）。life-as-condition-of-life 把“直接读出体现的估值（把汲取者与它所汲取的体现关系项的事件关联）”列为下一步。另一方面，`Becoming.Metaethics` 把 `related` 读作形成的关系，明列条件、依存、世系与合作；此前没有任何读法给出世系，而世代各由前一代给予的 `Brood` 在两种估值下完全不相关。本节在一类关系项的读法中给出两种直接的关系，并陈述它们对 G0 的传递意味着什么。成果记录：[living-on-and-descent](../../../../theories/becoming/results/records/living-on-and-descent.md)。

```text
Result(s): 复用 condition-correspondence-discipline（Interacts、Bearing、interaction、Connected.transfer、relabel_*_connected）、
           life-as-condition-of-life（一类读法、Embodied、arises_given、active_of_bearing、relabel、Brood、Mutualism.apart）、
           generation-is-replenishment（ComesToStand、Embodied.comesToStand、Provisioned、Sleeper）、
           metaethical-core-characterization（Valuation、transmits、significant_iff）；新增 living-on-and-descent（L4 Becoming.Descent）
Delta: 以之为生（LivesOn：在某步汲取一个关系项并以正需要依存于它）与世系（Descends：参与某步并在该步给予一个关系项、它跨该步开始作为条件而在；
       P18b 更正，原文不要求参与），作为交互之外的两种 related（sustenance、descent）；以之为生不是免费的（LivesOn.stands；LivesOn.active 另需体现；P18b 更正）；在 N_rel 之下沿两者的传递
       （living_on_reaches、lived_on_reaches、descent_reaches、ancestry_reaches）；平衡且 Acting 的流中生起的体现关系项从给予它的形成而来，
       珍视那个形成到达生起者的活的事件（Embodied.descends、arisen_reached）；世代由世系连通，G0 在那里有刻画（Brood.descended）；
       同一对应进入以之为生（Mutualism.relabel_sustenance）；世系跟着水平走（Provisioned.descends、Sleeper.no_descent）
Supplied premises / correspondence: 两种关系是 related 的候选读法，是否算作 N_rel 所传递的形成关系由 Ren 选择；N_rel 仍是前提；
       一类读法的同一对应由共同的索引给出；arisen_reached 需要平衡、Acting 与体现
Evidence: Becoming.Descent 的 25 项定理；合并检查器回执 20261009T091503.719598Z（799 项定理／1286 项声明审计，核心闭包 24 个模块，
          包 22 个模块，公理报告全空）；外围桥接重跑 20261009T091616.753919Z
Boundary: 不改变 living 与 C，不推出生起是好的或应当带来新的生起；世系使两个关系项的所有事件相关，不排定时间；给予的形成不必体现；
       只对逐步读法陈述；不含伦理结论
Integration: 回答 life-as-condition-of-life 的下一步与 §18 的 Mutualism.apart；给出 Metaethics 所列“世系”的第一种读法
```

[Becoming.Descent](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Descent.lean)（L4，导入 `Becoming.Correspondence` 与 `Becoming.Reserve`）：

| 声明 | 内容 |
|---|---|
| `Web.LivesOn`、`Web.sustenance`、`interaction_sustenance` | 以之为生：一个形成在某步汲取一个关系项，并以正需要依存于它。这样的事件与该关系项的每个事件相关；与交互合起来是 `sustenance`，它扩展交互的连通 |
| `LivesOn.active` | 以之为生不是免费的：在 `Dependent` 之下，活跃的形成以之为生的关系项若体现，就在该步活跃（P18b 更正，原文“只以在该步活跃的体现关系项为生”；体现是定理的假设，`Dependent` 本身给出的是 `LivesOn.stands`，见 §27 L8） |
| `living_on_reaches`、`lived_on_reaches` | 在 N_rel 之下，珍视一个以某关系项为生的事件，就珍视该关系项的每个活的事件；珍视该关系项的任一事件，就珍视以它为生的每个活的事件 |
| `Flow.Descends`、`Flow.descent`、`interaction_descent` | 世系：一个关系项从一个形成而来，当后者参与某步、在该步给予它，而它跨该步开始作为条件而在（P18b 更正，原文“当后者在某步给予它”，不要求参与；见 §27 L10）。世系使两个关系项的每个事件相关；与交互合起来是 `descent` |
| `descent_reaches`、`ancestry_reaches` | 在 N_rel 之下，珍视一个形成的任一事件，就珍视由它而来的关系项的每个活的事件，反之亦然 |
| `Embodied.descends`、`arisen_reached` | 在平衡且只有活跃形成给予的流中，生起的体现关系项从在该步活跃的另一个形成而来；于是在 N_rel 之下，珍视那个形成的任一事件，就到达生起者的每个活的事件 |
| `Brood.descended`（及 `birth_next`、`descends`、`alive_of_stands`、`self_alive`、`down`、`up`、`descent_connected`、`participates`、`not_coparticipating`、`not_interacting`） | 世代各由前一代给予：世系使它们连通，共同参与与交互都不连通它们；G0 在那里恰等于种子加 N_rel 加 N_std |
| `Mutualism.apart_sustenance_connected`、`other_other`、`relabel_sustenance` | 只依存于对方的蜂与花由以之为生连通；把它们的条件互换，共同参与与交互的连通不变（都不连通），以之为生的连通消失 |
| `Provisioned.descends`、`Sleeper.no_descent` | 种子从在它休眠时供给它的父代而来，此后生起时没有给予；从休眠中醒来不从任何形成而来，而生成不息 |

**解读。**

- **一类读法提供的关系。** 两类的表示中，形成与条件分开，所以事件只能经由一个共同的条件相关。一类读法中，一个形成所依的条件可以就是另一个关系项。以之为生与世系是这一读法才有的关系：前者是一个形成所依、所取的关系项，后者是一个关系项开始作为条件而在时所由来的给予。它们不是加在展开之外的东西，而是同一展开中已经有的汲取、依存与给予，在“哪个条件就是哪个关系项”的对应之下的读法。所以它们依赖这一对应（`relabel_sustenance`）：§22 J4 写明同一对应是表示的前提，J5 写明体现不进入两种估值；这里一类读法的同一对应第一次进入估值，`sustenance` 与 `descent` 的定义不含体现（P18b 更正，原文“这里体现第一次进入估值，正是经由这一对应”；见 §27 L9）。
- **不是免费的连通。** 交互要求依存能落空，以之为生同样要求实际的汲取与正需要的依存：在 `Dependent` 之下，所依的关系项在该步作为条件而在（`LivesOn.stands`），它体现时在该步活跃（`LivesOn.active`）（P18b 更正，原文“只能以在该步活跃的体现关系项为生”）。世系要求参与该步的形成正的给予与开始作为条件而在，空的给予与不参与者的给予项都不造成它（P18b 更正，原文“世系要求正的给予与开始作为条件而在，空的给予不造成它”：原定义不看给予者是否参与，不参与者的给予项曾造成世系，见 §27 L10）。所以 §10（P9）排除的免费连通没有回来。
- **珍视的传递。** 在 N_rel 之下，珍视狐的进食就到达兔的活；珍视兔的任一事件也到达以兔为生的狐的活的事件（`living_on_reaches`、`lived_on_reaches`）。这与 §12（P9b）的 `drawing_reaches` 同构：传递由使用承担，不由侵蚀承担。世系的传递沿着给予：生起的体现关系项总有一个给予它的活跃形成（§18 的 `arises_given`），所以珍视那个形成到达生起者的活的事件（`arisen_reached`）。
- **世系使世代成为一个整体。** `Brood` 的每一代只依存于自身、什么也不汲取，所以在共同参与与交互下各自孤立；世系使它们连通，于是 G0 在那里的刻画适用（`Brood.descended`）。在把体现的关系项读作“生”这一属于 Ren 的读法下（§23 K6），作者把它读作原话中两个“生”之间关系的一种形式内容：生起者由给予它的展开而来，并经由世系与整体相关（AI 论证）。这不替代 Ren 的原话，也不推出生起是好的：`living` 与 C 都没有改变。
- **世系跟着水平走。** 世系的定义用开始作为条件而在，不用生起：种子从在它休眠时供给它的父代而来（`Provisioned.descends`），从休眠中醒来不从任何形成而来（`Sleeper.no_descent`）。这与 §24 的结论一致：生成承担补充，在水平上升处。

**作者反审。**

*反驳 1：这只是把想要的连通写进 related。* 一个读法确实可以让任何东西连通；§10 正因此加了纪律。这里的两种关系都受同一纪律约束：以之为生要求能落空的依存，世系要求参与者实际的给予与开始作为条件而在（P18b 更正，原文“实际的给予”）；`Brood` 与蜂、花的结论是在这些约束下得到的。是否采用它们，是 Ren 的对应选择；本节陈述采用之后会怎样。

*反驳 2：世系使两个关系项的所有事件相关，太粗了。* 是一个选择。只把给予的那一步与生起者相关，会使父代的其他事件与后代无关（`Brood` 中第 0 代在第 5 步的事件就孤立了；P18b 补记：这一例子在更正后的定义下成立，第 0 代只参与第 0 步；原定义下第 0 代在第 5 步对第 6 代的给予项也造成世系，见 §27 L10）。世系作为关系项之间的关系，与 Metaethics 所列的世系（descent）一致；按时间排定的版本列为下一步。

*反驳 3：太阳给予种子也算世系，这不是“世系”。* 对，`Descends` 不要求给予的形成体现（§22 J7 的 `SunSeed`；§23 K6 的 `EmbodiedSun` 表明体现也不使它成为生命）。名称取 Metaethics 的用语，由 Ren 定；更窄的读法（只在给予的关系项体现时）可以由 `arises_from_embodied` 得到，没有单独陈述。

*反驳 4：这让 G0 珍视带来新的生起吗？* 不。G0 珍视活的主张；这里只是说，若世系算作形成的关系，珍视给予的形成的立场就到达生起者的活的事件。带来新的生起是否使结果更好是 C 的问题，`living` 与 C 都没有改变。

**边界。** 不含伦理谓词；不改变 `living` 与 C；两种关系是 `related` 的候选读法，是否采用属于 Ren；世系不排定时间，给予的形成不必体现，以之为生不问汲取的效果；依赖一类读法的同一对应；只对逐步读法陈述；见证都是最小见证。本节经第八次独立审查，见 §27。

## 26. 变化的规律：不加前提，开始成立与不再成立同步（P19）

2026-10-09。Ren 的新指示：“aim a complete theory of becoming, and finish related work”（[来源](../../../../sources/15-codex-theory-conversations/2026-10-09-complete-theory-of-becoming.md)）。计划第 9 节把“完整”读作四项可检查的内容（AI 的读法），第二项是：对每个展开成立的规律不加任何关于展开的前提而证明，其余每条规律写明它的前提。此前各模块的规律都在前提之下：`Dependent`、`Balances`、`Taking`、`Dissipative`、`Embodied`、`Carries`。本节陈述不需要这些前提的部分，并检查其中是否有实质内容，而不只是定义的重述。成果记录：[coming-and-ceasing-keep-pace](../../../../theories/becoming/results/records/coming-and-ceasing-keep-pace.md)。

```text
Result(s): 复用 unceasing-generation-needs-renewal（Arises、Unceasing、Rises、Falls、total）、becoming-renewal-reading（falls_finitely）、
           becoming-dependence-dynamics（Forms、Dissolves、Supported）、more-needs-renewers（steps 与 total 的引理）、
           generation-is-replenishment（ComesToStand）；新增 coming-and-ceasing-keep-pace（L3 Becoming.Change）
Delta: 开始成立与不再成立（ComesToBe、CeasesToBe），四种读法（Web.change_readings）；persists；支持只经由关系改变（Web.supported_of）；
       一段步上的升降相抵（over_stretch、family_over_stretch）；下限与上限（fallen_within、risen_within、rising_recurs、falling_recurs、
       Web.falls_need_rises、falls_finitely_from_floor）；有限家族中开始成立与不再成立同步（held_over_stretch、keep_pace、coming_recurs_iff），
       读于活动（Web.activity_over_stretch、Web.arising_recurs_iff、Web.unceasing_iff）与水平（Web.standing_recurs_iff）；无限家族的见证（Dawn、Dusk）
Supplied premises / correspondence: 没有关于展开的前提；表示的方法承诺：离散的步、自然数的量、计数时的可判定性（活动的可判定性是相关定理的假设，
       水平是否为正总可判定）；家族有限
Evidence: Becoming.Change 的 42 项定理；合并检查器回执 20261009T095726.865589Z（841 项定理／1342 项声明审计，核心闭包 25 个模块，
          包 23 个模块，公理报告全空）；外围桥接重跑 20261009T100002.522708Z
Boundary: 不含伦理结论；同步是数目的同步，不说明哪个形成生起或止息，也不说明为什么；“复现”不给出频率；不把形式规律当作现实的必然性；
       生生不息在哪个层次读、中文用语与名称由 Ren 定
Integration: 计划第 9 节第二项的第一部分；Renewal 的下降原则是一个量的下限；Generation、Flow、Dissipation 的更新规律是前提加这里的下限
```

[Becoming.Change](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Change.lean)（L3，导入 `Becoming.Flow`；`Becoming.Population` 改为导入它）：

| 声明 | 内容 |
|---|---|
| `ComesToBe`、`CeasesToBe`、`Web.Ceases`、`Web.CeasesToStand`、`Web.change_readings` | 一个规定跨一步开始成立（之前不成立、之后成立）或不再成立。形成的生起与止息、依存的形成与消解、条件开始与不再作为条件而在，是这同一种变化分别读于活动、依存与水平（都是 `Iff.rfl`） |
| `persists` | 可判定的规定在某步成立、此后没有一步不再成立，就一直成立。`Dependence` 的 `ceases_at_a_step` 是它不用可判定性的否定形式 |
| `Web.supported_of` | 支持只经由关系改变：一个形成在某步被支持，在另一步仍被支持，只要它在后者的每个依存在前者都有、所需不更大、条件的水平不更低 |
| `excess`、`rise`、`fall`、`across`、`over_stretch` | 任一步上，量在之后加其下降，等于在之前加其上升；任一段步上，终点加其间的全部下降等于起点加其间的全部上升。`excess` 用递归定义，不用自然数减法 |
| `risen`、`fallen`、`family_over_stretch` | 有限家族的总量连同成员的升降也是如此 |
| `fallen_within`、`rising_recurs`、`Web.falls_need_rises` | 量不低于零：有限家族在一段步上的下降至多比上升多出起点的总量，所以成员在任意晚的步下降就在任意晚的步上升；读于条件的水平，每个展开中有限多个条件持续下降就持续上升 |
| `falls_finitely_from_floor` | `Renewal` 的 `falls_finitely`（从某步起不上升的观测量只下降有限次）是一个量的下限 |
| `risen_within`、`falling_recurs` | 量有界时，有限家族的上升至多比下降多出每个成员的界，所以在任意晚的步上升就需要在任意晚的步下降 |
| `mark`、`mark_cases`、`mark_le_one`、`mark_pos`、`mark_iff`、`excess_mark`、`rise_mark`、`fall_mark` | 一个可判定的规定计 1 或 0；它的上升恰是开始成立，下降恰是不再成立。`mark` 与 `mark_cases` 从 `Reserve` 移来 |
| `comings`、`ceasings`、`held_over_stretch`、`marks_within`、`keep_pace` | 有限家族中：终点成立的成员连同其间不再成立的，恰是起点成立的成员连同其间开始成立的；开始成立与不再成立的次数之差不超过成员数 |
| `Recurs`、`Recurs.mono`、`Recurs.accumulates`、`pos_of_exceeds`、`coming_recurs_iff` | 有限家族中，开始成立复现恰当不再成立复现 |
| `Web.activity_over_stretch`、`Web.arising_recurs_iff`、`Web.unceasing_iff` | 读于活动（活动可判定）：有限家族的形成在终点活跃的连同其间止息的，恰是在起点活跃的连同其间生起的；它们在任意晚的步生起恰当在任意晚的步止息；形成有限多时，生起复现恰当某个形成在任意晚的步止息（P29b 更正，原文“生成不息恰当……”；见 §42 R5） |
| `Web.standing_recurs_iff` | 读于水平，不需要任何前提：有限家族的条件在任意晚的步开始作为条件而在，恰当它们在任意晚的步不再作为条件而在 |
| `Dawn.unceasing`、`never_ceases`、`rises`、`never_falls` | 无限家族：形成 f 跨第 f 步生起、从不止息，水平每步上升、从不下降。只生而不止需要无尽的新，上升复现而不下降需要无界 |
| `Dusk.ceasing`、`nothing_arises` | 无限家族：全部形成一开始活跃，形成 f 跨第 f 步止息，没有任何生起。只止而不生需要无尽的初始 |
| `le_dest`、`steps_mem`、`steps_last`、`steps_mono` | 一段步的引理 |

另外，`total_map` 与 `total_congr` 从 `Roles` 移到 `Flow` 的 total 一节，与其他 total 的引理放在一起，并新增 `total_ones`（每个成员计一次，总和是成员数）。`Roles` 与 `Reserve` 的定理数随之减少，内容不变。

**解读。**

- **不加前提的部分有实质内容。** 前四行是定义与恒等式：变化的读法、升降相抵。它们本身不多说什么，但把以前分散的定义（`Arises`、`Forms`、`Dissolves`、`ComesToStand`）收到同一种变化之下，并补上缺少的另一半（`Ceases`、`CeasesToStand`）。实质内容来自两个界：量不低于零，规定只计 0 或 1。由前者，下降复现需要上升复现；由后者，有限家族中开始成立与不再成立同步。这些对每个展开成立。
- **生起与止息在有限之中同步。** 有限家族中，生起复现恰当止息复现；任一段步上两者之差不超过成员数。所以在形成有限多且活动可判定的展开中，生起复现恰当止息复现（P25b 更正，原文“生成不息恰当止息不息”；见 §38 O7）：没有只生不灭的有限世界，也没有只灭不生的有限世界。作者把这读作 Ren 所说“生成、维持、转化、退化与消失在同一展开中”的一种形式内容（AI 论证）：生起与止息在有限之中一同复现。这是活动的读法；它是否为 Ren 提议中的“生成的”“退化的”由 Ren 选择：Ren 说二者“不overlap吧”，若取不重叠，这一读法就不是其所指（AI 的推论）；读作关系，更新的形成与消耗的形成不重叠（`Web.renewing_not_consuming`）（P25b 更正，原文“不是 Ren 的‘生成的’‘退化的’：Ren 说二者不重叠”；见 §38 O8）（P23c 更正，原文“生成与退化不是两个可以分开的过程，在有限之中它们一同复现”；见 §34 M1）。这不推出止息是好的或坏的，也不决定生生不息在哪个层次读：在谱系或整体的层次上不息，与成员的止息不息并不冲突（§21 的 `Generations`），这里的结论正是说成员层次上两者同步。
- **无限是逃脱的方式。** 只生不止需要无尽的新（`Dawn`）；只止不生需要无尽的初始（`Dusk`）。这与 §21 的 `needs_new`（部分终结、同时活跃的有限时，整体需要不断新的部分）和 §20、§23 的耗散结论（条件总共有限时生成终止）同一方向：有限性使生成须伴随别的东西，前提不同，所伴随的不同（止息、补充、开放）。
- **更新规律的分解。** `Generation` 的“生起消耗有限家族时，不息的生成需要更新复现”与 `Flow` 的“复现的取用需要补充复现”，现在可以读作一个前提（消耗、平衡）加这里的下限：前提把生起或取用变成下降，下限使下降的复现需要上升的复现。`Renewal` 的 `falls_finitely` 正是一个量的下限（`falls_finitely_from_floor`）。下限本身对每个展开成立：每个展开中，有限多个条件持续下降就持续上升（`Web.falls_need_rises`）。
- **开始作为条件而在不需要任何前提。** 水平是否为正总可判定，所以 `Web.standing_recurs_iff` 连可判定性的假设也不需要：有限家族的条件开始作为条件而在复现，恰当它们不再作为条件而在复现。§24 证明，平衡的流中开始作为条件而在复现需要补充复现；这里加上：它也需要不再作为条件而在复现。

**作者反审。**

*反驳 1：这些是平凡的计数，不是生成之论的内容。* 证明是计数，内容是：一个二值的规定在有限家族中无限多次改变，就在两个方向上都无限多次改变；读于活动，在任何有限的展开中生起与止息同步。它是二值与有限的推论，不排除二值与有限所排除之外的任何动力学；对整个空间成立的东西不多，这一条是其中之一（P23c 更正，原文“它说在任何有限的展开中，生成与退化同步。这正是 Ren 提议中‘计入整个空间，包括生成与退化’的一个形式陈述……这一条把生成与退化绑在一起”；见 §34 M1、M9）。平凡的是证明，不是结论；以前各模块需要前提才得到的“生成须伴随更新”，其下限部分在这里对每个展开成立。

*反驳 2：可判定性就是一个前提。* 它是表示的方法承诺，已在来源说明与计划第 9 节中单独公开：计数需要知道每一步是否成立。它不是关于展开的前提：不限制什么生起、什么止息。读于水平时连它也不需要。无论如何，相关定理把它作为显式假设写出。

*反驳 3：“有限家族”也是前提。* 是，它是定理的假设，`Dawn` 与 `Dusk` 表明它不可去掉。但它不是关于展开动力学的前提：任何展开中任何有限的形成家族都满足它。定理说的是“对每个展开、对其中每个有限家族”。

*反驳 4：把生成不息与止息不息等同，会被读成“生生不息需要死亡”。* 定理只说成员层次上的数目同步，不说止息是生成的条件或代价，也不说它好。§21 的 `Layered` 表明同样的成员可以反复生起与止息（短暂的部分）；那里的止息不是消失。是否把这读作生生不息的一部分，由 Ren 定。

**边界。** 不含伦理谓词；只对离散步的读法陈述；有限家族以列表给出；“复现”不给出频率或比例；同步是数目的同步，不说明哪个形成生起或止息，也不说明为什么；不把形式规律当作对现实的演绎必然性；中文用语“止息”“开始成立”“不再成立”“同步”是 AI 的提议，名称由 Ren 定。本节经第九次独立审查，更正见 §34。

## 27. 第八次独立审查与更正（P18b）

2026-10-09。按同一指示继续。另一 agent（Claude Opus 5.5，未参与撰写）独立审查了 P16c（§23）、P17（§24）与 P18（§25）（[审查](BECOMING-P16C-P17-P18-REVIEW.md)）。它在仓库之外从前导重新编译核心闭包的 24 个模块，1356 条源声明的公理报告全空；回执、源哈希、保留产物、引用哈希与证明绑定都对，数学全部接受，Lean 中没有数学错误。K2、K5、K7 关闭；K1、K3、K4、K6 关闭而有残余；K8 的八项中五项关闭。它提出十项（L1–L10）：一项定义与其陈述的意义不符（L10，最严重），两项散文中的错误（L5、L9），四项说得过强（L1、L2、L4、L8），一项缺少反例（L6），两项记账与表述（L3、L7）。审查没有发现替 Ren 选择任何读法；L1 的残余把体现读作生命，是 K6 已指出、P16c 已承认属于 Ren 的读法。本节记录逐项处理。审查的探针按需要移入相应模块，公理报告为空。§18、§20、§22–§25 与英文段落中受影响的句子已就地更正并标明；原文见提交 `4295dd24`。

```text
Result(s): 更正 living-on-and-descent（L8–L10）、reserve-defers-ending（L3(d)、L4–L6）、generation-is-replenishment（L7）、
           life-as-condition-of-life（L1、L9）；whole-persists-through-generation 与 identity-across-steps 的关联说明（L2）；
           检查器审计 Lean 生成的常量（L3(b)）；没有新的成果记录
Delta: Flow.Descends 要求给予的形成参与该步，新增 Stranger 与 Brood.not_descends（L10）；LivesOn.stands 与 Drowsy（L8）；
       Seed.no_held、Viable.no_held（L4）；Flow.carries_of_own（L5）；Web.redirect、redirect_same、redirect_dependent 与
       Famine.undermines_one、transformed_not_undermining、living_differs（L6）；Balances.rise_given、ComesToStand.rises、
       Web.rising_of_coming、Balances.rise_replenishes、rising_needs_replenishment、Growing、rise_lowers_on、rising_ceases_on、
       rising_opens、rising_draws_in、rising_ceases，原有的开始作为条件而在的定理改由它们推出（L7）；用语、标题与关联说明（L1–L3）
Supplied premises / correspondence: 不变；在所持条件被表示的地方，估值用哪种读法列为对应前提（L6）；世系按给予项计而不按净流量，
       列为又一个读法选择（L10）；审查时间的约定写入 _process/RESULT-WORKFLOW.md（L3(f)）
Evidence: 合并检查器回执 20261009T104417.218214Z（877 项定理／1387 项声明审计，核心闭包 25 个模块，包 23 个模块，源声明的公理报告全空；
          核心闭包中 Lean 生成的常量依赖公理的有 29 条，都是带字段构造子的 injEq 引理，只依赖 propext）；外围桥接重跑 20261009T104540.104898Z；
          实例检查通过
Boundary: 不含伦理结论；不改变任何读法选择的地位；新名称是建议；探针与新见证都是最小见证
Integration: §23–§25 的更正；§24 列为开放的“一般地构造转化的读法”完成；L7 使补充与耗散的定理都对上升陈述
```

### 27.1 逐项处理

| 项 | 审查所见 | 处理 |
|---|---|---|
| L1 | 体现的关系项仍被称作生命：`Roles` 的模块说明、节标题与 `active_of_bearing` 的说明，§18，§23.4 反驳 4，章节 §2 与 §8，英文 P14 与 P16b；章节 §2 的中文多一句英文中没有的 AI 读法；记录标题 | `Roles` 三处改为“An embodied relatum as a condition”。§18、§20、§22、§23.4、章节与英文改为“体现关系项 / embodied relatum”与“need not be embodied”，标明 P18b 用语与原文。章节 §2 那句中文删去。life-as-condition-of-life 的标题改为“回答‘生作为生的条件’：……”，H14 的用语只作为所回答的问题的名称 |
| L2 | `Dissipation` 的模块标题仍是无条件的“汲入”；两条关联说明仍写“部分不长久”，一条写“构成” | 标题改为“recurring taking opens finite families and, enclosed around, draws in”。两条说明改为记录标题的形式：部分短暂，或部分终结且同时活跃的部分有限时，整体经由部分的生成而持续 |
| L3 | (a) “给予者”残留在 §18、§22 与计划；(b) “每条声明的公理报告为空”没有排除编译器生成的 `injEq` 引理；(c) §24 反驳的次序是 1、2、3、4、6、5；(d) 英文用“draws”表示耗用储备；(e) P16b 的英文段落把包写成核心；(f) 记录的审查时间早于它引用的运行 | (a) 改为“给予它的关系项／形成”。(b) 两者都做：现行文字改为“每条源声明”；检查器另审计核心闭包的全部常量（含生成的），断言依赖公理的只有带字段构造子的 `injEq` 引理、只依赖 `propext`、不是源声明，并在回执中逐一列出（29 条，与审查的计数相同）。(c) 按编号排列。(d) 改为“uses no reserve”。(e) 改为“The package”。(f) 约定写入 [RESULT-WORKFLOW](../../../RESULT-WORKFLOW.md)：作者修订记录内容（主张、前提、对应、界限、反例、关联说明或下一步）时刷新审查时间，只把验证范围改指新回执、内容不变时不刷新。本次内容改动的六份记录随之刷新；becoming-dependence-dynamics 在 P17 改了界限与下一步，作者复核后刷新 |
| L4 | “储备是所持的条件”只给出一个方向：本模块自己的 `Seed` 与 `Viable` 的储备不是任何条件的水平，它们的网中也没有所持条件能承载种子 | 改为“储备可以是所持的条件；没有表示所持条件时，储备是给定的”。`Seed.no_held`、`Viable.no_held` 移入核心。“滞后就是依存转化到所持的条件上”限于所持条件承载它的地方。模块说明、根模块、包说明、§24、记录与章节 §9 随之更正 |
| L5 | `carries_of_held` 的前提只要求有形成从所持条件取用，不必是持有者：`Larder` 中狐不参与、不取用，乌鸦吃掉脂肪，前提全部成立 | 说明改为“被（参与的任何形成）取用”。新增 `Flow.carries_of_own`：持有者自己参与并从中取用时的形式；`Famine.carries` 改由它证明，狐燃烧自己的脂肪。`Larder` 留在审查的探针中 |
| L6 | 两种读法对狐第 1 步的事件给出不同的 living；转化的读法可以一般地构造 | `Web.redirect`（用 `if` 而不另设选择函数）、`redirect_same`、`redirect_dependent` 移入核心：所持条件承载形成时，把每个不被支持的依存移到所持条件上、需要为一，水平、活动与汲取不变，这样读出的依存网满足 `Dependent`。`Famine.undermines_one`、`transformed_not_undermining`、`living_differs` 移入核心。§24 反驳 2 与记录写明：两种读法在 living 上不同，选择是影响估值的对应前提；转化的读法满足 `Dependent` 由构造给出，是对储备的重新描述，不是关于展开的另一事实 |
| L7 | 证明只用到上升带来的正的给予，不用从零开始 | 一般定理对上升陈述：`Balances.rise_given`（`renewedBy` 改由它推出）、`Web.ComesToStand.rises`、`Web.rising_of_coming`、`Balances.rise_replenishes`、`rising_needs_replenishment`、`rise_lowers_on`、`rising_ceases_on`、`rising_opens`、`rising_draws_in`、`rising_ceases`；原有的 `standing_*` 定理改由它们推出，陈述不变。`Growing`：一个条件每步上升、每步被给予，从不开始作为条件而在。§24、记录与章节改为“要求跟着水平的上升走，开始作为条件而在是从零的上升” |
| L8 | `LivesOn.active` 以所依的关系项体现为假设；散文写成在 `Dependent` 之下只能以活跃的体现关系项为生；`Drowsy` 中吃者以既不体现、该步也不活跃的关系项为生 | 新增 `LivesOn.stands`：在 `Dependent` 之下，所依的关系项在该步作为条件而在。`LivesOn.active` 保留，所有说明写出体现的前提。`Drowsy` 移入核心：以之为生连通，交互不连通。模块说明、§25、记录、章节与检查器范围更正 |
| L9 | “这里体现第一次进入估值”：`sustenance` 与 `descent` 的定义都不含体现 | 改为“这里一类读法的同一对应第一次进入估值；两种关系的定义不含体现”。life-as-condition-of-life 的下一步写为以更宽的形式得到回答；living-on-and-descent 的对应与依赖说明随之更正 |
| L10 | `Flow.Descends` 读 `give`，不要求给予的形成参与该步。不参与者的给予项不进入任何水平，平衡与 `Acting` 都不约束它，却造成世系；`Brood` 中给予不看是谁给予，每一代都“从”每个自然数而来 | 定义改为要求参与：`∃ t, g ∈ L.present t ∧ 0 < L.give t g x ∧ W.ComesToStand t x`。`Embodied.descends`（`arises_given` 已给出参与）、`Brood.descends`、`Provisioned.descends` 与 `Brood.descended` 照旧成立；`Sleeper.no_descent` 改由没有参与者推出。新增 `Stranger`：流平衡、只有活跃形成给予，陌生者对种子的给予项在种子开始作为条件而在之步为正，种子只从父代而来；`Brood.not_descends`：第一代不从第八代而来。§25 反驳 2 的例子在更正后的定义下成立。世系按给予项计而不按净流量，写为又一个读法选择 |

### 27.2 新的已检查声明

| 模块 | 声明 | 内容 |
|---|---|---|
| Descent | `Flow.Descends`（更正） | 世系要求给予的形成参与该步 |
| Descent | `LivesOn.stands` | 在 `Dependent` 之下，活跃的形成以之为生的关系项在该步作为条件而在 |
| Descent | `Drowsy.Relatum`、`web`、`dependent`、`not_undermining`、`lives`、`eater_alive`、`sleeper_alive`、`down`、`up`、`sustenance_connected`、`not_interacting`、`drowsy` | 一个关系项始终以水平一作为条件而在、在奇数步醒来；吃者始终活跃，汲取它并以需要一依存于它。`Dependent` 成立，没有侵蚀；吃者在第 0 步以它为生，它不体现、该步不活跃；以之为生连通，交互只关联吃者的事件 |
| Descent | `Stranger.Relatum`、`web`、`toSeed`、`flow`、`balances`、`acting`、`absent`、`stranger` | 父代、种子与陌生者；只有父代参与，在第 0 步给予种子一单位；流另有陌生者对种子的给予项。流平衡，只有活跃形成给予；陌生者从不参与；种子跨第 0 步开始作为条件而在，只从父代而来 |
| Descent | `Brood.not_descends` | 第一代不从第八代而来：第八代在第 0 步的给予项不属于任何参与者 |
| Flow | `Web.ComesToStand.rises`、`Web.rising_of_coming` | 开始作为条件而在是从零的上升；成员在任意晚的步开始作为条件而在，就在任意晚的步上升 |
| Flow | `Balances.rise_given`、`Balances.rise_replenishes`、`rising_needs_replenishment` | 平衡的流中每次上升都被给予，补充每个包含它的家族；成员在任意晚的步上升时，家族的补充复现，不论取用什么。`renewedBy`、`standing_replenishes` 与 `standing_needs_replenishment` 改由它们推出 |
| Flow | `Growing.web`、`flow`、`balances`、`growing` | 一个条件每步上升一、每步被给予，从不开始作为条件而在 |
| Dissipation | `rise_lowers_on`、`rising_ceases_on`、`rising_opens`、`rising_draws_in`、`rising_ceases` | 被耗散家族的成员上升，降低家族的存量；从某步起被耗散的家族中，成员不在任意晚的步上升；耗散之下，成员在任意晚的步上升的不重复有限家族从任何一步起都不封闭，被围住时汲入；条件总共有限时，没有条件在任意晚的步上升。六个 `standing_*` 定理改由它们推出 |
| Reserve | `Flow.carries_of_own` | 持有者自己参与并从所持条件取用时，所持条件承载它 |
| Reserve | `Web.redirect`、`redirect_same`、`redirect_dependent` | 把每个不被支持的依存移到所持的条件上、需要为一；水平、活动与汲取不变；所持条件承载形成时，满足 `Dependent` |
| Reserve | `Seed.no_held`、`Viable.no_held` | 两颗种子的依存网中没有任何条件承载它们：储备是给定的 |
| Reserve | `Famine.undermines_one`、`transformed_not_undermining`、`living_differs` | 狐在第 1 步的事件按原读法侵蚀（它汲取兔，它在第 0 步满足过对兔的依存，兔在该步之后低于所需），按转化的读法不侵蚀（脂肪在该步之后仍为一） |

检查器另写出 `EnvironmentAudit.lean`：列出核心闭包每个模块的常量数（含 Lean 生成的）与每个依赖公理的常量，断言后者都是带字段构造子的 `injEq` 引理、只依赖 `propext`、不是源声明，回执记下 `core_closure_constants` 与 `generated_axiom_dependencies`。

### 27.3 审查列出的会改变判断的结果

1. 世系（L10）：要求给予的形成参与，重述三个世系定理与“空的给予不造成它”。完成；原定义下的反例（`Stranger`、`Brood` 中第一代从第八代而来）在更正后的定义下不成立，并成为定理（`Stranger.stranger`、`Brood.not_descends`）。
2. 以之为生（L8、L9）：以 `LivesOn.stands` 作为 `Dependent` 给出的东西，`LivesOn.active` 的每处说明写出前提，“体现第一次进入估值”改为同一对应。完成。
3. 储备（L4–L6）：“可以是所持的条件”，`Seed` 与 `Viable` 是给定的储备；更正 `drawn` 的说明并给出持有者自身取用的形式；写明转化的读法在第 1 步改变 living，并记下一般的构造。完成。
4. 上升（L7）：完成，且审查没有构造的部分（P17 的耗散定理对每个上升重述）也已构造。
5. 残余（L1–L3）：完成。
6. Ren 的选择保持开放：以之为生与世系是否算作 N_rel 所传递的形成关系；“生”与 living 的读法，包括体现的关系项是否是“生”；接续的读法与生生不息读到哪个层次；终结之步的汲取是否计入、对哪些汲取者；名称，包括给予的用语；以及新增的一项：在所持条件被表示的地方，估值用哪种读法。
7. 审查未构造而仍开放的：沿依存链、有储备的滞后共灭；净给予形式的世系。

### 27.4 作者反审

*反驳 1：要求参与是否太强，一个形成可以在不参与的步上给予？* 在这一表示中不能：`given` 只对参与者求和，平衡只约束 `given`，所以不参与者的给予项不进入任何水平，也不被 `Acting` 约束。要求参与正是要求给予实际发生。原定义并不更宽地反映给予，只是多读了表示中没有约束的分量。

*反驳 2：`redirect_dependent` 使 `Dependent` 在所持条件承载形成处总可满足，这是否削弱了 `Dependent`？* 它表明 `Dependent` 的内容与依存于什么的读法一起才确定：在所持条件被表示的地方，零储备与正储备是同一展开的两种读法，区别在于哪些依存被读出。这不削弱它，而是写明它不是关于展开本身、与读法无关的事实；两种读法在 living 上不同（`living_differs`），所以对估值来说，选择不是中立的，属于对应前提。

*反驳 3：把一般定理改对上升陈述，开始作为条件而在还说明什么？* 它说明体现的生起落在哪里：体现的关系项在生起时开始作为条件而在，所以 §20 与 §23 的结论适用。上升的形式更宽：`Growing` 表明要求也落在从不开始作为条件而在、只是增长的条件上。§26 的下限说明一般的另一半：没有前提时，下降的复现需要上升的复现；这里加上，平衡时上升需要给予。

*反驳 4：审计生成的常量是否越出“核心纯净”的要求？* 核心纯净的三条（只导入自身、源声明的公理报告为空、只用前导编译）不变。生成的 `injEq` 引理依赖 `propext`，它们属于环境，不属于证明；审计使这一事实被检查而不只是被说明。若以后出现别的依赖公理的生成常量，检查器会失败，需要先查明再接受。

**边界。** 不含伦理谓词；不改变读法选择的地位；新名称是建议；探针与新见证都是最小见证；转化读法的选择、世系按给予项计，是公开的读法选择；沿依存链的滞后共灭与净给予的世系，开放。本节的更正经第九次独立审查，L1–L10 全部关闭，见 §34（P23c 补记，原文“本节的更正尚未再经独立审查”）。

## 28. 上升与下降在同一交换中（P20）

2026-10-09。按同一指示继续计划 P20。§26 不加前提地证明：在有限家族中，开始成立与不再成立同步，但那是一段步上的数目与复现的同步，不说一次生起在哪一步伴随什么。本节问：一个成员上升（包括开始作为条件而在、体现的生起）的同一步上，是否另有成员下降？不加前提时不然：`Growing` 与 `Brood` 中有上升而什么都不下降。在平衡与耗散之下则然，而且有数量：被耗散的一步上，家族成员的下降至少等于其上升，每个取用的形成再多一。成果记录：[rising-and-falling-in-one-exchange](../../../../theories/becoming/results/records/rising-and-falling-in-one-exchange.md)。

```text
Result(s): 复用 no-finite-part-bears-taking（DissipatesOn、Dissipative、ClosedAt、runs_down、takes_of_gives）、
           coming-and-ceasing-keep-pace（rise、fall、risen、fallen、family_over_stretch、excess_pos）、
           generation-is-replenishment（rise_given、ComesToStand、Embodied.comesToStand、Brood）、
           unceasing-generation-needs-renewal（Depletes、Rises、Falls）、more-needs-renewers（Balances、Acting、Taking、takers）；
           新增 rising-and-falling-in-one-exchange
Delta: Flow：Balances.fall_taken、Balances.takenBy；Dissipation：Balances.falls_cover、Balances.falls_of_taking、Balances.depletes、
       rise_with_fall、standing_with_fall、rise_alone_opens、rise_exchange；Roles：Embodied.arising_with_fall、
       Brood.birth_only、Brood.rise_without_fall
Supplied premises / correspondence: 平衡（Balances）；该步上家族被耗散（DissipatesOn；耗散之下，每个不重复的封闭家族都是）；
       读于形成时另加只有活跃者给予与取用（Acting、Taking）；读于体现的生起时另加体现（Embodied）
Evidence: 合并检查器回执 20261009T110204.479251Z（889 项定理／1399 项声明审计，核心闭包 25 个模块，包 23 个模块，源声明的公理报告全空）；
          外围桥接重跑 20261009T110332.423150Z；实例检查通过；五份记录所引的模块定理数按新回执更正，其中四份此前已过期（Flow、Dissipation、Identity、Wholes）
Boundary: 下降不是止息，下降的成员可以仍作为条件而在；不说哪个成员下降，只说有；不说上升对下降者是好是坏；
       不含伦理谓词；“同一交换”是同一步上同一流中的给予与取用，不是因果的单独归属
Integration: 计划 P20；把 §26 的长程同步在耗散之下变为一步之内的伴随；Generation 的两个对应前提（RenewedBy、Depletes）
       都化归为流的前提；§20 与 §27 的“上升降低存量”加上“另一个成员下降”
```

| 模块 | 声明 | 内容 |
|---|---|---|
| Flow | `Balances.fall_taken` | 平衡的流中每次下降都被取用。`rise_given` 的对偶 |
| Flow | `Balances.takenBy` | 只有活跃者取用时，每次下降都是某个参与的活跃形成的取用，它汲取这一条件。`renewedBy` 的对偶 |
| Dissipation | `Balances.falls_cover` | 被耗散的一步上，家族成员的下降至少等于其上升，每个取用的形成再多一：`risen + takers ≤ fallen`。由 §26 的一步上的升降相抵（`family_over_stretch`）与 §17 的 `runs_down` 推出 |
| Dissipation | `Balances.falls_of_taking` | 被耗散的一步上，有形成从家族取用，就有成员下降，不论别的成员是否上升 |
| Dissipation | `Balances.depletes` | 一个事件的每一步上家族都被耗散且有形成从中取用，这个事件就消耗家族（`Generation` 的 `Depletes`） |
| Dissipation | `rise_with_fall`、`standing_with_fall` | 被耗散的家族中一个成员上升（开始作为条件而在），同一步上另有一个成员下降 |
| Dissipation | `rise_alone_opens` | 耗散之下，不重复的家族中有成员上升而没有成员下降，家族在该步不封闭：有参与的形成与家族之外的条件交换 |
| Dissipation | `rise_exchange` | 只有活跃者给予与取用时：一个成员上升，某个活跃形成给予它，并从家族取用；另一个成员下降，某个汲取它的活跃形成从中取用 |
| Roles | `Embodied.arising_with_fall` | 被耗散的家族中一个体现成员的生起，伴随同一步上另一个成员的下降 |
| Roles | `Brood.birth_only`、`Brood.rise_without_fall` | 没有耗散时不然：每一步上，第 t+1 代在它与第 t 代组成的家族中生起，家族在该步封闭，没有任何一代下降过；所以该家族在该步不被耗散（由 `arising_with_fall` 推出） |

**解读。**

- **长程的同步在耗散之下变成一步之内的伴随。** §26 说，有限家族中生起复现恰当止息复现，但两者可以相隔任意多步。在家族被耗散的一步上，平衡使上升在同一步上就伴随家族另一个成员的下降：不必等到以后，也不必在别处（P23c 更正，原文“耗散加上平衡，使上升在同一步上就伴随另一个成员的下降”；在 `Spray` 中流平衡且耗散，一个条件上升而没有条件下降，见 §34 M5）。数量上，下降至少等于上升加取用者的数目，所以耗散的家族在每个有交换的步上整体下降（`runs_down`），上升只是使别的成员下降得更多。
- **生成的两个对应前提化归为流的前提。** §13 中 `Becoming.Generation` 的结论用两个由应用给出的前提：每次上升都由某个形成造成（`RenewedBy`），事件在没有上升的步上消耗家族（`Depletes`）。§14 已证明前者在平衡且只有活跃者给予的流中成立（`renewedBy`）。这里证明后者的更强形式：在平衡的流中，被耗散且有取用的步上，家族的某个成员下降，即使另一个成员上升（`falls_of_taking`）；一个事件的每一步都是这样的步，它就消耗家族（`depletes`）。所以在流的读法中，`Generation` 的两个对应前提化归为平衡、只有活跃者给予、耗散，以及事件之步上有形成从家族取用；这些仍是对应前提，只是更基本，并且可以分别检验。
- **同一交换的两面。** `rise_exchange` 读于形成：给予上升成员的活跃形成自己从家族取用（耗散），另一个成员下降，由汲取它的活跃形成取用（平衡与 `Taking`）。读于一类关系项（`Embodied.arising_with_fall`）：一个关系项的生起，在同一步上就是家族中另一个关系项的下降。作者把这读作 Ren 所说“生成、维持、转化、退化与消失在同一展开中”在一步之内的一种形式内容（AI 论证）：在被耗散的家族中，生起不是一个可以单独发生的事件，它与别处的下降是同一次交换。
- **开放的单步判据。** §20 与 §27 证明，耗散之下，成员在任意晚的步开始作为条件而在（一般地，上升）的不重复有限家族，在任意晚的步不封闭。`rise_alone_opens` 给出单步的形式：耗散之下，有成员上升而没有成员下降的不重复家族，在该步就不封闭。`Brood` 正是这样：第 t+1 代生起，没有一代下降，家族封闭，所以它不被耗散。

**作者反审。**

*反驳 1：这只是耗散前提的改写。* 前提是每个形成的：它给予家族的少于从中取用的。结论是每个成员的：另一个成员的水平下降，下降的总量至少等于上升加取用者数。从形成到成员要经过平衡（每个成员的水平变化恰是给予与取用）与一步上的升降相抵（§26）。推导短，但内容不在前提中：前提不提及任何成员的水平。`Growing` 与 `Brood` 表明，没有耗散时结论不成立。

*反驳 2：“生与灭在同一交换中”说得过强。* 是。计划原题为“生与灭”，证明的是上升与下降：下降的成员可以仍作为条件而在、仍然活跃，什么都不必止息。本节与记录用“上升与下降”，计划的行随之更正。下降何时是不再作为条件而在，要看水平是否降到零，这里不陈述；关于止息，见 §26 不加前提的长程同步与 §17、§20 在耗散之下的终止定理。

*反驳 3：会被读成一个生起须以另一个的损失换来。* 定理不这样说。下降不是损伤：侵蚀在 `Becoming.Dependence` 中由依存与所需定义（`UnderminingOn`），一个条件下降后仍不低于每个依存于它的所需，汲取它就不是侵蚀；下降的成员可以是燃料、池水，而不是任何形成所依的东西。定理也不说上升是好的或坏的。它说的是在被耗散的家族中，交换在同一步上有两面；评价要另经 G0 与 C，不在这里。

*反驳 4：为什么只对被耗散的家族陈述，而不对一切封闭家族？* 耗散之下，每个不重复的封闭家族都被耗散（`Dissipative` 的定义），所以 `rise_with_fall` 加上 `dissipative ds t distinct closed` 就是封闭家族的形式；`rise_alone_opens` 是它的逆否。陈述为被耗散的家族，使前提只在用到的那一步上：一个流可以只在某些步、某些家族上被耗散。

**边界。** 不含伦理谓词；“同一交换”是同一步上同一流中的给予与取用，不把下降单独归给某个上升；不说哪个成员下降；下降不是止息；只对离散步的读法与自然数的量陈述；耗散、平衡与只有活跃者取用是对应前提，实际展开是否满足是经验问题；“上升”“下降”“同一交换”是 AI 的用语，名称由 Ren 定。本节经第九次独立审查，更正见 §34。

## 29. 演化在脊柱上（P21）

2026-10-09。按同一指示继续计划 P21。演化之论的核心候选说：组织的差异通过实际传递参与后续活动，并改变变异、发育、共同生活与下一轮选择的条件。本节问：在脊柱上，这一候选有什么最小的形式内容？脊柱已有世系（§25，§27 更正为给予的形成须参与该步）、支持与 `Dependent`（§6）、平衡与 `Balances.accumulates`（§14）、截断差 `excess`（§26）。新模块 `Becoming.Evolution`（L3，只导入 `Change`）用它们陈述传递、变异与选择，以及活动对后来选择的反馈。成果记录：[evolution-on-descent](../../../../theories/becoming/results/records/evolution-on-descent.md)。

```text
Result(s): 复用 living-on-and-descent（世系；定义移入本模块）、coming-and-ceasing-keep-pace（excess、excess_balance）、
           more-needs-renewers（Balances、Acting、accumulates、total 的引理）、generation-is-replenishment（ComesToStand）；
           新增 evolution-on-descent
Delta: Evolution：total_const、length_mul_le、offspring、selected、raised、lowered、price；Flow.DescendsAt、Flow.Descends
       （从 Descent 移来）；DescendsAt.active、DescendsAt.supported、unsupported_childless、never_supported_childless、
       selected_le、selection_within；TransmitsWithin、transmitted_supported、transmitted_within；Drawdown、Unchecked
Supplied premises / correspondence: price 不加前提；选择用 Acting 与 Dependent；传递是前提（TransmitsWithin）；
       transmitted_within 另加平衡
Evidence: 合并检查器回执（见记录）；外围桥接重跑；实例检查
Boundary: 不含伦理谓词；适应度没有定义；传递不由脊柱推出；price 是会计恒等式；选择只读作支持对给予的约束；
       不含繁殖率、突变、漂变、迁移与种群动力学；与演化之论既有机制的对应未证明
Integration: 计划 P21；世系从 L4 移到 L3，Descent 保留估值的读法；演化之论的独立纲领保持原范围
```

| 声明 | 内容 |
|---|---|
| `Flow.DescendsAt`、`Flow.Descends` | 一个关系项跨一步从一个形成而来：该形成参与这一步、给予它，它跨这一步开始作为条件而在。定义与 §27 的相同，只是移到 L3 并给出每一步的形式 |
| `price` | 不加前提：任意有限的亲代家族与各自的有限后代列表，任意的量，后代的总量加传递所降低的，等于亲代的量按后代数计数，加传递所升高的。Price 方程的加法计数形式 |
| `DescendsAt.active`、`DescendsAt.supported` | 只有活跃者给予时，后代从之而来的形成在给予之步活跃；活动另需支持时，它在该步被支持 |
| `unsupported_childless`、`never_supported_childless` | 选择：在一步不被支持的形成不在该步留下后代；从不被支持的形成没有后代 |
| `selected_le`、`selection_within` | 读于每个亲代都依存的条件上的所需：亲代所需按后代数加权的总量至多是条件的水平按后代数计数（P23c 用语，原文“选择项”）；所以后代任意量的总量加上从亲代所需降低的，至多是这样计数的水平加上升高的 |
| `TransmitsWithin` | 前提：在开始作为条件而在之步依存于 c 的后代，只从在给予之步依存于 c 的形成而来，且所需至多多 δ |
| `transmitted_supported` | 传递的曾被选择：后代的所需至多是该条件在给予之步的水平加 δ |
| `transmitted_within` | 活动设定后来的选择：平衡的流中，后代的所需加上自较早一步以来从条件取用的，至多是条件那时的水平加其后给予它的，再加 δ |
| `Drawdown.drawdown` | 见证：亲代以所需二依存于水平为二的池，从池取用一并给予两个后代；承继所需二的那个从开始作为条件而在之步起不被支持，所需一的那个被支持、活跃并转而取用 |
| `Unchecked.unchecked` | 没有 `Dependent` 时不然：超出支持而活跃的亲代，传递高于给予之步水平的所需 |

**解读。**

- **世系属于变化，不属于评价。** 世系由参与、给予与开始作为条件而在定义，不含估值。P18 把它放在 L4 的 `Descent`，因为它首先用于估值的连通。现在它在 L3 的 `Evolution` 中定义，`Descent` 导入它并保留 N_rel 下的读法（`descent_reaches`、`Brood.descended` 等）。这样，演化的定理不经过元伦理层。
- **Price 方程是恒等式，内容在别处。** `price` 与 §26 的升降相抵同类：不加前提，对任意量成立。它把后代的总量分为亲代的量按其后代加权的总量与传递的变化，但不说哪一项由什么决定。加权总量不是真正的选择项：每个亲代都有 k 个后代时它是亲代总量的 k 倍（`selected_uniform`），没有任何选择时也不为零（`unselected`）；真正的选择项即后代数与量的协方差没有陈述（P23c 更正，原文“它把从亲代到后代的变化分为选择项与传递项”；见 §34 M3）。两份既有笔记已手推其协方差形式并说明它是会计恒等式（[math-note](../../2026-10-05-direction-frontier/math-note.md)、[GENERATED-SELECTION-RECURRENCE-INTEGRATION](GENERATED-SELECTION-RECURRENCE-INTEGRATION.md)，引 Frank 2012）。这里的贡献是：它在纯核心中、以自然数与截断差检查过，并且两项各自有了脊柱上的内容。
- **选择即支持对给予的约束。** 适应度没有定义。在只有活跃者给予且活动需要支持的展开中，能留下后代的只是被支持的形成：选择不是另加的规律，而是 `Acting` 与 `Dependent` 合起来的推论。`selected_le` 把它写进 `price` 的加权总量：后代数加权的亲代所需，受条件的水平所限（P23c 用语，原文“选择项”）。
- **传递的曾被选择。** 后代承接亲代的依存（`TransmitsWithin`）时，后代的所需至多是给予之步条件的水平加 δ：界为零时，传下来的所需在给予时被满足过；界为正时可以从未被满足（`Slack`）（P23c 更正，原文“传下来的所需在给予时被满足过”；见 §34 M6）。δ 是变异向上的界；向下没有界。
- **活动设定后来的选择。** `transmitted_within` 把给予之步的水平展开为较早的水平与其间的取用和给予。所以其间形成做了什么（取用多少、给予多少）进入后来能传递的所需。`Drawdown` 中，这一反馈来自亲代自己：它的取用降低了池，使承继其所需的后代从一开始就不被支持；所需较少的后代被支持、活跃并转而取用。传递、变异、选择与反馈在同一展开中，这是演化之论核心候选在脊柱上的一个最小实例（AI 论证）。

**作者反审。**

*反驳 1：Price 方程是恒等式，算不上结果。* 是。记录的实质内容是选择与传递的定理：`unsupported_childless`、`selected_le`、`transmitted_supported`、`transmitted_within` 与两个见证。`price` 写入是因为它给出加权总量与传递的划分（P23c 用语，原文“选择与传递的划分”），而且与 §26 一样，是不加前提对整个空间成立的规律；记录与本节都不说它改进了 Price 方程。

*反驳 2：这里的“选择”太弱，它不是繁殖率的差别。* 是。这里的选择只是谁能在一步上给予；一个被支持的形成能有多少后代不受约束，后代数只是 `price` 中的权重。要得到繁殖率的差别，需要把后代数与给予的量联系起来（例如每个后代至少要给予多少），这列入下一步，不在本节。

*反驳 3：传递是前提，所以传递没有被解释。* 是，正如演化之论中重构是前提。一类读法中的世系只说给予它的形成给予（P23c 用语，原文“给予者”）；后代是否依存于亲代所依存的，要看依存怎样形成（§6 的形成与持续）。能否由此推出 `TransmitsWithin`，是开放的证明。

*反驳 4：`Drawdown` 会被读成“变异者胜出”。* 定理不评价。所需较少的后代被支持，只是因为亲代取用之后池的水平满足它而不满足另一个；承继所需的后代不被支持，在 `Dependent` 之下从不活跃，但仍作为条件而在（水平为一），不是消失。哪一个更好，要另经 G0 与 C。

*反驳 5：计划要求在外围接通既有的演化机制。* 计划说的是能证明对应时接通。结构复制（`StructuralCopying`）读的是记号序列的复制与材料预算，与流和依存网之间的对应需要另外建立，本轮没有尝试；它保持原范围，列入下一步。

**边界。** 不含伦理谓词；适应度没有定义，不说哪种所需更好；传递是前提；`price` 只以加法计数形式与自然数的量陈述，不含协方差形式；选择只读作支持对给予的约束；只对离散步的读法陈述；与演化之论既有机制的对应未证明；“世系”“传递”“选择”“变异”的这些读法是 AI 的表述，名称由 Ren 定。本节经第九次独立审查，更正见 §34。

## 30. 整体与其部分（P22）

2026-10-09。按同一指示继续计划 P22。Ren 的提议（[原话](../../../../sources/15-codex-theory-conversations/2026-10-08-theory-of-becoming-priority.md)）：加上公理可以定义好，好是整个空间的一部分；计入整个空间，生成的与退化的，就得到演化之论，或生成／生命之论，它甚至不需要公理。计划把这读作：规律对整个空间成立，前提划出部分。本节新模块 `Becoming.Space`（L3，导入 `Evolution` 与 `Reserve`）给出这一读法的形式结构。成果记录：[space-and-its-parts](../../../../theories/becoming/results/records/space-and-its-parts.md)。

（P23c 更正与改名：这是这一提议的一种结构（AI 的读法）。提议中的“生成的”“退化的”指哪个部分由 Ren 选择；Ren 2026-10-09 说二者不重叠（[原话](../../../../sources/15-codex-theory-conversations/2026-10-09-renewing-consuming-without-axioms.md)）。本节的部分按活动读，改名为生起复现与止息复现：`Generative`、`Degenerative`、`generative_ofRoles`、`degenerative_ofRoles`、`generative_iff`、`handing_generative` 现为 `ArisingRecurs`、`CeasingRecurs`、`arisingRecurs_ofRoles`、`ceasingRecurs_ofRoles`、`arising_iff_ceasing`、`handing_arising`。下面的 Delta 块保留 P22 时的名称；表格与解读用现名，受影响的句子已就地更正并标明。见 §34 M1。）

```text
Result(s): 复用 coming-and-ceasing-keep-pace（Ceases、unceasing_iff、Dawn、Dusk）、generation-is-replenishment
           （generation_ceases、Handing、Kindling、Flicker）、life-as-condition-of-life（roles 与迁移引理、Embodied、
           Mutualism）、reserve-defers-ending（Carries、carries_zero、active_finitely）、evolution-on-descent（Drawdown、
           Unchecked）；新增 space-and-its-parts
Delta: Space：Flow.still、World 及其部分（Finite、Generative、Degenerative、Living、Dependent、Balanced、Acting、Taking、
       Dissipative、Embodied、ArisingEmbodied、Carried）、ofRoles 与迁移、generative_iff、rests；世界 handing、spending、
       mutualism、drawdown、unchecked、unbalanced、idle、restless、kindling、flicker、dawn、dusk；contingent、separate、
       living_crosses、rests_needs
Supplied premises / correspondence: generative_iff 要求有限与活动可判定；rests 另要求平衡、耗散与生起者体现；
       其余是关于具体世界的陈述
Evidence: 合并检查器回执（见记录）；外围桥接重跑；实例检查
Boundary: 不评价任何部分；不证明整个理论不需要公理；部分的列举不完全；Living 只是逐步读法的结构条件
Integration: 计划 P22；Ren 的“计入整个空间”在核心上的结构；为 P23 的完整陈述提供整体与部分的框架
```

| 声明 | 内容 |
|---|---|
| `World`、`ofRoles`、`arisingRecurs_ofRoles`、`ceasingRecurs_ofRoles` | 一个世界是以一类读法的关系项、其间的流与依存网；空间是每个世界。两类读法的任一流与网都是一个世界，生起与止息在那里读法相同 |
| `ArisingRecurs`、`CeasingRecurs`、`Living` | 部分：生起复现（某个关系项在任意晚的步生起）；止息复现（某个关系项在任意晚的步止息）；每个事件都活（逐步读法中活跃者不侵蚀） |
| `arising_iff_ceasing` | 规律：有限且活动可判定的世界中，生起复现恰当止息复现 |
| `separate` | 关系项无限多时两者分离：`Dawn` 中生起复现而无止息，`Dusk` 中止息复现而无生起；两者无限由 `arising_iff_ceasing` 推出 |
| `contingent` | 七个前提（`Dependent`、`Balanced`、`Acting`、`Taking`、`Dissipative`、`Embodied`、`Carried`）各有满足与不满足它的世界 |
| `living_crosses` | 有限世界中四种组合都出现：生起复现且都活（handing）、生起复现而有不活（spending；P23c 起为 grazing）、不生起复现而都活（mutualism）、不生起复现而有不活（drawdown） |
| `rests` | 有限、活动可判定、平衡、耗散且生起者体现的世界中，生起与止息都不复现 |
| `rests_needs` | 每个前提都不可少：kindling（无限）、handing（不耗散）、unbalanced（不平衡；P23c 起为耗散不空的 leaking）、flicker（不体现）都继续生起 |
| `Spending.web`、`Spending.spends` | 与 `Handing` 同样的活动，只是每侧在站立时汲取自身的水平；持有者传出它的水平时侵蚀自身的依存 |
| `idle`、`restless` | 不活跃的关系项给予自身（满足平衡而不满足 `Acting`）；每步都超出支持而活跃的关系项，没有任何储备承载它 |

**解读。**

- **整体与部分的结构。** 空间是每个世界。不加前提的定理（§26 的变化规律、§29 的 Price 方程）对每个网、每个量陈述，所以它们就是对整体成立的规律，不需要另一个包装。各定理的前提每一个都有满足与不满足它的世界（`contingent`），所以它们划出真部分，不是隐藏的规律。这是 Ren“计入整个空间”的一种形式内容（AI 论证）：规律属于整体，前提属于部分。
- **生起复现与止息复现在有限世界中是同一部分。** §26 证明，形成有限多且活动可判定时生起复现恰当止息复现（P25b 更正，原文“生成不息恰当止息不息”；见 §38 O7）。读于世界：活动可判定的有限世界中，生起复现的部分与止息复现的部分重合；对每个世界陈述而不给可判定性，这一规律蕴含排中律（`law_decides`）（P25b 更正，原文“就是排中律”；见 §38 O11）。它们只在无限世界中分离，并且分离的两个世界无限这一点由规律本身推出，不需另证。这是活动的读法；读作关系，更新的形成与消耗的形成不重叠（`Web.renewing_not_consuming`），与 Ren 所说二者不重叠相合；提议中的“生成的”“退化的”指哪个部分，由 Ren 选择（P23c 更正，原标题“生成与退化在有限世界中是同一部分”，原文“有限世界中生成的部分与退化的部分重合”“‘生成的’与‘退化的’不是整体的两半，在有限的展开中它们是同一个部分”；见 §34 M1、M2）。
- **活跨越生起复现。** “每个事件都活”的部分既与生起复现的部分交叠，也与其补交叠，四种组合都在有限世界中出现。`handing` 与 `spending` 的活动完全相同，只差各侧是否汲取自身的水平；spending 中不活的事件是承担自身的体现关系项在其终结之步汲取自身，是否计入不活属于 Ren 的选择，所以这一对只在逐步读法的这一判定下显示活与否由汲取与依存的关系决定。`grazing` 不依赖这一判定：放牧者取用一个池，使另一个以池为依存的关系项落空，池不是汲取者，也从不活跃（P23c 更正，原标题“活跨越生成与退化”，原文“活与否不由生成与止息的样式决定，而由汲取与依存的关系决定”；见 §34 M7）。Ren 说加上公理可以定义好，好是整个空间的一部分；这里的 `Living` 是 G0 所计的 living 的一个结构部分，它不是生起的同义词，止息也不是不活（P23c 用语，原文“生成的同义词”）。
- **耗散使有限世界归于静止。** `rests` 把 §20（`generation_ceases`）与 `arising_iff_ceasing` 合起来：有限、活动可判定、平衡、耗散且生起者体现时，生起不再复现，所以止息也不再复现，活动最终不再改变。四个反例表明每个前提都不可少，其中 kindling 表明：在平衡与耗散之下，体现者的生起复现需要关系项无限，与 §17、§20 的“开放”相合（P23c 更正，原文“在耗散之下继续生成，需要展开越出每个有限部分”；flicker 与 unbalanced 是有限的反例，见 §34 M4）。平衡一行原用 `unbalanced`，它没有流，耗散空成立；P23c 改用 `leaking`，其中两侧的家族每步封闭且被取用（见 §34 M8）。

**作者反审。**

*反驳 1：大部分是把已有见证收集起来。* 部分是。新的内容是：世界与部分的定义及两类读法的嵌入；把前提的偶然性作为一个陈述（`contingent`），其中三个世界（`idle`、`restless`、`unbalanced`）与 `spending` 是新的；`living_crosses`；`rests` 及其每个前提的必要性；以及分离世界的无限由规律推出。`arising_iff_ceasing` 是 §26 的 `unceasing_iff` 读于世界，不算独立结果。

*反驳 2：有限世界的规律要求活动可判定，这削弱了“不加前提”。* 核心是构造性的，不用经典逻辑；计数需要可判定。经典地每个世界的活动都可判定，所以这不是关于展开的实质前提，而是构造性证明的要求。记录与模块都写明这一点。（P23c 补充：前一半对；后一半须写明，对每个世界陈述这一规律而不给可判定性，就要用排中律（`World.law_decides`）。可判定性因此作为逻辑承诺，与表示的其他承诺一起公开，见 §34 M2。）

*反驳 3：“每个前提都划出真部分”只对七个前提给出。* 是。`Census`、`TransmitsWithin`、`Around` 等其他前提没有逐一给出；前提的组合也没有逐一给出。完整的地图列入下一步。

*反驳 4：这被读成“理论不需要公理”。* 不是。本节显示哪些陈述不需要前提、哪些前提划出哪些部分。规范方向仍经 G0；“不加实质公理的整体演绎必然性”仍是开放的首要目标（[根基章节](../../../../theories/becoming/chapters/BECOMING-FOUNDATION.md)）。

**边界。** 不含伦理谓词，不评价任何部分；`Living` 只是逐步读法的结构条件；有限世界的规律要求活动可判定；部分的列举不完全；只对离散步的读法陈述；“世界”“生起复现”“止息复现”是 AI 的表述，提议中的“生成的”“退化的”指哪个部分由 Ren 选择（P23c 更正，原文“‘世界’‘生成的’‘退化的’的这些读法是 AI 的表述，名称由 Ren 定”）。本节经第九次独立审查，更正见 §34。

## 31. 完整的陈述与完成审计（P23）

2026-10-09。Ren 的指示：“aim a complete theory of becoming, and finish related work”。计划 P23 把已检查的结果作为一个整体陈述一次，并按这个陈述更新完成审计与开放纲领。本轮不新增 Lean 声明，也不新增成果身份。

```text
Result(s): 复用脊柱的全部记录；无新增成果身份
Delta: 正典章节新增“理论的完整陈述”一节（整体、生与灭、后续活动的条件、分化、地位五部分，每条标明表示／规律／定理／
       公理／读法／开放）；第 8 节重排为现状表与四类开放项（属于 Ren 的选择、哲学根据、经验对应、进一步的证明）；
       根基章节完成审计各行加入脊柱的证据，并加“脊柱的现状”一段；根基记录 theory-of-becoming-foundation 的下一步、
       验证范围、相关与历史；generation-is-replenishment 的“生起的生命”改为“生起的体现关系项”，只在 Ren 的读法下读作生
Supplied premises / correspondence: 无新前提；规律对脊柱所表示的世界成立（离散的步、自然数的量、共同索引；P23c 补：规律需要时活动可判定）
Evidence: 现有回执与记录；无新证明
Boundary: 形式陈述的完整不是必然性已证；每个生成能否这样表示是开放的哲学根据；读法与名称由 Ren 定
Integration: 计划 P23；根基章节第 5 节；为 P23b 的第九次审查提供完整陈述
```

**解读。**

- **“完整”指什么。** 完整的陈述在这个意义上完整：章节的每条主张都标明地位（表示、规律、定理、公理、读法或开放），每个开放项都归入四类之一。它不在这个意义上完整：整体的必然性已证。两种意义在章节、根基章节与根基记录中都分开写。
- **规律与表示。** 不加前提的规律（§26、§29）对每个世界成立，但“世界”是脊柱所表示的世界：离散的步、自然数的量、把条件与关系项对应起来的共同索引（§17），以及规律需要时每一步的活动可判定（P23c 补充，见 §34 M2）。每个生成是否都能这样表示，是一项哲学根据；不能这样表示的部分，需要扩展脊柱，例如连续时间或实数量的表示及其对应。两项分别列入第 8 节的哲学根据与进一步的证明。
- **四类。** 原第 8 节的每个“下一步”都有归类（AI 逐项对照了重排前后的文本）：读法与名称归 Ren 的选择，整体演绎、普遍实践根据、科学探究的根基与 G0／A／N 的根据归哲学根据，机制的实际实现、前提是否被实际展开满足与方向假说归经验对应，其余归进一步的证明，并按依存与同一、读法、继续生成、整体与部分、演化、共同活动、智慧分组。审查不是一类开放内容，单独列出。
- **完整标准的达成（P23c 补充，见 §34 M9）。** 计划 §9 的四项标准中：第 1 项（每种形态都在脊柱上）与第 4 项（开放项分类）满足；第 2 项在 P23c 后满足，可判定性在每处表示清单中公开；第 3 项在 P24 后对世界层面的十个前提满足（八个彼此独立，两个由其余推出），相对于延续关系、更新关系、衰减的储备或条件家族的前提（`NoSplit`、`RenewedBy`、`Decays`、`Depletes`、`Around`）没有映射，标准中的“混合的”部分没有在 `Space` 中定义，“生成的”“退化的”部分指什么由 Ren 选择。
- **完成审计。** 根基章节第 5 节表中每行的“现有证据”加入脊柱的结果，“剩余推论”不变：脊柱定位了整体主张的实质剩余（规律属于整体，前提划出部分），但不完成通向关系构成的连接。根基记录的下一步相应改写，保留原来的中心推论。
- **措辞更正。** generation-is-replenishment 原写“每次生命的生起都是一次补充”。“生命”是 Ren 的读法，不是定理的内容；现在写作生起的体现关系项自身是其他关系项的条件，只在 Ren 把它读作“生”时才读作生命。

**作者反审。**

*反驳 1：“完整的陈述”会被读成理论已经完成。* 章节在说明处与第 11 条、第 8 节开头、根基章节“脊柱的现状”与根基记录中都写明：这是形式陈述的完整，不是必然性已证。现状表中整体演绎、普遍实践根据、智慧之根与科学探究的根基仍标为开放。

*反驳 2：四类的划分本身是 AI 的判断。* 是。例如表示的范围既是哲学根据（每个生成能否这样表示），又引出进一步的证明（扩展脊柱），两面分别列出。Ren 可以重新归类；归类不改变任何结果。

*反驳 3：没有新的证明。* 对。依结果工作流，重述、汇集与复查不是新的独立结果，本轮不登记新成果身份；它的贡献是地位的标注、开放项的归类与完成审计的证据。

**边界。** 无新定理；规律只对脊柱所表示的世界成立；归类是 AI 的判断；“生”“生生”的读法与名称由 Ren 定。本节经第九次独立审查，更正见 §34。

## 32. 前提的地图（P24）

2026-10-09。按同一指示继续计划 P24，在第九次审查进行时完成。计划对“完整”的第三条读法要求每个动力学前提划出整个空间的真部分；§30 对七个前提给出了这一点。本节补上其余世界层面的前提，并把前提彼此对照：哪些推出哪些，其余是否独立。新 L3 模块 `Becoming.Premises`（导入 `Space`）。成果记录：[map-of-premises](../../../../theories/becoming/results/records/map-of-premises.md)。

```text
Result(s): 复用 space-and-its-parts（World、rests、unbalanced、mutualism）、no-finite-part-bears-taking（Enclosed、
           giving_needs_uptake）、more-needs-renewers（Census、Distinct）、evolution-on-descent（DescendsAt、
           TransmitsWithin）、reserve-defers-ending（carries_zero）、life-as-condition-of-life（Embodied、Mutualism）；
           新增 map-of-premises
Delta: Premises：世界上的普查（Counted）与有界传递（Transmitting）；蕴含 Dependent.carried、Finite.counted、
       Finite.enclosed、acting_of_enclosed、Finite.acting、follows；premises、Premised、MeetsAllBut；八个独立性世界
       strained、unbalanced、scatter、morsel、keeping、latent、multitude、novel；independent、none_follows；
       mutualism_premised、premised_rests；列表工具 beyond、keep 及其引理
Supplied premises / correspondence: Finite.counted 与 premised_rests 要求活动可判定；acting_of_enclosed 要求每一步都被围住；
       其余是关于具体世界的陈述
Evidence: 合并检查器回执（见记录）；外围桥接重跑；实例检查
Boundary: 只映射世界层面的八个前提；独立性相对于这八个；相对于另一读法的前提未映射；不评价任何部分
Integration: 计划 P24；完整性的第三条读法；为第十次审查（P24b）提供对象
```

| 声明 | 内容 |
|---|---|
| `Counted`、`Transmitting` | 世界上的普查：每步活跃的关系项被不重复地列出，所以每步只有有限多个活跃；世界上的有界传递：世系在一个界内传递每个依存 |
| `Dependent.carried` | 活动需要支持推出有储备承载（零储备，`carries_zero`） |
| `Finite.counted` | 活动可判定的有限世界有普查：从全部关系项中留下每步活跃的 |
| `acting_of_enclosed`、`Finite.enclosed`、`Finite.acting` | 只有活跃者取用且耗散时，在每个被围住的步上只有活跃者给予，因为那里给予需要取用；有限世界的每一步都被围住 |
| `premises`、`Premised`、`MeetsAllBut` | 八个前提的列表；满足全部；满足除 `P` 以外的全部而不满足 `P` |
| `independent` | strained（不满足活动需要支持）、unbalanced（平衡）、scatter（只有活跃者给予）、morsel（只有活跃者取用其所汲取的）、keeping（耗散）、latent（体现）、multitude（普查）、novel（有界传递），各满足其余七个 |
| `none_follows` | 所以没有一个前提由其余七个推出 |
| `mutualism_premised`、`premised_rests` | 始终活跃的互利者满足全部八个；有限、活动可判定且满足八个的世界中，生起与止息都不再复现，证明用到其中的平衡、耗散与体现（P25b 更正，原文“八个一起使…”；见 §38 O9）（P23c 用语，原文“生成与退化”） |

**解读。**

- **前提之间的结构。** 十个世界层面的前提里，有两个是另一个的较弱形式：有储备承载弱于活动需要支持（零储备），生起者体现弱于每个关系项体现。一个在活动可判定的有限世界中自动成立：普查（P25b 补“活动可判定”；不给可判定性而对每个有限世界要求普查，就蕴含排中律；见 §38 O9）。一个由另两个在被围住的步上推出（逐步的形式 `acting_across` 由 P25b 补出）：只有活跃者取用与耗散推出只有活跃者给予，因为耗散之下给予需要取用。这一条是新的：P13 的“给予需要取用”在世界层面读作，只有活跃者取用时，不活跃的关系项在有限世界中不能给予。
- **其余八个彼此独立。** 对每个前提，都有一个世界满足其余七个而不满足它。所以在这八个之中，没有一个前提藏在其余之中：每个都是对世界的独立限定（P25b 补“在这八个之中”：有限、被围住与可判定性不在地图中，加上它们，只有活跃者给予与普查就推出；多个见证没有流，关于流的四个前提在其中空成立，这足以证明独立，平衡另有取用与耗散每步起约束的见证 `draining_but`；见 §38 O9）。不满足普查的世界（multitude）与不满足只有活跃者给予的世界（scatter）都是无限的；这不是选择见证的巧合，而是蕴含要求的：有限世界有普查，并且在其中只有活跃者取用与耗散推出只有活跃者给予。scatter 中没有一步被围住：每步的交换都伸到无限多个关系项，耗散空成立，P16b 已经披露这种情形（`Spray`）。
- **novel：依存在世系中新形成。** 亲代烧掉燃料的两个单位，给子代一个单位，使子代开始作为条件而在；子代开始依存于亲代，而亲代自己从未有这一依存。所以有界传递不成立：世系中出现了新的依存，而不是传下来的。这是 §29 中“传递是前提”的见证：novel 满足其余七个前提，有界传递却不成立，所以传递不由它们推出。
- **全部一起。** 互利者满足全部八个，所以前提一起是相容的，并且不空：有活动，有依存，有体现；关于流的四个前提在其中空成立，因为没有流（P25b 补；见 §38 O9）。在活动可判定的有限世界中，满足八个的世界归于静止，证明用到其中的平衡、耗散与体现（§30 的 `rests`，生起者体现由体现推出）（P25b 更正，原文“在有限世界中，八个一起使世界归于静止”；见 §38 O9）。所以一个有限的世界若满足全部前提并使生起复现，是不可能的；生起复现需要越出某个前提，或者越出有限（P23c 用语，原文“继续生成”）。

**作者反审。**

*反驳 1：独立性见证太小、太人工。* 是小的。独立性只需要每个前提各有一个反模型；见证越小，越清楚地显示是哪个前提失败。它们不是对实际展开的描述，名称也由 Ren 定。

*反驳 2：“八个前提”的选择是任意的。* 部分是。这八个是脊柱定理在世界层面用到的动力学前提；相对于另一读法的前提（延续关系、更新关系、衰减的储备、条件家族）不是世界本身的限定，需要另一种地图；流中每个参与者只列一次是表示的条件。加入新前提时，独立性要重新检查，可能出现新的蕴含。

*反驳 3：premised_rests 只是 rests 的重述。* 是推论，不是独立结果；它显示的是：满足全部前提的有限世界没有生起复现的余地（P23c 用语，原文“继续生成”）。新的内容是蕴含、两个新前提与独立性。

**边界。** 无伦理谓词，不评价任何部分；只对离散步的读法陈述；有限世界的蕴含要求活动可判定；只映射世界层面的八个前提；前提与世界的名称是 AI 的表述，由 Ren 定。本节尚未经独立审查（计划 P24b）。

## 33. 开放（P25）

2026-10-09。按 Ren“aim a complete theory of becoming, and finish related work”继续，作为计划 P25。§30 的 `rests` 用有限使世界归于静止；§31（P23）陈述的理论在其第 8 节把这一点列为开放：在普查与被围住之下（而不只是有限时），全部前提是否使世界归于静止。本节回答：世界不必有限；起作用的是每步立着的有限多（活动的普查连同每个关系项体现），连同被围住（P25b 更正，原文“起作用的是被围住，不是有限”；见 §38 O1）。新 L3 模块 `Becoming.Openness`（导入 `Premises`）。成果记录：[continued-change-needs-openness](../../../../theories/becoming/results/records/continued-change-needs-openness.md)。

```text
Result(s): 复用 no-finite-part-bears-taking（Balances.runs_down、rise_lowers_on、Enclosed.around、Dissipative）、
           rising-and-falling-in-one-exchange（Balances.fall_taken）、generation-is-replenishment（ComesToStand.rises、
           Handing）、map-of-premises（Premised、Counted、beyond）、space-and-its-parts（World、ArisingRecurs、
           CeasingRecurs、Embodied；P23c 前为 Generative、Degenerative）、coming-and-ceasing-keep-pace（Ceases）、Renewal 的 falls_finitely；
           新增 continued-change-needs-openness
Delta: Openness：所立者的普查（Web.StandingCensus）与围住所立者的步（Flow.AroundStanding）；stock_eq、
       Enclosed.aroundStanding、fall_lowers_on、standing_runs_down、standing_never_rises、change_lowers、stills；
       世界上的 standingCensus、rises_of_arises、falls_of_ceases、rests_around、rests_enclosed、arising_opens（P23c 前为 generation_opens）；
       见证 exposed 与 exposed_world；列表工具 mem_append_left、mem_append_right
Supplied premises / correspondence: 平衡；耗散；所立者的普查；从某步起每步围住所立者。世界层面另要求活动的普查与每个
       关系项体现；rests_enclosed 与 arising_opens 要求关系项的相等可判定（P25b 起不要求，见 §38 O3）
Evidence: 合并检查器回执（见记录）；外围桥接重跑；实例检查
Boundary: 要求每个关系项体现，不只是生起者；耗散只约束被围住的交换，exposed 中它空成立；不评价开放或静止
Integration: 计划 P25；回答理论第 8 节列出的开放项；为第十次审查（P24b）提供对象
```

| 声明 | 内容 |
|---|---|
| `Web.StandingCensus`、`Flow.AroundStanding` | 每步立着的条件被不重复地列出；一步围住所立者：某个不重复、跨过该步封闭的家族包含该步前后立着的每个条件 |
| `StandingCensus.stock_eq`、`Enclosed.aroundStanding` | 所立者的总水平就是包含它的任何不重复家族的存量；关系项的相等可判定时，被围住的步围住所立者 |
| `standing_runs_down`、`standing_never_rises` | 跨过围住所立者的步，总水平下降至少为取用围住它的家族的形成数，所以不上升 |
| `fall_lowers_on`、`change_lowers` | 被耗散的家族中成员下降使存量下降（它被取用）；所以任何条件的水平上升或下降都使总水平下降 |
| `stills` | 从某步起每步都围住所立者时，没有条件的水平在任意晚的步变化 |
| `standingCensus`、`rises_of_arises`、`falls_of_ceases` | 活动的普查与每个关系项体现给出所立者的普查；体现的关系项生起即上升，止息即下降 |
| `rests_around`、`rests_enclosed` | 有普查、每个关系项体现、平衡且耗散的世界，从某步起每步围住所立者（相等可判定时：每步被围住）时，生起与止息都不再复现（P23c 用语，原文“生成与退化”） |
| `arising_opens` | 所以这样的世界生起复现时，并非从某步起每步都被围住（P25b 更正，原文“在任意晚的步有不被围住的步”，构造上更强；见 §38 O11）（P23c 改名，原名 `generation_opens`，原文“生成不息”） |
| `exposed`、`exposed_world` | Handing 的两侧另外在每步从无限多个地关系项各取一个单位再还回：满足全部八个前提，生起复现，没有一步被围住（P25b 补：总水平每步都是一；活动需要支持、有界传递与耗散在其中空成立；见 §38 O5、O6） |

**解读。**

- **总水平是只降不升的量。** 平衡与耗散一起，使跨过被围住的步的总水平不上升；更强地，任何水平的变化都使它严格下降。上升被给予，而在被围住的步上给予需要取用；下降被取用。所以变化本身消耗总水平。自然数的量只能严格下降有限多次（`falls_finitely`），所以被围住的展开中，变化只能有限多次。
- **世界的有限不是关键。**（P25b 更正，原标题“有限不是关键”：每步立着的有限多仍是关键，见 §38 O1。）§30 的 `rests` 要求关系项总共有限；这里关系项可以无限多，只要每步立着的有限多个被列出，且每步的交换被某个有限家族围住。两者都不是对方的特例：`rests` 要求有限而只要求生起者体现；这里不要求有限而要求每个关系项体现。
- **开放是生起复现的必要条件。** 读作对立面：满足普查、体现、平衡与耗散的世界若生起复现（P23c 用语，原标题与原文“生成不息”），那么在任意晚的步，有一步的交换伸到每个有限家族之外。这是 §17、§20（P13、P15）中家族层面的开放在世界层面的陈述，而且用变化的所立者，不是固定的家族。
- **exposed：开放不能去掉。** Handing 的两侧来回传递一个单位的水平，生起复现；另外在每步与无限多个地关系项交换一个单位，取用再还回，使地的水平保持为零。由于每步取用无限多个关系项，没有有限家族跨过任何一步封闭，所以耗散空成立。它满足全部八个前提（普查只列出立着的那一侧），生起复现。所以在八个前提之下，被围住这一条件不能从 `rests_enclosed` 中去掉（P25b 补：它说明八个前提推不出被围住；推不出开放要另一个见证，满足八个而每步被围住的互利者（`openness_contingent`）；它的开放是零净量的交换；见 §38 O4、O6）。

**作者反审。**

*反驳 1：exposed 只是利用耗散的表示漏洞。* 是利用了一个已披露的特点：耗散只约束被围住的交换（P16b、`Spray`）。这正是要显示的：被围住不是由八个前提推出的，它是一个独立的、关于开放的条件。地的交换（取一再还一）是零净流，它不给两侧任何东西；它只使每一步不被围住。一个要求“每步只与有限多个关系项交换”的更强耗散会排除它，但那是另一个前提，应当公开地加入，而不是藏在耗散里。

*反驳 2：要求每个关系项体现太强。* 是比 `rests` 的“生起者体现”强。止息读作下降，需要止息者体现；生起读作上升，需要生起者体现。只要求生起者体现时，`stills` 仍使生起停止吗？不立着却活跃的关系项可以不断止息而不改变水平；所以止息复现的部分需要更多。是否可以只用生起者体现得到生起复现的部分，列为下一步（记录的 next_delta）（P25b：已有答案：只有活动的普查时不能，kindling 每步被围住而生起不息（`rest_needs_standing`）；有所立者的普查时生起停止（`arising_stops`），止息不一定（dusk）；见 §38 O2）（P23c 用语，原文“生成停止”“退化部分”“生成部分”）。

*反驳 3：可判定的相等是额外前提。* 不是构造性证明的要求：被围住的步不是不围住所立者，而 `stills` 比较的是自然数，判定已在那里；P25b 去掉了这一要求（`Enclosed.around_not_not`）。`rests_around` 不要求它，直接以围住所立者为前提（P25b 更正，原文“是构造性证明的要求：把立着的两个列表合并为一个不重复的家族要判定相等。经典地它总是成立”；见 §38 O3）。

**边界。** 无伦理谓词，不评价开放或静止；只对离散步与自然数的量陈述；“开放”“被围住”“所立者”的读法与名称是 AI 的表述，由 Ren 定。本节经[第十次独立审查](BECOMING-P23C-P24-P25-REVIEW.md)，更正见 §38。

## 34. 第九次独立审查与更正（P23c）

2026-10-09。按同一指示继续。另一 agent（Claude Opus 5.5，未参与撰写）独立审查了 P18b（§27）、P19（§26）、P20（§28）、P21（§29）、P22（§30）与 P23（§31）（[审查](BECOMING-P18B-P23-REVIEW.md)）。它在仓库之外从前导重新编译核心闭包的 27 个模块，1571 条源声明的公理报告全空；闭包的 4423 个常量中依赖公理的只有 30 条编译器生成的 `injEq` 引理，都只依赖 `propext`，与回执所列相同；回执、源哈希、保留产物、引用哈希与证明绑定都对，数学全部接受，Lean 中没有数学错误。第八次审查的 L1–L10 全部关闭。它提出十项（M1–M10）：一项替 Ren 选择了读法（M1，最严重），四项省略前提（M2、M4、M5、M6），一项散文中的错误（M3），两项缺少反例（M7、M8），两项表述与记账（M9、M10）。P24（§32）与 P25（§33）在审查期间提交，审查没有读；其中受 M1 影响的用语一并更正。本节记录逐项处理。探针 N1、N4–N7 移入核心，公理报告为空。§26、§28–§33 与英文段落中受影响的句子已就地更正并标明；原文见提交 `a69455e3`。

```text
Result(s): 更正 space-and-its-parts（M1、M2、M7、M8）、evolution-on-descent（M3、M6）、
           rising-and-falling-in-one-exchange（M5）、coming-and-ceasing-keep-pace（M1 的对应说明）、
           theory-of-becoming-foundation（M2、M10(b)）、generation-is-replenishment（M10(a)）；随 M1 改名更正
           map-of-premises 与 continued-change-needs-openness；没有新的成果记录
Delta: Space：Generative、Degenerative、generative_ofRoles、degenerative_ofRoles、generative_iff、handing_generative 改名为
       ArisingRecurs、CeasingRecurs、arisingRecurs_ofRoles、ceasingRecurs_ofRoles、arising_iff_ceasing、handing_arising（M1）；
       Undecided、undecided_world 与 law_decides（M2，探针 N1）；Grazing、grazing_world 与 grazing_not_self，
       living_crosses 的不活一角改用 grazing（M7，探针 N6）；Leaking 与 leaking_world，rests_needs 的平衡一行改用它
       （M8，探针 N7）。Evolution：selected_uniform、unselected（M3，探针 N5）；Slack（M6，探针 N4）。Openness：
       generation_opens 改名为 arising_opens。模块说明、章节、根基章节、记录与计划的用语、标注与前提（M1–M10）
Supplied premises / correspondence: 不变；可判定性作为逻辑承诺与表示的其他承诺一起公开；提议中“生成的”“退化的”
       指哪个部分列为 Ren 的选择
Evidence: 合并检查器回执 20261009T132323.308231Z（1016 项定理／1662 项声明审计，核心闭包 29 个模块，包 27 个模块，
          源声明的公理报告全空）；外围桥接重跑 20261009T132432.792943Z；实例检查通过
Boundary: 不含伦理结论；不替 Ren 选择任何读法；新名称是建议；探针与新见证都是最小见证
Integration: §26、§28–§33 的更正；审查 §4 的第 1–6 项完成，第 7 项（Ren 的选择）保持开放
```

### 34.1 逐项处理

| 项 | 审查所见 | 处理 |
|---|---|---|
| M1 | P22 把 Ren 提议中的“generative, degenerative”读作某个关系项在任意晚的步生起／止息，据此在正典中陈述有限世界中两者是同一部分、彼此交叠；Ren 2026-10-09 说二者不重叠，正典没有提到这句原话，也没有把这一读法列为 Ren 的选择。读法始于 P19 的作者读法 | 世界的部分按活动命名：`World.ArisingRecurs`、`CeasingRecurs`、`arising_iff_ceasing`（生起复现／止息复现），连同 `arisingRecurs_ofRoles`、`ceasingRecurs_ofRoles`、`handing_arising`；`Openness` 的 `generation_opens` 改为 `arising_opens`。模块说明写为“states one structure for that proposal (an AI reading)”，写出 Ren 的原话与脊柱上的两种读法：活动的读法（生起复现与止息复现，有限世界中重合）与关系的读法（更新的形成与消耗的形成，作为关系不重叠，`Web.renewing_not_consuming`）。章节第 2、4 条，§2，§8 现状行，词汇表，记录的标题与对应，§26、§30 与根基第 1 行改写；词汇表保留 Ren 的用语“生成的／退化的”一行，指向关系的读法，另列“生起复现／止息复现”。章节 §8 Ren 的选择新增第一项：提议中的“生成的”“退化的”指哪个部分。计划 P22 行注明：退化的部分实现为止息复现，消耗不在其中 |
| M2 | 有限世界的规律需要活动可判定，对每个世界而不给可判定性就是排中律（探针 N1）；表示承诺的三处清单漏掉了它，根基第 1 行写“不加前提” | 三处清单（章节说明处、§8 哲学根据、根基“脊柱的现状”）加入“规律需要时每一步的活动可判定”；§8 哲学根据另加“逻辑承诺”一项。N1 移入核心：`Undecided`（一个关系项，没有流，活动以四为周期：不活跃、活跃、`Q`、不活跃）与 `World.law_decides`：若每个有限世界中生起复现都推出止息复现，则任何命题都有 Q ∨ ¬Q。根基第 1 行与根基记录的关联说明写为“活动可判定的有限世界”；第 4 条 `rests` 一句加入可判定；“活动不可判定时的规律”在进一步的证明中写明只在经典逻辑下成立，不能进入纯核心。§30 反驳 2 就地补充 |
| M3 | `price` 被说成把从亲代到后代的变化分为选择项与传递项；等式分解的是后代的总量，所谓选择项在没有任何选择时也不为零（探针 N5） | `Evolution` 的模块说明、`selected` 与 `price` 的说明、章节第 2 条与 §2、记录的主张、§29 与词汇表改为：后代的总量分为亲代的量按其后代加权的总量与传递的变化；加权总量不是真正的选择项，真正的选择项（后代数与量的协方差）没有陈述。N5 移入核心：`selected_uniform`（每个亲代都有 k 个后代时，加权总量是亲代总量的 k 倍）与 `unselected`（一个亲代、一个后代，量都是五：加权总量为五，传递项为零）。`selected_le` 与 `selection_within` 作为关于加权总量的陈述不变 |
| M4 | 第 4 条末句“在耗散之下继续生成，展开须越出每个有限部分”省略平衡与生起者体现；`flicker` 与 `unbalanced` 是有限的反例 | 改为：在平衡与耗散之下，不重复的有限家族中体现的成员在任意晚的步生起，家族就在任意晚的步不封闭，被围住时汲入（`Web.generation_opens`、`generation_draws_in`）。词汇表“汲入”一行与 §30 解读中 kindling 一句随之更正 |
| M5 | (a) “在耗散之下”上升伴随下降，缺“该步被耗散的家族”（探针 N2 `Spray`）；(b) “消耗前提由平衡与耗散推出”缺“且被取用”（探针 N3 `Still`） | (a) 章节第 4 条首句、记录 rising-and-falling-in-one-exchange 的标题、§9 Dissipation 与 Roles 两行、根模块与包说明改为“在家族被耗散的一步上”；§28 解读与英文 P20 就地更正。(b) §8“继续生成”行、§9 Dissipation 行、根模块与计划 P20 行改为“对各步家族被耗散且被取用的事件”。N2 与 N3 留在审查的探针中：更正后的陈述已写出被缺的前提 |
| M6 | “传下来的所需曾在给予之步被满足”只在界 δ 为零时成立（探针 N4） | 章节第 8 条、§2、§8 演化行与 §9 Evolution 行改为：传下来的所需至多比给予之步条件的水平多传递的界，界为零时曾在那里被满足。N4 移入核心：`Slack`（池、亲代与子代；流平衡、只有活跃者给予、活动需要支持、对池的依存在界一之内传递；子代跨第 0 步从亲代而来，所需为二，池在给予之步与每一步都只有一）。§29 就地更正 |
| M7 | `living_crosses` 中“生成复现而有不活”的唯一见证 `spending`，依赖 Ren 尚未作出的选择：终结之步对承担自身的体现关系项的自我汲取是否计入不活 | N6 移入核心：`Grazing` 与 `World.grazing`、`grazing_world`：在 `Handing` 上加一个池、一个放牧者与一个食草者，两者以需要一与二依存于池，都在第 0 步活跃，放牧者在这一步从池取用一个单位。世界有限、生起复现、`Dependent`、平衡、`Acting`、`Taking`，而不 `Living`：放牧者的事件侵蚀食草者对池的依存；池不是汲取者，也从不活跃，放牧者自己的依存在该步之后仍满足（`grazing_not_self`）。`living_crosses` 的这一角改用 grazing；`spending` 保留在 `contingent` 中，模块说明写明它只在那一判定下不活。§30 解读就地更正 |
| M8 | `rests_needs` 的平衡见证 `unbalanced` 没有流，耗散空成立（探针 N7） | N7 移入核心：`Leaking` 与 `World.leaking`、`leaking_world`：保留 `Handing.web`，持有者每步取用自己的一个单位而不给予。世界有限、生起复现、耗散、每个关系项体现，两侧的家族在每步封闭且被取用，只有平衡不成立。`rests_needs` 的平衡一行改用它；`unbalanced` 保留在 `contingent` 与 `Premises` 中。模块说明写明：`flicker` 的耗散在尾部空成立是被迫的，有限、平衡、耗散的世界中取用不复现（`Flow.Dissipative.finite_ceases`） |
| M9 | (a) “规律”的标注把定义上的同一、算术恒等式与二值和有限的推论归为一类；(b) 智慧一项归入进一步的证明；(c) 计划的四项完整标准中第 2、3 项部分未满足，现状没有写出 | (a) 章节第 2 条分为三种并各自标注：〔定义上的同一〕`change_readings`；〔算术恒等式〕`over_stretch`、`price`；〔二值与有限的推论〕`keep_pace`、`coming_recurs_iff`、`arising_iff_ceasing`。(b) 智慧一项移到经验对应（两种语言）。(c) 计划 P23 行与 §31 写明各标准的达成，见 §31 的补充 |
| M10 | (a) 四份记录的审查时间晚于包含它的提交；(b) 根基记录的中文用语与章节不一致；(c) §29 反驳 3 残留“给予者” | (a) generation-is-replenishment 改为 12:05:00，早于 P23 提交；evolution-on-descent、space-and-its-parts 与 theory-of-becoming-foundation 在本次内容修订中刷新为本次修订的时间。审查没有读的 map-of-premises 与 continued-change-needs-openness 的审查时间同样晚于各自的提交，本次内容修订时一并刷新。(b) 根基记录的关联说明改用章节的用语：止息、开始与不再作为条件而在、开始成立与不再成立，并写出可判定。(c) 改为“只说给予它的形成给予” |

### 34.2 新的已检查声明

| 模块 | 声明 | 内容 |
|---|---|---|
| Space | `World.ArisingRecurs`、`CeasingRecurs`、`arisingRecurs_ofRoles`、`ceasingRecurs_ofRoles`、`arising_iff_ceasing`、`handing_arising` | 改名，陈述不变：某个关系项在任意晚的步生起／止息；两类读法中读法相同；有限且活动可判定的世界中两者等价 |
| Space | `Undecided.act`、`four`、`le_four`、`arises_at`、`web`、`decides`、`World.undecided`、`undecided_world`、`law_decides` | 一个关系项，活动以四为周期：不活跃、活跃、`Q`、不活跃。世界有限，不论 `Q` 如何，每个周期开始时生起；任何止息都判定 `Q`。所以有限世界的规律对每个世界成立就推出排中律 |
| Space | `Grazing.Relatum`、`web`、`flow`、`side_taking` 等，`World.grazing`、`grazing_finite`、`grazing_arising`、`grazing_balanced`、`grazing_acting`、`grazing_taking`、`grazing_dependent`、`grazing_not_self`、`grazing_world` | `Handing` 的两侧加上池、放牧者与食草者；第 0 步放牧者从池取用一个单位，侵蚀食草者的依存。有限、生起复现、`Dependent`、平衡、`Acting`、`Taking`，而不 `Living`；放牧者只汲取池，池从不活跃，放牧者自己的依存在该步之后仍满足 |
| Space | `Leaking.flow`、`takes`、`World.leaking`、`leaking_world` | `Handing.web` 上，持有者每步取用自己的一个单位而不给予。有限、生起复现、耗散、每个关系项体现，不平衡；两侧的家族每步封闭且被取用 |
| Space | `living_crosses`、`rests_needs`（更正） | 生起复现而有不活的一角用 grazing；平衡一行用 leaking |
| Evolution | `selected_uniform`、`unselected` | 每个亲代都有 k 个后代时，加权总量是亲代总量的 k 倍；一个亲代、一个后代、量都是五时，加权总量为五，传递所升高与降低的都为零 |
| Evolution | `Slack.Relatum`、`web`、`flow`、`dependent`、`slack` | 流平衡、只有活跃者给予、活动需要支持、对池的依存在界一之内传递；子代从亲代而来，所需为二，池在给予之步与每一步的水平都是一：传下来的所需可以从未被满足 |
| Openness | `World.arising_opens` | 改名，陈述不变 |
| Premises | `premised_rests` | 陈述用新名：不生起复现，也不止息复现 |

### 34.3 审查列出的会改变判断的结果

1. 生成的与退化的（M1）：有限世界的规律以生起复现与止息复现陈述，正典中不再说“生成的”与“退化的”是同一部分、彼此交叠；Ren 的原话与关系的读法写在旁边；读法列为 Ren 的选择。完成。
2. 可判定性（M2）：加入每处表示清单，在根基第 1 行、根基记录与第 4 条恢复，并作为逻辑承诺列出；不可判定时的规律就是排中律，由 `law_decides` 证明。完成。
3. `price`（M3）：写明它分解什么，“选择项”只留给协方差。完成；协方差形式仍列为进一步的证明。
4. 完整陈述中的前提（M4–M6）：完成。
5. 见证（M7、M8）：grazing 与 leaking 移入核心。完成。
6. 表述（M9、M10）：完成。
7. Ren 的选择保持开放：提议中“生成的”“退化的”的读法（新增）；“生”“生生”与第二个“生”的读法，包括依赖消耗的生起是否算作生成；终结之步对承担自身的体现关系项的汲取是否计入不活、对哪些汲取者；接续的读法与生生不息读到哪个层次；以之为生与世系是否作为直接的估值；名称。
8. 审查没有构造而仍开放的：`rests` 中体现必要性的非空见证（尾部空成立是被迫的，见 M8）；`price` 的协方差形式；外围中经典逻辑下的有限世界规律。

### 34.4 作者反审

*反驳 1：改名只是换词。* 不是。旧名把 Ren 的用语给了一种读法，正典据此把“生成的与退化的是同一部分”陈述为定理，而 Ren 说二者不重叠。新名说出定理实际说的：活动的复现。Ren 的用语留给 Ren 选择，脊柱上的两种候选都写出。关系的读法（`RenewingIn`、`ConsumingIn`）相对于一个形成；把它提为世界的部分，需要选择怎样对形成量化，这也属于 Ren 的选择之后的工作，不在本次。

*反驳 2：`law_decides` 削弱了“不加前提的规律”。* 它不削弱定理，而是写明定理的逻辑承诺：在纯核心中规律以可判定为前提，这正是它能构造性地证明的形式；不加这一前提，规律就是排中律，不能进入纯核心。经典地每个世界的活动都可判定，所以它不是关于任何展开的前提，但它是逻辑的承诺，按 Ren 的优先指令与方法、模型、对应与规范的前提分开公开。

*反驳 3：grazing 也依赖读法。* 它依赖逐步读法中“侵蚀”的定义：活跃者的汲取使另一个关系项已满足的依存在该步之后落空。这是 `Living` 的定义本身，不是附加的选择。它不依赖终结之步自我汲取的判定：不活的事件汲取的是池，池不是汲取者，也从不活跃（P25b 更正：它在 §8 所写的选择之外，但被侵蚀的食草者在该步之后不活跃（`grazing_browser_ends`）；活动需要支持时，对持续不变的依存的每次侵蚀都使依存者在该步之后不活跃（`Web.Dependent.inactive_below`；P29b 更正，原文“都与依存者的终结同时”：依存者原本休眠时没有终结，见 §42 R1），所以“不依赖终结之步的判定”预设了 Ren 的选择只涉及被汲取者自身的终结；见 §38 O10）。它仍然依赖两类读法的同一对应，这是表示的前提，已公开。

*反驳 4：既然 `selected` 不是选择项，`price` 还有什么用。* `price` 是会计恒等式，审查与本研究都这样说；它的用处在于加权总量受条件的水平所限（`selected_le`、`selection_within`），这把支持对给予的约束写进后代的总量。真正的选择项需要整数或有理数的量与均值，列为进一步的证明。

**边界。** 不含伦理谓词；不改变任何读法选择的地位，新增的一项（提议中“生成的”“退化的”的读法）列为 Ren 的选择；新名称是建议；探针与新见证都是最小见证；可判定性是公开的逻辑承诺。本节的更正经[第十次独立审查](BECOMING-P23C-P24-P25-REVIEW.md)，见 §38。

## 35. 止息需要生起与静止定理（P26）

2026-10-09。按 Ren“aim a complete theory of becoming, and finish related work”继续，作为计划 P26。§30 的 `rests` 要求世界有限，§33 的 `rests_around` 不要求有限而要求每个关系项体现；记录 continued-change-needs-openness 的 next_delta 列出：只要求生起者体现时，被围住的世界是否也归于静止。本节的回答：再有所立者的普查时是肯定的（只有活动的普查时是否定的，kindling；P25b 更正，原文“本节的回答是肯定的”；见 §38 O2），靠的是一条计数的定律：在活动的普查之下，止息复现需要生起复现（普查定律）。于是归于静止只需生起停止，而生起者体现时，`stills` 使生起停止。由此得到一个静止定理，§30 的有限情形与 §33 的每个关系项都体现的情形都是它的推论。没有新模块：普查定律放在活跃形成的普查所在的 `Becoming.Population`，静止定理及其情形放在 `Becoming.Openness`。成果记录：新增 [ceasing-needs-arising](../../../../theories/becoming/results/records/ceasing-needs-arising.md)；修订 [continued-change-needs-openness](../../../../theories/becoming/results/records/continued-change-needs-openness.md)。

```text
Result(s): 复用 coming-and-ceasing-keep-pace（Arises、Ceases、Unceasing）、more-needs-renewers（Web.Census、search、
           length_le_of_sub）、map-of-premises（Counted、Finite.counted、keep）、space-and-its-parts（World、
           ArisingRecurs、CeasingRecurs、ArisingEmbodied、rests、dawn、dusk、separate）、continued-change-needs-openness
           （StandingCensus、AroundStanding、stills、rests_around）；新增 ceasing-needs-arising；修订 continued-change-needs-openness
Delta: Population：Web.arises_or_kept、arises_or_fewer、arises_within、arising_of_ceasing；Openness：World.arising_of_ceasing、
       Dawn.alive、mem_alive、alive_distinct、Dawn.census、World.census_one_way、World.comes_to_rest、Finite.standing、
       Finite.comes_to_rest、rest_needs_census；rests_around 改由静止定理证明
Supplied premises / correspondence: 普查定律：活动的普查（Census，每步活跃的形成列为不重复的有限表），世界层面另要求活动可判定；
       静止定理：活动的普查与可判定、所立者的普查、生起者体现、平衡、耗散、从某步起每步围住所立者
Evidence: 合并检查器回执 20261009T135303.461724Z（1029 项定理、1676 项声明审计、核心闭包 29 个模块、包 27 个模块，全部源声明公理报告为空）；
       外围桥接重跑 20261009T135417.468399Z；实例检查
Boundary: 普查定律是单向的（dawn）；普查不可少（dusk）；只对离散步与自然数的量陈述；不评价静止或开放；
       “生起复现”“止息复现”是活动的读法，是否为 Ren 提议中的“生成的”“退化的”由 Ren 选择（§34，M1；P25b 更正，原文“不是 Ren 的…”，见 §38 O8）
Integration: 计划 P26；回答 continued-change-needs-openness 的 next_delta；把 §30 与 §33 的两个静止定理合为一个
```

| 声明 | 内容 |
|---|---|
| `Web.arises_or_kept` | 从 N 到 T 之间，或者有形成生起，或者 T 时活跃的每个形成在 N 时已活跃（P27 推广为 `Listed.comes_or_held`） |
| `Web.arises_or_fewer` | N 之后某形成在 T 止息时，或者 N 之后有形成生起，或者 T + 1 时活跃的形成比 N 时少（P27 推广为 `Listed.comes_or_fewer`） |
| `Web.arises_within`、`Web.arising_of_ceasing` | 在普查之下，止息在任意晚的步发生时，活跃形成的数目不能一直下降，所以生起在任意晚的步发生（P27 把 `arises_within` 推广为 `Listed.comes_within`，`arising_of_ceasing` 成为 `Listed.coming_of_ceasing` 的活动读法） |
| `World.arising_of_ceasing` | 世界层面：活动可判定且有普查（`Counted`）时，止息复现推出生起复现 |
| `Dawn.alive`、`Dawn.census`、`World.census_one_way` | dawn 有普查（第 t 步活跃的恰是此前生起的 t 个），生起复现而止息不复现；dusk 止息复现而没有生起，所以按普查定律它没有普查 |
| `World.comes_to_rest` | 静止定理：有活动与所立者的普查、活动可判定、生起者体现、平衡、耗散，且从某步起每步围住所立者的世界，生起与止息都不再复现 |
| `World.Finite.standing`、`World.Finite.comes_to_rest` | 有限世界列出所立者（水平为正的关系项），每步围住它；所以 §30 的 `rests` 是静止定理的有限情形 |
| `World.rest_needs_census` | dusk 中没有立着的条件、没有取用与给予：所立者的普查为空表，每步围住所立者，生起者体现、平衡、耗散都成立，止息复现，没有活动的普查 |
| `World.rests_around` | 每个关系项都体现时，活动的普查列出所立者，活动由水平判定，于是由静止定理得到（P26 改证，陈述不变） |

**解读。**

- **普查定律是计数，不是有限。** 普查只要求每步活跃的形成有限且被不重复地列出，关系项总共可以无限多。一次之前没有生起的止息，使活跃的形成比先前少；数目是自然数，不能无穷地下降；所以止息在任意晚的步发生，迫使生起也在任意晚的步发生。反之不然：dawn 每步生起一个新的、从不止息，它有普查，止息不复现。dusk 中无穷多个初始形成依次止息而没有生起：它在第 0 步有无穷多个活跃者，没有普查。§30 的“活动可判定的有限世界中，生起复现恰当止息复现”于是分成两半：止息推出生起只需普查；生起推出止息需要有限，或别的约束同时活跃者的界。
- **静止定理。** 归于静止只需生起停止，止息由普查定律跟着停止。生起者体现时，生起就是水平上升；从某步起每步围住所立者时，平衡与耗散使水平不再变化（`stills`），所以生起停止。这把 §30 的 `rests`（要求有限，只要求生起者体现）与 §33 的 `rests_around`（不要求有限，要求每个关系项都体现）合为一个定理：两者的区别不在静止的机制，只在怎样得到所立者的普查与围住。有限给出两者；每个关系项都体现给出所立者的普查，围住仍是前提。
- **活动的普查不可少。** dusk 满足其余每个前提：没有立着的条件，所以所立者的普查是空表，每步都平凡地围住所立者；没有生起，所以生起者体现空成立；没有取用与给予，所以平衡与耗散成立。止息仍复现。失效的不是围住，而是普查：无穷多个不立着的活动可以依次终结，而不改变任何水平。止息在这里不读作下降，因为止息者不体现；普查定律越过了这一点，不要求止息者体现。
- **它仍是活动的读法。** 生起复现与止息复现是否为 Ren 提议中的“生成的”“退化的”由 Ren 选择（§34，M1；P25b 更正，原文“不是 Ren 的…”，见 §38 O8）；静止不是评价，开放也不是。

**作者反审。**

*反驳 1：普查定律只是平凡的计数。* 证明确实只用不重复列表的长度比较（`length_le_of_sub`）与自然数不能无穷下降。它的内容在于划分：§30 的同一部分在普查之下只剩一个方向，另一个方向需要更多，两半分别由 dawn 与 dusk 见证。它也解释了静止的世界中止息为什么停止，而不要求止息者体现：这正是 §33 反驳 2 留下的问题。

*反驳 2：静止定理是否只是把前提重排？* 它使两个已有定理成为同一定理的推论，并把 `rests_around` 的“每个关系项都体现”换成“生起者体现”加上所立者的普查。它覆盖的新情形是：关系项无限多、有活跃而不体现的关系项、只有生起者体现的世界。一个只被静止定理覆盖而不被 `rests` 与 `rests_around` 覆盖的见证容易构造（无限多个空闲的关系项旁有一个活跃而不立着的关系项），但本节没有在 Lean 中给出它，所以“严格更一般”只是陈述层面的比较，不是已检查的定理。

*反驳 3：可判定性是额外前提。* 普查定律在世界层面要求活动可判定，因为构造性的证明在下一步活跃者的表中查找此前不活跃者（`search`）。这是表示的逻辑承诺（§34，M2）。每个关系项都体现时，活动由水平判定，所以 `rests_around` 不另加它。

*反驳 4：耗散在这里只约束被围住的交换。* 是（P16b、`Spray`、§33 的 exposed）。静止定理以围住为前提，没有把开放藏进耗散；exposed 仍表明，八个前提之下去掉围住，生起可以不息。

**边界。** 无伦理谓词，不评价静止、开放或止息；只对离散步与自然数的量陈述；“普查”“静止定理”“归于静止”的名称与读法是 AI 的表述，由 Ren 定。没有所立者的普查时被围住的步（kindling 一类的世界）仍列为下一步（P25b：已回答，kindling 与 ember 每步被围住而生起不息，`rest_needs_standing`；见 §38 O2）。本节尚未经独立审查：第十次独立审查的对象截至 P23c。

## 36. 普查定律的一般形式与有界普查（P27）

2026-10-09。按 Ren“aim a complete theory of becoming, and finish related work”继续，作为计划 P27。§35 的普查定律只走一个方向：在普查之下，止息复现需要生起复现，dawn 表明反之不然。§30 的“活动可判定的有限世界中，生起复现恰当止息复现”于是分成两半，另一半（生起推出止息）需要什么，§35 只说“需要有限，或别的约束同时活跃者的界”。本节给出答案：需要的恰是计数的界。同时把普查定律推广到每步其成立者被列出的任何规定，活动与水平是它的两种读法，回答 ceasing-needs-arising 的下一步（同一规律读于水平）。没有新模块：一般形式放在 `Becoming.Population`，世界上的读法、水平的读法与见证放在 `Becoming.Openness`。成果记录：新增 [bounded-census-keeps-pace](../../../../theories/becoming/results/records/bounded-census-keeps-pace.md)；修订 [ceasing-needs-arising](../../../../theories/becoming/results/records/ceasing-needs-arising.md)。

```text
Result(s): 复用 ceasing-needs-arising（普查定律、Dawn.census、census_one_way）、coming-and-ceasing-keep-pace（ComesToBe、
           CeasesToBe、coming_recurs_iff、unceasing_iff）、space-and-its-parts（World、Finite、arising_iff_ceasing、dawn、
           Flow.still）、map-of-premises（Counted、Finite.counted、beyond）、more-needs-renewers（Census、search、
           length_le_of_sub）、continued-change-needs-openness（StandingCensus）；新增 bounded-census-keeps-pace；
           修订 ceasing-needs-arising
Delta: Population：Listed（每步成立者的列出）；Listed.comes_or_held、comes_or_fewer、comes_within、coming_of_ceasing
       （P26 的 Web.arises_or_kept、arises_or_fewer、arises_within 推广而来）；Listed.ceases_or_kept、ceases_or_more、
       ceases_within、ceasing_of_coming、coming_iff_ceasing；Web.Census 定义为活动的列出；Web.ceasing_of_arising、
       unceasing_iff_bounded；Openness：Web.StandingCensus 定义为水平的列出；StandingCensus.coming_of_ceasing、
       coming_iff_ceasing；World.CountedWithin、CountedWithin.arising_iff_ceasing、Finite.countedWithin、
       Finite.arising_iff_ceasing、dawn_unbounded；见证 Procession.web、Procession.census、procession、procession_world
Supplied premises / correspondence: 一般形式：每步成立者的不重复列出，每步可判定；有界形式另要求列表长度不超过同一个 B
Evidence: 合并检查器回执 20261009T141652.167311Z（1045 项定理、1697 项声明审计、核心闭包 29 个模块、包 27 个模块，
       全部源声明公理报告为空）；外围桥接重跑 20261009T141825.143331Z；实例检查。中间回执 20261009T141236.619967Z
       （外围 20261009T141402.494945Z）检查了推广之前的版本，保留为证据
Boundary: 界须对所有步统一；不给比率；不评价生起或止息；“生起复现”“止息复现”是活动的读法，是否为 Ren 提议中的“生成的”“退化的”由 Ren 选择（P25b 更正，原文“不是 Ren 的…”，见 §38 O8）
Integration: 计划 P27；回答 §35 留下的一半与 ceasing-needs-arising 的下一步；有限世界的规律成为有界普查定律的情形
```

| 声明 | 内容 |
|---|---|
| `Listed` | 一个规定每步的成立者被不重复地列出：每步有限多个成立，成员总共可以无限多 |
| `Listed.comes_or_held`、`comes_or_fewer`、`comes_within`、`coming_of_ceasing` | 普查定律的一般形式：不再成立复现需要开始成立复现（P26 的活动版本推广而来） |
| `Listed.ceases_or_kept`、`ceases_or_more` | 从 N 到 T 之间，或者有成员不再成立，或者 N 时成立的在 T 时都成立；一次开始成立若此前没有不再成立，使列表比 N 时长 |
| `Listed.ceases_within`、`ceasing_of_coming` | 列表都不长于 B 时，开始成立复现需要不再成立复现：列表不能长过 B |
| `Listed.coming_iff_ceasing` | 列表有界时两者同步 |
| `Web.Census`、`Web.ceasing_of_arising`、`Web.unceasing_iff_bounded` | 普查是活动的列出；有界普查之下，生起复现恰当止息复现（P29b 更正，原文“生成不息恰当止息复现”；见 §42 R5） |
| `Web.StandingCensus`、`StandingCensus.coming_of_ceasing`、`coming_iff_ceasing` | 所立者的普查是水平的列出；不再作为条件而在复现需要开始作为条件而在复现，有界时两者同步 |
| `World.CountedWithin`、`CountedWithin.arising_iff_ceasing` | 每步至多 B 个关系项活跃且被列出的世界中，生起复现恰当止息复现 |
| `World.Finite.countedWithin`、`Finite.arising_iff_ceasing` | 有限世界的每个普查都不长于关系项的数目；所以 §30 的 `arising_iff_ceasing` 是有界规律的情形 |
| `World.dawn_unbounded` | dawn 有普查而没有界 |
| `Procession.web`、`Procession.census`、`World.procession`、`procession_world` | 关系项 x 只在第 x 步活跃：每步一个，生起与止息都复现，关系项不是有限多个 |

**解读。**

- **一个计数定律，两个方向。** 列表每步记下成立者。一次不再成立，若此前（从 N 起）没有开始成立，就使列表比 N 时短；一次开始成立，若此前没有不再成立，就使列表比 N 时长。列表的长度是自然数：不能无穷地变短，所以不再成立复现迫使开始成立复现；有界时也不能无穷地变长，所以开始成立复现迫使不再成立复现。两个方向用同一个论证，只差界的有无。
- **三层。** 按每步成立者的计数，开始成立与不再成立的关系分为三层：有限且有界时两者同步（`coming_iff_ceasing`）；有限而无界时，不再成立需要开始成立，反之不然（dawn）；不再有限时，不再成立可以独自不息（dusk 没有普查）。§26 的有限家族定律与 §30 的有限世界定律都在第一层：有限家族或有限世界的每个列表都不长于成员数。procession 表明第一层不止于有限：关系项无穷多，每步只有一个在场。
- **一种变化，几种读法。** §26 说生起与止息、形成与消解、开始与不再作为条件而在是同一种变化读于活动、依存与水平。普查定律也是这样：它对每步其成立者被列出的任何规定成立，普查与所立者的普查是它读于活动与水平。读于依存（每步的依存被列出时）是直接的实例，留作下一步。
- **仍是活动与水平的读法。** 生起复现与止息复现是否为 Ren 提议中的“生成的”“退化的”由 Ren 选择（§34，M1；P25b 更正，原文“不是 Ren 的…”，见 §38 O8）；有界不是评价，procession 中的接替也不是。

**作者反审。**

*反驳 1：推广只是改名。* 推广去掉了活动这一具体规定：同一证明对任何规定成立，所以水平的读法不需要另证；P26 的三个辅助定理被替换而不是并存，`Web.arising_of_ceasing` 的陈述不变。被替换的名称记在 ceasing-needs-arising 的历史中。把 `Web.Census` 与 `Web.StandingCensus` 定义为 `Listed` 的两个读法，是定义上的相等，原有的证明不改。

*反驳 2：有界普查是不是另一种有限？* 不是：procession 的关系项无穷多，它不是有限世界（`procession_world`），而有界规律适用于它。有界只约束同时在场的数目，不约束总数。反过来，有限推出有界（`Finite.countedWithin`）。

*反驳 3：界须对所有步统一。* 是。只从某步起有界的情形可以把展开平移到那一步得到，但没有陈述；界随步增长而不超过某个慢速增长的函数时会怎样，也没有研究。这些列为下一步。

*反驳 4：procession 是不是太平凡？* 它是最小的见证：每步一个关系项在场，下一步换成下一个。它的作用只是表明有界规律越出有限世界；它不满足体现（水平都为零），所以不说明静止定理的情形。

**边界。** 无伦理谓词，不评价生起、止息或接替；只对离散步与有限列表陈述；“列出”“有界普查”“procession”的名称与读法是 AI 的表述，由 Ren 定。本节尚未经独立审查：第十次独立审查的对象截至 P23c。

## 37. 普查的平衡（P28）

2026-10-09。按 Ren“aim a complete theory of becoming, and finish related work”继续，作为计划 P28。§35 与 §36 的普查定律都是复现的定律：止息复现需要生起复现，列表有界时两者同步。它们留下三个下一步：带比率的版本（多少生起伴随多少止息）、只从某步起有界的情形、读于依存。本节给出三者。比率来自一个平衡：§26 对固定的有限家族证明了“终点成立的连同其间不再成立的，恰是起点成立的连同其间开始成立的”（`held_over_stretch`）；这里对每步的列表证明同一平衡，不要求固定的有限家族。没有新模块：平衡与依存的读法放在 `Becoming.Population`，水平的读法放在 `Becoming.Openness`。成果记录：新增 [census-balance](../../../../theories/becoming/results/records/census-balance.md)；修订 [bounded-census-keeps-pace](../../../../theories/becoming/results/records/bounded-census-keeps-pace.md) 与 [ceasing-needs-arising](../../../../theories/becoming/results/records/ceasing-needs-arising.md)。

```text
Result(s): 复用 ceasing-needs-arising（Listed、普查定律）、bounded-census-keeps-pace（有界定律）、coming-and-ceasing-keep-pace
           （mark、comings、ceasings、held_over_stretch、keep_pace）、more-needs-renewers（Distinct、mem_remove、total 的
           工具）、becoming-dependence-dynamics（Forms、Dissolves）；新增 census-balance；修订 bounded-census-keeps-pace、
           ceasing-needs-arising
Delta: Population：计数工具 mark_one、mark_zero、mark_add_not、total_congr_on、mem_insert、distinct_remove、
       marks_le_of_sub、balance_over_stretch；Listed.across、over_stretch、ceasings_within、comings_within；
       Web.Census.over_stretch；Web.DependenceCensus 与 forming_of_dissolving、forming_iff_dissolving；
       Listed.ceases_within、ceasing_of_coming、coming_iff_ceasing、Web.ceasing_of_arising、unceasing_iff_bounded
       改为界只需从某步 T 起成立；Openness：Web.decideComesToStand、decideCeasesToStand（实例）、
       Web.StandingCensus.over_stretch；StandingCensus.coming_iff_ceasing 改为界从某步起
Supplied premises / correspondence: 每步成立者的不重复列出，可判定；有界定律另要求从某步 T 起列表不长于 B
Evidence: 合并检查器回执 20261009T143148.368990Z（1061 项定理、1716 项声明审计、核心闭包 29 个模块、包 27 个模块，全部源声明公理报告
       为空）；外围桥接重跑 20261009T143305.859329Z；实例检查
Boundary: 平衡是计数，不是机制；不评价生起或止息；“生起”“止息”是活动的读法，是否为 Ren 提议中的“生成的”“退化的”由 Ren 选择（P25b 更正，原文“不是 Ren 的…”，见 §38 O8）
Integration: 计划 P28；回答 ceasing-needs-arising 与 bounded-census-keeps-pace 的下一步（比率、从某步起有界、读于依存）
```

| 声明 | 内容 |
|---|---|
| `marks_le_of_sub` | 不重复列表上某性质成立的成员，不多于另一张不重复列表上另一性质成立的成员，只要前者每个都在后者中且有后一性质 |
| `Listed.across` | 跨过每一步：步后列表的长度加上跨步不再成立的成员数，等于步前列表的长度加上跨步开始成立的成员数；跨步保持成立的成员在两张列表上计数相同 |
| `balance_over_stretch` | 每步平衡的计数在任一段步上平衡（逐步累加） |
| `Listed.over_stretch` | 任一段步上，终点的列表连同其间不再成立的，恰是起点的列表连同其间开始成立的 |
| `Listed.ceasings_within`、`comings_within` | 其间不再成立的至多是开始成立的加上起点的列表；开始成立的至多是不再成立的加上终点的列表 |
| `Web.Census.over_stretch`、`Web.StandingCensus.over_stretch` | 读于活动与水平：终点活跃（立着）的连同其间止息（不再作为条件而在）的，恰是起点的连同其间生起（开始作为条件而在）的 |
| `Web.DependenceCensus`、`forming_of_dissolving`、`forming_iff_dissolving` | 读于依存：每步的依存被列出时，消解复现需要形成复现；从某步起有界时两者同步 |
| `Listed.ceasing_of_coming`、`coming_iff_ceasing`、`Web.unceasing_iff_bounded` | 有界定律的界只需从某步 T 起成立；世界上的 `CountedWithin` 是 T = 0 的情形 |

**解读。**

- **进入与离开每步相抵。** 在每步有限的展开中，跨过一步，离开的与留下的合为步前的全部，进入的与留下的合为步后的全部；留下的在两边相同。所以步后的数目加上离开的，恰是步前的数目加上进入的。累加起来，任一段步上的离开与进入之差，恰是起点与终点的数目之差。§26 对固定的有限家族说过同样的话；这里不需要固定的家族，关系项总共可以无限多。
- **比率。** 由平衡，止息比生起多出的不超过起点的数目，生起比止息多出的不超过终点的数目。数目有界时，任一段步上生起与止息之差不超过界：两者不只同步复现，而且在任何长度的时段上数量相近。数目无界时（dawn），生起可以无限地超出止息。
- **一种变化，三种读法。** 普查定律与平衡读于活动（生起与止息）、水平（开始与不再作为条件而在）与依存（形成与消解），与 §26 中同一种变化的三种读法相应。依存的读法以依存对（形成、条件）为成员。
- **界从某步起。** 有界定律只用到某步之后的界：此前的数目可以任意大。所以“同时在场的有界”是一个最终的性质，与开头无关。
- **两条路线。** P26 与 P27 的复现定律直接用列表的长短证明；它们也是平衡的极限情形。两条路线一致，但没有合为一个证明，列为下一步。

**作者反审。**

*反驳 1：平衡只是记账。* 是记账，而且是精确的：它在每一步上成立，不是近似或长程平均。它的内容在于不需要固定的有限家族：关系项无限多时，§26 的定律无法陈述，这里仍可以陈述。比率由它直接得出。

*反驳 2：计数工具太多。* `mark_one`、`mark_zero`、`mark_add_not`、`total_congr_on`、`mem_insert`、`distinct_remove` 是一般的列表与标记工具，放在列表一节，供 `marks_le_of_sub` 与 `across` 使用；`balance_over_stretch` 是任何每步平衡的计数的累加，`Change.over_stretch` 的量的版本是它的一种情形，但没有改写成它的实例，以免改动已审查的模块。

*反驳 3：读于依存要求依存可判定。* 是，与读于活动要求活动可判定相同，属于表示的逻辑承诺。读于水平自动可判定。

**边界。** 无伦理谓词，不评价进入、离开、形成或消解；只对离散步与每步有限的列表陈述；名称（平衡、列出、有界普查）是 AI 的表述，由 Ren 定。本节尚未经独立审查：第十次独立审查的对象截至 P23c。

## 38. 第十次独立审查与更正（P25b）

2026-10-09。按同一指示继续。另一 agent（Claude Opus 5.5，未参与撰写）独立审查了 P24（§32）、P25（§33）与 P23c（§34）（[审查](BECOMING-P23C-P24-P25-REVIEW.md)）。它在仓库之外从前导重新编译核心闭包的 29 个模块，1732 条源声明的公理报告全空；闭包的 4894 个常量中依赖公理的只有 34 条编译器生成的 `injEq` 引理，都只依赖 `propext`，与回执所列相同；回执、源哈希、保留产物、引用哈希与证明绑定都对，数学全部接受，Lean 中没有数学错误。第九次审查的 M2–M10 关闭，M1 部分关闭。它提出十一项（O1–O11）：两项散文与记录中的错误（O4、O5），六项过强（O1、O3、O7、O8、O9、O10；其中 O7、O8 是 M1 的残留，O10 预设了 Ren 尚未作出的选择的范围），一项缺少反例（O2），两项表述与记账（O6、O11）。P26–P28（§35–§37）在审查期间提交，审查没有读；其中受影响的句子一并更正。本节记录逐项处理。探针 Q1–Q8、Q10 的内容移入核心，Q9 的内容由更正后的陈述写出；公理报告为空。§26、§30、§32–§37 与英文段落中受影响的句子已就地更正并标明。

```text
Result(s): 更正 continued-change-needs-openness（O1–O6）、map-of-premises（O9）、coming-and-ceasing-keep-pace（O7、O8）、
           space-and-its-parts（O8、O10、O11）、theory-of-becoming-foundation（O11(f)）、ceasing-needs-arising（O2）、
           evolution-on-descent（O11(d)）；没有新的成果记录
Delta: Dissipation：Enclosed.around_not_not。Roles：Web.Dependent.inactive_below。Space：grazing_decided、grazing_browser_ends、
       living_crosses_ceasing；law_decides、arising_iff_ceasing 与 grazing_world 的说明。Premises：acting_across（acting_of_enclosed
       由它证明）、draining、draining_decided、draining_but；Scatter 的构造子 giver 改为 source。Openness：Enclosed.aroundStanding_not_not；
       Flow.stills 只需围住不被否定；arising_stops（comes_to_rest 由它证明）；rests_enclosed 与 arising_opens 去掉 DecidableEq；
       Exposed.holder_one、holder_after、exposed_standing、openness_contingent；Kindling.sideOf、index、fuel_stands、census、unlisted，
       Ember.web、ember、rest_needs_standing。Change、Evolution 与根模块的说明（O7、O11）
Supplied premises / correspondence: 不变；删去一项（rests_enclosed 与 arising_opens 的可判定的相等）
Evidence: 合并检查器回执 20261009T145010.627958Z（1077 项定理／1739 项声明审计，核心闭包 29 个模块，包 27 个模块，
          源声明的公理报告全空）；外围桥接重跑 20261009T161851.010138Z（此前两次在负载下超时：20261009T145404.970266Z、20261009T151818.075474Z，每次 Lean 运行的时限现可由 LEAN_TIMEOUT 设定）；实例检查
Boundary: 不含伦理结论；不替 Ren 选择任何读法，新增两项 Ren 的选择；新名称是建议；新见证都是最小见证
Integration: §26、§30、§32–§37 的更正；审查 §4 的第 1–6 项完成，第 7 项（Ren 的选择）保持开放
```

### 38.1 逐项处理

| 项 | 审查所见 | 处理 |
|---|---|---|
| O1 | “起作用的是被围住，不是有限”漏掉定理所用的每步立着的有限多（活动的普查连同每个关系项体现）；kindling 有活动的普查、每步被围住、生起者体现、平衡、耗散，生起不息（Q1）；ember 每步被围住、每个关系项体现、平衡、耗散，没有普查，生起不息（Q2） | 章节第 4 条、§2、§8 现状行、§9 Openness 行、根基第 5 行、模块说明、记录的标题与对应、§33 与英文 P25 改为：世界不必有限；起作用的是每步立着的有限多，连同被围住。Q1 与 Q2 移入核心：`World.rest_needs_standing`（kindling：活动的普查、生起者体现、平衡、耗散、每步被围住于每个曾活跃的关系项，生起复现，没有所立者的普查；ember：同一流而每个关系项体现，每步被围住，生起复现，没有普查），连同 `Kindling.census`、`unlisted`、`Ember.web`、`World.ember` |
| O2 | 开放项“只要求生起者体现时被围住的世界是否归于静止”已有答案 | 开放项换为答案：只有活动的普查时不（kindling）；有所立者的普查时生起停止（Q3 移入核心为 `World.arising_stops`，`comes_to_rest` 改由它证明），止息不一定（dusk，`rest_needs_census`）；再有活动的普查时两者都停止，即审查未形式化的手证，已是 P26 的 `comes_to_rest`。章节进一步的证明中的“没有所立者的普查时被围住的步”换为“满足全部八个前提且每个都起约束的世界”。§35 的“本节的回答是肯定的”与英文 P26 一并更正：要再有所立者的普查 |
| O3 | 可判定的相等不是构造性证明的要求（Q4） | `rests_enclosed` 与 `arising_opens` 去掉 `[DecidableEq w.Relatum]`。新增 `Flow.Enclosed.around_not_not`（Dissipation：不判定相等时，被封闭的步不是不围住每个有限家族）与 `Flow.Enclosed.aroundStanding_not_not`；`Flow.stills` 的围住前提改为不被否定（`¬¬`），因为它比较的是自然数，判定已在那里（`Decidable.of_not_not`）；`arising_stops` 以 `not_not_intro` 传入直接的围住。`Enclosed.aroundStanding`（正面的陈述）保留，仍用可判定的相等。记录与 §33 反驳 3 更正 |
| O4 | 由 exposed 推出“开放不由八个前提推出”，需要另一个见证 | Q6 移入核心：`World.openness_contingent`：exposed 满足八个、没有一步被围住、生起复现；互利者满足八个、每步被围住、生起不复现。章节第 4 条、§2、§8 改为：八个前提既不决定被围住，也不决定开放 |
| O5 | 记录说 exposed 的总水平随世界上升；实际每步都是一 | Q5 移入核心：`World.exposed_standing`（所立者被列出，只有持有者；总水平每步为一；持有者每步下降；世界不有限），连同 `Exposed.holder_one`、`holder_after`。记录改为：总水平始终为一，无界的是与之交换的关系项的数目，各自水平为零 |
| O6 | exposed 中活动需要支持、有界传递与耗散空成立，只披露了耗散；它的开放是零净量的交换 | 模块说明、记录的反例与 §33 写明三项空成立、静止定理只用四个前提；“开放”指在每个有限家族之外的交换还是流入，列为 Ren 的选择 |
| O7 | 网层面“形成有限多时生成不息恰当止息不息”仍在 `Change`、根模块、README、章节 §2 与 §9、记录、§26 与根基第 5 行 | 改为“形成有限多且活动可判定时，生起复现恰当止息复现”；根基第 5 行写“生起不息”。`Web.Unceasing` 的名称与 `Becoming.Generation` 中的定义说明保持原范围 |
| O8 | 活动读法在正典中有三种地位：被排除、作为 Ren 的候选、被记为 Ren 定下的关系读法 | 正典中只留一种地位：由 Ren 选择的候选。章节第 4 条、§2、§8 现状行、词汇表与记录照录 Ren 的原话（“generative和degenerate虽然都在一个becoming model上，但是他们不overlap吧”），并标明 AI 的推论：若取不重叠，在有限世界中重合的活动读法就不是其所指。计划 §6 分开 Ren 的原话与 AI 的“作为关系”及 `renewing_not_consuming`。§26、§35–§37 与英文 P19、P22 就地更正 |
| O9 | (a) “有限世界有普查”漏掉可判定（Q9）；(b) `acting_of_enclosed` 写作逐步，定理要求每步被围住；(c) 见证的空成立没有写出；(d) `premised_rests` 只用到三个前提；(e) 地图不含有限、被围住与可判定性 | (a) 研究 §32、记录与章节 §9 加入可判定；不给可判定性而对每个有限世界要求普查就蕴含排中律，与 `law_decides` 同一结构，所以 Q9 不另移入核心。(b) 新增 `World.acting_across`（逐步的形式），`acting_of_enclosed` 由它证明。(c) Q10 移入核心：`World.draining`、`draining_but`：平衡的第二个见证，每步从两侧的封闭家族取用，取用与耗散在其中起约束；记录与 §32 写明各见证中空成立的前提。(d) 写为“证明用到其中三个：平衡、耗散与体现”。(e) 独立性写明相对于这八个 |
| O10 | grazing 的“不论终结之步怎样判定”预设了 Ren 的选择只涉及被汲取者自身的终结；活动需要支持时，对不变依存的侵蚀都与依存者的终结同时（Q8；P29b 注：这句本身过强，依存者原本活跃时才是终结，见 §42 R1）；“活跨越止息”在核心中没有可判定性实例（Q7） | Q8 移入核心：`Web.Dependent.inactive_below`（Roles，一般形式）与 `World.grazing_browser_ends`。`grazing_world` 的说明改为“在对终结之步汲取承担自身者的选择之外”。章节 §8 新增 Ren 的选择：与依存者的终结同时的侵蚀是否计入不活、对哪些汲取者（P29b 改为：依存者在该步之后不活跃的侵蚀，包括休眠的依存，见 §42 R1）。Q7 移入核心：`grazing_decided` 与 `World.living_crosses_ceasing` |
| O11 | (a) `law_decides` 只证明一个方向；(b) `arising_opens` 的说明比定理强；(c) 五处缺可判定；(d) `selected_le` 的说明；(e) §2 的消耗句缺“被取用”；(f) 七、八、十个前提的关系；(g) “最后一个 giver 已去掉”不准确；(h) 记录历史的空格；(i) 时间戳 | (a) 写为“蕴含排中律”；逆命题需要从排中律得到可判定的数据，在纯净核心中不能陈述（P29b 更正：此说不对，逆命题可以陈述，以排中律为假设不用可判定性也能证明，`World.law_of_em`、`World.law_iff_em`；见 §42 R2），经典地每个活动都可判定。(b) 写为“并非从某步起每步都被围住”。(c) 补上。(d) 改为加权总量，不是真正的选择项。(e) 补“对各步家族被耗散且被取用的事件”。(f) 章节第 3 条与 §2 写明：八个是七个去掉储备承载（由活动需要支持推出），加上普查与有界传递；连同两个较弱的形式共十个。(g) `Scatter.Relatum.giver` 改为 `source`。(h) 改正。(i) 无法从仓库核实，不改 |

### 38.2 新的已检查声明

| 模块 | 声明 | 内容 |
|---|---|---|
| Dissipation | `Flow.Enclosed.around_not_not` | 不判定相等时，被封闭的步不是不围住每个有限家族：每个成员是否在封闭家族中只需不被否定 |
| Roles | `Web.Dependent.inactive_below` | 活动需要支持时，跨一步落到所需之下、且在步后以不低的所需持续的依存，属于在步后不活跃的形成：对持续不变的依存的侵蚀使依存者在步后不活跃（P29b 更正，原文“与依存者的终结同时”；依存者原本活跃时才是终结，见 §42 R1） |
| Space | `grazing_decided`、`grazing_browser_ends`、`living_crosses_ceasing` | grazing 的活动可判定；食草者在第 1 步不活跃；在有限世界中，止息复现与否，都既可以每个事件都活，也可以有事件不活 |
| Premises | `acting_across`、`draining`、`draining_decided`、`draining_but` | 只有活跃者取用且耗散时，在被围住的步上只有活跃者给予；平衡的第二个见证：leaking 的流放在 spending 的网上，满足平衡之外的每个前提，两侧的家族每步封闭且被取用 |
| Openness | `Enclosed.aroundStanding_not_not`、`stills`（更正）、`arising_stops`、`rests_enclosed`、`arising_opens`（更正） | 被封闭的步不是不围住所立者；围住只需不被否定；所立者的普查、生起者体现、平衡、耗散与从某步起每步围住所立者使生起停止；两个世界定理不再要求可判定的相等 |
| Openness | `Exposed.holder_one`、`holder_after`、`exposed_standing`、`openness_contingent` | exposed 中所立者被列出，总水平每步为一，持有者每步下降，世界不有限；八个前提既不决定被围住，也不决定开放 |
| Openness | `Kindling.sideOf`、`index`、`fuel_stands`、`census`、`unlisted`，`Ember.web`、`World.ember`、`rest_needs_standing` | kindling 中活跃的是持有者，所以有活动的普查；没有列表包含每个燃料，所以没有所立者的普查；ember 的每个关系项在立着时活跃，所以没有普查；两者都每步被围住、平衡、耗散而生起复现 |

### 38.3 审查列出的会改变判断的结果

1. 静止定理的标题（O1）：每处写出每步立着的有限多。完成；判断 7 成为“限定后，是”。
2. 开放项（O2）：换为答案，两份 next_delta 更新。完成。
3. 可判定的相等（O3）：去掉。完成；判断 10 没有余下的限定。
4. 两句错误（O4、O5）：更正，开放不由八个前提推出引互利者。完成。
5. M1（O7、O8）：网层面的用语改为生起复现；活动读法在正典中只有一种地位，Ren 的原话照录；计划 §6 分开 Ren 的原话与 AI 的“作为关系”。完成。
6. 其余限定与表述（O9–O11）：完成，(i) 除外。
7. Ren 的选择保持开放，新增两项：与依存者的终结同时的侵蚀是否计入不活（O10）；“开放”指在每个有限家族之外的交换还是流入（O6）。
8. 审查没有构造而仍开放的：满足全部八个前提且每个都起约束的世界（O9(c)），列入进一步的证明。

### 38.4 作者反审

*反驳 1：“每步立着的有限多”是不是又把有限加回来了？* 加回来的是每一步的有限，不是世界的有限。kindling 与 ember 说明它不能去掉：每步都被围住、平衡、耗散，只要每步立着的有无穷多，生起就可以不息。§33 的推广是真的：有限世界在两点上起作用，给出普查，也给出被围住；P25 表明这两点可以分开要求，而世界本身不必有限。

*反驳 2：`stills` 的前提改为 `¬¬` 使陈述更难读。* 陈述更强：前提更弱，结论不变。说明写出为什么足够：比较的是自然数，判定已在那里。直接的围住经 `not_not_intro` 传入，`arising_stops` 与 `comes_to_rest` 的陈述不变。这使 `rests_enclosed` 不必要求可判定的相等，而可判定性是公开的逻辑承诺，不需要的不该列入。

*反驳 3：活动读法只作为候选，是不是回避了 Ren 的话？* 不是。Ren 的原话照录，AI 的推论标明：若取不重叠，这一读法就不是其所指。推论合理，但它是 AI 的，并决定 §8 的第一项选择；按方法，选择留给 Ren。审查也说明：若 Ren 声明活动读法不是其所指，O8 就只剩照录那句话。

*反驳 4：`law_decides` 为什么不证明逆命题？* 逆命题从排中律推出每个有限世界中的规律，需要把 `Q ∨ ¬Q` 变为可判定的数据，即 `Decidable`；从命题的析取消去到数据，在纯净核心中需要选择公理。所以说明写为“蕴含排中律”，经典地每个活动都可判定，这时规律由 `arising_iff_ceasing` 给出。（P29b 更正：这一回答不对。逆命题是命题，证明可以留在 `Prop` 中：按有限的关系项列表归纳，对排中律分情形，不需要 `Decidable` 数据，也不需要选择公理；见 §42 R2 与 `World.law_iff_em`。）

**边界。** 不含伦理谓词；不改变任何读法选择的地位，新增两项 Ren 的选择；新名称（ember、draining、source）是建议；新见证都是最小见证。本节的更正与 §35–§37 尚未经独立审查（计划 P28b）。

## 39. 每个前提都起约束的世界与名称的确认（P29）

2026-10-09。按 Ren“aim a complete theory of becoming, and finish related work”继续，作为计划 P29。第十次独立审查指出，前提的地图中有几个见证没有流，关于流的四个前提在其中空成立；满足全部八个前提的互利者也是如此（§38 O9）。章节的“进一步的证明”因此列出“满足全部八个前提且每个都起约束的世界”。本节给出它，并记录 Ren 对名称的确认。没有新模块：定义与世界放在 `Becoming.Premises`，它的静止放在 `Becoming.Openness`。成果记录：修订 [map-of-premises](../../../../theories/becoming/results/records/map-of-premises.md)、[continued-change-needs-openness](../../../../theories/becoming/results/records/continued-change-needs-openness.md)，名称写入 [space-and-its-parts](../../../../theories/becoming/results/records/space-and-its-parts.md)、[coming-and-ceasing-keep-pace](../../../../theories/becoming/results/records/coming-and-ceasing-keep-pace.md)、[ceasing-needs-arising](../../../../theories/becoming/results/records/ceasing-needs-arising.md)、[bounded-census-keeps-pace](../../../../theories/becoming/results/records/bounded-census-keeps-pace.md) 与 [census-balance](../../../../theories/becoming/results/records/census-balance.md)。

```text
Result(s): 复用 map-of-premises（八个前提、Premised）、continued-change-needs-openness（rests_enclosed）、
           space-and-its-parts（World 与各前提）、more-needs-renewers 与 no-finite-part-bears-taking（total 的工具）、
           evolution-on-descent（DescendsAt、TransmitsWithin）；修订 map-of-premises、continued-change-needs-openness
Delta: Premises：World.Binds；Brood（Relatum、level、fed、toChild、flow、eats、web、taking_part、kin、kin_distinct、
       closed、alive、index、outside）；World.brood、brood_balanced、brood_dissipative、brood_counted、brood_binds；
       Openness：World.brood_rests；Space 与根模块的文档写入 Ren 对名称的确认
Supplied premises / correspondence: 无新前提；brood 是一个具体世界，起约束只说某个条件被满足
Evidence: 合并检查器回执 20261009T163512.365801Z（1086 项定理、1760 项声明审计、核心闭包 29 个模块、包 27 个模块，全部源声明公理报告为空）；
          外围桥接重跑 20261009T163805.366023Z；实例检查
Boundary: 起约束不是在该世界中独立；brood 不有限，去掉地关系项得到有限世界，其中普查来自有限；不评价任何部分
Integration: 计划 P29；回答 map-of-premises 与 continued-change-needs-openness 的下一步“满足全部八个且每个都起约束的世界”；
             Ren 对名称的确认见[原话](../../../../sources/15-codex-theory-conversations/2026-10-09-arising-ceasing-names.md)
```

| 声明 | 内容 |
|---|---|
| `World.Binds` | 前提起约束：活动需要支持在活跃者以正需要依存于某条件时，平衡在水平变化时，只有活跃者给予与只有活跃者取用在参与者给予与取用时，耗散在参与者从封闭的家族取用时，体现在关系项生起时，普查在世界不有限、因而普查不来自有限时（P29b 更正：这只说整个世界不有限；`hatch` 中世界只因闲置的地关系项而不有限，普查来自只有三个关系项曾经活跃，见 §42 R3），有界传递在后代于其开始而立之步依存于某条件时 |
| `World.brood` | 食物在第一步立于三，此后立于一；亲代在第一步立于一，此后为零；子代在第一步为零，此后立于一；无限多个地关系项立于零。跨过第一步，亲代取用两个单位的食物与自身的一个单位，给子代一个单位；亲代与子代以需要一依存于食物 |
| `World.brood_binds` | 八个前提都成立，每个都起约束：亲代依存于食物，食物下降，亲代给予与取用，从食物、亲代与子代这一封闭家族取用，子代生起，世界不有限，子代在开始而立之步像亲代一样依存于食物 |
| `World.brood_rests` | 跨过第一步子代生起、亲代止息；每步都被围住在食物、亲代与子代之内；由 `rests_enclosed`，生起与止息都不再复现 |

**解读。**

- **前提不只是相容的。** 互利者表明八个前提可以同时成立，但其中关于流的四个空成立。`brood` 表明它们可以同时起约束：有交换、有依存、有世系与传递、有生起与止息，平衡与耗散都在约束实际的交换。它是一个最小的生命循环的形状：一个形成从所依存的条件取用、把自身的一部分交给后代、终结，后代像它一样依存于同一条件。这是 AI 的读法；名称（brood、亲代、子代、食物）是 AI 的表述，由 Ren 定。
- **普查起作用。** `brood` 有无限多个关系项，只有有限多个立着，所以普查与所立者的普查都不来自有限；静止定理在其中起作用，而 `premised_rests` 不适用。这正是 §38 O1 的要点：使世界归于静止的是每步立着的有限多与被围住，不是世界有限。（P29b 更正：“普查不来自有限”只对整个世界是否有限成立。地关系项闲置，只有食物、亲代与子代曾经活跃（`hatch_ever`、`hatch_idle`），由曾经活跃者的列表即得普查（`counted_of_ever`）；在静止定理适用的每个世界中，曾经活跃或立着的关系项都不是无界多（`rest_few`），所以静止定理比 `rests` 多涵盖的只是从不立着、从不活跃的关系项。见 §42 R3；`brood` 已改名 `hatch`，R10。）
- **起约束与独立不同。** 在 `brood` 中每步都被围住，所以只有活跃者给予由只有活跃者取用与耗散推出（`acting_across`）；它仍然起约束，因为确有参与者给予。起约束只说前提的条件被满足，不说它在该世界中不由其余推出。
- **名称。** Ren 引用 AI 关于 M1 的进度说明，并说“arising/ceasing is indeed better name”（[原话](../../../../sources/15-codex-theory-conversations/2026-10-09-arising-ceasing-names.md)）。所以 P23c 的改名保留，活动的读法以生起与止息命名，这是 Ren 确认的名称，不再列为 AI 拟定的用语（P29b 更正：Ren 确认的是英文的 arising/ceasing；中文 生起／止息 是 AI 的译名，仍是 AI 的用语；见 §42 R9）。Ren 提议中的“生成的”“退化的”指什么，仍由 Ren 说明；这句话没有说它，AI 也没有把关系的读法定为其所指。

**作者反审。**

*反驳 1：`brood` 是特意构造的。* 是；它是存在性的见证，与地图中的反例世界地位相同。它说明八个前提一起不只空成立，不说实际的生命满足它们。

*反驳 2：普查起约束定义为世界不有限，太强。* 在有限且活动可判定的世界中普查由有限推出（`Finite.counted`），所以普查的内容只有在世界不有限时才不由别的给出。去掉地关系项得到有限的世界，其余七个仍起约束，普查来自有限；这一变体没有另行检查。（P29b 更正：在静止定理的前提之下，普查的内容由只有有限多个关系项曾经活跃给出（`counted_of_ever`、`rest_few`），不由世界不有限给出；见 §42 R3。）

*反驳 3：亲代取用自身的一个单位不自然。* 它让亲代终结，使同一世界中有生起也有止息；没有它，`brood` 仍满足并约束八个前提，只是没有止息。耗散的约束来自亲代从食物取用的两个单位多于给予的一个单位。

**边界。** 无伦理谓词，不评价亲代的终结或子代的生起；只对离散步与自然数的量陈述；起约束是条件被满足，不是独立；名称由 Ren 定，生起与止息已由 Ren 确认。本节尚未经独立审查。

## 40. 复现定律由平衡推出与增长的界（P30）

2026-10-10。按 Ren“aim a complete theory of becoming, and finish related work”继续，作为计划 P30。§37 留下两项：P26 与 P27 的复现定律直接用列表的长短证明，与普查的平衡是两条路线；界随步增长时还剩什么（bounded-census-keeps-pace 的下一步：例如对数增长时，是否仍可能只生不灭）。census-balance 的下一步另有平衡读于依存。本节给出三者。没有新模块：累加的引理放在 `Becoming.Change`，定律放在 `Becoming.Population`，世界放在 `Becoming.Openness`。成果记录：修订 [census-balance](../../../../theories/becoming/results/records/census-balance.md)、[ceasing-needs-arising](../../../../theories/becoming/results/records/ceasing-needs-arising.md)、[bounded-census-keeps-pace](../../../../theories/becoming/results/records/bounded-census-keeps-pace.md) 与 [coming-and-ceasing-keep-pace](../../../../theories/becoming/results/records/coming-and-ceasing-keep-pace.md)。

```text
Result(s): 复用 census-balance（Listed.over_stretch）、coming-and-ceasing-keep-pace（Recurs.accumulates、steps 的工具、
           pos_of_exceeds）、ceasing-needs-arising 与 bounded-census-keeps-pace（Listed、CountedWithin、Dawn、Procession）、
           more-needs-renewers（Cycle 的列表）、becoming-dependence-dynamics（Forms、Dissolves）；修订 census-balance、
           ceasing-needs-arising、bounded-census-keeps-pace、coming-and-ceasing-keep-pace
Delta: Change：recurring_accumulates（Recurs.accumulates 改由它证明）。Population：Listed.ceasing_iff_shortfall、
       coming_iff_excess、ceasing_of_returning、ceasing_of_outpacing；coming_of_ceasing 与 ceasing_of_coming 改由平衡证明，
       陈述不变；去掉不再被用到的 comes_or_held、comes_or_fewer、comes_within、ceases_or_kept、ceases_or_more、
       ceases_within；Web.decideForms、decideDissolves（实例）、Web.DependenceCensus.over_stretch。Openness：World.CountedBy
       （CountedWithin 是常数界的情形）、CountedBy.arising_iff_ceasing；Slow.web、length、census、grows_between，
       World.slow、slow_decided（实例）、slow_world
Supplied premises / correspondence: 不变；有界定律的界只需在任意晚的步回到某数以内；slow_world 要求界不减而无界
Evidence: 合并检查器回执 20261009T170233.740799Z（1091 项定理、1771 项声明审计、核心闭包 29 个模块、包 27 个模块，
          全部源声明公理报告为空）；外围桥接重跑 20261009T170422.519028Z；实例检查
Boundary: 计数，不是机制；slow 是存在性的见证；不评价生起或止息；名称由 Ren 定
Integration: 计划 P30；回答 census-balance 的下一步（两条路线合一、读于依存）与 bounded-census-keeps-pace 的下一步
             （界随步缓慢增长时还剩什么）；依赖方向：ceasing-needs-arising 与 bounded-census-keeps-pace 现依赖 census-balance
```

| 声明 | 内容 |
|---|---|
| `recurring_accumulates` | 在任意晚的步为正的量，从任一步起的累加超过每个数；有限家族的 `Recurs.accumulates` 是其情形 |
| `Listed.ceasing_iff_shortfall` | 不再成立复现，恰当从每一步起某个后来的列表短于起点的列表连同其间开始成立的 |
| `Listed.coming_iff_excess` | 开始成立复现，恰当从每一步起起点的列表长于某个后来的列表连同其间不再成立的 |
| `Listed.coming_of_ceasing`（新证明） | 普查定律：不再成立复现时，其间不再成立的累加而超过起点的列表，由平衡，开始成立补足差额 |
| `Listed.ceasing_of_returning` | 列表在任意晚的步回到某数 K 以内时，开始成立复现需要不再成立复现：其间开始成立的累加而超过 K |
| `Listed.ceasing_of_coming`（新证明） | 有界定律：从某步起至多 B 个是回到 B 以内的情形 |
| `Listed.ceasing_of_outpacing` | 比率形式：每步的列表不长于 B t，且从每一步起某段步上开始成立的多于该段终点的界时，不再成立复现 |
| `Web.DependenceCensus.over_stretch` | 读于依存：终点的依存连同其间消解的，恰是起点的依存连同其间形成的 |
| `World.CountedBy`、`CountedBy.arising_iff_ceasing` | 每步 t 至多 B t 个关系项活跃且被列出；B 在任意晚的步回到某数以内时，生起复现恰当止息复现；`CountedWithin` 是常数界的情形 |
| `World.slow`、`slow_world` | 第 t 步活跃的是 B t 以下的关系项，以循环的列表为普查；B 不减而无界时，B 增长的每一步上关系项 B t 生起，没有关系项止息 |

**解读。**

- **一条路线。** 平衡读于复现是精确的：止息复现，恰当从每一步起某个后来的列表短于起点的列表连同其间开始成立的；开始成立复现，恰当起点的列表长于某个后来的列表连同其间不再成立的。复现的量在一段步上累加而超过任何数。所以普查定律：止息复现时，其间不再成立的终将超过起点的列表，平衡只能由开始成立补足；有界定律：开始成立复现时，其间开始成立的终将超过界，列表回到界内时，平衡只能由不再成立补足。§26 的有限家族定律早已这样证明（`rising_recurs`、`falling_recurs` 用累加与平衡），现在普查的定律也如此：复现的定律都是累加与平衡。P26 与 P27 中由列表长短给出的六个引理不再被用到，从核心中去掉；它们的陈述与检查保存在回执 20261009T163512.365801Z 与此前的提交中，§35、§36 记录了那条证明。两个定律的名称与陈述不变，用到它们的读法（活动、依存、水平、世界）不变。
- **回到界内即可。** 有界定律不要求界从某步起一直成立：列表只需在任意晚的步回到某数 K 以内，其间可以任意地大。读于世界：每步 t 至多 B t 个活跃（`CountedBy`），B 在任意晚的步回到某数以内时，生起复现恰当止息复现。
- **增长的界。** 界无界地增长时，不论多慢，都不使两者同步：对任何不减而无界的 B（例如对数），`slow B` 中第 t 步活跃的是 B t 以下的关系项，B 增长的每一步上关系项 B t 生起，没有关系项止息。这回答了 bounded-census-keeps-pace 的下一步：对数增长时，仍可能只生不灭。对不减的界，停在某数以内与无界增长两者必居其一，这是经典的；纯净核心分别陈述两侧：前者在它计数的每个世界中使生起与止息同步，后者在 slow 中不同步。dawn 是 B t = t 的一个变体（关系项与条件的读法不同）。
- **比率。** 列表无界时，止息复现恰当缺额出现；所以从每一步起，某段步上开始成立的多于该段终点的界时，止息就复现。这是充分条件，不是必要条件：列表可以远小于界。在 slow 中，任一段步上生起的恰是界的增长，从不多于终点的界。
- **读于依存的平衡。** 每步的依存被列出时，终点的依存连同其间消解的，恰是起点的依存连同其间形成的。于是平衡与复现定律都读于活动、依存与水平。

**作者反审。**

*反驳 1：去掉六个引理是不是删除了成果？* 它们是证明的步骤，不是成果记录的结论：两个定律的名称与陈述不变，只是证明经过平衡。核心中同一定理的两条证明，只会让读者以为它们说的是两件事。被去掉的陈述与检查保存在回执与提交历史中，相关记录的历史写明了替换；`search` 与 `length_le_of_sub` 仍被别处用到，保留。

*反驳 2：`ceasing_of_outpacing` 由 `ceasing_iff_shortfall` 直接得出，是否值得单列？* 它回答了界增长时问题的正面：什么足以使止息复现。它也说明 slow 为什么不违反它：其中生起从不多于界。

*反驳 3：slow 是特意构造的，而且没有流。* 是：它是存在性的见证，与 dawn 地位相同。它说明只靠计数的界不能更进一步；关于流的前提在 slow 中空成立（流是静止的流），带流与被围住时，静止定理给出另一种约束（§35）。

*反驳 4：二分只对不减的界。* 是。一般的界在任意晚的步回到某数以内时定律成立；界不单调而最终超过每个数时，对应的世界要取其后各步的最小值作为不减的界，这需要从存在得到数据，在纯净核心中不能构造，所以没有陈述。

*反驳 5：依赖方向改变了。* census-balance 原先依赖 ceasing-needs-arising（复用列出与普查的定义）；现在普查定律由平衡推出，两者互相依赖会成环。列出与普查的定义也声明在 census-balance 中，所以它不再依赖 ceasing-needs-arising，后者与 bounded-census-keeps-pace 依赖它。这是推理顺序的如实记录，不是改写历史：census-balance 的历史写明了反转。

**边界。** 无伦理谓词，不评价生起或止息；只对离散步与每步有限的列表陈述；可判定是逻辑承诺；名称（缺额、回到界内、slow）是 AI 的表述，由 Ren 定。本节尚未经独立审查：第十一次独立审查的对象截至 P29。

## 41. 沿依存之链的滞后共灭（P31）

2026-10-10。按 Ren“aim a complete theory of becoming, and finish related work”继续，作为计划 P31。reserve-defers-ending 与 life-as-condition-of-life 的下一步都列出沿依存链、有储备的滞后共灭；P17 只陈述了单环（`Carries.coextinct_lasts`，§24），第八次独立审查也把它列为开放。在 `Dependent` 之下，共灭沿依存链在同一步发生（`coextinct`）；有储备时，链上的每一环都推迟。单环定理的结论是形成只在有限多步活跃，它不给出下一环从哪一步起不被支持，所以不能逐环接下去。储备衰减时终结之步是显式的（`Carries.ends_within`），本节由此给出逐环的界；储备不衰减时，以排中律为假设，逐环仍可接下去，只是没有界。没有新模块：定理与见证放在 `Becoming.Reserve`，排中律之下的反例引理放在 `Becoming.Change`。成果记录：修订 [reserve-defers-ending](../../../../theories/becoming/results/records/reserve-defers-ending.md)。

```text
Result(s): 复用 reserve-defers-ending（Carries、Decays、Carries.ends_within、unsupported_after_end）、
           life-as-condition-of-life（Embodied、coextinct）、becoming-dependence-dynamics（Supported、Dependent）；
           修订 reserve-defers-ending
Delta: Change：exists_not_of_em；Reserve：Web.chainEnd、chainEnd_ge、chainEnd_zero、Carries.chain_ends、
       Carries.chain_ends_of_em；Cascade.upto、upto_pos、upto_le_one、
       upto_after、upto_self、web、embodied、supported_of_le、unsupported_late、reserve、falls、never_rises、carries、
       decays、ends、cascade
Supplied premises / correspondence: Carries 与 Decays（表示前提，同 ends_within）；链上的关系项都体现；从第 T 步起
       每一环以正需要依存于前一环；第一环从 T 起不活跃；无界的形式以排中律为假设代替 Decays
Evidence: 合并检查器回执 20261009T184816.006618Z（1109 项定理、1793 项声明审计、核心闭包 29 个模块、包 27 个模块，全部源声明公理报告
          为空）；外围桥接重跑 20261009T184936.948468Z；实例检查
Boundary: 界只对衰减的储备陈述，不衰减时以排中律为假设只得终结、没有界；不评价共灭；名称由 Ren 定
Integration: 计划 P31；回答 reserve-defers-ending 与 life-as-condition-of-life 的下一步（沿依存链、有储备的滞后共灭）
```

| 声明 | 内容 |
|---|---|
| `Web.chainEnd` | 链上各环的终结之步：第 0 环在 T；第 k+1 环在第 k 环终结之后，再过它在那时的储备那么多步 |
| `chainEnd_ge` | 每一环的终结之步不早于 T |
| `chainEnd_zero` | 零储备之下每一环都在 T 终结 |
| `Carries.chain_ends` | 储备承载且衰减，链上的关系项都体现，从 T 起每一环以正需要依存于前一环，第一环从 T 起不活跃时，第 k 环从 `chainEnd k` 起不活跃 |
| `Carries.chain_ends_of_em` | 不设 `Decays`，以排中律为假设：其余前提相同时，链上每个关系项从某步起不活跃，没有界 |
| `exists_not_of_em` | 以排中律为假设，否定的全称有反例：不在任意晚的步出现者有一步之后不再出现 |
| `Cascade.cascade` | 关系项 x 活跃至第 x 步，x+1 以需要一依存于 x，储备至第 x 步为一：前提全部成立，`Dependent` 不成立，`chainEnd k` 为 k+1，而第 k 个关系项在第 k 步仍活跃，界恰好达到 |

**解读。**

- **逐环的界。** 第 k 环从 `chainEnd k` 起不活跃；第 k+1 环以正需要依存于它，它体现，所以从那时起第 k+1 环不被支持（`unsupported_after_end`）；衰减的储备在其储备那么多步之后终结它（`ends_within`）。每一环的储备读于前一环终结之时，所以支持期间的补充已计入界中：reserve-defers-ending 原来的下一步担心“支持期间储备可以补充，链上的界须另设前提”，衰减之外不需要另设前提，界读于那时的储备即可。
- **零储备是同时的共灭。** 零储备恰是 `Dependent`（`carries_zero`），并空满足 `Decays`；`chainEnd` 恒为 T（`chainEnd_zero`），所以 `chain_ends` 在零储备之下是沿链从 T 起的同时共灭，即 `coextinct` 在一条序列链上、跨步的情形。
- **界可以达到。** 在 `Cascade` 中，每个关系项恰好比它依存的前一个多活一步：第 0 个从第 1 步起不活跃，第 k 个在第 k 步仍活跃，`chainEnd k` 为 k+1。没有储备时，链会同时终结：关系项 1 在第 1 步活跃而不被支持，`Dependent` 不成立。它的储备是给定的量，不是所持条件的水平，与 `Seed`、`Viable` 相同。
- **为什么要衰减，以及不衰减时。** 不设 `Decays` 时，休眠的形成可以任意晚地醒来（`Seed` 的储备在休眠中保持），一环的终结之步没有界。从某步起不被支持的形成只在有限多步活跃（`active_finitely`），但在构造的逻辑中“不复现”不能化为终结之步（这需要马尔可夫原则）（P33b 更正：这一步不是构造性的，即使活动可判定且至多发生一次，它也蕴含 LPO（`Web.lpo_of_ending`），马尔可夫原则不够；见 §45 T3），而下一环的“从某步起不被支持”需要前一环的终结之步。以排中律为假设（像 `Space` 中的 `law_of_em` 那样作为假设，不作为公理），“不复现”有一步之后不再出现（`exists_not_of_em`），逐环就可以接下去：链上每个关系项从某步起不活跃（`Carries.chain_ends_of_em`）。这一形式只说终结，不给界；核心仍从 prelude 编译，公理报告为空。

**作者反审。**

*反驳 1：这只是 `ends_within` 的迭代。* 是。新内容在于迭代可行、界逐环可读：`coextinct_lasts` 的结论（不复现）不能作为下一环的前提，`ends_within` 的显式终结之步恰好接上下一环需要的“从某步起不被支持”。

*反驳 2：所有环从同一步 T 起依存，是否太强？* 每一环的依存只需在前一环终结时已成立；取共同的 T 使陈述简单，`chainEnd_ge` 保证每一环的终结不早于 T。依存在链的中途改变（例如换宿主）时链断开，这时适用的是替代与转化，不是共灭。

*反驳 3：链是序列，不是图。* 一个关系项依存于几个条件时，任一个所需不被满足都使它不被支持；所以沿到达它的任一条链，界都成立：图上的每个关系项在到达它的某条链的 `chainEnd` 之后终结（P33b 更正：P31 的定理要求不止的链，在有限的链上空成立；现在 `chain_ends` 对 n 环的有限链陈述，沿到达它的每条有限链的界由它给出；见 §45 T2）。取所有链的最小值的形式没有陈述。

*反驳 4：`Cascade` 是特意构造的。* 是：它是界可以达到的最小见证，与 `Seed`、`Viable`、`Famine` 地位相同。种群、种子库与储蓄中的级联是应用的例子，不是定理的内容。

*反驳 5：以排中律为假设是否把经典逻辑带进了核心？* 没有。`chain_ends_of_em` 是一个条件陈述：排中律是它的一个前提，核心的公理报告仍为空，从 prelude 编译。它表明，构造地不能逐环接下去的只是把“不复现”化为终结之步这一步；接受排中律的读者由此得到无界的形式，不接受的读者仍有衰减时的有界形式。

**边界。** 无伦理谓词，不评价共灭；界只对离散步与衰减的储备陈述，不衰减的形式以排中律为假设、没有界；链上的依存与体现是表示前提；名称（chainEnd、Cascade）是 AI 的表述，由 Ren 定。本节尚未经独立审查。

## 42. 第十一次独立审查与更正（P29b）

2026-10-10。按 Ren“aim a complete theory of becoming, and finish related work”继续。另一 agent（Claude Opus 5.5，未参与撰写）独立审查了 P26（§35）、P27（§36）、P28（§37）、P25b（§38）与 P29（§39）（[审查](BECOMING-P25B-P29-REVIEW.md)，对象 `0cf14b8b`）。它在仓库之外从前导重新编译核心闭包的 29 个模块，1830 条源声明（1126 项定理）的公理报告全空；闭包的 5153 个常量中依赖公理的只有 35 条编译器生成的 `injEq` 引理，都只依赖 `propext`，与回执所列相同；回执、源哈希、保留产物、外围回执、引用哈希与证明绑定都对；各阶段的定理数与研究、计划和章节一致。数学全部接受，没有错误的 Lean 陈述。它写了 47 条探针声明（32 项定理，生成的 159 个常量都不依赖公理），提出十一项（R1–R11）：两项散文中的错误（R1、R2），六项过强（R3–R8，其中 R6 缺少反例），三项表述与出处（R9–R11）。第十次审查的 O2–O6、O9 关闭；O1、O7、O8、O10、O11 的残留就是 R4、R5、R9、R1、R2。P30（§40）与 P31（§41）在审查期间或之后提交，审查没有读；R6 与 R11(a) 已由 P30 回答。本节记录逐项处理。探针 S1、S2、S4–S6 的内容移入核心（S3 的内容已由 P30 给出），名称按核心改写；公理报告为空。§26、§34、§36、§38、§39 与英文段落中受影响的句子已就地更正并标明。

```text
Result(s): 更正 space-and-its-parts（R1、R2、R9）、map-of-premises（R3、R10）、continued-change-needs-openness（R3、R4、R8、R10）、
           bounded-census-keeps-pace（R5、R7、R9）、ceasing-needs-arising、census-balance、coming-and-ceasing-keep-pace（R9）；
           没有新的成果记录
Delta: Change：stays_failing、persists_of_em（exists_not_of_em 已在 P31 加入）。Roles：Web.Dependent.ceases_below；inactive_below 的说明。
       Space：quiet_of_once；World.Seedbank（Relatum、soil、level、flow、web、distinct）、World.seedbank、seedbank_world；World.law_of_em、
       World.law_iff_em；Ren 原话、名称与 grazing_browser_ends 的说明。Premises：listed_of_ever、World.counted_of_ever；World.Brood 改名
       World.Hatch，brood_* 改名 hatch_*；World.hatch_ever、hatch_idle；Binds 的说明。Openness：World.Finite.census_bounded（countedWithin
       由它证明）；gather、gather_self、mem_gather、comes_after、Listed.few_of_quiet、World.few_active、World.rest_few；Holding（level、
       flow、web、open_at、census）、World.holding、holding_world；brood_rests 改名 hatch_rests。Population：unceasing_iff_bounded 与模块
       说明的用语（R5）
Supplied premises / correspondence: 不变；law_of_em 以排中律为定理的假设，不是公理
Evidence: 合并检查器回执 20261009T185557.684339Z（1131 项定理／1826 项声明审计，核心闭包 29 个模块，包 27 个模块，源声明的公理报告全空）；
          外围桥接重跑 20261009T185801.898161Z；实例检查
Boundary: 不含伦理结论；不替 Ren 选择任何读法；§8 的一项选择按 R1 放宽，第一项选择按 R9 写出 Ren 回复时的语境；新名称（hatch、
          seedbank、holding）是建议；新见证都是最小见证
Integration: §26、§34、§36、§38、§39 与英文 P19、P25b、P29 的就地更正；审查 §4 的各项完成，Ren 的选择保持开放
```

### 42.1 逐项处理

| 项 | 审查所见 | 处理 |
|---|---|---|
| R1 | “活动需要支持时，对持续不变的依存的每次侵蚀都与依存者的终结同时”不成立：`inactive_below` 只给出依存者在该步之后不活跃；依存者此前就不活跃时没有终结。探针 sleeper：有限、平衡、每个关系项体现、活动需要支持，一次侵蚀使事件不活，而世界中从无止息。这句来自第十次审查的 O10 与 Q8 | 新增 `Web.Dependent.ceases_below`（Roles）：依存者原本活跃时，这样的侵蚀与它的终结同时。sleeper 移入核心为 `World.seedbank`（汲取者、种子、土壤）与 `seedbank_world`：活动需要支持、体现、平衡、有限，`UnderminingOn 0 drawer soil`，世界不 living，`inactive_below` 的前提成立，而种子从不活跃，世界中没有任何止息。Roles 与 Space 的模块说明、`inactive_below` 与 `grazing_browser_ends` 的说明、README、检查器、章节第 10 条与 §9、记录 space-and-its-parts 改写；§8 的 Ren 选择放宽为“依存者在该步之后不活跃的侵蚀”，包括休眠的依存。§34 反驳 3、§38.1 O10 与 §38.2 Roles 行就地标明。这句话的过强来自第十次审查本身 |
| R2 | §38 与英文 P25b 说 `law_decides` 的逆命题需要选择公理、在纯净核心中不能陈述；逆命题可以陈述，以排中律为假设、不用可判定性与选择即可证明（探针 `law_iff_em`） | 移入核心：`World.law_of_em`（以排中律为假设，有限世界中生起复现恰当止息复现，两个方向都证明，审查只给出一个方向）与 `World.law_iff_em`（对每个有限世界要求这一规律而不给可判定性，等价于排中律），连同 `quiet_of_once`（Space）与 `persists_of_em`、`stays_failing`（Change；否定的全称取反例的 `exists_not_of_em` 已在 P31 为沿链的共灭加入）。说明改为“等价于排中律”。§38.1 O11(a)、§38.4 反驳 4 与英文 P25b 就地更正；章节的逻辑承诺与开放项不再说这一规律只能在外围以经典逻辑陈述 |
| R3 | P29 中普查起约束的条件是世界不有限；`brood` 的地关系项闲置，普查来自只有三个关系项曾经活跃；在静止定理适用的每个世界中，曾经活跃或立着的都不是无界多 | 移入核心：`Listed.few_of_quiet`（列出之下开始成立不复现时，曾经成立的成员不是无界多），`World.few_active`，`World.rest_few`（静止定理的前提之下，曾经活跃的与曾经立着的关系项都不是无界多；围住只需不被否定），连同 `gather`、`mem_gather`、`comes_after`；`listed_of_ever` 与 `World.counted_of_ever`（曾经活跃者可列出时有普查）；`World.hatch_ever`（只有食物、亲代与子代曾经活跃）与 `hatch_idle`（地关系项从不立着、从不活跃、从不参与流、从不被依存或汲取）。`Binds` 的说明、Premises 与 Openness 的模块说明、章节第 3、4 条与 §2、根基第 5 行、记录与计划写明：世界不有限只因闲置的关系项；静止定理比 `rests` 多涵盖的只是从不立着、从不活跃的关系项。`hatch` 中活动需要支持起约束而不紧（食物从不低于所需），关于流的四个前提只在第 0 步起约束。§39 的“普查起作用”与反驳 2、英文 P29 就地更正。审查的手证（在静止定理的前提下，流只在有限多步参与）没有形式化，列为开放 |
| R4 | 记录 continued-change-needs-openness 的标题漏掉活动的普查，`dusk` 反驳它；“每步立着的有限多”混同两种普查 | 标题与对应写出每步立着的与活跃的有限多（两种普查），“立着的变化只有有限多次”；章节第 4 条、§2、§8 现状行与根基第 5 行同改。CLAIMS 由记录生成 |
| R5 | P27 重新引入“生成不息恰当止息复现”（O7 的残留） | `Population` 的模块说明与 `unceasing_iff_bounded` 的说明、记录 bounded-census-keeps-pace、§26 表、§36 表与英文 P19 改为“生起复现恰当止息复现”，就地标明 |
| R6 | 有界定律只需界在无限多步成立；任何不减且趋于无穷的计数都允许只生不灭 | 已由 P30 回答：`Listed.ceasing_of_returning` 与 `World.CountedBy.arising_iff_ceasing`（界在任意晚的步回到某数以内）对应探针 `ceasing_of_coming_often`、`arising_iff_ceasing_often`；`World.slow_world`（对每个不减而无界的界）对应 `paced_world`。章节 §2 写“须同时活跃者的计数趋于无穷”与“在任意晚的步至多 B 个” |
| R7 | `Finite.countedWithin` 的说明“每个普查”比陈述强 | 新增 `World.Finite.census_bounded`：有限世界的每个普查都以关系项的数目为界，不需要可判定性；`countedWithin` 由它证明，说明改为“活动可判定的有限世界有一个普查，它以关系项的数目为界”。记录的假设去掉“需要可判定的活动”这一普遍读法 |
| R8 | “满足八个前提而没有一步被围住的世界生起不息”读作一般时为假（探针 s6_holding） | 移入核心：`Holding` 与 `World.holding_world`：一侧以零净量与无界的地交换、保持其水平，满足八个前提，没有一步被围住，生起与止息都不复现，世界不有限。章节第 4 条、§2、§8 现状行、词汇表、根基第 5 行、记录与计划写为“一个这样的世界（exposed）……另一个（holding）……”：开放是生起不息的必要条件而不充分 |
| R9 | Ren 的“不overlap吧”有三种写法；Ren 确认的是英文的 arising/ceasing；Ren 回复时的语境没有写出 | Space 的模块说明与四份记录照录原话，或写为“以‘吧’预设二者不重叠”；中文各处写“Ren 确认英文名称 arising/ceasing（中文 生起／止息 是 AI 的译名）”；来源文件的标题改为 Ren 的原词，原标题在更正说明中保留；章节 §8 第一项写出 Ren 回复的 AI 说明中“despite Ren saying they shouldn’t overlap”一句，并请 Ren 说明活动的读法是否仍是候选。§39 与计划就地标明 |
| R10 | 核心中有两个不同的 brood | P29 的 `World.Brood`、`World.brood` 与 `brood_*` 改名 `World.Hatch`、`World.hatch`、`hatch_*`；`Roles` 中世代不息的 `Brood` 保持原名（它被章节、两份记录与 `Descent` 引用）。名称是建议，由 Ren 定 |
| R11 | (a) 依存的平衡没有实例；(b) 英文 P25b 没有计数行，计划 P25b、P29 行没有回执；(c) §2 的界；(d) census-balance 的下一步 | (a) 已由 P30 的 `Web.DependenceCensus.over_stretch` 回答。(b) 补上，标明 P29b 补记。(c) 见 R6。(d) 审查认为不需要处理 |

### 42.2 新的已检查声明

| 模块 | 声明 | 内容 |
|---|---|---|
| Change | `stays_failing`、`persists_of_em` | 不成立且在之后各步不开始成立者保持不成立，不需要可判定性；以排中律为假设，成立且在之后各步不再成立者保持成立 |
| Roles | `Web.Dependent.ceases_below` | 活动需要支持时，依存者原本活跃、其持续不变的依存跨一步落到所需之下，它就在该步止息 |
| Space | `quiet_of_once`、`World.Seedbank`、`World.seedbank`、`seedbank_world` | 以排中律为假设，列表中每个成员从某步起至多发生一次时，它们从某步起都不再发生；种子库：侵蚀而无终结 |
| Space | `World.law_of_em`、`World.law_iff_em` | 以排中律为假设，每个有限世界中生起复现恰当止息复现；对每个有限世界要求这一规律而不给可判定性，等价于排中律 |
| Premises | `listed_of_ever`、`World.counted_of_ever`、`World.Hatch`、`World.hatch_*`、`hatch_ever`、`hatch_idle` | 曾经成立者被一个有限表包含时，每步的成立者可列出；世界的普查由此得出；`hatch` 中只有三个关系项曾经活跃，地关系项闲置 |
| Openness | `World.Finite.census_bounded` | 有限世界的每个普查都以关系项的数目为界 |
| Openness | `gather`、`gather_self`、`mem_gather`、`comes_after`、`Listed.few_of_quiet`、`World.few_active`、`World.rest_few` | 列出之下开始成立不复现时曾经成立者不是无界多；静止定理适用的世界中曾经活跃与立着的关系项都不是无界多 |
| Openness | `Holding`、`World.holding`、`holding_world`、`hatch_rests` | 满足八个前提、没有一步被围住而什么也不生起的世界；`hatch` 在一次生起与一次止息之后归于静止 |

### 42.3 作者反审

*反驳 1：`seedbank` 是不是在制造一个不自然的反例？* 它是满足已公开定义的最小世界，与审查的 sleeper 相同：休眠的种子以不变的所需依存于土壤，汲取者取走土壤。它说明 R1 的那句话超出了定理，不说明种子库在现实中怎样。按方法，它只表明定义允许什么。被侵蚀的依存者休眠时，是否计入不活，现在明确列为 Ren 的选择的一部分。

*反驳 2：`law_iff_em` 把排中律放进纯净核心了吗？* 没有。排中律在 `law_of_em` 中是定理的一个假设，在 `law_iff_em` 中是等价的一边；核心的公理报告仍为空，从前导编译。它纠正的是一个关于核心能表达什么的错误说法：逆命题不需要 `Decidable` 数据，证明可以留在 `Prop` 中。审查只给出从生起到止息的方向；本节两个方向都证明，从止息到生起的方向用 `stays_failing` 与 `quiet_of_once`。

*反驳 3：`rest_few` 是否削弱了 P25 与 P26 的推广？* 它限定推广，不取消它。“世界不必有限，起作用的是每步立着的与活跃的有限多”在形式上仍成立，而且每步的前提比世界有限更容易核对。`rest_few` 说明这些世界在归于静止时与有限世界的差别只在从不立着、从不活跃的关系项。这一点属于推广本身，应当写在它旁边。

*反驳 4：为什么不删去 `Binds` 的普查一项，换成更强的条件？* 在归于静止的世界中，普查不能在更强的意义上起约束（`rest_few`）。保留 `Binds.counted` 并在说明中写清它只说世界不有限，比另造一个条件更诚实；`hatch_ever` 与 `counted_of_ever` 把普查的实际来源写成定理。

*反驳 5：改名 `hatch` 是否必要？* 两个 brood 用途相反：`Roles` 中的世代不息、不耗散，P29 的在一次生起后归于静止。章节在相隔几段处都称 `brood`。改动较少的一个被改名；名称由 Ren 定。

**边界。** 不含伦理谓词；不改变任何读法选择的地位，§8 的一项选择按 R1 放宽，第一项写出 Ren 回复的语境并请 Ren 说明；新名称是建议；新见证都是最小见证。本节的更正与 §40、§41 尚未经独立审查。

## 43. 延续下的普查平衡与跨一步的精确条件（P32）

2026-10-10。按 Ren“aim a complete theory of becoming, and finish related work”继续，作为计划 P32。identity-across-steps 的局限写着，没有分裂是更多迫使生起的充分条件，不是必要条件，精确的界限没有陈述；它的下一步与正典第 8 节的进一步证明都列出“延续关系上使更多迫使生起的充要条件”。另一方面，普查定律（§35–§37、§40）都以名字规定的同一读生起与止息，即每个形成只延续自身。本节回答前者，并把后者推到每个延续关系：普查定律在延续下的哪一半成立，恰由没有分裂或没有合并决定。没有新模块：一般的计数引理放在 `Becoming.Population`，延续下的读法与见证放在 `Becoming.Identity`。成果记录：修订 [identity-across-steps](../../../../theories/becoming/results/records/identity-across-steps.md)；新增 [census-balance-under-continuation](../../../../theories/becoming/results/records/census-balance-under-continuation.md)。

```text
Result(s): 复用 identity-across-steps（Continues、ArisesFrom、UnceasingFrom、NoSplit、arisesFrom_self、
           Census.decideContinues）、census-balance（mark_add_not、marks_le_of_sub、balance_over_stretch 的形式）、
           ceasing-needs-arising（Web.arising_of_ceasing）、bounded-census-keeps-pace（Web.ceasing_of_arising）、
           more-needs-renewers（Census、Distinct、length_le_of_matched、decideSome）；
           修订 identity-across-steps；新增 census-balance-under-continuation
Delta: Population：mark_le_total、total_le_mark、le_over_stretch、ge_over_stretch、gaining_of_losing、losing_of_gaining；
       Identity：forces_iff_noSplit、paired、paired_mem、paired_noSplit、paired_covers、forced_iff_more、
       Web.Continued、Web.CeasesFrom、Web.NoMerge、ceasesFrom_self、self_one_to_one、Census.balanceFrom、
       Census.balanceFrom_eq、Census.arisingFrom_of_ceasingFrom、Census.ceasingFrom_of_arisingFrom、
       Census.decideContinued；Tandem.web、alive、apart、census、kept、buds、budding、joins、joining
Supplied premises / correspondence: 延续关系是读法（同 identity-across-steps），定理对每个读法成立；普查；活动、延续与
       “是否延续某个活跃形成”可判定（定理的假设）；有界的一半另需从某步起至多 B 个活跃；跨一步的刻画对列表陈述，
       不需要依存网，forces_iff_noSplit 的必要方向用相等可判定
Evidence: 合并检查器回执 20261009T192237.890720Z（1153 项定理、1857 项声明审计、核心闭包 29 个模块、包 27 个模块，全部源声明公理报告
          为空）；外围桥接重跑 20261009T192558.793391Z；实例检查
Boundary: 只对离散步与每步有限的活动陈述；延续关系由读法给出，不说哪一个是同一；整段上没有分裂与没有合并只是充分
          条件，单步的刻画是精确的；平衡是计数，不是机制；不评价生起或止息；名称由 Ren 定
Integration: 计划 P32；回答 identity-across-steps 的下一步与第 8 节同名的进一步证明（延续关系上更多迫使生起的充要
             条件，跨一步）；把普查定律推到每个延续关系
```

| 声明 | 内容 |
|---|---|
| `forces_iff_noSplit` | 对一步的延续 S：对任意步前与步后的列表（步后的不重复），步后多于步前时总有步后的形成不延续步前的任何形成，恰当没有形成延续为两个 |
| `paired`、`paired_noSplit`、`paired_covers` | 两个列表按次序配对；步前的不重复时没有分裂；步后的不多于步前时，步后每个形成都延续某个步前的形成 |
| `forced_iff_more` | 步前与步后的列表都不重复时：在每个没有分裂的延续下都迫使生起，恰当步后多于步前 |
| `Web.Continued`、`Web.CeasesFrom`、`Web.NoMerge` | 在延续下被延续；在延续下止息：步前活跃，步后没有活跃的形成延续它；没有合并：步后活跃的形成不延续两个步前活跃的形成 |
| `ceasesFrom_self`、`self_one_to_one` | 每个形成只延续自身时，止息即止息，既无分裂也无合并 |
| `mark_le_total`、`total_le_mark` | 某成员有某性质的命题，其标记不超过有该性质的成员数；至多一个成员有它时，成员数不超过该命题的标记 |
| `Census.balanceFrom` | 普查之下每一步：没有分裂时，步后活跃的连同止息的至多是步前活跃的连同生起的；没有合并时至少如此 |
| `Census.balanceFrom_eq` | 两者都没有时恰好相等 |
| `le_over_stretch`、`ge_over_stretch` | 每步的不等式跨任一段步累加 |
| `gaining_of_losing`、`losing_of_gaining` | 每步终点连同失去的不超过起点连同得到的：失去复现需要得到复现；反向且计数从某步起有界时，得到复现需要失去复现 |
| `Census.arisingFrom_of_ceasingFrom` | 普查、没有分裂：止息在任意晚的步出现需要生起在任意晚的步出现 |
| `Census.ceasingFrom_of_arisingFrom` | 普查、没有合并、从某步起至多 B 个活跃：生起在任意晚的步出现需要止息在任意晚的步出现 |
| `Census.decideContinued` | 普查之下，延续可判定时，“是否被某个活跃形成延续”可判定 |
| `Tandem.kept` | 每步 t 与 t+1 两个形成活跃；每个形成只延续自身时，每步一个生起（t+2）、一个止息（t） |
| `Tandem.budding` | 读作萌出（t+1 延续为自身与 t+2，t 不被延续）：普查成立、没有合并、有分裂，每步 t 止息，从不生起 |
| `Tandem.joining` | 读作合并（t 与 t+1 都延续为 t+1）：至多两个活跃、没有分裂、有合并，每步 t+2 生起，从不止息 |

**解读。**

- **跨一步，精确的条件。** 一个形成 g 延续为两个不同的形成 f 与 f′ 时，步前只有 g、步后有 f 与 f′：步后更多，而每个都延续 g，没有生起；没有形成延续为两个时，步后每个形成都延续步前某个形成就使步后不多于步前（`length_le_of_matched`）。所以对任意步前与步后的形成，更多迫使生起恰当没有分裂（`forces_iff_noSplit`）。数目的一面也精确：在每个没有分裂的延续下都迫使生起，恰当步后多于步前，因为步后不多时，按次序配对（`paired`）就是一个没有分裂、使步后每个形成都延续某个形成的延续（`forced_iff_more`）。在一步上，没有分裂是延续上的充要条件，更多是数目上的充要条件；`arisesFrom_of_more` 是充分的一面读于依存网。
- **整段上。** 一次分裂只在那一步起作用：`Fork` 在第一步分裂，此后形成仍在任意晚的步生起；每步都有分裂可以吸收增长（`Budding` 中一个形成延续为所有形成，`Tandem.budding` 中每步只一个形成延续为两个）。整段上只对延续关系给出与结论等价的条件，只是重述（存在由延续封闭、无界增长的列表序列），所以本节不把它当作定理；精确的是单步的刻画，整段上没有分裂只是充分条件。
- **延续下的平衡。** 证明以跨步延续的配对数为中介。步后被延续的形成不多于配对数（每个被延续的至少有一对，`mark_le_total`），没有合并时恰是（每个至多一对，`total_le_mark`）；步前被延续的形成也不多于配对数，没有分裂时恰是；两种配对数相同（`total_swap`）。步后的数目是被延续的加生起的，步前的数目是被延续的加止息的，于是没有分裂时步后连同止息的至多是步前连同生起的，没有合并时至少如此，两者都没有时相等（`Census.balanceFrom`、`balanceFrom_eq`）。每个形成只延续自身时（`self_one_to_one`），这就是 `Listed.across` 读于活动。
- **两半的定律。** 每步的不等式跨段累加（`le_over_stretch`、`ge_over_stretch`），抽象地：一个计数每步终点连同失去的不超过起点连同得到的，失去复现就需要得到复现，因为复现的失去累积超过起点的计数（`gaining_of_losing`）；反向且计数从某步起有界时，得到复现需要失去复现（`losing_of_gaining`）。读于延续：没有分裂时止息复现需要生起复现，这是 `arising_of_ceasing` 推到每个没有分裂的延续（`Census.arisingFrom_of_ceasingFrom`）；没有合并且从某步起至多 B 个活跃时生起复现需要止息复现，这是 `ceasing_of_arising` 推到每个没有合并的延续（`Census.ceasingFrom_of_arisingFrom`）。
- **每个条件都不可少。** `Tandem` 是一个展开、三种读法：每个形成只延续自身时每步一个生起、一个止息（`kept`）；读作萌出，较晚的形成延续为自身与新形成、较早的不被延续，普查成立、没有合并，每步一个止息而从不生起（`budding`）；读作合并，两个都延续为较晚的那个，至多两个活跃、没有分裂，每步一个生起而从不止息（`joining`）。展开不变，读出的生起与止息随读法而变；平衡的每一半恰在一种读法下失效。

**作者反审。**

*反驳 1：单步的刻画是平凡的。* 两个方向都短。内容在于界限精确了：以前只知道没有分裂充分，现在知道在一步上它也必要，而在整段上不必要（`Fork`），所以整段的结论依靠的是许多步上的没有分裂，不是关于延续关系的某个整体条件。

*反驳 2：`forces_iff_noSplit` 用了相等可判定。* 只在必要的方向用：从“不能有两个不同的”得到“相等”。不设可判定时，同样的论证给出相等的双重否定；这是构造逻辑的界限，不是公理。`forced_iff_more` 与平衡都不用它。

*反驳 3：延续关系任意给定，平衡是否只是记账？* 是计数，不是机制：它不说哪个形成生起，也不说哪个读法对。它说明的是，普查定律不依赖名字规定的同一：只要读法没有分裂，止息需要生起就成立；只要没有合并，有界时生起需要止息就成立；能抹去生起或止息的恰是分裂或合并。identity-across-steps 中“延续关系下……”的计数部分由此回答；形成的类、任期与侵蚀在延续下仍未陈述。

*反驳 4：`Tandem` 是特意构造的。* 是，最小见证。它的意义在于三种读法作用在同一个展开上，是 `Turnover`（同一由表示给出）的计数版本。萌出与合并在生物中有其例（分裂繁殖、融合），那是应用，不是定理的内容。

**边界。** 无伦理谓词，不评价生起或止息；只对离散步与每步有限的活动陈述；延续关系由读法给出，本节不说哪一个是同一；整段上没有分裂与没有合并只是充分条件；名称（CeasesFrom、NoMerge、Tandem、paired）是 AI 的表述，由 Ren 定。本节尚未经独立审查。

## 44. 交换归于静止（P33）

2026-10-10。按 Ren“aim a complete theory of becoming, and finish related work”继续，作为计划 P33。第十一次独立审查在 R3 中注意到 `hatch` 的流只在第 0 步参与，并给出一个论证：在静止定理的前提之下这是必然的，被围住的一步上有取用时总水平至少下降一，给予需要取用，每步立着的有限多时这只能发生有限多次；它注明这是手写论证，审查没有形式化它。§42 把 R3 的其余部分移入核心（`rest_few`），这一论证仍未检查。本节把它证明为定理，并给出它的每个前提都不可少的见证。没有新模块：定理放在 `Becoming.Openness`。成果记录：修订 [continued-change-needs-openness](../../../../theories/becoming/results/records/continued-change-needs-openness.md)。

```text
Result(s): 复用 continued-change-needs-openness（Flow.AroundStanding、standing_never_rises、falls_finitely、
           Web.StandingCensus.stock_eq、World.exposed_world、exposed_standing、Kindling.unlisted、Exposed.stands_iff）、
           Becoming.Dissipation（Flow.Balances.runs_down、DissipatesOn.takes_of_gives、witnesses_not_dissipative、
           Frontier.burning_self）、Becoming.Flow（Cycle.closed_more）、space-and-its-parts（leaking_world、
           kindling_world）；修订 continued-change-needs-openness
Delta: Openness：Flow.ExchangeRecurs、Flow.exchange_lowers、Flow.exchanges_finitely、World.exchange_stops、
       World.exchange_needs
Supplied premises / correspondence: 所立者的普查、平衡、耗散，以及从某步起每步不被否定地围住所立者（定理的假设）；
       不需要活动的普查、体现或相等的判定；交换指在场的形成取用或给予正的量
Evidence: 合并检查器回执 20261009T194202.548300Z（1157 项定理、1862 项声明审计、核心闭包 29 个模块、包 27 个模块，全部源声明公理报告
          为空）；外围桥接重跑 20261009T194414.300336Z；实例检查
Boundary: 只对离散步与自然数量陈述；交换归于静止陈述为复现的否定；不评价静止或开放；名称由 Ren 定
Integration: 计划 P33；把第十一次审查 R3 的手写论证变为定理；补足静止定理：被围住时停止的不只是水平的变化，
             还有交换本身
```

| 声明 | 内容 |
|---|---|
| `Flow.ExchangeRecurs` | 流在任意晚的步交换：某个在场的形成取用或给予正的量 |
| `Flow.exchange_lowers` | 平衡与耗散之下、所立者被列出时，跨过围住所立者的一步，在场的形成取用或给予任何东西，所立者的总水平都严格下降 |
| `Flow.exchanges_finitely` | 从某步起每步不被否定地围住所立者时，交换不复现 |
| `World.exchange_stops` | 世界层面的同一陈述：有所立者的普查、平衡、耗散且从某步起被围住所立者的世界中，交换不复现 |
| `World.exchange_needs` | 四个前提各不可少，缺少一个时其余成立而交换复现：`exposed`（满足八个前提，没有一步被围住）、Flow 的循环（被围住、平衡，不耗散）、`leaking`（被围住、耗散，不平衡）、`kindling`（被围住、平衡、耗散，所立者不能被列出） |

**解读。**

- **交换为什么降低总水平。** 围住的家族持有一步上交换的一切：在场的形成不从它之外取用，也不给它之外（`ClosedAt`）。形成有所取用时，取用落在家族之内；只给予时，耗散使给予家族需要从家族取用（`takes_of_gives`）。所以它从家族取用正的量，平衡的流下家族的总水平至少下降取用者的数目（`runs_down`），而所立者的总水平就是家族的总水平（`stock_eq`，用到所立者的普查）。证明是构造的：“取用落在家族之内”先只得到双重否定，借自然数比较的可判定性消去。
- **交换为什么停止。** 跨过这样的步总水平不上升（`standing_never_rises`），每次交换都使它下降；一个不上升的自然数序列只能下降有限多次（`falls_finitely`）。所以交换在任意晚的步发生，与从某步起每步被围住不相容。
- **不由水平不再变化推出。** `stills` 说水平不再变化；交换不必改变任何水平：Flow 的循环中每步取用一个单位再还回，水平不变而交换不息。所以要用的是耗散使每次交换都严格降低总水平（`exchange_lowers`），而不只是水平变化时才降低。
- **需要的比静止定理少，给出的也不同。** 静止定理说的是活动，所以还需要活动的普查与生起者体现；交换的静止只关于流与水平。`dusk` 满足 `exchange_stops` 的全部前提而止息不息（`rest_needs_census`）：交换归于静止不给活动归于静止。
- **每个前提都不可少。** `exchange_needs` 的四个见证各缺一个前提。`exposed` 中耗散空成立，因为没有一步被围住；`kindling` 中围住只对空列表成立，因为没有列表列出所立者（每个未燃的燃料都立着），这正是没有普查时前提剩下的内容：“围住某个列表”不约束所立者。

**作者反审。**

*反驳 1：这只是 `stills` 的推论。* 见上：循环中水平从不变化而交换不息，所以交换的停止要用每次交换都使总水平严格下降，这是本节新证的引理。

*反驳 2：`kindling` 的见证用了空列表，是取巧。* 定理的前提是：有一个列表是所立者的普查，且从某步起每步围住它。去掉普查，剩下的“每步围住这个列表”对空列表成立；`kindling` 表明这时交换可以不息，所以普查不能去掉，而不是说空列表是所立者。

*反驳 3：陈述为复现的否定太弱。* 与静止定理同一形式（`¬ ArisingRecurs`）。得到“某步之后再没有交换”需要判定交换是否发生；可以判定时经典地两者等价。这是构造逻辑的界限，不是公理。

*反驳 4：这对生生有什么意义？* 本节不作评价。它说的是：在所立者有界地被列出、平衡且耗散的展开中，不只是持续的生起，连持续的交换都需要越出所立者的步。“开放”在这里有了更具体的形式内容：交换的持续，而不只是变化的持续。读法与名称属于 Ren。

**边界。** 无伦理谓词，不评价静止或开放；只对离散步与自然数量陈述；交换的静止是复现的否定；名称（ExchangeRecurs、exchange_lowers、exchanges_finitely、exchange_stops、exchange_needs）是 AI 的表述，由 Ren 定。本节尚未经独立审查。

## 45. 第十二次独立审查与更正（P33b）

2026-10-10。按 Ren“aim a complete theory of becoming, and finish related work”继续。另一 agent（Claude Opus 5.5，未参与撰写）独立审查了 P30（§40）、P31（§41）与 P29b（§42）（[审查](BECOMING-P30-P31-P29B-REVIEW.md)，对象 `a9326202`）。它在仓库之外从前导重新编译核心闭包的 29 个模块，1896 条源声明（1171 项定理）的公理报告全空；闭包的 5333 个常量中依赖公理的只有 35 条编译器生成的 `injEq` 引理，都只依赖 `propext`，与回执所列相同；回执、源哈希、保留产物、外围回执、402 个引用哈希与 112 个证明绑定都对，各阶段的计数与章节、研究和计划一致。数学全部接受，没有错误的 Lean 陈述。它写了 55 条探针声明（38 项定理，生成的 107 个常量都不依赖公理），提出八项（T1–T8）：三项错误（命名、散文与文档注释各一，T1、T3、T4），三项过强（T2、T5、T6），两项出处与记账（T7、T8）。第十一次审查的 R1、R2、R4–R7、R10 关闭；R3、R8、R9、R11 的残留就是 T5、T4、T7、T8。P32（§43）与 P33（§44）在审查期间或之后提交，审查没有读。本节逐项处理，并把审查的三个探针移入核心。成果记录：修订 [reserve-defers-ending](../../../../theories/becoming/results/records/reserve-defers-ending.md)、[continued-change-needs-openness](../../../../theories/becoming/results/records/continued-change-needs-openness.md)、[bounded-census-keeps-pace](../../../../theories/becoming/results/records/bounded-census-keeps-pace.md)；没有新的成果记录。

```text
Result(s): 更正 reserve-defers-ending（T2、T3）、continued-change-needs-openness（T4、T5）、bounded-census-keeps-pace（T1、T6）；
           没有新的成果记录
Delta: Change：LPO、clear、Clear（cases、false_of_not、not_both、and_left、and_right、and_both、of_not、mono、false_before、or_first、
       first_of_true、first_unique）。Reserve：Carries.chain_ends 与 chain_ends_of_em 改为对 n 环的有限链陈述；Web.climbs、
       Web.no_unending_chain；ShortCascade（web、unsupported、carries、decays、ranked）、short_cascade；Once（ind、ind_and_le、ind_fall、
       web、reserve、unsupported、carries、decided、once）、Web.lpo_of_ending。Openness：去掉重复的 namespace World（P30 的世界名为
       World.slow、World.slow_world 与 Slow.*）；Few（pick、found、passed、distinct_pick、distinct_found、mem_pick、mem_found、listed、
       comes_at、quiet）、Listed.lpo_of_few；holding_world 与模块说明的更正。Premises：模块说明的更正。登记：按回执所列的完整名称
       核对记录中的声明
Supplied premises / correspondence: 不变；LPO 是被陈述的命题，不是公理，也不是假设
Evidence: 合并检查器回执 20261009T195744.874839Z（1190 项定理／1905 项声明审计，核心闭包 29 个模块，包 27 个模块，源声明的公理报告全空）；
          外围桥接重跑 20261009T195906.931285Z；实例检查；make research-test
Boundary: 不含伦理结论；不替 Ren 选择任何读法；新名称（LPO 之外的 clear、Once、Few、ShortCascade、no_unending_chain、
          lpo_of_ending、lpo_of_few）是建议；新见证都是最小见证
Integration: §40、§41 与英文 P30、P31 的就地更正；来源文件的 AI 更正说明（T7）；计划 P30 一行补回执（T8）
```

### 45.1 逐项处理

| 项 | 审查所见 | 处理 |
|---|---|---|
| T1 | `Openness.lean` 在已打开的 `namespace World` 中又打开一次，P30 的世界实际叫 `Becoming.World.World.slow`；章节、研究、计划、文档注释与 bounded-census-keeps-pace 的别名和引用所写的 `World.slow_world` 不存在；登记只按名称的末段核对 | 去掉内层 namespace，把 `namespace Slow` 移到 `World` 之外，名称成为 `Becoming.World.slow`、`World.slow_world` 与 `Becoming.Slow.*`，文本与记录原来写的就是这些。登记检查加一步：证明绑定所指的回执列出该模块由 Lean 展开的声明时，记录中的每个声明须以完整名称出现在其中（`tools/research/registry.py`，并加测试）；全部记录现在通过 |
| T2 | `Carries.chain_ends` 与 `chain_ends_of_em` 的前提对每个 k 要求第 k+1 环依存于第 k 环，所以要求不止的链；在有限、没有依存之环的网中（如任何食物链）两个定理空成立；“沿到达它的任一条链”的说法多于任何已陈述的定理 | 两个定理改为对 n 环的有限链陈述（前提只对 k < n，结论对 k ≤ n），不止的链是对每个 n 的情形，名称不变。新增 `Web.no_unending_chain`（依存沿有界的等级上升时没有不止的链，审查的 `no_chain`）与 `short_cascade`（`Cascade` 截为三个关系项：有限形式给出关系项 2 从第 3 步起不活跃，界可以达到，而不止的链不存在，审查的 `Short.short`）。§41 反驳 3 与英文 P31 就地更正 |
| T3 | §41 与英文 P31 说把“只在有限多步活跃”化为终结之步“需要马尔可夫原则”；这一步即使在活动可判定且至多发生一次时也蕴含 LPO，马尔可夫原则推不出 LPO | 移入核心：`LPO`（Change）与 `Web.lpo_of_ending`（Reserve，见证 `Once`）：若每个从不被支持、有储备且活动可判定的形成都有一步之后不再活跃，LPO 成立。两处就地更正。马尔可夫原则推不出 LPO 是标准事实（Kleene 可实现性），本节不形式化 |
| T4 | `holding_world` 的说明以“生起者体现”转述 `arising_opens`；后者要求每个关系项都体现，`kindling` 满足说明所列的前提、每步被围住而生起不息 | 说明改为：每个关系项都体现时开放是必要的，不充分；只要生起者体现时不必要，`kindling` 每步被围住而生起不息（`rest_needs_standing`） |
| T5 | `Openness` 与 `Premises` 的模块说明说静止的世界中曾经活跃或立着的“只有有限多”，而 `rest_few` 给出的是“不是无界多”；有一个列表列出全部的较强形式蕴含 LPO | 说明改为“不是无界多”（P33 已改两处，本节改其余各处），`counted_of_ever` 的前提写为“有一个列表列出每个曾经活跃的关系项”。移入核心：`Listed.lpo_of_few`（见证 `Few`）：若每个每步被列出、开始成立不复现的规定都有这样的列表，LPO 成立 |
| T6 | bounded-census-keeps-pace 的 next_delta 说“判据是比率”，比率形式只是充分条件 | 改为：精确的判据是缺额，比率形式是充分条件，slow 中从不满足 |
| T7 | 来源文件的更正说明把“生起”“止息”定为 AI 在 P23c 中的译名；它们自 P10、P19 起就在用，P23c 用它们命名空间的部分 | 来源文件中 AI 的更正说明就地改正并注明出处；Ren 的原话不变。第十一次审查是证据，不改 |
| T8 | (a) 计划 P30 一行没有回执；(b) 已提交的 `lean-index.json` 列入另一会话未跟踪的草稿文件 | (a) 补上回执 20261009T170233.740799Z 与外围回执 20261009T170422.519028Z。(b) `lean_catalogue.py` 按设计包括未跟踪文件；那些文件属于另一会话，不触动，也不改共享的工具；它们提交后索引即与提交一致。已告知那个会话 |

### 45.2 新的已检查声明

| 声明 | 内容 |
|---|---|
| `LPO` | 有限全知原则：每个布尔序列有某项为真或处处为假；排中律给出它，它没有构造性证明 |
| `clear`、`Clear.*` | 第 t 步之前没有真；第一个真唯一，有真就有第一个真 |
| `Carries.chain_ends`、`Carries.chain_ends_of_em` | 对 n 环的有限链：被依存的关系项体现、每环以正需要依存于前一环、第一环从 T 起终结时，直到第 n 个的关系项各在其前各环的储备过去后终结（储备衰减），或以排中律为假设各有终结之步 |
| `Web.no_unending_chain` | 依存沿以 K 为界的等级上升时，没有满足不止的链前提的序列 |
| `short_cascade` | 截为三个关系项的级联：有限形式给出的界可以达到，不止的链不存在 |
| `Web.lpo_of_ending` | 若每个从不被支持、有储备且活动可判定的形成都有一步之后不再活跃，LPO 成立；见证 `Once` 在 s 的第一个真处活跃一次 |
| `Listed.lpo_of_few` | 若每个每步被列出、开始成立不复现的规定都有一个列表列出曾经成立的全部成员，LPO 成立；见证 `Few` 每步至多列出一个成员 |

### 45.3 作者反审

*反驳 1：把 `chain_ends` 改为有限形式而沿用名称，掩盖了原来的错。* 原陈述没有错，只是要求不止的链；新陈述严格更一般，原陈述是它对每个 n 的实例，原陈述的检查保留在回执 20261009T185557.684339Z 与此后各回执中，本节与记录历史写明了改变。沿用名称是因为各处文本说的“沿依存之链”本来指有限的链，现在与定理一致。

*反驳 2：LPO 的两个定理是逻辑上的附注，不属于生成之论。* 它们说明核心为什么只陈述较弱的形式：不在任意晚的步活跃、曾经成立的不是无界多，而不是有一步之后不再活跃、有一个列表列出全部。这是核心的逻辑承诺（章节 §8）的一部分，与 `law_iff_em` 同类：说明哪一步需要非构造的原则，以及需要多强的原则。

*反驳 3：名称检查只覆盖有回执列出声明的模块。* 是。别的回执不列展开的声明，那里仍只按名称的末段核对；审查列出的 84 个非核心名称属于那些模块，本节不改。

**边界。** 无伦理谓词；Ren 的选择保持开放；本节的新名称是 AI 的表述，由 Ren 定。本节尚未经独立审查。

## 46. 计数的全部规律（P34）

2026-10-10。按 Ren“aim a complete theory of becoming, and finish related work”继续，作为计划 P34。开放纲领把“对整个空间成立的规律的完整清单”列为进一步的证明；P23 的完成标准第 2 项说整体的规律“除了表示本身所排除的，不排除任何展开”。到 P33 为止，普查的平衡与由它推出的复现定律都已检查，但没有证明它们就是计数的全部规律：可能还有别的、尚未发现的计数规律。本节对计数回答这个问题，并说明哪些前提约束计数、全部八个约束到什么程度。成果记录：新增 [whole-law-of-counting](../../../../theories/becoming/results/records/whole-law-of-counting.md)。

```text
Result(s): 复用 census-balance（Listed、Listed.across 的证明、marks_le_of_sub、Web.Census）、
           coming-and-ceasing-keep-pace（comings、ceasings、mark、steps_last、steps_mem）、map-of-premises（八个前提、
           World.still_vacuous）、life-as-condition-of-life（Web.Embodied.arises_given）、space-and-its-parts（World、
           Flow.still）；新增 whole-law-of-counting
Delta: Population：Listed.keeps（Listed.across 改由它推出）、Tally、Listed.tally、steps 的长度与成员、Queue（gone、holds、
       line、listed、ceasings_eq、comings_eq、counts）、Pointwise、counting_laws；
       Premises：World.CountsObey、Queue.web、Queue.embodied、World.queue、World.embodiedQueue、queue_premised、
       embodiedQueue_premised、counting_free、Queue.lone_tally、counting_binds_jointly、Tended（队首照管的队列）、
       World.tendedQueue、tendedQueue_premised、premised_counting；Population：mark_turn
Supplied premises / correspondence: 列出与可判定（同普查的平衡）；性质尊重计数每步的值（Pointwise，代替函数外延性）
Evidence: 合并检查器回执 20261009T205957.521123Z（1223 项定理、1958 项声明审计、核心闭包 29 个模块、包 27 个模块，全部源声明公理报告为空）；
          外围桥接重跑 20261009T210516.903787Z；实例检查
Boundary: 只对离散步与每步有限的成立者陈述；只说计数；有限世界中与被围住时（静止定理之外）计数的规律没有陈述；
          不评价生起或止息；名称由 Ren 定
Integration: 计划 P34；回答开放纲领“对整个空间成立的规律的完整清单”的计数部分；补足前提的地图：哪些前提约束计数，
             全部八个约束到什么程度
```

| 声明 | 内容 |
|---|---|
| `Listed.keeps` | 跨每一步保持一些成员：连同不再成立的是步前的列表，连同开始成立的是步后的列表；普查的平衡 `Listed.across` 现由它推出 |
| `Tally`、`Listed.tally` | 计数表：每步某数 k 使 n t = k + c t 且 n (t+1) = k + a t；每个列出的计数都是计数表 |
| `Queue.holds`、`Queue.line`、`Queue.listed` | 队列：第 t 步在队中的，是从此前离开的总数起的 n t 个自然数，从队尾加入、从队首离开；每步被不重复地列出 |
| `Queue.counts` | 计数表之下，队列每步列出 n t 个，跨步离开 c t 个（队首的），加入 a t 个（队尾的） |
| `counting_laws` | 对计数的一个逐点的性质，在每个类型上每个列出的计数都满足它，恰当每个计数表都满足它 |
| `World.queue_premised`、`World.embodiedQueue_premised` | 排队而什么都不流动的世界满足除体现外的全部前提；排队且恰在活跃时立着的世界满足除平衡外的全部前提 |
| `World.counting_free` | 对计数的一个逐点的性质：对每个计数表成立，恰当它在每个世界的每个普查中成立，恰当它在满足除体现外全部前提的每个世界中成立，恰当它在满足除平衡外全部前提的每个世界中成立 |
| `World.counting_binds_jointly` | 平衡、只有活跃者给予且生起者体现时，普查之下没有关系项活跃的一步上没有生起；一个关系项从无到有地生起（`Queue.lone_tally`）在两个队列世界中都实现，所以这不是计数的规律 |
| `World.tendedQueue`、`World.tendedQueue_premised` | 由队首照管的队列：队首给予每个加入者一个单位、从每个离开者取用一个单位，活跃时与每个地关系项各交换一个单位；没有成员加入空队时满足全部八个前提 |
| `World.premised_counting` | 对计数的一个逐点的性质在满足全部八个前提的每个世界的普查中成立，恰当它对每个没有关系项活跃的一步上没有生起的计数表成立 |

**解读。**

- **为什么计数表是全部。** 计数表说的是：跨每一步，在场者分为留下的与离开的，之后的在场者是留下的加上来到的。任何满足这一点的数目序列，都可以由一个队列实现：成员依次从队尾加入，依次从队首离开，每步离开的恰是队首的 c t 个，加入的恰是队尾的 a t 个。所以从计数本身推不出关于展开的任何更多的东西；P26 到 P30 的复现定律、比率与界，都是计数表的推论（它们只用到平衡的等式），而不是另外的规律。（P34b 就地更正：此条原题“为什么平衡是全部”，说的却是保持的形式；平衡的等式严格弱于计数表，见下一条与 §48 U1。）
- **保持的形式。** 平衡原先写为 n (t+1) + c t = n t + a t。保持的形式更多地说出关系：跨一步有一些成员留下，离开的与来到的都相对于它们计数。它严格强于等式：它还说跨一步不再成立的不多于步前所列的，等式不给出这一点；计数表恰是平衡加上这一界（`tally_iff`），每步零个在列、一个不再成立、一个开始成立满足平衡而不是计数表（`balance_not_tally`），没有列出有这样的计数。所以全部规律须以保持的形式陈述。保持的形式推出原来的形式（`Listed.across` 由它推出）。（P34b 就地更正：原文给出的理由是保持的形式使证明不需要带 `propext` 的消去律；核心有不带公理的消去律，那不是理由，见 §48 U1、U7。）
- **逐点。** “对计数的一个性质”是数目序列上的任意命题。实现给出的计数与给定的计数逐点相等，而不是作为函数相等；在构造性的纯净核心中，由逐点相等推出函数相等需要函数外延性（Lean 中由 `Quot.sound` 证明）。所以定理要求性质尊重逐点相等。每个由各步的值说出的性质都如此，有函数外延性时每个性质都如此（P34b 就地更正：原文作“经典地”；函数外延性不是经典原则，Lean 中它来自 `Quot.sound`，与排中律和选择无关，见 §48 U7）。不用这一假设的刻画是：列出所能有的计数恰是计数表（`tally_iff_counted`）。
- **前提怎样约束计数。** 八个前提彼此独立（P24），但它们对计数的作用不同：缺平衡或缺体现的任何一组都不约束计数，因为两个队列世界分别满足除体现外与除平衡外的全部前提（关于流的前提在什么都不流动时空成立，体现在恰在活跃时立着时成立而平衡不成立）。平衡与体现连同只有活跃者给予一起约束：体现的生起是开始作为条件而在，平衡要求它被给予，只有活跃者给予要求给予者活跃，所以生起需要一个在场者。这不是计数的规律，因为从无到有的生起是一个计数表。
- **全部八个前提所加的。** 由队首照管的队列满足全部八个前提：队首给予加入者、从离开者取用，所以平衡成立，加入者由活跃的队首给予，离开者被活跃的队首取用；成员恰在队中时立着，所以体现成立；队首活跃时与每个地关系项各交换一个单位，净量为零，地关系项的水平不变而仍为零，所以没有有限家族在这样的步封闭，耗散在那里空成立；队空时（这时没有成员加入，也没有成员离开）什么都不交换。所以八个前提一起只在计数上加了一条：没有关系项活跃的一步上没有生起（`premised_counting`）。（P34b：审查（U3）指出，这个见证中耗散从不起约束，活动需要支持与有界传递也不起约束（`World.tended_not_binds`）；`premised_counting` 的范围包括前提空成立的世界。每个前提都起约束时，每个普查都计到某个生起（`World.binds_arising`），这在八个前提之下不是规律（`World.binds_adds`）。见 §48。）
- **与静止定理。** 静止定理（P26）是平衡、耗散、体现与被围住一起对计数的约束：生起与止息都不再复现。上面的世界中队首活跃的步没有一步被围住，所以它不受静止定理约束；计数在八个前提之下的这种自由，可以读作开放（P25）在计数上的形式（AI 的读法）。这些约束都来自前提的合作与被围住，不来自计数本身。

**作者反审。**

*反驳 1：队列太特殊，不是世界的“自然”实现。* 定理断言的是存在：每个计数表都至少由一个列出实现。任何更多的计数规律都必须在所有列出中成立，包括队列；队列不满足它，它就不是规律。实现是否“自然”与此无关。

*反驳 2：队列世界的关系项无限多，所以这不说明有限世界。* 对。有限世界中计数还受关系项的数目所限（在场的与来到的都不多于关系项），那里计数的规律本节没有陈述。记录的局限与下一步写明了这一点。（P35：它们已经陈述：有限世界中计数的规律恰是计数表、没有关系项活跃的一步上没有生起与从第 0 步起的变化界，与从某步起被围住时相同，见 §49。）

*反驳 3：`Pointwise` 是一个藏起来的公理。* 不是：它是定理的假设，不是核心的公理，任何具体的性质都可以直接检查它，例如 `counting_binds_jointly` 中的性质。它代替的是函数外延性，后者在 Lean 中依赖 `Quot.sound`；纯净核心不使用它。

*反驳 4：缺平衡或缺体现时不约束计数，这说明前提无用。* 不是：它说明每个前提单独地都不在计数上留下痕迹，约束计数的是前提之间的关系。平衡与体现一起说出了生起的一个条件（一个在场的给予者），再加上耗散与被围住，就有静止定理。这是一元方法的一个具体形式：约束来自关系，而不是来自分别命名的前提。

*反驳 5：队首照管的队列中耗散空成立，这使“满足全部八个前提”变得廉价。* 耗散只约束有封闭的有限家族的步（P16b）；队首活跃时它与无限多个地关系项交换，这正是 `exposed` 中那样的开放。见证没有违反任何前提，它说明：在不被围住的展开中，八个前提一起不再约束计数，除了生起需要一个在场者。若要求被围住，静止定理给出更强的约束；本节不陈述被围住时计数的全部规律。（P35：§49 陈述了它：再加一个变化界。）

*反驳 6：这对生生有什么意义？* 本节不作评价。它说的是：在场者的数目本身只记录进入与离开相抵；展开的方向（生起是否不息、是否归于静止）不能从计数读出，只能从给予与取用的关系读出。读法与名称属于 Ren。

**边界。** 无伦理谓词，不评价生起或止息；只对离散步与每步有限的成立者陈述；只说计数，读于世界只说活动；有限世界中与被围住时计数的规律见 §49；名称（Tally、Queue、Pointwise、CountsObey、counting_laws、counting_free、counting_binds_jointly、queue、embodiedQueue、tendedQueue、Tended、lone、mark_turn）是 AI 的表述，由 Ren 定。本节尚未经独立审查。

## 47. 延续的奠基：从想要延续者重述（W1–W5）

2026-10-10。Ren 提议从“想要自身延续者”重述普遍元伦理核心（[原话](../../../../sources/15-codex-theory-conversations/2026-10-10-wanting-continuation-one-axiom.md)）：想要延续者使其延续有意义；它须计入的整体范围依视角而定，不需要任何公理；加一条公理即闭合整体。AI 把它分为两半：动力学定出想要延续者必须计入的范围，定不出中心；那条公理的唯一作用是让每一点都是中心。Ren 答“exactly”，并说“commit them, then start implementation all the way to full completion”。本节实现[延续奠基计划](CONTINUATION-GROUNDING-PLAN.md)的 W1–W5；阶段以 W 编号，与并行会话的 P 编号分开。成果记录：新增 [continuing-self-fed-from-beyond](../../../../theories/becoming/results/records/continuing-self-fed-from-beyond.md)、[own-count-misses-joint-excess](../../../../theories/becoming/results/records/own-count-misses-joint-excess.md)、[held-lives-g0-is-centering](../../../../theories/becoming/results/records/held-lives-g0-is-centering.md)、[conveyance-crosses-the-boundary](../../../../theories/becoming/results/records/conveyance-crosses-the-boundary.md)、[derived-extent-limits](../../../../theories/becoming/results/records/derived-extent-limits.md)。

```text
Result(s): 复用 no-finite-part-bears-taking（taking_draws_in、Inward、Around、Lone）、generation-is-replenishment
           （rising_draws_in、Web.generation_draws_in）、more-needs-renewers（Balances、Acting）、
           metaethical-core-characterization（Valuation、SelfGood、transmits、shares、Neutral、Within、Reach）、
           becoming-stepwise-reading（Web.valuation、UnderminingAt、MetAbove.now）、life-as-condition-of-life（Flow.roles、
           Web.roles、inr_not_mem）、living-on-and-descent（sustenance、descent）、condition-correspondence-discipline
           （interaction）；新增上面五项
Delta: Continuation（L3，导入 Roles）：Conveys、FedFromBeyond、not_inward_of_fed、inward_of_not_fed、inward_iff_not_fed、
       fed_of_not_inward、fed_from_beyond、rising_fed_from_beyond、Web.generation_fed_from_beyond、Lone.fed、
       Lone.each_fuel_once、Lone.supply_not_source；WithinOwn、WithinJoint、joint_keeps、excess_lowers、excess_bounded、
       Pair、stays_below、ends_below、joint_excess_ends、Exceeding、Alone；Downstream、Mortal、Totalizer.careful；
       Standpoints（L4，导入 Descent 与 Continuation）：Valuation.Held、Valuation.Unheld、significant_iff_held、
       significant_iff_reached、Apart、Unclaimed、Relayed、Web.held_by_formations、Web.significant_iff_self；
       Flow.conveyance、conveyance_idle、boundary_crossed、Cut、region_not_a_cut、valuing_reaches_source、
       roles_conveyance、roles_conditions_unrelated；Totalizer.crossed、supply_not_cut、conveyance_only、own、
       valuation、center_not_derived
Supplied premises / correspondence: 平衡、耗散、被围住、不重复、可判定相等（W1、W2）；更新依存于所更新者的门控、Acting、
           Dependent（W3）；持有与可判定的持有，S0、N_std、N_rel 都是假设（W5）；输送作为 related（W2，Ren 的选择）；
           从想要一个目的到有理由求其所需的一步（W4）
Evidence: 合并检查器回执 20261009T222752.438253Z（1280 项定理、2062 项声明审计、核心闭包 31 个模块、包 29 个模块，全部源声明公理报告为空；
          Continuation 中 Lean 生成的 Totalizer.Place.fuel.injEq 依赖 propext，没有源声明使用它）；外围回执 20261009T223112.652163Z；实例检查
Boundary: 没有伦理公理；G0 仍是所采用的公理，重述待 Ren 接受；持有、输送与“想要即 S0”是对应前提或读法；见证是最小的；
          与外围磨损定律的联系是诠释性的；名称由 Ren 定
Integration: 延续奠基计划 W1–W5；Ren 提议的两半；chapter §6.7；G0 刻画（§6.1）保持其范围
```

| 声明 | 内容 |
|---|---|
| `Flow.Conveys`、`Flow.FedFromBeyond` | 参与的形成从 c 取用、向 d 给予，即有东西从 c 输送到 d；有东西从家族之外输送入某个成员，即家族从其外得到供给 |
| `Flow.inward_iff_not_fed` | 相等可判定时，从其外得到供给恰是该步不内向（`not_inward_of_fed` 不需要可判定） |
| `Flow.fed_from_beyond`、`Flow.rising_fed_from_beyond`、`Web.generation_fed_from_beyond` | 平衡与耗散之下，取用复现、成员上升复现或体现成员生起复现的有限家族，从某步起被围住时，不能从某步起都没有东西从其外输送入 |
| `Lone.supply_not_source` | 池每步都从其外得到供给，每份燃料只在它自己的那一步被输送出：必要的是得到供给，不必有哪个来源条件复现（输送的始终是同一个太阳） |
| `Flow.WithinOwn`、`Flow.WithinJoint`、`Pair.own_not_joint` | 各自在所给之内，合起来可以超出 |
| `Flow.joint_keeps`、`Flow.excess_lowers`、`Flow.excess_bounded`、`Pair.no_web` | 联合地在所给之内时水平不降；联合超出每步至少降一，连续 n 步需要起点至少 n；Pair 没有平衡的网 |
| `Flow.stays_below`、`Flow.ends_below`、`Flow.joint_excess_ends` | 更新者以至少 m 的需要依存于所更新者、只有活跃者给予、活动需要支持时，水平一旦低于 m 就一直低于 m，以至少 m 的需要依存者从此不活跃；联合超出使水平低于 m 时，终结更新者与以这样的需要依存的每个形成，取用者以这样的需要依存时也在内 |
| `Exceeding.all_end`、`Alone.all_continue` | 一个更新者与两个各在所给之内的取用者，两步后都终结；只有一个取用者时都延续 |
| `Downstream.one_way` | 推出的范围单向：自身只依存于它的地，每步活跃且被支持；以它所给为生的下游形成在它停止给予后终结 |
| `Mortal.after_its_end`、`Mortal.without_continues` | 想要的视界：生命两步、活着时每项依存都被满足的形成，终结了共享条件的更新，继承者在它终结之后才终结；没有它时其余延续 |
| `Totalizer.careful` | 谨慎的照管者：平衡、耗散、`Dependent`；照管者每步活跃且被支持，只依存于它的供给，供给被更新、每步从其外得到供给、被联合地在所给之内取用；它在第一步的事件侵蚀另一个形成，后者从第二步起不活跃 |
| `Valuation.Held`、`Valuation.significant_iff_held` | 每个活的主张都在某个立场的自身区域中时，G0 恰等于每个立场的 S0 加 N_std，不用连通与 N_rel |
| `Valuation.significant_iff_reached` | 持有可判定、每个活的主张都经已形成的关系从被持有的活的主张到达时，G0 恰等于处处 S0、N_std 与只指向无人持有者的 N_rel |
| `Apart`、`Unclaimed`、`Relayed` | 三个反模型：每个生命只被自己的立场珍视，两种中立都不成立（W8 后为 `Apart.not_enough`，原名 `standpoint_neutrality_is_needed`）；无人持有的生命；被到达而无人持有的生命 |
| `Web.held_by_formations`、`Web.significant_iff_self` | 逐步读、每个形成以自身事件为自身区域时，每个活的事件都被持有，G0 恰等于每个形成的 S0 加 N_std |
| `Flow.conveyance`、`Flow.conveyance_idle` | 以一类关系项读，输送使同一步的两个事件相关；闲置的关系项与任何事件都不相关 |
| `Flow.boundary_crossed`、`Flow.Cut`、`Flow.region_not_a_cut`、`Flow.valuing_reaches_source` | 延续家族的边界不会从某步起再无穿越，所以它的区域不是关系的切口；在 N_rel 下珍视一个关系项的事件，到达向它输送者的活的事件 |
| `Flow.roles_conveyance`、`Flow.roles_conditions_unrelated`、`Totalizer.conveyance_only` | 两个条件之间的输送使它们相关，交互、以之为生与世系在任何步上都不使两个条件相关；照管者的燃料与供给只由输送相关 |
| `Totalizer.center_not_derived` | （W8 后）各形成持有并珍视自身的事件，照管者也珍视太阳的事件：每个生命都被持有，S0 处处成立，各立场的意义沿供给（`Flow.FedBy`）封闭，而另一个形成活的事件从照管者的立场没有意义：N_std 与 G0 不成立；同一评价中照管者的事件经栖息地与之相关，从照管者自身区域沿已形成关系的传递不成立。W1–W5 的原陈述（向各自区域的传递，由 S0 推出）见 §47.2 C1 |

**解读。**

- **两半由证明分开。** 范围的一半（`Becoming.Continuation`）不含伦理谓词：它说想要延续者必须计入什么才能延续——其外的供给、对其所依存者的联合取用——而不说它应当计入。中心的一半（`Becoming.Standpoints`）说：对被持有的生命，G0 超出 S0 的可以集中在 N_std 上（在连通、每个立场都持有活主张的整体上也可集中在 N_rel 上，§47.2 C2）；而沿依存推出的范围不迫使 N_std（`Totalizer.center_not_derived`）。所以“这不需要任何公理”对范围成立，对中心在这一读法下不成立。（W8 更正：原文接着说计划 §3.4 的检验通过了，“见证造出来了”；审查指出原见证的传递合取由 S0 推出，检验如原样提出不可能失败。这一说法撤回；现在的见证含沿依存的封闭，界线的范围见 §47.2 C1。）
- **与原刻画。** `significant_iff`（§6.1）从一个种子出发，需要连通与 N_rel 把意义带到各处，§6.3 的大部分工作在保证连通。新的刻画在每个想要的点都有种子，在每个生命都被持有时只需 N_std 使它们共同；连通与 N_rel 在这一补全中只对无人持有的生命仍有作用，而在连通、每个立场都持有活主张的整体上，它们给出另一种补全（`significant_of_transmits`，W8）。在连通、有活的主张且每个生命都被持有的整体上，二者都等价于 G0；一般地互不蕴涵，原刻画保持其范围。对手的形状（§6.2）不变：主要的对手接受处处 S0，把意义限在各自的立场之内（`Apart`）。
- **范围以供给的形式到达其外。** 从其外得到供给是必要的，不必有哪个来源条件复现（`Lone`；输送的始终是同一个太阳，所以原文“特定的来源不是”多于它所示，W8 C3）；照管者的燃料每步不同。想要把他者计入为条件；主张层面的意义分不开把他者算作条件与算作想要者（W8 C2）；在 N_rel 下，以输送为关系时，珍视自身的事件到达来源的活的事件（`valuing_reaches_source`），但那是公理的关系一半，不是想要所要求的。
- **联合超出。** 元吸引子所选出的形成各自只计自身的取用；它们可以各在所给之内而合起来超出，联合超出持续不过原有的。更新依存于所更新者时（更新者的给予要求它自己被支持），联合超出终结更新与以这样的需要依存者，取用者以这样的需要依存时也在内；联合计入约束的是比条件所存更长远的想要（`Mortal`，W8 C6）。外部来源（太阳）的更新不受门控，这一结论不适用于它。与外围磨损定律（`jointly_exceeding_parts_end_shared_formation`）的联系是诠释性的，没有实例定理。
- **草图的改名。** 计划中的草图（`development/continuation-grounding-sketch/`）的三个反模型改名为 `Apart`（原 `OwnStandpoints`）、`Unclaimed`（原 `Unheld`，避免与 `Valuation.Unheld` 重名）与 `Relayed`（原 `Reached`）；其余声明保持草图中的名称。草图是计划的证据，保留原样。
- **弱式与强式。** 逐步读法的 `living`（活跃且不侵蚀）是弱式“不损”的一种读法；`Web.significant_iff_self` 在这一读法上给出“每个形成是自己的中心”。S0 只涉及活的主张，所以这样读时“不损”的过滤已在种子里（`Totalizer.keeper_not_living`，W8 C13）；Ren 的“as long as not harm”也可读作义务式：每个延续的意义是对他者不施损害的要求（W8 C12）。强式（整体的延续要创造更多意义）读作方向，联系 `Flow.More` 与 `World.ArisingRecurs`，本节没有新的形式内容。

**作者反审。**

*反驳 1：处处 S0 加 N_std 只是 G0 换个说法。* “G0 ⇒ 前提”的方向是平凡的；内容在反方向与极小性：对被持有的生命，连通与 N_rel 都不需要。这使论证的重心移动：§6.3 中保证连通的读法与纪律，对被持有的生命不再是 G0 的前提。

*反驳 2：持有把结论放进了前提。* 持有是对应前提，不是伦理前提：它说哪些生命在某个立场的自身区域中。在持有之下，结论还需要 N_std；`Apart` 说明两种中立都没有时，每个生命都被持有、处处 S0，而 G0 不成立。所以持有定位了中立的作用，没有替代它；在被持有的生命上 N_std 足够，但不是唯一的补全（W8 C2）。

*反驳 3：谨慎的照管者是人为的。* 定理是存在性的：推出的要求不迫使 N_std。更自然的见证不会改变这一点；若要推翻它，需要证明某个推出的要求蕴含 N_std，那将是更强、会改变论述的结果。（W8 更正：原见证没有含推出的要求，在评价层面它与 `Apart` 相同；现在的见证含沿依存的封闭。沿每个已形成关系读推出的范围时，界线不成立，见 §47.2 C1、C2。）

*反驳 4：输送使一切供给链连通，太廉价。* 输送需要实际的取用与给予；闲置的关系项不相关（`conveyance_idle`）。它确实比交互、以之为生与世系连通更多（`roles_conditions_unrelated`），所以是否采用它是实质的选择，属于 Ren。

*反驳 5：联合超出终结取用者自己，所以自利足以保护共享条件。* 只保护到自身所依存的程度：`Downstream` 中依存于自身的下游不在范围内，`Totalizer` 中照管者不依存的栖息地不在范围内，`Mortal` 中即使所依存的也只到想要的视界为止。

*反驳 6：“不需要任何公理”不成立，因为用了平衡、耗散与被围住。* 读作不需要伦理公理（[来源记录](../../../../sources/15-codex-theory-conversations/2026-10-10-wanting-continuation-one-axiom.md)的解释）：物理、对应与表示的前提仍是公开的前提，各有满足与不满足它们的世界。

*反驳 7：门控的联合超出与外围的磨损定律没有实例定理。* 对。记录把这一联系列为诠释性的，下一步是实例定理。

**边界。** 范围的一半没有伦理谓词；中心的一半不证明 S0、N_std 或 N_rel，不约束拒绝它们的立场，不推出义务、排序、认识或遵循。G0 仍是所采用的公理；重述、“想要即 S0”、公理的范围（想要者还是一切；无人持有的生命）、伤害的层级、“更多”的读法、输送是否算已形成的关系与名称（Conveys、FedFromBeyond、WithinOwn、WithinJoint、Held、Unheld、Apart、Unclaimed、Relayed、Cut、Exceeding、Alone、Downstream、Mortal、Totalizer、keeper 等）都由 Ren 定。见证是最小的。本节已经独立审查，更正见 §47.1–47.4。

### 47.1 独立审查与更正（W8）

2026-10-10。按计划 W8，另一 agent（Claude Opus 5.5，未参与撰写）独立审查了 W1–W5（[审查](CONTINUATION-GROUNDING-REVIEW.md)，对象 `1f6f375f`）。它对照回执 20261009T222752.438253Z 的源哈希重新编译探针，所有探针声明都不依赖公理。它判定 Lean 正确、无公理，一般定理说的与说明一致；G0 处处保持为所采用的公理，Ren 的选择都已列出。问题在诠释一层：共十三项，C1–C6 实质，C7–C13 次要，没有阻断项。探针以 `1f6f375f` 的字节重新编译，12 条公理报告全空，保存在 [development/continuation-grounding-review-probes/](development/continuation-grounding-review-probes/)。

```text
Result(s): 更正 derived-extent-limits（C1、C3、C7、C10、C11、C13）、held-lives-g0-is-centering（C2、C4、C5、C10、C11）、
           continuing-self-fed-from-beyond（C3、C9、C10）、own-count-misses-joint-excess（C6、C7）、
           conveyance-crosses-the-boundary（C8、C9）；没有新的成果记录
Delta: Standpoints：Valuation.own_transmission、Valuation.significant_of_transmits；Apart.standpoint_neutrality_is_needed 改名为
       Apart.not_enough，并加上 N_rel 不成立；Flow.FedBy；Totalizer.supply_not_cut_living_on、Totalizer.sig、Totalizer.fedBy_sun、
       Totalizer.keeper_not_living；Totalizer.valuation 改为照管者也珍视太阳的事件；Totalizer.center_not_derived 改为含沿供给的
       封闭、照管者的事件与另一形成的事件相关、从自身区域沿已形成关系的传递不成立；模块说明（标题改为“谁的延续计入”）。
       Continuation：模块说明与 Exceeding.all_end 的说明。根模块、README、check_becoming 的范围说明
Supplied premises / correspondence: 不变；FedBy 是依存的一步读法（在同一步参与并向所需条件给予），是对应的选择
Evidence: 合并检查器回执 20261009T231934.987085Z（1285 项定理／2069 项声明审计，核心闭包 31 个模块，包 29 个模块，源声明的公理报告全空；
          Continuation 中 Lean 生成的 Totalizer.Place.fuel.injEq 依赖 propext，没有源声明使用它）；外围回执 20261010T073508.393062Z（桥接 7 项定理，公理报告
          为空；此前两次尝试在机器内存压力下未完成，不作证据）；审查探针的重跑（不属于包）
Boundary: 不含伦理结论；不替 Ren 选择任何读法；“中心不由推出”限于沿依存推出的范围；新名称是建议
Integration: §47 与英文 W1–W5 的就地更正；章节 §6.7、前提卡、第 6 与第 10 项、§8–§10；计划 §0、§2–§4、§9 与实现状况；统一计划一行
```

### 47.2 逐项处理

| 项 | 审查所见 | 处理 |
|---|---|---|
| C1 | `center_not_derived` 的传递合取（意义传入各自区域）在任何评价中都由 S0 推出，所以评价层面的内容与 `Apart` 相同。Flow 与 Web 的谓词从不约束 sig，计划 §9 的检验如原样提出不可能失败 | 一般定理 `Valuation.own_transmission` 写明这一点。新增 `Flow.FedBy`；`Totalizer.valuation` 改为各形成珍视自身的事件、照管者也珍视太阳的事件；`center_not_derived` 改为：持有、处处 S0、各立场的意义沿供给封闭（从任何被珍视的事件出发，不只从自身区域）、另一形成活着而照管者不珍视、N_std 与 G0 不成立，并加上照管者的事件与另一形成的事件经栖息地相关、从自身区域沿已形成关系的传递不成立（审查的 `Tot.stronger` 与 `out_of_own_fails`）。界线写为：对沿依存推出的范围成立，对沿每个已形成关系推出的范围不成立。“见证造出来了”作为检验通过的说法撤回（§47 解读、记录、计划 §9）；“每项推出要求”改为“此处推出的每项要求”。原陈述在回执 20261009T222752.438253Z 中检查过，记录历史写明改变 |
| C2 | N_std 不是唯一的补全：连通、每个位置都持有活主张时，S0 加 N_rel 给出 G0；`Apart` 连通，N_rel 也不成立，所以它只说明持有与 S0 不够；主张层面的 sig 分不开工具性与最终的意义 | 新增 `Valuation.significant_of_transmits`；`Apart` 的定理改名 `not_enough` 并加上 N_rel 不成立；“中心不由推出”加上范围（沿依存，并且某个活主张在某个想要者的依存闭包之外）；写明选 N_std 是因为它不需要连通，并写明 sig 的局限（章节、模块、记录、计划）。把关系读作依存时，N_rel 正是“计入自身延续所依存的”的评价形式；这一读法对一般定理的应用是手写论证，没有另立定理 |
| C3 | `Lone` 只说明不必有来源条件复现，每次输送都是同一个太阳，而 `Lone.web.requires` 处处为假；中英文不一致 | 统一为“必要的是得到供给，不必有哪个来源条件复现”，并写明输送的始终是同一个太阳；derived-extent-limits 的第二个界限去掉“以供给的形式”；两个可移除来源交替供给的见证列为开放（章节 §8、记录 next_delta） |
| C4 | 若干处把 AI 的分解（S0 即想要，N_std 是唯一公理）归于 Ren | 模块说明、根模块、README、章节前提卡、术语表、第 10 项与计划 §0 都改为“AI 对 Ren 提议的读法，待 Ren” |
| C5 | “每一点都是中心”被注为 N_std，而放置中心的是 S0；N_std 是去中心化 | N_std 注为“从任一中心有意义的，从每个立场都有意义，没有哪个中心特殊”；“每个想要之点都是中心”归于 S0，并注明是 Ren 答“exactly”的 AI 说法；模块标题改为“谁的延续计入”；章节的草案就地改正 |
| C6 | 联合计入只约束比条件所存更长远的想要；“取用者在内”只对以这样的需要依存的取用者成立 | 两处限定写入模块说明、根模块、README、章节、记录与计划 §3.3 |
| C7 | 见证中的终结由定义规定 | 模块说明与 `all_end` 的说明改为：终结由活动规定，见证表明它们与平衡、支持和依存相容，终结的推出在一般定理中。强制形式（对 active 量化）没有加，列为开放 |
| C8 | “先前读法不穿越”言过：以之为生下供给的区域也不是切口 | 新增 `Totalizer.supply_not_cut_living_on`；说法改为：先前读法不使两个条件相关，输送新增的是两个条件之间、沿流入方向的关系 |
| C9 | 中文“传入”同时指输送与 N_rel 的传递 | 输送一律用“输送到／输送入／输送出”；“传递”只指 N_rel |
| C10 | 较小的言过与中英不一致五处 | 记录标题改为“G0 是 S0 加立场中立”；“都等价于 G0”加“有活的主张”；“不加前提”改为“只加可判定相等”；derived-extent-limits 的中文与英文对齐；`Lone` 的引用补 `Lone.lone` |
| C11 | `center_not_derived` 被两项记录认领，依赖方向反了 | 声明只归 derived-extent-limits，它对 held-lives-g0-is-centering 的 formal-reuse 改为复用 `Web.held_by_formations`；held-lives 不再列 `Totalizer` 的声明，对 own-count-misses-joint-excess 的依存去掉 |
| C12 | 章节引文删去 Ren 的中间一段而没有省略号；弱式的另一读法未列入 Ren 的选择 | 章节改为引 Ren 的全文（只略去重复助手的第一行，并注明）；弱式加上义务式的读法（每个延续的意义是对他者不施损害的要求），列入 Ren 的选择；它尚未形式化 |
| C13 | S0 只涉及 `living` 主张，已含“不损”的过滤；照管者的清除不服务任何东西；“被更新”依赖规定的太阳 | 新增 `Totalizer.keeper_not_living`；在模块说明、前提卡与记录中写明“S0 即想要”的读法含规范性的过滤，太阳什么都不需要是规定的。终结他者服务于照管者延续的见证（元吸引子的更强情形）列为开放 |

### 47.3 新的已检查声明

| 声明 | 内容 |
|---|---|
| `Valuation.own_transmission` | 处处 S0 时，每个立场的意义沿任何关系进入其自身区域：向自身区域的传递不比 S0 多 |
| `Valuation.significant_of_transmits` | 连通、每个立场都持有某个活主张时，处处 S0 加 N_rel 给出 G0（主张层面），不用 N_std |
| `Apart.not_enough` | 每个生命都被持有、只被自己的立场珍视：处处 S0，N_std、N_rel 与 G0 都不成立 |
| `Flow.FedBy` | 在同一步上，后一事件的形成参与并向前一事件的形成所需的条件给予 |
| `Totalizer.supply_not_cut_living_on` | 以之为生之下，以一类关系项读，供给的区域也不是切口：照管者以之为生 |
| `Totalizer.sig`、`Totalizer.valuation`、`Totalizer.fedBy_sun` | 各形成珍视自身的事件，照管者也珍视太阳的事件；只有照管者的延续被供给，且只被太阳供给 |
| `Totalizer.keeper_not_living` | 照管者在第一步的自身事件活跃而不活，S0 对它无所说 |
| `Totalizer.center_not_derived`（改） | 持有、处处 S0、各立场的意义沿供给封闭；另一形成在第零步活着而照管者不珍视；N_std 与 G0 不成立；照管者在第零步的事件与它相关，从自身区域沿已形成关系的传递不成立 |

### 47.4 作者反审

*反驳 1：沿供给封闭只是又一个由定义成立的合取。* 不是：它约束 sig。照管者若只珍视自身的事件，封闭就不成立，因为太阳供给它；审查的 `Tot.stronger` 正是为此而造。它说的是：照管者计入其延续所依存者（太阳的给予），仍不计入另一个形成。界线是否成立，取决于推出的范围沿依存还是沿每个已形成的关系；同一见证给出两边。

*反驳 2：既然 S0 加 N_rel 在连通的整体中也给出 G0，中心其实可以由动力学推出。* 只在依存使每两个生命都相连、每个立场都持有活的主张的整体中，并且要把 N_rel 本身读作想要的要求。N_rel 是规范前提：从“我的延续依存于它”到“它的活的事件对我有意义”是从想要一个目的到有理由求其所需的那一步（公开的前提），而它给出的是工具性的意义，主张层面的 sig 不区分工具性与最终的意义。所以这是第二种补全，不是从动力学推出中心；它在什么整体中成立是有用的判别，留给 Ren 的读法。

*反驳 3：太阳什么都不需要，使见证过于廉价。* 这是规定的，已写明。去掉这一规定、让太阳依存于燃料，只会让照管者的依存闭包包含更多条件，不会让它包含另一个形成的栖息地，因为照管者的延续不需要那个栖息地。更强的见证（终结他者服务于照管者的延续）列为开放。

*反驳 4：改名 `Apart` 的定理并改写 `center_not_derived`，掩盖了原来的说法。* 两者的原陈述都在回执 20261009T222752.438253Z 中检查过，记录历史与本节写明了改变；原陈述仍然为真，错误在诠释上，即把它们当作“需要 N_std”与“检验通过”的证据。

**边界。** 无伦理谓词；Ren 的选择保持开放，新增两项：推出的范围沿依存还是沿每个已形成的关系，以及“不损”是过滤还是对他者的要求；本节的新名称是 AI 的表述，由 Ren 定。

## 48. 第十三次独立审查与更正（P34b）

2026-10-10。按 Ren“aim a complete theory of becoming, and finish related work”继续。另一 agent（Claude Opus 5.5，未参与撰写）独立审查了 P32（§43）、P33（§44）、P33b（§45）与 P34（§46），以及 P35/P36 的两份草稿（[审查](BECOMING-P32-P34-REVIEW.md)，对象 `7f69f455` 与草稿 `D35.lean`、`D36.lean`）。它在仓库之外从前导重新编译核心闭包的 29 个模块，2028 条源声明（1263 项定理）的公理报告全空；闭包的 5650 个常量中依赖公理的只有 37 条编译器生成的 `injEq` 引理，都只依赖 `propext`，与回执所列相同；四个提交的回执、源哈希、保留产物与外围回执，1590 个引用哈希与 459 个证明绑定都对，各阶段的计数与章节一致。数学全部接受，没有错误的 Lean 陈述；两份草稿的定理也都对，其 70 条声明不依赖公理。它写了 42 条探针声明（34 项定理）与 8 个 `example`，生成的 78 个常量都不依赖公理；提出九项（U1–U9）：一项过强（U1，P34 的标题），一项出处错误（U2），一项说明与缺少的反例（U3），草稿的三项（U4–U6），P34 的说明（U7），中英对应（U8）与记账（U9）。另一会话的 W1–W5（`1f6f375f`）在审查期间提交，不在对象之内。本节逐项处理，把审查的探针移入核心；草稿按 U4–U6 重构，作为 P35 提交（§49）。草稿、探针与审计输出保存为[审查证据](development/becoming-p32-p34-review-probes/README.md)，不是登记的成果。成果记录：修订 [whole-law-of-counting](../../../../theories/becoming/results/records/whole-law-of-counting.md)、[census-balance-under-continuation](../../../../theories/becoming/results/records/census-balance-under-continuation.md)、[identity-across-steps](../../../../theories/becoming/results/records/identity-across-steps.md)；引用移动了的引理的记录随之更新声明的位置。

```text
Result(s): 更正 whole-law-of-counting（U1–U3、U7、U9）、census-balance-under-continuation（U2）、identity-across-steps（U8）；
           没有新的成果记录（P35 的记录见 §49）
Delta: Dependence：开头新增“算术”一节：le_dest（自 Change）、le_of_add_le_add_right 与 add_right_cancel（自 Horizon）、
       add_sub_turn、add_sub_of_le。Flow：le_total_of_mem（自 Dissipation）。Population：Balance、Tally.balance、
       Tally.ceasing_le、tally_iff、balance_not_tally、Tally.congr、tally_iff_counted；节标题与说明改为“计数表是计数的全部规律”。
       Premises：World.tended_not_binds、World.binds_arising、World.binds_adds；tendedQueue_premised 与 premised_counting 的说明。
       Identity：“步后列出的多于步前”。登记：形如 Lean 名称的别名须在所绑定回执列出的声明中
Supplied premises / correspondence: 不变
Evidence: 合并检查器回执 20261010T075031.720357Z（与 §49 同一次检查）；外围桥接重跑 20261010T075308.552033Z；实例检查；make research-test
Boundary: 不含伦理结论；不替 Ren 选择任何读法；新名称是建议
Integration: §46 与英文 P34 的就地更正；章节第 3、4 条、状态表、进一步的证明、§9 与术语表；README 与根模块的说明
```

### 48.1 逐项处理

| 项 | 审查所见 | 处理 |
|---|---|---|
| U1 | P34 的标题“平衡是计数的全部规律”过强：仓库中普查的平衡指 `Listed.across` 的等式，P34 证明的计数表严格强于它；每个列出都满足“跨一步不再成立的不多于步前所列的”，等式不给出它（审查的 `tally_iff`、`balance_not_tally`、`ceasing_bound_law`） | 移入核心：`Balance`（等式）、`Tally.balance`、`Tally.ceasing_le`、`tally_iff`（计数表恰是平衡加上这一界）与 `balance_not_tally`（Population）。各处改为“计数表是计数的全部规律”：章节第 4 条、状态表、进一步的证明、§9 的 Population 一行与术语表，记录的标题与断言，§46 与英文 P34 段落（就地更正并注明），README，根模块，Population 的模块说明、节标题与 `counting_laws` 的说明。复现定律只用等式，不变。提交标题与历史保留原样 |
| U2 | whole-law-of-counting 与 census-balance-under-continuation 的对应说活动的计数“不是 Ren 提议中的‘生成的’‘退化的’”；名称经 Ren 确认，所指没有；第十次审查 O8 之后其余各处都把这一问题留给 Ren | 两份记录都改为 census-balance 的标准句：引 Ren 的反问句，若取不重叠则不是其所指，并标明这是 AI 的推论；加历史 |
| U3 | `tendedQueue_premised` 的说明说耗散“只在什么都不交换处起约束”；按 `World.Binds`，队首照管的队列中耗散从不起约束，活动需要支持与有界传递也不起约束；“八个前提所加的只有这一条”的范围包括前提空成立的世界 | 说明改正；移入核心：`World.tended_not_binds`（三者在其中空成立，所以不是每个前提都起约束；审查的探针加上有界传递）、`World.binds_arising`（每个前提都起约束时，每个普查都计到某个生起）与 `World.binds_adds`（八个前提之下这不是规律）。章节第 3 条、Premises 的模块说明、§46 与记录的局限写明 |
| U4 | 草稿的两条规律是一条：从某步起的结算就是从第 0 步起的结算（审查的 `settles_zero`、`same_laws`）；`Closing` 的 T、T 之前与地的交换、`spare` 中的条件与 `early` 的情形都不需要 | 规律只陈述一次，以从第 0 步起的变化界（`∃ B, ChangeBound 0 B n c a`）；`ChangeBound.from_zero`、`changeBound_iff_zero` 与 `World.enclosed_iff_finite_counting` 移入核心；实现的世界去掉 T、地关系项与 T 之前的交换，关系项是自然数（`EnclosedQueue`、`World.enclosedQueue`）；T 只留在定量的 `World.enclosure_bounds_change` 中。见 §49 |
| U5 | 草稿说变化“不复现”，是对的；更强的形式（有一步之后不再变化）蕴含 LPO，对计数与满足八个前提的有限世界都如此（审查的 `lpo_of_settlesEnds`、`lpo_of_finiteEnds`） | 移入核心：`Swap`（在布尔序列的第一个真处替换一个成员）、`ChangeBound.lpo_of_ends` 与 `World.lpo_of_finite_ends`。正文说“不复现”“在变化界之内”，不说“停止” |
| U6 | 算术引理分散在 Horizon、Joint、Change、RelationalRenewal 与草稿中；草稿的 `le_sub_of_add_le` 与 `fin_eq` 重复已有的；`since`、`below` 太一般，`Settles` 读作“在某步归于静止”，`Closing` 与 `Closed` 近乎同名 | 自然数的算术集中在 Dependence 开头的一节（Change、Population 与 Horizon 都在其上）：`le_dest`、`le_of_add_le_add_right`、`add_right_cancel` 移入，`add_sub_turn` 与 `add_sub_of_le` 新增，都没有公理；`le_total_of_mem` 从 Dissipation 移入 Flow 的总量一节；复用 `RelationalRenewal.le_sub_from_add` 与 `Fin.eq_of_val_eq`。名称改为 `occurrences`、`ChangeBound`、`placesBelow`、`EnclosedQueue`、`FiniteQueue`，按 Ren 2026-10-10 的命名准则选定（[来源](../../../../sources/15-codex-theory-conversations/2026-10-10-zero-axiom-part-and-names.md)）。`Tended.decideEq` 不再需要 |
| U7 | `Pointwise` 是公平的假设，也可以不用；§46 说“经典地每个性质都如此”不对；§46 与英文段落给出的保持形式的理由（避免带 `propext` 的消去律）不成立 | 移入核心：`Tally.congr` 与 `tally_iff_counted`（列出所能有的计数恰是计数表，不用 `Pointwise`）；§46 改为“有函数外延性时”，理由改为 U1 的 |
| U8 | 英文把 `forced_iff_more` 说成“步后立着的更多”；“立着”是理论的术语（水平为正），这里比的是列表的长短 | 改为 “more formations are listed after the step than before”：Identity 的两处说明、检查器的范围说明、identity-across-steps 的英文、研究与计划的英文 |
| U9 | 草稿落地时须更新的开放项；登记不检查别名 | 开放项随 P35 更新：章节进一步的证明、记录的局限与下一步、§46 的边界与反驳 2、5、英文 P34 段落。登记新增检查：形如 Lean 名称、命名空间在所绑定回执中的别名，须在那些回执列出的声明中（`tools/research/registry.py`，加测试）；现有的这样的别名全部通过 |

### 48.2 新的已检查声明

| 声明 | 内容 |
|---|---|
| `Balance`、`Tally.balance`、`Tally.ceasing_le` | 平衡的等式；计数表满足它，且跨一步不再成立的不多于步前所列的 |
| `tally_iff`、`balance_not_tally` | 计数表恰是平衡加上这一界；零个在列、每步一个不再成立一个开始成立满足平衡而不是计数表 |
| `Tally.congr`、`tally_iff_counted` | 计数表尊重每步的值；列出所能有的计数恰是计数表 |
| `World.tended_not_binds` | 队首照管的队列中耗散、活动需要支持与有界传递空成立，不是每个前提都起约束 |
| `World.binds_arising`、`World.binds_adds` | 每个前提都起约束的世界中每个普查都计到某个生起；八个前提之下这不是计数的规律 |
| `le_dest`、`le_of_add_le_add_right`、`add_right_cancel`、`add_sub_turn`、`add_sub_of_le` | Dependence 开头的算术，公理报告为空（前导中的对应引理带 `propext`） |

### 48.3 作者反审

*反驳 1：把标题改成“计数表”只是换词。* 不是：两种说法的数学内容不同。“平衡是全部规律”按仓库里平衡的意思是假的（`balance_not_tally`）；“计数表是全部规律”是 P34 证明的。差别恰是一条规律：跨一步不再成立的不多于步前所列的。复现定律只用等式，所以仍然对。

*反驳 2：`tended_not_binds` 使 `premised_counting` 失去意义。* 不：它是对满足八个前提的全部世界的刻画，前提空成立的世界也在其中；`binds_adds` 说明，只取每个前提都起约束的世界，规律会更多（至少有一个生起）。两种范围回答不同的问题；后者的全部规律本节没有陈述。

*反驳 3：把算术引理移到 Dependence 打乱了模块的主题。* 这些引理是核心各层共用的自然数事实；Dependence 在 Change、Population 与 Horizon 的导入链上都在其下，Frame、Inquiry 与 Renewal 不需要它们。集中一处避免了重复；名称不变，只是位置变了，引用它们的记录随之更新声明的位置。

**边界。** 无伦理谓词；Ren 的选择保持开放；本节的新名称是 AI 按 Ren 的命名准则（[来源](../../../../sources/15-codex-theory-conversations/2026-10-10-zero-axiom-part-and-names.md)）所选。本节尚未经独立审查。

## 49. 被围住时与有限世界中计数的规律（P35）

2026-10-10。按 Ren“aim a complete theory of becoming, and finish related work”继续，作为计划 P35。P34 给出了计数的全部规律与全部八个前提之下的规律，把有限世界中与被围住时的计数规律列为下一步（§46 的边界、反驳 2 与 5）。静止定理（P26）说被围住时生起与止息都不再复现，但没有说计数还剩多少自由。本节回答：被围住为变化定下界；八个前提之下，从某步起每步被围住时与有限世界中计数的规律相同，恰是计数表、没有关系项活跃的一步上没有生起与从第 0 步起的变化界。两份草稿经第十三次审查后按 U4–U6 重构（§48）。成果记录：新增 [counting-under-enclosure](../../../../theories/becoming/results/records/counting-under-enclosure.md)。

```text
Result(s): 复用 whole-law-of-counting（Tally、Queue、Pointwise、World.CountsObey、counting_binds_jointly、Tended.front、
           Tended.occupied）、continued-change-needs-openness（Flow.standing_never_rises、Flow.change_lowers、standingCensus、
           aroundStanding_not_not、World.Finite.enclosed）、ceasing-needs-arising（rises_of_arises、falls_of_ceases）、
           map-of-premises（World.Premised.of、World.Binds）、no-finite-part-bears-taking（Flow.ClosedAt、Flow.Dissipative、
           total_le_of_support）；新增 counting-under-enclosure
Delta: Population：Queue.reached、occurrences（_before、_succ、_mono、_le、_zero_le）、falls_by_occurrences、ChangeBound（not_recurring、
       from_zero、joins、reach）、changeBound_iff_zero、Swap、ChangeBound.lpo_of_ends。Openness：World.length_le_stock、
       World.enclosure_bounds_change、EnclosedQueue（store、place、level、web、flow、span 与其引理）、World.enclosedQueue 与其前提、
       World.enclosed_counting、placesBelow、FiniteQueue、World.finiteQueue 与其前提、World.finite_counting、
       World.enclosed_iff_finite_counting、World.replaced、World.finite_dissipation_binds、World.replaced_attains、
       World.lpo_of_finite_ends
Supplied premises / correspondence: 同 P34：列出与可判定，逐点；被围住与有限是世界的条件，不是公理
Evidence: 合并检查器回执 20261010T075031.720357Z（1356 项定理、2161 项声明审计、核心闭包 31 个模块、包 29 个模块，全部源声明公理报告为空）；
          外围桥接重跑 20261010T075308.552033Z；实例检查
Boundary: 只说活动的计数；变化界以被围住时所立者的总水平为界，是可以达到的界，不是每个世界的值；每个前提都起约束时的全部规律没有陈述；
          不评价生起、止息或静止；名称由 Ren 定
Integration: 计划 P35；关闭 whole-law-of-counting 的下一步“有限世界中与被围住时计数的规律”；静止定理的定量形式
```

| 声明 | 内容 |
|---|---|
| `occurrences`、`ChangeBound` | 自第 T 步以来某量为正的步数；从第 T 步起，列出的数目连同自 T 以来有不再成立或开始成立的步不多于 B |
| `ChangeBound.not_recurring` | 变化界之内变化不复现 |
| `ChangeBound.from_zero`、`changeBound_iff_zero` | 从第 T 步起的变化界是从第 0 步起的变化界，大出 T 与 T 之前的计数 |
| `Queue.reached`、`ChangeBound.joins`、`ChangeBound.reach` | 离开的连同在队中的是起初的连同此后加入的；从第 0 步起在变化界 B 之内的计数表，其队列从不超过第 B + B·B 个成员 |
| `Swap`、`ChangeBound.lpo_of_ends` | 在布尔序列的第一个真处替换一个成员，变化界为二；若每个从第 0 步起在变化界之内的计数表都有一步之后不再变化，LPO 成立 |
| `World.enclosure_bounds_change` | 有普查、关系项都体现、平衡且耗散的世界中，从第 T 步起每步被围住时，计数从 T 起在第 T 步所立者的总水平之内 |
| `EnclosedQueue`、`World.enclosedQueue`、`World.enclosedQueue_premised`、`World.enclosedQueue_enclosed` | 被围住的队列：成员恰在队中时立着、活跃，队首立着变化界超出成员数的部分，队首只在队内交换，每有成员加入或离开的一步所立者下降一；每步都被围住，从第 0 步起在变化界之内且没有成员加入空队时满足全部八个前提 |
| `World.enclosed_counting` | 八个前提之下、从某步起每步被围住时，计数的规律恰是计数表、没有关系项活跃的一步上没有生起与从第 0 步起的变化界 |
| `placesBelow`、`FiniteQueue`、`World.finiteQueue`、`World.finiteQueue_premised` | 同一队列放在其成员曾占的有限多个位置上，是满足八个前提的有限世界 |
| `World.finite_counting`、`World.enclosed_iff_finite_counting` | 有限世界中计数的规律相同；所以从某步起被围住的世界与有限世界有相同的计数规律 |
| `World.replaced`、`World.finite_dissipation_binds`、`World.replaced_attains` | 第 0 步替换一个成员：队首从全部位置的封闭家族取用两个单位，耗散起约束；第 0 步所立者总共为二，此后一个成员连同一步变化恰为二，达到变化界 |
| `World.lpo_of_finite_ends` | 若每个满足八个前提、活动可判定的有限世界都有一步之后不再生起，LPO 成立 |

**解读。**

- **被围住定下变化界。** 静止定理只说变化不再复现。`enclosure_bounds_change` 说多少：被围住的步上所立者的总水平不升，每有生起或止息的一步至少降一（体现的关系项生起即开始立着，止息即不再立着，`Flow.change_lowers`）；活跃的关系项都体现、都立着，所以它们的数目不多于总水平。两者相加，此后任一步活跃者连同自被围住以来有变化的步，不多于被围住时的总水平。界数的是有变化的步，不是事件：同一步上可以有许多生起与止息。
- **变化界是全部。** 反过来，每个从第 0 步起在变化界之内、没有成员加入空队的计数表，都由一个满足八个前提、每步都被围住的世界实现：被围住的队列。它的所立者恰是队中的成员，每个立着一，队首另立着变化界超出成员数的部分；每有成员加入或离开的一步，所立者的总水平降一，队首取用的多于给予的，所以耗散成立；没有变化的步上什么都不动。
- **有限世界相同。** 有限世界的每一步都被围住（`World.Finite.enclosed`），所以它的计数在变化界之内；反过来，被围住的队列从不超过第 B + B·B 个成员（`ChangeBound.reach`），放在这些位置上它就是有限世界。所以在八个前提之下，有限世界、从某步起被围住的世界与每步都被围住的世界有相同的计数规律（`enclosed_iff_finite_counting`）。
- **不复现与终结之步。** 变化界之内变化不复现；但对每个这样的计数构造性地得到“有一步之后不再变化”是不行的：否则 LPO 成立（`ChangeBound.lpo_of_ends`、`World.lpo_of_finite_ends`）。这与 P33b 对网与列表的结果同类。
- **一元的读法（AI 论证）。** 变化界不是外加的限制：它就是被围住时所立者总水平的逐步耗散在计数上的样子。在被围住的展开中，每一次形成或消解都耗去关系中立着的一些东西；能不息地变化的是开放的展开（P25）。

**作者反审。**

*反驳 1：被围住的队列太特殊。* 同 §46 反驳 1：任何更多的规律都须在满足条件的所有世界中成立，包括这个队列；它不满足，那就不是规律。

*反驳 2：变化界的界不精确。* 对每个世界，界是被围住时所立者的总水平，并且可以用尽（`replaced_attains`）；但它是界，不是每个世界的值。规律说的是计数能是什么，不是某个世界的计数是什么。

*反驳 3：活动需要支持与有界传递在被围住的队列中空成立。* 是，与 P34 的见证相同；耗散在其中起约束（`finite_dissipation_binds`）。每个前提都起约束时的全部计数规律没有陈述；它至少多出一个生起（`World.binds_arising`）。

*反驳 4：“有限世界相同”抹去了有限的意义。* 在计数上，有限的意义正是一个变化界：数目与变化的步一起有界。从某步起被围住的世界在计数上无法与有限世界区分；区别在别处，例如这样的世界中曾经立着或活跃的不是无界多（`World.rest_few`），而不是有一个列表列出全部。

**边界。** 无伦理谓词，不评价生起、止息或静止；只对离散步与每步有限的活动陈述；变化界以被围住时所立者的总水平为界；水平与依存的计数在前提之下、每个前提都起约束时的全部计数规律没有陈述；名称（occurrences、ChangeBound、EnclosedQueue、enclosedQueue、FiniteQueue、finiteQueue、placesBelow、Swap、replaced）是 AI 按 Ren 的命名准则（[来源](../../../../sources/15-codex-theory-conversations/2026-10-10-zero-axiom-part-and-names.md)）所选：零公理部分取描述抽象动力学的形式词，草稿中的“预算”（budget）是金融的词，提交前改为“变化界”（`ChangeBound`）与“被围住的队列”（`EnclosedQueue`）。本节尚未经独立审查。

## 50. 见证改名（P36）

2026-10-10。Ren 指示：先求不用公理的最强陈述，作为第一部分；再加一条公理，作为第二部分。Ren 同时把名称交给 AI，标准有四条：
- 最精确的词；
- 零公理部分用描述抽象动力学的形式词；
- 偏好科学与系统的词；
- 社会与金融的词不作首选。

见[来源](../../../../sources/15-codex-theory-conversations/2026-10-10-zero-axiom-part-and-names.md)。P35 已按这些标准命名它新增的声明。本节把核心中其余见证的名称改为描述其动力学的名称，作为计划 P36（[计划 §10](BECOMING-UNIFICATION-PLAN.md#10-第一部分与第二部分--part-i-and-part-ii)，对照表在那里）。

```text
Result(s): 不新增结果；改名所及的记录在其历史中注明
Delta: 只改名：见证、关系项、世界与以其命名的声明；陈述、证明与计数不变
Supplied premises / correspondence: 无新增
Evidence: 合并检查器回执 20261010T083222.285294Z（1356 项定理、2161 项声明审计，全部源声明公理报告为空）；外围回执 20261010T084107.973758Z
Boundary: 名称是 AI 按 Ren 的命名标准所选，读法仍由 Ren 选择；第二部分的词汇等第二部分的公理定下后再看；
          外围定律族与命名空间 Generative 保留原名
Integration: 计划 P36；其后 P36b（生成不译作 generative）、P37（区域）、P38（第一部分的总陈述与章节重组）
```

**原则。**

- **名称说所述的动力学。** 举例：
  - `Shuttle`：两侧来回传递一个单位；
  - `Throughput`：同一传递每步烧掉新燃料；
  - `Lossless`：取走又还回，什么都不损失；
  - `OpenQueue`：队首与无界的地交换的队列，与 P35 的 `EnclosedQueue` 相对；
  - `Renewable`：每步更新一个单位的条件，它的两次运行是在更新之内取用（`withinRenewal`）与超出更新取用（`beyondRenewal`）。
- **换掉社会、金融与诗化的词，保留科学的名称。**
  - 换掉的社会与金融的词：递交、花费、照管、公地、共享与取胜、陌生者、人群、总体化者、照管者、礼物、继承者。
  - 换掉的诗化的词：太阳、黎明、黄昏、引火、余烬、花园、开花。
  - 科学与生态学的名称保留：孵化、互利、捕食、世代、种子库、啃食、饥荒、级联、潮汐、更替、世系、接续、休眠等。
- **`Totalizer` 改为 `Clearing`。** `Totalizer` 来自 Ren 关于 totalizing 的说法，换成 `Clearing` 也合于旧规：形式部分不以 Ren 的用语命名。它的定理 `careful` 改为 `undermines_within_renewal`，名字说的就是它所陈述的：在更新之内取用自身资源的形成，仍侵蚀栖居者。
- **历史与证据保留原名。** §1–§49、旧回执、审查文件与探针都保留原名，因为它们记载的是那些回执检查时的状态。读它们时，按对照表从旧名读到新名。

**检查。** 改名后的核心先在暂存区编译，再由合并检查器重查（回执 20261010T083222.285294Z），外围桥接对这个核心重查（20261010T084107.973758Z）。定理与声明审计的数目与 P35 相同。本节尚未经独立审查。

## 51. 接下来能形成什么：接纳、部分与区域（P37）

2026-10-10。Ren 指示“let's aim for a first, then try to archive b”，并确认两项读法，见[来源](../../../../sources/15-codex-theory-conversations/2026-10-10-axiom-route-levels-and-possibilities.md)：
- 可能性是从现有者接下来能形成什么；一个将来保留另一个所有的并有所增加时更多；一个形成的贡献是有它与无它的差；
- 整体从不是任何中心对它的模型；包含不许可强加的终结，许可它需要权衡的度量，那是另一个前提。

Ren 的确认是：“yes to both readings, go ahead with Part I.”。

此前 Ren 写道，生成的是“its existence creates more possibilities of becoming - more future, not less”，又写道“"not harm" - this is a phase transition with a clear boundary, not some "outside will or belief"”。Ren 还给出层级的次序：整体，较弱的是所在的系统，然后是自身。见[来源](../../../../sources/15-codex-theory-conversations/2026-10-10-centers-within-the-dynamics.md)。

本节是计划 P37（[计划 §10](BECOMING-UNIFICATION-PLAN.md#10-第一部分与第二部分--part-i-and-part-ii)），由本会话完成；分工经另一会话同意。它在核心中新增两个模块：
- `Becoming.Admission`，38 项定理；
- `Becoming.Regions`，18 项定理。

成果记录新增五项：
- [support-from-the-supported](../../../../theories/becoming/results/records/support-from-the-supported.md)
- [closing-needs-net-draw](../../../../theories/becoming/results/records/closing-needs-net-draw.md)
- [four-cases-of-a-part](../../../../theories/becoming/results/records/four-cases-of-a-part.md)
- [loss-beyond-a-region](../../../../theories/becoming/results/records/loss-beyond-a-region.md)
- [represented-boundary-against-dependence](../../../../theories/becoming/results/records/represented-boundary-against-dependence.md)

```text
Result(s): 复用 coming-and-ceasing-keep-pace（Web.supported_of）、rising-and-falling-in-one-exchange（Flow.Balances.rise_given）、
           more-needs-renewers（Flow.Balances、Flow.Acting、Web.Dependent、taken、given、total 的引理）、becoming-stepwise-reading
           （Web.RenewingAt、Kept、Participates、UnderminingAt、RenewingAt.not_undermining）、derived-extent-limits
           （Clearing、Clearing.undermines_within_renewal）、own-count-misses-joint-excess（excess_bounded、joint_excess_ends，
           作为已有的相界结果引用）；新增上列五项
Delta: Admission：GainsSupport、LosesSupport、Unloosened、Untightened 与 rises、falls；rise_given_by_supported、gains_from_supported、
       unsupported_stays、nothing_supported_stays；Restoring 的五个前提见证（Adapting、Inflow、Idle、Carried、Spontaneous）；
       Admits、Includes（refl、trans、not_exceeded）、Exceeds；withhold、partTaken、partGiven、WithheldLevels（unique）、
       Balances.withheld、supported_iff_within_margin、supported_of_net_give、admits_of_net_draw、closes_nothing、opens_nothing、
       changes_nothing；
       Inflow.withheld、Inflow.widens；Transfer（withheld、mixed）。Regions：AdmitsWithin、LosesBeyond、includes_iff_within_whole、
       narrow、not_losesBeyond_whole、not_losesBeyond、admitsWithin_self；RenewingOver、RenewingAt.over、RenewingOver.at、
       renewingAt_iff_over_all、RenewingOver.narrow、RenewingOver.keeps_own；Clearing.withheld、admitted_without、
       unsupported_with、narrows、loses_beyond、renewing_over_resource；Omitted.loses_own
Supplied premises / correspondence: 平衡、Acting、Dependent、要求不放松（吸收态）；部分是可判定的家族（part : F → Bool）；
       比较保持其余交换不变；离散的步与自然数的量；读法的对应是 AI 的，待 Ren
Evidence: 合并检查器回执 20261010T100351.523624Z（1412 项定理、2251 项声明审计、核心闭包 33 个模块、包 31 个模块，全部源声明
          公理报告为空，没有新的生成常量依赖公理）；外围回执 20261010T100610.366844Z
Boundary: 比较的是被接纳的形成，不比较更新能力与关系的丰富；只看接下来的一步；其余交换不随之调整；扣留后没有平衡的水平时
          无可比较（每个见证都给出扣留后的水平）；混合的部分不为包含定序；区域是陈述的参数；不含伦理谓词
Integration: 计划 P37；回答 §47 留下的“推出的范围达不到的”在可能性上的形式；给 P38 的第一部分总陈述提供区域；
             P39（第二部分）以 G0 为目标定理
```

| 声明 | 内容 |
|---|---|
| `Web.GainsSupport.rises`、`Web.LosesSupport.falls` | 要求不放松时只因所需条件上升而获得支持，要求不收紧时只因其下降而失去支持（经 `Web.supported_of`） |
| `Flow.rise_given_by_supported`、`Flow.gains_from_supported` | 平衡、Acting、Dependent 之下每次上升由被支持的形成给予，所以支持只从被支持者获得 |
| `Flow.unsupported_stays`、`Flow.nothing_supported_stays` | 家族中没有被支持者、要求不放松、只有成员给予成员所需时，没有成员再被支持；整体中什么都不再被支持或活跃 |
| `Restoring.*.restores` | 每项前提都必要：要求消解（Adapting）、家族之外的给予（Inflow）、不活跃的给予者（Idle）、不被支持的活跃给予者（Carried）、没有给予的上升（Spontaneous） |
| `Web.Admits`、`Web.Includes`、`Web.Exceeds` | 接纳；包含是预序；包含另一条的路径不被它超出 |
| `Flow.withhold`、`Flow.WithheldLevels.unique`、`Flow.Balances.withheld` | 扣留一个部分，扣留后的水平存在时唯一；每个水平加上该部分取走的，等于扣留后的水平加上该部分给予的 |
| `Flow.Balances.supported_iff_within_margin` | 相界精确：形成被支持，恰当在它所需的每个条件上，所需加上部分到此为止取走的，不多于扣留后的水平加上部分给予的，即部分的累计净汲取不超出余量 |
| `Flow.Balances.supported_of_net_give`、`admits_of_net_draw` | 关闭需要在所需条件上的净汲取，打开需要净给予 |
| `Flow.Balances.closes_nothing`、`opens_nothing`、`changes_nothing` | 每步给回不少于所取者不关闭，给予不多于所取者不打开，恰好给回者不改变 |
| `Restoring.Inflow.widens`、`Clearing.narrows`、`Transfer.mixed` | 扩大、缩小与混合的见证，各给出扣留后的水平 |
| `Web.AdmitsWithin.narrow`、`Web.LosesBeyond.narrow`、`Web.not_losesBeyond_whole`、`Web.AdmitsWithin.not_losesBeyond`、`Web.admitsWithin_self` | 区域越小，其外越多；整体之外什么都没有；单个形成之内成立的是它自身的接纳 |
| `Clearing.loses_beyond` | 清除者每步活跃且被支持，在它与来源之内不关闭任何东西，从第二步起在其外关闭栖居者 |
| `Web.RenewingOver`、`.at`、`.keeps_own`、`Clearing.renewing_over_resource`、`Omitted.loses_own` | 在条件区域上的更新：覆盖参与即该步的更新；覆盖所需且要求不收紧即保住自身支持，仍可侵蚀他者；遗漏所需可以经自身的汲取失去支持 |

**它回答了什么。**
- **可能性与三种区域。** 可能性读作接下来能形成什么，即每一步被水平接纳的形成。部分的贡献由有它与无它的比较给出，无它时保持其余交换不变，像 `Becoming.Joint` 的 but-for 检验保持动作不变。以包含比较，部分扩大、缩小、保持不变或混合。混合说明三种区域在包含之下不穷尽，给它定序需要度量，那是另一个前提。这与 Ren 确认的第二项读法一致：包含不许可强加的终结。
- **相界。** 关闭与不关闭之间的界由部分自身的净交换与他者所需的余量决定，不需要动力学之外的意志或信念。这个界是精确的（`supported_iff_within_margin`）：形成被支持，恰当部分在它所需的每个条件上的累计净汲取不超出扣留后的水平满足所需的余量。所以关闭一个能形成者，只经由在它所需条件上超出余量的净汲取（找出那个条件要用经典逻辑）；每步给回不少于所取的部分不关闭任何东西。已有的两个相界结果在 `Becoming.Continuation`：
  - 没有条件能被无限耗下去（`excess_bounded`）；
  - 使水平低于所需的联合超出，终结以其所需依存者（`joint_excess_ends`）。

  本节加上第三个：终结是吸收态（`unsupported_stays`）。
- **层级。** 我先前说过“只有不退化的动力学能无限延续”。这对部分不成立，`Clearing.loses_beyond` 就是对话中所说的搭便车者的反例：清除者在其依存之内一直延续，并在其外关闭栖居者。成立的是两个较窄的陈述：
  - 被持续耗下去的条件上，没有东西能无限延续；
  - 整体之外什么都没有，所以对整体，延续与不退化重合。

  区域越小，其外越多，这给出 Ren 的次序：整体、系统、自身，按判据的强弱排列，不加公理。
- **所表示的边界。** 一个中心的边界可以覆盖其所需而不覆盖其参与，于是保住自身而侵蚀他者；也可以遗漏其所需，于是经自身的汲取失去自身支持。只有覆盖其参与的边界给出该步的更新。

**作者反审。**
1. **接纳只看接下来的一步。** 可能性读作接下来能形成什么，经 Ren 确认；多步可达没有比较。
2. **反事实不让他者随之调整。** 扣留一个部分时其余交换照旧。他者因此过度取用时，扣留后没有平衡的水平，定理在那里空成立。所以每个见证都给出扣留后的水平，`WithheldLevels.unique` 保证它是唯一的那一条。
3. **只比较被接纳的形成。** Ren 也提到“renewal capacity, or richness of relations”，这里没有比较。
4. **吸收态需要要求不放松。** 形成通过消解其要求可以逃脱吸收态（`Adapting`）；这是转化，不是恢复。
5. **层级的定理大多是序的性质。** 实质在清除者的见证。“整体”是一个网中全部形成的区域，即所表示的整体；实际的整体从不完全被表示，这与 Ren 的第二项读法一致。
6. **所表示的边界只在一步上比较。** 多步的依存范围（供给其所需者的来源）没有进入比较。
7. **读法与名称是 AI 的。** 读法待 Ren；名称是 AI 按 Ren 的命名标准所选。
8. **两处用经典逻辑。** 把部分分为四种情形，以及从一个形成不被支持找出净汲取超出余量的那个条件，都用排中律；Lean 中证明的是两个方向的包含与精确的等价（`supported_iff_within_margin`），不是这两步。

**检查。** 核心先在暂存区对 4284d6ab 的核心编译，逐条审计：Admission 136 项声明、Regions 49 项，公理报告全部为空。合并检查器先对加入精确相界之前的版本（Admission 37 项定理）重查（回执 20261010T091630.066142Z，外围回执 20261010T092128.336807Z；两次运行都保留），加入 `supported_iff_within_margin` 之后再重查（回执 20261010T100351.523624Z），外围桥接对这个核心重查（20261010T100610.366844Z）。本节尚未经独立审查。

## 52. 每个前提选择之下计数的规律（P38）

2026-10-10。按 Ren“let's aim for the strongest claim without axiom, as the first part”（[来源](../../../../sources/15-codex-theory-conversations/2026-10-10-zero-axiom-part-and-names.md)）与“go ahead with Part I”（[来源](../../../../sources/15-codex-theory-conversations/2026-10-10-axiom-route-levels-and-possibilities.md)），作为计划 P38 中第一部分总陈述的“每个前提加了什么”。P34 与 P35 给出了计数的全部规律：缺平衡或缺体现的前提不约束计数，全部八个前提之下多出“没有关系项活跃的一步上没有生起”，被围住时再多出变化界。它们没有回答其余选择：八个前提的 256 个选择中，哪些约束计数、约束什么。本节给出完整的回答：不论有无被围住，计数的规律都只有几种，每种恰在一组可以写出的选择之下成立。成果记录：修订 [whole-law-of-counting](../../../../theories/becoming/results/records/whole-law-of-counting.md) 与 [counting-under-enclosure](../../../../theories/becoming/results/records/counting-under-enclosure.md)。

```text
Result(s): 复用 whole-law-of-counting（Tally、Queue、Pointwise、World.CountsObey、World.counting_binds_jointly、World.queue、
           World.embodiedQueue、World.openQueue）、counting-under-enclosure（ChangeBound、from_zero、World.enclosure_bounds_change、
           EnclosedQueue、World.enclosedQueue）、continued-change-needs-openness（Flow.standing_lowers）、map-of-premises（World.Premised）
Delta: Premises：World.taking_binds_counting、World.enclosed_binds_counting、World.Premise 与 Premise.Holds、World.Meets、
       World.BindsCounting、World.Premised.meets、OpenQueue.driven、World.drivenQueue 与 drivenQueue_holds、World.openQueue_holds
       （从 openQueue_premised 中分出）、World.queue_meets、embodiedQueue_meets、openQueue_meets、drivenQueue_meets、
       World.counting_under、World.counting_binds_iff。Openness：EnclosedQueue.empty_stays 与 idle 只要求该步的条件、
       World.enclosedQueue_taking 不再需要任何条件、World.enclosedQueue_dissipatesOn（逐步的耗散；enclosedQueue_dissipative
       由它得出）、EnclosedQueue.closing、World.closingQueue 与其平衡、closing_flows、closingQueue_enclosed、
       closingQueue_dissipative、World.BoundsChange、World.still_enclosed、World.enclosed_counting_under
Supplied premises / correspondence: 同 P34、P35：列出与可判定，逐点；被围住是世界的条件，不是公理；选择是到 Bool 的函数
Evidence: 合并检查器回执 20261010T101327.506085Z（1430 项定理、2280 项声明审计，全部源声明公理报告为空）；外围桥接重跑 20261010T102016.503705Z；实例检查
Boundary: 只说活动的计数；每个前提都起约束时的规律、有限世界中每个选择之下的规律、水平与依存的计数在前提之下没有陈述；
          不评价生起、止息或静止；名称按 Ren 的命名准则由 AI 选，读法由 Ren 定
Integration: 计划 P38（第一部分的总陈述：每个前提加了什么）；扩展 whole-law-of-counting 与 counting-under-enclosure
```

| 声明 | 内容 |
|---|---|
| `World.Premise`、`Premise.Holds`、`World.Meets` | 八个前提的名称；选择是到 Bool 的函数，世界满足它所选的每个前提 |
| `World.BindsCounting` | 选择约束计数：选中平衡与体现，并选中只有活跃者给予，或同时选中只有活跃者取用其所汲取的与耗散 |
| `World.taking_binds_counting` | 在平衡、只有活跃者取用、耗散与体现之下，普查中没有关系项活跃的一步上没有生起，不论谁给予 |
| `World.enclosed_binds_counting` | 在平衡、耗散与体现之下，被围住且没有关系项活跃的一步上没有生起，不论谁给予、谁取用 |
| `OpenQueue.driven`、`World.drivenQueue`、`World.drivenQueue_holds` | 由一个闲置的地关系项驱动的队列（P41b 注：应为不活跃的地关系项，它参与每一步的交换；见 §58 V6）：它给予每个加入者、从每个离开者取用，并在每步与每个地关系项各交换一个单位，所以没有家族封闭；满足除只有活跃者给予与只有活跃者取用外的全部前提 |
| `World.openQueue_holds` | 不论计数，开放的队列满足除只有活跃者给予与耗散外的全部前提：成员加入空队时队首闲置地给予 |
| `World.counting_under` | 在每个选择之下，计数的一个性质在满足它的每个世界的每个普查中成立，恰当它对每个计数表成立，且在选择约束计数时对每个没有关系项活跃的一步上没有生起的计数表成立 |
| `World.counting_binds_iff` | “没有关系项活跃的一步上没有生起”在一个选择之下是计数的规律，恰当这个选择约束计数 |
| `World.enclosedQueue_taking`、`World.enclosedQueue_dissipatesOn` | 被围住的队列不论计数都只在活跃时取用；它的耗散逐步成立，只要求该步没有成员加入空队、前后两步都在所立者之内 |
| `EnclosedQueue.closing`、`World.closingQueue`、`World.closingQueue_dissipative`、`World.closingQueue_enclosed` | 在第 T 步闭合的被围住的队列：T 之前每个关系项与队首各交换一个单位，所以没有家族封闭；从 T 起它就是被围住的队列，所立者多出 T；从 T 起有变化界、没有成员加入空队时它耗散 |
| `World.BoundsChange`、`World.enclosed_counting_under` | 选择约束变化：选中平衡、体现与耗散。从某步起每步被围住的世界中，在每个选择之下计数的规律是 `counting_under` 的规律，在选择约束变化时再加上：从某步起变化在一个界之内，且没有关系项活跃的一步上没有生起 |

**解读。**

- **两条路线。** P34 只给出一条：平衡、体现与只有活跃者给予。第二条不要求给予者活跃：没有关系项活跃的一步上，只有活跃者取用，所以什么都不被取用；被给予者的水平上升，体现使它在步后活跃，所以步后活跃者的列表是一个封闭的家族；耗散不许给予封闭家族而不取用，所以什么都没有被给予，没有东西生起。闲置的给予者可以在一个开放的展开中给予，却不能在一个封闭的家族中无偿给予。被围住的一步上连取用的前提也不需要：那一步本来就有封闭的家族，所立者的总水平为零，任何成员开始立着都会使它下降（`Flow.standing_lowers`）。
- **两种规律，256 个选择。** 每个选择之下计数的规律只有两种：计数表，或计数表加上没有关系项活跃的一步上没有生起。后者恰在选择约束计数时成立。其余每个选择之下，每个计数表都被实现：缺平衡由立着的队列，缺体现由不流动的队列，缺给予与取用两个前提由驱动的队列，缺给予与耗散由开放的队列。这四类覆盖了不约束计数的全部选择：选中平衡与体现而不约束计数，就是既缺只有活跃者给予，又缺取用或耗散中的一个。
- **被围住时多一种。** 从某步起每步被围住时，选中平衡、体现与耗散，计数还有一个界：从被围住起，活跃者连同有变化的步不多于那时所立者的总水平（P35），而且从那一步起没有关系项活跃的一步上没有生起。后一条在构造性的核心中须带着它的步陈述：变化界之内变化不复现（`ChangeBound.not_recurring`），但这本身不给出一步。见证是在第 T 步闭合的队列：T 之前与每个关系项交换，所以不被围住，可以任意生起；从 T 起就是 P35 的被围住的队列。
- **一元的读法（AI 论证）。** “没有关系项活跃的一步上没有生起”不是另加的规则，而是给予、取用、耗散与体现之间的关系在计数上的形状：在一个封闭的关系中，生起要从已经在场的东西中取得。它不需要给予者的活动，需要的是取用与封闭；被围住时连取用也不需要，因为封闭已经在那里。

**作者反审。**

*反驳 1：256 个选择是表示的产物。* 选择只是把已有的八个前提按“选中或不选中”排列；规律刻画的是每个排列下的世界。用 Bool 是为了在纯净核心中可判定地分情况，不加内容。

*反驳 2：普查与有界传递、活动需要支持不出现在条件中，像是被忽略了。* 它们对计数不起约束：普查由所给的普查本身满足；见证中没有依存，所以活动需要支持与有界传递空成立。这与 P34 的观察相同（`World.openQueue_not_binds`）。每个前提都起约束时的规律没有陈述，它至少多出一个生起（`World.binds_arising`）。

*反驳 3：驱动的队列与闭合的队列太特殊。* 同 §46 反驳 1：更多的规律须在满足条件的所有世界中成立，包括这些见证。

*反驳 4：有限世界呢？* P35 在全部八个前提之下证明了有限世界与被围住的世界计数规律相同。在其余选择之下，有限世界的规律没有陈述：这里的见证都有无限多个关系项。

**章节重组。** 章节在 §1 前加第一部分的说明，在 §5 后加第一部分的总陈述，在 §6 前加第二部分的说明；节标题不变，锚点保留。总陈述说三件事：对每个展开成立的（不加前提的规律与计数表），每个前提加了什么（前提的地图、本节的计数、静止与开放、依存与储备、部分与区域），动力学在何处不再决定（前提是否成立、终结之步、混合的部分、中心、意义）。第二部分的说明引 Ren 提议的公理与路线 (a)，并写明 G0 被证明之前仍是所采用的公理（P39）。组织与措辞是 AI 的。

**边界。** 无伦理谓词，不评价生起、止息或静止；只对离散步与每步有限的活动陈述；选择之下的规律只读于活动的普查；有限世界中每个选择之下的规律、每个前提都起约束时的规律、水平与依存的计数在前提之下没有陈述；名称（Premise、Meets、BindsCounting、BoundsChange、drivenQueue、closingQueue）是 AI 按 Ren 的命名准则所选：驱动（driven）与闭合（closing）是系统的词，分别说外来的强迫与在某步封闭的流。本节尚未经独立审查。

## 53. 一条公理推出什么（P39）

2026-10-10。Ren 提议第二部分的一条公理：“for anything, its continuation into the future has significance(doesn't have to be positive, we could argue as long as not harm), or continuation into the future needs to create more significance(being generative)”（[来源](../../../../sources/15-codex-theory-conversations/2026-10-10-wanting-continuation-one-axiom.md)）。Ren 选定路线：“let's aim for a first, then try to archive b”（[来源](../../../../sources/15-codex-theory-conversations/2026-10-10-axiom-route-levels-and-possibilities.md)）。在路线 (a) 下，G0 是由这条公理与第一部分推出的目标定理。

Ren 此后回答（[来源](../../../../sources/15-codex-theory-conversations/2026-10-10-centers-within-the-dynamics.md)）：
- 中心及其边界只存在于认知的结构与动力学中，也在同一系统之内形成，“so there isn't really who's continuation matters, which requires axiom”；
- “not harm”是“a phase transition with a clear boundary”。

所以本节不按 §47 的读法给每个想要之点放一个中心，而直接陈述 Ren 的原话。

本节是计划 P39（[计划 §10](BECOMING-UNIFICATION-PLAN.md#10-第一部分与第二部分--part-i-and-part-ii)），由本会话完成；分工经另一会话同意。它在核心中新增模块 `Becoming.Significance`，27 项定理。成果记录新增三项：
- [one-axiom-yields-g0](../../../../theories/becoming/results/records/one-axiom-yields-g0.md)
- [significance-retained-within-margin](../../../../theories/becoming/results/records/significance-retained-within-margin.md)
- [whole-first-and-bounded-centers](../../../../theories/becoming/results/records/whole-first-and-bounded-centers.md)

```text
Result(s): 复用 metaethical-core-characterization（Valuation、Significant、SelfGood、Seed、transmits、shares、Neutral、Within、
           G0、Extension、Comparison）、held-lives-g0-is-centering（被持有的生命上 G0 恰等于处处 S0 加 N_std，作为读法引用）、
           becoming-stepwise-reading（Web.valuation、Web.relations、UnderminingAt）、becoming-renewal-reading
           （Conditions.valuation）、closing-needs-net-draw（Admits、Includes、Exceeds、WithheldLevels、
           Balances.supported_iff_within_margin、opens_nothing）、four-cases-of-a-part（Restoring.Inflow.widens、
           Transfer.mixed）、loss-beyond-a-region（AdmitsWithin、AdmitsWithin.narrow、Clearing 的见证与 loses_beyond）、
           derived-extent-limits（Clearing，作为读法引用）；新增上列三项
Delta: Unrestricted、bounded、bounded_rival；Web.Retains（refl、trans、not_added、of_fewer、within）、Web.Adds、
       Includes.retains、Adds.exceeds、retains_iff_includes、adds_iff_exceeds、retains_agree、retains_bounded_iff；
       Flow.Balances.retains_iff_within_margin、loses_iff_beyond_margin、adds_iff_within_margin；
       Valuation.premises_of_unrestricted、Web.significant_of_unrestricted、Conditions.significant_of_unrestricted、
       Web.paths、Web.paths_g0_comparison、Web.significance_undetermined；Clearing.admitted_all_without、free_rider_loses、
       dependenceRegion、centers_disagree；Transfer.unordered；Restoring.Inflow.retains_adds；
       Preemption（flow、web、drawerPart、withheld、not_undermining_yet_loses）
Supplied premises / correspondence: 公理 Unrestricted 是定理的假设，不被证明；主张的意义读作某形成在某步之延续的意义
       （formation、step、reads）；平衡与扣留后的水平（每个见证给出它）；离散的步、自然数的量、可判定的部分；
       读法与名称是 AI 的，待 Ren
Evidence: 合并检查器回执 20261010T110824.890630Z（1457 项定理、2316 项声明审计、核心闭包 34 个模块、包 32 个模块，全部源声明公理报告
          为空，没有新的生成常量依赖公理）；外围回执 20261010T111624.656993Z
Boundary: G0 在主张层面是公理的直接推论；A、L、J1–J4 仍是前提；C 只在水平路径上推出；为混合部分定序的度量、形成个体化
          的层次、G0 的 living 指哪种读法、公理的规范根据都不推出；只比较被接纳的形成，每一步
Integration: 计划 P39（第二部分，路线 (a)）；G0 成为这条公理的定理，Ren 接受之前仍是所采用的公理；给 P40（路线 (b)）
             留下以依存为界的中心容许搭便车者（Clearing.centers_disagree）
```

| 声明 | 内容 |
|---|---|
| `Unrestricted`、`bounded`、`bounded_rival` | 公理：从每个立场，任何东西在每一步的延续都有意义，即延续之意义的边界中立；以区域为界的意义是在区域之内接受同一规则，有形成在某个立场的区域之外时不是公理 |
| `Web.Retains`、`Web.Adds`、`Retains.refl`、`Retains.trans`、`Retains.not_added` | 从一个立场，一条水平路径保留另一条上的有意义者，是指它接纳另一条所接纳的每个有意义的延续；增加，是指它接纳一个另一条不接纳的。保留是预序；保留另一条者不被它增加，所以不终结其中任何有意义者 |
| `Web.Includes.retains`、`Web.Adds.exceeds`、`Web.retains_iff_includes`、`Web.adds_iff_exceeds`、`Web.retains_agree` | 包含总保留，增加总超出；公理之下保留就是包含、增加就是超出，从每个立场都一样 |
| `Flow.Balances.retains_iff_within_margin`、`loses_iff_beyond_margin`、`adds_iff_within_margin` | “不损”的精确界：有部分的水平保留无它时的有意义者，恰当在无它时被接纳的每个有意义的延续所需的每个条件上，部分的累计净汲取不超出余量；失去恰在超出余量之处，增加恰在净交换把无它时不被接纳的形成带入余量之处 |
| `Valuation.premises_of_unrestricted` | 在主张的意义即某形成在某步之延续的意义的每种读法上，公理给出 G0、处处 S0、N_rel、N_std 与（有活者时的）种子，不用连通 |
| `Web.significant_of_unrestricted`、`Conditions.significant_of_unrestricted` | 逐步读法、关系层读法与整段读法都是这样的读法 |
| `Web.paths`、`Web.paths_g0_comparison` | 水平路径的框架：主张是某步的形成，在路径上被接纳即实现，没有步。公理之下，对 living 的每种读法 G0 成立，正面意义读作从每个立场都有意义；C 也成立，“更好”读作保留且增加有意义者 |
| `Web.significance_undetermined` | 没有任何东西有意义时，每条水平路径保留每一条，没有一条增加，逐步读法上的 G0 在任何活的事件上不成立；一切都有意义时 G0 成立 |
| `Web.Retains.of_fewer`、`Web.retains_bounded_iff`、`Web.Retains.within` | 有意义者越少，保留的越多；以区域为界的意义保留的是区域之内被接纳的；公理之下在整体中保留的在每个区域内保留 |
| `Clearing.admitted_all_without`、`Clearing.free_rider_loses` | 无清除者的部分时，每个形成每步都被接纳。公理之下从每个立场，这个部分失去栖居者；无它的水平保留有它的有意义者；清除者每步被支持，无它时也被接纳，所以扣留它不终结任何东西 |
| `Clearing.dependenceRegion`、`Clearing.centers_disagree` | 让每个形成的意义止于其依存所及：从清除者的立场，部分在每一步保留有意义者；从栖居者的立场，它失去栖居者 |
| `Transfer.unordered`、`Restoring.Inflow.retains_adds` | 公理之下，传送者的部分不被定序：两条路径各自增加对方缺少的；给予者的部分保留并增加 |
| `Preemption.flow`、`web`、`drawerPart`、`withheld`、`not_undermining_yet_loses` | 汲取者在第零步、任何依存形成之前取走条件唯一的单位。流平衡，只有活跃者给予与取用，活动需要支持，它的事件活跃且不侵蚀。但一个从第一步起需要该条件的形成，无此部分时每步被接纳，有此部分时第一步起每步不被支持；无此部分的水平包含有它的水平，公理之下部分失去一个有意义的延续 |

**它回答了什么。**
- **G0 是公理的直接推论。** 公理比 G0 强：它对每个形成、每一步、每个立场成立，G0 只要求活的主张从每个立场有意义。所以在主张的意义即延续之意义的读法上，G0 是公理限于活的主张。前提卡上的种子、S0、N_rel 与 N_std 由它给出；C 在水平路径上给出。A、L 与 J1–J4 仍是前提。这一步本身不深，实质在下面几项：它们经第一部分给出“不损”与“生成”的精确形式。
- **“不损”的相界。** Ren 说“not harm”是有清楚边界的相变。公理之下，保留就是包含，所以“不损”就是 P37 的相界：在每个有意义的延续所需的条件上，部分的净汲取不超出余量（`retains_iff_within_margin`）。界由部分自身的净交换与他者所需的余量定出，不需要动力学之外的意志或信念。增加（Ren 的“create more significance”）就是超出：部分的净交换把一个无它时不能形成的形成带入余量。所以 Ren 的强式是弱式之下的生成情形，不需要第二条公理。
- **尚未形成者也算。** 逐步读法（[becoming-stepwise-reading](../../../../theories/becoming/results/records/becoming-stepwise-reading.md)）只计已被满足的依存：一个事件活跃且不侵蚀，就是活的；侵蚀是在某步汲取一个条件，使它在步后既低于依存于它者当前的所需，又低于该依存曾被满足的所需。`Preemption` 表明这与保留不同。汲取者在任何依存形成之前取走条件，它不侵蚀任何东西，却使一个以后需要该条件的形成每步都不能形成；公理之下这是失去一个有意义的延续。G0 的 `living` 指哪种读法是 Ren 的选择；这里只证明两者不同。
- **整体优先。** 以区域为界的意义只看区域之内。公理之下，在整体中保留的在每个区域内都保留（`Retains.within`），反过来不成立。`Clearing.centers_disagree` 是反例：每个形成的意义止于其依存时，清除者从自己的立场保留一切，栖居者从自己的立场失去自身。公理之下这个部分从每个立场都失去栖居者，而扣留它不终结任何东西（`free_rider_loses`）。这给出 Ren 的次序：整体、所在的系统、自身，作为判断完整性的次序。Ren 说“not saying this is what life does”，这里也不说生命实际怎样做。
- **公理是需要的。** 第一部分没有一条定理提到意义；没有任何东西有意义时，什么都不被定序（`significance_undetermined`）。以区域为界的意义也是被给出的：Ren 说自身“can not justify itself without some sort of "belief"”。没有这条公理，动力学不决定意义。

**作者反审。**
1. **G0 在主张层面是直接的。** `premises_of_unrestricted` 的证明只有几行：公理对每个形成、每一步、每个立场都给出意义，G0 只取其中活的。所以“G0 被推出”不应读作深的定理。记录如实写明这一点；深的部分是保留、相界与先占，它们用到第一部分（P37 的精确相界）。
2. **`reads` 是对应，不是证明。** 主张的意义读作某形成在某步之延续的意义，由 `formation`、`step`、`reads` 给出。逐步读法、关系层读法与整段读法满足它；不满足它的读法上，定理不说什么。
3. **C 只在水平路径上推出。** `Web.paths` 是一个没有步的框架：主张是某步的形成，在路径上被接纳即实现。C 在“更好”读作保留且增加时成立；在一般的框架上 C 仍是前提。
4. **不分等级。** 意义是命题，不是量，所以混合的部分（`Transfer.unordered`）不被定序；定序需要度量，那是另一个前提。Ren 也说意义“doesn't have to be positive”：这里的“不损”是比较，不是正面的价值。
5. **个体化的层次。** 什么算一个形成（成员或谱系）决定什么算失去。见证中形成是给定的，层次没有推出。
6. **先占依赖“以后需要”的表示。** `Preemption` 中形成 `false` 从第一步起需要条件，这是表示的选择。它说明保留计入仍能形成者，逐步读法不计入；不说明先占在每个模型中都失去什么。
7. **以依存为界的中心是一个选择。** `Clearing.dependenceRegion` 让清除者的区域是它沿依存所及的形成（含来源），栖居者与来源只含自身。它说明这样的中心彼此分歧并容许搭便车者，这正是路线 (b) 须面对的。
8. **读法与名称是 AI 的。** `Unrestricted`、`Retains`、`Adds`、`bounded`、`Preemption` 是 AI 按 Ren 的命名准则所选：不受限、保留、增加、有界与先占都是形式与系统的词。读法待 Ren。

**检查。**
- 模块先在暂存区对 P37 的核心编译（P38 不影响它的导入），逐条审计全部 71 项声明（含 Lean 生成的辅助声明），公理报告全部为空。
- 合并检查器对加入模块的包检查三次，三次运行都保留，每次都通过：
  - 第一次是回执 20261010T104700.459715Z。之后只改了模块文档中的三处措辞：Ren 对中心的回答的转述、“positive”一句（Ren 说意义“doesn't have to be positive”）、立场索引的读法。
  - 第二次是回执 20261010T105720.952257Z。之后只改了根模块文档中的一处：G0 成立的范围写明为逐步、关系层与整段读法。
  - 第三次是回执 20261010T110824.890630Z，为本节的证据。
- 外围检查有两次运行在上述文档修改前中止，没有回执。
- 外围桥接对这个核心重查（20261010T111624.656993Z）。
- 本节尚未经独立审查。

## 54. 有限世界中每个选择之下计数的规律（P38b）

2026-10-10。按 Ren“let's aim for the strongest claim without axiom, as the first part”（[来源](../../../../sources/15-codex-theory-conversations/2026-10-10-zero-axiom-part-and-names.md)），补全第一部分总陈述中“每个前提加了什么”在有限世界中的部分。§52 给出了每个前提选择之下计数的规律，以及从某步起被围住时多出的变化界；其见证都有无限多个关系项，有限世界中每个选择之下的规律没有陈述（§52 反驳 4）。P35 只在全部八个前提之下证明有限世界与被围住的世界计数规律相同，第一部分的总陈述却在每个选择的语境中写“有限世界的计数规律与此相同”，范围不准确。本节给出有限世界中每个选择之下的完整规律，并给出两类世界恰在何时规律相同。成果记录：修订 [counting-under-enclosure](../../../../theories/becoming/results/records/counting-under-enclosure.md) 与 [whole-law-of-counting](../../../../theories/becoming/results/records/whole-law-of-counting.md)。

```text
Result(s): 复用 counting-under-enclosure（ChangeBound、from_zero、not_recurring、World.enclosure_bounds_change、
           World.enclosed_binds_counting、EnclosedQueue.span 与 within_span、EnclosedQueue.empty_stays、World.finiteQueue、
           World.enclosed_counting_under）、whole-law-of-counting（Tally、Queue、Pointwise、World.CountsObey、
           World.counting_binds_jointly、World.taking_binds_counting、World.Meets、World.BindsCounting、Queue.lone）、
           ceasing-needs-arising（World.Finite.census_bounded）、map-of-premises（World.Finite.enclosed、World.still_vacuous）
Delta: Openness：列表引理 exists_of_mem_map、distinct_map_on，places_listed（finiteQueue_finite 由它得出），
       comesToBe_congr、ceasesToBe_congr；Ring（slot 与 slot_step、slot_lt、slot_add、slot_ne、slot_apart、slot_inj，
       size、seat、seated、holds、web、stands、flow，occupied、front_holds、span_fits、holds_iff、census、counts、
       taken_held、given_held）；Queue.lone_settles；World.ring、embodiedRing、balancedRing 与其 premised／holds、
       balancedRing_acting、三个 _meets；World.finite_counting_under、finite_counting_binds_iff、finite_change_bound_iff、
       enclosed_iff_finite_counting_under
Supplied premises / correspondence: 同 §52：列出与可判定，逐点；有限是世界的条件，不是公理；选择是到 Bool 的函数
Evidence: 合并检查器回执 20261010T112632.899583Z（1488 项定理、2361 项声明审计，全部源声明公理报告为空）；外围桥接重跑 20261010T112836.954648Z；实例检查
Boundary: 只说活动的计数；每个前提都起约束时的规律、水平与依存的计数在前提之下没有陈述；不评价生起、止息或静止；
          名称按 Ren 的命名准则由 AI 选，读法由 Ren 定
Integration: 计划 P38b（第一部分的总陈述：每个前提加了什么，在有限世界中）；扩展 counting-under-enclosure
```

| 声明 | 内容 |
|---|---|
| `Ring.slot` | 把成员依次排在一圈 N 个位置上：第 k+1 个坐在第 k 个的下一个位置，满一圈回到第一个位置。用自己的递归而不用 `Nat.mod`，因为前导中关于取余的引理带 `propext` |
| `Ring.slot_add`、`Ring.slot_ne`、`Ring.slot_inj` | 相距 d < N 时，位置前进 d，或前进 d 再减一整圈；所以相距不到一圈的成员位置不同，至多 N 个依次的成员中位置相同的是同一个 |
| `Ring.size`、`Ring.seat`、`Ring.seated`、`Ring.holds` | 每步至多 M 个在队中时取 2M+1 个位置；第 k 个成员的位置；每步被占的位置；位置被占 |
| `Ring.holds_iff`、`Ring.census`、`Ring.counts` | 一步前后在队中的成员都在这一步的跨度内，跨度不长于 2M，所以在那里位置被占恰当成员在队中；环列出每步被占的位置，各一次，计到队列所计的 |
| `World.ring`、`World.embodiedRing`、`World.balancedRing` | 不立任何东西、什么都不流动的环；每个位置被占时立着一的环；其队首的位置再从每个位置取用其水平所降的、给予其所升的环 |
| `World.ring_meets`、`World.embodiedRing_meets`、`World.balancedRing_meets` | 三者分别满足不选体现、不选平衡、不选耗散的每个选择；第三者只在没有成员加入空队时满足只有活跃者给予（`World.balancedRing_acting`） |
| `World.finite_counting_under` | 有限世界中，在每个选择之下，计数的一个性质在满足它的每个有限世界的每个普查中成立，恰当它对每个满足三个条件的计数表成立：每步至多有某数个活跃；选择约束计数或约束变化时没有关系项活跃的一步上没有生起；选择约束变化时从第 0 步起有变化界 |
| `World.finite_counting_binds_iff`、`World.finite_change_bound_iff` | 前者在有限世界中恰当选中平衡与体现、并选中只有活跃者给予或耗散时是规律；后者恰当选择约束变化时是规律 |
| `Queue.lone_settles`、`World.enclosed_iff_finite_counting_under` | 一个关系项在第 0 步生起之后，从第 1 步起变化界为一；有限世界与从某步起被围住的世界在一个选择之下有相同的计数规律，恰当这个选择约束变化且约束计数 |

**解读。**

- **有限是从第一步起的被围住。** 有限世界的每一步都被围住，所以 §52 中被围住的一步上的约束（平衡、耗散与体现就足够，`World.enclosed_binds_counting`）在每一步都起作用：选中这三者，就在每一步都没有关系项活跃时没有生起，不需要只有活跃者给予，也不需要只有活跃者取用；变化界也从第 0 步起成立。有限还给计数一个界：每个普查至多计到关系项那么多。
- **三种规律。** 所以有限世界中 256 个选择给出三种规律：有界的计数表；再加没有关系项活跃的一步上没有生起（选中平衡、体现、只有活跃者给予而不选耗散）；再加这一条与从第 0 步起的变化界（选中平衡、体现与耗散）。在不被围住的世界中只有两种（§52）。
- **环。** 有限的见证需要把无限的队列放到有限多个位置上。在全部八个前提之下，P35 的见证用变化界数出成员曾占的位置。其余选择之下没有变化界，计数可以每步都变，成员无限多；但每步在队中的不多于某数 M，一步前后在队中的不多于 2M，所以把成员依次排在一圈 2M+1 个位置上，任一步前后的成员都占不同的位置，环计到队列所计的。三个环对应 §52 的三个队列世界：不立任何东西的队列、立着的队列与被围住的队列（变化界为零），只是位置可以被再次占用。
- **何时与被围住的世界相同。** P35 说全部八个前提之下两类世界无法区分。在一个选择之下，它们恰在选择约束变化且约束计数时无法区分：那里被围住时的变化界从某步起，等于从第 0 步起的变化界（`ChangeBound.from_zero`），并给计数一个界。不约束变化时，每步多一个的计数由每步被围住的队列实现，却不由任何有限世界实现；约束变化而不约束计数时，在第 1 步闭合的队列可以让一个关系项在被围住之前从无到有地生起，有限世界不行。
- **一元的读法（AI 论证）。** 有限不是另加的规则，而是关系总在一个封闭的家族之内：所有关系项就是这个家族。所以耗散在每一步都起作用，生起总要从已在场的取得，变化总耗去所立者。被围住只从某步起把展开收进这样的家族，所以它之前的生起不受约束。

**作者反审。**

*反驳 1：环只是表示的技巧。* 环是见证，不是断言的内容。断言说的是有限世界中计数的规律；要表明更多的规律不成立，须有满足条件的有限世界实现每个这样的计数表，环就是这样的世界。成员依次占位、满一圈重用，只用到计数表与每步的界，不加计数之外的内容。

*反驳 2：每步至多某数活跃是否已经是全部？* 不是：在约束计数或约束变化的选择之下还有规律，且这些规律恰在可写出的选择之下成立（两条“恰当”）。界本身在每个选择之下都是规律（`World.Finite.census_bounded`），所以计数表加界是最弱的一种。

*反驳 3：总陈述中“有限世界的计数规律与此相同”的旧句是否错了？* 读作全部八个前提之下，它是对的（`World.enclosed_iff_finite_counting`）；放在每个选择的语境中，它的范围不准确。本节把它改为精确的陈述：恰在选择约束变化且约束计数时相同，全部八个前提是其情形。

*反驳 4：为什么不直接用 `Nat.mod`？* 前导中关于取余的引理（如 `Nat.mod_lt` 以外的 `Nat.add_mod`、`Nat.mod_eq_of_lt`）带 `propext`，核心要求公理报告为空，所以用自己的递归 `Ring.slot` 与它的三条引理。

**边界。** 无伦理谓词，不评价生起、止息或静止；只对离散步与每步有限的活动陈述；有限世界中的规律只读于活动的普查；每个前提都起约束时的规律、水平与依存的计数在前提之下没有陈述；名称（Ring、slot、seat、seated、ring、embodiedRing、balancedRing）是 AI 按 Ren 的命名准则所选：环（ring）取自系统中的环形缓冲区，说依次占用、满一圈重用的有限位置。本节尚未经独立审查。

## 55. 每个前提都起约束时计数的规律（P38c）

2026-10-10。按 Ren“let's aim for the strongest claim without axiom, as the first part”（[来源](../../../../sources/15-codex-theory-conversations/2026-10-10-zero-axiom-part-and-names.md)），补全第一部分总陈述中计数的规律在每个前提都起约束时的部分。全部八个前提之下计数的规律恰是计数表与没有关系项活跃的一步上没有生起（P34，`World.premised_counting`）；其见证开放的队列中耗散、活动需要支持与有界传递空成立（`World.openQueue_not_binds`，第十三次审查 U3 的探针）。每个前提都起约束时，每个普查都计到某个生起，这在八个前提之下不是规律（`World.binds_arising`、`World.binds_adds`）；是否还有更多的规律没有陈述（whole-law-of-counting 的下一增量）。本节给出完整的规律：只多出这一条。另外，`hatch` 中每个前提都起约束而世界归于静止（P29），开放纲领中“每个前提都起约束的世界归于静止”容易读作一般的陈述；本节表明，每个前提都起约束既不决定静止，也不决定变化不息。成果记录：修订 [whole-law-of-counting](../../../../theories/becoming/results/records/whole-law-of-counting.md) 与 [continued-change-needs-openness](../../../../theories/becoming/results/records/continued-change-needs-openness.md)。

```text
Result(s): 复用 whole-law-of-counting（Tally、Queue、Pointwise、World.CountsObey、World.counting_binds_jointly、
           World.premised_counting、World.binds_arising、World.binds_adds、OpenQueue.front）、counting-under-enclosure
           （EnclosedQueue.place、place_pos、place_zero、total_place、span、within_span、span_distinct、empty_stays、
           outside_empty）、map-of-premises（World.Binds、World.Premised、World.hatch_binds）、continued-change-needs-openness
           （World.standingCensus、Web.StandingCensus.stock_eq、World.hatch_rests）
Delta: Openness：add_sub_turn_add；EnclosedQueue.place_le、total_place_le、total_place_pos；BindingQueue（excess、level、
       exchange、web、flow，excess_le、level_le、still_flows、still、idle、busy、moving_within、closed、not_closed）；
       World.bindingQueue 与 bindingQueue_decided、_census、_embodied、_balanced、_acting、_taking、_exceeds、
       _dissipative、_premised、_binds；World.binding_counting、World.binding_contingent
Supplied premises / correspondence: 同 §52：列出与可判定，逐点；起约束是 World.Binds 的八个条件；有限与被围住不是前提
Evidence: 合并检查器回执 20261010T132639.927992Z（1512 项定理、2392 项声明审计，全部源声明公理报告为空）；外围桥接重跑 20261010T132949.908183Z；实例检查
Boundary: 只在全部八个前提之下陈述；每个选择之下所选前提都起约束时的规律、水平与依存的计数在前提之下没有陈述；
          只说活动的计数；不评价生起、止息或静止；名称按 Ren 的命名准则由 AI 选，读法由 Ren 定
Integration: 计划 P38c（第一部分的总陈述：每个前提都起约束时）；修订 whole-law-of-counting 与 continued-change-needs-openness
```

| 声明 | 内容 |
|---|---|
| `BindingQueue.excess`、`BindingQueue.level` | 队首在第 T 步多立着 E，其余步不多；成员按其在队中的位置而立 |
| `BindingQueue.exchange`、`BindingQueue.web`、`BindingQueue.flow` | 在除第 T 步外队列不空的每一步上，队首与每个关系项各交换一个单位；每个关系项以其所立的水平依存于每个关系项；队首从每个成员取用其水平所降的、给予其所升的 |
| `BindingQueue.not_closed`、`BindingQueue.closed` | 在除第 T 步外队列不空的步上，没有家族封闭；在不交换的一步上，跨度封闭这一步 |
| `World.bindingQueue_exceeds` | 跨第 T 步，队列不空且队首多立着的多于加入的时，队首从跨度取用的多于给予的：所立者下降 |
| `World.bindingQueue_premised`、`World.bindingQueue_binds` | 没有成员加入空队、E 多于第 T 步加入的数目时，起约束的队列满足全部八个前提；第 T 步有成员加入时每个前提都起约束 |
| `World.binding_counting` | 每个前提都起约束时，八个前提之下计数的规律恰是计数表、没有关系项活跃的一步上没有生起，以及有某个生起 |
| `World.binding_contingent` | `hatch` 中每个前提都起约束而生起停止；每步一个成员替换另一个的起约束的队列中每个前提都起约束，生起与止息复现 |

**解读。**

- **起约束只多出一条。** 第十三次审查问：开放的队列中三个前提空成立，全部八个前提之下计数的规律是否因此才这么少？回答是否定的。每个前提都起约束时，计数的规律只多出“有某个生起”，而这一条只来自体现起约束这一条件本身（有关系项生起时体现起约束），不用任何前提（`World.binds_arising`）。所以八个前提即使都在起作用，对计数的约束也不多于计数表与“没有关系项活跃的一步上没有生起”。（P41b 注：“都在起作用”应读作 `World.Binds` 的八个条件都有实例；见证中活动需要支持与有界传递对任何活动、任何流都成立，见 §58 V1。）
- **起约束的队列。** 见证须让每个前提都起约束，同时实现每个满足条件的计数表。耗散只在被围住的步上起约束，而从某步起每步被围住会给出变化界（§49），所以队列只在一步 T 上闭合：其余队列不空的每一步上，队首与每个关系项各交换一个单位，没有有限的家族封闭；在 T 上，队首只在队中交换，并失去在那一步多立着的 E，所以所立者下降，耗散起约束。为了让所立者在 T 上下降，不论加入多少成员，E 须多于第 T 步加入的数目。依存与传递的约束由一个最弱的网给出：每个关系项以其所立的水平依存于每个关系项，所以活跃者依存于自己且所需为正，后代在其第一步所依存的，给予者也依存。（P41b 注：这一队列改名为只闭合一次的队列 `OnceClosedQueue`；其中活动需要支持与有界传递对任何活动、任何流都成立，只在条件有实例的意义上起约束，排除什么的只有耗散，见 §58 V1、V6。）
- **静止与不息都不由起约束决定。** `hatch` 中每个前提都起约束，世界归于静止；每步替换一个成员的起约束的队列中每个前提都起约束，生起与止息复现。所以开放纲领中“每个前提都起约束的世界归于静止”只说 `hatch`，本节随之更正这一句。
- **有限世界不在其中。** 普查起约束只在于世界不有限，所以没有有限世界使每个前提都起约束；有限世界中的规律见 §54。
- **一元的读法（AI 论证）。** 起约束说的是前提在这个展开中确有实例：有依存，有给予与取用，有封闭家族上的耗散，有生起与传下。它们都起作用时，计数仍只记录进入与离开的相抵，加上至少有一次生起：关系怎样被给予、取用与依存，在计数中没有留下更多。

**作者反审。**

*反驳 1：“每个关系项以其所立的水平依存于每个关系项”是平凡的依存。* 它是最弱的，但满足 `World.Binds` 的条件：一个活跃者以正的所需依存于某个条件。断言说的是每个起约束的世界中都成立的规律；要表明更多的规律不成立，见证只需要是其中一个。更强的依存只会使更少的世界满足前提，不会使已在所有起约束的世界中失败的性质成为规律。（P41b 注：这只回答了见证；对起约束这一概念的反驳没有回答：要求每个前提排除表示所允许者的读法使更少的世界满足，也可能使更多的性质成为规律。这一读法列为开放，见 §58 V1。）

*反驳 2：只在一步闭合是否人为？* 它是见证的选择。耗散的起约束只要求某一步上某个封闭的家族被取用；要求从某步起每步都闭合就给出变化界，那是被围住的情形（counting-under-enclosure）。

*反驳 3：每个选择之下所选前提都起约束时如何？* 没有陈述。起约束的条件本身就给出计数的性质：活动需要支持起约束时某一步有活跃者，体现起约束时有某个生起；在部分选择之下，它们与前提的交互还须逐一给出见证。

*反驳 4：起约束的队列的 E 依赖计数（E 多于第 T 步加入的数目），是否把计数写进了世界？* 是的，每个见证都由计数表构造，开放的队列与环也是；断言说的是满足这些条件的计数表都被某个起约束的世界实现，不是一个世界实现所有计数表。

**边界。** 无伦理谓词，不评价生起、止息或静止；只对离散步与每步有限的活动陈述；只在全部八个前提之下陈述；每个选择之下所选前提都起约束时的规律、水平与依存的计数在前提之下没有陈述；名称（BindingQueue、excess、exchange、bindingQueue、binding_counting、binding_contingent）是 AI 按 Ren 的命名准则所选：起约束的队列（binding queue）取自它让每个前提起约束的作用，excess 说队首在一步上多立着的，exchange 说开放步上的交换。本节尚未经独立审查。（P41b 注：本节已经第十四次独立审查；起约束的队列按其动力学改名为只闭合一次的队列，见 §58。）

## 56. 不用公理能走多远（P40）

2026-10-10。Ren 选定路线：“let's aim for a first, then try to archive b”（[来源](../../../../sources/15-codex-theory-conversations/2026-10-10-axiom-route-levels-and-possibilities.md)）。路线 (a) 见 §53。路线 (b) 是 AI 的表述，Ren 引用了它：

> No axiom. The theory only describes, and “should” is what a center does once its represented boundary matches what it actually depends on. The theory then explains recognition and motivation but claims no warrant beyond them.

AI 还提出两种不需要前提的机制：“selection between wholes: wholes whose parts sustain them outlast others”与“constraint: a part that degrades its whole removes its own supply”。Ren 回答，整体对自身的实现、理解与更新“also under the selection rules and constraints in theory, but in practice, how this happens, needs more thoughts”。对层级，Ren 写道：“i think it should be the whole, and a weaker version is within the system that one is in, then the self”。§53 留给路线 (b) 的问题是：以依存为界的中心容许搭便车者（`Clearing.centers_disagree`）。

本节是计划 P40（[计划 §10](BECOMING-UNIFICATION-PLAN.md#10-第一部分与第二部分--part-i-and-part-ii)），由本会话完成。它不加公理，问这条路线到达哪一层。核心新增模块 `Becoming.Interdependence`，28 项定理。不用公理的结果放进第一部分（章节 §2 的“供给与返回”与第一部分的总陈述），路线 (b) 的分析与比较放进第二部分（章节 §6.9）。成果记录新增三项：
- [feeding-closure](../../../../theories/becoming/results/records/feeding-closure.md)
- [consumption-ends-with-feeders](../../../../theories/becoming/results/records/consumption-ends-with-feeders.md)
- [closure-verdict-meets-axiom](../../../../theories/becoming/results/records/closure-verdict-meets-axiom.md)

另修订三项记录的界限与下一增量，断言不变：
- [loss-beyond-a-region](../../../../theories/becoming/results/records/loss-beyond-a-region.md)：`alongDependence` 与沿供给推出的范围一致，原是逐项对照，现由 `Clearing.dependenceRegion_iff` 证明；
- [whole-first-and-bounded-centers](../../../../theories/becoming/results/records/whole-first-and-bounded-centers.md)：以依存为界的区域恰是各形成的供给闭包，以它为意义的边界仍是选择；
- [represented-boundary-against-dependence](../../../../theories/becoming/results/records/represented-boundary-against-dependence.md)：多步的依存范围由供给闭包给出，并在 `Overshoot` 中与所表示的边界比较。

```text
Result(s): 复用 derived-extent-limits（Flow.FedBy、Clearing.fedBy_source）、own-count-misses-joint-excess
           （Flow.excess_bounded）、represented-boundary-against-dependence（Web.RenewingOver）、becoming-stepwise-reading
           （Web.UnderminingAt）、loss-beyond-a-region（Clearing.alongDependence、Clearing.loses_beyond、
           Web.LosesBeyond.narrow）、four-cases-of-a-part（Clearing.clearerPart、admitted_without、unsupported_with）、
           closing-needs-net-draw（Web.Admits、Flow.WithheldLevels）、one-axiom-yields-g0（Unrestricted、bounded）、
           significance-retained-within-margin（Web.Retains、Web.Adds、Web.Includes.retains、Web.retains_iff_includes）、
           whole-first-and-bounded-centers（Web.retains_bounded_iff、Web.Retains.within、Clearing.dependenceRegion、
           Clearing.free_rider_loses）；新增上列三项
Delta: Flow.FedClosed、Flow.WithinFeeding（refl、trans、of_fedBy）、Flow.fedClosed_within、Flow.beyond_gives_nothing；
       Flow.Balances.unfed_consumption_ends、unfed_consumption_stops、Flow.unfed_of_feeders_unsupported、
       Flow.Balances.consumption_ends_with_feeders；bounded_whole、Web.retains_bounded_iff_includes、
       Web.retains_bounded_iff_retains、Flow.within_closure_iff_retains；Overshoot（flow、web、balances、acting、taking、
       dependent、closure_whole、ends_through_feeder、steadyFlow、steadyWeb、steady_continues、within_closure_iff_retains）；
       Clearing.fedClosed、dependenceRegion_closed、dependenceRegion_self、dependenceRegion_iff、dweller_beyond、
       closure_supported、within_closure_yet_loses
Supplied premises / correspondence: 不加公理；一般定理的前提是平衡、只有活跃者给予、活动需要支持，以及形成在其活跃的
       每一步从所需条件取用；见证另有只有活跃者取用、只从其所汲取者取用；公理 Unrestricted 只作为比较定理的假设出现；
       供给读作同一步上向所需条件的给予；离散的步、自然数的量；读法与名称是 AI 的，待 Ren
Evidence: 合并检查器回执 20261010T133601.876717Z（1540 项定理、2426 项声明审计、核心闭包 35 个模块、包 33 个模块，全部源声明公理报告
          为空，没有新的生成常量依赖公理）；外围回执 20261010T133831.669969Z
Boundary: 中心想要自身的延续、表示其供给闭包都不推出；闭包之内的损失确实返回也不推出（供给者可以冗余，存量与时机决定
          终结何时到来）；路线 (b) 不主张根据；整体之间的选择没有建模；供给只计同一步的给予，闭包是形成层面的
Integration: 计划 P40（路线 (b)）；回答 §53 留下的以依存为界的中心容许搭便车者：不用公理时，这一损失只在依存到达
             所关闭者时被计入；路线 (b) 到达自身与所在的系统，只在整体是一个供给闭包时到达整体
```

| 声明 | 内容 |
|---|---|
| `Flow.FedClosed`、`Flow.WithinFeeding` | 形成的区域对供给封闭：供给一个成员之延续者都是成员；`g` 在 `f` 的供给闭包之内：含 `f`、对供给封闭的每个区域都含 `g` |
| `Flow.WithinFeeding.refl`、`trans`、`of_fedBy`、`Flow.fedClosed_within` | 闭包含其形成，可传递，含任何一步的每个供给者，本身对供给封闭：所以是含该形成、对供给封闭的最小区域 |
| `Flow.beyond_gives_nothing` | 闭包之外的，在任何一步都不向闭包成员当时所需的条件给予 |
| `Flow.Balances.unfed_consumption_ends`、`unfed_consumption_stops` | 在平衡、只有活跃者给予、活动需要支持之下，形成从第 T 步起在其活跃的每一步都在场并从条件 `c` 取用，而没有被支持者向 `c` 给予：它从第 T 步起至多连续活跃 `c` 在第 T 步的水平那么多步，所以不在此后每一步都活跃 |
| `Flow.unfed_of_feeders_unsupported`、`Flow.Balances.consumption_ends_with_feeders` | 形成活跃时需要 `c`，而从第 T 步起供给其延续的都不被支持，则没有被支持者向 `c` 给予；所以同一界成立，消耗随其供给者终结 |
| `Overshoot.flow`、`web`、`balances`、`acting`、`taking`、`dependent`、`closure_whole` | 两个形成各自以所需一依存于以自身命名的条件，在第 0 步各自供给对方的条件，所以任一个的供给闭包都是整体；第 0 步 `true` 从两个条件各取一个单位 |
| `Overshoot.ends_through_feeder` | 流平衡，只有活跃者给予与取用、只从其所汲取者取用，活动需要支持。第 0 步 `true` 在其所需的唯一条件上更新，在第 1 步仍被支持，而它的汲取侵蚀 `false` 的依存，`false` 供给 `true` 的条件。`false` 从第 1 步起不被支持，`true` 从第 1 步起至多连续活跃一步，从第 2 步起没有任何被支持者 |
| `Overshoot.steadyFlow`、`steadyWeb`、`steady_continues` | 依存相同，各自只从自己的条件取用：流平衡，两者每步都活跃且被支持 |
| `Overshoot.within_closure_iff_retains` | 公理之下，从任一立场、在每个比较上，闭包内的判断就是公理的判断 |
| `Clearing.fedClosed`、`dependenceRegion_closed`、`dependenceRegion_self`、`dependenceRegion_iff` | §53 沿依存的区域对供给封闭、含其形成，恰是各形成的供给闭包：清除者与供给其资源的来源；来源与栖居者没有被供给，各自只含自身 |
| `Clearing.dweller_beyond`、`Clearing.closure_supported` | 栖居者在清除者的闭包之外；闭包之内的每步都被支持，清除者每步活跃，栖居者从第 2 步起不被支持 |
| `bounded_whole` | 以整体为界的意义（各立场的区域都是整体）就是公理 |
| `Web.retains_bounded_iff_includes`、`Web.retains_bounded_iff_retains` | 另一条路径接纳的每个形成都在立场的区域之内、或被第一条接纳之处，以区域为界的意义与包含一样保留；公理之下，这时两个判断一致 |
| `Flow.within_closure_iff_retains` | 一个形成的供给闭包是整体时，公理之下，以闭包为界的判断在每个比较上都是公理的判断 |
| `Clearing.within_closure_yet_loses` | 以供给闭包为界，从清除者的立场，有其部分的水平保留无它时的有意义者；公理之下，从每个立场都不保留；从栖居者的立场、在栖居者自己的闭包内，无它的水平增加栖居者 |

**它回答了什么。**
- **所依存的，不用前提即到达。** 路线 (b) 要求所表示的边界与“what it actually depends on”一致。在形成层面，这读作供给闭包：它只由供给关系定义，不用任何前提，是含该形成、对供给封闭的最小区域；闭包之外的在任何一步都不向闭包所需的条件给予。§53 中各形成的意义止于其依存所及，那个区域恰是推出的供给闭包（`Clearing.dependenceRegion_iff`），所以 P39 的中心分歧不靠规定。P37 中 `alongDependence` 与沿供给推出的范围一致原是逐项对照，现在是定理。
- **约束沿供给而行。** AI 的第二种机制是“a part that degrades its whole removes its own supply”。一般定理给出它的形式：在平衡、只有活跃者给予、活动需要支持之下，供给者都不被支持时，消耗至多持续所耗条件的水平那么多步（`Flow.Balances.consumption_ends_with_feeders`）。`Overshoot` 表明，返回可以越过只覆盖所需条件的边界：一个形成在其所需的唯一条件上更新，跨过这一步保住自身支持，却经其供给者终结。P37 的一步比较（represented-boundary-against-dependence）由此在多步上补全：延续所依存的，到达供给者的延续。
- **闭包之外的不必返回。** `Clearing` 中栖居者在清除者的闭包之外：闭包之内的每步都被支持，清除者始终活跃，而栖居者终结。约束到不了返回不到任何人的损失。
- **路线与公理在哪里相合。** 以整体为界的意义就是公理（`bounded_whole`）。另一条路径接纳的每个形成都在区域之内、或被第一条接纳之处，以区域为界的判断就是公理的判断（`Web.retains_bounded_iff_retains`）。一个形成的供给闭包是整体时总是如此（`Flow.within_closure_iff_retains`），如 `Overshoot`。`Clearing` 中两者分开（`Clearing.within_closure_yet_loses`）。
- **所以路线 (b) 到达自身与所在的系统（AI 的读法，待 Ren）。** 想要自身延续、并表示其闭包的中心，有它自己的理由保留闭包之内的：那里的损失可以返回到它。这解释动机，不是根据。整体之间的选择保留延续的整体：它淘汰 `Overshoot` 的整体，保留 `Clearing` 的整体。所以两种机制都到不了返回不到任何人的损失。路线 (b) 只在整体是一个供给闭包时到达整体，那时它的判断就是公理的判断。公理所加的，是那些损失返回不到任何人的延续的意义，如栖居者的。Ren 写道整体可以实现自身，“like us, we recognize that "we" are the universe/ecosystem that realizes its own existence”。以整体为所表示边界的中心，持有的就是公理的意义（`bounded_whole`）；路线 (b) 要求所表示的边界与实际依存一致，所以只在依存到达整体时给出它。

**作者反审。**
1. **供给只计同一步的给予。** `Flow.FedBy` 要求供给者在同一步向所需条件给予。经条件的延迟输送（这一步给予，以后才被取用）不算供给，所以闭包可能漏掉这样的依存。延迟输送是否算供给，列为开放项。
2. **闭包是形成层面的。** 只要在某一步供给，就在闭包之内；链上各环可以在不同的步，也不按时间先后。所以闭包含已停止供给者，不是当下的依存。按步、按时间先后的依存范围列为开放项。
3. **返回不必然。** 一般定理只说：供给者都不被支持时，消耗终结。闭包之内的损失是否真的返回，取决于有无其他被支持的供给者（冗余），以及存量与时机。`Overshoot` 中只有一个供给者，存量是一。`ends_through_feeder` 是存在性的见证，不说每个闭包之内的损失都返回。
4. **见证的终结是规定的。** 和以往的见证一样，`Overshoot` 的活动由规定给出，见证表明它与平衡、支持与依存相容。终结的推出在一般定理中：见证用 `consumption_ends_with_feeders` 推出 `true` 从第 1 步起至多再活跃一步。
5. **比较用实际流与参照流。** 以扣留水平作的比较保持交换的其余部分不变，所以经动力学返回的终结不能在一个扣留比较中表明。`Overshoot` 在实际的流上表明终结；`steady_continues` 是另一个流（各自只取自己的条件），不是同一个流扣留一个部分。两者的差别是汲取的差别，不是一个部分的有无。
6. **“动机”是读法。** 定理不说中心想要什么，也不模型中心怎样表示其闭包。说表示其闭包的中心有其自身理由保留闭包之内的，是 AI 对路线 (b) 的读法：理由来自损失可以返回到中心。这是动机的解释，不是根据。
7. **整体之间的选择没有建模。** 关于选择的一句只用了两个见证中谁延续，没有群体、复制或竞争的模型。
8. **读法与名称是 AI 的。** `FedClosed`、`WithinFeeding`（供给闭包）与 `Overshoot`（越限，生态学与系统动力学的用语）是 AI 按 Ren 的命名准则所选。供给闭包读“what it actually depends on”与“the system that one is in”，待 Ren。

**检查。**
- 模块先在暂存区对含 `Becoming.Significance` 的核心编译，逐条审计全部 69 项声明（含 Lean 生成的辅助声明），公理报告全部为空。
- 合并检查器对加入模块的包检查一次，通过：回执 20261010T133601.876717Z。`Becoming.Interdependence` 的 28 项定理、34 项声明审计全部空依赖；Lean 生成而依赖 propext 的常量仍是 38 个，没有新增。
- 外围桥接对这个核心重查（20261010T133831.669969Z），闭包中其余 38 个模块的当前字节与已通过回执一致。
- 本节尚未经独立审查。

## 57. 计数自成一个模块（P41）

2026-10-10。按 Ren“please make sure the whole codebase is elegant, structurally and conceptually … if name is not the best to represent our truth, update them as well”（[来源](../../../../sources/15-codex-theory-conversations/2026-10-09-pure-core.md)），把前提给计数的规律加了什么，从 `Becoming.Premises` 与 `Becoming.Openness` 移入新模块 `Becoming.Counting`。这一部分在 P31–P38c 中逐步增长，分在两处：`Becoming.Premises` 本是前提的地图（哪些推出哪些，其余独立，全部满足，每个起约束），`Becoming.Openness` 本说明持续的变化需要所立者之外的交换（静止定理）；计数的规律的后半在 Openness 中，只因为它用到被围住与有限世界的引理。现在 `Becoming.Counting` 导入 `Becoming.Openness`，按一条线陈述：全部八个前提之下，每个选择之下，从某步起被围住时，有限世界中，每个前提都起约束时。成果记录：修订 [whole-law-of-counting](../../../../theories/becoming/results/records/whole-law-of-counting.md)、[counting-under-enclosure](../../../../theories/becoming/results/records/counting-under-enclosure.md) 与 [continued-change-needs-openness](../../../../theories/becoming/results/records/continued-change-needs-openness.md) 的证明引用。

```text
Result(s): 复用 whole-law-of-counting、counting-under-enclosure、continued-change-needs-openness；没有新的结果
Delta: 新模块 Becoming.Counting（130 项定理）：Premises 中自“计数在前提之下”起的部分，前提的名称与选择
       （World.Premise、Premise.Holds、Meets、Premised.meets）留在 Premises 新的“前提的选择”一节；Openness 中自
       “计数在被围住时”起的部分，连同只有环用到的列表引理 exists_of_mem_map、distinct_map_on；名称、陈述与
       证明逐字不变；三节标题由“每组前提”改为“每个选择”，与模块文档一致
Supplied premises / correspondence: 不变
Evidence: 合并检查器回执 20261010T145237.259199Z（1540 项定理、2426 项声明审计，全部源声明公理报告为空，核心闭包 36 个模块，
          包 34 个模块）；外围回执 20261010T145910.464504Z；移动的 191 项声明先在暂存树中逐一以 #print axioms 查过
Boundary: 只是结构；不加任何断言
Integration: 计划 P41；修订三条记录的证明引用与验证范围；模块文档、根模块文档、包 README、章节脊柱表与
             检查器范围随之更新
```

**为什么分开。**

- **三个问题。** 前提的地图回答前提彼此怎样关联，开放回答持续的变化需要什么，计数的规律回答前提给计数加了什么。三个问题各有自己的见证（互利者与 hatch；exposed、throughput 与 holding；队列与环）。第三个问题原先放在前两个模块的末尾，两个模块的文档都要分两半读。
- **依赖。** 计数的规律用到前两者：Premises 的前提，Openness 的被围住、有限世界与普查的界。所以它在两者之后。没有别的模块用到被移动的声明，移动不改变任何其他模块。
- **顺带改正。** 根模块文档中 Premises 与 Openness 的条目没有提到 P38–P38c 的计数结果；Openness 条目中“as does the world in which each of them binds”含糊，现在写明是 `hatch`。

**作者反审。**

*反驳 1：移动声明会不会使记录与引用失效？* 声明名称不变（命名空间不变）。三条记录引用的被移动的声明移到 Counting 的证明引用，相应反例的路径随之改正；其余记录引用的 Premises 与 Openness 的声明都没有移动，已逐一比对。登记检查逐一核对每个引用的声明在其文件中。

*反驳 2：为什么不并入 Population？* Population 不加前提：计数表是计数的全部规律。Counting 说的正是前提加了什么，需要 Space 的世界与 Premises 的前提，而 Population 在它们之下。

*反驳 3：历史文档中对 Openness 的引用？* 研究文档的旧节与审查报告保持原文，按日期读；当前的章节、记录与包文档指向 Counting。

**边界。** 无新数学，无伦理谓词；第十四次独立审查（P34b–P38c）的处理在下一节。

## 58. 第十四次独立审查与更正（P41b）

2026-10-10。按 Ren“let's aim for the strongest claim without axiom, as the first part”（[来源](../../../../sources/15-codex-theory-conversations/2026-10-10-zero-axiom-part-and-names.md)）与“aim a complete theory of becoming, and finish related work”继续。另一 agent（Claude Opus 5.5，未参与撰写）独立审查了 P34b（§48）、P35（§49）、P36（§50）、P36b、P38（§52）、P38b（§54）与 P38c（§55）（[审查](BECOMING-P34B-P38C-REVIEW.md)，对象 `c95f6576`，经六个提交）；P37 与 P39 不在对象之内，只核对第一部分总陈述是否如实转述 P37。它在仓库之外从前导重新编译核心闭包的 34 个模块，回执所列的 2462 条闭包源声明的公理报告全空；闭包的 6697 个常量中依赖公理的只有 38 条编译器生成的 `injEq` 引理，都只依赖 `propext`，与回执所列相同；六个提交的核心与外围回执、源哈希、检查器哈希与保留产物都与提交一致，回执都早于其提交；章节 §9 的计数等于回执；登记检查与四份记录的聚焦检查在快照上通过。P36 只改名：去掉注释后按词元比较，22 个改动的核心文件只有等长的标识符替换，替换是单射，保留运行的 737 条签名在改名之下逐条相同。数学全部接受，对象中没有错误的 Lean 陈述。它写了 32 条探针声明（22 项定理），其 82 个常量不依赖任何公理。问题六项（V1–V6）；最重要的是 V1 与 V2。

```text
Result(s): 更正 whole-law-of-counting（V1、V4、V5、V6）、counting-under-enclosure（V4、V5、V6）、
           continued-change-needs-openness（V6）、map-of-premises（V1、V4）；没有新的成果记录
Delta: Counting：World.enclosed_change_bound_iff；OnceClosedQueue.dependent_any_activity、
       OnceClosedQueue.transmits_any_flow；BindingQueue 与 World.bindingQueue 及以其命名的定理改名为 OnceClosedQueue
       与 World.onceClosedQueue；add_sub_turn_add 移到 Dependence 的算术一节。Premises：World.Finite.not_binds；
       World.FiniteHatch（Relatum、into、flow、web、taking_part、kin、kin_distinct、closed）、World.finiteHatch、
       finiteHatch_decided、finiteHatch_finite、finiteHatch_balanced、finiteHatch_dissipative、finiteHatch_premised、
       finiteHatch_binds_but_census；World.Binds 的说明。说明中 idle 只指不参与流的关系项（hatch_idle），驱动者是
       inactive，空成立是 vacuously
Supplied premises / correspondence: 不变
Evidence: 合并检查器回执 20261010T150853.470895Z（1552 项定理、2445 项声明审计，全部源声明公理报告为空；Dependence 59、
          Premises 59、Counting 132）；外围回执 20261010T151108.093153Z；新声明先在暂存树中从前导编译，核心模块没有输出
Boundary: 不含伦理结论；不替 Ren 选择任何读法；更强的起约束读法列为开放，没有尝试
Integration: 章节第 3、4、11 条，第一部分的总陈述，状态表、进一步的证明与审查，§9 的脊柱表；计划 §10、P36 对照表、
             P38 与 P38c 两行；§52、§55 与英文 P38、P38c 段落的就地注；模块说明、根模块、包 README 与检查器的范围
```

### 58.1 逐项处理

| 项 | 审查所见 | 处理 |
|---|---|---|
| V1 | 起约束的队列让每个关系项以每个关系项所立的水平为所需，所以活动需要支持对任何活动成立，有界传递对任何流成立（探针 `bindingQueue_shape`）；`binding_counting` 相对于 `World.Binds` 是对的，但“八个前提即使都在起作用”“依存与传递起约束”“约束世界而非空成立”读得比定义强；§55 反驳 1 只说见证，没有回答对起约束这一概念的反驳 | 移入核心：`OnceClosedQueue.dependent_any_activity` 与 `OnceClosedQueue.transmits_any_flow`，这一披露由此可检查。`World.Binds` 的说明改为：有东西满足其条件，所以前提不空成立；实例不必排除表示所允许的任何东西。起约束一律写作“每个前提的条件都有实例”：章节第 3 条、第一部分的总陈述、状态表与脊柱表，Counting 与 Premises 的模块说明、根模块、包 README、检查器，记录的主张、局限与反例，计划 P38c 两行与 §55、英文 P38c 段落的就地注。开放项：在每个前提都排除表示所允许者的起约束读法之下，“有某个生起”是否仍是唯一多出的规律；这一读法由 Ren 选择，本节没有尝试 |
| V2 | 计划 §10 把 Ren 的“let's aim for the strongest claim”写成“它是不用公理所能得到的最强陈述”；P38 一行写“在计数上补全”，随后 P38b 与 P38c 又补了两部分；总陈述末句的“完整”没有指明计划 §9 的四项标准 | 计划 §10 中英文改为“以……为目标”并注明原文；P38 一行注明补全的是一般世界中活动的计数在 256 个选择之下的规律；总陈述与第 11 条的末句链到计划 §9 的四项可检查内容，总陈述加一句：第一部分以最强陈述为目标，还没有表明它就是最强的，仍开放的形式问题见 §8 |
| V3 | 总陈述的五处不精确：“每件都已在 Lean 中检查”覆盖了不是 Lean 陈述的话；被围住一句省去“从某步起”与随之的一条；终结之步省去前提；部分与区域不写 P37 定理的前提；计数一条的边界不在原处 | 1“其中每条定理都已在 Lean 中检查”，并写明定理之间的说明不是 Lean 陈述；2 被围住一句用第 4 条的说法，并引 `enclosed_change_bound_iff`；3 终结之步写明普查、体现、平衡与耗散，以及“满足八个前提、活动可判定的有限世界”；4 部分与区域写明比较所用的扣留水平（`Flow.withhold`、`Flow.WithheldLevels`，这是表示上的选择）与平衡的流，`gains_from_supported` 另写平衡、只有活跃者给予、活动需要支持与要求不放松（先重读了 P40 加的“供给与返回”一条，写法与之一致）；5 计数一条后加边界：只是活动的计数，水平与依存的计数、每个选择之下所选前提都起约束时与有限世界中除普查外都起约束时的规律没有陈述 |
| V4 | 三处“恰”或“没有”没有核心定理：被围住时变化界恰在选中平衡、体现与耗散时是规律；没有有限世界使每个前提都起约束；有限世界中除普查外每个条件都可以有实例，这样的有限世界中计数的规律既没有陈述也没有列为开放 | 移入核心：`World.enclosed_change_bound_iff`（不约束变化时，每步多一个的计数由满足这个选择、从某步起被围住的世界实现，不在任何界内）；`World.Finite.not_binds`（由 `Binds.counted` 一行得出）；`World.finiteHatch` 与 `World.finiteHatch_binds_but_census`（去掉闲置地关系项的 hatch 有限、满足八个前提，除普查外每个条件都有实例，而不是每个前提都起约束）。第 4 条“不选耗散时”改为“不同时选中这三者时”，“恰”引新定理；有限世界中除普查外每个前提都起约束时计数的规律列入开放：章节 §8、whole-law-of-counting 与 counting-under-enclosure |
| V5 | counting-under-enclosure 的局限与下一步在 P38c 之后仍说每个前提都起约束时的规律没有陈述；§8 进一步的证明只引到 P35；P36 对照表漏了 `Provisioned.gift → provision`；P38c 把算术引理 `add_sub_turn_add` 放在 Openness | 记录改为指向 whole-law-of-counting（相对于 `World.Binds`），并列出被围住时与有限世界中仍开放的起约束规律；§8 加上 P38、P38b、P38c 与 `Becoming.Counting` 及开放项；对照表加一行；`add_sub_turn_add` 移到 Dependence 的算术一节，紧随 `add_sub_turn` |
| V6 | “idle”有两种意思（`hatch_idle` 不参与流；`drivenQueue` 的驱动者参与每一步，只是不活跃）；`bindingQueue` 以它在定理中的作用命名，不以其动力学；核心仍有金融词 `credits`、`overdraw` | 驱动者改为“不活跃的地关系项 / an inactive ground relatum”；英文“hold idly”（三个前提在见证中空成立）改为“hold vacuously”，与中文“空成立”一致；idle 只留给不参与流的关系项。起约束的队列改名为只闭合一次的队列（`OnceClosedQueue`、`World.onceClosedQueue`，审查另提的 `SingleClosureQueue` 也合准则）：除一步外每步开放，在那一步闭合并失去多立着的。旧名留在历史条目、保留的运行、旧回执与审查文件中，按计划 §10 对照表读。`credits`、`overdraw` 属于整个核心的用语，列为按 Ren 命名准则的下一次清理的候选，本节不改 |

### 58.2 新的已检查声明

| 声明 | 内容 |
|---|---|
| `World.enclosed_change_bound_iff` | 从某步起被围住的世界中，从某步起的变化界是一个选择之下的计数规律，恰当这个选择约束变化（选中平衡、体现与耗散） |
| `OnceClosedQueue.dependent_any_activity`、`OnceClosedQueue.transmits_any_flow` | 只闭合一次的队列的网对任何活动都需要支持，对任何流都在 1 + E 之内传递每个依存：这两个前提在其中只是条件有实例 |
| `World.Finite.not_binds` | 没有有限世界使每个前提都起约束 |
| `World.FiniteHatch`、`World.finiteHatch` 与其 `_finite`、`_balanced`、`_dissipative`、`_premised` | 去掉地关系项的 hatch：只有食物、亲代与子代，有限、平衡、耗散，满足八个前提 |
| `World.finiteHatch_binds_but_census` | 它有限、满足八个前提、不是每个前提都起约束，而除普查外每个条件都有实例 |
| `add_sub_turn_add` | 移到 Dependence 的算术一节；陈述与证明不变 |

### 58.3 作者反审

*反驳 1：起约束只是条件有实例，`binding_counting` 是否因此无意义？* 不是。它回答的是第十三次审查的问题：三个前提在开放的队列中空成立，规律之少是否来自空成立；答案是不，只要每个条件都有实例，规律仍只多出“有某个生起”。V1 说的是这一回答的范围：它不回答更强的起约束读法。更强的读法须先说明“排除表示所允许者”指什么（对活动、对流、对水平），这是读法的选择，所以列为开放而交给 Ren。

*反驳 2：新定理是否只是把探针搬进核心？* 是，按审查的修正建议；它们把散文中的“恰”“没有”变成可检查的陈述，没有新的数学主张。

*反驳 3：有限的 hatch 是否说明有限世界中的起约束规律也只多出“有某个生起”？* 不说明。它只表明除普查外的条件在有限世界中可以都有实例；每个这样的计数表是否都由一个这样的有限世界实现，没有给出，所以列为开放。

*反驳 4：为什么不同时清理 `credits`、`overdraw`？* 它们分布在八个核心模块中（Dependence、Return、Horizon、Joint、Substitution、Generation、Metaethics 与 Ranking，Ranking 中最多），改名牵涉许多记录与审查文件的对照；按 Ren 的命名准则，它们应在一次整体清理中处理，与本节的审查处理分开。

**边界。** 无伦理谓词；没有新的成果记录，断言的数学不变或只是补上散文已说的；更强的起约束读法、每个选择之下所选前提都起约束时的规律、有限世界中除普查外都起约束时的规律、水平与依存的计数在前提之下，仍开放。第十四次审查检查了 §48 的处理与 §49、§50、§52、§54、§55；§47.1–47.4 的处理、§51、§53、§56、§57 与本节尚未经独立审查。

## 59. 单位所承载的：每一分辨率下的静止（R1）

2026-10-10。按 Ren“let's push as far as possible and if we see a stronger claim that can be make and is important, give it a try. we push pareto frontier”与“keep going please, agree with direction”（[来源](../../../../sources/15-codex-theory-conversations/2026-10-10-pareto-frontier.md)）。这一方向读作：每个主张取其成立的最强形式，并以只缺一个前提的见证标出它失效的确切边界。此前列出的难题之一是表示的范围，即哪些规律是量与步的表示方式的产物；这里处理量的单位。脊柱以一个固定单位的自然数计量。按这个单位读，耗散说取用封闭家族的形成给回的至少比取用的少一个单位，所以每次交换至少损失一个单位，静止定理与开放的规律都以这些损失抵扣所立者。新模块 `Becoming.Resolution`（导入 `Becoming.Openness`）让单位在每步可以细分，把属于动力学的与属于固定单位的分开。成果记录：[rest-at-every-resolution](../../../../theories/becoming/results/records/rest-at-every-resolution.md)。

```text
Result(s): 新记录 rest-at-every-resolution；复用 continued-change-needs-openness（所立者的普查及其存量、围住所立者的步、
           exposed 的持有者）与 no-finite-part-bears-taking（耗散、封闭家族、DissipatesOn.replenishment_takers）
Delta: Flow.BalancesAt r：单位跨过第 t 步分为 r t 个更细的单位，r 恒为一时就是 Balances；损失的规律 losses_invariant、
       losses_bound 与量子的规律 Flow.quantum_bound、Flow.quantum_not_recurring；单位固定时取用停止 Flow.taking_stops；
       按比例的损失 Flow.DissipativeBy q 之下交换的规律 Flow.exchange_bound、Flow.exchange_not_recurring 与增长的规律
       World.growth_bound、World.growth_not_recurring、World.arising_not_recurring；见证 Asymptote、Circulation、
       Emission、Alternation 与边界定理 rest_needs_quantum、exchange_needs_quantum、arising_needs_quantum、
       arising_needs_proportion
Supplied premises / correspondence: 单位只细分（R T = 1，R (t + 1) = r t · R t，0 < r t）；按比例的损失是前提，是脊柱一单位
       损失的无单位对应，不是推出的；世界的规律另要活动的普查、关系项都体现、从 T 起每步被围住
Evidence: 合并检查器回执 20261010T155424.663562Z（1649 项定理、2571 项声明审计，全部源声明公理报告为空；Resolution 97，核心闭包 37
          个模块），外围回执 20261010T161037.642977Z；Becoming.Resolution 的声明先在暂存树中以已提交的核心源从前导编译，逐条 #print axioms
          全部为空
Boundary: 离散步；有理量，单位不变粗；界是否可达未证；交换的规律只对固定的封闭家族陈述；尚无独立审查
Integration: 回答 continued-change-needs-openness 的下一步“带比率或连续量的总水平”中有理量的部分；计划 §10 R1；章节 §9 的
             脊柱表与第一部分的开放项；模块说明、根模块、包 README 与检查器的范围
```

**机制。**

- **单位可以细分。** 跨过第 t 步，单位分为 r t 个更细的单位：步前的水平以更细的单位计，是以较粗单位计的 r t 倍（`Flow.BalancesAt`）。R 计每一步的单位数，以第 T 步的单位为一，R (t + 1) = r t · R t。以第 T 步的单位读，一个水平 n 在第 t 步是 n / R t，所以细分以越来越细的有理数表示量，而动力学不变。在耗散之下，封闭家族的存量连同取用者不多于 r t 乘此前的存量（`Flow.BalancesAt.lowers`）；r 恒为一时就是脊柱的情形。
- **损失的规律。** 一个在更细单位下不上升的量，若每步 q 乘余下的连同 k 个量子（每个是 R (t + 1) 个更细单位）不多于 q 乘此前所有的，那么自 T 起计到的量子不多于 q 乘该量在 T 的值（`losses_invariant`、`losses_bound`）。证明只是算术：不变量 q·s + K·R ≤ q·s_T·R 跨过一步乘以 r。由此，封闭家族损失至少 1/q 单位的步不多于 q 乘其存量，不复现（`Flow.quantum_bound`、`Flow.quantum_not_recurring`）。单位固定时，每个取用的步至少损失一个单位，所以取用停止（`Flow.taking_stops`）；r 恒为一时这就是脊柱的 `Flow.Balances.taking_ceases`。
- **按比例的损失。** 每个形成给回封闭家族的至多是所取用的 q/(q+1)（`Flow.DissipativeBy q`）。这一比例与单位无关。于是：
  - 取用至少 1/p 单位的形成使家族至少损失 1/(p(q+1)) 单位，所以这样的取用逐个逐步计数不多于 p(q+1) 乘存量（`Flow.BalancesAt.takers_lose`、`Flow.exchange_bound`）；
  - 增长至少 1/p 单位的关系项所得是被给予的，所以在围住它的家族中，补给至少是 R (t + 1)/p 乘增长者的数目，而按比例的损失使家族至少损失补给的 1/q（`Flow.BalancesAt.gain_given`、`Flow.BalancesAt.lowersBy`、`Flow.BalancesAt.gainers_lose`）；在有普查、关系项都体现、从 T 起每步被围住的世界中，围住的家族随步变化，所立者的总水平等于它的存量（`Web.StandingCensus.stock_eq`），所以增长者逐个逐步计数不多于 p q 乘 T 时所立者的总水平（`World.growth_bound`）；
  - 体现的关系项生起时从水平零开始，所以这一尺度的生起是这一尺度的增长（`World.arising_not_recurring`）。
- **边界。** 每个见证都在单位无尽细分时平衡且耗散，只缺一个前提：
  - `Asymptote` 一个取用者从一个池取用而不给回，按每个比例耗散；恰在单位于任意晚的步细分时它在任意晚的步取用（`Asymptote.exchange_recurs_iff`），池在每个细分的步下降，始终高于取用者的需要；所取用的缩小到每个量子之下。
  - `Circulation` 每步从池取用第 0 步的一整个单位，给回其余，只损失下一步的一个单位；所立者被列出，每步围住所立者，交换不息；由交换的规律，它不按任何比例耗散（`Circulation.not_dissipativeBy`）。
  - `Emission` 一个池每步取用下一步的两个单位，给回一个给当步生起的新关系项；它有普查、关系项都体现、每步被围住，并按比例耗散（给回一半）；每步都有新关系项生起，立于下一步的一个单位，即第 0 步单位的 2^-(t+1)。
  - `Alternation` 两侧轮流持有第 0 步的一整个单位与当步的一个单位；持有者取用全部并给另一侧除下一步一个单位以外的全部；它有普查、关系项都体现、每步被围住，一整个单位在任意晚的步生起；由增长的规律，它不按任何比例耗散（`Alternation.not_dissipativeBy`）。

**作者反审。**

*反驳 1：细分单位只是换记号，没有新内容？* 不是。在固定单位下，自然数的耗散蕴含每次交换至少损失一个单位，这是一个量子化的假设，此前没有陈述。见证说明：让损失随单位缩小，脊柱静止定理的其余前提都成立，其结论却不成立。所以静止定理依赖这一量子；细分之下仍成立的是损失的规律，以及按比例的损失连同最小尺度所给的界。

*反驳 2：按比例的损失是否把静止偷偷放进前提？* 它不提静止、有限或步数；它是每次转移的效率上界。单靠它不给出静止：`Emission` 按比例耗散，生起仍不息，只是尺度趋于零。静止要它连同最小尺度一起，而缺少最小尺度的情形恰是 `Asymptote` 与 `Emission`。

*反驳 3：见证满足的是静止定理的全部其余前提，还是只满足一部分？* `Emission` 与 `Alternation` 满足 `World.rests_enclosed` 与 `World.arising_opens` 的全部前提（普查、体现、耗散、每步被围住），只把平衡换为细分分辨率下的平衡；`Circulation` 满足 `World.exchange_stops` 的全部前提（所立者的普查、耗散、每步围住所立者），平衡同样换掉；`Asymptote` 对固定的封闭家族满足 `Flow.taking_stops` 的前提，只是单位细分。边界定理逐项陈述这些前提，由 Lean 检查。

*反驳 4：`Alternation` 与 `Circulation` 不按任何比例耗散，是直接验证还是推出？* 由两条规律推出：若按某比例耗散，增长的规律禁止一整个单位的生起复现，交换的规律禁止一整个单位的取用复现，而两者都复现。这同时检验了两条规律不是空的。

*反驳 5：增长的计数只数普查列表中的关系项，会不会漏掉？* 增长至少 1/p 单位的关系项在步后水平为正（R 为正），体现之下活跃，所以在普查列表中；`World.growth_not_recurring` 用的正是这一点。

*反驳 6：模块名与已有名称冲突？* 初稿的见证名 `Transfer` 与 `Becoming.Admission` 的 `Transfer` 冲突，检查器的第一次运行（回执 20261010T154024.599588Z，失败，保留）在根模块处报错；改名为 `Alternation`，它也更准确地描述两侧轮流持有的结构。其余声明已逐一对照包内所有声明，没有冲突。

**读法（AI，待 Ren）。** 有界效率之下，被围住的生成，任何固定尺度的都会停止；在围住之内只能以越来越细或越来越接近无损的方式继续。“生起不息需要开放”不依赖单位的形式是：固定尺度的生起不息需要开放，或需要损失的比例趋于零。这把开放的规律从整数的产物变为一个物理上可读的陈述。

**边界。** 离散步；量是细分后的有理数，单位不变粗；连续时间与实数量仍开放；界是否可达未证；交换的规律以固定的封闭家族陈述；按比例的损失是前提；没有伦理谓词；尚无独立审查。

### 59.1 下降、止息与储备（R1b）

2026-10-10。同一方向的下一步。R1 在每一分辨率下给出了生起的一半；静止定理还说止息停止，而储备推迟终结而不逃脱（`Web.Carries.lasts`）同样以每步至少一个单位计。

```text
Result(s): 修订 rest-at-every-resolution（同一分辨率与同一前提之下的更强结论，加上储备的最小花费，不另立记录）；新依赖
           reserve-defers-ending（储备 Web.Carries 与 Web.Carries.lasts）
Delta: Web.Loses、Web.losers；Flow.BalancesAt.loss_taken、Flow.BalancesAt.losers_lose；下降的规律 World.fall_bound、
       World.fall_not_recurring；World.ceasing_not_recurring；每一分辨率下的静止 World.rests_at_resolution；储备
       Web.CarriesAt、Web.CarriesIn、Web.carriesIn_one、Web.Carries.carriesAt、Web.CarriesAt.lasts；见证 Dwindle 与边界
       定理 reserve_needs_quantum
Supplied premises / correspondence: 下降与止息的规律与增长的规律前提相同；储备的规律另要从 T 起不被支持、活动可判定，
       并以每个活跃的步至少花去 1/p 单位为前提（最小花费，是脊柱一单位下降的无单位对应，不是推出的）
Evidence: 合并检查器回执 20261010T163746.432774Z（1662 项定理、2590 项声明审计，全部源声明公理报告为空；Resolution 110 项定理、145 项声明审计），
          外围回执 20261010T164738.513555Z；新声明先在暂存树中以已提交的核心源从前导编译，逐条 #print axioms 全部为空
Boundary: 同 §59；储备的最小花费是前提；Dwindle 只有一个关系项；尚无独立审查
Integration: 记录 rest-at-every-resolution；计划 §10 R1b；章节 §9 的脊柱表与第一部分；模块说明、根模块、包 README 与检查器的范围
```

**机制。**

- **下降的规律。** 跨过一步下降至少 1/p 单位的关系项，所失去的是被取走的：平衡之下，r t 乘步前的水平连同所得等于步后的水平连同所取，所以所取至少是下降的量（`Flow.BalancesAt.loss_taken`）。在围住它的家族中，取用至少是 R (t + 1)/p 乘下降者的数目，按比例的损失使家族至少损失取用的 1/(q+1)（`Flow.BalancesAt.losers_lose`）。所以在增长的规律的前提之下，下降者逐个逐步计数不多于 p(q+1) 乘 T 时所立者的总水平（`World.fall_bound`），不复现（`World.fall_not_recurring`）。
- **止息。** 体现的关系项止息时降到零，所以立于至少 1/p 单位者的止息是这一尺度的下降（`World.ceasing_not_recurring`）。连同 R1 的生起：在每一分辨率下，这一尺度的生起与止息都不复现（`World.rests_at_resolution`）。这是静止定理在每一分辨率下的形式：单位固定时，归于静止说的是从某步起什么都不生起、不止息；细分之下说的是，任何固定尺度的生起与止息都不复现。
- **储备。** 脊柱的储备在每个活跃而不被支持的步至少减少一个单位，所以推迟终结而不逃脱（`Web.Carries.lasts`）。只要求储备在更细单位下下降的读法（`Web.CarriesIn`）在单位固定时就是脊柱的储备（`Web.carriesIn_one`），而单位细分时储备可以永远下降。每一分辨率下的形式是 `Web.CarriesAt`：每个活跃而不被支持的步至少花去 1/p 单位；于是从 T 起不被支持时，形成活跃的步不多于 p 乘其在 T 的储备（`Web.CarriesAt.lasts`），证明用的是同一条损失的规律；脊柱的储备是 p 为一、单位固定的情形（`Web.Carries.carriesAt`）。
- **边界。** `Dwindle`：单位每步减半；一个从不被支持的形成每步都活跃；储备以当步单位计为 2^t + 1，在更细单位下每步下降（`Dwindle.carriesIn`），以第 0 步单位计是 1 + 2^-t，从上方趋于一个单位而永不到零；对任何 p，都有活跃的步花去不到 1/p 单位（`Dwindle.not_carriesAt`、`reserve_needs_quantum`）。

**作者反审。**

*反驳 7：下降的规律只是增长的规律的镜像？* 机制相同，界不同。增长者所得是被给予的，下降者所失是被取走的；按比例的损失对补给的约束是至少损失其 1/q，对取用的约束是至少损失其 1/(q+1)，所以增长的界是 p q，下降的界是 p(q+1)。两条都由同一条损失的规律推出。

*反驳 8：止息为什么需要体现？* 不体现的关系项可以水平为正而不活跃，止息只说活动停止。体现使止息时水平降到零，所以止息是下降；静止定理同样用这一前提。

*反驳 9：`Dwindle` 永远活跃而不被支持，是否违反脊柱的前提？* 它满足细分单位下的储备（`Web.CarriesIn`），只缺每步的最小花费。单位固定时 `Web.CarriesIn` 就是 `Web.Carries`（`Web.carriesIn_one`），而 `Web.Carries.lasts` 不容这样的储备永远维持活动；所以它恰在量子处。

*反驳 10：这是新结果还是同一结果的扩展？* 同一分辨率与同一前提之下的更强结论，加上储备的最小花费这一前提，归入同一记录；`World.rests_at_resolution` 是 R1 的 `World.arising_not_recurring` 与止息的合取。

**读法（AI，待 Ren）。** 有界效率之下，被围住的世界在每一分辨率下归于静止：任何固定尺度的生起与止息都停止，能继续的只有越来越细或越来越接近无损的变化。储备也是这样：没有每步的最小花费，一个不被支持的形成可以靠越来越细的储备永远活跃。

**边界。** 同 §59；储备的最小花费是前提；见证只有一个关系项；尚无独立审查。

### 59.2 按比例的损失只需对家族成立；每一尺度的最小损失只给出交换（R2）

2026-10-10。同一方向：把前提推到最弱。R1 的按比例损失原先对每个形成陈述，每条规律的证明却只用它对封闭家族的总和。本节把前提改为对家族陈述，并检验另一种减弱：只要求每一尺度的转移都有最小损失。

```text
Result(s): 修订 rest-at-every-resolution（同一记录：前提减弱；加入最小损失之下的交换律与见证 Trickle）
Delta: Flow.DissipatesBy 改为对家族陈述（封闭家族得回的至多是从它取走的 q/(q+1)），逐个形成的形式是充分条件
       Flow.DissipatesBy.of_each；R1、R1b 的每条规律以同样的陈述在这一较弱前提下成立；每一尺度的最小损失
       Flow.LosesAtSize、Flow.LosesAtEverySize、Flow.LosesAtSize.over、Flow.DissipatesOn.give_le、
       Flow.BalancesAt.takers_lose_least、Flow.exchange_bound_of_least_loss、Flow.exchange_not_recurring_of_least_loss、
       Flow.losesAtSize_of_each；quarter、quarter_eq、halving_pos；见证 Trickle 与边界定理 growth_needs_proportion
Supplied premises / correspondence: 最小损失的交换律另要脊柱的耗散（每个形成给回封闭家族的不多于所取）；m 不随步变化
Evidence: 合并检查器回执 20261010T165248.121581Z（1705 项定理、2645 项声明审计，全部源声明公理报告为空；Resolution 153 项定理、200 项声明审计），
          外围回执 20261010T165548.911356Z；新声明先在暂存树中以已提交的核心源从前导编译，逐条 #print axioms 全部为空
Boundary: 同 §59；比对家族的比例更弱而仍给出增长的规律的前提没有陈述；Trickle 的转移者不活跃；尚无独立审查
Integration: 记录 rest-at-every-resolution；计划 §10 R2；章节 §9 的脊柱表与第一部分；模块说明、根模块、包 README 与检查器的范围
```

**机制。**

- **对家族的比例。** 交换、增长与下降的规律都经过同一步：在封闭家族上，q + 1 乘补给不多于 q 乘取用（此前由逐个形成的条件求和得到）。所以 `Flow.DissipatesBy q` 现在就是这一对家族的不等式：家族的交换合起来至少失去所取的 1/(q+1)。逐个形成都如此时它成立（`Flow.DissipatesBy.of_each`），反之不然：一个形成可以无损，只要家族合起来失去一定比例。R1、R1b 的每条规律以同样的陈述在这一较弱的前提下成立；按比例耗散的见证（Asymptote、Emission）经 `of_each` 满足它，不按任何比例耗散的见证（Circulation、Alternation）连这一较弱前提也不满足，否定更强。
- **每一尺度的最小损失。** 另一种减弱：只要求取用至少 1/p 单位的转移失去至少 1/m 单位，m 不随步变化（`Flow.LosesAtSize`；对每个 p 有这样的 m 时是 `Flow.LosesAtEverySize`）。在脊柱的耗散之下（每个形成给回封闭家族的不多于所取，`Flow.DissipatesOn.give_le`），取用至少 1/p 单位的形成逐个逐步计数不多于 m 乘家族在 T 的存量（`Flow.exchange_bound_of_least_loss`），不复现（`Flow.exchange_not_recurring_of_least_loss`）。逐个形成按比例的损失给出这样的最小损失（`Flow.losesAtSize_of_each`）。
- **边界。** `Trickle`：单位每步分为四个（`quarter`）；两侧轮流持有第 0 步的一整个单位，第 t 步由 2^t 个水平为零的转移者分成 2^t 份交给另一侧，每份失去下一步的两个单位。以第 0 步单位计，每份约 2^-t，每份的损失约 2·4^-(t+1)，与所取之比趋于零。它有普查、关系项都体现、平衡、耗散、每步被围住；每一尺度都有最小损失（`Trickle.losesAtEverySize`），所以每个固定尺度的转移停止（`Trickle.exchange_stops`）；而一整个单位在任意晚的步生起，不按任何比例耗散（`growth_needs_proportion`）。

**作者反审。**

*反驳 11：把 `DissipatesBy` 改为对家族陈述，是否改变了已记录的结果？* 名称与定理的陈述不变，前提变弱，所以每条定理变强；逐个形成的形式经 `of_each` 仍给出它们。记录、模块说明与章节中“每个形成给回的至多是所取的 q/(q+1)”改为“每个封闭家族得回的至多是从它取走的 q/(q+1)”。§59 与计划 R1 的文字记录当时的形式，按原文保留。

*反驳 12：`Trickle` 的转移者不活跃，是否钻了空子？* R1 与本节的定理都不要求取用者活跃。转移者是水平为零的关系项；要求只有活跃者取用的变体没有构造。这里要说明的只是：每一尺度的最小损失不给出增长的规律。

*反驳 13：这是否说明增长的规律需要对家族的比例？* 只说明每一尺度的最小损失不够。计数转移只需最小损失；计数关系项的增长需要更多，因为一份得到可以分给任意多的转移。比对家族的比例更弱而仍给出增长的规律的前提没有陈述。

**读法（AI，待 Ren）。** 按比例的损失不是表示的偶然。增长的规律计数关系项得到多少，而一份得到可以分给任意多的转移；只有损失随所转移的量成比例，分割才不能把损失分没，每一尺度的最小损失做不到这一点。所以“被围住的生成停止”的物理前提可以读作：交换合起来失去所转移的一定比例。这也部分回答了向 Ren 提出的问题：前提现在是对家族的比例，逐个转移的效率上界只是它的充分条件。

**更正（2026-10-11，第十五次独立审查 W1、W2、W5；原文保留）。** 上面读法中“只有损失随所转移的量成比例，分割才不能把损失分没，每一尺度的最小损失做不到这一点”过度：对家族总和的任何前提都不受分割影响，审查的探针 ReplenishedLoses（被给予至少 1/p 单位的封闭家族至少失去 1/m 单位）严格弱于对家族的比例而仍给出增长的规律；分割打败的只是逐个转移的前提，Trickle 所用的是每步无界多的转移。本节开头“把前提推到最弱”应为“推向更弱”。Supplied premises 一行中“脊柱的耗散（每个形成给回封闭家族的不多于所取）”是证明所用的，脊柱的耗散本身要求取用的形成给回的至少少一个单位。见 §59.4。

**边界。** 同 §59；比对家族的比例更弱而仍给出增长的规律的前提没有陈述；Trickle 的转移者不活跃；尚无独立审查。

### 59.3 量的规律：按比例的损失为交换的总量定下最小的界（R3）

2026-10-11。同一方向：把结论推到最强。R1 至 R2 的规律都计数：取用、增长或下降至少 1/p 单位的有多少次。它们的证明都经过同一个每步的不等式：q + 1 乘余下的存量连同被取走的，不多于 q + 1 乘此前的存量（`Flow.BalancesAt.lowersTaking`）。这个不等式本身给出一条不提尺度的规律。本节在 Ren 2026-10-11 选择 A 之前完成，与 §59.4 一并提交；按 Ren，这一线作为研究笔记。

```text
Result(s): 修订 rest-at-every-resolution（同一记录：加入量的规律与其最小性；计数的规律改由它证明；Trickle 中总量无界）
Delta: refinedSum、refinedSum_invariant、refinedSum_mono、refinedSum_mul、refinedSum_marks、counts_of_amounts；
       Flow.uptake_bound、Flow.replenishment_bound、Flow.takersAbove_le、Flow.BalancesAt.gainers_le、
       Flow.BalancesAt.losers_le；World.taken_bound、World.given_bound；Flow.exchange_bound、World.growth_bound、
       World.fall_bound 改由量的规律证明（陈述不变）；powers、powers_pos、bernoulli_powers、powers_outgrow、
       quarter_pos；见证 Geometric 与 amount_sharp；Trickle.uptake、Trickle.throughput_unbounded、
       throughput_needs_proportion
Supplied premises / correspondence: 同 §59.2；量的规律只用 R T = 1 与 R (t + 1) = r t · R t
Evidence: 与 §59.4 同一回执 20261010T180948.563939Z（1788 项定理、2748 项声明审计，全部源声明公理报告为空；Resolution 207 项定理、261 项声明审计），
          外围回执 20261010T182121.048951Z；新声明先在暂存树中以已提交的核心源从前导编译，逐条 #print axioms 全部为空
Boundary: 离散步；总量以第 T 步的单位计，是有理数的和，不含实数量与连续时间；计数的界是否可达未证；尚无独立审查
Integration: 记录 rest-at-every-resolution；计划 §10 R3；章节 §9 的脊柱表与第一部分；模块说明、根模块、包 README 与检查器的范围
```

**机制。**

- **量的规律。** `refinedSum r ℓ T n` 把从 T 起 n 步的量相加：每步的量以下一步的单位计，再随单位在其后每步细分。它是以第 T + n 步的单位计的总量，除以 R (T + n) 就是以第 T 步的单位计。不变式（`refinedSum_invariant`）：每步 c 乘余下的连同该步的量不多于 c 乘此前的，则 c 乘余下的连同自 T 起的总量不多于 c 乘 T 时的量。按比例的损失给出 c = q + 1、量为被取走的（`lowersTaking`），与 c = q、量为得回的（`lowersBy`）。所以从 T 起封闭的家族被取走的总量至多是它在 T 的存量的 q + 1 倍，得回的至多 q 倍（`Flow.uptake_bound`、`Flow.replenishment_bound`）。在世界中，围住所立者的家族每步可以不同，从所立者被取走的与给予所立者的总量同样有界（`World.taken_bound`、`World.given_bound`）。这条规律不提任何尺度。
- **最小性。** `Geometric`：单位每步分为 q + 1 个，一个形成每步取走整个封闭的池，给回 q/(q+1)。池以第 t 步单位计立于 s·q^t，以第 0 步单位计立于 s·(q/(q+1))^t。q + 1 乘余下的连同被取走的总量恰是 q + 1 乘池（`Geometric.exact`）。由伯努利不等式（`bernoulli_powers`），(q+1)^n 超过 q^n 的每个倍数（`powers_outgrow`），所以对每个 m，被取走的总量到达 (q+1)s 的 1/m 之内（`amount_sharp`）。q + 1 不能换成更小的数。
- **计数是推论。** 取用至少 1/p 单位的形成每个都取走至少 1/p 单位（`Flow.takersAbove_le`）；增长至少 1/p 单位的关系项每个都被给予至少 1/p 单位（`Flow.BalancesAt.gainers_le`）；下降至少 1/p 单位的关系项每个都被取走至少 1/p 单位（`Flow.BalancesAt.losers_le`）。量子也是量：第 T 步单位的量子之和就是它们的个数乘 R (T + n)（`refinedSum_marks`）。所以计数不多于 p 乘量的界（`counts_of_amounts`）。交换、增长与下降的规律改由此证明，陈述与界都不变；生起、止息与每一固定尺度的静止随之。
- **边界。** `Trickle` 每一尺度都有最小损失，每个固定尺度的转移停止，而被取走的总量每步至少是第 0 步的一个单位，超过它的每个倍数（`Trickle.throughput_unbounded`、`throughput_needs_proportion`）。所以每一尺度的最小损失不给出量的规律。

**作者反审。**

*反驳 14：量的规律是否只是交换律的另一种写法？* 不是。交换律计数，需要尺度 1/p 与只细分的单位；量的规律为总量定界，不提尺度。它推出每个尺度的计数，反之不然：Trickle 有每个尺度的计数界，总量却无界。

*反驳 15：最小性是否只对一个特别的见证成立？* 最小性说的是常数 q + 1 不能更小：对每个 q 与每个池，有平衡、按比例 q 耗散、每步封闭的流，被取走的总量任意接近 q + 1 乘池。它不说每个流都接近这个界。

*反驳 16：交换、增长与下降的证明改经量的规律，是否改变了记录的结果？* 陈述、前提与界都不变，只是证明的路径。原来的逐步引理（`Flow.BalancesAt.takers_lose`、`gainers_lose`、`losers_lose`）保留，仍成立。

**读法（AI，待 Ren）。** 按比例的损失给出的是一个总量：被围住的家族一共能交换的，不超过它所立的 q + 1 倍。计数的规律是这个总量在某个尺度下的读数。只有每一尺度的最小损失时，总量可以无界，变化以越来越多、越来越小的份额继续。

**边界。** 同 §59；离散步；总量以有理的单位计，不含实数量与连续时间；计数的界是否可达未证；尚无独立审查。

### 59.4 算入细分：零前提的每一分辨率下的静止；第十五次独立审查（R4）

2026-10-11。向 Ren 提出的问题是：每个封闭家族失去从它取走的一定比例，是否作为理论的前提。作者列出六个选项（A 保持整单位，每次交换至少损失一个最小量；B 至 F 是比例、最小损失与无新前提的各种形式，见[来源](../../../../sources/15-codex-theory-conversations/2026-10-11-difference-in-becoming.md)）。Ren 的回答：

> A is right - because of change, there is difference, therefore there are difference in its possibility in its becoming(think in karmic way, karma passes, and that passing has to have a form of change which its reverse transformation will take another change), so in the sense of becoming, the becoming into will have relational difference, or it won't be "becoming"
>
> But for the case of 0, why can't we have it? and for the rest, they seem to be good research subjects, but this is separate matter, we can leave a note
>
> I feel there should be some elegant ways to solve it

作者的读法（AI，待 Ren）：最小差异属于生成本身，不属于表示；“the case of 0”指零前提的情形，即不添前提的每一分辨率下的静止；其余选项与第十五次独立审查的探针作为研究笔记。

```text
Result(s): 新增 rest-with-refinement-counted；修订 rest-at-every-resolution（审查更正；边界定理加入在固定单位下不平衡；作为不算入细分时的研究笔记）
Delta: Flow.withRefinement、Web.withRefinement、Flow.withRefinement_taken、Flow.withRefinement_given、
       Flow.balancesAt_iff_withRefinement、Flow.withRefinement_dissipatesOn_iff、Flow.ClosedAt.of_withRefinement、
       Flow.ClosedAt.withRefinement、Flow.Enclosed.of_withRefinement、Flow.refinement_gives_nothing、
       Flow.taking_needs_refinement；World.after 与 after_counted、after_embodied、after_balanced、after_dissipative、
       after_enclosed、after_recurs、rests_of_after；World.rests_unrefined、World.rests_refinement_counted、
       World.arising_opens_refinement_counted、World.arising_needs_refinement；Web.CarriesIn.lasts_unrefined；
       refinement_feeds_witnesses；Asymptote.not_balanced、Emission.not_balanced、Alternation.not_balanced（边界定理
       rest_needs_quantum、arising_needs_quantum 加入这一合取项）；total_map_some、mem_map_some、of_mem_map_some、refine_eq
Supplied premises / correspondence: 算入细分是一种读法（Ren 的方向，作者的展开待 Ren），不是推出的；定理对两种读法都陈述
Evidence: 合并检查器回执 20261010T180948.563939Z（1788 项定理、2748 项声明审计，全部源声明公理报告为空；Resolution 207 项定理、261 项声明审计），
          外围回执 20261010T182121.048951Z；新声明先在暂存树中以已提交的核心源从前导编译，逐条 #print axioms 全部为空
Boundary: 离散步；单位只细分；算入细分的流以 Option 为形成，不是同一种关系项的世界；尚无独立审查
Integration: 记录 rest-with-refinement-counted 与 rest-at-every-resolution；计划 §10 R4；章节 §9 的脊柱表与第一部分；
             模块说明、根模块、包 README 与检查器的范围；审查保存为 BECOMING-R1-R2-REVIEW.md
```

**机制。**

- **细分是一个给予。** 单位跨过第 t 步分为 split t + 1 个更细的单位时，在细分的单位下平衡是：下一步的水平连同被取走的，等于 (split t + 1) 乘此前的水平连同被给予的。(split t + 1) 乘水平就是水平加 split t 乘水平（`refine_eq`）。把 split t 乘水平读作又一个形成给予的，它什么也不取，平衡就成了脊柱的平衡（`Flow.balancesAt_iff_withRefinement`）。这个形成是 `Flow.withRefinement` 中的 `none`：它在场，取用为零，给每个条件 split t 乘其水平；`Web.withRefinement` 使它从不活跃，不要求、不汲取任何东西。
- **耗散排除只给不取。** 脊柱的耗散要求每个在场的形成给回封闭家族的不多于所取，取用时至少少一个单位。细分不取，所以在被耗散的封闭家族上它什么也不能给：算入细分的流在一个家族上耗散，恰当流自身的形成在其上耗散并且 split t 乘家族的存量为零（`Flow.withRefinement_dissipatesOn_iff`）。一步被围住时，细分的给予在封闭家族之外为零（封闭），在家族之内也为零（耗散），所以它什么也不给任何条件（`Flow.refinement_gives_nothing`；构造性证明，不判定成员）。
- **零前提的静止。** 于是算入细分、耗散并从 T 起每步被围住时，细分从 T 起什么也不给，在细分的单位下平衡从 T 起就是脊柱的平衡，流自身从 T 起耗散、被围住。把世界从 T 起读（`World.after`），脊柱的静止定理 `World.rests_enclosed` 给出它的静止，再读回原世界（`World.rests_of_after`）：生起与止息都不复现（`World.rests_refinement_counted`）。生起不息时，算入细分后没有一步开始每步被围住的一段（`World.arising_opens_refinement_counted`）：“生起不息需要开放”在每一分辨率下成立，前提只是脊柱的前提。
- **不算入细分。** 前提只说流自身耗散、被围住时，结论在细分什么也不给之处成立（`World.rests_unrefined`、`World.arising_needs_refinement`、`Flow.taking_needs_refinement`、储备的 `Web.CarriesIn.lasts_unrefined`）。
- **见证由细分供给。** Emission、Alternation 与 Circulation 中，以及单位在任意晚的步细分时 Asymptote 中，细分在任意晚的步有所给予；Dwindle 中细分每步给予储备（`refinement_feeds_witnesses`）。它们在固定单位下不平衡（`Asymptote.not_balanced`、`Emission.not_balanced`、`Alternation.not_balanced`；审查 W7.2）。

**第十五次独立审查的处理。** [审查](BECOMING-R1-R2-REVIEW.md)检查 R1、R1b 与 R2（`658db670`、`e79e00e5`、`de17f533`）：构建、公理、回执与计数全部正确，每条定理按陈述成立；文字有错处。逐项：

- **W1**（“计数关系项需要比例”过度）：模块说明、记录的对应与读法更正；§59.2 读法原文保留，附更正。审查的探针给出严格弱于比例而仍给出增长的规律的前提（ReplenishedLoses），按 Ren 作为研究笔记。
- **W2**（“推到最弱”）：计划 R2 行改为“推向更弱”；§59.2 原文保留，附更正。
- **W3**（中文章节把 Trickle 写反）：改为“无尽地带过（每个固定尺度的转移不复现）”。
- **W4**（量子规律的陈述缺少耗散）：模块说明、根模块、包 README 与检查器范围加入耗散。
- **W5**（最小损失交换律的耗散释义）：记录假设改为“每个取用的形成给回的至少比所取少下一步的一个单位；证明只用其不多于所取”。更弱的前提（NotGaining、只要求家族不被增益的量子规律）作为研究笔记。
- **W6、W7.1、W7.3、W7.4**（逐个形成的比例、严格更弱、Trickle 的下降与止息、界的可达）：作为研究笔记。**W7.2** 已移入核心（not_balanced）。
- **W8**：章节与记录改为“可以无尽地继续”；交换的规律以其家族的存量为界，围住之内的增长、下降、生起与止息以所立者为界，分开陈述；记录标题与 `World.rests_at_resolution` 的说明改为“每一固定尺度的静止”；根模块与包 README 改为“有见证”。
- **W9**：记录写明 Emission 每步加入一个关系项，见证只说明所缺的前提在其余前提之下是需要的；Trickle 说明中的比例改为“约四倍”。
- **W10**：“最小花费”改为“储备的最小下降”；“share”改为“比例 / proportion”；Trickle 的 carriers 改为 conduits（与储备的 Carries 分开）；记录中“读法属于 Ren”改为“读法（AI，待 Ren）”；“损失的规律”专指 `losses_bound`，量子的计数称“量子的规律”。
- **W11**（Trickle 的通道不活跃）：保留为开放项。

**作者反审。**

*反驳 17：算入细分是否把反例定义掉了？* 没有。不算入细分的规律与见证都保留并陈述（rest-at-every-resolution）；算入细分的定理对每个形成用的是脊柱原有的耗散。两种读法下的事实一致：细分在任意晚的步有所给予（`refinement_feeds_witnesses`）。变的是这一给予读作什么：表示的改变，还是一个源。Ren 的方向把它读作源，因为更细的差异也是一种生成。

*反驳 18：零前提的定理是否空洞？* 算入细分后，被围住、被耗散的世界中凡有所立之处细分什么也不给，所以每一分辨率下的静止是在单位实际上不再细分之处得到的。这正是内容：围住之内的细分是一个给予，要有来源，而被耗散的围住没有只给不取的形成。定理的力量在于不添前提：比例、最小尺度与储备的最小下降都不需要。

*反驳 19：细分在不立任何东西的条件上什么也不给，是否只管有所立的条件？* 是。细分给的是 split t 乘水平；水平为零的条件上单位的细分不改变任何量。静止定理只关于所立与活跃的关系项，所以这里不缺少什么。

**读法（AI，待 Ren）。** 每个量是一个被做出的差异。把单位分细，就是做出更细的差异，这本身是一个变化，要有所给予。被围住、被耗散的整体中没有只给不取的东西，所以围住之内不能凭空分细；分辨率的每一次细化都来自围住之外，或来自一个不被耗散的源。于是“生起不息需要开放”不依赖表示，在每一分辨率下成立，前提只是脊柱的前提。

**边界。** 离散步；单位只细分；算入细分的流以 Option 为形成，不是同一种关系项的世界（下一步：把细分作为普查中的关系项）；对“the case of 0”的读法待 Ren 确认；尚无独立审查。（“the case of 0”的读法已由 Ren 确认，见下。）

**之后（AI，待 Ren）。** Ren 随后说：“I know what "Every exchange loses at least one smallest amount" is now, it is entropy”，又说：“so that makes me to speculate if 0 is possible, if we can also derive entropy from this, if we can, spawn a new session to focus on this”。由此“0”也可读作无损的交换（损失为零）。本节的定理不依赖哪一种读法。无损的交换是否可能，每次交换的最小损失（熵）能否推出而不作前提，另开一个会话研究。

**Ren 的确认（2026-10-11）。** 作者问“0”指无损的交换还是零前提，Ren 答：

> pure thermodynamics, at atomic level, each exchange between objects holds the conservation of energy, but entropy still rise. zero premises. but for if "lossless exist", can we find a path, to figure out, and prove along the way? i think another session is working on this already

“the case of 0”指零前提，与原读法一致。须分清：算入细分不在脊柱的前提上添加前提；脊柱的耗散，即 Ren 读作熵的每次交换的最小损失，仍是脊柱的前提。它能否推出而不作前提，是 Ren 的类比所指的下一问。

**读法（AI）。** Ren 的类比分开了两种计数。微观的每次交换精确守恒能量，熵仍增加，所以一次交换精确保持的与增加的不是同一个量。照此，脊柱的损失不是守恒量的消灭，而是封闭家族内仍可用的差异的下降，正如能量守恒时可用功下降（Gouy–Stodola：损失的可用功等于环境温度乘以产生的熵）。物理上的边界：微观定律可逆，单从它们推不出每条轨迹上熵都增加；通行的说明加上计数（混合的构型远多于有序的构型）与有序的开端（过去假设）。Landauer 与 Bennett：把两个区分合并为一，至少向环境耗散 kT ln 2；不合并任何区分的一步，耗散原则上可以任意小，但只在无限慢的极限下。

**无损的交换存在时的路径（AI，候选，转给熵的会话）。**
- 历史的计数：逆转恢复水平而加长历史，所以一个历史中变化的计数不减，不需要前提（Ren 的第二条消息：“its reverse transformation will take another change”）。已有的 `endpoint-loss-and-return` 与 `ReturnConditions.lean` 中加入的计数器已给出“水平恢复而历史不恢复”的一部分，应先复用。
- 有限的围住之内精确平衡（无损）时，变化复现，没有只依赖水平而永远增加的量（离散的复现）。
- 合并的过去：有限多个构型上确定的一步之下，仍可到达的构型的个数不增。一步不合并任何两个构型时它不变，这时每个构型都复现；一步合并了两个，以后没有一步再把它们分开。于是在有限的围住之内，或者每个构型都复现（无损，没有箭头），或者某个区分永久失去（有箭头），不需要前提。这要求把一步表为构型的函数，脊柱尚无此结构。

这些是候选的陈述，不是定理；陈述与证明由熵的会话负责，本节不占用它的编号。

## 60. 每个选择之下所选前提都起约束时计数的规律（P45）

2026-10-10。按 Ren“let's aim for the strongest claim without axiom, as the first part, and add one axiom, as the following part, the no axiom part is most important and elegant”（[来源](../../../../sources/15-codex-theory-conversations/2026-10-10-zero-axiom-part-and-names.md)）与“aim a complete theory of becoming, and finish related work”继续。P41b 把计数的两项规律列为开放（§58 V4、whole-law-of-counting 的下一步）：每个选择之下所选前提都起约束时的规律，以及有限世界中除普查外每个前提都起约束时的规律。本节给出这两项。

```text
Result(s): 扩展 whole-law-of-counting（每个选择之下所选前提都起约束时、有限世界中除普查外每个前提都起约束时计数的规律）；
           修订 map-of-premises（每个前提各自起约束）与 counting-under-enclosure（开放项）；没有新的成果记录
Delta: Premises：World.Premise.Binds，每个前提各自起约束；World.Binds 改为每个前提都起约束（∀ p, p.Binds w），
       各前提的条件与原先的八项相同；前提的选择一节移到起约束之前；hatch_binds 与 finiteHatch_binds_but_census 按前提陈述。
       Counting：Web.saturated、Web.saturated_dependent、Flow.transmits_saturated、World.saturated、
       World.Premised.saturated；Tally.after_pos、World.counts_active、World.counts_arising；OpenQueue.level_le、
       EnclosedQueue.level_le；LossyQueue 与 World.lossyQueue（_dissipative、_taking、_acting、_binds、_binding）；
       RelayQueue 与 World.relayQueue（_balanced、_dissipative、_acts、_binds、_binding）；World.onceClosedQueue_binding、
       World.openQueue_saturated_binding；World.binding_counting_under、World.binding_activity_iff、
       World.binding_arising_iff、World.binding_joint_iff；World.finiteQueue_saturated_binds、
       World.finite_binding_counting。修改：只闭合一次的队列在步前或步后不空时交换（原先只看步前），
       World.onceClosedQueue_binds 不再要求没有成员加入空队，也不要求加入发生在第 T 步；World.binds_arising 只要体现起约束
Supplied premises / correspondence: 不变；起约束仍是条件有实例（P41b）
Evidence: 合并检查器回执 20261010T171040.121853Z（1734 项定理、2687 项声明审计，全部源声明公理报告为空；Premises 59、Counting 161），
          外围回执 20261010T171427.598973Z；新声明先在暂存树中从前导编译，逐条 #print axioms 全部为空
Boundary: 只是活动的计数；有限世界中每个选择之下所选前提都起约束时的规律没有陈述；更强的起约束读法仍开放（由 Ren 选择）；
          尚无独立审查
Integration: 章节第 3 条、第一部分的总陈述、§8、§9 的脊柱表与术语表；计划 P45；模块说明、根模块、包 README 与检查器的范围
```

**每个前提各自起约束。** P38c 只问每个前提都起约束的世界。按前提陈述起约束（`World.Premise.Binds`）之后，每个选择 S 都有同一个问题：在满足 S 且 S 所选的每个前提都起约束的世界中，普查的计数有哪些规律。每个前提的条件与 P38c 相同：活动需要支持在活跃者以正需要依存于某条件时起约束，平衡在水平变化时，只有活跃者给予与取用在参与者给予与取用时，耗散在参与者从封闭的家族取用时，体现在关系项生起时，普查在世界不有限时，有界传递在后代于其开始而立之步依存于某条件时。`World.Binds` 现在是每个前提都起约束，与原先八个字段的结构同义。

**规律。** 回答是 `World.counting_under` 的规律，再加至多三条（`World.binding_counting_under`）：

1. *有关系项活跃*，恰在选中活动需要支持、只有活跃者给予、只有活跃者取用或体现时（`World.binding_activity_iff`）。前三者的条件各以一个活跃的关系项为实例：需要支持的是活跃者；给予或取用的是参与者，只有活跃者给予或取用时它活跃，普查计到它（`World.counts_active`）。体现起约束时有生起，生起者步后活跃（`Tally.after_pos`）。
2. *有某个生起*，恰在选中体现时（`World.binding_arising_iff`）。体现的条件以一个生起的关系项为实例，体现之下普查把它计为开始成立（`World.binds_arising`、`World.counts_arising`）。
3. *在有关系项活跃的一步上有生起*，恰在选中体现，且选择约束计数（`World.BindsCounting`），或选中只有活跃者给予与有界传递时（`World.binding_joint_iff`）。约束计数时，没有关系项活跃的一步上没有生起，所以第 2 条的生起之步上有关系项活跃；有界传递起约束时有一个后代在某步从一个参与者传下，只有活跃者给予时这个给予者在该步活跃。

每条都是某个前提的条件的实例在计数上留下的。三个 iff 说，在别的选择之下这一条不是规律：没有选中这四个前提时，什么都不发生的计数表由一个所选前提都起约束的世界实现；不选体现时，每步一个关系项、没有生起也没有止息的计数表如此；选中体现，而选择既不约束计数、也不同时选中只有活跃者给予与有界传递时，一个关系项在第一步从无到有地生起并留下（`Queue.lone`），生起之步上没有关系项活跃。

**见证。** 反方向需要对每个满足这些规律的计数表构造一个世界，满足 S 且所选前提都起约束。

- *饱和的依存网*（`Web.saturated`）：每个关系项以其所立的水平依存于每个关系项。这样活动需要支持对任何活动成立（`Web.saturated_dependent`），水平有界时有界传递对任何流成立（`Flow.transmits_saturated`），所以满足八个前提的世界饱和之后仍满足它们（`World.Premised.saturated`）。这是最弱的依存，与 P41b 中只闭合一次的队列的网相同，只用作见证。
- *传递*（`World.relayQueue`）：在一个计数表的队列旁边，一个参与者在第 U 步从地关系项 1 取用两个单位，给地关系项 0 一个单位，失去另一个；水平随之改变，所以平衡、耗散、取用、给予与有界传递都起约束。地关系项 0 生起而不活跃，所以不满足体现，只用于不选体现的选择。选中活动需要支持、只有活跃者给予或取用时，参与者取为第 U 步的队首，在第 U 步活跃（`World.relayQueue_binding`）。
- *有损的队列*（`World.lossyQueue`）：开放队列的网饱和；跨第 U 步，队首与自身及每个在该步加入的成员各交换一个单位，再失去一个单位；一个地关系项在每步向每个关系项给予 gift t。所立者不记录这些交换与损失，所以它不平衡；它对任何 gift 都耗散，第 U 步队列不空时取用起约束，gift 恒为零时只有活跃者给予（`World.lossyQueue_binding`）。它用于选中体现而不选平衡的选择：有界传递起约束，或因为加入者在第 U 步从队首传下（U 取为第 3 条规律给出的步），或因为加入者从给予的地关系项传下。
- *只闭合一次的队列*（`World.onceClosedQueue_binding`）：选择约束计数时它满足全部八个前提且每个都起约束；选中平衡与体现而不选只有活跃者给予与取用时，有成员加入空队也不妨碍它满足其余的前提。为此它现在在步前或步后队列不空时交换（`OnceClosedQueue.exchange`），没有成员加入空队不再是耗散与起约束的条件（`World.onceClosedQueue_binds` 只要第 T 步队列不空、队首多立着的多于加入者，且某步有成员加入）。
- *饱和的开放队列*（`World.openQueue_saturated_binding`）：选中平衡、体现与只有活跃者取用，而不选只有活跃者给予与耗散时。

按体现、平衡、只有活跃者给予、取用、耗散与有界传递分情形，每个情形都由其中一个见证实现，所以 iff 的两个方向都在 Lean 中检查。

**有限世界。** 没有有限世界使每个前提都起约束（`World.Finite.not_binds`）。有限世界中除普查外每个前提都起约束时，八个前提之下计数的规律是有限世界的规律（计数表、没有关系项活跃的一步上没有生起、从第 0 步起的变化界）再加有某个生起（`World.finite_binding_counting`）。见证是 P38b 的有限队列把依存网饱和：有成员在第 T 步加入时，加入者生起而改变所立，从队首传下，步后活跃并依存于自身的所立；队首从所有位置的家族取用，这个家族封闭，耗散只许它给予少于所取的（`World.finiteQueue_saturated_binds`）。

**作者反审。**

*反驳 1：三条规律不过是把起约束的定义搬进计数？* 一半是。起约束是条件有实例，这三条就是这些实例在活动的计数上留下的；本节的内容在于“至多”与“恰”：见证表明实例不在计数上留下别的东西，三个 iff 表明每一条只在所说的选择之下是规律。

*反驳 2：见证用最弱的依存与不平衡的流，是否太容易？* 规律对所有满足选择且所选前提都起约束的世界成立，见证只需落在这个范围内。更强的依存只会使更少的世界满足前提；在某种更强的起约束读法之下规律可能更多，这一读法由 Ren 选择，仍开放（§58 V1）。有损的队列不平衡，只用于不选平衡的选择；传递不体现，只用于不选体现的选择。

*反驳 3：改动只闭合一次的队列是否改变了 P38c 的结论？* 没有。`World.binding_counting` 的陈述与证明的结构不变，只是所用的引理条件更弱；队列在步前或步后不空时交换，只使不封闭的步多了“步前空、步后不空”的步，P38c 的计数表中没有成员加入空队，所以这些步不出现。

*反驳 4：为什么有限世界中只陈述了除普查外全部起约束的情形？* 每个选择之下的有限的见证须是有限的世界；在有限世界中，只有活跃者取用且耗散时，被围住的步上只有活跃者给予（`World.Finite.acting`），所以第 3 条的条件在有限世界中会不同，需要另造有限的见证（例如 P38b 的环）。这留作开放，列入章节 §8。

**读法（AI，待 Ren）。** 每个前提起约束，只在计数上留下它的实例：有活动、有生起，以及（当生起被约束为从活动而来时）活动之步上的生起。其余的计数，前提即使都起约束也不决定。

**边界。** 离散步，活动的计数；水平与依存的计数在前提之下、有限世界中每个选择之下的起约束规律、更强的起约束读法仍开放；没有伦理谓词；名称（saturated、lossyQueue、relayQueue 等）是 AI 按 Ren 的命名准则所选，形式而描述动力学；尚无独立审查。

## 61. 反馈与所及（P42）

2026-10-10/11。Ren 写下长远的目标（[来源](../../../../sources/15-codex-theory-conversations/2026-10-10-strongest-claims-direction.md)）：

> you know the long term objectives don't you? I want to push the frontier as strong as possible, in terms of human knowledge, or have the full truth set(still need situational awareness), the universal ethics
>
> do you see answers for these questions?

AI 回答了 P39 与 P40 留下的问题（同一来源，AI 的话）：供给闭包对供给是精确的，却漏掉保护，如狼群压住会吃光森林的鹿；一般的对象是对影响形成所需者的一切影响的闭包；所在的系统还更大，`Clearing` 中栖居者在清除者的系统之内、依存之外；所以层次有四个：自身、依存、系统与整体。AI 还提出工作次序 (a)–(d)，前两项是：一个形成自身的反馈能计入哪些损失、不能计入哪些；四个层次与影响闭包。Ren 答：“continue, let's pursue the strongest claims and complete proof, i think you see the right direction, also update project context”。AI 把“i think you see the right direction”读作接受这一框架、各项回答与工作次序（来源中的 AI 读法，待 Ren）。对层级，Ren 此前写过：“i think it should be the whole, and a weaker version is within the system that one is in, then the self”（[来源](../../../../sources/15-codex-theory-conversations/2026-10-10-axiom-route-levels-and-possibilities.md)）。

本节是计划 P42（[计划 §10](BECOMING-UNIFICATION-PLAN.md#10-第一部分与第二部分--part-i-and-part-ii)），由本会话完成。它不加公理。核心新增模块 `Becoming.Feedback`，100 项定理，导入 `Becoming.Interdependence`。不用公理的结果放进第一部分（章节 §2 的“反馈与所及”与第一部分的总陈述），与路线 (b) 和 Ren 的层级的关系放进第二部分（章节 §6.10）。整合之前，P42 与 P43 一起经[第十六次独立审查](BECOMING-P42-P43-REVIEW.md)，十六项更正已处理（§62.1）；结果是五个闭包，不是四个层次，所及闭包是审查之后加上的。成果记录新增三项：
- [levels-of-closure](../../../../theories/becoming/results/records/levels-of-closure.md)
- [feedback-and-reach](../../../../theories/becoming/results/records/feedback-and-reach.md)
- [comparison-within-reach](../../../../theories/becoming/results/records/comparison-within-reach.md)

另修订四项记录，断言不变：
- [feeding-closure](../../../../theories/becoming/results/records/feeding-closure.md)、[consumption-ends-with-feeders](../../../../theories/becoming/results/records/consumption-ends-with-feeders.md)、[closure-verdict-meets-axiom](../../../../theories/becoming/results/records/closure-verdict-meets-axiom.md)：撤回把供给闭包也读作 Ren 的“the system that one is in”，为它提供所及闭包；closure-verdict-meets-axiom 由 comparison-within-reach 推进；
- [whole-first-and-bounded-centers](../../../../theories/becoming/results/records/whole-first-and-bounded-centers.md)：下一增量中的“路线 (b) 到达自身与所在的系统”改为“自身及其所依存的”。

```text
Result(s): 复用 feeding-closure（Flow.FedBy、Flow.WithinFeeding、Flow.FedClosed、Clearing.dependenceRegion_iff）、
           closure-verdict-meets-axiom（Web.retains_bounded_iff_includes）、closing-needs-net-draw
           （Flow.WithheldLevels、Web.Admits、Flow.Balances.withheld）、four-cases-of-a-part（Clearing.clearerPart、
           admitted_without、unsupported_with、Web.Includes、Web.Exceeds）、significance-retained-within-margin
           （Web.Retains、Web.Adds、Web.retains_iff_includes、Web.adds_iff_exceeds）、one-axiom-yields-g0
           （Unrestricted、bounded）、loss-beyond-a-region（Clearing.alongDependence、Clearing.loses_beyond）；
           新增上列三项
Delta: 闭包：ClosedUnder、WithinClosure（refl、trans、of_rel、mono、symm、not_rel）、closedUnder_withinClosure。层次：Web.DependsOn、
       Flow.FedFrom、Flow.Exchanges、Flow.AffectedBy、Flow.WithinInfluence、Flow.TakesPart、Flow.Shares、
       Flow.WithinSystem、Flow.Affects、Flow.WithinReach、Flow.fedClosed_iff、Flow.withinFeeding_iff、
       Flow.affectedBy_of_fedFrom、Flow.shares_of_affectedBy、Flow.withinInfluence_of_withinFeeding、
       Flow.withinSystem_of_withinInfluence、Flow.shares_symm、Flow.WithinSystem.symm、
       Flow.withinSystem_of_withinReach、Flow.withinSystem_closed；共同条件：Flow.system_whole_of_common、
       Flow.reach_whole_of_common、Flow.feeding_whole_of_common、Flow.feeding_unrestricted_of_common、
       Flow.bounded_system_whole。水平与反馈：Flow.Balances.levels_agree、support_agrees、agrees_iff_even、le_withheld、
       admits_without_taker、agrees_of_quiet、exchanges_before_of_differs、exchanges_of_differs、agrees_or_reaches_before、
       agrees_or_reaches、admits_unreached_before、admits_unreached、unregistered_beyond_influence；Flow.beyond_influence、
       Flow.unreached_within_influence、Flow.ite_part_zero、Flow.part_of_ite_pos。所及：Flow.Reaches、
       Flow.ReachesBefore（reaches）、Flow.reaches_within_closed、reaches_withinReach、reaches_withinSystem、
       unreached_within_system、own_within_reach、own_within_system。比较：Flow.Balances.retains_transfer、
       not_adds_transfer、comparison_local、comparison_within_reach、adds_iff_exceeds_of_decidable、
       not_not_adds_of_exceeds、closed_comparison；Flow.DiffersBefore、Flow.Balances.differs_before、
       comparison_within_difference。见证：Trophic（营养级联：mediates、mediated_unregistered、responsive_mixed、
       difference_reaches_forest、mixed_part 等）、Static.shares_unaffected、Clearing（alongDependence_closed、levels、
       clearer_system、sparedFlow、sparedWeb、unregistered、reaches_dweller、system_counts_dweller、system_whole、
       clearerReach、reach_middle、reach_centred、clearer_own、reach_counts_dweller、sourcePart、
       no_levels_without_source）、Margin.reach_without_misjudgment、Late.affected_without_effect
Supplied premises / correspondence: 不加公理；一般定理的前提只有平衡（Flow.Balances），部分的比较另用扣留水平
       （Flow.WithheldLevels，其余交换不变，是表示上的选择）；公理 Unrestricted 只作为三个见证的假设出现
       （Trophic.mediated_unregistered、responsive_mixed、mixed_part）；离散的步、自然数的量，部分是判定的形成家族；
       读法与名称是 AI 的，待 Ren
Evidence: 合并检查器回执 20261010T174514.186722Z（1882 项定理、2889 项声明审计、核心闭包 39 个模块、包 37 个模块，
          全部源声明公理报告为空；Lean 生成而依赖 propext 的常量 38 个，没有源声明使用）；外围回执 20261010T175236.872210Z；
          整合之前的第十六次独立审查（BECOMING-P42-P43-REVIEW.md）
Boundary: 形成知道其所及闭包、想要任何东西都不推出；意义本身仍是给定的；对每个意义正面形式的增加比较只在意义可判定处
          推出，一般只到双重否定；以扣留水平的比较固定其余交换，他者有回应的比较须给出第二个流；耦合不被度量
Integration: 计划 P42（工作次序 (a)–(b)）；推进 closure-verdict-meets-axiom：它的覆盖条件由动力学推出，只要意义覆盖部分
             所及；撤回 P40 把供给闭包读作所在系统的读法，为 Ren 的中间层级提供所及闭包（待 Ren）
```

| 声明 | 内容 |
|---|---|
| `ClosedUnder`、`WithinClosure` 与 `WithinClosure.refl`、`trans`、`of_rel`、`mono`、`symm`、`not_rel`、`closedUnder_withinClosure` | 区域对一个关系封闭：成员与之有此关系者都是成员；`g` 在 `f` 的闭包之内：含 `f` 的每个封闭区域都含 `g`。闭包自反、可传递，随关系增大，对称关系下对称，本身封闭，所以是含 `f` 的最小封闭区域 |
| `Flow.withinFeeding_iff`、`Flow.fedClosed_iff` | P40 的供给闭包就是对被供给（某一步）的闭包；对供给封闭就是对这一关系封闭 |
| `Flow.AffectedBy`、`Flow.WithinInfluence`、`Flow.Affects`、`Flow.WithinReach` | 形成受另一个影响：另一个与它所依存的条件交换；影响闭包是对受影响的闭包，即能影响它的；所及闭包是对影响的闭包，即它的交换能逐环影响的 |
| `Flow.TakesPart`、`Flow.Shares`、`Flow.WithinSystem`、`Flow.WithinSystem.symm` | 参与一个条件：依存于它或与它交换；两个形成共享一个条件：都参与它；系统是对共享的闭包，是类 |
| `Flow.withinInfluence_of_withinFeeding`、`Flow.withinSystem_of_withinInfluence`、`Flow.withinSystem_of_withinReach`、`Flow.withinSystem_closed` | 供给闭包在影响闭包之内；影响闭包与所及闭包都在系统之内；系统对影响封闭 |
| `Flow.system_whole_of_common`、`Flow.reach_whole_of_common`、`Flow.feeding_whole_of_common`、`Flow.feeding_unrestricted_of_common`、`Flow.bounded_system_whole` | 每个形成都参与一个条件时每个系统都是整体；都依存于它并与它交换时每个所及闭包都是整体；在某步都需要它并向它给予时每个供给闭包都是整体，以它为界的意义就是公理；每个中心的系统都是整体时，以系统为界的意义就是公理 |
| `Flow.Balances.levels_agree`、`support_agrees`、`agrees_iff_even`、`agrees_of_quiet`、`exchanges_before_of_differs` | 两个平衡的流在一个条件上起始、取用与给予相同，就使它相同；所以形成的支持只计入与其所依存者的交换；扣留部分时两种水平在某步于一个条件上相同，恰当此前部分向它给予的等于从它取用的；成员都不与它交换时相同；某步不同之处，必有成员在更早的步与它交换 |
| `Flow.beyond_influence`、`Flow.Balances.unregistered_beyond_influence` | 影响闭包之外的不与闭包成员所依存的条件交换；所以成员都在闭包之外的部分，在闭包之内每一步都不被计入 |
| `Flow.Reaches`、`Flow.ReachesBefore`、`Flow.Balances.admits_unreached_before`、`admits_unreached` | 部分到达一个形成：成员与它所依存的条件交换；在某步之前到达：成员在更早的步与它在该步所需的条件交换；在某步之前没有到达的，在该步有与无部分时同样被接纳 |
| `Flow.reaches_within_closed`、`reaches_withinReach`、`reaches_withinSystem`、`unreached_within_system`、`own_within_reach`、`own_within_system` | 成员在一个对影响封闭的区域之内的部分只到达区域之内；所及闭包与系统都是这样的区域；系统之外的部分到达不了系统之内；形成自身的部分在其所及闭包与系统之内 |
| `Flow.Balances.comparison_local` | 两个意义从一个立场在每步对部分此前已到达者一致时，对有与无部分的水平作同样的四个比较 |
| `Flow.Balances.comparison_within_reach` | 覆盖部分在每步之前已到达者的任何意义，有与无部分的水平恰如彼此包含那样彼此保留有意义者，两个方向都是；两者都不增加，恰当两者都不超出：公理的比较 |
| `Flow.Balances.adds_iff_exceeds_of_decidable`、`not_not_adds_of_exceeds` | 意义可判定时，增加就是超出；对每个意义，超出给出双重否定下的增加 |
| `Flow.Balances.closed_comparison` | 以对影响封闭、含部分成员的区域为界的意义，对这个部分作包含那样的比较；不用公理 |
| `Flow.DiffersBefore`、`Flow.Balances.differs_before`、`comparison_within_difference` | 两个平衡的流起始相同时，水平某步不同之处，两者在该条件上的取用或给予在更早的步不同；覆盖这一差别所及者的任何意义，对两个流作公理的比较 |
| `Trophic.mediates` | 营养级联：两个流都平衡，只有活跃者给予与取用，活动需要支持；有狼群时鹿只在第 0 步活跃，森林每步被支持；没有狼群而鹿有回应时，森林从第 2 步起不被支持；狼群不向任何条件给予，在森林的供给闭包之外、影响闭包之内；远处的形成在森林的系统之外 |
| `Trophic.mediated_unregistered`、`responsive_mixed`、`difference_reaches_forest` | 其余交换固定时狼群的部分不到达森林，森林每步有与无它都同样被接纳，部分缩小，关闭鹿，公理之下不保留；对照鹿有回应的流，同一取用是混合的；狼群的部分不到达森林，而两个流的差别在第 2 步之前到达它 |
| `Trophic.mixed_part` | 远处形成与狼群的联合部分：从远处形成的立场，以各系统为界的意义判它保留，公理之下它失去鹿 |
| `Static.shares_unaffected` | 两个形成依存于一个没有任何东西与之交换的条件：它们共享一个系统，却彼此不影响，也不在彼此的影响闭包之内 |
| `Clearing.levels`、`clearer_system`、`system_whole`、`reach_middle`、`reach_centred` | 来源在清除者的供给闭包之内，栖居者在其影响闭包之外、系统之内；每个形成都在每个形成的系统之内，以系统为界的意义就是公理；所及闭包含栖居者、不含来源，严格介于清除者与整体之间；栖居者的所及闭包只含它自己 |
| `Clearing.unregistered`、`reaches_dweller` | 清除者清除与不清除栖息地时，每步的支持都相同；它的部分到达栖居者 |
| `Clearing.system_counts_dweller`、`reach_counts_dweller` | 从清除者的立场，以各影响闭包为界，部分保留；以各系统为界，它失去栖居者；以各所及闭包为界的意义不是公理，部分却失去栖居者 |
| `Clearing.no_levels_without_source` | 其余交换不变时，没有水平平衡扣留来源之部分的流：这一比较不存在 |
| `Margin.reach_without_misjudgment` | 部分到达形成的影响闭包之外，有它时的水平包含无它时的，所以每个意义都保留：到达之外不必误判 |
| `Late.affected_without_effect` | 交换在依存之后：形成被影响、被到达，每步有与无部分都同样被接纳，部分在任何一步之前都没有到达它 |

**它回答了什么。**
- **反馈至多计入影响闭包。** AI 工作次序的 (a) 问：一个形成自身的反馈能计入哪些损失。在平衡的流中，水平只随其交换，所以形成的支持只计入与其所依存者的交换；影响闭包之外的不与闭包成员所依存的条件交换；所以成员都在影响闭包之外的部分，在闭包之内每一步都不被计入（`Flow.Balances.unregistered_beyond_influence`）。`Clearing` 中，清除者的支持不显示它是否终结栖居者。影响闭包是上界：其余交换固定时，只有直接到达形成的部分被计入（`Flow.Balances.admits_unreached`）。
- **层次有五个，方向有两个。** 次序 (b) 问四个层次与影响闭包。闭包统一了它们：供给、影响、所及与系统都是对一个关系的闭包，整体在最上面。影响闭包与所及闭包方向相反：前者是能影响形成的，后者是形成能影响的；`Clearing` 中两者互不包含（`Clearing.reach_middle`）。每个包含都有严格的见证（`Clearing.levels`、`Trophic.mediates`）。
- **比较在部分所及之内决定。** 覆盖部分所及的任何意义都给出公理的比较（`Flow.Balances.comparison_within_reach`）。这推进 P40：`Web.retains_bounded_iff_includes` 要求另一条路径接纳的每个形成都在区域之内或被第一条接纳；这里这一条件由动力学推出，只要意义覆盖部分在每步之前已到达的。更强的形式是比较的局部性（`comparison_local`）：两个意义在所及之处一致，比较就相同。任意两个流也是这样（`comparison_within_difference`），所以他者有回应时，比较在差别所及之内决定，差别含回应。
- **系统与 Ren 的中间层级。** 系统界定每个效果：在系统之内的只到达系统之内。它却不读 Ren 中间的“the system that one is in”：一个共同条件就使它成为整体（`Flow.system_whole_of_common`），系统划分形成，没有嵌套，也没有中心。为那一读法提供的是所及闭包（AI 的读法，待 Ren）：它有中心、可嵌套，指向前方，不必含中心所依存的。在它上面，Ren 的较弱版本读作：覆盖中心所及的意义，对所及之内、无它的水平存在的每个部分，在其余交换固定时给出公理的比较；`Clearing` 中这一意义不是公理，对清除者自身的部分却与公理一致（`Clearing.reach_counts_dweller`）。
- **“situational awareness”（AI 的读法，待 Ren）。** 只看重其反馈所计入者的中心，在部分只到达那个闭包之内时，对自身部分作公理的比较（`comparison_local`）；部分到达其外时可以误判，如清除者；到达其外本身不使它误判（`Margin`）。Ren 把“still need situational awareness”系于“the full truth set”。读作：要比较自身的部分，中心须知道部分在其反馈之外所到达的。

**作者反审。**
1. **两种反事实。** 以扣留水平的比较固定其余交换。它只计入部分直接的交换：狼群经鹿对森林的作用在其中不出现，狼群的部分反而缩小（`Trophic.mediated_unregistered`）；对照鹿有回应的流，它是混合的（`responsive_mixed`）。影响闭包的动机来自经他者传递的影响，而它所支持的计入定理用固定其余交换的比较：影响闭包是上界，不是所计入者的刻画。回应的流在见证中是给出的，不由动力学推出；动力学给出回应的比较列为开放。
2. **比较可以不存在。** 部分给出他者所取时，无它的水平可以不平衡任何流（`Clearing.no_levels_without_source`）。这类部分没有扣留的比较；两个流的比较（`comparison_within_difference`）仍可用，只要另给第二个流。
3. **时间的次序。** `AffectedBy`、`Reaches` 与 `Shares` 是形成层面的，不看步的先后：交换可以晚于依存（`Late.affected_without_effect`）。它们是可靠的上界。比较定理用按时间先后的 `ReachesBefore`，所以不受这一点影响；闭包本身不按时间先后，按步的闭包列为开放。
4. **正面形式的增加。** 核心是构造性的。对每个意义，“两者都不增加，恰当两者都不超出”成立；正面形式在意义可判定处成立，一般只到双重否定（`adds_iff_exceeds_of_decidable`、`not_not_adds_of_exceeds`）。缺的只是可判定性，它可以作为假设陈述。
5. **部分是判定的形成家族。** 一个形成的某一动作不与其其余交换分开；比较一个动作要经第二个流，如 `Clearing.unregistered` 中清除与不清除的两个流。
6. **共同条件不度量耦合。** `reach_whole_of_common` 的条件是布尔的，不看时间：一个共同条件就够。Ren 的“at this moment in time, the whole earth has become a highly entangled system”（[来源](../../../../sources/15-codex-theory-conversations/2026-10-10-truth-exists-opening.md)）是关于当下耦合强度的历史判断，这里不推出它，也不把它读作这一条件。
7. **知道其所及不推出。** 定理说部分到达什么，不说中心知道什么。中心怎样表示其所及闭包没有建模。
8. **读法与名称是 AI 的。** 闭包、影响闭包、所及闭包、系统、共同条件与营养级联（`Trophic`，生态学用语）是 AI 按 Ren 的命名准则所选；审查之后，`Protection`、`guards`、`verdict`、`commons`、`unguarded` 等改名（§62.1 第 16 项）。

**检查。**
- 模块在暂存区对核心编译，逐条审计全部 373 项声明（含 Lean 生成的辅助声明），公理报告全部为空；全部是项证明，不用策略、`propext`、`funext` 或经典推理。
- 合并检查器在一个分离的工作树中对加入 P42 与 P43 的包检查一次，通过：回执 20261010T174514.186722Z。`Becoming.Feedback` 的 100 项定理全部空依赖；Lean 生成而依赖 propext 的常量仍是 38 个，没有源声明使用它们。
- 外围桥接对这个核心重查（20261010T175236.872210Z），闭包中其余 42 个模块的当前字节与已通过回执一致。
- 整合之前经第十六次独立审查；处理见 §62.1。


## 62. 公理的分解（P43）

2026-10-10/11。Ren 在《Truth exist》中写道（[来源](../../../../sources/15-codex-theory-conversations/2026-10-10-truth-exists-opening.md)）：“There is a set of universal invariations, that for every universe, becoming happens, the law follows”，它是“the bases of all ethics, for all beings, in all universes”；又写道：“There is no absolute self, and the continuation goes beyond one’s cycle of life, goes beyond one’s death.” 此前 Ren 写道，自身是“a cognitive model which can not justify itself without some sort of "belief"”，“we”是“the universe/ecosystem that realizes its own existence”（[来源](../../../../sources/15-codex-theory-conversations/2026-10-10-axiom-route-levels-and-possibilities.md)），中心的“boundary”“is also with in the same cognitive system”（[来源](../../../../sources/15-codex-theory-conversations/2026-10-10-centers-within-the-dynamics.md)）。

AI 在 P42 之前提出（[来源](../../../../sources/15-codex-theory-conversations/2026-10-10-strongest-claims-direction.md)，AI 的话）：公理不由动力学推出，却可能由三个主张推出——每个行为都预设某个延续有意义；没有绝对的自身；真理对每个存在都一样；批评者必须否认的只有一步，即从“我为之行动的延续”到“延续本身”；这一步应精确陈述，在 Lean 中检查其骨架，并交独立审查。这是工作次序 (c)。AI 当时说这三个主张是 Ren 已持有的；第十六次审查把它更正为 AI 从 Ren 的话中读出的。“every act presupposes that some continuation matters”不是 Ren 的话。

本节是计划 P43，由本会话完成。核心新增模块 `Becoming.Boundaries`，47 项定理，导入 `Becoming.Feedback`；内容放进章节 §6.11。结果是公理的精确分解：它定位这一步，不降低公理的内容。审查之前的稿子把它叫作“由三个前提推出公理”，那一说法撤回（§62.1 第 3 项）。成果记录新增两项：
- [presupposition-scopes](../../../../theories/becoming/results/records/presupposition-scopes.md)
- [axiom-decomposition](../../../../theories/becoming/results/records/axiom-decomposition.md)

```text
Result(s): 复用 metaethical-core-characterization（Valuation.significant_iff）、held-lives-g0-is-centering
           （Valuation.significant_iff_held）、one-axiom-yields-g0（Unrestricted、bounded、
           Valuation.premises_of_unrestricted；公理读作边界中立）、significance-retained-within-margin
           （Web.retains_agree）、feeding-closure 与路线 (b)（Flow.WithinFeeding、Clearing.dependenceRegion_iff）、
           comparison-within-reach（Flow.Balances.comparison_within_reach、Flow.WithinReach、Flow.Shares）；
           新增上列两项
Delta: 边界与超赋值：Boundary（closure、whole、holds、of_larger、only_whole）、SuperTrue、SubTrue、BoundaryInvariant、
       superTrue_iff、boundaryInvariant_iff_determinate、superTrue_member_iff、subTrue_member、superTrue_all_iff、
       subTrue_all_iff。预设与辖域：SignificantWithin、superTrue_significantWithin_iff_union、
       superTrue_significantWithin_iff、subTrue_significantWithin_iff、subTrue_of_larger、subTrue_total_iff、
       subTrue_empty_iff、unrestricted_iff_superTrue、superTrue_level_free、bounded_closure_iff、bounded_closure_least、
       presupposition_scopes。分解：boundaryInvariant_iff_extends、boundaryInvariant_iff_all、
       boundaryInvariant_iff_conditional、not_subTrue_of_invariant、unrestricted_of_presupposed、
       unrestricted_iff_presupposed、unrestricted_iff_presupposed_along、unrestricted_iff_presupposed_of_whole、
       StandpointInvariant、unrestricted_of_standpointInvariant、boundaryInvariant_iff_standpointInvariant、
       OneCounts（sig、forms_apart）；推论 retains_agree_of_presupposed、Valuation.significant_of_presupposed。
       所及之内：Flow.presupposition_order、Flow.Balances.presupposed_comparison、presupposed_reach_comparison、
       Flow.unrestricted_iff_system_presupposed、Flow.unrestricted_iff_presupposed_of_common。见证：Clearing
       （without_presupposition、without_invariance、without_standpoint_invariance、with_fixed_boundary、levels_differ、
       own_presupposition、system_presupposition）
Supplied premises / correspondence: 覆盖（每个形成都在每个自身的某个可容许边界之内）、预设在每个立场次真、对边界不变，
       都是假设，不是 Lean 公理；沿一个关系，可容许的边界是含中心、对关系封闭的每个区域，整体在内（这一可容许性是
       实质的选择）；不用伦理前提；读法与名称是 AI 的，待 Ren；超真、次真取自超赋值（Fine 1975）与次赋值
       （Hyde 1997），依据先前知识
Evidence: 合并检查器回执 20261010T174514.186722Z；外围回执 20261010T175236.872210Z；整合之前的第十六次独立审查（BECOMING-P42-P43-REVIEW.md）
Boundary: 预设、覆盖与不变本身不推出；分解定位这一步，不降低公理；中心知道其所及闭包不推出；从意义到理由、动机或实践的
          一步不推出；G0 仍是所采用的公理，直到 Ren 接受替代，替代等待对 G0 各处用法的审计（P44）
Integration: 计划 P43（工作次序 (c)）；把公理超出预设的全部内容定位到不变的一步上，与 P39 的边界中立和 N_std 的规则
             相连；路线 (b) 与公理是同一预设的窄辖域与宽辖域
```

| 声明 | 内容 |
|---|---|
| `Boundary` 与 `closure`、`whole`、`holds`、`of_larger`、`only_whole` | 沿一个关系，形成之自身的边界：含它、对关系封闭的区域；闭包最小，整体最大，每个边界含闭包；关系越小，边界越多；一切都在闭包之内时整体是唯一的边界 |
| `SuperTrue`、`SubTrue`、`BoundaryInvariant`、`superTrue_iff`、`boundaryInvariant_iff_determinate` | 关于自身的主张，按每个可容许边界成立是超真，按某个成立是次真，按一个成立就按每个成立是对边界不变；有可容许边界时超真就是不变的次真；不变就是次真即超真 |
| `superTrue_member_iff`、`subTrue_member`、`superTrue_all_iff`、`subTrue_all_iff` | 不论怎样划都在自身之内的恰是闭包，按某种划法一切都在自身之内；整体可容许时，“自身之内的都有某性质”超真恰当一切都有，次真恰当闭包之内的都有 |
| `SignificantWithin`、`superTrue_significantWithin_iff_union`、`superTrue_significantWithin_iff`、`subTrue_significantWithin_iff` | 预设：从立场 `p`，区域之内一切的延续在每一步都有意义；超真是可容许边界之并上的意义，整体可容许时是 `p` 处的公理；沿关系次真是闭包上的意义 |
| `subTrue_of_larger`、`subTrue_total_iff`、`subTrue_empty_iff` | 沿较大的关系次真推出沿较小的；沿全关系次真恰是 `p` 处的公理，沿空关系次真恰是中心自身延续的意义 |
| `unrestricted_iff_superTrue`、`superTrue_level_free` | 公理恰是每个立场的预设沿关系超真，与沿哪个关系无关 |
| `bounded_closure_iff`、`bounded_closure_least`、`presupposition_scopes` | 以各中心闭包为界的意义，恰是不论怎样划都在自身之内者的意义，也是使每个预设次真的最小意义；同一预设，“不论怎样划”在窄辖域给出它，在宽辖域给出公理 |
| `boundaryInvariant_iff_extends`、`boundaryInvariant_iff_all`、`boundaryInvariant_iff_conditional`、`not_subTrue_of_invariant` | 整体可容许时，不变恰是从按某处划出的预设到按整体划出的预设，恰是从预设到 `p` 处公理的条件句；有了预设，它就是 `p` 处的公理；某个延续没有意义时，不变的预设在哪里都不次真 |
| `unrestricted_of_presupposed`、`unrestricted_iff_presupposed`、`unrestricted_iff_presupposed_along`、`unrestricted_iff_presupposed_of_whole` | 覆盖、次真与不变给出公理；整体可容许时公理恰是每个立场上次真且不变的预设，沿任何关系都是；每个形成都在每个中心的闭包之内时，整体是唯一的边界，公理恰是每个立场上次真的预设 |
| `StandpointInvariant`、`unrestricted_of_standpointInvariant`、`boundaryInvariant_iff_standpointInvariant`、`OneCounts.forms_apart` | 从一个立场有意义的从每个立场都有意义（N_std 的规则）；每个形成都在某个中心的闭包之内、每个预设都次真时，它给出公理，并与处处对边界不变等价；没有处处的预设时两者分开 |
| `retains_agree_of_presupposed`、`Valuation.significant_of_presupposed` | 推论：各立场的保留一致；在主张层面 G0 成立（经 `Web.retains_agree` 与 `Valuation.premises_of_unrestricted`，不计为独立结果） |
| `Flow.presupposition_order` | 沿全关系次真推出沿共享条件次真，沿共享条件推出沿影响与沿受影响，沿受影响推出沿供给，沿任何关系推出沿空关系 |
| `Flow.Balances.presupposed_comparison`、`presupposed_reach_comparison` | 预设沿一个含影响的关系次真时，对成员在中心闭包之内的每个部分作公理的比较；沿影响，是所及闭包之内的每个部分；不用不变，也不用超真（`comparison_within_reach` 的推论） |
| `Flow.unrestricted_iff_system_presupposed`、`Flow.unrestricted_iff_presupposed_of_common` | 每个中心的系统都是整体时，公理恰是每个立场上沿共享条件次真的预设；一个共同条件就使它成立 |
| `Clearing.without_presupposition`、`without_invariance`、`without_standpoint_invariance`、`with_fixed_boundary` | 每个前提都需要：没有意义时预设不变而公理不成立；以供给闭包为界的意义使预设次真而公理不成立，清除者处不变与对立场不变都不成立；只容许供给闭包时预设次真而不变，栖居者不在清除者的任何可容许边界之内，公理仍不成立 |
| `Clearing.levels_differ`、`own_presupposition`、`system_presupposition` | 次真依赖关系，超真不依赖；清除者自己的预设沿共享条件或超真时，给出它的部分失去栖居者，划在供给闭包处则有一个使部分保留的意义满足它；`Clearing` 只有一个系统，公理恰是沿共享条件处处次真的预设 |

**它回答了什么。**
- **路线 (b) 与公理是同一预设的两种辖域。** 沿一个关系，`SubTrue` 的预设是闭包上的意义；路线 (b) 以各中心闭包为界的意义，恰是确定在自身之内者的意义，也是使每个预设次真的最小意义（`bounded_closure_least`）。超真的预设是公理（`unrestricted_iff_superTrue`）。所以“不论边界怎样划”放在窄辖域给出路线 (b)，放在宽辖域给出公理（`presupposition_scopes`）；这一算子不对条件句分配。这把 P40 的路线 (b) 从供给推广到任何关系：沿空关系是一个立场自身的好，沿全关系是该立场上的公理。
- **公理的内容在哪里。** 整体可容许时，公理恰是每个立场上次真且对边界不变的预设（`unrestricted_iff_presupposed`）。不变恰是从预设到该立场上公理的条件句（`boundaryInvariant_iff_conditional`）；有了预设，它就是那里的公理（`boundaryInvariant_iff_all`）。所以这一分解没有把公理化约为更弱的或独立持有的前提：它把公理超出预设的全部内容定位到不变的一步上。P39 把公理读作边界中立：在一个立场上，这一步就是边界中立。跨立场，有了处处的预设与覆盖，它就是对立场不变，即 N_std 的规则（`boundaryInvariant_iff_standpointInvariant`）。于是核心已有的两个分解被带到延续的意义上：`Valuation.significant_iff`（种子、N_rel 与连通整体上的 N_std）与 `Valuation.significant_iff_held`（处处 S0 加 N_std）。审查之前写的“立场之间的一致是推出的，不是假设的”撤回：一致随这些前提推出，而前提之一就是这一步。
- **这一步两头都走。** 某个延续没有意义时，不变的预设在哪里都不成立（`not_subTrue_of_invariant`）：否认这一步的人可以保留预设而只在一种划法或一个立场上持有它，也可以放弃预设。这与此前审查在容差中发现的对等相同（[评价者路线的审查](EVALUATOR-GROUNDING-REVIEW.md) P3）：容差连同 Chain 承载 G0 超出 S0 的全部内容；这一步取代容差，同样承载公理超出预设的全部内容，只是一步，而不是沿分级联系的许多小步，所以不继承连锁悖论的反驳。
- **每个前提都需要。** `Clearing` 的四个见证各去掉一个前提或改变可容许类，公理都不成立。
- **所及之内的部分。** 沿影响次真的预设，对所及闭包之内的每个部分作公理的比较，不用不变，也不用超真（`presupposed_reach_comparison`）。这是 P42 比较的推论，读 Ren 的较弱版本。沿共享条件次真推出沿影响次真（`presupposition_order`），所以沿影响的前提较弱。每个中心的闭包都是整体时，不变平凡地成立（`unrestricted_iff_presupposed_of_whole`）：这一步没有被消除，而是移进了把自身的边界划成对关系封闭这一点。

**作者反审。**
1. **覆盖由构造成立。** 沿一个关系，含中心的每个封闭区域，整体在内，都算作自身的一种可容许划法，所以覆盖不用另加前提。这一可容许性是实质的选择；它也使可容许类不是对日常的、模糊的“自身”的超赋值：它没有确定的非成员（`subTrue_member`）。Ren 的“There is no absolute self”本身不给出覆盖；“we”是“the universe/ecosystem that realizes its own existence”支持把整体作为“we”的一种划法。
2. **对手在哪里。** 沿一个关系覆盖由构造成立，所以对手否认的是另一个前提。把意义奠基于已形成闭包的对手（如运作闭合），沿该闭包不对之封闭的关系否认次真，沿它对之封闭的关系否认不变，只有它也把可容许的划法限于那个闭包时才否认覆盖。模糊的自身在陌生者被每种划法排除处否认覆盖，在陌生者处于边缘处否认不变。降到零的分级权重，在闭包之内降到零否认次真，在闭包之外否认不变。现时目的的评价者否认次真。这里定位这些否认，不驳倒它们。
3. **预设与 Ren 的 belief。** Ren 写自身“can not justify itself without some sort of "belief"”，是在说自身层的限度。把这一 belief 用作前提，是 AI 的一步；沿一个关系次真，远强于某个延续有意义。
4. **不变与 Ren 的“universal invariations”。** Ren 的不变是规律跨宇宙的不变：“for every universe, becoming happens, the law follows”。“for all beings”最直接地读作对立场不变，即 N_std 的规则。把不变推广到意义，是 AI 的读法。
5. **文献只依据先前知识。** 超赋值（Fine 1975）、次赋值（Hyde 1997）、Nagel（1970）的行动者相对与行动者中立的理由、Gewirth（1978）的类属一致性原则及其批评、Parfit（1984）、Sidgwick 的实践理性的二元，都依据先前知识，没有重读原文。这里只用它们定位这一步：从行动者的立场到不偏的伦理的论证，正是在这一步上受到争议；Parfit 把没有深层的自我读作削弱自利理论的特权，对应覆盖；这一步不消解 Sidgwick 的二元，只把它定位在这一步上。
6. **层级次序（AI 的读法，待 Ren）。** Ren 的“the whole, and a weaker version is within the system that one is in, then the self”读作预设的三种读法：超真；沿影响次真，在所及闭包处；沿空关系次真，在自身处。所及闭包指向前方，所以在这一读法上，次序一路降到单纯的自身，不经过供给闭包，供给闭包在 `presupposition_order` 的另一支上。这一方向是否合适由 Ren 判断。
7. **“the continuation goes beyond one’s cycle of life, goes beyond one’s death”没有用到。** 它更自然地支持按谱系个体化与按时间先后的所及，列为开放。

**检查。**
- 模块在暂存区编译，逐条审计全部 64 项声明，公理报告全部为空；全部是项证明。
- 合并检查器回执 20261010T174514.186722Z：`Becoming.Boundaries` 的 47 项定理全部空依赖。外围回执 20261010T175236.872210Z。

### 62.1 第十六次独立审查与处理

落地时的更正（2026-10-11）：本审查在分支上称第十五次；R1–R2 的审查（[BECOMING-R1-R2-REVIEW.md](BECOMING-R1-R2-REVIEW.md)）先落地为第十五次，这里改称第十六次，内容不变。

另一 agent（Claude Opus 5.5，未参与撰写）在整合之前审查了 P42 与 P43 的暂存稿，以及应协调者要求追加的扩展（[审查](BECOMING-P42-P43-REVIEW.md)）。它对被审文件逐字节重编译，审计两个模块与扩展的全部声明，公理报告全部为空；142 个探针声明全部是项证明，没有经典推理。判断：Lean 全部成立；问题在模块层的散文、AI 的读法与框架，不在证明。下表是十六项更正的处理；表中的定理名是整合后的名称。

| 项 | 审查所见 | 处理 |
|---|---|---|
| 1 | 把系统读作 Ren 的中间层级，中间层级坍缩为整体：一个共同条件就使系统成为整体，系统是类，没有嵌套与中心（F1） | 撤回这一读法；为它提供所及闭包（`Flow.Affects`、`Flow.WithinReach`、`Flow.reaches_withinReach`、`Flow.withinSystem_of_withinReach`、`Clearing.reach_middle`、`reach_centred`、`reach_counts_dweller`），写明它指向前方、不必含供给闭包；加入 `Flow.system_whole_of_common`、`Boundary.only_whole` 与拆分后的 `Clearing.system_whole`；`Becoming.Interdependence` 的读法与章节 §6.9 加更正，P40 把供给闭包读作所在系统的读法撤回 |
| 2 | 较弱版本给出整体对系统之内每个行为的判断，说得过宽（§4） | 写明范围：所及之内、无它的水平存在的每个部分，其余交换固定；系统是整体时，前提就是该立场上的公理 |
| 3 | “由三个前提推出公理”是分解，不是化约；“derived, not assumed”不成立（F6） | 标题改为“The axiom decomposed: where its content lies”；加入 `boundaryInvariant_iff_conditional`、`boundaryInvariant_iff_determinate`、`not_subTrue_of_invariant`（审查的 `invariance_levels_down`），扩展 `boundaryInvariant_iff_all`；撤回“derived, not assumed”；写明复用 `Valuation.significant_iff`、`Valuation.significant_iff_held` 与 P39 的边界中立；补上“像容差连同 Chain 一样，承载公理在预设之外的全部内容” |
| 4 | 两种反事实：影响闭包的动机是经他者的影响，而计入与比较定理固定其余交换（F2） | 两个模块的说明加上这一点；加入见证 `Trophic.mediated_unregistered`（审查的 `protection_invisible`）、`responsive_mixed`、`Clearing.no_levels_without_source`；影响闭包的读法加“once effects pass through the support and activity of others”。审查之外另加 `Flow.Balances.comparison_within_difference`：任意两个流的比较在其差别所及之内决定，他者的回应在差别之内 |
| 5 | 扩展的标题与主张 (2)–(4) 说得过多，`Clearing.system_whole` 的位置不能编译（§6） | 标题改为“有了预设与中心覆盖，两种形式等价：那时每种都是公理”；`unrestricted_iff_presupposed_of_whole` 的说明写明“because the whole is then the only boundary”；不把 `Flow.unrestricted_iff_system_presupposed` 读作 Ren 的“highly entangled system”；主张 (4) 改为“在一个系统之内的只到达系统之内，在系统之外的到达不了系统之内”；`without_standpoint_invariance` 的说明与陈述对齐；`Clearing.system_whole` 按 `merge_ext.py` 拆分，Boundaries 另立 `Clearing.system_presupposition` |
| 6 | 对手的位置：在模块自己的边界下，闭包对手否认的是次真或不变，不是覆盖（F9） | 按审查的文字改写：沿一个关系覆盖由构造成立，各对手否认另一个前提，并加入分级权重与现时目的的评价者 |
| 7 | 对 Ren 的归属过度（§5） | “three claims Ren holds”改为“three claims the assistant read from Ren's words”；不变一条改为：“for all beings”最直接地读作对立场不变，“universal invariations”是规律跨宇宙的不变，推广到意义是 AI 的读法；预设一条加：Ren 写的是自身的限度，把 belief 用作前提是 AI 的一步 |
| 8 | 覆盖由可容许类构造进去（F7） | 改为：沿一个关系，覆盖成立，是因为含中心的每个封闭区域，整体在内，都算作自身的可容许划法；这一可容许性是实质的选择 |
| 9 | 超赋值术语（F8） | 注明超真取自 Fine 1975、次真取自 Hyde 1997；可容许类没有确定的非成员；不变就是确定（`boundaryInvariant_iff_determinate`）；两种辖域写成一个定理（`presupposition_scopes`） |
| 10 | 层级次序没有定理（F10） | 加入 `Flow.presupposition_order`（审查的 `presupposition_levels`）；次序的读法随所及闭包改为：超真；沿影响次真；沿空关系次真；`Clearing` 中沿共享条件与超真重合（`Clearing.system_presupposition`） |
| 11 | “the whole need not be admissible”有误导：沿共享条件整体总可容许 | 改为“Neither invariance nor super-truth is used” |
| 12 | “恰在其行为到达闭包之外处误判”有反例（F5，C3） | 改为：部分只到达闭包之内时作公理的比较（`Flow.Balances.comparison_local`，审查的 `verdict_local`）；到达之外时可以误判；到达之外本身不使它误判（`Margin.reach_without_misjudgment`） |
| 13 | 正面形式的增加判断（F4） | 加入 `Flow.Balances.adds_iff_exceeds_of_decidable` 与 `not_not_adds_of_exceeds`；“不推出的”改为：正面形式在意义可判定处成立，一般只到双重否定 |
| 14 | 局部的说明与陈述 | `system_retains_iff`（只给保留，公理只用来改写包含）换成不用公理、四个比较都给的 `Flow.Balances.closed_comparison`；`own_presupposition` 的说明改为“is met by a significance under which the part retains”；Boundaries 的“不推出的”加上预设本身是给定的、沿关系已带着传递；`superTrue_all_iff` 补上“where the whole is admissible” |
| 15 | 记录与复用 | P43 的记录写明复用 metaethical-core-characterization、held-lives-g0-is-centering、one-axiom-yields-g0 与 feeding-closure，增量是边界与超赋值的表述、两种辖域与对手的定位；`retains_agree_of_presupposed`、`Valuation.significant_of_presupposed` 写作推论；P42 的记录写明推进 closure-verdict-meets-axiom，`presupposed_comparison` 写作 comparison-within-reach 的推论 |
| 16 | 名称（Ren 的命名准则） | `Protection` 改为 `Trophic`（营养级联；审查建议的 `Cascade` 已是 `Becoming.Reserve` 中的命名空间）；`guards` 改为 `mediates`；判断（verdict）改为比较（`comparison_local`、`comparison_within_reach`、`closed_comparison`、`presupposed_comparison`、`presupposed_reach_comparison`）；“conduct”改为“a part's exchange”；假设名 `entangled` 改为 `connected`。审查之外，按同一准则另改：`commons`（经济学用语）改为共同条件（`system_whole_of_common` 等），`unguarded` 改为 `responsive`，`protection_unregistered` 改为 `mediated_unregistered` |

**审查之外的加强。** 比较定理改用按时间先后的 `ReachesBefore`（审查的 B4）；`closed_comparison` 不用公理；任意两个流的比较（`comparison_within_difference`、`difference_reaches_forest`）；共同条件下的所及闭包与供给闭包（`reach_whole_of_common`、`feeding_whole_of_common`、`feeding_unrestricted_of_common`：在某步每个形成都需要一个条件并向它给予时，路线 (b) 就是公理）；`Static.shares_unaffected`。

**边界。** 无伦理结论；不替 Ren 选择任何读法。仍开放：所及闭包是否读出“the system that one is in”、预设是否读出 Ren 的 belief、Ren 是否持有不变的一步（属于 Ren 的选择）；动力学给出回应的比较、按步的闭包、中心怎样表示其所及、耦合的度量（进一步的证明）；预设、覆盖与不变的根据（哲学根据）。本节与 §61 经第十六次审查；处理之后的文本尚未经独立审查。

## 63. 有限世界中与被围住时前提起约束的计数（P46）

2026-10-11。按 Ren“let's aim for the strongest claim without axiom, as the first part, and add one axiom, as the following part, the no axiom part is most important and elegant”（[来源](../../../../sources/15-codex-theory-conversations/2026-10-10-zero-axiom-part-and-names.md)）与“aim a complete theory of becoming, and finish related work”继续。P45 留下两项开放（§60 反驳 4，whole-law-of-counting 与 counting-under-enclosure 的下一步）：有限世界中每个选择之下所选前提都起约束时计数的规律，以及从某步起被围住且每个前提都起约束时的规律。本节给出这两项，并给出两者之间的一项：从某步起被围住时每个选择之下所选前提都起约束时的规律。这样，前提起约束时计数的规律在不限制、有限与从某步起被围住三类世界中都已陈述。

```text
Result(s): 扩展 counting-under-enclosure（有限世界中与从某步起被围住时，每个选择之下所选前提都起约束时计数的规律）；
           修订 whole-law-of-counting（开放项改指 counting-under-enclosure）；没有新的成果记录
Delta: Counting：World.enclosedQueue_saturated_binds、World.enclosed_binding_counting；RelayRing 与 World.relayRing
       （_balanced、_dissipative、_acts、_binds、_binding）；LossyRing 与 World.lossyRing（_dissipative、_taking、_acting、
       _binds、_binding）；Ring.exchanged、Ring.exchanging 与 World.exchangingRing（_balanced、_taking、_acting、_binds、
       _binding）；World.BoundsChange 可判定；World.finite_binding_census、World.finite_binding_counting_under、
       World.finite_binding_activity_iff、World.finite_binding_arising_iff、World.finite_binding_joint_iff；
       World.relayQueue_enclosed、World.lossyQueue_enclosed；EnclosedQueue.exchanged、EnclosedQueue.exchanging 与
       World.exchangingQueue（_balanced、_taking、_acting、_enclosed、_binds、_binding）；last_positive、Tally.occupied_from；
       EnclosedQueue.sub_add_le、store_succ_le、spare、held、sheddingWeb、shedding、spare_zero、held_outside、shedding_closed、
       shedding_flows 与 World.sheddingQueue（_balanced、_embodied、_enclosed、_level_le、_exceeds、_dissipative、_binds、
       _binding）；World.enclosed_binding_counting_under、World.enclosed_binding_activity_iff、
       World.enclosed_binding_arising_iff、World.enclosed_binding_joint_iff。已有声明不变
Supplied premises / correspondence: 不变；起约束仍是条件有实例（P41b）
Evidence: 合并检查器回执 20261011T001147.906623Z（2022 项定理、3071 项声明审计，全部源声明公理报告为空；Counting 212），外围回执 20261011T001754.342153Z；
          新声明先在暂存树中从前导编译，逐条 #print axioms 全部为空
Boundary: 只是活动的计数；更强的起约束读法仍开放（由 Ren 选择）；尚无独立审查
Integration: 章节第 3 条、第一部分的总陈述、§8、§9 的脊柱表与术语表；计划 P46；模块说明、根模块、包 README 与检查器的范围
```

**从某步起被围住且每个前提都起约束。** 全部八个前提之下，从某步起被围住时计数的规律是计数表、没有关系项活跃的一步上没有生起与从第 0 步起的变化界（`World.enclosed_counting`，P35）。每个前提都起约束时只多出有某个生起（`World.enclosed_binding_counting`），与不限于被围住时（`World.binding_counting`）和有限世界中除普查外每个前提都起约束时（`World.finite_binding_counting`）一样。见证是被围住的队列把依存网饱和：有成员在第 T 步加入时，加入者生起而改变所立，从队首传下，步后活跃并依存于自身的所立；队首从第 T 步的跨度取用，跨度封闭，耗散只许它给予少于所取的；关系项是自然数，没有有限的列表包含全部，所以普查也起约束（`World.enclosedQueue_saturated_binds`）。

**有限世界中每个选择之下。** 没有有限世界使普查起约束，所以在选中普查的选择之下，有限世界中每个性质都是规律（`World.finite_binding_census`）。不选普查时，回答是有限世界中该选择之下的规律（`World.finite_counting_under`：每步至多有某数活跃；约束计数或约束变化时没有关系项活跃的一步上没有生起；约束变化时从第 0 步起的变化界），再加至多三条（`World.finite_binding_counting_under`）：

1. *有关系项活跃*，恰在选中活动需要支持、只有活跃者给予、只有活跃者取用或体现时（`World.finite_binding_activity_iff`），与不限于有限世界时相同。
2. *有某个生起*，恰在选中体现时（`World.finite_binding_arising_iff`），也相同。
3. *在有关系项活跃的一步上有生起*，恰在选中体现，且选择约束计数或约束变化，或选中有界传递并选中只有活跃者给予、或同时选中只有活跃者取用与耗散时（`World.finite_binding_joint_iff`）。与 P45 不同之处有两个，§60 反驳 4 已预见：有限世界的每一步都被围住，所以平衡、体现与耗散本身就约束计数（`World.enclosed_binds_counting`），第 2 条的生起之步上就有关系项活跃；只有活跃者取用与耗散在被围住的步上推出只有活跃者给予（`World.Finite.acting`），所以有界传递起约束时，传下所从出的给予者在该步活跃。

每条的反方向与 P45 相同：什么都不发生的计数表、每步一个关系项而无生起的计数表、一个关系项在第一步从无到有地生起并留下（`Queue.lone`），都由满足选择且所选前提都起约束的有限世界实现。

**有限的见证。** P45 的见证有无限多个关系项，有限世界需要有限的见证。它们都按 P38b 把计数表的队列排在一圈位置上（`Ring.slot`、`Ring.counts`），并把依存网饱和：

- *环旁的传递*（`World.relayRing`）：位置 1 到第 U 步为止立着两个单位，参与者 g 在第 U 步取用这两个单位，给位置 0 一个，失去另一个；位置的所立与它是否被占无关，所以不满足体现，只用于不选体现的选择。选中活动需要支持、只有活跃者给予或取用时，g 取为第 U 步队首的位置，那时活跃（`World.relayRing_binding`）。圈按 M+1 取大小，至少有两个位置。
- *有损的环*（`World.lossyRing`）：每个位置被占时立着一；跨第 U 步，队首的位置与自身及每个开始被占的位置各交换一个单位，再失去一个单位。所立者不记录这些，所以它不平衡；它对任何计数都耗散（封闭的家族含队首的位置，队首多取了一个单位）。用于选中体现而不选平衡、并选中耗散或只有活跃者给予的选择：选中有界传递，并选中只有活跃者给予、或同时选中只有活跃者取用与耗散时，U 取为第 3 条规律给出的步；不选有界传递时，U 取为生起之后一步，那时队列不空；两个给予与取用的条件都不选时，U 取为生起之步，队首的位置不被占也可以给予与取用（`World.lossyRing_binding`）。
- *交换的环*（`World.exchangingRing`）：P38b 的平衡的环（队首的位置取用每个位置所降的、给予其所升的），在生起之后一步，队首的位置再与自身各交换一个单位，使取用起约束；它满足除耗散外的全部前提，没有成员加入空队时也满足只有活跃者给予（`World.exchangingRing_binding`）。用于选中体现、不选耗散，且不选平衡时也不选只有活跃者给予的选择。
- *饱和的有限队列*（`World.finiteQueue_saturated_binds`，P45）：选中平衡、体现与耗散，即约束变化时。

按体现、平衡、耗散、只有活跃者给予、取用与有界传递分情形，每个情形都由其中一个见证实现，所以 iff 的两个方向都在 Lean 中检查。

**从某步起被围住时每个选择之下。** 在每个选择 S 之下，从某步起被围住、S 所选前提都起约束时，计数的规律是被围住时该选择之下的规律（`World.enclosed_counting_under`：约束计数时没有关系项活跃的一步上没有生起；约束变化时从某步起的变化界，此后没有关系项活跃的一步上没有生起）再加 P45 的三条（`World.enclosed_binding_counting_under`），每条恰在与不被围住时相同的选择之下多出（`World.enclosed_binding_activity_iff`、`World.enclosed_binding_arising_iff`、`World.enclosed_binding_joint_iff`）。所以从某步起被围住时，被围住与起约束各自加上自己的规律，互不相干；有限世界中两者相干，因为那里生起之步本身也被围住。普查在这里可以起约束，因为见证有无限多个关系项。

见证都在某步之后被围住：

- *传递*（`World.relayQueue`，P45）在每一步被围住，它取用与给予的都在两个地关系项中（`World.relayQueue_enclosed`）；*有损的队列*（`World.lossyQueue`，P45）从地关系项的给予之后一步起被围住，跨度含队首与加入者（`World.lossyQueue_enclosed`）。
- *交换的队列*（`World.exchangingQueue`）：被围住的队列在生起之后一步让队首与自身再交换一个单位，使取用起约束；它在每一步被围住，满足除耗散外的全部前提，没有成员加入空队时也满足只有活跃者给予（`World.exchangingQueue_binding`）。用于选中平衡与体现而不选耗散的选择。
- *饱和的被围住的队列*（`World.enclosedQueue_saturated_binds`）：选中平衡、体现与耗散，并选中只有活跃者给予或取用时，选择约束计数，从第 0 步起的变化界由被围住时的变化界给出（`ChangeBound.from_zero`）。
- *失去多立单位的队列*（`World.sheddingQueue`）：选中平衡、体现与耗散而不选只有活跃者给予与取用时，耗散只能在封闭的步上起约束，而在平衡与体现之下封闭的家族失去一个单位，需要有所立者先多立一个单位。生起却可以只在被围住之前，从无到有，此后计数不再变化（如 `Queue.lone`）。所以先找一步 T′，那时有关系项活跃，此后没有关系项活跃的一步上没有生起（`Tally.occupied_from`：若变化界之步 T 上有关系项活跃，取 T；否则若生起不在 T 之前，取生起之步；否则取 T 之前最后一个有关系项活跃的步，`last_positive`，在有限的步中搜索）。队列在 T′ 闭合（此前每个关系项与队首各交换一个单位，没有封闭的家族），队首在 T′ 多立一个单位，跨 T′ 时失去它（`EnclosedQueue.spare`、`EnclosedQueue.held`），于是跨度在 T′ 失去的多于所给（`World.sheddingQueue_exceeds`），耗散起约束；T′ 之后它与被围住的队列相同（`EnclosedQueue.shedding_flows`）。它从 T′ 起被围住，满足选择，每个前提都起约束（`World.sheddingQueue_binds`、`World.sheddingQueue_binding`）。

**作者反审。**

*反驳 1：有限世界中的第 3 条是否只是改写了 P45？* 不是。它在有限世界中恰在更多的选择之下成立。选中体现、平衡与耗散而不选只有活跃者给予与取用时，P45 中一个关系项可以从无到有地生起（只闭合一次的队列），有限世界中不能：那里这个选择约束变化，因而没有关系项活跃的一步上没有生起。选中体现、只有活跃者取用、耗散与有界传递而不选平衡与只有活跃者给予时，P45 的有损的队列让一个地关系项给予每个关系项，传下由它而来；有限世界中每一步都封闭，给予须伴随损失，给予者于是取用而活跃。两处差别都由 `World.finite_binding_joint_iff` 确认。

*反驳 2：选中普查时“每个性质都是规律”是否空洞？* 是空洞的，而且如实：普查起约束即世界不有限，所以这类选择在有限世界中没有实例。单独陈述它（`World.finite_binding_census`），256 个选择在有限世界中就都有了回答。

*反驳 3：环旁的传递让未被占的位置立着单位，是否违背关系的读法？* 它只用于不选体现的选择，那里所立与活跃本来可以分开，体现正是使二者一致的前提。选中体现时用的是有损的环、交换的环与有限的队列，那里每个位置恰在被占时立着。

*反驳 4：从某步起被围住为何不像有限世界那样使第 3 条在更多的选择之下成立？* 因为被围住只从某步起：生起可以在被围住之前、在没有关系项活跃的一步上从无到有，被围住之后的变化界与没有关系项活跃的一步上没有生起都不触及它。失去多立单位的队列确认这一点：`Queue.lone` 由一个从第 1 步起被围住、满足平衡、体现与耗散且每个前提都起约束的世界实现。代价只是耗散的实例要放在被围住之后有所可失的一步上，这需要在有限的步中搜索那一步；变化界之步作为规律的一部分给出（P38b），所以搜索是有界的，不需要全知。

*反驳 5：多立的单位是否是为了见证而造的？* 是见证的构造，不是规律的内容：它只说明，在平衡、体现与耗散之下，一个封闭的家族要失去什么，须有所立者先立着它。规律本身（`World.enclosed_binding_counting_under`）不提到它。

**读法（AI，待 Ren）。** 起约束在计数上留下的仍只是它的实例。有限世界与从某步起被围住的世界的差别在于生起之步：有限世界的每一步都被围住，所以更多的生起须从活动而来；从某步起被围住时，生起可以在被围住之前，被围住与起约束各自加上自己的规律。

**边界。** 离散步，活动的计数；水平与依存的计数在前提之下、更强的起约束读法仍开放；没有伦理谓词；名称（relayRing、lossyRing、exchangingRing、exchangingQueue、sheddingQueue、spare、held 等）是 AI 按 Ren 的命名准则所选，形式而描述动力学；尚无独立审查。

## 64. G0 各处用法的审计（P44）

2026-10-11。Ren 的公理：“for anything, its continuation into the future has significance(doesn't have to be positive, we could argue as long as not harm), or continuation into the future needs to create more significance(being generative)”（[来源](../../../../sources/15-codex-theory-conversations/2026-10-10-wanting-continuation-one-axiom.md)）。P39 表明它推出 G0（§53）。P40 之后，AI 对“是否以这条公理替代 G0”的回答是分两步：先审计 G0 每处用法对 `living` 的读法，再替换；Ren 写道：“continue, let's pursue the strongest claims and complete proof, i think you see the right direction”（[来源](../../../../sources/15-codex-theory-conversations/2026-10-10-strongest-claims-direction.md)）。AI 把它读作接受这一次序（AI 的读法，待 Ren）。这是工作次序 (d)。

本节是计划 P44，由本会话完成。核心新增模块 `Becoming.Relevance`，30 项定理，导入 `Becoming.Boundaries` 与 `Becoming.Ranking`；桥接新增 5 项定理；内容放进章节 §6.12。结论：审计是干净的，其中一处读法是被迫的；在公理之下，以可能性读的 C 决定了 `Ranking` 留给读法选择的过度汲取，且不扣下任何事件。替换本身属于 Ren，G0 仍是所采用的公理。成果记录不新增，扩展两项：
- [one-axiom-yields-g0](../../../../theories/becoming/results/records/one-axiom-yields-g0.md)：G0 的每处用法由公理解除；公理就是对任何东西的 G0；理由前提须读在活的内容上；普遍理由不用连通。
- [ranking-under-readings](../../../../theories/becoming/results/records/ranking-under-readings.md)：可能性读法，以及可能性优先的次序。

```text
Result(s): 复用 one-axiom-yields-g0（Unrestricted、Valuation.premises_of_unrestricted、Web.paths）、ranking-under-readings
           （course、absent、undisturbed_sustains、ExtendsUnder、ComparisonUnder、wholeRun、stepwise、credited_before_loss、
           stops_credited、restraint、contest、sharing_credited、ThirdParty）、significance-retained-within-margin（Web.Retains、
           Web.Adds、Includes.retains、Retains.not_added）、four-cases-of-a-part（Web.Admits、Web.Includes、Admits.mono）、
           metaethical-core-characterization（SecuresPositiveGround、articulates、PositionedArticulation、universal_reason 的论证）、
           becoming-spine-instances（Frame.inventory、g0_iff）、relational-renewal-classification（overdraw_consuming、
           within_renewal_sustains、unfolding_dependent、malignant、sharing、winning）；扩展 one-axiom-yields-g0 与
           ranking-under-readings
Delta: 正面相关从意义读出：Frame.relevance、g0_of_unrestricted、relevance_least。公理就是对任何东西的 G0：
       unrestricted_iff_g0、Web.paths_somewhere、Web.unrestricted_iff_paths_g0。理由前提：securesPositiveGround_total、
       articulatesLiving、articulates_total、positioned_articulation_of_articulatesLiving、universal_reason_living、
       universal_reason_of_unrestricted、Widening（valuation、admitted、before、bare_forces_reason）。水平处处不低：
       Web.Includes.of_le、Web.not_added_of_le。可能性读法：Ranking.possible、possible_of_active、absent_admits_all、
       possible_extends、possible_ranks、possible_course_iff、possible_extends_iff、malignant_possible、possible_contest、
       possible_restraint、ThirdParty.possible_extends、possible_tie、readings_rank_presence、sharing_presence。可能性优先：
       possibleFirst、possibleFirst_order、possibleFirst_overdraw、possibleFirst_presence、Rest（courses、rest_ranked_below）。
       桥接：inventory_g0_of_unrestricted、relevance_inventory_iff、new_realization_of_unrestricted、
       contingent_generation_of_unrestricted、every_situated_position_has_reason_of_unrestricted
Supplied premises / correspondence: 公理（Unrestricted）只作假设出现；正面相关读作已实现的活的内容的意义、A 读在活的内容上、
       可能性读法与可能性优先的次序都是定义；C 只作定义 Comparison 出现；读法与名称是 AI 的，待 Ren
Evidence: 合并检查器回执 20261010T214440.263682Z；外围回执 20261010T222130.672025Z；对 G0 全部出现的逐处阅读（下表）
Boundary: 审计的完整性来自逐处阅读，Lean 证明的是解除引理，以及桥接已导入的三项定理的转移；从意义到理由的一步（A）仍是前提；
          比较继续用哪一种属于 Ren；G0 仍是所采用的公理，直到 Ren 接受替换
Integration: 计划 P44（工作次序 (d)）；把 P39 的“G0 推出”推到 G0 的每处用法；回答 Ranking 留下的问题的一部分：在公理之下，
             以可能性读的 C 给出整段读法把没有过度汲取或消耗的继续排在上面的每个排序，而不扣下任何事件
```

**审计。** `grep` 出 G0 在核心（9 个文件）与外围 generative-capacity（19 个文件）中的全部出现，逐处分类：

| 位置 | 用法 | 在公理之下 |
|---|---|---|
| `Metaethics`：`G0`、`Valuation.g0` | G0 的定义；主张层的 G0（`Valuation.Significant`）给出框架上的 G0 | 主张层的 G0 由公理推出（`Valuation.premises_of_unrestricted`，P39）；框架上的 G0 由 `g0_of_unrestricted` 给出，正面相关读作已实现的活的内容的意义 |
| `Metaethics`：`articulates`（A）、`positioned_articulation_of_articulates`（D）、`universal_reason` | 正面相关进入理由前提：A 以裸意义写出 | 一切都有意义时，以裸意义读的 A 给产生任何新内容的回应以理由（`articulates_total`、`Widening.bare_forces_reason`）；读在活的内容上的 A（`articulatesLiving`）给出 D（`positioned_articulation_of_articulatesLiving`）与普遍理由，且不用种子、中立或连通（`universal_reason_of_unrestricted`） |
| `Standpoints`、`Correspondence`、`Descent`、`Boundaries` | 主张层 G0 的刻画（处处 S0 加 N_std；种子加 N_rel 与 N_std）；中立不成立处 G0 不成立的反模型；P43 的推论 | 刻画是等价式，不受影响；公理推出等价式的两边（P39）；反模型定位公理所排除的有界规则 |
| `Significance` | 公理推出 G0 | 替换的依据 |
| `Ranking` | C 在两种 `living` 读法下的排序；不出现 G0 | 不受影响；在公理之下，以可能性读的 C 决定过度汲取族（见下） |
| `Interdependence`、根模块 | 只在说明中提到 G0 | 不受影响 |
| `Bridge` | 核心的 G0、C、D 按定义即外围的（`g0_iff` 等） | 新增五项，见下 |
| 外围 `GenerativeComparison.new_realization_has_positive_relevance` | 以 G0 为假设 | `new_realization_of_unrestricted` |
| 外围 `PositiveGroundUncertainty.contingent_generation_has_positive_ground`、`certified_integral_supplies_contributory_reason` | 以 G0 为假设；后者另有理由前提 `articulate : ∀ h q, positive h q → reason h` | 前者：`contingent_generation_of_unrestricted`；后者以从意义读出的正面相关实例化，理由前提保持其范围；以裸意义实例化，理由前提就要求每条历史都有理由 |
| 外围 `PositionedPositiveReason.every_situated_position_has_reason`、`g0_holds` 及其模型 | 前者以 G0 与 D 为假设；模型中 G0 成立（`g0_holds`），有通达而不背书的立场有理由，背书而无通达的没有 | `every_situated_position_has_reason_of_unrestricted`，D 读在从意义读出的正面相关上；模型中取处处成立的意义，公理成立，`g0Relevant` 就是从意义读出的正面相关（`living` 读作生成的），决定理由的仍是通达而不是背书 |
| 外围 `ProtectionPriorityRival.g0_recognizes_traded_gains`、`g0_leaves_ordering_open` | 以 G0 为假设；G0、C 与 J2 共存而 G0 不约束次序 | 前者以实例化解除；后者的模型中取处处成立的意义，公理成立，公理同样不约束次序 |
| 外围 `OpenFutureRevision.positive_ground_by_bound` | 以 G0 为假设 | 以实例化解除 |
| 外围 `RenewingFormation.event_reading_recognizes_both` | 在把每个已实现事件都算作生成的宽清单上以 G0 为假设 | 以实例化解除；公理同样给两个继续的事件以意义，区分要靠比较（见下） |
| 外围 `EvaluatorGrounding.reach_is_g0`、`self_good_derives_reachable_g0` | 推出一个立场、一条历史上的 G0 实例 | 不以 G0 为假设，不受影响 |
| 外围其余十二个文件 | 只在说明中提到 G0 | 不受影响 |

| 声明 | 内容 |
|---|---|
| `Frame.relevance`、`g0_of_unrestricted`、`relevance_least` | 从意义读出的正面相关：已实现、其延续从每个立场都有意义的活的内容；在公理之下，它在每个框架上、对 `living` 的每种读法满足 G0，且是满足 G0 的最小者，恰是已实现的活的内容 |
| `unrestricted_iff_g0`、`Web.paths_somewhere`、`Web.unrestricted_iff_paths_g0` | 在主张是形成在某步、每个主张都在某处实现的框架上，公理恰在 G0 以每个主张为活、以从每个立场的意义读正面相关时成立；每个依存网的水平路径都是这样的框架 |
| `securesPositiveGround_total`、`articulatesLiving`、`articulates_total` | 一切都有意义时，以裸意义确保根据就是确保任何新内容；以裸意义读的 A 给产生任何新内容的回应以理由，读在活的内容上的 A 给确保新的活的内容的回应以理由 |
| `Widening.bare_forces_reason` | 见证：唯一的新内容不活；以裸意义读的 A 迫使理由，读在活的内容上的 A 被空理由满足 |
| `positioned_articulation_of_articulatesLiving`、`universal_reason_living`、`universal_reason_of_unrestricted` | 读在活的内容上的 A 给出 D；主张层的 G0 加这一 A 给出普遍理由；在公理之下，不用种子、中立或连通 |
| `Web.Includes.of_le`、`Web.not_added_of_le` | 水平处处不低的路径包含另一条，从不被保留且增加排在下面 |
| `Ranking.possible`、`possible_of_active` | 可能性读法：继续的水平容许某形成之处记入它，活跃与否；在依存的继续中它记入每个活跃的形成 |
| `absent_admits_all`、`possible_extends`、`possible_ranks` | 没有焦点形成的继续每步容许每个形成；在定律族的每个定律中，超出更新地汲取者不在场的继续扩展它在场的继续，每个满足 C 的比较都把前者排得更高 |
| `possible_course_iff`、`possible_extends_iff` | 同一定律的两个继续有同样的所需；在公理之下，按可能性读法的扩展就是在定律的网上保留且增加有意义者 |
| `malignant_possible` | 恶性增殖：可能性读法把不在场排得更高，并记入它的第一个事件；逐步读法记入它，整段读法扣下它 |
| `possible_contest`、`possible_restraint`、`ThirdParty.possible_extends` | 共享扩展以消耗取胜；二元族中节制扩展过度汲取；有第三个形成时亦然，那里逐步读法不排序 |
| `possible_tie`、`readings_rank_presence`、`sharing_presence` | 在更新之内汲取的形成不增加可能性：两个继续容许同样的形成，互不扩展；两种 `living` 读法都把它的在场排得更高；共享是实例 |
| `possibleFirst`、`possibleFirst_order`、`possibleFirst_overdraw`、`possibleFirst_presence` | 先比可能性、再比一种读法所记入的事件：在可能性读法下满足 C，非自反、传递；不论第二步用哪种读法都把过度汲取者的不在场排得更高，第二步用任一种 `living` 读法都把在更新之内的在场排在不在场之上 |
| `Rest.rest_ranked_below` | 一个被支持而在第 0 步休息的形成：两个继续的可能性相同；可能性优先把休息排在不间断的活动之下 |
| 桥接 `inventory_g0_of_unrestricted`、`relevance_inventory_iff` | 在公理之下，外围的 G0 对每个清单成立，正面相关读作已实现、其延续有意义的生成内容；在框架的清单上它就是核心的 `Frame.relevance` |
| 桥接 `new_realization_of_unrestricted`、`contingent_generation_of_unrestricted`、`every_situated_position_has_reason_of_unrestricted` | 由公理推出：生成扩展的新实现、偶然的生成所确保的正面根据，以及定位表达的普遍指向（D 读在从意义读出的正面相关上） |

**它回答了什么。**
- **替换是干净的。** 每处以 G0 为假设的用法，都对任意的正面相关成立。从意义读出的正面相关在公理之下满足 G0（`g0_of_unrestricted`），且是满足 G0 的最小者，恰是已实现的活的内容（`relevance_least`），也就是外围模型中的 `g0Relevant`。所以每处用法由它解除；桥接对外围的接口作出这一点（`inventory_g0_of_unrestricted`），并写出桥接已导入的三项定理。刻画是等价式；反模型取处处成立的意义就满足公理；两者都不受影响。
- **公理就是对任何东西的 G0。** 在每个依存网的水平路径上，公理恰在 G0 以每个主张为活、以从每个立场的意义读正面相关时成立（`unrestricted_iff_g0`、`Web.unrestricted_iff_paths_g0`）。P39 说 G0 是公理限于活的主张；这里反过来：公理是 G0 扩到任何东西，并把“正面”减弱为“有意义”。所以替换不是换上一条外来的公理，而是 G0 自身的形式取最宽的辖域。
- **一处读法是被迫的。** 一切都有意义时，以裸意义读的 A 给产生任何新内容（活的与否）的回应以理由（`articulates_total`）；见证中唯一的新内容不活，裸意义的 A 仍迫使理由，读在活的内容上的 A 不迫使（`Widening.bare_forces_reason`）。所以在公理之下，正面相关必须读作活的内容的意义：意义不是正面相关，这也是 Ren“doesn't have to be positive”的一种读法。如此读，A 给出 D（`positioned_articulation_of_articulatesLiving`），普遍理由由公理推出，不用种子、N_rel、N_std 或连通（`universal_reason_of_unrestricted`）。前提卡上这四项都由公理给出，A 仍是前提。
- **在公理之下，C 以可能性读。** 可能性读法在一个继续的水平容许某形成之处记入它，活跃与否（`Ranking.possible`）。对同一定律的两个继续，在公理之下按此读法的扩展就是保留且增加有意义者（`Ranking.possible_extends_iff`），即 P39 的比较。在定律族的每个定律中，它把没有过度汲取者的继续排在有它的之上（`possible_ranks`）；在二元族中把节制排在过度汲取之上（`possible_restraint`），有第三个形成时亦然，那里逐步读法不排序（`ThirdParty.possible_extends`）；它也把共享排在以消耗取胜之上（`possible_contest`）。它不扣下任何事件：在依存的继续中它记入每个活跃的形成（`possible_of_active`），包括恶性增殖者的第一个事件；逐步读法记入这个事件，整段读法扣下它（`malignant_possible`）。`Ranking` 的结论是：要由 C 保持“没有它更好”，所比较的读法须扣下损失之前的事件；这一结论在可能性上不出现，因为排序来自部分失去的，而不是不计形成本身。
- **它不排序的。** 在更新之内汲取的形成不增加可能性：它的继续与没有它的继续容许同样的形成，互不扩展（`possible_tie`），而两种 `living` 读法都把它的在场排在上面（`readings_rank_presence`）；共享是实例（`sharing_presence`）。一般地，水平处处不低的路径从不被排在下面（`Web.not_added_of_le`），所以留下水平不低的休息与节制从不更差。
- **可能性优先。** 先比可能性、再比一种读法所记入的事件，这一比较在可能性读法下满足 C，且非自反、传递（`possibleFirst_order`）。不论第二步用哪种读法，它都把过度汲取者的不在场排在其在场之上（`possibleFirst_overdraw`）；第二步用任一种 `living` 读法，它都把在更新之内的在场排在不在场之上（`possibleFirst_presence`）。它也把不增加可能性的一次休息排在不间断的活动之下（`Rest.rest_ranked_below`）。

**作者反审。**
1. **审计的完整性来自阅读。** Lean 不能对“仓库中的每处用法”量化。这里的完整性是：`grep` 出 G0 的全部出现，逐处分类（上表）。解除引理对任意清单与任意框架成立，所以每处以 G0 为假设的定理都可实例化。只为桥接已导入的三项写出了 Lean；`ProtectionPriorityRival`、`OpenFutureRevision` 与 `RenewingFormation` 不在桥接的导入之内，以同一实例化成立，没有写成 Lean。
2. **从意义读出正面相关是定义。** 它不是推出的：AI 把 G0 的正面相关读作已实现的活的内容的意义。根据是上面被迫的一处：以裸意义读，A 就给任何新内容以理由。这一定义使正面相关恰是满足 G0 的最小者，所以它不给 G0 增加任何内容；外围已有的模型 `g0Relevant` 就是它。
3. **可能性读法计能形成的，不计形成了的。** 一个形成活着而不增加可能性，与它能活而没有活，不分高下（`possible_tie`）。推广开去，一个无物活动而水平处处足够的继续，与一个形成在更新之内兴旺的继续，也不分高下。这是 Ren 的三相（生成、中性、退化）的一种读法：不损也不增加的是中性。如果 Ren 认为“its continuation into the future has significance”说的是实际的延续，实际活着比能活更好，可能性读法就漏掉了它。
4. **可能性优先有代价。** 它是另加的前提；公理只给出可能性读法。它取回“在场优于不在场”，同时把不增加可能性的休息排在活动之下（`Rest.rest_ranked_below`），那正是 `RenewingFormation` 对按事件的 C 记下的表示限度（`event_comparison_ranks_rest_below`）。所以只要把实际的延续计在可能性之外，一次不增加可能性的停顿就算作失去；这一代价随读法而来，不是表示的偶然。
5. **整段读法扣下的是什么。** `malignant_possible` 表明，整段读法保持“没有恶性增殖更好”，靠的是扣下恶性增殖者在损失之前的事件，即把它当作从未活过。在公理之下，一切的延续都有意义，恶性增殖者的也有。可能性读法把它的不在场排得更高，而不否认它的事件有意义：排序来自它的部分失去的，即维持者的延续，而不是不计它是什么。判断落在部分的交换上，不落在谁该存在上（AI 的读法，待 Ren）。
6. **`possible_extends_iff` 的范围。** 它只对同一定律的两个继续成立，那里两者有同样的所需与需要量。不同定律的继续（如节制族的停止与过度汲取）各按自己的所需容许；`possible_restraint` 不依赖两者相同，但与保留、增加的等同需要共同的网。
7. **`Rest` 在定律族之外。** 定律族中焦点形成被支持时总是活跃的，所以休息不能在其中表示；`Rest` 与 `ThirdParty` 一样是另设的展开。

**检查。**
- 模块在暂存区编译，逐条审计全部 76 项声明（含 Lean 生成的匹配函数），公理报告全部为空；全部是项证明。桥接新增的五项在暂存区编译，公理报告为空。
- 合并检查器回执 20261010T214440.263682Z：`Becoming.Relevance` 的 30 项定理与桥接新增的 5 项定理全部空依赖。外围回执 20261010T222130.672025Z。
- P42 与 P43 先在分支上检查（回执 20261010T174514.186722Z，外围回执 20261010T175236.872210Z）；与 R3、R4 合并后，P42–P44 一次落地，上面的回执覆盖合并后的整个包。

**Ren 的选择。**
1. 是否以公理替换 G0 为所采用的公理。审计干净：替换后 G0 是定理，前提卡上的种子、S0、N_rel、N_std（与水平路径上的 C）由公理给出；A、L 与 J1–J4 仍是前提，A 读在活的内容上。
2. 正面相关是否读作已实现的活的内容的意义，作为“doesn't have to be positive”的读法。
3. 比较继续用哪一种：可能性读法，由公理自身给出，不增加可能性的在场与不在场不分高下，休息不更差；`living` 的一种读法加 C，整段读法扣下过度汲取者的事件，逐步读法不排序过度汲取与其不在场；或可能性优先，在场优于不在场，休息排在活动之下。

**边界。** 不推出伦理结论之外的东西；不替 Ren 选择读法；替换须经 Ren 接受。本节尚未经独立审查。

## 65. 所立者与依存的计数（P47）

2026-10-11。按 Ren“let's aim for the strongest claim without axiom, as the first part, and add one axiom, as the following part, the no axiom part is most important and elegant”（[来源](../../../../sources/15-codex-theory-conversations/2026-10-10-zero-axiom-part-and-names.md)）与“aim a complete theory of becoming, and finish related work”继续。P38 到 P46 给出的是活动的计数在前提之下的规律；whole-law-of-counting 与 counting-under-enclosure 的下一步都留着同一项：水平与依存的计数在前提之下（§63 的边界）。`Becoming.Population` 把同一个计数表读于三种列出：活动的普查、所立者的普查（`Web.StandingCensus`）与依存的普查（`Web.DependenceCensus`），不加前提时三者的规律都是计数表（`counting_laws`）。本节给出前提给后两者加了什么。这样，第一部分不加公理的计数规律在三个读法上都已陈述；所选前提都起约束时的规律仍只对活动陈述。

```text
Result(s): 新成果记录 counting-standing-and-dependence；修订 counting-under-enclosure 与 whole-law-of-counting（局限与下一步改指新记录）
Delta: 新核心模块 Becoming.Standing（导入 Becoming.Counting）：ceasings_congr、comings_congr、pairs、mem_pairs、
       Web.StandingCensus.length_le_stock；World.StandsObey、World.Embodied.decided、World.Embodied.standsObey_iff、
       World.Embodied.tally_of_stands；OpenQueue.sourced 与 World.sourcedQueue（_holds、_meets、_standing、_counts）；
       World.standing_counting_under、World.standing_iff_counting、World.standing_binds_iff；
       World.enclosure_bounds_standing、World.enclosed_binds_standing、World.BoundsStanding；
       EnclosedQueue.waiting、EnclosedQueue.waiting_front 与 World.waitingQueue（_holds、_meets、_standing、_counts）；
       World.embodiedQueue_stands、World.enclosed_standing_counting_under、World.enclosed_standing_bound_iff；
       World.activeRing（_holds、_meets、_counts）；World.finite_standing_counting_under、World.finite_standing_binds_iff、
       World.finite_standing_bound_iff；World.DependsObey、Queue.depending、World.dependingQueue（_premised、_census、_counts）、
       World.still_premised、World.dependence_counting、World.enclosed_dependence_counting；Ring.first、Ring.depending、
       World.dependingRing（_premised、_counts）、World.finite_dependence_counting。Becoming.Counting 只改结尾一段说明；
       已有声明不变
Supplied premises / correspondence: 不变；读于水平时水平为正可判定（自然数的比较），读于依存时要求可判定
Evidence: 合并检查器回执 20261011T003217.297180Z（2060 项定理、3126 项声明审计，全部源声明公理报告为空；Standing 38；核心闭包 41 个模块，
          包 39 个），外围回执 20261011T003646.599930Z；新模块先在暂存树中从前导编译，无警告，逐条 #print axioms 全部为空
Boundary: 所选前提都起约束时所立者与依存的计数规律、三种计数之间的联合规律没有陈述；尚无独立审查
Integration: 章节第 4 条、第一部分的总陈述、§8 的开放项与现状表、§9 的脊柱表与总数、§10 的术语表；计划 P47；
             模块说明、Counting 的结尾、根模块、包 README、检查器的核心模块列表与范围
```

**所立者与活动。** 关系项都体现时，立着就是活跃，所立者的普查就是活动的普查，两者的计数满足同样的性质（`World.Embodied.standsObey_iff`）。不选体现时，二者可以分开：由源供给的队列是 P38 的被驱动的队列，驱动者是地关系项 0，始终活跃而不立任何东西，与每个地关系项各交换一个单位；成员在队中时立着而从不活跃（`World.sourcedQueue`）。它平衡；只有源给予与取用，而源活跃；任何有限的家族之外都有一个地关系项与源交换，所以没有家族跨过任何一步封闭，耗散成立；活动需要支持与有界传递空成立（没有什么依存于什么），活动的普查是 [0]（`World.sourcedQueue_holds`）。所以它满足除体现外的全部前提，不论计数；它的所立者的普查计到队列所计的（`World.sourcedQueue_counts`）。于是在每个选择之下，所立者的计数规律就是活动的（`World.standing_counting_under`、`World.standing_iff_counting`）：计数表，以及恰在选择约束计数时，没有关系项立着的一步上没有关系项开始立着（`World.standing_binds_iff`）。

**被围住时，平衡与耗散单独约束所立者。** 流所取用与给予的是水平。在平衡与耗散之下，跨过围住所立者的步，所立者的总水平不升，任何水平变化都使它下降（`Flow.standing_never_rises`、`Flow.change_lowers`，P25）。立着的关系项至少立着一，所以所立者的数目不多于其总水平（`Web.StandingCensus.length_le_stock`）；从第 T 步起每步被围住时，所立者的任何普查自 T 起的变化，即此后任一步立着的数目连同自 T 以来有关系项开始立着或不再立着的步，不多于第 T 步所立者的总水平（`World.enclosure_bounds_standing`）。被围住而没有关系项立着的一步上，封闭家族的总水平是零，一个关系项开始立着会使它下降，所以没有关系项开始立着（`World.enclosed_binds_standing`）。两者都不需要关于活动的前提：不需要体现，不需要只有活跃者给予或取用，也不需要活动的普查。对活动，同样的界要经体现才成立（`World.enclosure_bounds_change`，P35），因为活动只在体现时随所立者而变。

所以从某步起每步被围住时，在每个选择之下，所立者的计数规律是：计数表；选择约束计数时，没有关系项立着的一步上没有关系项开始立着；选择选中平衡与耗散（`World.BoundsStanding`）时，从某步 T 起变化在一个界之内，此后没有关系项立着的一步上没有关系项开始立着（`World.enclosed_standing_counting_under`）。这是被围住时活动的规律（`World.enclosed_counting_under`，P38b）在其第二个条件中去掉体现。变化界恰在选中平衡与耗散时是所立者的规律（`World.enclosed_standing_bound_iff`），对活动则恰在选中平衡、体现与耗散时（`World.enclosed_change_bound_iff`）。

见证要在选中平衡而不选体现时满足只有活跃者给予与取用。等待的队列是 P38 的闭合的队列，只改活动：下一个加入者在立着之前就活跃，所以队首每步都活跃，队空时也是（`EnclosedQueue.waiting_front`）；给予与取用的只是队首，它活跃，所以只有活跃者给予与取用（`World.waitingQueue_holds`）。在第 0 步闭合时它每步被围住，满足除耗散与体现外的全部前提；在第 T 步闭合、从 T 起在变化界之内且此后没有成员加入空队时，耗散也成立（`World.closingQueue_dissipative`），满足除体现外的全部前提（`World.waitingQueue_meets`）。不选平衡时，体现的队列（P34）满足其余全部前提，什么都不流动，每步被围住。

**有限世界中。** 有限世界的每一步都被围住，所以平衡与耗散在那里单独约束所立者。在每个选择之下，有限世界中所立者的计数规律是：每步至多有某数立着的计数表；选择约束计数或选中平衡与耗散时，没有关系项立着的一步上没有关系项开始立着；选中平衡与耗散时，从第 0 步起的变化界（`World.finite_standing_counting_under`、`World.finite_standing_binds_iff`、`World.finite_standing_bound_iff`）。与活动相比（`World.finite_counting_under`），没有关系项立着的一步上没有关系项开始立着在平衡、并在耗散或体现连同只有活跃者给予之下成立，活动的对应一条则在平衡与体现、并在耗散或只有活跃者给予之下成立：去掉的仍只是平衡与耗散起约束之处的体现。新的有限见证是始终活跃的环：P38b 的平衡的环，每个位置始终活跃、被占时立着，满足除耗散与体现外的全部前提（`World.activeRing_holds`）；选中耗散时用有限的队列（P35），不选平衡时用体现的环。

**依存。** 要求可判定时，前提不给依存的计数加任何规律：在每个选择之下，在每个世界中、从某步起每步被围住时，以及每步至多有某数依存时在有限世界中，对计数的一个性质在依存的每个普查中成立，恰当它对每个计数表成立（`World.dependence_counting`、`World.enclosed_dependence_counting`、`World.finite_dependence_counting`）。有限世界中依存是关系项的对，至多是其数目的平方（`pairs`、`mem_pairs`）。见证是依存的队列与环：一个条件（关系项 0，或环的第一个位置）立在一、始终活跃；队列的成员或环的位置在队中时依存于它，各需它的一个单位，每个依存都被满足；没有什么流动（`World.dependingQueue`、`World.dependingRing`）。没有什么流动、水平不变时，四个关于流的前提与平衡都成立，只剩三个关于依存网的前提：活动需要支持（每个依存都被满足）、体现（只有条件活跃，也只有它立着）与普查（[0]）（`World.still_premised`）。所以这些世界满足全部八个前提，计到每个计数表。前提只在依存与活动、水平与世系一起时约束它：活动需要支持只要求活跃者所依存的支持它，有界传递只要求后代开始立着时所依存的，其亲代也依存，所需在一个界之内。

**作者反审。**

*反驳 1：体现之下所立者就是活跃者，这一半是否平凡？* 是恒等，不是新的规律，所以证明直接转用活动的定理。内容在另外两处：不选体现时，一个满足其余全部前提的世界实现所立者的每个计数表，所以没有关系项立着的一步上没有关系项开始立着在那里不是规律；被围住时，所立者的界不需要体现。

*反驳 2：源活跃而不立着，成员立着而不活跃，是否违背关系的读法？* 它只用于不选体现的选择，那里所立与活跃本来可以分开，体现正是使二者一致的前提（与 §63 反驳 3 相同）。选中体现时，所立者的规律就是活动的，不用这个见证。

*反驳 3：被围住为所立者定下界，是否已由 P25 给出？* P25 给出所立者的总水平跨过被围住的步只降不升，任何水平变化都使它下降（continued-change-needs-openness），并由此推出交换与生起的停止。这里新加的是计数的形式与它的精确范围：所立者的普查自 T 起的变化界（`World.enclosure_bounds_standing`），以及它在每个选择之下恰在选中平衡与耗散时是规律（`World.enclosed_standing_bound_iff`）；缺平衡或缺耗散时，体现的队列与在第 0 步闭合的等待的队列实现每个计数表。所以复用 P25 的结果，不重做。

*反驳 4：依存的见证是否退化？* 初稿的见证以零所需依存，什么都不立着、不活跃；一个依存什么也不需要，读者可以说它不算依存。改为条件立在一、始终活跃，每个依存需要一个单位且被满足后，定理不变，见证不再依赖零所需，所以只计所需为正的依存或只计被满足的依存，规律也相同。仍然没有什么流动：关于流的前提在那里空成立。这正是结论的内容：前提不给依存本身的计数加规律，它们约束的是依存与活动、水平与世系的联合。

*反驳 5：为何不陈述所选前提都起约束时的规律？* 对活动，起约束加上的是条件的实例（P38c、P45、P46）。对所立者与依存，要逐个选择构造使所选前提都起约束、又实现所立者或依存的每个计数表的见证。按 Ren 2026-10-11 的转向（[来源](../../../../sources/15-codex-theory-conversations/2026-10-11-zero-premise-laws.md)），选择表不再扩展：这些规律改为去掉前提、对每个世界重述，局部条件写在规律之内（[零前提计划](ZERO-PREMISE-PLAN.md)）。模块说明与记录的局限写明它们没有陈述。

*反驳 6：三种计数各自的规律是否就是整体的计数规律？* 不是。三种计数之间有联合规律，例如在平衡与只有活跃者给予之下，没有关系项活跃的一步上没有关系项开始立着；这里没有陈述，记录的局限写明。

**读法（AI，待 Ren）。** 被围住的展开所耗去的是立着的东西：平衡与耗散约束的是水平，所以所立者先受约束，活动只在体现时随之受约束。依存是关系的形状，前提不单独约束它的形成与消解，只在它与活动、水平与世系相遇处约束。

**边界。** 离散步，每步有限的所立者与依存；所选前提都起约束时所立者与依存的计数规律、三种计数之间的联合规律没有陈述，按 Ren 的转向不再作为选择表扩展；更强的起约束读法仍开放（由 Ren 选择）；没有伦理谓词，不评价立起、不再立着、形成或消解；名称（StandsObey、DependsObey、BoundsStanding、sourcedQueue、waitingQueue、activeRing、dependingQueue、dependingRing、pairs）是 AI 按 Ren 的命名准则所选，形式而描述动力学；尚无独立审查。

## 66. 一步的规律，条件在规律之内（P48）

2026-10-11。按 Ren 的转向：“stop extending the premise-selection tables. New goal: remove premises and derive the most general versions, zero premises first”（[来源](../../../../sources/15-codex-theory-conversations/2026-10-11-zero-premise-laws.md)）；又按 Ren 同日“一起先完成一个统一的理论”的指示（[来源](../../../../sources/15-codex-theory-conversations/2026-10-11-one-unified-theory-together.md)）。本节把 Ren 先点名的四条规律对每个世界重述：静止与持续变化需要开放、不再存在需要生起、封闭约束变化、生起需要活跃的给予者。每条规律里，证明用到的条件写在规律之内，是关于该世界在证明用到它的那些步与关系项上的事实。所作的一步是局部化，不推出任何前提：表示之内各前提仍是偶然的、彼此独立的（`World.contingent`、`World.independent`）。新核心模块 `Becoming.Locality` 导入 `Becoming.Dissipation`，`Becoming.Roles` 导入它。撤回的联合规律原编号 P48，它的三个引理在这里被改写为局部规律。

```text
Result(s): 新成果记录 laws-of-one-step；修订 continued-change-needs-openness、counting-under-enclosure、
           whole-law-of-counting、counting-standing-and-dependence、ceasing-needs-arising、life-as-condition-of-life
           （证明改经新的规律，局限与下一步改指新记录）
Delta: 新核心模块 Becoming.Locality（导入 Becoming.Dissipation）：
       pos_iff_lt、lt_iff_pos、exists_lt_of_total_lt、rises_or_le、unmet_or_lower、unmet_from、recurs_iff_unmet；
       Web.StandingCensus、Web.StandingCensus.stock_eq（自 Openness 移来）、Web.StandingCensus.length_le_stock（自 Standing 移来）；
       Flow.BalancesOn、Flow.Balances.on、Flow.balances_iff_on、Flow.BalancesOn.over；
       Flow.BalancesOn.comesToStand_iff、ceasesToStand_iff、rise_given、fall_taken、rises_iff_gives、
       Flow.DissipatesOn.still_untaken；Flow.BalancesOn.runs_down、taking_lowers、fall_lowers、rise_lowers、
       comes_from_standing；Flow.RunsDownOn、Flow.RunsDown、Flow.RunsDownClosed、Flow.RunsDownOn.changes_iff、
       exchanges_iff、stock_eq、Flow.RunsDown.standing_le、changes_iff、Flow.RunsDownClosed.exchanges_iff、runsDown、
       Flow.rise_of_standing、Flow.change_recurs_iff、Flow.exchange_recurs_iff；Flow.RunsDown.rise_zero、fall_pos_iff、
       lowers_mark、Flow.RunsDownOn.takers_le_fall、Flow.standing_bounds_change、Flow.runsDown_bounds_change、
       Flow.runsDown_change_bound；Flow.BalancesOn.arises_iff、arises_given；
       Covers、ListsAt、NoneComes、accumulates_or、stays_failing_within、came_between、Covers.within、
       cohort_closes_iff、ceasing_needs_arising、Covers.coming_from_of_ceasing、coming_of_ceasing_covered、Listed.covered、
       not_not_all、ceases_once、Covers.ceasing_steps_within、ceasing_steps_found、Covers.ceasing_not_recurring、
       Covers.not_not_coming_from（不再存在需要生起一节由“0 axiom completeness”会话起草并验证，此处整合）。
       推论改证（陈述不变）：Web.Embodied.arises_given（Roles）；Flow.fall_lowers_on、standing_runs_down、
       standing_never_rises、change_lowers、stills、exchange_lowers、exchanges_finitely、World.arising_of_ceasing、
       Web.StandingCensus.coming_of_ceasing，新增 Flow.AroundStanding.runsDownClosed（Openness）；
       World.enclosure_bounds_change、taking_binds_counting、enclosed_binds_counting（Counting）；
       World.enclosure_bounds_standing、enclosed_binds_standing（Standing）
Supplied premises / correspondence: 无；每条规律的条件写在规律之内
Evidence: 合并检查器回执 20261011T071749.484228Z（2171 项定理、3257 项声明审计，全部源声明公理报告为空；Locality 57；核心闭包 43 个模块，
          包 41 个），外围回执 20261011T071753.574921Z；先在暂存树中从前导编译，无警告，逐条 #print axioms 全部为空
Boundary: 超出整单位的量、连续时间未在此检验；规律 3 与规律 1 的复现用所立者的普查；尚无独立审查
Integration: 章节第 4 条、第一部分的总陈述、§8 的开放项与现状表、§9 的脊柱表与总数、§10 的术语表；计划 P48；零前提计划；
             模块说明、根模块、包 README、检查器的核心模块列表与范围
```

**一步的平衡。** 流跨过一步在一个家族上平衡：每个成员步后的水平连同被取的，等于步前的水平连同被给的（`Flow.BalancesOn`）。平衡就是每一步、每个家族上的平衡（`Flow.balances_iff_on`）；平衡的流的每个证明只在它用到的步与条件上需要它。

**生起需要活跃的给予者。** 一个条件跨过一步平衡时，它开始立着，恰当它此前立在零，且被给的多于被取的（`Flow.BalancesOn.comesToStand_iff`）。它不再立着，恰当它此前立着，且被取的等于它所有的连同被给的（`Flow.BalancesOn.ceasesToStand_iff`）。跨过没有从家族取用的一步，平衡的家族中有成员上升，恰当有参与者给予它（`Flow.BalancesOn.rises_iff_gives`）；家族上的耗散排除这一点：给予须以从家族取用为条件（`Flow.DissipatesOn.still_untaken`）。一个关系项在一步的两端都体现、只有活跃者给予它时，它生起恰当它开始立着，所以由一个活跃的、不是它自己的给予者给予（`Flow.BalancesOn.arises_iff`、`Flow.BalancesOn.arises_given`）。跨过一个包含它的家族被平衡与耗散的一步，不会从无中开始立着（`Flow.BalancesOn.comes_from_standing`）。`Web.Embodied.arises_given`、`World.taking_binds_counting`、`World.enclosed_binds_counting` 与 P47 的 `World.enclosed_binds_standing` 改为它的推论。撤回的联合规律的三个引理就是两个当且仅当与 `still_untaken`。

**静止。** 家族跨过一步时满足三点：不重复地包含步前或步后立着的每个条件，流在它上面平衡，并在它上面耗散。这时称家族跨过该步下降（`Flow.RunsDownOn`），条件中没有封闭。跨过这样的一步，有条件的水平改变，恰当家族的总水平下降（`Flow.RunsDownOn.changes_iff`）；家族也封闭时，有参与者取用或给予，也恰在此时（`Flow.RunsDownOn.exchanges_iff`）。持续变化需要开放，取确切形式：所立者有普查时，水平在任意晚的步改变，恰当它在任意晚的、所立者不下降的步上改变（`Flow.change_recurs_iff`）；交换连同封闭也一样（`Flow.exchange_recurs_iff`）。一般形式是 `recurs_iff_unmet`，有三个条件：在条件之下事件使一个量下降；在条件之下这个量不上升；它的每次上升都是事件。这时事件复现，恰当它在不满足条件的步上复现。找那一步的搜索有界，不用判定。`Flow.stills`、`Flow.exchanges_finitely`、`standing_never_rises`、`change_lowers`、`exchange_lowers`、`standing_runs_down` 与 `fall_lowers_on` 改为它的推论，`Becoming.Openness` 的静止定理随之。

**下降约束变化。** 任何一段步，不加条件：末步立着的，连同总水平下降的步，不多于首步的总水平连同它在这一段上升的全部（`Flow.standing_bounds_change`）。总水平只在所立者不下降的步上上升，所以在下降的各步上，末步立着的连同有水平改变的步不多于首步的总水平；这不需要判定水平是否改变（`Flow.runsDown_bounds_change`）。对任何计数的变化界见 `Flow.runsDown_change_bound`；`World.enclosure_bounds_change`（P46）与 `World.enclosure_bounds_standing`（P47）是它的推论。Ren 把这条称为“封闭约束变化”；约束变化的是下降，即在包含所立者的家族上平衡与耗散，封闭是前提给出下降的方式。

**不再存在需要生起。** 本节一部分由“0 axiom completeness”会话起草并验证，此处整合。一个列表覆盖一步上成立者，指那里每个成立的成员都在列表上（`Covers`）。对任何有限列表，段末它成立的连同这一段上的不再成立，等于段首它成立的，恰当这一段上它没有成员开始成立（`cohort_closes_iff`）。一个列表恰好列出第 N 步成立者（`ListsAt`），N 之后没有开始成立时，段末成立的连同自 N 以来不再成立的，恰好等于第 N 步成立的数目（`ceasing_needs_arising`）。只要在任意晚的步有列表覆盖成立者，不再成立的复现就需要开始成立的复现（`coming_of_ceasing_covered`）；普查覆盖每一步（`Listed.covered`），普查定律是它的推论，`World.arising_of_ceasing` 与 `Web.StandingCensus.coming_of_ceasing` 改经它证明。不用判定时：一个列表覆盖第 N 步，N 之后没有开始成立，则不再成立不复现（`Covers.ceasing_steps_within`、`Covers.ceasing_not_recurring`、`Covers.not_not_coming_from`）。

**表示的承诺（Ren 的第 4 项）。** 以下由陈述与证明读出：
- **可判定。** 规律 1、3、4 不判定世界的任何谓词，证明只判定数的大小；规律 2 的确切计数需要标记，它的“不复现”形式不需要。
- **整单位。** 规律 1 与 4 的一步当且仅当只用加法与次序。规律 1 的复现与规律 3 的界用最小差异：耗散中的 sign 项，每个取用的形成至少失去一个单位（Ren 的选项 A）。超出整单位的量下各条是否成立，这里尚未检验；静止由分辨率一线覆盖（R4：把细分算作给予时，每一分辨率下都静止）。
- **时间。** 较粗的步由局部化的 `Sampling` 检验（落地队列第 7 项，来自“0 axiom completeness”会话）：每个关系项只列出一次时，家族上的平衡与耗散跨过一个粗步内的各细步合成；家族下降只需要在粗步两端包含所立者；只有活跃者给予与取用仍依步而定。
- **有限。** 所立者的普查（每步有限多立着）只被规律 1 的复现与规律 3 用到，作用只是使每步的总水平是一个数；一步的规律不需要普查。

**作者反审。**

*反驳 1：把前提搬进规律之内，是否只是改写？* 不只是。第一，得到原来没有的确切形式：一步上水平改变当且仅当总水平下降，复现当且仅当在不满足条件的步上复现，而且后者用有界搜索给出那一步，不用判定。第二，条件比把前提限于那些步更弱：下降不需要封闭，耗散只在那一个家族上；规律 2 只需要一步的列表，或任意晚的步上的覆盖列表，不需要普查；规律 3 对所立者不需要体现，对活动只需要生起与不再活跃者的体现。第三，选择结果改经这些规律证明，所以新模块是来源，不是包装。

*反驳 2：每条都是“Y 当且仅当 Z”吗？* 规律 1、4 与规律 2 的群体定律是当且仅当，复现定律也是。规律 3 是不等式：它的确切形式是 `over_stretch` 的恒等式，连同一步的当且仅当。界按界陈述，并写出它所来自的恒等式。

*反驳 3：所立者的普查是否偷渡了有限？* 它只用来使每步的总水平是一个数。下降的步上家族本身给出这个数，但在不下降的步上，立着的可以无穷多。所以复现定律留着普查，作为尾段各步上的局部条件（a 类），没有作为全局前提。要去掉它，须在无穷多立着时给出总水平，那就是改变量的表示（b 类），属于 Ren 的决定。

*反驳 4：为何不沿用“封闭约束变化”的名称？* 证明表明封闭不是所需的条件，所需的是下降。名称 `runsDown_bounds_change` 描述证明了的内容，Ren 的说法仍作为推论的描述保留；名称由 Ren 定。

*反驳 5：规律 2 来自另一会话，是否经过同样的检查？* 收到的文件逐字保存，sha256 记录在整合的工作区。它在同一暂存树中与其余部分一起从前导编译，逐条公理报告为空，并作为一节并入 `Becoming.Locality`。为了不与 `World.ceasing_not_recurring` 混淆，四个名称改为以 `Covers.` 开头；与普查定律陈述相同的 `Listed.coming_of_ceasing_covered` 没有并入，相关推论直接改证。

*反驳 6：这是否推出了前提？* 没有。规律对每个世界成立，不论前提成立与否；前提对每一步成立时，局部条件在每一步成立，选择结果因此是推论。前提本身仍是偶然的。

**读法（AI，待 Ren）。** 前提约束的第一部分规律，是每一步及其关系项的规律；前提是使它们的条件处处成立的一种方式。

**边界。** 离散步；超出整单位的量与连续时间未在此检验，较粗的步待 `Sampling` 落地；复现定律与规律 3 用所立者的普查；规律 3 的界用最小差异（选项 A）；没有伦理谓词；名称（BalancesOn、RunsDownOn、RunsDown、RunsDownClosed、Covers、ListsAt、NoneComes 等）是 AI 按 Ren 的命名准则所选；尚无独立审查。

## 67. 折叠 G0（P51）

2026-10-11。Ren（[原话](../../../../sources/15-codex-theory-conversations/2026-10-11-fold-g0.md)）：

> if we don't need G0 as axiom, fold it, at least for part i, and commit

它回答 P42–P44 落地后的报告。报告列出 §64 的三项选择（是否以公理替换 G0；正面相关是否读作已实现的活的内容的意义；比较继续用哪一种），并提出下一项：审计第二部分哪些结果不用公理成立，以移入第一部分。AI 的读法（待 Ren）：
- 条件成立：第一部分不需要采用 G0，第二部分中它是那一条公理的定理；这以从意义读出的正面相关为准（§64 的读法）。
- 所以 G0 不再是所采用的公理：它的定义与已检查的刻画都保留，只改地位，在第一部分是条件，在第二部分是定理。第一项选择以此回答；第二项是折叠所用的读法，仍开放；第三项仍开放。
- “at least for part i”：第一部分现在就做；同一条件在第二部分也成立，所以章节不再在任何地方称 G0 为所采用的公理。“at least”也读作为报告所提的更大一步留出余地：第二部分中不用公理成立的结果移入第一部分。

本节是计划 P51，由本会话完成。没有新的 Lean，没有新的成果记录；改的是 G0 的地位与说到它的文字。

```text
Result(s): 复用 metaethical-core-characterization（G0、Valuation.Significant、Valuation.significant_iff、极小性反模型）、
           held-lives-g0-is-centering（Valuation.significant_iff_held）、one-axiom-yields-g0
           （Valuation.premises_of_unrestricted、Web.significance_undetermined、g0_of_unrestricted、relevance_least、
           unrestricted_iff_g0、Web.unrestricted_iff_paths_g0）；不新增，不扩展
Delta: G0 的地位：从所采用的公理改为第一部分中的条件（不用公理刻画，动力学不决定）与第二部分中公理的定理；
       章节的前提卡、§5、第一部分的总陈述、第 10 条、第二部分各处与 §8 照此改写；七项记录的文字照此更正
Supplied premises / correspondence: 无新前提；折叠以从意义读出的正面相关为准（§64 的读法，待 Ren）；
       “fold”与“at least”的读法是 AI 的，待 Ren
Evidence: 上列定理在核心回执 20261010T214440.263682Z 中，公理报告为空；本节没有新的检查
Boundary: 不推出 G0 成立；不改任何定义或定理；正面相关的读法与比较的方式仍属 Ren；
          核心七个模块的说明随后在 P47 的核心检查中一并更改（99e78ddd，回执 20261011T003217.297180Z）
Integration: 第一部分得到 G0 的条件陈述（章节 §5 与总陈述三）；第二部分以 G0 或其各部分为假设的定理在公理之下成立
             （§53、§64）；回答 §64 的第一项选择
```

**改了什么。**
- **前提卡。** G0 一行从“Ren 授权的公理，采用”改为“已折叠，不是公理”：第一部分把它作为条件陈述，由下面三条精确刻画（`significant_iff`、`significant_iff_held`），动力学不决定它（`Web.significance_undetermined`）；第二部分中它是公理的定理，各处用法由从意义读出的正面相关解除。公理一行去掉“Ren 接受之前 G0 仍是所采用的公理”。
- **第一部分。** §5 新增“G0 折叠：一个条件，不是公理”：G0 恰是什么（连通时种子加两项中立，被持有时处处 S0 加立场中立，极小性），它与那一条公理（公理恰是对任何东西的 G0），动力学不决定它；断言它成立属于第二部分。总陈述三“意义”一条照此改写；理论的完整陈述中第 10 条的地位标为“G0 不是公理”，地位词表中的“公理”改指第二部分的一条公理。
- **第二部分。** 开头、§6.1、§6.7、§6.8、§6.9、§6.11、§6.12 中“G0 仍是所采用的公理”与“替换须经 Ren 接受”改为折叠后的陈述；§6.1–§6.7 与 §7 的定理以 G0 或其各部分为假设，在公理之下这些假设成立，A、C、L 与 J1–J4 仍是公开的前提。
- **§8。** 状态表与 Ren 的选择去掉“是否以公理替代 G0”“重述是否替代 G0”，记下折叠；G0 的根据就是那一条公理的根据。术语表新增 G0。
- **一句话与两个目标。** 在它之下 G0 是定理，不再是公理；伦理方向的目标经 G0 及公开的实践前提完成，G0 现在是第二部分那一条公理的定理。
- **记录。** 七项记录中说 G0 仍是所采用的公理、或替换待 Ren 的文字改为折叠后的陈述，各加一条历史：axiom-decomposition、closure-verdict-meets-axiom、held-lives-g0-is-centering、metaethical-core-characterization、one-axiom-yields-g0、positive-ground-open-futures、presupposition-scopes。它们的定理不变。
- **范围与指令。** 生成之论的范围记录（前提一句）与指令登记各加一段；登记中先前“G0 仍是所采用的公理”的两段由新的一段取代，原文保留。

**作者反审。**
1. **折叠依赖一种读法。** 第二部分中 G0 是定理，是在正面相关读作已实现的活的内容的意义时（`g0_of_unrestricted`、`relevance_least`）。若 Ren 另读正面相关，例如读作继续创造更多意义（强式），G0 只在那一读法由意义推出之处是定理；那时第二部分要重新审视。第一部分的折叠不依赖这一读法：刻画与“动力学不决定”对任意意义成立。
2. **没有新的 Lean。** 每条引用都是已在核心回执中的定理：公理之下 G0 成立且从意义读出的正面相关是满足它的最小者（`g0_of_unrestricted`、`relevance_least`），公理恰是对任何东西的 G0（`unrestricted_iff_g0`）。更精确的折叠形式——以从意义读出的正面相关，G0 恰是公理限于已实现的活的内容——没有写成 Lean，所以章节没有声称它。
3. **G0 的名字保留。** 折叠不删 G0：它仍是定义、刻画与各处定理的假设；改的只是它不再被采用为真。G0/J 的已完成成果保持其条件范围，G0 现在由第二部分的公理给出，而不是另一条公理。
4. **开篇未改。** Ren 的开篇（`theories/becoming/OPENING.md`，README 由它生成）的注释仍写“G0 remains the adopted axiom until this one takes its place”。按其注释，开篇只随 Ren 改；替换的文字交给 Ren。
5. **Lean 说明。** 落地时核心七个模块的说明仍写 G0 仍是所采用的公理；改说明须重跑核心检查，所以补丁交给下一次核心检查。整合者在 P47 的核心检查中一并更改（99e78ddd，回执 20261011T003217.297180Z），七个模块都通过检查，此后模块说明与章节一致。

**边界。** 不推出 G0 成立，不改变任何定理；本节尚未经独立审查。

## 68. 每个变化之律保留、失去与回返的：零前提（R6）

2026-10-11。Ren 答“0”指什么时说：

> pure thermodynamics, at atomic level, each exchange between objects holds the conservation of energy, but entropy still rise. zero premises. but for if "lossless exist", can we find a path, to figure out, and prove along the way? i think another session is working on this already

随后：

> i like the direction you are going, please keep advancing, zero-premise, zero axiom(we are not physics, we derive further)

（[来源](../../../../sources/15-codex-theory-conversations/2026-10-11-difference-in-becoming.md)）。熵的会话在流与网的层面研究无损的交换（`Becoming.Entropy`，以第一定律为前提）。本节在其下一层：对任意构型上的任意变化之律，不加任何前提，问什么被保留、什么失去、什么回返。按[工作板](../../../BECOMING-WORKBOARD.md)认领为 R6。

```text
Result(s): 新增 recurrence-without-premise
Delta: 新核心模块 Becoming.Recurrence（L2，只导入 Becoming.Frame）：
       revisits_within、Revisits、revisits_of_held、revisits_from、unheld_of_new、unlisted_of_new；
       Marks、sumOver、le_sumOver、never_falls_over、Marks.mono、Marks.change_stops、not_marks；
       Law.orbit、Law.Lossless、Law.Merges、Law.Returns、Law.Reachable、Law.KeepsPossibilities；
       Law.lost_stays、Law.merged_stays、Law.Lossless.cancel、Law.lossless_of_returns、Law.Returns.reachable、
       Law.Returns.undo；Law.Lossless.returns、Law.returns_of_reachable、Law.lossless_iff_returns、
       Law.returns_iff_keeps、Law.lossless_of_reachable、Law.Merges.loses、Law.Lossless.unlisted、
       Law.Lossless.no_rise、Law.rise_not_lossless；Law.succ_open、Law.pred_open；Law.withHistory、
       Law.withHistory_lossless、Law.withHistory_new、Law.withHistory_never_returns、
       Law.withHistory_loses_beginning、Law.withHistory_unlisted、Law.present_orbit、Law.return_keeps_history、
       Law.present_forgets；Law.process、Law.run；Run.revisits_from、Run.change_stops、Reach.lost_stays
Supplied premises / correspondence: 无关于展开或变化之律的前提；“某个列表持有这些构型”不对任何展开假设，
       写进用到它的规律之内；不用可判定性；表示的承诺只有离散的步；无损与回返的等价只对确定的律（next : S → S）陈述
Evidence: 合并检查器回执 20261011T011019.444120Z（2115 项定理、3194 项声明审计，全部源声明公理报告为空；Recurrence 55 项定理、68 项声明），
          外围回执 20261011T011213.027508Z；新声明先在暂存树中以已提交的核心源从前导编译，逐条 #print axioms 全部为空
Boundary: 离散的步；“有限多构型”指某个列表持有它们；无损与回返的等价只对确定的律；遗忘的计数未陈述；尚无独立审查
Integration: 记录 recurrence-without-premise；计划 §10 R6；章节 §9 的脊柱表与第一部分；模块说明、根模块、包 README 与检查器的范围；工作板 R6
```

**机制。**

- **鸽巢，不判定任何东西。** 一个列表持有一个序列的前 l.length + 1 项时，其中两项相同（`revisits_within`）。证明对列表归纳：每一项在 a :: l 中，就是 a 或在 l 中，这是给定的成员关系的两种情形，不判定构型是否相等。若两项是 a，得到重访；若没有一项是 a，全在 l 中；若恰一项是 a，跳过它（`skipAt`）后其余在 l 中。于是有限多构型中的序列从每一步起都重访（`revisits_from`），任何过程的任何运行也是（`Run.revisits_from`）；从不重访的序列没有列表持有（`unheld_of_new`、`unlisted_of_new`）：不重访需要开放。
- **有标记的变化停止。** 构型的一个量沿序列从不下降、跨每次变化都上升（`Marks`）时，它在有限多构型上有界（`le_sumOver`），每次变化至少加一，所以变化不复现（`Marks.change_stops`）。变化复现的有限展开中，没有量标记它（`not_marks`）。
- **每个律保留与失去的。** 对确定的律 next：某一步不能到达的构型，以后任何一步都不能到达（`Law.lost_stays`）；任何过程中，沿一条可行路径失去的可达，在每个延续中都失去（`Reach.lost_stays`，即 endpoint-loss-and-return 的“损失沿延续保持”在脊柱上的形式）。被合并的两个构型以后任何一步都不分开（`Law.merged_stays`）。每个构型都回返时律不合并任何东西（`Law.lossless_of_returns`，用两个回返时间的乘积）；回返的构型在每一步都可得（`Law.Returns.reachable`）。撤销就是继续：s 回返时，同一律的继续把 next s 带回 s（`Law.Returns.undo`）。
- **有限多构型中，无损即回返。** 列表持有每个构型时，三者是一：律不合并任何东西（`Law.Lossless`）；每个构型都回返；每个构型在每一步都可得（`Law.lossless_iff_returns`、`Law.returns_iff_keeps`）。无损推出回返：s 的轨道重访，在 i < j 处相同，无损使前 i 步可以消去（`Law.Lossless.cancel`），所以 s 在 j − i 步后回返（`Law.Lossless.returns`）。在列表长度那么多步后可得推出回返：通向 s 的轨道在列表长度之内重访，重访点之后是一个环，s 在环上（`Law.returns_of_reachable`）。于是合并永久失去一个可能（`Law.Merges.loses`）；无损而有构型不回返，就没有列表持有每个构型（`Law.Lossless.unlisted`）。无损时，沿轨道从不下降的量在轨道上不变（`Law.Lossless.no_rise`）；所以沿轨道从不下降而在某步上升的量，即一个箭头，需要合并（`Law.rise_not_lossless`）。
- **开放的世界把三者分开。** 往上数（`Nat.succ`）不合并、不回返、一步后不能再有开端，并且每步上升：无损的箭头（`Law.succ_open`）。往下数（`Nat.pred`）把零与一合并，却每个数在每一步都可得（`Law.pred_open`）。“有限多构型”这一条件，两个方向都需要。
- **保留历史。** 让当下按律继续、并进入过去（`Law.withHistory`），每个律都不合并（`Law.withHistory_lossless`），从不重访（过去的长度每步加一，`Law.withHistory_new`），从不回返（`Law.withHistory_never_returns`）；开端在第一步之后就不能再有（`Law.withHistory_loses_beginning`）；没有列表持有一个展开所保留的历史（`Law.withHistory_unlisted`）。保留的历史的当下按律本身继续（`Law.present_orbit`）。当下回返时，它带着另一段历史回来（`Law.return_keeps_history`）。展开经过的构型有列表持有时，当下遗忘：从每一步起，两段不同的历史共有一个当下（`Law.present_forgets`）。

**反驳与回答（作者）。**

*反驳 1：这些是有限集合的教科书事实吗？* 数学是：鸽巢原理；有限集上的单射是双射，双射的每个点都回返。作为复用的数学记入，不作为数学上的新发现。增量是：在脊柱上以零前提、不用可判定性陈述；合并、可能的失去与回返在有限多构型中的等价，以及开放世界中把它们分开的两个见证；保留历史的构造与它需要开放；与静止规律的连接（反驳 2）。

*反驳 2：这里的“无损”是不合并，不是 Ren 所说交换中不损失量。二者怎样相关？* 第一定律之下，被围住的家族的构型落在有限多个之中（熵的会话的 `configurations_exact`）。变化是构型的函数时（熵的会话的 `Web.Determined`），本节的规律就作用于它：不合并恰是回返；有量的损失（耗散）时从不重访，有限多构型中从不重访的变化停止，停止就合并两个构型（熵的会话的 `Web.merges_of_settles`、`Flow.Balances.merges_of_dissipates`）。所以在有限的围住之内，量的损失推出区分的损失。这些作为实例定理，在两边都落地后给出。

*反驳 3：“保留历史需要开放”是否平凡？* 构造上，历史有无穷多，所以是的。内容在对照：同一展开，保留其历史时无损而有箭头（过去的长度），在有限多构型中的当下却遗忘。无损与箭头只在开放中共存（`Law.succ_open`、`Law.withHistory_unlisted`）；在有限多构型中，箭头需要合并（`Law.rise_not_lossless`）。

*反驳 4：变化停止的结论是否强于所证？* `Marks.change_stops` 证的是变化不复现（复现的否定），不是有一步之后不再变化；后者需要 LPO（`Becoming.Change` 的 `Web.lpo_of_ending`）。

*反驳 5：非确定的过程怎样？* 重访、变化停止与失去的可达保持失去，对每个过程陈述；无损与回返的等价只对确定的律。过程的形式（例如每个构型至多一个前驱）是下一步。

**读法（AI）。** Ren 的类比：原子层面每次交换守恒能量，熵仍增加，零前提。物理学的第二定律用到两样东西：守恒的动力学，与一个低熵的开端（过去假设）。这里两样都不假设。在有限多构型中，律不合并任何东西，恰是每个构型都回返，没有任何量上升；有上升（箭头），就有合并，就有一个可能永久失去。所以无损的交换存在，而且恰在两处：有限多构型中的回返（没有箭头），与保留其历史的生成（有箭头，需要开放）。物理学设为前提的低熵开端，在这里是保留的历史的开端：它在第一步之后就不能再有（`Law.withHistory_loses_beginning`），是推出的，不是假设的。熵读作有限的当下对其历史的遗忘：两段历史共有一个当下（`Law.present_forgets`）。Ren 的“karma passes, and that passing has to have a form of change which its reverse transformation will take another change”：撤销就是继续（`Law.Returns.undo`），当下回来而历史不回来（`Law.return_keeps_history`）。这些读法属于 AI；与物理学的对应只是读法，不是物理推导。

**边界。** 离散的步；“有限多构型”指某个列表持有它们；无损与回返的等价只对确定的律；遗忘的计数（需要判定构型相等）未陈述；尚无独立审查。

## 69. 第二部分的清点：什么不用公理（P52）

2026-10-11。Ren（[原话一](../../../../sources/15-codex-theory-conversations/2026-10-11-one-unified-theory-together.md)，[原话二](../../../../sources/15-codex-theory-conversations/2026-10-11-fold-g0.md)）：

> part i first, then consider second(maybe a lot in second will move to part i)

> if we don't need G0 as axiom, fold it, at least for part i, and commit

G0 折叠之后（§67），第二部分所加的只有一条公理。本节问：第二部分的定理中，哪些用到它，用在哪里。零前提的清点排除了第二部分的模块，并早于 P42–P44 的落地；本节补上这一部分，并加上公理与评价条件这一维。按[工作板](../../../BECOMING-WORKBOARD.md)认领为 P52。逐条的表、方法与提议在[清点](PART-II-INVENTORY.md)，可由[脚本](PART-II-INVENTORY.py)从两张回执所绑定的源重现。

```text
Result(s): 不新增成果；复用章节第二部分以名称引用的全部声明（182 个：157 条定理、25 个定义），
           其中 one-axiom-yields-g0、significance-retained-within-margin、whole-first-and-bounded-centers、
           closure-verdict-meets-axiom、comparison-within-reach、axiom-decomposition、presupposition-scopes、
           metaethical-core-characterization、held-lives-g0-is-centering 等记录的定理
Delta: 清点：22 条以公理为假设，各只在所指名的点上用到它（从某立场、某形成在某步的意义），
       每条都是一条对任何意义成立的规律在这些点上的特例；135 条不用公理（85 条无前提，18 条只用第一部分的前提，
       12 条以评价条件、2 条以结构条件为假设，18 条刻画公理而不假设它）；18 条用前提者中 14 条不在零前提清点之内；
       提议（待 Ren）：不用公理的移入第一部分，第二部分只留公理的断言与其根据
Supplied premises / correspondence: 无新前提；分类读自签名，点读自证明；章节的结构属 Ren，第一部分的顺序与接口属整合者
Evidence: 核心回执 20261011T071749.484228Z 与外围回执 20261011T071753.574921Z 所绑定的源（Locality 落地之后；在 R6 之前的回执之下结果相同）；
          脚本 PART-II-INVENTORY.py；本节没有新的检查
Boundary: 只覆盖第二部分以名称引用的声明；§7 以记录名引用的外围结果不在内；不推出公理；不改任何定义或定理；尚无独立审查
Integration: 章节 §8 的 Ren 的选择加一项（第二部分的结构）；零前提清点 §1.3 可并入 14 行；整合者排序前提的局部化
```

**结论。**
- **22 条用到公理，135 条不用。** 点有三种：见证中的一个形成在一步（`Clearing.free_rider_loses` 只用到栖居者在第 2 步）；被比较的路径所接纳、或超出之处的形成；活的、已实现的主张（G0 的各个推出）。
- **每条都是对任何意义成立的规律的特例。** 比较的一般局部形式 P42 已经给出：意义覆盖部分在每步之前已到达者，就对这个部分作公理的比较（`Flow.Balances.comparison_within_reach`）。G0 的推出的局部形式就是 G0 本身：以从意义读出的正面相关，G0 恰是公理限于已实现的活的内容（§67）。
- **所以第二部分在第一部分之外只加一句断言。** 公理一经断言，就在所指名的点上满足意义的条件；对一个部分的比较，只需在部分所及之处满足。A、C、L 与 J1–J4 仍是实践规律的公开条件，不被断言。
- **前提的局部化仍要做。** 18 条只用第一部分前提的定理中，4 条已在零前提清点之内；其余 14 条中两条只用可判定（b2），`Flow.region_not_a_cut` 经由 `Flow.fed_from_beyond`，11 条在第二部分的模块里，最终经 `Balances.withheld`（与 `Balances.differs_before`）只在之前各步、在所比较的形成所需的条件上用到平衡。

**反驳与回答（作者）。**
1. *读签名是机械的，有什么内容？* 读签名本身是机械的。内容有三点：哪些点；P42 的 `comparison_within_reach` 已是比较的一般局部形式；由此得到的结构，即第二部分在第一部分之外只加一句断言。
2. *“只在点上用到”对任何全称假设都成立。* 是，所以这不是结论。结论是所需的点由陈述本身给出：被比较的路径、部分的所及、活的主张。因而每条都可以带着局部条件陈述。
3. *移动是否抹去公理的作用？* 不。公理仍是唯一不被推出的断言：动力学不决定意义（`Web.significance_undetermined`）。移动的只是不用它的规律；移动之后，它的作用更清楚：在所指名的点上满足意义的条件。
4. *关键词分类会漏吗？* 第一遍按关键词，随后逐条读签名核对。首遍有两类误判，已更正：见证的结论被当作前提，以及 `∀`、`∃`、`↔` 的辖域；脚本现按 Lean 的结合规则处理辖域。各节的 `variable` 只引入数据。若仍有遗漏，最可能在评价条件的名称上；脚本列出每条的假设，可以复查。
5. *A、C、L、J1–J4 怎样？* 清点把它们归为评价条件。它们仍是实践规律的公开条件，不被断言，移动不改变这一点。

**边界。** 不新增定理，不改定义；移动待 Ren；尚无独立审查。

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
- *not undermining* (the working candidate in `Web.valuation`, pending Ren's choice): an event undermines when it draws on a condition at a step after which the condition is below both the present need of a dependence on it and a need that dependence met during its unbroken tenure (as corrected in P7b, P9b and P11b). Breaking is a case of undermining. This reading credits the broken formation, makes no drawer undermining through a dependence never met while it held, keeps both directions of divergence from the whole-run reading, and withholds the breaking step and drawing after a loss. Its cost: `draws` carries no amount and undermining does not ask what a draw does, so under a dependence once met and not yet restored any draw is withheld, however small, even one that changes no level.

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

- **Undermining is repaired.** "Met then or before" compared the present need with any past level, so a newly arrived dependent made every later drawer undermine. A dependence must now have been met at some step while it held (`MetSince`, refined in P9b to compare the need at that step and replaced in P11b by the minimum form `MetAbove`); the old behaviour is the witness `NewNeed.never_met_not_undermining`.
- **But-for holds the move fixed.** `MakesDifference` and `Overdetermined` are relative to the move actually taken (`BreaksBy`); otherwise an exogenous shock decides them (`Shock.move_decides`).
- **The horizon result holds with feedback** (`Feedback.prefix_does_not_decide`), but the conflict between criteria (a) and (c) is scoped. The whole-run reading itself credits drawing beyond renewal in the renewing run (`whole_run_credits_overdraw`). A per-step amount reading is finitely decidable and withholds every overdraw (`amount_reading`); it escapes only by not crediting every whole-run-renewing run. Whether a verdict on the problem Ren adopted (winning by consumption) covers events before the threshold is interpretive: Ren adopted the problem and stated that generation and degeneration do not overlap; the verdict on pre-threshold events is an AI extension.
- **Run level and step level are distinct.** In gradual depletion no finite set of events makes the run-level difference (`no_finite_segment_makes_difference`), while the breaking event makes the step-level one (`breaking_event_makes_step_difference`).
- **Criterion (b) is only partly met** by the stepwise, cycle and relation readings: a drawer taking exactly the renewal undermines at a break another causes (`Pool.within_share_undermines`), and a drawer that changes no level undermines after an earlier loss (`Pinned.undermining_without_effect`). Undermining reads co-participation in an unrestored shortfall, not contribution to non-return.
- **Substitution preserves consumption on the whole-run reading only**, nearly by definition; the stepwise reading credits the substituting consumer before the sustaining formation loses support and withholds it until it switches, one step in `extracting` (`stepwise_credits_substitution`) and two in `slow` (§12).
- **Smaller corrections.** Renewal implies renewal within one step, not conversely (`LateMet`); cycle length 0 is degenerate; the formation-level cycle reading is not finitely decided; "adopted" becomes "working candidate, pending Ren's choice".
- **Restraint.** In the two-part family, under both readings C ranks a course in which every need stays met above overdraw, and malignant growth below the same formation stopping before the threshold (`restraint_ranks`, `malignant_restraint`). There the stepwise reading loses the comparison with the formation's absence; with a third formation sharing the condition the restraint comparison can be lost too (`ThirdParty`, §12).

Open: Ren's words on events before the threshold, and a web with amounts and renewal rates. P8, P9 and §11 were then not yet independently reviewed; the third review and its corrections are in §12.

**P9b: third independent review and corrections (§12).** A separate Opus 5.5 agent that did not write the work reviewed P8, P9 and the P7b corrections ([review](BECOMING-P8-P9-P7B-REVIEW.md)). It recompiled every declaration from the prelude with empty axiom reports, found the counts, hashes and aliases correct and accepted the mathematics. It raised twelve findings on the correspondence between definitions and prose, with axiom-free probes, and found no choice made on Ren's behalf and no AI text quoted as Ren's words. All findings are handled; the probes become core theorems.

- **Undermining compares the need then.** `MetSince` now asks that the need was met at some step of the unbroken tenure and that the present need is no greater than the need then (replaced in P11b by the minimum form, §15). With a falling or a rising need, a dependence never met at its own need makes no drawer undermining (`FallingNeed`, `RisingNeed`). A one-step lapse starts a new tenure (`Gap`); whether dormancy is continuing dependence is an application duty.
- **But-for needs the move to be available.** `MakesDifference` requires the same move to be available from the withheld configuration (`Tagged`). It reads as intended when the move determines the step (`Determined`, which `Pool` and `Shock` satisfy); a shock written into the step relation makes the loss overdetermined again (`Hidden`). Exogenous shocks belong in the move.
- **The stepwise cost is scoped.** The comparison with absence is lost only for a formation with a credited event before the loss (`Immediate`). Restraint is kept only in the two-part family (`ThirdParty`). A substituting consumer is withheld from the sustaining formation's loss of support until it switches: one step in `extracting`, two in `slow`.
- **Interaction is a structural coincidence.** It ignores order and effect (`Later`, `Pinned.drawing_interacts`), so it is glossed as one drawing on a condition on which the other depends at a positive level, at any steps; an ordered, effect-sensitive version is open. Transmission is carried by drawing (`drawing_reaches`), so only half of Q5 is excluded, and the residual free connection needs only a condition everyone depends on at a positive level, used once (`one_use_connects`). Co-dependence is a relation the discipline omits, co-constitution through a common condition, not a mere correlation.
- **Provenance.** "Better without it" is the AI's comparative form of the problem Ren adopted (C's formal route), not Ren's verdict.

The core now has 265 theorems and 502 declaration audits, all with empty axiom reports. Open: a tenure through bounded absence, restraint beyond the two-part family, an ordered and effect-sensitive interaction, and Ren's choice of reading. These corrections have not been independently reviewed again.

**P10: continued generation (§13).** No reading of `living` includes further generation (criterion (d)). Ren's words name "a whole direction of unceasingly creating more 生"; `Becoming.Generation` states only its "unceasing" part, on the whole's continuation. A formation arises across a step when it is inactive before and active after it. Arising, becoming active, is the formal carrier of one reading of the second 生 (the author's reading). Generation is unceasing when some formation arises at arbitrarily late steps.

Suppose arising depletes a finite family of conditions: at each step at which no condition of the family rises, one of them falls (whatever its relation to the arising formation, as corrected in P11b). Then unceasing generation makes some condition of the family rise at arbitrarily late steps; and when every rise is made by some active formation renewing the condition, renewing activity recurs. Renewal can recur with nothing arising (`Tide.renewal_without_arising`, P11b), so under these premises unceasing generation is strictly stronger than recurring renewal. Further:

- arising on a consumed condition ceases (`Growth`);
- substitution among unrenewed conditions defers the end and does not escape it (`Relay`);
- dissipation ends generation: if a quantity never rises and every arising lowers it, generation is not unceasing. The author's argument that no finite part is unceasing on its own holds only under that dissipation premise; a closed cycle sustains unceasing generation (`Recycle`, P11b).

A bloom arising again and again on a condition the sun renews meets every premise; the stepwise working candidate withholds each of its blooms, and the reading over cycles of two credits it. "More", diversity and complexity are not stated, and the generation component has not been added to any reading of `living`. Section 13 was reviewed in the fourth independent review; its corrections are in §15.

**P11: more (§14).** Section 13 states only the "unceasing" of Ren's words. `Becoming.Flow` reads conditions as amounts that the formations taking part in each step take and give. A flow balances a web when every change of a condition's level is what is taken from it and given to it. Then the family's total plus its uptake equals its total before plus its replenishment, over one step and over any stretch. Balance also makes every rise the work of an active renewer, so the correspondence premise `RenewedBy` of §13 becomes a theorem.

"More" is read as: for every number, from some step on at least that many formations take from a finite family of conditions. Amounts are natural numbers, so each taker takes at least one unit; this positive minimum uptake is a premise (P11b). More without end then needs replenishment that no eventual bound bounds. When each formation gives at most a fixed amount, it needs renewers that no eventual bound bounds; their number can still be zero at infinitely many steps (`Pulse`, P11b). Renewers and growers arising at every step meet every premise, while the unceasing bloom of §13 never has more than one formation taking.

As corrected in P11b, what this gives is a strict hierarchy of the replenishment each property needs, not of the properties themselves. The author reads it as one structural sense of 生生: more 生 needs more renewing formations, which may be the takers themselves (`Cycle`). Diversity, complexity and possibility are not stated. Section 14 was reviewed in the fourth independent review; its corrections are in §15.

**P11b: fourth independent review and corrections (§15).** A separate Opus 5.5 agent that did not write the work reviewed P9b, P10 and P11 ([review](BECOMING-P9B-P10-P11-REVIEW.md)). It recompiled the 17 core modules from the prelude with empty axiom reports, found the counts, receipt, hashes and aliases correct, and accepted the mathematics. It raised fourteen findings on the correspondence between definitions, prose and premises, with axiom-free probes. It found no reading of `living` chosen for Ren, two provenance issues, and payment and ledger vocabulary in the pure core that Ren had corrected. All findings are handled, and the probes become core theorems.

- **Undermining takes the minimum form.** A draw undermines when, after its step, the condition is below both the present need of a dependence on it and a need that dependence met during its unbroken tenure (`MetAbove`). The three P9b exclusions stand. After a need has grown, a draw below the need that was met now undermines without breaking (`Stunted`). Falling short only of a need grown beyond anything met still does not.
- **But-for.** `determined_dichotomy`: when the move determines the step and is available with a part withheld, and the dependence still holds and is met there, either the part makes the difference or the same move still breaks the dependence. When withholding a supporting part leaves the dependence unmet, the test is silent.
- **Depletion, stated as what it is.** `Paid` is renamed `Depletes`. `depletes_iff` shows that it says only that some condition of the family changes at each step of the event. An unrelated tide meets it for a flicker that depends on nothing (`Tide`), and the bloom meets it only vacuously, since it arises at a rise.
- **The flow form.** In a balanced flow, when formations that take from the family at their first active step arise at arbitrarily late steps, the family is replenished at arbitrarily late steps (`replenishment_recurs`). This covers concurrent replenishment, which a net rise cannot see (`Garden.undepleted`).
- **Dissipation.** `dissipation_ceases` states the result for any quantity that never rises and that every arising lowers. A family's total is such a quantity only under dissipation, and it presupposes commensurable units. A closed cycle sustains unceasing generation (`Recycle`).
- **More implies unceasing under a census.** `Becoming.Population` proves `Flow.More.unceasing`. Its premises are a census listing the active formations at each step once, a flow listing each formation taking part once, and only active formations taking, from conditions they draw on (`Flow.Taking`). Under them more without end implies unceasing generation. The bloom meets these premises and is not more, so the implication is strict. Without a census (`Dormant`) or without `Taking` (`Inactive`), more comes with nothing arising. The converse of `Taking` is an application duty (`Crowd`).
- **Averages and cycles.** Over any stretch from which at least `K` formations take, replenishment is at least `K` per step less the stock at the start (`Balances.replenished_over`); with bounded capacity, renewers grow in the same averaged sense. Renewers can be the takers themselves, the total never changing (`Cycle`). The claim that the demand is carried beyond every finite part needs a dissipation premise and is withdrawn.
- **Names and boundaries.** Following Ren's vocabulary corrections, the core now uses depletion, uptake, replenishment and balance in place of payment, load, supply and ledger. The names are the reviewer's suggestions, and the final choice is Ren's. `Arises` is glossed as one formal carrier of the second 生, in the author's reading, and "generation by consumption" becomes "arising on a consumed condition". The structural reading's boundary now states that formations and conditions are two kinds here, so life as a condition of life is a relation the representation omits. P14 reads it with one kind of relatum (below).

The core now has 376 theorems and 688 declaration audits over 18 modules, all with empty axiom reports. Open: a dissipative flow theorem, quantities with a rational floor, and Ren's choices of the scope of the second 生 and of "more". These corrections have not been independently reviewed again.

**P12: identity across steps.** `Becoming.Identity` relates two namings of formations one to one at each step (`Reidentify`), leaving every step's levels, activity, dependences and drawing unchanged. A renaming preserves the readings defined from relations (checked for five), so labels carry nothing (P12b correction; originally "every reading, so names carry nothing"). Any re-identification preserves each step's relations, each condition's class, what a flow takes and gives, the counts of takers and renewers, more without end, a census of the active formations and `Taking`; so under a census more without end makes generation unceasing under every re-identification (`Flow.More.unceasing_reidentified`). What follows a formation depends on identity: its class over the run, the tenure of a dependence, undermining, transformation and arising. Exchanging names at odd steps changes all of them (`Turnover`). Keeping the names of continuing activity makes no arising, and keeping those of continuing dependence removes no undermining. Succession remains open. A lineage's members arise without end when named apart, and nothing arises when they are named as one (`Lineage`). An heir succeeding an elder makes later drawing undermine (`Succession`). How to read succession is Ren's choice. The core now has 422 theorems and 760 declaration audits over 19 modules, all with empty axiom reports. This section was reviewed by the fifth independent review; see P12b.

**P13: dissipation.** `Becoming.Dissipation` states dissipation on flows. Across a step, a family is closed when no formation taking part exchanges with a condition outside it, and a formation dissipates on it when it gives the family no more than it takes from it, and less when it takes. In a balanced flow a dissipated family falls by at least its number of takers at each step. Dissipated from some step on, its takers over all later steps number at most its stock there, and taking from it does not recur. So under dissipation on every closed family, a finite family from which formations take at arbitrarily late steps is open at arbitrarily late steps, and so is every finite family containing it. More without end and the unceasing arising of takers are such taking. With finitely many conditions in all, taking does not recur. A sun burning a fresh fuel at every step, giving a pool less than it burns while ever more growers take from the pool, meets every premise (`Frontier`). Without dissipation a closed cycle sustains more without end (`Cycle`). This turns the author's argument that a finite part on which taking recurs must open into a theorem under a stated premise (P16c correction; originally "that no finite part bears continued taking alone": where dissipation holds vacuously the opening exchange may be unrelated, and a family enclosed around draws in, see P16c). The core now has 450 theorems and 798 declaration audits over 20 modules, all with empty axiom reports. This section was reviewed by the sixth independent review; dissipation binds only where some finite family is closed, and the requirement comes from any recurring uptake, not only from more (see P16b).

**P14: roles.** `Becoming.Roles` reads formations and conditions as two roles of one relatum. The two-kind reading of `Web` and `Flow` embeds in the one-kind reading in which no formation is a condition (P16b correction; originally "is"). Read so, every listed reading and the connection of both valuations is kept, and no formation active at some step is embodied or bears on itself. Which condition is which relatum is supplied by the shared index (P16b). A relatum is embodied when it stands as a condition exactly while it is active, and bears on itself when, while active, it depends on its own standing. Under `Dependent`, a formation depending on an embodied relatum is active only while that relatum is (P18b wording; originally "lives only while that relatum does"), activity passes along chains of such dependence, and a relatum that is not active ends every formation whose chain reaches it (coextinction). Drawing on an embodied relatum that bears on itself, across the step at which it ends, breaks its own dependence whatever ends it, so the drawing event is not living; whether drawing at an ending should so count, and for which drawers, belongs to Ren's reading of 生生 (P16b correction; originally "whether ending another life should so count"). In a balanced flow where only active formations give, an embodied relatum arises only as another active formation gives to it, and that formation need not be embodied (P16b correction; originally "life from life"; P16c wording, originally "a giver"; P18b wording, originally "need not be a life"). Drawing on a relatum that bears on itself interacts with each of its active events, so a bee and a flower each depending on itself and on the other are connected with no third condition; where each depends only on the other, neither valuation relates them. A fox ends with the hare it eats, and generations arise without end, each given by the one before. This answers H14 of the fourth review. The core now has 513 theorems and 878 declaration audits over 21 modules, all with empty axiom reports. This section was reviewed by the sixth independent review; see P16b.

**P12b: the fifth independent review.** A separate agent (Claude Opus 5.5) reviewed P11b and P12 ([review](BECOMING-P11B-P12-REVIEW.md)). It accepted all the mathematics with empty axiom reports, closed H1–H14, and found twelve issues (I1–I12) in premises, prose and correspondence. In the flow form, recurring uptake needs recurring replenishment (`uptake_needs_replenishment`): arising works only through the uptake it brings, and a constant consumer with nothing arising needs replenishment too (`Steady`). That the flow lists each formation once is a necessary premise of `More.unceasing` (`Repeated`), and the garden and the cycle meet every premise (`Garden.counted`, `Cycle.counted`). Labels carry nothing, while the pattern of names across steps carries identity. Continuity read one way lets the new naming make a continuity; read both ways it preserves arising and undermining exactly (`Reidentify.back`), and joining across a dormant step still changes a formation's class (`Dormancy`). Arisings made by naming alone can meet every premise of `Unceasing.regeneration_recurs` (`TideFlip`). Splits and merges change the continuation relation, not the number of formations. Under a census, with each formation taking part listed once and only active formations taking, under every continuation in which no formation continues as two more without end makes formations arise at arbitrarily late steps (`Flow.More.unceasingFrom`), while budding defeats it (`Budding`); no split is sufficient, not necessary (`Fork`; P16b correction, premises restored). A lineage and its members are two levels of one unfolding, with the part–whole relation omitted (`Layered`). The heir of `Succession` now lives. The core now has 559 theorems and 948 declaration audits over 19 modules, all with empty axiom reports. These corrections were reviewed by the sixth independent review; see P16b.

**P15: generation is replenishment.** Following the fifth review's I3 and its §4 item 2, P15 lets generation itself, rather than uptake, carry the requirement. Read with one kind of relatum, an embodied relatum is given at least the standing it arises with (`Embodied.given_of_arises`), so its arising replenishes every family containing it, and embodied arising at arbitrarily late steps needs replenishment at arbitrarily late steps, whatever is taken (`generation_needs_replenishment`). A formation giving to a family dissipated on takes from it (`DissipatesOn.takes_of_gives`), so under dissipation an embodied arising in a closed family without repetition lowers the family's stock (`Embodied.arising_lowers`); this derives the physical premise of `dissipation_ceases` for such arisings (P16c correction; originally "Under dissipation a formation giving to a family takes from it"). A finite family in which embodied members arise at arbitrarily late steps is therefore not closed from any step on (`generation_opens`), though the opening exchange may be unrelated to it (`SprayHanding`, P16c), and with finitely many relata in all, embodied arising does not recur (`generation_ceases`). Each premise is needed. Two sides handing one standing back and forth generate without end in a closed world without dissipation (`Handing`). Burning a fresh fuel, they do so under dissipation while every finite family containing a side opens (`Kindling`). A relatum whose activity is not its standing arises with nothing given to it (`Flicker`). The brood is not dissipative (`Brood.not_dissipative`, renamed in P16b from `Brood.costless`). The package now has 588 theorems and 987 declaration audits over 19 modules, all with empty axiom reports (P16c correction; originally "The core"). This section was reviewed by the seventh independent review; see P16c.

**P16: wholes and parts.** Following the fifth review's I10 and its §4 item 7, the new module `Becoming.Wholes` states the part–whole relation that a single level of naming omits. A formation is the whole of some parts when it is active exactly while some part is (`Web.Whole`), and `Layered`'s lineage is the whole of its members (`Layered.composed`). A whole arises only as a part arises (`Whole.arises_part`). A whole active at every step from some step on persists only through its parts' generation. If no part is active at two steps `d` apart, a part arises within every `d` consecutive steps (`Whole.arises_within`); the bound is attained (`Shifts`). If each part's activity ends and the active parts are listed finitely, parts arise at arbitrarily late steps (`Whole.needs_arising`). Without these premises a whole can persist while nothing arises (`Immortal`, `Countless`), and the converse fails (`Gaps`). The premises are consistent: a lineage of two-step generations is active at every step and never arises while a member arises at every step (`Generations`). Where parts are brief, or end with finitely many active at once, reading 生生不息 as the lineage's persistence needs unceasing generation of its members; at which level it is read remains Ren's (P16c correction; originally "Where parts do not last … entails"). The package now has 614 theorems and 1028 declaration audits over 20 modules, all with empty axiom reports (P16c correction; originally "The core"). This section was reviewed by the seventh independent review; see P16c.

**P16b: the sixth independent review.** A separate agent (Claude Opus 5.5) reviewed P13, P14 and P12b ([review](BECOMING-P13-P14-P12B-REVIEW.md)). It recompiled the 21 modules of the core closure from the prelude with empty axiom reports, accepted all the mathematics and closed I1–I12. It found eleven issues (J1–J11) in premises, prose and correspondence, with two recurring patterns: an omitted premise, and a supplied correspondence presented as a result.

- **Dissipation binds where a step is enclosed.** A step is enclosed when some finite family without repetition is closed across it (`Flow.Enclosed`). There, under dissipation, a formation that gives takes more than it gives (`Dissipative.gives_less`), so giving needs uptake (`giving_needs_uptake`). Where no step is enclosed, dissipation is vacuous and a renewer can give while taking nothing (`Spray`).
- **Any recurring uptake.** Keeping one eater fed already reaches beyond every finite family (`Lone`). The 整体 reading therefore concerns any recurring uptake, not only more. The frontier with growers depending on the pool meets every premise together (`Rooted`), and the earlier witnesses are not dissipative (`witnesses_not_dissipative`).
- **What the one-kind reading keeps and adds.** It keeps `Acting`, `Taking`, a census, a distinct present and dissipation as well (`roles_acting`, `roles_taking`, `roles_census`, `roles_distinct`, `roles_dissipative`). Which condition is which relatum is supplied by the shared index. Relabelling the conditions onto themselves keeps dependence, undermining, living and both connections, while changing which relata are embodied (`relabel`). So the two-kind representation embeds in the one-kind reading and omits that identification. Embodiment itself enters neither valuation (`Mutualism.apart_embodied`).
- **Endings.** Drawing on a self-bearing embodied relatum at the step at which it ends breaks a dependence, whatever ends it. This includes a bystander that takes nothing and the relatum's own last event (`Wilting`; P18b wording, originally "a self-bearing life", "the life"). Whether that should count, and for which drawers, is Ren's choice.
- **Giving.** An embodied relatum arises through the giving of another active relatum, which need not be embodied (`SunSeed`; P18b wording, originally "need not be a life"). Where only embodied relata give, the relatum that gives is embodied (`arises_from_embodied`), and being embodied is not being a life (`EmbodiedSun`, P16c; originally "the giver is embodied").
- **Splits.** No split is sufficient for `Flow.More.unceasingFrom`, not necessary (`Fork`), and without a census it fails (`Dormant.no_split_without_arising`).
- **Vocabulary and counts.** The cost vocabulary becomes "giving needs uptake", and `Brood.costless` becomes `Brood.not_dissipative`; Ren may revert either. The P12, P13 and P14 paragraphs count the core closure (19, 20 and 21 modules). The P12b, P15 and P16 paragraphs count the package (19, 19 and 20).

The package now has 676 theorems and 1115 declaration audits over a closure of 22 modules (a package of 20), all with empty axiom reports (P18b correction; originally "The core"). These corrections were reviewed by the seventh independent review; see P16c.

**P16c: the seventh independent review.** A separate agent (Claude Opus 5.5) reviewed P15, P16 and P16b ([review](BECOMING-P15-P16-P16B-REVIEW.md)). It recompiled the 22 modules of the core closure from the prelude, with empty axiom reports for all 1185 declarations, accepted all the mathematics, and found J1–J11 closed, J1 and J7 with an overclaim and J11 with residues. It raised eight findings (K1–K8) in premises, prose and correspondence, with two patterns: a conclusion met by unrelated exchange where dissipation holds vacuously, and embodiment read as life.

- **Inflow.** The conclusion of `generation_opens` and of `Dissipative.opens`, that a finite family is not closed at arbitrarily late steps, can be met by a sink exchanging with ever new relata while generation recurs in the family with nothing flowing in (`SprayHanding`). A step encloses a family around when some finite family without repetition containing it is closed across the step (`Flow.Around`). With decidable equality every enclosed step encloses every finite family around (`Enclosed.around`). Under dissipation, a family enclosed around from some step on, on which taking recurs, draws in: at arbitrarily late steps some formation gives to it and takes from beyond it (`taking_draws_in`). Recurring embodied generation draws in the same way (`generation_draws_in`, through `generation_ceases_on`). `Kindling`, `Frontier` and `Lone` are enclosed at every step and draw in. Titles now state the literal conclusion, and drawing in where the family is enclosed around.
- **Dissipated on.** A formation giving to a family takes from it only where the family is dissipated on (`Frontier.gives_without_taking`). `gives_less` needs a family without repetition (`Lone.repeated_family`).
- **Wholes.** `Whole` is coincidence of activity, not constitution (`whole_self`, `Immortal.each_other`). The two theorems are stated for parts covering every step from some step on (`Web.Covered`), and a persisting whole is so covered (`Whole.covered`). Where parts end and finitely many are active at once, ever new parts arise (`needs_new`). Under brevity the same parts may arise again (`Layered.brief`, `within`, `arise_again`). "Is" becomes "through", `Listed` enters the titles, and neither premise yields more parts.
- **Giving.** Where only embodied relata give, the relatum that gives is embodied; it may be a sun depending on nothing (`EmbodiedSun`). "Life from life" is not a theorem, and whether embodied relata are 生 is Ren's reading.
- **Merges.** On the garden a merge comes with a persisting grower re-read as arising at every step, so the conclusion holds without more (`Merge.idle`). Where the merged formation ends, what arises is exactly what is new (`Confluence`).
- **Vocabulary and counts.** "Giver" becomes "the relatum that gives" in current text, and the hypothesis `givers` becomes `gives_embodied`; Ren decides the vocabulary. The P15 and P16 paragraphs count the package, not the core.

The package now has 728 theorems and 1182 declaration audits, over a core closure of 22 modules and a package of 20, all with empty axiom reports. These corrections were reviewed by the eighth independent review; see P18b.

**P17: reserve, and coming to stand.** `Dependent` lets a formation be active only where it is supported, and `Embodied` lets a relatum stand as a condition only while it is active; both exclude what is held. [Becoming.Reserve](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Reserve.lean) states what a reserve carries ([reserve-defers-ending](../../../../theories/becoming/results/records/reserve-defers-ending.md)). New theorems in Flow, Dissipation and Roles move the requirement of §20 and §23 onto what it actually uses ([generation-is-replenishment](../../../../theories/becoming/results/records/generation-is-replenishment.md)).

- **`Dependent` is the zero reserve.** A reserve does not rise across a step at which its formation is unsupported, and falls if the formation is active there (`Web.Carries`). The zero reserve is exactly `Dependent` (`carries_zero`), so relaxing it means a positive reserve, not activity outside dependence.
- **A reserve can be a held condition** (P18b correction; originally "is"). In a balanced flow, consider a condition that nothing gives to while its holder is unsupported, and that is taken from, by whatever takes part, while the holder is active there (P18b correction; originally "that the holder takes from"). That condition carries the holder (`Flow.carries_of_held`). Where no held condition is represented, the reserve is supplied (`Seed.no_held`). The same levels, activity, drawing and flow can be read with the dependence transformed onto the held condition (`Famine.transformed_dependent`), a reading that differs in living (P18b correction; originally "The same unfolding"; see P18b).
- **A reserve defers the end and does not escape it.** A formation unsupported from some step on is active only finitely often, and at most as often as its reserve at the start (`Carries.lasts`). This holds after a loss without return (`consumed_lasts`) and after the end of an embodied relatum it depends on (`coextinct_lasts`). It is the pattern of `substitution_defers`.
  - **Dormancy.** Unsupported, a formation arises only finitely often (`arising_finitely`). Dormancy itself uses no reserve under `Carries` (P18b wording; originally "draws nothing"). A reserve that also decays (`Decays`) bounds the time as well (`ends_within`).
  - **Witnesses.** The bounds are attained by `Seed`, `Viable` and `Famine`, in which a fox outlives the hare by exactly its fat.
- **Generation bears replenishment where standing rises.** A condition comes to stand across a step when its level is zero before it and positive after it (`Web.ComesToStand`); what the theorems use is the rise, from zero in this case (P18b; see there). In a balanced flow it is given at least its new standing. Recurring in a family, it needs the family's replenishment to recur (`standing_needs_replenishment`). It lowers the stock of a family dissipated on (`standing_lowers_on`). Under dissipation, a finite family without repetition in which it recurs is open at arbitrarily late steps (`standing_opens`); enclosed around, the family draws in (`standing_draws_in`). With finitely many conditions in all, it does not recur (`standing_ceases`). As §23 found, the opening exchange may be unrelated to the family.
  - An embodied relatum comes to stand as it arises (`Embodied.comesToStand`), so the nine theorems on embodiment of §20 and §23 now follow from these, with their statements unchanged.
  - A relatum standing while active, and absent at some earlier step, came to stand in between (`came_to_stand`). A seed is given its standing while dormant and arises with nothing given (`Provisioned`). Waking from dormancy is arising without coming to stand, and needs nothing given (`Sleeper`, in whose flow nothing takes part).
- **Author's reading.** Without support, what is held only defers the end; unceasing arising, where what arises comes to stand, needs unceasing replenishment. Whether these formations and relata are 生 is Ren's reading (§23, K6). The author reads this as one formal content of 不息 that what is held cannot carry alone (an AI argument). It does not replace Ren's words.

The package now has 774 theorems and 1257 declaration audits, over a core closure of 23 modules and a package of 21, all with empty axiom reports. Section 24 was reviewed by the eighth independent review; see P18b.

**P18: living on and descent.** [Becoming.Descent](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Descent.lean) (L4) adds two readings of `related` that only the one-kind reading has, each added to interaction, with the living events of the stepwise reading unchanged ([living-on-and-descent](../../../../theories/becoming/results/records/living-on-and-descent.md)).

- **Living on.** A formation lives on a relatum at a step when it draws on it and depends on it at a positive need there (`Web.LivesOn`). Like interaction it is not free: under `Dependent` the relatum an active formation lives on stands at that step (`LivesOn.stands`), and where it is embodied it is active there (`LivesOn.active`) (P18b correction; originally "lives only on an embodied relatum active at that step"). It connects the bee and the flower that depend only on each other, which neither co-participation nor interaction connects (`Mutualism.apart_sustenance_connected`). Under N_rel, valuing the fox's eating reaches the hare's living, and conversely (`living_on_reaches`, `lived_on_reaches`).
- **Descent.** A relatum descends from a formation that takes part in a step at which it gives to the relatum and across which the relatum comes to stand (`Flow.Descends`; P18b correction, originally without taking part), and descent relates every event of the two. An embodied relatum that arises descends from another active formation, which need not be embodied (`Embodied.descends`). So under N_rel, valuing that formation reaches the arisen relatum's living events (`arisen_reached`).
  - Generations each given by the one before are connected by descent alone, and G0 there is exactly a seed with N_rel and N_std (`Brood.descended`).
  - Descent follows coming to stand: a provisioned seed descends from its parent, and waking from dormancy descends from nothing (`Provisioned.descends`, `Sleeper.no_descent`).
- **Where the identification enters.** Relabelling the conditions of the bee and the flower each onto the other keeps co-participation and interaction and removes the connection by living on (`Mutualism.relabel_sustenance`).
- **What is not claimed.** Whether these readings count as formed relations for N_rel is Ren's choice, as is taking embodied relata as 生. Neither living nor C changes, so nothing here makes bringing about new arising better.

The package now has 799 theorems and 1286 declaration audits, over a core closure of 24 modules and a package of 22, all with empty axiom reports. Section 25 was reviewed by the eighth independent review; see P18b.

**P19: laws of change with no premise.** Following Ren's instruction to aim at a complete Theory of Becoming, [Becoming.Change](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Change.lean) states what holds of every unfolding, with no premise about it ([coming-and-ceasing-keep-pace](../../../../theories/becoming/results/records/coming-and-ceasing-keep-pace.md)). The representation's commitments are disclosed separately: discrete steps, natural-number amounts, and decidability where counting needs it.

- **One change.** A determination comes to be across a step where it fails before and holds after, and ceases to be where it holds before and fails after. A formation arising and ceasing, a dependence forming and dissolving, and a condition coming to stand and ceasing to stand are this one change, read of activity, dependence and standing (`Web.change_readings`). Support changes only through relations (`Web.supported_of`).
- **Rises and falls.** Over any stretch, an amount at the end with its falls is the amount at the start with its rises, and so for a finite family (`over_stretch`, `family_over_stretch`).
- **A floor and a ceiling.** No amount falls below zero, so in a finite family recurring falls need recurring rises (`rising_recurs`). In every unfolding, levels of finitely many conditions that keep falling keep rising (`Web.falls_need_rises`). `falls_finitely` of `Becoming.Renewal` is this floor for one amount. With amounts bounded, recurring rises need recurring falls (`falling_recurs`).
- **Coming to be and ceasing to be keep pace.** A determination counts zero or one, so both bounds hold. Over any stretch, in a finite family, the members holding at the end with those that ceased to be are those holding at the start with those that came to be (`held_over_stretch`). Comings and ceasings differ by at most the number of members (`keep_pace`), and each recurs exactly when the other does (`coming_recurs_iff`).
  - Read of activity: formations of a finite family arise at arbitrarily late steps exactly when they cease at arbitrarily late steps. With finitely many formations, arising recurs exactly when ceasing does (`Web.unceasing_iff`; P29b correction: this read “generation is unceasing exactly when ceasing is”, section 42 R5).
  - Read of standing, with no premise at all: coming to stand recurs in a finite family exactly when ceasing to stand does (`Web.standing_recurs_iff`).
- **Infinity is the escape.** Ever new formations can arise with none ceasing (`Dawn`), and endlessly many formations active at the start can cease with nothing arising (`Dusk`).
- **Author's reading.** In any finite family, arising and ceasing recur together. The author reads this as one formal content of Ren's scope, formation through dissolution within one unfolding (an AI argument). This is a reading of activity; whether it is the proposal's generative and degenerative is Ren's to choose: Ren asked whether the two do not overlap (‘不overlap吧’), and if non-overlap is taken this reading is not what is meant (the AI's inference); read as relations, renewing and consuming formations do not overlap (`Web.renewing_not_consuming`) (P25b correction; originally “not Ren's generative and degenerative: Ren said the two do not overlap”; see section 38, O8) (P23c correction; originally "generation and degeneration recur together"; see section 34, M1). It does not make ceasing good or a cost of generation. The level at which 生生不息 is read, and the names, remain Ren's.
- **Housekeeping.** `mark` moves here from `Reserve`. `total_map` and `total_congr` move from `Roles` to the totals section of `Flow`, which gains `total_ones`.

The package now has 841 theorems and 1342 declaration audits, over a core closure of 25 modules and a package of 23, all with empty axiom reports. Section 26 was reviewed by the ninth independent review; see P23c.

**P18b: the eighth independent review.** A separate agent (Claude Opus 5.5) reviewed P16c, P17 and P18 ([review](BECOMING-P16C-P17-P18-REVIEW.md)). It recompiled the 24 modules of the core closure from the prelude, with empty axiom reports for all 1356 source declarations, and accepted all the mathematics. K2, K5 and K7 are closed, K1, K3, K4 and K6 closed with residues, and five of K8's eight items closed. It raised ten findings (L1–L10). No reading was chosen for Ren. The corrections are made in place and marked; section 27 records the handling.

- **Descent requires taking part (L10, the most serious).** `Flow.Descends` read `give` without requiring the formation that gives to take part in the step. A gift entry of a formation taking no part enters no level, and neither balance nor `Acting` constrains it, yet it made descent; in `Brood` every generation descended from every number. Descent now requires the formation to take part. Every published positive result holds, and the spurious descents fail as theorems (`Stranger.stranger`, `Brood.not_descends`). Descent counts gift entries, not net flow, a further choice of reading.
- **What living on needs (L8, L9).** Under `Dependent` the relatum lived on stands at that step (`LivesOn.stands`); only where it is embodied is it active there (`LivesOn.active`). An eater can live on a dormant relatum that is neither embodied nor active, and living on connects them where interaction does not (`Drowsy`). Neither relation's definition mentions embodiment: what first enters the valuation is the one-kind identification.
- **Reserve (L4–L6).** A reserve can be a held condition; where none is represented it is supplied, and no condition of the seeds' webs carries them (`Seed.no_held`, `Viable.no_held`). The held condition may be taken from by whatever takes part; where the holder itself takes from it, as the fox burns its fat, the reserve is its own use (`Flow.carries_of_own`). Moving each unsupported dependence onto the held condition gives a `Dependent` reading by construction (`Web.redirect`, `redirect_dependent`), and that reading differs in living: the fox's event at step one undermines as published and not when its dependence is moved onto its fat (`Famine.living_differs`). Which reading the valuation uses is a correspondence premise.
- **The requirement follows the rise (L7).** In a balanced flow every rise is given to (`Balances.rise_given`). The replenishment and dissipation theorems now hold for any rise (`rising_needs_replenishment`, `rise_lowers_on`, `rising_ceases_on`, `rising_opens`, `rising_draws_in`, `rising_ceases`), and coming to stand is the rise from nothing (`ComesToStand.rises`), so the earlier theorems follow with their statements unchanged. A condition can rise at every step without ever coming to stand (`Growing`).
- **Residues and bookkeeping (L1–L3).** Embodied relata are no longer called lives: "an embodied relatum as a condition" in `Roles`, and "need not be embodied" in the prose, while H14's phrase names only the question the record answers. The `Dissipation` title states the enclosure. Two related notes state their premises. "Giver" is gone from current text, the §24 rebuttals run in order, dormancy "uses no reserve", and the P16b paragraph counts the package. The text now says that every *source* declaration has an empty axiom report. The checker also audits every constant Lean generates in the core closure: only the injectivity lemmas of constructors with fields (`injEq`) depend on an axiom, `propext`; there are 29, and no source declaration uses them. The convention for review stamps is in the result workflow.

The package now has 877 theorems and 1387 declaration audits, over a core closure of 25 modules and a package of 23, all source declarations with empty axiom reports. Section 27 was reviewed by the ninth independent review; see P23c.

**P20: rising and falling in one exchange.** Section 26 shows, with no premise, that coming to be and ceasing to be keep pace in a finite family, as counts and recurrences over stretches. It does not say what accompanies a single rise at its own step, and without a premise nothing need: in `Growing` and `Brood` a member rises while nothing falls. Under balance, across a step at which a family is dissipated on, a rise is accompanied at its own step (P23c correction; originally "under balance and dissipation") ([rising-and-falling-in-one-exchange](../../../../theories/becoming/results/records/rising-and-falling-in-one-exchange.md)).

- **Every fall is taken from.** In a balanced flow every fall is taken from (`Balances.fall_taken`). Where only active formations take, some active formation drawing on the condition takes from it (`Balances.takenBy`). These are the duals of `rise_given` and `renewedBy`.
- **Falls cover rises.** Across a step dissipated on, a family's members fall by at least as much as they rise, and by one more for each formation taking from it (`Balances.falls_cover`). This follows from the one-step balance of rises and falls in section 26 and `runs_down` in section 17.
- **Rising and falling in one exchange.** Where a member of a family dissipated on rises, another member falls across the same step (`rise_with_fall`, `standing_with_fall`). Where only active formations give and take, an active formation gives to the one and takes from the family, and an active formation drawing on the other takes from it (`rise_exchange`). Read with one kind of relatum, the arising of an embodied member comes with another member falling (`Embodied.arising_with_fall`).
- **A one-step test of openness.** Under dissipation, a family without repetition in which a member rises while none falls is open across that step (`rise_alone_opens`). The brood is such a case: each generation arises in a closed family of itself and the one before, and no generation ever falls, so that family is not dissipated on (`Brood.rise_without_fall`).
- **Generation's premises reduce to the flow's.** A formation taking from a family dissipated on makes some member fall, whether or not another rises (`Balances.falls_of_taking`). An event at whose steps this happens depletes the family (`Balances.depletes`). Read through flows, both correspondence premises of `Becoming.Generation` therefore follow: `RenewedBy` from balance with only active formations giving, and `Depletes` from balance, dissipation and taking at the event's steps.
- **Boundaries.** A fall is a lowering, not a ceasing: the member that falls may still stand. Nor is a fall a harm; undermining is defined by needs, and the falling member may be fuel that nothing depends on. "One exchange" means giving and taking in one flow across one step. It does not attribute a particular fall to a particular rise. The plan's original title, "coming to be and ceasing to be in one exchange", was too strong and is corrected.
- **Bookkeeping.** Five records cite module theorem counts. They now follow the new receipt; four of them (Flow, Dissipation, Identity, Wholes) were stale before.

The package now has 889 theorems and 1399 declaration audits, over a core closure of 25 modules and a package of 23, all source declarations with empty axiom reports. Section 28 was reviewed by the ninth independent review; see P23c.

**P21: evolution on the spine.** The theory of evolution's central candidate says that differences in organizations enter subsequent activity through actual transmission and alter the conditions of later selection. Section 29 gives that candidate its minimal formal content on the spine, in a new module `Becoming.Evolution` (L3, importing only `Change`) ([evolution-on-descent](../../../../theories/becoming/results/records/evolution-on-descent.md)).

- **Descent belongs to change, not to valuation.** Descent is defined by taking part, giving and coming to stand, with no valuation. It moves from `Becoming.Descent` (L4) to `Becoming.Evolution` (`Flow.DescendsAt`, `Flow.Descends`), and `Descent` imports it and keeps its readings under N_rel.
- **A law of transmission with no premise.** Over any finite family of parents with finite lists of offspring and any amounts, the offspring's total with what transmission lowered is the parents' amounts counted once for every offspring, with what transmission raised (`price`). This is Price's equation in additive counting form. It is an accounting identity, as two existing notes say; what is new is that it is checked in the pure core and that both of its terms receive content on the spine.
- **Selection as support constraining giving.** Fitness is not defined. Where only active formations give and activity needs support, only supported formations leave descendants (`DescendsAt.supported`, `unsupported_childless`, `never_supported_childless`), and the parents' needs weighted by their offspring are bounded by the condition's level counted once for every offspring (`selected_le`, `selection_within`). This weighted total is not the selection term proper: it is k times the parents' total where every parent has k offspring (`selected_uniform`, P23c; originally "the selection term").
- **What is transmitted was selected.** Where descendants take up their parents' dependences within δ (`TransmitsWithin`, a premise), a descendant's need is at most the condition's level at the giving step, plus δ (`transmitted_supported`); with δ positive it may never have been met (`Slack`, P23c).
- **Activity sets later selection.** In a balanced flow, that level is the earlier level with what was taken from and given to the condition in between (`transmitted_within`). In `Drawdown` the parent's own taking lowers the pool, so the descendant inheriting its need is unsupported from its first standing step on, while the one needing less is supported, active and takes in turn. Without `Dependent`, a formation active beyond its support transmits a need above the level (`Unchecked`).
- **Boundaries.** Selection here constrains who can give at a step, not how many offspring a formation has; reproductive rates, mutation, drift, movement and population dynamics are not covered. Transmission is a premise, as reconstruction is in the theory of evolution. No correspondence to the existing mechanisms (`StructuralCopying` and others) is attempted this round; they keep their scope. Nothing is evaluated.
- **Bookkeeping.** The record living-on-and-descent now cites `Flow.Descends` in `Evolution.lean`; its claim is unchanged.

The package now has 910 theorems and 1435 declaration audits, over a core closure of 26 modules and a package of 24, all source declarations with empty axiom reports. Section 29 was reviewed by the ninth independent review; see P23c.

**P22: the whole and its parts.** Ren proposed that with an axiom the good can be defined as a part of the whole space, while counting all the space, generative and degenerative, gives the theory of becoming without an axiom. Section 30 gives one structure for that proposal, an AI reading, in a new module `Becoming.Space` (L3, importing `Evolution` and `Reserve`) ([space-and-its-parts](../../../../theories/becoming/results/records/space-and-its-parts.md)).

- **The space.** A world is its relata, read with one kind, with the flow among them and their web (`World`); the two-kind reading of any flow and web is a world (`World.ofRoles`). The laws stated with no premise, those of change and Price's equation, are stated of every web and amount, so they hold throughout the space.
- **Arising recurring and ceasing recurring are one part in finite worlds.** In a finite world whose activity is decided, arising recurs exactly when ceasing does (`arising_iff_ceasing`, section 26's `unceasing_iff` read of worlds). This is a reading of activity; which parts Ren's "generative, degenerative" name is Ren's to choose, and Ren asked whether the two do not overlap (‘不overlap吧’) (P23c correction; originally "Generation and degeneration are one part", with `generative_iff`; see section 34, M1). With infinitely many relata either recurs without the other (`separate`, from `Dawn` and `Dusk`), and that those worlds are infinite follows from the law.
- **Premises carve parts.** Seven premises are each met by some worlds and not by others (`contingent`); `idle`, `restless`, `unbalanced` and `spending` are new worlds for this.
- **Living crosses arising.** Among finite worlds all four combinations of arising recurring or not with every event living or not occur (`living_crosses`). `handing` and `spending` have the same activity and differ only in whether each side draws on its own standing; the pair shows that drawing and dependence decide living only under the stepwise verdict on drawing on a self-bearing relatum at its ending, which is Ren's to choose. `grazing` does not rest on that verdict (P23c correction; see section 34, M7).
- **Dissipation brings a finite world to rest.** In a finite, balanced, dissipative world whose activity is decided and whose arising is embodied, neither arising nor ceasing recurs (`rests`), and each premise is needed (`rests_needs`; since P23c the balance witness is `leaking`, whose dissipation is not vacuous).
- **Boundaries.** No part is evaluated. This does not show that the theory needs no axiom; it shows which statements need no premise and which premises carve which parts. The law for finite worlds needs decidable activity because the core is constructive. The parts listed are not exhaustive.

The package now has 939 theorems and 1501 declaration audits, over a core closure of 27 modules and a package of 25, all source declarations with empty axiom reports. Section 30 was reviewed by the ninth independent review; see P23c.

**P23: the theory stated in full, and the completion audit.** Following Ren's instruction to aim at a complete theory of becoming, section 31 states the checked results once as a whole and updates the completion audit and the open programme accordingly. No Lean declaration and no result identity is added.

- **The full statement.** The canonical chapter gains “The theory stated in full”, in five parts: the whole, coming to be and ceasing in one unfolding, the conditions of further activity, differentiation, and standing. Each item is marked as representation, law, theorem, axiom (G0), reading or open.
- **Laws and representation.** The laws with no premise hold of every world as the spine represents worlds: discrete steps, natural-number amounts, a shared index identifying conditions with relata, and, where a law needs it, activity decided at each step (P23c addition). Whether every becoming can be so represented is listed as philosophical warrant; extending the spine, for instance to continuous time or real amounts, is listed as a further proof.
- **Four classes.** Section 8 of the chapter now gives a status table and places every open item in one of four classes: Ren's choices, philosophical warrant, empirical correspondence and further proofs. Review is listed separately, since it checks existing results.
- **The completion audit.** Each row of the foundation chapter's audit cites the spine's results as evidence, and its remaining inference is unchanged: the spine locates the whole claim's substantive remainder without discharging it. The foundation record's next step is rewritten to match, keeping its central inference.
- **A wording correction.** The record generation-is-replenishment no longer says that every arising of life is a replenishment; it says that an arising embodied relatum which is itself a condition of others is read as 生 only under Ren's reading.

Section 31 was reviewed by the ninth independent review; see P23c.

**P24: the map of premises.** The plan's third part of completeness asks that each dynamical premise carve a proper part of the whole space; section 30 gave this for seven premises. Section 32 adds the remaining premises stated of worlds and maps the premises against one another, in a new L3 module `Becoming.Premises` (importing `Space`) ([map-of-premises](../../../../theories/becoming/results/records/map-of-premises.md)). It was completed while the ninth review ran.

- **Two more premises.** A census (`Counted`) and bounded transmission (`Transmitting`) are premises of worlds too.
- **What follows from what.** Activity needing support makes activity carried, by the zero reserve (`Dependent.carried`). Every relatum embodied makes whatever arises embodied. A finite world whose activity is decided has a census (`Finite.counted`); without decidability, asking this of every finite world implies excluded middle (P25b addition; see section 38, O9). Where only active relata take and the flow dissipates, only active relata give across an enclosed step, since giving needs uptake there (`acting_across`, added in P25b); every step of a finite world is enclosed (`acting_of_enclosed`, `Finite.acting`).
- **The remaining eight are independent.** For each of activity needing support, balance, only active relata giving, only active relata taking what they draw on, dissipation, embodiment, a census and bounded transmission, a world meets the other seven and not it (`independent`), so none follows from the others (`none_follows`). The worlds failing a census (`multitude`) and failing only active relata giving (`scatter`) are infinite, as the implications require. In `novel` a child comes to depend on the parent that gave it its standing, a dependence the parent never had, so transmission fails.
- **All together.** Mutualists active throughout meet all eight (`mutualism_premised`), the four about the flow vacuously, and a finite world whose activity is decided and which meets the eight comes to rest, the proof using balance, dissipation and embodiment (`premised_rests`, a corollary of `rests`) (P25b correction; originally “the eight together bring the world to rest”; see section 38, O9).
- **Boundaries.** Only the eight premises stated of worlds are mapped; premises relative to a continuation relation, a renewal relation, a decaying reserve or a family of conditions are not. Independence is relative to these eight. No part is evaluated, and the names are Ren's to choose.

The package now has 974 theorems and 1583 declaration audits, over a core closure of 28 modules and a package of 26, all source declarations with empty axiom reports. Section 32 has not yet been independently reviewed.

**P25: openness.** Section 30's `rests` brings a world to rest through finiteness; section 31 listed as open whether all premises bring a world to rest under a census and enclosure instead. Section 33 answers: the world need not be finite; what does the work is finitely many standing at each step (a census with every relatum embodied), together with enclosure (P25b correction; originally “enclosure, not finiteness, does the work”; see section 38, O1). It is a new L3 module `Becoming.Openness` (importing `Premises`) ([continued-change-needs-openness](../../../../theories/becoming/results/records/continued-change-needs-openness.md)).

- **Total standing runs down.** Where what stands at each step is listed, each once (`Web.StandingCensus`), the total standing across a step enclosed around what stands (`Flow.AroundStanding`) falls by at least the number of formations taking from the enclosing family (`standing_runs_down`), so it never rises, and any condition's standing rising or falling lowers it (`change_lowers`): a rise is given to, and giving needs uptake there; a fall is taken from (`fall_lowers_on`).
- **Rest from enclosure.** So where every step from some step on is enclosed around what stands, no standing changes at arbitrarily late steps (`stills`). A world with a census whose relata are all embodied, with a balanced, dissipative flow, enclosed from some step on, comes to rest (`rests_around`, `rests_enclosed`); the finiteness of the world is not needed, finitely many standing at each step is (P25b correction; originally “finiteness is not needed”).
- **Recurring arising opens.** Read the other way, arising that recurs in such a world is incompatible with every step from some point on being enclosed (`World.arising_opens`, named `generation_opens` before P23c): exchange beyond every finite family (P25b correction; originally “needs a step not enclosed at arbitrarily late steps”, constructively stronger).
- **Openness cannot be dropped.** In `exposed` the sides of `Handing` also take a unit from each of infinitely many ground relata and give it back at every step. It meets all eight premises and arising recurs in it; no step is enclosed, so dissipation binds at none (`exposed_world`). (P25b addition: its total standing is one at every step; activity needing support and bounded transmission hold vacuously too; it shows that enclosure does not follow from the eight, and the mutualists, every step enclosed, show that openness does not either; see section 38, O4–O6.)
- **Boundaries.** The world-level theorems need every relatum embodied, not only whatever arises; decidable equality is required by the constructive proof (P25b correction: it is not; see section 38, O3); dissipation binding only enclosed exchange is a disclosed feature of its representation. Neither openness nor rest is evaluated, and the names are Ren's to choose.

The package now has 994 theorems and 1612 declaration audits, over a core closure of 29 modules and a package of 27, all source declarations with empty axiom reports. Section 33 has not yet been independently reviewed.

**P23c: the ninth independent review.** A separate agent (Claude Opus 5.5) reviewed P18b, P19, P20, P21, P22 and P23 ([review](BECOMING-P18B-P23-REVIEW.md)). It recompiled the 27 modules of the core closure from the prelude, with empty axiom reports for all 1571 source declarations; of the closure's 4423 constants only 30 compiler-generated `injEq` lemmas depend on an axiom, `propext`, as the receipt lists. It accepted all the mathematics and closed L1–L10 of the eighth review. It raised ten findings (M1–M10): one reading chosen for Ren, four omitted premises, one error in prose, two missing counterexamples, and two of presentation and bookkeeping. P24 and P25, committed during the review, were not read by it; their wording affected by M1 is corrected too. The corrections are made in place and marked; section 34 records the handling.

- **Generative and degenerative (M1, the most serious).** P22 read the "generative, degenerative" of Ren's proposal as some relatum arising or ceasing at arbitrarily late steps, and the canonical texts then stated that in a finite world the two are one part and overlap. On 9 October Ren said that they do not overlap. The parts of the space are now named for what they are: arising recurring and ceasing recurring (`World.ArisingRecurs`, `World.CeasingRecurs`, `World.arising_iff_ceasing`; `World.arising_opens` in `Openness`). Ren's words stand beside the two readings the spine offers: as activity, arising and ceasing recurring coincide in finite worlds; as relations, renewing and consuming formations do not overlap (`Web.renewing_not_consuming`). Which parts the proposal's words name is listed first among Ren's choices.
- **Decidability (M2).** The finite-world law needs activity decided; over every world without it, the law is excluded middle (`World.law_decides`, from the review's probe). Decidability now appears in every list of the representation's commitments, and as a logical commitment beside the method, model, correspondence and normative premises.
- **What `price` divides (M3).** The identity divides the offspring's total into the parents' amounts weighted by their offspring and the change in transmission. The weighted total is not the selection term proper: it is k times the parents' total where every parent has k offspring (`selected_uniform`), and five where nothing is selected (`unselected`). The covariance form remains a further proof.
- **Premises restored (M4–M6).** Embodied arising in a finite family under balance and dissipation leaves the family open and, enclosed around, it draws in; a rise comes with another member's fall across a step at which the family is dissipated on; depletion follows for an event at whose steps the family is dissipated on and taken from; a transmitted need exceeds the giving step's level by at most the bound of transmission, and may never have been met where the bound is positive (`Slack`).
- **Witnesses (M7, M8).** `grazing` gives a finite world in which arising recurs and some event is not living without resting on the verdict about self-drawing at an ending: a grazer takes from a pool another relatum depends on (`grazing_world`, `grazing_not_self`). `leaking` replaces the balance witness of `rests_needs` with a world whose dissipation binds: the holder takes its own unit at every step and gives nothing (`leaking_world`).
- **Presentation (M9, M10).** The laws are tagged as identity by definition, arithmetic identity, or consequence of two-valuedness and finiteness. Wisdom moves to empirical correspondence. Section 31 and the plan state which completeness criteria are met: criteria 1 and 4; criterion 2 after this correction; criterion 3 for the ten premises stated of worlds, while premises relative to other relations and the "mixed" part are not mapped. Review stamps are at or before their commits, the foundation record uses the chapter's terms, and the last "giver" is gone (P25b correction: from the account of 生生; the witness constructor `Scatter.Relatum.giver` remained until P25b renamed it `source`; see section 38, O11).

The package now has 1016 theorems and 1662 declaration audits, over a core closure of 29 modules and a package of 27, all source declarations with empty axiom reports. Section 34 has not yet been independently reviewed.

**P26: ceasing needs arising, and the rest theorem.** Section 30's `rests` needs a finite world and section 33's `rests_around` needs every relatum embodied; the record continued-change-needs-openness left open whether an enclosed world comes to rest when only what arises is embodied. With a census of what stands as well, it does, by a counting law (P25b correction; originally “It does”; with a census of what is active alone it need not, `kindling`; see section 38, O2). Under a census of what is active, recurring ceasing needs recurring arising (`Web.arising_of_ceasing` in `Becoming.Population`; `World.arising_of_ceasing` in `Becoming.Openness`): a ceasing not preceded by an arising leaves fewer formations active, and the count cannot fall forever. Not conversely: `dawn` has a census and keeps arising while nothing ceases, and `dusk` keeps ceasing while nothing arises, so it has no census (`World.census_one_way`). The finite-world law of section 30 thus splits in two: ceasing to arising needs only a census, arising to ceasing needs more. The rest theorem follows (`World.comes_to_rest`): a balanced, dissipative world with censuses of what is active and of what stands, whose activity is decided and whose arising is embodied, comes to rest once every step from some step on is enclosed around what stands, since standing stops changing, so embodied arising stops, and ceasing stops with it by the census law. Finite worlds (`World.Finite.comes_to_rest`, the statement of `World.rests`) and worlds whose relata are all embodied (`World.rests_around`, now proved from the theorem) are its two cases. The census of what is active is needed: `dusk` meets every other premise, with nothing standing and every step enclosed, and keeps ceasing (`World.rest_needs_census`). That the theorem is strictly more general than its two cases is a comparison of statements; no witness covered by it alone is formalized. Enclosed steps without a census of what stands remain open (P25b: answered; `kindling` and `ember`, enclosed at every step, keep arising, `World.rest_needs_standing`).

The package now has 1029 theorems and 1676 declaration audits, over a core closure of 29 modules and a package of 27, all source declarations with empty axiom reports. Section 35 has not yet been independently reviewed.

**P27: the census law in general, and the bounded census.** Section 35's census law goes one way: under a census, ceasing recurring needs arising recurring, and dawn shows the converse fails. Section 30's law of finite worlds, that arising recurs exactly when ceasing does, thus splits in two, and section 35 left open what the other half needs. It needs exactly a bound on the count. Where the members of which a determination holds are listed at each step, each once (`Listed`, in `Becoming.Population`), a ceasing to be not preceded by a coming to be shortens the list and a coming to be not preceded by a ceasing to be lengthens it; the list cannot shorten forever, so ceasing recurring needs coming recurring (`Listed.coming_of_ceasing`, generalizing P26's helpers), and where no list is longer than B it cannot lengthen forever either, so the two recur together (`Listed.ceasing_of_coming`, `Listed.coming_iff_ceasing`). A census is this listing read of activity (`Web.Census`; `Web.unceasing_iff_bounded`), and the census of what stands is the listing of standing (`Web.StandingCensus`; `Web.StandingCensus.coming_of_ceasing`, `coming_iff_ceasing`), answering the next step of ceasing-needs-arising. Read of worlds (`Becoming.Openness`): where at most B relata are active at each step, listed (`World.CountedWithin`), arising recurs exactly when ceasing does; every census of a finite world is bounded (`World.Finite.countedWithin`), so the finite law is a case (`World.Finite.arising_iff_ceasing`); `procession`, with relatum x active at step x alone, is bounded and not finite and keeps arising and ceasing (`World.procession_world`); `dawn` has no bound (`World.dawn_unbounded`). By counting, arising and ceasing fall into three tiers: finite and bounded at each step, they recur together; finite but unbounded, ceasing needs arising and not conversely; no longer finite, ceasing can recur alone. The bound must hold at every step; the case bounded only from some step on, rates and the reading of dependence remain open. New record bounded-census-keeps-pace; ceasing-needs-arising revised.

The package now has 1045 theorems and 1697 declaration audits, over a core closure of 29 modules and a package of 27, all source declarations with empty axiom reports. Sections 35 and 36 have not yet been independently reviewed.

**P28: the census balance.** The census laws of sections 35 and 36 are laws of recurrence, and they left three next steps: a version with rates, a bound holding only from some step on, and the reading of dependence. All three are given here. The rates come from a balance. Where the members of which a determination holds are listed at each step (`Listed`), the list after a step with the members that ceased to be across it is the list before it with the members that came to be (`Listed.across`): the members kept across the step are counted alike on both lists (`marks_le_of_sub`). Summed over any stretch (`balance_over_stretch`), the list at the end with what ceased is the list at the start with what came (`Listed.over_stretch`), so ceasings exceed comings by at most the count at the start and comings exceed ceasings by at most the count at the end (`Listed.ceasings_within`, `Listed.comings_within`). This is section 26's `held_over_stretch` without a fixed finite family. Read of activity and standing: `Web.Census.over_stretch`, `Web.StandingCensus.over_stretch`. Read of dependence, with dependence pairs as members (`Web.DependenceCensus`): dissolving recurring needs forming recurring, and with a bound the two recur together (`forming_of_dissolving`, `forming_iff_dissolving`). The bounded law now needs its bound only from some step on (`Listed.ceasing_of_coming`, `coming_iff_ceasing`, `Web.unceasing_iff_bounded`); the world premise `CountedWithin` is the case of a bound at every step. The recurrence laws of P26 and P27 are limiting cases of the balance, though proved directly; joining the two routes remains open. New record census-balance; bounded-census-keeps-pace and ceasing-needs-arising revised.

The package now has 1061 theorems and 1716 declaration audits, over a core closure of 29 modules and a package of 27, all source declarations with empty axiom reports. Sections 35 to 37 have not yet been independently reviewed.

**P25b: the tenth independent review.** A separate agent (Claude Opus 5.5) reviewed P24, P25 and P23c ([review](BECOMING-P23C-P24-P25-REVIEW.md)). It recompiled the 29 modules of the core closure from the prelude, with empty axiom reports for all 1732 source declarations; of the closure's 4894 constants only 34 compiler-generated `injEq` lemmas depend on an axiom, `propext`, as the receipt lists. It accepted all the mathematics, closed M2–M10 of the ninth review and M1 in part, and raised eleven findings (O1–O11). P26–P28, committed during the review, were not read by it; their sentences affected are corrected too. The corrections are made in place and marked; section 38 records the handling.

- **Rest needs finitely many standing at each step (O1, O2).** "Enclosure, not finiteness" left out a premise the theorems use. The world need not be finite, but finitely many must stand at each step. `kindling` lists what is active, its arising is embodied, it balances and dissipates, and every step is enclosed around every relatum ever active, yet arising never ceases, since every unburnt fuel stands; `ember`, the same flow with every relatum embodied, is enclosed at every step with no census and keeps arising (`World.rest_needs_standing`). With a census of what stands, arising stops (`World.arising_stops`, from which `comes_to_rest` is now proved); ceasing need not (`dusk`).
- **No decision of equality (O3).** `rests_enclosed` and `arising_opens` hold without `DecidableEq`: an enclosed step is not not enclosed around any list (`Flow.Enclosed.around_not_not`), and `Flow.stills` needs each enclosure only not refuted, since what it compares are numbers.
- **The premises decide neither enclosure nor openness (O4–O6).** `exposed` meets the eight with no step enclosed and keeps arising, its total standing one at every step and its openness an exchange at zero net (`World.exposed_standing`); mutualists meet the eight with every step enclosed and come to rest (`World.openness_contingent`). Activity needing support and bounded transmission hold vacuously in `exposed`, as dissipation does.
- **Residues of M1 (O7, O8).** The web-level wording now says that arising recurs exactly when ceasing does. The activity reading has one status in the canonical texts: a candidate for Ren's choice. Ren's words are quoted ("generative和degenerate虽然都在一个becoming model上，但是他们不overlap吧"), and the AI's inference is labelled: if non-overlap is taken, the activity reading is not what is meant. Plan section 6 separates Ren's words from the AI's "as relations".
- **The map of premises (O9).** Decided activity is restored where a finite world is said to have a census. Giving needs uptake at each enclosed step (`World.acting_across`). A second balance witness takes from a closed family at every step (`World.draining_but`). `premised_rests` uses three of the eight, and independence is relative to the eight.
- **Grazing (O10).** Where activity needs support, a dependence left below its need and persisting at no lower need belongs to a relatum not active after the step (`Web.Dependent.inactive_below`), so the browser grazing undermines ends at that step (`World.grazing_browser_ends`). Whether undermining that co-occurs with the ending of the relatum depending counts against living is a new choice for Ren (P29b correction: the relatum depending is not active after the step, which is its ending only where it was active, and the choice covers dormant dependence too; section 42 R1), beside whether "openness" names exchange beyond every finite family or inflow. Living crosses ceasing as well as arising (`World.living_crosses_ceasing`).
- **Presentation (O11).** `law_decides` is glossed as implying excluded middle; its converse needs choice to turn a disjunction into decidable data, so it cannot be stated in the pure core (P29b correction: this is wrong; the converse can be stated and, with excluded middle as a hypothesis, is proved in the pure core with neither decidability nor choice, `World.law_of_em`, `World.law_iff_em`; section 42 R2). Other items: the `selected_le` docstring; the qualifier of the depletion sentence; how the counts of seven, eight and ten premises relate; and `Scatter`'s `giver`, renamed `source`.

The package then had 1077 theorems and 1739 declaration audits (receipt 20261009T145010.627958Z), over a core closure of 29 modules and a package of 27, all source declarations with empty axiom reports (count line added in P29b, R11).

**P29: the world in which each premise binds, and the names confirmed.** The tenth review noted that several witnesses in the map of premises have no flow, so the four premises about the flow hold there vacuously, as they do for the mutualists meeting all eight (O9). `World.Binds` says what it is for each premise to bind: something meets its condition. In `brood`, all eight hold and each binds (`World.brood_binds`): a parent takes two units of food and its own unit and gives its young one unit; the young comes to stand depending on the food as the parent did; the parent ceases; and infinitely many ground relata stand at nothing, so neither census comes from finiteness (P29b correction: only in that the whole world is not finite; the ground relata are idle, only three relata are ever active, and a census follows from the list of them; section 42 R3). Every step is enclosed, and the world comes to rest after one arising and one ceasing (`World.brood_rests`, by `rests_enclosed`). Binding is not independence: with every step enclosed, only active relata giving follows from taking and dissipation, yet it binds, since something gives. Ren, quoting the AI's progress note on M1, said "arising/ceasing is indeed better name" ([words](../../../../sources/15-codex-theory-conversations/2026-10-09-arising-ceasing-names.md)). The P23c rename stands: the activity reading is named arising and ceasing, English names Ren confirmed (the Chinese 生起／止息 being the AI's rendering; section 42 R9). What the proposal's "generative" and "degenerative" name remains Ren's to say.

The package now has 1086 theorems and 1760 declaration audits, over a core closure of 29 modules and a package of 27, all source declarations with empty axiom reports. Sections 35 to 39 have not yet been independently reviewed.

**P30: the recurrence laws from the balance, and growing bounds.** Section 37 left two items: the recurrence laws of P26 and P27 were proved from the lengths of lists, a second route beside the census balance; and what remains where the bound grows with the steps (whether, under logarithmic growth, arising can still go on without ceasing). Read of recurrence the balance is exact: ceasing recurs exactly when, from each step, some later list is shorter than the list at the start with what came between (`Listed.ceasing_iff_shortfall`), and coming to be recurs exactly when the list at the start is longer than some later list with what ceased between (`Listed.coming_iff_excess`). A quantity positive at arbitrarily late steps totals past every bound (`recurring_accumulates`, of which `Recurs.accumulates` is now a case). So the census law and the bounded law follow from the balance, as section 26's laws of a finite family already did; the six lemmas of the earlier route are no longer used and are removed from the core, their statements and checks kept in receipt 20261009T163512.365801Z and the commit history, and the two laws keep their names and statements. The bound need only return within some number at arbitrarily late steps (`Listed.ceasing_of_returning`; read of worlds, `World.CountedBy.arising_iff_ceasing`, of which `CountedWithin` is the case of a constant bound). A bound growing without end does not keep arising and ceasing together, however slowly: for every non-decreasing, unbounded `B`, in `slow B` the relata below `B t` are active at step `t`, relatum `B t` arises across each step at which `B` grows, and nothing ceases (`World.slow_world`); so under logarithmic growth arising can still go on without ceasing. Where the list grows without end, ceasing recurs where the comings over some stretch from each step outnumber the bound at its end (`Listed.ceasing_of_outpacing`), a sufficient condition, not a necessary one. The balance is also read of dependence (`Web.DependenceCensus.over_stretch`). Since the census law now follows from the balance, the dependency is reversed: census-balance no longer depends on ceasing-needs-arising, and that record and bounded-census-keeps-pace depend on it.

The package now has 1091 theorems and 1771 declaration audits, over a core closure of 29 modules and a package of 27, all source declarations with empty axiom reports. Sections 35 to 40 have not yet been independently reviewed; the eleventh review covers P25b to P29.

**P31: lagged coextinction along chains of dependence.** reserve-defers-ending and life-as-condition-of-life both listed lagged coextinction along chains of dependence under a reserve as their next step. P17 stated it across one link (`Carries.coextinct_lasts`), but its conclusion, that the formation is active only finitely often, gives no step from which the next link is unsupported. Under a reserve that decays (`Web.Decays`) the end step is explicit (`Carries.ends_within`), and the end runs down the chain: where the relata of a chain are embodied, each depends at a positive need on the one before it from step `T` on, and the first is inactive from `T`, each relatum is inactive from `chainEnd`, the first link ending at `T` and each later one once its reserve, read where the link before it ended, has passed (`Carries.chain_ends`). Since each reserve is read at the end of the link before, replenishment while supported is counted in the bound and needs no further premise. With the zero reserve every link ends at `T` (`chainEnd_zero`): coextinction at once along the chain, as under `Dependent` (`coextinct`). The bound is attained (`Cascade.cascade`): each relatum outlives the one it depends on by exactly one step, relatum `k` still active at step `k` with `chainEnd k` equal to `k + 1`. Without decay a dormant link can wake arbitrarily late, and turning "only finitely often" into an end step needs Markov's principle (P33b correction: the step is not constructive; even for decided activity happening at most once it implies LPO, `Web.lpo_of_ending`, which Markov's principle does not give; see section 45, T3); with excluded middle as a hypothesis, not an axiom, as for `law_of_em` in `Space`, what does not recur has a step after which it does not occur (`exists_not_of_em`), and each relatum of the chain still ends, with no bound (`Carries.chain_ends_of_em`). Along a graph rather than a chain, the bound holds along any chain reaching a relatum (P33b correction: P31's theorems needed an unending chain and were vacuous for finite ones; `chain_ends` is now stated for finite chains of n links and gives the bound along each finite chain reaching a relatum; see section 45, T2), since any unmet requirement leaves it unsupported.

The package now has 1109 theorems and 1793 declaration audits, over a core closure of 29 modules and a package of 27, all source declarations with empty axiom reports. Sections 35 to 41 have not yet been independently reviewed; the eleventh review covers P25b to P29.

**P29b: the eleventh independent review.** A separate agent (Claude Opus 5.5) reviewed P26, P27, P28, P25b and P29 at `0cf14b8b` ([review](BECOMING-P25B-P29-REVIEW.md)). It recompiled the 29 modules of the core closure from the prelude: all 1830 source declarations (1126 theorems) have empty axiom reports, and of the 5153 constants only the 35 generated `injEq` lemmas the receipt lists depend on an axiom, `propext`. Receipts, hashes, retained artifacts, reference hashes, proof bindings and the counts across phases all match. The mathematics is accepted and no Lean statement is wrong. It raised eleven findings: two errors in prose (R1, R2), six overclaims (R3–R8) and three items of presentation and provenance (R9–R11). P30 and P31 were not reviewed; P30 had already answered R6 and R11(a).

- **Undermining and ending (R1).** Where activity needs support, undermining an unchanged dependence leaves the relatum depending inactive after the step; it is that relatum's ending only where it was active (`Web.Dependent.ceases_below`). In `seedbank`, finite, balanced, embodied and with activity needing support, a drawer undermines a dormant seed's dependence and nothing in the world ever ceases (`World.seedbank_world`). The sentence "every undermining co-occurs with an ending" came from the tenth review; Ren's choice about such undermining now covers dormant dependence.
- **Excluded middle (R2).** The converse of `law_decides` can be stated: with excluded middle as a hypothesis, arising recurs exactly when ceasing does in every finite world, both directions, with neither decidability nor choice (`World.law_of_em`, with `quiet_of_once`, `persists_of_em`, `stays_failing`), so asked of every finite world without decidability the law is equivalent to excluded middle (`World.law_iff_em`). The core's axiom reports stay empty.
- **What the rest theorem adds (R3, R4).** Under the rest theorem's premises not unboundedly many relata ever stand or act (`Listed.few_of_quiet`, `World.few_active`, `World.rest_few`), and a census follows where what is ever active is listed (`World.counted_of_ever`). So the worlds it covers beyond finite ones add only relata that never stand or act; in `hatch` (renamed from `brood`, R10) the ground relata are idle and only three relata are ever active (`World.hatch_ever`, `World.hatch_idle`). Activity needing support binds there without being tight, and the flow premises bind at step 0 only. The record title and the chapter now say finitely many standing and finitely many active at each step.
- **Other overclaims (R5–R8).** "Arising recurs exactly when ceasing recurs" replaces "generation is unceasing exactly when ceasing recurs" in `Population` and the record (R5). R6 was answered by P30. Every census of a finite world is bounded by the number of its relata, with no decidability (`World.Finite.census_bounded`, R7). Openness with the eight premises does not give arising without end: `holding` meets all eight with no step enclosed and never arises or ceases (`World.holding_world`, R8).
- **Provenance (R9–R11).** Ren's sentence is quoted verbatim or glossed as a tag question presuming no overlap. What Ren confirmed is the English arising/ceasing, the Chinese 生起／止息 being the AI's rendering. The source file is retitled with a correction note, and chapter §8 quotes the AI note Ren replied to and asks Ren whether the activity reading remains a candidate. The English P25b paragraph and the plan's P25b and P29 rows gain their count lines and receipts.

The package now has 1131 theorems and 1826 declaration audits, over a core closure of 29 modules and a package of 27, all source declarations with empty axiom reports. Sections 40 to 42 have not yet been independently reviewed.

**P32: the census balance under a continuation, and the exact condition across one step.** identity-across-steps said that no split is sufficient for more to force arising, not necessary, with no exact boundary stated, and listed a necessary and sufficient condition as its next step. Across one step the condition is exact: for any lists before and after a step, more always leaves some formation after the step continuing none before it exactly when no formation continues as two (`forces_iff_noSplit`), since a formation continuing as two continues both members of a longer list; and arising is forced under every continuation without splits exactly when more formations are listed after the step than before, since otherwise pairing the lists in order (`paired`) continues every formation after the step without a split (`forced_iff_more`). Over a run a single split acts only at its step (`Fork`), and the exact condition on continuations would only restate the conclusion. The census laws read arising and ceasing under the identity the names stipulate; under any continuation, with a formation ceasing when no formation active after the step continues it (`Web.CeasesFrom`) and a merge one formation continuing two (`Web.NoMerge` excludes it), the census balance holds in two halves: without splits the formations after a step with those ceasing are at most those before with those arising, without merges at least, with neither exactly (`Census.balanceFrom`, `balanceFrom_eq`), the proof going through the continuing pairs (`mark_le_total`, `total_le_mark`, `total_swap`). Each formation continuing only itself has neither (`self_one_to_one`), and there this is `Listed.across`. Added up over stretches (`le_over_stretch`, `ge_over_stretch`, `gaining_of_losing`, `losing_of_gaining`), ceasing recurring needs arising recurring under every continuation without splits (`Census.arisingFrom_of_ceasingFrom`), and under a bounded count arising recurring needs ceasing recurring under every continuation without merges (`Census.ceasingFrom_of_arisingFrom`). Each condition is needed: in `Tandem` two formations are active at each step; read with each continuing only itself one arises and one ceases across every step, read as budding one ceases and nothing ever arises, read as joining one arises and nothing ever ceases, at most two active.

**P33: the exchange comes to rest.** The eleventh review (R3) observed that in `hatch` the flow takes part only at step 0 and gave a hand argument that under the rest theorem's premises this is forced, noting that it had not formalized it. It is now a theorem. Under balance and dissipation, with what stands listed, a formation taking part across a step enclosed around what stands that takes or gives anything lowers the total standing (`Flow.exchange_lowers`): the enclosing family holds what is exchanged, and under dissipation giving to it needs taking from it. Since the total never rises across such steps, where every step from some step on is, not refutably, enclosed around what stands, no formation takes or gives at arbitrarily late steps (`Flow.exchanges_finitely`, `World.exchange_stops`; `Flow.ExchangeRecurs` names recurring exchange). This does not follow from standing ceasing to change: in the cycle of `Becoming.Flow` standing never changes while a unit is taken and given back at every step. It needs neither the census of what is active nor embodiment, so the exchange coming to rest does not give activity coming to rest: `dusk` meets its premises while ceasing recurs (`rest_needs_census`). Each of the four premises is needed (`World.exchange_needs`): the exchange recurs without enclosure (`exposed`, meeting all eight premises), without dissipation (the cycle), without balance (`leaking`) and without the census of what stands (`kindling`, where enclosure around the empty list says nothing about what stands).

**P33b: the twelfth independent review.** A separate agent (Claude Opus 5.5) reviewed P30, P31 and P29b at `a9326202` ([review](BECOMING-P30-P31-P29B-REVIEW.md)). It recompiled the 29 modules of the core closure from the prelude: all 1896 source declarations (1171 theorems) have empty axiom reports, and of the 5333 constants only the 35 generated `injEq` lemmas the receipt lists depend on an axiom, `propext` alone; receipts, hashes, artifacts, 402 reference hashes, 112 bindings and the counts all match. The mathematics is accepted, with no Lean statement wrong; its 55 probe declarations are axiom-free. Eight findings are handled:

- **Names (T1).** A doubled `namespace World` made P30's world `Becoming.World.World.slow`; it is now `World.slow`, `World.slow_world` and `Slow.*`, as every text already said. The registry now checks each declaration a record names against the full names its bound receipt lists, where the receipt lists them.
- **Chains of any length (T2).** `Carries.chain_ends` and `chain_ends_of_em` asked every link to have a further link depending on it, so they held only of unending chains and said nothing of a food chain. They are now stated for finite chains of n links, the unending chain being the case of every n; where dependences climb a bounded rank no chain goes on without end (`Web.no_unending_chain`), and the cascade cut to three relata attains the finite bound (`short_cascade`).
- **Omniscience (T3, T5).** Turning ‘active only finitely often’ into an end step implies the limited principle of omniscience, even for decided activity happening at most once (`Web.lpo_of_ending`, with `Once`); the study's ‘needs Markov's principle’ was wrong. A list holding every member that ever holds, the strong form of `few_of_quiet`, implies it too (`Listed.lpo_of_few`, with `Few`). So the core states the weak forms, and the module docs now say ‘not unboundedly many’.
- **The rest (T4, T6–T8).** `holding_world`'s docstring now says `arising_opens` needs every relatum embodied; the bounded census's next step says the shortfall is the exact criterion and the rate form only sufficient; the source note dates the Chinese renderings 生起/止息 from P10 and P19; the plan row for P30 cites its receipts; the lean index lists another session's untracked drafts by design, and those files are left untouched.

**P34: the whole law of counting.** The open programme listed ‘a complete list of the laws holding of the whole space’, and the completeness criterion said the laws of the whole exclude nothing beyond what the representation excludes; until now nothing showed what all the laws of counting are. They are the tally, the kept form of the balance. (P34b correction: this first said that the census balance and the recurrence laws drawn from it are all the laws of counting, which is false; the balance equation of `Listed.across` is weaker than the tally, see P34b.) Across each step some members are kept, with what ceased making the list before and with what came the list after (`Listed.keeps`, from which `Listed.across` now follows); counts of this form are a tally (`Tally`), and every tally is counted by a queue whose members join at the back and leave from the front (`Queue.counts`). So a property of the counts holds of every listing, on every type, exactly when it holds of every tally (`counting_laws`); the property need only respect the counts' values at each step (`Pointwise`), in place of function extensionality, which the pure core does not assume. Read of worlds, relata queuing with nothing flowing meet every premise but embodiment and relata queuing that stand while active every premise but balance, so a property of the counts of a census holds in every world meeting either seven exactly when it holds of every tally (`World.counting_free`): premises lacking balance or embodiment leave counting free. Together, with only active relata giving, they bind it: what arises is given by a relatum active at the step, so nothing arises across a step at which nothing is active, which is no law of tallies (`World.counting_binds_jointly`). That is all the eight premises add: a queue tended by its front, which gives to each relatum joining, takes from each leaving and, while active, exchanges a unit each way with every ground relatum, meets all eight wherever nothing joins an empty queue (`World.tendedQueue_premised`), so under all eight the laws of counting are the tally and that nothing arises across a step at which nothing is active (`World.premised_counting`). No finite family is closed at a step at which the front is active, so dissipation holds there idly, as in `exposed`, and so do activity needing support and bounded transmission (`World.tended_not_binds`, P34b); the laws of counting under enclosure and in finite worlds are stated in P35. (P34b correction: this paragraph first gave sparing cancellation, whose prelude lemma carries `propext`, as a further merit of the kept form; the core has cancellation without axioms, and the reason for the kept form is that it is stronger.) New record: whole-law-of-counting.

**W1–W5: continuation grounding.** Ren proposed restating the Universal Metaethical Core from what wants its continuation: wanting gives one's continuation significance, the extent of what one must count needs no axiom, and one axiom closes the whole. The AI analysis, which Ren answered “exactly”, split it in two halves, and the proofs draw the line where it said, along dependence (scoped after the W8 review). The extent, with no ethical premise (`Becoming.Continuation`, L3): conveying and being fed from beyond are, with equality decided, exactly a step that is not inward (`Flow.inward_iff_not_fed`), so under balance and dissipation a finite family from which taking recurs, enclosed around from some step on, cannot from any step on be fed from nothing beyond it (`Flow.fed_from_beyond`, with rising and embodied-arising forms), while no source condition need recur, the one sun doing all the conveying (`Lone.supply_not_source`); draws each within what a step gives can jointly exceed it (`Pair.own_not_joint`), joint excess cannot outlast what was held (`Flow.excess_bounded`), and where renewal is given only by formations depending on what they renew it ends the renewers and every formation depending at such a need, a taker among them where it so depends (`Flow.joint_excess_ends`, `Exceeding.all_end`; with one taker all continue, `Alone.all_continue`); the joint count binds a want that outlasts what the condition holds. The extent so derived runs one way (`Downstream.one_way`), ends with the want (`Mortal.after_its_end`), and a careful keeper meets every requirement derived here while ending another formation (`Totalizer.careful`). The center (`Becoming.Standpoints`, L4): where every living claim is held, lying in some standpoint's own region, G0 is exactly S0 at every standpoint with N_std, using neither connection nor N_rel (`Valuation.significant_iff_held`); unheld lives need N_rel from a held one (`significant_iff_reached`); each premise is needed (`Apart.not_enough`, where neither neutrality holds; `Unclaimed`; `Relayed`); on a connected whole where every standpoint holds a living claim, S0 with N_rel is another completion (`Valuation.significant_of_transmits`); read stepwise each formation is its own center (`Web.significant_iff_self`); and with each formation valuing its own events and the keeper also the events that feed it (`Flow.FedBy`), the keeper's web has S0 everywhere and significance closed along feeding while another life has no significance from the keeper, so along dependence the center is not derived, while transmission along every formed relation fails in the same witness (`Totalizer.center_not_derived`). Read with one kind of relatum, conveyance is a candidate reading of related under which a continuing family's region is no cut (`Flow.region_not_a_cut`), relating two conditions, which interaction, living on and descent never do (`Flow.roles_conditions_unrelated`); adopting it is Ren's choice. Reading S0 as wanting and N_std as the one axiom is the AI's reading, pending Ren; G0 remains the adopted axiom until Ren accepts the restatement. New records: continuing-self-fed-from-beyond, own-count-misses-joint-excess, held-lives-g0-is-centering, conveyance-crosses-the-boundary, derived-extent-limits.

**W8: the independent review.** An independent Opus 5.5 agent reviewed W1–W5 ([review](CONTINUATION-GROUNDING-REVIEW.md), commit `1f6f375f`). The Lean is correct and axiom-free; the thirteen findings, six of them substantive, lie in the interpretation. The center witness's transmission conjunct followed from S0, so the witness is strengthened: with the keeper valuing also the sun's events, significance is closed along feeding, and in the same witness transmission along every formed relation fails, so the line holds along dependence (C1). N_std is one completion of S0; on a connected whole where every standpoint holds a living claim, S0 with N_rel is another (`Valuation.significant_of_transmits`, C2). `Lone` shows only that no source condition need recur (C3). Splitting the axiom into S0 and N_std is the AI's reading; a center at every point is S0, while N_std makes no center privileged (C4, C5). The joint count binds wants that outlast the stock, and takers end only where they depend at such a need (C6). The witnesses' endings and the sun's needing nothing are stipulated (C7, C13). What conveyance adds is a relation between two conditions (C8, `Totalizer.supply_not_cut_living_on`). The Chinese text uses 输送 for conveying (C9). The smaller corrections C10–C12 include quoting Ren's full message and adding the deontic reading of “not harm” to Ren's choices. Handling is in §47.1–47.4; the probes are kept as review evidence.

**P34b: the thirteenth independent review.** A separate agent (Claude Opus 5.5) reviewed P32, P33, P33b and P34 at `7f69f455`, with the drafts of P35 and P36 ([review](BECOMING-P32-P34-REVIEW.md)). It recompiled the 29 modules of the core closure from the prelude: all 2028 source declarations (1263 theorems) have empty axiom reports, and of the 5650 constants only the 37 generated `injEq` lemmas the receipt lists depend on an axiom, `propext` alone; receipts, hashes, artifacts, 1590 reference hashes, 459 bindings and the counts all match. The mathematics, the drafts' included, is accepted, with no Lean statement wrong; its 42 probe declarations are axiom-free. Nine findings are handled:

- **The headline (U1).** ‘The balance is the whole law of counting’ was too strong: the census balance is the equation of `Listed.across`, and the tally is strictly stronger, being exactly the balance with no more ceasing across a step than were listed before it (`tally_iff`); none listed, with one ceasing and one coming at every step, balances and is no tally (`balance_not_tally`). The law is now named as proved: the tally is the whole law of counting. The recurrence laws use only the equation and stand.
- **Ren's words (U2).** Two records said the counting of activity is not the proposal's generative and degenerative; they now carry the standard sentence, which leaves that to Ren and marks the conditional inference as the AI's.
- **Idle premises (U3).** In the tended queue, the witness of `premised_counting`, dissipation, activity needing support and bounded transmission hold idly (`World.tended_not_binds`); where every premise binds, every census counts an arising (`World.binds_arising`), which is no law under the eight alone (`World.binds_adds`).
- **The drafts (U4–U6).** Settling from some step is settling from the first, so the drafts' two laws are one; it is stated once, with a change bound from the first step, and the drafts' worlds are rebuilt without a start step or ground relata (P35). An end step for change implies the limited principle of omniscience (`ChangeBound.lpo_of_ends`, `World.lpo_of_finite_ends`). The core's arithmetic is gathered at the head of `Becoming.Dependence`, and `le_total_of_mem` moves to the totals of `Becoming.Flow`.
- **The rest (U7–U9).** `tally_iff_counted` states the whole law with no `Pointwise`; section 46 now says function extensionality, not classical logic, gives every property, and gives U1 as the reason for the kept form; `forced_iff_more` is glossed with formations listed, not standing; the open items move with P35; the registry checks aliases written as Lean names against the bound receipts.

**P35: counting under enclosure and in finite worlds.** P34 left the laws of counting under enclosure and in finite worlds open. Enclosure bounds change: in a world with a census whose relata are embodied, balanced and dissipative, with every step from `T` on enclosed, the relata active at any later step, together with the steps since `T` at which something arose or ceased, number at most the total standing at `T` (`World.enclosure_bounds_change`), since that total never rises across an enclosed step and falls at every step of change. A change bound from some step is one from the first (`changeBound_iff_zero`), and within it change does not recur (`ChangeBound.not_recurring`). Conversely an enclosed queue, whose front holds what the bound leaves beyond one unit for each member and exchanges only within the queue, has every step enclosed and meets all eight premises wherever a change bound from the first step holds of its counts and nothing joins an empty queue (`World.enclosedQueue_premised`). So under the eight, with every step from some step on enclosed, the laws of counting are the tally, that nothing arises across a step at which nothing is active, and a change bound from the first step (`World.enclosed_counting`). The queue never reaches past its `B + B * B`-th member (`ChangeBound.reach`), so on those places it is a finite world meeting the eight (`World.finiteQueue_premised`), in which dissipation binds and the bound is attained (`World.finite_dissipation_binds`, `World.replaced_attains`): finite worlds have the same laws of counting (`World.finite_counting`, `World.enclosed_iff_finite_counting`). That change does not recur cannot be strengthened to a step after which nothing arises in every such world without the limited principle of omniscience (`World.lpo_of_finite_ends`). Activity needing support and bounded transmission hold idly in the queue, as in P34's witness; the laws of counting where every premise binds are not stated. The names follow Ren's naming criteria of 10 October ([source](../../../../sources/15-codex-theory-conversations/2026-10-10-zero-axiom-part-and-names.md)): the drafts' ‘budget’, a financial word, became the change bound (`ChangeBound`) and the enclosed queue (`EnclosedQueue`) before commit. New record: counting-under-enclosure.

**P36: witness names.** Ren asked for the strongest claim without axiom as Part I and one axiom as Part II. Ren delegated names under four criteria:
- the most precise word;
- in the zero-axiom part, formal words describing the abstract dynamics;
- scientific and systems words;
- social and financial words not the first choice.

P36 renames the core's remaining witnesses accordingly, together with the declarations named after them:
- `Handing` → `Shuttle`
- `Kindling`/`Ember` → `Throughput`/`EmbodiedThroughput`
- `Spending` → `SelfDrawing`
- `Keeping` → `Lossless`
- `Tended` → `OpenQueue`, the counterpart of `EnclosedQueue`
- `Commons` → `Renewable`, with the runs `withinRenewal` and `beyondRenewal`
- `Totalizer` → `Clearing`, with clearer, dweller and resource, and `careful` → `undermines_within_renewal`
- `sun` → `source`
- `Dawn`/`Dusk` → `Accretion`/`Attrition`
- `Garden` → `Expansion`
- `Bloom` → `Oscillation`
- `Stranger` → `Unrelated`
- `Crowd` → `Unrecorded`
- heir/elder → successor/predecessor

The full table is in plan section 10.

Statements, proofs and counts are unchanged: receipt 20261010T083222.285294Z has 1356 theorems and 2161 declaration audits, and the periphery receipt is 20261010T084107.973758Z. Historical sections, receipts and reviews keep the old names and are read through the table. Part II vocabulary waits for the axiom Ren chooses.

**P37: what can form next.** Ren confirmed two readings. Possibilities are what can form next, compared by inclusion, with a formation's contribution the difference between the future with it and without it. The whole is never any center's model of it, so inclusion licenses no imposed ending. P37 states this on the spine with no axiom, in two new modules, `Becoming.Admission` (38 theorems) and `Becoming.Regions` (18).
- **Admission.** Levels admit a formation when they meet every requirement it has; support is admission by the levels that stand. Where requirements do not loosen, support is gained only through a rise, and in a balanced flow where only active formations give and activity needs support, only from the supported. So where nothing beyond gives, the end absorbs, and each premise of that is needed (`Restoring`).
- **The boundary is a net exchange.** A part withheld leaves the rest of the exchange as it was; its levels are unique where they exist, and the accounting is exact. The boundary is exact (`supported_iff_within_margin`): a formation is supported exactly when, on every condition it requires, the part's cumulative net draw stays within the margin by which the levels without it meet the need. So closing what can form needs a net draw on a condition required, beyond the margin (finding that condition uses classical logic), and opening needs a net give.
- **Four cases.** Compared by inclusion, a part widens (`Inflow.widens`), narrows (`Clearing.narrows`), keeps the same (`changes_nothing`) or is mixed (`Transfer.mixed`); the split into these four uses classical logic. Ordering mixed parts needs a measure, a further premise.
- **Levels.** What holds within a region holds within every region inside it, what is lost beyond a region is lost beyond every region inside it, and nothing lies beyond the whole. The clearer continues and closes nothing within its dependence while closing the dweller beyond it (`Clearing.loses_beyond`). This is the free-rider counterexample to "only non-degenerating dynamics continue indefinitely", which holds of the whole and not of parts.
- **Represented boundaries.** Renewal over a region of conditions:
  - is renewal at the step where the region covers the formation's participation;
  - keeps its own support where the region covers its requirements, yet may undermine another;
  - can lose its own support where the region omits a requirement (`Omitted.loses_own`).

Reading these as Ren's generative, degenerative and neutral, and as self, system and whole, is the AI's reading, pending Ren. The receipt is 20261010T100351.523624Z and the periphery receipt 20261010T100610.366844Z. Records added: support-from-the-supported, closing-needs-net-draw, four-cases-of-a-part, loss-beyond-a-region and represented-boundary-against-dependence. The author's counterreview is in section 51.

Section 52 (P38) states what each premise adds to counting, under every selection of the eight premises. A second route binds counting without any premise on giving: under balance, taking, dissipation and embodiment, nothing is taken at a step at which nothing is active, whatever is given comes to stand and so is active after the step, the relata active after it form a closed family, and dissipation lets nothing be given to it (`World.taking_binds_counting`). At an enclosed step, balance, dissipation and embodiment suffice (`World.enclosed_binds_counting`). So under each of the 256 selections the laws of counting are the tally alone, or the tally with nothing arising across a step at which nothing is active. The second holds exactly where balance and embodiment are selected with only active relata giving, or with only active relata taking and dissipation (`World.counting_under`, `World.counting_binds_iff`). Every other selection is met by a queue that counts every tally: the queue standing while active, the queue with nothing flowing, a queue driven by an idle ground relatum (`World.drivenQueue`; P41b note: an inactive ground relatum, as it takes part at every step, section 58), or the open queue. In worlds enclosed from some step on, one more condition is added exactly where balance, embodiment and dissipation are selected: from some step on, change stays within a bound and nothing arises across a step at which nothing is active (`World.enclosed_counting_under`). The witness there is an enclosed queue closing at that step (`World.closingQueue`). The chapter now has a Part I header before section 1, Part I stated whole after section 5 (what holds of every unfolding, what each premise adds, where the dynamics stop deciding), and a Part II header before section 6, quoting Ren's proposed axiom and route (a), with G0 the adopted axiom until P39 proves it; headings and anchors are unchanged. The laws under each selection in finite worlds, and where every premise binds, are not stated. Receipt 20261010T101327.506085Z has 1430 theorems and 2280 declaration audits; the periphery receipt is 20261010T102016.503705Z. The section has not been independently reviewed.

**P39: what the one axiom yields.** Ren proposed one axiom, “for anything, its continuation into the future has significance(doesn't have to be positive, we could argue as long as not harm), or continuation into the future needs to create more significance(being generative)”, and chose route (a), with G0 as its target theorem. Ren then answered that a center and its boundary exist only within cognitive structure and dynamics, so no axiom decides whose continuation matters, and that not harm is a phase transition with a clear boundary. Section 53 therefore states the axiom as Ren's words, not as a center at every wanting point. `Becoming.Significance` (27 theorems) reads it as boundary neutrality for the significance of continuation (`Unrestricted`): from every standpoint, the continuation of anything has significance at every step.
- **G0 follows, immediately.** Take any reading in which a claim's significance is that of a formation's continuation at a step; the stepwise, relation and whole-run readings are such readings. On it, G0, S0 at every standpoint, both neutralities and a seed follow, with no connection used (`Valuation.premises_of_unrestricted`). On level paths C follows too, with better read as retaining and adding (`Web.paths_g0_comparison`). G0 is the axiom restricted to living claims; A, L and J1–J4 remain premises.
- **Not harm is the margin.** Under the axiom retaining what has significance is inclusion. So a part does no harm exactly where its net draw stays within the margin, loses a continuation exactly where the draw exceeds it, and adds one exactly where its net exchange brings a formation within it (`Flow.Balances.retains_iff_within_margin` and its two companions). Ren's strong form is the generative case of the weak one.
- **What has not yet formed counts.** A drawer taking a condition before any dependence on it forms is living on the stepwise reading, yet under the axiom it loses a possibility (`Preemption.not_undermining_yet_loses`). Which reading G0's living names is Ren's choice.
- **The whole first.** What retains in the whole retains within every region (`Web.Retains.within`), and not conversely. Centers bounded by their dependence license the free rider and disagree (`Clearing.centers_disagree`). Under the axiom the free rider's part loses the dweller from every standpoint, and withholding it ends nothing (`Clearing.free_rider_loses`).
- **The axiom is needed.** Where nothing has significance, nothing is ordered (`Web.significance_undetermined`).

G0 remains the adopted axiom until Ren accepts this axiom in its place. Records added: one-axiom-yields-g0, significance-retained-within-margin and whole-first-and-bounded-centers. Receipt 20261010T110824.890630Z has 1457 theorems and 2316 declaration audits; two earlier passed runs, 20261010T104700.459715Z and 20261010T105720.952257Z, differ from it only in documentation (three passages of the module's and one of the root module's). The periphery receipt is 20261010T111624.656993Z. The author's counterreview is in section 53, and the section has not been independently reviewed.

Section 54 (P38b) completes what each premise adds to counting, in finite worlds. Every step of a finite world is enclosed, so there balance, embodiment and dissipation bind counting by themselves at every step and bound change from the first step, and every census is bounded. Under each selection of the eight premises the laws of counting in finite worlds are those of a tally with at most some number active at each step, adding that nothing arises across a step at which nothing is active where balance and embodiment are selected with only active relata giving or with dissipation, and a change bound from the first step where balance, embodiment and dissipation are selected (`World.finite_counting_under`, `World.finite_counting_binds_iff`, `World.finite_change_bound_iff`): three kinds of law, where worlds in general have two. The finite witnesses seat the members of a queue in turn round a ring of 2M + 1 places, where at most M are in the queue at each step, so members in the queue before or after any step hold distinct places and the ring counts what the queue counts (`Ring.slot`, `Ring.slot_inj`, `Ring.counts`); the ring is defined by its own recursion because the prelude's remainder lemmas carry `propext`. A ring with nothing standing meets every premise but embodiment, one whose places stand while held every premise but balance, and one whose front's place also takes what falls and gives what rises every premise but dissipation (`World.ring_meets`, `World.embodiedRing_meets`, `World.balancedRing_meets`). Finite worlds and worlds enclosed from some step on have the same laws of counting under a selection exactly when it bounds change and binds counting (`World.enclosed_iff_finite_counting_under`); this corrects the scope of the Part I statement's earlier sentence that finite worlds have the same laws, which holds under all eight premises (`World.enclosed_iff_finite_counting`) and not under every selection. The laws where every premise binds are not stated. Receipt 20261010T112632.899583Z has 1488 theorems and 2361 declaration audits; the periphery receipt is 20261010T112836.954648Z. The section has not been independently reviewed.

Section 55 (P38c) gives the laws of counting where every premise binds. Under the eight premises the laws of counting are the tally and that nothing arises across a step at which nothing is active (`World.premised_counting`), but in its witness three premises hold idly (`World.openQueue_not_binds`, the thirteenth review's U3 probe); where every premise binds, every census counts something arising (`World.binds_arising`), and it was open whether binding adds more. It does not: where every premise binds, the laws of counting under the eight are exactly the tally, that nothing arises across a step at which nothing is active, and that something arises (`World.binding_counting`). The witness is a binding queue, open across every step but one, `T`, at which its front stands `E` more; across `T` it exchanges only within the queue and loses that excess, so what stands falls and dissipation binds, while every relatum depends on every relatum at what it stands at, so activity needing support and bounded transmission bind wherever something joins (`World.bindingQueue_exceeds`, `World.bindingQueue_premised`, `World.bindingQueue_binds`). (P41b note: these two premises hold there whatever is active and whatever flows, binding only in that their conditions have instances; the queue is renamed the queue closed once, `OnceClosedQueue`; see section 58.) Every premise binding decides neither rest nor change without end: in `hatch` arising stops, and in a binding queue in which one member replaces another at every step arising and ceasing recur (`World.binding_contingent`); the open programme's sentence that the world in which every premise binds comes to rest is about `hatch` only and is corrected. No finite world binds every premise, a census binding only where the world is not finite. The laws where the premises of each selection bind are not stated. Receipt 20261010T132639.927992Z has 1512 theorems and 2392 declaration audits; the periphery receipt is 20261010T132949.908183Z. The section has not been independently reviewed. (P41b note: it has since been checked by the fourteenth review; see section 58.)

**P40: how far the route without axiom reaches.** Ren chose to aim for route (a) first and then to try route (b). Route (b) is the AI's wording, which Ren quoted: it adds no axiom and reads “should” as what a center does once its represented boundary matches what it actually depends on; section 56 quotes it in full. P40 asks which level that route reaches. `Becoming.Interdependence` (28 theorems) adds no axiom; the axiom appears only as a hypothesis of comparisons.
- **What a continuation depends on is reached without premise.** A formation's feeding closure is the least region holding it that is closed under feeding (`Flow.WithinFeeding`). Nothing beyond it gives, at any step, to a condition a member then requires (`Flow.beyond_gives_nothing`). In `Clearing`, section 53's region along dependence is exactly each formation's feeding closure (`Clearing.dependenceRegion_iff`); P37 had checked that match only by inspection.
- **The constraint runs along feeding.** Under balance, with only active formations giving and activity needing support, consumption whose feeders are all unsupported lasts at most as many steps as the level of what it consumes (`Flow.Balances.consumption_ends_with_feeders`). In `Overshoot` a formation renews over the one condition it requires and keeps its own support across the step, yet ends through its feeder (`Overshoot.ends_through_feeder`). Taking only from their own conditions, both continue (`Overshoot.steady_continues`).
- **What lies beyond the closure need not return.** In `Clearing` everything within the clearer's closure is supported at every step, while the dweller, beyond it, ends (`Clearing.closure_supported`).
- **Where the route meets the axiom.** Significance bounded by the whole is the axiom (`bounded_whole`). Wherever every formation the other path admits lies in the region or is admitted by the first, the verdict bounded by the region is the axiom's (`Web.retains_bounded_iff_retains`). So it is on every comparison where a formation's feeding closure is the whole (`Flow.within_closure_iff_retains`). In `Clearing` the two part (`Clearing.within_closure_yet_loses`).

On the AI's reading, pending Ren, route (b) reaches the self and the system one is in, and the whole only where the whole is one feeding closure. A center that wants its continuation and represents its closure has its own reason to retain what lies within it; this explains motivation and is not a warrant. What the axiom adds is significance for continuations whose loss returns to no one, such as the dweller's. G0 remains the adopted axiom. Records added: feeding-closure, consumption-ends-with-feeders and closure-verdict-meets-axiom. The limitations and next steps of loss-beyond-a-region, whole-first-and-bounded-centers and represented-boundary-against-dependence are revised; their claims are unchanged. Receipt 20261010T133601.876717Z has 1540 theorems and 2426 declaration audits; the periphery receipt is 20261010T133831.669969Z. The author's counterreview is in section 56, and the section has not been independently reviewed.

**What the premises add to the laws of counting forms its own module (P41).** Following Ren's request that the codebase be elegant structurally and conceptually, the part of the core stating what the premises add to the laws of counting moves from `Becoming.Premises` and `Becoming.Openness` into a new module, `Becoming.Counting` (130 theorems), which imports `Becoming.Openness`. It states, in one line: under all eight premises, under each selection, with enclosure from some step on, in finite worlds, and where every premise binds. `Becoming.Premises` keeps the map of premises and their selections by name; `Becoming.Openness` keeps the rest theorem and openness. Names, statements and proofs are unchanged; the three section headings now say "each selection", as the module documentation does. The three records citing moved declarations cite them in Counting. Receipt 20261010T145237.259199Z (1540 theorems, 2426 declaration audits, core closure 36 modules, package 34); periphery receipt 20261010T145910.464504Z.

**The fourteenth independent review and its corrections (P41b).** Another agent (Claude Opus 5.5, an author of none of it) reviewed P34b, P35, P36, P36b, P38, P38b and P38c ([review](BECOMING-P34B-P38C-REVIEW.md), object `c95f6576`). It recompiled the 34 closure modules from the prelude outside the repository: all 2462 closure source declarations the receipt lists have empty axiom reports, and only the 38 generated `injEq` lemmas depend on `propext`, as listed. The six commits' receipts, hashes and retained artifacts match. P36 is a pure renaming by token comparison. The mathematics is accepted, with no wrong Lean statement, and its 32 probe declarations depend on no axiom. Of six findings, V1 and V2 matter most. V1: in the witness for `binding_counting`, activity needing support and bounded transmission hold whatever is active and whatever flows, so "binds" means only that each condition has an instance. This is now said wherever binding is described, and checked (`OnceClosedQueue.dependent_any_activity`, `OnceClosedQueue.transmits_any_flow`). The `World.Binds` docstring says an instance need not exclude anything. A stronger reading of binding is listed as open, for Ren. V2: plan section 10 now says Part I *aims at* the strongest claim with no axiom. The P38 row is scoped. The Part I statement ties "complete" to plan section 9's four checkable criteria and says that being the strongest has not been shown. V3: the Part I statement now says each *theorem* is checked, and states the enclosure law with its step. It names the premises of the end-step and parts-and-regions theorems, and gives the counting bullet's boundary in place. V4: new core theorems `World.enclosed_change_bound_iff`, `World.Finite.not_binds` and `World.finiteHatch_binds_but_census`. The last shows a finite world meeting the eight in which every condition but the census has an instance. The laws of counting in such worlds are listed as open. V5: stale record fields, chapter section 8 and the P36 table (`Provisioned.gift → provision`) are corrected, and `add_sub_turn_add` moves to Dependence. V6: the driver is an inactive ground relatum, "hold idly" becomes "hold vacuously", and the binding queue is renamed the queue closed once (`OnceClosedQueue`) for its dynamics. `credits` and `overdraw` are left for a later sweep under Ren's naming criteria. Receipt 20261010T150853.470895Z (1552 theorems, 2445 declaration audits); periphery receipt 20261010T151108.093153Z.

**What the unit of amounts carries: rest at every resolution (R1).** Following Ren's "we push pareto frontier" and "keep going please, agree with direction" ([source](../../../../sources/15-codex-theory-conversations/2026-10-10-pareto-frontier.md)), read as stating each claim in its strongest true form with the exact boundary where it fails. The spine counts amounts in natural numbers of one unit, so dissipation loses at least a unit at every exchange, a quantum on which the rest and openness laws rely. The new module `Becoming.Resolution` lets the unit split into finer units across each step (`Flow.BalancesAt`), separating the dynamics from that quantum.
- **The loss law.** Whatever the refinement, the quanta of the unit of step `T` a never-rising quantity loses, counted from `T`, number at most `q` times the quantity there (`losses_bound`). So a closed family loses at least `1/q` of the unit at no more than `q` times its stock steps (`Flow.quantum_bound`); with the unit fixed, taking from a closed family stops (`Flow.taking_stops`).
- **Loss in proportion.** Where every formation gives a closed family at most `q/(q+1)` of what it takes (`Flow.DissipativeBy q`), the formations taking at least `1/p` of the unit number in all at most `p(q+1)` times the stock (`Flow.exchange_bound`). In a world with a census, embodied relata and every step from `T` on enclosed, the relata gaining at least `1/p` of the unit number in all at most `p q` times the total standing (`World.growth_bound`), so such gains, and arising at that size, do not recur (`World.growth_not_recurring`, `World.arising_not_recurring`).
- **The boundaries.** Each witness is balanced at a unit splitting without end and dissipative, and lacks one premise. `Asymptote`, losing all it takes, is taken from without end exactly where the unit splits without end. `Emission`, with a census, embodied relata, every step enclosed and half of what it takes lost, has a new relatum arise at every step at sizes shrinking without bound. `Circulation` exchanges, and `Alternation` has arise in turn inside an enclosure, one whole unit at every step; by the two laws neither is dissipative by any share.

On the AI's reading, pending Ren: with bounded efficiency, enclosed generation of any fixed size stops, and inside an enclosure it can continue only ever finer or ever closer to lossless. This answers, for rational amounts and discrete steps, the next step of continued-change-needs-openness; continuous time and real amounts remain open. The first checker run failed on a name clash with `Becoming.Admission` (`Transfer`, now `Alternation`; receipt 20261010T154024.599588Z retained). Record added: rest-at-every-resolution. Not yet independently reviewed; the author's counterreview is in section 59.

**Falling, ceasing and reserve at every resolution (R1b).** Under the same resolution and premises, the relata falling by at least `1/p` of the unit inside an enclosure, counted relatum by relatum and step by step, number at most `p(q+1)` times the total standing at `T` (`World.fall_bound`): what falls is taken (`Flow.BalancesAt.loss_taken`), and loss in proportion makes the enclosing family lose at least `1/(q+1)` of what is taken (`Flow.BalancesAt.losers_lose`), where it loses at least `1/q` of what is given, so the bound for falling is `p(q+1)` and for growth `p q`. An embodied relatum ceasing falls to zero, so ceasing at that size does not recur either (`World.ceasing_not_recurring`), and with R1 neither arising nor ceasing at that size recurs (`World.rests_at_resolution`): the rest theorem at every resolution. A reserve read in a refining unit that only falls (`Web.CarriesIn`, the spine's `Web.Carries` when the unit is fixed, `Web.carriesIn_one`) may fall forever. Where each active step beyond support costs at least `1/p` of the unit (`Web.CarriesAt`), a formation unsupported from `T` on is active at most `p` times its reserve at `T` (`Web.CarriesAt.lasts`, by the same loss law), the spine's reserve being the case of `p` one at a fixed unit (`Web.Carries.carriesAt`). In `Dwindle`, at a unit halving at each step, a formation never supported is active at every step, its reserve `1 + 2^-t` units of step 0 falling towards one unit and never reaching zero, with no least cost (`reserve_needs_quantum`). The least cost is a premise, the unit-free counterpart of the spine's one-unit fall. The same record is revised, with reserve-defers-ending as a new dependency. Receipt 20261010T163746.432774Z, periphery receipt 20261010T164738.513555Z. Not yet independently reviewed; the author's counterreview is in section 59.1.

**Loss in proportion per family, and a least loss at each size (R2).** Every law of R1 and R1b uses loss in proportion only summed over the closed family, so `Flow.DissipatesBy q` now says just that: each closed family gets back at most `q` parts in `q + 1` of what is taken from it. It holds where each formation does so (`Flow.DissipatesBy.of_each`), not conversely, so every law keeps its statement under a weaker premise, and the witnesses dissipative by no share now fail the weaker premise as well. A different weakening, a least loss at each size (a formation taking at least `1/p` of the unit loses at least `1/m` of it, `m` the same at every step, `Flow.LosesAtSize`), gives the exchange law with the spine's dissipation (`Flow.exchange_bound_of_least_loss`), but not the growth law. In `Trickle`, at a unit quartering at each step, a whole unit of step 0 passes between two sides in `2^t` parts at step `t`, each losing two units of the step after: every size has a least loss and transfers of each fixed size stop, yet a whole unit arises without end, with no share lost (`growth_needs_proportion`). Counting transfers needs a least loss at each size; counting what relata gain, lose, begin or end needs more, since one gain can be split across any number of transfers. Whether a premise weaker than the family's share still gives the growth law is not stated, and the carriers of `Trickle` are not active. Receipt 20261010T165248.121581Z, periphery receipt 20261010T165548.911356Z. Not yet independently reviewed; the author's counterreview is in section 59.2.

**The amount law (R3).** Every law of R1 to R2 counts: the times something takes, gains or falls by at least `1/p` of the unit. All their proofs pass through one inequality per step, and that inequality itself gives a law naming no size. Summing each step's amount in the unit of step `T` (`refinedSum`), everything taken from a family closed from `T` on is at most `q + 1` times its stock at `T`, and everything given back at most `q` times (`Flow.uptake_bound`, `Flow.replenishment_bound`). In a world with a census, embodied relata and every step from `T` on enclosed, the same holds of what is taken from and given to what stands (`World.taken_bound`, `World.given_bound`). The bound is the least. In `Geometric` a formation takes a closed pool in full at each step and gives back `q` parts in `q + 1`, at a unit splitting into `q + 1`. Everything taken comes within `1/m` of `q + 1` times the pool for every `m` (`amount_sharp`, through Bernoulli's inequality). Every count follows from the amount law (`counts_of_amounts`), and the exchange, growth and fall laws are now proved this way, their statements unchanged. In `Trickle`, where every size has a least loss, everything taken grows past every multiple of the unit (`throughput_needs_proportion`). Done before Ren's choice of A and committed with R4; by Ren's choice this line is kept as research notes. The same receipt as R4. Not yet independently reviewed; the author's counterreview is in section 59.3.

**Rest with the refinement counted; the fifteenth review (R4).** Asked whether each closed family should lose a fixed proportion of what is taken from it as a premise, Ren answered on 11 October 2026 that a least difference at every exchange belongs to becoming (‘A is right - because of change, there is difference’), asked ‘for the case of 0, why can't we have it?’, and asked that the other options be kept as research notes ([source](../../../../sources/15-codex-theory-conversations/2026-10-11-difference-in-becoming.md)). Splitting the unit into `split t + 1` is itself a change. Counted as a formation that gives each condition `split t` times its level and takes nothing (`Flow.withRefinement`), balance at the refining unit is the spine's balance (`Flow.balancesAt_iff_withRefinement`). The spine's dissipation excludes giving without taking: with the refinement counted, a flow dissipates on a family exactly where its own formations do and the refinement gives the family nothing (`Flow.withRefinement_dissipatesOn_iff`), and across a step enclosed and dissipated on with it counted the refinement gives nothing (`Flow.refinement_gives_nothing`). So with the refinement counted the spine's premises bring rest at every resolution with no premise added (`World.rests_refinement_counted`), and arising without end needs openness (`World.arising_opens_refinement_counted`). Without counting it, the same holds wherever the refinement gives nothing (`World.rests_unrefined`, `Flow.taking_needs_refinement`, `Web.CarriesIn.lasts_unrefined`), and every witness of R1 is fed by the refinement (`refinement_feeds_witnesses`) and does not balance at the fixed unit (`Asymptote.not_balanced`, `Emission.not_balanced`, `Alternation.not_balanced`). The line of loss in proportion (R1 to R3) is kept as research notes. The fifteenth independent review of R1, R1b and R2 ([review](BECOMING-R1-R2-REVIEW.md)) found the build, axioms, receipts and statements correct and the prose wrong in places: an overclaimed necessity (W1), an inverted Chinese sentence (W3), dissipation missing from the quantum law (W4), quantifier slips (W8) and financial words (W10, now ‘least fall of the reserve’, ‘proportion’ and Trickle's ‘conduits’). All are corrected, the historical passages kept with correction notes; the review's probes are kept as research notes. On the AI's reading, pending Ren: a finer distinction is itself a becoming that something must give, so arising without end needs openness at every resolution with only the spine's premises. Ren then read the least loss per exchange as entropy and confirmed that ‘the case of 0’ means zero premises (‘pure thermodynamics, at atomic level, each exchange between objects holds the conservation of energy, but entropy still rise. zero premises.’). Counting the refinement adds no premise to the spine's, while the spine's dissipation stays its premise. Whether lossless exchanges exist, and whether the least loss can be derived rather than supplied, is taken up in a separate session; the candidate statements relayed to it are in section 59.4. Record rest-with-refinement-counted added; rest-at-every-resolution revised. Receipt 20261010T180948.563939Z, periphery receipt 20261010T182121.048951Z. Not yet independently reviewed; the author's counterreview is in section 59.4.

**The laws of counting where the premises of each selection bind (P45).** Following Ren's "let's aim for the strongest claim without axiom, as the first part" and "aim a complete theory of becoming, and finish related work", this states the two laws of counting that P41b left open (section 58). A premise now binds on its own (`World.Premise.Binds`), each condition as before, and `World.Binds` is every premise binding. Under each selection, where each selected premise binds, the laws of counting are those of `World.counting_under` and at most three more (`World.binding_counting_under`); each is what an instance of a condition leaves in the counts, and each is a law exactly under the selections named.
- **Something is active,** exactly where activity needing support, only active relata giving, only active relata taking or embodiment is selected (`World.binding_activity_iff`): the first three have an active relatum as their instance, and what arises is active after the step.
- **Something arises,** exactly where embodiment is selected (`World.binding_arising_iff`).
- **Something arises across a step at which something is active,** exactly where embodiment is selected and the selection either binds counting or selects only active relata giving and bounded transmission (`World.binding_joint_iff`): with transmission binding, a descendant arises from a participant, active where only active relata give.
- **The witnesses.** A saturated web, every relatum depending on every relatum at what it stands at, keeps the premises a world meets where levels are bounded (`Web.saturated`, `World.Premised.saturated`). Without embodiment, a relay beside a queue hands one of two units on to a ground relatum and loses the other (`World.relayQueue_binding`). With embodiment but without balance, a lossy queue's front, across one step, exchanges a unit each way with itself and each member joining and loses one unit more, which no standing records (`World.lossyQueue_binding`). With embodiment and balance, the queue closed once, which now exchanges across every open step at which it is not empty before or after, so that binding no longer needs nothing joining an empty queue (`World.onceClosedQueue_binding`), and the open queue with its web saturated (`World.openQueue_saturated_binding`).
- **Finite worlds.** Where every premise but the census binds, the laws of counting under the eight are those of finite worlds and that something arises (`World.finite_binding_counting`), witnessed by the finite queue with its web saturated (`World.finiteQueue_saturated_binds`). The laws in finite worlds where the premises of each selection bind are not stated: there taking with dissipation gives only active relata giving across enclosed steps (`World.Finite.acting`), and finite witnesses are needed.

On the AI's reading, pending Ren: binding leaves in the counts only its instances, activity and arising, and arising at a step of activity where arising is bound to come from activity. Records extended or revised: whole-law-of-counting, map-of-premises, counting-under-enclosure. Receipt 20261010T171040.121853Z (Premises 59, Counting 161). Not yet independently reviewed; the author's counterreview is in section 60.

**P42: feedback and reach.** Ren set out the long-term objectives: “I want to push the frontier as strong as possible, in terms of human knowledge, or have the full truth set(still need situational awareness), the universal ethics”; after the AI's answers, Ren replied “continue, let's pursue the strongest claims and complete proof, i think you see the right direction, also update project context” ([source](../../../../sources/15-codex-theory-conversations/2026-10-10-strongest-claims-direction.md)). P42 asks, with no axiom, how far a formation's own feedback reaches, how far a part's exchange reaches, and where the comparison with and without a part is decided. `Becoming.Feedback` (100 theorems) imports `Becoming.Interdependence`; the axiom appears only as a hypothesis of three witnesses.
- **Five levels of closure.** A region is closed under a relation when whatever a member bears the relation to is a member, and `WithinClosure` gives the least such region holding a formation, the Bridge's seed–edge closure from one seed (`withinClosure_iff_closure`). The feeding closure, the influence closure (what can affect a formation), the reach closure (what its exchange can affect, link by link) and the system (the closure under sharing a condition, a class) are each such a closure. The feeding closure lies within the influence closure, and the influence and reach closures lie within the system. Each inclusion can be strict, and influence and reach point in opposite directions (`Clearing.levels`, `Clearing.reach_middle`, `Trophic.mediates`).
- **One common condition makes the system the whole.** Where every formation takes part in one condition, every system is the whole (`Flow.system_whole_of_common`). Where every formation depends on it and exchanges with it, every reach closure is the whole. Where at one step every formation requires it and gives to it, every feeding closure is the whole, and route (b) is the axiom (`Flow.feeding_unrestricted_of_common`).
- **What feedback registers.** In a balanced flow a formation's support registers only its exchanges with what it depends on (`Flow.Balances.support_agrees`). So a part whose members all lie beyond a formation's influence closure is registered within it at no step (`Flow.Balances.unregistered_beyond_influence`). In `Clearing` the clearer's support is the same at every step whether or not it clears the habitat, while the dweller ends (`Clearing.unregistered`).
- **The comparison is decided within reach.** For any significance covering what a part has reached before each step, the comparison of the levels with and without the part is the axiom's comparison by inclusion (`Flow.Balances.comparison_within_reach`). Two significances that agree on that reach compare alike (`comparison_local`). Where significance is decidable, adding is exceeding (`adds_iff_exceeds_of_decidable`); in general this holds only under double negation. This advances P40: the covering condition of `Web.retains_bounded_iff_includes` now follows from the dynamics. The comparison of any two balanced flows that start alike is decided within what their difference reaches (`comparison_within_difference`), so where others respond, the difference holds their responses.
- **Where the comparison stops.** The comparison by withheld levels holds the rest of the exchange fixed. In the trophic cascade, with the deer's browsing held as it is, the wolves' part narrows and closes the deer (`Trophic.mediated_unregistered`); against the flow in which the deer respond, the same taking is mixed (`Trophic.responsive_mixed`). Where a part gives what others take, the levels without it may not exist (`Clearing.no_levels_without_source`). Reaching beyond a formation's influence closure does not by itself misjudge it (`Margin.reach_without_misjudgment`).

On the AI's reading, pending Ren, the system does not read Ren's middle level, “the system that one is in”: one common condition makes it the whole, and it has no center. The reach closure is offered in its place: it has a center, can be nested and points forward. P40's reading of the feeding closure as that level is withdrawn. “still need situational awareness” is read as follows: to compare its own part, a center must know what the part reaches beyond its feedback. Records added: levels-of-closure, feedback-and-reach and comparison-within-reach. Feeding-closure, consumption-ends-with-feeders, closure-verdict-meets-axiom and whole-first-and-bounded-centers are revised; their claims are unchanged. The author's counterreview is in section 61.

**P43: the axiom decomposed.** Ren wrote that there is “a set of universal invariations, that for every universe, becoming happens, the law follows”, “the bases of all ethics, for all beings, in all universes”, and that “There is no absolute self, and the continuation goes beyond one’s cycle of life, goes beyond one’s death” ([source](../../../../sources/15-codex-theory-conversations/2026-10-10-truth-exists-opening.md)). The AI read three claims from Ren's words that might give the axiom and proposed stating exactly the one step a critic must deny. `Becoming.Boundaries` (47 theorems) imports `Becoming.Feedback`. It decomposes the axiom and locates that step; it does not reduce the axiom. Along a relation, a boundary of a formation's self is a region holding it and closed under the relation. A claim about the self is super-true when it holds at every admissible boundary (Fine 1975), sub-true when it holds at some (Hyde 1997), and boundary-invariant when holding at one means holding at every one, that is, when it is determinate (`boundaryInvariant_iff_determinate`).
- **Two scopes.** The presupposition from a standpoint is that everything within the region has significance at every step. Sub-true along a relation, it is significance on the closure, and route (b) is the least significance making every presupposition sub-true (`bounded_closure_least`). Super-true, it is the axiom (`unrestricted_iff_superTrue`). So “however the boundary is drawn” gives route (b) in the narrow scope and the axiom in the wide one (`presupposition_scopes`).
- **Where the axiom's content lies.** Where the whole is admissible, the axiom is exactly the presupposition, sub-true and boundary-invariant at every standpoint (`unrestricted_iff_presupposed`). Invariance is exactly the conditional from the presupposition to the axiom at that standpoint (`boundaryInvariant_iff_conditional`). Given the presupposition everywhere and covering, invariance is the same as standpoint invariance, the rule N_std (`boundaryInvariant_iff_standpointInvariant`). So all of the axiom's content beyond the presupposition lies in the invariance step, as tolerance together with Chain carried all of G0's content beyond S0. The step runs both ways: where some continuation lacks significance, an invariant presupposition is nowhere sub-true (`not_subTrue_of_invariant`). Each premise is needed (`Clearing.without_presupposition`, `without_invariance`, `without_standpoint_invariance`, `with_fixed_boundary`).
- **Parts within reach.** A presupposition sub-true along affecting gives the axiom's comparison for every part within the reach closure, with neither invariance nor super-truth (`Flow.Balances.presupposed_reach_comparison`, a corollary of P42). It reads Ren's weaker version.

Covering holds by construction: along a relation, every closed region holding the center, the whole included, counts as an admissible drawing of the self, and that admissibility is a substantive choice. Using Ren's “belief” as a premise, and extending Ren's invariance across universes to significance, are the AI's steps. G0 remains the adopted axiom until Ren accepts a replacement, which waits on an audit of G0's uses (P44). Records added: presupposition-scopes and axiom-decomposition.

**The sixteenth independent review (§62.1).** (Called the fifteenth on the branch; the review of R1–R2 landed first under that number, so this one is renumbered the sixteenth, its content unchanged.) Before integration another agent (Claude Opus 5.5, an author of none of it) reviewed P42 and P43 ([review](BECOMING-P42-P43-REVIEW.md)). It recompiled the reviewed files byte for byte and audited every declaration of both modules and the extension; every axiom report is empty, and its 142 probe declarations are term proofs without classical reasoning. The Lean is accepted; the sixteen findings concern the module prose, the AI's readings and the framing, and all are handled. The largest are these:
- one common condition collapses the system to the whole, so the reach closure is added for Ren's middle level (F1);
- “the axiom derived from three premises” is a decomposition, not a reduction, and is withdrawn (F6);
- the comparison by withheld levels holds the rest of the exchange fixed, so effects through others' responses do not register in it (F2), answered by the trophic witnesses and by the comparison of any two flows;
- the three claims are the AI's reading of Ren's words, not claims Ren holds.

Names follow Ren's naming criteria: `Protection` becomes `Trophic`, “verdict” becomes “comparison” and “commons” becomes “common condition”. The first checker run failed on a name clash with the Bridge's `Closure` (receipt 20261010T173822.496446Z retained), so the core's closure became `WithinClosure`, and the Bridge now proves the two are one closure (`withinClosure_iff_closure`). Receipt 20261010T174514.186722Z (Feedback 100, Boundaries 47, Bridge 35); periphery receipt 20261010T175236.872210Z. The text after the handling has not been independently reviewed.

**Counting where premises bind in finite worlds and under enclosure (P46).** Following Ren's "let's aim for the strongest claim without axiom, as the first part" and "aim a complete theory of becoming, and finish related work", this states the two laws of counting P45 left open (section 60, objection 4), and the one between them, so that the laws of counting where premises bind are stated in unrestricted, finite and eventually enclosed worlds.
- **Enclosure, every premise binding.** With every step from some step on enclosed, where every premise binds the laws of counting under the eight are those under enclosure and that something arises (`World.enclosed_binding_counting`), the enclosed queue with its web saturated binding every premise, the census included (`World.enclosedQueue_saturated_binds`).
- **Finite worlds, each selection.** No finite world binds the census, so under a selection with it every property is a law there (`World.finite_binding_census`). Under each selection without it, where each selected premise binds, the laws are those of `World.finite_counting_under` and at most three more (`World.finite_binding_counting_under`): something is active and something arises, exactly where they are added in general (`World.finite_binding_activity_iff`, `World.finite_binding_arising_iff`); and something arises across a step at which something is active, exactly where embodiment is selected and the selection binds counting or bounds change, or selects bounded transmission with only active relata giving or with only active relata taking and dissipation (`World.finite_binding_joint_iff`). The two differences from P45 are what finiteness adds: every step is enclosed, so balance, embodiment and dissipation bind counting, and taking with dissipation gives only active relata giving (`World.Finite.acting`).
- **Finite witnesses.** A relay beside a ring, handing one of the two units one place stands at on to another whatever holds them (`World.relayRing_binding`); a lossy ring, whose front's place across one step exchanges a unit each way with itself and each place coming to be held and loses one unit more (`World.lossyRing_binding`); a balanced ring whose front's place exchanges one unit more each way with itself across the step after something joins (`World.exchangingRing_binding`); and the finite queue with its web saturated.
- **Enclosure from some step on, each selection.** Under each selection, where its premises bind, the laws are those of `World.enclosed_counting_under` and the three of P45 (`World.enclosed_binding_counting_under`), each under exactly the same selections as where nothing is enclosed (`World.enclosed_binding_activity_iff`, `World.enclosed_binding_arising_iff`, `World.enclosed_binding_joint_iff`): enclosure and binding add their laws each on its own, since what arises may arise before enclosure. The relay is enclosed at every step and the lossy queue after its gift (`World.relayQueue_enclosed`, `World.lossyQueue_enclosed`); without dissipation, a queue whose front exchanges one unit more with itself is enclosed throughout (`World.exchangingQueue_binding`); and with balance, embodiment and dissipation but neither only active relata giving nor taking, a queue closes at a step at which something is active, from which on nothing arises across a step at which nothing is active (`Tally.occupied_from`, found by a bounded search), its front standing one spare unit there and shedding it, so that dissipation binds at a closed step (`World.sheddingQueue_binding`).

On the AI's reading, pending Ren: binding still leaves only its instances in the counts; finite worlds and eventually enclosed ones differ at the step at which something arises, which in a finite world is itself enclosed. Records extended or revised: counting-under-enclosure, whole-law-of-counting. Receipt 20261011T001147.906623Z (Counting 212). Not yet independently reviewed; the author's counterreview is in section 63.

**P44: G0's uses under the axiom (§64).** Every occurrence of G0 in the core (9 files) and the periphery's generative-capacity modules (19 files) was audited. Each use is a hypothesis for an arbitrary positive relevance, a characterization, a countermodel or a mention in prose. Read from significance, positive relevance is realized living content whose continuation has significance from every standpoint. Under the axiom it satisfies G0 on every frame and is the least positive relevance that does, exactly the realized living content (`g0_of_unrestricted`, `relevance_least`), so every use is discharged; the Bridge states this for the periphery's interface and for its three imported theorems. The axiom is exactly G0 for anything, with “positive” weakened to “has significance” (`unrestricted_iff_g0`). One reading is forced: with bare significance the reason premise A gives a reason for any new content, living or not (`articulates_total`, `Widening.bare_forces_reason`). Read on living content, A gives D, and the universal reason follows from the axiom with no seed, neutrality or connection premise (`universal_reason_of_unrestricted`). Read on possibilities, what a course's levels admit, extension under C is, under the axiom, retaining and adding what has significance (`Ranking.possible_extends_iff`). It ranks the absence of an overdrawing formation, restraint and sharing as the whole-run reading does, and it withholds no event (`Ranking.malignant_possible`). It leaves a formation that adds no possibility unranked against its absence, where both readings of `living` rank its presence higher (`Ranking.possible_tie`). Possibilities first, then a reading, is a strict order satisfying C that ranks that presence higher, and it also ranks a rest below uninterrupted activity (`Ranking.Rest.rest_ranked_below`). The records one-axiom-yields-g0 and ranking-under-readings are extended. G0 remains the adopted axiom; the replacement, the reading of positive relevance and the comparison of courses are Ren's choices. Receipt 20261010T214440.263682Z (Relevance 30, Bridge 40); periphery receipt 20261010T222130.672025Z. P42 and P43 were first checked on their branch (receipts 20261010T174514.186722Z and 20261010T175236.872210Z); merged with R3 and R4, P42 to P44 landed together, and the receipt above covers the merged package. Not yet independently reviewed.

**P51: G0 folded (§67).** Ren answered the report after P42–P44 landed: “if we don't need G0 as axiom, fold it, at least for part i, and commit” ([source](../../../../sources/15-codex-theory-conversations/2026-10-11-fold-g0.md)). On the AI's reading, pending Ren, the condition holds: Part I needs no adopted G0, and in Part II G0 is a theorem of the one axiom, with positive relevance read from significance (section 64). So G0 is no longer an adopted axiom. Its definition and checked characterizations stay, and only its standing changes: it is a condition in Part I and a theorem in Part II. This answers the first of section 64's three choices; the reading of positive relevance, which the fold uses, and the comparison of courses remain Ren's. No Lean is new and no record is added.
- **Part I.** A new paragraph in chapter section 5 states G0 as a condition with no axiom: on a connected whole with a living claim it is a seed with both neutralities (`Valuation.significant_iff`); where every living claim is held it is S0 at every standpoint with standpoint neutrality (`Valuation.significant_iff_held`); on the level paths of every web the axiom is G0 for anything (`Web.unrestricted_iff_paths_g0`); and the dynamics do not decide it (`Web.significance_undetermined`). The Part I stated whole, item 10 of the full statement and the premise card say the same.
- **Part II.** G0 is a theorem of the axiom (`Valuation.premises_of_unrestricted`, `g0_of_unrestricted`), and the theorems of chapter sections 6.1–6.7 and 7 take G0 or its parts as hypotheses, which hold under the axiom; A, C, L and J1–J4 stay disclosed premises. Every “G0 remains the adopted axiom” in the chapter is replaced, and the open lists drop whether the axiom or the restatement replaces G0.
- **Records.** Seven records' text is corrected, with a history entry each and their theorems unchanged: axiom-decomposition, closure-verdict-meets-axiom, held-lives-g0-is-centering, metaethical-core-characterization, one-axiom-yields-g0, positive-ground-open-futures and presupposition-scopes. The scope of the Theory of Becoming and the directive register record the fold.

What the fold leaves: under another reading of positive relevance, G0 is a theorem only where that reading follows from significance. The single “iff” stating G0 as the axiom restricted to realized living content is not written in Lean and is not claimed. Ren's opening still says G0 remains the adopted axiom and changes only with Ren. Seven core modules' docstrings, which still said the same at landing, were folded in P47's core run (99e78ddd, receipt 20261011T003217.297180Z), where all seven passed the core check.

**Counting what stands and what depends (P47).** Following Ren's "let's aim for the strongest claim without axiom, as the first part" and "aim a complete theory of becoming, and finish related work", this states what the premises add to the two other listings of `Becoming.Population`, the census of what stands and the census of dependences, the item whole-law-of-counting and counting-under-enclosure left open, so that Part I's laws of counting are stated, with no axiom, in all three readings. New core module `Becoming.Standing` (importing `Becoming.Counting`).
- **What stands, unenclosed.** Where every relatum is embodied, what stands is what is active, and the counts of the two censuses obey the same properties (`World.Embodied.standsObey_iff`). Without embodiment a queue fed from a source, the driven queue whose driver is active throughout and stands at nothing while its members stand and never act, meets every other premise whatever its counts (`World.sourcedQueue_holds`). So under each selection the laws of counting what stands are those of activity (`World.standing_counting_under`, `World.standing_iff_counting`, `World.standing_binds_iff`).
- **Enclosure bounds what stands under balance and dissipation alone.** With every step from `T` on enclosed, the change from `T` of any census of what stands stays within the total standing at `T` (`World.enclosure_bounds_standing`), and nothing comes to stand across an enclosed step at which nothing stands (`World.enclosed_binds_standing`), with no premise on activity: what the flow takes and gives is standing, and embodiment is what carries the bound to what is active. So with enclosure from some step on the laws of counting what stands are those of `World.enclosed_counting_under` with embodiment dropped from the condition for a change bound (`World.enclosed_standing_counting_under`), a change bound being a law exactly where balance and dissipation are selected (`World.enclosed_standing_bound_iff`). Where balance is selected without embodiment the witnesses are waiting queues, closing queues whose next to join is active before it stands, so that the front is active at every step (`World.waitingQueue_holds`).
- **Finite worlds.** Every step is enclosed, so the laws of counting what stands are those of a tally with at most some number standing at each step, nothing coming to stand across a step at which nothing stands where the selection binds counting or selects balance and dissipation, and a change bound from the first step where it selects balance and dissipation (`World.finite_standing_counting_under`, `World.finite_standing_binds_iff`, `World.finite_standing_bound_iff`), with a ring each of whose places is active throughout as the new witness (`World.activeRing_holds`).
- **Dependence.** With requiring decided, the premises add nothing to the law of counting dependences, under each selection, with enclosure from some step on and, with at most some number holding at each step, in finite worlds (`World.dependence_counting`, `World.enclosed_dependence_counting`, `World.finite_dependence_counting`). A queue and a ring whose members depend while in it on a common condition standing at one and active throughout, each needing a unit of it and met, with nothing flowing, meet all eight premises whatever the counts (`World.still_premised`, `World.dependingQueue_premised`, `World.dependingRing_premised`). A first draft had the dependences at need nothing; the met dependence at need one removes that objection without changing the theorems.

On the AI's reading, pending Ren: what an enclosed unfolding spends is what stands, activity being bound with it only where embodied; the premises bear on dependence only where it meets activity, standing and descent. The laws where each selected premise binds, and joint laws of the three counts, are not stated for what stands and what depends; following Ren's redirect of 11 October the selection tables are not extended, and these laws are to be restated for every world with no premise ([zero-premise plan](ZERO-PREMISE-PLAN.md)). New record counting-standing-and-dependence; counting-under-enclosure and whole-law-of-counting revised. Receipt 20261011T003217.297180Z (Standing 38). Not yet independently reviewed; the author's counterreview is in section 65.

**What every law of change keeps, loses and returns to, with no premise (R6).** Asked what "0" meant, Ren wrote on 11 October 2026 that at the atomic level each exchange conserves energy and entropy still rises, with zero premises, and asked whether, if lossless exchange exists, a path can be found and proved along the way; then: ‘please keep advancing, zero-premise, zero axiom(we are not physics, we derive further)’ ([source](../../../../sources/15-codex-theory-conversations/2026-10-11-difference-in-becoming.md)). A new core module, `Becoming.Recurrence`, importing only `Becoming.Frame`, states what holds of every law of change on configurations of any kind, with no premise and no decidability; that a list holds the configurations is a condition written into each law that uses it. A list holding the first `l.length + 1` values of a sequence holds two equal ones (`revisits_within`, a pigeonhole by induction on the list that uses membership as given), so a sequence held by a list revisits from every step on, as does every run of every process (`Run.revisits_from`), and no list holds a sequence that never revisits (`unlisted_of_new`). A quantity of the configuration that never falls and rises across every change (`Marks`) stops change within finitely many configurations (`Marks.change_stops`). Under a determined law a possibility lost stays lost and configurations merged stay merged (`Law.lost_stays`, `Law.merged_stays`, and `Reach.lost_stays` for every process). Where a list holds every configuration, merging nothing, every configuration returning and every configuration reachable at every step are one (`Law.lossless_iff_returns`, `Law.returns_iff_keeps`); losing nothing, no quantity rises along an orbit, so an arrow needs a merge (`Law.Lossless.no_rise`, `Law.rise_not_lossless`), and a merge loses a possibility for good (`Law.Merges.loses`). Open worlds separate the three: counting on merges nothing, never returns and rises at every step, and counting down merges yet keeps every possibility (`Law.succ_open`, `Law.pred_open`). Keeping its history, every law merges nothing, never returns, cannot have its beginning again after the first step, and has no list holding it (`Law.withHistory_lossless`, `Law.withHistory_never_returns`, `Law.withHistory_loses_beginning`, `Law.withHistory_unlisted`); where the present returns it comes back with another history (`Law.return_keeps_history`), and within finitely many configurations two different histories share one present from every step on (`Law.present_forgets`). On the AI's reading: lossless exchange exists exactly as return within finitely many configurations, with no arrow, and as becoming that keeps its history, with an arrow and an open world; the low-entropy beginning that physics supplies is here the beginning of the kept history, which cannot be had again; entropy reads as the forgetting of a finite present. The mathematics (pigeonhole; an injection of a finite set into itself is a bijection, every point of which returns) is credited as reused. Record recurrence-without-premise added. Receipt 20261011T011019.444120Z, periphery receipt 20261011T011213.027508Z. Not yet independently reviewed; the author's counterreview is in section 68.

**The laws of one step, with their condition inside them (P48).** Following Ren's redirect of 11 October ("stop extending the premise-selection tables. New goal: remove premises and derive the most general versions, zero premises first"), and Ren's instruction of the same day to finish one unified theory together, this restates the four laws Ren named first for every world: rest and continued change needing openness, ceasing needing arising, closure bounding change, and arising needing an active giver. In each, the condition the proof uses is stated inside the law, as a fact about the world at the steps and relata where the proof uses it. The move made is localization. No premise is derived: within the representation the premises stay contingent and independent (`World.contingent`, `World.independent`). The new core module is `Becoming.Locality`, which imports `Becoming.Dissipation` and is imported by `Becoming.Roles`. The withdrawn joint law kept the number P48, and its three lemmas are recast here.
- **Balance at a step.** The flow balances on a family across one step (`Flow.BalancesOn`). Balance is the same as balance on every family across every step (`Flow.balances_iff_on`).
- **Arising needs an active giver.** Where a condition is balanced across a step, it comes to stand exactly when it stood at nothing and was given more than was taken from it (`Flow.BalancesOn.comesToStand_iff`). It ceases to stand exactly when it stood and what was taken from it is all it had with all it was given (`Flow.BalancesOn.ceasesToStand_iff`). Across a step at which nothing is taken from a balanced family, a member rises exactly when something taking part gives to it (`Flow.BalancesOn.rises_iff_gives`), and dissipation on the family excludes this (`Flow.DissipatesOn.still_untaken`). Take a relatum embodied at both ends of the step, and suppose only active formations give to it. It arises exactly when it comes to stand, and an active giver other than itself gives to it (`Flow.BalancesOn.arises_iff`, `Flow.BalancesOn.arises_given`). Nothing comes to stand from nothing across a step at which a family holding it is balanced and dissipated on (`Flow.BalancesOn.comes_from_standing`). The following are now its corollaries: `Web.Embodied.arises_given`, `World.taking_binds_counting`, `World.enclosed_binds_counting` and P47's `World.enclosed_binds_standing`. The three lemmas of the withdrawn joint law are the two iffs and `still_untaken`.
- **Rest.** Across a step the family runs down when three things hold: it holds, without repetition, whatever stands before or after the step; the flow balances on it; and the flow dissipates on it (`Flow.RunsDownOn`). Closure is not part of this condition.
  - Across such a step, some condition's standing changes exactly when the family's total falls (`Flow.RunsDownOn.changes_iff`). With the family also closed, something taking part takes or gives exactly then (`Flow.RunsDownOn.exchanges_iff`).
  - Continued change needs openness, exactly. Under a census of what stands, standing changes at arbitrarily late steps exactly when it changes at arbitrarily late steps across which what stands does not run down (`Flow.change_recurs_iff`); the exchange obeys the same law with closure (`Flow.exchange_recurs_iff`).
  - The general form is `recurs_iff_unmet`. An event recurs exactly where it recurs without a condition when three things hold: under the condition the event lowers an amount; the amount never rises under the condition; and every rise of the amount is the event. The search for the step is bounded, so no decision is used.
  - `Flow.stills`, `Flow.exchanges_finitely`, `standing_never_rises`, `change_lowers`, `exchange_lowers`, `standing_runs_down` and `fall_lowers_on` are now its corollaries, and with them the rest theorems of `Becoming.Openness`.
- **Running down bounds change.**
  - Over any stretch, with no condition, what stands at its end, with the steps at which the total standing fell, number at most the total standing at its start with everything it rose (`Flow.standing_bounds_change`).
  - The total rises only across steps at which what stands does not run down. So across steps that run down, what stands at the end with the steps at which some standing changed is within the total at the start, with no decision of whether a standing changed (`Flow.runsDown_bounds_change`).
  - For any counts, the change bound is `Flow.runsDown_change_bound`.
  - `World.enclosure_bounds_change` (P46) and `World.enclosure_bounds_standing` (P47) are its corollaries.
  - Ren named the law "closure bounds change". What bounds change is the running down, balance and dissipation on a family holding what stands. Closure is how the premises supply that.
- **Ceasing needs arising.** This part was drafted and verified by the session "0 axiom completeness" and integrated here.
  - A list covers what holds at a step when every member holding there is on it (`Covers`).
  - For any finite list, what holds of it at the end of a stretch, with its ceasings, is what held of it at the start exactly when none of it comes to be across the stretch (`cohort_closes_iff`).
  - Take a list holding exactly what holds at `N` (`ListsAt`), with nothing coming to be after `N`. Then what holds at the end with what ceased since `N` number exactly those holding at `N` (`ceasing_needs_arising`).
  - Ceasing recurring needs coming to be recurring wherever some list covers what holds at arbitrarily late steps (`coming_of_ceasing_covered`). The census law is the case of a census (`Listed.covered`). `World.arising_of_ceasing` and `Web.StandingCensus.coming_of_ceasing` are re-proved through it.
  - Without decidability, with a list covering `N` and nothing coming to be from `N` on, ceasing does not recur (`Covers.ceasing_steps_within`, `Covers.ceasing_not_recurring`, `Covers.not_not_coming_from`).

Commitments of the representation (Ren's item 4), from the statements and proofs:
- **Decidability.** Laws 1, 3 and 4 take no decision of any predicate of the world; their proofs decide only the order of numbers. Law 2's exact count needs marks, and its form that ceasing does not recur needs none.
- **Whole units.** The one-step iffs of laws 1 and 4 use addition and order only. The recurrence of law 1 and the bounds of law 3 use the least difference: dissipation's sign term, a unit lost by each formation taking (Ren's option A). Whether each law survives amounts finer than whole units has not yet been checked here. For rest, the resolution line covers it (R4: rest at every resolution with the refinement counted).
- **Time.** The test on coarser steps is the localized `Sampling` (queue item 7, from the session "0 axiom completeness"). Balance and dissipation on a family compose across the fine steps of a coarse step, with each relatum listed once, and a family running down needs to hold what stands only at the two coarse ends. Acting and taking stay relative to the step.
- **Finiteness.** The census of what stands, finitely many standing at each step, is used by the recurrence of law 1 and by law 3, and only to make the total standing a number at each step. The one-step laws need no census.

On the AI's reading, pending Ren: the laws of Part I that the premises bound are laws of each step and its relata, and the premises are one way of making their conditions hold everywhere. New record laws-of-one-step. Revised records: continued-change-needs-openness, counting-under-enclosure, whole-law-of-counting, counting-standing-and-dependence, ceasing-needs-arising and life-as-condition-of-life. Receipt 20261011T071749.484228Z (Locality 57). Not yet independently reviewed; the author's counterreview is in section 66.

**P52: the inventory of Part II (§69).** Ren had written “part i first, then consider second(maybe a lot in second will move to part i)” ([source](../../../../sources/15-codex-theory-conversations/2026-10-11-one-unified-theory-together.md)), and after the fold of G0 (P51) what Part II adds is one axiom. Of the 157 theorems Part II cites, 22 take the axiom as a hypothesis and 135 do not: 85 take no premise, 18 only Part I's premises, 12 an evaluative and 2 a structural condition, and 18 characterize the axiom without assuming it. Each of the 22 uses it only at named points, the significance from a standpoint of a formation at a step: one formation in a witness, the formations a compared path admits or where it exceeds, or the living realized claims. Each is a law for any significance specialized there. For comparisons the general local form is already P42's `Flow.Balances.comparison_within_reach`; for the derivations of G0 the local form is G0 itself (P51). So Part II adds one assertion to Part I, and A, C, L and J1–J4 stay disclosed conditions. The proposal, pending Ren, moves what does not use the axiom into Part I and keeps in Part II the assertion and its warrant; chapter section 8 lists it among Ren's choices. Of the 18 premise rows, 14 lie outside the zero-premise inventory; 11 are in Part II's modules and use balance only at earlier steps, through `Balances.withheld`. The inventory and its script are in [PART-II-INVENTORY](PART-II-INVENTORY.md). No Lean is new and no record is added; not yet independently reviewed.

The package now has 2171 theorems and 3257 declaration audits, over a core closure of 43 modules and a package of 41, all source declarations with empty axiom reports. Sections 40 to 42 were checked by the twelfth independent review, handled in section 45; sections 43, 44 and 46 by the thirteenth, handled in section 48; section 47 was checked by the continuation-grounding review, handled in §47.1–47.4; the handling in section 48 and sections 49, 50, 52, 54 and 55 by the fourteenth, handled in section 58; sections 59 to 59.2 by the fifteenth, handled in section 59.4; sections 61 and 62 by the sixteenth, before integration, handled in §62.1. The following have not yet been independently reviewed: the handling in §47.1–47.4, and sections 51, 53, 56, 57, 58, 59.3, 59.4 and 60, and the text of sections 61 and 62 after that handling, and sections 63 to 69. The periphery bridge passed against this core (receipt 20261011T071753.574921Z).
