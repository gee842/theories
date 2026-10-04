# Q2　V6.1 数学修复规格

*2026-10-03。Claude Opus 5.5 子代理，作为 V6.1 的数学规划者撰写。读过：`v6/THEORY.md` §2–§8 与附录 A 全部相关证明；`SYNTHESIS-v6.0.md`；`R-v6.0-math.md` 及其脚本日志；`REVIEW-v6-codex.md` 与 `counterexamples_codex.py`；`R-v6.0-systems.md` 与 `X-v6.0-systems-opus-check.md`（含 `review60-systems-check/` 脚本）；`R-v6.0-adversarial.md` 与 `X-v6.0-adversarial-opus-check.md`；`R-v6.0-alignment.md`；`paper-readiness/X-G2-opus-check.md`；`syn60/k0.py`；`checks_v6.py` 及日志。没有改动任何既有文件。*

*本文件的每个新陈述都在 scratchpad `v61-math/` 用独立脚本核过（纯 Python，`s1`–`s12`，日志同名 `.log`）。"独立"的意思是：用直接计算贴现收益、模拟份额、求数值最优反应或数值雅可比来检验，而不是把要检验的不等式写进检查代码再"验证"它。审阅者与起草者同属一个模型家族，§10.7 的盲点声明同样适用；完成后仍须交家族外复核。*

**怎样读。** 第〇节是结论。第一节回答"一股压力"能否优雅地证明，并给出核心表述与耦合表。第二到十一节逐项给出修复：每项包括问题、新的数学陈述、假设、证明纲要、范围、散文可说与不可说，以及拟用的英文原文。第十二节是检查设计，第十三节是记号表，第十四节列出随之要改的段落。

---

## 〇、结论

1. **"一股压力"能被优雅地证明一部分，不能证明全部。** 可以证明的是**一个环路增益**：在对称地位附近，相对选择、可转换性、决定性三个条件，以及反身闭合（成功买到对规则、纠错者的控制），合成同一个标量
$$\Gamma=(1-\beta)\sum_j r_j\,\omega_j\,\frac{d_j}{d_j+\delta_{f,j}}.$$
   - 平等地位不稳定，当且仅当 $\Gamma>1$。
   - 复利（能力通道）与俘获（规则支持通道）是同一个和里的加项。
   - 同一个增益还给"地位"定价：一单位今天的相对收益值 $\Gamma_\delta/(1-\Gamma_\delta)$ 单位的未来自身收益。由此，任何持有 $\theta_0<n-1$ 的前瞻行动者，都表现得像持有
   $$\theta_\Gamma=\frac{n\theta_0-(n-1)(1+\theta_0)\Gamma_\delta}{n-(1+\theta_0)\Gamma_\delta}\;\to\;-1\quad(\Gamma_\delta\to1).$$
     这就是 Powell（1991）所说"相对收益关切由结构内生"的精确形式：**复利制造相对目标，无论行动者持有什么目标。**
   - 于是宿主的可见度、"够了之点"、对称惩罚的可执行性、两方话语的信息量，都成为 $\Gamma_\delta$ 的比较静态。

   **不能证明的是：** 速率侵蚀（定理 5.12 需要 (X)(U)(φ)，关乎能力的绝对增长，不关乎不平等）、决定性突破的概率 $p_d$ 与决定性位置的价值 $D$（C5、C7），以及多方语言（$n\ge3$ 时相对记账制造联盟而非沉默）。这些不是 $\Gamma$ 的函数。

   **所以作者的决定成立：** 核心应写成"一组相互联系的条件"。命题"一个环路增益"是这组条件之所以**相互联系**、而不是一张清单的形式理由。"一股压力"不应恢复为统摄六个签名的口号。可以说"one loop gain"，只用于复利—转换—俘获—记账这一簇。

2. **执行条件（取代命题 5.7）** 已用马尔可夫链的直接贴现值核对：20 万次随机抽样，0 例不符。
   - 新增一个可执行的等价形式：可容忍的最大突破概率 $\bar p_d=1-[(1-\delta)g+\delta(D-C)]/[\delta(D-v)]$。
   - 新增一个实质发现：若惩罚就是回到竞赛，而竞赛中也可能突破，那么当 $D+U>2P$ 时，"惩罚"是偏离者乐见的彩票。即使偏离本身从不突破，回到竞赛也可能威慑不了（`s1` S1g）。
3. **定理 5.16** 按 $p_d$ 与 $\bar p_d$ 重写。I′、II、III 分别处理。与推论 5.8 一致。个体理性与集体理性分开。
4. **推论 5.8：** $n=2$ 时对**一切**惩罚成立（包括混合策略，模仿对方的混合策略即得 0），比原文更强。$n\ge3$ 时只对"惩罚者同取一策"成立。角色分化的惩罚可以维持纯相对行动者之间的非阶段均衡合作；反例中 $\delta\ge0.706$（`s2`）。
5. **引理 3.3(2)：** 加上"等额负担"和"规避条件"。一旦执行依赖守约者，守约与规避两者都稳定，中间有一个倾覆点（`s5`）。命题 6.7 加前提 $A_\tau$；R8 相应收窄。
6. **引理 3.10：** 改为对一切划分都成立的陈述：收益为全体共有的性状，在任何划分、任何层级上都被选择反对。它只能经 Price 方程的传递项上升，或经改变持有者相对收益的规则上升。"预见"只在失败不可逆、收益为全局时才是唯一及时的途径。
7. **注释 5.3 → 命题 5.3：** 一般形式为
$$\kappa_c\Omega\big((1-\beta)r-1\big)>nk_0+\delta_fS.$$
   - 上限只保证局部稳定。全局保护需要一条不随名次的流入，并给出精确条件。
   - 增长模型变体中，$\rho(r-1)>\delta_f$ 应为 $g_K((1-\beta)r-1)>\delta_f+nk_0/S$。
   - $\chi$ 退回 §4，只作可占有性。
8. **命题 5.14：** 两方时成立。$n\ge3$ 时，一对之间的有效偏差是 $b_0n/(n-2)$，对第三方的影响相互抵消。相对记账让对手失语，让盟友结块，与命题 3.11 相接。
9. **第 4 节：** 速率律 $\alpha\ge g/(1+\eta)$ 与成本是否随规模增长无关，这是稳健的结果。$\sqrt{\cdot}$ 阈值、$k^{2/\eta}$ 和"三阶矩"都取决于成本的规模弹性。按决策计成本、$\eta=1$ 时，集中度的度量恰是 HHI。"拆分只延迟"需要固定成本为零或在下降。全部数值核过（`s7`）。
10. **命题 7.10** 拆成三表：必要（写明模型与期限）、充分、规范。R1、R3、R4、R8 的例外栏按核对结果补全。

---

## 一、"一股压力"能否优雅地证明

### 1.1 判断

作者问：三重侵蚀与复利、俘获结果，是不是同一组共享参数（$\beta,\kappa_c,K_0,r,p_d,D,\chi,b_{ij}$）在一个不等式族里的比较静态。

**回答分三层。**
- **有一个真正的统一。** 复利（注释 5.3）、反身闭合（注释 2.3、命题 4.2、4.8 的证书）是同一个不等式：转换通道增益之和小于一。它们在对称地位处是一个线性环路，秩为一，所以增益相加（命题 A）。
- **记账侵蚀被这个增益驱动。** 同一个增益给地位定价，把任何持有的 $\theta_0$ 推向 $-1$（命题 B）。凡是以 $\theta$ 为参数的结果，都成为 $\Gamma_\delta$ 的比较静态：命题 3.5 的各条、推论 5.8 与注释 5.9 的阈值、两方话语、"够了之点"。
- **其余的不在这个族里。** 执行侵蚀中由决定性突破带来的部分（$p_d$、$D$、$v$），需要 C5（是否存在惩罚不到的位置）、C7（侦测是否快于突破）和 §4 对制裁者的俘获。$\Gamma$ 只决定其中的"到达决定性所需时间"。速率侵蚀需要 (X)(U)(φ)。语言侵蚀在 $n\ge3$ 时方向不单调。

所以，说成"家族相似"对核心来说太弱，说成"一股压力"对全体来说太强。诚实的表述是：**一个环路增益作为核心，通过共享参数和共享状态（集中度），与另两个条件（决定性的位置；速率与覆盖）相连。**

### 1.2 命题 A（一个环路增益）

**模型。** $n$ 个载体，每期争夺奖金 $\Omega$。
- **分配规则。** 份额 $\beta$ 均分，其余按相对强度分配：$p_i=e^{\sigma_i}/\sum_je^{\sigma_j}$。对数强度 $\sigma_i$ 随存量 $X_i^j$ 递增。存量包括能力、规则支持、人才、数据、声望。例如 $\sigma_i=r\ln K_i+r a Z_i$。
- **存量的动态。** 赢得物以比率 $\kappa_j$ 转入存量 $j$；存量 $j$ 另有不靠赢得的流入 $k_{0j}$，以 $d_j$ 折旧，并以 $\delta_{f,j}$ 向均值扩散：
$$X_i^{j\prime}=(1-d_j)X_i^j+\kappa_j\Omega\Big[(1-\beta)p_i+\tfrac{\beta}{n}\Big]+k_{0j}-\delta_{f,j}(X_i^j-\bar X^j).$$
- **对称地位处的三个量。**
  - 决定性 $r_j=\partial\sigma/\partial\ln X^j$。对数进入时等于 $r$；线性进入时等于 $raZ^\ast$。
  - 赢得份额 $\omega_j=\kappa_j\Omega/(\kappa_j\Omega+nk_{0j})$，即存量中来自赢得的部分。
  - 持久度 $d_j/(d_j+\delta_{f,j})$。

**陈述（英文拟文见 1.5）。** 设 $r_j\ge0$，$d_j+\delta_{f,j}\le1$。令
$$\Gamma=(1-\beta)\sum_j r_j\,\omega_j\,\frac{d_j}{d_j+\delta_{f,j}}.$$
1. 平等地位局部渐近稳定，当且仅当 $\Gamma<1$。
2. 若某个条件被移除，$\Gamma$ 即为零：
   - 全部均分（$\beta=1$，没有相对分配）；
   - 不可转换（$\kappa_j=0$ 对一切 $j$）；
   - 没有决定性（$r_j=0$）。
3. 复利通道（能力，$r_K=r$）与反身通道（对规则、纠错者的控制）的增益相加。一个通道独自不足以打开回路，几个通道合起来可以。

**证明纲要。**
- **分解。** 在对称稳态 $X^{j\ast}=(\kappa_j\Omega/n+k_{0j})/d_j$ 处线性化。对和为零的偏差（相对地位的偏差），$\Delta p_i=\Delta\sigma_i/n$。共同方向的偏差不改变份额，乘子为 $1-d_j$。
- **矩阵。** 于是每个载体的相对偏差向量满足 $x'=Jx$，$J=D+\tfrac1n uv^\top$，其中 $D=\mathrm{diag}(1-d_j-\delta_{f,j})$，$u_j=(1-\beta)\Omega\kappa_j$，$v_j=\partial\sigma/\partial X^j$。
- **秩一判据。** $J\ge0$。$\rho(J)<1$ 当且仅当 $I-J=\mathrm{diag}(d_j+\delta_{f,j})-\tfrac1nuv^\top$ 是非奇异 M 矩阵；对秩一修正，这又等价于 $1-\tfrac1nv^\top\mathrm{diag}(d+\delta_f)^{-1}u>0$。
- **化简。** 代入 $X^{j\ast}$，即得 $\Gamma<1$。

**核对。**
- `s3` (A)：4,000 个随机两通道系统中，数值雅可比的谱半径与 $\Gamma$ 判据 0 例不符。
- (A′)：非线性模拟中，偏差在 $\Gamma>1$ 时增长，在 $\Gamma<1$ 时衰减。$\Gamma$ 依次为 1.5、0.3（加入 $k_0$）、0.9（$\beta=0.4$）、1.1（$r=0.8$ 加反身通道）、0.9（纠错加快）、0.75（扩散），结果全部吻合。

**范围。**
- 这是对称地位处的局部陈述。全局情形另需陈述，见第七节的上限。
- 只适用于强化的通道（$r_j\ge0$）。抵消通道（如注释 4.5 的动员）不能简单相减。
- 奖金总额 $\Omega$ 是固定的，即纯再分配。
- 第 4 节的场模型证书 $\sum_jR_{ij}<1$ 与此同形：转换 × 效果 /（阻尼 × 成本），按通道求和。但那是在俘获态取值，不是在对称地位取值。散文只能说"同形"，不能说"同一个定理"。

### 1.3 命题 B（地位的价格；复利制造相对目标）

**陈述。** 在命题 A 的模型中，设某行动者以 $\delta$ 贴现，把净收益按与赢得物相同的比率再投入。令
$$\Gamma_\delta=(1-\beta)\sum_j r_j\,\omega_j\,\frac{\delta d_j}{1-\delta(1-d_j-\delta_{f,j})},$$
则 $\Gamma_\delta<\Gamma$，且 $\delta\to1$ 时 $\Gamma_\delta\to\Gamma$。
1. 今天一单位相对净收益（$\pi_i-\bar\pi$），值未来自身收益的
$$\lambda=\frac{\Gamma_\delta}{1-\Gamma_\delta}$$
个单位（一阶）。当 $\Gamma_\delta\to1$ 时它发散；对有耐心的行动者，发散点就是平等地位失稳的点。
2. 持有 $\theta_0<n-1$ 的行动者，一阶上按命题 3.5 的目标行动，其自我模型为
$$\theta_\Gamma=\frac{n\theta_0-(n-1)(1+\theta_0)\Gamma_\delta}{n-(1+\theta_0)\Gamma_\delta},\qquad 1+\theta_\Gamma=(1+\theta_0)\frac{n(1-\Gamma_\delta)}{n-(1+\theta_0)\Gamma_\delta}.$$
   $\theta_0=0$ 时为 $-(n-1)\Gamma_\delta/(n-\Gamma_\delta)$。$\Gamma_\delta\to1$ 时，$\theta_\Gamma\to-1$ 对一切 $\theta_0<n-1$ 成立。
3. 推论。共同通道的权重 $(1+\theta_\Gamma)/n$ 随 $\Gamma_\delta$ 下降到零，于是以下各项都是 $\Gamma_\delta$ 的单调函数：
   - 宿主的可见度与"够了之点" $(1+\theta_\Gamma)H/n$；
   - 返还征费的权重；
   - 违约收益；
   - 命题 5.14 中两方话语的偏差。

