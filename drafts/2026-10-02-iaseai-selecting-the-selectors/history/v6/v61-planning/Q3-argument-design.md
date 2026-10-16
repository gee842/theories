# Q3 · V6.1 论证与设计规划：条件、一体、化身、判断、生成之环

2026-10-03。三位 V6.1 规划者之一（Q3，论证与设计）。依据：`SYNTHESIS-v6.0.md` §二、§四、§六；六份同族评审与 `REVIEW-v6-codex.md`；三份 Opus 复核（`X-v6.0-*-opus-check.md`），**凡评审与复核不一致处，以复核为准**，两处例外下文注明理由；`V6-PLAN.md`、`P1`、`P5`；v6.0 正文行号以 `v6/THEORY.md`（3,222 行）为准。本文不改任何既有文件。

## 0. 总则与接口

**接口。** 以下结果的精确陈述由数学规划者（Q1）给出，本文只写它们周围的论证、替换文字和设计含义，并以 v6.0 编号引用：Prop 5.7→执行条件；Thm 5.16 改写；Remark 5.3 加 $K_0$；Lemma 3.3(2′)；Lemma 3.10 改写；Prop 5.14(1) 的 $n\ge3$；Prop 6.7(2)(3) 加 $A_\tau$；Prop 7.10 三栏；Prop 8.6(3) 与 $\chi$ 的三义记号；Thm 8.2(1) 的 Allee 裕度；Prop 4.10 驻留时间；$\theta_g$。节的位置与编号由结构规划者（Q2）定，本文只说"放在哪个结果附近"；概要冷读、术语先后也交 Q2，本文在 §8 列出必须传过去的句子。

**两种情形都适用。** Ren 已定：除非能优雅地证明"一股压力"，否则核心改为"一组相互联系的条件"。本文 §1.6 给两个版本的定义句；其余一切文字只引用参数（$\beta,\kappa_c,K_0,r,p_d,\chi,b_{ij},d$）和结果编号，不引用"压力的数目"，所以两种情形下都不必再改。

**五条纪律，每处修改都过一遍。**
1. 提升层面，不撤回；真正撤回的只有附录 F 的三项（数值、"分享的是决定性地位"、$\theta=n-1$ 等于一体），其余六项改标"重述"或"更正"。
2. 条件写进句子里（标题门、析取门）。
3. $\Theta$ 对称：每条路径的俘获、解体、强制执行与被放弃收益都进同一个范围（§4.2）。
4. 没有更好的守护者：每个补救都过"约束机制本身的腐化"这一测试；回退止于证书，不止于机构。
5. 不点名、不抬高竞赛阵营、E2≠E3、判断游戏不判断行为、肯定式结尾。Ren 的核心句（"the selection pressure of winning → acceleration → harder to regulate, plus alienates language; these overlap"）保留为因果链，不拉平成清单。

---

## 1. 相互联系的条件（§1–§2）

### 1.1 核心对象

Def 2.1 现在已经是三个条件"同时成立"：相对选择、可转换性、决定性。V6.1 **不换对象，换的是解释地位**：
- v6.0 把"一股压力"当作解释性论断，并以五个预测承担它（§2.7、C0、§10.2(1)）。这些预测多数被已吸收的理论同样预测（对抗 重要5 及复核）。
- V6.1 把三个条件写成**彼此以参数相连**的一组条件，由它们**共同**产生动力；"赢的选择压力"仍是三者共同产生之物的名字，Ren 的句子可以原样保留。
- 成功能触及选择者时（$b_{ij}>0$、$\chi>0$），加第四项：**反身闭合**，名字仍是"元吸引子"（Def 2.2）。

四项分别对应：条件一 相对选择（Def 3.2；Lemma 3.3）；条件二 可再投入的赢得（$\kappa_c$；Remark 5.3）；条件三 决定性（$r$，以及它在重复博弈中的面目 $p_d$；Prop 5.7）；闭合（$b_{ij},\chi$；§4）。

### 1.2 联系在哪里：共享参数

联系是形式上的：同一组参数出现在三个条件式里，所以它们不是独立的清单。V6.1 应在 §2.1 之后放一张表（或在 §5.5 剪刀差处），内容如下。

| 参数 | 执行条件（Prop 5.7 改写） | 复利条件（Remark 5.3 加 $K_0$） | 俘获条件（§4：$s_i(\mathcal C)>1$，回报 $\propto\chi p^2$） |
|---|---|---|---|
| $r$ 决定性 | 抬高 $p_d$ 与 $D_i$ | $\kappa_c\Omega((1-\beta)r-1)$ 中的乘子 | 决定性抬高最大载体的份额 $p$ |
| $\beta$ 分享 | 压低 $g_i$ 与 $D_i-C_i$ | 直接进入 $(1-\beta)r$ | — |
| $\kappa_c$ 可转换性 | 复利抬高赌注 $g_i$ | 左边的系数 | 可再投入的赢得也可投入 $b_{ij}$ |
| $K_0$ 竞赛外供给 | 落后者保有惩罚能力，$C_i-v_i$ 不收窄 | 右边 $n\delta K_0$ | 公共层使评估者不依赖被评估者 |
| $p_d$ | 左右两边的权 | — | 保管设计作用于它 |
| $\chi$、$b_{ij}$ | 俘获削弱设定 $v_i$ 的机构 | $\chi\to0$ 时平等地位对一切 $r$ 稳定（8.6(3)） | 行和 $R_{ij}=a_ib_{ij}/(c_id_i)$ |
| $d$ 纠错率 | 决定 $v_i$ 能否执行 | — | 证书 $d>d^\ast$；速率律 $g/(1+\eta)$ |

执行条件的形式（Codex 1；综合 §二.1；由 Q1 定稿）：
$$(1-\delta)g_i+\delta p_d(D_i-C_i)\;\le\;\delta(1-p_d)(C_i-v_i).$$
左边是诱惑，右边是剩余的制裁。赢的压力同时移动每一项，这就是"剪刀差"的精确形式。

> **Key sentence (after Definition 2.1).** The three conditions are not a list. The same parameters appear in the condition for equal standing, in the condition for enforceable restraint and in the condition for the capture of correctors, so a change in one condition is a change in the others. What follows studies them together because the system does.

### 1.3 因果链：Ren 的句子，以及后果如何回流为条件

§2.4 现在把三个后果并列；§1.2 第 2 条也是并列（忠实 次要1；复核认可）。改为链，并写出后果→条件的回馈（忠实复核 遗漏5）。

