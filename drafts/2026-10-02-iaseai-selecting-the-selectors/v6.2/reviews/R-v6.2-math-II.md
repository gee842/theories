# R-v6.2-math-II：数学评审（下半，第 6–11 节与 S6–S11）

评审对象：`v6.2/THEORY.md` 第 6–11 节，`v6.2/SUPPLEMENT.md` S6–S11，以及它们在 CLAIMS、S7 矩阵和表 9.1、11.3 中的对应条目。
方法：每个结果先读前提与证明，再用自己的脚本独立推导、复算（纯 Python 标准库），不调用也不信任 `checks_v62.py`；只在数字对不上时才去读对应块，弄清它算的是什么。
脚本：`/private/tmp/claude-501/v62verify/math2/`（`s6_checks.py`、`s6b_checks.py`、`host.py`、`thost.py`、`commonfront.py`、`dwell.py`、`dwell_cap.py`、`sprt.py`、`misc.py`、`extra.py`）。

---

## 总判断

第 6–11 节与 S6–S11 的数学，在各自模型内基本成立。本轮修补的重点结果我都独立推导或复算过，结论和数字都对得上，包括：命题 6.4 加上 $p=1$ 的 (2)、注 S6.1 的近锁界、命题 6.7 的匹配变体、命题 7.3(2) 的条件独立前提、命题 8.6 的 $T-P+F>0$、表 9.1 R1 的 lim sup 形式、定理 10.4 在两种宿主上的裕度、命题 11.1(2) 的混合均衡界、命题 S11.4 的驻留时间。没有发现致命项。

有两处重要问题。
- **选择规则的前提写弱了。** 证明实际用的是复制子动力学（或强度有下界的选择），陈述里却只写 "payoff-monotone" 或 "cumulative"。这样一来，R1、R2 的必要性，命题 9.2(2)，引理 6.5 和命题 6.7(2) 的"趋于零"，在所写的前提下都有反例。
- **注 6.8 的"不充分"缺前提。** "协调必要而不充分"中"不充分"那一半，依赖两个没有写进陈述的前提。

其余都是次要问题：
- 一个数字标错：0.1836 不是精确的累计风险；
- 两处修正没有传到正文：第二种分享约定下的地位下界，零税时的"扩散"；
- 不等式的等号边界；
- 表格漏写前提；
- 登记表的卫生问题。

所有修法都是把条件写回陈述，不需要撤回任何论点。

---

## 发现

### 致命

无。

### 重要

**M2-01　"payoff-monotone/cumulative"选择推不出份额收敛；R1、R2、命题 9.2、引理 6.5、命题 6.7(2) 的前提都不足**

- **位置**
  - THEORY 表 9.1 R1、R2 的"模型"列（"payoff-monotone selection among carriers otherwise alike"）；
  - 命题 9.2（"Let selection among carriers be payoff-monotone"）；
  - 引理 6.5（"retention is cumulative"）；
  - 命题 6.7 第 2 层（"selected relatively, payoff-monotonically and cumulatively"）及 (2) 的"tending to zero"；
  - 上游是命题 3.4 第二句和引理 3.3(3) 的"its share tends to one"，这两处属上半部，但本节的结论都从这里继承。
- **问题**
  - 定义 3.2 的"relative + payoff-monotone"只约束份额增长率之差的**符号**，不约束大小。
  - 命题 3.4 的证明（S3）写的是"Under replicator dynamics … $\frac{d}{dt}\ln(p_k/p_l)=(e_k-e_l)(\nu-\tau_{\rm eff})$"。从 $B(t)\to\infty$ 推出"竞赛者份额趋于一、负荷趋于 $\bar e$"，靠的正是这一步。
  - "cumulative"一词在 S0 里没有定义。
