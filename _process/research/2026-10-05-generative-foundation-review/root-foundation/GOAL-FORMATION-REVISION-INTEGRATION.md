# 形成、反思与目的修订的相连实现 / Joined formation, reflection and goal revision

2026-10-08, Asia/Bangkok. AI-authored research answering [Ren's instruction](../../../../sources/15-codex-theory-conversations/2026-10-08-goal-formation-and-revision.md). The [canonical chapter](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/GOAL-FORMATION-AND-REVISION.md) supplies the explanatory account. This study reuses the existing directory and closes the finite implementation connection identified in [the earlier normative argument, §7](GENERATIVE-ALIGNMENT-REVISION.md#7-当前结论与下一项判别--result-and-next-discriminator).

**结果：同一模型历史中的实际反馈形成目的，校准后的后果证据及形成记录支持判断，响应改变操作目的，有权限的改革改变原选择规则，后续行动消费新目的并保留真实损失。改变后的规则也改变后续目的取得。** 新增 **43项 Lean 定理、85项显式声明审计**通过；另重查50项继承定理、80项继承声明，分列不重复计数。完成的是相连理论候选及有限条件实现，不是生物全尺度验证、充分理解的普遍判准或伦理必然收敛。

**Result.** A single model history connects acquired goals, calibrated evidence about consequences and formation, a warranted comparison, responsive goal change, authorized reform of selection, actual continuation and changed subsequent acquisition. Forty-three new theorems and 85 explicit-declaration audits pass. The 50 inherited theorems and 80 inherited audits remain separately credited. This is theoretical/formal completion at the declared scope, with same-author counterreview below; no independent-agent acceptance or new human/animal experiment is claimed.

## 1. The inference advanced

The universal normative programme needs to explain how its reasons can reach goals and selectors that themselves have a history. This study supplies a bounded **implementation and correspondence requirement** for that connection. It neither replaces ethical warrant with adaptive success nor restarts the completed G0/J argument.

The affirmative argument is:

1. A goal's formative feedback explains its retention but does not exempt its consequences from the whole comparison.
2. Evidence that identifies an additional lost basic condition, and a feasible alternative preserving the other basic conditions, brings the existing J2 comparison to bear on that goal.
3. Revising the operative outcome criterion can then be warranted even while the old criterion is accurately and successfully pursued.
4. The same acquired model of formation can identify the selection relation that will obstruct the revised practice. Reform requires actual means, resources and legitimate authority; insight alone supplies none of these.
5. Later operation must consume the revised goal and the changed support relation. A stated intention or a reset simulation is insufficient to establish the joined implementation.

The Lean witness satisfies this sequence. It starts from no acquired operative goal and carries the same account, feedback totals, consequence records and losses through the transition. The inherited native learning and biological studies are explanatory precedents; they are **not** silently treated as the physical carriers of this new finite model.

## 2. Premises and correspondence ledger

| Premise | Where it enters | What is and is not established |
|---|---|---|
| G0: living and further generation have basic positive significance | Ethical interpretation | An explicit starting axiom, not proved by the controller or supplied as a custom Lean axiom |
| J1/J2: full comparison and scoped priority of basic conditions | Imported `PracticalJudgment.Better` and the warranted-revision proof | The mathematical relation checks the inference; its ethical authority comes from the separate explicit commitments |
| J3/J4: bounded responsibility, authorization and feasible practical selection | Scope of deliberate reform | A Boolean authorization input tests a gate; it does not derive legitimate authority, standing or a complete duty allocation |
| Two practices, outcome laws and two goal criteria | `perform`, `attainment`, `meansFor` | Counted output and transferable mastery are stipulated local quantities, not fitted observations or a universal welfare score |
| Basic/secondary classification | `protects` and `gains` | Access and maintenance represent independently justified basic claims; counted output and mastery are distinct optional gains here. Whether actual costs or omitted effects cross those boundaries needs application evidence |
| Finite formative law family | `feedback`, `inferFormation` | Two trials identify the actual selector within this family. Unknown laws, confounding and arbitrary institutional structures are outside that identification result |
| Signal and reliable reference law | `encode`, `decode`, `calibrate` | Correct decoding is checked, including reversed signals. Calibration's reference meaning is supplied. False references retain a failure and a repair witness |
| Trial schedule, memory and acquisition architecture | `experience`, `acquire` | The operative goal and ground are acquired; the architecture and experiment schedule are not themselves learned here |
| Responsive deliberation | `reviseGoal` | Conditional change is implemented. Correct grounds do not force motivation; the nonresponsive branch retains the old goal |
| Intervention model | `predictFeedback`, `proposedSelector` | Unchanged-rule prediction depends on the inferred origin; replacement prediction uses the supplied law. Correct-origin correspondence is explicit; the model is not an oracle for new laws |
| Actual cost and finite support | `charge`, `cycle`, `operate` | Work, reserve and spent are accounted. The reserve is finite, its legitimate allocation is supplied, and no replenishment mechanism or indefinite viability is proved |
| Stable applicability | Conditions fixed during the successful continuation | A changed-condition witness defeats continued reliance on stale grounds. Monitoring/reacquisition is needed; a universally reliable automatic monitor is not supplied |

The model separates these roles for analysis while maintaining one state/history. It does not posit an independent subject confronting an external realm of facts or values. Nor does it derive the local law from a complete generative foundation. Its omissions are named representational limits, not proofs that the fuller theory cannot explain those relations.

**规范排序的范围。** `Better` 比较本例两种实践的完整已表示保护与可放弃产出；累计改革成本另在资源账户保留。将该成本说成未损伤其他基本条件，是本例明确的对应前提，不能仅凭“账户还没归零”推出。新取得的 mastery 是新目的的成就判准，并与真实计数产出一起作为不同的次级增益保留；二者未被折成一个总数。无基本损失时规则保留真实不可比；有损胜出依靠额外基本保护及公开 J2。

## 3. Checked mathematical package

Sources: [GoalFormationRevision.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/GoalFormationRevision.lean), [checker](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/check_goal_formation_revision.py), [passing receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/goal-formation-revision-verification.json).

Lean **4.29.1** compiles unchanged source snapshots in an isolated import directory. The checker rejects warnings, unfinished/unsafe/native-decision escapes and undeclared imports; prints each explicit declaration's axiom dependencies; and retains theorem signatures, source/helper hashes, toolchain binary hash and logs. It verifies that live sources still match the checked snapshots. Earlier failed compilations and earlier passing representations remain in the retained run directory; the receipt points to the latest successful version. Closed witnesses use kernel-checked `decide`, not `native_decide`.

| Module | Theorems | Explicit declarations audited | Dependencies |
|---|---:|---:|---|
| New `GoalFormationRevision` | 43 | 85 | 33 empty; 46 `propext`; 6 `propext, Quot.sound` |
| Inherited `PracticalJudgment` | 30 | 46 | 40 empty; 3 `propext`; 1 `propext, Quot.sound`; 2 also `Classical.choice` |
| Inherited `KnowledgeCorrespondence` | 20 | 34 | 31 empty; 3 with `propext, Classical.choice, Quot.sound` |

These are standard Lean dependencies; no new custom axiom is introduced. Absence of custom axioms does not remove substantive assumptions encoded in definitions and theorem hypotheses. The count concerns explicit declarations; generated structure constructors and recursors are not presented as separately counted audits.

The practical comparator is used in the new warrant and joined-history theorems. The inherited calibration interface is explicitly rechecked/re-exported; the local Boolean channel and acquired-history correspondence also receive their own proofs. We do not claim that importing a calibration theorem physically composes the earlier learning experiments.

| Checked connection | Representative exact declarations |
|---|---|
| Different goals rank outcomes differently; supplied means achieve each | `goal_criteria_really_disagree`, `supplied_means_realize_their_goal` |
| Stated losses support revision, with real output lost, mastery gained and safe/conflict incomparability | `warranted_revision`, `revision_loses_real_output`, `harmless_practices_incomparable`, `crossed_losses_incomparable` |
| Actually acquired formation and calibrated evidence | `acquired_history_identifies_origin`, `goal_depends_on_actual_formative_rule`, `acquired_calibration_correct` |
| Revision while the old metric still succeeds; recognition distinguished from response | `revised_goal_with_old_metric_still_successful`, `recognition_does_not_force_revision` |
| Model-guided reform and changed subsequent acquisition | `formation_model_predicts_intervention`, `acquired_intervention_prediction_realized`, `reform_changes_later_goal_acquisition` |
| Actual operation, history and conservation | `changed_goal_is_consumed_by_operation`, `cycle_conserves`, `supported_finite_continuation`, `continued_practice_preserves_actual_consequences` |
| Joined normative and operational result | `joined_revision_has_warrant_and_actual_continuation` |

`supported_finite_continuation` is generic in the number of supported cycles and account quantities. Most intervention and failure claims are deliberately finite witnesses. There is no theorem quantifying over every intelligence or every possible formative history.

## 4. Substantive counterreview and retained failures

This section is same-author review, not an independent agent's acceptance.

**“The model only changes means.”** The final representation separates `Goal`, `Practice` and `attainment`. The two goals rank the same outcomes oppositely, and the old goal's means remain optimal for it. Actual operation follows the new goal. This answers the operative-level objection. It does not refute the stronger fixed-metaobjective description: the response architecture is supplied and can be represented by an ordinary controller.

**Retained correction from final review.** The first representation of secondary gains omitted mastery and therefore made the harmless old practice dominate. Adding a distinct goal criterion exposed that omission. The final `gains` retains both mastery and counted output; `harmless_practices_incomparable` replaces the earlier superiority claim. The harmful-case protection result survives. Earlier passing snapshots prove their narrower definitions only and are superseded for the present application; their omitted-gain verdict is not evidence about the fuller case.

**“Understanding is only a label.”** There is no `Understands` flag. Acquired records identify formation; calibrated signals distinguish actual losses; the inferred rule affects intervention choice; false evidence can mislead and subsequent correction can repair the decision. These are functioning connections. They do not constitute a proof that every equally functional implementation has complete semantic or conscious understanding; nor do we posit an unexplained extra faculty merely to withhold credit.

**“Reform is automatically good.”** In the safe variant the practices are incomparable because each has a distinct optional gain. Retaining the old goal is one undefeated response, not a theorem that it is best. In the crossed-loss variant neither practice has the stipulated priority. Reform may fail for lack of authority or work. An aggregation-sensitive rival can reject J2 even with every outcome represented; it is not thereby inconsistent with G0.

**“Later success erases the earlier damage.”** The initial actual loss, both trial records, old feedback totals and forgone output remain. Continued activity adds records rather than resetting the history. Nothing here proves complete compensation or discharge of prior obligations.

**“The support loop is self-sustaining.”** It is not: the finite reserve pays for the demonstrated extension. Unchanged selection blocks the third subsequent operation, while reform permits five and then blocks the sixth. The general cycle theorem states its reserve premise. Legitimate funding, renewal and systemic displacement of costs require further correspondence.

**“The formation account cannot matter because the intervention law was supplied.”** Prediction of a replacement rule does use that supplied law. What is acquired is which formative rule produced the old goal and whether its unchanged operation will support the new one. The wrong-formation witness prevents reform; changing the actual formative rule changes the acquired goal. This is identification and use within a known family, not unrestricted causal discovery.

**“A proof of revised judgment ensures reliable conduct.”** Nonresponse preserves correct grounds and the old goal. A false reference can hide the loss; correcting it restores revision. Missing feedback blocks assessment. Stale grounds continue the old goal despite a new loss. The controller therefore demonstrates conditional capability and genuine failure, not guaranteed ethical development.

## 5. Primary research and conventional credit

Targeted primary-source abstract checks, 2026-10-08; not a full literature review or performance comparison.

| Source | What the source supports | Relation to this result |
|---|---|---|
| Everitt, Filan, Daswani and Hutter (2016), [Self-Modification of Policy and Utility Function in Rational Agents](https://arxiv.org/abs/1605.03142) | Formal self-modification, including conditions involving anticipated consequences and evaluation through current utility | Goal preservation under a current evaluator is a substantive existing formal account. Our operative goal revision is compatible with a fixed higher-level controller; the ethical question is which comparative commitments warrant revision |
| Yang et al. (2020), [Learning to Incentivize Other Learning Agents](https://papers.neurips.cc/paper_files/paper/2020/hash/ad7ed5d47b9baceb12045a929e7e2f66-Abstract.html) | Learned incentives account for their effects on recipients' learning and resulting extrinsic returns | Changing conditions that shape learning is established work. Our contribution is the stated joined correspondence and normative application, not inventing incentive reform or outperforming that method |
| Carroll et al. (2024), [AI Alignment with Changing and Influenceable Reward Functions](https://arxiv.org/abs/2405.17713) | Dynamic, influenceable preferences and tradeoffs among eight alignment notions | Preference change is already explicitly studied. The present G0/J route supplies a declared appraisal of a constructed change, without proving those commitments uniquely correct or the empirical case realized |

A conventional model-based learner with retained evidence, a higher-level comparison rule and control over incentives could implement the same finite history. That is credited as a genuine explanation. Nothing in the proofs establishes exclusivity for the theory's vocabulary. The remaining explanatory contribution must come from the defensible connection among formation, normative grounds, differentiated responsibilities and actual continuation.

## 6. Completion audit and next correspondence

The present request is answered with a connected account and a checked realization, including the actual consumption of changed goals and the effect of reform on later acquisition. No unused selector label or unspent infinite fund stands in for the final transition. The chapter explains which descriptive changes are required when goals and formative arrangements become variable.

The stronger claims remain distinct: autonomous formation of the deliberative architecture, generation of genuinely new goal repertoires in this implementation, universal semantic sufficiency, reliable moral convergence and the full biological joint experiment are not established. This does not reopen the existing evaluative, method-revision, semantic or explicit-axiom ethical candidates at their completed scopes.

The next empirical bridge is **acquired grounds → criterion revision and targeted formative intervention → later acquisition and continued practice in one recorded history**. A discriminating study must keep the old metric attainable; vary relevant consequences independently of approval; distinguish correct judgment from implemented response; record the costs and authority of reform; and test false or stale grounds. Simulated evidence, protocol design and actual experimental validation must retain separate statuses. The [earlier biological joint programme](BIOLOGICAL-JOINT-VALIDATION.md) remains unexecuted at its full target.

Index maintenance and source bindings: [owned edit record](GOAL-FORMATION-REVISION-INDEX-EDITS.json) and [scoped checks](GOAL-FORMATION-REVISION-CHECKS.json). These verify this study's integration, not every concurrently changing repository source.
