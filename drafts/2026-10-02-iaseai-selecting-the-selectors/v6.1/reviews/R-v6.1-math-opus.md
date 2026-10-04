# V6.1 数学评审（Opus）

*2026-10-04。对象：`v6.1/THEORY.md`（sha256 `242a61240d810e51…`）与 `SUPPLEMENT.md`，对照 `../v6/v61-planning/Q2-math-repairs.md`、`../v6/reviews/R-v6.0-math.md` 与 `REVIEW-v6-codex.md`。独立脚本放在 scratchpad `review61/math-opus/`，纯 Python 标准库，日志与脚本同名（`.log`）。没有读其他 v6.1 评审，没有改动项目文件。审阅者与起草者同属一个模型家族，见第四节。*

## 一、总判断

**代数基本都对。** 以下各项我都独立重推，并用与作者不同的构造做了数值复核，没有发现代数错误：
- Prop 2.2 的秩一判据与 Sherman–Morrison 定价；
- Prop 2.3；
- Prop 5.4(1)–(5)；
- Cor 5.5 中 $n=2$ 的论证；
- Prop 5.15；
- §4 的全部指数；
- Lemma 8.2 的耦合证明。

**问题集中在三个接口上。**
1. **环路增益与地位价格。** 它们是在"他人策略固定"的非策略模型里证明的。让对手按状态反应（马尔可夫完美均衡，MPE）之后：
   - 平等处的地位价格放大到公式的 1.04–7.9 倍；
   - 落后者的地位价格降到接近零；
   - 结构 $\Gamma=0.6$ 时平等地位就已失稳。

   因此核心散文"Γ 决定领先是否复利，并给每个行动者的地位定价"，在策略情形下不成立。
2. **速率律的"必要"一半依赖准静态容量。** 在有限速度的选择动态下，这一半不成立；"充分"一半仍成立。
3. **"固定部分 $f$"实际是边际成本下限。** 换成真正的固定成本，阈值指数和"需求封顶"都会改变。

**其他问题。**
- Lemma 3.10 对非线性的 payoff-monotone 规则陈述为假。
- Thm 10.5 的可存续条款是循环的。
- R4 的例外栏写错。
- 两个标为 independent 的检查块，实际是恒等式。

**没有致命错误。** 这些问题都可以在不改变论证方向的前提下修复。在我算过的例子里，第 1 条反而加强了"复利制造相对目标"的方向。

## 二、问题

### 致命

**无。**

需要提醒一点：如果 §1.2 第 1 条、§2 主张框和中文导读"核心"段继续说 Γ "decides whether leads compound … for every actor"，而不改成"结构增益"或"均衡弹性"（见 M1），这句话会成为外部评审最先举出的反例。

### 重要

**M1　地位价格与环路增益在完整随机博弈中不成立（攻击 1）**

- **位置：**
  - Prop 2.2(3)；
  - Prop 3.9 及其首句 "every forward-looking actor acts as if it valued only its standing"；
  - §1.2 第 1 条、§2 主张框、导读"核心"段；
  - §5.5 剪刀差的 [num]；
  - §7.2 对 Branch III 的定义（"loop gain below one"）；
  - Test Γ。
- **问题：**
  - "others' strategies fixed"只写在 Scope 里，不在陈述里。
  - 这不是一个可以忽略的一阶近似。在均衡中，对手的强度对状态的导数 $de_2/ds$ 在平等处一阶非零。所以"固定他人"与均衡是两个不同的一阶对象。
