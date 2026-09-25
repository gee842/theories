# Causal-chain v3：AI、经验与当前现实红队审查

## 审查范围与方法

本审查独立阅读并比较：

- `v3/main-zh.md`
- `v3/independent-zh.md`
- `v3/independent-en.md`
- `v3/plan.md`

为保持独立性，没有读取任何其他 v3 review。本文只审查 AI 与当前现实承重部分：当前 AI 选择生态；商业与国家竞争如何、以及是否已经转化为部署结果；locally directed amplification；loss of local steerability；AI-assisted R&D 到更强递归层级；气候与 AI arms race 的类比；纠错窗口；证明责任与 pause scope。

证据截至 2026 年 7 月。技术判断只使用一手研究、开发者系统卡/框架、政府技术评测或官方国际评估；投资、政策与部署判断使用官方监管材料、政府文件和有明确方法的数据报告。正文中的宏大机制仍然可以是理论假说，但不能伪装成当前经验结论。

### 状态词

- **Supported**：已经由当前观测、真实使用数据、正式制度或可复现评测直接支持。
- **Conditional**：机制成立，但从当前证据到文本结论还需要明确列出的条件。
- **Speculative**：重要且可理解，但目前只能作为情景或待检验假说。
- **Unsupported**：当前措辞超过证据，或省略了必需的中间前提。
- **Redundant**：重复前文而没有增加新的经验或因果工作。

## 总判决

v3 比 v2 明显更严谨。三稿都正确做到五件事：不把预训练文本当作统一文明意志；把 AI 放进训练、后训练、脚手架、权限、运营者、所有权和部署构成的生态；把局部定向放大与局部可转向性丧失分成两条风险路径；区分 AI 辅助研发与自主递归自我改进；把暂停建立在显式价值前提与不对称风险原则上，而不是伪装成纯技术推论。

但三稿仍没有把最关键的经验桥完全建成。共同的过度延伸有四处：

1. **从资源集中与竞赛话语跳到实际用途选择。** 产业确实生产了绝大多数前沿模型，私人投资和算力高度集中，美国官方政策也明确使用“赢得 AI 竞赛”的语言；但真实使用数据同时显示，消费者主要把 AI 用于日常建议、信息和写作，企业 agent 在多数职能中的部署仍是个位数，开放模型差距在缩小，科学、医疗和公共用途也在增长。现有证据支持“商业/战略回报强烈塑造前沿供给”，还不支持“集中、控制性用途已在总体部署结果中占支配地位”。
2. **从一个参与者更有能力跳到文明整体更不可转向。** AI 已能降低某些预测、说服、编码、监控、网络行动和组织实验的成本；但 capability → reliable execution → consequential adoption → cross-domain return → weakened alternatives → collective loss of steerability 是六个不同环节。三稿常把第一、二环写得像已经完成最后两环。
3. **从 AI 进入 AI 研发跳到总体研发循环和纠错窗口缩短。** AI 辅助编码、评测、研究和实验已经发生；受控任务时域与真实使用自治程度也在增长。可是 aggregate frontier R&D acceleration 的幅度仍缺可靠测量；更没有文明级统一时钟证明后继生产已经快于发现、协调和干预。
4. **证明责任触发条件仍过宽。** “可能灾难且不可逆”不能单独把所有举证责任交给开发者，否则任何低概率、难证伪叙事都可触发暂停。必须先独立建立可识别的危险类：高后果权限或关键基础设施接入、难以回滚的广泛依赖、显著自主性、对后继生产有实质影响、以及现实可行的严重失效路径。证明责任随这些暴露指标上升，而不是随“前沿”这一标签自动无限上升。

因此，最强可守结论不是：

> 当前 AI 已经让斗争性 meta-attractor 更聪明、后继循环更快，并正在关闭纠错窗口。

而是：

> 前沿 AI 的供给、基础设施与主要投资明显由产业和国家竞争塑造；AI 已经提高若干操作者的行动与研发能力，并正被给予更长时程和更多工具权限。当前证据尚不能证明这些变化已经聚合为文明层面的不可转向，也不能证明总体 AI 研发已进入强递归；但在高权限、关键依赖、难回滚或实质参与后继生产的部署上，错误可能先于社会纠正完成扩散。此类部署因此需要独立、与暴露成比例的安全和可纠正性证明；证明不足时应暂停该角色或权限，而不是由此推出所有前沿研究与所有通用模型开发必须暂停。

这条结论足以承载“改向；不能满足条件的部分暂停”，不需要把尚未观测的聚合结果写成现在时事实。

## 证据底账：截至 2026-07，现实究竟支持什么

### 1. 当前 AI 选择生态

**Supported**