**证明纲要。**
- **价值。** 今天的相对收益 $y$ 按 $\kappa$ 进入各存量的相对偏差。此后每期自身收益增加 $\tfrac{(1-\beta)\Omega}{n}v^\top J^{t-1}\kappa y$，现值为 $\delta\tfrac{(1-\beta)\Omega}{n}v^\top(I-\delta J)^{-1}\kappa y$。由 Sherman–Morrison 化简为 $\lambda y$。
- **$\theta_0\ne0$ 的修正。** 未来奖金总额固定，所以他人平均收益减少 $\Delta W_i/(n-1)$。连续价值因此乘以 $(n-1-\theta_0)/(n-1)$。
- **合成。** $\pi_i+\theta_0\bar\pi_{-i}+\lambda'(\pi_i-\bar\pi)$ 除以正系数，即得 $\theta_\Gamma$（命题 3.5(4) 的推广）。

**核对。**
- `s3` (B)：在非线性模型中做扰动、算现值，与 $\Gamma_\delta/(1-\Gamma_\delta)$ 比较，$\Gamma<1$ 的随机系统最大相对误差 $1.7\times10^{-6}$。
- $\Gamma\ge1$ 但 $\Gamma_\delta<1$ 时，随扰动 $x\to0$ 收敛到公式值（6.43 → 6.27 → 6.25 → 6.244，公式为 6.243）。
- (C)、(C′)：两期竞赛中，第一期净收益成为第二期能力。直接求出的对称均衡强度，与命题 3.9 的 $e(\theta_\Gamma)$ 完全一致（六位有效数字），$\theta_0=-0.5,0,0.5,1,1.9$ 全部吻合。

**范围。**
- 这是一阶、局部的结果，假定奖金固定。若能力也扩大奖金，$\lambda$ 更小。
- 它刻画的是"其他人策略固定时，单个行动者的相对收益值多少"。在完整的随机博弈中，状态还会影响他人策略，需要另行处理。
- 若行动者短视（$\delta=0$），则 $\lambda=0$。此时选择本身仍偏向 $\theta=-1$（命题 3.9(4)），两条路径殊途同归。

**数值**（$n=4$，`s12`）：

| $\Gamma_\delta$ | $\theta_0=0$ | $\theta_0=0.4$ | $\theta_0=2$ |
|---|---|---|---|
| 0.25 | −0.20 | +0.15 | +1.77 |
| 0.5 | −0.43 | −0.15 | +1.40 |
| 0.75 | −0.69 | −0.53 | +0.71 |
| 0.9 | −0.87 | −0.80 | −0.08 |
| 0.99 | −0.99 | −0.98 | −0.88 |

### 1.4 它统一了什么，没有统一什么

| 结果 | 是否为 $\Gamma$（或 $\Gamma_\delta$）的比较静态 | 说明 |
|---|---|---|
| 注释 5.3 / 命题 5.3（复利） | **是**，即 $\Gamma<1$ 的单通道情形 | |
| 注释 2.3（反身反馈基准） | **是**，即双通道情形 | 加入复利后，阻尼 $\mu$ 被复利吃掉一部分：$ab<(\mu-d_K\Gamma_K)\,d$ |
| 命题 4.2、4.8(2)（俘获） | **同形** | 场模型中按通道求和的行和；在俘获态取值 |
| 命题 3.5 的各项（可见度、征费、违约、恶意） | **是**，经 $\theta_\Gamma$ | |
| 推论 5.8、注释 5.9 的 $\theta$ 阈值 | **是**，经 $\theta_\Gamma$ | 见 1.7 的数值 |
| 命题 5.14(1)（两方） | **是**，经 $\theta_\Gamma$ 与偏差 | |
| 命题 5.7 中的 $p_d$、$D$、$v$ | **部分** | $\Gamma$ 决定到达决定性的时间 $T_{\text{dec}}=\ln(\bar\Delta/\varepsilon_0)/\ln(1+d_K(\Gamma-1))$；$p_d$ 还取决于决定性门槛（C5）和侦测、反应时滞（C7）；$v$ 取决于 §4 对制裁者的俘获 |
| 命题 5.11、定理 5.12（速率） | **否** | 能力的绝对增长与可争议覆盖，即 (X)(U)(φ)，C1 |
| 命题 5.14，$n\ge3$ | **否**（方向不单调） | 相对记账在对手之间压低信息，在盟友之间保留信息 |
| 语言的其他通道（Goodhart、叙事选择） | **否** | |

### 1.5 推荐的核心表述（英文拟文）

**Definition 2.1 (The conditions of winning) [D].** 取代原定义 2.1。$\chi$ 从此处移除，它只保留为第 4 节的可占有性。

> Carriers are any reproducible units that can gain or lose share. A system of carriers is subject to *the loop of winning* when the following conditions hold together. They are interconnected conditions, not one cause; Proposition 2.6 states how the first three and the fourth combine.
> 1. **Relative selection.** What is won is allocated by success relative to the others (Definition 3.2); a share $\beta$ of it may be divided equally whatever the outcome.
> 2. **Convertibility.** Part of what is won, a share $\kappa_j$, converts into stocks that raise future winning: capacity, rule support, talent, data, standing. Stocks also come from sources not won in the contest ($k_{0j}$).
> 3. **Decisiveness.** Stocks convert into winning by an increasing success function; $r_j$ is the decisiveness of stock $j$.
> 4. **Reflexive access.** Among the stocks that success can buy is control over the selection itself: the rules, the evaluators and correctors, the formation of minds, the language in which success is described (Definition 2.2).
>
> Two further conditions decide what the loop does to those who live with it, and they are not functions of the loop: whether a position beyond any sanction can be reached (decisive positions, Section 5.2; crux C5), and whether capability grows faster than contestable correction (Section 5.3; crux C1).

**Proposition 2.6 (One loop gain) [T].** 放在 §2.1 末，或作为 §5.1 的开头。

> *In the contest above, let the stocks evolve as $X_i^{j\prime}=(1-d_j)X_i^j+\kappa_j\Omega[(1-\beta)p_i+\beta/n]+k_{0j}-\delta_{f,j}(X_i^j-\bar X^j)$, with $p_i=e^{\sigma_i}/\sum_ke^{\sigma_k}$ and strength $\sigma_i$ increasing in each stock. At equal standing write $r_j=\partial\sigma/\partial\ln X^j\ge0$, $\omega_j=\kappa_j\Omega/(\kappa_j\Omega+nk_{0j})$ for the share of stock $j$ that is won, and let*
> $$\Gamma=(1-\beta)\sum_jr_j\,\omega_j\,\frac{d_j}{d_j+\delta_{f,j}}.$$
> 1. *Equal standing is unstable if and only if $\Gamma>1$. The channels add: compounding through capacity and the reflexive closure through control over the rules are terms of one sum.*
> 2. *For an actor discounting at $\delta$, a unit of relative net payoff today is worth $\Gamma_\delta/(1-\Gamma_\delta)$ units of its own future payoff, where $\Gamma_\delta=(1-\beta)\sum_jr_j\omega_j\,\delta d_j/(1-\delta(1-d_j-\delta_{f,j}))<\Gamma$, and $\Gamma_\delta\to\Gamma$ as $\delta\to1$.*
> 3. *An actor that holds the self-model $\theta_0<n-1$ therefore acts, to first order, as if it held*
> $$\theta_\Gamma=\frac{n\theta_0-(n-1)(1+\theta_0)\Gamma_\delta}{n-(1+\theta_0)\Gamma_\delta},$$
> *which falls to $-1$ as $\Gamma_\delta\to1$. Compounding manufactures the relative objective, whatever objective is held.*

紧随其后的一段散文：

> The conditions of Definition 2.1 are interconnected in a precise sense. Sharing, provision not won in the contest, diffusion and correction each lower $\Gamma$; decisiveness and every channel through which success buys advantage raise it. The same $\Gamma$ that decides whether leads compound decides how much standing is worth, and so how far every actor's working self-model moves toward the purely relative one (Proposition 3.5). This is the formal content of an older observation: concern for relative gains depends on how far gains convert into future advantage (Powell 1991). What $\Gamma$ does not decide is whether a position beyond sanction can be reached, and whether capability outruns correction. Those are separate conditions, and Sections 5.2 and 5.3 treat them.

### 1.6 耦合表（"相互联系的条件"之所以相互联系）

符号约定："↑险"表示参数升高使该处的危险（失稳、侵蚀）加重；"↓险"表示减轻；"0"表示在模型中没有直接作用；"经 X"表示间接作用。

| 参数 | $\Gamma$（命题 2.6/5.3） | $\theta_\Gamma$ 与记账（3.5） | 执行：$p_d$ 与 $\bar p_d$（5.7） | 俘获证书（4.4/4.8） | 两方话语（5.14） | 速率与覆盖（5.11/5.12） |
|---|---|---|---|---|---|---|
| $\beta$ 分享 | ↓险（所有通道乘以 $1-\beta$） | ↓险 | $g$↓：↓险。$D-C$：承诺式分享为↑险（胜后可食言，命题 5.10(3)），同期托管为 0 | 0 | ↓险 | 0 |
| $\kappa_c$ 可转换 | $k_0>0$ 时↑险；$k_0=0$ 时为 0 | 同左 | 经 $\Gamma$ 缩短 $T_{\text{dec}}$：↑险 | 0（转入控制的 $\kappa_Z$ 为↑险） | 经 $\theta_\Gamma$ | 0 |
| $k_0$ 不靠赢得的供给（"树"） | ↓险（降低 $\omega$） | ↓险 | $p_d$↓，且落后者保有惩罚能力，$v$↓：↓险 | 0 | ↓险 | 0 |
| $r_j$ 决定性 | ↑险 | ↑险 | $p_d$↑，$g$↑：↑险 | 经反身通道：↑险 | ↑险 | 0 |
| $\delta_f$ 扩散 | ↓险 | ↓险 | $p_d$↓（领先衰减，注释 7.1）：↓险 | 0 | ↓险 | 0 |
| $\chi$、$b_{ij}$ 可占有与转换 | ↑险（反身通道） | ↑险 | 制裁者被俘获，$v$↑：↑险 | ↑险（4.2(3)、4.4(2)） | 指标被俘获，$m$↑：↑险 | 被俘获的评估降低 $U$：↑险 |
| $d$ 纠正速率 | ↓险（$\Gamma_Z\propto1/d_Z$） | ↓险 | ↓险 | ↓险 | ↓险 | ↓险 |
| $\gamma$ 控制成本（AI 使其↓，[A]） | $\gamma$↓：↑险 | 经 $\Gamma$ | 经 $v$：↑险 | $\gamma$↓：↑险 | 经 $m$ | 视情况 ± |
| $f$ 固定成本 | 0 | 0 | 0 | ↓险（阈值；需求封顶） | 0 | 0 |
| $\Omega$ 赌注，$k_0$ 不变 | ↑险（$\omega$↑） | ↑险 | 各项同比放大时为 0；经 $p_d$ 为↑险 | ↑险（规则支持的价值↑） | ↑险 | 经 (X) |
| $p_d$ | 0 | 0 | ↑险 | 0 | 0 | 0 |
| $D-C$ | 0 | 0 | ↑险（$\bar p_d$↓） | 0 | 0 | 0 |
| $\delta$ 耐心 | $\Gamma_\delta$↑：↑险 | ↑险 | 重复博弈更强：↓险。**双刃** | 0 | 经 $\theta_\Gamma$ | 0 |
| $\theta_0$ 持有的自我模型 | 0 | ↓险 | ↓险 | 0 | ↓险 | 0 |
| 侦测时滞 $\tau$（C7） | 0 | 0 | $p_d$↑：↑险 | 0 | 0 | 0 |
| (X)(U)(φ) | 0 | 0 | 0 | 0 | 0 | 承载全部 |

**表中最值得写进正文的三处：**
- **$k_0$ 降低 $\Gamma$。** 这是"树"的形式内容（综合第二节第 2 条），而且它同时作用于 $\Gamma$、$\theta_\Gamma$ 和 $p_d$。
- **耐心是双刃的。** 它加强重复博弈的执行，又抬高地位的价格。
- **承诺式分享在执行条件里是↑险。** 原因是决定性的胜者可以食言。

### 1.7 剪刀差的精确形式（取代 §5.5 的复合陈述）

> **The scissors, stated exactly [T∣A].** *Restraint is enforceable iff $p_d\le\bar p_d$ (Proposition 5.7(2)). Under the conditions of Definition 2.1, growth in the stakes relative to provision not won in the contest, and a falling cost of control, move both sides at once:*
> - *it raises $p_d$, because a larger $\Gamma$ shortens the time a lead needs to become decisive;*
> - *it lowers $\bar p_d$, because larger stakes raise the one-period gain and the value of a decisive position, capture of the correctors weakens the sanction ($v$ rises), and a larger $\Gamma_\delta$ moves every actor's working objective toward the relative one.*
>
> *Each arm is proved under its own conditions; the conjunction is composite. It is the precise sense in which the means of restraint weaken as the thing to be restrained grows.*

**数值示意（简化形式，标 [N, reduced form]）。** 取注释 5.9 的二元博弈（$n=4$，$\delta=0.9$，$D=C$），令行动者的工作目标为 $\theta_\Gamma(\theta_0,\Gamma_\delta)$。可执行克制所容许的最大 $\Gamma_\delta$（`s12`）：

| $p_d$ | $\theta_0=0$ | $\theta_0=0.4$ |
|---|---|---|
| 0 | 0.92 | 0.95 |
| 0.5 | 0.85 | 0.91 |
| 0.9 | 0.39 | 0.62 |
| ≥ 0.99 | 不存在 | 不存在 |

这是两片刀刃同时作用的数值形式。

**简化形式的前提。** 二元博弈与一个复利竞赛并行进行，后者按地位分配赢得物。此时随机博弈的状态效应已由 $\lambda$ 一阶吸收，不重复计算。

### 1.8 散文可说与不可说

**可说：**
- "The conditions of winning combine into one loop gain"；
- "compounding manufactures the relative objective"；
- "compounding and capture are terms of one sum"；
- "the scissors is the joint movement of $p_d$ and $\bar p_d$"。

**不可说：**
- 六个签名出自"one pressure"；
- 速率侵蚀、决定性突破、多方语言是 $\Gamma$ 的结果；
- 平等地位的全局性质由 $\Gamma$ 决定；
- 命题 2.6 是"新的自然律"。它是标准的线性稳定性加 Sherman–Morrison 计算，新的是组织方式和它对 $\theta$ 的含义。

