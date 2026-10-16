# X-G2 复核：G2 论文架构的事实与推荐

*2026-10-03 夜。Claude Opus 5.5 独立复核 `G2-paper-architecture.md`（Fable 5.1）。读过：G2；v6 §4 与附录 A.4；v2 `submission/main.tex` 与 `NOTES.md`；round-2 四份评审与综合；v6 七份评审与综合；G1、G3；v3 `reviews/MATH-CHECK.md`、`R-v3.1-external-handoff.md`；v5.2 systems 评审；09-28 论文；`experiment/`；`build/carrier.py`。联网核对了 OpenReview API、IASEAI'27 投稿指南和 AAAI 出版政策。核算脚本在 scratchpad 的 `xg2/chk.py`。没有改动任何既有文件。*

## 结论

1. **方向成立。** 以 v2 为骨架，加入 V6 §4 的部分结果，是现有材料里最稳的一篇。G1、G3、v6 综合和我的判断一致。
2. **G2 的核心事实说法不成立。** 命题 4.2(2)、4.4、4.10 从未进入 v2，round-2 没有审过它们。审过它们的是 v3 数学核对、v3.1 外部评审和 v4/v5 各轮，全部是 AI 评审。v6 数学评审明确没有审 §4。
3. **移植不是照搬。** 有两处要重新推导，或者改模型：
   - 成本结构（按载体计还是按决策计；$f>0$ 还是 $f=0$）。它决定 $\sqrt{\cdot}$ 阈值、$k^{2/\eta}$ 和三阶矩是否成立。v2 的仿真和试点用的是另一种成本。
   - 记号冲突。
4. **摘要有五处超出所证。** 详见"推荐是否成立"一节。
5. **按"质量先于截止"，IASEAI'27 只能是条件满足才投。** 先跑设计 2、定下成本结构、做家族外核对。这些在 10/5 中午前全部做完，可能性低。

## 事实核对表