- **证据（反例）**
  - 取规则 $\dot p_k/p_k-\dot p_l/p_l=\kappa(t)(\pi_k-\pi_l)$，$\kappa(t)=e^{-t}$。它满足定义 3.2 的两条：加常数不变，符号保持。
  - 令 $\tau_{\rm eff}=0$，则 $B(t)=\nu t\to\infty$，但 $\ln(p_{\rm race}/p_{\rm other})$ 收敛。
  - 在 R1 反例所用的宿主上（$\rho=0.05$，$h_V=0.08$，下限 0.3，初始竞赛份额 0.001），算到 $t=2000$：竞赛份额停在 0.0027，$\min V=0.9956$，轨迹全程可存续。
  - 所以"可存续 ⟹ $B\not\to\infty$"在所写前提下不成立（`extra.py`）。
  - 构造一个自治规则也行：$\dot u=\Delta\pi\,(x^\ast-x)$，份额饱和在 $x^\ast<1$。
  - 同理，引理 6.5 写的是"acting on a common term lowers relative performance net of every benefit"，没写"差距有正下界"；而 S6 的证明写了"by at least a positive margin"。差距如果衰减得足够快，累计劣势有界，份额就不趋于零。
  - 引理 6.5 还只说"admissible variants include"，没有像命题 6.7 那样要求该变体"in the support of selection"。
- **修法**
  1. 在 S0 定义"累积选择"：存在常数 $\kappa>0$，使得当 $\pi_k>\pi_l$ 时 $\frac{d}{dt}\ln(p_k/p_l)\ge\kappa(\pi_k-\pi_l)$。复制子动力学是 $\kappa=1$ 的情形。
  2. 在以下各处把"payoff-monotone"改成"cumulative (S0)"：表 9.1 R1、R2 的模型列，命题 9.2 的总前提，命题 3.4 的第二句，引理 3.3(3) 的"tends to one"，命题 6.7 第 2 层，引理 6.5。
  3. 引理 6.5 补两处："by a margin bounded away from zero (or with cumulative disadvantage unbounded)"，以及"present in the support of selection"。命题 6.7 的 $(A_\tau)$ 同样补上"by a positive margin"，S6 证明里已经这样写了。
  4. 定理 10.4 已明写复制子动力学，不受影响。

**M2-02　注 6.8 的"coordination necessary, not sufficient"：不充分的一半缺两个前提**

- **位置**
  - THEORY 注 6.8 的斜体陈述与标题；
  - §6.4 的"for which coordination is necessary and, for the masked divergences of Remark 6.8, not sufficient"；
  - §9"Where admission does not reach"中的"For masked classes R8a is necessary and not sufficient"。
- **问题**
  - 斜体陈述是条件式："Once $p_{\rm det}F$ falls below the tax … whatever coordination stands behind it"，字面上为真。
  - 但协调能做的事之一，正是把 $F$ 抬高。只要 $p_{\rm det}>0$，把 $F$ 提到"税额 / $p_{\rm det}$"以上，约束就重新成立。
  - 所以"不充分"这个一般结论需要两个前提：(i) $F$ 有上界，S6 写的是"bounded by exclusion, the largest sanction admission holds"；(ii) 在固定的审计接入下，$p_{\rm det}$ 随能力上升趋于零，即 C12。
  - 两条都只在 S6 出现（"If $p_{\rm det}$ falls toward zero as capability rises while $F$ is bounded by exclusion…"），核心陈述里没有。按"陈述自带条件"的规则，这一条是 E2、E3 的"来自对齐内部的最强理由"，承重，不能只放在补充材料里。
- **证据**
  - 在 S6 自己的数例里（税 0.3），$p_{\rm det}F=0.35$ 就能把未对抗变体清除。
  - 不加上界，任何 $p_{\rm det}>0$ 都存在足够大的 $F$。"whatever coordination stands behind it"只在 $F\le F_{\max}$ 时成立。
- **修法**
  - 斜体陈述加一句："If $F$ is bounded by exclusion, $F\le F_{\max}$, and $p_{\rm det}$ falls toward zero as capability rises at fixed auditor access (C12), there is a capability beyond which no admissible sanction keeps the divergence out."
  - 标题保留，§6.4 和 §9 的两处引用各加"(under the premises of Remark 6.8)"。

### 次要

**M2-03　命题 S6.2(3)："exact realized risk from $t=5$ is 0.1836"是错的；例子在 $t=0$ 的存活为零**
- **位置**：SUPPLEMENT S6，命题 S6.2 的数值 (3)；`checks_v62.log` 第 193–194 行。
- **问题**
  1. 0.1836 是 $\sum_{t\ge5}[1-(1-2^{-t})^3]$，即各期风险之和，本身就是上界。精确的累计风险是 $1-\prod_{t\ge5}(1-2^{-t})^3=0.1726$。
  2. 该例在 $t=0$ 的实现风险为 1（$\Delta\psi_0=1$），所以从 $t=0$ 起的存活恰为零。拿一个存活为零的例子说明"可和"，与引理 5.11 的要点（$h_t<1$ 时可和才保证存活有正下界）相悖。
