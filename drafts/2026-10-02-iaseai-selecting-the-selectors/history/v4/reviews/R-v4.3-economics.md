# THEORY v4.3 评审：经济学视角

*评审对象：`v4/THEORY.md`，"No Winning Position: the integrated theory (v4.3)"，1851 行，约 2.8 万词。全文读完，含 Appendix A–C。同时读了 `checks_v4.py/.log`、`checks_v42.py/.log` 和 `reviews/R-v4.1-external-gpt.md`。*

*视角：机制设计、竞赛理论、公共经济学（公地、庇古责任）、规制与俘获的政治经济学（Stigler、Becker、Acemoglu–Robinson）、演化博弈与间接演化方法、灾难性风险下的决策理论。*

*方法：所有我有疑问的计算都用纯 Python 重算过。脚本在 scratchpad `review-econ/`（`p22*.py`、`p6phi.py`、`survival.py`、`allpay_asym.py`）；scratchpad 是临时目录，所以关键数字都写在正文里，可以复现。上一轮外部评审指出的问题，凡 v4.3 已在原处修好的（G-R2 的谈判协议、G-R3a 的非对称纯均衡、G-R4 的验证必要性、G-R5 的完整行和、G-R6 的退出损失、G-R8 的控制器范围），本文不再重复提出。*

---

## 1. 总体判断

v4.3 比 v4.1 严谨得多。§1.7 把"选择层"和"策略层"分开，并区分 $O_\theta$、$\pi$、$W$、$\Phi$ 四种量度，这是真正的改进。Props 2–5、11、13、19–21 的局部代数我逐条核过，都是对的。

但按顶级理论刊物的标准，这一版还不能投。原因有四个，前两个是确定的错误。

1. **Proposition 22 用了不一致的博弈约化，标签是错的。** 它的 2×2 表把 $S$ 放在"只有一个对手背叛"的局面下计算，把 $P$ 放在"所有人都背叛"的局面下计算，然后拿两者比较。在 $n$ 人博弈里正确计算最优反应之后：分立前沿（SEP）是囚徒困境，不是 chicken；共同前沿（CF）把它变成一个协调博弈（stag hunt），"全体背叛"仍然是 Nash 均衡，合作**不是**占优策略（E1）。Theorem C(1)、Corollary 1(4)、Proposition 25(3) 和 §0 都建立在"合作占优"上。
2. **"生存优先"的委托条件是在错误的量度里推出来的。** Prop 6(6) 和 Theorem S 用的条件 "$1/n>\Delta\psi$"，是在加性损失里令 $L_e=L_c$ 得到的；它不是生存概率 $\Phi$ 里的条件。我构造了两个反例，方向相反，这个条件两边都会判错（E2）。
3. **Theorem S 的力量几乎全部来自一个量：共享的纠错失败 $q_{\mathrm{II}}$。** 极限结论 (1)–(2) 只要 $q_{\mathrm{II}}\to1$ 就成立，$q_{\mathrm I}$ 和 $p_{\text{dec}}$ 这两个极限是多余的。对于获胜者，只有 $q_{\mathrm{II}}$ 和 $q_W$ 起作用。按 L1，危险率取决于竞赛强度；一旦危险率随局面变化，单独竞赛者的 $q_{\mathrm{II}}$ 可以很低，领先者在生存意义上面对的博弈就可能是囚徒困境。另外，"弱占优"并不能从定理的假设推出；证明只推出 $\varpi^\ast_\Phi\to0$（E3、E4）。
4. **K7 仍然只是被假设的条件，§1.7 的层次纪律在第 8、10、13 节和 §0 又漏了。** 多处把"选择作用于行动"写成"选择产生偏好"（E6、E7）。另外，v3.1 原有的相关文献段落（Stigler、Peltzman、Laffont–Tirole、Ostrom、Hardin、Vega-Redondo、Koçkesen–Ok–Sethi、Alger–Weibull、Barrett 1994、Carraro–Siniscalco、Han et al.、Askell et al.）在 v4.3 正文里全部消失。参考文献还在，正文却不再与这些文献对话，这违反了"不做有损合并"的原则（E11–E13）。

这些都能修，而且修好之后理论会更强。生存分析在修正后有一个清楚、可以辩护的核心：**能传到领先者那里的论证只有共享的节奏界（$q_{\mathrm{II}}$），而且在这个分量上双方利益一致，关于它的预测可以可信地传递。** 第二阶理论（控制矫正者的能力被选择）配上 Prop 11 的速率比较，是本文最原创的经济学内容。只是速率条件的经济含义比正文写的温和（E10），政策重心应该相应移到"不可占有性"和结构性分拆上。

---

## 2. 问题清单（按严重程度排序）

### E1 Proposition 22：2×2 约化不一致；SEP 不是 chicken，CF 下合作不是占优策略

**位置。** §9.4 Prop 22(1)–(3)；Appendix A 中 Prop 22 的证明。下游受影响的有：Theorem C(1)（"cooperation is dominant"）、Corollary 1(4)、Prop 25(3)、§8.2 的表、§0 第 8 层、中文概要第 8 条。

**原文主张。** 在 $n=4$、$r=1.3$、$\Omega=\Omega_c=L_b=c=1$、$\ell=0.3$、$e_c=0.05$ 时，分立前沿下博弈是 chicken；共同前沿下合作占优；"盖子"随赢的价值陡增。

**问题。** 附录里各格的定义是：
- $R$：所有人都合作；
- $T$：$i$ 背叛，其余人合作；
- $S$：$i$ 合作，**恰好一个**对手背叛，另外 $n-2$ 人合作；
- $P$：**所有** $n$ 人都背叛。

分类时比较的是 $S$ 和 $P$。可是这两格所处的"其他人的策略组合"不同，所以 $S$ 与 $P$ 之差不是 $i$ 在任何固定 $\sigma_{-i}$ 下的最优反应比较。正确的做法是：对每个 $k$（其他人中的背叛者人数），在其他人策略固定的条件下，比较 $u_i(C\mid k)$ 和 $i$ 背叛时的最优反应 $\max_x u_i(D,x\mid k)$。

**计算。** 参数同原文。背叛者在给定合作者 $e_c$ 时取他们之间的对称均衡强度；$i$ 在其他人全部固定的条件下取最优反应。

| 其他背叛者数 $k$ | SEP：合作 | SEP：背叛（最优反应） | CF：合作 | CF：背叛（最优反应） |
|---|---|---|---|---|
| 0 | −0.610 | **+0.116** | **+0.140** | +0.002 |
| 1 | −1.056 | **−0.586** | −0.885 | **−0.670** |
| 2 | −1.331 | **−1.298** | **−1.291** | −1.297 |
| 3 | −1.422 | **−1.396** | −1.422 | **−1.396** |

这张表说明三件事。
- **SEP。** 对每个 $k$，背叛都是最优反应。这是 $n$ 人囚徒困境。原文说均衡是"一人竞赛、其余让步"，这不成立：面对一个竞赛者（强度 0.328），让步者转为竞赛，收益从 −1.056 升到 −0.586。
- **CF。** 合作只在 $k=0$ 时是最优反应（$k=2$ 时也是，但只差一点）。$k=1$ 时最优反应是竞赛（−0.670 对 −0.885）。全体背叛是 Nash 均衡：单独的合作者只得 −1.422，低于 $P=-1.325$。此外还有一个部分均衡：两个竞赛者，加一个两人的合作池。
- 我扫了 $r\in\{1,1.3\}$、$e_c\in\{0.05,\dots,0.4\}$：全体背叛在所有情形下都是均衡，合作在任何情形下都不占优。

