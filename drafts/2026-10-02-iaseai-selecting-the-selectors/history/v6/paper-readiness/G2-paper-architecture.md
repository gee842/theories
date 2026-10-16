# G2 衍生论文架构：从 v6.0 切出一篇 10 页会议论文

*2026-10-03。Claude（Fable 5.1）为 Ren 起草。依据：`v6/THEORY.md`（v6.0）、`CLAIMS.md`、`CHANGELOG.md`；`v6/reviews/` 七份评审（fidelity、alignment、adversarial、math、systems、evidence、Codex）；`v6-planning/P3` §7；`submission/main.tex`（v2）与 `NOTES.md`；`reviews/round2/` 对 v2 的四份评审与综合。未改动任何既有文件。*

## 0. 结论先行

1. **推荐论点 (iii)**：v2 论文《Selecting the Selectors》加上 V6 第 4 节里经过核对、无评审争议的三个新结果。三个候选中，只有它的每条承重结果同时通过了 v2 的两轮论文评审和 v6 的七份评审。
2. **适配**：装得下 10 页（预算 9.7 页，一图一表），条件是只进 §4 的结果；不进 §2 的"赢的压力"框架、§5 的三重侵蚀、§6 的强形式化身、§7–§10 的比较与判断。这些要么有致命发现待修，要么属于另一篇论文。
3. **截止前可行，但有两道门**：今晚确认 OpenReview 账号已批（审批可达两周，这是真正的硬约束）；10 月 5 日 12:00（曼谷）过 D 门，过不了就不投。
4. **做好的路**：跑预注册的实验设计 2、补一行实测、请家族外的人读证明。若因此错过 IASEAI'27，归宿是 2027 年春季的会议或期刊，不是勉强投一个弱版本。

## 1. 三个候选论点

| | (i) 三重侵蚀与决定性两难 | (ii) 普遍约束不可见 + 嵌套奖励回路 | (iii) 选择选择者（v2）+ V6 强化 |
|---|---|---|---|
| 一句话 | 赢的压力下，增长同时抬高诱惑、削弱执行、纠错与共同理解；若决定性优势可得，只有建在目标与共同保管里的合作能持久 | 相对选择看不见对所有人一律适用的约束；训练回路的最外层是开发者间的相对选择，所以单个实验室的对齐去不掉它 | 当成功能换成对未来选择过程的控制时，选择会偏爱这种能力本身——只在大而广的载体中、回报可占有且持久、纠错慢时；通用 AI 推动每一个条件；独立纠错必须以可算出的速率增长 |
| 承重结果 | Prop 5.7、Cor 5.8、Prop 5.11、Thm 5.12（含 X/U/φ）、Prop 5.14、Thm 5.16、Prop 5.10 | Lemma 3.3(2)、Prop 3.4、Prop 6.1、Lemma 6.5、Prop 6.7 | v2 Props 1–6、Cors 1–3（四位评审逐行核过证明，三方独立复现数值）+ v6 Prop 4.2(2)(4)、4.3、4.4、4.10、Remark 4.7(4) |
| 新意 | "剪刀差"好记，决定性终结未来之影表述干净。但工具全是标准的（吸收态重复博弈、模仿不可战胜、Crawford–Sobel），且全部条件于 C5——理论自己说证据指向尚未到来 | "训练信号的最外层是赢的压力"对对齐读者有力；"私人成本的偏差很快修、共同成本的偏差要等共同约束"是可检验的新预测。但形式核心只是平移不变性加定义，多重性论题与 Hendrycks 2023 已覆盖大半 | "控制选择的能力何时本身被选择"先于俘获文献（round-2 R3："a genuinely prior question with a crisp answer"）；新加的速率条件、"拆分只延迟不阻止"、"三阶矩而非 HHI"、"暂停须隔离规则制定"具体、意外、可测 |
| 风险 | 三条承重结果今天就有致命/重要发现：5.7 条件漏项（Codex 1、math I1）、5.16 两支不成立（math F1、adversarial 4）、5.14(1) 多方不成立（Codex 5、math I2）。修好的形式是新的、未经评审的；10 页会变成论断清单；审稿人会按现实主义阵营追问 C5 | 3.3(2) 须改为"等额发生"（math I4、Codex 2；adversarial 11 称其为公共经济学常识）；6.7 推论丢了豁免条款，需"对齐税为正"的显式前提（alignment B1）；化身的因果说法超出文献（alignment A1）。形式内容薄，会被读成立场文 | "什么都没测"（所有评审）；形式核心初等且部分已知（round-2 R4）；图 2 的"代表性载体"假设偏离式 (3)，须改为按自身份额计（round-2 必修 1）；约 20 个新词 |
| 页数 | 不适配：5 条结果 + 4 条前提 + 分支分类 + C5 证据，至少 12 页 | 适配有余，但大半是散文 | 适配：v2 已 8.3 页，加 1.2 页新结果，需从相关工作与设计原则裁 0.6 页 |
| 裁定 | 第二篇论文，待修复落地 | 并入 (iii) 的 AI 节作一条有条件注记 | **推荐** |

