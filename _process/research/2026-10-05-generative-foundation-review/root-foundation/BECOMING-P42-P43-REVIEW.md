# P42–P43 独立审查：反馈、所及与边界 / Independent review of P42–P43: feedback, reach and boundaries

2026-10-10/11，Asia/Bangkok。**AI 独立审查（另一 agent，未参与撰写）。**

审查对象 / Objects:
- `scratchpad/p42/src/Feedback.lean`（P42），sha256 `5b6ba16326ae8a99580961608fd1ac6aa1309da923648d3ea43e97a4c1e8d666`
- `scratchpad/p42/src/Boundaries.lean`（P43），sha256 `42020742b2da0a490c9269431d1663efc9085cd48921906433fac9b6cdc2b942`
- 应协调者要求追加 / added at the coordinator's request: `scratchpad/p42/ext/P43Ext.lean`，sha256 `331ca5a63a36104c51ef38a330c3ec943b6776cabffe829c1d413f4a21fcc156`

本审查只在 `review/` 下建文件。没有修改仓库，没有运行 make 目标或检查器，没有改变 git 状态。/ Only files under `review/` were created. The repository, its git state and its checkers were not touched.

## English summary

**Formal status.**
- Lean 4.29.1 (`f72c35b3`). The scratch build's sources are byte-identical to the files under review, and the core modules they use match the repository.
- An audit of every declaration gives empty axiom reports: 229 in Feedback, 39 in Boundaries and 14 in the extension (ten theorems).
- Each theorem proves what its own docstring states, except the local points in corrections 3, 5, 11 and 14.
- The problems lie in the module-level prose, the AI readings and the framing, not in the proofs.
- All 142 probe declarations are free of axioms, and no probe uses classical reasoning.

**Verdicts.**

