# R-v4.4-argument：整体论证、标题与证明、忠实度与论文（第二轮）

*评审对象：`v4/THEORY.md`，"No Winning Position: the integrated theory (v4.4)"，2271 行，约 3.64 万词（v4.3 为 2.79 万词）。评审日期：2026-10-03。视角与上一轮相同：科学哲学、系统思维与资深编辑。*

*读过的材料：*
- *THEORY.md 全文；*
- *我上一轮的评审 `reviews/R-v4.3-argument.md`，以及 `reviews/SYNTHESIS-v4.3.md`；*
- *Ren 的方向记录全文，重点是他 10 月 3 日对五视角评审的回复；*
- *`checks_v44.log`，以及 `checks_v44.py` 中 LM、SV 两节的代码；*
- *`theories/meta-attractor/README.md` 与 `theories/alignment-selection-on-cognition/README.md` 的开篇；*
- *Ren 的写作纪律，以及 "why and meaning" 的记录。*

*我手算复核了以下内容，均无误：Prop 23 的五组数字（含"领先者"两组）、Prop 23(3) 的不等式、Prop 24 的反例路径、Prop 28 的实现危险率（$0.0395=1-0.99\cdot0.985^2$）。脚本没有重跑。本评审只新建这一个文件，没有改动任何已有文件。*

---

## 1. 总体判断

**这一版做对了最重要的一件事。** 五位评审一致指出的循环已经消失：Theorem S 和 Theorem E 不再假设它们要证明的极限。现在的结构是：
- **三个前提：**
  - (X) 竞赛中能力复利；
  - (U) 人能理解、能争议的纠错能力，增长慢于任何指数；
  - (φ) 超出纠错范围的行为中，有不可逆的模式。
- **一个引理：** Lemma M。未覆盖的比例趋于一，危险率不可求和。
- **一个二难：** Prop 26。超出理解的纠错要么缺席，要么就是委托。
- **一个机制：** Lemma D。被委托的系统不承载行动者的共同利益。
- **一个选择论证：** Prop 27。赢家是竞赛选出来的。

这是正确的论证形状。一个结果性的假设（$q\to1$）被换成了三个可以分别检验、分别反驳的前提：
- (X) 是竞赛者自己的前提 P2；
- (U) 是每个现有制度都承认的事实；
- (φ) 是前沿安全框架自己写下的失控阈值。

立场方要拒绝结论，就必须拒绝其中一个前提，并为此承担举证责任。Ren 说"这几个 →1 本身可以被继续证明，或者至少有理性判断的答案"，这就是它的恰当形式。

**但"derived, not assumed"只对一部分为真。**
- **$q_{\mathrm{II}}\to1$：** 确实由 (X)(U)(φ) 推出。推导只有两行，内容都在前提里。这可以接受，但正文应当说"归约为三个前提"，而不是不加条件地说"军备竞赛本身制造了它"。
- **$q_{\mathrm I}\to1$：** 有两条路。
  - Prop 26 的第二支加上 Lemma D，是推导。
  - Prop 6 那条路仍然依赖 DC（加法度量下的条件），而且与 L6、Lemma D 一起构成一个内部矛盾（N2）。
- **$p_{\text{dec}}$ 与 (L4)：** 没有被推出。
  - Prop 27 给出的是选择压力。附录 A 自己写着 "not a deduction about any particular winner"。
  - Theorem E 的假设表 "(L3)–(L6)" 仍然包含 L4。
  - §10.7 新引入的 P3（优势不饱和）没有进入任何定理。
  - 而 §1.8 与附录 C 说 L4 "no longer assumed but derived"。这是一处新的"标题大于证明"（N3）。

**最大的缺口换了位置（N1）。** 上一轮的缺口是"孤立竞赛者只靠 $q_{\mathrm{II}}$"。v4.4 的补法是：Lemma M 对孤立竞赛者自己的复利能力也成立。但 Lemma M 是渐近的：$H\to\infty$，沿着*持续*的竞赛。
- 立场方最强的版本恰好是有限时间的："冲刺到决定性优势，然后放慢。"
- 在 CSF 模型中，$r$ 越大，赢所需的能力差距越小。所以这次冲刺不必走到理解之外很远。对一个赢后停下的赢家，Lemma M 给不出 $\Phi^T\to0$。
- Prop 29(5) 自己也承认这一点（"The safety bought is the winner's, not every actor's"），这与 Theorem S(1) 的"包括最强者和孤立竞赛者"直接冲突。

修复不难，而且会让论证更忠实于 Ren：把赢家分成两类。
- 对没有"够了"的赢家，Lemma M 恰好说明：癌式逻辑在毁掉宿主的同时也毁掉自己。
- 对会停下的赢家，如实写成困难情形，给出三种压力和一个均衡论证。

**一个内部矛盾，修复后反而得到更强的主结论（N2）。** 矛盾是这样产生的：
- 按 §10.1，生存包含自主；按 Lemma D，锁定的委托结束作为行动者的生存。
- 所以，一个生存优先、又知道 Lemma D 的行动者，在没有别人委托时永远不会先委托：委托即使赢了，赢的也是被委托的过程。
- 现稿 Prop 6(6) 的生存形式没有计入锁定的代价；Theorem S 和 Theorem E 又用加法度量下的 DC 推出"被迫委托"。于是它们与 L6 冲突。

正确的推导是"两个零"。只要有任何一个行动者委托（相对目标者在任何 $s>0$ 都会委托，见 Prop 6(4)；这与 Prop 4(4) 的"竞赛由最激进者开启"是同一个逻辑），其余每个行动者就只剩两条路：
- 委托，被 Lemma D 锁定；
- 不委托，$w\to0$，在 L4 与 P3 下被支配。

两条路都趋于零。这正是 Ren 截图里"要么暴力的消灭，要么加入"和"第一种基本完蛋"在生存度量下的形式。由此可以得到三点：
- E1 在知情的生存优先者之间是自我执行的；
- 只要有一个行动者不在其中，所有人都被推入"两个零"；
- 所以 E1 必须覆盖所有有能力的行动者。

这是"世界必须合作"的一个不依赖 DC 的定理形式，也给了 Ren 的"E1 第一优先"一个模型内的理由。

**是不是一个论证？比 v4.3 更是。** v3 的选择层现在有三条路进入主梁：
- 经由 Prop 26（用到 Props 10–11）；
- 经由 Prop 27（用到 Props 1、3(4)、9）；
- 经由 Lemma D（用到 Lemma 0、Remark 3）。

这正是上一轮 A10 要求的。剩下的问题是次序：§8（立场）大量引用只在 §10 才出现的 Lemma M、Props 26–27 和 Theorem E。读者在第 8 节读到的是一串前向引用（N9）。

**忠实度：大体忠实，有三处偏差。**
- "E3 始终必要"被写成 "Ren's priority"。Ren 给的次序是：E1；其次，E2 或 E3（N8）。
- "社会和意识条件"仍译作 "social and cognitive conditions"，丢掉了"问题在心"这一维（N8）。
- "agent 的 cognitive model 是被筛选的"只写了一句。理论自己的 Prop 3(4) 第二条（偏好可观测且 $n\ge3$ 时，偏向 $\theta<0$）正好适用于 AI 竞赛，却没有用上（N3）。

**冷读：比 v4.3 更难被一句话打掉，但新增了三个攻击面。**
- "渐近的同义反复"：Lemma M 加上"E3 下危险为零"的设定，结论几乎是构造出来的（N4、N6）。
- "赢了就停"（N1）。
- 博弈论读者会发现的内部矛盾（N2）。

另外，噪音明显增加了：
- "repair" 出现 129 次，v4.3 为 71 次；
- 附录 C 之前，版本号出现 97 次，v4.3 为 53 次；
- 正文里出现 "Ren's reading"、"Ren's reply"、"Ren's image"、"Ren's priority"（N10）。

**长度。** 3.64 万词，比 v4.3 多 30%。对一份理论文件，这不是问题；Ren 明确说过不要因篇幅约束理论。问题在于重复：
- 对"先赢后治理 / 良性赢家"的回答出现在六处；
- 对"用 AI 让 AI 安全"的回答出现在五处；
- 对威慑的回答出现在三处。

这既不利于压缩，也不利于冷读。建议每个回答只有一个家，其他地方交叉引用；另出一份干净的阅读稿（N15）。

**论文。** 截稿是 10 月 5 日 AOE。建议以 v3.1 已匿名、文献已核实的 LaTeX 为骨架，按主梁重写。最小计划见第 7 节。截稿前必须修的是：
- N1、N2、N3；
- Corollary 2 的第一条理由（N7）。

N2 若来不及，就在论文中明写 DC，并用脚注说明它与 L6 的关系。

---

## 2. 上轮条目核验表（A1–A21）

判定：✓ 修复成立；◐ 部分成立，有残余；✗ 未修，或修复不成立。

