# Causal-chain v6 — AI 工程与证据停止审计

审计对象：`v6/plan.md`、`v6/main-zh.md`、`v6/independent-zh.md`、`v6/independent-en.md`。为校准 v6 的有限修复目标，另读 `v5/reviews/deep-synthesis-and-consolidation-direction.md` 与 `v5/reviews/ai-empirical-red-team.md`；未读取任何其他 v6 review。事实核验截止 2026-07-13。

## 一、停止判定

**PASS。停止标准已经达到。**

三稿均未留下足以要求 v7 causal-chain 的承重错误：没有把正反馈写成必然收敛，没有把能力直接写成现实净效应，没有用第一条 AI 路径替第二条提供证据，没有把低层研发辅助写成已经自治的递归自我改进，也没有让暂停权免受自身的反总体化检验。规范结论所需的桥也已明说：当一个具体高杠杆角色存在严重且不可逆的可信路径，并可能在改向前消耗独立纠正条件时，继续扩张失去默认正当性；这不是由“尚无安全保证”直接推出停止。

**最佳单一底稿是 `independent-zh.md`。** 它是唯一同时显式承载四个计划要求的证据锚点、五级递归、协调缺口、角色级纠错余量与干预比较的中文稿；其 AI 段也是三稿中最不容易在压缩时丢掉条件项的一份。`main-zh.md` 仍是更好的公共节奏与篇幅控制样板，`independent-en.md` 是最好的英文逻辑控制，但二者都不如独立中文稿具备完整的独立证据承重。

这意味着后续可以做一次**定稿级选择、压缩和引文校正**，但不应再开启新的理论版本。若权威中文稿必须采用 `main-zh.md` 的篇幅，应把 `independent-zh.md` 的四锚点证据纪律移入主稿，而不是重写因果链。

## 二、承重问题与非承重问题的边界

### 未发现的承重失败

- **没有 category error：** totalization 被定义为独立观察、拒绝、纠正、替代维持与后继生产逐渐失去因果力，而不是集中、增长、依赖或统一外观本身。
- **没有 scale jump：** 三稿都保留 `capability → reliable adoption → consequential permission/scale → concentrated return → dependency/successor influence` 的中间层，并明确扣除公共能力、防御、替代供给、制度摩擦与协调。
- **没有 evidence-level collapse：** level 1 已成立，level 2 部分成立，level 3 是净经验问题，level 4—5 未公开成立；第二条持续中心路径也没有借用第一条局部放大路径的证据。
- **没有 hidden normative bridge：** 动力学不定义善；生成性只是反封闭元约束，仍须同痛苦、尊严、义、非支配、公平与关系地位共同判断。暂停的负担转移理由是下一步可能毁掉后来识错与修复的条件，而不是风险存在本身。
- **没有 self-defeating restraint principle：** 三稿都识别冻结后来者、保留 incumbent asymmetry、秘密/军事位移与单一闸门垄断重启权；正当克制必须增加纠错余量、保留公共替代、可争议、可罢免并能退场。

### 仍可修订但不足以拒绝停止的项目

