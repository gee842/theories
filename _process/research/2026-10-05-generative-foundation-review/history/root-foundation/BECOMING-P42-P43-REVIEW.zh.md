<a id="p42p43-独立审查反馈所及与边界--independent-review-of-p42p43-feedback-reach-and-boundaries"></a>
# P42–P43 独立审查：反馈、所及与边界

> **中文版（2026-10-17）。** 正典文本是[英文版](BECOMING-P42-P43-REVIEW.md)；本版由重构时从双语原文拆出，不与英文同步维护，两者有出入时以英文为准。

2026-10-10/11，Asia/Bangkok。**AI 独立审查（另一 agent，未参与撰写）。**

审查对象
- 应协调者要求追加

本审查只在 `review/` 下建文件。没有修改仓库，没有运行 make 目标或检查器，没有改变 git 状态。

<a id="english-summary"></a>

---

<a id="0-范围与方法--scope-and-method"></a>
## 0. 范围与方法

全文阅读两个模块与扩展。另读了：
- 它们所用的核心：`Significance`、`Interdependence`、`Admission`、`Regions`、`Continuation`（`Clearing`）、`Standpoints`（`FedBy`、`significant_iff_held`）、`Metaethics`（`Neutral`、`Valuation.shares`、`significant_iff`）；
- Ren 10 月 10 日的原话记录（含 `structural-names`、`zero-axiom-part-and-names`）；
- 此前的独立审查 `EVALUATOR-GROUNDING-REVIEW.md`、其论证与记录 `self-good-reachable-g0`；
- 被复用的记录：`one-axiom-yields-g0`、`held-lives-g0-is-centering`、`feeding-closure`、`closure-verdict-meets-axiom`、`metaethical-core-characterization`；
- HEAD 版章节 §6.7–§6.9。

超赋值论与亚赋值论（Fine 1975；Hyde 1997）、营养级联只依据**先前知识**，没有重读原文。

- (甲) 表示省略了某一关系
- (乙) 重构论证中未解决的推论
- (丙) 满足所述条件的真实反例

<a id="1-形式复核--formal-recheck"></a>
## 1. 形式复核

- 构建中的 `Feedback.lean`、`Boundaries.lean` 与被审文件逐字节相同。`Significance`、`Interdependence`、`Admission`、`Regions`、`Continuation`、`Standpoints`、`Metaethics`、`Flow` 与仓库核心相同。
- 公理审计（`probes/Audit.lean`，用 `Lean.collectAxioms` 遍历两个模块的全部常量）：`Becoming.Feedback` 229 个声明、`Becoming.Boundaries` 39 个，均无公理。
- 扩展副本 `probes/P43Ext_copy.lean` 编译通过，十个定理的 `#print axioms` 均无依赖；连同辅助声明共 14 个，0 个有公理。
- 探针：`ProbeA` 24 个声明、`ProbeB` 44 个、`ProbeC` 74 个，共 142 个，均无公理（`probes/namespace-audit/`）。全部是项证明，没有一个探针用到经典推理，所以每一个建议的新定理都可以进纯核心。
- 输出原样存于 `probes/*.out.txt` 与 `probes/namespace-audit/*.out.txt`。合并位置的检查在 `probes/merge-check/`（§6）。

<a id="2-p42反馈与所及--feedback-and-reach"></a>
## 2. P42：反馈与所及

<a id="f1乙重大把系统读作-ren-的中间层级中间层级坍缩为整体--reading-the-system-as-rens-middle-level-collapses-it-into-the-whole"></a>
### F1（乙，重大）把系统读作 Ren 的中间层级，中间层级坍缩为整体

`Flow.Shares` 不看时间、不看方向，而且只要共同依存就成立。`Flow.WithinSystem` 是等价类（`Flow.WithinSystem.symm`，与 `Closure.refl`、`Closure.trans`）。于是：
- 只要有一个条件，每个形成都在某一步依存于它或与它交换，每个系统就是整体（A1 `system_whole_of_commons`）。共享的大气、阳光、海洋都满足这一点，不论耦合多弱、发生在哪一步。
- 两个形成只要都依存于一个从未被交换的条件，就在同一系统中，而彼此毫无影响（A1 `Static.shares_unaffected`）。
- 在 `Clearing` 中，每个形成的系统都是整体（A1 `clearing_clearer_system`；扩展 `Clearing.system_whole`）。
  - 所以 `Clearing.levels` 中“栖居者在清除者的系统内”和 `Clearing.system_counts_dweller` 都不能区分系统层与整体层：在这里，以系统为界的意义就是公理。
  - 唯一区分二者的见证，是 `Protection` 中只与自己的条件相连的远处形成。
