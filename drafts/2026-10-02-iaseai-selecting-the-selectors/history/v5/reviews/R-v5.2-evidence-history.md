# R-v5.2 评审：证据、来源与思想史

*对象：`v5/THEORY.md` v5.2，*Changing the AI Trajectory*。评审范围：§1.1、§1.2、§1.4、§1.5、§1.6，§2.6 证据表，References 中 "The governing model: evolution, behaviour, performativity and history" 一组，以及 `v5/EVIDENCE.md` 的 E1、E2、E7、E13–E16 和 Gaps。对照读了 `reviews/REVIEW-v5.1.md`（起草模型的自审，F1–F12 已改）。凡是自审已经处理的问题，本文不再重复；如果在它的修法之上还有问题，会注明"在 F9/F10 之上"。*

*视角：经济史、经济思想史、演化生物学、行为经济学。*

*核对方法分三级，每条结论都注明属于哪一级。*
- *原文：取得了原文并做了全文检索。包括 Friedman 1970 全文；Business Roundtable 1997 年 *Statement on Corporate Governance* 全文；SIA–BCG 2021 的两页摘要和 53 页完整报告；OpenAI Preparedness Framework v2 的 PDF；外交部网站上的《人工智能全球治理行动计划》；Zhu 2026 的 arXiv 摘要。*
- *摘要或书目：读了出版方页面、RePEc/PMC 摘要或书目记录。§1.4–1.5 引用的其余期刊文献都属于这一级。*
- *凭已有知识：本轮没有检索、只凭已有知识写出的文献，单独标"未检索"，使用前必须核对。*

*作者为 Ren，正文由 Claude 起草；本评审也由 Claude（Opus 5.5）完成，但不是起草 v5.1/v5.2 的那次会话。*

---

## 总判断

§1.4–1.5 引用的来源都真实存在，没有编造的文献。多数说法与原文相符，书目细节大体正确。第 1 节的骨架是：Ψ 是错的，但它通过自我证实、表演性、选择和地位驱动维持自己。在证据上，这个骨架站得住，而且比 v5.0 好得多。

问题集中在三处。三处都能就地修补，修完以后第 1 节会更有力。

1. **谱系选错了最近的祖先，还与自己引用的 Harvey 相矛盾（Z1）。** 第 5 条把今天 AI 政策里"赢得竞赛、取得主导"的说法接在新自由主义和股东至上之后。但这套说法更直接的来源是另一条脉络：国家之间的生存竞争学说，以及冷战时期的技术竞赛。而且 E1 引用的 2025 年文件出自一个奉行关税和出口管制的政府，这恰是新自由主义传统所反对的。"首先在英美经济体"这个说法，与 Harvey 的开篇叙述不符。
2. **"各种出身的领先者都持有 Ψ"在登记中没有对称的证据（Z2）。** 支持 Ψ 的声明只来自一个国家。另一个国家只出现在反证栏里，而且是拿它的对外治理文件去对照对方的国内战略文件。正文说 Ψ"不是任何文明的本质"，但冷读者从登记的结构里读出的恰恰是本质化。
3. **"Ψ 是错的"有几处说过了头，几位对手的立场也被写弱了（I2–I5）。** 具体有五点：
   - "每一次重大跃迁都需要压制内部竞争"，与该领域的综述（West et al. 2015）相反。
   - 人群层面并不自利，这一点驳不倒 Alchian–Friedman 的"仿佛"论证。而本文自己的命题 4.2(4) 正是这个论证的形式版本。
   - Friedman、股东至上、OpenAI 准备框架三处，都没有写成对方最强的版本。
   - Anderson 等人所说的"地位"本来就排除了支配。
   - 声望也会复利（Matthew effect），这直接威胁 V5。

---

## 来源核对表

