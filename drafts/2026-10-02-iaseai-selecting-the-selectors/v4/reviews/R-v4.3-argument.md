# R-v4.3-argument：整体论证、标题与证明、目的与压缩

*评审对象：`v4/THEORY.md`，"No Winning Position: the integrated theory (v4.3)"，1851 行。评审日期 2026-10-03。视角：科学哲学、系统思维与资深编辑。我检查的是三件事：标题级断言是否等于被证明的内容，各层是否构成一个论证，论证能否经得住带敌意的冷读。*

*读过的材料：THEORY.md 全文；Ren 的方向记录 `sources/16-claude-code-directions/2026-10-03-v4-direction-cooperation.md` 全文；友人对话的 `full-summary.md`；上一轮外部评审 `reviews/R-v4.1-external-gpt.md`；`checks_v42.log`。我手算复核了 Prop 3(1)、Prop 5、Prop 8(2)（含"parity 时 δ>0.7"）、Prop 13(2)、Prop 23(3) 和 Theorem S(3) 的代数，均无误；脚本未重跑。本评审只新建这个文件，没有改动任何已有文件。*

---

## 1. 总体判断

**局部结果大体可靠，问题在接缝和标题。** 经过两轮修复，v4.3 的大多数局部命题在其模型内是对的。比较突出的有：Prop 4(3) 的全付极限、Prop 6 的被迫委托、Prop 7(3) 的鲁棒界 $e^{a\tau_c}$、Prop 8 的谈判协议条件，以及 Prop 13 和 Theorem B 的验证边界。剩下的问题几乎都在组合处和标题处，也就是前两轮评审一贯攻击的地方：标题说的比定理多。这一版的新内容（Theorem S、Theorem E、Prop 25、Corollary 3）恰好集中在这里。

**主梁的力量来自被假设的极限。** "世界必须合作"由第 10 节承载。它的结构是：
- 生存是最低需求；
- 竞赛的三类危险率趋于 1；
- 所以竞赛的每个分支都保不住生存；
- 所以合作在生存意义上弱占优，信任门槛趋于零；
- 剩下的只有出口。

这条链是对的，也是全文最有原创性的部分：把度量从"目标"换成"生存"，囚徒困境就变成弱占优；过渡因此首先是预测的改变，然后才是信任的改变。但现稿有两处问题：
- Theorem S 把三个极限当作假设，然后做了一个乘积式的代数。Theorem E 在陈述中又引入了 Theorem S 的条件，形成循环（A1）。
- §0 把最重的条件说成"只需要"（A1）。

**最弱的三个点，也是冷读者会攻击的地方：**
1. 孤立竞赛者（以及最强者）。"赢家也保不住"在这一分支上只靠 $q_{\mathrm{II}}$，而 L1 并不给出它（A2）。
2. 以支配或消灭结束竞赛。这两条路也"否定 H0"，却不在出口清单里（A3）。
3. "在今天的世界理性已明确告诉我们"。这句话没有被论证（A6）。

**一个好消息：理论蕴含的结论比它写出来的更强，也更贴近 Ren 的原意。** Theorem E 的证明自己承认，E2 和 E3 只能推迟被迫委托。所以长期来看，生存要求以协议结束竞赛，或者共同把 AI 撤出竞赛。这正是"世界必须合作"的长期定理形式，也正好落在 Ren 的第一优先上："否则博弈游戏会收敛主导权会递交"。现稿用"最多得其二"（Corollary 3）来表述，反而说弱了。按定义，这个表述还有一处自相矛盾（A4）。

**九层是一个论证，但没有把主梁摆在前面。** 实际结构是一条主梁加两组支撑：
- 主梁：生存 → 竞赛机制 → 生存分解 → 预测先于信任 → 出口 → 回应立场；
- 支撑一：竞赛机制（第 2.3、3 节）；
- 支撑二："竞赛内部没有独立的守护者"（第 4、5 节，来自 v3）。

宿主与底线这条慢路线（Theorem 1、2）是并列的第二条论证（Tier 2）。v3 的二阶层在主梁里有一个确定、而且关键的位置：它是封住立场方两条最强退路（"用 AI 让 AI 安全"和"先赢后治理"）的引理。现稿没有这样用它（A5、A10）。

**目的：部分达到。**
- 对称的、生存优先的、处在全面竞赛中的对手：论证强，而且新。
- 最强者、孤立竞赛者、持不饱和相对目标者、企业：论证弱。
- 第 8 节的框架对，但还不是"完美回应"。立场方的两个最强版本没有被正面回答，(A)⇒H3 靠定义成立（A5）。

**论文：必须改为主梁在前。** 10 页能承载：生存主梁、三个竞赛机制、验证边界、对立场的回应、出口。宿主模型与纠错者场的完整结果应放附录。这是需要 Ren 拍板的取舍（第 6 节）。

**截稿前的修复优先序：**
1. 用显式前提重写 Theorem E，并把 Theorem S(1) 降为引理（A1、A3）；
2. 加入"自知之明前提" X₂（A2），给条件 D 补上生存形式（A7）；
3. 用"长期必要性"替换"最多得其二"（A4）；
4. 写出反驳树、"纠错在竞赛之下"引理和良性赢家一项（A5）；
5. 统一术语（A8），修改末句（A20）。

其余可以放到之后。

---

## 2. 标题与证明对照表

判定：✓ 相符；◐ 需要限定；✗ 不符或缺证明。

