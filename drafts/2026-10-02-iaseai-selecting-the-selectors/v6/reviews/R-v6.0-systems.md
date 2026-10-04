# v6.0 评审：复杂系统、制度设计与生成性替代

2026-10-03。视角：反馈结构、吸引子与暂态、杠杆点、多中心治理、过渡动力学；并检验正面方案（生成的元吸引子、按功能推导形态、分阶段过渡）是否自洽、非乌托邦、并且经得起本文自己诊断的那些动力。

**对象。** `v6/THEORY.md` v6.0。读了 §1、§2.1–2.8、§3.2–3.8、§4、§5.3、§6.6、§7.4、§7.8–7.11、§8、§9、§10、附录 A.3–A.4、A.8–A.9、C、D、E、G，以及 `../v5/reviews/R-v5.2-systems.md`、`CHANGELOG.md`、`checks_v6.log`。

**算了什么。** 脚本在 scratchpad `review60-systems/`（临时目录，参数写在正文）。
- **S1**：D=1 场模型里"改革—撤回"的最短驻留时间，与 $1/(\varepsilon d)$ 比较。
- **S2**：定理 8.2(1) 的暂态在 logistic 宿主与归一化 Allee 宿主（峰值再生率同为 ρ）下的差别。

## 总判断

v5.2 系统评审的要点大多处理正确：定义 2.2 分三层（F2）；"一个根"改为"一股压力"并给出证伪条件（F1）；驻留时间、补偿回路表、危机窗口进入 §9.4（F8）；Allee 宿主写入 §3.2（F3）；动态指标进入注释 4.7(4) 与附录 C（F5）；keystone 恢复（§4.5）；双稳模型诚实地退入研究计划。§2–4 的系统骨架是稳的。

正面方案是这一版新的重心，也是审稿人会攻击的地方。它有两处结构性缺口，都可以在原处修：
1. **Compact 没有通过本文自己的守护者测试。**它把融资、所有权、评估任命、规则、执行、保管捆在一个机构里，自我固化，并用一个形成方式未说明的"受影响者议院"终止无穷回退。这正是作者划的红线："没有更好的守护者"。
2. **生成之环没有写出它的闭合。**四股各有载体与检验，但没有说明是什么再生产"奖励贡献"这条规则本身，也就是生成秩序的"选择选择者"是谁。第二股的条件 $\chi r\le1$ 与 Compact 的"收入与合同"条款不相容；第三股说的是人的恐惧，压力的载体却是企业与国家。

其余问题是量级与一致性：驻留时间低估 2–16 倍（S1）；§3.2"更苛刻的宿主下结论 a fortiori 成立"对正面结果不成立（S2）；§10.2 仍写"参数层面的干预会被重新吸收"，与命题 4.9(2) 和 Meadows 相矛盾（v5.2 F1 第 4 点没有改完）。

## 一、致命（可在原处修复）

### F1 Compact 没有通过注释 8.12

**位置。** §8.6 Compact 表；§8.7 注释 8.12 与压力测试；定义 8.10 末段。

**问题。**
1. *撤回测试（8.12(2)）。*定义 8.10 说"A closure that cannot state that has left the kernel. The test of any closure is whether it says what would end it"。Compact 表"Amendment and succession: Protections entrenched"，而全表没有一行说明什么条件会终止或解散 Compact 本身、什么条件下它的保管与执行权退回。"No participant can revise a purpose while it is under assessment"还给了冻结修订的工具——谁宣布"正在评估"？按本文自己的判据，Compact 已经离开了可纠正核。
2. *整体化测试（8.12(3)）。*§8.6 说各功能"can be combined in different ways"，候选方案却把全部功能放进一个机构：出资、拥有公共层、任命评估者、定规则、执行、保管决定性能力。§8.2 刚警告"A cooperative order whose loop gain greatly exceeds its damping also resists correction"，Compact 的固化条款正是高增益、低阻尼。
3. *无穷回退在哪里停。*评估者"Appointment by a body in which no provider votes"——谁任命这个 body？三个压力测试（内部人联盟、D8、修订）最后都靠"affected persons' chamber"，而它的形成方式、谱系、行和从未说明。定义 2.2 把"the formation of the minds that will hold positions"列为反身的四条通道之一，这个议院正落在这条通道上。不说明它的形成，它就是改了名字的"更好的守护者"。本文自己的答案应当是：回退不靠任何可信的终端机构终止，而靠每一个节点的行和小于一与谱系去相关。
4. *只排除 provider。*定义 2.1 把国家列为载体，命题 8.3(2) 说规则制定者处于地位竞赛中。评估者的行和必须计入来自国家的转化（命题 8.8 自己写了"from the verifier's own side"），Compact 表却只排除 provider。

