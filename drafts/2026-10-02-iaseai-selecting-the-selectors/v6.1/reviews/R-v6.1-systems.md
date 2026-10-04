# V6.1 评审：系统动力学与制度设计

2026-10-04。对象：`v6.1/THEORY.md`（sha256 前缀 242a61240d810e51）及 SUPPLEMENT S2、S4、S5.1、S7、S9–S15，DISCUSSION X10、X11，TESTS §5–§9。先读了 `../v6/reviews/R-v6.0-systems.md` 与其 Opus 复核。
脚本与日志（纯 Python 标准库）在 scratchpad `review61/systems/`：`s1_loopgain.py`、`s2_dwell.py`、`s2b_depth.py`、`s2c_pause.py`、`s3_zones.py`、`s4_joint.py`、`s5_joint2.py`、`s5b_clocks.py`、`s6_metaloop.py`，各有同名 `.log`。

## 1. 总判断

上一轮系统评审的要点大多已吸收：Compact 拆成分持的功能，生成之环经由共有之物闭合，驻留时间分两相，keystone 窗口，参与门槛，快慢回路分离。§4 场模型的数字，我用独立方法全部复现，包括 3.81。**没有致命问题。**

需要改的问题有三类。
1. **回路结构的形式对应不准。** Γ 是正系统的直流环路增益，判稳是对的；但"纠错降低 Γ"只在水平型通道成立，在比值型（容量）通道里方向相反。四个回路里，"监管滞后"不是第四条正回路，而是被削弱的那条负回路。
2. **准静态与驻留结论不稳健。** 联合模拟显示：控制成本单调下降时，速率律是保守的；在改革逆转处，以及引入慢变量（人类能力）时，它是乐观的。驻留时间取决于锁定有多深；替代谱系不是细节，而是让驻留时间有界的结构条件。
3. **生成设计与过渡的控制结构有缺口。** 生成之环和功能—形态表都没有"节奏"这一股，而节奏是全文的中心 crux。有几条条款能被被评估方操纵。"按登记指标启动保管"如果要在触发时重新作集体决定，就恰好在 p_d 最高时继承命题 5.4 的失效。

## 2. 发现

### 致命

无。

### 重要

#### I1　Γ 中纠错的方向取决于通道形式；Γ 不决定速度，且只是局部量

**位置。**
- §2 开头框"Why"："…diffusion and correction lower it"。
- §7.1 表与 S7 全表的"correction rate d"一行：Loop gain 与 Working objective 两列都标 ↓。
- Remark S2.1。
- S13"Loop gain and breakout probability"。
- §10.4 第二股的条件"Loop gain below one with margin"。

**问题。**
1. 按式 (2)，r_j、ω_j 固定时，∂Γ/∂d_j = (1−β)r_jω_jδ_f/(d_j+δ_f)² ≥ 0。Γ_δ ∝ δd/(1−δ(1−d−δ_f)) 对 d 严格递增，δ_f=0 时也一样。
   - 在比值型（Tullock）通道里，加快折旧或纠错不降低 Γ；有扩散时反而抬高它。命题 2.3 用的就是这种通道。
   - 只有强度随存量水平线性上升的通道，比如场模型里的规则支持 a·z，才有 r_j=sX*∝1/d，纠错才降低 Γ。
   - 命题 2.3(1) 本身就显示了这一点：S*=(κΩ+nk₀)/d_K，d_K 越大，右侧越小，越容易失稳。
2. Γ 是直流增益，只定符号，不定速度。按 S13，p_d 经 T_dec 由 Γ 决定，这一步不成立。
3. Γ 在平等处取值。反身通道的回报 ∝p²（命题 4.3），培养出的转换 ∝Σp_k^{1+(2−ξ_v)/η}（命题 4.5(4)），所以在当前不平等的状态下增益更高。以 η=1、ξ_v=0、n=4 为例，一方份额 0.6 时，反身项约为平等时的 3.5 倍。

**证据（s1）。**

