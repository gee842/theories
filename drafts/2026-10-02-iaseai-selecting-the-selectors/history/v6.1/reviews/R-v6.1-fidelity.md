# R-v6.1 评审：对 Ren 的忠实度，以及 v6.0→V6.1 的损失

*2026-10-04。对象：`v6.1/THEORY.md`（sha256 242a61240d810e51…）及 LEDGER、LEDGER-units.tsv、CHANGELOG、DISCUSSION X1/X8/X10、TESTS §5。不查证明。评审者与起草者同属一个模型家族，偏差见第 4 节。脚本在 scratchpad `review61/fidelity/`（`units.py`、`sample.py`，仅用标准库）。*

## 1. 总判断

V6.1 在论证层面比 v6.0 更忠实于 Ren：上轮的七条"重要"大多已修好。"一体"现在是系统性质，经由理解起作用（§3.7、§7.2）；关系自我与大同用了 Ren 的原话；"增长不是危险，心是"有命题 5.14 支撑；"判断博弈，不判断行为"、预测→对齐理解→协调、元吸引子之名的理由都在正文。**没有致命问题。** 但损失集中在一个账本查不到的地方：在一些整体被保留的段落里，恰好丢掉了表达 Ren 规范裁定的那一句。例如广义 E1 的范围（劳动、金融、说服）、"衰败与更新属于生长"、被拒绝的更好守护者名单、"落后无法承受，所以先反对这个逻辑"。随机抽样的 62 个单元几乎都保住了实质；按 Ren 关键词定向扫描时，却找到十几处真实损失。另有三类问题：两个一页摘要（§1.2 与导读）都没有出现"我们是一体"；X1 有两个语料键标错；导读有几处翻译腔和歧义。

## 2. 发现

### 致命

无。

### 重要

**重要 1：广义 E1 被收窄，并从判断中消失。"判断博弈，不判断行为"因此变弱。**
- **位置**：THEORY §0 第 3 段；§6.6（"A use falls under broad E1 when…"）；§11.3 E1；§12.1 第一层第 1 条；导读"判断"段。
- **问题**：Ren 2026-09-26 的裁定是："任何会集中的竞争性博弈都被 AI 加速"，人作为工具的地方（劳动）AI 会胜过人；窄清单只是先停什么的顺序，不是范围。v6.0 有两种措辞。V6.1 合并时只留了较窄的一种（"games that concentrate control *over shared conditions*"）。按这个判据，Ren 的范例（人人用 AI 写求职信，不用的人落后）不一定算在内。这正是 Ren 否定过的"可操作性反射"。
- **证据**：
  - v6.0 L-60-§9.3-p02（账本：rewritten 0.25）："AI not used as an instrument in any contest that tends toward dominance or concentration, such as labour, finance and persuasion. The unit is the game, not the act: a use that helps one person is still an instrument in a game if everyone's use of it makes those without it fall behind."
  - v6.0 L-60-§10.1-p01（rewritten 0.17）："Treat the broad form, AI out of every game that concentrates control over shared conditions, as the scope to which the narrow form is the first step."
  - v6.0 L-60-§0-p03（kept 0.74）的机制句"…and makes those without it fall behind"。
  - 以上三句在 V6.1 中都已不在。"labour" 在 V6.1 只出现一次，在命题 6.4 的 Scope 里，而且是作为排除项。§12.1 三层判断里没有一层含广义 E1。
- **修法**：
  - §0 恢复："…an instrument in a game whose aggregate concentrates control and makes those without it fall behind."
  - §6.6 判据改为："A use falls under broad E1 when, aggregated over its users, it raises convertibility, decisiveness or the conversion of success into control in a competitive game that concentrates: over shared conditions, and equally in labour, finance and persuasion, where those without it fall behind."
  - §12.1 第 1 条末加："The broad form, AI not an instrument in any game that concentrates, is the scope; the narrow form is the first step."
  - 导读判断段加"狭义 E1 是起点，广义 E1 是范围"。

