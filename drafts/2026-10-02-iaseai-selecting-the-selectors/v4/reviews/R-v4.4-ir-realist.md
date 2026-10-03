# 评审：No Winning Position v4.4 —— 国际关系与战略研究视角（第二轮）

*评审对象：`v4/THEORY.md`（v4.4，2026-10-03，2271 行）。评审视角：持怀疑态度的结构现实主义者与讨价还价理论学者（Waltz、Mearsheimer、Jervis、Schelling、Fearon、Powell、Grieco、Glaser、Kydd；核战略、军控、预防性战争、安全困境、攻防理论）。本评审由 Claude (Opus 5.5) 撰写，是独立评审，立场是程序委员会中最强、也最公平的批评者。*

*阅读范围：*
- *THEORY.md 全文，包括附录 A（证明）和附录 C（对上一轮各条的处理）；*
- *上一轮本视角评审 `reviews/R-v4.3-ir-realist.md` 与 `reviews/SYNTHESIS-v4.3.md`；*
- *`THEORY-v4.3.md`：对照了第 3.5 节、第 9.5 节的 Precedents、"Relative gains"两段和 Theorem E 的陈述；*
- *Ren 的方向文件 `sources/16-claude-code-directions/2026-10-03-v4-direction-cooperation.md`，尤其最后两节；*
- *`checks_v44.log`。*

*未运行脚本。文中凡是本评审自己算的数字，都标明为"示意计算"，参数由本评审选定，不是稿件的。引文按本评审者的知识核对，没有把握的地方标"需核对"，未编造。*

---

## 1. 总体判断

### 1.1 进步是实质性的

v4.4 认真回应了上一轮的核心意见：
- **生存比较改成了区域形式。** Proposition 23(2) 给出无需信任的区域；危害随分支变化，$q^P_{\mathrm{II}}\ge\max(q^T_{\mathrm{II}},q^S_{\mathrm{II}})$。稿件还坦白承认：面对一个必然竞赛的对手（$\varpi=0$），在区域之外，生存优先本身给不出克制的理由（§2.3、§10.3、§13）。这正是上一轮 IR1(c) 要求的诚实，也是让现实主义读者继续读下去的前提。
- **L6 不再免疫化。** 边缘政策被归为生存意义上的胆小鬼博弈，不再被改称"癌性"。
- **"癌性"只剩一个定义。** 有了技术名 unbounded relative objective，结构来源（无政府、决定性、无承诺装置）也得到承认。
- **威慑被重读为通往 E2 的尝试。** 更低的 $c_A$ 的两个相反效应都写出来了。
- **核先例与四点不同第一次进入正文。**
- **极限不再是前提。** 它们改由 (X)(U)(φ)、Lemma D 和 Proposition 27 推出。

因此，面向 IR 的核心主张现在可以作为一个**有条件的防御性现实主义命题**来辩护：若 (φ) 成立、对手是生存优先型，竞赛就是一个信任门槛沿竞赛趋于零的猎鹿博弈。这比 v4.3 强得多。

### 1.2 但"现实主义者自己的第一前提导向合作"这一挪用仍然站不住

原因有四。

**第一，前提只是搬了家，没有被消除。** 争议从"$q\to1$"挪到了四处：
- (φ)：不可逆失败模式的每期危害有正下界，而且永不下降；
- (X) 中"需要覆盖的危害多样性"指数增长这一步；
- L3：AI 决策的速度优势无界增长；
- Lemma D 对"生存"的定义：自主包括代表本方在共同项上的利益。

§0 说承载结论的是"竞赛者自己的前提（P1、P2）加上 (U)"，这低报了 (φ) 和 L3。而 Proposition 27 恰恰是现实主义者自己的论证（承诺问题，加上对意图的不确定）：它让落后更致命，并抬高地位向生存的转化率。所以，一个接受 Proposition 27、拒绝 (φ) 和 Lemma D 生存定义的现实主义者，用稿件自己的 Theorem S 机器就能推回竞赛的理由（N2、N3、N7、N9）。

**第二，个体判据与集体判据之间有一次切换。**
- Theorem S 用的是个体判据：每个行动者自己的 $\Phi_i$，按 L6 排序。
- Lemma E0 和 Theorem E 排除"消灭"时，用的是集体判据，即"every actor's survival"。v4.3 的 Theorem E 原本是个体判据（"some actor's survival"），v4.4 为了处理 A3 改成了集体判据。
- 在困难情形下，$\Phi^S\to0$ 意味着任何生存概率有正下界的行动都优于克制，包括预防性打击和 MAIM 式的破坏。
- 按稿件自己的对称数值，只要灾难性升级的概率低于约 0.79，预防就同时优于留在外面和加入（N1 的示意计算）。
- 更麻烦的是：沿着竞赛，慑止一个生存优先者发动预防所需的升级概率趋于 1。也就是说，L6 取消了 Proposition 8(4)"高昂的战争成本慑止预防"。

现在的形式化，等于在不知不觉中为 Ren 自己说的"导弹直接冲着数据中心去"提供了生存论证。对面向现实主义者的挪用，这是致命的，但可以修复。

**第三，核先例这一步走对了，但写得太薄，有事实错误，与 §8.5 的判定也不一致。**
- 冷战记录说明的是：当自然提供饱和（有保障的二次打击）、危害集中在使用时，对手在保持对抗的同时活了下来。
- 对手以协议放弃一类能力，只发生在这类能力被普遍认为昂贵或效果存疑的时候（ABM）。被认为有决定意义的能力（MIRV、精确打击力量）没有被放弃。
- 所以这份记录支持的是 Corollary 1（先降低赢的价值，协议才便宜），而不是"在相信决定性时，对手可以靠协议实现 E2"。
- 稿件把冷战的"E2 held under (K)"算作出口的证据，把 Plan A 的"E2/E3 held under (K)"判为伪解，又把自己的"E1 held in common under H0"算作真正的出口。三者需要同一个标准（N6、N8）。

**第四，过渡机制里有两个可以直接指出的错误。**
- Corollary 2 说，各方在共享危害上利益一致，所以关于它的信息可信。可 Proposition 14 自己的偏差例子（发送者希望接收者"比状态所需的更克制"）正是关于共享危害的报告，偏差 $b=\lambda\beta_s>0$（N4）。
- "竞赛本身扩大这个区域"没有证明，而且被 `checks_v44.log` 中 Proposition 24 的反例路径直接反驳：沿该路径，$\Phi^S/\Phi^P$ 从 0.18 降到 0.02（N3）。

### 1.3 总体建议

1. **改写面向 IR 的一句话主张。** 建议写成："若 (φ) 与 L3 成立（证据如下），对生存优先型国家，竞赛是一个门槛趋于零的猎鹿博弈；在困难情形下，没有任何生存位置，预防者也不例外，因为持续预防本身就是一条竞赛分支。"后半句要成立，需要 N1 中的 Lemma P。
2. **把"生存"收窄到现实主义者认得出的含义。** $q_{\mathrm I}$ 应写成共享危害和机器速度升级的放大器，而不是定义上的死亡（N7）。
3. **用一个标准统一判定冷战、Plan A 与 E1。** 这个标准是：在 H0 下，任何安排的持久性都取决于赢的价值是否下降（N6）。

### 1.4 新问题的严重度一览

| ID | 问题 | 严重度 | 主要位置 |
|---|---|---|---|
| N1 | 个体判据下，困难情形推荐预防；Lemma E0 只靠切换到集体判据排除它；L6 使 Prop 8(4) 失效 | 致命（就现实主义挪用而言） | Thm S；§10.4；Lemma E0；Thm E；Prop 8(4) |
| N2 | 前提搬家：(φ)、(X) 的危害多样性一步、L3、Lemma D；§0 的认识论陈述低报了它们 | 严重 | §0；§10.2；§12 |
| N3 | "竞赛扩大区域"被稿件自己的数值反驳；$c_{\text{conv}}$ 是定义而非推导，且 Prop 27 推高它 | 严重 | §2.3；§10.3；Prop 24 |
| N4 | Corollary 2：共享危害的报告仍有正偏差，与 Prop 14 冲突；参数是私人的 | 严重 | Cor 2；§7.2；§14 |
| N5 | 困难情形与"两类型结果"：断言而非推导；覆盖要求隐含强制；缺少类型不确定；Jervis"双重危险"象限未处理 | 严重 | §10.4；Prop 22(4)；Prop 24 |
| N6 | 同一结构三种判定：冷战（证据）、Plan A（伪解）、E1 共同持有（出口）；对 Plan A 的判定措辞不公平 | 严重 | §10.7；§8.5；Thm E(2)–(3) |
| N7 | Lemma D：现实主义者认不出这种"生存"；把选择规则的结论搬到战略行动者身上 | 中等（偏严重） | §10.1；附录 A |
| N8 | 核先例：事实错误、饱和论之争、漏掉关键先例；实际说明的东西与正文所说不同 | 中等 | §10.7；参考文献 |
| N9 | Prop 27：一半是现实主义自己的论证（因而帮的是竞赛），一半超出命题的地位 | 中等 | Prop 27；附录 A |
| N10 | 对 MAIM 的批评建立在不可观测性上，与"E2 最可核查"冲突；在大国之间，可信性才是首要问题 | 中等 | Prop 25(1)；§10.5 |
| N11 | P1 二难与 P2 二难都不穷尽；"E2 costs nothing"不成立 | 中等 | §10.7；§10.2；§8.4 |
| N12 | Theorem E(2) 的长期必要性依赖 L3，L3 仍是假设，且没有反驳条件 | 中等 | L3；Thm E(2)；§12 |
| N13 | $\Phi^R$ 需要可和的残余危害，人类制度难以满足；应比较危害率 | 中等 | Thm S(2)；§12 |
| N14 | 第 8 节仍把不持有 (A) 的方案列为该立场的形式；(S) 的集体定义使 Prop 29(5) 成为定义性的；漏掉领先者的窗口逻辑 | 中等 | §8；Prop 29 |
| N15 | Lemma E0 的二分不穷尽：瓦解与和解 | 小 | Lemma E0 |
| N16 | 措辞与引文的残留（附录 C 漏列 IR18） | 小 | 多处 |

---

## 2. 上轮条目核验表（IR1–IR18）

附录 C 的标记：
- "Done"：IR1、IR3、IR4、IR5、IR8、IR9、IR15、IR16、IR17；
- "Partly"：IR2、IR6、IR7、IR10–IR14；
- IR18 没有列出。

下表逐条判断修复对 IR 读者是否成立。