| # | 位置 | 标题级断言 | 正文实际给出（及其条件） | 判定 |
|---|---|---|---|---|
| 1 | 标题 | "No Winning Position" | 正文没有定义它。物质上：只在完全耗散的极限下，加入的期望值等于必输（Prop 4(3)）；对最强者需要 K7，而 K7 没有被导出。生存上：Theorem S 在三个极限被假设时成立 | ✗ 应定义为"在竞赛之内没有保得住生存的位置"，并加上条件 |
| 2 | §0 第 2 段 | "The theory makes that prediction exact" | Theorem S 是给定极限下的代数，危险率没有测量 | ◐ 改为 "precise, and conditional" |
| 3 | §0 认识论段 | 生存论证 "needs fewer conditions… needs only that a race… passes its points of no return, and that a decisive winner whose objective is relative extends its dominance" | 实际需要：D 的生存形式、L1、L3、L4、L5、L6、危险独立、对称、某个危险类具有存在性、孤立竞赛者的 $q_{\mathrm{II}}$ | ✗ 把最重的假设说成"只需要"（A1） |
| 4 | §0 末，§14 | "In today's world reason says clearly that the actors must cooperate" | §12 自认 "not measured"、"least established"、"None systematic"；"evidence that the race premise is held… will be documented in revision" | ✗ 没有论证（A6） |
| 5 | §0 第 3 层，§14 | "joining buys nothing that staying out would not" | Prop 4(3)：只在 $r\ge n/(n-1)$ 的完全耗散极限下成立；$r$ 较小时加入有正收益 | ◐ 加 "in a fully decisive contest" |
| 6 | §0 第 3 层 | 竞争压力在利害超过增量风险时迫使委托 | Prop 6 在条件 D 下成立；D 的生存形式混用了时间单位 | ◐（A7） |
| 7 | §0 第 3 层，§14 | "correction cannot keep pace" / "correction falls behind" | Prop 7 只对超出鲁棒范围的危险类成立，且需要 L1 | ◐ 加限定 |
| 8 | §3 标题 | "why racing cannot be won" | 证明的是：期望上不划算，赢家保不住决定权。总有人会赢 | ✗ 改为 "what racing costs" 或 "why racing does not pay" |
| 9 | Theorem A 名称 | "The race premise removes the case for racing" | 去掉的是物质、福利与生存层面的理由。在行动目标层面，竞赛仍是最优反应（Prop 4(1)）。K7 没有被导出 | ◐ 改为 "…removes the material case for racing" |
| 10 | §4.4 末句 | "There is no better guardian to be found by winning" | 四条定性理由 | ◐ 作为小结可以；论证可以加强（A5 第 2 点） |
| 11 | §7 标题 | "Trust is the bottleneck" | Corollary 2：对生存优先者，约束性障碍不是信任 | ✗ 两处冲突（A15） |
| 12 | §7.1、§8.1 口号 | "Verification amplifies trust; it does not produce it" | 模型里没有"放大"。Prop 13(3)：完美而及时的检测使 $\varpi^\ast=0$。口号只对可靠性信任 $\vartheta_v$ 成立 | ◐（A15） |
| 13 | Theorem B | 所需验证随赢的价值上升 | Prop 13(2) 的代数，正确，条件已写明 | ✓ |
| 14 | Prop 25 | 每个安全手段的需求随 K 或 A 变坏，"或它本身是场内纠错者" | 是已有结果的汇编；析取的后一半使它难以证伪 | ◐（A16） |
| 15 | Corollary 3 | "Struggle, acceleration, safety: at most two" | (A)⇒H3 靠定义；(A) 本身预设了 (K)；K+S 只能暂时成立（Theorem E 的证明自己这样说）；(S) 一词两义 | ✗（A4、A5） |
| 16 | §8 引言 | "asks for something its own commitments rule out" | A4、A5 修复后成立 | ◐ |
| 17 | Theorem 1、Theorem 2 | 慢路线；安全保障的充分与必要部分 | 条件齐全，逻辑强度已经分清 | ✓ |
| 18 | Theorem C 名称 | 存在、可达、过渡中存活、持续 | 存在：只有一个数值例；可达：自认 "not shown"（生存版除外）；持续：列出所需条件 | ✗ 不是定理（A16） |
| 19 | Theorem S，§0 第 9 层，中文概要 | "No branch… secures survival, for any actor, the one that prevails included" | 三个极限被假设之后的乘积代数。赢家（T 支）只经 $q_{\mathrm{II}}$、$q_W$ 受损，而 L1 不给出孤立竞赛者的 $q_{\mathrm{II}}\to1$ | ✗（A1、A2） |
| 20 | Corollary 2 | "The transition is a change of prediction" | 需要：L6 成为共同知识；Φ 是地平线概率；合作在锁定之前到达 | ◐（A18） |
| 21 | §10.3 | 在 cancerous 目标下，落后不可承受 | 在 L4 下成立，条件已写明 | ✓ 但 "selected preference" 与 Prop 3(4) 矛盾（A8） |
| 22 | Theorem E，§0，§10.5，§14，中文概要 | "Every other course crosses a point of no return"；"其余道路都越过两个不可回头点之一" | 陈述循环；¬H0 不等于 E0（漏了支配与消灭）；量词用的是 "some actor"；$p_{\text{dec}}$ 不是两个不可回头点之一 | ✗（A1、A3） |
| 23 | §10.4，§0，§14 | "the exits are taken in order" | 这个次序是规范上的优先（Ren 原话是"优先选择"），不是推导出来的；E1–E3 本身也需要协调 | ◐（A12） |
| 24 | §0 末段 | "Nothing here asks any actor to sacrifice its interests" | Prop 24：$p^S_{\text{dec}}\gg p_{\text{dec}}$ 时，单方 E1 会降低生存 | ◐ |
| 25 | §14 末句（加粗） | "…the conditions under which anyone's winning remains viable" | 与标题和 Theorem S 相反，并用了"赢"的语法 | ✗（A20） |
| 26 | §2.3 "In plain words" | "Constructing opposition within one system is a mistake about the system one is part of" | 只在 $\kappa$ 计入全部耦合时成立，而条件写在下一段 | ◐ 先写条件，再写结论 |

---

## 3. 按严重度排列的发现

### A1【致命】Theorem S、Theorem E、Corollary 3 的陈述循环，§0 把最重的条件说成"只需要"

**位置：** §0 的 "Epistemic status"；§10.2 Theorem S；§10.4 Theorem E；§8.3 Corollary 3；附录 A。

**问题：**
- Theorem S 的假设包含 $q_{\mathrm I}\to1$、$p_{\text{dec}},p^S_{\text{dec}}\to1$、$q_{\mathrm{II}}\to1$。它的结论 $\Phi^T,\Phi^P,\Phi^S\to0$ 是各因子相乘的代数，附录 A 的证明只有一行。这是恒等式，不是定理。
- Theorem E 的陈述是 "Let (L1)–(L6) *and the conditions of Theorem S* hold. If H0–H3 all hold, every actor's survival → 0"。Theorem S 的条件已经包含三个极限，于是 H0–H3 变得多余；证明却又从 H0–H3 推出这些极限。陈述与证明不一致，冷读者会读成循环。
- Corollary 3 写 "Under the conditions of Theorem E"，继承了同一个问题。于是 Corollary 3(1) 的实际内容是"假设生存趋于零，所以没有安全"。
- §0 写道："The survival argument of Section 10 needs fewer conditions than the rest. It needs only that a race in which AI is the instrument passes its points of no return…"。这句把最强的假设（竞赛越过不可回头点）称为"只需要"。带敌意的读者只用这一句就能否定全篇："你假设竞赛以灾难结束，然后得出竞赛以灾难结束。"

**为什么重要：** 这是 Ren 目的的主梁，"必须合作"由它承载。它也正是前两轮评审一贯攻击的"标题与定理之间的缝"。

**修复：**
1. 把 Theorem S(1)–(2) 降为 *Lemma S (survival decomposition)*。主陈述改用非渐近的结果：Theorem S(3) 的上界 $\varpi^\ast_\Phi\le(\Phi^P-\Phi^S)^+/(\Phi^R-\Phi^T)$，加上 Prop 23(2)–(3) 的 $\Phi^S\ge\Phi^P$ 条件。它回答的是一个定量问题：危险率到什么水平，合作在生存意义上占优。
2. 用显式前提重写 Theorem E，逐条从 H 推出极限，每条标出所需条件。建议文本：

   > **Theorem E′ (Exits).** Assume L3, L5, L6, condition $D_\Phi$ (A7), independent hazards, and (X) some hazard class whose uncorrected growth ends every actor's survival.
   > (i) If H0 and H1 hold, then for every actor that keeps AI as its instrument, $q_{\mathrm I}\to1$ as $s$ grows (Prop. 6, Lemma 1, Lemma D of A9).
   > (ii) If H2 holds and the decisive entity's objective is relative (L4), $p_{\text{dec}},p^S_{\text{dec}}\to1$.
   > (iii) If H3 holds for a class in (X), $q_{\mathrm{II}}\to1$ (Prop. 7 with L1; for the lone racer, X₂ of A2).
   > Hence under H0–H3, $\Phi^T,\Phi^P,\Phi^S\to0$ (Lemma S).
   > (iv) Long run: see A4.

3. Corollary 3 只引用 Theorem E′。
4. §0 的认识论段要逐条列出生存论证的承重条件，并标出其中哪些是竞赛者自己的前提（见 A6）。不要再写"only"。

### A2【致命】"赢家也保不住"在孤立竞赛者分支上只靠 $q_{\mathrm{II}}$，而 L1 并不给出它

**位置：** §10.2 的生存分解、Theorem S(1)–(2)、Corollary 2；§0 第 9 层；中文概要第 9 条。

**问题：**
- $\Phi^T=(1-q_{\mathrm{II}})(1-q_W)$。这一支没有 $q_{\mathrm I}$，因为别人在克制，自己不被迫委托；也没有 $p_{\text{dec}}$，因为赢的是自己。所以 "the one that prevails included" 与 "cooperation is weakly dominant"（后者需要 $\Phi^R>\Phi^T$）完全取决于孤立竞赛者的 $q_{\mathrm{II}}$，以及 $q_W$。
- L1 把危险增长率绑在总竞赛强度 $\mathcal E$ 与能力增长速度上，而 T 支上的 $\mathcal E$ 最低。理论对 T、P、S 三支用的是同一个 $q_{\mathrm{II}}$，却没有论证：一个面对克制者的单独竞赛者，会越过纠错的速度。

**为什么重要：** 如果孤立竞赛者能在纠错范围之内取胜，$\Phi^T$ 可以大于 $\Phi^R$。那样一来：
- 在生存度量下背叛也有利，囚徒困境以生存的形式重新出现；
- Corollary 2（预测先于信任）失效；
- E2 和 E3 不能自我执行。

这正是"让对的一方先赢"这一立场的最强版本，也是 IR 读者第一个会问的问题："如果对方停了，我为什么不赢？"

