# When inquiry can rest without losing the ability to return

Research continuation, 5 October 2026, Asia/Bangkok. AI-generated research assistance under Ren's direction, with mathematical, implementation, and primary-literature audits by three returning agents. Ren's immediate request was: “please continue, next frontier”. This is a research snapshot, not a verbatim conversation, empirical validation, or a claim that a universal alignment law has been established.

The [previous cycle](2026-10-05-renewal-of-inquiry.md) found that positive returns do not ensure continuing inquiry when accessible reserves are bounded and shortfalls recur. It also exposed the cost of inquiry after useful work has ended. This cycle makes productive output depend on a stock that can deteriorate and recover, and lets ordinary observations guide whether diagnostic capacity is kept, abandoned, rebuilt, or used.

The resulting distinction is **current activity versus an attainable route to future correction**. Maintaining a department forever need not maintain its function well. Closing it need not destroy that function if rebuilding remains timely, affordable, and sufficiently informed. Conversely, current production can continue after a particular standard of reliable future correction has become unattainable. The standard, disturbance class, and available alternatives must be specified before making that judgment.

## 1. A sharper structural target

Let a decision state contain productive stock, accessible cash, inquiry readiness, and a posterior over hidden conditions:

\[
z=(x,b,r,\pi).
\]

A useful action is not available merely because its mature benefits exceed its total cost. Its evidence must arrive soon enough, its actual payments must be affordable in sequence, and the response must still work at the state reached. Under an explicit safety region \(\mathcal K\), a robust finite-horizon version is

\[
\mathcal V_0=\mathcal K,\qquad
\mathcal V_{n+1}=\left\{z\in\mathcal K:
\exists a\in\mathcal A(z),\ 
\text{every possible successor lies in }\mathcal V_n\right\}.
\]

This is established viability/control reasoning on an information state. It describes the states from which an available observation-based policy can maintain the declared condition through the remaining horizon. It is more demanding than low expected loss. A Bayesian probability-of-survival version replaces “every” with an optimized expectation and an explicit probability threshold. Different requirements produce different feasible sets; there is no uniquely correct safety region supplied by mathematics.

The finite experiment below optimizes an expected objective under an expected burden constraint. It **does not compute this robust set**. Keeping the distinction prevents a favorable mean from becoming an unwarranted guarantee.

## 2. Evidence, time, and cash impose separate necessary conditions

Compare a healthy and a hazardous world under the same policy. Let \(P_0^O,P_1^O\) be the distributions of all observations available by the last useful response time, including ordinary production and the controller's randomization. If reopening must occur with probability at least \(1-\beta\) in the hazardous world and at most \(\alpha\) in the healthy world, with \(\alpha<1-\beta\), then

\[
D_{\rm KL}(P_1^O\Vert P_0^O)
\ge \operatorname{kl}(1-\beta,\alpha).
\]

This is the standard relative-entropy data-processing bound applied to the binary reopening event. Under a bounded conditional-information model, at most \(n\) paid samples with divergence at most \(D\), plus ordinary evidence contributing at most \(I_o\), require

\[
nD+I_o\ge\operatorname{kl}(1-\beta,\alpha).
\]

