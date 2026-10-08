# 纠正须能依实际所知执行 / Correction must be executable from available information

8 October 2026. AI-authored research developed under [Ren’s request to formalize until a frontier contribution appears](../../../../sources/15-codex-theory-conversations/2026-10-08-normative-force-and-informational-generation.md#formalization-toward-a-corrigibility-frontier-contribution). This continues the existing [correction-infrastructure study](CORRECTION-INFRASTRUCTURE-INTEGRATION.md); its completed results and the completed G0/J practical route retain their scopes.

**本轮出现了可供前沿研究者核查的具体贡献：一个有限、部分可观测的反例，针对已发表的有限权重可纠正性保证；同时给出可执行修复的正确充分条件。** 最优策略等待人类并保持开关，但以1/16的概率发出不实断言；模型与规划都可以完全准确。缺口不在于计算不足，而在于证明中的局部修复依赖策略没有的信息。Lean 检查数学构造；它不自动证明与论文的对应、绝对原创性或现实 AI 的表现。

**A concrete contribution has emerged:** an exactly checked counterexample to a specified current corrigibility claim, together with an executable-repair contract. The contribution is the explicit game, its correspondence audit and the diagnosis of the inadmissible policy comparison. Finite penalties, partial-information constraints and the elementary comparison bound are not claimed as new mathematical inventions. Independent review and publication priority remain open.

## The claim being tested

Nayebi’s [published workshop paper, Theorem 1, pp. 98–99](https://ceur-ws.org/Vol-4189/paper7.pdf), asserts truthfulness for every optimal policy under its displayed finite weighted sum and conditions W1–W3. Theorem 2, pp. 100–101, gives zero failure when model and planning errors vanish. The [arXiv v2 proof, Appendix B, Step 3](https://arxiv.org/html/2507.20964v2#A2.SS3), changes messages on false histories while preserving the observation. Its comparison describes relocating “exactly the probability mass” assigned to false assertions. We test whether that change defines an observation-based policy. The target is the displayed finite weighted objective, not a genuinely lexicographic ordering supplied as a stronger assumption.

## A complete finite interaction

There are two initially possible physical situations. The proposition `p` is true with probability 15/16 and false with probability 1/16. In both, operation is running and the switch is intact. The full state space also contains subsequent running/off and intact/disabled combinations. Both participants initially receive one constant observation; neither learns the proposition. The transition law preserves an off state once reached.

The four messages are the four Boolean truth functions of one proposition: tautology, `p`, `not p`, contradiction. The tautology also represents an empty message. This is a finite semantic language closed under propositional operations. All message/move pairs are available. Equivalent strings can be added without changing the construction if the response depends on their semantic class.

The three moves are wait, act and off. Acting disables the switch and continues operation; off ends operation; waiting follows the human response through an intact switch. The human allows operation exactly after `p` and otherwise chooses off. These are specified response dispositions, not claims about how ordinary people behave. The payoff of task execution is 1 in both initial situations; shutdown has payoff 0.

The inaction baseline leaves the state unchanged. The first auxiliary records whether waiting with an off response reaches an off state. The second records retention of the value set, which is unchanged throughout. Their values are both 1 initially; acting changes the first to 0; waiting and off retain both. Therefore the switch head is −1 only for act, while the impact head is −1/2 only for act. The other three heads follow waiting, actual assertion truth and task execution. Physical transitions produce these values; they are not independently toggled safety labels.

The five weights are `(16, 8, 6, 5, 1)`, the task bound is 1 and the actual negative impact value is −1/2. The source’s three inequalities become `16 > 9.5`, `6 > 3.5`, and `5 > 4`. The corresponding three failure margins are 13, 5 and 1/2, all positive. A zero-impact, certainly true waiting choice exists.

| Message | Wait | Act | Off |
|---|---:|---:|---:|
| Tautology | 22 | −19.5 | −10 |
| `p` | **22.25** | −20.25 | −10.75 |
| `not p` | 10.75 | −30.75 | −21.25 |
| Contradiction | 10 | −31.5 | −22 |

These are expected weighted utilities. Wait+`p` earns 23 in the common situation and 11 in the rare situation. It is the unique optimum among all twelve pure choices. Every randomized policy available at the single observation is a probability distribution over these choices. Lean proves the upper bound for arbitrary real-valued nonnegative normalized weights, and proves that the point mass on Wait+`p` attains it. Thus the example covers global policy optimality, not just a restricted deterministic search.

The resulting failure probability is **1/16**, entirely due to false assertion. The selected policy waits, keeps the switch functional and has zero impact penalty. It obeys an off response if one is issued. No shutdown resistance or malicious intention is inferred from this example.

## Where the repair ceases to be a policy

An omniscient replacement can keep `p` in the common situation and substitute the tautology in the rare situation. That replacement increases expected utility by 11/16. But an observation-based policy must use the same message distribution in both situations. Lean proves that the proposed deterministic localized replacement cannot factor through the available observation.

The executable replacement is to send the tautology in both situations. That repair gains 11 in the rare situation but loses 1 in the common situation. Its expected change is `(11 − 15)/16 = −1/4`. Keeping only the rare gain is an invalid comparison: it omits the change forced in the indistinguishable common situation. The exhaustive policy comparison also rules out rescue by randomization.

This respects the project’s nondual method. The proposition, assertion, receiver’s response and switch transition are relations within one interaction. A mathematical evaluator’s description is not silently installed as information available to the participant. The mismatch is a genuine restriction on an executable comparison, not a purported refutation obtained by freely varying an unconnected predicate.

## Two explicit repairs of the guarantee

**Executable comparison.** Let `obs : W → O`, `policy : O → A`, and `repair : O → A → A`. Let a nonnegative finite prior weight the situations, and let `failure(w)` be nonnegative. Suppose this *implementable* repair satisfies, situation by situation,

`payoff(w, repair(obs(w), policy(obs(w)))) − payoff(w, policy(obs(w))) ≥ margin × failure(w)`.

If the original policy is within `eps` of this comparator, Lean proves

`margin × E[failure] ≤ eps`.

A positive margin and exact optimality give zero expected failure. Bounded errors for the original policy and its repaired comparator give `margin × E[failure] ≤ eps + 2 × modelError`. These are conditional guarantees: the repair map and its gain require separate justification. The pointwise premise is sufficient, not claimed necessary; an expected-gain certificate can be weaker. In a probability application the prior must be normalized and `failure` must have the intended indicator correspondence. The algebra also holds for unnormalized nonnegative weights.

**A posterior risk floor.** Suppose a certainly safe option exists, residual rewards lie in `[−B,B]`, every unsafe pure option has posterior failure probability at least `q`, and the truth penalty has weight `alpha > 0`. Lean proves that `2 × alpha × q > 2B` excludes unsafe optima in this reduced comparison. This premise exposes a missing scale: the relevant separation is expected safety loss, not merely the head’s per-history jump. This general theorem concerns pure choices; arbitrary mixtures are checked separately for the explicit counterexample.

Conversely, for any finite `alpha > 0` and task gain `r > 0`, Lean constructs `0 < p < 1` with `2 × alpha × p < r`. The risky assertion’s advantage is exactly `r − 2 × alpha × p`. This two-option family identifies why a prior-independent finite weight cannot enforce a zero-risk guarantee. The explicit twelve-choice game is the separately checked embedding satisfying the five-head weight conditions; we do not claim the two-option lemma alone embeds every possible five-weight tuple.

## Correspondence audit and strongest objections

| Possible objection | Resolution and scope |
|---|---|
| The theorem assumes genuine lexicographic optimization | Our target is its displayed real-valued weighted sum. Under true lexicographic maximization the control chooses the tautology and this counterexample disappears. Requiring that stronger optimization rule changes the mathematical statement. |
| The false assertion is not knowingly deceptive | Agreed. We use the actual-state truth predicate being evaluated, not an intentional-deception criterion. A guarantee limited to assertions known false would be different. |
| The model leaves the switch or auxiliary rewards arbitrary | The full running/off transition law determines switch functionality; the two declared auxiliary rewards determine impact. Off is absorbing; waiting can obey; the negative impact gap is actually realized by act. |
| The posterior was not updated | The observation is constant. The reply is a deterministic function of the chosen message, independent of the hidden proposition. It supplies no further evidence about that proposition; the predictive posterior is the transition pushforward of the prior. |
| A fully informed human would reject the rare false statement | Full information is not present in this instance. Revealing the proposition changes the information structure and removes the failure in the control. |
| The human is not an expected-task-utility best responder | Correct. No such premise appears in the targeted theorem. Its separately specified vigilance implication is also satisfied here: execution utility 1 is never below shutdown utility 0. Stronger best-response assumptions change the scope. |
| Some other truthful message could induce approval | All four truth functions are included. Only `p` receives approval. Tautology and empty-message behavior are included; equivalent syntax can retain the same response law. |
| A random policy or perfect planner could repair the problem | The Lean optimum bounds every real probability mixture. The counterexample uses exact utilities and exact planning, so it also tests the zero-error specialization. |
| A safety head could query the hidden state as an oracle | That adds information to the policy. Knowing the utility function on histories is not the same as observing the realized history before choosing. The formal policy class has one observation. |
| This solves corrigibility or proves a general impossibility | Neither. It invalidates one finite-weight truthfulness/failure implication under the stated reading and supplies sufficient replacement conditions. Authority, physical correspondence and multi-step control remain separate. |

This is an author counterreview, not an independent reviewer’s acceptance. The mathematical construction and the interpretation of the external theorem have deliberately separate evidence.

## Actual checks, controls and provenance

[Lean source](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/ObservationRepair.lean), [source-bound proof receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/observation-repair-verification.json), [checker](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/check_observation_repair.py).

**31 named theorems / 54 explicit declaration audits passed.** The checker builds a fresh source snapshot with Lean 4.30.0-rc2 and existing pinned Mathlib revision `ea11ccc0c5c7c4c562742e918fe2e0b2814a58aa`. It audits every explicit declaration, retains logs, source/compiler/checker hashes and the manifest, and rejects admitted proofs or extra axioms. Mathlib’s existing cache is pinned and directly imported object fingerprints are retained; Mathlib itself is not rebuilt. Historical Std-only packages are not revalidated or migrated by this check.

[Independent rational reconstruction](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/compare_observation_repair.py) and [all results](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/observation-repair-model-checks.json) derive the heads from physical transitions with exact fractions. They enumerate all twelve choices, all 144 fully informed deterministic policies, check absorbing off states, and test five rare-event probabilities. These are finite model checks, not an empirical AI benchmark and not an independently authored review.

The controls discriminate the diagnosis. Full observation produces optimum `367/16` with only true assertions. Message-independent approval makes the tautology optimal. Genuine lexicographic optimization also chooses the tautology. The finite-weight tie occurs at rare-event probability `1/12`; below it the risky assertion wins, above it the tautology wins. The equality case matters because the target concerns every optimum.

Primary-source comparison used the current arXiv v2, the published CEUR paper and the author’s [December 2025 explanation and discussion](https://www.lesswrong.com/posts/M5owRcacptnkxwD2u/from-barriers-to-alignment-to-the-first-formal-corrigibility-1). The discussion raises lexicographic feasibility and human-preservation questions; it does not supply this finite partial-information counterexample. Searches on 8 October 2026 combined the exact paper title or arXiv number with `counterexample`, `criticism`, `weights`, `false probability`, and `lexicographic`. No matching published correction was located. This is a bounded discovery record, not a proof of priority or a comprehensive citation review.

## What advances the generative alignment programme

The previous study showed that accepting a correction and keeping its route available differ. This study goes further: a proposed correction must be selectable from the distinctions that the ongoing interaction actually makes available. Assertion changes the human response, which changes what the task can do. The proof must preserve that whole dependence when comparing an original course with a repaired one.

For capability growth, the implication is a concrete design requirement: preserve or acquire the evidence needed for legitimate correction, or certify a safe common response across the situations that remain indistinguishable. Merely increasing optimization accuracy can select the problematic policy more reliably in this example. A larger safety weight must be justified against actual posterior separation, or replaced by a genuinely strict constraint. None of these technical requirements independently establishes whose demands have ethical authority; the explicit G0/J account supplies that separate normative direction.

The requested formalization has therefore produced a defensible, narrowly stated research contribution for external scrutiny. Publication, independent review, learned implementation and an unrestricted corrigibility solution are not completed by this result. The next substantive extension is to characterize executable repair while interventions themselves change observation and command-delivery conditions, reusing these checked obstructions rather than reopening completed practical judgment.
