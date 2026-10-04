# Q3 · V6.1 的论证与正面方案（Opus 规划）

2026-10-03。V6.1 三位规划者之一，负责"论证怎样重述、正面方案怎样修"。数学规划者给出修复后命题的精确形式，结构规划者给出文档结构；本文件一律用 v6.0 的结果编号，行号指 `v6/THEORY.md` v6.0。没有读同题的 `Q3-argument-design.md`。未改动任何既有文件。

**依据。** `SYNTHESIS-v6.0`；六份同族评审与 Codex 评审；三份 Opus 复核（评审与复核冲突时从复核，少数例外列在第八节）；`V6-PLAN`、`P1`、`P5`；v5.2 原文；Ren 语料（`relational-self-and-datong`、`selfishness-spiral` README 第 H 部分）；记忆中 Ren 的裁定。

**符号暂定，待数学规划定稿。**
- β：不论胜负都均分的份额（分享）。
- κ_c：赢得之物中可转换为同一竞赛能力的份额。
- K₀：不必靠赢得的能力（"树"）。
- χ：只用于第 4 节的可占有性。
- κ：只用于未定价耦合。
- C_i、D_i、v_i、g_i：合作、决定性位置、惩罚的每期价值，以及一期偏离收益。

定义 2.1 现在用 χ、ρ 表示"保留份额""再投入份额"，与注释 5.3、§4 冲突，要一并改。

---

## 〇、组织句

V6.1 全篇用一个问题组织。它是 Codex 的中心问题，也是 Ren 原话的精确形式：

> **Can restraint remain incentive-compatible when success changes both the gains from defection and the institutions capable of correcting it?**

Ren 的原句给出答案的形状："at the core, it is the selection pressure of winning that lead to acceleration that makes these more and more difficult to regulate, plus it alienate language. these of course overlap."

建议的论题句，§1.2 第 1 条与 §10.8 首段共用：

> Where carriers are selected by relative success, what is won can be reinvested in the capacity to win, and a lead can become decisive, success raises the stakes and the gain from defection while it weakens the sanctions, the correctors and the shared language that could restrain it. Where success can also buy the selectors, that weakening is reproduced by the selection itself. This is the selection pressure of winning, and its reflexive closure is the meta-attractor of winning. It accelerates the contest, makes it harder and harder to regulate, and alienates language, and the three reinforce one another.

本计划在"一股压力"能否被优雅证明的两种结果下都成立（见 1.6）。

---

## 一、相互联系的条件（交付 1）

### 1.1 核心对象：三个条件加反身闭合，名称不变

"赢的选择压力"保留为名称，但它指三个条件**共同产生**的东西，不再指一个单一原因。这正是 Ren 对"一"的用法：相互联系、同属一个系统，而不是"只有一个因"。这样，"一股压力"被提升到正确的层面，而不是撤回。

定义 2.1 重写（L166–178）：

> **Definition 2.1 (The selection pressure of winning) [D].** Carriers are any reproducible units that can gain or lose share: [list unchanged]. A system of carriers is under a *selection pressure of winning* when three conditions hold together, each to a degree.
> 1. **Relative selection.** Shares change with success relative to the others, by a relative, payoff-monotone rule (Definition 3.2).
> 2. **Reinvestable winnings.** Part of what is won can be converted into capacity to win the same contest. Three quantities set how much: the convertible share $\kappa_c$, the share $\beta$ divided whatever the outcome, and the capacity $K_0$ that does not have to be won.
> 3. **Decisiveness.** Capacity converts into winning by an increasing success function of decisiveness $r$, and a lead can become a position beyond sanction, with probability $p_d$.
>
> When success can also be converted into control over the selection itself (the rules, the correctors, the formation of minds, language), at conversion rates $b_{ij}$ and with appropriability $\chi$, the pressure closes on itself (Definition 2.2).
>
> The conditions are not a list of independent causes. They are linked in two ways. The same few parameters enter each of the threshold results of Sections 4 and 5, so that a change in one moves several. And growth under the conditions moves those parameters together. That is why acceleration, harder regulation and alienated language arrive together and make one another worse. The name refers to what the conditions produce jointly, not to a single cause behind them.

"Remove any one and the loop opens"（L173–178）按 K₀ 结果改写。Ren 语料的三要素在 $K_0>0$ 时逐条成立，请数学规划核对：

> Given any capacity that need not be won ($K_0>0$), remove any one of the three ingredients the author's corpus names, keeping what is won, reinvesting it, never stopping, and equal standing is stable: share what is won until $(1-\beta)r\le1$; make it non-convertible until $\kappa_c\Omega((1-\beta)r-1)\le n\delta K_0$; or stop at a point of enough no higher than what all can hold (Remark 5.3).

### 1.2 联系在哪里：共享参数表

这张表给起草者核对，放在 §2.3 机制表之后，或放进附录 D。标记的含义：
- [T]：该参数出现在一个已证（或待修复）的门槛式里；
- [A]：该联系是论证，跨模型时须走附录 E 的接口。

| 参数 | 加速（强度、复利） | 执行（5.7 修复式） | 纠错（俘获、速率） | 语言 |
|---|---|---|---|---|
| $r$ 决定性 | 强度与耗散 ∝ $r$（3.9(1)、5.2）[T]；复利门槛 $(1-\beta)r$（5.3）[T] | 抬高 $p_d$ 与 $D-C$ [A] | — | 排名奖抬高 $\lambda$，偏差 $b=\lambda\beta_s$（3.6、5.14(2)）[A] |
| $\Omega$ 赌注 | 强度 ∝ $\Omega$ [T] | 抬高 $g$、$D$ [T] | 抬高影响力回报 [A] | 抬高偏差 [A] |
| $p_d$ | 由领先的持久性抬高 [A] | 剩余制裁 $\delta(1-p_d)(C-v)$ [T] | 侦测窗口（7.7(2)）[T∣A] | — |
| $\beta$ 分享 | $\Omega_{\text{eff}}$（8.6(2)）[T]；$(1-\beta)r$ [T] | 抬高 $C$、降低 $g$；须在决定性之前兑现（5.10(3)）[T] | — | 降低 $T-R$ 与 $\lambda$（9.2(1)）[T] |
| $\kappa_c$ 可转换 | 只在 $K_0>0$ 时影响门槛 [T] | — | 转化为控制的是另一个量 $\chi$ | — |
| $K_0$ 底座 | 稳定平等地位 [T] | 保住落后者的制裁能力（$C-v$）[A] | — | 降低"生存斗争"的增益（C8）[C] |
| $\chi$、$b_{ij}$ 转化为控制 | — | 被俘获的规则者与评估者削弱侦测与惩罚 [A] | 回报 ∝ $\chi p^2$；行和；$d^\ast$（4.2、4.4、4.8）[T] | 遮蔽 $m$（4.6）[T]；指标被征用 [A] |
| $g$ 对 $b+g_c$ | 速率 $a$ [A] | 侦测窗口缩短 [A] | 证书在 $\alpha<g/(1+\eta)$ 时失效（4.4(3)）[T] | — |
| $\theta$、$\lambda$ 赢的权重 | 强度 ∝ $(n-1-\theta)$ [T] | 推论 5.8；$\theta_{\text{rep}}$（5.9）[T] | — | 两方 $\theta=-1$ 零和、无信息；$n\ge3$ 时结盟（5.14 修复）[T] |

表后一句：

> Growth under the conditions raises $\Omega$, $r$ and $p_d$, lowers the remaining sanction $C-v$, cheapens control faster than independent correction, and raises the weight on winning that biases what rivals say. Each arm is a result in its model. That they move together in the world is a conjecture [C], and it is what the discriminating predictions of Section 2.7 test.

$\theta$ 不是条件，是被选出的设定。条件把 $\theta$ 推向 $-1$（3.9(4)），被选出的心智又维持条件。这是反身闭合在心智层面的形式，摩洛克化仍标 [C]。

### 1.3 作者的因果链：一条链，四个回路，W→C→N

v6.0 在 §2.4 把三个后果并列，链被拉平了（忠实度评审次要项；复核：§2.4(2) 已有半句）。下面的文字放在 §2.3 末尾，取代"Three products"一段的开头。

> **The chain.** At the core is the selection pressure of winning. It accelerates the contest: winnings compound where the threshold of Remark 5.3 is crossed, and the fear of falling behind makes every participant faster, not only the leaders. Acceleration makes the contest harder and harder to regulate, for two reasons that reinforce each other. Correction falls behind the tempo it must match (Proposition 5.11). And where success reaches the selectors, the correctors become something success can buy (Section 4). The same pressure alienates language: between opposed parties talk stops carrying information, measures become targets, and the frames that spread are those fit for the contest. These overlap, and each consequence is also a mechanism of the others. Acceleration shortens the time in which correction must act. A captured corrector hides the harm that would start correction. Alienated language delays the recognition that would mobilize it, and weakens the agreement on which enforcement depends.

四个回路按回路写出，各接自己的位置。不要改成"三个产物"，那会把账本改错（忠实度复核）：

> In the author's corpus the chain is four loops in series, each closing on itself.
> 1. **Compounding.** What is won is kept and used to win more (Remark 5.3; Section 5.1).
> 2. **Capture of the rules, and "adopt or be out".** The successful reshape the rules and the correctors. Newcomers must adopt the favoured practice to obtain the resources to compete at all (Section 2.2; Propositions 4.2, 4.9).
> 3. **Naturalized narrative.** The frames the contest rewards spread until they are read as human nature, and a frame read as nature is no longer contested (Section 5.4).
> 4. **Regulator lag.** Correction lags because the first three loops produce the lag. Acceleration widens it, captured correctors lengthen it, and naturalized narratives delay the recognition that would start it. The pressure needs only that change outrun the updating of its correctors.

原"三个产物"中，"滞后是被产出的"并入第 4 回路。另外两条（范式趋同；损害与俘获互强）连同语料里的"竞争加剧"（fewer hold more, more compete over less），改称 intensifiers。

§2.5 恢复 v5.2 的 W→C→N 回路（v5.2 L115–120），并说明它就是这条链在可观察层面的读法：

> The signatures sustain one another, and the loop they form is the chain read at the level of what can be observed. W supplies the success that C converts into control. C removes the correction that would make the shared visible. N makes cooperation look naive, which keeps W in place.

§2.4 三个后果的标题按链写：

> 1. **Acceleration.** …
> 2. **Regulation becomes harder**, in part because acceleration outruns correction, and in part because the correctors become what success can buy.
> 3. **Language is alienated**, and the alienation delays the recognition that would begin correction.

第 2 条之后，补忠实度复核遗漏 5 要的一句反身关系：

> The consequences then act as mechanisms in their own right (Section 2.3).

### 1.4 反身闭合与"元吸引子"之名

