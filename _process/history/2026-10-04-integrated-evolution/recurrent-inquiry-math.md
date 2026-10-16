# Recurrent inquiry, aging evidence, and paid succession

Mathematical working memo, 5 October 2026. AI-generated research assistance under Ren's research direction. These are applications and elementary derivations within established decision theory, not originality claims or universal social laws. No experiment is implemented in this memo.

## 1. Two modules, with the boundary preserved

Use two explicitly separate models. Module A makes testing and maintenance decisions endogenous, while assuming that its controller retains a sufficient belief without charge. Module B prices transmission to one successor and correctly handles evidence carried by silence or other surviving channels. They are not an integrated model of paid institutional memory across repeated succession.

This separation avoids a substantive error: an unpaid archive does not automatically make a successor's Bayesian belief equal to the stationary prior. If a predecessor's capacity choice, balance, action, or decision not to send depends on its information, the surviving object can itself be evidence. Resetting the belief to one half despite that evidence would be an imposed restriction on reasoning, not ordinary Bayesian forgetting. An integrated successor model must specify the information interface and account for these channels, or explicitly evaluate a restricted controller architecture.

Finite-horizon belief-state optimization is established POMDP theory; [Smallwood and Sondik (1973)](https://doi.org/10.1287/opre.21.5.1071) already analyze finite-state hidden Markov control and a machine-maintenance example. For the genuinely decentralized extension, [Nayyar, Mahajan, and Teneketzis](https://arxiv.org/abs/1209.1695) formulate dynamic programs in which a coordinator uses common information and selects prescriptions for agents' private information. That is relevant prior art for a future integrated model, not a claim that the two modules below already solve it.

## 2. Module A: the smallest endogenous maintenance decision

There are finitely many periods remaining. Need \(S_t\in\{0,1\}\) follows a known symmetric Markov chain with switch probability \(0<h<1/2\). The public model, action set, and common loss criterion remain fixed. Its Bayesian prediction map is

\[
T(p)=h+(1-2h)p,
\qquad p=\Pr(S_t=1\mid\text{controller's information}).
\tag{1}
\]

Operation \(u_t\in\{0,1\}\) treats at cost \(c\), or does not treat and incurs loss \(L\) when need is present:

\[
\ell(S,u)=cu+LS(1-u),\qquad 0<c<L.
\tag{2}
\]

Treatment does not change the future hidden state. There are no informative passive observations in this benchmark. In particular, the controller cannot infer the state from an observed untreated loss or a state-dependent cash balance. If such feedback exists, it must be included as another observation channel. The analyst can score realized losses without giving them to the controller; this restricted feedback is an explicit abstraction.

Capacity \(z_t\in\{0,1\}\) determines whether a diagnostic is available now. A diagnostic \(d_t=1\) costs \(k>0\) and perfectly reveals \(S_t\). This is an oracle benchmark for acquiring a known kind of information, not candidate generation, diagnosis in actual clinical practice, or open-ended discovery. Without a diagnostic, posterior \(q=p\); with one, \(q=0\) with probability \(1-p\) and \(q=1\) with probability \(p\).

After any diagnostic, the controller chooses whether to buy capacity for the next period, \(v_t\in\{0,1\}\), at cost

\[
s_zv_t,\qquad s_1=m>0,\quad s_0=K>0,\qquad z_{t+1}=v_t.
\tag{3}
\]

Thus existing capacity lapses without upkeep. Rebuilding inactive capacity has one-period lag: payment today makes it available next period, never retroactively for today's test. Assume \(m\leq K\) where comparing the value of active and inactive capacity. Longer construction lags require a countdown state.

For the smallest resource-constrained version, inquiry has a per-period procurement limit \(B\), with

\[
kd_t+s_zv_t\leq B.
\tag{4}
\]

The operating action is financed separately; its cost \(c\) still enters the objective. Unspent procurement allowance is not banked in this version. The allowance is an exogenous physical limit; expenditure on tests, upkeep, and rebuilding is chosen endogenously. This is not yet a model of how production regenerates the total resource supply.

Without budget interaction with operation, the minimum expected operational loss is

\[
g(p)=\min\{c,Lp\}.
\tag{5}
\]

Let \(V_n(p,z)\) be minimum expected discounted total loss over \(n\) periods, with \(V_0=0\) and discount factor \(0<\beta\leq1\). Write \(\nu_p^0=\delta_p\) and \(\nu_p^1=(1-p)\delta_0+p\delta_1\). The exact Bellman equation is

\[
\boxed{
V_n(p,z)=
\min_{d\in\{0,1\}:\ d\leq z,\ kd\leq B}
\left\{
kd+\mathbb E_{q\sim\nu_p^d}
\min_{v\in\{0,1\}:\ kd+s_zv\leq B}
\left[g(q)+s_zv+\beta V_{n-1}(T(q),v)\right]
\right\}.
}
\tag{6}
\]

This charges both testing and standby capacity even when no eventual benefit is realized. Capacity can be retained or rebuilt after either diagnostic result. Financing is a decision derived from anticipated losses and feasible actions, not a calendar reduction after a negative investigation.

For a single common physical budget, put operation inside the inner minimum and replace its constraint and cost by

\[
kd+cu+s_zv\leq B,
\qquad cu+Lq(1-u)+s_zv+\beta V_{n-1}(T(q),v).
\tag{7}
\]

This variant is also exact, but a diagnostic can consume resources needed for treatment. The unconstrained information-value formulas below then require a nonbinding budget. Neither formulation counts the spending limit as a cost: actual expenditure and incurred harm are the costs.

## 3. Warranted negative evidence can be economically valuable

With one action remaining and enough procurement allowance for the test, perfect information changes operational expected loss from \(g(p)\) to \(cp\). Its gross value is

\[
\boxed{
\Delta(p)=g(p)-cp
=\begin{cases}
(L-c)p,&p\leq c/L,\\
c(1-p),&p\geq c/L.
\end{cases}
}
\tag{8}
\]

Testing is strictly worthwhile for that one action exactly when \(\Delta(p)>k\). If \(p\geq c/L\), the current policy treats everyone. A positive diagnosis preserves that action; a negative diagnosis saves its entire cost. The ex ante gross benefit \(c(1-p)\) comes from warranted negative findings. Calling them failed inquiry mistakes a change from treatment to justified restraint for absence of benefit.

If \(p<c/L\), the current action is already no treatment. A negative finding has no immediate action value in this one-step problem; it can still inform later decisions. No claim that every negative result is valuable follows.

The maximum one-step value is \(c(1-c/L)\), attained at the action threshold, not generally at maximal uncertainty \(p=1/2\). When the interval is nonempty, the exact myopic testing region is

\[
\frac{k}{L-c}<p<1-\frac{k}{c}.
\tag{9}
\]

Future uses of information can change this region in (6). Maximizing information, testing rate, or the number of positive findings is not equivalent to minimizing the stated common loss.

## 4. A negative conclusion ages even when its record is perfectly preserved

Let \(\lambda=1-2h\in(0,1)\). After a perfect negative observation, with no new information for \(j\) transitions,

\[
p_j=T^j(0)=\frac{1-\lambda^j}{2}.
\tag{10}
\]

Historical evidence that \(S_0=0\) remains true; the inference that \(S_j=0\) becomes less warranted. If \(\theta=c/L<1/2\), no treatment ceases to be uniquely optimal at the first integer

\[
j_*=\left\lceil\frac{\log(1-2\theta)}{\log\lambda}\right\rceil
\quad\text{with}\quad p_{j_*}\geq\theta.
\tag{11}
\]

Equality permits either action; strictly above the threshold treatment is preferable in the absence of another test. If \(\theta\geq1/2\), this particular aged negative never crosses the treatment threshold at finite age, although it still ceases to justify certainty about the current state. For \(h=0\), there is no aging; for \(h=1/2\), one transition erases predictive content. These boundary cases require their direct formulas rather than (11).

A controller that retains an instruction “do not treat” as if the old negative were timeless incurs excess current expected loss

\[
\bigl[Lp_j-c\bigr]_+
\tag{12}
\]

relative to an aging-aware controller restricted to the same two operational actions. This is an error in interpreting retained evidence, not a defect in the truth of the original observation. Correctly used free information can be ignored; a compulsory archive fee or a compulsory stale policy is a different intervention.

## 5. Exact option value of maintaining inquiry without testing now

When resource constraints do not alter the relevant comparison, retaining capacity after posterior \(q\) compares

\[
m+\beta V_{n-1}(T(q),1)
\quad\text{with}\quad
\beta V_{n-1}(T(q),0).
\tag{13}
\]

Thus it is strictly worthwhile precisely when its cost is below the discounted future advantage of availability. The corresponding rebuilding comparison uses \(K\), subject to its lag and feasibility. Under \(m\leq K\), available capacity is weakly better than inactive capacity before upkeep costs: it permits every inactive policy at no greater cost, plus immediate diagnosis.

A two-period example gives a complete certificate. Start with \(p=0,z=1\): a warranted negative has just established that there is no current need. Take

\[
L=10,\quad c=4,\quad h=.2,\quad
k=1,\quad m=.1,\quad\beta=1,
\tag{14}
\]

and enough procurement allowance. A current test is strictly dominated: it cannot change the known state or its future predictive distribution. Next period the belief is \(.2\). No test then costs \(g(.2)=2\), whereas an available test costs \(1+4(.2)=1.8\). Therefore maintaining now without testing costs \(.1+1.8=1.9\), versus \(2\) if capacity lapses. Rebuilding next period cannot restore that period's test because it has one-period lag.

More generally, from \(p=0,z=1\) with two periods left, the exact strict condition is

\[
\boxed{m<\beta[\Delta(h)-k]_+.}
\tag{15}
\]

This assumes the relevant test and upkeep are feasible; there is no value from capacity beyond the two-period horizon. It proves that current testing value can be zero while maintaining the option to test is worthwhile. It does not prove that standby inquiry is always worth funding. High upkeep, an unchanging known state, unaffordable tests, or no remaining useful decision can remove the value. Finite-horizon terminal dismantling must not be described as a general degeneration mechanism.

## 6. Module B: a successor, a visible channel, and paid communication

Consider a separate one-succession problem. A predecessor knows a binary diagnostic state \(S\). A successor will make one operational decision after \(j\) Markov transitions. Both share the same objective, know the transition model, and know the disclosure rule.

The successor already sees a surviving channel \(C\), potentially including capacity, balances, ordinary actions, or a record-existence indicator. Conditional on \(C=x\), define

\[
q_x=\Pr(S=1\mid C=x).
\tag{16}
\]

This conditional probability must be calculated from the actual channel. It is not overwritten by the stationary prior. The sender also knows \(C\). It can send the truthful state or send nothing, at fee \(f>0\) per sent message. Delivery is reliable, silence is distinguishable from delivery failure, and the agreed mapping from private state to message is known. Those assumptions make silence interpretable; they are not free consequences of shared interests.

Write \(r_j=T^j(0)\), so \(T^j(1)=1-r_j\). Conditional on \(q=q_x\), no extra communication gives cost \(g(T^j(q))\), whereas full information about the historical state gives cost

\[
(1-q)g(r_j)+qg(1-r_j).
\]

Its gross value is consequently

\[
\boxed{
D_j(q)=g(T^j(q))-
\left[(1-q)g(r_j)+qg(1-r_j)\right]\geq0.
}
\tag{17}
\]

The inequality follows directly from concavity of \(g\) and \(T^j(q)=(1-q)r_j+q(1-r_j)\). It is a decision-specific value of historical information, not an intrinsic scalar value of the archive.

There are four deterministic disclosure rules for each visible \(x\): send neither state, only 0, only 1, or both. Either one-sided rule fully reveals \(S\), because silence identifies the unsent state. Sending both has the same informational result and a weakly higher expected cost. Therefore the exact optimal cost among deterministic rules is

\[
\boxed{
\min\left\{
g(T^j(q)),
(1-q)g(r_j)+qg(1-r_j)+f\min\{q,1-q\}
\right\}.
}
\tag{18}
\]

Send the rarer state if \(D_j(q)>f\min\{q,1-q\}\); otherwise additional disclosure is not strictly worthwhile. Average this minimum over the actual distribution of \(C\). This is exact for the declared deterministic protocol class. It is not a claim about arbitrary noisy, strategic, or uncommitted communication.

If \(C\) already reveals \(S\), then \(q\in\{0,1\}\), \(D_j(q)=0\), and another archive has no informational benefit. If \(C\) is uninformative, \(q\) equals the prior, but silence under selective disclosure can still be informative. For example, a rule that sends only negative diagnoses makes no message evidence of a positive diagnosis. Calling all missing records ignorance would reverse its meaning.

If a reliable, agreed handoff channel itself costs \(f_0\), pay that cost before private disclosure, with channel activation chosen from the common information \(C\). Its opening condition becomes

\[
D_j(q)>f_0+f\min\{q,1-q\}.
\tag{19}
\]

This fixed fee charges for the ability to interpret silence as well as for delivered messages. A rule under which private information determines whether the channel is activated would itself create another signal and needs another posterior calculation.

## 7. Exact value and expiry of a stationary-prior archive

For an uninformative visible channel and stationary prior \(q=1/2\), (17) simplifies to

\[
\boxed{
D_j(1/2)=\frac{L}{4}
\left[\lambda^j-\left|1-\frac{2c}{L}\right|\right]_+.
}
\tag{20}
\]

To check it, put \(r_j=(1-\lambda^j)/2\). If \(c/L\leq1/2\), the current prior recommends treatment; the old negative changes that action only when \(Lr_j<c\), giving \(D_j=(c-Lr_j)_+/2\). If \(c/L\geq1/2\), apply the analogous calculation to the old positive, giving \(D_j=[L(1-r_j)-c]_+/2\). Both reduce to (20).

The historical state can remain statistically correlated with current need after it has no value for this particular action: both historical diagnoses can imply the same current optimal decision. A positive communication fee makes the economic usefulness interval shorter still. Under one-sided reliable disclosure, communication is worthwhile only if

\[
D_j(1/2)>f_0+f/2.
\tag{21}
\]

With the parameters \(L=10,c=4,h=.2\), gross archive values at ages \(j=1,2,3,4\) are respectively \(1,.4,.04,0\). The perfectly preserved old diagnosis remains a truthful historical record throughout. A new diagnostic can still have substantial current value even after this old record loses its decision value.

## 8. What is established, and what remains open

The exact results here are conditional: negative findings can justify valuable restraint; an old conclusion must be propagated through a change model; keeping inquiry available can have option value despite zero current testing value; and paid inheritance must be evaluated relative to all surviving information, including informative silence. These results follow from the specified Markov process, loss, and information interfaces. No claim about the moral adequacy of that loss follows.

Module A gives endogenous procurement within an exogenous resource allowance and free belief memory. Module B gives one paid communication decision with specified side information, reliable delivery, and a shared protocol. Combining them requires tracking the joint distribution of hidden state, private knowledge, and publicly visible resources under previous policies. Merely adding an archive bit and resetting all other beliefs to one half is not that model.

The known latent state, known switch rate, fixed treatment, common objective, perfect diagnostic, and stipulated information channels are strong restrictions. Unknown change rates, misleading tests, productive but informative actions, endogenous resource production, strategic concealment, and changing purposes remain separate extensions. In particular this cycle returns to information within a supplied representation to isolate renewal and succession; it does not explain the generation of a new representation. A future finite experiment should test the derived value and timing comparisons before making broader claims about institutions or alignment.

## 9. Audit of the implemented extensions

Implementation audit, 5 October 2026, of `experiments/recurrent-inquiry/model.py`, `test_model.py`, `PROTOCOL.md`, and saved `results/analysis.json`. The implementation preserves the two-module boundary and uses undiscounted finite-horizon costs. Its main eight-period examples extend the diagnostic to succeed with probability \(s=.8\); the two-period certificate retains \(s=1\).

**A failed diagnostic is not a negative diagnosis.** Conditional on testing, the implemented posterior law is

\[
\nu_p^1=s(1-p)\delta_0+sp\delta_1+(1-s)\delta_p.
\tag{22}
\]

Success is independent of need. An explicit failure therefore preserves the previous posterior; a successful negative sets the current need probability to zero. The code then applies one Markov transition to every branch. Diagnostic cost is paid regardless of its outcome, and diagnostic plus upkeep/rebuilding fees satisfy the cap in each realized branch. Upkeep follows the observed result and buys next-period capacity. These timings agree with (6), with (22) replacing its perfect-test observation law.

For a single remaining action, gross testing value becomes \(s\Delta(p)\), and the exact maintenance certificate (15) becomes \(m<[s\Delta(h)-k]_+\) when \(\beta=1\) and the required expenditures are feasible. This extension does not permit false positive or false negative reports: success is truthful, while failure is explicitly uninformative. A state-dependent failure rate would require a different posterior update.

**The fixed-calendar comparison is a constrained policy comparison.** Each calendar fixes the next-capacity choices before outcomes, while permitting tests and operation to depend on the current belief. The occupancy linear program has a source weight for every calendar, flow conservation for every reachable time/belief pair, and one aggregate expected inquiry-cost constraint. It consequently permits an ex ante lottery over calendars and adaptive randomized tests within each selected calendar. A pathwise cumulative-spending constraint is not implemented; the realized per-period procurement cap remains enforced for every permitted action.

The adaptive Bellman policy minimizes operational loss plus actual inquiry expenditure. If another policy had weakly lower expected inquiry expenditure and strictly lower operational loss, it would have strictly lower total loss, contradicting this optimum. Thus comparison at the adaptive optimum's own expected expenditure is mathematically justified. In the saved eight examples the calendar program uses that entire bound to numerical precision, so the comparison actually matches expected expenditure, not only its upper allowance. The recorded operating-loss gaps are approximately .007655 to .083365, with flow residuals below \(1.12\times10^{-16}\). These are exact-model optimization comparisons up to numerical tolerance, not sampled effect estimates.

The stationary-state control \(h=0\) still has a positive adaptive advantage: failed diagnostics can require another period of capacity, while successful learning removes that need. The advantage therefore does not isolate environmental change alone. The \(h=1/2\), zero-success, and prohibitive-upkeep controls have no adaptive advantage within numerical tolerance. The saved stale-model comparison explicitly substitutes assumed \(h=0\) for true \(h=.1\); it tests model misspecification, not learning an unknown change rate from experience.

**Delivery erasure changes what silence means.** For a fixed visible cue, let \(q\) be its posterior about the historical state, \(\delta\) the state-independent probability that an attempted message is delivered, and \(e_0,e_1\in[0,1]\) the sender's conditional probabilities of attempting a truthful message. Intentional silence and failed delivery produce the same received symbol. Their unnormalized state probabilities are

\[
w_0=(1-q)(1-\delta e_0),\qquad
w_1=q(1-\delta e_1).
\tag{23}
\]

Whenever \(w_0+w_1>0\), the correct historical-state posterior after silence is \(w_1/(w_0+w_1)\). The code constructs exactly these joint probabilities and then ages the posterior. A delivered truthful message reveals the historical state. Setup cost is charged whenever the opportunity is established, including branches with no attempted or delivered message; the message fee is paid per attempt, including failed deliveries. The public cue determines whether to establish the opportunity before private-state-dependent disclosure. The successor does not see a private attempt invoice, state-dependent debit, or delivery acknowledgement; any such observable would be another channel and would change (23).

**Four deterministic rules also suffice against hidden private randomization.** The protocol's observation that publicly randomizing among agreed rules cannot improve their minimum expected cost is correct, but by itself does not cover an unobserved state-dependent coin toss by the sender. The stronger statement holds here as well.

Let \(a=T^j(0)\). After opening the channel, optimized expected cost conditional on the cue is

\[
\begin{aligned}
F(e_0,e_1)
={}&\delta(1-q)e_0g(a)+\delta q e_1g(1-a)\\
&+\min\{c(w_0+w_1),\ L[a w_0+(1-a)w_1]\}\\
&+f_0+f[(1-q)e_0+q e_1].
\end{aligned}
\tag{24}
\]

The delivered-message and fee terms are affine in \((e_0,e_1)\). The silent-message term is the minimum of two affine functions, hence concave. Therefore \(F\) is concave on the unit square. Every point is a convex combination of its four vertices, so

\[
F(e_0,e_1)\ \geq\ \min_{(b_0,b_1)\in\{0,1\}^2}F(b_0,b_1).
\tag{25}
\]

This proves that hidden sender randomization cannot improve on the four enumerated deterministic rules. Randomized receiver actions also cannot improve a linear expected loss; the receiver already takes the minimum of its two actions. Finally compare the best open-channel value with the closed-channel value. These conclusions rely on this one-step common-objective problem, unrestricted choice among its declared actions, and expected additive costs. Extra communication quotas, strategic objectives, unknown delivery, or a different information structure require a fresh argument.

An independent evaluation of (24) matched every recorded deterministic alternative in all 117 saved handoff cases. A finite check of 8,424 private-randomization points was also consistent with (25); the concavity proof, not that grid check, establishes the optimization result.

All five implementation tests were independently rerun successfully with the experiment's Python runtime. They check the two-period certificate, failed versus negative diagnoses, filtering, forward cost accounting and branch feasibility, the calendar program against exhaustive Bellman calculations, and communication posteriors and aging. This audit does not treat those checks as evidence beyond the specified finite models.

**Keep economic expiry distinct from loss of all decision value.** For the implemented communication parameters \(h=.1,L=1,c=.4,f_0=.02,f=.1\), fresh evidence with an uninformative cue and reliable delivery has optimal total loss \(.27\): operating loss \(.2\), setup \(.02\), and expected message fee \(.05\). At delivery probability \(.8\), sending only a negative diagnosis gives total loss \(.31\). Silence then has posterior \(5/6\), rather than certainty, and the receiver treats.

At record age four, gross full-information value is still \(.25(.8^4-.2)=.0524\), but reliable selective disclosure costs \(.07\), so the optimal channel closes. Gross decision value reaches zero only at age eight. This differs from the earlier illustration with \(h=.2,L=10,c=4\), whose gross value reaches zero at age four. Neither cutoff says that the historical diagnosis was false, or that new inquiry has ceased to be useful.
