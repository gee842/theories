# The Theory of Becoming：整合为一个理论的方案 / Unification plan

2026-10-09，Asia/Bangkok。AI（Claude）应 Ren 的要求“请发一个或者几个subagent……整体看一下整个repo，然后再决定，怎样是最elegant的方法，然后给我一个plan”撰写。依据四份只读普查（Lean 形式层、理论文档、基础设施、统一抽象设计）及主会话的独立复核；承接[核心与伦理同构审查](CORE-ETHICS-ISOMORPHISM-AUDIT.md)。本文是计划，不新增定理或成果记录；[原型](development/becoming-spine-prototype/README.md)只作开发草稿保存。

## 0. 结论

**不重写，加一条“脊柱”。** 核心 `Generative.Process` 保持不动，在它上面加一组薄层：先给状态加上主张赋值，再加模态形式与 Becoming 谓词，最后让 Universal Metaethical Core 成为同一语言中的一组公开前提。伦理不再有自己的世界模型。旧模块与记录按原范围保留，只为约 12 个通用模式模块补转换定理。叙述层只新增一章正典入口，不改任何已被记录绑定的章节。整条脊柱约 6–9 个工作日；逐一重写 126 个伦理模块需要 20 个以上工作日，且大多只是重新编码有限例子，不值得做。

## 1. 普查得到的事实

**形式层**
- 工作源码 561 个模块、10,648 条定理，无 `sorry`、无自定义公理；58% 传递导入核心。
- `Process` 只在核心中声明一次；`State` 被重新声明 75 次，`Event` 83 次。
- 重复的组合子：约 22 个自建 `Trace` 归纳类型；约 12 个 `Reach` 副本，`BecomingReversibility.Reach` 与 `GeneratedPaths.Reach` 逐字相同；8 种“忠实变换”；8 条储备或更新界；303 处手写的轨迹归纳。
- 伦理层：携带 G0 的 24 个模块（399 条定理）都不接核心。
- 叶子：40 个模块依赖 Mathlib（工具链 4.30.0-rc2），另有序理论与模型论、Rat 市场动力学。概率在全仓都是有限权重，暂不需要随机过程层。

**记录层**
- 84 条记录，49 条 `formal-reuse` 依赖边，128 条“关联而非已证转换”。
- 伦理族（F07）没有一条 formal-reuse 边进入核心族（F01）。
- `relational-renewal-classification`（F01）与 `renewing-consuming-formation`（F07）是同一种分类的两层表述，互不相通。

**叙述层**
- `unified-2026-10-05/` 共 138 章、5 MB。最大的 `GENERATIVE-GROUNDING`、`UNIFIED-ETHICAL-GROUNDING` 都是按日期堆叠的状态段落。
- G0／J 前提表在 7 章中重复，且彼此不一致：D 不在 `PRACTICAL-JUDGMENT`、`ALIGNMENT-DIRECTION` 的前提表里。
- “Universal Metaethical Core” 不出现在任何章节中，只出现在 README、目标和记录里。
- 阅读目录漏掉 31 章，包括全部 Becoming 与 G0 章节。
- “whole” 至少有四种用法：展开本身、理论、接续、Lean 类型。

**基础设施**
- 没有 lakefile；约 430 个按模块的检查器，各自用临时 `LEAN_PATH` 编译。
- 改动一个被绑定的源文件会使所有绑定它的记录漂移：101 个章节被绑定；`GenerativeComparison.lean` 被 7 条记录绑定，`GenerativeCore.lean` 被 5 条。
- 新增的桥接文件不引起任何漂移。

## 2. 最优雅的结构

