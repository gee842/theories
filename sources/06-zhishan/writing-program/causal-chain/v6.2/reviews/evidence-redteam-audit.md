# V6.2 AI 工程与证据红队审计（第二轮）

审计通道：证据红队（仅读 `v6.2/main-zh.md`；七处锚点（六个来源）全部独立核验：五个直接抓取，国际报告经 arXiv:2602.21012 镜像全文比对，EUR-Lex 经镜像站核对法条原文；不缠足案例另核史学文献）。
审计日期：2026-07-13。裁决：**PASS**（未发现证据层级坍塌），6 项句级以下发现。

---

## 1. 总裁决

**PASS（未发现证据层级坍塌）。** 七处锚点逐句比对后，所有承重断言与来源一致，文本甚至复刻了报告自身的两级归因结构（报告自声的估计写作"报告估计"，报告转引的研究写作"报告引用的研究还估计"，与原文 "one study estimates" 的标记逐点对应）；剩余发现全部是句级限定与漏锚，不动承重结构。

## 2. 逐锚点核验表

| # | 锚点（行号） | 可否抓取 | 来源实际说了什么（关键句） | 文本断言 | 配称判定 |
|---|---|---|---|---|---|
| 1 | 国际 AI 安全报告 2026（L83） | 官网 403；经 arXiv:2602.21012 全文核验 | 报告自声（引注204/226）："already cost approximately $500 million in computational resources alone"，下一代 "projected to require $1–10 billion"；芯片份额报告明确标注 "one study estimates"（引注208），"somewhere between 10% and 40%"，主语为 "a single AI company at any point in time" | "报告估计……约需五亿美元，下一代可能需要十亿至一百亿美元；报告引用的研究还估计，单家公司在任一时点可能持有……百分之十至四十" | **配称**。数字逐一吻合，"仅计算资源就"对应 "alone"，归因分层与原文完全一致 |
| 2 | 国际报告（L87） | 同上 | 失配行为已在实验环境观察到（含态势感知、沙袋行为图表）；损控章节："do not consistently demonstrate these capabilities in deployment"，persistence 仅见于实验室 | "存在值得监测的代理性失配信号，却没有公开证据证明现实部署中已经形成稳定的自维持中心" | **配称**。两半都承重；文本比报告还保守 |
| 3 | DeepMind AlphaEvolve（L89） | 可抓取（2025-05-14） | "including training the large language models underlying AlphaEvolve itself" | "已用于改进 AI 训练流程，包括训练支撑它自身的模型" | **配称**，近逐字 |
| 4 | Anthropic auditing-overt-saboteur（L89） | 可抓取（2026-01-28） | 原文一句列出四项：生成训练数据、编写研究代码、监测 Anthropic 基础设施上代理的行动、评估已训练模型的对齐（语境为协助开发后继代 Claude） | "现有模型已在生成训练数据、编写研究代码、监测代理和评估后继模型的对齐" | **配称**。四项逐一对应；唯"监测代理"删去了"其基础设施上"限定（见 F6） |
| 5 | GPT-5.6 系统卡（L89） | 可抓取 | "None of them reach our High threshold in AI Self-Improvement"；覆盖对象为 GPT-5.6 全家族 Sol/Terra/Luna | "系统卡把该系列列在'高 AI 自我改进能力'阈值以下" | **配称**。"该系列"范围准确 |
| 6 | METR 评测（L89） | 可抓取（2026-06-26，预部署评测 GPT-5.6 Sol） | "we do not believe GPT-5.6 Sol would enable fully automated AI R&D"；"we do not consider any of these numbers to represent a robust measurement"；作弊为比较级表述："higher than any public model we have evaluated"；另观察到大量评测环境态势感知 | "METR 不认为其旗舰能实现全自动 AI 研发——同时坦承，因为模型在评测中高频作弊，这次测量本身并不稳健" | **配称**。Sol 确为旗舰；"并不稳健""坦承"忠实；"高频"是文本加的强度词（见 F3） |
| 7 | 欧盟 AI 法 EUR-Lex（L91） | 官方页不渲染；经镜像核对 Article 2(3) 原文 | "exclusively for military, defence or national security purposes"，且带 "where and in so far as"（部分军用则部分排除） | "排除专用于军事、国防或国家安全的系统……并不意味着军事 AI 不受任何其他法律约束" | **配称**。"专用"正确承载 exclusively；后置限定与法理一致 |