| Question | Verdict |
|---|---|
| 1. Correspondence | **Accept with narrowed scope.** The Lean is correct; the prose claims more than the theorems at the points in §7. |
| 2. P42 | **`verdict_within_reach`: accept.** It is a genuine locality theorem, and a stronger form is checked (B1).<br>**The ¬-form of adding: accept with narrowed scope.** The positive form holds where significance is decidable (B2).<br>**`Reaches`: accept** for the comparison that holds the rest of the exchange fixed. It ignores the order of steps (C4) and counts direct effects only (C1).<br>**"Feedback registers only the influence closure": accept as an upper bound only** (F2).<br>**The system as Ren's "the system that one is in": reject** (F1). |
| 3. P43 | **The reduction: accept as an exact decomposition that locates the step; reject as a reduction to weaker or independently held premises** (F6).<br>**Super- and sub-truth: accept with terminology corrections** (F8).<br>**The two-scope claim: accept.**<br>**The witnesses: accept.**<br>**The rivals: accept for the vague self as worded; reject for the closure rival.** Under the module's own boundaries, the closure rival denies sub-truth or invariance, not covering. P7 is not located (F9). |
| 4. Conduct within the system | **Accept with narrowed scope.** The claim covers parts wholly within the system whose levels without them exist, in the fixed-rest comparison. Where the system is the whole, the premise is the axiom at that standpoint. |
| 5. Readings of Ren | **Mixed:** two plausible, two contestable and five overreaching (§5). |
| 6. Names and stronger results | Stronger or sharper theorems are checked in nine groups (A1–A4, B1–B5). Five names should change. |
| Extension | **(1) Accept.**<br>**(2) Accept the theorem and correct its heading.** Record that the step is boundary neutrality at each standpoint (P39's reading of the axiom) and N_std across standpoints.<br>**(3) Accept the theorem; reject** the reading "Ren's highly entangled system" and the "no invariance" framing.<br>**(4) Reject the inference:** the conclusion holds only for parts within the system.<br>The plan places `Clearing.system_whole` in Feedback, which does not compile; the split in `merge_ext.py` does. |

**Top findings.**
1. **(乙) The system is the whole wherever one condition is shared by all.**
   - One condition in which every formation takes part makes every system the whole (A1 `system_whole_of_commons`).
   - Co-dependence on a condition that nothing exchanges with is enough to put two formations in one system (A1 `Static`).
   - In `Clearing` every system is the whole (A1; extension `Clearing.system_whole`).
   - Systems are equivalence classes: they partition the formations, with no nesting and no center. Ren speaks of "system and subsystem" and asks "where is this system centered".
   - Where the system is the whole, the self drawn along sharing a condition has one admissible boundary, the whole (A1 `only_whole`). The presupposition is then the axiom at that standpoint, and "the weaker version gives the whole's verdict" holds only because this reading has put the whole into the weaker version.
   - A centered, nested middle level is checked: the reach closure, what a center's exchanges affect, link by link (B3, B5). In `Clearing` it is {clearer, dweller}. Significance over it is not the axiom, yet it gives the axiom's verdict on the clearer's own part.
   - The reach closure is forward-directed. It omits the source that the clearer depends on, so it does not hold the feeding closure (B5).
2. **(乙) The reduction is a decomposition.**
   - Where the whole is admissible, invariance is exactly the conditional from the presupposition to the axiom at that standpoint (A2 `boundaryInvariant_iff_conditional`). Equivalently, it is the determinacy of the presupposition (A2).
   - Given the presupposition, invariance at a standpoint is the axiom there, which P39 already reads as boundary neutrality (`one-axiom-yields-g0`).
   - With the presupposition at every standpoint and centers covering, invariance everywhere is standpoint invariance, N_std's rule (extension `boundaryInvariant_iff_standpointInvariant`).
   - The premises therefore carry two existing decompositions to the significance of continuation: `Valuation.significant_iff` (a seed, N_rel and N_std on a connected whole) and `Valuation.significant_iff_held` (S0 at every standpoint with N_std).
   - The claim that agreement between standpoints is "derived, not assumed" must be withdrawn.
   - Invariance runs downward as readily as upward (A2 `invariance_levels_down`). This is the parity the earlier review's P3 found in tolerance.
3. **(甲) Two counterfactuals.** The influence closure is motivated by mediated influence: wolves protect a forest through the deer. Every verdict and registration theorem, however, uses the comparison that holds all other exchange fixed.
   - Under that comparison the wolves' part does not reach the forest and never registers on it. It narrows: it loses the deer (C1 `protection_invisible`).
   - Against the responsive flow that the module itself supplies, the same part is mixed (C1 `responsive_mixed`).
   - Where a part gives what others take, the comparison may not exist. In `Clearing` there are no levels without the source (C2).
4. **(乙/丙) "Every act within that system".**
   - The claim fails for a part that joins a formation with one beyond its system (C1 `mixed_part`).
   - It gives no verdict where the levels without the part do not exist (C2), and it does not see responses (C1).
   - The sentence "misjudges its own acts exactly where they reach beyond that closure" has a counterexample (C3).

**What survives.** All the Lean survives.
- `verdict_within_reach` is a real result. The verdict on a part needs significance only over what the part reaches. Under the fixed-rest comparison the reach is the right scope, apart from timing (B4).
- The four closures survive, each inclusion with a witness that it can be strict.
- The two-scope observation is correct and illuminating.
  - Route (b) is the significance of what lies definitely within the self: the supervaluation operator at narrow scope, on membership. It is also the least significance that makes every presupposition sub-true.
  - The axiom is the presupposition held definitely: the operator at wide scope.
- P43 states the decomposition as an equivalence ("exactly"). The extension's claim (1) is right: the decomposition locates the step and does not weaken the axiom.

**Top corrections** (§7, in order of severity):
1. Withdraw the reading of the system as Ren's middle level, or state its collapse. Offer the reach closure pending Ren, stating that it is forward-directed, and reconcile with P40's reading.
2. State the weaker-version claim with its exact scope.
3. Call the reduction a decomposition and add `boundaryInvariant_iff_conditional`. Withdraw "derived, not assumed". Cite the reuse of `Valuation.significant_iff`, `Valuation.significant_iff_held` and P39's boundary-neutrality reading.
4. Disclose the two counterfactuals, with the wolves and source witnesses.
5. Correct the extension's headings and claims (2)–(4), and split `Clearing.system_whole` as `merge_ext.py` does.
6. Relocate the rivals.
7. Correct the attributions to Ren.

---

## 0. 范围与方法 / Scope and method

全文阅读两个模块与扩展。另读了：
- 它们所用的核心：`Significance`、`Interdependence`、`Admission`、`Regions`、`Continuation`（`Clearing`）、`Standpoints`（`FedBy`、`significant_iff_held`）、`Metaethics`（`Neutral`、`Valuation.shares`、`significant_iff`）；
- Ren 10 月 10 日的原话记录（含 `structural-names`、`zero-axiom-part-and-names`）；
- 此前的独立审查 `EVALUATOR-GROUNDING-REVIEW.md`、其论证与记录 `self-good-reachable-g0`；
- 被复用的记录：`one-axiom-yields-g0`、`held-lives-g0-is-centering`、`feeding-closure`、`closure-verdict-meets-axiom`、`metaethical-core-characterization`；
- HEAD 版章节 §6.7–§6.9。

超赋值论与亚赋值论（Fine 1975；Hyde 1997）、营养级联只依据**先前知识**，没有重读原文。

I read both modules and the extension in full. I also read:
- the core modules they use;
- Ren's records of 10 October, including the two naming records;
- the earlier review, with its argument and record;
- the records that P42–P43 reuse;
- chapter §6.7–§6.9 at HEAD.

Fine 1975, Hyde 1997 and the trophic-cascade literature are cited from prior knowledge, not re-read.

**分类 / Classification**（同此前审查 / as in the earlier review）：
- (甲) 表示省略了某一关系 / a relationship omitted by the representation；
- (乙) 重构论证中未解决的推论 / an unresolved inference；
- (丙) 满足所述条件的真实反例 / a genuine counterexample satisfying the stated conditions。

## 1. 形式复核 / Formal recheck

- 构建中的 `Feedback.lean`、`Boundaries.lean` 与被审文件逐字节相同。`Significance`、`Interdependence`、`Admission`、`Regions`、`Continuation`、`Standpoints`、`Metaethics`、`Flow` 与仓库核心相同。
- 公理审计（`probes/Audit.lean`，用 `Lean.collectAxioms` 遍历两个模块的全部常量）：`Becoming.Feedback` 229 个声明、`Becoming.Boundaries` 39 个，均无公理。
- 扩展副本 `probes/P43Ext_copy.lean` 编译通过，十个定理的 `#print axioms` 均无依赖；连同辅助声明共 14 个，0 个有公理。
- 探针：`ProbeA` 24 个声明、`ProbeB` 44 个、`ProbeC` 74 个，共 142 个，均无公理（`probes/namespace-audit/`）。全部是项证明，没有一个探针用到经典推理，所以每一个建议的新定理都可以进纯核心。
- 输出原样存于 `probes/*.out.txt` 与 `probes/namespace-audit/*.out.txt`。合并位置的检查在 `probes/merge-check/`（§6）。

In English:
- The build's sources are byte-identical to the files under review and to the repository core.
- All 268 module declarations have empty axiom reports, as do the extension's 14 declarations and the 142 probe declarations.
- The probes are all term-mode and use no classical reasoning.

运行方式 / How run: `cd work_p36 && LEAN_PATH=work_p36 lean review/probes/<file>.lean`。不用 `-o`，不写入构建。/ No `-o`; nothing is written to the build.

## 2. P42：反馈与所及 / Feedback and reach

### F1（乙，重大）把系统读作 Ren 的中间层级，中间层级坍缩为整体 / Reading the system as Ren's middle level collapses it into the whole

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

In English:

`Flow.Shares` ignores time and direction and is met by mere co-dependence, and `Flow.WithinSystem` is an equivalence class. Hence:
- **One commons.** One condition in which everything takes part makes every system the whole (A1). A shared atmosphere suffices, however weak the coupling and at whatever step.
- **Co-dependence.** Two formations that merely depend on a condition nobody exchanges with share a system without affecting each other (A1 `Static`).
- **`Clearing`.** Every system is the whole, so `Clearing.levels` and `Clearing.system_counts_dweller` cannot separate the system level from the whole: there, significance bounded by the system is the axiom. Only `Protection`'s isolated far formation separates the two levels.
- **A partition.** Systems partition the formations, with no nesting and no center, whereas Ren's "system and subsystem" and "where is this system centered" ask for both. The question Ren answered used a tumour (the AI's passage). A tumour's system is naturally the body; under `Shares` it is everything that shares any condition with it.
- **One boundary.** Where the system is the whole, the self drawn along sharing a condition has one admissible boundary, the whole (`only_whole`). Its presupposition is then the axiom at that standpoint, as the extension's own docstring says: "the weaker version is the axiom".

