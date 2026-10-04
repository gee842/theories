# R-v6.1 评审：证据与引文

*对象：`v6.1/` 的 THEORY.md（sha256 前缀 242a61240d810e51，已核对）、SUPPLEMENT.md、DISCUSSION.md、EVIDENCE.md（EV1–EV17）、LEDGER.md、CHANGELOG.md。对照 `../v6/reviews/R-v6.0-evidence.md`。评审者是 Claude（Opus 5.5），与起草者同属一个模型家族（见第四节）。今天是 2026-10-04。*

*核对方式分两种。【联网】：取得原文或出版方页面。其中 Jones 2024 和 NBER w35276 两篇下载了 PDF，抽取全文后逐句检索。【书目】：凭书目知识核对，未联网，书目细节有把握，但没有逐字核对原文。*

---

## 一、总判断

1. **上轮的修补大多落实，没有发现编造的文献。** 上轮唯一的【致命】项已修好，Amodei 文章的 stick 与 carrot 现在逐字引用，§8.3(d) 也照写。§9.6 先例表的四处问题、Engels 的"推算"、Kydd 的"act as"、ARCHES 的"follows from"都已改正。
2. **本轮没有【致命】项，有六个【重要】项，分三类。**
   - **一处新引入的误引。** 上轮要求把贴现结论从 Fudenberg & Koh 撤下，v6.1 改挂到 Jones (2024)，但 Jones 的原文并不支持"贴现准则偏好必然灾难的竞赛"。他的结论恰好相反：效用一旦有曲率，规划者就会停下。
   - **证据过时。** 截至 2026 年 10 月，有四组证据已过时，而且其中好几处正好削弱正文的说法：
     - "前沿未曾易手"如今有一份权威来源与之相反；
     - 两个领先国家都没有背书最新的军事 AI 宣言；
     - 一个领先国家投票反对联合国科学小组的任命；
     - 开发者及其背后资本在规则上的政治支出，已经是 T4 的直接证据。这部分支出也包括起草模型的开发者自己的支出，按登记的利益披露原则应当记录。
   - **证据强度在正文被说过头，参考文献的机制也有缺陷。** T5 的状态写成"Supported"，T2 被推广到所有书面承诺。参考文献方面，xref 脚本只检查单向，而且姓氏会撞键，导致正文引用的 Maynard Smith & Szathmáry 1995 在 THEORY 文献表中缺失，检查却报告"all cited works listed"。
3. **† 文献全部真实存在，转述大多准确。** 优先核对的八项中：
   - Duersch–Oechssler–Schipper（S5 的措辞）、判别核、Copeland、Hanahan & Weinberg、Kydd、ARCHES 六项的转述准确；
   - Jones 2024 的用法有误；
   - Caulin & Maley 的因果句需要加限定，并补上 2025 年的反证。

---

## 二、发现

### 【致命】

无。

### 【重要】

#### I1 Jones (2024) 被用来支持它没有说过的结论

**位置。**
- THEORY §8.1："a discounted criterion can favour a race that ends in catastrophe with certainty when the hazard it adds is below the growth it adds (Jones 2024)"；
- §8.4 与 DISCUSSION X8 "Where the criteria disagree" 中，同一句话没有加引注；
- SUPPLEMENT S8 "*Discounting*"："a race is preferred iff $h<g_r-g_p$, though it ends in catastrophe with certainty (Jones 2024)"；
- EVIDENCE EV11 与 LEDGER §3 都写"attributed to Jones (2024) alone"。

