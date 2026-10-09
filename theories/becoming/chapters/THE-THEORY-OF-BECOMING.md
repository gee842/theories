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

每个前提都具名、可见。在 Lean 中，它们是定义或假设，不是公理；脊柱的每条源声明的公理报告都为空。

Every premise is named and visible. In Lean they are definitions or hypotheses, never axioms; every source declaration of the spine has an empty axiom report.

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
- **不加前提的规律。** 以下对每个展开成立，不加任何关于它的前提（[Becoming.Change](../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Change.lean)，[coming-and-ceasing-keep-pace](../results/records/coming-and-ceasing-keep-pace.md)）。一个规定跨一步开始成立或不再成立；形成的生起与止息、依存的形成与消解、条件开始与不再作为条件而在，是这同一种变化分别读于活动、依存与水平。任一段步上，一个量在终点加上其间的下降，等于在起点加上其间的上升。量不低于零，所以有限家族中下降复现就需要上升复现：每个展开中，有限多个条件持续下降就持续上升；量有界时，上升复现也需要下降复现。于是在有限家族中开始成立与不再成立同步：任一段步上，终点成立的成员连同其间不再成立的，恰是起点成立的成员连同其间开始成立的，两者之差不超过成员数，一方复现恰当另一方复现。形成有限多时，生成不息恰当某个形成在任意晚的步止息；条件开始作为条件而在复现，恰当不再作为条件而在复现，这不需要任何前提。有限性起作用：无尽的新可以只生起而不止息（`Dawn`），无尽的初始可以只止息而不生起（`Dusk`）。下面各条都写明它们加的前提，前提划出整个空间的一部分。表示的方法承诺另行公开：离散的步、自然数的量、计数时的可判定性。
- **依存的变化。** 依存本身属于展开：一个形成依存于哪些条件、所需多少，可以跨步形成、维持、断裂与消解，变化总发生在某一步上（[Becoming.Dependence](../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Dependence.lean)）。在形成只在有支持处活跃的前提（`Dependent`，排除缓冲与滞后）下，定理把损失之后的三种结局联系起来，它们既不穷尽也不互斥：以不弱于先前的依存继续，意味着条件已恢复；无回程的损失之后仍活跃，意味着依存已转化；依存不变则终止。同一过程、同一配置下，在同一步断裂同一依存（按步首约定读）之后，三种结局都可实现：断裂的读法不决定后继配置，构成断裂的那一步选定结局（[becoming-dependence-dynamics](../results/records/becoming-dependence-dynamics.md)）。`Dependent` 恰是零储备：储备在形成不被支持时不上升、在其间活跃时下降，有储备时形成越过支持至多再活跃其储备那么多次，损失与共灭之后的终结推迟而不逃脱；储备可以就是所持条件的水平，同一展开也可以读作依存转化到所持的条件上（[Becoming.Reserve](../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Reserve.lean)，[reserve-defers-ending](../results/records/reserve-defers-ending.md)）。这是表示内的定义与约束，不是第一句话的证明。
- **跨步的同一。** 一步的哪个形成延续前一步的哪个，由表示的命名规定，每一步的关系并不确定它（[Becoming.Identity](../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Identity.lean)，[identity-across-steps](../results/records/identity-across-steps.md)）。改名保持由关系定义的读法（检查了五种）：标签不承载任何东西，名字跨步的模式承载同一。每一步的关系、每个条件的类、取用者的数目与“更多”不依赖跨步的同一；形成在整段上的类、依存的任期与侵蚀、转化与“一个终结而另一个形成”之分、生起与不息依赖它。只改动谁延续谁，这些就全部改变（`Turnover`）；单由命名造成的生起可以满足下文“继续生成”的全部前提（`TideFlip`）。以旧命名为参照保持跨步持续活动与持续依存的名字，改认不制造生起，也不去掉侵蚀；新命名仍可把终结者与在该步或其后开始者接起来，即接续：谱系的成员分开命名时不息地生起，合为一个时没有生起（`Lineage`）；继承者接续长者时，长者失去之后的汲取每一步都侵蚀（`Succession`）。双向保持连续时，生起与侵蚀恰被保持，单步的接续被排除（`no_join`），但跨过休眠的接续仍改变形成的类（`Dormancy`）。谱系与成员是同一展开的两个层次；部分与整体的一种关系由整体陈述：整体恰在某个部分活跃时活跃，这是活动的重合，不是构成，谱系是其成员的整体（[Becoming.Wholes](../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Wholes.lean)，[whole-persists-through-generation](../results/records/whole-persists-through-generation.md)）。从某步起每步活跃的整体，若部分短暂（从不在相隔 d 步的两步都活跃），或部分终结且同时活跃的部分有限（活动都终结且活跃的部分可有限列出），部分就不断生起：整体经由部分的生成而持续；部分短暂时这可以是同样的部分反复生起（`Layered`），部分终结时是不断新的部分（`needs_new`），都不是数目增长；有永不终结的部分或无穷的同时储备时则不然（`Immortal`、`Countless`），部分不息地生起也不使整体持续（`Gaps`）。接续怎样读、“生生不息”读到哪个层次，属于 Ren。在普查、`present` 不重复与 Taking 之下，由“更多”迫使的不息在每种一对一的命名下成立（`More.unceasing_reidentified`），在每种没有形成延续为两个的延续关系下更多也迫使生起（`More.unceasingFrom`，合并允许）。没有分裂是充分条件，不是必要条件：一次分裂不必使生起失效（`Fork`），把新形成读作萌出时结论不成立（`Budding`）；没有普查时，没有分裂也不够（`Dormant`）。
- **一个关系项的两种角色。** 形成与条件是同一个关系项的两种角色，不是两类存在（[Becoming.Roles](../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Roles.lean)，[life-as-condition-of-life](../results/records/life-as-condition-of-life.md)）。两类的表示嵌入没有形成作为条件的一类读法：这样读，列出的读法与估值的连通都不变，其中曾活跃的形成既不体现（恰在活跃时作为条件而在）也不承担自身。一类读法另需一个对应：哪个条件就是哪个形成。它由共同的索引给出，是表示的前提，两类读法检查不到它（`relabel`）；体现与承担自身是在这一对应下的读法。在活动需要支持（`Dependent`）之下，依存于体现关系项的形成只在它活跃时活跃，活动沿依存链传递，一个关系项的终结终结每个依存链到达它的形成（`coextinct`）。体现的关系项的生起就是它作为条件的水平的上升，所以生成本身就是补充（[generation-is-replenishment](../results/records/generation-is-replenishment.md)）。

**Formation, persistence, transformation, degeneration and dissolution are relational changes along runs, not five stages.** One activity can make a continuation actually possible while destroying another condition, and a retained form need not retain its efficacy. The results above establish, at their scopes:

