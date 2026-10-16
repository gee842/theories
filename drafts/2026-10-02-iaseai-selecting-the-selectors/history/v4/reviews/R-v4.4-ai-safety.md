# THEORY v4.4 评审（第二轮）：AI 安全与治理从业研究者视角

审查对象：`v4/THEORY.md`，"No Winning Position: the integrated theory (v4.4)"，2271 行，约 3.6 万词。全文已通读，包括附录 A 的证明、附录 B 的数值说明和附录 C 的逐条对照。

读的顺序：
1. 本人上一轮评审 `reviews/R-v4.3-ai-safety.md`；
2. `reviews/SYNTHESIS-v4.3.md`；
3. `THEORY-v4.3.md` 的第 8、10 节，用来对照改动；
4. Ren 的方向文件 `sources/16-claude-code-directions/2026-10-03-v4-direction-cooperation.md`，重点是最后三节。

另外复核了 `checks_v44.log` 中的 RC（命题 28）和 LM（引理 M）两组输出，并手算了命题 28 的四组均衡和实现风险，与正文一致。

评审立场与上一轮相同：IASEAI'27 程序委员会成员，来自技术对齐、控制、评估和前沿治理社群。先替对方给出最强论证，再判断本文是否答上了。

**核查范围与限度。**
- **AI 2040。** 2026-10-03 通过抓取工具读了 ai-2040.com 的这些页面：首页、summary、FAQ、How Plan A solves our 5 biggest problems、Plan A Assumptions、Comparing Possible Plans、Deal Decline、Verification Plan、Covert AI Projects、Capability Scaling Strategy、Compute in Plan A、Security in Plan A、Alignment Roadmap。
  - 抓取工具先经一个小模型处理再返回内容。下文标为"原文"的句子，是该工具作为逐字引文给出的，投稿前仍须对原页核一遍。
  - 网站的 PDF 超过抓取上限，没有读到。
  - "对退出方施加制裁与威胁"一条，本轮没能复核（上一轮读到过）。
  - "解体时各方保留协议前算力 2% 的加固储备"，来自 Deal Decline 页的检索摘要。
  - "一方的数据中心设在第三国、由东道国接管威胁触发自毁"的具体安排，只见于二手摘要，没有在原页核实。
- **文献。** 第 5 节所列近期文献的作者、编号和日期，都通过检索确认过。
- **安全框架。** OpenAI Preparedness Framework v2 的竞争者条款，用检索到的原文句子确认。Anthropic RSP v3.0 的"竞争者条件承诺"与"领先时放慢"条款，用检索摘要加上上一轮读过的原文确认。
- **AI 2027。** slowdown 结局的细节（落后方约差两个月；以 DPA 合并国内算力，达到全球约 50%）来自检索摘要，没有读原页。

---

## 1. 总体判断

### 1.1 这一版做对了什么

v4.4 是一次实质修订，不是措辞调整。对本社群最重要的进步有七点。

1. **(A) 不再包含 H3。** "(A) 排斥 (S)"的同义反复拆掉了。争点被明确放到三个前提上：(X) 复利、(U) 有界理解、(φ) 不可逆模态。第 12 节为每个前提写出了反驳观测。方向是对的：争点现在可以检验，而不是靠定义得出。
2. **主范例换对了。** "领先换安全裕度"被立为这一立场的主形式（命题 29），并点名了 Aschenbrenner、Amodei、AI 2027 slowdown 结局和 Stafford–Trager–Dafoe。
3. **风险补偿进入正文（命题 28）。** 数字可以复现，适用条件写得诚实。
4. **MAIM 的读法与 Theorem E 自洽了。** 它被重读为"以威慑实施 E2 的尝试，在 P2 下失效"。
5. **§8.5 对 Plan A 的描述大体准确。** 主动承认了 Plan A 的合作要素，撤回了"most complete version"这个稻草人说法。
6. **Theorem E 的结构现在是全文最有价值的部分。** E3 是常设条件（Theorem E(1)）；长期生存要求 E0 或共同的 E1（Theorem E(2)）。这是"世界必须合作"最干净的定理形式，远好于"三选二"。
7. **一组诚实修复。** L6 去免疫化、命题 24 的诚实修复、核武器的四点差异、"P2 两难"推论，PC 都会认可。

### 1.2 还没有过关的地方

**核心问题已经从"假设了极限"转移到"假设 AI 监督的覆盖为零"。** 这是本轮最主要的判断（N1）。

v4.4 的推导链是：由 (X)(U)(φ) 推出引理 M；再由命题 26 推出"超出理解的纠错要么缺席，要么就是委托"。对账后会发现两处记账不一致。
- 引理 M 的未覆盖比例 $1-U/X$ 中，$U$ 只计"人能理解、能争议"的纠错。
- 由 AI 承担、人无法逐项争议的监督，在 (φ) 的危险率里按零覆盖计算。

也就是说，"AI 监督不提供安全"被写进了 (φ) 的适用方式。可这恰恰是 scalable oversight、AI control 和自动化对齐研究整个研究纲领所否认的命题。

还有一处不一致。命题 26 的第二支（委托）要借引理 D 才变得致命，而引理 D 只在竞赛下成立。引理 M 却在合作下也把同一部分行为计为未覆盖。

PC 里的对齐与控制研究者会一眼看到这一点。好消息是它能修，修完更强。N1 给出一个"逐层监督保真度"的推导：只需"每层监督的误差下降得不够快"，引理 M 就能恢复，不必假设"AI 监督无效"。

**其余主要问题：**
- **§8.5 的"伪解"诊断作为判据太宽（N2）。** 诊断是"形式是合作，内容是竞赛，竞赛留在执行层"。可本文自己的 Definition 3 也要求对不合作者实行覆盖和执行，同样适用。另外，Plan A 的验证思路是限制背叛的规模，而不是要求近乎完美的探测，所以说它"需要近乎完美的及时探测"不公平。用 Plan A 自己的数字，可以把"伪解"做成一个可检验的三条件判据，既更公平，也更有杀伤力。
- **命题 29 只是一份指向其他结果的清单，不是一个关于领先的模型（N3）。** 第 (1) 条的机制与竞赛理论的"挫败效应"相反。最有力的证据都没有用上：
  - RSP v3 写明，领先时放慢，"直到不再相信自己有显著领先"；
  - AI 2040 作者对"领先方烧掉部分领先做安全"（他们的 Plan C）估计的成功率是 20–63%；
  - Plan A 自己要求的起飞时间约为十年。
- **Theorem E(2) 与推论 3 依赖 L3 外生给定的 $s$ 指数增长（N4）。** 如果 E2 把战略决策环中的能力封顶在委托门槛 $s^\ast$ 以下，"(K)+E2 只能推迟"就不成立。这与本文 §10.7 的冷战读法（"靠阻止决定性而存活"）有张力，也与 Fudenberg & Koh 2026 的 pacing 均衡有张力。
- **推论 2 自相矛盾（N5）。** 它说关于共享危险的消息"无偏、因而可信"，这与本文 §7.2 自己的 Crawford–Sobel 设定矛盾。
- **最接近的文献仍未引用（S10）。** 上一轮点名的几篇，§13 仍写着"to be identified and verified"，尽管上一轮已经给出完整书目。本轮我逐条核实了编号（第 5 节），并补上三篇新发现的近邻工作。

### 1.3 IASEAI 结论

**若压缩为 10 页、按现状投稿：borderline，偏 weak reject。** 比上一轮上调了一档。

加分：
- 立场被公平地重述了；
- 以下内容是这个社群会认真读的：风险补偿；二阶的纠错者选择及其速率条件；掩蔽与保守报警；时滞稳健界；"E3 常设，长期必须 E0 或 E1"的结构。

扣分：
- **核心推导**在对齐研究者看来仍是"假设 AI 监督无效"（N1）。
- **新颖性**会受质疑：与 Manhattan Trap、Dung & Hellrigel-Holderbaum 2025、Roussel et al. 2026、Fudenberg & Koh 2026 的重叠没有定位。
- **Plan A 一节**如果保留"需要近乎完美的探测"等说法，会被 AI Futures Project 一方的审稿人判为不公平。

**做到下面这一处修改，再加上第 5 节的定位，可以进入 weak accept。**

**最重要的一处修改：把 (U)、(φ) 和命题 26 从渐近前提改写成一个可测量的"监督追得上"条件，并据此把主命题改写成举证责任形式。** 分三步：
1. **拆开纠错能力。** 写成"人类带宽 × 每单位人类注意力的杠杆"。杠杆由 AI 逐层提供，每层保真度 $f<1$。由此可以推出：除非逐层误差至少以约 $1/(gt)$ 的速率下降，有效覆盖率趋于零，引理 M 成立（推导见 N1）。被争议的假设"AI 监督无效"，于是换成"逐层监督误差下降得不够快"。后者可测、可反驳，而且对齐研究者自己就在追踪这个量。
2. **把命题 26 写成三支：** 缺席；委托；或用限制能力与权限的方式预防。再证明第三支在 (K) 下属于命题 4 意义上的克制，会被竞争掉。
3. **主命题改写为举证责任形式。** 在 (K)(A) 下，安全同时要求两件事：
   - 覆盖的增长不低于能力的增长；
   - 端到端纠错时滞落在 $e^{-a\tau}$ 的容忍度之内。

   这两项的证据都在竞赛内部形成（第 4–5 节）。而竞赛一方自己的框架把安全承诺写成以"仍然领先"或"对手也遵守"为条件（RSP v3、PF v2）。所以对方无法用自己认可的 safety case 标准证成"竞赛中也安全"。Theorem S 降为这一命题在极限下的推论。