- **证据**（`s2_mpe.py`、`s2b_mpe_extra.py`、`s2c_profile.py`、`s2d_eqgain.py`、`s2e_check.py`）：
  - *模型。* 两人；每期以 Tullock 抽签争奖金，强度为 $K^r e$；赢得物转为能力，总能力处于稳态；$\theta_0=0$，$\delta=0.9$。
  - *求解。* MPE 用价值迭代求到 $10^{-12}$，最优反应做了全局核对；网格取 800 与 1600 点，结果相同。
  - *平等处的地位价格。* $\lambda_{\rm MPE}/\lambda_{\rm 公式}$：
    - $\delta=0.9$ 时为 1.05–2.67；
    - 共享损失 $\ell=0.5$ 时为 4.75；
    - $\delta=0.97$、$\Gamma=0.6$ 时为 7.87，即 $\theta_\Gamma=-0.35$，而 $\theta_{\rm MPE}=-0.81$。

    跳跃很小时（$d=0.05$），"固定他人"的精确值与公式只相差 0–3%，MPE 仍为公式的 1.05–2.67 倍。所以差异来自策略反应，不来自非线性。
  - *远离平等时。* $\Gamma=0.9$、$s=0.25$ 的落后者，$\lambda_{\rm MPE}=0.026$（$\theta\approx-0.01$），而"固定他人"给出 0.98。落后者放弃竞争，按自身收益行动。所以"每个向前看的行动者"不成立。
  - *平等地位的稳定性。*
    - 均衡中平等处的 $dp/ds$ 为 3.3–7.7，结构决定性 $r$ 只有 1–1.5。
    - 均衡环路增益 $\Gamma_{\rm eq}=\Gamma\cdot(dp/ds)/r=1.9$–$3.5$，而结构 $\Gamma=0.6$–$0.9$。
    - 从 $s=0.52$ 出发，期望份额 40 期后到 0.633。
    - 100 期后 $|s-\tfrac12|$ 的均值为 0.136，被动动态只有 0.081。

    因此 Prop 2.2(1) 的门槛 $\Gamma=1$，不适用于强度由策略决定的竞赛。而 Prop 3.9 用的正是这种组合。
  - *文献。* 这与动态竞赛中的气馁效应、优势递增一致（Harris–Vickers 1987；Budd–Harris–Vickers 1993；Athey–Schmutzler 2001；Konrad 2009†，凭记忆，须核对）。同一文献也有追赶结构，方向可以反转，所以我没有证明放大普遍成立。
- **修法：**
  1. 把"others' strategies and the prize fixed"写进 Prop 2.2(3) 与 Prop 3.9 的陈述，Prop 3.9 改标 [thm∣prem]。首句改为："Near equal standing, compounding raises the weight a forward-looking actor puts on standing; $\theta_\Gamma$ is that weight when rivals do not respond."
  2. 把 $r_j$ 定义为均衡中赢得份额对存量的弹性，含强度反应。这样 Prop 2.2 的形式不变。补一句：在气馁型竞赛中它可达结构决定性的数倍，所以结构 $\Gamma<1$ 是平等地位稳定的必要条件，不是充分条件（就所算类别而言）。
  3. §1.2、§2 与导读中的 "decides whether leads compound" 改为 "sets the structural gain of the loop"。Branch III 改用 $\Gamma_{\rm eq}$ 定义，或标 [conj]。
  4. §5.5 的 [num]（0.92→0.39）注明是"对手不反应"的约化形式。
  5. 在 `checks_v61.py` 中新增一个 MPE 块，可以 `s2_mpe.py` 为底稿。

**M2　速率律的"必要"部分依赖准静态容量（攻击 3）**

- **位置：**
  - Assumption 4.2 末句；
  - Prop 4.5(2) 的 "fails beyond a finite time"；
  - §4.3 的 "needs to grow only half as fast"；
  - §1.2 第 3 条与导读第 3 条；
  - Prop 9.1 的 R3a（列为 necessary）；
  - TESTS Study 2。