- **证据**：`extra.py`。精确累计风险 0.17262，风险之和 0.18363。从 $t=1$ 起的存活 $\prod_{t\ge1}(1-2^{-t})^3=0.0241$。
- **修法**
  - 改为"exact 0.1726 (sum of hazards 0.1836)"。
  - 例子把下标整体移一位：$s_t=2^{t+1}$，$\Delta\psi_t=2^{-(t+1)}$。这时自身边际收益为 +0.023、+0.037、+0.102…，满额授权在每期都是均衡，$h_0<1$。正文同时写出从起点算的存活。

**M2-04　零税时"扩散"还是"中性"：正文两处与命题 6.7 的范围说明矛盾**
- **位置**
  - THEORY §6.4"The tax is not fixed"段："progress that brings the tax to zero or below spreads the safeguard without coordination"；
  - SUPPLEMENT S7 矩阵 P23："where the tax is zero or negative the safeguard spreads without coordination"。
- **问题**：命题 6.7 的 Scope 写的是"Where the tax is negative the safeguard spreads…; where it is zero the safeguard is neutral"。S6 的 CI(i) 数值也写着零税时"neither spreads nor is removed"。
- **修法**：两处都改成"below zero spreads the safeguard; at zero it is neutral"。

**M2-05　"keeps the divergence out if [sanction] ≥ gain"：等号时规避者并不消失**
- **位置**：命题 6.7(3)；表 9.1 R8a；S9 R8a 段。
- **问题**：引理 3.3(3) 的原文是"compliance survives if $\bar F_k\ge c_k$ … tends to one if strict"。等号时，规避变体保持初始的相对份额，"keeps out"言过其实。注 6.8 用的"survives"是对的。
- **修法**：改为"keeps the divergence from spreading if …, removes it if every inequality is strict, and within a type only if"。

**M2-06　§10.2 正文的地位下界没有带上分享约定（V6.1 的错误修了一半）**
- **位置**：THEORY §10.2"The positional part cannot be divided"段："however much of the divisible prize is shared, the uninvadable intensity stays at least $r\Omega_s/(nc)$ (part (2))"。
- **问题**
  - 在第二种约定（分给其余 $n-1$ 方）下，当 $\beta\varrho>(n-1)/n$ 时，$\Omega_{\rm eff}=\Omega_s-(\beta\varrho\,n/(n-1)-1)\Omega_e<\Omega_s$。
  - S10 自己写了"Under the second, $\Omega_{\rm eff}\ge\Omega_s$ while $\beta\varrho\le(n-1)/n$"，命题 10.2(2) 也已分开两种约定，但这句正文没跟着改。
- **证据**：$n=4$，$\Omega_e=\Omega_s=r=c=1$，$\beta\varrho=1$。第二种约定下不可侵入强度为 0.1667，低于 $r\Omega_s/(nc)=0.25$；第一种约定下是 0.25（`extra.py`）。
- **修法**：改为"stays at least $r\Omega_s/(nc)$ when the shared part is divided among all, and positive for every $\beta$ iff $\Omega_s>\Omega_e/(n-1)$ when it goes to the others"。

**M2-07　命题 8.5(1)："as the racing branches deteriorate, this bound rises toward one"并不单调**
- **位置**：THEORY 命题 8.5(1)；S8 中的完整陈述。
- **问题**
  - 界为 $1-\max(\Phi^S,\Phi^P)/(s_P\Phi^R+(1-s_P)\Phi^P)$。当 $\Phi^S>\Phi^P$ 时，单独降低 $\Phi^P$ 会缩小分母，界反而**下降**。
  - S8 的证明写的是极限（"as $\Phi^S,\Phi^P\to0$ … tends to one"），这是对的。
- **证据**：$\Phi^S=0.5$，$\Phi^R=0.9$，$s_P=0.5$。$\Phi^P$ 从 0.4 降到 0.3，界从 0.231 降到 0.167（`extra.py`）。
- **修法**：改为"tends to one as $\Phi^S$ and $\Phi^P$ tend to zero, and rises when they fall in proportion"。

