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
| `Web.activity_over_stretch`、`Web.arising_recurs_iff`、`Web.unceasing_iff` | 读于活动（活动可判定）：有限家族的形成在终点活跃的连同其间止息的，恰是在起点活跃的连同其间生起的；它们在任意晚的步生起恰当在任意晚的步止息；形成有限多时，生成不息恰当某个形成在任意晚的步止息 |
| `Web.standing_recurs_iff` | 读于水平，不需要任何前提：有限家族的条件在任意晚的步开始作为条件而在，恰当它们在任意晚的步不再作为条件而在 |
| `Dawn.unceasing`、`never_ceases`、`rises`、`never_falls` | 无限家族：形成 f 跨第 f 步生起、从不止息，水平每步上升、从不下降。只生而不止需要无尽的新，上升复现而不下降需要无界 |
| `Dusk.ceasing`、`nothing_arises` | 无限家族：全部形成一开始活跃，形成 f 跨第 f 步止息，没有任何生起。只止而不生需要无尽的初始 |
| `le_dest`、`steps_mem`、`steps_last`、`steps_mono` | 一段步的引理 |

另外，`total_map` 与 `total_congr` 从 `Roles` 移到 `Flow` 的 total 一节，与其他 total 的引理放在一起，并新增 `total_ones`（每个成员计一次，总和是成员数）。`Roles` 与 `Reserve` 的定理数随之减少，内容不变。

**解读。**

- **不加前提的部分有实质内容。** 前四行是定义与恒等式：变化的读法、升降相抵。它们本身不多说什么，但把以前分散的定义（`Arises`、`Forms`、`Dissolves`、`ComesToStand`）收到同一种变化之下，并补上缺少的另一半（`Ceases`、`CeasesToStand`）。实质内容来自两个界：量不低于零，规定只计 0 或 1。由前者，下降复现需要上升复现；由后者，有限家族中开始成立与不再成立同步。这些对每个展开成立。
- **生起与止息在有限之中同步。** 有限家族中，生起复现恰当止息复现；任一段步上两者之差不超过成员数。所以在形成有限多的展开中，生成不息恰当止息不息：没有只生不灭的有限世界，也没有只灭不生的有限世界。作者把这读作 Ren 所说“生成、维持、转化、退化与消失在同一展开中”的一种形式内容（AI 论证）：生起与止息在有限之中一同复现。这是活动的读法，不是 Ren 的“生成的”“退化的”：Ren 说二者不重叠，读作关系，更新的形成与消耗的形成不重叠（`Web.renewing_not_consuming`）（P23c 更正，原文“生成与退化不是两个可以分开的过程，在有限之中它们一同复现”；见 §34 M1）。这不推出止息是好的或坏的，也不决定生生不息在哪个层次读：在谱系或整体的层次上不息，与成员的止息不息并不冲突（§21 的 `Generations`），这里的结论正是说成员层次上两者同步。
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
- **生起复现与止息复现在有限世界中是同一部分。** §26 证明，形成有限多时生成不息恰当止息不息。读于世界：活动可判定的有限世界中，生起复现的部分与止息复现的部分重合；对每个世界陈述而不给可判定性，这一规律就是排中律（`law_decides`）。它们只在无限世界中分离，并且分离的两个世界无限这一点由规律本身推出，不需另证。这是活动的读法；读作关系，更新的形成与消耗的形成不重叠（`Web.renewing_not_consuming`），与 Ren 所说二者不重叠相合；提议中的“生成的”“退化的”指哪个部分，由 Ren 选择（P23c 更正，原标题“生成与退化在有限世界中是同一部分”，原文“有限世界中生成的部分与退化的部分重合”“‘生成的’与‘退化的’不是整体的两半，在有限的展开中它们是同一个部分”；见 §34 M1、M2）。
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
| `mutualism_premised`、`premised_rests` | 始终活跃的互利者满足全部八个；有限且活动可判定的世界中，八个一起使生起与止息都不再复现（P23c 用语，原文“生成与退化”） |

**解读。**

