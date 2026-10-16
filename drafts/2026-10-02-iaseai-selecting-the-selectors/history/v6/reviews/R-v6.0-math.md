# v6.0 数学评审：新增与重述的形式结果

2026-10-03。对抗性数学评审，视角是博弈论、竞赛理论、演化动力学、概率与机制设计。独立会话，未复用 `checks_v6.py`。

**对象。** `v6/THEORY.md` v6.0：Remark 2.3；Lemma 3.3；Prop 3.5 及 θ 的识别；Lemma 3.10 与 §3.7 的推论；Prop 3.11；Remark 5.3；Prop 5.4；Remark 5.6；Prop 5.7；Cor 5.8；Remark 5.9；Prop 5.10；Prop 5.14；Thm 5.16；Prop 6.7；Prop 7.10；Lemma 7.11；Prop 8.6；Def 8.10；Prop 8.11。附录 A 中对应的证明都读了。

**脚本。** 纯 Python，放在 `/private/tmp/claude-501/-Users-ren-theories/125c36f5-6a17-4570-bcbc-ade65a8a973f/scratchpad/review60-math/`，汇总输出在 `review60-math.log`。

| 脚本 | 内容 |
|---|---|
| `r1_basic.py` | Remark 2.3；Lemma 3.3 的例子；Prop 3.5（精确有理数）；θ 识别；Prop 3.11 |
| `r2_lemma310.py` | Price 方程：划分依赖性与传递项 |
| `r3_remark53.py`、`r3b_convertibility.py`、`r3c_cap_above.py` | 再投资阈值、分享与可转换性、上限 |
| `r4_prop57.py` | 用贴现收益直接验证 Prop 5.7，Thm 5.16(1) 与 Cor 5.8 的对照 |
| `r5_prop514.py` | $n=3$ 的廉价谈话反例；Crawford–Sobel 的 $N(b)$ |
| `r6_common_constraint.py` | 普遍约束与规避 |
| `r7_lemma711.py` | FD 例子；耦合问题 |
| `r8_sec5_8_numbers.py`、`r9_club_theta0.py` | §5、§8 的全部 [N] |

## 总判断

**代数与数字基本都对。** 我复算的 [N] 全部复现，Prop 3.5 的恒等式在精确算术下成立。

**问题集中在两类地方：**
- **复合结论的逻辑。** Thm 5.16 是 §5.6 所说"论证需要的"那一条，它的两支与结论都有缺口。
- **模型参数与它承载的论断对不上。** Remark 5.3 的 $\chi$ 实际上是"分享"参数，却被 Prop 8.6(3) 当作"可转换性"来用。

另有几处"当且仅当""必要"写得比证明强：Prop 5.7、5.14、7.10，以及 Lemma 3.10 之后的推论。

---

## 一、问题（按严重程度排列）

### F1【致命】Thm 5.16 两支都不成立如所写，结论句是不合逻辑的推论

**位置。** Thm 5.16 及其证明（A.5）；§5.5 末段；§1.2 第 5 条。

**问题。**
1. **第 (1) 支与同节的 Cor 5.8 矛盾。** "Punishment remains available and cooperation can be enforced"在 $p_d$ 很小时并不普遍成立。对 $\theta=-1$，即使 $p_d=0$，对称惩罚也无法维持合作（Cor 5.8）；Remark 3.7 的贴现阈值在 $\lambda\to\infty$ 时趋于 1。而按本文的诊断，压力恰恰选择 $\theta=-1$。
2. **第 (2) 支的"requires common custody"不是 Prop 5.7 的推论。** Prop 5.7 给出的只是一个析取：要么 $p_d$ 保持很小，要么克制本身是所持目标下的阶段均衡。压低 $p_d$ 的途径不止共同托管，还有不建造（E2）、侦测快于突破（C7 不成立）、防御占优。证明中"only custody … keeps $p_d$ near zero"是断言，没有推导。
3. **"After that, it requires objectives … stage-game equilibrium"与第 (1) 支自相矛盾。** 托管若真把 $p_d$ 压到近零，重复博弈的执行就恢复了。
4. **结论"In neither case does the premise justify the race"混淆了个体理性与集体结果。** 在 Branch I，竞赛对每个行动者都是最优反应（Thm 5.15(a)、Prop 5.1）。第三条 bullet"whose objectives give least"还依赖 Prop 7.2(2) 的 [A]（胜前克制与胜后克制正相关）。

