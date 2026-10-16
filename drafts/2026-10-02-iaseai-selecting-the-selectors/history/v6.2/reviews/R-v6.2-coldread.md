# V6.2 冷读评审：结构现实主义、产业组织与军控视角

*评审对象：THEORY.md（§0–§12，导读除第 4 条与判断外未读）、并按需对照 SUPPLEMENT、DISCUSSION、TESTS、CLAIMS、EVIDENCE。评审者：Claude（与起草者同一模型家族），2026-10-04。本评审未读本轮其他评审，未读 V6.2 以前的版本正文；只为核对是否重复，看过 V6.1 的 SYNTHESIS。独立脚本在 `/private/tmp/claude-501/v62verify/coldread/`（纯标准库）：`algebra.py`、`p101.py`、`dwell.py`、`scissors.py`、`scissors_r.py`、`scissors_monthly.py`。*

## 总判断

作为“记录在案的完整理论”，V6.2 在同类文本中纪律最严：每条结果都在模型内陈述，范围段自陈失效条件，模型与世界分开；我独立推导的十余条核心代数全部成立，三组数值（命题 10.1、S11.4 的驻留、Remark S5.2 的联合模型）从独立重建中逐数复现。没有致命项。问题集中在四处。一是标题层仍有一处丢了承担经验内容的前提：覆盖定理在摘要、§1.2、主张框、导读和 CLAIMS 里都丢了 (residual floor)。二是判断的核心，第二层“预先承诺、由机制执行”的启动，没有说明这一机制在触发时怎样逃过命题 5.4(4) 的执行失败；本文自己的设计把对最强参与者的执行（D5）留给了未定的第三层。三是 “provision beneath the game” 一词三义，[thm] 只对其中一义成立。四是联合模型只在高决定性处算过：按本文自己引用的扩散率，剪刀在 $r\le1.5$ 时根本不合拢，而这一点没有写进主张。作为一篇“论文”，它眼下最受限的是：没有一个阈值被定位到哪一侧，所以形式装置几乎不决定判断。最能抬高它的单项改动，是加一节“当下在哪一侧”的标定（见第五节）。

## 致命

无。我没有找到一条在其模型内为假的形式结果，也没有找到使判断整体失效的矛盾。下面的“重要”项都可以靠写回条件或补一个前提修好，不必撤回论点。

## 重要

### M1　覆盖定理的标题句丢了 (residual floor)

- **位置。** 摘要（"Where contestable coverage falls ever further behind hazardous variety and failure is shared, survival tends to zero whoever races."）；§1.2 第 4 条；§5 主张框（"... survival tends to zero whoever is racing [thm∣prem]"）；导读第 4 条（"覆盖越来越落后于危险的多样性、失败会蔓延时，谁在竞赛存活都趋于零"）；CLAIMS §1 第 18 行。
- **问题。** 定理 5.13 用两个前提：(coverage lags) 与 (residual floor)。标题句只写了前者和 (shared failure)。SUPPLEMENT S5 "What would make coverage lag" 自己写道："Under strict legibility, (coverage lags) is close to definitional for systems beyond human capability, and the empirical content lies in (residual floor)"。也就是说，标题点了近乎定义性的那个前提，丢了承担经验内容的那个。这违反了 §1.4 自定的标签规则："[thm∣prem] proved given premises the statement names"。
- **证据（反例）。** 设 $Y_t=2^t$、$U_t=t$，则 $u_t\to1$，覆盖越来越落后；失败共享；每期不可逆风险取 $0.3u_t/t^2$，可和。存活收敛到 0.741，不趋于零（`algebra.py` 第 6 项）。这个情形满足标题句的全部条件，结论却不成立。
- **修法。** 五处都补一个从句。英文可写："Where contestable coverage falls ever further behind hazardous variety, what it leaves uncovered carries a hazard of irreversible loss bounded below in every period, and failure is shared, survival tends to zero whoever races." 导读写作"……且未覆盖部分每期带有不低于某一下界的不可逆风险……"。§0 的 "If the hazards of capability outgrow the correction that can contest them" 已是条件句，可以不改。

### M2　第二层的“预先承诺、由机制执行”没有推出它能逃过执行失败

