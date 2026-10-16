# Recoverable inquiry: exploratory finite decision study

5 October 2026. AI-generated study under Ren's direction. This protocol records the implemented design and the declared comparison run after development; it is **not a preregistration**. No empirical observations or random simulations are used. Initial development with H=5 and burden budget .6 selected no paid tests. A subsequent H={5,6,8}, budget={.02,.05,.1,.15,.2,.6} sweep is preserved in `development.json`, including all no-testing results. H=8, budget .02 selected rebuilding and testing; it was chosen for an explanatory trace after seeing this result. `development-h8-detail.json` records the same case following a numerical speed improvement. No inference from parameter frequencies to real-world prevalence is intended.

## Question and scope

When can an institution let paid inquiry rest while retaining an affordable route to restore it? Couple noisy evidence, stock regeneration, endogenous production receipts, paid readiness with a rebuilding lag, and an explicit expected cumulative intervention/testing burden. Fixed purposes, repair technology, correct known probabilities, free belief retention, and a finite horizon are supplied. This module does not inherit earlier experiments' candidate-generation ability automatically.

## Information and chronology

The controller observes remaining periods, stock x in {0,1,2,3}, cash b in {0,...,8}, diagnostic readiness r, and a rational posterior p for the hidden binary fault. Initially H=5 in the original config, x=3,b=8,r=1,p=0. The main comparison changes H to 8 and varies only the declared burden budget.

1. Pay one to keep existing readiness, or drop it free. If not ready, rebuilding costs three and becomes usable only **next period**. Rebuilding cannot enable an immediate test.
2. If already ready and upkeep was paid, optionally pay two for a binary diagnostic with sensitivity and specificity .9. Bayes-update on its outcome. A preliminary design used truthful-or-erased observations; it was replaced before implementation with this genuinely noisy diagnostic.
3. Choose repair, possibly conditional on that diagnostic, at cost three. Direct repair without diagnosis is always in the action set if affordable. All expenses must fit opening cash on every branch.
4. Repair u resets the current fault to zero. Draw damage D with probability .1 if healthy, .8 if faulty; observed next stock is clip(x+1+u−2D,0,3). Zero stock is absorbing, so later income and actions end. This irreversible boundary is stipulated.
5. Receive income 2x' after expenses. Retain at most eight cash; overflow goes to treasury and cannot finance later actions. Update once from the joint law of observed stock and income. Income is deterministic from stock and not a second independent signal.
6. Hidden fault changes: healthy→fault .1; fault→healthy .05. If the posterior after production is q, next p=.1+.85q. Thus even a recent negative finding ages.

The full joint distribution, including clipping and repair's effect, is used. Rational arithmetic computes observation probabilities and beliefs; floating-point dynamic programming evaluates costs. No latent realized-error counter is visible to the policy.

## Objective and burden

Minimize expected sum(expense−output) −2*terminal_stock +12*I(terminal_stock=0), subject to expected sum[I(repair and pre-repair fault absent)+.05*I(test)]≤budget. This is a **finite-horizon ex ante expected burden**, not FDR, a probability of any error, a pathwise cap, or a lifetime guarantee. Repair can improve stock even without the target fault; a target-absent repair is not necessarily mistaken or net harmful. Its assigned burden and the test disruption are explicit evaluative choices. Cash costs and this burden have different units. The cost objective includes failure loss; the burden budget alone is not a complete welfare measure.

Cost has no terminal cash bonus because net cash flows are already included. Terminal stock is assigned salvage value, an explicit horizon assumption. Cash conservation on each branch and in expectation is: final cash − initial cash + treasury + expense − output = 0. Physical resources enabling stock renewal lie outside this small model; endogenous revenue does not imply a thermodynamically closed economy.

## Decision solution and comparisons

Enumerate the finite reachable belief-state DAG. Bellman recursion solves each nonnegative Lagrange multiplier with declared lexicographic tie-breaking. An ex ante lottery between two deterministic policies meets the expectation constraint; each component need not meet it separately. The best dual lower bound is recorded against the lottery's feasible cost, with a target gap 1e−8. Report the actual gap, not an unqualified exact arithmetic optimum. A separate lexicographic minimum-burden solution identifies restricted-mode infeasibility. An infeasible comparator has no reported feasible cost.

Modes share starting resources, ordinary information, production, and repair technology, but may spend different amounts:

- `adaptive`: choose readiness, tests and contingent repair freely within the model.
- `no_test`: same direct repair and ordinary stock/output information, no paid diagnostic. Positive-cost unused readiness is available but not artificially rewarded.
- `continuous`: compulsorily keep/rebuild when affordable and test whenever ready and affordable. Optimize repair responses. This is a compulsory-service benchmark, not the best calendar or all possible continuous policies. At the initial state its first test alone incurs .05 burden, so tighter budgets may be infeasible.

The main H=8 budget grid is {0,.01,.02,.03,.05,.1,.2,.4,.6}. Controls at budget .02, H=8 use adaptive mode and change one condition: onset=0 (known absent fault), sensitivity=specificity=.5 (uninformative paid test), initial cash=2, initial stock=1, output per stock=1, initial readiness=0. The original H=5/budget .6 case remains a separate declared control. This is an exploratory selection, not an exhaustive sensitivity analysis. Comparing different initial stock cases does not isolate liquidity; comparing adaptive and no_test does isolate the option to pay for diagnosis within the chosen technology.

Save all configurations, mode minima, metrics, reachable policies for the main .02 example, and selected traces. A trace is a deliberately selected possible history, not a representative random trajectory. Its conditional component probability is not the total chance of restarting. 'Test after an untested period' does not by itself mean a prior paid negative test followed by resumed testing; inspect the actual actions before assigning that interpretation.

## Verification and limits

Independent tests enumerate latent events, compare small-horizon Bellman/lottery values with occupancy linear programs or direct action mixtures, check prefix cash and observation chronology, verify rebuilding lag and direct repair, and test infeasible burden bounds. The input manifest preserves the exact code/config/protocol used for each output directory. Do not overwrite existing result directories.

The finite DP does not implement the separate robust viability recursion, continuous bridge-liquidity certificate, or indefinite alpha-spending result in the mathematical memo. It permits collapse under an expected-loss objective. It does not prove a safe infinite-horizon stationary policy, an institutional attractor, universal optimal inquiry, or an AI alignment solution.
