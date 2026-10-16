<a id="p42p43-独立审查反馈所及与边界--independent-review-of-p42p43-feedback-reach-and-boundaries"></a>
# Independent review of P42–P43: feedback, reach and boundaries

> Some passages exist only in the [Chinese edition](BECOMING-P42-P43-REVIEW.zh.md): 87 passages in 15 sections, mainly “The extension”; “Reading the system as Ren's middle level collapses it into the whole”; “F6（乙，重大）“三前提推出公理”是分解，不是化约 / The reduction is a decomposition”; “Super-truth and sub-truth”; “Conduct within the system”.

Objects:
- `scratchpad/p42/src/Feedback.lean`（P42），sha256 `5b6ba16326ae8a99580961608fd1ac6aa1309da923648d3ea43e97a4c1e8d666`
- `scratchpad/p42/src/Boundaries.lean`（P43），sha256 `42020742b2da0a490c9269431d1663efc9085cd48921906433fac9b6cdc2b942`
- added at the coordinator's request: `scratchpad/p42/ext/P43Ext.lean`，sha256 `331ca5a63a36104c51ef38a330c3ec943b6776cabffe829c1d413f4a21fcc156`

Only files under `review/` were created. The repository, its git state and its checkers were not touched.

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

<a id="0-范围与方法--scope-and-method"></a>
## 0. Scope and method

I read both modules and the extension in full. I also read:
- the core modules they use;
- Ren's records of 10 October, including the two naming records;
- the earlier review, with its argument and record;
- the records that P42–P43 reuse;
- chapter §6.7–§6.9 at HEAD.

Fine 1975, Hyde 1997 and the trophic-cascade literature are cited from prior knowledge, not re-read.

**分类 / Classification**（同此前审查 / as in the earlier review）：
- a relationship omitted by the representation；
- an unresolved inference；
- a genuine counterexample satisfying the stated conditions。

<a id="1-形式复核--formal-recheck"></a>
## 1. Formal recheck

In English:
- The build's sources are byte-identical to the files under review and to the repository core.
- All 268 module declarations have empty axiom reports, as do the extension's 14 declarations and the 142 probe declarations.
- The probes are all term-mode and use no classical reasoning.

运行方式 / How run: `cd work_p36 && LEAN_PATH=work_p36 lean review/probes/<file>.lean`。不用 `-o`，不写入构建。/ No `-o`; nothing is written to the build.

<a id="2-p42反馈与所及--feedback-and-reach"></a>
## 2. Feedback and reach

<a id="f1乙重大把系统读作-ren-的中间层级中间层级坍缩为整体--reading-the-system-as-rens-middle-level-collapses-it-into-the-whole"></a>
### Reading the system as Ren's middle level collapses it into the whole

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

<a id="f2甲重大两种反事实影响闭包与判断所用的比较不一致--two-counterfactuals-the-influence-closure-and-the-comparison-used-for-verdicts"></a>
### Two counterfactuals: the influence closure and the comparison used for verdicts

In English, the influence closure is grounded in mediated influence, but every verdict and registration theorem holds all other exchange fixed. Under that comparison:
- **The wolves.** The wolves' part does not reach the forest and never registers on it. It narrows: it loses the deer (C1 `protection_invisible`).
- **The responsive flow.** Against the responsive flow that the module itself supplies, the same part is mixed: with the wolves the forest is admitted at step 2 (counting from 0), and without them the deer at step 1 (C1 `responsive_mixed`). So the verdict's category depends on the counterfactual.
- **The source.** Withholding a part that gives what others take may leave no levels at all (C2), and then no verdict exists.
- **Direct reach.** A formation's support registers only the parts that reach it directly (`admits_unreached`). The influence closure is the scope of registration only in a comparison where others respond, and that comparison is not yet built.
- **Acts and parts.** `Clearing.unregistered` compares an act through a separate flow. The verdict machinery works on decided families of formations and cannot isolate one act of a formation.

<a id="f3甲次要affectedbyreachesshares-不看步的次序--the-relations-ignore-the-order-of-steps"></a>
### The relations ignore the order of steps

The relations allow the exchange to come after the dependence (C4). They are sound upper bounds, not influence itself. A step-ordered sharpening is checked (B4): where the levels differ at `t`, some member exchanged before `t`.

<a id="f4乙甲中等判断定理本身--the-verdict-theorem-itself"></a>
### The verdict theorem itself

