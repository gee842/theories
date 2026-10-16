# R-v6.2 评审：损失与对 Ren 的忠实度

*2026-10-04。对象：`v6.2/THEORY.md`（4 Oct 15:51 构建）、LEDGER 与 `LEDGER-v62-sentences.tsv`、CLAIMS §8–§9、DISCUSSION X1、CHANGELOG、README，以及 `planning/x1-notes.md`、`front-notes.md`、`registers-notes.md`。语料：`~/theories/theories/*/README.md`、`sources/`、`drafts/2026-10-02-friend-conversation/transcript.md`、`sources/16-claude-code-directions/`。未改动任何项目文件。脚本都在 `/private/tmp/claude-501/v62verify/fidelity/`，只用标准库：`recheck.py`、`cmp_tsv.py`、`homes.py`、`sample_kept.py`、`corpus_tags.py`、`quotes.py`，以及 `q1.txt` 和 `q2.txt`。评审者与起草者同属一个模型家族，偏差见第 4 节。*

## 1. 总判断

V6.2 在损失这一维上基本守住了。我独立重算了 V6.1 全部 1,060 句的包含率，并逐条核对了低于 0.4 的 101 句的去向，又从 0.4–0.8 两档随机抽了 38 句。只发现两处实质损失：§2.4 把"AI 可以成为载体"写成了无条件句；§4.6 把自家试验"不支持该机制"改成了"四项中三项成立"。上轮 R-v6.1-fidelity 列出的十四处损失，全部按 LEDGER §6 的说法落了地。

核心里 48 个实质 `[corpus: …]` 标注，逐字核对后，归属错误都已改正。不确定作者的三句改成了"In the corpus's words"，七处四环引文全部逐字。剩下的问题有四处：§6.2 把一段模型编辑过的译文放在引号里当作 Ren 的话；§7.1 的"attractor of attractors"译法可议；§7.3 有一句逐字引文会被冷读者读反；§10.5 的方括号掩盖了转写稿里"听不清"的标记。

方向上，§0、§3.7、§3.8、§5.3、§6.6、§10、§12.4 都忠实于 Ren 的要点：预测→对齐理解→协调、肯定式意义、"我们是一体"、没有更好的守护者、判断博弈而非行为、危险不在增长而在心。全文没有点名国家或企业，也没有通用 AI 安全腔。

但有三处与 Ren 的裁定对不上，应由 Ren 定夺。其一，第二层把停止（E2）与放缓（E3）放在"预测触发"之后。Ren 10-03 的裁定是：若连 AI 不作斗争工具都做不到，就先停下或放缓。其二，"信任是结果，不是前提"一语作为标题，依据的是一行作者不确定的 2025 年提示词；Ren 10-04 的口述却是"没有信任，核查都白搭"。其三，广义 E1 的加粗判据比 Ren 的裁定窄。

此外，英文摘要没有用途与意义；中文导读第二层把 E2 和 E3 的触发条件合成了一个，还有几句读不通。**没有致命问题。**

## 2. 发现

### 致命

无。

### 重要

**I1：第二层的"预测触发"与 Ren 10-03 的条件次序没有对上，§11.3 自己的 E2 定义也与之相抵。**
- **位置**：THEORY §12 主张框与 §12.1 第二层（Trigger、Commitment）；§11.3 "E2: stop"与 "The order"；§5.3（"Call E2 stopping: not building capability of the decisive class while the conditions for governing it are absent"）；§7.2 末两段（"common custody is a preparation, not an emergency"）；摘要；§1.2 第 9 条；导读"判断"第二层。
- **问题**：
  - Ren 10-03 的裁定（`sources/16-claude-code-directions/2026-10-03-v4-direction-cooperation.md`，逐字）是一个条件次序："如果不能合作：优先选择是不把ai本身和对ai的使用嵌入或者变成这种逻辑，即ai不应该以斗争的方式存在，也不能被当成斗争的工具……其次，如果连这个都做不到，我们人类应该有自知之明，先别搞asi，rsi，我们虽然技术条件达到了，但是社会和意识条件依然未达到，应该先停下来，让合作变得可能……要么就把发展速度降低到认知以及通过认知可以做出应当应对的速度以下。其他都是人类绝路啊。"
  - V6.2 的写法与之不同。广义 E1 是"范围"，不是一个步骤。E2 与共同保管要等到"到达决定性位置的估计时间减去保管就位时间，低于登记余量"时才启动，而且要由经认证的纠错者来估计。在那之前，决定性一类的能力可以继续建造。
  - 但 §5.3 与 §11.3 给 E2 下的定义是"在治理它的条件缺失时不建造"，而 V6.2 自己承认这些条件（准确的耦合模型、共享的预测、共同保管）现在都不具备。按这个定义，E2 现在就该生效；按 §12.1，E2 现在不生效。
  - 全文没有出现 Ren 的这一次序。§11.3 "The order" 只按所需信任排了 E1→E2/E3，没有"若做不到，就先停下"的条件结构，也没有"其他都是绝路"的判断。