The reach closure (B3) is centered and nested.
- In `Clearing` it is strictly smaller than the system (B5).
- On a premise weaker than the system's, it gives the axiom's verdict on every part within it.
- It is forward-directed. It omits the source that the clearer depends on, so on that reading the order of readings runs down to the bare self, not to the feeding closure. Whether this direction fits is for Ren.

If the intent is that in an entangled world the system one is in is the whole, the text should say that the weaker version then coincides with the axiom, and the formal condition should measure coupling rather than one shared condition.

P40, P42 and P43 read three different closures as Ren's levels; they must be reconciled.

### F2（甲，重大）两种反事实：影响闭包与判断所用的比较不一致 / Two counterfactuals: the influence closure and the comparison used for verdicts

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

In English, the influence closure is grounded in mediated influence, but every verdict and registration theorem holds all other exchange fixed. Under that comparison:
- **The wolves.** The wolves' part does not reach the forest and never registers on it. It narrows: it loses the deer (C1 `protection_invisible`).
- **The responsive flow.** Against the responsive flow that the module itself supplies, the same part is mixed: with the wolves the forest is admitted at step 2 (counting from 0), and without them the deer at step 1 (C1 `responsive_mixed`). So the verdict's category depends on the counterfactual.
- **The source.** Withholding a part that gives what others take may leave no levels at all (C2), and then no verdict exists.
- **Direct reach.** A formation's support registers only the parts that reach it directly (`admits_unreached`). The influence closure is the scope of registration only in a comparison where others respond, and that comparison is not yet built.
- **Acts and parts.** `Clearing.unregistered` compares an act through a separate flow. The verdict machinery works on decided families of formations and cannot isolate one act of a formation.

### F3（甲，次要）`AffectedBy`、`Reaches`、`Shares` 不看步的次序 / The relations ignore the order of steps

`AffectedBy g h` 只要求 g 在某一步依存于 c，h 在某一步与 c 交换；交换可以晚于依存。

C4 `Late.affected_without_effect` 是一个见证：
- `false` 只在第 1 步交换，`true` 只在第 0 步依存；
- 于是 `true` 被影响、被到达，但每一步有无该部分都一样被接纳。

这些关系都是正确的上界，不是影响本身。精确化已检查：水平不同之处，必有成员在**此前**某步交换过（B4 `exchanges_before_of_differs`）。所以可以定义按时间排序的所及，进而得到前向的“光锥”闭包。

The relations allow the exchange to come after the dependence (C4). They are sound upper bounds, not influence itself. A step-ordered sharpening is checked (B4): where the levels differ at `t`, some member exchanged before `t`.

### F4（乙/甲，中等）判断定理本身 / The verdict theorem itself

- **正确的推进。** `Flow.Balances.verdict_within_reach` 正确。它从动力学推出了 `Web.retains_bounded_iff_includes` 所需的覆盖条件：未被到达者有无该部分都一样被接纳。这是 P40 记录 `closure-verdict-meets-axiom` 的真实推进。
- **更强的形式。** 两个意义只要在部分所及之处一致，四个判断就相同（B1 `verdict_local`）。原定理是其中一个取公理时的特例。“the verdict on a part is decided within what it reaches” 精确说的正是 B1。
- **增加判断的形式。** “neither adds exactly where neither exceeds” 足以判断不增加，不足以确证增加。
  - 在意义可判定处，正面形式可构造地推出（B2 `adds_iff_exceeds_of_decidable`）；一般只到双重否定（B2 `not_not_adds_of_exceeds`）。
  - 所以“What is not derived”中这一条应改写：缺的只是可判定性，可以作为假设陈述，而不是不可推出。
- **只有保留。** `Flow.Balances.system_retains_iff` 只给出保留，不给出增加。公理在其中只用来把包含改写为公理的保留。

In English:
- `verdict_within_reach` is correct. It advances P40's `Web.retains_bounded_iff_includes` by deriving that theorem's cover condition from the dynamics.
- Its stronger form holds (B1): significances that agree on the reach give the same four verdicts.
- The adding verdicts hold in positive form where significance is decidable (B2), and otherwise only up to double negation. The note should say so, rather than that they are not derived.
- `system_retains_iff` covers retaining only, and its axiom hypothesis serves only to rewrite inclusion.