| ID | 上轮问题（简） | 附录 C | 本轮判断 | 理由与残余 |
|---|---|---|---|---|
| IR1 | Theorem S 把相对收益论证吸收进条件；L6 下极限偏向加入；危害不随策略组合变化 | Done | **部分成立** | 已做：区域（Prop 23(2)）；分支相关危害；承认 $\varpi=0$；§2.3 与 §13 的句子已改；L6 的比值形式；Theorem S(3) 改为风险占优与颤抖手完美。残余：（a）"the race itself enlarges that region"未证明，且被 Prop 24 的路径反驳（N3）；（b）$c_{\text{conv}}$ 只是乘法定义，不是 Powell 式的推导（N3）；（c）争议被搬进 (φ) 与 Lemma D（N2）；（d）时间口径的不对称改成了"$h_R$ 可和"的条件，而这个条件在经验上很难满足（N13）。 |
| IR2 | 生存博弈漏掉预防分支和不对称领先者 | Partly | **未成立，而且更尖锐了** | Lemma E0 只论证了目标失去生存，没有给出攻击者的 $\Phi^{\text{Prev}}$。Theorem S 让 $\Phi^S\to0$ 之后，预防对个体生存最大化者更有吸引力，L6 还取消了 Prop 8(4) 的慑止（N1）。不对称领先者部分有改进：K7 段改为"对最强者需要比较租金与损失"，Lemma M 用于孤立竞赛者；但这依赖胜后仍然复利（N14）。 |
| IR3 | 核革命、威慑、军控缺席；冷战是反例 | Done | **部分成立** | §10.7 写出了四点不同、ABM 和 P1 二难，方向正确。残余：事实错误（弹头不能用国家技术手段计数；部分禁试条约不是 E2；"fastest arms race"）；饱和论在核领域本身有争议；P3 没有进入任何定理的假设；漏掉 Baruch 计划、1945–49 年的核垄断、生物武器公约、核不扩散条约；与 §8.5 的判定不一致（N6、N8）。 |
| IR4 | "生存包含自主"拉伸了 Mearsheimer；委托不等于失控 | Done | **部分成立** | Lemma D 给出了一个机制，$q_{\mathrm I}$ 与共享的失控也分开了。但 Lemma D 失去的是"代表本方在共同项上的利益"，这不是现实主义意义上的生存；Lemma D 还把 Lemma 0（选择规则）用到 L6 行动者的选择上，违反 §1.7 规则 1。军政关系与核指挥控制文献仍未用来支撑 Lemma D（N7）。 |
| IR5 | 威慑与 MAIM 只看一面；与 E2 的定义矛盾 | Done | **基本成立** | Prop 25(1) 改为"通往 E2 的尝试"；更低的 $c_A$ 的两个效应、Schelling 的显著性、Debs–Monteiro 都写进去了；§6.3 表与 §13 也相应修改。残余：失败的理由建立在可观测性上，与 §10.5"E2 最可核查"冲突；P2 被偷换成"连续且不可观测"；在大国之间，可信性才是首要问题（N10）。 |
| IR6 | 第 8 节的立场是合成物；(A) 依赖 (K) | Partly | **部分成立** | "最多得其二"已撤回，代之以 Corollary 3 与长期结果，这样更干净。残余：以破坏相威胁与 Plan A 都不持有 (A)，却仍被列为该立场的形式；(S) 定义为每个行动者的生存，使 Prop 29(5) 成为定义性的（N14）。 |
| IR7 | 螺旋模型与威慑模型冲突；困难情形无解 | Partly | **部分成立** | 困难情形已经点明，"没有赢的位置"与标题相合；降低 $r$ 的防御被归入 E2；声明不为强制背书。残余："两类型结果"是断言；"cover them"隐含强制；没有类型不确定（Kydd、Glaser）；Prop 24 与 Prop 22(4) 显示稿件断言的最优反应可能被支配（N5）。 |
| IR8 | Corollary 2：预测是廉价话语；分配问题 | Done | **部分成立，并引入一个新错误** | 已限于共享危害；与区域挂钩；"必须先于锁定"很好；分配问题列为未决。但"利益在共享危害上一致，所以信息可信"与 Prop 14 的偏差例子冲突（N4）。§0 第 104 行与 §14 第 1704 行仍写成无条件的"不需要事先的信任"。 |
| IR9 | L6 的免疫化 | Done | **基本成立** | 反驳条件已经诚实。残余：领导人层面的激励（Bueno de Mesquita et al. 2003）、为翻身而赌博、损失域中的风险偏好没有讨论；§13 对"Status is valued for its own sake"的回答（"defeats itself"）仍是在替行动者规定理性。 |
| IR10 | "癌性目标"：概念滑移、G-R3 回流、道德化 | Partly | **基本成立** | 一个定义、技术名称、结构来源、"不是任何行动者"已与"改变博弈"挂钩，G-R3 的回流已改正。残余：节标题"The logic to oppose"和"everyone should first oppose this logic"在 IR 读者听来仍带道德讨伐的腔调；对国家用"被选择"的说法仍需 Fazal（2007）式的限定（N9）。 |
| IR11 | 边界错误与结构现实主义；κ 被当作良性标量 | Partly | **未处理** | κ 仍是固定标量，没有写成依赖预期的形式；Waltz 对化约论的批评没有回应。§10.4 承认"structure produces it"，算是对第三意象的部分承认。 |
| IR12 | 预防性战争：经验基率；先发制人；A8 的核背景 | Partly | **未处理** | §3.5 与 v4.3 逐字相同：没有经验基率（Levy 1987；Reiter 1995），没有先发制人机制，"missiles at the data centres"仍无出处。新增的 Branch II 多期计算（B2）很好。另外，L6 改变了 Prop 8(4) 的含义（N1）。 |
| IR13 | 验证：透明—安全取舍；Nitze 准则；Kydd 对信任的定义 | Partly | **未处理** | Coe and Vaynman 2020、Nitze、Kydd 对信任的定义都没有进入正文。在 MAIM 与核查并存的世界里，透明—安全取舍尤其要紧（N10）。 |
| IR14 | 先例取自错误的领域；缺少军控记录 | Partly | **小部分成立** | §10.7 加了冷战一段。§9.5 的 Precedents 与 v4.3 只差一个交叉引用（臭氧、天花），§13 仍以"Precedents exist (9.5; 10.7)"回答"Rivals cannot cooperate"。军控先例表没有做（N8）。 |
| IR15 | 出口顺序与可验证性；E1 的范围 | Done | **成立** | 优先与可行已经分开；单边 E1 从战略决策回路开始；对手之间 E2/E3 最可核查，E1 作为规范来建设。E1b 的范围（劳动、金融、说服）仍然很宽，但已经排在后面。 |
| IR16 | "加入一无所得"只对风险中性的对称行动者成立 | Done | **成立** | §0、中文概要和 Prop 4(3) 都已限定，强者租金也已写出。 |
| IR17 | Theorem E 的假设已含 Theorem S 的极限 | Done | **基本成立** | 假设改为 (X)(U)(φ)、L1、L3–L6 加委托条件，证明从这些前提推出。残余：P3（不饱和）是隐含的假设（N8、N11）。 |
| IR18 | 措辞与不点名原则；若干过强的判断 | **未列出** | **大部分未处理** | "Struggle"仍在 §8.4 标题与 Corollary 3 的名称中；"reason says clearly"仍是无人称的断言；"no better guardian"仍在；§6.3 "Measures that change standing … Exit: None"仍在；Harsanyi and Selten 1988 仍未在正文引用。"dead end for humanity"已加限定，有改进（N16）。 |

**对附录 C 的总评。** 附录 C 把 IR1、IR3、IR4、IR8 标为 Done，偏宽了，应改为 Partly。IR11–IR13 实际上没有处理，应标 Open。IR18 应补列。

---

## 3. 新问题（按严重度排序）

### N1 个体判据下的困难情形推荐预防；Lemma E0 只靠切换到集体判据排除它 —— 致命（就"现实主义者的前提导向合作"而言）

**位置。**
- Theorem S（第 1350–1361 行）；
- §10.4 困难情形（第 1387–1391 行）；
- Lemma E0 与 Theorem E（第 1412–1421 行）；
- §10.6（第 1452 行）；
- Proposition 8(4)（第 522 行）；
- L6（第 1249 行）；
- 标题；
- 对照 v4.3 的 Theorem E（v4.3 第 1204 行）。

**稿件的主张。**
- "No branch of the race secures survival."
- 关于支配与消灭："Neither preserves every actor's survival."
- 困难情形下："there is no winning position."

**批评者会这样论证。**

**(a) 判据被换掉了。**
- Theorem S 是逐个行动者的判据：$\Phi_i$，按 L6 排序。
- Lemma E0 排除"消灭"的理由是：目标失去生存，攻击者承担冲突成本和报复风险。结论却写成"neither preserves every actor's survival"。对攻击者自己的 $\Phi_i$，Lemma E0 什么也没有证明。
- Theorem E 的对象（"every actor's survival bounded away from zero"）、§10.6 的"drives some actor's survival to zero"、结论的"Every other course drives some actor's survival to zero"，用的都是集体判据。
- v4.3 的 Theorem E 原本是个体判据（"some actor's survival"）。v4.4 为了回应 A3，换成了集体判据。
- 现实主义者的 L6 是个体判据。所以在最关键的一步，稿件用了一个现实主义者并不持有的判据。

**(b) 在困难情形下，Theorem S 让预防成为生存上的最优反应。**
- 对手必然竞赛时，克制得到 $\Phi^S$，加入得到 $\Phi^P$，两者都趋于零。任何生存概率有正下界的行动，都严格优于这两者。
- *示意计算（参数由本评审选定）。*
  - 取稿件 §10.3 对称例子中"留在外面会提高对手的决定性概率"一行：$\Phi^R=0.90$，$\Phi^P=0.134$，$\Phi^S=0.140$。
  - 设预防以概率 $e$ 升级为灾难（$\Phi=0$）；否则以概率 $\sigma$ 成功，场回到类似 R 的状态，失败则加入竞赛：
  $$\Phi^{\text{Prev}}=(1-e)\,[\sigma\Phi^R+(1-\sigma)\Phi^P].$$
  - 取 $\sigma=0.7$、$e=0.2$，得 $\Phi^{\text{Prev}}=0.54$。这接近 $\Phi^S$ 的四倍，也高于孤立竞赛的 $\Phi^T=0.224$。
  - 只有当 $e>0.79$ 时，预防才不如留在外面或加入；$\sigma=0.3$ 时，临界值是 $0.62$。