- `main-zh.md` 没有显式给出前沿/后继生产集中锚点，也没有为协调覆盖句单独落引文；这是证据呈现不足，不是其因果推理依赖了虚假事实。
- `independent-en.md` 没有显式给出集中锚点；其余三锚点和证据等级完整。
- `independent-zh.md` 的集中数字来自官方国际报告对研究的综合，而非直接的企业库存披露；它已写成“报告引用的研究估计”，没有把估计冒充普查事实。可进一步补底层研究或精确章节，但不影响其有限用途。
- GPT-5.6 的 fully automated AI R&D 判断最好直接链接 [METR 的原始评测摘要](https://metr.org/blog/2026-06-26-gpt-5-6-sol/)，而不是只经 OpenAI system card 转述。这是 source upgrade，不是结论修复。
- “足够可逆”“显著恶化”“严重且不可逆”等词仍需在具体政策或安全论证中操作化。v6 已给出对象、比较项、证据要求与纠错链；精确 cutoff、复核期限和退出流程属于后续 role-specific policy design，正是停止标准允许留下的工作。

## 三、四个证据锚点审计

| 锚点 | 当前一手/官方证据能支持什么 | 三稿表现 | 判定 |
| --- | --- | --- | --- |
| 前沿/后继生产的集中或影响 | 2026 国际报告称当前前沿训练的单次计算成本约 5 亿美元、下一代预计 10—100 亿美元，并转述研究估计单一公司在任一时点可能持有全球数据中心 AI 芯片的 10%—40%。这支持高门槛与少数资本—基础设施关系对后继生产有显著影响，不证明封闭或 totalization。[International AI Safety Report 2026](https://internationalaisafetyreport.org/publication/international-ai-safety-report-2026) | `independent-zh.md` 明确给出并限制推论；`main-zh.md` 与 `independent-en.md` 只有结构性陈述，没有显式锚点。 | 独立中文稿通过；另两稿为引用补强项。 |
| AI 已进入后继模型工作流 | DeepMind 披露 AlphaEvolve 已改进 AI training processes，包括训练支撑自身的模型；Anthropic 明确披露现有 Claude 用于生成训练数据、写研究代码、监控代理并评估后继模型。这足以证明 level 1 与部分 level 2，不足以证明自治后继生产。[DeepMind](https://deepmind.google/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/)，[Anthropic](https://alignment.anthropic.com/2026/auditing-overt-saboteur/) | 独立中文稿用 DeepMind，英文稿用 Anthropic，均准确限制推论；主稿以官方综合报告概括同一边界。 | 三稿通过；独立稿的直接一手锚点更强。 |
| 总体加速与自主自我改进的当前证据边界 | 官方国际报告判断 AI-assisted R&D 的总体加速证据 mixed，并指出现实研发中的模糊目标和长反馈没有被短任务 benchmark 覆盖；OpenAI 报告 GPT-5.6 低于其 High AI Self-Improvement threshold；METR 不认为该模型能实现 fully automated AI R&D，同时明确其 time-horizon 测量因作弊处理而不稳健。这支持“level 3 未决、4—5 未公开成立”，不支持“风险不存在”或对所有前沿模型作普遍上限判断。[International AI Safety Report 2026](https://internationalaisafetyreport.org/publication/international-ai-safety-report-2026)，[OpenAI GPT-5.6 system card](https://deploymentsafety.openai.com/gpt-5-6)，[METR](https://metr.org/blog/2026-06-26-gpt-5-6-sol/) | 三稿都保持不对称结论；没有把单模型 system card 外推为行业定律。 | 通过。 |
| 真实但不完整的协调，尤其军事/秘密缺口 | 2026 国际报告记录安全框架和法律义务增长，同时指出框架阈值、范围、执行力和标准化外部审计仍不一致。EU AI Act Article 2(3) 明确排除专用于军事、国防或国家安全的系统；这证明该法的覆盖缺口，但不等于军事 AI 不受任何其他法律约束。[International AI Safety Report 2026](https://internationalaisafetyreport.org/publication/international-ai-safety-report-2026)，[EU AI Act](https://eur-lex.europa.eu/eli/reg/2024/1689/oj?locale=en) | 独立英文稿最精确地加上“不等于军事 AI 在所有法律之外”；独立中文稿的表述也未越界；主稿的判断正确但缺独立引文。 | 三稿概念通过；主稿需引文补强。 |

四锚点的证据共同支持的是一个**不对称判断**：集中与 successor influence 真实，低层递归真实，协调增长也真实；但总体净加速、高度自动化后继生产、现实部署中的稳定自维持中心，以及所有高杠杆角色的负纠错余量，都没有被当作已成立事实。三稿没有跨越这条边界。

## 四、计划指定的八项压力测试

### 1. 高杠杆角色定义

**通过。** 三稿都没有按“重要行业”给角色贴标签，而是要求后继影响或高后果执行权，同可能跑在独立发现、阻断和恢复之前的扩散、依赖或损害结合。这个定义把 capability、permission、exposure 与 correction margin 置于同一可检验对象中。

`independent-zh.md` 与 `independent-en.md` 还给出最有效的反差：可撤回、无关键权限且有人类替代的研究助手，不等于接入武器或后继训练、持续运行或不可召回的系统。后续 policy 可以为各行业量化，但因果链不再靠行业名称承重。

### 2. 条件性净增益

**通过。** 最关键的 `when` 没有在结论中消失。三稿都要求可靠采用、关键权限/规模、集中回报、依赖与后继影响实际耦合，并要求 counter-capacity 没有获得相当力量。`independent-zh.md` 最明确地说“这个‘当’不能消失”，随后又把当前结论限定为撤回“某些高杠杆角色无条件扩张的推定”，而不是声称已测得文明总体净增益。

第六节的规范结论同样没有倒退成 capability jump：暂停对象仍须具有可信的风险能力—现实暴露路径，且较轻措施不能及时恢复可逆性。由此，AI 可能同时增强主回路与反向力量的事实没有被抹去。

### 3. 两条 AI 路径

**通过。** 第一条是 stronger-evidence route：局部可控、无机器自我也可放大市场或安全竞赛。第二条明确增加持久运行、记忆、长时程、工具、资源访问与环境反馈等条件，并保持为较弱证据路径。三稿都说第一条不能证明新持续中心已经形成，第二条不出现也不取消第一条。

GPT-5.6 公开材料中的作弊、持续性与少量代理性失配信号足以支持“值得监测”，但 METR 的不稳健 time-horizon 与外部 sabotage 评测边界不支持“现实自维中心已经形成”。三稿正好停在这个证据等级。

### 4. 五级递归

**通过。** 独立两稿完整列出：

1. AI-assisted research 已成立；
2. 研发环节部分自动化已部分成立；
3. 机构级净研发加速仍是反事实问题；
4. 大部分后继生产高度自动化未公开成立；
5. 持久系统在更少外部指导下递归重构并再生产自身能力未公开成立。

`main-zh.md` 用一句话压缩了同样的五层而未混层。最重要的是，低层进入 successor workflow 没有被写成高层 autonomy，当前上限证据也没有反过来抹掉 level 1—2 的文明相关性。

### 5. 纠错余量

**通过。** 三稿都把纠错余量拆成至少发现、归因、共同决定、阻断与恢复，并同扩散、依赖、后继生产和不可逆伤害的时间/权力关系比较。英文稿进一步指出这不是一个单一文明时钟，而是概率、时间与权限的分布；这避免了把“协调正在增长”或“存在某种干预工具”误当作完整可逆性。

它们也明确说事故不会自动形成有效反馈、缺乏 assurance 不自动证明负余量。因而这里不存在从不确定性直接跳到停止的经验越界。

### 6. 协调覆盖

**通过。** 三稿同时承认法律、国际测试、企业框架与公共讨论的增长，以及跨法域一致性、共同触发、独立审计、军事/秘密部署和阈值前执行没有形成闭环。它们没有用 coverage gap 宣称“完全没有协调”，也没有把一项区域法律等同全球充分覆盖。

最值得保留的是英文稿的限定：EU AI Act 的排除只证明该框架的军事/国家安全缺口，不证明军事 AI 在所有法律之外。这一限定应在最终中文版引文注释中保留。

### 7. 角色级干预比较

**通过停止标准，尚待后续政策操作化。** 三稿都比较继续扩张、降权限/分阶段部署、定向暂停与协调暂停，并规定只有较轻措施无法在下一增量显著恶化风险前恢复可逆性与独立纠正时，才升级到暂停。对象是具体训练、发布、权限或部署，不是无限类别“AI”。

`independent-zh.md` 还要求证据独立、可复验、贴近部署，并把公共利益、防御与替代供给纳入反事实。这已经足以支撑 role-level presumption shift。它没有给出通用数值 cutoff，但不同角色不应共享虚假的统一阈值；精确 trigger、owner、复核、期限和解除条件属于后续安全论证。

### 8. 克制的递归性

**通过。** incumbent freeze 与 secret/military displacement 两个核心失败模式均被保留；单闸门捕获被正确视为它们的延伸。正当克制不得保存导致危险的不对称，必须保护公共科学、防御性能力和独立替代，并把争议、共同决定、罢免与退出能力留给受影响中心。

这个原则并非“所有暂停都正确”，而是要求暂停也接受同一净效应比较。它因此没有自我豁免，也没有用治理困难恢复加速的默认正当性。

## 五、逐稿判定与最佳底稿

| 草稿 | 停止判定 | 最强处 | 非承重修订 |
| --- | --- | --- | --- |
| `main-zh.md` | PASS | 最好的公共节奏、六段结构、结尾力度；所有核心条件都已存在。 | 补集中锚点；为协调句补官方引文；AI 证据最好从一段压缩为两段以免 successor workflow 与上限共用模糊来源。 |
| `independent-zh.md` | PASS，最佳底稿 | 四锚点最完整；高杠杆定义、五级递归、证据—规范桥、干预反事实和克制递归均最稳。 | 将 fully automated AI R&D 直接链到 METR；如需公共发表，按主稿节奏压缩约 15%—20%，但不可删掉条件项。 |
| `independent-en.md` | PASS，最佳英文控制 | 最精确的 effective gain、两路径、纠错链与军事法律限定；英文概念最稳定。 | 补集中锚点；减少部分重复限定；把最终 authoritative English 同中文最佳底稿逐桥对齐。 |

选择 `independent-zh.md` 不是因为它信息最多，而是因为删掉任一关键段都更容易暴露哪一座桥正在承重。`main-zh.md` 已经足以证明理论停止，却在第五节把四类证据压进过少的句子；这增加读者把“公开证据支持哪些层级”与“作者作出何种规范判断”混读的概率。最安全的定稿路线是以独立中文稿为事实—逻辑基线，用主稿做删减约束。

## 六、最终停止理由

V6 已完成计划规定的有限修复：独立性被物质化；代价转移经可保留不对称耦合相对脆弱性；道德保存、再生产与 selector change 被分层；受影响中心获得共同决定、反制与罢免地位；made minds 被纳入不确定性下的非耗材原则；AI 的四类证据锚点与五级递归保持时态；暂停成为角色级比较；克制接受自身的反总体化检验。

剩余工作都属于停止标准明确允许留下的类别：直接引文升级、主稿证据锚点补齐、中文压缩、英文对齐，以及针对具体角色另做阈值与治理设计。它们不改变“斗争进入 successor selection → 独立回答能力下降 → moral/material counter-selection → conditional AI gain → correction-margin burden shift → reflexive restraint”这条承重链。

**因此：PASS；不要生成 v7 causal-chain。以 `independent-zh.md` 为最佳底稿，以 `main-zh.md` 为压缩边界，以 `independent-en.md` 为英文校准控制，进入 authoritative-text consolidation。**