| 条目 | 附录 C 标注 | 核验 | 说明与残余 |
|---|---|---|---|
| A1 陈述循环；§0 的 "only" | Done | ✓（有残余） | Theorem S 和 E 不再继承彼此的条件，陈述与证明一致。§0 认识论段改为 "carry it most"，不再说 "only"。残余：§0 只列"竞赛者的前提加 (U)"，漏了 (φ)、L4/P3、DC 和 L5，还把 (U) 称为 "a fact"；Theorem S 的假设表仍然有 DC（N2） |
| A2 孤立竞赛者 | Done（"covered by Lemma M"） | ◐ | 只对持续复利的竞赛者成立。有限冲刺后停下的赢家没有覆盖；Prop 29(5) 自认赢家可以买到自己的安全；E2 的"自我执行"依赖同一个缺口。X₂ 没有以前提的形式出现，"自知之明"的理由被一个战略理由替代了（N1） |
| A3 支配与消灭；量词 | Done | ✓ | Lemma E0 写出了两种非协议的结束方式；Theorem E 用 "every actor's survival"。残余：Lemma E0 只点名了"两只钟"（到达决定性优势的时间，对比不可回头点），没有比较；Theorem E(2) 的 "Survival over an unbounded horizon" 漏了 "every actor's" |
| A4 长期必要性 | Done | ✓（有残余） | Theorem E(2) 与 Corollary 3 已改写，与上轮建议一致。残余：E(2) 经由 DC 推出，与 L6、Lemma D 冲突（N2）。Corollary 3(3) 的 "holds safety only until (K) is given up" 有歧义；这个措辞来自我上一轮的建议，应改为"只在有限时间内使生存为正；只有在这段时间内放弃 (K)，它才有用" |
| A5 完美回应 | Done | ✓ | 已到位：树、Lemma C 的内容（Prop 26 后的段落）、良性赢家（Prop 25(5)、Prop 27）、(K) 与 (S) 的定义。残余：对"竞赛之外、超出理解的 AI 纠错"缺一个递归论证（N5）；树缺"赢了会停吗"这一问（N1） |
| A6 "今天的世界" | Done | ◐ | §10.2 "Why the conditions hold today" 的六点写得好，尤其第 3 点（可控性二难）与第 4 点（可检验）。残余：§12 仍写 "The evidence that the race premise is held … will be documented in revision"；第 1 点 "Under P2, (X) holds by their own account" 说过了（N4） |
| A7 D 的生存形式 | Done | ✓（有残余） | Prop 6(6) 的 $\Phi_i=Q[w_i+(1-w_i)(1-p)]$ 是对的，单期的限定已写明，两个方向的反例都在日志里。残余：没有计入 Lemma D 的锁定代价（N2） |
| A8 cancerous 的定义；免疫化 | Done | ✓ | 一个定义（unbounded relative）、两种来源、两类型结果；免疫化已撤回；"selected preference" 已删除。残余：Prop 27 引入"认知被筛选"，重新打开了偏好演化的问题，应借 Prop 3(4) 的第二条来处理（N3） |
| A9 Lemma D；$q_{\mathrm I}$ 与共享危险 | Done | ◐ | Lemma D 已加入，$q_{\mathrm I}$ 与 $q_{\mathrm{II}}$ 已分开。残余：证明从 Lemma 0（共同项"不被选择"）直接推出"不被代表"，这一步太快，应当用 Prop 1（改变行动时被选择淘汰）；从"不代表共同利益"到"作为行动者的生存结束"，仍有一步是定义（N2） |
| A10 L6 对企业 | Done | ✓ | §10.1 末段写明：L6 是关于国家与联盟的前提；企业经由选择与规则制定者被约束 |
| A11 E1 的拆分与范围 | Done | ✓ | E1a/E1b 完整表达了 Ren 的两半；范围与 9 月 26 日的裁定和 §9.5 一致；H0 改称 "a struggle" |
| A12 次序与可行性 | Done | ◐ | 次序已写成规范上的优先；可行性一段写得好。残余：E2 的 "self-enforcing by Lemma M" 依赖 N1 的缺口；"E3 always" 被归给了 Ren（N8） |
| A13 E3 的纠错须人可争议 | Done | ✓ | 已以 $\mathcal K\ge\mathcal K_{\min}$ 与 contestability 为条件。残余：E3 的不等式写成了 $a\,\tau_{\text{eff}}$，而 $\tau_{\text{eff}}$ 是有效责任的符号，应为 $\tau_c$（N14） |
| A14 AI 2040 的归类 | Done | ✓（有残余） | 改为"(K) 之下的 E2/E3"，并如实承认 Plan A 的目标与要素。残余："Plan A 保留 H1"是断言；若干事实细节仍需对照原文核实；缺一个对任何方案都适用的"伪解检验"（N12） |
| A15 信任一节的标题与口号 | Done | ✓ | §7 的标题、可证明的那句话、两处 "exact form" 的合并都已完成。残余：同一句话在 §7.1 与 §8.2 逐字出现两次 |
| A16 "定理"的通胀 | Partly | ◐ | Theorem C 已改为 Proposition C；Prop 25 的析取已删除。新的通胀出现在 Prop 27（选择压力加外部文献加类比）、Prop 28（一个数值例，被称为 "the strongest answer"）、Prop 29（已有结果的组合）（N11） |
| A17 K7 | Done | ◐ | 正文已如实写出：最强者需要 L6，或者生存比大于租金比。但 "Lemma M supplies the ratio" 继承了 N1 |
| A18 地平线与时间 | Done | ✓ | 已定义 $\Phi_i(H)$；Corollary 2 写明"过渡必须在锁定之前"，$h_R$ 随达成时间上升（定性） |
| A19 冷战与文献 | Partly | ✓ | §10.7 的四点差异与"阻止决定性就是 E2"，是本版最强的新段落之一；文献已恢复。残余：† 文献未核实；Stafford、Trager 和 Dafoe（2022）在 §8.1 与 §13 被描述为两种不同的结论，需对照原文 |
| A20 末句 | Done | ✓ | "not who comes first, but what every actor needs in order to go on"，好 |
| A21 杂项 | Part | ◐ | 已改：Tier 表；$n=2$；E3 的界（但符号错了）；Def 3(d)；Remark 6；§0 的 "sacrifice" 一句。未改：Prop 3(3) 仍是同义反复；§2.3 "In plain words" 仍先结论后条件；repair 注释不减反增（71 → 129） |
| 上轮表 #8、#9 | — | ✗ | §3 标题仍是 "why racing cannot be won"；Theorem A 的名称仍是 "removes the case for racing"，没有加 "material" |
| 上轮表 #1 | — | ◐ | 标题在 §10.4 被定义为"若有行动者明知而竞赛，则没有赢的位置"，但 §0 没有定义。它的含义也从"竞赛赢不了"变成了困难情形（见第 3 节表 #1） |

**小结。** 21 项中 14 项成立，其中几项有残余；7 项部分成立。上轮表中有两个小项未改：§3 的标题和 Theorem A 的名称。部分成立的几项（A2、A9、A12、A17）都指向同一处：有限时间，以及委托在生存度量下的代价。这就是 N1 和 N2。

---

## 3. 标题与证明对照表（v4.4）

