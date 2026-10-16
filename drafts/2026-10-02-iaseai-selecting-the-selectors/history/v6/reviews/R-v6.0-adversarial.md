# R-v6.0 对抗性评审：来自结构现实主义、产业组织与"受监管的竞争"阵营的最强反方

2026-10-03。对象：`v6/THEORY.md` v6.0（3,222 行）。依据 `../v6-planning/P6-adversarial-alternatives.md` 检查 v6 是否兑现了 P6 的要求，不重复 P6。遵守作者裁定：不点名国家与企业；反方取论证上最强者；评判博弈与选择，不评判人。未改动任何既有文件。评审者与起草者同属一个模型家族，§10.7 的盲点声明同样适用于本文。

## 总判断

v6 兑现了 P6 的多数形式要求：Moloch、现实主义、Stigler、Pierson 被明确吸收（§2.9）；"一体"写成三条件（§5.5）；继续路径获胜的条件事先登记（§7.11）；三区降为例示、双稳推迟、"分享反转"改为"缩小"；T-A..T-K 入表；两条风险通道分开；盲点声明入正文。这些是实质进步，应保留。

但三个核心问题未解。**第一，可证伪性在形式上满足、在实质上不满足。**§2.7 的五个预测几乎全部被本文自己吸收的理论同样预测，§10.5 所列"替代预测"多为稻草人；定义 7.12 的四个标志宽到任何有效的监管都占其一（责任=后果回源），于是"有效的监管"被重命名为"改变选择"。**第二，§10.1 的判断不是从标准 D 推出的。**D 要求对每条路径——包括 Compact 的捕获与解体——在同一 Θ 上取最坏情形，正文只对继续路径做了这一步；E2 延迟的救命收益也未计入 O1。**第三，若干关键句子超出形式结果所能承载**：§0 的无条件预测与 §5.6 自述的限制矛盾；定理 5.16(1) 把 I′、II 分支并入"买不到持久之物"；引理 3.10 是 Price 方程的恒等式，推不出"必须由看见系统为一的行动者预先设计"；"共同保管先于决定性"与定理 7.7 对核查的否定相抵触。

更根本地：元吸引子框架对 AI 没有特异的诊断力——它对任何递增收益产业都成立。AI 特有的判断全部挂在 (X)(U)(φ) 与 C5/C7 上，而这些是 AI 风险文献的前提，不是本文的贡献。诚实的定位是"一个组织框架加若干新的形式结果"，并把"现在就该做"与"若 C5 成立则必须做"分成两张清单。

## 发现（按严重性）

### 【致命 1】§10.1 的判断不是标准 D 的推论

**位置**：§10.1；§7.11 "Where the decision criteria disagree"；§8.7 表；定义 7.8。
**问题**："Under standard D, the worst case over the justified range includes a rising uncovered share on the continuation path, because no evidence today excludes it." 若 Θ 的边界是"证据未排除"，则 Compact 的最坏情形——唯一的全球保管者被捕获，即对所有人的 O2——同样未被排除。D 第 1 步对两条路径都失败，应进入第 3 步比较最低上界；正文没有做。§7.11 的数值例只给 Compact 配了"解体 2%、回退损失 0.5"，没有"捕获→O2"分支。§8.7 对 Compact 的 D1–D8 全部填"By design; to be tested"，对继续路径填实证（EV3）。定义 7.8 要求"using its own documents and estimates, not assumptions added by the tester"——Compact 没有估计，于是免检；Plan A 有估计（约一年到超级智能），于是被扣分。
**最强反方**：正文把"未测量"对继续路径读作有罪，对自己的设计读作无罪。这正是 Codex 对 v5.2 §6.9/§9.2 的批评，v6 只在 §10.1 末段加了范围说明，结论未动。
**修法**：(a) 把 §10.1 拆成两张清单："warranted now under D"——窄 E1、R1–R3、R5–R8（受监管竞争阵营也接受）；"warranted if C5 and C7 are unfavourable"——E2、共同保管、Compact。(b) 给 Compact 的 Θ 加一行 *capture of the custodian → O2 for all, probability unknown*。(c) 加一句：*"Standard D does not by itself rank the two paths: both fail the tolerance in the worst case over Θ. The ranking rests on a judgment that continuation's worst case is reached by default while the design's worst case requires an additional failure. That judgment is stated here, not derived."*

### 【致命 2】E2 的代价记为"有界、可恢复"，O1 的账只记一边

