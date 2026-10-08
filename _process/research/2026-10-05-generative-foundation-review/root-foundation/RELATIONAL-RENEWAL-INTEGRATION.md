# 参与关系中的更新与消耗：无公理的关系性区分 / Renewing and consuming as a relation to participated conditions, without axioms

2026-10-09，Asia/Bangkok。AI（Claude）撰写，执行 [Ren 的指示](../../../../sources/15-codex-theory-conversations/2026-10-09-renewing-consuming-without-axioms.md)：“请完成用关系结构把两种形成分开：一种更新它所参与关系的继续形成条件，另一种消耗这些条件。这两个，应该不需要任何axiom”。起因是[外部视角审查](UNIVERSAL-METAETHICS-OF-AGENCY-REVIEW.md) §3.3 的恶性生成问题。证明源为 [RelationalRenewal.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/RelationalRenewal.lean)，成果记录为 [relational-renewal-classification](../../../../theories/shengsheng-buxi-generative-existence/results/records/relational-renewal-classification.md)。

同日 Ren 追问：“为什么？我G0是什么？generative和degenerate虽然都在一个becoming model上，但是他们不overlap吧”（[原话](../../../../sources/15-codex-theory-conversations/2026-10-09-renewing-consuming-without-axioms.md#ren-follow-up)）。§6 据此修正，原文保留；“消耗更坏”这一比较由 [RenewalComparison.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/RenewalComparison.lean) 接入 G0/C 并检查，记录为 [relational-reading-comparison](../../../../theories/shengsheng-buxi-generative-existence/results/records/relational-reading-comparison.md)。

## 0. 关系配置

依[非二元方法](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/NONDUAL-METHOD.md)，先说明配置。同一展开中，若干形成持续发生；它们的继续依存于某些条件处在一定水平；它们的活动又取用、改变这些条件。条件常常由依存于它的那一形成自己更新：机体维持自己的活力，社群维护自己的公地，生态维持自己的土壤。形成、条件和依存是同一历史中分化的方面，不是先有独立所有者、再交换资源。

## 1. 成果块

```text
Result(s): new relational-renewal-classification. Related, not formally reused: renewing-consuming-formation
       (narrower law class), Depletion.lean, ContinuationRenewal.lean, CollectiveDestruction.lean,
       endpoint-loss-and-return, positive-ground-open-futures
Delta: a classification of formation by its relation to the conditions of the relations it participates in,
       defined over arbitrary unfoldings, exclusive and not exhaustive; irreversibility of consumption derived
       from the renewer's dependence on what it renews; formation at every step and the focal formation's own
       trajectory shown not to decide the class; joint consumption without a single consumer; escalation that
       begins within renewal. All with zero axiom dependencies.
Supplied premises / correspondence: definitions only for the general part; for the law family, levels,
       support thresholds, renewal and draw rates are local representations of one shared condition
Evidence: RelationalRenewal.lean; relational-renewal-verification.json (Lean 4.29.1, passed; 35 theorems,
       60 declaration audits, every axiom set empty; 4 application examples)
Boundary: one shared condition in the law family; no substitution between conditions; strict per-step renewal
       (seasonal cycles fall under neither); attribution within joint consumption not formalized; no ethical
       ranking; real correspondence not established
Integration: THEORY-OF-BECOMING §renewing-and-consuming-formation; review §3.3; goal theory-of-becoming

Result(s): new relational-reading-comparison. Formal reuse: relational-renewal-classification
       (overdraw_consuming, within_renewal_renewing, independent_overdraw_persists, renewing_not_consuming);
       GenerativeComparison G0, Inventory, Extends, GenerativeExtension, ComparisonPrinciple (imported unchanged)
Delta: the relational classification fed into GenerativeComparison's inventory. Under the relational reading
       (active events of non-consuming formations as grounds), G0 credits exactly those events; for every law of
       the family drawing beyond renewal, C ranks the unfolding with the focal formation strictly below the same
       unfolding without it; the broad event reading leaves the two incomparable and admits an irreflexive,
       transitive C-respecting comparison preferring the overdraw; sharing extends winning by consumption under
       both readings
Supplied premises / correspondence: C as a hypothesis (the comparisons use C, not G0); the relational reading of
       G0's generation; the absent course as "the same unfolding without the focal formation"
Evidence: RenewalComparison.lean; same receipt (15 theorems, 24 declaration audits, every axiom set empty;
       4 further application examples)
Boundary: whole-continuation classification (a consuming formation's events before its overdraw are not grounds);
       mixed cases not decided by C; one law family; C's defense as an articulation of G0 is philosophical
Integration: §6 below; THEORY-OF-BECOMING §renewing-and-consuming-formation; review §3.3
```

## 2. 定义：只用关系，不用评价

`Unfolding` 只给出：各条件在各步的水平，各形成在各步是否发生，一项形成依存于哪些条件、需要它们处在什么水平，以及它取用哪些条件。

| 定义 | 含义 |
|---|---|
| `Supported` / `Dependent` | 形成所依存的条件都达到其需要；形成只在受支持时发生。 |
| `Participates f c` | f 依存于 c，或 f 取用 c。这是“它所参与关系”的条件。 |
| `Renewed c` | 在每一步，c 都维持在依存于它的每一项形成所需的水平。 |
| `Consumed c` | 某项依存于 c 的形成，自某步起永久失去 c 的支持。 |
| `RenewingIn f` | f 参与的每个条件都得到更新。 |
| `ConsumingIn f` | f 取用的某个条件被消耗。 |

这些定义中没有“好”“坏”“应当”或任何评分，只说明哪些形成在什么时候还能继续。因此 Ren 所说的“不需要任何axiom”在两层上成立：

1. **没有规范或附加实质公理。** 分类由同一展开中的依存、取用和水平决定。定义说明分类的含义，不预先判定任何一类形成的价值。
2. **Lean 层没有公理依赖。** 检查器要求每项声明的公理集为空，连 `propext` 也没有。为此本模块自证了所需的自然数减法引理，没有调用 Lean 核心库中依赖 `propext` 的版本。

本结果完成的是区分，以及据此对恶性生成的识别；这两项都不需要公理。说更新型形成具有正面意义，就是 G0 本身；本结果给出 G0 所说的“生”的关系内容（见 §6）。

## 3. 已检查的命题

**一般部分（任意展开）。**

| 声明 | 内容 |
|---|---|
| `renewing_not_consuming`、`renewed_not_consumed` | 两类互斥。 |
| `fluctuating_neither` | 不穷尽：支持反复出现却不持续的情形既非更新型也非消耗型，分类不是强加的二分。 |
| `renewing_keeps_support` | 更新型形成的每个依存条件在每一步都支持它。 |
| `lost_support_ends` | 条件被消耗时，依存于它的形成自那时起不再发生。 |
| `unrenewed_drawdown_finite` | 若某条件没有任何更新，而形成每次发生都使它下降，则该形成只能发生有限次。中间可以停歇，所以缺少的是更新，不只是休息。这比 `Depletion.lean` 要求每一步都严格下降更弱。 |

**规律族。** `Law` 表示一个共享条件：一个依存于它的维持性形成在条件支持它时加以更新；焦点形成在受支持时发生，取用一定量并可能有所贡献；`formed` 计数焦点形成在每次发生时形成的新组织单位。

| 声明 | 内容 |
|---|---|
| `within_renewal_sustains`、`within_renewal_renewing` | 取用不超过更新与贡献时，焦点形成是更新型的，每一步都发生，形成量无界（`formed t = t`）。更新不是静止。 |
| `no_return_below_support`、`permanently_below` | 一旦条件跌破维持性形成的支持，更新本身就停止；焦点形成的贡献若不超过取用，条件不能回升。消耗的不可逆来自更新者对被更新条件的依存，而不是另设“速率不回升”。 |
| `overdraw_crosses_support`、`overdraw_consuming` | 取用持续超过更新与贡献时，在不超过初始水平的步数内跌破支持，焦点形成是消耗型，维持性形成永久停止。 |
| `dependent_overdraw_ends_itself` | 焦点形成若依存于该条件，它也随之永久停止，总形成量有界：形成而后止息。 |
| `independent_overdraw_persists` | 焦点形成若不依存于该条件，可以每一步都发生、形成量无界，同时是消耗型：依存于该条件的关系永久失去它。 |
| `formation_does_not_decide` | 每次发生都形成一个新单位，这对一切规律成立；培育型因此生生不息，恶性增长却消耗所属组织的条件、终止自身、形成量有界。“形成新组织”不能区分二者。 |
| `own_trajectory_does_not_decide` | 两段展开中，焦点形成自身每一步的发生和形成量完全相同；一个是更新型，一个是消耗型。没有任何只看形成自身轨迹的谓词（持续、成功、增长）能决定分类。 |
| `jointly_consuming` | 两项形成各自单独取用都在更新之内；一起取用则消耗，二者与更新它们共同条件的关系一起停止。没有单一的消耗者，分类属于它们的共同关系。 |
| `escalation_consumes` | 取用逐步升级，前三步都在更新之内，条件水平甚至上升；此后超出更新，消耗，并终止自身。 |

## 4. 对恶性生成的回答

审查的问题是：逐项读取的 G0，加上“一切能够持续形成新组织的过程”这一范围，会给恶性生成以正面意义。三个案例在关系结构中的位置如下：

- **癌细胞增殖。** 它依存于所属机体维持的条件，又以超出该机体更新的速度取用这些条件。`dependent_overdraw_ends_itself`：它终止机体对条件的更新，随后终止自己；它的“持续形成新组织”只是有界的一段。
- **军备竞赛。** 双方依存于共同的经济与生态条件，每一步的取用回应对方。`escalation_consumes`：起初在更新之内，看似可持续，越过更新后即为消耗；`jointly_consuming`：即使每一方单独都在更新之内，共同的取用也可以消耗。
- **meta-attractor 中自我强化的“赢”。** 赢家的继续常常不依存于输家的条件。`independent_overdraw_persists`：它可以每一步持续、无界地形成新组织，同时永久消耗依存关系的条件。`own_trajectory_does_not_decide`：只看赢家自身，无论看它的持续、成功还是增长，都无法与可持续地共享条件的形成区分。

第三个案例说明，Ren 的表述中“它所参与关系”是必要的。若只问一个形成能否持续，赢家会通过检验；问的是它所参与关系的继续形成条件，赢家就是消耗型。“生生不息”中的“不息”因此不是单个形成自身的不息，而是它参与的生成关系的不息。

Ren 在[生生方向](../../../../sources/15-codex-theory-conversations/2026-10-07-shengsheng-ethical-direction.md)中给出的第三种范围是“一切能够**持续**形成新组织的生成过程”。按本结果的关系读法，“持续”并不包括消耗型形成：依存者终止自身，不依存者终止它所参与的关系。

## 5. 与既有及并行结果的关系

| 结果 | 关系 |
|---|---|
| [Depletion.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/Depletion.lean) | 单一储备在每一步严格下降时没有无限执行。`unrenewed_drawdown_finite` 放宽为只在形成发生时下降、其余时间不回升。相关，不导入。 |
| [ContinuationRenewal.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/ContinuationRenewal.lean) | 无限继续需要更新反复出现，且更新本身不推出无界新颖性。本结果说明更新相对于谁、由谁维持，以及消耗何时不可逆。相关，不导入。 |
| [CollectiveDestruction.lean](../../../../experiments/market-generativity/meta-attractor/CollectiveDestruction.lean) | 两个局部许可分别成立、共同执行却越限的算术见证。`jointly_consuming` 给出动力学版本，并加上共同条件更新的不可逆停止。解释关联。 |
| [renewing-consuming-formation](../../../../theories/shengsheng-buxi-generative-existence/results/records/renewing-consuming-formation.md) | 同日另一会话的较窄结果：在给定磨损规律下，更新之内生生不息，持续超出则总量以 `stock + tri renew` 为界并停止，共享形成随之停止，并附 G0 逐事件接口。它的不可逆来自规律字段 `bounded`，本结果则从更新者的依存推出；它的消耗型形成总会终止自身，不覆盖不依存的赢家；它没有一般分类。它的显式总量界与起初多形成的反转是本结果没有的。两者独立证明，互不导入。 |
| [endpoint-loss-and-return](../../../../theories/shengsheng-buxi-generative-existence/results/records/endpoint-loss-and-return.md) | 固定规律下保留全部端点可能当且仅当可以返回。`no_return_below_support` 给出一种具体的不可返回机制。解释关联，不是形式组合。 |
| [SITUATED-RENEWAL-PROOF](SITUATED-RENEWAL-PROOF.md) | 用量超过原有支持时继续需要补充或改变支承路径。本结果补充：补充若来自依存于该条件的形成，跌破其支持即失去补充路径。 |

## 6. 对 G0 的含义

本节于 2026-10-09 依 Ren 的追问修正（[原话](../../../../sources/15-codex-theory-conversations/2026-10-09-renewing-consuming-without-axioms.md#ren-follow-up)）。修正前的文字保留在本节末。

**G0 的对象本来就是生生。** G0 是“整体中的生及其继续生成具有基本正面规范意义”。把形式 `Inventory.generative` 读成“任何已实现的新组织”，是 AI 的形式化读法，不是 Ren 的 G0：审查 §3.3 这样读，并行结果的 `eventInventory` 把它设为恒真。“持续形成新组织”中的“持续”已经排除消耗型：依存的消耗者终止自身（`dependent_overdraw_ends_itself`），不依存的消耗者终止它所参与的关系（`overdraw_consuming`）。恶性生成问题出在读法，不出在 G0。本结果不是“限定” G0，而是给 G0 已有的对象一个可检查的关系内容。

**生成与退化不重叠。** `renewed_not_consumed` 与 `renewing_not_consuming` 证明：同一条件不能既被更新又被消耗，同一形成不能既是更新型又是消耗型。不重叠不等于穷尽，波动情形两者皆非。一次发生还可以同时参与两种关系，例如赢家维持自身的条件，同时消耗依存者的条件。重叠的是发生，不是关系；[Becoming 章](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/THEORY-OF-BECOMING.md)原有的“一次发生可能使某种继续成为现实能力，同时毁掉另一种条件”说的就是这一点。

**分工。** 哪些关系是生成、哪些是退化，属于描述；本结果完成了这部分，不需要公理。说生成一侧有正面意义，就是 G0 本身，不是 G0 之外另欠的工作。

**消耗更坏：由 C 判出，并已检查。** 形式 G0 逐项赋予正面相关性，本身不作比较；“更坏”是比较，在公开的形式路线中由 C 承担：完全覆盖且无损失、又多出生成的接续严格更好。C 被当作 Ren 所说“一种整体的，不断创造更多生的方向”的比较表述；这一辩护是哲学论证，不在 Lean 审计之内。[RenewalComparison.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/RenewalComparison.lean) 把本结果接入 `GenerativeComparison`，不加新前提，不依赖 Lean 公理：

| 命题 | 内容 |
|---|---|
| `g0_relational` | 关系读法，即库存只列不消耗形成的发生：G0 恰好肯定这些发生。对消耗者的发生，G0 不发出正面意义；这是沉默，不是负面判决。 |
| `overdraw_relational_extension`, `overdraw_comparison_ranks` | 规律族中凡超出更新取用的焦点形成，与同一展开中它不发生的接续相比：关系读法下后者是前者的生成扩展，C 把它严格排在上面；非对称的比较不能反过来偏好有它的接续。依存的（恶性增长）与不依存的（以消耗取胜）同样成立。 |
| `overdraw_broad_incomparable`, `broad_comparison_admits_overdraw` | 逐事件的广义读法下二者互不扩展；存在满足 C、非自反且传递的比较，偏好有该形成的接续。 |
| `malignant_comparison` | 上述两点在恶性增长参数上的实例。 |
| `contest_comparison` | 以消耗取胜与同一形成在更新之内的共享相比，两种读法下共享都是生成扩展，因为赢家自身的发生在两条接续中相同。差别在 G0：广义读法下 G0 仍肯定赢家消耗时的每次发生，关系读法下不肯定。 |

所以，让 C 能对恶性增长作出裁决的，正是对“生”的关系读法。原第 2 点“消耗型形成没有因此被判为‘坏’”修正如下：消耗永久取走依存者继续生成的条件；在 C 之下，消耗的接续严格不如其非消耗对照，这一点已在整个规律族中检查。有限完成、休息与适当结束仍不是消耗：它们停止，却不使依存者永久失去条件。

**仍开放。**

1. 混合情形：每条接续各有对方缺少的生成时，C 不裁决（`GenerativeComparison.tradeoff_has_opposite_strict_appraisals`）。对某些条件更新、对另一些条件消耗的发生，其总判需要更强的比较或 J 层承诺。
2. 波动情形的归属，以及周期层面的更新，尚未定义。
3. 关系读法按整条接续分类：消耗型形成在取用超出更新之前的发生，也不计为根据。逐步分类尚未确定。
4. 比较接续可行与否，属于 P/N 与情境，比较本身不决定。消耗所终止的依存关系是否构成须回应的损失、由谁回应，仍属 J1/J3 与对应条件。

**修正前的文字（保留）：**

> 逐项读取的 G0 以“已实现的新组织”为生成内容，在 `formation_does_not_decide` 的两种展开中都会发出正面意义。把 G0 的对象读作**生生**，即更新它所参与关系的继续形成条件的形成，就把癌、升级竞赛与赢家放在 G0 的对象之外。这一限制不是先行的好坏筛选：它由第 2 节的描述性定义决定，对任何评价符号都同样成立。Ren 拒绝把生缩成“已被独立判好的可能性”，这一要求因此得到保留。
>
> 仍需分清：
>
> 1. G0 给生生以正面意义，这仍是采用的规范承诺；本结果只决定它适用于什么。
> 2. 消耗型形成没有因此被判为“坏”。有限完成、休息与适当结束不是消耗：它们停止，却不使依存者永久失去条件。消耗所终止的依存关系是否构成须回应的损失，仍由 J1/J3 与对应条件判断。
> 3. 混合情形，即对某些条件更新、对另一些条件消耗，以及不穷尽的波动情形，都不能由本分类给出总判。

## 7. 反审与边界

**最强的对手说法：** 分类取决于给定的支持阈值与依存关系，所以“是否消耗”被转移到表示的选择上。回应：阈值与依存是关于实际关系的对应陈述，可以错，也可以经验检验，但它们不是评价。表示一旦给定，分类就由定理决定；改变阈值会改变结论，这正是可被反驳的条件。

**会改变本结论的情形。**

1. 依存者若通过未表示的替代路径恢复，即可替代条件，那么在单一条件表示中显示为消耗的情形，在更完整的表示中可能是更新。规律族只有一个共享条件，替代未建模。
2. `Renewed` 要求每一步都维持支持。季节性或周期性的系统可能在周期层面是更新型，在本定义下却归入“二者皆非”；周期层面的更新尚未定义。
3. 在一个总体得到更新的循环中，捕食之类的情形会使个别生命终止。本分类关于继续形成的条件，不抹去这些个别损失；个体层面的关系要单独表示。
4. 共同消耗中，哪一方改变就足以恢复更新，属于差异归因，本结果没有形式化。
5. 焦点形成在维持者停止后若贡献多于取用，就成了恢复者；`no_return_below_support` 明确排除了这一情形。
6. `formed` 是计数，不是复杂度量；规律族中的数值是局部表示。肿瘤、军备竞赛或任何具体竞争满足这些规律，需要各自的经验证据。

**检查。** `check_relational_renewal.py` 以 Lean 4.29.1 编译源码，逐项审计声明与签名，要求每项声明的公理集为空，并编译应用例。`GenerativeComparison.lean` 原样作为依赖编译，并记录其哈希；它由自己的检查器审计，不在本回执的公理审计之内。回执为 [relational-renewal-verification.json](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/deeper/relational-renewal-verification.json)，结果为通过。`RelationalRenewal` 有 35 项定理、60 项声明审计，`RenewalComparison` 有 15 项定理、24 项声明审计，公理依赖全部为空；编译 8 个应用例。定理数包括 8 项算术辅助引理，它们不是另外的成果。本次没有独立 agent 审查。

**English scope.** A formation is classified by its relation to the conditions of the relations it participates in, by dependence or drawing. It is renewing when every such condition keeps supporting each formation that depends on it, and consuming when it draws on a condition some dependent formation permanently loses. The two classes are exclusive and not exhaustive. When a condition is renewed by a formation that depends on it, drawing it below that formation's support ends the renewal, so the loss does not return within the law. A dependent formation that overdraws ends itself with bounded formation. An independent one can persist and form without bound while ending the dependent relation, and its own trajectory cannot be distinguished from that of a sustainable formation. Joint drawing can consume when each party alone is within renewal, and escalation that starts within renewal can consume. Neither the classification nor these results uses an ethical premise or any Lean axiom. Corrected after Ren's follow-up: G0's object was always 生生, so the result supplies the relational content of what G0 affirms rather than restricting G0, and generation and degeneration do not overlap as relations, although one occurrence can participate in both. That the generative side is positive is G0 itself. That consumption is worse is a comparison: with C and the relational reading, every overdraw in the law family is ranked strictly below the same unfolding without it, while the broad event reading leaves them incomparable and admits a strict C-respecting comparison preferring the overdraw. Mixed cases remain undecided by C, and finite fulfillment, rest and appropriate ending are not consumption.