**为什么重要。** 这是全文的 remedy test——"约束机制本身的腐化"。Compact 只是候选，但它是唯一展开的候选；若它对自己的测试都不过，§8.7 的表格就是自评。

**修法。**
- 加一行"Dissolution and withdrawal of powers"：Compact 的保管、执行与紧急权各自写明终止条件（可核查的指标，不是日期），并说明哪些功能**不得**同处一个机构（至少：出资公式的修订者、评估者的任命者、执行者三者分离，各有行和证书）。
- 为议院写形成规则：按人口与暴露抽选或多谱系提名，任期轮换，计入它的行和。建议原文：*"The chamber is a corrector, and Section 4 applies to it: its members are drawn by a rule no participant controls, rotate, and its inbound row sum is certified like any evaluator's. The regress ends not at a trusted body but at nodes each of which is certified."*
- "Appointment by a body in which no provider **or single state** votes decisively"，行和计入国家。
- 执行后备"collective restriction of frontier inputs"本身是决定性级别的能力，应归入 Custody 行（k-of-n 释放、条件与日落）。

### F2 生成之环没有闭合，四股之间有不一致

**位置。** §8.2 全节；§8.1"Reward for contribution"；Compact 表"Reward and authority""Financing"。

**问题。**
1. *什么再生产这条规则？*定义 2.2(1) 的元吸引子是"a positive loop runs through the rule"。注释 2.4 说科学、法治靠自己维持的条件而持续——那是正回路：规则奖励贡献→贡献者占据位置→他们维持规则。§8.2 的四股写的却是**约束**（奖赏不可转化、纠错独立、供给不挂钩地位），不是回路。第四股"纠错在共同手中"是负回路。于是生成秩序 = 一条未写出的正回路 + 一条加强的负回路，两者稳定性后果不同：前者给它持久性（也给它整体化风险），后者给它可纠正性。本文没有说出这个结构，所以无法回答它自己的第一问"How does it keep obtaining resources?"——命题 4.3 说纠错是内部供给不了的二阶公共品，生成秩序的纠错由谁供给、这个供给者又由谁选择，正是"选择选择者"的生成版，§8.2 没有写。
2. *第二股与 Compact 矛盾。*条件是 $\chi r\le1$，$\chi$ 为可再投入同一竞赛的份额。Compact 让 provider"earn revenue and contracts by usefulness"：金钱买得到算力与人才，对企业 $\chi\approx1$。Compact 实际切断的是 $b_{ij}$（成功→规则支持）和加了"cap on any one provider's share of essential services"（注释 5.3(2) 的 $\bar K$）。应写明：对企业，$\chi$ 不能压到零而不杀死生产性激励；起作用的是转化为**控制**的 $\chi\to0$、转化为**能力**的上限 $\bar K\le K^\ast$，以及 $b_{ij}$ 的切断。
3. *第三股的层面错位。*"Provision beneath the game"降低的是人对生存斗争的信念；但 §3.1 规则 1 要求"a selection result transfers only where the selected objective is shown to be the actors'"，而压力的载体是企业（生存=份额）与国家（生存=安全）。给人口的体面生活不改变载体的生存函数。第三股要么写明它作用的层面（选民、员工、决策者的个人恐惧→通过 §3.6 的 molochlization 间接作用于载体），要么承认它对顶层载体只有 prestige 通道（§2.3）。
4. *"exit... selection with the opposite sign"*（第四股）与定义 8.1(a) 的覆盖矛盾：引理 3.3(2) 的保护恰恰依赖不能退出共同约束。应区分：可退出 provider 与服务，不可退出共同约束。

**修法。** 在 §8.2 加一段"The closure of the generative loop"，画出两条回路：*"The positive loop: a rule that rewards contribution puts contributors in the positions that maintain the rule. The negative loop: contribution funds correctors keyed to no one. The first gives persistence and is the totalization risk; the second gives correctability. Who selects the correctors is the generative form of selecting the selectors, and Section 4 applies to it; the Compact's answer is the formula levy and the chamber, both of which must themselves pass Remark 8.12."* 第二、三、四股按上面改写条件。

