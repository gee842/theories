# What the absence of paid tests establishes—and what it leaves open

Analytic continuation, 5 October 2026. This note interprets completed results and a small separating witness. It does not alter the frozen H4 study or claim substantive transfer to a second implementation.

## Three different claims

1. **Finite tested absence.** Every selected optimum in the 1,134-case H4 support-probe study had zero expected test count. Therefore, for each tested starting state and scalar direction, there is a no-test policy attaining the optimum of the test-available problem. The optimum over no-test policies equals the unrestricted optimum at those tested points. This says nothing about unprobed priorities or initial conditions, and does not mean a single policy optimizes all priorities.
2. **Structural dominance.** A theorem of this kind would require that every testing policy in a stated model class has a feasible no-test counterpart with no worse declared outcomes. The finite grid does not establish that quantification. A same-technology counterexample below disproves it for the broader family of initial states and priorities.
3. **Inquiry is useless.** This would range over further questions, information channels, purposes, resource rules, horizons, and institutions. Neither the computation nor a restricted dominance theorem supports that claim.

The original process has direct repair without a diagnosis; repair also improves productive stock even when its fault target is absent. It charges upkeep 1 plus test 2 before any repair cost 3, and rebuilding costs 3 with a one-round lag. These mechanisms can reduce the value of diagnosis. Their joint presence plus the no-test result does not separately identify which mechanism explains every selected case. Ordinary stock observations also already carry information.

## An exact informative-diagnosis witness

Keep the same productive and diagnostic technology, cost schedule, damage probabilities, and burden definition. Change the decision state and stated priority: one round remains, stock is 1, the diagnostic is already ready, fault prior is 1/2, and accessible cash is 6. These conditions lie outside the original main grid, which had H4, initial readiness 0, and total funds 5. This is an exploratory separating example, not a retrospective correction to that grid.

The sensor has sensitivity and specificity .9. Maintain, test, and repair only on a positive signal. A positive occurs with probability .5. The resulting primary vector is

\[
(F,E,B,U)=(.085,4.5,.1,.135).
\]

Here:

- The only collapse branch is a negative signal followed by damage without repair: \(.5(.9)(.1)+.5(.1)(.8)=.085\).
- Upkeep and test cost 3, and repair costs another 3 with probability .5, giving expense 4.5. The positive branch's full cost 6 is prepaid and affordable.
- Target-absent repair occurs with probability \(.5(.1)=.05\); adding test burden .05 gives burden .1.
- A positive signal followed by healthy-state damage after repair leaves stock 1 with probability \(.5(.1)=.05\). Together with collapse, terminal stock-below-two probability is .135.

For any no-test policy in this one-round case, let \(q\) be its probability of repair. Its action cannot depend on the hidden fault, and additional upkeep without a test has no remaining physical value. Hence

\[
F=.45(1-q),\qquad B=.5q,\qquad E\ge3q,
\]

with equality in expense when needless upkeep is omitted. Requiring \(B\le.1\) forces \(q\le.2\), so every no-test policy has \(F\ge.36\). The diagnostic policy reaches .085 while respecting the same burden bound and an expected-expense ceiling 4.5. Thus it makes the joint requirements \(F\le.1,B\le.1,E\le4.5,U\le.15\) attainable; no no-test lottery can meet them. Those numerical requirements are illustrative commitments, not derived ethical standards.

Equivalently, the scalar probe \(20F+E+10B\) gives:

| Policy | F | E | B | Weighted result |
|---|---:|---:|---:|---:|
| No test, no repair | .45 | 0 | 0 | 9 |
| No test, direct repair | 0 | 3 | .5 | 8 |
| Test, repair positive | .085 | 4.5 | .1 | **7.2** |
| Test, repair negative | .365 | 4.5 | .5 | 16.8 |
| Test, repair neither | .45 | 3 | .05 | 12.5 |
| Test, repair both | 0 | 6 | .55 | 11.5 |

Keeping readiness without testing only adds 1 to the corresponding no-test cost. This exhausts the deterministic one-round prescriptions. Randomization gives convex combinations and cannot improve the minimum linear score, so repair-positive is uniquely optimal for this probe.

## Information, rather than extra treatment, explains the separating effect

Replace only sensor accuracy by sensitivity=specificity=.5. Under the **same** test-and-repair-positive policy, a positive still occurs with probability .5. Repair frequency and expected expense remain exactly .5 and 4.5. Outcomes become

\[
(F,E,B,U)=(.225,4.5,.3,.275).
\]

The informative sensor therefore lowers failure and target-absent treatment at matched expected spending and repair frequency. Its value comes from making the decision correlate with the hidden fault; it does not come from simply doing more repair. The informative policy is not better than direct repair in every coordinate: direct repair has lower failure and lower expense but much larger target-absence burden.

There is a genuine restricted dominance theorem for the uninformative sensor. If its output is conditionally independent of the hidden state and future environment given information already available, and testing has no other beneficial side effects, its output can be simulated by a free private coin with the same conditional distribution. A controller can execute the same subsequent decisions with no larger expenditure and no test burden. If its original decisions depend on remaining cash, a virtual ledger can emulate the original spending path. Nonnegative costs, no harmful effects from retaining cash, and adequate memory are required. Under these assumptions paid uninformative testing cannot improve the attainable efficient outcomes at any finite horizon. That argument does **not** apply to the .9/.9 sensor.

## Every finite horizon versus an infinite process

The pooling theorem applies to each finite horizon satisfying its hypotheses; it is stronger than checking H4 and weaker than saying an actual institution can operate forever. Three distinctions matter:

- Equality of what two models can attain does not prove that either can attain indefinite survival. Both can have the same eventual-collapse probability, including one, or the same unbounded lifetime expense.
- Quantifying over finite horizons does not, by itself, select one controller valid for all time. In some finite-state safety problems compactness or a fixed-point argument supplies that extension; it is an additional argument, not a consequence of the phrase “every finite horizon.”
- The present **policy-emulation construction** is actually online and independent of the chosen horizon. If the access and banking assumptions remain valid indefinitely, infinite executions are well-defined, and sufficient memory remains available, the same virtual-ledger adapter can be run at every time. Couple the models on the same infinite stream of environmental random choices. The construction preserves every operational step, so it preserves the whole operational path and any specified measurable event of that path. Nonnegative lifetime costs can be compared as extended sums, possibly infinite. This gives an infinite-path equivalence under stronger maintained assumptions; it still proves no perpetual feasibility, finite total burden, or empirical permanence of those assumptions.

The published finite result did not establish those indefinite implementation assumptions, and no additional infinite-horizon numerical claim is needed to interpret it correctly.

## Mathematical consequences and substantive transfer

A parameterized theorem can have infinitely many instances or derived consequences without being a complete empirical account. Counting consequences does not validate the assumptions in a new setting. The diagnostic witness is another instance of the same simulator's technology, not an independent physical implementation.

The currently missing transfer evidence is specific: identify a second implementation, measure its access, latency, observation, and payment mechanisms independently of its recovery outcomes, freeze the mapping and predictions, and then evaluate those predictions. A formal preservation theorem tells us what would follow **if** that mapping meets its conditions. It does not establish that the mapping actually does so. More simulator elaborations can expose limits and suggest measurements, but cannot replace that test.
