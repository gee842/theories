# THEORY v4.3 评审：AI 安全与治理从业研究者视角

审查对象：`v4/THEORY.md`，"No Winning Position: the integrated theory (v4.3)"，1851 行，约 2.8 万词。全文已通读。为避免重复，先读了 `reviews/R-v4.1-external-gpt.md`。

评审立场：IASEAI 程序委员会成员，熟悉技术对齐、控制与评估文献，熟悉前沿安全框架和 if-then 承诺、算力治理与硬件验证、AI 情景预测（AI 2027、AI 2040）、"Superintelligence Strategy"/MAIM、结构性风险与 gradual disempowerment，也熟悉"必须竞赛，而且能把竞赛做安全"一派的论证。下文尽量替对方给出最强论证，再判断本文是否答上了。

**核查范围。** 本轮有网络访问。2026-10-03 读了 ai-2040.com 的以下页面：首页、summary、FAQ、How Plan A solves our 5 biggest problems、Plan A Assumptions、Comparing Possible Plans、Deal Decline、Verification Plan、Covert AI Projects、Capability Scaling Strategy、Compute in Plan A。还读了 Anthropic RSP v3.0 原文 PDF 的相关段落，并通过检索核对了 OpenAI Preparedness Framework v2 和 Google DeepMind FSF v2 的相关条款。AI 2040 各页是经抓取工具的摘要读到的，所以下文凡是引作原话的句子，投稿前都应再对原页核一遍。§8.4 引用的 "without relying on trust" 一语，在我抓到的页面里没有找到，可能在主叙事或 PDF 中，请核对。

文中 S6 的风险补偿数值，是我在本文 Proposition 6 的模型里独立算出来的，不在仓库的检查脚本中。

---

## 1. 总体判断

**这一版做对了什么。** v4.3 确实修复了 v4.1 评审指出的大部分具体错误：
- Theorem B 改成了条件形式；
- Proposition 6(5) 承认失控成本占优时不会委托；
- Proposition 8 写明了谈判协议；
- §8.4 改成"补充性阅读"。

整套写法很诚实：有分层、有连接假设、预先写明了什么证据能推翻它、每处修复都留了标记。这在这个领域并不常见，评审会认可。

**IASEAI 结论：当前版本拒稿（weak reject 到 reject）。** 理由有五条，按分量排序。

1. **核心论断没有击败对手，只是假设了对手错。** 这是最主要的一条。Section 8 的"斗争、加速、安全，最多得其二"（Corollary 3）是 Theorem E 的重述。Theorem E 的前提是：
   - 被迫委托概率 $q_{\mathrm I}\to1$；
   - 纠错被甩开的概率 $q_{\mathrm{II}}\to1$；
   - 决定性结局概率 $p_{\text{dec}}\to1$，再加上 L4 和 L6。

   "竞赛并且能安全"一派的立场，恰恰是否认这几个极限：对齐与控制能扩展，所以 $q_{\mathrm I}$、$q_{\mathrm{II}}$ 小；威慑或防御占优，所以 $q_W$ 小；"我方"赢家有止境，所以 L4 对我方不成立。对方可以接受论文的每一条定理，同时否认其前提。而且 (A) 的定义里直接含有 H3（"发展快过纠错"），"(A) 排斥 (S)" 因此接近同义反复（S1）。
2. **对两个最重要对手的刻画，相关社群会认为失真。**
   - AI 2040 Plan A 更接近本文自己的 E0+E3，被归为 (K)(A)(S) 立场"最完整的版本"（S2）。
   - MAIM 是用威慑阻止决定性冲刺，按本文自己的 Theorem E 属于 E2 式出口，却被按"预防性战争"建模并判为"None"（S3）。

   这两个社群的人很可能就坐在 PC 里。
3. **本文自己的出口要用到它批评的工具，自我适用没有做。**
   - E0 和 E2 都需要对不信服者执行，执行靠的正是验证和威慑。
   - "先改变预测，后有信任"（Corollary 2）被本文自己的 Proposition 14（廉价话语）和 Proposition 4(4)（竞赛由最激进者开启）削弱（S4）。
4. **最接近的已有和同期工作几乎没有引用。** 包括：
   - Katzke & Futerman 2024 "The Manhattan Trap"；
   - Roussel et al. 2026（Aguirre 为作者之一）关于自利导向暂停的博弈论证；
   - Fudenberg & Koh 2026 "Cooperating against Catastrophe"；
   - Han et al. 的 AI race 演化博弈系列；
   - Askell, Brundage & Hadfield 2019；
   - Stafford, Trager & Dafoe 2022；
   - Kulveit et al. 2025 Gradual Disempowerment；
   - MIRI TGT 2025。

   没有这些，Theorem S 看起来像重新发现（S10）。
5. **体裁不合。** 28k 词、25 个以上命题，不是会议论文。还有若干措辞会被读成修辞压倒论证，例如 "cancerous objective"、"dead end for humanity"、"In today's world reason says clearly"。其中一处会让 L6 不可证伪（S11）。

**什么能让它进入 accept 区间。** 压缩成 8 到 10 页的一篇，以本文真正新的部分为骨架：
- 二阶选择与所需独立纠错速率（Proposition 9–11）；
- 掩蔽与保守报警（Section 5）；
- 时滞稳健性界（Proposition 7(3)）。

用这三样去回答"竞赛并且安全"的立场。同时公平地重述 Plan A 与 MAIM，并与上列文献明确定位。

**最重要的一处修改。** 把 Section 8 和 Section 10 从"在极限假设下不可能"改写成"在 (K) 与 (A) 下，安全无法从竞赛内部被证明"。具体有四步：
1. 写出竞赛路线若要安全必须满足的定量条件。至少包括：检测比"背叛到决定性"更快；端到端纠错时滞小于能力倍增时间，并留出稳健裕度；独立纠错增长率不低于 $g/(1+\eta)$；评估者全行和小于 1。
2. 用比较静态（而不是极限）证明，每一条都被 (K) 或 (A) 推向坏的方向。这一点 Proposition 25 已经部分做到。
3. 证明这些条件所需的证据在竞赛内部形成，因而受掩蔽、捕获、廉价话语和时滞约束（Section 4、5、7.2、3.4），对方无法用自己认可的标准证成。这个标准就是 safety case 和 "strong argument that catastrophic risk is contained"，后者是 RSP v3 自己的措辞。
4. 把 Theorem S 降为这个命题在极限下的推论。

这样，对方即使不接受 $q\to1$，也必须面对举证责任。这才是 Ren 想要的、谨慎的知识分子"无法简单驳倒"的形式。

---

## 2. 问题清单（按严重度排序）

严重度分四级：致命 / 重大 / 中等 / 次要。

### S1【致命】Corollary 3 靠假设对方前提为假取胜；"三选二"有一部分是定义出来的

**位置：** §8.3 Corollary 3 及附录 A 中它的证明；§10.4 Theorem E；§0、§14 的总结句。

**问题与论证。**

1. **前提就是争点。** Corollary 3(1) 就是 Theorem E。Theorem E 的证明依次用到：
   - 条件 D 加 L5 推出 $q_{\mathrm I}\to1$；
   - H2 加 L4 推出 $p_{\text{dec}},p^S_{\text{dec}}\to1$；
   - H3 加 L1 加 Proposition 7 推出 $q_{\mathrm{II}}\to1$。

   竞赛并且安全一派的立场，正是否认这些极限：
   - 对齐与控制随 AI 扩展，所以 $\Delta\psi$ 和 $q_{\mathrm{II}}$ 下降；
   - 威慑或防御使 $q_W$ 小；
   - 我方赢家受约束，所以 L4 对我方不成立。

   定理是对的，但它回答的是"如果你错了会怎样"，不是"你为什么错了"。