- laws with no premise, holding of every unfolding: arising and ceasing, forming and dissolving, coming to stand and ceasing to stand are one change read of activity, dependence and standing; over any stretch an amount at the end with its falls is the amount at the start with its rises; in a finite family recurring falls need recurring rises, and coming to be and ceasing to be keep pace, so that with finitely many formations generation is unceasing exactly when ceasing is, while ever new or endlessly many formations escape this (`Dawn`, `Dusk`); every law below names the premise that picks out its part;
- endpoint loss and return;
- the difference between current capacity and eventual reachability;
- the exact condition under which pooling processes invents no history;
- joint change with unchanged local states;
- local loss recoverable within a retained joint relation;
- dependence that forms, holds, breaks and dissolves at steps, and three outcomes of a loss (ending, transformation, restoration), connected by theorems where a formation is active only where supported; the reading of the break does not fix which follows; that premise is the zero reserve, and with a reserve, which can be the standing of a held condition, these endings are deferred, not escaped;
- identity across steps: labels carry nothing, while the pattern of names across steps carries identity; each step's relations, each condition's class and more without end do not depend on who continues whom, while a formation's class, tenure, undermining, transformation and arising do; continuity read one way leaves succession open, read both ways it still leaves succession across dormancy, and the reading of succession is Ren's; under a census, with each formation taking part listed once and only active formations taking, more forces arising under every continuation without splits, a sufficient condition and not a necessary one. A whole is active exactly while some part is, a coincidence of activity rather than constitution; a persisting whole of brief parts, or of parts that end with finitely many active at once, persists only through their generation: the same parts arising again, or ever new parts, though not more of them.
- formations and conditions are two roles of one relatum: the two-kind representation embeds in the one-kind reading in which no formation is a condition and keeps every listed reading, while which condition is which relatum is supplied by the shared index; where a relatum stands as a condition exactly while it is active, a formation depending on it lives only while it does, and its ending ends every formation whose chain of dependence reaches it; the arising of such a relatum is its coming to stand, so generation is itself replenishment, a requirement that follows standing, not activity.

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

**继续生成。** 以上读法读出的都是“不损”。作者把生生的第二个“生”的一种读法陈述为生起：一个形成跨某步生起，当它此前不活跃、此后活跃；生成不息，当某个形成在任意晚的步生起，同一形成可以再生起（[Becoming.Generation](../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Generation.lean)，[unceasing-generation-needs-renewal](../results/records/unceasing-generation-needs-renewal.md)）。一个事件消耗一个有限的条件家族，当在它的每个家族都不上升之步，其中某个条件下降；这只说事件的每一步家族中有条件变化，不涉及事件与那个条件的关系（`depletes_iff`、`Tide.unrelated_depletion`）。若生起消耗家族，不息的生成使其中某个条件在任意晚的步净上升；若每次上升都由某个形成的更新造成，更新的活动就在任意晚的步复现。平衡的流给出不需要净上升的形式：在平衡的流中，任意晚的步上有正的取用，就需要任意晚的步上有补充（`uptake_needs_replenishment`），它看得见与汲取同步的补充；取用的形成不息地生起是其一种情形，补充者于是在任意晚的步出现（`replenishment_recurs`），恒定的取用者群体是另一种（`Steady`）。生起在这一形式中只经由它带来的取用起作用。月亮更新的潮水在任意晚的步上升而没有任何生起，所以在这些前提下，不息的生成严格强于复现的更新（`Tide.renewal_without_arising`）。以不被更新的条件为条件的生起停止；在有限个不被更新的条件之间替代，推迟终结而不逃脱终结。一个量从不上升而每次生起都使它下降（耗散）时，生成不是不息的（`dissipation_ceases`）；没有耗散，总量不变的封闭循环可以维持不息的生成（`Recycle.closed_unceasing`）。作者由此论证：在耗散之下，任何有限部分都不能独自不息；对流中的取用，证明的是它的字面形式：取用复现的有限家族在任意晚的步不封闭，家族被围住时须从其外汲入（见下文“更多”）；耗散空成立时，有限部分可以独自承担，而开放由与它无关的交换满足（`SprayHanding`）。这里只读出 Ren 原话“不断创造更多生”中的“不断…生”；第二个“生”的范围留给 Ren。

**Continued generation.** As the author's reading of the second 生, a formation arises across a step when it is inactive before and active after it; generation is unceasing when some formation arises at arbitrarily late steps. An event depletes a finite family when at each of its steps at which none of them rises one of them falls, which says only that some condition of the family changes. When arising depletes the family, unceasing generation makes renewal recur; in balanced flows, uptake at arbitrarily late steps needs replenishment at arbitrarily late steps, which sees replenishment concurrent with drawing; takers arising unceasingly are one case and a constant population of takers another, so arising works there only through the uptake it brings. A tide the moon renews rises with nothing arising, so under these premises unceasing generation is strictly stronger than recurring renewal. Arising on a consumed condition ceases, and substitution among unrenewed conditions defers the end without escaping it. Under dissipation generation is not unceasing; without it, a closed cycle can be. Only the “unceasing” of Ren's “unceasingly creating more 生” is stated here; the scope of the second 生 is Ren's.

**更多。** 把条件读作数量：每步参与的形成从条件取用多少、给予多少（[Becoming.Flow](../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Flow.lean)、[Becoming.Population](../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Population.lean)，[more-needs-renewers](../results/records/more-needs-renewers.md)）。流平衡时，条件水平的每次变化恰是取用与给予之差；一步或一段步上，家族的总水平加上取用，等于之前的总水平加上补充（消耗与补充的平衡）。每次上升于是都由某个活跃的补充者造成，上面“每次上升都由形成的更新造成”从前提变为定理。“更多”读作（作者的读法）：对每个数，从某步起至少有那么多形成从一个有限的条件家族取用。量是自然数，每个取用者每步至少取用一个单位，所以这样的生成需要家族所得的补充没有最终的界；每个形成每步的给予有上限时，补充者也没有最终的界，在平均的意义上越来越多，却可以在无穷多步上为零（`Pulse.pulsed`）。在活跃形成的普查之下，流的 `present` 每步每个形成只列一次，只有活跃的形成取用时，不止地更多蕴含不息的生成（`More.unceasing`）；花园与循环满足全部这些前提（`Garden.counted`、`Cycle.counted`）；不息地反复生起的开花满足这些前提而不更多，所以蕴含是严格的；没有普查、`present` 有重复、或取用者从不活跃时，不止地更多可以没有任何生起（`Dormant`、`Repeated`、`Inactive`）。所需的补充于是构成严格的层级：复现的取用需要补充在任意晚的步出现，不止地更多需要补充没有最终的界。补充者可以就是取用者自身（`Cycle.closed_more`）。在耗散之下（每一步，每个在该步封闭的不重复有限家族上，参与的形成给予它的不多于从中所取，取用时更少），取用在其上复现的有限家族，连同包含它的每个有限家族，在任意晚的步都与其外交换，这一交换可以与家族无关；家族被围住（每步的交换落在包含它的有限个条件之内）时，它汲入：在任意晚的步有形成给予它而从其外取用（`taking_draws_in`）；条件总共有限时，取用不再复现（[Becoming.Dissipation](../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Dissipation.lean)，[no-finite-part-bears-taking](../results/records/no-finite-part-bears-taking.md)）。在平衡的流中，每次下降都被取用；被耗散的一步上，家族成员的下降至少等于其上升，每个取用的形成再多一。所以一个成员上升（包括体现的生起），同一步上另一个成员下降，两者是同一次交换的两面；不重复的家族中有上升而没有下降，就表明家族在该步不封闭；没有耗散时不然（`Brood.rise_without_fall`）。上面作为前提的消耗由此推出（[rising-and-falling-in-one-exchange](../results/records/rising-and-falling-in-one-exchange.md)）。下降不是止息，也不是侵蚀。耗散只约束有封闭的有限家族的步：在这样的步上，给予须以取用为条件（`giving_needs_uptake`）；没有封闭的步时它是空的，补充者可以什么都不取而给予（`Spray`）。作者把它读作“生生”的一种结构：更多的取用需要没有最终界的补充，由展开之内的形成给出；在耗散之下，复现的取用，无论来自不止的更多、生成还是维持，都由越出每个有限部分的展开承担，维持一个取用者已经如此（`Lone`）。可能性、多样性与复杂性的上升是“更多”的另外读法，这里不陈述。