- 系统是一个划分：不能嵌套，也没有中心，同一类中每个成员的系统相同。
  - Ren 说的是 “so this is a relation that is self recursive - system and subsystem”，并问 “where is this system centered”。
  - Ren 回答的那段问话（AI 所写）以肿瘤为例。肿瘤所在的系统自然读作身体；按 `Shares` 读，它是一切与之共享某个条件者。
- 系统是整体时，沿共享条件画出的自我只有一个可容许边界：整体（A1 `only_whole`）。
  - 这时“沿共享条件下真”就是该立场上的公理（A1 `clearing_subTrue_shares_iff`；扩展 `Flow.unrestricted_iff_system_presupposed`，其文档自己写着 “the weaker version is the axiom”）。
  - “较弱版本给出整体的判断”之所以成立，是因为这一读法把整体放进了较弱版本。

另有一个居中、可嵌套的读法，已检查：**所及闭包**，即在“影响”关系下的闭包（B3 `WithinReach`）。
- 它包含部分所及的一切（`reaches_withinReach`），并位于系统之内（`withinSystem_of_withinReach`）。
- 沿它下真的前提弱于沿共享条件下真（`subTrue_affects_of_shares`），却同样给出对其中每个部分的公理判断（`presupposed_reach_verdict`）。
- 在 `Clearing` 中，清除者的所及闭包是 {清除者，栖居者}，不含来源（B5 `middle`）；栖居者的所及闭包只有它自己（B5 `centred`）。
- 以所及闭包为界的意义不是公理。但从清除者的立场，它判定清除者的部分失去栖居者，与公理相同（B5 `reach_counts_dweller`）。
- 它是前向的：清除者所依存的来源不在其中，所以它不包含供给闭包。
  - 以它为中间层时，各读法的蕴涵链下行到赤裸的自我（A3 `subTrue_of_larger`，A2 `subTrue_empty_iff`），而不到供给闭包。
  - 这一方向是否合 Ren 的意思，须 Ren 判断。

若本意是“在已高度耦合的世界里，所在的系统就是整体”，文本应明说此时较弱版本与公理重合。形式条件也应度量耦合，而不是只看有无一个共同条件。

此外，三个模块把三个不同的闭包读作 Ren 的层级，须统一：
- P40 把供给闭包读作 “the system that one is in”（`Interdependence` 文档与章节 §6.9）；
- P42 改读为共享闭包；
- P43 又把供给闭包读作“自身的依存”。

<a id="f2甲重大两种反事实影响闭包与判断所用的比较不一致--two-counterfactuals-the-influence-closure-and-the-comparison-used-for-verdicts"></a>
### F2（甲，重大）两种反事实：影响闭包与判断所用的比较不一致

影响闭包以经由他者的影响为根据：狼经由鹿保护森林（`Protection.guards`）。但所有判断与登记定理都用另一种比较：扣留部分，其余交换不变。在这一比较下：
- **狼的部分。** 它不到达森林。尽管狼在森林的影响闭包内，森林的支持在每一步都与无狼时的接纳相同。这个部分什么也没有开启，关闭了鹿：它是收窄的。公理之下它不保留有意义者（C1 `protection_invisible`）。
- **响应的流。** 模块自己给出一个鹿会响应的流（`unguardedFlow`，满足平衡、活动、汲取与依存）。与之相比，同一部分是混合的：
  - 有狼时第 2 步（自 0 计）接纳森林，无狼时不接纳；
  - 无狼时第 1 步接纳鹿，有狼时不接纳；
  - 公理之下两条路径互不保留（C1 `responsive_mixed`）。

  判断的类别随反事实而变：一种说收窄，另一种说混合。