### F5（丙，次要）“恰在其行为到达闭包之外处误判” / "Misjudges ... exactly where they reach beyond that closure"

C3 `Margin.reach_without_misjudgment` 是反例：
- 行动者的部分到达影响闭包之外的形成；
- 但有该部分时的水平包含无它时的水平，所以任何意义都保留；
- 于是以影响闭包为界的意义与公理判断相同。

已证的说法是：其行为只到达闭包之内时，判断与公理相同（B1 `verdict_local`）；到达之外时可能误判，而到达之外本身并不足以误判（C3）。

C3: a part reaches beyond its center's influence closure yet changes no admission there, so every significance retains. What is proved is narrower. Such a center judges its own acts as the axiom does wherever they reach only within the closure (B1). Beyond the closure it can misjudge them, but reaching beyond does not suffice (C3).

## 3. P43：边界 / Boundaries

### F6（乙，重大）“三前提推出公理”是分解，不是化约 / The reduction is a decomposition

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

In English:
- **Invariance as the conditional.** Invariance is exactly the conditional from the presupposition to the axiom at that standpoint (A2). Equivalently, it is the determinacy of the presupposition. The decomposition has the form A ⇔ B ∧ (B → A).
- **At one standpoint.** Given the presupposition, invariance is the axiom at that standpoint, which P39 already reads as boundary neutrality.
- **Across standpoints.** With the presupposition everywhere and centers covering, invariance at every standpoint is standpoint invariance, N_std's rule (extension).
- **Sub-truth carries transmission.** Sub-truth along a relation carries the seed and transmission along that relation, from bare S0 (the empty relation) to the axiom (the total relation).
- **Reuse.** The premises carry the decompositions of `Valuation.significant_iff` and `Valuation.significant_iff_held` to the significance of continuation, and the record must cite that reuse.
- **Withdraw.** "Derived, not assumed" must go.
- **Downward.** Invariance runs downward as readily as upward (A2): the P3 parity.
- **Tolerance.** Invariance replaces tolerance, carrying the same load without tolerance's small-step motivation.

### F7（乙，中等）覆盖由可容许类构造进去 / Covering is built into the admissible class

沿一个关系，凡含中心、对关系封闭的区域都算自我的可容许边界，整体也在其中（`Boundary.whole`），所以覆盖自动成立（`subTrue_member`）。

“Boundaries closed along a relation meet it without further premise, since the whole is one” 形式上为真。但实质前提就在可容许类的选择里：这一选择让任何形成都不是任何自我的明确非成员。

Along a relation every closed region holding the center, the whole included, is admissible, so covering holds by construction. The substantive premise is that choice of class, under which nothing is a clear non-member of any self.

### F8（乙，中等）超真与下真 / Super-truth and sub-truth

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

In English:
- **Structure.** The structure is right, and `superTrue_member_iff` is "definitely within the self".
- **Terms.** "Super-true" is Fine's (1975) term; "sub-true" is subvaluationist (Hyde 1997), not Fine's. The module cites neither.
- **Not a supervaluation of the self.** The admissible class has no clear non-members, so it is not a supervaluation of the ordinary vague "self".
- **Invariance is determinacy.** Assuming invariance assumes that the presupposition has no penumbra, which a supervaluationist about the self would deny.
- **The two scopes.** The claim is correct. Route (b) puts the "definitely" operator at narrow scope and the axiom puts it at wide scope; the operator does not distribute over the conditional.

### F9（乙，中等）对手的位置 / Where the rivals sit

模块说：闭合坐标对手（此前审查 P5）与模糊自我否认覆盖。沿一个关系，覆盖自动成立，所以这些对手否认的是另一个前提：
- **P5 闭合对手**把意义建立在已形成的闭合上。
  - 沿一个该闭合不对之封闭的关系，它否认下真。例如操作闭合不对供给封闭：有机体由其外者供给，而 `subTrue_selfSignificant_iff` 要求整个闭包都有意义。
  - 沿一个该闭合对之封闭的关系，它只在该闭合处持有预设，否认不变性，正如路线 (b) 在供给闭包处（`Clearing.without_invariance`）。
  - 只有同时把可容许的画法限于该闭合时，它才否认覆盖（`Clearing.with_fixed_boundary`）。
- **模糊自我**：每个可容许画法都把陌生人排除在外时，否认覆盖，这是模块所述的情形；陌生人在边缘时，预设不确定，否认的是不变性（A2 `boundaryInvariant_iff_determinate`）。
- **P7 在有限距离处归零的分级权重**：权重在闭包内归零时，否认沿该关系的下真；在闭包外归零时，否认不变性；都不是否认覆盖。模块没有给它定位。
- **认知主义的清晰未知断点**：可容许类是单元集，否认覆盖，除非断点就是整体。
- **现时目的评价者**否认下真。

In English: along a relation covering holds by construction, so these rivals deny another premise.
- **The closure rival (P5).** It denies sub-truth along a relation under which its closure is not closed: operational closure is not closed under feeding. Along a relation under which its closure is closed, it denies invariance, as route (b) does at the feeding closure. It denies covering only if it also restricts the admissible drawings to its closure.
- **The vague self.** It denies covering as the module words it, when every admissible drawing leaves the stranger out. It denies invariance when the stranger is borderline.
- **P7.** It denies sub-truth if its weight vanishes inside the closure, and invariance if the weight vanishes beyond it. The module does not locate P7.

### F10（乙，次要）层级次序没有定理 / The order of levels has no theorem