| # | 位置 | 标题级断言 | 正文实际给出的（及其条件） | 判定 |
|---|---|---|---|---|
| 1 | 标题 | "No Winning Position" | §0 没有定义。§10.4 把它定义为"若有行动者明知而竞赛，则没有赢的位置"，即困难情形。所以标题命名的是理论给出最少的地方；它仍是否定句，也仍用"赢"的语法 | ◐ 理论文件可以保留，但应在 §0 定义；论文换成肯定式标题 |
| 2 | §0 第 2 段 | "derives that prediction from the dynamics of an arms race" | $q_{\mathrm{II}}$ 由 (X)(U)(φ) 推出；$q_{\mathrm I}$ 部分推出（DC 仍在）；L4 与 $p_{\text{dec}}$ 没有推出；有限冲刺的赢家没有覆盖 | ◐ 改为 "reduces it to three premises about the arms race, two of them the racers' own" |
| 3 | §0 认识论段 | 承重的条件是"竞赛者的前提，加上关于每个现有制度的一个事实" | 还需要 (φ)、L4/P3、L5、L6、Lemma D 的定义步和 DC；(U) 是被论证的前提，不是"事实" | ◐ |
| 4 | §0 末；§10.2 | "reason says clearly, in today's world, that the actors must cooperate" | §10.2 的六点给出了内在批评；§12 仍说竞赛前提的证据"will be documented" | ◐ 比 v4.3 好得多 |
| 5 | §0 第 3 层 | "joining buys nothing … fully dissipative limit" | Prop 4(3)，条件已写进句子 | ✓ |
| 6 | §0 第 3 层；§3.4 标题；§14 | "correction cannot keep pace" / "falls behind" | Prop 7 只对超出鲁棒范围的危险类成立 | ◐ 仍未加限定 |
| 7 | §3 标题 | "why racing cannot be won" | 证明的是"不划算"和"保不住" | ✗ 未改 |
| 8 | Theorem A 的名称 | "removes the case for racing" | 去掉的是物质与生存层面的理由；在行动者的目标层面，竞赛仍是最优反应 | ◐ 未改 |
| 9 | (X) | "This is the race premise P2, and it is the racers' own premise" | P2 说能力复利；(X) 说"纠错必须覆盖的、与危险相关的行为种类"按指数增长。两者之间需要一座桥 | ◐（N4） |
| 10 | Lemma M | "Inside the race, the time of perils does not end" | 在 (X)(U)(φ) 下成立，而且其实只需要未覆盖比例有一个正的下界。E3 下"生存为 1"是设定的结果（残余危险取为零） | 极限 ✓；数值 ◐（N6） |
| 11 | Prop 26；Prop 7(5) | "Correction faster than understanding is either absent or delegated"；"delegation in any case" | 在竞赛之内成立（Remark 3）。对竞赛之外、超出理解的纠错，需要一个递归论证：纠错者本身就是超出理解的行为 | ◐（N5） |
| 12 | P2 二难 | "No race is both fast enough to be worth running and slow enough to be corrected" | 渐近成立；但分支 II 不是"失去对象"，而是"可以被纠正" | ◐ |
| 13 | §1.8、附录 C、中文概要 | L4 "no longer assumed but derived" | Prop 27 给出的是选择压力（附录 A 自认 "not a deduction about any particular winner"）；Theorem E 仍假设 L4；P3 不在任何定理里 | ✗（N3） |
| 14 | Lemma D | "Delegation does not carry survival" | "不被选择"推不出"不被代表"；"自主"那一步仍是定义；与 Prop 6(6)、L6 不一致 | ◐（N2） |
| 15 | Theorem S(1)；§0 第 9 层；中文概要第 9 条；§14 | "No branch … secures survival, for any actor … the lone racer included"；"独自竞赛者也不例外" | 对持续复利的竞赛者成立；对有限冲刺后停下的赢家不成立；Prop 29(5) 自己承认了这一点 | ✗（N1） |
| 16 | Theorem S(2) | $\Phi^R$ 有界远离零 | 需要残余危险可求和，这个条件很强；改用危险率的比较更稳 | ◐（N6） |
| 17 | Theorem S(3)；§0 的 "vanishes"；§14 的 "needs no prior trust" | 信任门槛趋于零 | 只在极限下，或在 Prop 23(2) 的区域内成立；在有限情形下是猎鹿博弈，门槛为 0.16、0.42 | ◐ §0 与 §14 说过头 |
| 18 | Corollary 2 | "Every actor's interest is aligned on it, so by Proposition 14 … messages about it can be credible" | 与 Prop 14 的偏差模型相反：那里发送方的偏差，恰是希望对方比状态所需更多地克制，所以它会夸大共同危险。第二条理由（来自公开前提的推导）成立 | ◐（N7） |
| 19 | Prop 27 | "(L4) is … what the race selects for" | 作为选择压力 ✓；"instrumental convergence and reward hacking" 是类比，没有写成映射 | ◐（N11） |
| 20 | Prop 28 | "This is the strongest answer to the claim that alignment will scale" | 一个数值例（$L_c=100L_e$），是存在性结果；用 Lemma D 可以得到更强的一般形式 | ◐（N11） |
| 21 | Prop 29 | "Each step fails for a reason the race itself supplies" | (2) 还需要一行推导；(5) 承认赢家的安全，与 Theorem S(1) 冲突 | ◐（N1） |
| 22 | Prop 25 | 每种手段的需求，都被 (K) 或 (A) 推向反方向 | 逐项写出了依赖；析取已删除 | ✓ |
| 23 | Corollary 3 | 斗争与持久的安全互斥 | 在 Theorem E 的条件下成立 | ✓（(3) 的措辞见 A4） |
| 24 | §8.5；中文概要 | AI 2040 是"伪解" | 以 Plan A 保留 H0∧H1 为条件；"保留 H1"是断言；部分事实需要核实 | ◐（N12） |
| 25 | Lemma E0 | 不经协议结束竞赛，保不住每个行动者的生存 | 成立；赢家一侧的"两只钟"只被点名 | ✓ |
| 26 | Theorem E（主陈述） | 若每个行动者的生存都有界远离零，则至少有一个 H 被否定；若竞赛结束，则以协议结束 | 不再循环；假设表仍含 L4 与 DC | ✓（残余见 N2、N3） |
| 27 | Theorem E(1) | "¬H3 is necessary in every case, including under cooperation" | 需要递归论证，或者 contestability 这一规范前提 | ◐（N5） |
| 28 | Theorem E(2)；§0；§14；中文概要 | "the theorem form of 'the world must cooperate'" | 经由 DC、L3、L5、Lemma D 推出；漏了 "every actor"；与 L6 冲突。修复后反而更强 | ◐（N2） |
| 29 | E2 | "By Lemma M this is self-enforcing in survival terms" | 若决定性类别（ASI、RSI）被定义为超出可争议理解的能力，基本成立；对一般的决定性能力，$r$ 大时小幅领先就能取胜，不成立 | ◐（N1） |
| 30 | §10.5 "The order" | "The order is Ren's priority: E1 first, E3 always, E2 …" | Ren 的次序是：E1；其次，E2 或 E3。"E3 always" 来自 Lemma M。附录 C 的来源说明写的是 "the order E1, then E2/E3" | ✗ 归属错误（N8） |
| 31 | §10.6 | "holds exactly as far as Theorem E's conditions do" | 诚实 | ✓ |
| 32 | §10.7 | "If AI is not decisive, E2 costs nothing" | 在竞赛中没有代价，但放弃了 ASI 的非竞赛价值 | ◐ |
| 33 | §14 末句 | "not who comes first, but what every actor needs in order to go on" | 与全文一致 | ✓ |

---

## 4. 新问题（按严重度排列）

### N1【致命】Lemma M 是渐近的，而立场方最强的版本是有限时间的："冲刺到决定性优势，然后放慢"

**位置：**
- Theorem S(1) 中的 "includes the strongest actor and the lone racer"；
- §6.2 中的 "Lemma M supplies the ratio"；
- §10.5 中 E2 的 "self-enforcing"；
- Lemma E0 的支配情形；
- §13 对"暂停把优势让给不暂停者"的第二个回答；
- 中文概要第 9 条，§0 第 9 层，§14 的 "not racing alone"。

**问题：**
- **Lemma M 说的是什么。** 沿着*持续*的竞赛（$H\to\infty$），未覆盖的比例趋于一，危险率不可求和，所以生存趋于零。它回答的是"一直复利下去会怎样"。
- **立场方说的是什么。** 他们的主张是有限时间的：在 $t_{\text{dec}}$ 取得决定性优势，然后停止复利，在理解的节奏内治理。这正是 §8.1 "a lead buys a safety margin" 的终点，也是"先赢后治理"。
- **CSF 模型给出的结果。** $r$ 越大，赢所需的能力差距越小。要使 $w_i\ge1-\epsilon$，只需 $\sigma_i/\sigma_j\ge((1-\epsilon)/\epsilon)^{1/r}$，而当 $r\to\infty$ 时这个比值趋于 1。所以，面对克制者，孤立竞赛者不必走到理解之外很远。在 (φ) 下，它暴露在未覆盖区域的时间是有限的，生存概率有界远离零。
- **文本自己承认了这一点。** Prop 29(5) 写道："If the margin works and the leader prevails … The safety bought is the winner's, not every actor's"。这与 Theorem S(1) 的"赢家的生存也趋于零"直接冲突。
- **E2 也受影响。** "背叛暂停，就是独自建造超出自己理解的东西"，只有当决定性类别本身被定义为超出可争议理解的能力时才成立。RSI 按定义就是不按人的节奏复利，ASI 按定义就超出人的理解。对一般的决定性能力，这句话不成立。

**为什么重要：** "我为什么不能赢了就停？"这是 Ren 要回应的那类人最强的一句话，上一轮的 A2 也指向这里。如果"独自竞赛者也不例外"这句标题级断言在这里被打开，冷读者会认为全部"没有赢家"的结论都只是渐近的修辞。

**修复：** 不需要新的数学，只需要分情形。
1. **按赢家的目标分成两类。**
   - **目标没有"够了"的赢家**（unbounded relative，即 L4 的对象）。它不会停止复利：领先到任何程度，这个目标都不会停止奖励"更多"。所以 Lemma M 适用于它自己的能力，$\Phi^T\to0$。这正好是 Ren 的癌的意象的精确形式：癌式逻辑在毁掉宿主的同时，也毁掉自己。建议把它写进 Theorem S(1)，并在 §10.4 用一句话点出："the logic to oppose destroys its own bearer"。这样，"反对这个逻辑"就有了理性上最强的理由：它对持有者本身也是死路。
   - **会在"够了"处停下的赢家。** 理论给不出极限，能给出的是三种压力和一个选择论证：
     - 冲刺期间暴露在未覆盖区域：$\Phi^T\le\exp(-h\varphi\int_{\text{sprint}}(1-U/X)\,dt)$；
     - 被即将被支配者预防性攻击，即 $q_W$。Prop 8 表明，面对决定性而且快的权力转移，在 A8 下攻击是理性的；
     - 冲刺途中为了速度而委托，于是 Lemma D 适用。Prop 6(1) 表明，对手都不委托时，委托的收益最大；
     - 选择论证：Prop 27 说，会停下的赢家在赢之前就被选择淘汰，赢之后又在它自身内部被选择淘汰（§4.4）。
2. **再加一个均衡论证。** 在竞赛前提下，T 分支不是任何人能停留的分支。"会停下"的承诺无法核实（Props 8、15），所以克制者把它当作 L4 对待，并按 Prop 4(1)（加入或消灭）转入 P 分支，或者发动预防性攻击。因此，一个打算"赢了就停"的竞赛者，实际所处的分支是 P（所有人都在复利，Lemma M 与 Prop 6 都适用），或者是战争。这正是 Ren 截图里的"要么暴力的消灭，要么加入"。
3. **把 E2 的对象定义为超出可争议理解的能力类别（ASI、RSI）。** 这就是上一轮的 X₂，也是 Ren 说的"第二种要看我们造出来的是什么"。在这个定义下，E2 的自我执行论证成立：背叛者无法可靠地停下一个按定义就超出其理解的东西（(φ) 加上 Prop 26）。
4. **标题级断言改为：** "No branch of a continued race secures survival for an actor that keeps racing. A winner that would stop at enough is the hard case: it is exposed during the sprint, invites preventive attack, cannot make its stopping credible, and is what the race selects against." 中文概要第 9 条与 §14 相应修改。
5. **在 §8.4 的树中加一问：** "Q4′. Will you stop compounding once you lead?"
   - 否：Lemma M 适用于你自己。
   - 是：见上面三种压力；而且其他行动者无法核实你会停下。

