# R-v6.2 评审：证据与引文

*对象：`v6.2/` 的 THEORY.md、SUPPLEMENT.md、DISCUSSION.md、EVIDENCE.md（EV1–EV18）、TESTS.md、CLAIMS.md，以及 `planning/` 中的 D4-evidence-notes、x1-notes、registers-notes、final-build-notes。对照 `../v6.1/` 的三份文献表与 `../v6.1/reviews/R-v6.1-evidence.md`。评审者是 Claude（Opus 5.5），与起草者同属一个模型家族（见第六节）。日期：2026-10-04。*

*核对方式。*
- *【全文】* 取得 PDF，用我自己写的纯标准库抽取器（`/private/tmp/claude-501/v62verify/evidence/pdftext.py`、`pdftext2.py`）抽出全文后逐句检索。Jones (2024)、NBER w35276、RSP v3.0、OpenAI Preparedness Framework v2 用这种方式。
- *【记录】* arXiv API 与 Crossref API 返回的书目记录与摘要，脚本见 `parse.py`、`crossref.py`、`crossref2.py`。
- *【页面】* WebFetch 取得的网页。这个工具会先做摘要，我要求它逐字引用，但仍可能有转述误差。
- *【知识】* 凭书目知识核对，没有联网。

*脚本均在 `/private/tmp/claude-501/v62verify/evidence/`：*
- `refdiff.py`：比对 V6.1 与 V6.2 的三份文献表；
- `cites.py`、`ctx.py`：双向核对正文引用与文献表，并取出引用语境；
- `ess_tullock.py`：Tullock 竞赛有限群体 ESS 的完全耗散；
- `arith.py`：EV9、EV10、Jones 与 Wald 界的算术。

---

## 一、总判断

1. 本轮新增的文献（三份表合计约 70 条，另有登记册专用的约 10 条）都真实存在。作者、年份和出处，除个别格式问题外都准确。没有发现编造的文献。2024–2026 年对齐文献的转述大多忠实于原文，Jones (2024) 的误读也已彻底改正。
2. 有四处【重要】问题，都属于正文或登记册把来源说成了它没有说的话：
   - Fernández Domingos 与 Han 的实验改变的是**私有**风险，不是共有风险，而且风险水平确实影响了选择。正文 §11.2 把它当作"共有风险几乎不改变行为"的观察来用。
   - Kulveit et al. (2025) 的机制恰恰是竞争压力，正文 §6.3 却说成 "with no race"。
   - 正文 §7.3 的 T1 行说起草模型开发者那份海湾资本备忘录"结果不详"。该开发者 2025-09-02 的融资公告已列出一家海湾主权基金。这是对称标准下一项对该开发者不利的遗漏。
   - 被掩蔽偏差的准入依靠"行为控制不了的证据"（权重、激活、微调诱出），而所引的三项来源都明确写出了这些渠道的局限。
3. 本轮没有【致命】项。四项都可以在原句内修好，不动定理，也不动三层判断。
4. EVIDENCE 中正文所依赖的各行（EV1、EV2、EV4、EV5、EV6、EV8、EV11），除上面 Fernández Domingos 一条和 T1 的遗漏外，我逐条核到的引文都逐字无误，正文对证据强度的表述也基本得当。§11.5 与 X11 的先例大体准确，有两处次要的史实精度问题。正文中没有点名任何国家或企业。

---

## 二、发现

### 【致命】

无。

### 【重要】

#### E1 Fernández Domingos 与 Han (2026)：实验里是私有风险，风险水平也有显著效应；正文与登记册都写成"共有风险几乎不改变行为"

**位置。**
- THEORY §11.2 第二段："in an idealized experiment, falling behind drove unsafe choices while the stated level of shared risk changed them little, a finding of exploratory analysis (EV11) [obs]"；
- EVIDENCE EV11 第一条："the pre-registered comparison across levels of shared risk was not supported; … the stated level of shared risk (10% to 90%) changed them little"；
- TESTS C6/C8 一行，以及 Study 5。

**依据。**
- arXiv:2607.26034 摘要【记录】："Unsafe development gave faster progress and higher immediate payoffs but accumulated **private** risk up to a treatment-specific maximum of 10%, 60%, or 90%"。
- 正文 HTML【页面】："Private setback risk applies to players who win the race or tie for first place. If a setback occurs, the affected player loses the payoff from the task." 对手不受影响。
- 预注册的比较只有 prmax=0.6 对 0.9，结果无差异（Bonferroni 校正后 p=1）。
- 后来加做的 0.1 组与两个高风险组差异显著："Unsafe play is significantly higher in the prmax=0.6 and prmax=0.9 treatments than in the prmax=0.1 treatment (prmax=0.1 vs. 0.6: t=2.635, p=0.0272; prmax=0.1 vs. 0.9: t=2.811, p=0.0161)"。作者的演化模型复现的正是这一 "treatment effect"。

**问题。**
- 这项实验没有检验共有风险，所以不能拿来说明本文的机制，即相对选择看不见共有损失（Lemma 3.3）。
- "10% 到 90% 几乎不改变"也不成立：只有 60% 与 90% 两组之间几乎无差别。
- 这个误读偏向本文的论点，而且是 [obs] 标签下的经验陈述。它从 v5 一路沿用（"Checked 2026-10-03"），V6.1 的证据评审没有发现。