- **问题：** §4 自己的机制是"influence over correctors is selected"，Prop 4.3 给的是选择梯度。但速率律要求容量每时每刻都处在最优水平 $q^\ast(t)\propto e^{(\alpha_{\rm ctl}-\alpha_{\rm cor})t/\eta}$。
- **证据**（`s4_cost.py` (c)；$p=0.6$，$\eta=1$，$\alpha_{\rm ctl}=0.2$，阈值为 0.1）：
  - $\alpha_{\rm cor}=0.09$：
    - 准静态下证书在 $t=146$ 失效，此后不再恢复（$s_E\to21.8$）；
    - 加性梯度（$V=1$、100）、对数梯度（$V=1$）、离散类型复制者（$V=1$、20，突变率 $10^{-3}$）下，在 $t=300$ 内都不失效，且 $s_E\to0$。
  - $\alpha_{\rm cor}=0.05$：
    - 准静态在 $t=28.8$ 失效；
    - 复制者在 $t=51$–86 失效；
    - 加性 $V=100$ 在 $t=36$ 短暂失效，随后恢复。
  - *解析。* 在加性动态 $\dot q=V\,\partial\Delta\pi/\partial q$ 下，$q(t)\le q_0+V\chi p^2\hat Y/(d_0\alpha_{\rm cor})$。所以任何 $\alpha_{\rm cor}>0$ 最终都使证书成立。
  - *反方向稳健。* $q$ 滞后于上升的 $q^\ast$ 只会降低培育量，所以在任何一阶滞后动态下，$\alpha_{\rm cor}\ge\alpha_{\rm ctl}/(1+\eta)$ 仍是充分的。
  - *对其他节的影响。*
    - Thm 4.12 的结论不依赖准静态，见次要 6。
    - §6 的 $\mathcal M$ 按指数动态建模，不涉及准静态。
    - §11.4 的驻留时间默认改革期间 $G$ 不变，这是第三种隐含假设。若容量是沉没存量，驻留时间更长。
- **修法：**
  1. Prop 4.5(2) 拆成两句："sufficient whatever the speed of adaptation; necessary when capacity tracks its selected level (optimizing carriers, or adaptation faster than $(\alpha_{\rm ctl}-\alpha_{\rm cor})/\eta$)"。
  2. R3a 改标"必要（准静态下）"，例外栏加一条"capacity adapts more slowly than its target"。
  3. TESTS Study 2 预期的失效征象方向反了。慢适应下，证书在低于速率律的增速下仍成立；需要检验的是适应速度本身。
  4. §11.4 写明驻留时间对容量动态的假设。

**M3　"固定部分 $f$"实为边际成本下限，读作真正的固定成本时两项结论不成立（攻击 4）**

- **位置：**
  - Assumption 4.2（$f p^{\xi_f}q$ 对 $q$ 线性）；
  - S0 表中的 "variable and fixed cost"；
  - Prop 4.3 的阈值；
  - Prop 4.5(3) 的 "the requirement levels off"；
  - §4.3 与 R3a 把 "a fixed cost of control AI does not lower" 作为持久补救。
- **证据**（`s4_cost.py` (b)）：
  - *阈值指数。* 改为一次性固定成本 $Fp^{\xi_f}$ 后，指数是 $\eta/(2\eta+2-\xi_v-\eta\xi_f)$。$\eta=1$、$\xi=0$ 时为 1/4，不是 1/2。
  - *需求不再封顶。* $\gamma$ 从 $10^{-2}$ 降到 $10^{-8}$ 时，$d^\ast$ 依次为 4.6、46、465、4648，与 $f=0$ 的渐近行为相同。线性 $f=0.3$ 时 $d^\ast\to1.20$。
- **修法：**
  - 全文改称 "a per-unit (marginal) cost of capacity that AI does not lower"，例如法定的逐项程序成本。
  - 明说真正的固定成本只推迟培育，不封顶。

**M4　Lemma 3.10 对 "every payoff-monotone rule" 陈述为假**

- **位置：** THEORY §3.6 Lemma 3.10；S3 的证明只用了线性适应度 $w=w_0+b\bar z-cz$。
- **证据**（`s5_misc.py`）：
  - 两组，$z=\{0,1\}$ 与 $\{0.6,0.6\}$，收益为全体共有。
  - 适应度 $w=\varphi(\pi)$，$\varphi=\log(1.05+\pi)$ 递增且凹。
  - 组间项 $\operatorname{Cov}(w_g,z_g)=+0.0005>0$，总项为 $-0.122$。
  - 原因是 Jensen 不等式：组内方差大的组，均值适应度被压低。
- **修法：**
  - 改为 "The total selection term $\operatorname{Cov}(w,z)$ is non-positive under every payoff-monotone rule; each of the between- and within-group terms is non-positive when fitness is affine in payoff."
  - 结论（性状只能经传递项、或经改变相对收益的规则上升）不变。
  - PR 块只用线性适应度，测不到这一点，应补一个非线性例子。

