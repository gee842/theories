# FIXES-v6.2-verify：V6.2 核验轮发现的落实记录

*2026-10-04。执行者：Claude（Opus 5.5），与起草者、评审者、核验者同属一个模型家族。依据：五份评审 `R-v6.2-{math-I,math-II,fidelity,coldread,evidence}.md` 与五份对抗核验 `C-v6.2-*.md` 的判定。只改了 `src/`（core、supp、disc、reg，以及 `src/refs_v62.py` 的文献数据）和 `checks_v62.py`；装配文档全部由构建生成，没有直接改动。所有"确认"与"部分成立"的发现都已落实，按核验者的修法，并按严重度先后处理；两项"驳回"（fidelity m9、evidence E13）未动。凡需 Ren 的话、价值判断或篇幅决定的，没有替他决定，列在第三节。*

*行号指改后的 `src/` 文件。"改前 → 改后"只给要点；完整的改前文本在本次改动前的快照里（会话草稿区 `snap/`），也可以从 `v6.1/`、各评审文件引文中对照。*

## 一、构建与检查状态

| 步骤 | 结果 |
|---|---|
| `python3 src/assemble_v62.py` | no problems；核心 93 个、补充 35 个声明；核心约 59,560 词（改前 56,194），补充 61,453 词，讨论 21,397 词；导读 3,168 字（改前 2,650） |
| `(cd src && python3 refs_v62.py)` | THEORY 111 条、SUPPLEMENT 92 条、DISCUSSION 134 条（改前 103、89、132） |
| 再次 `assemble_v62.py` | no problems |
| `python3 xref_v62.py` | ALL CHECKS PASS：三份文献表双向覆盖；32/32 必留短语在；导读九条与第 1.2 节逐条对上（第 9 条 67%，与改前相同）；核心正文未点名任何国家或企业。登记册中原先无处解析的 Khan 2024、Kenton 2024、Zhu 2026 现已在 THEORY 文献表中 |
| `python3 checks_v62.py > checks_v62.log` | 41 个块、202 条断言全部通过（改前 40 块、188 条），324 秒，退出码 0。新增 VF 块 14 条断言；SM(12)、AL(6.11) 两条按平移后的例子重写；JX(e) 与 JX(E) 的标签改为"一期约化下的恒等式"与"实现核对" |

句子账：按 LEDGER §3 的方法对 V6.1 全部 1,060 句重算，低于 0.4 的为 100 句（≥0.8：569；0.6–0.8：255；0.4–0.6：136）。新落到 0.4 以下的三句（V61-0452、V61-0579 改写，V61-0387 更正）都已判定去处；V61-0015、V61-0075 回到 0.4 以上；V61-0388 改记"改写"。重生成的 TSV 在 `src/reg/LEDGER-v62-sentences.tsv`。根目录的 `LEDGER-v62-sentences.tsv` 不在可写范围内，**需要复制过去**：`cp src/reg/LEDGER-v62-sentences.tsv LEDGER-v62-sentences.tsv`。

## 二、逐项处理

判定沿用核验文件："确认"、"部分成立"、"驳回"。

### math-I（R-v6.2-math-I）