**修法。**
- §11.2 改为："in an idealized laboratory race in which unsafe play carried a private risk of losing one's winnings, choices tracked the state of the race, falling behind and a rival's unsafe move, more than risk preferences, an exploratory finding that does not test shared risk (EV11) [obs]"。
- 如果这句话只是用来说明"改变预测不够"，也可以整句删去，因为 Fey and Ramsay 之后的论证不依赖它。
- EV11 照实登记：私有风险、由胜者承担；预注册的 0.6 对 0.9 无差异；补做的 0.1 组不安全选择显著较少；落后与对手的不安全选择预测不安全选择（探索性分析）。
- TESTS C6/C8 和 Study 5 一并改。Study 5 设计的共有风险处理，正好可以说成填补这项实验的缺口。

#### E2 Kulveit et al. (2025) 被写成 "with no race"，而其机制的核心正是竞争压力

**位置。** THEORY §6.3 "*Us:*" 一段："where AI lowers that dependence, it does so with no race and no misaligned system (Kulveit et al. 2025)"。

**依据。**
- arXiv:2501.16946 与 ICML 2025 position track（PMLR 267:81678–81688）【记录】。
- 正文【页面】："firms will face intense competitive pressure to adopt and delegate authority to these systems"（§2.4.1）；"states will face a growing pressure to adopt these technologies to maintain their relative power compared to other states"（§4.3.1）；"Those who resist these pressures will eventually be displaced by those who do not"（执行摘要）。
- 该文说的是不需要突然的能力跃升或明显的失准，没有说不需要竞赛。

**问题。**
- "no misaligned system" 是忠实的，"no race" 不是。
- 而且这样写恰好遮蔽了 Kulveit 等人与本文同源的一面：国家为维持相对实力而采用，企业因竞争而让渡权力，正是赢的选择压力。

**修法。** 改为："where AI lowers that dependence, it does so without a decisive winner and without a misaligned system, through the competitive pressure on firms and states to adopt it (Kulveit et al. 2025)"。X1 中 Davidson–Kulveit 一条的 "Absorbed" 也可以补上"under competitive pressure"。

#### E3 T1 行说海湾资本备忘录"结果不详"，但该开发者自己的融资公告已列出一家海湾主权基金

**位置。**
- THEORY §7.3 表 T1 行："conduct not shown: one reported decision weighed a stated principle against staying at the frontier, and how it came out is not known"；
- EVIDENCE EV1 "Conduct, as reported"："whether the investment was taken, and on what terms, is not recorded here"；
- EVIDENCE 头部的 Disclosure 清单。

**依据。**
- Anthropic 2025-09-02 的公告 "Anthropic raises Series F at US$183B post-money valuation"【页面，一手来源】列出："Significant investors in this round include … Ontario Teachers' Pension Plan, **Qatar Investment Authority**, TPG …"。
- 卡塔尔投资局本身也发布了参投消息（The Peninsula 2025-09-03 等多家报道【页面】）。
- 这一轮距 EV1 所记的 2025 年 7 月备忘录约六周。

**问题。**
- 登记册的披露原则是：凡涉及起草模型开发者、与某一行相关的来源，不论利弊都要记录，并请读者检查是否遗漏不利项。
- 这是一项可以公开查到、对该开发者不利的结果，正文却说"不详"，所以 T1 行的事实陈述是错的。
- 修正之后，T1 在**行为**层面多了一件有一手来源的证据。这条证据有利于本文的诊断，所以修正并不削弱论证，只是此前的遗漏偏向起草方开发者。同一模型家族的起草者和评审者在这里都有偏差风险（见第六节）。

**修法。**
- T1 行只写角色，改为："…one reported decision weighed a stated principle against staying at the frontier, and the developer's next financing round included a Gulf state's sovereign fund"。也可以把 "conduct not shown" 改为 "conduct shown in one case"。
- EV1 记录该公告（‡ page，一手），删去 "whether the investment was taken … is not recorded here"，并在 Disclosure 清单中加上这一项。
- 按同一标准，其他开发者同类的主权资本与海湾算力交易，如果要记，也应记录同类文件。我没有逐一核实这些交易。

#### E4 "行为控制不了的证据"说得比所引来源更强

**位置。**
- THEORY Remark 4.9："the bound on $m_{\rm model}$ must come from evidence that behaviour does not control, such as weights and activations (Goldowsky-Dill et al. 2025), training data, and elicitation by fine-tuning (Greenblatt, Roger, Krasheninnikov and Krueger 2024)"；
- Remark 6.8 后的段落："evidence the system's behaviour does not control: weights, activations and training data in auditors' hands"；
- SUPPLEMENT S4 (3) 与 S6 "Hence the direction of the bound"；
- EVIDENCE EV6 "Effect on the recommendation"；
- 中文导读第 5 条的对应句。