- **来源。** 部分给出他者所取的东西时，比较可能根本不存在。`Clearing` 中扣留来源后，清除者仍每步从资源取一单位，没有自然数水平能平衡（C2 `no_levels_without_source`）；对来源的部分于是没有任何判断。
- **直接到达。** 在这一比较下，一个形成的支持只登记直接到达它的部分（`Flow.Balances.admits_unreached`）。
  - 只有在他者的支持与活动随之改变的比较中，影响闭包才是登记的范围，而模块还没有建立这种比较。
  - 所以 `unregistered_beyond_influence` 是真的上界，但不是紧的上界。“影响闭包读作反馈能登记的”须加这一说明。
- **行为与部分。** `Clearing.unregistered` 比较的是“清除与不清除”这一行为（另给的 `sparedFlow`），不是扣留一个部分。部分是形成的集合，判断机制不能把一个形成的某一行为与它的其余交换分开。

<a id="f3甲次要affectedbyreachesshares-不看步的次序--the-relations-ignore-the-order-of-steps"></a>
### F3（甲，次要）`AffectedBy`、`Reaches`、`Shares` 不看步的次序

`AffectedBy g h` 只要求 g 在某一步依存于 c，h 在某一步与 c 交换；交换可以晚于依存。

C4 `Late.affected_without_effect` 是一个见证：
- `false` 只在第 1 步交换，`true` 只在第 0 步依存；
- 于是 `true` 被影响、被到达，但每一步有无该部分都一样被接纳。

这些关系都是正确的上界，不是影响本身。精确化已检查：水平不同之处，必有成员在**此前**某步交换过（B4 `exchanges_before_of_differs`）。所以可以定义按时间排序的所及，进而得到前向的“光锥”闭包。

<a id="f4乙甲中等判断定理本身--the-verdict-theorem-itself"></a>
### F4（乙/甲，中等）判断定理本身

- **正确的推进。** `Flow.Balances.verdict_within_reach` 正确。它从动力学推出了 `Web.retains_bounded_iff_includes` 所需的覆盖条件：未被到达者有无该部分都一样被接纳。这是 P40 记录 `closure-verdict-meets-axiom` 的真实推进。
- **更强的形式。** 两个意义只要在部分所及之处一致，四个判断就相同（B1 `verdict_local`）。原定理是其中一个取公理时的特例。“the verdict on a part is decided within what it reaches” 精确说的正是 B1。
- **增加判断的形式。** “neither adds exactly where neither exceeds” 足以判断不增加，不足以确证增加。
  - 在意义可判定处，正面形式可构造地推出（B2 `adds_iff_exceeds_of_decidable`）；一般只到双重否定（B2 `not_not_adds_of_exceeds`）。
  - 所以“What is not derived”中这一条应改写：缺的只是可判定性，可以作为假设陈述，而不是不可推出。
- **只有保留。** `Flow.Balances.system_retains_iff` 只给出保留，不给出增加。公理在其中只用来把包含改写为公理的保留。

<a id="f5丙次要恰在其行为到达闭包之外处误判--misjudges--exactly-where-they-reach-beyond-that-closure"></a>
### F5（丙，次要）“恰在其行为到达闭包之外处误判”

C3 `Margin.reach_without_misjudgment` 是反例：
- 行动者的部分到达影响闭包之外的形成；
- 但有该部分时的水平包含无它时的水平，所以任何意义都保留；
- 于是以影响闭包为界的意义与公理判断相同。

已证的说法是：其行为只到达闭包之内时，判断与公理相同（B1 `verdict_local`）；到达之外时可能误判，而到达之外本身并不足以误判（C3）。

<a id="3-p43边界--boundaries"></a>
## 3. P43：边界

<a id="f6乙重大三前提推出公理是分解不是化约--the-reduction-is-a-decomposition"></a>
### F6（乙，重大）“三前提推出公理”是分解，不是化约

- **不变性即条件句。** 整体可容许时，不变性**恰是**条件句“预设下真 → 该立场上的公理”（A2 `boundaryInvariant_iff_conditional`，不以预设为前提；扩展的 `boundaryInvariant_iff_all` 是其带前提的形式）。
  - 它也恰是预设的确定性：在某处为真则处处为真（A2 `boundaryInvariant_iff_determinate`）。
  - 所以给定预设，不变性就是该立场上的公理。分解的形式是 A ⇔ B ∧ (B → A)。