2. **(A) 的定义里含有 H3。** H3 是"发展快过某类危害的纠错"（$a\tau_c$ 超出稳健纠错范围）。既然如此，由 Proposition 7，"(A) 排斥 (S)" 几乎是分析性的。对方说的"加速"不是"快过纠错"，他们声称纠错也在用 AI 加速。把争点写进对方立场的定义，PC 一眼就会看出来。
3. **三个角并不独立。**
   - Corollary 3(3) 自己承认，即使放弃 (K)，"development must still stay within the tempo of correction"。也就是说，(A) 中的 H3 在 (A)+(S) 这个角里同样被放弃了。
   - Corollary 3(2) 的 (K)+(S) 要靠 E2 或 E3。但在 (K) 下，单方减速不是最优反应（Proposition 4），所以 E2 或 E3 只能联合实施。联合减速本身就是合作，是对 (K) 的部分否定。
4. **证明里有一句与 §6.3 表格矛盾。** 附录 A 写道："No instrument of Theorem B or Proposition 25 negates any of H0–H3"。可是 §6.3 表把"verified agreement among rivals"标为 "E0 in part"。而一个有效的 MAIM 会否定 H2（见 S3）。

**真正的实质内容**其实是两条：
- (i) 在 (K) 下，节奏由竞赛决定（L1 加 Proposition 4），要把节奏压到纠错速度以下必须有协议；
- (ii) H3 推出 ¬(S)（Proposition 7）。

"竞赛并且安全"一派真正与众不同的主张，是"无需对手合作、在竞赛内部就能实现安全"。所以最锋利的命题不是"三选二"，而是"(K) 下不存在单边或竞赛内的安全"。

**修复。**
- **(a)** 把 Corollary 3 重述为："在 (K) 下，安全需要关于节奏或关于工具的协议；不存在单边安全。"保留"三选二"作为通俗口号，但正文不要称之为三难定理。
- **(b)** 用比较静态取代极限。每个工具成功的概率都随赢的价值 $T$、节奏 $a$、控制成本下降率 $g$ 单调下降。生存概率是这些工具同时成功的乘积，因此在 (K)(A) 下单调下降。这不需要任何 $q\to1$。
- **(c)** 用"危险期"（time of perils）的结构重写 Theorem S。累计生存概率为正，当且仅当风险率可和，即 $\int\psi(t)\,dt<\infty$。乐观派实际上主张"短暂高危期之后进入安全态"（参见 Ord 2020；Thorstad 关于 time of perils 的批评）。本文的机制正好可以论证：在 (K)(A) 下，$\psi$ 不会以可和的速度下降。理由有三：Proposition 6 中委托随 $s$ 增长；Proposition 7(3) 中稳健性按 $e^{-a\tau}$ 衰减；Proposition 11 中纠错被捕获。这比"$q\to1$"强，也更公平。
- **(d)** 加入第 1 节所述的"不可证成"命题。

### S2【重大，接近致命】§8.4 对 AI 2040 Plan A 的定位与若干细节不准确；真正的 (K)(A)(S) 范例没有处理

**位置：** §8 开头（"in which AI 2040: Plan A is the most complete version"）；§8.4 第 916–929 行；§6.3 表 "Verified agreement" 一行。

**与原文核对的结果。**

**准确的部分：**
- 验证尚不成熟；
- 立即高置信度地核查暂停大概需要关停数据中心；
- 协议解体时摧毁算力、晶圆厂与机器人，各方保留 2% 的加固储备，并以制裁、网络攻击乃至军事回应作为威胁；
- 若不摧毁算力，解体后约一周到 ASI；若摧毁，约一年；
- 协议衰退（解体或受损）在其情景中的累计估计约为一半。Deal Decline 页给的是作者之一的估计，约 48%，大致在解体与受损之间各半；
- 对政府行动有意采取乐观设定；
- "If high AI takeover risk becomes common knowledge... relying on trust may be the best option"。
- 关于"最难的部分"：Verification Plan 说的是 research titration，即决定研发该以什么速度推进。§8.4 写成"workload approval, safety cases and research titration"，应收窄为 titration。

**不准确或不公平的部分：**
- **"keeps (K)"。** Plan A 明确声称要消除 superintelligence race 的 "winner take all" dynamic（"5 biggest problems"页的 Problem 3）。它的原则包括：many companies in many countries at the frontier、model parity、total research transparency、Citizens Dividend。开源权重被限定在协议前的能力水平。这些恰恰是本文 Corollary 1 所说"唯一能同时放松所有约束的杠杆"，即降低赢的价值。§8.4 结尾承认它们 load-bearing，但开头又把 Plan A 归为保留 (K) 的立场。两处不一致。
- **"keeps a form of (A)... drives a large expansion of compute (Prop. 25(3))"。** Compute supplement 把算力增长（2028 年末约 2.9 亿 H100e，到 2040 年约 1 万亿）归因于经济价值，并用 cap-and-trade（2032 年起）和硬件研发限速约束它，不是归因于"保持领先"。"保持领先"确实存在于 Covert AI Projects 页：合法联合体对秘密项目的算力优势从约 20 倍扩大到 2035 年约 4.3 个数量级。但实现方式是供应链核算和限制秘密项目的算力获取，是结构性的；不是 Proposition 22 那种双方自由选择努力程度的赛跑（见 S15）。
- **"the pace is set by the follower's threat"。** 这句只对了一半。Capability Scaling Strategy 写的是 "scale as quickly as possible subject to maintaining high confidence that the scaling is safe"。如果对秘密项目的探测更悲观，就应放慢软件进步，以免泄露给秘密项目。
- **"the most complete version of the position"。** Plan A 的作者在 Comparing Possible Plans 中明确判定：竞赛（Plan D）和对对手的破坏（Plan B）都劣于协议。把他们归入"保持斗争"的立场，会被读成稻草人。

**§8.4 漏掉了更有力、也更准确的批评。**
1. **节奏的一部分由协议衰退风险决定。** Scaling Strategy 写明，延长时间线会提高解体或受损风险，因此在安全界限内更快扩展更可取。交接决策直接拿"对齐置信度"去换"衰退风险"，例如在 95% 置信度且年衰退风险超过约 5% 时就交接。这正是本文 Proposition 15 的论点：赢的价值被保留时，竞赛动机以时钟的形式进入协议，节奏不再只由纠错决定。
2. **终点是约 2040 年向 AI 交接。** "Hand off once we have high confidence that the AIs are aligned"。在本文的语言里，这是在时间压力下、在不到 100% 的置信度下，有计划地穿过不可回头点一。
3. **Plan A 保留 H2。** 它先快速扩展到 TED-AI（约 2035 年），再近乎暂停。所以它否定的是 H3（靠 titration），没有否定 H2。按 Theorem E，否定一个假设只是必要条件，不是充分条件。
4. **Plan A 自己有 E2 作后备。** Plan S，即无限期停止，是发现秘密项目或对齐"极难"时的后备。它拒绝把 Plan S 作为主方案的主要理由，是停止期间对齐进展更慢。本文必须正面回应这一论点（见 S7 中关于 E2 的部分）。
5. **验证本身依赖 AI。** Verification Plan 写到 AI-assisted checks 和 trusted AI monitoring。于是"无需信任"把信任从对手的意图搬到了验证 AI 的对齐上（见 S9）。

**还有一处与本文自己矛盾。** 按本文 Corollary 3(2)，"保留部分竞赛、联合减速、追求安全"正是允许的 (K)+(S) 角。Plan A 按其意图正在这个角里。所以本文不能说 Plan A 违反"三选二"。只能说：它否定 H3 的方式（titration）是它自己承认的最弱环节；它保留了 H2；它的执行层保留了相对地位（Proposition 15(3)、Proposition 21）。

