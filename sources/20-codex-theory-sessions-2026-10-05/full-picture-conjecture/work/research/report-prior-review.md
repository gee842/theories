# Independent review of the synthesis and the next comparison

5 October 2026. Reviewed `/Users/ren/Documents/Codex/2026-10-05/full-picture-conjecture/outputs/full-picture-synthesis.md` against the prior-results audit and numerical certificates. The report was not edited. This review concentrates on inherited claims and prospective experiment identification, not the separate primary-text audit.

## Overall assessment and requested corrections

The claim summary correctly distinguishes conditional mathematical constraints, finite synthetic results, empirical hypotheses, proposed definitions, and normative commitments. It does not present S01–S06 as one fully integrated model. The selected calculations and proofs inspected are correct under the displayed assumptions: prefix balance, the abundance rescaling, the historical-prediction probabilities, the exact two-sample .85 power ceiling and three-sample certificate, six-round lifetime, and the recovery bridge. The safety-preservation induction is consistent with the stated exact action/observation/predicate contract. Recorded counts of 16 transitions and 396 safety comparisons agree with the saved formal-check output; I did not independently reimplement that whole verifier.

Three corrections should be made before delivery:

1. **Historical compression section: “The question changed” is too strong and can obscure the actual result.** The event being predicted can remain exactly the next need state and the action threshold can stay `.3`. What changes is the admitted temporal model family, so the same old summary loses predictive sufficiency. Suggested replacement: “The records did not become false. The admitted model family changed, making an erased distinction relevant even to the same next-state question.” A separate future-question example can still be cited as U22–U23.

2. **The six-round lifetime sentence needs independent grants.** Say “independent returns of three with probability one half on each active round.” Marginal half-probability alone is insufficient: a random-phase alternating sequence of zero/three grants has those marginal probabilities and no two consecutive zeros, so a cap-two account need not shut down. Alternatively state the full uniform conditional shortfall premise, but independence is shortest for this exact example.

3. **The next-test replay is underspecified.** An external replay is valid only if the schedule is chosen without the recipient's future observations/outcomes, and equality concerns *actual expected expense in the recipient model*, not equal nominal transfers or the donor's expense. The detailed conditions and a concrete protocol follow below. At the time of review no independent next-test protocol with numerical horizons was found; the sentence claiming one exists should point to this review/protocol or be weakened. The earlier `prior-results.md` contains a proposal outline, not a frozen detailed protocol.

Two optional precision changes:

- “An original mapping failure” in the Darwin paragraph can be “A constructed mapping failure.” The example is useful without inviting a novelty reading. If only newborns are counted, explicitly say the next generation consists of those descendants; if parents survive, frequencies would not be exactly zero/one.
- The claim that equal pushed-forward kernels are required for exact stochastic aggregation should specify “for every initial state and permitted action/history.” Strong lumpability is the right contract for that scope. A restricted initial law can support weaker aggregation without satisfying the universal statewise criterion.

## Why a replay can quietly cheat

Let `H_t` be the recipient's permitted history at a support decision, and `U` the policy's random seed, independent of the latent process conditional on declared baseline information. A legitimate feedback rule `g_t(H_t,U)` must be measurable at the time it acts. A calendar `C=(C_0,…,C_{H−1})` is chosen before those future histories, with `C` independent of future recipient shocks given explicitly permitted baseline covariates.

Taking the schedule that an adaptive policy would generate on the *same recipient's eventual trajectory*, then replaying it from time zero, is invalid as a nonadaptive comparator. That schedule can encode future shocks and can reveal them to the recipient controller. Even when the schedule is not announced, its later values can carry this information. Hiding the calendar does not repair the dependence. Same-recipient hypothetical schedules also create cross-world conditioning if changed support changes the histories that generated the schedule.

A valid independent-donor replay samples a schedule from a separate donor trajectory **before** the recipient trajectory is generated. Donor randomness must be independent of recipient shocks. Paired common random numbers may be shared between the recipient arms to reduce Monte Carlo variance, but the donor schedule must not be a function of that shared recipient seed. All controllers must know the relevant randomization/observation protocol; treating a correlated schedule as uninformative would itself be a filtering error.

