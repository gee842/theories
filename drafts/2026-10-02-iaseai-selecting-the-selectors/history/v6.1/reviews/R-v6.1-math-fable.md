# V6.1 数学评审（Fable）

2026-10-04。对象：`v6.1/THEORY.md`（sha256 前缀 242a61240d810e51）与 `SUPPLEMENT.md`，对照 `../v6/v61-planning/Q2-math-repairs.md`、`../v6/reviews/R-v6.0-math.md`、`REVIEW-v6-codex.md`。视角：博弈论、动力系统、产业组织。脚本（纯 Python 标准库）在 `/private/tmp/claude-501/-Users-ren-theories/125c36f5-6a17-4570-bcbc-ade65a8a973f/scratchpad/review61/math-fable/`，`m1`–`m6`，日志同名 `.log`。`checks_v61.py` 复跑一次，输出与 `checks_v61.log` 除耗时外逐字一致（`checks_v61.rerun.log`）。

**家族偏差声明。** 评审者与起草者同属一个模型家族。偏差最可能落在三处：(i) 我在论文自己的建模原语（Tullock 竞赛、收益单调选择、对称均衡、平等地位处的线性化）之内攻击，没有质疑原语本身；家族外的博弈论者可能首先质疑"所有存量由同一个赢得物喂养"（秩一结构）或"收益单调选择"是否适合企业与国家。(ii) 手工复推可能与起草者共享同一种代数习惯，所以每条优先结果我都另用不含待检公式的数值方法核过。(iii) 严重程度的判断是共同口味最可能起作用的地方。

## 1. 总判断

V6.1 的形式核心在各自的模型内是对的：环路增益、复利条件、执行条件、相对惩罚的两种情形、第 4 节的全部指数、回退耦合引理，我都独立复推并用自己的数值方法核过，没有发现一条优先结果在其所述模型内为假。问题集中在**陈述超出模型**与**前提缺漏**两类：最重要的一条是"同一个增益给地位定价"只在纯存量复利模型里精确，一旦对手的未来努力随地位调整，地位的价格就乘上一个 O(1) 的策略因子（Tullock 加努力时恰为 $2(n-1)/n$），$\Gamma_\delta$ 本身不再定价；其次是引理 3.3(3) 的双稳结论少了一条前提，定理 4.12 的 (b)(c) 两条前提在证明里没有用到，准静态假设是证书的最坏情形而 R3a 的"必要"没有写明依赖它。推论 5.5 的反例是弱均衡，但存在严格变体，反例本身站得住。没有致命项。`checks_v61.py` 大体名实相符，RH 块例外；CS 块只测了 $\eta=1$，LG 块只测了两个存量，我已补测。

## 2. 发现

### 致命

无。

### 重要

**I1　命题 2.2(3)、命题 3.9、§2 主张框、§1.2 第 1 条："同一个增益给地位定价"超出了模型。**
- 位置：THEORY 命题 2.2(3)、命题 3.9 及其 Scope；§2 主张框"the same number prices standing for every actor"；SUPPLEMENT S13 "Loop gain and working objectives"一行。
- 问题：$\lambda=\Gamma_\delta/(1-\Gamma_\delta)$ 是在"赢得物只由存量决定、再投入是机械的、他人策略固定"的模型里推出的。只要未来的赢得物还取决于对手当期选择的努力，地位的一阶价格就是 $\lambda_{\rm full}=\delta\kappa\frac{n}{n-1}\,dV_i/dK_i$，其中 $dV_i/dK_i$ 含对手努力对 $K_i$ 的反应项。目标 $\pi_i+\lambda(\pi_i-\bar\pi)$ 的**结构**保留（我验证了 $V_i$ 对能力零次齐次，所以只剩相对部分），但 $\lambda$ 不再是 $\Gamma_\delta$ 的函数。
- 证据（`m2`）：两期博弈，第二期为 Tullock 竞赛、强度 $K_i^{r_2}f_i$、努力 $f_i$ 内生。直接求得的对称子博弈完美均衡强度 $e^\ast$ 与 $e(\theta(\lambda_{\rm full}))$ 六位一致，与 $e(\theta(\lambda_{\rm red}))$ 不一致；解析上 $\lambda_{\rm full}/\lambda_{\rm red}=2(n-1)/n$，数值为 1.0000、1.3333、1.5000、1.6667（$n=2,3,4,6$），对 $r_2$、$\Omega_2$、$\delta$、$\kappa$ 的变化不变。此处策略项为正（对手被更强的对手劝退，努力下降），简化式**低估**地位的价格；换一种第二期技术符号可以反过来。LG(C) 六位吻合只因为那个模型第二期没有努力。
- 修法：命题 2.2(3) 写成"在本模型中精确"；命题 3.9 的 Scope 加一句"若未来赢得物还取决于对手的努力，$\lambda$ 乘以一个策略因子，在加努力的 Tullock 竞赛中为 $2(n-1)/n$，其符号取决于对手是被劝退还是被激励"；主张框与 §1.2 的"prices standing for every actor"改为"prices standing in the compounding model"；S13 该行记下因子；§5.5 剪刀差的 [num] 已标 reduced form，保留。