| 来源 | 文中说法 | 核实 | 更正 |
|---|---|---|---|
| Friedman 1970, *NYT Magazine*, 13 Sept | 利润是唯一社会责任，"so long as it stays within the rules of the game" | 是（原文） | 引文准确。该句是 Friedman 自引 *Capitalism and Freedom*（1962）。同文还说经营者应遵守"law"与"ethical custom"所体现的社会基本规则；最强版本应包含这一点（I4） |
| Jensen & Meckling 1976, *JFE* 3(4):305–360 | 代理理论围绕经理与所有者的对齐重塑企业 | 是（书目） | 准确。它是关于所有权结构的实证理论；规范性的"股东价值最大化"主张主要来自后来的著作，Jensen 本人 2001 年又转向"enlightened value maximization"（未检索） |
| Business Roundtable 1997 / 2019 | 1997 年宣布股东至上，2019 年修订 | 是（1997 原文；2019 新闻稿） | 1997 年文件题为 *Statement on Corporate Governance*（September 1997）。E15 的引句逐字正确，同文还说董事会的"paramount duty"是对股东的。该文前言列出前身文件，包括 1981 年的 *Statement on Corporate Responsibility*（未读）。2019 年：8 月 19 日，181 位 CEO 签署，正确 |
| Harvey 2005, OUP | 新自由主义"首先在英美经济体"兴起，再扩散到世界 | 书目是；说法不符 | Harvey 导论以 1978–80 年的多地转向开篇，第一个例子是一个共产党执政经济的自由化。正文另称智利 1973 年政变后是"第一次实验"。见 Z1 |
| SIA–BCG 2021，"Strengthening the Global Semiconductor Supply Chain in an Uncertain Era" | "没有任何公司或国家能够实现半导体自给自足"；≥1 万亿美元；价格上涨 35–65% | 数字是；措辞否（原文） | 报告原句是"No company or even entire nation is vertically integrated across all"（指现状）。报告说完全自给"成本惊人、执行可行性存疑"，并建议有针对性的本土产能激励。"无法实现"是本文的加强。见 I1 |
| Henrich et al. 2001, *AER* 91(2):73–78 | 15 个小规模社会都不支持标准自利模型；合作随市场整合度和合作收益上升 | 是（摘要） | 准确。可补 Henrich et al. 2010, *Science* 327:1480 的复制结果。反证：Lamba & Mace 2011, *PNAS* 108(35) 发现同一族群内各村落之间的差异，与跨文化差异相当 |
| Fischbacher, Gächter & Fehr 2001, *Econ. Letters* 71(3):397–404 | 一次性公共品实验中，约一半是条件合作者，约三分之一搭便车 | 是 | 准确（策略法；另约 14% 呈驼峰型） |
| Frank, Gilovich & Regan 1993, *JEP* 7(2):159–171 | 经济学学生更常背叛，训练有贡献；"推论有争议" | 是 | 争议没有写全。Yezer, Goldfarb & Poppen 1996, *JEP* 10(1):177–186：现场"丢信"实验中，经济学学生归还的信更多。Girardi, Mamunuru, Halliday & Bowles 2024, *Southern Econ. J.* 90(3):792–814：双重差分下，学习经济学对自利没有可辨别的影响。证据更支持自我选择，而不是训练（I3） |
| Ferraro, Pfeffer & Sutton 2005, *AMR* 30(1):8–24 | 理论通过制度设计、规范与语言自我实现 | 是 | 准确。有正式论争：Felin & Foss 2009, *Org. Sci.* 20(3) 提出"自我实现的边界"，FPS 同期回应 |
| MacKenzie 2006, MIT Press | 金融模型重塑了它所描述的市场 | 是（书目） | 准确。同书也讨论"反表演性"（1987 年崩盘），可用来说明 Ψ 也会自我挫败 |
| Fudenberg & Levine 1993, *Econometrica* 61(3):523–545 | 自我确认均衡：路径上的信念正确，路径外可以错 | 是 | 准确。建议补 Fudenberg & Levine 2006, *AER* 96(3):630–651：当偏离的代价高、没人去试时，错误信念在理性学习下也能长期存续。这正是高赌注下 Ψ 无法被证伪的机制 |
| Anderson, Hildreth & Howland 2015, *Psych. Bull.* | 地位欲望是基本动机，跨文化、性别、年龄、人格 | 是（摘要） | 准确，但该文把地位定义为尊重、钦佩与自愿服从，并明确区别于权力（I5）。参考文献缺卷期页：141(3):574–601 |
| Henrich & Gil-White 2001, *EHB* 22(3):165–196 | 支配与声望两条路线；声望授予技能与贡献 | 是 | 原文中声望授予的对象是值得学习的技能、知识与成功；"贡献"是引申（I5） |
| Maynard Smith & Szathmáry 1995 | "每一次"重大跃迁都是整合 | 书目基本是 | 首版出版者为 W. H. Freeman/Spektrum（牛津），OUP 平装本 1997 年。作者把这些性质列为跃迁的常见特征；性和语言的起源不是"能独立复制者合为整体"的直接例子（I2） |
| Aktipis et al. 2015, *Phil. Trans. R. Soc. B* 370(1673):20140219 | 癌是对多细胞合作的欺骗 | 是 | 准确 |
| Hofstadter 1944, Univ. of Pennsylvania Press | 由其史家"命名"为社会达尔文主义 | 部分 | 该词 1877 年已见于英文（Fisher），1880 年见于法文（Gautier）。Hofstadter 是使它在美国学界流行的人，不是命名者 |
| Leonard 2009 † | "标签的历史有争议" | 是（摘要） | *JEBO* 71(1):37–51，可改为 ‡。Leonard 的实质论点更强：在 Hofstadter 的书里，达尔文式论证同时服务于自由放任和进步主义改革中的种族主义、优生学与帝国主义（"达尔文集体主义"）。所以 Ψ2 不专属于市场脉络（Z1、I4） |
| Meadows 1999, Sustainability Institute | 参数层面的干预杠杆低，目标与范式是最深的杠杆 | 是 | 准确。它是系统思维的启发式，不是经验证据。"系统抵抗干预"这一说法应归于 Forrester/Sterman 的 policy resistance（未检索） |
| Jervis 1976；Kydd 1997, *World Politics* 49(3) | 螺旋"使各方成为它所恐惧的类型" | 是（书目） | Kydd 的模型中类型是固定的，螺旋改变的是信念和行为。应写"acts as the type it feared" |
| Ostrom 1990, CUP † | 公地可以不靠主权者或私有化来治理 | 是 | 准确，可改为 ‡。证据来自边界清楚的小尺度公共池塘资源；Ostrom 的设计原则偏向多中心治理（I3） |
| Polanyi 1944 (New York: Farrar & Rinehart)；Kropotkin 1902 (London: Heinemann)；Smith 1759 (London: A. Millar)；Darwin 1871 (London: John Murray, 2 vols) † | 列为 Ψ 的批评者 | 是 | 书目如左，可改为 ‡。Darwin 对社会本能的解释，本身依赖部落之间的竞争（*Descent*, ch. 5），这正是 §1.4 要回答的那个反驳（I2） |
| E1：America's AI Action Plan, 2025-07-23 | "winning the AI race"，主导 | 是 | 正式题名为 *Winning the Race: America's AI Action Plan*。第三支柱包括出口"全栈"AI、在国际标准机构中对抗对手的影响 |
| E1 反证：《人工智能全球治理行动计划》, 2025-07-26 | 合作、能力建设、联合国科学小组、"向善为民" | 是（外交部原文） | 由"2025 世界人工智能大会暨人工智能全球治理高级别会议"发表。"向善为民"、联合国两项机制、能力建设三句都在原文中。它是对外治理文件，与对方的国内战略文件不对等（Z2） |
| E2：OpenAI Preparedness Framework v2, 2025-04-15 | 对手发布无相当保障的系统时"may adjust our requirements"，须先确认并公开 | 部分（原文） | PDF 原文是"could adjust accordingly … but only if"，后面跟三个条件：评估认为不会实质增加严重伤害的总体风险；公开承认；为避免"race to the bottom on safety"，保障仍要严于对方，并分享信息以资验证。登记漏了第一和第三个条件（I4） |
| E2：Zhu 2026, arXiv:2609.08789 | 710 个承诺实例；77% 弱化；67%/53% 未披露；8 对中有 7 对 | 是（摘要） | 准确。单作者 Louis Yiven Zhu，未经同行评审 |
| E2：Anthropic RSP v3.0 | "until and unless we no longer believe we have a significant lead" | 未能确认 | GovAI 分析的相应措辞是"clear lead"。需要对照政策原文逐字核对 |
| E7：International AI Safety Report 2026 | 2026-02-03 发布，Bengio 领衔，30 多国 | 是 | 准确。但 §1.4 用 E7 支持"失败沿集中的共享基础设施节点传播"，E7 这一行没有引到报告里讲集中度和单点故障的部分 |

