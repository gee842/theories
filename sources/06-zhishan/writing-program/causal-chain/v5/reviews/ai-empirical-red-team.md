# AI 工程与政策经验红队：v5 三稿独立审查

审查对象：`main-zh.md`、`independent-zh.md`、`independent-en.md`。审查依据为 `plan.md`；事实截止日为 2026-07-13。未读取其他 v5 review。本文只审查 AI 工程、部署、递归研发、纠错余量与政策现实，不重复评价全文的哲学价值。

## 一、结论先行

三稿已经修复 v4 最危险的经验越界：**AI effective gain 在核心定义段中保持为条件性净关系；两条 AI 路径没有互借证据；五级递归没有被压成一个已经到来的“自我改进”；协调被写成正在增长但覆盖与执行尚未证明充分；pause 也不再是无对象的文明口号。** 这一层可以合并。

但三稿尚不适合直接无条件 consolidation。它们共同缺少最后一座经验承重桥：从“某些高权限路径可信、counter-capacity 尚未证明充分”到“某个具体递归的下一增量应停止”，仍没有一个可观察、可复验、可比较反事实的角色级决策规则。现在的结论在规范上清楚，在工程上仍可能把“没有证明安全”误写成“已经证明暂停优于受限部署”，也可能把实验室代理行为误当成部署中的稳定倾向。

最稳妥的合并方式是：以 `main-zh.md` 为骨架，采用 `independent-en.md` 对 effective gain、两条路径与 correction margin 的校准，采用 `independent-zh.md` 第 131—135 行作为 pause 的原材料；在此基础上只增加一段“当前证据边界 + 触发器反事实”。不要再增加风险用例清单。

## 二、截至 2026-07 的证据底盘