这与 Ren 的方向一致：竞赛自己制造了让这几个量趋于 1 的动力学。更准确的说法是：**竞赛并不制造复利；竞赛拆掉了复利的每一道刹车。** 具体是：
- L1 抬高了 $g$；
- 命题 4 使单方减速被支配；
- 命题 28 把安全进步换成速度；
- 命题 9–11 让纠错者被选择；
- 引理 D 让被委托的系统按竞赛表现被保留。

引理 M 本身只依赖复利，不依赖竞赛，Theorem E(1) 已经承认这一点。把这句话说清楚，"必须合作"的理由就从"极限"变成了"刹车只能一起踩"。

---

## 2. 上轮条目核验表

"附录 C 标记"一栏是 v4.4 的自评。"本评审判断"一栏是我对该修复在本社群面前是否站得住的判断。

| 条目 | 附录 C 标记 | 本评审判断 | 依据与残留 | 还需要什么 |
|---|---|---|---|---|
| S1 前提即争点；(A) 含 H3 | 完成 | **部分成立** | (A) 不再含 H3；推论 3 改为"斗争与安全"，撤回了"三选二"；采用了危险期框架（引理 M："the time of perils does not end"）。残留：争点转入 (U)(φ)，以及"只计人可争议的覆盖"的记账方式（N1）；"比较静态 + 举证责任"命题没有写；推论 3(1) 依赖 L3 的 $s$ 无界增长和 DC（N4）。 | N1 的修复；把"在竞赛内部无法证成"写成一个命题 |
| S2 Plan A 定位与细节 | 完成 | **大体成立** | 要素、作者、去赢家通吃的设计、作者对竞赛与破坏的判断，都已准确。残留：衰退估计应归属一位作者，且其中包括"受损"；"需要近乎完美的探测"不公平；把引理 D 用到交接上缺前提；"留下了原因"一句与同节对其合作要素的肯定自相矛盾；§12 K1 的"needs no elaboration"仍在。 | N2 的事实核对表与三条件判据 |
| S3 MAIM 建模 | 完成 | **成立（定性）** | 威慑读作 E2 的尝试；§6.3 表和 §13 都已更新。残留：没有"领先者是否冲刺"的小模型；没有承认 MAIM 作者自己提出的可观测性补救（透明、AI 辅助检查、数据中心选址）；没有引用 Abecassis 2025 和 Arnold 2025 两篇批评。 | 写一个冲刺威慑条件：冲刺收益 < 及时发现概率 × 被破坏的损失；补引文 |
| S4 tu quoque；推论 2；部分联盟 | 完成 | **部分成立** | 推论 2 收窄到共享危险，加上了"由公开前提推出"；可行性与优先级分开写了。残留：推论 2 中"无偏"一句与 §7.2 矛盾（N5）；执行层的 tu quoque 没有处理（对不信服者实行覆盖，仍需验证与威慑）；异质信念版的 Theorem B 没有做；部分联盟仍列为开放问题；产生预测的机构没有施加第 4 节的分析。 | N5；补一段"执行只需处理信念分布的上尾"的论证 |
| S5 三处混同 | 完成 | **部分成立** | 引理 D 给出了机制；命题 26 区分了 $U(t)$ 之内的 AI 辅助纠错。残留：命题 7(5) 第 507 行仍写 "If the faster correction is supplied by the contest's own systems, that is Proposition 6"；"control over correctors"与 AI control 的术语冲突没有改；§6.3 的 AI control 一行没有改。 | 删去或改写第 507 行那句，改指命题 26；全文改用 "influence over correctors" |
| S6 风险补偿 | 完成 | **成立** | 手算复核：$\Delta\psi=0.005$ 时两方委托，$1-0.99\cdot0.985^2=0.0395$；$0.003$ 时三方委托，$1-0.987^3=0.0385$；$0.001$ 时 $0.0326$；基线 $1-0.99^3=0.0297$。与正文一致。 | 一般形式与措辞（N9） |
| S7 出口的操作化 | 部分 | **部分（同意）** | 出口已命名并划定范围：E1a/E1b；E3 加入了"可争议"要求。指标仍未提出。 | 见 N8 的指标表 |
| S8 "足够好、分布式"的供给 | 开放 | **开放（同意）** | §10.8 仍有 "autonomous provision ... held by no one"，与 E1、$\mathcal K_{\min}$ 的张力没有化解；近邻工作（CAIS、Keep the Future Human、Scientist AI、d/acc）没有引用。 | 至少引用并说明差异；"树"保留作结尾意象 |
| S9 $T$ 的内生性；验证依赖 AI | 部分 | **基本未成立** | 只在"可靠性信任"之下注明了验证依赖 AI。以下三点都没做：投入端核算限制背叛规模，因而 $T$ 是内生的；"及时"的正确时间尺度是秘密积累算力所需的时间，不是背叛到产生决定性效果的时间；算法进步会侵蚀投入端的界限，需要一个速率条件。这个缺口直接造成了 §8.5 对 Plan A 的不公平（N2）。 | 写出速率条件：投入端界限的收紧速率不低于算法效率的进步速率 |
| S10 新颖性与定位 | 部分 | **未成立** | §13 写着 "should be engaged before publication (to be identified and verified)"，而上一轮已给出完整书目。 | 第 5 节给出已核实的编号 |
| S11 体裁与修辞 | 部分 | **理论稿可以接受** | §0 的 "reason says clearly" 现在绑定到 §10.2 的六点；"cancerous" 统一为一个定义，并有中性名称；L6 去免疫化。论文版仍需：删去修复标记；把"AI 起草"声明换成会议要求的 AI 使用披露；删去 "dead end for humanity"；癌症意象移入脚注。 | 论文版处理 |
| S12 Theorem S 的建模细节 | 开放 | **实际已部分完成** | 附录 C 低估了自己：$q_{\mathrm{II}}$ 已按分支区分；$h_R$ 已与 E3 挂钩（Theorem S(2)）；"我方赢家有止境"已由命题 27 处理。还缺用对方自己的数字校准。这些数字现在可以核对：避免错位接管的概率，Plan A 70–81%，Plan C 20–63%，Plan D 10–55%。 | 补一段校准 |
| S13 §6.3 表 | 部分 | **部分** | 新增了四行："领先换裕度"、"降低所有人决定性的防御"、"保留竞赛的验证协议"、"AI 移出竞赛"。残留：前沿安全框架的竞争者条款仍未当作证据使用；AI control 一行没有改；缺三行：HEMs 与算力治理、国际科学评估、军事 AI 的人类控制规范。 | N7 |
| S14 掩蔽归类 | 开放 | **开放，而且扩散了** | §5.1 仍把 evaluation awareness 和 sandbagging 列入 $\beta_{\text{in}}$。§10.2 第 5 点又把 evaluation awareness 当作"不可缩短的证据时滞"，这是范畴错误（N7）。 | 单列一项模型侧掩蔽 $\beta_{\text{model}}$ |
| S15 命题 22 与 Plan A 的机制 | **附录 C 漏列** | **部分** | 命题 22 已按 $n$ 人博弈修复；Plan A 的领先机制已改述为供应链核算。残留：$e^\ast(\Omega)$ 仍是单组参数下的数字；MAGIC、CERN for AI 没有引用。附录 C 的 AI 安全条目里没有列 S15。 | 补列；给出一般的比较静态，或注明结果依赖参数 |
| S16 $\iota$ 二元 | 开放 | **开放（同意）** | 理论稿可以保留。 | 论文版加一句说明 |
| S17 杂项 | 开放 | **部分** | "without relying on trust" 已核实：Verification Plan 原文为 "This deal needs to be enforceable without relying on trust"。v4.4 转述为 "designed to work without trust" 是准确的，这一子项关闭。残留：第 528 行的 "missiles at the data centres" 仍加引号而无出处；† 参考文献未核；K1 未改。 | 删去引号或注明出自 Ren；核对 † 文献 |

---

## 3. 新问题（按严重度排序）

严重度分四级：致命、重大、中等、次要。

### N1【致命，但可修】引理 M 与命题 26 记账不一致；AI 监督在 (φ) 中按零覆盖计；(U) 没有操作化；"可争议"没有定义

**位置：** §10.2 的 (U)、(φ)、引理 M、命题 26 和"P2 dilemma"；§4.3 命题 11 之后的处方，以及命题 25(4)；Theorem E(1)；§8.4 树中的 Q3；§12 的 (U) 一行。

**问题与论证。**

1. **记账不一致。**
   - 命题 26 把"超出 $U(t)$ 的行为"分成两支："不被纠正"与"被人无法理解和争议的系统纠正（委托）"。第二支只有在竞赛下，借 Remark 3 和引理 D，才变得致命。
   - 引理 M 用的未覆盖比例是 $1-U/X$，而 $U$ 按 (U) 的定义只计人可争议的纠错。于是"被 AI 监督覆盖、但人无法争议"的行为，在引理 M 里已经按"未覆盖"算，并承受每期 $h\varphi$ 的危险。
   - 两处合在一起，结论"超出理解的纠错要么缺席、要么就是委托，两支都致命"，靠的是 (φ) 对 AI 监督按零覆盖计算，而不是推导。
   - 合作下这个问题更明显。Theorem E(1) 说 ¬H3 在合作下也必要，"because Lemma M applies to any development that outruns contestable understanding"。可是合作下第二支并不经过引理 D。若 AI 监督确实有效，本文没有给出它在合作下也致命的理由。

