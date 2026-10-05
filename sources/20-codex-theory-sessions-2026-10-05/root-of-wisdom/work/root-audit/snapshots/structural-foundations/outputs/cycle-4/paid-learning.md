# Paid learning that changes an implemented selector

5 October 2026. The earlier studies distinguished feasible correction from what an actual selector chooses. This module supplies a concrete learning mechanism: a finite controller pays for observations, retains a specified statistic in a physical register, updates its posterior over an unknown regime, and uses that posterior to decide whether to maintain a corrective apparatus. The observations change the implemented decision; the analyst does not substitute the true regime for them.

This is a finite Bayesian study with exact rational calculations. It does not claim that expected-score optimization supplies a sure-safety guarantee. A low-reserve example makes that distinction consequential rather than merely verbal.

## 1. The physical episode and the unknown object

A persistent hidden regime `Θ∈{H,L}` determines the frequency of a fault. The supplied prior is `P(H)=π`. Conditional on that single regime, the probe observations `Y₁,…,Y_N` and the later deployment fault `Z` are independent Bernoulli variables with parameter `p_Θ`.

The learner does not know `Θ`. It does know the prior, the two likelihoods, the candidate actions, and their costs. What is learned is **which supplied regime is more plausible**, not the likelihood family, a new concept, an objective, or a new repair procedure.

Before deployment it can choose between:

- **Maintain:** pay `m` to keep local diagnostic readiness. If the deployment fault occurs, the known diagnose–authorize–implement protocol restores the function for a further cash bill `C` within its deadline.
- **Do not maintain:** pay no readiness fee. On a fault, a substitute provider can perform timely repair for cash bill `A`. If that bill cannot be prepaid, repair fails and the declared evaluation assigns consequence `L`.

The local route has the same simple physical interpretation as the earlier recurrent-repair model: ready diagnosis, authorization, and indicated implementation can restore production, with their support expense included in `C`. The substitute is explicitly retained; maintenance is not made valuable by deleting every alternative. Both service routes meet the declared three-slot repair deadline when funded. Fault occurrence is visible, and the specified repair services supply any fault-specific diagnosis their execution needs.

The model assesses one deployment duty after learning. It is not silently identified with the third cycle's eight-module model or its recurring finance. There is no cash income between the episode's payments. Later restored production is not used to pay an earlier test or repair bill.

**Actual cash and imputed consequence differ.** Failure loss `L` enters the stated objective but is never deducted as an imaginary cash payment. Every actual branch keeps cash nonnegative. If a repair bill is unaffordable, the program records failure instead of granting credit that the process does not possess.

The objective for this supplied selector is

`expected money spent + L × probability of failed repair`.

This is a declared valuation, not a derived ethical ranking of money and harm. A protected requirement to repair every possible fault would be a different test.

## 2. Paid observations and actual controller memory

The institution chooses a fixed probe count `N` and a register architecture before observing any data. A probe takes one lead-time slot and costs `s`; this is the supplied all-in charge for its comparable diagnostic exposure, measurement, and current write operation. The later deployment can begin after the chosen cohort completes, and `N` must fit the public lead-time bound. There is no hidden delay utility beyond that bound and the declared prices.

A retained data bit costs `μ` per holding interval. The final interval between the last report and the selection action also requires retention. The physical alternatives are:

| Register protocol | Final retained information | Paid retention |
|---|---|---|
| OR accumulator | Whether any probe was positive | One bit over `N` intervals |
| Counter | Exact positive count from zero to `N` | `ceil(log₂(N+1))` bits over `N` intervals |
| Last report only | The last probe result | One bit for the final interval only; earlier reports discarded |
| Erased | Empty register | No retained payload |
| Paid OR, then lost | Empty register after final loss | Same expenditure as the OR accumulator |

The zero-probe case uses no data storage. Register validity and the public program phase are supplied payload-independent metadata; the counter's charged data cells encode the `N+1` possible counts. The program and public clock are fixed operating infrastructure, not claimed to be physically free in every implementation.

