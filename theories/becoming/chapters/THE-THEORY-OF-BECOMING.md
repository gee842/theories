# The Theory of Becoming / 生成／变化之论

2026-10-09，Asia/Bangkok。方向：Yongxu Ren。本章的组织与表述由 AI（Claude）撰写，依据：

- Ren 的[优先提议](../../../sources/15-codex-theory-conversations/2026-10-08-theory-of-becoming-priority.md)；
- Ren 对[整体与 manifold](../../../sources/15-codex-theory-conversations/2026-10-09-becoming-whole-generative-manifold.md)的澄清；
- Ren 的[生生方向](../../../sources/15-codex-theory-conversations/2026-10-07-shengsheng-ethical-direction.md)；
- Ren 的[统一为一个理论](../../../sources/15-codex-theory-conversations/2026-10-09-one-theory-unification.md)的指示。

Ren 的原话以引文标出，其余是 AI 的阐述。

**本章是理论的正典入口。** 本章：

- 把已建立的论证组织为一个理论；
- 列出全部前提；
- 指向每项结论的证据。

新的形式结果陈述在同一条 Lean 脊柱上（§9）。既有章节仍是各自论证与证据的记录，按原范围保留；它们作为入口的作用由本章取代（§11）。

**This chapter is the canonical entry to the theory.** It does three things:

- organizes the established arguments as one theory;
- states every premise;
- links each conclusion to its evidence.

New formal results are stated on one Lean spine (§9). Earlier chapters remain the record of their arguments and evidence at their original scope, and this chapter replaces only their role as entry points (§11).

## 一句话 / In one sentence

**生成／变化之论说明：在同一关系展开中，关系怎样形成、维持、转化、退化与消解，生命、演化、认识与评价怎样在其中分化。它不先假定生成是好的。** 它的 Universal Metaethical Core 采用 Ren 授权的一条公理 G0：整体中的生及其继续生成具有基本的正面规范意义。连同公开的实践前提，它给出向每个处境中的智能提出的理由，以及 AI 对齐的规范框架。

**The Theory of Becoming explains formation, persistence, transformation, degeneration and dissolution within one relational unfolding, and how life, evolution, knowing and evaluation differentiate within it, without first assuming that becoming is good.** Its Universal Metaethical Core adopts one axiom authorized by Ren, G0: living and further generation within the whole have basic positive normative significance. With explicit practical premises, it supplies reasons addressed to every situated intelligence and a normative framework for AI alignment.

Ren 提出这一范围时写道：

> when we add axiom, we can define what is good, which is a part of the whole space generative model projects
>
> but, if we count all space, generative, degenerative, we get The theory of evolution, or the theory of becoming/life, which doesn't even require axiom, i think can be done with 0

并澄清：

> the whole thing, the theory of becoming, is deductively necessary.
>
> generative is a part of its manifold

**由此有两个分开的目标。**

1. **整体的演绎必然性**：说明 Becoming 整体的必要内容，不加实质公理。这是开放的首要目标（§8）。
2. **整体中的伦理方向**：经公开的 G0 及实践前提，说明生生怎样获得规范意义。在已声明的条件下，这一目标已经完成（§6）。

二者不能互相替代。无伦理公理不等于无实质公理；Lean 公理报告为空也不等于没有前提。

**Two targets are kept apart.**

1. **The deductive necessity of the whole**, without added substantive axioms, is the open first priority.
2. **The ethical orientation within the whole**, through disclosed G0 and practical premises, is complete at its declared conditions.

Neither substitutes for the other. An absence of ethical axioms is not an absence of substantive premises, and an empty Lean axiom report is not an absence of premises.

## 0. 前提卡 / Premise card

每个前提都具名、可见。在 Lean 中，它们是定义或假设，不是公理；脊柱的每条声明的公理报告都为空。

Every premise is named and visible. In Lean they are definitions or hypotheses, never axioms; every declaration of the spine has an empty axiom report.

| 层 / Layer | 前提 / Premise | 内容 / Content | Lean | 地位 / Standing |
|---|---|---|---|---|
| 逻辑 / Logic | 证明语言 | Lean 4.29.1 内核与 Std；有限归纳的轨迹 | — | 方法承诺，另作说明 |
| 动力学 / Dynamics | 过程 | 声明可容许的变化：`step s a t` | `Generative.Process` | 每次应用外给的局部规律 |
| 对应 / Correspondence | 可观测量 | 主张的实现、条件水平、依存与汲取对应实际历史 | `Frame.realized`、`Conditions` | 应用义务 |
| 对应 | 形成 E | 被评价的生活与关系确实在展开中形成 | — | 应用义务 |
| 对应 | 连通 | 活的主张经已形成的关系相连 | `Valuation.Connected` | 在条件与参与的对应纪律下由共同条件给出（§6.3）；一条纪律已陈述（交互：一方汲取、另一方以正水平依存），在声明的类中给出连通 |
| 对应 | `living` 的读法 | 已定义三种：整段（活跃且在该运行中不消耗）、逐步（活跃且不侵蚀）、关系层；都相对于一次运行，读出的是与他者依存相容的活动，不含继续生成 | `Conditions.valuation`、`Web.valuation`、`Web.relations` | 公开的读法选择，由 Ren 决定（§6.3）；是否即生生，是哲学论证 |
| 伦理 / Ethics | **G0**（Ren 授权的公理） | 整体中的生及其继续生成具有基本正面意义 | `Valuation.Significant` | 采用；其内容由下面三条精确刻画 |
| 伦理 | S0 | 一个立场自身活的、继续生成的内容对它有正面意义 | `SelfGood` → `Seed` | 规范前提 |
| 伦理 | N_rel | 意义沿已形成的关系传到活的内容（承受者一侧） | `transmits` | 边界中立前提 |
| 伦理 | N_std | 活的内容的意义对每个立场成立（立场一侧） | `shares` | 边界中立前提 |
| 伦理 | A | 有通达、且在所见范围上确保本立场下的正面内容，即有一项支持理由（受话者一侧） | `articulates` | 外在论表述前提 |
| 实践 / Practice | C | 无损失且实现更多活的内容的扩展更好 | `Comparison` | 比较前提 |
| 实践 | L | 结果比较提升到多结果回应；保守默认是“每个结果都优于每个结果” | `LiftBetter` | 实质承诺（§6.5） |
| 实践 | J1–J4 | 完整比较与保留损失；基本条件优先；有界责任；正当可行的选择 | `PracticalJudgment`、`BetterAt` | AI 提出、Ren 授权的附加承诺 |

**不假定的内容。** 本理论不假定以下各项：

- 生成是好的；
- 整体必然改善或普遍增长；
- 存在固定的共同效用；
- 存在彼此独立的价值所有者；
- 每次变化都具生成性；
- 每个处境都有确定的全局因果次序。

**Not assumed:**

- that becoming is good;
- inevitable improvement or universal growth;
- a fixed common utility;
- independent owners of value;
- that every change is generative;
- a definite global causal order at every interface.

## 1. 生成：同一展开 / Becoming: one unfolding

**机制。** 起点是过程：一个配置经一次可容许的变化成为另一个配置。

- 框架 `Frame` 只多加一件事：每个配置上实现了哪些主张。主张描述分化了的实现及其关系，不是独立的所有者。
- 运行 `Run` 是无穷的实际执行。
- 可达 `Reach` 是有限的可容许路径。
- 不变量 `Invariant` 是每步都保持的性质。
- 新实现 `Novel` 是某种读法下此前未实现的主张。

这些都由核心的轨迹 `Trace` 定义，因此与核心的组合、乘积和传递定理直接相接（[Becoming.Frame](../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Frame.lean)）。

**Mechanism.** The starting point is the process: a configuration becomes another through an admissible change.

- A `Frame` adds only which claims are realized at each configuration.
- A `Run` is an infinite actual execution.
- `Reach` is a finite admissible path.
- An `Invariant` is preserved by every step.
- `Novel` is a claim of a given reading realized and not realized before.

All are defined through the core `Trace`, so they compose with the core's theorems.