In English:
- `verdict_within_reach` is correct. It advances P40's `Web.retains_bounded_iff_includes` by deriving that theorem's cover condition from the dynamics.
- Its stronger form holds (B1): significances that agree on the reach give the same four verdicts.
- The adding verdicts hold in positive form where significance is decidable (B2), and otherwise only up to double negation. The note should say so, rather than that they are not derived.
- `system_retains_iff` covers retaining only, and its axiom hypothesis serves only to rewrite inclusion.

<a id="f5丙次要恰在其行为到达闭包之外处误判--misjudges--exactly-where-they-reach-beyond-that-closure"></a>
### "Misjudges ... exactly where they reach beyond that closure"

C3: a part reaches beyond its center's influence closure yet changes no admission there, so every significance retains. What is proved is narrower. Such a center judges its own acts as the axiom does wherever they reach only within the closure (B1). Beyond the closure it can misjudge them, but reaching beyond does not suffice (C3).

<a id="3-p43边界--boundaries"></a>
## 3. Boundaries

<a id="f6乙重大三前提推出公理是分解不是化约--the-reduction-is-a-decomposition"></a>
### The reduction is a decomposition

In English:
- **Invariance as the conditional.** Invariance is exactly the conditional from the presupposition to the axiom at that standpoint (A2). Equivalently, it is the determinacy of the presupposition. The decomposition has the form A ⇔ B ∧ (B → A).
- **At one standpoint.** Given the presupposition, invariance is the axiom at that standpoint, which P39 already reads as boundary neutrality.
- **Across standpoints.** With the presupposition everywhere and centers covering, invariance at every standpoint is standpoint invariance, N_std's rule (extension).
- **Sub-truth carries transmission.** Sub-truth along a relation carries the seed and transmission along that relation, from bare S0 (the empty relation) to the axiom (the total relation).
- **Reuse.** The premises carry the decompositions of `Valuation.significant_iff` and `Valuation.significant_iff_held` to the significance of continuation, and the record must cite that reuse.
- **Withdraw.** "Derived, not assumed" must go.
- **Downward.** Invariance runs downward as readily as upward (A2): the P3 parity.
- **Tolerance.** Invariance replaces tolerance, carrying the same load without tolerance's small-step motivation.

<a id="f7乙中等覆盖由可容许类构造进去--covering-is-built-into-the-admissible-class"></a>
### Covering is built into the admissible class

Along a relation every closed region holding the center, the whole included, is admissible, so covering holds by construction. The substantive premise is that choice of class, under which nothing is a clear non-member of any self.

<a id="f8乙中等超真与下真--super-truth-and-sub-truth"></a>
### Super-truth and sub-truth

In English:
- **Structure.** The structure is right, and `superTrue_member_iff` is "definitely within the self".
- **Terms.** "Super-true" is Fine's (1975) term; "sub-true" is subvaluationist (Hyde 1997), not Fine's. The module cites neither.
- **Not a supervaluation of the self.** The admissible class has no clear non-members, so it is not a supervaluation of the ordinary vague "self".
- **Invariance is determinacy.** Assuming invariance assumes that the presupposition has no penumbra, which a supervaluationist about the self would deny.
- **The two scopes.** The claim is correct. Route (b) puts the "definitely" operator at narrow scope and the axiom puts it at wide scope; the operator does not distribute over the conditional.

<a id="f9乙中等对手的位置--where-the-rivals-sit"></a>
### Where the rivals sit

In English: along a relation covering holds by construction, so these rivals deny another premise.
- **The closure rival (P5).** It denies sub-truth along a relation under which its closure is not closed: operational closure is not closed under feeding. Along a relation under which its closure is closed, it denies invariance, as route (b) does at the feeding closure. It denies covering only if it also restricts the admissible drawings to its closure.
- **The vague self.** It denies covering as the module words it, when every admissible drawing leaves the stranger out. It denies invariance when the stranger is borderline.
- **P7.** It denies sub-truth if its weight vanishes inside the closure, and invariance if the weight vanishes beyond it. The module does not locate P7.

<a id="f10乙次要层级次序没有定理--the-order-of-levels-has-no-theorem"></a>
### The order of levels has no theorem

The order follows from `Boundary.of_larger` (A3), but in `Clearing` its first two readings coincide. The reading maps Ren's "the self" to the feeding closure; the bare self is the empty relation (A2).