The actual update rules are `R←R OR Y_t`, `R←R+Y_t`, overwrite by `Y_t`, or erase to `⊥`, according to the selected architecture. The final selector receives **only** this physical register, the public `N`, its known architecture, and the resulting cash. No observation history is passed to it.

The planned probe and storage fees are paid before their outcomes become available. With no intervening income, affordability of their total is sufficient for all those payment prefixes. Fees, cohort size, and timing are independent of the payload, so remaining cash and stopping time do not secretly encode discarded observations. Adaptive stopping and its informative public traces are outside this fixed-cohort class.

After learning, paying for maintenance deliberately converts evidence into a physical action. Its cost and later effects are included. That visible choice is an intended output of the selector, not an uncharged route by which earlier data circumvent its register restriction.

## 3. The actual selection rule

For each possible final register value `r`, the program computes

`P(H|r)=πP(r|H)/[πP(r|H)+(1−π)P(r|L)]`,

then predicts `p(r)=P(H|r)p_H+[1−P(H|r)]p_L`.

Crucially, the likelihood is that of the **final register**, not the full history that the analyst enumerates. After erasure, `P(r|H)=P(r|L)=1`, so the selector returns to the prior. A last-report controller conditions on one report rather than on the earlier discarded reports.

When both routes can be fully financed after learning, the rule chooses maintenance precisely when

`p(r)(A−C)>m`.

Ties choose no maintenance. If the substitute is unfunded but the local route is affordable, the same rule replaces `A` by the stated failure consequence `L`. If local repair also cannot be afforded, its score includes failure rather than an unfunded successful repair. The checker uses actual remaining cash in every comparison.

**Why the rule is optimal for its supplied criterion.** At each register value, the two expected continuation scores are affine functions of its posterior fault probability. Selecting the smaller gives the minimum conditional expected score. Summing over register values gives the minimum for that fixed architecture; independent randomization cannot improve a minimum of two available scores. This is ordinary finite Bayesian decision theory, not a new learning theorem.

The outer comparison enumerates all public `N` and register choices in the declared finite menu. It is a supplied architecture optimizer, not a claim that the learner invents its own memory representation or discovers the model family.

## 4. Base result: evidence induces selective maintenance

Take

`π=1/5`, `p_H=1/2`, `p_L=0`,

`s=0.08`, `μ=0.02`, `m=1`, `C=6`, `A=L=14`.

Initially the predicted fault probability is `0.1`. Maintenance would cost `1+0.1×6=1.6`, while the substitute route has expected expense `0.1×14=1.4`; the actual prior-based selector therefore does not maintain.

Any positive probe rules out the supplied no-hazard regime. With no positives in `N` probes,

`P(H|0,…,0)=1/(1+4·2^N)`.

Maintenance requires posterior high-regime probability above `1/4`. Thus the implemented policy is:

- maintain after a retained positive;
- do not maintain after all retained negatives.

An OR bit plus the public fixed `N` is sufficient for the entire relevant posterior in this special family. Counting every positive supplies no additional decision information here and can cost more to retain. This sufficiency is model-relative; the overlapping-regime control below removes it.

The adoption probabilities are exact:

`P(maintain|H)=1−2^(−N)`, `P(maintain|L)=0`.

At initial cash fifteen, the selected two-probe protocol pays `0.20` for probes and retention, leaving `14.80`, enough for either subsequent route. It maintains in 75% of high-regime episodes and zero low-regime episodes. The substitute repairs faults in the remaining cases. Every actual deployment fault is therefore repairable under this selected protocol.

### Exact learning-size threshold

For the tested base OR cohorts (`0≤N≤8`), and more generally while the relevant response bills remain funded, the total expected score is

`J_N=0.8+0.6·2^(−N)+0.1N`.

**Derivation.** In regime H, maintenance is chosen with probability `1−2^(−N)` and costs `1+(1/2)6=4` on average; the unmaintained route costs seven on average. Regime L incurs no deployment expense. Weighting by prior `1/5` gives `0.8+0.6·2^(−N)`, then add `0.1N` learning expense.