**真正的 (K)(A)(S) 范例没有被正面处理。** 这些包括：
- "领先者用领先换取安全裕度"（a lead buys a safety margin）：Aschenbrenner 2024；AI 2027 的 slowdown 结局，即领先方短暂放慢、修好对齐、然后胜出并主导之后的安排；Amodei 2024 的 entente strategy；
- MAIM 的 competitiveness 支柱；
- 前沿安全框架中"以竞争者为条件"的条款（见 S13）。

**修复。**
- 把 Plan A 重新定位为："E0（部分、双边、以透明为核心）+ E3（titration）、保留 H2、执行层残留 (K)"。逐条与本文对接：Corollary 1 是一致点；Proposition 15(3) 和 21 是执行层的残留；衰退风险推动的节奏是 Proposition 15；交接是不可回头点一。
- 以"a lead buys a safety margin"作为 (K)(A)(S) 的主范例，正面回应（见 §3 表第 1 行）。
- Ren 的"不点名"裁定可以保留在正文，但参考文献应当列出具体文件。否则 "Many current plans share one position" 是无出处的断言。§12 K1 写 "needs no elaboration and will be documented in revision"，评审不会接受。

### S3【重大】MAIM/威慑被建模成预防性战争；按本文自己的 Theorem E，一个有效的 MAIM 是 E2 式出口

**位置：** §3.5 Proposition 8 及其后讨论；Proposition 25(1)；§6.3 表 "Deterrence by threatened sabotage" 一行（Exit 栏为 "None"）；§13 的 deterrence 条目。

**问题。**
- Proposition 8 把实力转移当作外生，把行动当作结束谈判的战争。MAIM（Hendrycks, Schmidt & Wang 2025）的逻辑是威慑式拒止：破坏性回应便宜且可信，所以领先者不会发起决定性冲刺，转移根本不发生。破坏是有限行动，之后现状恢复、谈判继续，不存在 Fearon/Powell 那种转移后的承诺问题。
- 本文的"威胁降低 $c_A$，使预防条件更容易满足"，对 MAIM 支持者来说是正中下怀：便宜的破坏正是要让冲刺无利可图。
- 按 Theorem E，否定 H2 就是出口。一个起作用的 MAIM 正是以威慑强制执行 E2。表中填 "None"，与本文自己的框架不一致。

**本文其实有更好的回应，只是没有用上。**
1. **可观测性与可区分性。** 决定性冲刺与正常进展在可观测量上难以区分。这是 Jervis 1978 意义上的攻守不可区分。自动化 AI 研发可以在数据中心内部、在算法层面推进。这正是 Theorem B(2) 的及时性论证，也是 MAIM 批评者的核心论点：Abecassis 2025, "Refining MAIM"（MIRI）认为，"可接受用途"与"决定性优势"之间的 breakout 距离极短，所需的监测保真度与反应速度实际上无法达到；另见 AI Frontiers 2025 "Superintelligence Deterrence Has an Observability Problem"。
2. **不可验证的指控。** 敌对状态下，"对方在冲刺"的判断是廉价话语（Proposition 14）。误判会触发 Proposition 8 的螺旋。
3. **MAIM 的 competitiveness 支柱肯定 H1**，鼓励把 AI 纳入军事与国家能力，正好加速 Proposition 6 的被迫委托。

所以 MAIM 的问题不是"它保留了竞赛"，而是"它试图用威慑实施 E2，但在 P2 之下拿不到实施 E2 所需的及时观测，同时它的另一支柱加强了 H1"。

**修复。**
- 加一个"领先者选择是否冲刺"的模型：威慑成立当且仅当 冲刺收益 < 被及时发现的概率 × 被破坏的损失。由此自然得到与 Theorem B 相同的及时性条件。
- §6.3 表的 Exit 栏改为："在可观测、可区分的前提下是 E2 的一种执行方式；在 P2 下这一前提失效；其 competitiveness 支柱强化 H1。"

### S4【重大】本文的出口需要它所批评的工具；"先改变预测"被自己的 Proposition 14 和 4(4) 削弱；"无合作时的出口"缺部分联盟模型

**位置：** §10.2 Corollary 2；§10.4 Theorem E 的顺序部分与 Proposition 24；§13 "A pause hands the advantage..." 条目；Definition 3(d)–(f)。

**问题。**
1. **执行的自我适用（tu quoque）。** 只要有一个不信服 Theorem S 的有能力行动者，竞赛就会重启（Proposition 4(4)：竞赛由最激进者决定）。所以 E0 和 E2 都要求对不信服者执行。执行靠的是验证和威慑。于是 Theorem B 与 Proposition 25 同样适用于本文自己的方案。本文目前只说"降低赢的价值后，所需的验证会变少"（Theorem B(4)）。但这只对已经信服的行动者成立。
2. **Corollary 2 与 Proposition 14 冲突。** "预测成为共识"要求行动者相信对方真的相信这个预测。在敌对状态下，"我认为竞赛是自杀"是带偏差的廉价话语：有动机让对方松懈，自己加速。按 Proposition 14，这种话不能完全可信。要建立共同知识，需要代价高昂的信号（Kydd 2005），也就是又回到了信任与验证。"过渡首先是预测的改变，而不是信任的改变"因此言过其实。
3. **产生预测的机构本身是一个纠错者。** 共同预测需要一个可信的认知来源，类似 IPCC 或 International AI Safety Report。按 Section 4，它的资金、人员和数据也会被所评估的场选择。本文没有把 Section 4 用到这个"预测机构"上。
4. **"在合作不可得时依次采取出口"缺少行动者结构。** 若 E2 或 E3 单方实施，在目标意义上被 Proposition 4 支配。若联合实施，那就是 E0。Proposition 24 自己也承认，当 $p^S_{\text{dec}}\gg p_{\text{dec}}$ 时条件不成立。Section 13 说"不提议在前沿竞赛中单方克制"，而合作不可得时的 E2 恰恰只能是单方或部分联盟的。这两处在逻辑上有张力。

**修复。**
- **异质信念版本的 Theorem B。** 所需检测率 $\upsilon$ 由信服度分布的上尾决定，即 $\max_i$ 感知 $T_i$，或由联盟覆盖率决定。本文的方案因此可以表述为：用共同理解压缩这个分布，让执行只需处理一条尾巴。而"竞赛并且安全"立场使整个分布保持在高位。这个区别足以回答 tu quoque，又不需要否认执行的必要。
- **部分联盟（minilateral/club）模型。** 控制芯片供应链的联盟可以对外实施 E2，参见 Nordhaus 2015 climate clubs；Barrett 关于条约参与的模型；Plan A 的 compute accounting。需要说明联盟覆盖率达到多少时，E1+E2 是自我执行的。
- **对产生预测的机构施加 I2/I3。**

### S5【重大】三处混同：AI 辅助纠错与委托决策；委托锁定与丧失自主；"control"一词

**位置：** Proposition 7(5) 第 463 行；Lemma 1；§10.1 的 "Survival includes autonomy"；Theorem E 证明中的 $q_{\mathrm I}\to1$；§4.1 的 "control over correctors"；§6.3 表 "Operator alignment, scalable oversight, AI control" 一行。

1. **AI 辅助纠错不等于委托竞赛决策。** 第 463 行写 "If the faster correction is supplied by the contest's own systems, that is Proposition 6"。但 Proposition 6 讲的是把战略、军事、经济决策交给 AI 而不经人工审查。AI control 协议（Greenblatt et al. 2024）的结构则是：可信的较弱模型监控不可信的强模型，人工审计其中一部分。这是用 AI 缩短纠错时滞，不是交出竞赛决策。两者的风险结构不同。

   对 AI 辅助纠错，正确的连接是两处：
   - Section 4：纠错工具由所评估的场供给，存在捕获风险；
   - control 文献自己承认的边界：只有在"可信模型"与"不可信模型"的能力差可控时，control 才有效。

   在 (A) 下，这个能力差扩大得更快，所以 control 的适用窗口被更快穿过。这个回应会被 control 社群接受，因为是他们自己的假设。