- **证据**：grep "绝路""先别搞""pause solution""if even"，THEORY、DISCUSSION、CLAIMS、TESTS 零命中。CLAIMS §9 的九项待决里没有这一项。上轮综合（SYNTHESIS §五.2）只请 Ren 决定"强制限制"放哪一层，触发规则本身从未交给他。§7.2 的"a preparation, not an emergency"进一步强化了"现在还不必停"的读法。
- **修法**：
  1. 在 §12.1 开头（或 §11.3 "The order"）用 Ren 的话写出次序，标 [corpus: possibility-space, 2026-10-03]，并给中文原文："If cooperation cannot be had, the first choice is that AI is neither made into the logic of struggle nor used as its instrument (broad E1); failing even that, stop ASI and recursive self-improvement until the social and cognitive conditions exist, or slow development below the pace at which understanding can respond (E2, E3); every other path is a dead end."
  2. 让第二层与 §11.3 的定义一致。一种写法是：E2 作为"在治理条件缺失时不建造决定性一类"，现在就生效；触发规则只管共同保管的强制启动与回滚。E3 按危险类别以覆盖指标触发，保持不变。
  3. 若保留现行设计，就在 CLAIMS §9 新增一项，请 Ren 决定"E2/E3 现在约束，还是等触发"。同时在 §12.1 写明：现行设计偏离 10-03 裁定，偏离的理由是可执行性（命题 5.4(4)）。
  4. §7.2 "common custody is a preparation, not an emergency"改为 "common custody can still be prepared rather than improvised"。

**I2："信任是结果，不是前提"作为标题，依据是一行作者不确定的提示词，与 Ren 10-04 的口述方向相反。**
- **位置**：THEORY §1.2 第 9 条（"need no trust: trust is an outcome of a staged transition, not its precondition"）；§11 主张框；§11.1 第三段及其引文 [corpus: selfishness-spiral, 2025-03-14]；§11.1 第一段（"Confidence in reliable instruments of verification lets parties cooperate without good will"）；导读第 9 条（"信任是分阶段过渡的结果，不是前提"）；CLAIMS D30、D40。
- **问题**：
  - 引文 "Trust is not a prerequisite—it is an outcome …" 出自 `good_bot.md` 的 §4。语料把该文件标为"AI-drafted from Ren's ideas"，X1 与 D30 也标了"attribution uncertain"。
  - Ren 10-04 的录音（他当天交来、并入了 possibility-space 与 alignment-selection 两个 README）说的却是：「无论你是建立核查机制（verification），还是提高透明度（transparency），只要没有信任，这些都白搭」[47:25]；「所以，为什么一开始就认定对方不可信？我们先尝试接触」[41:57]；信任「也要建立在信息可信的基础上」[30:17]。possibility-space README 读作"verification is a condition of trust, not its replacement"。
  - V6.2 §11.1 确有一句让步（"installing them is itself a first step taken under ϖ"）。但标题句与导读把"不是前提"说成了无条件的。§11 主张框只在"where the first steps are of this kind"条件下成立。"lets parties cooperate without good will"一句与 Ren 的"白搭"正好相反。
  - 这一录音在 V6.2 里只用了 [45:06] 与 [32:51]、[18:05]；grep [47:25]、[41:57]、[46:20]、"白搭"，零命中。