**M2-08　表格漏写前提**
- **位置与问题**
  - 表 7.1 "Capture"行：危险侧的速率律 $\alpha_{\rm cor}<\alpha_{\rm ctl}/(1+\eta)$ 要求命题 4.5(2) 的两个前提，即无单位成本下限 $f=0$、存在正的培植通道，表里没写。$f>0$ 时，要求在 $\max\{A/c_{\rm ev},d_f\}$ 处封顶，不是速率。
  - 表 7.1 "Enforcement"行：$p_d>\bar p_{d,i}$ 只对 $D_i(a)>v_i$ 的偏离有意义（命题 5.4(2)），表 9.1 R4 写了，表 7.1 没写。
  - 表 7.1 "Compounding"行，"Side of (14) moved"一列写"Temptation"。但 $p_d$ 同时出现在 (14) 两侧：$\delta p_d(D-C)$ 和 $\delta(1-p_d)(C-v)$。
  - 表 9.1 R3a："sufficient at any speed of adaptation"漏了命题 4.5(2) 的限定，即"for every adjustment of capacity that starts at or below its selected level and does not raise it while above"。S9 里写了。
  - 表 9.1 R2 "not needed"："$h_V\bar p_{\rm unc}\bar e<\rho(1-V_{\min})$"只计入了未覆盖者的负荷。已覆盖者的剩余负荷如果不趋于零，也必须计入。
- **修法**
  - Capture 行加"(no per-unit floor, a positive cultivation channel)"；
  - Enforcement 行加"with $D_i(a)>v_i$"；
  - Compounding 行改为"Both, through $p_d$: a growing gap shortens $T_{\rm dec}$, so $p_d$ rises"；
  - R3a 补上限定；
  - R2 的条件改为 $h_V[\bar p_{\rm unc}\bar e+(1-\bar p_{\rm unc})\bar e_{\rm cov}]<\rho(1-V_{\min})$。

**M2-09　近锁界："'Near certainty' is exact"的含义要说清；$s\ge206.4$ 一例漏了 $p=1$**
- **位置**：THEORY §6.3 命题 6.4 之后一段；注 S6.1；S6 命题 6.4 的数值。
- **问题**
  1. 注 S6.1 的界对 $(n,p,\text{他人策略})$ 一致成立，只在 $n\to\infty$、$k=0$、$p=1$ 时取到。固定 $n$ 时，更不确定的锁也够用：$n=2$、$s=2$、$p=1$ 时，最坏比值因子是 2，一致界是 3。等号情形也成立，因为每个有限 $n$ 下比值都严格小于一致界。
  2. "With $n=2$, $q_L=0.99$ … all delegating is an equilibrium only for $s\ge206.4$"隐含 $p=1$。取 $p=0.5$ 时，$s\to\infty$ 的比值趋于 $1.5A<1$，任何速度下都不是全授权均衡。
- **证据**：`s6_checks.py`。20,000 次随机抽样中注 S6.1 零违反；比值随 $n$ 依次为 1.0076、1.6793、1.9756、2.0147，逼近一致界 2.0152。`extra.py` 的最坏因子：$n=2,3,10$ 时分别为 2.0、2.33、2.8。
- **修法**：改为"exact as a bound uniform in $n$, $p$ and the others' profile, approached as $n\to\infty$; for a given $n$ a less certain lock suffices"。206.4 一例补"$p=1$"。

**M2-10　CI(j) 的 $1.4\times10^{-87}$ 是 $t=2000$，不是 $t=200$**
- **位置**：S6 命题 6.7 数值"The matched variant"一项。
- **问题**：原文"falls to $2\times10^{-9}$ by $t=200$ [CI(i)], and to $1.4\times10^{-87}$ in a second implementation [CI(j)]"，读者会以为两种实现在同一时刻差了 78 个数量级。读了 `ext_CI` 的 (j)：它跑到 $T=2000$，$e^{-0.1\cdot2000}=1.4\times10^{-87}$；CI(i) 是 $e^{-0.1\cdot200}=2.06\times10^{-9}$。两者一致。
- **修法**：写成"and to $1.4\times10^{-87}$ by $t=2000$ in a second implementation"。

