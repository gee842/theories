# G3 模拟程序委员会评审：IASEAI'27

*2026-10-03。三位审稿人加一位领域主席，均为模拟。A＝把 V6.0 核心（概要、§0–3、§5、§6.4/命题6.7、§7.10–7.11、§10、附录G）按现状压成的10页匿名稿；B＝现有 v2《Selecting the Selectors》（`submission/main.tex`）。引文照录原文，评分为1–10分。文中的概率是模拟委员会的主观估计，不是预测。*

**门槛判断。** IASEAI 是跨学科会议，欢迎形式化的治理与伦理论文，录取线低于顶级 ML 会议主会。但审稿人只读10页正文，对三件事很敏感：
- 贡献能否一句话说清；
- 论证能否在正文里核验；
- 主张是否超出证据。

## 评分总表

| 审稿人 | 稿 | 相关 | 原创 | 严谨 | 重要 | 清晰 | 建议 |
|---|---|---|---|---|---|---|---|
| R1 技术安全/ML | A | 7 | 5 | 3 | 5 | 3 | 拒稿 |
| R1 | B | 8 | 6 | 7 | 6 | 6 | 弱接收 |
| R2 政治经济/IR | A | 7 | 5 | 4 | 6 | 4 | 弱拒稿 |
| R2 | B | 7 | 6 | 7 | 6 | 6 | 弱接收（边界） |
| R3 哲学/伦理 | A | 8 | 7 | 5 | 6 | 5 | 边界（偏拒） |
| R3 | B | 6 | 6 | 7 | 5 | 6 | 边界（偏收） |

## 审稿人1：技术 AI 安全/ML

### 稿A
**强项**
1. 命题4.4把"AI 降低控制成本"变成了可检验的条件：独立纠错的增长须满足 α ≥ g/(1+η)；拆分只延迟、不阻止证书失效（4.4(7)）；衡量集中度应看份额三阶矩，而不是 HHI（4.4(8)）。条件具体，且有反垄断含义。
2. §5.3 给出可争议覆盖的定义 U1–U4，还提出了测量方法，例如"固定人工小时下植入缺陷的捕获率"和"固定审计预算下控制协议的安全性"。这些可以直接接到 AI control 与可扩展监督的研究上。
3. 每条主张都标了类型（[T][T∣A][A][N][C]），附录G列出反例，脚本可复现，连失败的先导实验也照实报告。这种自我约束少见。

**最致命的批评**
1. 承重命题有错。命题5.7假设决定性位置 "valued conservatively at no more than the cooperative payoff"，却给出 "if and only if" 条件。若该价值低于合作收益，可维持条件会多出一项正值，所给条件就只是充分条件。附录证明称取上界是 "the most favourable case for cooperation"，其实是最不利的情形。定理5.16又把 p_d→1 换成了 "attainable"，所以"决定性两难"在所述形式下不成立。
2. 命题6.7的结论超出了证明："Instrumental convergence and reward hacking are, at the level that decides, coordination problems." 证明只是引理3.3的组合。能带来私人收益的安全措施（提高可靠性，或减少奖励黑客，也就是提高产品质量）会被相对选择偏爱；对垄断者来说，奖励黑客也仍然是技术问题。对齐研究者会把这句话读成贬低技术工作。
3. 多数结果是标准结果的重述（Richardson、Hayes 延迟界、Crawford–Sobel、平移不变性、Tullock 竞赛），长期结论实际由前提承担："Under strict U1, (U) is close to definitional for systems beyond human capability"。"this agreed in 200,000 random draws" 这类检查验证的是代数恒等式，不是模型本身。正文有七十余个编号结果，10页里一个也证不了。

**最能提分的单一改动**：只留3–4个结果并加以修正（5.7写成精确的执行条件；6.7限定为"净私人成本为正的安全措施"），在正文给出证明，再给一个能与对齐实践区分开的预测。