所以 CF 做的事是把囚徒困境变成有多重均衡的协调博弈。按"$i$ 对其余人整体"的约化来读：$R=0.140$、$T=0.002$、$P=-1.325$、$S=-1.422$，这是 stag hunt，信任门槛为 0.41。合作是风险占优的（$g_C=0.138>g_D=0.097$）。这仍然是一个有价值的结果，但它需要信任，Theorem C 的"existence without trust"因此不成立。

**是什么在起作用。** 把 $R-T$ 拆开看：
- SEP 基线：−0.726。
- 只加"合作池合力"（效应 iii），$R$ 不变：−0.612。
- 只加"合作者之间不互相臣服"（效应 i），防御仍然分立：+0.024。
- 两者都加：+0.138。

让 $R>T$ 成为可能的，是"合作者不互相臣服"这一假设。这相当于先假设合作者之间的承诺问题已经解决，而这恰恰是 Prop 8 和 Prop 15 所说的难点。

**"盖子"的敏感性。** 这个模型对 $(\Omega,\Omega_c,L_b,e)$ 是一次齐次的。
- 若 $\Omega_c$ 和 $L_b$ 都随 $\Omega$ 同比例变化，则 $e^\ast=0.035\,\Omega$ 恰好成立，且 $R(e^\ast)=0.173\,\Omega>0$。用于盖子的价值份额是常数。
- 若 $\Omega_c=\Omega$ 而 $L_b$ 固定，$\Omega=0.5,1,2,4,8$ 时 $e^\ast=0.0125,0.035,0.10,0.25,0.60$，$R(e^\ast)$ 始终为正。

原文说"陡增"，又说在 $\Omega=2$ 时 $R<0$。这两点都只在"$\Omega$ 上升而 $\Omega_c$、$L_b$ 固定"时才出现，也就是来自比值 $\Omega/\Omega_c$。"The lid grows with the pressure" 应改为"随赢的价值**相对于**合作价值和落后惩罚而增长"。这与 Corollary 1 的说法一致，但 §8.2 的表读起来像是在说绝对量。

**不对称和"排除而不臣服"。** 设潜在背叛者是低成本的领先者，$c_d=0.7, 0.5, 0.3$，合作者 $c=1$。
- 若输掉的背叛者会被臣服，$e^\ast=0.0475, 0.0625, 0.09$，可行。
- 若输掉的背叛者只被排除在共同价值之外，那么对 $c_d\le0.7$，在 $e_c\le2$ 范围内找不到任何 $e_c$ 能使 $T\le R$。原因是 $R=0.25-2.2e_c$，一旦 $e_c>0.19$，它就低于零努力的搭便车者所得 $-0.9e_c$。

因此，对一个更强的领先者，这个构造只有在合作池能臣服它时才成立。而这正是原文自己（§4、§9.4 末尾）警告的权力集中。这个张力应该放进命题主体，不能只留在脚注里。

**文献。** 这是国际环境协议文献里的联盟稳定问题：内部稳定与外部稳定（d'Aspremont et al. 1983；Carraro and Siniscalco 1993；Barrett 1994）。Barrett 的"合作悖论"是：自我执行的协议只有在合作收益小时才能做大。Prop 22(3) 本质上是这一结果在竞赛里的版本。v3 的参考文献库里已经有 barrett1994 和 carraro1993。

**严重程度。** 22(1)、22(2) 按原文表述是**确定错误**；22(3) **表述过强**。

**修复建议。**
- (a) 把命题改写为"大联盟的内部稳定"：$R\ge T$ 当且仅当 $e_c\ge e^\ast$。
- (b) 报告完整的最优反应表和所有均衡，并明确：CF 创造了一个全体合作均衡，但全体背叛均衡仍在；给出门槛和风险占优。
- (c) 把"联盟在察觉背叛后重新优化合力"（Barrett 的 Stackelberg 联盟）加进模型，接上 $\upsilon$。
- (d) 把"成员之间不互相臣服"单列为一个承诺假设。
- (e) 用比值表述盖子。
- (f) 加入不对称的背叛者。

改完之后，Theorem C(1) 应改为"存在一个合作均衡"，而可达性仍需要信任门槛，或者需要 Theorem S。

### E2 "生存优先"的委托条件推错了量度（Prop 6(6)、Theorem S、§12 表中的 D 行）

**位置。** Prop 6(6)；Theorem S 的假设（"under condition D, which for survival-first actors reads $1/n>\Delta\psi$"）；Theorem E 的证明；§12 表中的 D 行。

**问题。** Prop 6 的 $u_i=-L_e(1-w_i)-L_c[1-Q]$（其中 $Q=\prod_j(1-\psi_j)$）是加性损失。令 $L_e=L_c$ 得到的不是生存概率。它重复计算了"既输掉竞赛又失控"这一联合事件，也忽略了第 10 节自己的设定：输掉竞赛只以概率 $p_{\text{dec}}$ 导致臣服。

与第 10 节一致的量度是
$$\Phi_i=Q\cdot\big[w_i+(1-w_i)(1-p)\big].$$
当 $s\to\infty$ 时，委托严格占优的条件是：
- $k=0$ 时：$(1-\psi_1)>(1-\psi_0)\big[1-p\tfrac{n-1}{n}\big]$；
- $k\ge1$ 时：$(1-\psi_1)\big[1-p\tfrac{k}{k+1}\big]>(1-\psi_0)(1-p)$。

**反例**（$n=3$，$r=1$，$s\to\infty$）：

| $(\psi_0,\psi_1,p)$ | 原文条件 $1/n>\Delta\psi$ | $\Phi$ 中委托的收益（$k=0,1,2$） | 实际结论 |
|---|---|---|---|
| (0, 0.5, 1) | 不成立（"不被迫"） | +0.167, +0.125, +0.042 | 被迫委托 |
| (0.01, 0.2, 0.1) | 成立（"被迫"） | −0.122, −0.104, −0.092 | 从不委托 |

两个方向都判错了。

**更深一层。** §10.1 把自主纳入了生存的定义："handed its consequential decisions to systems it can no longer overrule … has not survived"。按这个定义，锁定后的委托本身就是 $\Phi=0$。对生存优先者而言，委托是一个**选择**，不是外生危险。只有当不委托也会让 $\Phi\to0$（被臣服）时，生存优先者才会委托。所以，"被迫委托，因此 $q_{\mathrm I}\to1$"这一推导链不能照原样使用。两种修法任选其一：
- 把 $q_{\mathrm I}$ 定义为条件概率 $\Pr(\text{失去自主}\mid\text{委托})<1$，然后在 $\Phi$ 里推出委托的选择；
- 保留加性模型，但不再把它称为"生存优先"。

此外，$\Phi^T=(1-q_{\mathrm{II}})(1-q_W)$ 里没有 $q_{\mathrm I}$。可是 Prop 6(1) 说，委托收益在 $k=0$（与克制者竞赛）时最大。这两处不一致。补上 $(1-q_{\mathrm I}^T)$ 反而会让 $\Phi^R>\Phi^T$ 更稳。