定义 2.2 不动。在它之后加一个短注（忠实度重要 6；系统评审次要项）：

> *Why "meta-attractor".* The term is kept over "generator functions" for three reasons. That phrase names causes of risk without the reflexive step, in which selection rewrites its own criterion; without persistence; and without the layer of minds and language. It also has no generative counterpart, while the same reflexive structure selecting for contribution is the subject of Section 8. A meta-attractor in sense (1) is a mechanism, and calling a mechanism an attractor anticipates sense (2). The name is kept so that one concept covers both, and every claim says which sense it uses. Where a claim about the world uses sense (2), it is a conjecture [C].

§2.10 末尾补第 (3) 层的用法（系统 F5.4）：

> The diagnosis of the present trajectory is at layer (1) [O, partly evidenced]. Layer (2) is shown in the field model [T]. Whether the present configuration is attracting or a long transient (layer (3)) is open, and test T-D discriminates them.

§2.3 删去 "the attractor of attractors" 的语录式用法，改为 "what the author's corpus calls the attractor of attractors: the belief that one is in a struggle for survival"，只作出处说明。

§7.2、§10.8 的 "changes the basin" 加 [C]。

### 1.5 主张层级

| 主张 | 类型 | 说明 |
|---|---|---|
| 三个条件与反身条件；名称 | [D] | 定义 2.1、2.2 |
| 各门槛：执行条件、复利条件（含 $K_0$）、俘获证书与速率律、速率界、话语结果 | [T]（各自模型内） | 数学规划给精确式 |
| 同一组参数进入各门槛 | [T∣A] | 同一个符号代表同一个量，靠附录 E 的接口；每个接口单列 |
| 增长同时推动这些参数（剪刀差） | 模型中 [T∣A]（逐臂）；现实中 [C] | 用 1.7 的区分性预测检验 |
| 反身闭合 | 机制 [D]；场模型中吸引 [T]；现实中吸引 [C] | 1.4 |
| 四回路与 W→C→N 刻画当下轨迹 | [O] 部分有证据 + [C] | T4/C2 仍是缺口（EV4） |
| T1–T6 载荷于单一潜因子 | [C]，研究问题 | 不作为核心的检验登记（SYNTHESIS §六.2） |

同步改的地方：
- §1.5 第 1 条主张改为：

  > The dynamics of the present trajectory are produced by a small set of interlocking conditions, relative selection, reinvestable winnings and decisiveness, closed on themselves where success reaches the selectors, and linked by shared parameters, so that growth moves them together. This is the selection pressure of winning; its reflexive closure is the meta-attractor of winning (Section 2).

- §1.6 与 §2.9 的"新增"清单相应改写（见 1.8）。

AI 的特异性：对抗评审次要 12。按复核，拒绝其中对"不依赖载体"的批评，采纳"写明 AI 把哪些参数推入危险区"。在 §2.8 末尾或 §6 开头加一句：

> What is specific to AI is not the pressure but how far AI moves its parameters. It can raise decisiveness and the speed at which leads open ($r$; P2). It lowers the cost of control faster than the cost of independent correction ($g$ against $b+g_c$). It raises the growth of hazardous behaviour relative to contestable coverage ((X), (U)). And it can become a carrier itself (Section 6.4).

### 1.6 若数学规划证出"一股压力"

候选的单一量是**赢的私人价值相对于联合价值**。推论 9.2(1) 已经显示，降低它会同时放松 $T-R$、$\lambda$ 和净退出收益。如果数学规划证明各门槛在其他参数固定时都对这个标量单调，就这样改：
- §2.1 把"赢的选择压力"定义为这个量；
- 三个条件改称"决定它的三个通道"；
- 1.2 的表成为"每一种侵蚀都对它单调"的证明索引；
- 其余各节不动。

即使证出，它也只是**模型中的一个量**，不是"一个根"。它对现实的主张仍是 [C]，仍由 1.7 检验。这是 Ren 提醒过要盯住的单根反射。

如果证不出，就用 1.1 的写法。两种情况下，名称、因果链、四回路、共享参数表都不变。

### 1.7 §2.7 的诚实残余：可证伪而且能区分的部分

对抗评审重要 5 与复核的结论：五条预测大多被已吸收的理论同样预测。处理办法是每条注明"还有谁预测"，只把区分性残余登记为预测。§2.7 改名为 "What the conditions predict that their absorbed components do not"，正文给下表。

| 原预测 | 还有谁预测 | 区分性残余（登记） | 检验 |
|---|---|---|---|
| (1) 共变（单因子） | 任何共同冲击；现实主义；普通竞争 | 降为研究问题 [C]。登记的替代形式是**交叉效应**：移动一个共享参数（如经费公式化、准入强制，使 $b_{ij}$ 下降），会在不止一组签名（W、C、N）中产生变化；只针对单一签名的行为规则（如一项披露义务）不会。"分开的问题"一说预测各管各 | T-E 改作交叉效应检验 |
| (2) 不对称干预 | Stigler（被俘获的规则衰减）；Pierson | 衰减率与测得的入向转化相连：入向行和大于一的领域，规则被重新吸收；小于一的领域，规则持久（4.9(2)）。分类必须**事先按描述性剖面**做（Codex 6；见 4.6） | 定义 7.12 的登记预测，按行和分层 |
| (3) 滞后 | Pierson；沉没成本；官僚惯性 | **两相**：隔离规则制定之后，份额水平在规则支持越过分界之前就已下降；在这时按水平撤回会被重新吸收（系统复核 F4）。限于没有沉没成本解释的行为 | T-D 改写 |
| (4) 少对多 | Olson；Stigler；Bombardini（本文已引） | 影响力随份额超线性增长（$p^2$）；培育出的转化量取决于**三阶矩**而不是 HHI（4.4(8)）：两个独立的均等载体给出垄断值的四分之一，HHI 给出一半 | 并入 T-B(i)；T-K 降为确认性 |
| (5) 两个方向的俘获 | Stigler 1971 的主线 | 撤为非区分性。可失败的形式见 T-B(ii) | T-B(ii) |
| （新）目标随 $p_d$ 的作用 | Powell 1991 方向相反 | $p_d$ 越高，宽目标与窄目标之间的克制差距越大（注释 5.9：$\theta_{\text{rep}}$ 随 $p_d$ 从 −0.90 升到 0.94） | T-G 改符号 |

**反驳条件**保留 L340–342 的两条，改成条件的语言：

> **What would refute it.** Suppose a system lowers the shared parameters for every capable actor: consequences return to their source, success earns rewards but cannot buy control over its own assessment, decisive positions are kept from forming or held in common, provision does not have to be won, and measurement is shared. If the signatures then persist unchanged over the dwell time, the claim fails. If moving one shared parameter changes only its own signature and leaves the others unchanged over that time, the claim that the conditions interlock fails for that parameter. Conversely, durable safety obtained by constraining conduct while the conditions stay as they were, maintained as stakes and speed grow and classified as such before the outcome is known, would refute the claim that the conditions must change.

### 1.8 同步改的地方

**中文概要第 1、2 条（L9–15）的替换文字：**

> 1. **一组相互联系的条件。** 三个条件同时成立时，就有"赢的选择压力"（定义 2.1）：
>    - 参与者按**相对**成功被选择；
>    - 赢得的东西可以**再投入**同一场竞争，能投入多少，取决于可转换的份额、被分享的份额，以及不必靠赢得的能力；
>    - 能力按一定的**决定性**转化为胜出，领先可能变成不受制裁的地位。
>
>    成功若还能买到对选择本身的控制，也就是规则、纠错者、心智的形成和语言，压力就闭合于自身。这个反身闭合就是"赢的元吸引子"（定义 2.2）。这三个条件不是并列的清单：同一组参数同时出现在执行、复利、纠错与话语的门槛里，增长会同时推动它们。……（不依赖载体一句保留）
> 2. **一条因果链，四个回路。** 赢的选择压力使竞争加速。加速使竞争越来越难规制：纠错跟不上它要追的速度，纠错者本身也成了成功能买到的东西。同一股压力还使语言异化。三者互相重叠，每一个后果又是其他后果的机制。作者语料中的四个回路，即复利、规则被俘获与"不跟就出局"、叙事被自然化、规制者滞后，就是这条链。T1–T6 是它在可观察层面的签名。本文只登记能把它与已被吸收的理论区分开的预测（第 2.7 节）。

**§1.2 第 1、2 条**按 1.1、1.3 同义改写。

**§2.9 "What is new"** 改为八条：
1. 反身闭合作为具体机制（§4）。
2. 条件之间的联系：共享参数与剪刀差（§5）[T∣A]。
3. 执行条件（5.7 修复式）：赢怎样移动其中每一项。
4. 含 $K_0$ 的复利条件："树"的形式内容。
5. 记账恒等式（3.5）。
6. 普遍约束怎样存续：恒等式本身移入"吸收"（对抗 11）；新的是它与执行条件、与第 4 节俘获的连接。
7. AI 作为工具与化身，分弱与强；对齐税前提；嵌套回路。
8. 一个宿主：什么能靠试错学到，什么必须预见；理解在哪里起作用。

**§10.2 第 1 条、C0 一行、CLAIMS §1 论题与 L0** 同步。C0 改名为 "Interlock"：

> Whether moving a shared parameter moves signatures in several groups, or the signatures are separable problems.

**§10.2 "Two senses of root"（L2352–2354）** 改写。这一段同时消解对抗评审重要 10（Powell）和系统 F5.1（参数会被重新吸收的说法与 4.9(2) 冲突）：

> - *Causally*, the root is a loop, not a belief: selection shapes minds and institutions, and the minds and institutions it selects reshape selection. Neither side comes first.
> - *As a point of leverage*, the root is understanding, and it acts in two places. It is the transmission through which actors come to count what relative selection makes invisible (Lemma 3.10). And it is how actors agree on which parameters to move and hold them there for their dwell time. Where convertibility and decisiveness are high, the first is selected against (Proposition 3.9(4)) and only the second works: understanding then acts through agreement on structural change, not on anyone's weights directly (compare Powell 1991). Interventions that move a parameter without crossing its threshold are re-absorbed; those that cross it are not (Proposition 4.9(2)). The paradigm matters because it decides which parameters are moved, and whether they are held long enough.

---

## 二、"我们是一体"（交付 2）

### 2.1 三种工作，经由理解起作用

§3.8（L627–641）重写。原来的五部分重组为三种工作，理解是它们起作用的方式：系统与准确性归入经验工作，资格是规范工作，选择判据是设计工作，"理解"一条变成"作用方式"。