- **在单个立场上。** 给定预设，不变性就是该立场上的公理，而 P39 已把公理读作边界中立（`one-axiom-yields-g0`）。
- **在各立场之间。** 预设处处下真、且中心覆盖时，处处的不变性等价于立场不变（扩展 `boundaryInvariant_iff_standpointInvariant`），即 N_std 的规则（`Valuation.shares`）用于延续的意义。
- **下真带有传递。** 沿一个关系的下真，带有种子与沿该关系的传递：沿空关系是赤裸的 S0（A2 `subTrue_empty_iff`），沿全关系就是公理（A2 `subTrue_total_iff`）。
- **复用。** 三前提因此把两个已有的分解搬到延续的意义上：
  - `Valuation.significant_iff`（连通整体上的种子、N_rel、N_std）；
  - `Valuation.significant_iff_held`（处处 S0 加 N_std，章节 §6.7）。

  此前论证 §9 已把“立场到规范的桥”定为 N_std、一项公开前提。依 AGENTS.md，记录须写明复用，不作独立新结果。
- **撤回 “Agreement between standpoints is then derived, not assumed”。** 在其余前提下，每个立场上的不变性等价于一个一致性前提。
- **不变性也向下传递。** 若某一延续从该立场没有意义，不变的预设处处为假（A2 `invariance_levels_down`）。
  - 这正是此前审查 P3 对容差指出的对等性。
  - 承认覆盖与不变性的批评者，可以否认预设本身，走现时目的的反思性出口。
  - 所以 “It is the one step a critic who grants the other two premises must deny” 字面为真，但须补上对等的另一面。
- **“It takes the place of the earlier route's tolerance”。** 给定预设，不变性承担了公理超出预设的全部内容，与当时容差加 Chain 的处境相同；只是它没有“难以分辨的小步”那样的动机，只有一步。

<a id="f7乙中等覆盖由可容许类构造进去--covering-is-built-into-the-admissible-class"></a>
### F7（乙，中等）覆盖由可容许类构造进去

沿一个关系，凡含中心、对关系封闭的区域都算自我的可容许边界，整体也在其中（`Boundary.whole`），所以覆盖自动成立（`subTrue_member`）。

“Boundaries closed along a relation meet it without further premise, since the whole is one” 形式上为真。但实质前提就在可容许类的选择里：这一选择让任何形成都不是任何自我的明确非成员。

<a id="f8乙中等超真与下真--super-truth-and-sub-truth"></a>
### F8（乙，中等）超真与下真

- **结构。** 结构正确：对可容许的完全精确化取全称或存在。`superTrue_member_iff` 正是“明确在自我之内”。
- **术语来源。** 模块没有引文献。“super-true”取自 Fine 1975 的超赋值论；“sub-true”取自亚赋值论（Hyde 1997），不是 Fine 的用语。
- **不是对“自我”的超赋值。** Fine 的可容许精确化须保持明确情形，并尊重半影联系。
  - 对关系封闭可以看作一种半影联系。
  - 但本模块的可容许类里，每个形成都在某个可容许画法之内，没有明确的非成员，所以它不是对日常“自我”这一模糊谓词的超赋值。
  - “整体可容许”正是关于自我的超赋值论者会否认的。
- **不变性即确定性。** `BoundaryInvariant` 就是预设的确定性（A2）：按经典读法，要么超真，要么在每个可容许画法上都不成立。
  - 关于自我的超赋值论者会说：正因为“自我”模糊，预设在窄的画法上真、在整体上假，所以是不确定的。
  - 假设不变性，就是假设这一预设没有半影。
- **两种辖域。** 这一说法正确。
  - 路线 (b) 是“∀g，确定在自我之内 → 有意义”，算子在窄辖域（`bounded_closure_iff`、`bounded_closure_least`）。
  - 公理是“确定地：∀g，在自我之内 → 有意义”，算子在宽辖域（`unrestricted_iff_superTrue`）。
  - “确定地”这一算子不对条件句分配，所以两者不同。
  - 建议用一个定理同时陈述二者，并写明路线 (b) 在此推广到任意关系。

<a id="f9乙中等对手的位置--where-the-rivals-sit"></a>
### F9（乙，中等）对手的位置