**I2　引理 3.3(3) 末句：双稳结论缺前提，按字面为假。**
- 位置：THEORY 引理 3.3(3)："If the sanction weakens as evaders spread … compliance and evasion are both stable, separated by a tipping share"；SUPPLEMENT S3 证明；命题 6.7(3)、R8 继承。
- 问题：双稳需要 $s(0)>c_k>s(1)$。制裁随规避者增多而下降但始终高于成本，则守约全局稳定；起点就低于成本，则规避全局稳定。证明里"$s(x)=c$ 的根 $x^\dagger$"默认了根存在于 $(0,1)$。
- 证据（`m6`(1)）：$c=0.3$，$s(x)=0.5+0.5(1-x)\ge0.5$，从规避者份额 0.95 出发回到全体守约，无倾覆点；$s(x)=0.24(1-x)$，从 0.05 出发走向全体规避。$q_0F=0.48$ 与 $1.2$ 两例才双稳，倾覆点 0.375、0.750 与公式一致。
- 修法：加前提"provided the expected sanction exceeds the cost at full compliance and falls below it at full evasion"。

**I3　定理 4.12：前提 (b)(c) 在证明中闲置，定理实为命题 3.4 加命题 4.7 的推论。**
- 位置：THEORY 定理 4.12 及 Scope；SUPPLEMENT S4 证明。
- 问题：(e) 直接假定在 $[V_{\min},V_{\rm alarm}]$ 带内 $x_{\rm ev}(t)>(m_{\rm fl}-m_{\rm out})/(m_{\rm in}-m_{\rm out})$，这恰等价于 $m(t)>m_{\rm fl}$；于是结论只用 (a)（宿主在无警报时下行）、(d)、(e) 与命题 4.7。(b)(c) 推出的 $x_{\rm ev}\to1$ 不进入任何一步。"慢路径"的机制（控制成本下降 → 速率律 → 评估被俘获）因此是动机，不是证明。Scope 已承认 (e) 是"要核查的条件"，但定理的陈述仍把 (b)(c) 列为前提。
- 证据：S4 证明原文三句，第二句（"By (c) … $x_{\rm ev}\to1$"）的结论未被第三句使用。另见 `m5`：即使选择很快，证书失效（$t\approx69$）到评估域被俘获（$x>1/2$，$t\approx119$–$123$）之间有约 50 期的滞后，所以 (c) 本身也到不了 (e)。
- 修法：二选一。或把定理写成以 (a)(d)(e) 为前提、[thm]，再在散文里说 (b)(c) 是让 (e) 成立的机制，并把"两个时钟"的比较列为 [prem]；或真正从 (b)(c) 加一个时钟比较前提推出 (e)，标 [thm∣prem]。

**I4　准静态假设（假设 4.2；命题 4.5(2)；R3a；定理 10.5 的 (I2)）：是证书的最坏情形，R3a 的"必要"依赖它却未写明。**
- 位置：THEORY 假设 4.2 末句；命题 4.5 Scope；命题 9.1 表 R3a 行（模型列无"准静态"，例外列无"能力选择慢"）；SUPPLEMENT S13 "Capacity and the field"。
- 问题与证据（`m5`）：把能力 $q$ 的选择写成乘性方差的梯度动态 $\dot q=s_q q^2\,\partial_q\Delta\pi$，与场模型 $\dot z$、$\dot x$ 联合积分，$z$ 用精确指数更新。选择快（$s_q=100$）时，证书失效时刻与准静态完全一致（69.3 对 69.3；$\eta=2$ 时 69.1 对 69.1），门槛 $\alpha_{\rm ctl}/(1+\eta)$ 上下两侧的结局都与速率律一致；选择慢（$s_q\le0.1$）时 $q$ 落后于 $q^\ast$，速率律预言 $t\approx69$ 失效的证书在 250 期内始终成立。门槛速率不动，失效**时刻**与有限期限下的必要性动了。因为 $q\le q^\ast$（从 $q^\ast$ 以下出发），准静态给出最大的培育转换，是证书的最坏情形：对一条"要求"这是正确的方向，但 R3a 作为"必要条件"只在选择足够快时成立。
- 修法：R3a 行模型列加"capacity quasi-static (selection fast relative to the drift of $q^\ast$)"，例外列加"selection on capacity slower than that drift"；命题 4.5(2) 的 Scope 加"the failure time is a lower bound on the real one"；TESTS Study 2 可直接用 `m5` 的设计。