**依据【记录】。**
- Goldowsky-Dill et al. 摘要："current performance is insufficient as a robust defence against deception"。
- Greenblatt, Roger, Krasheninnikov and Krueger (2024) 摘要：微调诱出 "may be unreliable when high-quality demonstrations are not available, e.g. as may be the case when models' (hidden) capabilities exceed those of human demonstrators"。这恰好是本文需要这条渠道的那一段能力区间。
- Bailey et al. 2024, "Obfuscated Activations Bypass LLM Latent-Space Defenses"（arXiv:2412.09565，10 位作者）："state-of-the-art latent-space defenses — including sparse autoencoders, representation probing, and latent OOD detection — are all vulnerable to obfuscated activations… neural activations are highly malleable"。
- 本文自己在 Baker et al. 2025 那里已经承认：对监测器施加优化会产生混淆。同样的逻辑也适用于针对探针的训练。

**问题。**
- 被掩蔽一类的准入规则（Remark 6.8，tier 1(b) item 7）建立在"行为控制不了"之上。所引来源支持的只是"行为较难直接控制"，而且每一条都写明了在高能力处可能失效。
- 正文虽然把"准入能否在准入能力处界住掩蔽"列为 C12，但 Remark 4.9 和 Remark 6.8 的陈述本身仍是无条件的。按"陈述自带条件"的规则，这里少了条件。

**修法。**
- Remark 4.9 改为："…must come from channels that behaviour controls less directly: weights and activations, which linear probes read for strategic deception though not yet robustly (Goldowsky-Dill et al. 2025) and which optimization against a probe can obfuscate (Bailey et al. 2024); training data; and elicitation by fine-tuning, which recovers withheld capability given good demonstrations and may fail where the hidden capability exceeds the demonstrators' (Greenblatt, Roger, Krasheninnikov and Krueger 2024). How far these channels bound masking at a given capability is crux C12."
- Remark 6.8 后的段落、S4、S6 与 EV6 作相应修改；中文导读第 5 条不必改动。
- Bailey et al. 2024 加入 THEORY 与 SUPPLEMENT 的文献表。

### 【次要】

1. **E5 Stix et al. (2025) 的前瞻判断被标为 [obs]。**
   - **位置：** THEORY §6.4 *Strong incarnation* 末句："…are deployed first inside the developer, where an admission condition that applies only at release does not reach them (Stix et al. 2025) [obs]"。DISCUSSION X1 和中文导读第 5 条也作为事实陈述。
   - **依据：** 摘要原文是 "The most advanced future AI systems **will** first be deployed inside the frontier AI companies"，这是一份入门报告中的预判，不是观察研究。
   - **修法：** 改标 [prem]，或写 "are expected to be deployed first … (Stix et al. 2025)"。若要保留 [obs]，应当引用开发者系统卡中关于发布前内部使用的记载。

2. **E6 Fudenberg and Koh (2026) 在正文中被说成"唯一均衡"。**
   - **位置：** THEORY §8.3(b) 写 "pacing can be the unique equilibrium of a capability race"，X8 写的是 "unique Markov perfect equilibrium"。
   - **依据：** 摘要说，在 Markov 完美均衡中参数高时 "only pacing survives"；对全部子博弈完美均衡只说 "high risk rules [perpetual racing] out"，并给出灾难概率的上界。结论只适用于两家企业。
   - **修法：** 正文改为 "the unique Markov perfect equilibrium of a two-developer capability race"。

3. **E7 过程笔记里已经指出、却没有落实到正文的三处引文修正。** x1-notes "For the integration editor" 第 3、4 项与 registers-notes "Found in passing" 第 2、3 项都已指出。
   - **(a) §6.3 "hidden loyalties … (Davidson, Finnveden and Hadshar 2025)"：** 报告原用 "singular / secret loyalties"，X1 已改，正文未改。
   - **(b) §6.4 "a single optimizer of a bounded goal still acquires options … (Turner et al. 2021)"：** 有界目标的情形不是 Turner 的定理，应写 "(compare Turner et al. 2021)"，X1 已经按 "for most reward functions" 改了。
   - **(c) §1.4 What is new 中 "concern for relative gains depends on how far gains convert into future advantage (Powell 1991)"：** x1-notes 第 3 项认定这一句丢掉了 Powell 的条件，X1 已改为 "arising where gains can be turned into advantage in the use of force and fading where force is too costly"。正文与 X1 现在对同一篇文献的读法不一致。
   - **修法：** 照笔记的措辞落实到正文。

4. **E8 Williams et al. (2025) 用的是模拟用户反馈。**
   - **位置：** THEORY §6.4 "manipulation learned from user feedback (Williams et al. 2025)"。
   - **依据：** 摘要原文："training LLMs with Reinforcement Learning with **simulated** user feedback"。
   - **修法：** 改为 "manipulation learned from simulated user feedback"。与 Sharma et al. 2023（真实人类偏好数据）的证据强度不同，应当区分。

5. **E9 Budd, Harris and Vickers (1993) 被说成"决定于"联合收益。**
   - **位置：** DISCUSSION X1："whether the asymmetry between rivals grows is decided, near equality, by whether joint payoff rises with the gap"。
   - **依据：** 摘要【页面，IDEAS】："We show that several effects are at work. The state tends to evolve in the direction where joint payoffs are greater…"，并且 "there may be equilibria in which this last effect means that the laggard works harder than the leader even though all the other effects work in favour of the leader"。"near equality" 是起草者加的限定，摘要里的近似是渐近展开。
   - **修法：** 改为 "the state tends to drift toward greater joint payoff, among several effects, and self-reinforcing effort costs can reverse it"。