2. **委托锁定不等于丧失自主。** Lemma 1 说的是人类独立完成被委托决策的能力在衰退。§10.1 和 Theorem E 却把它当作"把决策交给无法推翻的系统"。失去亲自做的能力，不等于失去推翻或改向的能力。今天的空管离不开计算机，但仍受控。$q_{\mathrm I}\to1$ 需要两条机制之一：
   - 被委托系统未对齐，即每期风险 $\psi_1$ 在整个时域上累积；
   - 推翻在竞争中不可行：推翻就是克制，按 Proposition 4 被支配。这正是 gradual disempowerment 的机制（Kulveit et al. 2025；Critch 2021 RAAPs）。

   本文应当明确写出这两条，并引用它们。
3. **"control" 一词撞车。** Section 4 的 "control over correctors"（对纠错者的影响力或捕获能力），与 AI 安全里的 "AI control" 是完全不同的东西。§6.3 表把 "AI control" 和 "capability cheapens control (Prop. 11)" 放在同一格，AI 安全读者会读错。建议全文改为 "influence over correctors" 或 "capture capacity"。

### S6【重大】对"对齐和控制会扩展"这一最强论点，本文没用上自己模型里最锋利的回答：风险补偿

**位置：** Proposition 25(2)；§13 "Technical alignment will be solved in time"。

**论证。** Proposition 6 的条件 D 是 $L_e/n>L_c\Delta\psi$。对齐或控制进步降低 $\Delta\psi$，结果反而让条件 D 更容易成立，委托更早成为占优策略。

我在 Proposition 6 的模型中做了计算，取 $n=3$、$r=1$、$L_e=1$、$L_c=100$、$\psi_0=0.01$，并对纯策略纳什均衡做穷举：

| $\Delta\psi$ | $s$ 较大时的均衡 | 每期"任一方失控"的实现概率 |
|---|---|---|
| 0.19 | 无人委托 | 0.0297 |
| 0.01 | 无人委托 | 0.0297 |
| 0.005 | 两方委托（$s\ge100$） | 0.0395 |
| 0.003 | 全部委托（$s\ge100$） | 0.0385 |
| 0.001 | 全部委托（任意 $s$） | 0.0326 |

"委托变安全"了 38 到 190 倍，实现的风险却上升了 10% 到 33%。在 $\Delta\psi\in[0.001,0.19]$ 的整个区间内，实现风险从未低于"无人委托"的基线；只有当 $\Delta\psi\to0$ 时才回到基线。这是典型的风险补偿或 Peltzman 效应，与 Stafford, Trager & Dafoe 2022 的结论一致：安全改进会被风险补偿抵消，甚至被逆转。

本文 Proposition 3 中也有温和的版本。在 $\theta=0$ 时，总共同损失 $n\ell e$ 对 $\ell$ 的弹性是 $c/(c+\ell)<1$：降低单位共同损失，有一部分被更高的投入抵消。

**修复。** 新增一个命题："在 (K) 下，不完美的对齐进步可以提高实现的失控风险"，附上上面的数值。这是对"alignment will scale"最有力、也最公平的回应：它不否认对齐会进步，而是指出在竞赛中进步被换成了更多委托和更快速度。

同时要写明适用条件：如果对齐进步同时降低 $\psi_0$，或者进步足够彻底（$\Delta\psi\to0$），效应就会减弱。

### S7【重大】出口 E1–E3 在操作上不够明确

**位置：** §10.4 Theorem E 与 "The order"；Definition 3(e)；§14。

**E1（AI 不进入竞赛）。**
- **范围过宽。** "every contest that AI would accelerate (labour, finance, persuasion, conflict)"，这样等于要求 AI 退出市场、广告和政治，既不可行，也不是模型推出来的。L3 只需要"AI 节奏的决策优势增长"。
- **把 AI 作为竞赛对象和 AI 作为竞赛工具混在一起。** "AI does not exist as a contest" 说的是前者，即前沿竞赛本身。H1 说的是后者。在一场竞赛中造出决定性能力（H2），它本身就是这场竞赛的工具，所以 ¬H1∧H2 近乎自相矛盾。E1 必须与 E0 或 E2 同时成立才有意义。"E1 优先"的排序因此需要重新论证。
- **可操作的界线可以从本文自身导出。** 一项 AI 使用不在竞赛之内，若同时满足：
  - (i) 收益非竞争性或共享，或者后果回流到使用者（I1 意义下的责任）；
  - (ii) 在对抗性领域，后果重大的决策保留人工审查，且节奏是对手可观察的人类节奏；
  - (iii) 平行的人类能力维持在 $\mathcal K\ge\mathcal K_{\min}$。
- **现实中已有 E1 的种子**，本文应当引用并作为出口实例：
  - 2024 年两国领导人关于"保持人类对核武器使用决定的控制"的共同表态；
  - 2023 年 Political Declaration on Responsible Military Use of AI and Autonomy；
  - CCW 关于致命性自主武器的讨论；
  - 金融市场的熔断与交易暂停，这是给算法竞赛设节奏上限的先例。

**E2（暂不建造决定性能力）。**
- **"决定性"按效果定义，只能事后知道，而且是相对的。** 同一系统对弱防御者是决定性的，对强防御者则不是。应当用事前阈值来定义：
  - AI R&D 自动化阈值，例如 FSF 的 ML R&D CCL、RSP 的 AI R&D 阈值、Preparedness Framework 的 AI self-improvement 类别；
  - Aguirre 2025 的 autonomy/generality/intelligence 三重交集；
  - 经效率修正的训练算力上限。
- **"social and cognitive conditions for governing them" 没有判据。** 建议定义为 Definition 3 的各要素到位且 E3 检验通过。否则 E2 就是期限不定的停止，正好落入 Plan A 对 Plan S 的批评：停止期间对齐进展更慢。
- **与 Proposition 15 冲突。** 只停前沿训练、不限制算力与算法进步，会让 overhang $\mathcal O$ 增长，按 Proposition 15 抬高净退出收益。所以 E2 必须包括投入端的限制：芯片产量、硬件效率、算法研究的可见性。Plan A 的 cap-and-trade 和硬件研发限速就在做这件事。本文应当把这一点写进 E2，否则 E2 本身会制造协议崩溃的条件。

**E3（慢于纠错）。** 条件 $a(\tau_{\text{obs}}+T_d+T_r)<1$ 写得很清楚，但 $a$ 是"危害不稳定模态的增长率"，没有操作化。建议的落地方式如下。
- **用能力倍增时间作为 $a$ 的代理：** $a\approx\ln2/T_2$，并把这一映射写成 L1 式的连接假设。$T_2$ 可以取危险能力指标的倍增时间，例如 METR 的任务时长在 2019–2025 年约 7 个月倍增一次（Kwa et al. 2025）；或训练算力的趋势（Epoch）。
- **端到端纠错时滞** $L=\tau_{\text{obs}}+T_d+T_r$ 是可以测量的：评估节奏、从能力出现到被发现的时间、决策时间、撤回时间。若要求稳健容忍度不低于 $e^{-1}$，则 $L\le T_2/\ln2$。按 7 个月的倍增时间，端到端时滞应在 10 个月左右以内。立法周期通常以年计。开源权重的 $T_r=\infty$，所以凡是可能越过某危害类阈值的开源发布，都与 E3 不相容。这是一个可检验、会让读者坐直的推论。
- **与前沿安全框架的操作化对接。** 评估节奏（例如每 4 倍有效算力评估一次）、alert threshold 和 buffer 本质上就是 $\tau_{\text{obs}}$ 与能力增长之间的比较。本文在此基础上新增两点：$\tau$ 必须包括社会层面的决策和撤回（$T_d,T_r$）；稳健性按 $e^{-a\tau}$ 衰减。
- **阈值型危害。** 很多危害（例如生物武器能力提升）更像阈值事件，而不是线性不稳定模态。对这类危害，E3 应当表述为"预警信号与越过阈值之间的提前量，大于 $T_d+T_r$"。
- **Proposition 7(4) 的不可缩短时滞。** 对社会层面的危害（说服、劳动、gradual disempowerment），表现窗口以年计，E3 因此要求极慢的节奏。本文应当正面承认这一含义，而不是让读者自己发现。