- **位置。** §12.1 第二层 *Commitment*（"Activation is committed in advance and executed by mechanism ... so a collective decision taken there would inherit the enforcement failure it was meant to prevent [thm∣prem]"）；§12 主张框 Why；§7.2 末两段；DISCUSSION X8 冲刺与保管对照表的 D5 行（"execution first by its host jurisdiction, then a coercive fallback compared, not settled ... the hard case remains"）；§10.5 末段（"Where execution through a host jurisdiction fails against the strongest participant (D5), what remains is the coercive restriction of frontier inputs, which the design does not settle"）。
- **问题。** 触发时，领先一方面对的正是命题 5.4(4)：$p_d\to1$ 且 $D\ge C$ 时，只能维持阶段博弈均衡内的克制。事先作出的承诺，是对触发时行为的许诺。它若不在触发前改变 $p_d$ 或改变届时的制裁，就受同一条件约束；这正是命题 5.8 与 7.3(3) 用来批评“良性赢家”的承诺问题。推论 5.7 列出的手段只有两类：(a) 改变前提，即不建、保管已持有、检测快于突破；(b) 抬高 $\bar p_d$，即能在成功后存活的制裁、目标。“预先承诺”不属于其中任何一类，除非它在触发前已经装好其中某一项。本文自己的设计对 D5 的回答，是第三层“比较而不定论”的强制限制。所以，第二层启动恰恰在最需要它的那一方面前，可执行性落在第三层。文中 [thm∣prem] 的推理没有写出这个前提。
- **证据。** 命题 5.4(4)、推论 5.7(a)(b)、命题 5.8 原文；X8 的 D5 行；§10.5。
- **修法。** 把前提写进 *Commitment*，可写："Activation executes by mechanism only to the extent that its means are in force before the trigger: compute and weights already under controls that custody holds (hardware-enabled limits, escrowed keys), so that at the trigger the deviation it prevents is no longer available (Corollary 5.7(a)), or a sanction that survives success already in place (5.7(b)). Where neither is installed, activation against the leading party rests on the coercive fallback of tier 3." 同时在第一层加一项，或把第一层第 2 项从“研究与试点”扩展为“在触发前装好的执行手段”，因为 EV17 说这些手段已有原型、尚未部署。另外把“执行手段是否在触发前就位”登记为 C7 或 C4 的一部分。这样改，第二层的理由更诚实，也更强：竞赛前提成了现在就装执行手段的理由，而不只是现在就作承诺的理由。

### M3　第一层（甲）第 4 项里的“启动承诺”并非与所有分歧无关

- **位置。** §12.1 第一层（甲）第 4 项（"... and the commitment to activate taken now"）；TESTS §3.1 第 (4) 列与第 65 行（"Under N1, a criterion that values speed highly can still accept every item here, since none of them stops or slows anything"）。
- **问题。** 第一层（甲）的定义是："A step belongs here only if its justification does not depend on how any crux comes out"。启动承诺意味着触发时启动保管与 E2，也就是承诺停止，这与 TESTS 第 65 行“没有一项停止或放慢任何东西”直接矛盾。它的理由也依赖 C4：按命题 4.3，保管机构是最大的转化目标，若它在压力测试中比它要防止的情形更糟，启动承诺就是有害的。TESTS 中第 4 项的 C4 格只谈“准备”的成本，没有谈承诺。
- **修法。** 第一层（甲）第 4 项保留设计、机构、指标、启动规则的登记，以及按 D1–D8 的压力测试。“启动承诺”移入第二层的 *Commitment*（那里本来就有），写成以保管机构通过事先登记的压力测试为条件。同时改正 TESTS 第 65 行。

### M4　“provision beneath the game”一词三义，[thm] 只对其中一义成立