**严重程度。** **确定错误**（量度用错；结论的偏差方向依参数而定）。

**修复建议。** 用上面的 $\Phi$ 条件替换 Prop 6(6) 和 §12 的 D 行；在 Theorem S 中，把委托写成生存优先者在 $\Phi$ 里的选择。

### E3 Theorem S 的逻辑结构：结论由 $q_{\mathrm{II}}$ 单独承担；"弱占优"推不出；时间范围缺失

**位置。** §10.2 Theorem S、Prop 23；Appendix A；§0、中文概要、§14。

**(a) 冗余与承重。** $\Phi^T$、$\Phi^P$、$\Phi^S$ 三者都含有因子 $(1-q_{\mathrm{II}})$。因此仅凭 $q_{\mathrm{II}}\to1$，结论 (1)、(2) 就成立；$q_{\mathrm I}\to1$ 和 $p_{\text{dec}}\to1$ 对极限结论是多余的，它们只影响极限之前 $S$ 和 $P$ 的排序。

对获胜者（$\Phi^T$）而言，起作用的只有 $q_{\mathrm{II}}$ 和 $q_W$。所以"the one that prevails included"这一说法，完全建立在共享纠错失败（或预防性战争）上，也就是 Prop 7(3) + L1 + K4 作用于单独竞赛者的情形。这应该明说。它不削弱理论，反而说明了论证的核心在哪里。

**(b) 危险率不随局面变化，与 L1 矛盾。** L1 说危险增长率 $a$ 随总竞赛强度不减，因此 $q_{\mathrm{II}}^T$（只有一人竞赛）$\le q_{\mathrm{II}}^P$。$\Phi^R>\Phi^T$ 要求单独竞赛者自己的危险就很大（不妨称为"lone-racer condition"），但这一条不在假设里。

例子：领先者 $\pi_L=0.8$，$q_{\mathrm I}=0.2$，$q_W=0.1$，$p_{\text{dec}}=0.9$，$p^S_{\text{dec}}=0.95$，$q_{\mathrm{II}}^P=0.3$，$q_{\mathrm{II}}^T=0.05$，$h_R=0.15$。得到 $\Phi^R=0.850<\Phi^T=0.855$，$\Phi^P=0.413>\Phi^S=0.035$。领先者在生存意义上面对的是**囚徒困境**。

一般地，这个分类可以是占优、stag hunt、囚徒困境，也可以是 chicken（当 $\Phi^T>\Phi^R$ 且 $\Phi^S>\Phi^P$ 时）。chicken 正是核边缘政策的经典结构。

**(c) "弱占优"推不出。** 附录对 (2) 的证明只推出 $\varpi^\ast_\Phi\to0$。弱占优还需要 $\Phi^S\ge\Phi^P$，也就是 Prop 23(3) 的条件，而它不在 Theorem S 的假设里。

在精确极限下，$\Phi^S=\Phi^P=0$。按 L6 的字典序偏好，平局由次级量度决定。只要次级量度给出 $S<P$（例如 Prop 4(1) 的情形，或 $\theta=-1$ 的目标；在对称、完全耗散的物质收益下则是再次打平），(D,D) 就是字典序博弈的 Nash 均衡。它不是 trembling-hand perfect 的：只要对方以任意 $\varepsilon>0$ 的概率合作，C 在 $\Phi$ 上就严格更好（Selten 1975）。

正确的表述是："(C,C) 风险占优，其吸引域趋于整个信念空间；(D,D) 只作为非完美均衡存留。"相应的选择论证应该是完美性，或者 Prop 13(4) 已用过的 global games，而不是"弱占优"。§0、中文概要和 §14 都应相应改写。

**(d) $u=\Phi V$ 的判据。** 原文的充分条件是"$\Phi$ 之差超过 $V_{hi}/V_{lo}-1$"。它是对的，但太弱：只要 $V_{hi}/V_{lo}\ge2$，这个条件就永远无法满足。而且在极限附近它用错了对象。正确的判据是比值：$\Phi_a/\Phi_b>V_{hi}/V_{lo}$。

例如 $\Phi_a=0.02$、$\Phi_b=0.01$、$V_{hi}/V_{lo}=1.5$：差值判据不成立，比值判据成立。在极限附近，$\Phi^S/\Phi^P$ 由收敛速率决定，假设本身不能确定它。所以在 $u$ 里，$S$ 与 $P$ 的排序是不确定的；能确定的只有 $R$ 对 $T$（$\Phi^R/\Phi^T\to\infty$）。

**(e) 时间范围。** $\Phi$ 是"over the horizon in question"。如果危险按期发生，那么任何为正的常数 $h_R$ 在无限时间范围内都会使 $\Phi^R\to0$。要 $\Phi^R>0$，需要合作下的**累积**危险收敛，即 $\sum_th_{R,t}<\infty$，而竞赛下 $\sum_tq_{\mathrm{II},t}=\infty$。这是一个关于"合作加上纠错能把危险压下来"的实质性假设（类似"time of perils"），应写进定理的假设。可参照 Aschenbrenner (2020) 和 Martin and Pindyck (2015)。

**(f) 独立性。** 极限结论对相关性是稳健的，因为 $\Phi\le1-\max(\text{危险})$。但极限之前的数值和 Prop 23(3) 不稳健：$p_{\text{dec}}$ 与 $q_{\mathrm{II}}$ 由同一个能力增长驱动，正相关会使 $\Phi^P$ 高于乘积公式给出的值。

**(g) 数值说明不全。** §10.2 第三条没给出 $q_W=0.3$；整组数字用的是 $n=2$（`checks_v42.py`），正文却写"$n$ actors symmetric"。

**严重程度。** **表述过强** + **缺少条件**。

**修复建议。** 拆成三个命题：
- (1′) 若每个竞赛局面 $X$ 下都有 $q_{\mathrm{II}}^X\to1$，且合作下累积 $h_R$ 有界，则所有竞赛分支 $\Phi\to0$；
- (2′) 对任意正的信任，合作都是最优反应；(D,D) 不是完美均衡；
- (3′) 合作弱占优当且仅当 Prop 23(3) 成立。

把危险率写成依赖局面的形式（$q_{\mathrm{II}}^T,q_{\mathrm{II}}^S,q_{\mathrm{II}}^P,h_R$），并用 L1 把它们与总强度联系起来。

### E4 异质性与过渡（Corollary 2）：领先者、$n$ 人博弈、信念与可信度、选择层

**位置。** Theorem S、Prop 23(3)、Prop 24、Corollary 2、§10.3、§13。

**(a) 领先者。** 设领先者在竞赛中获胜的概率为 $\pi_L$，则
$$\Phi^P_L=(1-q_{\mathrm I}^L)(1-q_{\mathrm{II}})(1-q_W^L)\big(1-p_{\text{dec}}(1-\pi_L)\big),\qquad\Phi^S_L=(1-q_{\mathrm{II}})(1-p^S_{\text{dec}}).$$
对主要行动者，退出等于把决定性优势交给对手，所以 $p^S\to1$，从而 $\Phi^S_L\approx0$。这时 $S$ 对 $P$ 的比较，只有在 $q_{\mathrm I}^L$ 或 $q_W^L$ 接近 1 时才对退出有利。可是已经领先的一方委托压力最小：它委托带来的 $\Delta w$ 很小。

