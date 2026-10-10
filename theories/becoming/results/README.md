# 理论成果与论证目录 / Results and argument catalogue

更新 / Updated: 2026-10-08 · [仓库首页](../../../README.md) · [研究进度与下一步](ROADMAP.md) · [完整研究记录](../../../RESEARCH.md)

**从这里查：一个论证说了什么、为什么重要、中文与英文怎样对应、Lean 检查了哪一部分、还有什么需要研究。**

**Use this directory to find the argument, its significance, its Chinese and English formulations, its Lean correspondence and its remaining questions.**

## 阅读入口 / Reading routes

| 文档 / Document | 内容 / Contents |
|---|---|
| [成果登记表 / Canonical result register](RESULT-REGISTER.md) | 每项已迁移主张的单一记录：前提、证据、状态、依赖、反例与别名；阅读页自动生成。 / One editable record per migrated claim, with generated reading views. |
| [会话成果与证明复用 / Session outcomes and proof reuse](SESSION-RESULTS.md) | 会话到成果族、规范复用入口、重复证明判别及新增章节。 / Chats mapped to result families, canonical reuse targets, overlap decisions and additional chapters. |
| [全部理论分支 / Theory map](THEORY-MAP.md) | 17 个分支的中英论证、意义、状态和后续；含方法档案。 / Bilingual branch accounts, including the method archive. |
| [统一论证 A–L](ARGUMENTS-A-L.md) · [统一论证 M–Z](ARGUMENTS-M-Z.md) | 逐章中英阅读版：论证、意义、范围、下一问题、原文、Lean 与证据。 / Paired chapter readings with scope, questions, sources and evidence. |
| [Lean 模块](LEAN-INDEX.md) · [定理名称](LEAN-DECLARATIONS.md) | 按模块及声明名称定位源码；区分检查记录与当前源码。 / Find modules and named declarations; distinguish recorded checks from current sources. |
| [研究路线 / Roadmap](ROADMAP.md) | 已有结果、持续方向与建议的下一检验。 / Established results, ongoing directions and proposed tests. |
| [细项主张账本 / Claim register](../chapters/CLAIMS.md) | 原有细项主张、证据类别、反例与研究沿革。 / Existing detailed claims, evidence classes and counterexamples. |

## 按问题阅读 / Read by question

