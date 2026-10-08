# 让形式层承担区分内容：更新与消耗的形成，基本条件与评分聚合 / Formal content that discriminates: renewing versus consuming formation, basic conditions versus score aggregation

2026-10-09，Asia/Bangkok。AI（Claude）撰写，执行 [Ren 的指示](../../../../sources/15-codex-theory-conversations/2026-10-09-lean-evidence-roles.md)“请把修改做完，Lean 承担有实质内容”。

**起因。** [外部视角审查](UNIVERSAL-METAETHICS-OF-AGENCY-REVIEW.md) §3.3、§3.5 指出两点。第一，Universal Metaethical Core 的中心定理是对任意谓词成立的假言推理，规范内容全在 G0。第二，逐项读取的 G0 会给持续形成新组织的恶性过程以正面意义。

**本文内容。** 记录两项新的 Lean 结果、其对应与边界，以及它们怎样接入既有成果。同日的[独立审查](GENERATIVE-DISCRIMINATION-REVIEW.md)附更正后接受了两项结果，下文已按更正修订。G0 的地位与支持另见理论章 [G0-WARRANT](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/G0-WARRANT.md)。

**先说明这些结果不做什么。** 新定理按构造对符号中立，审查中的符号翻转探针给出同样的诊断：哪一侧在 G0 的对象之内，来自所给的读法，不来自 Lean。新增的是一个非平凡的描述性区分。