2. **两支并不穷尽。** 还有第三支：**预防**，即用限制权限和能力的办法，让灾难性行动无法发生或一定被抓住。AI control 的原意并不是"理解"不可信模型的行为，而是在假设它可能未对齐的前提下设计协议，让它无法得逞（Greenblatt, Shlegeris, Sachan and Roger 2024；本文没有引用这篇）。沙盒、断网、速率限制、关键操作双人签字，都不需要理解被监督的行为。
   - 补上这一支，论证反而更强。在 (K) 下，限制权限会削弱竞赛实力，是命题 4 意义上的克制，按命题 6 的逻辑会被竞争掉：扩张权限本身就是一种委托压力。

3. **与本文自己的处方冲突。** 命题 11 之后与命题 25(4) 给出的处方是："equip independent correctors with AI, while that correction stays within $U(t)$"。这里必须二选一。
   - 如果"人加 AI 工具"仍算在 $U(t)$ 之内，那么 $U$ 可以随 AI 增长，(U) 的亚指数前提就成问题。
   - 如果不算，这个处方对引理 M 就毫无帮助。

   本文必须说明选哪一边。

4. **(U) 的证据是双刃的。**
   - **Ashby 的必要多样性定律**要求调节者与被调节对象的多样性相匹配，但它不要求调节者是人。Ashby 本人就讨论过"放大调节"。所以 Ashby 支持的是"纠错必须随 $X$ 扩张"，而不是"只有人的理解才算数"。
   - **更好的证据**是 Bloom, Jones, Van Reenen and Webb 2020（"Are Ideas Getting Harder to Find?"）。研究生产率持续下降，人类知识的增长要靠指数增长的研究人员投入。人口不会指数增长，人能核对的理解也就不会指数增长。
   - **反面证据也该承认**：科学文献长期呈指数增长（de Solla Price 1963）。但那种增长是由研究人数的增长驱动的。

5. **对方最强的五个反论，以及本文能怎样回应**（回答任务问题 3）。

   | 反论 | 最强表述 | 能站住的回应 |
   |---|---|---|
   | Debate 与 prover–verifier 博弈（Irving, Christiano and Amodei 2018） | 判断比生成便宜。人当裁判，AI 互相论证，人的理解不必与能力同步增长 | obfuscated arguments 问题（Barnes 2020）：诚实一方未必能高效指出对方论证中的错误。实证结果有正有负（Khan et al. 2024；Kenton et al. 2024）。更根本的是总带宽：决策的数量随 $X$ 增长，即使每个决策都可判断，人的总审计工时也有限 |
   | AI control 与 trusted monitoring | 由可信的弱模型监控不可信的强模型，人只审被标记的少数动作，每个人工小时的杠杆随自动化增长 | 可信模型必须弱到不会 scheme，而可信与不可信之间的能力差在 (A) 下扩大。control 评估要求红队能引出不可信模型的最强攻击，这一点随能力超过红队而退化。control 的提出者本人就把它定位为早期变革性 AI 阶段的"桥"。这与引理 M 是一致的，本文应当这样写，而不是把它们写成对立 |
   | Weak-to-strong generalization（Burns et al. 2023） | 弱监督者能引出强模型的大部分能力 | 能引出能力，不等于能保证对齐性质。恢复比例也不是安全保证 |
   | 可解释性与形式验证提高 $U$ | 归因图、auditing game（Marks et al. 2025 中，盲测团队找出了被植入的隐藏目标）；guaranteed safe AI（Dalrymple et al. 2024）：人只需理解规格，证明交给小型可信检查器 | 覆盖率问题：解释了多大比例的计算？规格充分性问题：世界模型是否充分，恰恰落在人类理解的上限上 |
   | 自动化对齐研究 | 用 AI 做对齐研究，人只核对研究成果 | AI 2040 自己的 Alignment Roadmap（页面自述 "almost entirely focused on Plan C"）承认，在 "high-stakes, difficult, open-ended, and conceptually loaded tasks" 上，"we can't check the AI's output effectively"；又说 "AI control will probably be the most load bearing part of the safety case"；交接之后，"the AI project actually empowers AI systems with the ongoing management of the intelligence explosion"。这是命题 26 第二支最直接的证据，而且来自对方阵营 |

   结论：命题 26 在极限下成立，即能力无界复利、监督的层数或保真度有界时。在到达极限之前，它取决于两个经验量：每层监督的保真度，以及可信与不可信之间能力差的增长速度。当前写法把这两个经验问题写成了定义。

**修复一：推导，而不是假设。** 记号如下：
- $B(t)$：人类审计注意力，亚指数增长；
- $m>1$：每层监督的放大倍数；
- $f<1$：每层的保真度，即上一层能抓住下一层会漏掉的问题的概率。

推导分三步。
1. 用 $B$ 覆盖 $X$ 需要 $k(t)=\ln(X/B)/\ln m$ 层。
2. 整条监督链的保真度为
   $$f^{k}=(X/B)^{\ln f/\ln m}.$$
3. 在 (X)(U) 下 $X/B\sim e^{gt}$，于是 $f^k\sim\exp(gt\ln f/\ln m)\to0$。

**含义。**
- **引理 M 恢复，但只需"$f$ 有界地小于 1"。** 有效覆盖率趋于零，每期危险趋于 $h\varphi$。这一步不需要"AI 监督无效"。
- **与命题 11 平行的速率结果。** 要让 $f^k$ 保持有界下界，需要 $k(1-f)$ 有界，也就是每层误差 $1-f$ 至少以 $\ln m/(gt)$ 的速率下降。命题 11 说独立纠错要以 $g/(1+\eta)$ 的速率增长；这里说逐层监督误差要以约 $1/(gt)$ 的速率下降。
- **(K)(A) 把这个要求推向坏的方向。**
  - (A) 提高 $g$，要求更苛刻；
  - 在 (K) 下，监督系统按竞赛表现被保留（Remark 3）；
  - 命题 28 把 $f$ 的改进换成更多的委托。

  三者合起来，就是"AI makes AI safe"在 (K)(A) 下要承担的举证责任。
- **单层 trusted monitoring 也被覆盖。** 它是 $k=1$ 的特例：$f$ 随可信与不可信之间的能力差递减，而这个差距在 (A) 下扩大，同样推出覆盖下降。

**修复二：操作化"可争议"（contestable）。** 建议的定义：某一类纠错决策在时刻 $t$ 是可争议的，当且仅当以下四条同时成立。
- **(C1) 可辨读。** 存在人在预算 $b$ 内可以核对的理由（证据加论证）。核对不依赖被评估系统及其谱系的输出，或者只依赖可靠性已在更早的 $U$ 之内被证成的工具。
- **(C2) 可推翻。** 有指定的人类机构能在 $T_r$ 之内推翻它。
- **(C3) 确实被行使。** 人为植入的错误被抓出的比例不低于 $p$，人工推翻率不为零。这一条防止橡皮图章和自动化偏差（Parasuraman and Manzey 2010）。
- **(C4) 有容量。** 人工审计的吞吐覆盖后果性决策的比例不低于 $\rho$。

$U(t)$ 就是满足 C1–C4 的决策覆盖量。它可以测量：在 control 评估和 auditing game 中，固定人类工时，看植入缺陷的被抓率如何随模型能力变化。(U) 的反驳观测于是可以写成："在固定人类工时下，植入缺陷的被抓率不随能力上升而下降。"

**修复三：诚实处理合作下的情形。** 在合作下，如果 AI 监督的保真度确实达到上面的速率，本文推不出交接是致命的。应当说明合作下 E3 的"人可争议"要求有两个来源：
- 一部分是规范前提（§13："those affected ... should keep a meaningful capacity to contest"）；
- 一部分来自"监督保真度无法在 $U$ 之外被证成"。后者是一个证成问题，不是必然失败。

**修复四：补全 §8.4 的树。** Q3 缺一个分支："能，用人可审计的 AI 辅助监督，并达到所需的保真度"。这一支应当接到："那就是在做 E3。请核对逐层误差的下降速率。在 (K) 下，独立纠错供给不足（命题 10），而且它的进步会被换成速度（命题 28）。"

### N2【重大】§8.5：事实大体准确，但"伪解"判据太宽，有两处不公平；用 Plan A 自己的数字可以把它做成可检验的判据

**位置：** §8.5；§6.3 表倒数第二行；Theorem E(3)；附录 A 中没有对应的证明。

**(a) 事实核对**（回答任务问题 2）。