例子：$\pi_L=0.8$，$q_{\mathrm I}=0.2$，$q_W=0.2$，$q_{\mathrm{II}}=0.3$，$p_{\text{dec}}=0.9$，$p^S=0.95$，$h_R=0.1$。结果是 stag hunt，门槛 **0.494**。把共享的 $q_{\mathrm{II}}$ 提到 0.8，门槛降到 0.114。

所以对领先者，承重的是共享的节奏危险，而不是被迫委托或臣服。Prop 24（单方面实行 E1）对小行动者（$p^S\approx p$）是可信的，对两个最领先的行动者则不可信。偏偏他们才是关键。

**(b) $n$ 人博弈与最弱环节。** $R$ 要求其余 $n-1$ 人**全部**合作。Prop 4(4) 自己也说，只要一人竞赛，竞赛就开始。若信念相互独立，个体所需信任为 $\varpi\ge(\varpi^\ast)^{1/(n-1)}$。原文例子中的门槛 0.047，在 $n=4$ 时变成 0.361，$n=8$ 时变成 0.646。最小努力博弈的实验（Van Huyck, Battalio and Beil 1990）显示，协调失败随人数增加。

**(c) 信念。** Corollary 2 需要的不只是一个共享的预测，而是所有有能力的行动者之间的共同知识。在非共同先验下，理性推理不能保证意见一致（Aumann 1976）。互相乐观的文献（Fey and Ramsay 2007；Smith and Stam 2004）说明的情形是：每一方都相信自己会是那个保持控制的赢家。这正是 Theorem S(4) 列出的那种信念。

**(d) 预测的可信度。** 按本文自己的 Prop 14，对手说"竞赛会害死所有人"，这一信息偏向让接收者克制（$b=\lambda\beta_s$）。在竞争关系下，除非 $b<1/4$，它并不可信。可信的预测必须来自接收者能核查的证据，或者来自独立渠道（I3），而独立渠道本身也是一个受 Props 9–11 约束的纠错者。所以"先改预测、后有信任"预设了一个未被俘获的证据渠道。

但这里有一个对作者有利的细节。在共享分量 $q_{\mathrm{II}}$ 上，双方的利益是一致的，关于它的信息可以可信；关于 $p_{\text{dec}}$、$q_{\mathrm I}$ 的信息则不行。(a) 已经表明，领先者的论证恰恰由 $q_{\mathrm{II}}$ 承担。因此 Corollary 2 应限定在"共享危险的预测"上。这样限定之后，它反而成立。

**(e) 层次（§1.7 规则 2 的违反）。** $q_{\mathrm{II}}$ 是所有人共有的项。由 Lemma 0，载体之间的选择看不见它。改变决策者的预测，不会改变各行动者内部和之间对"做法"的选择；§4.4 和 Remark 3 自己也说"winner is a field"。§10.3 的"oppose the objective"等于假设：只要证明 $\theta=-1$ 降低 $\Phi$，它就会被放弃。可是如果这个目标真是被选择出来的，选择并不响应 $\Phi$。所以过渡必须是两件事：策略层上改变预测，**加上**载体层上改变收益（$\tau_{\text{eff}}>\nu$，Theorem 2）。Corollary 2 只写了前一件。

**(f) 时间一致性。** Corollary 2 只在委托锁定之前适用；$T_{\text{lock}}$ 之后，做决定的已经不是原来的决策者。这一点应写成条件。

**(g) 一个建设性的补充。** 对模糊厌恶的 maxmin 行动者（Gilboa and Schmeidler 1989），信任门槛无关紧要：对他人行动取 maxmin，比较的就是 $S$ 和 $P$。这时决定性的条件是 Prop 23(3)，而不是门槛，而 (a) 恰好表明领先者在哪里不满足它。

**严重程度。** **缺少条件**。

### E5 K7 与 $\Delta^{\text{coop}}$：定义不良；如何使其可推导

**位置。** §6.2；§12 表中的 K7 行；Appendix A 中 Theorem A 的 "The comparison"。

**定义上的问题。**
1. 集合 $U$ 跨越了不同模型，各有不同的策略空间和量度：Prop 4 用目标量度或 $\pi$，Prop 6 用加性损失，Prop 8 用谈判价值，"win then govern"根本没有模型。要定义"$U$ 中的最佳路径"，需要一个共同的收益函数。
2. "避免的损失"和"放弃的租金"都需要一个反事实，即其他人采取什么策略。"与克制者竞赛"对应激励相容约束（IC，即 $T$）；"加入竞赛"对应参与约束（IR，分歧点 $P$）。K7 把这两种约束混在一起了。
3. 三个括号一般不能相加：危险与租金之间有交互项。

**如何使其可推导。**

(a) **非对称竞赛中领先者的租金有闭式解。** 在全支付竞赛中，设成本 $c_1<c_2$，共同奖金差为 $\Omega+L_b$。强者的租金是 $(\Omega+L_b)(1-c_1/c_2)$，弱者对加入与不加入无差异（Hillman and Riley 1989；Baye, Kovenock and de Vries 1996）。模拟验证（40 万次抽样，与闭式解一致到 0.002 以内）：

| $(\Omega,L_b,c_1,c_2)$ | 强者加入 | 闭式解 | 弱者加入 | 退出 |
|---|---|---|---|---|
| (1, 1, 0.5, 1) | −0.001 | 0.000 | −0.999 | −1.000 |
| (1, 5, 0.5, 1) | −2.004 | −2.000 | −5.000 | −5.000 |

所以 Prop 4(3) 的"joining buys nothing"对除最强者以外的所有人成立；**最强者从加入中得到的收益随 $L_b$ 增加**。这就是 K7 难点的闭式表达。Tullock 型的类似结果见 Nti (1999) 和 Stein (2002)。

(b) 把各类危险写成总强度的函数，让 L1 显式化。

(c) 把合作安排写成一个带分配规则 $s_i$ 的机制：
- IR：$s_i\Omega_c-\text{成本}\ge U_i^{\text{race}}$；
- IC：$s_i\Omega_c-\text{成本}\ge T_i$。

在可转移效用下，满足所有 IR 的分配规则存在，当且仅当合作的总剩余不小于各方竞赛收益之和。这一点可以由"耗散加共同损失"（把 Prop 5 推广到非对称情形）推出。于是 K7 分解为两部分：可推导的总效率，加上分配规则是否可行这一制度问题。

(d) **一个必须正视的张力。** 满足领先者 IR 的分配必须反映它的外部选项（Binmore, Rubinstein and Wolinsky 1986），也就是一种"比例安排"。可是 Prop 15(3) 说，比例安排保留了退出动机。

(e) 若行动者私下知道自己的能力（也就是外部选项），Myerson and Satterthwaite (1983) 意味着：同时满足 IR、IC 和预算平衡的机制，不能保证以概率 1 达成有效协议。Cramton, Gibbons and Klemperer (1987) 则表明，初始位置足够对称时，有效解散是可行的。对应到本文：验证（$\upsilon$）减少私人信息；位置越不对称，有效协议越难。这为 Theorem B 提供了一个机制设计的基础。

(f) Theorem S 的角色可以重新理解为：它在 $\Phi$ 中压低了每一方的外部选项，从而扩大了核。由于 $\Phi$ 不可转移，K7 在 $\Phi$ 中应写成 $\Phi^R_i\ge\max_U\Phi_i$，而不是"net material gain"。

