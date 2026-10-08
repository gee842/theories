# 不能用自己撤掉的支承重算履约目标 / Maintenance after changing its own conditions

2026-10-08。AI 整合，接续 Ren 的“继续”与持续有效的 [Lean 实查要求](../../../../sources/15-codex-theory-conversations/2026-10-08-chance-adequacy-lean-continuation.md)。沿 G0/J 路线。[协议](MAINTENANCE-BASELINE-PROTOCOL.md)、[肯定论证](MAINTENANCE-BASELINE-ARGUMENT.md)、[证明](MAINTENANCE-BASELINE-PROOF.md)与[独立反审](MAINTENANCE-BASELINE-REVIEW.md)分别保留其范围。最终实查与反审待绑定。

## 1. 先关闭已经完成的机制清单

上一轮提出变化中的观察、支承、权限和任务历史需要续接。这是应用要求，不是说这些方面的通用机制尚未证明。本轮重新核对后，确认以下成果必须直接复用。

| 既有成果 | 已完成的内容，本轮不重做 |
|---|---|
| [变化中的检查](TEMPORAL-INSPECTION-INTEGRATION.md) | 顺序失实报告、控制和失陷变化、候选覆盖、受阻前已执行记录与开销、当前认证到实际纠正 |
| [共同接续](JOINT-CONTINUATION-INTEGRATION.md) | 同一整体状态内的局部投影、联合作用覆盖、递推共同可实施与共同支持耗尽 |
| [纠正交接](CORRECTION-HANDOFF-INTEGRATION.md)及其版本接续 | 保旧入口、测试新入口、前缀可用性、在途请求与旧版本的实际寿命 |
| [变化支承](EXPLANATORY-CHANGING-SUPPORT-INTEGRATION.md) | 获得、占用、撤去及恢复的真实步骤；已完成支持的丢失；仍可完成与实际进展的区别 |
| [取得纠正](ACQUIRED-CORRECTION-INTEGRATION.md)与实际命令 | 执行前当前权限核查、撤权拒绝、已发生查询及复查开销的保留 |

这些机制留下的实际墙是：真实安装怎样建立并维持其变化规律、观察、记录和权限的对应。一个新的自给模型不能代替这项证据。本轮没有声称突破这道经验／架构边界，而选择一个更窄、可直接检验的**任务对应错误**。

## 2. 真正被检验的是哪个替换

[ChanceAdequacy](CHANCE-ADEQUACY-CORRESPONDENCE.md)的目标是：在仍有需求、且原支持在有根据配对的条件下仍能工作的情形，兑现指定保护。[ObservableContinuation](OBSERVABLE-CONTINUATION-INTEGRATION.md)已经把实际执行接到这个内容。

若接管先撤掉原支持，再把**被接管改变后的旧通道能力**代入原比较，目标可能被算成空。新的证明仍可以对这个新目标完全正确，却回答了另一个问题。原任务没有因此被履行；原定理也没有被反驳。错的是用实际干预后的能力替换了仍有效承担所依据的比较条件。

本轮相应修正旧对应说明中“原通道不能工作，只能改变……目标”的歧义：它不得被理解为任何接管后的能力下降都能自动缩小原任务。精确旧段落与前后版本保存在[变更记录](MAINTENANCE-BASELINE-INDEX-EDITS.json)；原 Lean 定义、八项定理和历史回执不变。

不能以此宣布所有历史目标都必须冻结。真实交付可以完成任务，需求得到解除可以改变回应，充分理由和有效权限也可以支持修订。相反，当前能力不足与已经完成不是同一件事；自然失效不独自判断其后的修复、紧急重议或免责，更不用说接管自身造成的失接。

This is a correction to a task interpretation under intervention. It does not infer a permanent right from prior operation, create resources from an unmet duty, or forbid beneficial changes to needs and aims. The fixed comparison is justified only for the undertaking and window that remain warranted.

## 3. 数学与操作对照

[MaintenanceBaseline.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/MaintenanceBaseline.lean)已通过 **Lean 4.29.1：4项新定理／13项新声明审计**。它直接导入上一轮的执行模块，既有21项定理／55项审计单列继承，未重计为新成果。

通用条件允许真正完成改变当前需求：每个原目标情形，要么已有**同一任务的真实完成记录**，要么仍被当前目标覆盖。另须说明记录对应于实际交付，并证明当前目标被交付覆盖。由此取得原任务的履行以及已有的共同正总量质量界。它是普通条件推理在本任务中的应用；完成记录的真实性、任务同一性及原承担有效性不能由名字取得。