If replayed transfers must come from recipient production, every prescribed payment still needs a lawful source and sufficient available cash when due. A request that cannot be paid must be handled by a predeclared common feasibility rule. Such a comparator has a nonadaptive *intended schedule* and an adaptive affordability filter; call it that. Financing every replay payment from an unpriced external treasury changes the resource boundary. Choosing schedules after checking which ones are affordable on realized recipient paths is selection on future outcomes.

## Correct meaning of matched expected spending

For a policy `π`, define `C(π)=E_π[Σ_t c_t]`, where `c_t` charges every actual inquiry-related payment at the correct time: diagnostics, readiness, rebuilding, records and communication if present. Define whether support transfers are internal reallocations or final expenditures; count each only once. Use the full law induced by `π`, since a policy changes production, survival, and later opportunities to spend.

Fix the adaptive reference policy and compute its budget `B=C(π_F)` analytically in the known finite model, or estimate it using training trajectories disjoint from evaluation. Then compare it to the best allowable calendar policy under `C(π_C)≤B`, while both enforce identical pathwise cash rules. A policy-level optimization using the supplied population distribution is legitimate; choosing a policy from each evaluation trajectory's future outcomes is not.

To preserve the clean nesting argument, define:

- `Π_F`: readiness/support decisions can use the declared observed history; all sensing and repair rules are nonanticipating and feasible.
- `Π_C`: the same class except the support/readiness schedule is sampled ex ante independently of later recipient shocks. Sensing and ordinary responses may still adapt to their permitted observations.

Then `Π_C⊆Π_F`, provided both have the same allowed external randomization and all other rules. Optimize a declared operating loss under the shared expected inquiry cap, or compare attainable outcome vectors under that cap. Weak adaptive advantage follows from nesting and is not empirical evidence. A strict gap is a conditional value-of-feedback result.

An independently replayed donor distribution is just one member of `Π_C`. Beating it need not mean beating the best nonadaptive allocation. Therefore report both the donor replay and the optimal ex ante calendar lottery. If only donor replay is computationally available, narrow the claim accordingly.

Exact expected-spending equality is possible when the target lies between attainable calendar costs: mix two feasible complete policies with a coin selected ex ante, using `λ=(B−C_0)/(C_1−C_0)`. The component costs must be evaluated in the recipient process, not the donor's. If equality is unavailable or wasteful, report the optimal `≤B` comparison and unused allowance; do not burn resources merely to manufacture a match. A matched expectation does not match pathwise expenditure, timing, harm, or total social burden. Those remain reported outcomes or additional constraints.

“Comparable observation access” should mean identical primitive sensors, visible actions, public funding information and filtering rules. Actual observation transcripts may differ because the intervention changes which tests occur or whether production survives; forcing identical transcripts could remove the very mechanism under examination. If changes in *realized* information are mediators, report them rather than call them matched.

## A rigorous two-period guard with exact matching

Before a larger renewal experiment, use the following complete analytical guard. It has now been arithmetically checked by `prior_schedule_guard.py`; it is not an integrated recurrent-production result.

There are two decision periods. Both arms start with readiness and cash six. Before period zero, the calendar arm samples its retain/drop choice independently of everything that follows. At period zero both observe a fair public signal `S`. There is no current operational problem. If `S=0`, next-period need is certainly absent; if `S=1`, next-period need occurs with probability `.2`. Both know this law. Keeping readiness for period one costs `.1`; dropping it means a rebuild started in period one arrives only in period two, after the final decision.

At period one, an available perfect diagnostic costs one. Treatment after a positive result costs four and prevents loss ten. Without diagnosis, a controller can treat directly or do nothing. Every payment is affordable from initial cash, including the maximum bill `5.1`; no future output funds an earlier expense. The displayed performance comparison separates actual expected inquiry expense from expected treatment-plus-unprevented-loss. There is no other evidence. Observation and ordinary-action interfaces are identical.

The feedback rule keeps readiness exactly when `S=1`, tests then, and treats only a positive. Its expected inquiry expense is `(.1+1)/2=.55`; its expected operating loss is `.5·.2·4=.4`; total `.95`.