### N2【高】L6 加上 Lemma D，与"被迫委托"冲突；修复后得到一个更强、也更忠实的"世界必须合作"

**位置：** Prop 6(6)；Lemma D；Theorem S 与 Theorem E 的假设 "the delegation condition of Proposition 6(5)"；Theorem E(2) 及其证明；§10.2 第 3 点。

**问题：**
- **委托本身有生存代价。** §10.1 说生存包含自主；Lemma D 说锁定的委托结束作为行动者的生存。所以对生存优先者，委托本身就有代价：锁定之后 $\Phi=0$。
- **Prop 6(6) 的生存形式不完整。** $\Phi_i=Q[w_i+(1-w_i)(1-p)]$ 只计入了失控 $Q$，没有计入锁定。按理论自己的定义，这个形式是不完整的。
- **计入锁定后的结论。** 没有别人委托时，一个知道 Lemma D 的生存优先者永远不会先委托：委托即使赢了，赢的也是被委托的过程。所以，Theorem E(2) 用加法度量下的 DC 推出"委托变得占优"，在 L6 之下不成立。上一轮综合第 5 条已经提到这一点（"对生存优先者，委托是一个选择"），v4.4 没有处理。
- **附带问题：Lemma D 的证明。** 证明用 Lemma 0 推出 "retained systems' behaviour on such terms is not selected for the actor's stake"。但"不被选择"推不出"不被代表"。这里需要的是 Prop 1：凡是改变行动的、代表共同利益的行为（也就是克制），都会被选择淘汰。

**为什么重要：** 博弈论读者会发现这个矛盾，并以此否定"世界必须合作"的定理形式，因为 Theorem E(2) 正是经由 DC 推出的。

**修复：** 建议加入一个新命题，以替换 Theorem E(2) 对 DC 的依赖。

> **Proposition (Two zeros).** Let (L3), (L5), Lemma D, and (L4) for delegated processes with P3 hold, so that losing to a delegated process with decisive advantage means subordination ($p\to1$). Consider a survival-first actor.
> (i) If no other actor delegates, not delegating is strictly better in $\Phi$: delegating ends survival as an actor at the lock even when the delegated process prevails.
> (ii) If any other actor delegates, then as $s$ grows both options tend to zero: delegating, by Lemma D; not delegating, because $w_i\to0$ and $p\to1$.
> (iii) Hence E1 is self-enforcing among survival-first actors who hold the prediction of Lemma D, and it fails for all of them if any capable actor delegates. An actor with a relative objective delegates at every $s>0$ (Proposition 6(4)), and the race is set by the most race-inclined actor (Proposition 4(4)). So E1 must cover every capable actor (Definition 3(a)), and survival over an unbounded horizon requires E1 held in common or the contest ended by agreement.

这个命题比现稿强在四处：
- 它不需要 DC；
- 它与 L6 和 Lemma D 一致；
- 它把"E1 第一优先"从 Ren 的价值次序，变成了模型内的理由：E1 是唯一在知情的生存优先者之间自我执行的出口；
- 它是 Ren 截图第 1、3、7 条（"被迫 delegate"、"第一种基本完蛋"、"要么暴力的消灭，要么加入"）在生存度量下的直接形式。

还需同时做三件事：
1. **Prop 6(6)：** 加入锁定的代价；或者明确写明，它描述的是不相信 Lemma D 的行动者。后者在描述上也有价值：竞赛之所以在进行，部分是因为行动者相信"我们对齐的 AI 就是我们"。
2. **Theorem E(2)：** 写成 "every actor's survival over an unbounded horizon"。
3. **Lemma D：** 证明改用 Prop 1。"作为行动者的生存结束"如实写成一步：锁定之后，没有任何替该行动者作决定的过程会权衡它的共同项，所以它的生存取决于没有人管理的危险。

还有一点实际意义。Lemma 1 已经表明，维持 $\mathcal K\ge\mathcal K_{\min}$ 就能解除锁定。委托可以是渐进的，"without a visible line"，所以 E1 的可操作形式就是并行维持人的能力。这一点可以和第 (iii) 条写在一起。

### N3【高】L4 与 $p_{\text{dec}}$ 并没有被"推出"；P3 没有进入任何定理；"认知被筛选"没有用上理论里最合适的结果

**位置：**
- §1.8 的 L4 条目与该节末段；
- 附录 C；
- 中文概要（"赢家是被竞赛选择出来的"）；
- Theorem S(1)（"By Proposition 27, the race selects for (L4). Hence … $\Phi^S\to0$"）；
- Theorem E 的假设表 "(L3)–(L6)"；
- §10.7 的 P3。

**问题：**
- **说法前后矛盾。** 附录 A 对 Prop 27 的说明是 "a statement about the selection pressure the race applies, not a deduction about any particular winner"，这是诚实的。但 §1.8 写的是 "(L4) is then no longer assumed but derived"，两处互相矛盾。
- **Theorem E 仍假设 L4。** 这本身没错，但与"derived"的说法不一致。
- **P3 没有进入定理。** $\Phi^S\to0$ 还需要 $p^S_{\text{dec}}\to1$，它来自 P1 和 P3（优势不饱和）。§10.7 写了 "This should be stated as a premise of its own, P3"，但 P3 没有进入 §1.5、Theorem S 或 Theorem E。
- **"认知被筛选"只写了一句。** Ren 说的是"agent 的 cognitive model 是被筛选的"。Prop 27 的前五条都是关于行动、行动者、控制权和被委托系统的选择；关于认知，只有一句 "The environment and its positive feedback shape the models that agents form"。而 Prop 3(4) 自己列出的第二条结果正好适用于 AI 竞赛：偏好可观测且 $n\ge3$ 时，偏向 $\theta<0$ 的承诺扭曲是有利的（Güth and Yaari 1992；Heifetz, Shannon and Spiegel 2007）。少数几个行动者、学说公开、彼此观察，这正是前沿 AI 竞赛的结构。

**修复：**
1. **改措辞。** 写成："(L4) is grounded rather than assumed ad hoc: the race selects for it (Proposition 27), and no winner can credibly disavow it (Propositions 8, 15). It remains a premise of Theorems S and E." 中文概要与附录 C 相应修改。
2. **加入 P3。** 把 P3 写进 §1.5 的竞赛前提（P1、P2、P3），并列入 Theorem S 与 Theorem E 的假设。
3. **给"认知被筛选"找到理论内的根据。** 在 Prop 27 中加一条：在行动者少、自我模型可观测的结构里，偏好层面的选择也偏向 $\theta<0$（Prop 3(4) 第二条）。这样 Ren 的"认知被筛选"就有了理论内的、带文献的根据，又不违反 Prop 3(4) 已经写下的范围限定。还可以再加一个机制：竞赛把具有相对认知的人和机构选入决策位置，也就是 meta-attractor 所说的 "selected minds build selected organizations"。这是对决策者的选择，与偏好演化是两回事。
4. **把类比写成映射。** "instrumental convergence and reward hacking" 应当写成映射，而不是类比：
   - 代理指标是相对地位；
   - 真实目标是 $W$ 或 $\Phi$；
   - 竞赛以真实目标为代价去优化代理指标，这就是 Prop 3(2) 与 Prop 3(4)。

   另外，Turner 等（2021）讲的是 MDP 中的最优策略，不是 "competitive reward environments"，引用时的描述需要收窄。

### N4【高】"(X) 就是竞赛者自己的前提"需要一座桥；Lemma M 的极限比写出来的更便宜，所以内容不在极限里

**位置：** §10.2 的 (X)；"Why the conditions hold today" 第 1 点；§0 认识论段。

**问题：**
- **P2 与 (X) 不是同一件事。** P2 说能力增长很快，领先在短窗口内打开；(X) 说"纠错必须覆盖的、与危险相关的行为种类"至少按指数增长。竞赛者会接受前者，而否认后者："能力在复利，但我们把与危险相关的行为限制住了（隔离、窄部署、控制）。"这正是他们"可控"的主张。
- **极限本身不是内容。** Lemma M 的极限只需要两样东西：未覆盖比例有一个正的下界，再加上 (φ)。也就是说，即使理解按指数增长，只要它覆盖不了全部，结论照样成立。冷读者会说："你假设了一个常数危险率，然后发现无穷长的时间里必然出事。"真正的内容是另外两点：
  - 竞赛下的危险率趋于它的最大值 $h\varphi$；
  - E3 下的危险率停留在残余水平。

**修复：**
1. **把 (X) 拆成两部分：**
   - (X1) 能力复利，即 P2，这是竞赛者自己的前提；
   - (X2) 作为竞赛工具的能力是通用的，并被部署到竞赛的各个领域，所以纠错必须覆盖的行为随能力一起增长（Ashby 的必要多样性）。

   (X2) 要列入 §12 的条件表。反驳它的观测是：在决定性能力类别上，与危险相关的行为种类被证明是有界的。
2. **在 Lemma M 后加一句说明：** 极限只需要未覆盖比例有正的下界；(U) 决定的是危险率趋近 $h\varphi$ 的速度。这样写反而更稳，因为它表明结论对"理解增长得多快"不敏感。
3. **与 N6 一起，把 Theorem S(2) 改成危险率的比较。**