| ID | 判定 | 处理与位置（改前 → 改后） |
|---|---|---|
| M1 | 确认（重要） | 选修法 (a)，并补出修法 (b) 的精确式。`core/50_s5.md:40` Remark 5.5：标签 [thm] → [thm; identity: JX]；"(14) reads υ ≥ 1−p̄" 与"恰为命题 8.6 的门槛"改为只在**一期约化**下成立（D、v 读作以逃脱、及时检测为条件的归一延续值，含揭晓前各期）；保留为 [thm] 的只有 p_d=1−υ(T_dec) 与"检测须超过随获胜价值上升的水平"（对 D>v、C>v 的偏离）。`core/50_s5.md:42` Scope 写明约化只在 T_dec=1 时精确，两种时序把交点分别前移、后移 [num: VF]。`supp/05_S5.md:48–61`：新增 *Exact timing*，给出 (A) 检测触发惩罚：(1−δ)g + a^T(D−C) ≤ λδ(1−a^T)/(1−a)(C−v)；(B) 完全监测、只推迟制止：(1−δ)g + δ^T p_d(D−v) ≤ δ(C−v)；证明两式下"门槛随 D 上升"仍成立（用 E[δ^{min(𝒯,T)}] 与随机占优）；联合模型阈值 0.551 → (A) 0.514、(B) 0.556（D−C=0.5：0.536 → 0.514、0.554），无突破时制裁权重 0.461 对 0.9。*Check of the clock* 中按约化式抽样的偏离值改标 [identity: JX]，写明"不检验时序"。`supp/05_S5.md:139` Remark S5.2 注明用的是约化时序，并给两种时序下的阈值。`core/80_s8.md:82` 命题 8.6 Scope 加 "in the one-period reduction"。`checks_v62.py`：JX 块头与 (e) 标签改为恒等式；VF(b) 逐期加总核对两种闭式（误差 2.7e-15、1.9e-15）并重算三种阈值 |
| M2 | 确认（重要） | `core/20_s2.md:43` 命题 2.2(4)：r^pr（与 r^eq）改为沿相对移动（本方 +y，其余各 −y/(n−1)）定义，r^eq = nX*·dp/dy，注明它等于原定义 n²/(n−1)·∂p/∂lnX；r^pr 为同一移动下本方强度固定、对手按马尔可夫策略。`supp/02_S2.md:29` Price 一条重写：说明为何必须沿相对移动、只动本方存量为何不行，给静态反例（n=2、s=1：只动本方 1.00，相对移动 1.50，共同移动使 p_i 变化 −0.25）[num: VF]；共享损失项改为沿同一移动取导数。`supp/02_S2.md:49` S2.2(2) 注明齐次竞赛中两种定义一致。`supp/00_S0.md:24` 符号表同步。VF(a) 以纳什迭代独立复算 |
| M3 | 确认（次要） | `core/50_s5.md:118` 命题 5.17(1)："Perron 根随各通道赢得份额上升" → "随各通道的赌注上升；随某通道赢得份额上升只在 ξ_r<1（如比值通道）"。`core/50_s5.md:123` "The pivot"：限于比值通道，并写明"供给与赌注同步增长使两刃不动"只在 ξ_r=0 成立，其余通道增益随赌注增长。`supp/05_S5.md:133` Arm 1 补出推导（r_jω_j ∝ Ω·X*^{ξ−1}，对 Ω 的弹性 1−ω+ξω；经由供给变动时当且仅当 ξ<1 上升）；"pivot" 补水平通道按 2、4 倍同步放大时 Γ 也放大 2、4 倍 [num: VF]。VF(d) 用数值雅可比核对 |
| M4 | 确认（次要） | "at least in proportion" 改为"决定性随存量增长得足够快之处，尤其至少同比增长之处"，并指向 S2.4(2) 的精确阈值：`core/20_s2.md:9`（Why 框）、`core/20_s2.md:60`（Which levers，补一句阈值低于同比）、`core/10_s01.md:21`（§1.2 第 1 条）、导读第 1 条 `core/00_head.md:16`、`reg/CLAIMS.md:62`（chansign 行）、`reg/CLAIMS.md` §9 第 6 项 |
| M5 | 确认（次要） | `supp/04_S4.md:60`："a_ev B̂ = c_ev = 1" → "a_ev Σ_j b̂_{ev,j} ȳ_j = c_ev = 1, so that a_ev B̂ = p = 0.6"。`checks_v62.py` CS(c) 标题同改 |
| M6 | 确认（次要） | `core/50_s5.md:105` 命题 5.16 Scope：二次第三方改为"第三方收益之和为 −k y²"，加条件 n−1+θ(1+k)>0，标签改 [thm; num: TK]。`supp/05_S5.md:125` 补两行证明（曲率、理想点差、斜率，按斜率重标即化为 Crawford–Sobel）。VF(h) 网格核对四组参数 |
| M7 | 确认（次要） | `supp/02_S2.md:43` Remark S2.1 第二条：写明两载体、度量为"领先者相对均值"(X₁−X₂)/(X₁+X₂)，停在 0.447；并注明按 S5.2 的度量 X₁/X₂−1 同一路径第 80 期达到 50%（停在 1.618），四载体时相对均值第 77 期达到 [num: VF]。`core/50_s5.md:125` 命题 5.17 Scope 同步注明。VF(e) 核对 |
| M8 | 确认（次要） | `supp/02_S2.md:113` "Leaders held" 后补两情形论证，刃边 δ_f = d_K Γ₀ 明言一阶不定、不作断言；另报 299 组随机设定（243/56）[num: CE, VF]。`core/20_s2.md:56` 命题 2.3 Scope：模拟改为 [thm, local] 的一阶结论，模拟作核对，案例数改为"十个点名情形与 400 组随机设定"，与 S2 一致。VF(f) 核对 |
| M9 | 确认（次要） | `supp/05_S5.md:139`："at or below … in all 96" 改为由 p_d≥0、D≥C、θ_Γ≤θ₀ 与 p̄ 随 θ 上升推出，只核对实现；保留 84 与 12 两个有信息的计数。`checks_v62.py` JX(E) 断言标签同改 |
| M10 | 确认（次要） | `supp/05_S5.md:65`：σ₁(h)=σ₂(swap(h)) → σ₁(prefix,k)=σ₂(prefix,swap(k))，并写明为何只交换惩罚阶段历史 |
| M11 | 确认（次要） | 与 coldread M1 合并处理，见下 |
| M12 | 确认（次要） | `core/20_s2.md:36` 命题 2.2 Model：份额版本 (1) 是确定性的；概率（抽签）版本给的是期望下一期存量，平等状态不是随机过程的不动点，(1) 的稳定性指期望偏差的一阶动态 |

### math-II（R-v6.2-math-II）