**计算。** `r4_prop57.py`：在 Prop 6.1 的博弈中取 $\theta=-1$、$p_d=0$。对 $\delta=0.5$ 到 $0.999$，偏离收益都是 $1.033$，惩罚余量都是 $0$，所以任何 $\delta$ 下都不可维持。

**为什么重要。** §5.6 写明全文"needs the dilemma of Theorem 5.16"。外部评审会首先指出第 (1) 支与 Cor 5.8 的冲突。修好之后论证反而更强：相对目标在两支中都无法被执行。

**修法。**
> *Theorem 5.16.* (1) If no deviation can yield a position beyond punishment ($p_d$ small), restraint can be enforced by repetition among actors with $\theta>-1$, given monitoring and $\delta$ above the threshold of Proposition 5.7(1); among purely relative actors it cannot be enforced by symmetric punishment even then (Corollary 5.8). (2) If a deviation yields, with $p_d\to1$, a decisive position worth at least the cooperative payoff, durable restraint requires at least one of: (a) keeping $p_d$ small, by not building capability of the decisive class, by holding it so that no party can use it alone, or by detection faster than breakout; (b) objectives under which restraint is a stage-game equilibrium. In case (2) racing can be each actor's best response; what the premise cannot justify is the race as a collective course, which leaves everyone's protection to the winner's objective.

### F2【致命】Remark 5.3 的 $\chi$ 是分享参数，不是可转换性；Prop 8.6(3) 与"只有第三个杠杆改变方向"在本文自己的模型里不成立

**位置。** Def 2.1；Remark 5.3；Prop 8.6(3) 及其后的三杠杆总结；§8.2（第 1864 行）；V5。

**问题。**
- **$\chi$ 的实际含义。** 在 $K_i'=(1-\delta)K_i+\kappa[\chi\Omega p_i+(1-\chi)\Omega/n]$ 中，$1-\chi$ 是均分的份额，所以 $\chi=1-\beta$，正是 Prop 8.6(2) 的分享。
- **再投资比例不影响阈值。** 乘子 $1+\delta(\chi r-1)$ 与 $\kappa$ 无关，连时间尺度也无关，所以"$\kappa$ sets … the time scale"不对。
- **按 8.6(3) 的定义读，结论不成立。** 若"只有 $\chi$ 可再投资、其余不可转换"，即 $K_i'=(1-\delta)K_i+\kappa\chi\Omega p_i$，乘子对一切 $\chi>0$ 都是 $1+\delta(r-1)$。也就是说，单靠不可转换，平等地位永不稳定。
- **可转换性起作用的条件。** 只有存在不靠赢得的能力来源 $K_0$ 时，它才起作用：平等地位不稳定，当且仅当 $\kappa\chi\Omega(r-1)>n\delta K_0$。
- **"方向"一词指的是两件事。** Prop 8.6(2) 的"不反转方向"说的是强度选择（$x^\ast>0$）；Remark 5.3 说的是地位动力学。在后者中，恰恰是分享（$\beta\ge1-1/r$）消除了不稳定。
- **记号。** $\chi$ 在 §4 还表示可占有性，8.6(3) 同一句里出现了两种含义。

**计算。** `r3_remark53.py`、`r3b_convertibility.py`，取 $r=1.5$、$\delta=0.05$：
- 分享模型：$\chi=0.6$ 时乘子为 $0.995$（稳定）；
- 不可转换模型：$\chi=1,0.6,0.3,0.1$ 时乘子都是 $1.025$；
- 加入 $K_0=1$ 后：$\chi=0.6$ 时为 $0.991$；
- 改变 $\kappa$ 时，乘子保持 $1.025$ 不变。

**为什么重要。** 这是"赢者之规"（V5）唯一的形式内容。按现在的写法，本文自己的模型给出的杠杆排序恰好相反。

**修法。** Remark 5.3 写明 $\chi=1-\beta$，并加上带 $K_0$ 的版本。Prop 8.6(3) 改为：
> *Let a share $\kappa_c$ of winnings be convertible into capacity in the same contest. Without a source of capacity not won in the contest, $\kappa_c$ sets only the level; with such a source $K_0$, equal standing is stable iff $\kappa_c\Omega(r-1)\le n\delta K_0$. Sharing stabilizes it iff $(1-\beta)r\le1$.*

总结句改为：两者都能稳定地位；两者都不改变强度选择的符号。