**(c) 沿着竞赛，慑止预防所需的升级概率趋于 1。** 由上式，慑止一个生存优先者发动预防所需的灾难性升级概率为
$$e^\ast=1-\frac{\max(\Phi^S,\Phi^P)}{\sigma\Phi^R+(1-\sigma)\Phi^P}.$$
当 $\Phi^S,\Phi^P\to0$ 而 $\sigma\Phi^R>0$ 时，$e^\ast\to1$。
- Proposition 8(4)"Large costs of conflict deter preventive attack"是流量收益模型的结论。
- 在 L6 下，比较的是生存而不是流量。一场仍有一半生存概率的战争，严格优于一个 $\Phi\to0$ 的克制。
- 所以在拥核的对手之间，稿件的生存转向恰恰取消了核威慑对预防的抑制。
- Ren 的原话"要么暴力的消灭，要么加入"和"导弹直接冲着数据中心去"，在现在的形式化里成了生存优先者的理性选项。

**(d) 与标题的关系。**
- 如果 $\Phi^{\text{Prev}}$ 有正下界，困难情形下对强者就存在一个"最不坏"的位置，即预防。这与"No Winning Position"在精神上相悖。
- 这也恰恰是 IASEAI 的读者最不应该从本稿推出的结论。

**证据与文献。**
- Trachtenberg 1988/89：1949–54 年领先方对预防性战争的严肃考虑。
- Burr and Richelson 2000/01：1963–64 年考虑打击另一大国的核计划，最终放弃。
- Debs and Monteiro 2014：不可观测的权力转移，以及误判之下的预防。
- Levy 1987、Copeland 2000：预防动机与衰落中的主导国。
- Kydd 1997、2005：对安全寻求者实施预防，会制造螺旋。

**修复，或最佳回应。**
1. **加一个引理："持续预防是一条竞赛分支"（Lemma P）。**
   - 对一个能力复利、进展不可观测的目标，预防不是一次性的：目标会重建，需要反复"割草"。
   - 若每次打击的升级概率和每期重建的概率都有正下界，预防者的每期危害就有正下界，$\Phi^{\text{Prev}}\to0$。这与 Lemma M 是同一结构。
   - 要及时发现不可观测的算法进展、并在机器速度上打击，预防者需要 AI 支持的情报与打击能力。这就是 H1，经 L3 回到 Prop 6 与 Lemma D。
   - 写出这个引理，"在困难情形下，包括预防者在内都没有生存位置"才成立，标题才一致。
2. **把 (c) 变成论据，而不是隐患。**
   - 沿着竞赛，落后者的预防在生存意义上越来越理性，这就把 $q_W$ 内生化了：$q_W\to1$。
   - 这是对竞赛者最有力的现实主义论证之一：**你的竞赛使对手对你的预防性打击变得理性。**
   - 同时必须写出另一面：预防者自己按 Lemma P 也活不下来。这就是悲剧的结构，也是"没有赢的位置"的完整含义。
3. **加入对类型的不确定。**
   - 预防针对的是"被认为必然竞赛"的对手。若对手实际上是生存优先型，预防就摧毁了一个门槛趋于零的猎鹿博弈，并制造出稿件最怕的那种对手（Kydd 的螺旋）。
   - 给出先验 $\mu$（对手为困难型）下预防的期望生存，并说明 Debs–Monteiro 式的误判如何抬高错误预防的概率。
4. **把集体判据明示为规范前提。**
   - §13 的规范前提里已经有"those affected should keep a capacity to contest"。
   - 在 Theorem E 之前写明：E 的对象是"每个行动者的生存"，这是规范性的。
   - 对个体生存最大化者，本稿给出的回答是 Lemma P，不是 Lemma E0。
5. **说清困难情形下的排序。**
   - E1>E3>E2 是 Ren 的规范优先（稿件已承认），不是在困难情形下按生存推出的排序。
   - 若按每期危害率比较各个输的位置，预防可能排第一。本稿必须说明它为什么仍然不选：依据是第 1、3、4 点，而不是定义。

### N2 前提被搬了家，而不是被消除：(φ)、(X) 的一步、L3 与 Lemma D —— 严重

**位置。**
- §0 Epistemic status（第 146 行）；
- §10.2 的 (X)(U)(φ)（第 1269–1279 行）；
- "Why the conditions hold today"（第 1313–1321 行）；
- §12 生存条件表（第 1551–1563 行）；
- §13 Limitations（第 1668 行）。

**稿件的主张。**
- "The conditions that carry it most are the racers' own premises, that the advantage is decisive and fast, together with a fact about every present institution: understanding does not grow as fast as what it must understand."
- 关于 (X)："This is the race premise P2, and it is the racers' own premise."

**批评者会这样论证。**
1. **(X) 比 P2 强。**
   - P2 说：能力增长快，领先可以在短窗口内打开。
   - (X) 说：correction 必须覆盖的危害相关行为，其多样性至少指数增长。
   - 从"能力"到"需要覆盖的危害多样性"这一步是本稿的，不是竞赛者的。
2. **P2 讲的是相对速度，(X) 和 (U) 比较的是绝对速度与理解。** 两者可以分开（见 N11）。
3. **(φ) 是全部论证里争议最大的前提。**
   - 它说：未被覆盖的行为中，有一部分以每期至少 $h\varphi$ 的概率造成不可逆伤害，而且 $h$ 不随时间下降。
   - Lemma M 的"the time of perils does not end"完全来自 $h$ 的正下界。
   - 这正是竞赛者不接受的 AI 风险前提，§0 却没有把它列为承载结论的条件。
4. **同一结构也"证明"了核威慑在长期必然失败**，因为每期核战争概率也有正下界。
   - Waltz 一派会用核学习（Nye 1987）回答：危害可以随经验下降，从而可和。
   - 若在 AI 情形下 $h$ 能随学习下降（例如随可解释性的进展），Lemma M 就弱化为"取决于学习速度与复利速度之比"。
5. **L3（$s$ 无界增长）仍是假设**，却承载 Theorem E(2) 的长期必要性（N12）。
6. **Lemma D 的生存定义承载 $q_{\mathrm I}\to1$**（N7）。

**后果。** 设想一个现实主义者：接受 P1、P2 和 Proposition 27，拒绝 (φ) 与 Lemma D 的生存定义。用稿件自己的 Theorem S 机器，他得到的是：$\Phi^T,\Phi^P$ 保持为正，而 $\Phi^S\to0$，因为 Proposition 27 让落后致命。这就是竞赛的理由，而且比在 v4.3 里更强。

**修复。**
- **改写 §0。** 建议写成："The conditions that carry it most are three: the racers' own premise that the advantage is decisive and fast; that understanding does not grow as fast as capability; and that some failure modes beyond understanding are irreversible at a rate that does not decline (φ). The first is theirs; the second holds of every institution; the third is the AI-risk premise, and it is where the evidence must be shown."
- **在"Why the conditions hold today"中为 (φ) 补一条证据。**
  - 已观察到的评估意识、奖励黑客、在评估中隐藏能力（§5 已引 van der Weij et al. 2025、Needham et al. 2025）。
  - 再说明为什么在竞赛中 $h$ 不随学习下降。Proposition 28（安全进步被换成速度）正是"$h$ 不下降"的机制，应当在这里引用。
- **写出 Lemma M 的学习版本。**
  - 若 $h(t)$ 下降，且 $\int h(t)(1-U/X)\,dt<\infty$，生存为正。
  - 在 (K)(A) 下，竞赛把 $h$ 的下降换成速度（Prop 28），所以 $h$ 不下降。
  - 这是一个可检验、而且对现实主义者有约束力的说法，也回答了核学习这个类比。

### N3 "竞赛本身扩大这个区域"未证明，且被稿件自己的数值反驳；$c_{\text{conv}}$ 是定义，不是推导 —— 严重

**位置。**
- §2.3 "Relative gains"（第 398 行）；
- §10.3 "Relative gains, revisited"（第 1373–1375 行）；
- Proposition 24（第 1444–1448 行）；
- `checks_v44.log` 的 SV 一节。

**稿件的主张。**
- "The realist's first premise … argues against the race in the region of Proposition 23, and the race itself enlarges that region."
- "$\lambda_{\text{eff}}=\lambda c_{\text{conv}}$ … follows Powell (1991) … Theorem S says $c_{\text{conv}}\to0$."

**批评者会这样论证。**

**(a) 区域是否扩大，取决于两组速度的赛跑。**
- 竞赛抬高 $q_{\mathrm I}$ 和 $q^P_{\mathrm{II}}/q^S_{\mathrm{II}}$，使区域 $\Phi^S\ge\Phi^P$ 扩大。
- 竞赛也抬高 $p^S_{\text{dec}}$，而 Proposition 27 正好推动它，这使区域缩小。
- 稿件自己的反例路径（Prop 24：$q_{\mathrm I}=p_{\text{dec}}=1-\varepsilon$，$p^S_{\text{dec}}=1-\varepsilon^2$）给出：$\varepsilon=0.1$ 时 $\Phi^S/\Phi^P=0.18$，$\varepsilon=0.01$ 时 $0.02$（`checks_v44.log`）。
- 也就是说，随着竞赛逼近极限，留在外面相对于加入越来越差。在 L6 的比值形式下，面对一个确定的竞赛者，加入的理由沿这条路径随竞赛推进而**增强**。

**(b) $c_{\text{conv}}$ 没有模型。**
- Powell（1991）的相对收益关切是从模型里推出来的：武力是否可用，决定相对收益是否重要。稿件只写了一个乘法定义。
- 用稿件自己的式子就能推出来。在 $\Phi_i=Q[w_i+(1-w_i)(1-p)]$（Prop 6(6)）中，$\partial\Phi_i/\partial w_i=Q\,p$。这就是地位转化为生存的边际率：
$$c_{\text{conv}}=Q\,p,\qquad Q=(1-q_{\mathrm I})(1-q_{\mathrm{II}})(1-q_W).$$
- 由此立刻看到两件稿件没有说的事：
  - $c_{\text{conv}}\to0$ **只**经由 $Q\to0$，也就是只经由 (φ) 和 Lemma D；
  - Proposition 27 推动 $p\to1$，**提高** $c_{\text{conv}}$。所以 Prop 27 与 Lemma M 在相对收益问题上方向相反，而稿件把两者都当作支持自己的论据。

**(c) 极限下的 $c_{\text{conv}}\to0$ 并不等于"相对收益不重要"，而是"什么都不重要"**，因为所有竞赛分支都会死。
- 现实主义者会说，有意义的问题始终在极限之前。
- 在极限之前，Prop 23 的领先者例子给出 $\Phi^S=0.035$ 对 $\Phi^P=0.367$（共享危害 0.3），地位向生存的转化很强。

**修复。**
- 删去"the race itself enlarges that region"，或者改写成有条件的说法。给出区域扩大的充分条件，大意是：自主丧失与共享危害上升得比对手的决定性概率更快，例如
$$\frac{d}{dt}\ln\frac{1-q^S_{\mathrm{II}}}{(1-q_{\mathrm I})(1-q^P_{\mathrm{II}})}>\frac{d}{dt}\ln\frac{1-p_{\text{dec}}(n-1)/n}{1-p^S_{\text{dec}}}.$$
  并把 Prop 24 的路径列为不满足这一条件的例子。