| ID | 判定 | 处理与位置 |
|---|---|---|
| M2-01 | 部分成立（重要） | `core/30_s3.md:23` 定义 3.2：新增"累积选择"——存在常数 ϰ>0，使 π_k>π_l 时 d/dt ln(p_k/p_l) ≥ ϰ(π_k−π_l)；复制子动力学 ϰ=1；注明单调性只定符号。（常数记作 ϰ，因 κ_s 已是地位权重。）`supp/00_S0.md:45` 符号表加 ϰ。`core/30_s3.md:34` 命题 3.4 第二句："If all φ_k are equal" → "If selection is also cumulative, all φ_k are equal"。`supp/03_S3.md:13` 引理 3.3(3) 证明引用新定义；`supp/03_S3.md:19–21` 命题 3.4 证明改为"任何累积规则至少为复制子的 ϰ 倍"，并新增 *Why cumulative*，用核验者的自治三次率反例（d/dt logit = (Δπ)³，τ_eff = ν−1/(1+t)：B=ln(1+t)→∞，份额不超过 0.0017，母体始终高于 0.99；同一路径下复制子使母体降到 0.017）[num: VF]。`core/90_s9.md:13` 表 9.1 R1 模型列 "payoff-monotone" → "cumulative ({{relsel}})"（R2 承"the same"）；`core/90_s9.md:31` 命题 9.2 前提改为累积选择。`core/60_s6.md:49` 引理 6.5 补"在选择的支撑内"与"差距有正下界"，"cumulative" 指向定义；`core/60_s6.md:63` (A_τ) 补 "by a positive margin"。核验者已指出评审原反例无效，未采用。VF(g) 核对 |
| M2-02 | 确认（重要） | `core/60_s6.md:71` Remark 6.8 斜体陈述补：协调可以抬高 F，所以"不充分"只在两前提下一般成立——F ≤ F_max（以排除为界）且固定审计接入下 p_det 随能力趋于零（C12），此时存在一个能力，超过它任何可准入的制裁都挡不住。标题保留。`core/60_s6.md:67`（§6.4）、`core/90_s9.md:27`（§9）各加"under its/the premises of Remark 6.8"；同步 `core/60_s6.md:3`（§6 主张框）、`core/10_s01.md:25`（§1.2 第 5 条）、导读第 5 条、`supp/09_S9.md:15`、`reg/EVIDENCE.md`（EV6）、`reg/CLAIMS.md`（masked 行）、`disc/01_X1.md:153` |
| M2-03 | 确认（次要） | `supp/06_S6.md:45`（命题 S6.2(3)）例子整体平移一期：s_t=2^{t+1}，Δψ_t=2^{−(t+1)}，各期风险都低于一，从起点的存活约 0.024；尾界从 t=4 起为 3/16。`supp/06_S6.md:47` 证明同步。`supp/06_S6.md:49` 数值：边际收益 +0.023、+0.037、+0.102、+0.154、+0.186，网格最优反应 t=0..40，t=4 起精确累计风险 0.1726（风险之和 0.1836）。`checks_v62.py` SM(12)、AL(6.11) 按平移后的例子重写并断言这些数 |
| M2-04 | 确认（次要） | 五处"zero or below/negative spreads"都改为"负税扩散，零税在选择下中性，只经第 1 层看重公共项的开发者选择而扩散"：`core/60_s6.md:75`、`supp/07_S7.md:104`（P23）、`core/c0_s12.md:14`（§12.1 第 3 项）、`core/80_s8.md:56`（§8.3(a)）、`supp/06_S6.md:82`（可读推理）；另同步 `disc/08_X8.md:7`、`reg/TESTS.md`（C9 格、第 7 项）、`core/c0_s12.md:20` 中"withdrawn … pays privately"补零税情形 |
| M2-05 | 确认（次要） | "keeps the divergence out" → "keeps it from spreading …, removes it under cumulative selection if every inequality is strict, and within a type only if"：`core/60_s6.md:63`（命题 6.7(3)）、`core/90_s9.md:21`（R8a）、`supp/09_S9.md:15`（S9 R8a）、`core/c0_s12.md:20`（§12.1 第 7 项） |
| M2-06 | 确认（次要） | `core/a0_s10.md:36`：下界 rΩ_s/(nc) 限于"分给所有人"（第二种约定下限于 βϱ ≤ (n−1)/n），并写出第二种约定下对每个 β 为正当且仅当 Ω_s > Ω_e/(n−1) |
| M2-07 | 确认（次要） | `core/80_s8.md:68` 命题 8.5(1)："随竞赛分支恶化而升向一" → "Φ^S、Φ^P 趋于零时趋于一，按比例下降时上升"。`supp/08_S8.md:36` 证明补比例下降的单调性与单独降低 Φ^P 的反例（0.231 → 0.167）[num: VF] |
| M2-08 | 确认（次要） | 表 7.1：`core/70_s7.md:22` Capture 行补"无单位成本下限、正的培植通道"；`core/70_s7.md:23` Enforcement 行补 D_i(a)>v_i；`core/70_s7.md:20` Compounding 行"Temptation" → "Both, through p_d"。表 9.1：`core/90_s9.md:15` R3a 补调整路径限定；`core/90_s9.md:14` R2 的条件改为 h_V[p̄_unc ē + (1−p̄_unc) ē_cov] < ρ(1−V_min)，`supp/09_S9.md:8` 同步并定义 ē_cov |
| M2-09 | 部分成立（次要） | `supp/06_S6.md:33` 206.4 一例补 p=1。`supp/06_S6.md:35` Remark S6.1：界对 n、p、剖面一致、等号时仍严格；给定 n 时绑定剖面是其余全部委托、p=1，比值 (1−q_L)a(1+(n−1)s/n)，s=2 时因子 2.0、2.33、2.8、2.98 [num: VF]（原文"k=0"已改）。`core/60_s6.md:45` "below" → "at most"，补"一致界；给定 n 时较不确定的锁也够"。"Near certainty is exact" 保留，核验者认为不错 |
| M2-10 | 确认（次要） | `supp/06_S6.md:67`："in a second implementation" → "by t=2000 in a second implementation" |
| M2-11 | 确认（次要） | "pooled effort" → "each cooperator's effort e_c"：`core/a0_s10.md:21`（命题 10.1 首句与陈述）、`supp/10_S10.md:11`（(4)、(5)）、`disc/10_X10.md:40`。表 11.3 `core/b0_s11.md:88`：陡升一句从 "Not shown" 移到 Support |
| M2-12 | 确认（次要） | `core/70_s7.md:7`（主张框）、`core/70_s7.md:64`（推论 7.4(2)）："toward those whose objectives give least" → "toward those that extend dominance, and so, where extending dominance goes with giving least, toward those whose objectives give least"；`supp/07_S7.md:19` 证明同步。§8.3(d) 本已正确，未动 |
| M2-13 | 部分成立（次要） | `supp/08_S8.md:7` 引理 8.2 例子写明 h_c(t)=0.05(0.2+0.01t)+0.001、安排自身风险 0.0015、退路 h_c(max(t−10,0))。`supp/10_S10.md:39` 定理 10.4 裕度写明选择速度 s=1，并写出 ρ_A=ρA/(1−A)、指回 S3（核验者指出 S3 已有，故只作交叉引用） |
| M2-14 | 部分成立（次要） | `supp/11_S11.md:69` Remark S11.3(2)："at every level of noise" → 在两个登记水平上、在检验已知的噪声下成立；两水平之间是不敏感区；七维的界限于已满足维度位于上登记水平或以上。`supp/11_S11.md:73` 数值补不敏感区（真值 0.75：压下约 0.06 对界 0.0072）与噪声误设（假设 1、真为 2：误判约 0.2 对 0.0101）[num: VF]。`core/b0_s11.md:50` 定义 11.2 补噪声模型与两个水平。独立性与已知分布原文已有，未重复 |
| M2-15 | 确认（次要） | `supp/11_S11.md:89` 补"无下限时达到的深度"：logit 峰值 u₀+(ζc/εd)(G−1−ln G)，慢十倍时 71.6（份额 8e-32），等速 11.3（1.2e-5）；说明有限总体中前者已灭绝，无下限的值只显示算术，有下限的值才是有意义的量级 [num: VF]。`core/b0_s11.md:72` §11.4 补一句。反射上限一项，S11.4(4) 已有，未加 |
| M2-16 | 确认（次要） | `core/b0_s11.md:89` 表 11.3 中 Remark S11.5 标签 [thm∣prem] → [thm]。`reg/CLAIMS.md:152` require："R9 new, awaiting confirmation" → "kept by Ren on 4 October 2026"。`reg/CLAIMS.md:127` topology："never necessary" → "not necessary"。`core/60_s6.md:19` 命题 6.1(3) 补"等号时极限保留成本项" |

