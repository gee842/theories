# Selection and the continuity of renewal

Research continuation, 5 October 2026. Ren asked to continue toward universal constraints on continued becoming while retaining findings, insights, and decisions. This cycle studies how renewal practices spread and how successors become functional. The conceptual direction is Ren's; the mathematical synthesis and working models are AI-generated. Three research agents and the coordinating agent developed and reviewed the work. No empirical experiment or AI deployment benchmark was run.

The main advance is a distinction among transmission, operating viability, and successful replacement. A practice can produce more future capacity while losing through another transmission channel. Paying contributors from real output can make maintenance spread while also reducing the output left for shared support. A successor that both spreads faster and performs better once mature can still break an indispensable function during its introduction.

The [research hub](../../_process/research/2026-10-04-integrated-evolution/README.md), [log](../../_process/research/2026-10-04-integrated-evolution/RESEARCH-LOG.md), and [claim register](../../_process/research/2026-10-04-integrated-evolution/CLAIMS.md) preserve the wider program. This snapshot continues [universal constraints and maintained correction](2026-10-04-universal-constraints-and-maintained-correction.md). The models below are complementary restricted mechanisms, not a single calibrated system or a completed universal theory.

## Renewal can be transmitted through competing channels

The previous paid-renewal model used support \(E\), corrective capacity \(C\), and fixed effort \(u\):

\[
\dot E=P(C)-\delta E-uEC,\qquad
\dot C=\eta uEC-\mu C,\qquad
P(C)=\frac{aC}{1+C/K}.
\]

The new extension lets capacity carry either a high-effort practice \(u_H\) or a lower-effort practice \(u_L\), with \(u_H>u_L>0\). Let \(C_H,C_L\) denote their absolute amounts. Each creates same-practice replacement capacity at gross rate \(\eta u_iEC_i\).

A second route changes practices within existing capacity. At encounters between unlike practices, high-effort carriers copy low effort at a rate proportional to the immediate expenditure saving. The resulting transfer is

\[
J=\kappa E(u_H-u_L)\frac{C_HC_L}{C_H+C_L}.
\tag{1}
\]

This specifies an observation and uptake mechanism. It assumes adoption responds to current expenditure without crediting the replacement capacity that expenditure produces. It is not asserted to be universally rational behavior. A different observation or reward process can change the copying law.

Put \(x=C_H/(C_H+C_L)\), \(C=C_H+C_L\), and \(\bar u=u_L+(u_H-u_L)x\). Production, loss, and copying then give the exact aggregate dynamics

\[
\boxed{
\begin{aligned}
\dot E&=P(C)-\delta E-\bar u EC,\\
\dot C&=(\eta\bar u E-\mu)C,\\
\dot x&=(\eta-\kappa)E(u_H-u_L)x(1-x).
\end{aligned}}
\tag{2}
\]

The two transmission effects are visible separately: inherited production favors high effort at rate \(\eta E(u_H-u_L)\); current-cost copying favors low effort at rate \(\kappa E(u_H-u_L)\). The selection difference is derived from specified events. Labels such as “good” or “aligned” play no role in the event rates.

The support-plus-converted-capacity balance still cancels internal transfers:

\[
\frac{d}{dt}\left(E+\frac C\eta\right)
=P(C)-\delta E-\frac{\mu}{\eta}C.
\tag{3}
\]

Switching does not produce new capacity merely by changing a practice's label.

## A global loss result and a viable alternative

For \(A=a\eta/\mu>1\), the earlier model's critical effort is

\[
u_{\mathrm{crit}}=
\frac{\delta}{K(\sqrt A-1)^2}.
\]

Suppose \(u_L<u_{\mathrm{crit}}<u_H\). A functioning all-high-effort state can exist. Its upper positive equilibrium is stable against the specified low-effort alternative when \(\kappa<\eta\), and unstable to it when \(\kappa>\eta\). The additional invasion-direction eigenvalue is