- **位置。** §2.2 黑体句；命题 5.17 的支点；§8.2 G5（"provision of the conditions of a decent life sits beneath the game"）以及"G5 holds down the won share, the pivot of the scissors"；§10.1 "Provision that does not become the system"；§10.4 第三股（"Shared provision, good enough, distributed and replaceable: the $k_0$ of the loop gain"）；§12.1 第 8 项（"Shared provision of useful services ... Provision not won in the contest lowers the won share on which the scissors turn (Proposition 5.17) [thm]"）。
- **问题。** 在模型里，$k_0$ 是流入竞争者决定性存量（能力）的、不按名次的流入；$\omega=\kappa\Omega/(\kappa\Omega+nk_0)$ 是竞争者能力中必须赢得的份额。给人的体面生活供给（G5），以及给使用者的服务，只有在进入竞争者的决定性存量时才降低 $\omega$。否则它们通过驱力起作用（C8，[conj]），或通过降低被争夺的赌注起作用，这在模型里是另一个参数。§10.4 自己已经分了三层："for persons ...; for states ...; for providers, $k_0$ is literally capability not won: a common layer of compute, evaluation infrastructure and services"。但 G5 的“逆转复利与地位”和第 8 项的 [thm]，是对三义合在一起说的。
- **修法。** 在 §2.2 首次出现处把三义分开：(a) 给竞争者的能力供给 $k_0$，如公共算力、公开评估设施、公开的技术知识，经 $\omega$ 起作用，[thm]；(b) 给人的体面生活供给（G5），经驱力起作用，C8，[conj]；(c) 由多家提供的基本服务，经依赖上限起作用，D5。第 8 项的 [thm] 只挂在 (a) 上，G5 的行注明作用经由 (a) 还是 (b)。“树”的意象可以同时覆盖三义，但形式内容只属于 (a)。

### M5　联合模型只在高决定性处算过；两刃极不对称，这一点没有写进主张

- **位置。** §5 主张框（"in one reduced model the first two close together [num]"）；§5.5 Scope；Remark S5.2（"Over 96 settings of ... decisiveness (2 and 3) ..."）；摘要与 §1.2 第 4 条对两刃的对称表述。
- **证据。** 我独立重建了 S5.2 的第一种设定（`scissors.py`），逐数复现：$\omega<0.551$；目标刃单独 0.556；突破刃单独永不合拢（$\omega=0.9$ 时 $p_d=0.449$）；交点处 $\Gamma=1.32$、$\Gamma_\delta=0.92$、$p_d=0.100$；$\theta_0=0.4$ 时 0.57。随后扫描决定性 $r$（`scissors_r.py`，其余参数照原设定）：$r=1$ 时，$\delta_f\in\{0,0.05,0.1\}$ 都永不合拢；$r=1.5$ 时只在 $\delta_f=0$ 合拢（$\omega=0.952$）；$r=1.7$、$\delta_f=0.05$ 时为 0.975。改用 Remark S2.5 自己的月度示例率（$d=0.02$–$0.05$，$\delta_f=0.05$–$0.1$，`scissors_monthly.py`），合拢要求 $r\approx3$–$4$ 以上。原因很简单：在 S5.1 的阶段博弈里，$p_d\approx0$ 时克制失效的工作权重是 $\theta_{\rm rep}(0)=-0.901$，对应 $\Gamma_\delta\approx0.924$；只有 $(1-\beta)r\omega\delta d_K/(1-\delta(1-d_K-\delta_f))$ 能达到约 0.92 时剪刀才合拢。另一方面，联合阈值与目标刃单独的阈值只差 0.005；第二种设定里，检测加快一倍，相遇只从第 59 期推到第 60 期。
- **问题。** 主张框里的 [num] 没有写出自己的条件。按本文自己对现状的读法（领先短、扩散快），这个区域恰恰是剪刀不合拢的区域。与此同时，计算出的不对称是一个被低估的实质结果：在这些模型里，执行的杠杆是 $\omega$（经由地位价格），而不是检测速度。
- **修法。** 主张框改为："in two reduced models, at decisiveness well above one, the blades close as the stakes outgrow fixed provision, the objective blade doing nearly all the closing; at $r\le1.5$ with diffusion they do not close"。JX 的扫描加上 $r\in\{1,1.5\}$ 与 S2.5 的 $\delta_f/d$ 比。§5.5 加一句政策读法："在这些模型里，随赌注增长的供给让两刃都不动，加快检测几乎不移动交点；这不减少 Remark 5.5 在突破刃起约束作用时的地位"。摘要可以保持两刃并列，但 §1.2 第 4 条应注明“联合模型中目标刃主导”。