| §8.5 的说法 | 核对结果 | 依据 |
|---|---|---|
| 作者为 Larsen, Dean, Halstead, Lifland, Greenblatt, Kokotajlo（2026） | 准确 | 首页 |
| "designed to work without trust between the parties" | 准确 | Verification Plan 原文："This deal needs to be enforceable without relying on trust" |
| 算力申报与供应链核算；inference-only 改造；工作负载重算；研究透明 | 准确 | Verification Plan、Covert AI Projects |
| 解体时摧毁算力、晶圆厂和机器人 | 准确，即 MACD（Mutually Assured Compute Destruction） | Deal Decline |
| 加固储备与协议前算力成比例 | 准确：各方保留协议前算力的 2% | Deal Decline（经检索摘要） |
| 对退出方的制裁与威胁 | 本轮未复核 | — |
| 意在消除赢家通吃：多家公司、研究透明、扩散、公民红利 | 准确 | 5 biggest problems 页原文："Plan A prevents WW3 by ending the 'winner take all' effects of a race to superintelligence" |
| 作者认为竞赛和破坏都劣于协议 | 准确，而且有数字 | Comparing Possible Plans 中五位作者对"避免错位接管"的估计：Plan A 70–81%，Plan B 20–68%，Plan C 20–63%，Plan D 10–55% |
| "Proportional reserves preserve relative positions" | 需要收窄：只适用于解体之后的退路；协议期间的设计目标是 parity | 5 problems 页："many companies and governments with similar levels of AI" |
| "with $\mu\to1$ required at the moment of greatest temptation (Proposition 15(2))" | 命题 15(2) 推不出这一点，它是一个增长率条件。也没有回应 Plan A 为保证摧毁可信所做的设计（摧毁由对方的接管威胁触发）。另外，储备固定为协议前算力的 2%，而算力要增长约三个数量级，所以 Plan A 的设计本身就会让 $\mu\to1$ | Deal Decline；Compute 页（到 2040 年约 1 万亿 H100e） |
| 合法联盟须保持对秘密项目的领先，靠供应链核算在结构上实现 | 准确 | Covert AI Projects：约 20 倍，到 2035 年扩大到约 4.3 个数量级 |
| "requires near-perfect, timely detection (Theorem B)" | **不公平** | FAQ 原文把问题改写成 "What's the biggest defection they could get away with, and how bad would that be?"。估计秘密项目约占全球算力 0.5%，约 120 万到 150 万 H100e，比最大的合法实验室小约 24 倍。Plan A 的路线是压低 $T$，不是把 $\upsilon$ 推向 1 |
| 验证尚不成熟 | 准确 | Verification Plan 原文："Today, the verification frontier is not mature" |
| 节奏部分由协议衰退的风险决定 | 准确 | Capability Scaling 原文："scale as quickly as possible subject to maintaining high confidence that the scaling is safe"；延迟的收益会被 "the deal declining, covert projects reaching dangerous capabilities, or other existential risks" 抵消 |
| "In its scenario it estimates that risk at roughly even odds by 2040" | **需要改归属** | Deal Decline 页给的是一位作者（Lifland）的估计：协议开始后 10 年内 48%，5 年内 37%，解体与受损大致各半；年风险率在第 0–2 年约 11.6%，第 2–5 年约 6.9%，第 5–10 年约 4.0% |
| 列出的衰退原因 | 准确，但有选择 | 原文还包括领导层更替（选举、继任）、地缘冲击、发现秘密项目、灾难 |
| 保留 H2；以交接结束；交接受衰退风险的时间压力 | 准确，而且可以加上数字 | Capability Scaling 原文："if there were >5%/year chance of deal decline, that would point toward a handoff"，对应约 95% 的对齐置信度；到达 TED-AI 后 "close to a pause"，然后交接。5 problems 页：智能爆炸持续至少 10 年，交接前约 5 年处于顶尖专家水平的 AI |
| "a planned crossing of the first point of no return (Lemma D)" | **前提不足** | 引理 D 要求被委托的系统按竞赛表现被保留，在协议下这一点没有论证。更准确的说法是命题 26 的第二支，见 (c) |
| titration "which it calls the hardest part to execute" | 基本准确，应加 "arguably" | Verification Plan 原文："This will arguably be the hardest part of the deal to execute on competently" |
| "correction inside the field (Propositions 9–11 and 26)" | 需要论证 | titration 在多国政府全透明之下进行。本文命题 18 自己说，对手的监督有助于保持独立。要说它在"场内"，必须给出全行和的论证 |
| "relying on trust may be the better option" | 准确（原文用的是 "best"） | Plan A Assumptions 原文："If high AI takeover risk becomes common knowledge (for example, after we've caught early misaligned AIs in the act of sabotage), relying on trust may be the best option." |
| "It leaves the cause in place: the value of winning" | 与同一节对其合作要素的肯定自相矛盾 | 5 problems 页的 Problem 3 |

**(b) 判据太宽。** §8.5 的诊断是"保留竞赛在其执行之中"，具体是比例储备、互相摧毁、联盟必须保持领先。可是本文自己的出口同样需要执行。
- §10.4 说："Everyone else's best response is to hold E1 and E2 in common, and to cover them (Definition 3(a))。"
- 对不合作者实行覆盖，就需要验证、威慑和制裁。

按"执行中含有竞赛"这个标准，Definition 3 也会被判为伪解。Plan A 的作者一定会指出这一点。

**(c) 建议：一个可检验的三条件"伪解"判据。** 每一条都能用方案自己的文件来核对。

- **(P-i) 退路是一场决定性竞赛。** 解体时各方手里剩下的，是从保留下来的相对地位出发的决定性竞赛。
  - Plan A：各方保留协议前算力 2% 的加固储备，比例与协议前一致；算法进步因研究透明而为各方共有。按 Deal Decline 页，即使摧毁了算力，解体后约一年就到 ASI；不摧毁则约一周。
  - 也就是说，退路是一场为期一年、起点对称的冲刺，正好落在本文命题 8 和 Theorem A 分支 I 最坏的区域。
  - 这比"μ→1"更锋利：MACD 摧毁的是硬件，摧毁不了知识。而在算法外溢约 67%（Covert AI Projects 页的估计）的条件下，知识才是越积越大的那部分 overhang。
- **(P-ii) 解体风险在方案需要覆盖的时长上不可和。**
  - Plan A：一位作者估计第 5–10 年的年风险约为 4%。如果风险维持在这个量级，累计解体概率趋于 1。这是引理 M 型的不可和风险。
  - Plan A 对此的回答，是在衰退之前以交接结束协议，于是进入 (P-iii)。
- **(P-iii) 终点是交接。** 方案以交接为出口：把纠错交给人无法争议的系统，而交接所需的置信度被解体时钟压低。
  - Plan A：年衰退风险超过 5% 时，95% 的对齐置信度就交接。
  - Alignment Roadmap（面向 Plan C）承认，在最难的任务上 "we can't check the AI's output effectively"。

对照 Definition 3：真解在三条上都不同。
- 不建造决定性能力（E2），所以退路的起点远在"一年到 ASI"之前；
- 降低赢的价值（推论 1），并把 AI 移出竞赛（E1），所以解体风险可和；
- 没有交接期限。

Plan A 三条都满足，所以是伪解。这样，"伪解"就不再是一个标签，而是一个可检验的谓词。Plan A 的作者可以争论数字，但无法争论分类的逻辑。这完全符合 Ren 的要求：揭穿它"看起来像解"的原因。而且全部用的是他们自己的数字，比现在的写法更公平，也更有力。

**(d) 验证一节需要的修正。** "需要近乎完美的及时探测"应当改为以下三点：
- Plan A 压低 $T$ 的方式是限制背叛规模；
- 这个上界会被两件事侵蚀：算法外溢（他们自己估计约 67%），以及单位算力所含能力的增长；
- 因此存在一个速率条件：联盟在有效算力上的比值优势，增长速度必须不低于算法外溢使它缩小的速度。Plan A 对此的回答是硬件研发限速（约每年 10%）和 cap-and-trade。

写成这样，才是对 Plan A 公平而又尖锐的定量评估（与 S9 相同）。

**(e) Theorem E(3) 的机制与 Plan A 不吻合。** 详见 N4。Plan A 在 TED-AI 附近近乎暂停。按 E2 的定义，它并没有把能力封顶在委托门槛 $s^\ast$ 以下：TED-AI 远在 $s^\ast$ 之上。所以 Plan A 的问题不是"推迟了 $t^\ast$"，而是把世界停在了一个能力水平上，在这个水平，战略决策环中的委托压力已经最大，而它又没有 E1。

在我读到的页面中，没有找到 Plan A 关于 AI 在军事与战略决策环中使用的条款。如果确实没有，这是本文对 Plan A 最干净、也最公平的一条批评：**它缺的是 E1。** 请在原文和 PDF 中核实。

### N3【重大】命题 29 没有击败"领先换安全裕度"的最强版本；最有力的证据没有用上

**位置：** §8.1 命题 29；§6.3 表中"A lead buys a safety margin"一行；§13 对应的条目；附录 A 中命题 29 的证明。

**对方的最强表述**（合并几位代表）：
- **Aschenbrenner 2024：** 民主国家联盟保有"healthy lead"，并靠实验室安全防止被窃取，从而能在智能爆炸期间拿出部分领先做安全，并以强势地位谈判。
- **Amodei 2024 的 entente：** 先靠供应链取得领先，再以分享收益换取其他各方不来破坏。
- **AI 2027 slowdown 结局：** 领先方约领先两个月，用 DPA 合并国内算力以延长领先，改用可监控推理的架构（Safer-1），放慢并完成对齐。
- **Stafford, Trager and Dafoe 2022：** 在敌意中等、或落后方能力差距较大时，落后方不会冒险使用高风险技术，除非它追了上来。
- **Anthropic RSP v3.0 附录 A：** 领先、并有明确证据表明对手短期内追不上时，"delay AI development and deployment as needed ... until and unless we no longer believe we have a significant lead"。