§2.7 的单因子预测降为 [C]，这一点 SYNTHESIS 已定。可以加一条从命题 2.6 推出的**区分性**预测：

> **(T-Γ)** *Conduct's sensitivity to shared harm should fall with measured provision not won in the contest relative to the stakes, and with diffusion, holding declared objectives fixed. A theory in which relative concern is a fixed preference predicts no such interaction.*

---

## 二、修复 1：执行条件（取代命题 5.7）

### 2.1 问题
- **估值方向写反。** 原文把决定性位置估为"不超过合作收益"，并称这是"对合作最有利的情形"，方向正好反了。"当且仅当"只在 $D=C$ 时成立（Codex 1；Math I1）。
- **DF 检验是循环的。** 它用待证的不等式来定义"可维持"。
- **证明漏了一项。** 惩罚阶段同样存在突破的可能，原证明没有计入。

### 2.2 新陈述

**设定。**
- 阶段博弈以贴现 $\delta\in(0,1)$ 重复，每个行动者按自己的目标 $O_i$ 行动，监督是完美的。
- $a^\ast$ 的每期值为 $C_i=O_i(a^\ast)$；一期偏离收益为 $g_i=\max_aO_i(a,a^\ast_{-i})-C_i$。
- 偏离后，自下一期起以概率 $p_d$ 进入决定性位置：一个吸收态，超出一切惩罚，对 $i$ 每期值 $D_i$。
- 否则进入对 $i$ 的最严厉的可信惩罚。$v_i$ 是该惩罚的归一化值，即 $(1-\delta)$ 乘以其续值，并且**在每一期（包括惩罚阶段）都可能突破的同一个博弈里计算**。

**陈述。**
1. **执行条件（精确）。** 在"$i$ 偏离后转入 $i$ 的最严厉可信惩罚"这一策略组合下，$a^\ast$ 可维持，当且仅当对每个 $i$：
$$(1-\delta)g_i+\delta p_d(D_i-C_i)\;\le\;\delta(1-p_d)(C_i-v_i).$$
   左边是诱惑：即期收益，加上突破的期望收益。右边是剩下的制裁。
2. **等价形式。** 当 $D_i>v_i$ 时，$a^\ast$ 可维持当且仅当 $p_d\le\bar p_{d,i}$，其中
$$\bar p_{d,i}=1-\frac{(1-\delta)g_i+\delta(D_i-C_i)}{\delta(D_i-v_i)}.$$
   在 $D_i>v_i$ 且 $0\le\bar p_{d,i}<1$ 的区域内，$\bar p_{d,i}$ 随 $g_i$、$D_i$、$v_i$ 下降，随 $C_i$ 上升。
   - 对 $D_i$ 的单调性要求 $\bar p_{d,i}\ge0$，即 $(1-\delta)g_i\le\delta(C_i-v_i)$。
   - 对 $v_i$ 的单调性要求 $\bar p_{d,i}<1$。
3. **与旧界的关系。** 去掉突破项的界 $(1-\delta)g_i\le\delta(1-p_d)(C_i-v_i)$：
   - $D_i=C_i$ 时精确；
   - $D_i\ge C_i$ 时只是必要条件；
   - $D_i\le C_i$ 时只是充分条件。
4. **极限 $p_d\to1$。** 条件变为 $(1-\delta)g_i\le\delta(C_i-D_i)$。
   - 若 $D_i\ge C_i$，可维持的组合包含在所持目标的阶段均衡之内；若 $D_i>C_i$，则严格在内。克制必须连一次成功的突破都胜过：$g_i\le-\delta(D_i-C_i)/(1-\delta)<0$。
   - 若 $D_i<C_i$，非阶段均衡的合作在 $p_d=1$ 时仍可存活。
5. **惩罚中的突破改变 $v_i$。** 两人博弈，惩罚是回到"都竞赛"这一阶段均衡（每期值 $P_i$）；每个竞赛者每期以概率 $q$ 突破，$U_i$ 是被支配的每期值。则
$$v_i=\frac{(1-\delta)P_i+\delta q(D_i+U_i)}{1-\delta+2\delta q}.$$
   若 $D_i+U_i>2P_i$，回到竞赛就是偏离者乐见的彩票。即使偏离本身从不突破（$p_d=0$），也可能威慑不了。

### 2.3 证明纲要
- **(1)** 合作值 $C_i/(1-\delta)$；偏离值 $(C_i+g_i)+\delta[p_dD_i/(1-\delta)+(1-p_d)v_i/(1-\delta)]$。两者比较后乘以 $1-\delta$。由于贴现、支付有界，一次偏离原理在这个带吸收态的随机博弈中成立，所以条件充分且必要（对给定的可信 $v_i$）。若要说"$a^\ast$ 是某个子博弈完美均衡的路径"，须把 $v_i$ 取为该博弈的最小子博弈完美续值，即 Abreu（1988）在吸收态随机博弈中的推广。这一步引用要谨慎写，见 2.5。
- **(2)** 把 (1) 解为 $p_d$ 的不等式。
- **(3)** 新旧两界相差 $\delta p_d(D_i-C_i)$。
- **(4)** 令 $p_d=1$。
- **(5)** 解惩罚阶段的递推 $V_P=P+\delta[q\tfrac{D}{1-\delta}+q\tfrac{U}{1-\delta}+(1-2q)V_P]$。

### 2.4 核对（`s1`）
- **S1a。** 20 万次随机抽样，$D<C$、$D=C$、$D>C$ 各约三分之一。用值迭代直接计算合作值与偏离值，判定结果与 (1) 的条件 **0 例不符**。
- **S1b。** 旧界在三种情形下的表现：

| 情形 | 样本数 | 旧界判可维持、实际偏离有利 | 实际可维持、旧界判否 |
|---|---|---|---|
| $D<C$ | 66,842 | 0 | 10,032 |
| $D=C$ | 66,620 | 0 | 0 |
| $D>C$ | 66,538 | 10,723 | 0 |

- **S1c。** 蒙特卡洛独立抽样与值迭代吻合。
- **S1d。** Codex 的两个反例（$C=3$，$g=1$，$\delta=0.9$；$p_d=1,D=2$ 与 $p_d=0.5,D=3$）都复现：合作值 30，偏离值 22。
- **S1e。** $p_d=1$ 时阈值 $g^\ast=-\delta(D-C)/(1-\delta)$ 的两侧都正确。
- **S1f/g。** $v$ 的闭式与值迭代一致。$D=4$、$U=0$ 时，$q=0.1$ 就使 $v=1.29>C=1$，克制在 $p_d=0$ 时也不可维持；$D=3$、$U=-5$ 时，惩罚反而更严。

### 2.5 范围
- 监督完美；决定性位置是吸收态，在下一期实现。不完美监督见 Green–Porter，属另一模型。
- $p_d$ 是"偏离在惩罚能起作用之前成为决定性"的概率。分支 II 的慢速突破，以"侦测加反应时滞 $\tau$"与"到达决定性时间 $T_{\text{dec}}$"的比较来折算：$p_d=\Pr(T_{\text{dec}}<\tau)$。
- (1) 中的"当且仅当"针对给定的惩罚续值。"$a^\ast$ 是某个子博弈完美均衡的路径"这一说法，需要最小续值存在并可达，在有限阶段博弈加贴现下成立。附录 A 应写一句：Abreu 的最优惩罚码在带吸收态的随机博弈中的推广，引用前请核对。

### 2.6 散文可说与不可说

**可说：**
- 决定性削弱未来的影子；
- $p_d\to1$ 且 $D\ge C$ 时，执行收缩到所持目标的阶段均衡之内，$D>C$ 时严格在内；
- 剪刀差是 $p_d$ 与 $\bar p_d$ 的相向运动；
- 以竞赛为惩罚，在可能突破的世界里不是可靠的惩罚。

**不可说：**
- "当且仅当"不限定 $D=C$；
- 把 $D$ 取为合作值是"保守"或"对合作最有利"；
- DF 块"与直接计算一致"；
- 注释 5.9 中的 $\theta_{\text{rep}}$ 是真阈值的"下界"。它是 $D=C$ 时的阈值；$D>C$ 时真阈值更高，$D<C$ 时更低。

### 2.7 英文拟文

> **Proposition 5.7 (The enforcement condition) [T].** *Consider a stage game repeated with discount $\delta\in(0,1)$ under perfect monitoring, each actor acting on its objective $O_i$. Let $a^\ast$ be a profile with per-period value $C_i=O_i(a^\ast)$, and $g_i=\max_aO_i(a,a^\ast_{-i})-C_i$ the one-period gain from deviating. Suppose a deviation yields, from the next period and with probability $p_d$, a decisive position: an absorbing state beyond any punishment, worth $D_i$ per period to $i$. Let $v_i$ be $(1-\delta)$ times $i$'s continuation value under the harshest credible punishment, computed in the same game, in which breakouts remain possible during punishment.*
> 1. *$a^\ast$ is sustained by reversion to that punishment if and only if, for every $i$,*
> $$(1-\delta)g_i+\delta p_d(D_i-C_i)\le\delta(1-p_d)(C_i-v_i).$$
> *The left side is the temptation, immediate and decisive; the right side is the sanction that remains.*
> 2. *Equivalently, when $D_i>v_i$, $a^\ast$ is sustained iff $p_d\le\bar p_{d,i}=1-\big[(1-\delta)g_i+\delta(D_i-C_i)\big]/\big[\delta(D_i-v_i)\big]$.*
> 3. *The bound without the breakout term, $(1-\delta)g_i\le\delta(1-p_d)(C_i-v_i)$, is exact when $D_i=C_i$, necessary when $D_i\ge C_i$, and sufficient when $D_i\le C_i$.*
> 4. *As $p_d\to1$ the condition becomes $(1-\delta)g_i\le\delta(C_i-D_i)$. If $D_i\ge C_i$ the sustainable profiles lie within the stage-game equilibria of the objectives actually held, strictly within them when $D_i>C_i$: restraint must be preferred even to a breakout that succeeds. If $D_i<C_i$, cooperation that is not a stage equilibrium can survive $p_d=1$.*
> 5. *Breakouts during punishment change $v_i$. If punishment is reversion to a stage equilibrium in which both of two actors race, worth $P_i$ per period, and each racer breaks out with probability $q$ per period, being subordinated being worth $U_i$, then $v_i=[(1-\delta)P_i+\delta q(D_i+U_i)]/(1-\delta+2\delta q)$. When $D_i+U_i>2P_i$, reversion to the race is a lottery the deviator welcomes, and it can fail to deter even where the deviation itself never breaks out.*
>
> *Across 200,000 random parameter settings, direct evaluation of discounted values agrees with (1) in every case, and the bound without the breakout term fails in the directions stated in (3) [N].*

注释 5.9 改动：
- 把缩写 $D=\delta(1-p_d)/(1-\delta)$ 更名为 $\Lambda$，避免与 $D_i$ 冲突。
- 删去"lower bound"一句，改为：

> *"The thresholds are those of the boundary case $D=C$; a decisive position worth more than cooperation raises them: with $D=0.5$ in objective units, $\theta_{\text{rep}}$ at $p_d=0.9$ rises from $-0.32$ to $+2.34$ [N]."*

**T-G 的符号。** 由 (2)，$p_d$ 越高，可执行所需的 $\theta$ 越高，所以目标越重要。T-G 应改为预测正的交互作用：在 $p_d$ 高的领域，测得的 $\theta$ 对克制的影响更大。这与对抗复核遗漏 B 和 Codex 的意见一致。

---

## 三、修复 2：定理 5.16

### 3.1 问题
- **(1) 与推论 5.8 冲突。** $\theta=-1$ 时即使 $p_d=0$ 也不可执行。
- **三个分支被并在一起。** 原文把 I′、II、III 都并入"买不到持久之物"：I′ 买到饱和点，II 买到决定性。
- **把"可得"当成"$p_d\to1$"。**
- **"须共同保管"推不出来。** 证明里的"only custody … keeps $p_d$ near zero"是断言，没有推导。
- **"保管之后仍须阶段均衡"与 (1) 矛盾。** 保管压低 $p_d$ 后，重复博弈的执行就恢复了。
- **混淆了个体理性与集体理性。**

（Math F1；Codex 1；对抗致命 4 及其 Opus 复核。）

### 3.2 分支按 $p_d$ 与 $\Gamma$ 重新定义（定理 5.15 的小改）
- **III（不决定）：** $\Gamma<1$（平等地位稳定），且不存在超出惩罚的位置，$p_d=0$。注意：低 $r$ 不够，反身通道可以让 $\Gamma>1$（`s3` A′ 中 $r=0.8$ 时 $\Gamma=1.1$）。
- **I′（决定但饱和）：** 竞赛买到饱和水平（例如可生存的二次打击），这是持久之物；超过饱和点后 $p_d=0$。
- **II（决定但慢）：** $T_{\text{dec}}$ 长。若侦测加反应快于 $T_{\text{dec}}$，则有效 $p_d$ 小；若慢于它，就落入 I 的情形。竞赛最终买到的是决定性。
- **I（决定、快、不饱和）：** $T_{\text{dec}}<\tau$，$p_d\to1$。

### 3.3 新陈述（英文拟文）

> **Theorem 5.16 (Decisiveness and the enforcement of restraint) [T∣A].** *Let restraint $a^\ast$ be a profile of the repeated contest, with the enforcement condition of Proposition 5.7, and $\bar p_{d,i}$ the largest breakout probability at which $i$'s restraint can be enforced.*
> 1. *Where no deviation yields a position beyond punishment (Branch III; Branch I′ above its saturating level), or where breakouts are detected and answered before they become decisive (Branch II with timely detection), restraint can be enforced by repetition among actors whose working objectives have $\theta>-1$, given monitoring, $C_i>v_i$, $\delta$ above the threshold of Proposition 5.7, and a punishment that does not itself raise the chance of breakout. Among purely relative actors it cannot be enforced, even then, by any punishment the punished actor can imitate (Corollary 5.8). Racing buys no lasting object in Branch III; in Branch I′ it buys the saturating level, and in Branch II a decisive position that timely detection can deny.*
> 2. *Where a deviation yields, with probability $p_d\to1$, a decisive position worth $D_i\ge C_i$ (Branch I, or Branch II without timely detection), the enforceable profiles lie within the stage equilibria of the objectives held, strictly within when $D_i>C_i$ (Proposition 5.7(4)). Durable restraint then requires $p_d\le\bar p_{d,i}$ for every $i$. Two kinds of means achieve it:*
>    - *(a) means that keep $p_d$ low: not building capability of the decisive class (E2); holding it so that no party can use it alone; detection and response faster than breakout (C7, Theorem 7.7);*
>    - *(b) means that raise $\bar p_d$: objectives under which a decisive position is worth no more than restraint, so that $(1-\delta)g_i\le\delta(C_i-D_i)$ and $\bar p_{d,i}\ge1$; sanctions that survive success (a lower $v_i$); and lower stakes in deviation (a lower $g_i$).*
>
>    *The list of means is a classification, not a proof that no other exists.*
> 3. *In case 2, racing can be each actor's best response to a racing rival (Proposition 5.1). What the premise of the race cannot justify is the race as a collective course. That course leaves everyone's protection after a win to the winner's objective (Proposition 5.10). Under the premise [A] of Proposition 7.2(2), it shifts the winners toward those whose objectives give least.*