- **前提之间的结构。** 十个世界层面的前提里，有两个是另一个的较弱形式：有储备承载弱于活动需要支持（零储备），生起者体现弱于每个关系项体现。一个在有限世界中自动成立：普查。一个由另两个在被围住的步上推出：只有活跃者取用与耗散推出只有活跃者给予，因为耗散之下给予需要取用。这一条是新的：P13 的“给予需要取用”在世界层面读作，只有活跃者取用时，不活跃的关系项在有限世界中不能给予。
- **其余八个彼此独立。** 对每个前提，都有一个世界满足其余七个而不满足它。所以没有一个前提藏在其余之中：每个都是对世界的独立限定。不满足普查的世界（multitude）与不满足只有活跃者给予的世界（scatter）都是无限的；这不是选择见证的巧合，而是蕴含要求的：有限世界有普查，并且在其中只有活跃者取用与耗散推出只有活跃者给予。scatter 中没有一步被围住：每步的交换都伸到无限多个关系项，耗散空成立，P16b 已经披露这种情形（`Spray`）。
- **novel：依存在世系中新形成。** 亲代烧掉燃料的两个单位，给子代一个单位，使子代开始作为条件而在；子代开始依存于亲代，而亲代自己从未有这一依存。所以有界传递不成立：世系中出现了新的依存，而不是传下来的。这是 §29 中“传递是前提”的见证：novel 满足其余七个前提，有界传递却不成立，所以传递不由它们推出。
- **全部一起。** 互利者满足全部八个，所以前提一起是相容的，并且不空：有活动，有依存，有体现。在有限世界中，八个一起使世界归于静止（§30 的 `rests`，生起者体现由体现推出）。所以一个有限的世界若满足全部前提并使生起复现，是不可能的；生起复现需要越出某个前提，或者越出有限（P23c 用语，原文“继续生成”）。

**作者反审。**

*反驳 1：独立性见证太小、太人工。* 是小的。独立性只需要每个前提各有一个反模型；见证越小，越清楚地显示是哪个前提失败。它们不是对实际展开的描述，名称也由 Ren 定。

*反驳 2：“八个前提”的选择是任意的。* 部分是。这八个是脊柱定理在世界层面用到的动力学前提；相对于另一读法的前提（延续关系、更新关系、衰减的储备、条件家族）不是世界本身的限定，需要另一种地图；流中每个参与者只列一次是表示的条件。加入新前提时，独立性要重新检查，可能出现新的蕴含。

*反驳 3：premised_rests 只是 rests 的重述。* 是推论，不是独立结果；它显示的是：满足全部前提的有限世界没有生起复现的余地（P23c 用语，原文“继续生成”）。新的内容是蕴含、两个新前提与独立性。

**边界。** 无伦理谓词，不评价任何部分；只对离散步的读法陈述；有限世界的蕴含要求活动可判定；只映射世界层面的八个前提；前提与世界的名称是 AI 的表述，由 Ren 定。本节尚未经独立审查（计划 P24b）。

## 33. 开放（P25）

2026-10-09。按 Ren“aim a complete theory of becoming, and finish related work”继续，作为计划 P25。§30 的 `rests` 用有限使世界归于静止；§31（P23）陈述的理论在其第 8 节把这一点列为开放：在普查与被围住之下（而不只是有限时），全部前提是否使世界归于静止。本节回答：起作用的是被围住，不是有限。新 L3 模块 `Becoming.Openness`（导入 `Premises`）。成果记录：[continued-change-needs-openness](../../../../theories/becoming/results/records/continued-change-needs-openness.md)。

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
       关系项体现；rests_enclosed 与 arising_opens 要求关系项的相等可判定
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
| `arising_opens` | 所以这样的世界生起复现时，在任意晚的步有不被围住的步（P23c 改名，原名 `generation_opens`，原文“生成不息”） |
| `exposed`、`exposed_world` | Handing 的两侧另外在每步从无限多个地关系项各取一个单位再还回：满足全部八个前提，生起复现，没有一步被围住 |

**解读。**