模块说：闭合坐标对手（此前审查 P5）与模糊自我否认覆盖。沿一个关系，覆盖自动成立，所以这些对手否认的是另一个前提：
- **P5 闭合对手**把意义建立在已形成的闭合上。
  - 沿一个该闭合不对之封闭的关系，它否认下真。例如操作闭合不对供给封闭：有机体由其外者供给，而 `subTrue_selfSignificant_iff` 要求整个闭包都有意义。
  - 沿一个该闭合对之封闭的关系，它只在该闭合处持有预设，否认不变性，正如路线 (b) 在供给闭包处（`Clearing.without_invariance`）。
  - 只有同时把可容许的画法限于该闭合时，它才否认覆盖（`Clearing.with_fixed_boundary`）。
- **模糊自我**：每个可容许画法都把陌生人排除在外时，否认覆盖，这是模块所述的情形；陌生人在边缘时，预设不确定，否认的是不变性（A2 `boundaryInvariant_iff_determinate`）。
- **P7 在有限距离处归零的分级权重**：权重在闭包内归零时，否认沿该关系的下真；在闭包外归零时，否认不变性；都不是否认覆盖。模块没有给它定位。
- **认知主义的清晰未知断点**：可容许类是单元集，否认覆盖，除非断点就是整体。
- **现时目的评价者**否认下真。

<a id="f10乙次要层级次序没有定理--the-order-of-levels-has-no-theorem"></a>
### F10（乙，次要）层级次序没有定理

“super-true, sub-true along sharing a condition, and sub-true at the self's dependence” 这一次序可由 `Boundary.of_larger` 得到一串蕴涵，已检查（A3 `presupposition_levels`）：超真 → 沿共享下真 → 沿受影响下真 → 沿供给下真。

但在 `Clearing` 中前两者重合（系统即整体），模块的见证分不开它们。另外，这里把 Ren 的“the self”读作供给闭包；赤裸的自我是空关系（A2 `subTrue_empty_iff`）。

<a id="4-系统内的行为--conduct-within-the-system"></a>
## 4. 系统内的行为

`Flow.Balances.presupposed_system_verdict` 与 `Clearing.own_presupposition` 在表示之内为真：对成员全在中心系统内的部分，没有失败。它们的成立依赖于：
1. 扣留比较，其余交换不变。经由他者的效果看不见，判断类别可以改变（F2，C1）。
2. 扣留后的水平存在。关键给予者没有判断（C2）。
3. 部分是可判定的形成集合。一个形成的某一行为不能单独分出（F2）。
4. 离散步与自然数量。
5. 把系统读作共享闭包。系统是整体时，前提就是该立场上的公理（F1）。
6. 部分成员全在系统内。联合部分若含系统外成员，就有反例：从远处形成的立场，以其系统为界的意义判其保留，公理判其失去鹿（C1 `mixed_part`）。
7. 保留取正面形式，增加只取否定形式（F4）。

在表示之外，若比较允许他者响应，扣留一个部分可以使他者与实际流中从未交换过的条件交换。例如没有狼时，鹿迁入另一系统的森林。那时以实际系统为界的意义看不到这一效果（甲，未形式化）。

还有，“the whole need not be admissible”有误导：沿共享条件，整体总是可容许的。本意是：不用不变性，也不用超真。

<a id="5-ren-的原话与-ai-的读法--rens-words-and-the-ais-readings"></a>
## 5. Ren 的原话与 AI 的读法

