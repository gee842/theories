# Paid noisy evidence and timely revision

A controller can become more accurate about which rule is appropriate while becoming less likely to deliver a usable successor. In this finite example, a supplied three-probe update rule identifies the appropriate label with probability \(27/32\), but its acquisition cost or delay can reduce successful handoff to \(27/64\). A finance-aware controller then does better with one probe, achieving \(3/4\). No inquiry achieves \(1/2\). These are exact probabilities in a declared Bayesian model, not sure-safety guarantees.

This companion study is separate from the cycle-6 population-and-repair experiment. It isolates noisy learning, physical report memory, paid rule revision, and a finite support deadline. It does not reuse that experiment's grant, diagnostic-channel, observation, or model-rewrite prices, and its thresholds cannot be inserted into the population ledger.

## 1. Fixed physical and informational contract

The old working rule is A. At the start of the evaluation window, the environment either remains in regime A or has changed to regime B. The current regime \(\theta\) is drawn with supplied prior

\[
\Pr(\theta=A)=\Pr(\theta=B)=1/2.
\]

It stays fixed through this window and the successor's declared obligation. A successor meets that obligation exactly when it receives the matching rule and at least six units of usable working reserve by deadline \(D\). Its underlying plant and these two rule implementations are supplied; this experiment does not derive or learn their physical performance specification.

The evaluator starts with integer reserve \(R\), no interim income, and an endowed current A program. At most three observations are available. Given the regime, their potential reports are independent:

\[
\Pr(X_i=1\mid B)=3/4,\qquad
\Pr(X_i=1\mid A)=1/4.
\]

Thus every finite binary report word has positive probability under both regimes. The observed variable is evidence of the regime, not a direct revelation of it. The prior, likelihood family, actions, deadline, fees, and controller programs are supplied before sampling; the learned object is the current regime.

One observation takes one slot and requires two units paid in advance: one for measurement and one for the finite register's retention/update interval. Keeping A launches immediately with no revision expense. Replacing it by B costs two and takes one additional slot. No revision can finish after the support deadline. On-time completion at \(D\) is allowed.

The six-unit working reserve is transferred to the successor as part of whatever cash remains; it is not an observation or revision expense. A funded launch transfers the entire remainder. An unfunded or late launch fails and leaves the untransferred remainder with the failed evaluation process. Every branch conserves cash:

\[
R=(\text{measurement and memory bills})
  +(\text{revision bill})
  +(\text{cash transferred})
  +(\text{cash left untransferred}).
\]

There is no credit against future success, no source of funds during evaluation, and no repeated-epoch claim. This finite model does not establish a self-financing process.

### Payment and action order

At a decision time, a controller can keep A, request B revision, buy another observation, or abort. A measurement can begin only if its two-unit fee is available and it can finish by \(D\). The fee is paid before its random report arrives. Revision can begin only if its own fee is available and its one slot fits. A B request that cannot begin fails; it does not silently revert to A. If revision completes but the remaining reserve is below six, the B rule may have been installed but the successor is not usable. Choosing A likewise fails if the remaining reserve is below six.

The finance-aware comparator checks the eventual child requirement when selecting its actions. The actual three-probe rule below does not: it is an explicitly supplied acquisition-and-majority mechanism, not an optimizer of funded delivery.

## 2. The memory is a physical part of the controller

The retained evidence is a counter \(k\in\{0,1,2,3\}\), initially zero. After report \(X\), the update is \(k\leftarrow k+X\). The public phase \(n\in\{0,1,2,3\}\) counts completed measurement slots. Cash and the current program are physical state. The decision interface contains only \((n,k,b)\), the preset protocol, and the supplied model; it cannot reread an ordered report history. The rental/update fee includes enough counter capacity for this maximum of three reports. It is a specified tariff, not a general law that memory costs are independent of bit count.

One paid retention interval covers the counter through acquisition and until the next decision. When a final rule is selected, the counter can be discarded; the B revision fee covers the ensuing actuation command and program delivery. The fixed program, phase counter, and model description are not additional report storage.

Two same-price controls make the restriction concrete. Both commit to the same three measurement times and payments before any report:

* **Last report only:** each new bit overwrites the old payload; the final selector receives only that bit.
* **Erased report:** each paid report payload is destroyed before the next controller decision. The final controller receives only \(\bot\) and defaults to A.

The erased control still pays the stated measurement and storage bills; it represents loss after paying, not a cheaper storage architecture. For these fixed cohorts, phase, remaining cash, and acquisition history are identical under every report word. They cannot encode a lost bit. The copier receives no hidden observer transcript or unpriced external memory.

The optimizer below uses the retained-count architecture only. No claim is made that its count-state recurrence solves an arbitrary erased-memory architecture while remembering lost reports.

## 3. Actual updating, fixed behavior, and the paid optimum