**逐条评估命题 29：**

**(1) "The follower's best response to a leader that slows is to accelerate (Proposition 4(1))"——机制不对。**
- 命题 4(1) 比较的是 $S$ 与 $P$（面对一个竞赛者时，克制还是竞赛），并不是最优反应的斜率。
- 竞赛理论里，最优反应不是单调的。差距大时，落后方会减少投入，这就是挫败效应。本文已经引用的 Dixit 1987 恰好给出这个方向：强者先作承诺时，弱者会少投入。Stafford et al. 的结论也是这样。
- 所以对方会说：只要我保持大的领先，跟随者就会被挫败，花掉其中一小部分是安全的。

本文其实有正确的机制，只是没写：
- **花掉领先，就把竞赛带回均势。** 在均势附近，投入强度与偷工最大（命题 3 和 5；Stafford et al. 自己的"差距小且敌意高"区域）。
- **领先在跟随方不加速时也会缩小。** 途径是扩散、蒸馏和窃取。Plan A 自己估计约 67% 的算法进步外溢；Aschenbrenner 的论证本身就以安全能防住窃取为前提。

所以，裕度的半衰期由扩散决定，与领先方是否花钱做安全无关。

**(2) "a fixed lead buys a shrinking fraction of the uncovered hazard"——依赖 (U)，与 N1 是同一个争点。** 对方会说，裕度是拿来做 AI 辅助的对齐研究的（AI 2027 的 Safer-1），所以覆盖随能力增长。

但对方阵营里有直接证据，本文没有用上：
- **所需时长。** AI 2040 Plan A 要求 "the intelligence explosion happens over the course of at least 10 years"，交接前约 5 年处于顶尖专家水平的 AI。而 AI 2027 slowdown 的起点只是约两个月的领先。
- **成功率。** Comparing Possible Plans 把"领先方烧掉部分领先做安全，至少放慢 1 个月"列为 Plan C。五位作者对它避免错位接管的估计是 20–63%，Plan A 是 70–81%，Plan D（竞赛）是 10–55%。
- **换算。** 以 Plan D 为基线，Plan C 带来的接管风险下降，只相当于 Plan A 带来的下降的 14% 到 34%：
  - Lifland：13/38；
  - Kokotajlo：10/70；
  - Larsen：15/60；
  - Dean：15/60；
  - Greenblatt：8/26。

  写出"领先换裕度"情景的那批作者，自己估计领先能买到的安全，只有协调放慢所能买到的三分之一左右甚至更少。这是对命题 29(2) 最有力、也最公平的校准，同时补上了 S12 的最后一项。

**(3) "It cannot be certified from inside the contest (Proposition 26)"——引错了。** 命题 26 讲的不是证成。证成的论证属于第 4–5 节和命题 14：判断裕度够不够用的证据，由领先方自己的评估者在时间压力下产生，并受掩蔽（包括 evaluation awareness）的影响。

AI 2027 slowdown 中，放慢的决定由一个监督委员会以 6 比 4 投票作出。Plan C 的 Alignment Roadmap 写的是 "AI control will probably be the most load bearing part of the safety case"。这两点都可以作为例证。但"举证责任"这个命题本身仍然没有写出来（见 1.3）。

**(4) "Gains in safety are converted into speed (Proposition 28)"——模型不对应。** 命题 28 来自对称、单期的委托博弈，领先情景是不对称的。

不过有更直接的制度证据：
- RSP v3 的 "until and unless we no longer believe we have a significant lead"；
- PF v2 原文："If another frontier AI developer releases a high-risk system without comparable safeguards, we may adjust our requirements"。

安全承诺被明文写成以对手行为为条件，对手的安全变化会直接改变自己的要求。这正是本文命题 16（没有单边解）和命题 29(1) 的制度形式。

**(5) "The safety bought is the winner's, not every actor's"——这是价值分歧，需要明说。** entente 一派明确接受对手被支配，这正是他们的目标。本文的 (S) 定义为"every actor's survival"，里面已经包含了对手的自主。所以对他们，论证必须落在领先方自身的生存上：引理 M 作用于它自己的复利；命题 27；§4.4。

还有一点更有力，却没有写：**AI 2027 slowdown 中的裕度不是"花掉"的，而是"造出来"的**——靠用 DPA 合并国内算力，达到全球约 50%。这正是命题 9 所说的、对控制纠错者回报最大的集中。§4.4 说赢家仍是一个场，这里就是实例：结局中权力集中在一个监督委员会手里。这是用本文自己的二阶层反驳"领先换裕度"最有力的一处。

**修复。**
1. 用"扩散加均势"取代第 (1) 条的机制，引 Dixit 1987、Konrad 2009、Stafford et al. 2022，以及 Plan A 的外溢估计。
2. **给一个最小模型。** 记领先为 $\Delta(t)$（以时间计）。领先方完全暂停时，有
   $$\dot\Delta=-\delta\Delta-1,$$
   其中 $\delta$ 是扩散率。领先在
   $$T_p=\delta^{-1}\ln(1+\delta\Delta_0)<\Delta_0$$
   时耗尽。裕度够用的条件是 $T_p\ge\tau_{\text{req}}$。按 AI 2040 自己的估计，$\tau_{\text{req}}$ 以年计，而领先以月计。
3. 引用 RSP v3 附录 A，作为这一立场的制度形式。按 Ren 的不点名原则，正文写"一家领先开发者的框架"，在参考文献中列出出处。
4. 先承认局部成立：领先大、敌意中等时，落后方的冒险确实会减少。有了这个让步，其余论证才可信。
5. 第 (5) 条写明其中的价值前提，并加上 AI 2027 的"合并造裕度"一点。

### N4【重大】Theorem E(2) 与推论 3 依赖 L3 外生给定的 $s$；若 E2 封顶在 $s^\ast$ 以下，"(K)+E2 只能推迟"不成立；与 §10.7 和 Fudenberg & Koh 2026 有张力

**位置：** Theorem E(2)–(3) 及其证明（"Neither E2 nor E3 changes $g_s$ to zero"）；推论 3(1)、(3)；§10.7；L3。

**论证。**

$s$ 是 AI 节奏决策相对人类节奏决策的优势，它是部署在决策环中的能力的函数。L3 把它写成外生的 $s_0e^{g_st}$，而 E2 和 E3 恰恰在限制能力。分情况看：
- **只有 E3，且 $U$ 无界（比如线性增长）：** $s$ 仍然无界，$t^\ast$ 终会到达。"推迟"成立，只是可能推迟得很久。
- **E2 是一个水平上限 $\bar C$：** 有 $s\le s(\bar C)$。若 $s(\bar C)<s^\ast$，委托永远不会成为占优策略，(K)+E2 就第一不可回头点而言是持久的。此时推论 3(3) 的 "holds safety only until (K) is given up" 不成立。

与本文其他部分的张力：
- **§10.7 冷战一节**说对手"kept their contest by preventing decisiveness ... That is E2"，读法正是"(K)+E2 可以持久"。除非本文明说核和平同样只是推迟（风险不可和，部分靠运气，Sagan 1993），否则两处矛盾。
- **Fudenberg & Koh 2026**（arXiv:2609.28291）研究连续时间的能力竞赛。安全门槛以固定速率前进，共同灾难的风险率随"能力与安全之差"上升。结论是：灾难风险高时，唯一的 Markov 完美均衡是 pacing。这几乎就是 (K)+E3 作为无需协议、自我执行的均衡的形式化。

  这与本文 Theorem S(3) 一致（共享危险高时，合作不需要事前信任），也支持 E3。但它的模型里没有委托通道。本文能补上的，正是：
  - $s$ 增长带来的委托压力，可能在长期打破 pacing；
  - 透明度的提供者本身会被选择（第 4–5 节）。他们发现内部能力被隐藏、滞后公开时，pacing 更难维持，这与本文的掩蔽结果完全对接。

**修复。** 写明 (K)+E2 持久的条件：当且仅当 E2 在战略决策环中划的线低于委托门槛，即 $s(\bar C)<s^\ast$（按 DC 的精确形式）。

由此，Theorem E(2) 可以改写为：(K) 下的长期生存，需要以下三者之一：
- E0；
- 共同的 E1；
- 一条永久维持在 $s^\ast$ 以下的 E2 线。

第三者本身就是 E1 的一种形式，即不让 AI 主导决策环。三者都需要覆盖所有有能力的行动者，所以"世界必须合作"的结论保留，而且没有了内部矛盾。这也给 E2 的线提供了一个可操作的标准（见 N8），并把 Plan A 的问题定位为缺少 E1（N2(e)）。

### N5【重大】推论 2 说"共享危险的消息无偏，因此可信"，与 §7.2 本文自己的模型矛盾

**位置：** 推论 2 第一段："Every actor's interest is aligned on it, so by Proposition 14, with no bias on what all share, messages about it can be credible."

**论证。**
- 在 §7.2 的设定里，偏差 $b=\lambda\beta_s$ 来自发送者从接收者某一方向的反应中获得的好处，原文就举了"the receiver restraining more than the state warrants"为例。
- 关于共享危险的消息，作用正是促使对方克制。在 $\lambda>0$ 时，对方多克制，发送者在相对地位上就获益。所以恰恰对这类消息，$b>0$。可信与否，取决于接收者的反应，而不取决于状态是不是共享的。
- 危险的参数（$h$、$\varphi$、$g$，以及"自己的系统是否已被当场抓到"）有一部分是私人信息。Plan A 打开信任之门的条件是 "after we've caught early misaligned AIs in the act of sabotage" 成为共同知识，而这正是实验室层面的私人证据。