| G2 的说法 | 判定 | 依据 | 备注 |
|---|---|---|---|
| 推荐论点"每条承重结果同时通过了 v2 的两轮论文评审和 v6 的七份评审"（§0 第 1 条、§1 表"承重结果"行） | 不成立 | v2 `main.tex` 里没有暂停、速率律、拆分和三阶矩（grep 核过）；round-2 只审了 Props 1–6 和 Cors 1–3（`reviews/round2/SYNTHESIS.md`） | round 1 审的是 v1，v1 没有 Props 2–3 和 Cors 1–3，所以 v2 的核心结果也只过了一轮 |
| 4.2(2)(4)、4.4、4.10 经过核对 | 部分成立，出处写错 | v3 `MATH-CHECK.md`（Prop 3、Prop 5、附录 B 的 Prop 9 暂停）；`R-v3.1-external-handoff.md`（"Proposition 5 的长期公式…可作为论文的主要结果"）；v4.3/4.4 math；v5.2 systems（3.6(7)(8)、3.12） | 这些核对发现过真错误：$f>0$ 那句是错的；$k$ 应为 $k^2$；"certified" 需要整行；"cannot invade from rarity"有歧义。v6 改掉了大部分。核对者全是 AI，没有人类数学家 |
| v2 结果"四位评审逐行核过证明，三方独立复现数值" | 基本成立，需限定 | round-2 SYNTHESIS："The proofs are correct"；R1、R2、R4 各自写代码复现了数值 | 同一轮评审也判定：加入成本后 Prop 3 不成立（R2 W2，MAJOR）；图 2 没有实现式 (3)。复现的是一个没有实现模型的仿真 |
| 七份 v6 评审对 4.2–4.10 都没有致命或重要发现 | 字面成立，含义不成立 | math 评审的对象清单不含 §4；Codex 说明自己"not a certification of all 85 numbered results"；只有 systems 读了 §4 和 A.4 | systems F4 指出 4.10 之后的驻留时间低估 2–16 倍，且份额先升后降（G2 已吸收）。Codex（第 1368 行）和 alignment 都指出行和证书不证明错误独立。G1 明说 4.4(3)–(8) 还需一次独立数学审读，G2 的说法与之相反 |
| §4"从 v2 到 v5.2 到 v6 一直稳定" | 不成立 | 速率由 $g/2$ 改为 $g/(1+\eta)$；拆分因子由 $k$ 改为 $k^2$，再改为 $k^{2/\eta}$；$f>0$ 那句被判错后改写为 4.4(5) | 只有最近两版是稳定的 |
| 4.2(2) 就是"容量不能从稀有入侵"的定理形式 | 部分成立 | 4.2(2) 要求 $f>0$，且成本按载体计；round-2 的数值和试点用的是按决策计的线性成本 | 两种设定的阈值标度不同：按载体计是 $\sqrt{f/\cdot}$，按决策计是 $\gamma\delta/(ab\chi)$，线性 |
| "助手降低转化成本"有已核实的文献 | 不成立 | v2 NOTES："AI channel is a hypothesis about magnitudes"；v6 EVIDENCE 的 EV4："No source was retrieved" | 这正是 4.4 的前提：$\gamma(t)$ 随 AI 下降 |
| v2 必修 1（图 2）和必修 2（棘轮）已计入日程 | 基本成立，漏一项 | round-2 必修 1、2；R2 W2 | 漏了聚合的第三个前提：代表性生产，它只在单一主导谱系时成立。按自身份额重跑后，$\chi$ 阈值约为 0.55，$\chi=0.3$ 和 $0.5$ 都失败，从 1% 起步一律失败。v2 摘要里"仅靠容量选择就能把场推过阈值"一句必须改写 |
| OpenReview 截止 2026-10-06 10:59 UTC（曼谷 17:59） | 成立 | [OpenReview API](https://api2.openreview.net/invitations?id=IASEAI.org%2F2027%2FConference%2F-%2FSubmission)：duedate 为 10:59Z，expdate 为 11:29Z。网站写的是 5 Oct AOE | OpenReview 比 AOE 早一小时 |
| 账号审批可能要两周 | 成立 | [投稿指南](https://docs.google.com/document/d/e/2PACX-1vR_hLJSEv5WZF66P2HPg8zvezNttnaHvuekFJGdam3gYBMJu57ma2iKeXJKl_DHF4oCuJZ7CLc-IE3d/pub)；会议页 | 会议页要求所有作者在 9 月 18 日前已有账号 |
| 10 页、AAAI 套件、双盲、贡献声明 | 成立 | 投稿指南 | 正文至多 10 页，不含参考文献；图表计入页数；附录不计，审稿人也不必读；贡献声明须"situates the work with respect to earlier published versions without naming venues or authors" |
| archival 要求"无平行评审，形式内容全新" | 大体成立，说得偏严 | 指南：至少 50% 的技术内容是新的；评审期间不得在其他 archival 场所受审。non-archival 须向 PC 披露既往发表 | — |
| "archival 要求亲自到场；不确定能否到场就选 non-archival" | 不成立 | 指南："Virtual presentation options will not be available"；archival 论文须有作者注册、到场并报告，才收入论文集 | 两条轨道都没有线上报告，选 non-archival 解决不了到场问题。会期是 2027-02-09/10 |
| AI 协助"评审指南未规定" | 字面成立，有遗漏 | IASEAI 指南确实没有 LLM 条款。但 IASEAI'26 论文集由 [AAAI Press 出版](https://ojs.aaai.org/index.php/IASEAI/issue/view/741)，[AAAI 政策](https://aaai.org/aaai-publications/aaai-publication-policies-guidelines/)规定："use of any AI system … only allowed if its role is properly documented in the manuscript" | archival 定稿必须在文中说明 AI 的作用，作者对全部内容负责 |
| archival 接收概率约 45% | 无法核实 | 这是 round-2 同族 AI 评审对"v2 修后"的主观估计；G1 认为偏乐观 | 它不是对 v2+ 的估计 |
| 录用率约 19% | 部分核实 | AAAI OJS 显示 IASEAI'26 论文集收 57 篇 archival 论文 | 300 篇投稿这个数没有核实 |
| （G2 未提及） | 遗漏 | OpenReview 表单有一个必勾项：须经 IASEAI 门户进入且已有门户账号，否则"may be desk rejected" | 门 0 应加上这一项 |

## 推荐是否成立

**方向成立，但移植要做实事。**

1. **成本结构。** $p^2$ 回报来自"转化自身的成功"，这一点是稳的。$\sqrt{\cdot}$ 阈值、拆分因子 $k^{2/\eta}$、"三阶矩而非 HHI"三条结论，都要求能力成本按载体计，不随规模增长。
   - 若成本按决策计（v2 `carrier.py` 写的是"cost 0.05 per decision"，试点是"gamma*q_k per decision"），阈值是线性的，拆分因子是 $k^{1/\eta}$。$\eta=1$ 时，集中度的度量恰好是 HHI：两个等份额载体的培育转化是垄断时的 1/2，而按载体计是 1/4（`chk.py`）。
   - 所以 4.4(8) 是一个以成本结构为条件的结果。如实写出来反而更有价值：哪一阶矩决定俘获，取决于影响成本是否随规模增长。这一点本身可以检验。
2. **$f$ 的张力。** 4.2(2) 的规模阈值要求 $f>0$。4.4(3)(7) 的速率律和"拆分只延迟"要求 $f=0$，或者 $f$ 也在下降。
   - $f$ 固定时，拆成 3 份就能把每一份都压到阈值以下，拆分的效果是永久的。核算结果：垄断时 $s_{\mathsf E}$ 随 $\gamma\to0$ 发散，拆分后一直停在 0.05。
   - v3 MATH-CHECK 6.6 已经指出过同一张力。
3. **准静态假设。** 4.4 假定能力瞬时等于 $q^\ast(d(t),\gamma(t))$。没有一次让能力随选择演化的联合仿真。
4. **记号。** v2 的 $\zeta$ 是可占有的支持存量；v6 的 $\zeta$ 是采纳速率（4.10 的 $\varepsilon/\zeta$ 用的就是这个）。$r$/$z$、$\kappa$/$\zeta$、$W$/$\Delta\pi$、$T$/$T_h$、$\beta$/$m$ 都要统一。证明要按 v2 的记号重写：不需要新证明，但文本是新的，要重新核对。
5. **4.10 的来源。** 4.10 就是 09-28 论文的 Prop. 10，那篇论文的摘要里几乎有同一句话。它与 v2 的 $D=1$ 模型相容：我核过 Lyapunov 函数沿解不减，随机抽 1 万个点，0 例违反。但这个结果归哪篇论文，要先定。

**摘要有五处超出所证：**
- "cannot invade from rarity"：只在存在固定成本或按决策计的线性成本时成立。
- "grows … with its scope"：只在每个域的份额固定时成立。固定总规模时还需要 $\hat\varphi>\hat\eta$，这正是 round-2 必修 3 纠正过的那句话。
- "splitting … without preventing it"：需要 $f=0$ 或 $f$ 下降，需要 $\alpha<g/(1+\eta)$，还需要成本按载体计。
- "a pause … completes capture unless rule-making is insulated"：
  - 只有冻结份额高于 $1/R$ 时，暂停才完成俘获。
  - 隔离只在份额低于 $\sigma(0)$ 时才能解除俘获。$\varepsilon=\zeta$、$R=2$ 时 $\sigma(0)\approx0.68$（我复算的）。
  - 这是 $D=1$ 的模型。
- "tests that separate"：唯一一次试点里，失败的恰恰是区分"控制"与"规则自行变化"的那条预测（P1，REPLAY 组）。

检测延迟那句也应加上"在固定的平均报警之下"。

**另有一处违背 G2 自己的规则。** G2 说只放入没有争议的结果，大纲却放入了 Prop 6.7 的窄形式和 Lemma 3.3 的一句。这两条都有待修的重要发现，应删去，或标为假设。

## 遗漏的风险

1. **作者责任。** v2 和 v6 的结果 Ren 都还没有审读过（NOTES 写明；CLAIMS 多标 D）。双盲之下审稿人看不出这一点，但作者必须能为每一条证明辩护。AAAI 政策还要求在文中说明 AI 的作用。G2 只写了"正式稿由 Ren 定"，低估了这件事。
2. **重叠。**
   - 4.10 与 09-28 论文重叠；v3/v3.1 和 v6 共用 §4。
   - 只要其中任何一篇公开或另投，archival 轨道的"50% 新内容"和贡献声明都要处理。
   - G2 写"自引要么第三人称，要么不引"，其中"不引"不可取。
3. **试点。**
   - 失败的 P1 恰是区分性的那条预测。
   - 试点是对模型本身的仿真，不是经验实验。
   - "预注册"只是本地带时间戳的文件，论文里应写"pre-specified"。
   - 试点的成本结构与 4.2(2) 不一致，审稿人看得出来。
4. **门的次序。** G2 把家族外核对放在 D 门之后（10/5 下午），应放在门之前。
5. **到场与门户账号。** 见核对表。
6. **页数。** 9.7 页的预算没有经过实际编译验证。本机没有 TeX。
7. **证书的读法。** 行和小于 1 证明的是没有俘获，不证明错误独立。AI 一节和设计原则里要写"必要而非充分"。

## 我的建议

按下面的顺序做，不以截止日为锚：

1. **今晚过门 0。** 三项：OpenReview 账号；IASEAI 门户账号；2027-02-09/10 能否亲自到场。任何一项不满足，就不投 IASEAI'27，这没有损失。
2. **先跑设计 2。** 纯 Python，约几小时。按 `PREDICTIONS-2.md` 跑，不改预测，结果照写。
3. **定下 §4 的成本结构。**
   - 写一个假设框，分别推导按载体计和按决策计两种成本下的阈值、拆分因子和集中度度量。
   - 速率律写成"整套控制成本都下降时成立；固定部分不降时，只需要一个水平"。
   - 图 2 和试点改用同一种成本。
   - 这一步同时修了 V6 §4。
4. **改完 v2 的必修 1–10。** 包括写明代表性生产这一前提；按 $\chi$ 阈值约 0.55 改写摘要；文献逐条联网核实。
5. **移植。** 放入 4.2(1)(2)(4)、4.4(1)(2)(3)(5)(7)(8)、Def 4.1、Remark 4.7(1)(2)。4.10 等归属定了再以带条件的注记放入，或者留给 09-28 论文。能做的话，加一次 4.4(3) 的联合仿真。
6. **家族外核对放在任何去留判断之前。** 请 Codex 核，最好再有一位人类读者。Ren 要通读全文和证明。
7. **摘要逐句对到结果。** 修上面列出的五处。
8. **最后决定投不投。** 1–7 全部通过，才在 OpenReview 截止前上传。否则转投 2027 年的场所（要求另核），并加一个经验锚点：T-B 的公开评论编码，或用 LLM 裁判面板估计 $\beta$。
9. **理论 V6.1。**
   - 按 SYNTHESIS-v6.0 第七节的顺序修 5.7、5.16、3.3(2)、3.10、5.3/8.6(3)、5.14 和 7.10。
   - 把第 3 步并入 §4。
   - 然后交 Codex。

第 3 步论文和理论共用，应最先做。