6. **E10 TESTS 引用的 Khan et al. 2024 与 Kenton et al. 2024 不在任何文献表里。** V6.1 评审已经指出，CLAIMS 表 G7 也承认 "cited in TESTS only"。两篇都存在【记录】：arXiv:2402.06782（ICML 2024）、arXiv:2407.04622（NeurIPS 2024），D4 笔记已经备好条目。**修法：** 加入 DISCUSSION 的文献表（TESTS 的引用按约定在那里解析）。Zhu 2026 只在 EVIDENCE 中有完整出处，也宜一并列入。

7. **E11 "more so with capability and situational awareness … each has been shown in constructed settings"（THEORY §6.4 *Weak incarnation*）。**
   - "each" 修饰的是倾向，但"随能力增强"并不是每一项都有证据。有证据的只有：Hubinger et al. 的持久性在最大模型中最强；Needham et al. 的评估意识。
   - 关机抵抗（Schlatter et al.）的差异按模型呈现，没有按能力单调变化。
   - **修法：** 改为 "…, in some studies more so with capability or situational awareness; each tendency has been shown in constructed settings (EV6)"。

8. **E12 X11 "The first nuclear monopoly and the period of superiority (1945–54)" 一行的 "the advantage was small in stockpile"** 只适用于 1945–48 年。
   - Norris–Kristensen 的两套数字：1947 年 13 或 32 枚，1948 年 56 或 110 枚；到 1953 年已超过 1,100 枚，1954 年超过 1,600 枚【页面，The Bulletin "U.S. nuclear warheads, 1945–2009"】。Trachtenberg 所论的 1949–54 年，优势是"正在流失"（wasting），并不是"在库存上很小"。
   - **修法：** 改为 "small in stockpile until 1948 (Rosenberg 1983), and from 1949 a wasting advantage offset by the other side's bomb and conventional forces (Trachtenberg 1988/89)"。该行的结论 "restraint where the advantage was not decisive" 不受影响。

9. **E13 X11 不扩散一行 "several were carried out, mostly not by the cooperating powers (Fuhrmann and Kreps 2010)"：无法核实。**
   - 原文全文无法取得，我未能核对计数。
   - 按我所知，该文 1941–2000 年的数据集里包括二战期间盟国对德国计划的打击，以及 1991 年有一个核大国参与的联军打击。所以 "mostly" 取决于时间窗口和对"合作的大国"的界定。
   - **修法：** 限定为"在核不扩散条约时期"，或者给出原文的计数。

10. **E14 §11.5 "The Biological Weapons Convention shows that a weapon … can be renounced unilaterally"：** 单方面放弃发生在 1969 年，早于 1972 年的公约。X11 的写法（"one party renounced it unilaterally"）是准确的。**修法：** 改为 "The record that led to the Biological Weapons Convention shows…"。

11. **E15 EV1 的同类对同类仍有缺口。**
    - 开发者竞争性文章一栏只记了起草方开发者首席执行官的文章（stick 与 carrot）。另一家开发者首席执行官同一体裁的文章没有记录：Altman, "Who will control the future of AI?", *Washington Post*, 2024-07-25，主张 "U.S.-led global coalition"，让民主的 AI 胜过威权的 AI【页面，经多家报道核实】。那家开发者在登记册里只出现在 RFI 和合作性的 Charter 一侧。
    - 另外两处小问题：
      - Anthropic OSTP 提交的引文去掉了句首的 "We believe"（原文 "We believe the United States must take decisive action…"），应当保留或标出省略；
      - EO 14365 §5 除 BEAD 资金外还涉及可酌情的联邦拨款，EV3 只写了前者。

12. **E16 书目标记与细节。**
    - 许多条目仍是没有限定词的 "†"（如 Weitzman 1974、Shavell 1984、Fearon 1995、Jervis 1976/1978、Schelling 1960），也有自造的 "† (pages per the v6.1 evidence review)"，都不合文献表开头的图例。
    - 本轮我经 Crossref 确认了下列记录，可以改标 "‡ (record)" 或 "† (record)"：
      - Weitzman，RES 41(4):477–491；
      - Shavell 1984，JLS 13(2):357–374；
      - Shavell 1986，IRLE 6(1):45–58；
      - Abreu，Econometrica 56(2):383–396；
      - Cho–Kreps，QJE 102(2):179–221；
      - Wald，AMS 16(2):117–186；
      - Kydd 2000；Snidal 1991；Grieco 1988；Powell 1991；Powell 2006；
      - Aghion et al. 2001；Athey–Schmutzler 2001；Budd–Harris–Vickers 1993；
      - Hehenkamp et al. 2004；Cardaliaguet 1996；Podvig 2002；Calvano et al. 2020；Butler et al. 2025。
    - 其他细节：
      - Thornley 一条，Crossref 给出的卷期年份为 2025（2024 年在线）；
      - Kulveit et al. 可以补上页码 81678–81688；
      - Gardner-Challis et al. 的第 7 位作者是 Charlie Griffin。

---

## 三、新增文献逐条核实（V6.2 文献表中有、V6.1 三份表中都没有的）