- **总水平是只降不升的量。** 平衡与耗散一起，使跨过被围住的步的总水平不上升；更强地，任何水平的变化都使它严格下降。上升被给予，而在被围住的步上给予需要取用；下降被取用。所以变化本身消耗总水平。自然数的量只能严格下降有限多次（`falls_finitely`），所以被围住的展开中，变化只能有限多次。
- **有限不是关键。** §30 的 `rests` 要求关系项总共有限；这里关系项可以无限多，只要每步立着的有限多个被列出，且每步的交换被某个有限家族围住。两者都不是对方的特例：`rests` 要求有限而只要求生起者体现；这里不要求有限而要求每个关系项体现。
- **开放是生起复现的必要条件。** 读作对立面：满足普查、体现、平衡与耗散的世界若生起复现（P23c 用语，原标题与原文“生成不息”），那么在任意晚的步，有一步的交换伸到每个有限家族之外。这是 §17、§20（P13、P15）中家族层面的开放在世界层面的陈述，而且用变化的所立者，不是固定的家族。
- **exposed：开放不能去掉。** Handing 的两侧来回传递一个单位的水平，生起复现；另外在每步与无限多个地关系项交换一个单位，取用再还回，使地的水平保持为零。由于每步取用无限多个关系项，没有有限家族跨过任何一步封闭，所以耗散空成立。它满足全部八个前提（普查只列出立着的那一侧），生起复现。所以在八个前提之下，被围住这一条件不能从 `rests_enclosed` 中去掉。

**作者反审。**

*反驳 1：exposed 只是利用耗散的表示漏洞。* 是利用了一个已披露的特点：耗散只约束被围住的交换（P16b、`Spray`）。这正是要显示的：被围住不是由八个前提推出的，它是一个独立的、关于开放的条件。地的交换（取一再还一）是零净流，它不给两侧任何东西；它只使每一步不被围住。一个要求“每步只与有限多个关系项交换”的更强耗散会排除它，但那是另一个前提，应当公开地加入，而不是藏在耗散里。

*反驳 2：要求每个关系项体现太强。* 是比 `rests` 的“生起者体现”强。止息读作下降，需要止息者体现；生起读作上升，需要生起者体现。只要求生起者体现时，`stills` 仍使生起停止吗？不立着却活跃的关系项可以不断止息而不改变水平；所以止息复现的部分需要更多。是否可以只用生起者体现得到生起复现的部分，列为下一步（记录的 next_delta）（P23c 用语，原文“生成停止”“退化部分”“生成部分”）。

*反驳 3：可判定的相等是额外前提。* 是构造性证明的要求：把立着的两个列表合并为一个不重复的家族要判定相等。经典地它总是成立；`rests_around` 不要求它，直接以围住所立者为前提。

**边界。** 无伦理谓词，不评价开放或静止；只对离散步与自然数的量陈述；“开放”“被围住”“所立者”的读法与名称是 AI 的表述，由 Ren 定。本节尚未经独立审查（计划 P24b）。

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

*反驳 3：grazing 也依赖读法。* 它依赖逐步读法中“侵蚀”的定义：活跃者的汲取使另一个关系项已满足的依存在该步之后落空。这是 `Living` 的定义本身，不是附加的选择。它不依赖终结之步自我汲取的判定：不活的事件汲取的是池，池不是汲取者，也从不活跃。它仍然依赖两类读法的同一对应，这是表示的前提，已公开。

*反驳 4：既然 `selected` 不是选择项，`price` 还有什么用。* `price` 是会计恒等式，审查与本研究都这样说；它的用处在于加权总量受条件的水平所限（`selected_le`、`selection_within`），这把支持对给予的约束写进后代的总量。真正的选择项需要整数或有理数的量与均值，列为进一步的证明。

**边界。** 不含伦理谓词；不改变任何读法选择的地位，新增的一项（提议中“生成的”“退化的”的读法）列为 Ren 的选择；新名称是建议；探针与新见证都是最小见证；可判定性是公开的逻辑承诺。本节的更正尚未再经独立审查（计划 P24b）。

## 35. 止息需要生起与静止定理（P26）

