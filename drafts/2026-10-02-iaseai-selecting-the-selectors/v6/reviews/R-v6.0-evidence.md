# R-v6.0 评审：证据、来源与思想史

*对象：`v6/THEORY.md` v6.0（3,222 行）与 `v6/EVIDENCE.md`（EV1–EV17）。对照了 `v5/reviews/R-v5.2-evidence-history.md`，以及 `CLAIMS.md` §7 的处置表。评审者是 Claude（Opus 5.5），与起草 v6 的会话不同，但属于同一模型家族（THEORY §10.7）。*

*核对分三级。*
- *【原文】取得原文并做了检索：OpenAI Preparedness Framework v2 的 PDF、Anthropic RSP v3.0 的 PDF、Amodei 的文章、国发〔2017〕35 号、ARCHES 全文、Zhu 2026 的摘要全文。*
- *【页面】读了出版方页面、arXiv 摘要、书目库或可靠的二手报道。*
- *【书目】凭已有知识，未联网，文中注明"未检索"。*

---

## 总判断

1. **文献是真实的。** 本轮联网核对了 45 项（见下表），全部存在，没有编造。其中书目细节要改的有 6 处（Skalse 的会议版题名、Engels 的发表信息、Copeland 两条重名、Leonard 的状态、两处缺页码），转述或用法要改的有十余处。其余 † 文献我按书目知识逐条看过，未见错误；因为没有联网，仍应保留 †。
2. **上轮的修补大多落实了。** 九项点名的修补里，七项落实得好：SIA–BCG 的措辞；Friedman 的最强版本，含 Stigler 和"无代表征税"；Hart–Zingales；Spencer 与标签史；现实主义关于未来意图的回应；地位与支配之分；Frank et al. 的位置。没修完的有两项：
   - OpenAI 条款仍然缺"并分享信息以资验证"，CLAIMS §7 却标为"Repaired"；
   - EV1 的对称性仍然不足。

   上轮的次要项大多没有处理（见【次要】第 12 条）。
3. **唯一的【致命】项在 EV1。** 登记转述 Anthropic CEO 的文章时，删去了"robust military superiority"，也删去了"阻断或延迟对手获取芯片与设备"。登记头部专门作了利益披露，并声明对所有行动者用同一标准，恰恰在这一处软化了。改一句即可。
4. **证据与结论之间有几处错配。**
   - "领先只有几个月"既被读成支持"饱和"（P3），又被读成"落后可以挽回"。
   - Engels et al. 的数字是模型推算，正文却称之为"测量"。
   - "有约束力的约束被明确拒绝"没有说明是谁拒绝的。
5. **思想史部分基本准确，可以对外。** 两条脉络、多元传统、严复译 Huxley 都站得住。§9.6 的先例表有四处事实或出处问题。
6. **规则检查通过。** 正文没有把任何具体的国家对或企业对当作理论的主语。

---

## 一、参考文献与登记来源核对表

