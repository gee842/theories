# Recoverable inquiry: maintenance, observation, and repeated-error limits

Research memo, 5 October 2026. AI-generated research assistance under Ren's research direction. Five close primary sources were inspected for the ninth cycle. This memo identifies established baselines and requirements for a proposed finite model; it reports no new experiment or general institutional law.

The relevant existing framework is resource-constrained control under partial observation, with jointly chosen sensing and repair. The useful proposed extension is a particular closed feedback: a hidden hazard damages productive capacity; production pays for maintaining and restarting inquiry; inquiry informs a response that helps preserve that productive capacity. A pause is successful only relative to an explicit future-service requirement and error or harm criterion. Keeping a bank balance positive is not enough, and continuously operating inquiry need not be desirable.

## Five close primary sources

### 1. Maintaining the system and its means of observation

Chiel van Oosterom, Lisa M. Maillart, and Jeffrey P. Kharoufeh, **Optimal Maintenance Policies for a Safety-Critical System and Its Deteriorating Sensor**, *Naval Research Logistics* 64(5), 399–417 (2017). [Author repository record and abstract](https://repub.eur.nl/pub/102727/); [accepted author manuscript](https://cecas.clemson.edu/~kharouf/old/Papers/deteriorating_sensor_accepted.pdf).

A sensor gives free but progressively less informative observations of a binary system state. Costly full inspections reveal that state and create an opportunity to replace the sensor; an out-of-control system is replaced. A POMDP coordinates these decisions to minimize discounted operating, inspection, and replacement costs. The authors derive a threshold structure within their model.

**Boundary:** jointly maintaining an asset and the capacity to diagnose it is already formalized. The proposed model must add something more specific, such as diagnostics financed by the productive asset under hard liquidity limits. The paper's passive sensor observations are costless, so it is not a direct model of continuously paid readiness. The repository abstract and indexed manuscript text were checked; the direct manuscript fetch failed, and no uninspected threshold assumptions are imported here.

### 2. Production already supplies evidence about hidden deterioration

Abraham Grosfeld-Nir, **A Two-State Partially Observable Markov Decision Process with Uniformly Distributed Observations**, *Operations Research* 44(3), 458–463 (1996). [Publisher record and abstract](https://pubsonline.informs.org/doi/10.1287/opre.44.3.458).

The production system can deteriorate from good to bad; output quality supplies observations of its hidden state. A controller chooses between continuation and costly replacement to maximize discounted future income. The paper derives model-specific control-limit policies and an analytical infinite-horizon solution for uniformly distributed observations. It also reports that finite-horizon thresholds need not vary monotonically with remaining time.

**Boundary:** production, learning, and repair have long been coupled in maintenance models. For the new benchmark, production receipts and observed losses must enter the information state alongside diagnostic results. The existence of paid testing does not mean that paid testing is the only source of evidence. Only the publisher abstract was needed for this comparison; its particular threshold formulas are not used.

### 3. Expected performance is different from resource feasibility

Tomáš Brázdil, Krishnendu Chatterjee, Martin Chmelík, Anchit Gupta, and Petr Novotný, **Stochastic Shortest Path with Energy Constraints in POMDPs** (2016). [Full author paper, arXiv v2](https://arxiv.org/pdf/1602.07565v2); [conference version](https://www.ifaamas.org/Proceedings/aamas2016/pdfs/p1465.pdf).

The model combines partially observed dynamics with a capped resource that can be consumed or replenished. Its hard requirement keeps resource levels positive along executions until a target is reached, while expected total cost is optimized. It reduces the problem to a POMDP with resource levels incorporated into the state. Resource level is explicitly perfectly observable in the full paper's Remark 2. This is stronger than constraining expected consumption.

**Boundary:** recoverability under a budget is an established control problem. Expected future output does not pay an expense due now. The proposal concerns recurrent preservation rather than one-time target reachability, and may have different observation assumptions. If actual cash is unknown, this fully observed-resource construction cannot be applied unchanged; a belief over the relevant resource state is required.

### 4. Pausing observation while managing detection delay

Taposh Banerjee and Venugopal V. Veeravalli, **Data-Efficient Quickest Change Detection in Minimax Settings**, *IEEE Transactions on Information Theory* 59(10), 6917–6931 (2013). [Published author PDF](https://vvv.ece.illinois.edu/papers/journal/bane-veer-tit-2013.pdf); [earlier full manuscript](https://arxiv.org/abs/1211.3729).

DE-CuSum chooses when to observe and when to declare a change. The constraints concern pre-change sampling frequency and false-alarm rate, defined using the reciprocal of the mean time to false alarm. Under its known pre/post-change laws and divergence conditions, the procedure achieves first-order asymptotic optimality as the permitted false-alarm rate approaches zero. Bounded sampling pauses matter for the strongest worst-case delay criterion. The published PDF and detailed manuscript were inspected; theorem numbering is not transferred between versions.

**Boundary:** evidence-guided suspension and reactivation are established. Sampling-rate savings do not establish that standby machinery is paid, that repair remains feasible, or that damage during the detection delay is acceptable. A mean time to false alarm is not the probability of avoiding all false alarms forever. The paper's asymptotics are not finite-deadline or finite-reserve guarantees.

### 5. Repeated testing, depleted error budgets, and restart

Aaditya Ramdas, Fanny Yang, Martin J. Wainwright, and Michael I. Jordan, **Online Control of the False Discovery Rate with Decaying Memory**, NeurIPS 2017. [Primary conference paper](https://papers.nips.cc/paper_files/paper/2017/file/7f018eb7b301a66658931cb8a93fd6e8-Paper.pdf).

The paper studies online testing with weighted errors and a changing stream of hypotheses. It identifies both old discoveries underwriting later errors and practical loss of testing power after long null stretches. Temporary abstention and a decaying-memory error criterion enable a form of restart. Its stated FDR guarantees require the specified independence, monotonicity, and weighting conditions; conditional validity alone gives a different guarantee in Theorem 2.

**Boundary:** restarting after a long period without discoveries is also an established statistical issue. But the repair changes the criterion to decaying-memory FDR; it does not replenish a fixed lifetime probability-of-any-error budget. Statistical alpha-wealth is an accounting device, not money, productive stock, or a compensating benefit to someone harmed. Even weighted FDR is a ratio criterion, not an absolute cumulative-harm bound.

## The information boundary must include financial and physical consequences

Let the physical state contain hidden hazard \(H_t\), productive stock \(K_t\), cash \(B_t\), and inquiry readiness \(C_t\). A controller observes a declared history \(\mathcal F_t\), not these coordinates automatically. Its information state is their joint conditional distribution,

\[
\pi_t(h,k,b,c)=\Pr(H_t=h,K_t=k,B_t=b,C_t=c\mid\mathcal F_t).
\]

Coordinates observed exactly can be removed from the latent part, but their realized values remain conditioning information. Every observed production receipt, stock measurement, expenditure, refused transaction, repair result, or diagnostic result belongs in the same update. In a finite model with a joint transition-and-observation kernel \(M_a(s',o\mid s)\), the update is

\[
\pi_{t+1}(s')=
\frac{\sum_s\pi_t(s)M_{a_t}(s',o_{t+1}\mid s)}
{\sum_{s,s'}\pi_t(s)M_{a_t}(s',o_{t+1}\mid s)}.
\]

This general form avoids an unjustified independence assumption between output, stock changes, and diagnostic signals. These are standard Bayesian accounting requirements, not new results.

For example, if hazard deterministically lowers a known stock from two to one, receipts equal the current stock, and receipts are observed, the receipt reveals the hazard through that transition. Paid diagnosis may then have no additional information value. With noisy output, receipts still update beliefs even when they are not conclusive. If cash and stock are deliberately unobserved, an action rule using their true values to decide affordability supplies an unauthorized observation unless the payment outcome is explicitly modeled. Worst-case affordable actions, paid account inspection, and transactions that can fail are distinct alternatives.

Waiting also changes beliefs without a fresh signal. If a healthy system independently enters a persistent hazardous state with probability \(q\) each period, a current hazard probability \(p\) becomes \(1-(1-p)(1-q)^d\) after \(d\) unobserved periods. Thus a timed restart can be justified by known dynamics. No paid sampling does not imply no possible restart; it may imply less targeted or slower restart. Conversely, a negative diagnostic does not freeze the state as safe.

## Recoverability requires a specified standard

At least four questions differ:

- Is there an affordable action sequence that would restore inquiry in the true physical state?
- Can an observation-based policy identify and execute a suitable sequence before productive support is lost?
- What is the probability of recovering before a deadline under the model and initial belief?
- Can recovery be guaranteed over every relevant hidden state and disturbance sequence?

The first is not sufficient for the others. Each possible state may have a successful action while the required actions conflict under the same observations. A small posterior probability of irreversible failure may be acceptable under an expected-loss objective but rules out a probability-one guarantee if no safe action remains for that possibility. Even perfect diagnosis cannot help after repair becomes unaffordable or physically ineffective.

The model should distinguish inactive inquiry, degraded readiness, repairable productive damage, and irreversible loss of the means to restart. Declaring a state absorbing is a substantive technology or institutional assumption. If another provider or treasury can rebuild the function, include that route and its cost. Conversely, treating dormant readiness as free would remove the very maintenance problem being investigated.

## Choose the cumulative error or harm quantity before optimizing

Let \(A_t\) indicate intervention and \(H_t=0\) indicate that it is unwarranted under the declared purpose. Useful quantities include

\[
V_T=\sum_{t\le T}A_t\mathbf 1\{H_t=0\},\qquad
R_T=\sum_{t\le T}A_t,
\]

\[
\Pr(V_T>0),\quad
\mathbb E[V_T],\quad
\mathbb E\!\left[\frac{V_T}{R_T\vee1}\right],\quad
\mathbb E\!\left[\sum_{t\le T}\ell_t A_t\mathbf 1\{H_t=0\}\right].
\]

These are probability of any false intervention, expected count, FDR, and expected cumulative weighted harm. They are not interchangeable. A long-run rate divides a cumulative quantity by time; discounting or forgetting introduces another distinct objective. False intervention may also be too narrow: a response can be warranted yet dangerous or badly executed, and failure to intervene can harm people. The full loss function should include those possibilities when in scope.

For a finite exploratory model, an explicit bound on expected cumulative harm can be a tractable choice. A bound calculated under a Bayesian state model is conditional on that model and prior; it is not automatically a uniform frequentist guarantee. An expected bound is also not a pathwise cap.

If the system does not observe whether an intervention was actually false, it cannot update its policy by subtracting the true false-intervention indicator from a remaining budget. That would reveal the hidden state. It can instead use a conservative observable count of interventions, charge posterior expected harm, or solve an expected-constraint control problem with a correctly specified budget allocation over future observations. These have different interpretations. Merely enforcing a Lagrangian penalty does not establish that a requested hard constraint has been met.

For conditionally valid tests, predictable levels whose total is bounded by \(\delta\) give a probability-of-any-false-rejection bound via a union bound. This allows repeated attempts without resetting the same \(.05\) claim each time. It is a sufficient construction, not the only valid method or an optimal resource policy. Tightening thresholds can require more information, longer detection delay, or lower power. Relaxing to FDR or a long-run rate may permit more responsive monitoring, but that is a change in the tolerated error quantity and must be declared.

## A useful necessary information condition

There is a simple audit for a proposed reliable restart, independent of any particular detector. Compare two possible worlds, a hazard world and a safe world. Let \(P_1\) and \(P_0\) be the laws of the complete observable transcript available by the last useful intervention time under the same policy. For the event \(E\) that intervention occurs by that deadline, data processing gives

\[
D_{\mathrm{KL}}(P_1\|P_0)
\ge \operatorname{kl}\big(P_1(E),P_0(E)\big).
\]

If desired power is at least \(1-\beta\), false intervention at most \(\alpha\), and \(\alpha<1-\beta\), the right side is at least \(\operatorname{kl}(1-\beta,\alpha)\). This is the standard binary-event consequence of relative entropy, not a new theorem. Identical observable transcript laws therefore cannot support unequal intervention probabilities.

The transcript includes passive production evidence as well as paid diagnostics. Only under additional independent-sample assumptions does its divergence simplify to a sample count times a per-sample divergence. A budget or damage deadline limiting available information can make the requested error/power pair infeasible. Passing this necessary inequality does not establish that an affordable policy exists, that the likelihood model is right, or that the resulting intervention is legitimate.

## Mechanism comparisons that would clarify the contribution

Use a common production and repair process to compare continuous diagnosis, periodic diagnosis, evidence-guided diagnosis using all ordinary observations, paid standby with restart, and deliberate abandonment. Include settings where ordinary production is highly informative, weakly informative, or silent. The first can make an additional detector redundant; the last exposes the cost of retaining a genuinely separate detection channel.

Vary whether standby readiness decays, whether rebuilding takes time, and whether repair restores the revenue-producing stock. Remove the cash constraint as an information-only benchmark, and supply a clearly labeled full-information controller as an upper bound. A policy family chosen by a grid is a policy comparison, not an optimal POMDP solution. If optimizing expected value and imposing an error constraint, verify both the actual constraint and the proposed policy's feasible payment sequence.

Report productive output, inquiry and standby expense, repair expense, useful and unwarranted interventions, missed or delayed corrections, stock failure, and time until affordable restart is lost. Report quantities over a declared horizon and distinguish temporary outages from permanent loss. Do not let the terminal value make liquidation or last-period neglect look like regenerative behavior without explaining the horizon effect.

The possible contribution is the explicit coupling of **recoverable information access, an eroding source of its own finance, and a stated cumulative-harm standard**. Each ingredient and several pairwise combinations already have close predecessors. A small exact model could expose when apparently economical silence consumes the means to hear and respond later, and when silence is instead a sensible use of resources. It would not yet explain why institutional purposes, repair technology, or protected standing emerge. Whose harm matters and who may reopen a question remain normative choices, not implications of a maintenance equation.

## Proposed next frontier: attainable correction under plural constraints

**Unrun proposal after inspecting `experiments/recoverable-inquiry/model.py` and its protocol.** The implemented horizon-five case selects no tests; the horizon-eight, burden-.02 case drops initial diagnostic readiness and later rebuilds for a first test after deterioration. It does not demonstrate a paid negative finding followed by retesting. Its achievement is finite-horizon optimization in a known model under an ex ante expectation constraint. The next step should expose a common structure across the accumulated modules rather than append another physical mechanism.

Replace the privileged scalar objective with a vector of explicitly distinct evaluative quantities. For each permissible observation-based policy \(\pi\), let \(L(\pi)\in\mathbb R^m\) contain expected losses: productive shortfall, intervention burden borne by different participants, or loss of future correction capacity. Let \(\Gamma\) specify who may authorize actions at each observable history. Define

\[
\mathcal C_\Gamma=\{L(\pi):\pi\text{ obeys resource, information, and authority constraints}\}.
\]

**Finite expected-feasibility proposition.** With finite horizon, finite action/observation alphabets, and admissible ex ante lotteries over deterministic policies, \(\mathcal C_\Gamma\) is a compact convex polytope. Declared requirements \(L_i\le b_i\) are jointly feasible exactly when

\[
\min_{v\in\mathcal C_\Gamma}\lambda\!\cdot v
\le \lambda\!\cdot b
\quad\text{for every }\lambda\in\mathbb R_+^m.
\]

The forward implication follows by multiplying feasible inequalities by nonnegative weights. The reverse follows by separating \(b\) from the closed convex set \(\mathcal C_\Gamma+\mathbb R_+^m\). This is standard convex feasibility, not a new theorem. A separating weight certifies incompatible requirements; it is not an agreed social utility or evidence of whose interests should prevail.

For a sharp counterexample, two available policies have loss vectors \((0,2)\) and \((2,0)\). Each participant can separately obtain loss zero. Yet no lottery satisfies both bounds \((.9,.9)\): every attainable vector sums to two. The certificate is \(\lambda=(1,1)\). If an already physically feasible but forbidden policy gives \((.8,.8)\), permitting it restores joint feasibility. This distinguishes conflict among available options from a correction blocked by authority.

Pure action-set removal shrinks \(\mathcal C_\Gamma\) when information, resources, dynamics, and policy conventions remain fixed. This monotonicity does not describe a political change that also alters trust, information, incentives, or production. Nor does a feasible centralized policy show that independently acting participants will implement it.

Convexification itself needs justification. An ex ante lottery can meet everyone's average bound while imposing unacceptable harm on a person or realized history. Pathwise prohibitions, individual protections, and restrictions on randomization must be imposed separately; forbidding lotteries can make the attainable set nonconvex and invalidate the converse certificate above. Fixed thresholds also do not represent the formation or revision of purposes.

**Testable next step:** reuse the current small-horizon decision graph and its recorded metrics to compute attainable vectors under two or three declared bounds. Compare unchanged physics with a diagnostic-access restriction or repair veto. Preserve a witness policy for feasible requirements and a separating certificate for infeasible ones; separately check each lottery component and prohibited outcome. Report whether lost correction comes from resources, information, evaluative conflict, or the stipulated authority restriction. This would provide a reusable comparison across modules without pretending to resolve the legitimacy of their purposes.