“super-true, sub-true along sharing a condition, and sub-true at the self's dependence” 这一次序可由 `Boundary.of_larger` 得到一串蕴涵，已检查（A3 `presupposition_levels`）：超真 → 沿共享下真 → 沿受影响下真 → 沿供给下真。

但在 `Clearing` 中前两者重合（系统即整体），模块的见证分不开它们。另外，这里把 Ren 的“the self”读作供给闭包；赤裸的自我是空关系（A2 `subTrue_empty_iff`）。

The order follows from `Boundary.of_larger` (A3), but in `Clearing` its first two readings coincide. The reading maps Ren's "the self" to the feeding closure; the bare self is the empty relation (A2).

## 4. 系统内的行为 / Conduct within the system

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

In English, the result is true in the representation for parts wholly within the center's system, and it depends on items 1–7 above. Beyond the representation:
- **Responses.** A comparison in which others respond can make withholding a part create exchanges with conditions never touched in the actual flow. Formations outside the actual system can then be reached (甲, not formalized).
- **"The whole need not be admissible".** This misleads: along sharing a condition the whole is always admissible. What is meant is that neither invariance nor super-truth is used.

## 5. Ren 的原话与 AI 的读法 / Ren's words and the AI's readings

| 读法 / Reading | 评估 / Assessment |
|---|---|
| 影响闭包读“自身反馈能登记的”/ the influence closure as what feedback can register | **可信**，须附 F2 的说明。/ **Plausible**, with F2's disclosure. |
| “still need situational awareness”读作“须知道反馈之外” / read as knowing beyond one's feedback | **可信**，是 AI 的推衍；Ren 的括注附在“full truth set”上。/ **Plausible** AI elaboration; Ren's parenthesis qualifies "the full truth set". |
| 系统读“the system that one is in” / the system as "the system that one is in" | **过度**：使中间层级成为整体，与 Ren 的“system and subsystem”与“where is this system centered”不合（F1）。/ **Overreaching** (F1). |
| “weaker version”给出整体对系统内每一行为的判断 / gives the whole's verdict on every act within the system | **过度**：范围见 §4；系统即整体时，它的前提就是该立场上的公理。/ **Overreaching**; see §4. Where the system is the whole, its premise is the axiom at that standpoint. |
| 预设读 Ren 的“belief” / the presupposition as Ren's "belief" | **可争议**：Ren 说自我“can not justify itself without some sort of "belief"”，是在说明自我层最弱；把这一信念当作被授予的前提，是 AI 的一步。沿关系的下真也远强于“某一延续有意义”。/ **Contestable**: Ren wrote it of the self's limit. Using it as a premise is the AI's step, and sub-truth along a relation is far stronger than "some continuation matters". |
| 覆盖读“There is no absolute self”与“the universe/ecosystem that realizes its own existence” / covering as these two lines | **可争议**：后一句支持整体是“我们”的一种画法；前一句本身推不出覆盖；实质在可容许类（F7）。/ **Contestable**: the second line supports the whole as a drawing of "we"; the first does not imply covering; the substance is the admissible class. |
| 不变性读“universal invariations”“for all beings” / invariance as Ren's invariances | **过度**：Ren 的不变性是“for every universe, becoming happens, the law follows”，即法则在各宇宙中的不变。“for all beings”最直接的形式是立场不变（N_std）；扩展已证，在给定前提下它与边界不变等价。/ **Overreaching**: Ren's invariances are invariances of the law across universes. "For all beings" reads most directly as standpoint invariance. |
| “three claims Ren holds” | **过度**：这是助手在 AI 所写语境中的提议。Ren 的“i think you see the right direction”在记录中仍作待定读法。“every act presupposes that some continuation matters”不是 Ren 的话。/ **Overreaching attribution.** |
| 扩展：系统即整体读“Ren's highly entangled system” / the extension: system = whole as "Ren's highly entangled system" | **过度**：Ren 说的是“at this moment in time, the whole earth has become a highly entangled system, everyone country, every person, is heavily coupled into it”，是关于当下耦合强度的历史判断。形式条件是布尔的、不看时间，在有一个公共条件的任何世界、任何时代都成立（A1）。/ **Overreaching**: Ren's claim is about present coupling strength; the formal condition holds in any world with one commons. |

“the continuation goes beyond one's cycle of life, goes beyond one's death” 没有被用到；它更自然地支持按谱系个体化与按时间排序的所及（B4）。/ Ren's line on continuation beyond death is unused. It bears on individuating by lineage and on step-ordered reach (B4).

## 6. 扩展 `P43Ext.lean` / The extension

十个定理全部正确，且无公理。/ All ten theorems are correct and axiom-free.

- **主张 (1)：接受。** `boundaryInvariant_iff_all` 正确。建议同时给出不带前提的 `boundaryInvariant_iff_conditional` 与 `invariance_levels_down`（A2），后者显示这一步可以双向走。/ **Accept.** Add the unconditional form and the downward direction.
- **主张 (2)：接受定理，更正标题。**
  - “The two forms of the step are one”过度：没有处处的预设时，两者分开（A4 `forms_apart`：一个处处相同的意义满足立场不变，却不满足边界不变）。
  - 两者在所给前提下等价，是因为二者那时都等价于公理。
  - 应明说：边界不变在单个立场上就是边界中立（P39 对公理的读法）；`StandpointInvariant` 就是 N_std 的规则用于延续的意义。
  - `unrestricted_of_standpointInvariant` 与 §6.7 的结构同形：每个中心的 S0 加 N_std（`Valuation.significant_iff_held`、`Web.significant_iff_self`）。
  - 并撤回 P43 的“derived, not assumed”。

  / **Accept the theorem.** Without the presupposition everywhere, the two forms differ (A4). They coincide under the stated premises because each is then the axiom. State that the step is boundary neutrality at one standpoint and N_std across standpoints, and withdraw "derived, not assumed".