```text
L0  Core        Process / Trace / Feasible / projection / history unfolding   （不改；327 个依赖者）
L0′ Run         无限运行 Run P（现在有 5 处各自用 Nat → State 编码）
L1  Frame       Frame = Process + realized : S → C → Prop + generative : C → Prop + 可观测量
L2  Modal       CommonResponse（= Robust）、After、Sound/Sufficient、Reach、通用 trace_invariant、
                Scope = 一个 sound 探究策略实际执行所到达的端点
L3  Becoming    Novel（沿轨迹的新实现）、更新／消耗（Run 上可观测量的性质）、端点损失与返回、耗竭
L4  Universal Metaethical Core（同一语言中的公开前提，宇宙多态）
                G0：生成内容被实现 → 正面相关
                D ：在 Scope 上确保 + 位置有通达 → 支持理由；位置 = 被实现的通达主张 Access p r
                L ：把结果间比较提升到回应间比较的规则（新显式前提）
                J1–J4：由 realized 定义的序、基本条件优先、责任分配、正当选择
Leaves          ℝ/Mathlib、序理论、Rat 市场：作为叶子包，只在实际用到时补适配
```

**为什么这样最简洁：**
- 只有一个世界模型；伦理是同一语言里的前提，不是另一套模型。这也正是非二元方法的要求。
- 所见范围由动力学给出：一个 sound 探究策略实际执行所到达的端点，不再是可以随结论挑选的自由参数。
- 位置是被实现的主张，没有行动者原语；理由随位置的形成而形成、随其消散而失效。这是 Becoming 真正把内容送进伦理层的地方。
- 忠实变换就是核心的 `trace_map`/`trace_lift`；`Robust` 在定义上就是 `CommonResponse`。

原型（20 条定理，全部无公理依赖，主会话独立复编译）已经验证：`Frame` 实例化 `Inventory`；`Robust ↔ CommonResponse`；`Reached ↔ Trace`；历史迁移等于 `trace_map`/`trace_lift`；`normative_lift`；`RelationalRenewal` 的展开是一个确定性核心过程的唯一运行。

## 3. 整合本身暴露出的三项实质发现

1. **隐藏前提 L。** `Situation.realize` 是函数，默认每个选项只有一个结果；`Process.step` 是关系，允许多个结果。只要对回应作 J 序比较，就需要一条提升规则，例如“每个结果都优于每个结果”或“每个结果都优于某个结果”；而且传递性还需要中间回应可行。选择哪条规则是规范内容，应与 J4 并列公开。
2. **所见范围可以由动力学定义。** 这收窄了正面根据结果中一个原本由应用自行给出的参数。
3. **更新／消耗是同一个分类。** F01 与 F07 两条记录、`Depletion`、`ContinuationRenewal` 及 8 条储备或更新界，可以统一为 `Run` 上可观测量的性质。这是审查 §3.3 在核心层的答案，也是整合中唯一预期会产生新的实质定理的地方。

## 4. 迁移不变量

- **只增不改。** 不编辑、不移动既有源码、回执和被绑定章节，也不重跑旧检查器（重跑会覆盖其回执）。
- **新目录与约束。** 放在 `experiments/.../generative-basis/lean/becoming/`，全仓唯一的文件名，独立命名空间 `Becoming`；只依赖 Std，工具链 4.29.1，检查器强制所有新声明公理报告为空。
- **一个合并检查器。** 自动解析导入闭包；对继承模块断言当前哈希等于其历史回执中的 `source_sha256`；分别报告新旧审计数；回执文件名唯一。
- **记录方向为 core → spine → ethics。** 伦理模块只作为定义被引用，不作为结果依赖，以免依赖成环。只有当一条具名桥接声明证明了转换时，才把相应的 `related` 链接升级为 `formal-reuse`。
- **`normative_lift` 只按组合登记，不作为成果展示。** 它只有三行；全部价值在于 `secured` 从哪里来。
- **转换定理写明方向。** 能证等价就证 iff；只能单向时如实写出，不悄悄削弱前提。
- **冻结闭包。** 开工前按哈希冻结所用模块闭包，因为未跟踪的新模块在不断到来。