### I1【重要】Prop 5.7：前提方向写反，"iff"只在决定性位置的价值恰等于合作收益时成立

**位置。** Prop 5.7 的设定（"valued conservatively at no more than the cooperative payoff"）；A.5 证明（"upper value, the most favourable case for cooperation"）；Remark 5.9 的 scope note。

**问题。** 记决定性位置的每期价值为 $D_i$。真实的激励相容条件是
$$g_i\le\frac{\delta}{1-\delta}\big[p_d(O^\ast_i-D_i)+(1-p_d)(O^\ast_i-v_i)\big].$$
由此：
- $D_i<O^\ast_i$ 时，文中条件只是充分条件，而且 (2) 不成立；
- $D_i>O^\ast_i$ 时，文中条件只是必要条件；
- 只有 $D_i=O^\ast_i$ 时才是"iff"。

取"上界"对合作最**不**利，证明里的说法正好反了。Remark 5.9 说"$\theta_{\text{rep}}$ is a lower bound"，这需要 $D\ge O^\ast$，与设定的"no more than"矛盾。

**反例与计算。**
- 囚徒困境：$R=3$、$T=5$、$P=1$，$\theta=0$，$D=1$，$\delta=0.6$，$p_d=1$。合作可以维持，但文中条件判为不可维持（`r4`）。
- 20 万次随机抽样：$D<O^\ast$ 时有 12,235 例可维持而条件不成立；$D>O^\ast$ 时有 9,998 例条件成立而偏离有利；$D=O^\ast$ 时 0 例。
- DF 块的 21,096 例不是独立检验。$p_d=1$ 时，"可维持"与"阶段均衡"按构造就是同一个判据。

**修法。**
> *Let the decisive position be worth $D_i$ per period. (1) If $D_i=O_i(a^\ast)$, $a^\ast$ is sustained iff [the displayed condition]. (2) If $D_i\ge O_i(a^\ast)$ (the premise of the race), the condition is necessary, and as $p_d\to1$ the sustainable profiles are contained in the stage equilibria of the held objectives. (3) If $D_i<O_i(a^\ast)$ it is only sufficient.*

另外注明：$v_i$ 是最严厉的可维持惩罚值，计算时须计入惩罚阶段同样存在的 $p_d$。

### I2【重要】Prop 5.14(1)：$n\ge3$ 时"相对目标即零和，故谈话无信息"不成立

**位置。** Prop 5.14(1) 第二句；§2.3 表格；§5.5；§9.2。A.5 的证明只写了"between two parties"。

**问题。** 对 $n$ 个参与者整体零和，不等于两两对立。成对的目标之和是
$$O_i+O_j=\tfrac{n-2}{n-1}(\pi_i+\pi_j)-\tfrac{2}{n-1}\textstyle\sum_{k\ne i,j}\pi_k,$$
所以两个相对的竞争者在针对第三方的事情上利益一致。

**反例（`r5`）。** $n=3$，全体 $\theta=-1$。发送者知道 $u\in\{0,1\}$；当接收者选择 $y=u$ 时，第三方损失 1。完全揭示是均衡，双方各得 $1/2$；不谈话时为 $1/4$。

**为什么重要。** 第三种侵蚀的论断范围因此缩小。同时它揭示出相对目标的另一面：两两合谋对付第三方。这与 Prop 8.8 的"rivals can collude against third parties"一致，值得写进去。

**修法。**
> *(1) Where sender's and receiver's objectives sum to zero (two parties with $\theta=-1$), every equilibrium is payoff-equivalent to no talk. With $n\ge3$ relative actors a pair is not opposed: talk between two rivals can be credible about actions against a third.*

### I3【重要】Lemma 3.10 本身同义反复；"That the lemma leaves only this route is a theorem"不成立

**位置。** Lemma 3.10，以及其后两段（"cannot be discovered by selection … designed in advance"）。

**问题。**
1. **Price 方程丢了传递项 $\mathrm E[w\Delta z]$。** A.3 把它称作"within-group selection"，其实它包括学习、说服等有偏传递，而本文自己的路线（理解）正是通过这一项起作用的。
2. **"一个群体"是划分方式的选择，不是关于世界的事实。** 在同一个宿主之内，子单元（国家、企业）之间的选择或模仿照样存在。真正对一切划分都成立的不变量是：收益为全体共有的性状，在任何层级上都是共同项（Lemma 3.3），因而都被抵消。
3. **规则未必只能事先设计。** 收益部分落在本地的规则，可以在子单元的试验中被找到。