| 设定 | d 或条件 | Γ | 结果 |
|---|---|---|---|
| 比值型：r=2、κΩ=1、k₀=0.2、δ_f=0.1、n=2 | d=0.1 | 0.714 | 稳定 |
| 同上 | d=0.3 | 1.071 | 失稳：偏差谱半径 1.029，400 期放大 2.7×10³ |
| 同上 | d=0.6 | 1.224 | 失稳 |
| 线性型：s=1.2 | d=0.3 | 1.5 | 失稳 |
| 同上 | d=0.6 | 0.857 | 稳定 |
| Remark S2.1：d=0.2、δ_f=0.1 | — | 2 | 精确增长因子 1.30，文中公式给 1.20；应为 1+(d+δ_f)(Γ−1) |
| Γ 同为 1.2，增益放在快通道（d+δ_f=0.5） | — | 1.2 | 1% 的差距涨到 50% 需 41 期 |
| Γ 同为 1.2，增益放在慢通道（d+δ_f=0.02） | — | 1.2 | 同样涨幅需 980 期 |

**修法。**
- "Why"框改为：*"Sharing, provision that does not have to be won and diffusion lower it in every channel; correction lowers it in channels whose strength rises with the level of the stock, such as rule support, and not in ratio-form channels such as capacity, where faster depreciation leaves it unchanged without diffusion and raises it with diffusion (Proposition 2.3)."*
- §7.1 表与 S7 表把 d 拆成两行：规则支持的纠错（↓）；容量折旧（0 或 ↑，工作目标一列为 ↑）。
- 修正 S2.1 的公式。多通道时写明：增长因子是 (S1) 的根 λ*，不是 Γ 的函数。S13 改为"T_dec set by λ*"。
- 第二股的条件补上："evaluated at the present distribution of standing, where the reflexive channel's gain scales with a high moment of shares (Proposition 4.5(4))"。

#### I2　四回路：形式类型混在一起，延迟与主导权转移没写，负回路的振荡没有建模

**位置。** §7.1"The chain, as four loops"（任务所说的 §2.3 链条，现在在这里）；S2 Bounds；Remark 4.6；S4"What the field model cannot show"；§10.4"each the dual of a loop of Section 7.1"。

**问题。**
1. 四条"回路"形式上不同类：
   - 复利与俘获是同一状态（地位集中度）上的两条正通道。命题 2.2 说它们的增益**相加**，是并联，不是"in series"那样相乘。
   - 自然化叙事是正回路，但只有 [conj]（§5.4），没有形式结果。
   - 监管滞后是纠错这条**负回路**。前三条压低它的增益（命题 4.9），掩蔽和节奏拉长它的延迟（命题 4.7、5.11）。
2. 真正的危险结构是回路主导权从负回路转到正回路。文中没有这样说，也没有给出各回路的时间常数：容量周转约 1/(d_K+δ_f)，规则支持约 1/(εd)，采纳约 1/ζ，心智形成以代际计。
3. 全文唯一的负回路（纠错或动员）在任何动态模型里都没有以带延迟的形式出现：Γ 只对正通道成立，场模型又是合作系统，不能有环。

**证据。**
- s1(d)：正通道 g₁=0.5（D₁=0.6），加一条慢的反向通道 g₂=−0.05（D₂=0.95）。净直流增益只有 0.25<1，特征值却是 1.000±0.122i，模为 1.0075：周期 52 期的**增长振荡**，600 期放大 111 倍。可见 Remark 4.6 的"监管周期"可以是发散振荡，不只是锁定。
- §10.4 表的第三股"Dual of: The belief in a struggle for survival"，对偶的是 §7.1 所说的 gain（驱力），不是四回路之一。监管滞后则没有对偶股。

**修法。**
- 语料原文保留（不做有损合并），后面补一段形式对应：*"Formally the four differ. Compounding and capture are reinforcing channels that add in one loop gain and share one state, the concentration of standing (Proposition 2.2); the naturalized narrative is a reinforcing loop stated as a conjecture (Section 5.4); regulator lag is the balancing loop of correction, whose gain capture lowers (Proposition 4.9) and whose delay tempo and masking lengthen (Propositions 5.11, 4.7). The danger is a shift of loop dominance from the balancing loop to the reinforcing ones, across delays that run from the turnover of capacity to the formation of minds."*
- S2 加一条 remark：带延迟的反向通道，在净增益小于 1 时也可能产生增长振荡 [num]。因此纠错不能从 Γ 里减掉；监管周期列入 Study 2。
- §7.1 的"gain"（驱力）与 loop gain 撞名。改称 amplifier，或注明它不是 Γ 的因子，而是经 θ_Γ（命题 3.9）部分由 Γ 内生。

#### I3　联合模拟（TESTS Study 2）：准静态在单调趋势下保守，在逆转和慢变量处乐观

