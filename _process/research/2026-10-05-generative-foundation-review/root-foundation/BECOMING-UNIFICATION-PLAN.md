# The Theory of Becoming：整合为一个理论的方案 / Unification plan

2026-10-09，Asia/Bangkok。AI（Claude）应 Ren 的要求撰写：先是“请发一个或者几个subagent……整体看一下整个repo，然后再决定，怎样是最elegant的方法，然后给我一个plan”。之后 Ren 指示“你自己全改了吧……先更新好计划，然后再一步步完整完成，保持代码和整体结构优雅”（[原话与解释](../../../../sources/15-codex-theory-conversations/2026-10-09-one-theory-unification.md)）。

依据：
- 四份只读普查（Lean 形式层、理论文档、基础设施、统一抽象设计）及主会话的独立复核；
- 承接[核心与伦理同构审查](CORE-ETHICS-ISOMORPHISM-AUDIT.md)。

本文是计划，不新增定理或成果记录；[原型](development/becoming-spine-prototype/README.md)只作开发草稿保存。

**修订（同日）。**
1. 第 6 节的决定已全部定下。
2. 第 2、3 节加入评价者路线的重组：G0 等于 S0 加边界中立，D 等于外在论表述加立场中立。
3. P3 从“复制移植”改为“实例化”：通用模块本来就对抽象接口多态，复制只会造出重复代码。
4. 模块数按直接重扫更正（第 1 节）。

## 0. 结论

**不在原处改写，在核心上加一条“脊柱”，让伦理成为同一语言中的公开前提。**
- 核心 `Generative.Process` 保持不动。
- 在它上面加几层薄层：先给状态加上主张赋值，再加运行、可达与探究范围，再加 Becoming 的更新／消耗分类。
- 最后加 Universal Metaethical Core。它只是一组具名前提及其推论，没有自己的世界模型。

既有的伦理模块不复制、不改写：
- 通用模块对抽象接口（`Inventory`、`Continuations`、`Robust` 等）多态，脊柱给出这些接口的实例，它们的全部定理就直接作用于脊柱。
- 只有三类地方需要新证明：
  - 一个模块重建了核心已有的组合子，需要证明二者等价；
  - 函数式单一结果需要推广为关系式结果，这时要用提升规则 L；
  - 规范前提需要重组。

叙述层只新增一章正典入口，不改任何已被记录绑定的章节。

## 1. 普查得到的事实

**形式层**
- 工作源码 561 个模块、10,648 条定理，无 `sorry`、无自定义公理；58% 传递导入核心。
- `Process` 只在核心中声明一次；`State` 被重新声明 75 次，`Event` 83 次。
- 重复的组合子：
  - 约 22 个自建 `Trace` 归纳类型；
  - 约 12 个 `Reach` 副本，`BecomingReversibility.Reach` 与 `GeneratedPaths.Reach` 逐字相同；
  - 8 种“忠实变换”；8 条储备或更新界；303 处手写的轨迹归纳。
- 伦理族（`universal-ethics` 及其子目录）共 128 个模块、约 30,500 行、2,220 条定理。
  - 其中 45 个含类型多态定理（约 10,800 行、758 条）；以多态定理为主的 18 个（约 4,600 行、288 条）。
  - 先前报的“34 个、约 8,600 行”是普查粗估，以此处直接重扫为准。
  - 其余是具体有限例子，平均每条定理约 14 行，多由 `decide`、`simp`、`rfl` 完成。
- 携带 G0 的 24 个模块都不接核心。
- 叶子：40 个模块依赖 Mathlib（工具链 4.30.0-rc2），另有序理论与模型论、Rat 市场动力学。概率在全仓都是有限权重，暂不需要随机过程层。

**记录层**
- 84 条以上的记录、49 条 `formal-reuse` 依赖边、128 条“关联而非已证转换”。
- 伦理族（F07）没有一条 formal-reuse 边进入核心族（F01）。
- `relational-renewal-classification`（F01）与 `renewing-consuming-formation`（F07）是同一种分类的两层表述，互不相通。

**叙述层**
- `chapters/` 共 138 章、5 MB。
- G0／J 前提表在 7 章中重复且不一致；“Universal Metaethical Core” 不出现在任何章节中；阅读目录漏掉 31 章。

**基础设施**
- 没有 lakefile；约 430 个按模块的检查器。
- 改动一个被绑定的源文件，会使所有绑定它的记录漂移；新增文件不引起漂移。

## 2. 结构

```text
L0  Core        Process / Trace / Feasible / projection（不改）
L1  Frame       Frame = Process + realized : S → C → Prop；Run、Reach、不变量、历史 (s, t)、Novel
L2  Inquiry     CommonResponse、After、Sound（导入 InquirySufficiency，不重定义）；
                Scope = 一个 sound 策略从所信状态实际执行所到达的端点
L3  Renewal     Run 上可观测量给出 RelationalRenewal 的展开；更新／消耗分类；
                generative = 更新型形成，是整体展开的一部分（Ren：generative is a part of its manifold）
L4  Metaethics  Universal Metaethical Core（具名前提与推论）
      S0  某一立场下，自身的生及继续生成有正面意义（种子；第一人称）
      N   边界中立：下面三条规则不受已形成边界的限制
          N_rel  正面意义沿非零的已形成关系传递到生生（承受者一侧：自他、亲疏、物种、时间距离）
          N_std  对生生的正面意义不随评价立场而取消（立场一侧）
          A      在所见范围内确保自身立场下的正面内容，且有通达 → 支持理由（受话者一侧：不以认同为条件）
      C   多实现生生内容的扩展接续严格更好
      L   把结果间比较提升到回应间比较的规则（默认：每个结果优于每个结果）
      J1–J4  保护优先、序、责任分配、正当选择
      对应条件：E（形成对应）、连通（已形成关系把相关生生连在一起）、generative 取关系读法
    定理：
      G0 ⇔ 种子 ∧ N_rel ∧ N_std（在连通整体上）——Ren 的 G0 的内容刻画，不是替换
      D  ⇐ A ∧ N_std ——已有 positioned-positive-reason 的前提 D 由此得出
      极小性：去掉任一项都有一致的反模型；每个对手都恰是同一规则加上一条已形成的边界
Leaves          ℝ/Mathlib、序理论、Rat 市场：作为叶子包，只在实际用到时补适配
```

Lean 中 L1–L4 是包 `Becoming` 的模块 `Becoming.Frame`、`Becoming.Inquiry`、L3 的 `Becoming.Renewal`、`Becoming.Dependence`、`Becoming.Return`、`Becoming.Horizon`、`Becoming.Joint`、`Becoming.Substitution`，以及 L4 的 `Becoming.Metaethics`、`Becoming.Ranking` 与 `Becoming.Correspondence`；`import Becoming` 导入全部。既有模块经 `Becoming.Bridge` 连到核心，它在包内但不属核心（[包说明](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/README.md)）。

**为什么这样最简洁：**
- **一个世界模型。** 伦理是同一语言中的前提，不另立模型。这正是非二元方法的要求。
- **所见范围由动力学给出。** 它是 sound 策略实际执行所到达的端点，不再是可以随结论挑选的自由参数。
- **位置是被实现的主张，没有行动者原语。** 理由随位置的形成而形成。
- **对手全部是同一种形状。**
  - 承受者一侧：门槛论、闭合论、只算自身谱系者，都是把传递规则限在一条已形成的边界内。
  - 立场一侧：立场相对论者限在自己的立场内。
  - 受话者一侧：内在论者限在认同者内。
  - 仓库里已有的句子“A role's existence cannot certify its own normative authority”（UNIFIED-ETHICAL-GROUNDING 的中心问题），在形式上就是：这些规则的边界限制都要拿掉。
  - 是否接受这一点是一项规范前提，本体论推不出它（审查 P5）。