<a id="4-系统内的行为--conduct-within-the-system"></a>
## 4. Conduct within the system

In English, the result is true in the representation for parts wholly within the center's system, and it depends on items 1–7 above. Beyond the representation:
- **Responses.** A comparison in which others respond can make withholding a part create exchanges with conditions never touched in the actual flow. Formations outside the actual system can then be reached (甲, not formalized).
- **"The whole need not be admissible".** This misleads: along sharing a condition the whole is always admissible. What is meant is that neither invariance nor super-truth is used.

<a id="5-ren-的原话与-ai-的读法--rens-words-and-the-ais-readings"></a>
## 5. Ren's words and the AI's readings

| Reading | Assessment |
|---|---|
| the influence closure as what feedback can register | **Plausible**, with F2's disclosure. |
| “still need situational awareness”读作“须知道反馈之外” / read as knowing beyond one's feedback | **Plausible** AI elaboration; Ren's parenthesis qualifies "the full truth set". |
| 系统读“the system that one is in” / the system as "the system that one is in" | **Overreaching** (F1). |
| gives the whole's verdict on every act within the system | **Overreaching**; see §4. Where the system is the whole, its premise is the axiom at that standpoint. |
| the presupposition as Ren's "belief" | **Contestable**: Ren wrote it of the self's limit. Using it as a premise is the AI's step, and sub-truth along a relation is far stronger than "some continuation matters". |
| covering as these two lines | **Contestable**: the second line supports the whole as a drawing of "we"; the first does not imply covering; the substance is the admissible class. |
| invariance as Ren's invariances | **Overreaching**: Ren's invariances are invariances of the law across universes. "For all beings" reads most directly as standpoint invariance. |
| “three claims Ren holds” | **Overreaching attribution.** |
| the extension: system = whole as "Ren's highly entangled system" | **Overreaching**: Ren's claim is about present coupling strength; the formal condition holds in any world with one commons. |

Ren's line on continuation beyond death is unused. It bears on individuating by lineage and on step-ordered reach (B4).

<a id="6-扩展-p43extlean--the-extension"></a>
## 6. The extension

All ten theorems are correct and axiom-free.

- **Accept.** Add the unconditional form and the downward direction.

  / **Accept the theorem.** Without the presupposition everywhere, the two forms differ (A4). They coincide under the stated premises because each is then the axiom. State that the step is boundary neutrality at one standpoint and N_std across standpoints, and withdraw "derived, not assumed".

  / **Accept the theorem; reject the reading and the framing.** The whole is then the only boundary, so invariance holds trivially. The step has moved into the requirement that boundaries be closed.

  / **Reject the "so".** The theorem shows that the system is closed to what lies outside. The conclusion for one's own part follows from other theorems, and it fails for joint parts with members beyond the system (C1).
- Its docstring claims two conjuncts its statement lacks.
- Placement.**

  / As planned, `Clearing.system_whole` cannot go into Feedback, because its third conjunct uses Boundaries. The split in `merge_ext.py` compiles axiom-free.

<a id="7-须作的更正按严重程度-required-corrections-by-severity"></a>
## 7. Required corrections, by severity

1. The reading of the system**（F1）。
   - 在 `Feedback.lean` 的 AI 读法中，把 “The system reads Ren's “the system that one is in”: everything linked to the formation through conditions in which they take part.” 改为：
     > The system is the class of formations linked through conditions in which they take part. It bounds every effect: what lies within it reaches only within it, and what lies beyond reaches nothing within it. Wherever one condition is taken part in by everything it is the whole, as in `Clearing`, so it does not read Ren's intermediate “system that one is in”. For that reading the reach closure is offered, pending Ren: what a center's exchanges affect, link by link (`Flow.WithinReach`). It is centered and nested, lies within the system, and need not hold the center's feeding closure.
2. The weaker version**（§4）。
   - 把 “Ren's weaker version, “within the system that one is in”, gives the whole's verdict on every act within that system.” 改为：
     > Significance that covers a center's system gives the axiom's verdicts on every part whose members all lie within that system and whose levels without it exist, in the comparison that holds the rest of the exchange fixed. Where the system is the whole, that significance is the axiom at the center's standpoint.