For any ex ante calendar lottery, let `q` be the probability of retaining readiness and let `a` be its diagnostic probability conditional on readiness and `S=1`. Testing under `S=0` has no operating value and is dominated. Put `u=qa`. Inquiry expense is `.1q+.5u≥.6u`, because `q≥u`. Operating loss is `1−.6u`. Under the common `.55` expense allowance, `u≤11/12`, so operating loss is at least `.45`. Equality is attained by retaining with probability `q=11/12`, then always testing when `S=1`. Thus both spend **.55**, but the best calendar has operating loss **.45**, versus feedback **.40**.

Simply replaying the feedback arm's marginal retain frequency `.5` is **not** a spending match: the independent recipient replay spends only `.1(.5)+.5(.5)=.30`, because half of its retained capacity occurs when no test is useful. This example detects exactly the comparator error at issue. Its strict `.05` operating-loss difference is established finite decision theory with known purposes and signal laws. It does not show selection of funding institutions, open-ended inquiry, or renewal from production.

## Concrete next experiment after the guard

Use a two-stage test with frozen scope; do not introduce every proposed mechanism simultaneously.

**Stage A — test the projection contract.** Start with the already inspected finite recoverable-inquiry transition model, reimplemented or copied into this task's own directory from the frozen reference. Choose horizon four initially and retain its exact stock states `0,…,3`, cash `0,…,8`, binary readiness, paid rebuild lag, noisy test and ordinary stock evidence. Add a second treasury account and one explicit permission bit that controls same-period transfer; use no record-format, proposal-generation, or strategic-recognition module at this stage. Define transfers as conserving the sum of the accounts, and check expense timing. Freeze two descriptions: the full typed state, and a coarse state retaining only stock, readiness, and total cash. For pairs merged by the coarse map, compute exact attainable vectors of collapse probability, inquiry expense, target-absent intervention burden, and repair completed before a stated terminal deadline. Count an exact difference as failure of the coarse abstraction. Add the permission/access distinction and test every declared action/intervention, not only observed passive trajectories. Both equality and inequality are meaningful results; a state-dependent filter that cannot be represented is a failed closure claim.

**Stage B — test feedback in support allocation.** On the same frozen physical process and horizon, permit the transfer decision either to use current permitted history (`Π_F`) or to follow an ex ante randomized transfer-intent calendar (`Π_C`), with the same public affordability filter. Keep diagnosis and repair adaptive in both. Use the same initial resources and primitive observation channels; every transfer comes from the same recipient treasury. Compute the Pareto frontier of collapse probability and intervention burden at declared actual expected inquiry limits, with no ethical weights inferred from the dynamics. Evaluate a simple independent-donor replay and the best calendar lottery separately. An exact finite occupancy formulation or enumeration must enforce nonanticipation; each policy component's observation history and ex ante calendar are part of its state. Do not condition calendar sampling on the recipient's future signal or survival.

Freeze controls before solving: no hazard onset; uninformative diagnostic; free immediate rebuilding; transfer permission always granted; and a deterministic-support case where all recipients need the same support calendar. A gap attributable specifically to information-based transfer timing should disappear when there is no relevant history variation. No-hazard and uninformative-test controls should reveal unnecessary expense. Free rebuilding removes only the delayed-readiness mechanism; a remaining gap can come from payment access, so it must not be automatically called a failed control. Same initial funds are not a spending match; record all costs and inaccessible overflow.

The next experiment is **unrun**. These are specified implementation targets rather than verified conclusions. The record-format, proposal/admission/enactment, and legitimacy modules should be subsequent interventions after the first omission and policy comparison are validated. A more comprehensive simulator may be useful later, but adding all modules at once would make a failure hard to identify and a successful fit easy to overinterpret.

## Scope and durable checks

No prior source file or synthesis file was modified. This review created only its own records:

- `work/research/report-prior-review.md` — this note.
- `work/research/prior_schedule_guard.py` — exact rational arithmetic for the guard.
- `work/research/prior_schedule_guard.json` — resulting certificate.

The earlier `prior_checks.py`/`prior_checks.json` independently cover the inherited numerical examples. Neither these checks nor a future synthetic comparison establish empirical institutional validity or ethical sufficiency.