- **主张 (3)：接受定理，拒绝读法与“no invariance”的说法。**
  - 闭包是整体时，整体是唯一的可容许边界（A1 `only_whole`），所以不变性平凡成立，正如 `Clearing.with_fixed_boundary` 中单一边界的情形。
  - 这一步没有被去掉，而是放进了“边界对共享条件封闭”的要求。
  - `unrestricted_iff_presupposed_of_whole` 的文档应写明原因；假设名 `entangled` 应改为 `connected`。

  / **Accept the theorem; reject the reading and the framing.** The whole is then the only boundary, so invariance holds trivially. The step has moved into the requirement that boundaries be closed.
- **主张 (4)：拒绝其推论。**
  - `Flow.unreached_within_system` 正确，说的是系统对外封闭：系统外的部分到达不了系统内。
  - 对自身部分的结论来自 `Flow.own_within_system` 与 `presupposed_system_verdict`，不来自它。
  - 对含系统外成员的联合部分，结论不成立（C1 `mixed_part`）。
  - 对完全在系统外的部分，以系统为界的意义判其保留，而公理可能判其失去。

  / **Reject the "so".** The theorem shows that the system is closed to what lies outside. The conclusion for one's own part follows from other theorems, and it fails for joint parts with members beyond the system (C1).
- **文档与陈述。** `Clearing.without_standpoint_invariance` 的文档比陈述多两项（预设下真、每个形成在自身闭包内）：补入合取项或删去。/ Its docstring claims two conjuncts its statement lacks.
- **合并位置 / Placement.**
  - 按所述计划把 `Clearing.system_whole` 放进 Feedback 不能编译：其第三个合取项用到 Boundaries 中的 `SubTrue`、`Boundary`、`SelfSignificant`（`merge-check/FeedbackPart.lean`：`SubTrue` 未知）。
  - `merge_ext.py` 的拆分可以编译且无公理：Feedback 留两个合取项，Boundaries 另立 `system_presupposition`（`merge-check/FeedbackPartSplit.lean`、`BoundariesPartSplit.lean`）。

  / As planned, `Clearing.system_whole` cannot go into Feedback, because its third conjunct uses Boundaries. The split in `merge_ext.py` compiles axiom-free.

## 7. 须作的更正（按严重程度）/ Required corrections, by severity

1. **系统的读法 / The reading of the system**（F1）。
   - 在 `Feedback.lean` 的 AI 读法中，把 “The system reads Ren's “the system that one is in”: everything linked to the formation through conditions in which they take part.” 改为：
     > The system is the class of formations linked through conditions in which they take part. It bounds every effect: what lies within it reaches only within it, and what lies beyond reaches nothing within it. Wherever one condition is taken part in by everything it is the whole, as in `Clearing`, so it does not read Ren's intermediate “system that one is in”. For that reading the reach closure is offered, pending Ren: what a center's exchanges affect, link by link (`Flow.WithinReach`). It is centered and nested, lies within the system, and need not hold the center's feeding closure.
   - 加入 B3、B5 的定理（`Flow.WithinReach`、`Flow.reaches_withinReach`、`Flow.withinSystem_of_withinReach`、`Flow.Balances.presupposed_reach_verdict`、`Flow.subTrue_affects_of_shares`、`ClearingReach.reach_counts_dweller` 等；并入时后者可放在 `Clearing` 下）。
   - 加入 A1 的 `system_whole_of_commons`、`only_whole` 与扩展的 `Clearing.system_whole`。
   - 在 `Interdependence.lean` 的读法与章节 §6.9 中，撤回或标注“供给闭包也读 the system that one is in”。
2. **较弱版本 / The weaker version**（§4）。
   - 把 “Ren's weaker version, “within the system that one is in”, gives the whole's verdict on every act within that system.” 改为：
     > Significance that covers a center's system gives the axiom's verdicts on every part whose members all lie within that system and whose levels without it exist, in the comparison that holds the rest of the exchange fixed. Where the system is the whole, that significance is the axiom at the center's standpoint.
   - `Boundaries.lean` 的 “The weaker version gives the whole's verdict on conduct within one's system.” 作同样的限定。
3. **分解，不是化约 / A decomposition, not a reduction**（F6）。
   - 标题 “The axiom from three premises” 改为 “The axiom decomposed: where its content lies”。
   - 加入 `boundaryInvariant_iff_conditional`、`invariance_levels_down`、`boundaryInvariant_iff_determinate`，以及扩展的 `boundaryInvariant_iff_all`，并写：
     > Invariance is the conditional from the presupposition to the axiom at that standpoint; given the presupposition, it is the axiom there. The decomposition locates the step and does not lower the axiom's content. It runs both ways: where some continuation lacks significance, an invariant presupposition is nowhere true.
   - 把 “Agreement between standpoints is then derived, not assumed” 改为：
     > Agreement between standpoints follows. Given the presupposition at every standpoint and covering by centers, invariance is equivalent to standpoint invariance, the rule of N_std (`boundaryInvariant_iff_standpointInvariant`).
   - 加一段复用说明：
     > Given the presupposition, invariance at a standpoint is the axiom there, which P39 reads as boundary neutrality. The premises carry the decompositions of `Valuation.significant_iff` (a seed, N_rel and N_std on a connected whole) and `Valuation.significant_iff_held` (S0 at every standpoint with N_std) to the significance of continuation.
   - 把 “It takes the place of the earlier route's tolerance” 补为：
     > ... and, like tolerance with Chain, it carries all of the axiom's content beyond the presupposition.
