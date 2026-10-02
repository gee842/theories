# Selecting the Selectors v3：下一版的思路（待 Ren 确认）

*Claude Opus 5.5 于 2026-10-02 晚撰写。依据：第二轮四份评审（`reviews/round2/`）、GPT 对 v2 的评审与交接（`sources/03-meta-attractor/2026-10-02-selecting-the-selectors-v2-review-gpt.md`）、第一轮评审与 GPT 交接稿，以及 Ren 的判断：“如果修完后的判断依然是50%，那说明这一篇写的有问题，theories显然不止当下的潜力”。按 Ren 的指示，本版不做实验，不做预测。下面的命题都已推导到能写证明的程度，正文要等 Ren 确认思路后再写。*

## 一 诊断：v2 为什么封顶在一半左右

四位评审给 v2 的估计中位约 30%，修完必改项约 45%。GPT 的结论是“不需推倒，但需实质修改”。问题不在理论，而在论文的写法。

1. **数学放错了地方。** v2 的形式核心恰好落在理论最通用的部分：
   - 成本收益梯度。它的形式已见于生态位构建的垄断条件和 Olson。
   - 阈值网络与 k-core。
   - 一个假定的线性掩蔽项。

   评审因此判定“标准工具，已知形式”。理论真正独特的部分仍是文字：
   - 选择器本身被选择；
   - 纠错能力在结构上被选择淘汰；
   - 封闭会移除本可触发纠错的变量和行动者。
2. **宽度压过深度。** 8.4 页里有六个命题、四个注、约二十个新术语、九条治理原则。每块只有一段，边缘处主张跑在证明前面，于是被查出约十五处可核查的错误。
3. **与 AI 只是类比。** 载体是组织，评估掩蔽 β 来自假设。对齐只经由成本参数进入模型。模型量与 AI 评估中可测的量没有对接。
4. **定位错了战场。** 写成“捕获理论”，就会被拿去和成熟的规制捕获文献比，在那里显得单薄。理论最有力的东西是一个关于纠错的结论：递归选择偏向控制，而饿死纠错。

## 二 理论的潜力在哪里：v3 的主线

meta-attractor 理论最核心的区分，是“自我复制增强的同时外部纠错削弱”的病理型，和“自我复制增强的同时纠错也增强”的生成型。v2 把病理当成附加条件，是外加的。v3 要把它变成被推导出来的结论：

> **递归选择奖励对选择器的控制，同时饿死对选择器的纠错。前提是控制的回报可以留给自己，而纠错的回报不能。**

这一句同时回答了四个问题：
- 为什么病理不是偶然；
- 为什么集中和跨域覆盖（通用 AI）是危险的放大器；
- 为什么独立纠错必须由竞争之外的制度供给；
- 应该调哪些量。

“meta”在这里有了形式内容：被选择的对象，是改变选择环境的投入，以及纠正选择环境的投入。

v3 的五个结果按这条主线排列：控制、纠错、监督门槛、检测、场。

### 结果一：控制能力何时被选择（修正并加强 v2 命题 2）

- **局部选择梯度。** W′(q) = χ yᵀMy − C′(q)，其中 M_ij = a_i b̂_ij L_i / d_i。按 GPT R12，表述为局部梯度，不写成 exactly when。均值变化要求有变异、忠实传递。
- **规模门槛（新）。** 回报对载体**自身**的成功是二次的。小载体投资控制不划算，稀有的高能力载体无法入侵。这是把图 2 的错误改对后得到的更强结论：控制能力只在已经很大的载体中被选择，**它放大支配，而不是制造支配**。顺序是先支配、后控制。
- **范围。** 分开两种比较：
  - 固定每域份额时，回报随域数超线性增长；
  - 固定总规模时，回报有界，只有在跨域转换强于域内转换（φ̂ > η̂）时才随范围上升。
- **辅助推论。** 只在二次成本下成比例；在一般凸成本下，只能说被选择的能力不下降。
- **棘轮。** 在固定成本下，捕获集、core 和级联闭包随平均能力单调。计入能力成本后，需要充分条件 c_i b̂_ij ≥ γ b⁰_ij。

### 结果二：纠错为何被选择淘汰（新，主线的另一半）