**位置。** 假设 4.2 末句；命题 4.5(2) 及其 Scope；命题 9.1 的 R3a（"necessary"）；定理 4.12(e) 与 S4 的图示；TESTS Study 2；S13"Capacity and the field""Correction rate and coverage"。

**模型（s4、s5、s5b）。**
- 参数取 checks_v61 的 CS 块：χ=Y=η=1，ξ_v=0，p=0.6，A=0.3，a_E·B̂=1，c_E=1，d(t)=2e^{α_cor·t}，γ=e^{−0.2t}。速率律阈值为 α_ctl/(1+η)=0.1。
- 评估域按式 (10)：ζ=1，ε=0.5，x_ev(0)=0.01。
- 容量 q 取四种动态：
  - QS：q=q*，即准静态；
  - R(κ)：常速滞后，q′=κ(q*−q)；
  - GA(V)：Price 梯度、加性方差，q′=V(χp²Y/d−γq)，调整率 Vγ 随控制变便宜而下降；
  - GM(V)：方差 ∝q²。
- 刚性方程用指数积分器。
- 人类能力 ℳ：委托下以 δ_h 衰减，否则以 ϱ_h 恢复；纠错率取 d_eff=d·(ℳ/ℳ₀)^w。

**结果。**

| 实验 | 结果 |
|---|---|
| E1 证书失效与俘获时刻，α_cor=0.05 | QS 28.8/44.9；R(0.1) 38.1/56.0；R(0.03) 46.9/66.3；GM(1) 28.9/45.0；GA(1) 从不失效。滞后 Δt=η·ln(1+g/κ)/(α_ctl−(1+η)α_cor)，g=(α_ctl−α_cor)/η：κ=0.1 时预测 9.2，模拟 9.3 |
| E1′ 视界内仍被俘获的最大 α_cor，H=150/300/600 | QS 0.085/0.093/0.096；R(0.03) 0.079/0.090/0.095；GM(0.1) 0.063；GA(1) 0.009；GA(0.1) 0 |
| E2 逆转：d₁=0.5 的俘获态（G=1.46），把 d 提到 d₂ 维持 T 后撤回 | d₂=1.0 所需 T：QS 94.8，R(0.03) 107.7（+14%）；d₂=0.7：354 对 399 |
| E3 两个时钟：α_cor=0，m_in=0.5>m_fl | QS 与 R(κ≥0.1) 静默越过地板，报警时 V=0.20；R(0.03) 与 GA(1) 在 t=32.1、V=0.58 时及时报警 |
| E4a 委托 D(t)→1，w=1 | 仍被俘获的最大 α_cor 从 0.096 升到 0.145、0.190、0.231（δ_h=0.05、0.1、0.2），约为 0.1+δ_h，有限视界内略小 |
| E4b 俘获→掩蔽→"委托看似安全"的回路：D=0.1+k_D·x_ev，δ_h=0.2，ϱ_h=0.05，w=0.5 | 从俘获态解除所需的永久 d：k_D=0 时 0.634，与准静态证书的 0.638 一致；k_D=0.3 时 1.006；k_D=0.6 时 1.675 |

**回答三个问题。**
1. **时间尺度不分离时，准静态结论是否存活？** 控制成本单调下降时，只要容量的调整率不随之衰减，速率律作为指数条件就存活，滞后只推迟失效。此时准静态是保守的：它让证书失效得更早。
2. **在哪里断？** 三处。
   - 若选择对容量的响应随成本曲线变平而变慢（GA），速率律就高估了需求，"必要"不成立。容量要指数增长，就得能跳向不断远去的最优点；这更像策略选择，而不是渐进选择。按 §3.1 的规则，这需要单独论证。
   - 在逆转处，容量是存量。准静态高估改革的效果，在本参数下约 6–14%；κ≪εd 时差距更大。
   - 若纠错依赖人类能力，而委托在侵蚀它，速率律就多出约 δ_h 一项，并出现滞回：所需改革是准静态证书的 1.6–2.6 倍。Study 2 预期的特征（纠错增速略高于速率律仍然失效）不会来自容量滞后，因为滞后只会推迟失效；它来自这类侵蚀纠错本身的慢变量。
   - 另外，定理 4.12 的条件 (e) 对容量的时间常数敏感。定理本身没错，(e) 是被检验的条件；但 S4 的外生时钟图示掩盖了这一点。