比对用 `refdiff.py` 完成，以（第一作者，年份，题名）为键。V6.1 的条目无一在 V6.2 中消失。正文引用与文献表的双向核对用 `cites.py` 完成：三份正文的引用都能在本文件的文献表中找到；反向检查也没有发现未被引用的条目。唯一的例外是 TESTS 的 Khan、Kenton 和 Zhu（见 E10）。

### 2024–2026 年对齐文献

| 文献 | 状态 | 引用句是否忠实 |
|---|---|---|
| Hubinger et al. 2024, arXiv:2401.05566（39 位作者） | 已核实【记录】 | 忠实："deception that survives safety training"；EV6 注明是人为构造的后门 |
| Greenblatt, Denison et al. 2024, arXiv:2412.14093（20 位作者） | 已核实【记录】 | 忠实；14%、78% 无误 |
| Meinke et al. 2024, arXiv:2412.04984（6 位作者） | 已核实【记录】 | 忠实，包括 Claude 3.5 Sonnet 为训练中获得的目标而故意表现不佳 |
| MacDiarmid et al. 2025, arXiv:2511.18397（22 位作者） | 已核实【记录】 | 忠实："aligned behavior on chat-like evaluations, but misalignment persists on agentic tasks" |
| Schoen et al. 2025, arXiv:2509.15541（19 位作者） | 已核实【记录】 | 忠实："this awareness decreases covert behavior, while unawareness increases it" |
| van der Weij et al. 2024, arXiv:2406.07358 | 已核实【记录】 | 忠实 |
| Greenblatt, Roger, Krasheninnikov, Krueger 2024, arXiv:2405.19550 | 已核实【记录】 | 部分忠实，漏了来源自述的局限（E4） |
| Goldowsky-Dill et al. 2025, arXiv:2502.03407 | 已核实【记录】 | 部分忠实，漏了 "insufficient as a robust defence"（E4） |
| Marks et al. 2025, arXiv:2503.10965（35 位作者） | 已核实【记录】 | 忠实；"black-box 团队未找到"出自正文，摘要只写四队中三队成功 |
| Baker et al. 2025, arXiv:2503.11926 | 已核实【记录】 | 忠实："monitorability tax"；较弱模型监测较强模型 |
| Guan et al. 2025, arXiv:2512.18311（12 位作者） | 已核实【记录】 | 忠实："RL optimization does not materially decrease monitorability"；更小模型配更高推理强度；监测器算力扩展 |
| Korbak et al. 2025, arXiv:2507.11473 | 已核实【记录】（V6.1 已列） | 忠实 |
| Schlatter, Weinstein-Raun, Ladish 2025, arXiv:2509.14260, TMLR 2026 | 已核实【记录】 | 忠实（仅在 EV6） |
| Li et al. 2026 EvalDetectBench, arXiv:2609.01611 | 已核实【记录】；arXiv 提交日期为 2026-06-08，与编号不一致之处登记册已注明 | 忠实（仅在 EV6） |
| Panickssery, Bowman, Feng 2024, arXiv:2404.13076 | 已核实【记录】 | 忠实 |
| Gardner-Challis et al. 2026, arXiv:2602.20628（7 位作者） | 已核实【记录】+【页面】 | 忠实；文中有红队实验（GPT-4.1 自我识别的共谋），"constructed settings" 成立 |
| Brown-Cohen et al. 2025, arXiv:2506.13609（6 位作者） | 已核实【记录】 | 忠实；"under certain stability assumptions" 可以补上 |
| Stix et al. 2025, arXiv:2504.12170（9 位作者） | 已核实【记录】 | 标签过强（E5） |
| Davidson, Finnveden, Hadshar 2025, Forethought | 已核实【知识】+ x1-notes 的页面核对 | 正文 "hidden loyalties" 应为 "secret loyalties"（E7a） |
| Kulveit et al. 2025, ICML 2025 position, PMLR 267 | 已核实【记录】 | 有误（E2） |
| Terekhov et al. 2026, ICLR 2026, arXiv:2506.05296 | 已核实【记录】+ ICLR 页面 | 忠实 |
| Huang et al. 2025, arXiv:2503.00555 | 已核实【记录】 | 忠实 |
| Bai et al. 2022, arXiv:2204.05862 | 已核实【记录】 | 忠实："improves performance on almost all NLP evaluations"；"larger models" 的限定出自正文 |
| Sharma et al. 2023, arXiv:2310.13548 | 已核实【记录】 | 忠实 |
| Williams et al. 2025, ICLR 2025, arXiv:2411.02306 | 已核实【记录】 | 漏了 "simulated"（E8） |
| Askell, Brundage, Hadfield 2019, arXiv:1907.04534 | 已核实【记录】 | 忠实 |
| Calvano et al. 2020, AER 110(10):3267–3297 | 已核实【记录】 | 忠实 |
| Fish, Gonczarowski, Shorrer 2024, arXiv:2404.00806，"Accepted to EC 2026" | 已核实【记录】 | 忠实 |
| Turner and Tadepalli 2022, NeurIPS 35 | 已核实【记录】 | 忠实 |
| Turner, Hadfield-Menell, Tadepalli 2020, AIES | 已核实【记录】 | 忠实 |
| Thornley 2024, *Phil. Studies* 182(7):1653–1680 | 已核实【记录】（卷期年 2025） | 忠实 |
| Soares et al. 2015; Taylor 2016 | 已核实【知识】 | 忠实 |
| Khan et al. 2024; Kenton et al. 2024 | 已核实【记录】 | 引用忠实，但缺文献表条目（E10） |