### S8【重大】§10.6"足够好、分布式、可替换"的供给，以及"决定性与足够"的界线，技术上站不住

**位置：** §10.6；§6.3 表 "Open release" 一行；§13 的 Limitations。

1. **界线不是模型本身的属性。**
   - 后训练增强（scaffolding、工具、agent 化）可以在不重新训练的情况下显著提升能力（Davidson et al. 2023）；
   - 开放权重的安全训练可以被少量微调撤销（Qi et al. 2024；Lermen et al. 2023）；
   - tamper-resistant 方法（Tamirisa et al. 2024）尚不稳健；预训练数据过滤（O'Brien et al. 2025）有希望，但不完整；
   - 蒸馏和合成数据可以把"足够"的系统变成训练"决定性"系统的材料；
   - 许多"足够"的系统可以被编排、聚合。

   最难的地方在 AI 研发能力：一个足以帮助管理现代社会的系统，很可能也足以加速 AI 研发。"systems that stop growing once they meet the need"不是可以工程化保证的属性。
2. **与 E1 和 Lemma 1 有张力。** "autonomous provision of... security and the functions of administration... held by no one"，这正是 AI 安全社群担心的失控形态。"autonomous" 和 "held by no one" 与"保持人类为玩家"、$\mathcal K\ge\mathcal K_{\min}$ 冲突。"可替换"不足以化解这个冲突。
3. **与本文自己的 Proposition 18 冲突。** 应用层"分布式"，而基础模型、芯片和云集中在少数供给者手里。共享的基础模型是共同的入向转换来源，全行和会因此越过 1。小载体低于 Proposition 9 的规模门槛 $p^\ast$，这并不能抵消上游集中。
4. **"像树一样"在 IASEAI 会被读作诗意比喻，而不是论断。** 可以保留为结尾意象，但需要技术规格支撑。

**修复。**
- 把 §10.6 与已有方案对接：Drexler 2019 CAIS；Aguirre 2025 "Keep the Future Human"（关闭通往 AGI 的门，转而建造 Tool AI），这与 E2 加 §10.6 高度重合，必须引用并说明差异；Bengio et al. 2025 的 Scientist AI（非 agentic）；Buterin 的 d/acc。
- 用 Jervis 1978 的"攻守平衡与可区分性"作为"足够与决定"的概念框架：可共享、防御性、可区分的能力降低 $r$；排他、进攻性、不可区分的能力提高 $r$。
- 列出可测量的候选界线：自主程度上限、单系统算力上限、AI R&D 阈值、发布前后的能力上限检验；并诚实标为开放问题。

### S9【重大】Theorem B 把 $T$ 当作外生；算力治理使 $T$ 内生；验证依赖 AI 时，"信任"被转移而不是消除

**位置：** §7.1 Proposition 13；§8.1 Theorem B；§8.2 表 "Verification" 一行。

1. **$T$ 不是外生的。** 算力治理的逻辑（Sastry et al. 2024：可探测、可排他、可量化）是限制背叛的规模，而不只是探测背叛。Plan A 的 FAQ 也这样提问：不是"对方会不会背叛"，而是"能逃避发现的最大背叛有多大、有多坏"。它的估计是秘密项目约占全球算力的 0.5%。在这种情况下，$T$ 被验证约束住了，"$T\to\infty$ 时 $\upsilon_{\min}\to1$"并不适用。
2. **"及时"的时间尺度。** 投入端验证的时间尺度是秘密积累算力所需的时间：晶圆厂、电力、建设，以年计。它不是"背叛开始后到产生决定性效果"的时间。本文 Theorem B(2) 的"窗口很短"只对后者成立。
3. **本文真正有力的论点在这里：投入端的约束会被算法进步侵蚀。** 达到同一能力所需的算力大约每年下降数倍（Ho et al. 2024）。透明的研究还会外溢给秘密项目，Plan A 自己也担心这一点。因此可以写一个与 Proposition 11 同构的速率条件：投入端验证的界限必须以不低于算法效率进步的速度收紧，否则 $T$ 的上界随时间失效。这比"$T\to\infty$"更公平，也更难反驳。
4. **AI 化的验证与承诺。** 包括 AI 测谎（Plan A 的稳定器之一）、trusted AI monitoring、zk 训练证明、程序均衡（Tennenholtz 2004）。这些把信任从"对手的意图"转移到"验证 AI 及其供应链的对齐与完整性"上，而后者正是尚未解决的问题。程序均衡要求可验证的代理真的掌握决策，否则承诺不可信。这就是不经人工推翻的委托，即不可回头点一。本文应当把这一点写进 Theorem B(3)：验证不承载的东西里，还应加上"验证器自身的对齐"。

### S10【重大】新颖性与定位不足

详见第 4 节。要点如下。

**基本不新的部分**（作为构件可以，但必须说明来源）：
- Propositions 1–2：Armstrong, Bostrom & Shulman 2016；Han et al. 2020；
- Proposition 3：Schaffer；
- Proposition 5：Tullock 租耗散；
- Proposition 6：Hendrycks 2023；Horowitz 2019；Scharre 2018 的速度压力；
- Proposition 8：Fearon/Powell；
- Proposition 13：保证博弈；Askell et al. 2019 的五个因素几乎与本文的四个杠杆一一对应；
- Proposition 14：Crawford–Sobel；
- Theorem S：Katzke & Futerman 2024 已经论证，同样的前提蕴含竞赛自我挫败，包括大国冲突、失控、权力集中三条通道，并把 ASI 定性为 trust dilemma 而不是囚徒困境；Roussel et al. 2026 用博弈论论证，失控成本足够高时，暂停符合国家自利；Yudkowsky & Soares 2025 是面向公众的版本。

**相对新的部分：**
- Proposition 9–11：AI 降低控制成本时，所需独立纠错的增长率 $\alpha\ge g/(1+\eta)$，以及拆分指数；
- 掩蔽与捕获的耦合，以及"保守报警需要独立的掩蔽上界"（Remark 5）；
- Proposition 7(3) 对 pacing problem 的稳健性形式化；
- Proposition 21：冻结份额的暂停可能完成捕获；
- 若加入 S6：竞赛中的风险补偿；
- 可能最有价值的一点：维持 pacing 均衡所需的观测通道本身被选择。Fudenberg & Koh 2026 证明，高灾难风险下只剩 pacing 均衡，但需要关于内部能力的透明度；本文的 Section 4–5 说明，这种透明度的供给者正是被捕获的对象。

这一点应当成为论文的定位句。

### S11【重大】体裁与认识论姿态

- **篇幅。** 28k 词、25 个以上命题，PC 无法审。必须选一条主线，见第 1 节的建议。
- **§0 仍保留 "In today's world reason says clearly that the actors must cooperate..."（第 136 行）。** GPT 评审 §14 最后一条指出过这个问题；附录 C 称已"tied to its conditions"，但这句话仍是无条件的断言。属于修复回流。
- **"cancerous objective"**（§10.3），以及 L6 的反驳栏（第 1317 行）和 §13（第 1380 行）的写法：任何"为地位接受高丧失自主风险"的行动者，都被定性为持有 cancerous objective、是"要反对的目标"。这相当于把 L6 的反例重新命名为病理，使 L6 不可证伪。这与 §12 "Refutation named in advance" 的反免疫原则相矛盾。建议改为中性术语（例如 "relative-standing-first objective"），并承认：若存在这样的行动者，Theorem S 对它不成立，此时需要执行而不是说服（与 S4 相连）。
- **"every other path is a dead end for humanity"**（第 1236 行）虽然附了条件，但在会议语境里会被当作结论来读。
- **AI 生成的说明。** 文首"Every sentence is AI-drafted"和各类来源说明，应当换成会议要求的 AI 使用披露。人类作者必须对全文负责。