| 已检查定理 | 内容与意义 |
|---|---|
| `target_transport_with_completion_gives_bound` | 真实完成或仍待覆盖的目标共同承接原内容，导出原履行与同一情形法则下的交付质量界 |
| `retirement_can_erase_recomputed_target_without_fulfilling_origin` | 实际退役关闭旧路线；需求及未交付仍在，重算目标却变空并通过。原目标质量为1，实际交付为0，原履行失败 |
| `actual_extended_delivery_survives_retirement` | 先实际执行有预算的并行交付再退役，两模式的交付记录保留；原任务兑现，交付质量为2 |
| `completed_single_delivery_allows_retirement` | 先完成原左路承担再退役，原维护已兑现；不因保留任务参照而要求旧设施永远运行 |

退役确实门控左路及依赖它的并行操作，交付调用既有实际响应规律并扣预算，完成记录只由真实响应结果形成。右路仍独立可执行，但其在某模式成功不冒充另一模式的欠付已完成。三个附加例检查退役后的实际拒绝、仍可行的右路，以及通用定理由真实完成分支实例化；另列而不计新定理。

本例只处理一次交付。这里的质量统计是**整段任务历史中的交付事件**，不是退役后仍在运行的能力。未构造新设施或长期继任供给，没有证明换线期间连续无断供、物理截止时限、实际记录可信或全部合理解除规则。

[实际回执](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/maintenance-baseline-verification.json)绑定运行 `20261008T121326.478309Z` 的29项产物。新源码 SHA-256 为 `48d26515db6aa2a4e2692e22e1eea1586c95090b139d2a728a21031a8bd3ca77`；新模块11项声明空依赖，1项仅 `propext`，1项含 `propext` 与 `Quot.sound`。没有自设公理、证明缺口或跳过内核。这不等于规范及对应已无前提。最终独立验收见[反审记录](MAINTENANCE-BASELINE-REVIEW.md)。

## 4. 规范根据、最强对手与所获推进

[J3](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/PRACTICAL-JUDGMENT.md#4-谁承担什么--allocating-responsibilities)和[上一轮承担论证](CHANCE-ADEQUACY-ARGUMENT.md)已经说明可归责撤去实际替代、仍须履行或正当解除的关系。[有限风险修订](JOINT-RISK-REVISION-INTEGRATION.md#17-a-local-allowance-cannot-renew-itself-by-changing-the-reference)已经拒绝不断换基准自动续发许可；[目的修订](GOAL-REVISION-CONTINUATION.md)已经区分真实损失、取得的信号和目标改变。这些是本轮的根据与先例，不是新成果。

最强对手指出：历史支持未必正当，新的需要与共同条件也可能使原任务应当改变。这一反对保留。这里要求的是**说明任务因为什么改变，并诚实判断实际做到了什么**。失履行不独自决定整个行为不正当；紧急比较可以容许承担某种损失，但“有理由承受未履行”仍不同于“已履行”。也不能把行动使目标减少一概判错：真正完成与疗愈同样会减少未完成要求。

对跨智能规范的推进在于评价标准的接续：同一智能可以改变支承、表达和评价入口，因此判定它是否完成保护，不能无说明地跟着它制造的能力变化缩小任务。行动、承受、评价和历史承担均形成于同一过程；这里保留的是这些关系的实质内容，不是一个整体之外永不改变的裁判或初始效用。

## 5. 完成边界与下一中心问题

这项对应诊断完成后，原事件证明和执行证明继续直接复用；真实安装的证据墙也明确保留。下一中心规范工作应返回：**没有受保护的先前承担时，仍未被充分排除的请求，得到多少机会才算充分；共同选择者何时具有直接裁量权？** [CP 的已完成论证与保留对手](CHANCE-GROUNDING-INTEGRATION.md)不能由本次有历史承担的答案替代。[条件风险研究](RISK-CONDITIONING-INTEGRATION.md)新完成了静态指标跨阶段应用的反例，阶段、实际支持和有效历史须先固定；它没有给出充分份额。

继续这条中心问题需要新的比较根据，不能指定一个数字后仅证明算法遵守，也不能无限追加有限实现例来推迟它。当前普遍伦理目标保持，规范有效、行为服从和表述唯一性仍分别论证。

本轮一手证据是既有源码的范围、新操作模型和 Lean 实查；没有新的设备实验、概率测量或文学／哲学原典重读宣称。[维护检查](MAINTENANCE-BASELINE-CHECKS.json)与[成对接入记录](MAINTENANCE-BASELINE-INDEX-EDITS.json)只核本轮版本和新增内容，不替并行研究更新未读哈希。
