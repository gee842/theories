# When total funds suffice: a finite access theorem and its boundaries

Formal research appendix, 5 October 2026. Companion to [the access study](access-and-correction.md). The frozen protocol, local inherited-model snapshot, verification scripts, and exact results are in [the reproduction bundle](access-study-evidence.zip). No source-workspace or root experiment files were changed. This memo proves a stronger positive result than the observation that inaccessible money may be unusable. The result is conditional and not claimed novel.

## 1. Precise result

**With guaranteed free, immediate transfers, a sufficiently large cash cap, lossless overflow storage, and no other effects of account location, replacing separate accounts by total funds preserves all attainable operational outcome laws under an explicit normalization interface.** It need not preserve literal transfer/payment actions or account-specific outcomes.

The distinction is important. The negative example refutes a raw total-money projection under restricted access. The positive theorem identifies conditions under which that projection can be repaired by changing the action interface to “make the available money spendable, then act.” This is a proved transformation of a declared model, not evidence that real accounts are interchangeable.

The frozen experiment has cash cap 8 and maximum full-round bill 6. Its immediate-access mode already performs the required normalization automatically before each round. The main positive numerical check therefore verifies an algebraically warranted contract; it is not an independent discovery of financial fungibility.

## 2. Objects and assumptions

Write the financial state as \((b,t,p)\), where \(b\) is accessible cash, \(t\) treasury funds, and \(p\) the access mode. Use \(\pi\), rather than \(p\), for the hidden-fault posterior. Let \(z\) retain remaining horizon, productive stock, readiness, posterior, and all other nonfinancial variables needed for the declared process. Total funds are \(N=b+t\).

For the positive result assume:

1. \(0\le b\le C\), \(t\ge0\), with a fixed cash cap \(C\). The horizon is finite.
2. Access is guaranteed whenever normalization is required. Treasury-to-cash transfers take zero time, cost nothing, and preserve total funds. They have no effects on production, observation, risk, authority, or the protected outcome vector.
3. Operational/infrastructure payments are nonnegative and occur before new income. Every complete round, including every diagnostic-contingent branch, has total bill at most \(L\le C\).
4. Income \(I\ge0\) is credited after the round's payments: fill cash to \(C\), retain every remaining unit in treasury. There is no inaccessible external overflow sink in the immediate-access model.
5. Conditional on the retained physical/belief state and the chosen nonfinancial actions, the environment and primitive observation laws do not depend on the partition between the accounts. The split supplies no additional hidden-state information omitted from the retained posterior.
6. There are no holding costs, distinct account yields, seizure risks, transfer fees, transfer-dependent rewards, signaling effects, or terminal preferences over the partition. Criteria may depend on physical outcomes, latent target absence, expenditures, action counts, total funds, and time; the same environment realization will be coupled below.
7. The comparison allows admissible observation-history policies with private randomization and memory sufficient to emulate a virtual financial ledger. No policy is allowed to spend funds it lacks or treat future income as current cash. The maximum-transfer procedure itself is implementable from observed account balances or by a declared authorized bank operation.

The original model gives sufficient-belief memory freely. This memo retains that idealization explicitly. If controller memory and computation are priced, one must also price and verify the virtual-ledger implementation; equality of ideal attainable sets would then not establish equality of physically affordable controller sets.

All finite-horizon reachable totals are bounded: in the primary H4 grid, initial total is 5 and each round earns at most 6, so \(N\le29\). An unbounded treasury type therefore does not create an infinite reachable financial state set for this experiment.

## 3. The banking identity

Define the canonical split of a nonnegative total by \(\kappa_C(N)=(\min(C,N),(N-C)_+)\), and normalization of valid accounts by

\[
\nu_C(b,t)=\bigl(\min(C,N),(N-C)_+\bigr),\qquad N=b+t.
\]

It moves \(\min(t,C-b)\) into cash. It preserves \(N\), is idempotent, and makes every same-total partition identical at the start of the operational round.