**M2-11　命题 10.1 的"pooled effort"其实是每个合作者的努力 $e_c$；表 11.3 的"Not shown"列混入了已证的结论**
- **位置**：命题 10.1 陈述与 S10 中的完整陈述（5）；表 11.3 "Existence"行。
- **问题**
  - 按文中描述重建了模型：合作者把 $n_ce_c$ 合并，强度为 $(n_ce_c)^r$，$\Omega_c$ 平分，失败方承担 $L_b$，竞赛者取对称最优反应不动点。$T=R$ 的门槛分别在 $e_c=0.0054$、0.0349、0.1406、0.4898 处，与文中"0.0054, 0.035, 0.14, 0.49"一致，说明这是 $e_c$，不是合并后的总努力（Ω=1 时为 $4e_c=0.14$）。
  - 表 11.3 "Not shown"列写着"the pooled effort it needs rises steeply with the value of winning"，这是已证的限制，不属于未证事项。
- **证据**：`commonfront.py` 完整复现了：$R=0.140$，$T=0.0017$；分立前沿下全竞赛是唯一纯均衡；信任门槛 0.6106；$n=2$ 时 $r\le1.22$ 全合作仍是均衡。
- **修法**：改为"the effort each cooperator contributes to the pool"。表 11.3 中把该句移到"Support"列作为限制，或另起"Limit"。

**M2-12　命题 7.3(2) 的 $X$ 与推论 7.4(2) 的"objectives give least"之间缺一步认同**
- **位置**：§7 主张框；推论 7.4(2)；§8.3(d)。
- **问题**：命题 7.3 的 $X$ 是"having won, it extends its dominance rather than limiting it"；推论 7.4(2) 和主张框写的是"shifts winners toward those whose objectives give least"（指命题 5.8 的给予份额）。两者相关，但等同需要一句前提。
- **修法**：要么把 $X$ 定义为"having won, gives the governed least (Proposition 5.8)"，要么在推论 7.4(2) 中写"…toward those that extend dominance, and so, where extending dominance goes with giving least, …"。

**M2-13　有些例子按正文无法复现：缺参数**
- **位置与问题**
  - S8 引理 8.2 的例子（0.976、0.864、0.211）。正文没写安排本身的风险率（`check_FD` 中是 0.0015），也没写"restarts continuation ten periods later"的含义（实际是 $h_c(t-10)$）。按这组参数可以复现，也确实满足引理的两个条件。
  - 定理 10.4 的裕度数值。没写选择速度 $s=1$；阈值宿主的 $\rho_A$ 也没给。我试出 $\rho_A=\rho A/(1-A)$，也就是使宿主处处更苛刻的最大值，用它能复现 $V_u=0.254,\dots,0.481$ 和裕度 0.260–0.505。
- **证据**：`host.py`、`thost.py`。宽容宿主上 $\Delta_{\min}$ 为 0.108、0.165、0.355，以及 0.125、0.192、0.414，裕度 0.08 时的谷底 0.1397、0.1136，都复现了。阈值宿主上我得到 0.261、0.306、0.359、0.423、0.506。
- **修法**：在 S8、S10 中写明这些参数。

**M2-14　注 S11.3 的 Wald 界还有前提没写**
- **位置**：注 S11.3(2)；定义 11.2。
- **问题**
  - Wald 的 $a/(1-b)$、$b/(1-a)$ 界针对两个简单假设（两个登记水平），并要求似然比按**已知**的噪声分布计算。"at every level of noise"成立的前提是检验知道噪声水平；如果噪声要估计，界不再成立。
  - 真值落在两个登记水平之间时（不敏感区），错误率不受控。
  - 慢变量的读数往往自相关，而"independent readings"是前提。
- **证据**：`sprt.py` 复现了全部数值：固定 16 次读数在单位噪声下通过率 0.953、双倍噪声下 0.372，七维分别为 0.713 和 0.001；SPRT 平均读数我模拟得 10.5、38.9、150.8，与文中的 10.5、38.7、148.6 在抽样误差内一致，两类错误率都低于各自的界。
- **修法**：写明"with a registered noise model; error rates bounded at the two registered levels, with an indifference zone between them; readings independent or the test adjusted for dependence"。

**M2-15　无下限时的驻留数值，依赖替代者以 $10^{-31}$ 的份额存活**
- **位置**：命题 S11.4(2)、(4)；§11.4 的"10.45 to 3.81"。
- **问题**
  - $G=10$、规则制定慢十倍时，从 0.99 开始隔离，期间 logit 峰值约为 $4.6+10(9-\ln10)=71.6$，即替代者份额约 $8\times10^{-32}$。在任何有限总体里它已经灭绝，驻留时间应为无穷。
  - 结论（无下限则无界）不受影响，反而更强，但 10.45、16.18 这类数字容易被当成现实量级。