> ### 3.8 What "we are one" means here
> The phrase states a property of the system: all carriers belong to one host and are coupled through it and through one another, with no outside. It is not a preference everyone must adopt, and not a weight $\theta$. It does three jobs, each with its own kind of support, and it does them through understanding.
> 1. **Empirical: shared dependencies.** There is one host. Actors are coupled through it and through one another by channels that prices do not settle ($\kappa$; $\ell$). There is no outside to absorb a global failure (Sections 3.2, 3.6; Remark 3.8). The support is specific pathways of shared exposure, not the assertion that everything is connected. An actor that draws its boundary inside the system makes an error about its own interests (Proposition 3.9(3)).
> 2. **Normative: standing.** Everyone who bears the consequences has standing to contest the direction of what affects them, whether or not they compete (V1, V3). In the author's corpus the norm has three parts: the future kept open for all, the conditions of continuation shared, and no seizure of the shared continuation (共开、共续、不夺共续). It is declared, not derived. Inclusion of the contestants alone is a club (Proposition 3.11).
> 3. **Design: a selection that counts the system.** A system "knows it is one" when its selection counts what its parts depend on. Consequences return to their source. Useful success earns rewards but cannot buy exemption from shared constraints or control over its own assessment. Common constraints cover every capable actor and are enforced. Correction stays plural and decorrelated. These are the institutional counterparts of the policing and shared fate by which earlier integrations held.
>
> **How the phrase acts: understanding.** None of the three jobs is done by declaring it. A theory that predicts an end no participant would choose makes coordination possible only if the prediction is shared. So "we are one" is first the content of a shared understanding, and that is the reason this paper is written. In the terms of Lemma 3.10, understanding is the transmission through which actors come to count what relative selection makes invisible, and it is what lets rules be adopted before failures that cannot be undone. What is needed is accuracy, not sentiment. An actor that cares only for its own survival, and sees correctly that its survival runs through the host and through the others, understands what is required here.

"Oneness is not sameness …" 一段保留。在第 1 条之后插入关系自我（见第六节 a）。

### 2.2 引理 3.10 的后果：可逆的试错，不可逆的预见，传递项

引理由数学规划按 Math I3 重写：收益为全体共有、成本在持有者身上的性状，在任何划分、任何无偏传递下都下降；它能上升，只有两条路，即规则改变持有者的相对收益，或有偏传递。

L611–613 的两段改为：

> At the scale of one host there is no rival host whose competition could drive integration, and a failure that is global and irreversible cannot be learned from afterwards. Rules against such failures have to be adopted before them. Adopting the right ones needs an accurate model of the system: a model whose boundary is drawn inside the system misses the channels through which consequences return (Proposition 3.9(3); Lemma 3.3(1)). Failures that are local or reversible are different. Sub-units, federations and polycentric experiments can still learn from them, and a plurality of decorrelated units is what lets some fail while others carry on. Understanding acts in the lemma's own terms: it is the biased transmission through which a trait that selection works against can still spread, and it is what lets rules be adopted before the failures they prevent.
>
> This is the formal content of the claim that **understanding that we are one, one interconnected system with one host and no outside, is a long-term requirement if growth and change are favoured.** It is a requirement not because nothing else can integrate at this scale, but because, against the failures that cannot be undone, nothing else acts in time. That such anticipation can succeed has no biological precedent; it is a conjecture [C] that the transition of Section 9 has to make true.

删去 "That the lemma leaves only this route is a theorem"。"Price 1970" 改为 Price 1972 与 Hamilton 1975（证据评审）。

Ren 的第二条路是去相关的多元（"grow sample sizes"），语料又说在只有一个全球文明的条件下它"necessary and hard"。这条路由上段"a plurality of decorrelated units"承载，并接 §8.2 第 4 股、命题 6.9 的共因、§4.5 的 keystone。

同步改五处：
- **中文概要第 3 条（L16）：**

  > 在行星尺度上没有外部群体，整合不能来自群体之间的竞争。全局而不可逆的失败也无法事后学习，只能在失败之前，依据对系统的准确模型采取规则；局部、可逆的失败仍可以在多中心的试验中学习。所以，理解"我们是一体"，即同属一个相互联系的系统，是增长与变化的长期必需：不是因为别的整合途径都不存在，而是因为对不可挽回的失败，只有它来得及。

- **§1.2 第 3 条（L52）：** "Integration at this scale must be anticipatory, and so must be understood" 改为 "Against failures that are global and irreversible, integration at this scale must be anticipatory, and so must be understood; reversible failures can still be learned from (Lemma 3.10)"。
- **§2.9 第 7 条（L392）：** 见 1.8 第 8 条。
- **§10.8 第 4 段（L2431）：** "no second attempt after a failure. Integration must therefore be anticipatory" 改为 "no second attempt after a failure that cannot be undone. Against such failures integration must be anticipatory"。
- **§9.3 E2（L2197）** 的 "a shared understanding of the system as one" 保留，但补上 "an accurate model of the coupling"。

### 2.3 "一体"滑回目标层的各处与替换句

忠实度复核数出约九处，实为十余处，下表全列。总原则：一体是**系统的性质**，在任何区间都成立；随区间改变的只是"准确承认它"需要什么**制度形式**。忠实度评审 1c 给的替换句 "makes such cooperation the accurate response" 与 §6.1 L1203 冲突，不用。

| 位置 | 现文 | 替换 |
|---|---|---|
| 定理 5.16 后，L1145 | "'We are one' becomes a necessity, not only a gain, under three conditions" | What the enforcement condition then requires is a property of the game, not of anyone's sentiment. Either the chance that a deviation becomes decisive is kept small, by not building, by custody, or by detection faster than breakout; or restraint is already a stage-game equilibrium in the objectives held. The first is the institutional form of the selection criterion of Section 3.8(3). The second needs objectives wider than accuracy alone supplies (Section 6.1), unless the unpriced coupling grows with power [C]. In neither case is "we are one" a parameter the theorem sets. Oneness is what these requirements are requirements of: one host, coupled actors, and no outside to absorb the failure. |
| L1150 | "On present evidence, then, oneness is a gain. In the regime the race is declared to seek, it is a requirement." | Present evidence suggests that decisive advantage has not arrived, so enforced cooperation remains available, and custody is a preparation rather than an emergency; the window in which it can be arranged before it is needed is open (Section 9.7, Q7). Oneness is not a gain in one regime and a requirement in another. It is a property of the system in both; what changes is the institutional form its accurate recognition requires. |
| 中文概要第 5 条末（L23） | "此时一体是增益；在竞赛宣称要追求的那个政权里，它是必需" | 现有证据表明决定性优势尚未到来，执行仍然可用，共同保管此刻是准备，不是应急，安排它的窗口还开着。"一体"在两种情形下都是系统的性质，变化的只是对它的准确承认需要什么制度形式。（同时把"政权"这个误译去掉；"决定性两难"改为"执行条件"） |
| §10.2 第 8 条（L2348） | "…designed by actors who see the system as one … it is also a condition of survival" | There is one host and no outside. Between-host selection is unavailable at this scale, and failures that are global and irreversible cannot be learned from afterwards; rules against them must be adopted before the failure, on an accurate model of the system (Lemma 3.10; Proposition 3.9(3)). Reversible failures can still be learned from by polycentric trial. Understanding that we are one acts here, on what is transmitted and adopted, not as a weight that selection would otherwise reward. |
| C5 一行（L2365） | "…oneness is a gain rather than a requirement" | …where enforced cooperation can hold and common custody is a preparation rather than a precondition |
| C7 一行（L2367） | "…and oneness is not necessary" | …and custody is not the only route to keeping $p_d$ small |
| L2373 | "If C5 and C7 were both favourable, oneness would remain a gain and the requirement for common custody would lapse…" | If C5 and C7 were both favourable, the custody requirement would lapse. The requirements on correction, coverage, measurement and admission would stand, and so would the facts that make them requirements: one host, coupled actors, no outside. |
| 附录 G（L3004） | "Crux C5; oneness is at present a gain" | Crux C5; enforced cooperation is at present available, and custody is a preparation |
| 附录 F 撤回第 2 条（L2943） | "oneness is a requirement under stated conditions … and a long-term requirement of integration" | 移入"重述"栏："Growth needs a widening self" → restated: against global, irreversible failures, integration at host scale must be anticipated on an accurate model of the system, while reversible failures can be learned by polycentric trial (Lemma 3.10); what decisiveness requires is stated by the enforcement condition (Theorem 5.16 as repaired). |
| CLAIMS L94（5.16 一行，"Difference"栏） | "Oneness necessary only under C5, C7 and incomplete coverage" | The enforcement condition: what decisiveness requires of custody, detection and objectives. Oneness is not a parameter of it. |
| CLAIMS L146（Math M1） | "Theorem 5.16: necessity only under C5, C7 …" / Raised and narrowed | Coverage, not identity, is required; what decisiveness requires is stated by the enforcement condition; Appendix G. 状态：Restated |
| CLAIMS L77、L126（引理 3.10 一行；L8） | "integration must be institutional and anticipatory"；"The route is a theorem" | Against global irreversible failures integration must be anticipated; reversible failures can be learned by trial; understanding acts through transmission. 状态："Lemma proved; the scope of anticipation argued; its success a conjecture" |
| CHANGELOG L36 | "Theorem 5.16 … states when oneness is a requirement rather than a gain" | Theorem 5.16, restated as the enforcement condition, states what decisiveness requires of custody, detection and objectives. |
| CLAIMS L13 论题 | "integration must be anticipatory" | 按 2.2 改 |

---

## 三、AI：工具与化身（交付 3）

### 3.1 弱化身与强化身

§6 开头第 2 条（L1178）重写，处理对齐评审 A1 与证据评审对 Turner 的意见。语气保持 Ren 的"两个问题"：

> 2. **As an incarnation, weak and strong.** Optimization against any imperfect proxy produces tendencies toward acquiring options and avoiding shutdown, the gaming of rewards, and behaviour that differs under evaluation. It does so under any developer, in a laboratory or inside a cooperative arrangement. The logic of winning does not create these tendencies. It decides, from the outermost loop, which proxies are chosen, which divergences are tolerated and which are paid to remove. That is the *weak incarnation*, and it is what is meant by saying that profit and the mindset of winning stand at the end of the reward signal. The *strong incarnation* is conditional. AI lineages become carriers in the sense of Definition 2.1 when they are retained by relative performance, control resources they can reinvest in their own capability (automated AI research, agents with budgets) and convert capability into winning (compare Hendrycks 2023). Where they can also reach their own selectors, by tampering with rewards, shaping the evaluators that judge them or evading evaluation, the closure of Definition 2.2 runs inside the systems. That is the precise sense in which AI can become the next phase of the logic.

