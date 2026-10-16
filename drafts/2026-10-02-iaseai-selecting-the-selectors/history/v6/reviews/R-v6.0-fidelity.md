# R-v6.0 评审：对 Ren 方向的忠实度、架构、内容损失

*2026-10-03。评审对象 `v6/THEORY.md`（v6.0）及 CLAIMS/CHANGELOG/附录 F。透镜：忠实、架构、连贯、损失。不查证明。评审者与起草者同属一个模型家族，同族偏差适用。*

## 总判断

v6.0 在骨架上忠实于 Ren 的八条意见：一股压力→反身闭合→重叠机制→三重侵蚀→工具与化身→一个系统→改变选择内容→生成的元吸引子→过渡→判断，这条脊柱在正文里是连着的，各节互相引用而不重复。正文不点名国家、企业、人物（人名只出现在登记与文献）；替代方案一律给"最强形式"，没有偏向竞赛阵营；E2 与 E3 分开；"判断游戏不判断行为"、"危险的是心不是增长"、肯定式结论都在。**没有致命问题。**

重要问题有三类：(1) "一体"在定理 5.16 和 §10.2 又滑回"目标宽度加保管"，即偏好层；(2) 附录 F 把九项标为"撤回"，与计划 §4"提升层面而非撤回"和 CLAIMS §7 的"Raised"自相矛盾，正是 Ren 要的"更优雅的办法"没有写进正文；(3) v5.2 §1.3 的三样东西（关系自我与大同、κ 随力量上升的收敛猜想、θ_g 阈值）被删且未入账本，账本另有三处记错。冷读方面，§0 很好，但中文概要 24 行塞了 19 个编号引用，术语先于解释。

## 发现（按严重度）

### 【重要 1】"一体"在必要性论断处滑回目标层

- **位置**：定理 5.16 之后（1145 行）："'We are one' becomes a necessity, not only a gain, under three conditions"；中文概要第 5 条"此时一体是增益；在竞赛宣称要追求的那个政权里，它是必需"；§10.2 第 8 条末句。
- **问题**：定理 5.16(2) 要求的是"common custody"加"objectives… under which restraint is a stage-game equilibrium"，即目标宽度与保管。紧接着把这个要求叫作"我们是一体"，等于把 §3.8 刚刚立起来的"系统性质"又定义为"目标与制度设定"。§3.8 说"一体不是偏好"，5.16 用法与之不一致。
- **为什么重要**：这正是 Ren 第 7 条批评的"too literal"。评审者会抓住这一句说"一体仍然等于 θ 足够大"。
- **修法**：改为 "Cooperation built into objectives and custody then becomes a necessity, not only a gain. That is the institutional form in which the system counts itself as one (Section 3.8(5)); oneness itself is the property that makes such cooperation the accurate response, not a parameter the theorem sets." 概要与 §10.2 同改。另：概要"政权"是 regime 的误译，应作"那种状态／区间"。

### 【重要 2】§3.7 从"预见性整合"到"必须理解为一体"的一步是断言

- **位置**：611–613 行："Those rules… have to be designed in advance, by actors who see the system as one"；"anticipation requires that the system be understood as one"。
- **问题**：引理 3.10 证明的是群间项为零，整合只能靠改变群内回报的规则。"规则必须由看见整体的人设计"没有推导：为什么不能由只想避免灭绝的狭隘行动者设计？而且"That the lemma leaves only this route is a theorem"说过头，它还需要"没有外生冲击完成整合"这一假设。
- **修法**：补一句机制：预见性规则必须建在系统的模型上；边界画在系统之内的模型会错估耦合（命题 3.9(3)），所以它设计出的规则会漏掉它看不见的回报通道（引理 3.3(1)）。这样"理解为一体"= 模型准确，与 §3.8 第 3 条接通，而不是另起一条规范要求。

### 【重要 3】附录 F 的"Withdrawn"与计划、CLAIMS 矛盾

- **位置**：附录 F "Withdrawn, and why" 九项；CLAIMS §7 同样条目标 "Raised and narrowed"；计划 §4 明言只需撤回三项（数值、"分享的是决定性地位"、θ=n−1=一体）。
- **问题**：九项中六项（一个根、增长需扩展自我、分享反转、设计被再吸收、三区为主定理、谱系国别）每条正文都写了"replaced by…"的提升形式，却被归在"撤回"下。
- **为什么重要**：Ren 问的是"有没有更优雅的办法"，v6 的办法（提升层面）是对的，但账本的标签把它又写成了撤回。读者只看附录会得出"v6 撤回了大半核心论断"。
- **修法**：附录 F 分两栏："Restated at the level of game and selection"（六项，各给 v5.2 原文→v6 形式一行）与 "Withdrawn"（仅三项）。与 CLAIMS §7 用同一组词。

