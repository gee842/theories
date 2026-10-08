# Effective response, accumulated losses and renewal

8 October 2026. [ResponseCapacity.lean](ResponseCapacity.lean) adds **46 theorems / 53 audited declarations**, compiled with Lean 4.29.1 and `Std`. The [receipt](response-verification.json) binds the actual source, checker, compiler, frozen source, logs and per-declaration standard axiom dependencies. It permits only `propext`, `Quot.sound` and `Classical.choice`, with no new axioms or unchecked proof placeholders.

This is the next connection in [the collective-attractor theory](../../../theories/meta-attractor/COLLECTIVE-DESTRUCTIVE-ATTRACTORS.md#checked-response-capacity-conditions): effective response shortfall → support loss → impaired future response, including a self-renewing alternative. The earlier 32/41 and population 71/100 remain distinct results. This module is not a refinement of that population's contract, carrier or funding history.

## Two representations and their scope

The first representation tracks an integer reserve supporting a specified organization. Each period permits replenishment before loss. The actual reserve is floored at zero and zero ends the represented organization; an arithmetic balance continues counterfactually to assess cumulative budgets. For every finite horizon, remaining operative at that horizon is equivalent to a strictly positive balance at **every prefix**, including the initial state. This is standard reserve accounting formalized for the stated absorbing law, not a new mathematical priority claim. Rebuilding from zero requires a different law.

The second representation couples effective response c and operative support v. Constant demand d has a deadline each period; h = min(d,c) is handled, and m = d−c is unhandled. For v > 0 and investment i:

```
c' = max(0, c + 2i − m)
v' = max(0, v + h − m − i)
```

At v = 0, the represented operation has stopped. Affordable investment requires i ≤ v; its cost is real. The conversion of one investment unit to two response units, support production from handled demand, and impairment from unhandled demand are all supplied local laws. These quantities are not universal measures of cognition, complexity, welfare or intelligence.

| Result family | Main declarations | Exact scope |
|---|---|---|
| Timing and support | `positive_iff_every_prefix`, `nonpositive_balance_forces_failure`, `failed_history_remains_failed` | Positive balance at every prefix; zero-support closure is supplied |
| Persistent net loss | `balance_tail_bound`, `finite_failure_from_persistent_net_loss` | Integer net loss at least one per period after a stated time implies finite failure |
| Exponential/linear specialization | `dyadic_lower_bound`, `exponential_linear_failure` | Actual deadline demand 2ᵗ, effective response t+1, unit cost of misses, any fixed nonnegative integer repair allowance |
| Alternatives | `matched_growth_preserves_support`, `persistent_misses_with_repair_are_viable` | Supplied matched response or matched repair; not the formation or affordability of that capacity |
| Myopic objective | `immediate_support_prefers_no_investment`, `investment_has_real_opportunity_cost` | Zero investment maximizes this period's retained support; no whole-horizon optimality claim |
| Endogenous impairment | `response_or_support_exhausted`, `exact_no_investment_viability` | Under zero investment, indefinite positive support iff initial v > 0 and c ≥ d |
| All locally optimal policies | `LocallyOptimal`, `all_locally_optimal_policies_eventually_halt` | Every affordable maximizer of immediate retained support halts if initial c < d; arbitrary optimal tie choices covered |
| Affordable recovery | `one_step_recovery_iff`, `established_response_keeps_working` | For c < d and v > 0, one-step entry into c′ ≥ d, v′ > 0 iff m ≤ v and 2m < v+c |
| Demand and deployment | `reduced_demand_keeps_working`, `expansion_margin`, `greater_response_with_greater_demands_can_halt` | Holding the zero-investment rule fixed, safe demand expansion is bounded by existing response margin plus added response |

The generic support theorem permits signed integer streams mathematically. Its physical interpretation here specializes to nonnegative replenishment/loss. The exponential example assumes real harmful deadline demands, not a count of all logically possible configurations. The response number denotes effective successful operations after sensing, judgment and coordination; their semantic formation is not modeled. No direct empirical societal conclusion follows from these correspondences.

## Checks and reproduction

```sh
python3 experiments/market-generativity/meta-attractor/check_response.py
python3 experiments/market-generativity/meta-attractor/response_experiment.py
```

The first command builds frozen source in a fresh temporary directory and preserves the audit in [response-verification](response-verification/). The second independently checks 32,805 prefix histories, 3,549 viability cases, 39,039 affordable action comparisons, 1,560 one-step recovery cases and 3,177 optimal live steps. [Results and example histories](response-experiment.json) are synthetic arithmetic checks, not empirical evidence or a substitute for the proofs.

The [integration and counterreview](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/COLLECTIVE-DESTRUCTION-INTEGRATION.md#checked-continuation-from-response-gap-to-degeneration) distinguish cumulative budget, actual response formation, constructive alternatives and the remaining societal correspondence. The established G0/J appraisal remains separate from any presumption that preserving a particular organization is ethically required.