### fidelity（R-v6.2-fidelity）

| ID | 判定 | 处理与位置 |
|---|---|---|
| I1 | 确认（重要） | 按核验者修法：`core/b0_s11.md:56` §11.3 "The order" 后新增一段，英文转述 Ren 10-03 的条件次序（广义 E1 → E2 或 E3），附中文原文，标 [corpus: possibility-space, 2026-10-03]；"其他都是人类绝路啊"标为他的判断 [val]；附 10-04 [45:45][46:02][46:20] 三句，注明是中英夹杂口述的编辑译文，标 [corpus: alignment-selection, 2026-10-04]；末句写明他的启动条件（广义 E1 未达成）不同于 §12.1 的预测触发，二者如何取舍交 Ren，不在此定。`core/c0_s12.md:9` §12.1 开头加一句指向。`reg/CLAIMS.md:450` §9 新增第 10 项，列出三种选择。**没有**由起草方决定"E2 现在生效"；导读第二层与 §1.2 第 9 条"随答复对齐"一项待 Ren（见第三节）。§7.2 措辞为可选，未改。新增 D43、D44；X1 补对应三行 |
| I2 | 确认（重要） | `core/10_s01.md:29` §1.2 第 9 条、`core/00_head.md:24` 导读第 9 条按评审改写（开头几步无需信任；信任随过渡增长；核查不能代替信任；第一步是不先认定对方不可信）。`core/b0_s11.md:13` "cooperate without good will" 加限定（只对核查看得见的部分，且须先有信念让人装设）。`core/b0_s11.md:17` §11.1 第三段：保留 2025 那行（仍作"In the corpus's words"）与必留短语 "Trust is mainly an outcome"；加入调和句"信任不是协调的前提，却是核查起作用的前提"，引 Ren 10-03 "bottleneck" 一句（附中文）与 10-04 [47:25][41:57]（注明编辑译文）。D40 改写、新增 D45；§9 新增第 11 项。[46:20] 已在 §11.3 引用 |
| I3 | 确认（重要） | `core/60_s6.md:103` 加粗判据改为四个析取项（人人采用而各留原位、压下没有它的人；取代本身是工具的人；抬高可转换性、决定性或成功向控制的转化；使博弈加速），保留 "in a competitive game that concentrates"。`reg/CLAIMS.md:408` D19 同步 |
| I4 | 确认（重要） | `core/00_head.md:5` 摘要首句加"为协调而作的预测"，末句加肯定式意义（不重复"不反对增长、竞争"）。§0 段落次序为可选，未动 |
| I5 | 部分成立（重要） | 导读（`core/00_head.md`）：第二层把 E2/保管与 E3 的触发分开、写"停止不是放缓，各有各的指标"（:29）；"在场模型"两处改"在'场'模型"（:24、:33）；狭义 E1 首次出现处加注（:24）；C0 写成"待检验的猜想 C0"（:19）；第 1 条（:16）、第 4 条（:19，含桥接句与"剪刀"引入）按评审改写；第 3 条读不通处按评审改写，主语"母体"按核验意见保留（:18）；用途与意义补劳动替代（:9），首句"讲赢"→"求胜的逻辑"（:9）。`core/30_s3.md:119` §3.8 "calls it" → "names its discourse"；D42 补注并交 Ren。翻译腔各条未改，列入 CLAIMS §9 第 13 项 |
| I6 | 确认（重要） | `core/60_s6.md:23` §6.2：引文前加"here in an edited translation of mixed Chinese and English speech"，英文在删节处加"…"。`reg/CLAIMS.md:405` D16 写明所示中文本身是编辑译文，并附原始转写；`disc/01_X1.md:35` X1 行同步 |
| m1 | 确认 | `core/70_s7.md:35` "the attractor of attractors" → "an attractor of the meta-attractor"（中文原文不变）。`reg/CLAIMS.md:412` D23 记两种读法，交 Ren；`disc/01_X1.md:18` 同步 |
| m2 | 部分成立 | 定义 2.1 不动（按核验）。`core/20_s2.md:93` §2.4 末句 → "Trained AI systems are carriers, and under the conditions of Section 6.4 the pressure and its closure run inside them"。`core/60_s6.md:77` §6.4 → "Trained systems are carriers…; AI lineages come under the pressure themselves when…"。为保持一致，`core/60_s6.md:3` §6 主张框、`core/10_s01.md:25` §1.2 第 5 条与导读第 5 条也由"即是载体"改为"自身处在这一压力之下，其闭合在内部运行" |
| m3 | 确认 | `core/70_s7.md:93` 只引不歧义的片段。`reg/CLAIMS.md:444` §9 第 4 项补记此句；X1 行同步 |
| m4 | 确认 | `core/a0_s10.md:85` "[centralization or decentralization]" → "[inaudible: 'centralization' or 'decentralization']"。`reg/CLAIMS.md:418` D29 改为转写者对听不清语音的标注；X1 行同步 |
| m5 | 确认 | `core/40_s4.md:112` 试验句改为"did not support the mechanism: its first prediction … failed, while the other three held (EV12)"。TSV 中 V61-0388 改记 reworded（见第一节） |
| m6 | 确认 | `core/10_s01.md:9` §0："not to any participant" → "not to growth, competition, technology or any participant"；衰败句后逐字引 "I would look at decay as a form of growth"。`disc/01_X1.md:62` X1 补 [00:57:27] 行。§12.4 一意两说的删改是文体选择，未改（第三节） |
| m7 | 部分成立 | `core/a0_s10.md:38` "a lever, not a concession" → "a lever, within the lines drawn below"；按转写逐字引 Ren 的两个条件（[00:26:09] "as long as there are still this intelligence compounding like dynamics"；[00:27:02–19] 核查使模型不能被微调、训练去做其他危险之事，"definitely the direction. But that direction does not mean execution"），标 [corpus: meta-attractor, 2026-10-02, 00:26:09–00:27:19]，未用 README 转述作"his account"。X1 行同步 |
| m8 | 确认 | V1 按评审改写：`core/10_s01.md:36`、`core/60_s6.md:99`（§6.6 首句）、`core/c0_s12.md:85`（§12.4 短式）。`reg/CLAIMS.md:406` D17 同步并附原话 |
| m9 | 驳回 | 未改。"不夺共续"是语料原文 |
| m10 | 确认 | 句子账重算：低于 0.4 的 100 句，三句新判定、两句回升，V61-0388 改记（见第一节）。`reg/LEDGER.md:156` 起 §3 计数与说明更新。TSV 重生成于 `src/reg/`，待复制到根目录 |
| m11 | 确认 | 同 evidence E7(a)(b)，见下 |
| m12 | 部分成立 | 不加 CLAIMS §9 项（按核验）。`core/50_s5.md:94` "pace binds even a generative order" → "the pace of hazardous scope, not of need-directed growth, binds…"；随后引 Ren 10-03 风险速度一句（全文中文附英文转述，[corpus: possibility-space, 2026-10-03]）与 10-04 [47:35]（编辑译文，[corpus: alignment-selection, 2026-10-04]）。新增 D46 |