3. **核心应当怎么说？**
   - 命题 4.5 的 Scope 加：*"In a joint simulation in which capacity adjusts at a finite rate, the rate law survives when the adjustment rate does not fall as control cheapens, failure being delayed by η ln(1+g/κ)/(α_ctl−(1+η)α_cor); when selection on capacity slows as the cost curve flattens, the requirement is lower. The quasi-static model is conservative while the cost of control falls, and optimistic after reforms and wherever correction itself rests on a slow variable that the contest erodes."*
   - R3a 改为"necessary when capacity tracks its selected level"；证书检查**测得的**转换，而不是 q*。
   - S13 新增一个接口："Human capacity and correction"：d 依赖 ℳ；完全委托时速率律约加 δ_h；若俘获使委托显得安全，就形成一个带滞回的回路。同时把 Study 2 预期的失效特征改写成上面的说法。

#### I4　驻留时间取决于锁定深度；替代谱系是让驻留有界的结构条件；命题 4.11 的 Scope 句与它所附的暂停不符

**位置。** S11"Dwell times"；§11.4"Dwell times"；命题 4.11 的 Scope；TESTS Study 2 末项；CHANGELOG"Not done"。

**复现（s2，与 DW 块方法独立）。** 做法是反向积分求出鞍点的稳定流形，隔离期轨迹用解析式，再取首次进入。
- 驻留：1.886/5.318/10.453（ε/ζ=0.1）；5.859/10.343/16.181（ε=ζ）。
- x_σ：0.984（ε/ζ=0.1）；0.676（ε=ζ）。
- s*：1.594/4.965/10.000。
- **3.81 可以复现**：G=10、ε/ζ=0.1，替代份额的硬下限 0.001。同一下限下，G=5 为 2.99；ε=ζ、G=10 为 11.79。下限 0.01 时为 3.52。

**问题。**
1. **深度。** 没有下限时，驻留随起点的 logit 深度线性增长：每多一个 logit 单位，多出 ε/ζ 个 1/(εd)。
   - G=2、ε=ζ：x₀=0.99 时 5.86；1−10⁻³ 时 8.17；1−10⁻⁶ 时 15.08；1−10⁻¹² 时 28.90。
   - G=10、ε=ζ：从 16.18 升到 39.22。

   俘获态的 logit 以 ζ(G−1) 的速度增长，所以在纯模型里，所需维持时间随俘获已持续的时间增长。S11 的数字暗含 x₀=0.99 这个任意起点。
2. **替代谱系的效果取决于它的形式。**
   - 能在规则改变后被招募、作为再生源的谱系（硬下限）会缩短驻留。
   - 放在选择之外、不招募的谱系（x=(1−λ)y，等价于 b→b(1−λ)）没有作用：10.44。
   - 对称的再播种 μ（λ=10⁻³）给出 3.28（G=10、ε/ζ=0.1）和 8.78（ε=ζ），但它也在再播种主导实践。
3. **命题 4.11 的 Scope 句。** "at least ln G/(εd) plus the time to repay" 不适用于冻结份额的暂停：冻结的份额不会累积锁定。所需长度是 ln(G/S(x_p))/(εd)（s2c）：
   - G=2、ε=ζ：x_p=0.3 时不需要暂停（S=2.15>G）；x_p=0.5 时 0.69=ln G；x_p=0.6 时 1.50；x_p≥0.676 时为无穷；
   - ε/ζ=0.1：x_p=0.1 时 0.24；x_p=0.95 时 2.08。

**修法。**
- S11 与 §11.4 加：*"The hold depends on how deep lock-in has become: each unit of logit depth adds ε/ζ units of 1/(εd), and without a floor on the alternative, depth grows with the age of capture. A lineage of the alternative that can recruit when the rule changes bounds it (10.45 to 3.81 with a 0.1% floor); one kept outside selection does not [num]."*
- 这正好给"可"（多元谱系）提供一条定量理由：多元让改革的代价有界，也让它可估计。份额接近 1 时，锁定深度从水平上分辨不出来。
- 命题 4.11 的 Scope 改用 S11 的冻结份额公式；"ln G 加偿还"一句只留在 §11.4，那里说的是隔离规则制定、份额不冻结的情形。
- CHANGELOG 中"alternative-lineage dwell"一项可以关闭，注明所用定义。

#### I5　生成之环与功能—形态表缺"节奏"和"人类决定权"

