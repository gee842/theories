# Selection audit: adoption, continuation, and succession

Research audit, 5 October 2026. This cycle connects the existing feasibility models to specified selectors and transmission mechanisms. It does not derive inevitable improvement, inevitable preservation of repair capacity, moral authority from persistence, or a universal empirical theory. The earlier [universality audit](../cycle-3/universality-audit.md) explains the larger scope.

## What this cycle can genuinely explain

A fixed finite-horizon decision rule can genuinely model **endogenous adoption of infrastructure**: installation, retention, or abandonment becomes an outcome of the current state and the rule. Calling the rule an optimizer does not invalidate it as a behavioral mechanism. The model should state that the objective, horizon, information, and computational implementation are supplied assumptions.

That is different from explaining why the decision rule itself was adopted. Four levels should remain distinct:

| Level | Explicit modeled object | Claim justified |
|---|---|---|
| Feasible capacity | Existentially quantified admitted controller | A successful policy exists |
| Actual choice | A specified selector `σ` acting on its permitted information | This system chooses these actions under the supplied rule |
| Learning or institutional amendment | An update mechanism for estimates, objectives, horizon, or selector code | These aspects of the rule change through specified feedback |
| Population selection and transmission | Contributions, copying/influence, mutation or transformation, and a population update | Some variants become more or less represented through this specified process |

There is no requirement to endogenize every assumption before making useful predictions. Every model has an outer semantics. The improvement is to identify which formerly unexplained choice has become an outcome and which rule remains a boundary assumption. A perfect externally calculated policy can be a declared benchmark. It becomes the actual system's behavior only if access to that decision procedure is assumed or modeled.

## A common semantic contract for selector comparisons

Hold the physical process, starting configuration, disturbance realization or declared distribution, action menu, observation interface, and payment order fixed when comparing selectors. Include clocks and existing apparatus in that starting configuration. Changing the horizon and quietly changing initial cash, free information, or installation state would compare different systems.

An actual selector can choose an attempted action that fails. It must not receive only the actions lying inside the infinite viability kernel unless that protective filter is explicitly part of its implementation. Otherwise long-run solvency has already been imposed on the selector being tested for short-term failure.

For each decision rule, specify:

- what is scored: output, withdrawals, terminal cash, welfare, survival, or another quantity;
- which outcomes and costs enter the score, including costs borne after turnover;
- horizon, discounting, terminal value, and terminal constraints;
- whether the plan is committed to or recomputed after each observation;
- how exact ties are resolved, using the same rule across the comparison;
- which model and observations the selector possesses, and whether computation or search is charged or supplied as a boundary assumption.

These are mechanism parameters, not inconvenient qualifications. They determine the predicted choice.

## Finite horizons: the discriminating issue is the omitted continuation

A short planning horizon does not by itself imply bad maintenance decisions. Immediate effects may justify maintenance; a good terminal value can summarize distant consequences; and a certified terminal region can keep later choices feasible. Conversely, a longer horizon does not automatically optimize the external evaluator's objective or correct a wrong environment model.

An elementary benchmark makes the distinction precise. In a discounted stationary finite decision process, let `V*` be the infinite-horizon optimal value for the same reward and admissible controls. A finite-horizon calculation with terminal value `V*` returns `V*` at every backward step because `V*` is a Bellman fixed point. Thus even one-step planning with that exact continuation value selects an infinite-horizon optimal action. This is a mathematical benchmark, not a claim that an actual system knows or can afford to calculate `V*`.

The useful intervention therefore separates **horizon length**, **terminal continuation treatment**, and **available model information**. If only the zero-terminal-value short-horizon selector fails, the result supports that specified truncation mechanism. It does not establish a universal disadvantage of every short-horizon implementation.

