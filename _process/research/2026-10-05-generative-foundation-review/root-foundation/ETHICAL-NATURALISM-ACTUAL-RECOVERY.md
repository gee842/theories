# 实际恢复不能抹掉中断 / Actual recovery retains the interruption

7 October 2026, Asia/Bangkok. AI-authored continuation of [ethical naturalism §11](ETHICAL-NATURALISM.md#11-评价被实行时取向是否由延续导出) and the [enacted-orientation handoff](../../../handoffs/2026-10-07-enacted-orientation.md). This advances the unfinished immediate/eventual bridge under [Ren's first priority](../../../../sources/15-codex-theory-conversations/2026-10-07-normative-grounding-first-priority.md). It is a supporting adequacy result for whole-process ethical justification. It is not another candidate claiming that a persistent dynamics is already good.

**Result.** The handoff's proposed reduction of whole-history loss/recovery comparison to eventual realizability fails. Even if every interruption is actually followed by restoration, a finite process can accumulate arbitrarily many unavailable occasions while retaining exactly the same eventual activity profile. A constructive replacement records actual losses, actual recoveries, and the interruption that occurred between them, all at the same immediate level. Restoration changes what can happen next; it does not make the interrupted interval absent from the history.

**结论。** “后来确实恢复”与“中间没有失去实际实现的机会”不是同一回事。前者成立不能证明后者。可以从过程内部同时记录取消、恢复与已经发生的中断，而不把每次暂时失去都判为整体上的恶，也不把每次回升算成没有代价的净生成。这个结果关闭了把整体比较直接压缩成最终可实现性的路线；它没有关闭普遍伦理根据的问题。

## 1. The exact transition being tested

The proposed connection was:

> Recurring immediate losses have return paths; therefore actual loss and recovery can be compared wholly at the level of eventual realizability, where recurring enactment preserves possibilities.

The first clause needs quantifier discipline. In the existing `EnactedOrientation.lean`, `RecursUnboundedly` means **for every natural number there exists a finite trace** with at least that many marked transitions. It does not supply one specified infinite actual history. `recurring_enactment_keeps` finds **some reachable marked transition** on a return path. It does not say every marked transition returns, that an offered return is taken, or that all actual interruption is restored. Those theorems remain correct at their stated scope.

The second clause fails even after strengthening the premises: the new witness explicitly performs the restoration after every closure. Its histories are actual runs of the one supplied transition law, with recovery included, not records that announce opposite evaluations while changing nothing.

The ethical target is also fixed. We test whether eventual continuation preserves the information needed to assess **actual realization and its interrupted conditions**. We do not assume that every action label deserves protection, every unavailable option is adverse, or infinite preservation is the end of every good activity. An action that completes a finite undertaking need not remain performable forever.

## 2. One process, differentiated relations

[`ActualRecovery.lean`](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/naturalism/ActualRecovery.lean) imports the existing naturalism chain. For a Boolean capability `c` and an actual `Run r`:

| Profile component | What is counted |
|---|---|
| `losses c r` | Actual transitions from available to unavailable |
| `recoveries c r` | Actual transitions from unavailable to available |
| `interruptions c r` | Unavailable destination occasions in the actual history |

The third count excludes the starting state so composition counts the shared boundary once. It counts specified observation occasions, **not elapsed time, suffering, welfare, or units of ethical damage**. Replacing one interval by several observations changes it. A physical application must justify its clock or supply duration weights; this formal construction does neither. No cross-capability sum is introduced.

The generic projection `c` is supplied. In the concrete witness it is **derived from the process's own enabling relation**: `ready_is_enabled` proves that the Boolean state is true exactly when the `realize` event is presently enabled. `close` and `restore` change this relation; `hold` retains it. The state, possible realization, and activity changing its conditions are dependent descriptions of this one process. They are not a subject, an independent environment, and an externally assigned value.

This representation preserves actual order, the changing enabling relation, and restoration. It omits the constitution of the activity, experience, consent, other differentiated effects, and why realization of this activity matters. Those omissions block a complete ethical verdict; they do not block the adequacy test concerning immediate and eventual realization.

## 3. Constructive results

For every process and every actual finite run, without state finiteness or decidable state equality:

1. **Composition:** each of the three counts adds when runs are concatenated (`losses_append`, `recoveries_append`, `interruptions_append`).
2. **Actual balance:** losses plus final presence equals recoveries plus initial presence (`actual_balance`). Loss and recovery are defined at one immediate level; possible paths never count as actual restoration.
3. **Restored endpoints:** if the capability has the same availability at both endpoints, actual loss and recovery counts agree (`restored_balance`).
4. **No historical erasure:** continuation cannot decrease the interruption already recorded (`continuation_keeps_interruption`). If a restored run contains a loss, it contains both recovery and a positive retained interruption (`restored_loss_is_not_erased`). This is a fact about its history, not an injunction to treat every interruption as wrong.

These results replace the protected-scope attempt's mixed-level account, where immediate gains could be credited repeatedly while eventual losses remained zero. They also replace binary immediate non-loss as the only descriptive output: actual restoration receives its own positive record, while the interrupted interval remains available for assessment.

## 4. Substantive rival within the same finite process

The witness has two states and four kinds of event:

- `close`: the realization becomes unavailable;
- `restore`: it becomes available again;
- `hold`: availability stays as it is;
- `realize`: the activity occurs while it is available.

Every event is eventually realizable from either state (`every_action_eventually`). Thus the **entire eventual activity profile**, not just the selected realization, is identical in both states (`eventual_profiles_identical`). The same law admits these histories:

| Actual history of length `2n` | Losses | Recoveries | Unavailable destination occasions |
|---|---:|---:|---:|
| Repeat `realize; hold` exactly `n` times | 0 | 0 | 0 |
| Repeat `close; restore` exactly `n` times | n | n | n |

Both start and end available, have equal length, and preserve every eventual activity throughout. The second actually restores after every closure. Its interruptions still grow with `n` (`episodes_profile`, `matched_recovery_unbounded`). Therefore **actual return plus eventual preservation does not entail absence of accumulated interruption**. The distinction is generated by actual transitions within the same process, rather than by changing a moral predicate.

A second family remains closed for `n` `hold` events. Restoration remains reachable after every prefix, yet no recovery occurs in that prefix (`eventual_is_not_actual_recovery`). Reachability supplies no finite upper bound on actual postponement. These constructions prove arbitrary finite histories; the result does not claim a law selects one history or establishes observed infinite recurrence.

There is no function of the endpoints alone giving the interruption profile (`interruptions_not_endpoint_determined`). The table also rules out equal-length endpoint plus eventual-profile representations. This directly answers the proposed reduction. It does **not** refute a fuller generative theory that already retains actual interruption, or prove that the continuously available history is ethically better in every interpretation. Closure could realize rest, restraint, protection, or another warranted effect absent from this projection.

## 5. A positive criterion for reasons concerning recovery

The surviving proposal is **actual restoration with accountable interruption / 实际恢复，并对已发生的中断负责**. It has two levels whose relationship must remain explicit.

**Representational criterion, established here.** A claimed restoration of a particular capacity must identify the actual later transition restoring that same relational capacity, at the level at which it was lost. Keep the lost interval in the history. Merely locating a possible route cannot certify recovery; matching endpoint availability cannot certify that the intervening opportunity was realized. A change in the capacity's identity or in what counts as an occasion needs an explicit correspondence. These requirements follow from what the restoration claim purports to describe; they add no independent moral world to the unfolding.

**Bounded practical conclusion, argued rather than formalized.** When a proposal justifies an interruption specifically by saying that a warranted realization will be restored **without leaving anything relevant unmet**, it owes two answers: how restoration actually occurs, and whether the foregone interval itself leaves an unmet claim. If that interval contained a warranted time-dependent realization, citing an identical eventual profile does not answer the claim. An adequate practical justification must instead establish that the interruption is immaterial to that realization, or supply a reason answering the burden—such as protection, a chosen finite commitment, a necessary transformation, or another competing realization. This is a constraint on the adequacy of that offered reason, not an unconditional prohibition of interruption.

The affirmative force is limited but real. **Once a claim to actual or timely fulfillment is independently warranted, mere reachable recovery cannot discharge that fulfillment claim, and subsequent availability cannot by itself show timely fulfillment.** A different claim may require only restored access or an available opportunity. An accessible route can discharge that more limited claim when its conditions are actually met; no further exercise of the opportunity is thereby owed. The kind and deadline of the warranted claim must be fixed before testing, rather than silently changed from access to performance. These are distinctions within the consequence under consideration. No premise that all options or all persistence are good is needed. Equally, the antecedent—why this realization has practical standing, for whom, at what strength—has not been derived by this study. The positive rule transfers an already justified claim through its actual history; it does not manufacture that claim from an event count.

This also supplies a defensible treatment of commitments. A finite undertaking may culminate in an actual completion that forecloses alternatives. The fact of foreclosure should be recorded, while the fulfilled undertaking and its relations can answer whether anything remains owed. Perpetual retention of the unchosen alternatives is not part of the restoration criterion. This avoids the old inference from any option loss to adverse ethical quality. It does not yet solve conflicts among warranted undertakings.

## 6. Counterreview and remaining premise

**Could restoring an available route fully answer the claim?** Yes, if the warranted claim is to access or opportunity and the route actually meets its terms. The no-substitution argument applies to claims of actual or timely fulfillment, not to every warranted claim. It supplies no requirement that people exercise restored opportunities.

**Could a temporary interruption be harmless?** Yes. The profile deliberately does not label it harm. Sleep, anesthesia, maintenance, restraint, rest, or a finite completion could warrant losing immediate capabilities. Their adequate description includes what is realized and protected through the interruption. The result blocks historical erasure, not compensation or overall justification.

**Does the rival preserve the independently specified target?** Yes for the target actually tested: event availability, its actual loss and recovery, the retained eventual profile, and the actual observation occasions. It omits why those occasions matter. Consequently it refutes reduction of that profile, not a fully interpreted ethical identity. Any stronger ethical rival must specify the affected realizations, their constitution, competing effects, and corresponding reasons.

**Is adding the count merely importing a welfare objective?** It would be, if interruption count were silently minimized as the ethical rule. It is not minimized here. It is an additive record exposing a difference that the eventual abstraction omits. The offered practical argument needs independently warranted relevance, not an analyst-supplied scalar reward.

**Does a repaired future compensate the past?** Whether it can answer a past burden is an ethical question. It cannot change the fact that the relevant interval occurred. A constitutive thesis identifying adequate recovery with compensatory fulfillment must explain that correspondence; the numerical equality of loss and restoration events does not supply it.

**What remains supplied?** The transition law; the capability projection in the general result; the actual history; the observation convention; and, for the bounded practical conclusion, the warranted standing and temporal requirements of the realization. In the witness the capability projection is derived from enabling, and the arbitrary family of histories is explicitly constructed. None of this derives the law's unique necessity, universal moral standing, a complete order of competing effects, or motivation to act on a warranted reason. No additional premises are hidden by the empty Lean axiom reports.

**What would change this conclusion?** A proposed eventual-level representation must recover the contrasting actual profiles, perhaps by including retained effects and time-dependent claims in its states. That would enrich the representation; it would not vindicate the bare `Can` reduction refuted here. A philosophical account could establish that a particular interrupted realization has no remaining claim after a specified restoration. It would then justify that particular comparison, rather than prove every actual return ethically cancels every interruption.

## 7. Status, checks, and next bridge

The unfinished **actual-history loss/recovery bridge** is closed at its representational scope: same-level compositional profiles and a precise counterexample decide the proposed reduction. The **protected-scope problem and universal ethical warrant remain open**. [The earlier protected-scope counterexamples](ETHICAL-NATURALISM-PROTECTED-SCOPE.md) all remain preserved: restraint, escape, mutually excluding commitments, symmetric rivals, and unrecorded harms are not purportedly solved by an interruption count.

The [focused checker](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/naturalism/check_actual_recovery.py) builds the unchanged naturalism closure and this module in a fresh temporary directory, checks source hashes against the earlier receipt, rejects warnings and proof placeholders, and requires an empty axiom report for every new theorem. A separate Python reconstruction checks the three history families at `n = 0…100`. The [receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/naturalism/actual-recovery-verification.json) records the actual results. Existing package proofs and receipt remain unchanged.

**Next normative bridge:** choose one independently characterized finite realization—not generic continued inquiry or maximal possibility—and defend why its actual fulfillment or frustrated timing has practical standing in the whole. Test a substantive rival that grants the full generative and experiential organization while denying that claim's force, and compare legitimate completion, protective interruption, and avoidable frustration. This study supplies the correspondence that such a justification must preserve. It does not replace that priority with another mechanism gate.