2026-10-09。按 Ren“aim a complete theory of becoming, and finish related work”继续，作为计划 P26。§30 的 `rests` 要求世界有限，§33 的 `rests_around` 不要求有限而要求每个关系项体现；记录 continued-change-needs-openness 的 next_delta 列出：只要求生起者体现时，被围住的世界是否也归于静止。本节的回答是肯定的，靠的是一条计数的定律：在活动的普查之下，止息复现需要生起复现（普查定律）。于是归于静止只需生起停止，而生起者体现时，`stills` 使生起停止。由此得到一个静止定理，§30 的有限情形与 §33 的每个关系项都体现的情形都是它的推论。没有新模块：普查定律放在活跃形成的普查所在的 `Becoming.Population`，静止定理及其情形放在 `Becoming.Openness`。成果记录：新增 [ceasing-needs-arising](../../../../theories/becoming/results/records/ceasing-needs-arising.md)；修订 [continued-change-needs-openness](../../../../theories/becoming/results/records/continued-change-needs-openness.md)。

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
       “生起复现”“止息复现”是活动的读法，不是 Ren 的“生成的”“退化的”（§34，M1）
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
- **它仍是活动的读法。** 生起复现与止息复现不是 Ren 的“生成的”“退化的”（§34，M1）；静止不是评价，开放也不是。

**作者反审。**

*反驳 1：普查定律只是平凡的计数。* 证明确实只用不重复列表的长度比较（`length_le_of_sub`）与自然数不能无穷下降。它的内容在于划分：§30 的同一部分在普查之下只剩一个方向，另一个方向需要更多，两半分别由 dawn 与 dusk 见证。它也解释了静止的世界中止息为什么停止，而不要求止息者体现：这正是 §33 反驳 2 留下的问题。

*反驳 2：静止定理是否只是把前提重排？* 它使两个已有定理成为同一定理的推论，并把 `rests_around` 的“每个关系项都体现”换成“生起者体现”加上所立者的普查。它覆盖的新情形是：关系项无限多、有活跃而不体现的关系项、只有生起者体现的世界。一个只被静止定理覆盖而不被 `rests` 与 `rests_around` 覆盖的见证容易构造（无限多个空闲的关系项旁有一个活跃而不立着的关系项），但本节没有在 Lean 中给出它，所以“严格更一般”只是陈述层面的比较，不是已检查的定理。

*反驳 3：可判定性是额外前提。* 普查定律在世界层面要求活动可判定，因为构造性的证明在下一步活跃者的表中查找此前不活跃者（`search`）。这是表示的逻辑承诺（§34，M2）。每个关系项都体现时，活动由水平判定，所以 `rests_around` 不另加它。

*反驳 4：耗散在这里只约束被围住的交换。* 是（P16b、`Spray`、§33 的 exposed）。静止定理以围住为前提，没有把开放藏进耗散；exposed 仍表明，八个前提之下去掉围住，生起可以不息。