- 用 $c_{\text{conv}}=Qp$ 替换定义式，写成 Powell 式的比较静态：$\partial c_{\text{conv}}/\partial q<0$，$\partial c_{\text{conv}}/\partial p>0$。
  - IR 读者会认出这正是 Powell 的结构。
  - 主张也随之变得诚实："相对收益关切随工具可控性的下降而下降，随落后致命性的上升而上升。本稿认为前者在竞赛中占优，理由是 (φ)。"

### N4 Corollary 2：共享危害的信息并不因为"利益一致"而可信 —— 严重

**位置。**
- Corollary 2（第 1363–1367 行）；
- Proposition 14 及其设定（第 828–837 行）；
- §0 第 104 行；
- §14 第 1704 行。

**稿件的主张。** "Every actor's interest is aligned on it, so by Proposition 14, with no bias on what all share, messages about it can be credible."

**批评者会这样论证。**

**(a) 判断可信度的标准用错了。**
- 在 Crawford–Sobel 模型里，决定可信度的不是双方在**状态**上有没有共同利益，而是给定状态时，双方偏好的**接收者行动**是否一致。
- 稿件自己在 §7.2 给出的偏差例子，恰恰是"the receiver restraining more than the state warrants"，偏差为 $b=\lambda\beta_s$。
- 关于共享危害的报告正属于这一类：只要 $\lambda>0$，发送者就希望对手高估共享危害，从而更多地克制。所以这类报告的偏差为正，在 $b\ge1/4$ 时完全不可信。
- 冷战中的"导弹差距"，就是在共同面临的危险上夸大或误判的例子。

**(b) 推导公开，参数却是私人的。**
- 稿件的第二个理由更好："The prediction is also a derivation from public premises (P1, P2 and (U)) that each actor can check for itself."
- 但公开的只是推导的形式。(φ) 中的 $h$ 和 $\varphi$，以及能力增长率 $g$，都来自各方对自己系统的私人评估。按 §7.2 的说法，这正是"an actor has most reason to withhold or shade"的信息。
- 况且如 N2 所说，承载推导的还有 (φ)，而 (φ) 不在稿件列出的"public premises"里。

**(c) 分配问题。** 分配问题（Fearon 1998；Krasner 1991）在 §13 被列为未决，这是诚实的。但讲过渡的那一节，仍然写得好像这个问题不存在。

**(d) 两处无条件的表述。**
- §0 第 104 行："the trust threshold vanishes"。
- §14 第 1704 行："cooperation needs no prior trust"。
- 两处都应加上限定："在区域 23(2) 内，或沿竞赛趋于零"。

**修复。**
- 删去"Every actor's interest is aligned on it, so by Proposition 14 … credible"。
- 改为：在竞争之下，关于共享危害的**言辞**仍是廉价话语。过渡依靠两样东西：
  - 每个行动者可以独立核验的推导与证据，例如独立评估者的结果、公开的事故数据；
  - 代价高昂的信号（Kydd 2005）。
- 指出本稿已经有一个天然的分离信号：在自己的战略决策回路中单边实行 E1（Prop 24），并让它可以核查。
  - 对困难型行动者，模仿这个信号代价很高，因为要放弃速度优势 $s$。
  - 对生存优先型行动者，代价很低，因为在区域内它本来就占优。
  - 这样，Corollary 2 就变成一个 Kydd 式的安抚结果，现实主义者可以接受。

### N5 困难情形与"两类型结果"：断言而非推导；覆盖要求隐含强制；缺少类型不确定 —— 严重

**位置。**
- §10.4（第 1381–1393 行）；
- Proposition 22(4)（第 1150 行）；
- Proposition 24（第 1444–1448 行）；
- §6.3 表中"Measures that change standing"一行（第 768 行）；
- §13 的"The other side will never cooperate"（第 1615–1620 行）。

**稿件的主张。**
- "Actors that hold an unbounded relative objective. The theory predicts they will not be persuaded. Everyone else's best response is to hold E1 and E2 in common, and to cover them."
- "It does not endorse coercion."

**批评者会这样论证。**

**(a) "Everyone else's best response"没有推导。**
- 按 Prop 24，面对一个竞赛者，单边 E1 可能比加入更差，这是稿件自己的反例。
- 非竞赛者之间"共同持有"E1 和 E2，并不改变竞赛者的 $p_{\text{dec}}$：所有非竞赛者都仍处在 S 分支。
- 按 Prop 22(4)，非竞赛者联合起来压住一个背叛者所需的努力，随赢的价值陡增，这就是"竞赛上移一层"。而强到足以压服背叛者的联合体，本身就是权力的集中（§4）。
- 所以在稿件自己的结果里，这个"最优反应"要么被支配，要么就是联合起来竞赛。

**(b) "and to cover them"隐含强制。**
- Definition 3(a) 的覆盖要求约束**每一个**份额能够增长的行动者。
- 对一个不愿加入的有能力行动者实施覆盖，只能靠强制：出口管制、制裁、拒止，或者打击。
- 可是 §6.3 的表把"改变对手地位的措施（投入管制、自力更生）"标为 Exit: None，§10.4 又说本稿不为强制背书。三处放在一起是矛盾的。
- 在困难情形下，稿件要么放弃覆盖，要么接受强制，要么说明第三条路是什么。

**(c) 二分不等于类型不确定。**
- 现实主义与讨价还价文献处理的是混合情形：不知道对手属于哪一类。见 Jervis 1976 的螺旋模型与威慑模型，Glaser 1992、2010，Kydd 1997、2005。
- 行动者真正面对的问题是：在先验 $\mu$ 下，克制、单边 E1、可核查的克制提议、拒止、预防，各自的期望生存是多少；以及什么样的信号能够分离类型。
- 稿件只说了"生存优先型适用 Theorem S，困难型不会被说服"。

**(d) Jervis 1978 的攻防框架是一个尚未回答的挑战。**
- 按稿件自己的 P1（决定性，即进攻占优）和两用性（攻防难以区分），AI 正好落在 Jervis 的"双重危险"象限，在那里合作最难。
- 本稿应有的回答是：开发中的共享危害是 Jervis 2×2 之外的第三个变量，相当于一件会危及持有者的武器，它的作用类似于给进攻一个负收益。
- 这一点很有原创性，但必须写出来，并以生物武器为先例（见 N8）。

**修复。**
- **把两类型写成先验 $\mu$ 下的贝叶斯博弈。** 一页即可。
  - $\mu$ 低于某个阈值时，生存优先型的最优策略是：提出可核查的 E1/E2，并单边实行 E1。
  - $\mu$ 较高时，比较拒止、联合 E2 与预防的期望生存，其中预防用 N1 的 Lemma P。
- **说清困难情形下覆盖靠什么。** 只有两条路：被覆盖方同意，或者强制。
  - 若本稿不为强制背书，就写明：此时 Definition 3(a) 无法满足，结果是"没有生存位置"。
  - 若有条件地接受拒止（例如对决定性类别所需的投入实施拒止），就把它从 Exit: None 改为"在困难情形下，可能是 E2 的强制形式，代价是提高 λ 和信任门槛"，并给出净效应为正的条件。
- **写出 Jervis 象限的论证**，见 (d)。

### N6 同一结构，三种判定：冷战（证据）、Plan A（伪解）、E1 共同持有（出口） —— 严重

**位置。**
- §10.7（第 1467–1475 行）；
- §8.5（第 1014–1050 行）；
- Theorem E(2)–(3)（第 1420–1421 行）；
- §10.5 的可行性段落（第 1438–1442 行）。

**稿件的主张。**
- 冷战："the rivals kept their contest by preventing decisiveness, which is E2"，被当作出口的证据。
- Plan A："E2 and E3 held under (K) … By Theorem E(3), E2 and E3 held under (K) only postpone"，判为伪解。
- Theorem E(2)：长期生存要求 E0，"or taking AI out of it for every actor (E1, held in common)"。

**批评者会这样论证。**

**(a) 冷战的军控正是"E2 held under (K)"。**
- 它保持对抗，依靠相互确保摧毁，并按对等（SALT 的"基本对等"）设限，也就是一种比例安排。
- Plan A 是同一结构在 AI 上的版本：比例储备、相互确保摧毁、联盟保持领先。
- 若比例安排因 Prop 15(3)"保留相对动机"而使 Plan A 成为伪解，那么 SALT 和 ABM 条约也是伪解。可 §10.7 把它们当作出口的证据。
- 除非把两者的区别说出来，否则 IR 读者会认为这是双重标准。区别只能来自四点不同，尤其是饱和与 $g_s>0$。可是 §10.7 和 §8.5 互不引用。

**(b) "E1 held in common under H0"同样是在保留的对抗之下持有一个出口。**
- 按稿件自己的 L3，背叛 E1（秘密把 AI 放进决策回路）的收益是速度优势 $s$，而 $s$ 随时间增长。这正是 Prop 22(4)"盖子随压力增长"和 Prop 15 的结构。
- 按 §10.5，E1 又是最难核查的出口，因为它涉及软件和内部流程。
- 所以用判定 Plan A 的同一个标准，E1 在 H0 下的共同持有也只能推迟。Theorem E(2) 的析取支"或者 E1 共同持有"并不比 Plan A 更持久，除非赢的价值下降。

**(c) 对 Plan A 的判定是否公平。** 这一判定是 Ren 的裁定。我评估的是正文的论证是否准确、公平。

做得好的地方：
- 描述现在准确，承认了 Plan A 反赢家通吃的设计，也承认了其作者对竞赛与破坏的判断；
- 指出 Plan A 以有计划的交接（handoff）为终点，这是最有力、也最公平的批评；
- 指出 research titration 是场内的纠错。

不公平或不准确的地方：
- **"disguise"带有恶意伪装的含义。** 按稿件自己的描述，Plan A 自称是延迟到约 2040 年的安排，并不自称是终局。更准确的说法是"a holding arrangement that cannot be the end state"。这正是 Ren 方向文件中"至少 insufficient"的最低要求，正文的论证完全支持这一点。
- **"It treats the symptom … with the race's own means"打击面过宽。** 对手之间任何可行的军控都要保持对等，否则弱势一方不会签字（Grieco）。若以此判为伪解，就判掉了所有对手之间的军控，包括 §10.7 赞许的那些。
- **本稿的 E0 没有对背叛的执行机制**，只有共享预测（Corollary 2，见 N4）与信任。现实主义者会说，Plan A 至少有执行机制。本稿应当正面回答：在区域 23(2) 内，执行是多余而无害的；在区域之外，Plan A 的执行是必要的，但不充分。