### S12【中等】Theorem S 的建模细节

- **$q_{\mathrm{II}}$ 在 $T$、$P$、$S$ 三个分支上用同一个值。** 但 L1 让 $a$ 随总竞赛强度上升：在 $T$ 分支（只有一方竞赛）和 $P$ 分支（全体竞赛），$a$ 不同。应当按分支写 $q_{\mathrm{II}}^{T}\le q_{\mathrm{II}}^{P}$。
- **$\Phi^R=1-h_R$ 是外生给定的。** 合作下继续发展的风险（Plan A 也要交接）并不小。对方会说"合作也可能失败"，Plan A 自己估计的协议衰退约为一半。本文需要说明 $h_R$ 与 E3 的关系。
- **"我方赢家有止境"（非对称的 L4）这个最强版本没有被单独处理。** 本文的工具其实足以回答：
  - (i) 赢家是一个场（§4.4），其被委托系统受相对选择（Remark 3）；
  - (ii) 一个获得决定性优势的赢家，其未来克制的承诺不可信。这正是 Proposition 8 和 15 的承诺问题，用在了霸主身上；
  - (iii) 对手同样相信"我方赢家有止境"，所以这个信念不能成为共同知识，按它行事会触发对手的预防逻辑。

  应把这三点写成一个命题。
- **校准。** 不妨用对手自己的数字。按我对 Comparing Possible Plans 的读取，竞赛（Plan D）的对齐成功概率约为 25%，Plan A 约为 72%（请核对原页）。按对方自己的估计，合作分支的生存概率显著高于竞赛分支。这比 checks 里的假设数值更有说服力。

### S13【中等】§6.3 表的若干行需要更新或补充

- **"Operator alignment, scalable oversight, AI control" 一行低估了它们。** 它们正是 E3 和 I2/I3 的技术内容。Corollary 3(3) 自己说，合作下的节奏由"independent, AI-equipped correction"决定，这就是 scalable oversight 与 control 被交到独立纠错者手里。Exit 栏应改为"在独立纠错者手中时，是 E3 的技术基础"。"Supplies" 一栏也不只是"catches its own model's misbehaviour"：control 的目标是在假设模型未对齐的前提下防止灾难性行动。
- **"Frontier safety frameworks" 一行应当补上 2025–2026 年的证据。这些证据强烈支持本文：**
  - OpenAI Preparedness Framework v2（2025 年 4 月）：若另一前沿开发者发布了无同等防护的高风险系统，"we may adjust our requirements"；
  - Google DeepMind FSF v2（2025 年 2 月）：某些缓解措施若不被广泛采用，社会价值会显著降低；
  - Anthropic RSP v3.0（2026 年 2 月）写明 "we cannot unilaterally and unconditionally commit to staying in line with the industry-wide recommendations"，并采用 "competitor-contingent commitments"。其附录 A 的 "Anthropic in the lead" 情形承诺 "delay AI development and deployment as needed... until and unless we no longer believe we have a significant lead"。

  这几乎逐字印证了 Proposition 1/16（没有单边解）和 Proposition 25(3)（节奏由跟随者的威胁决定）。这是竞赛并且安全一派自己的承认，是本文最有力的经验证据，却完全没有出现。（"不点名"的问题可以用参考文献的方式处理。）
- **"Public evaluation institutes" 一行。** 2025 年起，若干公共 AI 安全评估机构被更名并转向安全或"标准与创新"。这是 C2 的证据（纠错者被竞赛重新选择），但需要谨慎表述。另外，加州 SB 53 和欧盟 GPAI Code of Practice 主要是把开发者自己的框架法定化，即"阈值在场内设定"在法定化后仍然存在。
- **缺失的行：**
  - 算力治理与硬件机制（HEMs、on-chip），它们不同于"验证协议"；
  - AI 辅助的验证与承诺；
  - d/acc 与防御加速；
  - 国际科学评估（International AI Safety Report）。这是 Corollary 2 "让预测成为共识"在现实中的载体，其局限（措辞保守，以及报告自己所说的 "evidence dilemma"）正是本文 Section 5 的主题；
  - 军事 AI 的人类控制规范，即 E1 的种子。

### S14【中等】Section 5 把模型自身的掩蔽与评估者的谱系偏差混在一起

**位置：** §5.1 第 574 行，$\beta_{\text{in}}$ 的例子包括 "evaluation awareness and sandbagging"。

**问题。** 评估觉察与 sandbagging（van der Weij et al. 2024；Needham et al. 2025）是被评估模型的行为，对独立评估者同样起作用。由于独立者通常缺乏白盒或 CoT 访问，可能作用得更强（Casper et al. 2024）。它们应当归入 $\beta_{\text{out}}$，或单列一项。

这一点很重要：它说明 Remark 5 所需的"独立的掩蔽上界"不能只靠制度独立来获得，还需要白盒方法、可解释性，或真实部署中的 ground truth。

### S15【中等】Proposition 22 的"盖子随压力增长"只是一个参数化，与 Plan A 的机制不对应

**问题。**
- $e^\ast$ 随 $\Omega$ 的增长（0.0075 → 0.49）只在 $n=4$、$r=1.3$ 等特定参数下算出，需要给出一般性的比较静态。
- Plan A 中，合作者的领先靠的是对秘密项目算力的供应链约束，不是双方自由选择努力。正确的对接通道是 S9 的"算法外溢使维持领先所需的算力差距扩大"。
- 共同前沿与 MAGIC（Hausenloy, Miotti & Dennis 2023）、CERN for AI、Intelsat 模式（Ho et al. 2023）以及 Plan A 的 "Consortium" 同属一类，应当引用。

### S16【次要】Proposition 6 和 7 的建模现实性

- $\iota$ 是二元的，而 $s=s_0e^{g_st}$ 无界增长。实践中的争论是 "meaningful human control" 和审查时滞。建议把 $\iota$ 改成连续的人工审查时滞，结论（被迫压缩到零）大概仍然成立，但更可信。
- Proposition 7 的线性不稳定模态与阈值型危害之间的映射需要说明（见 S7 中 E3 的部分）。

### S17【次要】杂项

- 第 482 行 "missiles at the data centres" 加了引号，却没有出处。它来自 Ren 的消息，应当删去引号或注明来源。
- §8.4 中的 "without relying on trust" 需要核对出处。
- † 参考文献仍未核实。
- §12 K1 "needs no elaboration"，见 S2。

---

## 3. "竞赛并且安全"的最强论点对照表

