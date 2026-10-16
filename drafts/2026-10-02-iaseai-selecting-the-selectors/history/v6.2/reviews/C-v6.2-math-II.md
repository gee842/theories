# C-v6.2-math-II：对 R-v6.2-math-II 各项发现的对抗复核

脚本：`/private/tmp/claude-501/v62verify/confirm-math-II/`（`c01.py`、`c_misc.py`、`c11.py`、`c13.py`、`c13b.py`、`c14.py`，纯标准库）。结果：确认 11 项，部分成立 5 项，驳回 0 项。

- **M2-01｜部分成立**：问题属实，但范围和反例都要修正。命题 3.4 第二句、表 9.1 R1/R2 的模型列、命题 9.2(2) 只写了"payoff-monotone"，确实推不出 B→∞ ⟹ 份额→1。不过有三点要改。(a) "cumulative"并非没有定义：S3 引理 3.3(3) 的证明里写了"the log-ratio of two variants moves with the integral of their payoff gap as under replicator dynamics"。引理 3.3(3) 已写"cumulative payoff-monotone"，引理 6.5 和命题 6.7 第 2 层也已写"cumulative"，这几处不必改成别的词，只需把 S3 的这个定义移进定义 3.2 或 S0。引理 6.5 补"正下界的差距"和"在选择支撑内"；命题 6.7 的 (A_τ) 在正文补"by a positive margin"。(b) κ(t)=e^{-t} 依赖时间，不是定义 3.2 所写的 F(p,π) 形式。所谓"自治版" du/dt=Δπ(x*−x) 在 x>x* 时符号反转，并不 payoff-monotone。(c) 合法的自治反例：取 d/dt logit=(Δπ)^3，τ_eff=ν−1/(1+t)，则 B=ln(1+t)→∞。此时竞赛份额停在 0.00166，min V=0.997；同一 τ 下复制子动力学的 min V=0.017，越过下限（c01.py）。
- **M2-02｜确认**：核心斜体陈述是条件式，本身为真；但标题"not sufficient"，以及 §6.4、§9 的一般化说法，依赖两个只写在 S6 的前提：F≤F_max（以排除为上界），以及在固定审计接入下 p_det 随能力上升→0（C12）。在 S6 自己的数例里，p_det·F=0.35>0.3 就能清除变体，所以协调可以通过抬高 F 恢复约束。修法照原样采用。
- **M2-03｜确认**：checks 代码里的"exact"其实是 Σ[1−(1−2^{-t})^3]=0.1836，即风险之和；精确的累计风险是 1−∏=0.1726。从 t=1 起的存活为 0.0241。整体平移一期后，自身边际收益为 +0.0231、+0.0372、+0.1018…；在 t=0..40 的网格上，满额授权都是最优反应（c_misc.py）。修法成立。
- **M2-04｜确认**：THEORY §6.4 和 S7 P23 的"zero or below spreads"与命题 6.7 的 Scope、CI(i) 矛盾。同类措辞还出现在 §12.2 第 3 项（"to zero or below, the safeguard spreads"）、§8.3(a)（"zero or below … the safe variant is also the winning one"）和 S6 legible reasoning 段（"zero or negative, legibility pays privately"），应一并改。可以补一句：零税时选择中性，只有通过第 1 层，在看重公共项的开发者中靠选择而扩散。
- **M2-05｜确认**：F̄_k=c_k 时规避者保持初始的相对份额，S6 证明本身写的也是"does not grow … selected out if strict"。核心命题 6.7(3)、表 9.1 R8a、S9 用"keeps out"言过其实。§12.2 第 7 项"sanctioned at least at … which keeps the divergence out"也要同样修改。
- **M2-06｜确认**：n=4、Ω_e=Ω_s=r=c=1、βϱ=1 时，第二种约定给出 0.1667，低于 rΩ_s/(nc)=0.25；第一种约定给出 0.25（c_misc.py）。§10.2 正文这句没有跟着命题 10.2(2) 改。修法成立。
- **M2-07｜确认**：Φ^S=0.5、Φ^R=0.9、s_P=0.5 时，Φ^P 从 0.4 降到 0.3，界从 0.2308 降到 0.1667；两者按比例下降时，界依次为 0.231、0.375、0.545、0.75、0.894，单调上升。措辞问题，程度轻微；修法成立。
- **M2-08｜确认**：五点逐一核对都成立。表 7.1 Capture 行的速率律漏了命题 4.5(2) 的 f=0 和正培植通道；Enforcement 行的 p̄_d 只在 D_i>v_i 时有定义，D≤v 时 (14) 的方向反转；p_d 同时进入 (14) 两侧，应写"Both"；R3a 漏了调整路径的限定；R2 的"not needed"条件应计入已覆盖者的剩余负荷（定理 10.4 下 e_min>0）。表头"each row in the model of the result it cites"只能部分弥补。
- **M2-09｜部分成立**：缺 p=1 属实：s*=2/A−2=206.42，存活 0.0045 只在 p=1 时成立；p=0.5 时 s→∞ 的比值为 0.0144<1。但"Near certainty is exact"本身不错：一致界正确、可逼近，等号时仍严格成立，可以把"below"改为"at most"。要补的是：给定 n 时，绑定的剖面是 k=n−1，不是注 S6.1 所说的 k=0；精确门槛为 (1−q_L)a(1+(n−1)s/n)<1，s=2 时最坏因子分别为 2.0、2.33、2.8、2.98（n=2、3、10、100）。
- **M2-10｜确认**：ext_CI(j) 的 run 默认 T=2000，日志值为 1.38e-87=e^{-200}；CI(i) 是 e^{-20}≈2.06e-9。两者一致，原文的并列写法会误导读者。
- **M2-11｜确认**：独立重建得到 R=0.140、T=0.0017；T=R 时 e_c 分别为 0.0054、0.0349、0.1406、0.4898，对应的合并总量 n·e_c 为 0.0215、0.140、0.562、1.959（c11.py）。legacy N22 也把 e_c 叫作"pooled effort"。表 11.3 的"Not shown"列混入了已证的结论。修法成立。
- **M2-12｜确认**：命题 7.3(2) 的 X 是"extends dominance"，推论 7.4(2)、主张框和 S7 证明（"Proposition 7.3(2) gives the second"）却写成"objectives give least"，缺一步认同。但位置列里的 §8.3(d) 写的是"toward those that extend dominance"，本来就是对的，不需要改。
- **M2-13｜部分成立**：s=1 未写属实：s=2 时谷底为 0.2918，不是 0.1397（c13.py）。但 ρ_A=ρA/(1−A) 已在 S3"Hosts harsher than the forgiving one"中写明，这一半不成立。引理 8.2 的例子缺的不只是 h_a=0.0015 和 h_c(t−10)，连延续路径的风险 h_c(t)=0.05(0.2+0.01t)+0.001 本身也没写；按这组参数可复现 0.976/0.864/0.211 与 0.875/0.575/0.026（c13b.py）。修法改为：S8 写明 h_c(t)、h_a 和滞后；S10 写明 s=1，并引用 S3 的 ρ_A。
- **M2-14｜部分成立**：S11.3(2) 已写明"independent readings whose likelihood ratio is computed from their distribution"，独立性和已知分布两个前提都在，修法中这两项是重复的。真正缺的是不敏感区：界只在两个登记水平上成立。模拟显示，真值 0.75 时（已过阈值 0.5，属于"已满足"）被压下的概率为 0.058，远高于界 0.0072，所以"ready state held back ≤ Σb/(1−a)"只在每个已满足维度位于上登记水平或其上时成立。"at every level of noise"应改为"at every known noise level"：σ 误设为 1 而真值为 2 时，误判率为 0.196，界为 0.0101（c14.py）。
- **M2-15｜确认**：G=10、规则制定慢十倍时，logit 峰值为 71.57，替代者份额 8.3e-32。等速时峰值为 11.29，份额 1.2e-5，在大总体中并未灭绝，所以这一批评主要针对慢速情形（10.45 等）。修法中"写明为反射上限"一项，S11.4(4) 的"never exceeds 1−φ_alt … grows from it"已基本说了。
- **M2-16｜确认**：(1) 表 11.3 标 [thm∣prem]，S11.5、CLAIMS 和 §11 正文都标 [thm]，属实。(2) CLAIMS `require` 仍写"R9 new, awaiting confirmation"，属实。(3) CLAIMS `topology` 写"never necessary"，属实。(4) 命题 6.1(3) 没有覆盖等号情形，而 S6 数值给出 (0,0,1)→0.9375、(1,0,2)→2.1，我已复算。

同族偏差：我与起草者、原评审同属一个模型家族。在 M2-01 中，我把 S3 证明里的行内说明当作"cumulative"的定义，这个判断可能偏宽；家族外评审若认为定义必须放在 S0 或定义 3.2，会把 M2-01 判得更重。