**修复。**
- **定一个统一标准。** "在 H0 下，任何安排（E1、E2、E3，或它们的核查版）的持久性都取决于赢的价值是否下降；不下降，按 Theorem E(3) 就只能推迟。"
- **按这个标准统一判定三者。**
  - 冷战的安排够用，是因为自然提供了饱和（技术压低了赢的价值），而且 $g_s$ 有界。
  - Plan A 不够，是因为 AI 没有饱和，且 $g_s>0$。
  - E1 同理，除非 Corollary 1(1) 起作用。
- **把 Plan A 重新表述为"必要的桥，不是终点"。** 它的核查与执行在过渡期有用；它的不足在于不降低赢的价值，并以交接为终点。
- 若保留"伪解"一词，就说明它在本稿中的确切含义：形式上是合作，持久性仍依赖竞赛的手段。并去掉"disguise"。

### N7 Lemma D：现实主义者认不出这种"生存"；而且它把选择规则的结论搬到了战略行动者身上 —— 中等（偏严重）

**位置。**
- §10.1（第 1245–1263 行）；
- 附录 A 的 Lemma D（第 1944 行）；
- §1.7 规则 1（第 299 行）。

**稿件的主张。** "Locked delegation in a contest therefore ends survival as an actor that decides its own course. This holds even when each delegated system is faithful to its operator."

**批评者会这样论证。**

**(a) 概念问题。**
- Lemma D 证明的是：锁定之后，没有哪个决策过程代表行动者在**共同项**（宿主、共享危害）上的利益。
- 对结构现实主义者，这不是生存的丧失。Waltz 的生存是单位的保全；Mearsheimer 的生存是领土完整，以及国内秩序相对于**外部**的自主。
- 一个由忠实的、追求相对地位的 AI 运作的国家，在现实主义意义上不仅活着，而且是一个更纯粹的现实主义国家。它本来就不太代表共同项：在 Prop 2 里，G 从相对项中消去。
- 所以，$q_{\mathrm I}$ 进入 Φ，对现实主义者仍然是定义上的扩展，上一轮 IR4 的核心没有解决。真正的生存通道只剩两条：$q_{\mathrm{II}}$（共享危害），以及机器之间的冲突。

**(b) 层次混用。**
- Lemma D 用 Lemma 0（相对选择规则下共同项被消去）来说明被保留的系统对共同项盲目。
- 但 Lemma 0 讲的是选择规则。L6 下的国家是战略行动者，它依据 Φ 挑选决策系统，而 Φ 含有共同因子 $Q$（Prop 6(6)），这个因子不会被消去。
- §1.7 规则 1 正好禁止这种移植："A result about selection does not transfer to strategic actors unless their objective is shown to be the selected one."
- 要让 Lemma D 成立，需要两步论证：
  - 在国家内部，决策系统的保留遵循相对规则。例如按对抗演习中的相对表现采购，或者机构之间的竞争。
  - 生存优先的国家为什么不在保留标准里加入共同项。可以用 Prop 28（安全进步被换成速度）来回答。

**(c) 一个被浪费的通道。**
- 在冷战文献里，最能让现实主义者在意委托的，不是"自主"，而是机器速度下的危机不稳定，包括：
  - 相互对突然袭击的恐惧（Schelling 1960，第 9 章）；
  - 无意升级（Posen 1991）；
  - "闪电战争"（flash war，Scharre 2018）。
- 这是 $q_{\mathrm{II}}$ 的一个具体机制：被委托的系统之间的互动没有人类否决。§10.7 第 3 点已经提到这一点，却没有用来支撑 Lemma D。

**(d) 领导人层面。**
- 对领导人而言，锁定的委托就是失去权力。选择者理论（Bueno de Mesquita et al. 2003）为领导人在意 $q_{\mathrm I}$ 提供了理由。
- 这是一个现实主义者能够接受、又支持 $q_{\mathrm I}$ 的论证，稿件没有用。

**修复。** 在面向 IR 的版本中：
1. 把现实主义意义上的生存限定为单位的保全；把 $q_{\mathrm I}$ 的作用写成 $q_{\mathrm{II}}$ 的放大器（被委托的系统对共同项盲目，机器速度的互动没有否决），而不是一种独立的死亡。
2. 用 Feaver 的 always/never 困境、Schelling 的 reciprocal fear、Posen 与 Scharre，为 Lemma D 提供经验依据。
3. 补上国家内部选择规则的论证；或者把 Lemma D 的适用范围限定为"由相互竞争的组织构成的行动者"。

### N8 核先例：方向正确，但太薄，有事实错误，实际说明的东西也与正文所说不同 —— 中等

**位置。**
- §10.7（第 1465–1475 行）；
- §13（第 1605 行）；
- §12（第 1562 行）；
- 参考文献（第 2252 行）。

**事实与引用问题。**
1. **"ran the fastest arms race in history"。** 这是没有依据的最高级，改为"the largest and longest"更稳妥。
2. **第 1 点"The danger of nuclear weapons lies in use"不完整。**
   - 冷战的险情大多来自部署姿态：警报级别、预警即发射、事故与虚假预警（Sagan 1993；Blair 1993；Schlosser 2013），以及常规作战引发的无意升级（Posen 1991）。
   - 威慑不仅没有压制这些危害，还制造了它们。
   - 更准确、也更有力的写法是："威慑压制蓄意使用；它不触及、并且部分制造了部署姿态带来的危害。AI 的危害属于后一类，而且在开发阶段就出现。"
3. **第 2 点"饱和"在核领域本身就有争议，而争议的一方正是现实主义者。**
   - Green（2020）、Long and Green（2015）、Lieber and Press（2020）、Kroenig（2018）认为，超级大国一直在追求损害限制与核优势；饱和论（Jervis 1989）对国家行为的预测落空了。
   - 稿件应当说明：即使在饱和成立的领域，对手们仍在追逐优势，以及这对 AI 意味着什么。
   - P3 在正文中写成"This should be stated as a premise of its own"，像是评审意见的残留。P3 既没有进入 §1.5 的前提，也没有进入 Theorem S/E 的假设，尽管 Prop 27 的 L4（支配延伸到能够触及的一切）需要它。
   - Mearsheimer 本人认为，全球霸权因"水的阻挡力"和核威慑而不可能。AI 能否打破这一点，正是 P3 要回答的问题，应当引用。
4. **第 3 点"a human veto averted at least one near-miss (Sagan 1993)"需要指明事件。**
   - 若指 1983 年的虚假预警，或 1962 年的潜艇事件，这些细节在 Sagan 1993 出版时大概还没有公开（需核对），应当引用后来的来源，例如 Hoffman 2009，以及关于 1962 年潜艇事件的档案研究（需核对）。
   - Hoffman 2009 也记录了苏联的半自动报复系统，这是"时间压缩把决策推向自动化"的直接例证。
5. **第 4 点"Warheads and launchers can be counted by national technical means"不准确。**
   - 发射器可以用国家技术手段计数，弹头不能。正因如此，SALT/START 才采用计数规则，后来又需要现场核查。
   - 更准确的类比是：算力像发射器，可以观测；算法和模型权重像弹头，不能观测。
   - 这个类比反而对稿件有利：它说明了为什么基于算力的 E2 可以核查，以及算法进展为什么会使算力阈值逐渐失效。
6. **"the ABM Treaty, the test bans. That is E2"。**
   - ABM 条约是好例子。
   - 部分禁止核试验条约禁止的是大气层、外层空间和水下试验，地下试验照常进行。它并不阻止决定性，动机主要是放射性沉降和防扩散。把它列为 E2 很牵强。
   - 更贴切的是把某个领域排除在军事竞争之外的条约，例如外空条约（禁止在轨部署大规模杀伤性武器）和海床条约。它们更接近 E1。
7. **引文错配。**
   - 参考文献把 Feaver 1992 写成"Command and control in emerging nuclear nations. *International Security*"。那篇文章发表于 1992/93 年冬季号，讨论的是新兴核国家。
   - 正文用它支持"核大国被推向预先授权"，所需要的应当是 Feaver 1992 年的专著 *Guarding the Guardians*（Cornell UP）。

**实际说明的东西与正文所说不同。**
- **冷战说明了什么。** 当自然提供饱和、危害集中在使用上时，对手在保持对抗的同时活了下来。这与本稿的分支分类一致，相当于 Branch III 的核版本，是有用的证据。
- **冷战没有说明什么。** 它没有说明"当对手相信某种能力具有决定意义时，能够靠协议放弃它"。记录恰恰相反：
  - ABM 条约禁止的，是一种被普遍认为昂贵、效果存疑的能力；
  - MIRV 和精确打击力量这类被认为有意义的能力，没有被禁止；
  - ABM 条约在 2002 年被退出。
- 这份记录支持的是 Corollary 1，即先降低赢的价值，协议才便宜，也就是 Barrett 所说的"便宜的协议才会成功"。所以"Either way, E2 is cheap or necessary"应当改为："E2 among rivals has historically been achieved when cheap; the task is to make it cheap by lowering the value of winning."
- **"survived"还有两层含义要交代。** 冷战不是以协议结束的，而是以一方内部瓦解结束的（N15）。冷战期间危害随学习下降（Nye 1987），这与 (φ) 中常数 $h$ 的设定相冲突（N2）。

**漏掉的先例**（按与本稿的对应关系排列）：
- **1946 年 Acheson–Lilienthal 报告与 Baruch 计划。**
  - 把危险活动置于国际所有，这是本稿 E0/E1"共同持有"最直接的先例。
  - 它失败在顺序上：领先方要求在管制到位之前保留垄断，落后方要求领先方先放弃。
  - 这正是 Corollary 2"过渡必须先于锁定"的历史版本（Bundy 1988）。
- **1945–49 年的核垄断。**
  - 这是最接近"决定性领先"的历史情形。领先方内部有人认真主张预防性战争（Trachtenberg 1988/89），但最终没有实行。
  - 原因包括：优势并非决定性的、常规力量的对比、规范与国内约束（Tannenwald 1999、2007）。这些正好可以用来检验 Prop 27"被选择的赢家"。
- **1972 年生物武器公约。**
  - 这是最接近 AI 的类比：危害出现在开发阶段，使用不可控，并且会危及持有者。
  - 一方以不可控、军事价值低为由单方面放弃（具体出处需核对：Tucker and Mahan 2009），另一方却在公约之下维持了大规模秘密计划（Leitenberg and Zilinskas 2012）。
  - 它同时支持两件事：Theorem S 的逻辑（危及持有者的武器可以被单方放弃），以及困难情形的存在（共享危害没有说服另一方，而公约没有核查）。