**M5　Thm 10.5(1)：可存续条款循环，且"更苛刻的宿主才需要裕度"不成立**

- **位置：** THEORY Thm 10.5(1)；S10。
- **问题：**
  - "the trajectory is viable if, in addition, the host stays above its floor while the load falls" 以结论为前提。
  - 证明实际只给出 $\liminf V\ge1-h_Ve_{\min}/\rho>V_{\min}$。这一步还需要 $h_Ve_{\min}<\rho(1-V_{\min})$，现在只由"low enough load"隐含。
- **证据**（`s8_logistic_margin.py`）：
  - 宽容的 logistic 宿主，竞赛策略起始占 99%，地板分别为 0.2、0.3、0.5 时，可存续需要 $\Delta\ge0.108$、0.165、0.355。
  - 文中的 $\Delta=0.08$ 会让宿主下探到 0.140。
  - Allee 宿主的 $\Delta_{\min}$（0.260–0.505），我用不同的积分器和不同的判据独立复现，数字正确。
- **修法：**
  - 两种宿主都写成裕度条件：$\Delta\ge\Delta_{\min}$（宿主、$V_{\min}$、初始构成、选择速度）。区别在于：logistic 宿主缺少裕度时，越界可以恢复；阈值宿主缺少裕度时，永久崩溃。
  - "first computable instance of the correctable kernel" 改为"一个固定策略下可存续参数边界的实例"。它没有对策略取并、对扰动取交，不是判别核。

**M6　两个 "independent" 检查块实为恒等式（攻击 6）**

- **EC 块**（`checks_v61.py` 第 292–347 行；Prop 5.4 的 Scope；S15）：
  - $V_{\rm coop}\ge V_{\rm dev}$ 与 (14) 是同一个不等式乘以 $1-\delta$ 后移项。精确有理数下，两万次 0 例不符是必然的（`s3_enforce.py` (1)）。
  - 唯一被"计算"的 $V_P$，就是 (5) 的闭式。
  - S1b 对旧界的比较也是纯代数：两界只相差 $\delta p_d(D-C)$。
  - 它没有检验"当且仅当"所依赖的博弈性质：惩罚者的激励、多期偏离、$p_d$ 与 $q$ 的一致性。
  - S1c 的蒙特卡洛给出 22.414，精确值为 22.000，$z\approx+2.9$，没有做显著性判断。换种子后 $|z|<1.1$（`s6_ec_mc.py`），所以只是噪声。
- **LG(C)/(C′) 块：**
  - $\lambda$ 取自两期模型自己的二期导数 $\delta\Omega_2r_2\kappa/(n\bar K)$，不是 $\Gamma_\delta/(1-\Gamma_\delta)$。
  - 对称均衡的一阶条件只含对称点的一阶导数，所以"六位有效数字一致"按构造成立。
  - 它检验的是 Prop 3.5(3) 的 $\lambda\leftrightarrow\theta$ 映射，不是 Prop 3.9 的动态内容。
- **其他块：**
  - CS(c) 用的是准静态 $q^\ast$，测不到 M2；
  - PR 用线性适应度，测不到 M4；
  - CR 以容差接受弱均衡，不报告严格性。
- **修法：**
  1. EC 与 LG(C) 改标 identity。
  2. THEORY 中 "direct evaluation … agrees … in all of 200,000" 和 "computed equilibrium equals $e(\theta_\Gamma)$ to six digits" 改述为代数核对。
  3. 新增两个真正独立的块：MPE 地位价格（对应 M1）和非准静态容量（对应 M2）。
  4. EC 补一个显式行动的随机博弈版本：逐状态检查一次偏离，包括惩罚阶段，并让突破技术同时决定 $p_d$ 与 $q$。

### 次要

