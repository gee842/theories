# 中英理论链索引：范围、维护与更新 / Bilingual chain index: scope and maintenance

Recorded 8 October 2026, Asia/Bangkok. [Ren's request and selections](../../../../sources/15-codex-theory-conversations/2026-10-08-bilingual-generativity-chain-index.md) authorize a complete bilingual table of the connected chain, saved as a document and updated when the research changes. The later [cancellation directive](../../../../sources/15-codex-theory-conversations/2026-10-08-cancel-daily-theory-chain-update.md) removes the daily scheduled check. This record is AI-authored.

## 文档与范围 / Document and coverage

主文档是[生成、共同实现与伦理对照表](../../../../theories/shengsheng-buxi-generative-existence/results/GENERATIVITY-CHAIN.md)。首版包含62项导航：8项根基与正面论断、8项延续与共同实现、6项伦理根据与情境理由、20项学习—关切—良知—智慧及应用、14项形式支撑、6项原话与证据入口。它们是不同类型的维护单元，不是62项独立的已证理论，也不是全部历史来源的逐句翻译。

The first edition has 62 entries: 8 grounding/positive claims, 8 continuation/co-realization entries, 6 ethical/situated claims, 20 developmental and application links, 14 formal-support packages and 6 provenance/evidence entries. These are different maintenance units, not 62 independently proved theories. The scope is the connected chain confirmed by Ren, rather than every branch of the repository.

复用[总成果目录](../../../../theories/shengsheng-buxi-generative-existence/results/README.md)所指的同一原文，另按本问题的论证关系组织；没有改写现有目录生成器、阅读JSON或其生成分卷。主表链接当前理论、研究整合、评审、源码和原有检查记录。该引用句及其英文是AI候选表述，不重新署作Ren原话。

The table points to the same original research as the broader results catalogue, organizing it around the requested argumentative chain. Existing catalogue data and generated chapters remain untouched. The quoted sentence and its English translation remain an AI-authored candidate formulation.

## 编辑来源 / Editable sources

- [配对数据 / Paired data](../../../../theories/shengsheng-buxi-generative-existence/results/data/generativity-chain.json)：双语行、稳定ID、相对链接、内容更新日期、已读来源哈希、已检查页面清单。
- [生成与检查脚本 / Renderer and checker](build_generative_chain.py)：生成同一 Markdown 文档，检查配对字段、ID、文件、章节锚点、来源版本及输出一致性。
- [用户指令 / User source](../../../../sources/15-codex-theory-conversations/2026-10-08-bilingual-generativity-chain-index.md)：保留原始范围与历史授权；每日安排已由后续指令取消。

数据中的 `reviewed_sources` 只是已核读版本的指纹，不能证明摘要正确。`known_discovery_paths` 只表明哪些文件路径已经检查是否进入本表，不表示所有这些文档都已全文重读、属于本表范围或已经证明。

Source fingerprints record reviewed versions; they do not establish semantic correctness. The discovery inventory records inspected page paths, not full-text reading or inclusion of every page. Watch existing linked files plus `RESEARCH.md`, and inspect newly added current-theory/root-foundation pages for relevance.

## 研究后的维护流程 / Post-research maintenance workflow

1. 从仓库指令与当前 `RESEARCH.md` 开始，检查 Git 状态，保留其他会话的工作。运行 `--changes` 查看已关联来源的变化及新增/删除页面。
2. 重读变化的原文；新页面先判断是否进入本理论链。核对当前结论、明示假设、反例、中文与英文意义、原有回执与当前源码是否仍对应。只有来源真的支持，才升级完成状态。
3. 如有相关变化，编辑同一 JSON 中的两种语言、状态和链接；新增相关命题可以增加行，旧结果被替代时保留可追溯入口，不抹去反例。只有内容或链接改变，才更新内容日期及本记录的实质变更条目。
4. 对实际重读且已修订或确认的文件使用 `--record-review`；检查新增/删除文件的相关性后使用 `--record-discovery-review`。不要只刷新哈希掩盖未读的变化。
5. 运行 `--render` 与 `--check`，确认本地链接、锚点及生成内容。必要时在仓库首页或主理论入口保留导航，但不重新生成或重写并行维护的总成果目录。
6. 没有实质变化则不改表、不重复运行Lean或经验实验。维护任务不自动延伸理论、不向其他聊天发送消息、不更改原始来源，也不提交其他会话的文件。

Read changed sources before updating both languages. Preserve conditional scope, counterexamples and provenance. A changed fingerprint is a prompt to review, not permission to assert a stronger conclusion. With no relevant content change, leave the table unchanged and avoid redundant proof or experiment runs. Index maintenance does not authorize new research, messaging other chats or rewriting parallel catalogues.

从仓库根目录使用 / From the repository root:

```sh
python3 _process/research/2026-10-05-generative-foundation-review/root-foundation/build_generative_chain.py --changes
python3 _process/research/2026-10-05-generative-foundation-review/root-foundation/build_generative_chain.py --record-review path/to/actually-reviewed-source.md
python3 _process/research/2026-10-05-generative-foundation-review/root-foundation/build_generative_chain.py --record-discovery-review
python3 _process/research/2026-10-05-generative-foundation-review/root-foundation/build_generative_chain.py --render
python3 _process/research/2026-10-05-generative-foundation-review/root-foundation/build_generative_chain.py --check
```

`--record-review` 的示例路径需要替换为实际已读文件；它不自动更正文字。渲染会拒绝未确认的已关联来源变化。新增页面仍由维护者判断，不自动复制章节或新增结论。

## 日程已取消 / Schedule cancelled

Ren 随后要求：“把之前每天更新的规则去掉”。已通过应用工具删除“更新中英生成理论链”自动任务（原标识 `automation`），每日09:00检查不再执行。仓库指令、阅读文档及生成器已移除有效的每日安排；现有文档和研究发生变化时的同步维护保留。

Ren subsequently requested removal of the daily update rule. The app tool deleted “更新中英生成理论链” (former identifier `automation`), ending the daily 09:00 check. Repository instructions, the reading document and its renderer no longer prescribe daily upkeep. The document and maintenance during relevant research remain available.

[后续原话 / Follow-up directive](../../../../sources/15-codex-theory-conversations/2026-10-08-cancel-daily-theory-chain-update.md)取代先前的日程授权；原始请求与初次检查回执保留历史范围，不代表仍有活动日程。 / The follow-up supersedes the scheduling authorization; the original request and initial receipt remain historical records, not active schedules.

## 初次核验与保存 / Initial verification and preservation

三路材料核读分别整理核心命题、机制与应用、形式支撑；主作者汇合并去除重复的良知主行，补入所引核心候选、非最大化限定及有限认识范围。数学整理核对7份既有回执的17项源码绑定，没有重跑编译。表格整理本身没有新增定理、经验结果或伦理证明。

Four shared-file pre-edit byte snapshots and original link bases are recorded in [the preservation manifest](development/generative-chain-index-before/PROVENANCE.json). Existing unrelated edits remain preserved. The [initial checks](GENERATIVITY-CHAIN-INDEX-CHECKS.json) record the generated table, references, source fingerprints and the precise shared-file additions; these are editorial checks, not scientific revalidation.

## 更新记录 / Changes

| 日期 / Date | 变化 / Change |
|---|---|
| 2026-10-08 | 建立62项中英理论链索引、来源版本和维护流程；安排用户要求的每日变化检查。 / Created the 62-entry bilingual chain, source versions and maintenance workflow; arranged the requested daily change check. |
| 2026-10-08 | 按后续指令删除每日自动任务并移除每日维护规则；理论内容保持不变。 / Deleted the daily automation and removed the daily-maintenance rule at Ren’s subsequent request; theory content unchanged. |

## 交付前独立复核 / Independent editorial review before delivery

两路独立复核确认主链范围、双语及条件性结论区分；据此修正 C21 英文漏掉的“此前不能共同发生”，将 C09 的绝对不可能改为推理不足，并明确箭头仅为阅读主线。交付前纳入并行完成的 G0—K 取舍候选、必要损失与有限认识检查、已成立比较的减损传递，以及生命依存和恢复的证据入口。新增 F13、F14，合计62项；同一形式包在概念行和形式行重复链接，不重复计为新成果。

Two independent editorial reviews accepted the chain’s general scope and distinctions, while prompting a restored condition in the English C21, a weaker and accurate inference claim in C09, and clarification of the reading order. Newly available tradeoff, loss-comparison and living-dependency evidence was incorporated before delivery. F13 and F14 bring the index to 62 entries; repeated links do not count as independent results. The extra formal bindings are recorded in [the supplemental receipt check](GENERATIVITY-CHAIN-EXTRA-FORMAL-CHECKS.json). No scientific checks were rerun for this index.