### coldread（R-v6.2-coldread）

| ID | 判定 | 处理与位置 |
|---|---|---|
| M1（含 math-I M11） | 确认（重要） | 六处补 (residual floor)，用前提本身的比例形式："the chance of irreversible loss is at least a fixed fraction of the share left uncovered"：`core/00_head.md:5`（摘要）、`core/10_s01.md:24`（§1.2 第 4 条）、`core/50_s5.md:3`（§5 主张框）、`core/50_s5.md:84`（定理 5.13 黑体首句）、`reg/CLAIMS.md:18`；导读第 4 条 `core/00_head.md:19` 写"不可逆损失的概率不低于未覆盖份额的一个固定比例" |
| M2 | 部分成立（重要） | 按核验修法（执行手段不放第一层）。`core/c0_s12.md:26` 第二层 *Commitment*：写明事先承诺本身是对触发时行为的许诺，除非执行手段在触发前已就位（保管持有的休眠硬件限制或托管密钥，推论 5.7(a)；或成功后仍存续的制裁，5.7(b)），否则同一条件约束它，对领先方的启动落到第三层强制兜底；装设休眠手段列入"现在准备"，以通过 D4、D5 为条件。原 [thm∣prem] 的负向句保留。`core/c0_s12.md:5` 主张框 Why 补一句。C4 登记"手段是否在触发前就位"：`core/c0_s12.md:62`、`reg/TESTS.md:16`；C7 的下一测量补硬件控制是否已休眠装设（`reg/TESTS.md:19`） |
| M3 | 确认（重要） | `core/c0_s12.md:15` 第一层（甲）第 4 项删去"并现在作出启动承诺"，改为设计、机构、指标、启动规则登记并按 D1–D8 压力测试，"启动承诺属第二层"；承诺移入第二层 *Commitment*，以保管通过事先登记的压力测试为条件（`core/c0_s12.md:26`）。导读第一层（甲）`core/00_head.md:27` 删"启动承诺"，第二层补条件。`reg/TESTS.md:46` 第 (4) 项描述同改；`reg/TESTS.md:65` 补"启动承诺会停止东西，属第二层，C4、C10、N1 作用于它" |
| M4 | 确认（重要） | `core/20_s2.md:58` 首次出现处分三义：(a) 给竞争者的能力供给 k₀，经 ω，[thm]；(b) 给人的体面生活供给，只在进入竞争者决定性存量时经 ω，否则经驱力（C8）[conj] 或赌注；(c) 多家提供的基本服务，经依赖上限与资助的备用（X8，D5）。`core/80_s8.md:46` G5 注明限于 (a)、否则经驱力；`core/c0_s12.md:21` 第 8 项的 [thm] 只挂 (a)，(b)(c) 各写作用途径 |
| M5 | 部分成立（重要） | `core/50_s5.md:3` 主张框：联合模型的合拢写成有条件的（决定性高到贴现增益可近于一时合拢；扩散使增益远低于一时不合拢），"one reduced model" → "two reduced models"。`core/50_s5.md:125` §5.5 Scope 同改，政策读法写成条件式（检测及时且 D=C 时供给是主要杠杆；时钟慢且 D>C 时检测速度也移动门槛，至多 0.13）。`supp/05_S5.md:139` S5.2 补 26/96 慢时钟设定、r 扫描（r=1 永不；r=1.5 仅无扩散、约 0.95；r=1.7、δ_f=0.05 为 0.975）、Γ_δ≥0.924 的解析原因 [num: VF/JX]。未断言现实处于不合拢区 |
| M6 | 确认（重要） | `core/c0_s12.md:34` 理由 (i)：不对称改写为"一旦发生，有点名而未经验证的逆转（C4）"对"一旦发生，没有逆转"，两侧是否发生都取决于分歧（续行：C1、C2、C5；设计：C4），排序对设计自身风险的依赖是 C4（§8.1）。每项损失的 [thm∣prem] 与排序的 [val] 保留 |
| M7 | 确认（重要） | `core/70_s7.md:104` §7.4 新增 "The strongest counter-reading"（Narayanan and Kapoor 2025；Ding 2024），落到 C1、C5 与 Branch III。`core/80_s8.md:93` §8.3 新增 (h)；`core/80_s8.md:107` §8.4 表加一行；`disc/08_X8.md:84` X8 新增一节（最强形式、剩下什么、改变什么、什么能证明足够）；`reg/TESTS.md:12`、`:17` C1、C5 现有证据栏补入。两部文献的记录已核：Knight 研究所页面（标题、作者、日期，"impact … materialized … diffused"、"reject nonproliferation … decreases resilience" 两句）与 Crossref（Ding 2024，普林斯顿大学出版社）；"不存在决定性优势"一点页面摘要未能逐字确认，故正文只写"按此读法前沿领先本身不是决定性的" |
| M8 | 部分成立（重要） | `core/10_s01.md:7` §0 与导读 `core/00_head.md:9` 改用本文判据（竞争动态且趋于集中之处，在模型中即再投入相对回报超过共同回报之处，需逐个市场表明）。`core/60_s6.md:103` §6.6 加一句回应产业组织反方（"留在原位"说的是地位不是福利；增长奖金且 (1−β)r<1 时向前看放宽自我，命题 3.9(2)；劳动处引 Acemoglu and Restrepo 2019）。未采用评审"奖金不随人人采用而增长"的错误条件 |
| m1 | 确认 | **未插入**：两种读法都写入 CLAIMS §9 第 12 项（`reg/CLAIMS.md:452`），由 Ren 选 |
| m2 | 部分成立 | `core/50_s5.md:3` 主张框"加速"改为"随赌注增长"，并以命题 3.6(1)、5.15 与 Remark S2.1 为据。`core/c0_s12.md:81` §12.4 "success raises the stakes" 改为"随赌注增长……；奖金随所有人再投入而增长处，成功本身抬高赌注（命题 3.9）"，"accelerates" 前加"as the stakes grow"。另 `core/10_s01.md:24` §1.2 第 4 条与导读第 4 条同加"随着赌注增大" |
| m3 | 确认 | `core/10_s01.md:26` "therefore cannot justify" → "cannot, on V1–V3, justify"；导读第 6 条 `core/00_head.md:21` 加"依 V1–V3" |
| m4 | 部分成立 | `core/a0_s10.md:21` 命题 10.1 补"每人按自身努力付 c、按总强度承担 ℓ（如第 3.4 节）"与"对每个对手的信任 = 其各自独立合作的概率"；`supp/10_S10.md:11` 同步。遗留来源已有注明，未加 |
| m5 | 确认 | `core/20_s2.md:60` §2.2 定义一次"what winning confers"（β；κ 对 k₀；扩散；χ；奖金是否地位性），降低 r 列为同一博弈上的并列杠杆，"a change of the game" 指二者。`core/30_s3.md:3` §3 主张框 → "only a change of the game, in what winning confers or in its decisiveness, corrects it" |
| m6 | 确认 | 加"for a deviation whose decisive position is worth more than punishment"：`core/00_head.md:5`（摘要）、`core/50_s5.md:27`（命题 5.4 黑体首句）；同步 `core/10_s01.md:24`、`core/50_s5.md:3` 与导读第 4 条 |
| m7 | 确认 | `core/a0_s10.md:3` §10 主张框拆开："更好地优化同一目标纠正不了它" [thm∣prem]；"不必废除选择、竞争、增长" [val] |
| m8 | 确认 | `core/30_s3.md:11` host："…in no parasitic sense: the part of…" → "…in no parasitic sense; in the models, the part of it whose costs do not return…" |
| m9 | 部分成立 | `core/80_s8.md:35` 出口管制句后补量级，带全部限定（示例值、无分享、无供给、扩散对称；定向管制只部分阻断、且只对对手），指向 Remark S2.5；未称"现有扩散率" |
| m10 | 确认 | `core/40_s4.md:51` 命题 4.5 Scope：门槛对边际成本的正则变化同样成立（η 为渐近弹性），以严格不等式陈述，等号由慢变因子决定；比任何幂都陡的边际成本下任何正的纠错增长终究足够，可能先有过渡失效；标 [thm]。`supp/04_S4.md:41` 新增 *Beyond the power law* 证明（含 q/ln(e+q) 等号反例、指数型情形；并说明此时只断言"从某日起"），引 Bingham, Goldie and Teugels 1987（Crossref 记录已核） |