### N5【中高】回应"用 AI 让 AI 安全"还差一步：超出理解的纠错者本身就是超出理解的行为；(U) 的根据应以后果反馈为主

**位置：** Prop 26；Prop 7(5) 的 "delegation in any case"；Theorem E(1) 的 "including under cooperation"；§10.2 中 (U) 的三条根据。

**问题：**
- **竞赛之外的情形没有覆盖。** Prop 26 的第二支在竞赛之内成立（Remark 3）。但对于竞赛之外的、独立的、人无法理解的 AI 纠错，Lemma D 不适用，因为它不是"为竞赛表现而被保留的"。于是 Theorem E(1) 的"在合作之下 ¬H3 也是必要的"缺了一个理由。现稿只能诉诸 contestability 这一规范前提。
- **(U) 的根据不是最强的。** (U) 的第一条根据是"人的智能受生物学限制"。对齐研究者会回答：可扩展监督可以让人的判断借助 AI 扩展。Ren 自己的语料里有更强的根据：判断依赖后果反馈，而后果反馈的形成有一个不可压缩的下限（2026-08-22 的立场论文；09-28 论文的 epistemic lag，即 Prop 7(4)）。工具可以提高观察的吞吐量，但不能让后果更早发生，也不能让人更快地理解它。

**修复：**
1. **在 Prop 26 中加一句递归论证：** "A corrector whose decisions lie beyond $U(t)$ is itself hazard-relevant behaviour beyond $U(t)$, so Lemma M applies to it. Correction beyond understanding does not reduce the uncovered fraction; it relocates it." 这样，Theorem E(1) 在合作之下也成立，而且不必依赖规范前提。这也是对"AI makes AI safe"最干净的回答：监督者本身就是需要被监督的一部分。
2. **重排 (U) 的根据：**
   - 第一条：后果反馈的不可压缩下限（Prop 7(4)）；
   - 第二条：制度的节奏；
   - 第三条：生物学限制。
3. **在 §12 的 (U) 一行写明它与可扩展监督的关系。** 如果可扩展监督被证明在决定性能力类别上既保持可争议、又按能力的速度增长，(U) 就被反驳了。现有的反驳条件已经接近这一点，可以直接点名。

### N6【中】Theorem S(2) 要求"残余危险可求和"，太强；E3 下"生存为 1"是设定的结果

**位置：** Theorem S(2)；§12 的 $h_R$ 一行；Lemma M 后的数值；`checks_v44.py` 中的 `run_mismatch(capped=True)`。

**问题：**
- 任何安排都不会有可求和的长期危险，冷读者会立刻指出这一点。
- 数值中 E3 的生存为 1，是因为覆盖范围之内的危险被设为零。

**修复：**
- 改用危险率的比较："If the long-run hazard rate under the arrangement, $\bar h_R$, is below $h\varphi$, then $\Phi^X(H)/\Phi^R(H)\le e^{-(h\varphi-\bar h_R)H}\to0$." 这只需要"竞赛下的危险率高于安排下的危险率"，比可求和弱得多，却同样给出比值趋于零，从而支撑 Theorem S(3) 与 §10.1 的比值准则。
- 数值中给 E3 加一个正的残余危险（例如 $h\varphi$ 的十分之一），并报告两条生存曲线。这正好可以作为论文的图 2。

### N7【中】Corollary 2 的第一条理由与 Prop 14 相反；"认知被筛选"与"预测可以被每个行动者自己核验"之间有张力

**位置：** Corollary 2；§10.3；Prop 14 的设定。

**问题：**
1. **第一条理由与 Prop 14 相反。** 在 Prop 14 中，发送方的偏差恰恰是"希望接收方比状态所需更多地克制"。关于共同危险的消息，正是发送方最想夸大的，因为夸大会让对手放慢。所以 "every actor's interest is aligned on it, so … messages about it can be credible" 与理论自己的模型相反。
2. **与 Prop 27 有张力。** Prop 27 说竞赛选出看不见共同条件的认知；Corollary 2 说预测是每个行动者都能自己核验的推导。如果决策者的认知被选择得看不见共同危险，"能核验"就不等于"会核验"。

**修复：**
1. **处理第一条理由。** 删去它，或者改写为：在生存度量下，对相对地位的有效权重是 $\lambda_{\text{eff}}=\lambda c_{\text{conv}}$（§10.3），所以偏差 $b=\lambda_{\text{eff}}\beta_s$ 随 $c_{\text{conv}}\to0$ 而消失。但这只对已经接受这一预测的行动者成立，所以可信度一旦开始被共享，就会自我加强。

   主要依靠第二条理由：预测是从公开前提出发的推导（要补上 (φ)），不依赖私人信息。这也正是 Ren 说的"理性可以明确告诉我们"。
2. **把张力写成一个关于时间的结果。** 过渡必须赶在两只钟之前到来：
   - 一只是锁定（$T_{\text{lock}}$）；
   - 另一只是对决策者认知的选择。这正是 meta-attractor 所说的过程：其他选项先停止再生产，然后变得不可理解。

   所以"越早越好"有两个独立的理由。这既忠实于 Ren，也让 Corollary 2 更锋利。

### N8【中，忠实度】出口次序的归属；"意识条件"；E3 与"成长不是危险"

**位置：** §10.5 "The order"；E2；中文概要第 9 条；附录 C 的来源说明。

**问题：**
- **次序的归属。** 正文写的是 "The order is Ren's priority … E1 first … E3 always … E2 as the measure that holds the trajectory open"。Ren 的原话是：
  - E1 优先；
  - 其次，如果连这个都做不到，先别搞 ASI、RSI，先停下来（E2）；
  - "要么"把发展速度降到认知以下（E3）。

  "E3 始终必要"来自 Lemma M，不是 Ren 的次序。附录 C 的来源说明写的是 "the order E1, then E2/E3"，与正文不一致。上一轮综合把"E3 的地位"列为需要 Ren 决定的第 2 项，方向记录里没有他的回复。
- **"意识条件"。** E2 仍写 "social and cognitive conditions"，而 Ren 写的是"社会和意识条件"。按他 9 月 25 日的裁定（"the problem is the mind not the approach"），"意识"指的是自我模型与共同理解，而不只是认知能力。
- **E3 与"成长不是危险"。** "E3 always, including under cooperation" 可能被读成"增长本身就是危险"，这与 Ren 9 月 25 日的裁定（"we can grow exponentially till we met our need, but we can't compounding forever"）有张力。

**修复：**
- **次序。** 写成："E1 first (Ren's priority). E3 always: this is derived (Lemma M, Theorem E(1)), and it matches the corpus's 'development within understanding'. E2, Ren's pause, holds the trajectory open." 并请 Ren 确认。
- **"意识条件"。** 可以写成 "the social conditions, and the shared self-understanding ($\theta$, Section 2.3; the prediction of Corollary 2), for governing it"。
- **E3。** 加一句：以需要为方向的发展有"够了"的点，自然满足 E3（§10.8 "Good enough"）；E3 约束的是没有"够了"的复利。这样就与"成长不是危险，心才是"一致，也与 N1 中"癌式逻辑连自己一起毁掉"连成一线。

### N9【中】次序：第 8 节依赖第 10 节

**位置：** §8 全节。它用到的 Lemma M、Props 26 和 27、Theorem E(2)–(3)、Lemma D，都要到 §10 才出现。

**问题：** 从 §8 读起的读者，会遇到一串尚未定义的引用。论证在逻辑上是一个，在阅读顺序上却是倒置的。

**修复：** 理论文件和论文都适用。次序改为：
1. §1–5 保持不变；
2. §6，为什么竞赛失败（Theorem 1、A）；
3. 新的 §7，生存与军备竞赛，即现 §10.1–10.3：生存，(X)(U)(φ)，Lemma M，Props 26–27，Lemma D，Theorem S，Corollary 2；
4. §8，信任与验证；
5. §9，立场 (K)(A)(S)，即现 §8；
6. §10，出口，即现 §10.4–10.8 加上 Theorem E；
7. §11，必须改变什么，即现 §9。

这样主梁就是线性的：机制 → 生存 → 预测 → 信任 → 立场 → 出口 → 合作的内容。

### N10【中，冷读】噪音与署名

**位置：** 全文。

**问题：**
- "repair" 出现 129 次；附录 C 之前，版本号出现 97 次。
- 正文有 "Ren's reading of AI 2040"、"The derivation follows Ren's reply"、"Ren's image for it is cancer"、"The order is Ren's priority"。

冷读者无法理解这些，也会把整份文件读成一份未完成的稿子。

**修复：**
- 理论文件保留来源，这对 Ren 的工作方式是必要的。但正文只保留一种低噪音的标记，例如每处修复只留一个上标编号，对应附录 C 的条目。
- 另出一份干净的阅读稿 `THEORY-clean.md`，用脚本去掉 repair 括注和版本说明句。
- 论文以干净稿为母本。

### N11【中】新的"命题"通胀：Prop 27、28、29

**问题：**
- Prop 27 由五条已有结果、两条外部机制和一句类比组成；
- Prop 28 是一个参数组合（$L_c=100L_e$）下的数值例，却被称为 "the strongest answer to the claim that alignment will scale"；
- Prop 29 是已有结果的组合，其中 (2) 还需要一行推导，Lemma M 本身并不直接给出它。