\[
-(\eta-\kappa)E_H^*(u_H-u_L).
\tag{4}
\]

**Conditional global result.** If \(\kappa>\eta\), \(C_0>0\), and both practices are initially present, then \(C\to0\) and \(E\to0\).

The proof accommodates changing mean effort. If total support exposure \(\int_0^\infty E\,dt\) is finite, capacity's per-capita renewal has a finite cumulative contribution while depreciation continues; capacity therefore declines exponentially. If exposure were infinite, the exact share equation would imply \(x\to0\), eventually placing mean effort below a fixed \(\widehat u<u_{\mathrm{crit}}\). The logarithmic extinction certificate from the previous cycle remains valid with this upper bound on effort. It forces exponential depletion, contradicting infinite exposure. Thus no persistent trajectory satisfies either case.

The [full proof](../../_process/research/2026-10-04-integrated-evolution/practice-transmission-model.md) also establishes a sharper consequence: every mixed collapsing trajectory retains a strictly positive limiting high-effort share. Low effort need not reach fixation for the system to lose functioning capacity. Fractions at extinction describe vanishing stocks, not surviving populations.

For \(\kappa<\eta\), the upper high-effort equilibrium is locally stable in the full system. That supplies a genuine alternative regime, although sufficiently depleted starts can still collapse. Thus favorable transmission and recoverability remain distinct.

![Inherited production and current-cost copying produce different stock trajectories](/Users/ren/theories/_process/research/2026-10-04-integrated-evolution/practice-transmission.png)

The illustration uses \(a=9\), \(\delta=\eta=\mu=K=1\), \(u_H=.5\), \(u_L=.1\), and matched initial stocks near the high-effort equilibrium. Changing only \(\kappa\) from .5 to 1.5 changes persistence to collapse. In the collapsing case, support first increases from 2 to about 4.633 while the capacity replenishing it deteriorates. This stock increase is real within the model. It conceals neither a measurement error nor fictitious reserves; it simply does not establish renewal of those reserves.

The remaining assumptions include inherited production, the observation used for copying, fixed response coefficient \(\kappa\), no added cost for switching, and the external feedstock supporting \(P(C)\). The model endogenizes practice prevalence, not every condition governing its evolution.

## Rewarding maintenance has a resource allocation consequence

A second model derives an adoption advantage from a paid share of actual output. It is useful because a reward cannot then be increased without changing shared renewal.

At fixed operating scale, let \(x\) be the contributor share and \(P(x)=Bx/(h+x)\) the gross production flow per active time. A fraction \(\phi\) is retained by contributors; the remaining \(1-\phi\) replenishes shared support. Contributors pay effort cost \(c\) and a claim or enforcement charge \(k\phi\). Their current-return advantage is

\[
s(x;\phi)=\frac{\phi B}{h+x}-c-k\phi.
\tag{5}
\]

With activity \(g(E)=E/(L_0+E)\) and pairwise copying proportional to positive current-return differences,

\[
\boxed{
\begin{aligned}
\dot x&=\nu g(E)x(1-x)s(x;\phi),\\
\dot E&=g(E)(1-\phi)\frac{Bx}{h+x}-\delta E.
\end{aligned}}
\tag{6}
\]

Retained and shared production sum to the actual flow; the reward is not an external bonus. Private operating budgets and the institution enforcing claims are nevertheless incomplete parts of this model. Charging a fee does not establish that enforcement functions or persists. Divisible output is assumed; the same subtraction should not automatically be applied to nonrival knowledge.

When the stable active-time composition is interior,

\[
x_*=\frac{\phi B}{c+k\phi}-h,\qquad
E_*=\frac{(1-\phi)[B-hk-hc/\phi]}{\delta}-L_0.
\tag{7}
\]

The expression applies only for \(0<x_*<1\) and \(E_*>0\). At complete contribution, the appropriate support equilibrium is instead \(E_R=(1-\phi)B/[\delta(h+1)]-L_0\).