| 读法 | 评估 |
|---|---|
| 影响闭包读“自身反馈能登记的” | **可信**，须附 F2 的说明。 |
| “still need situational awareness”读作“须知道反馈之外” / read as knowing beyond one's feedback | **可信**，是 AI 的推衍；Ren 的括注附在“full truth set”上。 |
| 系统读“the system that one is in” / the system as "the system that one is in" | **过度**：使中间层级成为整体，与 Ren 的“system and subsystem”与“where is this system centered”不合（F1）。 |
| “weaker version”给出整体对系统内每一行为的判断 | **过度**：范围见 §4；系统即整体时，它的前提就是该立场上的公理。 |
| 预设读 Ren 的“belief” | **可争议**：Ren 说自我“can not justify itself without some sort of "belief"”，是在说明自我层最弱；把这一信念当作被授予的前提，是 AI 的一步。沿关系的下真也远强于“某一延续有意义”。 |
| 覆盖读“There is no absolute self”与“the universe/ecosystem that realizes its own existence” | **可争议**：后一句支持整体是“我们”的一种画法；前一句本身推不出覆盖；实质在可容许类（F7）。 |
| 不变性读“universal invariations”“for all beings” | **过度**：Ren 的不变性是“for every universe, becoming happens, the law follows”，即法则在各宇宙中的不变。“for all beings”最直接的形式是立场不变（N_std）；扩展已证，在给定前提下它与边界不变等价。 |
| “three claims Ren holds” | **过度**：这是助手在 AI 所写语境中的提议。Ren 的“i think you see the right direction”在记录中仍作待定读法。“every act presupposes that some continuation matters”不是 Ren 的话。 |
| 扩展：系统即整体读“Ren's highly entangled system” | **过度**：Ren 说的是“at this moment in time, the whole earth has become a highly entangled system, everyone country, every person, is heavily coupled into it”，是关于当下耦合强度的历史判断。形式条件是布尔的、不看时间，在有一个公共条件的任何世界、任何时代都成立（A1）。 |

“the continuation goes beyond one's cycle of life, goes beyond one's death” 没有被用到；它更自然地支持按谱系个体化与按时间排序的所及（B4）。

<a id="6-扩展-p43extlean--the-extension"></a>
## 6. 扩展 `P43Ext.lean`

十个定理全部正确，且无公理。

- **主张 (1)：接受。** `boundaryInvariant_iff_all` 正确。建议同时给出不带前提的 `boundaryInvariant_iff_conditional` 与 `invariance_levels_down`（A2），后者显示这一步可以双向走。
- **主张 (2)：接受定理，更正标题。**
  - “The two forms of the step are one”过度：没有处处的预设时，两者分开（A4 `forms_apart`：一个处处相同的意义满足立场不变，却不满足边界不变）。
  - 两者在所给前提下等价，是因为二者那时都等价于公理。
  - 应明说：边界不变在单个立场上就是边界中立（P39 对公理的读法）；`StandpointInvariant` 就是 N_std 的规则用于延续的意义。
  - `unrestricted_of_standpointInvariant` 与 §6.7 的结构同形：每个中心的 S0 加 N_std（`Valuation.significant_iff_held`、`Web.significant_iff_self`）。
  - 并撤回 P43 的“derived, not assumed”。

- **主张 (3)：接受定理，拒绝读法与“no invariance”的说法。**
  - 闭包是整体时，整体是唯一的可容许边界（A1 `only_whole`），所以不变性平凡成立，正如 `Clearing.with_fixed_boundary` 中单一边界的情形。
  - 这一步没有被去掉，而是放进了“边界对共享条件封闭”的要求。
  - `unrestricted_iff_presupposed_of_whole` 的文档应写明原因；假设名 `entangled` 应改为 `connected`。

- **主张 (4)：拒绝其推论。**
  - `Flow.unreached_within_system` 正确，说的是系统对外封闭：系统外的部分到达不了系统内。
  - 对自身部分的结论来自 `Flow.own_within_system` 与 `presupposed_system_verdict`，不来自它。
  - 对含系统外成员的联合部分，结论不成立（C1 `mixed_part`）。
  - 对完全在系统外的部分，以系统为界的意义判其保留，而公理可能判其失去。

- **文档与陈述。** `Clearing.without_standpoint_invariance` 的文档比陈述多两项（预设下真、每个形成在自身闭包内）：补入合取项或删去。
- **合并位置
  - 按所述计划把 `Clearing.system_whole` 放进 Feedback 不能编译：其第三个合取项用到 Boundaries 中的 `SubTrue`、`Boundary`、`SelfSignificant`（`merge-check/FeedbackPart.lean`：`SubTrue` 未知）。
  - `merge_ext.py` 的拆分可以编译且无公理：Feedback 留两个合取项，Boundaries 另立 `system_presupposition`（`merge-check/FeedbackPartSplit.lean`、`BoundariesPartSplit.lean`）。

