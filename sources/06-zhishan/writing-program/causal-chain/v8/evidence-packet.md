# Causal-chain V8 — Movement V evidence packet

资料截止：**2026-07-13**

用途：只为三份 V8 首稿承重 Movement V 的现实链。本文件不做政策建议、规范论证、AI 总效用结算，也不替正文选择修辞。

## 证据状态

- **[已观察]**：来源直接披露了事件、测量、合同、财务结果或已发生的组织行为。
- **[合理推断]**：由多项已观察事实支持，但来源没有直接测量该因果关系，或反事实仍不清楚。
- **[未证明]**：截至资料截止日不能当作现在事实写入正文。
- 公司公告能证明公司做了什么、报告了什么或承诺了什么；不能单独证明其产品效果、未来交付或社会后果。
- “announced / ceiling / planned / projected / mobilise” 分别是宣布、合同上限、计划、预测、拟撬动，不等于已支付、已建成或已产生结果。

## 一页结论

| Movement V 所需环节 | 当前证据状态 | 最窄可承重判断 | 会削弱过强诊断的事实 |
|---|---|---|---|
| 前沿模型、资本、算力与组织集中 | **已观察，强** | 前沿模型生产主要在产业组织；训练算力、先进芯片制造和私募资金高度集中 | 顶级模型并非一家垄断；中美模型差距接近消失；开放模型与开放项目仍在扩张 |
| 收入、估值、云与芯片收益回流 | **已观察到资源回流；完整因果仅属合理推断** | 融资明确被用于算力；云商把现金流投入 AI 基础设施；芯片商在收入增长同时大增研发和内部算力支出 | 许多前沿开发商尚未证明稳定盈利；capex 不全属于前沿 AI；承诺未必交付；高支出已压低自由现金流或利润率 |
| 国家战略与安全需求回流 | **已观察，强于“效果”证据** | 美国、欧盟、中国及国防机构已经把 AI 作为竞争力、主权或安全能力配置资金、采购与组织 | 预算上限不等于拨付；部分公共算力明确面向开放、科研和中小企业；多供应商采购也在降低单一依赖 |
| AI 进入 AI 研发 | **已观察到编码、实验与有明确评分器的优化；完整自动化未观察** | AI 已经参与前训练工程、代码、实验、内核、芯片布局和训练效率优化，能够缩短若干研发子循环 | 长任务收益明显下降；真实研发目标含混、反馈慢；没有证据证明端到端前沿研发或自我维持的递归改进已经实现 |
| 依赖、切换成本、独立评估与替代 | **依赖和信息不对称已观察；“不可退出”未证明** | 云—模型合作含回购云服务、排他/控制权、技术耦合与敏感信息共享；闭源前沿系统限制外部可见性 | 多云、开放权重、独立评测机构、开源评测工具和监管介入都真实存在；资金充足的开发商已能跨云扩张 |
| 真实反向反馈 | **已观察** | 出口管制、竞争执法、物理电网约束、预部署评测和法律义务已经改变收入、合同、工程或发布行为 | 反向反馈的覆盖、独立性和持续效果尚未证明；多数前沿安全框架仍主要是自愿安排 |

---

## 1. 前沿 AI 的资本、算力与组织集中

### 1.1 模型生产与组织