**位置。** §10.4 的表，及"each the dual of a loop of Section 7.1"；§10.5 的表；对照 §9 的 R5、§5.3、§11.3 的 E3、X10 的"Other provisions"。

**问题。**
- **有功能，缺形态。**
  - R5（未覆盖的危险份额可和）在 §10.5 没有形态，在 §10.4 也没有对应的股；而 §12 把它当作中心 crux。
  - E1 和 O2（D3）只出现在 X10 的"其他条款"里。
  - 监管滞后没有对偶股。
- **有形态，缺功能。** X10 里的"受影响者议院"和"上诉"，在核心表中没有对应的功能行：R7 的 standing，以及纠正纠错者本身的错误。"Authority (V4)"一行给的是判据，不是形态。

**修法。**
- §10.4 加第五股：*"Pace bound to understanding | Dual of: regulator lag | Carrier: tempo thresholds tied to measured coverage per class; drilled human capacity | Condition: aτ_c<1 with margin; uncovered share summable | Test: catch rates of planted defects at fixed human hours stay level as capability grows"*。
- 第三股改写为"dual of the gain"。
- §10.5 加四行：Tempo（R5，定理 5.12、命题 5.11）；Human decision authority（O2、E1、引理 6.3）；Standing of those affected（R7，对应议院）；Due process against correctors（对应上诉）。
- "Authority"一行的形态写成"separation rule plus chamber"。

#### I6　设计中可被操纵的条款（机制设计与 Goodhart）

**位置。** X10 的表：
- Evaluation 行："findings lose executive force until recertified"；
- Standard-setting 行："held-out metrics registered in advance"；
- Levy 段；
- Execution、Fallback、Rules 三行的 Financing 和 Appointment 都是"—"；
- Chamber、Appeal 两行的"Ends"是"—"；
- Recusal 段："lapse if not concluded within their deadline"；
- End conditions 段。

**问题与推导。**
1. **注入致失格。** 行和计入"来自被评估方"的转化（命题 4.9(2)、10.6）。被评估方单方面向某个评估者输送资金、人员或数据，就能把它的行和推过 1，使针对自己的发现失去执行力。用同样的办法也能凑出"若干证书失效"，触发解散。
2. **预先登记的留出指标一旦公开，就不再是留出的。** Goodhart（§5.4）。
3. **征税按 d* 指数化。**
   - d* 由测得的转换（A、B̂、χ）算出。付费方把影响转到未被测量的通道，就能压低 d*，从而压低经费。
   - 若由领这笔经费的纠错者来估算 d*，他们又有夸大的激励。
   - X10 一边写"A levy on frontier compute above a threshold"，一边写"revenue base is decoupled from the activity it constrains, so that it does not shrink under E2"。前沿算力恰恰是 E2 所约束的活动，两句互相矛盾。
4. **最难的环节规定最少。** 执行和强制后备（D5，最难的情形）在表中没有融资、没有任命规则、没有行和证书。议院和上诉没有撤换或终止条件，过不了 Remark 10.8 的撤回测试。
5. **"逾期失效"可被拖延利用。** 被评估方不给访问，拖到截止期，评估就自动失效。
6. **共同前沿内部的搭便车。** 命题 10.2(4)(5)：合并努力低于阈值时只剩全员竞赛；所需的合并努力随 Ω 陡增，从 0.0054 升到 0.49。前沿贡献若是自愿的，搭便车会把协调均衡推回竞赛。

**修法。**
1. *"Conversion into an evaluator from a party it assesses, outside the evaluator's disclosed channels, is a violation by that party; it does not suspend findings against that party, and the assessment is reassigned to an evaluator of different lineage."* 解散只由覆盖率，以及不能归因于被评估方的证书失效触发。
2. 留出指标用哈希预先承诺，评估时才揭示。
3. 税基要宽于被约束的活动：总算力，或按经济规模缴纳的条约份额，前沿算力另加附加费。d* 由不领这笔经费的机构按保守上界估计，并用直接测量（漏检相关性、植入缺陷的捕获率）校核；设下降速率上限（棘轮）。
4. 为执行和后备写明融资、任命和行和证书；为议院和上诉写明撤换条件。
5. 被评估方拖延期间，截止期停止计时。
6. 前沿贡献按公式缴纳，与征税同源，而不是自愿。

#### I7　多中心与 Ostrom：功能分离不等于多中心

**位置。** §10.5"A candidate configuration"、X10、§3.6。

**对照 Ostrom 设计原则。**