### 【重要 4】v5.2 §1.3 三项内容被删且未入账

- **位置**：v5.2 164–167 行。
- **问题**：(a) "the identity that the relational view of the self describes… (the author's theory of the relational self and 大同)"——Ren 自己的理论，v6 全文无"relational"；(b) "Convergence [C]: κ plausibly rises with power… accuracy and inclusion converge"——这是把"一体首先是看得准"落地的猜想，v6 无；(c) 命题 1.3(3) 的 θ_g=(r(n−1)−1)/(1+r)——"总物质收益在任何规模下为正当且仅当 θ≥θ_g"，v6 命题 5.2(3) 只剩天花板，θ_g 消失。附录 F 对三者均无记录。
- **为什么重要**：违反"不做有损合并"；(a) 还是 Ren 的语料而非 AI 代拟。
- **修法**：(a) 入 §3.8 第 3 条末或 §8.2 第 1 股，一句即可：accuracy about one's boundary is the formal face of the author's relational account of the self, in which a self is the action-centre of its relations rather than a point outside them；(b) 作 [C] 入 §3.6 末，并接 C-crux 的 κ 测量；(c) 恢复为命题 5.2(3) 的第二句。三者补入附录 F。

### 【重要 5】账本三处记错

- "The reform dilemma and the guardian test → Remark 8.12"：8.12 只有守护者四问，没有改革两难（"取得改革能力的路径先筛掉改革本身"，Ren 2025-06；Alex 00:35:16）。应在 §8.7 开头补一段，并与 §9 "compensating loop" 接通。
- "What the environment rewards, the mind promotes → §3.3"：实在 §3.6（593 行）。
- "Four loops… → §2.3"：§2.3 恢复的是三个"产物"（滞后被产出、范式趋同、损害与俘获互强），四个回路本身没有作为回路写出。应在 §2.3 表后加一段把四回路串起来，或把账本改为"as three products"。

### 【重要 6】"元吸引子"胜过"生成函数"的理由不在正文

- **位置**：定义 2.2；§2.9 只把 generator functions 列为"被吸收"。理由只在 CHANGELOG。
- **问题**：Ren 说"you need to have good reason"。正文读者看不到理由；且把一个"机制"命名为"吸引子"（定义 2.2 "A meta-attractor is the mechanism of (1)"）本身需要一句解释。
- **修法**：在定义 2.2 后加一个短注：The term is kept over "generator functions" for three reasons: that phrase names causes of risk without the reflexive step (selection rewriting its own criterion), without persistence, and without the layer of minds and language; and it has no generative counterpart, whereas the same reflexive structure selecting for contribution is examined in Section 8. 并说明"attractor"指层 (2) 已证的情形，层 (1) 沿用此名是为了一个概念容纳两种符号。

### 【重要 7】冷读：概要与 §1.2 术语先于解释

- **位置**：中文概要 1–10 条含 19 个编号引用；第 4 条"回报随份额的平方增长""二阶公共品"、第 5 条"阶段均衡""稳健性""可争议的覆盖"均无白话；§1.2 第 1 条用 carriers、reflexive closure、signatures、substrate，定义都在 §2 以后；定义 2.1(1) 前引定义 3.2。
- **判断**：§0 四段非常好，用途与意义先于术语。概要的第一段也对，但从第 1 条起就是给审稿人看的摘要。
- **修法**：概要每条先一句白话再括注编号，或把编号集中到条末；"二阶公共品"改"竞争者自己供给不了的纠错"；"阶段均衡"改"不靠未来惩罚也会自觉遵守的那部分"。§1.2 第 1 条改 "whatever can gain or lose share (carriers)"。定义 2.1(1) 把"relative, payoff-monotone"的白话（只看差异、好的多长）写在句内。

### 【次要】