**重要 2：肯定式意义被冲淡。**
- **位置**：§0 第 4 段；§12.4 末段；导读"用途与意义"。
- **问题**：
  - v6.0 §0 的 "Decay and renewal belong to growth." 被删，且未入账。L-60-§0-p04 被标为 kept 0.59，所以没有人读到这一句。
  - V6.1 用"We are part of a larger process of becoming, and that process is good"。Ren 的原话更强："we are not just our life. We are the whole process of the universe doing this and itself and this is great"（`2026-10-02-friend-conversation/transcript.md` 01:06:32–01:06:43）。relational-self README 第 23 条也是 "we are in the system *and are* the system"。
  - "part of" 是成员关系，Ren 说的是同一。这一句正是"我们是一体"在意义层的形式。§3.7 已写出"we are the collective we belong to (我们即是集)"，但最显眼的 §0、§12.4 和导读用的是较弱的一种。
- **修法**：
  - §0 与 §12.4 改为："We are not only our separate lives: we are the larger process of becoming, going on through us, and that is good. Decay and renewal belong to its growth. Humanity has a great future in it…"
  - 导读改为："我们不只是各自的一生；我们就是这场更大的生生过程本身，它借我们继续展开，这是好的。衰败与更新，也是生长的一部分。"

**重要 3：两个一页摘要都没有出现"我们是一体"，导读还缺了 Ren 的靶子"狭隘自我"。**
- **位置**：§1.2 第 2 条；导读论证链第 2 条。
- **问题**：
  - §1.2 第 2 条止于 "…and so must be understood"。v6.0 摘要链第 8 条那句 "Understanding that we are one interconnected system is therefore a long-term requirement if growth and change are favoured"（L-60-§10.2-p01，按重复删除）的要义，现在只在 §3.6 和 §12.4。
  - 导读全文没有"一体"二字（只有"同属一个宿主"）。
  - §1.2 第 2 条里 "selection favours the narrow self-model that the system's real coupling punishes" 这一句，导读也没有。它是 Ren 所说的靶子："a you that only you cares about"，被竞争选择奖赏，即 molochlization（`feedback_ren_why_and_meaning`）。
- **修法**：
  - §1.2 第 2 条末加："That is why understanding that we are one, one interconnected system with one host and no outside, is a long-term requirement if growth and change are to continue."
  - 导读第 2 条改为："所有参与者共处同一个母体，彼此耦合，没有外部。相对选择看不见共有之物……选择偏爱把边界画在系统之内的狭隘自我，而系统真实的耦合恰恰惩罚它。环路增益高时……对全局而不可逆的失败，整合只能事先依据对系统的准确理解来完成，所以，理解'我们是一体'是增长与变化得以延续的长期条件；可挽回的失败仍可从试错中学习。"

**重要 4："没有更好的守护者"和"先反对这个逻辑"只剩了口号。**
- **位置**：注 10.8；§3.8 "The logic to oppose"；§8.3(f)。
- **问题与证据**：
  - (a) v6.0 L-60-§8.7-p01（kept 0.51）："Philosopher-kings, priestly classes, enlightened stewards and new universities have each been proposed as the guardians who would hold the line, and each is a corrector to which Section 4 applies." 这一句被删。这是 Ren 在 10-02 对话里逐一拒绝的那几种答案（meta-attractor README §N）。注 10.8 只剩 "no better guardian is an answer"，读者看不到被拒绝的是什么。
  - (b) v6.0 L-60-§7.12-p03（kept 0.51）："If a winner's logic is of this kind, falling behind cannot be survived, and every actor has reason first to oppose the logic itself." 这是 Ren 10-03 的裁定（"如果胜利者的逻辑是 cancer 式的，落后并不可以承受，因此所有人都应该去首先反对这个逻辑"），V6.1 全文已不在，X1 只留了后半句。
  - (c) 核心 §8.3(f) 把注 8.9 缩成 "because the penalty is set by the winner"，丢了第三条理由："it accepts the frame of the contest: it insures against losing instead of declining the game"。这一条现在只在 S8。剩下的理由（可靠性）是一个"在博弈内适应"的理由，与 Ren 的裁定正好相反。
- **修法**：
  - (a) 恢复到注 10.8 第一句之后。
  - (b) 作为 §3.8 "The logic to oppose" 的首句。
  - (c) §8.3(f) 改为："Insuring against falling behind is not an exit: the penalty is set by the winner, and insurance accepts the frame of the contest, hedging against losing instead of declining the game (Remark 8.9)."