The **actual majority rule** commits to three observations, then recommends B exactly when \(k\ge2\); otherwise it keeps A. It stops if the cohort itself cannot be completed. At final selection it attempts the recommended implementation under the payment and timing rules above, with no fallback after an infeasible B request.

The **fixed rule** takes no observations and retains A. With \(R\ge6\), its success probability is \(1/2\).

The **full-information bound** receives \(\theta\) at time zero at no observation cost, then selects its matching rule. This deliberately free information is an upper bound, not a physically implemented paid evaluator. Revision still costs two and one slot. For \(R\ge6\), its success is one if \(R\ge8\) and \(D\ge1\), and \(1/2\) otherwise.

The **paid optimum** maximizes the probability of delivering a matching, sufficiently funded successor on time within the finite count-memory grammar. It chooses observations and stopping times as well as its final rule. Costs are constraints on that objective, not automatically a welfare metric.

Given the count state, the posterior is

\[
\pi_{n,k}=\Pr(B\mid n,k)
=\frac{3^{\,2k-n}}{1+3^{\,2k-n}}.
\]

This formula is specific to the base prior and overlapping likelihoods; the checker uses the general likelihood formula for controls. Sufficiency follows directly from conditional independence: the probability of an ordered word depends only on its length and count.

Let \(V(n,k,b)\) be the best success probability from that physical decision state. There are no waiting actions; elapsed time is \(n\). Available terminal values are

\[
V_A=1-\pi_{n,k}\quad\text{if }b\ge6,\ n\le D,
\]
\[
V_B=\pi_{n,k}\quad\text{if }b\ge8,\ n+1\le D.
\]

If \(n<3\), \(b\ge2\), and \(n+1\le D\), observation has value

\[
V_{\rm obs}
 =(1-q_{n,k})V(n+1,k,b-2)
  +q_{n,k}V(n+1,k+1,b-2),
\]
\[
q_{n,k}=\tfrac14(1-\pi_{n,k})+\tfrac34\pi_{n,k}.
\]

The value is the maximum of feasible terminal values, observation value, and abort value zero. On equal values the implementation prefers immediate A, then immediate B, then observation. This tie rule selects a specific witness; no expected-cost optimality theorem is inferred from the tie convention alone.

The recurrence is exact by induction on remaining observations: each allowed choice has the displayed conditional outcomes; after a report the actual retained counter and cash determine the next state. Randomizing among current actions cannot exceed their maximum. This is a finite Bayesian optimality statement. Nature is sampled according to the declared law, rather than universally adversarial at every report.

## 4. An exact cost-and-deadline frontier

For integer \(R\ge6\), nonnegative integer \(D\), the base prices and likelihoods, and at most three probes, the paid optimum is

\[
\boxed{
V(0,0,R)=
\begin{cases}
27/32,&R\ge14,\ D\ge4,\\
3/4,&R\ge10,\ D\ge2,\ \text{and the first case fails},\\
1/2,&\text{otherwise}.
\end{cases}}
\]

**Upper bounds.** Three free reports have Bayes classification accuracy \(27/32\); a controller with at most that evidence and additional implementation constraints cannot exceed it. If either reserve or deadline does not permit B after three reports, a third observation can end only in A or failure. Its expected funded success is at most the current posterior probability of A. Stopping in A before that observation is at least as good whenever A can be funded; otherwise the third observation cannot improve the reserve. Hence the third observation can be removed without reducing the optimum. The best classifier with at most two reports has accuracy \(3/4\), including its posterior tie at one positive report. Finally, if B cannot be implemented after even one observation, every branch that samples can succeed only through A. Its total success is at most the prior probability \(1/2\); sampling adds no usable decision option.

**Attainment.** With \(R\ge14,D\ge4\), take three reports and follow the majority. Six pays for evidence, two remains available for B revision, and six remains for the child. With \(R\ge10,D\ge2\), take one report and choose its indicated rule. With \(R\ge6\), retain A immediately. These witnesses meet all prefix and deadline conditions, proving the formula. ∎

The frontier is not an infinite-time result. More probes, a richer action menu, new income, different priors, or later support define a different problem.

### Why better classification can produce worse delivery

Under either regime the three-report majority is correct with probability

\[
1-\left[3(1/4)^2(3/4)+(1/4)^3\right]=27/32.
\]

At \(R=12,D=4\), the cohort spends six and leaves six. Every A recommendation can launch, while every B recommendation pays two for revision and then leaves only four for the child. Therefore only the event “regime A and majority A” succeeds:

\[
\Pr(\text{usable successor})
=\tfrac12\cdot\tfrac{27}{32}
=27/64
<1/2.
\]

The correct-label probability remains \(27/32\). At \(R=14,D=3\), all three observations fit, but B's additional revision slot does not. The same \(27/64\) delivery probability results. That failed B revision cannot begin, so its fee is not charged in this timing case.