**形成、维持、转化、退化与消解都是沿运行的关系变化，不是五个阶段。** 同一次活动可以使某种继续成为现实能力，同时毁掉另一种条件。一个形态还在，不等于它仍有原来的作用能力。以下结果说明这些区分：

- **端点可能。** 沿一段实际轨迹，全部端点可能得到保留，当且仅当存在回程；否则有构造性的丧失见证（[endpoint-loss-and-return](../results/records/endpoint-loss-and-return.md)）。
- **当前能力与最终可达。** 二者不同：准备会改变一步内的共同实现能力（[effective-capacity-and-eventual-reachability](../results/records/effective-capacity-and-eventual-reachability.md)）。
- **整体可能空间。** 合并一族过程的步骤，恰好保留它们端点历史的并集，当且仅当这个并集对共同边界的接合封闭。包容全部结果，不等于可以任意拼接结果的成立条件（[becoming-context-coherence](../results/records/becoming-context-coherence.md)）。
- **共同作用。** 各部分的局部状态都不变，共同作用仍可改变（[joint-correlation-reduced-dynamics](../results/records/joint-correlation-reduced-dynamics.md)）。局部区别可以丧失，而在保留的共同关系上仍可恢复（[control-coherence-loss](../results/records/control-coherence-loss.md)）。
- **规律与轨迹。** 步骤规律与端点轨迹相互决定（[trace-law-equivalence](../results/records/trace-law-equivalence.md)）；保持步骤的映射传递轨迹（[finite-trace-transport](../results/records/finite-trace-transport.md)）。
- **依存的变化。** 依存本身属于展开：一个形成依存于哪些条件、所需多少，可以跨步形成、维持、断裂与消解，变化总发生在某一步上（[Becoming.Dependence](../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Dependence.lean)）。在形成只在有支持处活跃的前提（`Dependent`，排除缓冲与滞后）下，定理把损失之后的三种结局联系起来，它们既不穷尽也不互斥：以不弱于先前的依存继续，意味着条件已恢复；无回程的损失之后仍活跃，意味着依存已转化；依存不变则终止。同一过程、同一配置下，在同一步断裂同一依存（按步首约定读）之后，三种结局都可实现：断裂的读法不决定后继配置，构成断裂的那一步选定结局（[becoming-dependence-dynamics](../results/records/becoming-dependence-dynamics.md)）。这是表示内的定义与约束，不是第一句话的证明。

**Formation, persistence, transformation, degeneration and dissolution are relational changes along runs, not five stages.** One activity can make a continuation actually possible while destroying another condition, and a retained form need not retain its efficacy. The results above establish, at their scopes:

- endpoint loss and return;
- the difference between current capacity and eventual reachability;
- the exact condition under which pooling processes invents no history;
- joint change with unchanged local states;
- local loss recoverable within a retained joint relation;
- dependence that forms, holds, breaks and dissolves at steps, and three outcomes of a loss (ending, transformation, restoration), connected by theorems where a formation is active only where supported; the reading of the break does not fix which follows.