**依据（【联网】，NBER w31837 全文）。**
- Jones 的简单模型是静态的，规划者只选使用 AI 的强度 $T$。最优条件是 $\delta\,v(c)\le g$（式 1），其中 $v(c)=u(c)/(u'(c)c)$，是一年生命价值与人均消费之比。
- 当 $\gamma\ge1$ 时 $v(c)$ 随消费上升，所以规划者会在有限的 $T^\ast$ 停下。Table 1 与 Key Points 1–2 给出的数字是：
  - 对数效用下，40 年、累计风险约 1/3；
  - $\gamma=2$ 时，4.5 年、累计风险约 4%；
  - $\delta=2\%$ 时，立刻关停。
- "风险低于增长就一直跑下去，直至必然灾难"只出现在效用对消费线性（$v\equiv1$）的特例里。原文对此只有一句旁注 "with linear utility, v(c) would equal one"。
- 原文里没有"竞赛与配速"的比较，也没有 $h<g_r-g_p$ 这一条件。
- Key Point 5 说的是：在 AI 不改善死亡率时，贴现越低，可接受的一次性风险越接近零。

所以 §8.1 把"贴现准则"整体描述为会偏好必然灾难，在 Jones 自己的模型里，对标准曲率并不成立。

**修法。**
- §8.1 改为："…and under discounted expected utility the acceptable existential risk depends sharply on the curvature of utility: with log utility a planner accepts about a one-in-three cumulative risk for a 55-fold gain in consumption, with stronger curvature about 4% (Jones 2024); only if utility is linear in consumption is a course preferred whenever the hazard it adds is below the growth it adds, though it ends in catastrophe with certainty (S8)."
- §8.4 与 X8 的同一句加上 "linear in consumption"。
- S8 写明 $h<g_r-g_p$ 是本文的推导，并注明它相当于 Jones 式 (1) 在 $v\equiv1$ 时的特例；保留 Key Point 4（死亡率改善提高可接受风险），补上 Key Point 5。
- 文献条目补页码 6(4):575–590。
- EV11 与 LEDGER 的相应句子一并改。

#### I2 "前沿未曾易手"如今有相反的权威来源；决定性的证据整体过时

**位置。** THEORY §7.2 "though the frontier has not changed hands"；§7.3 表的 Decisiveness 行；EV5 的来源与 Reading；C5。

**依据（【联网】）。**
- 2026 年 AI Index（2026-04-13）写道，两个领先国家的模型性能差距 "has effectively closed"。在 Arena 榜上，自 2025 年 2 月起两国模型 "traded the lead multiple times"，2026 年 3 月最佳模型之间只差 2.7%（[TNW 转述](https://thenextweb.com/news/stanford-ai-index-2026-china-us-performance-gap)）。
- EV5 只引了 Epoch 按 ECI 的口径（2026-01，平均落后 7 个月，前沿一直在同一国），没有记录这份相反的口径。
- Epoch 2026-05-29 更新：自 2026 年 1 月起，开放权重模型平均落后 4 个月，约 8 个 ECI 点，比 EV5 引的 2025 年 10 月的 3 个月略宽（[Epoch](https://epoch.ai/data-insights/open-closed-eci-gap)）。
- METR 的时间跨度页面（2026-05-08 更新）注明 "Measurements above 16 hrs are unreliable with our current task suite"（[METR](https://metr.org/time-horizons/)）。EV5 和 §5.3 拿来证明"capability growth is measured"的主要序列，对最前沿的模型已经碰到量程上限。

**修法。**
- §7.2 改为 "…though by one composite index the frontier has stayed with developers in one state, while on a preference leaderboard the top position has been matched and the gap is now a few per cent (EV5)"。
- §7.3 表的 Decisiveness 行同样改。
- EV5 补上以上三条来源，Reading 改为："领先是否易手取决于口径；无论用哪种口径，领先都短，这一点不利于 (decisive)。"

结论不变，甚至更强：领先短，不利于决定性。但"未曾易手"不能再作为单一事实来写。

#### I3 军事 AI 文件与联合国科学小组：对称的记录已经可以取得，结果削弱了正文所说的"种子"

**位置。**
- THEORY §11.4 "Where things stand"：Stage 1 的种子是 "an international scientific assessment and a UN scientific panel"，Stage 2 的种子包括 "multilateral declarations on military uses of AI"；
- §7.3 表的 T6 行；
- EV8（军事 AI 一条仍是"From prior knowledge… signatory lists to be checked"）；
- EVIDENCE 缺口第 12 条。

**依据（【联网】）。**
- 联大第 79/239 号决议（2024-12-24）：159 票赞成，两个领先国家都投赞成（[UN-project](https://un-project.org/votes/resolution/A-RES-79-239/)）。
- 第 80/58 号决议（2025-12-01）：167–5–5，一个领先国家投反对票，另一个投赞成票（[UN-project](https://un-project.org/votes/resolution/A-RES-80-58/)）。
- REAIM 2026《Pathways to Action》（A Coruña，2026-02-04/05）：34–35 国背书，**两个领先国家都没有背书**（据路透社 2026-02-06 的报道）。
- 2026-02-12 联大以 117–2–2 任命科学小组 40 名成员。投反对票的一个领先国家称小组及全球对话是 "a significant overreach of the UN's mandate and competence"；另一个领先国家要求把能力建设作为核心议题（[UNRIC](https://unric.org/en/general-assembly-appoints-artificial-intelligence-panel/)）。EV8 只写了 2025 年 8 月设立时的协商一致。
- 科学小组 2026-07-01 发布初步报告，结论是安全措施落后于能力；首届全球对话于 2026-07-06/07 在日内瓦举行（据报道，未读原文）。这比 EV7 引的 2026 年 2 月 IASR 更新。
- 世界人工智能合作组织（2025-07-26 提出）已核实（[上海市政府](https://english.shanghai.gov.cn/en-WAICLatest/20250726/54fe55779ead485a8d71fafc68ff6c42.html)），EV8 可以去掉 "not retrieved"。

**问题。**
- 正文 T6 一行只记录了一个国家"拒绝有约束力的约束"，却没有记录两个领先国家同时拒签最新的军事 AI 宣言。
- 正文把联合国科学小组算作没有争议的种子，却没有提到任命它时的反对票。

两处都违反登记自己定的"同一标准"。

**修法（只写角色）。** §11.4 改为："Stage 1 has seeds in an international scientific assessment and a UN scientific panel, whose appointment one leading state opposed as an overreach; Stage 2 in an affirmation of human control over nuclear use and a bilateral dialogue with an incident channel, while the most recent multilateral declaration on military AI was endorsed by neither leading state and the most recent General Assembly resolution on it was opposed by one…"。T6 行补上一句 "both leading states declined the latest multilateral declaration on military AI"。EV8 按文件逐条列出两国的表态；缺口第 12 条改为已填。

#### I4 T4/EV4：最缺证据的一环，现在已有直接证据，并且涉及起草模型的开发者

**位置。** EV4（"No source was retrieved in the v5 pass"）；THEORY §7.3 T4 行（"Gap: mechanism proved, channels not measured"）；§7.3 末段；缺口第 2 条。

**依据（【联网】，报道层面）。**
- 一个由行业资本支持的超级 PAC 网络在 2025 年筹得逾 1.25 亿美元，主张宽松规则和联邦优先（[Semafor](https://semafor.com/article/02/12/2026/anthropic-donates-to-super-pac)；另见 [Bloomberg Government](https://news.bgov.com/private-equity/andreessen-horowitz-fuel-ai-industrys-51-million-midterm-haul)）。
- 一家开发者于 2026-02-12 向一个主张安全监管、支持出口管制、反对联邦优先的超级 PAC 捐出 2,000 万美元（[Semafor](https://semafor.com/article/02/12/2026/anthropic-donates-to-super-pac)）。这家开发者就是起草模型的开发者。
- NBER w35276 §6.3（【联网】，全文）指出：要求有约束力的共同规则，"need not be read only as public-spirited restraint or as regulatory capture"，因为共同约束可以改变对手的激励，从而对提出者本身有利。

**问题。**
- 这些都是"成功再投入到对规则的影响"的直接例子，而且两个方向都有。
- 登记头部写明 Anthropic 的声明"held to the same standard"。按这一原则，起草方开发者的政治支出必须记录。

**修法。**
- EV4 两个方向并列登记，并按本文自己的变量分类：哪些影响是可占有的（$\chi>0$，例如有利于领先者的出口管制），哪些不可占有。不按支出方声明的目的分类。
- T4 行改为 "Partly evidenced: large political spending by developers and their backers on both sides of rule-making (EV4); scaling with share not tested"。
- 头部的利益披露补一句：EV4 包含起草方开发者的支出。

#### I5 正文对证据强度说过头：T5、T2，以及"书面承诺已按对手设定"

**位置与问题。**
1. **§7.3 T5 行。** 状态是 "Supported by the structure of the harms"，登记栏写 EV5、EV7。
   - EV5 讲的是能力增长，EV7 讲的是纠错不完整，都没有触及"共同伤害未进入决策"。
   - 缺口清单里也没有 T5。
   - 结构推理不是证据。应改为 "Argued from the structure of the harms; not measured; some harms do return (EV13 for propagation)"，并在缺口中补上 T5。
2. **§8.3(b)、DISCUSSION X8 与 §7.3 T2 行。** "written commitments are already set relative to rivals and revised mostly toward weakening (EV2)"。
   - 按对手设定这一点，证据只是两家开发者的框架条款。
   - "大多削弱"只来自一篇单作者、未经同行评议的预印本（Zhu 2026，只读了摘要，我已核实摘要数字无误）。
   - 应改为 "two developers' frameworks condition commitments on rivals; one unreviewed study codes 77% of traced changes across twelve developers as weakening (EV2)"。
3. **EV2 的 "Strong support for T2"。** T2 的前提是"对手推进时加速或放松保障"，而条款只是许可，并非已经行使的决定（EV2 自己的 Uncertainty 也这样写）。应改为 "support at the level of written commitments, not of conduct"。
4. **EV2 的反证栏漏了两条。**
   - RSP 3.1 版（2026-04-02）明确写 "we remain free to take measures such as pausing … in any circumstances in which we deem them appropriate"。这是保留的裁量权，不是承诺，但应当与"暂停措辞被删除"一句并列。
   - RSP 现行版本是 3.4（2026-07-08 生效，[更新页](https://www.anthropic.com/rsp-updates)）。EV2 的引文要对照现行版本重新核对。
   - 另外，NBER w35276 的脚注 9 把 RSP 3.0 的修订读作"承诺问题"，可以作为独立的佐证。

#### I6 引文机制：一条正文引用无法解析，检查脚本却报告全部通过

**位置。** THEORY 文献表；DISCUSSION 文献表；`xref_v61.py` 与 `src/refs_v61.py` 的 CIT 正则。

**问题（自写脚本 `SCRATCH/cites.py`、`cites2.py` 双向核对）。**
- THEORY §3.6 引用了 "Maynard Smith and Szathmáry 1995"，但 THEORY 文献表里没有这一条，却列了正文没有引用的 "Smith, H. 1995. *Monotone Dynamical Systems*"。原因是正则把 "Smith and Szathmáry 1995" 的键算成 (Smith, 1995)，恰好撞上 Hal Smith。refs_v61.py 为 ('Maynard','1995') 改好的 W. H. Freeman 条目因此从未进入文献表，这是从 v6.0 退化来的（v6.0 THEORY 第 3211 行原本有这一条）。
- DISCUSSION 文献表列了 Acemoglu, Egorov & Sonin 2012，正文没有引用。它是因为与 Acemoglu & Robinson 2012 撞键才被收进来的。
- THEORY 与 DISCUSSION 都列了 Schelling 1966，正文都没有引用。SUPPLEMENT 里 Schelling 1966 出现了两次。
- xref 只检查"引用 → 文献表"这一个方向。CHANGELOG 的 "every citation listed" 因此是一个它无法保证的断言。

**修法。**
- THEORY 文献表补上 "Maynard Smith, J. and Szathmáry, E. 1995. *The Major Transitions in Evolution*. W. H. Freeman."，删去 H. Smith。DISCUSSION 删去 Acemoglu–Egorov–Sonin。Schelling 1966 或者删去，或者在正文引用。
- 两个脚本的键改为（第一作者，第二作者或 et al.，年份），并加上反向检查。

### 【次要】

1. **§8.3(c) 误读了 Bueno de Mesquita, Dziuda & Polborn (2026)。** 【联网】全文 Prop. 9 与 Cor. 1 讲的是：先行承诺略低速度的企业（Stackelberg 意义上的 leader）可以获益，因为对手随之减速，而且这是局部结果。文中没有"能力领先者"，也没有"a large lead can discourage a follower"。改为 "a developer able to commit first to a slightly slower speed gains, because rivals slow too (Bueno de Mesquita, Dziuda and Polborn 2026)"；"large lead discourages" 改引 Harris & Vickers 1987 与 Konrad & Kovenock 2009（X8 已经这样引）。
2. **X8 "Deterrence and prevention" 把 Abecassis 2025 当作 MAIM 的 best case 来引。** 【联网】该文是对 MAIM 的批评：红线不清、无法监测，破坏威胁的可信度存疑。应改放到 *What remains*。
3. **X2 "Cells" 的 "because suppression scales with size"。**
   - Caulin & Maley 2011 提出的是假说性解释。
   - Butler et al. 2025（*PNAS*，"No evidence for Peto's paradox in terrestrial vertebrates"，【联网】据大学新闻稿）发现，较大的物种肿瘤患病率确实较高，只是升幅远低于细胞数的倍数；体型演化较快的谱系风险较低。
   - 改为 "large animals show far less cancer than their cell numbers would predict, plausibly because suppression evolved with size (Caulin and Maley 2011), though prevalence still rises somewhat with size (Butler et al. 2025)"。论点"增长不是断层线"不受影响。
4. **先例的措辞（任务 5）。**
   - **X11 ABM 行。** "reduced the offensive race" 说过了头。条约去掉的是进攻扩张的一个动因，而多弹头没有受限，战略弹头在 1970 年代仍成倍增加。宜改为 "removed one driver of the offensive race; warheads still multiplied through multiple warheads, which were not limited"。同一行 *What it shows* 列把有争议的退约动机当成了结论，应加 "if"。
   - **THEORY §11.5 把三个先例的限制条件删掉了，而这三处恰好都是与 AI 不可类比的地方。** DISCUSSION 都写了：BWC 被单方面放弃，部分原因是军事价值低，且放弃方另有核替代；蒙特利尔议定书成立时替代品已经可得，"a low value of winning"；核电的 "later lapses"。§11.5 各补半句即可。
   - **Outer Space/Seabed 两条约。** 排除的只是在轨道和海床部署大规模杀伤性武器，太空的军事利用仍在继续。"A domain kept out of the contest" 宜改为 "a class of weapons kept out of a domain"。
   - **"The first nuclear monopoly" 一行。** Trachtenberg 写的是垄断结束后的优势期（1949–54），预防战争的争论也集中在这一时期。行名宜改为 "The first nuclear monopoly and the period of superiority (1945–54)"。
   - **§11.3 与 X11 的 1983 年预警事件。** 仍然没有出处（上轮已提）。
   - 其余日期、行动者与结果都准确：Acheson–Lilienthal 与 Baruch 均为 1946 年；PTBT 1963；BWC 1972；ABM 1972/2002；INPO 1979；蒙特利尔 1987/1990，贸易措施见于 1987 年文本，多边基金由 1990 年修正案设立。
5. **X10 全球最低税。** 2026-01-05 包容性框架通过 "side-by-side" 安排，使一个领先国家的母公司集团基本豁免 IIR/UTPR（[EY](https://taxnews.ey.com/news/2026-0115-breaking-tax-news-oecd-releases-side-by-side-arrangement-exempting-us-multinationals-from-most-pillar-two-global-minimum-tax-rules)）。比起 "leakage where coverage is incomplete"，这更贴近本文 D5 与 §9 "Coverage can unravel" 的情形，即最大的参与者拿到豁免。宜照此改写，只写角色。
6. **EV3 过时。**
   - 2026-01 设立了诉讼工作组。2026-04 一家开发者起诉某州的 AI 法，联邦行政部门介入，法院于 4 月 27 日暂停该法的执行（【联网】，律所通报）。EV3 的 "Next measurement: outcomes of pre-emption litigation" 已经有了第一个结果，应当登记。
   - 英国机构改名为 Security Institute，与 T3 的"依赖被监督者"没有直接关系，应说明它在 T3 中的作用，或者删去。
7. **EV9 与 §11.3 的"每八个月翻倍"。** Ho et al. 2024 的 90% 区间是 2–22 个月（【联网】，NeurIPS 2024 摘要），"2.5–3× a year" 只是中心值。正文应补一句区间，并注明这是 2012–2023 年的预训练数据。
8. **EV1 同类对同类仍有残缺。**
   - 开发者一栏，竞争性的声明只有起草方开发者 CEO 的一篇，另一家开发者只出现在合作一侧。可以补上：
     - 两家开发者对 2025 年 3 月同一份 RFI 的提交（【书目】，未检索）；
     - 另一来源国 17 家开发者 2024 年 12 月的安全承诺（[ETO Agora](https://agora.eto.tech/instrument/1831)，【联网】）。
   - 国内战略文件一栏，一方是 2025 年的文件，另一方是 2017 年的文件，时间上不对等。应补国发〔2025〕11 号《关于深入实施"人工智能+"行动的意见》（2025-08，含"全球合作"行动，【联网】），两面都要记录。
9. **SUPPLEMENT S5 关于 Duersch–Oechssler–Schipper 的措辞准确**（【联网】，arXiv:1003.4274 与 GEB 76(1):88–96）。原文讲的是 imitate-if-better 规则；结论是，当且仅当相对收益博弈为广义石头剪刀布型时，模仿会被"money pump"；只适用于对称两人博弈。S5 说 "concern a dynamic imitation rule… rock–paper–scissors games are covered once mixed imitation is allowed"，是正确的。应删去 "(the wording of that citation is to be checked against the source)"，补页码，并删去 CHANGELOG "Not done" 中的这一项。
10. **判别核的引用正确**（【联网】，书目：Annals of the ISDG vol. 4，pp. 177–247）。Definition 8.1 的"∃ 非预期策略、∀ 扰动"与判别核的定义一致。建议同时引概念的原始出处：Cardaliaguet 1996, *SIAM J. Control Optim.* 34(4):1441–1460（【书目】）。
11. **书目格式。**
    - Copeland "2000b" 没有对应的 2000a，应改为 2000，并补 25(2):187–212。
    - Leonard 2009 的标记写成了 "† (title seen; journal details not checked) ‡"。这是 refs_v61.py 中 `mark()` 的正则只剥离行尾 "†" 造成的。应改为 ‡，补 *JEBO* 71(1):37–51（上轮已提）。
    - Fuhrmann & Kreps 的全题应为 "…: A Quantitative Empirical Analysis, 1941–2000"，补 54(6):831–859。条目中的 "not retrieved" 与正文的 "unchecked" 现在都可以删去。
    - Larsen et al. 补首字母，"E10" 改为 "EV10"。
    - 补 arXiv 号：Hendrycks, Schmidt & Wang 2503.05628；Marks et al. 2503.10965；Kulveit et al. 2501.16946（另补副题与 ICML 2025 position track）。
    - 补出处：Güth & Yaari 1992 收于 Witt (ed.)，U. Michigan Press；Snyder 1965 收于 Seabury (ed.)，*The Balance of Power*。
    - 补出版者：Ikenberry、Jervis 1976、Mearsheimer、Weibull、Osgood、Bundy、Leitenberg & Zilinskas 等。
    - 统一标记写法："‡ (abstract)""‡ (full text)""† (not retrieved)" 混用。
    - 正文两处标签重复："Proposition Proposition 9.2"（§8.3(b)）、"Theorem Theorem 10.5(3)"（§9 表 R1）。
    - TESTS 引用的 Khan et al. 2024、Kenton et al. 2024 不在任何文献表里。
12. **小的转述问题。**
    - Prop. 5.15(1) 的"零和则无信息"是标准推论，不是 Crawford & Sobel 原文的命题，宜写 "compare"。
    - Prop. 3.6(3) 的 "at $r=1$ the prize is fully dissipated (Schaffer 1988)"：Schaffer 给的是有限群体 ESS 这一概念，Tullock 竞赛完全耗散的结论应补 Hehenkamp, Leininger & Possajennikov 2004, *EJPE* 20(4)（【书目】）。
    - §6.1 引 Gabriel 2020 支持"集体问题而非感知错误"，二者契合较弱，宜写 "compare"。
13. **上轮未落实的原始出处。**
    - 12 月行政令仍然引律所摘要。
    - 超级智能对话仍然引报道。白宫情况说明书现已可取得（[whitehouse.gov](https://www.whitehouse.gov/fact-sheets/2026/09/fact-sheet-president-donald-j-trump-advances-a-fair-and-reciprocal-relationship-with-china-while-hosting-historic-state-visit/)），"cannot be allowed to drift toward global governance" 出自该国 OSTP 主任，已核实。
    - 宕机事故的损失估计仍是二手来源。
    - CLAIMS §7 把 "Evidence asymmetries and citation errors" 标为 "Repaired"，应改为 "Partly repaired"，并列出 I1–I6。
14. **EV6 的两条"to be checked"现已可核实。** Palisade 的研究是 arXiv:2509.14260，MacDiarmid et al. 是 arXiv:2511.18397。EvalDetectBench（arXiv:2609.01611，2026-06-08）也已核实，可以去掉 "title seen, not read"。

---

## 三、做得好、不应改动的地方

1. EV1 按三类来源、每类两面的结构；Amodei 的引文逐字准确；§8.3(d) 把 stick 和 carrot 一起写，是该策略最强的版本。
2. EV2 用 RSP 原文作主证据，OpenAI 条款写全，并把"向上看齐"条款列入反证。
3. 凡是解读都标明是解读：EV8 的 "this register's interpretation"、Hart–Zingales 的 [interpretive]、ABM 的 "matter of interpretation"。
4. Engels 写作 "derived"；Fernández Domingos & Han 注明 exploratory；Fudenberg & Koh 标明只读了摘要。
5. 引理 3.10 及其推论收窄为"全局且不可逆的失败须预先整合；可逆的失败可以多中心试错"，与思想史相符。
6. 缺口清单把饱和 (unsaturated) 与 (decisive) 分开登记，另有 "What the register cannot yet support" 一段。
7. X11 先例表对上轮四处问题的修正：Baruch 与 Acheson–Lilienthal 分写；核垄断一行删去 P3；NPT 一行拆开；蒙特利尔写到 1990 年修正案。
8. 正文没有点名任何国家或企业（xref 与我的抽查都确认），本报告建议的改写也都只写角色。

---

## 四、核对了什么，没有核对什么

### 上轮修补逐项（对照 EVIDENCE 末尾的更正清单与 LEDGER §3）

| 上轮项 | 判断 | 说明 |
|---|---|---|
| F1 Amodei 的 stick 与拒止 | 已落实 | EV1 逐字引用；§8.3(d)；T1 行不再写复数的 "developers' statements" |
| I1 EV1 同类对同类 | 大部分落实 | 三栏两面已经齐全。开发者一栏与时间对等仍有残缺（次要 8） |
| I2 OpenAI 条款写全、RSP 原文 | 已落实 | RSP 已更新到 3.4，反证需补（I5） |
| I3 饱和与"可以挽回" | 已落实，但已过时 | 已按上轮意见修好。新的相反来源见 I2 |
| I4 Engels 的数字是推算 | 已落实 | §6.5 |
| I5 §9.6 先例表四处 | 已落实三处半 | 1983 年事件仍没有出处；新发现的措辞问题见次要 4 |
| I6 拒绝有约束力约束的主语、对方的主张、军事 AI 文件 | 部分落实 | 主语改为一国官员，已落实。对方的主张仍写 "not retrieved"（现已可核实）；军事 AI 的签署情况未核（见 I3） |
| I7 引理 3.10 的推论 | 已落实 | Price 1972 与 Hamilton 1975 已改引 |
| 次要 1 Kydd 的 "act as" | 已落实 | |
| 次要 2 补免疫编辑的出处 | 已落实 | Hanahan & Weinberg |
| 次要 3 挤入 | 已落实 | 写在 EV14；正文 §5.4 已不再主张挤出 |
| 次要 4 "an early defence"、[interpretive] | 已落实 | |
| 次要 5 Zhu、IASR、FDH 措辞；状态升级 | 已落实 | |
| 次要 6 ARCHES 写 "follows from"；新意重叠 | 已落实 | X1 |
| 次要 7 撤回 "power-seeking emerges" | 已落实 | |
| 次要 8 V1 的悬空引用 | 已落实 | |
| 次要 10 Aghion 等 2019 | 已落实 | 已删去 |
| 次要 11 思想史文献 | 部分落实 | Huxley、严复、Schwartz 已补；修昔底德、墨子、康有为未补，这三处只点名、没有年份，可以接受 |
| 次要 12 书目项 | 部分落实 | Anderson、Hofstadter、Alger、行动计划题名已改。Maynard Smith & Szathmáry 因撞键退化缺失（I6） |
| 表中其余各项：Caulin & Maley 的因果句 | 未落实 | 次要 3 |
| 表中其余各项：Leonard | 未落实 | 次要 11 |
| 表中其余各项：Copeland a/b | 未落实 | 只剩 "b"，次要 11 |
| 表中其余各项：Duersch 页码 | 未落实 | 次要 9 |
| 表中其余各项：行政令与对话改引原始出处 | 未落实 | 次要 13 |
| 表中其余各项：Fudenberg & Koh 贴现命题 | 撤下了，但改挂到 Jones，属于误引 | I1 |

### 核对表

#### 优先八项

| 文献 | 状态 | 说明 |
|---|---|---|
| Duersch, Oechssler & Schipper 2012 | 已核实【联网】 | GEB 76(1):88–96。S5 的措辞准确（见次要 9） |
| Cardaliaguet, Quincampoix & Saint-Pierre 1999 | 已核实【联网】 | pp. 177–247；判别核的用法正确（见次要 10） |
| Copeland 2000b | 已核实【联网】；格式有误 | IS 25(2):187–212；"b" 应删去。2000a 已不再被引用 |
| Jones 2024 | 书目已核实【联网】；用法有误 | AER: Insights 6(4):575–590（见 I1） |
| Hanahan & Weinberg 2011 | 已核实【联网】 | *Cell* 144(5):646–674。三项转述（抑制生长信号的逃逸、招募微环境、免疫逃逸）都在原文中；免疫逃逸属于 "emerging hallmark" |
| Caulin & Maley 2011 | 书目已核实；转述需加限定 | 见次要 3 |
| Kydd 1997 | 已核实【联网】 | *World Politics* 49(3):371–400；"act as" 正确 |
| Critch & Krueger 2020（ARCHES） | 已核实（上轮【联网】） | "follows from" 正确 |

#### 其余 † 文献（共约 107 条）

- **有误或需要补全：**
  - Fuhrmann & Kreps 2010：题名不全（次要 11）；
  - Leonard 2009：标记写错（次要 11）；
  - Güth & Yaari 1992、Snyder 1965、Aumann 1990：缺出处；
  - Kulveit 2025、Hendrycks, Schmidt & Wang 2025、Marks 2025：缺 arXiv 号（以上均为【联网】或【书目】核实）；
  - Gabriel 2020、Crawford & Sobel 1982：书目无误，用法宜写 compare（次要 12）。
- **【联网】已核实：** Kulveit et al. 2025、Hendrycks, Schmidt & Wang 2025、Marks et al. 2025（arXiv:2503.10965；3 支有权访问训练数据的队伍成功，仅有黑盒权限的 1 支失败）、Fuhrmann & Kreps 2010、Hanahan & Weinberg、Kydd、Copeland、Cardaliaguet et al.。
- **【书目】已核实**（书目要素与转述均无误，未逐字核对原文）：
  - **国际关系与战略：** Abbott et al. 2000；Jervis 1976、1978；Fearon 1995；Fey & Ramsay 2007；Powell 1991、2006；Glaser 1994/95、2010；Gilpin；Waltz；Walt；Wendt 1992、1999；Wohlforth；Ikenberry；Kindleberger；Deutsch；Debs & Monteiro；Coe & Vaynman 2015、2020；Nye 1987；Snyder；Schelling；Osgood；Posen；Van Evera；Scharre；Bundy；Burr & Richelson；Rosenberg 1983；Leitenberg & Zilinskas；Mearsheimer。
  - **经济学与博弈论：** Arrow & Fisher；Arthur；Campbell；Goodhart；Dal Bó；Stigler；Laffont & Tirole；Olson；Kamenica & Gentzkow；Tennenholtz；Weibull；Crawford & Sobel；Alger et al. 2020；Baye et al.；Bloom et al.；Carlsson & van Damme；Dekel et al.；Dixit；Ewerhart；Fershtman & Judd；Gilboa & Schmeidler；Heifetz et al.；Hillman & Riley；Hirshleifer；Jones 1995；Kandori et al.；Ok & Vega-Redondo；Pérez-Castrillo & Verdier；Skaperdas；Young；Wilde；Harris & Vickers；Konrad & Kovenock。
  - **AI 安全：** Burns 2023；Barnes & Christiano 2020；Clymer 2024；Critch 2021；Critch & Russell 2023；Dafoe 2020；Denison 2024；Everitt 2021；Korbak 2025；Langosco 2022；Qi 2024；Tessler 2024；Hendrycks 2023。
  - **生物学：** Frank 1995；Price 1972；Hamilton 1975；Rankin et al. 2007；Merton 1968。
  - **系统与控制：** Gunderson & Holling；Olsson 2006；Senge；Sterman；Knight & Leveson；Hayes 1950。
  - **思想史：** Huxley 1893；严复 1898；Schwartz 1964；Acemoglu & Robinson 2012；Ostrom 1990。
- **无法核实：** 无。

#### 抽样核对的 ‡ 与未标记文献，以及登记中的来源（逾 30 项，偏重第 II、III 部分）

| 来源 | 状态 | 说明 |
|---|---|---|
| Zhu 2026 | 已核实【联网】 | 12 家开发者、710 个实例、12 对版本；77%；67%/53%；"seven of eight" |
| Fudenberg & Koh 2026 | 已核实【联网】 | 摘要中没有贴现命题 |
| Fernández Domingos & Han 2026 | 已核实【联网】 | 预注册的比较未得到支持；"落后"一结论来自探索性分析 |
| Bueno de Mesquita et al. 2026 | 已核实【联网】 | EV11 正确；§8.3(c) 有误（次要 1） |
| Stafford, Trager & Dafoe 2022 | 已核实【联网】 | 两项转述都与摘要一致 |
| Amodei 2024 | 已核实【联网】 | EV1 引文逐字准确 |
| METR TH1.1 | 已核实【联网】 | 130.8 天与 165.3 天准确；量程上限见 I2 |
| Epoch 两页 | 已核实；需更新 | 见 I2 |
| AI 2040 Plan A | 已核实【联网】 | 作者、4%/年、48% 均准确。基率分析是由一个 Claude 模型完成的（见下文模型偏差） |
| Abecassis 2025 | 已核实【联网】；用法有误 | 见次要 2 |
| 超级智能对话 | 已核实【联网】 | 白宫情况说明书与 TNW |
| 世界人工智能合作组织 | 已核实【联网】 | |
| A/RES/79/239、80/58 | 已核实【联网】 | |
| REAIM 2026 | 已核实（据报道） | |
| 科学小组任命投票 | 已核实【联网】 | |
| 参议院 99–1 | 已核实【联网】 | |
| 英国机构改名 | 已核实【联网】 | 2025-02-14 |
| 州法诉讼 | 已核实【联网】 | |
| RSP 3.0–3.4 | 已核实【联网】 | |
| OpenAI PF v2 | 已核实【联网】 | 仍是现行版本 |
| 17 家开发者的安全承诺 | 已核实【联网】 | |
| 超级 PAC | 已核实（据报道） | |
| Palisade、MacDiarmid、EvalDetectBench | 已核实【联网】 | |
| Ho et al. 2024 | 已核实【联网】 | |
| AI Index 2026 | 已核实（据报道） | |
| Butler et al. 2025 | 已核实（据新闻稿） | |
| 全球最低税 side-by-side | 已核实【联网】 | |
| 国发〔2025〕11 号 | 已核实【联网】 | |
| Armstrong et al. 2016；Schaffer 1988；Fudenberg & Levine 1993；Greenblatt 2024；Turner 2021；Henrich et al. 2001；Liberman 2004；Anderson 2015；Henrich & Gil-White；Cheng 2013；Fischbacher 2001；Rees 1994；Barrett 2003；Trachtenberg；Hart & Zingales；Choi & Bowles；Alchian；Acemoglu & Robinson 2008；Becker 1983；Oliver 1980；Heckathorn；Seidman；Morris；Hirsch 1985；Soulé；Richardson；Aktipis 2015；Krakauer 2009；Acemoglu, Egorov & Sonin 2012；Panchanathan & Boyd；Price 1970 | 已核实【书目】 | 部分已由上轮【联网】核实 |

### 自己的计算

- 双向引文核对脚本 `SCRATCH/cites.py`、`cites2.py`（纯标准库），结果见 I6。
- 推导了 $h<g_r-g_p$：在效用对消费线性、贴现的模型中，竞赛价值为 $c_0/(\rho+h-g_r)$，配速为 $c_0/(\rho-g_p)$，由此得出该条件。在对数效用下条件不同。这一推导用来确认 I1 的判断。

### 未核对

- RSP 3.4 版中 EV2 引文是否仍然逐字存在（页面只给了 PDF 链接）。
- IASR 2026 与科学小组初步报告的原文。
- 两家开发者对 2025 年 3 月 RFI 的提交。
- EV13 的 Parametrix 原始报告。
- TESTS、CLAIMS 中除引文以外的证据性陈述。
- 没有运行 `checks_v61.py`，那不属于本维度。
- 没有阅读本目录下其他评审的报告，以保持独立。

### 模型家族偏差

我与起草者属于同一模型家族，有五处可能受影响。

1. **对起草方开发者的处理。** EV1、EV2、EV4 都涉及起草方的开发者。我在 I4 中要求记录这家开发者的政治支出，在 I5 中要求补上 RSP 3.1 的保留裁量权。两者方向相反，正是为了检验对称。即便如此，外部评审仍应复核我是否在别处放过了对这家开发者不利的材料。
2. **知识截止。** 我们的知识截止都在 2026 年 6 月。凡是 2026 年 6 月以后的事项，我都只依据联网结果；WebFetch 由小模型做摘要，Jones 与 NBER 两篇改为抽取 PDF 全文自行核对。
3. **来源本身有 AI 参与。** AI 2040 的衰退基率由一个 Claude 模型完成，Marks、MacDiarmid 两篇出自起草方开发者。它们在登记中被用于说明某条路径的"最强形式"，外部读者可能认为存在利益关联。
4. **【书目】核对的局限。** 标为【书目】的条目依赖同一家族共享的记忆。如果有系统性的记忆错误，我和起草者可能同时出错。
5. **对推论"是否合理"的判断。** 判断一个推论是否站得住，可能与起草者共享同样的框架偏好，例如更容易接受"选择"框架下的解读。任务 5 的先例推论尤其需要家族外的历史学者复核。