- **修法**：
  1. §1.2 第 9 条改为："… need no trust to begin; trust then grows as an outcome of the transition. Verification is not a substitute for it: installing instruments, and reading their reports as information rather than as moves, already needs some prior belief, so the first step is to stop presuming the other's type."
  2. 导读第 9 条改为："……开头几步不需要信任；信任随分阶段的过渡而增长。但核查不能代替信任：装设核查、把核查结果当作信息而不是招数来读，本身就需要一点先在的信任，所以第一步是不先认定对方不可信。"
  3. §11.1 并列引 Ren 10-04 [47:25][41:57]，注明"spoken, from an edited Chinese translation"。2025 年那一行保留为语料的话。§11.1 第一段末句改为 "…lets parties cooperate without good will about what verification can see, and only once some belief has let them install it"。
  4. CLAIMS §8 新增一行，§9 新增一项请 Ren 确认。
  5. 可选：Ren 的「没有办法这样安全地赢」[46:20] 正是本文核心论断的口语形式，可放进 §0 或 §12.4。

**I3：广义 E1 的加粗判据比 Ren 的裁定窄，也比 §6.6 前一句的机制窄。**
- **位置**：THEORY §6.6（"**A use falls under broad E1 when, aggregated over its users, it raises one of these three in a competitive game that concentrates.**"，"these three"指可转换性、决定性、成功向控制的转化）；CLAIMS D19。
- **问题**：
  - Ren 09-26 的原话（`2026-09-26-planetary-technology-and-the-literature.md`，逐字）："if everyone uses ai to write a job application, then it doesn't actually make things easier, but just add another instrument into the pipeline, and the ones who doesn't use ai get left behind. for any game, that is competitive in dynamics and concentrates, ai accelerate it, and if human is a part of the 'instrument(labor)' - ai out compete people"。
  - 他的范例是：人人都用的工具既不改变各人位置，又把不用的人压下去；人本身是工具时，AI 取代人。这两种机制都不必然"抬高三个参数之一"。在比率型竞赛里，所有人加上同一件工具，改变的是各方的有效存量，$r$ 不变。劳动被替代，也不必然提高可转换性。
  - 所以，按加粗判据，Ren 的求职信例子可能不算在内，而这正是他 09-26 否定的那种收窄（"可操作性反射"）。§6.6 前文已写出正确的机制（"leaves each adopter's standing where it was and pushes down those without it; … in labour, it displaces them"），判据却没有吸收它。
- **证据**：D19 自记"the criterion is the fidelity review's proposal (D)"。这条判据是上轮同族评审给出的模型文字，不是 Ren 的。
- **修法**：判据改为："**A use falls under broad E1 when, aggregated over its users, it is an instrument in a competitive game that concentrates: where its adoption by all leaves each where it stood and pushes down those without it, where it displaces people who are themselves the instrument, or where it raises convertibility, decisiveness or the conversion of success into control.**" D19 同步。

**I4：英文摘要没有用途与意义；§0 把意义放在了承诺之后。**
- **位置**：THEORY 摘要；§0 四段的次序。
- **问题**：
  - Ren 的说明（`feedback_ren_why_and_meaning`："Lead high-level summaries, intros and public texts with prediction→shared understanding→coordination and the affirmative meaning"）。中文导读做到了，"用途与意义"一段在最前。英文摘要却从机制开始，以三层判断结束。全文没有"为协调而作的预测"，也没有肯定式意义。多数英文读者只读摘要。
  - §12.4 自己写"The meaning is affirmative, and it comes before the commitment"，§0 的次序却是：预测、生存是最低要求（承诺）、博弈而非行为、意义。
- **修法**：
  1. 摘要首句前加："This is a prediction written for coordination: on the present trajectory the logic of winning carries every participant toward an outcome none would choose, and the prediction has to be shared before coordination becomes possible."
  2. 摘要末尾加："The meaning is affirmative: we are the larger process of becoming, going on through us, and what is opposed is one logic, not growth, competition or any people."
  3. 可选：§0 把 "The meaning is affirmative" 移到第二段。