**整体与 manifold。** 演绎必然性的主张针对 Becoming 整体；生成性是其中的部分，不是每次变化必须满足的条件。退化、终止与混合变化都在同一展开中，不需要被改名为生成。详见[根基范围](BECOMING-FOUNDATION.md#whole-and-manifold)与[关系怎样变化](THEORY-OF-BECOMING.md)。

**Whole and manifold.** The necessity claim concerns Becoming as a whole. Generativity is part of it, not a condition every change must meet.

## 2. 组织、更新与演化 / Organization, renewal and evolution

**更新与消耗是同一个分类，属于运行。** 经条件的可观测量读出，任一过程的任一运行都是一个关系展开（[Becoming.Renewal](../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Renewal.lean)）。

- **更新。** 一个形成是更新的，当它依存或汲取的每个条件，都继续支持每个依存于该条件的形成。
- **消耗。** 一个形成是消耗的，当它汲取的某个条件，使某个依存者从某步起永久失去支持。
- 两类互斥，但不穷尽：波动的情形两者都不是（[relational-renewal-classification](../results/records/relational-renewal-classification.md)）。

**Renewal and consumption form one classification, and it belongs to runs.** Read through observables of conditions, every run of every process is one relational unfolding.

- A formation is renewing when every condition it depends on or draws on keeps supporting every formation that depends on it.
- It is consuming when it draws on a condition some dependent permanently loses.
- The classes are exclusive but not exhaustive: fluctuating cases are neither.

**一条原则约束无更新的继续：从某步起不再上升的可观测量，只能下降有限次。** 以下三条界都是它的情形（`falls_finitely`）：

- 耗竭：每步都降低储备，则没有运行；
- 自然数秩的复现更新：凡非更新之步都降低秩，则更新任意晚地复现；
- 无更新汲取：汲取者的活跃只有有限次。

**分类属于运行，不属于配置或形成自身的轨迹。** 同一过程、同一初始配置下，焦点形成每一步都活跃：一次运行在更新之内，另一次消耗维持者的条件，维持者随之终止（`class_belongs_to_the_run`）。因此，持续、成功或增长都不能证明更新（[own_trajectory_does_not_decide](../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/RelationalRenewal.lean)）。

**逐步读法。** 分类也可以逐步读：一个事件（形成，步）在更新之内，当它所在之步维持它所参与条件上的每个依存（`RenewingAt`）。整段更新的形成，每个活跃步都在更新之内；一个形成也可以在自己的每个活跃步都在更新之内，整段却不更新。

作为 `living` 的逐步读法，四次独立审查之后的工作候选（待 Ren 选择）是“活跃且不侵蚀”。事件侵蚀，当它在某步汲取某条件，而该步之后，条件既低于一个依存现在的所需，也低于该依存在不间断成立期间的某步曾被满足的所需（`MetAbove`）。在断裂某个依存之步汲取（断裂）是侵蚀的一种。这一读法：

- 记入被断裂者自己的事件（它不汲取）；
- 在依存成立期间从未以其所需被满足的依存，不使汲取者侵蚀，所需下降时也如此（`NewNeed.never_met_not_undermining`、`FallingNeed.never_met_not_undermining`）；只低于增长到从未被满足的所需，不算侵蚀（`RisingNeed.grown_need_not_met`），所需增长之后，把水平取到曾被满足的所需之下的汲取侵蚀而不断裂（`Stunted.stunting_undermines`）；依存中断一步即开始新的一段（`Gap.lapse_starts_afresh`），休眠或迁出是否表示为持续的依存，是应用义务；
- 扣下损失之后继续的汲取：那样的汲取不再断裂什么；在公地见证中，它使条件回不来（`drawing_after_loss`）；
- 代价：它读的是共同参与一个未恢复的短缺，不是汲取的效果。`draws` 不带数量，所以恰取更新量、甚至不改变任何水平的汲取也被扣下（`Pool.within_share_undermines`、`Pinned.undermining_without_effect`）。

它与整段读法两个方向都有分歧：加码之前的汲取逐步被记入，整段却记为消耗；短暂下降中断裂之步的汲取逐步不被记入，而条件随后恢复，整段不记消耗（[becoming-stepwise-reading](../results/records/becoming-stepwise-reading.md)，[审查与更正](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md)）。

**回程给更新分级。** 更新与消耗之间按回程时间分级：每步都维持、在有界周期内回到、终会回到而无界、不再回到。消耗恰是某个依存不再回程（`consumed_iff`）。季节性条件在两步周期内更新；恢复可以无界地变慢而条件从不被消耗。更新蕴含一步周期内更新，逆命题不成立（`LateMet`）。周期层面的读法在两步周期下记入短暂下降，对每个周期都扣下加码（[becoming-return-grades](../results/records/becoming-return-grades.md)）。

**有限的历史不决定分类。** 对每个视界，同一过程有两次运行在视界之前完全相同：每步都超出更新地汲取，每个事件都在更新之内；此后一次更新，一次消耗。任何由有限前缀决定、并记入每次更新运行的读法，必记入某次消耗运行（[becoming-finite-horizon](../results/records/becoming-finite-horizon.md)）；在有反馈的支持门控定律中也是如此。这一结论的力量来自“记入每次更新运行”：那次更新运行在视界之前同样超出更新地汲取，整段读法记入这些汲取（`whole_run_credits_overdraw`）；按数量的读法（所取不超过更新）可由有限历史判定，并扣下每一次超出（`amount_reading`）。若要判断的是一段汲取的整段结局，需要对运行之继续的探究与审议，不只是对过去的观察。

**One principle bounds continuation without renewal: an observable that never rises from some step on falls only finitely often.** Its cases are depletion, natural-rank recurrent renewal and unrenewed drawdown. **The class belongs to the run**, not to a configuration or to the formation's own trajectory: persistence, success and growth do not certify renewal. **A stepwise classification** places an event within renewal when its step keeps every dependence on the conditions it participates in. As the stepwise reading of `living`, the working candidate after four independent reviews, pending Ren's choice, an event lives when it is active and not undermining: it does not draw on a condition at a step after which the condition is below both the present need of a dependence on it and a need that dependence met during its unbroken tenure. It and the whole-run reading differ in both directions. **Return grades renewal**: consumption is exactly a dependence that never returns, and recovery can slow without bound while the condition is never consumed. **No finite history decides the classification**: any reading fixed by a finite prefix that credits every renewing run credits some consuming run, with feedback too. A per-step amount reading escapes this only by not crediting every renewing run.

**联合消耗没有单一的消耗者。** 两个形成各自都在更新之内，合起来却消耗了共同条件，两者都随之终止。这一类属于它们的联合关系（`jointly_consuming`）。

- **反馈。** 在更新依赖被更新条件的定律族中，越过支持阈值的损失在定律内不会回来（`no_return_below_support`）。
- **修复。** 有支持的贡献路线可以修复维持关系（[supported-renewal-recovery](../results/records/supported-renewal-recovery.md)）。
- **替代。** 同一定律族中，能替代条件的消耗者转化依存而持续，在整段读法下仍是消耗的（几乎由定义给出），维持者终止；逐步读法在维持者失去支持之前记入它，此后到它转向为止扣下它（`stepwise_credits_substitution`、`slow_withheld_two_steps`）。自身的持续不证明更新（[substitution-preserves-consumption](../results/records/substitution-preserves-consumption.md)）。
- **窄定律类。** 在一个磨损定律类中，更新与消耗是动力学上可区分的（[renewing-consuming-formation](../results/records/renewing-consuming-formation.md)）。

**继续生成。** 以上读法读出的都是“不损”。作者把生生的第二个“生”的一种读法陈述为生起：一个形成跨某步生起，当它此前不活跃、此后活跃；生成不息，当某个形成在任意晚的步生起，同一形成可以再生起（[Becoming.Generation](../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Generation.lean)，[unceasing-generation-needs-renewal](../results/records/unceasing-generation-needs-renewal.md)）。一个事件消耗一个有限的条件家族，当在它的每个家族都不上升之步，其中某个条件下降；这只说事件的每一步家族中有条件变化，不涉及事件与那个条件的关系（`depletes_iff`、`Tide.unrelated_depletion`）。若生起消耗家族，不息的生成使其中某个条件在任意晚的步净上升；若每次上升都由某个形成的更新造成，更新的活动就在任意晚的步复现。平衡的流给出不需要净上升的形式：在第一个活跃步从家族取用的形成不息地生起时，补充与补充者在任意晚的步出现，它看得见与汲取同步的补充（`replenishment_recurs`）。月亮更新的潮水在任意晚的步上升而没有任何生起，所以在这些前提下，不息的生成严格强于复现的更新（`Tide.renewal_without_arising`）。以不被更新的条件为条件的生起停止；在有限个不被更新的条件之间替代，推迟终结而不逃脱终结。一个量从不上升而每次生起都使它下降（耗散）时，生成不是不息的（`dissipation_ceases`）；没有耗散，总量不变的封闭循环可以维持不息的生成（`Recycle.closed_unceasing`）。作者由此论证：在耗散之下，任何有限部分都不能独自不息。这里只读出 Ren 原话“不断创造更多生”中的“不断…生”；第二个“生”的范围留给 Ren。

**Continued generation.** As the author's reading of the second 生, a formation arises across a step when it is inactive before and active after it; generation is unceasing when some formation arises at arbitrarily late steps. An event depletes a finite family when at each of its steps at which none of them rises one of them falls, which says only that some condition of the family changes. When arising depletes the family, unceasing generation makes renewal recur; in balanced flows, takers arising unceasingly make replenishment recur, which sees replenishment concurrent with drawing. A tide the moon renews rises with nothing arising, so under these premises unceasing generation is strictly stronger than recurring renewal. Arising on a consumed condition ceases, and substitution among unrenewed conditions defers the end without escaping it. Under dissipation generation is not unceasing; without it, a closed cycle can be. Only the “unceasing” of Ren's “unceasingly creating more 生” is stated here; the scope of the second 生 is Ren's.

**更多。** 把条件读作数量：每步参与的形成从条件取用多少、给予多少（[Becoming.Flow](../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Flow.lean)、[Becoming.Population](../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Population.lean)，[more-needs-renewers](../results/records/more-needs-renewers.md)）。流平衡时，条件水平的每次变化恰是取用与给予之差；一步或一段步上，家族的总水平加上取用，等于之前的总水平加上补充（消耗与补充的平衡）。每次上升于是都由某个活跃的补充者造成，上面“每次上升都由形成的更新造成”从前提变为定理。“更多”读作（作者的读法）：对每个数，从某步起至少有那么多形成从一个有限的条件家族取用。量是自然数，每个取用者每步至少取用一个单位，所以这样的生成需要家族所得的补充没有最终的界；每个形成每步的给予有上限时，补充者也没有最终的界，在平均的意义上越来越多，却可以在无穷多步上为零（`Pulse.pulsed`）。在活跃形成的普查之下，只有活跃的形成取用、且只从它汲取的条件取用时，不止地更多蕴含不息的生成（`More.unceasing`）；不息地反复生起的开花满足这些前提而不更多，所以蕴含是严格的；没有普查，或取用者从不活跃时，不止地更多可以没有任何生起（`Dormant.more_without_arising`、`Inactive.more_without_arising`）。所需的补充于是构成严格的层级：取用者不息地生起需要补充在任意晚的步出现，不止地更多需要补充没有最终的界。补充者可以就是取用者自身（`Cycle.closed_more`）；把要求传到展开中更远之处需要耗散前提。作者把它读作“生生”的一种结构：更多的取用需要没有最终界的补充，由展开之内的形成给出。可能性、多样性与复杂性的上升是“更多”的另外读法，这里不陈述。

**More.** Read as amounts, conditions are taken and given by the formations taking part in each step, and depletion balances replenishment. In a balanced flow every rise is made by an active renewer, so the premise above becomes a theorem. Generation more without end, with ever more formations taking from a finite family from some step on (the author's reading), needs replenishment with no eventual bound, since each taker takes at least one unit; when each formation gives at most a fixed amount, renewers have no eventual bound and grow in an averaged sense, though they can be absent at infinitely many steps. Under a census of active formations, with only active formations taking from what they draw on, more without end implies unceasing generation, strictly; without the census or with inactive takers it does not. The replenishment needed thus forms a strict hierarchy. The renewers can be the takers themselves. Diversity, complexity and possibility are not stated.

**演化是具体的机制，不是一切变化的同义词。** 传递、重建、变异与选择各有其关系，须各自说明（[演化之论](THE-THEORY-OF-EVOLUTION.md)、[演化组织](EVOLUTIONARY-ORGANIZATION.md)）。已检查的连接如下：

- 继承的结构排列改变后续复制（[inherited-structural-copying](../results/records/inherited-structural-copying.md)）；
- 形成的登记改变复制的保真度（[formed-copying-registration](../results/records/formed-copying-registration.md)）；
- 形成的检查／编辑改变已形成的后继（[formed-copying-correction](../results/records/formed-copying-correction.md)）；
- 生长约束碎裂与后继组成（[growth-constrained-fragmentation](../results/records/growth-constrained-fragmentation.md)）；
- 组织规则的形成与继承（[organizational-rule-inheritance](../results/records/organizational-rule-inheritance.md)）。

**Evolution names specific mechanisms**, with transmission, reconstruction, variation and selection each explained through their own relations. It is not a synonym for every change.

## 3. 认识与探究 / Knowing and inquiry

**所见范围由动力学给出。** 一个探究策略的所见范围，是它实际执行可达的配置。可靠（sound）的策略在其所见范围上确保它的目标（`Scope.secures`，[Becoming.Inquiry](../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Inquiry.lean)）。这收窄了一个原本由应用自行给出的参数。

**The scope of an inquiry is given by the dynamics**: the configurations its actual executions reach. A sound policy secures its goal there.

**判断即一步探究。** 不确定下的判断不需要另立概念：在每个所信配置上都可容许的回应，恰是“判断过程”的共同回应——这个过程在被判断的配置上取一个可容许的回应，然后结束（`commonResponse_judge_iff`）。稳健判断、观察下的纠正与安全选择因此都是同一个共同回应；细化观察就是收窄信念，所以它们保持（`commonResponse_antitone`；外围桥接 [CorrectionInquiry](../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/CorrectionInquiry.lean)）。

**A judgment is a one-step inquiry.** A response admissible at every configuration believed possible is exactly a common response of the process that takes one admissible response and closes. Robust judgment, correction under observation and safe choice are therefore one common response, and refining observation narrows belief, so it preserves them.

**知识。** [知识一章](KNOWLEDGE.md)辩护如下候选：命题知识是这样的真实判断——它的形成或维持，通过认知能力与使其正确的实际关系相连，且其正确不是偶然。知道、理解与会做是不同的成就，[哲学说明](PHILOSOPHICAL-ACCOUNT.md)把它们与共同探究和实践智慧合在一起。

**Knowledge.** The defended candidate is a true commitment competently connected to what makes it correct, and non-accidentally so. Knowing that, understanding and knowing how are distinct achievements.

**已检查的探究条件。**

- **有限可错探究的必要信息条件**：承诺覆盖不超过两类错误权重加证据分离（[finite-fallible-inquiry-necessity](../results/records/finite-fallible-inquiry-necessity.md)）。
- **分支测试**：分支测试等价即双模拟（[branching-tests-bisimulation](../results/records/branching-tests-bisimulation.md)）。
- **有限计划**：可行性等价于按观察分支的有限计划（[finite-continuation-plans](../results/records/finite-continuation-plans.md)）。
- **推导**：推导可靠（[derivation-soundness](../results/records/derivation-soundness.md)）；保留绑定的代入恰在每个位置提供原有根据（[binding-preserving-substitution](../results/records/binding-preserving-substitution.md)）。
- **跨尺度的问题**：问题能否翻译与恢复（[finite-granularity-question-recovery](../results/records/finite-granularity-question-recovery.md)）。全部前缀问题仍可能遗漏中间损失（[prefix-observation-loss](../results/records/prefix-observation-loss.md)）。
- **学习**：取得的绑定进入组合使用（[acquired-binding-compositional-use](../results/records/acquired-binding-compositional-use.md)）；学习程序经实际执行重建（[learned-procedure-transmission](../results/records/learned-procedure-transmission.md)）。
- **证据**：被执行的指令传递候选证据（[mediated-evidence-transport](../results/records/mediated-evidence-transport.md)）；可错见证下的完整可诊断性（[fallible-witness-diagnosability](../results/records/fallible-witness-diagnosability.md)）。

**开放。** 完整核心对科学探究的不可或缺性尚未建立（[scientific-inquiry-foundation](../results/records/scientific-inquiry-foundation.md)）。

## 4. 集体动力学 / Collective dynamics

**共同活动先从实际关系说明。** 不预设对立的利益、筹码、谁赢得更多或固定的共同效用（[共同问题提醒](../../../sources/15-codex-theory-conversations/2026-10-08-collective-destructive-attractors.md#common-problem-solving-and-awareness)）。实际的冲突与差异保留。

**Collective activity is explained from actual relations first**, without presupposing opposed interests, bargaining chips, winners or a fixed common utility. Real conflicts and differences remain.

**市场。** 只有当成功的活动更新了后续交换与生活所依赖的条件、且受影响者仍能发现损害并改变安排时，市场选择才保持在生成区域（[市场与生成区域](MARKETS-AND-GENERATIVE-REGIMES.md)）。已检查的界如下：

- 保护证书下的持续运行（[market-protected-continuation](../results/records/market-protected-continuation.md)）；
- 部分纠正的精确到达边界（[market-partial-correction-boundary](../results/records/market-partial-correction-boundary.md)）；
- 有支持的有限转移（[market-supported-finite-transition](../results/records/market-supported-finite-transition.md)）；
- 有限支持救不回的正种子区间（[market-finite-support-obstruction](../results/records/market-finite-support-obstruction.md)）。

**Markets** stay in generative regimes when successful activity renews the conditions of further exchange and life, and affected people can still discover damage and change the arrangement.

**赢的元吸引子。** 当成功者获得的影响削弱了对产生成功的策略的约束时，当下的优势就改变未来的选择（[meta-attractor](../../meta-attractor/README.md)）。脊柱给出以下结构事实：

- **联合消耗没有单一的消耗者**（§2）；
- **共同参与**：消耗者与失去支持者共同参与被汲取的条件（`consumption_relates`）；
- **差别制造属于共同活动**：多重决定下，扣除任何单独一方的部分，损失照样发生，没有哪一方单独造成差别，而关系读法仍把每个汲取者计为消耗；一个形成的渐进耗竭中，整段的结局由尾部决定，没有哪个有限的事件集合造成整段的差别，而断裂事件造成那一次断裂的差别（[joint-difference-making](../results/records/joint-difference-making.md)）；
- **替代不证明更新**：靠消耗取胜的一方可以转向别的条件而持续，失去者不随之恢复；在逐步读法下，它在失去者失去支持之前被记入，此后到它转向为止被扣下（§2）。

因此，在 N_rel 下，靠消耗赢得的一方不能以“无关”为由把失去者放在意义之外（§6.3）；在关系读法下，“我的一份不造成差别”也不把它移出消耗。这些都不推出责任或义务。

**The meta-attractor of winning**: present advantage that weakens restraints on its own strategy changes future selection. Four spine facts bear on it:

- joint consumption has no single consumer;
- the consumer and the formation that loses support participate in the drawn condition;
- under overdetermination no single part makes the difference, while the relational reading still counts each drawer as consuming;
- substitution lets a consumer persist without certifying renewal.

Under N_rel, winning by consumption cannot place the loser outside significance by unrelatedness, and under the relational reading “my share makes no difference” does not remove a drawer from consumption. Neither yields responsibility or duty.

## 5. 评价的形成 / How evaluation forms

**立场、其区域与意义都在展开中形成。** `own` 是已形成关系的区域，不是所有者；`related` 是非零的已形成关系，即条件、依存、传承与合作。

**一个标准获得影响、认出其对象、得到正当根据、被实际遵行，是四个不同的问题。** 形成的标准可以是错的；学习某种倾向，不等于学到了理由。

**Positions, their regions and significance form within the unfolding.** A standard's influence, its recognition of a target, its warrant and its actual enactment are four distinct questions. A formed standard can be wrong.

**已建立的形成路线。**

- **评价接续**：取得的理解形成评价影响，并进入有根据的应用（[评价接续](EVALUATIVE-UPTAKE.md)、[评价根据](EVALUATIVE-GROUNDING.md)）。
- **在条件下获得正当回应**：起初缺失的评价联系，可以成为对另一存在有根据回应的中介；同一联想学习之后也可以压制这一回应，而不推翻理由。
- **评价者路线**：自我之善，加不受限单调性与容差，给出立场索引、单一历史上的 G0 实例。经独立审查，它已收窄（[self-good-reachable-g0](../results/records/self-good-reachable-g0.md)），并在 §6 中统一。

**比较的读法。**

- **关系信息**：共同组合比较需要关系信息，单项可能性不够（[relational-generative-comparison](../results/records/relational-generative-comparison.md)）。
- **关系读法**：按关系读法，C 把消耗性形成排在它不在的情形之下；逐事件的宽读法则不作决定（[relational-reading-comparison](../results/records/relational-reading-comparison.md)）。
- **基本条件优先**：它独立于 C，并排除每个自然数分数（[protection-priority-excludes-uniform-aggregation](../results/records/protection-priority-excludes-uniform-aggregation.md)）。
- **分类未定时的比较**：见[classification-robust-generative-comparison](../results/records/classification-robust-generative-comparison.md)。

## 6. Universal Metaethical Core / 普遍元伦理核心

### 6.1 G0 的内容 / What G0 says

Ren 对伦理质量的回答：

> 我的答案是生生不息 - 一种整体的，不断创造更多生的方向，而这个方向产生的可能性，多样性越高，复杂性/复杂结构的复杂度可以不断的上升，就是一个好的方向

G0 是 Ren 授权采用的公理措辞。它的对象从一开始就是生生；“生”的几种范围都可以成立，并可能得到不同的范围。

**刻画定理。** 在有某个活的主张的连通整体上，下面两者等价（`significant_iff`，[Becoming.Metaethics](../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Metaethics.lean)）：

- 每个立场都持有的 G0（主张层面）；
- 种子 S0，加两条边界中立 N_rel 与 N_std。

因此，G0 中超出评价者原本已持有之物的全部内容，都精确落在边界中立上。“G0 ⇒ 前提”这一方向几乎是平凡的，内容在反方向与极小性。

**Characterization.** On a connected whole with some living claim, G0 for every standpoint is equivalent to a seed (S0) with relational and standpoint boundary neutrality. Everything G0 adds beyond what an evaluator already holds lies in boundary neutrality. This characterizes Ren's adopted G0 and does not replace it.

### 6.2 极小性与对手的形状 / Minimality and the shape of rivals

去掉种子、N_rel、N_std、连通或 A 中的任何一项，都留下一个一致的反模型。**每个对手都接受同一条规则，只是限在某个已形成的边界之内**：

- 自己的区域；
- 自己的立场；
- 认同者。

拒绝 G0 的一方因此不必否认规则，只需划出一条边界。争论随之落到这条边界有没有根据上。Sidgwick 的实践理性二元论没有因此消解，只是被定位到边界中立这一前提上。

Each premise has a consistent countermodel when dropped. **Every rival accepts the same rule inside a formed boundary.** The disagreement is located at whether that boundary is warranted.

### 6.3 从展开读出连通与消耗 / Connection and consumption from the unfolding

L3 可以给出 `living` 与 `related` 两项对应（[becoming-renewal-reading](../results/records/becoming-renewal-reading.md)）：

- `living` 取关系读法，即活跃且在该运行中不消耗的形成事件；
- `related` 取共同参与某一条件。

由此得到三点：

- **连通在对应纪律下由共同条件给出。** 每个活的形成都参与的共同条件，使整体连通；于是在那里 G0 恰等于种子加 N_rel 加 N_std（`significant_iff_of_common`）。条件互不相交时，整体可以不连通（`Separate.not_connected`）。但这依赖什么算条件、什么算参与：加入一个人人在水平 0 依存的条件即可免费连通，而人人汲取的过粗的共同条件又会在其依存落空时使 living 变空。一条对应纪律（[condition-correspondence-discipline](../results/records/condition-correspondence-discipline.md)）只在一方汲取、另一方以正水平依存时才经由条件相关：惰性条件不再连通任何东西（`inert_connects`）；每个活的事件都承担于其上、有活的汲取者与活的依存者的条件，仍使整体连通（`connected_of_commons`）；经由一个条件的连通由它的活的使用造成（`Shared.connection_by_living_use`）。交互是结构上的共现（一方汲取、另一方以正水平依存，在任何步上），还不排定时间，也不问效果；共同依存是纪律所省略的关系，不是没有关系。纪律排除不了人人以正水平依存、被一个活的事件使用一次的被更新条件（`one_use_connects`），那是一个须由应用检验的事实主张。
- **意义沿共同参与传递。** 消耗者与被消耗者共同参与被汲取的条件；在 N_rel 下，一个立场若珍视某个消耗者的活动，就必须珍视被它消耗的形成的每个活的事件（`valuing_consumption_reaches`）。传递不用到消耗本身。
- **读法相对于一次运行。** 同一过程、同一配置的两次运行可以给出不同的 living（`class_belongs_to_the_run`）。不依赖运行的读法，以及它与 `universal_reason` 的接通，开放。
- **对应义务不变。** 生物圈、气候之类的条件是否真被所有活的形成共同参与，是经验对应；关系读法是否即生生，是哲学论证。

**逐步读法与关系层读法。** 以“活跃且不侵蚀”为 `living`、以各自步上共同参与某一条件为 `related`，前两点照样成立：共同条件给出连通（`Web.significant_iff_of_common`）；在断裂之步汲取的事件与被断裂者共同参与该条件，在 N_rel 下，珍视这一事件的立场必珍视被断裂者活的事件（`Web.valuing_breaking_reaches`）。依存不变时整段与逐步读法的 `related` 相同，只在 `living` 上分歧，而且两个方向都有（`Commons.readings_differ`）。关系层读法以（形成，条件，步）为主张；一个事件的逐步读法恰是它所参与关系的读法的合取，同一事件可以有一个活的关系和一个侵蚀的关系（`Web.living_iff_relations`）。

**读法由 Ren 选择。** 独立审查判定关系读法的哲学根据尚未确立（[审查](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING-REVIEW.md)）。[研究 §8.5](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md) 按五条判据比较了各读法，并给出两条有范围的形式约束。其一，任何由有限前缀决定、并记入每次整段更新运行的读法，必记入某次消耗运行（`finite_reading_credits_consumption`）；它是否与 Ren 所采纳的问题冲突，取决于对这一问题的判决是否覆盖越过阈值之前的事件，以及可观测量是否带数量（`amount_reading`）。其二，单一部分的整段 but-for 检验不能代替参与（`Overdetermined.no_difference`、`no_finite_segment_makes_difference`）。[第二次审查](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-P7-REVIEW.md)接受全部数学，修正了侵蚀与 but-for 的定义，更正见研究 §11；[第三次审查](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-P8-P9-P7B-REVIEW.md)再修正二者，并把排序、替代与交互的说法收窄到所证明的范围，更正见研究 §12；[第四次审查](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-P9B-P10-P11-REVIEW.md)把侵蚀改为最小形式，并把继续生成与更多的说法收窄，更正见研究 §15。现有读法读出的都是“不损”，不含继续生成；继续生成陈述在整体的继续上（§2“继续生成”），尚未进入 `living` 的读法。哪一种读法或组合是生生的读法，是 Ren 方向内的规范与诠释选择，本章不替 Ren 作出。

The Becoming layer can supply `living` (the relational reading) and `related` (participation in a common condition):

- Under a correspondence discipline for conditions and participation, a common condition makes the whole connected, discharging that premise. One discipline is stated: a condition relates two events only when one draws on it and the other depends on it at a positive level. Idle conditions then connect nothing, a commons with a living drawer and a living dependent still connects, and connection through a condition is made by its living use; interaction is a structural coincidence at any steps, not yet ordered or effect-sensitive, and co-dependence is a relation the discipline omits; a renewed condition on which every formation depends at a positive level, used once, is not excluded, and is a factual claim for application to check.
- Under N_rel, valuing a consumer's activity reaches what it consumes, through co-participation in the drawn condition.
- The readings are relative to a run; a run-independent reading is open.
- Whether actual common conditions are shared by all living formations, and whether the relational reading is 生生, remain correspondence and philosophical questions.
- Read stepwise (active and not undermining) or at the level of relations, the first two still hold. The whole-run and stepwise readings differ in `living` in both directions. None includes further generation. Which reading, or combination, is the reading of 生生 is Ren's choice; the study's comparison supplies the material.

### 6.4 向每个立场的理由 / Reasons addressed to every position

**D 由 A 导出。** 不以认同为条件的定位表述 D，由 A 与 G0 的不带索引的意义导出（`positioned_articulation_of_articulates`）。

**普遍理由。** 一个以新的活的内容为目标的可靠探究，给每个有通达的立场一项支持理由（`universal_reason`）。规范前提是种子、N_rel、N_std 与 A；连通（在 §6.3 的对应纪律下，相对于一次运行）与可靠性是展开与探究的事实（[metaethical-core-characterization](../results/records/metaethical-core-characterization.md)，复用 [positioned-positive-reason](../results/records/positioned-positive-reason.md)、[positive-ground-open-futures](../results/records/positive-ground-open-futures.md)）。

**理由不是更多的东西。** 一项支持理由不是义务，也不是排序，也不预测认识或遵循。

**D follows from A**, and a sound inquiry for new living content gives every position with access a contributory reason. A contributory reason is not a duty or a ranking, and predicts no recognition or compliance.

### 6.5 比较、提升与实践判断 / Comparison, lifting and practical judgment

**C 与 J。** C 在框架的配置上陈述；J1/J2 的“先基本条件、再活的增益”由桥接层的 `BetterAt` 陈述（[practical-judgment-g0-j](../results/records/practical-judgment-g0-j.md)）。

**L 是被整合暴露出来的隐藏前提。** 情境给每个回应一个结果，过程却可以有多个结果；只要对回应作比较，就需要一条提升规则。在保守的 L 下：

- 比较、理由、协调选择的存活、持续改进无存活者，都对每个框架成立；
- 函数式情境恰是其中的确定情形（`articulation_iff_lifted`，[becoming-spine-instances](../results/records/becoming-spine-instances.md)）。

L 是实质承诺：

- 有一好一坏两个结果的回应，在两个方向上都不可比；
- 传递性需要一个可行的中间回应。

**C 的排序取决于它所比较的读法。** 以两次继续为配置、以读法所记入的事件为实现的主张，C 就是这一框架上的比较（[Becoming.Ranking](../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Ranking.lean)，[ranking-under-readings](../results/records/ranking-under-readings.md)）：

- 没有某个形成的继续扩展有它的继续，仅当读法扣下该形成的每个事件；
- 整段读法下，C 把没有过度汲取者的继续排得更高，也把共享排在以消耗取胜之上；
- 逐步读法下，过度汲取者有一个使每个所需仍被满足的事件时，这一事件被记入，C 不再决定它的在场与不在场（恶性增殖与以消耗取胜都是实例），但仍把共享排在以消耗取胜之上；没有这样的事件时（例如第一步就越过支持），逐步读法同样把不在场排得更高（`Immediate`）；
- 在二元定律族中，两种读法下 C 都把在阈值之前停止的继续排在过度汲取之上（`restraint_ranks`、`malignant_restraint`）：那里逐步读法失去与不在场的比较，不失去与节制的比较；有第三个形成共用条件时，与节制的比较也可以失去（`ThirdParty`）。

所以若要由 C 得出“没有恶性增殖更好”，C 所比较的读法须扣下损失之前的事件，或者在 C 之外加更强的比较。G0 与 C 是否共用一种读法，属于 Ren 对生生读法的选择（§6.3）。

**What C ranks depends on the reading it compares.** Under the whole-run reading C ranks the continuation without an overdrawing formation higher, and sharing above winning by consumption. Under the stepwise reading it still ranks sharing above winning, but no longer decides between an overdrawing formation and its absence when the formation has an event whose step leaves every need met, because that event is credited; without such an event the stepwise reading too ranks the absence higher. In the two-part family both readings rank restraint before the threshold above overdraw, so there the stepwise reading loses the comparison with absence; with a third formation sharing the condition the restraint comparison can be lost too.

**L was a hidden premise exposed by integration.** Under the conservative L, the comparison, reason, survival and continual-improvement results hold on every frame. The functional situation is exactly the deterministic case. L is substantive.

### 6.6 不做什么 / What it does not do

不证明 S0、N、A、C、L 或 J，不约束拒绝它们的立场，也不处理使新生命存在的价值。规范根据、认识、动机、遵循与实际保存是不同的主张；方向、持续能力、每步单调增长与标量最大化也是不同的主张。

It proves none of S0, N, A, C, L or J, binds no rejecting position, and does not treat the value of bringing new lives into existence.

## 7. AI 对齐 / AI alignment

**主张**（[对齐方向](ALIGNMENT-DIRECTION.md)，[alignment-direction-g0-j](../results/records/alignment-direction-g0-j.md)）：

**使 AI 的形成、学习、行动和更新，支持整体中实际的生及其继续生成，使生命、心智、关系、生活方式与组织能够丰富地共同发展；以真实损失、基本生活条件、有界责任和正当参与约束取舍，使这种发展能够被认识、质疑和纠正。**

**We propose aligning AI formation, learning, action and revision with actual living and further generation within the whole: enabling richer co-development of life, minds, relationships, ways of living and organization, while governing tradeoffs through real losses, basic living conditions, bounded responsibility and legitimate participation, with effective opportunities to understand, challenge and correct that development.**

**同一根据适用于每一层选择。** AI 的能力经由计算、能源、劳动、知识、训练、使用与制度形成。目的、评价与选择规则本身也改变生及其继续条件，因此进入同一 G0/J 评价，不必为每一层选择另找一个起点（[变化中的生成性对齐](ALIGNMENT-THROUGH-CHANGE.md)）。

- **能力不等于权限。** 能力不授予治理权；跨智能的适用，意味着相关处境相似时理由相似，不预测相同的心理。
- **向 AI 的理由。** `universal_reason` 向每个处境中的智能提出理由，其中包括 AI。理解了理由，不等于必定服从理由。

**纠正须是可执行的序列。** 接受纠正的倾向，不等于纠正能被送达和完成。已检查的条件包括：

- 恢复期间预留关机的余量（[reserved-shutdown-during-recovery](../results/records/reserved-shutdown-during-recovery.md)）；
- 被中断变化后的证据恢复与纠正通达的界（[recoverable-mediated-change](../results/records/recoverable-mediated-change.md)）；
- 保证到达的判据（[assured-route-criterion](../results/records/assured-route-criterion.md)）；
- 风险界与实际结果的区别（[risk-certificate-outcome-distinction](../results/records/risk-certificate-outcome-distinction.md)）。

**One ground reaches actions, ends and selectors.** Capability grants no governing authority, and correction must be an executable sequence. Reasons are addressed to every situated intelligence, AI included; understanding a reason is not complying with it.

## 8. 开放纲领 / Open programme

| 目标 / Target | 现状 / Status | 下一步推论 / Next inference |
|---|---|---|
| Becoming 整体的演绎必然性，不加实质公理（[theory-of-becoming-foundation](../results/records/theory-of-becoming-foundation.md)） | 开放；有限相容性、作用损失与依存变化方式的相互约束已在各自范围内建立 | 确立整体中的各规定是同一展开中内在相关的环节，而不只是收集实例（[根基 §9](BECOMING-FOUNDATION.md#9-the-content-of-the-whole-deduction)） |
| 更强的普遍实践根据（[universal-practical-warrant](../results/records/universal-practical-warrant.md)） | 开放；在公开前提下已有普遍理由 | 不经外给目的而建立理由的根据 |
| 核心作为智慧之根（[wisdom-root](../results/records/wisdom-root.md)） | 开放 | 说明智慧的实际形成 |
| 科学探究的必要关系根基（[scientific-inquiry-foundation](../results/records/scientific-inquiry-foundation.md)） | 开放 | 由独立陈述的成就建立核心的不可或缺性 |
| 动态依存 | 已定义并检查（[becoming-dependence-dynamics](../results/records/becoming-dependence-dynamics.md)）：依存跨步形成、维持、断裂与消解；定理联系起来的损失的三种结局，表示内的约束；替代在支持门控定律中保持整段分类（[substitution-preserves-consumption](../results/records/substitution-preserves-consumption.md)） | 放宽 `Dependent`（缓冲、储备、滞后）；形成的个体化 |
| 读法 | 已定义并比较，读法选择开放：整段、逐步（不侵蚀）、周期与关系层（[becoming-stepwise-reading](../results/records/becoming-stepwise-reading.md)、[becoming-return-grades](../results/records/becoming-return-grades.md)）；有限前缀不决定分类（[becoming-finite-horizon](../results/records/becoming-finite-horizon.md)） | Ren 选择生生的读法或其组合，以及 G0 与 C 是否共用一种读法（C 的排序随读法而变，[ranking-under-readings](../results/records/ranking-under-readings.md)）；条件的对应纪律已给出一条（[condition-correspondence-discipline](../results/records/condition-correspondence-discipline.md)），其时间次序、对效果的敏感与对整段读法的陈述开放；不依赖运行的读法；带数量与更新率的网；继续生成的成分 |
| 继续生成 | 陈述在整体的继续上：在有限条件、生起消耗有限家族、更新由形成造成的前提下，不息的生成需要更新复现，更新不蕴含生成；在平衡的流中，取用者不息地生起需要补充复现（[unceasing-generation-needs-renewal](../results/records/unceasing-generation-needs-renewal.md)）；读作取用者数目的“更多”需要补充与补充者没有最终的界，在普查与 Taking 之下严格蕴含不息（[more-needs-renewers](../results/records/more-needs-renewers.md)） | 第二个“生”的范围与以消耗为条件的生起是否为生成（Ren）；可能性、多样性与复杂性的上升；每次给予都耗散的流；生成成分进入 `living` 的读法；与 `universal_reason` 的新的活的内容接通 |
| 共同活动中的归属 | 相对于动作的 but-for 差别制造在多重决定下与关系参与分离；整段与步层面的检验分开（[joint-difference-making](../results/records/joint-difference-making.md)） | 更精细的归属（如 NESS、实际因果）作为另一读法；不推出责任 |
| 独立反审 | 关系读法与 P3b–P6 已经独立审查（[审查](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING-REVIEW.md)）：数学接受，哲学根据未确立，二十项更正已处理。回程、视界、共同活动与替代（P7）经[第二次审查](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-P7-REVIEW.md)：数学接受，侵蚀与 but-for 的定义已修正，十五项更正已处理。C 在各读法下的排序（P8）、条件的对应纪律（P9）与 P7b 的更正经[第三次审查](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-P8-P9-P7B-REVIEW.md)：数学接受，侵蚀改为比较那一步的所需，but-for 要求动作可取，排序、替代与交互的说法收窄，十二项更正已处理。P9b、不息（P10）与更多（P11）经[第四次审查](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-P9B-P10-P11-REVIEW.md)：数学接受，侵蚀改为最小形式，消耗前提、严格性见证、耗散、层级与补充者的说法收窄，十四项更正已处理。A 的外在论辩护、N 的哲学根据未经独立审查 | 进行这些审查 |
| 经验对应 | 共同条件、各机制的实际实现 | 识别与可区分的检验 |
| 更强的方向假说 | 现实一般地发展出更共同、更有回应的更新：开放 | 不作为前提使用 |

## 9. 形式脊柱 / The formal spine

全部新的形式结果都陈述在同一条脊柱上。脊柱不能表达某个结果时，扩展脊柱，而不是另建模型。既有的通用伦理模块不复制、不改写：脊柱给出它们接口的实例（[实例分类表](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-INSTANCE-CLASSIFICATION.md)）。

All new formal results are stated on one spine; when it cannot express a result, the spine is extended rather than another model built. Existing generic modules are instantiated, not copied.

**核心纯净 / A pure core.** 按 [Ren 的要求](../../../sources/15-codex-theory-conversations/2026-10-09-pure-core.md)，核心（L0 及其两个基础模块，加 L1–L4）不导入核心以外的任何模块，其中每条声明的公理报告为空，并且只用 Lean 的内置前导即可编译；检查器每次都检查这三点。G0、C、D 与确保的正面根据在核心中陈述一次；桥接层证明既有模块的定义就是这些，依存方向从外围指向核心。外围可用任何合适的工具（Mathlib、Python）。核心是 Lean 包 `Becoming`：`import Becoming` 导入全部四层，桥接 `Becoming.Bridge` 在包内但不属核心（[包说明](../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/README.md)）。

The core (L0 with its two foundation modules, and L1–L4) imports nothing outside itself; every declaration in it has an empty axiom report, and it compiles from Lean's prelude alone. The checker verifies all three on every run. The bridge proves that existing modules' definitions are the core's; dependence runs from the periphery, which may use any suitable tool, to the core. The core is the Lean package `Becoming`: `import Becoming` brings in all four layers, and `Becoming.Bridge` sits in the package but outside the core.

| 层 / Layer | 模块 | 内容 | 定理 |
|---|---|---|---:|
| L0 | `GenerativeCore` | 过程、轨迹及其组合、传递 | 继承 |
| L1 | [Becoming.Frame](../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Frame.lean) | 框架、运行、可达、不变量、新实现 | 11 |
| L2 | [Becoming.Inquiry](../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Inquiry.lean) | 所见范围；可靠策略确保其目标；判断即一步探究 | 6 |
| L3 | [Becoming.Renewal](../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Renewal.lean) | 运行上的更新／消耗；一条下降原则 | 6 |
| L3 | [Becoming.Dependence](../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Dependence.lean) | 依存的形成、维持、断裂与消解；损失的三种结局；逐步的更新、断裂与侵蚀 | 53 |
| L3 | [Becoming.Return](../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Return.lean) | 回程等级；消耗恰是不再回程；周期层面的读法 | 29 |
| L3 | [Becoming.Horizon](../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Horizon.lean) | 有限前缀不决定分类，有反馈时也如此；按数量的读法 | 14 |
| L3 | [Becoming.Joint](../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Joint.lean) | 相对于动作的 but-for 差别制造；多重决定；动作决定步骤时的二分；整段与步层面的检验 | 21 |
| L3 | [Becoming.Substitution](../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Substitution.lean) | 支持门控定律中的替代：整段读法下保持消耗，逐步读法在失去支持之前记入 | 7 |
| L3 | [Becoming.Generation](../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Generation.lean) | 生起与不息；消耗前提；不息的生成需要更新复现，更新不蕴含生成；替代推迟终结；耗散与封闭循环 | 30 |
| L3 | [Becoming.Flow](../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Flow.lean) | 消耗与补充的平衡；平衡的流中上升由补充者造成；取用者不息地生起需要补充复现；不止地更多需要没有最终界的补充与补充者；不息的生成尚不是更多 | 58 |
| L3 | [Becoming.Population](../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Population.lean) | 活跃形成的普查；在普查与 Taking 之下更多蕴含不息；没有普查或 Taking 时的反例 | 20 |
| L4 | [Becoming.Metaethics](../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Metaethics.lean) | 前提卡、G0 刻画、极小性、普遍理由；整段、逐步与关系层的读法 | 35 |
| L4 | [Becoming.Ranking](../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Ranking.lean) | C 在整段与逐步读法下的排序；二元定律族中节制排在过度汲取之上 | 27 |
| L4 | [Becoming.Correspondence](../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Correspondence.lean) | 条件的对应纪律：交互；惰性条件不连通；连通由活的使用造成 | 25 |
| 桥接 / Bridge | [Becoming.Bridge](../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Bridge.lean) | 既有接口是脊柱的实例；核心定义即既有定义；J1/J2 的 `BetterAt`；比较经 L 推广；整段读法即既有的关系清单 | 34 |

[合并检查器](../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/check_becoming.py)与[回执](../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/becoming-verification.json)覆盖 376 项定理、688 项声明审计，公理报告全部为空；核心闭包共 18 个模块；15 个继承模块的当前字节须与已通过的回执一致。依赖 Mathlib 的叶子经外围桥接 [CorrectionInquiry](../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/CorrectionInquiry.lean) 连到核心：它用 Lean 4.30.0-rc2 与 Mathlib 检查，核心模块在那里同样编译通过，桥接的 7 项定理公理报告为空。方向与计划见[统一计划](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-UNIFICATION-PLAN.md)。

The consolidated checker and receipt cover 376 theorems and 688 declaration audits, all with empty axiom reports; the core closure has 18 modules. The current bytes of 15 inherited modules must match passed receipts. Mathlib leaves connect through the peripheral bridge CorrectionInquiry, checked with Lean 4.30.0-rc2 and Mathlib; the core compiles there too, and the bridge's 7 theorems have empty axiom reports.

## 10. 术语表 / Glossary

| 中文 | English | 含义 / Meaning | Lean |
|---|---|---|---|
| 生成／变化 | Becoming | 关系的形成、维持、转化、退化与消解构成的整体展开 | — |
| 生生 | 生生 (generativity) | 整体中的生及其继续生成；伦理方向的对象 | `living` |
| 过程 | process | 声明可容许的变化 | `Generative.Process` |
| 框架 | frame | 过程加上每个配置实现的主张 | `Frame` |
| 运行 | run | 无穷的实际执行 | `Run` |
| 可达 | reach | 有限的可容许路径 | `Reach` |
| 不变量 | invariant | 每步保持的性质 | `Invariant` |
| 新实现 | novel realization | 某种读法下此前未实现的主张 | `Novel` |
| 所见范围 | scope | 策略实际执行可达的配置 | `Scope` |
| 判断过程 | judgment process | 在被判断的配置上取一个可容许的回应然后结束；其共同回应即稳健判断 | `judgeProcess` |
| 条件 | conditions | 条件水平、活跃、依存与汲取的可观测量 | `Conditions` |
| 更新／消耗 | renewing / consuming | 对所参与条件的关系分类 | `RenewingIn`、`ConsumingIn` |
| 依存网 | web of dependence | 依存、所需水平与汲取随步变化的展开 | `Web` |
| 维持／断裂 | kept / broken | 跨一步，被满足的依存仍被满足／不再被满足 | `Kept`、`Broken` |
| 形成／消解（依存） | forms / dissolves | 依存跨一步出现／消失 | `Forms`、`Dissolves` |
| 步内更新 | within renewal at a step | 事件所在之步维持其所参与条件上的每个依存；逐步的更新分类 | `RenewingAt` |
| 断裂（事件） | breaking | 在断裂某个依存之步汲取该条件 | `BreakingOn`、`BreakingAt` |
| 生起 | arising | 形成跨某步由不活跃变为活跃 | `Arises` |
| 不息 | unceasing generation | 某个形成在任意晚的步生起；同一形成可以再生起 | `Unceasing` |
| 消耗（有限家族） | depletion | 在事件的每个家族都不上升之步，其中某个条件下降；只说家族中有条件变化 | `Depletes` |
| 耗散 | dissipation | 一个量从不上升，而每次生起都使它下降 | `dissipation_ceases` |
| 流 | flow | 每步参与的形成从条件取用与给予的量；平衡时水平的变化恰是二者之差 | `Flow`、`Balances` |
| 取用／补充 | uptake / replenishment | 一步中参与的形成从家族取用的总量／给予家族的总量；二者与水平的变化相平衡 | `uptake`、`replenishment` |
| 取用者／补充者 | takers / renewers | 一步中从家族取用／给予家族的形成 | `takers`、`renewers` |
| 取用而生起 | arising taking | 形成在其第一个活跃步从家族取用 | `ArisesTaking` |
| 普查 | census | 每步活跃的形成列为不重复的有限表 | `Census` |
| 取用即汲取 | taking | 只有活跃的形成取用，且只从它汲取的条件取用 | `Taking` |
| 不止地更多 | more without end | 对每个数，从某步起至少有那么多形成从有限的条件家族取用 | `More` |
| 侵蚀 | undermining | 在某步汲取某条件，而该步之后条件既低于一个依存现在的所需，也低于该依存在不间断成立期间的某步曾被满足的所需；逐步读法的 living 是活跃且不侵蚀 | `MetAbove`、`UnderminingOn`、`UnderminingAt` |
| 回程 | return | 某步成立的依存在以后某步（或 `p` 步之内）再被满足 | `Returns`、`ReturnsWithin`、`RenewedWithin` |
| 视界 | horizon | 有限的前缀；两次运行在其前相同 | `Run.AgreeUpTo` |
| 差别制造 | making a difference | 扣除一方的部分后，以同一动作的每一步都维持依存（且该动作可取） | `MakesDifference`、`Overdetermined` |
| 交互 | interaction | 一方汲取某条件、另一方以正水平依存于它，在任何步上；对应纪律下的 related | `Interacts`、`Web.interaction` |
| 承担 | bearing | 以正水平依存于某条件，条件能使之落空 | `Bearing` |
| 惰性条件 | idle condition | 没有活动汲取它，或没有依存能落空的条件 | `Idle` |
| 形成事件 | formation event | （形成，步）；整段与逐步读法的主张 | `F × Nat` |
| 关系（读法层） | relation | （形成，条件，步）；关系层读法的主张 | `Web.relations` |
| 评价 | valuation | 活、关系、区域、意义 | `Valuation` |
| 自身区域 | own region | 已形成关系的区域，不是所有者 | `own` |
| 意义 | significance | 立场下的正面意义 | `sig` |
| 种子 | seed | 某个立场下某个活的主张有意义 | `Seed` |
| 边界中立 | boundary neutrality | 规则不被任何已形成的边界限制 | `Neutral`（对比 `Within`） |
| 连通 | connected | 活的主张经已形成的关系相连 | `Connected` |
| 支持理由 | contributory reason | 支持某回应的理由；不是义务或排序 | `Reason` |
| 提升规则 | lifting rule | 把结果比较提升到多结果回应 | `LiftBetter` |

## 11. 既有章节的位置 / Where the earlier chapters stand

`chapters/` 中的章节是论证、证据与批评的记录，按原范围保留，不因本章而改写。本章取代的只是它们作为入口的作用。[完整阅读目录](../results/README.md)为每章列出论证、意义、范围与下一问题。

The chapters remain records of argument, evidence and criticism at their original scope; this chapter replaces only their role as entry points. The [reading catalogue](../results/README.md) lists every chapter with its argument, significance, scope and next question.

| 类别 / Kind | 章节 / Chapters | 现在的作用 / Current role |
|---|---|---|
| 现行方法 / Method | [非二元方法](NONDUAL-METHOD.md) | 一切根基工作前必读 |
| 现行研究 / Active studies | [根基范围](BECOMING-FOUNDATION.md)、[关系怎样变化](THEORY-OF-BECOMING.md)、[G0 的根据](G0-WARRANT.md)、[演化之论](THE-THEORY-OF-EVOLUTION.md)、[对齐方向](ALIGNMENT-DIRECTION.md)、[知识](KNOWLEDGE.md) | 各自目标下的当前论证；本章引用其结论 |
| 历史综合 / Historical syntheses | [Start here](START-HERE.md)、[统一理论](THEORY.md)、[生成根据](GENERATIVE-GROUNDING.md)、[共同前提](FOUNDATION-PREMISES.md)、[综合记录](SYNTHESIS-RECORD.md)、[完成计划](COMPLETION-PLAN.md) | 历史证据；作为入口的作用已由本章取代 |
| 各部分的证据 / Evidence by part | 形成与发展（[生成发展](GENERATIVE-DEVELOPMENT.md)、[形成](FORMATION.md)、[共同形成](JOINT-FORMATION.md)）；评价（[评价接续](EVALUATIVE-UPTAKE.md)、[统一伦理根据](UNIFIED-ETHICAL-GROUNDING.md)、[实践判断](PRACTICAL-JUDGMENT.md)）；集体（[市场](MARKETS-AND-GENERATIVE-REGIMES.md)、[多元系统](PLURAL-SYSTEMS-AND-CORRECTION.md)）；形式（[形式核心](FORMAL-CORE.md)、[Lean 核心](GENERATIVE-CORE-LEAN.md)）；其余见目录 | 历史证据，按原范围保留 |
| 登记 / Registers | [成果登记表](../results/RESULT-REGISTER.md)、[细项主张](CLAIMS.md) | 自动生成；以记录为准 |