- **复用而不复制。** 忠实变换就是核心的 `trace_map`／`trace_lift`；`Robust` 在定义上就是 `CommonResponse`；通用伦理模块经接口实例化直接作用于脊柱。

## 3. 整合暴露出的实质发现

1. **隐藏前提 L。** `Situation.realize` 是函数，`Process.step` 是关系。只要对回应作 J 序比较，就需要一条提升规则；传递性还需要中间回应可行。
2. **所见范围可以由动力学定义。** 这收窄了正面根据结果中一个原本由应用自行给出的参数。
3. **更新／消耗是同一个分类。** 两条记录、`Depletion`、`ContinuationRenewal` 及 8 条储备或更新界，可以统一为 `Run` 上可观测量的性质。对应 Ren 的 G0 时，`generative` 由这一分类给出，不由应用自行指定。把形式读法认作生生，仍是对应，不是 Lean 结果。
4. **G0 的内容可以刻画。** 在连通整体上，G0 等价于“某处有一个生生被珍视”加两条边界中立规则。
   - G0 中超出“评价者本来就持有的东西”的全部内容，因此精确落在边界中立上。
   - D 的“不以认同为条件”来自 A 与 N_std。A 是关于有贡献理由的外在论表述。
   - 这把[评价者路线审查](EVALUATOR-GROUNDING-REVIEW.md)要求的 BI、P+ 与“立场到规范的桥”统一为同一形状的三条规则。
   - 它没有证明这些规则为真，也不及于不接受它们的立场。

## 4. 迁移不变量

- **只增不改。** 不编辑、不移动既有被绑定的源码、回执和章节，也不重跑旧检查器。例外：本会话接手的评价者路线，审查明确要求修改其 Lean 说明，改后重跑该模块自己的检查器，旧运行保留在其 `checks/` 目录中。
- **新目录与约束。** 放在 `experiments/.../generative-basis/lean/becoming/`，命名空间 `Becoming`，工具链 4.29.1。新声明的公理报告必须为空，检查器强制。P5a 起核心只用 Lean 内置前导；P5b 起它是 Lean 包 `Becoming`，模块名全仓唯一。
- **一个合并检查器。**
  - 自动解析导入闭包，按依赖顺序编译；
  - 对继承模块断言当前哈希等于其历史回执中的 `source_sha256`；
  - 新旧模块的审计数分别报告；回执文件名唯一。
- **记录方向为 core → spine → ethics。** 只有当一条具名桥接声明证明了转换时，才把 `related` 升级为 `formal-reuse`。
- **转换定理写明方向。** 能证等价就证 iff；只能单向时如实写出，不悄悄削弱前提。
- **规范桥按组合登记。** 它们与符号无关；价值来自动力学给出的 `secured` 和对前提的诚实刻画。

## 5. 阶段