**修复。**
1. 删去引用命题 14 的那一句。
2. 推论 2 改为立足于三点：
   - 由公开前提推导，这一点正文已有；
   - 可核验的共享危险证据：带第三方核验的事故披露、由双方的独立评估者运行的共同评估套件、联合红队、国际科学评估的流程；
   - 代价高昂的信号（Kydd 2005），例如单方公开对自己不利的危险能力评估结果。
3. 注明在 $\lambda>0$ 时，来自对手的消息会被打折扣。所以预测必须可核对，或者来自 $b\approx0$ 的一方，例如独立科学家；而他们又受第 4 节约束，这就是 S4.3 提出的"产生预测的机构本身是纠错者"。

### N6【中等】"E2 costs nothing"忽视了延迟收益的代价，与命题 17 自相矛盾

**位置：** §8.4 树的 Q1（"E2 costs nothing"）；§10.7 末段（"Either way, E2 is cheap or necessary"）。

**论证。** 即使 AI 不具有决定性，E2 也会推迟 ASI 或 RSI 带来的收益。对方认为这些收益极大（Amodei 2024）。Plan A 拒绝把 Plan S 作为主方案，也正是因为停止期间 "does worse than Plan A at making forward progress towards solving the safety/alignment problems"。本文命题 17 自己承认，在共同前沿下 "the residual failure is too little speed, not too much"。

**修复。** 写成不可逆性的不对称：
- 若 AI 不具有决定性，E2 的代价是收益的延迟，而延迟有界、可以挽回；
- 若具有决定性，Theorem S 适用，损失不可逆。

这里用期权价值与不可逆性的经典结果（Arrow and Fisher 1974；Henry 1974），比"代价为零"可信得多。

### N7【中等】§6.3 表和评估相关表述的残留错误；前沿安全框架的证据没有用上

1. **AI control 一行（第 762 行）。**
   - 现在："Supplies: The developer catches its own model's misbehaviour"；"Exit: None: a faithful instrument of the contest is still its instrument"。这把 operator alignment 与 control 混为一谈。
   - 建议改为：
     - Supplies：在假设模型可能未对齐的前提下，防止灾难性行动的协议，用红队式的 control 评估来检验（Greenblatt et al. 2024）；
     - Leaves：有效窗口受可信与不可信之间能力差的限制，而 (A) 扩大这个差距；人类审计带宽；
     - Exit：由独立纠错者掌握时，是 E3 的技术基础。这与本文命题 11 之后的处方一致。
2. **术语冲突。** "Control over correctors"（§4.1 标题，以及第 552、695、742、1298 行）与 AI control 撞车，建议全文改为 "influence over correctors"。
3. **前沿安全框架一行，补上证据：**
   - PF v2（2025 年 4 月）的上述条款；
   - RSP v3.0（2026 年 2 月）的竞争者条件承诺和附录 A 的"领先"条款；
   - FSF v2（2025 年 2 月）：某些缓解措施的社会价值取决于是否被广泛采用。

   这是"竞赛并且安全"一方在制度上的自我承认，对应命题 16 和命题 29(1)，是本文现在最强、却仍未使用的经验证据。
4. **evaluation awareness 的归类。**
   - §5.1 把 evaluation awareness 和 sandbagging 列入 $\beta_{\text{in}}$。它们是被评估模型自身的行为，对独立评估者同样起作用，甚至更强（S14）。
   - §10.2 第 5 点又把 evaluation awareness 称为"不可缩短的证据时滞"。按命题 7(4) 的定义，不可缩短的时滞是指证据只在一个任何测试都缩短不了的显现窗口之后才出现。evaluation awareness 是测量效度问题，属于掩蔽，可以部分地用白盒探针和真实部署监测来处理。
   - 建议单列一项 $\beta_{\text{model}}$。第 5 点改举真正的不可缩短时滞：说服、劳动替代、gradual disempowerment 这类社会层面的危害。
5. **§10.2 第 4 点。** "No actor at the frontier has published verifiable limits"，就"可核验"而言是准确的。但应当引用已有的不可核验承诺：
   - OpenAI Charter（2018）："if a value-aligned, safety-conscious project comes close to building AGI before we do, we commit to stop competing with and start assisting this project"；
   - RSP v3 附录 A。

   它们都不具约束力，也可以由同一机构修改。这样，命题 27 中关于承诺问题的那一条就有了经验内容。
6. **缺失的三行：**
   - 算力治理与硬件机制（投入端验证，不同于协议验证）；
   - 国际科学评估（International AI Safety Report）：它是推论 2 在现实中的载体，其"evidence dilemma"正是第 5 节的主题；
   - 军事 AI 的人类控制规范：E1 的种子，包括 2023 年的 Political Declaration、2024 年两个核大国领导人关于核武器使用决定保持人类控制的表态、REAIM；金融市场的熔断机制，是给机器节奏设上限的先例。

### N8【中等】E1–E3 的可操作指标（回答任务问题 5）

附录 C 自己列为未完成。下面给出可以直接写进第 12 节的指标。其中"$a\approx\ln2/T_2$"是一个连接假设，类似 L1，应当照此标明。

| 出口 | 指标 | 阈值或判据示例 | 测量者与先例 | 反驳观测 |
|---|---|---|---|---|
| E1a 不为竞赛目标而建造或选择 | 训练目标与 model spec 审计：通用模型是否以"击败对手"或相对份额为奖励；部署中拒绝服务纯相对目标的比例 | 通用前沿模型不以相对优势为训练目标 | 独立审计 model spec 和训练环境清单 | 弱指标，诚实标注 |
| E1b 战略与军事决策环 | 需有人类授权、并有最短审议时间下限的后果性决策所占比例 | 核指挥控制 100%；武力使用与升级决策列出清单 | 条令、演习记录、事后审查；2023 Political Declaration、REAIM | 在比例不变的情况下，被委托系统仍主导结果（橡皮图章：人工推翻率趋于 0） |
| E1b 节奏上限 | 自动化代理在市场、网络行动中受熔断约束的覆盖率；获得机器速度交战授权的系统数量 | 有熔断，以及每个交易或行动的最短人类时滞 | 金融监管（熔断、LULD）的先例 | — |
| E1 平行人类能力（$\mathcal K\ge\mathcal K_{\min}$） | 被委托职能中，有训练有素的人员能在 X 小时内不借助 AI 接管的比例；手动回退演练的频率与成功率 | 关键职能 ≥ 1 次/季度，演练成功率 ≥ p | Bainbridge 1983；航空业的手动飞行要求 | 演练失败率上升，说明锁定正在发生（引理 1） |
| E1 与 E2 的交界：$s$ 的代理 | 在兵棋与战略模拟中，AI 节奏决策对人类节奏决策的胜率优势 | 战略决策环中的能力封顶在使 $s<s^\ast$ 的水平（N4） | 军方与独立研究机构的模拟 | — |
| E2 能力阈值（事前） | AI R&D 自动化阈值（各家框架的 AI R&D 或 ML R&D 类别）；METR 任务时长；自主复制与适应 | 例如以某个 50% 成功率任务时长作为红线 | 有法定访问权的独立评估者 | 越过阈值后，危险能力没有随之出现 |
| E2 投入端 | 经效率修正的训练算力上限；未核算算力占全球的比例；最大未申报集群的规模 | Plan A 的目标量级约 0.5% | 供应链核算、HEMs（MIRI TGT 2025；Scher 2026 列出的 28 种研究限制核查机制） | — |
| E2 速率条件（S9） | 投入端界限的收紧速率与算法效率进步速率之比 | 比值 ≥ 1。Ho et al. 2024：预训练的算力效率约每 8 个月翻倍，所以名义算力上限每年须收紧约 2.5–3 倍，才能守住同一条能力线 | Epoch 型的趋势测量 | — |
| E2 的退出条件 | Definition 3 的 (a)–(f) 各有代理：覆盖的算力份额；有法定访问权的独立评估者；I2 证书的估计值；事故报告与联合核查是否运作 | 全部到位，且 E3 检验通过 | — | — |
| E3 节奏 | $a\approx\ln2/T_2$，$T_2$ 为危险能力代理的倍增时间 | METR（Kwa et al. 2025）：约 7 个月（2019–2025），近期估计更短；对应 $a\approx0.10$/月 | METR 等 | 危险能力的增长与总体能力脱钩 |
| E3 端到端时滞 | $L=\tau_{\text{obs}}+T_d+T_r$：从能力出现到被独立评估发现、从发现到决策、从决策到撤回（下线、召回权重）的时间 | 命题 7(3)：建模相对误差 $\epsilon_m<e^{-aL}$。$T_2=7$ 个月时，$L$ 为 6、12、24 个月对应的容忍度分别是 0.55、0.30、0.09；$T_2=4$ 个月时分别是 0.35、0.12、0.016。以年计的立法周期在当前倍增速度下几乎没有稳健裕度；开放权重的 $T_r=\infty$，容忍度为零 | 监管机构、事故报告的期限 | 在观测到的 $aL$ 下，纠错仍然稳健 |
| E3 与 (U) | $\dot U/U$ 对 $\dot X/X$；$U$ 按 N1 的 C1–C4 定义测量（固定人类工时下植入缺陷的被抓率、人工推翻率、审计覆盖率） | $\dot U/U\ge\dot X/X$，这是引理 M 的前极限形式 | control 评估、auditing game | 固定人类工时下，被抓率不随能力下降 |
| E3 不可缩短时滞的危害类 | 分阶段部署，并设随机保留的对照组，用来缩短 $m_e$ | 部署节奏不快于 $m_e$ | 社会层面危害的监测 | — |

