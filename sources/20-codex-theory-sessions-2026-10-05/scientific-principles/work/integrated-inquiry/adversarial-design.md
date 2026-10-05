# Pre-implementation adversarial protocol notes

5 October 2026. These are design constraints and conditional guarantees for the integrated model, supplied before its development freeze. They do not declare an unimplemented experiment successful.

## What the integrated model must actually connect

The proposed connection is experience → review opening → paid evidence → possible rule or mandate revision → different subsequent actions → revenues/costs → maintenance, loss, or reconstruction of inquiry capacity. A new variable for each arrow is insufficient. Every arrow must change an executable transition and have a recorded input.

Use distinct ledgers for cash and performance. Cash enters only through declared external contracts and payments that have actually settled. Predicted future rebates cannot pay today's invoice without an explicit credit facility. Error reduction is not itself money. Maintenance and rebuild costs must be checked before actions execute. Unpaid upkeep must cause the specified capability consequence, not merely be reported as an expense.

A financially closed ledger means there are no unrecorded transfers. It does not mean the institution is physically isolated or earns resources without an external payer. Contract prices and initial capital remain supplied environmental conditions.

## Cheap paired evidence without a hidden counterfactual oracle

When two rules produce predictions and do not alter the outcome, both may issue frozen predictions on the same new service case. One later observed label can score both. This is legitimate reuse: it avoids duplicating outcomes that are genuinely shared, while charging both computations and any additional fields, linkage, or delayed-record retention required by the comparison. It would be invalid if the policies changed the outcome through different interventions.

Let D_t be incumbent weighted prediction error minus candidate weighted prediction error, plus the known difference in their recurring standalone deployment costs. Keep one-time checking/setup expense in the cash ledger and total program evaluation, not invisibly in or out of this per-deployment comparison. A claim about better expected future episodes is distinct from the total value of having conducted the research.

For binary predictions and mandate weights in [0,1], the error difference lies in [-1,1]. If absolute recurring-cost difference is bounded by c_max, then |D_t|≤B=1+c_max. Use the actual per-case bound; do not aggregate many episodes into a needlessly wide ±75 bound. Other weights require a correspondingly adjusted bound.

## A small anytime-valid checker

For a fixed candidate and frozen mandate, choose a small fixed collection of nonnegative betting fractions lambda_l≤1/B before the next observation. Define

E_(l,n)=product_(t=1)^n (1+lambda_l D_t),

and E_n=sum_l w_l E_(l,n), with fixed nonnegative weights summing to one. A grid such as {.05,.1,.25,.5,.75}/B is a supplied testing design, not a learned scientific objective. Log arithmetic is preferable for long streams.

Under the null condition E[D_t | admissible prior checking history]≤0 for every comparison in the review, each factor has conditional mean at most one, every process is nonnegative, and E_0=1. Thus the mixture is a nonnegative supermartingale. The nonnegative-supermartingale crossing inequality gives

P(sup_n E_n≥1/alpha_j)≤alpha_j.

The review may stop for insufficient funds, a deadline, cooldown, or lack of evidence without weakening this crossing bound. A threshold crossing supports a departure from the declared null. It does not promise that a candidate remains superior after an arbitrary distribution shift.

For stationary IID checked cases and frozen rules, the condition reduces to nonpositive expected paired gain. With general drift it is stronger: nonpositive conditional gain throughout the sampled review. Rejecting that composite null does not identify the current or future mean. The synthesis must state which interpretation the implementation uses.

There is a filtration detail with delayed feedback: bets and candidate selection cannot use unrevealed outcomes; delays/censoring cannot selectively expose favorable labels. Preserve frozen forecasts, reveal after a declared outcome-independent delay, and process comparisons in order. Under an exogenous IID case sequence, fixed bets yield the usual crossing bound for the prospective comparison sequence even if other service work occurs while labels are pending. An endogenous sampling scheme or outcome-dependent reporting delay needs its own conditional argument, not an automatic appeal to IID data.

## Lifetime accounting for endogenous review starts

Index all started reviews by j, even if some are aborted or fail. Assign alpha_j=alpha/[j(j+1)]. Since sum_j 1/[j(j+1)]=1, the total allowance is alpha. If the conditional crossing guarantee holds at each adaptively chosen start, conditioning on all earlier history and applying a countable union bound gives

P(any accepted change from a review satisfying its nonpositive-gain null)≤alpha.

Reviews may start in response to observed errors, expenses, demand, or complaints. Those trigger observations may select the question and candidate; they must not be reused as fresh checking observations. A restart does not reset the lifetime counter. Failed reviews may spend no statistical error in fact, but their allocated allowance is not freely recycled without a separately justified method.

Candidate, incumbent, mandate, bound, and compared running costs must remain frozen within a review. A changed purpose cannot retroactively reweight accumulated evidence. Either defer the mandate change, or abort the old review and open a newly indexed one with fresh evidence. The probability guarantee covers the formal error event, not ethical legitimacy or every possible definition of error.