4. **两种反事实 / Two counterfactuals**（F2）。
   - 在两个模块的表示说明中加入：
     > The verdicts compare the levels without a part with every other exchange held fixed, so they register only a part's direct exchanges, and a formation's support registers only the parts that reach it (`Flow.Balances.admits_unreached`). Mediated effects, such as the wolves' protection of the forest through the deer, appear only in a comparison where others respond. With the rest fixed, the wolves' part narrows and does not reach the forest; against the responsive flow it is mixed. Where a part gives what others take, the levels without it may not exist, and no verdict is given.
   - 把 C1 `protection_invisible`、`responsive_mixed` 与 C2 `no_levels_without_source` 作为见证加入。
   - 在 “The influence closure reads what a formation's own feedback can register” 后加：“once effects pass through the support and activity of others”。
5. **扩展 / The extension**（§6）。
   - 标题 “The two forms of the step are one” 改为：
     > Given the presupposition and centers covering, the two forms of the step are equivalent: each is then the axiom.
   - `unrestricted_iff_presupposed_of_whole` 的文档加：“because the whole is then the only boundary”。
   - 不把 `Flow.unrestricted_iff_system_presupposed` 读作 Ren 的 “highly entangled system”。
   - 主张 (4) 改为：
     > What lies within a system reaches only within it, and what lies beyond reaches nothing within it.
   - `without_standpoint_invariance` 的文档与陈述对齐。
   - 按 `merge_ext.py` 的方式拆分 `Clearing.system_whole`。
6. **对手的位置 / Rivals**（F9）。把 “A rival that grounds the self in a formed closure, such as operational closure, denies it, and so does a vague self whose every admissible drawing leaves the stranger out.” 改为：
   > Along a relation, covering holds by construction, so these rivals deny another premise. A rival that grounds significance in a formed closure denies sub-truth along any relation under which that closure is not closed, as operational closure is not closed under feeding. Along a relation under which it is closed, it denies invariance: it holds its presupposition only at that closure, as route (b) does at the feeding closure. It denies covering only if it also restricts the admissible drawings to that closure. A vague self denies covering where every admissible drawing leaves the stranger out, and invariance where the stranger is borderline. A graded weight that falls to zero denies sub-truth if it falls inside the closure, and invariance if beyond it. A present-aim evaluator denies sub-truth.
7. **对 Ren 的归属 / Attributions to Ren**（§5）。
   - “three claims Ren holds” 改为 “three claims the assistant read from Ren's words”。
   - 不变性一条改为：
     > Ren's “for all beings” reads most directly as standpoint invariance, the rule of N_std; given the presupposition and covering, boundary-invariance is equivalent to it. Ren's “universal invariations” are invariances of the law across universes; extending them to significance is the AI's reading.
   - 预设一条加：
     > Ren wrote this of the self's limit; using the belief as a premise is the AI's step.
8. **覆盖 / Covering**（F7）。把 “Boundaries closed along a relation meet it without further premise, since the whole is one.” 改为：
   > Along a relation, covering holds because every closed region holding the center, the whole included, counts as an admissible drawing of the self. That admissibility is the substantive choice.
9. **超赋值术语 / Supervaluation terms**（F8）。
   - 模块或记录若引文献，注明 super-truth 取自 Fine 1975、sub-truth 取自亚赋值论（Hyde 1997）。
   - 注明本模块的可容许类没有明确的非成员，以及不变性就是确定性。
   - 把两种辖域写成一个定理。
10. **层级次序 / Order of levels**（F10）。加入 `presupposition_levels`，并写明在 `Clearing` 中前两种读法重合。
11. **“the whole need not be admissible”**。在 `Flow.Balances.presupposed_system_verdict` 的文档与模块说明中，把 “No invariance is used, and the whole need not be admissible.” 改为：
    > Neither invariance nor super-truth is used.
12. **误判的说法 / The misjudging sentence**（F5）。把 “A center that values only what its feedback registers misjudges its own acts exactly where they reach beyond that closure, as the clearer does.” 改为：
    > A center that values only what its feedback registers judges its own acts as the axiom does wherever they reach only within that closure (`verdict_local`). Where they reach beyond it, it can misjudge them, as the clearer does; reaching beyond does not by itself make it misjudge (`Margin`).
13. **正面的增加判断 / Positive adding verdicts**（F4）。
    - 把 “What is not derived” 中 “the adding verdicts in positive form: the core is constructive, so they are stated as “neither adds exactly where neither exceeds”.” 改为：
      > the adding verdicts in positive form for every significance. They are stated as “neither adds exactly where neither exceeds”; they hold in positive form where significance is decidable (`adds_iff_exceeds_of_decidable`), and in general up to double negation (`not_not_adds_of_exceeds`).
    - 并加入这两个定理与 `verdict_local`。
14. **局部的文档与陈述 / Local docstrings**。
    - `system_retains_iff` 的文档与 Feedback 模块说明中，“judges what is done within it as the axiom does”（及 “judges every part within that system as the axiom does”）改为：
      > retains along every part within it exactly where the axiom's significance does
    - Boundaries 模块说明中，“Drawn at the feeding closure, it licenses the part” 改为：
      > Drawn at the feeding closure, it is met by a significance under which the part retains

      这与定理自己的文档一致。
    - `Boundaries` 的 “What is not derived” 加：
      > the presupposition itself, which is supplied as every significance is (`Web.significance_undetermined`); along a relation it already carries transmission along that relation, from the bare S0 of the empty relation to the axiom of the total one
    - 模块说明中 `superTrue_all_iff` 补上 “where the whole is admissible”。