| 原则 | 状况 | 说明 |
|---|---|---|
| DP1 边界 | 有 | 能力阈值、危险类别 |
| DP2 收益与成本相称 | 部分 | 主要付费者没有表决权；命题 10.7 也承认强类型需要接近其竞赛收益的份额 |
| DP3 集体选择 | 缺 | provider 不得修订规则。Ostrom 的经验是，被规制的使用者不参与修订，会损失本地知识与守约；强者还有退出选项。这与俘获理论有张力，文中没有说明这一张力 |
| DP4 监测 | 有 | — |
| DP5 分级制裁 | 有 | — |
| DP6 冲突解决 | 部分 | 上诉是集中的，不低成本，也不就近 |
| DP7 外部承认 | 缺 | 行星尺度没有外部权威；与国家主权的关系只有"东道国先执行"一句 |
| DP8 嵌套 | 缺 | 每个功能只由一个机构持有。这是单一尺度上的功能分离（权力分立），不是多中心（多尺度、管辖重叠、相互调适）；"many hands"只用在评估上 |

全球公地的文献（Dietz、Ostrom 与 Stern 2003；Stern 2011，凭记忆，未重读原文）另外提了三条：分析性审议、制度多样性、嵌套。前两条文中已有（阶段 1 和"学习"一行），嵌套缺。

另一个缺口：证书"任何人都能从公开数据重算"，但谁来强制转换数据的披露与审计？这个数据层是新的 keystone，表中没有对应的功能行。

**修法。**
- 加一句 DP3：provider 有发言权、没有表决权（notice-and-comment、技术输入），并披露自身的转换。
- 各功能分国家、区域、全球三层，有共同地板，相互承认。"学习"一行已有雏形。
- 新增功能行：*"Disclosure of conversion data | Certificates are only as good as the data on conversion, and omission is the cheapest capture | Mandatory, audited disclosure with a sanction above the gain from omission (Lemma 3.3(3))"*。
- 写明"separately held functions"在每个功能上仍是单中心，与"polycentric complex"不同。

#### I8　把过渡当作控制问题：启动、可观测性、滞回、次序

**位置。** §12.1"Prepared now, activated on registered indicators"及其触发句；定义 11.4；§11.4 的表与 Dwell、Windows 两段；命题 11.5。

**问题。**
1. **执行延迟。**
   - 预先准备保管等于前馈加预置的执行器，把回路延迟 τ_c 从"建设加决定"缩短到"检测加决定"。按命题 5.11（aτ_c<1，裕度 e^{aτ_c}），这是正确的控制逻辑，应保留。
   - 但如果"启动"要在触发时作一次新的集体决定，触发恰好发生在 T_dec 已短、p_d 已高的时候，也就是剪刀合拢处（命题 5.4(4)、§5.5），克制在此时最难执行。所以启动必须预先承诺、由机制自动执行，类似财政里的自动稳定器。
2. **可观测性。**
   - T_dec 的估计受掩蔽影响（m_model 也作用于独立评估者，命题 4.7），也受策略性披露影响（开源与闭源的差距 C5 可被被测方操纵），偏向触发过迟。
   - S11 说能否撤回取决于规则支持相对分界线的位置，但 z 观测不到；份额接近 1 时，锁定深度也分辨不出（见 I4）。
3. **滞回。**
   - 启动和解除用不同的指标，这是对的。
   - 但定义 11.4 的准备度只看水平，没有驻留条件；而 S11 已经表明，水平先于安全改善（Test D）。
   - 七个维度合取、不可互补，再加上测量噪声，会系统性地偏向"未准备好"，由此产生退出压力；按 §9，覆盖可能因此连锁瓦解。
4. **次序。**
   - §11.4 按信任由易到难串行排列各阶段。按时间常数，应当最慢的先开始：阶段 3 的驻留是 ln G/(εd) 加偿还，若 1/(εd) 取制度周转的 5–10 年，就是数十年；人类能力恢复约 1/ϱ_h；心智形成以代际计。这些都比领先差距的动态慢。
   - §12.1 的分层其实已是并行的，与 §11.4 不一致。
5. **命题 11.5 的性质。**
   - 它标为 [thm]，证明只是按四项罗列别处的结果，没有证明四项可以同时满足，也不是控制意义上的可达性。
   - 用 Aubin 的语言，可达是指当前状态位于目标集在可容许控制下的可存续捕获域（viable capture basin）之中；S11 的驻留时间正是一维场模型里的最短捕获时间。
   - 渐进的步骤只有当每一步各自跨过阈值、并保持驻留（棘轮）时，才能穿过分界线；否则会被命题 4.10 重新吸收。

