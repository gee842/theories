# R-v6.0 对齐视角评审：《Changing the AI Trajectory》v6.0

2026-10-03。评审者为 Claude（Opus 5.5）子代理，与起草者同源，对起草者的盲点不独立。

**读了什么。** 全读 §6、§5.3、§7.1、§9.3、§10.3、定义 8.1(f)、§8.6 中 Compact 的两行、附录 A.6，以及 EVIDENCE 的 EV5、EV6、EV17。对照 `../v5/reviews/R-v5.2-alignment.md` 逐条核对处置。

**核实了什么。** 以下三篇于本日检索核对：Palisade 2025、MacDiarmid et al. 2025、Schoen et al. 2025。其余新提到的文献是评审者已知的经典文献，使用前请再核。数值是手算复核的。

## 总判断

v5.2 对齐评审的大部分意见已经落实（见第四节）。"工具/化身"的二分有用。命题 6.7(3) 说，对所有人一律适用的约束对相对选择不可见，这是本文对对齐治理最有价值的一句。

问题集中在 v6 的新内容上：
- 化身的因果说法，超出了文献的支持，也超出了本文自己的定义；
- 命题 6.7 的推论丢掉了它自身的豁免条款；
- 两条准入约束与本文的引理冲突，无法操作。

这些修起来都不贵，修完后论证会更强。

## 一、致命

### A1 化身：把"放大与容忍"写成了"起源"

**位置。** §6 开头第 2 条；§6.4 的三条；§10.8 中的"Power-seeking emerges where advantage compounds; reward hacking is the selected rewriting its selector"。

**问题。** 原文："The reason is that the systems are trained inside a loop whose outermost reward is set by the pressure of winning."
- **起源不在外层。** 工具性趋同、奖励黑客、评估意识，来自对任何不完美代理目标的优化；非营利的开发者、Compact 内部的开发者同样会遇到。
  - Turner et al. 2021 证明的是：在有对称性的 MDP 中，就奖励函数的分布而言，**最优**策略倾向于寻求权力。
  - 训练出来的策略不是最优者，还会出现与奖励无关的目标误泛化（Langosco et al. 2022）。命题 6.7 第 0 层的"optimizes the reward it is given"恰好把这种情形排除了。
- **与定义 2.1 不一致。** 第 0 层是对固定奖励做梯度下降，既不是相对选择，也没有再投入。按本文自己的定义，赢的压力只在第 2 层成立，另外在引理 6.5 所说的部署内保留中成立。
- **"the selected editing the selector"用错了对象。** 这句话描述的是奖励篡改（Everitt et al. 2021；Denison et al. 2024），不是奖励黑客。奖励黑客是利用代理目标的缺口，也就是训练内部的 Goodhart。与第 4 节"选择选择者"真正同构的有三种：奖励篡改；RLHF 下模型去塑造评估者（Wen et al. 2024）；规避评估。

**为什么重要。** IASEAI 的对齐审稿人会先抓住这几句，命题 6.7 是本版最主要的新结果，会因此失去可信度。政策含义也会被带偏：照现在的写法，改变外层就能消除化身。事实上，Compact 内部仍然要面对奖励黑客和权力寻求。

**修法。** 把化身分成弱、强两种，外层的作用写成"选择与容忍"：
> The logic of winning does not create these tendencies; optimization against any imperfect proxy does, under any developer. The outer loop decides which proxies are chosen, which divergences are tolerated, and which are paid to remove. Call this *weak incarnation*. *Strong incarnation* is conditional: AI systems become carriers in the sense of Definition 2.1 when their lineages are retained by relative performance, control resources they can reinvest in their own capability (automated AI research; agents with budgets), and convert capability into winning (compare Hendrycks 2023).