**I5　推论 5.5 的反例是弱纳什均衡，且相对惩罚者对"伤害谁"结构性无差异。**
- 位置：THEORY 推论 5.5 Scope（"such a punishment is a stage equilibrium"）；SUPPLEMENT S5；`checks_v61.py` CR(c)。
- 问题与证据（`m3`）：三人少数派博弈的惩罚组合 $[(A,X),(A,X),(A,Y)]$ 中，承担代价的惩罚者 1 在 $(A,X)$ 与 $(A,Y)$ 之间**恰好无差异**（目标都为 $-0.5$），而它一旦换到 $(A,Y)$，偏离者的目标从 $-0.5$ 跳到 $+1.0$，惩罚解除。这不是参数巧合：对一切 $a,b$ 偏离者在惩罚中都得 $-0.5$，惩罚者 1 都无差异。给 X 的唯一性奖励加 $+\varepsilon$ 使均衡严格，加 $-\varepsilon$ 则惩罚者 1 严格偏好放走偏离者，均衡消失。两名惩罚者都偏好 Y 角色（$+1.0$ 对 $-0.5$），角色分配是均衡选择问题。更一般地（`m3` 末段），$\theta=-1$ 的惩罚者在"伤害偏离者"与"伤害同伴惩罚者"之间精确无差异，所以纯相对行动者之间的角色分化惩罚至多是弱均衡，除非惩罚技术只能指向偏离者或收益有不对称。
- 修法：Scope 改为"such a punishment is a (weak) stage equilibrium; a small asymmetry in the positional prize makes it strict, and relative punishers are indifferent whom they hurt, so bloc enforcement needs role assignment"。反例的职能（为"相对行动者什么都执行不了"划界）不受影响；相反它加强了"结块需要协调"的读法。

### 次要

