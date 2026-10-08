# 运行上的更新／消耗与生生的关系读法 / Renewal on runs and the relational reading

2026-10-09，Asia/Bangkok。AI（Claude）按 Ren 的指示“你自己全改了吧……先更新好计划，然后再一步步完整完成，保持代码和整体结构优雅”（[原话与解释](../../../../sources/15-codex-theory-conversations/2026-10-09-one-theory-unification.md)）完成[统一计划](BECOMING-UNIFICATION-PLAN.md)的 P3b。成果记录：[becoming-renewal-reading](../../../../theories/becoming/results/records/becoming-renewal-reading.md)。

## 1. 问题

Universal Metaethical Core 的前提卡里有三项对应：形成 E、连通、`living` 的读法。在 P2 中，`living` 和 `related` 是 `Valuation` 的外给参数，连通是假设。P3b 要回答的是：Becoming 层能否从展开本身给出这两项，从而让连通成为可以检查的动力学性质，而不是一条前提？

这里的“形成”和“条件”是同一展开中的分析角色：一个形成依存于某些条件，或从某些条件中汲取，或两者兼有。它们不是彼此独立的实体，也不是价值的所有者。

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
| `living_iff_relational` | 这一 `living` 就是已记录的[关系读法](../../../../theories/becoming/results/records/relational-reading-comparison.md) |
| `connected_of_common`、`significant_iff_of_common` | 如果每个活的形成都参与同一个条件，整体就是连通的；于是 G0 恰等于种子加 N_rel 加 N_std，连通由展开给出，不再假设 |
| `consumption_relates` | 消耗本身就是一种已形成的关系：消耗者与失去支持的形成共享被汲取的条件 |
| `valuing_consumption_reaches` | 在 N_rel 下，一个立场若珍视某个消耗者的活动，就必须珍视被它消耗的形成的每个活的事件 |
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

*回应。* 同意。数学上的新内容在第 2 节的后半：分类属于运行，消耗本身是一种关系，连通可由共同条件给出。统一的价值是让三条界落在同一个对象（运行）上，此后陈述不必再各建一个序列模型。

**反驳 2：`related` 太粗。** 任何两个从同一生物圈汲取的形成都“相关”，于是连通几乎自动成立，伦理内容全落到 N_rel 上。

*回应。* 粗细是读法的选择。这里如实公开，并没有证明它。

- `valuing_consumption_reaches` 用到的关系，只是“一方汲取、另一方依存于同一条件”，比共同参与更窄，在更细的读法下同样成立。
- 共同条件确实让连通变得容易，但这正是要公开的位置：拒绝 G0 的一方，现在必须拒绝 N_rel 或 N_std，即在边界内适用传递或共享，而不能声称两者无关。
- 生物圈、气候之类的条件是否真被所有活的形成共同参与，是经验对应，不在本结果之内。

**反驳 3：消耗者自己的事件不算活的，这似乎预先判了它。** 关系读法把消耗者的事件排除在 living 之外，`valuing_consumption_reaches` 的前提（某立场珍视消耗者的活动）因而只能来自 S0 以外。

*回应。* 正是这样，而且这是结论的要点。S0 只要求珍视自己活的、进一步生成的内容。一个在关系读法下消耗的形成，其活动不在其中；如果某个立场仍珍视这一活动（例如赢者珍视赢），N_rel 就把意义传到被消耗者。

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
5. 独立反审尚未进行。

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

### 6.2 损失的三条去路

| 声明 | 内容 |
|---|---|
| `continuing_restores` | 以不弱于先前的依存继续活跃，就意味着条件已经恢复 |
| `consumed_continues_transformed` | 无回程的损失之后仍然活跃的形成，必已转化其依存：不再依存于该条件，或所需更少 |
| `consumed_ends_when_fixed` | 依存不变时，无回程的损失终止该形成 |
| `Crossing.loss_does_not_decide` | 同一过程、同一配置、同一个断裂，三次运行。第一次：形成终止，损失无回程。第二次：旧依存消解，对另一条件的依存形成，形成始终活跃，损失无回程。第三次：形成蛰伏，条件得到更新，同一依存此后一直被维持。损失本身不决定去路 |