## 5. 阶段

| 阶段 | 内容 | 验收 | 工作量 |
|---|---|---|---|
| P0（今天） | 提交本线已有工作；保存本计划与原型 | 本线文件入库，HEAD 中链接完整 | — |
| P1 脊柱核心 | `BecomingFrame`（Frame、Run、Reach、`trace_invariant`、Novel），`BecomingModal`（通用 CommonResponse、After、Scope、反单调性）；合并检查器；记录 `becoming-spine` | 空公理；继承哈希与回执相符 | 1–2 日 |
| P2 伦理层 | `MetaethicalCore`：宇宙多态的 G0、按状态索引的 D（通达即主张）、显式 L、J1–J4；`sound_inquiry_gives_positioned_reason`；一页前提卡（G0、D、E、L、J1–J4） | 同上；前提卡与记录逐项一致 | 1–2 日 |
| P3 适配 | 约 12 个通用模式模块的转换定理：`GenerativeComparison`、`PracticalJudgment`、`PracticalReach`、`StandardsBridge`、`PositiveGroundUncertainty`、`PositionedPositiveReason`、`JointContinuationClassification`、`WholeGroundCoverage`、`WholePracticalRestriction`、`GenerativeLossComparison`、`RenewingFormation`、`RelationalRenewal`；按具名声明升级 `related` 链接 | 每条升级都有具名声明 | 2–3 日 |
| P3b 更新／消耗统一 | `Depletion`、`RenewingFormation`、`RelationalRenewal`、`ContinuationRenewal` 统一为 Run 可观测量的一个分类定理 | 新的实质结果，独立反审 | 1 日 |
| P4 叙述 | 新正典入口 `THE-THEORY-OF-BECOMING`（8 部分：Becoming、组织与演化、认识与探究、集体动力学、评价的形成、Universal Metaethical Core、AI 对齐、开放纲领），附术语表和前提卡；旧章作为证据链接；README 首段指向它；补齐阅读目录 | 不改任何被绑定章节；渲染与检查通过 | 1–2 日 |
| P5（可选） | 只作索引的 Lake 工作区、层级模块名、Mathlib 叶子包（4.30） | 不参与回执 | 1 日 |

## 6. 需要 Ren 决定

1. **路线。** 采用“加脊柱、只增不改”（推荐），还是全面重写。
2. **术语与 G0 的作用域。** 两种选择：
   - “Becoming”指整个展开，“生成／generative”只指其中更新进一步形成条件的模式，与消耗、退化并列。这样 G0 获得区分内容，回应审查 §3.3，但改变了 G0 的作用域。
   - 保留 generative 作总称，区分只由动力学承担；这是并行会话 `RenewingFormation` 当前的做法，G0 逐事件同时承认两者。

   这是理论内容的决定，不是工程决定。
3. **提升规则 L 的默认。** 推荐以“每个结果都优于每个结果”作保守默认并公开；更强的规则作为可选承诺。
4. **工作规则。** 是否在 AGENTS.md 加一条：“新的形式结果陈述在脊柱上；只有脊柱确实表达不了时才另建模型，此时应扩展脊柱。”
5. **旧章节的标注。** 是否在新正典章中把 `GENERATIVE-GROUNDING`、`UNIFIED-ETHICAL-GROUNDING` 等标为“历史证据”。原文不动，只在新章中说明。

## 7. 主要风险

- **过度宣称。** 提升定理是一行假言推理，桥接容易被说成已经证明了伦理。
- **悄悄削弱前提。** 转换定理可能在不知不觉中削弱前提。
- **并发冲突。** 多个会话同时改记录 JSON；任何一条记录的结构错误都会阻断全部渲染。
- **工具链分裂。** Std 部分在 4.29.1，Mathlib 叶子在 4.30.0-rc2。
- **闭包变动。** 未跟踪的新模块持续到来，所用闭包会变；必须按哈希冻结。