**修复：**
- **加入显式前提 X₂。** Ren 的原话已经给出了它："第二种要看我们造出来的是什么"；"我们虽然技术条件达到了，但是社会和意识条件依然未达到"。建议文本：

  > (X₂) *At present, capability of the decisive class (ASI, recursive self-improvement) has hazard modes whose growth exceeds the robust reach of the correction available to whoever builds it, alone or with others (Prop. 7(3)–(4)).*

  在 X₂ 下：
  - $q_{\mathrm{II}}^T$ 也趋于 1，"赢家也保不住"有了机制；
  - E2 有了独立于"决定性"的理由，即自知之明；
  - E2 在生存度量下可以自我执行：背叛暂停，等于独自造出超出纠错的东西（见 A12）。

  X₂ 要列入 §12 的条件表，并写出反驳它的观测，例如独立测得的、在决定性能力类上保持鲁棒的纠错。
- **第二条路（可选，需谨慎）。** 一个接近决定性优势的孤立竞赛者，会落入所有其他方的预防性攻击条件（Prop 8），于是 $q_W$ 在 T 支上上升。这只能作为预测来写，不能作为建议；否则与 Prop 25(1) 对"以威慑为稳定器"的批评冲突。

### A3【高】Theorem E 把"否定 H0"等同于 E0，漏掉了支配与消灭；量词写成了 "some actor"

**位置：** §10.4 Theorem E；§10.5；§0；§14。

**问题：**
- ¬H0 的意思是"不再处于竞赛"。竞赛也可以因为一方获胜（支配）或一方被消灭而结束。Ren 的截图本身就写着："要么暴力的消灭，要么加入"。
- Prop 8 显示，在 (A8) 下预防性攻击对攻击者是理性的。攻击者的生存概率约为 $w_1$，有界远离零。
- Theorem E 写的是 "every trajectory on which *some* actor's survival stays bounded away from zero negates at least one hypothesis"。按字面，支配和消灭正是这样的轨迹。但它们不在出口清单上，也不在 §10.5 "everything else" 的清单上：§10.5 列了 deterrence，没有列 preventive war。
- "其余道路都越过两个不可回头点之一"还混入了 $p_{\text{dec}}$（从属），而从属不是两个不可回头点之一。

**为什么重要：** "其他都是人类绝路"是 Ren 的结论句，而目前它的逻辑载体有缺口。冷读者只需要一句话就能打开这个缺口："按你的 Theorem E，赢或打掉对方就是出口。"

**修复：**
1. 把量词改为 "every actor's survival bounded away from zero"，或改为"每个生存优先行动者的生存"。
2. 加一条引理，分两种情况：
   - 以支配结束竞赛：被支配者的生存保不住（L4）。赢家要保住生存，就必须在 PoNR-I/II 之前到达决定性优势。这是两只钟的比较：到达决定性优势的时间，对比 $t^\ast$ 与 $1/a$。在 P 支上赢家已经委托（Prop 6）；在 T 支上见 A2。
   - 以消灭结束竞赛：被攻击者生存丧失；攻击者承担冲突成本和报复风险。在相互不可接受的报复下，$q_W$ 落在双方身上。
3. 把 E0 定义为 "¬H0 by an agreement that preserves every actor's survival"。
4. 把中文概要改为"其余道路都会使某个行动者的生存趋于零"，或者在说明中把 $p_{\text{dec}}$ 单列出来。

### A4【高】理论蕴含一个比"最多得其二"更强、也更忠实的结论

**位置：** §10.4 Theorem E 的证明末句与 "E2 and E3 hold the trajectory open until E0 or E1 is reached"；§8.3 Corollary 3。

**问题：**
- Theorem E 的证明说 "under E3 alone, $s$ still grows and $t^\ast$ is only postponed"。也就是说，只要 H0∧H1 成立（竞赛在进行，AI 是工具），并且 $s$ 在增长（L3），被迫委托就只是被推迟。长期看，生存要求以协议否定 H0，或者否定 H1；而由 Prop 24，否定 H1 必须是共同的。这就是"世界必须合作"的长期定理形式。现稿没有把它写成结果。
- Corollary 3 的三角写法与定义不一致：
  - (A) 被定义为 "at the pace the contest sets"，已经预设了 (K)。所以 "(A) and (S) exclude (K)" 在定义之下自相矛盾，正文只好在 (3) 中把 acceleration 换成 "development as fast as independent correction can follow"，这是换义。
  - "(K) and (S) exclude (A)" 暗示存在一个稳定的 K+S 角，而 Theorem E 的证明否认这一点。

**为什么重要：** 修正后的结论与 Ren 的原话一一对应：
- (K) 排除持久的安全，对应"否则博弈游戏会收敛主导权会递交"；
- (A) 只决定多快失去安全；
- 放弃 (A)、保留 (K)（即 E2、E3），只能暂时维持安全，对应"先停下来，让合作变得可能"；
- 其余都是绝路。

"最多得其二"既说弱了，又可以被反驳。

**修复：**
- 在 Theorem E′ 中加入第 (iv) 条：

  > (iv) *Long run.* If $g_s>0$, (i) holds whatever H2 and H3. Hence a trajectory on which every actor's survival stays bounded away from zero over an unbounded horizon ends the contest by agreement (E0) or takes AI out of it for every actor (E1 held in common). E2 and E3 postpone $t^\ast$ and keep $\Phi^S$ positive until then.

- 把 Corollary 3 改为：

  > **Corollary 3′ (Struggle and safety).** Lasting safety excludes (K). (A) presupposes (K) and shortens the time before safety is lost. Giving up (A) while keeping (K), by E2 or E3, keeps safety only until (K) is given up.

- 如果想保留"at most two"这句好记的话，只放在结论里，并紧跟精确的形式。

### A5【高】第 8 节还不是"完美回应"

**位置：** §8 全节；Prop 25；Corollary 3；§13 的对应反驳。

问题有五个，第 5 点是组织方式的建议。

**1. (A)⇒H3 靠定义成立。** "按竞赛节奏发展"并不等于"某个危险类超出了纠错速度"。持这一立场者今天最强的版本恰恰是：用 AI 加速安全研究与纠错，让纠错跟上（自动化对齐、AI 评估 AI）。理论有现成的零件回答它，但没有组装：
- Prop 7(5)："If the faster correction is supplied by the contest's own systems, that is Proposition 6"；
- Remark 3；
- Props 9–11：场内纠错者被选择，独立纠错所需速率为 $g/(1+\eta)$；
- Prop 7(3)：在自适应的对手之间，模型误差不缩小；
- Prop 7(4)：不可缩短的证据滞后。

建议把它们写成一条引理，作为 Corollary 3 的前提被证明，而不是被定义：

> **Lemma C (Correction under the contest).** Under (K), correction faster than the contest's hazard growth is supplied either by the contest's own systems, which is delegation of correction to systems retained for relative performance (Prop. 6, Lemma 1, Remark 3), or by independent correctors, which (K) under-supplies (Prop. 10) and whose required rate rises as AI cheapens control (Prop. 11). For classes with an irreducible evidence lag $m_e$, $a\tau_c\ge a\,m_e$ whatever is done (Prop. 7(4)), and robust correction tolerates model error of at most $e^{-a m_e}$ (Prop. 7(3)). Hence under (A), which raises $a$, H3 holds for every class with an irreducible lag once $a\,m_e$ passes the robust bound, and for other classes unless independent correction grows faster than $g/(1+\eta)$.

**2. "良性领先者会在够了的地方停下"这一版本没有被正面回答。** 立场方会说："让对的一方赢，赢了以后自我约束。"理论在 §12 的 L4 行自己承认：若赢家有可信、可验证的限度，$p^S_{\text{dec}}$ 就不再意味着从属。也就是说，良性赢家对他人是可生存的。这是立场方最强的一手。理论内部有现成的回答：
- (a) 对即将获得决定性优势的一方，它的未来承诺不可信（Prop 8 的 Fearon 机制；Prop 15）；
- (b) 这个承诺对它自己也不可靠：赢家的决定已经交给为相对表现而被保留的系统（Remark 3 加 Lemma 0），赢家本身也是一个场（§4.4）；
- (c) 要让这种限度可信，所需要的恰好就是 Definition 3 的内容。

建议把它作为 Prop 25 的第五项，并加进表格。