| Reserve / deadline | Three-report recommendation accuracy | Actual usable successor | Best paid usable successor | Free-information bound |
|---|---:|---:|---:|---:|
| 14 / 4 | \(27/32\) | \(27/32\) | \(27/32\) | 1 |
| 12 / 4 | \(27/32\) | \(27/64\) | \(3/4\) | 1 |
| 14 / 3 | \(27/32\) | \(27/64\) | \(3/4\) | 1 |
| 10 / 4 | \(27/32\) | 0 | \(3/4\) | 1 |
| 8 / 4 | \(27/32\) | 0 | \(1/2\) | 1 |

The last row is an access/finance gap even though an oracle could implement either rule. Paying for one report leaves six, after which B can no longer be both revised and financed. The optimal paid controller does not acquire information that cannot improve a feasible choice.

With \(R=14,D=4\), an optimal early-stopping witness observes twice. If reports agree, it stops; if they differ, it buys the third and follows it. Two agreeing bits already determine the eventual three-bit majority. Disagreement probability is \(3/8\), so this witness uses \(2+3/8=19/8\) observations on average. Its expected actual bill is \(2(19/8)+2(1/2)=23/4\), compared with seven for the fixed cohort. Both achieve \(27/32\). At \(R=12,D=4\), the saved policy uses one report, spends three on average, and achieves \(3/4\).

## 5. Controls and scope of the guarantee

With full funding, last-report memory achieves \(3/4\) rather than count memory's \(27/32\). Complete erasure followed by default A achieves \(1/2\). This is a literal finite-memory comparison; the scorer never secretly restores earlier bits. Under the underfunded \(R=12\) majority mechanism, erasure/default A happens to improve delivered success from \(27/64\) to \(1/2\), despite losing information. It changes the actual selected behavior and its revision bill; it does not show that removing information improves the optimized feasible policy set.

Three further controls are checked:

* **No regime change:** with prior \(\Pr(B)=0\) and \(R=6\), retaining A achieves one. The fixed three-probe mechanism spends the necessary working reserve and achieves zero. Learning was unnecessary under this supplied known regime.
* **A perfectly separating probe:** setting the likelihoods to zero under A and one under B lets the optimizer identify and implement the rule with probability one at \(R=10,D=4\). The three-probe mechanism still spends too much and fails. This isolates evidence overlap from implementation waste.
* **Free observation and memory:** with the base overlapping signals but zero acquisition/storage fees, \(R=8,D=4\) suffices for \(27/32\). Finite noisy evidence still leaves classification error after its financial obstruction is removed.

For the base overlapping signals, no finite policy in this grammar can guarantee success under every positive-probability regime/report realization. Any report prefix that causes launch has positive likelihood in both regimes; a single installed A or B cannot match both. Abort is failed delivery. At most three reports also gives the stronger quantitative expected-success upper bound \(27/32\). Thus an expected improvement does not imply the earlier cycles' sure-safety property, and the free-information bound is not an achievable certainty claim for noisy paid observations.

The model does not address unknown likelihood families, a regime changing during the observation window, report corruption beyond the declared controls, recurrent maintenance of the observer, population growth, or an endogenous mechanism selecting the majority or Bayesian objective.

## 6. Exact verification and preserved artifacts

The standard-library checker uses rational arithmetic. Its dynamic program is cross-checked by enumerating all deterministic action tables on the ten public-phase/count states. For a fixed initial reserve, cash before final revision is \(R-2n\), so a table indexed by \((n,k)\) also covers every possible dependence on the available cash in that check. Six states before the final observation have actions A, B, or probe; the four final states have actions A or B. Each check covers

\[
3^6\,2^4=11{,}664
\]

tables. Explicit abort need not be listed: its zero payoff cannot improve a maximum, and an infeasible attempted action also fails. For every table, the separate enumerator evaluates both regimes and all eight potential three-bit words, taking actions only from the permitted current counter state. Unused potential reports are integrated out; they are never inputs to an early decision.

Four settings give 46,656 table checks and 746,496 potential-history rollouts. This enumerator shares the declared terminal payment routine with the other checks, so agreement is not independent physical-model validation. It is an exhaustive check of the Bellman decision calculation within the stated grammar. The checker also verifies all 55 reserve/deadline pairs with \(6\le R\le16\) and \(0\le D\le4\), eight selected settings and their memory controls, every reported cash-conservation identity, and the two early-stopping expected-cost calculations. The analytical proof above, rather than grid extrapolation, establishes the frontier outside those 55 points.

* [Exact checker](verification/check_paid_revision.py)
* [Results, state/action certificates, and branch ledgers](verification/paid-revision-results.json)
* [Reserve/deadline frontier](verification/paid-revision-frontier.csv)

Run from the workspace:

    python3 outputs/cycle-6/verification/check_paid_revision.py

The preserved run reports all assertions passed.