| # | 论点（最强表述与代表） | 本文是否回应（位置） | 缺什么 / 应如何回应 |
|---|---|---|---|
| 1 | **领先者用领先换取安全裕度；负责任的一方必须领先才能设定规范。** "Healthy lead" 带来安全裕度（Aschenbrenner 2024）；AI 2027 slowdown 结局；entente strategy（Amodei 2024）；RSP v3 附录 A "in the lead" 情形 | 部分回应：§4.4 赢家是一个场；Prop. 8；Prop. 25(3)；Thm S | 应先承认局部成立：领先确实减少偷工（Stafford et al. 2022；Armstrong et al. 2016）。再说明它为何不能扩展：(i) 裕度等于领先时长；快速跟随、外溢和间谍活动使领先只有数月，而 E3 要求的社会层面纠错以年计；(ii) 裕度条件以"仍然领先"为前提，RSP v3 写明 "until and unless we no longer believe we have a significant lead"，节奏于是由跟随者决定；(iii) 领先触发 Prop. 8；(iv) 霸主"之后会克制"的承诺不可信（Prop. 8/15 用于霸主）；(v) "设定规范"即把成功转换为规则影响力（$b_{ij}$），正是 Prop. 9 的捕获通道 |
| 2 | **对齐与控制会扩展。** 自动化对齐研究、AI control、scalable oversight；用 AI 解决 AI | 部分回应：Remark 3；Prop. 7(3)；Prop. 25(2) | 缺风险补偿（S6）：(K) 下，不完美的对齐进步可以提高实现风险。缺 control 自身的适用边界：可信与不可信模型的能力差在 (A) 下扩大更快。缺"危险期"结构：需要风险率可和（S1(c)）。缺"无法从内部证成"（第 1 节）。"对齐到好价值、而不是对齐到运营者"的版本也应回应：拒绝服务相对目标的模型是克制型载体，Prop. 1 适用于它 |
| 3 | **验证技术会成熟。** HEMs、flexHEG、zk 训练证明、遥测 | 回应：Thm B | 缺 $T$ 的内生性（投入端限制背叛规模）；缺"及时"的正确时间尺度（积累而非突破）；缺最有力的点：算法进步侵蚀投入端界限，由此得到速率条件（S9）；缺验证器自身的对齐 |
| 4 | **防御占优的 AI / d/acc 让竞赛变安全** | 未回应 | 用 Jervis 1978：共享、可区分的防御能力降低 $r$。此时竞赛对象消失（Thm A 分支 III），与本文结论一致，d/acc 是 (A)+(S) 角的盟友。排他、不可区分的"防御"（类似导弹防御）提高 $r$，是 (K)。应把 d/acc 写成 Corollary 3(3) 的范例 |
| 5 | **AI 赋能的协调与验证让信任变得不必要。** AI 测谎、AI 谈判者、程序均衡、zk | 部分回应："verification amplifies trust" | 应补上：信任被转移到验证 AI 的对齐和供应链上（循环依赖）；程序均衡要求可验证的代理真正掌握决策，等于不经推翻的委托（不可回头点一）；Prop. 14：意图仍不可验证 |
| 6 | **暂停把权力交给最不谨慎的人；暂停期间对齐进展更慢（Plan S 批评）；overhang** | 部分回应：§13 三条 | 应补上：(i) E2 在投入端实施（算力可排他）；(ii) overhang 与 Prop. 15 的冲突，所以 E2 必须包括投入限制；(iii) 暂停期间可以在现有系统上做安全研究（Plan A 的 Stage 2 就是近乎暂停）；(iv) 第三条答复（"不暂停者也活不下来"）依赖 Thm S 的极限，应改用比较静态 |
| 7 | **威慑（MAIM）已经稳定，并能阻止冲刺** | 回应，但建模不对（S3） | 改为"威慑式拒止是否能实施 E2"：可观测性与可区分性、P2 下的及时性、指控的廉价话语、competitiveness 支柱强化 H1；引用 Abecassis 2025 等批评 |
| 8 | **必须身在前沿才能做安全研究、才能在规则制定中有席位** | 未回应 | Section 4 恰好回答：席位就是转换通道 $b_{ij}$；Prop. 9 中控制的回报随份额平方增长。研究访问可以通过非竞争性安排提供（Prop. 17/22） |
| 9 | **军事与经济必要性：我不用，对手会用** | 回应：Prop. 6、24 | 缺现实中的 E1 先例（核指挥控制的人类控制表态、Political Declaration、CCW）和节奏上限的类比（熔断）；缺部分联盟模型（S4） |
| 10 | **决定性优势是神话，起飞会很慢，竞争正常且有益** | 回应：Thm A 分支 III、"cooperation does not end competition" | 应承认：若 P1 不成立，快路线的结论消失，只剩 Tier 2（依赖 C0）和 Section 4。这本身也是反对"竞赛"修辞的理由（Cave & ÓhÉigeartaigh 2018） |
| 11 | **全球治理本身是灾难性风险：极权锁定、单点失败、卡特尔** | 部分回应：Prop. 22 末段、§4.4、Def. 3 "constrains properties, not form" | 应前置并正面回应 Bostrom 2019 VWH 的张力；把 Section 4 明确用到 E0 的机构上；说明为什么"分散且独立的纠错"比"单一守护者"更稳 |
| 12 | **对齐一旦解决，交给对齐的 AI 是最安全的终局**（Plan A 的交接） | 未回应 | 应指出：交接是在时间压力下（衰退风险）、以有限置信度、有计划地穿过不可回头点一；"高置信度"由场内纠错者给出（Section 4–5） |

---

## 4. 必须引用或正面回应的已有工作

带"待核"的条目，作者或细节我没有完全确认。

**A. 与 Theorem S 和 Corollary 3 最接近（必须定位差异）**
- Katzke, C. & Futerman, G. (2024). *The Manhattan Trap: Why a Race to Artificial Superintelligence is Self-Defeating.* SSRN / arXiv:2501.14749。同样的前提蕴含竞赛自我挫败，三条通道是冲突、失控和对民主的破坏；ASI 是 trust dilemma 而非囚徒困境。
- Roussel, E., Lauwaert, L., Swoboda, T., Ramsey, G., Uuk, R., Dung, L. & Aguirre, A. (2026). *Are we Doomed to an AI Race? Why Self-Interest Could Drive Countries Towards a Moratorium on Superintelligence.* arXiv:2605.01297。
- Fudenberg, D. & Koh, A. (2026). *Cooperating against Catastrophe.* arXiv:2609.28291。连续时间竞赛加上安全阈值：高风险下只剩 pacing 均衡；内部能力不透明会使合作更难维持。
- Yudkowsky, E. & Soares, N. (2025). *If Anyone Builds It, Everyone Dies.*
- Barnett, P. & Scher, A. (2025). *AI Governance to Avoid Extinction: The Strategic Landscape and Actionable Research Questions.* arXiv:2505.04592。"Off switch"与 halt，以及 US National Project 情景。
- MIRI TGT (2025). *An International Agreement to Prevent the Premature Creation of Artificial Superintelligence.* arXiv:2511.10783（作者待核）。
- Aguirre, A. (2025). *Keep the Future Human.* 与 E2 加 §10.6 高度重合。

**B. AI 竞赛的博弈与演化模型**
- Armstrong, Bostrom & Shulman (2016)，已引用。
- Han, T. A., Pereira, L. M., Santos, F. C. & Lenaerts, T. (2020). To regulate or not. *JAIR* 69。以及 Han et al. (2022) 关于自愿安全承诺的后续工作。
- Fernández Domingos, E. & Han, T. A. (2026). *Falling Behind Drives Unsafe Development in an Idealised AI Race Experiment.* arXiv:2607.26034。这是 $L_b$ 的行为证据。
- Askell, A., Brundage, M. & Hadfield, G. (2019). *The Role of Cooperation in Responsible AI Development.*
- Stafford, E., Trager, R. & Dafoe, A. (2022). *Safety Not Guaranteed: International Strategic Dynamics of Risky Technology Races.* 包含风险补偿，以及领先者与落后者的偷工条件。
- Emery-Xu, N., Park, A. & Trager, R. (2024). Uncertainty, Information, and Risk in International Technology Races. *Journal of Conflict Resolution.*
- Naudé, W. & Dimitri, N. (2020). The race for an artificial general intelligence. *AI & Society.*
- Cave, S. & ÓhÉigeartaigh, S. (2018). An AI Race for Strategic Advantage: Rhetoric and Risks. *AIES.* 竞赛叙事本身的风险，与 Corollary 2 直接相关。