- **证据**：`dwell.py` 复现了 1.89、5.32、10.45 和 5.86、10.34、16.18，返回时刻 1.594、4.965、10.0，深度序列 3.45 至 28.90 和 1.59 至 4.34，$x_\sigma$（$G=2$、慢十倍时为 0.984，所以 $x_0=0.9$ 不在 (1) 的范围内，与 1.585 小于 1.594 一致）。`dwell_cap.py` 用 logit 上的硬上限复现了有下限时的 3.52、3.81、4.60、6.04、2.99、9.48、11.79。
- **修法**：在 S11.4 中写出隔离期间达到的最大深度，并说明"without a floor, an alternative at such shares would be extinct in a finite population; the floored values are the meaningful magnitudes"。另外说明"可招募谱系"在模型里就是 logit 上的反射上限，即替代者从 $\phi_{\rm alt}$ 起以选择速率增长。

**M2-16　标签与登记表的卫生**
- 表 11.3 把注 S11.5 标为 [thm∣prem]，S11 和 CLAIMS `ratchet` 都标 [thm]。应统一；建议用 [thm]，因为它是场模型内的结论。
- CLAIMS `require` 仍写"R9 new, awaiting confirmation"，但 Ren 已于 10 月 4 日确认保留 R9。
- CLAIMS `topology` 写"Row sums a sufficient certificate, never necessary"，应为"not necessary"。
- 命题 6.1(3) 没覆盖等号情形 $\beta_c=1+\max(\beta_b,\beta_h)$，数值里却给了 0.9375 和 2.1。可在陈述里补一句"at equality the limit keeps a cost term"。

---

## 好的部分，应当保留

- **命题 6.4 与注 S6.1。** $\Phi_D/\Phi_N$ 的闭式、$p=1$ 时"至少一个角点是均衡"的恒等式 $A(n-1)s^2/[n(n+s)]\ge0$、$p<1$ 时的内点唯一均衡（0.1 的例子：1.00259、1.00097、0.99928），以及近锁界 $(1-q_L)(1+s)(1-\psi_1)<1-\psi_0$，我都独立证明或复算过，全部成立。
- **命题 11.1(2) 的改正正确。** 每个均衡中 $\rho_{\mathsf E}\le c_{\mathsf R}/\Pi_{\mathsf R}$；在 $c_{\mathsf S}\le\Pi_{\mathsf S}c_{\mathsf R}/\Pi_{\mathsf R}$ 时由半分离均衡取到，$\sigma_{\mathsf R}=(1-\mu)(1-\varpi^\ast)/(\mu\varpi^\ast)$。V6.1 的"only if $1-\mu\ge\varpi^\ast$"只在纯策略下成立。直观准则的精炼论证也对。
- **命题 7.3(2) 加上"winning depends on $X$ only through $E$"是必要的。** 我构造了反例：$P(X\mid E)=0.5>0.4$，$P(W\mid E)=0.5>0.1$，但 $P(X\mid W)=0.067<P(X)=0.45$。
- **命题 8.6(2) 补上 $T-P+F>0$，以及注 5.5 的恒等式。** $(T-R)/(T-P+F)=1-\bar p_{d,i}$，代数准确。
- **表 9.1 R1 的 lim sup 形式方向正确，"$B\not\to\infty$"更强。** 必要性的证明和"平均形式不充分"的反例（$t\approx88.9$ 跨越下限）都已复现。有限时域的例子（$V(50)=0.4353$，$t=\ln3/\rho=109.9$）也对。
- **定理 10.4 的裕度论证干净。** 用倾斜分布的均值对倾斜量求导得负方差，再用比较定理，得出 $V$ 关于 $\Delta$ 逐点单调，所以可存续的裕度构成区间 $[\Delta_{\min},\infty)$。两种宿主上的数字都复现了，撤回循环条款和"kernel"说法的处理也对。
- **命题 S11.4。** 下集（down-set）论证、深度单调、下界 $(u_0-\operatorname{logit}x_\sigma)/(\zeta c)$、以及招募与非招募的对比，都成立。
- **命题 S6.4 用可和的例子替换了 V6.1 的不可和例子。** 数字 0.5101、0.6888、0.473、0.630、$7.1\times10^{-10}$ 都对。
- **命题 6.9 的预算比较可以写成一般结论。** 在相同预算下，逐层冗余总不差于整链冗余：$(1-(1-p)^m)^k\ge1-(1-p^k)^m$，这是可靠性理论里部件级冗余优于系统级冗余的经典结论。我做了 200,000 次随机抽样，没有反例。建议把例子提升为这一句，并引用 Barlow 和 Proschan。
- **命题 10.2 两种约定的证明都正确。** 有效自我模型在 $(-1,n-1)$ 上随 $\beta$ 严格增，导数分子为 $(1+\theta_0)(n-1-\theta_0)/n>0$；SH 的全部数字也复现了。

