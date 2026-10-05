# Repeated revision of a carried admission rule

Executed follow-up, 5 October 2026. This extends the single-change study without altering its audited implementation. The new files are `repeated_revision.py` and `repeated-revision-results.json`.

## Result

The implemented learner changed the same admission clause in both directions as its task distribution changed:

**Require single-field improvement → allow pair search without it → require it again → allow pair search again.**

The current rule is carried into each subsequent study. The learner's choice follows observed priced prediction losses on exploratory tasks and a separate fresh check; hidden task labels do not enter its decision functions. After each choice, 32 new tasks are actually processed with the installed rule.

This demonstrates repeated, outcome-sensitive revision within a supplied grammar. It does not demonstrate an autonomous decision to begin studying its standards, discovery of new goals, or invention of the meta-validation procedure.

## What was fixed before execution

One script specifies three externally scheduled phases: randomized deterministic interaction tasks, independent fair-label tasks, then randomized deterministic interactions again. The investigator receives ordinary context/label observations rather than a message naming the phase. The environment generator implements the shifts. The only editable clause is the prefix-improvement requirement; the grammar toggles it symmetrically. The requirement of final training improvement and the local validation test remain fixed.

Seeded pseudorandom generation supplies reproducible simulated sample paths. Independent sampling is a condition of the probability model and its theorem, not an empirical conclusion established by these paths.

Each phase has 128 discovery pairs. Fixed fresh checking counts are 256, 8,192, and 256. The larger middle check addresses the smaller expected advantage of returning to restricted search. Each phase uses significance level `.05/3`. Distinct disjoint streams come from one fixed seed, `7140301`, with fixed phase/stage offsets. There was one execution, no search over seeds, no continued sampling until acceptance, and no reuse of earlier checking outcomes.

The task loss, price list, base model grammar, and 64-prediction horizon are inherited from the single-change study. Separate budgets of 17,000, 340,000, and 17,000 units are supplied externally. Conservative reserves include every possible priced study payment and 32 post-decision task executions: 16,048, 334,440.32, and 16,048 units. Meta-editing and checking arithmetic remain unpriced as declared in the original toy model.

## Actual transitions and costs

| Phase | Externally supplied task law | Carried prefix rule | Fresh checking mean gain | Lower bound | Total priced expense, including post-decision tasks |
|---|---|---|---:|---:|---:|
| 1 | Randomized deterministic interactions | Required → not required | 20.6900 | 7.2209 | 11,704.96 |
| 2 | Independent fair labels | Not required → required | 2.9756 | .5946 | 232,716.12 |
| 3 | Randomized deterministic interactions return | Required → not required | 20.6900 | 7.2209 | 11,704.96 |

Total priced expense is **256,126.04** units. The middle reversal is expensive under the chosen conservative checking procedure. Nothing in the model claims that a real researcher should pay this amount or that this is an efficient meta-learning algorithm.

The post-decision executions confirm enactment. In phases 1 and 3, the installed unrestricted pair search proposed and adopted a useful rule on all 32 tasks, making zero errors over 2,048 predictions per phase. In phase 2, the restored restricted search made 14 proposals, adopted none, and made 1,003 errors over 2,048 independent-null predictions. Error near one half is appropriate for that law; the benefit of the restricted procedure is its lower cost, not prediction of independent noise.

The separate exact evaluator gives expected gain 20.69 for each move to pair search under interaction tasks and 3.000078125 for the reverse move under independent-null tasks. The middle checking estimate 2.97560302734375 is consistent with that exact mean. The learner never receives these evaluator quantities.

## Why the three-check claim remains valid

At the start of each fresh check, condition on every earlier event, including the carried rule, prior acceptances, discovery outcomes, and supplied phase schedule. The selected alternative and sample count are then fixed, and the next checking pairs are independent draws from the declared stable within-phase law. Each bounded paired-loss difference lies in `[-75.31,75.31]`.

The one-sided Hoeffding lower bound therefore wrongly certifies a nonpositive mean gain with conditional probability at most `.05/3` in each phase. A union bound gives probability at most `.05` of any such false acceptance across these three scheduled checks. Independence among the three acceptances is unnecessary. This statement is conditional on the declared data-generating and observation assumptions. Arbitrary within-phase drift, outcome-dependent extra tests, or a continuation beyond the three allocated checks is outside the claim.

This familywise guarantee is distinct from the earlier single-change study and its follow-up. It belongs to this newly specified three-phase protocol; it does not retroactively combine all experiments in the research session into one error budget.

## Expense and utility are not interchangeable

The reported 256,126.04 is every priced acquisition, candidate-fitting, and deployment-field payment, including post-decision executions. Routine prediction errors enter the loss criterion but are not debited from the cash reserve. Useful predictions made while studying may have value; their value depends on the counterfactual service requirement.

The output records therefore also retain matched-service comparisons: an incumbent supplying both prediction streams versus one incumbent and one candidate stream. Interaction-phase comparisons are exact; the independent-null comparison uses observed outcomes and is only a descriptive estimate, because the same reports selected the rule. No new inference is made from that reused accounting. If those service blocks were not needed, if alternate services existed, or if losses did not convert into available funds, the economic interpretation changes. The prototype does not optimize how often to run meta-studies or renew its own study budget.

## Explanation supported by the mechanism

A methodological rule can be rationally expanded when it blocks informative models and contracted when its extra searches consume resources without improving predictions. Accordingly, development of science need not be a monotonic movement toward either more permissive or more restrictive procedures. Which change is warranted depends on task structure, costs, horizon, and available evidence about the procedures themselves.

The protected recurring route is essential here. After phase 2, if the returned prefix rule also acquired exclusive authority to decide whether phase 3's meta-probe could open, the deterministic interaction plateau would block the return to pair search. That counterfactual follows from the independently checked lockout result. Carrying a reviseable admission rule is therefore different from preserving the route by which it can be reconsidered.

The recurrence mechanism itself remains supplied: scheduled protected probes, external replenishment, a symmetric edit grammar, reliable outcome access, fixed error allocation, and fixed loss. The next genuine frontier is explaining when those enabling practices are maintained, changed, or lost, while avoiding a hidden designer who always supplies the needed intervention at the needed time. This example establishes repeated revision inside that boundary; it does not erase the boundary.

The independent audit in `repeated-revision-audit.md` exactly replayed all three records, checked expense/reserve arithmetic and rule carry, instrumented calls to verify that the incumbent stayed fixed during each comparison and that post-decision tasks used the changed rule, and confirmed no observations were acquired under zero funding. No code correction was required for this extension.