**重要 5：账本的方法支撑不了它的结论，§5 与 §7 有误记。**
- **问题**：
  - LEDGER §6 只人工读了 69 个 check 单元。321 个 rewritten 单元无人读过：判据是三元组包含率 ≥0.12，或节级词袋覆盖率 ≥0.6。251 个 kept 单元的判据是包含率 ≥0.4。
  - 这个判据看不见"段落大体保留、规范句被删"的情形。我按句计算包含率（全部 641 单元，2,292 句，对 V6.1 全部文件合并计算）：低于 0.2 的有 496 句；kept 单元里低于 0.3 的散文句有 83 句。
  - 上面重要 1、2、4 的损失全部落在 kept 或 rewritten 单元里。
  - LEDGER §5 说 "Only true duplicates and version narrative were deleted"，与事实不符。
  - LEDGER §7 记 "A self-replicating economy carries the switch with it → SUPPLEMENT S5"，但 S5 里没有这一句（grep "replicat|switch" 在 SUPPLEMENT 中零命中）。
- **随机抽样结果**：分层随机抽 62 单元（种子 20261004；22 check、40 rewritten；覆盖 §1–§10 与附录），实质保住 59 个，部分丢失 2 个，真实丢失 1 个（§2.7-p01，见次要 3）。定向抽 12 个单元，丢失 10 处。损失集中在 Ren 的规范句上。
- **修法**：账本改为句级比对（可直接用 `units.py` 的做法）。对所有包含率低于 0.3 的非公式句逐句判读；下表各条或恢复，或写进 §5 并给理由；删掉 §5 那句总括。

| v6.0 位置（账本状态） | 丢失的内容 | 建议去处 |
|---|---|---|
| §0-p03（kept 0.74） | "…and makes those without it fall behind" | §0（重要 1） |
| §0-p04（kept 0.59） | "Decay and renewal belong to growth." | §0、§12.4、导读（重要 2） |
| §9.3-p02（rewritten 0.25） | 广义 E1：劳动、金融、说服；"一人受益仍是博弈工具" | §6.6、§11.3（重要 1） |
| §10.1-p01（rewritten 0.17） | 广义 E1 是范围，狭义是第一步 | §12.1 第 1 条（重要 1） |
| §10.2-p01（check，按重复删） | 摘要中的"we are one … long-term requirement" | §1.2 第 2 条（重要 3） |
| §7.12-p03（kept 0.51） | 落后无法承受，所以先反对逻辑本身 | §3.8（重要 4） |
| 注 7.13 第三条 | 保险接受了竞赛框架 | 核心 §8.3(f)（重要 4） |
| §8.7-p01（kept 0.51） | 哲人王、祭司阶层、开明管家、新大学 | 注 10.8（重要 4） |
| §8.2-p01（kept 0.46） | 生成环的制度形态（共享能力、分布的能动性、多元的观察与批评、维护与修缮、公地的更新）；退化环的闭合句 "fear deepens" | §10.4。现文的退化环停在 "trust collapses"，没有闭合，却称作"环" |
| §5.1-p23（rewritten 0.24） | "Expansion is an anaesthetic for the winning model… Winning does not end the game. The logic itself is the replicator… a self-replicating economy… carries the same switch with it" | 注 5.3 之后；改正 LEDGER §7 |
| §4.3-p04（rewritten 0.23） | "growing understanding without executive authority may change nothing" | §4.3 末或 §12.2。全文以理解为杠杆，这条限制更应留在正文 |
| §10.2-p02（kept 0.43） | Meadows 的层级；"The paradigm can change only if the system is understood" | §12.2，或在 LEDGER §3 说明为何换成阈值说（次要 3） |
| §5.4-p04（rewritten） | 偏好伪装（Kuran 1995）；反向表演性，模型可以使自己失效（MacKenzie 2006） | §5.4 或 X1。后者正是"共享的预测可以避免自身成真"的依据 |
| v6.0 评审已列 | ASTRA 七层、GPT 九步链；计划 §三.6 承诺"ASTRA 一句" | TESTS 研究计划一句；或在 LEDGER 说明不恢复 |