### M6　第三层理由 (i) 把“有条件的推导”说成“推导出的不可逆损失”

- **位置。** §12.1 理由 (i)："The asymmetry is between reversals that are designed and not yet tested and losses that are derived and cannot be undone."
- **问题。** 列出的现状损失，都是在本文自己当作分歧的前提下推出的：定理 5.13 依 C1 的两条前提，命题 4.13 依 (e)/(clock)，命题 5.8 依决定性（C5），引理 6.3 依 $q_L$。设计的逆转依 C4。所以两侧都依赖未测的分歧，真正的不对称在于“一旦发生，有没有点名的逆转”，而不在于推导与否。此外，按引理 8.2，设计解散后的退路继承了现状的失效模式，所以排序实质上取决于 (bounded own risk)，也就是 C4。原句的说法会被敌意读者当作修辞上的偏向。
- **修法。** 改为："The asymmetry is between failures that, if they occur, have a named reversal not yet shown to work (C4), and failures that, if they occur, have none; whether either occurs turns on cruxes on both sides (C1, C2, C5 for continuation; C4 for the design)." 每项损失的不可逆性保留 [thm∣prem]，排序保留 [val]。这样改，理由不变弱，反而更难反驳。

### M7　两个最强的当代反方没有被正面回应：“作为普通技术的 AI”与 GPT 扩散理论

- **位置。** §8.3、§8.4、DISCUSSION X8 与 X1、TESTS 的 C1 与 C5。
- **问题。** (a) Narayanan 与 Kapoor（2025，"AI as Normal Technology"）认为，影响按扩散与机构采纳的速度到来，而不是按能力的速度；不存在决定性优势；应取韧性，而非防扩散；防扩散会集中权力、制造单点失效。这同时冲击诊断（C1：部署慢则覆盖跟得上；C5）和 G4、保管。(b) Ding（2024，*Technology and the Rise of Great Powers*）的 GPT 扩散理论认为，通用技术带来的大国优势来自扩散能力，而不是前沿领先；这直接质疑 (decisive) 前提把前沿领先当作决定性。本文已有回应所需的全部材料：分支 III、C1/C5 有利时第二层失效、Remark 10.3 的两阶、守护者测试；扩散在本文中本来就是杠杆。但两种立场都没有被点名，也没有按“最强形式、剩下什么、什么能证明它足够”的格式处理。按“对反方取其最强”的标准，这是缺口。
- **修法。** X8 加 (h) "Normal technology and diffusion"：最强形式即上述两条。剩下的：增长通道按部署速度仍然起约束作用，定理 5.13 的前提可以按类测量；保管的集中问题由 Remark 10.3 与守护者测试回答；它们自己的韧性处方就是 G1、G3、G6。什么能证明它足够：C1 与 C5 都测得有利，此时第二层失效，而判断已经登记了这一点。§8.3 加一句，§8.4 加一行。顺带指出：GPT 扩散理论支持本文“扩散是杠杆”的结论（S2.5：阻断扩散时 $r>1$ 即足以 $\Gamma>1$）。

### M8　广义 E1 点名的领域写成了无条件，而本文自己的判据是有条件的