**3. (K) 的定义与 L6 冲突。** (K) 被定义为包含 "the objective remains relative"。这使持此立场者成为 $\theta=-1$ 的行动者，而 Theorem E 和 Corollary 3 依赖 L6（生存优先）。建议把 (K) 只定义为 "contest for decisive advantage with AI as its instrument"（即 H0∧H1），把目标是否相对留给 L4，并让 L4 作用于决定性实体。

**4. (S) 一词两义。** 在定义中，(S) 是手段（"instruments that leave (K) and (A) in place"）；在 Corollary 3 中，(S) 是结果（生存有界远离零）。应统一为结果，手段归入 Prop 25。

**5. 组织方式：一棵反驳树。** 立场方的每一条自洽的退路，要么落在理论的某个出口上，要么是一次让步（见第 6 节的图 1）。这就是"完美回应"在论证形式上的含义：不是证明对方错，而是证明对方每一个自洽的修正都落回理论给出的出口。

### A6【高】"今天的世界"没有被论证，最有力的证据形式也没有被用上

**位置：** §0 末；§12（"will be documented in revision"）；§14。

**问题：** 这句承重的话是 Ren 的认识论立场："在今天的世界，这已经是理性可以明确告诉我们的了"。但 §12 自己写着 "not measured"、"least established"、"None systematic"。

**为什么重要：** Ren 要的不是"无条件的定理"，而是"今天的理性已经明确"。这需要一节专门的论证。现稿只有断言。

**修复：** 增加一节 "Why the conditions hold today"。它的结构是内在批评，而不是测量：
1. P1–P2（决定性、快）是竞赛者公开的前提，所以 Theorem A 在他们自己的前提上成立。
2. 竞赛者主张"我们的系统可控"，这给出一个两难：
   - 如果委托足够安全（$\Delta\psi$ 小），条件 D 成立，委托被迫（Prop 6），决定权转移（Lemma D，见 A9）；
   - 如果不够安全，那么按竞赛节奏造出来的，就是超出纠错的东西（X₂）。

   两支都落在不可回头点上。这样，$q_{\mathrm I}$ 和 $q_{\mathrm{II}}$ 的高位部分来自对手自己的信念，而不是作者的估计。
3. L4：迄今没有任何行动者公开过可验证的、"够了"的限度。这是一个可检验的陈述。
4. 存在证据滞后无法缩短的危险类：评估意识、延迟显现的伤害。§12 的 C4 行已有材料。
5. 以威胁破坏作为稳定器的提议已经在公开讨论中，所以 Prop 8 的条件已在议程上。

### A7【高】条件 D 的生存形式混用了时间单位，并与 L6 有张力

**位置：** Prop 6(6)；§12 的 D 行；Theorem S 的条件。

**问题：**
- Prop 6 是单期博弈：$u_i=-L_e(1-w_i)-L_c[1-\prod(1-\psi_j)]$，其中 $\psi$ 是"per-period"危险。生存形式（$L_e=L_c$）的 "$1/n>\Delta\psi$" 等于假设每一期竞赛都完全决定生死：每期的失败者以 $(n-1)/n$ 的概率出局。
- 如果每期竞赛被决定的概率是 $\pi_{\text{dec}}\ll1$，D 大约变成 $\pi_{\text{dec}}/n>\Delta\psi$。
- 如果竞赛只决定一次，而委托会锁定 $H$ 期，代价应是累积危险 $(1-\psi_0)^H-(1-\psi_1)^H$。
- 按文中的例子（$\psi_0=0.01$、$\psi_1=0.2$，每期增量 19%），一个有远见的生存优先者不会委托。这意味着 L6 本身削弱了 $q_{\mathrm I}\to1$。

**修复：**
- 写出 $D_\Phi$ 的两种形式，并说明各自对应哪种竞赛结构。
- 把文中的例子换成 $\Delta\psi$ 小的情形。这恰恰是竞赛者自己的信念，正好接上 A6 第 2 点的两难。
- 在 Theorem S 的条件中标明这一点。

### A8【高（冷读）/中（逻辑）】"cancerous"的定义不一致；"selected preference"让已修复的错误回流；反例被改成了标签

**位置：** §10.3；Remark 6；§12 的 L6 行；§13 的 "Survival is not lexicographic" 和 "Status is valued for its own sake"。

**问题一：定义不一致。** 正文至少给了五种说法：
- (a) "ranks relative standing above the shared survival of the system"（§10.3）；
- (b) Prop 3 中 $\theta=-1$ 的物质目标；
- (c) 相对选择在行动上的结果（Prop 3(4)）；
- (d) 没有"够了"的点（L4）；
- (e) §12 和 §13 的 "knowingly trade a high probability of losing autonomy for standing"。这里比较的是行动者自己的生存，与 (a) 的"共同生存"不是一回事。

**问题二：已修复的错误回流。** §10.3 末段（第 1194 行）与 §13（第 1382 行）写 "The objective is a selected preference (Proposition 3(4))"。而 Prop 3(4) 在 v4.2 已经明确写道："This is a result about selected actions. Whether preferences themselves evolve to θ=−1 … is not modelled here (repair G-R3)." 这是上一轮 G-R3 修复的回流。

**问题三：自我免疫。** §12 的 L6 行与 §13 把"不接受生存优先"的行动者直接归为 cancerous。冷读者会称之为自我免疫：任何反例都被重新命名为病。

**修复：**
1. 只用一个技术定义：在决定性维度上不饱和的相对目标（unbounded relative objective），也就是 L4 的对象。"把相对地位排在共同生存之上"作为 Lemma 0 下的推论，而不是定义。论文中用中性词；tumour 的图像最多一句，放在机制之后。
2. 删去 "selected preference"，改为 "the objective that selection on actions rewards"。
3. 把自我免疫改写成一个两类型的结果：
   - 对生存优先者，Theorem S 与 Corollary 2 适用；
   - 对持不饱和相对目标者，理论预测他们不会被说服。其余行动者的最优反应是共同的 E1、E2 与覆盖。这正是 Ren 说的"所有人都应该去首先反对这个逻辑"。
4. 让"反对这个逻辑"落到一个可操作的量上：使 L4 对每个行动者都不成立，也就是可信、可验证的"够了"的限度。§12 的 L4 行已经给出了 L4 的反驳条件，可以直接反过来用作建设性内容。这也符合 Ren"肯定优先于否定"的写作纪律。

### A9【中】"生存包含自主"目前靠定义；$q_{\mathrm I}$ 与 Prop 6 的 $\psi$ 口径不一

**问题一：** §10.1 把"把决定交给无法推翻的系统"定义为没有存活。立场方会说："我们对齐的 AI 就是我们。"现稿这一步是靠定义赢的。

**修复：** 理论内有现成的机制。行动者的生存部分是共同项：宿主与共享危险。被委托的系统是按竞赛表现被保留的（Remark 3）；由 Lemma 0，共同项在这种选择中相互抵消。所以锁定之后，没有任何作决定的过程代表该行动者在共同项上的生存利益。建议写成 *Lemma D (delegation does not carry survival)*。这样 $q_{\mathrm I}$ 就不再靠定义。

**问题二：** Prop 6 中的失控 $\psi$ 是"由任何一方造成、所有人承担"的共享损失；§10.2 的 $q_{\mathrm I}$ 却是私人的，只有委托者失去自主。两者应分开：
- $q_{\mathrm I}$ 是私人的自主丧失（锁定）；
- 委托造成的共享失控并入共享因子（$q_{\mathrm{II}}$，或单列 $q_c$），并且也要出现在 $\Phi^S$ 中。

### A10【中】L6 对国家合理，对企业不合理；这正是 v3 层应该接上的位置

**问题：** 有限责任使企业偏向冒险，理论自己在 §6.3 的表中也提到了 judgment-proofness。所以"生存优先"对企业是一个弱前提，而 §0 说本文的主体是 "states, firms, blocs"。

**修复：** 理论在 §1.2 已经做出了正确的区分："Between states, only the strategic forms… apply"；在开发者之间，起作用的是模仿和资源流动。建议明确写出：
- Theorem S、Theorem E 约束的是国家与联盟（策略层）；
- 企业通过选择（Prop 1、Lemma 0）和规则制定者（Prop 16）被约束。

这样，v3 的选择层与纠错者层在主梁里有了确定的位置，而不是并列的第二篇论文。这也回应了 Ren 在 v4.0 时的要求："those parts belong to one theory"。