### evidence（R-v6.2-evidence）

| ID | 判定 | 处理与位置 |
|---|---|---|
| E1 | 确认（重要） | `core/b0_s11.md:25` §11.2 改为"私有风险、由胜者承担；选择更随竞赛状态而非风险偏好；设计未检验共有风险，作者自己说明"。`reg/EVIDENCE.md:197` EV11 照实登记：私有风险；预注册 0.6 对 0.9 无差异；补做的 0.1 组显著更少不安全（p=0.0272、0.0161）；竞赛状态效应属探索性；引作者局限原句；注明此前误读。`reg/TESTS.md:18` C6/C8、`reg/TESTS.md:188` Study 5 同改（共有风险处理填补此缺口） |
| E2 | 确认（重要） | `core/60_s6.md:55` "with no race and no misaligned system" → "without a sudden jump in capability, a coordinated bid for power or a misaligned system, through the competitive pressure on firms, and on states to keep relative power, to adopt it"。`disc/01_X1.md:136` X1 同步（可选项一并做了） |
| E3 | 确认（重要） | `core/70_s7.md:83` T1 行只写角色："conduct not shown … how it came out is not known" → "conduct shown in one reported case: … and state investors of the kind it weighed took part in the developer's next financing rounds"。`reg/EVIDENCE.md:40` EV1：删"是否接受投资未记录"，记 Series F（2025-09-02，一手页面列 QIA，‡ page）、Series G（2026-02-12，一手页面：MGX 共同领投、QIA 为重要投资者，‡ page）、Series H（2026-05，据报道两者再投，一手页面未取到，† not retrieved）；注明其他开发者同类资本本轮未记、按同一标准应记。`reg/EVIDENCE.md:18` Disclosure 清单补入。Reading 段同步 |
| E4 | 部分成立（重要） | "evidence that behaviour does not control" → "controls less directly"：`core/40_s4.md:77`（Remark 4.9）、`supp/04_S4.md:80`（S4(3)）、`core/60_s6.md:73`（Remark 6.8 后一段）、`supp/06_S6.md:78`、`reg/EVIDENCE.md:142`（EV6）、`core/90_s9.md:19`（表 9.1 R6）、`core/c0_s12.md:25`（*Estimator*）、`reg/TESTS.md:142`（触发条款）、`disc/08_X8.md:139`（风险表）、`supp/09_S9.md:13`（S9 R6）、`supp/07_S7.md:119`（S7 矩阵），以及 `reg/CLAIMS.md` alarm 行、`reg/README.md:30`。Remark 4.9、S4(3)、EV6 写出各通道的限度（Goldowsky-Dill：尚不稳健；Bailey et al. 2024：针对探针优化可混淆激活；McGuinness et al. 2025：微调后的模型可零样本躲过未见过的监测器；Greenblatt, Roger, Krasheninnikov and Krueger：隐藏能力超过示范者时可能失效），并加"能在多大程度上界住掩蔽是 C12"。Bailey、McGuinness 两条 arXiv 记录已核，入 THEORY、SUPPLEMENT 文献表。已点名 C12 的段落未重复加（按核验） |
| E5 | 确认 | `core/60_s6.md:77` 拆成两句：内部使用已有早期公开迹象 [obs]；最可能受压的系统预期先在内部部署 [prem]。`disc/01_X1.md:135` X1、导读第 5 条、§1.2 第 5 条同步 |
| E6 | 确认 | `core/80_s8.md:58` §8.3(b) 与 `disc/08_X8.md:15` X8 Best case："the unique equilibrium of a capability race" → "the unique Markov perfect equilibrium of a two-developer capability race" |
| E7 | 确认 | (a) `core/60_s6.md:55` "hidden loyalties" → "singular or secret loyalties"（审计一句改"secret loyalties"）；(b) `core/60_s6.md:79` "(Turner et al. 2021)" → "(compare Turner et al. 2021)"；(c) Powell 1991 两处按 X1 读法改写，共通道推广标为本文自己的添加：`core/10_s01.md:52`（§1.4）、`core/30_s3.md:82`（§3.5） |
| E8 | 确认 | `core/60_s6.md:67` "user feedback" → "simulated user feedback" |
| E9 | 部分成立 | `disc/01_X1.md:114` 按核验者修正后的措辞改写（"drift toward greater joint payoff … among several effects; a self-reinforcing pattern of effort costs can make the laggard work harder even where the other effects favour the leader"） |
| E10 | 确认 | 核心 §6.5 补一句引 Khan et al. 2024、Kenton et al. 2024（`core/60_s6.md:93`，内容按两篇 arXiv 摘要），T2 行补 (Zhu 2026)（`core/70_s7.md:84`）；三者因此进入 THEORY 文献表，xref 不再报登记册未解析 |
| E11 | 确认 | `core/60_s6.md:61` "more so with capability and situational awareness … each has been shown" → "in some studies more so with capability or situational awareness … each tendency has been shown"；`core/60_s6.md:3` 主张框 Why 同步。可选的 Chaudhary et al. 2025 未加（原有梯度主张已删） |
| E12 | 确认 | `disc/11_X11.md:70` 按核验者措辞改写（1948 年以前库存小；1949 年起优势大但在流失） |
| E13 | 驳回 | 未改 |
| E14 | 部分成立 | `core/b0_s11.md:95` 按核验者措辞改写（"biological-weapons record … as one party did before the 1972 Convention …, and, under a convention without verification, that a covert programme can persist"） |
| E15 | 确认 | (a) `reg/EVIDENCE.md:37` EV1 补另一开发者首席执行官 2024-07-25《华盛顿邮报》文章（报道核实，原文未取到，† not retrieved）；(b) `reg/EVIDENCE.md:38` 恢复 "We believe"；(c) `reg/EVIDENCE.md:78` EV3：§5(a) 使有"onerous"州法的州失去 BEAD 非部署资金资格，§5(b) 指示各机构评估是否以州法为可酌情拨款的条件 |
| E16 | 部分成立 | `src/refs_v62.py`：图例补"identifier"（v6.0 证据评审核过存在与标识、未记读了什么）与"not retrieved"含 v6.0 带来而无核对记录者，并允许分号后附注；新增 `legend_form()`：裸 † → "† (not retrieved)"，裸 ‡ → "‡ (identifier)"，四种图例外写法映射到图例形式（"(pages per the v6.1 evidence review)"→"(record)"，"‡ (abstract record)"→"‡ (abstract)"，"(record of the volume)"→"(record)"，"‡ (full text and page)"→"‡ (full text)"）。按核验意见不用"‡ (record)"。Kulveit 补 PMLR 267:81678–81688；Thornley 补"182(7):1653–1680, 2025 (online 2024)"（引文年份 2024 不变）；Weitzman 1974 补页码并标 † (record)（Crossref 核过首页）。三份表裸标记现为零 |