**严重程度。** **缺少条件**。

### E6 §1.7 的层次纪律仍有泄漏

**位置与问题。** 下面每条都违反了规则 1 或规则 3，或者混用了量度。

- l.396（Prop 4(2) 末句）、l.659（Theorem A(b)）：写的是 "the relative objective that selection produces (Proposition 3(4))"。可是 Prop 3(4) 自己说，它讲的是行动，不是目标。
- l.1175、l.1194（§10.3）："the objective that relative selection produces"；"The objective is a selected preference (Proposition 3(4))"。
- l.1382（§13）："That preference is also a product of the selection in Proposition 3(4)"。
- Remark 3（l.450）、§6.3 表（l.711）、Prop 25(2)（l.874）、§13（l.1360）："a faithful system pursues its operator's relative objective"。这预设了操作者持有 $\theta=-1$，属于策略层的假设。若操作者的 $\theta=\kappa$，一个忠实的系统追求的是 $\theta=\kappa$。应改为"追求操作者的目标；在竞赛下，该目标在 X 的程度上是相对的"。
- Prop 6(4)（l.437）："$L_c$ cancels (Lemma 0)"。Lemma 0 讲的是选择规则；相对目标里共同项相消，是另一个代数事实（见 Prop 3 证明中的展开）。
- Remark 6 第二条："A winner whose objective is relative does not see it (Lemma 0) and consumes it"。落后者的自主供给不是共同项。相对目标对落后者的收益赋予负权重，所以赢家看得见它，而且有动机去毁掉它（恶意）。结论更强，但给出的理由错了。另外，把单个行动者自己的供给称为"part of the host"，与 §1.1 的定义（共享条件）冲突。
- §0 第 3 层、§14 的列表："in material terms, joining buys nothing that staying out would not"。这只在完全耗散的对称极限下成立。当 $r<n/(n-1)$ 时，加入的收益是 $(\Omega+L_b)/n\cdot(1-r(n-1)/n)>0$，而且随 $L_b$ 增加；不对称情形见 E5(a)。
- (4) 式把一个相对收益记作 $W(q)$，而 §1.3 和 §1.7 里 $W$ 是真实福利。恰恰在这一节出现符号混用。建议改名，例如 $\Delta\pi^q$。
- Prop 22 没有说明它用的量度（实际是 $\theta=0$ 时的 $\pi$），违反规则 3。
- §7.4 的 "true payoffs/true measure" 在 $W$ 和 $\Phi$ 之间含糊。
- §0 说："The survival argument … needs fewer conditions than the rest"。它实际需要 L1、L3–L6、D（而且 D 写错了，见 E2）、$q_{\mathrm{II}}$ 的稳健纠错界（K4 + Prop 7(3)）、合作下累积 $h_R$ 有界、对称（极限之前）、以及不依赖局面的危险率（E3(b)）。"条件更少"的说法过强。§0 的 "In today's world reason says clearly that the actors must cooperate" 也超出了这些条件性结果。

**严重程度。** **表述过强**。

**修复建议。** 逐处改为"selection on actions favours the behaviour of …"；需要偏好层结论的地方，引用 E7 的文献并写明条件。

### E7 Prop 3(4) 与间接演化方法：文献实际意味着什么

**原文范围声明。** "Whether preferences themselves evolve to $\theta=-1$ depends on whether preferences are observed … not modelled here"。这个声明是对的，但不完整，并且与 §9.4 相冲突。

**文献分三类：**
1. **作用于行动的选择，有限群体对抗全场。** 这时选出的是 Schaffer ESS，即 $\theta=-1$ 的行为（Schaffer 1988；Hehenkamp, Leininger and Possajennikov 2004）。模仿动态也给出同样结果（Vega-Redondo 1997；Alós-Ferrer and Ania 2005）。原文在这一点上是对的。
2. **偏好不可观察。** 在随机匹配的大群体里，选出的是物质收益下的 Nash 行为，即 $\theta=0$ 而不是 $-1$（Ok and Vega-Redondo 2001；Ely and Yilankaya 2001；Dekel, Ely and Yilankaya 2007 在零可观察度时的结果）。在对抗全场的有限群体里，选出的是 Schaffer 行为，等价于 $\theta=-1$。所以 $-1$ 还是 $0$ 取决于**群体结构**：前沿上只有少数行动者，属于有限情形；Prop 1 中众多载体之间的复制子动态，属于大群体情形。
3. **偏好可观察。** 一般而言，物质收益最大化者不稳定，选出的扭曲方向由策略斜率决定（Güth and Yaari 1992；Bester and Güth 1998；Possajennikov 2000；Heifetz, Shannon and Spiegel 2007）。

   以 $r=1$ 的 Tullock 竞赛为例，在对称均衡处，最优反应对其他人总强度的斜率是 $(2-n)/(2(n-1))$。$n=2$ 时斜率为零，没有一阶承诺价值（Dixit 1987）；$n\ge3$ 时是策略替代，承诺更激进有利，因此偏向恶意，即 $\theta<0$（Koçkesen, Ok and Sethi 2000 讨论了 aggregative games）。但 $\theta=-1$ 一般不是精确的被选点。Leininger (2009, *Public Choice*) 专门研究了竞赛中的演化稳定偏好，作者应核对其结论。

   在高可观察度、可重新匹配的条件下，DEY (2007) 表明只有有效结果是稳定的，这是一条合作性偏好可以被选择的路径。在有正向配对时，Alger and Weibull (2013) 得到 homo moralis；在有结构的有限群体里，Alger, Weibull and Lehmann (2020) 得到"局部竞争带来的恶意 + Kantian 成分"。

**对本文的含义。**
- (i) Prop 3(4) 应写明："$\theta=-1$ 行为是有限群体、偏好不可观察时的预测；偏好可观察时，$n\ge3$ 的预测是被承诺扭曲的 $\theta<0$；在高可观察度并有正向配对时，合作性偏好可以稳定。"
- (ii) §9.4 的 "the accurate self-model … is individually rational whatever others do"，以及 §2.3 "In plain words" 里的 "whatever the others do"，只在他人**行动**固定时成立。一旦自我模型可被观察（本文自己的 Remark 就设想了这种情形），$\theta=\kappa$ 就不是最优的：稍微更激进的自我模型能得到更高的物质收益（KOS 2000；HSS 2007）。因此"纠正自我模型"本身也处在一场承诺竞赛之中，除非博弈改变。这与本文 Remark 中的 "second-order race" 一致，却与 §9.4 的说法矛盾。
- (iii) DEY 和 Alger–Weibull 的结果对本文其实是资源：它们说明了在什么条件下 §10.3 期望的偏好转变能够自我维持（高可观察度加正向配对），可以直接用来支持 Def 3(f)。

**严重程度。** **定位问题** + **表述过强**（§9.4）。

### E8 Corollary 3 与 Theorem E 的逻辑结构

**(a) 对 (A) 的两种定义来回切换。** (A) 被定义为 "the pace the contest sets"，这本身就预设了 (K)。
- 在 (1) 中，(A) 经由 L1 在 (K) 之下推出 H3。
- 在 (3) 中，(A) 被重新解释为"在竞赛之外、在纠错节奏之内的快速发展"，也就是 $\neg$H3。