**修复：**
- **Prop 27** 分成两部分：由理论推出的部分（前五条），以及引用的机制和 Ren 的解释（后两条）。
- **Prop 28** 改称 "Example"，或 "Proposition (risk compensation, existence)"，并补上一般形式：任何使 $\Delta\psi$ 越过 Prop 6(5) 委托阈值的改进，都会使实现的危险率从基线跳升。在生存度量下再加上 Lemma D，这次跳升对委托者而言就是 $q_{\mathrm I}$ 从零跳到一。这比"失控率上升 10%–33%"强得多，而且用的是理论自己的语言。
- **Prop 29(2)** 补一行推导：领先 $\Delta$ 的时间里能补上的覆盖，约为 $U'\Delta$，而未覆盖的量 $X-U$ 按指数增长。

### N12【中】§8.5 缺一般的"伪解检验"；Plan A 的若干细节需要核实

**问题：**
- **只批评了一个方案。** §8.5 的框架是对的（"form of cooperation, content of race"），也公允地承认了 Plan A 的目标。但它的 "disguise" 部分是按 Plan A 的细节逐条写的。读者得到的是对一个方案的批评，而不是一个能用于任何方案的判据。这与 Ren 的"AI 2040 不是主要对象"、"回应立场而不是文件"略有偏差。
- **"Plan A 保留 H1"是断言。** "Plan A keeps H1"（AI 仍是竞赛的工具）没有论证，而 Theorem E(3) 能否用于 Plan A 正取决于这一点。
- **细节需要对照原文核实：**
  - "roughly even odds by 2040"，这实际上就是 v4.3 删去的 51% 那个数字；
  - "which it calls the hardest part to execute"；
  - "its own verification plan concedes that such verification is not yet mature"；
  - 作者名单。
- **显眼程度。** 中文概要单独列出 AI 2040，使它比正文里的定位更显眼。

**修复：**
1. **§8.5 以一个一般定义开头：** "An arrangement is a *pseudo-solution* if its stability requires the probability of timely detection to approach one as the value of winning grows (Theorem B), that is, if it bounds the gain from defection by detection and deterrence rather than lowering it. It treats detectable defection, a symptom of the race, with the race's own means." 判据有三条：
   - 它是否降低赢的价值（Def 3(d)）；
   - 它是否把 AI 移出竞赛（Def 3(e)）；
   - 它是否按理解的节奏发展（E3）。
2. **Plan A 压缩为一段，作为例子，并写成条件句：** "To the degree that it keeps H0 and H1 (proportional standing, deterrence, AI in the contest's instruments), Theorem E(3) applies."
3. **保留现有的结尾句**，那是这一节最好的部分："not a different plan but the same direction carried through"。
4. **中文概要**把这一条改为"保留竞赛于其下的验证协议是伪解（例如 AI 2040）"。

### N13【低至中】§0 与 §14 的若干过头措辞

- §0 第 9 层的 "the trust threshold vanishes"，改为 "tends to zero as the race continues"。
- §14 的 "cooperation needs no prior trust"，改为 "needs little prior trust, and none in the region of Proposition 23(2)"。
- §0 第 3 层的 "correction cannot keep pace"，加上 "for hazard classes beyond the robust reach of the available correction"。
- §3 的标题改为 "what racing costs"；Theorem A 改名为 "…removes the material and survival case for racing"。
- P2 二难：分支 II 不是"失去对象"，而是"慢到可以被纠正"。建议改为 "No race is both fast enough to open decisive leads within short windows and slow enough to stay within correction"。
- §10.7 的 "E2 costs nothing"，改为 "costs nothing in the contest"。

### N14【低】错误与一致性

- E3 中的 $a\,\tau_{\text{eff}}$ 应为 $a\,\tau_c$。$\tau_{\text{eff}}$ 是有效责任的符号（§1.2）。
- Corollary 3(3) 的措辞，见 A4。
- Theorem E(2) 的量词，应写 "every actor's"。
- Corollary 2 的公开前提只列了 P1、P2 和 (U)，漏了 (φ)。
- Prop 29(1) 用 Theorem B(2) 来支持"领先的大小无法核实"；更准确的依据是 Prop 14 和 Theorem B(3)。
- "Verification can replace belief in intentions only to the extent…" 一句，在 §7.1 与 §8.2 逐字重复。
- Stafford、Trager 和 Dafoe（2022）在 §8.1 被描述为"领先足够大时，领先者可以投资于安全"，在 §13 被描述为"安全改进可能被风险补偿抵消"。需要对照原文，二者择一，或分别注明。
- Prop 3(3) 仍是同义反复；§2.3 的 "In plain words" 仍是先结论后条件。两处都是上一轮 A21 提过的。

### N15【低】长度与重复

**问题：** 正文约 2.87 万词，加上附录共 3.64 万词。同一个回答出现在多处：
- "先赢后治理 / 良性赢家"：§4.4、§6.3 的表、Prop 25(5)、Prop 27 后的段落、§8.4 的 Q4、§13；
- "用 AI 让 AI 安全"：Prop 7(5)、Prop 26 后的段落、Prop 25(2)、Prop 25 的表、§13；
- 威慑：§6.3 的表、Prop 25(1)、§13；
- 自我模型的修正：§2.3 末段与 §9.4。

**修复：** 不删内容，遵守"不做有损的合并"。每个回答只在一处完整陈述，建议放在立场一节；其他地方用一句话加交叉引用。这样正文大约可以减少 10%，而不丢任何结果。

---

## 5. 对 Ren 方向的忠实度（重点是 10 月 3 日的最新方向）

| Ren 的原话（摘要） | v4.4 的表达 | 判断 | 建议 |
|---|---|---|---|
| "生存是最低博弈需求" | §0 第 2 段；§10.1，引现实主义的生存前提 | ✓ 忠实 | — |
| "我们可以预测当下 trajectory 的博弈预期 outcome" | $\Phi_i(H)$；Corollary 2；"before the lock" | ✓（有缺陷） | 第一条理由与 Prop 14 相反；补上"两只钟"（N7） |
| "如果胜利者的逻辑是 cancer 式的，落后并不可以承受，因此所有人都应该去首先反对这个逻辑" | §10.4：一个定义，两种来源；"反对"即使 L4 对所有人都不成立；两类型结果；Remark 6 | ✓ 前半句，以及"反对"的内容，是忠实的；◐ "首先"的次序与最强的理由说弱了 | 用 Lemma M 说明癌式逻辑连自己一起毁掉（N1）。把"反对这个逻辑"放在出口之前，作为第 0 步，并与 Corollary 2 相连：反对的方式，是让"它会毁掉持有者"成为共识 |
| "如果不能合作：优先选择是不把 ai 本身和对 ai 的使用嵌入或者变成这种逻辑……否则博弈游戏会收敛主导权会递交" | E1a/E1b；"Once dominance has passed to delegated systems, no transition remains possible" | ✓ 两半都表达了，范围也对 | 用"两个零"给 E1 一个模型内的自我执行理由（N2） |
| "其次……人类应该有自知之明，先别搞 asi，rsi……技术条件达到了，但是社会和意识条件依然未达到，应该先停下来，让合作变得可能，可以理性思考，再去造更复杂的 ai" | E2 "build the conditions for governing it first"；"social and cognitive conditions"；理由是 "self-enforcing by Lemma M" | ◐ 肯定式的命名好，"再去造"的时间顺序也保留了；但"自知之明"被换成了战略理由，"意识"被换成了 "cognitive" | 把 E2 的对象定义为超出可争议理解的能力类别（X₂，见 N1 第 3 点）；"意识条件"接到自我模型与共同理解上（N8） |
| "要么就把发展速度降低到认知以及通过认知可以做出应当应对的速度以下" | E3，含 $\mathcal K\ge\mathcal K_{\min}$ 与可争议性 | 内容 ✓ 忠实；地位与归属 ✗ | "E3 always" 是模型的结论，不是 Ren 的次序；请 Ren 确认（N8） |
| "其他都是人类绝路啊" | §10.6："holds exactly as far as Theorem E's conditions do" | ✓ 诚实 | — |
| AI 2040 是伪解；要消解它的伪装，但它不是主要对象 | §8.5 的框架与结论句 | 框架 ✓；执行 ◐ | 先给出一般的伪解检验，Plan A 只作为一段例子（N12） |
| 完美回应"即打算不改变斗争思想，又打算加速，还想安全的人" | §8：立场重新定义；主形式 Prop 29；树；Props 25、28；Corollary 3 | ✓ 结构上接近完美 | 缺的两步，正是这些人最强的两句话："赢了就停"（N1），"用 AI 监督 AI"（N5 的递归论证） |
| "要考虑人类的 intelligence 有限并无分指数增长……认知……是线性，或者低于线性" | (U) | ✓ | 以后果反馈的不可压缩下限为主要根据（N5），这是 Ren 自己 08-22 立场论文的论证 |
| "风险增长的速度超过纠错速度……对于我们社会下的所有体制来讲，这个都是对的……现实复杂度增长与认知增长速度之间的错配……而我们社会当下就面临这样的问题" | Lemma M；Ashby、pacing problem、ingenuity gap；"societies faced it before AI" | ✓ 忠实，文献选得好 | 说明极限对理解的增长速度不敏感，这反而加强了 Ren 的判断（N4） |
| "meta attractor 给出了一个 agent 的 cognitive model 是被筛选的" | Prop 27 中的一句 | ◐ 说弱了 | 用 Prop 3(4) 第二条，并加入"把具有相对认知的人与机构选入决策位置"这一机制（N3） |
| "环境和正反馈也构造 cognitive modeling，我们的社会现状就是一个巨大的 instrumental convergence，和 reward hacking" | Prop 27 的第六条 | ◐ 是类比，没有写成映射 | 代理指标 = 相对地位；真实目标 = $W$ 或 $\Phi$；Goodhart = Prop 3(2)、3(4)（N3 第 4 点） |
| "在现实条件下，这几个 →1，本身可以被继续证明，或者至少有理性判断的答案" | §10.2 的推导与 "Why the conditions hold today" | ✓ 这一步做对了 | 措辞应是"归约为前提"，而不是"已经推出"（N3） |
| "这两个主要问题，并不在我的理论，arms race 自然创造这几个 →1 的 dynamics 的条件，而现在的 trajectory，就是 arms race" | "They are what an arms race does"；"the present trajectory is an arms race" | 框架 ✓；"现在就是军备竞赛" ◐ 仍未举证（§12 写着 "will be documented"） | 用不点名的公开证据，先在 §12 补三条：前沿安全框架中以竞争对手为条件的条款（S13）；算力扩张；公开的"竞赛"叙事 |
| 写作纪律：不点名国家与公司 | 用 grep 核对过：没有点名 | ✓ | 论文中对 Amodei、Aschenbrenner 的引用，保持为对其论点的引用 |
| 写作纪律：机制先于结论，肯定优先于否定 | §10.4 先定义、后意象 ✓；出口的名称是肯定式 ✓；§2.3 仍先结论后条件 ✗；标题仍是否定式 ◐ | ◐ | — |
| 写作纪律：不偷带 win/race 的语法 | 末句已改 ✓；"keep pace" 仍有数处，问题轻微 | ✓ | — |
| 写作纪律：不做有损的合并 | Tier 结构保留；全部结果保留；Theorem C 是降级而不是删除 | ✓ | 重复用交叉引用解决，不删（N15） |
| 认识论："没有任何一个定理能证明'世界必须合作' 这个我'不同意'……但是，我觉得在今天的世界，这已经是理性可以明确告诉我们的了" | §0 认识论段改为以肯定句开头："The conclusion is derived from conditions…" | ✓ 上一轮的 ✗ 已修复 | — |