## 三、需要 Ren 决定的事项（未替他决定）

1. **E2/E3 由什么启动**（I1；CLAIMS §9 第 10 项，D43、D44）：(a) 由广义 E1 未达成启动（他 10-03 的条件）；(b) 由预测触发启动（现行）；(c) 两者并用。导读第二层与 §1.2 第 9 条要随他的答复改；§7.2 "a preparation, not an emergency" 是否软化也随之定。
2. **信任的调和句**（I2；§9 第 11 项，D40、D45）：确认或改写"信任不是协调的前提，却是核查起作用的前提"。
3. **"if growth and change are favoured" 为何附此条件**（coldread m1；§9 第 12 项）：两种读法，他选后再插入。
4. **导读的语感**（I5；§9 第 13 项，D41）：七处翻译腔改法，以及第 3 条末句主语用"母体"还是"竞赛"。
5. **讲赢**（I5；D42）：是否继续以 "the logic of winning" 兼指讲赢与整个求胜逻辑。
6. **"一个 meta attractor 的 attractor"**（m1；D23）：两种英译读法。
7. **§7.3 那句 "if we don't believe"**（m3；§9 第 4 项）：开头是否笔误。
8. **新渲染待确认**：D43–D46（10-03 次序、10-04 三句、信任与 bottleneck、风险速度一句与 [47:35]）。
9. **可选、未做**：§0 把意义段前移（I4）；§12.4 删去与 Ren 原话同义的改写句（m6）；Chaudhary et al. 2025（E11）；Fuhrmann–Kreps 补计数（E13 驳回后的可选项）。
10. **篇幅**：核心由约 56.2k 增到约 59.6k 词，导读由 2,650 增到 3,168 字。篇幅已由 Ren 接受，此处只报告。
11. **TSV**：`src/reg/LEDGER-v62-sentences.tsv` 需复制到根目录，替换旧 TSV（可写范围外，未代为复制）。