### N9【中等】命题 28 应给出一般形式，并收窄"最强回答"的措辞

**一般形式（解析结果，不只是数值）。** 在命题 6 的单期模型中，若 $\psi_0$ 固定，任何有 $k\ge1$ 个委托者的均衡，其实现风险
$$1-(1-\psi_0)^{n-k}(1-\psi_0-\Delta\psi)^{k}$$
对每个 $\Delta\psi>0$ 都大于基线 $1-(1-\psi_0)^n$。所以在命题 6(5) 的精确条件使委托成为均衡的整个区间上，只降低委托特有危险的进步，都会使实现风险高于进步之前。只有在 $\Delta\psi\to0$ 时才回到基线。四个数值点是这个一般结论的实例，正文应当给出一般形式。

**适用范围要写明。**
- 只涉及对齐进步中"委托专属"的那一部分；降低 $\psi_0$ 的进步可以降低实现风险。
- 单期，对称。
- 没有计入委托可能带来的其他风险的下降，例如更快的防御。

**措辞。** "This is the strongest answer to the claim that alignment will scale" 应当改为："对'让委托更安全就会让世界更安全'这一主张的回答。"

**与 alignment tax 文献对接。** Christiano 的思路是降低对齐税，好让安全的选项有竞争力。命题 28 说明：当"安全的选项"就是"不委托"时，降低委托的风险税会把行为推向风险更高的选项。这样表述精确、公平，对齐社群也能接受。

### N10【中等】(X) 测的是什么：行为多样性还是危险能力；时间单位与校准

**问题。**
- (X) 用的是"hazard-relevant behaviour 的多样性"。可前沿安全框架的做法，是集中盯住少数威胁模型（CBRN uplift、网络、自主性、AI R&D），用阈值评估。对方会说：总的行为多样性在爆炸，但危险的子集是可以瞄准的。
- 本文需要论证危险子集为什么也在复利：
  - 危险能力是通用能力的副产品；
  - 会出现新的威胁模型（unknown unknowns）；
  - AI R&D 自动化本身就是复利的来源。
- (φ) 把危险率设为与未覆盖**比例**成正比，而不是与未覆盖的**量**成正比。引理 M 之所以成立，靠的正是这个设定。应当说明理由，例如评估注意力是按比例分配的。

**校准。**
- 引理 M 的数值例子 $g=0.3$ 没有标单位。
- 按 METR 约 7 个月的倍增时间，$g$ 约为每年 1.2。
- `checks_v44.log` 应当给出一组按此校准的结果，并标明时间单位。

**选择性取用前提。** "(X) ... is the racers' own premise" 有选择地取用了对方的前提。对方的前提里也包括"AI 会加速对齐"。只拿 (X) 而用 (U) 否定后者，只有在 (U) 有独立论证时才成立，也就是 N1。

### N11【次要】命题 27 与引理 D 的论证质量

- **命题 27 的引用。** 命题 27 用 Omohundro 2008 和 Turner et al. 2021 论证"竞赛是社会尺度的工具性趋同"。这两篇是关于优化智能体的结果，用到国家和公司身上是类比。"the meta-attractor and selection-on-cognition theories in this corpus" 是未发表的本语料，在 IASEAI 上不能当证据；双盲评审时还会暴露作者身份。建议论文版只保留选择与承诺问题这两条。
- **引理 D 的证明是文字论证。** 从"保留不看共同项"到"$q_{\mathrm I}\to1$"，还缺一步：漂移有多大、是否不可逆。gradual disempowerment 文献（Kulveit et al. 2025；Critch 2021 的 RAAPs）提供了这个机制，应当在引理 D 处直接引用，而不只是放在 §13 的文献列表里。

### N12【次要】符号、引用与附录 C 的自评

- **E3 的定义（第 1431 行）。** 写成了 "$a\,\tau_{\text{eff}}$ stays below the hard bound"。$\tau_{\text{eff}}$ 是 §1.2 的有效责任，这里应为 $\tau_c$。
- **命题 29 的引用。** 29(1) 第三点引 Theorem B(2)，那是关于背叛探测的及时性，不是裕度大小的核验。29(3) 引命题 26 来支持"无法证成"，也不对（见 N3）。
- **命名冲突。** "Lemma E0"与出口"E0"撞名。
- **§8 对 (A) 的说明。** "Fast development outside a contest is a different thing: development at the tempo of correction" 与 Theorem E(1) 矛盾：竞赛之外的快速发展同样可能跑过理解。
- **§8.1 对 Stafford et al. 的转述。** 写成 "a large enough lead lets the leader invest in safety"，不准确。他们的结果是关于落后方是否冒险、以及能力差距与敌意程度的作用。
- **命题 7(5) 第 507 行的残句**（S5），**第 528 行的引号**（S17），**第 1537 行的 K1**（S2、S17）。
- **附录 C 的自评。** S4、S5 标为"完成"，实际是部分完成；S12 标为"开放"，实际已部分完成；S15 漏列；S17 中"without relying on trust"的核对已可关闭。
- **漏引。** 全文讨论 AI control，却没有引用 Greenblatt et al. 2024。AI 2040 的引用应当逐页列出所用的补充页面：Capability Scaling Strategy、Comparing Possible Plans、Covert AI Projects、Deal Decline、Verification Plan、Plan A Assumptions、Alignment Roadmap、How Plan A solves our 5 biggest problems。

---

## 4. "竞赛并且安全"立场的 steelman 对照表（对 v4.4）

| # | 论点（最强表述与代表） | v4.4 的回应（位置） | 是否充分 | 缺什么，应如何回应 |
|---|---|---|---|---|
| 1 | **领先换安全裕度。** Aschenbrenner 2024；Amodei 2024 的 entente；AI 2027 slowdown；RSP v3 附录 A；Stafford et al. 2022 | 命题 29；§6.3；§13 | 部分 | N3：机制换成扩散加均势；最小模型 $T_p=\delta^{-1}\ln(1+\delta\Delta_0)$；AI 2040 的 Plan C 与 Plan A 对比（约 14–34%）；AI 2027 的裕度靠合并国内算力造出来；承认局部成立 |
| 2 | **Scalable oversight / debate 让人的判断随能力扩展** | 命题 26 | 不足 | N1：逐层保真度推导；obfuscated arguments；总带宽；C1–C4 |
| 3 | **AI control 是一座桥，桥上做自动化对齐研究** | 命题 26、25(2)；§6.3 表 | 不足，表格还有误述 | 承认 control 自述的适用窗口，与引理 M 一致；引 Alignment Roadmap 的 "we can't check" 和 "most load bearing"；可信与不可信的差距在 (A) 下扩大 |
| 4 | **可解释性与形式验证提高 $U$** | 未回应 | 未回应 | 覆盖率与规格充分性；用 C1–C4 判断什么算可争议；auditing game 的被抓率曲线作为 (U) 的检验 |
| 5 | **风险补偿被高估：进步也降低 $\psi_0$；框架阈值有约束力** | 命题 28 注明了 $\psi_0$ 的条件 | 部分 | N9 的一般形式与适用范围；PF v2 的 "may adjust" 表明阈值本身以对手为条件 |
| 6 | **MAIM 威慑已经稳定** | 命题 25(1)；§13 | 大体 | 补冲刺威慑条件；承认 MAIM 自己的可观测性补救；引 Abecassis 2025、Arnold 2025 |
| 7 | **投入端核算限制背叛规模（Plan A、MIRI TGT）** | Theorem B | 不足 | S9 的速率条件；Plan A 自己约 67% 的外溢估计；Scher 2026 的研究限制核查；不要再说"需要近乎完美的探测" |
| 8 | **无需协议的 pacing 均衡（Fudenberg & Koh 2026）** | 未回应 | 未回应 | N4：它支持 Theorem S(3) 和 E3；本文补上的是委托通道和透明度提供者被选择 |
| 9 | **民主一方获胜是良性的；entente 会分享收益** | 命题 27；§4.4 | 部分 | 写明价值前提；AI 2027 的裕度靠集中造出来（命题 9）；OpenAI Charter 一类承诺不可核验，可由同一机构修改 |
| 10 | **速度的收益：延迟代价巨大** | §0 的肯定式结尾；命题 17 | 不足 | N6：不可逆性的不对称；与命题 17 对齐 |
| 11 | **全球协议本身危险：锁定、监控、缺乏决策程序**（1a3orn 2026 对 Plan A 的批评） | 命题 22 末段；Definition 3 "constrains properties, not form"；§4.4 | 部分 | 把第 4 节明确用到 E0 的机构上；"缺乏争端决策程序"可以被命题 18 的限度（先联合裁决、再回应）吸收 |
| 12 | **交接给对齐的 AI 是最安全的终局（Plan A）** | §8.5 第 4 点；命题 26 | 部分 | N2：这是设计上就选择了命题 26 的第二支，交接时点由解体时钟决定；在合作下它是否致命，是一个证成问题（N1） |
| 13 | **必须身在前沿，才能制定规范、才有席位**（RSP v3 的理由："落后对安全是坏事"） | 未回应 | 未回应 | 第 4 节：席位就是转换通道 $b_{ij}$；命题 9 中控制的回报随份额平方增长；RSP v3 的这条理由本身就是命题 16 的证据 |
| 14 | **不存在决定性优势，AI 是普通技术**（Narayanan and Kapoor 2025） | Theorem A 分支 III；P2 两难；§10.7 的 P1 两难 | 大体 | 删去"E2 代价为零"（N6）；说明不具决定性时，本文仍有第 4 节和 Tier 2 的结论 |