设纠错能力 u：它提高规则支持被纠正的速度 d，或降低掩蔽，惠及所有人。

- 对任何收益里含有该实践规则支持的载体（在位者），u 的选择梯度为负：纠错削弱它自己的支持。
- 对替代实践的载体，梯度为 σ·G_u − C_u′(u)。σ 是它在替代者中的份额，G_u 是替代者整体的边际收益。分散的挑战者搭便车，只有集中的挑战者或竞争之外的机构会供给纠错。

结论：控制被大的在位者过度供给，纠错被在位者反对、被分散者少供给。这就是病理型元吸引子的选择机制。它的形式对应已知的“二阶公共品”（制裁和监督是公共品）。v3 的新意在于把它放进同一个递归选择模型，与控制能力的选择直接对照，并由此推出结果三。

### 结果三：独立监督的最低门槛（新，整合性结果）

评估域不被捕获的稳健条件是行和小于 1（v2 命题 4d）。如果只按当前的转换计算，会低估需要多快的纠错，因为选择会培养出更多控制能力。

在长周期和统一纠错率 d 下，把被选择的能力 q* = χŶ/(γd) 代入评估域的行和，得到最低纠错率：

  d* = [ a_E B⁰_E + √( (a_E B⁰_E)² + 4 c_E a_E χ Ŷ B̂_E / γ ) ] / (2 c_E)，

其中 Ŷ = Σ_ij y_i a_i b̂_ij y_j 是支配载体的规模和范围项。

- χ = 0 时退化为不计二阶选择的朴素门槛 d₀ = a_E B⁰_E / c_E，且 d* ≥ d₀。
- d* 随可占有性 χ、支配载体规模的平方（Ŷ ∝ λ²）、跨域范围和能力向评估的转换 B̂_E 上升。
- d* 随能力成本 γ 下降。所以**能干的 AI 助手降低控制成本，会抬高独立监督的门槛**。
- 拆分支配载体（反垄断、互操作）使 Ŷ 按份额的平方下降，从而降低门槛。
- 有限周期（L < 1）只会降低 q*，所以按 L = 1 算出的 d* 是保守的充分门槛。

这是全文最可引用的结论：**忽略二阶选择，会系统性低估让 AI 评估保持独立所需的纠错强度。** 它把控制、纠错、集中、AI 辅助和治理杠杆连成一个可以计算的式子，正对 GPT 所说“原创性应集中在连接结果上”。

### 结果四：被捕获的评估如何隐藏伤害（按 GPT R1–R4 和我方 R2 重写）

- **有效掩蔽从评审构成推出，而不是假设。** m = x_E β_in + (1 − x_E) β_out，其中 x_E 一开始就定义为评估中出自被评估谱系的份额。形成域通过 β_out 起作用：所有谱系都在支配者的产出上训练。
- **检测时刻与四类结局。** 及时检测、迟到检测、观察窗内未检出、永久静默。β = 0.6 是迟到报警（约 t = 2359），不是永不报警。
- **永久静默的条件。**
  - V → 0 时，必要条件是 limsup m ≥ V_alarm/K；充分条件是此后 m 一直不低于该值，且此前没有报过警。
  - V 趋于正平衡 V* 时，阈值降为 m ≥ (V_alarm − V*)/(K − V*)。**停在报警线下方不远的中等伤害，只需很小的偏差就能永远隐藏**（例：V* = 0.5 时 m ≥ 0.2）。这是 GPT 反例给出的、比原稿更锋利的结论。
- **延迟定律。** 仅在指数下降和常数 m 的情形下陈述。
- **多样性的边界。** 等相关误差下，面板平均可降低方差 σ²[r + (1 − r)/n]，但不能消除共享的系统偏差。替换句：“Diverse panels can reduce some evaluation errors, but family diversity alone does not bound shared systematic masking.”
- **校准。** 同家族减异家族只能识别 β_in − β_out。绝对掩蔽要在多个损伤水平上对照客观真值，β = (S − V)/(K − V)。文献里的“几个百分点”不能当作 β。

### 结果五：跨域场（压缩，细节放附录）

