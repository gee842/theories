# 核心与伦理层的论证同构审查 / Structural audit: core and ethics arguments

2026-10-09，Asia/Bangkok。AI（Claude）应 Ren 的问题“伦理和核心，他们之间的论证结构上，是不是同构的？我们是不是重复造轮子了？我觉得所有应该都可以整合为一个理论才对”所作的结构审查。本文是仓库普查与论证形式比较，不新增定理，也未证明形式同构；下文的对应是论证模式层面的对应，须由桥接定理检验。

## 1. 普查（工作源码，排除保留副本与回执目录）

| Lean 目录 | 模块 | 传递导入 `GenerativeCore` | 定理 |
|---|---|---|---|
| `lean/deeper`（含 Becoming 系列） | 91 | 78 | 1389 |
| `lean/inquiry-root/sufficiency` | 45 | 44 | 1441 |
| `lean/universal-ethics/generative-capacity` | 82 | **6** | 1285 |
| `lean/universal-ethics`（顶层） | 38 | 22 | 650 |
| `lean/universal-ethics/evolution-connectionism` | 6 | 0 | 199 |

伦理模块族共 126 个，只有 28 个接到核心；`generative-capacity` 子目录 82 个模块中仅 6 个。成果登记中有 49 条 `formal-reuse` 依赖边，另有 123 条“关联而非已证转换”。

## 2. 论证形式的对应

| 论证形式 | 核心（建立在 `Process` 上） | 伦理层（多为自建模型） |
|---|---|---|
| 同一回应对全部所容许情形都成立 | `InquirySufficiency.CommonResponse P safe goal response B r` | `PracticalJudgment.Robust`；`PositiveGroundUncertainty` 的 ∀h∃q |
| 证据收窄可能情形 | `After P sense B a o`；`ClassifiedThrough` | `StandardsBridge.learn/revise`；`robust_under_refinement` |
| 归纳闭包／可达 | `Trace P s as t` | `WholeGroundCoverage.Reached` |
| 表示变换下的忠实保留 | `projection_exact_iff`、`trace_faithful_iff` | `faithful_history_transport_preserves_joint_bundles`；`required_under_faithful_redescription` |
| 有限储备界与更新 | `Depletion.trace_reserve_bound` | `RenewingFormation`（2026-10-09 并行新建，只导入 `GenerativeComparison`） |
| 接续空间 | `Process` 的轨迹 | 抽象 `Whole`／`Inventory`，或各模块自建的 `Arrangement`、`FormationModel` 等 |

核心的充分探究是多步版本；伦理层在一步或固定所见范围上重证了它的特例。

## 3. 伦理层真正新增的内容

1. **规范桥。** G0（生成且实现 → 正面相关）、D（在所见范围内确保 → 理由）都是谓词上的蕴涵。[外部审查](UNIVERSAL-METAETHICS-OF-AGENCY-REVIEW.md) §3.5 的探针显示，它们是与符号无关的假言推理。因此，伦理层的定理在形式上等于“一条关于生成谓词的动力学定理”接上 G0／D。
2. **接续上的序与分配结构。** J1 的保护包含加增益、J2 的词典序、非支配前沿、交叉基本损失的不可比、责任分配（`Assigned`、唯一回应者）。这些是新的结构，但其定义域仍是接续空间，不需要另一套过程模型。

## 4. 判断

两层的论证在模式层面高度同构；伦理层大量重建了核心已有的过程、可达、稳健回应、证据收窄与忠实变换。原因是许多模块为了自足和审计干净而只导入 `Std`。代价是结果不能组合：大部分跨层连接只能登记为“关联”。

这也与[非二元方法](../../../../theories/becoming/chapters/NONDUAL-METHOD.md)不一致。该方法要求区分“说明评价怎样形成”与“论证何者值得肯定”，但“两者关乎同一展开，不设立分离的伦理与因果实在”。在两套各自的世界模型里分别证明动力学与伦理，正是形式层上的分立。

## 5. 整合结构（建议）

```text
The Theory of Becoming
├─ 核心：Process／接续、轨迹、投影（GenerativeCore，已无公理依赖）
├─ 生成谓词：形成、更新／消耗、退化（deeper/Becoming、Depletion）
├─ 模态形式：共同回应、探究与证据收窄、忠实变换（inquiry-root）
└─ Universal Metaethical Core：一层薄的公开前提
   ├─ G0、D：把动力学定理提升为正面根据与理由（一条通用提升定理）
   └─ J1–J4：接续空间上的比较、分配与选择
```

第一步是一个桥接模块：以核心 `Process` 的接续实例化 `Inventory` 与所见范围；证明 `Robust` 是 `CommonResponse` 的一步特例、`revise` 对应 `After`、`Reached` 对应 `Trace`；给出通用提升定理：任一核心定理若在所见范围内确保生成内容，则在 G0、D 下给出面向每个有通达位置的理由。此后新的伦理结果陈述在核心之上；既有模块与记录按原范围保留，只在代价低时补转换定理。

**会改变本判断的结果：** 若桥接中发现伦理层某个模式无法在 `Process` 上表述（例如所需的接续同一性超出轨迹与投影所能表示的范围），则该处是核心缺少的关系，应扩展核心，而不是保留另一套模型。