1. **Prop 9.1 的 R4 例外 "$D<C$" 写错。**
   - $D<C$ 时 (14) 仍是精确条件，$p_d\le\bar p_d$ 只是可能自动满足。
   - 反例：$C=1$，$D=0.9$，$v=0$，$g=2$，$\delta=0.9$，得 $\bar p_d=0.864$；$p_d=0.9$ 时克制不可执行（`s3_enforce.py` (4)）。
   - 应改为"$(1-\delta)g\le\delta(C-D)$，即 $\bar p_d\ge1$"，S9 同改。
   - 同表 R1 的依据写成 "Theorem Theorem 10.5(3)"，§8.3(b) 写成 "Proposition Proposition 9.2"，都是重复词。
2. **Prop 4.5(3) 在 $[H_f]$ 下漏了初始条件，另有一处符号反了。**
   - "required rate is $\min\{\alpha_f,\alpha_{\rm ctl}/(1+\eta)\}$" 在 $\alpha_{\rm cor}=\alpha_f$ 且初始已有培育时不成立：$f_0=0.1$ 时证书在 $t=37$ 失效且不恢复（`s7_Hf.py`）。
   - 应写成：$\alpha_{\rm cor}>\alpha_f$；或 $\alpha_{\rm cor}\ge\alpha_f$ 且初始无培育；或 $\alpha_{\rm cor}\ge\alpha_{\rm ctl}/(1+\eta)$ 且 $d_0>d^\ast$。
   - S4 的 "under $[H_f]$ that level falls at $\alpha_f$" 应为 rises，因为该水平与 $1/f$ 成正比。
3. **Prop 5.4(5)。**
   - 闭式假定每期至多一方突破（$2q\le1$），须写明。
   - 正文与 EC 的例子（$D=4$，$U=0$，$q=0.1$，$v=1.286>C=1$）落在 $v>C$ 区域：双方都宁要"带突破的竞赛"，不要合作。这说明的是合作本身不被偏好，不是惩罚失效。
   - 建议改用 $P<v<C$ 的例子：$C=1$，$P=0$，$D=4$，$U=0$，$g=2$，$\delta=0.9$，$q=0.045$，此时 $v=0.895<C$。$q=0$ 时克制可执行，$q=0.045$ 时不可执行（`s3_enforce.py` (2)）。
   - 结论本身不在刀刃上：$g=5$ 时，$q\in(0.016,0.056)$ 整个开区间都成立。
4. **Cor 5.5 的三人反例建立在弱均衡上（攻击 2）。**
   - 惩罚组合中，偏离者和一名惩罚者在 X 与 Y 之间恰好无差异：三人的最优单边偏离增益分别为 0、0、−0.2。
   - 但结论稳健。在保持匿名对称的随机扰动下，存在严格的角色分化惩罚的博弈数：$\varepsilon\le0.05$ 时 400/400，$\varepsilon=0.1$ 时 372/400，$\delta^\ast$ 的中位数为 0.71（`s3_enforce.py` (5)）。
   - 由哪位惩罚者取 Y 是均衡选择，但两种分配都可行。
   - 建议在 Scope 写 "weak in the printed example; strict under small symmetric perturbations"，CR 块同时报告严格性。
5. **Lemma 3.3(3)。** 双稳需要 $s(0)>c>s(1)$。"sanction weakens as evaders spread"本身推不出双稳。
6. **Thm 4.12。** 证明只用到 (reach)、(a)、(d)、(e)，而 (e) 直接给出 $m>m_{\rm fl}$；(b)、(c) 没有被用到。应写明 (b)(c) 只让 (e) 显得可信，并不蕴含 (e)。这也意味着 M2 不影响 4.12 的结论。
7. **Thm 5.12。** 证明没有用到 (variety grows)。或者从前提中删去，或者说明它只是 (coverage lags) 的动机。
8. **标签。**
   - Thm 7.1 中 Branch I′ 的 "can stabilize as nuclear deterrence did" 不是定理内容。
   - Cor 7.3 的 "cannot justify" 是规范判断：形式部分标 [thm∣prem]，结论标 [val]。
   - Thm 8.11 末句（算力核算要求联盟优势的增速不低于扩散的侵蚀）没有模型也没有证明，应标 [conj] 或 [prem]。S8 证明所引的 (1)–(4) 在正文陈述中不存在。