- **位置。** §0（"In a contest decided by relative strength, an instrument that every contestant adopts leaves each adopter where it stood and pushes down whoever lacks it, and where people are themselves the instrument, as in labour, it displaces them. No single use shows this; the aggregate does, in labour, finance and persuasion as much as in force"）；§6.6（"Broad E1 is therefore AI not used as an instrument in any contest that tends toward dominance or concentration, in labour, finance and persuasion as much as over shared conditions"）；导读第 1 段（"劳动、金融、说服都是如此"）。
- **问题。** §6.6 自己的判据是有条件的："A use falls under broad E1 when, aggregated over its users, it raises one of these three in a competitive game that concentrates"。Ren 的原话也是有条件的："for any game, that is competitive in dynamics and concentrates"。命题 3.9(2) 与 S3.2 还表明：奖金随共同能力增长、$(1-\beta)r<1$ 时，向前看反而放宽自我。许多市场用途正是这种增长奖金的博弈：人人采用会压低价格、扩大产出，抬高共同回报。“每个采用者留在原位”对比值竞赛里的地位成立，对福利不成立。“在劳动中取代人”也没有回应产业组织与劳动经济学的最强反方，即任务创造与互补（Acemoglu 与 Restrepo 2019）。这不是反对“判博弈，不判行为”，而是要按这条原则办：先表明那个博弈是集中的、奖金固定或是地位性的。
- **修法。** §0 与导读改为“……在劳动、金融、说服中，凡是博弈按相对实力决定、奖金不随人人采用而增长之处都是如此，需要逐个市场来表明”。§6.6 加一句回应产业组织的反方：共同回报与消费者剩余；命题 3.9(2) 给出了条件。劳动处引任务创造的文献。由于广义 E1 是判断的“范围”（§12.1），这一处属于标题层。

## 次要

- **m1　“if growth and change are favoured”没有一句说明为什么这样附条件**（摘要、§1.2 第 2 条、§3.6、§12.4）。这是 Ren 的原词，应当保留。建议在 §3.6 补一句，把它接到已有结果上："Under growth and change, new hazard modes keep arriving (the growth channel of Section 5.3), so anticipation has to keep pace without end; were variety to stop growing at need, coverage could catch up (Proposition 5.15). That is why the requirement is long-term, and why it is conditional on favouring growth and change." 这是我的解读，请 Ren 确认。
- **m2　“accelerate”和“success raises the stakes”没有对应的结果。** §5 主张框写"The conditions of winning accelerate the contest ... [thm]"，§12.4 写"success raises the stakes"与"it accelerates the contest"。各模型中赌注都是外生的（命题 5.17；S5.2 中 $\Omega_t=e^{0.05t}$），§5.1 也没有一条结果陈述速度上升。修法：引命题 5.15（不饱和目标下强度与赌注成正比）与 5.2，写明“随赌注增长”；把 "success raises the stakes" 改为 "as the stakes grow"。
- **m3　§1.2 第 6 条 "The premise therefore cannot justify that course" 没有标签。** "therefore"读起来像推导，而推论 7.4(3) 是 [val: V1–V3]，§7 主张框也标了 [val]。修法：改为 "cannot, on V1–V3, justify that course"。
- **m4　命题 10.1 仅凭正文不可复现。** 收益结构没有写全：合伙者胜时每人得 $\Omega_c/n_c$ 而不是 $\Omega$；每人按总强度承担 $\ell$；赛者胜时合伙者承担 $L_b$。我从 $R=0.140$ 反推出这一结构，复现了全部数字：$T=0.0017$，信任门槛 0.6106，所需合伙努力 0.0054、0.0349、0.1406、0.4898（`p101.py`）。修法：在 S10（最好也在正文）写明收益；注明数字来自 v4.5 的旧代码。
- **m5　“change what winning confers”时宽时窄。** §2.2 把分享与扩散都算进去；§12.1 的范围句又包括“降低决定性”，而决定性是能力如何转化为胜利，不是赢了得到什么。§3 主张框 "only a change in what winning confers corrects it [thm∣prem]" 的真假取决于取哪一义。修法：在 §2.2 定义一次，写明它覆盖 $\beta$、$\kappa$ 与 $k_0$、扩散、$\chi$ 和地位奖金；降低 $r$ 作为同一博弈上的并列杠杆列出。
- **m6　摘要的执行句缺条件。** "Restraint is enforceable only while each deviation's chance of becoming decisive stays below a threshold" 只对 $D_i>v_i$ 的偏离成立，而且是在完全监测之下。补半句即可。
- **m7　§10 主张框把一个综合性主张标成 [thm∣prem]。** 指 "The way out of an optimization trap is a change in what winning confers, neither a better optimization ... nor the abolition of selection ..."。它是概括，不是定理。修法：标 [def] 或 [val]，并写出它概括的结果（Remark 3.10、命题 10.2、引理 3.11）。
- **m8　“host”在一句里有两个定义。** §3.1 写的是 "the body every carrier lives in ...: the part of the shared conditions whose costs do not return to their source"，而 "Every actor persists only while the host does" 只对前一义成立。修法：写成“the body every carrier lives in; in the models, the part of it whose costs do not return ...”。
- **m9　Remark S2.5 的量级在正文里被低估。** 在现有扩散率下，$\Gamma>1$ 需要 $r\approx2$–$6$；扩散被阻断时 $r>1$ 即足够。这让 §8.2 关于出口管制的那句话有了量级：管制把复利门槛从 $r\approx3$–$6$ 降到 1。建议在 §2.2 "What the loop gain does not decide" 或 §7.2 加一句。
- **m10　速率律可以推广，从而更稳健。** 设影响能力的边际成本对 $q$ 是 $\eta$ 阶正则变化的，选定水平就是 $q^\ast\sim(\gamma d)^{-1/\eta}$，于是 $G_{\rm ev}$ 的培育项 $\propto q^\ast/d$，门槛仍是 $\alpha_{\rm ctl}/(1+\eta)$，其中 $\eta$ 是边际成本的渐近弹性。若边际成本比任何幂都陡（如指数型），$q^\ast$ 只按 $\ln$ 增长，任何正的纠错增长率最终都够。可以在命题 4.5 的 Scope 加一句。这样，前一轮评审认为最可单独发表的结果就不再依赖幂函数形式，经验靶子也更清楚：影响能力的边际成本弹性。

