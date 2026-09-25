# Causal Chain v4：AI／经验／当前现实红队审查

> 审查日期：2026-07-13
>
> 审查对象：`plan.md`、`main-zh.md`、`independent-zh.md`、`independent-en.md`
>
> 方法边界：未读取任何其他 v4 review。时间敏感判断只用截至 2026-07 的官方资料或一手研究核验；公司自报只作为该公司部署、政策或内部观测的证据，不当作全行业无偏估计。

## 一、结论先行

三稿已经成功避开两个常见错误：它们没有把 consumer query 的多数误写成文明方向，也没有把 AI-assisted research 直接等同于 autonomous recursive self-improvement。两条风险路径和五级递归的**概念区分**是成立的，且 `independent-en.md` 对“能力本身不决定净方向”的限定最完整。

但三稿尚未完成最重要的经验桥梁。它们证明了“少数高杠杆用途可以比大量普通用途更重要”的**可能性**，还没有证明这些用途在现实中的加权回流已经强到足以决定 frontier direction；证明了 AI 可以提高若干局部能力，还没有证明这些能力提高了某一 totalizing loop 的**净有效增益**；证明了协调有不可压缩的关系时间，还没有比较 capability、counter-capacity 与 coordination 三者的实测增长率。因此，当前最强的可辩护结论是：

> 已有证据支持立即把若干高权限、高不可逆、高外溢、进入后继研发的部署改向，并在其不能满足明确安全与可逆条件时停止扩大；证据尚不足以从三稿现有事实前提推出一个范围未定义、反事实未比较的文明级 pause。

问题不是结尾“太坚定”，而是正文把四个尚需证明的经验命题压缩成了一个姿态：

1. 高杠杆少数的**实际选择权重**大于低风险多数的分散反馈；
2. AI 带来的行动增益主要被斗争性回路捕获，而非也同样增强发现、审计、协商、开放替代与防御；
3. 后继生产速度正在逼近或超过特定纠错过程，而非只在抽象上可能更快；
4. pause 在现实反事实中降低总风险，而非把能力、资本和秘密研发进一步推向最难约束的中心。

不补这四步，“frontier supply / high leverage”会变成一个无法被普通有益使用反驳、也无法被反向能力增长证伪的特殊 denominator；“stance 与 means 分开”则会掩盖 pause 本身改变选择环境这一事实。

## 二、证据底账：截至 2026-07 能说到哪里