**More.** Read as amounts, conditions are taken and given by the formations taking part in each step, and depletion balances replenishment. In a balanced flow every rise is made by an active renewer, so the premise above becomes a theorem. Generation more without end, with ever more formations taking from a finite family from some step on (the author's reading), needs replenishment with no eventual bound, since each taker takes at least one unit; when each formation gives at most a fixed amount, renewers have no eventual bound and grow in an averaged sense, though they can be absent at infinitely many steps. Under a census of active formations, with each formation listed once in the flow's present and only active formations taking, more without end implies unceasing generation, strictly, and the garden and the cycle meet every premise; without the census, with repetition in present, or with inactive takers it does not. The replenishment needed thus forms a strict hierarchy. The renewers can be the takers themselves. Dissipation binds at steps where some finite family is closed, and there giving needs uptake; under it, a finite family on which taking recurs, whether from more, generation or maintenance, and every finite family containing it, is open at arbitrarily late steps, though the opening exchange may be unrelated to it; enclosed around, it draws in, some formation giving to it and taking from beyond it at arbitrarily late steps; and with finitely many conditions in all, taking does not recur. In a balanced flow every fall is taken from. Across a step dissipated on, a family's members fall by at least as much as they rise, so a member rising, as an embodied relatum arising, comes with another member falling in the same exchange; a rise with nothing falling shows a family without repetition open across that step; and the depletion premise above follows. A fall is a lowering, neither a ceasing nor an undermining, and without dissipation a rise need not be accompanied. Diversity, complexity and possibility are not stated.

**一个关系项的两种角色，经由给予的生起。** 以一类关系项读（[Becoming.Roles](../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Roles.lean)，[life-as-condition-of-life](../results/records/life-as-condition-of-life.md)），一个形成可以是其他形成与自身的条件；哪个条件就是哪个形成，由表示的共同索引给出（`relabel`）。在平衡且只有活跃形成给予的流中，体现的关系项只经由另一个活跃形成的给予而生起（`Embodied.arises_given`）；给予它的形成不必体现，可以是一个不依存于任何东西的太阳（`SunSeed`）。在只有体现的关系项给予这一表示前提下，给予它的关系项也体现（`arises_from_embodied`），它仍可以是一个不依存于任何东西的太阳（`EmbodiedSun`）。在把体现的关系项读作“生”这一属于 Ren 的读法下，作者把这读作原话中两个“生”之间关系的一种形式内容（AI 论证），不替代 Ren 的原话；一代代形成可以不止地生起，每一代由前一代给予（`Brood`）。体现的关系项在生起时开始作为条件而在，至少被给予它的新水平，所以生成本身就是补充：体现的成员在任意晚的步生起时，家族的补充复现，不论取用什么（[generation-is-replenishment](../results/records/generation-is-replenishment.md)）。这一要求跟着水平的上升走，不跟着活动走：平衡的流中任何上升都被给予（`Balances.rise_given`），开始作为条件而在是从零的上升（`Web.ComesToStand`），一个条件也可以只是不断上升（`Growing`）；种子可以在休眠时被给予它的水平，此后生起时没有任何给予（`Provisioned`），从休眠中醒来不开始作为条件而在，不受这一要求约束（`Sleeper`）；没有支持时，在储备之下醒来只有有限多次，储备推迟终结而不逃脱（[reserve-defers-ending](../results/records/reserve-defers-ending.md)）。给予被耗散家族的形成从家族取用，所以在耗散之下，封闭的不重复家族中体现成员的每次生起都降低家族的存量；体现的生成在一个有限家族中复现，家族就在任意晚的步不封闭，这一交换可以与家族无关（`SprayHanding`），家族被围住时它汲入（`generation_draws_in`）；关系项总共有限时它终将停止（`generation_opens`、`generation_ceases`）。上文“继续生成”中 `dissipation_ceases` 所设的物理前提，对封闭家族中体现成员的生起，由平衡、耗散与体现推出。没有耗散（`Handing`）或不体现（`Flicker`）时，这些结论不成立；燃烧新燃料的传递满足全部前提（`Kindling`）。汲取承担自身的关系项，与它的每个活跃事件相互作用：蜜蜂与花各自依存于自身与对方时，没有第三个条件就连通，G0 在那里恰为种子加两项中立；各自只依存于对方时，两种估值都不关联它们，尽管两者都体现：体现本身不进入估值（`Mutualism`、`Mutualism.apart_embodied`）。在承担自身的体现关系项终结之步汲取它，不论是什么终结了它，是断裂，所以不是 living（`Embodied.ending_breaks`、`Predation`）；这包括旁观的汲取者、自然的终结与该关系项自身的最后事件（`Wilting`）。是否应如此、对哪些汲取者，属于 Ren 对生生的读法。

**Two roles of one relatum, and arising through giving.** Read with one kind of relatum, a formation can be a condition of others and of itself; which condition is which formation is supplied by the representation's shared index. In a balanced flow where only active formations give, an embodied relatum arises only as another active formation gives to it, and the formation that gives need not be embodied (`SunSeed`). Where only embodied relata give, the relatum that gives is embodied too, and may still be a sun depending on nothing (`EmbodiedSun`); taking embodied relata as 生, a reading that is Ren's, the author reads this as one formal content of the relation between the two 生; generations can arise without end, each given by the one before. An embodied relatum comes to stand as it arises and is given at least its new standing, so generation is itself replenishment: where embodied members of a family arise at arbitrarily late steps, its replenishment recurs whatever is taken. The requirement follows the rise of standing, not activity: in a balanced flow every rise is given to (`Balances.rise_given`), coming to stand is the rise from nothing (`Web.ComesToStand`), and a condition can simply keep rising (`Growing`); a seed can be given its standing while dormant and arise later with nothing given (`Provisioned`), and waking from dormancy, which is not coming to stand, is not bound by it (`Sleeper`); without support, under a reserve, waking recurs only finitely often, the reserve deferring the end without escaping it. A formation giving to a family dissipated on takes from it, so under dissipation each embodied arising in a closed family without repetition lowers its stock; a finite family in which embodied generation recurs is open at arbitrarily late steps, though the opening exchange may be unrelated to it (`SprayHanding`); enclosed around, it draws in (`generation_draws_in`); and with finitely many relata in all it stops. This derives the physical premise of `dissipation_ceases` for such arisings. Without dissipation (`Handing`) or without embodiment (`Flicker`) these conclusions fail; a handing that burns fresh fuel meets every premise (`Kindling`). Drawing on a relatum that bears on itself interacts with each of its active events, so mutualists each depending on itself and on the other relate directly, with no third condition; where each depends only on the other, neither valuation relates them, though both are embodied. Drawing on an embodied relatum that bears on itself, across the step at which it ends, is breaking and so not living, whatever ends it: this includes a bystander, a natural ending and the relatum's own last event (`Wilting`). Whether it should be, and for which drawers, is Ren's reading.

**演化是具体的机制，不是一切变化的同义词。** 传递、重建、变异与选择各有其关系，须各自说明（[演化之论](THE-THEORY-OF-EVOLUTION.md)、[演化组织](EVOLUTIONARY-ORGANIZATION.md)）。已检查的连接如下：

- 继承的结构排列改变后续复制（[inherited-structural-copying](../results/records/inherited-structural-copying.md)）；
- 形成的登记改变复制的保真度（[formed-copying-registration](../results/records/formed-copying-registration.md)）；
- 形成的检查／编辑改变已形成的后继（[formed-copying-correction](../results/records/formed-copying-correction.md)）；
- 生长约束碎裂与后继组成（[growth-constrained-fragmentation](../results/records/growth-constrained-fragmentation.md)）；
- 组织规则的形成与继承（[organizational-rule-inheritance](../results/records/organizational-rule-inheritance.md)）。

**在脊柱上，经世系的演化有最小的形式内容**（[Becoming.Evolution](../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Evolution.lean)，[evolution-on-descent](../results/records/evolution-on-descent.md)）。世系由参与、给予与开始作为条件而在定义，不含估值。不加前提：任意有限的亲代家族与后代，从亲代到后代的变化分为选择项（亲代按其后代加权）与传递项（`price`，Price 方程的加法计数形式；它是会计恒等式）。只有活跃者给予且活动需要支持时，只有被支持的形成留下后代（`unsupported_childless`），选择项受条件的水平所限（`selected_le`）。后代承接亲代的依存（`TransmitsWithin`，前提）时，传下来的所需曾在给予之步被满足（`transmitted_supported`）；在平衡的流中，其间的取用与给予设定后来能传递的（`transmitted_within`）。一个亲代自己的取用降低了池，使承继其所需的后代不被支持，所需较少的后代被支持并转而取用（`Drawdown`）：传递、变异、选择与活动对选择的反馈在同一展开中。适应度没有定义；繁殖率、突变、漂变与种群动力学不在其中；上列机制保持各自的范围，与它们的对应尚未证明。

**Evolution names specific mechanisms**, with transmission, reconstruction, variation and selection each explained through their own relations. It is not a synonym for every change. On the spine, evolution through descent has a minimal formal content. Descent is defined by taking part, giving and coming to stand, with no valuation. With no premise, the change from parents to offspring divides into a selection term and a transmission term (`price`, Price's equation in additive counting form, an accounting identity). Where only active formations give and activity needs support, only supported formations leave descendants, and the selection term is bounded by the condition's level. Where descendants take up their parents' dependences (`TransmitsWithin`, a premise), a transmitted need was met at the giving step, and in a balanced flow what is taken and given in between sets what can be transmitted later. A parent's own taking can leave the descendant inheriting its need unsupported while one needing less is supported and takes in turn (`Drawdown`). Fitness is not defined; reproductive rates, mutation, drift and population dynamics are not covered; the mechanisms above keep their scope, and no correspondence to them is yet proved.

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
- **直接的关系（候选）。** 以一类关系项读，交互之外还有两种直接的 `related`：以之为生（在某步汲取一个关系项并以正需要依存于它）与世系（参与一个关系项开始作为条件而在之步，并在该步给予它）。以之为生与交互一样不免费：它需要实际的汲取与能落空的依存；在 `Dependent` 之下所依的关系项在该步作为条件而在，体现时在该步活跃，但它不必体现，也不必活跃（`Drowsy`）。两者的定义都不含体现：这里进入估值的是一类读法的同一对应。它们使只依存于对方的蜂与花、各由前一代给予的世代连通，世代那里 G0 恰等于种子加 N_rel 加 N_std；在 N_rel 下，珍视狐的进食就到达兔的活，珍视给予的形成就到达生起者的活的事件。是否采用它们属于 Ren；`living` 与 C 不变（[Becoming.Descent](../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Descent.lean)，[living-on-and-descent](../results/records/living-on-and-descent.md)）。
- **读法相对于一次运行。** 同一过程、同一配置的两次运行可以给出不同的 living（`class_belongs_to_the_run`）。不依赖运行的读法，以及它与 `universal_reason` 的接通，开放。
- **对应义务不变。** 生物圈、气候之类的条件是否真被所有活的形成共同参与，是经验对应；关系读法是否即生生，是哲学论证。

**逐步读法与关系层读法。** 以“活跃且不侵蚀”为 `living`、以各自步上共同参与某一条件为 `related`，前两点照样成立：共同条件给出连通（`Web.significant_iff_of_common`）；在断裂之步汲取的事件与被断裂者共同参与该条件，在 N_rel 下，珍视这一事件的立场必珍视被断裂者活的事件（`Web.valuing_breaking_reaches`）。依存不变时整段与逐步读法的 `related` 相同，只在 `living` 上分歧，而且两个方向都有（`Commons.readings_differ`）。关系层读法以（形成，条件，步）为主张；一个事件的逐步读法恰是它所参与关系的读法的合取，同一事件可以有一个活的关系和一个侵蚀的关系（`Web.living_iff_relations`）。

**读法由 Ren 选择。** 独立审查判定关系读法的哲学根据尚未确立（[审查](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING-REVIEW.md)）。[研究 §8.5](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md) 按五条判据比较了各读法，并给出两条有范围的形式约束。其一，任何由有限前缀决定、并记入每次整段更新运行的读法，必记入某次消耗运行（`finite_reading_credits_consumption`）；它是否与 Ren 所采纳的问题冲突，取决于对这一问题的判决是否覆盖越过阈值之前的事件，以及可观测量是否带数量（`amount_reading`）。其二，单一部分的整段 but-for 检验不能代替参与（`Overdetermined.no_difference`、`no_finite_segment_makes_difference`）。[第二次审查](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-P7-REVIEW.md)接受全部数学，修正了侵蚀与 but-for 的定义，更正见研究 §11；[第三次审查](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-P8-P9-P7B-REVIEW.md)再修正二者，并把排序、替代与交互的说法收窄到所证明的范围，更正见研究 §12；[第四次审查](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-P9B-P10-P11-REVIEW.md)把侵蚀改为最小形式，并把继续生成与更多的说法收窄，更正见研究 §15。现有读法读出的都是“不损”，不含继续生成；继续生成陈述在整体的继续上（§2“继续生成”），尚未进入 `living` 的读法。哪一种读法或组合是生生的读法，是 Ren 方向内的规范与诠释选择，本章不替 Ren 作出。

The Becoming layer can supply `living` (the relational reading) and `related` (participation in a common condition):

- Under a correspondence discipline for conditions and participation, a common condition makes the whole connected, discharging that premise. One discipline is stated: a condition relates two events only when one draws on it and the other depends on it at a positive level. Idle conditions then connect nothing, a commons with a living drawer and a living dependent still connects, and connection through a condition is made by its living use; interaction is a structural coincidence at any steps, not yet ordered or effect-sensitive, and co-dependence is a relation the discipline omits; a renewed condition on which every formation depends at a positive level, used once, is not excluded, and is a factual claim for application to check.
- Under N_rel, valuing a consumer's activity reaches what it consumes, through co-participation in the drawn condition.
- Read with one kind of relatum, two direct readings of related are stated beside interaction: living on, drawing on a relatum and depending on it at a positive need, and descent, giving to a relatum, while taking part in the step, as it comes to stand. Under `Dependent` the relatum lived on stands at that step; it need be neither embodied nor active (`Drowsy`). Neither definition mentions embodiment: what enters the valuation is the one-kind identification. They connect the bee and the flower that depend only on each other and generations each given by the one before; under N_rel valuing the fox's eating reaches the hare's living, and valuing a formation that gives reaches the living events of what arises. Adopting them is Ren's choice, and neither living nor C changes.
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
| 动态依存 | 已定义并检查（[becoming-dependence-dynamics](../results/records/becoming-dependence-dynamics.md)）：依存跨步形成、维持、断裂与消解；定理联系起来的损失的三种结局，表示内的约束；替代在支持门控定律中保持整段分类（[substitution-preserves-consumption](../results/records/substitution-preserves-consumption.md)）；跨步的同一在哪些读法中起作用，单向的连续把它约束到接续为止，双向的连续把它约束到跨过休眠的接续为止；在普查、`present` 不重复与 Taking 之下，在每种没有分裂的延续下更多迫使生起，没有分裂是充分条件，不是必要条件（[identity-across-steps](../results/records/identity-across-steps.md)）；持续的整体，若部分短暂，或部分终结且同时活跃的部分有限，需要部分不断生起（[whole-persists-through-generation](../results/records/whole-persists-through-generation.md)）；`Dependent` 是零储备，有储备时终结推迟而不逃脱，储备在休眠中衰减时休眠的时间也有界；储备可以是所持的条件，没有表示时是给定的；所持条件承载形成时，依存转化到它上面的读法由构造满足 `Dependent`，而在 living 上不同（[reserve-defers-ending](../results/records/reserve-defers-ending.md)） | 沿依存链、有储备的滞后共灭；在所持条件被表示的地方，估值用哪种读法（Ren）；接续的读法与“生生不息”读到哪个层次（Ren）；跨过休眠的连续读法；整体的依存与侵蚀怎样由部分构成；延续关系下的类与侵蚀；延续关系上使更多迫使生起的充要条件；从关系推出跨步的同一 |
| 读法 | 已定义并比较，读法选择开放：整段、逐步（不侵蚀）、周期与关系层（[becoming-stepwise-reading](../results/records/becoming-stepwise-reading.md)、[becoming-return-grades](../results/records/becoming-return-grades.md)）；有限前缀不决定分类（[becoming-finite-horizon](../results/records/becoming-finite-horizon.md)） | Ren 选择生生的读法或其组合，以及 G0 与 C 是否共用一种读法（C 的排序随读法而变，[ranking-under-readings](../results/records/ranking-under-readings.md)）；条件的对应纪律已给出一条（[condition-correspondence-discipline](../results/records/condition-correspondence-discipline.md)），其时间次序、对效果的敏感与对整段读法的陈述开放；交互之外的以之为生与世系两种候选读法已给出（[living-on-and-descent](../results/records/living-on-and-descent.md)），是否采用属于 Ren；不依赖运行的读法；带数量与更新率的网；继续生成的成分 |
| 继续生成 | 陈述在整体的继续上：在有限条件、生起消耗有限家族、更新由形成造成的前提下，不息的生成需要更新复现，更新不蕴含生成；在平衡的流中，复现的取用需要补充复现，取用者不息地生起是其一种情形（[unceasing-generation-needs-renewal](../results/records/unceasing-generation-needs-renewal.md)）；读作取用者数目的“更多”需要补充与补充者没有最终的界，在普查、`present` 不重复与 Taking 之下严格蕴含不息（[more-needs-renewers](../results/records/more-needs-renewers.md)）；在耗散之下，复现的取用，无论来自更多、生成还是维持，其有限家族在任意晚的步不封闭，被围住时须从其外汲入，耗散只约束有封闭的有限家族的步（[no-finite-part-bears-taking](../results/records/no-finite-part-bears-taking.md)）；以一类关系项读，形成与条件是一个关系项的两种角色，哪个条件就是哪个形成由共同的索引给出；在平衡且只有活跃形成给予的流中，体现的关系项只经由另一个活跃者的给予而生起，给予它的形成不必体现（[life-as-condition-of-life](../results/records/life-as-condition-of-life.md)）；体现的生起本身就是补充；要求跟着水平的上升走，平衡的流中每次上升都被给予，在耗散之下在有限家族中复现的上升使家族不封闭，被围住时汲入（[generation-is-replenishment](../results/records/generation-is-replenishment.md)）；被耗散的一步上，一个成员上升，同一步上另一个成员下降，消耗前提由平衡与耗散推出（[rising-and-falling-in-one-exchange](../results/records/rising-and-falling-in-one-exchange.md)） | 第二个“生”的范围与以消耗为条件的生起是否为生成（Ren）；在承担自身的体现关系项终结之步的汲取是否计入不 living、对哪些汲取者（Ren）；汲取是否终结了它的因果读法；以之为生与世系是否作为直接的估值采用（Ren）；生成在多大程度上读作体现、体现的关系项是否读作“生”（Ren）；活动与水平不同步（种子、休眠）时的生成；可能性、多样性与复杂性的上升；生成成分进入 `living` 的读法；与 `universal_reason` 的新的活的内容接通 |
| 整体的规律 | 不加前提、对每个展开成立的一组规律已给出（[coming-and-ceasing-keep-pace](../results/records/coming-and-ceasing-keep-pace.md)）：同一种变化读于活动、依存与水平；一段步上的升降相抵；有限家族中下降复现需要上升复现，开始成立与不再成立同步，一方复现恰当另一方复现 | 对整个空间成立的规律的完整清单，以及每个前提都有满足与不满足它的展开（计划 P22）；下降何时在同一步上就是不再作为条件而在（P20 给出了上升与下降的同一交换）；生生不息在哪个层次读（Ren） |
| 演化 | 经世系的传递、变异与选择在脊柱上有最小的形式内容（[evolution-on-descent](../results/records/evolution-on-descent.md)）：不加前提的传递律；只有被支持的形成留下后代；传下来的所需曾被满足，其间的活动设定后来的选择。演化之论的独立纲领保持原范围（[演化之论](THE-THEORY-OF-EVOLUTION.md)） | 由依存的形成推出传递（`TransmitsWithin` 现为前提）；把后代数与给予的量联系起来（繁殖的读法）；有理数量与协方差形式；与结构复制、重构及组织规则继承的对应（外围） |
| 共同活动中的归属 | 相对于动作的 but-for 差别制造在多重决定下与关系参与分离；整段与步层面的检验分开（[joint-difference-making](../results/records/joint-difference-making.md)） | 更精细的归属（如 NESS、实际因果）作为另一读法；不推出责任 |
| 独立反审 | 关系读法与 P3b–P6 已经独立审查（[审查](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING-REVIEW.md)）：数学接受，哲学根据未确立，二十项更正已处理。回程、视界、共同活动与替代（P7）经[第二次审查](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-P7-REVIEW.md)：数学接受，侵蚀与 but-for 的定义已修正，十五项更正已处理。C 在各读法下的排序（P8）、条件的对应纪律（P9）与 P7b 的更正经[第三次审查](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-P8-P9-P7B-REVIEW.md)：数学接受，侵蚀改为比较那一步的所需，but-for 要求动作可取，排序、替代与交互的说法收窄，十二项更正已处理。P9b、不息（P10）与更多（P11）经[第四次审查](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-P9B-P10-P11-REVIEW.md)：数学接受，侵蚀改为最小形式，消耗前提、严格性见证、耗散、层级与补充者的说法收窄，十四项更正已处理。跨步的同一（P12）与 P11b 的更正经[第五次审查](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-P11B-P12-REVIEW.md)：数学接受，十二项更正已处理（P12b）。耗散（P13）、角色（P14）与 P12b 的更正经[第六次审查](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-P13-P14-P12B-REVIEW.md)：数学接受，耗散只约束有封闭的有限家族的步，一类读法的同一对应是表示的前提，终结之步的汲取与给予的说法收窄，十一项更正已处理（P16b）。生成即补充（P15）、整体与部分（P16）与 P16b 的更正经[第七次审查](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-P15-P16-P16B-REVIEW.md)：数学接受，耗散空成立时的开放可以由无关的交换满足，汲入须家族被围住，整体是活动的重合，“生由生”不是定理，`Merge` 的生起是重读，八项更正已处理（P16c）。P16c 的更正、储备与开始作为条件而在（P17）、以之为生与世系（P18）经[第八次审查](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-P16C-P17-P18-REVIEW.md)：数学接受，世系要求给予的形成参与该步，以之为生在 `Dependent` 之下给出的是所依者作为条件而在，储备可以是而不必是所持的条件，转化的读法在 living 上不同，要求跟着上升走，十项更正已处理（P18b）。不加前提的变化规律（P19）、P18b 的更正、上升和下降的同一交换（P20）与经世系的演化（P21）尚未经独立审查。A 的外在论辩护、N 的哲学根据未经独立审查 | 进行这些审查 |
| 经验对应 | 共同条件、各机制的实际实现 | 识别与可区分的检验 |
| 更强的方向假说 | 现实一般地发展出更共同、更有回应的更新：开放 | 不作为前提使用 |

## 9. 形式脊柱 / The formal spine

全部新的形式结果都陈述在同一条脊柱上。脊柱不能表达某个结果时，扩展脊柱，而不是另建模型。既有的通用伦理模块不复制、不改写：脊柱给出它们接口的实例（[实例分类表](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-INSTANCE-CLASSIFICATION.md)）。

All new formal results are stated on one spine; when it cannot express a result, the spine is extended rather than another model built. Existing generic modules are instantiated, not copied.

**核心纯净 / A pure core.** 按 [Ren 的要求](../../../sources/15-codex-theory-conversations/2026-10-09-pure-core.md)，核心（L0 及其两个基础模块，加 L1–L4）不导入核心以外的任何模块，其中每条源声明的公理报告为空，并且只用 Lean 的内置前导即可编译；检查器每次都检查这三点，并审计 Lean 生成的常量：其中依赖公理的只有带字段构造子的单射引理（`injEq`，依赖 `propext`），没有源声明使用它们。G0、C、D 与确保的正面根据在核心中陈述一次；桥接层证明既有模块的定义就是这些，依存方向从外围指向核心。外围可用任何合适的工具（Mathlib、Python）。核心是 Lean 包 `Becoming`：`import Becoming` 导入全部四层，桥接 `Becoming.Bridge` 在包内但不属核心（[包说明](../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/README.md)）。

The core (L0 with its two foundation modules, and L1–L4) imports nothing outside itself; every source declaration in it has an empty axiom report, and it compiles from Lean's prelude alone. The checker verifies all three on every run and audits the constants Lean generates: the only ones depending on an axiom are the injectivity lemmas of constructors with fields (`injEq`, on `propext`), which no source declaration uses. The bridge proves that existing modules' definitions are the core's; dependence runs from the periphery, which may use any suitable tool, to the core. The core is the Lean package `Becoming`: `import Becoming` brings in all four layers, and `Becoming.Bridge` sits in the package but outside the core.

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
| L3 | [Becoming.Flow](../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Flow.lean) | 消耗与补充的平衡；平衡的流中上升由补充者造成；复现的取用需要补充复现，取用者不息地生起与恒定的取用者都是其情形；不止地更多需要没有最终界的补充与补充者；不息的生成尚不是更多；每次上升都被给予，每次下降都被取用，上升复现时补充复现，开始作为条件而在是从零的上升 | 76 |
| L3 | [Becoming.Change](../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Change.lean) | 不加前提、对每个展开成立的规律：同一种变化读于活动、依存与水平；不再成立之外即持续；支持只经由关系改变；一段步上的升降相抵；量不低于零，有限家族中下降复现需要上升复现，量有界时反之亦然；有限家族中开始成立与不再成立同步，一方复现恰当另一方复现；形成有限多时生成不息恰当止息不息；无限家族的见证 | 42 |
| L3 | [Becoming.Population](../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Population.lean) | 活跃形成的普查；在普查、`present` 不重复与 Taking 之下更多蕴含不息，花园与循环满足全部前提；缺少任一前提时的反例 | 36 |
| L3 | [Becoming.Identity](../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Identity.lean) | 跨步的同一：改名与改认；不依赖与依赖同一的读法；单向与双向的连续，接续与休眠；延续关系，没有分裂时更多迫使生起（充分而不必要），萌出或没有普查时不然；谱系与成员的两个层次；含合并时的生起可以是持续形成被重读，被合并者终结时生起的恰是新的 | 83 |
| L3 | [Becoming.Wholes](../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Wholes.lean) | 整体与部分，活动的重合：整体只经由部分的生起而生起；部分覆盖每一步时，部分短暂则有部分不断生起（可以是同样的部分），部分终结且同时活跃的部分有限则不断有新的部分生起；持续的整体被部分覆盖；前提必要与逆命题不成立的见证 | 36 |
| L3 | [Becoming.Dissipation](../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Dissipation.lean) | 封闭与耗散；被耗散的家族上取用终止；取用复现的有限家族在任意晚的步不封闭，被围住时汲入，维持一个取用者已如此；条件总共有限时取用终止；封闭的步上给予须以取用为条件，没有封闭的步时耗散是空的；给予被耗散家族的形成从中取用；上升（包括开始作为条件而在）不需要自身的取用也落入其中；被耗散的一步上，下降至少等于上升加取用者数，一个成员上升，另一个成员下降，有上升而无下降的不重复家族在该步不封闭，消耗前提由此推出 | 89 |
| L3 | [Becoming.Roles](../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Roles.lean) | 形成与条件是一个关系项的两种角色，两类读法嵌入其中，同一对应由共同的索引给出；体现与承担自身；共灭；终结之步的汲取；经由另一个活跃者的给予而生起；生成即补充，耗散之下在有限家族中复现的体现生成使家族不封闭，被围住时汲入；互利、捕食、凋谢、世代、太阳与种子、体现的太阳、传递、燃烧、汇旁的传递与闪现的见证；体现的生起就是开始作为条件而在；耗散之下体现的生起伴随另一个成员的下降，世代中不然 | 134 |
| L3 | [Becoming.Reserve](../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Reserve.lean) | 储备：零储备恰是 `Dependent`，储备可以是所持的条件，没有表示时是给定的；所持条件承载形成时，转化的读法由构造满足 `Dependent`，而在 living 上不同；储备推迟损失与共灭之后的终结而不逃脱，在休眠中衰减时也界定时间；水平可以早于活动，醒来不开始作为条件而在；种子、存活力、饥荒、休眠与供给的见证 | 42 |
| L3 | [Becoming.Evolution](../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Evolution.lean) | 世系、传递、变异与选择：世系由参与、给予与开始作为条件而在定义；不加前提的传递律（Price 方程的加法计数形式）；只有活跃者给予且活动需要支持时，只有被支持的形成留下后代，选择项受条件的水平所限；传递是前提，传下来的所需曾在给予之步被满足，其间的取用与给予设定后来能传递的；`Drawdown` 的见证与没有 `Dependent` 时的反例 | 21 |
| L4 | [Becoming.Metaethics](../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Metaethics.lean) | 前提卡、G0 刻画、极小性、普遍理由；整段、逐步与关系层的读法 | 35 |
| L4 | [Becoming.Ranking](../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Ranking.lean) | C 在整段与逐步读法下的排序；二元定律族中节制排在过度汲取之上 | 27 |
| L4 | [Becoming.Correspondence](../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Correspondence.lean) | 条件的对应纪律：交互；惰性条件不连通；连通由活的使用造成；一类读法保持连通，承担自身的形成直接相关，体现不进入估值 | 37 |
| L4 | [Becoming.Descent](../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Descent.lean) | 一类读法提供的两种直接关系：以之为生与世系（定义在 `Becoming.Evolution`）；在 `Dependent` 之下所依者作为条件而在，不必体现或活跃；世系要求给予的形成参与该步；沿二者的 N_rel 传递；生起的体现关系项从给予它的活跃形成而来；世代由世系连通，G0 在那里有刻画；同一对应进入以之为生；世系跟着水平走 | 41 |
| 桥接 / Bridge | [Becoming.Bridge](../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/Bridge.lean) | 既有接口是脊柱的实例；核心定义即既有定义；J1/J2 的 `BetterAt`；比较经 L 推广；整段读法即既有的关系清单 | 34 |

[合并检查器](../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/check_becoming.py)与[回执](../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/becoming-verification.json)覆盖 910 项定理、1435 项声明审计，源声明的公理报告全部为空；核心闭包共 26 个模块（包 24 个模块，含根模块与桥接）；15 个继承模块的当前字节须与已通过的回执一致。依赖 Mathlib 的叶子经外围桥接 [CorrectionInquiry](../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/CorrectionInquiry.lean) 连到核心：它用 Lean 4.30.0-rc2 与 Mathlib 检查，核心模块在那里同样编译通过，桥接的 7 项定理公理报告为空。方向与计划见[统一计划](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-UNIFICATION-PLAN.md)。

The consolidated checker and receipt cover 910 theorems and 1435 declaration audits, all source declarations with empty axiom reports; the core closure has 26 modules (the package 24, with the root and the bridge). The current bytes of 15 inherited modules must match passed receipts. Mathlib leaves connect through the peripheral bridge CorrectionInquiry, checked with Lean 4.30.0-rc2 and Mathlib; the core compiles there too, and the bridge's 7 theorems have empty axiom reports.

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
| 开始成立／不再成立 | comes to be / ceases to be | 一个规定跨一步由不成立变为成立／由成立变为不成立；生起、形成与开始作为条件而在，止息、消解与不再作为条件而在，是它分别读于活动、依存与水平 | `ComesToBe`、`CeasesToBe`、`Web.change_readings` |
| 形成／消解（依存） | forms / dissolves | 依存跨一步出现／消失 | `Forms`、`Dissolves` |
| 步内更新 | within renewal at a step | 事件所在之步维持其所参与条件上的每个依存；逐步的更新分类 | `RenewingAt` |
| 断裂（事件） | breaking | 在断裂某个依存之步汲取该条件 | `BreakingOn`、`BreakingAt` |
| 生起 | arising | 形成跨某步由不活跃变为活跃 | `Arises` |
| 止息 | ceasing | 形成跨某步由活跃变为不活跃；有限家族中生起复现恰当止息复现 | `Web.Ceases`、`Web.arising_recurs_iff` |
| 同步 | keeping pace | 有限家族中，任一段步上开始成立与不再成立的次数之差不超过成员数；终点成立的连同其间不再成立的，恰是起点成立的连同其间开始成立的 | `keep_pace`、`held_over_stretch` |
| 不息 | unceasing generation | 某个形成在任意晚的步生起；同一形成可以再生起 | `Unceasing` |
| 消耗（有限家族） | depletion | 在事件的每个家族都不上升之步，其中某个条件下降；只说家族中有条件变化；平衡的流中，事件之步上家族被耗散且有形成从中取用时成立 | `Depletes`、`Balances.depletes` |
| 耗散 | dissipation | 在依存网上：一个量从不上升，而每次生起都使它下降；在流上：每个参与的形成给予封闭家族的不多于从中所取，取用时更少；只约束有封闭的有限家族的步，在那里给予须以取用为条件 | `dissipation_ceases`、`Dissipative`、`giving_needs_uptake` |
| 同一交换 | one exchange | 被耗散的一步上，一个成员的上升与另一个成员的下降；不把某次下降单独归给某次上升，下降不是止息 | `rise_with_fall`、`rise_exchange` |
| 封闭 | closed | 一步中没有参与的形成与家族之外的条件交换 | `ClosedAt` |
| 封闭的步 | enclosed step | 跨该步有一个不重复的有限家族封闭；条件总共有限时每步都是 | `Enclosed` |
| 围住 | enclosed around | 跨该步有一个包含该家族的不重复有限家族封闭；相等可判定时每个封闭的步都围住每个有限家族 | `Around`、`Enclosed.around` |
| 汲入 | drawing in | 在任意晚的步有形成给予家族而从家族之外取用；耗散之下，被围住而取用或体现的生成复现的家族汲入 | `Inward`、`taking_draws_in`、`generation_draws_in` |
| 流 | flow | 每步参与的形成从条件取用与给予的量；平衡时水平的变化恰是二者之差 | `Flow`、`Balances` |
| 取用／补充 | uptake / replenishment | 一步中参与的形成从家族取用的总量／给予家族的总量；二者与水平的变化相平衡 | `uptake`、`replenishment` |
| 取用者／补充者 | takers / renewers | 一步中从家族取用／给予家族的形成 | `takers`、`renewers` |
| 取用而生起 | arising taking | 形成在其第一个活跃步从家族取用 | `ArisesTaking` |
| 普查 | census | 每步活跃的形成列为不重复的有限表 | `Census` |
| 取用即汲取 | taking | 只有活跃的形成取用，且只从它汲取的条件取用 | `Taking` |
| 不止地更多 | more without end | 对每个数，从某步起至少有那么多形成从有限的条件家族取用 | `More` |
| 改认／改名 | re-identification / renaming | 在每一步把两种命名一一对应，每一步的关系不变；每一步都相同的改认是改名 | `Reidentify`、`Reidentify.rename`、`Web.reidentify` |
| 连续 | continuity | 跨一步持续活动、或持续依存于某条件的形成保持名字；以旧命名为参照是单向的，另以新命名为参照是双向的；一种同一的读法，不是同一的定义 | `KeepsActive`、`KeepsTenure`、`Reidentify.back` |
| 接续 | succession | 把在某步终结的形成与在该步或其后开始的形成接为同一个（中间可以有不活跃、不依存的步，例如休眠）；单向的连续不排除它，双向的连续不排除跨过休眠的它，怎样读属于 Ren | `Lineage`、`Succession`、`Dormancy`（见证） |
| 延续关系 | continuation | 一步之后的形成延续一步之前的哪个形成；分裂是一个形成延续为几个，合并是几个延续为一个；改认是一一对应的延续 | `Web.Continues`、`ArisesFrom`、`NoSplit` |
| 整体／部分 | whole / parts | 整体恰在某个部分活跃时活跃，是活动的重合；部分短暂，或部分终结且同时活跃的部分有限时，整体的持续需要部分不断生起 | `Whole`、`Covered`、`Brief`、`Ends`、`Listed` |
| 角色 | roles | 形成与条件是一个关系项的两种角色；两类读法嵌入没有形成作为条件的一类读法；哪个条件就是哪个形成由共同的索引给出，是表示的前提 | `Web.roles`、`Flow.roles`、`Web.relabel` |
| 体现 | embodied | 关系项恰在活跃时以正的水平作为条件而在，是同一对应下的读法；它的生起就是开始作为条件而在，所以是补充；体现本身不进入两种估值 | `Embodied`、`Embodied.comesToStand`、`Embodied.replenishes`、`Mutualism.apart_embodied` |
| 开始作为条件而在 | coming to stand | 条件的水平跨一步从零变为正，是从零的上升；在平衡的流中每次上升都被给予，开始作为条件而在至少被给予新的水平，所以是补充；上升在耗散之下复现时使有限家族不封闭，被围住时汲入 | `Web.ComesToStand`、`ComesToStand.rises`、`Balances.rise_given`、`standing_given`、`rising_draws_in` |
| 不再作为条件而在 | ceasing to stand | 条件的水平跨一步从正变为零；有限家族中开始作为条件而在复现恰当它复现，不需要任何前提 | `Web.CeasesToStand`、`Web.standing_recurs_iff` |
| 承担自身 | bearing on itself | 关系项活跃时以正的需要依存于自身的水平 | `SelfBearing` |
| 共灭 | coextinction | 在 `Dependent` 之下，一个在某步不活跃的关系项在该步终结每个依存链（以正需要、经体现的关系项）到达它的形成；有储备时，单环的共灭推迟而不逃脱 | `coextinct`、`Carries.coextinct_lasts` |
| 储备 | reserve | 形成不被支持时不上升、在其间活跃时下降的量；零储备恰是 `Dependent`；可以是所持条件的水平，没有表示所持条件时是给定的量；从某步起不被支持的形成至多活跃开始时储备那么多次 | `Web.Carries`、`carries_zero`、`Flow.carries_of_held`、`Carries.lasts` |
| 侵蚀 | undermining | 在某步汲取某条件，而该步之后条件既低于一个依存现在的所需，也低于该依存在不间断成立期间的某步曾被满足的所需；逐步读法的 living 是活跃且不侵蚀 | `MetAbove`、`UnderminingOn`、`UnderminingAt` |
| 回程 | return | 某步成立的依存在以后某步（或 `p` 步之内）再被满足 | `Returns`、`ReturnsWithin`、`RenewedWithin` |
| 视界 | horizon | 有限的前缀；两次运行在其前相同 | `Run.AgreeUpTo` |
| 差别制造 | making a difference | 扣除一方的部分后，以同一动作的每一步都维持依存（且该动作可取） | `MakesDifference`、`Overdetermined` |
| 交互 | interaction | 一方汲取某条件、另一方以正水平依存于它，在任何步上；对应纪律下的 related | `Interacts`、`Web.interaction` |
| 以之为生 | living on | 一类读法中，一个形成在某步汲取一个关系项并以正需要依存于它；在 `Dependent` 之下所依者在该步作为条件而在；交互之外 related 的一种候选读法 | `Web.LivesOn`、`LivesOn.stands`、`Web.sustenance` |
| 世系 | descent | 一类读法中，一个关系项在开始作为条件而在之步被参与该步的一个形成给予，就从它而来；使两者的每个事件相关，是 related 的另一种候选读法 | `Flow.DescendsAt`、`Flow.Descends`、`Flow.descent` |
| 传递 | transmission | 后代承接亲代的依存，所需至多多 δ；是由应用给出的前提，脊柱不推出；`price` 中是每个后代相对其亲代的变化 | `Flow.TransmitsWithin`、`raised`、`lowered` |
| 选择 | selection | 只有活跃者给予且活动需要支持时，只有被支持的形成留下后代；`price` 中是亲代按其后代数加权；适应度没有定义 | `unsupported_childless`、`selected`、`selected_le` |
| 传递律 | law of transmission | 不加前提：后代的总量加传递所降低的，等于选择项加传递所升高的；Price 方程的加法计数形式，是会计恒等式 | `price` |
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