---

## 发现

### 致命

#### Z1 谱系：选错了最近的祖先，与所引的 Harvey 相矛盾

**位置。** §1.5 第 5 条及其后一段；中文概要"它有一段历史"；E15。

**问题。**
1. 正文写道，AI 政策中"赢得竞赛、取得主导"的说法"is the same model applied to the newest technology"，并把这句话放在新自由主义转向的叙述末尾。读者会读成直系后裔，但这条线在历史上是弱的。
   - 古典新自由主义在思想上是世界主义、反重商主义的（Slobodian 2018，未检索）。Friedman 和 Hayek 都会反对出口管制、关税和国家入股企业，而 E1 所引的 2025 年文件正出自推行这些政策的政府。
   - "主导"一词更近的祖先是国家层面的生存竞争学说：从 19 世纪末的国家达尔文主义（Pearson 1900；Bernhardi 1911），到冷战技术竞赛中的"导弹差距"和"太空竞赛"，再到今天的技术民族主义（均未检索）。
2. "首先在英美经济体"与 Harvey 不符。Harvey 导论把 1978–80 年写成多地同时的转折，智利 1973 年后的实验在独裁之下进行。思想起源也不限于英美：Mont Pèlerin 学会 1947 年由一位奥地利经济学家在瑞士召集，德国秩序自由主义者也在其中。
3. Ψ2 的规范子句"胜者即正义"比达尔文早两千多年：修昔底德的米洛斯对话、《高尔吉亚》中的卡利克勒斯、法家的"富国强兵"。"朴素达尔文主义"只是它的现代科学外衣。不写出这一点，读者会以为本文把"强权即公理"归咎于 19 世纪的英国。

两条脉络都满足 Ψ 的定义，所以根模型本身不受影响。但只讲一条，就把 Ψ 归到了一次转向上。这正是作者提醒过的"把一切归为一个根"的反射。