**重要 6：X1 有两个语料键标错，日期也不可查。**
- **证据**：
  - **讲理／讲赢**，以及"争则'我对'，我大于理"：§3.8、§5.4 和 X1 都标 [corpus: meta-attractor]，但 `theories/meta-attractor/README.md` 中没有"讲赢"。原句"合作才讲理，斗则讲赢"出自 2026-05-05《古文一元论与语言的逻辑收敛》，见 `alignment-selection-on-cognition/README.md` 第 32 条与 l.476，以及 `jian-and-wenyan-as-formal-language/README.md` 第 53 条与第 113 条。
  - **五种终局**：§3.6 与 X1 标 [corpus: possibility-space]，该 README 里没有终局分类。原处是 `selfishness-spiral-and-narrative-value-frames/README.md` §"The endgames" 与第 95 条，出自 `01-writings-2025/prompt.md`，2025-02-27。样本量对冲（第 96 条）也出自同一处。
  - **其余核对**：molochlization（alignment-selection l.201；meta-attractor §N；转写稿 00:01:05）正确。"ecology of our cells"（2026-04-12）、我们即是集（2026-05-05）、行动中心、大同是方向而非终点（relational-self 第 12 条）正确。共开、共续、不夺共续（shengsheng；relational-self 第 31 条）正确。"attractor of attractors"（meta-attractor 第 50 条）正确。复利原句（2026-06-03）与博弈设计公理（2024-07-28）正确。
  - **未入表与证据强度**：力之所及，责之所在 没有键，出处是《生生不息论》2026-07-14 本 l.357。LEDGER §7 把改革两难记为"Author's corpus (2025)"，但 meta-attractor README l.1001 写明该句"not yet verified against an original"。可核实的来源只有 10-02 的对话。
  - **日期**：X1 表说"each has its sources and dates"，但表中没有日期列。
- **修法**：
  - 讲理／讲赢改键为 `alignment-selection`（并注 `jian-and-wenyan`）；五种终局改键为 `selfishness-spiral`。
  - X1 表加日期列与 jian-and-wenyan 一行；力之所及标 `shengsheng`（书，2026-07-14）。
  - 改革两难的 2025 归属标"未经原文核实"。

**重要 7：导读有翻译腔和歧义；"逐条对应"只是条数一致。**
- **歧义**：第 5 条"弱化身：……强化身是条件式的"会被读成"弱化／强化 + 身"。改为"化身的弱形式：……；化身的强形式是有条件的：AI 的谱系本身成为载体"。
- **翻译腔**：
  - "压力就闭合于自身"改为"压力就转回来作用于选择本身"。
  - "这些条件的签名"改为"这些条件的征候"。
  - "就是生成的"改为"就成了生生的结构"。
  - "领先是否复利"改为"领先会不会越滚越大"。
  - "能力按一定的决定性转化为胜出"改为"能力越强，胜出越有把握（决定性）"。
  - "这个过程是好的"见重要 2。
- **用词**："宿主"在中文里默认是寄生关系的宿主，会把参与者读成寄生物。Ren 的书用"母体"（《生生不息论》l.113："癌亦增长，而其长竭母体之生"）。建议改为"共同的母体"，或"共同的承载条件"。
- **与 §1.2 的对应**：
  - 第 1 条讲的是"加速、难规制、语言异化"，§1.2 第 1 条讲的是条件、闭合与环路增益（后者在导读"核心"段）。
  - 第 2 条漏了狭隘自我（重要 3），第 3 条漏了"被俘获的评估可以让母体在任何警报之前越过底线"。
  - 判断段第二层漏了"对前沿投入的强制限制"。
  - 导读没有 §0 的"生存是最低要求"。
  - `xref_v61.py` 只比较条数（l.61–66），所以 CHANGELOG 说的 "the guide and Section 1.2 in step" 只是条数相同。
- **修法**：照上改；"逐条对应"改为"与第 1.2 节同序"，或把第 1 条换成 §1.2 第 1 条的内容；xref 改为逐条核对关键词。

### 次要