3. A decomposition, not a reduction**（F6）。
   - 加入 `boundaryInvariant_iff_conditional`、`invariance_levels_down`、`boundaryInvariant_iff_determinate`，以及扩展的 `boundaryInvariant_iff_all`，并写：
     > Invariance is the conditional from the presupposition to the axiom at that standpoint; given the presupposition, it is the axiom there. The decomposition locates the step and does not lower the axiom's content. It runs both ways: where some continuation lacks significance, an invariant presupposition is nowhere true.
   - 把 “Agreement between standpoints is then derived, not assumed” 改为：
     > Agreement between standpoints follows. Given the presupposition at every standpoint and covering by centers, invariance is equivalent to standpoint invariance, the rule of N_std (`boundaryInvariant_iff_standpointInvariant`).
   - 加一段复用说明：
     > Given the presupposition, invariance at a standpoint is the axiom there, which P39 reads as boundary neutrality. The premises carry the decompositions of `Valuation.significant_iff` (a seed, N_rel and N_std on a connected whole) and `Valuation.significant_iff_held` (S0 at every standpoint with N_std) to the significance of continuation.
   - 把 “It takes the place of the earlier route's tolerance” 补为：
     > ... and, like tolerance with Chain, it carries all of the axiom's content beyond the presupposition.
4. Two counterfactuals**（F2）。
   - 在两个模块的表示说明中加入：
     > The verdicts compare the levels without a part with every other exchange held fixed, so they register only a part's direct exchanges, and a formation's support registers only the parts that reach it (`Flow.Balances.admits_unreached`). Mediated effects, such as the wolves' protection of the forest through the deer, appear only in a comparison where others respond. With the rest fixed, the wolves' part narrows and does not reach the forest; against the responsive flow it is mixed. Where a part gives what others take, the levels without it may not exist, and no verdict is given.
   - 在 “The influence closure reads what a formation's own feedback can register” 后加：“once effects pass through the support and activity of others”。
5. The extension**（§6）。
   - 标题 “The two forms of the step are one” 改为：
     > Given the presupposition and centers covering, the two forms of the step are equivalent: each is then the axiom.
   - 主张 (4) 改为：
     > What lies within a system reaches only within it, and what lies beyond reaches nothing within it.
6. **对手的位置 / Rivals**（F9）。把 “A rival that grounds the self in a formed closure, such as operational closure, denies it, and so does a vague self whose every admissible drawing leaves the stranger out.” 改为：
   > Along a relation, covering holds by construction, so these rivals deny another premise. A rival that grounds significance in a formed closure denies sub-truth along any relation under which that closure is not closed, as operational closure is not closed under feeding. Along a relation under which it is closed, it denies invariance: it holds its presupposition only at that closure, as route (b) does at the feeding closure. It denies covering only if it also restricts the admissible drawings to that closure. A vague self denies covering where every admissible drawing leaves the stranger out, and invariance where the stranger is borderline. A graded weight that falls to zero denies sub-truth if it falls inside the closure, and invariance if beyond it. A present-aim evaluator denies sub-truth.
7. Attributions to Ren**（§5）。
   - “three claims Ren holds” 改为 “three claims the assistant read from Ren's words”。
   - 不变性一条改为：
     > Ren's “for all beings” reads most directly as standpoint invariance, the rule of N_std; given the presupposition and covering, boundary-invariance is equivalent to it. Ren's “universal invariations” are invariances of the law across universes; extending them to significance is the AI's reading.
   - 预设一条加：
     > Ren wrote this of the self's limit; using the belief as a premise is the AI's step.
8. **覆盖 / Covering**（F7）。把 “Boundaries closed along a relation meet it without further premise, since the whole is one.” 改为：
   > Along a relation, covering holds because every closed region holding the center, the whole included, counts as an admissible drawing of the self. That admissibility is the substantive choice.
9. Supervaluation terms**（F8）。
12. **误判的说法 / The misjudging sentence**（F5）。把 “A center that values only what its feedback registers misjudges its own acts exactly where they reach beyond that closure, as the clearer does.” 改为：
    > A center that values only what its feedback registers judges its own acts as the axiom does wherever they reach only within that closure (`verdict_local`). Where they reach beyond it, it can misjudge them, as the clearer does; reaching beyond does not by itself make it misjudge (`Margin`).
13. Positive adding verdicts**（F4）。
    - 把 “What is not derived” 中 “the adding verdicts in positive form: the core is constructive, so they are stated as “neither adds exactly where neither exceeds”.” 改为：
      > the adding verdicts in positive form for every significance. They are stated as “neither adds exactly where neither exceeds”; they hold in positive form where significance is decidable (`adds_iff_exceeds_of_decidable`), and in general up to double negation (`not_not_adds_of_exceeds`).