### A11【中】E1 的范围与 §9.5 矛盾；Ren 说的是"斗争"不是"竞争"；E1 只形式化了一半

**问题一：范围矛盾。** §10.4 写 E1 的 "scope is every contest that AI would accelerate (labour, finance, persuasion, conflict)"；§9.5 却写 "It does not end competition… competition in products, science and service is compatible with viability"。两处互相矛盾。友人对话里 Ren 也明确区分了一般的生态竞争和他真正针对的东西：一个异化的自我模型在追求"更多"。

**问题二：只形式化了一半。** Ren 的原话有两半："不把ai本身和对ai的使用嵌入或者变成这种逻辑，即ai不应该以斗争的方式存在，也不能被当成斗争的工具"。E1 只否定了 H1，即 AI 作为工具。另一半"AI 本身不以斗争的方式存在"没有被表示，也就是：AI 系统不被构造成、也不被选择成持有相对目标的系统。这一半在理论中其实有锚点：Remark 3，以及 L4 适用于 "a delegated process"。

**修复：**
- H0 改为 "a contest for decisive advantage (struggle)"；
- E1 拆为两项：
  - E1a：不构造、也不按竞赛表现选择持相对目标的 AI 系统；
  - E1b：不把 AI 用作争夺决定性优势的工具；
- E1 的范围限定在争夺支配的竞赛，与 §9.5 保持一致。

### A12【中】出口次序是规范上的优先，不是推导出来的；"无法合作时"的出口本身也需要协调

**问题一：** "Each later exit asks less… and preserves less" 是排序的理由，不是定理。Ren 说的是"优先选择"，这是价值上的次序。应如实写成 "priority by what each exit preserves"。

**问题二：** 可行性有缺口。Prop 24 说，当 $p^S_{\text{dec}}\gg p_{\text{dec}}$ 时，单方 E1 保不住生存，"E1 must also be held in common"；单方 E2 或 E3 则是 Prop 4 意义上的克制。所以在 "while cooperation is not yet available" 时可走的出口，仍然需要合作，只是范围更窄的合作。现稿没有说明，为什么更窄的合作比 E0 更容易得到。

**修复：** 为每个出口分别写出可以单方执行的部分和需要协调的部分：
- E1 的单方部分：不把自己的冲突决定和战略决定交给 AI；并行维持 $\mathcal K\ge\mathcal K_{\min}$（Lemma 1）。
- E2：在 X₂ 下，它在生存度量下可以自我执行。背叛暂停，等于独自造出超出纠错的东西，所以 $\Phi^T$ 低。这是一个可以证明的结果，它恰好说明了为什么 E2 比 E0 需要的信任更少。
- E3：同理。

这样，出口次序既是 Ren 的优先，又有可得性上的论证。

### A13【中】E3 与 Corollary 3(3) 让 AI 装备的纠错设定节奏，可能把加速从后门放回来

**问题：** Ren 的原话是"把发展速度降低到认知以及通过认知可以做出应当应对的速度以下"，这里的认知是人的认知，对应他的第二个不可回头点："cognitive capability can not follow up"。而 Corollary 3(3) 写 "Outside the contest… that tempo is set by independent, AI-equipped correction"。如果纠错由人无法理解的 AI 来执行，那就是经由纠错通道的委托，PoNR-I 换了一条路重新出现。

**修复：** 把 E3 中的纠错限定为人能理解、能争议的纠错（contestability premise，§9.3），并以 Lemma 1 的 $\mathcal K\ge\mathcal K_{\min}$ 作为约束。AI 装备的纠错，只有在保持这一条件时才计入 $\tau$。

### A14【中】AI 2040 的归类既不公平，也不是 Ren 的原话

**问题：** 把一个"把超级智能推迟到 2040 年"的方案列为"保持斗争、加速、又要安全"的实例，作者群会强烈反对，评审也会觉得这是稻草人。Ren 的原话是：验证是"大家现在的道路"，要证明它"走不通，至少insufficient"；以及"AI2040也没有那么重要"。把它当作 K+A+S 的实例，来自助手的 gloss。

**修复：** 理论能给出更准确、也更有力的定位：Plan A 是"保持 (K) 之下的 E2"，即一个暂时的出口。
- 按 Theorem E′(iv)，它只能把轨迹保持开放，直到达成 E0 或 E1；
- 按 Theorem B，只要赢的价值仍然很大，它的验证就必须趋于完美，而且必须及时；
- 按 Prop 21 和 Prop 15(3)，按比例冻结会保留相对动机；
- 它自己承认的那扇门（接管风险成为共同知识时，依赖信任可能是更好的选择）正是 Corollary 2。

这样读，结论更强，对方也更难拒绝。

### A15【中】信任：第 7 节标题与 Corollary 2 冲突，"amplifies"口号与 Prop 13(3) 冲突，"exact form"出现了两次

**问题：**
- §7 的标题是 "Trust is the bottleneck"，而 Corollary 2 说 "the binding obstacle… is not trust"。
- 口号 "Verification amplifies trust; it does not produce it" 有两个问题：模型里没有"放大"；而 Prop 13(3) 说完美而及时的检测使 $\varpi^\ast=0$，即在 $\varpi$ 的意义上，验证替代了信任。这句口号只对可靠性信任 $\vartheta_v$ 和安装验证设施时的第一步成立。
- §7.4 与 §10.2 各自宣称自己是 "the exact form of 'the understanding has to be aligned first'"。

**修复：**
- §7 标题改为 "Trust: the bottleneck while winning appears to pay"。
- 口号改为可以证明的句子："Verification can replace belief in intentions only to the extent that its instruments are themselves trusted, and installing them is a first step taken on that belief."
- 把两处 "exact form" 合并：Corollary 1(1)（降低赢的价值，会同时放松全部约束）是一般形式，Corollary 2 是它在生存度量下的特例。

### A16【中】"定理"一词的通胀

**问题：**
- Theorem S(1)–(2) 是乘积恒等式；
- Theorem C 是一张需求清单：存在只靠一个数值例，可达性自认 "not shown"；
- Prop 25 是已有结果的汇编，其中 "or the instrument is a corrector inside the field" 这个析取使它难以证伪；
- Corollary 3 是标签之间的映射。

博弈论与 IR 读者看到 "Theorem"，会按定理的标准来审。落差会被读成"数学装饰"。

**修复：** "Theorem"只留给非平凡的推导：Prop 4(3) 的全付极限、Prop 7(3) 的鲁棒界、Prop 11 的速率律、Theorem 1、Theorem 2、修复后的 Theorem E′，以及 Prop 23 和 Theorem S(3) 的上界。其余改名：
- Theorem C 改为 "Framework (four requirements)"；
- Theorem S(1) 改为 Lemma；
- Prop 25 改为 "Proposition (requirements of the instruments)"，去掉析取项，逐项写出它依赖的命题和条件。

### A17【中】K7 并没有被 Theorem S 取代

**问题：** §6.2 写："Theorem S… replaces the comparison with an ordering of survival probabilities, which needs no comparison of rents with losses"。但 §10.1 的一般形式 $u=\Phi V$ 要求生存概率之差超过 $V_{\text{hi}}/V_{\text{lo}}-1$。对最强者来说，支配的价值远高于仅仅存活，所以这个条件正是乘法形式的 K7。

**修复：** 如实写出：对最强者，结论要么需要 L6 的字典序，要么需要生存概率之差超过它的租金比。这是最强者的关键量，应列入 §12 的条件表。

### A18【中】时间问题：Φ 应是"若竞赛继续"的地平线概率；$\Phi^R$ 依赖于在锁定前达成合作

**问题：**
- Theorem S 说 "as the race proceeds… →1"，而 Corollary 2 的"预测"需要的是：现在就对整条继续下去的轨迹作出评估。如果按"随时间推移"来读，等极限到来时，锁定已经发生（Lemma 1），过渡已经不可能。
- $\Phi^R=1-h_R$ 中的 $h_R$ 是"在协议下剩余的危险"。协议达成得越晚，$h_R$ 越高，因为锁定之后还有恢复期。