**次要 1：撤回项大多没有理由，两项其实是改述。** LEDGER §3 的 9 条 "Withdrawn" 中，只有一条带理由（"the figures are derived"）。"Power-seeking emerges where advantage compounds" 实际已改述为 §6.4 的弱化身；"Only changing what winning converts into reverses the direction" 实际已改述为命题 10.3。两条都应归入 Restated 或 Corrected。"Oneness is a gain in one case and a requirement in another" 的理由在 §7.2 正文，账本没有引。**修法**：每条写一行理由，并注明 v6.0 位置。"Corrected" 各条都说明了错在哪里，可以不动。

**次要 2：CHANGELOG 没有记录偏离已批准计划的两处。**
- Ren 批准的是"四个条件"：相对选择、可转换性、决定性、反身闭合（V6.1-PLAN 第一节；记忆 `project_theories_folder` 10-03 条）。V6.1 定义 2.1 写成"三个条件，反身闭合另述"。新写法更干净，也与"元吸引子 = 闭合"一致，但属于对 Ren 已定之事的改动，应写进 CHANGELOG，或回到四条。
- 计划 §三.6 承诺的"ASTRA 一句"未做，也未说明。
- 名称"赢的选择压力"、Γ 为其环路增益、四部结构、两份伴篇、Compact 移入 X10：这些都与 Ren 的决定相符。

**次要 3：未入账的内容改动。**
- (a) v6.0 §2.7 的预测"两个方向的俘获"（captured rules "raise entry barriers against challengers. The second direction is easy to overlook"）。到 V6.1 Test B，"支持抬高对手成本的义务（barriers to entry）"被列为反对本理论的预测；与此同时 §10.1 仍说成功不能买到"exclude entrants"的权利。这可能是为了让检验有区分力而做的正确收窄，但 Ren 第二回路"adopt or be out"里的这一面因此看不见了。
- (b) "滞后效应"预测（撤回一条改变了选择的规则，行为不会完全复原）被删，改成 Test D 的"两阶段"。
- (c) §12.2 把 Meadows 的"参数层干预会被目标与范式未变的系统吸收回去"换成了"越过阈值的参数干预不会被吸收"。
- 以上三处都应写入 LEDGER §3 并给理由。(c) 还要请 Ren 确认：它让"范式"只起"决定动哪个参数"的作用。

**次要 4：对竞赛阵营的口吻。**
- §8.3(d) 与 X8："Its force comes from the combination of stick and carrot."
- X8："proposed in explicitly humanitarian and defensive terms … a real challenge to a path that assumes…"
- 这几句是在信其自述，与 Ren "don't read them as a believer"、"不要把有名当作有力"不合。建议改为："It persuades by promising both security and benefits; both rest on the winner's restraint after the fact, which is what the commitment tests examine." X8 的引述改为 "proposed, in its authors' terms, as humanitarian and defensive"。
- §11.3 E2："The cost is large and, for those who bear it, irreversible"。"large" 是无据的断言，且与上一句"只是决定性一类相对非决定性系统的余量"相抵。改为 "The cost can be large (crux C10)"。
- §7.2 与 X1："this is defensive realism with one more variable"。这把理论等同于现实主义的一支。改为："Readers in international relations will find its nearest neighbour in defensive realism, which it extends by a hazard that endangers its holder and departs from by treating self-help as a selected institution."

**次要 5：语气。** 词汇层面相当干净：没有 "crucial""delve"之类的套话。问题在几处通用的 AI 安全话语和竞赛语法：
- §4.3："If AI cheapens independent correction as fast as control, the certificate holds without budget growth: **AI-assisted correction can win this race**." 竞赛语法。改为 "AI-assisted correction can keep pace"。
- §6.6 与 §12.4："AI is a planetary technology, and its purpose can be shared flourishing." "shared flourishing"是通用语。改为 Ren 的说法："AI is a planetary technology: its effects cross every boundary of those who decide about it, so it is for all, not a means for one side to grow bigger at the others' expense (V1)."
- §10.1："Cooperation is not only a constraint on danger. Its purpose is … medicine and public health, education, science… The joint value is very large; the race dissipates it…" 这是先列好处、后无机制的通用写法。改为机制先行："Taken out of the contest, capability stops being spent on standing: what the race dissipates (Proposition 5.2) becomes available for need, in medicine…, and in the long-horizon work that fragmented incentives under-supply."
- §1.2 第 1 条仍以未经解释的 "carriers" 开头（v6.0 评审重要 7 的修法未落实）。改为 "Where whatever can gain or lose share (carriers) is selected by relative success…"。
- §2.2 Ren 原句截掉了 "and trade everything for winning"，应补回：它正是"单一维度的选择淘汰平衡者"的口语形式。