- **核不扩散条约与大国合谋（Coe and Vaynman 2015）；反扩散与对他国核计划的预防考虑（Burr and Richelson 2000/01；Gavin 2015）。**
  - 这就是"部分联盟对外执行 E2"，§13 把它列为未决。
  - 它也是困难情形的历史答案，而那个答案是强制。
- **Snyder 1965 的稳定—不稳定悖论。**
  - 决定性层面的稳定，可能加剧较低层面的竞争。
  - 对 AI 而言，这意味着 E2 可能把竞争推向网络行动和影响力行动，而这正是 E1b 想覆盖的领域。

**修复。**
- 把 §10.7 扩成一张表，列为：先例 | 否定了哪一条假设 | 是什么使它成立或失败 | 说明哪一个命题。
- 改正上面列出的事实错误。
- 把结论改为："The nuclear record shows rivals surviving when nature supplied saturation, and forgoing capabilities by agreement when those capabilities were judged cheap to forgo. AI lacks the first (P3), so safety must come from the second, which requires lowering the value of winning first."

### N9 Proposition 27"被选择的赢家"：一半是现实主义自己的论证，因而帮的是竞赛；另一半超出了命题的地位 —— 中等

**位置。**
- Proposition 27（第 1295–1311 行）；
- 附录 A（第 1952 行）；
- §10.4（第 1383 行）。

**评估。**

**有帮助的部分。** "A winner cannot credibly commit to limits on its use of decisive advantage"是纯粹的 Fearon/Powell，再加上 Mearsheimer 所说的对意图的不确定。现实主义者接受这一点。

**但它帮的是竞赛。**
- 这正是现实主义者害怕落后的理由：赢家不可信，所以落后就成了生存问题。
- 在 $c_{\text{conv}}=Qp$ 中（N3），Prop 27 推高 $p$，从而推高 $c_{\text{conv}}$。
- 所以 Prop 27 本身并不导向合作。导向合作的是"赢家自己也保不住控制"，即 Lemma M、Lemma D 和 §4.4。
- 稿件应当把两者分开：Prop 27 解释为什么落后是致命的，这与现实主义一致；Lemma M 解释为什么领先也是致命的，这是本稿的贡献。

**超出地位的部分。**
- **前两条依据讲的是载体之间的选择。** Prop 1 和 Prop 3(4) 讲的是载体，而 §1.2 写明"Between states, only the strategic forms of Sections 2–3 apply"。把它们用于国家，违反了 §1.7 规则 1。1945 年以后国家灭亡很少见（Fazal 2007），国家之间的"选择"很弱。
- **工具性趋同和奖励黑客讲的是优化器。** Omohundro 2008 与 Turner et al. 2021 的结果是关于优化器的；"the race is, at the scale of a society, an instrumental convergence and a reward hacking"是一个类比。至于引用"本语料库中的 meta-attractor 与 selection-on-cognition 理论"，那是对未发表工作的自引，程序委员会不会把它当作论据。
- **它不是命题，却被当作极限使用。** 附录 A 给出的"证明"是："The conclusion is a statement about the selection pressure the race applies, not a deduction about any particular winner." 这样它只能算论证或评注。可 Theorem S 却用它来得到作为极限的 L4（"By Proposition 27, the race selects for (L4)"），也就是把一种压力当成了极限。

**还需要回答历史反例。**
- Ikenberry（2001）论证，大战之后的胜者多次通过制度自我约束（strategic restraint），以降低他国的恐惧和自己的执行成本。
- 1945–49 年的核垄断者也没有把支配延伸到它能触及的一切（N8）。
- 稿件可以这样回答：那些优势并不是决定性的（P1/P3 不成立），而且约束依靠的是他国可以检验的制度，也就是 Definition 3 的内容。这个回答很好，但需要写出来。

**修复。**
- 把 Prop 27 改称 Remark 或 Argument。
- 把 L4 的依据收窄为承诺问题加对意图的不确定，并明说这是现实主义自己的论证；选择与工具性趋同作为支持性的机制，而不是推导。
- 回应 Ikenberry 和核垄断这两个反例。
- 删去对未发表语料的依赖，或者把它移到注释里。

### N10 对 MAIM 的批评建立在不可观测性上，与"E2 最可核查"相冲突 —— 中等

**位置。**
- Proposition 25(1)（第 952–958 行）；
- §6.3 表中"Deterrence by threatened sabotage"一行（第 765 行）；
- §10.5 的可行性段落（第 1440 行）；
- §13（第 1598–1603 行）。

**批评者会这样论证。**

**(a) 两处说法不能同时成立。**
- Prop 25(1) 说："Under P2, capability grows continuously and is dual-use, and algorithmic progress cannot be observed. So thresholds lack salience … detection is not timely"。
- §10.5 说："Among rivals, E2 and E3 are the most verifiable, since they concern chips, fabs, datacentres, compute and pace."
- 如果算力足够可观测，可以用来核查 E2，那它也足以为 MAIM 提供显著的阈值。MAIM 的作者正是以大型数据中心可以观测为前提的。
- 如果算法进展使算力阈值失效，那它同时削弱了 MAIM 和 E2 的核查。

**(b) P2 讲的是速度，不是连续性，也不是不可观测性。**
- 快速而离散的跃升，反而可能更显著。
- "不可观测"是另一个前提，应当单独命名（例如 P4），并分别说明它对 MAIM 和对 E2 核查的影响。

**(c) 在大国之间，MAIM 更像反扩散，而不像相互确保摧毁。**
- 反扩散的历史记录是：针对弱小无核国家的项目实施过打击；针对大国的项目只被考虑过，没有实施（Burr and Richelson 2000/01）。
- 按 Prop 8(4)，对拥核对手而言，$c_A$ 极高。所以在大国之间，MAIM 的首要问题是**可信性**（Schelling 的"留有余地的威胁"），其次才是可观测性。
- 但要注意 N1：在 L6 下，高昂的 $c_A$ 不再足以使威胁不可信。这是一个必须正面处理的张力。

**(d) 核查本身可能为破坏提供目标信息。** 这就是透明—安全取舍（Coe and Vaynman 2020），也是上一轮的 IR13，至今仍未处理。在 MAIM 与 Plan A 并存的世界里，它尤其相关。

**修复。** 把对 MAIM 的批评改建在三点上：
1. 在 (K) 之下，赢的价值始终很大，所以所需的及时检测和可信度都趋于极限（Theorem B）；
2. 在大国之间，威胁有可信性问题，而这一问题在 L6 下会反转（N1）；
3. 它把 AI 推进军事能力，从而强化 H1。

可观测性作为单独的前提处理，并且对 E2 的核查使用同一个前提。

### N11 P1 二难与 P2 二难都不穷尽 —— 中等

**位置。**
- §10.7 末段（第 1475 行）；
- §8.4 决策树的 Q1（第 1003 行）；
- §10.2 的 Corollary（The P2 dilemma）（第 1293 行）。

**批评者会这样论证。**

**(a) P1 二难漏掉了一支。**
- 稿件写道："If AI is not decisive, E2 costs nothing … If it is decisive, Theorem S applies."
- 漏掉的第三支是"决定性且可控"。这正是"领先换安全裕度"立场的前提，也是现实主义者会选的那一支。
- Theorem S 需要的不只是 P1，还需要 (X)(U)(φ)、L3、L5、L6 和委托条件。

**(b) "E2 costs nothing"不成立。**
- E2 按名称禁止 ASI 和递归自我改进。即使它们不具决定意义，禁止它们仍然放弃了其经济与军事价值。按 Gilpin（1981）和权力转移理论，增长率的差异本身就是权力转移的来源。
- 准确的说法应当是"在安全意义上没有代价"。
- 这里还有一处定义上的含糊：
  - 若"决定性类别"按定义就是"具有决定意义的能力"，那么在第一支里 E2 是空的；
  - 若按名称指 ASI 和 RSI，那么 E2 就有代价。

**(c) P2 二难混淆了相对速度与绝对速度。**
- 稿件写道："No race is both fast enough to be worth running and slow enough to be corrected."
- P2 讲的是相对速度（领先在短窗口内打开），Lemma M 比较的是绝对速度与理解。
- 一方按理解允许的速度增长，另一方增长得更慢，领先照样会打开。
- 这样的竞赛以 E3 的速度进行，属于 Branch II。稿件自己承认，在那里讨价还价与纠错是有效的；Theorem E(2) 又说，即使如此，委托终将占优（L3）。

**修复。**
- P1 二难改为三支，第三支交给 Prop 29 和"why the conditions hold today"的第 3 点。
- "E2 costs nothing"改为"costs nothing in security"。
- P2 二难区分相对速度与绝对速度，并说明在 E3 之下进行的竞赛属于 Branch II，其长期风险来自 L3（见 N12）。

### N12 Theorem E(2) 的长期必要性依赖 L3，而 L3 仍是假设，也没有反驳条件 —— 中等

**位置。**
- L3（第 308 行）；
- Theorem E(2)（第 1420 行）；
- 附录 A 的 Theorem E（第 1969、1976 行）；
- §12 生存条件表。

**批评者会这样论证。**

**(a) 长期必要性只有 L3 一个依据。**
- 稿件说："Survival over an unbounded horizon therefore requires ending the contest by agreement (E0), or taking AI out of it for every actor"。
- 这句话唯一的依据是：在 H0∧H1 下，$s$ 无界增长，迟早会越过 $s^\ast$。这正是 L3，即 $s=s_0e^{g_st}$。
- 稿件推导了 $q_{\mathrm I}$、$q_{\mathrm{II}}$ 和 L4，但没有推导 L3。
- §12 的生存条件表里也没有 L3 这一行。$q_{\mathrm I}$ 那一行的反驳条件是"维持 $\mathcal K\ge\mathcal K_{\min}$"，而不是"$s$ 会饱和"。

**(b) 现实主义者会提出 $s$ 的饱和。**
- 在战略层面，决策速度的优势受到生产、后勤、部署等物理过程的限制，超过某一点就不再转化为胜率。这是 P3 在决策速度上的版本。
- 若 $s$ 饱和于 $s_{\max}<s^\ast$，Prop 6 的委托就永远不会占优；在 H0 下，E2/E3 也就不只是推迟。

**(c) 一个技术细节。**
- 在 E3 之下，能力的增长不快于理解，是次指数的，所以 $s$ 不可能按 $g_s>0$ 的指数增长。
- 附录 A 中"Neither E2 nor E3 changes $g_s$ to zero"应改为："$s$ 仍然无界增长，只是更慢。"

**修复。**
- 把 L3 列入 §12，给出反驳条件：战略决策速度的优势会饱和。
- 为不饱和提供论证：在网络行动和机器速度的互动中，速度直接决定结果（Scharre 2018；Horowitz 2019，需核对）。
- 修正 E3 下 $s$ 的增长形式。