Model predictive control already supplies precise examples where finite optimization is combined with terminal conditions to guarantee a continuing property. Chen and Allgöwer use a terminal cost and region in a particular nonlinear control scheme. Its restricted stability result motivates the terminal-condition control here; it does not establish solvency or institutional stability for our renewal process. [Chen and Allgöwer, 1998](https://www.sciencedirect.com/science/article/pii/S0005109898000739).

### Accounting and horizon traps

1. **Count flows and terminal assets consistently.** If the reward already includes the net change in cash, adding all final cash can count the same gain twice. If the reward is withdrawals or delivered output instead, retained cash can be a distinct terminal asset. State the intended objective rather than calling every expression “profit.”
2. **Retain prefix feasibility.** A positive projected terminal balance cannot finance an earlier installation fee. Receipts, expenses, capacity limits, and overflow must have the same order in the selector's forecast and actual execution.
3. **Expose cash-cap effects.** Spilled surplus can make extra earning valueless under a terminal-cash objective. This may create broad ties or make costly maintenance appear free at the cap. That is a property of this supplied financial objective, not necessarily a physical benefit.
4. **Specify the horizon boundary.** A failure at the first excluded step, a cost payable just after turnover, and a completed duty followed by safe retirement are distinct events. An indexing convention should not decide the substantive result accidentally.
5. **Distinguish commitment from replanning.** A planned delayed installation may be postponed again whenever the horizon moves. Verify the realized trajectory, not only the initial optimal plan.
6. **Check all tied optimal actions.** If the reported collapse depends on an arbitrary tie-breaking convention, show that dependence. A strict ranking or an all-ties conclusion is stronger evidence for the proposed mechanism.

## Learning is an update process with a survival problem

Changing an action because a known model and state changed is adaptive control in a broad sense, but it is not necessarily learning. A learning claim needs an estimated object, an observation/update rule, retained state, and a relationship between acquired evidence and later actions. Perfectly solving the true model afresh after each episode does not test whether the actor can learn that model.

Watkins and Dayan provide a clean contrasting example: their tabular Q-learning rule updates action values from experienced transitions. The convergence theorem assumes a specified Markov setting, suitable learning rates, bounded rewards, and repeated sampling of every state-action pair; samples need not form one uninterrupted trajectory. It is not a theorem that a resource-limited learner survives while exploring. [Watkins and Dayan, 1992](https://www.gatsby.ucl.ac.uk/~dayan/papers/cjch.pdf), §2 and theorem.

That distinction is particularly important here. An absorbing bankruptcy state can prevent further experimentation. Restarting failed episodes with fresh capital supplies an additional recovery mechanism. If such resets are used, record their source and cost; otherwise compare learning subject to the same physical solvency constraints. A guarantee of eventual value convergence conditional on endless data cannot substitute for a guarantee of continued access to that data.

Learning efficiency, viability while learning, and long-run optimality are separate tests. The present cycle need not solve all three. It should say which one its mechanism actually studies.

## Succession, transmission, and selection

At turnover, distinguish what crosses the boundary:

- physical assets and liabilities;
- permission and execution access;
- records, retained estimates, or a compiled policy;
- a rule label, horizon, or preference parameter;
- the source-selection and interpretation procedure used by the successor.

A inherited label does not automatically give the successor its predecessor's information, assets, or authority. Conversely, replacing the incumbent does not erase information still carried by public prices, the apparatus state, a clock, or another participant. The previous paid-memory models already demonstrate why retention and usable access must be distinguished.

Copying a selector from one incumbent to one successor is inheritance. Differential survival can change the composition of surviving organizations. Differential reproduction or imitation can change representation through contributions to new selectors. These are different mechanisms. Report absolute population size or number of surviving organizations alongside trait frequencies: an increasing share of a variant can coexist with severe population decline.

For a population update, define a contribution weight `w_i≥0` and a successor-type kernel `K_i(j)` for each current carrier. A generic normalized update has the form

\[
x'_j=\frac{\sum_i x_i w_i K_i(j)}{\sum_i x_i w_i},
\]

when the denominator is positive. This bookkeeping form does not explain the weights or kernels. They require a mechanism—observed payoff, reproductive output, election, imitation, training, or another stated process. It also does not specify absolute population growth; that requires its own update. If total contribution is zero, extinction cannot be hidden by normalization.

The Price-equation literature already separates selection from transmission effects. El Mouden and colleagues make that distinction for cultural traits and stress that influence is trait-specific. Neither generic social status nor organizational survival is automatically the correct contribution weight. This paper supplies conceptual distinctions, not an empirical endorsement of a turnover mechanism in the current toy process. [El Mouden, André, Morin, and Nettle, 2014](https://onlinelibrary.wiley.com/doi/full/10.1111/jeb.12296), definitions and transmission discussion.

### Selection need not preserve viability

The general inference “a successful variant spreads, therefore the population becomes more viable” is invalid without a bridge between contribution and the protected function. A variant can gain influence before its deferred costs are realized; an individually favorable change can alter a shared environment; learning can transform the transmitted rule. Which possibility occurs depends on the specified mechanism.

There is direct biological prior art against an unconditional adaptation-to-persistence inference. Gyllenberg and Parvinen analyze evolutionary processes leading from a viable population to extinction and give model-specific conditions and exclusions. The publisher abstract supports this limited precedent; its detailed theorem is not imported here. [Gyllenberg and Parvinen, 2001](https://www.sciencedirect.com/science/article/pii/S0092824001902538).

The current models should make their own more limited claims from their own transition rules. The biological example does not prove that every institution, economic system, or AI population follows the same mechanism.

## Discriminating controls

| Control | Hold fixed | What it discriminates |
|---|---|---|
| No future fault or harmless fault | Physical operating costs and supplied selector objective | Whether maintenance is useful only under the modeled disturbance duty |
| Free, equally timely alternative repair | Fault sequence and evaluation | Whether failure concerns one infrastructure route rather than a universal need for that carrier |
| Correct continuation value or certified terminal region | Short horizon and physical process | Horizon truncation versus limited lookahead with adequate continuation information |
| Commitment versus repeated replanning | Initial forecast, objective, and horizon | One-time investment ranking versus repeated postponement |
| Inherited rule with erased estimates, then estimates restored | Assets, authority, and fault process | Transmission of a label versus usable decision knowledge |
| Neutral copying versus payoff-weighted copying | Physical payoffs and initial type frequencies | Transmission alone versus differential influence |
| Same copying rule with longer outcome-measurement window | Physical process and inherited types | Immediate score advantage versus deferred maintenance costs |
| Safe ending or handoff | Physical costs, liabilities, and rights respected by that ending | Continuing one carrier versus fulfilling the declared duty |
| Exact proportional replication | Ratios, per-module cash, objective scaling, and observation access | A genuine scale correspondence versus an unscaled reward or fixed absolute fee |

The safe-ending control must be declared before evaluating outcomes. Supply an executable retirement, shutdown, or handoff action whose safety and outstanding obligations are checked. Reclassifying accidental collapse as a successful ending after seeing the result would not be a meaningful control. Likewise, a no-hazard case need not retain infrastructure whose only modeled purpose is hazard response.

These controls can produce null or reversed effects without weakening the underlying accounting and information constraints. They identify the domain of the selection mechanism and prevent “more maintenance” from becoming an unstated moral objective.

## Independent audit of this cycle's supplied mechanisms

### Rolling investment on the shared-repair process

The root model keeps the previous `n=8,c=1,p=4,u=2` repair process, uses exactly periodic fault onsets eight slots apart, and permits channel purchases at 30 per additional channel at a cycle boundary. Removal is free and destroys the removed channels; there is no resale value. Starting cash and cap are 240. These changes must remain explicit: the deterministic forecast is not the earlier guarantee against every allowed fault schedule, and installation/adoption is now an action.

An independent boundary-state enumeration covered all `241×9=2,169` states `(cash,installed channels)`, using payment-feasible cycle edges. Its greatest fixed point and finite-horizon calculations agree with the root checker:

| Initial state | One-cycle preferred plan | Two-cycle preferred plan | Indefinite continuation feasible? |
|---|---|---|---|
| `(240,0)` | Install 2; end at 140 | Install 4, retain 4; end at 136 | Yes |
| `(140,2)` | Retain 2; end at 100 | Upgrade to 3, retain 3; end at 78 | No |
| `(88,4)` | Retain 4; end at 96 | Retain 4 twice; end at 104 | Yes |
| `(101,3)` | Retain 3; end at 85 | No feasible two-cycle plan | No |

The exact viability frontier is

\[
b\ge88+30\max(4-k,0)
\]

for installed channel count `k∈{0,…,8}` and carried-cash cap 240. Four channels are the only design with nonnegative full-cycle increment. Reaching that design requires the missing channel fees plus its 88-unit repair reserve. Before reaching it, every feasible cycle loses cash, and detours cannot reduce the total missing-channel purchase cost. If it is never reached, the uniformly negative increments eventually exhaust any finite reserve. Conversely, buy the missing channels—or freely discard any excess—and repeatedly use four; the cash increment is eight per cycle, capped at 240.

This yields a stronger conclusion than delayed realized bankruptcy. The one-cycle selector's first choice leaves `(140,2)`, below the 148 needed to reach four channels. It has already destroyed indefinite continuation capacity. The two-cycle selector leaves `(128,4)`, within the invariant region `k=4,b≥88`. For starting cash from 208 through 240, the short-horizon first choice similarly leaves the viability region despite viable initial resources.

The root code now gives an explicit response to forecast infeasibility: use the longest shorter feasible horizon, and fail only when no complete repair is payable. This resolves the distinction between lack of a two-cycle plan and immediate physical inability to repair. At `(101,3)`, one cycle still works; the planner must not label its unavailable two-cycle forecast as an already missed payment.

The most useful succession control is already present in the invariant check: the one-cycle selector also retains four channels once they exist. It can inherit a viable apparatus and continue, even if it does not inherit the longer horizon. This model therefore distinguishes adoption financing from ongoing maintenance and physical-asset inheritance from rule inheritance. Resetting apparatus to zero at turnover would require a separate physical replacement mechanism.

I inspected the root planner, its shorter-horizon fallback, its cycle-to-slot expansion, its fixed-point calculation, and the saved results. The independent calculation above used compressed cycle edges; the root checker separately checks microstep ledger consistency. The reported no-hazard control increases the cash cap to avoid saturation ties and declares this changed comparison. The safe-ending control changes the declared duty to a single completed cycle with permitted costless closure. Neither should be presented as an unchanged infinite-continuation task.

### Actual-rule transport and paid transmission

The [selection-and-scale memo](selection-and-scale.md) correctly transports actual closed-loop transitions instead of replacing the concrete selector with a better existential controller. Its joint event/state kernel condition preserves correlations, not just one-time output frequencies. The finite-horizon total-variation bound `min(1,δ+Nε)` follows from sequential coupling and a union bound; it does not imply an infinite-horizon sure guarantee. The planner correspondence correctly requires preservation of feasible candidate trees, positive affine score comparisons, tie order, and subsequent updates.

I checked the example's four-state controlled safe set, mutation timing, and probability formulas. Starting with the reserve-preserving rule, survival through `N` cycles requires `N−1` successful handoffs, giving `(1−μ)^(N−1)`; the expected failed-cycle index is `1+1/μ` for `μ>0`. The final successful cycle's transmission can cause failure only in the next cycle. The same financial plant still admits a safe controller, but this does not give its installed corrupted program a free self-replacement operation.

The audit requested explicit finite event alphabets for pointwise kernel sums; that clarification is now in the memo. For continuous event labels, equality must instead be formulated for measurable sets. No other substantive proof issue was found. This example models transmission fidelity, not differential population reproduction or selection.

### Paid regime learning and infrastructure adoption

The paid-learning checker constructs the posterior from the joint regime mass of the **final physical register**, rather than giving the selector the analyst's observation history. The same persistent hidden regime determines conditionally independent probe observations and the later deployment fault. The prior, likelihood family, candidate measurement protocols, and score are supplied; the learned object is the regime posterior.

In the base case the low regime has zero fault probability, so a positive OR bit identifies the high regime and an all-zero OR bit identifies the unique all-zero sample pattern. Given the publicly fixed sample count, OR is sufficient for the deployment decision; an exact count has no additional information there. The overlapping-regime control correctly creates a situation in which one and two positive samples imply different decisions and the count register can improve the result.

The checker separates actual cash from an imputed failure loss and checks branchwise conservation. With initial cash eight, the expected-score winner takes a `1/40` failure risk, although unconditional maintenance is affordable at total cash cost at most seven and handles every admitted deployment fault. This is a valid contrast between different criteria, not evidence of a computation error or irrationality. The finite episode does not establish recurrent learning finance or long-run survival. No substantive issue was found in the inspected posterior, memory-channel, or cash calculations.

## Prior-art and access register

| Primary source | Evidence actually inspected | Use here and limit |
|---|---|---|
| Chen and Allgöwer (1998), [*A Quasi-Infinite Horizon Nonlinear Model Predictive Control Scheme with Guaranteed Stability*](https://www.sciencedirect.com/science/article/pii/S0005109898000739), DOI 10.1016/S0005-1098(98)00073-9 | Primary publisher abstract; a full-paper mirror was retrieved but later text access failed | Terminal-condition precedent only; no detailed theorem imported into the cash process |
| Watkins and Dayan (1992), [*Q-learning*](https://www.gatsby.ucl.ac.uk/~dayan/papers/cjch.pdf) | Author-hosted full PDF, update mechanism, convergence theorem and its sampling conditions | Explicit learning precedent and assumption audit; no safe-exploration guarantee asserted |
| El Mouden, André, Morin, Nettle (2014), [*Cultural transmission and the evolution of human behaviour: a general approach based on the Price equation*](https://onlinelibrary.wiley.com/doi/full/10.1111/jeb.12296) | Full publisher HTML, definitions, transmission decomposition, limitations | Selection/transmission distinction; no general empirical maximization claim imported |
| Gyllenberg and Parvinen (2001), [*Necessary and Sufficient Conditions for Evolutionary Suicide*](https://www.sciencedirect.com/science/article/pii/S0092824001902538), DOI 10.1006/bulm.2001.0253 | Indexed primary publisher abstract and author-institution metadata; direct publisher open failed | Existence of a relevant model-specific countertradition; full proof not inspected |

These ingredients are established prior art. The contribution under investigation is the explicit coupling and testing of a selector, renewal process, and succession mechanism with consistent information and payment semantics. No priority claim is made.