**次要 6：拼装错误。** §8.3(b) 有 "Proposition Proposition 9.2"；§9 R1 行有 "Theorem Theorem 10.5(3)"。`xref_v61.py` 没有查出。

## 3. 好的、不要改的

- **§3.7 与 §7.2 的"一体"**：三种工作（经验、规范、设计）都经由理解起作用；"What is needed is accuracy, not sentiment"，与 Ren "合作须出于结构而非情感"（relational-self README）一致；"Oneness is what these requirements are requirements of"。上轮重要 1 已彻底修好，不要再往"θ 足够大"方向改。
- **关系自我一段**用了 Ren 的原话（ecology of our cells；我们即是集；万物并育而不相害；和实生物，同则不继），并说明为何不需要个人与集体两极中的任何一极。
- **§5.3**："growth is not the danger; the mind is"，以命题 5.14（可满足的需要有"够了之点"；相对目标没有）为机制，与 Ren 09-25 的裁定一字不差。
- **§3.8**："癌"只有一个定义，且明言不用于人、族群或机构；Ψ "locally rational and systemically false"，并承认 Ψ 部分地被自己做成真的。
- **§6.4**：保留了 Ren 的 "profit and the mindset of winning stand at the end of the reward signal"，以及"人类目前没有协调机制"。同时用 $A_\tau$ 把论断收窄到共同成本的那部分，方向没有变。
- **§3.6**：五种终局的第三种（叙事改变，视彼此为一体）被定为"本文的目的"，这正是 Ren 原文的读法。
- **§10.4**：生成秩序经由共同之物、不经由赢家而延续，拒绝科举式路径；改革两难有两条出路，"neither is a better guardian"。
- **§10.5**：形态按功能推导，不沿个人或集体、集中或分散的轴。
- **§2.2**：Ren 的复利原句与博弈设计公理；§7.1 四回路按回路写。
- **§0 四段**用途先于术语。LEDGER §3 把改述、更正、撤回分开写（上轮重要 3 已修）。

## 4. 查了什么，没查什么

**查了：**
- THEORY.md 全文精读。
- LEDGER、CHANGELOG、README、V6.1-PLAN，DISCUSSION X1、X8（部分）、X10（部分），TESTS §5。
- 上轮 R-v6.0-fidelity，以及记忆中的三份指导。
- 10-02 对话转写（意义相关段落）。
- 语料 README：meta-attractor、selfishness-spiral、alignment-selection、possibility-space、relational-self、shengsheng、jian-and-wenyan、drives、the-fork，按关键词 grep 并读相关段落。
- 《生生不息论》2026-07-14 中文本：grep 力之所及、和实生物、母体、大同。
- 损失：分层随机 62 单元全文对读，另定向 12 单元；全部 641 单元按句计算三元组包含率；260 句低存活散文句与 kept 单元中 83 句逐条判读，可疑者 grep V6.1 全部文件确认。

**没查：**
- 数学与数值，没有运行 `checks_v61.py`。
- SUPPLEMENT 与 EVIDENCE 未通读。
- 语料 README 未通读。
- 英文版《生生不息论》只看了目录。
- 两处日期未核实："what the environment rewards, the mind promotes (2025)"与"trust is an outcome (2025)"。

**同族偏差：**
- 我与起草者同属一个模型家族，最可能在两处放水。第一，把"意思相近的改写"判为"实质保住"：我的句级扫描用字面包含率，正是为了抵消这一点，但判读仍是我做的。第二，把一般的 AI 安全话语当作中性。
- 本文给出的中英文改写同样是模型文字，应以 Ren 的原句为准。
- 判断"Ren 的语域"时，我依据的是 README 与转写稿中的引文，而不是 Ren 本人对 V6.1 的阅读。他尚未读过 V6.1。