**位置**：§9.3 E2："Its cost, if AI turns out not to be decisive, is the delay of benefits: bounded and recoverable."；§1.4。
**问题**：延迟的医疗与科学能力造成的死亡不可恢复，按 V2 属 O1。D 保护 O1，却只把 AI 导致的灾难计入，不计延迟导致的死亡。Jones (2024) 正是在这个权衡上工作，正文只引其折现结果。
**最强反方**：十年的 E2 若使可预防死亡延后，其 O1 期望损失可能与所防灾难同量级；不计它，就不是"同一 Θ 用于每条政策"。
**修法**：§1.4 加：*"O1 counts large-scale loss of life from any cause attributable to a policy, including deaths from benefits forgone. Section 9.3 states E2's O1 cost in these terms; its magnitude is crux C9."* 若作者坚持不计，须在 V2 处明说这是价值选择，并接受 Arrow–Fisher 的不可逆性论证在此两边对称。

### 【致命 3】§0 的无条件预测与正文自述的限制矛盾

**位置**：§0 首段；§5.6；命题 5.13。
**问题**：§0："carries every participant toward an outcome none of them wants, including whoever would win." §5.6 自述未证明"every path through a race ends at zero survival"；命题 5.13："A winner that freezes or rolls back keeps positive survival"；定理 5.12 依赖 (X)(U)(φ)，§10.3 称其未测量。中文概要首段同样无条件。
**修法**：*"predicts that, on the present trajectory and under the premises of Section 5.3, the logic of winning carries the participants toward an outcome none of them would choose, and that a winner escapes it only by ceasing to compound (Proposition 5.13)."*

### 【致命 4】定理 5.16 两处超出其引理

**位置**：§5.5。
**问题一**：(1) "If unilateral decisive advantage is not attainable (Branches I′, II and III)… Racing buys no lasting object." I′ 是"决定性但饱和"：赛跑买到的正是饱和点（可生存的二次打击能力），正文自己用了这个例子；II 是"决定性但慢"：仍买到决定性。只有 III 成立，而 III 下买到的是 Arthur 式锁定份额，不是"无物"。
**问题二**：(2) "Durable restraint then requires… common custody"，而 C7 写"enforced cooperation can then hold even where advantage is decisive (Theorem 7.7(2))"。定理陈述说唯一，随文说三条件，二者不一致。"the premise does not justify the race"还混淆了集体理性与个体最优：命题 5.1(1) 自己证明对已赛跑的对手克制从不是最优反应；前提不能为集体赛跑辩护——这就是 Moloch，不是新结果。
**修法**：(1) 限定为 Branch III，I′、II 单列：*"racing buys an object that saturates or arrives slowly; enforced cooperation can hold there."* (2) 定理内写入 C7：*"requires either common custody before decisiveness or detection faster than the time to decisiveness (C7)."* "defeats the race"改为 *"defeats the race as a collective choice; racing remains each actor's best response to a racing rival, which is the dilemma."*

### 【重要 5】五个预测几乎全被已吸收理论同样预测；替代为稻草人

**位置**：§2.7；§10.5；T-B、T-C、T-D、T-E、T-F、T-K。
**问题**：(1) 共变——任何共同冲击（能力冲击、融资周期、政府更替）都产生单因子；现实主义单独预测单因子（威胁），普通竞争单独预测单因子（资本成本），T-E 把"两因子"归给两者之和是拼凑；正文自己"三个对象分别测量"反而预测多因子。(3) 滞后——Pierson、沉没合规成本、官僚惯性都预测；T-D 的替代"无锁定的多极陷阱"不是任何人的立场。(4) 少对多——Olson、Stigler、Bombardini（正文已引）预测相同。(5) 两个方向——Stigler 1971 原文；T-B 写"The theory also predicts the second"，于是任何立场都确认。T-C 的替代"只有能力信号重要"是进攻性现实主义；防御性现实主义（Glaser）容许意图信号，而 §7.12 自称与之只差一个变量——T-C 不能把本文与防御性现实主义分开。T-F 的"unless the pressure is attributed to rivals"是逃逸条款。
**修法**：每条预测先写"哪个已吸收理论也预测它"，只保留区分性残余：p² 标度；限于无沉没成本解释的行为的滞后；T-G 的交互效应。T-B(ii) 改为可失败形式：*"Incumbents oppose non-appropriable correction (mandated access, arm's-length funding) even where it raises rivals' costs more than their own; support for such correction at net cost to themselves refutes the channel."* 若不愿下这些注，按 P6 §5.1，把"one pressure"改为"a shared set of mechanisms"。