**总评。** v4.4 是迄今对 Ren 方向最忠实的一版。偏差都能在一处修好，而且多数修复会同时加强论证。在这里，忠实与严谨并不冲突。Ren 的几条直觉正是 N1、N2 和 N8 的修复方向：
- 癌式逻辑连自己一起毁掉；
- 要么消灭，要么加入；
- 要看造出来的是什么；
- 问题在心。

---

## 6. 冷读风险

| 冷读者会怎样否定 | 来源 | 如何化解 |
|---|---|---|
| "你假设了常数危险率，然后发现无穷长的时间里必然出事；E3 下的危险被你设成了零" | Lemma M；Theorem S(2)；数值 | N4、N6：说明极限为什么便宜；以危险率的比较为主；给 E3 加上残余危险 |
| "竞赛会结束。赢了就放慢" | Theorem S(1)；E2；Prop 29(5) 自己承认 | N1：区分两类赢家；论证 T 分支不稳定；把 E2 的对象定义为超出理解的能力类别 |
| "按你自己的 Lemma D，生存优先者根本不会委托" | Prop 6(6)；DC；Theorem E(2) | N2："两个零"命题 |
| "可扩展监督会让人的理解随能力扩展" | (U) | N5：后果反馈的下限；递归论证 |
| "关于共同危险的消息，正是最会被夸大的" | Corollary 2 对 Prop 14 的引用 | N7 |
| "你说 L4 是推出来的，可它还在你的假设表里" | §1.8 与 Theorem E 不一致 | N3 |
| "'cancer'、'reward hacking'、'pseudo-solution' 都是修辞" | §10.4；Prop 27；§8.5 | 机制先行已基本做到；Prop 27 写成映射；伪解给出一般判据（N3、N12） |
| "Ren 是谁？为什么有 129 处 repair？" | 全文 | N10：干净稿 |
| "AI 2040 并没有保留 AI 作为竞赛的工具" | §8.5 第 4 点与 Theorem E(3) | N12：写成条件句，并给出一般检验 |
| "现在的轨迹是军备竞赛？证据在哪里？" | §12 的 "will be documented" | 补三条不点名的公开证据（第 5 节） |
| "q = 0.6 这类数字是随手设的" | Prop 23 的数值 | 这些数字只用于说明阈值的形状；论文图 2 改用由 Lemma M 生成的生存曲线 |
| "Prop 28 的参数是挑出来的" | $L_c=100L_e$ | N11：作为存在性结果，补上一般形式与生存形式 |
| "Turner 等讲的不是社会" | Prop 27 | N3 第 4 点 |
| "冷战就是反例" | §10.7 | 已经化解，这一段应保留 |
| "企业是有限责任，不是生存优先" | §10.1 | 已经化解 |

**是否太长、太重复？** 作为理论文件，3.64 万词可以接受；Ren 明确要求先把理论做完整，再压缩。真正的问题有三个：
- 噪音：repair 括注与版本号（N10）；
- 重复：同一个回答出现在三到六处（N15）；
- 阅读顺序倒置（N9）。

这三者都不需要删掉任何结果。处理之后，正文大约减少 10%，冷读的难度会明显下降，压缩成论文时也有了一份可以直接取材的母本。

---

## 7. 10 页版计划（更新）

*前提：AAAI 双栏，10 页。附录不计页数，但审稿人可以不读附录，所以正文必须自足。下面按约 8.9 页正文做预算，为参考文献留出余地。截稿时间：2026 年 10 月 5 日 AOE。*

### 7.1 标题

**推荐：** "Survival Is Shared: Why Rivals Developing Decisive AI Must Cooperate"

**备选：**
- "Faster Than Understanding: Survival, Prediction and Cooperation among Rivals Developing Advanced AI"。它把 Lemma M 的机制放进标题，符合"机制先于结论"。
- "What Every Actor Needs to Go On: Survival and the Exits from an AI Arms Race"。它与末句呼应，是肯定式。
- 保留 "No Winning Position"：只有在副标题当场给出定义时才可以，例如 "No Winning Position: Why No Branch of an AI Arms Race Secures Survival"。但它仍是否定式；而且 N1 修复之后，"no branch" 需要加限定。

理由与上一轮相同：标题应当是肯定的，命名实际证明的东西，并且不用"赢"的语法。

### 7.2 摘要（199 词）

> Many plans for advanced AI keep the contest between rivals, build capability at the pace the contest sets, and seek safety through a lead, verification, deterrence and control of their systems. We examine this position in terms of survival, the one requirement every actor shares: to go on deciding its own course. Three premises carry the analysis. In the race capability compounds, as the racers hold; correction that people can understand and dispute grows more slowly; and some behaviour beyond such correction can do irreversible harm. From these we derive what earlier analyses assumed. Correction beyond understanding is either absent or delegated to systems the contest selects, which do not carry the actors' shared stake; once any actor delegates, every other actor must choose between lock-in and subordination. No branch of a continued race secures survival for an actor that keeps racing, and survival-first actors who share this prediction need little prior trust to cooperate. Verification must approach perfection as the value of winning grows, so an agreement that keeps the contest underneath only postpones. Long-run survival requires ending the contest by agreement or keeping AI out of it for everyone, with development held to the tempo of understanding.

*注：*
- *"once any actor delegates…" 需要 N2 的"两个零"命题。若来不及，改为 "and competitive pressure forces decisions onto them"，并在正文写明 DC。*
- *"for an actor that keeps racing" 是 N1 修复后的诚实措辞，不要删去。*

### 7.3 主梁一段（正文第 1 节的核心段落）

> Survival is every actor's minimum. In an arms race for decisive AI, capability compounds while the correction people can understand and dispute does not. What lies beyond that correction is either uncorrected or corrected by systems the contest has selected, and neither carries what the actors share. Once any actor hands the contest's decisions to such systems, every other actor is left between lock-in and subordination. Along the continued race, no branch secures survival for an actor that keeps racing, and the logic that never reaches enough destroys its own bearer as well as its host. For survival-first actors who share this prediction, cooperation needs little prior trust, so the transition begins as a change of prediction. Verification cannot replace that prediction while winning appears to pay. Until cooperation is reached, AI is kept out of the contest, development stays within understanding, and decisive capability waits for the conditions to govern it.

### 7.4 图

- **图 1：反驳树。** 即 §8.4 的树，加上 N1 的 Q4′。根节点是 (K)(A)(S)，每片叶子要么是让步，要么是出口。可以用 TikZ 画；为了省时间，也可以用一个紧凑的两栏表格代替。
- **图 2：生存曲线。** 横轴是地平线 $H$，纵轴是 $\Phi$。画三条线：
  - 持续的竞赛（Lemma M）；
  - E3，加上一个正的残余危险；
  - "冲刺后停下"的赢家（N1）。

  图中标出 $\varpi^\ast_\Phi<1/2$ 的地平线。改写 `checks_v44.py` 中的 `run_mismatch` 即可，大约需要一小时。

### 7.5 章节与页数预算

