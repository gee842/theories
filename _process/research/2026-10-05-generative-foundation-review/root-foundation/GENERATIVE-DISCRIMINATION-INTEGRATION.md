# 让形式层承担区分内容：更新与消耗的形成，基本条件与标量聚合 / Formal content that discriminates: renewing versus consuming formation, basic conditions versus scalar aggregation

2026-10-09，Asia/Bangkok。AI（Claude）撰写，执行 [Ren 的指示](../../../../sources/15-codex-theory-conversations/2026-10-09-lean-evidence-roles.md)“请把修改做完，Lean 承担有实质内容”。起因是[外部视角审查](UNIVERSAL-METAETHICS-OF-AGENCY-REVIEW.md) §3.3、§3.5：Universal Metaethical Core 的中心定理是对任意谓词成立的假言推理，规范内容全在 G0；逐项读取的 G0 又会给持续形成新组织的恶性过程以正面意义。本文记录两项新的 Lean 结果、其对应与边界，以及它们怎样接入既有成果。G0 的地位与支持另见理论章 [G0-WARRANT](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/G0-WARRANT.md)。

## 0. 关系配置

依[非二元方法](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/NONDUAL-METHOD.md)：同一展开中，一项活动从当前所持条件（`stock`）形成进一步组织；同一展开中另有一组织以一定速率（`renew`）恢复这些条件；活动每步的形成压力为 `demand`。三者是同一历史中分化的方面，不是彼此交换资源的独立所有者。局部规律 `WearLaw` 规定一个关系：压力在更新速率之内，更新组织不受损；超出时，活动所取用的正是进行更新的那一组织，更新速率随之下降。哪些真实过程满足这一规律，是对应问题，不由定理裁定。

第二项结果中，选项 `k` 是同一历史的不同接续：`k = 0` 保住一项受保护的基本条件、无次级增益；`k > 0` 失去该条件、实现 `k` 项次级生成增益。

## 1. 更新与消耗的形成 / Renewing and consuming formation

```text
Result(s): new renewing-consuming-formation; reuses GenerativeComparison.G0 and Inventory
Delta: under one supplied wear law, ceaseless formation within renewal; bounded total and explicit
       cessation beyond renewal; cessation of co-dependent formation under any allocation;
       local first-step reversal of the whole comparison; per-event G0 covers both continuations
Supplied premises / correspondence: WearLaw (keep, wear, bounded); persistent excess over the
       initial renewal rate; correspondence of stock, renewal and demand to real relations
Evidence: RenewingFormation.lean; generative-discrimination-verification.json (Lean 4.29.1, passed)
Boundary: no recovery of the renewing organization in this law; ceasing is not shown to be bad;
       temporary surges and bounded-sensitivity regimes are outside the theorems
Integration: positive-ground-open-futures (evidence and related); G0-WARRANT §2.2
```

**已检查的命题。** 设 `budget c = c.stock + tri c.renew`，其中 `tri r = 1 + 2 + … + r`，即更新速率逐步磨损时仍能提供的全部更新。

| 声明 | 内容 |
|---|---|
| `within_renewal_invariant`、`within_renewal_ceaseless`、`within_renewal_grows` | 压力每步在 1 与初始更新速率之间：更新组织保持不变，所持条件不下降，每步实现全部压力；形成永不停止，累计至少随时间线性增长。 |
| `beyond_step`、`beyond_renewal_invariant`、`beyond_renewal_bounded` | 压力持续超出初始更新速率：每步“已形成 + 剩余预算”不超过此前预算；整个展开的累计形成不超过初始 `budget`。 |
| `beyond_renewal_budget_falls`、`beyond_renewal_ceases`、`beyond_renewal_not_ceaseless` | 预算未耗尽时每步严格下降；自时刻 `budget c0` 起不再形成任何东西。 |
| `shared_formation_ceases`、`consuming_part_ends_otherwise_ceaseless_formation` | 同一条件上的另一分化部分只要持续超出更新，任何分配方式下分给本部分的形成都有界并在同一时刻停止；同一部分若无此消耗部分，则生生不息。 |
| `sustained_cumulative`、`sustained_eventually_exceeds_every_consuming`、`consuming_forms_more_first` | 以满更新速率持续形成，累计为 `n × renew`；预算之后，它超过每一种消耗型接续。只要有所持条件，就存在一种消耗型压力在第一步形成得更多。 |
| `unitWear` | 规律类非空：超出时每步磨损一单位。 |
| `event_reading_favors_both`、`whole_direction_separates` | 以每个已实现的形成事件为一项生成内容，G0 同时给两种接续的事件以正面意义，包括消耗型在第一步多出的事件；把它们分开的是 `Ceaseless`，这是 A 部分的动力学性质。 |

A 部分不含任何规范谓词，因此审查中的符号翻转探针不适用：把 G0 位置换成任何谓词，`Ceaseless` 的区分依然成立。检查器的控制例明确核对了这一点。

**这项结果给了什么。** Ren 的生生判准是“一种整体的，不断创造更多生的方向”，并且明确拒绝缩成“已被独立判好的可能性”（[原话](../../../../sources/15-codex-theory-conversations/2026-10-07-shengsheng-ethical-direction.md)）。本结果说明这一整体判准有非循环、可检查的内容：在同一局部规律下，它把更新内的形成与消耗更新组织的形成分开，且不借助任何先行的好坏筛选。逐项计数的读法则会在早期偏向消耗型。审查 §3.3 的出路 (B) 因此在这个规律类中得到了形式化。