---

## 5. 仍缺或误引的已有工作

以下各条都在 2026-10-03 检索核实过，除非另有标注。

**A. 必须定位差异（与 Theorem S、E 和第 8 节最接近）**
- Katzke, C. and Futerman, G. (2024). *The Manhattan Trap: Why a Race to Artificial Superintelligence is Self-Defeating.* SSRN 5067833，2024-12-21。同样的前提蕴含竞赛自我挫败，三条通道是大国冲突、失控、对自由民主的破坏；ASI 是 trust dilemma，而不是囚徒困境。上一轮给的 arXiv 编号没有核实到，以 SSRN 为准。
- Dung, L. and Hellrigel-Holderbaum, M. (2025). *Against racing to AGI: Cooperation, deterrence, and catastrophic risks.* arXiv:2507.21839。**本轮新增，极近。** 三条论证：竞赛的危险远超收益；获胜未必带来支配；合作与威慑是更安全的替代。
- Roussel, E., Lauwaert, L., Swoboda, T., Ramsey, G., Uuk, R., Dung, L. and Aguirre, A. (2026). *Are we Doomed to an AI Race? Why Self-Interest Could Drive Countries Towards a Moratorium on Superintelligence.* arXiv:2605.01297。失控成本足够高时，暂停符合国家自身利益。这与 Theorem S(3) 同构，必须说明本文多出了什么：二阶选择、委托、节奏。
- Fudenberg, D. and Koh, A. (2026). *Cooperating against Catastrophe.* arXiv:2609.28291，2026-09-23。结论见 N4：只有 racing、两者并存、只有 pacing 三种区域；内部能力隐藏并滞后公开时，pacing 更难维持。这是 E3 与第 5 节最近的形式化邻居。
- Scher, A., Abecassis, D., Barnett, P. and Abeyta, B. (2025). *An International Agreement to Prevent the Premature Creation of Artificial Superintelligence.* MIRI TGT，arXiv:2511.10783。E2 的条约形态。
- Barnett, P. (2026). *The Closing Window: How Governments Could Lose Their Ability to Restrain Advanced AI.* arXiv:2608.05173。**本轮新增。** 治理层面的"不可回头点"：硬件扩散、算法进步、危险模型发布。直接对应引理 1，以及推论 2 的"必须在锁定之前"。
- Scher, A. (2026). *Verifying Restrictions on Frontier AI Research.* arXiv:2606.28694。**本轮新增。** 列出 28 种研究限制的核查机制，对应 E2 的验证和 Plan A 的 titration。
- Barnett, P. and Scher, A. (2025). arXiv:2505.04592。本轮未复核。
- Aguirre, A. (2025). *Keep the Future Human*；Yudkowsky, E. and Soares, N. (2025). *If Anyone Builds It, Everyone Dies.*

**B. 威慑**
- Hendrycks, Schmidt and Wang (2025)：本文已引，但应写明三个支柱，以及他们自己提出的可观测性补救。
- Abecassis, D. (2025). *Refining MAIM: Identifying Changes Required to Meet Conditions for Deterrence.* MIRI，2025-04-11。
- Arnold, J. R. (2025). *Superintelligence Deterrence Has an Observability Problem.* AI Frontiers，2025-08-14。
- Hatz, S. (2025). *The Nuclear Analogy in AI Governance Research.* arXiv:2510.21203。只在检索结果中见到，未读，供 §10.7 参考。

**C. 竞赛模型与实验**
- Stafford, Trager and Dafoe (2022)：已引，但需修正转述（N12）。
- Emery-Xu, Park and Trager (2024), *Journal of Conflict Resolution.*
- Fernández Domingos, E. and Han, T. A. (2026). *Falling Behind Drives Unsafe Development in an Idealised AI Race Experiment.* arXiv:2607.26034（已核实存在）。
- Konrad, K. (2009). *Strategy and Dynamics in Contests*：挫败效应，用于 N3。
- Naudé and Dimitri (2020).

**D. 监督与控制（本文讨论了，却没有引用）**
- Greenblatt, Shlegeris, Sachan and Roger (2024). AI Control. *ICML.*
- Irving, Christiano and Amodei (2018), Debate；Barnes (2020) 关于 obfuscated arguments 的报告；Khan et al. (2024)；Kenton et al. (2024)。
- Burns et al. (2023), Weak-to-strong generalization；Christiano et al. (2018), IDA；Leike et al. (2018), recursive reward modeling。
- Marks et al. (2025), auditing language models for hidden objectives；Dalrymple et al. (2024), Towards Guaranteed Safe AI。
- Parasuraman and Manzey (2010), automation complacency and bias；Bainbridge (1983), Ironies of Automation。

**E. 前沿安全框架与承诺（作为证据，正文不点名，列入参考文献）**
- Anthropic RSP v3.0（2026-02-24）及其附录 A；之后已有更新版本，引用时注明所用版本。
- OpenAI Preparedness Framework v2（2025-04-15）。
- Google DeepMind Frontier Safety Framework v2（2025-02）。
- OpenAI Charter（2018）。

**F. 危险期、理解的增长、不可逆性**
- Sagan (1994)；Ord (2020)；Thorstad (2022), Existential risk pessimism and the time of perils：引理 M 的 "time of perils" 应当引用它们。
- Bloom, Jones, Van Reenen and Webb (2020), *AER*：支持 (U)。de Solla Price (1963)：反面证据。
- Arrow and Fisher (1974)；Henry (1974)：用于 N6。

**G. 趋势与证据**
- Kwa et al. (2025, METR) 任务时长的倍增；Ho et al. (2024, Epoch) 语言模型的算法进步。
- International AI Safety Report (2025, 2026)。

**H. 对 Plan A 与 entente 的已有批评（非正式，但直接相关）**
- 1a3orn (2026). *AI 2040: Is it actually a deal?* LessWrong，2026-07-20。论点是 MACD 之下缺乏事前的争端决策程序，并有监控风险。
- Tegmark (2024) 对 entente 的批评。

**I. 误引**
- §8.1 对 Stafford et al. 的转述（N12）。
- Ashby 1956 用来支持 (U) 是双刃的（N1）。
- "Lemma C"出自论证评审的叫法，可以保留，但正文应指明它对应命题 26 的哪一部分。

---

## 6. 应当保留的部分

1. **Theorem E 的结构。** E3 是常设条件；长期生存要求 E0 或共同的 E1；E2/E3 让路保持敞开。这是本文最有价值的结构性洞见。按 N4 补上"E2 线低于 $s^\ast$"之后，它会成为"世界必须合作"最难反驳的形式。
2. **命题 7(3) 的 $e^{a\tau_c}$ 稳健性下界。** 配上 N8 的 METR 校准（倍增 7 个月、时滞 12 个月时，容忍度约 0.30），会是论文里最让人坐直的一个数字。
3. **命题 9–11 的二阶选择与速率条件 $g/(1+\eta)$。** 可以与 N1 新推出的"逐层监督误差须以约 $1/(gt)$ 下降"并列，组成"纠错必须追得上"的一对速率定理。这是本文相对 Manhattan Trap、Roussel et al.、Fudenberg & Koh 真正新的部分。
4. **命题 28 的风险补偿。** 按 N9 给出一般形式和适用范围。
5. **Remark 5 的保守报警与"上界必须来自场外"。**
6. **§8.5 对 Plan A 合作要素的肯定，以及它自己留下的那道门**（"relying on trust may be the best option"，与推论 2、Theorem S(3) 收敛）。按 N2 换成三条件判据之后，这一节会既公平又致命。
7. **推论 1："降低赢的价值是唯一同时放松所有约束的杠杆"。** 这是与 Plan A 作者最可能形成共识的地方。
8. **命题 21：冻结份额的暂停可能完成捕获。**
9. **§10.7 核武器的四点差异。** 按 N4 与推论 3(3) 对齐之后，冷战就成了 E2 的证据，而不是反例。
10. **一组诚实修复：** 命题 6(5)–(6)、命题 24 的修复和 L6 的去免疫化。它们让对手看到本文没有在挑参数。
11. **"P2 两难"一句：** "No race is both fast enough to be worth running and slow enough to be corrected." 修完 N1 之后，可以作为论文的标题句备选。
12. **§10.4 的"改变结构与选择环境，而不是反对任何行动者"。**

---

*评审人说明：本评审由 Claude（Opus 5.5）以 IASEAI 程序委员会中 AI 安全与治理从业研究者的视角撰写。网页引文经抓取工具处理，标为"原文"的句子投稿前须对原页逐字核对。N1 中的逐层保真度推导和 N3 中的最小领先模型是评审人的建议，不在仓库的检查脚本中，采用前应加入 `checks_v44.py` 复核。*