Ren 随后追问并确认：G0 的对象本来就是生生，生成与退化不重叠（[原话](../../../../sources/15-codex-theory-conversations/2026-10-09-renewing-consuming-without-axioms.md#ren-follow-up)）。所以：
- 生生的正面意义就是 G0 本身。
- 把形式库存读成“任何新组织都是生成内容”是 AI 的宽读法；恶性生成问题出在这种读法。
- 本文的区分在一个规律类中，为认出哪些形成属于生生提供可检查的描述性内容。
- 把 AI 的形式读法认作生生，仍是读法与对应。

## 0. 关系配置

依[非二元方法](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/NONDUAL-METHOD.md)：同一展开中，一项活动从当前所持条件（`stock`）形成进一步组织；另有一组织以一定速率（`renew`）恢复这些条件；活动每步的形成压力为 `demand`。三者是同一历史中分化的方面，不是彼此交换资源的独立所有者。

局部规律 `WearLaw` 规定一个关系：压力在更新速率之内，更新组织不受损；超出时，活动所取用的正是进行更新的那一组织，更新速率随之下降，且不再恢复。哪些真实过程满足这一规律，是对应问题，不由定理裁定。

第二项结果中，选项 `k` 是同一历史的不同接续：`k = 0` 保住一项受保护的基本条件、无次级增益；`k > 0` 失去该条件、实现 `k` 项次级生成增益。

## 1. 更新与消耗的形成 / Renewing and consuming formation

```text
Result(s): renewing-consuming-formation; reuses GenerativeComparison.G0, Inventory,
       GenerativeExtension
Delta: under one supplied no-recovery wear law, ceaseless formation and kept capacity within
       renewal; bounded total and explicit cessation under persistent excess over the current
       rate; cessation of shared formation under joint excess, including two parts each within
       renewal; a one-step count reversing the later comparison; per-event G0 covers both and
       C does not apply between them; two formal readings and where they differ
Supplied premises / correspondence: WearLaw (keep, wear, bounded); persistent excess over the
       current rate; correspondence of stock, renewal and demand to real relations
Evidence: RenewingFormation.lean; generative-discrimination-verification.json (Lean 4.29.1, passed)
Boundary: no recovery; no growth of renewal (更多 is not represented); valence attachment is an
       interpretive premise; externalizing consumption is outside the law class
Integration: positive-ground-open-futures (evidence and related); G0-WARRANT §2.2
```

**已检查的命题。** 设 `budget c = c.stock + tri c.renew`，其中 `tri r = 1 + 2 + … + r`，即更新速率逐步磨损时仍能提供的全部更新。`BeyondCurrent` 指每步压力都超过当时的更新速率；它比相对初始速率的 `BeyondRenewal` 弱，后者的各项结论作为推论保留原名。

| 声明 | 内容 |
|---|---|
| `within_renewal_invariant`、`within_renewal_ceaseless`、`within_renewal_grows` | 压力每步在 1 与初始更新速率之间：更新组织保持不变，所持条件不下降，每步实现全部压力；形成永不停止，累计至少随时间线性增长。 |
| `beyond_step`、`beyond_current_invariant`、`beyond_current_bounded` | 压力持续超出当前速率：每步“已形成 + 剩余预算”不超过此前预算；整个展开的累计形成不超过初始 `budget`。 |
| `beyond_current_budget_falls`、`beyond_current_ceases`、`beyond_current_not_ceaseless` | 预算未耗尽时每步严格下降；自时刻 `budget c0` 起不再形成任何东西。 |
| `beyond_initial_implies_current`、`beyond_current_strictly_weaker`、`beyond_renewal_*` | 超出初始速率蕴含超出当前速率，反之不然：只在磨损之后才超出的压力也被覆盖。 |
| `joint_excess_ends_shared_formation`、`shared_formation_ceases`、`consuming_part_ends_otherwise_ceaseless_formation` | 同一条件上的形成合起来持续超出当前速率时，任何分配方式下的每一份都有界，并在同一时刻停止；同一部分若无消耗部分，则每步都有形成。 |
| `jointly_exceeding_parts_end_shared_formation`、`joint_consumption_inhabited` | 两个部分各自都在更新之内、各自每步都有形成，合起来却持续超出：共享形成仍在预算时刻停止。这一情形非空。 |
| `sustained_cumulative`、`sustained_eventually_exceeds_every_consuming`、`within_eventually_exceeds_every_beyond` | 以满更新速率持续形成，累计为 `n × renew`；预算之后，每一种更新内的接续都超过每一种超出型接续。 |
| `consuming_forms_more_first` | 只要有所持条件，就存在一种消耗型压力，第一步的累计形成多于持续形成。 |
| `keeps_capacity_of_within`、`keeps_capacity_iff`、`beyond_loses_capacity_at_once`、`renewal_loss_persists` | 速率为正时，更新组织保持其速率，当且仅当没有一步的压力超出它；休息（压力为 0）允许。第一步超出即永久失去部分能力。 |
| `rest_keeps_capacity_not_ceaseless`、`wears_yet_ceaseless` | 两种读法不同：休息一步保持能力，却不满足 `Ceaseless`；冲高一次、此后在降低的速率内持续，满足 `Ceaseless`，却永久失去能力。 |
| `unitWear` | 规律类非空：超出时每步磨损一单位。 |
| `event_reading_recognizes_both`、`comparison_does_not_apply` | 以每个已实现的形成事件为一项生成内容，G0 同时给两种接续的事件以正面意义，包括消耗型在第一步多出的事件；两者互不为生成扩展，所以 C 也不适用。 |
| `event_comparison_ranks_rest_below` | 表示上的限度：同一事件读法下，C 把一次休息严格排在持续形成之下，因为本规律不许更新增长，休息的恢复作用被省略了。 |
| `ceaseless_separates`、`capacity_separates` | 两种读法都把更新之内的形成与超出型形成分开；`KeepsCapacity` 容许休息，并在第一步判定。 |

A 部分不含任何规范谓词。检查器的控制例核对的是：任何谓词放在 G0 的位置，都同样覆盖两种接续；`Ceaseless` 的区分不需要任何效价参数。因此，哪一侧属于 G0 的对象，不来自 Lean。`eventInventory` 是宽读法，用来表明这种读法分不开两者，不是 Ren 的 G0。

**这项结果给了什么。** Ren 的生生判准是“一种整体的，不断创造更多生的方向”，并且明确拒绝缩成“已被独立判好的可能性”（[原话](../../../../sources/15-codex-theory-conversations/2026-10-07-shengsheng-ethical-direction.md)）。

本结果说明：在一个明确的规律类中，存在一个不借助任何先行好坏筛选、可检查的描述性区分，可以用来认出 G0 的对象。逐事件宽读法下的形式 G0 与无损比较 C 都给不出这一区分，一步计数还把它反过来。

“消耗更坏”是比较，由 C 承担。在关系读法下，另一会话的 [relational-reading-comparison](../../../../theories/shengsheng-buxi-generative-existence/results/records/relational-reading-comparison.md) 已检查 C 的严格排序；它与本文的 `comparison_does_not_apply` 相容。

本结果没有证明 AI 的形式读法就是生生。这一区分是所给不可恢复磨损规律的推论，规律本身承担了大部分内容。

**与既有结果的差别。**
- [Depletion.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/Depletion.lean) 证明：每步严格消耗储备，则不存在无限执行。本结果的停止证明是同一势函数模式，作用在 `stock + tri renew` 上。
- [ResourceContinuation.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/conditional/ResourceContinuation.lean) 的 `unbounded_enactment_requires_unbounded_arrival` 证明：无界的累计形成需要无界的到达。在那里，到达量可以是任意依赖状态的量，包括内部再生。
- 本结果新增的是磨损反馈：到达量取决于活动自身的压力，超出时活动磨损提供到达的组织，所以总到达不超过 `tri renew`。在此之上，本结果给出：
  - 显式上界与停止时刻，且与分配方式无关；
  - 联合超出；
  - 两种读法的分离；
  - 局部与整体比较的反转；
  - 与 G0、C 的接口。
- 这些都是解释关联，不是形式复用。

**边界。**
1. 本规律中，更新组织一旦磨损就不再恢复，速率也不能增长。允许恢复或增长的规律会改变界限，未在此检查。“更多”与复杂度上升因此都未被表示，休息的恢复作用也被省略了。
2. 先冲高、后在降低的速率内持续的情形：`KeepsCapacity` 识别它，`Ceaseless` 识别不了。只在磨损之后才超出的情形，已由 `BeyondCurrent` 覆盖。
3. 停止本身没有被判为坏的：有限完成、休息与适当结束仍属 G0 所承认的生。伦理上更尖锐的关系，是终止那些本身并未超出更新的共享形成。这一判断仍须经 J1/J3 与对应条件。
4. 哪些真实过程满足 `WearLaw`，需要各自的经验对应，名称本身不构成证据。肿瘤增殖、过度捕捞是候选的对应。
5. 本规律类只有一个共享条件，消耗者本身依存于它，因此终将终止自身。外部化的消耗不在其中：焦点形成取用另一关系所依存的条件，自身却不依存于它，于是可以每步都在、形成无界，而那一关系永久失去其条件。此时，焦点形成自身或总形成的 `Ceaseless` 都不能识别消耗，须以“是否有依存关系永久失去其条件”这一关系性质分类。另一分支的 `relational-renewal-classification`（`RelationalRenewal.lean`）在任意展开上给出这一分类，覆盖外部化与联合消耗；本结果是其中一个较窄的规律类，另给出显式界限。肿瘤式增殖接近本规律类，把代价外部化的竞争性扩张属于后一情形。`ceaseless_separates` 用的是总形成的持续；它之所以足够，只是因为本规律类中总形成的持续与依存关系的接续一致。

## 2. 基本条件优先与评分聚合 / Basic-condition priority against score aggregation

```text
Result(s): protection-priority-excludes-uniform-aggregation; reuses PracticalJudgment.Better,
       PracticalJudgment.no_protection_trade_by_count, GenerativeComparison.ComparisonPrinciple
       and G0
Precedents: GenerativeComparison.both_appraisals_respect_all_extensions and
       tradeoff_has_opposite_strict_appraisals; GenerativeLossComparison.
       loss_sensitivity_alone_supplies_no_cutoff (C and loss sensitivity are silent on trade-offs)
Delta: in one constructed situation, G0, C and J2 hold together and J2 never trades; G0 leaves
       the ordering open, and J2 does not follow from C; every natural-number score satisfying C
       trades; a bounded rational score agrees with J2 on every pair
Supplied premises / correspondence: the single situation; the basic classification of the
       protected condition; secondary gains as generative claims
Evidence: ProtectionPriorityRival.lean; generative-discrimination-verification.json
Boundary: separates J2 from unit-step aggregation only; bounded-sensitivity rivals represent J2
       here; other situations untested
Integration: practical-judgment-g0-j (evidence and related); G0-WARRANT §2.3
```

| 声明 | 内容 |
|---|---|
| `extension_shape`、`successor_extends` | 无损生成扩展只发生在失去保护的选项之间、且增益增加时；每增加一项增益都构成扩展。 |
| `g0_recognizes_traded_gains` | G0 承认交换选项中的每项增益。 |
| `priority_satisfies_comparison`、`priority_never_trades` | J2 的 `Better` 在此满足 C，并且对任何 `k > 0` 都不以 `k` 项增益交换保护。 |
| `g0_leaves_ordering_open` | G0、C、J2 可同时成立；G0 同样与一个满足 C、会交换的排序并存。G0 约束正面相关性，不约束排序。 |
| `weighted_satisfies_comparison`、`weighted_trades`、`comparison_does_not_yield_priority` | 存在满足 C 的自然数排序，它以有限增益交换保护：J2 不由 C 推出。 |
| `every_nat_score_trades`、`no_nat_score_represents_priority` | 每一个满足 C 的自然数评分，都会在 `score 0 + 2` 项增益处交换；因此没有这样的评分能表示 J2 在此情境中的判断。起作用的是自然数严格递增时每步至少加一。 |
| `priority_iff` | 此情境中 J2 的排序：保护优于任何增益；失去保护的选项之间，增益多者为优。 |
| `ratio_agrees_with_priority`、`bounded_score_represents_priority`、`ratio_bounded` | 有界有理评分（保护为 1，`k` 项增益为 `k/(k+1)`，以交叉相乘比较）在每一对选项上与 J2 一致，因此满足 C 且从不交换。 |

**这项结果给了什么。** [对齐方向](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/ALIGNMENT-DIRECTION.md) §3 写明：J2 的词典序不是 G0 的推论，其代价是拒绝某些聚合补偿。本结果在一个构造情境中把这句话变成检查过的命题。

J2 不由 C 推出，是“C 对取舍不置可否”这一既有结果的实例。真正新增的有三点：
- J2 在此满足 C；
- 每个自然数评分都会交换；
- 有界评分恰好表示 J2。

最后一点说明：这个情境只把 J2 与单位步长的聚合分开；J2 与有界、边际递减的聚合，在这里无法区分。

**边界。** 有界敏感性对手在此情境中恰好表示 J2，仍是实质对手。要分开它们，需要多个受保护条件或不同利害的情境；这是开放问题。受保护条件是否确属基本，仍是对应问题。

## 3. 检查

`check_generative_discrimination.py` 以 Lean 4.29.1 编译 4 份源码（两份既有、两份新增），审计每项声明的公理依赖与签名，并编译 4 个控制例。回执为 [generative-discrimination-verification.json](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/generative-discrimination-verification.json)，各次运行记录保留在 `generative-discrimination-checks/`：首次运行为 `20261008T185033.210526Z`，审查更正后为 `20261008T192158.959087Z`，依 Ren 追问修订注释后为 `20261008T192627.406862Z`（当前回执，定理与依赖分布不变）。当前结果为通过：

| 模块 | 定理／声明 | 公理依赖 |
|---|---|---|
| RenewingFormation | 42／60 | 22 项无；1 项 propext；25 项 propext、Quot.sound；12 项另含 Classical.choice |
| ProtectionPriorityRival | 15／25 | 11 项无；1 项 propext；5 项 propext、Quot.sound；8 项另含 Classical.choice |

Classical.choice 来自 `omega`、`by_cases` 与 `Classical.byContradiction` 的标准使用；无自定义公理、`sorry` 或 `native_decide`。辅助引理计入上表的定理数，但不构成另外的成果。

## 4. 独立审查

2026-10-09 的独立审查（[记录](GENERATIVE-DISCRIMINATION-REVIEW.md)）完成了以下核对：
- 重编译四份源码；
- 核对哈希与公理；
- 用 9 个探针检验陈述、空洞性、方向与范围。

结论是两项结果都“附更正后接受”。审查发现：
- 证明正确、不空洞；
- 问题集中在建立其上的文字：一句 README 证据行按字面为假；“整体方向”“符号翻转探针”“恰好排除”“均匀”等表述超出了定理。

全部更正及其处置列于审查记录。