After a feasible total payment \(c\le\min(C,N)\), then income \(I\), cash and treasury become

\[
b'=\min\{C,\min(C,N)-c+I\},
\]
\[
t'=(N-C)_++[\min(C,N)-c+I-C]_+.
\]

Consequently

\[
b'+t'=N-c+I,
\qquad
\nu_C(b',t')=\kappa_C(N-c+I).
\tag{1}
\]

Because all payments are nonnegative and no income arrives between them, an affordable full realized bill makes every earlier prefix affordable. A contingent prescription must still be feasible on every possible diagnostic branch. Since \(L\le C\), normalization once before the round is sufficient for every financially feasible branch; no hidden within-round transfer is required.

The operational state \((z,N)\) therefore has closed finance dynamics \(N'=N-c+I\). This is a genuine exact macro transition, provided the nonfinancial kernel and observation assumptions also hold.

## 4. Proposition 1: exact quotient of the normalized operational model

Consider the frozen immediate-access model at living, nonterminal decision points, and use as its action a complete operational prescription: infrastructure choice, test/no test, and diagnostic-contingent repair rule. Let

\[
q(z,b,t,0)=(z,b+t,0).
\]

For same-total states, normalization produces the same cash and treasury before the prescription is selected. Thus:

- The feasible operational prescriptions are the same, including every prefix constraint.
- The conditional laws of diagnostic observations, physical transitions, expenditure, target-absence burden, and output are the same for a common prescription.
- The next total satisfies (1); the posterior and readiness updates are the same.

Therefore \(q\) is an exact action-conditioned stochastic quotient **for this normalized macro interface**. The primary outcome vector \((F,E,B,U)\) is preserved. So are action counts and earned output. Terminal total funds are preserved. Terminal cash and treasury separately need not be preserved by an arbitrary total projection; in the particular living H4 comparison, the first normalization makes the full subsequent state laws identical under common prescriptions, which is stronger.

**Proof.** Equality of the normalized financial states gives equality of prescription availability. By assumption 5, the same prescription has the same primitive observation and physical-outcome law. The finance update's pushforward depends only on total funds, the realized cost, and income by (1). The retained posterior, readiness, and time updates agree. Induction over the finite horizon yields equal operational trajectory laws for every common operational policy and hence equal declared outcome vectors. At terminal or collapsed states the operational criteria depend only on the retained terminal physical state, and no further payment is available. ∎

This proposition does not claim equality of arbitrary policies that deliberately choose different actions in the two systems. It pairs each policy with its counterpart through the specified interface. An identical deterministic tie rule will choose matching optimal metrics when it sees identical normalized states and action orderings.

## 5. Proposition 2: normalization does not remove attainable operational outcomes from arbitrary lawful transfer policies

Now enlarge the concrete comparison class: the controller may choose any lawful partial transfer, or no transfer, before operating. The round's other assumptions remain unchanged. Transfer decisions may depend on its legitimate history and private randomness. Let \(\mathcal A_{\rm raw}(z,b,t)\) be the set of attainable laws of retained operational/environment traces, excluding transfer amounts, account-specific signals, and individual account paths. Let \(\mathcal A_{\rm norm}(z,N)\) be the corresponding set under compulsory maximum normalization and operational policies with the same history/random-memory allowance.

Then

\[
\boxed{\mathcal A_{\rm raw}(z,b,t)=\mathcal A_{\rm norm}(z,b+t).}
\tag{2}
\]

This includes the joint latent physical path for assessing target-absence burden; it does not grant either controller observation of that hidden path. In particular, all attainable primary expected vectors are equal, not merely one scalar optimum or the efficient frontier.

**Proof, normalization to raw.** A raw controller can choose the maximum lawful transfer each round and then execute any normalized controller. All actions, observations, physical outcomes, and costs can be coupled identically.

**Proof, raw to normalization.** Fix any admissible raw controller and initial split. A normalized controller stores a virtual copy of that raw controller's ledger, action history, and private random state. It executes the raw controller virtually, including its partial-transfer decisions, and takes the same nonfinancial actions in the actual normalized system. Couple the systems using the same diagnostic and physical random outcomes. At the start of a round, normalized cash is \(\min(C,N)\). The virtual raw controller can have at most that much cash. Any complete raw feasible branch costs at most \(N\), at most \(L\le C\), and therefore fits in normalized cash. Every nonnegative payment prefix also fits. By the account-independent environment assumption, the same nonfinancial choices give identical physical signals, costs, burden, and income. Both total accounts change by \(-c+I\). The virtual ledger can be updated exactly from its earlier balances, chosen transfer, payments, and observed income. Continue inductively. Thus every raw operational law is achieved in the normalized system. ∎

The policy can intentionally refrain from an action that has become affordable. Extra liquidity does not compel extra treatment, testing, or spending. This fact is needed for equality, rather than only an ability to achieve “better” outcomes.

The theorem concerns **lawful** policies. If the raw model admits deliberate invalid-payment attempts that trigger a special failure sink, that behavior is outside the stated feasible-policy class. Equality would require adding the same failure-producing action to the macro model or restricting attention to admissible policies. Similarly, a resource-oblivious controller class or a fixed installed program might not contain the virtual-ledger implementation.

For the exact finite belief MDP, scalar optimization can use deterministic Markov policies. The policy-emulation proof permits more history because it compares arbitrary transfer strategies. Equality of attainable expected vectors can alternatively be stated for randomized history policies; restricting both sides to a smaller stationary or memoryless class needs a separate argument and is not assumed here.

## 6. Raw labeled actions still fail to commute

Take \(C=8\), \((b,t)=(0,5)\) and \((5,0)\). Both have total 5 and granted permission.

- The literal action “pay 3 now, without preceding transfer” is feasible only from the second state.
- The literal action “transfer 5 into cash” is feasible only from the first state.

Thus the original same-label transition quotient fails. The operational prescription “make funds spendable, then pay 3” has an implementation in both states. Its cash transfer amount depends on the observed balance, but does not require hidden fault information.

This is a controller refinement with zero-time, zero-cost internal transfer steps. It is not a proof that transfer events, observers of those events, or raw microstep trace lengths are identical. If the original question concerns payment timing at microstep resolution, signaling, legal process, or a transfer's legitimacy, those discarded details may be precisely what matters.

## 7. A sufficient financial representation depends on the access regime

The protocol has three observed modes: \(-1\) is permanently barred, 0 is immediate, and 1 is barred this round then immediate. A useful sufficient representation is a typed union:

\[
\psi(z,b,t,p)=
\begin{cases}
(z,-1,b), &p=-1,\\
(z,0,N), &p=0,\\
(z,1,b,N), &p=1.
\end{cases}
\tag{3}
\]

For permanently barred funds, the treasury never affects operational feasibility or any primary metric. Cash evolves as \(b'=\min(C,b-c+I)\), and treasury can be omitted from this particular operational model. Its amount still matters for the bookkeeping identity, which is a different query.

For immediate access, Proposition 1 applies. For delayed access, current cash controls today's bills while total funds determine next round's normalized resources; keeping both suffices. There can be further horizon- or query-specific reductions, so (3) is sufficient rather than a globally minimal state representation.

**Adding permission to total is not enough in barred mode.** Both barred states can have the same total and still have different access. Conversely, retaining every account forever is unnecessarily detailed if a treasury is permanently irrelevant to every retained question. This is the positive structural result: the appropriate state depends on the intervention/permission contract.

If permissions can change later, the permanently barred reduction no longer applies. Two states with equal current cash but different treasury holdings can become operationally different when permission is granted. A current permission bit alone does not summarize the future permission process.

### Exact corollary: an institution change can invalidate an old sufficient state

Consider H2, stock2, readiness0, known current fault, accessible cash0, and treasury either0 or3. Under permanent exclusion, both states have minimum failure .612: both must do nothing in round one, and neither can repair after the adverse first-round stock transition. Thus treasury can legitimately be omitted within the permanently barred model.

Now enlarge the institutional transition family to permit a known unlock at the start of round two. At the current decision point both treasuries are still inaccessible, and every current accessible variable and action is identical. First-round damage has probability .8 and yields stock1 with income2. On this branch, next-round normalization gives the treasury0 state only2 and the treasury3 state5. The former cannot repair; the latter can pay3 and avoid collapse. The exact minimum failure probabilities are therefore .612 and0. The treasury3 witness again has expected expense2.4 and absent-target burden .04. Without first-round damage, both survive the one remaining round regardless.

The predictive question—attainable two-round survival—has stayed fixed. What changed is the admitted future permission mechanism. A summary sufficient under permanent exclusion is no longer sufficient in the expanded family. This is a structural analogue of inherited claim U20's model-relative sufficiency, not a demonstration of discovery of unconceived institutions or a general claim that all historical details should be retained.

## 8. A two-round failure that cannot be detected from the first action menu

Use the frozen process with horizon 2, stock 2, readiness 0, known initial fault \(\pi=1\), total funds 5, and permanently barred treasury. Compare accessible cash 0 and 1. Both have the same sole first operational action: drop readiness, no test, no repair.

First-round damage has probability .8. Damage leaves stock 1 and produces income 2. The two cash balances become 2 and 3. If damage does not occur, stock becomes 3, and collapse is impossible in the one remaining round even without repair.

After the first damage observation, the next-round fault posterior is .95: the fault has clearance probability .05. Without repair, second-round damage has probability

\[
.95(.8)+.05(.1)=.765.
\]

The cash-0 initial state now has only 2 and cannot pay the repair cost 3. Its minimum two-round collapse probability is therefore

\[
.8(.765)=.612=153/250.
\]

The cash-1 initial state now has 3 and can repair when stock fell to 1. Repair clears the fault and gives stock increment 2 before any damage, so even damage leaves stock 1 rather than zero. Its minimum collapse probability is exactly zero. This witness policy spends expected \(.8\times3=2.4\), and its expected absent-target repair burden is \(.8\times.05=.04\). It buys no test.

The distinction is generated by a later payment threshold after endogenous income. Equal current total funds and equal current action menus do not suffice for a closed dynamic abstraction. The analytic witness was known before the main H4 run; it is not held-out evidence.

## 9. Boundaries: delay, fees, capacity, observations, and terminal preferences

**Delay.** With one round remaining, stock 1, known fault, readiness 0, and total 5, a transfer available only next round cannot finance the present repair. Cash 0 has minimum collapse probability .8; cash 3 can repair and achieve zero. Delayed funds are not made current by having the same eventual total.

**Transfer fees.** Suppose a repair costs 1, total funds are 1, and transferring from treasury incurs a separate fee 1. State \((1,0)\) can repair, while \((0,1)\) cannot cover both transfer and repair. Even when both could repair, unequal transfer fees can change the expense coordinate. Maximum normalization may then itself be wasteful relative to a just-enough transfer.

**A cap below the round's total bill.** With cash cap 1 and total 2, two mandatory payments of 1 cannot both be funded by one start-of-round normalization if no transfer is allowed between them. A rule looking only at total bill \(2\le N\) would be false. Allowing another transfer between payments repairs that different model. The frozen model avoids the problem by maximum bill \(6\le8\).

**Account-dependent losses.** Distinct interest, holding costs, seizure risk, overflow destruction, or production effects of the balance can make normalization change the future total or physical process. Equation (1) and the coupling must then be rederived.

**Information or signaling.** If the initial split is correlated with the hidden fault and its information is omitted from the retained posterior, merging splits loses information. If observed transfers change another actor's actions, omitting transfer behavior changes the causal process. Neither case satisfies the common-kernel assumption.

**Account-specific terminal obligations.** “Leave one unit in treasury” and “leave one unit in immediately accessible cash” are different predicates. Total funds alone cannot preserve them. The primary protocol explicitly excludes terminal partition preference while retaining both balances for audit; the distinction must remain visible in reporting.

**No free controller implementation.** A finite memory budget can prevent simulation of an arbitrary virtual ledger. A fixed policy might automatically spend any accessible amount, so greater liquidity changes its behavior. Proposition 2 compares selectable policies in a declared class, not every installed controller's response to a transfer.

## 10. Entire attainable sets, frontiers, and seven support probes

Propositions 1–2 establish equality of all attainable primary expected vectors under their contracts. This is stronger than the equality of efficient frontiers. For example, attainable sets \(\{(0,0),(1,1)\}\) and \(\{(0,0)\}\), with both coordinates minimized, have the same efficient point but differ as sets. Their convexifications still have that distinction.

Conversely, checking finitely many scalar support directions cannot prove equality of entire frontiers or attainable sets. In two dimensions, the convex hull of \((0,2),(2,0)\) and that hull enlarged with \((.9,.9)\) have identical minima in each coordinate separately, but different minima of their sum. A finite probe set can miss a difference in an unprobed direction.

For a finite experiment with arbitrary ex ante lotteries, attainable expected-vector sets are compact and convex. Equality of their support functions in **all** real directions characterizes equality of the sets. The frozen seven directions are a useful, declared subset. A difference in any one proves inequality; agreement in all seven is inconclusive unless an independent structural theorem applies. No sampled lottery is needed to optimize a single linear support direction: at least one deterministic finite-horizon policy attains its optimum.

A lexicographic tie rule selects one point among policies with the same primary scalar value. Equal support values by themselves do not imply equal selected metric vectors if the policy spaces or tie rules differ. Under immediate normalization the full normalized state, operational action set, dynamics, and tie rule coincide, which supplies the stronger equality used by the protocol.

## 11. Access monotonicity and its limits

For the same initial accounts and environment, allowing immediate free access permits emulation of a delayed or permanently barred policy by maintaining its virtual ledger and taking the same nonfinancial actions. Likewise, delayed access can emulate permanently barred use. Under the same history/random-memory and account-neutral criteria assumptions,

\[
\mathcal V_{\rm barred}\subseteq
\mathcal V_{\rm delayed}\subseteq
\mathcal V_{\rm immediate},
\]

where \(\mathcal V\) denotes attainable operational expected vectors. Hence the minimum of each fixed scalar support direction under immediate access is no worse than under delayed/barred access.

This does not say every coordinate of the selected policy improves, that every installed controller improves, or that equality is impossible. A failure-minimizing policy may spend more or impose more target-absence burden. The institutional validity of the access rule remains an external question.

An initially all-liquid state is not automatically an all-horizon equality control: later production can create treasury overflow, and later bills can make it useful. The protocol correctly records that proposed control expectation as something to check, not as a theorem. Known-safe controls likewise need their stated damage/onset assumptions; “fault absent now” does not alone remove later need.

## 12. Verification and status

`formal_access_verify.py` independently enumerates 53,228 canonical payment/income identities over caps 1–8, totals 0–30, incomes 0–6, and all admissible partitions and payments. It also checks 73,130 two-payment prefix-dominance cases, and exactly recomputes the H2 .612 versus 0 witness, its 2.4/.04 expense/burden, the H1 delayed-access boundary, and the delayed-unlock model-expansion corollary. Results are saved in `formal_access_checks.json`.

Those checks support the formulas and analytic examples. They do not independently solve the main H4 support-probe grid, demonstrate empirical adequacy, or discover a universal access law. The general preservation claims follow from the stated proofs and require each assumption to be checked when transported to another setting.

The useful conclusion is conditional: a resource sum becomes an adequate operational state only when the access, timing, observation, cost, and outcome contracts make the different partitions interchangeable for the permitted procedures. The present model supplies one exact positive case and several exact ways it can fail.