**计算（`r2`）。**
- 100 个子单元在同一宿主下，单元层面的规则：组间 Price 项为 $+0.057$。
- 成本 $0.05$、说服率 $0.10$ 时，性状在单一群体中趋于固定。

**修法。**
> *Lemma 3.10. A trait whose benefit is common to the whole population and whose cost falls on its bearer declines under every partition and every payoff-monotone rule with unbiased transmission; between-group selection at no level can favour it. It can rise only if a rule changes the bearer's relative payoff, or through biased transmission.*

后文改为：收益为全球、失败不可逆的规则不能靠选择得到，必须在失败之前采纳，但其组件可以从局部试验中学习。

### I4【重要】Lemma 3.3(2) 的引申、Prop 6.7(2)(3) 与 R8：行动约束不是共同的收益项

**问题。**
- **普遍的上限会改变相对收益。** 例：$e=(1,0.6,0.2)$ 的三家，在上限 $e\le0.4$ 下的成本是 $(0.6,0.2,0)$，排序反转（`r6`）。
- **选择随之作用于规避。** $q=0.5$、$F=0.5$ 时，规避者的份额趋于 1（`r6`）。"Invisible"只对守约者彼此之间成立。Lemma 6.5 的写法（"(a) fails"）是对的；Prop 6.7(3)"is a common term"给错了理由。
- **Prop 6.7(2) 的第二句没有根据。** 第 1 层最大化的是开发者自己的目标，不是相对地位。只有在 $\theta=-1$，或者作为第 2 层选择的长期极限（Prop 3.4(3) 中 $B\to\infty$）时，它才成立。
- **"协调问题"的结论只覆盖一部分。** 奖励黑客和权力寻求中，成本由开发者自己承担的那部分会被竞争内化。"Coordination problems"只适用于共同成本的那部分。

**修法。**
> *Lemma 3.3(2′). Among carriers that comply with a constraint enforced on all, it does not affect relative growth; an evader gains relatively, so the constraint survives iff the expected sanction is at least that gain.*

Prop 6.7 的 (2)、(3) 和结论句据此改写，并写明长期选择的条件。

### I5【重要】Prop 8.11(3)："相对目标没有'够了'"的证明并不区分目标

**问题。**
- **强度对一切 $\theta<n-1$ 都与赌注成正比**（`r8`：$\theta=-1,0,1,2.5$ 都是线性的），零次齐次并不刻画相对目标。
- **Prop 3.5(6) 中 $\theta=0$ 的"够了之点"$(1+\theta)H/n$ 随 $n$ 增大趋于 0。**
- **正文漏了 (φ)。** Thm 5.12 对任何目标都适用。
- **从"强度∝赌注"到"能力复利"缺少一环。**

**为什么重要。** "growth is not the danger; the mind is"（§8.6、§9.3）的形式依据就在这里。

**修法。**
> *(3) An objective that is not satiated, relative position or an absolute payoff linear in the stakes, has no point of enough: symmetric intensity is proportional to the stakes for every $\theta<n-1$; the relative objective adds the invisibility of $L$. Under (X), (U) and (φ), Theorem 5.12 applies to any continuation branch.*

口号相应改为：满足可饱和需要的增长有"够了"；非饱和的目标没有。

### I6【重要】Prop 7.10："必要"的例外栏不全，R7 不是推导结果

**问题。** 每行引用的结果说明，机制在要求缺失时会起作用，但没有说明这个要求不可替代。
- **R4** 漏了两种例外：侦测快于突破，以及克制已是所持目标下的阶段均衡（$\theta\ge\theta^\ast$）。这正是 Thm 5.16 正文自己列出的条件。
- **R8** 漏了"第 2 层的选择不是相对的"。Lemma 6.5 证明的是准入约束的充分性，不是必要性。
- **R7** 是规范性要求（V3）。Prop 3.11 只证明了相对于系统最优的过度生产，没有证明 O1/O2 超出容忍度。
- **R1** 漏了 Prop 3.4(2) 的协方差条件和直接上限。
- **R3** 以 $ab<\mu\delta$ 作为豁免，而 Remark 2.3 自己承认局部稳定不能约束偏移。

**修法。** 把例外栏补全。R7 移出"必要"表，归入 V3。标题改为"Requirements: each blocks a mechanism shown to drive the hazard; necessary unless the listed alternatives hold"。

### 次要