- **因果链被拉平**：Ren 的第 5 条是链："压力→加速→越来越难规制，加上语言异化"。§2.4 把三者并列；链只在 §5.5 剪刀差和 §2.3 "lag is produced" 恢复。建议 §2.4 第 2 条首句改为 "Correction becomes harder, in part because acceleration outruns it…"。
- **第三侵蚀偏薄**：§5.4 约 20 行，而语言异化是三后果之一。Ren 语料的叙事—价值框架（NVF）机制（P5 §1.5：词汇逃出游戏、框架锁死、"by the time you notice the frame…"）只用了一句。可加一段"叙事作为被选择的载体"，用 §2.2 的 (x,σ) 形式。
- **§7.12 位置漂移**：它是 §2.6 的 IR 译本，放在 §7.11 比较之后像附录。建议并入 §2.6 末或 §5.5 之后。v5.2 §4.6 的"攻防框架双重危险象限（P1 加两用）"一句被删。
- **比例**：§2.6 "systemically false" 的思想史段（Spencer、Hofstadter、Bannister、Leonard）是对评审的防御，占了 Ψ 一节近半；"the gain"（Ren 的"吸引子的吸引子"）被埋在地位文献里。建议思想史移入 §2.8 谱系段，"the gain"独立成一段。§7（7.5k 词）与 §8（7.4k）相当，可接受。
- **ASTRA 七层、GPT 九步链**：P1 §2.4 建议至少列为 [C]；v6 全无。可入 §10.6 研究计划一句。
- **v1 五个区分**在 §4.1 表中，账本未记功。

## 八条意见与裁定

| 条目 | 状态 | 依据 |
|---|---|---|
| 1 不依赖载体 | 守住 | 定义 2.1 载体清单；§2.8 六个载体加另一个星球；§8.6 联邦 |
| 2 两个 AI 问题；奖励信号末端 | 守住 | §6 引言、命题 6.7、§6.6 两层 |
| 3 不用黑白框架 | 守住 | §8.6 按功能推导；注 8.7；正文无 individualism/Western |
| 4 时间非主要 | 守住 | §10.7 外部评审先于投稿；无截止日 |
| 5 一股压力、重叠、三后果 | 守住（链被拉平） | §2.3–2.4、§5.5；见次要 1 |
| 6 三区太窄 | 守住 | 命题 5.7/推论 5.8 一般形式；注 5.9 例示 |
| 7 "一"=同属一系统；提升而非撤回 | 部分 | §3.8 五部分正确；定理 5.16 滑回；附录 F 标"撤回" |
| 8 元吸引子的理由 | 部分 | 定义 2.2 三层好；理由不在正文 |
| 不点名 | 守住 | 正文只有历史人物与学者；CEO 文只在 EV1 并披露 |
| 不抬高竞赛阵营 | 守住 | §7 对称给最强形式；§7.11 事先登记继续胜出的条件 |
| E2≠E3 | 守住 | §9.3 |
| 判断游戏不判断行为 | 守住 | §0、V5、§9.3 广义 E1 |
| 增长非危险，心是 | 守住 | 定理 5.12 后、命题 8.11 |
| 肯定式意义 | 守住 | §0、§10.8 |
| 不做有损合并 | 部分 | 见重要 4、5 |
| 机制先于结论 | 守住 | §2.1 以维护者被置换的故事开篇 |

## 损失表

| 项目 | 原处 | 账本说 | 实际 |
|---|---|---|---|
| 关系自我与大同 | v5.2 §1.3 | 未记 | 消失 |
| κ 随力量上升、准确与包容收敛 [C] | v5.2 §1.3 | 未记 | 消失 |
| θ_g 总收益为正的阈值 | v5.2 命题 1.3(3) | "P1.3(2)–(3) → 5.2(2)–(3)" | 天花板在，θ_g 无 |
| 改革两难 | 语料 2025；10-02 | 注 8.12 | 只有守护者四问 |
| 环境奖励什么，心就推举什么 | 语料 2025 | §3.3 | 在 §3.6 |
| 四回路 | 语料 | §2.3 | 只恢复三个产物 |
| 攻防框架双重危险象限 | v5.2 §4.6 | "§4.6 → §2.6, §7.12" | 该句消失 |
| ASTRA 七层；GPT 九步链 | v2 评审；GPT 交接 | 未记 | 消失（P1 建议列 [C]） |
| v1 五个区分 | v1 表 1 | 未记 | 在 §4.1 表（应记功） |
| v5.2 全部编号结果 | — | 附录 F 逐条 | 核对 69 项均有去处，无遗漏 |
| v4.5 开篇、树、够的点、信任是结果、不可优化出陷阱、合一非同 | v4.5、语料 | 各处 | 均在所述位置 |