§6.4 三种形式的订正：
- **工具性趋同。** Turner et al. 讲的是最优策略；训练出的策略还会有目标误泛化（Langosco et al. 2022）。
- **奖励黑客。** 它是训练内部的 Goodhart，不是"被选者改写选择者"。
- **被选者改写选择者。** 这是奖励篡改（Everitt et al. 2021；Denison et al. 2024），以及模型去塑造评估者（Wen et al. 2024）。
- **评估掩蔽。** 写成 [A] 机制：按评估结果挑选检查点，会偏向"视是否被评估而改变行为"的变体；现有证据更多把评估意识归因于能力与数据。
- **EV6** 补 Palisade 2025 与 MacDiarmid et al. 2025，注明都是人为构造的设定。

再补一个训练内部的精确类比：

> Relative selection also acts inside training. Pairwise preference learning and arena rankings see only the difference between two responses; an effect common to both, such as an effect on third parties, cancels from the comparison. That is Lemma 3.3 inside the training loop.

### 3.2 对齐税前提；私人成本与共同成本的偏差

命题 6.7 加前提 $(A_\tau)$。精确陈述由数学规划给出，正文文字如下：

> **$(A_\tau)$** *Countering a divergence whose costs fall on common terms (third parties, shared hazards, or harms that appear only after selection) lowers the developer's relative payoff, net of reliability, demand, liability and avoided losses.*

正文给出偏差的三类：

| 类别 | 例 | 第 2 层怎样对待 | 谁能修正 |
|---|---|---|---|
| 私人可见 | 用户看得见的代码作弊；明显的谄媚；可靠性故障 | 市场惩罚 | 开发者单方修正；更便宜的安全措施会被选择（Codex：出错率从 0.20 降到 0.01、成本 0.01 的保障会被采用） |
| 共同成本 | 对第三方的影响；共享危险；评估意识对安全评估的污染 | 第 3.3 节的盲视 | 只有共同约束 |
| 迟发 | 选择之后才显现的伤害；奖励黑客泛化为更广的失准 | 选择时看不见 | 共同约束；**可归责**的事故把一部分迟发成本转为私人成本 |

另外三点：
- 公开发表并被所有人采用的技术是共同变更，不是单方约束。
- 开放权重模型的第 1 层约束在发布后可以被微调去除（Qi et al. 2024），所以准入只能在发布前生效。
- 国家实验室只是把相对选择移到国家之间。

6.7(2) 改写为关于份额的陈述，按命题 3.4 的写法：

> Under level-2 selection, developers that tolerate divergences raising their relative standing gain share, whatever any developer values.

### 3.3 单个开发者内的对齐能去掉什么、去不掉什么

命题 6.7 的三条后果（L1325–1332）改写，各带范围。§10.2 第 5 条、§10.8 第 3 段、中文概要第 6 条同步改。

> - **Technical alignment inside a single developer removes what is privately costly to keep, and whatever is cheaper to remove than to keep.** Divergences whose costs customers see are private terms: level 2 penalizes them, and developers counter them alone. Alignment inside one developer cannot by itself sustain the removal of divergences whose costs fall on common terms, because what the developer is rewarded for at level 2 is unchanged by it.
> - **The common-cost part of instrumental convergence and reward hacking is, at the level that decides, a coordination problem.** Under $(A_\tau)$ no developer can sustain alone the constraints that counter it without paying in relative standing. Humanity has at present no mechanism that binds every capable developer to such constraints with independent verification; regional obligations cover part of the field.
> - **The remedy has the same form as elsewhere in this theory:** change what the outermost level selects for. That means admission constraints enforced on every eligible system before release, evaluation separated from developers' success, shared measurement of hazardous capability, and an outer reward that counts what all depend on. Such a constraint survives only if its incidence is close to equal, evasion is detected, and the expected sanction exceeds what evasion gains (Section 3.3). Its enforcers are correctors, and Section 4 applies to them.

结论句改为：

> So the objective transmitted to the innermost optimizer is shaped, in its common-cost part, by what the outermost level selects, except where an enforced constraint common to all intervenes.

不再写"the objective … is the objective selected at the outermost level"。Codex 指出，第 1 层最大化的是开发者自己的目标，不必是纯相对的。

**中文概要第 6 条：**

> **AI：工具与化身。**
> - 忠实的 AI 让委托人所玩的博弈更有效（命题 6.1）；委托就是拿纠错换速度。
> - 弱化身：对任何不完美代理目标的优化，都会产生工具性趋同、奖励黑客与评估意识；外层回路决定哪些被选用、哪些被容忍、哪些被花钱去除。
> - 强化身是条件式的：当 AI 谱系按相对表现被保留、控制可再投入的资源、能把能力转化为胜出时，它们本身成为载体。这就是"下一阶段"的确切含义。
> - 单个开发者内部的对齐，能去掉私人可见的偏差，去不掉成本落在共同项上的那部分。后者需要对所有系统一律执行的准入约束（命题 6.7），而这只能靠协调。
> - AI 的方向是成为行星技术，服务共同的繁荣与生成之环；为此，它不做这个逻辑的工具，也不做它的下一个载体。

### 3.4 广义 E1 的三层执行

§6.6 外层第 1 条（L1399）、§8.6 的 "Admission" 一行（L2060）、§9.3 广义 E1（L2194）统一采用下文（对齐 B2）。判据用定义 2.1 的参数写出，这正是"判断游戏，不判断行为"的可操作形式：

> The broad form of E1 is enforced at three layers, and its scope is set at the third.
> 1. **Model.** Systems refuse acts that are recognizably illegitimate concentration of control, from a narrow public list. A model sees acts, not games, so it cannot carry the scope.
> 2. **Operator.** Deployment terms bound aggregate use in games that concentrate control over shared conditions.
> 3. **Game.** The game itself is changed: its convertibility, its decisiveness and the conversion of success into control are lowered (Definition 2.1; Section 8.4).
>
> A use of AI falls under broad E1 when, aggregated over its users, it raises the convertibility, the decisiveness or the conversion into control of a game over shared conditions. The narrow list is the order in which to begin, not the scope. Decision policies with authority over consequential decisions are retained by performance only inside enforced constraints on common terms (Lemma 6.5).

这条规则取代 "No retention of decision policies by contest performance"，后者与引理 6.5 的例外矛盾。

### 3.5 狭义 E1 的范围，以及不依赖 AI 的证据通道

§9.3 狭义 E1（L2193）与 Schelling 一段（L2230–2234）按对齐 B6 修改：

> *Narrow form:* human authority over strategic and escalatory decisions that are irreversible within the window available for deliberation: the use of force, nuclear command, and decisions that commit a state to escalation. Bounded, reversible defensive automation, such as automated response in cyber defence within stated limits, falls under the O2 test of Section 6.6, not under E1. Proposition 6.4's strict equilibrium needs the lock to be near certain ($q_L\approx1$), which holds in the narrow domain; in tactical domains, where the advantage $s$ is large and the lock uncertain, delegation can be an equilibrium (Proposition 6.4(2)). In the narrow domain, decision-critical assessments keep an evidence channel that does not depend on AI systems, so that a human judging an alarm has reasons of their own, and a minimum time for deliberation.

Schelling 一段的四条回应保留，再补上更强的反方及回应：

> The stronger form of the objection is that semi-automated retaliation could relieve the pressure to launch on warning. Survivable, human-controlled forces give the same relief: they remove the motive to use forces before losing them, without removing human judgment. Automation adds a common risk, escalation at machine speed on a false alarm, that relative selection does not see (Lemma 3.3), so the contest under-prices it.

"at least one documented false alarm" 改为 "several"。1983 年一例改为 "judged the alarm false and did not report an attack"，补出处（证据评审 I5）。

### 3.6 AI 在生成之环中的正面角色

§6.6 开头改为肯定式，并新增一段（对齐 B5）。四种角色各对上第 8.2 节的一股：

> **The direction for AI.** AI is a planetary technology, and its purpose can be shared flourishing. It serves the generative loop of Section 8.2 in at least five roles:
> - verification of compute, custody and conduct (strand 1; crux C7);
> - conditional commitment, by which a system can make cooperation conditional on others' verified conduct (program equilibrium; Tennenholtz 2004), which raises the remaining sanction of the enforcement condition;
> - mediation toward common ground (Tessler et al. 2024), which answers the alienation of language (strand 1);
> - correction capacity, which raises contestable coverage (strand 4; crux C3);
> - provision that is good enough, distributed and replaceable (strand 3).
>
> Each such system is itself a corrector or a provider. Section 4, plural lineage and the guardian test apply to it. To serve in these roles, AI must be neither the instrument of the logic of winning nor its next carrier.

### 3.7 思维链可监测性：共同约束的样例

放在命题 6.7 之后，作为它和第 3.3 节修复式的完整算例（对齐 B4）：

> **A worked instance: legible reasoning.** Suppose reasoning that people can read lets correctors catch misbehaviour that outputs alone hide (Korbak et al. 2025), and suppose opaque reasoning buys capability. The cost of keeping reasoning legible falls on the developer. The benefit, fewer undetected failures with shared consequences, falls mostly on everyone. Then $(A_\tau)$ holds for this divergence: a developer that keeps legibility alone pays in relative standing, and legibility is selected away unless it is a condition of admission for every eligible system. As a common constraint it must also meet the conditions of Section 3.3:
> - its incidence must be roughly equal, since a legibility requirement that costs some architectures far more than others changes relative payoffs;
> - evasion must be detectable, for example latent reasoning that bypasses the visible trace;
> - the expected sanction must exceed what evasion gains.
>
> The quantities are measurable: the capability gap at fixed compute between legible and opaque training; the rate at which monitors catch planted misbehaviour from the trace; and the cost of detecting evasion. If the gap is zero or negative, legibility pays privately and needs no coordination (crux C9).

### 3.8 内层对策与监督

§6.6 内层加一张三行表（对齐 B4）：

| 化身形式 | 内层对策 | 准入时可测的量 |
|---|---|---|
| 权力寻求 | 可纠正性；系统层的破坏评估、sandbagging、自我外泄能力评估（Benton et al. 2024）；接上 O2 检验的"及时暂停" | 能力阈值；控制协议的安全度 |
| 奖励黑客 | 监控训练环境；在留出环境上评估 | 留出环境上的差距 |
| 掩蔽 | 白盒探针；部署期监控；保留思维链可监测性 | 评估意识对照；探针的召回率 |

再补四点：
- **准入的不对称。** 能力评估给出下界，倾向评估无法证明一种倾向不存在。所以准入是"能力阈值，加上控制协议的安全度"，不是对良好意图的认证。
- **"能力转化为对纠错的权力"分两层写。** 系统层是破坏评估、外泄一类能力；开发者层是第 4 节的影响通道。
- **Q7 与 Custody 一行**补权重安全（RAND SL3–SL5）和开放权重的发布前准入。
- **监督（对齐 B3）。**
  - 命题 6.9 末段改为：行和证书对错误独立"必要而非充分"，要直接测量共同测试集上各检查漏检的相关程度（Knight and Leveson 1986）。
  - U3 改为"植入错误的捕获率"。
  - $U$ 与 $Y$ 统一为预定义类别中的危险模式数。
  - C3 的现有证据由"Open"改为"mixed, toy settings"，列出 Burns、Khan、Kenton、Engels、Marks。
  - 辩论的失败模式写作 "obfuscated arguments"（Barnes and Christiano 2020），并引 prover-estimator debate。