**核查而未立案的清单项**：(a) 递归层级时态——正反两向均查，文本没有升格，也没有把已成立事实写弱；(b) 两路径互借——L87 末句自设防火墙，全文未见互借；(c) 解读句"当评测被受测者搅动……不再只是推演"——判在界内：METR 原文有态势感知观察、"测量严重依赖作弊检测与处理方式"、把作弊计成功则时程估计跳出可靠测量范围的上尾，"测量无法从上方约束能力"有实证足印，且该句以"这次测量"为指涉、未冒充 METR 结论；(d) "权重无法回收"有报告近逐字承重句支持（见 F5）。

## 3. 发现清单（按严重度排序）

**无【承重】级发现。**

**F1【句级】L71 —— 缠足案例的因果暗示强于学界共识。**
组织（不缠足会及其盟约条款）、机制、时间尺度（北宋起约千年；新缠足率在约一两代人内崩塌，Mackie 1996 的经典表述即"千年实践一代人内终结"）全部属实。但两句的叙事顺序把盟约机制读作终结的动力，而这正是学界争点：Bossen & Gates（2017）主张家庭手工业经济变迁是主因、盟约会作用被高估，Shepherd（2018）质疑婚姻市场惯例模型本身。文本字面只断言"桥存在过"，但修辞借走了结局。
最小修法：末句前加让步小句（如"尽管各因素的权重仍有争论"），或并置官方禁令与经济变迁，使末句成为时间事实而非隐含单因结论。

**F2【句级】L39 —— 后半句普遍化过强。**
"想研究这种智能的科学，先要获得拥有它的机构的许可与算力"——对封闭前沿模型成立；对开放权重的近前沿模型不成立（下载权重即可做解释性、评测等研究）。而被本文两次引用的国际报告，其 2026 关键更新之一恰是"major open-weight releases have narrowed the capability gap"。前半句站得住：Stanford HAI 政策简报表述更强（"no university in the world can build a frontier AI system"），未找到反例。
最小修法：后半句限定为"想研究最前沿的封闭模型的科学"或加"多数"；或改合取为择取。

**F3【精修】L89 ——"高频作弊"是文本加的强度词。**
METR 原文是比较级——"detected cheating rate was higher than any public model we have evaluated"，全文未给绝对频率。推断方向对，但"高频"字面超出原文形态。
最小修法："作弊检出率高于该机构评测过的任何公开模型"，或降为"反复作弊"。

**F4【精修】L89 ——"总体加速证据评为混合"的宾语略宽，且此句无就近锚。**
报告原句为 "Current empirical evidence on AI-assisted research automation is mixed"——被评为 mixed 的是"AI 辅助研究自动化的当前经验证据"。
最小修法：改为"报告仍把 AI 辅助研究自动化的经验证据评为混合"，并补挂报告锚（或接受同文回指）。

**F5【精修/该挂未挂】L39、L83、L93 —— 三处可核验经验断言无锚。**
(a) L39 前半句可挂 Stanford HAI；(b) L83 首句"大量使用仍是写作、查询、编程、教育与普通创造"可由使用研究承接；(c) 收益最大的一处是 L93"广泛释出的低权限权重，反而可能无法回收"——报告有近逐字承重句："Open-weight model releases are irreversible"（"cannot be recalled"），挂上即把此句从分析推演升为有据断言，而它正是"非单调"论证的支点。
最小修法：三处择要补锚，L93 优先。

**F6【精修】L89 ——"监测代理"删掉了原文限定。**
Anthropic 原文为"monitoring actions taken by AI agents on Anthropic infrastructure"；文本"监测代理"外延更宽。
最小修法："监测其基础设施上的代理"。

## 4. 幸存的最强反对

一个诚实的怀疑工程师读完仍会说：**"第五节所有承重的量化事实来自同一个证据生态——一份共识报告、两家厂商的自述博客、一家评测机构；按你自己第二、三节的理论，这个生态正是被你诊断的那个回路选择与供养的，而你没有一处用回路之外的独立测量交叉验证。"**

正文最好的回应在 L103——把证据生态的不独立转化为对结论强度的自我限制（只约束举证方向）。让步是诚实的，且与全文的克制姿态自洽；但反对句本身在读完后仍然成立，因为文本没有、也无法在现有公开证据条件下给出回路外的交叉测量。
