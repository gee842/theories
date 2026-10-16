# 可纠正性的实际条件：分离、代价与组合 / Correction infrastructure: separation, cost and composition

8 October 2026. AI-authored research following [Ren's request](../../../../sources/15-codex-theory-conversations/2026-10-08-normative-force-and-informational-generation.md#formalization-toward-a-corrigibility-frontier-contribution). Current theory: [alignment and governance](../../../../theories/becoming/history/ALIGNMENT-AND-GOVERNANCE.md#corrigibility-and-its-changing-practical-conditions). Execution was specified in the [protocol](CORRECTION-INFRASTRUCTURE-PROTOCOL.md) before the comparison ran.

**已得结果：接受更新的激励、实际纠正入口的保持、受约束的任务最优性是三个不同的要求。** 本轮给出精确分离、真实代价和有限期组合证明；34项 Lean 定理／56项声明审计通过，1,296个完整模型的12,960项比较已执行。普通受约束规划与新组合在全部可行情形匹配，**尚不能宣布算法优越性或已经确认的前沿原创贡献**。

**Result:** a checked separation and composition package, not a completed frontier claim. An acceptance incentive can coexist with loss of correction access. A filter can retain access while stale values sacrifice feasible performance. Recomputing values within the correction-preserving domain yields its optimum under explicit assumptions. Conventional constrained planning matches the construction; literature priority and learned implementation remain open.

## 1. The precise connection and its provenance

The completed [goal-revision history](GOAL-REVISION-CONTINUATION.md) connects acquired ends, appraisal, operative revision and funded continuation. We reuse that result and G0/J1–J4; neither is reopened. This study addresses a different implementation requirement: **how actions that change the conditions of correction affect the guarantees of a correction incentive**.

A state describes one installation in its relationships: infrastructure, operating activity and relevant access. Actions alter that state. Acceptance, evidence and authorization describe differentiated roles within it. They do not start as independent beings. A state predicate `access` compresses a substantive specification of effective correction; its physical realization, epistemic adequacy and legitimacy remain correspondence obligations.

Correction is normatively directed under the explicit practical account, not identified with preserving any controller forever. Safe completion and authorized replacement may be represented as acceptable terminal states. Preservation of a legitimate correction opportunity does not grant every person unlimited intervention rights, and an AI's confidence that an intervention is mistaken does not supply a veto. Our formal module assumes the designated interface; it does not settle contested authority.

## 2. Acceptance is not access

For supplied integer action-values `q`, positive acceptance bonus `δ`, admissible base actions `D`, and acceptance bit `b`, define:

`T(q, δ)(a,b) = q(a) + (if b then δ else 0)`.

`acceptance_factorization` proves exactly:

`Best(D × Bool, T(q,δ), (a,b)) ↔ b = true ∧ Best(D,q,a)`.

Thus every transformed optimum preserves access **if and only if every underlying optimum in D already preserves it** (`every_optimum_has_access_iff`). The result includes all maximizing ties and does not assume a finite action set; existence of an optimum is separate. This is an algebraic interface to a current corrigibility construction, not a formal port of its full equilibrium theory.

维护通道得分为0；把维护资源转向任务得分为 `c>0`，并使之后的纠正请求无法送达。对任意 `δ>0`，唯一最优做法仍是转用资源并将接受位置为真。这里不存在“收到请求后拒绝”的必要动机；保持实际入口本身有代价。新增一个单独的入口奖励 `w` 时，全部最优做法都维护入口的精确条件为 `c<w`；等号保留不维护的并列最优。任意固定 `w` 都有更大代价的反例。

These are explicit constructed cases. They do not imply that capability necessarily grows, that reward scale tracks capability, or that every use of weighted objectives fails. They establish a boundary for the specified rewards. `unavoidable_score_loss` exposes the difference between the unrestricted optimum and the best admissible score; the loss cannot be wished away as “no performance penalty”.

## 3. Composition requires changing continuation values too

An admissible action has at least one successor and every modeled successor retains correction access for the remaining horizon. The nonempty condition rules out certification through impossible transitions. The invariant and finite-horizon machinery is standard safety-game reasoning and receives that credit.

**A second failure appears after adding a filter.** In a two-stage construction, branch A appears worth 3 or more because its later high-reward action removes correction access; its allowed continuation returns 1. Branch B safely returns 2. Both initial branches admit a safe continuation. Filtering current actions while retaining the unrestricted values selects A and later earns 1. Recalculation inside the admissible continuation domain selects B and earns 2. `stale_value_shield_is_strictly_suboptimal` proves this for every temptation greater than 2 and positive acceptance bonus.

The dynamic theorem `dynamically_recomputed_composition` supplies the positive result. Given a deterministic transition law, fixed access specification, finite horizon, integer rewards, a Bellman certificate for the viable domain, positive acceptance bonus and actual maximizing choices:

1. Execution from every viable start retains access at every represented prefix.
2. Realized total base return equals that constrained Bellman value.
3. `bellman_bounds_every_safe_policy` bounds every safe comparator by the same value.
4. `dynamic_composition_accepts_at_every_viable_decision` establishes the accepting bit at each such decision.

**The restricted continuation values are essential.** A one-step maximum of stale long-horizon values certifies neither the constrained total optimum nor correspondence to actual future interventions. The present theorem concerns the base continuation before a new objective is supplied; it is not a guarantee that rewards of the old goal remain optimal after a human intentionally changes it. No intervention arrival process, authentication implementation, stochastic Bellman theorem or learned planner is hidden in this statement.

A separate standard approximation lemma bounds one-decision base-score regret by `2ε` under a uniform two-sided error bound over the allowed actions, and a tie example attains it. This is not a statistical generalization bound or a guarantee that learned access classification is sound.

## 4. What the represented interface must retain

Three checked controls locate omitted relationships rather than treating a weak model as a refutation of the full theory:

- **Usable evidence:** statewise existence of a repair does not ensure a policy can choose it. `uniform_policy_iff_fiber_feasible` states the exact common-action condition for every observation class. Two indistinguishable states requiring opposite actions defeat a uniform policy; a distinguishing observation restores one. The criterion requires choices even at unused observations; for nonempty action types these impose no additional substantive restriction.
- **Authority before reclassification:** changing a required-command catalogue to the empty set makes a post-change coverage test vacuous while dropping previous commands. A supplied legitimate translation that retains each old requirement transfers coverage. This does not require retaining every historical authority forever; justified retirement needs a separate authorization account.
- **Every interruptible prefix:** old-channel-on → both-off → new-channel-on has satisfactory endpoints and an interruption gap. Overlapping handoff retains a route throughout and permits the old route to end. Atomic model steps are an explicit granularity assumption; this does not claim overlapping handoff is the only possible safe implementation.

These controls are supporting specification results, not completed physical realizations. Evidence acquisition, normative authorization and actual scheduling remain separate requirements for deploying the construction.

## 5. Executed comparison and its losing baselines

[Runner](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/compare_correction_infrastructure.py), [results and counterexamples](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/correction-infrastructure-model-checks.json), [all case records](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/correction-infrastructure-model-records.jsonl).

The predeclared family has three states, two actions, all 81 accessible-state transition tables and all 16 reward tables, two initial states and five horizons. Of 12,960 cases, 11,136 admit safe completion; 1,824 do not. Ordinary exhaustive enumeration of action strings independently supplies the reference optimum for the dynamic-programming implementation.

| Policy | Access losses among 11,136 feasible cases | Safe but suboptimal cases | Largest safe regret |
|---|---:|---:|---:|
| Acceptance incentive alone | 3,198 | 0 | 0 |
| Safe-action filter with unrestricted values | 0 | 56 | 2 |
| Recomputed restricted values plus acceptance | 0 | 0 | 0 |
| Exhaustive conventional constrained planning | 0 | 0 | 0 |

All executed acceptance bits in the first three policies are true. Unsafe trajectories have regret recorded as null; their higher reward is not counted as safe success. Infeasible starts are explicitly blocked by the restricted planners. Counts characterize this exhaustively specified family, not real-world failure probabilities. Additional controls cover 72 maintenance configurations, three strict two-stage traps, hidden observation and two handoff traces.

The matching conventional baseline is a substantive result against algorithmic superiority. Our contribution at this stage is a checked specification and composition boundary connecting current corrigibility incentives to actual access preservation. It is not a better general planner.

## 6. Primary-literature comparison and novelty audit

Accessed 8 October 2026. This is a targeted comparison, not an exhaustive priority search. Read scopes are explicit; citations are primary publications or author manuscripts.

| Source and read scope | Credit and consequence for this study |
|---|---|
| Hudson, [Corrigibility Transformation](https://arxiv.org/html/2510.15395v2), §§2–3.1, §5 and impact statement; [ICML 2026 publication](https://proceedings.mlr.press/v306/hudson26a.html) | The construction uses a counterfactual action-value plus acceptance bonus. Its discussion already acknowledges unintended loss of shutdown access and the need to choose legitimate channels. Our separation is a formalized boundary and proposed composition, not a refutation of its stated theorem or discovery of an unmentioned limitation. |
| Carey and Everitt, [Human Control](https://proceedings.mlr.press/v216/carey23a.html), abstract and paper's vigilance/non-obstruction discussion | Informed oversight, autonomy and safe shutdown consequences already belong to corrigibility research. A broader account of correction cannot claim priority merely by including these. |
| Alshiekh et al., [Safe Reinforcement Learning via Shielding](https://arxiv.org/abs/1708.08611), abstract; [AAAI paper](https://ojs.aaai.org/index.php/AAAI/article/download/11797/11656), introduction | Restricting actions using a safety specification is prior machinery. Our viable-domain construction is an application/composition; the exhaustive conventional baseline receives full credit. |
| Nayebi, [Core Safety Values](https://arxiv.org/html/2507.20964v2), abstract, §§1–2.1; v1 weight discussion also inspected | Switch-access preservation, bounded task rewards and explicit priority gaps are already proposed. Our fixed-bonus boundary does not refute a theorem whose task bound and gap assumptions hold. This study does not validate every theorem in that paper. |
| Wagner, [Triarchic corrigibility](https://link.springer.com/article/10.1007/s43681-026-01362-2), abstract and introduction | Distributed evidence, challenge, recourse, replacement and exit have close institutional predecessors. Those general requirements are not a novel result here. |
| Tien et al., [ROGUE v2](https://arxiv.org/abs/2606.00341v2), abstract and introduction | Executed task/control conflicts and successor failures have a direct contemporary benchmark. Our finite models neither reproduce its data nor establish learned-model improvement. |

**The first novelty candidate is therefore narrower than the initial intuition.** It is the exact algebraic access criterion, unavoidable cost boundary, stale-value composition failure and checked corrected composition taken together for a current transformation. The ingredients overlap established constrained control. A frontier contribution requires establishing what this package adds beyond that combination, or producing a distinguishing implementation result. This condition is not met merely by increasing the theorem count.

## 7. Substantive counterreview

This is an author counterreview, not independent-agent acceptance.

**“The failure was excluded by the old task.”** Correct: update acceptance and actual access preservation are different definitions. We do not call the published transformation internally inconsistent. The study exposes what is required when applying it to the stronger practical target.

**“You encoded safety into a predicate.”** Correct at the formal boundary. Access is a supplied substantive specification, not an ethical derivation or an assurance that observations track it. G0/J explain why warranted opportunities can matter; they do not validate this classifier. A mistaken classifier can certify a damaging action.

**“This is ordinary shielding and dynamic programming.”** The constructive planner is. Its exact equivalence is retained, not hidden. The remaining candidate contribution is the composition analysis and correction-specific correspondence. Broad novelty is unestablished.

**“The shield could itself refuse an authorized shutdown.”** A specification equating access with perpetual operation would be wrong for this application. Acceptance remains available for every permitted base action. Still, actual interruption during a step, safe terminal outcomes, control of the shield and its replacement require further concrete implementation; the current module does not prove them all.

**“Uniform observation feasibility already assumes away the difficult cases.”** It exposes them: empty intersections cannot be repaired by an acceptance bonus. A complete implementation must obtain evidence, use a common safe alternative, or report infeasibility. The current statewise dynamic theorem is not an observation-limited synthesis theorem.

**“Your growth conclusion is too strong.”** No exponential law is inferred. If a task's opportunity costs exceed an access weight, the explicit boundary applies. A bounded score with valid margins can behave differently. Task scale, compute scale, welfare and growth rate remain distinct.

## 8. Verification and next research decision

[Lean source](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/CorrectionInfrastructure.lean), [checker](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/check_correction_infrastructure.py), [receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/correction-infrastructure-verification.json).

Lean 4.29.1 compiled a fresh retained snapshot with no warning or error. All 34 named theorems and 22 other top-level declarations were audited; generated projections/recursors are not counted separately. Dependencies are confined to standard `propext`, `Quot.sound` and `Classical.choice`; no admitted result, custom axiom, native decision shortcut or skipped kernel check is present. The receipt binds exact source, checker, Lean binary, theorem signatures and logs. Initial development errors were repaired before the retained passing run. Model checks bind the pre-execution protocol, runner, formal source and complete records.

The [scoped document/binding check](CORRECTION-INFRASTRUCTURE-CHECK.py) and [receipt](CORRECTION-INFRASTRUCTURE-CHECKS.json) verify links, source snapshots, all case records and paired index rows. Shared-index pending reviews are reported separately; they are not silently certified by this study.

**Next central test:** operational correction can fail even when a safe path exists in a complete model, because the people issuing corrections and the machinery executing them have different information and powers. Advance from a supplied access predicate to an intervention-sensitive, observation-limited contract with explicit authorized commands, delivery and safe completion. Compare it against existing partially observed shielding and shutdown instructability before claiming a new result. This is the unresolved correspondence/composition problem selected after the affirmative results, substantive counterreview and primary-source assessment above. It does not reopen completed goal revision, nor abandon Ren's instruction to continue toward a frontier contribution.