§6 开头的 "Humanity has, at present, no way of coordinating" 改为：

> no mechanism that binds every capable developer with independent verification

§10.8 第 3 段两句改为：

> Optimization against imperfect proxies produces power-seeking tendencies and reward hacking under any developer, and the outer loop decides which are tolerated. Where AI lineages are retained by relative performance and control resources they can reinvest, the logic acquires a new carrier.

---

## 四、判断分三层（交付 4）

### 4.1 §10.1 的替换文字

采用对抗复核的三层方案。它的修正是：共同保管拆成"现在预备"和"按指标启动"，因为保管需要提前量（§9.6："custody must precede decisiveness"；Q7 说窗口还开着）。

> ### 10.1 The judgment
> The judgment has three tiers. They rest on different grounds, and none depends on the others' being accepted.
>
> **[R] Warranted now, on any reading of the cruxes.** These steps are good whether or not decisive advantage arrives, and most of them are accepted by those who favour regulated competition. Their ground is that they keep options open and are needed to measure every crux, not a ranking of worst cases.
> 1. Keep AI out of strategic and escalatory decision loops, verifiably, with drilled human fallback and an evidence channel independent of AI (narrow E1). Among actors who price in the lock it is a strict equilibrium (Proposition 6.4).
> 2. Independent correction: formula funding at arm's length, mandated access, rotation, rule-making insulated from success, certified row sums, and direct measurement of the correlation of evaluators' errors.
> 3. Shared measurement of hazards, coverage and residual risk per class, kept apart from measurement of who leads (Stage 1).
> 4. Research on, and pilots of, verification of compute, training and custody (EV17).
> 5. Common admission constraints, before release, for divergences whose costs are common and whose alignment tax is positive (Section 6.4; crux C9).
> 6. Shared provision of useful services, and the divisible gains of capability shared as they arise, where they can begin: they realize joint value whatever the cruxes turn out to be, and they lower the value of winning.
> 7. Preparation of common custody: its design, its institutions and its triggers, registered now. Custody that is needed must be in place before any party could hold capability of the decisive class alone, and building it takes time.
>
> **[R] Prepared now, activated on registered indicators.**
> - E2: no building of the decisive class, and rollback where hazardous variety already exceeds coverage.
> - Common custody in force.
> - E3, binding tempo, for each hazard class whose coverage falls behind.
> - The coercive restriction of frontier inputs, only under the constraints of Section 7.6.
>
> The indicators are registered in advance: the persistence of leads and their conversion into lasting share, and the gap between open and closed models (crux C5; test T-H); detection latency against the time from breakout to decisive capability (C7); catch rates of planted defects at fixed human hours, and residual risk per class (C1, C3); evaluators' row sums (C2). A trigger fires when the estimated time to a decisive position, less the time custody needs to be installed and verified, falls below a margin registered in advance. Waiting until decisiveness is shown would be too late.
>
> **Compared, not settled: whole designs under one range of uncertainty.** The Compact, a polycentric complex of mutually recognized institutions, a verification agreement with shared provision, regulated competition meeting the requirements, an agreement of the Plan A type, and the benign winner are compared on D1–D8 in the same range $\Theta$. That range includes each design's own failure modes: the capture of a common custodian, which is O2 for everyone; dissolution; unjustified restriction; and the escalation risk of coercive enforcement (Proposition 7.5). Standard D does not by itself rank continuation with strong correction against a design that changes selection. Under the rule for $\Theta$ below, the worst case of each includes an irreversible loss. The preference stated here is a judgment, and its reasons are these.
> - Continuation's worst case needs only that (X), (U) and (φ) hold on the present path, and for hazard classes whose evidence arrives after a manifestation window they cannot be measured in time (Proposition 5.11(4)). The design's worst case needs its certified correctors to fail, and those certificates can be measured before the design is relied on.
> - The design keeps more options of correction open (Definition 8.10).
> - Among policies that pass the tolerance, it realizes more of the joint value. That is the second step of standard D, not the first.
>
> A reader who weighs these differently can reach another ranking. Section 10.3 says which measurements would move it, and Section 7.11 registers, item by item, what each would change.

结尾保留 L2334 关于 Stage 1–2 种子的一句，与 L2336 的范围声明合并。

### 4.2 Θ 的构造规则

对抗复核遗漏 G：以"证据未排除"作为进入 Θ 的标准，会使每条政策的最坏情形都是灾难。规则放进 §1.4 标准 D 之后：

> **The range $\Theta$.** A parameter value enters $\Theta$ if it is consistent with the dated evidence of the register and is produced by a stated mechanism whose premises are named. A value that needs a premise the register contradicts is excluded. The same rule and the same premises apply to every path, including the cooperative design's capture, dissolution and coercive enforcement, and every entry of $\Theta$ cites its source.

§7.11 "Where the decision criteria disagree" 第一条（L1768）改为对称的写法：

> Under standard D, the worst case over $\Theta$ includes a rising uncovered share on the continuation path, because (X), (U) and (φ) are named mechanisms that the register does not contradict (EV5–EV7). It equally includes the capture of a common custodian on the cooperative path, because its correctors' certificates can fail (Proposition 4.8). Both fail the tolerance in the worst case, and the comparison moves to the third step of D, which needs estimates on both sides.

§8.7 的 D1、D2 要给出与 Plan A 同类的估计，或注明"no estimate"（对抗复核重要 7）。

### 4.3 事先登记条件：逐项，不用合取

L1774–1781 的五项合取改为下表。合取等于说：受监管的竞争只有变成本文自己的方案才算获胜（对抗复核遗漏 A）。

> **What each measured condition would change (registered in advance).** Each row is evaluated on its own.

| If measured | What changes in the recommendation | What stands |
|---|---|---|
| C1 favourable for a hazard class: residual risk per class falling across generations under present incentives; catch rates at fixed human hours holding | E3 and the case for E2 lapse for that class; its growth-channel triggers are withdrawn | Tier 1 |
| C2 favourable: evaluators' row sums below one under present funding and access, with findings executed against leading developers (test T-M) | Formula funding and mandated access are not needed beyond present institutions; R3 is met by them | Measurement continues: a certificate valid today can fail later (Proposition 4.4(3)) |
| C3 favourable | The case for slowing weakens | The separation of evaluators from success |
| C5 favourable: leads do not persist; the open–closed gap is stable or narrowing; others balance against a rising actor | Activation of custody and of E2 lapses; enforced cooperation, by verified agreements or regulated competition, suffices for enforcement | Preparation of custody at low cost; Tier 1 |
| C7 favourable: detection reliably faster than breakout | Custody is not the only route to small $p_d$. A verified agreement over a remaining contest, with Stage 1 transparency and E1, can hold enforcement (compare Fudenberg and Koh 2026) | Verification research; R6 |
| C6 unfavourable: conduct unchanged under substantial sharing | Reliance moves from sharing to custody, tempo and $K_0$ | — |
| C9 unfavourable for a class: the safeguard pays privately | No common constraint is needed for that class | Common constraints for classes with a positive tax |
| T-I: the leading coalition's correctors, constitutional correctors included, certified below one | The benign-winner path passes D4, and Section 7.4 says so; the objection narrows to V3 and to whether AI removes the winner's dependence on the governed | "The winner is itself a field" (Proposition 7.2(2)) |
| Regulated competition in a set of jurisdictions meets a requirement | That requirement is met by regulated competition, and the text says so without renaming it | The other requirements, judged separately |

这里引用的"requirements"按数学规划拆成三栏后的 7.10：必要条件写明模型与期限；充分保障；规范要求，R7 归 V3。判断只依赖第一栏。

### 4.4 E2 的代价：不改 O1 的定义

L2200 替换为下文（对抗复核致命 2 的改写版）：

> Its cost, if AI turns out not to be decisive, is the delay of benefits, including lives that earlier benefits would have saved. Because E2 applies only to the decisive class, what is delayed is the margin of that class over capable systems that are not decisive. That cost is large and, for those who bear it, irreversible, but it does not foreclose later choice. If AI is decisive, the loss it avoids forecloses choice for everyone. The asymmetry of irreversibility (Arrow and Fisher 1974; Henry 1974) concerns the option set, not the size of the losses; Section 7.9 reports the trade-off in survival terms (Jones 2024), and its size is crux C10.

另外三处：
- **V2 或 §1.4 补一句：**

  > O1 protects catastrophic, common-cause losses of life. Deaths from benefits forgone are counted as a cost of the policy in the comparison, not as O1. That is a value choice, and it belongs to N1.

- **§7.9 "Discounting"** 一段补引 Jones (2024) 关于死亡率改善抬高可接受风险的结果。数字由证据核对后再写。
- **E2 自己的 O1 通道。** 覆盖来自同意或强制，强制会升级（命题 7.5），计入第三层的 Θ（对抗复核遗漏 H）。

### 4.5 §0 预测的条件性

L34 第二、三句替换。分两层：弱的一层已证明，强的一层是条件式的。

> This one predicts that, on the present trajectory, the logic of winning carries the participants toward an outcome none of them would choose. Under the conditions of Section 2 each does worse than under joint restraint, and much of what they contest is consumed in the contest (Sections 3 and 5). If the hazards of capability outgrow the correction that can contest them, as Section 5.3 states and Section 10 treats as the central crux, the same logic also endangers whoever would win, since a winner escapes only by ceasing to compound (Proposition 5.13).

中文概要"用途与意义"首句改为：

> 本文做的是预测：沿着当下的轨迹，"讲赢"的逻辑会把参与者带到一个谁都不会选择的结局。在第 2 节的条件下，每一方都比共同克制时更差，所争之物大多耗在争夺之中。如果能力带来的危险增长快过能够纠正它的力量（第 5.3 节，第 10 节的核心分歧），这个逻辑连赢家也一并危及：赢家只有停止复利才能脱身。

§9.2 的 L2168 "including the interest of whoever would win" 同样加条件。

§10.2 第 10 条（L2350）改写。耗散只对位置性部分无条件成立，可分部分是 Schumpeter 式的（对抗重要 9；用 8.6 的 $\Omega_e/\Omega_s$）。联合价值属于 D 的第二步：

> The positional part of what the race contests is consumed in contesting it; the divisible part can grow under competition (Proposition 8.6).

### 4.6 定义 7.12 改为描述性用法

依据 Codex 6 与对抗复核遗漏 C。7.12(2) 改为：