| 节 | 内容 | 页 |
|---|---|---|
| 1 Introduction | 中性地陈述立场 (K)(A)(S)；生存是最低需求；主梁一段；五条贡献；认识论（条件尽量取竞赛者自己的前提，并预先列出反驳） | 0.9 |
| 2 Related work | AI 竞赛模型（Armstrong 等；Han 等；Stafford 等）；竞赛理论与全付极限；承诺问题与预防性战争；保证博弈与验证；核革命与冷战；pacing problem 与必要多样性；结构性风险与渐进失权；俘获（v3 的二阶层） | 0.5 |
| 3 Model | 行动者，CSF，P1–P3；三种度量（目标、物质、生存 $\Phi(H)$）；(X1)(X2)(U)(φ)；用一个框列出连接假设（L3、作为被选择结果的 L4、L5、L6）；Lemma 0 一行；自我模型的边界错误，即 Prop 3(1)–(2)，0.2 页（这是 Ren 明确要求的 non-dual 一点） | 1.1 |
| 4 Mechanisms of the contest | 加入与耗散（Prop 4(1)、(3)；Prop 5 一行）；被迫委托与锁定（Prop 6(5)、Lemma 1、Lemma D）；节奏界（Prop 7(1)、(3)、(4)）；预防性攻击（Prop 8(2)、(4)） | 1.5 |
| 5 What the arms race does to survival | Lemma M（含"极限很便宜"的说明）；Prop 26（含递归论证）；Prop 27（压缩，含 Prop 3(4) 第二条）；两个零；Prop 23；Theorem S（分两类赢家）；Corollary 2；图 2 | 1.8 |
| 6 Trust and verification | Prop 13 的紧凑版；Theorem B；三种信任，一句；伪解的一般判据；AI 2040 作为一个例子，三到四句 | 0.8 |
| 7 Keep the contest, accelerate, be safe | Prop 29；Prop 25 的表；Prop 28（含生存形式）；Corollary 3；图 1 | 1.0 |
| 8 Exits | Lemma E0；Theorem E（含 (1)、(2)）；E1a/E1b，E2（定义为超出理解的能力类别），E3；次序（优先）与可行性；Prop 24，一句；冷战，一段 | 0.7 |
| 9 Conditions and refutation | 一张表：(X2)、(U)、(φ)、L4/P3、L6、Lemma D、A8、$\bar h_R$，以及各自的反驳观测 | 0.4 |
| 10 Conclusion | 末句 | 0.2 |
| 合计 | | 8.9（含两张图；超页时先压缩第 2、6 节） |

### 7.6 正文与附录的分配

| 结果 | 位置 |
|---|---|
| Prop 3(1)–(2)、Prop 4(1)(3)、Prop 5（一行）、Prop 6(5)、Lemma 1、Lemma D、Prop 7(1)(3)(4)、Prop 8(2)(4)、Lemma M、Prop 26、Prop 27（压缩）、两个零、Prop 23、Theorem S、Corollary 2、Prop 13、Theorem B、Prop 29、Prop 28、Corollary 3、Lemma E0、Theorem E | 正文 |
| Prop 25 | 正文，以表格形式 |
| Props 14、15，Corollary 1，Prop 24 | 正文各一句，证明放附录 |
| 宿主模型；Props 1–2、Theorem 1、Theorem 2；Props 9–12、16、19–21（慢路线、纠错者被选择、静默越线） | 附录 B："The slow route and the selected corrector"。正文只在 Prop 26、27 中各用一句：速率律 $g/(1+\eta)$；控制权在最大者中被选择 |
| Props 17、18、22，Definition 3，Proposition C | 附录 C："What cooperation must contain" |
| §6.3 的补救措施表（带出口一栏） | 附录 D。这张表对政策读者最有用 |
| 对 Plan A 的完整读法；冷战的完整对照 | 附录 E |
| 数值与脚本 | 附录 F，加补充材料 |

**不进论文的内容：**
- 版本历史、repair 括注、中文概要、mermaid 图；
- Ren 与 Claude 的署名、文件路径，以及 "09-28 paper" 之类的内部指称；
- §12 中关于在位者立场的预测，以及结构可恢复性；
- §10.8 中树的意象，最多在结论里留一句。

### 7.7 现实的最小计划（截稿 10 月 5 日 AOE）

**先确认两个硬约束：**
- **OpenReview 账号。** IASEAI 提示审批"可能需要两周"。如果 Ren 还没有账号，这就是决定性的约束，其他一切都以它为前提。
- **摘要注册日期。** 查看征稿说明里是否有更早的摘要注册日期。题目、摘要和作者在截稿时冻结。

**第 0 步（Ren，约 30 分钟）：** 需要 Ren 决定四件事：
- 标题；
- 是否采用方案 A：主梁进正文，v3 的慢路线进附录；
- E3 的地位，即"always"；
- 是否接受 N1 的诚实措辞："for an actor that keeps racing"，赢后停下的赢家作为困难情形。

**第 1 步（约 3 小时）：** 直接在论文文本中修复 N1、N2、N3 和 N7，不必先回写 THEORY.md。
- N1：只需改写 Theorem S(1) 的一段，并加入 T 分支的均衡论证。
- N2：若写不完整，就用 Theorem E(2) 的 DC 版本，加脚注说明它与 L6 的关系。
- N3：只是措辞，再加上 P3。
- N7：删去第一条理由。

**第 2 步（6–8 小时）：** 以 `v3/main.tex` 为骨架。它的序言、参考文献、相关工作和模型节都已匿名、已核实，直接沿用；重写第 4–9 节。图 1 可以先用表格代替；图 2 用 `run_mismatch` 生成。

**第 3 步（约 2 小时）：** 附录。
- 证明直接取自 THEORY.md 的附录 A，以及 v3.1 的附录；
- 三个检查脚本作为补充材料；
- 匿名化。

**第 4 步（约 2 小时）：** 核实正文中出现的 † 文献，约 20 条。优先核实这些：
- Fearon 1995、Powell 2006；
- Hillman 与 Riley 1989、Baye、Kovenock 与 de Vries 1996；
- Crawford 与 Sobel 1982、Skogestad 与 Postlethwaite 2005；
- Ashby 1956、Marchant 等 2011、Homer-Dixon 2000；
- Jervis 1989、Sagan 1993；
- Omohundro 2008、Turner 等 2021；
- Stafford、Trager 与 Dafoe 2022（同时确定采用哪一种描述）；
- Larsen 等 2026 的作者名单。

**第 5 步（约 1 小时）：** 调整页数，写贡献声明，上传。若还有时间，做一次单人冷读，把论证与数学合在一个人身上。按 Ren 的成本规则，这一步要先问过 Ren 再运行。

**退路（如果只剩不到一天）：** 在 v3.1 "No Viable Race" 的基础上，用一个约 2 页的新节 "Survival and the exits" 替换其第 7–8 节的部分内容。新节包含：
- Lemma M；
- Prop 26；
- Theorem S（诚实版）；
- Theorem B，一段；
- Theorem E(2) 与出口。

这样可以保住 v3.1 已核实的约 100 条文献和已经调好的版面。不建议退回 v2 "Selecting the Selectors"：它虽然可以直接提交，但不是 Ren 说的"证明世界必须合作"。

---

## 8. 应当保留的

- **用三个前提代替三个极限。** (X)(U)(φ) 加 Lemma M，是本版最重要的进步。它把立场方的反驳变成了一个举证责任问题："你否定哪一个前提？"其中两个前提是对方自己的。
- **Prop 26 的二难：超出理解的纠错，要么缺席，要么就是委托。** 加上递归论证之后，它就是对"用 AI 让 AI 安全"最干净的回答。
- **Lemma D。** 修好证明之后，它是全文把"自主"从定义变成机制的关键一环，也是"两个零"的基础。
- **P2 二难。** 修好分支 II 的措辞之后，它是全文最好记、也最难反驳的一句。
- **"Why the conditions hold today"的六点。** 尤其是第 3 点（可控性二难）和第 4 点（"没有任何前沿行动者公布过可核实的、对决定性优势用途的限度"，这一点可以检验）。
- **§8 的重建：**
  - 以"领先换安全裕度"为主形式；
  - (S) 是结果；
  - (A) 不再包含 H3；
  - 用树来组织；
  - "every leaf is a concession or an exit"。
- **Prop 28 的风险补偿。** 写成一般形式、并加上生存形式之后，它是对"对齐会随规模解决"最公平、也最锋利的回答。
- **Theorem E(2) 的长期必要性，以及 E1a/E1b 的拆分。** 后者完整表达了 Ren 的两半：AI 不以斗争的方式存在，也不作为斗争的工具。范围与 9 月 26 日的裁定一致。
- **Lemma E0 的量词修复，以及 §10.6 的末句** "holds exactly as far as Theorem E's conditions do"。
- **§10.7 的核武器对照。** 四点差异，以及"冷战中，对手靠阻止决定性优势，同时保住了对抗与安全，这就是 E2"。这一段把最直接的反例变成了证据。
- **Prop 22 在一致的 n 人博弈中的诚实重算：**
  - 它是协调博弈，不是合作占优；
  - $n=2$ 时连全合作均衡也没有；
  - "盖子随压力长"只需要 $R\ge T$。
- **Prop 6(5)–(6) 的精确条件与两个方向的反例**，以及让 `checks_v44.py` 重现每一位评审的反例的做法。
- **§10.4 的单一定义与两类型结果**，以及撤回免疫化的那一段。
- **§0 认识论段的肯定式开头。** 它不再以 Ren 说"不同意"的那种句子开头。
- **末句：** "What has to be agreed is not who comes first, but what every actor needs in order to go on."
- **全文没有点名任何国家或公司。**