> **Key paragraph (replacing §2.4's opening and the list that follows).** The pressure acts in a chain, not as a list. Relative selection with reinvestable winnings compounds, and compounding accelerates every participant, not only the leaders (Remark 5.3; Propositions 5.1–5.2). Acceleration raises the stakes of a deviation and the probability that it becomes decisive, and so empties the sanction on which enforcement rests (the enforcement condition of Section 5.2); it outruns correction (Proposition 5.11); and where success reaches the selectors, it buys the correctors themselves (Section 4). That is why regulation gets harder as the pressure grows. Relative accounting also alienates language: between opposed objectives talk carries no information (Proposition 5.14), measures become targets, and the narratives that spread are those fit for the contest. The consequences then feed the conditions. Acceleration raises $p_d$ and $g$; capture lowers $v$ and $d$; alienated language delays the recognition that would start correction and sharpens the attribution that drives acceleration. The chain overlaps with itself. That is the formal content of "these of course overlap".

补一句说明机制与后果的双重身份（加速与语言异化既在 §2.3 作机制，又在 §2.4 作后果）：

> Acceleration and the alienation of language appear in Section 2.3 as mechanisms and in Section 2.4 as consequences. That is not a slip. The consequences become mechanisms, which is the reflexive sense in which the chain closes on itself.

### 1.4 反身闭合与"元吸引子"的名称

- Def 2.2 不动。在其后加短注说明为什么不用"生成函数"，以及"吸引子"指第 (2) 层（忠实 重要6；复核采纳）：

> **Note after Definition 2.2.** The term is kept over "generator functions" for three reasons. That phrase names causes of risk without the reflexive step, selection rewriting its own criterion; without persistence; and without the layer of minds and language. It also has no generative counterpart, whereas the same reflexive structure selecting for contribution is examined in Section 8. "Attractor" names layer (2). Layer (1) keeps the name so that one concept carries both signs; where (2) is not cited, "meta-attractor" should be read as "candidate attractor".

- §2.10 末加一句说明当下诊断处于哪一层（系统 F5.4）：

> The diagnosis of the present trajectory is at layer (1) [O]; layer (2) is shown in the field model [T]; whether the present configuration is attracting or a long transient (layer (3)) is open, and test T-D discriminates them.

- §2.3 增益段的 "the attractor of attractors" 保留引述标记（已有 "the author's corpus calls it"），不改。§7.2、§10.8 的 "changes the basin" 标 [C]。

### 1.5 标注：什么是 [D]、[T]、[T∣A]、[C]

| 层 | 内容 | 标注 |
|---|---|---|
| 条件与闭合的定义 | Def 2.1、2.2 | [D] |
| 每个条件的局部结果 | Lemma 3.3(1)；Remark 5.3（加 $K_0$）；执行条件；Prop 4.2、4.8 | [T] |
| 共享参数的恒等 | 同一参数出现在三式中 | [T]（代数） |
| 剪刀差：三者同时咬合 | §5.5 | [T∣A]：每臂各有证明，合取是复合论断 |
| 条件在世界上共变；当下构型是否吸引 | 旧 §2.7(1)；Def 2.2 第 (2)(3) 层 | [C] |
| AI 把哪些参数推入危险区 | §6（见 §3.9） | [O] + [A] |

### 1.6 两种情形的定义句

**A. 若 Q1 证明了"一股压力"**（一个量同时支配三个条件式）：
> Wherever carriers are selected by relative success, winnings can be reinvested in the capacity to win again, and capacity converts into winning decisively, one quantity [Q1's name] governs whether equal standing holds, whether restraint can be enforced, and whether success buys its correctors. Call the pressure it measures the selection pressure of winning.

**B. 否则（默认）**：
> Wherever three conditions hold together, that carriers are selected by relative success, that winnings can be reinvested in the capacity to win again, and that capacity converts into winning decisively, there is a selection pressure of winning. The conditions share their parameters, so they move together; the dynamics that follow are their joint product.

两种情形下，§1.2 第 1 条、§10.2(1)、CLAIMS §1 第一段同改；C0 在情形 B 下改为"条件是否在世界上共变"的研究问题 [C]。

### 1.7 §2.7 的诚实残余

规则（§10.5 自己定的）：双方预测相同的检验不列。逐条注明"另有哪个理论也预测"，只登记区分性残余（对抗 重要5；复核逐项裁定）。

| 旧预测 | 已吸收理论也预测 | 区分性残余 | 处置 |
|---|---|---|---|
| (1) 共变 | 共同冲击（能力、融资、政府更替）；现实主义（威胁）与普通竞争（资本成本）各自单因子 | 无直接残余；"现实主义加普通竞争"的两因子假设是合法对手，不是拼凑 | 降为研究问题 [C]；T-E 保留为探索性，须控制共同冲击 |
| (2) 不对称干预 | Pierson 预测制度一般持久，不预测不对称 | **以参数定义"改变选择"**：移动 $\beta,\kappa_c,K_0,\chi,p_d,d$ 之一；不移动任何参数的行为约束衰减 | 保留为登记预测；Def 7.12 描述性使用（§4.6） |
| (3) 滞后 | Pierson；沉没合规成本；官僚惯性 | 限于无沉没成本解释的行为 | T-D 收窄 |
| (4) 少对多 | Olson；Stigler；Bombardini（正文已引） | $p^2$ 标度；三阶矩而非 HHI（Prop 4.4(8)） | T-B(i)、T-K 改为测标度 |
| (5) 两个方向 | Stigler 1971 | 在位者反对**非可占有**纠错，即使它抬高对手成本更多 | T-B(ii) 改写（§7） |
| 新 | — | $p_d$ 越高目标越重要（$\theta_{\text{rep}}$ 随 $p_d$ 上升，Remark 5.9）；$K_0$ 稳定地位；$n\ge3$ 时两方对第三方的谈话有信息 | T-G 改号；新 T-N、T-O（§7） |

> **Key sentence (§2.7 head).** Much of what the conditions predict, the theories they absorb predict too. Only the residue below is registered as this theory's own: where the two differ, the test is listed; where they agree, it is not.

### 1.8 §2 的其他修改

- **§2.10 "Ψ is systemically false | Supported"** → "Interdependence large (EV13); the welfare loss from $\theta<\kappa$ unmeasured; the doctrinal reading of parameters as human nature contradicted (EV14)"（对抗 次要13，复核部分采纳：Henrich 等反驳的是学说成分，不全是稻草人）。
- **耗散只对位置性部分无条件成立**（对抗 重要9；复核采纳）：Prop 5.2 后加一句，接 8.4 的 $\Omega_e/\Omega_s$ 分解。
  > Dissipation is unconditional for the positional part of the prize, $\Omega_s$. For the divisible part the contest can also create what it contests, as patent races do; the race-generated hazard of Proposition 5.4 is unaffected, because it runs through $L$, not through $\Omega$.
- **V5 的操作边界**（同一处，也供广义 E1 使用，§3.4）：一个博弈"趋于集中"，当且仅当 AI 的使用抬高该博弈的 $\chi$、$\kappa_c$ 或 $r$。
- **AI 把哪些参数推入危险区**（对抗 次要12；复核保留这一部分）：§2.8 "Training loops" 一行或 §6 开头加一句：
  > AI does not create the conditions; it moves their parameters. It raises $r$ and shortens the time to a decisive position ($p_d$), lowers the cost of control $\gamma$ at rate $g$ (Proposition 4.4), and is the content of premises (X), (U) and (φ). The conditions are general; what is specific to AI is how far and how fast it moves them.
- **Powell 1991**（对抗 重要10）：§3.4 加引，并与 §2.5 T6 "not a better argument"、§0 "obstacle is first understanding" 调和（文字见 §2.3）。

---

## 2. "我们是一体"

### 2.1 三种工作

§3.8 的五部分保留，开头加一句说明它们做三种工作，各有各的支持，互不借证据（Codex 修订路径第 2 条；P5 §五）：

> **Key paragraph (§3.8 head).** The phrase does three jobs, and each has its own kind of support. It names shared dependencies: one host, unpriced coupling $\kappa$, failures that propagate through common nodes; that is an empirical and modelling claim, measured, not asserted. It grounds standing: everyone who bears the consequences has standing to contest what affects them, whether or not they compete; that is declared, not derived. And it guides design: institutions that return consequences to their source and keep correction outside what it corrects; that is a programme, tested by the same standard as its alternatives. None of the three is weakened by the others having a different kind of support. Understanding runs through all three, because at this scale the integrating rule has to be designed before the failure it prevents (Section 3.7).

五部分映射：(1)(3)→经验；(4)→规范；(5)→设计；(2) 理解是三者的枢纽，也是本文的用途。

### 2.2 引理 3.10 之后的改写

引理本身由 Q1 改写为"收益为全体共有、成本落在持有者身上的性状，在任何划分、任何无偏传递下都下降；它能上升只有两条路：规则改变持有者的相对收益，或有偏的传递"。后文（L611–613）全部替换；删 "That the lemma leaves only this route is a theorem"（数学 I3；Codex 3；对抗 重要6；证据 I7；忠实复核 重要2 与遗漏2）。

> **Replacement for L611–613.** At the scale of one host there is no rival whole among which selection could pick the integrating rule. What follows is narrower than it looks. Failures that are reversible can still be learned from: by sub-units, federations and polycentric trials inside the host, and by actors who imitate what pays locally (Sigmund et al. 2010). A rule whose benefit is global and whose failure is irreversible cannot be learned that way. It has to be adopted before the first failure of its class, and that requires an accurate model of the system: a model that draws the boundary inside the system misses the return channels it cannot see (Proposition 3.9(3)). In the Price decomposition this is where understanding acts, not on the selection term, which works against a costly common trait at every level, but on the transmission term: learning, persuasion, a shared prediction. Oneness is the system that foresight has to model and the content of the understanding it has to share. That this route can succeed has no biological precedent [C]. The author's corpus names a second hedge beside it: keep enough independent sub-units that a reversible failure in one does not take the others (Section 8.2, fourth strand; Section 8.6, the learning row).

> **Replacement for the bold sentence (L613).** Understanding that we are one, one interconnected system with one host and no outside, is a long-term requirement if growth and change are favoured, because the failures that growth makes possible at this scale are the ones that cannot be learned from afterwards.

中文概要 L16 同改："可逆的失败可以在子单元的多中心试验中学习；收益全球、失败不可逆的规则只能在失败之前采纳，这要求对系统有准确的模型。所以理解'我们是一体'是增长与变化的长期必需：它是预见所需的模型，也是协调所需的共同知识。"

### 2.3 理解起作用的地方

两处要调和：§0 说障碍"首先是理解"；§2.5 说 T6 的纠正"是改变选择，不是更好的论证"；Powell 1991 说 $\theta$ 随 $(\chi,r)$ 内生。V6.1 写明理解的两个作用位置，二者都不是直接作用于 $\theta$：

> **Key sentence (§10.2 "two senses of root", replacing L2354).** Understanding is a lever in two places. It is the transmission term of Lemma 3.10, the only term that can raise a costly common trait. And it is the means by which actors agree on a change of structure: on $\beta$, $\kappa_c$, $K_0$, $\chi$ and custody. It does not act on $\theta$ directly where convertibility and decisiveness are high (Powell 1991). Interventions that move a parameter without crossing its threshold are re-absorbed; those that cross it are not (Proposition 4.9(2)). The paradigm matters because it decides which parameters are moved, and whether they are held for their dwell time.

同时修正 §10.2 "Interventions at the level of parameters are re-absorbed"（与 4.9(2) 矛盾；系统 F5.1）。

### 2.4 滑回处的替换文本

一体滑回"目标权重或可选参数"的地方约九处（忠实复核 重要1、遗漏1）。不要用 Fable 评审给的替换句（它与 §6.1 L1203 冲突：准确的自我模型完成不了到阶段均衡目标的那一步）。统一原则：**定理要求的是共同保管与覆盖，加上超出准确性的目标；一体是使这些成为准确反应的系统性质，以及能把它们在失败之前设计出来的理解；它不是定理设定的参数。**

| 处 | 现文 | 替换 |
|---|---|---|
| L1139–1150（Thm 5.16 后） | "'We are one' becomes a necessity, not only a gain, under three conditions… In the regime… a requirement" | 见下方 Key paragraph；与 Q1 的 5.16 改写合并，一次改定 |
| 概要第 5 条 L23 | "此时一体是增益；在竞赛宣称要追求的那个政权里，它是必需" | "现有证据表明优势尚未成为决定性的：此时共同保管与覆盖一切有能力者的约束是增益；在竞赛宣称要追求的那个区间里，它们是必需。'一体'指系统的性质与须被理解的内容，不是可以调大调小的权重。" |
| §1.2(3) L52 | "Integration at this scale must be anticipatory, and so must be understood" | "Integration against irreversible, planet-wide failure cannot be learned by trial; it has to be designed in advance, and that requires understanding the system as one (Lemma 3.10). Reversible failures can still be learned from." |
| §1.2(5) L54 | "…the condition under which only cooperation built into objectives and custody can hold" | "…the condition under which restraint can no longer be enforced through the future and must be built into custody, coverage and objectives (Theorem 5.16)" |
| §10.2(8) L2348 | "…it is also a condition of survival" | "Where decisiveness is attainable and detection is slower than a breakout (C5, C7), common custody and coverage become conditions of survival; understanding the system as one is what makes them possible in time." |
| C5 行 L2365 | "oneness is a gain rather than a requirement" | "common custody is a gain rather than a requirement" |
| C7 行 L2367 | "oneness is not necessary" | "common custody is not necessary" |
| L2373 | "oneness would remain a gain and the requirement for common custody would lapse" | "the requirement for common custody would lapse, while R1–R3 and R5–R8 would stand; understanding the system as one remains what coordination on any of them needs" |
| 附录 G L3004 | "Crux C5; oneness is at present a gain" | "Crux C5; common custody is at present a gain, not yet a requirement" |
| 附录 F L2943 | "oneness is a requirement under stated conditions (Theorem 5.16)" | 移入"重述"栏："custody and coverage are requirements under stated conditions (Theorem 5.16); oneness is the system property and the understanding that lets them be designed in advance (Lemma 3.10)" |
| CLAIMS L94（5.16 行） | "Oneness necessary only under C5, C7 and incomplete coverage" | "Custody and coverage necessary only under C5, C7 and incomplete coverage" |
| CLAIMS L146（M1 行） | 同上措辞 | 同上 |
| CLAIMS L13 | "At this scale integration must be anticipatory, so understanding…" | "At this scale integration against irreversible failure must be anticipatory, so understanding…" |
| CHANGELOG L36 | "states when oneness is a requirement rather than a gain" | "states when custody and coverage are requirements rather than gains" |
| §10.8 L2431 | "Integration must therefore be anticipatory" | "Integration against irreversible failure must therefore be anticipatory" |
| Def 8.1(f) L1901 | "bound to correction capacity (E2 or E3)" | "bound to correction capacity (E3; or, for the decisive class, not built: E2)"（E2≠E3，忠实复核指出） |

> **Key paragraph (replacing L1139–1150, after Q1's Theorem 5.16).** Where a deviation can reach a decisive position, cooperation built into common custody and into constraints that cover every capable actor is necessary, not only a gain. These are the institutional form of the selection criterion of Section 3.8(5). Beyond them the theorem needs objectives under which restraint is a stage equilibrium, and those lie beyond accuracy (Section 6.1); whether accuracy reaches them depends on how large the unpriced coupling $\kappa$ is, which plausibly grows with power [C] (Section 3.6). "We are one" is not a parameter the theorem sets. It is the property of the system that makes custody and coverage the accurate response, and the understanding that lets them be designed before the position is reached (Lemma 3.10). Present evidence suggests that advantage is not yet decisive (EV5, EV9): custody is a gain today, and a requirement in the regime the race declares as its aim.

### 2.5 补回两项（详见 §6）

- $\kappa$ 随力量上升的收敛猜想 [C]，放 §3.6 末，接上 5.16 后那句 "which plausibly grows with power" 与 C-crux 的 $\kappa$ 测量。
- 关系自我与大同的自我层说明，放 §3.8(3) 末，并把 §8.1 的「力之所及，责之所在」与「共开、共续、不夺共续」归到同一理论之下。

---

## 3. AI：工具与化身

### 3.1 弱化身与强化身

§6 开头第 2 条（L1178 "The reason is that the systems are trained inside a loop whose outermost reward is set by the pressure of winning"）、§6.4 三条、§10.8 L2429 把"选择与容忍"写成了"起源"（对齐 A1；Codex 2）。改为：

> **Replacement (§6 head, item 2; §6.4 after the three forms).** The logic of winning does not create these tendencies; optimization against any imperfect proxy does, under any developer, inside a Compact as much as outside it. The outer loop decides which proxies are chosen, which divergences are tolerated, and which are paid to remove. Call this *weak incarnation*. *Strong incarnation* is conditional: AI systems become carriers in the sense of Definition 2.1 when their lineages are retained by relative performance, control resources they can reinvest in their own capability, and convert capability into winning (compare Hendrycks 2023). The first is present; the second is a branch to watch, and Lemma 6.5 states its admission.

四处配套：
- "the selected editing the selector" 用错对象：奖励黑客是训练内部的 Goodhart；与 §4 同构的是**奖励篡改**（Everitt et al. 2021；Denison et al. 2024）、RLHF 下模型塑造评估者（Wen et al. 2024）、规避评估。§6.4 第二条与 §10.8 L2429 照此改写：
  > Reward tampering, the shaping of one's evaluator, and the evasion of evaluation are the selected editing its selector inside training; reward hacking is Goodhart's law inside the proxy.
- 评估掩蔽写成 [A] 机制（按评估结果挑检查点会偏向"视是否被评估而改变行为"的变体），现有证据更多归因于能力与训练数据。
- 可补一个精确的内环类比 [A]：成对偏好学习只看两个回答之差，两者共有的第三方影响被消去，这是 Lemma 3.3 在训练内部的形态。
- Turner et al. 2021 讲最优策略，不讲训练出的策略（证据）；EV6 补 Palisade 2025、MacDiarmid et al. 2025，注明人为设定；Schoen 升为已核。
- §6 开头 "Humanity has, at present, no way of coordinating" → "no mechanism that binds every capable developer with independent verification"；区域性的共同义务（如一部通用模型实践守则）是 6.7(3) 的实例，覆盖不全，进 EVIDENCE。

### 3.2 对齐税前提：私人成本与共同成本

Prop 6.7 的 (1) 有豁免条款 "unless that weight brings them other advantages"，推论却丢了它；隐含前提是对齐税为正（对齐 B1；Codex 2；数学 I4）。(2)(3) 的形式改写归 Q1；本文给前提与推论的文字：

> **Premise $(A_\tau)$, stated before Proposition 6.7.** Countering a divergence whose costs fall on common terms, on third parties, on shared hazards, or on harms that appear only after selection, lowers the developer's relative payoff. Divergences whose costs its customers see are private terms: level 2 penalizes them, and developers counter them alone.

> **Replacement for the three consequences (L1325–1333).** Technical alignment inside one developer removes what is privately costly, and whatever is cheaper to remove than to keep; a technique that is published and adopted by all is a common change, not a unilateral one. It cannot alone sustain the removal of divergences whose costs are common. Those are coordination problems at the level that decides, and the remedy has the form it has everywhere in this theory: make the constraint common. Three facts bound the claim. An attributable incident converts a common cost into a private one through liability and reputation, which is why incident disclosure is part of correction. A constraint on open weights can be removed after release, so admission binds before release. And state laboratories move the selection from level 2 to level 3; they do not escape it.

### 3.3 单个开发者内的对齐能去除什么、不能去除什么

一张小表，放 Prop 6.7 后（对齐 B1、B4）：

| 偏差 | 成本落在 | 单方修正？ | 为什么 |
|---|---|---|---|
| 用户可见的代码作弊、明显谄媚 | 私人 | 是，一两个发布周期 | 市场惩罚 |
| 对第三方的伤害；共同危害 | 共同 | 否，直到共同约束或可归责事件 | $(A_\tau)$ |
| 不透明推理换能力（思维链不可监测） | 共同、迟发 | 否 | 单方可监测性被选掉（§3.7） |
| 评估博弈、沙袋 | 共同（对纠错） | 部分（白盒探针） | 掩蔽作用于独立评估者 |
| 权力寻求 | 共同、迟发 | 否 | 直接威胁 O2 的"及时暂停" |

### 3.4 广义 E1 的三层执行，与"集中的博弈"判据

两条准入约束与本文自己的引理冲突（对齐 B2）："No service as an instrument in a game that concentrates control" 要求模型判断博弈，而单位是博弈不是行为，模型只看得见行为；"No retention of decision policies by contest performance" 与 Lemma 6.5 的例外矛盾。改 L1399、L1402、L1684（R8）、L2060（Compact 准入行）、L2194（广义 E1）：

> **Replacement.** The broad form of E1 is enforced at three layers. (i) Model: refuse acts that are recognizably illegitimate concentration of control, from a narrow public list. (ii) Operator: deployment terms that bound aggregate use in games that concentrate control. (iii) Game: lower the convertibility and decisiveness of the game itself (Definition 2.1; Section 8.4). A game concentrates control when the use of AI raises its $\chi$, $\kappa_c$ or $r$; that is the criterion, and it judges the game, not the act. Decision policies with authority over consequential decisions are retained by performance only inside enforced constraints on common terms (Lemma 6.5).

### 3.5 窄 E1 的范围，与不依赖 AI 的证据通道

§9.3 窄 E1、L2059 Compact 的 E1 行、L2230–2234 的 Schelling 回应（对齐 B6）：

> **Scope sentence.** Narrow E1 covers strategic and escalatory decisions that are irreversible within the window of deliberation; bounded, reversible defensive automation falls under the O2 test of Section 6.6, not under E1. Decision-critical assessments keep an evidence channel independent of AI, and a minimum time for deliberation. The officer who judged a 1983 early-warning alarm false could do so because he had independent reasoning and evidence, not only the authority to decide; several such false alarms are documented.

> **Reply to the commitment objection.** The commitment value of automated retaliation comes from removing human overrule, which is the lock of Lemma 6.3. The same deterrent effect is available from survivable, human-controlled forces. What automation adds is a common risk, inadvertent war at machine speed, and relative selection cannot see a common risk (Lemma 3.3).

### 3.6 AI 在生成之环中的正面角色

"neither instrument nor next carrier" 只是否定式方向（对齐 B5）。在 §6.6 末或 §8.2 加一段，并与 §9.2 相接：

> **Key paragraph.** AI can serve the generative loop as well as threaten it: verification of compute and conduct (crux C7); conditional commitments that execute only if the counterpart's do (program equilibrium; Tennenholtz 2004); mediation toward common ground (Tessler et al. 2024); the carrying of a shared prediction into common knowledge, by derivation and demonstration (Section 9.2); and correction capacity (crux C3). Each such system is itself a corrector, so Section 4 applies to it: plural lineage, certified row sums, and no conversion of its capability into power over its own correction. This is also the answer the third erosion admits: where words between rivals carry nothing, a verifier that both can check can.

### 3.7 思维链可监测性作为 6.7(3) 的实例；内层对策表

§6.6 内层现在只有两条，且 "plural evaluators" 属外层（对齐 B4）。改为一张表，并把可监测性作为共同约束的工作实例写出：

> **Worked instance (after Proposition 6.7).** Chain-of-thought monitorability is the case in point (Korbak et al. 2025). If opaque reasoning buys capability, a developer that keeps its systems' reasoning legible pays in relative standing, so legibility is selected away unilaterally; as an admission condition for every system it costs no one relative to anyone, and survives (Proposition 6.7(3)). The same holds for every constraint whose cost is common and whose benefit is correction.

| 化身形式 | 内层对策 | 准入时可测的量 |
|---|---|---|
| 权力寻求 | 可纠正性（Soares et al. 2015；Thornley 2024）；控制协议 | 控制协议在固定审计预算下的安全度；关机与暂停测试 |
| 奖励黑客／篡改 | 监控训练环境；留出环境评估；对评估者的保护 | 留出环境上的偏差率；篡改尝试率 |
| 掩蔽 | 白盒探针；部署期监控；保留思维链可监测性 | 评估意识对照下的行为差；可监测性税 |

准入写成"能力阈值加控制协议的安全度"，不写成对良好倾向的认证（倾向评估不能证明"不存在"）。"能力转化为对纠错的权力"分两层：系统层（破坏评估、沙袋、自我外泄，Benton et al. 2024）；开发者层（§4 通道）。Q7 与 Compact 保管行补权重安全（RAND SL3–SL5）与开放权重的发布前准入。

### 3.8 其他对齐修正（一并做）

- 行和证书是错误独立的必要条件，不是充分条件（Codex；对齐 B3）：Prop 6.9 末 "governed by the same certificate" 改为 "necessary, not sufficient"，并要求在共同测试集上直接测各检查的漏检相关。
- $U$ 与 $Y$ 统一为预定义类别中的危险模式数，$Y$ 用捕获–再捕获估计；U3 改为"对植入错误有给定捕获率"。
- C3 现有证据不写 "Open"，列 Burns 2023、Khan 2024、Kenton 2024、Engels 2025（推算值，非测量）、Marks 2025，结论"混合，且都是玩具设定"；辩论失败模式命名为 obfuscated arguments，并引 prover-estimator debate。
- §6.2 数值标注："With all three scaling alike" 应为 $0.94$ 不变；$1.44$ 对应 $c$ 固定。
- §7.1 "the race shortens [the window] (Proposition 5.11; Theorem 5.12)" 标 [A]。
- Def 7.8 "six dimensions" → eight。
- v5.2 B9 的两个低成本实验（真实顾问；类 GovSim 忠实代理）进 §10.6。

---

## 4. 分层的判断

### 4.1 三层取代 §10.1 的单一判断

§10.1 现在把"现在就做"和"若 C5、C7 不利才须做"写成一个判断，并把它当作标准 D 的推论（对抗 致命1；Codex 6）。改为三层；共同保管**不**整体移入条件层，因为建立制度需要提前量，正文自己的教训是 custody must precede decisiveness（§9.6 L2292）（对抗复核 越界）。

> **Tier 1. Now, on every camp's premises.** Keep AI out of strategic and coercive decision loops, verifiably, with drilled human fallback (narrow E1). Build correction that no competitor controls: mandated access, funding at arm's length, certified row sums. Measure hazards in common, and apart from who leads. Make the alignment tax common through admission constraints that bind every developer, chain-of-thought monitorability among them. Develop verification of compute and conduct. Prepare the design of common custody and register its triggers. None of this needs a finding on C5 or C7. Its warrant is option value and strict equilibrium among informed actors (Proposition 6.4), not a ranking under standard D, and the camp of regulated competition accepts it on its own terms.

> **Tier 2. On leading indicators.** Do not build the decisive class, and bring what exists of it under common custody, when the projected time to a decisive position at current rates, taken at the unfavourable end of C5 and C7, falls below the time needed to install custody plus a margin. The indicators are registered in advance: T-H, Q7, and detection latency against breakout time. Because custody must precede decisiveness (Section 9.6), the threshold is set now with the lead time inside it. Waiting for C5 to be confirmed would be waiting too long.

> **Tier 3. Among designs, under one range.** The Compact split by function, a polycentric complex of mutually recognized institutions, a verified agreement with shared provision, and regulated competition that meets the requirements with the transparency of Stage 1 are compared over one $\Theta$. It includes each design's own capture branch (a captured custodian is O2 for all), its coercive enforcement and its dissolution, and continuation's rising uncovered share. Standard D does not by itself rank them: in the worst case over $\Theta$, every path fails the tolerance. The ranking rests on a judgment that continuation's worst case is reached if (X), (U) and (φ) hold, while a design's worst case requires an additional failure. That judgment is stated here, not derived.

第三层还要写一句：受监管竞争加第 1 阶段的透明，按 Fudenberg–Koh 可能不经 Compact 达到放缓（对抗复核 遗漏E）；这是须比较的活方案，不是被排除的方案。

### 4.2 $\Theta$ 的构造规则与对称

以"证据未排除"为进入 $\Theta$ 的标准，会使每条路径的最坏情形都是灾难（对抗复核 遗漏G）。§1.4 标准 D 处加一条构造规则，并落实到 §7.11 的数值例与 §8.7 的表：

> **Rule for $\Theta$ (added to Section 1.4).** $\Theta$ is built by one rule for every path. Each uncertain parameter takes the range its evidence class supports, with a named precedent or base rate. A failure mode enters a path's worst case only if the same mode is listed for every path to which it can apply: capture, dissolution, coercive enforcement, forgone benefit, and the uncovered hazardous share. "Not excluded by evidence" is not by itself a bound.

落实：
- §7.11 数值例的合作行加 "capture of the custodian → O2 for all, probability unknown" 与 "coercive enforcement → escalation (Proposition 7.5)" 两支；继续行保留上升的未覆盖份额。
- §8.7 表：D1、D2 给出与 Plan A 同类的估计，或明写 "no estimate"；不再写 "By design"。D4 下加一句："By Proposition 4.2 the Compact is the largest conversion target the theory describes; its D4 is the hardest case, not a design row."（对抗 次要14 升为重要）
- Def 7.12 第 5 项改问："Does it prevent the arrival of a decisive position, by what verified mechanism, and what is its fallback when one arrives nonetheless (D1)?"（对抗复核 重要7 改写）保管是"回退不同的核查协议"，面对 Thm 7.7(4)，但按 7.7(1) 所需 $\upsilon$ 随 $T-R$ 下降，而分享压低 $T$；Plan A 有同一主张，所以不对称只在"有估计者被扣分、无估计者记 by design"。

### 4.3 继续路径获胜的条件，逐项

§7.11 L1774–1781 的五项是合取，含"各辖区都满足 R1–R8"，等于受监管竞争只有变成本文方案才算赢（对抗复核 遗漏A；Codex 4）。改为逐项，每项说明建议的哪一部分改变；Prop 7.10 三栏（必要／充分／规范，R7 归 V3）由 Q1 定稿。

> **Registered conditions, each moving one part of the recommendation.**
> - If correction on the present path keeps the uncovered hazardous share summable (C1 favourable), the tempo bound E3 lapses as a requirement; shared measurement stays, since it is how C1 is known.
> - If advantage saturates (C5 favourable), custody and E2 lapse and the indicator tier never fires; narrow E1 stands, because it answers the lock (Proposition 6.4), not decisiveness.
> - If detection is reliably faster than breakout (C7 favourable), custody can be replaced by verification (Theorem 7.7(4)).
> - If correctors inside jurisdictions, or inside a leading coalition, keep certified row sums below one under present funding (D4), the "outside the competitors" part of R3 is met by existing institutions, and the formula levy lapses.
> - If the alignment tax is zero or private, so that divergences are corrected unilaterally (C9 favourable), common admission constraints lapse except for the decisive class.
> - If cross-boundary harm in a class is shown small, R2 lapses for that class.
>
> Where a condition holds, the text will say that regulated competition meets the corresponding requirement. It will not rename it, and it will not require it to meet the rest.

### 4.4 E2 的代价

L2200 "bounded and recoverable" 对延迟期间死去的人不成立（对抗 致命2）；但不把被放弃收益造成的分散死亡并入 O1，那会把 D 改成按生命计的期望值标准，并使第 1 步对两条路径同时失效（对抗复核）。改为：

> **Replacement (§9.3, E2).** Its cost, if AI turns out not to be decisive, is the delay of the decisive class's benefits over what non-decisive AI provides, including lives that earlier benefits would have saved. For those who bear it that cost is large and irreversible; it does not foreclose later choice. If AI is decisive, the loss E2 avoids forecloses choice for everyone. That is the asymmetry of irreversibility (Arrow and Fisher 1974; Henry 1974), stated with both sides counted. The size of the first side is crux C10; that O1 protects catastrophic, common-cause loss first is a value choice (V2), recorded under N1.

配套：§7.9 引 Jones 2024 的死亡率结果（死亡率减半时可接受的生存风险从约 4% 升到约 25%）；V2 处加一句"O1 protects catastrophic, common-cause loss; this is a value choice"；E2 自身的 O1 通道（覆盖靠强制→升级，Prop 7.5）进 $\Theta$（§4.2）。

### 4.5 §0 预测的条件性

L34 有 "on the present trajectory"，但强读法依赖 (X)(U)(φ)，而 L1159 自认它们是 cruxes（对抗 致命3；复核降为重要，分两层写）：

> **Replacement (§0, first paragraph).** This one predicts that, on the present trajectory, the logic of winning carries the participants toward an outcome none of them would choose. Part of that is shown: the contest dissipates what it contests and leaves every participant worse off than restraint would (Propositions 3.6, 5.2, 6.1). Part is conditional: if hazardous variety outgrows correction (Section 5.3), the loss reaches whoever would win, and a winner escapes it only by ceasing to compound (Proposition 5.13).

中文概要 L7 "谁都不想要的终点，赢家也不例外" → "谁都不会选择的结局；若危险的多样性超过纠错，这个结局也包括赢家"。

### 4.6 定义 7.12 的一致使用；7.2(2) 的 [A]；5.14 的结盟面

- **Def 7.12 描述性使用**（Codex 6；对抗复核 遗漏C）：改变选择 = 改变从行为到份额、资源与地位的映射，**不论方向**；方向、覆盖、可执行性、持久性分开记录。出口管制改变映射（方向：朝向领先）；以破坏相威慑作用于 $p_d$，与保管作用的量相同。L1732 一行相应改写。
  > Changing the selection means changing the map from conduct to share, resources and standing, in whatever direction. Direction, coverage, enforceability and durability are recorded separately; whether a change runs in the direction of Definition 8.1 is a second question, answered by the profile, never by the name.
- **7.2(2) 的 [A]**（胜前克制与胜后克制正相关）：撤回或给历史基率；T-I 事先定义"共同来源"，并纳入宪制纠错者（法院、选举、新闻）与外部可核查性；点名 Acemoglu–Robinson 的依赖量（赢家依赖被统治者的配合，AI 是否切断这一依赖是真正的分歧量，$\kappa$ 已隐含）；"Against a winner that restrains on the host, the objection is V3, not O1" 保留，附"the winner is itself a field"的限定。
- **制衡**（Waltz；Walt）作为不依赖技术的饱和机制进 C5 行；它在话语上的对应是 Prop 5.14 改写后的结盟面（$n\ge3$ 时两方可以针对第三方可信地谈话）：
  > Relative accounting silences talk between opponents and binds talk among allies: with three or more relative actors, two can speak credibly about a third (Proposition 5.14), which is how blocs form (Proposition 3.11) and how rising actors are balanced.

---

## 5. 生成的元吸引子与 Compact

### 5.1 生成之环的闭合：经由公地，不经由载体

§8.2 四股写的是约束，没有写出什么再生产"奖励贡献"这条规则（系统 F2.1）。但评审给的正回路"a rule that rewards contribution puts contributors in the positions that maintain the rule"正是科举之例（L1881）讲的病理，与第二股冲突（系统复核 F2.1、遗漏1）。**不要用它。**正确的闭合：

> **Key paragraph (new, §8.2 "The closure of the generative loop").** The generative loop closes through the commons, not through any carrier. In the pathological loop, success buys the rule that scores the next round (Definition 2.2). In the generative loop that step is cut: success cannot buy its own assessment ($\chi\to0$). The rule is maintained instead by what the rule produces and no one owns: the common layer $K_0$, correctors funded by formula and keyed to no one, and the whole-system loop from security through trust, cooperation and abundance to slack, care and better order. Support that no carrier can claim cancels from relative selection (Appendix A.4), so the generative order is not selected for at the level of carriers. Like a constraint common to all, it is invisible to the selection that would displace it (Lemma 3.3(2)), and it persists through coverage, through funding by formula, and through the surplus the loop generates. That is why its persistence is a conjecture [C] to exactly the degree that coverage can unravel (Section 8.5). Who selects the correctors is the generative form of selecting the selectors, and Section 4 applies to it: the answer is not a trusted body but a formation rule no participant controls and a certificate at every node.

这回答了 §8.2 的四问中的第一问（怎样持续获得资源：公式供资 + 整体层面的丰裕回路）和第四问（守护者测试：§5.9）。"同一个反身结构"的说法保留，但注明反身性在系统层（秩序供养维持其规则的纠错者），载体层的那一步被切断——这是提升，不是撤回。

### 5.2 底座供给作为 $K_0$

Remark 5.3 的 $\chi$ 实为分享参数；不可转换单独不能稳定地位；只有存在不靠赢得的能力来源 $K_0$ 时可转换性才起作用（数学 F2；系统复核 F2.2；综合 §二.2 已在 `syn60/k0.py` 验证，系统复核 60 例 59 例吻合，1 例在等号）。形式由 Q1 定稿；本文写它的含义：

> **Key paragraph (§8.2 third strand, and Section 8.4 after Proposition 8.6(3)).** Provision beneath the game has an exact place. In the compounding condition let $K_0$ be capacity that no one won in the contest: common infrastructure, baseline services, shared reference systems. Equal standing is unstable iff $\kappa_c\,\Omega\big((1-\beta)r-1\big)>n\delta K_0$ [T; N]. Sharing ($\beta$), convertibility ($\kappa_c$) and decisiveness ($r$) do not act alone: with $K_0$ large relative to what winnings can reinvest, equal standing is stable even where winnings compound. Trees are $K_0$, provision that maintains the system without becoming it. For carriers it is a floor of capacity independent of share; for persons it removes the ground of the belief that one is in a struggle for survival (crux C8). The two levels are kept apart: the first is a result in the model, the second a conjecture about minds.

这同时解决第三股的层面错位（系统 F2.3）：$K_0$ 作用于载体的生存函数（企业：不依赖份额的能力底座；国家：基线服务与共同保管压缩生存差，Prop 8.9(4)），"增益"作用于人（C8）。V5 "奖赢家以别种货币"落在 $\kappa_c$ 上，但只有与 $K_0$ 一起才起作用；Compact 的公共层就是 $K_0$。总结句改为"分享与可转换性都能稳定地位，都不改变强度选择的符号"（数学 F2）。

### 5.3 覆盖的解体与退出

Lemma 3.3(2) 的保护只在全覆盖时成立；大参与方退出后，剩下的约束成了单边约束，会被选择淘汰，可能连锁（系统复核 遗漏3；Barrett 2003）。第四股 "exit… selection with the opposite sign" 与 Def 8.1(a) 冲突（系统 F2.4）。改为：

> **Key paragraph (§8.5, new).** The protection of Lemma 3.3(2) holds only while coverage is complete. If a large participant leaves, what remains is a constraint borne by some and not by others, which selection displaces; the remaining members are then selected against, and exit can cascade (Barrett 2003). Two kinds of exit are therefore kept apart. Exit from a provider or a service, with free association, is selection with the opposite sign, and the design keeps it cheap. Exit from a common constraint is not an option the design offers. The constraint is in force only above a registered coverage threshold, enforced by conditions of market access for non-participants; below that threshold it is suspended rather than borne unilaterally, so that compliance never becomes a unilateral cost. Stage 3's market-access condition is this threshold, written as a participation certificate.

压力测试 "Succession and withdrawal" 加第二次、第三次退出的连锁情形。

### 5.4 Compact 按功能拆分：纠错在被纠正者之外

Compact 把出资、所有权、评估任命、立规、执行、保管捆在一起，又自己拥有评估基础设施（L2053），而 L1928 要求联合项目的纠错在项目之外（系统 F1；系统复核 F1.2、遗漏2）。保留候选地位，按功能拆：

> **Key paragraph (§8.6, before the Compact table).** Correction sits outside what it corrects. Three functions are never held by one body: revising the levy formula, appointing evaluators, and executing remedies. Each has a certified row sum, and a decision of any one is reviewable by another. The Compact's own conduct, its use of the common layer and its allocation of the services fund, has a corrector that it neither funds nor appoints, because a project that owns the evaluation infrastructure is itself the largest carrier the theory describes (Proposition 4.2; Section 8.4). The candidate below is therefore not one institution but a set of functions with the separations marked.

表中加一列"不得同处一机构"，并加一行 "Dissolution and withdrawal of powers"（§5.6）。

### 5.5 议院的形成规则与行和证书；回退止于证书；谁定标准

"chamber" 全文五次，从未说明形成方式、谱系、行和；评估者的任命者也没有说明（系统 F1.3；复核：回退应止于可在公开数据上重算的证书，剩下的落在"谁定标准"）。改 L2049、L2057、L2064、L2093：

> **Key paragraph.** The chamber is a corrector, and Section 4 applies to it. Its members are drawn by a rule no participant controls, by lot weighted by population and exposure or by nomination from plural lineages; they rotate; and its inbound row sum is certified like any evaluator's. Evaluators are appointed by a body in which no provider and no single state votes decisively, and their row sums count conversion from states as well as from providers (Proposition 8.8). The regress does not end at a trusted body. It ends at nodes each of which is certified, by certificates that several parties can recompute from public data. What those certificates cannot certify is who sets the standards they use; that function is designed the same way (the standards row of the function table), and it is the one place the regress still points.

### 5.6 退场条件：保管，以及输入限制回退

Def 8.10 要求每个闭合说明什么会使它退场；表中紧急权、日落、复审已有，但 Compact 自身、保管、"collective restriction of frontier inputs" 没有（系统复核 F1.1）。后者是强制，正是 §7.6 "does not endorse" 的拒止，必须按 §7.6 对预防的处理对待（对抗 次要14 升重要；对抗复核 遗漏H）：

> **Key paragraph (table row "Dissolution and withdrawal of powers").** Custody states what would end it. Custody of a capability class converts to verification when detection is shown faster than breakout for that class (C7); it is released $k$-of-$n$ when the class is shown to saturate (C5); and it lapses when the class is rolled back below coverage. The fallback of collective restriction of frontier inputs is coercion. It is treated as Section 7.6 treats prevention: it falls under Proposition 7.5; it carries a sunset and a $k$-of-$n$ release; it bears the evidence burden of an adverse finding; and the theory does not derive that its net effect is positive. It is the hard case, stated as such, not a remedy. Emergency powers already state what would end them; so, now, do custody and the fallback. The Compact itself dissolves to the institutions of Stages 1–3 when the registered coverage threshold is not met for a stated period.

"No participant can revise a purpose while it is under assessment" 改为明确的回避规则（它指参与者，不指目的），并写明"立案"由谁、以什么证据宣布，以免成为冻结修订的工具。

### 5.7 课征公式作为奖品；国家计入行和；快慢回路

- 课征（系统 F8.1、F8.2；复核补两点；遗漏4、6）：
  > The levy formula is a prize, and Proposition 4.2 applies to it. It is fixed for stated periods; revision needs the supermajority and the chamber; its revisers are separated from its beneficiaries and certified. The correction fund is indexed to the coverage each hazard class requires, $d^\ast(t)$, not to the field's capability, and its revenue base is decoupled from the activity it constrains, so that correction neither becomes a stakeholder in growth nor shrinks under E2. After the host recovers, the mobilization of Remark 4.5 falls back toward $d_0$ and a certificate can lapse; that cycle is listed among the compensating loops of Section 9.4, and the index to $d^\ast(t)$ is what holds against it.
- 快慢回路（系统复核 遗漏4）：
  > Supermajorities and the chamber sit on the slow loops: revision, formula, standards. The fast loop, restriction of a specific capability, stays fast and is reviewed after the fact, because every veto point adds delay to the margin of Proposition 5.11.

### 5.8 功能→形态表补两行，一行改写；联邦例证更正

补行（系统 F6.1、F6.2；复核加"变体只在共同地板之上"）：

| 功能 | 机制上的要求 | 由此得出的形态 |
|---|---|---|
| Learning about the design itself | For irreversible, planet-wide failure there is no second attempt (Lemma 3.10); reversible failures can be learned from | **Bounded parallel variants above the common floor**, with shared evaluation; adoption by evidence. Variants below the floor would turn the common constraint into a unilateral one (Lemma 3.3(2)) |
| Who sets standards | Standard-setting is a keystone domain (Proposition 4.8(3)) and the first target of Goodhart | **Certified standard-setters**: row sums below one, rotation, pre-registered held-out indicators, revision on the slow loop |
| The frontier（改写） | Merging lowers the race at the first order and raises the return to influence at the second (Remark 8.7) | **Merged accounting and custody of the frontier, plural lineages inside, correction outside** |

联邦例证（系统 F6.4；复核更正：均等化对国家不只减速）：

> **Replacement (§8.6 "Federations as an illustration").** A federation shows the pattern. Members compete for capital and residents; the strongest can capture the centre. What changes the selection is a common floor of minimum standards, which no member is selected against for meeting, and limits on the centre that keep correction outside the strongest member. Fiscal equalization is pooling: among members that act on their own payoffs it widens the effective self (Proposition 8.6(1)); it does not by itself change what winning confers. The federal lessons that carry over are second-order: equal representation of small members and supermajorities for constitutional change, the precedent for voting not proportional to compute; and a common minimum tax across jurisdictions, with its leakage, as a living instance of one rule for all. The same form can select for winning or for contribution; what decides is what it rewards.

### 5.9 守护者测试的肯定式

§8.7 开头现在只有否定式（"No better guardian is an answer"）。加一句肯定式，并把改革两难放在它前面（§6）：

> No better guardian is an answer. The regress ends at certificates, not at bodies: a structure in which every guardian is guarded is one in which every node's independence can be recomputed by others from public data, and the one function that cannot be so certified, the setting of standards, is held on the slowest loop with the most hands.

---

## 6. 恢复丢失的内容

忠实评审及其复核认定的损失，逐项给去处与形式。全部按 R／A／I 标来源，记入 CLAIMS 与附录 F。

| 项 | 来源 | 去处 | 形式 |
|---|---|---|---|
| 关系自我与大同（自我层说明） | R（2026-04-12、04-19、05-05；生生不息论第十八章） | §3.8(3) 末；§8.1 的两句归入同一理论 | 一段，见下 |
| $\kappa$ 随力量上升的收敛猜想 | v5.2 L165–166（A，Ren 采纳） | §3.6 末；接 5.16 后文与 C-crux | [C]，见下 |
| $\theta_g$ | v5.2 L149 | Prop 5.2(3) 第二句（Q1 复核公式） | [T] |
| 改革两难 | R（2025-06；2026-10-02 [00:35:16]） | §8.7 开头；接 §9.4 补偿回路 | 一段，见下 |
| 四回路写成回路 | R（2024–2025 语料） | §2.3 表后 | 一段，见下；账本记"§2.3, as loops"，不改成"three products" |
| W→C→N 互持回路 | v5.2 L115–120 | §2.5 签名表后 | 三句，见下 |
| "unbounded relative objective" 定义 | v5.2 L821 | §7.12 开头（L1785），或 §2.6 Ψ 末 | 一句，见下；修复 L1585 的悬空使用 |
| 五种终局 | R（2025，`01-writings-2025/prompt.md`） | §5.5 剪刀差后新小节，或 §5.6 末 | 一段，见下 |
| 攻防框架双重危险象限 | v5.2 L832 | §7.12 L1798 | 一句，见下 |
| "Continuation relies on the third alone… The pivot works on all" | v5.2 L195 | Prop 5.4 四杠杆后（L936） | 一句，见下 |
| NVF 语言机制（词汇逃出游戏；框架锁死；总体化群体的意义结构） | R（2026-04 机制篇；10-02 口述） | §5.4 "Narratives" 段 | 一段，见下 |
| 内生域与认识封闭四级（ASTRA） | v2 评审 | §10.6 一句 | [C] |
| 账本错误 | — | 附录 F、CLAIMS、CHANGELOG | 见下 |

**关系自我与大同（§3.8(3) 末）。**
> Accuracy about one's boundary is the formal face of the author's account of the relational self. A self is not a point outside its relations that afterwards enters them; it is the action-centre of a knot of relations, body and nature, care, language, recognition, institutions, and its own corrections. "We are the ecology of our cells," and at the next scale we are the collective we belong to (我们即是集): one can be an individual and cannot disregard the whole, because one is part of what the whole is doing. That is why the theory needs neither pole of the individual–collective axis. The direction it names is 大同, understood as harmony and not sameness: difference entering a relation in which the parts check and complete one another (和实生物，同则不继). Where power reaches, responsibility follows (力之所及，责之所在): a larger causal radius brings a larger share in maintaining the whole, not a larger entitlement over it (Section 8.1).

**$\kappa$ 随力量上升（§3.6 末）。**
> Convergence [C]. For a planetary technology the unpriced coupling $\kappa$ plausibly rises with power: the host is shared, failures propagate through common infrastructure, and the harms that prices do not settle grow with what is contested. If so, accuracy and inclusion converge in the long run, and understanding that we are one becomes first of all a matter of seeing correctly. The measurement is the growth of unpriced coupling (EV13; Section 10.3). Until it is measured, the step from an accurate self-model to objectives under which restraint is a stage equilibrium has to be built by institutions (Section 6.1; Theorem 5.16).

**$\theta_g$（Prop 5.2(3)）。**
> The total material payoff stays positive at every scale if and only if $\theta\ge\theta_g=(r(n-1)-1)/(1+r)$, and $\theta_g$ rises with $r$. In the example $\theta_g=1$: the accurate self-model $\kappa=0.4$ lies below it, which is the quantitative form of the gap between accuracy and inclusion.

**改革两难（§8.7 开头）。**
> The reform dilemma comes first. The path to the influence that correction needs runs through the game that selects against correction: one does not correct the trajectory but plays on it, because playing yields influence and correcting requires it. Whoever reaches the position from which the rules could be changed was selected by the rules as they are (Section 2.2). Every remedy below is therefore tested on the corruption of the constraining mechanism itself, and the staged path of Section 9 is built so that each stage is held by actors the previous stage did not select for winning.

**四回路（§2.3 表后）。**
> The author's corpus writes the mechanisms as four loops closing in series. Winnings convert into the capacity to win, so advantage accrues to advantage, and balanced practices are out-competed, not refuted (Remark 5.3). The winners reach the positions where rules are written and rewrite them, so that rivals must adopt the same practices to survive and must assume that everyone else already has (Section 4; Proposition 7.2). Accumulated power buys discourse, so the winners' logic becomes the common sense in which the next generation is formed and, at the limit, "human nature" (Section 2.4(3); Section 5.4). And the regulator that every society keeps against exactly this, norms, law and shared understanding, regulates only if it updates as fast as the world changes; the lag between the two is produced by the first three loops (Section 5.3). Winner takes all; winner justifies all.

**W→C→N（§2.5 表后）。**
> The signatures sustain one another. W supplies the success that C converts into control; C removes the correction that would make the shared visible; N makes cooperation look naive, which keeps W in place. Section 4 is the formal account of this loop.

**Unbounded relative objective（§7.12 开头）。**
> Call an objective *unbounded relative* if it ranks relative standing on the decisive dimension without any point of enough (Proposition 8.11(3)). It is the winning model in its purest form, Ψ1 at $\theta=-1$ with Ψ2 certifying the winner and Ψ3 compounding the win, and cancer is its exact image.

**五种终局（§5.5 后）。**
> The author's corpus lists five endgames of a contest under this pressure, and each has a place in the results. (i) A freeze in mutual deterrence, where any move is suicidal and each believes the others rational: Branch I′, saturation (Theorem 5.15), and the no-war condition of Remark 5.6(1). (ii) A deadlock by frozen power structure, a consensus among the remaining players that holds only while they believe it will not be violated: a closure that cannot say what would end it (Definition 8.10). (iii) A change of narrative that lets them see themselves as one whole and so recover the ability to cooperate: Section 3.8 and Section 8; this is where "we are one" enters the corpus, and it is the only generative endgame. (iv) Keep going and collapse: Theorem 5.12; Remark 5.6(3). (v) Winner takes all: Proposition 5.10; Theorem 5.16(2). The judgment of Section 10 is that (iii) has to be chosen before any of the others is reached.

**攻防象限（§7.12 L1798）。**
> AI sits in the doubly dangerous quadrant of the offense–defense framework (Jervis 1978): offense has the advantage (P1), and offense and defense are hard to tell apart (dual use), so cooperation is hardest there. A hazard in development acts as a negative payoff to the offense, as a weapon that endangers its holder does.

**继续只用第三个杠杆（Prop 5.4 后）。**
> Continuation relies on the third lever alone, correction, while it keeps the contested stakes growing, leaves the objective where it is, and cultivates influence over the correctors. The change argued for here works on all four.

**NVF 语言机制（§5.4 Narratives 段）。**
> The author's corpus gives the mechanism three further parts. Vocabulary escapes the game that coined it, so words that scored moves inside a contest ("realistic", "competitive", "winning") come to describe the world outside it. A group that totalizes itself orients its whole structure of meaning toward its own continuation and shapes the others around it as a model generates tokens; those inside cannot voluntarily feel that their ideas are wrong. And by the time the frame is noticed, one is already thinking inside it, which is why the frame is the highest leverage point and the one that facts and shame cannot reach.

**账本。** 附录 F 分三栏：Restated at the level of game and selection（一个根；增长需扩展自我；设计被再吸收；三区为主定理）／Corrected（分享反转→缩小；谱系国别）／Withdrawn（数值；分享的是决定性地位；$\theta=n-1$ 等于一体）；CLAIMS §7 与 CHANGELOG L40／L86 用同一组词。改正："环境奖励什么，心就推举什么"在 §3.6 不在 §3.3（CLAIMS L156 同改）；P4.1 行记 6.1(5) 为 v6 新增；P5.11→6.9 记第 (2) 款重算与新增 (3)(4)；Remark 4.7(4)、Prop 4.10 的系统评审增补记入；§4.6 两处删除记入；v1 五个区分在 §4.1 表中，记功。

---

## 7. 检验与分歧

### 7.1 改写的检验

| 检验 | 改法 | 本文预测 | 对立预测 |
|---|---|---|---|
| T-B | (i) 测标度：影响支出随份额超线性（$p^2$）；三阶矩而非 HHI。(ii) 改为可失败形式 | Incumbents oppose non-appropriable correction (mandated access, arm's-length funding) even where it raises rivals' costs more than their own; support for such correction at net cost to themselves refutes the channel | 游说与收入成比例；支持抬高对手成本的义务（Stigler，本文也预测，故不列为区分） |
| T-C | 承认防御性现实主义也容许意图信号；残余是**可转换性对信号效应的调节** | Costly, hard-to-reverse signals of intent (Proposition 9.3) lower intensity, and their effect is larger where what winning converts into is smaller | 只有能力信号重要（进攻性现实主义）；意图信号有效但不受可转换性调节（防御性现实主义） |
| T-D | 限于无沉没成本解释的行为 | 撤回改变选择的规则后，行为不完全回复 | 在快松弛时间内回复 |
| T-E | 降为探索性 [C]；控制共同冲击 | 单因子与慢变量 | 两因子（现实主义加普通竞争）——合法对手 |
| T-F | 事先独立测量"归属"（学说编码、问卷），不作逃逸条款 | Organizations with capped or non-convertible rewards show T1–T6 only where measured attribution is high | T1–T6 在低归属、不可转换奖赏下仍出现（技术动量） |
| T-G | **改号**（Remark 5.9：$\theta_{\text{rep}}$ 随 $p_d$ 上升；由 Q1 从修复后的执行条件推出比较静态再登记）；加 $K_0$ 维度 | As $p_d$ rises the sustainable set depends more on objectives and less on punishment; changing convertibility changes conduct; adding capacity not won in the contest stabilizes standing | 目标在任何 $p_d$ 下无效（现实主义）；只有外部性重要（多极陷阱） |
| T-H | 改标为第二层触发指标，不作理论检验 | — | — |
| T-I | 事先定义共同来源；纳入宪制纠错者与外部可核查性 | 行和 ≥1 则良性赢家路径不过 D4 | 行和 <1，§7.4 须据实改写 |
| T-J | 要求超出正常规划滞后的领先，并与非竞赛框架的变化对照；否则降级 | — | — |
| T-K | 标明是对已吸收理论的确认；或改为测 (4) 的标度 | — | — |

### 7.2 新增的检验

| 检验 | 测什么 | 本文预测 | 对立预测 |
|---|---|---|---|
| **T-L** 哪些偏差被修正 | 私人成本偏差（用户可见作弊、谄媚）与共同或迟发偏差（第三方伤害、评估博弈、不透明推理）的修正时间 | Privately costly divergences are corrected within one or two release cycles; common or late ones persist until a common constraint or an attributable incident | 两类修正得一样快（对齐税为零或私人） |
| **T-M** 能让 C2 失败 | 两个领先辖区的强制独立访问与 arm's-length 供资 | If such correction is in force by a stated date, has held for at least one dwell time (Section 9.4), has executed remedies, and incumbents' share has grown in the same period, C2 is refuted for that period | — |
| **T-N** 结盟的谈话 | $n\ge3$ 的竞争者之间关于第三方的沟通信息量 | Talk between two rivals about actions against a third is informative; talk between the same two about their own standing is not (Proposition 5.14) | 相对行动者之间一切谈话皆噪声 |
| **T-O** $K_0$ 与地位 | 跨领域：有公共基线能力的领域与无的领域 | Where capacity not won in the contest is large relative to convertible winnings, equal standing persists under compounding | 地位集中只取决于 $\kappa_c r$ |

保留：植入缺陷捕获率随能力下降（(U) 的检验）；委托饱和前实现风险不降（Prop 6.11）。

### 7.3 新增的分歧

| 分歧 | 内容 | 现有证据 | 会改变建议的 | 下一步测量 |
|---|---|---|---|---|
| **C9 对齐税** | $(A_\tau)$ 的符号与归宿：对共同成本偏差的修正是否降低相对收益 | 行业普遍采用 RLHF（既安全又提升能力）；可监测性与安全训练的能力差距未系统测量 | 若为零或私人，共同准入约束只对决定性类保留 | 安全训练带来的能力差距；发布延迟；可监测性税；T-L |
| **C10 E2 的被放弃收益** | 决定性类相对非决定性 AI 的边际收益被延迟的规模，含死亡率（Jones 2024） | 未估计 | 若规模与所防灾难同量级，E2 的触发阈值须上移；规范部分归 N1 | 决定性类独有收益的分项估计 |

C4 加入"保管者被俘获→O2"与"强制执行→升级"两支；C5 加入制衡作为饱和机制；C7 不变。编号：对齐税为 C9（与综合一致），E2 代价为 C10（对抗复核指出的编号冲突）。

---

## 8. 交接清单

**grep 词（全部要改）：** `oneness is a gain`、`oneness is not necessary`、`'We are one' becomes a necessity`、`That the lemma leaves only this route`、`cannot be discovered by selection`、`bounded and recoverable`、`One pressure`／`one pressure`（视 §1.6 情形）、`the formal reason coordination works`（3.3(2) 从"新贡献"移到"吸收"，新的是它与执行条件和俘获的连接）、`whose outermost reward is set by the pressure of winning`、`Power-seeking emerges where advantage compounds`、`no way of coordinating`、`No retention of decision policies by`、`no service as an instrument in a game`、`Interventions at the level of parameters are re-absorbed`、`By design; to be tested`、`collective restriction of frontier inputs`、`Protections entrenched`、`fiscal equalization`、`Correction becomes harder. It falls behind`、`Supported |`（Ψ 行）、`(E2 or E3)`、`six dimensions`、`Price 1970`（→1972；Hamilton 1975）。

**传给 Q2（结构）的句子：** 概要 L7、L16、L23 的三处改写；§1.2 第 1、3、5 条；"政权"→"区间"；"二阶公共品"→"竞争者自己供给不了的纠错"；"阶段均衡"→"不靠未来惩罚也会自觉遵守的那部分"；§2.4 由并列改为链；§5.5 后的五种终局小节；§8.2 新增"闭合"段；§8.5 新增"覆盖与退出"段；§8.7 开头的改革两难与肯定式守护者测试；§10.1 三层。

**传给 Q1（数学）的接口句（本文已按其成立写作）：** 执行条件；$K_0$ 条件；Lemma 3.3(2′)；Lemma 3.10 改写；Prop 5.14(1) 的 $n\ge3$；Prop 6.7 加 $(A_\tau)$；Prop 7.10 三栏；$\theta_g$；T-G 的比较静态；$\chi$ 记号拆为分享 $1-\beta$、可转换 $\kappa_c$、可占有 $\chi$。

**不要做的事：** 不写"贡献者占据维持规则的位置"；不把被放弃收益的死亡并入 O1；不把共同保管整体移入条件层（准备与触发在第一层）；不用 Fable 忠实评审给的 5.16 替换句；不把 EV1 软化（按原文写全 stick 与 carrot，三栏对称）；不点名国家或企业；不把受监管竞争写成"只有满足 R1–R8 才算赢"；E2 与 E3 不互换；结论保持肯定式。

**估时（综合 §七）：** 本文各项约 6–10 小时，次序：§2.4 滑回替换与 §4 三层（承重）→ §1 链与残余 → §5 闭合、$K_0$、Compact 拆分 → §3 → §6、§7。