保留 v2 中正确的部分：
- 配置稳定性，并补上 c_i > 0 的标准假设；
- 证书：孤立检验不能认证，行和能认证，core 是精确判据，评估域可以稳健设防火墙；
- 带种子条件的级联；
- 改革与再吸收；
- keystone 集合。按 GPT R7，改为可多项式求解的最小 keystone 集，并给出算法；NP 难的是“清空 core”和预算化的最大坍塌，另作说明。

这部分支撑结果三，不再独占篇幅。

## 三 论文结构与篇幅（主文 10 页上限，目标 9.5 页）

| 节 | 内容 | 页 |
|---|---|---|
| 1 引言 | AI 评估中赢家提供选择器的具体问题；核心问题（递归选择奖励什么）；主线句；五个结果的通俗表述；贡献与 Statement of Contributions 合并为一段 | 1.0 |
| 2 相关工作 | 诚实完整的定位，见第五节 | 0.8 |
| 3 模型 | 场模型；评估域构成与有效掩蔽从一开始就定义；中性的 meta-attractor 定义与病理判据（病理 = 选择偏向控制、偏离纠错） | 1.2 |
| 4 控制 | 结果一 | 1.4 |
| 5 纠错 | 结果二 | 0.8 |
| 6 独立监督的门槛 | 结果三，附一张小图：d*/d₀ 随 χ 和规模的变化 | 0.9 |
| 7 选择器被选择：检测 | 结果四 | 1.1 |
| 8 场层面的审计与改革 | 结果五，压缩版 | 0.6 |
| 9 AI 与治理 | 参数映射表（每个量对应的 AI 渠道、可测指标和现有证据）；监督技术的准确描述；设计规则表（每条标明由模型推出、映射或规范，以及现有工具和本文的增量） | 1.3 |
| 10 局限与结论 | | 0.4 |

v2 中以下内容删除或移入附录：
- 第 3 节的“认识封闭分层”“实践生态”两段，压成一句；
- 误差可达图和 min-cut 的 Remark，降为治理表中的一行；
- “关闭测试”，按 GPT R11 改写为规范预警，放进治理表；
- 六域数值例子，移附录，只作说明；
- 附录 D（离散版本），在正文引用一次或删去。

## 四 评审意见的处理方式

| 问题（来源） | v3 的处理 |
|---|---|
| 图 2 与方程 (3) 不一致（R1、R2、R4） | 改为按自身份额计算，并写成规模门槛和“放大而非制造支配”的结论（结果一） |
| 棘轮漏了成本（R2、GPT R8） | 走保守路线：命题限定在固定成本下，并给出计入成本时的充分条件；数值只作说明 |
| 可核查错误（R2、R4、GPT R1、R2、R5、R6、R7） | 全部按评审给出的替换文本改正：永久静默条件、β = 0.6、辅助推论、范围推论、keystone、0.96、“not which can exist”、“sets of selectors”、核心表述 |
| 形成域机制推不出面板失效（R2、GPT R4） | 用有效掩蔽 m 显式写入 β_out |
| β 与百分点混用（R1、R3、R4、GPT R3） | 删除这个推断，改写为绝对校准的测量协议 |
| 可扩展监督描述有误（R1、R2、R3） | AI control 的可信模型是同一提供方的弱模型，其 β_out > 0 恰好支持本文论点；debate 的裁判弱而非不独立；weak-to-strong 用“earlier generation” |
| 新颖性说过头（四位都提） | 第五节的定位；Statement 改为“new results in this setting, obtained with standard tools” |
| 对齐只经由成本（R1、R4） | 改为“operator alignment is not sufficient”；对齐通过降低 γ 抬高 d*，影响是双向的（也可以加快纠错），都在结果三中显式出现 |
| 治理可操作性（R3） | 设计规则表；补上专业性与独立性的权衡；补充现有工具（SOX/PCAOB、评级机构改革、监管市场、DRCF、JTC 21、AISI 访问协议） |
| 识别段（R2、R3、GPT R10） | 区分结构识别与因果识别；补上 μ 项与核参数；可行的自然实验路线 |
| 清晰度（R4） | 主线一句话；术语减半；记号去重；每个命题配一句证明思路；摘要 170 字左右 |
| 文献错误（R3、R4） | Laurito、Goel、Greenblatt、Narechania、Büthe–Mattli、Carpenter 2008、Kwak 年份、EU AI Act、Abdalla |