### 【重要 6】引理 3.10 推不出加粗句

**位置**：§3.7；中文概要 3；§10.2(8)；§10.8。
**问题**：引理是"单群体内群间项为零"，Price 方程的恒等式。推出"Those rules cannot be discovered by selection among alternatives; they have to be designed in advance, by actors who see the system as one"有三处跳跃：(a) 星球级人口在 Price 意义上不是单群体——企业与国家之间的群间选择正是本文描述的赛跑，命题 3.4(2) 的 Cov(e,φ) 就是群间通道；"一个宿主"（共享外部性）≠"一个群体"（无群结构）。(b) 改变群内支付的规则历史上由受害者联盟（Becker 1983，已引）、自利讨价（Ostrom）、驻守强盗（Olson）产生，无人"看见系统为一"。(c) "the only failure available is the loss of the one"被 §9.6 自己反驳：三里岛→INPO 是从非终结失败中学习，Nye 1987 亦然。
**修法**：保留引理，删"That the lemma leaves only this route is a theorem"。加粗句改为：*"At the scale of one host, integration cannot come from selection among rival hosts. It can come from sub-catastrophic failures, from coalitions of the harmed, and from design. Only design acts before the first catastrophic failure in a class, and design at this scale requires that the system be understood as one. That is the sense in which oneness is a requirement."*

### 【重要 7】"共同保管先于决定性"与定理 7.7 相抵触

**位置**：§5.5；定义 8.1(e)；§7.7；定义 7.12 第 5 项。
**问题**：决定性类别是过程而非物件；"保管"只能是不建造（E2）或共同持有，两者都要核查"没有人单独在建"。定理 7.7(4) 说算力核查的界随算法进步侵蚀，Remark 6.10 说能力不可远预测。保管面对与 Plan A 相同的突围问题，却在定义 7.12 第 5 项"enforcement survives decisiveness"上独享通过——按命题 5.7 没有任何东西在决定性后存活，该项只筛出保管。Copeland 的问题也回来：明天的能力取决于今天训练什么，核查"未来能力的保管"就是核查意图。
**修法**：承认 *"Common custody is a verification agreement with a different fallback; it faces Theorem 7.7(4) in full."* 第 5 项改为"what is its fallback when a decisive position nonetheless arrives (D1)"，并给 Compact 的 D1 一个与 Plan A 同类的估计。

### 【重要 8】良性赢家：命题 7.2(2) 的假设 [A] 被正文自己的先例反驳

**位置**：§7.4；§7.8 表；§9.6；T-I。
**问题**：7.2(2) 假设胜前克制与胜后克制正相关。同节写"The holder of the first nuclear monopoly did not extend its dominance to everything it could reach"，§9.6 写预防战争"seriously argued… and not carried out"——该行动者赛跑时毫无克制，胜后却自缚。Ikenberry 的核心正是赢家自缚因为便宜；§7.8 把良性赢家的 D1 预填"Domination"，恰是 Ikenberry 否认的。T-I 测 AI 评估者的行和，而国家的内部纠错者是法院、选举、新闻；"shared sources"若含国籍与国家拨款，任何本国评估者行和≥1 由构造成立。另外，接受 Olson 的 n=1 结论后，赢家路径在 O1 上按本文模型是安全的，剩下的只有 O2/V3。
**修法**：撤 [A] 或给历史基率；D1 改为"depends on the winner's constitutional correctors"；T-I 纳入宪制纠错者并事先定义 shared source；明写 *"Against a winner that restrains on the host, the objection is V3, not O1."* 应直面 Acemoglu–Robinson 关于精英让步的论证：赢家依赖被统治者的配合，而 AI 是否切断这种依赖才是真正的分歧量——正文用 κ 隐含了它，未命名。

### 【重要 9】固定奖金的 Tullock 模型把创新竞争全部记为耗散

**位置**：§3.6；命题 5.2；§10.2(10) "the joint value that the race dissipates"。
**问题**：Ω 外生。专利竞赛与 Schumpeter 式增长中，竞争创造奖金；定义 2.1 的"可再投入"正是内生增长所依赖的。V5 说产品竞争继续，但前沿能力本身就是产品，正文没有给出区分"赛决定性优势"与"产品竞争"的操作标准。
**修法**：§5.1 加 Ω(E) 内生情形（§8.4 已有凹的 Ω(E)，可对称用于赛跑），报告耗散结论在何种弹性下翻转；给 V5 一条操作边界。