| Probes `N` | Expected score |
|---:|---:|
| 0 | 1.4 |
| 1 | 1.2 |
| 2 | **1.15** |
| 3 | 1.175 |

The next probe's gross expected benefit is `0.3·2^(−N)`. It exceeds its `0.1` expense for the first two probes and falls below it thereafter. The minimum is `N=2`. Even if the lead-time limit were relaxed, no larger OR cohort could beat it: knowing the regime for free already has minimum expected deployment expense `0.8`, so any `N≥4` costs at least `0.8+0.1N≥1.2`; `N=3` is checked explicitly. Insufficient remaining cash cannot lower that bound because the stated failure consequence is at least the successful repair fee. The finite menu also includes last-only, erased, counter, and paid-but-lost memory; none beats the two-probe OR protocol at these prices.

Knowing the regime without learning expense would yield expected deployment cost `0.2×4+0.8×0=0.8`. The difference is not presumed recoverable: information costs, finite evidence, and the supplied memory interface limit the implemented learner.

## 5. Capacity and actual adoption can diverge

Now keep the same statistical family and selector but provide only eight initial cash units. Two-probe learning still costs `0.20`, and the maintained route still fits (`1+6≤7.80`). The substitute's fourteen-unit bill does not.

The selector nevertheless has the same expected score and chooses the same policy, because the model deliberately assigns an unfunded fault the numerical failure consequence `L=A=14`. That equality is a supplied valuation, not a statement that failure and purchased repair are materially equivalent.

The failure event is exactly: high regime, no positive in the two probes, and a later deployment fault. Its probability is

`(1/5)·(1/2)^2·(1/2)=1/40=0.025`.

Under the same initial eight units, **unconditional maintenance without inquiry** costs at most seven and repairs every admitted fault. The protected robust capacity therefore exists, while this expectation-minimizing implemented selector does not use it. The failure is not a theorem that learning or Bayes updating is inherently harmful; the actual selector optimizes a criterion that permits this risk.

For any finite `N`, all-negative evidence remains possible in regime H. Its posterior never reaches zero. If the protected duty demands repair for every event in the model's support and the substitute is unaffordable, such evidence cannot certify that maintenance may safely be dropped. A robustly constrained selector in this example must retain the local route even after negative evidence; no probing is needed for that decision.

The same formula quantifies finite rather than absolute assurance. Under the OR rule and sufficient residual cash for local repair, high-regime maintenance adoption reaches `1−δ` only if `2^(−N)≤δ`. Greater confidence needs more paid probes and memory. No finite such threshold turns the all-negative event into impossibility.

### Learning itself can consume an enabling margin

With initial cash `7.1`, unconditional maintenance is initially feasible. One probe with retention spends `0.1`, leaving exactly seven. Two probes spend `0.2`, leaving `6.9`: now neither the seven-unit maintained route nor the fourteen-unit substitute can be fully prepaid on a fault. At that point the register may contain stronger evidence while the physical guarantee is gone.

The specified architecture optimizer responds to this constraint by choosing one probe, score `1.2`, rather than two. If the two-probe architecture is imposed anyway, its modeled fault-failure probability is `0.1`, the unconditional deployment hazard. Thus spending on discovery can change later feasible actions; accurate information does not itself finance implementation.

## 6. Reversals and controls

### Maintenance is unnecessary when the relevant hazard is absent

If both supplied regimes have fault probability zero, every probe is negative and no deployment fault can occur. No maintenance and no inquiry achieve score zero. Any positive probe/storage expense is wasted for this objective, and maintenance adds `m` without benefit. This is a direct proof in the no-hazard model, not a simulation frequency claim.

When the base regime is known to be H, the controller instead maintains immediately and needs no inquiry; its expected expense is four. When L is known, it chooses neither inquiry nor maintenance. Information is useful only when it can change a relevant choice enough to repay its cost.