1. **命题 2.3(2)**："a cap $\bar K$ no higher than equal-standing capacity … locally stable"在 $\bar K=K^\ast$ 处不成立。此时 $\phi(K^\ast)=0$，$\phi'(K^\ast)=d_K[(1-\beta)r\omega_K(n-1)/n-1]$，为正时稍低于 $K^\ast$ 的落后者被排除。`m1`(C)：$n=5,r=1.5$，从 $0.97K^\ast$ 出发终值 0.000；$0.98K^\ast$ 的上限则全体回到上限。改"strictly below"。命题 2.3(1) 的"iff"在等号处同样未判定，命题 2.2 已正确避免，2.3 应一致。
2. **命题 5.4(1)**：陈述把"一次偏离"的 $g_i=\max_a$ 与单一 $p_d$ 并列，隐含 $p_d$ 对一切偏离相同。若不同偏离带不同的 $(g,p_d)$，最大 $g$ 的偏离未必是约束所在：`m6`(2)，$C=3,D=6,v=1,\delta=0.9$，偏离 A $(g=1,p_d=0.1)$ 满足 (14)，偏离 B $(g=0.2,p_d=0.6)$ 不满足。改为对每个偏离分别成立，或写明 $p_d$ 为所有偏离共有。这与"剪刀差"的读法有关：抬高 $p_d$ 的偏离（暗中加速）与抬高 $g$ 的偏离可以不同。
3. **命题 5.4(5)**："each … with probability $q$"而"neither with $1-2q$"排除了同时突破，且需 $q\le1/2$（`m6`(5)：$q=0.6$ 时 $1-2q<0$）。写明互斥与 $q\le1/2$。
4. **定理 5.12**：(variety grows) 在证明里闲置，结论只用 (coverage lags) 与 (residual floor)（`m6`(4)）。可保留为动机，但不应列在"Under …"里，或注明。
5. **注释 S2.1**：单通道特征值是 $1+(d_K+\delta_f)(\Gamma-1)$，不是 $1+d_K(\Gamma-1)$；S13 与 NB(d) 同。`m6`(3)：$d_K=0.05,\delta_f=0.05,\Gamma=3$ 时 1%→50% 需 21 期而非 41 期。$\delta_f=0$ 时无误。
6. **命题 4.5、§4.3**：$\hat Y$ 在 THEORY 与 S4 都未定义，而拆分论证"$\hat Y$ divided by $k^2$"要求 $\hat Y=p^2\bar y^\top\hat A\bar y$。按字面，$q^\ast=(\chi\hat Y/(\gamma p^{\xi_v}d))^{1/\eta}$ 与命题 4.3 的 $p^2$ 看似不符。补一句定义。
7. **标签**：定理 7.1 分支 I′ 的"can stabilize as nuclear deterrence did"是 [obs]，混在 [thm] 里；定理 8.11(3) 末句"that bound holds only if the verified coalition's advantage … grows at least as fast as diffusion erodes it"在 S8 没有推导，应标 [conj] 或 [prem]；定理 10.5(1) 关于更苛刻宿主的"needs a margin"由 HO 的数值支持而非证明，可标 [num]；命题 2.2(1)"the channels add"依赖所有存量由同一个赢得物喂养（秩一），若规则支持由单独选择的游说支出喂养则不相加，宜入 Scope。
8. **记号**（核心符号表声称全局唯一）：$U_i$ 在 5.4(5) 作被支配价值，与全局 $U$（覆盖）冲突；$q$ 在 5.4(5) 作突破概率，与 S0 的 $q$（转换能力）冲突；$d$ 在 6.1 作危害系数，与全局 $d$（纠正速率）冲突；$C(q;p)$（假设 4.2）与 $C_i$ 冲突；$\sigma$ 在定义 2.4 作规则、在命题 2.2 作强度，同在 §2；$s$ 在 3.11 作集团规模，与 S0 的 $s$（速度优势）冲突；$F$ 在定义 2.4、3.2 作映射，与 S0 的 $F$（制裁）冲突；$\varpi$ 在 S3 命题 3.7 作 $G(V)=\varpi V$，与全局 $\varpi$（信任）冲突；$\mu$ 在 S3、S14 作有偏传递率，与 S0 的 $\mu$（先验）冲突。$\delta$、$\kappa$、$J_i$、$\Phi$、$\mathcal M$、$\theta$、$\Gamma$ 一致（S2 证明里 $J$ 作雅可比、$\lambda$ 作特征值是局部用法）。另有三处重复词：THEORY 第 681 行"Proposition Proposition 9.2"、第 734 行"Theorem Theorem 10.5(3)"、CLAIMS 第 164 行"Assumption Assumption 4.2"。
9. **`checks_v61.py`**：RH 块标"independent"，但 `sym_eq` 每次迭代直接赋闭式 $e$，"h direct"与"formula"按构造相等，是恒等式；只有末行单组参数的网格最优反应是独立检验。CS 块全部 $\eta=1$（`m4` 已在 $\eta=0.5,2$、$\xi\in\{0,0.3,0.5,0.7,1\}$ 补测，全部吻合）。LG 块只测两个存量、$\sigma=r\ln K+raZ$（`m1` 在三存量、$\sigma=r_1\ln X^1+aX^2+b\sqrt{X^3}$ 下 0/2996 不符）。T3 的 $n=10,b_0=0.2$ 行偏差恰为 $1/4$，"exists iff bias<1/4: True"是浮点伪象，均衡确实不存在。EC 不检验惩罚的可信性，与命题 5.4(1)"对给定惩罚值"的措辞相符，不是缺陷。
10. **命题 9.1 R1 行**："long-run average"应写明取 $\limsup$（证明用"average at most $\nu-\epsilon$ beyond $T_0$"）。

## 3. 站得住、不应改动的部分