**与既有结果的差别。** [Depletion.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/Depletion.lean) 证明：每步严格消耗储备，则不存在无限执行。[ResourceContinuation.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/ResourceContinuation.lean) 的 `unbounded_enactment_requires_unbounded_arrival` 证明：无界的累计形成需要无界的到达。在那里，到达量是外给的。本结果中，更新本身由同一展开中的组织产生，并可被同一活动磨损，因此界限是内生的（`stock + tri renew`）。本结果还新增了对共享条件的部分的结论、局部与整体比较的反转，以及与 G0 的接口。两者是解释关联，不是形式复用。

**边界。**
1. 本规律中，更新组织一旦磨损就不再恢复；允许恢复的规律会改变界限，未在此检查。
2. `BeyondRenewal` 是相对初始速率的持续超出；先冲高后回落的情形不在定理之内。
3. 停止本身没有被判为坏的：有限完成、休息与适当结束仍属 G0 所承认的生。伦理上更尖锐的关系，是终止那些本身并未超出更新的共享形成。这一判断仍须经 J1/J3 与对应条件。
4. 哪些真实过程（肿瘤增殖、过度捕捞、自我强化的竞争性扩张等）满足 `WearLaw`，需要各自的经验对应；名称本身不构成证据。
5. 本规律类只有一个共享条件，消耗者本身依存于它，因此终将终止自身。外部化的消耗不在其中：焦点形成取用另一关系所依存的条件，自身却不依存于它，于是可以每步都在、形成无界，而那一关系永久失去其条件。此时焦点形成自身或总形成的 `Ceaseless` 都不能识别消耗，须以“是否有依存关系永久失去其条件”这一关系性质分类。另一分支的 `relational-renewal-classification`（登记中，`RelationalRenewal.lean`）在任意展开上给出这一分类，覆盖外部化与联合消耗；本结果是其中一个较窄的规律类。肿瘤式增殖接近本规律类；把代价外部化的竞争性扩张属于后一情形。

## 2. 基本条件优先与标量聚合 / Basic-condition priority against scalar aggregation

```text
Result(s): new protection-priority-excludes-uniform-aggregation; reuses PracticalJudgment.Better,
       PracticalJudgment.no_protection_trade_by_count, GenerativeComparison.ComparisonPrinciple and G0
Delta: J2's ordering satisfies C and never trades; a C-respecting scalar ordering trades (J2 is
       independent of G0 and C); every natural-number score satisfying C trades
Supplied premises / correspondence: the single situation; the basic classification of the
       protected condition; secondary gains as generative claims
Evidence: ProtectionPriorityRival.lean; generative-discrimination-verification.json
Boundary: bounded or diminishing-sensitivity rivals are not excluded; other situations untested
Integration: practical-judgment-g0-j (evidence and related); G0-WARRANT §2.3
```

| 声明 | 内容 |
|---|---|
| `extension_shape`、`successor_extends` | 无损生成扩展只发生在失去保护的选项之间、且增益增加时；每增加一项增益都构成扩展。 |
| `g0_recognizes_traded_gains` | G0 承认交换选项中的每项增益。 |
| `priority_satisfies_comparison`、`priority_never_trades` | J2 的 `Better` 满足 C，并且对任何 `k > 0` 都不以 `k` 项增益交换保护：G0、C、J2 可同时成立且有区分力。 |
| `weighted_satisfies_comparison`、`weighted_trades`、`comparison_does_not_yield_priority` | 存在满足 C 的标量序，它以有限增益交换保护：J2 不能由 G0 与 C 推出。 |
| `every_scalar_comparison_trades`、`no_scalar_represents_priority` | 每一个满足 C 的自然数评分，都会在 `score 0 + 2` 项增益处交换；因此没有这样的评分能表示 J2 在此情境中的判断。 |

**这项结果给了什么。** [对齐方向](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/ALIGNMENT-DIRECTION.md) §3 写明：J2 的词典序不是 G0 的推论，其代价是拒绝某些聚合补偿。本结果把这句话变成检查过的命题。在 C 的范围内，J2 恰好排除了“每项增益至少增加一个单位”的整个聚合对手类，而 G0 自身对此不置可否。已有的 `no_protection_trade_by_count` 说明 J2 不交换；本结果补上 J2 相对于 G0/C 的独立性，并补上被排除的对手类。

**边界。** 实数值、边际递减且有上界的评分（例如收敛到受保护选项以下）可以与 J2 在此例一致，仍是实质对手，未被排除。结论只针对这一个情境构造；受保护条件是否确属基本，仍是对应问题。

## 3. 检查

`check_generative_discrimination.py` 以 Lean 4.29.1 编译 4 份源码（两份既有、两份新增），审计每项声明的公理依赖与签名，并编译 3 个控制例；回执为 [generative-discrimination-verification.json](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/generative-discrimination-verification.json)，保留运行记录位于 `generative-discrimination-checks/`。结果为通过：

| 模块 | 定理／声明 | 公理依赖 |
|---|---|---|
| RenewingFormation | 21／35 | 14 项无；1 项 propext；14 项 propext、Quot.sound；6 项另含 Classical.choice |
| ProtectionPriorityRival | 10／17 | 8 项无；1 项 propext；4 项 propext、Quot.sound；4 项另含 Classical.choice |

Classical.choice 来自 `omega`／`by_cases` 的标准使用；无自定义公理、`sorry` 或 `native_decide`。辅助引理计入上表的定理数，但不构成另外的成果。本次没有独立审查，记录状态为 `recorded-checked`。