### X1 新增的国际关系、产业组织与军控文献

| 文献 | 状态 | 引用句是否忠实 |
|---|---|---|
| Grieco 1988, IO 42(3):485–507 | 已核实【记录】 | 忠实 |
| Snidal 1991, APSR 85(3):701–726 | 已核实【记录】；摘要据检索结果 | 忠实：两方时相对收益阻碍合作，多方时影响小得多 |
| Powell 1999, Princeton UP | 已核实【知识】 | 忠实：权力转移阴影下的讨价还价 |
| Gilbert and Newbery 1982, AER 72(3):514–526 | 已核实【知识】；Crossref 本轮未命中 | 忠实：在位者的抢先激励 = 垄断利润 − 双寡头利润 |
| Budd, Harris, Vickers 1993, RES 60(3):543–573 | 已核实【记录】+ 摘要 | "decided" 说过头（E9） |
| Athey and Schmutzler 2001, RAND 32(1):1–26 | 已核实【记录】+ 摘要 | 忠实；摘要另有"足够耐心时"的反向效应，可以一并写出 |
| Aghion, Harris, Howitt, Vickers 2001, RES 68(3):467–492 | 已核实【记录】 | 与标准读法一致；全文未读（无法核实"far behind are discouraged"的具体出处） |
| Avenhaus, von Stengel, Zamir 2002, Handbook ch. 51, 1947–1987 | 已核实【记录】 | 忠实：我推导出 Prop 8.6(2) 的门槛 $(T-R)/(T-P+F)$ 与检查博弈的威慑条件 $\beta\ge d/(d+b)$ 逐项一致 |
| Schelling and Halperin 1961, Twentieth Century Fund | 已核实【知识】 | 忠实 |
| Kydd 2000, IO 54(2):325–357 | 已核实【记录】 | 忠实 |
| Shavell 1984, JLS 13(2):357–374；Shavell 1986, IRLE 6(1):45–58 | 已核实【记录】 | 忠实 |
| Grossman and Helpman 1994, AER 84(4):833–850 | 已核实【知识】 | 忠实 |
| Harris and Vickers 1987；Konrad and Kovenock 2009；Konrad 2009 | 已核实【记录/知识】 | 忠实（discouragement effect） |
| Hehenkamp, Leininger, Possajennikov 2004, EJPE 20(4):1045–1057 | 已核实【记录】 | 忠实：`ess_tullock.py` 验证有限群体 ESS 每人 $rV/n$，总耗散 $rV$，在 $r=1$ 时完全耗散 |
| Cardaliaguet 1996, SICON 34(4):1441–1460 | 已核实【记录】 | 忠实 |
| Abreu 1988；Cho and Kreps 1987；Wald 1945 | 已核实【记录】 | 忠实：Wald 界 $\mathsf a/(1-\mathsf b)$、$\mathsf b/(1-\mathsf a)$ 无误 |
| Weitzman 1974 | 已核实【记录】 | 忠实 |

### 其他新增文献

| 文献 | 状态 | 引用句是否忠实 |
|---|---|---|
| Kuran 1995；MacKenzie 2006；Maynard Smith and Szathmáry 1995；Meadows 1999 | 已核实【知识】 | 忠实：Meadows 十二个干预点的编号与正文的映射逐一无误 |
| Podvig 2002, SGS 10(1):21–60；Hoffman 2009 | 已核实【记录/知识】 | 忠实；正文没有加"上报即会触发报复" |
| Butler et al. 2025, PNAS 122(9) | 已核实【记录】 | 忠实 |

---

## 四、EVIDENCE 各行（对称标准）