**为什么推荐 (iii)。**
- 满足"先建全理论、再压缩"：§4 从 v2 到 v5.2 到 v6 一直稳定，七份评审没有一条针对 4.2–4.10 本身（Codex 只指出 §7 把 4.8(2) 的充分条件当成了必要条件，那是用法问题；systems 评审说"§2–4 的系统骨架是稳的"）。
- v6 新加的结果恰好是 round-2 评审要的：4.2(2) 的规模阈值就是"容量不能从稀有入侵"的定理形式；4.2(4) 就是对场预测 (a) 的更正；4.4 是审稿人要的"可量化的把手"；4.10 直接对应暂停之争。
- AI 的特异性有据：评估者准入条款、同族裁判偏好、相关误差、助手降低转化成本，都是已核实的文献，不像 C5 那样待定。
- 它天然守住作者的规则：不点名（扫描通过，只有 "EU AI Act" 作为工具）、不谈二元对、不抬高竞赛阵营、开头是平白事实。
- (i)、(ii) 的健全部分都能作后续论文；今天塞进 10 页，只会把全理论尚未修好的部分带进双盲评审。

## 2. 推荐论点的论文方案

### 2.1 题目
- **推荐**：*Selecting the Selectors: When Success Buys Control over AI Evaluation, and How Fast Independent Correction Must Grow*
- 备选 1：*Selection for Control over Selection: Capture, Correction and the Evaluation of AI*
- 备选 2：*Who Evaluates the Evaluated: Selection for Control over AI Evaluation and Its Correction*

保留 "Selecting the Selectors"（round-2 R4：好记、点中现象）；副题说出新的统一论断。"meta-attractor" 不进题目与摘要。

### 2.2 Abstract（约 200 词）

> AI systems are increasingly selected by benchmarks, evaluators, reward models and standards that the most successful developers help to build, fund or supply. We ask when selection itself favours practices that acquire control over the processes that later select them. When carriers of a practice differ heritably in their capacity to convert success into rule support, that capacity is selected when its appropriable, persistence-weighted return exceeds its marginal cost. The return grows with the square of the carrier's share and with its scope across domains, so control capacity is selected in large carriers and cannot invade from rarity; it vanishes when rule support is shared, correction is fast or returns arrive late. For coupled domains we give decentralized certificates against capture and show which reforms are re-absorbed, and derive how fast independent correction must grow when assistants lower the cost of control: splitting a dominant carrier delays capture without preventing it. Evaluators drawn from the evaluated lineage delay the detection of harm by an amount that diverges at a computable masking level, and a pause that freezes shares completes capture unless rule-making is insulated during it. We state tests that separate these mechanisms from entrenchment, and governance principles that follow.

### 2.3 逐节大纲与页数预算（AAAI 双栏，≤10 页；目标 9.7，留 0.3 缓冲）