## Checking capability must have an independently specified function

If routine service already retains full linked contexts, labels, and both candidate forecasts, a model cannot claim missing information merely because a checker flag prohibits scoring those records. It must acknowledge a substitute computational route or price the actual necessary work.

One coherent design gives routine service only group-level counts, errors, and expenses. Prospective paid review activates detailed case linkage, additional feature logging where required, and shadow forecasts. Raw linked records are otherwise discarded. The current predictor may consume fields transiently without retaining them. The review facility then supplies a genuine retention and execution capability that aggregate histories cannot reconstruct.

This is still a supplied action interface. Its cost, upkeep, restoration time, and possible substitutes must be explicit. Do not call an imposed organizational prohibition a physical information impossibility. A fixed/free-checker control should reveal exactly which mechanism depends on this capacity, rather than receiving hidden world truths unavailable in all other arms.

## Multi-agent purpose change

The proposed institutional-purpose mechanism can compare predeclared group-specific and inclusive mandates. Separate stakeholders have distinct persistent concerns and observable reports; an explicit decision procedure determines whether the institution adopts a mandate. A mandate must change prospective loss weights, access, allocation, or admission rules. Merely changing a label or rescoring an unchanged history is insufficient.

Retain each group's raw errors, service coverage, delays, and costs separately under every arm. This permits cross-evaluation under old and new mandates and prevents changed objectives from manufacturing apparent improvement. Group membership or need must be accessible through declared records, not evaluator-only world state.

Fixed stakeholder concerns and a fixed constitution mean this is endogenous institutional adoption among supplied purposes. It is not creation of ultimate values or deduction of whose interests matter. A successful vote is not proof of legitimacy. A complaint may justify investigation without being automatically accepted as true or sufficient for changing the mandate.

## Controls and independent validation

At minimum compare the integrated procedure with fixed purpose, fixed review timing, no protected opening, and a fixed-capability or cost-free-checker ablation. Keep contract conditions, environments, and starting resources comparable; report actual expense rather than assuming equal caps mean equal spending. Preserve group outcomes rather than reducing all comparisons to the changing internal score.

Required failure controls include: stable worlds with no need to revise; uninformative extra checking; expensive maintenance/rebuild; substitute evidence routes; delayed or unavailable feedback; a wrong or noisy proposal; a mandate that changes mid-review; income insufficient to preserve capacity; and group interests that conflict instead of yielding unanimous beneficial revision. Every control need not have a large factorial crossing; each must address a real causal claim in the model.

Development seeds may be used to find implementation errors and inspect behavior. After fixing code, rules, thresholds, prices, scenario definitions, horizons, outcomes, and analysis, record a manifest/hash. Then run a separate held-out seed set once. Do not select seeds or alter thresholds to obtain the preferred trajectory. If held-out results prompt revision, label those runs development and create a new independent validation set. Report failures and costs of the proposed mechanism alongside successes.

Paired common environmental streams can improve arm comparisons, but only when actions do not change that environmental component. Shared random numbers must not supply one arm outcomes that it did not actually observe or pay to acquire. Evaluator truth can compute external metrics, but learner state and trigger inputs must remain separate.

## Simpler alternative selected for stationary atomic reviews

If the implemented review samples a controlled stationary environment and uses fixed compiled forecasts, a predeclared paired batch is simpler than the streaming checker above. In a round with one fresh case per group, define

G_i=sum_g w_g(error_inc,g - error_candidate,g) - delta,

where delta is the known difference in recurring deployment cost, positive if the candidate costs more. Let W be the sum of weights for groups on whose allowed contexts the two compiled forecasts can differ. W is computable from forecasts, without knowing the outcome law. Then G_i lies in [-W-delta,W-delta], of width 2W. The deterministic cost shift does not widen the interval.

For n independent checking rounds and a fixed candidate, mandate, and task law, a one-sided lower bound is

mean(G)-2W sqrt(log(1/alpha_j)/(2n)).

This bound targets the mean of the supplied paired comparison. At W=.5, alpha_j=.025 and n=256, its radius is approximately .08488. When W=0, errors agree identically on the allowed domain and gain is the known constant -delta; there is no statistical uncertainty to test for that comparison.

n may be selected using the separate pilot and available funds, but must be fixed before any fresh checking labels are used. Payment failure may abort the batch without acceptance. No acceptance on an early favorable prefix, no enlarging the same checked sample after a disappointing result, and no changing its weights after seeing its results. The lifetime alpha allocation remains available by conditioning on all earlier data at each fresh batch.

Independence need not mean identical distributions for the elementary Hoeffding bound, but then the target is the average of those rounds' expected gains. If a balanced deterministic context schedule is used to estimate a uniform-context target, verify that the complete predeclared batch actually balances the contexts. Random IID contexts per group avoid that bookkeeping distinction. Delayed reports must arrive without outcome-dependent censoring. The world held stationary during an atomic review is a supplied experimental condition; it is not discovered or guaranteed by the learner.