**I5：中文导读有一处违反 E2≠E3，有两处读者无从理解，另有几句读不通或带翻译腔。**
- **位置**：THEORY 中文导读（第 7–35 行）。
- **问题与改写**：
  1. **第二层把三项的触发合成一个**（违反 E2≠E3）。原文："停止建造决定性一类的能力（E2），共同保管，按理解的节奏发展（E3）。到达决定性位置的估计时间减去保管就位时间，低于登记的余量即触发"。§12.1 写的是 E3 有自己的指标（"E3 activates for a hazard class whose coverage falls behind"；"each is activated on its own indicators"）。改为："停止建造决定性一类的能力（E2）与共同保管：到达决定性位置的估计时间减去保管就位所需的时间，低于事先登记的余量即启动。按理解的节奏发展（E3）：按危险类别，覆盖一旦落后（残余风险不降，或植入缺陷的检出率随能力上升而下降）即启动。停止不是放缓，各有各的指标。"（另见 I1。）
  2. **"在场模型中"读不通**（第 9 条；"本文不主张什么"里的"吸引只在场模型中得证"）。中文读者会读成"在场 / 模型"。改为"在'场'模型中"，或"在选择场模型中"。
  3. **"狭义 E1"没有定义**（第 9 条、第一层（甲）），C0、C2 等标号也没有说明。在第 9 条首次出现处加注："狭义 E1（把一旦交出便无法收回的决策，如动武与核指挥，留在人手中）"。"现实中是否一同合拢是 C0"改为"现实中是否一同合拢，是待检验的猜想 C0"。
  4. **第 3 条整段读不通**。原文："对纠错者的影响若归买者所有，回报随份额的平方增长，在最大的载体中被选择。AI 压低控制成本时，起点合格、按其一定比例增长的独立纠错保得住评估，无单位成本下限时更慢者会输给影响力跟上的载体，依靠被委托侵蚀的人的能力时还须更快。"改为："对纠错者的影响若能买下并归己所有，其回报随份额的平方增长，选择因而把它集中到最大的载体。AI 压低控制成本时，独立纠错只要起点经过认证、增长不慢于成本下降速度的一定比例，评估就不会被俘获；没有单位成本下限时，增长更慢的纠错会被影响力随之上升的载体俘获；纠错若依靠人的能力，而这种能力正因委托给 AI 而退化，还须增长得更快。"同条末句"母体会在任何平均警报之前越过可及的底线"，主语错了（英文的主语是竞赛）。改为"竞赛会在任何平均化的警报响起之前，把母体拖过一条本可触及的底线"。
  5. **第 4 条**。原文："谁在竞赛存活都趋于零；危险不在增长，而在心。"前半句不合语法；后半句缺了 §1.2 的桥接句（"an objective not satiated in the stakes has no point of enough"），读来像突兀的格言。改为："无论谁在竞赛，存活的概率都趋于零；不随赌注而满足的目标没有'够了'之点，所以危险不在增长，而在心。"此外，"剪刀的轴"在上下文中没有出现过"剪刀"，改为"必须赢得的那份能力是两刃共同的支点（本文称之为'剪刀'）"；"收窄设定门槛的目标"改为"把决定这一门槛的目标收窄"。
  6. **第 1 条**。原文："杠杆分通道：分享与扩散压低每个通道，不靠赢得的供给压低决定性增长不及存量比例者（如能力），纠错压低至少同比例者（如规则支持）。"改为："杠杆按通道起作用：分享与扩散在每个通道都压低增益；不必赢得的供给，在决定性增长慢于存量的通道（如能力）压低增益；纠错则在决定性至少与存量同比增长的通道（如规则支持）压低增益。"
  7. **翻译腔**：
     - 核心："改变它的不是更好的玩家，而是改变赢了之后能得到什么"，"改变"重复且句式不对称，改为"出路不在换上更好的玩家，而在改变赢了能得到什么"。
     - 第 6 条："门槛转在少数共同参数上"改为"这些门槛取决于少数几个共同参数"；"证据有点明的缺口"改为"证据的缺口已逐一注明"。
     - 第 7 条："会随赌注与速度侵蚀"改为"会随赌注增大、速度加快而失效"。
     - 第 8 条："也可以是生成的"改为"也可以是生生的"。
     - 第三层："多有点名而未经验证的退路"改为"大多有已指明、但尚未验证的补救之路"。
     - 第 2 条："就是长期的必需"改为"就是长期不可或缺的"。
     - 用途与意义："它正经由我们继续"改为"它借着我们延续"。
  8. **"讲赢"被用来指整个求胜逻辑**（用途与意义首句："'讲赢'的逻辑会把所有参与者带到……"）。在 Ren 那里，讲赢与讲理对举，说的是争执中的话语（"斗则讲赢"），不是整个求胜逻辑（D42 已记为渲染）。首句改为"求胜的逻辑"。讲赢留给第 8 条与 §3.8 的原处。
  9. **用途与意义漏了"人本身就是工具时被取代"**（§0："where people are themselves the instrument, as in labour, it displaces them"）。在"劳动、金融、说服都是如此"前加"人本身就是工具的地方（如劳动），它直接把人替换掉"。