## 五 定位策略

先承认已知的形式，再说清楚新在哪里：

- **形式先例：**
  - 生态位构建困境与垄断（Krakauer–Page–Erwin 2009；Lehmann 2008）；
  - 集体行动与寻租（Olson 1965；Tullock 1967）；
  - 可占有性（Teece 1986）；
  - 二阶公共品与制裁（Yamagishi 1986 等，待核）；
  - 阈值级联与 k-core。
- **制度与捕获：**
  - 规制捕获、文化捕获、深度捕获；
  - 认证中介与评级（Lizzeri；Strausz；Bolton–Freixas–Shapiro）；
  - 内生制度（Greif–Laitin；Acemoglu–Egorov–Sonin）；
  - 场域理论（Bourdieu；Fligstein–McAdam；DiMaggio–Powell）；
  - 排名的反身性（Espeland–Sauder）。
- **AI 侧：**
  - 结构性风险（Critch；Kulveit）；
  - 评审偏差与相关误差；
  - 奖励模型集成（Eisenstein）；
  - 监督技术。
- **新意：**
  1. 在同一个递归选择模型里，同时推出控制被选择、纠错被淘汰；
  2. 把二阶选择接入跨域捕获阈值，得到独立监督的最低门槛 d*，以及它对可占有性、集中、范围和 AI 辅助的依赖；
  3. 被捕获评估的检测条件，包括“中等伤害最容易被藏住”；
  4. 落到 AI 评估的设计规则。

所有新文献在写入前逐条核验。

## 五点五 标题与摘要草稿

标题候选：
- A：Selecting the Selectors: Control, Correction and Recursive Selection in AI Evaluation（推荐）
- B：Selecting the Selectors: Why Recursive Selection Rewards Control over AI Evaluation and Starves Its Correction
- C：保留 v2 标题

摘要草稿（约 180 词）：

> When the winners of AI development help build the benchmarks, judges, reward models and standards that evaluate the next round, selection becomes recursive. We model this recursion and ask what it selects for. Investment in shaping evaluation is selected when its returns can be kept, persist longer than correction erases them, and accrue to carriers already large across domains; in fragmented fields it is not. Investment in correction faces the opposite incentives: incumbents are selected against it and dispersed challengers free-ride on it, so it is supplied only by concentrated rivals or by institutions outside the competition. Accounting for the control capacity that selection will cultivate, we derive the minimum rate of independent correction that keeps evaluation uncaptured. It rises with appropriability, with the square of the dominant carrier's size, and as capable assistants make control cheaper. Captured evaluation then delays the detection of harm, and harms that settle just below the alarm can be hidden by small biases; diverse judge panels reduce error but not shared bias. The results yield design rules for AI evaluation.

## 六 风险和预先应对

- **“仍是标准工具。”** 主动承认，把新意限定在连接结果和定量含义上。d* 和“中等伤害最易隐藏”在先例里都没有。
- **“没有实证。”** 这是一篇理论论文，Ren 已决定不做实验。局限处写明；第 9 节给出每个量的测量路径和现有证据，不硬凑数据。
- **“新命题的错误。”** 结果二和结果三是新推导的。每条写出完整证明，并做数值核对代数（只核对公式，不是实验）。截止前若时间允许，再请 Ren 决定是否做一轮独立复审。

## 七 时间表（截止 10 月 5 日 AOE，即曼谷 10 月 6 日约 19:00）

- 10 月 3 日：Ren 确认思路后，写模型和结果一至三的正文与证明。
- 10 月 4 日：结果四、五，AI 与治理，引言和摘要，相关工作，图，编译。
- 10 月 5 日：按全部评审意见逐项自查；视情况复审；定稿；准备 Overleaf 版。

## 八 需要 Ren 决定

1. 是否同意这条主线：控制 vs 纠错，以 d* 为整合结果。
2. 标题：A、B 或 C。
3. 正文是否保留少量由模型生成的说明性图（不是实验）。建议保留一张 d* 图；六域数值放附录。
4. `experiment/` 文件夹：实验在你叫停前已经跑完，结果不会用进论文。建议从论文目录删除，git 历史中保留记录。
5. 摘要是否出现 meta-attractor 一词。建议在第 3 节定义，摘要不放。