14. Local docstrings**。
    - `system_retains_iff` 的文档与 Feedback 模块说明中，“judges what is done within it as the axiom does”（及 “judges every part within that system as the axiom does”）改为：
      > retains along every part within it exactly where the axiom's significance does
    - Boundaries 模块说明中，“Drawn at the feeding closure, it licenses the part” 改为：
      > Drawn at the feeding closure, it is met by a significance under which the part retains

    - `Boundaries` 的 “What is not derived” 加：
      > the presupposition itself, which is supplied as every significance is (`Web.significance_undetermined`); along a relation it already carries transmission along that relation, from the bare S0 of the empty relation to the axiom of the total one
15. Records and reuse**。
      - `metaethical-core-characterization`（`Valuation.significant_iff`）；
      - `held-lives-g0-is-centering`（`Valuation.significant_iff_held`）；
    - “conduct”改为 “a part's exchange”。

<a id="8-探针--probes"></a>
## 8. Probes

Files：
- `review/probes/ProbeA.lean`（sha256 `8a0dafae…6fd70`）、`ProbeB.lean`（`385048b1…3810b`）、`ProbeC.lean`（`61cb618e…1752e`）；

All are term-mode, and every `#print axioms` reports no axioms.

| Id | Theorem（`Becoming.ReviewP42.` 下） | Shows |
|---|---|---|
| A1 | `system_whole_of_commons`, `only_whole`, `clearing_clearer_system`, `clearing_subTrue_shares_iff`, `Static.shares_unaffected` | One commons makes the system the whole; then the whole is the only boundary; co-dependence suffices. |
| A2 | `boundaryInvariant_iff_conditional`, `invariance_levels_down`, `boundaryInvariant_iff_determinate`, `subTrue_total_iff`, `subTrue_empty_iff` | Invariance is the conditional and determinacy, and runs downward; the relation sets the strength. |
| A3 | `subTrue_of_larger`, `presupposition_levels` | The order of levels as implications. |
| A4 | `forms_apart` | The two invariances differ without the presupposition everywhere. |
| B1 | `Flow.Balances.verdict_local` | Agreement on the reach decides the verdict. |
| B2 | `Flow.Balances.adds_iff_exceeds_of_decidable`, `Flow.Balances.not_not_adds_of_exceeds` | Positive adding verdicts. |
| B3 | `Flow.Affects`, `Flow.WithinReach`, `Flow.reaches_withinReach`, `Flow.withinSystem_of_withinReach`, `Flow.Balances.presupposed_reach_verdict`, `Flow.subTrue_affects_of_shares` | The reach closure: centered, nested, on a weaker premise. |
| B4 | `Flow.Balances.exchanges_before_of_differs` | Step-ordered reach. |
| B5 | `ClearingReach.middle`, `ClearingReach.centred`, `ClearingReach.reach_counts_dweller` | A genuine middle level in `Clearing`, without the source. |
| C1 | `Wolves.protection_invisible`, `Wolves.responsive_mixed`, `Wolves.far_system`, `Wolves.mixed_part` | Mediated protection is invisible; the verdict's category depends on the counterfactual; a mixed part. |
| C2 | `Source.no_levels_without_source` | No comparison for an essential giver. |
| C3 | `Margin.reach_without_misjudgment` | Reaching beyond without misjudgment. |
| C4 | `Late.affected_without_effect` | Affected without effect. |
| M | fails）, `FeedbackPartSplit.lean`, `BoundariesPartSplit.lean` | Placement of `Clearing.system_whole`. |

Verbatim output (an excerpt; every line has this form):

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

The third line from the end comes from `merge-check/FeedbackPartSplit.lean`.）

In this Lean, `Nat.succ_ne_zero` and overlapping wildcard patterns bring in `propext`. The probes avoid both, and merged code must too.

<a id="9-审查者自身的边界--reviewers-limits"></a>
## 9. Reviewer's limits

- Probes show entailment or consistency under the stated conditions only.
- The literature is cited from prior knowledge.
- No normative verdict is given on any premise; only inference, correspondence, scope and reading are judged.
- The point about responsive comparisons in §4 is a sketch, not formalized.
- The merge in progress was not reviewed, apart from the placement of `system_whole` in `merge_ext.py`.