随后的散文改为：

> This is the correct form of the dilemma. The premise that motivates the race, that a rival might win decisively, describes the regime in which repetition stops enforcing restraint. In that regime restraint rests either on keeping breakouts improbable, or on objectives and sanctions under which a breakout is not worth taking. The race supplies neither.

"we are one" 成为必需的三条件（C5、C7、覆盖不全）保留，但措辞改为：

> "Where decisiveness is attainable, detection is slower than breakout and coverage is incomplete, $p_d$ cannot be kept low, and restraint has to rest on objectives under which a successful breakout is not worth taking."

这正是 §3.8 的第 5 部分（选择标准），把"一体"连到 $\bar p_d\ge1$。

### 3.4 证明纲要
- (1) 由命题 5.7(1) 在 $p_d=0$ 时得到：条件化为 $(1-\delta)g\le\delta(C-v)$，在 $C>v$、$\delta$ 足够大时可满足。$\theta=-1$ 时引推论 5.8。
- 分支 II：有效 $p_d=\Pr(T_{\text{dec}}<\tau)$。
- (2) 由命题 5.7(2)(4) 得到；(a)(b) 是对 $\bar p_d$ 表达式各项的分类。
- (3) 引命题 5.1、5.10、7.2(2)[A]。
- 整体为 [T∣A]，因为它连接了各自条件下证明的结果。

### 3.5 可说与不可说

**可说：** 前提描述的正是执行失效的政权；在其中竞赛不能作为集体路线得到辩护。

**不可说：**
- "须共同保管"作为唯一出路；
- "保管之后仍须阶段均衡"；
- I′ 和 II 买不到任何东西；
- 竞赛对个体不是最优反应。

---

## 四、修复 3：推论 5.8 的范围

### 4.1 判断
- **$n=2$。** 原证明只用了"惩罚者同取一个行动"，结论可以更强。两人对称博弈的相对目标是反对称矩阵 $A$；被罚者模仿惩罚者的**混合**策略 $y$，就得到 $y^\top Ay=0$。所以一切惩罚，包括混合的、非对称的，都给被罚者至少 0。（`s2`(a)：两万次随机抽样，$|y^\top Ay|\le2\times10^{-16}$。）
- **$n\ge3$，匿名博弈。** 若一切惩罚者使用同一个（可以是混合的、独立的）策略，被罚者模仿之，得到一个可交换的组合，期望相对收益为 0。（`s2`(b)：3,000 例 0 违反。）
- **$n\ge3$，角色分化的惩罚。** 反例（`s2`(c)）：三人，行动为 (克制/竞赛) × (X/Y) 的少数派博弈。
  - 合作组合"全体 (R,X)"不是阶段均衡，$g=1.2$。
  - 惩罚组合中，偏离者与一名惩罚者取 X，另一名取 Y：偏离者的相对收益为 $-0.5$。这个组合是目标意义下的阶段纳什均衡，所以冷酷回退是可信的。
  - 合作在 $\delta\ge g/(g+0.5)=0.706$ 时可维持。
  - 若改用对称惩罚（全体 (A,X)），被罚者可以模仿，得 0。
- **Duersch–Oechssler–Schipper（2012）的范围。** 那是两人对称博弈中"若更好则模仿"这一**动态规则**的结果：除非相对收益博弈属于广义石头剪刀布类，否则该规则不会被利用到超过有界的量。推论 5.8 用到的只是一个静态事实：两人对称零和博弈的值为 0。因此石头剪刀布类型也包括在内，只要允许混合模仿。

  引文措辞须对照原文核实。我凭记忆复述，标 †。

### 4.2 英文拟文

> **Corollary 5.8 (Relative objectives and punishments that can be imitated) [T].** *Let the stage game be symmetric and every actor hold the purely relative objective ($\theta=-1$), so that every symmetric profile gives each actor 0.*
> 1. *With two actors, every punishment, mixed or pure, leaves the punished actor at least 0: it can imitate the punisher's strategy, and a symmetric two-player zero-sum game has value 0.*
> 2. *With $n\ge3$ actors in an anonymous game, every punishment in which all punishers use the same strategy leaves the punished actor at least 0.*
>
> *In either case $v_i\ge0=C_i$, so by Proposition 5.7 a symmetric cooperative profile is sustainable only if $(1-\delta)g_i+\delta p_dD_i\le0$; when $D_i\ge0$ it must be a stage equilibrium in objectives, at every $\delta<1$ and every $p_d$.*
> 3. *With $n\ge3$, punishments in which the punishers take different roles can hold a purely relative deviator below zero. In a three-player minority game with a racing dimension, such a punishment is itself a stage equilibrium and sustains cooperation that is not a stage equilibrium for $\delta\ge0.706$ [N].*
>
> *Relative actors can therefore enforce cooperation only by coordinating as blocs against a deviator, which is the enforcement face of Propositions 3.11 and 5.14(2).*

**散文。** 删去"the purely relative objective is the one that the ordinary machinery of repeated cooperation cannot restrain"中的无条件读法，改为"…cannot restrain through punishments the punished can imitate; what remains to it is the machinery of blocs"。

---

## 五、修复 4：引理 3.3(2)、命题 6.7 与 R8

### 5.1 问题
- **普遍适用不等于等额负担。** 一项上限在 $e=(1,0.6,0.2)$ 的三方之间造成 $(0.6,0.2,0)$ 的成本（Math I4；Codex 2）。
- **规避者被选择。** 守约者之间彼此看不见约束，但规避者看得见。
- **共同的责任制不是共同项。** 它恰恰靠改变收益差起作用。
- **命题 6.7(3) 丢了自己的豁免条件（Ali B1）。** 私人可见的偏差会由开发者单方修正。

### 5.2 引理 3.3 新陈述（英文拟文）

> **Lemma 3.3 (Blindness, and what a common rule needs) [T].**
> 1. *(Unchanged.) Under a relative rule, the trajectory of shares is unchanged by any term common to all payoffs …*
> 2. *Incidence. A constraint whose cost is the same additive amount for every carrier is a common term and leaves relative growth unchanged among the carriers that comply. A constraint whose cost differs across carriers changes relative payoffs by the difference in incidence, and is selected on like any payoff difference. A constraint borne by one carrier alone is selected against.*
> 3. *Evasion. If carrier $k$ can evade a constraint that costs it $\kappa_k$, facing an expected sanction $\varsigma_k$ (detection times penalty, including loss of admission), evaders gain $\kappa_k-\varsigma_k$ relative to compliers. Under a payoff-monotone rule with cumulative selection, compliance survives iff $\varsigma_k\ge\kappa_k$ for every type that can evade. If the sanction weakens as evaders spread, because detection is funded by compliers or rule-making is captured by evaders, compliance and evasion are both stable, separated by a tipping share.*

> *A common liability on the harmful conduct is not a common term. Under it $\pi_k-\pi_l=(\nu-\tau_{\text{eff}})(e_k-e_l)$, so it reverses selection on the conduct once $\tau_{\text{eff}}>\nu$ (Proposition 3.4). Coordination works through two routes, which should not be confused: rules that make the harmful conduct pay less for everyone (visible to selection, and reversing it), and common constraints whose compliance cost is equal (invisible to selection among the compliant). Both need coverage, and both need an expected sanction at least the gain from evasion, supplied by correctors that Section 4 shows success can capture.*

**归类。** "普遍约束对相对选择不可见"从 §2.9 的"新增"移入"吸收"（对抗意见 11）。新增的是它与规避条件、执行俘获的连接，即倾覆点。

### 5.3 核对（`s5`）
- 成本 (0.3, 0.1) 下，相对增长率为 $(-0.1,+0.1)$；等额 0.2 下为 $(0,0)$。
- 规避：$\kappa=0.3$。$qF=0.25$ 或 $0.27$ 时规避者份额趋于 1；$qF=0.35$ 或 $0.4$ 时趋于 0。
- 执行依赖守约：$q=q_0(1-x_{\text{ev}})$，$q_0=0.8$，$F=0.6$。倾覆点为 $x=1-\kappa/(q_0F)=0.375$；从 0.05 和 0.2 出发回到全体守约，从 0.4 和 0.6 出发走向全体规避。
- 共同责任制：$\tau=1.5>\nu=1$ 时，高负荷者份额趋于 0；$\tau=0.5$ 时趋于 1。
- $A_\tau$ 的反面：错误率从 0.20 降到 0.01、成本 0.01 的单方保障被选择**偏好**（份额趋于 1）。收益为共同的保障被淘汰。

### 5.4 命题 6.7 新陈述（英文拟文）

> **Proposition 6.7 (The nested reward loop) [T∣A].** *Levels 0–2 as before. Assume that level 2 is relative and payoff-monotone with cumulative selection (H1 of Theorem 4.11), and premise*
> - *$(A_\tau)$: countering the divergence in question at level 1 lowers the developer's payoff net of every private benefit: reliability, demand, liability, avoided losses.*
>
> 1. *Terms common to all developers cancel from the selection at level 2 (Lemma 3.3(1)).*
> 2. *Level 1 counters a divergence of level 0 wherever countering raises the developer's own objective. Divergences whose costs reach the developer through its customers, liability or reputation are private terms, and level 2 favours developers that counter them. Under $(A_\tau)$, developers that counter the divergence lose share, and with cumulative selection their share tends to zero, whatever their objectives (Proposition 3.4(3)).*
> 3. *Under $(A_\tau)$, a constraint adopted by one developer is selected against. A constraint enforced on every developer as a condition of admission survives selection among compliers when its incidence is equal, and survives evasion iff the expected sanction is at least each developer's gain from evasion (Lemma 3.3(2)–(3)); the sanction is itself subject to Section 4.*
>
> *So the divergences that persist in the innermost optimizer are those whose costs fall on common terms and are not covered by an enforced common constraint.*

**原文三条推论的替换：**
- **第一条：**
> "Technical alignment inside one developer removes what is privately costly and whatever is cheaper to remove than to keep. It cannot alone sustain the removal of divergences whose costs are common."
- **第二条：** 把"Instrumental convergence and reward hacking are … coordination problems"收窄为：
> "The parts of instrumental convergence and reward hacking whose costs are common are, at the level that decides, coordination problems."
- **第三条：** 加上开放权重一句：
> "Admission constraints act only before release; weights released openly can be fine-tuned around them."

**新增关键分歧 C9（对齐税）。** 可测的量：安全训练带来的能力差、发布延迟、可监测性税。注意与对抗评审提议的"C9"编号冲突，二者择一另编。

**新增检验 T-L。** 本文预测：私人可见的偏差在一两个发布周期内被修正；共同的或迟发的偏差持续存在，直到出现共同约束或可归责的事件。对立预测：两类偏差修正得一样快。

### 5.5 R8 新行（并入第九节的必要条件表）

| 要求 | 何时必要 | 依据 | 何时不需要 |
|---|---|---|---|
| R8 对共同成本的偏差施加共同准入约束，负担等额，并防规避；在这类约束之外，不按竞赛表现保留决策 | 第 2 层的选择是相对的、累积的；$A_\tau$ 成立；系统按竞赛表现被保留 | 命题 6.7(3)；引理 6.5 | 第 2 层不是相对选择（例如公共授权）；净私人成本 ≤ 0；不按竞赛表现保留；准入只能管到发布之前 |

---

## 六、修复 5：引理 3.10

### 6.1 问题
- **漏了传递项。** Price 方程中的 $\mathrm E[w\Delta z]$ 被丢掉了。
- **"一个群体"只是一种划分方式的选择。**
- **可逆的失败仍然可以试错。**
- **"只剩预见"被称作定理，这不成立。**

（Math I3；Codex 3；对抗 6；Evi I7。）

### 6.2 对一切划分都成立的陈述
设性状给持有者带来成本 $c>0$，给**全体**带来均等的收益。在任意划分下，Price 方程分解为
$$\bar w\Delta\bar z=\underbrace{\operatorname{Cov}_g(w_g,z_g)}_{\text{群间选择}}+\underbrace{\operatorname E_g\operatorname{Cov}_{j\in g}(w_j,z_j)}_{\text{群内选择}}+\underbrace{\operatorname E[w\,\Delta z]}_{\text{传递}}.$$
- **两个选择项都非正。** $w_g$ 与 $w_j$ 中的共同收益对一切单位相同，于是只剩 $-c\,z$。
- **在任何划分、任何层级都如此。** 全局收益在每一层都是共同项，这正是引理 3.3 在每一层的形态。

**对照：只惠及本群的性状。** 若收益只惠及本群，那么在与收益范围相配的划分下，群间项可以为正。这时可以从子单元（国家、企业）的选择或模仿中找到它。

**核对（`s6`）。** 600 个体、30 个单元，五种划分（一群、30 单元、5 集团、随机 50 组、个体）：
- 全局收益：群间项分别为 0、−0.0019、−0.00002、−0.0011、−0.0123，都 ≤ 0。
- 本群收益：按 30 单元划分时群间项为 +0.0097。
- 有偏传递：$\dot z=-cz(1-z)+\mu(1-z)$ 的稳定点为 $\mu/c$（0.4、0.8、1.0），复现 Codex 的例子。
- 可逆与不可逆：失败中不可逆的比例为 0、0.05、0.2、1 时，"只从失败中学习"在 400 期内遭受不可逆损失的概率为 0、0.14、0.46、1.0；预先采纳为 0、0.06、0.22、0.70（基本危险 0.03/期，规则下降到 0.003/期，可逆失败后采纳的概率为 0.5）。这是示意，不是估计。

### 6.3 英文拟文