| 节 | 内容 | 来源（v2 / v6 编号） | 页 |
|---|---|---|---|
| 1 Introduction | 平白事实开头（基准由已部署系统构成、评估者依赖准入、裁判偏爱同族）；问题；一段答案；一个合并的贡献清单（含 Statement of Contributions） | v2 §1 | 1.0 |
| 2 Related work | 四段：俘获与锁定；生态位构建与可占有性；集体行动、寻租与认证；AI 结构风险与评估。补 round-2 列出的缺失文献 | v2 §2 + 本文 2.5 | 0.7 |
| 3 Practices, selectors, model | 式 $(x,z)$；配置命题；俘获三条件与"集中≠俘获"表；病理三条件独立；"meta-attractor" 只作中性标签一句 | v2 §3；v6 Def 4.1、Prop 4.8(1)、Remark 2.4 | 1.2 |
| 4 Selection for control over selection | 容量命题；**规模阈值 $p^\ast$ 与"不能从稀有入侵"**；范围条件 $\hat\varphi>\hat\eta$；何时不被选择；助手两面性（仅二次成本）；棘轮（补成本条件与 $\bar q$ 一致性假设）；纠错是内部供给不了的二阶公共品 | v2 Prop 2、Cors 1–3、Prop 3；v6 Prop 4.2(1)–(4)、4.3(1)(3) | 1.8（含图 1 约 0.5） |
| 5 How much independent correction, how fast | 认证阈值 $d^\ast$；AI 压低控制成本时需 $\alpha\ge g/(1+\eta)$；AI 同样压低纠错成本的对称情形一句；拆分延迟 $2\ln k/(g-(1+\eta)\alpha)$ 而不阻止；三阶矩而非 HHI | v6 Prop 4.4(1)(2)(3)、(4) 一句、(7)(8) | 0.8 |
| 6 Coupled fields: certificates, reforms, pauses | 行和证书；孤立测试不能认证；核精确；级联与再吸收；keystone 与关闭的窗口；**冻结份额的暂停**（驻留时间按 systems F4 改为 $\ln R/(\varepsilon d)$ 加份额松弛，注明先升后降） | v2 Props 4–5；v6 Prop 4.8(2)–(4)、4.9、4.10 | 1.2 |
| 7 Detection: masked evaluation | 面板平均掩蔽（加形成项 $\beta_Fx_F$）；静默穿越；发散的延迟；保守报警与"界必须来自外部"；掩蔽隐藏水平不隐藏动态（一句，细节入附录） | v2 Prop 6、Remarks 1–3；v6 Prop 4.6(1)(2)(5)、Remark 4.7(1)(2)(4) | 0.8 |
| 8 Why general-purpose AI raises the stakes | 表 1；转化更便宜；多域在场；裁判之席；与可扩展监督的关系（按 round-2 必修 4 更正）；"服从不等于场对齐"改写为"不充分"；一条有条件注记：训练回路是一个选择域，净私人成本为正的保护措施在开发者层被选择掉，除非对所有人等额施加 | v2 §7；v6 Lemma 3.3 窄形式、Prop 6.7(3) 窄形式 | 1.2（含表 1 约 0.45） |
| 9 Tests, identification, scope | 三臂实验协议（正文一段，附录 C）；**披露试点：20 个种子，四条预测一条失败，诊断与预注册的设计 2**；场预测（更正 (a)(d)）；识别作为可恢复性，边际改革作自然实验；"何时失去效力" | v2 §8；EV12 | 0.6 |
| 10 Design principles, limitations, conclusion | 每条原则标注"推导/映射/规范"；现有工具一句；限度；结论 | v2 §§9–10 | 0.4 |
| **合计** | | | **9.7** |

附录（不计页）：A 证明（含 4.2(2)(4)、4.3、4.4、4.10，自 v6 附录 A 移植）；B 数值与稳健性（自身份额 vs 代表性载体两种制式、√μ 规则、滞回、场图、延迟表、驻留时间）；C 实验协议、试点报告与设计 2；D 离散时间版本；E 符号表。

### 2.4 V6 结果去向

| 去向 | 结果 |
|---|---|
| 正文 | Def 4.1；Prop 4.2(1)–(4)；Prop 4.3(1)(3)；Prop 4.4(1)(2)(3)(7)(8)；Prop 4.6(1)(2)(5)；Remark 4.7(1)(2)(4)；Prop 4.8(1)–(4)；Prop 4.9(1)–(3)；Prop 4.10；Remark 2.4（作为 P1–P3）；Lemma 3.3 只作一句（等额施加的共同约束不改变守约者间的相对增长） |
| 附录 | Prop 4.3(2)(4)(5)；Prop 4.4(4)(5)(6)；Remark 4.5；Prop 4.6(3)(4)；Remark 4.7(3)；§4.7 的识别式；Remark 2.3 作为 $D=1$ 的稳定性基准 |
| 排除 | 全部 §2（Def 2.1、Def 2.2 三层、机制表、T1–T6、§2.7、§2.8、Ψ、§2.10）；§3 除 Lemma 3.3 窄形式外全部（Prop 3.5、3.6、3.9、Lemma 3.10、Prop 3.11、§3.8）；Thm 4.11（依赖 H0 与 Prop 3.4，会把论文拉宽）；全部 §5；§6 除一条窄注记外全部；全部 §7–§10；EV1–EV3 的具体条目（会点名） |