9. **§5.5 剪刀差。**
   - "none exists above $p_d=0.99$" 应为约 0.95（$\theta_0=0$）与约 0.98（$\theta_0=0.4$）。
   - "larger stakes lower $\bar p_d$" 需要 $D$ 与 $g$ 增长得比 $C-v$ 快。$\bar p_d$ 对 $(g,C,D,v)$ 零次齐次，S7 的表里自己也写了 "neutral if all terms scale alike"。
   - NB 的约化形式在惩罚阶段取 $q=0$，而 $p_d$ 取到 0.9，与 Prop 5.4(5) 不一致。
10. **Prop 10.3(2)。**
    - $\Omega_{\rm eff}=(1-\beta\varrho)\Omega_e+\Omega_s$ 要求分享额由全部 $n$ 人（含胜者）均分。
    - 若分给其余 $n-1$ 人，有效奖金为 $(1-\beta\varrho\,n/(n-1))\Omega_e+\Omega_s$。
    - 应与 Prop 5.7 区分 $n$ 与 $n-1$ 的方式保持一致。
11. **Prop 2.3(2)。** "no higher than equal-standing capacity" 应为 "below"。
    - $\bar K=K^\ast$ 时 $\phi(K^\ast)=0$，且 $\phi'(K^\ast)=d_K[\Gamma(n-1)/n-1]$。
    - 当 $\Gamma>n/(n-1)$ 时，落后者会离开，局部稳定不成立。
    - S2 证明中 "$\phi(\bar K)\ge0$ gives local stability" 需要严格不等号（`s9_cap_edge.py`：$n=2,r=3$ 与 $n=4,r=2$ 时落后者离开）。
12. **Remark S2.1。** 乘子应为 $1+(d_K+\delta_f)(\Gamma-1)$，漏了 $\delta_f$。
13. **Cor 5.6。** 在前提 "$p_d\to1$" 之下又列出 "(a) keeping $p_d$ low"，措辞自相矛盾。应写成"改变这一前提本身"。
14. **Prop 5.15(2) 的标题 "allies form blocs"。**
    - 结果证明的是两件事：对第三方的影响不构成一对行动者之间的冲突；这一对之间的冲突被放大 $n/(n-2)$ 倍。"结块"是解释，不是定理，建议标 [conj] 或改述。
    - $b_0n/(n-2)$ 对二次型的第三方损害也成立，按状态单位计（`s5_misc.py`）。
15. **记号（攻击 5）。** 正文末与 S0 都宣称"每个符号全篇只有一义"，这不成立（行号为文件行号）：
    - $J$：S2 第 49 行作雅可比；
    - $\lambda$：S2 第 52 行作特征值，与"对赢的权重"冲突；
    - $D$：S2 第 50 行作对角阵，S4 第 193 行 $[0,1]^D$ 中作域的个数；
    - $v$：Remark 2.5 中作偏差，S2 第 48 行有 $v_j$，S4 第 187 行有 $v_d$；
    - $C$：Assumption 4.2 中是成本函数 $C(q;p)$，Lemma 8.2 中是延续路径；
    - $d$：(15) 中是危害系数，与"纠正速率"冲突；
    - $U$：Prop 5.4(5) 的 $U_i$、S8 第 361 行的均匀抽样 $U_t$、S10 的竞赛收益 $U$，都与"可争议覆盖"冲突；
    - $m$：Prop 3.11 中是非参赛者数，Prop 6.9 中是每层检查数，都与"掩蔽"冲突；
    - $\tau$：S5 第 237 行作侦测时滞，与"责任"冲突；
    - S0 列为"全局"的 $q$、$s$、$F$、$\mu$、$\varpi$ 也各有他义：分别见 Prop 5.4(5)；Lemma 3.3 与 Prop 3.11；Def 3.2；S3 第 151 行；S3 第 125 行；
    - S3 第 107 行的 $\kappa_k$ 作成本，违反"$\kappa$ 带下标即为可转换份额"的约定。

    $\delta$ 只作贴现，这一点成立；$\Phi$ 与 $\mathcal M$ 也一致。修法有两种：
    - 一是把宣称限于表内符号，并给冲突者改名：雅可比改为 $\mathcal J$，Remark 2.5 改用 $u,w$，成本函数改为 $\mathrm{Cost}(q;p)$，(15) 的 $d$ 改为 $h_d$；
    - 二是删去"只有一义"的宣称。