### 稿B
**强项**
1. 问题单一："when does selection itself favor practices that acquire control over later selection?" 中心结果给出了能力被选择的条件，其中可占有性扮演 Hamilton 规则里亲缘度的角色；推论还列出了不被选择的情形。
2. 耦合域的结果干净：行和证书、core 的精确性、关键石，以及检测延迟公式（与仿真相差在0.3时间单位以内）。证明完整。
3. 与评估实践衔接：LLM 评审的同族偏好和相关错误；debate、AI control、W2S/RRM 在"选择者位置"上的差别；要求独立性 "counted in control units over funding, data, lineage and authority"。

**最致命的批评**
1. 没有经验锚定："The numbers illustrate the propositions and estimate nothing"；表1也写明 "illustrative, not measurements"。R_ij、χ、β 一个也没有估计。
2. 增量需要说得更清楚。作者自认 "The tools are standard"，Price 方程一步 "only keeps the books"。最接近的先例 Krakauer, Page & Erwin (2009) 没有引用，而 V6 自己已经指出了它。
3. 没有战略性掩蔽："Competition among practices within a domain, endogenous domains and strategic masking remain open." 可是评估意识与 sandbagging 恰恰是 AI 评估中最相关的情形。

**单一改动**：用真实数据锚定一个量。例如用 LLM-judge 面板数据估计 β 如何随同族份额变化，检验预测(d)：检测延迟随同族份额增长。

## 审稿人2：政治经济/国际关系/治理

### 稿A
**强项**
1. 给对立路径以最强的版本，例如"赢、自缚、分享"（Ikenberry、Kindleberger、Wohlforth、Olson）。Alchian 和 Friedman 被并入理论，而不是当作靶子；§7.11还预先登记了"受监管竞争胜出"的条件。
2. 把 Stigler 式俘获从"偶发"推进到"被选择"，并给出可检验的预测：影响力随份额的平方增长；在位者支持可占有的纠错、反对不可占有的纠错；俘获有两个方向。
3. 定义7.12用 Abbott 等人的约束性维度描述各种安排，并事先为五项现行政策画了像，便于政策学者使用。

**最致命的批评**
1. 核心政策论证与俘获文献相冲突："A restraint that covers every capable carrier is invisible to the selection that would displace it." 引理3.3(2)只对等额扣减成立，而普遍适用不等于等额负担。统一规则的合规成本各不相同，正是在位者"抬高对手成本"的工具，文本自己的预测5也这样说。"协调为何有效"的全部重量都压在这个被过度解读的引理上。
2. 有重新贴标签、因而不可证伪的风险："Each alternative that succeeds does so by changing what the system selects for, whatever it is called." 政策画像把出口管制判为 "No: it constrains rivals, and its aim is a lead"。但按定义7.12的描述性定义，出口管制显然改变了从行为到份额的映射。分类看上去取决于对方向的偏好。
3. 诊断的证据比结论薄。把机制连到现实的 T4 自评为 "Gap"，"Not measured in this register"；T2 依赖一篇预印本；作者的先导实验 "did not support it"。再加上 "A civilization on another planet ... would face the same pressure" 这样的句子，全文读来像宏大理论，而不是可检验的政治经济学。

**单一改动**：把"一股压力"的宏大诊断换成一个可证伪、考虑负担分布的主张：在合规成本各异、存在豁免时，统一规则何时仍然中性。再用一组数据检验，例如 T-B：把 AI 规则制定中的公开评论按企业规模、以及对两类纠错的立场编码。

### 稿B
**强项**
1. 正面回答了 "Is this regulatory capture renamed?"，在单位、选择者、对象三处作了区分，在 Stigler、Dal Bó、Carpenter、Kwak 的文献中定位准确。
2. 治理原则可以操作：
   - 降低规则制定的可占有性：接口中立的标准、轮换的留出集、按结果采购、起草者的利益冲突规则；
   - "keep exit cheap"；
   - 按控制单元计算独立性；
   - 与欧盟 AI 法案的公告机构、FDA 用户费的经验（Carpenter 2008）相对照。
3. 关键石和 "a way of succeeding can outlive its origin" 给出了改革顺序的理论，对改革者有用。