### N13 $\Phi^R$ 依赖可和的残余危害，人类制度难以满足；应当比较危害率 —— 中等

**位置。**
- §10.1（第 1247 行）；
- Theorem S(2)（第 1352 行）；
- §12 中 $h_R$ 一行（第 1563 行）。

**批评者会这样论证。**
- Theorem S(2) 要求合作安排下的残余危害可和，这样 $\Phi^R$ 才有正下界。
- 但对手之间的安排，每期都有不可忽略的瓦解风险：
  - 华盛顿海军条约体系在 1930 年代中期终结；
  - ABM 条约在 2002 年被退出；
  - 按稿件的转述，Plan A 自己估计到 2040 年衰退的概率约为一半。
- 若瓦解风险每期都有正下界，$\Phi^R\to0$，与竞赛分支无异。
- 现实主义者（Mearsheimer 1994/95）会说"没有永久的制度"，从而认为 Theorem S(2) 的条件在经验上从未满足。

**修复。** 改为比较渐近危害率。
- 竞赛分支每期危害的下界是 $h\varphi$（Lemma M）；合作安排的每期危害是 $h_{\text{res}}+h_{\text{break}}$。
- 只要 $h_{\text{res}}+h_{\text{break}}<h\varphi$，就有 $\Phi^X/\Phi^R\to0$。L6 的比值形式就足以得出结论，不再需要可和。
- 这样主张更弱，但更稳，而且直接把 Prop 15（安排的瓦解）接进了生存论证。

### N14 第 8 节的"立场"仍把不持有 (A) 的方案算在里面；(S) 的集体定义使 Prop 29(5) 成为定义性的 —— 中等

**位置。**
- §8 开头（第 882–903 行）；
- Proposition 29（第 909–924 行）；
- §8.5。

**批评者会这样论证。**

**(a) 形式 4 和形式 5 不持有 (A)。**
- (A) 的定义是"Capability, decisive capability included, is built at the pace the contest sets"。
- 形式 4（以破坏相威胁的威慑）和形式 5（Plan A）都明确反对以竞赛的速度建造决定性能力：前者要阻止决定性的冲刺，后者要推迟到 2040 年。
- 所以它们是 (K)+(S)，而不是 (K)+(A)+(S)。
- §8.5 的结论（E2/E3 held under (K)）其实已经这样归类了，引言却仍把它们列为同一立场的形式。上一轮 IR6 的这一部分仍然存在。

**(b) Prop 29(5) 在稿件的定义下是定义性的。**
- (S) 被定义为"every actor's survival bounded away from zero"。
- 持有这一立场的人所说的"安全"，是没有失控灾难，并且本方存活。
- Prop 29(5) 说："If the margin works and the leader prevails, the others are dominated … The safety bought is the winner's, not every actor's"。在稿件的定义下，这句话是定义性的；对领先者来说，它不构成反驳。
- 真正的论证在前四项。

**(c) Prop 29(1) 漏掉了反方向。**
- 第一点（领先者放慢时，追随者会加速）是对的。
- 但领先者看到自己的窗口正在关闭时，也有动机先发制人（Copeland 2000；Van Evera 1999 关于"窗口"的论述；Lebow 1984）。
- 这使"领先换裕度"多了一种失败方式，而且来自领先者自己。

**修复。**
- 把形式 4 和形式 5 移到"(K)+(S) without (A)"一组，交由 Corollary 3(3) 处理。
- 把 (S) 拆成两层："每个行动者的生存"（规范层面），以及"没有失控灾难且本方存活"（立场持有者所指的含义）。Prop 29 应针对后者论证。
- 补上领先者的窗口逻辑。

### N15 Lemma E0 的二分不穷尽 —— 小

**位置。** Lemma E0（第 1412–1416 行）。

**批评者会这样论证。**
- 经验上，对抗关系（rivalry）最常见的终结方式，既不是支配，也不是消灭，而是：
  - 政治冲击与政权更替；
  - 一方的内部瓦解；
  - 一方接受对方地位的和解。
- 相关文献见 Goertz and Diehl 1995；Colaresi, Rasler and Thompson 2007（均需核对）。
- 冷战本身就是以一方内部瓦解结束的；英美之间的霸权转移是以和解完成的。
- 在 L4 成立时，和解并不安全，因为赢家不可信，所以可以论证这些方式在 AI 情形下不可用。但这需要写出来，否则"Neither preserves every actor's survival"所依赖的穷尽性不成立。

**修复。** 加一句：其他终结方式（瓦解、和解）在 L4 下，要么等同于支配，要么依赖一方的承诺，因而回到 Prop 27 与 E0。

### N16 措辞与引文的残留 —— 小

- **"Struggle"。** 它仍出现在 §8.4 的标题"Struggle and safety"、Corollary 3 的名称，以及 §0 与 §14 的"keep the struggle"中。上一轮 IR18 指出，熟悉特定政治词汇的英文读者可能认为它别有所指；附录 C 没有列出 IR18。建议英文版改用 contest 或 rivalry。
- **"reason says clearly, in today's world, that the actors must cooperate"（第 146、1321 行）。** 这是 Ren 的方向文件明确要求表达的判断，我不建议删除。但在 IR 读者面前，应当写成作者的判断（"we judge that reason says clearly …"），并紧接着点出它所依赖的 (φ)。
- **"There is no better guardian to be found by winning"（第 613 行）与"dead end for humanity"（第 1463 行）。** 后者已经加了限定，有改进；前者仍带檄文的腔调。
- **§3.5 第 528 行的引语。** 加了引号的"missiles at the data centres"仍然没有出处（上一轮 IR12(e)）。它是 Ren 的话，应当注明，或者去掉引号。
- **§13 中关于 † 的一句。** "References marked † in this paragraph are carried from v3.1's verified bibliography unless they are new"意思不清，而且与参考文献一节对 † 的定义（新增、尚未核实）相冲突。
- **"security dilemma"一词。** 正文从未使用这个词，它只出现在文献小标题里。§2.3 与 §3 讲的就是一个带共享宿主的安全困境，应当点名，IR 读者会立刻认出。
- **Harsanyi and Selten 1988。** 仍在参考文献中，正文没有引用。
- **Glaser 1994。** 应为 1994/95，*International Security* 19(3)。

### 3.17 IR 相关引文核查

以下依本评审者的知识核对，没有查原书页码。标"需核对"的地方，本评审没有把握。

| 引文 | 稿件用途 | 判断 | 说明 |
|---|---|---|---|
| Waltz 1979 | 生存是一切目标的前提 | 准确 | 约 p. 91–92。Waltz 也写到国家"at a maximum, drive for universal domination"（约 p. 118），与 §10.4 的结构读法相容。 |
| Mearsheimer 2001 | 领土完整与国内秩序的自主 | 准确（第 2 章，约 p. 31） | 这里的自主是相对外部而言的，与 Lemma D 的"自主"不是一回事（N7）。第 4 章的全球霸权不可能论（"水的阻挡力"）与 P3 相关，应当引用。 |
| Grieco 1988 | 地位转化为安全 | 大体准确，有偏差 | 与上一轮相同：Grieco 的论证是一般性的无政府论证，以"转化"为条件的是 Powell 1991。 |
| Powell 1991 | "$\lambda_{\text{eff}}=\lambda c_{\text{conv}}$ follows Powell" | 引用准确，用法松散 | Powell 的相对收益关切是推导出来的，稿件只写了一个定义（N3）。 |
| Fearon 1995；Powell 2006 | 承诺问题 | 准确 | — |
| Debs and Monteiro 2014 | 误判触发预防 | 准确（*IO* 68(1)） | — |
| Schelling 1960、1966 | 显著性；边缘政策 | 准确 | 1960 年书第 9 章"reciprocal fear of surprise attack"应当用于 N7。 |
| Jervis 1978 | 安全困境、攻防理论 | 准确（*World Politics* 30(2)） | 其"双重危险"象限没有被处理（N5）。 |
| Jervis 1989 | 饱和 | 准确 | 饱和论有争议（Green 2020；Lieber and Press 2020）。 |
| Glaser 1994 | 安全困境与攻防理论 | 年份应为 1994/95，*IS* 19(3) | 文章内容是"合作作为自助"，更适合用来做防御性现实主义的定位（第 4 节）。 |
| Feaver 1992 | 预先授权的压力 | 参考条目可能错配 | 条目是 *IS* 上的文章（1992/93，讨论新兴核国家）；正文需要的是专著 *Guarding the Guardians*（1992）。 |
| Bracken 1983；Blair 1993 | 预先授权；预警即发射 | 准确 | — |
| Sagan 1993 | 人类否决避免险情；运气 | 书目准确；"human veto"一句需要指明事件 | 见 N8 第 4 点。 |
| Kydd 2005；Osgood 1962 | 代价高昂的信号；GRIT | 准确 | Kydd 的类型不确定框架应当用于困难情形（N5）。 |
| Hendrycks, Schmidt and Wang 2025 | MAIM | 引用准确 | 对其机制的刻画已经改善，残余问题见 N10。 |
| Selten 1975 | 颤抖手完美 | 准确 | 只在极限下适用：在 $\Phi^S<\Phi^P$ 严格成立时，(D,D) 是严格均衡。 |
| Jones 2016 | 有界效用下生存占优 | 准确（*JPE* 124(2)） | — |
| Omohundro 2008；Turner et al. 2021 | 工具性趋同 | 准确 | 用于国家和社会是类比（N9）。 |
| Ashby 1956；Marchant, Allenby and Herkert 2011；Homer-Dixon 2000 | (U) | 准确 | — |
| Aschenbrenner 2024；Kokotajlo et al. 2025 | 领先换安全裕度 | 大体准确 | Amodei 2024 的 "entente" 论更多是关于用优势塑造结局，是否主张"安全裕度"需核对。 |
| Stafford, Trager and Dafoe 2022 | 领先与安全投资；风险补偿 | 文献存在（工作论文）；对其结论的表述需核对 | — |
| Peltzman 1975 | 风险补偿 | 准确（*JPE* 83(4)） | — |
| Larsen et al. 2026（AI 2040） | Plan A | 本评审无法独立核实 | — |

**应补的 IR 文献**（未加标注的，本评审有较高把握；标"需核对"的，请核对卷期）：
- **预防与窗口**
  - Levy 1987, *World Politics* 40(1)
  - Trachtenberg 1988/89, "A 'Wasting Asset'", *IS* 13(3)
  - Burr and Richelson 2000/01, *IS* 25(3)
  - Copeland 2000, *The Origins of Major War*
  - Van Evera 1999, *Causes of War*
  - Lebow 1984, *IS* 9(1)
  - Gavin 2015, "Strategies of Inhibition", *IS* 40(1)
  - Reiter 1995, *IS* 20(2)