**修法。**
- 触发句后加：*"Activation is committed in advance and executed by mechanism, not decided afresh when the trigger fires, because the trigger fires where restraint is least enforceable (Proposition 5.4(4)); its indicators rest on channels that observe actions directly, under the conservative rule of Remark 4.8."*
- 定义 11.4：每一维加上"在该维慢变量的时间常数内保持达标"，写明测量误差和序贯判定规则。
- §11.4 的阶段表改写为并行轨道，每条轨道标出时间常数。
- 命题 11.5 改标 [def] 加各项支持，或重述为捕获域命题，写明哪些部分已证。
- 写明"graduated steps reach only as a ratchet"。

#### I9　杠杆（Meadows）

**对应。**

| 层级 | 本文的干预 |
|---|---|
| #7 正回路增益 | Γ：β、k₀、κ、δ_f |
| #8 负回路 | d、τ、覆盖 |
| #6 信息流 | 后果返回、共享测量、掩蔽、验证 |
| #5 规则 | χ→0、one rule for all、准入约束、分离规则 |
| #4 改变结构的权力 | "选择选择者"就是 #7 的赢家夺取 #4/#5 |
| #3 目标 | 改变赢得之物所授予的东西 |
| #2 范式 | Ψ 与"we are one" |
| #9 延迟、#11 缓冲 | E3、驻留、地板之上的裕度、备用能力、替代谱系；只零散出现 |

**判断。**
- 本文的独特之处在于把干预放在 #7 与 #4/#5 的**耦合**上（χ、b_ij），并用命题 4.10 说明为什么不跨阈值的参数改革会被重新吸收。层级是对的。
- 但高杠杆点延迟最长、阻力最大。本文的变革路径"理解（#2）→ 就规则达成一致（#5）"，按引理 3.10 只能经由传递项起作用，所以需要 #9 和 #11 来争取时间。
- I1 恰好是 Meadows 所说"把杠杆往错误方向推"的一例：提高容量的折旧不会削弱复利。

**修法。** §12.2 加一句：把节奏（#9），以及替代谱系、备用能力和宿主裕度这类缓冲（#11），列为争取驻留时间的低阻力杠杆。

### 次要

**m1　Remark 2.5 的措辞。** 文中说它是命题 2.2 的"two-channel case"，但不是。命题 2.2 的 J 是经由胜率这一枢纽的秩一扰动；Remark 2.5 的对角线没有自增益，是一条交叉回路。两者"of the same form"（都是直流环路增益小于 1），并非同一定理。S2 对命题 4.9 已经这样写，这里照写即可。

**m2　Remark S5.1 与 Test G。**
- 我用直接累加折现收益流的办法复现了全部数字：θ_rep 为 −0.901、−0.812、−0.322、0.634、0.937；θ=0 在 p_d=0.9495 处失去可执行性；D=0.5、p_d=0.9 时为 2.337。
- 但"so the restraint gap … grows with p_d"只在 D=C 时成立（s3）。设 θ~U[−1,3]，宽目标为 θ>1，窄目标为 θ<1：
  - D=0 时，差距随 p_d=0、0.5、0.8、0.9、0.95、0.99、1 依次为 +0.05、+0.09、+0.21、+0.34、+0.50、+0.82、+0.97，单调上升；
  - D=0.5 时依次为 +0.05、+0.30、+0.92、+0.33、0、0、0，呈驼峰状。p_d→1 时，没有任何 θ≤n−1 能维持克制，这正是 Test G 所登记的结构现实主义的反面预测。
- 修法：S5.1 和 TESTS 改为"grows with p_d over the range where the wider objective still sustains restraint; when a decisive position is worth more than cooperation the gap closes as p_d→1 (Proposition 5.4(4)), where this theory and structural realism agree; the test discriminates at intermediate p_d"。

**m3　一个让"生成秩序是否吸引"可以计算的建议。**
- 经由共有之物的闭合，可以写成**环路增益上的环路**：Γ_δ → θ_Γ（式 9）→ 规则制定 → Γ。
- 玩具模型（s6，n=4，θ₀=0.5，规则制定对 θ_Γ 的响应陡度为 k）：
  - k=12、θ_c=0 时，有两个稳定不动点：Γ_δ=0.108（θ_Γ=0.39）和 0.98（θ_Γ=−0.95），中间 0.404 处是不稳定点；
  - k=2 时只有一个不动点。