- **命题 2.2(1)(2) 与 S2 的秩一/Sherman–Morrison 证明。** 我按不同结构复核：三个存量、强度对各存量分别对数、线性、平方根进入，随机 2996 系统，Perron 根与 $\Gamma$ 判据 0 例不符；非线性模拟在 $\Gamma=0.983$ 衰减、$1.201$ 增长；三存量下地位价格的现值与 $\Gamma_\delta/(1-\Gamma_\delta)$ 最大相对误差 $7\times10^{-7}$。$\Gamma_\delta<\Gamma$ 的证明正确。
- **命题 2.3(1) 与全局上限条件 $\phi>0$ on $(0,\bar K)$。** 代数与 SM(9) 都对；"从每个起点恢复当且仅当"成立。
- **命题 5.4(1)–(5)。** 推导逐步复核；(2) 的四个单调性方向我由微分确认（对 $D$ 的单调性恰在 $\bar p_d\ge0$ 时成立，对 $v$ 恰在 $\bar p_d<1$ 时成立，与原文一致）；(5) 的闭式与"$D+U>2P$ 时 $v>P$"正确。EC 块是真正独立的检验，Q2 要求的"不用不等式验证不等式"已落实。
- **推论 5.5(1)(2)。** $n=2$ 反对称矩阵的混合模仿、$n\ge3$ 可交换组合，证明正确。
- **命题 5.15(2)。** 我手工解出两方理想点：$y_S-u=\frac{(n-1)b_0}{n-2}+\frac{K}{2(n-2)}$，$y_R-u=\frac{K-2b_0}{2(n-2)}$，差 $b_0n/(n-2)$，与第三方项 $K$ 无关；两者曲率相同（$(n-2)/(n-1)$），所以 Crawford–Sobel 的 $1/4$ 条件直接适用。
- **第 4 节。** 阈值指数 $1/(2-\xi_f)$、$q^\ast\sim p^{(2-\xi_v)/\eta}$、拆分因子、集中度矩、支出指数 $2+(2-\xi_v)/\eta$、速率律门槛与培育项增长率 $(\alpha_{\rm ctl}-(1+\eta)\alpha_{\rm cor})/\eta$，在 $\eta=0.5,1,2$ 全部与数值最优化一致；$\partial q^\ast/\partial\gamma<0$、$\partial q^\ast/\partial d<0$、$\partial q^\ast/\partial\chi>0$。"速率律不依赖规模弹性、阈值与矩依赖"的区分是对的。
- **引理 8.2。** 单调耦合证明正确，撤回按解体日期条件化的那一步也对（SM(4) 的 0.291 对 0.324）。
- **命题 10.3(1)(2)、定理 10.5(3)、命题 3.9 的代数。** 全部复核无误；10.3(1) 的 $\theta_{\rm eff}$ 系数我逐项展开确认。
- **结构。** [thm]/[thm∣prem]/[num]/[conj] 的区分比 v6.0 清楚得多；S14 反例表与各处 Scope 的坦白（完整随机博弈、准静态未做）是这版的优点，I1、I4 只是要求把已承认的局限写进相应结果的措辞与表格。

## 4. 核过与未核过

**核过（自己推导加自己脚本）**：命题 2.2 全部三条（`m1`、`m2`）；命题 2.3(1)(2)（`m1`）；引理 3.3(2)(3)（`m6`）；命题 3.9（手推加 `m2`）；引理 3.10（Price 分解手推）；假设 4.2 与命题 4.3、4.5 全部四条（`m4`、`m5`）；定理 4.12（逻辑）；命题 5.4(1)–(5)（手推加 `m6`）；推论 5.5（`m3`）；推论 5.6（逻辑）；定理 5.12（逻辑，`m6`）；命题 5.15(2)（手推）；定理 7.1、推论 7.3（逻辑）；引理 8.2（证明）；定理 8.11（逻辑）；命题 9.1 各行的依据；命题 10.3（手推）；定理 10.5(1)(3)（证明）；注释 S2.1（`m6`）；符号表（grep）；`checks_v61.py` 各块的独立性，并复跑全套。

**未核过**：命题 3.4–3.7、3.11、5.1–5.2、5.7–5.11、5.13–5.14、第 6 节各命题、命题 8.3、8.8、8.10、8.12、10.1–10.2、10.6–10.7、第 11 节各命题，只通读未复算；遗留套件（`--legacy`）未运行；参考文献、EVIDENCE、DISCUSSION 未审；完整随机博弈的马尔可夫完美均衡未求解，I1 只做了两期扩展；准静态的联合模拟只用了一种选择动态（乘性方差梯度），替代谱系对驻留时间的影响未碰。