**修复：**
- 把 Φ 定义为：从现在起，在给定策略组合下，到地平线 $H$ 为止的生存概率。极限改写为 "as $H$ grows, or as capability grows along the continued race"。$h_R(t_{\text{agree}})$ 随达成时间递增。这样 Corollary 2 才真正是一个"预测"，"越早越好"也有了形式。
- 数值上也要说明这一点。在 `checks_v42.log` 的第一组参数（$q_{\mathrm I}=0.05$）下，阈值是 0.211，而且置身事外并不优于加入。所以过渡必须发生在危险还低、但预测已经被共享的时候。

### A19【中】缺少冷战的对照，以及 AI 竞赛文献的定位

**问题一：冷战的反例。** 冷读者的第一反应会是："冷战 45 年里有斗争、有加速，也基本安全。'至多得其二'被历史反驳了。"理论的回答其实是现成的：
- 核武器不给出决定性优势：二次打击能力使 $r$ 很小，对应 Theorem A 的第三支；
- 核武器不作决定，所以没有 H1。而几次近失事件，正说明了人在回路中的价值，对应 $q_{\mathrm I}$；
- 危险的增长是有界的。

AI 的不同恰好在 H1 与 H2。这一段会大大增强论证，必须写。

**问题二：文献定位。** 以下文献需要核实后再引用：
- AI 竞赛的博弈模型：Armstrong–Bostrom–Shulman 2016（已引）；Han, Pereira, Santos & Lenaerts 2020（JAIR）；Stafford, Trager & Dafoe 2022 "Safety not guaranteed"；Emery-Xu, Park & Trager 关于国际技术竞赛中不确定性与信息的工作；
- 合作在负责任 AI 开发中的作用：Askell, Brundage & Hadfield 2019；
- 决策速度与自主武器：Scharre 2018。

其中 Stafford、Trager、Dafoe 一类的结果（领先足够大时，领先者有余力投入安全），正是"先赢后治理"的经济学版本，必须回应。

### A20【低至中】结论末句与标题相反，并使用了"赢"的语法

**问题：** "What must be agreed is not who wins, but the conditions under which anyone's winning remains viable." 这句是 v3 的遗留。在 v4.3 的框架下（赢保不住生存），它暗示"赢"可以是可生存的，也违反了 Ren 的写作纪律：反竞赛的文本里不偷带 win/race 的语法。

**修复：** 改为 "What has to be agreed is not who comes first, but what every actor needs in order to go on." 或者更具体："…not who leads, but the conditions under which every actor keeps its own decisions."

### A21【低】其他

- §0 的 Tier 列表没有更新：Prop 25、Corollary 3、Theorem C 不在任何一层。
- Theorem S 的数值用的是 $n=2$（由日志反推得出），正文只写了 "n actors are symmetric"，没有给出 $n$。
- E3 的不等式 $a(\tau_{\text{obs}}+T_d+T_r)<1$ 是比例纠错的界，与 Prop 7(2)（加入导数作用后可以到 2）不一致。应改为 "below the bound of the available correction, with the margin of Prop 7(3)"。
- Definition 3(d) 要求 "makes Theorems 1, A and S common knowledge"，在定义里写入本文自己的定理，读起来是自我指涉。应改为"由独立证据形成的、关于赢的价值的共同评估"。
- Remark 6 的第二点引用 Remark 2 来证明 "consumes"，但 Remark 2 讲的是暴露不均与隔离，不是消耗。而且同一个论证也适用于 §10.6 的共同供给，所以需要说明：§10.6 只在已经退出竞赛之后成立。
- §0 写 "Nothing here asks any actor to sacrifice its interests"，但 Prop 24 显示单方 E1 在某些条件下会降低生存。应改为 "…asks no actor to act against its survival when others do the same"。
- Prop 3(3)：$W$ 的定义已经包含 $\kappa$，所以"按错误的目标行动，按正确的目标衡量更差"是同义反复。实质内容在 $\kappa>0$ 与 Prop 3(2)。建议降为 Remark。
- §2.3 "In plain words" 的结论句写在它的条件（Relative gains 一段）之前。按"机制先于结论"的纪律，两者应调换顺序。
- 全文有 71 处 "repair" 注释（大部分在正文），"v4.1" 在附录 C 之前出现了 36 次。对理论文件的冷读者，这是噪音。建议把它们集中到附录 C，另保留一份干净的阅读稿。

---

## 4. 对 Ren 方向的忠实度（逐条）

| Ren 的原话（摘要） | v4.3 的表达 | 判断 | 建议 |
|---|---|---|---|
| "重点就是证明世界必须合作…否则…我们会fuck up" | Theorem E 的出口是 E0、E1、E2、E3 四选一；"必须合作"没有被写成一个结果 | ◐ 说弱了 | A4 的长期必要性，即 E0 或共同的 E1，就是"必须合作"的定理形式 |
| 在 systems thinking、game theory、alignment、math 的框架下 | 四者都在。alignment 最薄：只有 Remark 3、Prop 25(2)、Prop 7(3) | ◐ | 补上"用 AI 让 AI 安全"和"良性赢家"两项（A5） |
| 两个不可回头点：被迫委托；认知跟不上 | Prop 6 加 Lemma 1；Prop 7 | ✓ | — |
| "第一种基本完蛋 / 第二种要看我们造出来的是什么 / 按当前逻辑搞也基本完蛋" | "要看造出来的是什么"没有被表示；$q_{\mathrm{II}}$ 只绑在竞赛强度上 | ✗ 漏了 | 前提 X₂（A2） |
| "这个条件非常容易达成并且不可预期，只要任意博弈方…" | Prop 4(4)，引了 unilateralist's curse | ✓ | — |
| "要么暴力的消灭，要么加入" | Prop 4(1) 与 Prop 8，并诚实写出 4(2)、4(3)、8(3)、8(4) 的限度 | ✓ | 但"消灭"作为一种 ¬H0 没有进入 Theorem E（A3） |
| 验证（AI 2040）："这条道路走不通，至少insufficient" | Theorem B 证明的是"在赢的价值很大时不够" | ✓（达到 insufficient） | AI 2040 的归类改为"保持 (K) 下的 E2"（A14） |
| 信任是瓶颈：消息可信、承诺可守，以及它的重要性 | Prop 13、14、15，三种信任 | ✓ | 第 7 节标题与 Corollary 2 要协调（A15） |
| 子系统在同一系统中构造边界、创立对立是反理性的（ego dynamics，non-dual） | Prop 3，Relative gains 一段，§10.2 | ✓ 诚实地限定了范围 | 先写条件、后写结论（A21）；"意识条件"可以接到 $\theta$ 上（见下面 E2 一行） |
| "没有任何一个定理能证明'世界必须合作'这个我'不同意'…但在今天的世界，这已经是理性可以明确告诉我们的了" | §0 的开头是 "No theorem proves unconditionally that the world must cooperate" | ✗ 开头正是 Ren 说他不同意的那种措辞；"今天"一句没有论证 | 以肯定句开头："The conclusion is derived from conditions, each named with what would refute it; the conditions that carry it are the racers' own premises and …; in today's world reason says clearly…"。再加 A6 的那一节 |
| 不要点名任何国家或公司 | 全文没有点名（已用 grep 核对） | ✓ | — |
| 先把理论做完整，之后再压缩 | 是 | ✓ | — |
| "生存是最低博弈需求" | §10.1 | ✓ | 需要 Lemma D，使"自主"不靠定义成立（A9） |
| "我们可以预测当下trajectory的博弈预期outcome" | Theorem S 与 Corollary 2 | ◐ | Φ 改为地平线概率（A18） |
| "如果胜利者的逻辑是cancer式的，落后并不可以承受，因此所有人都应该去首先反对这个逻辑" | §10.3、Remark 6 | ◐ 前半忠实；"首先反对"没有可操作的内容 | "反对" = 使 L4 对所有行动者都不成立，即可验证的"够了"的限度；把它放在出口之前，作为第 0 步（A8） |
| "如果不能合作：优先…不把ai本身和对ai的使用嵌入或者变成这种逻辑…否则博弈游戏会收敛主导权会递交" | E1 只否定了 H1（工具） | ◐ 只表达了一半；范围扩大到了一切竞争 | 拆成 E1a 与 E1b，范围限定在争夺支配的竞赛（A11）；"主导权递交"即 $q_{\mathrm I}$ |
| "其次…自知之明，先别搞asi，rsi…技术条件达到了，但是社会和意识条件依然未达到，应该先停下来，让合作变得可能，可以理性思考，再去造更复杂的ai" | E2 被改写为"不造带来决定性优势的能力" | ◐ 丢了"自知之明"的理由：危险在于造出来的是什么，不只在于决定性；"意识条件"译成了 "cognitive conditions" | 用 X₂ 给 E2 一个独立的理由；"意识条件"可以接到自我模型 $\theta$（Prop 3）与理解的节奏上 |
| "要么就把发展速度降低到认知以及通过认知可以做出应当应对的速度以下" | E3 写为 $a(\tau_{\text{obs}}+T_d+T_r)<1$ | ✓ 形式化得好 | 但 Corollary 3(3) 让 AI 装备的纠错来设定节奏，要限定为人可以争议的纠错（A13） |
| "其他都是人类绝路啊" | §10.5，"holds exactly as far as Theorem E's conditions do" | ✓ 诚实 | 依赖 A1、A3 的修复 |
| "AI2040也没有那么重要，主要是…完美的回应这些'即打算不改变斗争思想，又打算加速，还想安全的人'" | 重建了第 8 节 | ◐ 框架对，但还不完美 | 补上反驳树、Lemma C、良性赢家一项，并修复 Corollary 3（A4、A5） |
| 友人对话（像树一样的自主供给；分布式、可更替；为所有人） | §10.6 | ✓ 大体忠实，也保留了 Alex 的观点 | "rather than to grow every year" 与 Ren 对发展、新奇的肯定有轻微张力（他的原意是"成长不是危险，心才是"），改为 "built to meet need rather than to gain standing" |