1. **Prop 3.11(2)。** 集团博弈等于原博弈（$n=k$）的前提是把 $\ell$ 换成 $s\ell$：强度为 $0.156$，而不是 $0.192$。集团大小不等且 $r\neq1$ 时，成功函数也不同（$3^{1/2}$ 倍）。
2. **θ 的识别。** 比值识别的是 $(1+\theta)\psi$，其中 $\psi$ 是被感知到的 $\ell$ 的份额。$\psi=0.5$、真实 $\theta=0$ 时，得到 $\hat\theta=-0.43$（`r1`）。这正是本文所说"看不见"的情形。识别还要求 $\theta$ 共同。所谓"exact"只是代数恒等。
3. **Remark 5.3(2)。** 上限只保证局部稳定。$\chi=1$、上限 $1.5<K^\ast=2$ 时，低于 $0.61$ 的落后者被排除（`r3`）。"Pushed out"只在 $\chi=1$ 时成立（`r3c`）。"$\rho(r-1)>\delta_f$"没有给出模型；按自然的写法，它是 $\rho\Omega(r-1)/(n\bar K)>\delta_f$。
4. **Prop 5.10(3)。** 按 5.10 自己的设定（分给 $n-1$ 个他人），食言收益是 $\beta\Omega(n-1-\theta)/(n-1)$。用 $/n$ 时须写明是均分给 $n$ 个人。
5. **Lemma 7.11 的证明。** "$S^A(H\mid\tau)\ge S^C(H)$"在 $\tau$ 与状态相关时不成立：例中为 $1/5<3/5$（`r7`）。须写明在同一状态上耦合比较；结论在耦合下成立。
6. **Remark 5.6(3)** 需要 $\Delta_y>(n-1)c_y$。**Prop 5.4** 中的"scales $\Omega_t$"应为 $\Omega_e$。**§8.4**"Pooling does nothing … under relative selection"与 Prop 8.6(1)"selection slows"矛盾；这是 v5.2 次要 3，尚未改。
7. **Def 8.10。** "对每个错误都存在纠正"的量词结构是判别核（guaranteed viability，Cardaliaguet），不是 viability kernel。离开该核是不可逆点，不等于 O1/O2 发生。
8. **记号冲突。**
   - $\delta$：阻尼、贴现、折旧；
   - $\kappa$：耦合、再投资；
   - $\chi$：三义；
   - $\rho$：再生、再投资；
   - $D$、$R$、$K$ 也各有多义。

   A.0 说"symbols are local"，但 8.6(3) 跨节引用。
9. **Prop 8.6(2)。** $r\le1$ 时有一行证明：$y\mapsto\Delta(y,x^\ast)$ 是凹的，不必用网格。数值上 $r=1.3$（$n=4$）仍不可入侵，$r=2$ 时零强度可入侵。
10. **Prop 5.14(3)** 应引 Aumann (1990)。

## 二、站得住的部分

- **Remark 2.3。** 解析证明正确，30 万次抽样无误；$\mu,\delta\le1$ 保证较小的根大于 $-1$。
- **Prop 3.5。** 恒等式与 (1)–(6) 在精确算术下全部成立，λ↔θ 的映射也对，是全文最干净的统一结果。
- **Prop 3.11(1)。** 数字复现。还可以更进一步：$\theta=0$ 时 $\mathcal E=0.92$，对局外人的损害为 $5.5$；俱乐部为 $31.0$，系统最优为 $2.2$。包容的俱乐部比孤立的自我伤害局外人更多，这加强了本文的论点（`r9`）。
- **Prop 5.4。** 公式、界和 $\theta=-1$ 的值正确。
- **Lemma 5.5。** $0.342$、$0.216$、$0.136$、$0.702$ 都复现。
- **Remark 5.6、5.9 和 Prop 5.10。** 数字全部复现。
- **Cor 5.8。** 在所述范围内正确。
- **Prop 5.14。** $n=2$ 时的零和证明正确；Crawford–Sobel 的 $N(b)$ 无误。
- **Prop 8.6(1)(2)。** 正确：$x^\ast$ 的公式与三组例子都复现。
- **Prop 8.11(1)(2)。** 正确。$0.717$ 复现；按 $1.1^t$ 计为 $1.89\times10^{-9}$，按脚本的 $e^{0.1t}$ 计为 $1.83\times10^{-9}$。
- **Lemma 7.11 的 FD 例子。** 用独立的递推复现。