排除只有两种理由：有待修的评审发现（5.7、5.16、5.14(1)、3.10、3.3(2) 广义、6.7 强形式、7.10、7.12、§10.1），或属于另一篇论文/只有全理论能承载的规范判断。

### 2.5 相关工作定位
- **俘获理论**（Stigler 1971；Laffont & Tirole 1991；Dal Bó 2006；Carpenter & Moss 2013；Kwak 2014；Hanson & Yosifon）给出通道；新的是选择偏爱能用这条通道的载体、回报按份额平方放大、场层面的证书。
- **锚定与递增收益**（Arthur 1989；Pierson 2000；Acemoglu & Robinson 2008；Hardt et al. performative power）：成功塑造未来成功；新的是先于它的问题——重塑选择的能力何时本身被选择，以及何时不被选择（Cor 1）。
- **生态位构建与可占有性**（Krakauer, Page & Erwin 2009；Lehmann 2008；Kylafis & Loreau 2008；Gerlee & Anderson 2015；Arrow 1962；Teece 1986）：χ 的最近前身；差别三条——被改的对象是选择规则本身、跨域的场、价值相反（侵蚀而非拯救公共品）。
- **集体行动与寻租**（Olson 1965；Tullock 1967；Grossman & Helpman 1994；Bombardini 2008；Bombardini & Trebbi 2012）：规模阈值的经验对应；新的是动态选择表述与"纠错是二阶公共品"（Oliver 1980；Heckathorn 1989）。
- **认证、评级与标准制定**（Lizzeri 1999；Strausz 2005；Bolton, Freixas & Shapiro 2012；Lerner & Tirole 2006；Simcoe 2012；Mattli & Büthe 2003）：掩蔽作为面板平均；新的是延迟律与谱系份额 $x_E$。
- **对选择规则的选择**（Campbell 1974；Barberà & Jackson 2004；Acemoglu, Egorov & Sonin 2012；Bowles et al. 2003；Klüver 2002）：新的是第三层的可遗传变异与速率条件。
- **级联与单调系统**（Morris 2000；Easley–Kleinberg；Kempe et al. 2003；Seidman 1983；Hirsch 1985；Smith 1995）：明说是标准工具——"new results in this setting, obtained with standard tools"。
- **AI 结构风险与评估**（Zwetsloot & Dafoe 2019；Critch & Krueger 2020；Critch 2021；Hendrycks 2023；Hammond et al. 2025 已把 selection pressures 列为风险因素；Kulveit et al. 2025；Longpre 2024；Raji 2022；Panickssery 2024；Awuni 2026；Kim 2025；Goel 2025；Eisenstein 2023）：继承"逐系统对齐不充分"；新的是带条件的机制与两面的助手结果。

### 2.6 唯一的图与唯一的表
- **图 1**（跨双栏，约 0.5 页，三小格）：(a) 模型示意——六个域、转化箭头、实践对共享条件 $V$ 的负荷、带掩蔽的评估报告；AI 裁判/训练回路画成 D→E 的一条转化边，助手画成降低培育转化成本的箭头。(b) 按自身份额计的容量—俘获扫描（χ 三值；等份额起点 vs 1% 起点，显示不能从稀有入侵）。(c) $d^\ast(\gamma)$ 曲线与 $k$ 拆分的延迟。滞回图与场图入附录 B。
- **表 1**：行为模型量（χ、控制成本 γ/f、范围 $|S|$、进入评估的转化 $b_{Ej}$、掩蔽 $\beta_{in}/\beta_{out}$、纠错率 $d$、速度比 ε/ζ）；列为：通用 AI 对它做什么｜证据与状态（已测/有文献/假设）｜进入哪条结果｜哪项检验能测它。这把 round-2 R3 要的"参数→代理→状态"做进唯一的表。

## 3. 适配检查

**装得下，但要守三条纪律**，否则会变成论断清单：
1. 全文只问一个问题（控制选择的能力何时被选择，被选择后怎样纠正），只用一个量（归一化转化 $R_{ij}$ 及其行和）贯穿五个结果节；每节开头一句"这一节回答什么"。
2. 新词压到 10 个以内（practice、rule support、conversion、$R_{ij}$/row sum、appropriability、conversion capacity、capture 三条件、masking、certificate、keystone），加符号表；删掉没有结果用到的构造（layers of closure、error-access graph/min-cut；practical/epistemic closure 只留一句）。
3. 每条命题正文给一行证明思路（round-2 R4）；"exactly when" 改 "when"，避免同义反复之嫌。