**依据。**
- Harvey 2005 导论（[OUP](https://academic.oup.com/book/40603/chapter/348210808)）；
- Leonard 2009（[RePEc](https://ideas.repec.org/a/eee/jeborg/v71y2009i1p37-51.html)）；
- Fourcade-Gourinchas & Babb 2002, *AJS* 108(3)，比较四国走向新自由主义的不同路径；Hall & Soskice 2001, *Varieties of Capitalism*（均未检索）。

**修法（就地修补，不删内容）。**
- 把第 5 条改写为两条脉络，各自一句：
  - (i) *Within firms and public institutions*：股东至上、代理理论、按市场标准设计公共机构。这一转向在自由市场型经济体中最早、最彻底，再经贸易、金融与发展机构扩散，各国差异很大。
  - (ii) *Between states*：生存竞争学说，从古代的"强者为所能为"，到 19 世纪末的国家达尔文主义，再到冷战技术竞赛。先发国家和后发国家都采纳过它。
  - 然后写：今天 AI 政策的"竞赛与主导"同时继承了两者。前者提供"规则可以买"的制度，对应 C；后者提供"落后不可挽回"的国家叙事，对应 Ψ3。
- 把 "first in the Anglo-American economies" 改为 "first articulated in a transatlantic network of economists, first applied at scale in the 1970s under authoritarian as well as democratic governments, and carried furthest by the liberal market economies"。用制度类型命名，而不是用民族命名，也更合作者"正文不点名"的规则。
- 加一句："The normative clause of Ψ2 is older than Darwin; naive Darwinism is its modern scientific dress."
- 把 "is the same model applied" 改为 "fits Ψ's tenets"，这是定义加观察（[D]+[O]）。凡是谱系意义上的说法，标 [C]。

#### Z2 "各种出身的领先者都持有 Ψ"：登记里的证据不对称

**位置。** §1.5 末段 "Ψ is now held, in some measure, by leading states and firms of every origin"；中文概要；§2.6 第一行和第三行；E1；E15 的 Effect。

**问题。**
- E1 支持 Ψ 的证据只有一个国家的声明。另一个领先国家只出现在 Contrary 栏，用的是对外的全球治理文件，去对照对方的国内战略文件。§2.6 的 W 行也是同样的结构。
- 正文明确说 Ψ"不是任何文明的本质"，登记的结构却把一方放在 Ψ 这边、另一方放在合作那边。
- 这一条比任何单个文献错误都更伤第 1 节的可信度，因为它违反了作者自己的规则。

**依据（登记中可以点名）。**
- 2017 年《新一代人工智能发展规划》（国发〔2017〕35号）把"构筑我国人工智能发展的先发优势"列为目的，目标是 2030 年"成为世界主要人工智能创新中心"（[gov.cn](https://www.gov.cn/zhengce/content/2017-07/20/content_5211996.htm)）。
- 2017 年 9 月，第三个大国的领导人说，AI 领域的领导者将成为世界的统治者；同一场合他又说垄断地位极不可取，并表示愿意分享技术（[Fortune](https://fortune.com/2017/09/04/ai-artificial-intelligence-putin-rule-world)）。支持与反证出自同一个场合。
- 一家前沿开发者的 CEO 在 2024 年的文章中，主张民主国家联盟取得"clear advantage"和"robust military superiority"（[Machines of Loving Grace](https://darioamodei.com/machines-of-loving-grace)）。这是企业声明中以对手持有 Ψ 为前提的 Ψ3，也就是 §1.2 所说的"归属"路径。按作者的规则，它只作为登记中的证据，不当作"最强论证"。
- 反证也应当对称：
  - OpenAI Charter 承诺，若有价值一致、重视安全的项目先接近 AGI，就"stop competing with and start assisting"（[Charter](https://openai.com/charter/)）。这一条款在公司改制后是否仍然有效，本身就是一个检验。
  - Preparedness Framework v2 中明确写有"race to the bottom"条件。
  - 上面那位领导人的反垄断表态。
  - 《人工智能全球治理行动计划》。
- "落后就要挨打"是常见的政治话语，就是 Ψ3 的通俗说法。要入登记，需要找到带日期的官方出处。

**修法。**
- 把 E1 拆成三行：E1a 是国内战略文件，按国家并列；E1b 是对外治理文件，按国家并列；E1c 是企业声明。
- §2.6 W 行的"最强反证"改成同类文件对同类文件。
- 正文不变，仍不点名，只在登记中做到对称。
- 补齐之前，E15 Effect 中"held … by actors of every origin"标为 [C]。

### 重要

#### I1 SIA–BCG 的措辞；以及同一份报告里更好的 κ 证据

**位置。** §1.4 Material 第一条；E13。

**问题。**
- "found that no company or country can achieve self-sufficiency"把报告对现状的描述，改写成了不可能性。报告说的是目前没有任何公司乃至国家在所有环节上垂直整合；完全自给成本惊人、可行性存疑；报告的政策建议是有针对性地扶持本土产能。
- 同一份报告里还有一个例子，比 E7 更直接地说明不经价格结算的耦合：一种蚀刻气体（C4F6）若损失 6000 万至 1 亿美元的供应，下游 NAND 的收入损失约为 100 亿至 180 亿美元，约为直接影响的 175 倍。

**修法。**
- 正文改为："An industry assessment found every country interdependent in the chain; fully self-sufficient regional chains would need at least a trillion dollars of additional investment and raise prices by 35 to 65 percent (E13)."
- C4F6 的例子写进 E13，作为 κ 的初步证据，并放到 Material 第二条下。
- 来源：[完整报告](https://www.semiconductors.org/wp-content/uploads/2021/05/BCG-x-SIA-Strengthening-the-Global-Semiconductor-Value-Chain-April-2021_1.pdf)。

#### I2 生物学：三处要修，修完反而更有力

**位置。** §1.4 Biological；§1.5 末尾所列的 Darwin。

1. **"In each major transition"。** 这是过度概括。改为 "in the transitions in individuality"，或 "in many of the major transitions"。
2. **"Each transition required the suppression of competition inside the new whole."** 这与该领域的综述相反。West, Fisher, Gardner & Kiers 2015（*PNAS* 112(33):10112–10119，[PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC4547252/)）的结论是：在多数个体性跃迁中，组内冲突之所以低，是因为群体从一开始就是克隆的或强制共命运的，再加上生态收益；主动压制竞争的作用有限，社会昆虫中的工蜂治安是例外。压制竞争确实是合作演化的一条主要途径（Frank 2003, *Evolution* 57:693–705，[PDF](https://stevefrank.org/reprints-pdf/03Evol.pdf)），但不是每一次都需要。

   修好后与本文更贴合："Integration came mostly from interests aligned by construction, shared fate from the start, and secondarily from policing." 前者对应命题 1.5 的汇总与分享，后者对应纠错。生物学由此给出了两个杠杆，而不只是一个比喻。
3. **"没有外部群体"的回答还少两步。** 自审 F10 已经补了这一回答，以下在 F10 之上。
   - 第一步：Darwin 正是用部落之间的胜负来解释社会本能的（*Descent* ch. 5，[文本](https://psychclassics.yorku.ca/Darwin/Descent/descent5.htm)）。把 Darwin 列为批评者，需要加半句："Darwin, whose account of the social instincts itself rested on competition between tribes"。
   - 第二步：对本文最强的生物学威胁是"狭隘利他"。Choi & Bowles 2007（*Science* 318:636–640）和 Bowles 2009（未检索）认为，人类的组内合作与组间冲突是共同演化的。若果真如此，"没有外部群体"就意味着历史上的整合驱动力在行星尺度上缺席。本文的回答（理解加制度）是一个**没有生物学先例的前提**，应标 [C]，不能写成从生物学推出的结论。可以借 Price 方程把这一步说清楚：只有一个群体时，组间协方差项为零，剩下的只有偏向相对地位的组内选择，所以整合只能靠预见和制度。

**补强。** 要说明"相对选择会毁掉整体"，更贴切的证据是演化自杀，即选择把种群推向灭绝（Rankin, Bargum & Kokko 2007, *TREE* 22(12):643–651），以及 Frank 2011 *The Darwin Economy* 的鹿角军备竞赛（未检索）。它们说明，真实的达尔文主义预言的是浪费性的地位竞赛，而不是"胜者即适者"。这比"重大跃迁"更直接地驳倒 Ψ2 的经验部分，也与引理 4.4 同构。

#### I3 "Ψ 是错的"需要逐条说明"错"在哪里

**位置。** §1.1 第 2 步；§1.4 开头的 "It fails on four counts"；§2.6 "Ψ is false | Supported"。

**问题。**
- **对手最强的版本从来没有说人是自利的。** Alchian 1950 和 Friedman 1953（"The Methodology of Positive Economics"）的论证是：竞争环境会让存活下来的组织表现得"仿佛"在最大化。本文自己的命题 4.2(4) 就是这一论证的形式版本：对强度的选择偏好 θ=−1 的行为。所以，人群中有一半是条件合作者，驳不倒"被选择出来的行动者按 Ψ1 行动"。本文的第 3 条机制其实已经承认了这一点。正文应当把这层关系写明：Ψ1 作为人性的描述是错的，但 Ψ1 式的行为会被选中，后者正是 §1.5 的论点。
- **Ψ2 有一个规范子句。** "胜者即正义"不是关于世界的命题，经验证据驳不倒它，只能由 V1–V5 拒绝它。"Ψ is a model of the world, and it can be checked against the world" 只适用于 Ψ2 的描述部分。
- **Ψ1"误判了行动者自身的利益"依赖 κ>0。** E7 只定性地显示了耦合，E13 自己也写明它不确立 κ。κ 的大小没有测量（建议的证据见 I7）。
- **Ostrom 的证据来自边界清楚的小尺度公共池塘资源。** 她的设计原则偏向多中心、嵌套的治理，扩展到全球公地需要修改（Stern 2011, *Int. J. of the Commons* 5(2)，未检索）。这对 §7 的单一共同前沿有约束，至少应在 E14 中写明。
- **Frank et al. 1993 放错了位置。** 后来的研究把差异主要归于自我选择（见核对表）。它更适合作为第 3 条机制"心智的选择"的证据，而不是表演性的证据。表演性有更直接的证据：
  - Liberman, Samuels & Ross 2004（*PSPB* 30(9):1175–1185）：同一个囚徒困境，叫"华尔街游戏"还是"社区游戏"，合作率差别很大，而且名称的预测力超过声誉；
  - Bowles & Polanía-Reyes 2012（*JEL* 50(2):368–425，51 项实验）：为自利者设计的激励常常挤出社会偏好；
  - Ghoshal 2005（*AMLE* 4(1):75–91，未检索）：直接论证代理理论的教学具有表演性，正好接上 Jensen–Meckling 那一条。

**修法。**
- §2.6 这一行的状态改为：
  - "False as a law of nature and as a reading of evolution (O); false about actors' interests where unpriced coupling exists (T given κ>0; κ evidenced qualitatively, unmeasured); Ψ3 contingent on rules (C)"；
  - 反证栏补上：选择论证（Alchian；命题 4.2(4)）、狭隘利他、支配路线同样可行（Cheng et al. 2013）。
- §1.4 开头加一句："Ψ's normative clause is not refuted by evidence but rejected by the values of §1.6."

#### I4 对手的最强版本（在 F9 之上）

1. **Friedman。**
   - 他所说的规则包括"ethical custom"。
   - 更要紧的是，规则可以被买，这一点本来就是芝加哥学派自己的发现：Stigler 1971 的规制俘获理论（未检索）。Friedman 本人也公开批评企业游说政府谋取保护（1983 年演讲，1999 年刊于 Cato Policy Report，[Cato](https://www.cato.org/policy-report/marchapril-1999)）。
   - 所以 "the mechanism of this paper is where it fails" 应写成：这一学说的作者看到了规则俘获，他们的对策是缩小可被俘获的、有裁量权的规则制定。本文的分歧在于对策：一项具有行星尺度、存在未定价耦合的技术，没有"不制定规则"这个选项；不设规则，规则就由赢家的系统事实上制定。
   - Friedman 的另一论证是：经理拿别人的钱去追求社会目标，等于"无代表的征税"。这一论证反而支持 V3 和独立的公共纠错，而不支持企业靠自愿框架自律（E2）。引用它会让 §1.5 更公平，也更有力。
2. **股东至上。** E15 写道："counts only one party's payoff, which is Ψ1 at the level of the firm"。这是稻草人。它的最强版本是：剩余索取者承担剩余风险；在合同完备、外部性由法律定价的条件下，最大化剩余价值就是最大化总剩余。Hart & Zingales 2017（*J. Law, Finance & Accounting* 2(2):247–274，[ECGI](https://ecgi.global/working-paper/companies-should-maximize-shareholder-welfare-not-market-value)）在主流经济学内部证明：外部性与生产决策不可分离时，Friedman 的分离论就不成立。这正是本文的 κ。E15 的 Competing explanations 应改成这一层，正文第 5 条可以加半句。
3. **OpenAI 准备框架。** 见核对表。登记漏掉的两个条件里，有一个明说是为了避免"race to the bottom on safety"。把它写全，E2 依然支持 W 的节奏，因为这一条款仍然以对手的行为为条件；同时也显示，开发者自己知道这种动力存在。写全后，这条证据更难反驳。
4. **社会达尔文主义的研究史。** 正文写道："later applied to society as a justification of hierarchy and domination"。这一句不应暗示 Spencer 本人的意图：Spencer 预言社会将从"军事型"走向"工业型"，他反对军国主义（未检索）。Leonard 2009 的实质论点见核对表。Bannister 1979（未检索）认为这个标签主要是批评者用来指责对手的。这些都支持本文"不是某一脉络的本质"的立场，应当写进正文那半句里，而不只是一句"有争议"。
5. **现实主义（§1.2）。** "fear makes each side the type it feared"要改正，见核对表。现实主义最强的回应是：今天行为的可核查性，解决不了对方**未来意图**的不确定性（Mearsheimer 2001；Copeland 2000）。§1.2 说"beliefs respond to verifiable conduct"，应加一句，指向 §8 中针对能力而非意图的核查。

#### I5 地位、声望与 V5

**位置。** §1.5 第 4 条；V5；E16。

**问题。**
- **定义不一致。** Anderson et al. 2015 证明为基本动机的"地位"，定义为尊重、钦佩与自愿服从，并明确与权力区分。也就是说，被证明是基本动机的，本来就是声望型的那一种。"Ψ channels the drive into dominance"应改写为："The drive is for respect; dominance is a substitute route to rank."
- **支配同样可行。** Cheng, Tracy, Foulsham, Kingstone & Henrich 2013（*JPSP* 104(1):103–125，[PDF](https://henrich.fas.harvard.edu/sites/scholar.harvard.edu/files/henrich/files/cheng_et_al_2013.pdf)）发现，支配和声望都能带来实际影响力，只是支配者不受喜爱。这一条应写进 E16 的 Contrary。
- **声望授予的不只是贡献。** Henrich & Gil-White 的声望授予值得学习的技能与成功，所以竞赛的赢家也会得到声望。
- **声望也会复利。** Merton 1968 的 Matthew effect（*Science* 159:56–63）说明，声望会累积，并转化为资源和人才。今天的 AI 领域本身就是一个声望经济：基准榜单、论文、排名。

**修法。** V5 加一个条件："prestige that does not convert into control over the shared conditions or their correctors"。这正是本文的转化率 χ。这样，V5 就从一句愿景变成了一个可测量的设计条件。E16 的 Next measurement 改为测量声望向算力、资本和评估权的转化。

#### I6 两种传统都是复数的

**位置。** §1.5 所列的批评者；V4。

**问题。**
- 所列的批评者全部是欧洲人（Smith、Darwin、Kropotkin、Polanyi、Ostrom）。V4 则只把"中国传统"写成支持一种好理想的来源。合起来看，西方既是病源又是解药，中国传统只有善的一面。这两点都是不对称的。
- 而真实的历史更能支持"不是文明的本质"：
  - Ψ2 在晚清是被**翻译**进来的。严复 1898 年的《天演论》译自 Huxley 的 *Evolution and Ethics*。Huxley 原讲演的主旨是伦理的进步在于对抗宇宙过程，严复却借 Spencer 加按语，把它变成了"物竞天择"的国家存亡学说（Schwartz 1964，[Yan Fu](https://en.wikipedia.org/wiki/Yan_Fu)）。一篇反 Ψ2 的讲演，被译成了 Ψ2 的口号。
  - 批评也出现在中国：
    - 孙中山在《孙文学说》（1919）中说物种以竞争为原则、人类以互助为原则，直接承接 Kropotkin（措辞需核对原文）；
    - 章太炎 1906 年的《俱分进化论》认为善与恶俱进；
    - 康有为的《大同书》设想破除国界等九界，这正是包容的自我模型。
  - 中国传统里也有以强为正当的脉络，即法家的耕战与富国强兵。

**修法。**
- 正文不点名国家，只写："The strand travelled. Translated into doctrines of national survival in late-industrializing states, it was answered there too, by thinkers who set mutual aid against struggle and imagined the removal of boundaries."
- 具体人名放进参考文献。
- V4 改为"one strand of the Chinese tradition, which like every tradition also contains strands that justified power by strength"。
- 作者自己的大同论正是这条批评传统的延续。写出来是资产，不是让步。

#### I7 缺失的证据：按对第 1 节的影响排序

1. **Ψ 在 AI 组织中的直接证据**（§2.6 第一行承认的缺口）：章程与声明（Z2 所列，正反都要有）；高管薪酬是否与相对排名或市场份额挂钩；投资回报上限的设立与取消。
2. **未定价耦合 κ**：
   - 上面的 C4F6 例子；
   - Carvalho, Nirei, Saito & Tahbaz-Salehi 2021（*QJE* 136(2):1255–1321，[PDF](https://www.kellogg.northwestern.edu/faculty/alirezat/JapanEQ.pdf)）：冲击沿供应链上下游传播，地震使日本次年实际 GDP 增速下降 0.47 个百分点；
   - 2024 年 7 月一次安全软件更新使约 850 万台设备崩溃。Parametrix 估计财富 500 强的直接损失约 54 亿美元，其中只有 10–20% 有保险（二手报道，[链接](https://cybersecuritynews.com/crowdstrike-outage-loss-5-4-billion/amp/)）。这是失败沿集中节点传播、而价格没有结算的直接证据。
3. **在 AI 中检验 Ψ3。** Epoch AI 测得：开放权重模型在 ECI 上平均落后约 3 个月（2025 年 10 月；[Epoch](https://epoch.ai/data-insights/open-weights-vs-closed-weights-models)）；另一领先国家的模型自 2023 年以来平均落后约 7 个月（[Epoch](https://epoch.ai/data-insights/us-vs-china-eci)）。这条证据两头都有分量：它反驳"落后不可挽回"，支持 §1.4 Compounding 一段；同时它也削弱了决定性优势情景的紧迫性。两面都应写入。规则使 Ψ3 成真的直接证据，见 Philippon 2019 *The Great Reversal* 和 Autor et al. 2020 *QJE* 135(2)：集中度上升与游说、反垄断松弛有关，并且因司法辖区而异（均未检索）。
4. **相互依存可以被武器化。** Farrell & Newman 2019（*International Security* 44(1):42–79，[Belfer](https://belfercenter.org/publication/weaponized-interdependence-how-global-economic-networks-shape-state-coercion)）。Copeland 2015 的贸易预期理论认为，预期被切断时，相互依存反而加剧冲突。Angell 1910 的教训是，单靠"相互依存使战争不划算"的论证，并没能阻止 1914 年。本文已经区分了贸易依存和 κ（F7），但应明说为什么 κ 不会像贸易那样被转化为筹码：危害的耦合无法靠脱钩切断。
5. **思想史上的两个支点**（均未检索）：
   - Hirschman 1977 *The Passions and the Interests*：为商业辩护的最初论证，是用利益驯服对荣耀和支配的激情。照此说，Ψ 不是市场传统本身，而是支配的激情穿上利益的外衣回来了。这一说法对对手更公平，也更锋利，还能把第 4 条机制（支配与声望）和第 5 条机制（历史）连起来。
   - Slobodian 2018：新自由主义者设计了不受民众政治干预的规则（"encasement"），结构上与本文隔离纠错者的设计相似；区别在于隔离的是谁、防的是谁。写出这一点，本文对新自由主义的批评会更准确。
6. **先例。** §1.3 的核心命题"竞赛是自我模型的性质"，在国际关系理论中的先例是 Wendt 1992（*IO* 46(2):391–425，[RePEc](https://ideas.repec.org/a/cup/intorg/v46y1992i02p391-425_02.html)）：自助与权力政治是制度，不是无政府状态的本质。他的三种无政府文化（敌人、对手、朋友）大致对应 θ 的取值。应当引用，并引 Mearsheimer 1994/95 的反驳（未检索）。

### 次要

1. Hofstadter："named" 改为 "popularized"，并注明 1877 年的出处（[Wikipedia](https://en.wikipedia.org/wiki/Social_Darwinism)）。"survival of the fittest" 出自 Spencer 1864，Darwin 自《物种起源》第 5 版（1869）起采用。
2. Maynard Smith & Szathmáry 的出版者（见核对表）；Anderson et al. 补卷期页；Leonard 和 Ostrom 改为 ‡。
3. Friedman 的引句注明自引 *Capitalism and Freedom*。
4. Meadows 标明是启发式；"resist" 归于 policy resistance。
5. E1 用正式题名；E1 反证注明发布主体；E2 的 RSP 引句逐字核对。
6. V1 说跨境影响的经验问题 "Section 2.6 treats separately"，但 §2.6 表中并没有这一行。要么补一行，要么改指 N 行。
7. MacKenzie 的"反表演性"可以放进第 2 条机制，说明 Ψ 也有使自己变假的时候。
8. 第 1 条机制可补 Fudenberg & Levine 2006（见核对表）：赌注越高，越没人去试克制，Ψ 就越难被证伪。

---

## 类型标签与登记缺口

| 位置 | 现状 | 应为 |
|---|---|---|
| §1.4 "Ψ1 misdescribes the actor's own interests" | 无标签，§2.6 写 Supported | [T] 以 κ>0 为条件；κ>0 为 [O]（定性），大小未测 |
| §1.4 "Evolution's largest innovations were integrations" | 无 | [O]，限定为"许多"或个体性跃迁 |
| §1.4 "At the planetary scale there is no outside group" | 无 | 分析性陈述 [D]；"integrating force must come from the shared host" 为 [C]（无生物学先例） |
| §1.4 "Ψ3 holds where institutions built under Ψ make it hold" | 无 | [C]，部分为 [O]（Philippon；Epoch 的追赶数据） |
| §1.5(2) 表演性用于 Ψ | 无 | 一般机制为 [O]（有争议）；用于 Ψ 为 [C] |
| §1.5(4) "Ψ channels the drive into dominance" | 无 | [C] |
| §1.5(5) "self-interest moved from an assumption … to a norm" | 无 | [O]，属于解释性的思想史（补 Ghoshal、Berman 2022、Ferraro） |
| §1.5(5) "the same model applied to the newest technology" | 无 | 谱系意义为 [C]；改写为 "fits Ψ's tenets" 后为 [D]+[O] |
| §1.5 "held … by leading states and firms of every origin" | 无，E15 写作已支持 | 补齐 Z2 之前为 [C] |

**Gaps 列表**目前只覆盖全文的缺口。第 1 节应补以下四项，按影响排序：
- (7) Ψ 被持有的情况，按出身对称地记录；
- (8) Ψ 在 AI 组织的章程、薪酬与投资条款中的体现；
- (9) κ 的大小，即未定价耦合的传播与放大；
- (10) 声望是否保持不可转化（χ）。

谱系上的因果链不必列为缺口，按 Z1 改写后就不再需要它。

---

## 站得住的部分

- **引用的真实性。** 所有来源都存在。Friedman 1970 和 BRT 1997 的引文逐字正确，SIA 的数字正确，Henrich 2001 和 Fischbacher 2001 的转述正确。没有张冠李戴。
- **第 1 条机制的适用范围。** 自审 F11 改过之后，自我确认均衡的用法是准确的：它只用于存在合作均衡的博弈，并且明确排除了单期博弈。
- **"批评的是 Ψ 对市场的解读，不是市场"（F8）。** 这一区分有证据支撑（Henrich 2001、2010），而且比多数同类文献更公平。
- **"Ψ 既在被持有时支配，也在被归于对手时支配。"** 这一条把现实主义的结构路径收进了根模型，同时保留了可检验的出口：可核查的行为能够改变归属。
- **"这是一支成为主导的思想脉络的历史，不是任何文明的本质"，以及列出同一传统中的批评者。** 方向是对的。Z1、Z2、I6 的修补都在加强这一立场，而不是推翻它。
- **癌的比喻。** 有 Aktipis et al. 支撑，用法也限定在 §1.4 说明的意义之内。

---

## 待作者决定

1. **谱系写一条还是两条（Z1）。** 建议写两条，分别是企业-制度的一条和国家间生存竞争的一条。这样根模型 Ψ 不变，但历史不再被归到一次转向上。
2. **"Anglo-American" 是否换成 "liberal market economies"。** 后者命名的是制度类型，不是民族，更合"正文不点名"的规则，也更准确。
3. **登记中是否加入企业 CEO 的文章与他国领导人的言论（Z2）。** 它们只用作"Ψ 被持有或被归属"的证据，并配上对称的反证；不当作对方的最强论证。其中一篇出自 Claude 的开发者的 CEO，这一点应当照实写明，不回避。
4. **正文是否写入晚清的翻译与回应（I6）。** 可以不点名国家，只写"后发国家"。这是让"不是文明的本质"从断言变成可以展示的历史的最省力的办法，也把作者自己的大同论放回它的思想谱系里。
5. **V5 是否加上"声望不可转化为对共享条件的控制"这一条件（I5）。** 加上以后，V5 就接到了 χ，成为可测量的设计条件。
6. **"Ψ 是错的"在 §2.6 中是否拆成三个状态（I3）。** 建议拆开。这样 §1.4 承担的证据负担与它实际拥有的证据一致，对手最强的选择论证也被正面收编为第 3 条机制。