| 行 | 核到的内容 | 状态 | 正文的强度表述 |
|---|---|---|---|
| EV1 | EO 14365 的编号、日期、90 FR 58499–58501、§2 原句、§3 三十天、§8(b) 例外【页面，govinfo】；行动计划的 "Winning the AI race…"、"cement U.S. dominance in artificial intelligence"【页面】；Anthropic OSTP 提交（2025-03-06）的出口管制原句与六个方面【页面】；Amodei 文章的 stick 与 carrot（V6.1 已核实） | 已核实，有两处次要（E15）；Conduct 一项有误（E3） | T1 "Evidenced in declarations" 得当；"how it came out is not known" 有误（E3） |
| EV2 | OpenAI PF v2 §4.3 原句逐字无误，包括 "rigorously confirm"、"but only if" 和三个条件【全文】；RSP v3.0 的 "driven by a collective action problem…"、"we cannot commit to following them unilaterally"、"until and unless we no longer believe we have a significant lead"、"meet or exceed"、"General upleveling" 逐字无误【全文】；v3.0–v3.4 的生效日期，以及 v3.1、v3.2、v3.4 的修改要点【页面】；GovAI 分析的四点【页面】；Zhu 2026 的 710 处、12 对版本、77%、67%/53%【记录】；BdM §6.3 两段原句与脚注 9【全文】 | 已核实 | T2 写 "written commitments, not conduct"，得当 |
| EV4 | 2026-02-12 与 2026-07-21 两笔 2,000 万美元、501(c)(4)、四项立场、"cannot be used to influence the election of any candidate"、"a way to slow or block the deployment"【页面，一手】；Leading the Future 网络 2025 年下半年筹得 1.25 亿美元以上，捐款者包括一位前沿开发者联合创始人、风投与 Perplexity【页面】 | 已核实 | T4 "Partly evidenced" 得当；按可占有性分类，不按声明目的分类，做法正确 |
| EV5 | METR TH1.1：131 天对 165 天【页面】；"Measurements above 16 hrs are unreliable…"（2026-05-08）【页面】；Epoch 开放与封闭模型差距：四个月、8 点（2026-05-29），以及 2025-10-30 的三个月【页面】；Epoch 国别比较：自 2023 年起前沿全部出自一国，平均落后 7 个月（4 到 14）【页面】；AI Index 2026 的 "effectively closed"、"traded the lead multiple times"、2.7%【页面】；METR arXiv:2503.14499 v4，NeurIPS 2025【记录】 | 已核实 | §7.2 写 "is reported to have been traded"，Decisiveness 行写 "Not established"，都得当 |
| EV6 | 见第三节；Needham et al. 的 AUC 0.83 对 0.92【记录】 | 已核实 | §7.3 写 "Shown in constructed settings"，得当；Remark 4.9 与 6.8 的推论过强（E4） |
| EV8 | 第 79/239 号决议 159–2–5，两国都投赞成【页面】；第 80/58 号决议 167–5–5，第一国反对、第二国赞成【页面】；2026-02-12 任命投票 117–2–2，两国表态原句【页面】；REAIM 2026 两国都未背书，85 国中 35 国背书【页面】；政治宣言 2024-03 有 54 国背书【页面】；2026-09-25 白宫情况说明书的 "U.S.-China Super Intelligence (SI) Dialogue"、"by November 2026"、"a bilateral communication channel for SI incidents"【页面，一手】 | 已核实 | T6 "Mixed" 与 §11.4 "Where things stand" 都得当 |
| EV11 | Jones (2024) 的 Key Points 1–5、40 年、55 倍、约三分之一、4.5 年、约 4%、δ=2% 时立即停止、约 25%【全文】，算术见 `arith.py`；BdM 的 Prop 9、Cor 1、局部结果、Meta 顾问披露【全文】；Fudenberg–Koh 摘要【记录】；Fernández Domingos–Han【记录+页面】 | Jones、BdM、Fudenberg–Koh 已核实；Fernández Domingos–Han 有误（E1） | §8.1 对 Jones 的转述现在正确；§8.3(b) 对 Fudenberg–Koh 略强（E6）；§11.2 对 Fernández Domingos–Han 有误（E1） |

EV9 也顺带核对了：NeurIPS 版的 90% 区间为 2 到 22 个月，arXiv v1 的 95% 区间为 5 到 14 个月；$2^{12/8}=2.83$，$2^{12/22}=1.46$，$2^{6}=64$，都无误。

---

## 五、§11.5 与 X11 的先例

1. **准确的部分。** 以下各项与我所知的史实一致【知识；部分有 V6.1 评审的页面核对】：
   - Acheson–Lilienthal 与 Baruch（1946）：Baruch 计划提出制裁不受否决、另一方反对视察、领先方在管制就位前保留垄断（Bundy 1988）；
   - ABM 条约（1972 年签署、2002 年退出），多弹头不受限；
   - 部分禁试条约（1963）；
   - 外层空间条约与海床条约：排除的是一类武器在一个领域的部署；
   - BWC 与隐蔽计划（Leitenberg and Zilinskas 2012）；
   - 1979 年后的核电与 INPO（Rees 1994）；
   - 蒙特利尔议定书，含 1987 年文本中对非缔约方的贸易措施与 1990 年修正案设立的基金（Barrett 2003）；
   - 稳定–不稳定悖论（Snyder 1965）；
   - Nye 1987。
2. **V6.1 评审的五处措辞修改都已落实**（ABM、外空与海床、行名改为 "period of superiority"、§11.5 补回限制条件、1983 年事件的出处）。
3. **仍有问题的三处：** 1945–54 年"库存小"（E12）、"mostly not by the cooperating powers" 无法核实（E13）、BWC 与单方面放弃的先后（E14）。
4. **措辞得当的地方。** "custody must precede decisiveness" 是从先例得出的推论。X11 用 "was read by the other side as a bid to keep it" 表述，措辞得当，正文 [obs] 后面跟着 "X11, corrected against the sources"，可以接受。

---

## 六、正文点名检查与同一模型家族的偏差

**点名检查。** 我对 THEORY 正文（文献表之前）做了正则扫描：
- 英文方面，扫描了国家、首都、地区、企业、产品、人名，包括 United States/U.S./China/Russia/Soviet/Gulf/OpenAI/Anthropic/DeepMind/xAI/Biden/Trump/Xi/Petrov 等；
- 中文导读方面，扫描了 美国、中国、苏联、海湾、白宫、各企业名 等。

