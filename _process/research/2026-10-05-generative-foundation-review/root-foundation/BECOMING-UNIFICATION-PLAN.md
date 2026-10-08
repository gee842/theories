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
- `unified-2026-10-05/` 共 138 章、5 MB。
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

Lean 中 L1–L4 是包 `Becoming` 的四个模块 `Becoming.Frame`、`Becoming.Inquiry`、`Becoming.Renewal`、`Becoming.Metaethics`；`import Becoming` 导入全部。既有模块经 `Becoming.Bridge` 连到核心，它在包内但不属核心（[包说明](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/README.md)）。

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
| P2 伦理核心 ✓ | `MetaethicalCore`：S0、N_rel、N_std、A、C、L、J 的具名定义；G0 刻画定理；D 的导出；极小性反模型与“对手即有界规则”；脊柱上的普遍位置理由；提升规则 L。记录 `metaethical-core-characterization`；一页前提卡 | 已完成（d79d0d9d）：[metaethical-core-characterization](../../../../theories/shengsheng-buxi-generative-existence/results/records/metaethical-core-characterization.md) |
| P2b 评价者路线更正 ✓ | 执行[审查](EVALUATOR-GROUNDING-REVIEW.md) §6 的 15 项更正：论证文档、Lean 说明、记录 `self-good-reachable-g0`（收窄标题与主张）、G0-WARRANT 相关段；P+ 版第二步由 P2 承担 | 已完成（001c5cdd）：记录与审查逐项对应；该模块检查器重跑通过 |
| P3 实例化 ✓ | 先用脚本对 45 个含多态定理的模块分类，结果存入本研究。再按接口逐一处理：给出脊柱实例；对重建核心组合子者证明等价（`Robust`、`Reached`、`revise`、`Guarantees` 等）；函数式结果用 L 推广。相应记录增加证明绑定，按具名声明升级 `related` 链接 | 已完成：[分类表](BECOMING-INSTANCE-CLASSIFICATION.md)覆盖 45 个模块并逐行机械检查；11 个接口都有具名实例或等价定理（`BecomingInstances`），记录 [becoming-spine-instances](../../../../theories/shengsheng-buxi-generative-existence/results/records/becoming-spine-instances.md)。证明绑定放在新记录上，既有记录按原范围保留不改；新记录以 `related` 连到它们，唯一的 `formal-reuse` 是对 C 与 L 的直接使用 |
| P3b 更新／消耗统一 ✓ | 由 Run 可观测量构造 `RelationalRenewal` 的展开，`RenewalComparison` 的关系读法成为脊柱上 `generative` 的规范读法；`Depletion`、`ContinuationRenewal` 的储备界作为同一分类的实例 | 已完成：[整合与作者反审](BECOMING-RENEWAL-READING.md)，记录 [becoming-renewal-reading](../../../../theories/shengsheng-buxi-generative-existence/results/records/becoming-renewal-reading.md)。`BecomingRenewal` 为 L3；读法在 `MetaethicalCore` 中由 L4 使用 L3 给出。三条界的统一是组织性的；`ContinuationRenewal` 的良基形式更一般，不由该原则导出 |
| P4 叙述 ✓ | 新正典入口 `THE-THEORY-OF-BECOMING`：Becoming、组织与演化、认识与探究、集体动力学、评价的形成、Universal Metaethical Core、AI 对齐、开放纲领。附术语表与前提卡；旧章作为证据链接，并在新章中标为历史证据；README 首段指向它；补齐阅读目录 | 已完成：正典章节（2bcf314b）。阅读目录补齐 32 个缺项；17 个过期条目先读原文差异再更新字段与版本标记；生成视图（CLAIMS、理论首页）以生成清单为准，记为 `generated-view`，其各行随成果记录检查；Lean 文本目录重新同步。两项目录检查、渲染、`research-check` 与 36 项测试通过 |
| P4b 工作规则 ✓ | AGENTS.md 增一条：新的形式结果陈述在脊柱上；脊柱表达不了时扩展脊柱，而不是另建模型 | 已完成：规则在 AGENTS.md「Evidence and preservation」首条，链接正典章节 §9 与脊柱目录 |
| P5a 核心纯净 ✓ | 按 [Ren 的要求](../../../../sources/15-codex-theory-conversations/2026-10-09-pure-core.md)：核心（L0 及其两个基础模块，加 L1–L4）不导入核心以外的模块，公理报告全空，只用 Lean 内置前导即可编译。G0、C、D 与确保的正面根据在核心陈述；桥接层以 `Iff.rfl` 证明既有模块的定义即核心定义；J1/J2 的 `BetterAt` 与 `living_iff_relational` 移到桥接层 | 已完成：检查器每次核对闭包、空公理报告与仅用前导编译；80 项定理／146 项声明审计 |
| P5b 包结构 ✓ | 核心改为 Lean 包 `Becoming`，按所述之事命名：`BecomingFrame` → `Becoming.Frame`，`BecomingModal` → `Becoming.Inquiry`（它讲探究的所见范围，不是模态逻辑），`BecomingRenewal` → `Becoming.Renewal`，`MetaethicalCore` → `Becoming.Metaethics`，`BecomingInstances` → `Becoming.Bridge`；根模块 `Becoming` 导入四层。声明名不变，记录别名照旧有效；上面各行保留当时的模块名 | 已完成：检查器按包路径命名模块并核对闭包；记录、章节与链接改到新路径；包说明给出读者入口与新旧名对照 |
| P5c Mathlib 叶子 ✓ | 不建 Lake 工作区：Mathlib 已安装（既有检查器经 `SYSTEMS_MATHLIB_PROJECT` 使用 `~/repos/生生不息`），沿用 Python 检查器。外围桥接模块导入核心与 Mathlib 叶子，证明其接口是核心的实例，用 4.30.0-rc2 编译；核心不导入它 | 已完成：核心增“判断即一步探究”（`judgeProcess` 由桥接层移入 `Becoming.Inquiry`，`commonResponse_judge_iff`），核心 81 项定理／147 项声明审计。外围桥接 `CorrectionInquiry`（7 项定理，公理报告全空）证明 `CorrectionBoundary` 的实施与共同行动、`ObservationChange` 的安全选择都是每个观察格上的共同回应，两模块的细化定理由 `commonResponse_antitone` 导出；核心在 4.30.0-rc2 下同样编译通过。其余三个叶子是具体模型或关系代数，核心没有对应接口，分类表写明理由 |

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