> **Lemma 3.10 (What selection at any level cannot supply) [T].** *Let a trait cost its bearer and confer a benefit received equally by every member of the population. Under every partition into groups and every payoff-monotone rule, the between-group and within-group selection terms of the Price equation are non-positive: the benefit is a term common to all at every level (Lemma 3.3). The trait can rise only through the transmission term, by biased transmission such as learning, persuasion, or imitation guided by a model of the system rather than by one's own payoff, or through a rule that changes the bearer's relative payoff: policing, liability that returns consequences, reward for contribution that does not convert into advantage, an enforced common constraint (Price 1972; Frank 1995).*

**取代第 611–613 行的散文：**

> At the scale of one host, the benefits of the rules that keep the host viable are common to all. Selection among firms, states or blocs, the subunits of the one host, cannot favour such rules, because their benefits do not differ between subunits. Rules whose benefits are partly local can be found by selection or imitation among subunits, and polycentric experiment is the way to find them. For the common part, two routes remain:
> - adoption after reversible failures, by learning and by coalitions of the harmed (Becker 1983; the history of Section 9.6);
> - adoption before failure, guided by a model of the system.
>
> Where the failure to be avoided is global and irreversible, only the second acts in time. That is where understanding that we are one is required: it acts on the transmission term, and it must hold before the first failure in the class. That the route can succeed has no biological precedent; it is a conjecture [C] that the transition of Section 9 has to make true.

**散文的界限。**
- **可说：** 全局收益的规则在任何层级都不被选择偏好；对全局且不可逆的失败，预见是唯一及时的途径；理解作用在传递项上。
- **不可说：**
  - "the lemma leaves only this route is a theorem"；
  - 规则不能从局部试验中找到；
  - 整合不能来自受害者联盟或从失败中学习。
- **§3.8 的修改。** 第 1 部分把"Lemma 3.10"改为"one host and global benefits (Lemma 3.10)"。第 5 部分不动。
- **新增一行到 §8.6 的表。** 采纳系统评审 F6.1，并加上 Opus 复核的限制："learning about the design itself | bounded parallel variants above a common floor, shared evaluation, adoption by evidence"。

---

## 七、修复 6：注释 5.3 → 命题 5.3（复利），命题 8.6(3)，上限，记号

### 7.1 问题
- **$\chi$ 实为分享参数。** $\chi=1-\beta$。
- **$\kappa$ 在 $k_0=0$ 时与阈值无关。**
- **8.6(3) 的"只有第三个杠杆改变方向"在本文模型中不成立。**
- **上限只保证局部稳定。**
- **"$\rho(r-1)>\delta_f$"没有模型。**

（Math F2；Sys F2 及其 Opus 复核。）

### 7.2 一般形式与核对
**模型（折旧加扩散）。** $K_i'=(1-d_K)K_i+\kappa_c\Omega[(1-\beta)p_i+\beta/n]+k_0-\delta_f(K_i-\bar K)$，$p_i\propto K_i^r$。
- 对称稳态 $K^\ast=(\kappa_c\Omega/n+k_0)/d_K$，总量 $S^\ast=nK^\ast$。
- 平等地位不稳定，当且仅当
$$\kappa_c\Omega\big((1-\beta)r-1\big)>nk_0+\delta_fS^\ast\quad\Longleftrightarrow\quad(1-\beta)\,r\,\omega_K\,\frac{d_K}{d_K+\delta_f}>1,$$
  其中 $\omega_K=\kappa_c\Omega/(\kappa_c\Omega+nk_0)$。
- 这是命题 2.6 的单通道情形。$k_0$ 写成"稳态等价"$K_0=k_0/d_K$ 时，即综合中的 $\kappa_c\Omega((1-\beta)r-1)>nd_KK_0$。综合写作 $n\delta K_0$，结论一致。
- 核对：`s3` (A′)；`syn60/k0.py`；Opus 复核的 C3（60 例中 59 例吻合，1 例恰在等号上）。

**增长变体（无折旧）。** 总量每期增长 $\rho\Omega$，即原文的 $\rho$。份额乘子为 $\frac{S(1-\delta_f)+\rho\Omega(1-\beta)r}{S+\rho\Omega+nk_0}$，所以不稳定当且仅当
$$\rho\Omega\big((1-\beta)r-1\big)>\delta_fS+nk_0.$$
- 记 $g_K=\rho\Omega/S$ 为能力的增长率，条件为 $g_K((1-\beta)r-1)>\delta_f+nk_0/S$。
- 原文"$\rho(r-1)>\delta_f$"是 $\beta=0$、$k_0=0$ 且 $\rho$ 被理解为 $g_K$ 时的特例。
- **$S$ 随时间增长。** 若奖金不随总能力增长，条件会随时间失效。只有赌注与能力同步增长（$\Omega\propto S$）时，它才是常数。
- 核对：`s8` (10)，四种情形与线性化乘子一致。

**上限（局部与全局）。** 设除落后者外都已到上限 $\bar K\le K^\ast$。落后者的净流入为
$$\phi(K)=\kappa_c\Omega\Big[(1-\beta)\tfrac{K^r}{K^r+(n-1)\bar K^r}+\tfrac\beta n\Big]+k_0-d_KK.$$
- 上限从**每一个**起点都保住平等地位，当且仅当 $\phi(K)>0$ 对一切 $K\in(0,\bar K)$ 成立。
- $r>1$ 时，这要求一条不随名次的流入：$\beta\kappa_c\Omega/n+k_0>0$。
- 一个简单的充分条件是 $\beta\kappa_c\Omega/n+k_0\ge d_K\bar K$。
- 核对（`s8` (9)，$n=5$，$r=1.5$，$\bar K=1.5<K^\ast=2$，落后者从 0.1 出发）：

| $\beta$ | $k_0$ | $\min_K\phi$ | 模拟终值 |
|---|---|---|---|
| 0 | 0 | −0.0041 | 被排除 |
| 0.02 | 0 | −0.0023 | 停在 0.059 |
| 0.2 | 0 | +0.013 | 全体到上限 |
| 0 | 0.002 | −0.0021 | 停在 0.06 |
| 0 | 0.03 | +0.026 | 全体到上限 |

  精确条件与模拟全部一致。

### 7.3 英文拟文

> **Proposition 5.3 (When winnings compound, and what enough requires) [T].** *Let $n$ agents hold capacity $K_i$ and divide a prize $\Omega$ each period, a share $\beta$ equally and the rest in proportion to $p_i=K_i^r/\sum_jK_j^r$. A share $\kappa_c$ of what each receives converts into capacity; capacity also receives $k_0$ per period from sources not won in the contest, depreciates at rate $d_K$, and diffuses toward the mean at rate $\delta_f$.*
> 1. *Equal standing is unstable if and only if*
> $$\kappa_c\Omega\big((1-\beta)r-1\big)>nk_0+\delta_fS^\ast,$$
> *where $S^\ast$ is total capacity at equal standing. Without capacity from outside the contest and without diffusion, the condition is $(1-\beta)r>1$, and $\kappa_c$ sets only the level of capacity. With such a source, a smaller convertible share stabilizes equal standing. This is Proposition 2.6 with one channel.*
> 2. *If total capacity grows without depreciation, by the reinvested prize, the condition holds at each date with $S$ the current total: $\rho\Omega((1-\beta)r-1)>\delta_fS+nk_0$. It is constant only if the stakes grow with total capacity.*
> 3. *A point of enough. If agents stop reinvesting at a cap $\bar K\le K^\ast$, equal standing is locally stable. It is restored from every starting point if and only if a laggard's inflow exceeds its depreciation at every level below the cap. When $r>1$ this needs inflow not tied to rank, from sharing or from provision, and $\beta\kappa_c\Omega/n+k_0\ge d_K\bar K$ suffices. Without it, laggards below a threshold are excluded. A cap above $K^\ast$ only limits the winners.*

**随后的散文：**
- 原来的三要素加 $r$ 改为四个量：$(1-\beta)$、$\kappa_c$ 与 $k_0$、$r$、上限。
- 加一句：
> "Provision beneath the game is not only a support for those who fall behind: it is what makes a point of enough hold globally, and what makes non-convertible rewards work."

**命题 8.6(3) 英文拟文：**

> 3. *Changing what winning converts into. Let a share $\kappa_c$ of winnings be convertible into capacity in the same contest, with capacity also coming from sources not won in it. Equal standing is unstable iff $\kappa_c\Omega((1-\beta)r-1)>nk_0+\delta_fS^\ast$ (Proposition 5.3). Without such sources, $\kappa_c$ sets only the level. Making winnings non-convertible stabilizes standing only together with provision not won in the contest. If success cannot be converted into control over correction ($\chi=0$ in Section 4), the reflexive channel of Proposition 2.6 vanishes, the return to influence over correctors is zero (Proposition 4.2(3)), and the required correction rate falls to its value without second-order selection (Proposition 4.4(2)).*

**三杠杆总结改为：**

> Pooling widens the effective self of anyone who values its absolute payoff, and does nothing under relative selection. Sharing scales every channel of the loop by $1-\beta$; it can stabilize equal standing, but it does not change the sign of the selected intensity while a positional part remains (part 2). Changing what winning converts into lowers the won share of each stock, which needs provision not won in the contest, or removes a channel outright, which is what $\chi=0$ does to the reflexive closure. None of the three makes the uninvadable intensity zero while a positional prize remains; that needs custody or prevention of the positional part.

**第二股（§8.2）条件改为：**

> "$\Gamma\le1$: $(1-\beta)r\,\omega_K<1$ for capacity, and success cannot buy control over its own assessment (the reflexive channels removed, $\chi\to0$)"

同时采纳 Opus 复核的意见：Compact 的公共层就是 $k_0$。

### 7.4 记号
- **删去定义 2.1 中的 $\chi$ 与 $\rho$。**
- **$\chi$ 只作第 4 节的可占有性。**
- **分享一律用 $\beta$。** 它与 §4.4 的 $\beta_{\text{in}},\beta_{\text{out}}$、命题 6.1(5) 的 $\beta_b$ 等有下标区分。
- **可转换份额用 $\kappa_c$。** 与 §3.6 的耦合 $\kappa$ 以下标区分；若起草者认为仍易混淆，可改用 $\xi_c$。
- **折旧用 $d_K$。** 原为 $\delta$，与贴现冲突。
- **扩散沿用注释 7.1 的 $\delta_f$。**
- 详见第十三节。

---

## 八、修复 7：命题 5.14

### 8.1 问题
"相对目标即零和，故话语无信息"在 $n\ge3$ 时不成立（Codex 5；Math I2）。

### 8.2 一般结构与新结果
设 $\theta=-1$，$n\ge3$，发送者 $S$、接收者 $R$：
$$O_S-O_R=\frac{n}{n-1}(\pi_S-\pi_R),\qquad O_S+O_R=\frac{n-2}{n-1}(\pi_S+\pi_R)-\frac{2}{n-1}\sum_{k\ne S,R}\pi_k.$$
- 接收者行动对第三方的影响，以相同方式进入两者的目标。
- 这一对之间的冲突，只来自两者之间的物质冲突，并被放大。

**均匀二次模型。**
- 设定：$\pi_S=-(y-u-b_0)^2$，$\pi_R=-(y-u)^2$，第三方 $\pi_k=-\kappa_ky$。
- 有效偏差（两者理想点之差）为
$$b_{\text{eff}}=b_0\frac{n}{n-2},$$
  与 $\kappa_k$ 无关。
- 信息性均衡存在，当且仅当 $b_{\text{eff}}<1/4$。
- $n\to2^+$ 时偏差趋于无穷，回到 (1)；$n\to\infty$ 时偏差趋于 $b_0$。

**核对（`s4`）。**
- 恒等式：一万次抽样，误差 $3.6\times10^{-15}$。
- 理想点之差由数值最大化求得，与 $b_0n/(n-2)$ 完全一致（$n=3,4,6,10$）。
- 两条消息的分割均衡直接构造：边界类型无差异，接收者对期望目标作数值最优反应。均衡存在当且仅当 $b_{\text{eff}}<1/4$；边界 $a=1/2-2b_{\text{eff}}$ 与 CS 一致。
- $b_0=0$、$\kappa=0.7$（共同对第三方施加成本）时，完全揭示是均衡。
- 三人二元例子：Codex 与 Math 的例子都复现，接收者价值从 1/4 升到 1/2。

### 8.3 英文拟文