## 好的，不应改的

- **陈述纪律。** 结果在模型内陈述；各处 Scope 自陈失效；S13 的接口、S14 的反例、Table 7.1 的 † 标记；“What is not claimed”一节。结构现实主义读者最常抓的“把模型当世界”，在这里几乎无处可抓。
- **命题 3.9 与 Remark 3.10 的“两种错误”。** “持有的边界错误”与“复利下准确的工作目标”分开，"Each actor computes correctly; the game is wrong" 有确切条件。这是把 Powell 1991 往前推了一步，也是“判博弈，不判行为”最好的形式化。
- **逐通道的杠杆。** 比值通道与水平通道分开："Trees for capacity, correction for rule support, sharing and openness for all"。还有“阻断扩散抬高想利用的那个增益”。
- **命题 4.3、4.5、4.6。** $p^2$ 标度、速率律的两半、拆分因子与份额高阶矩，以及委托侵蚀纠错者本身。
- **执行条件 (14) 的分解。** Remark 5.5 与命题 8.6 的门槛完全对应（我已核）；推论 5.7 对手段的分类。
- **对竞赛派的回应。** 取最强形式，用机制作答：冲刺之后冻结，靠负担与持有者来回答；良性赢家，靠 $\kappa_W$ 与 C13，并引 Ikenberry、Kindleberger、Gilpin。没有抬高它们，也没有回避。
- **判断的分层。** 第一层（乙）把举证责任放在撤回一方，第二层的释放读自己的指标并要求驻留。层次按理由的种类划分，而不是按谁接受。
- **掩蔽型偏差。** 准入写成能力门槛，并成为 E2、E3 来自对齐内部的最强理由。
- **规则。** 我扫描了正文，没有点名任何国家或企业。E2 与 E3 始终分开。意义是肯定的。

## 它是一篇好论文吗：最受限之处，与最有效的单项改动

它是一份出色的理论记录，但还不是一篇好论文。主要贡献（我数下来五到六条：环路增益与逐通道杠杆、地位价格与两种错误、选择选择者与速率律、执行条件的分解、嵌套奖励回路与掩蔽、一体与预先整合）埋在大约同样多的、结论近于前提的结果里，例如命题 4.13、定理 5.13、命题 6.4(1)、7.3(1)。敌意审稿人会说：形式装置几乎不决定判断。第一层与第一层（乙）靠保护标准、提前期和举证责任就能成立；第三层按本文自己的规则落到“判断”；只有第二层的启动真正需要装置，而它恰好有 M2 的缺口。