**解读。** 终止、转化与恢复不是外加的三个阶段。它们是同一依存关系跨步变化的三种结果，由同一结构定义，由定理相互约束，并在一个过程中都实际发生。[正典章节 §1](../../../../theories/becoming/chapters/THE-THEORY-OF-BECOMING.md#1-生成同一展开--becoming-one-unfolding) 说“形成、维持、转化、退化与消解都是沿运行的关系变化，不是五个阶段”，这里是它在表示范围内的形式实例。

它也回应了[根基 §9](../../../../theories/becoming/chapters/BECOMING-FOUNDATION.md#9-the-content-of-the-whole-deduction) 区分的“关系整体与分化”：在这个表示中，各种变化方式由同一依存结构区分，而不是各自命名的谓词。但它不完成整体演绎。表示中的规定由同一结构构成，不等于全部现实的规定都如此构成，后者仍需哲学论证；[整体演绎的审查](GROUNDING-INFERENCE-AND-PRESENTATION.md#19-the-whole-deduction-and-the-passage-from-inclusion-to-relation)已说明，多数几种方式不能代替这一步。

### 6.3 逐步读法

L3，同一模块：

| 声明 | 内容 |
|---|---|
| `RenewingAt`、`renewing_at_active`、`not_renewing_at_of_broken` | 一个事件（形成，步）在更新之内，当它活跃，且该步维持它所参与的每个条件上的每个依存。整段运行的更新使每个活跃步都在更新之内；某步若断裂了它所参与条件上的依存，该事件就不在更新之内 |
| `Commons.stepwise_credits_before_escalation` | 先在更新之内汲取，后来超出：整段读法记为消耗；逐步读法记入第一步，不记第二步 |
| `Commons.dip_breaks_without_consuming` | 先超出一次，再停下等条件更新：整段读法不记为消耗；逐步读法不记入断裂的那一步 |
| `Dip.renewing_at_each_step_not_in_run` | 维持者在它自己的每个活跃步都在更新之内，整段却不更新：它不活跃时，另一个形成断裂了共同条件。整段更新不是自身各步的合取 |

L4，[Becoming.Metaethics](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Metaethics.lean) 的“The stepwise reading”一节：

| 声明 | 内容 |
|---|---|
| `Web.valuation` | 逐步读法：事件在更新之内即为 living；两个事件的形成在各自的步上共同参与某一条件，即为 related |
| `Web.connected_of_common`、`Web.significant_iff_of_common` | 每个活的事件都参与的条件使整体连通，于是 G0 恰等于种子加 N_rel 加 N_std，与整段读法相同 |
| `Web.breaking_relates`、`Web.valuing_breaking_reaches` | 断裂本身是一种关系：在断裂之步汲取的事件不是活的，并且与被断裂形成参与该条件的每个事件相关。在 N_rel 下，珍视这一事件的立场，必珍视那些活的事件 |
| `Conditions.stepwise_related`、`Commons.readings_differ` | 依存不变时，两种读法的 `related` 相同，只在 `living` 上不同；两个方向都有分歧 |

### 6.4 作者反审

**反驳 1：三条去路只是定义上的分情况。**

*回应。* 部分同意。`kept_or_broken` 与 `continuing_restores` 证明很短。内容在别处：
- 这些关系在依存可变的模型中成立，而静态模型表达不了转化；
- `loss_does_not_decide` 是存在性结果：三条去路在同一过程、同一配置下都实际发生，所以去路由后续关系决定（形成是否改变依存、条件是否得到更新），不由损失本身决定。

**反驳 2：逐步读法偷偷带进了因果归属。** 维持者的事件被记入更新，即使维持条件的是别人。

*回应。* 逐步读法读的是事件所处的关系，不是它的因果贡献。`Dip` 正显示这一点：维持者每步都在更新之内，条件却正被别的形成断裂。差别制造的归属仍是 [relational-renewal-classification](../../../../theories/becoming/results/records/relational-renewal-classification.md) 的下一步，这里没有做。

**反驳 3：两种读法冲突，哪一个是生生？**

*回应。* 两者回答不同的问题。整段读法问：形成在整段运行中是否消耗。逐步读法问：一个事件所在的那一步是否维持其条件。`Commons.readings_differ` 证明两个方向都有分歧，所以不能把一个当作另一个的细化。以哪一种或哪种组合作为 `living` 的读法，仍是前提卡上公开的对应选择。

**反驳 4：转化把所需水平降低也算进去，太宽。**

*回应。* 是的，依存减弱也算转化。应用若要区分减弱与替代，可以用 `Dissolves`／`Forms` 细分；`Crossing` 的转化运行是替代。

**反驳 5：逐步读法太严。** 条件因季节等原因自然下降时，下降那一步上的任何事件都不被记入。

*回应。* 属实，这是读法的严格性。周期层面的更新是 relational-renewal-classification 的下一步，可以作为第三种读法，这里没有做。

**反驳 6：`Crossing` 是为结论构造的玩具。**

*回应。* 它的作用是可能性见证：在可以表达依存变化的最小过程里，同一个断裂的三种去路都可实现。它不说明实际系统中哪条去路常见；那是经验问题。

### 6.5 边界

- 不证明任何读法是生生的正确读法，也不证明 S0、N、A、C、L 或 J。
- 依存可观测量与实际历史的对应，是每次应用的义务。
- 不处理差别制造归属、周期层面的更新，以及条件替代下分类是否保持（`Crossing` 的替代例除外）。
- 整体演绎仍开放（见 6.2 的解读）。
- 独立反审尚未进行。

## English summary

P3b of the unification plan. The Becoming layer can now supply two correspondence items of the Universal Metaethical Core.

- **Runs carry the classification.** `Becoming.Renewal` reads any run through observables of conditions as a `RelationalRenewal` unfolding, so the renewing/consuming classification applies to every run of every process.
- **One principle.** The depletion, natural-rank recurrent-renewal and unrenewed-drawdown bounds are cases of one principle: an observable that never rises from some step on falls only finitely often.
- **The class belongs to the run.** In one process from one configuration, one run renews and another consumes.
- **The reading.** In `Becoming.Metaethics`, `Conditions.valuation` makes `living` the recorded relational reading and `related` participation in a common condition.
- **Connection.** A common condition discharges connection, so G0 there is exactly a seed with N_rel and N_std. Disjoint conditions can leave a whole unconnected.
- **Consumption.** Consumption is itself a formed relation. Under N_rel, a standpoint that values a consumer's activity therefore holds significant the living events of what it consumes.

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
- **Three ways through a loss.** Continuing with an unweakened dependence means the condition was restored. A formation still active after a loss without return has transformed its dependence; with fixed dependence it ends. In one process from one configuration, the same broken dependence leads to an ending, a transformation and a restoration: the loss does not decide its issue.
- **The stepwise reading.** An event is within renewal when its step keeps every dependence on the conditions it participates in. Whole-run renewal credits every active step. Otherwise the two readings differ in both directions. A consumer's events before escalation are credited stepwise. A breaking event in a run whose condition returns is not credited stepwise, although its formation does not consume. A formation can be within renewal at each of its own steps without renewing in the run.
- **Evaluation.** `Web.valuation` reads `living` stepwise. A common condition still discharges connection. A breaking event is related to the broken formation, so under N_rel valuing it reaches that formation's living events.

The author's counterreview concedes that the dichotomies are short. The substantive content is that transformation becomes expressible and that the loss does not decide its issue. The stepwise reading records relational situation, not causal contribution. Which reading of `living` to adopt remains a disclosed correspondence. The whole deduction remains open: modes distinguished by one structure in a representation do not establish the relational constitution of everything actual.