| 文献 | 状态 | 说明 | 链接 |
|---|---|---|---|
| Duersch, Oechssler & Schipper 2012 | 已核实，可升 ‡ | *GEB* 76(1):88–96，补页码。结论限于对称的两人博弈；相对收益博弈为广义"石头剪刀布"型时不成立。推论 5.8 处的"compare"可保留，但应注明这一范围 | [EconBiz](https://www.econbiz.de/Record/unbeatable-imitation-duersch-peter/10011049802) |
| Turner et al. 2021 | 已核实，可升 ‡ | NeurIPS 34。命题针对的是最优策略，不是训练出的策略。§10.8 "Power-seeking emerges" 超出其范围 | [NeurIPS](https://proceedings.neurips.cc/paper/2021/hash/c26820b8a4c1b3c2aa868d6d57e14a79-Abstract.html) |
| Skalse et al. 2022 | 更正 | 会议版题名为 "Defining and Characterizing Reward **Gaming**"，arXiv:2209.13085 题名为 "…Reward Hacking"，两者都应注明。转述准确 | [NeurIPS](https://proceedings.neurips.cc/paper_files/paper/2022/hash/3d719fee332caa23d5038b8a90e81796-Abstract-Conference.html) |
| Gao, Schulman & Hilton 2023 | 已核实，可升 ‡ | PMLR 202:10835–10866。所谓"true objective"在原文中是合成设置下的 gold reward model，宜注明 | [PMLR](https://proceedings.mlr.press/v202/gao23h.html) |
| Schoen et al. 2025 | 已核实，可升 ‡ | 共 19 位作者。原文的发现是：评估意识减少隐蔽行为，去除评估意识则增加隐蔽行为。作者也承认，隐蔽行为率的下降不能排除部分来自情境意识。EV6 可由"凭已有知识"改为已核实 | [arXiv](https://arxiv.org/abs/2509.15541) |
| Engels et al. 2025 | 更正 | 已发表于 NeurIPS 2025（Spotlight）。9.4%–51.7% 是推算值，不是测量值（见 I4） | [arXiv](https://arxiv.org/abs/2504.18530) |
| Hammond et al. 2025 | 已核实，可升 ‡ | CAIF Technical Report #1。三种失败模式是 miscoordination、conflict、collusion；七个风险因素中就有 "selection pressures"（见【次要】6） | [arXiv](https://arxiv.org/abs/2502.14143) |
| Critch & Krueger 2020 | 已核实，可升 ‡ | "The multiplicity thesis" 见 ARCHES §2.8。它预言多个委托方与多个系统将会出现；"单一委托对齐不足"是由它推出的结论，不是这一命题本身 | [arXiv](https://arxiv.org/abs/2006.04948) |
| West et al. 2015 | 已核实，可升 ‡ | *PNAS* 112(33):10112–10119。原文说主动压制竞争的机制"在许多关键点上作用较小"，与 §3.7 一致 | [St Andrews](https://research-repository.st-andrews.ac.uk/handle/10023/6969) |
| Choi & Bowles 2007 | 已核实，可升 ‡ | *Science* 318(5850):636–640；转述准确 | [PDF](https://pdodds.w3.uvm.edu/files/papers/others/2007/choi2007a.pdf) |
| Caulin & Maley 2011 | 书目已核实；转述更正 | *TREE* 26(4):175–182。Peto 悖论说的是个体的癌症风险不随体型上升，按细胞算，大型动物的风险反而低得多。"do not get more cancer per cell" 应改为 "show no higher cancer risk despite far more cells"。"because suppression scales with size" 是主流解释，不是定论 | [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC3060950) |
| Rees 1994 | 已核实，可升 ‡ | 芝加哥大学出版社。转述与原书"communitarian regulation"的论点一致 | [UCP](https://press.uchicago.edu/ucp/books/book/chicago/H/bo3618989.html) |
| Barrett 2003 | 已核实，可升 ‡ | OUP。第 8 章讲蒙特利尔议定书，另有 trade linkage 和 side payments 两章 | [OUP](https://academic.oup.com/book/36180) |
| Hart & Zingales 2017 | 已核实，可升 ‡ | *JLFA* 2(2):247–274，补页码。原文的论证依赖股东的亲社会偏好；把它等同于 κ（物质耦合）是本文的引申，应标 [interpretive] | [now](https://nowpublishers.com/article/Details/LFA-0022) |
| Cheng et al. 2013 | 已核实，可升 ‡ | *JPSP* 104(1):103–125 | [Harvard](https://coevolution.fas.harvard.edu/publications/two-ways-top-evidence-dominance-and-prestige-are-distinct) |
| Liberman, Samuels & Ross 2004 | 已核实，可升 ‡ | *PSPB* 30(9):1175–1185 | [Scinapse](https://scinapse.io/papers/1989891117) |
| Bowles & Polanía-Reyes 2012 | 已核实，可升 ‡ | *JEL* 50(2):368–425，综述 51 项实验。原文同时指出挤入也会发生，§5.4 应补半句 | [CESifo WP](https://cesifo.org/DocDL/cesifo1_wp2734.pdf) |
| Stern 2011 | 已核实，可升 ‡ | *IJC* 5(2):213–232。该文专门讨论新兴技术的"风险公地"，本文目前只用了一句 | [IU DLC](https://dlc.dlib.indiana.edu/dlc/items/61002cb4-b3a2-45a6-9de8-4d405a1f45a5) |
| Bannister 1979 | 已核实，可升 ‡ | Temple University Press, Philadelphia | [MUSE](https://muse.jhu.edu/book/9822) |
| Hirschman 1977 | 已核实，可升 ‡ | Princeton UP。"The first defence" 宜改为 "an early defence"：书中写的是资本主义胜利之前的一类论证，并没有说它是最早的辩护 | [PUP](https://press.princeton.edu/node/57465) |
| Soulé 2003 | 已核实，可升 ‡ | *ComPlexUs* 1(3):123–133。原文证明的是多稳态点（multistationarity）的必要条件；multistability 是其子集，所以正文的说法成立 | [arXiv](https://arxiv.org/abs/q-bio/0403033) |
| Richardson 1960 | 已核实，可升 ‡ | Boxwood Press, Pittsburgh；稳定条件 αβ>kl 的写法正确 | [Penn](https://find.library.upenn.edu/catalog/999895413503681) |
| Farrell & Rabin 1996 | 已核实，可升 ‡ | *JEP* 10(3):103–118 | [RePEc](https://ideas.repec.org/a/aea/jecper/v10y1996i3p103-18.html) |
| Abreu 1988 | 已核实，可升 ‡ | *Econometrica* 56(2):383–396 | [RePEc](https://ideas.repec.org/a/ecm/emetrp/v56y1988i2p383-96.html) |
| Stafford, Trager & Dafoe 2022 | 已核实，可升 ‡ | GovAI 工作论文。§7.3 的"落后者不冒险"和 §6.5 的"风险补偿使安全改进打折甚至逆转"都与摘要一致 | [GovAI](https://www.governance.ai/research-paper/safety-not-guaranteed-international-strategic-dynamics-of-risky-technology-races) |
| Leonard 2009 | 已核实（上轮） | *JEBO* 71(1):37–51。应删去"journal details not checked"，改为 ‡（上轮已提，未改） | [RePEc](https://ideas.repec.org/a/eee/jeborg/v71y2009i1p37-51.html) |
| Trachtenberg 1988/89 | 书目已核实；用法更正 | 题名为 "…the Shifting Nuclear Balance, **1949–1954**"，主体是垄断结束后的优势期（见 I5） | [MUSE](https://muse.jhu.edu/article/446783/summary) |
| Price 1970 | 用法更正（未检索） | 组间/组内分解出自 Price 1972（*Ann. Hum. Genet.* 35:485–490），Hamilton 1975 把它用于群体选择。引理 3.10 和 CLAIMS 中的引用都应改 | — |
| Copeland 2000 ×2 | 更正 | 同作者同年有两条，应区分 2000a/2000b。§2.6 的"未来意图"出自 *IS* 25(2) 的书评文章；§7.3 的"窗口关闭"出自 *The Origins of Major War* | — |
| OpenAI Preparedness Framework v2，§4.3，p.11 | 更正（原文） | 原文是 "If we are able to rigorously confirm that such a scenario has occurred, then we could adjust accordingly the level of safeguards…, but only if"，后接三条。第三条是 "…keep our safeguards at a level more protective than the other AI developer, **and share information to validate this claim**"。EV2 漏了末句，并混入了博客的措辞（见 I2） | [PDF](https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf) |
| Anthropic RSP v3.0 | 已核实（原文） | 2026-02-24 生效。Appendix A 中 "until and unless we no longer believe we have a significant lead" 逐字正确，可删去"should be checked" | [RSP](https://www.anthropic.com/responsible-scaling-policy/rsp-v3-0) |
| Amodei, *Machines of Loving Grace*, 2024-10 | 更正（原文） | 见 F1 | [原文](https://darioamodei.com/machines-of-loving-grace) |
| 国发〔2017〕35 号 | 已核实（原文） | 2017-07-08 印发。既有"构筑我国人工智能发展的先发优势""占据人工智能科技制高点"，也有"深化……国际合作，共同应对全球性挑战" | [gov.cn](https://www.gov.cn/zhengce/content/2017-07/20/content_5211996.htm) |
| A/RES/79/325 | 已核实 | 2025-08-26 协商一致通过；科学小组 40 人，职责限于**非军事领域** | [UN](https://www.un.org/pga/wp-content/uploads/sites/110/2025/12/A_RES_79_325-EN.pdf)；[FAQ](https://www.un.org/independent-international-scientific-panel-ai/en/faq) |
| 2025-12-11 行政令 | 已核实（二手） | 题名和"global AI dominance"属实。应改引联邦公报原文 | [Sidley](https://datamatters.sidley.com/2025/12/23/unpacking-the-december-11-2025-executive-order-ensuring-a-national-policy-framework-for-artificial-intelligence/) |
| 2026-09-24/25 超级智能对话 | 已核实（报道） | 原始出处是白宫情况说明书，应改引。"cannot be allowed to drift toward global governance" 是一国 OSTP 主任的话。"no binding obligation" 是登记自己的解读（见 I6） | [TNW](https://thenextweb.com/news/us-china-super-intelligence-dialogue-ai-incident-channel) |
| International AI Safety Report 2026 | 更正 | 2026-02-03 发布。专家顾问组由 29 国以及欧盟、经合组织、联合国提名，不是"30 多国"。报告本身也写到模型能区分评估与部署并相应改变行为，可交叉引用到 EV6 | [techUK](https://www.techuk.org/resource/the-release-of-the-international-ai-safety-report-2026-navigating-rapid-ai-advancement-and-emerging-risks.html) |
| METR Time Horizon 1.1 | 已核实 | 2023 年后的倍增时间：130.8 天，旧任务集为 165.3 天 | [METR](https://metr.org/blog/2026-1-29-time-horizon-1-1/) |
| Epoch：国家间差距；开放与封闭模型 | 已核实；登记有遗漏 | 2026-01-02 一页：落后平均 7 个月，范围 4–14 个月，**此间前沿模型全部来自同一国**。2025-10-30 一页：开放权重模型落后约 3 个月，**曾数次完全追平**（见 I3） | [国家间](https://epoch.ai/data-insights/us-vs-china-eci)；[开放/封闭](https://epoch.ai/data-insights/open-weights-vs-closed-weights-models) |
| Zhu 2026 | 已核实；措辞更正 | 语料覆盖 12 家开发者，但 710 个承诺实例取自 12 对相邻版本。§2.10 的 "twelve developers' frameworks" 应改 | [arXiv](https://arxiv.org/abs/2609.08789) |
| Fudenberg & Koh 2026 | 已核实（摘要） | 模型是两家企业、外生推进的安全阈值，并强调透明度。摘要里没有 §7.9 归于它的贴现命题 h<g_r−g_p，应核对正文，否则删去该处引用 | [arXiv](https://arxiv.org/abs/2609.28291) |
| Bueno de Mesquita, Dziuda & Polborn 2026 | 已核实 | NBER w35276 | [NBER](https://www.nber.org/papers/w35276) |
| Fernández Domingos & Han 2026 | 已核实；措辞更正 | 预注册的风险水平比较没有得到数据支持；"落后加剧不安全选择"来自探索性分析，应注明 | [arXiv](https://arxiv.org/abs/2607.26034) |
| Needham et al. 2025 | 已核实 | 1,000 条、61 个数据集；最佳 AUC 0.83，人类基线 0.92 | [arXiv](https://arxiv.org/abs/2505.23836) |
| flexHEG（Petrie, Aarne, Ammann & Dalrymple 2025） | 已核实 | 2025 年 4 月由 ARIA 委托，共三部分 | [arXiv](https://arxiv.org/abs/2506.15093) |

---

## 二、发现

### 【致命】

#### F1 EV1 与 §7.4：对同一公司 CEO 文章的转述被软化

**位置。** EVIDENCE EV1 的第四个来源；THEORY §7.4 "In AI the strategy has been proposed…"；§2.10 第一行的 "developers' statements"。

**问题。**
- 原文的"entente strategy"有两面：
  - 民主国家联盟靠保障供应链、快速扩张和 "blocking or delaying adversaries' access to key resources like chips and semiconductor equipment" 取得 "clear advantage"，并 "use AI to achieve robust military superiority (the stick)"；
  - 同时以分享收益作 carrot，换取他国支持 "the coalition's strategy to promote democracy"。

  目标是让对手 "give up competing with democracies… and not fight a superior foe"。
- EV1 只保留了 carrot，删去了 stick 和拒止，还标为"凭已有知识"；上轮评审其实已经给出了链接和 "robust military superiority" 这句原话。
- 对政府文件，登记逐字引用 "dominance"；对开发者的 CEO，登记却只给温和的转述。登记头部专门作了利益披露，冷读者会把这一处当作偏袒的证据。
- §2.10 写的是复数的 "developers' statements"，而 EV1 只有一份企业文件。

**依据。** [原文](https://darioamodei.com/machines-of-loving-grace)。

**修法。**
- EV1 逐字引用上面两句，状态改为 Checked。
- §7.4 改为 "…a clear advantage, including military superiority and the denial of key inputs to adversaries, and then offers its benefits…"。这仍然是该策略的最强版本，因为它的力量本来就来自 stick 与 carrot 的组合。
- §2.10 改为单数，或者补上其他开发者的同类声明，并配上对称的反证（见 I1）。

### 【重要】

#### I1 EV1 的"合作目标"仍然不是同类对同类

- 2017 年的规划本身就同时写了"先发优势""制高点"和"深化国际合作"。登记只引了前者，于是该国的合作证据全部落在 2025 年的对外文件上。
- 另一国的"合作目标"取自 Action Plan 第三支柱，其题名是 "Lead in International AI Diplomacy and Security"，内容包括向盟友出口全栈技术、加强出口管制的执行、在标准机构中对抗对方的影响。把它算作"合作目标"，偏宽了。
- 两国各有一份同类的对外文件：各自主导、都经协商一致通过的联大决议，78/265（2024-03-21）与 78/311（2024-07-01）。
- 企业一侧没有反证。可补：
  - OpenAI Charter 的 "stop competing with and start assisting" 条款；
  - RSP v3.0 Appendix A 中向上看齐的承诺："meet or exceed" 竞争者的风险降低水平，以及 "general upleveling"。

**依据。** [国发〔2017〕35 号](https://www.gov.cn/zhengce/content/2017-07/20/content_5211996.htm)；[78/265](https://www.pbs.org/newshour/politics/the-un-adopts-a-resolution-backing-efforts-to-ensure-artificial-intelligence-is-safe-secure-and-trustworthy)；[78/311](https://cn.chinadaily.com.cn/a/202407/04/WS668654f8a3107cd55d269e22.html)；[Charter](https://openai.com/charter/)。

**修法。** EV1 按国内战略文件、对外文件、企业声明分三栏，每栏两方并列（即上轮 Z2 的方案）。正文不动。

#### I2 EV2：OpenAI 条款仍不全；RSP 应改用原文

- **OpenAI。** §4.3 漏了 "and share information to validate this claim"。前提的原文是 "rigorously confirm that such a scenario has occurred"，登记写的 "risk landscape has actually changed" 是博客的措辞。CLAIMS §7 写的 "EV2 restated with all conditions | Repaired" 应改正。
- **RSP 原文比 GovAI 的分析更直接。** 原文说："This approach represents a change from our previous RSP, driven by a collective action problem… Our previous RSP committed to implementing mitigations that would reduce our models' absolute risk levels to acceptable levels, without regard to whether other frontier AI developers would do the same… we cannot commit to following them unilaterally." 这几乎就是命题 8.3，应作为 EV2 的主证据。
- **反证栏要补。** Appendix A 也有向上的竞争者条款，可见以对手为条件的承诺是双向的。
- **§2.10 T2 行。** "one dropped its pause language in 2026" 出自二手分析，应改为原文的说法：从绝对风险的承诺，改为"公司计划加行业建议"。

**依据。** [PF v2 PDF](https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf) 第 11 页；[RSP v3.0](https://www.anthropic.com/responsible-scaling-policy/rsp-v3-0)。

**修法。** 如上。RSP 的 "in the lead" 情景正是 §7.3"领先并用于安全"的一个实例，可以交叉引用。

#### I3 "饱和"与"可以挽回"：证据与结论错配

**位置。** §2.10 的决定性一行；EV5 的 "Reading for decisiveness"；C5；§10.2(4)；§9.6 第二行的 "P1 and P3 failed"。

**问题。**
- P3 说的是"没有任何领先程度能让更多的领先变得无用"。几个月的差距和效率扩散，说明的是领先短、扩散快，与 P1 以及领先能否持久有关，与 P3 无关。
- Epoch 的同一页写明，2023 年以来前沿模型全部来自同一国，落后 4–14 个月。差距没有扩大，但也没有被反超。所以 "refute the claim that falling behind cannot be recovered" 说过了头。开放权重模型确实"曾完全追平"，这一句可以保留。

**修法。** 改为 "present evidence indicates short, diffusing leads, against P1 at present; it does not bear on saturation (P3)"。EV5 把"前沿未曾易手"列入反证。

#### I4 Engels et al. 的数字不是测量

§6.5 写道 "Those are toy settings, but they are measurements"。原文的 NSO 成功率，是把四个博弈中拟合出的 Elo 曲线代入作者的 NSO 理论，再用数值方法（部分为解析）求出的。应改为 "derived from fitted scaling curves in four games"，并补上 NeurIPS 2025。

**依据。** [arXiv](https://arxiv.org/abs/2504.18530)。

#### I5 §9.6 先例表的四处问题

1. **巴鲁克计划。**
   - 失败不只在顺序：巴鲁克在艾奇逊—利连撒尔报告之上加了一条，安理会对违约者的制裁不得否决；苏方也反对现场核查。
   - 两份文件应分开写。"custody must precede decisiveness" 的结论不受影响。
   - [state.gov](https://history.state.gov/milestones/1945-1952/baruch-plans)
2. **首次核垄断。**
   - Trachtenberg 写的是 1949–1954 年。1945–49 年要另找出处，例如 Rosenberg 1983, *IS* 7(4)，讲当时的库存极小（未检索）。
   - Tannenwald 认为核禁忌主要形成于 1950 年代以后。
   - 1945–49 年没有 P3 失效的证据，"P3" 应删去。
3. **NPT 一行。**
   - Burr & Richelson 只支持"曾考虑打击"。"对弱国实施打击"要另引：1981、2007、2025 年的几次打击，以及 Fuhrmann & Kreps 2010, *JCR* 54(6)（未检索）。
   - 实施打击的多不是"合作的大国"，两句应拆开。
4. **蒙特利尔议定书（1987）。** 多边基金是 1990 年伦敦修正案设立的，应写 "the Protocol and its 1990 amendment"。[GAO](https://legistorm.com/reports/view/gao/27748/Operations_of_the_Montreal_Protocol_Multilateral_Fund.html)

另外三处措辞：
- **ABM。** "capabilities judged decisive" 宜改为 "in which one side held a lead"。2002 年退约的动机属于解释，应标明。
- **冷战的结束。** "The Cold War ended by the internal collapse of one side, not by agreement" 太绝对：INF、CFE、"2+4" 条约、START 都是谈判的结果。宜改为 "largely by…, accompanied by negotiated reductions"。
- **§9.3 的 1983 年预警事件。** 没有出处，"prevented a response" 也有争议。应补出处，并改为 "judged the alarm false and did not report an attack"。[参考](https://en.wikipedia.org/wiki/Stanislav_Petrov)

#### I6 "有约束力的约束被明确拒绝"：谁拒绝的没写，对方的立场也没记

**位置。** §2.10 的 T6 行；§9.4 "Where things stand"；EV8；C4。

**问题。**
- 这句话出自一国 OSTP 主任就双边对话所作的表态。正文写成没有主语的事实，读者会以为各方都拒绝了。
- EV8 没有记录另一方同期的治理主张，例如 2025 年 7 月提出的世界人工智能合作组织（未检索）。
- "creates no binding obligation" 是登记自己的解读，没有引用原始出处。
- 联合国科学小组只管非军事领域，恰好不覆盖窄 E1。军事 AI 的多边文件都没有进登记：REAIM 2023/2024；2023 年的《关于负责任地军事使用人工智能和自主性的政治宣言》；联大第 79/239 号决议。各领先国家对这些文件的签署情况不同，正好可以用来检验"同一标准"（签署名单需核对）。

**依据。** [TNW](https://thenextweb.com/news/us-china-super-intelligence-dialogue-ai-incident-channel)；[UN FAQ](https://www.un.org/independent-international-scientific-panel-ai/en/faq)。

**修法。**
- 正文写成 "one leading state's official"，只写角色，不点名。
- EV8 补上述三项。
- Stage 2 的种子补上军事 AI 文件。

#### I7 引理 3.10 之后的推论，在思想史上说得过强

**问题。** 引理本身没有错。但 "Those rules cannot be discovered by selection among alternatives; they have to be designed in advance" 排除了两条在单一群体内部也能发现规则的途径：
- 子单元之间的多中心试错，例如 Ostrom 的嵌套治理和联邦内部的制度实验，只要失败不是致命的就行得通；
- 间接互惠与声誉，它们不经设计就能改变组内收益（Panchanathan & Boyd 2004，本文已引）。

本文真正需要的只是：不可逆的失败不能靠试错来发现。

**修法。**
- 改为 "…cannot be discovered by trial among civilizations; for irreversible failures they must be anticipated, while sub-units can still learn by polycentric experiment"。这也与 §8.6 的"纠错多元"一致。
- Price 1970 改引 Price 1972 与 Hamilton 1975。

### 【次要】

1. §7.6 仍写 "makes the rival the type it was feared to be"。上轮已指出，Kydd 的模型里类型是固定的，应改为 "act as"。
2. §2.8 "Cells"：Aktipis et al. 不是"免疫编辑"的出处，应补 Hanahan & Weinberg 2011 或 Dunn et al. 2002（未检索）。
3. §5.4 应补一句：挤入也会发生（Bowles & Polanía-Reyes）。
4. §2.8 的 "first defence" 改为 "an early defence"；Hart–Zingales 到 κ 的映射标 [interpretive]。
5. Zhu、IASR、Fernández Domingos & Han 三处措辞按上表更正。Schoen、Needham、2017 年规划、RSP 的状态升为已核实。
6. §6.1：ARCHES 处的 "is the multiplicity thesis" 改为 "follows from"。§2.9 新意第 6 条应注明重叠：Hammond et al. 已把 "selection pressures" 列为风险因素，Hendrycks 2023 也已提出 AI 之间的自然选择。
7. §10.8 的 "Power-seeking emerges where advantage compounds" 超出了 Turner et al. 的范围。
8. V1 说跨境影响由 "Section 2.10 treats separately"，但 §2.10 没有这一行。上轮第 6 条已提，未改。
9. CLAIMS §7 写 "Frank et al. moved to §3.3"，实际在 §3.6。
10. Aghion, Jones & Jones 2019 在正文中没有被引用。
11. §2.8 的思想史条目在参考文献里都没有对应：Thucydides；Huxley 1893；严复 1898；Schwartz 1964；《墨子》；康有为《大同书》。上轮已建议补入。
12. 上轮的书目项没有改：
    - Anderson et al. 补卷期页 141(3):574–601；
    - Maynard Smith & Szathmáry 首版由 W. H. Freeman 出版；
    - Hofstadter 补出版者宾夕法尼亚大学出版社；
    - Alger et al. 2020 补 *JET* 185:104951 和副题；
    - EV1 改用正式题名 *Winning the Race: America's AI Action Plan*。

---

## 三、上轮修补的落实情况

| 上轮项 | v6 位置 | 判断 |
|---|---|---|
| SIA–BCG 措辞（I1） | §3.6；EV13 | 已落实；C4F6 和软件更新事故的写法准确 |
| OpenAI 条款写全 | EV2 | 未完：缺 "share information to validate this claim" |
| Friedman 的最强版本 | §2.8 Firms | 已落实 |
| 用 Hart & Zingales 写股东至上 | §2.8；EV15 | 已落实；到 κ 的映射宜标为解释 |
| Spencer 与标签史 | §2.6 | 已落实（popularized；Leonard；Bannister） |
| 现实主义与未来意图 | §2.6 | 已落实；Copeland 两条需分 a/b |
| 地位是尊重，不是支配 | §2.3；V5；EV16 | 已落实 |
| 多元传统 | §2.8；V4 | 已落实；缺参考文献 |
| Frank et al. 1993 的位置 | §3.6 | 已落实 |
| 登记的对称性（Z2） | EV1 | 部分落实；见 F1、I1 |
| 生物学（I2） | §3.7；引理 3.10 | 已落实；推论过强，见 I7 |

## 四、规则检查

通过。
- 正文里出现的 "in China, Mozi…" 和 "Chinese tradition" 指思想传统，不是国家。
- "a bilateral dialogue"、"leading states' affirmation"、"the first nuclear monopoly"、"one party renounced… another kept a covert programme"、§7.11 的 "Export controls on advanced chips"，都是不点名的历史或现实例子，属于允许的范围。
- I6 的修法只写角色，也在规则之内。

## 五、缺口（按对论证的影响排序）

1. **同类对同类的声明矩阵（EV1）。** 两国各列三类文件，再加至少三家开发者的章程或声明，正反都要有。
2. **军事 AI 的多边文件及签署情况。** 这是窄 E1 和 Stage 2 最直接的证据，目前空缺。
3. **P3（饱和）。** 目前没有任何证据，应与 P1 分开登记。
4. **以原始出处替换二手报道。** 包括：12 月行政令（联邦公报）、CAISI（商务部声明）、超级智能对话（白宫情况说明书）、软件更新事故的损失估计（Parametrix 报告）。
5. **§9.6 的出处与反例。** 需要补反扩散打击的出处、1945–49 年的库存，以及 INPO 的反例，如 2002 年 Davis-Besse 事件（未检索）。没有反例，"durable" 一词承担了过多的分量。
6. **Stern 2011。** 它对"新兴技术风险公地"的设计原则作了修订，可以直接用于 §8 的设计。