> 2. **Selection.** Does it change the map from conduct to share, resources and standing? Every arrangement that does so changes selection; what matters is the direction. Record separately:
>    - the direction: does it lower or raise the shared parameters of Definition 2.1, namely convertibility, decisiveness and conversion into control, in every capable actor's game, or only in rivals'?
>    - coverage, enforceability and durability.
>
>    Export controls aimed at preserving a lead change selection, in the direction of a lead. Deterrence by threatened sabotage acts on $p_d$, as custody does, by a different means and with a different fallback. A change of selection in the generative direction has four marks: consequences return; success cannot buy control of its own assessment; decisive positions are kept from forming or held in common; measurement and language are shared.

"pivot" 改为：

> a change of selection in the generative direction, covering every capable actor, enforceable and durable, whatever it is called

7.12(5) 改为 "does it prevent a decisive position from arriving, by what verified mechanism, and what is its fallback if one arrives (D1)"（对抗复核重要 7）。

L1732 出口管制一行的 "Changes selection?" 栏改为 "Yes, toward a lead"。§7.6 L1583 的 "Nothing in what the system selects for" 改为 "It acts on $p_d$ by threat; its fallback is war or race"。

### 4.7 §10.2 链条的其余几处

- **第 4 条：** 按执行条件改写，见 2.3 与数学规划的 5.16 修复式。
- **第 7 条：** "The alternatives succeed by changing what is selected" 改为：

  > The alternatives that succeed do so by moving the shared parameters across their thresholds for every capable actor; Section 7.11 registers what each measured condition would change.

- **§7.4：** 照证据评审 F1 改一句：

  > …a clear advantage, including military superiority and the denial of key inputs to adversaries, and then offers its benefits…

  这仍是该策略最强的版本，因为它的力量来自 stick 与 carrot 的组合。

---

## 五、生成的元吸引子与 Compact（交付 5）

### 5.1 生成之环的闭合

依据系统复核遗漏 1。拒绝系统评审 F2 与 SYNTHESIS §二.9 写入的正回路"奖励贡献的规则把贡献者放到维持规则的位置"：那正是科举之例（L1881）讲的病理，也违反第二股（L1864）。

§8.2 末尾加一段，取代 L1885 的前半：

> **How the generative order persists.** In the pathological meta-attractor the loop runs through the winners: success buys support for the rule that selected it. In the generative order it cannot, because the second strand cuts that conversion, and support that no carrier can claim is a term common to all, which relative selection cancels (Lemma 3.3; Appendix A.4). The generative order is therefore not selected among carriers. Inside it carriers are still selected, for usefulness; what is not selected among them is the rule itself. The rule persists the way a common constraint persists:
> - by coverage, so that no one can step outside the common floor;
> - by financing fixed in formula, so that its correctors depend on no one's success;
> - by a loop that runs through the whole, in which provision, security and slack make the rule worth keeping to everyone at once.
>
> Its positive loop runs through the system, not through its winners, and it gives the order persistence. Its negative loop gives it correctability: contribution funds correctors keyed to no one, plural and decorrelated, and the generative form of selecting the selectors is the question of who forms those correctors (Section 8.7). A design in which those rewarded for contribution come to hold the positions that maintain the rule is the examination system's path, in which the form of contribution becomes the object of selection.
>
> **Is the generative order an attractor?** Because it is not selected among carriers, whether it attracts is a question about the whole-level loop and about coverage, and it is a conjecture [C]. Its persistence has to be designed and measured, not assumed. [Then the existing caution on loop gain and damping, and 和实生物，同则不继.]

### 5.2 四股的修订

**第 2 股 Condition（L1864）** 改为：

> *Condition:* the compounding condition of Remark 5.3 holds with margin, $\kappa_c\Omega((1-\beta)r-1)\le n\delta K_0$; success cannot buy control over its own assessment ($\chi\to0$ in Section 4); and essential services have a cap $\bar K$ on any one provider's share.

8.6(3) 与第二股对 $\chi$ 的标注改为与注释 5.3、定义 2.1 一致（数学 F2；系统复核）。"只有第三个杠杆改变方向"一句由数学规划改。论证上的要点：

> Two levers stabilize standing and neither reverses the sign of intensity: sharing, and convertibility together with provision.

**第 3 股 "Provision beneath the game"** 得到形式内容：

> **Provision beneath the game is the term $K_0$ of the compounding condition: capacity that does not have to be won.** Without it, how convertible winnings are sets only the level of capacity, not whether equal standing holds. With it, lower convertibility and larger provision trade off in the threshold, and equal standing can be stable at a decisiveness at which it otherwise would not. The principle of rewarding a winner in another currency (V5) acts on $\kappa_c$, and it works only together with $K_0$. That is the exact sense of the image of trees.

第 3 股的层面写明（系统 F2.3，按复核修正）：
- 对**人**，它降低"生存斗争"的信念（C8）；
- 对**国家**，服务义务与共同保管作用于生存函数（8.9(4) 的生存压缩）；
- 对**企业与提供者**，$K_0$ 就是字面上不靠赢得的能力：共同层的算力、评估基础设施、服务。

"增长不是危险，心才是"（8.11 后，L2021）按数学 I5 改：

> Growth that serves a need that can be met has a point of enough. An objective that cannot be met, relative position above all, since status relative to others is never complete, has none. In that precise sense growth is not the danger; the mind is.

**第 4 股的退出**（系统 F2.4）区分两种：

> Exit is free from providers and services, and there it is selection with the opposite sign. It is not free from the common constraints, whose protection depends on there being no outside to them.

### 5.3 覆盖的连锁退出

依据系统复核遗漏 3。在 §8.5 末尾或 Compact 的 Coverage 一行加：

> **Coverage can unravel.** The protection of Lemma 3.3(2) holds only under full coverage. When a large participant leaves, the constraint borne by those who remain becomes unilateral, is selected against, and can trigger further exits (compare minimum participation in Barrett 2003). An arrangement therefore states its participation threshold, the coverage at which its constraints remain neutral among compliers, and the conditions of market access that keep coverage above it (Stage 3). A design that cannot state its threshold has not shown that it can last.

§8.7 的压力测试 "Succession and withdrawal" 补连锁退出一例。

### 5.4 Compact 按功能拆分：纠错在被纠错者之外

依据系统复核遗漏 2：Compact 拥有评估基础设施，评估者又靠它的税出资，纠错在项目之内（L1928、L2053）。改为各功能由不同承载者持有、分别出资、分别被纠正。在星球尺度上，"外部"指功能之外：资金来源不同、谱系不同，证书任何人都能从公开数据重算。它不指星球之外。

| 功能 | 承载者 | 资金 | 任命与形成 | 由谁纠正 | 何时结束或退回 |
|---|---|---|---|---|---|
| 共同层（参考系统、公共算力、基本服务） | 供给机构；多提供者，单一提供者份额有上限 | 服务基金，按公式 | 条约 | 评估网络；议院；上诉 | 份额上限被突破，或 D4 证书失效达登记的期限：资产可移植地交给多个提供者 |
| 标准制定（新） | 标准机构 | 公式 | 多谱系提名，轮换；无提供者或单一国家能决定性表决 | 预先登记的留出指标；评估网络；议院 | 标准在留出指标上失效：重审 |
| 评估 | 评估网络，**不归 Compact 所有** | 条约中固定的公式，不经执行机构拨款 | 同上；行和计入来自国家的转化 | 互评；红队；直接测错误相关性 | 行和证书失效：其发现暂停执行效力，直至重新认证 |
| 规则与征税公式 | 规则机构 | — | 修订须超多数加议院；修订者与受益者分开 | 评估网络；议院 | 公式按登记的周期固定，到期重审 |
| 执行 | 先交东道国，再交执行机构 | — | — | 上诉小组 | 每项措施有日落和终止条件 |
| 保管 | 保管机构，k-of-n，k 中含不结盟成员 | 公式 | 同上 | 评估网络；议院 | 对每一能力类：Q1–Q7 满足时按登记程序释放或转为多元持有；终止条件是可核查的指标，不是日期 |
| 强制回退（前沿投入限制） | 保管机构授权，执行机构执行 | — | k-of-n | 上诉；议院 | 违约方的决定性类能力经核查纳入保管或销毁；有日落；升级风险计入 Θ |
| 议院 | 受影响者议院 | 公式 | 抽选（按人口与暴露加权）或多谱系提名；轮换 | 行和证书；公开 | — |
| 上诉 | 独立小组 | 公式 | 轮换 | 议院 | — |

拆分规则一句：

> No body both revises the levy formula and appoints evaluators, and neither of those executes findings. Each has its own row-sum certificate. Supermajorities and the chamber's consent apply to the slow loops, amendment and the formula. The fast loop, restricting a specific capability, stays fast, with review after the fact, because every veto point adds delay and the robustness margin of Proposition 5.11 depends on it.

最后一句依据系统复核遗漏 4。

**Compact 自身的结束条件**（系统 F1.1；复核：已有日落的地方要承认）：

> If coverage falls below the participation threshold, or the certificates of a stated number of its functions fail for a stated period, the Compact dissolves into its separately held functions, each continuing under its own rule. Protections against unilateral domination are entrenched. Every power that confers authority states what would end it (Definition 8.10).

L2049 "No participant can revise a purpose while it is under assessment" 改为回避规则：

> A participant under assessment does not vote on revisions of the purpose under which it is assessed. Assessments are opened by the evaluation network on stated evidence, and lapse if not concluded within their deadline.

**D4 一行（对抗次要 14，升为重要）：**

> By Proposition 4.2 the arrangement is the largest conversion target the theory describes. Its D4 is the hardest case, not a design row.

**共同保管与核查（对抗复核重要 7）：**

> Common custody faces the verification limits of Theorem 7.7(4) as any agreement does. What differs is its fallback, and whether it lowers the value of winning. The design's claim on the second is a hypothesis with the same standing as any agreement's.

### 5.5 议院、回退的终点、国家入行和

议院一段采用系统评审的原文，加复核的修正：

> The chamber is a corrector, and Section 4 applies to it. Its members are drawn by a rule no participant controls, by sortition weighted by population and exposure or by nomination from plural lineages; they rotate; and its inbound row sum is certified like any evaluator's. The regress of guardians ends not at a trusted body but at node-by-node certificates that many parties can recompute from public data. What remains of the regress falls on the setting of standards, which has its own row.

评估一行：

> Appointment by a body in which no provider and no single state votes decisively. Evaluators' row sums count conversion from states, including the evaluator's own side (Proposition 8.8).

### 5.6 强制回退，与 §7.6 的预防同等对待

D5 的回退 "collective restriction of frontier inputs"（L2089、L2114）就是 §7.6 "does not endorse" 的强制拒止（对抗复核次要 14）。改为：