**最受限之处：没有一个阈值被定位。** $\Gamma$ 没有估计；Table 7.1 每一行都没有“我们在哪一侧”；诊断靠宣言中的征候。本文自己的数字（S2.5、S5.2，以及我的扫描）其实已经暗示了答案：按现在的扩散率，能力通道的复利与剪刀大概不合拢，除非决定性很高；最可能已经越线的，是当前集中度下的规则支持通道（领导者份额 0.6 时，培育转化的矩约为对等时的 3.6 倍）、增长通道（C1）和掩蔽类（C12）。

**最有效的单项改动：在 §7 加一节“当下在哪一侧”（约 1.5–2k 词）。** 对 Table 7.1 的每一行，用登记册给出参数的证据区间：能力通道的 $r$、$\omega$、$d$、$\delta_f$；规则通道在当前份额下的 $\chi$ 与矩；$x_{\rm ev}$；EV9 的效率侵蚀。然后在这些区间上运行 S5.2 的联合模型和速率律，逐行写出“哪一侧、多确定、什么测量会改变它”。这一节会把诊断从“征候”变成“定位”，也会表明判断的分层与证据吻合：第一层（乙）针对的，正是最可能已越线的那几行；第二层针对的，正是证据显示尚未越线、但一旦越线就不可逆的那一行。它不需要新的数学，所需机器都在 S2.5、TESTS §7 和 JX 里。

## 短论文（约 12–15k 词）：必须包含什么，可以留给 V6.2 什么

**必须包含**（括号内为建议篇幅）：
1. 问题、谜题、一个想法（“改变赢了得到什么”）、不主张什么、标签（1.5k）。
2. 定义 2.1（三条件加闭合）；命题 2.2(1)(2)；逐通道杠杆（S2.4）；Remark S2.5 的量级；定义 2.4 的三种对象，一段（2k）。
3. 命题 3.5 的恒等式；命题 3.9 两种情形；Remark 3.10；引理 3.3(1)；引理 3.11，以及“一体”作为预先整合的必要条件，一段，附 m1 的接法（1.5k）。
4. 命题 4.3、4.5(1)(2)、4.6(1)、4.11；命题 4.13 一句（2k）。
5. (14) 与命题 5.4(1)(2)(4)；Remark 5.5；推论 5.7；命题 5.17 连同 M5 的条件与不对称；定理 5.13，三个前提写全（M1）；命题 5.15；E2 与 E3 的定义（2k）。
6. 命题 6.1；命题 6.7；Remark 6.8；窄 E1 一句（1.5k）。
7. 压缩版 Table 7.1（九行三列）；推论 7.4，标 [val]；第五节建议的“当下在哪一侧”，压缩成一张表（1.5k）。
8. 替代路径一张表，含 M7 新增的“普通技术与扩散”；良性赢家与冲刺各一段（1k）。
9. 三层判断，按 M2、M3 修正；关键分歧 C0、C1、C2、C5、C9、C12、C13；什么测量会改变判断（1.5k）。

**可以留给 V6.2**：Ψ 的完整论述与四个回路；命题 3.6、3.7、3.12；Remark 5.3；命题 5.9、5.10、5.12、5.16（短论文里各留一句）；命题 6.2–6.5、6.9 与混沌注；场模型命题 4.10、4.12；§8 的全部替代路径与耐久测试；§9 的要求表（短论文以“Table 7.1 反读”一句带过）；§10 的设计表（短论文只留 G1–G7 与“经由共有之物而非赢家”一段）；§11 的轨道、准备度与驻留（短论文留“棘轮”与“信任是结果”两句）；Meadows；语料引文只留两三句（"trade everything for winning"、"growth is not the danger; the mind is"、讲理与讲赢）；完整的符号表。

## 检查了什么，没检查什么

**通读。** THEORY §0–§12。导读只读了第 4 条与判断部分。

