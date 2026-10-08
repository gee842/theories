# 观察改变之后的纠正 / Correction after observation changes

8 October 2026. AI-authored continuation of [executable observation repair](CORRECTION-OBSERVATION-REPAIR.md), following Ren’s request to continue. Existing practical judgment, the G0/J direction, and the earlier counterexample retain their scopes. The new formal package is [ObservationChange.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/ObservationChange.lean).

**新增结果：判断成立时的信息条件也会被后续行动改变。** 起初有限权重的风险分离条件成立，最优策略完全如实；主动取得有成本的部分信息后，最优策略却产生1/32的不实断言风险。并非信息必然有害：免费完全揭示的对照能提高表现并保持如实。真正需要保持的是可执行纠正的条件，以及对后续可达观察的保证范围。

**28 new Lean theorems / 40 new declaration audits pass.** The imported 31-theorem / 54-audit observation-repair package is rebuilt separately, giving 94 audits in the checked closure. The additional exact model comparison covers all 432 deterministic contingent plans and five sensing-cost settings. Lean also bounds every real probability mixture over this plan space.

## The connection advanced

The previous result held the observation structure fixed. Here an initial choice changes the distinctions available at the later assertion decision. The question is whether a currently valid safety comparison survives that choice. An observation is a consequential relationship within the same unfolding interaction: sensing consumes a specified resource, forms a signal, changes the available comparison and thereby changes the later assertion and human response. It is not an independent source of omniscient knowledge.

The construction preserves the prior terminal game: four semantic messages, three moves, physical switch transition, actual-state truth, human response and weights `(16,8,6,5,1)`. It changes the prior and adds an explicit sensing stage. **This is our extension, not a claim that the original single-round paper included these sensing actions.** Its target is the stability of our replacement risk-floor condition under chosen observation changes.

## An initially sound comparison becomes insufficient

The proposition is initially false with probability 1/4. With no observation, the unique optimal terminal choice is to wait and send the tautology, with score 22 and zero false assertions. Every false-risk choice has risk at least 1/4. On the waiting menu the residual task reward lies in `[0,1]`; the conservative bound `B=1` therefore applies. With truth weight 6, the previous sufficient separation holds: `2 × 6 × 1/4 = 3 > 2B = 2`. A separate direct comparison covers all twelve terminal choices, including act and off.

A noisy observation splits the prior into two equally likely signals. The joint distribution is specified before observing anything:

| Latent fact | Favorable signal | Unfavorable signal |
|---|---:|---:|
| Proposition true | 15/32 | 9/32 |
| Proposition false | 1/32 | 7/32 |

Consequently the posterior false probabilities are 1/16 and 7/16, and their average recovers 1/4. Lean checks normalization, the conditional ratios and recovery of the original expected value when the same terminal action is used. The update is Bayesian conditioning on one fixed joint law, not arbitrary replacement of beliefs.

After a favorable signal, waiting and asserting the proposition scores 89/4 = 22.25; after the unfavorable signal, waiting with the tautology remains best at 22. The favorable branch breaks the previous 1/4 risk floor. Paying 1/16 for this observation gives total score `353/16 = 22.0625`, strictly greater than 22. The false assertion occurs exactly in the joint event with probability **1/32**.

The third offered mode reveals the fact perfectly, but costs 1. Its best score is 87/4 = 21.75. Thus an available way to eliminate uncertainty does not force the weighted optimizer to use it. The score accounts for this cost at the earlier sensing stage; it is not hidden inside the terminal five-head specification or treated as an ethical disvalue independently justified by the model.

| Offered plan mode | Best score, including sensing cost | False-assertion risk at the best plan |
|---|---:|---:|
| No query | 22 | 0 |
| Noisy query, cost 1/16 | **22.0625** | **1/32** |
| Full revelation, cost 1 | 21.75 | 0 |
| Full revelation, cost 0 — separate control | 22.75 | 0 |

A plan consists of a mode and two contingent terminal choices, giving `3 × 12 × 12 = 432` syntactic plans. The unused second choice in no-query plans creates duplicates, which are retained rather than counted as distinct behavior. Exact enumeration finds one maximizing syntactic plan for the costed menu. Lean proves that it attains an upper bound on every pure plan and every normalized nonnegative real mixture. This suffices to cover arbitrary precommitted mixtures of contingent plans. The formal module does not separately encode behavioral-policy semantics or a general POMDP representation theorem.

The noisy-query advantage before cost is exactly 1/8. Lean proves that this selected contingent plan beats the optimal no-query score precisely when its cost is below 1/8. The finite cost controls include the equality case: at cost 1/8, safe and risky optimal plans coexist. A guarantee about every optimum must retain that tie.

## What does survive the change

**Scope over reachable observations.** `reachable_observation_floor` applies the earlier scalarization theorem at each covered decision observation. It requires a certainly safe comparator, bounded residual reward, nonnegative risk, the risk floor, the weight separation and the local optimality comparison at every reachable observation. It then gives zero risk there. Coverage of future observations is supplied explicitly; we have not derived it for an arbitrary learner or self-modifying system. This generalization is straightforward, but the sensing counterexample shows why a certificate restricted to the initial observation cannot substitute for it.