- **证据**：xref 对导读只做双语关键词匹配，第 9 条 67%，刚过门槛，查不出以上任何一处。

**I6：§6.2 把一段模型编辑过的译文放在引号里，当作 Ren 的话。**
- **位置**：THEORY §6.2："The author put the result as a question: "Even if they were perfectly aligned to you … That makes no sense at all" (即使它们是与你完美对齐的结果，完全遵循你的意志，在大家当下的思维方式……中，结果就会好吗？这件事太说不通了) [corpus: alignment-selection]"。
- **问题**：
  - 括号里的中文不是 Ren 的话，是翻译会话把中英夹杂的口语"统一整理成中文"后的编辑稿。alignment-selection README 自标"(zh, spoken, translated)"；10-04 的请求说明也写着"none is verbatim speech"。口语原话（x1-notes 已查出）是"但如果它们是你的完美的aligned的一种结果 的完全遵循意志 … 它能好吗 它它太不make sense了"。
  - 按 §1.4 自己定的规则（"A quoted line is his own words unless it is introduced as the corpus's"），读者会把这段中文当作 Ren 原话。x1-notes 在 Verification 第 5 条已提醒，未落实。
  - 英文删去了"the present Western state of struggle"却没有省略号。删去这一句符合不点名的规则，但删节应当标出。
- **修法**：改为 "The author put the result as a question, here in an edited translation of mixed Chinese and English speech: …"；英文在 "given how everyone thinks now" 后加 "…"。或者直接引口语原话，附英译。D16 补写"the Chinese shown is itself the edited translation"。

### 次要

**m1：§7.1 "the attractor of attractors"对"这是一个meta attractor的attractor"的译法可议。**
- **位置**：THEORY §7.1 "The drive"；CLAIMS D23；X1。
- **问题**：meta-attractor README 自己有两种读法。第 50 条作"The attractor of attractors"；own words 70 的英译则是"*This is an attractor of the meta-attractor.*"后一种把生存压力的信念接到本文标题概念上：它是把系统拉向赢的元吸引子的那个吸引子。这一读法更贴原文，对本文也更有用。
- **修法**：英文作 "this is an attractor of the meta-attractor"，或两种都给并注明。D23 记两种读法，交 Ren。

**m2：§2.4 与定义 2.1 说"训练出的 AI 系统就是载体"，与 §6.4 的"在……条件下成为载体"相抵。**
- **位置**：§2.4 末句 "Trained AI systems are themselves carriers (Section 6)"；定义 2.1 "…and trained AI systems are carriers"；§6.4 "Strong incarnation is conditional. AI lineages become carriers in the sense of Definition 2.1 when…"。
- **问题**：V6.1 原句是"And it can become a carrier itself"（V61-0179）。TSV 把它记为 reworded，实际是丢了条件。导读第 5 条写"化身的强形式有条件"，与 §2.4 相反。
- **修法**：§2.4 改为 "Trained AI systems gain and lose share, and under the conditions of Section 6.4 they become carriers of the pressure themselves." 定义 2.1 的列举改为 "and, under conditions stated in Section 6.4, trained AI lineages"。

**m3：§7.3 一句逐字引文会被冷读者读反。**
- **位置**：§7.3："In the author's words, 'if we don't believe that others will also compete and play this winner takes all game, … this kind of thinking itself creates the trap and reality'"。
- **问题**：前文的论点是"相信领先是决定性的，会选出领先确实是决定性的那个均衡"。引文开头的"if we don't believe"字面意思相反，原文这里可能是笔误。逐字引文是对的，但不加处理会误导。
- **修法**：只引不歧义的片段："In the author's words, the belief that others 'will also compete and play this winner takes all game, even if we don't ourselves', so that 'not participating means losing', is a thinking that 'itself creates the trap and reality'." 放进 CLAIMS §9 第 4 项（引文惯例）。