<a id="7-须作的更正按严重程度-required-corrections-by-severity"></a>
## 7. 须作的更正（按严重程度）

1. **系统的读法
   - 加入 B3、B5 的定理（`Flow.WithinReach`、`Flow.reaches_withinReach`、`Flow.withinSystem_of_withinReach`、`Flow.Balances.presupposed_reach_verdict`、`Flow.subTrue_affects_of_shares`、`ClearingReach.reach_counts_dweller` 等；并入时后者可放在 `Clearing` 下）。
   - 加入 A1 的 `system_whole_of_commons`、`only_whole` 与扩展的 `Clearing.system_whole`。
   - 在 `Interdependence.lean` 的读法与章节 §6.9 中，撤回或标注“供给闭包也读 the system that one is in”。
2. **较弱版本
   - `Boundaries.lean` 的 “The weaker version gives the whole's verdict on conduct within one's system.” 作同样的限定。
3. **分解，不是化约
   - 标题 “The axiom from three premises” 改为 “The axiom decomposed: where its content lies”。
4. **两种反事实
   - 把 C1 `protection_invisible`、`responsive_mixed` 与 C2 `no_levels_without_source` 作为见证加入。
5. **扩展
   - `unrestricted_iff_presupposed_of_whole` 的文档加：“because the whole is then the only boundary”。
   - 不把 `Flow.unrestricted_iff_system_presupposed` 读作 Ren 的 “highly entangled system”。
   - `without_standpoint_invariance` 的文档与陈述对齐。
   - 按 `merge_ext.py` 的方式拆分 `Clearing.system_whole`。
7. **对 Ren 的归属
9. **超赋值术语
   - 模块或记录若引文献，注明 super-truth 取自 Fine 1975、sub-truth 取自亚赋值论（Hyde 1997）。
   - 注明本模块的可容许类没有明确的非成员，以及不变性就是确定性。
   - 把两种辖域写成一个定理。
10. **层级次序 / Order of levels**（F10）。加入 `presupposition_levels`，并写明在 `Clearing` 中前两种读法重合。
11. **“the whole need not be admissible”**。在 `Flow.Balances.presupposed_system_verdict` 的文档与模块说明中，把 “No invariance is used, and the whole need not be admissible.” 改为：
    > Neither invariance nor super-truth is used.
13. **正面的增加判断
    - 并加入这两个定理与 `verdict_local`。
14. **局部的文档与陈述

      这与定理自己的文档一致。
    - 模块说明中 `superTrue_all_iff` 补上 “where the whole is admissible”。
15. **记录与复用
    - P43 的记录写明复用：
      - `metaethical-core-characterization`（`Valuation.significant_iff`）；
      - `held-lives-g0-is-centering`（`Valuation.significant_iff_held`）；
      - `one-axiom-yields-g0`（公理读作边界中立）；
      - `feeding-closure` 与 P40 的路线 (b)。
    - P43 的增量是：边界与超赋值的表述、两种辖域的读法、对手的定位。`retains_agree_of_presupposed` 与 `Valuation.significant_of_presupposed` 是经 `Web.retains_agree`、`Valuation.premises_of_unrestricted` 得到的推论，不计为独立结果。
    - P42 的记录写明 `verdict_within_reach` 推进 `closure-verdict-meets-axiom`。`system_retains_iff` 与 `presupposed_system_verdict` 是它的推论。
16. **名称 / Names**（Ren 的命名规则，五处）。
    - `Protection` 改为 `Cascade`，取营养级联这一科学术语。`Protection` 命名的是一个角色，而所给关系是不经供给、经由他者的影响。
    - `Protection.guards` 改为 `Cascade.mediates`。
    - `verdict` 是法庭用词。核心称之为“按包含比较”与“四种情形”（`Becoming.Admission`），可用 `comparison` 或 `case`，如 `comparison_within_reach`。
    - 假设名 `entangled` 改为 `connected`。

<a id="8-探针--probes"></a>
## 8. 探针

文件
- `Audit.lean`：两个模块的公理审计；
- `P43Ext_copy.lean`：扩展的逐字副本加 `#print axioms`；
- `namespace-audit/`：每个探针文件全部局部声明的审计，结果为 A 24、B 44、C 74、扩展 14 个声明，0 个有公理；
- `merge-check/`：合并位置的检查（§6）；
- 输出：`*.out.txt`。