| 阶段 | 内容 | 验收 |
|---|---|---|
| P0 ✓ | 本线提交 78f1abda；整库检查点 4e7642e1 | 已完成 |
| P1 脊柱 ✓ | `BecomingFrame`：Frame、Run（含窗口即轨迹）、Reach、不变量、历史、Novel。`BecomingModal`：Scope、sound 策略确保其目标、反单调性。合并检查器 `check_becoming.py` | 已完成（d79d0d9d）：空公理；继承哈希与回执相符 |
| P2 伦理核心 ✓ | `MetaethicalCore`：S0、N_rel、N_std、A、C、L、J 的具名定义；G0 刻画定理；D 的导出；极小性反模型与“对手即有界规则”；脊柱上的普遍位置理由；提升规则 L。记录 `metaethical-core-characterization`；一页前提卡 | 已完成（d79d0d9d）：[metaethical-core-characterization](../../../../theories/becoming/results/records/metaethical-core-characterization.md) |
| P2b 评价者路线更正 ✓ | 执行[审查](EVALUATOR-GROUNDING-REVIEW.md) §6 的 15 项更正：论证文档、Lean 说明、记录 `self-good-reachable-g0`（收窄标题与主张）、G0-WARRANT 相关段；P+ 版第二步由 P2 承担 | 已完成（001c5cdd）：记录与审查逐项对应；该模块检查器重跑通过 |
| P3 实例化 ✓ | 先用脚本对 45 个含多态定理的模块分类，结果存入本研究。再按接口逐一处理：给出脊柱实例；对重建核心组合子者证明等价（`Robust`、`Reached`、`revise`、`Guarantees` 等）；函数式结果用 L 推广。相应记录增加证明绑定，按具名声明升级 `related` 链接 | 已完成：[分类表](BECOMING-INSTANCE-CLASSIFICATION.md)覆盖 45 个模块并逐行机械检查；11 个接口都有具名实例或等价定理（`BecomingInstances`），记录 [becoming-spine-instances](../../../../theories/becoming/results/records/becoming-spine-instances.md)。证明绑定放在新记录上，既有记录按原范围保留不改；新记录以 `related` 连到它们，唯一的 `formal-reuse` 是对 C 与 L 的直接使用 |
| P3b 更新／消耗统一 ✓ | 由 Run 可观测量构造 `RelationalRenewal` 的展开，`RenewalComparison` 的关系读法成为脊柱上 `generative` 的规范读法；`Depletion`、`ContinuationRenewal` 的储备界作为同一分类的实例 | 已完成：[整合与作者反审](BECOMING-RENEWAL-READING.md)，记录 [becoming-renewal-reading](../../../../theories/becoming/results/records/becoming-renewal-reading.md)。`BecomingRenewal` 为 L3；读法在 `MetaethicalCore` 中由 L4 使用 L3 给出。三条界的统一是组织性的；`ContinuationRenewal` 的良基形式更一般，不由该原则导出 |
| P4 叙述 ✓ | 新正典入口 `THE-THEORY-OF-BECOMING`：Becoming、组织与演化、认识与探究、集体动力学、评价的形成、Universal Metaethical Core、AI 对齐、开放纲领。附术语表与前提卡；旧章作为证据链接，并在新章中标为历史证据；README 首段指向它；补齐阅读目录 | 已完成：正典章节（2bcf314b）。阅读目录补齐 32 个缺项；17 个过期条目先读原文差异再更新字段与版本标记；生成视图（CLAIMS、理论首页）以生成清单为准，记为 `generated-view`，其各行随成果记录检查；Lean 文本目录重新同步。两项目录检查、渲染、`research-check` 与 36 项测试通过 |
| P4b 工作规则 ✓ | AGENTS.md 增一条：新的形式结果陈述在脊柱上；脊柱表达不了时扩展脊柱，而不是另建模型 | 已完成：规则在 AGENTS.md「Evidence and preservation」首条，链接正典章节 §9 与脊柱目录 |
| P5a 核心纯净 ✓ | 按 [Ren 的要求](../../../../sources/15-codex-theory-conversations/2026-10-09-pure-core.md)：核心（L0 及其两个基础模块，加 L1–L4）不导入核心以外的模块，公理报告全空，只用 Lean 内置前导即可编译。G0、C、D 与确保的正面根据在核心陈述；桥接层以 `Iff.rfl` 证明既有模块的定义即核心定义；J1/J2 的 `BetterAt` 与 `living_iff_relational` 移到桥接层 | 已完成：检查器每次核对闭包、空公理报告与仅用前导编译；80 项定理／146 项声明审计 |
| P5b 包结构 ✓ | 核心改为 Lean 包 `Becoming`，按所述之事命名：`BecomingFrame` → `Becoming.Frame`，`BecomingModal` → `Becoming.Inquiry`（它讲探究的所见范围，不是模态逻辑），`BecomingRenewal` → `Becoming.Renewal`，`MetaethicalCore` → `Becoming.Metaethics`，`BecomingInstances` → `Becoming.Bridge`；根模块 `Becoming` 导入四层。声明名不变，记录别名照旧有效；上面各行保留当时的模块名 | 已完成：检查器按包路径命名模块并核对闭包；记录、章节与链接改到新路径；包说明给出读者入口与新旧名对照 |
| P5c Mathlib 叶子 ✓ | 不建 Lake 工作区：Mathlib 已安装（既有检查器经 `SYSTEMS_MATHLIB_PROJECT` 使用 `~/repos/生生不息`），沿用 Python 检查器。外围桥接模块导入核心与 Mathlib 叶子，证明其接口是核心的实例，用 4.30.0-rc2 编译；核心不导入它 | 已完成：核心增“判断即一步探究”（`judgeProcess` 由桥接层移入 `Becoming.Inquiry`，`commonResponse_judge_iff`），核心 81 项定理／147 项声明审计。外围桥接 `CorrectionInquiry`（7 项定理，公理报告全空）证明 `CorrectionBoundary` 的实施与共同行动、`ObservationChange` 的安全选择都是每个观察格上的共同回应，两模块的细化定理由 `commonResponse_antitone` 导出；核心在 4.30.0-rc2 下同样编译通过。其余三个叶子是具体模型或关系代数，核心没有对应接口，分类表写明理由 |
| P6 动态依存与逐步读法 ✓ | 按 Ren 的[指示](../../../../sources/15-codex-theory-conversations/2026-10-09-pure-core.md#rens-follow-up-finish-the-renames-then-continue-the-theory)“move on to pursue the theory of becoming, and prove the necessary proofs”，扩展脊柱而不另建模型：L3 新模块 `Becoming.Dependence` 让依存、所需水平与汲取读取配置，重做 `Renewed`／`Consumed`，并给出逐步读法；L4 增加逐步的关系读法 `Web.valuation` | 已完成：[研究 §6](BECOMING-RENEWAL-READING.md#6-动态依存与逐步读法p6)，记录 [becoming-dependence-dynamics](../../../../theories/becoming/results/records/becoming-dependence-dynamics.md) 与 [becoming-stepwise-reading](../../../../theories/becoming/results/records/becoming-stepwise-reading.md)。依存不变时精确复原静态读法；变化发生在步上；损失的终止、转化与恢复由定理相互约束，同一过程中三者都实际发生；逐步与整段读法两个方向都有分歧。核心 84 项定理，连桥接共 116 项定理／225 项声明审计，公理报告全空；外围桥接重跑通过。整体演绎仍开放 |
| P6b 独立审查与更正 ✓ | 另一 agent（Claude Opus 5.5，未参与撰写）独立审查 P3b–P6：[审查](BECOMING-RENEWAL-READING-REVIEW.md)。数学接受，关系读法的哲学根据未确立，要求二十项更正 | 已完成：[研究 §7](BECOMING-RENEWAL-READING.md#7-独立审查与更正)。逐步 living 由“在更新之内”改为“活跃且不侵蚀”（`UnderminingAt`）：先按审查 Q12 改为“不断裂”，再因 `drawing_after_loss` 改为“不侵蚀”；三个候选连同使它们不被采用的见证都保留在核心中。新增关系层读法 `Web.relations` 与 `living_iff_relations`；`Unmet.consumed_without_loss` 披露继承的 `Consumed` 不要求依存曾被满足。散文更正落在研究、章节、模块说明与记录中 |
| P7 回程、视界、共同活动与替代 ✓ | 承接 `relational-renewal-classification` 与 `becoming-dependence-dynamics` 的下一步，以及审查对读法比较与判据的要求；仍按“prove the necessary proofs” | 已完成：[研究 §8](BECOMING-RENEWAL-READING.md#8-回程视界共同活动与替代p7)。L3 新增 `Becoming.Return`（回程等级，消耗恰是不再回程，周期读法）、`Becoming.Horizon`（有限前缀不决定分类）、`Becoming.Joint`（but-for 差别制造在多重决定下与关系参与分离）、`Becoming.Substitution`（支持门控定律中替代保持消耗）。记录 [becoming-return-grades](../../../../theories/becoming/results/records/becoming-return-grades.md)、[becoming-finite-horizon](../../../../theories/becoming/results/records/becoming-finite-horizon.md)、[joint-difference-making](../../../../theories/becoming/results/records/joint-difference-making.md)、[substitution-preserves-consumption](../../../../theories/becoming/results/records/substitution-preserves-consumption.md)。核心闭包 13 个模块；连桥接共 169 项定理／332 项声明审计，公理报告全空；外围桥接重跑通过。读法比较给出两条形式约束；哪种读法是生生的读法，由 Ren 选择 |
| P8 C 在各读法下的排序 ✓ | 把研究 §8.5 中只作了论证的代价在核心上证明：逐步读法下 C 是否仍把过度汲取者的不在场排在其在场之上 | 已完成：[研究 §9](BECOMING-RENEWAL-READING.md#9-c-在各读法下的排序p8)。L4 新增 `Becoming.Ranking`：不在场扩展在场，仅当读法扣下该形成的每个事件；整段读法下 C 把不在场排得更高（在核心上重述 relational-reading-comparison，桥接证明读法与水平相同）；逐步读法下 C 不决定，恶性增殖与以消耗取胜都是实例；共享对以消耗取胜的排序在逐步读法下保持。记录 [ranking-under-readings](../../../../theories/becoming/results/records/ranking-under-readings.md)。核心闭包 14 个模块；连桥接共 186 项定理／361 项声明审计，公理报告全空；外围桥接重跑通过 |
| P9 条件的对应纪律 ✓ | 第一次独立审查列出的第一种会改变其判断的结果：一条排除惰性或虚设条件的对应规则，并证明在声明的类中连通仍成立 | 已完成：[研究 §10](BECOMING-RENEWAL-READING.md#10-条件的对应纪律p9)。L4 新增 `Becoming.Correspondence`：一方汲取、另一方以正水平依存，两个事件才经由该条件相关；惰性条件不构成关系，加入它不改变 living、关系与连通（Q4 排除）；每个侵蚀关系都是交互；有活的汲取者与活的依存者的共同条件仍使整体连通，G0 在那里恰等于种子加 N_rel 加 N_std；连通由活的使用造成；人人汲取并依存的被更新条件排除不了，是应用义务。记录 [condition-correspondence-discipline](../../../../theories/becoming/results/records/condition-correspondence-discipline.md)。核心闭包 15 个模块；连桥接共 207 项定理／395 项声明审计，公理报告全空；外围桥接重跑通过 |
| P7b 第二次独立审查与更正 ✓ | 另一 agent（Claude Opus 5.5，未参与撰写）独立审查 P7 与“不侵蚀”的选取：[审查](BECOMING-P7-REVIEW.md)。数学接受；`UnderminingOn` 与 but-for 的定义须修正；散文七处强于 Lean；§8.5 的表在 (a)(b) 与 but-for 一栏上不公允 | 已完成：[研究 §11](BECOMING-RENEWAL-READING.md#11-第二次独立审查与更正p7b)。侵蚀改为要求依存在其成立期间曾被满足（`MetSince`）；but-for 固定实际所取的动作（`BreaksBy`，`Shock`）；视界结果在有反馈的支持门控定律中成立（`Feedback`），按数量的读法逃出它（`amount_reading`）；整段与步层面的差别制造分开；替代的保持只对整段读法成立（`stepwise_credits_substitution`）；(b) 只部分满足（`Pool.within_share_undermines`、`Pinned`）；逐步读法下 C 仍把节制排在过度汲取之上（`malignant_restraint`），代价限于与不在场的比较。“采用”改为待 Ren 选择的工作候选。七个记录更正、五个记录改指新回执。核心闭包 15 个模块；连桥接共 236 项定理／451 项声明审计，公理报告全空；外围桥接重跑通过 |
| P9b 第三次独立审查与更正 ✓ | 另一 agent（Claude Opus 5.5，未参与撰写）独立审查 P8、P9 与 P7b 的更正：[审查](BECOMING-P8-P9-P7B-REVIEW.md)。数学接受；`MetSince` 比较现在的所需；依存中断一步即抹去历史；but-for 须动作可取；逐步读法的代价、节制、替代与交互的说法强于 Lean | 已完成：[研究 §12](BECOMING-RENEWAL-READING.md#12-第三次独立审查与更正p9b)。`MetSince` 比较那一步的所需（`FallingNeed`、`RisingNeed`）；依存的一段须不间断，作为应用义务披露（`Gap`）；`MakesDifference` 要求动作可取，`Determined` 写明检验何时合乎其意（`Hidden`、`Tagged`）；逐步读法失去与不在场的比较须有被记入的事件（`Immediate`），节制的结论限于二元定律族（`ThirdParty`），替代者被扣下到转向为止（`slow`）；交互是结构上的共现，传递由汲取承担（`drawing_reaches`），剩余的免费连通只需一次使用（`one_use_connects`）；“没有它更好”标为 C 的 AI 形式路线。六个记录更正，另五个记录改指新回执（becoming-dependence-dynamics 并改计数）。核心闭包 15 个模块；连桥接共 265 项定理／502 项声明审计，公理报告全空；外围桥接重跑通过 |
| P10 继续生成 ✓ | 第一次独立审查的判据 (d) 与研究 §7.3 第 4 项：现有读法都不含继续生成的成分 | 已完成：[研究 §13](BECOMING-RENEWAL-READING.md#13-继续生成生起不息与更新p10)。L3 新增 `Becoming.Generation`：生起与不息的生成；有限条件家族只能支付有限次事件；生起由家族支付、上升由形成的更新造成时，不息的生成需要更新复现；更新不蕴含生成（`renewal_without_generation`）；以消耗进行的生成停止（`Growth`）；替代推迟终结而不逃脱（`Relay`）；总水平不升的有限家族不能维持不息的生成；逐步读法扣下一个不息再生起的形成的每次开花（`Bloom`）。只形式化 Ren 原话中的“不断…生”，不含“更多”。记录 [unceasing-generation-needs-renewal](../../../../theories/becoming/results/records/unceasing-generation-needs-renewal.md)。核心闭包 16 个模块；连桥接共 283 项定理／541 项声明审计，公理报告全空；外围桥接重跑通过 |
| P11 更多 ✓ | `unceasing-generation-needs-renewal` 的下一步：陈述 Ren 原话中的“更多” | 已完成：[研究 §14](BECOMING-RENEWAL-READING.md#14-更多流供给与更新者p11)。L3 新增 `Becoming.Flow`：条件作为形成取用与给予的数量；平衡的流的账目；平衡且只有活跃者给予时，每次上升由给予它的形成造成（P10 的前提 `RenewedBy` 成为定理；P18b 用语，原文“给予者”）；读作“从某步起取用者至少任意多”的更多，需要供给没有最终的界，每个形成给予有限时需要给予的形成的数目没有最终的界（`Garden` 满足全部前提；P18b 用语，原文“给予者”）；不息的开花尚不是更多（`Bloom.not_more`）。可能性、多样性与复杂性不在其中。记录 [more-needs-renewers](../../../../theories/becoming/results/records/more-needs-renewers.md)。核心闭包 17 个模块；连桥接共 311 项定理／588 项声明审计，公理报告全空；外围桥接重跑通过 |
| P11b 第四次独立审查与更正 ✓ | 另一 agent（Claude Opus 5.5，未参与撰写）独立审查 P9b、P10 与 P11：[审查](BECOMING-P9B-P10-P11-REVIEW.md)。数学接受；所需增长后，`MetSince` 抹去曾被满足的水平；`Paid` 不涉及生起的形成；严格性所引见证没有上升；“任何有限部分都不能独自不息”需要耗散；“严格的层级”作为蕴含不成立；`More` 数的是取用者；“给予者越来越多”只在平均意义上成立；支付与账目用语与 Ren 的纠正相冲突 | 已完成：[研究 §15](BECOMING-RENEWAL-READING.md#15-第四次独立审查与更正p11b)。侵蚀取最小形式 `MetAbove`（`Stunted`）；`Joint` 加入 `determined_dichotomy`；`Paid` 改为 `Depletes` 并照实说明（`depletes_iff`、`Tide.unrelated_depletion`）；严格性改引 `Tide.renewal_without_arising`；`dissipation_ceases` 写明耗散前提，没有耗散时 `Recycle` 不息；流的形式 `replenishment_recurs`（`ArisesTaking`，`Garden.undepleted`）；平均下界 `replenished_over`、`renewers_over`（`Pulse`）；补充者可以就是取用者（`Cycle`）。L3 新增 `Becoming.Population`：在活跃形成的普查与 `Taking` 之下更多蕴含不息（严格，`Bloom.counted`），没有它们时不蕴含（`Dormant`、`Inactive`、`Crowd`）。用语改为消耗、补充、取用与补充者。七个记录更正，另六个记录改指新回执。核心闭包 18 个模块；连桥接共 376 项定理／688 项声明审计，公理报告全空；外围桥接重跑通过 |
| P12 跨步的同一 ✓ | 开放纲领“动态依存”一行与 becoming-dependence-dynamics 的下一步：形成的个体化；终止与转化之分依赖外给的同一 | 已完成：[研究 §16](BECOMING-RENEWAL-READING.md#16-跨步的同一改名改认与接续p12)。L3 新增 `Becoming.Identity`：改认在每一步把两种命名一一对应，每一步的关系不变；改名保持全部读法；任何改认保持每一步的关系、每个条件的类、`Dependent`、每个事件是否在更新之内与是否断裂，以及流的取用与给予、取用者与补充者的数目、`More`、普查与 `Taking`，所以在普查之下更多在每个改认下蕴含不息（`More.unceasing_reidentified`）；只改动谁延续谁，形成的类、侵蚀、转化与生起都改变（`Turnover`）；保持持续活动的改认不制造生起，保持持续依存的改认不去掉侵蚀（`KeepsActive`、`KeepsTenure`）；接续仍开放（`Lineage`、`Succession`）。记录 [identity-across-steps](../../../../theories/becoming/results/records/identity-across-steps.md)；P11b 时漏记的第四次审查补入五个记录的检验范围。核心闭包 19 个模块；连桥接共 422 项定理／760 项声明审计，公理报告全空；外围桥接重跑通过 |
| P13 耗散 ✓ | 第四次独立审查 H6、H12：“任何有限部分都不能独自不息”“没有一个有限的部分独自承担”需要耗散前提 | 已完成：[研究 §17](BECOMING-RENEWAL-READING.md#17-耗散复现的取用打开有限家族p13)。L3 新增 `Becoming.Dissipation`：封闭（`ClosedAt`）与耗散（`DissipatesOn`、`Dissipative`）；平衡的流中，被耗散的家族跨一步至少下降其取用者的数目（`runs_down`），此后取用者的总数不超过存量（`takers_within`），取用不再复现（`taking_ceases`）；在耗散之下，取用复现的有限家族连同包含它的每个有限家族在任意晚的步都与其外交换（`Dissipative.opens`、`More.opens`、`opens_of_arising`）；条件总共有限时取用终止（`finite_ceases`）；`Frontier` 满足全部前提并且不止地更多。记录 [no-finite-part-bears-taking](../../../../theories/becoming/results/records/no-finite-part-bears-taking.md)。核心闭包 20 个模块；连桥接共 450 项定理／798 项声明审计，公理报告全空；外围桥接重跑通过 |
| P14 角色 ✓ | 第四次独立审查 H14：把形成与条件分为两类，省略了“生作为生的条件” | 已完成：[研究 §18](BECOMING-RENEWAL-READING.md#18-角色生作为生的条件与经由给予的生起p14)。L3 新增 `Becoming.Roles`：一类关系项的读法（`Web.roles`、`Flow.roles`）保持列出的全部读法，其中曾活跃的形成既不体现也不承担自身；体现（`Embodied`）与承担自身（`SelfBearing`）；在 `Dependent` 之下，依存于体现关系项的形成只在它活跃时活跃，不活跃的关系项终结每个依存链到达它的形成（`coextinct`）；在承担自身的体现关系项终结之步汲取它是断裂（`ending_breaks`）；在平衡且只有活跃形成给予的流中，体现的关系项只经由另一个活跃形成的给予而生起（`arises_given`；P16b 更正标题，给予它的形成不必体现；P18b 用语，原文“给予者”）；见证 `Mutualism`、`Predation`、`Brood`。L4 的 `Becoming.Correspondence` 新增一节：一类读法保持两种估值的连通；汲取承担自身的关系项与它的每个活跃事件相互作用，互利者无需第三个条件就连通，不承担自身时两种估值都不关联它们。记录 [life-as-condition-of-life](../../../../theories/becoming/results/records/life-as-condition-of-life.md)。核心闭包 21 个模块；连桥接共 513 项定理／878 项声明审计，公理报告全空；外围桥接重跑通过 |
| P12b 第五次独立审查 ✓ | 第五次独立审查（[审查](BECOMING-P11B-P12-REVIEW.md)）I1–I12：P11b 与 P12 的数学全部接受，问题在前提的陈述、散文与对应 | 已完成：[研究 §19](BECOMING-RENEWAL-READING.md#19-第五次独立审查与更正p12b)。`Flow`：`uptake_needs_replenishment`（复现的取用需要复现的补充），`replenishment_recurs` 由它推出，见证 `Steady`；`Population`：`More.grows`，present 不重复的必要性（`Repeated`），全部前提的正面见证（`Garden.counted`、`Cycle.counted`），关系形式的鸽巢原理 `length_le_of_matched`；`Identity`：标签与名字跨步的模式之分，双向的连续（`Reidentify.back` 与四个双向定理、`Lineage.one_way`、`Succession.one_way`），`Dormancy`、`TideFlip`、`Layered`，活跃的继承者，延续关系与 `NoSplit` 之下更多迫使生起（`More.unceasingFrom`、`continuation_reidentify`），萌出时不然（`Budding`），交换名字的见证共用 `Reidentify.exchanging`。记录 identity-across-steps、more-needs-renewers 与 unceasing-generation-needs-renewal 更正，另四个记录补界限或用语。核心闭包 21 个模块；连桥接共 559 项定理／948 项声明审计，公理报告全空；外围桥接重跑通过 |
| P15 生成即补充 ✓ | 第五次独立审查 I3 与 §4 第 2 项：流的形式中生起只经由取用起作用，需要一个让生成本身承担要求的耗散定理；no-finite-part-bears-taking 的界限（不取用的生起）与 life-as-condition-of-life 的下一步（耗散之下的一类读法） | 已完成：[研究 §20](BECOMING-RENEWAL-READING.md#20-生成即补充生起本身承担要求p15)。`Becoming.Roles` 新增两节：平衡的流中体现的关系项至少被给予它生起时的水平（`Embodied.given_of_arises`），它的生起补充每个包含它的家族（`Embodied.replenishes`），体现的生成复现时补充复现，不论取用什么（`generation_needs_replenishment`）；`Becoming.Dissipation` 新增 `DissipatesOn.takes_of_gives`；在耗散之下封闭家族中体现成员的生起降低存量（`Embodied.arising_lowers`，推出 `dissipation_ceases` 的前提），体现的生成复现的有限家族从任何一步起都不封闭（`generation_opens`；P16c：交换可以与家族无关，被围住时汲入，`generation_draws_in`），关系项总共有限时它终将停止（`generation_ceases`）；见证 `Handing`（无耗散）、`Kindling`（满足全部前提）、`Flicker`（不体现）与 `Brood.not_dissipative`（原名 `Brood.costless`）。记录 [generation-is-replenishment](../../../../theories/becoming/results/records/generation-is-replenishment.md)。核心闭包 21 个模块；连桥接共 588 项定理／987 项声明审计，公理报告全空；外围桥接重跑通过 |
| P16 整体与部分 ✓ | 第五次独立审查 I10 与 §4 第 7 项：谱系与成员是两个层次，部分与整体的关系被省略；需要一个含部分与整体关系的表示 | 已完成：[研究 §21](BECOMING-RENEWAL-READING.md#21-整体与部分整体经由部分的生成而持续p16)。L3 新增 `Becoming.Wholes`（导入 `Identity`）：整体恰在某个部分活跃时活跃（`Whole`），只经由部分的生起而生起（`Whole.arises_part`）；从某步起每步活跃的整体，部分从不在相隔 d 步的两步都活跃时，每 d 步内有部分生起（`Whole.arises_within`，`Shifts` 表明界可达）；部分的活动都终结且活跃的部分可列出时，部分在任意晚的步生起（`Whole.needs_arising`）；`Immortal`、`Countless` 表明前提必要，`Gaps` 表明逆命题不成立，`Generations` 满足全部前提；`Layered.composed`。根模块文档中 Identity 一条按 P12b 更正。记录 [whole-persists-through-generation](../../../../theories/becoming/results/records/whole-persists-through-generation.md)，identity-across-steps 改指它。核心闭包 22 个模块；连桥接共 614 项定理／1028 项声明审计，公理报告全空；外围桥接重跑通过 |
| P16b 第六次独立审查 ✓ | 第六次独立审查（[审查](BECOMING-P13-P14-P12B-REVIEW.md)）J1–J11：P13、P14 与 P12b 的数学全部接受，问题在前提的陈述、散文与对应；两个反复出现的模式是省略前提与把所给的对应呈现为结果 | 已完成：[研究 §22](BECOMING-RENEWAL-READING.md#22-第六次独立审查与更正p16b)。`Dissipation`：封闭的步（`Enclosed`），耗散之下给予的形成在封闭的不重复家族上取得多于所给（`gives_less`）、给予须以取用为条件（`giving_needs_uptake`），没有封闭的步时耗散是空的（`Spray`），维持一个取用者已越出每个有限家族（`Lone`），生长者依存于池的前沿（`Rooted`），此前的见证都不耗散（`witnesses_not_dissipative`）；`Roles`：一类读法也保持 Acting、Taking、普查、present 不重复与耗散，哪个条件就是哪个关系项由共同的索引给出（`relabel`），终结之步的汲取不论是什么终结了生命（`Wilting`、`SelfBearing.met_iff`），`arises_given` 中给予的关系项不必体现（`SunSeed`、`arises_from_embodied`），`Brood.costless` 改名为 `Brood.not_dissipative`；`Correspondence`：重新标号保持两种估值的连通，体现不进入估值（`Mutualism.apart_embodied`）；`Identity`：没有分裂是充分的，不是必要的（`Fork`），`Merge`、`decideContinues`、`Dormant.no_split_without_arising`、`no_join`。“代价”一族用语改为“给予须以取用为条件”，属建议。四个记录更正，另四个记入审查。核心闭包 22 个模块（包 20 个）；连桥接共 676 项定理／1115 项声明审计，公理报告全空；外围桥接重跑通过 |
| P16c 第七次独立审查 ✓ | 第七次独立审查（[审查](BECOMING-P15-P16-P16B-REVIEW.md)）K1–K8：P15、P16 与 P16b 的数学全部接受；耗散空成立时“不封闭”可以由与家族无关的交换满足，“整体的持续就是部分的生成”与“生由生已证明”过强，`Merge` 的生起是重读 | 已完成：[研究 §23](BECOMING-RENEWAL-READING.md#23-第七次独立审查与更正p16c)。`Dissipation`：围住（`Around`）与只向内（`Inward`），被围住而取用复现的家族汲入（`taking_draws_in`），相等可判定时被封闭的步围住每个有限家族（`Enclosed.around`），`Frontier` 与 `Lone` 每步被封闭并汲入，`Frontier.gives_without_taking`、`Lone.repeated_family`；`Roles`：`arising_lowers_on`、`generation_ceases_on`、`generation_draws_in`，`SprayHanding`（结论由无关交换满足），`Kindling.around`、`draws_in`，`EmbodiedSun`（体现不等于是生命），假设 `givers` 改名为 `gives_embodied`；`Wholes`：覆盖（`Covered`）是两个定理的主语，`needs_new`，`whole_self`、`Immortal.each_other`，`Layered.brief`、`within`、`arise_again`；`Identity`：`Merge.idle`、`Confluence`。标题改为字面结论，“就是”改为“经由”，“给予者”改为“给予它的关系项”（用语属 Ren）。五个记录更正，其余改指新回执。核心闭包 22 个模块（包 20 个）；连桥接共 728 项定理／1182 项声明审计，公理报告全空；外围桥接重跑通过 |
| P17 储备 ✓ | 开放纲领“动态依存”一行的“放宽 `Dependent`（缓冲、储备、滞后）”；life-as-condition-of-life 的界限（种子库、储备与休眠之下共灭不必成立）与 generation-is-replenishment 的下一步（活动与水平不同步） | 已完成：[研究 §24](BECOMING-RENEWAL-READING.md#24-储备活动越过支持水平越过活动p17)。L3 新增 `Becoming.Reserve`（导入 `Roles`）：储备（`Web.Carries`）在形成不被支持时不上升、在其间活跃时下降，零储备恰是 `Dependent`（`carries_zero`），储备可以是所持条件的水平（`Flow.carries_of_held`）；从某步起不被支持的形成至多活跃开始时储备那么多次（`Carries.lasts`），所以滞后的终结与滞后的共灭推迟而不逃脱（`consumed_lasts`、`coextinct_lasts`），储备在休眠中衰减时休眠的时间也有界（`Decays`、`ends_within`）；`Seed`、`Viable` 与 `Famine` 达到这些界，`Famine` 读作依存转到脂肪上时满足 `Dependent`。开始作为条件而在（`Web.ComesToStand`）在 `Flow` 与 `Dissipation` 中陈述（`standing_given`、`standing_needs_replenishment`、`standing_lowers_on`、`standing_ceases_on`、`standing_opens`、`standing_draws_in`、`standing_ceases`），§20 与 §23 关于体现的定理改由它推出，陈述不变（`Embodied.comesToStand`）；活跃时作为条件而在的关系项若先前不在，就在活跃之前开始作为条件而在（`came_to_stand`、`Provisioned`），从休眠中醒来不开始作为条件而在（`Sleeper`）。记录 [reserve-defers-ending](../../../../theories/becoming/results/records/reserve-defers-ending.md)，推广 generation-is-replenishment。核心闭包 23 个模块（包 21 个）；连桥接共 774 项定理／1257 项声明审计，公理报告全空；外围桥接重跑通过 |
| P18 世系 ✓ | life-as-condition-of-life 的下一步“直接读出体现的估值”与 §18、§22 J5 的 `Mutualism.apart`（都体现而不相关）；`Becoming.Metaethics` 所列的世系没有读法，各由前一代给予的世代在两种估值下不相关 | 已完成：[研究 §25](BECOMING-RENEWAL-READING.md#25-世系关系项经由所依与所给直接相关p18)。L4 新增 `Becoming.Descent`（导入 `Correspondence` 与 `Reserve`）：以之为生（`Web.LivesOn`：在某步汲取一个关系项并以正需要依存于它）与世系（`Flow.Descends`：在一个关系项开始作为条件而在之步给予它），作为交互之外的两种 related（`sustenance`、`descent`）；以之为生不免费（`LivesOn.active`）；沿二者的 N_rel 传递（`living_on_reaches`、`lived_on_reaches`、`descent_reaches`、`ancestry_reaches`）；生起的体现关系项从给予它的活跃形成而来（`Embodied.descends`、`arisen_reached`）；世代由世系连通而不由共同参与或交互连通，G0 在那里恰等于种子加 N_rel 加 N_std（`Brood.descended`）；同一对应进入以之为生（`Mutualism.relabel_sustenance`）；世系跟着水平走（`Provisioned.descends`、`Sleeper.no_descent`）。是否采用属于 Ren。记录 [living-on-and-descent](../../../../theories/becoming/results/records/living-on-and-descent.md)。核心闭包 24 个模块（包 22 个）；连桥接共 799 项定理／1286 项声明审计，公理报告全空；外围桥接重跑通过 |

## 6. 决定（2026-10-09 定下）

Ren 把以下决定交给 AI 执行（“你自己全改了吧”）：

1. **路线。** 加脊柱、只增不改、实例化而不复制。
2. **术语与 G0 的作用域。** 由 Ren 定下：
   - “Becoming”指整个展开；“generative is a part of its manifold”（[原话](../../../../sources/15-codex-theory-conversations/2026-10-09-becoming-whole-generative-manifold.md)）。
   - G0 的对象从一开始就是生生；生成与退化作为关系不重叠（[Ren 追问](../../../../sources/15-codex-theory-conversations/2026-10-09-renewing-consuming-without-axioms.md#ren-follow-up)，`renewing_not_consuming`）。
   - “消耗更坏”由 C 承担。
3. **提升规则 L 的默认。** 以“每个结果都优于每个结果”作保守默认并公开；更强的规则作为可选承诺。
4. **工作规则。** 在 P4b 加入 AGENTS.md。
5. **旧章节。** 只在新正典章中标为历史证据，原文不动。

## 7. 主要风险

- **过度宣称。**
  - 刻画定理中“G0 ⇒ 前提”一侧几乎是平凡的，价值在于极小性和对手的统一形状。
  - 规范桥都是假言推理，不能说成已经证明了伦理。
- **悄悄削弱前提。** 每条转换定理写明方向和前提。
- **范围。** S0 加 N 不及于不接受边界中立的立场，也不处理使新生命存在的价值。
- **工具链分裂。** 核心只用前导，在 4.29.1 检查；Mathlib 叶子在 4.30.0-rc2。核心不依赖任何一方的库，因此两个工具链都能编译它。
- **闭包变动。** 开工前按哈希冻结所用模块闭包；当前只有本会话在写，风险较低。

## 8. 架构与命名 / Architecture and names

按 Ren 的[要求](../../../../sources/15-codex-theory-conversations/2026-10-09-pure-core.md#rens-follow-up-elegance-and-names)，整个代码库在结构与概念上对读者优雅，名称不最能表达所述之事时就改。

**三环，依存只指向核心。**

| 环 | 内容 | 工具链与检查 |
|---|---|---|
| 核心 | 基础三模块与包 `Becoming` 的四层 | 只用 Lean 前导；`check_becoming.py` 核对闭包、空公理报告、仅前导编译 |
| 桥接 | `Becoming.Bridge`：既有 Std 模块的接口即核心概念 | 4.29.1，同一检查器；公理报告为空 |
| 外围 | 既有模块、Mathlib 叶子及其桥接 `CorrectionInquiry`、Python 实验 | 任意合适的工具；`CorrectionInquiry` 用 4.30.0-rc2 与 Mathlib 检查，核心在那里同样编译 |

每个工具链一个检查器，每个检查器一张回执；外围检查器要求它闭包中的核心模块与核心回执一致。读者入口是[包说明](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/README.md)。

**命名约定。** 模块按所述之事命名，包路径即模块名；声明名稳定，因此记录别名不随模块改名失效；旧名留在历史条目与保留的运行中，不改写证据。

**全库改名（2026-10-09 完成）。** Ren 的[后续指示](../../../../sources/15-codex-theory-conversations/2026-10-09-pure-core.md#rens-follow-up-finish-the-renames-then-continue-the-theory)是不删数据、完成其余并提交 main。两个目录据此改名：

| 旧名 | 新名 | 理由 |
|---|---|---|
| `theories/shengsheng-buxi-generative-existence/` | `theories/becoming/` | 理论现名 The Theory of Becoming；旧名来自早先“生成性存在”的表述 |
| `…/unified-2026-10-05/` | `theories/becoming/chapters/` | 正典章节不再是带日期的工作目录 |

目录用 `git mv` 移动，文件内容不因移动而变。现行文件中的路径按有序替换规则改写，每个改写文件都核对为原字节的纯替换。指令记录只改 Markdown 链接目标，引用 Ren 原话的行不动。证据保留原字节，其中的旧路径按对照表读：导入原件、冻结副本、保留运行、回执、Lean 源码和历史阅读版都属此类。已审哈希只在改动核对为纯替换后沿用，各登记的过期状态与改名前相同。逐文件对照与检查器见[架构记录](../../../architecture/README.md#directory-renames-9-october-2026--目录改名)。

L0 命名空间 `Generative` 保留。`GenerativeCore` 的字节被 593 张回执哈希，改名会使这些继承回执全部失效，而收益最小；根模块 `Becoming` 的说明已写明它的含义。

Three rings, with dependence pointing only toward the core; one checker and one receipt per toolchain. Modules are named for what they state; declaration names are stable, so aliases survive module renames. At Ren's request the theory directory became `theories/becoming/` and the dated chapter folder became `chapters/`. Live references were rewritten and verified as pure path substitution, evidence keeps its bytes, and a rename receipt maps every rewritten file. The L0 namespace `Generative` stays, because renaming it would invalidate every inherited receipt.

## 9. 走向完整的生成之论 / Toward a complete Theory of Becoming

2026-10-09。Ren 的[指示](../../../../sources/15-codex-theory-conversations/2026-10-09-complete-theory-of-becoming.md)：“aim a complete theory of becoming, and finish related work”。依 Ren 的[优先提议](../../../../sources/15-codex-theory-conversations/2026-10-08-theory-of-becoming-priority.md)：

- 计入整个空间，包括生成与退化，生成之论或许不需要公理；
- 加上公理，就划出整个空间中的一部分。

范围是同一展开中关系的形成、维持、转化、退化与消失，以及它们怎样改变后续活动的条件；生命、演化与评价在其中分化。

**“完整”读作四项可检查的内容（AI 的读法）。**

1. **每种形态都在同一条脊柱上。** 形成、维持、转化、退化、消失，以及生命、演化、评价，各有陈述在核心上的定理。
2. **整体的规律不加前提。** 对每个展开都成立的规律，不加任何关于展开的前提而证明；其余每条规律都写明它的前提。表示本身的方法承诺另行公开：离散的步、自然数的量、计数时的可判定性。
3. **前提划出部分，不是整体的公理。** 动力学的每个前提，都证明有展开满足它、也有展开不满足它：它划出整个空间中真实而非空的一部分。生成的、退化的与混合的部分都非空。
4. **开放的内容分类。** 每个开放项归入四类之一：Ren 的选择、哲学根据、经验对应、待证。

完整的形式表示不等于整体对现实的演绎必然性。[根基记录](../../../../theories/becoming/results/records/theory-of-becoming-foundation.md)在“关系构成”一步得到论证之前保持开放。强的零公理假说不缩成“Lean 公理报告为空”。

| 阶段 | 内容 | 验收 |
|---|---|---|
| P18b 第八次独立审查 ✓ | 另一 agent（Claude Opus 5.5）审查 P16c、P17 与 P18（[审查](BECOMING-P16C-P17-P18-REVIEW.md)）L1–L10：数学全部接受；世系接受不参与的给予项，`LivesOn.active` 省略体现的前提，储备只在一个方向上是所持的条件，转化的读法改变 living，要求用到的是上升，以及用语与记账的残余 | 已完成：[研究 §27](BECOMING-RENEWAL-READING.md#27-第八次独立审查与更正p18b)。`Flow.Descends` 要求给予的形成参与该步（`Stranger`、`Brood.not_descends`）；`LivesOn.stands` 与 `Drowsy`；`Seed.no_held`、`Viable.no_held`、`Flow.carries_of_own`；`Web.redirect`、`redirect_dependent` 与 `Famine.living_differs`；补充与耗散的定理对上升陈述（`rise_given`、`rising_needs_replenishment`、`rise_lowers_on`、`rising_ceases_on`、`rising_opens`、`rising_draws_in`、`rising_ceases`，`Growing`），原有定理改由它们推出；检查器审计 Lean 生成的常量；用语、标题、关联说明与审查时间的约定。回执 20261009T104417.218214Z（877 项定理／1387 项声明审计） |
| P19 变化的规律 ✓ | L3 新模块 `Becoming.Change`：不加前提的规律。不变即持续；量的增减相抵（任何一段上，终点加下降等于起点加上升）；支持只经由关系的变化而改变（条件下降、依存改变或所需增长）；活动、水平、依存与支持的变化都是同一种“跨一步的变化”的实例 | 已完成：[研究 §26](BECOMING-RENEWAL-READING.md#26-变化的规律不加前提开始成立与不再成立同步p19)。`Becoming.Change`（导入 `Flow`，`Population` 改导入它）：开始成立与不再成立（`ComesToBe`、`CeasesToBe`），生起与止息、形成与消解、开始与不再作为条件而在是它的读法（`Web.change_readings`）；`persists`、`Web.supported_of`；一段步上的升降相抵（`over_stretch`、`family_over_stretch`）；下限与上限（`fallen_within`、`risen_within`、`rising_recurs`、`falling_recurs`、`Web.falls_need_rises`），`Renewal` 的 `falls_finitely` 是一个量的下限（`falls_finitely_from_floor`）；超出原计划：有限家族中开始成立与不再成立同步（`held_over_stretch`、`keep_pace`、`coming_recurs_iff`），读于活动（`Web.activity_over_stretch`、`Web.arising_recurs_iff`、`Web.unceasing_iff`）与水平（`Web.standing_recurs_iff`，不需要任何前提）；无限家族的见证 `Dawn`、`Dusk`。`mark` 从 `Reserve` 移来，`total_map`、`total_congr` 从 `Roles` 移到 `Flow` 的 total 一节。记录 [coming-and-ceasing-keep-pace](../../../../theories/becoming/results/records/coming-and-ceasing-keep-pace.md)。核心闭包 25 个模块（包 23 个）；连桥接共 841 项定理／1342 项声明审计，公理报告全空；外围桥接重跑通过 |
| P20 上升与下降在同一交换中 ✓ | `Flow` 与 `Dissipation` 新增：在平衡且只有活跃者取用的流中，每次下降都是某个活跃形成的取用；在耗散之下，被耗散家族中一个成员上升（包括开始作为条件而在），同一家族中另有成员下降；没有耗散时不然（`Brood`） | 已完成：[研究 §28](BECOMING-RENEWAL-READING.md#28-上升与下降在同一交换中p20)。原题“生与灭”说得过强：证明的是上升与下降，下降不是止息。`Flow`：`Balances.fall_taken`、`Balances.takenBy`（`rise_given`、`renewedBy` 的对偶）；`Dissipation`：`Balances.falls_cover`（被耗散的一步上，下降至少等于上升加取用者数）、`Balances.falls_of_taking`、`Balances.depletes`（`Generation` 的消耗前提由平衡与耗散推出）、`rise_with_fall`、`standing_with_fall`、`rise_alone_opens`（有上升而无下降的不重复家族在该步不封闭）、`rise_exchange`；`Roles`：`Embodied.arising_with_fall`、`Brood.birth_only`、`Brood.rise_without_fall`。记录 [rising-and-falling-in-one-exchange](../../../../theories/becoming/results/records/rising-and-falling-in-one-exchange.md)。回执 20261009T110204.479251Z（889 项定理／1399 项声明审计），外围 20261009T110332.423150Z |
| P21 演化在脊柱上 ✓ | L4 或 L3 新模块 `Becoming.Evolution`：经世系的传递（后代承接给予它的形成的依存）、变异（所需不同）与选择（共同条件之下支持的差别）；差别经由传递进入后续活动，并改变后续选择的条件。既有的演化机制（`StructuralCopying` 等）保持原范围，能证明对应时在外围接通 | 已完成：[研究 §29](BECOMING-RENEWAL-READING.md#29-演化在脊柱上p21)。演化的最小形式内容在核心上，不替代演化之论的独立目标。L3 新模块 `Becoming.Evolution`（导入 `Change`；`Descent` 改导入它）：世系（`Flow.DescendsAt`、`Flow.Descends`，从 `Descent` 移来，估值的读法留在 L4）；不加前提的传递律 `price`（Price 方程的加法计数形式，是会计恒等式）；选择即支持对给予的约束（`DescendsAt.supported`、`unsupported_childless`、`never_supported_childless`、`selected_le`、`selection_within`），适应度没有定义；传递是前提（`TransmitsWithin`），传递的曾被选择（`transmitted_supported`），活动设定后来的选择（`transmitted_within`）；见证 `Drawdown`，没有 `Dependent` 时的反例 `Unchecked`。繁殖率、突变、漂变与种群动力学不在其中；与 `StructuralCopying` 等的对应本轮没有尝试，保持原范围，列入下一步。记录 [evolution-on-descent](../../../../theories/becoming/results/records/evolution-on-descent.md)。回执 20261009T112625.591552Z（910 项定理／1435 项声明审计），外围 20261009T112736.537510Z |
| P22 整体与其部分 ✓ | 新模块 `Becoming.Space`：P19 的规律对整个空间成立；`Dependent`、`Balances`、`Dissipative`、`Embodied`、`Acting`、`Carries` 等每个前提都有满足与不满足它的展开；生成的（生成不息）、退化的（消耗、终结）、混合的与“每个事件都 living”的部分都非空，且彼此交叠 | 已完成：[研究 §30](BECOMING-RENEWAL-READING.md#30-整体与其部分p22)。Ren 提议的形式内容：规律对整体成立，前提划出部分。L3 新模块 `Becoming.Space`（导入 `Evolution` 与 `Reserve`）：世界（`World`，以一类读法的关系项、流与依存网；两类读法经 `ofRoles` 嵌入）与其部分（`Generative`、`Degenerative`、`Living` 与七个前提）；有限且活动可判定的世界中生成复现恰当退化复现（`generative_iff`），无限时分离（`separate`）；七个前提各有满足与不满足它的世界（`contingent`；新世界 `idle`、`restless`、`unbalanced`、`spending`）；有限世界中生成与否都既可都活也可有不活（`living_crosses`）；耗散使有限、平衡且生起者体现的世界归于静止（`rests`），每个前提都不可少（`rests_needs`）。原计划写的 `Carries` 读作“有储备承载”（`Carried`）；`Census` 等其余前提与前提组合的地图列入下一步。记录 [space-and-its-parts](../../../../theories/becoming/results/records/space-and-its-parts.md)。回执 20261009T114557.489291Z（939 项定理／1501 项声明审计） |
| P23 完整的陈述 ✓ | 正典章节加“完整的生成之论”一节：整体的规律、前提划出的部分、生与灭的统一、后续活动的条件、演化与评价的位置；根基章节的完成审计；根基记录的下一步；开放纲领按四类重排 | 已完成：[研究 §31](BECOMING-RENEWAL-READING.md#31-完整的陈述与完成审计p23)。正典章节新增“理论的完整陈述”（五部分，每条标明表示／规律／定理／公理／读法／开放）；第 8 节为现状表与四类开放项（Ren 的选择、哲学根据、经验对应、进一步的证明），每个原有的下一步都已归类；根基章节完成审计各行加入脊柱的证据，剩余推论不变；根基记录的下一步改写并保留中心推论；表示的范围列为哲学根据。无新增 Lean 声明或成果身份；形式陈述的完整不写成必然性已证 |
| P23b 第九次独立审查 | 另一 agent 审查 P19–P23 | 逐项处理 |

各阶段沿用既有流程：先在暂存区编译并核对公理，再登记包、写记录与研究章节，跑全部检查，最后提交。读法、名称、“生”的范围与接续仍由 Ren 定，见上文第 6 节与研究各节的“边界”。

**English.** Following Ren's instruction to aim at a complete Theory of Becoming and finish the related work, completeness is read as four checkable parts:

1. Every mode of the scope is stated on the one spine.
2. The laws that hold of every unfolding are proved with no premise, and every other law names its premise. The representation's own commitments (discrete steps, natural-number amounts, decidability where counting needs it) are disclosed separately.
3. Each dynamical premise is shown to pick out a proper, non-empty part of the whole space. Generative, degenerative and mixed parts are all non-empty.
4. Everything open is classified as Ren's choice, philosophical warrant, empirical correspondence or a further proof.

The phases are:
- P18b: the eighth review.
- P19: laws of change with no premise.
- P20: rising and falling in one exchange (first titled "coming to be and ceasing to be", which was too strong).
- P21: evolution on the spine (descent, a law of transmission with no premise, selection through support, transmission as a premise, and activity setting later selection).
- P22: the whole and its parts (the space of worlds, laws of the whole, premises carving parts, living crossing generation, and dissipation bringing a finite world to rest).
- P23: the complete statement (the theory stated in full, with a status for each item; the open programme in four classes; the completion audit with the spine's evidence).
- P23b: the ninth review.

Formal completeness of a representation does not establish the deductive necessity of the whole for reality, and the readings and names remain Ren's.