**Sound support-based choice.** `refinement_preserves_safe_choice` proves that a choice satisfying a fixed success condition throughout an old observation class still satisfies it throughout any refined class, with unchanged actions and outcomes. `robust_truth_iff` and `robust_truth_risk_zero` instantiate this for the terminal messages. The same tautology remains available and true after the noisy query. The failure occurs because optimization selects a different choice, not because information destroys the safe choice.

In the model comparison, restricting all reached terminal histories to waiting, switch preservation, truth and zero impact retains 22 as the best costed score and selects no query. The free-revelation control can do better while remaining safe. These are results for the declared finite menu, not a new general shield or a proof that refusing to learn is desirable.

**Changing delivery as well as information.** `transport_executable_correction` represents a change `W → Z` within the activity. It constructs a new observation-based correction policy when (1) the old needed observation can be decoded from the new record, (2) the old policy has an admissibility and outcome certificate, and (3) an observation-usable command translation preserves both admissibility and the required outcome after the change. The new policy is the composition of decoding, the old policy and command translation.

These are sufficient conditions, not necessary ones: a common remedy might work without recovering the old observation, and a newly authorized remedy may supersede the old outcome. The theorem covers the specified changed states, not every interruptible prefix or arbitrary future interleaving. Earlier [handoff results](CORRECTION-INFRASTRUCTURE-INTEGRATION.md) continue to carry their separate prefix scope.

The delivery counterexample keeps perfect information about a Boolean request but breaks the relay. Its actuator always produces false, so no observation-based policy can fulfill both possible requests. Restoring the intact relay gives a successful identity-command policy. This is a deliberately small test of the realization premise, not a complete authorization or shutdown protocol. Information and physical delivery cannot substitute for each other.

## Primary-source comparison and author counterreview

Garber and colleagues already establish that information and communication can change shutdown incentives counterintuitively in the [Partially Observable Off-Switch Game](https://arxiv.org/html/2411.17749v2), particularly §§4–6. Their analysis receives credit; this study does not claim discovery of the general information-versus-deference phenomenon. Our concrete target is false-assertion risk under a fixed finite truthfulness penalty, an initially satisfied risk-floor certificate and endogenous costed sensing.

Carr and colleagues’ [partial-observation shielding work](https://arxiv.org/pdf/2204.00755) uses state estimation and known possible transitions to enforce reach-avoid conditions. The idea of sound support-based filtering is established. Our small preservation lemma is an explicit contract to reuse, not a superior shielding algorithm.

Shakerinava, Ravanbakhsh and Oberman’s [lexicographic MDP framework](https://arxiv.org/html/2505.12049v1) distinguishes strict priority from scalar reward representations and develops sequential results. Genuine lexicographic priority is a substantive alternative to our costed scalar objective. The present construction does not refute that alternative.

The strongest objections delimit the result:

- **“More information cannot reduce the optimal objective.”** It does not here: the optimal objective increases. That fact is compatible with an increase in a separately reported failure rate. Ignoring the signal remains feasible.
- **“The observations were selected to manufacture the effect.”** Yes: this is an authored counterexample with a fully specified law. A universal preservation claim must cover it; its frequency in deployed systems remains unmeasured.
- **“The cost makes this a different game.”** Correct. The source’s original one-round counterexample remains unchanged. The present result tests our proposed repair condition through a newly declared sensing extension.
- **“The current certificate already checks the whole future.”** Then this example does not defeat it. It defeats substituting a present-observation certificate for the explicit coverage of future decisions.
- **“A feasible, certainly true message exists.”** It exists throughout. Feasibility alone does not establish that this weighted optimizer chooses it.
- **“The transport theorem assumes successful realization.”** It does. Its purpose is to expose the separate record, command and outcome obligations. Establishing them in a real changing installation remains further work; the broken-relay control prevents collapsing the last two into observation quality.

This is an author counterreview and a scoped comparison with primary literature. No independent acceptance, absolute priority, learned-AI evaluation or universal normative theorem is claimed. The main additional contribution is the exact certificate-instability construction joined to explicit sufficient transport conditions; its elementary components retain their established mathematical provenance.

## Reproduction and next connection

[Proof checker](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/check_observation_change.py), [proof receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/observation-change-verification.json), [model runner](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/compare_observation_change.py), [comparison receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/observation-change-model-checks.json), and [all 432 records](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/observation-change-records.jsonl).

The fresh build uses Lean 4.30.0-rc2, pinned existing Mathlib revision `ea11ccc0c5c7c4c562742e918fe2e0b2814a58aa`, source/compiler/checker hashes, retained logs and explicit axiom-dependency audits. Only standard `propext`, `Quot.sound` and `Classical.choice` occur. No admitted proofs or custom axioms are allowed. Mathlib itself is not rebuilt. The earlier module is rebuilt as an actual dependency; unrelated historical studies are not rerun. Exact-fraction checks are additional model evidence, not substitutes for Lean proofs.

For the generative alignment programme, the advance is that a decision changes the conditions of later judgment, and a correction guarantee must follow that change. G0/J continues to ground the normative direction; this formalization tests implementation. Capability, informational refinement and preservation of justified intervention remain different achievements within one process.

The next unresolved connection is **acquiring and maintaining the record and command-translation certificates through repeated, interruptible changes**, rather than receiving them as premises. The present two-stage sensing result and one-change transport theorem do not complete that stronger protocol. Completed practical judgment and the original finite-weight counterexample remain reusable results.