| 问题 / Question | 推荐起点 / Entry points |
|---|---|
| 已经建立了怎样的共同基础？ / What foundation has been established? | [生成根据](ARGUMENTS-A-L.md#generative-grounding) · [前提与范围](ARGUMENTS-A-L.md#foundation-premises) · [全篇理论](ARGUMENTS-M-Z.md#theory) |
| 组织怎样形成学习和修正能力？ / How do organization, learning and revision form? | [生成发展](ARGUMENTS-A-L.md#generative-development) · [学习路线修正](ARGUMENTS-A-L.md#learning-route-revision) · [评价接续](ARGUMENTS-A-L.md#evaluative-succession) |
| 生生为何有伦理意义？ / Why does generativity matter ethically? | [统一伦理](ARGUMENTS-M-Z.md#unified-ethical-grounding) · [评价根据](ARGUMENTS-A-L.md#evaluative-grounding) · [良知](ARGUMENTS-A-L.md#liangzhi-evolution) |
| 数学与一般规律推进到哪里？ / How far do mathematical and general results reach? | [Lean 核心](ARGUMENTS-A-L.md#generative-core-lean) · [数学根前沿](ARGUMENTS-M-Z.md#mathematical-root-frontier) · [条件普遍性](ARGUMENTS-A-L.md#conditional-universality) |
| 怎样检验或改变理论？ / How can the theory be tested or revised? | [经验范围](ARGUMENTS-A-L.md#empirical-scope) · [实验接入](ARGUMENTS-A-L.md#experimental-access) · [非二元方法](ARGUMENTS-M-Z.md#nondual-method) |
| 与既有思想、技术和共同生活有什么关系？ / How does it connect to earlier theories and practice? | [理论分支图](THEORY-MAP.md) · [道与生成](ARGUMENTS-A-L.md#dao-and-generativity) · [王阳明](ARGUMENTS-M-Z.md#wang-yangming) |

## 覆盖与证据含义 / Coverage and evidence

本阅读版保留 **139 个顶层 Markdown 章节**及 **17 个理论分支 README** 的已记录核读版本。新增章节、来源变化及会话成果见[当前检查点地图](SESSION-RESULTS.md)；旧摘要与哈希没有因导航更新而自动升级。章节是阅读和维护单元，不是独立理论或定理数。每项提供中英论证与意义，完整原文、历史批评及证明继续保留。

This reading edition retains the recorded source versions of **139 unified chapters** and **17 branch READMEs**. Additional chapters, changed source versions and session outcomes appear in the [checkpoint map](SESSION-RESULTS.md). Navigation updates do not certify old summaries or refresh their review hashes. Chapters are reading units, not independent theories or theorems; full arguments, criticism and proofs remain at their original locations.

| 标签 / Category | 含义 / Meaning |
|---|---|
| 有条件的检查结果 / Checked conditional result | Lean 检查指定定义与前提下的形式推论；模型与实际对象的对应、伦理前提的根据另列。 / Formal inference under specified definitions and hypotheses; correspondence and normative warrant remain separate. |
| 哲学或文本论证 / Philosophical or textual argument | 有正面论证、异议与来源；没有直接 Lean 时明确保留。 / Argument, criticism and sources; missing direct formalization stays visible. |
| 历史数学结果 / Historical mathematics | 保持原有手证、计算或历史检查的验证范围；不由后来的关联模块追认。 / Retains its original hand-proof, computation or historical-check scope. |
| 经验或合成证据 / Empirical or synthetic evidence | 真实研究、对应解释、有限模拟各按原有范围阅读。 / Real studies, correspondence and finite simulations keep distinct scopes. |
| 开放研究 / Open research | 目标、猜想和拟议检验；不计作完成结果。 / Targets, conjectures and proposed tests, not completed results. |

角色、边界、认识和评价都按[非二元方法](../chapters/NONDUAL-METHOD.md)理解为同一展开中形成的关系。分类只是阅读分工，不把过程分成互不相关的事实、价值或主体与世界。正面成果、实际损失和反例均保留。

Under the shared nondual method, roles, boundaries, knowing and evaluation are differentiated relations within one unfolding. The catalogue’s categories organize reading; they do not split reality into independent domains. Positive results, losses and counterexamples remain visible.

## 逐项列表 / Complete chapter list

编号沿用原文件名，支持页面搜索（中文、英文或文件名）。每项的 Lean 栏只指认具体对应；“有 Lean”不表示整个哲学结论都已获证。

Identifiers follow source filenames. Search by Chinese, English or filename. A Lean link identifies a particular correspondence; it does not certify the entire philosophical claim.

| 编号 / ID | 中英标题 / Bilingual title | 类别 / Category |
|---|---|---|
| [`abstraction-acquisition`](ARGUMENTS-A-L.md#abstraction-acquisition) | 从预测失败获得抽象 / Acquiring abstraction from prediction failure | 学习 / learning |
| [`alignment-and-governance`](ARGUMENTS-A-L.md#alignment-and-governance) | 对齐与治理中的未来条件 / Conditions of a future in alignment and governance | 对齐 / alignment |
| [`alignment-axis`](ARGUMENTS-A-L.md#alignment-axis) | 善恶与可辩护的对齐方向 / A defensible good–evil direction for alignment | 伦理 / ethics |
| [`alignment-completion`](ARGUMENTS-A-L.md#alignment-completion) | 对齐与治理的完成条件 / Completion conditions for alignment and governance | 路线 / roadmap |
| [`alignment-direction`](ARGUMENTS-A-L.md#alignment-direction) | 我们主张怎样的 AI 对齐方向 / The direction of AI alignment we propose | 对齐 / alignment |
| [`alignment-through-change`](ARGUMENTS-A-L.md#alignment-through-change) | 变化中的生成性对齐 / Generative alignment through change | 对齐 / alignment |
| [`architecture-formation`](ARGUMENTS-A-L.md#architecture-formation) | 组织怎样改变自己能形成的架构 / How organization changes the architectures it can form | 机制 / mechanism |
| [`architecture-learning`](ARGUMENTS-A-L.md#architecture-learning) | 形成的路线学习他者的差异 / A formed route learns a recipient's difference | 学习 / learning |
| [`assumption-free-foundation`](ARGUMENTS-A-L.md#assumption-free-foundation) | 生生的无假设奠基：从实际发生到生成的根据 / An assumption-free foundation of 生生: enactment and its warrant | 基础 / foundation |
| [`attainable-mathematical-questions`](ARGUMENTS-A-L.md#attainable-mathematical-questions) | 并非总有信息最多的可行探究 / There need not be a most informative feasible inquiry | 数学 / mathematics |
| [`autonomous-method-formation`](ARGUMENTS-A-L.md#autonomous-method-formation) | 数学方法连接的形成与替换 / Forming and replacing a mathematical method connection | 学习 / learning |
| [`basic-conflict-judgment`](ARGUMENTS-A-L.md#basic-conflict-judgment) | 基本要求冲突时怎样判断 / Judgment when basic claims conflict | 伦理论证 / ethical argument |
| [`becoming-foundation`](ARGUMENTS-A-L.md#becoming-foundation) | 生成与变化之论：根基范围 / Theory of Becoming: foundational scope | 基础 / foundation |
| [`choice-and-generative-context`](ARGUMENTS-A-L.md#choice-and-generative-context) | 共同选择、有限合并与情境 / Joint choice, limited aggregation and context | 伦理论证 / ethical argument |
| [`claims`](ARGUMENTS-A-L.md#claims) | 已登记主张与历史账本 / Registered claims and historical ledger | 导航 / navigation |
| [`claims-and-paid-action`](ARGUMENTS-A-L.md#claims-and-paid-action) | 诉求、实际行动与持续保护 / Claims, actual action and continuing protection | 伦理接口 / ethics interface |
| [`cognition-learning-and-evolution`](ARGUMENTS-A-L.md#cognition-learning-and-evolution) | 生成展开中的认知、学习与演化 / Cognition, learning and evolution within becoming | 学习 / learning |
| [`cognition-li-and-reciprocity`](ARGUMENTS-A-L.md#cognition-li-and-reciprocity) | 认知、理与恕的条件推论 / Cognition, li and a conditional account of reciprocity | 经典思想 / classical |
| [`completion-plan`](ARGUMENTS-A-L.md#completion-plan) | 物理形成与更新分支的完成计划 / Completion plan for physical formation and renewal | 路线 / roadmap |
| [`concern-and-correction`](ARGUMENTS-A-L.md#concern-and-correction) | 关切与有效纠正的连接 / Concern and effective correction | 机制 / mechanism |
| [`concern-and-new-reasons`](ARGUMENTS-A-L.md#concern-and-new-reasons) | 理由内容的扩展：既有判断何时继续成立 / Extending reasons: when earlier judgments survive | 伦理发展 / ethics development |
| [`conditional-universality`](ARGUMENTS-A-L.md#conditional-universality) | 局部律所蕴含的条件普遍性 / Conditional universality from local laws | 数学 / mathematics |
| [`connected-generative-model`](ARGUMENTS-A-L.md#connected-generative-model) | 一个连贯生成模型的实际连接 / Actual connections in one model of becoming | 综合 / synthesis |
| [`controlled-refinement`](ARGUMENTS-A-L.md#controlled-refinement) | 在描述转换中保留学习者 / Controlled refinement without losing the learner | 数学 / mathematics |
| [`cost-sensitive-learning`](ARGUMENTS-A-L.md#cost-sensitive-learning) | 真实学习数据能识别什么 / What real learning data can identify | 经验研究 / empirical |
| [`cybernetics`](ARGUMENTS-A-L.md#cybernetics) | 生成根基中的控制论 / Cybernetics within generative grounding | 比较 / comparison |
| [`dao-and-generativity`](ARGUMENTS-A-L.md#dao-and-generativity) | 生成论与道：生成、德与善的贯通 / Generativity and dao: generation, de and goodness | 经典思想 / classical |
| [`deeper-generative-root`](ARGUMENTS-A-L.md#deeper-generative-root) | 更深的生成根基与内在解释 / A deeper generative root and immanent explanation | 基础 / foundation |
| [`empirical-scope`](ARGUMENTS-A-L.md#empirical-scope) | 候选基础的证据范围 / Evidence scope of the candidate foundation | 证据 / evidence |
| [`ethical-foundation`](ARGUMENTS-A-L.md#ethical-foundation) | 生成世界中受影响者何以重要 / Why affected beings matter within becoming | 伦理 / ethics |
| [`ethical-learning`](ARGUMENTS-A-L.md#ethical-learning) | 伦理学习：关切怎样形成、取得根据并继续改变 / Ethical learning: how concern forms, acquires warrant and keeps changing | 伦理发展 / ethics development |
| [`evaluation-and-faithful-reporting`](ARGUMENTS-A-L.md#evaluation-and-faithful-reporting) | 有价值的未来与忠实报告 / Valued futures and faithful reporting | 对齐 / alignment |
| [`evaluative-application`](ARGUMENTS-A-L.md#evaluative-application) | 获得的理解何时支持具体行动 / When acquired understanding warrants action | 伦理接口 / ethics interface |
| [`evaluative-grounding`](ARGUMENTS-A-L.md#evaluative-grounding) | 形成的倾向怎样回应正当诉求 / How a formed disposition answers a justified claim | 伦理接口 / ethics interface |
| [`evaluative-plasticity`](ARGUMENTS-A-L.md#evaluative-plasticity) | 评价连接的学习与改变 / Learning and changing an evaluative connection | 学习 / learning |
| [`evaluative-succession`](ARGUMENTS-A-L.md#evaluative-succession) | 评价的继承、后继与新证据 / Acquired evaluation, succession and new evidence | 学习 / learning |
| [`evaluative-uptake`](ARGUMENTS-A-L.md#evaluative-uptake) | 后果怎样进入对象导向的选择 / How acquired consequences influence recipient-directed choice | 学习 / learning |
| [`evidence-and-institutional-correction`](ARGUMENTS-A-L.md#evidence-and-institutional-correction) | 证据怎样转为制度纠正 / From evidence to institutional correction | 治理 / governance |
| [`evolutionary-organization`](ARGUMENTS-A-L.md#evolutionary-organization) | 演化怎样形成并改变演化组织 / How evolution forms and changes evolutionary organization | 机制 / mechanism |
| [`experimental-access`](ARGUMENTS-A-L.md#experimental-access) | 学习模型检验自身实验接入 / A learned model tests its experimental access | 学习 / learning |
| [`explanatory-necessity`](ARGUMENTS-A-L.md#explanatory-necessity) | 生成关系是否是充分解释的必要基础？ / Are relations of becoming indispensable to explanation? | 数学 / mathematics |
| [`formal-core`](ARGUMENTS-A-L.md#formal-core) | 关系生成性的形式核心 / Formal core of relational generativity | 形式汇编 / formal compendium |
| [`formal-specification`](ARGUMENTS-A-L.md#formal-specification) | 物理形成、更新与共享能力的规格 / Specification for formation, renewal and shared capability | 形式规格 / formal specification |
| [`formation`](ARGUMENTS-A-L.md#formation) | 有效纠正怎样形成与被阻止 / How effective correction forms and is prevented | 机制 / mechanism |
| [`formation-math`](ARGUMENTS-A-L.md#formation-math) | 通过替代能力形成有效纠正的数学 / Mathematics of correction through a constructed alternative | 数学 / mathematics |
| [`formation-prior-art`](ARGUMENTS-A-L.md#formation-prior-art) | 形成有效纠正的先行研究审查 / Prior-art review of effective correction formation | 审查 / review |
| [`formed-route-monitor`](ARGUMENTS-A-L.md#formed-route-monitor) | 学习者取得自身学习路线的证据 / A learner acquires evidence about its learning route | 学习 / learning |
| [`foundation-premises`](ARGUMENTS-A-L.md#foundation-premises) | 共同基础的前提与已导出内容 / Premises and derived content of the common foundation | 方法 / methodology |
| [`g0-warrant`](ARGUMENTS-A-L.md#g0-warrant) | G0 的根据：一项采用的公理怎样得到支持 / The warrant for G0: how an adopted axiom is supported | 规范基础 / normative foundation |
| [`generated-logic`](ARGUMENTS-A-L.md#generated-logic) | 生成条件与逻辑规则 / Conditions of becoming and logical rules | 数学 / mathematics |
| [`generated-self-and-ethics`](ARGUMENTS-A-L.md#generated-self-and-ethics) | 生成的我与不以根本所有者为前提的伦理 / The generated self and ethics without a fundamental owner | 基础 / foundation |
| [`generative-core-lean`](ARGUMENTS-A-L.md#generative-core-lean) | 生成核心的 Lean 实现与入口 / Lean realization and public entries of the generative core | 形式索引 / formal index |
| [`generative-development`](ARGUMENTS-A-L.md#generative-development) | 调节、学习与关切怎样发展 / Development of regulation, learning and concern | 综合 / synthesis |
| [`generative-grounding`](ARGUMENTS-A-L.md#generative-grounding) | 意义、学习与智慧的生成奠基 / Generative grounding of significance, learning and wisdom | 研究纲领 / programme |
| [`generative-mathematical-admissibility`](ARGUMENTS-A-L.md#generative-mathematical-admissibility) | 通过一致完备化解释数学可容许性 / Mathematical admissibility through coherent completion | 数学 / mathematics |
| [`generative-selection`](ARGUMENTS-A-L.md#generative-selection) | 选择、共享条件与纠正的更新 / Selection, shared conditions and renewal of correction | 选择 / selection |
| [`goal-formation-and-revision`](ARGUMENTS-A-L.md#goal-formation-and-revision) | 理解并改变自身形成条件 / Understanding and changing one's formative conditions | 学习 / learning |
| [`hanzi-and-theory-tree`](ARGUMENTS-A-L.md#hanzi-and-theory-tree) | 汉字、组合与理论树的局部对应 / Hanzi, composition and local mappings to the theory tree | 经典思想 / classical |
| [`huigen`](ARGUMENTS-A-L.md#huigen) | 慧根：整个生成理论的必要性问题 / Huigen: necessity of the entire theory | 基础 / foundation |
| [`immanent-mathematical-identity`](ARGUMENTS-A-L.md#immanent-mathematical-identity) | 生成活动中的数学同一性 / Mathematical identity within becoming | 数学 / mathematics |
| [`inquiry-and-mathematical-identity`](ARGUMENTS-A-L.md#inquiry-and-mathematical-identity) | 探究改变仍可辨认的内容 / Inquiry changes what remains identifiable | 数学 / mathematics |
| [`inquiry-revision`](ARGUMENTS-A-L.md#inquiry-revision) | 保留后果改变后续询问的安排 / Retained consequences revise further inquiry | 学习 / learning |
| [`joint-formation`](ARGUMENTS-A-L.md#joint-formation) | 关切、证据与有效权力共同形成和更新 / Joint formation and renewal of concern, evidence and power | 机制 / mechanism |
| [`joint-formation-math`](ARGUMENTS-A-L.md#joint-formation-math) | 学习、证据、权力和关切的联合形成数学 / Mathematics of jointly formed learning, evidence, power and care | 数学 / mathematics |
| [`joint-obstructions`](ARGUMENTS-A-L.md#joint-obstructions) | 没有隐藏善意的联合形成阻碍 / Obstructions to joint formation without hidden benevolence | 审查 / review |
| [`joint-prior-art`](ARGUMENTS-A-L.md#joint-prior-art) | 关切、证据与权力联合形成的先行研究 / Prior art on joint formation of concern, evidence and power | 审查 / review |
| [`knowledge`](ARGUMENTS-A-L.md#knowledge) | 生成中的知识 / Knowledge within becoming | 认识论 / philosophical epistemic |
| [`learning-interface`](ARGUMENTS-A-L.md#learning-interface) | 后果差异如何进入可用修订 / From consequential difference to accessible revision | 数学 / mathematics |
| [`learning-route-revision`](ARGUMENTS-A-L.md#learning-route-revision) | 学习者改变学习路线并传递改变 / A learner changes and transmits its learning route | 学习 / learning |
| [`liangzhi-evolution`](ARGUMENTS-A-L.md#liangzhi-evolution) | 本然良知的生成演化 / Generative evolution of prereflective moral responsiveness | 伦理发展 / ethics development |
| [`living-dependencies`](ARGUMENTS-A-L.md#living-dependencies) | 生命延续中的实际依存 / Living dependencies within generative continuation | 机制数学 / mechanism mathematics |
| [`market-dynamics-math`](ARGUMENTS-M-Z.md#market-dynamics-math) | 市场更新、选择与俘获的数学模型 / Market renewal, selection and capture | 数学模型 / mathematical model |
| [`markets-and-generative-regimes`](ARGUMENTS-M-Z.md#markets-and-generative-regimes) | 使市场维持生成方向 / Keeping markets in generative regimes | 应用 / application |
| [`material-prediction-composition`](ARGUMENTS-M-Z.md#material-prediction-composition) | 材料构造接入预测与修正 / Material construction of prediction and correction | 机制 / mechanism |
| [`material-selector-composition`](ARGUMENTS-M-Z.md#material-selector-composition) | 由真实部件构造可改换的选择器 / Constructing revisable selectors from actual parts | 机制 / mechanism |
| [`material-updater-composition`](ARGUMENTS-M-Z.md#material-updater-composition) | 选择器与更新器共用同一材料历史 / Selectors and updaters sharing one material history | 机制 / mechanism |
| [`mathematical-core`](ARGUMENTS-M-Z.md#mathematical-core) | 系统谓词与证明的数学核心 / A mathematical core for systems predicates and proofs | 数学 / mathematics |
| [`mathematical-root-frontier`](ARGUMENTS-M-Z.md#mathematical-root-frontier) | 生成根基的数学重构前沿 / The frontier of mathematical reconstruction | 数学 / mathematics |
| [`mathematical-truth-and-the-root`](ARGUMENTS-M-Z.md#mathematical-truth-and-the-root) | 数学真理与生成根基 / Mathematical truth and the generative root | 数学 / mathematics |
| [`mathematics-and-generativity`](ARGUMENTS-M-Z.md#mathematics-and-generativity) | 数学与生成奠基 / Mathematics and generative grounding | 数学 / mathematics |
| [`measured-feedback-correspondence`](ARGUMENTS-M-Z.md#measured-feedback-correspondence) | 测得的反馈与实际对应 / Measured feedback and physical correspondence | 经验识别 / empirical identification |
| [`memory-correction-and-succession`](ARGUMENTS-M-Z.md#memory-correction-and-succession) | 记忆修正、选择性继承与后续执行 / Memory correction, selective inheritance and execution | 经验识别 / empirical identification |
| [`meta-revision`](ARGUMENTS-M-Z.md#meta-revision) | 修订策略的资源与信息边界 / Resource and information limits of metarevision | 数学边界 / mathematical boundary |
| [`method-revision`](ARGUMENTS-M-Z.md#method-revision) | 由实际后果修订数学方法 / Revising mathematical methods through consequences | 机制 / mechanism |
| [`model-family-revision`](ARGUMENTS-M-Z.md#model-family-revision) | 用新证据修订模型族 / Revising model families with new evidence | 机制 / mechanism |
| [`new-possibilities`](ARGUMENTS-M-Z.md#new-possibilities) | 新可能性的形成 / Formation of new possibilities | 机制 / mechanism |
| [`nondual-method`](ARGUMENTS-M-Z.md#nondual-method) | 全项目非二元研究方法 / The project-wide nondual method | 方法 / methodology |
| [`noninstrumental-concern`](ARGUMENTS-M-Z.md#noninstrumental-concern) | 一体之仁与非工具性关切 / Co-formed benevolence and noninstrumental concern | 伦理机制 / ethical mechanism |
| [`paid-preimport-evidence`](ARGUMENTS-M-Z.md#paid-preimport-evidence) | 命令导入前取得独立证据 / Acquiring independent evidence before command import | 机制 / mechanism |
| [`philosophical-account`](ARGUMENTS-M-Z.md#philosophical-account) | 认识与生活的生成哲学 / A philosophy of becoming for knowing and living | 综合 / synthesis |
| [`plural-systems-and-correction`](ARGUMENTS-M-Z.md#plural-systems-and-correction) | 因应转化：多系统、共同试验与父子关系 / Responsive transformation: plural systems, shared trials and parent/subsystem relationships | 对齐 / alignment |
| [`practical-judgment`](ARGUMENTS-M-Z.md#practical-judgment) | 实践判断：保留、转化、交接、结束与责任 / Practical judgment: preservation, transformation, transfer, ending and responsibility | 伦理 / ethics |
| [`pre-qin-and-wenyan`](ARGUMENTS-M-Z.md#pre-qin-and-wenyan) | 先秦与文言传统的竞争解释 / Competing explanations across pre-Qin and classical Chinese traditions | 经典比较 / classical comparison |
| [`prediction-action`](ARGUMENTS-M-Z.md#prediction-action) | 形成的机器取得预测并用于行动 / Formed machinery acquires prediction and acts | 机制 / mechanism |
| [`prediction-protocol`](ARGUMENTS-M-Z.md#prediction-protocol) | 预测器的多事件学习协议 / The predictor’s multi-event learning protocol | 形式接口 / formal interface |
| [`protocol-completion`](ARGUMENTS-M-Z.md#protocol-completion) | 发出的操作何时保证完成 / When an issued operation is guaranteed to complete | 形式接口 / formal interface |
| [`protocol-composition`](ARGUMENTS-M-Z.md#protocol-composition) | 多个物理事件如何实现一个学习步骤 / Composing physical protocols into learning steps | 形式接口 / formal interface |
| [`proved-connections`](ARGUMENTS-M-Z.md#proved-connections) | 已证结果之间的连接 / Connections among proved results | 形式索引 / formal index |
| [`reason-protection`](ARGUMENTS-M-Z.md#reason-protection) | 从当前理由到有效保护 / From current reasons to effective protection | 机制与策略 / mechanism strategy |
| [`recipient-correction`](ARGUMENTS-M-Z.md#recipient-correction) | 不覆盖其他位置的条件而修正帮助 / Correcting recipient action without overwriting other conditions | 机制 / mechanism |
| [`recipient-cue-grounding`](ARGUMENTS-M-Z.md#recipient-cue-grounding) | 外部社会线索与受益者行动 / External social cues and recipient-directed action | 经验识别 / empirical identification |
| [`recipient-harm-and-action`](ARGUMENTS-M-Z.md#recipient-harm-and-action) | 受影响者损害与学习行动 / Recipient harm and learned action | 经验识别 / empirical identification |
| [`recipient-reason-action`](ARGUMENTS-M-Z.md#recipient-reason-action) | 实际受益者理由进入行动 / Actual recipient reasons enter action | 机制 / mechanism |
| [`recipient-reason-revision`](ARGUMENTS-M-Z.md#recipient-reason-revision) | 新后果修订受益者理由与行动 / Fresh consequences revise recipient reasons and action | 机制 / mechanism |
| [`recipient-renewal`](ARGUMENTS-M-Z.md#recipient-renewal) | 受益者支持下的学习更新与延续 / Recipient-supported learning renewal | 机制 / mechanism |
| [`recipient-transmission`](ARGUMENTS-M-Z.md#recipient-transmission) | 受益者路线形成与后果资助传递 / Formed recipient routes and consequence-funded transmission | 机制 / mechanism |
| [`recorded-reasons`](ARGUMENTS-M-Z.md#recorded-reasons) | 记录、可修订理由与重建 / Recorded evidence, revisable reasons and reconstruction | 机制 / mechanism |
| [`relations-across-scales`](ARGUMENTS-M-Z.md#relations-across-scales) | 尺度之间的关系 / Relations across scales | 机制数学 / mechanism mathematics |
| [`revisable-concern-settlement`](ARGUMENTS-M-Z.md#revisable-concern-settlement) | 可修订关切的选择与接续 / Selection and succession of revisable concern | 机制与策略 / mechanism strategy |
| [`reward-learning-and-recipient-choice`](ARGUMENTS-M-Z.md#reward-learning-and-recipient-choice) | 奖励关联学习与受益者选择 / Reward association and recipient-directed choice | 经验识别 / empirical identification |
| [`route-diagnostics`](ARGUMENTS-M-Z.md#route-diagnostics) | 学习路线的诊断证据 / Evidence for diagnosing learning routes | 形式接口 / formal interface |
| [`scientific-philosophy`](ARGUMENTS-M-Z.md#scientific-philosophy) | 科学哲学与探究的生成条件 / Scientific philosophy and inquiry’s generative conditions | 认识论 / philosophical epistemic |
| [`selector-revision`](ARGUMENTS-M-Z.md#selector-revision) | 选择器通过自身后果被改换 / Selector revision through its consequences | 机制 / mechanism |
| [`semantic-action-composition`](ARGUMENTS-M-Z.md#semantic-action-composition) | 保持行动所涉对象与命题 / Preserving recipient and proposition through action composition | 形式接口 / formal interface |
| [`semantic-calibration`](ARGUMENTS-M-Z.md#semantic-calibration) | 以先前实际取得的记录校准理由 / Calibrating reasons against acquired records | 形式接口 / formal interface |
| [`shengsheng`](ARGUMENTS-M-Z.md#shengsheng) | 生生：活动怎样形成进一步活动 / 生生: how activity forms further activity | 综合 / synthesis |
| [`source-map`](ARGUMENTS-M-Z.md#source-map) | 来源、谱系与证据边界 / Sources, genealogy and evidence boundaries | 导航 / navigation |
| [`start-here`](ARGUMENTS-M-Z.md#start-here) | 统一理论简明入口 / The unified foundation in brief | 导航 / navigation |
| [`stochastic-prediction-composition`](ARGUMENTS-M-Z.md#stochastic-prediction-composition) | 保留失败学习的完整接续分布 / Complete continuation distributions including learning failures | 形式接口 / formal interface |
| [`strongest-foundation-claim`](ARGUMENTS-M-Z.md#strongest-foundation-claim) | 最强生成根基主张 / The strongest foundation claim | 研究纲领 / research programme |
| [`successor-learning`](ARGUMENTS-M-Z.md#successor-learning) | 后继学习并传递其修正 / A successor learns and transmits its correction | 机制 / mechanism |
| [`sustained-living-judgment`](ARGUMENTS-M-Z.md#sustained-living-judgment) | 持续的生活组织与共同实践判断 / Sustained living organization and collective practical judgment | 伦理机制 / ethical mechanism |
| [`synthesis-record`](ARGUMENTS-M-Z.md#synthesis-record) | 综合与核查记录 / Synthesis and verification record | 导航 / navigation |
| [`system-individuation`](ARGUMENTS-M-Z.md#system-individuation) | 系统怎样形成其边界与可能性 / Systems, constitutive relationships and possible change | 基础 / foundation |
| [`system-warrant`](ARGUMENTS-M-Z.md#system-warrant) | 系统关系与可行变化怎样获得根据 / Grounding system relationships and admissible variations | 基础 / foundation |
| [`systems-complexity-chaos`](ARGUMENTS-M-Z.md#systems-complexity-chaos) | 系统、复杂性与混沌的生成整合 / Systems, complexity and chaos within generative grounding | 数学 / mathematics |
| [`the-theory-of-becoming`](ARGUMENTS-M-Z.md#the-theory-of-becoming) | 生成／变化之论 / The Theory of Becoming | 综合 / synthesis |
| [`the-theory-of-evolution`](ARGUMENTS-M-Z.md#the-theory-of-evolution) | 演化之论 / The Theory of Evolution | 研究纲领 / research programme |
| [`theory`](ARGUMENTS-M-Z.md#theory) | 关系生成与智慧的条件 / Relational generativity and the conditions of wisdom | 综合 / synthesis |
| [`theory-of-becoming`](ARGUMENTS-M-Z.md#theory-of-becoming) | 生成关系怎样变化 / How relations of becoming change | 机制 / mechanism |
| [`tool-evidence-and-authority`](ARGUMENTS-M-Z.md#tool-evidence-and-authority) | 外部证据、权限与有效行动 / External evidence, authority and effective action | 经验识别 / empirical identification |
| [`unified-ethical-grounding`](ARGUMENTS-M-Z.md#unified-ethical-grounding) | 整体生成中的统一伦理根据 / Unified ethical grounding within becoming | 规范基础 / normative foundation |
| [`universal-ethical-minimum`](ARGUMENTS-M-Z.md#universal-ethical-minimum) | 容纳多元生活的普遍伦理最低主张 / A universal ethical minimum compatible with plural lives | 伦理论证 / ethical argument |
| [`updater-formation`](ARGUMENTS-M-Z.md#updater-formation) | 形成并改变修订选择器的机制 / Forming and changing selector updaters | 机制 / mechanism |
| [`valuation-development`](ARGUMENTS-M-Z.md#valuation-development) | 评价倾向怎样发展 / How valuation develops | 机制数学 / mechanism mathematics |
| [`valuation-identification-bounds`](ARGUMENTS-M-Z.md#valuation-identification-bounds) | 评价改变的可识别性界限 / Bounds for identifying changed evaluation | 识别数学 / identification mathematics |
| [`wang-yangming`](ARGUMENTS-M-Z.md#wang-yangming) | 王阳明、一体之仁与工夫的整体整合 / Wang Yangming, benevolence and situated practice | 经典伦理 / classical ethical |
| [`wisdom-and-context`](ARGUMENTS-M-Z.md#wisdom-and-context) | 智慧、情境与共同核心 / Wisdom, context and the common core | 认识论 / philosophical epistemic |
| [`zero-axiom-practical-judgment`](ARGUMENTS-M-Z.md#zero-axiom-practical-judgment) | 零公理实践判断：正在建立的根据 / Zero-axiom practical judgment | 规范基础 / normative foundation |

## 维护 / Maintenance

条目数据位于 [A–L](data/arguments-a-l.json)、[M–Z](data/arguments-m-z.json)和[分支表](data/theory-map.json)。`source_sha256` 记录阅读对应的源码版本；原文变化后须重读相关条目。生成视图记为 `generated-view`，其各行随成果记录检查。以本目录取代复制工作区；原始研究继续在既有理论与研究文件中修订。

The JSON registers hold the paired readings. `source_sha256` records the inspected version; changed sources require a targeted reread. Generated views record `generated-view`; their rows follow the record checks. Continue substantive work in the existing study files.

```sh
python3 _process/research/2026-10-05-generative-foundation-review/root-foundation/build_results_catalogue.py --check
python3 _process/research/2026-10-05-generative-foundation-review/root-foundation/build_lean_catalogue.py --check
```

这些命令从仓库根目录执行，只核对目录、字段、链接与快照，不编译 Lean，也不增加科学证据。更新时先修订受影响的中英条目和版本标记，再去掉 `--check` 生成相应目录；Lean 的实际复现按各包自己的 README 进行。详见[本轮编辑记录](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/RESULTS-CATALOGUE-RECORD.md)。

Run from the repository root. These checks validate documentation, links and snapshots, not Lean proofs. Review affected bilingual entries and version markers before regeneration. Reproduce formal results through each package’s own instructions.