**作者会舍不得的内容，以及去处：**

| 内容 | 去处 |
|---|---|
| 赢的选择压力（Def 2.1）、元吸引子三层、不依赖载体、另一个星球 | 全理论。论文只留中性的"自我维持的制度"一词并引 Klüver |
| 三重侵蚀、剪刀差、决定性两难（§5） | 第二篇论文，待 5.7/5.16/5.14 按 math I1、F1、I2 与 Codex 1 修好；可用 Codex 的问句立题："当成功同时改变背叛的收益和纠正它的制度时，合作还能激励相容吗" |
| 两通道记账恒等式与 θ 的识别（Prop 3.5；math 称"全文最干净的统一结果"） | 第二篇论文的工具节，或一篇短文 |
| 嵌套奖励回路强形式（Prop 6.7）、工具与化身 | 本篇留一条有条件注记；强形式等 alignment A1/B1 修复与检验 T-L 后，作立场文或第二篇的 AI 节 |
| 窄 E1 为严格均衡（Prop 6.4；adversarial 称"跨阵营最稳的建议"） | 委托与锁定的论文，不在本篇 |
| "我们是一体"、Lemma 3.10、Prop 3.11 | 全理论；论文不能承载规范判断，3.10 的推论也在修 |
| 生成的元吸引子、按功能推导形态、Compact、守护者测试、过渡 | 全理论；或日后治理论文（systems F1/F2 修好之后） |
| 标准 D 下的判断、E1/E2/E3 | 全理论。论文只能给标注"推导/映射/规范"的设计原则 |
| 讲赢/讲理、癌的意象、"先换盆再加速" | 全理论；冷读与匿名都不允许进论文 |

## 4. 双盲与冷读问题
- **语料痕迹**：v6 §4 的文字含 "the author's corpus"、"the author's pilot experiment"、EV/附录引用；移植时一律改第三人称与论文自己的附录号。不得出现讲赢/讲理、生生不息、大同、物竞天择、molochlization、"attractor of attractors"、"cosmic cancer"、"change the basin, then add speed"、"the winner's rule"。
- **自引**：09-28 的论文和任何已公开的元吸引子短文，要么第三人称引用，要么不引。Statement of Contributions 里 "conceptual antecedents appeared in informal essays" 只在短文确已公开、且措辞无法回指作者时保留，否则删（NOTES 已标）。
- **链接与文件**：不链接全理论、仓库、预印本；补充材料只上传 `figures.py`、`field.py`、`carrier.py`、`checks.log`，先扫路径与用户名；`build.sh` 不上传。用官方套件编译，`\author{Anonymous Submission}`，检查 PDF 元数据 Author 字段为空；上传文件名中性。
- **不点名**：v2 扫描通过。不要移植 EV1–EV3 的具体条目（CEO 文章、某框架删去暂停语言、评估机构更名），按暗示即可识别机构；证据只写角色。Zhu 2026 若引，按 evidence 评审改为"710 个承诺实例，取自 12 对相邻版本"。
- **冷读**：摘要和引言第一句是事实；每个新词第一次出现给一个平白从句；"meta-attractor" 不进摘要（R4）；"answerability" 不进题目，除非形式化。
- **诚实披露**：检验一节必须写一句试点（EV12）：一次 20 个种子的运行，四条预测一条失败，诊断为谱系太少与漂移，设计 2 已预注册未跑。不写日期。
- **AI 协助**：评审指南未规定；评审稿不含致谢，正式稿怎么写由 Ren 定。

## 5. 两条日程

### (a) 截止前（OpenReview `duedate` 2026-10-06 10:59 UTC，曼谷 17:59；现在是 10 月 3 日晚）

**范围**：v3 = v2 + round-2 必修 1–10 + 三个 v6 移植（Prop 4.2(2)(4) 作规模与范围结果；Prop 4.4(1)(2)(3)(7)(8)；Prop 4.10）+ 一图一表合并。Remark 4.7(4) 与 Prop 4.3 只在页数允许时进正文，否则入附录。不进任何 §2、§3（除一句）、§5–§10 的内容。