**最致命的批评**
1. 没有行动者："Shares and stocks belong to practices, not to actors." 模型里没有联盟和反动员（Becker 1983 未引用），也没有选举与舆论。它是合作系统，只能产生锁定，不能产生改革周期，而管制史恰恰以周期为特征。
2. 识别只停留在方案上。作者承认 "Correlations in funding or personnel alone do not show capture"，却没有完整分析过一个真实场域。
3. 政策的代价没有权衡："reforms must overshoot the conditions under which it arose"。过冲会压制正当的专业参与、拖慢规则制定，而作者自己也承认 "a beneficial innovation may need standards that support it"。

**单一改动**：加一个完整的案例，例如评估机构访问条款或标准起草席位的时间序列，展示证书和关键石诊断能得出与普通俘获理论不同的结论。

## 审稿人3：AI 哲学/伦理

### 稿A
**强项**
1. 规范前提显式、可以拒绝："stated so that a reader can reject one and see what follows"。V1–V5、标准D、规范性分歧N1–N3分开列出，并承认期望值准则与贴现准则会给出不同的结论。
2. 文本声明 "The analysis judges games, not acts"，"癌症"的意象也明确不用于个人、民族或机构。"we are one" 被拆成五个部分，并承认 "The norm that everyone affected has standing is declared, not derived."
3. 区分 O1–O4。O4不受保护，以免"行动者生存"暗中保护在位者。对善意赢家路径的承诺问题也分析得清楚，这在 AI 伦理文献中少见。

**最致命的批评**
1. 未经论证的形而上学进入了正文："We are part of a larger process of becoming, and that process is good." 这句话不在 V1–V5 之中，却承担着"意义是肯定的"这一判断的重量。V4 的特定传统来源、"讲赢/讲理"在10页内无法辩护，还会损害匿名。
2. "错误"是按构造得出的。命题3.9先定义含 κ 的 W，再证明按 θ=κ 行动可以使 W 最大，所以 "Part (3) is the precise sense in which an isolated self-model is an error, not a preference" 近乎同义反复。实质在于 κ 有多大，而文本承认 κ "not yet measured in size"，因此 "Ψ is locally rational and systemically false" 中的 "false" 并没有确立。"That the lemma leaves only this route is a theorem" 是同一类越界：Price 恒等式既排除不了制度学习，也排除不了局部可逆的试验。
3. 预防原则用得不对称。D 要求所有政策用同一个 Θ，但结论依赖 "No evidence today excludes the case in which correction falls behind on the present path"。同样，也没有证据排除合作安排自身的失败（C4 未知）。Θ 对称时，D 未必推出 "warranted now"。此外，V4（权威因改善生活而正当）与 V3（可争议性）之间有张力：绩效合法性正是不受问责的权力最常用的辩护，正文没有处理。

**单一改动**：加一张"结论—依赖"表，写明每条实践结论依赖哪条价值、哪个定理、哪项证据。在对称的 Θ 下重做 §10 的判断，如实报告结论是否还成立。删去形而上学的句子。

### 稿B
**强项**
1. 价值中立做得克制："A positive baseline cost is relative to a stated baseline, not a verdict on harm or legitimacy"。病理 P1–P3 与递归本身分开，并有"生成型"作对照。
2. "A normative test, not derived from the model, asks three questions." 关闭选项的三问有真实的哲学内容：是否公开；是否独握重开的钥匙；是否仅因托管变化就使他人不能。
3. "Treating objections as evidence that the objector is captured would reproduce the loss of correction it describes." 作者对理论的自我封闭有自觉。

**最致命的批评**
1. 规范前提埋在局限一段里："Acting on the results rests on three normative premises"。治理建议的规范基础只有一句话。
2. 俘获的定义太薄。"capture-dependent if c_i>0" 只看基线成本的符号，没有说明影响力何时变得不正当（受托目的、受影响者的地位），因此正当的专业影响与俘获无从区分。
3. 对伦理受众的意义有限。谁承担被掩蔽的伤害、分配问题、受影响者的参与，几乎都没有讨论。

**单一改动**：把 V6 的定义4.1和 V3 移入 B 的第3节。定义4.1要求俘获的三项条件分别成立，其中包括受托目的受损；修订与俘获则按"谁来修订、受影响者是否保有反对的地位"区分。