**独立推导（全部成立）。**
- §2–§3：命题 2.2(1) 的秩一 Perron 根，400 组随机多通道、无一不一致；2.2(2)；2.2(3) 中 $\Gamma_\delta<\Gamma$；命题 2.3(1)、(2)(i)(ii)，以及 $\Omega=gS$ 时的不稳定条件；命题 3.5(3)；3.6(1) 的均衡强度；3.7 的耗竭门槛；3.9(1) 的 $\theta_\Gamma$ 与 3.9(2) 的比值 $(1-\beta)r$（无限期几何和）；Remark 3.10 的 0.381 与工作权重 0.15、−0.15、−0.53、−0.80。
- §4：命题 4.5(2) 速率律的指数；4.5(4) 的拆分因子与矩；4.6(1)。
- §5：命题 5.2(1) 与 $\theta_g$；5.4(1)(2)(5)；Remark 5.5 与命题 8.6 的门槛相等；5.8 的对数份额；5.16(1)(2)，数值最大误差 $1.4\times10^{-8}$。
- §6–§11：命题 6.1(1)(2) 与“降低伤害抬高 $\theta^\ast$”；8.6(2)；引理 8.2 的耦合逻辑；10.2(2) 两种约定；Remark S6.1 的界。
- 数字：S2.5 的 $r$ 区间；$0.95^7\approx0.70$；EV9 的每年 2.8 倍与 1.5–64 倍。

**独立复现的数值。** 命题 10.1 全部数字；S11.4 的驻留（1.89、5.32、10.45、5.85 对 5.86、10.34、16.18；底线 0.1% 时 3.81；保护于选择之外时 10.44）；Remark S5.2 第一种设定的全部数字，并作了 $r$ 与 $\delta_f$ 的扫描。

**跨文件核对的数字。** 四个月；0.45；1.6–2.6；0.61；10.45、3.81、10.44；"over a hundred times"（EV13 约 175 倍）；十五个小型社会；2.8 倍。各处一致。

**对照过的伴随文本。** S3（3.6、3.9、S3.2）、S5（5.10–5.17、S5.1、S5.2）、S6（6.4）、S10（10.1）、S11（S11.4）、S4 场模型；DISCUSSION X1 的国际关系部分与“新在哪里”、X8 的良性赢家与冲刺、X10 的保管；TESTS §3.1 与分歧表；EVIDENCE EV5、EV13；V6.1 的 SYNTHESIS（只为避免重复）。

**没有检查。**
- 证明：命题 2.2(4) 与 Remark S2.2（MPE，原文已标待外审）；命题 4.4、4.10–4.13；引理 3.11 的 Price 方程；命题 5.9；5.12 的控制论；6.7 的形式部分；Remark 6.8；命题 6.9；定理 10.4 的裕度；命题 S8.1、S8.5；11.1 的直觉准则；Remark S11.3 的序贯检验。
- 代码与文献：没有运行或阅读 `checks_v62.py`。文献未核，尤其 2026 年的 Fudenberg 与 Koh、Bueno de Mesquita 等、Gardner-Challis 等、Terekhov 等；我的知识截止于 2026 年年中，无法凭记忆确认。
- 登记册：EV5、EV13 以外的证据行；LEDGER 的忠实度；语料引文的准确性。
- DISCUSSION X2、X10 大部分、X11。

## 同族偏差

我与起草者同属一个模型家族。偏差可能在四处起作用。
1. **可读性。** 我习惯这种层层嵌套条件的英文。人类审稿人读摘要与 §1.2 的成本，大概比我判断的高；“它还不是一篇好论文”的判断里，这一项我可能低估了。
2. **重建共用约定。** 命题 10.1 的收益结构是我从原文数字反推的，这可能与原文共享同一错误。剪刀重建沿用了原文的一阶映射 $\theta_\Gamma$，我没有独立检验 $\Gamma_\delta\approx0.92$ 附近一阶近似的有效性。M5 的扫描结论与原文同模型，不是模型之外的检验。
3. **反方的选择。** 我判断“最强反方”时用的是我自己的显著性排序。M7 选了 Narayanan 与 Kapoor、Ding；国际关系或产业组织的人类学者可能另有首选，例如单极稳定论的最新版本，或技术扩散的经济史文献。
4. **对判断的认同。** 我对判断分层的总体认同，可能部分来自与起草者相同的价值先验。M2、M3、M6 是我能找到的、最可能被家族外读者首先攻击之处，但未必穷尽。

建议：M2（第二层的执行机制）与 M5（联合模型的参数区域）优先请家族外读者复核，前者最好请军控方向的人类学者看。