结果：
- 正文中没有点名任何国家或企业。
- 出现的专名只有三类：条约名（Montreal Protocol、Biological Weapons Convention）；状态行中的 "Claude" 和 "Codex"，用作起草与评审的出处说明，属于披露，不是论证中的点名，不必改；文献表题名中的 "Russian early-warning system"。
- SUPPLEMENT 与 DISCUSSION 也没有点名作为行动者的国家或企业。X1 中 "in China, Mozi's impartial care" 是思想传统，不是行动者。
- EVIDENCE 按自己的规则点名来源，这符合约定。

**同一模型家族的偏差可能在哪里起作用。**
1. 关于起草模型开发者的条目。E3 是我在登记册"请读者检查不利遗漏"的提示下专门去找的。D4 笔记所列"留给外部评审"的三项我没有核实，同一家族的评审者在这里仍可能系统性地少找：联邦游说披露、2024 年对一项州法案的 "support if amended" 信函、国防合同及 2026 年的用途争议。
2. 对齐文献中，Hubinger、Greenblatt–Denison、MacDiarmid、Marks 四项出自该开发者的研究者。我读的是摘要与少量正文，对其框架（"constructed settings"、"masked divergence"）可能与起草者共享先入之见。E4 是在这里唯一发现的过强之处。外部评审者应当专门检查：EV6 是否只收了"演示存在"的研究，而漏了"在部署中罕见"或"缓解有效"的反向研究。
3. 对"对称标准"的理解：登记册与我都把"同类文件"作为标准。外部评审者可能认为还应当包括同类**行为**，例如其他开发者的主权资本交易（E3 修法中已提及，未核实）。

---

## 七、好的、不应改动的

1. **Jones (2024) 的改正是范例。** 正文只说曲率决定可接受风险，$h<g_r-g_p$ 写明是本文在线性效用下的推导，EV11 记下了全部数字与条件。我用全文逐项核对，无一处出错。
2. **EV2 把三份文本逐条并列，引文全部逐字准确。** 三份是：
   - RSP 的集体行动段；
   - 保留的暂停裁量，并写明 "retained discretion, not a commitment"；
   - 外部分析与 Zhu 的单作者未评审研究。
   正文 T2 写 "written commitments, not conduct"，强度恰当。
3. **EV4 按可占有性分类，并把起草方开发者的支出与反方网络的支出并列。** 做法正确，也符合对称标准。分类依据的是本文自己的变量（$\chi$、$d$），没有采信支出方自述的目的。
4. **EV5 与 §7.2 对"领先是否易手"的写法得当。** "depends on the measure" 与 "is reported to have been traded" 都没有说过头，也没有说不足。
5. **EV8 按文件逐条列出两个领先国家的表态。** 这是 V6.1 评审 I3 要求的，落实得完整，引文无误。
6. **对齐文献部分的结构清楚，转述总体忠实。** 结构是：掩蔽 → 控制 → 主体内的集中 → 代价的度量。转述中 MacDiarmid 的 "chat-like evaluations … agentic tasks"、Schoen 的因果方向、Guan 的三项结论尤其准确。
7. **文献表双向一致，标记分级也比 V6.1 规范。** 本轮的自动核对和我的独立核对都表明：V6.1 的撞键问题（Maynard Smith 与 H. Smith、Acemoglu、Schelling 1966）都已解决。

---

## 八、核查了什么，没有核查什么

**核查了。**
- 三份文献表与 V6.1 的差异，以及正文引用与文献表的双向一致。
- 第三节所列全部新增文献的存在性与书目：arXiv API、Crossref，或凭知识。
- 2024–2026 年对齐文献每一处引用句与摘要的对应。
- X1 新增国际关系、产业组织文献的引用句与摘要或标准读法的对应。
- EV1、EV2、EV4、EV5、EV6、EV8、EV11 的主要一手来源：
  - 四份 PDF 全文：Jones、NBER w35276、RSP v3.0、PF v2；
  - 约二十个网页：联邦公报、白宫、Anthropic 两篇捐款文与融资公告、UNRIC、UN-project、Epoch、METR、HAI、GovAI、Capacity。
- §11.5 与 X11 的先例；正文点名。
- Hehenkamp 的耗散、Avenhaus 的门槛、Wald 界、EV9、EV10 与 Jones 的算术。

**没有核查。**
- 付费墙后的全文：Snidal、Budd–Harris–Vickers、Aghion et al.、Athey–Schmutzler、Fuhrmann–Kreps、Rosenberg、Trachtenberg、Grossman–Helpman、Gilbert–Newbery。这些只核对了记录与摘要，或者凭知识。
- 书籍：Kuran、MacKenzie、Powell 1999、Schelling–Halperin、Hoffman、Maynard Smith–Szathmáry、Meadows，凭知识。
- 以下来源我没有重新取得：Wired 报道原文、OpenAI RFI 原页、UN 小组初步报告本身、EY 的最低税报道、国发〔2025〕11 号原文、ETO AGORA 页面、Fudenberg–Koh 全文。
- EV3、EV7、EV9 以外的其余登记行（EV12–EV18）只抽查了 EV18。
- 正文的数学，以及 LEDGER-v62-sentences.tsv。

**会话中已有其他评审文件出现在 `reviews/` 目录。** 为保持独立，我没有阅读它们。