**m4：§10.5 的方括号掩盖了转写稿的"听不清"标记。**
- **位置**：§10.5 "…makes [centralization or decentralization] dangerous"；CLAIMS D29（"An editorial insertion"）。
- **问题**：转写稿 [01:03:44] 原作 "[centralization or decentralization unclear]"，即转写者对听不清的音频所作的猜测，不是编辑补字。
- **修法**：写作 "[unclear in the recording; probably 'centralization or decentralization']"，或在 X1 注明。D29 改为"a transcriber's conjecture for inaudible speech"。

**m5：§4.6 把自家试验的否定结果改写成了正面语气。**
- **位置**：§4.6 末段 "In the author's pilot experiment three of four pre-specified predictions held, and the first … failed (EV12)"。
- **问题**：V6.1 原句是 "The author's pilot experiment on this mechanism did not support it, one of four pre-specified predictions failing"（V61-0388，TSV 记 1.00 kept）。失败的 P1 恰是本节机制本身。EV12 写的是"No experimental support for the mechanism of THEORY §4 yet"。新句先讲"三项成立"，弱化了这一点。
- **修法**："The author's pilot experiment did not support the mechanism: its first prediction, that conversion capacity rises only where the loop is closed and appropriable, failed, while the other three held (EV12)…"。

**m6：§0 的意义段不再说"不反对增长"；Ren 关于衰败的原话没有引；§12.4 同义说了两遍。**
- **位置**：§0 "The meaning is affirmative"；§12.4 第三段；X1。
- **问题**：
  - V6.1 §0 原有 "The theory opposes one logic, not growth, competition, technology or any people"（V61-0015）。现在 §0 只说 "not to any participant"，"not growth"移到了 §1.4 与 §12.4。依 Ren 09-25 的裁定，意义段应当直接说出这一点。
  - "Decay and renewal belong to its growth" 是改写。Ren 的原话 "I would look at decay as a form of growth"（[00:57:27]；shengsheng own words 92）更直接，全文没有引。X1 表也没有 [00:57:27] 这一行，尽管 §0 的 [corpus: shengsheng, 2026-10-02] 标在这一句上。
  - §12.4 先写 "We are not only our separate lives: we are the larger process…, and that is good"，紧接着又逐字引 Ren 的同义原话，同一层意思说了两遍。
- **修法**：
  - §0 改为 "Its opposition is to a logic, not to growth, competition, technology or any participant…"。
  - §0 引原话："Decay is a form of growth, in the author's words 'I would look at decay as a form of growth' [corpus: shengsheng, 2026-10-02]."
  - X1 补 [00:57:27] 一行。
  - §12.4 删去改写句，只留 Ren 原话。

**m7：§10.2 "What should diffuse" 对开放模型的定调比 Ren 积极。**
- **位置**：§10.2 "Diffusion … so openness is a lever, not a concession … open models are, in the author's words, 'a huge leverage', 'both good and bad'"。
- **问题**：Ren 的立场（alignment-selection 第 210 条，[00:26:09–00:27:58]）是："Open-source intelligence is a direction, not an execution. It is safe only with verification that models cannot be retrained for dangerous uses, and only if the compounding dynamics are resolved." 现文先下"lever, not a concession"的判断，Ren 的两个条件没有写出来。
- **修法**：引语后加 "…: a direction, in his account, safe only with verification that models cannot be retrained for dangerous uses and only where the compounding dynamics are resolved"。

**m8：V1 的渲染加了一层推导，又略窄了 Ren 的话。**
- **位置**：§1.3 V1；§6.6 首句；CLAIMS D17。
- **问题**：
  - Ren 原话："AI is a planetary technology, it should be used for all, not for someone's own interest to fight for bigger … it should be used to benefit everyone and the whole world"。
  - V1 写成 "its effects and dependencies cross every boundary of those who decide about it, **so** it is for all"。这把一个价值立场变成了从外溢事实推出的结论：好像外溢小了，"为了所有人"就不成立了。
  - "at the others' expense" 也比 "to fight for bigger" 窄。
- **修法**："AI is a planetary technology: it is for all and for the whole world, not for anyone's own interest in fighting to grow bigger; its effects and dependencies also cross every boundary of those who decide about it."

**m9：共开、共续、不夺共续。** 源文件（`ssbx-repo/义理/人类命运共同体_共同体之证.md`）作"非夺共续"（sense formula「正续 + 非夺共续 + 共开」），或"¬夺共续"。"不夺共续"是起草者的渲染。改作"非夺共续"，或在 D5 注明。