## 二、重要

### F3 §3.2"a fortiori"对正面结果不成立（S2）

**位置。** §3.2 末："none weakens a result that follows"；定理 8.2(1) 与其 [N]（宿主跌到 0.14 后恢复）。

**计算。** 复制者选择在负荷 0.1 与 1 之间，责任裕度 $\Delta=\tau_{\text{eff}}-\nu$，竞赛份额从 0.99 起，ρ=0.05、h=0.08。logistic 宿主：Δ=0.10 跌到 0.15 后回到 0.84，任何 Δ>0 都恢复。Allee 宿主归一化到同一峰值再生率 $\rho_A=4AK\rho/(K-A)^2$：A=0.15 时 Δ=0.10 **永久崩溃**，Δ=0.15 才恢复；避免崩溃的最小裕度 $\Delta_{\min}(A)$ 为 0.086、0.100、0.114、0.130、0.147（A=0.05–0.25）。

**为什么重要。** 更苛刻的宿主加强不可能性结果（定理 4.11），但**削弱**充分性结果（定理 8.2(1)）：(I1)–(I4) 从一开始生效也不够，还需要裕度与选择速度满足一个与 Allee 阈值相关的条件。这正是命题 9.6(3)"过渡期生存"的内容，也是定义 8.10 的核应当计算的第一个对象。

**修法。** §3.2 改为"The impossibility results hold a fortiori for harsher hosts; the sufficiency of Theorem 8.2(1) does not: under an Allee host the transient must stay above the Allee threshold, which requires a liability margin $\Delta>\Delta_{\min}(A)$ [N]"。定理 8.2(1) 的"viable if the host stays above its floor during the transient"改成对 Allee 阈值的条件，并把这个集合叫作过渡的可存续核。

### F4 驻留时间低估，且反应非单调（S1）

**位置。** §4.5 命题 4.10 后"at least of the order of $1/(\varepsilon d)$"；§9.4 Dwell times；命题 9.6(4)。

**计算。** a=c=d=1，从 (0.99, b/d) 起。
- 隔离规则制定（b→0）后撤回：$T_{\min}\varepsilon d$ 在 ε/ζ=0.1 时为 1.17、1.89、3.12、5.23、6.04（R=1.5、2、3、5、10）；ε/ζ=1 时为 4.6、5.9、7.6、10.3、16.2。随 $\ln R$ 与 ε/ζ 增长。
- 提高 d 使 R′=0.5 后恢复：按原 d 计 1.3–1.8（ε/ζ=0.1）、8–11（ε/ζ=1）。
- 只把份额压到 0.3 并维持、规则支持不动（R=5）：永不解除，与命题 4.9(2) 一致。
- **两相。**隔离后头 $\ln R/(\varepsilon d)$ 内，累积的支持仍高于 c/a，份额**继续上升**，之后才下降。

**为什么重要。** "$1/(\varepsilon d)$"只在 R 小、规则制定远慢于采纳时成立；R=10 且两者同速时差 16 倍。两相意味着阶段 3 之后，评估的谱系份额会先升后降，用水平指标读会误判为失败——Sterman 的"worse before better"。此外 $1/(\varepsilon d)$ 只是规则支持这一个慢变量；阶段 2 的慢变量是 $\mathcal K$（引理 6.3 的 $1/\beta_c$），阶段 4 是悬置能力。

**修法。** §9.4 改为：*"In the field model the dwell time is at least $\ln R/(\varepsilon d)$ plus the relaxation of shares, from about one to sixteen times $1/(\varepsilon d)$ in the examples, growing with the captured conversion ratio and with the speed of rule-making relative to adoption [N]. During the first $\ln R/(\varepsilon d)$ the lineage share rises before it falls; a rollback judged on levels in that phase would be premature."* 每一阶段写出自己的慢变量与时间尺度。

### F5 定义 2.2 的使用：三处失守，一层未用

**位置。** §10.2"Two senses of root"；§2.3"the attractor of attractors"；§7.2 与 §10.8"changes the basin"；定义 2.2(3)。