全部是项证明，`#print axioms` 均为 “does not depend on any axioms”。

| 编号 | 定理 | 显示 |
|---|---|---|
| A1 | `system_whole_of_commons`, `only_whole`, `clearing_clearer_system`, `clearing_subTrue_shares_iff`, `Static.shares_unaffected` | 一个公共条件即使系统为整体；系统为整体时唯一边界是整体；`Clearing` 中沿共享下真即公理；共同依存而不交换也同属一系统 |
| A2 | `boundaryInvariant_iff_conditional`, `invariance_levels_down`, `boundaryInvariant_iff_determinate`, `subTrue_total_iff`, `subTrue_empty_iff` | 不变性即条件句、即确定性，并可向下传递；预设的强度由关系决定 |
| A3 | `subTrue_of_larger`, `presupposition_levels` | 层级次序作为蕴涵 |
| A4 | `forms_apart` | 没有处处的预设时两种不变性分开 |
| B1 | `Flow.Balances.verdict_local` | 在所及处一致即判断相同 |
| B2 | `Flow.Balances.adds_iff_exceeds_of_decidable`, `Flow.Balances.not_not_adds_of_exceeds` | 正面的增加判断 |
| B3 | `Flow.Affects`, `Flow.WithinReach`, `Flow.reaches_withinReach`, `Flow.withinSystem_of_withinReach`, `Flow.Balances.presupposed_reach_verdict`, `Flow.subTrue_affects_of_shares` | 所及闭包：居中、可嵌套、前提更弱 |
| B4 | `Flow.Balances.exchanges_before_of_differs` | 按时间排序的所及 |
| B5 | `ClearingReach.middle`, `ClearingReach.centred`, `ClearingReach.reach_counts_dweller` | `Clearing` 中所及闭包是真正的中间层，且不含来源 |
| C1 | `Wolves.protection_invisible`, `Wolves.responsive_mixed`, `Wolves.far_system`, `Wolves.mixed_part` | 经由他者的保护在扣留比较中看不见；判断类别随反事实而变；含系统外成员的联合部分 |
| C2 | `Source.no_levels_without_source` | 关键给予者没有比较 |
| C3 | `Margin.reach_without_misjudgment` | 到达闭包之外而不误判 |
| C4 | `Late.affected_without_effect` | 受影响而无效果 |
| M | `merge-check/FeedbackPart.lean`（失败 | 合并位置 |

`#print axioms` 原样输出（节选，全部同形）

```text
'Becoming.ReviewP42.Flow.Balances.verdict_local' does not depend on any axioms
'Becoming.ReviewP42.Wolves.responsive_mixed' does not depend on any axioms
'Becoming.ReviewP42.Source.no_levels_without_source' does not depend on any axioms
'Becoming.ReviewP42.boundaryInvariant_iff_conditional' does not depend on any axioms
'Becoming.ReviewP42.ClearingReach.reach_counts_dweller' does not depend on any axioms
'Becoming.Clearing.system_whole' does not depend on any axioms
Becoming.Feedback: checked 229 declarations, 0 with axioms
Becoming.Boundaries: checked 39 declarations, 0 with axioms
```

（倒数第三行来自 `merge-check/FeedbackPartSplit.lean`。

注意：本版 Lean 中 `Nat.succ_ne_zero` 依赖 `propext`，带通配符的重叠模式匹配也会引入 `propext`。探针因此改用 `Nat.noConfusion` 与完整、不重叠的模式；并入核心时须照此写。

<a id="9-审查者自身的边界--reviewers-limits"></a>
## 9. 审查者自身的边界

- 探针是有限模型与一般定理，只显示所述条件下的推出或一致。对实际世界中系统是否为整体，只给出形式条件，不作经验判断。
- 没有重读 Fine、Hyde 或营养级联文献。
- 没有判断任一前提在规范上是否正确，只判断推论、对应、范围与读法。
- 响应式比较下系统可能被越出（§4），只是论证草图，没有形式化。
- 没有审查 `work_next/` 与 `next/` 中正在进行的合并；只检查了 `merge_ext.py` 对 `system_whole` 的放置。