### 【重要 10】θ 是自由参数还是结构的函数（Powell 1991）

**位置**：§3.4；§10.2 "As a point of leverage, the root is understanding"；§2.5 T6 "Its correction is a change in what is selected, not a better argument"。
**问题**：Powell 表明相对收益关切是收益能否转化为优势的函数，即 θ 由 (χ,r) 决定；§7.12 部分承认。若如此，"理解"不是直接杠杆，T-G 的交互预测正是 Powell 的结论。§2.5 说对 T6 更好的论证无用，§0 又说障碍"首先是理解"，需要调和。
**修法**：*"Understanding is a lever only as the means by which actors agree on structural change; it does not act on θ directly where χr is high."*

### 【重要 11】引理 3.3(2) 是刀锋条件，且不是新贡献

**位置**：§3.3；§2.9 第 5 项。
**问题**："invisible to selection"要求等额发生。真实规则的发生按规模不等（固定合规成本偏向在位者），这正是预测 (5) 的筑门槛方向。普遍覆盖是必要非充分，正文却称其为"the formal reason coordination works"并列为新增——这是公共经济学的"公平竞争场"常识。
**修法**：改为"coverage with equal incidence"，从 §2.9 新增清单移入"absorbed"。

### 【次要 12】定义 2.1 第 3 条近乎空洞

"Capacity converts into winning by an increasing success function"对任何 r>0 的竞赛成立。于是"一股压力"等于"任何递增收益竞赛"，对 AI 无特异诊断力；AI 特有内容全在 P1–P3 与 (X)(U)(φ)。应直说。

### 【次要 13】"Ψ is systemically false | Supported"

§2.10 表。"false"依赖 κ 的大小（EV13 未测）；Henrich 等反驳的是个体层面的经济人，而定义 2.5 的 Ψ 是选择偏好的行为，Alchian 的 as-if 已被接受——证据打在稻草上。改为"Interdependence large; the welfare loss from θ<κ unmeasured"。

### 【次要 14】Compact 是命题 4.2 描述的最大转化目标

§8.4 自认"the project, as the largest carrier, has the largest return to influence over its correctors"；"correction outside the project"在星球级没有外面。Remark 8.12 问了，答案是"By design"。应在 C4 下写：*"By Proposition 4.2 the Compact is the largest conversion target the theory describes; its D4 is the hardest case, not a design row."* D5 的"collective input restriction"是多边标签下的强制，与 §7.6 对威慑的批评应对称处理。

### 【次要 15】检验的可行性

T-A：对手发布≈利润压力≈融资时点，三类事件共线，12 家开发者识别力弱。T-C：分离事件罕见。T-J："修辞先于行为"在任何领域都成立（计划先于预算）。T-H、T-K 可行且有用，但 T-H 测的是条件 C5 而非理论，T-K 是对已吸收理论的确认。缺一条能让 C2 失败的检验，建议：*"If by a stated date mandated independent access with arm's-length funding is in force in two leading jurisdictions while incumbents' share has grown, C2 is refuted for that period."*

## 应当保留的

- 命题 3.5 两通道恒等式与 θ 的双扰动识别：把分散的结果放到一根轴上，并给出测量路径。
- 命题 5.7 与推论 5.8：决定性消灭未来之影；纯相对目标无法被对称惩罚约束。干净、新、可检。
- 命题 8.6 三杠杆的分离，以及"分享缩小而不反转"的诚实。
- 命题 5.10 与"位置性部分不可分割"。
- 命题 4.4(7)(8)：拆分按 k^{2/η} 延迟而不阻止；三阶矩而非 HHI。具体、出人意料、可测。
- 命题 6.4：窄 E1 是知情行动者间的严格均衡。这是跨阵营最稳的建议，应作为"现在就做"清单的首项。
- 引理 7.11 的 F1/F2 与 §7.11 的事先登记条件：把比较变成两个可检查的条件。
- §2.10 的对立证据栏、§10.7 的家族盲点、附录 G 的反例登记、§5.6 的"未证明"清单。
- Remark 4.7(4) 的自相关指标；命题 6.11 多分支的如实报告。
- "评判博弈而非行为、不点名"的纪律。
