# Recoverable inquiry with productive state and cumulative burden

5 October 2026. Design review for the ninth cycle. No implementation or numerical result is audited here. The proposed experiment joins productive cash, physical state, paid diagnostic readiness, and retained beliefs. It isolates control of a supplied repair action; it does not replace the preceding situated-proposal model with a claim that new proposals are being generated.

## What changes, and what remains supplied

The previous renewal model supplied six units of ordinary output regardless of inquiry or deterioration. The present model makes output depend on the productive state that response can maintain. It can therefore distinguish pausing an unnecessary test from losing the material ability to test later, and restarting a diagnostic apparatus from rescuing a producer after irreversible collapse.

This is close to established maintenance theory. [Smallwood and Sondik's finite-horizon partially observed control paper](https://pubsonline.informs.org/doi/pdf/10.1287/opre.21.5.1071) explicitly includes a machine-maintenance example. Partial observation plus maintenance is not a new foundation. The potentially useful contribution of this cycle is the explicit coupling of actual cash production, paid readiness with rebuilding delay, all available observations, and a certified cumulative-burden constraint, together with transparent failure controls.

The horizon, transition law, sensor, repair efficacy, stock dynamics, burden weights, and terminal values remain supplied. A finite-horizon optimum under those inputs cannot establish a universal maintenance schedule, an ethical value function, or indefinite viability.

## Adopted chronology and observation interface

The current design has horizon five, with six considered if computationally manageable. Observable stock is \(x\in\{0,1,2,3\}\), cash is \(b\in\{0,\ldots,8\}\), and diagnostic readiness is \(r\in\{0,1\}\). The fault \(\theta\in\{0,1\}\) is hidden. Its transition after production has probabilities \(P(\theta'=1\mid\theta=0)=.1\) and \(P(\theta'=0\mid\theta=1)=.05\). The controller retains its sufficient belief freely; physical diagnostic readiness has a price.

At the start of a living round, a ready apparatus can be kept for one cash unit or dropped for free. An absent apparatus can be rebuilt for three, but becomes usable only next round. An apparatus kept this round can perform a diagnostic for two additional units. Repair remains available without a diagnostic and costs three. Every selected prefix must be affordable before income arrives. This avoids creating diagnostic value by forbidding direct repair, and avoids borrowing silently against favorable future production.

The final sensor design is binary with sensitivity and specificity .9. An earlier reveal-or-erasure proposal was superseded before implementation. With prior fault probability \(p\), the current sensor gives

\[
P(+)=.1+.8p,
\quad p_+=\frac{.9p}{.1+.8p},
\quad p_-=\frac{.1p}{.9-.8p}.
\]

At \(p=0\), even a positive sensor result leaves posterior zero; at \(p=1\), even a negative result leaves posterior one. These are consistency checks on updating a known state, not defects of Bayes' rule. After ordinary recurrent transitions the belief will generally lie between those endpoints.

Repair resets the current effective fault to zero. Given repair decision \(u\), damage \(D\) occurs with probability .1 when the effective state is healthy and .8 when faulty. Productive stock and cash income are

\[
x'=\operatorname{clip}(x+1+u-2D,0,3),
\qquad Y=2x'.
\]

Cash after spending and income is capped at eight; overflow goes to the treasury. The controller observes actual \(x'\) and the consequent income, rather than a hidden expected outcome. Zero stock is stipulated to be absorbing, with no actions or output, even if cash remains. Thus productive collapse is an imposed irreversible boundary. Recoverability in this model concerns diagnostic readiness while production survives, not a proof that every failed producer can be rebuilt.

## All observed consequences must enter one filter

The likelihood used for the next belief must sum all hidden damage outcomes compatible with the observed clipped stock. It is a joint observation calculation. Income is a deterministic copy of stock and must not be multiplied into the likelihood as an independent second observation. Cash after clipping may lose information, but it cannot add a hidden signal beyond the declared actual income and chosen spending.

Without repair, let \(p^{\mathrm{post}}\) be the fault posterior after the observed production/stock transition. The next-round prior is

\[
p'= .1+.85p^{\mathrm{post}}.
\]

With repair, the current fault is reset, so the next prior is .1 regardless of the earlier belief or production result. This is an intervention on the state, not an arbitrary erasure of knowledge. Production after successful repair cannot reveal whether the pre-repair target was absent merely by showing a healthy result.

The initial state \(x=3,b=8,r=1,p=0\) represents a recent negative determination supplied before the horizon. Give every comparator the same information. The later model should include a range of starting beliefs or clearly label its special initial condition. A negative diagnostic during the experiment must remain in the posterior; it cannot be discarded when the apparatus is dropped or rebuilt.

## A tractable exact finite algorithm

Use belief states \((h,x,b,r,p)\), with rational beliefs for the rational transition parameters. Memoized finite-horizon dynamic programming can merge identical information states without retaining irrelevant histories. Cash, stock, and readiness are observed; the hidden fault must not appear in the policy key as if observed.

The sequential decision nodes are infrastructure choice, optional diagnostic, and repair after the diagnostic result or absence of a test. With a binary sensor, a flat equivalent enumeration includes four contingent repair prescriptions after testing, plus the two no-test repair choices, within each compatible infrastructure choice. A staged Bellman calculation naturally chooses repair separately after each signal. Restricting testing to a hard-coded positive-test repair rule would fail to optimize the declared problem; negative-result repair can still have value when stock restoration matters.

Budget feasibility must be checked on each signal branch. In particular, paying upkeep and a diagnostic may leave too little for repair. A controller can rationally drop the apparatus to retain repair funds. It can also rebuild now for next-round information while responding directly now. The procedure should not silently forbid those feasible combinations.

The declared primary cost is cumulative spending minus actual income, with terminal stock salvage \(2x\) and an extra failure penalty twelve when terminal stock is zero. Because the zero state is absorbing, terminal zero also means collapse by the horizon. The salvage price and failure penalty are preferences, not fitted physical constants; retain sensitivity to them. A terminal stock value can discourage finite-horizon stripping, but cannot certify long-run viability.

The monetary identity is

\[
\Delta b+\text{spending}+\text{treasury overflow}=Y.
\]

Consequently cumulative income minus spending already equals treasury overflow plus the change in cash balance. Do not add terminal cash again as a second reward unless the objective is reformulated. Stock salvage is a separate terminal value and can be added as declared. Any diagnostic burden or target-absent intervention burden must be labeled as additional harm rather than silently counted as another payment.

## Cumulative burden and certification

The proposed burden is expected target-absent repairs plus .05 per diagnostic. It is deliberately not called a false-action count: repair can restore depleted stock even when the hidden fault is absent. For a chosen repair, the target-absent probability uses the posterior immediately before repair. Using the repaired state would falsely classify every repair as target-absent; using subsequent output to announce a hidden pre-repair state would leak information.

Let \(F(\pi)\) denote this cumulative expected burden and \(C(\pi)\) the primary expected cost. The constraint is \(F(\pi)\le .6\) ex ante. No test-level significance interpretation is needed for this Bayesian sensor. The constraint controls an expectation over the specified horizon, not the harm on every realized trajectory and not a lifetime false-action probability.

For multiplier \(\lambda\ge0\), solve the Bellman problem for \(C+\lambda F\). A feasible policy or ex ante mixture supplies an upper bound on the constrained optimum, while

\[
\min_\pi\{C(\pi)+\lambda F(\pi)\}-\lambda\beta
\]

is a valid lower bound. Report their gap. A mixture of two policies at a common supporting multiplier can attain the budget when the finite policy set has the relevant exposed face. Mixing policies from an arbitrary coarse multiplier grid does not, by itself, prove constrained optimality. It can still provide a feasible bound if the separate dual lower bound is valid. If the unconstrained optimum already meets the burden budget, no mixture is needed.

An alternative is a finite occupancy-measure linear program over all reachable belief states. Expected burden is a linear occupancy cost, with feasibility and observation probabilities fixed by the belief model. This is established constrained-control methodology; see [Altman, *Constrained Markov Decision Processes*](https://www.routledge.com/Constrained-Markov-Decision-Processes/Altman/p/book/9781315140223). The weighted Bellman route is likely smaller here, provided its certificate is retained.

If probability of at least one target-absent repair is also reported, evaluate it with an extra hidden cumulative flag, never exposed to the controller. An expected count and a probability of any event are different. The union bound provides a conservative relationship, but neither should be relabeled as the other. Ordinary posterior updates and expected stage burdens alone suffice for the stated expected-burden optimization.

## Discriminating controls and failure criteria

1. **Information completeness.** Compare filtering with an independently enumerated hidden-state history for a short horizon. Identical public histories must give identical beliefs and decisions regardless of the simulator's hidden path. A no-diagnostic comparator still receives stock, income, and cash observations. Ignoring those observations would manufacture an inquiry advantage.
2. **Real pausing and restarting.** Record a positive-probability reachable path in which a negative result reduces inquiry, production evidence later raises concern, and paid apparatus rebuilding or resumed testing follows. Report the cash and readiness decisions on that path. If no such path exists in the optimized policy, do not claim the current parameters demonstrate evidence-driven restart. Inability to afford inquiry is also different from choosing to pause it.
3. **Direct-action alternative.** Optimize the no-diagnostic restriction while leaving repair and passive inference available. More expensive or less informative diagnostics should sometimes be unused. A completely uninformative paid sensor must not improve the unconstrained optimum. If direct repair becomes free and has no target-absent burden, inquiry may become unnecessary rather than universally beneficial.
4. **Material feasibility.** Evaluate poor-stock/low-cash states, including productive collapse, rather than only the affluent initial state. Removing the guaranteed production floor does not imply that a clever information policy can rescue every state. Check that the policy never spends future income before it exists and that cap overflow returns to the treasury.
5. **Burden and horizon limits.** Retain primary cost, expected burden, failure probability, stock, output, spending, and the dual gap. Vary the burden bound and terminal values. Lower intervention burden can increase productive failure when a healthy but depleted stock needs restoration; that tradeoff should remain visible.

The earlier finite-buffer eventual-shutdown theorem concerns an infinite sequence with a particular self-financing rule. It does not transfer automatically to this adaptive, partially observed, finite-horizon control problem. This cycle can show when conserving productive capacity, preserving diagnostic readiness, and acting on evidence are jointly feasible under a declared objective. It cannot turn those distinct requirements into an unconditional promise of perpetual inquiry or continued becoming.

## Implementation and development audit

5 October 2026. Reviewed `experiments/recoverable-inquiry/model.py` and all eighteen records in `development.json`. The root was still preparing the full frontier report. No substantive filtering, prefix-finance, or main Bellman error was found. Two reporting/comparison corrections were sent before further analysis: distinguish capacity restoration from the current weak witness, and detect restricted-mode burden infeasibility rather than comparing unlike constraints.

### The implemented observation and accounting rules

The binary sensor's posterior calculation is correct. Production groups hidden damage events by the actual clipped stock before computing the posterior, so it does not double-count stock and its deterministic income. Repair resets the effective fault before production, while target-absent burden is calculated from the pre-repair posterior. Expenditure is paid before production, infrastructure rebuilt this round cannot test until the next round, and direct repair remains available after any affordable infrastructure choice. The contingent test prescriptions allow repair choices on both positive and negative outcomes.

Canonicalizing belief/readiness in terminal nodes does not erase decision-relevant information: those nodes have no future actions, and zero stock is stipulated irreversible. Such a canonical terminal belief is an implementation placeholder, not an inferred statement that the fault has disappeared.

I checked several cases independently against elementary formulas. At prior \(1/10\), a positive result has probability \(9/50\) and posterior \(1/2\); a negative result has probability \(41/50\) and posterior \(1/82\). From stock three without repair, next stock two has probability \(17/100\) and next-round fault belief \(1/2\); next stock three has probability \(83/100\) and belief \(10/83\). Repair at stock three gives stock three with probability one after clipping, and next belief \(1/10\). All agree with the implementation.

A separate one-round manual control has optimal cost −11.6 and zero burden for both the adaptive and no-test modes: drop readiness, do not repair, receive expected output 5.8 and expected stock salvage 5.8. The continuous mode pays upkeep and a test despite the certain initial healthy state, attaining cost −8.6 and burden .05. The code matches these values. These are independent checks of the implemented information/timing rules, not a full implementation audit of the forthcoming analysis script.

### Preserve the negative development results

All six recorded budgets at horizon five and all six at horizon six select **zero paid tests and zero rebuilds**. The budgets are .02, .05, .1, .15, .2, and .6. At horizon eight, five of the same six budgets still select zero paid tests and rebuilds. Those are substantive countercases to an unqualified claim that optimal correction needs continuous paid inquiry. Passive stock evidence and direct response can be sufficient under the declared model and preferences.

Only the recorded horizon-eight, budget-.02 case uses paid testing: expected tests .1375297375, expected rebuilds .29575234125, target-absent repair burden .01312351312, and total burden .02. Its expected primary cost is −43.12729236087, with the reported primal/dual gap approximately \(5.65\times10^{-10}\). Its terminal failure probability is .12438943051. The paid-test case was found during exploratory horizon/budget development, not in a preregistered comparison. All earlier zero-test cases must remain in the research record and final interpretation.

The distinction between burden and productive safety is material. For the same horizon, budget .05 uses no paid testing and has terminal failure probability about .0118152; budgets .15 and above have zero terminal failure in the recorded calculations. A tighter target-absent burden constraint can permit substantially more productive collapse. Lower burden is not an unqualified improvement in every outcome, and repairs without the hidden target can still restore productive stock.

### Correct witness semantics

The reviewed `witness` function selects a complete path containing a test immediately after an untested round. That event can be a first paid test. It does not require an earlier test, a negative sensor result, a readiness drop, a rebuilding decision, or any persistent period of abandonment. Its returned probability is that selected complete path's probability under one deterministic mixture component; it is neither the total probability of restart nor automatically the unconditional probability under the whole ex ante mixture.

The development metrics do already imply a narrower valid statement. Both components of the horizon-eight budget-.02 mixture drop the initially ready apparatus at the root. Both later have positive expected rebuilding and testing. Since a dropped apparatus can test again only after rebuilding, later tests in that particular solution require restoration of capacity. A suitable label is **initial readiness dropped, later rebuilt, then a first paid test within the horizon**, unless stronger event tracing establishes more.

To substantiate actual capacity restoration, the witness should track a transition from `ready=1` with `support=drop`, later `support=rebuild` while absent, and a subsequent paid test after the rebuilding lag. Merely seeing the action string `drop` while readiness is already zero is not abandonment. To claim resumed *testing*, additionally require a prior paid test before the drop. To claim a negative-result-driven cycle, require an observed in-horizon negative result in the relevant preceding history; the supplied initial belief zero is not a newly observed result of the implemented policy. Print cash and posterior along the trace and distinguish selected-path illustration from aggregate event probability.

### Fairness of the modes and burden certificates

The `no_test` mode keeps all passive stock/income observations and direct repair choices. It is a fair restriction of the adaptive action space. A weak inequality favoring adaptive cost is therefore a consistency property of nested feasible sets; the size and interpretation of a strict gap are the interesting quantities.

The reviewed `continuous` mode forces both apparatus support whenever affordable and a diagnostic whenever immediately available and affordable. It still chooses repair adaptively. This is a continuous-testing comparator, not the strongest policy that merely preserves readiness while choosing test times optimally. Any report about permanent *capacity* should keep that distinction explicit or add a separately defined readiness-preserving comparator.

Every continuous-mode policy at the supplied initial state tests in the first round and therefore incurs at least .05 expected burden immediately. It is infeasible at budget .02. An unconstrained continuous result must not be compared as though it met the adaptive .02 cap. A separate lexicographic minimum-burden Bellman calculation can establish the restricted mode's true feasibility threshold. Exceeding an arbitrary multiplier ceiling is a computational bracketing failure, not by itself a general proof of infeasibility.

Within a feasible bracket, the constrained solver uses a valid approach: an ex ante mixture of feasible policy outcomes supplies the upper bound, and solved weighted Bellman values supply dual lower bounds. Policies need not be exactly optimal at the same sampled multiplier if the reported upper/lower gap certifies the numerical approximation. The development gaps support that limited finite-model claim. Their burden guarantee is ex ante; an individual trajectory or one selected mixture component can exceed the budget.

No root code was edited. The witness and restricted-mode feasibility points remain requests for the subsequent analysis/implementation pass, rather than claims that the reviewed development values are numerically wrong.
