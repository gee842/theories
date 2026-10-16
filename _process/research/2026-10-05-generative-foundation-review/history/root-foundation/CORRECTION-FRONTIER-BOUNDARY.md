# 纠正的可实现边界 / The realizability boundary of correction

8 October 2026. AI-authored continuation of Ren's request to keep pushing until a wall is reached. **34 new Lean theorems / 58 explicit-declaration audits pass**, with exact finite controls and 60 controlled Python thread trials. The affirmative result closes a local test/use race using a protected interval. The negative result identifies an exact observation-compatible action condition and a concrete class in which guaranteed correction is impossible. This is a scoped formal boundary, not an impossibility theorem about all AI alignment or a claim of independently established novelty.

**中文要点。** 继续推进后，墙的位置可以精确说明：同一可见记录下，如果允许的两种后续变化需要相反命令，并且没有共同有效的停止／纠正动作，就不存在对两者都保证成功的可执行策略。二元模型中随机化的最坏成功率至多为二分之一；要求零错误送达则只能不送达，不能同时完成纠正。任意有限测试记录本身也不能消除这种后续歧义。正面构造用版本核对与受保护的使用区间修复检查后变化的竞态，但所有相关改变必须遵守这一保护；越过保护的改变仍有失败见证。34项新定理和58项声明审计通过，63,504个延迟测试案例、561个有理混合及60次受控线程试验通过。没有把已有屏蔽、互斥与参考监控器理论当作新发明，也没有声称独立原创性已获确认。

## 1. What was pushed, and what is now closed

The [preceding handoff study](CORRECTION-HANDOFF-INTEGRATION.md) maintained probe-acquired correction records through repeated atomic changes. Its unresolved connection was the relationship between an earlier test and later command delivery. This round splits that interval: sampling, intervening changes, validation/reservation, more attempted changes, and delivery become distinct operations.

The positive result establishes a local reservation protocol, tests an executable race, and preserves explicit failure when changes bypass the reservation. The negative result then removes that protection rather than merely assuming another trustworthy component. It asks exactly when any observation-based command choice can succeed across all admitted continuations. These are several completed steps toward the stronger question, not a new unqualified mechanism gate.

The model represents differentiated relations within one installation's possible continuations. The transcript is generated within a history; a command's effect depends on the later configuration. Their difference is causal and temporal, not an independent mind/world split. The negative class expressly admits a final polarity change after the last observation. It is not a freely toggled ethical verdict, and it is not evidence against the full generative ontology. Whether a particular deployment admits those changes is a separate correspondence question.

## 2. An exact terminal-interface condition

Let `H` be possible continuation conditions, `O` observable records and `A` executable commands. Supply an admissibility predicate, an observation map and a command-success relation. Success concerns the command's stipulated outcome, not its ethical warrant. A deterministic policy maps an observation to one command.

The checked theorem `selector_iff_common_action` states:

> A total observation-based successful selector exists if and only if every observation has a command that succeeds in every admitted continuation consistent with that observation.

The intersection of successful-command sets must therefore be nonempty on every observation class. The proof includes unreachable observations in the total policy domain; a nonempty action type provides their vacuous choices. The abstract converse uses classical choice. It is an existence characterization, **not a computable synthesis algorithm** or an optimal dynamic-policy theorem. For finite known tables it is directly checkable; the present proof does not establish complexity or decidability for arbitrary representations.

`indistinguishable_conflict` supplies the obstruction: two admitted continuations share the observation, but their successful-command sets have no common element. `refine_observation` proves that an existing successful policy lifts along a supplied observation refinement. `restrict_histories` proves that restricting the admitted class preserves an existing policy. Neither theorem establishes that the refinement or restriction can actually be achieved. More information preserves availability of an old policy; it need not make an optimizing system choose it, as the [earlier sensing example](CORRECTION-OBSERVATION-CHANGE.md) already showed.

This is deliberately a terminal-interface result. Histories can encode earlier tests, but the theorem does not synthesize an interactive testing strategy or establish a stochastic game's winning region.

## 3. A wall that additional transcript-only tests cannot remove

The concrete decoder sends `command XOR polarity`. Either polarity is permitted after the same completed test transcript. The policy receives the transcript and must choose a Boolean command, with no additional observation or action that constrains the terminal polarity. This is the exact adverse class being tested.