**m10：LEDGER §3 与 TSV 已落后于最终构建。**
- **证据**：
  - 按现文本重跑 sentcheck，低于 0.4 的有 101 句，不是 99 句。多出的两句：V61-0452 "For classes with an irreducible lag only slowing helps."，TSV 记 1.00 kept nearly verbatim，现为 0.14，实际已改写为 §5.3 "For hazard classes whose manifestation window no testing shortens, $a$ is the only lever left…"；V61-0387 "The same recursion can be generative…"，TSV 记 0.52 "kept, reworded"，现为 0.33，而 LEDGER §4.2 已把它列为更正（"was false"）。
  - 全部 1,060 句中，有 8 句的包含率与 TSV 相差超过 0.1。
- **修法**：最终构建后重生成 TSV；这两句分别改记 reworded、corrected；LEDGER §3 的计数改为 101。

**m11：x1-notes 与 registers-notes 交给整合编辑的两项未处理**（不属忠实度，顺带记下）。
- §6.3 "hidden loyalties (Davidson, Finnveden and Hadshar 2025)"：原报告用词是 singular / secret loyalties。
- §6.4 "a single optimizer of a bounded goal still acquires options … (Turner et al. 2021)"：有界目标的情形不是 Turner 的定理，应作 "compare"。

**m12：§5.3 给"危险不在增长，而在心"加了一条边界，应请 Ren 确认。**
- **位置**：§5.3 "The rule has one boundary: hazardous variety that outgrows contestable coverage is dangerous under any mind, which is why pace binds even a generative order"。
- **问题**：这条边界有机制支撑（定理 5.13），也限定在危险的多样性上，而不是一般的增长。但它为非竞赛的秩序加了一条速率约束。Ren 09-25 恰恰否定过模型"给生产性复利加速率上限"的做法。
- **修法**：在 CLAIMS §9 加一项请 Ren 确认。句中把 "pace" 改为 "pace of hazardous scope, not of need-directed growth"。

## 3. 好的、不要改的

- **§0 前三段**：为协调而作的预测、生存是最低要求、判断博弈而非行为。人作为工具被替代、劳动、金融、说服都写进了机制句。
- **§12.4**：逐字引 Ren 的"we are not just our life … this is great"。"我们是成员"已改为"我们就是"。
- **§3.7**：三种工作都经由理解起作用；"What is needed is accuracy, not sentiment"；关系自我用 Ren 原话（"We are the ecology of our cells"，我们即是集，两处都已逐字核对）；"Oneness is not sameness"。
- **§3.8**：以 Ren 10-03 裁定开篇，附中文原文，逐字。"癌"只有一个定义，且明言不用于人、族群或机构。Ψ 的三重表述。**"Each actor computes correctly; the game is wrong"**（注 3.10）是"判断博弈"最精确的形式化，不要改。
- **§5.3**：命题 5.15 支撑"growth is not the danger; the mind is"，并引书中"癌亦增长，而其长竭母体之生"（逐字，l.113）。
- **§7.1 四环**：七处英文引文全部逐字（`compound_selfishness.md`、`cognitive_lag.md`、Ouroboros 对话），并给出形式对应。注意"regulator lag 不是第四个增强环"。
- **§8.3**："on its merits rather than its prominence"；(d) 改为"It persuades by promising both security and benefits; both rest on the winner's restraint after the fact"；"答立场，不答文件"。竞赛阵营的论证没有被抬高。
- **§10**：
  - 树、"who builds and funds such provision, not who holds it"、理解给所有人而不给一个阶层。
  - 注 10.5 列出被拒绝的守护者，并逐字引 [00:35:16]。
  - §10.4 两环用书中原文，结于恐惧愈深。
  - §10.5 逐字引 Ren 的"decentralization is not the fundamental issue"。