| 时间（曼谷） | 节点 |
|---|---|
| 10/3 夜 | **门 0**：OpenReview 账号已批？没有就不走这条路。**门 T0**：Overleaf 建项目，用 `submission/` 的 AuthorKit27 把 v2 原样编译一次，确认页数 |
| 10/4 上午 | 载体修复：图 2 改按自身份额计并重跑；规模结果写成命题（即 v6 4.2(2)）；棘轮加成本条件 $c_i\hat b_{ij}\ge\gamma b^0_{ij}$ 与 $\bar q$ 一致性假设；冻结容量的反事实补成本 |
| 10/4 下午 | 必修 3–10：可查的错句（NP-hard、预测 (a)、形成项、Cor 3 仅二次成本、β≥0.6、0.88→0.96 等）；监督段更正；定位段与新意句；β 与偏好提升的推断标为启发式；文献与书目修正；精度清单；图的可读性 |
| 10/5 上午 | 移植 4.4 与 4.10：正文陈述、附录证明（自 v6 附录 A）、数值从 `checks_v6.py` 移入 `build/` 并重生成 `checks.log`；4.10 的驻留时间按 systems F4 写 |
| 10/5 12:00 | **D 门**：①每条定理附录有证明且有数值核对；②摘要、引言、结论逐句能追到结果或文献，无任何无条件的"必须合作"；③匿名扫描（姓名、"Ren"、语料项目名、URL、"the author's"）与 PDF 元数据；④含图表 ≤10 页；⑤贡献声明在；⑥官方套件编译通过；⑦试点披露句在。**过不了就不投**，保留修好的稿 |
| 10/5 下午 | 请 Codex（家族外）花 2–3 小时只核三处：4.2(2)、4.4、4.10 的措辞与证明是否超出所证；按意见改 |
| 10/5 晚 | Ren 定题目、摘要、轨道；在 OpenReview 先建条目（截止时题目、摘要、作者锁定） |
| 10/6 06:00–09:00 | 上传，留 ≥5 小时缓冲 |

**轨道**：archival（无平行评审，形式内容全新）要求亲自到场；若到场不确定，选 non-archival。**预期**：round-2 估计修完约 45% 的 archival 概率；v6 移植会加一点，"什么都没测"仍在。

### (b) 做好的路
1. **跑设计 2**（`experiment/PREDICTIONS-2.md`，40 个种子，已预注册）。成则写进论文，败也写进论文。round-1 四位评审一致认为实验是让论文"重要"的那一步；round-2 R1 估计加 10–15 个百分点。
2. **补一行实测**：例如领先谱系在常用基准/评估工具/标准草案中的作者或资助份额的时间序列，或评估面板的谱系构成 $x_E$。识别路径论文里已有（logit 速度回归）。有一行实测，"nothing is measured" 就不再是每份评审的第一句。
3. **家族外审读**：一位数学家读 Props 2–3 与新加的 4.4（NOTES："A mathematician should reread them"）；一位 IO/公共经济学读者看寻租与可占有性的定位；一位评估治理从业者看表 1 与原则。Codex 已读 v6，缺的是人。
4. **评审点名的扩展**：策略性掩蔽；同一域内多实践竞争；频率依赖的收益；"不能从稀有入侵"从数值事实升为定理；掩蔽的形成项。
5. **冷读重写**：新词 ≤10、符号表、正文一行证明思路。

**场所**。IASEAI'27 在题材上完全合适（档案轨、技术与治理混合、约 19% 录用）。做好的版本需要 4–8 周，赶不上。那时的归宿：2027 年春季截稿的 AI 伦理/治理会议（如 AIES、FAccT 的 2027 届，须核对征稿；FAccT 更看重实证），或期刊收完整形式（如 *AI & Society*、*Minds and Machines*；模型若继续发展，也可投经济学/政治经济学期刊，须核对契合）。可行的组合：现在按 (a) 的范围投 IASEAI'27，同时为 2027 年的场所做带实验与实测的 v4——若 v3 被档案收录，v4 须有 ≥50% 的新技术内容（实验加实测足够），或作期刊长文。若门 0 不过，或 Ren 只要质量，就跳过 IASEAI'27 直接做 v4；(i) 作为第二篇，待修复之后。

## 6. 请 Ren 定
1. 是否走 (a)：前提是 OpenReview 账号已批，且接受"过不了 D 门就不投"。
2. 题目三选一；"meta-attractor" 是否完全退出正文（建议：只留一句并引 Klüver）。
3. 轨道：archival 还是 non-archival，取决于能否到场。
4. 第二篇论文（三重侵蚀）是否按 Codex 的问句立题，待 math F1/I1/I2 修复后启动。