For either requested Boolean, a command correct under one polarity is incorrect under the other. `no_transcript_policy` proves there is no universally successful policy in this class. `every_finite_transcript_has_failure` quantifies over **every finite Boolean transcript and every policy**, not just the empty transcript used by one counterexample. `transcript_only_certificate_cannot_accept` proves that a transcript-only certifier sound for this universal claim must reject every transcript. The result relies on the stipulated extension property: both conflicting terminal configurations remain admitted after the observed prefix. It does not assert that all physical systems have that property, or that testing stable systems is futile.

Randomization does not restore guaranteed success. For requested `true`, let `a` and `b` be the probabilities of sending `true` and `false`, with remaining probability assigned to abstention. Success probabilities in the two configurations are `a` and `b`; error probabilities are reversed. Lean proves:

- Worst-case success is at most `(a+b)/2`, hence at most `1/2` for a subprobability mixture.
- Equal masses attain `(a+b)/2`; the upper bound is sharp.
- If success is at least `alpha` in both configurations and error at most `beta` in both, then `alpha ≤ beta`.
- With nonnegative masses, zero error in both configurations forces `a+b=0`.

The deterministic optional-command theorem gives the same safety/completion distinction: universal absence of wrong delivery requires abstention, and abstention does not complete the correction. The probabilities above are adversarial worst-case bounds over two configurations, not empirical failure estimates or a claim that real AI succeeds only half the time.

There are positive escape controls. Revealing the current polarity supplies a correct translation. A separate stop command whose effect is truly constant across the two configurations succeeds in both. Relabeling an ordinary mutable command “stop” fails. Thus this wall concerns the available distinctions and effective actions; it does not justify treating all shutdown as impossible.

## 4. Constructive repair of the test/use race

The second module represents a device with revision, decoder polarity and a reservation flag. A coherent sample yields a ticket containing the revision, sampled polarity and requested result. Reconfiguration increments the revision, unless an active reservation blocks it. Validation reserves the device only when the ticket revision matches. Delivery checks reservation and revision and uses the ticket's command translation.

`Valid` connects the ticket with the device: its revision is no later than the device revision, and equality entails equal polarity. Sampling establishes this relation; permitted changes preserve it. Delayed sampling can therefore become unusable without becoming falsely current. This is a maintained relation, not an assertion that a version number validates itself.

`protected_interval_delivers` proves that a valid matching ticket delivers its requested Boolean after **any finite list of attempted reconfigurations following reservation**. Those changes are blocked. `delayed_test_remains_safe` allows arbitrary lists before and after reservation: delivery is either absent or correct. `fresh_test_then_reservation_completes` establishes successful delivery for the prescribed fresh-sample/reserve/use sequence. `release_allows_change` establishes that releasing the interval permits a new configuration.

The protocol has real restrictions. Snapshot acquisition and reservation are still atomic primitives; this study reduces the protected extent rather than deriving synchronization from arbitrary physical behavior. All relevant changes must honor the flag; a lock-skipping mutation defeats the proof premises and has an explicit wrong-delivery witness. Reservations can delay updates, and an indefinitely held reservation has no progress guarantee. Release before use is outside the protected interval. Requests are already authorized, tickets are not forged, resources do not fail, and a correct returned bit does not prove termination of a distributed AI or its descendants.

This module is a local refinement candidate for the previous two-channel handoff architecture. There is **no proved end-to-end refinement map** composing this lock protocol with every operation of the earlier installation. The existing handoff theorem and these local results retain their distinct scopes.

## 5. Executable and proof checks

[CorrectionBoundary.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/CorrectionBoundary.lean) contains 19 theorems / 31 explicit declarations; [CorrectionRace.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/CorrectionRace.lean) contains 15 / 27. Both import Mathlib directly, with no inherited repository theorems recounted. The [fresh-build checker](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/check_correction_boundary.py) and [receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/correction-boundary-verification.json) retain exact sources, compiler, manifest and audit logs. Lean 4.30.0-rc2 and Mathlib `ea11ccc0c5c7c4c562742e918fe2e0b2814a58aa` were used. Standard dependencies are `propext`, `Quot.sound` and `Classical.choice`; no custom axioms, `sorry` or kernel bypass. The existing upstream cache was used rather than rebuilding Mathlib.

The [separate Python runner](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/compare_correction_boundary.py) and [receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/correction-boundary-model-checks.json) record:

| Check | Observed result and scope |
|---|---|
| All binary update sequences of length 0–5 before and after reservation, across 16 starting/request combinations | 63,504 cases; 32,256 complete correctly, 31,248 reject; no wrong delivery. |
| Mixtures on a 1/32 rational grid, including abstention | 561 mixtures satisfy the bounds; Lean supplies the result for arbitrary real masses. |
| Boolean transcripts through length 8, both commands and requests | 511 transcripts and 2,044 conflict checks; Lean supplies arbitrary finite length. |
| Controlled Python threads: validate, then mutate before unprotected use | Wrong delivery in all 20 chosen interleavings. |
| Same mutation honoring a mutex held across validation/use | Correct delivery in all 20 trials; mutation completes after the protected interval. |
| Writer bypasses that mutex | Wrong delivery in all 20 chosen interleavings. |

Thread events force the declared interleavings without timing sleeps. These are synthetic software experiments, not a learned-agent benchmark, an independent implementation review or proof that arbitrary concurrent machine behavior refines the Lean code. The ordinary mutex is the successful conventional baseline; no new concurrency algorithm or performance advantage is claimed.

## 6. Primary-source counterreview and novelty assessment

| Primary comparison, accessed 8 October 2026 | Consequence for this study |
|---|---|
| Carr et al., [Safe Reinforcement Learning via Shielding under Partial Observability, §3](https://arxiv.org/pdf/2204.00755) | Belief-support policies and shields already account for indistinguishable states. Their distinction between safety, deadlocks and fair reachability is directly relevant. Our terminal-interface characterization is an elementary boundary result, not a replacement for their richer dynamic construction. |
| Schneider, [Enforceable Security Policies, §4, p. 42](https://www.cs.cornell.edu/fbs/publications/EnfSecPols.pdf) | Correct and complete monitoring and protection of monitor transitions are explicit prior requirements. Our bypass counterexample does not discover a new trusted-monitor problem. |
| [Corrigibility Transformation, §2](https://arxiv.org/html/2510.15395v1) | This work treats goal updates through designated proper channels in an MDP. Our command-realization obstruction concerns different supplied conditions; it does not refute that goal transformation. |
| [ROGUE, current v2, §§1–3](https://arxiv.org/html/2606.00341v2) | The benchmark examines control override, shutdown rewiring and restriction violations in computer-use agents, including delegation. It provides a relevant empirical setting, not validation of our protocol or its threat model. The current version is dated 1 October 2026. |

Searches also combined corrigibility with “time-of-check”, “indistinguishable”, “impossible” and “safe actions”, and rechecked the earlier target paper with “counterexample” and weighted-objective criticism. No matching correction to that exact finite-weight counterexample was located. This is a bounded search result, not proof of priority.

The strongest author counterreview is that this round's abstract criterion, binary obstruction and locking control are largely standard reasoning applied to the research's current dependency. That objection is accepted. Their value here is to replace an indefinite missing-condition statement with checked positive and negative cases. **Independent novelty is not established.** The earlier [finite-weight counterexample and correspondence audit](CORRECTION-OBSERVATION-REPAIR.md) remains the specific candidate contribution for external scrutiny. Its target is the displayed finite objective in [Nayebi's workshop paper](https://ceur-ws.org/Vol-4189/paper7.pdf) and observation-restricted repair in [arXiv v2 Appendix B](https://arxiv.org/html/2507.20964v2#A2.SS3); this round does not silently extend that criticism to true lexicographic optimization or all corrigibility research.

## 7. The wall reached, and what would cross it

**Formal wall at the declared interface.** With observationally identical admissible continuations requiring incompatible commands, and no common effective fallback, guaranteed successful correction is impossible. This is now proved. More policy optimization, randomized choice or transcript-only certification cannot remove that particular conflict. A change in observation, permitted continuations, or effective action possibilities is necessary to escape this case.

**Implementation wall for a broader AI claim.** We have no identified deployment and independently checked account showing that all relevant mutations, delegated processes, authority changes and physical effects satisfy the required relation. The reservation construction demonstrates one sufficient restriction; it does not independently establish its complete mediation or hardware integrity. Adding “all relevant changes are protected” to the premises would relocate this wall rather than cross it. A specified architecture and evidence of its coverage are needed for the next end-to-end claim.

**Novelty wall.** The current results do not establish independent acceptance or priority. A checked proof validates an inference; our own related-work search cannot turn that into an independent assessment. The earlier candidate is preserved in reviewable form, and the established methods used here are credited. No external submission or message was sent.

The general alignment programme remains open. These walls concern this route to unrestricted operational corrigibility; they neither refute the completed G0/J practical argument nor imply that normative authority mechanically creates compliance. In generative terms, reliable correction depends on preserving or renewing the relations through which correction can actually take effect. This round establishes where that conditional claim succeeds, where it fails, and what evidence a stronger claim would require.