**边界。** 无伦理谓词，不评价静止、开放或止息；只对离散步与自然数的量陈述；“普查”“静止定理”“归于静止”的名称与读法是 AI 的表述，由 Ren 定。没有所立者的普查时被围住的步（kindling 一类的世界）仍列为下一步。本节尚未经独立审查：第十次独立审查的对象截至 P23c。

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
Boundary: 界须对所有步统一；不给比率；不评价生起或止息；“生起复现”“止息复现”是活动的读法，不是 Ren 的“生成的”“退化的”
Integration: 计划 P27；回答 §35 留下的一半与 ceasing-needs-arising 的下一步；有限世界的规律成为有界普查定律的情形
```

| 声明 | 内容 |
|---|---|
| `Listed` | 一个规定每步的成立者被不重复地列出：每步有限多个成立，成员总共可以无限多 |
| `Listed.comes_or_held`、`comes_or_fewer`、`comes_within`、`coming_of_ceasing` | 普查定律的一般形式：不再成立复现需要开始成立复现（P26 的活动版本推广而来） |
| `Listed.ceases_or_kept`、`ceases_or_more` | 从 N 到 T 之间，或者有成员不再成立，或者 N 时成立的在 T 时都成立；一次开始成立若此前没有不再成立，使列表比 N 时长 |
| `Listed.ceases_within`、`ceasing_of_coming` | 列表都不长于 B 时，开始成立复现需要不再成立复现：列表不能长过 B |
| `Listed.coming_iff_ceasing` | 列表有界时两者同步 |
| `Web.Census`、`Web.ceasing_of_arising`、`Web.unceasing_iff_bounded` | 普查是活动的列出；有界普查之下，生成不息恰当止息复现 |
| `Web.StandingCensus`、`StandingCensus.coming_of_ceasing`、`coming_iff_ceasing` | 所立者的普查是水平的列出；不再作为条件而在复现需要开始作为条件而在复现，有界时两者同步 |
| `World.CountedWithin`、`CountedWithin.arising_iff_ceasing` | 每步至多 B 个关系项活跃且被列出的世界中，生起复现恰当止息复现 |
| `World.Finite.countedWithin`、`Finite.arising_iff_ceasing` | 有限世界的每个普查都不长于关系项的数目；所以 §30 的 `arising_iff_ceasing` 是有界规律的情形 |
| `World.dawn_unbounded` | dawn 有普查而没有界 |
| `Procession.web`、`Procession.census`、`World.procession`、`procession_world` | 关系项 x 只在第 x 步活跃：每步一个，生起与止息都复现，关系项不是有限多个 |

**解读。**

- **一个计数定律，两个方向。** 列表每步记下成立者。一次不再成立，若此前（从 N 起）没有开始成立，就使列表比 N 时短；一次开始成立，若此前没有不再成立，就使列表比 N 时长。列表的长度是自然数：不能无穷地变短，所以不再成立复现迫使开始成立复现；有界时也不能无穷地变长，所以开始成立复现迫使不再成立复现。两个方向用同一个论证，只差界的有无。
- **三层。** 按每步成立者的计数，开始成立与不再成立的关系分为三层：有限且有界时两者同步（`coming_iff_ceasing`）；有限而无界时，不再成立需要开始成立，反之不然（dawn）；不再有限时，不再成立可以独自不息（dusk 没有普查）。§26 的有限家族定律与 §30 的有限世界定律都在第一层：有限家族或有限世界的每个列表都不长于成员数。procession 表明第一层不止于有限：关系项无穷多，每步只有一个在场。
- **一种变化，几种读法。** §26 说生起与止息、形成与消解、开始与不再作为条件而在是同一种变化读于活动、依存与水平。普查定律也是这样：它对每步其成立者被列出的任何规定成立，普查与所立者的普查是它读于活动与水平。读于依存（每步的依存被列出时）是直接的实例，留作下一步。
- **仍是活动与水平的读法。** 生起复现与止息复现不是 Ren 的“生成的”“退化的”（§34，M1）；有界不是评价，procession 中的接替也不是。

**作者反审。**

*反驳 1：推广只是改名。* 推广去掉了活动这一具体规定：同一证明对任何规定成立，所以水平的读法不需要另证；P26 的三个辅助定理被替换而不是并存，`Web.arising_of_ceasing` 的陈述不变。被替换的名称记在 ceasing-needs-arising 的历史中。把 `Web.Census` 与 `Web.StandingCensus` 定义为 `Listed` 的两个读法，是定义上的相等，原有的证明不改。

*反驳 2：有界普查是不是另一种有限？* 不是：procession 的关系项无穷多，它不是有限世界（`procession_world`），而有界规律适用于它。有界只约束同时在场的数目，不约束总数。反过来，有限推出有界（`Finite.countedWithin`）。

*反驳 3：界须对所有步统一。* 是。只从某步起有界的情形可以把展开平移到那一步得到，但没有陈述；界随步增长而不超过某个慢速增长的函数时会怎样，也没有研究。这些列为下一步。

*反驳 4：procession 是不是太平凡？* 它是最小的见证：每步一个关系项在场，下一步换成下一个。它的作用只是表明有界规律越出有限世界；它不满足体现（水平都为零），所以不说明静止定理的情形。

**边界。** 无伦理谓词，不评价生起、止息或接替；只对离散步与有限列表陈述；“列出”“有界普查”“procession”的名称与读法是 AI 的表述，由 Ren 定。本节尚未经独立审查：第十次独立审查的对象截至 P23c。

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
  - Read of activity: formations of a finite family arise at arbitrarily late steps exactly when they cease at arbitrarily late steps. With finitely many formations, generation is unceasing exactly when ceasing is (`Web.unceasing_iff`).
  - Read of standing, with no premise at all: coming to stand recurs in a finite family exactly when ceasing to stand does (`Web.standing_recurs_iff`).
- **Infinity is the escape.** Ever new formations can arise with none ceasing (`Dawn`), and endlessly many formations active at the start can cease with nothing arising (`Dusk`).
- **Author's reading.** In any finite family, arising and ceasing recur together. The author reads this as one formal content of Ren's scope, formation through dissolution within one unfolding (an AI argument). This is a reading of activity, not Ren's generative and degenerative: Ren said the two do not overlap, and read as relations, renewing and consuming formations do not (`Web.renewing_not_consuming`) (P23c correction; originally "generation and degeneration recur together"; see section 34, M1). It does not make ceasing good or a cost of generation. The level at which 生生不息 is read, and the names, remain Ren's.
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
- **Arising recurring and ceasing recurring are one part in finite worlds.** In a finite world whose activity is decided, arising recurs exactly when ceasing does (`arising_iff_ceasing`, section 26's `unceasing_iff` read of worlds). This is a reading of activity; which parts Ren's "generative, degenerative" name is Ren's to choose, and Ren said the two do not overlap (P23c correction; originally "Generation and degeneration are one part", with `generative_iff`; see section 34, M1). With infinitely many relata either recurs without the other (`separate`, from `Dawn` and `Dusk`), and that those worlds are infinite follows from the law.
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
- **What follows from what.** Activity needing support makes activity carried, by the zero reserve (`Dependent.carried`). Every relatum embodied makes whatever arises embodied. A finite world whose activity is decided has a census (`Finite.counted`). Where only active relata take and the flow dissipates, only active relata give across every enclosed step, since giving needs uptake there; every step of a finite world is enclosed (`acting_of_enclosed`, `Finite.acting`).
- **The remaining eight are independent.** For each of activity needing support, balance, only active relata giving, only active relata taking what they draw on, dissipation, embodiment, a census and bounded transmission, a world meets the other seven and not it (`independent`), so none follows from the others (`none_follows`). The worlds failing a census (`multitude`) and failing only active relata giving (`scatter`) are infinite, as the implications require. In `novel` a child comes to depend on the parent that gave it its standing, a dependence the parent never had, so transmission fails.
- **All together.** Mutualists active throughout meet all eight (`mutualism_premised`), and in a finite world whose activity is decided the eight together bring the world to rest (`premised_rests`, a corollary of `rests`).
- **Boundaries.** Only the eight premises stated of worlds are mapped; premises relative to a continuation relation, a renewal relation, a decaying reserve or a family of conditions are not. Independence is relative to these eight. No part is evaluated, and the names are Ren's to choose.

The package now has 974 theorems and 1583 declaration audits, over a core closure of 28 modules and a package of 26, all source declarations with empty axiom reports. Section 32 has not yet been independently reviewed.

**P25: openness.** Section 30's `rests` brings a world to rest through finiteness; section 31 listed as open whether all premises bring a world to rest under a census and enclosure instead. Section 33 answers: enclosure, not finiteness, does the work. It is a new L3 module `Becoming.Openness` (importing `Premises`) ([continued-change-needs-openness](../../../../theories/becoming/results/records/continued-change-needs-openness.md)).

- **Total standing runs down.** Where what stands at each step is listed, each once (`Web.StandingCensus`), the total standing across a step enclosed around what stands (`Flow.AroundStanding`) falls by at least the number of formations taking from the enclosing family (`standing_runs_down`), so it never rises, and any condition's standing rising or falling lowers it (`change_lowers`): a rise is given to, and giving needs uptake there; a fall is taken from (`fall_lowers_on`).
- **Rest from enclosure.** So where every step from some step on is enclosed around what stands, no standing changes at arbitrarily late steps (`stills`). A world with a census whose relata are all embodied, with a balanced, dissipative flow, enclosed from some step on, comes to rest (`rests_around`, `rests_enclosed`); finiteness is not needed.
- **Recurring arising opens.** Read the other way, arising that recurs in such a world needs a step not enclosed at arbitrarily late steps (`World.arising_opens`, named `generation_opens` before P23c): exchange beyond every finite family.
- **Openness cannot be dropped.** In `exposed` the sides of `Handing` also take a unit from each of infinitely many ground relata and give it back at every step. It meets all eight premises and arising recurs in it; no step is enclosed, so dissipation binds at none (`exposed_world`).
- **Boundaries.** The world-level theorems need every relatum embodied, not only whatever arises; decidable equality is required by the constructive proof; dissipation binding only enclosed exchange is a disclosed feature of its representation. Neither openness nor rest is evaluated, and the names are Ren's to choose.

The package now has 994 theorems and 1612 declaration audits, over a core closure of 29 modules and a package of 27, all source declarations with empty axiom reports. Section 33 has not yet been independently reviewed.

**P23c: the ninth independent review.** A separate agent (Claude Opus 5.5) reviewed P18b, P19, P20, P21, P22 and P23 ([review](BECOMING-P18B-P23-REVIEW.md)). It recompiled the 27 modules of the core closure from the prelude, with empty axiom reports for all 1571 source declarations; of the closure's 4423 constants only 30 compiler-generated `injEq` lemmas depend on an axiom, `propext`, as the receipt lists. It accepted all the mathematics and closed L1–L10 of the eighth review. It raised ten findings (M1–M10): one reading chosen for Ren, four omitted premises, one error in prose, two missing counterexamples, and two of presentation and bookkeeping. P24 and P25, committed during the review, were not read by it; their wording affected by M1 is corrected too. The corrections are made in place and marked; section 34 records the handling.

- **Generative and degenerative (M1, the most serious).** P22 read the "generative, degenerative" of Ren's proposal as some relatum arising or ceasing at arbitrarily late steps, and the canonical texts then stated that in a finite world the two are one part and overlap. On 9 October Ren said that they do not overlap. The parts of the space are now named for what they are: arising recurring and ceasing recurring (`World.ArisingRecurs`, `World.CeasingRecurs`, `World.arising_iff_ceasing`; `World.arising_opens` in `Openness`). Ren's words stand beside the two readings the spine offers: as activity, arising and ceasing recurring coincide in finite worlds; as relations, renewing and consuming formations do not overlap (`Web.renewing_not_consuming`). Which parts the proposal's words name is listed first among Ren's choices.
- **Decidability (M2).** The finite-world law needs activity decided; over every world without it, the law is excluded middle (`World.law_decides`, from the review's probe). Decidability now appears in every list of the representation's commitments, and as a logical commitment beside the method, model, correspondence and normative premises.
- **What `price` divides (M3).** The identity divides the offspring's total into the parents' amounts weighted by their offspring and the change in transmission. The weighted total is not the selection term proper: it is k times the parents' total where every parent has k offspring (`selected_uniform`), and five where nothing is selected (`unselected`). The covariance form remains a further proof.
- **Premises restored (M4–M6).** Embodied arising in a finite family under balance and dissipation leaves the family open and, enclosed around, it draws in; a rise comes with another member's fall across a step at which the family is dissipated on; depletion follows for an event at whose steps the family is dissipated on and taken from; a transmitted need exceeds the giving step's level by at most the bound of transmission, and may never have been met where the bound is positive (`Slack`).
- **Witnesses (M7, M8).** `grazing` gives a finite world in which arising recurs and some event is not living without resting on the verdict about self-drawing at an ending: a grazer takes from a pool another relatum depends on (`grazing_world`, `grazing_not_self`). `leaking` replaces the balance witness of `rests_needs` with a world whose dissipation binds: the holder takes its own unit at every step and gives nothing (`leaking_world`).
- **Presentation (M9, M10).** The laws are tagged as identity by definition, arithmetic identity, or consequence of two-valuedness and finiteness. Wisdom moves to empirical correspondence. Section 31 and the plan state which completeness criteria are met: criteria 1 and 4; criterion 2 after this correction; criterion 3 for the ten premises stated of worlds, while premises relative to other relations and the "mixed" part are not mapped. Review stamps are at or before their commits, the foundation record uses the chapter's terms, and the last "giver" is gone.

The package now has 1016 theorems and 1662 declaration audits, over a core closure of 29 modules and a package of 27, all source declarations with empty axiom reports. Section 34 has not yet been independently reviewed.

**P26: ceasing needs arising, and the rest theorem.** Section 30's `rests` needs a finite world and section 33's `rests_around` needs every relatum embodied; the record continued-change-needs-openness left open whether an enclosed world comes to rest when only what arises is embodied. It does, by a counting law. Under a census of what is active, recurring ceasing needs recurring arising (`Web.arising_of_ceasing` in `Becoming.Population`; `World.arising_of_ceasing` in `Becoming.Openness`): a ceasing not preceded by an arising leaves fewer formations active, and the count cannot fall forever. Not conversely: `dawn` has a census and keeps arising while nothing ceases, and `dusk` keeps ceasing while nothing arises, so it has no census (`World.census_one_way`). The finite-world law of section 30 thus splits in two: ceasing to arising needs only a census, arising to ceasing needs more. The rest theorem follows (`World.comes_to_rest`): a balanced, dissipative world with censuses of what is active and of what stands, whose activity is decided and whose arising is embodied, comes to rest once every step from some step on is enclosed around what stands, since standing stops changing, so embodied arising stops, and ceasing stops with it by the census law. Finite worlds (`World.Finite.comes_to_rest`, the statement of `World.rests`) and worlds whose relata are all embodied (`World.rests_around`, now proved from the theorem) are its two cases. The census of what is active is needed: `dusk` meets every other premise, with nothing standing and every step enclosed, and keeps ceasing (`World.rest_needs_census`). That the theorem is strictly more general than its two cases is a comparison of statements; no witness covered by it alone is formalized. Enclosed steps without a census of what stands remain open.

The package now has 1029 theorems and 1676 declaration audits, over a core closure of 29 modules and a package of 27, all source declarations with empty axiom reports. Section 35 has not yet been independently reviewed.

**P27: the census law in general, and the bounded census.** Section 35's census law goes one way: under a census, ceasing recurring needs arising recurring, and dawn shows the converse fails. Section 30's law of finite worlds, that arising recurs exactly when ceasing does, thus splits in two, and section 35 left open what the other half needs. It needs exactly a bound on the count. Where the members of which a determination holds are listed at each step, each once (`Listed`, in `Becoming.Population`), a ceasing to be not preceded by a coming to be shortens the list and a coming to be not preceded by a ceasing to be lengthens it; the list cannot shorten forever, so ceasing recurring needs coming recurring (`Listed.coming_of_ceasing`, generalizing P26's helpers), and where no list is longer than B it cannot lengthen forever either, so the two recur together (`Listed.ceasing_of_coming`, `Listed.coming_iff_ceasing`). A census is this listing read of activity (`Web.Census`; `Web.unceasing_iff_bounded`), and the census of what stands is the listing of standing (`Web.StandingCensus`; `Web.StandingCensus.coming_of_ceasing`, `coming_iff_ceasing`), answering the next step of ceasing-needs-arising. Read of worlds (`Becoming.Openness`): where at most B relata are active at each step, listed (`World.CountedWithin`), arising recurs exactly when ceasing does; every census of a finite world is bounded (`World.Finite.countedWithin`), so the finite law is a case (`World.Finite.arising_iff_ceasing`); `procession`, with relatum x active at step x alone, is bounded and not finite and keeps arising and ceasing (`World.procession_world`); `dawn` has no bound (`World.dawn_unbounded`). By counting, arising and ceasing fall into three tiers: finite and bounded at each step, they recur together; finite but unbounded, ceasing needs arising and not conversely; no longer finite, ceasing can recur alone. The bound must hold at every step; the case bounded only from some step on, rates and the reading of dependence remain open. New record bounded-census-keeps-pace; ceasing-needs-arising revised.

The package now has 1045 theorems and 1697 declaration audits, over a core closure of 29 modules and a package of 27, all source declarations with empty axiom reports. Sections 35 and 36 have not yet been independently reviewed.