The inequality is necessary, not sufficient. A relevant primary treatment of adaptive change-of-measure arguments is [Kaufmann, Cappé, and Garivier (2016), Lemma 1](https://jmlr.org/papers/volume17/kaufman16a/kaufman16a.pdf). Information inherited from history belongs in the transcript; an omitted cash or output signal cannot be declared unavailable simply to make a paid diagnostic appear valuable.

Waiting can also change belief through known dynamics. With onset probability .1 and clearance .05, a posterior \(p\) ages to \(.1+.85p\). A negative finding does not freeze the world in the state it described. No new paid observation therefore does **not** imply that reopening is impossible: a timed policy can reopen, but may be less discriminating.

A separate continuous recovery certificate isolates a further obstruction. After repair, suppose

\[
\dot x=g-\delta x,\qquad \dot b=\kappa x-o-m.
\]

Let the sustainable stock be \(x_*=g/\delta\), its net operating margin be \(A=\kappa x_*-o-m>0\), and the initial output deficit relative to that stock be \(D=\kappa(x_*-x_c)\). If \(D>A\), the exact cash bridge required during the recovery dip is

\[
b_c\ge\frac{D-A-A\log(D/A)}{\delta}.
\]

Assumptions include the stated trajectory, an independently viable physical stock path, and no binding cash ceiling during the dip. If \(D\le A\), no dip occurs. For example, \(A=1,D=3,\delta=1\) requires approximately .9014 units already accessible at repair, despite the positive eventual margin. This certificate is analytically derived by minimizing cumulative net output; it is a separate continuous model, not a fitted equation for the discrete experiment.

These requirements must be met **jointly**. More eventual information cannot pay an earlier bill; more future revenue cannot repair a stipulated irreversible loss after its deadline. The balance, observation, and timing constraints are candidates for implementation-independent foundations, conditional on the dependencies being correctly identified. Their satisfaction alone says nothing about the legitimacy of the response.

## 3. An exact finite model with earned revenue

The [experiment](../../experiments/recoverable-inquiry/README.md) uses observed stock from zero to three, cash from zero to eight, diagnostic readiness, and a hidden fault. A ready apparatus costs one per period to retain; a test costs two. Rebuilding costs three and takes until the next period. A noisy binary test has sensitivity and specificity .9. Direct repair costs three and remains possible without testing.

After optional diagnosis and repair, stock changes by

\[
x'=\operatorname{clip}(x+1+u-2D,0,3),
\]

where \(u\) indicates repair and damage \(D\) occurs with probability .1 if healthy and .8 if faulty. Repair clears the current fault before damage. Zero stock is an imposed absorbing failure boundary. Income \(2x'\) arrives **after** all current payments. Reserves above eight pass to a treasury that cannot finance later actions. Productive technology and environmental inputs remain supplied; making income endogenous does not make the system physically closed.

Every observed stock transition updates the fault posterior. Cash and output deterministic from that transition are not counted as independent evidence. Exact rational probabilities generate the finite belief graph; floating-point Bellman calculations evaluate policies. The initial fault probability is zero, but the fault can arise later.

The expected cost is expenditure minus output, **minus** terminal stock salvage value (two per unit), plus a twelve-unit collapse penalty. A separate constraint bounds

\[
\mathbb E\sum_{t<H}
\left[\mathbf1\{\text{repair while its fault target is absent}\}
+.05\mathbf1\{\text{test}\}\right]\le\eta.
\]

The target-absence probability is assessed **before** repair clears the fault. Because repair also improves stock, a target-absent repair can still be useful. This chosen burden is not a count of necessarily mistaken decisions, a complete measure of harm, or a universal ethical standard. It is a finite-horizon expectation, not a pathwise cap or a lifetime error guarantee.

We compare adaptive diagnostic access, ordinary production evidence without paid tests, and a compulsory-service benchmark that keeps/rebuilds and tests whenever affordable. All receive the same production and repair technology, initial resources, and ordinary observations. Actual spending differs. A Lagrange calculation supplies deterministic policies; an ex ante lottery between two policies meets the expected constraint, with a separately recorded dual bound certifying numerical accuracy. Component policies need not satisfy that constraint individually.

## 4. What the calculation found

The original five-period case with burden allowance .6 bought **no tests**. All twelve initial five- and six-period development cases also bought none. These negative results remain in the record. Ordinary evidence and direct repair can make paid diagnosis unnecessary.

At eight periods and allowance .02, adaptive access improves expected cost from −42.908108 to −43.127292 compared with ordinary evidence alone. Collapse probability falls from 17.5176% to 12.4389%. Both meet the same .02 expected burden bound. Expected paid tests are .137530 and expected rebuilds .295752. The advantage in the objective is modest, about .219184 cost units; this is a mechanism example, not a large general effect.

A selected possible path is concrete: start healthy at stock three and drop readiness; continue ordinary production; observe stock fall to two and update the fault probability upward; pay three to rebuild; stock then falls to one while rebuilding; pay upkeep and test; after a positive result, pay for repair and return to stock three. Every payment is funded before the resulting output arrives. The saved path is deliberately selected, not a representative random run. It shows restoration after dropping initial readiness and the **first paid test within this horizon**, not a demonstrated negative-test→long-pause→retest sequence.

At allowance .05, both adaptive and no-test modes instead use no paid diagnosis and achieve the same cost −47.263097 and collapse probability 1.1815%. A tighter target-absence/testing limit therefore changes the value of information while allowing more productive failure. This is not evidence that tighter overall safety is bad: the constrained quantity is explicitly narrower than total harm.

The compulsory-service mode has minimum expected burden .371175 over eight periods. It is infeasible at .02 and is not assigned a misleading “feasible” comparison cost there. Its expense at looser budgets remains reported. The main nine-budget frontier and seven additional controls are all retained; the declared study contains 34 cases, including restricted-mode infeasibility.

The controls also qualify the mechanism. A completely uninformative paid test reproduces the no-test optimum. Starting with cash two instead of eight, or with no initial readiness, leaves the highlighted result unchanged: the selected policies can earn enough before rebuilding. Lower initial stock and halved output remove paid testing in the selected controls. Halving output changes both returns and financing, so it does not isolate a pure liquidity effect. A known-absent fault needs no diagnostic, but healthy random stock damage still makes direct repair potentially useful.

Seven independent tests pass, including direct latent-event enumeration, exhaustive one-period policy mixtures, and two-period occupancy linear-program checks. Across all feasible declared cases, the largest primal–dual gap is 8.81e−9 and the largest expected cash-ledger residual is 7.11e−15. These verify computations within the supplied model, not empirical adequacy. Exact run inputs, a later strengthening of test assertions, and both original and clearer figure layouts are retained separately.

## 5. What this changes in the larger theory

The previous result warned that recurrent shortfalls can extinguish inquiry despite positive returns. This result adds that preserving the **option of warranted correction** can require a changing combination of ordinary observation, cash, dormant readiness, rebuilding, and direct action. Permanent testing is only one possible implementation, and it can be inferior.

The finite horizon remains decisive. If each test imposes at least \(h_0>0\) burden and infinitely many tests are required in expectation, total undiscounted expected lifetime burden cannot be finite: it is at least \(h_0\mathbb E[N]\). Likewise, summable per-episode false-alarm allowances approach zero; with a uniform bound on information before each genuinely new episode's deadline, uniform detection power eventually becomes impossible by the KL bound above. These statements do not rule out learning one persistent fact, time-uniform inference under valid assumptions, vanishing test costs, or a permanent response that ends the need for testing.

The tested decision problem does not implement an infinite-horizon statistical guarantee. A long-run burden rate, a finite-period budget, and a probability of ever making an error are different commitments. Changing the criterion can be legitimate, but cannot be hidden behind the same word “safe”.

This is a close application of existing research. [Van Oosterom, Maillart, and Kharoufeh (2017)](https://repub.eur.nl/pub/102727/) jointly optimize system and sensor maintenance. [Brázdil and colleagues (2016)](https://arxiv.org/abs/1602.07565) distinguish hard resource feasibility from expected cost in partially observed control. [Banerjee and Veeravalli (2013)](https://arxiv.org/abs/1211.3729) study on/off observation under sampling and false-alarm constraints. The full [prior-art audit](../../_process/research/2026-10-04-integrated-evolution/recoverable-inquiry-prior-art.md) also covers production as evidence and statistical restart. No originality is claimed for these ingredients.

The research contribution sought here is a disciplined account of their conjunction: how a process can spend, lose, or regenerate its capacity to discover and enact a correction while financing that capacity from what correction helps preserve. The model still supplies the purpose, probability family, repair option, and authority. It therefore cannot yet explain legitimate disagreement or the formation of new purposes and conceivable responses.

## 6. The next frontier: feasible correction without a shared score

We should now stop adding mechanisms merely to make the model larger. The next target is to replace the single supplied objective with explicit, potentially conflicting requirements belonging to different affected parties. Which combinations remain attainable under the available evidence, timing, resources, and authority? When does failure arise from physical limits, unresolved uncertainty, conflicting requirements, or an institution's restriction of an otherwise available correction?

A finite model can represent attainable **vectors** of consequences. With admissible ex ante lotteries these vectors form a convex set, and separating weights can certify that a proposed package of thresholds is infeasible. Such weights are mathematical witnesses to incompatibility; they are not a discovered common utility. If lotteries across people or outcomes are unacceptable, expected-vector convexification is itself inappropriate. Removing authorized actions while holding everything else fixed can only shrink the attainable set; changing institutions more broadly can also change information and resources, so that simple inclusion argument must not be overextended.

This is an unrun next target. It would let the theory distinguish “we cannot meet these requirements together” from “the current controller is not permitted or rewarded to do so,” without pretending that coordination requires every person to share one scalar goal. Changing purposes and legitimate revision remain further questions rather than conclusions supplied by the optimization.

Supporting records: [mathematical derivations and independent tests](../../_process/research/2026-10-04-integrated-evolution/recoverable-inquiry-math.md), [design audit](../../_process/research/2026-10-04-integrated-evolution/recoverable-inquiry-design-review.md), [experiment and reproduction](../../experiments/recoverable-inquiry/README.md), [claim register](../../_process/research/2026-10-04-integrated-evolution/CLAIMS.md), and [research log](../../_process/research/2026-10-04-integrated-evolution/RESEARCH-LOG.md).