---

## 查了什么，没查什么

**独立推导或复算过的**
- **S6**：命题 6.1 的 (1)–(3)，含全部指数组合和双刃数字；命题 6.2 的 $s^\ast=1.1628$ 和 0.5196，以及与直接收益的对照；引理 6.3；命题 6.4 的 (1)–(4) 与随机检验；注 S6.1；命题 S6.2 的 (1)–(4)，含两根 0.153 和 0.937、角点、$t=0..7$ 的网格最优反应；注 S6.3；命题 S6.4；注 S6.5（logistic 映射平均 7.38 步和 37.33 步）；BT 的 0.7110 和 0.024；命题 6.7 与注 6.8 的逻辑和 CI 的多类型判断；命题 6.9 全部数字与对抗盲区。
- **第 7 节**：表 7.1 九行逐一对照所引结果；命题 7.2 的各分支，其中分支 II 的议价逆向归纳我按 (A8) 重建，结论"$N\le3$ 攻击、$N\ge4$ 不攻"成立；命题 7.3；推论 7.4。
- **第 8 节**：定义 8.1；引理 8.2 的耦合；命题 8.5；命题 8.6 的 (1)、(2)、(4)，含 $-3.73$ 的例子；定理 8.7；命题 S8.1 的四组数字；注 S8.2；命题 S8.5(2) 的反例；贴现比较。
- **第 9 节**：表 9.1 R1–R9 的逻辑与数值（R4 的 0.864；R1 的两个反例）；命题 9.2；注 S9.1 的 0.375 和 0.75。
- **第 10 节**：命题 10.1 完整重建；命题 S10.1；命题 10.2 与 SH；定理 10.4 在两种宿主上；命题 S10.3 的可行性和、0.872 与 BIC 论证。
- **第 11 节**：推论 S11.1；命题 11.1 与精炼；命题 S11.2 的例子（0.797，$2\times10^{-44}$）；注 S11.3 全部数字；命题 S11.4 全部数字与证明；表 11.3 的标签。

**没有查的**
- 上半部的结果本身：命题 3.4、引理 3.3、命题 4.5、4.10、5.4 等。我只核对了本节如何引用它们；M2-01 的问题源头在 3.4 和 3.3(3)，应由上半部评审确认。
- S7 的"Near parity"MPE 数字（MP，原文已标"held for outside review"）。
- S8 的 SM(4)、SM(14) 两状态马尔可夫例子和精确动态规划。
- S9 R3a 的 FF 数字（$t=38.4$、588）。
- DL 和 TR 的随机抽样计数（1,586、60、300、200、135）只核了逻辑一致，没有按原分布复抽。
- 再播种变体（3.28、4.12）。
- Jones 2024 的数字（属 [obs]）。
- 第 12 节、DISCUSSION 的 X8、X10、X11，以及 S13 接口。
- 没有运行 `checks_v62.py`，也没有核对其 188 条断言。

---

## 同族偏差

我与起草者是同一模型家族，这在三处可能有影响。

1. **重建模型**。命题 10.1、驻留的"可招募谱系"、阈值宿主的 $\rho_A$、引理 8.2 的例子，正文都没有给全模型，我是按自己读出的意思重建的。复现成功，说明数字与**这种**读法一致，但不能排除我和起草者共享同一种误读。家族外评审应按正文字面另行重建一次，M2-13 列出的缺参数尤其要查。
2. **"在模型内成立"的认定**。我倾向于接受条件式陈述"字面为真"，这可能低估了 M2-02 这类"标题比陈述说得多"的问题。家族外评审对这一类可能更严。
3. **漏查边界**。M2-01 的反例来自"只约束符号的单调规则"。同族模型可能对"payoff-monotone ≈ 复制子"这种默认等同有共同盲点。我是在读 S3 证明时才注意到的，其他章节里也可能还有同类的默认等同，我没有逐一排查。