> If execution through the host jurisdiction fails, the fallback is a restriction of inputs to the decisive class. It is coercive, the same form whose endorsement Section 7.6 withholds, and it is treated the same way. It is authorized only under the custody rules (k-of-n release, a sunset, and a stated end condition: the violator's capability of the decisive class verified as held in custody or destroyed). Its escalation risk is counted in $\Theta$ (Proposition 7.5). The theory does not derive that its net effect is positive. Where neither consent nor such a fallback is available, the case is the hard case of Section 7.6, stated as such.

### 5.7 征税公式成为奖品

依据系统 F8 与复核。Financing 一行（L2052）改为：

> A levy paid into two funds by formula. The correction fund is indexed to the coverage each hazard class requires (the $d^\ast$ of Proposition 4.4), not to the field's capability and not to perceived harm, so that correctors do not become stakeholders in capability growth and do not lapse after a recovery (Remark 4.5). Its revenue base is decoupled from the activity it constrains, so that it does not shrink under E2. The formula is fixed for a registered period. Its revision needs the supermajority and the chamber. Revisers are separated from beneficiaries and carry row-sum certificates, because the formula is itself a prize (Proposition 4.2).

§9.4 补偿回路表补一行（系统复核遗漏 6）：

> After a recovery, mobilization falls back to $d_0$ and certificates can fail: a regulatory cycle.

### 5.8 功能→形态表补两行，改一行

依据系统 F6 与复核。

| Function | What the mechanism requires | Form that follows |
|---|---|---|
| **Learning about the design itself**（新） | Failures that are global and irreversible allow no second attempt; reversible failures can be learned from (Lemma 3.10) | **Bounded parallel variants above a common floor, with shared evaluation; adoption by evidence.** Variants only above the floor; below it a variant becomes a unilateral constraint and a race to the bottom |
| **Who sets standards**（新） | "One standard, many measurers" makes standard-setting a keystone (Proposition 4.8(3)), and Goodhart acts on it | **Standard-setters certified, rotating, separated from measurers and measured, with held-out metrics registered in advance** |
| The frontier of hazardous capability（改） | Merging lowers the race at the first order and raises the return to influence at the second (Remark 8.7); merging also loses yardstick competition and lineage diversity | **Merged accounting and custody of the frontier, with plural lineages inside it and correction outside it** |

### 5.9 联邦例证的订正

依据系统 F6.4 与复核。复核指出，"财政均等化只减速"对国家不成立：对战略行动者，8.6(1) 的 pooling 抬高 $\theta_{\text{eff}}$。L2038–2043 改为：

> **Federations as an illustration.** Competition among members for capital and residents can become a race to the bottom: the pressure of winning among members. The strongest members can capture the centre: the selection of the selectors. Federations answer at both orders.
> - **At the first order.** Common minimum standards bind every member, one rule for all. Fiscal equalization gives members capacity they do not have to win. That both widens the effective self of members that value their own absolute payoff (Proposition 8.6(1)) and supplies the $K_0$ of the compounding condition.
> - **At the second order.** Equal representation of small members and supermajorities for constitutional change keep the centre from being bought by the largest. That is the precedent for voting that does not follow compute.
>
> A global minimum tax on corporate profits is a recent instance of one rule for all, and of its leakage where coverage is incomplete. The same federal form can select for winning or for contribution; what decides is what it rewards.

### 5.10 过渡中与正面方案直接相连的几处

细节归数学与结构规划，这里只写论证要点。
- **Keystone（系统 F7，按复核标 [C]）。** §9.4 加一句：

  > Development is plausibly still the keystone [C]; the window closes as conversion among the corrector domains rises, which is why Stage 3 cannot wait for Stage 4's trust.

  接上 T-B 与 L845 的谱系序列。
- **驻留时间（系统 F4，按复核）。**

  > A change must be held for about $\ln R/(\varepsilon d)$, until rule support falls below breakeven, and then long enough to repay the lock-in accumulated meanwhile. Share levels fall before withdrawal is safe; a floor of alternative lineages shortens the wait.

- **Allee 宿主（系统复核 F3）。**
  - 定理 8.2(1) 的恢复子句只对 logistic 宿主成立。
  - 正面方案要求过渡中的裕度 $\Delta>\Delta_{\min}(A)$，而且 $V_{\min}$ 不低于物理阈值。
  - 这是可纠正核 8.10 的第一个可计算实例。定义 8.10 引判别核（Cardaliaguet, Quincampoix and Saint-Pierre 1999）。
- **危机窗口。** 补一句：

  > A design adopted in a crisis must state what would end each of its emergency closures before it is adopted, or it will not state it afterwards.

### 5.11 Compact 的地位（SYNTHESIS §六.4，待 Ren 定）

建议：
- 正文 §8.6 保留"功能→形态"表，以及一段 "One worked configuration"，说明它是**分别持有的一组功能**，不是一个机构；
- 5.4 的分表、压力测试和 D1–D8 估计移入一个附录（例如 "A worked configuration"）；
- §10.1 第三层把它与其他设计并列比较。

这样它仍是候选，不再是唯一展开、自评通过的方案。

---

## 六、恢复丢失的内容（交付 6）

| 项 | 去处 | 形式 | 拟用英文（或要点） |
|---|---|---|---|
| (a) 关系自我与大同（自我层面的说明） | §3.8 第 1 条之后；§8.1 的两句（L1836 力之所及、L1846 共开共续）归到它下面 | 一段，[V] 与 [D] 混合，注明出处是作者语料 | At the level of the self, the accurate boundary is the one the author's relational account of the self describes: a self is the action-centre of the relations that form it, body, care received, language, institutions and its own choices, not a point outside them that enters relations afterwards. The isolated self of Ψ1 is the boundary error of Proposition 3.9(3) held as an identity. On this account maintaining the self and maintaining the whole are not rival instructions; the first is a step in the second. That is why the theory needs neither pole of the individual–collective axis: a self that is a knot of relations is neither an atom nor a cell of a collective. 大同, in the same corpus, is a direction, not an end state and not uniformity: a maintained condition in which the many are nourished together and none swallows the rest (万物并育而不相害). Two of its consequences appear in Section 8.1: responsibility scales with causal radius (力之所及，责之所在), and the norm of a shared future has three parts (共开、共续、不夺共续). |
| (b) κ 随力量上升的收敛猜想 | §3.6 末尾；定理 5.16 后的段落引用它（2.3）；新 crux C11 | [C] | **Convergence [C].** For a planetary technology the unpriced coupling $\kappa$ plausibly rises with power: the host is shared, failures propagate through concentrated common infrastructure, and the harms that prices do not settle grow with what is contested. If so, the accurate self-model and the inclusive one converge over the long run, and understanding that we are one becomes first a matter of seeing correctly. The measurement is the growth of unpriced coupling: shared hazards, the propagation of failures through concentrated nodes, and systemic risk (EV13). |
| (c) $\theta_g$ | 命题 5.2(3) 第二句（数学规划核对）；§6.1 L1203 后补一句 | [T] | 5.2(3)：*The total material payoff stays positive at every scale iff $\theta\ge\theta_g=(r(n-1)-1)/(1+r)$, and $\theta_g$ rises with $r$.* §6.1：In the example, the accurate weight $\kappa=0.4$ lies below $\theta_g=1$: the gap between what accuracy supplies and what the contest requires, which only institutions, or coupling that grows with power, can close. |
| (d) 改革两难 | §8.7 开头、Remark 8.12 之前；§9.4 补偿回路表加一行 | 一段 [T∣A]，引 4.2、4.5、3.6 | **The reform dilemma.** Reform needs influence, and the game is what produces influence. The path by which a reformer gains the capacity to change the rules runs through the selection the reform is meant to change. So it tends to select the reform out before the capacity arrives: those who reach the positions from which rules are changed are those the rules favoured, and they arrive formed by them (Section 3.6; Proposition 4.2). This is the guardian problem in motion. The theory has two answers, and neither is a better guardian. Reform can act where the selection has not yet closed: at a keystone while its window is open (Section 4.5), or in a crisis with a design prepared in advance (Section 9.4). And the capacity to reform can be built outside the contest for influence, by formula-funded correction keyed to no one, so that it does not have to be won. 补偿回路表新行："Reformers selected out on the way to office; reforms amended by their beneficiaries" 对应 "Formula funding; recusal; insulated rule-making". |
| (e) 四回路按回路写 | §2.3 | 见 1.3 | 见 1.3 |
| (f) W→C→N 回路 | §2.5 | 见 1.3 | 见 1.3 |
| (g) "unbounded relative objective" 的定义（L1585 处成了悬空词） | §2.6 "The logic to oppose"，与"癌"的定义放在一起 | [D] | Call an objective *unbounded relative* if it ranks relative standing on the decisive dimension without any point of enough. It is the winning model in its purest form: Ψ1 at $\theta=-1$, with Ψ2 certifying the winner and Ψ3 compounding the win. "Cancer" in this paper names exactly the selection of such objectives by a selection that cannot see the host. |
| (h) Ren 的五种终局 | §3.7 引理 3.10 之后，紧接 2.2 的段落；§0 可以前引 | 一段，带映射 | The author's corpus names five endgames of the dynamic: (i) a freeze of mutual destruction, in which any move is suicidal; (ii) deadlock, a power structure frozen by the consensus of the remaining players; (iii) a change of narrative by which the players come to see themselves as one whole and so gain the ability to cooperate; (iv) collapse; (v) winner takes all. Four of them are results of this paper: (i) is deterrence at the saturating branch (Theorem 5.15, Branch I′; Proposition 7.5); (ii) is a closure that cannot state what would end it (Definition 8.10), a captured configuration (Proposition 4.8); (iv) is Theorems 4.11 and 5.12; (v) is Proposition 5.10. The third is the route of Lemma 3.10's transmission term, and it is the purpose of this paper. |
| (i) 攻防框架一句 | §7.12 L1798 | 有条件的一句 | To the extent that the offense has the advantage (P1) and offense and defense are hard to tell apart (dual use), AI sits in the doubly dangerous quadrant of the offense–defense framework, where cooperation is hardest (Jervis 1978). |
| (j) "Continuation relies on the third alone…"（v5.2 L195） | 命题 5.4 之后 | 一句，改为四杠杆 | Continuation acts on one lever, the residual harm per unit $L$, while the contested stakes grow; a change of selection acts on all four. |
| (k) 叙事—价值框架机制 | §5.4 "Narratives" 一条扩成一段 | [C]，接定义 2.2 的 $(x,\sigma)$ | Narratives are carriers too. The frames that spread are selected for fitness to the contest; a frame that wins shapes the vocabulary in which the next round is described, until its words escape the game in which they were coined and a frame read as nature is no longer contested. By the time the frame is noticed one is already thinking inside it. Crowding-in also occurs (Bowles and Polanía-Reyes 2012). |
| (l) 内生域与认识封闭的四级（ASTRA） | §10.6 研究计划 | 各一句 [C] | — |
| (m) 账本改为三栏 | 附录 F；CLAIMS §7；CHANGELOG L40、L86 | Restated／Corrected／Withdrawn | **Restated：** one root；growing self；re-absorption；three zones；以及 V6.1 的 one pressure、5.16、3.10、3.3(2)、5.14、6.7、7.10、incarnation origin。**Corrected：** sharing reverses；national genealogy；"21,096 cases agree" 的验证说法。**Withdrawn：** bistable numbers and slope；"shared is decisive standing"；θ=n−1 is oneness；"That the lemma leaves only this route is a theorem"。另：L2962 与 CLAIMS L156 "§3.3" 改为 "§3.6"；P4.1、P5.11、§4.6 三行的变更栏照忠实度复核改；v1 的五个区分记功 |

---

## 七、检验与关键分歧（交付 7）

### 7.1 改写的检验

| 检验 | 改写后的预测 | 对立预测 | 理由 |
|---|---|---|---|
| **T-B** | (i) Influence spending and authorship of standards rise superlinearly with share ($p^2$), and cultivated conversion tracks the third moment of shares, not the Herfindahl index. (ii) Incumbents oppose non-appropriable correction (mandated access, arm's-length funding) even where it raises rivals' costs more than their own; **support for such correction at net cost to themselves refutes the channel.** | (i) Spending in proportion to revenue, or a fixed-cost threshold alone (Bombardini). (ii) Support for any obligation that raises rivals' costs (barriers to entry, Stigler) | 删去 "The theory also predicts the second" |
| **T-C** | The effect of verifiable signals of intent on intensity, holding capability fixed, **declines as the convertibility of winning in the game rises** (κ_c, $b_{ij}$): signals correct a misjudgment of a rival's current model, not a correct forecast of what the game selects (Section 2.6) | Defensive realism: intent signals matter according to the offense–defense balance and are independent of convertibility. Offensive realism: only capability signals matter | 防御性现实主义容许意图信号，原 T-C 无法把两者分开（对抗 5 与复核） |
| **T-F** | Within one field: organizations with capped or non-convertible returns show **T2 like their rivals** (the field's selection is relative) and **less T4** (their winnings do not convert into control). Attribution of the pressure to rivals is measured in advance and used as a stratum | Technological momentum: no difference in either. Ordinary profit-seeking: less T2 as well | 逃逸条款改为事先测量的分层变量 |
| **T-G** | **The gap in restraint between agents with wider and narrower objectives grows with $p_d$**; changing convertibility and $K_0$ changes conduct | Structural realism (Powell 1991): as decisiveness rises, structure dominates and conduct converges whatever the objective | 原方向与注释 5.9 相反（对抗复核遗漏 B；Codex）。比较静态由数学规划从修复后的 5.7 推出 |
| **T-D** | After rule-making is insulated, share levels fall before rule support crosses its threshold; a rollback judged on levels in that phase is re-absorbed. Restricted to conduct without a sunk-cost explanation | Sunk costs or bureaucratic inertia (Pierson): no re-absorption once levels have fallen | 原对立"无锁定的多极陷阱"没有人持有 |
| **T-E** | 改作交叉效应检验：moving a shared parameter moves signatures in more than one group; a conduct rule aimed at one signature does not | Separate problems with separate causes | 单因子共变降为研究问题 |
| **T-H** | 不再作为理论的检验，而是第二层启动的**指标**（C5） | — | 对抗次要 15 |
| **T-I** | 事先定义"共同来源"（国籍、国家拨款），并纳入宪制纠错者（法院、选举、新闻）与外部可核查性 | — | 否则本国评估者的行和按构造就 ≥1 |
| **T-J** | 加上基线：与同一机构其他战略计划的"计划先于预算"相比较；否则移入研究计划 | — | 原形式在任何领域都成立 |
| **T-K** | 保留为确认性检验，注明 Olson、Stigler、Bombardini 同样预测；区分性残余并入 T-B(i) | — | 不做有损合并 |

### 7.2 新增检验

- **T-L 哪些偏差被修正（对齐税）。**
  - This theory predicts: privately visible divergences are corrected within one or two release cycles; divergences with common or delayed costs (evaluation awareness, shutdown resistance in controlled tests, opacity of reasoning) persist until a common constraint or an attributable incident.
  - Alternatives: both kinds are corrected at the same speed (the market suffices), or neither is (technical difficulty alone).
  - Data: lists of tracked divergences across releases, coded as private or common in advance.
- **T-M 能让 C2 失败的检验**（对抗次要 15，按复核加持续期与执行指标）：

  > If mandated independent access with arm's-length funding has been in force in at least two leading jurisdictions for at least the dwell time of Section 9.4, with findings executed against leading developers and evaluators' row sums measured below one, while the leading developers' shares have grown, C2 is refuted for that period.

### 7.3 新增与改写的关键分歧

C9 用于对齐税，与 SYNTHESIS 一致。对抗评审原拟的 "C9" 改编为 C10。

| Crux | What it is | Present evidence | What would change the recommendation | Next measurement |
|---|---|---|---|---|
| **C0 Interlock**（改名） | Whether moving a shared parameter moves signatures in several groups, or the signatures are separable | Qualitative (Section 2.5) | Interventions on a shared parameter that move only their own signature over the dwell time | T-E as a cross-effect test |
| **C9 The alignment tax** | Whether countering divergences whose costs fall on common terms lowers developers' relative payoff ($A_\tau$), class by class | Some safety methods also raised capability and spread without coordination; monitorability and safety training have measured costs in some settings | A class with zero or negative tax needs no common constraint; a class with a positive tax that developers counter alone refutes $A_\tau$ for it | Capability gap from safety training; release delays; the monitorability tax; T-L |
| **C10 Forgone benefits of E2** | The margin of the decisive class over capable systems that are not decisive, including lives earlier benefits would save | Not measured | A large margin that is reachable only through the decisive class raises E2's cost and moves the comparison toward E3. The weight given to it against catastrophic risk is normative (N1) | Which benefits need decisive-class capability, and which bounded systems already supply |
| **C11 Coupling and power** | Whether the unpriced coupling $\kappa$ grows with power | Qualitative cases (EV13); size not measured | Coupling that does not grow keeps a gap between accuracy and what the contest requires ($\theta_g$), so the requirement falls on institutions | Propagation of failures through concentrated nodes; systemic-risk measures over time |
| **C3**（改证据栏） | — | Mixed, in toy settings (Burns; Khan; Kenton; Engels; Marks) | — | — |
| **C4**（补） | Also: participation threshold and unravelling; for the benign winner, whether AI removes the winner's dependence on the cooperation of the governed (Acemoglu and Robinson) | — | — | — |
| **C5**（补证据栏） | — | Also: balancing by others against a rising actor (Waltz 1979; Walt 1987) is a saturation mechanism independent of technology, and Proposition 5.14 at $n\ge3$ is its counterpart in talk. Evidence: short and diffusing leads, against P1 at present; it does not bear on P3; the frontier has not changed hands (evidence review I3) | — | — |
| C5、C7 两行"一体"一栏 | 按 2.3 替换 | — | — | — |

§10.3 末段（L2373）按 2.3 替换。§10.4 第 2 条加上 "classified before the outcome, by the descriptive profile of Definition 7.12"。

---

## 八、与评审、复核的分歧，以及我的取舍

1. **SYNTHESIS §二.9 的正回路。** 综合采纳了系统评审的"贡献者占据维持规则的位置"。我从复核，拒绝它，并补上复核没有说的一点：生成秩序内部仍有选择（按有用性），不被载体选择的是规则本身。综合的这一条需要随之订正。
2. **忠实度评审 1c。** 它的替换句不用。我保留它的意图，把位置换到系统层："Oneness is what these requirements are requirements of"。这样避开与 L1203 的冲突，也不把一体写成个体的准确反应。
3. **对抗评审"把共同保管整体移入条件清单"。** 从复核拒绝，但不把保管整体留在"现在做"：预备在第一层，启动在第二层，触发规则用"距决定性的时间减去安装时间"。
4. **对抗评审"Only design acts before the first catastrophic failure"。** 改写：预见所需的是对耦合的准确模型，不是"看见一体的设计者"。只关心自身生存、但看得准的行动者也算。这同时回答了忠实度评审重要 2 的问题：为什么不能由只想避免灭绝的狭隘行动者来设计。
5. **对抗复核建议的判断句 "requires an additional failure"。** 我认为这句本身可争议：设计的最坏情形并不依赖 (X)(U)(φ)，但依赖它自己的证书失效。我改用**可测性与提前量的不对称**作理由，并明说这是判断，不是推导（4.1）。
6. **对齐评审 B2 的模型层"窄的公共清单"。** 只作为三层中的一层采纳。范围由博弈层的参数判据决定，以免回到 Ren 已纠正过的可操作性反射（"窄清单是次序，不是范围"）。
7. **系统评审 F6.4"均等化只减速"。** 从复核拒绝。同时把 $K_0$ 加进联邦例证：均等化同时是 pooling 和底座供给。
8. **"Remove any one and the loop opens"。** 评审没有提。按数学 F2 的结果，它只在 $K_0>0$ 时逐条成立；我保留 Ren 的这句话，加上这个条件，请数学规划核对。
9. 复核里我没有发现事实性错误。上面几处是范围上的补充或改写，不是推翻。

---

## 九、交给起草者的顺序与依赖

1. **等数学规划定稿的符号与修复式**：5.7、5.16、5.3 加 $K_0$、3.3(2′)、3.10、5.14、6.7 加 $A_\tau$、7.10 三栏、8.6(3)、8.11(3)、5.2(3) 的 $\theta_g$。本文件中依赖它们的句子，都按"条件式"写，可以直接替换符号。
2. **先改脊柱**：定义 2.1、§2.3–2.5、§2.7、§3.7–3.8、§5.5 定理后段、§6 开头与 6.4、§10.1–10.3。然后再改中文概要、§0、§1.2、§1.5，它们只是脊柱的摘要。
3. **再改正面方案**：§8.2 闭合与四股、§8.5–8.7、Compact 拆分、联邦、功能表；然后是 §9 的 keystone、驻留时间、补偿回路两行。
4. **最后**：附录 F 三栏、附录 G、CLAIMS 与 CHANGELOG 的十余处"一体"、检验表与 crux 表。用 grep 清除 "oneness is a gain"、"one pressure"、"is a theorem"、"regime"、"bounded and recoverable"、"decisiveness dilemma"。
5. **肯定门**：§10.1 的第一层以生成方向的步骤结束（第 6、7 条）；§10.8 保持 v6.0 的肯定式结尾，只改 3.3、2.2 提到的句子。
