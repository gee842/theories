# Access and attainable correction

Local protocol frozen before the main numerical run, 5 October 2026. This is a constructed finite-model study, not external preregistration or empirical evidence. It executes the first access-only stage of `outputs/next-test.md`. New input versions or unplanned analyses must be recorded separately.

## Question and prospective predictions

Does projecting accessible cash and a treasury to their sum preserve attainable correction outcomes? Keep productive stock, readiness, remaining horizon, full posterior information, and access mode in the projection. This isolates account access from other omissions.

Predictions fixed before the main run:

1. With a barred treasury, at least one same-total pair differs in a minimum linear support value over the declared outcome vector. A witness need not differ in its initial action set.
2. With free immediate maximal transfer before every round, every same-total partition has equal operational support values and projected metric vectors, under the same tie rule. Formal work will distinguish this normalized macro-action interface from literal transfer/payment labels.
3. Access delayed until the second round can retain dependence on the initial cash partition; imminent bills matter.
4. Access is weakly useful in nested feasible-policy classes, but it need not be strictly useful. All-liquid and known-safe/no-damage controls should exhibit no benefit. Removing production can remove a delayed cash-threshold distinction.

## State and chronology

State: `(remaining, stock, cash, treasury, readiness, fault posterior, unlock counter)`. Posterior is an exact rational. Stock lies in 0..3, accessible cash in 0..8, treasury is nonnegative with no cap; reachable treasury is finite at finite horizon. Unlock counter -1 means barred forever, 0 free immediate access, and 1 barred this round then free from next round. All are observed. The fault is hidden; all ordinary stock, cash, income, readiness, permission and diagnostic signals are observed. Memory of a sufficient posterior is free, as in the inherited model.

For a living nonterminal state with counter zero, normalize first: move `min(treasury,8-cash)` into cash, without fee or delay. No other transfer occurs within the round. This is an explicitly chosen macro-action interface. Generalization to arbitrary transfer policies requires a separate refinement proof; literal transition equivalence is not assumed.

Then use the inherited productive/inquiry process:

1. Choose drop (fee0, next readiness0); if currently ready choose keep (fee1, next readiness1); if currently unready choose rebuild (fee3, next readiness1). Rebuilt equipment cannot test in the current round.
2. Only keep on already ready equipment allows a diagnostic, costing2 and having sensitivity and specificity .9. Fees are paid before new income.
3. Choose repair/no repair conditional on any diagnostic. Repair costs3, resets the current fault to absent, and contributes +1 in the stock update. Every branch must be affordable using current normalized cash.
4. Damage D is Bernoulli(.1) when healthy and Bernoulli(.8) when faulty. Stock becomes `clip(stock+1+repair−2D,0,3)`. Observed stock/output are filtered jointly, once, including clipping.
5. Income `2*new stock` arrives after all bills. Fill cash to cap8 and retain every excess unit in treasury. Transfers conserve total accounts. Fault then evolves with onset .1 and clearance .05; posterior aging is `.1+.85*p` after the production observation. Unlock counter1 becomes0.
6. Stock0 is absorbing; activity and income stop. At horizon end no extra actions or transfers occur. Terminal account balances remain in the ledger.

No credit, borrowing, legal interpretation, strategic capture, policy selection, or evolving recognition is modeled. The largest full round bill is6, below cash cap8. Terminal cash allocation carries no preference or reward.

## Outcomes and optimization

Primary vector to minimize: `(F,E,B,U)` where F is probability of ever reaching stock0, E is expected total paid expenditure, B is expected repairs made when their fault target is absent plus .05 per paid diagnostic, and U is probability terminal stock is below2. Stock0 is absorbing, so F equals terminal stock0 probability. U is a stipulated terminal recovery criterion, not all notions of timely recovery. B is a limited burden proxy, not total harm: a target-absent repair can improve stock.

Also retain test count, repair count, rebuilding count, upkeep count, inquiry-only expense, output, and both terminal account balances. Conservation: terminal cash + terminal treasury + total expense = initial total accounts + earned output in expectation and on each branch.

Predetermined support directions `(F,E,B,U)`:

- `(1,0,0,0)` failure only;
- `(0,0,0,1)` terminal recovery only;
- `(0,1,0,0)` expenditure only;
- `(0,0,1,0)` burden only;
- `(12,1,0,0)`;
- `(12,1,4,0)`;
- `(4,1,1,4)`.

These are mathematical probes of attainable sets, not a selected social utility. Unequal minima of one linear probe certify unequal attainable sets. Equal values of seven probes do not prove equality of entire sets. No claim to compute a full Pareto frontier is made. Exact equivalence where established needs the formal map.

Tie order after scalar support is expenditure, burden, terminal-unrecovered probability, failure probability, tests, rebuilds, action index. Solve exact rational finite-horizon dynamic programming; retain selected actions and all metrics. If exact calculations prove too costly, retain the failure and change protocol explicitly before approximation; do not quietly relabel a floating optimum exact.

## Frozen main grid and controls

Main horizon4. Stock in {1,2,3}; initial total cash5 partitioned as cash0..5 and treasury5−cash; readiness0; prior fault in {0,1/2,1}; access barred/immediate/one-round-delayed. This is 162 initial conditions, each evaluated in seven directions. No sampled trajectories or statistical significance claims.

Verification uses horizons1 and2, including an independently derived witness at H2, stock2, prior1, readiness0, total5: barred cash0 versus cash1 have the same sole first action, but predicted minimum collapse probabilities .612 versus0. The better policy spends expected2.4 on repair and incurs expected target-absent repair burden .04. This is a preread analytic witness, not held-out evidence.

Controls fixed before the main run:

- Repeat H4 stock2 prior1, splits0/1/5, barred/immediate with output0 (removes the endogenous funding channel).
- Repeat H4 stock2 prior0, splits0/1/5, all three access modes with onset0 and healthy damage0 (no fault/physical deterioration).
- Repeat H4 stock1 prior1/2, splits0/1/5, all modes with initial readiness1 (checks the inquiry interface).
- Repeat H4 stock2 prior1, splits0/1/5, barred/immediate with completely uninformative test sensitivity=specificity=.5.
- All-liquid partition cash5,treasury0 is included in every base grid group; permission can still matter later if new overflow becomes trapped, so equality there is a proposed control expectation to check, not a theorem over arbitrary horizons.

No H8/H12 outcome inspection in this cycle. Those remain separately frozen follow-on evaluations if the H4 model merits them.

## Verification and reporting

An independent agent checks the latent production/observation kernel, the H2 witness, cash timing, rebuilding lag, and small-horizon decision calculation. Check open normalized partition equality; controlled differences for barred/delayed; total probability one; branchwise conservation; cap and affordability. Record runtime, graph/node counts, exact rational outputs, code and protocol hashes, all grid results, controls, and failed prospective expectations.

The source reference workspace is read only. This task owns all snapshots, implementations, and results. No claimed empirical cross-domain transfer, universal completeness, or ethical derivation follows from this simulator.