> **Proposition 5.14 (Talk under relative accounting) [T].**
> 1. *Two parties. Where a sender's and a receiver's objectives sum to zero at every state and action, every equilibrium is payoff-equivalent to one without talk (Crawford and Sobel 1982; Farrell and Rabin 1996). Two actors with $\theta=-1$ in a two-player game are such a pair (Proposition 3.5(2)).*
> 2. *Three or more. With $n\ge3$ actors at $\theta=-1$, $O_S-O_R=\frac{n}{n-1}(\pi_S-\pi_R)$: what the receiver's action does to third parties enters both objectives alike. A pair of rivals is therefore not opposed about actions against a third, and talk between them can be fully informative there. In the uniform-quadratic model a material bias $b_0$ between them becomes an effective bias $b_0n/(n-2)$, and informative talk exists iff $b_0n/(n-2)<1/4$ [N].*
> 3. *(Crawford–Sobel, unchanged.)*
> 4. *(Shared hazard, unchanged; cite Aumann 1990 for the point that a sender who intends to race still gains from the receiver's cooperation.)*

**随后的散文：**

> Relative accounting silences talk between two opponents and amplifies their material conflict; among three or more it keeps talk informative about what a pair can do to others. The third erosion has two faces: rivals stop informing one another, and those who still inform one another do so as blocs against third parties. That is the language face of Proposition 3.11, and of Corollary 5.8(3) for enforcement.

**§2.3、§2.4、§5.6 表、§9.2 的改动。** "where objectives are opposed"后加"(between two parties; among more, talk binds blocs)"。

---

## 九、修复 8：命题 7.10 拆成三表

### 9.1 问题
- **R1 换了期限。** 定理 8.2(3) 讲的是全时可存续；有限期限下存在反例。
- **R3 把充分当必要。** 行和小于一是充分的全局证书；Codex 给出 $R=2$、低初值时不被俘获的反例。
- **R4 的例外不全。**
- **R7 是价值要求。**
- **R8 的例外不全。**

（Codex 4；Math I6；对抗复核遗漏 A。）

### 9.2 新陈述（英文拟文）

> **Proposition 7.10 (Requirements, by the kind of support each has) [T∣A].** *Table A states conditions that are necessary in a named model and over a named horizon; each is necessary only there, and the last column names the routes by which an arrangement can do without it. Table B lists safeguards that are sufficient and not necessary. Table C lists requirements that rest on values. The proposition organizes results proved elsewhere; it does not rank designs.*

**表 A　必要条件（写明模型与期限）**

| 要求 | 何时必要 | 模型与期限 | 依据 | 何时不需要 |
|---|---|---|---|---|
| **R1** 后果回流：有效责任的长期平均 ≥ $\nu$ | 全时可存续 | 宿主 (1)；H0；复制者选择；存在竞赛策略载体（支持假设） | 定理 8.2(3) | **有限期限 $H$**：零责任轨迹在 $H$ 之前不越过地板（Codex 例：$V(50)\ge0.435>0.2$，满负荷到 109.9 才越过，`s9` (c)）；H0 不成立；竞赛载体不存在，或累积优势有界（命题 3.4(4)）。有限期限下的必要条件是：责任须把累积优势路径压到"恰触地板于 $H$"的路径之下（单调比较） |
| **R2** 覆盖每一个份额能增长的行动者 | 全时可存续 | 同 R1，且未覆盖者的负荷能达到 H0 水平 | 命题 3.4(3)、8.3(1)；引理 3.3(2) | 危害只在本地；未覆盖者合计的最大负荷到不了地板：$h\,p_{\text{unc}}\bar e<\rho(1-V_{\min}/K)$；期限短于越过所需的时间 |
| **R3a** 独立纠错的增长率 ≥ $g/(1+\eta)$，或移除转换通道 | 评估证书对一切 $t$ 成立 | 场模型；$\mathcal C$ 已被俘获；存在正的培育通道；$\gamma$ 以 $g$ 下降 [H_γ]；能力准静态 | 命题 4.4(3) | $\chi=0$ 或通道被移除；固定成本 $f$ 不下降（需求封顶，4.4(5)）；$\mathcal C$ 未被俘获；期限短于失效时刻 |
| **R3b** $\operatorname{core}(\mathcal D)=\emptyset$ | 从**每一个**初态都不被俘获 | 场模型 (3) | 命题 4.8(4) | 只需排除实际会到达的初态（Codex：$R=2$，初值 0.1 时收敛到无俘获）。全行和 < 1 是更强的充分条件，见表 B |
| **R4** $p_d\le\bar p_d$ | 突破可能时可执行的克制 | 命题 5.7，$D\ge C$ | 定理 5.16(2) | 分支 III；I′ 的饱和点以上；II 且侦测及时；$D<C$；目标与制裁使 $\bar p_d\ge1$ |
| **R5** 未覆盖的危险份额可求和 | $H\to\infty$ 时生存不趋于零 | (X)(U)(φ) | 定理 5.12 及其逆命题 | (X)、(U) 或 (φ) 任一不成立；有限期限下改用命题 5.13 的暴露 |
| **R8** 见第五节 5.5 | 见第五节 5.5 | | | |

**表 B　充分保障（不必要）**

| 保障 | 保证什么 | 依据 |
|---|---|---|
| 每个纠错域的全行和 < 1 | 该域从一切状态都不被俘获 | 命题 4.8(2) |
| (I1)–(I4) | logistic 宿主下的可存续（附暂态条件）；逐点更苛刻的宿主需要裕度 $\Delta>\Delta_{\min}$ | 定理 8.2(1)，第十一节 |
| 独立于被观察者的观察：保守警报、析取警报 | 警报在越过地板之前触发 | 注释 4.7(1)(3) |
| 共同保管、不建造、侦测快于突破 | 压低 $p_d$ | 定理 5.16(2a) |
| 核查，且 $\upsilon F$ 不小于净退出收益 | 阻止不可逆的退出 | 命题 7.6 |

R6（观察独立于被观察者、共同测量、可核查信号）改列于此。直接观察行为的通道足够时，R6 不必要。

**表 C　规范要求**

| 要求 | 依据 |
|---|---|
| **R7** 受影响者有资格；包容不止于俱乐部 | V3。命题 3.11 证明的是：相对于系统最优，对局外人的伤害被过度生产。它没有证明 O1/O2 超出容忍度 |
| 对单方支配的保护先定，不拿来换参与 | §8.5 |

**"不能单独满足"一句改为：**

> "R2 needs more than one party by definition. R3 is a second-order public good that competitors do not supply (Proposition 4.3). Of the means in R4, custody needs more than one party, and not building binds only the one that refrains."

**§7.11 事先登记的条件。** 按对抗复核遗漏 A 重写，不用五项合取。每个条件单独写明它成立时建议的哪一部分改变：
- C1 成立 → 速度部分改向"加强纠错的继续"；
- C5、C7 成立 → 保管部分降为预备；
- D4 成立 → 胜者内部纠错的担忧解除；
- 各辖区规则满足表 A → 本文说受监管的竞争满足要求。

### 9.3 核对
- R1：`s9` (c)。
- R3b：Codex 的 RK4 不变矩形论证，并入 `checks_v61` 的 FA 块。
- R4：`s1`、`s12` (c)。
- R8：`s5` (e)。

---

## 十、修复 9：第 4 节的成本结构

### 10.1 问题（X-G2 复核）
- **三个结论依赖成本按载体计。** $\sqrt{\cdot}$ 阈值、$k^{2/\eta}$、"三阶矩而非 HHI"都要求能力成本不随载体规模增长。按决策计成本时，阈值是线性的，拆分因子是 $k^{1/\eta}$，$\eta=1$ 时集中度的度量是 HHI。
- **$f$ 的张力。** 规模阈值要求 $f>0$；速率律与"拆分只延迟"要求 $f=0$ 或 $f$ 在下降。
- **"AI 降低控制成本"是假说。**

### 10.2 决定：写出一般成本结构，两种情形并列

不宜只选一种。两种都有经济理由：
- **按载体计**（$\xi_v=0$）：影响能力在载体自己的决策之间不相竞用。例如一个标准办公室、一套评估工具链、一笔资助关系，其产出随载体的覆盖面增长。
- **按决策计**（$\xi_v=1$）：每转换一单位成功都要付费。例如按次付费的评估、按议题的游说。

哪一种成立，是一个可检验的经验问题。因此用一个参数族写出全部结果。这样做的好处是**区分出稳健的结论与依赖成本的结论**。

**假设框 4.0（英文拟文）：**

> **Assumption 4.0 (The cost of conversion capacity) [A].** *A carrier with share $p$ pays $C(q;p)=f\,p^{\xi_f}q+\gamma\,p^{\xi_v}q^{1+\eta}/(1+\eta)$ for conversion capacity $q$, with $\eta>0$, $f\ge0$ and size elasticities $\xi_f,\xi_v\in[0,1]$. With $\xi=0$ capacity is non-rival across the carrier's own decisions (a standards office, an evaluation toolchain, a funding relationship); with $\xi=1$ it is bought per decision converted.*
> - *$[H_\gamma]$ AI lowers the variable cost of control, $\gamma(t)=\gamma_0e^{-gt}$.*
> - *$[H_f]$ AI lowers the fixed part as well, $f(t)=f_0e^{-g_ft}$.*
>
> *Both are hypotheses, not observations (EV4 records no retrieved source). Capacity is taken at its selected level $q^\ast(d(t),\gamma(t))$ at every date (quasi-static).*

### 10.3 重述的结果（英文拟文）

> **Proposition 4.2(2).** *With $f>0$, capacity pays only above the size threshold $p^\ast=\big(f/(\chi\bar y^\top M\bar y)\big)^{1/(2-\xi_f)}$: a square-root threshold when the fixed part is per carrier, a linear one when it is per decision. A smaller carrier that carries capacity is selected against. With $f=0$, every carrier with $p>0$ has a positive marginal return at $q=0$, largest for the largest.*

> **Proposition 4.4.** *Parts (1)–(2) hold with $\gamma$ replaced by $\gamma p^{\xi_v}$.*
> 3. *(Rate law.) Under $[H_\gamma]$, with $d(t)=d_0e^{\alpha t}$ and $f=0$ or falling, the certificate holds for all $t$ iff $\alpha\ge g/(1+\eta)$ and $d_0>d^\ast(\gamma_0)$, and fails beyond a finite time if $\alpha<g/(1+\eta)$, **for every size elasticity $\xi_v$**.*
> 5. *(The fixed part.) If $f>0$ does not fall, the requirement levels off at $\max\{A/c_{\mathsf E},\chi\hat Y/(fp^{\xi_f})\}$ and no growth beyond it is needed. Under $[H_f]$ the required rate is $\min\{g_f,g/(1+\eta)\}$.*
> 7. *(Splitting.) Splitting a dominant carrier into $k$ equal parts with no common controller divides cultivated conversion by $k^{(2-\xi_v)/\eta}$.*
>    - *If $f=0$ and the net exponent $g-(1+\eta)\alpha$ is positive, a fixed split delays the failure of the certificate by $\Delta t=(2-\xi_v)\ln k/(g-(1+\eta)\alpha)$ and does not prevent it [N: $\eta=1$, $g=0.2$, $\alpha=0$, $k=10$: $23.0$ at $\xi_v=0$, $11.5$ at $\xi_v=1$].*
>    - *Under $[H_f]$ it delays the onset of cultivation in each part by $(2-\xi_f)\ln k/g_f$.*
>    - *If $f>0$ does not fall, parts below the size threshold cultivate nothing, and the split is permanent.*
>
>    *A permanent effect therefore needs channels removed outright, a fixed cost of control that AI does not lower, or a number of independent units that grows over time.*
> 8. *(Concentration.) Across carriers, total cultivated conversion is proportional to $\sum_kp_k^{1+(2-\xi_v)/\eta}$: the third moment of shares when $\xi_v=0$ and $\eta=1$, the Herfindahl index when $\xi_v=1$ and $\eta=1$. Two equal independent carriers give a quarter of the monopoly value in the first case and a half in the second [N]. Which moment governs capture is an empirical question about how the cost of influence scales with size. The model implies that influence spending rises with share as $p^{\xi_v+(1+\eta)(2-\xi_v)/\eta}$, at least quadratically, which is testable.*

**第 754–757 行的散文。** "under quadratic cost and long horizons, it needs to grow only half as fast"保留，并加一句："This rate does not depend on how the cost of influence scales with size; the size threshold, the splitting factor and the concentration measure do."

**前提的标记。** 中文概要第 4 条、§1.2 第 4 条、§2.9 第 1 条、§4.7 中"AI 降低控制的成本"一律加 [A] 或"if AI lowers…"。A.0 的 (A4) 改为引用假设框 4.0。

**定理 4.11 的 (H2)(H3)。** 写明依赖 $[H_\gamma]$，且 $f=0$ 或 $[H_f]$。

### 10.4 核对（`s7`）
- **阈值。** $f=0.05$ 时，按载体计为 0.22361，按决策计为 0.05000，与公式一致。
- **集中度。** 两个等份额载体相对于垄断：$\xi_v=0$ 为 0.25，$0.5$ 为 0.354，$1$ 为 0.50。份额 (0.5, 0.3, 0.2) 时分别为 0.16（三阶矩）、0.244、0.38（HHI）。
- **拆分因子。** $k^{(2-\xi_v)/\eta}$：$k=10$ 时为 100、31.6、10。
- **速率律。** 主导载体份额 0.6，$\alpha=0.09$ 时三种 $\xi_v$ 的 $s_{\mathsf E}$ 都按 $e^{0.02t}$ 增长并越过 1；$\alpha=0.11$ 时都衰减。
- **拆分延迟。** 模拟得 23.00（$\xi_v=0$）和 11.50（$\xi_v=1$），公式为 23.03 和 11.51。
- **$f$ 固定为 0.3。** 垄断在 10.75 时越过 1，十个部分永不越过。$f$ 以 0.05 下降时，各部分的培育起点比垄断晚 92.1，等于 $2\ln10/0.05$。

**仍未做、应补的：** 能力随选择演化，与场模型 (3) 联合模拟，用来检验准静态假设（X-G2 第 3 点）。见第十二节的 QS 块。

---

## 十一、修复 10：较小的各项

每项给出新陈述和核对。

### 11.1 命题 8.11(3)："够了之点"不专属于相对目标；前提 (φ)

> 3. *An objective that is not satiated in the stakes, whether relative position or an absolute payoff linear in them, has no point of enough: symmetric intensity is proportional to the stakes for every $\theta<n-1$, because the success function is homogeneous of degree zero. An objective bounded in the stakes is satiated, and its intensity is bounded as they grow. The relative objective adds the invisibility of the shared loss (Proposition 3.5). Under (X), (U) and (φ), Theorem 5.12 applies to any continuation branch, whatever the objective.*

- **核对。** `s8` (8)：线性 $u$ 时，强度 0.19、1.88、18.75 随赌注线性增长；饱和 $u=1-e^{-\Omega}$ 时，强度 0.12、0.19、0.19。Math 的 r8：$\theta=-1,0,1,2.5$ 时强度都线性于赌注。
- **散文。** "growth is not the danger; the mind is"改为：
> "Growth that meets satiable needs has a point of enough; objectives that are not satiated have none."
- **按 Codex 改。** "growth directed at need … meets E3 by itself"改为：
> "Deliberately bounded hazardous scope, with correction that keeps growing, is a sufficient route (part 1); its connection to purpose is a design hypothesis."
- **补一句。** 与命题 2.6 相连：
> "$\Gamma$ also prices standing, so the actors who would need a point of enough are pushed away from it by the loop."

### 11.2 命题 5.10(3) 的分母

> 3. *A promise made before the win to give a fraction $\beta$ of a prize $\Omega$ to the $n-1$ others is worth breaking by $\beta\Omega(n-1-\theta)/(n-1)$; if the fraction is instead divided equally among all $n$, the winner included, by $\beta\Omega(n-1-\theta)/n$ (Proposition 3.5(5)).*

核对：`s8` (1)，$\theta=-1,0,1,2$ 时两种情形都与公式一致。

### 11.3 命题 3.11(2)：集团的 $s\ell$

> 2. *If the contestants form $k$ blocs of equal size $s=n/k$, each inclusive internally and acting as one actor, the game among blocs is the original game with $n=k$ and shared loss $s\ell$ per unit of intensity. Every result about the race then holds at the level of blocs. With blocs of unequal size and $r\ne1$, a bloc's strength also depends on its size (with equal total effort, a bloc of three weighs $3^{1-r}$ times a single contestant), and the bloc game is a contest with asymmetric strengths.*

核对：`s8` (2)，(k, s) = (2,2)、(3,2)、(2,3) 时集团强度为 0.1563、0.1389、0.1316，与"$n=k$，$s\ell$"的公式一致，而不是 0.1923 或 0.1709。

### 11.4 $\theta$ 的识别，被感知份额 $\psi$ 混淆

> **Measuring the weight.** *… The ratio of responses identifies $(1+\theta)\psi/(n-1-\theta)$, where $\psi$ is the share of the shared loss that actors perceive: $R=n(1+\theta)\psi/(n-1-\theta)$. If only half is perceived, a true $\theta=0$ reads as $-0.43$ [N]. Separating $\theta$ from $\psi$ needs a third perturbation that changes the visibility of shared harm without changing its size (disclosure), or an independent measure of perceived harm; it also needs a common $\theta$. The identification fails exactly where the theory says shared harm goes unseen.*

核对：`s8` (3)，有限差分求得的比值与公式一致，$\theta=0,0.4,1$，$\psi=1,0.5$。

### 11.5 引理 7.11：耦合

> **Lemma 7.11 (When an arrangement cannot do worse) [T].** *Let both paths be driven by the same exogenous world process, and let the irreversible event on each path occur at date $t$ when a common uniform draw $U_t$ falls below that path's conditional hazard. Assume, at every date and on every history of the joint process on which both paths have survived:*
> - *(F1) once $A$ has dissolved, $A$'s hazard is no higher than $C$'s;*
> - *(F2) while $A$ lasts, $A$'s hazard, its own hazards included, is no higher than $C$'s.*
>
> *Then $S^A(H)\ge S^C(H)$ at every horizon, whatever the rule, possibly endogenous, by which $A$ dissolves.*

- **证明。** 在每条共同存活的历史上，$\{A\text{ 于 }t\text{ 发生}\}\subseteq\{C\text{ 于 }t\text{ 发生}\}$，所以按路径有 $S^C_H\subseteq S^A_H$。
- **删去原证明中的一步。** "$S^A(H\mid\tau)\ge S^C(H)$ for every $\tau$"在解体依赖状态时不成立：Math 的例子为 1/5 对 3/5；`s8` (4) 为 0.291 对 0.324。
- **特例。** 若 $C$ 的危险是确定的时间表，F1、F2 只需在 $A$ 的历史上陈述。
- **核对。** `s8` (4)：两状态马尔可夫世界，解体是内生的（坏状态更可能解体），动态规划精确计算。$H=10,30,100$ 时 $S^A\ge S^C$，条件化的那一步则失败。

### 11.6 命题 6.1(5)：成本指数

> 5. *Suppose [A] that $b$, $d$ and $c$ scale with effectiveness as $\epsilon^{\beta_b}$, $\epsilon^{\beta_d}$ and $\epsilon^{\beta_c}$, so that prize, harm and cost grow with exponents $1+\beta_b$, $1+\beta_d$ and $\beta_c$.*
>    - *If $\beta_c<1+\max(\beta_b,\beta_d)$, cost drops out of the limit: $\theta^\ast\to(b-d)/(b/(n-1)+d)$ when $\beta_b=\beta_d$; $\theta^\ast\to n-1$ when $\beta_b>\beta_d$; $\theta^\ast\to-1$ when $\beta_d>\beta_b$.*
>    - *If $\beta_c>1+\max(\beta_b,\beta_d)$, $\theta^\ast\to-\infty$: cost alone deters racing for every self-model.*
>    - *At equality, cost enters the limit.*

- **核对（`s8` (5)）。**
  - (0,0,0) → 1.50；(1,1,0) → 1.50；(0,0.5,0) → −0.99；(0.5,0,0) → 2.998。
  - (1,0,3) 与 (0,0,1.5) → $-\infty$。
  - 等号情形：(0,0,1) → 0.9375 $=(b-d-c)/(b/3+d)$；(1,0,2) → 2.1 $=3(b-c)/b$。
- **随后的数值。** "with all three scaling alike, 1.44"改为：
> "with $b$, $d$ and $c$ fixed it is $1.44$ at $\epsilon=10$; with $c$ also scaling with $\epsilon$ it stays $0.94$"
  （Ali 次要 1。）
- **原条件的问题。** 原文的"$\beta_c<\beta_b=\beta_d$"既不必要也不充分；正确条件是 $\beta_c<1+\beta_b$。

### 11.7 命题 6.4(2)："一个或两个"

> *… Both, or exactly one, can hold, depending on $s$; at least one always holds, because $A(n+(n-1)s)/n-An(1+s)/(n+s)=A(n-1)s^2/[n(n+s)]\ge0$.*

核对：`s8` (6)，十万次抽样，"两者都不成立"为 0 例，"两者都成立"为 4,068 例。

### 11.8 命题 6.9 与错误独立

替换第 1368 行：

> *Full row sums below one certify that no party controls the checks' funding, appointment or access (Proposition 4.8(2)). They do not certify that the checks' errors are independent. A shared source of error in training data, models or method defeats checks with no institutional conversion at all: six checks of reliability $0.9$ with a blind spot common to all, covering a share $\rho$ of hazards, catch $(1-\rho)(1-0.1^6)$ [N]. The ceiling must be measured directly, by the correlation of misses on a common test set (Knight and Leveson 1986). The row-sum certificate is necessary for independent correction, not sufficient.*

核对：`s8` (7)，$\rho=0,0.05,0.3$ 时捕获率为 1.000、0.950、0.700。

§6.6、Compact 的评估行、D7 同步改为"necessary, not sufficient"。

### 11.9 定义 8.10：判别核

> **Definition 8.10 (The correctable kernel) [D].** *The correctable kernel is the set of states of the world from which some non-anticipative strategy of admissible correction avoids O1 and O2 against every sequence of errors in the justified range. In viability theory this is a discriminating, or guaranteed-viability, kernel of a game against disturbances (Cardaliaguet 1996; Cardaliaguet, Quincampoix and Saint-Pierre 1999)†, not the viability kernel of undisturbed dynamics (Aubin 1991). Leaving the kernel is the loss of guaranteed correctability: from outside it, some foreseeable sequence of errors leads to O1 or O2 whatever admissible correction does. It is a point of no guaranteed return, earlier than the losses themselves.*

- "Leaving the kernel is what O1 and O2 name"一句删去。
- 第一个可计算的实例：11.10 中 Allee 宿主的 $\Delta_{\min}$。
- 文献标 †，须核对。

### 11.10 定理 8.2(1)：处处更苛刻的宿主（按系统 Opus 复核）

- **宿主的选择。** 用逐点更苛刻的 Allee 宿主，即每单位再生率
$$\rho_A(V/A-1)(1-V/K),\qquad\rho_A=\rho A/(K-A),$$
  它在每个 $V$ 处都不超过 $\rho(1-V/K)$，并在 $K$ 处与 logistic 相切。
- **评审选错了宿主。** 评审用的峰值归一化宿主，在 $V\gtrsim0.33$ 时比 logistic **更**宽容，所以不能用。

> 1. *Sufficiency. Under (I1)–(I4), $\tau_{\text{eff}}>\nu$ after a finite time and $E(t)\to e_{\min}$. On the logistic host (1), $\liminf_tV(t)\ge K(1-he_{\min}/\rho)>V_{\min}$, and the trajectory is viable if, in addition, the host stays above its floor while $E$ falls. On a host whose regeneration is no greater than (1) at every level and which degrades by itself below a threshold $V_u(E)$, sufficiency needs more. The transient must stay above $V_u(e_{\min})$, which requires a liability margin $\Delta=\tau_{\text{eff}}-\nu$ above a minimum $\Delta_{\min}$ set by the host, the initial composition and the speed of selection. The normative floor must also satisfy $V_{\min}\ge V_u(e_{\min})$ for crossing it to be the first loss.*

**[N]：**
- **logistic。** 从一开始就有责任 $\Delta=0.08$，竞赛策略占 99%：宿主下探到 **0.1397** 后恢复（`s9` (a)，两种步长）。这是第 1915 行"0.14"的独立复现。原数值只在 `v3/checks.log` 第 50 行，由 `checks_v31.py` 产生，附录 B 没有为这个结果列出它。
- **逐点更苛刻的 Allee 宿主**（$e_{\min}=0.1$，$x_0=0.99$）：

| $A$ | 0.05 | 0.10 | 0.15 | 0.20 | 0.25 |
|---|---|---|---|---|---|
| $\Delta_{\min}$ | 0.26 | 0.31 | 0.36 | 0.42 | 0.51 |
| $V_u(e_{\min})$ | 0.25 | 0.31 | 0.36 | 0.42 | 0.48 |

  $A\ge0.10$ 时，$V_u$ 高于 $V_{\min}=0.3$（`s9` (b)，复现 Opus 复核）。logistic 宿主在 $\Delta=0.02$ 时仍会恢复。

**§3.2 的句子改为：**

> "The crossing results (Proposition 3.4(3), Theorem 4.11) hold a fortiori for hosts whose regeneration is lower at every level. The sufficiency of Theorem 8.2(1) does not: it needs the margin condition stated there [N]. A host normalized to the same peak regeneration is not harsher in this sense; it regenerates faster above about a third of capacity."

### 11.11 驻留时间（按系统 Opus 复核的精确值）

替换第 814 行"at least of the order of $1/(\varepsilon d)$"，并改写 §9.4 Dwell times：

> *In the field model the dwell time of a reform that insulates rule-making is at least $\ln R/(\varepsilon d)$, the time rule support needs to fall below break-even, plus the time to repay the lock-in accumulated meanwhile. With rule-making ten times slower than adoption ($\varepsilon/\zeta=0.1$), $T_{\min}\varepsilon d$ is $1.89$, $5.32$ and $10.45$ for $R=2$, $5$ and $10$; with the two equally fast it is $5.86$, $10.34$ and $16.18$ [N].*
>
> *During the first $\ln R/(\varepsilon d)$ the share keeps rising. It is back at its starting level when $R(1-e^{-s})=s$, $s=\varepsilon dt$, which gives $s=1.59$, $4.97$ and $10.0$, well before withdrawal is safe. Share levels fall before withdrawal is safe, so a rollback judged on levels would be premature; what decides is where rule support stands relative to the separatrix.*
>
> *Keeping a small alternative lineage shortens the dwell. For the pause of Proposition 4.10 with rule-making insulated, the dwell is exactly $\ln\big((b/d)/S(x_p)\big)/(\varepsilon d)$, with $S$ the separatrix height, and infinite when $x_p\ge\sigma(0)$.*

命题 4.10 的数值句改为：

> "When rule support adapts as fast as shares ($\varepsilon=\zeta$, $R=2$), an insulated pause never undoes capture from a frozen share of $\sigma(0)=0.68$ or more; $\sigma(0)$ rises to $0.98$ when rule-making is ten times slower [N]."

**核对。**
- `s10` 用前向积分（logit 坐标，不截断 $x$，不用分界线），全部复现 Opus 复核的值：1.886、5.318、10.453；5.859、10.343、16.181；$s^\ast$ 为 1.594、4.965、10.000；$\sigma(0)$ 为 0.676、0.984、0.321、0.775、0.516。
- "0.1% 替代谱系使 10.45 降到 3.81"这一数值来自 Opus 复核（c1），我未独立复现，写进正文前须进 `checks_v61`。
- 每个阶段的慢变量（阶段 2 是 $\mathcal K$，即引理 6.3 的 $1/\beta_c$；阶段 4 是悬置的能力）按系统评审补入 §9.4。

### 11.12 注释 4.7(4)：自相关的 [N, systems review]

- **核对。** `s11`：随机 logistic 宿主，$E=0.4$，真值 $V^\ast=0.36$。静态掩蔽 $m=0,0.25,0.5$ 下，报告均值为 0.358、0.519、0.679，而滞后一期自相关**完全相同**（0.9814）：仿射变换保持相关系数。由此恢复的状况为 0.376，有限样本偏差；系统评审为 0.373。
- **加一个反例。** 带记忆的报告滤波（指数平滑 0.8）使恢复值降到 0.042，指标失效，与正文所列的局限一致。
- **措辞。** 标注改为 [N]，引 `checks_v61` 的 AC 块。"to first order"可以删去：对静态、无记忆、仿射的掩蔽，这是精确的。

### 11.13 命题 4.10 与 09-28 论文的重叠（只标出）

命题 4.10 就是 09-28 论文的 Prop. 10，那篇的摘要里几乎有同一句话（X-G2）。V6.1 要在 §2.9 或附录 F 写明来源，归属待作者定。

---

## 十二、检查设计

### 12.1 原则
1. **不用不等式验证不等式。** 凡是"条件当且仅当"的结果，都用直接计算（值迭代、蒙特卡洛、数值最优反应、份额模拟、数值雅可比）判定结果，再与条件比较。DF 块的做法（用待证不等式定义"可维持"）一律废止。
2. **每个范围边界至少一个会失败的检验。** 例如 $D\ne C$、$n\ge3$、非等额负担、$f>0$、逐点更苛刻的宿主。
3. **恒等式块单独标注。** TC、TH 这类恒等式检查保留，但在日志里标"identity"，正文不称"与直接计算一致"。
4. **正文每个 [N] 指向一个块。** 不指向临时目录。
5. **只用纯 Python 标准库。** 本机没有 numpy。约 1–2 分钟内跑完。

### 12.2 新块（`checks_v61.py`，可直接以 `v61-math/s*.py` 为底稿）

| 块 | 对象 | 独立检验的做法 | 预期 / 已得结果 |
|---|---|---|---|
| **EC** | 命题 5.7(1)–(4) | 显式马尔可夫链（合作、惩罚、两个决定性吸收态）值迭代；随机抽 20 万组，$D<C$、$=C$、$>C$ 各三分之一；蒙特卡洛交叉验证；Codex 的两个反例；$p_d=1$ 阈值两侧 | 0 例不符；旧界按 S1b 的方向失败（`s1`） |
| **PB** | 命题 5.7(5)（惩罚中的突破） | 同一个马尔可夫链，改变 $q$；$D+U$ 大于和小于 $2P$ 两种情形 | $v$ 的闭式吻合；$D=4,U=0,q=0.1$ 时在 $p_d=0$ 下不可维持（`s1` S1f/g） |
| **CR** | 推论 5.8 的范围 | (a) $n=2$ 随机反对称矩阵，混合模仿；(b) $n\ge3$ 匿名博弈，同策略惩罚；(c) 三人少数派博弈：检验惩罚组合是阶段纳什均衡，直接计算贴现值 | $\le2\times10^{-16}$；0/3000；$\delta^\ast=0.706$（`s2`） |
| **LG** | 命题 2.6(1) | 随机多通道系统，数值雅可比、谱半径对 $\Gamma$；非线性模拟偏差的增长与衰减；包括 $r<1$ 而反身通道使 $\Gamma>1$ 的情形 | 0/4000（`s3` A、A′） |
| **PS** | 命题 2.6(2)(3) | 非线性模型扰动后算现值，对 $\Gamma_\delta/(1-\Gamma_\delta)$；两期竞赛直接求均衡，对 $e(\theta_\Gamma)$，含 $\theta_0\ne0$ | 相对误差 $<2\times10^{-6}$；六位一致（`s3` B、C、C′） |
| **T3** | 命题 5.14(2) | 恒等式；数值求理想点之差；直接构造两消息分割均衡（数值最优反应、二分边界类型） | $b_0n/(n-2)$；存在当且仅当 $<1/4$（`s4`） |
| **CI** | 引理 3.3(2)(3)；命题 6.7 的 $A_\tau$ | 复制者模拟：非等额负担、规避、依赖守约的执行（倾覆点）、共同责任制、单方保障的负净成本 | `s5` |
| **PR** | 引理 3.10 | 五种划分的 Price 分解（全局与本群收益）；有偏传递的稳定点；可逆与不可逆失败的蒙特卡洛 | 全局收益下群间项 ≤ 0（`s6`） |
| **CS4** | 第 4 节成本结构 | 数值最大化求 $q^\ast$（导数二分，不用闭式）；阈值、矩、拆分因子、速率律（三种 $\xi_v$）、拆分延迟（模拟越过时刻）、$f$ 固定或下降 | `s7` |
| **QS** | 第 4 节准静态假设 | **待做：** 载体的 $q$ 按复制者选择演化，与场模型 (3) 联合积分；检验速率律在非准静态下是否保持。失败的标志是：$\alpha$ 略大于 $g/(1+\eta)$ 而证书仍失败 | 尚未运行 |
| **SM** | 11.1–11.8 | `s8` 的 (1)–(10) | 全部按上文 |
| **HO** | 定理 8.2(1)；R1 | logistic 宿主暂态 0.1397；逐点更苛刻的 Allee 宿主的 $\Delta_{\min}$ 与 $V_u$；R1 有限期限反例 | `s9` |
| **DW** | 命题 4.10、§9.4 | logit 坐标前向积分，二分求 $T_{\min}$；两相时刻；$\sigma(0)$；**补**：替代谱系下限、本文暂停设计的精确驻留时间 | `s10`（后两项待补） |
| **AC** | 注释 4.7(4) | 随机宿主，三种静态掩蔽对比带记忆的滤波 | `s11` |
| **FA** | R3b | Codex 的不变矩形，$R=2$，低初值 | 并入 Codex 脚本 |
| **N12** | 第一节、§2.2 引用的派生数字 | `s12`（标为派生量，底层公式由上述各块检验） | |

### 12.3 现有 [N] 中缺脚本或只是恒等式的
- **在 v6 的套件中缺脚本：**
  - **定理 8.2 的 0.14：** 只在 `v3/checks.log` 第 50 行（`checks_v31.py`），附录 B 没有为此列出；已由 `s9` 独立复现为 0.1397。
  - **命题 4.10 的 [N, systems review]：** 只在系统评审的临时目录；已由 `s10` 复现，并更正为 $\sigma(0)=0.68$。
  - **注释 4.7(4) 的 [N, systems review]：** 只在临时目录；已由 `s11` 复现。
  - **0.1% 替代谱系的 3.81：** 系统复核提出，进正文前须进 DW 块。
- **只是恒等式或公式求值、不构成独立检验的：**
  - **DF：** 21,096 例，用待证不等式定义"可维持"（Codex）。
  - **DF 的 1,260 例对称检查：** 只验证"对称组合给 0"这一平凡事实，没有检验惩罚。
  - **v5 中 4.4(7) 的"23.03"：** 公式求值；`s7` 用模拟得 23.00，可替代。
  - **UC：** 只测了等额负担。
  - **TK：** 只测两方零和。
  - **RI 的上限检查：** 只从近乎相等的起点出发，即只检验局部。
  - **TH：** 在模型内按构造精确，并假定 $\psi=1$。
- 这些块保留时须改标签，或按 12.2 替换。

### 12.4 家族外复核
上述修复完成后，交 Codex 复核时请它重点攻击三处：
- 命题 2.6(2)(3) 在完整随机博弈中的表述（状态影响他人策略时，一阶结论是否仍然成立）；
- 推论 5.8(3) 的反例是否依赖弱均衡；
- 第 4 节的准静态假设（QS 块）。

---

## 十三、记号表（V6.1 统一）

| 记号 | V6.1 含义 | 原冲突 | 处理 |
|---|---|---|---|
| $\chi$ | 只作可占有性（§4） | 定义 2.1、注释 5.3 中作"留给赢家的份额"；8.6(3) 中作"可再投入份额" | 后两处改用 $1-\beta$ 与 $\kappa_c$ |
| $\beta$ | 均分的份额 | §4.4 的 $\beta_{\text{in/out}}$；6.1(5) 的 $\beta_b$ 等；CS 的 $\beta_s$ | 靠下标区分 |
| $\kappa_c$；$\kappa_j$ | 赢得物转入能力（或存量 $j$）的份额 | §3.6 的耦合 $\kappa$ | 保留下标；也可改用 $\xi_c$ |
| $k_0$（$K_0=k_0/d_K$） | 不靠赢得的流入 | — | 新增 |
| $d_K$；$d_j$ | 折旧 | 注释 5.3 的 $\delta$ | $\delta$ 只作贴现 |
| $\mu,d$ | 注释 2.3 的阻尼 | 原为 $\mu,\delta$ | $\delta$ 改为 $d$ |
| $\delta_f$ | 扩散 | 注释 5.3 中有一句未定义的用法 | 沿用注释 7.1 |
| $\Gamma,\Gamma_\delta$ | 环路增益；贴现环路增益 | 命题 5.13 的 $\Gamma=Y_\tau/U(\tau)$，以及 $\Gamma_X$ | 5.13 中改为 $\varrho_Y$ 或保持局部 |
| $\omega_j$ | 存量 $j$ 中来自赢得的份额 | §3.5 的 $G(V)=\omega V$（局部） | 可接受 |
| $\theta_\Gamma$ | 环路诱导的工作自我模型 | 命题 8.6(1) 的 $\theta_{\text{eff}}$（汇集） | 二者可以复合：先汇集，再复利 |
| $C_i,D_i,v_i,g_i,p_d,\bar p_d$ | 执行条件中的各量 | $D$：域的数目、5.2 的耗散 $D(\theta)$、注释 5.9 的缩写；$C(q)$ 是成本函数 | 注释 5.9 的缩写改为 $\Lambda$；其余靠局部性 |
| $\xi_v,\xi_f$ | 影响成本的规模弹性 | — | 新增 |
| $[H_\gamma],[H_f]$ | AI 降低控制成本（可变部分、固定部分） | 原为隐含前提 | 明标 [A] |
| $A_\tau$ | 对齐税前提 | — | 新增 |
| $\psi$ | 被感知的共同损失份额 | 命题 6.2 的 $\psi_0,\psi_1$ | 靠下标区分 |
| $\sigma_i$ | 命题 2.6 中的对数强度 | 命题 4.10 的 $\sigma(0)$ | 两处都是局部的 |

A.0 的"Symbols are local"一句保留，但须删去 8.6(3) 跨节引用 $\chi$ 的写法。

---

## 十四、随之要改的段落（传播清单）

- **中文概要。**
  - 第 1 条：改为"一组相互联系的条件"，并加"它们合成一个环路增益"。
  - 第 3 条：引理 3.3 改为"等额、可执行"；引理 3.10 改为"全局收益在任何层级都不被选择"。
  - 第 4 条：AI 降低控制成本标为前提。
  - 第 5 条：执行条件、$p_d$ 与 $\bar p_d$；两难改写；语言的两面。
  - 第 6 条：$A_\tau$；"单个实验室内部去不掉"收窄为"共同成本的部分"。
  - 第 7 条：R1–R8 分三表。
  - 第 8 条：分享与"树"（$k_0$）；"只有改变赢能换来什么才打开回路"改为三杠杆的新总结。
- **§0。** 首段改为对抗复核建议的弱、强两层（不是本文件的范围，但与 5.16 相连）。
- **§1.2。**
  - 第 1 条改为 Definition 2.1 的新表述。
  - 第 3 条去掉"which is why coordination works"的无条件读法。
  - 第 5 条最后一句改为 5.16 的新散文。
  - 第 6 条加 $A_\tau$。
- **§1.5 的"claims five things"。** 第 1 条"signatures of one selection pressure"改为"products of interconnected conditions that combine into one loop gain at their core"。
- **§2.1、§2.3–2.5。**
  - 定义 2.1 替换。
  - 机制表中"Compounding and conversion"的锚点改为命题 2.6、5.3。
  - §2.3"Decisiveness is the limit of compounding"改为"Decisiveness is reached faster where the loop gain is larger (Proposition 2.6); whether a position beyond sanction exists is a separate condition"。
  - T1 一行中"even actors without relative objectives lose enforced restraint"加"and, where the loop gain is large, come to act on relative objectives (Proposition 2.6)"。
- **§2.7。** 单因子预测降为 [C]（已定）。加 T-Γ。
- **§2.9 的"新增"清单。**
  - 第 3 条改为"the enforcement condition and its two blades"。
  - 第 5 条移入"吸收"。
  - 第 7 条改为"where integration must be anticipatory: global benefits and irreversible failures"。
  - 新增"one loop gain and the price of standing"。
- **§3.3、§3.7、§3.8、§3.11。** 按第五、六、十一节。
- **§4。** 假设框 4.0；命题 4.2(2)、4.4(1)(3)(5)(7)(8)；命题 4.10 的数值；§4.7 的"Mechanism"中速率律加 [A]。
- **§5。**
  - 注释 5.3 改为命题 5.3；命题 5.7、推论 5.8、注释 5.9（$\Lambda$）。
  - 命题 5.10(3)；命题 5.14。
  - §5.5 的剪刀差与定理 5.15、5.16。
  - §5.6 表的前三行与"does not establish"清单：加"that relative actors cannot enforce anything (Corollary 5.8(3))"。
- **§6。** 命题 6.1(5) 及随后的数值；命题 6.4(2)；命题 6.7 及三条推论；命题 6.9 末段；§6.6 外层第 1 条（"invisible … and so survive it"改为"survive when incidence is equal and evasion is sanctioned"）。
- **§7。** 命题 7.10 三表；§7.11 的登记条件；T-G 的符号。
- **§8。**
  - 定义 8.1(a) 改为"coverage … with equal incidence and sanctions above the gain from evasion (Lemma 3.3(3))"。
  - 定理 8.2(1)；命题 8.3 散文"invisible to selection"同改。
  - 命题 8.6(3) 与三杠杆总结。
  - §8.2 第二股的条件。
  - 定义 8.10、命题 8.11(3)。
  - §8.6 表第一行的依据（Lemma 3.3(2)(3)）。
- **§9.4。** 驻留时间。
- **§10.2。**
  - 第 5 条（嵌套回路）、第 8 条（预见）按新陈述改。
  - "参数层面的干预会被重新吸收"按系统评审 F5.1 改。不在本文件范围，但与 4.9(2) 相连。
- **附录 A。** 按以上各节的证明纲要重写对应证明。新增命题 2.6 与 5.3 的证明。
- **附录 B。** 换为 `checks_v61` 的块表（12.2），注明 12.3 的旧块已替换或改了标签。
- **附录 G。** 登记本文件的反例：
  - $D<C$ 时 $p_d=1$ 仍可合作；
  - $n=3$ 下角色分化的惩罚；
  - $n=3$ 下的信息性谈话；
  - 非等额负担；
  - 一个宿主内部的传递项；
  - 有限期限的 R1；
  - $R=2$ 的低初值；
  - 上限的排除盆；
  - $\xi_v=1$ 时度量是 HHI；
  - 峰值归一化的宿主并不更苛刻。
- **CLAIMS.md。** 各条目的类型：
  - 命题 2.6 为 [T]；
  - 剪刀差为 [T∣A]；
  - 定理 5.16 为 [T∣A]；
  - 命题 7.10 为 [T∣A]（表 A）、[T]（表 B）、[V]（表 C）；
  - 第 4 节的 $[H_\gamma]$、$[H_f]$ 为 [A]。

---

## 附：脚本与关键输出

全部在 `/private/tmp/claude-501/-Users-ren-theories/125c36f5-6a17-4570-bcbc-ade65a8a973f/scratchpad/v61-math/`，日志同名 `.log`。纯 Python 3.11，每个脚本在 1–20 秒内跑完。

| 脚本 | 内容 | 关键输出 |
|---|---|---|
| `s1_enforcement.py` | 执行条件、旧界、蒙特卡洛、Codex 反例、$p_d\to1$、惩罚中的突破 | 0/200,000 不符；S1b 表；$v$ 的闭式 |
| `s2_cor58_scope.py` | 推论 5.8 的范围 | $n=2$ 混合模仿；$n=3$ 反例，$\delta^\ast=0.706$ |
| `s3_loopgain.py` | 命题 2.6 | 0/4000；PV 误差 $1.7\times10^{-6}$；两期竞赛六位一致 |
| `s4_talk.py` | 命题 5.14(2) | $b_0n/(n-2)$；分割均衡当且仅当 $<1/4$ |
| `s5_constraint.py` | 引理 3.3(2)(3)、$A_\tau$ | 倾覆点 0.375；责任制翻转；负净成本的保障被选择 |
| `s6_price.py` | 引理 3.10 | 全局收益下群间项 ≤ 0（五种划分）；$\mu/c$ |
| `s7_cost.py` | 第 4 节成本结构 | 阈值、矩、拆分、速率律（三种 $\xi_v$）、$f$ 的两种情形 |
| `s8_small.py` | 11.1–11.8、上限、增长变体 | 见各节 |
| `s9_host.py` | 定理 8.2(1)、Allee、R1 | 0.1397；$\Delta_{\min}$ 0.26–0.51；$V(50)\ge0.435$ |
| `s10_dwell.py` | 驻留时间、$\sigma(0)$ | 复现 Opus 复核全部值 |
| `s11_autocorr.py` | 注释 4.7(4) | 自相关在三种静态掩蔽下相同；带记忆的滤波使之失效 |
| `s12_numbers.py` | 派生数字（第一节、二节） | $\theta_\Gamma$ 表；$\Gamma^\ast(p_d)$；$\bar p_d$；$T_{\text{dec}}$ |