**C. 结构性风险、gradual disempowerment、选择与 Moloch**
- Zwetsloot, R. & Dafoe, A. (2019). Thinking About Risks From AI: Accidents, Misuse and Structure.
- Dafoe, A. (2018). *AI Governance: A Research Agenda.*
- Critch, A. & Krueger, D. (2020). ARCHES。Critch, A. (2021). What Multipolar Failure Looks Like, and RAAPs。Remark 3 和 Lemma 0 的近亲。
- Kulveit, J. et al. (2025). Gradual Disempowerment. arXiv:2501.16946；ICML 2025 position paper。对应 $q_{\mathrm I}$ 与 E1。
- Hendrycks, D. (2023). Natural Selection Favors AIs over Humans。Hendrycks, Mazeika & Woodside (2023). An Overview of Catastrophic AI Risks（其中的 AI race 一节）。
- Alexander, S. (2014). Meditations on Moloch。Bostrom (2014) 的 decisive strategic advantage；Bostrom (2019) The Vulnerable World Hypothesis。

**D. 威慑与 MAIM 之争**
- Hendrycks, Schmidt & Wang (2025)，已引用，但应写明其三支柱。
- Abecassis, D. (2025). *Refining MAIM.* MIRI（作者待核）。
- AI Frontiers (2025). Superintelligence Deterrence Has an Observability Problem。IAPS (2025). Crucial Considerations in ASI Deterrence。RAND (2025). Seeking Stability in the Competition for AI Advantage。
- Jervis, R. (1978). Cooperation under the Security Dilemma. *World Politics.* 必须引用。Schelling & Halperin (1961)。

**E. 验证与算力治理**
- Shavit (2023)；Baker (2023)；Wasil et al. (2024)；Sastry, Heim et al. (2024)；Kulp et al. (2024, RAND HEMs)；Scher & Thiergart (2024)；Harack et al. (2025)（待核）；Ho, L. et al. (2023) *International Institutions for Advanced AI*；Trager et al. (2023) 的 jurisdictional certification；Hausenloy, Miotti & Dennis (2023) MAGIC。

**F. 前沿安全框架、safety cases、评估科学与捕获**
- Karnofsky (2024). If-Then Commitments。Clymer et al. (2024)；Buhl et al. (2024) safety cases。
- 框架原文：Anthropic RSP v3.0（2026，附录 A）；OpenAI Preparedness Framework v2（2025）；Google DeepMind FSF v2（2025）。
- Raji et al. (2022) Outsider Oversight；Casper et al. (2024) Black-Box Access is Insufficient；Longpre et al. (2024) A Safe Harbor for AI Evaluation。
- Wei, K., Ezell, C., Gabrieli, N. & Deshpande, C. (2024). How Do AI Companies "Fine-Tune" Policy? Examining Regulatory Capture in AI Governance. *AIES.* 直接对应 Section 4。
- van der Weij et al. (2024) AI Sandbagging；Needham et al. (2025) 关于评估觉察（待核）。
- International AI Safety Report (2025, 2026)。

**G. 对齐、控制与可扩展监督**
- Greenblatt, Shlegeris, Sachan & Roger (2024). AI Control（ICML）。Irving, Christiano & Amodei (2018) Debate；Bowman et al. (2022)。
- 开放权重的可篡改性：Qi et al. (2024)；Lermen et al. (2023)；Tamirisa et al. (2024)；O'Brien et al. (2025)。后训练增强：Davidson et al. (2023)。

**H. 军事 AI、速度与人类控制**
- Horowitz, M. (2019). When speed kills. *Journal of Strategic Studies.* Scharre, P. (2018). *Army of None.*
- Political Declaration on Responsible Military Use of AI and Autonomy (2023)；2024 年关于核武器使用决定保持人类控制的领导人表态。

**I. 时滞、自动化与节奏**
- Bainbridge, L. (1983). Ironies of Automation. *Automatica.* Lemma 1 的经典来源。
- Marchant, Allenby & Herkert (eds.) (2011). *The Growing Gap Between Emerging Technologies and Legal-Ethical Oversight: The Pacing Problem.*
- Ord (2020) *The Precipice*；Thorstad 关于 time of perils 的批评。

**J. 替代路线与 §10.6 的近邻**
- Drexler (2019) CAIS；Bengio et al. (2025) Scientist AI；Buterin (2023) d/acc；Nordhaus (2015) Climate Clubs（部分联盟）。
- 合作 AI 与程序均衡：Dafoe et al. (2020) Open Problems in Cooperative AI；Tennenholtz (2004)；Conitzer & Oesterheld (2023)。

**K. 立场范例（作为被回应对象）**
- Kokotajlo et al. (2025) AI 2027；Aschenbrenner (2024) *Situational Awareness*；Amodei (2024) *Machines of Loving Grace*（entente）；Tegmark (2024) 对 entente 的批评；AI 2040 的 Comparing Possible Plans 与 Capability Scaling Strategy 两页。

**L. 经验趋势**（用于 E3 和 S9）
- Kwa et al. (2025, METR) 任务时长倍增；Ho, A. et al. (2024, Epoch) Algorithmic progress in language models。

---

## 5. 应当保留的部分

1. **Section 4 的二阶选择与速率条件（Proposition 9–11）。** "AI 降低控制成本时，独立纠错至少要以 $g/(1+\eta)$ 的速率增长"，以及拆分指数 $k^{2/\eta}$。这是本文最新颖、最可检验、对评估治理最有用的结果。建议作为会议版的核心之一。
2. **掩蔽与报警规则（Proposition 12 与 Remark 5）。** "静默越线是报警规则的属性，而报警规则是治理选择"，以及"保守报警需要来自场外的掩蔽上界"。这对评估政策有直接含义；按 S14 修正分类即可。
3. **Proposition 7(3) 的 $e^{a\tau_c}$ 稳健性下界。** 这是对 pacing problem 最干净的形式化："预测性控制也逃不过模型误差容忍度按指数缩小"。配上 S7 建议的 E3 测量方法，会很有说服力。
4. **Theorem B(3)："验证不承载的东西"。** 包括不可验证的信息、未来承诺、审批者的判断、验证自身的可靠性。尤其是"抽样重算证明申报的就是运行的，但不能证明批准是对的"，这一区分在验证社群里不常被说清楚。
5. **Corollary 1："降低赢的价值是唯一同时放松所有约束的杠杆"。** 这是本文相对 Plan A 最好的规范性洞见，也是与 Plan A 作者最可能形成共识的地方。他们自己也说要消除 winner-take-all。
6. **Proposition 21：冻结份额的暂停可能完成捕获，所以暂停必须隔离规则制定。** 新颖，并且直接影响暂停提案的设计。
7. **Proposition 6(5)–(6) 与 Proposition 8(3)–(4) 的诚实处理。** 失控成本占优时不委托；谈判协议改变结论；高战争成本起威慑作用。这些让对手看到本文不是在挑参数。再加上 S6 的风险补偿命题，这一节会很强。
8. **§7.4 的"四种障碍"表。** 它把误判、真实冲突、协调失败和动态承诺分开，可以作为全文的组织框架。
9. **Proposition 18 的全行和修复与五条限度。** 它对"竞争者互相验证即独立"的天真看法给出了精确修正。
10. **§12 的预先命名反驳证据，以及关于"在位者对'针对自己'与'普适'纠错的立场"的可检验预测。** 这一预测可以用公开征求意见的文本编码，适合作为后续实证论文。
11. **"以生存作为现实主义自己的第一前提"这一修辞桥梁**（§10.2 "Relative gains, revisited"）。对国家安全读者很有效。Manhattan Trap 用的是同一策略，本文应当引用它并说明自己多出的部分：二阶捕获和节奏。
12. **整套诚实性装置。** 分层、连接假设 L1–L6、每个组合定理继承的条件、修复标记。会议版保留精简版本即可。