**写作纪律检查：**
- *机制先于结论。* 违反处有：§2.3 的 plain words；§7.1 与 §8.1 以口号开头；§3.2 的加粗句写在数值之后，这个可以接受。
- *肯定优先于否定。* 标题是否定句；出口全部用否定形式（keep out、do not build、slower）。建议给出肯定的名称：
  - E1："AI as common infrastructure, not as an instrument of dominance"；
  - E2："build the conditions for governing it first"；
  - E3："develop at the tempo of understanding"。
- *不偷带 win/race 语法。* 违反处是末句（A20）；"keep pace"出现多次，问题轻微。
- *保持多元、不做有损的合并。* Tier 结构与保留全部结果做得好。

---

## 5. 冷读风险

| 冷读者会怎样否定 | 来源 | 如何化解 |
|---|---|---|
| "你假设竞赛以灾难结束，然后得出它以灾难结束" | Theorem S 的假设；§0 的 "needs only" | A1、A6：非渐近的上界，加上建立在对手自己前提上的两难 |
| "对方停了，我为什么不赢？" | T 支只有 $q_{\mathrm{II}}$ 和 $q_W$ | A2 的 X₂；A3 的两只钟 |
| "冷战就是反例" | 没有冷战对照 | A19 |
| "你把委托定义成死亡" | §10.1 | A9 的 Lemma D |
| "凡是不同意你的都被叫做癌" | §10.3、§12 的 L6 行、§13 | A8：中性定义，加上两类型的结果 |
| "'Theorem'只是把引用汇编到一起" | Theorem C、Theorem S(1)、Prop 25、Corollary 3 | A16 |
| "AI 2040 推迟超级智能，你却说它在加速" | §8.4 | A14 |
| "'用 AI 把 AI 变安全'你没回答" | 第 8 节 | A5 的 Lemma C |
| "良性领先者会自我约束" | 第 8 节没有正面回答 | A5 第 2 点 |
| "q=0.6 之类的数字是随手写的" | Theorem S 的数值 | 只用于说明阈值的形状；主陈述用上界与条件，不用点值 |
| "企业是有限责任，不是生存优先" | L6 被施加于所有行动者 | A10 |
| "每期 19% 的失控增量还被迫委托？" | Prop 6(6) 的例子 | A7 |
| "E1 是要把 AI 从市场里清出去吗？" | §10.4 的范围 | A11 |
| "定义里要求接受你的定理" | Definition 3(d) | A21 |
| "通篇修复注释，像是一份没完成的稿子" | 71 处 repair 注释 | 移入附录 C，另出干净的阅读稿 |
| 意象与引语：tumour、trees、"missiles at the data centres" | §10.3、§10.6、§3.5 | 在理论文件中可以保留，但放在机制之后；论文中 tumour 和 trees 最多各一句，"missiles" 只保留引文出处 |
| 没有提"不可预期"如何测量 | §3.3 末句 "reached without a visible line" | 这是可以接受的定性结论，指向 Prop 4(4) 即可 |

---

## 6. 10 页 IASEAI 版本的计划

*前提：理论文件保持完整；这里是论文的压缩方案。AAAI 双栏 10 页，按 NOTES.md，附录不计页数，但审稿人可以不读附录，所以正文必须自足。下面的方案按约 8.8 页正文预算，并为参考文献留出余地。如果参考文献也计入 10 页，就再压缩第 7、9 节。*

### 6.1 标题

推荐：**"Survival Is Shared: Why Rivals Racing for Decisive AI Must Cooperate, and What to Do Until They Can"**

备选：
- "The Shared Minimum: Survival, Prediction and Cooperation among Rivals Developing Advanced AI"（更中性）；
- "Struggle or Safety: A Conditional Case that Rivals Must Cooperate on Advanced AI"（更直接，但标题以否定性的二选一组织）。

理由：标题应当是肯定句，命名本文实际证明的东西（生存是共同的），并且不使用"赢"的语法。"No Winning Position"既没有定义，又是否定句，还要求一个本文没有证明的普遍性。

### 6.2 摘要草稿（198 词）

> Many plans for advanced AI keep the contest between rivals, build capability at the contest's pace, and seek safety through verification, deterrence and control of their own systems. We analyse this position under stated conditions. Survival as a self-governing actor is every player's minimum requirement. In a contest for decisive advantage with AI as its instrument, three mechanisms threaten it: competitive pressure forces decisions onto AI systems retained for relative performance, which cannot register what the players share; correction loses robustness exponentially in hazard growth times delay, and fails where evidence lags; and an imminent decisive shift makes promises incredible and invites preventive attack. Decomposing survival by branch, we show that when these hazards are high, neither winning, joining nor falling behind secures it, cooperation becomes weakly dominant for survival-first players, and the trust it needs falls toward zero: the transition begins with a shared prediction. Verification lowers the trust required, but must be near-perfect and timely to the degree that winning appears to pay. Over a long horizon, survival requires ending the contest by agreement or taking AI out of it; pausing decisive capability, or slowing below the tempo of correction, holds the way open until then.

*注意：*
- *第三句的"cannot register what the players share"需要 A9 的 Lemma D。*
- *最后一句需要 A4 的 Theorem E′(iv)。如果截稿前来不及完成，就改为 "Until cooperation is reached, the exits, in order of priority, are…"。*

### 6.3 一段话的主梁（正文第 1 节就应当是这段）

> Survival is every player's minimum. Under the race premise, three mechanisms (forced delegation, the tempo bound, preventive attack) make each branch of the race unable to secure it, the winner's included where decisive capability outruns its builder's correction. Measured in survival, cooperation is weakly dominant and the trust threshold vanishes, so the transition is a change of prediction before it is a change of trust. Verification cannot substitute for that prediction while winning appears to pay. The position "keep the struggle, accelerate, be safe" fails at each of its instruments, and every consistent repair of it lands on an exit. Over a long horizon, the exits reduce to two forms of cooperation.

### 6.4 图

- **图 1：反驳树。** 这是"完美回应"的可视化。根节点是立场 (K)+(A)+(S)：
  - Q1 决定性优势是否真在争夺之中？否：竞赛失去对象（Theorem A 的第三支）。是：进入 Q2。
  - Q2 你的 AI 是否安全到可以把竞赛决定交给它？是：委托被迫（Prop 6），决定交给为相对表现而被保留的系统（Lemma D），落到 PoNR-I。否：进入 Q3。
  - Q3 那么能否按竞赛的节奏纠正它？在 (K) 下，纠错要么是竞赛自己的（即委托），要么是供给不足的独立纠错（Lemma C）；证据滞后不可缩短，所以落到 PoNR-II。
  - Q4 赢家会在够了的地方停下吗？对即将获得决定性优势的一方，这个承诺不可信（Prop 8、15），对它自己也不可靠（Remark 3、§4.4）。要让它可信，所需要的就是合作。
  - Q5 威慑或验证能守住吗？见 Theorem B 与 Prop 25。

  每一片叶子要么是让步，要么是出口。