## 四、查了什么，没查什么；同族偏差

- 每条新加的数字都有核对：VF 块 14 条断言（纳什迭代、逐期加总、模拟、数值雅可比、网格最大化、蒙特卡洛），外加 SM(12)、AL(6.11) 重写。核对前我先在草稿区独立写脚本复算（`fix/m1_timing.py`、`m2_rpr2.py`、`m5_sweep.py`、`m7_td.py`），再移入检查文件。M2 的静态反例我起初误把对手响应取为"本方固定时对手之间的均衡"，结果与核验者不符；改为"对手在新状态下的全纳什策略"（包络定理所用的那一种）后完全一致，正文按后者写。
- 新文献：Bailey 2024、McGuinness 2025、Khan 2024、Kenton 2024、Zhu 2026、Chaudhary 2025 经 arXiv API 核记录；Acemoglu and Restrepo 2019、Ding 2024、Bingham et al. 1987、Weitzman 1974 经 Crossref；Narayanan and Kapoor 2025 与开发者的 Series F、Series G 公告经页面抓取（工具会做摘要，引句按逐字要求取得）。Series H 与华盛顿邮报文章只核到报道。
- 引 Ren 的中文原话都对照了来源：10-03 的两段（`sources/16-claude-code-directions/2026-10-03-v4-direction-cooperation.md`）、10-04 译稿（`drafts/2026-10-04-soi-si-lom-5-2/translation-zh.md`）、10-02 转写（`drafts/2026-10-02-friend-conversation/transcript.md` [00:26:09]–[00:27:19]、[00:57:27]、[01:03:44]）。
- 没做：没有请家族外读者复核；没有重读全部 SUPPLEMENT 与 DISCUSSION 去找同类问题（只按发现所列位置与 grep 同义句处理）；E3 的同标准要求（其他开发者的主权资本）未补查。
- **同族偏差**：我与起草者、评审者同属一个模型家族。最可能起作用之处：(1) 对 Ren 的话作英文转述与映射（如把他的次序对到 E1/E2/E3），这是起草方的读法，已全部登记为 D 项；(2) 导读中文由我改写，仍是模型中文；(3) M1、M2 的时序与"对手响应"读法由我选定，家族外读者可能另有读法；(4) E3 涉及起草模型的开发者，本轮按披露原则补记了不利项，但同类遗漏可能系统性偏少。