按第一种定义，(A)∧¬(K) 是空集，(A)∧(S) 无论如何都不可能；按第二种定义，(1) 推不出来。所谓"三选二"其实是一个两难：(K)∧(A$_{\text{contest}}$) ⇒ ¬(S)；要在安全的前提下求快，就必须离开竞赛。Rodrik 式的三难困境要求每一对都可行，而这里有一对是靠改写定义才变得可行的。

**(b) 哪个假设真正承重。** 每个竞赛分支都含有 $(1-q_{\mathrm{II}})$，所以单靠 H3（经由 $q_{\mathrm{II}}\to1$）就足以让所有竞赛分支的生存趋于零；H0–H2 只是经由 L1 作为 H3 的原因进入。由此：
- 在 $\Phi$ 中逻辑上必要的出口是 $\neg$H3；
- E0 之所以是出口，是因为 Def 3(e) 把 E3 内置进去了；
- E1、E2 只有在它们（经由 L1）把 $a$ 压到稳健纠错界以下时才是出口，这是一个额外的因果主张。

E1 → E2/E3 这个次序是规范和策略上的判断（在锁定之前让人仍然是参与者），并不是从 Theorem E 推出来的。应该明说这一点。

**(c)** Theorem E 的证明使用了 D，而 D 写错了（见 E2）。

**严重程度。** **表述过强**。

### E9 L4 与 L6 的一致性；核边缘政策

**(a)** Theorem S 同时用了 L6（所有人都生存优先）和 L4（拥有相对目标的决定性赢家会把支配扩展到所有人）。如果所有人都生存优先，那个持相对目标的赢家从哪里来？有三种可能：
- 赢家是一个被委托的过程，那就归入 $q_{\mathrm I}$ 或 $q_{\mathrm{II}}$；
- L4 从无政府状态下的求生推出（攻势现实主义，Mearsheimer 2001，正文已引）；
- L4 从承诺问题推出：赢家无法可信地承诺不剥削（Fearon 1995；Powell 2006）。

后两种推导都能在没有任何"cancerous preference"的情况下得到 L4 式的结果。这会改变 §10.3 的规范结论：要反对的是一种**结构**（无政府状态 + 决定性优势 + 缺少承诺装置），而不是一种偏好。这样立论更稳，也更不容易被读成道德指控。

**(b)** 把 L6 当作行为假设，要面对 Schelling (1960, 1966) 和 Powell (1990) 的核边缘政策：行动者会**故意**操纵共享的灾难风险，把它当作工具。Prop 25(1) 的"以破坏威胁来威慑"正是这种做法。在核边缘政策下，共享风险是策略选择的结果，生存博弈的结构是 chicken。§13 的回答（"such actors hold the cancerous objective"）是在给理论免疫：定理根本不覆盖这类行动者。应该明说这一点，并单独分析 chicken。

**(c)** L6 的微观基础：在 $u=\Phi V$ 中，若 CRRA 系数 $\gamma>1$，效用有上界，于是 $V_{hi}/V_{lo}$ 有界，生存的利害占主导（Jones 2016, 2024）。Jones (2024) 表明，当 $\gamma\ge2$ 左右时，即使增长收益很大，能容忍的存在性风险也很小。这比字典序更干净，也更容易引用。

**严重程度。** **缺少条件** / **定位问题**。

### E10 Prop 11 的速率条件：推导正确，但经济含义比正文写的温和

**核对结果。** $s_{\mathsf E}=A/(c_{\mathsf E}d)+Z_\eta\gamma^{-1/\eta}d^{-(1+\eta)/\eta}$；所需速率 $\alpha\ge g/(1+\eta)$；$\eta=1$ 时的根也对。这里的经济直觉是：$d$ 出现两次（既缩短规则支持的寿命，又缩小被培养的能力），$\gamma$ 只出现一次。

**(a) 对称的 AI 降本。** 若 AI 以相同速率降低控制成本和独立纠错成本（$g_c=g$），那么即使预算增长 $b=0$，由于 $g_c\ge g/(1+\eta)$，证书也一直成立。所以 §0 第 4 层"the independent correction required rises as AI cheapens control"，就所需水平 $d^\ast(t)$ 而言是真的，就可行性而言不是。证书失效要求 $g>(1+\eta)(b+g_c)$：控制成本下降的速度必须是纠错成本下降速度的 $(1+\eta)$ 倍。这实际上加强了"给独立纠错者配备 AI"这一处方，应该正面写出来。

**(b) 依赖函数形式。** 若转换是凹的，$\hat b\,q^\beta$（$\beta\le1$），则所需速率为 $\alpha\ge\beta g/(1+\eta)$。推导：$q^\ast\propto(\gamma d)^{-1/(1+\eta-\beta)}$；数值核对时，被培养项在临界值两侧的增长率为 ±0.020（$\beta=1$）和 ±0.0067（$\beta=0.5$）。所以"只需一半速度"是函数形式造成的。稳健的内容是："所需速率 = $g$ × 培养的规模收益 ÷（1 + 成本凸性）"。

**(c) 速率不可能无限增长。** $d$ 是纠正规则支持的速率（单位是 1/时间），它受制度时间常数的约束，Prop 7 的节奏界也适用于它。让 $d$ 永远指数增长是不现实的。若 $d$ 有界且 $f=0$，那么任何 $g>0$ 最终都会让证书失效。真正持久的补救是 $\chi\to0$（不可占有性）、$f>0$ 的下限、以及结构性分拆（$k^{2/\eta}$）。政策重心应相应移动。

**(d) 准静态。** $q^\ast$ 假设选择能跟上不断移动的最优点；选择速度有限时会有滞后。这一点影响不大，但应说明。

**(e) 加总。** $f=0$ 时，第 $k$ 个载体的梯度是 $\chi p_k^2\,\bar y^\top M\bar y$，所以整个场的俘获压力正比于 $\sum_kp_k^2=$ **HHI**。这把 Prop 9 接到了产业组织里的集中度度量和结构性补救上，值得写出来。

**(f) 定位。** Laffont and Tirole (1991, 1993)：俘获受利害大小和合谋交易成本的约束；AI 降低 $\gamma$，相当于合谋的交易成本下降；他们的补救（降低利害、降低激励强度）对应于 $\chi\to0$。Martimort (1999)：俘获随关系持续时间加深，是一种动态俘获。综述见 Dal Bó (2006)。

**严重程度。** **定位问题**；§0 的相应说法**表述过强**。

### E11 "二阶选择"的新颖性需要定位

**相关文献。**
- 俘获理论：Stigler (1971)；Peltzman (1976)（俘获程度是内点、连续的）；Becker (1983)；Grossman and Helpman (1994)；Laffont–Tirole；Martimort。
- 制度与权力：Acemoglu and Robinson (2006) 的 political replacement effect，(2008) 的 captured democracy；Glaeser, Scheinkman and Shleifer (2003) 的制度颠覆随不平等加剧，这与本文的 $p^2$ 相似；Sonin (2003)；Greif and Laitin (2004) 的准参数与自我强化的制度。
- 政策反馈：Pierson (1993, 2000)。
- 公地治理：Ostrom (1990) 的第 4 条设计原则（监督者对使用者负责），这正是 I2 要解决的问题。
- 惩罚制度：反社会惩罚（Herrmann, Thöni and Gächter 2008）；池惩罚（Sigmund et al. 2010，正文已引）。