15. **记录与复用 / Records and reuse**。
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
    - “conduct”改为 “a part's exchange”。
    - 假设名 `entangled` 改为 `connected`。

## 8. 探针 / Probes

文件 / Files：
- `review/probes/ProbeA.lean`（sha256 `8a0dafae…6fd70`）、`ProbeB.lean`（`385048b1…3810b`）、`ProbeC.lean`（`61cb618e…1752e`）；
- `Audit.lean`：两个模块的公理审计；
- `P43Ext_copy.lean`：扩展的逐字副本加 `#print axioms`；
- `namespace-audit/`：每个探针文件全部局部声明的审计，结果为 A 24、B 44、C 74、扩展 14 个声明，0 个有公理；
- `merge-check/`：合并位置的检查（§6）；
- 输出：`*.out.txt`。

全部是项证明，`#print axioms` 均为 “does not depend on any axioms”。/ All are term-mode, and every `#print axioms` reports no axioms.

| 编号 / Id | 定理 / Theorem（`Becoming.ReviewP42.` 下） | 显示 / Shows |
|---|---|---|
| A1 | `system_whole_of_commons`, `only_whole`, `clearing_clearer_system`, `clearing_subTrue_shares_iff`, `Static.shares_unaffected` | 一个公共条件即使系统为整体；系统为整体时唯一边界是整体；`Clearing` 中沿共享下真即公理；共同依存而不交换也同属一系统 / One commons makes the system the whole; then the whole is the only boundary; co-dependence suffices. |
| A2 | `boundaryInvariant_iff_conditional`, `invariance_levels_down`, `boundaryInvariant_iff_determinate`, `subTrue_total_iff`, `subTrue_empty_iff` | 不变性即条件句、即确定性，并可向下传递；预设的强度由关系决定 / Invariance is the conditional and determinacy, and runs downward; the relation sets the strength. |
| A3 | `subTrue_of_larger`, `presupposition_levels` | 层级次序作为蕴涵 / The order of levels as implications. |
| A4 | `forms_apart` | 没有处处的预设时两种不变性分开 / The two invariances differ without the presupposition everywhere. |
| B1 | `Flow.Balances.verdict_local` | 在所及处一致即判断相同 / Agreement on the reach decides the verdict. |
| B2 | `Flow.Balances.adds_iff_exceeds_of_decidable`, `Flow.Balances.not_not_adds_of_exceeds` | 正面的增加判断 / Positive adding verdicts. |
| B3 | `Flow.Affects`, `Flow.WithinReach`, `Flow.reaches_withinReach`, `Flow.withinSystem_of_withinReach`, `Flow.Balances.presupposed_reach_verdict`, `Flow.subTrue_affects_of_shares` | 所及闭包：居中、可嵌套、前提更弱 / The reach closure: centered, nested, on a weaker premise. |
| B4 | `Flow.Balances.exchanges_before_of_differs` | 按时间排序的所及 / Step-ordered reach. |
| B5 | `ClearingReach.middle`, `ClearingReach.centred`, `ClearingReach.reach_counts_dweller` | `Clearing` 中所及闭包是真正的中间层，且不含来源 / A genuine middle level in `Clearing`, without the source. |
| C1 | `Wolves.protection_invisible`, `Wolves.responsive_mixed`, `Wolves.far_system`, `Wolves.mixed_part` | 经由他者的保护在扣留比较中看不见；判断类别随反事实而变；含系统外成员的联合部分 / Mediated protection is invisible; the verdict's category depends on the counterfactual; a mixed part. |
| C2 | `Source.no_levels_without_source` | 关键给予者没有比较 / No comparison for an essential giver. |
| C3 | `Margin.reach_without_misjudgment` | 到达闭包之外而不误判 / Reaching beyond without misjudgment. |
| C4 | `Late.affected_without_effect` | 受影响而无效果 / Affected without effect. |
| M | `merge-check/FeedbackPart.lean`（失败 / fails）, `FeedbackPartSplit.lean`, `BoundariesPartSplit.lean` | 合并位置 / Placement of `Clearing.system_whole`. |

`#print axioms` 原样输出（节选，全部同形）/ Verbatim output (an excerpt; every line has this form):

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

（倒数第三行来自 `merge-check/FeedbackPartSplit.lean`。/ The third line from the end comes from `merge-check/FeedbackPartSplit.lean`.）

注意：本版 Lean 中 `Nat.succ_ne_zero` 依赖 `propext`，带通配符的重叠模式匹配也会引入 `propext`。探针因此改用 `Nat.noConfusion` 与完整、不重叠的模式；并入核心时须照此写。/ In this Lean, `Nat.succ_ne_zero` and overlapping wildcard patterns bring in `propext`. The probes avoid both, and merged code must too.

## 9. 审查者自身的边界 / Reviewer's limits

- 探针是有限模型与一般定理，只显示所述条件下的推出或一致。对实际世界中系统是否为整体，只给出形式条件，不作经验判断。/ Probes show entailment or consistency under the stated conditions only.
- 没有重读 Fine、Hyde 或营养级联文献。/ The literature is cited from prior knowledge.
- 没有判断任一前提在规范上是否正确，只判断推论、对应、范围与读法。/ No normative verdict is given on any premise; only inference, correspondence, scope and reading are judged.
- 响应式比较下系统可能被越出（§4），只是论证草图，没有形式化。/ The point about responsive comparisons in §4 is a sketch, not formalized.
- 没有审查 `work_next/` 与 `next/` 中正在进行的合并；只检查了 `merge_ext.py` 对 `system_whole` 的放置。/ The merge in progress was not reviewed, apart from the placement of `system_whole` in `merge_ext.py`.