## 领域主席元评审

**预计决定**
- **B：接收（海报或短报告）的可能大于拒稿，约六成。** 三位审稿人都在边界到弱接收之间，分歧小。主要风险有两个：没有经验锚定；伦理受众可能觉得意义有限。
- **A（按现状）：拒稿，接收可能约一到两成。** R1指出了承重命题的错误；R2判它为不可证伪的宏大理论；R3欣赏它的规范架构，但不能为其中的形而上学和不对称推理背书。另有两项程序风险：
  - 匿名：全文有20处 "the author" 或 "author's corpus"，还有可检索的自造词 molochlization 和"讲赢"；
  - AI 起草：头注写着 "Every sentence is AI-drafted"，须按 CFP 的 LLM 政策披露，作者也必须能为每个证明负责。
- **不要同时投 A 和 B**：两稿的 §4 大量重叠，会触发重复投稿规则。

**决定性考量**
1. **贡献与篇幅之比。** B 只有一个问题、六个命题，证明放在附录；A 即使只取核心也有数十个结果，外加八项要求、十一项检验，审稿人在正文里一个也核验不了。
2. **严谨性。** A 的承重结果都有可以指出的漏洞，包括5.7/5.16、3.3(2)/6.7、3.10、5.14向多方的推广，以及 R1–R8 的"必要性"。B 中未发现错误。
3. **姿态。** A 的"无论叫什么"和跨星球的普遍性，会让政策审稿人判它不可证伪；B 的 "When the account loses force" 一段反而增加了可信度。
4. **A 的独特价值。** 决策标准、规范性分歧、AI 作为工具与化身、嵌套奖励回路，都是 B 没有的，也正是本会伦理受众想看的。这些值得保留，但需要合适的载体。

**对 V6 派生稿最有杠杆的五项改动（按序）**

| # | 改动 | 所需时间 |
|---|---|---|
| 1 | **只选一条主线，按10页重切。** 推荐"B+"：以 B 为骨架，加入 V6 的命题4.4（AI 降低控制成本时独立纠错的增速条件；拆分只延迟；三阶矩）、定义4.1和注4.7（保守警报；掩蔽隐藏水平而不隐藏动态）。"赢的元吸引子"只在引言里作一段动机、在结论里作一段展望。若坚持 V6 主线，只留四个结果：命题3.5、引理3.3(1)、修正后的5.7、修正后的6.7，其余放附录或另写一文。 | 2天 |
| 2 | **修正承重错误，降低主张的强度。** 5.7写成精确的执行条件，5.16改为条件性陈述，不再称两难；3.3(2)限于等额负担，6.7(3)与 R8 随之修改；删去3.10的 "is a theorem"；5.14只限两方；R1–R8 拆成三栏：模型内的必要条件、充分保障、规范要求。 | 改措辞2天；重新推导和新检验需1–2周 |
| 3 | **去掉不可证伪的框定。** 删去 "whatever it is called"。全文一致使用定义7.12的描述性定义：出口管制也改变了选择，只是方向与覆盖不同。把 §10 的判断写成对称 Θ 下的条件性结论，承认合作安排的风险未知。 | 2天 |
| 4 | **清理规范部分与匿名问题。** 加价值—结论依赖表；删去 "process of becoming is good"、癌症意象、外星普遍性和思想史谱系；V4 改为不指认来源的一般表述，并处理它与 V3 的张力；删去所有 "the author's corpus/pilot"；按 CFP 处理 AI 起草的披露。 | 2天 |
| 5 | **加一个经验锚点。** 三选一：T-B（编码规则制定中的公开评论，检验 p² 与双向俘获）；LLM-judge 面板实验，估计 β 与检测延迟；T-A（安全框架修订的事件研究）。这是从"弱接收"到"稳接收"的主要差距。 | 2–6周 |

**模拟估计与建议。** 2天内完成第1–4项后，"B+"的接收可能约七成；坚持 V6 主线的 A′ 约三到四成。第5项能再提高一档。建议本届投"B+"。V6 的整体理论更适合写成长篇期刊稿或专著，不宜直接压缩成会议稿。