**问题。**
1. §10.2："Interventions at the level of parameters are re-absorbed by a system whose goals and paradigm are unchanged (Meadows 1999; Proposition 4.9)"。命题 4.9(2) 恰恰说使 $s_i<1$ 的边际改革（参数）**不会**被重新吸收；本文最强的杠杆 χ、d、$b_{ij}$ 全是参数；Meadows 没有说参数会被重新吸收。v5.2 F1 第 4 点没有改完。
2. "the attractor of attractors"（§2.3 增益一段）是语录式比喻，与刚建立的三层定义相撞。
3. §7.2、§10.8 的"changes the basin"是对现实世界的第 (2) 层断言，未标 [C]；§8.2 末已经诚实地标了，结论却收回了这份诚实。
4. 第 (3) 层"长暂态"定义后全文未用。而它正是对**当下轨迹**最诚实的读法：C5 说决定性未确立，当下的构型可能是暂态而非吸引子。§2.5、§2.10 从未说当下轨迹处于哪一层。

**修法。** §10.2 改为："Interventions that move a parameter without crossing its threshold are re-absorbed; those that cross it are not (Proposition 4.9(2)). The paradigm matters because it decides which parameters are moved and whether they are held for their dwell time." 删去或标注比喻；§7.2、§10.8 的 basin 加 [C]；在 §2.10 末加一句："The diagnosis is at layer (1) [O]; layer (2) is shown in the model [T]; whether the present configuration is attracting or a long transient (layer (3)) is open, and test T-D (hysteresis) discriminates them."

### F6 功能→形态表：原则对，缺两行，一例有误

**位置。** §8.6 表与联邦例证；注释 8.7。

**判断。** 表的原则真正脱离了集中/分散轴：**凡须对所有人一律适用的，统一（相对选择看不见它，引理 3.3(2)）；凡须纠错的，多元（无单点俘获，命题 4.8）。**"Authority... not by the degree of concentration"是关键句。但：
1. **缺"关于设计本身的学习"一行。**引理 3.10 说行星尺度没有群间选择，规则只能预先设计。但在**同一系统之内**，有界的并行变体加共同评估，是不冒行星级失败就能获得变异的唯一途径——这是多中心治理按功能的理由（Ostrom 2010 的并行实验与跨单元学习），不是意识形态。阶段 5"expansion by evidence"已经暗含它。建议加行：*Learning about the design itself | No second attempt at planetary scale (Lemma 3.10) | Bounded parallel variants with shared evaluation; adoption by evidence.*
2. **缺"谁定标准"一行。**"One standard, many measurers"把标准制定域做成了 keystone（命题 4.8(3)：一个域被俘获可级联），且 Goodhart 直接作用于它。形态应是：标准制定者有行和证书、轮换、预先登记的留出指标。
3. "A common frontier"一行不是从机制推导的统一形态，而是权衡（命题 8.4 的供给不足 vs 命题 4.2 的最大载体）。应写成"merged **accounting and custody** of the frontier, plural lineages inside"。
4. **联邦例证。**"fiscal equalization"是命题 8.6(1) 的 pooling，本文自己证明它在相对选择下只减速、不改方向；做功的是最低标准（普遍约束）与对中心的限制。联邦真正可借的是它的二阶解法：小成员的平等代表与超多数——这正是 Compact"voting not proportional to compute"的先例，本文没有连起来。2021 年全球最低公司税是"one rule for all"及其泄漏的现成实例。

### F7 keystone 在 §9 没有被用

**位置。** §4.5"Keystones, and a window that closes"；§9.4 阶段 3。

**问题。** §4.5 证明：在起源域（开发）仍是 keystone 时，那里的责任与准入改革能解除整个场的俘获；一旦评估、规则、人才形成诸域相互维持，窗口关闭。这是过渡的**次序与期限**，§9 却没有引用。EV3（评估机构转向业界、志愿准入）正是相互转化上升的信号。

**修法。** §9.4 加一段：*"Development is the keystone today (EV3, EV4). Stage 3's mandated access and the separation of reward from authority act at the keystone; the window closes as conversion among the corrector domains rises, which is why Stage 3 is not deferrable to Stage 4's trust."*

### F8 Compact 的两条新回路（第 4 节的俘获机制作用于它自身）

**位置。** Compact 表 Financing；§9.4 补偿回路表阶段 3。

1. 纠错基金"indexed to the field's capability"使纠错者成为能力增长的利益相关方——监管预算依赖，经典俘获回路；E2 之下税基收缩。应索引到各危险类别的**覆盖需求**（命题 4.4 的 $d^\ast$），不索引到前沿能力。
2. 补偿回路表承认"the distribution formula becomes a new prize (Proposition 4.2 applies to it)"，Compact 表却没有相应条款。应：公式定期固定，修订需同一超多数与议院，修订者与受益者分离并有行和证书。