- **核革命之争**
  - Green 2020, *The Revolution That Failed*
  - Long and Green 2015, *JSS*（需核对）
  - Lieber and Press 2017, *IS* 41(4)；Lieber and Press 2020, *The Myth of the Nuclear Revolution*
  - Kroenig 2018
  - Snyder 1965（需核对）
  - Nye 1987, *IO* 41(3)
  - Posen 1991
  - Schlosser 2013
  - Hoffman 2009
  - Tannenwald 1999, *IO* 53(3)；Tannenwald 2007
- **国际控制与军控**
  - Acheson–Lilienthal Report 1946
  - Bundy 1988, *Danger and Survival*
  - Coe and Vaynman 2015, *JOP* 77(4)（需核对）
  - Coe and Vaynman 2020, *APSR* 114(2)
  - Leitenberg and Zilinskas 2012
  - Tucker and Mahan 2009（需核对）
  - 核国家关于在核使用决策中保持人类控制的公开表态：这是 E1 在指挥控制领域的最窄形式（具体文本需核对）
- **类型不确定与安抚**
  - Jervis 1976
  - Glaser 1992, *World Politics* 44(4)；Glaser 2010
  - Kydd 1997, *World Politics* 49(3)
  - Kydd 2000, *IO* 54(2)
- **赢家的克制与对抗关系的终结**
  - Ikenberry 2001, *After Victory*
  - Fazal 2007
  - Goertz and Diehl 1995（需核对）
  - Colaresi, Rasler and Thompson 2007
- **机器速度**
  - Scharre 2018
  - Horowitz 2019, *JSS* 42(6)（需核对）
- **其他**
  - Bueno de Mesquita et al. 2003
  - Gilpin 1981
  - Mearsheimer 1994/95, *IS* 19(3)
  - Fearon 1998, *IO* 52(2)
  - Krasner 1991, *World Politics* 43(3)

---

## 4. 最强的剩余反驳，以及稿件是否回答了它

### 4.1 批评者会这样说

> "把这篇稿件里关于国家的部分剥出来，它证明了三件事。
>
> 第一，如果 (φ) 成立，即不可逆失败模式的每期危害永不下降，并且失去对自己工具的自主算作死亡，那么竞赛的每一条分支在长期都会死。于是对相信这一点的生存优先型国家，相互克制是一个门槛趋于零的猎鹿博弈。这不是对现实主义的反驳，这就是防御性现实主义：当竞争的共同代价足够高、对手是安全寻求者时，合作就是自助（Glaser 1994/95；Jervis 1978）。你们的贡献在前提，即开发中的共享危害。可那个前提正是我们与你们的分歧所在，而你们把它说成'竞赛者自己的前提'。
>
> 第二，在我们真正担心的情形里，也就是不知道对手是不是安全寻求者，或者对手无论如何都会竞赛，你们自己的生存演算给出的是我们的答案。你们的 Proposition 27 说赢家不可信，所以落后是致命的。你们的 Proposition 24 的路径说，竞赛越逼近极限，留在外面相对于加入就越差。你们的 Theorem S 说留在外面的生存趋于零，所以任何生存概率有正下界的行动都更好，包括预防性打击；而在生存优先之下，连高昂的战争成本都慑止不了它。你们只是把判据从'我的生存'换成了'每个行动者的生存'，才把预防排除掉。
>
> 第三，核记录说明，对手在保持对抗的情况下活了下来，靠的是自然提供的饱和；他们只在某种能力被认为便宜、可以放弃时，才以协议放弃它。你们把 Plan A 叫作伪解，因为它在保留的对抗之下，用核查和相互确保摧毁维持 E2。可是按同样的标准，冷战军控和你们自己的'E1 共同持有'也都只能推迟。你们唯一持久的出口是结束对抗本身，也就是走出无政府状态。而你们自己的第 4 节证明，任何强到足以执行它的守护者，都会被最强的一方俘获。
>
> 所以，本稿是防御性现实主义，加一个 AI 风险前提，再加一个乌托邦纲领。在困难情形下，它没有给出任何不属于我们工具箱的东西。"

### 4.2 v4.4 是否回答了

只回答了一部分。

**对第一条。**
- v4.4 已经接受了"猎鹿博弈"的结构，也接受了"$\varpi=0$ 时生存优先给不出克制的理由"，这很诚实。
- 但 §0 仍然把承载结论的条件说成"竞赛者自己的前提，加上 (U)"，没有承认 (φ) 才是分歧所在（N2）。
- Lemma D 的生存定义也没有改成现实主义者认得出的形式（N7）。

**对第二条：没有回答。**
- Lemma E0 只处理了目标的生存，没有给出 $\Phi^{\text{Prev}}$。
- "两类型结果"是断言，不是推导。
- 稿件没有注意到 L6 反转了 Prop 8(4)：在生存优先之下，高昂的战争成本不再能慑止预防（N1、N5）。

**对第三条：部分回答。**
- §10.7 写出了四点不同，却没有用它们来区分冷战与 Plan A；E1 在 H0 下能否持久，也没有被检验（N6、N8）。
- 至于第 4 节的俘获结果与 E0 之间的张力，稿件用"全行和小于一"和"相互承认的多个机构"来回应。这是一个好的回答，但没有放在面向现实主义者的位置上。

### 4.3 应当怎样回答（五步）

1. **认领防御性现实主义，并点明新变量。**
   - 不再说"现实主义被它自己的前提驳倒"。
   - 改说："在 Jervis 和 Glaser 的框架里，加入一个他们没有的变量：开发过程中危及持有者的共享危害。它使'双重危险'象限中的进攻优势变得自我挫败。"
   - 以生物武器公约作为最贴近的先例。它同时说明了两件事：这一逻辑能让一方单方面放弃，以及困难情形确实存在。
2. **把 (φ) 作为铰链公开辩护。**
   - 给出 Lemma M 的学习版本，即 $h(t)$ 下降时生存为正的条件。
   - 用 Prop 28 论证：在 (K)(A) 下，$h$ 不会下降。
   - 在"why the conditions hold today"中列出 (φ) 的现有证据。
   - 承认：若 (φ) 不成立，竞赛对现实主义者就是理性的，本稿预测竞赛会继续。
3. **写出 Lemma P，并把困难情形写成类型不确定下的博弈。**
   - 持续预防本身就是一条竞赛分支：目标会重建，打击有升级风险，预防者还需要 AI 支持的情报与打击能力。所以 $\Phi^{\text{Prev}}\to0$。
   - 错误的预防会摧毁与生存优先型对手之间的猎鹿均衡（Kydd）。
   - 写出 $q_W$ 的内生化：竞赛使对手对竞赛者的预防变得理性。
   - 给出困难情形下各个输的位置按危害率的排序，并诚实说明本稿的出口次序是规范性的。
4. **统一标准，修正 Corollary 2。**
   - 在 H0 下，任何安排的持久性都取决于赢的价值是否下降。冷战时，自然压低了它；AI 没有这种条件。
   - 所以 Plan A、E1、E2、E3 都是桥；Corollary 1(1) 是唯一能同时放松所有约束的杠杆。
   - 关于共享危害的言辞是廉价话语。过渡依靠可以独立核验的推导与证据，以及代价高昂的信号。单边、可核查的 E1（在自己的战略决策回路中）正是这样一个分离信号。
5. **为这位读者分层呈现主张。**
   - 面向现实主义者的核心是："你可以保留对抗（H0），但不能让 AI 成为它的工具（¬H1，从战略决策回路开始），也不能建造决定性类别的能力（¬H2）。在 (φ) 之下，这两件事对你自己的生存是占优的；在困难情形下，任何人都没有生存位置，包括预防者。"
   - Definition 3 的完整纲领（独立的纠错者、宿主、覆盖劳动与金融的 E1b）作为第二层呈现。明确它属于制度主义的论证，并用第 4 节的俘获结果为它设计约束。

---

## 5. 对这位读者有效、应当保留的部分

1. **对 $\varpi=0$ 的诚实。** Prop 23(2) 的无需信任区域，加上 Theorem S(3) 的风险占优和极限下的颤抖手完美，这是对现实主义者唯一正确的论证策略：靠占优，而不是靠信任。它不受对手类型不确定的影响，应当保留。
2. **分支相关的危害。** "你的竞赛通过对手危及你自己"，是对"对手反正会竞赛"最好的回答。按 N1 的修复把 $q_W$ 内生化之后，它会更有力。
3. **Lemma M 与 Prop 26。** "超出理解的纠错要么缺席，要么就是委托"，再加上 Ashby 的必要多样性定律和 pacing problem 的文献，是本稿面向战略研究最新颖的论证之一。补上学习版本之后，它对现实主义者有约束力。
4. **Prop 28（风险补偿）。** 它与 Peltzman 和 Stafford–Trager–Dafoe 一致，现实主义者能够接受。它也正是 (φ) 中 $h$ 不下降的机制，应当在 §10.2 引用。
5. **Prop 29 的结构。** 它与"窗口"文献（Van Evera、Lebow、Copeland）一一对应，应当保留，并补上领先者一方的窗口逻辑。
6. **威慑被重读为通往 E2 的尝试。** 这是正确的归类，更低的 $c_A$ 的两个效应也写得很好。
7. **四点不同。** 方向正确。改正事实错误之后，尤其是委托和可观测性两点（算力像发射器、算法像弹头），会成为 IR 读者最常引用的段落之一。
8. **优先与可行的区分，以及从战略决策回路开始的单边 E1。** 这是通往现实主义者的桥。应当把它表述为代价高昂的信号（N4）。
9. **Branch II 的多期计算（B2）。** 把"慢"定义为每期的转移小于 $(1-\delta)(1+c_A-w_{t+1})$，这是对 Fearon/Powell 的严谨使用。
10. **L6 不再免疫化，边缘政策被归为胆小鬼博弈。** 应当保留，并补上领导人层面的激励。
11. **上一轮已肯定的部分，仍然成立。**
    - Prop 2 是加上共享宿主的 Grieco 模型。
    - 第 4 节是对现实主义的制度批评（Mearsheimer 1994/95；Krasner 1991）的形式化。
    - Prop 6 与 Lemma 1 和核指挥控制文献吻合。
    - Theorem B 与 Prop 13 对应 Nitze 准则和 Jervis 的收益杠杆。
12. **"unbounded relative objective"这个技术名称，以及对其结构来源的承认。** 这让"反对一种逻辑而不是反对行动者"在 IR 读者面前第一次可以辩护。剩下要做的，是去掉标题与个别句子中的讨伐腔调。
13. **不点名。** 对这位读者是正确的选择。历史先例可以按条约或制度的名称引用，不违背这一原则。

---

*本评审没有修改 THEORY.md 或任何既有文件，也没有提交。*