- **[已观察]** Stanford 2026 AI Index 统计，2025 年超过 90% 的 notable AI models 由产业界产生；同时，若干资源最密集系统已不再披露训练代码、参数量、数据集规模和训练时长。[Stanford HAI：Research and Development](https://hai.stanford.edu/ai-index/2026-ai-index-report/research-and-development)
  - 限度：“notable” 是入选口径，不等于全部 AI 研究；“产业界”也不是单一公司。该事实支持“前沿模型生产组织集中于产业”，不单独证明市场垄断。
- **[已观察／反向观察]** 截至 2026 年 3 月，Anthropic、xAI、Google、OpenAI、Alibaba、DeepSeek 均处于 Arena 顶部梯队；美国最强模型相对中国最强模型的领先仅为 2.7%，且领先位置自 2025 年初多次互换。[Stanford HAI：Technical Performance](https://hai.stanford.edu/ai-index/2026-ai-index-report/technical-performance)
  - 这削弱“一个组织已经控制前沿”或“国家间能力差距只会扩大”的说法，但不削弱高成本前沿主要由少数大型组织生产的事实。
- **[已观察]** 英国 CMA 在 2024 年识别出 Google、Apple、Microsoft、Meta、Amazon、Nvidia 六家大公司之间超过 90 项与 foundation models 有关的伙伴关系和战略投资；CMA 同时承认这些关系可以带来资源、专业能力和创新。[CMA：Foundation Models update](https://www.gov.uk/government/news/cma-outlines-growing-concerns-in-markets-for-ai-foundation-models)
  - 限度：这是关系网络计数和竞争风险判断，不是已证明的合谋或排除效果。

### 1.2 算力、芯片与制造链

- **[已观察，估算口径]** AI Index 估计全球 AI 算力容量自 2022 年以来年均增长约 3.3 倍，至 2025 年达到 1,710 万 H100-equivalents；Nvidia 占总量 60% 以上，Google 与 Amazon 提供其余大部分，Huawei 份额较小但上升。[Stanford HAI：Research and Development](https://hai.stanford.edu/ai-index/2026-ai-index-report/research-and-development)
  - 限度：H100-equivalent 是跨硬件折算估计，不等于所有芯片销量或实际可用训练集群。
- **[已观察]** 同一报告称，TSMC 制造几乎所有领先 AI 芯片；TSMC 的美国扩建于 2025 年开始运营。报告同时统计美国有 5,427 个数据中心，数量超过任何其他国家十倍。[Stanford HAI：Research and Development](https://hai.stanford.edu/ai-index/2026-ai-index-report/research-and-development)
  - 限度：数据中心“数量”没有按功率或加速器容量加权；TSMC 是制造集中，不表示芯片设计或云服务也只有一家。

### 1.3 资本集中

- **[已观察，数据库统计]** AI Index 的 Quid 数据显示，2025 年全球 AI 私人投资约 3,447 亿美元，同比增长 127.5%；其中生成式 AI 约 1,709 亿美元。单笔超过 10 亿美元的融资事件由 2024 年 15 起升至 2025 年 28 起；报告明确判断资金分布比获投公司数量增长得更集中。[Stanford 2026 AI Index，Economy chapter](https://hai.stanford.edu/assets/files/ai_index_report_2026_chapter_4_economy.pdf)
- **[已观察，地理口径]** 2025 年美国私人 AI 投资约 2,859 亿美元，为中国私人投资的 23.1 倍；但该口径不含中国政府引导基金，因此不能当作中美 AI 总投入比。[Stanford 2026 AI Index，Economy chapter](https://hai.stanford.edu/assets/files/ai_index_report_2026_chapter_4_economy.pdf)
- **[合理推断]** 资本、训练算力、先进制造、云分发和前沿模型组织的集中重叠，使少数组织更容易持续承担下一轮训练、推理和人才成本。
- **[未证明]** 这些数据没有证明：单一公司或国家已经垄断前沿；非前沿研究已经消失；替代组织永远无法进入；集中必然继续上升。

### 反向观察

- **[已观察]** 2025 年 GitHub 上 AI 开源项目达到约 560 万，Hugging Face 上传量自 2023 年以来增长约三倍。[Stanford HAI：Research and Development](https://hai.stanford.edu/ai-index/2026-ai-index-report/research-and-development)
- **[已观察]** 截至 2026 年 3 月，最强闭源与最强开放模型的报告性能差距约 3.3%；差距较 2024 年 8 月的 0.5% 有所扩大，但仍不存在“开放替代已经消失”的证据。[Stanford HAI：Technical Performance](https://hai.stanford.edu/ai-index/2026-ai-index-report/technical-performance)
- **[已观察]** 学术界仍是高被引 AI 研究的重要来源；“产业生产绝大多数 notable models”不能改写成“产业生产绝大多数知识”。[Stanford 2025 AI Index：Research and Development](https://hai.stanford.edu/ai-index/2025-ai-index-report/research-and-development)

---

## 2. 商业收益、估值、云与芯片如何回到下一轮能力

### 2.1 融资与估值进入算力

- **[已观察：宣布的融资]** 2026 年 2 月 OpenAI 宣布以 7,300 亿美元 pre-money valuation 获得 1,100 亿美元新投资，并把所需条件直接列为 compute、distribution 与 capital；公告称资金和合作将扩展基础设施及全球分发。[OpenAI：Scaling AI for everyone](https://openai.com/index/scaling-ai-for-everyone/)
- **[已观察：实际执行的一部分]** SoftBank 于 2026 年 7 月 1 日执行第二笔 100 亿美元投资，并披露以同额 bridge facility 借款筹资；这是其计划投入 OpenAI 的 300 亿美元中的第二笔，第三笔原计划 10 月执行。[SoftBank：Execution of Follow-on Investment](https://group.softbank/en/news/press/20260701)
  - 这能证明高估值与战略预期伴随大额股权融资、银行融资和资产负债表扩张；不能证明全部 1,100 亿美元已经到账，也不能证明估值本身是已实现收益。
- **[已观察：较早轮次的直接用途]** OpenAI 在 2025 年 3 月宣布 400 亿美元融资、post-money valuation 3,000 亿美元，并明确称融资将用于推进研究和扩大算力基础设施。[OpenAI：New funding to build towards AGI](https://openai.com/index/march-funding-updates/)

### 2.2 云收入与基础设施支出

- **[已观察]** Amazon 2025 年 AWS 收入为 1,287 亿美元、营业利润 456 亿美元。同期 Amazon 自由现金流降至 112 亿美元，主要原因是 property and equipment 购买额同比增加 507 亿美元；公司称该增加主要反映 AI 投资，并宣布 2026 年约 2,000 亿美元 capex 计划。[Amazon 2025 Q4 and full-year results](https://ir.aboutamazon.com/news-release/news-release-details/2026/Amazon-com-Announces-Fourth-Quarter-Results/default.aspx)
  - 已发生的是 2025 年收入、利润、现金流和投资增加；2,000 亿美元是 2026 年计划，且 Amazon capex 不全属于 AI。
- **[已观察 + 前瞻计划]** Alphabet 2025 年实际 capex 为 914 亿美元，约 60% 用于服务器、40% 用于数据中心与网络设备；公司给出的 2026 年 capex 区间为 1,750–1,850 亿美元，并称投资对象包括 Google DeepMind 前沿模型、Cloud 需求、产品与广告系统。[Alphabet 2025 Q4 earnings call](https://abc.xyz/investor/events/event-details/2026/2025-Q4-Earnings-Call-2026-Dr_C033hS6/default.aspx)
  - 这证明云/广告现金流与 AI 基础设施配置处在同一公司资产负债表；不提供“哪一美元收入导致哪一训练运行”的反事实因果。

### 2.3 芯片收入、研发与内部算力

- **[已观察]** Nvidia FY2026 总收入 2,159 亿美元，同比增长 65%；Data Center 收入 1,937 亿美元，同比增长 68%。同期研发支出由 129 亿增至 185 亿美元，增长 43%；公司称研发增长部分由内部 compute and infrastructure 支出增长 79% 驱动。[Nvidia FY2026 Form 10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm)
  - 这是“AI/数据中心需求扩大芯片收入，同时供应商扩大研发、人员和内部算力”的直接同周期证据。
  - **[合理推断]** 商业成功扩大 Nvidia 可用于下一代芯片和软件平台的资源；10-K 没有给出若收入较低时研发会少多少，因此严格的因果强度仍不能量化。

### 2.4 伙伴关系把投资回购为云服务和分发

- **[已观察]** FTC 对 Microsoft–OpenAI、Amazon–Anthropic、Alphabet–Anthropic 的强制信息调查发现：云商获得股权和收入分享权、不同程度的咨询/控制/排他权；AI 开发商承诺把云商投资的很大部分重新花在该伙伴的云服务；双方共享折价算力、模型/IP、训练和财务信息，并把模型集成进云商产品与平台。[FTC staff report, January 2025](https://search.ftc.gov/news-events/news/press-releases/2025/01/ftc-issues-staff-report-ai-partnerships-investments-study)
  - 这是本 packet 中“投资 → 云消费 → 产品分发 → 收入/信息 → 下一轮资源”最直接的合同结构证据。
- **[已观察／反向观察]** OpenAI 又在 2025 年与 AWS 签署 380 亿美元多年算力承诺，计划使用数十万 Nvidia GPU，并保留进一步扩张能力。[OpenAI–AWS partnership](https://openai.com/index/aws-and-openai-partnership/)
  - 它证明资本充足的前沿开发商能够跨云扩张，削弱“单一云不可退出”；同时，它没有削弱前沿算力仍集中在少数 hyperscalers 与 Nvidia 供应链的判断。

### 此处只能推断、不能写成事实的部分

- **[合理推断]** 收入、估值与战略预期通过股权融资、债务、capex、研发、人才和分发回到下一轮模型生产，形成正反馈。
- **[未证明]** 目前没有公开账目把每家前沿实验室的“模型能力提升”逐项归因于上一轮收入或估值。
- **[未证明]** OpenAI、Anthropic 等前沿模型公司尚不能仅凭公开资料证明其前沿训练已经由稳定利润自我融资；年度化收入不等于净利润或正自由现金流。
- **[未证明]** announced infrastructure commitments 不等于已建成算力；hyperscaler capex 不等于全用于前沿训练。

### 反向观察

- **[已观察]** Amazon 的 AI 相关资产投入已显著压低自由现金流；Alphabet 和 Microsoft 也披露 AI 基础设施带来更高折旧、运营成本或毛利率压力。[Amazon results](https://ir.aboutamazon.com/news-release/news-release-details/2026/Amazon-com-Announces-Fourth-Quarter-Results/default.aspx)；[Microsoft FY2025 earnings call](https://www.microsoft.com/en-us/investor/events/fy-2025/earnings-fy-2025-q4)
- **[权威综合判断]** 2026 International AI Safety Report 指出，前沿训练算力成本约 5 亿美元、下一代模型可能需 10–100 亿美元；数千亿美元基础设施投资仍是对不确定回报的押注，若收入不足，公司可能削减 scaling investment。[International AI Safety Report 2026, §1.3](https://internationalaisafetyreport.org/publication/international-ai-safety-report-2026)
  - “可能削减”是机制判断，不是已经观察到行业整体缩减。

---

## 3. 商业竞争与国家安全竞赛

### 3.1 公开的竞争目标

- **[已观察：政府目标与叙事]** 2025 年美国《AI Action Plan》把 AI 明确写成争夺全球主导地位的竞赛，并称最大 AI ecosystem 将设置标准并取得经济和军事利益；行动框架覆盖创新、基础设施、外交与安全。[White House：America’s AI Action Plan](https://www.whitehouse.gov/wp-content/uploads/2025/07/Americas-AI-Action-Plan.pdf)
  - 这证明国家战略公开使用“race / dominance / economic and military benefits”作为选择语言；不证明该理论判断必然正确，也不测量它对每家公司决策的因果效应。
- **[已观察]** 美国国防部 CDAO 于 2025 年向 Anthropic、Google、OpenAI、xAI 各授予一个 **2 亿美元 ceiling** 的协议，用于 national-security mission areas 的 frontier/agentic AI；每个协议在授予时实际 obligated 的 FY2025 RDT&E 资金约为 **200 万美元**。[CDAO announcement](https://www.ai.mil/Latest/News-Press/PR-View/Article/4242822/cdao-announces-partnerships-with-frontier-ai-companies-to-address-national-secu/)；[DoD contract notice](https://www.defense.gov/News/Contracts/Contract/article/4243673/)
  - 不得把“四个 2 亿 ceiling”写成“已经拨付 8 亿美元”。它们证明采购路径和组织关系已经建立。

### 3.2 国家与区域资源配置

- **[已观察：承诺而非全部支出]** 欧盟 2025 年启动 InvestAI，目标撬动 2,000 亿欧元 AI 投资，其中新的 200 亿欧元 facility 用于最多五座 AI gigafactories；官方把设施定位为支持复杂模型、科研、企业及开放协作。[European Commission：InvestAI](https://digital-strategy.ec.europa.eu/en/news/eu-launches-investai-initiative-mobilise-eu200-billion-investment-artificial-intelligence)；[AI Continent Action Plan](https://digital-strategy.ec.europa.eu/en/factpages/ai-continent-action-plan)
  - “mobilise” 包含公共—私人资金目标，不等于欧盟已经支出 2,000 亿欧元。
- **[已观察：跨行业基金]** 中国于 2025 年末启动国家创业投资引导基金，预计总规模 1 万亿元人民币，覆盖集成电路、量子、生物医药、脑机接口、航空航天、AI、未来能源等战略领域；官方称至少 70% 投向种子和早期企业。[中国政府网英文版：National venture capital guidance fund](https://english.www.gov.cn/news/202512/26/content_WS694e4e56c6d00ca5f9a08486.html)
  - 该 1 万亿元不是 AI 专项金额，不能全部计入 AI 投资。
- **[已观察]** AI Index 统计欧洲与中亚的国家支持 AI supercomputing clusters 由 2018 年 3 个增至 2025 年 44 个，并把 AI sovereignty 记录为国家政策的中心主题之一。[Stanford HAI：Policy and Governance](https://hai.stanford.edu/ai-index/2026-ai-index-report/policy-and-governance)

### 3.3 可承重与不可承重

- **[合理推断]** 当政府把模型、芯片、数据中心和采购同时定义为竞争力与安全投入时，相对领先可转化为预算、合同、许可、组织地位和下一轮基础设施优先权。
- **[未证明]** 公开材料没有证明所有国家 AI 投资都由安全竞赛驱动；医疗、科研、行政效率、产业政策和公共服务也是明示目的。
- **[未证明]** 战略投入将必然产生技术领先、国家安全或商业回报。

### 反向观察

- **[已观察]** DoD 的 Open DAGIR 明确采用竞争采购、government-owned interoperable repositories、多供应商接入，并说明其结构“not about a single company or product”。[CDAO：Open DAGIR](https://www.ai.mil/Initiatives/Open-DAGIR/)
- **[已观察]** 欧盟 AI Factories / gigafactories 的官方设计包含大学、中小企业、初创公司和开放协作，不只是把公共资源交给既有前沿公司。[European Commission：AI Continent Q&A](https://digital-strategy.ec.europa.eu/en/faqs/ai-continent-action-plan-qa)
- 这些安排证明国家回流也可以扩展替代能力；其实际开放程度、长期治理和使用分布仍需未来数据。

---

## 4. AI 进入 AI 研发的当前层级

### 4.1 已经发生的层级

| 研发层级 | 证据状态 | 事实 |
|---|---|---|
| 代码、调试、数据与实验辅助 | **已观察** | Anthropic 对 20 万条内部 Claude Code 记录的分析称，pre-training 团队 54.6% 的使用是构建新功能，常用于运行更多实验；研究还包含 132 名工程师/研究者调查和 53 次访谈。[Anthropic internal study](https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic) |
| 有明确目标函数和自动评估器的优化 | **已观察** | Google DeepMind 报告 AlphaEvolve 改进数据中心调度、AI accelerator 电路和 Gemini 训练内核；公开技术材料称内核平均加速 23%，使 Gemini 总训练时间下降约 1%。[DeepMind announcement](https://deepmind.google/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/)；[AlphaEvolve paper](https://arxiv.org/abs/2506.13131) |
| 数小时机器学习 research engineering | **混合结果** | RE-Bench 有 7 个开放式 ML 工程环境、61 名人类专家共 71 次八小时尝试。最佳 agent 在两小时预算下得分约为人类四倍；八小时下人类略胜，合计 32 小时下人类约为 agent 两倍。[RE-Bench](https://arxiv.org/abs/2411.15114) |
| 真实世界、长期、含糊目标的完整 AI 研发 | **未证明** | 2026 International AI Safety Report 判断现有 AI-assisted research automation 证据混合；真实 AI R&D 还有目标含糊、大实验反馈慢、是否改进模型需较长时间才能确认等瓶颈。[International AI Safety Report 2026](https://internationalaisafetyreport.org/publication/international-ai-safety-report-2026) |
| 无人端到端生产更强后继模型 | **未证明** | 没有权威公开证据表明当前系统能独立选择研究方向、获得训练资源、完成前沿训练、验证改进、部署后继模型并持续重复该循环。 |

### 4.2 时间压缩：能说到哪里

- **[已观察，基准指标]** 2026 International AI Safety Report 汇总 METR 结果：当前系统在约 80% 成功率下可完成相当于人类专家约 30 分钟的软件工程任务，该 task-length 指标过去六年约每七个月翻倍；但任务越长，性能越差，基准缺少资源约束、不完整信息和多主体协调等真实工作特征。[International AI Safety Report 2026, lines on task horizons](https://internationalaisafetyreport.org/publication/international-ai-safety-report-2026)
- **[已观察／反向观察]** 在一项随机对照试验中，16 名熟悉自己大型开源仓库的资深开发者完成 246 项任务时，使用 2025 年初 AI 工具反而平均慢 19%。[METR randomized trial](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)
  - 该小样本结果不能外推全部开发工作；它直接否定“任何 AI 编码使用都必然缩短周期”。
- **[合理推断]** 编码、实验生成、内核优化和评测这些子循环已能被压缩；若其结果被真实采用，它们可加快下一轮研发。
- **[未证明]** 基准 task horizon 的指数趋势不是前沿实验室整体研发周期的直接测量，也不证明能力增长已经形成自维持的递归加速。
- **[未证明]** 2026 International AI Safety Report 明确称，对“AI 自动化自身 R&D”反馈环的实证理解仍然很少，人类监督需求和大规模实验的慢反馈都不清楚。[International AI Safety Report 2026](https://internationalaisafetyreport.org/publication/international-ai-safety-report-2026)

### 4.3 来源限度

- Anthropic 与 DeepMind 材料是开发者对内部使用和结果的披露；它们是已发生案例，但缺乏独立审计和完整反事实。
- RE-Bench 可复现且有人类对照，但任务数少，评价的是受限环境中的 research engineering，不是完整科学共同体或前沿实验室。
- **[未证明]** “AI 已经在生产 AI”只能在“参与代码、实验、优化、评测和训练工程”这一窄义下成立；不能写成“AI 已自主生产后继 AI”。

---

## 5. 依赖、切换成本、独立评估与替代能力

### 5.1 合同、技术与云依赖

- **[已观察]** FTC 调查发现云—模型伙伴关系可能通过排他/控制权、云消费承诺、技术集成和敏感信息共享提高合同及技术切换成本，限制开发商改换云商或同时使用多个云商。[FTC staff report](https://search.ftc.gov/news-events/news/press-releases/2025/01/ftc-issues-staff-report-ai-partnerships-investments-study)
  - “可能提高”是 FTC 对已见合同结构的竞争风险判断；报告没有量化每一伙伴的实际迁移成本。
- **[已观察，邻近基础设施证据]** CMA 2025 cloud market final decision 认定 AWS 与 Microsoft 在英国有 significant market power，技术壁垒和 egress fees 限制 switching 与 multi-cloud；迁移还涉及技能、延迟、透明度、业务中断和机会成本。[CMA final decision report](https://assets.publishing.service.gov.uk/media/688b8891fdde2b8f73469544/final_decision_report_31.7.25.pdf)
  - 这是广义云基础设施证据，不是所有 AI 模型/API 客户的专门迁移研究。
- **[反向观察]** 同一 CMA 调查认为 committed-spend discounts 按当时实施方式并未构成竞争损害；不同障碍的影响依客户数据量、架构和业务需求而异。[CMA provisional findings summary](https://www.gov.uk/government/news/cma-independent-inquiry-group-publishes-provisional-findings-in-cloud-services-market-investigation)

### 5.2 独立评估的能力与依赖

- **[已观察]** AI Index 记录：几乎所有领先开发商报告能力基准，但 responsible-AI benchmark 报告仍稀疏；Foundation Model Transparency Index 平均分由 2024 年 58 降至 2025 年 40，训练数据、算力和部署后影响披露尤其不足。[Stanford HAI：Responsible AI](https://hai.stanford.edu/ai-index/2026-ai-index-report/responsible-ai)
- **[权威综合判断]** 2026 International AI Safety Report 认为开发商掌握训练数据、内部安全问题和内部评测等外部主体缺少的信息，商业考虑使大量信息保持 proprietary；有限的真实交互数据也阻碍独立评估长期影响。[International AI Safety Report 2026](https://internationalaisafetyreport.org/publication/international-ai-safety-report-2026)
- **[已观察]** 英国 AISI 自 2023 年起评测 30 多个 frontier systems；其公开趋势报告说明，评测通常获得 API checkpoint access，有时早于公开发布，但经常没有 fine-tuning API、没有最大化 inference compute，也只公开聚合结果而不标模型/公司。[AISI Frontier AI Trends Report](https://www.aisi.gov.uk/frontier-ai-trends-report)
  - 这同时证明两件事：独立政府评测真实存在；其上限仍部分依赖开发者提供何种访问。
- **[已观察／反向观察]** AISI 已开源 Inspect 与大量 evaluations；METR 公开任务、代码和 agent trajectories，并声明不接受公司补偿。[AISI Inspect Evals](https://www.aisi.gov.uk/blog/inspect-evals)；[METR research and disclosure](https://metr.org/)

### 5.3 替代生产与退出并未消失

- **[已观察]** 开放模型、六家顶级开发商、中美能力接近、多云协议和公共 AI factories 都表明现实替代仍存在；不能把集中写成“只剩一个模型、一个国家或一个云”。来源见本 packet 第 1、2、3 节。
- **[权威综合判断]** 2026 International AI Safety Report 认为开放权重扩大了较少资源主体的研究和商业机会，使更多研究者可以测试、改造、在本地运行模型；同时开放权重更难召回、保护措施更易移除。[International AI Safety Report 2026, open-weight section](https://internationalaisafetyreport.org/publication/international-ai-safety-report-2026)
- **[合理推断]** 当前最可靠的诊断不是“已经无法退出”，而是：在最强训练、云迁移和闭源评测上，独立替代与纠正所需的资本、访问、技能和时间可能增长，并部分依赖被评估或被替代的公司。
- **[未证明]** 公开证据尚未量化“共同纠正比能力增长晚多少”；也没有证明所有客户、研究者、国家或组织的退出能力都在单向下降。

---

## 6. 已发生的反向反馈与约束

这些事实必须与正反馈同写；否则会把方向性诊断夸大成已完成的锁定。

| 反向反馈 | 已发生事实 | 不能据此证明什么 |
|---|---|---|
| 出口与安全管制改变芯片收入 | Nvidia 因 H20 出口限制确认 45 亿美元 excess inventory / purchase obligation charge，并曾预计下一季少约 80 亿美元收入；FY2026 10-K 仍保留该 45 亿损失。[Nvidia Q1 FY2026 results](https://investor.nvidia.com/news/press-release-details/2025/NVIDIA-Announces-Financial-Results-for-First-Quarter-Fiscal-2026/)；[FY2026 10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm) | 不证明出口管制降低全球总算力；它也可能刺激替代芯片和国内投资 |
| 竞争执法促成实际商业变化 | CMA 2026 年称 AWS 与 Microsoft 正采取 material steps 降低 egress fees、改善 interoperability；CMA 将继续检查 multi-home 和 switching。[CMA announcement](https://www.gov.uk/government/news/cma-announces-package-of-actions-on-business-software-and-cloud-services) | 不证明迁移壁垒已消失或措施长期有效 |
| 预部署评测改变发布方式 | 2026 International AI Safety Report 记录，多家开发商在 2025 年因不能排除模型帮助生物武器新手的可能性，而以额外 safeguards 发布模型。[International AI Safety Report 2026, key developments](https://internationalaisafetyreport.org/publication/international-ai-safety-report-2026) | 不证明 safeguards 足以消除风险，也不证明模型发布被停止 |
| 法律义务开始形成组织反馈 | 欧盟 GPAI obligations 自 2025-08-02 已适用；Amazon、Anthropic、Google、Microsoft、Mistral、OpenAI 等已签署 Code of Practice。委员会罚款执法权要到 **2026-08-02** 才开始，晚于本 packet 截止日。[European Commission：Code and signatories](https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai)；[enforcement timeline](https://digital-strategy.ec.europa.eu/en/faqs/guidelines-obligations-general-purpose-ai-providers) | 截至 2026-07-13 不能声称罚款执法已经产生效果；签署也不等于完全履行 |
| 电力、设备与审批形成物理瓶颈 | IEA 记录 2025 年数据中心用电增长 17%，AI-focused data centers 更快；变压器、燃气轮机、先进芯片与 IT 组件供应收紧，connection / approval 已被拖延。IEA 2025 模型估计约 20% 的 2030 前计划容量有 grid-delay 风险。[IEA 2026 update](https://www.iea.org/news/data-centre-electricity-use-surged-in-2025-even-with-tightening-bottlenecks-driving-a-scramble-for-solutions)；[IEA 2025 analysis](https://www.iea.org/reports/energy-and-ai/ai-and-energy-security) | 20% 是风险估计，不是 20% 已取消；瓶颈也会引发新的电网和能源投资 |
| 开放与多供应商路线提供替代 | 顶级开发商多于一家、开放模型差距仍有限、OpenAI 已跨 Azure/AWS/Oracle 扩张、DoD 采用 interoperable multi-vendor 架构 | 不证明替代成本低，也不证明开放模型能复现最昂贵的训练与部署栈 |
| 研发效果并非单向正增益 | RE-Bench 长任务中人类重新领先；METR 的资深开源开发者 RCT 测得 AI 组慢 19% | 不证明 AI 整体无生产率收益；证明“任何接入都自动加速”不成立 |

---

## 7. 三稿可共用的事实边界

### 可直接作为现在时事实

- 前沿模型生产、训练算力、先进芯片制造和大额私人投资高度集中，但仍有多家顶级组织、多个国家和开放替代。
- 收入、融资、估值与战略采购已经转成服务器、数据中心、云合同、研发、人力与分发；回流的合同和财务通道可被直接观察。
- 国家安全与技术主权已经成为资金、采购、出口限制和组织扩张的显性选择器。
- AI 已进入 AI 编码、实验、评测、训练工程、芯片与算法优化的多个环节。
- 云切换壁垒、伙伴合同耦合、闭源信息不对称和评测访问依赖真实存在。
- 出口管制、竞争执法、开放模型、独立评测、法律义务、收益压力和物理瓶颈也在产生真实反向反馈。

### 必须标成推断

- 上述环节合起来正在形成“胜出资源 → 更强后继生产 → 更高依赖 → 下一轮更难停”的正反馈。
- 商业与安全竞争缩短了组织愿意等待独立证据的时间。
- 独立评估、替代生产和退出相对前沿能力增长变得更晚、更贵。
- AI 对研发子循环的加速可能进一步压缩共同理解与纠正的时间。

这些推断有多项事实共同支持，但目前没有一个公开数据集直接测量完整链条或其净强度。

### 截至 2026-07-13 不得写成已证事实

- AI 已经自主、端到端生产更强的后继 AI，或已形成自维持的递归智能。
- 一个公司、国家、模型或吸引子已经完全控制全球 AI。
- 开放替代、独立研究、独立评估或多云退出已经消失。
- 每一笔 AI 收入、估值增长、国家预算或 capex 都会回到竞争性前沿训练。
- 已宣布的数千亿美元基础设施、国家基金或合同 ceiling 已全部支付、建成或投入使用。
- 反向反馈不存在；或相反，现有安全框架、监管、开放模型与市场竞争已经足以抵消正反馈。
- 当前证据能够给出递归失控、锁定、坍塌或灭绝终局的概率。

## 最短事实链

1. **[已观察]** 少数产业组织掌握大部分 notable model production，算力、先进制造、云和大额资本也高度集中。
2. **[已观察]** 融资、云收入、芯片收入和战略采购已经转成更多算力、基础设施、研发、人才与分发；部分伙伴合同把投资直接回购为云消费。
3. **[已观察]** AI 已在下一轮 AI 的代码、实验、优化、评测和训练工程中工作。
4. **[已观察]** 云迁移、闭源访问和信息不对称使独立切换与评估存在成本；开放模型、多云与公共/独立评测仍构成现实反力。
5. **[合理推断]** 因而已有条件形成“资源回流 + 研发子循环加速 + 依赖增加”的正反馈，但其完整速度、净强度和未来终局均未被直接证明。