- **图 2：生存的分解。** 横轴是 $q_{\mathrm I}$，纵轴是 $\Phi^R,\Phi^T,\Phi^P,\Phi^S$，标出 $\Phi^S=\Phi^P$ 的交点以及阈值 $\varpi^\ast_\Phi$，数据用 `checks_v42.py` 的参数。也可以换成出口的示意图。

### 6.5 章节与页数预算

| 节 | 内容 | 页 |
|---|---|---|
| 1 Introduction | 中性地陈述立场（K、A、S）；生存是最低需求；五条贡献；认识论（条件式；条件尽量取竞赛者自己的前提；预先列出反驳） | 1.0 |
| 2 Related work | AI 竞赛模型、竞赛理论与租耗、预防性战争与承诺问题、保证博弈与验证、冷战与军控、以威胁破坏为稳定器、AI 2040 | 0.5 |
| 3 Model | 行动者，CSF，P1 与 P2；三种度量（目标、物质、生存）；四类危险；用一个框列出连接假设（L1、L3、L4、L5、L6、X₂）；Lemma 0 用一行 | 1.0 |
| 4 Three mechanisms of the race | 4.1 完全决定性竞赛中加入等于必输（Prop 4(3)，Prop 5 一行），自我模型的边界错误（Prop 3(1)–(2) 与 relative gains，共 0.3 页）；4.2 被迫委托（Prop 6 用 $D_\Phi$，Lemma 1，Lemma D）；4.3 节奏界（Prop 7(1)、(3)、(4)）；4.4 预防性攻击（Prop 8 在 A8 下，加 8(4)） | 2.0 |
| 5 The race in survival terms | Prop 23；Theorem S（主陈述为非渐近上界）；Theorem E′（含长期必要性）；Corollary 2；图 2 | 1.5 |
| 6 Trust and verification | Prop 13；Theorem B；三种信任；Prop 14 与 15 各一句；四类障碍（表格可省） | 0.9 |
| 7 Struggle, acceleration, safety | 反驳树（图 1）；Lemma C；Prop 25 的表（含良性赢家一项）；Corollary 3′；AI 2040 作为一个例子（一段，定位为"保持 (K) 下的 E2"） | 1.1 |
| 8 Exits and what cooperation must contain | 出口次序（优先），各出口的单方部分与需协调部分，Prop 24；Definition 3 的压缩版；"竞赛内部没有守护者"一段（Props 9–11 的速率律 $g/(1+\eta)$ 一句）；四项要求（原 Theorem C） | 0.6 |
| 9 Conditions, refutation, limits | 一张条件表（L4、L6、D、A8、X₂、$q$ 的指标与反驳观测）；冷战对照一段；开放问题 | 0.5 |
| 10 Conclusion | — | 0.2 |
| 合计 | | 9.3（含两图；若超页，压缩第 2、6 节） |

### 6.6 正文与附录的分配

| 结果 | 位置 |
|---|---|
| Prop 4(3)、Prop 5（一行）、Prop 3(1)–(2)、Prop 6、Lemma 1、Prop 7(1)(3)(4)、Prop 8、Prop 13、Theorem B、Prop 23、Theorem S（上界）、Theorem E′、Corollary 2、Lemma C、Lemma D、Prop 24、Corollary 3′ | 正文 |
| Prop 25 | 正文，以表格形式 |
| Props 14、15，Corollary 1 | 正文各一句，证明放附录 |
| 宿主模型、Prop 1–2、Theorem 1、Theorem 2、Prop 12、Remark 5（慢路线与静默越线） | 附录 B："The slow route" |
| Props 9–11、19–21、Prop 10、Prop 16、Prop 18（纠错者被选择） | 附录 B："No guardian inside the contest"；正文保留一段与速率律 |
| Props 17、22（共同前沿），Theorem C 的数值 | 附录 C |
| §6.3 的补救措施表（带出口一栏） | 附录 D（这张表对政策读者很有用，不要丢） |
| 数值 | 附录 E |

### 6.7 删去或不进论文

- 版本历史、全部 repair 注释、中文概要、mermaid 图；
- §10.6 的树的意象：只留一句，放进结论；
- §12 关于在位者立场的可检验预测，以及 structural recoverability：留在理论文件里；
- §9.5 的工具清单：只留一句（"fund correction outside the contest; fix rules before capture"）；
- 对 AI 2040 的逐条读法：只留一段；
- 匿名化：删去 Ren、Claude、文件路径、"09-28 paper"等字样。

### 6.8 方案 B（交 Ren 决定）

如果 Ren 认为 v3 的核心（纠错者被选择、速率律、静默越线）必须进正文，就用它替换第 6 节的大部分内容：
- 正文保留"no guardian inside the contest"一节，0.9 页：Prop 9 的平方律、Prop 11 的速率律、Prop 12 的静默越线；
- 信任与验证压到 0.4 页，只保留 Theorem B。

代价是：对 AI 2040 与"验证之路不够"的回应会变薄，而那是 Ren 在 10 月 3 日明确要求的回应对象之一。我的建议是方案 A，因为 v3 的内容在方案 A 里已经以 Lemma C 的形式承担了主梁上的一环。

### 6.9 截稿前的修复次序

1. A1、A3：重写 Theorem E′，把 Theorem S(1) 降为引理，修改 §0 的认识论段。
2. A2：引入 X₂，写进条件表。
3. A4：写出长期必要性，用 Corollary 3′ 替换原来的 Corollary 3。
4. A5：写 Lemma C，加入良性赢家一项，画反驳树。
5. A7、A9：$D_\Phi$ 与 Lemma D，各一段。
6. A8、A20：统一术语，修改末句。
7. 然后才开始压缩成论文。A10–A19、A21 可以在论文写作中顺手处理，或者推迟到截稿之后。

---

## 7. 应当保留的

- **四层架构，以及每个组合结果都列出它继承的条件。** 这是 v4.2 以来最重要的进步，也是抵御"标题大于定理"这类攻击的基础设施。
- **Prop 4(3) 的全付极限：在完全决定性的竞赛中，加入的期望值恰好等于必输。** 这是本文最干净、最可信的"no winning position"物质形式，目前被埋没了，应在论文里放到显眼位置。
- **Prop 6、Lemma 1 与 Remark 3 的组合：被迫委托、能力锁定、委托出去的过程被竞赛选择。** 再补上 Lemma D，就是全文最有力的机制。
- **Prop 7(3) 的 $e^{a\tau_c}$ 鲁棒界，以及 Prop 7(4) 的不可缩短滞后。** 它们严格、少见，正好回答"用 AI 让纠错跟上"。
- **Prop 8：把谈判协议写成显式条件 (A8)，并给出 8(4)（战争成本高时起威慑作用，而不是引发攻击）。** 这是诚实的写法。
- **Prop 13 与 Theorem B 作为边界，而不是必要性；以及三种信任的区分。** 这是公正对待验证路线的写法。
- **度量的切换，即 Prop 23 与 Corollary 2 的"预测先于信任"。** 这是本文对"从竞赛到合作的过渡"最原创的贡献，应成为论文的核心结果。
- **§7.4 的四类障碍表。** 它说明本文没有把一切都归结为"缺少理解"。
- **§6.3 的补救措施表及其出口一栏。** 对政策读者，这是最有用的一页。
- **Remark 6 拒绝"让落后可承受"的理由，以及 §10.6 中共同的、分布式的、可更替的供给。** 只需把两者的区别说清楚：前者是私人保险，后者是共同的供给，而且只在已经退出竞赛之后成立。
- **§12 的"预先命名的反驳"，以及三张条件表。** 这是对 Ren 认识论立场最好的支撑；把 X₂、$D_\Phi$ 和最强者的租金比加进去即可。
- **全文没有点名任何国家或公司。**
- **§10.5 末句 "holds exactly as far as Theorem E's conditions do"。** 这是诚实的结论措辞，A1 与 A3 修复之后应原样保留。