**真正的新内容。**
- (i) 把俘获写成跨耦合领域的频率依赖选择：有转换矩阵、行和证书，以及 $k$-core 和级联结果；
- (ii) 控制能力以 $p^2$ 和规模门槛的 Price/Hamilton 形式被选择；
- (iii) 在控制成本下降时的速率比较。

(i) 和 (ii) 是把 Stigler、Olson、Acemoglu–Robinson 用演化语言重新形式化，新颖性有限但真实。(iii) 最原创，但见 E10。

还应说明：(3) 式的双稳态 $x\in\{0,1\}$ 来自 logistic–线性动态这一函数形式。Peltzman 式的最优化规制者给出的是内点的、连续变化的俘获；所以门槛和级联结果是模型特定的。

另外，v3.1 的 Related Work 段落已经引用了上面大部分文献，v4.3 正文没有保留，应恢复。

**严重程度。** **定位问题**。

### E12 I1 不是"责任"；庇古工具在复制子动态下的形态

**(a) 定义冲突。** §1.1 把 host 定义为"其成本不会通过顾客、声誉、法院回到源头"的部分。按这个定义，对 host 损害的"责任"不可能经由法院实现，I1 实际上是对可观察代理变量收取的规制性收费或禁令。§9.5 自己也承认这一点。应引用 Shavell (1984) 关于事前规制与事后责任的分析（判决豁免、损害分散、无人起诉），以及 Shavell (1986)。

**(b) 规范框架。** $\tau>\nu$ 是一个角点禁令。在线性 $G$ 下，只有 $\Theta>1$ 时它才是有效的；若 $\Theta<1$ 而 C0 成立，线性 $G$ 下"有效"的结果会越过底线。所以本文的规范框架是约束式的（safe minimum standard，Ciriacy-Wantrup 1952）。Weitzman (1974) 表明，在门槛附近边际损害很陡时，数量工具优于价格工具。这个规范选择应明说。

**(c) 建设性建议。** 在复制子选择下，常数收费无法把 $E$ 引到内点目标：$\tau<\nu$ 时 $E\to\bar e$，$\tau>\nu$ 时 $E\to e_{\min}$，$\tau=\nu$ 时选择中性。要瞄准与底线相容的负荷 $E^\ast$，可以用随负荷变化的反馈式庇古收费 $\tau(E)=\nu+k(E-E^\ast)$，它使 $E^\ast$ 在复制子动态下渐近稳定；或者用可交易的总量上限。

**(d)** Theorem 2(3) 的必要条件，我核过证明，是对的。它是必要而远非充分的条件：$\tau=\nu-1/(1+t)$ 满足它，底线却仍被越过。原文的写法对此是诚实的。

**严重程度。** **定位问题**。

### E13 一阶部分的定位：本文相对于公地文献到底多了什么

- (a) Lemma 0 是复制子和模仿动态的平移不变性（Weibull 1995；Hofbauer and Sigmund 1998），它的经济内容全在 A1。
- (b) Prop 1(2) 是没有传递项的 Price 方程（Price 1970；Frank 1995），应在这里引用，而不只在 Prop 9 引用。
- (c) **本文真正多出来的一点应明说。** Hardin、Gordon、Olson 的公地悲剧，需要每个行动者在共同损失中的私人份额足够小（Prop 2 中 $\lambda=0$ 时即 $n>\Theta$）。而相对收益上的选择，即使对 Olson 意义上的"特权集团"（$n<\Theta$，每个人在绝对收益下都会克制）也会把公地耗尽，因为无论规模多大，$G$ 都会相消。Prop 2 的 $\lambda$ 则说明了地位关切如何摧毁特权集团（Olson 1965；Hirsch 1976；Frank 1985；Vega-Redondo 1997）。这是本文一阶部分的真正贡献，目前没有写出来。
- (d) §13 回应 "This is the tragedy of the commons" 时，现在一篇文献都没引；应恢复 Hardin、Ostrom、Olson。

**严重程度。** **定位问题**。

### E14 Prop 4(3) 与 Remark 6 的细节

- (a) 在全支付竞赛或 $r\ge2$ 的极限下，$P=S$ 是混合均衡的无差异性质：支撑集里的每个出价收益相同，前提是其他人的混合策略固定。如果退出是可观察的，其他人会重新优化。以 $n=2$ 的全支付竞赛、带共同损失为例：加入的收益是 $-L_b-\ell E[e_j]=-1.231$，可信退出的收益是 $-L_b=-1.000$（对手以接近零的努力获胜）。在物质收益上，退出严格更好，差额为 $\ell E[e_j]$。这支持本文的论点，但代价是确定被臣服，而这已经计入 $L_b$。
- (b) 不对称情形见 E5(a)。
- (c) Remark 6 说"Under L4, $L_b$ is unbounded"。可是当 $r<n/(n-1)$ 时，$P-S=(\Omega+L_b)/n\cdot(1-r(n-1)/n)\to\infty$，加入会变得无限有吸引力；只有对称的完全耗散极限才保持 $P=S$。Remark 6 中 "Two things survive: … joining buys nothing" 必须带上"对称、完全耗散"这两个限定。
- (d) 文献：竞赛中的惩罚，见 Moldovanu, Sela and Shi (2012)。

**严重程度。** **缺少条件** / **小问题**。

### E15 Prop 24 把 E1 等同于 $\Phi^S$

"把 AI 排除在自己的竞赛行为之外"（E1）不等于零强度的克制（$\Phi^S$）。一个以人的节奏参与竞赛的行动者，有它自己的获胜概率 $w^H$ 和 $q_W^H$：
$$\Phi^H=(1-q_{\mathrm{II}})(1-q_W^H)\big(1-p_{\text{dec}}(1-w^H)\big).$$
随着对手的 $s$ 增长，$w^H\to0$，条件趋近 Prop 23(3)。但这是一个推导结果，不是恒等式，应写出来。

**严重程度。** **小问题**。

### E16 其他小问题

- 符号冲突：(4) 式的 $W(q)$ 与真实福利 $W$；Prop 21 证明中用作 Lyapunov 函数的 $\Phi$ 与生存概率 $\Phi$；host 函数 $G$ 与 Prop 13(2) 的 $G=T-R$；控制能力 $q$ 与 $q_{\mathrm I}$ 等；Remark 5 的报警水平 $a$ 与增长率 $a$；Prop 13(2) 的 $L$ 与 $L_i$、$L_b$、$L_e$。v4.2 声称已经修好符号问题，但这几处还在。
- Prop 2 说 "Selection corresponds to $\lambda\to\infty$"。在有许多小载体的复制子动态下，被选行为同样对应于 $\lambda=0$、$n\to\infty$（价格接受者）。在本文的线性模型里两者重合，应说明。
- 建议把本评审的反例写进 `checks_v43.py`：Prop 22 的 $n$ 人最优反应表、$\Phi$ 中的委托条件、领先者的生存博弈、非对称全支付竞赛的租金。这与 v4.2 的做法一致，即用"打破旧表述的那个反例"来检验修复。

---

## 3. 必须对话的文献，以及它们会改变什么