- 这样，§10.4 的 [C] 就可以在一个指定的模型里成为定义 2.4(2) 意义上的结果，"先换盆地再加速"也有了分界线的含义。
- 注意：这种统一正是同一模型家族偏好的那类优雅，只宜当作建议。

**m4　术语。**
- "four loops in series"：见 I2。
- 议院与上诉没有终止条件：见 I6。
- 任务所称"§2.3 的四回路"现在位于 §7.1。

## 3. 好的、不应改动的部分

1. **Γ 的构造。** 胜率是单一枢纽，秩一耦合，直流增益判稳，通道增益相加；论证用 Perron–Frobenius，并以数值 Jacobian 核对。我用非线性模拟复核过，符号判定无误。Γ_δ/(1−Γ_δ) 作为地位的价格，相当于闭环增益 1/(1−L)，经命题 3.9 把结构与目标连起来。这是全文最强的形式支点。S2 的"Γ 统一什么、不统一什么"一表是诚实的。
2. **场模型的读法。**
   - 合作系统，因而描述锁定而非周期（Hirsch），这一点写得诚实；
   - "无俘获态总是局部稳定，所以俘获靠播种到来，没有临界慢化；改革中自相关上升反而表示进展"，这是正确且有用的预警学结论；
   - 速率律与 ξ_v 无关；
   - 命题 4.11 的 x_σ（0.676、0.984）与 S11 的两相驻留，以及"用份额水平判断回撤为时过早"（Test D）：我用独立方法完全复现。
3. **定义 2.4 的三层，以及按层标注。** 生成秩序是否吸引标为 [C]，§7.4 也说明当下处在哪一层是开放的。
4. **生成闭合"不经由赢家"。** 规则不在载体之间被选择，只能靠覆盖、公式供资和整体回路来维持；明确拒绝"贡献者占据规则岗位"（科举之路）。这一点是对的，应保留。
5. **X10 的分离规则。** 超多数与议院只放在慢回路上，快回路保持快速、事后审查；按命题 5.11，这是正确的控制设计。保管的终止条件是可核查的指标而不是日期。"Coverage can unravel"与参与门槛，以及"合并前沿、分散纠错"的两阶反向，也都应保留。
6. **"预先准备、按登记指标启动"。** 用前馈克服执行延迟，方向正确，只需按 I8 改为自动执行。
7. **S14 的反例表与各处的 [conj]、[C] 标注**，保留。

## 4. 核对了什么，没核对什么

**读过的部分。**
- THEORY：§2–§12 中与本维度相关的全部；
- SUPPLEMENT：S0、S2、S4、S5（含 S5.1）、S6（6.3）、S7、S9–S15；
- DISCUSSION：X10、X11；
- TESTS：§5–§9；
- CLAIMS：对 v6.0 评审的处置表；
- 上一轮系统评审及其 Opus 复核。

**计算过的部分：** s1–s6，内容见上；参数写在各脚本的开头。

**没有核对的部分。**
- 命题 4.3、4.5 的证明，只核对了指数条件；
- 定理 4.12、10.5 的数值（HO 块），以及命题 10.6、10.7、11.2；
- X8 与 EVIDENCE；
- 没有运行 checks_v61.py；
- Ostrom 与 Stern 的原文没有重读，上面的对照凭记忆；
- 联合模拟只试了四种容量动态，一个评估域、外生的 C 集合，参数取自 CS 块，没有校准。"准静态在单调趋势下保守、在逆转和慢变量处乐观"这一方向，在四种动态里一致，但没有证明。

**同一模型家族的偏差。** 我与起草者同属或相近的模型家族，以下几处可能受影响：
1. m3 的统一化建议，正是这个家族偏好的优雅形式；
2. 对 §10 设计是否健全的判断，可能与起草者有共同盲点，尤其可能低估结构现实主义的反对：没有外部执行者，D5 是否可解；
3. 对 Ostrom 的对照可能来自同一批二手概述；
4. 联合模拟中把纠错与人类能力耦合（d_eff=d·ℳ）是我的建模选择，不是本文的命题；它落在 S13 已登记的开放接口"d≤F(U, resources, delay, authority)"之内。