### High learning or memory prices remove the incentive to learn

Raising probe price to `0.4` or retained-cell price to `0.3` makes the best checked protocol use no probes and retain the prior-based policy, score `1.4`. In the base OR family, the first observation's maximum gross improvement is `0.3` and later improvements decrease; these prices defeat that improvement. Last-report, count, erased, and lost-memory alternatives are also enumerated.

If only one lead-time slot is available, the best protocol takes one probe and scores `1.2`; it cannot realize the two-probe optimum before deployment. Giving storage a zero price improves the two-probe score to `1.11`, while the probe expense remains real.

### A cheap substitute can make local maintenance and learning unnecessary

Reducing the substitute's fault bill from fourteen to seven means even the high regime has expected incremental saving `p_H(A−C)=0.5`, below the one-unit readiness fee. No regime warrants maintenance under the supplied score. The optimum is no inquiry and the substitute route, expected expense `0.7`. This control keeps a concrete replacement mechanism rather than treating incumbent preservation as the objective.

### The memory sufficient for one model can become insufficient in another

Set `p_L=0.1`, retain `p_H=0.5` and prior `0.2`, set maintenance fee two, and reduce probe and retained-cell prices to `0.005` each. Now a positive may come from either regime, and positive counts carry distinctions that the OR flag merges.

At a matched cohort of three:

| Register | Total expected score | Implemented response |
|---|---:|---|
| OR | 2.46016 | Maintain after any positive |
| Counter | **2.39188** | Do not maintain after one positive; maintain after two or three |

The counter pays for its additional physical data cell. Its better evidence changes the actual selector enough to cover that price. Across the full declared menu up to eight probes, the optimum is five probes with a three-bit counter, score **2.3732016**. It maintains with probability `0.8125` in H and `0.08146` in L. Some unnecessary maintenance remains possible because the regimes have overlapping evidence laws.

This does not show that larger records are always preferable. In the base family, the OR bit is sufficient and the extra count storage merely costs more. Appropriate memory depends on the admitted model and decision test.

### Losing paid memory actually changes behavior

Forcing loss of the final OR register after two paid probes gives the selector the empty symbol, so its posterior is the prior and it never adopts maintenance. At base cash fifteen its expected score is `1.6`: the original `1.4` deployment expense plus `0.2` of spent learning support. The corresponding intact register scored `1.15`. No hidden transcript allows the lost-memory controller to use the observations anyway.

## 7. Exact verification and scope

The [standard-library checker](verification/check_paid_learning.py) writes [complete rational results](verification/paid-learning-results.json) and a [protocol frontier](verification/paid-learning-frontier.csv). It enumerates every binary probe history for each public cohort and register architecture, aggregates likelihoods by the physical final register, and separately evaluates every positive-probability regime/fault/payment branch.

The current record covers **505 protocols**, **28,120 enumerated probe histories**, and **2,426 positive cash/outcome branches** in twelve parameter cases. Nine base cohort sizes agree exactly with the closed-form posterior, adoption, and score expressions. Every cash branch satisfies

`cash_remaining + actual_learning_expense + actual_deployment_expense = initial_cash`,

with nonnegative remaining cash. A second register-conditioned score calculation agrees with the explicit branch calculation. The overlap example and limited-cash risk have additional exact assertions. All checks passed.

These checks establish the implemented finite calculations, not a general convergence theorem or empirical institutional claim. The probes are conditionally independent under the supplied regime; model drift, strategic reporting, correlated probes, changing interventions, and selection of the probe grammar would require different likelihoods and mechanisms. The final fault does not finance the preceding research, and the episode is not restarted with free inherited cash inside the code.

The mechanism is now more than a capacity assertion: an actual specified selector learns from paid retained evidence and changes action. Its remaining supplied components—prior, models, actions, prices, valuation, and architecture optimizer—are explicit. Explaining how those components are formed and transmitted remains separate from learning the hidden regime within them.