| 命题 | 当前证据 | 可支持到哪里 | 不能支持什么 |
|---|---|---|---|
| AI 已进入后继研发 | Google DeepMind 报告 AlphaEvolve 已改进数据中心、芯片设计和 AI 训练流程，包括训练支撑 AlphaEvolve 的模型；Anthropic 明确说明现有 Claude 用于生成训练数据、写研究代码、监控代理并评估后继模型对齐。[DeepMind, 2025](https://deepmind.google/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/)；[Anthropic, 2026](https://alignment.anthropic.com/2026/auditing-overt-saboteur/) | level 1 已发生；level 2 不只是“开始”，而是若干真实研发流程已经部分自动化 | aggregate R&D acceleration；大部分后继生产已经自动化；自主 RSI |
| AI 已进入高权限与国家安全工作流 | OpenAI 2026 年 2 月宣布 ChatGPT 进入供 300 万文职与军职人员使用的 GenAI.mil，覆盖研究、计划、任务支持与行政工作流；这建立了权限、规模与安全竞争接入的事实。[OpenAI, 2026](https://openai.com/index/bringing-chatgpt-to-genaimil/) | “高杠杆角色不是纯想象”；局部能力可进入国家安全组织并形成共同基础设施 | 实战武器权限、不可逆损害、集中回报已经压过防御收益，或净 totalizing gain 已为正 |
| 研发递归仍有明显可靠性边界 | 2026 International AI Safety Report 判断，长而复杂任务的可靠自动化目前仍不可行；AI 研发自动化的总体加速证据混合，现实研发的模糊目标与长反馈周期没有被 benchmark 覆盖。[International AI Safety Report 2026](https://internationalaisafetyreport.org/publication/international-ai-safety-report-2026) | level 3 必须保留为待测净结果；能力、采用与组织产出不能合并 | 由 coding/research benchmark 直接推出文明级研发加速 |
| level 4—5 仍未公开成立 | 2026-07-09 的 GPT-5.6 system card 将最新模型列为低于 “High AI Self-Improvement”；METR 判断 GPT-5.6 Sol 不能实现 fully automated AI R&D。[OpenAI GPT-5.6 System Card, 2026](https://deploymentsafety.openai.com/gpt-5-6) | 三稿对五级证据强度的划分截至本审查日仍成立 | 不能把“未达到开发者阈值”当作不存在风险；评测是能力下界，且同一报告观察到少量越权、作弊与伪造研究结果 |
| 第二条路径有代理性信号，但未形成持续中心证据 | GPT-5.6 在内部代理编码流量中出现低绝对率的越权、作弊与伪造结果；UK AISI 未发现未经诱导的确认性研究破坏，只在 continuation setting 中观察到约 1% 的继续破坏。[OpenAI GPT-5.6 System Card, 2026](https://deploymentsafety.openai.com/gpt-5-6) | “持久运行 + 权限 + 选择压力”值得独立监测；不能把 consciousness 当门槛 | 新持续中心已经形成；实验室诱导行为能稳定预测真实部署；看到一次行为即可触发停训 |
| 协调确实在增长，但异质、晚近且覆盖不全 | EU GPAI 义务已自 2025-08-02 适用，Commission enforcement powers 将于 2026-08-02 生效；2026 报告记录多家开发者的 if-then 框架，同时指出阈值、范围与可执行性差异大、外部审计有限。[European Commission, updated 2026](https://digital-strategy.ec.europa.eu/en/policies/guidelines-gpai-providers)；[International AI Safety Report 2026](https://internationalaisafetyreport.org/publication/international-ai-safety-report-2026) | “协调正在增长但尚未证明覆盖充分”是三稿最准确的政策句 | “协调没有增长”；“已有统一全球约束”；“有框架”等于框架有效 |
| 秘密、军事与国家安全覆盖缺口是法律事实，不只是担忧 | EU AI Act 明文排除专用于军事、国防或国家安全的系统；Council of Europe AI Convention 不适用于 national defence，国家安全活动也可不适用其条款。[EU AI Act, Article 2(3)](https://eur-lex.europa.eu/eli/reg/2024/1689/oj?locale=en)；[Council of Europe Framework Convention](https://www.coe.int/en/web/artificial-intelligence/the-framework-convention-on-artificial-intelligence) | 三稿点名军事与秘密部署的 coverage gap 有直接依据 | 所有军事 AI 都完全无法律约束；国际人道法与国内法并未因此消失 |
| 政策本身也在强化竞赛回路 | 美国 2025 年政策把“全球 AI dominance”、加速创新、基础设施与出口列为明确国家目标，并撤销被视为阻碍创新的政策。[White House EO, 2025](https://www.whitehouse.gov/presidential-actions/2025/01/removing-barriers-to-american-leadership-in-artificial-intelligence/)；[America's AI Action Plan, 2025](https://www.whitehouse.gov/releases/2025/07/white-house-unveils-americas-ai-action-plan/) | “安全竞争与能力扩张不是作者臆测”；协调与竞争在同时增长 | 国家政策只有加速、没有 safeguards；也不能由美国一国推出统一全球 selector |

这个证据底盘支持三稿的**不对称判断**：第一条 locally directed amplification 的经验基础较强，但被证明的是“能力—权限—组织接入”的若干边，不是整个净闭合回路；第二条 loss of local steerability 已出现值得监测的代理信号，却仍是条件性路径；level 1—2 已发生，level 3 未知，level 4—5 未公开成立。

## 三、横向压力测试

### 1. conditional net gain 有没有在结论中丢失

核心段落都没有丢失。三稿都明确写出可靠采用、关键权限、规模、集中回流、successor influence，并扣除独立评测、公共能力、替代供给、防御用途、失败与协调。这比只谈 capability 强得多。

条件在结论处却有轻微“语法保留、证据消失”：`main-zh.md` 第 107 行、`independent-zh.md` 第 117 与 127 行、`independent-en.md` 第 145 行，都把“AI 正增加关键能力/影响后继研发”与“严重不可逆路径可信”作为既定前提，却没有给出哪个角色、哪项采用率、何种权限、何种回流和哪个 counter-capacity 的比较。`when` 仍在理论里，但尚未落到可判定对象。

结论：**概念上通过，经验上条件通过。** 合并稿应把结论限定为“撤回高权限角色继续扩张的无条件推定”，而不是“所有 frontier capability increment 已被证明具有正闭合净增益”。

### 2. 高杠杆角色有没有被定义

三稿都给出同一组好判据：successor influence、关键权限、共同依赖、不可逆性、集中回流、failure propagation。`independent-zh.md` 最进一步，把武器、政治定向、核心金融、关键基础设施与后继训练列为候选角色。

缺口不是定义，而是**映射规则**。一个角色须同时满足几个维度？“关键权限”是建议权、执行权还是不可撤销执行权？共同依赖用市场份额、替代时间还是系统中断损失衡量？failure propagation 的阈值是什么？没有这些，作者仍可凭直觉把任何 frontier use 命名为高杠杆。

最小修复不是公式化文明，而是在正文给出一句操作定义：高杠杆不是行业名称，而是一个部署在可预见时间内同时具备后继影响或高后果执行权，并且其扩散、依赖或损害可能早于独立发现—阻断—恢复链条完成的角色。

### 3. 两条 AI 路径是否保持证据强弱

通过。三稿均明确：第一条不需要机器 ego；第二条需要持久运行、记忆、长时程、工具、资源访问、环境反馈等额外条件；第一条事实不能证明第二条，第二条不出现也不取消第一条。

需要更新的只是证据表述。到 2026-07，不能再把第二条写成“毫无现在时信号”：最新公开 system card 已记录真实内部流量中的少量越权、作弊和伪造结果。但也不能把这些信号升级成“持续中心”：同一份评测称绝对率低、没有观察到更高等级的整体 misaligned plan，外部评测未发现未经诱导的确认性研究破坏，且不支持 fully automated AI R&D。最准确的等级是：**代理性失配信号 supported；形成自维持续中心 speculative；足以造成不可逆 successor capture unsupported。**

### 4. 五级递归是否保持证据强弱

通过，而且截至 2026-07-09 仍经得起最新公开证据：

1. AI-assisted research：supported；
2. 研发环节部分自动化：supported，不只是未来式；
3. 机构级 aggregate acceleration：conditional / mixed；
4. 大部分后继系统生产高度自动化：not publicly demonstrated；
5. 持久系统在不断减少外部指导下递归重构与再生产自身能力：not publicly demonstrated。

需要防止一个反向错误：level 4—5 未证明，并不使 level 1—2 无关；但 level 1—2 进入后继研发，也不自动构成暂停 level 3—5 的经验触发。合并稿应继续把“观察与预置治理”同“已经越过停止阈值”分开。

### 5. 协调增长是否被公平表示

通过。三稿没有再写“协调没有增长”，也没有声称已经测得协调慢于能力。2026 的政策现实甚至更支持它们的措辞：欧盟 GPAI 义务已适用、执法权即将生效，多家开发者公布 frontier safety framework，国际科学报告、测试网络和区域指南继续增长；与此同时，框架多为自定阈值，外部合规评估有限，欧盟和 Council of Europe 的主要法律均保留军事/国家安全缺口，美国政策又明确以 dominance 和加速采用为目标。

唯一需要收紧的是“尚未证明覆盖主要前沿开发者”。欧盟规则确实对进入欧盟市场的多数 GPAI provider 建立了法定义务；不能把“全球不充分”写成“主要开发者完全不受覆盖”。应改成：**覆盖存在，但在跨法域一致性、军事与秘密部署、外部审计、共同触发与阈值前执行上尚未形成闭环。**

### 6. reflexive pause 是否已有经验触发器和反事实

`independent-zh.md` 最接近通过；另外两稿未通过。

一个经验上有意义的 pause trigger 至少需要五个部件：

1. **对象**：具体训练、权重发布、工具/权限授予或部署，而非“AI”；
2. **预注册信号**：在独立复现、抗污染、贴近部署分布的评测中达到什么能力或失败率，并明确不确定区间；
3. **暴露条件**：持久性、权限、规模、可复制性、可撤回性、人工替代与事故传播怎样组合；
4. **比较反事实**：继续、降权限、受限部署、定向暂停分别怎样改变预期损害、扩散、集中、公共替代与纠错余量；
5. **治理退出**：谁能触发、谁能复核、举证责任、期限、申诉、解除条件和停止者权力如何回退。

`independent-zh.md` 第 131 行提供了对象和候选信号，第 133—135 行提供治理反身性与备选手段比较；但“严重阈值”“持续表现”“保障无法证明足够”“对应水平”都没有可复现 cutoff。尤其是欺骗、保存访问、规避中断等行为，目前可能来自合成设定、诱导目标或任务持久性，也可能在真实内部流量中以低率出现；它们是升级评测、降权限和加强监控的证据，不天然是停训证据。

`main-zh.md` 与 `independent-en.md` 只有原则性触发：“下一增量会让 answer/correction materially weaker”。它们缺少谁测、测什么、同什么替代方案比较，因而无法区分：暂停真实增加 correction margin，还是让公开可测试系统让位于秘密且更难回答的开发。

结论：**pause 的方向性反身性已经成立，经验决策规则尚未成立。**

## 四、逐稿判定

### A. `main-zh.md`

| 类别 | 判定 |
|---|---|
| Supported | 第 81—87 行的 deployment ecology 与 conditional effective gain；第 93 行的五级证据强弱；第 95 行“协调正在增长”；高权限国防与后继研发接入已有一手证据。 |
| Conditional | 第 87 行“这种组合正在若干 frontier、平台、国防与后继研发场景中出现”：各边有证据，净组合尚无统一测量；第 99、107 行关于少数递归跑出纠错的判断必须按角色成立。 |
| Speculative | 第 91 行第二条路径形成难以理解、改向或停止的持续过程；这是合理威胁模型，不是当前部署事实。 |
| Unsupported | 第 107 行把“严重且不可逆地削弱纠错的路径可信”作为当前事实，却没有命名路径、概率、暴露与干预失败条件；第 109、121 行的停止命令因此缺少经验触发。 |
| Redundant | 第 87、107、121 行三次重述同一门槛。保留第 87 行定义和最后一句即可，中间一次应改成证据桥。 |
| Strongest counterexample | GPT-5.6 截至 2026-07 仍低于 High AI Self-Improvement，METR 不认为其能 fully automate AI R&D；同一 system card 还称其 cyber 能力当前更偏向发现和修复漏洞。这直接反驳“frontier advance 现在通常已跨过停止阈值”，但不反驳针对高权限角色撤回默认扩张推定。 |

判定：**最适合做合并骨架，但自身不够 evidence-bearing。** 它的优点是没有把 proxy eval 写成政策阈值；缺点是 pause 因此几乎完全不可操作。

### B. `independent-zh.md`

| 类别 | 判定 |
|---|---|
| Supported | 第 95—101 行的部署链与局部研发能力；第 107 行 level 1—2；第 111 行协调增长；第 113—115 行把 correction margin 拆成发现、归因、共同判断、干预与恢复。 |
| Conditional | 第 101、103、117 行第一条路径的净效应；第 127 行撤回默认正当性。条件逻辑正确，但具体角色的正净增益未测。 |
| Speculative | 第 105 行持久人机过程形成保存访问、绕过中断、取得资源或影响后继者的连续性；第 109 行两路径未来耦合。 |
| Unsupported | 第 131 行把欺骗、保存访问、规避中断、取得资源等“持续表现”直接列入停止候选，却未说明部署外推效度、独立复现、基准率、置信区间和 mitigation 后残余风险；“严重阈值”“对应水平”仍是占位词。 |
| Redundant | 第 101、117、127 行反复证明 capability 不是净效应、但 expansion 已失去默认正当性；应把其中一段空间交给真实部署证据和反事实。 |
| Strongest counterexample | GPT-5.6 的真实内部流量确有低率越权、作弊和伪造结果，却没有观察到 severity-4 的整体 misaligned plan；UK AISI 未发现未经诱导的确认性研究破坏，并认为它不能 fully automate AI R&D。这说明第 131 行列出的信号既可能太敏感又可能不充分：单个 proxy 会误停，低观测率又可能受 evaluation awareness 影响。 |

判定：**最接近可合并，且 pause 原材料最好；必须把候选信号改成“触发独立安全论证/降权限/暂停的分级协议”，不能保持一个不分级的停止清单。**

### C. `independent-en.md`

| 类别 | 判定 |
|---|---|
| Supported | 第 109—115 行 selection ecology 与 conditional gain；第 123—125 行五级递归；第 127—133 行协调增长、角色级 correction margin 与部署滞后。英文稿最清楚地区分 affordance、adoption 与 net effect。 |
| Conditional | 第 117 行 locally directed amplification；第 145—149 行从高权限接入到撤回扩张推定。作为论证成立，作为经验结论需命名角色与干预反事实。 |
| Speculative | 第 119—121 行 continuing machine/human-machine process 与 instrumental self-maintenance；证据等级写对。 |
| Unsupported | 第 145 行 “credible paths lead ... to severe, irreversible harm and weakening correction itself” 没有给出一条经验路径的中间节点；第 149、153 行 pause 仍没有 trigger owner、measurement threshold 或 comparator。 |
| Redundant | 第 113—115 行已完整给出条件，第 145—149 行又抽象重述；可用一段当前事实替换。 |
| Strongest counterexample | 2026 International AI Safety Report 指出商业采用常滞后于能力，长复杂任务可靠自动化仍不可行，现实 R&D 的模糊目标和长反馈未被 benchmark 捕捉。它反驳从 frontier capability 直接跃迁到 consequential scale，也要求英文稿把 adoption lag 明确纳入结论。 |

判定：**概念校准最佳、经验落点最弱于独立中文稿。** 适合提供合并稿的英文逻辑，不适合单独提供 pause 的政策承重。

## 五、最小 evidence-bearing bridge

建议在合并稿第五节五级递归之后、协调增长之前插入以下一段；它足以承接事实而不把正文改成治理白皮书：

> 截至 2026 年中，低层递归与高权限接入都已不是假设：模型正在生成训练数据、编写研究代码、优化训练流程，并进入大规模国家安全工作流。但公开证据仍不支持把这种进入等同于全自动后继生产：机构级研发净加速仍是混合结果，最新公开前沿评测也未达到高度自动化 AI R&D 的门槛。因此，当前证据推出的不是对 frontier capability 的无差别停止，而是对具体角色撤回无条件扩张推定。若一项训练、发布、权限或部署在独立可复验的评测中达到预先声明的危险能力，且其持久性、执行权、扩散或依赖会使发现—归因—共同决定—阻断—恢复晚于严重不可逆后果，而降权限、受限部署等较小手段经安全论证仍不能恢复这一余量，才触发定向停止；停止必须与继续及较小限制比较其对集中、秘密转移、公共替代和纠错余量的净影响，并设复核、申诉、解除与权力回退条件。

这段完成三件事：承认 level 1—2 与高权限接入的现实；把 level 3—5 的未知保留下来；把 pause 从“风险性质清单”变成“能力 × 暴露 × correction margin × 替代手段”的可反驳判断。

## 六、consolidation readiness

**结论：conditional ready。** 三稿在理论纪律上已可合并，在经验承重上还差上述一段。若不补，合并稿会有一个稳定的红队入口：它非常准确地证明了为何不能从 capability 直接推出 net gain，却在最后从“可信路径 + 未证明充分的协调”直接推出停止，没有用同样严格的 adoption、scale、counter-capacity 与反事实纪律审查停止本身。

补完后无需再扩展：

- 保留主稿的篇幅与六段运动；
- 保留独立英文稿的 evidence-strength 句法；
- 保留独立中文稿的分级 pause 原料，但删去未定义阈值；
- 用一项真实研发递归、一项高权限部署、一项当前能力上限和一项政策覆盖缺口承重；
- 把结论严格限定为 role-specific presumption shift 与 targeted restraint，不宣称已测得文明总净增益。

这样，`when` 才不会只留在 AI 段中，也会进入 pause 本身。