The mechanism has two constraints. Too little retained return can make maintenance invasible even when an all-maintainer system would be viable. Too much retention can sustain contribution while leaving shared support below a protected floor.

For \(B=4,h=c=\delta=1,k=.2,L_0=.1\), and protected floor \(E_{\min}=.7\):

| Retained fraction | Practice and support outcome at the relevant equilibrium |
|---|---|
| .1 | All-maintainer support would be 1.7, but a noncontributing practice invades. |
| .3 | Stable contributor share is about .132; support is about .227, below the floor. |
| .5 | Stable contributor share is about .818; support is .8, above the floor. |
| .8 | Complete contribution is stable; support is .3, below the floor. |

These are selected-equilibrium results, not guaranteed transitions from every initial state. At complete support depletion, activity and copying stop. The [working memo](../../_process/research/2026-10-04-integrated-evolution/selection-of-renewal.md) derives the branch-specific feasible retention interval and its restrictions.

This module gives no universal recommendation to privatize, centralize, or maximize retention. It identifies a balance that depends on the actual production and allocation mechanism. Partially retained benefits have substantial prior art, including [Lerch and colleagues' resource-explicit analysis](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1010666).

## A successor can win before it can perform the required function

A third model grants a new practice both a positive adoption advantage and better mature performance. It still permits transition failure.

Let adoption follow \(\dot x=sx(1-x)\), \(s>0\), from a mature seed \(\varepsilon\). Later adopters require duration \(L\) to become functional. The mature fraction is

\[
m(t)=
\begin{cases}
\varepsilon,&t<L,\\
x(t-L),&t\ge L.
\end{cases}
\tag{8}
\]

A full predecessor population supplies one unit of required service; mature successors supply \(b>1\) units. Immediate retirement at adoption leaves predecessor service \(1-x\), so the support balance is

\[
\dot E=\gamma[(1-x)+bm-1]
=\gamma(bm-x),\qquad \gamma>0.
\tag{9}
\]

The adoption advantage \(s\) is assumed independently of productivity \(b\). This deliberately distinguishes what spreads from what performs. The equations apply until crossing a declared support floor invalidates the transition.

For \(b\varepsilon<1\), a declining-support interval occurs exactly when

\[
\boxed{e^{sL}>
\frac{b(1-\varepsilon)}{1-b\varepsilon}.}
\tag{10}
\]

For rare seeds this approaches \(sL>\log b\). It compares replacement speed with maturation delay and mature productivity. It is not a universal speed limit on innovation.

The support trajectory integrates explicitly, yielding an exact maximum draw on the initial reserve. With \(\varepsilon=.01,b=2,L=2,s=1,\gamma=1\), the required reserve is approximately .729169. A reserve of .5 reaches its floor at time 4.937242, when adoption is already about 58.47%. The successor has become the majority and would eventually deliver twice the service, but its mature capacity has not yet established the indispensable function.

![A successor can spread before functional capacity has matured](/Users/ren/theories/_process/research/2026-10-04-integrated-evolution/replacement-gap.png)

The plotted continuation beyond a reserve breach describes the unconstrained equations for calculating required support. It does not establish recovery after the assumed irreversible failure. The [replacement memo](../../_process/research/2026-10-04-integrated-evolution/replacement-and-establishment.md) gives exact formulas, timing conventions, and separate definitions of selective invasion, stochastic demographic establishment, and functional establishment.

## An invariant of maturation work

One constructive policy retains predecessor service until each successor becomes functional. It requires extra concurrent capacity

\[
I(t)=x(t)-m(t).
\]

Predecessor service is then \(1-m\), and \(\dot E=\gamma(b-1)m\ge0\). The specified support stock does not decline. The old form can disappear as successor maturation completes.

For any monotone adoption schedule completing the same replacement, let \(a(u)\ge0\) be its adoption flow. Every cohort spends \(L\) units of time pending, so

\[
\boxed{
\int_0^\infty I(t)\,dt
=\int_0^\infty a(u)\int_u^{u+L}dt\,du
=L(1-\varepsilon).
}
\tag{11}
\]

This is an exact schedule-independent quantity: total pending-capacity time. Under the specified full predecessor-retention policy it is also total duplicate-service time. Faster rollout changes peak concurrent demand, while the total in (11) stays fixed.

This is established occupancy-time accounting, related to the accounting behind [Little's law](https://pubsonline.informs.org/doi/abs/10.1287/opre.9.3.383); the finite-rollout proof requires no stationary queue. For heterogeneous durations \(\ell(u)\), the identity becomes \(\int I\,dt=\int\ell(u)\,dA(u)\), with adoption measure \(dA\). A common conditional mean duration gives the corresponding expectation. Congestion, abandonment, and changing training technology require their actual durations and completion process.

Keeping predecessors is not free. If an independently funded overlap budget pays \(c_o\) per capacity-time unit, this protocol needs at least \(c_oL(1-\varepsilon)\), adequate peak capacity, and authority to implement the handoff. Expenditure must not secretly breach another protected stock. In the example, total overlap is 1.98 capacity-time units and peak extra capacity is approximately .4621.

Full retention is sufficient, not a universal minimum. Surplus mature productivity can permit earlier retirement; the pointwise minimum extra predecessor amount needed to prevent negative support flow is \([x-bm]_+\). A stock reserve can fund temporary deficits too. The invariant constrains the stated maturation process; it does not prohibit better technology or another handoff policy.

## What the three mechanisms imply together

The proposed general framing becomes more discriminating:

- **Transmission compatibility:** the processes increasing a practice's prevalence need not reward the functioning capacity it creates.
- **Allocation feasibility:** financing individual participation can change the support available to the surrounding system.
- **Transition continuity:** successful spread and superior mature function do not establish that the change can be completed without losing an indispensable function.

These are mechanism classes to investigate, not a claim that all biological, social, and AI cases share the same coefficients. Together they explain why operating viability, resistance to a particular invader, and feasible replacement deserve separate tests.

For AI development, a possible application is to distinguish adoption of a model, workflow, or evaluation rule from the maturity of expertise and correction capacity replacing its predecessor. For institutions, a possible application is to identify who funds the overlap and how they capture enough of its benefit to continue doing so. These are hypotheses requiring independently defined functions, measurements, and legitimate intervention authority.

The existing literature already studies selection over payoff-changing traits, institutions, and social structure. [Akçay's evolving-network model](https://www.nature.com/articles/s41467-018-05130-7) is a direct precedent for a successful cooperative regime changing the structure that sustains it. The [prior-art audit](../../_process/research/2026-10-04-integrated-evolution/selection-prior-art-audit.md) locates these contributions and preserves the earlier failed pilot prediction.

## Verification and the next question

The [reproducible calculation](../../_process/research/2026-10-04-integrated-evolution/verify_selection_and_replacement.py) and [saved results](../../_process/research/2026-10-04-integrated-evolution/selection-and-replacement-checks.json) check the transmission model at four conditions, compare tighter integration tolerances, evaluate appropriation equilibria, verify the replacement integral against independent quadrature, and check the overlap identity at four rollout speeds. Both figures were inspected visually. The transmission theorem received separate proof review.

The checks concern the equations, not their empirical adequacy or originality. The strongest unresolved issue is selection over the rules themselves: why are the observation, allocation, and handoff practices that preserve functioning conditions chosen, funded, enforced, and revised? The next model should make that choice a consequence of observable returns and political or organizational uptake, while charging its implementation costs. It should also permit legitimate replacement and explain when a better rule cannot invade or cannot complete the transition.

This cycle contributes restrictions and constructive examples toward the north star. It does not assume that a universal trajectory, a unique ethical gradient, or an inevitable movement toward regeneration has been found.