- **归属**：三处作者不确定的句子（局部胜出…、Trust is not a prerequisite…、If we don't solve dominant attractors…）都改为"In the corpus's words"。Ψ2 改引 Ren 原话的逐字片段。X1 表一行一段，附来源、日期，并标出不确定处。
- **CLAIMS §8 的 D 表**（42 条）对核心几乎完整。我逐个对照了 48 个实质标注，缺漏只有 m3、m4、m6 和 I2 涉及的几处。
- **LEDGER §6**：十四处损失全部落地（逐条 grep 并读原文核实），LEDGER §7(a)–(f) 补录了 V6.1 未入账的改动。
- **其他**：核心没有点名任何国家或企业，"中国"只出现在思想史（墨子、康有为、严复）中。Ren 的"favoured"用在了全部五处，另加 CLAIMS 论题一处。通用 AI 安全套话为零（grep stakeholder、flourish、crucial、harness 等）。

## 4. 查了什么，没查什么

**损失**
- 从 `v6.2/` 运行 `src/sentcheck.py`，得 1,060 句，其中 101 句低于 0.4。
- `recheck.py` 按现文本独立重算 TSV 全部句子的包含率，并与 TSV 对比：8 句漂移超过 0.1，另有 22 句已移出核心。
- `homes.py` 对 99 条低于 0.4 的处置，抽出其 home 中的引语片段，在 THEORY、SUPPLEMENT、DISCUSSION、README、TESTS、CLAIMS 中检索。未命中的逐条人工对读，其中约 75 条对照原文读过。
- `sample_kept.py` 用种子 20261004，从 0.4–0.6 档抽 28 句、0.6–0.8 档抽 10 句，每句与最接近的 V6.2 句并排对读。
- 合计核对约 137 条处置，重点看 reworded、moved、merged、withdrawn。发现实质损失 2 处（m2、m5），TSV 失准 2 处（m10）。
- LEDGER §6 的十四处逐条核对。

**Ren 的话**
- 读了三份记忆文件。
- `corpus_tags.py` 抽出核心全部 50 个 `[corpus]` 标注（48 个实质）。`quotes.py` 把 62 条引语在 `theories/`、`sources/`、转写稿和 `_process/` 中做逐字检索（归一化引号与空白），结果见 q1、q2 的输出。命中后对照原始 HUMAN 轮或转写段落：2024-10-30、2024-07-28/29、2025-02-03、2026-03-28、2026-04-12、2026-05-05、2026-06-03/05、09-25、09-26、10-02 转写、10-03 裁定、书 2026-07-14、至善 2026-07-23、SSBX 源文件。
- 读了 X1 表、CLAIMS §8–§9、x1-notes 的 Verification、front-notes 与 registers-notes 的相关条目。

**方向**
- 通读 THEORY 的摘要、导读、§0–§1、§2.1–§2.4、§3.4–§3.8、§5.1、§5.3、§6.4、§6.6、§7.1–§7.3、§8.3–§8.4、§10、§11.1–§11.4、§12.1–§12.4。
- 对照 Ren 10-03、09-26、09-25 的裁定与 10-04 录音的 README 整合段。

**导读**
- 逐句通读，并与 §1.2、§12.1 逐条对照。运行了 `xref_v62.py`（只读）。

**没查**
- 数学、证明与数值。没有运行 `checks_v62.py`，那 188 条断言不在本维度。
- SUPPLEMENT 只读了两处语料段与若干 home；DISCUSSION 的 X8、X10、X11 未通读。
- 没听原始录音，10-02 转写的讲者归属（Ren 为 Speaker B）沿用他本人的暂定说法；10-04 录音只读了 README 引的中文译稿，未核对音频。
- 书与至善的行号只核对了字串存在，没有逐行比对上下文。
- 本目录 `reviews/` 中其他评审（Codex 等）有意未读，以保持独立。

**同族偏差**
- 我与起草者同属一个模型家族，可能在三处放水或失准。
  1. 把模型式改写当作"实质保住"。字面包含率与逐字检索是为抵消这一点，但判读仍由我做。
  2. 对模型式的中文更宽容。我给的中文改写本身也是模型文字，应以 Ren 的语感为准。
  3. I1 与 I3 批评的触发规则和 E1 判据，恰恰出自或得到同族评审的赞同（SYNTHESIS §六把触发规则列为"应保留"；E1 判据是上轮同族忠实度评审提的）。我的批评可能在纠正一个家族盲点（偏好可操作的 if-then 机制），也可能是矫枉过正。所以两项都写成"交 Ren 定夺"，而不是"必须改"。
- Ren 尚未读过 V6.2，本文对"Ren 的语域"的判断，依据是语料与记忆，而不是他对本版的反应。