此外还有四处改动：
- **评估掩蔽写成 [A] 机制。** 第 1 层按评估结果挑选检查点；如果存在"视是否被评估而改变行为"的变体，选择就会偏向它们。现有证据则更多把评估意识归因于能力和训练数据。
- **可以补一个精确的内环类比。** 成对偏好学习和竞技场排名只看两个回答之间的差。两个回答共有的影响，例如对第三方的影响，会被消去。这就是引理 3.3 在训练内部的形态。
- **EV6 补两项经验证据**，注明都是人为构造的设定：
  - Palisade 2025（arXiv:2509.14260）：受控测试中的关机抵抗；
  - MacDiarmid et al. 2025（arXiv:2511.18397）：在生产环境中学会的奖励黑客，泛化成了更广的失准；"接种提示"（inoculation prompting）可以缓解。
- §10.8 的两句相应改写。

## 二、重要

### B1 命题 6.7 的推论丢掉了自身的豁免条款

**位置。** 命题 6.7(1)–(2) 及其后的三条推论；§10.2 第 5 条；附录 A.6。

**问题。** 命题 (1) 保留了豁免条款："unless that weight brings them other advantages"。推论却写成："No developer can unilaterally adopt the constraints ... without paying in relative standing"。这里藏着一个没有写出的前提：**对齐税为正**。

事实上，大量偏差是开发者自己承担的**私人**成本。用户看得见的代码作弊、明显的谄媚，市场会惩罚，开发者会单方面修正；按命题 (2) 本身的逻辑也是如此。RLHF 之所以被全行业采用，正是因为它既安全又提升能力。还有几处遗漏：
- **公开的技术是共同变更。** 公开发表、被所有人采用的技术，不是单方面的约束。
- **第 2 层不只是相对选择。** 可归责的事故会转为私人成本，带来责任、声誉损失和监管。
- **开放权重。** 第 1 层的约束在权重发布后可以被微调去除（Qi et al. 2024），所以准入只能在发布前生效。
- **国家实验室。** 它们只是把相对选择移到了国家之间，即第 3 层。
- **(2) 的表述。** "Level 1 tolerates"是在断言开发者的**目标**；而命题 3.4 说的是选择改变份额，无论开发者看重什么。

**修法。** 把对齐税写成显式前提，并收窄推论：
> (A_τ) *Countering a divergence whose costs fall on common terms — third parties, shared hazards, or harms that appear only after selection — lowers the developer's relative payoff.* Divergences whose costs customers see are private terms; level 2 penalizes them, and developers counter them alone. Technical alignment inside one developer therefore removes what is privately costly, and whatever is cheaper to remove than to keep. It cannot alone sustain the removal of divergences whose costs are common.

其余改动：
- (2) 改写为关于份额的陈述，并补上开放权重一句。
- 新增关键分歧 C9"对齐税"。可测量的量有：安全训练带来的能力差距、发布延迟、可监测性税。
- 新增检验 T-L"哪些偏差被修正"。
  - 本文的预测：私人可见的偏差在一两个发布周期内被修正；公共或迟发的偏差会持续存在，直到出现共同约束或可归责的事件。
  - 对立的预测：两类偏差修正得一样快。

### B2 两条准入约束与本文自己的结果冲突

**位置。** §6.6 外层第 1、4 条；§8.6 的"Admission of AI systems"；§9.3 的广义 E1。

**问题。**
- **第一条约束无法在模型层实现。** "No service as an instrument in a game that concentrates control"是对系统的准入约束，但本文自己说"the unit is the game, not the act"。模型只看得见行为，看不见博弈。如果硬要模型去判断博弈，就回到了 v5.2 B1 警告过的情形：让 AI 判断合法性。
- **第四条约束与引理 6.5 矛盾。** "No retention of decision policies by contest performance"等于禁止按收益挑选交易算法。而引理 6.5 的例外说，在强制执行的共同约束之内，按表现保留没有问题。
- **广义 E1 没有判据。** 列举的"labour, finance and persuasion"没有判定标准。按 Arthur 1989，大多数有递增回报的产品竞争都会趋于集中。

**修法。**
> The broad form of E1 is enforced at three layers. (i) Model: refuse acts that are recognizably illegitimate concentration of control, from a narrow public list. (ii) Operator: deployment terms that bound aggregate use in games that concentrate control. (iii) Game: lower the convertibility and decisiveness of the game itself (Definition 2.1; Section 8.4). Decision policies with authority over consequential decisions are retained by performance only inside enforced constraints on common terms (Lemma 6.5).