| 文献 | 改变什么 |
|---|---|
| d'Aspremont et al. 1983；Carraro and Siniscalco 1993；**Barrett 1994** | Prop 22 应改写为联盟的内部和外部稳定；"盖子随压力增长"就是 Barrett 的合作悖论；联盟对背叛的重新优化应纳入模型（E1） |
| Van Huyck, Battalio and Beil 1990；Selten 1975；Carlsson and van Damme 1993 | $n$ 人最弱环节结构；以完美性和风险占优取代"弱占优"（E3、E4） |
| Hillman and Riley 1989；Baye, Kovenock and de Vries 1996；Nti 1999；Stein 2002；Moldovanu, Sela and Shi 2012 | 领先者租金有闭式解；"joining buys nothing"不适用于最强者；K7 可以推导（E5、E14） |
| Myerson and Satterthwaite 1983；Cramton, Gibbons and Klemperer 1987；Binmore, Rubinstein and Wolinsky 1986 | 私人能力信息下有效协议不可能，位置对称时可能；外部选项决定分配，与 Prop 15(3) 形成张力（E5） |
| Schaffer 1988；**Vega-Redondo 1997**；Alós-Ferrer and Ania 2005；Hehenkamp, Leininger and Possajennikov 2004 | Prop 3(4) 在行动层成立；一阶部分的贡献应表述为"特权集团也会耗尽公地"（E7、E13） |
| Güth and Yaari 1992；Bester and Güth 1998；Possajennikov 2000；**Koçkesen, Ok and Sethi 2000**；**Heifetz, Shannon and Spiegel 2007**；**Dekel, Ely and Yilankaya 2007**；Ok and Vega-Redondo 2001；**Alger and Weibull 2013**；Alger, Weibull and Lehmann 2020；Leininger 2009（请核对） | $\theta=-1$ 是一个角点；可观察时 $\theta=\kappa$ 不稳定，§9.4 需要修改；高可观察度和正向配对是合作性偏好得以稳定的条件（E7） |
| **Stigler 1971**；Peltzman 1976；Becker 1983；**Laffont and Tirole 1991, 1993**；**Martimort 1999**；Dal Bó 2006；Grossman and Helpman 1994 | 为第二阶理论定位；AI 降低 $\gamma$ 对应合谋交易成本下降；Peltzman 的内点俘获与本文双稳态的对比（E10、E11） |
| Acemoglu and Robinson 2006, 2008；Glaeser, Scheinkman and Shleifer 2003；Greif and Laitin 2004；Pierson 1993 | political replacement effect、制度颠覆、准参数；$p^2$ 与 HHI（E10、E11） |
| Hardin 1968；**Ostrom 1990**；Olson 1965；Bergstrom, Blume and Varian 1986 | 一阶部分的基线；Ostrom 的"可问责的监督者"就是 I2；私人供给的中性（Prop 10(3)、(5)） |
| **Shavell 1984, 1986**；Kolstad, Ulen and Johnson 1990；**Weitzman 1974**；Ciriacy-Wantrup 1952 | I1 是事前规制，不是责任；在门槛附近数量工具优于价格；约束式的规范框架（E12） |
| Schelling 1960, 1966；Powell 1990；Chassang and Padró i Miquel 2010；Baliga and Sjöström 2004；Fey and Ramsay 2007；Aumann 1976 | 核边缘政策（共享风险作为工具，chicken）；策略风险下威慑可能适得其反；军备竞赛中的私人信息；互相乐观与非共同先验（E4、E9） |
| **Jones 2016, 2024**；**Aschenbrenner 2020**；**Martin and Pindyck 2015**；Weitzman 2009；Gilboa and Schmeidler 1989 | L6 的 CRRA 微观基础；"time of perils"与累积危险；多重灾难之间相互依赖，因此出口不能逐个评估；maxmin 下 Prop 23(3) 是决定性条件（E3、E4、E9） |
| Armstrong, Bostrom and Shulman 2016（已引）；**Askell, Brundage and Hadfield 2019**；**Han, Pereira, Santos and Lenaerts 2020**；Naudé and Dimitri 2020；Stafford, Trager and Dafoe 2022；Emery-Xu, Park and Trager（请核对发表处） | 直接以 AI 竞赛为对象的经济学和演化博弈文献；本文的竞赛结果与它们重叠，需要说明差异（E11） |

v3 的参考文献库里已有其中约一半（stigler1971、peltzman1976、laffont1991、dalbo2006、ostrom1990、hardin1968、olson1965、vegaredondo1997、kockesen2000、algerweibull2013、barrett1994、carraro1993、shavell1986、askell2019、han2020、frank1985、hirsch1976）。恢复 v3.1 的 Related Work 并加以扩展，是成本最低的一步。

---

## 4. 正确且有价值的部分

**我核对过并确认无误的结果：**
- Prop 2 的代数、阈值 $\bar\lambda$ 和重复博弈的临界值（0.11、0.47、0.95）；
- Prop 3 的闭式解和 $W(\theta)$ 的单调性；
- Prop 4(3) 的闭式解及其要点：落后惩罚是奖金差的一部分；
- Prop 5 的公式及数值 1.27；
- Prop 6(1)–(5) 在其自身量度内；
- Prop 11 的代数和速率；
- Prop 13 的修复；
- Prop 17；
- Props 19–21；
- Prop 23(3) 的代数；
- Theorem 2(3) 的证明。

v4.2 和 v4.3 对上一轮外部评审的修复，在我检查的范围内都成立。

**值得保留并强调的内容：**
1. **§1.7 本身。** 区分选择层和策略层，区分 $O/\pi/W/\Phi$，在这类跨学科理论里很少见。要做的是把它贯彻到第 8、10、13 节（E6）。
2. **一阶部分的真正贡献。** 相对选择即使在特权集团中也会耗尽公地；地位关切 $\lambda$ 会摧毁 Olson 的特权集团。只要写清楚（E13），这是对公地文献的实在补充。
3. **第二阶理论。** 控制矫正者的能力以 $p^2$ 和规模门槛被选择，纠错是二阶公共品，再加上 AI 改变两个速率之比。它为 Stigler 和 Laffont–Tirole 提供了一个动态的、选择论的版本。它的政策含义（不可占有性 $\chi\to0$、按 $k^{2/\eta}$ 的结构性分拆、给独立纠错者配备 AI）在修正 E10 之后会更锋利。
4. **观察层。** 掩蔽同时削弱所有依赖报告的去中心化出口（§5.3），而以行动为基础的验证不受影响。这是一个清楚、可检验的贡献。
5. **信任分析。** 把信任门槛放进赢的价值、验证、脆弱性和惩罚四个杠杆的框架里，"验证放大信任而不产生信任"有清楚的模型含义。
6. **修正后的生存分析核心。** 经 E3 和 E4 修正后，第 10 节有一个比现在更强的版本："对每一个行动者，包括领先者，竞赛不安全，是因为共享的纠错失败 $q_{\mathrm{II}}$；在这个分量上各方利益一致，所以关于它的预测可以可信地传递；它对载体层的选择不可见，所以除了改变预测，还必须改变收益（$\tau_{\text{eff}}>\nu$）。"这把 Theorem S、Prop 14、Lemma 0 和 Theorem 2 连成一个整体，正是作者想要的"一个理论"。
7. **诚实的条件化。** 四层结构、每个组合定理列出它继承的条件、第 12 节的可证伪表。这些做法本身值得保持。