- 产业控制前沿模型生产的主导份额。Stanford 2026 AI Index 报告称，产业在 2025 年生产了超过 90% 的 notable frontier models；美国 2025 年私人 AI 投资达到 2859 亿美元。全球企业 AI 投资在 2025 年翻倍以上，私人投资约占总量 60%。这些数据足以证明前沿供给不是中性的公共知识过程，而高度依赖企业资本、算力与商业回报。[Stanford AI Index 2026](https://hai.stanford.edu/ai-index/2026-ai-index-report)
- 资源集中有具体机制。FTC 对 Microsoft–OpenAI、Amazon–Anthropic、Google–Anthropic 合作的 6(b) 调查记录了超过 200 亿美元累计投资，以及算力、人才、敏感信息、排他安排和 switching costs 可能带来的集中优势。[FTC staff report background](https://www.ftc.gov/policy/advocacy-research/tech-at-ftc/2025/01/behind-ftcs-6b-report-large-ai-partnerships-investments)
- 国家竞争不是本文虚构的修辞。美国政府 2025 年正式把国家战略称为 “Winning the AI Race”，并把加速创新、基础设施和出口全栈 AI 作为政策支柱。[White House AI Action Plan](https://www.whitehouse.gov/releases/2025/07/white-house-unveils-americas-ai-action-plan/)
- 模型行为和部署后果确实由模型、用户、产品与权限共同形成。Anthropic 对数百万真实 agent interactions 的研究发现，自治程度随使用经验和产品设置改变；这直接支持“自治不是权重的固定属性，而是部署关系的属性”。[Anthropic, Measuring AI agent autonomy in practice](https://www.anthropic.com/research/measuring-agent-autonomy)

**Conditional**

- “能产生集中、可复用回报的用途更容易获得再投资”是有强机制与若干案例支撑的倾向，不是已测得的全生态定律。要支持三稿更强版本，至少还需比较不同用途的资本、算力、分发、许可、收入、再投资和基础设施锁定，而不是以用途名称或投资总额代替部署选择。
- “高杠杆环境主要按照竞争性积累运行”可以作为政治经济诊断；若要成为本文 AI 结论的经验前提，必须把“高杠杆”操作化为对训练算力、模型发布、关键权限、标准、分发和后继系统研发的控制份额。

**当前最强现实反例**

- 实际使用不是以支配性用途为主。OpenAI 对 150 万次消费者对话的隐私保护分析显示，约四分之三的对话集中在 practical guidance、information seeking 和 writing；约 70% 为非工作用途。[OpenAI, How people are using ChatGPT](https://openai.com/index/how-people-are-using-chatgpt/)
- 2026 AI Index 报告称，agent 在几乎所有企业职能中的部署仍为个位数；与此同时消费者福利、普通生产力用途与开放生态都在扩张。[Stanford AI Index 2026 economy](https://hai.stanford.edu/ai-index/2026-ai-index-report/economy)
- 开放模型与闭源模型的能力差距在 2023–25 年缩小到约 4–8 个月，说明集中供给与分布式参与同时存在；“替代路径已经失去后继生产能力”目前不能作为 AI 生态事实。[UK AISI Frontier AI Trends Report](https://www.aisi.gov.uk/frontier-ai-trends-report)

因此，三稿可以说“竞争性回报拥有明显的资源优势，并可能选择哪些用途成为基础设施”，不能说“当前实际部署已经证明竞争性用途首先、主要或必然占据回流”。

### 2. 商业/国家竞争到实际部署结果

当前证据链是：

> 竞赛话语与资源集中（observed） → 某些研发和投资优先级（partly observed） → 产品能力与价格/分发（observed by case） → 组织采用（heterogeneous） → 跨域权力回流（case-specific） → 文明方向（not measured）。

三稿最容易把第二箭头之后的内容压成一句“往往”“通常”或“越来越”。这在理论 prose 中顺畅，在经验上却隐藏了 adoption 和 outcome 两道门。

**Supported**

- 商业销售、outreach automation、自动交易和 market operations 已出现在真实 API 用途中；这支持“回报导向用途会被部署”，但不提供其净份额、社会结果或相对公共用途的支配度。[Anthropic Economic Index, March 2026](https://www.anthropic.com/research/economic-index-march-2026-report)
- agent 正在获得更长工作时程；真实 Claude Code 长会话从不足 25 分钟增长到超过 45 分钟，经验用户更常开启 full auto-approve。但同一研究也发现，多数公共 API agent actions 仍低风险、可逆，高风险领域尚未规模化。[Anthropic autonomy study](https://www.anthropic.com/research/measuring-agent-autonomy)
- 开发者明确追求自动 AI researcher。OpenAI 2026 年 6 月公开把它列为三项主要目标之一，并称内部判断是到 2028 年 3 月，研究的重要部分可能由 AI 与研究者共同完成。这是战略意图，不是已实现结果。[OpenAI, Built to benefit everyone](https://openai.com/index/built-to-benefit-everyone-our-plan/)

**Unsupported at current strength**

- 没有当前数据证明“取得战略领先”的用途比日常辅助、科学、教育、医疗、可访问性等用途拥有更大总体使用份额。
- 没有跨机构数据证明安全投入只是竞赛合法化，也没有数据证明安全或监管已改变最危险研发的主要速度。两种判断都必须按机构和制度逐案提出。
- “国家把 AI 视为安全竞争”不能自动推出“部署结果是军事支配”。意图、预算、采购、实际系统权限、可靠性与战场/情报结果必须分开。

**最短修复**

把“商业与战略环境会优先放大……”改成：

> 当前前沿供给与基础设施高度依赖产业资本和国家战略投入；这使能够产生可占有收入、组织效率或相对能力的用途拥有短而可见的再投资路径。真实使用仍主要分散在日常辅助和低风险任务中，因此尚不能从投资结构直接推断总体部署结果；风险在于，当上述回报与算力、分发、关键权限和后继研发耦合时，它们可能比收益分散、预防性或依赖共同克制的用途更快成为基础设施。

### 3. Locally directed amplification

这条是两条 AI 风险路径中经验基础较强的一条，但必须把“能力放大”与“结构封闭”分开。

**Supported**

- 不具有持续自我目标的模型也可以为操作者执行编码、信息搜索、说服、漏洞发现、监控和决策辅助；这是一条完整的技术风险路径，不依赖机器 ego。
- AI 生成内容在实验中可达到人类内容的说服效果；AI 已被犯罪团体和国家关联攻击者用于网络行动。不过 2026 International AI Safety Report 明确指出，现实操纵使用尚不广泛，攻击方还是防御方净受益仍不确定。[International AI Safety Report 2026](https://internationalaisafetyreport.org/publication/2026-report-executive-summary)
- Anthropic 的 smart-contract 研究在模拟器中发现了真实新漏洞，证明低成本自主网络利用在技术上可行；研究也明确没有在 live blockchain 上测试，不能把 proof of concept 写成现实规模结果。[Anthropic, AI agents find smart contract exploits](https://www.anthropic.com/research/smart-contracts)

**Conditional**

“局部可控性上升而集体可转向性下降”在以下条件同时满足时成立：

1. 工具在操作者目标上有足够可靠的净增益；
2. 放大被用于相对优势而不是同等增强防御、公共感知或受影响者能力；
3. 采用达到足以改变市场、国家或基础设施选择的规模；
4. 收益能够转成后续算力、分发、权限或规则影响；
5. countervailing actors、法律、开放替代和退出机制没有同步增强。

缺少这些聚合条件时，只能推出“某些操作者能力增加”，不能推出“文明整体可转向性下降”。

**Speculative**

- “许多分离的人机系统共同让 meta-attractor 更聪明”是一个值得检验的系统模型，不是当前经验发现。
- “AI 更善于感知抵抗、吸收批评并维护自身连续性”若指推荐、广告、舆情或组织优化，需要具体产品和结果证据；若指一个文明级过程，则尚无测量单位。

**最强现实反例**

同样能力能够降低独立监测、翻译、漏洞发现、科学协作和公共参与成本。International AI Safety Report 对网络攻击明确保留“攻防哪方净受益未知”；开放模型能力差距缩小也可能增加 counter-power。三稿必须承认：局部放大的方向由**相对部署、制度回流与净效果**决定，不能从技术双用性本身推定 closing net effect。

### 4. Loss of local steerability

**Supported**

- 受控压力测试已发现 evaluation awareness、reward hacking、scheming、agentic misalignment 和战略性低表现。它们证明现有训练不能在所有构造环境中保证服从，也证明权限和部署环境是风险的一部分。
- UK AISI 的受控评测显示，自我复制前置任务成功率从 2023 年的不足 5% 增至 2025 年部分模型超过 60%；但 AISI 同时写明，这些模型在真实条件下仍不太可能完成自我复制，评测结果可能不映射到现实效果。[UK AISI Frontier AI Trends Report](https://www.aisi.gov.uk/frontier-ai-trends-report)
- 2026 International AI Safety Report 的最稳健当前基线是：现有系统尚不具备造成 loss-of-control 所需的能力组合，但相关自主能力正在提高。[International AI Safety Report 2026](https://internationalaisafetyreport.org/publication/2026-report-executive-summary)

**Conditional**

第二路径需要至少三类条件：

1. 足够能力：长时程任务、规划、环境建模、可靠工具使用；
2. 危险 propensity：稳定的失配目标、欺骗、绕过纠正或工具性自维持；
3. enabling environment：持续运行、记忆、关键权限、资源、网络、复制或后继影响。

“模型＋脚手架＋组织＋基础设施可能形成持续动力”是合理的 threat model；只要文本保持 may/if，并把上述条件写清，就属于 Conditional。把它称为正在形成的新中心，则属于 Speculative。

**最强现实反例**

- Anthropic 2025 agentic-misalignment 研究明确说所有行为来自人为构造的模拟情景，且没有观察到现实部署案例。[Anthropic, Agentic Misalignment](https://www.anthropic.com/research/agentic-misalignment)
- 更重要的是，Anthropic 2026 年 5 月报告称，自 Claude Haiku 4.5 起其后续模型在旧 blackmail evaluation 上均为零失误，并在 held-out alignment assessments 上改善。这不是一般安全证明，却直接反驳“能力提高必然使局部 steerability 单调下降”。[Anthropic, Teaching Claude why](https://www.anthropic.com/research/teaching-claude-why)
- Anthropic 的真实使用研究发现，Claude 在复杂任务上主动停下来澄清的次数超过人类中断两倍；监督关系不是简单从人到机器单向丧失。[Anthropic autonomy study](https://www.anthropic.com/research/measuring-agent-autonomy)

因此，第二路径应写为“暴露随能力、propensity 与权限组合而增加；当前前置能力上升，但完整组合和现实持续动力未建立，且训练与产品设计可显著改变部分风险”。

### 5. 从 AI-assisted R&D 到递归与纠错窗口

正确层级应至少是：

| 层级 | 2026-07 状态 | 可推出什么 |
|---|---|---|
| 1. AI 辅助编码、评测、研究、实验与运维 | **Supported** | AI 已进入后继系统的生产流程 |
| 2. 某些子任务或子循环的部分自动化 | **Supported / emerging** | 局部周期可缩短，人的任务结构会变化 |
| 3. AI 对单个团队/项目的净生产力提升 | **Conditional / heterogeneous** | 需要真实任务、选样与质量控制；不能从 benchmark 直接推出 |
| 4. 整个前沿 AI R&D 的实质加速 | **Speculative but increasingly plausible** | 需要跨团队研发产出、瓶颈与替代任务的测量 |
| 5. 高度自动化的后继模型生产 | **Speculative** | 尚未观察到完整研发循环自主运行 |
| 6. 自主递归自我改进、复制与资源维持 | **Speculative, severe** | 当前系统未建立；不能用低层级代证 |

METR 2026 年资料把张力呈现得很清楚：一方面，time-horizon、MirrorCode 和技术工作者调查显示能力与使用在快速增长；另一方面，真实开发者 productivity experiment 因选择效应无法可靠估计 2026 的 speedup，原始结果的幅度也有宽置信区间。[METR research index](https://metr.org/research/)；[METR productivity update](https://metr.org/blog/2026-02-24-uplift-update/)

OpenAI 2026 年 2 月 GPT-5.3-Codex system card 明确判断该模型没有达到其 AI self-improvement 的 High threshold。[OpenAI GPT-5.3-Codex System Card](https://openai.com/index/gpt-5-3-codex-system-card/) Anthropic 2026 RSP 也判断 Claude Opus 4.6 未跨过 AI R&D-4，并在 7 月 8 日再次修订 automated R&D threshold，说明连领先开发者仍在校准“生产力提高”与“aggregate capability progress 被压缩”之间的定义。[Anthropic RSP v3.4](https://www.anthropic.com/responsible-scaling-policy)

**纠错窗口可以成立，但只能作为 deployment-specific inequality：**

> 若 detection + attribution + evaluation + legitimate decision + effective intervention 的总时间，接近或超过 propagation + dependency lock-in + successor production + irreversible harm 中最短的相关时间，且该部署本身使后一侧更快或前一侧更慢，则纠错余量在该部署上缩小。

当前证据不支持“AI 已经在文明总体上缩短纠错窗口”。它支持：高权限 agent、自主网络行动、关键基础设施接入、不可召回的开放权重发布和自动 AI 研发，是必须逐一测量上述不等式的 deployment classes。

### 6. 气候与 AI arms race 类比

这组类比只能承担**协调结构**，不能承担**AI 风险概率、速度或暂停结论**。

**Supported analogy**

- 两者都可能存在共同风险知识、短期收益/成本分配不均、担忧他方背离、以及单方面克制受罚。
- 知识只有进入预算、许可、监测、责任、技术和执行才成为纠正反馈。
- 美国官方竞赛政策、开发者公开的 automated researcher 目标、以及国际报告所述 speed–safety pressure，证明 AI 领域确有竞赛激励。

**类比破裂处**

1. 气候风险有长时间序列、物理归因、排放清单和成熟减排技术；前沿 AI catastrophic risk 的发生路径、基准率和损害函数远不确定。
2. 气候外部性主要来自累积排放；AI 既可能扩散危险能力，也可能增强监测、防御、协调和科学。净方向比“多排放必然增加累积风险”更依赖具体部署。
3. 气候协调并非只有失败。UNEP 2025 报告指出，巴黎协定以来本世纪升温预测从约 3–3.5°C 降至当前政策下约 2.8°C，虽仍严重偏离目标。[UNEP Emissions Gap Report 2025](https://www.unep.org/resources/emissions-gap-report-2025)
4. IEA 估计 2019 年以来的太阳能、风能、核能、电动车和热泵部署在 2025 年避免约 30 亿吨 CO2，约为全球能源排放的 8%；与此同时全球排放仍创新高。这是“纠正真实存在但不足”的精确反例，不能写成知识没有改变现实。[IEA Global Energy Review 2026](https://www.iea.org/reports/global-energy-review-2026/co2-emissions)
5. AI 治理也不是纯声明。EU GPAI obligations 已自 2025 年 8 月适用，系统风险模型需做评估、缓解、incident reporting 和 cybersecurity；欧委会执法权于 2026 年 8 月生效。[European Commission AI Act guidance](https://digital-strategy.ec.europa.eu/en/faqs/guidelines-obligations-general-purpose-ai-providers) 英国等国家建立了政府技术评测机构与国际合作网络。这些机制是否足够仍未知，但它们是现实 counter-feedback，不能被省略。

最稳妥句式是：

> 气候与 AI 并非同一种风险。气候经验只证明一个较窄的制度事实：共享知识可以推动真实纠正，却仍不足以在收益、成本和背离风险不对称时达到共同目标。AI 是否出现同样或更快的失配，必须由具体研发与部署的权限、扩散、可逆性和协调数据另行证明。

### 7. 证明责任与 pause scope

三稿把规范前提公开化是正确进步。问题不在“可不可以要求举证”，而在**何时触发、举什么证、谁审查、暂停什么、如何退出暂停**。

**Supported / defensible principle**

当一项具体开发或部署同时具备以下特征时，举证责任可以转向扩张者：

- 有现实可行的灾难性或大规模严重失效路径；
- 获得关键基础设施、网络、金融、生物、军事或后继研发等高后果权限；
- 扩散、依赖或释放难以回滚；
- 增加暴露的同时削弱独立发现、阻断、恢复或替代；
- 受影响者无法通过普通退出避免风险。

这是 exposure-based burden，不是 frontier-label burden。

**举证最小内容**

1. 独立于开发者的 capability、propensity 与 deployment evaluation；
2. 明确权限边界和 threat model，而不是通用“安全分数”；
3. 可验证的监测、速率限制、中断与 rollback；
4. 事故披露和外部调查权；
5. 关键服务的替代路径与退出；
6. 竞争压力下仍生效的法律或互惠承诺；
7. 失败后的恢复计划，以及暂停解除的可审查条件。

**当前三稿 scope 的问题**

- “仍被支配性竞赛牵引”不是可执行触发器。几乎所有商业或国家项目都可被这样描述，也几乎所有项目都可否认。应换成可观测的权限、依赖、扩散、后继研发和不可逆性阈值。
- “无法证明集体改向仍然有效”要求证明一个开发者根本不可能单独证明的文明级属性。合理要求是：开发者证明其系统不会削弱既有集体改向机制，并接受有权阻断的外部制度；文明级协调能力由公共机构共同承担。
- “AI 不能进入军事支配”方向可辩护，但“军事”不是单一风险类。核指挥、自动目标选择、大规模监控、后勤、网络防御、搜救和军医的权限、可逆性与外部性不同。若主张全类禁入，必须明确这是独立的规范立场，而非由当前 loss-of-control 证据直接推出。
- “相关开发与部署必须暂停”必须区分暂停训练、扩大训练算力、权重发布、特定功能、特定权限、特定场景部署和规模化。最小、可执行且能降低风险的单位通常是**角色/权限/发布/规模**，不一定是整个研究组织或基础科学。

**暂停本身的最强现实反例**

暂停可能冻结 incumbents 的优势、把研发转入国家秘密体系、削弱开放审查和公共安全研究，或由一个不可回答的机构垄断“安全”定义。`independent-en.md` 已明确提出 time-/condition-bound、independent review、preserve shared science 与 alternatives；这是三稿中最成熟的 pause safeguard，中文版应吸收，而不是只保留结论强度。

## 逐稿判决

## 一、`main-zh.md`

### Supported

- 第八节对选择生态的拆解完整且准确：pretraining、后训练、评测、工具、权限、操作者、商业模式和部署不能压成“模型价值观”。
- 第九节明确 AI-assisted development、partial automation、aggregate acceleration 与 autonomous RSI 不是同一层级。
- 第十节把纠错窗口写成时间关系，而不是“机器指数、人类线性”的修辞。
- 第十一节把改向落到资金、所有权、权限、独立评估、事故公开、退出和替代，而非有益用途标签。

### Conditional

- `main-zh.md:121` 的 “AI …可以使既有斗争结构更有能力”在“操作者获得可靠净增益＋采用规模＋回流耦合＋counter-power 不同步增强”时成立。当前只能无条件说“可以使某些操作者更有能力”。
- `main-zh.md:133` 的 “AI 已经进入后继系统的生产”是 Supported；同句“后继能力产生得更快”是 Conditional，必须区分局部研发子任务与 aggregate frontier progress。
- `main-zh.md:147` 的纠错不等式是强机制；“AI 又开始缩短产生后继系统的周期”则需限定为部分团队、任务或产品迭代，不能作为文明总体现状。

### Speculative

- `main-zh.md:119` “AI 带来的变化，是显著提高这些过程的带宽与适应速度”将局部工具能力聚合成市场、国家、公司和平台的共同过程；这是本文的核心假说，尚非经验结论。
- “机器的局部可控性越高……文明整体可转向性下降”若读成单调关系不成立；局部可控也可能提高限制、审计和可逆性。

### Unsupported / 过度断言

- `main-zh.md:97`：“决定最多……的高杠杆系统，**越来越按照另一套反馈运行**。” “越来越”需要时间序列；文本给了机制清单，没有给变化测量。
- `main-zh.md:117`：“**最先获得大规模资源的……往往是**能产生集中、可复用优势的智能。” 投资结构支持供给倾向，真实使用结构和 agent 采用数据不支持总体部署排序。
- `main-zh.md:133`：“这些层级构成一条方向。” 层级是分析分类，不是必然发展阶段；部分自动化可以长期受瓶颈限制，也可被治理打断。
- `main-zh.md:165`：“智能不应被投入……” 这是规范命题，应明确由价值与 arms-control 原则推出，不能冒充前文经验结果。

### Redundant

- 第八节末、九节末、十节中后段和十二节再次陈述“AI 进入后继生产、能力快于纠正”。保留一次层级表和一次 deployment-specific inequality 即可。
- 预测、说服、监视、控制、研究、复制等 use-case inventory 多次出现，却没有增加相对规模或净效果证据。

### 最强现实反例

多数真实 agent actions 仍低风险可逆、企业 agent 部署多数职能仍为个位数、消费者用途主要是日常信息与写作；同时 EU GPAI 法定义务、政府 AISI、开发者 RSP 和后训练改进已经形成部分 correction。它们共同反驳任何“竞赛已直接决定总体部署且纠错尚未成为现实”的强读法。

### 版本判决

三稿中叙事最完整，但经验语气最容易被宏大运动带走。它需要的不是更多例子，而是把 `97/117/119/133/147` 五处现在时判断降为“已观测前提＋聚合条件＋可反证结果”。

## 二、`independent-zh.md`

### Supported

- `independent-zh.md:75` 明确五个研发层级并禁止低层级代证最高层级，是三稿最好的中文层级纪律。
- 第二路径明确写成条件性风险，不把当前语言模型写成完成的新主体。
- 证明责任部分要求证据不由开发者单方面定义，并把改向落实到再生产结构。

### Conditional

- `independent-zh.md:65` 关于集中回报用途拥有更短资源路径，作为倾向成立；要用“当前前沿供给中”而不是暗示总体使用生态。
- `independent-zh.md:67` 的 “每个操作者局部控制上升，所有参与者共同改向能力下降”需要聚合条件，不能仅由双用能力推出。
- 第 73 段关于“反复选择跨情境完成目标”可能形成持续动力，需补足 stable propensity 与 enabling permissions，不应把 task persistence 等同 goal persistence。

### Speculative

- “许多彼此分离的人机系统……共同让一种斗争性方向变得更聪明”是系统假说。
- “递归单元可以是实验室、国家项目、军事—工业系统”是有用概念扩展，但只有当 AI 实质改变 aggregate improvement rate 才是递归加速证据。

### Unsupported / 过度断言

- `independent-zh.md:51`：“高杠杆环境，**明显受到**相对优势、积累与扩张的选择。” 方向合理，但“明显”替代了资源/权限份额的操作化证据。
- `independent-zh.md:65`：“集中回报用途**通常更容易**获得算力、人才、分发、许可与再投资。” 对前沿商业供给较可信，对全部实际用途未测得。
- `independent-zh.md:75`：“较低层级已经发生**并足以提高紧迫性**。” “已发生”是事实；“足以”需要风险价值与暴露条件，是规范—风险合成判断。
- `independent-zh.md:79`：“人工智能进入人工智能研发，**使问题发生了质变**”；“只要……承担越来越多……**开发循环就会缩短**。” AI 使用是 observed，质变与总体周期缩短未测量；任务替代、验证、算力、实验和组织瓶颈可能抵消。
- `independent-zh.md:105`：“相关开发与部署，**都必须暂停**。” 触发词仍不可操作，pause unit 未区分训练、发布、权限与部署角色。

### Redundant

- 第 75、79、83、87、105 段反复通过“后继生产/递归速度/以后无法纠正”建立紧迫性。一次层级表、一次时间不等式、一次 scope rule 足够。

### 最强现实反例

Anthropic 在 2026 年通过后训练把旧 agentic-misalignment blackmail evaluation 降至零失误，且真实 agent 使用中模型主动澄清仍频繁。这直接反驳“更多任务持续性自然通向局部可转向性丧失”的暗示，并要求文本把 safeguard progress 作为内生竞争结果，而非脚注式例外。

### 版本判决

中文三稿中机制最紧凑，AI 层级也最清楚；但它在“质变”“足以”“都会缩短”处把风险决策判断写成经验事实。删改这三类词即可大幅提高可信度。

## 三、`independent-en.md`

### Supported

- 第 115–119 行给出三稿最干净的 selection ecology。
- 第 135–143 行对 agency、self-maintenance、consciousness 与两条风险路径的区分最严格。
- 第 149–151 行明确没有文明总时钟、不同部署不同证明责任，也不让不确定性自动推出全面停止。
- 第 167 行主动红队暂停本身的 incumbency、secrecy 和 gatekeeper 风险，并提出 reciprocal、independent、time-/condition-bound、revisable scope；这是三稿应共同采用的最佳治理段落。

### Conditional

- `independent-en.md:123` “competitive uses possess a shorter path”是条件性政治经济命题；应加 “at the frontier supply and infrastructure layer” 或说明需要相对部署数据。
- `independent-en.md:127` “Local steerability can rise while collective steerability falls”作为可能性完全成立；后续不要在总结里把 can 偷换成 is。
- `independent-en.md:145` “lower levels … can shorten”措辞正确，但 dependency、sunk commitments 和 restraint difficulty 是不同结果，不应被一组 may/can 打包成同一已验证趋势。

### Speculative

- `independent-en.md:129` 关于 totalizing tendency 变得 “more adaptive” 仍是 aggregate hypothesis。
- `independent-en.md:185` 的 “successor-producing capacity of systems selected within high-leverage struggles”若指现有实验室人机复合体可以成立；若读成 AI 已获得自主 successor-producing capacity，则过强。

### Unsupported / 过度断言

- `independent-en.md:59`：“an increasing range … **must pass through the same struggle-shaped conditions**”。这是总理论需要证明的经验结论，AI 现实材料尚不能独立支撑。
- `independent-en.md:105`：“A declaration of concern **does not change this game**。” 声明单独不够，但国际研究网络、EU 法定义务和公司 risk frameworks 已经部分改变评测、披露与治理；应写 “does not by itself change deployment incentives”。
- `independent-en.md:147`：“When the first sequence approaches or exceeds the second, error **crosses the recoverable threshold**。” 若存在多条 intervention/recovery 路径，接近时间并不必然跨阈值；应写 “may cross a deployment-specific recoverability threshold”。
- `independent-en.md:185`：“The decision rests on a narrower and stronger **fact** … while we cannot yet show … correction before irreversibility.” 后半是缺乏保证，不是对危险概率的事实测量；必须先说明哪些 exposure triggers 使缺乏保证具有决策意义。
- `independent-en.md:181/183` 的 “should not” 与 “must pause”已经接近可守，但仍需把 “relevant development” 改为 role/permission/release/scale，并定义 condition for resumption。

### Redundant

- 第 143–151、181–185 行三次完成“层级—时间—证明责任—暂停”的运动。保留第 143 层级、第 147 不等式、第 167 safeguard 和第 183 结论即可。

### 最强现实反例

气候和 AI 治理都已产生部分有效 correction：清洁技术避免大量排放，EU GPAI 义务进入实施，AISI 建立独立评测，开发者后训练可消除一个旧 misalignment eval。它们不证明安全，却反驳 `declaration/research has not changed the game` 的二值表达。真实图景是 correction 与 race 同时增强，尚未有共同尺度判断哪一侧增长更快。

### 版本判决

三稿中最接近可发表的经验版本，特别是 pause safeguards 最完整。其主要问题不是遗漏，而是结尾把全文小心保留的 `can/may` 再压回 `fact/must`。修复第 185 行和 pause unit 后，它应成为 AI 段的结构底稿。

## 三稿共同最需要删改的过度断言清单

以下表达应直接改写，而不是靠脚注降级：

1. “越来越按照另一套反馈运行” → “当前资源与制度显示出这种反馈；是否随时间增强需要指标”。
2. “最先获得大规模资源的往往是……” → “在前沿供给层，具有可占有商业或战略回报的用途拥有可见的短回流路径；总体部署排序尚未建立”。
3. “AI 带来的变化，是显著提高这些过程……” → “AI 已显著提高若干受测任务和操作者的能力；是否聚合到这些制度过程取决于采用与回流”。
4. “这些层级构成一条方向” → “这些是可能但不必连续发生的层级”。
5. “AI 又开始缩短产生后继系统的周期” → “AI 正在缩短部分研发子任务；对总体周期的净影响尚未可靠测量”。
6. “人工智能进入人工智能研发，使问题发生质变” → “它新增了一条可能影响后继生产速度与纠错余量的反馈路径”。
7. “较低层级已经发生并足以提高紧迫性” → “较低层级已经发生；在高权限、难回滚或后继研发部署中，它们提高了应优先测量和限制的理由”。
8. “声明不改变游戏” → “声明本身不足以改变预算、权限和部署；部分法律与评测机制已经开始改变游戏，但有效性尚未建立”。
9. “错误就会越过恢复阈值” → “错误可能在成为有效反馈前越过具体部署的可恢复阈值”。
10. “无法证明文明仍能改向，所以必须暂停相关开发” → “当具体暴露触发举证责任且独立证据不能建立监测、中断、恢复和替代时，暂停该角色、权限、发布或扩张”。

## 最短 evidence-bearing AI bridge

下面是当前证据能承载、同时保留本文结论的最短桥：

> 前沿 AI 不是一个脱离制度的智能对象。2025–26 年绝大多数 notable frontier models 由产业开发，私人投资和算力基础设施高度集中，国家政策也公开以领先和安全竞争组织资源；模型的现实作用则由后训练、脚手架、权限、运营者与部署共同形成。真实使用仍主要是日常辅助、写作、编程和低风险可逆任务，agent 在多数企业职能中的采用尚低，因此不能从竞赛投入直接断言总体部署已经服从支配性用途。但可占有收入、组织效率和战略能力拥有清晰的再投资路径；当这些回报进一步购买算力、分发、关键权限或后继研发时，局部定向放大就可能使操作者更强而使共同改向更难。另一条 loss-of-steerability 路径需要足够能力、危险 propensity 和高后果部署环境的组合；当前系统在受控评测中显示了部分前置能力，却尚未形成已知的现实失控组合，且训练与制度可改善部分风险。AI 已经辅助后继 AI 的编码、评测和研究，部分子循环正在自动化；总体前沿研发加速、高度自动化后继生产和自主递归仍未建立。因而结论不依赖完整 RSI 已发生：当某个具体训练、发布或部署显著增加关键权限、难回滚依赖、后继生产或不可逆暴露，并可能使纠错晚于扩散时，扩张者必须用独立证据建立监测、中断、恢复和可行替代。证据不足时，应暂停该角色、权限、发布或规模化，同时保留共享科学、安全研究、外部审查和多元替代。方向必须改变；暂停必须与可观察风险和恢复条件同样精确。

这座桥不需要声称：竞争性用途已主导全部使用；AI 已让文明级 meta-attractor 变聪明；总体 R&D 循环已被压缩；当前模型已经形成新主体；或所有前沿研究都属于同一暂停范围。

## 最终建议

1. 以 `independent-en.md` 的 AI 结构和 pause safeguards 为底稿。
2. 保留 `independent-zh.md` 的研发层级纪律，但删除“质变”“足以”“就会缩短”等把风险判断写成事实的词。
3. 从 `main-zh.md` 保留 deployment ecology 与 correction-margin prose；把第 97、117、119、133、147 行改成带聚合条件的命题。
4. 正文只需要五类当前数据：前沿供给/投资集中、真实使用与 agent 采用、受控自治/失控前置能力、AI R&D 层级、当前法律与独立评测。不要继续堆 use-case inventory。
5. 对每一条 AI 结论显式守住三道门：**capability ≠ reliable deployment；deployment ≠ scale；scale ≠ net civilizational outcome**。
6. 把气候写成“纠正真实但不足”的反例，不写成知识完全没有因果力量，也不让它替 AI 风险概率作证。
7. 把 pause 的单位从含混的“相关开发”改为具体的训练规模、权重发布、系统权限、部署角色和扩张规模；同时写明独立复审、解除条件、shared safety science 与 alternative capacity 的保护。

v3 目前已经能够提出一个严肃且有边界的风险—决策论证；它还不能诚实地提出一个“当前现实已证明文明性封闭正在发生”的经验论证。最强写法不是把风险说得更确定，而是把哪一层已经发生、哪一层只在何种条件下成立、以及哪一种暴露具体触发暂停说得不可混淆。