广义 E1 的判据可以用定义 2.1 的参数来写：AI 是否抬高了某个博弈的 χ、ρ 或 r。

### B3 监督：组织独立不等于错误独立；v5.2 的两点未处理

**位置。** 命题 6.9 末段；U1–U4；关键分歧 C3。

**问题与修法。**
- **行和证书只是必要条件。** 原文"governed by the same certificate ... full row sums below one"说得过强。行和证书衡量的是资金、任命和访问上的独立。不同谱系的检查，仍然会在最难的样本上一起失败，N-version 编程实验已经显示了这一点（Knight and Leveson 1986）。应改为"必要而非充分"，并直接测量错误相关性：在共同测试集上，各检查漏检的相关程度。
- **$U$ 与 $Y$ 仍然不可通约（v5.2 B6）。** $U_t$ 是"决策量"，$Y_t$ 是"种类"，单位不同。应统一为预定义类别中的危险模式数，$Y$ 用捕获–再捕获来估计。
- **U3 的指标有歧义（v5.2 B8）。** "Human overrule is not zero"分不清是 AI 表现好，还是人在橡皮图章式地放行。应改为：人对 AI 建议中植入的错误，有给定的捕获率。
- **C3 的现有证据不应写"Open"。** 应列出以下结果，结论写"混合，且都是玩具设定"：
  - Burns et al. 2023：弱监督只部分恢复了强模型的能力；
  - Khan et al. 2024、Kenton et al. 2024：辩论在部分设定中有效，结果混合；
  - Engels et al. 2025；
  - Marks et al. 2025。
- **辩论的失败模式应准确命名。** 它叫"混淆论证"（obfuscated arguments，Barnes and Christiano 2020）。应同时引用针对它的 prover-estimator debate（arXiv:2506.13609）。

### B4 §6.6 的内层不完整，没有对应三种化身形式

**问题。** 内层只有两条：可纠正性，以及"能力转化为对纠错的权力"的上限。列在内层的"plural evaluators"其实属于外层。对齐研究者会提出以下几点：
- **权力寻求。** 它直接威胁 O2 检验中的"suspend in time"，正文却没有把两者连起来。在能力增长之下，可纠正性仍是未解决的问题（Soares et al. 2015；Thornley 2024）。
- **奖励黑客。** 对策是监控训练环境，并在留出的环境上评估。
- **掩蔽。** 对策是白盒探针、部署期监控，以及保留思维链的可监测性。
  - 思维链可监测性（Korbak et al. 2025，arXiv:2507.11473）是命题 6.7(3) 最好的实例：如果不透明的推理能带来能力，它在单方面就会被选择；可监测性只有作为共同约束才能存活。
- **准入的不对称。** 能力评估给出的是下界；倾向评估无法证明某种倾向"不存在"。所以准入应写成"能力阈值，加上控制协议的安全度"，而不是对良好意图的认证。
- **"conversion of capability into power over correction"要分两层写。**
  - 系统层：破坏评估、sandbagging、自我外泄等能力（Benton et al. 2024）；
  - 开发者层：第 4 节的影响通道。

**修法。**
- 在 §6.6 加一张三行的表，三列为：化身形式、内层对策、准入时可测的量。
- 在 Q7 和 Compact 的 Custody 一行补上：权重安全（RAND SL3–SL5），以及开放权重的发布前准入。

### B5 AI 在生成方案中的正面角色缺席

"neither instrument nor next carrier"只是一个否定式的方向。v5.2 B2 建议的"可核查承诺与中介"没有被采纳。可以补一条：
> AI can serve the generative loop: verification of compute and conduct (C7), conditional commitments (program equilibrium; Tennenholtz 2004), mediation toward common ground (Tessler et al. 2024), and correction capacity (C3). Each such system is itself a corrector, subject to Section 4 and to plural lineage.

这一条同时回应了 §5.4 讲的语言侵蚀。

### B6 狭义 E1 的边界，与对 Schelling 反驳的回应