## 三、做得好、不应改的

- **Prop 2.2 的证明干净、正确。** 它由均值与偏差分解、secular 方程加 Perron–Frobenius、Sherman–Morrison 定价组成。
  - 复核：1,500 个随机系统，含 1–3 个通道、对数与线性两种进入方式、各通道的 $k_0$ 与扩散，用全雅可比幂迭代计算，0 例不符（`s1_loopgain.py`）。
  - "固定他人"下，地位价格公式的相对误差为 $4\times10^{-7}$。
  - 应保留，并明确作为结构基准。
- **Prop 5.4 的三处修复全部正确，** 是对 v6.0 两份评审的正确落实：
  - $D$ 相对 $C$ 的三分法；
  - $\bar p_d$ 及其单调区域；
  - 惩罚阶段中的突破。
- **Cor 5.5 的 $n=2$ 混合模仿论证**（反对称矩阵 $y^\top Ay=0$）比 v6.0 更强，而且正确。
- **§4 的成本参数化正确。** 阈值、$q^\ast$、拆分因子、集中度 $\sum p^{1+(2-\xi_v)/\eta}$、支出指数，在 300 组随机 $(\xi_f,\xi_v,\eta)$ 下数值微分 0 例不符。"速率律不依赖规模弹性，阈值与集中度依赖它"这一区分是对的。
- **Prop 5.15。** (1) 用 $E[\min]\le\min E$ 的证明简洁正确；(2) 的 $b_0n/(n-2)$ 正确。
- **Lemma 8.2 改用耦合，是对的。** 独立的两状态动态规划复现了 $S^A\ge S^C$。撤回条件化那一步也是对的。
- **作者的做法应保留。** 一是把检查块分为 independent、identity、derived 三类，只需改两处标签；二是在各 Scope 段坦白"他人固定"和"准静态未测"。方向都对，应把这些前提升格进陈述。

## 四、核对了什么，没核对什么

**核对了：**
- 优先列表中全部结果的陈述与证明，逐条重推。
- 重跑 `checks_v61.py`，输出与 `checks_v61.log` 逐行一致。
- 独立脚本：
  - `s1`：Prop 2.2、2.3；
  - `s2`、`s2b`–`s2e`：MPE；
  - `s3`：Prop 5.4、Cor 5.5、R4；
  - `s4`：§4、准静态、固定成本；
  - `s5`：Lemma 3.10、Thm 10.5、Lemma 8.2、Prop 5.15；
  - `s6`：EC 的蒙特卡洛；
  - `s7`：$[H_f]$；
  - `s8`：logistic 宿主上的裕度；
  - `s9`：Prop 2.3(2) 上限恰为 $K^\ast$ 的边界情形。

**没有核对：**
- Prop 4.9–4.11 与场模型引理；
- Prop 5.1、5.2、5.8–5.13（Thm 5.12 只核对了逻辑）；
- §6 的各命题（只查了记号）；
- Prop 8.3、8.10、8.12、10.6、10.7 与 §11 各结果；
- legacy 套件；
- Abreu 最优惩罚在带吸收态的随机博弈中的推广；
- $n\ge3$ 的 MPE；
- 追赶型竞赛（M1 的放大方向可能在那里反转）；
- 文献：M1 所引的动态竞赛文献凭记忆，标 †。

**模型家族偏差。** 我与起草者、Q2 的规划者同为 Opus 5.5。偏差可能起作用的地方有三处：
- 选择 Tullock 抽签作为代表性的策略模型；
- 参数取在作者的取值附近；
- 倾向于把放大的结果读成"加强了论点"。

M1 与 M2 最需要家族外复核，特别是两件事：在追赶结构中搜索反例；把 EC 做成显式行动的随机博弈版本。