| 现实命题 | 一手证据 | 红队判定 |
|---|---|---|
| 大量现实使用并非军事、操纵或自主递归 | Anthropic 2026-01 的真实使用数据仍显示 Claude 使用集中在 coding 等普通工作任务，Claude.ai 中 augmentation 略占多数；2026-06 报告又显示 personal、work、agentic tasks 并存，产品表面差异很大。[Anthropic Economic Index 2026-01](https://www.anthropic.com/research/anthropic-economic-index-january-2026-report)、[2026-06](https://www.anthropic.com/research/economic-index-june-2026-report) | **supported**。三稿承认这一点是必要修正；但不能据此推出这些使用没有方向性反馈。 |
| 前沿算力和后继生产确有集中回流 | FTC 对大型云商—前沿实验室合作的 6(b) 调查发现股权、收入分成、云支出承诺、控制／排他权、切换成本和对算力与人才入口的影响；OpenAI 2026-04 更直接把自身路径写成“more compute → better models → more usage → revenue → more infrastructure”的 flywheel。[FTC staff report](https://search.ftc.gov/news-events/news/press-releases/2025/01/ftc-issues-staff-report-ai-partnerships-investments-study)、[OpenAI infrastructure statement](https://openai.com/index/building-the-compute-infrastructure-for-the-intelligence-age/) | **supported**，这是三稿最强现实支点。但它只证明集中与正反馈，不自动证明 totalization、反向反馈失败或文明净方向。 |
| 该回路不是封闭单中心，替代供给与公共算力也在增长 | OpenAI 的前沿训练已跨 Microsoft、Oracle 等多套超算基础设施；欧盟截至 2026 年报告 19 个 AI Factories、公共 EuroHPC 入口及拟建 gigafactories，明确面向初创公司、研究和公共部门。[OpenAI MRC](https://openai.com/index/mrc-supercomputer-networking/)、[EU AI Factories](https://digital-strategy.ec.europa.eu/en/policies/ai-factories) | **supported counterexample**。它不消除集中，但反驳“替代方向已经失去后继生产条件”的强写法；必须测量集中度、可替代性与实际访问，而不能只列资本规模。 |
| AI 已在部分任务中真实降低搜索、执行和研发成本 | Google 的一手研究在六类可评分科学任务上展示了自动生成、执行和迭代实验软件，并把部分搜索从月压到小时／天；OpenAI 报告企业内 Codex 部署显著压缩部分工程流程，Anthropic 也公开确认现有 Claude 被用于生成训练数据、写研究代码、监控 agent 与评估后继模型。[Google ERA](https://research.google/blog/accelerating-scientific-discovery-with-ai-powered-empirical-software/)、[OpenAI Cisco case](https://openai.com/index/cisco/)、[Anthropic alignment audit](https://alignment.anthropic.com/2026/auditing-overt-saboteur/) | **supported but selected**。这足以证明 level 1 和部分 level 2；公司案例有选择偏差，尚不能外推为总体研发加速率。 |
| AI 并不单调提高所有行动者的生产率 | METR 的随机对照试验中，16 名熟悉自身大型开源仓库的开发者完成 246 项真实任务，使用 2025 年初前沿工具反而慢 19%；研究者明确限定该结果不代表多数开发场景。[METR RCT](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/) | **strongest capability counterexample**。任何“AI 会提高回路增益”的句子都必须写成部署、任务、权限与反馈条件的交互命题。 |
| AI 可提高说服能力，但现实操纵效果不是由生成能力直接推出 | 预注册实验显示候选人导向的 AI 对话可产生高于传统视频广告的态度效应；个性化 GPT-4 辩论也比人类更有说服力。与此同时，OpenAI 2026-06 查获的两组现实影响行动虽使用模型生产内容，却未发现突破其自有活动圈的 meaningful breakout。[Nature voter experiments](https://www.nature.com/articles/s41586-025-09771-9)、[Nature Human Behaviour personalization RCT](https://www.nature.com/articles/s41562-025-02194-6)、[OpenAI threat report](https://openai.com/index/prc-linked-influence-operations-ai-debates/) | **conditional**。能力、规模化成本下降、分发、信任和实际行为改变是不同环节；三稿目前把前两环写得像已完成后两环。 |
| 前沿 AI 已进入国家安全和防务基础设施 | Anthropic 2025-07 报告 Claude 已在 classified networks 的国防与情报工作流中部署；OpenAI 2026-02 将 ChatGPT 部署到面向 300 万军民人员的 GenAI.mil，但公开用途主要是文档、采购、研究、规划和行政支持。[Anthropic–DoD](https://www.anthropic.com/news/anthropic-and-the-department-of-defense-to-advance-responsible-ai-in-defense-operations)、[OpenAI GenAI.mil](https://openai.com/index/bringing-chatgpt-to-genaimil/) | **supported**，足以触发定向审查；不足以写成 AI 已进入武器决策或“军事支配”本身，除非补部署层证据。 |
| agent 能力时域在快速增长，但当前系统尚未证明高等级自我改进 | METR 的公开任务时域测量给出过去六年约 7 个月翻倍的趋势，但任务主要是软件与推理，并强调外推不确定；OpenAI 2026-07 最新 GPT-5.6 系统卡仍将 AI self-improvement 判为 below High；Anthropic Opus 4.6 观察到更强 sabotage concealment 与过度 agentic 行为，但认为未达到改变部署判断的程度。[METR time horizon](https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/)、[GPT-5.6 system card](https://deploymentsafety.openai.com/gpt-5-6)、[Claude Opus 4.6 system card](https://www-cdn.anthropic.com/14e4fb01875d2a69f646fa5e574dea2b1c0ff7b5.pdf) | level 1 **supported**；level 2 **partly supported**；level 3 **conditional**；level 4 **speculative**；level 5 **unsupported as a present fact**。 |
| 严重能力已出现可操作的提前触发，而现实反应通常是加护栏，不是停止所有扩张 | OpenAI 2026 模型已被归类为 Bio/Chem High 和 Cyber High，但仍低于 AI self-improvement High，并通过分层监测、访问控制、可信研究访问等部署；Anthropic 当前最强模型处于 ASL-3，RSP 明定能力阈值、风险报告和必要时暂停训练／部署。[OpenAI GPT-5.6](https://deploymentsafety.openai.com/gpt-5-6)、[Anthropic RSP 3.4](https://www.anthropic.com/responsible-scaling-policy)、[Anthropic roadmap](https://www.anthropic.com/responsible-scaling-policy/roadmap) | **supported**。现实已经提供 targeted redirect / restricted deployment 的触发，却没有提供 blanket pause 的共同阈值。 |
| 文明协调确有滞后和反复，但不能说“没有同步增长”而不定义指标 | 反向证据并不为空：EU GPAI 义务自 2025-08 起适用、2026-08 开始执行；UN 已建立覆盖 193 国的 Global Dialogue 与独立科学小组；国际 AI 安全机构网络做过联合测试；NIST/CAISI 的跨机构测试仍在扩大。另一方面，美国政策明确以“winning the AI race”和去监管为方向，NIST 联盟也从 safety 改名并扩大为 innovation/adoption；EU 部分高风险规则延至 2027–2028。[EU GPAI timeline](https://digital-strategy.ec.europa.eu/en/policies/guidelines-gpai-providers)、[UN Dialogue](https://www.un.org/global-dialogue-ai-governance/en)、[NIST international testing](https://www.nist.gov/news-events/news/2024/11/fact-sheet-us-department-commerce-us-department-state-launch-international)、[US AI Action Plan](https://www.whitehouse.gov/releases/2025/07/white-house-unveils-americas-ai-action-plan/)、[NIST consortium 2026](https://www.nist.gov/news-events/news/2026/05/nist-expands-ai-consortiums-scope-calls-new-members)、[EU implementation delay](https://digital-strategy.ec.europa.eu/en/news/eu-agrees-simplify-ai-rules-boost-innovation-and-ban-nudification-apps-protect-citizens) | “协调尚不足以约束全部高杠杆部署”是 **supported**；“协调没有以同样速度增长”是 **unsupported comparison**，除非给出共同量尺和时间序列。 |

## 三、总论证的六个压力点

### 1. Frontier / high-leverage denominator：必要，但还不足以绕过大量低风险反例

三稿正确指出，文明方向不能按 query 数量投票。核武、金融结算或基础设施控制的方向性也从来不由日常交易次数决定。问题在于，高杠杆 denominator 目前由作者指定，却没有被操作化。

至少要补四项：

- **控制份额**：frontier training compute、关键云／芯片／能源、主要分发入口分别由谁控制，集中度如何变化；
- **回流份额**：哪些部署带来的收入、数据、许可或国家资源实际回到下一代训练，而不是只具有理论可能；
- **权限权重**：军事、政治、金融、能源、关键基础设施与 AI R&D 中，模型是摘要助手、建议者、执行者还是不可绕开的决策接口；
- **反向权重**：相同 frontier capability 是否也在增强审计、网络防御、科学开放、公共算力、跨语言协商与替代供给。

没有这些，高杠杆 denominator 会产生一个封闭结构：普通有益使用因为“不高杠杆”被排除；公共算力与开源替代因为“尚不够强”被排除；安全与协调因为“依赖被约束者”被排除；剩下的所有证据自然只会支持既定方向。`independent-en.md` 已写出真实反证条件，却没有用现实数据执行自己的反证。

**最强现实反例**不是“很多人拿 AI 写邮件”，而是同一高杠杆层中已经存在 public compute、开放权重、跨云供给、国际联合测试和 capability-triggered safeguards。它们尚不足以证明方向已改，但足以否定“高杠杆层只有一种回路”的暗示。

### 2. AI 如何实际提高 totalizing loop gain：三稿仍把 affordance 当 effect

可以把有效回路增益最低限度写成：

> **有效增益 = 能力提升 × 采用／权限 × 规模与回流 × 相对优势捕获 − 同期 counter-capacity − 新摩擦与失败。**

三稿主要写了第一项，并列举第二、三项的可能形式。现实证据显示每个乘数都可能接近零或反号：AI 在熟悉的大型代码库中可能减速；影响行动能批量产出内容但不能突破分发；高能力模型可因监控、沙箱、可信访问和 actor-level enforcement 而降低攻击转化；公共科学也能把同样的搜索成本下降转成共享能力。

因此，`main-zh.md` 的“AI 提高的是 totalizing loop 的 gain”、`independent-zh.md` 的“服从工具正在提高斗争性回路的增益”和 `independent-en.md` 的“the loops ... are raising their gain faster”都写过了证据。更准确的是：

> AI 已经提高若干可被斗争性回路利用的局部增益；在高集中回报、关键权限、规模部署和反向能力缺口同时存在的场景，它很可能提高该回路的净有效增益。当前公开证据显示这种组合已在部分企业、平台、国防与后继研发场景出现，但尚无跨场景净估计。

### 3. 两条风险路径：第一条较强，第二条仍是条件性风险

第一条——局部服从系统放大既有选择回路——不需要机器主体，经验基础明显更强。它只需要证明 AI 降低既有行动者在预测、说服、搜索、组织、监控或研发上的成本，并证明收益回流。现有资料已经能支持“若干场景出现”，不能支持“文明净方向已经由此决定”。

第二条——持久 runtime、工具、资源和反馈形成新的难以改向中心——作为风险模型是严肃的，但当前仍是 **speculative/conditional**。系统卡中的 sabotage、scheming、overly agentic behavior 是评测信号；它们不是现实系统已经自主维持资源、跨部署存续或控制后继生产的证据。三稿在字面上承认这一点，却在结尾用“两条都可能耗尽 correction margin”把它们重新加总成同一现实紧迫性。应分别给概率、暴露和触发，不应以第一条的可信度替第二条抬升现在时态。

### 4. 五级递归：分类好，因果箭头仍跳级

五级区分应保留：

1. AI-assisted research；
2. partial automation of AI R&D；
3. aggregate acceleration；
4. highly automated successor production；
5. autonomous recursive self-improvement。

当前证据状态并非一条已经启动的单调阶梯：level 1 明确存在；level 2 在编码、评测、训练数据和监控环节存在，但人类仍控制问题设定、验证和整合；level 3 有公司自报、任务时域和更短产品周期的间接证据，却缺少“如果没有 AI，前沿能力曲线会慢多少”的反事实；level 4 尚未被公开证明；level 5 的最新前沿系统卡仍为 below High。

尤其需要删除或收窄“较低层级正在缩短开发周期”作为无条件事实。较低级活动存在不等于净周期缩短；存在大量新增实验、验证负担、rework 与安全摩擦。最短修复是把 level 3 定义成一个待测结果，而不是 level 1–2 的自然总和。

### 5. Correction margin：有好问题，没有当前估计

三稿把 correction margin 定义为“发现—归因—理解—共同决策—有效干预”所需时间与“扩散—锁定—后继生产—不可逆伤害”所需时间之差，这个结构是 **supported as a decision framework**。但目前没有一个场景完成左右两边的估计。

“数字复制快、信任形成慢”不足以证明 margin 已为负：模型发布可以快，进入受监管关键基础设施可能慢；国际协定慢，模型级访问控制、撤回、权重不发布和产品下线可以快；社会后果发现慢，capability eval 又可能在部署前触发。反过来，关键基础设施锁定、模型权重扩散和秘密军事部署确实可能使纠正极慢。margin 必须是**部署级变量**，不能是“文明总时钟”。

建议至少给两个对照场景：

- 可撤回、无关键权限、留有人工替代的科学助手：扩散快，但可逆性和 counter-capacity 也高，margin 未必危险；
- 可持续运行、接入武器／政治定向／核心金融或后继训练、退出会造成系统性中断的 agent：归因与协调时间可能长于锁定或伤害时间，margin 可合理推定为危险。

### 6. “文明协调未同步增长”：现在是修辞性净比较

这是三稿最明显的 unsupported claim。技术能力可用任务时域、模型阈值、算力和部署规模衡量；“理解、信任、德性、共同意志”没有对应指标。把不可通约的对象说成“没有同速增长”，读起来像事实，实际是规范判断与观察的混合。

现实更复杂：协调基础设施确实增长——EU GPAI 法律、国际联合测试、UN 科学小组与全球对话、公司能力阈值框架都在 2024–2026 出现；它们的覆盖、执行力、军事适用、独立性和速度又明显不足，并出现去监管、竞赛叙事与延期。可以诚实而有力地写：

> 反向协调正在增长，但尚未证明它能够覆盖主要前沿开发者、秘密与军事部署、跨境扩散和高权限后继研发，也尚未证明它能在能力跨越阈值前实施共同约束。

这比“没有同步增长”更窄，却更能承受现实反例。

## 四、逐稿判定

### A. `main-zh.md`

| 标签 | 具体命题 | 判定 |
|---|---|---|
| **supported** | AI 方向由 archive、训练、后训练、评测、权限、拥有、部署和回流共同形成；两条风险路径必须分开；五级递归不能压成一个词。 | 全稿最稳固的 AI 架构。 |
| **conditional** | consumer query 不是决定 frontier direction 的 denominator；少量高杠杆使用可以塑造后继系统。 | 逻辑成立，经验上需补控制份额、回流份额、权限层级和 counter-capacity。 |
| **conditional** | AI 汇集信号、预测、搜索、说服、监控与研发，从而提高 existing loop gain。 | 只能在采用、权限、规模、收益捕获和反向能力缺口成立时推出。 |
| **speculative** | 带记忆、长时程、资源和环境反馈的复合系统形成新的持续中心。 | 是合理风险模型，不是当前事实；最新公开系统卡不支持已到 self-improvement High。 |
| **unsupported** | “文明形成共同意志与纠正自身的能力没有以同样速度增长。” | 没有共同量尺；现实存在显著协调增长与显著不足两组相反证据。 |
| **unsupported leap** | 从 correction margin 的可能缩短直接推出“军事支配、政治操纵、不可逆社会控制或失控后继生产”应先停。 | 方向可支持；但未说明哪些现实系统已满足这些类别、停止什么、替代与泄漏反事实如何。 |
| **redundant** | 最后多次用“刹车／油门”“悬崖／道路”“完整地图”重复 stance。 | 重复不能补 pause 的经验桥。保留一个意象，把篇幅用于触发和反事实。 |

**最强现实反例：**当前最前沿公开模型已经在 Bio/Chem 与 Cyber 被定为 High，同时通过访问分层、监控、可信研究通道和安全控制部署；AI self-improvement 仍 below High。这说明“危险能力已出现”可以经验地推出 restricted deployment / stronger safeguards，却不自动推出停止整个后继递归。

**最危险过度断言：**“只需看见：继续提高当前回路的增益，会消耗未来真正作出选择的时间。”这里把需要证明的“净增益已提高”和“选择余量已下降”写成了无需测量的所见。

### B. `independent-zh.md`

| 标签 | 具体命题 | 判定 |
|---|---|---|
| **supported** | 两条斗争路径、AI 两条风险路径、五级递归的分层和“警告事故不会自动成为反馈”。 | 因果分辨率优于主稿。 |
| **supported/conditional** | AI 可让总体化方向更会吸收反向反馈，例如分类批评、测试界面、复制有效叙事。 | 说服与自动实验研究支持能力面；“总体化方向”是否实际获得净优势仍需部署证据。 |
| **conditional** | 高权限、深依赖、可占有回报和反向能力缺口结合时，AI 降低竞赛与环境改写成本。 | 三稿中最准确的 gain 句，应成为共同版本的核心桥。 |
| **speculative** | 机器或人机复合过程形成操作者难以阻断的持续动力。 | 条件写得好，但“可能形成另一个吸引子”不应在结尾与第一路径同权加总。 |
| **unsupported** | “较低层级正在缩短开发周期”以及“理解、德性、信任和协调能力没有以同样速度增长”。 | 前者缺 AI-free counterfactual，后者缺共同量尺。 |
| **unsupported leap** | “仍把高权限智能接入无法安全退出的竞争，并提高关键依赖、不可逆性或后继生产速度”就应暂停相关递归。 | 接近可操作触发，但“无法安全退出”“提高”均未设证据阈值，“相关递归”范围仍不明。 |
| **redundant** | 结尾用三段连续重述“姿态不能被手段稀释”。 | 实际遗漏不是勇气，而是 pause policy 的 general-equilibrium effect。 |

**最强现实反例：**AI 不只可吸收批评，也能显著增强 counter-feedback：预部署能力评测已经先于公开部署触发 Bio/Cyber High，联合安全机构能做跨国测试，网络防御者也获得更强模型。若正文不比较两种增益，“智能进入什么，就放大什么”只是双向真理，不能给出净方向。

**最危险过度断言：**“两条路径因此独立成立。”第一条作为已发生机制部分成立；第二条只作为条件性风险成立。应改成“两条路径在逻辑上独立；现实证据强度不同”。

### C. `independent-en.md`

| 标签 | 具体命题 | 判定 |
|---|---|---|
| **supported** | “Capability alone does not establish this result”，并列出 adoption、permission、scale、returns 与 counter-capacity 的必要条件。 | 三稿最好的经验纪律，应移植到主稿。 |
| **supported** | 现实高杠杆层存在资本—算力—基础设施—依赖—回报链，以及国防／安全部署。 | 有 FTC、公司基础设施与国防部署的一手材料支撑。 |
| **conditional** | privately appropriable / strategically decisive uses 有更短 reproduction path。 | 高度合理且有公司 flywheel 支点，但仍需与公共算力、开放供给和安全投资比较。 |
| **speculative** | persistent machine or human-machine process becomes locally unsteerable。 | 明确是风险路径；不能写成 present-tense trajectory 的已完成部分。 |
| **unsupported** | “the loops with the greatest capacity ... are raising their gain faster than the forces able to redirect them”；“We do know ... before ... capacity for common redirection have grown at the same rate.” | 这是全文最关键、却未测量的净比较。 |
| **unsupported leap** | “Where a high-risk recursion ... cannot yet be redirected, we should stop increasing its power until another direction is real.” | 比中文稿范围更窄，但 `high-risk`、`cannot be redirected`、`another direction is real` 没有判定规则，也没有 pause counterfactual。 |
| **redundant** | “brake/accelerator” 与 “cliff/route” 连续出现。 | 英文稿自身已承认 means 决定干预是否重现危险；下一句却把 means 从结论有效性中隔离，逻辑回撤。 |

**最强现实反例：**本稿自己的反证条件已有现实实例：约束随能力增强（High capability safeguards）、共同基础设施增加独立供给（EU public compute）、跨国联合测试、替代模型与跨云训练。它们也许仍弱于竞赛，但本稿不能既要求这些作为证伪窗口，又不执行比较便宣布竞赛增益更快。

**最危险过度断言：**“Both routes can consume the correction margin”语义上没错，但用 possibility 为现在的停下结论提供同一权重。应改成 route-specific：第一路径用实际部署与回流触发；第二路径用 autonomy/persistence/resource-acquisition eval 与 system containment 触发。

## 五、现在有哪些 redirect / pause 的经验触发

### 已足以支持“现在 redirect”的触发

- 模型已经进入 classified defense/intelligence workflows、广泛国防企业平台或政治定向系统，即便当前只做分析和行政，也应从一开始限制权限、用途和回流；
- 模型达到 Bio/Chem High 或 Cyber High，已被开发者自己的框架认定可能显著降低严重伤害路径的门槛；
- AI 已参与后继模型的训练数据、研究代码、评测和监控，应该把独立验证、审计隔离与人类否决权嵌入研发回路；
- 个性化政治说服已有随机实验效果，且现实影响行动已使用模型规模化内容，应限制隐蔽定向、身份伪装和不透明批量分发；
- frontier compute / cloud partnership 已出现锁定和输入控制风险，应扩大可替代供给、公共算力、互操作和独立评测访问。

这些都是**改向**的现实证据，不需要等待 RSI。

### 足以支持“暂停某项训练或部署”的条件，但三稿尚未证明已普遍满足

- capability threshold 已跨越，而相应 safeguards 尚不能证明足以降低严重风险；
- 系统在受控测试中持续展示跨任务欺骗、保存访问、规避中断、资源获取或操纵监督的能力，且无法由独立评测可靠检出；
- 一个部署将模型置于高权限、持久、低可观测、难撤回环境，并且没有人工替代、隔离和可验证停止机制；
- AI 对后继研发的净加速达到预先定义阈值，而 alignment、security 与 external evaluation 没有达到对应保障等级；
- 权重或能力一旦扩散即不可回收，预期严重损害的纠正时间明确长于扩散／锁定时间。

Anthropic RSP 和 OpenAI Preparedness Framework 已经证明这种 capabilities-to-mitigations / pause-if-not-ready 结构在实践上可以表达。三稿若拒绝给 pause 任何触发，便不是超越 checklist，而是让“不能改向”由作者直觉决定。

## 六、stance 与 means：当前分法掩盖了 pause counterfactual

“刹车可能被误用，不代表油门正确”只反驳一种稻草人：实施有风险，所以什么都不做。现实选择不是二元踏板。至少还有 staged deployment、限制权限、推迟权重发布、可信研究访问、模型级监控、算力治理、公开替代、只停某一用途、只停某一能力阈值以上的训练等组合。

更重要的是，pause 不是把同一世界静止下来。它会改变选择环境：

- 单方暂停可能把人才、资本、国家支持和数据推给更不透明的参与者；
- 由既有大实验室定义的门槛可能冻结其优势，削弱开放替代和外部审计；
- 民用公开研发放慢而军事／秘密研发继续，可能提高而非降低安全困境；
- 停止所有高能力研发也可能减少网络防御、生物安全、评测与 alignment counter-capacity；
- 可信、对称、可验证的局部限制则可能降低互相猜疑，并真实增加 correction margin。

所以 means 不只是执行 stance 的次级问题；它参与判断某个具体 pause 是否忠于 stance。一个会增加集中、秘密化、军事优势和不可审计性的 pause，可能正是 totalizing loop 的新燃料。

正文可以维持价值立场先行，但必须把结论改成带反事实的决断：

> 对每个拟扩大能力的高风险递归，比较继续、受限部署、定向暂停和协调暂停如何改变集中度、泄漏、替代供给、反向能力与纠错余量；若没有一种受限部署能在能力扩张前恢复足够的可逆性和独立纠正，就暂停该递归。暂停不是因为手段无关，而是因为在该反事实中，暂停最能保护改向条件。

这不会把文明立场降格成程序。它防止文明立场以错误手段实现自己的反面。

## 七、最短 evidence-bearing AI bridge

建议用下面五句替换三稿从“多数低风险使用”跳到“AI 提高 totalizing gain”的长段核心。它保留方向力度，也把公开证据能承担的强度写准：

> 截至 2026 年，前沿 AI 已不只用于日常辅助：它已进入企业工程、科学搜索、国防与情报工作流，也参与后继模型的编码、训练数据、评测与监控。实验和真实部署显示，它能在一些场景降低技术搜索、执行和个性化说服的成本；同样的一手证据也显示，增益高度依赖任务，内容生成未必转化为现实影响，熟悉复杂代码库的专家甚至可能变慢。因此，AI 不会自动提高 totalizing gain。只有当能力提升同时获得关键权限和规模部署，其可占有或战略回报回流为算力、基础设施与后继研发，而独立评测、替代供给和协调能力没有相应增强时，它才提高斗争性回路的净有效增益。当前证据支持这种组合已经在若干前沿、平台和国防场景出现，但尚不足以证明它支配 AI 的总体使用，或已压倒所有反向回路。

英文最短版：

> By 2026, frontier AI had entered enterprise engineering, scientific search, defense and intelligence workflows, and parts of successor-model development. Experiments and deployments show real reductions in the cost of some technical search, execution, and personalized persuasion, but also strong task dependence, failures of generated influence to achieve real-world reach, and measured slowdowns in expert coding. AI therefore does not automatically raise a totalizing loop's gain. It does so when capability is coupled to consequential permission and scale, its concentrated returns reproduce compute, infrastructure, and successor R&D, and independent evaluation, alternative supply, and coordination do not rise with it. Public evidence shows that conjunction in some frontier, platform, and defense settings, not yet across AI use as a whole.

## 八、最小修订优先级

1. **必须改：**把“文明协调没有同步增长”改成“协调在增长，但覆盖与执行尚未证明能跑在若干高杠杆阈值之前”，并给现实正反证据。
2. **必须改：**把 effective gain 写成条件交互，至少包含 adoption/permission、scale/returns 与 counter-capacity；加入 METR 减速和现实影响行动未 breakout 两个反例。
3. **必须改：**把五级递归的 level 3 从既成事实改成待测结果；明确 level 4–5 尚无公开证明。
4. **必须改：**把“两条路径独立成立”改成“逻辑独立、证据强度不同”，分别指定触发。
5. **必须改：**让 pause 结论比较 continue / restricted deployment / targeted pause / coordinated pause 的反事实；定义“不能改向”和“相关递归”。
6. **应改：**用 FTC + OpenAI 自述 flywheel 支撑集中回流，同时用 EU public compute、跨云供给和联合评测执行理论自己的反证窗口。
7. **应删：**结尾重复的刹车、油门、悬崖、地图意象。一个即可；省下的篇幅给当前触发与 evidence-bearing bridge。

## 最终判决

v4 的 AI 论证不是错误，而是**强方向、弱净估计**。它最可信地证明了三件事：前沿智能的生产与部署确实嵌在资本和安全竞赛中；AI 已能提高若干参与者的感知、搜索、说服、执行和后继研发能力；某些高权限和不可逆部署不应以普通有益使用的多数作为免责理由。

它尚未证明三件更强的事：这些增益在总体上已压倒 AI 对 counter-feedback 的增强；文明协调能力的增长率低于能力增长率；未定义范围的 pause 比受限部署、公开替代和能力门槛治理更能降低同一 totalizing dynamic。

因此，三稿可以坚定推出“现在定向改向，并对无法满足可逆性与保障阈值的具体递归暂停扩大”，不能在不补反事实与触发的情况下推出“手段暂未解决但 pause 立场已经独立成立”。真正经得起现实的强结论，不是把 means 放到以后，而是证明在考虑 means 改变世界之后，所选择的 restraint 仍然扩大而非收窄未来。