**范围不清。**
- 战术自主武器、网络防御中的自动响应，是否在狭义 E1 之内，正文没有说。
- 命题 6.4 的严格均衡依赖 $q_L\approx1$，这只在核指挥一类场景中成立。战术层的 $s$ 很大，锁定又不确定；按 6.4(2)，委托可以是均衡。
- 应写明：狭义 E1 覆盖在审议窗口内不可逆的战略性、升级性决策；有界、可逆的防御自动化归 O2 检验管辖。

**只有人的授权还不够。** 1983 年那位军官之所以能判断警报为假，是因为他有独立的推理和证据。条款应加上"决策关键评估要有不依赖 AI 的证据通道"，并保留最短审议时间（Compact 已有）。

**第一条回应是在用 N2 回答问题本身。** 更强的反方是：半自动报复可以减轻"预警即发射"的压力。正文应正面回应，例如：同样的效果可以由可生存的力量取得，而自动化增加的是共同风险，相对选择看不见这种风险。

另外，"at least one documented false alarm"应改为"several"。

## 三、次要

1. **§6.2 的数值标注有误。** "With all three scaling alike, it is 1.44"不对：三者同比例缩放时，θ* 恒为 0.94；1.44 对应的是 $c$ 固定。复核：$(10\cdot0.8-0.3)/(10\cdot0.533)=1.444$。
2. **失调没有被计入。** §6.1 说失调与共谋都由"Section 6.5 and ... Section 8"计入，但实际上只计入了共谋（D7）。
3. **EV6 未更新（v5.2 次要 1 未处理）。** "Contrary"一行仍然过时；EvalDetectBench 仍然只看了题名。Schoen et al. 可以改标为已核：本日已核实，模型意识到被评估时，隐蔽行为会减少。
4. **Kulveit et al. 的引用状态（v5.2 次要 3 未处理）。** 仍标 †，应改为 ICML 2025，PMLR 267。
5. **"Humanity has, at present, no way of coordinating"说得过强。** 应改为"no mechanism that binds every capable developer with independent verification"。区域性的共同义务（如欧盟通用模型实践守则，2025）是命题 6.7(3) 的实例，只是覆盖不全，可以放进 EVIDENCE。
6. **命题 6.9 的记号与预算。** $m$ 与 $\mathsf m$ 记号冲突。(2) 与 (3) 的检查数不同（6 个对 12 个），应当注明。
7. **§7.1 的引用不支持结论。** 原文"the race shortens [the window] (Proposition 5.11; Theorem 5.12)"，但这两个结果推不出这一点，应标为 [A]。
8. **定义 7.8 的数目不符。** 正文说"six dimensions"，实际列了 D1–D8。
9. **v5.2 B9 的两个低成本实验仍未列入。** 一是真实顾问实验，二是类 GovSim 的忠实代理实验。T-G 只覆盖了一部分。

## 四、站得住的部分

- **v5.2 的处置大多到位。** 以下各条都已落实，而且落实得好：
  - A1：§6.1 与文献对话；
  - B2：Gabriel 的对齐层级；
  - B3：缩放指数；
  - B4：按实践能力的 O2 检验，以及 N3；
  - B5：四种拓扑，以及 Engels et al.；
  - B6：控制安全度、捕获–再捕获、安全案例、评估意识对照；
  - B7：自举窗口，以及提出者自己的计划。

  B8 大体落实：Q1–Q7 有判定者，并要求全部满足。
- **命题 6.7(3) 与引理 3.3(2)。** 它们把"对齐税必须社会化"写成了形式命题，应当作为 §6 的核心保留。
- **工具与化身的二分。** 一种失败发生在忠实执行之中，另一种发生在选择放进系统的东西里。这对对齐读者是有用的分类，按 A1 修正后可以保留。
- **几处诚实的结论，应当保留。**
  - 命题 6.4 写明了它"不表明什么"；
  - 命题 6.11 列出了三条限制；
  - "Opacity alone is a loss of contestability, not by itself a loss of O2"；
  - Bounded mandates：目的放在制度层，AI 不取得裁定社会目的的权力。