## 三、次要

- **定义 8.10。**有扰动（可预见的错误）的可存续核是 Aubin 的 discriminating kernel（Cardaliaguet、Quincampoix 与 Saint-Pierre 1999），应引。全文没有一个结果用它计算；S2 的 $\Delta_{\min}(A)$ 可以作为第一个实例。
- **命题 8.11(3)。**"Under (X) and (U), capability then compounds"是引入前提，不是推导；复利来自注释 5.3 的 $\chi r>1$，不来自 Tullock 竞赛。齐次零次的论证本身是对的：相对目标对共同缩放不变，所以"够"没有定义。另外 $Y_N$ 由谁设定——需要本身是一个选择器，可被诱导膨胀；注释 5.3(2) 的 $\bar K\le K^\ast$ 应与之相连。"meets E3 by itself"要加条件：$Y_N$ 在覆盖落后太多之前到达（命题 5.13 的暴露）。
- **定义 2.2(1)。**把机制叫"吸引子"是术语错位。加一句：读者应把未引 (2) 的"meta-attractor"读作"候选吸引子"。
- **危机窗口**一段太薄：危机中采纳的预备方案，在 D1–D8 上与分阶段采纳有何不同？紧急采纳最容易产生"不能说出自己何时结束的闭合"（定义 8.10）。
- **Meadows 缺的杠杆：**缓冲（#11）——宿主在地板之上的裕度应作为被管理的量，纠错者的算力储备；存量—流量结构（#10）——算力供应链的瓶颈同时是核查的杠杆与俘获的风险，是设计变量而非背景。
- 命题 4.10 的"[N, systems review]"标注很好；§9.4 的"[C for real institutions]"同样好，应推广到 §7.2、§10.8。

## 四、站得住的部分

- **定义 2.2 的三层**，以及 §8.2 末对"生成秩序是否吸引"标 [C]：这是本版最大的诚实，应保留并贯彻（F5）。
- **引理 3.3(2)→"one rule for all"的推导**：把选择的盲视从病理变成保护，是 §8.6 真正脱离意识形态轴的根据。
- **命题 8.6 三个杠杆**：pooling 不改方向、sharing 按比例缩小、改变赢能换来什么才打开回路；位置性部分不可分割。这是对 v5.2 M2 的正确修复，也是整个正面方案的形式支点。
- **注释 8.7 两阶反向**，以及"merge the frontier, disperse correction"：系统上正确，并且诚实地写了共模失效。
- **§8.2 的自我警告**："a cooperative order whose loop gain greatly exceeds its damping also resists correction"——F1 要求的只是把这句话用到 Compact 自己身上。
- **注释 8.12(4)"理解的分布"**是一条原创且系统上正确的判据：按 Conant–Ashby，理解的分布就是多样性的分布；一个靠他人不理解而维持地位的阶层，是纠错多样性的单点。
- **§8.5 把参与收益、表决权、反支配保护分开**，并承认不可兼得时应宣布不可行。
- **命题 4.10 与"暂停以其间的变化计值"**；**注释 4.7(4)**；**keystone**；**补偿回路表**；**先例表**（尤其 Montreal 与核电业的"动机不变、选择已变"读法）。
- **证伪条件**（§2.7、定义 7.12 的登记预测）与 **G 附录**：反例被登记而不是被吸收。

## 五、待 Ren 决定

1. Compact 是否拆分功能后再作为候选，还是保留捆绑版、但加"解散与权力退回"行与议院的形成规则（F1）。
2. §8.2 是否明写两条回路（正回路给持久，负回路给可纠正），并把"谁选择生成秩序的纠错者"作为 §8 的中心问题（F2）。
3. S2 的 $\Delta_{\min}(A)$ 是进定理 8.2 的注释，还是进研究计划；§3.2 的 a fortiori 一句无论如何要改（F3）。
4. 驻留时间是否按 S1 改写为 $\ln R/(\varepsilon d)$ 加份额松弛，并加"先升后降"的预测（F4）。
5. 功能→形态表是否加"学习"与"谁定标准"两行，多中心是否按功能（变异的唯一来源）而非按名称进入（F6）。
