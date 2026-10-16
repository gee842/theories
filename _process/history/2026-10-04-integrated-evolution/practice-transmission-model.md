# How renewal practices are transmitted

Working mathematical memo, 5 October 2026. AI-generated derivation in Ren's research program. The root agent constructed this extension; the mathematical research agent separately checked its aggregation and extinction proof. This is a conditional model result with no originality or empirical-validation claim.

## The mechanism being added

The [paid-renewal model](endogenous-renewal-math.md) makes support and corrective capacity maintain one another but fixes renewal effort. This extension makes the prevalence of two renewal practices endogenous. It distinguishes two routes of transmission: creation of new functioning capacity inherits a practice, while existing capacity can copy another practice in response to an observed current cost.

Let \(C_H,C_L\ge0\) be amounts of functional capacity carrying practices \(u_H>u_L>0\), and \(C=C_H+C_L>0\). Effort of type \(i\) consumes support at rate \(u_iEC_i\), creating same-practice capacity at gross rate \(\eta u_iEC_i\). All capacity decays at rate \(\mu\). This inheritance assumption must be tested in any application.

At encounters between unlike types, an \(H\) carrier switches to \(L\) at a rate proportional to the immediate per-unit expenditure saving \(E(u_H-u_L)\). Aggregate switching is

\[
J=\kappa E(u_H-u_L)\frac{C_HC_L}{C},\qquad \kappa\ge0.
\tag{1}
\]

This is a specified observation and uptake mechanism, not a deduction that rational agents necessarily copy cheap practices. It assumes copying responds to current expenditure without crediting its concurrent production of replacement capacity. If observers measure that production, value later effects, or have different information, a different switching law may result. The parameter \(\kappa\) measures this particular uptake response.

Together,

\[
\boxed{
\begin{aligned}
\dot E&=P(C)-\delta E-E(u_HC_H+u_LC_L),\\
\dot C_H&=(\eta u_HE-\mu)C_H-J,\\
\dot C_L&=(\eta u_LE-\mu)C_L+J,\\
P(C)&=\frac{aC}{1+C/K}.
\end{aligned}}
\tag{2}
\]

The common replenishment process has the same declared external feedstock boundary as before. Switching conserves total capacity and itself has no additional modeled physical cost. The adoption rule and its cost are remaining assumptions. \(C\) can represent standardized units of a function, not necessarily a count of persons or organizations. A social or AI application requires a justified carrier and unit.

## Exact aggregation

Put \(x=C_H/C\), \(\Delta u=u_H-u_L\), and \(\bar u=u_L+\Delta u x\). Summing and differentiating yields

\[
\boxed{
\begin{aligned}
\dot E&=P(C)-\delta E-\bar u EC,\\
\dot C&=(\eta\bar u E-\mu)C,\\
\dot x&=(\eta-\kappa)E\Delta u\,x(1-x).
\end{aligned}}
\tag{3}
\]

The first transmission route favors \(H\) at rate \(\eta E\Delta u\); the specified cost-based copying favors \(L\) at rate \(\kappa E\Delta u\). These terms have the same units. Their difference is derived from (2), rather than assigned as the fitness of a desirable practice.

For \(0<x_0<1\),

\[
\log\frac{x(t)}{1-x(t)}
=\log\frac{x_0}{1-x_0}
+(\eta-\kappa)\Delta u\int_0^t E(s)\,ds.
\tag{4}
\]

This gives an empirical separation: changing copying speed changes the selection direction without directly changing production efficiency \(\eta\) or the two maintenance intensities. Conversely, improving conversion efficiency affects actual renewal as well as the differential production term.

As before, \(V=E+C/\eta\) satisfies

\[
\dot V=P(C)-\delta E-\mu C/\eta
\le aK-\min(\delta,\mu)V.
\tag{5}
\]

The nonnegative state is invariant, all stocks are bounded, and \(C(t)>0\) at finite times if \(C_0>0\).

## A functioning renewal regime can be destabilized by copying

Let \(m=\mu/\eta\), \(A=a/m>1\), and

\[
u_{\mathrm{crit}}=\frac{\delta}{K(\sqrt A-1)^2}.
\]

Suppose \(u_H>u_{\mathrm{crit}}\). On \(x=1\), the upper positive equilibrium from the paid-renewal model has

\[
E_H^*=\frac{m}{u_H}.
\]

The two ecological eigenvalues are stable there. The additional share eigenvalue is

\[
\boxed{\lambda_{\mathrm{practice}}
=-(\eta-\kappa)E_H^*\Delta u.}
\tag{6}
\]

Therefore:

- If \(\kappa<\eta\), that positive equilibrium is locally asymptotically stable against the specified low-effort alternative.
- If \(\kappa>\eta\), the low-effort alternative invades it and the equilibrium is unstable in the practice direction.
- If \(\kappa=\eta\), the composition is constant. The zero share eigenvalue does not establish asymptotic attraction of one practice.

This is resistance to a specified alternative under the stated transmission law. It is not a proof of stability against every mutation or an unlimited class of strategic changes. The invasion eigenvalue concerns growth of a rare deviation around a nonzero equilibrium, where share and absolute rare-type growth have the corresponding local interpretation.

## Global collapse under a selected subcritical practice

**Proposition.** Assume \(A>1\), \(u_L<u_{\mathrm{crit}}<u_H\), \(\kappa>\eta\), \(C_0>0\), \(E_0\ge0\), and \(0<x_0<1\). Then \(E(t)\to0\) and \(C(t)\to0\).

The proof must permit the effort \(\bar u(t)\) to change. Applying a fixed-policy extinction theorem without this step would be insufficient.

**Case 1: finite total support exposure.** If \(\int_0^\infty E(s)\,ds<\infty\), then

\[
C(t)=C_0\exp\left[\eta\int_0^t\bar u(s)E(s)\,ds-\mu t\right]
\le C_0\exp\left[\eta u_H\int_0^\infty E(s)\,ds-\mu t\right].
\]

Thus \(C\) declines exponentially. Since \(\dot E\le aC-\delta E\), support also vanishes.

**Case 2: infinite total support exposure.** Equation (4) implies \(x\to0\), so \(\bar u\to u_L\). Choose a constant \(\widehat u\) with \(u_L<\widehat u<u_{\mathrm{crit}}\); eventually \(\bar u\le\widehat u\).

Define

\[
W=E+\frac C\eta+\frac{\delta}{\eta\widehat u}\log(C/K).
\]

For sufficiently late times,

\[
\begin{aligned}
\dot W
&=P(C)-mC-\frac{\delta m}{\widehat u}
+\delta\left(\frac{\bar u}{\widehat u}-1\right)E\\
&\le P(C)-mC-\frac{\delta m}{\widehat u}\\
&\le K(\sqrt a-\sqrt m)^2-\frac{\delta m}{\widehat u}<0.
\end{aligned}
\tag{7}
\]

The last inequality is strict by the choice of \(\widehat u\). Since \(E+C/\eta\ge0\), a uniform negative bound on \(\dot W\) forces \(C\to0\) exponentially; the same comparison gives \(E\to0\). This completes the dichotomy. In fact exponential decay in the second case contradicts its infinite-exposure assumption; the proof still establishes that no persistent trajectory can satisfy it.

**A stronger consequence.** Case 2 is inconsistent, so every trajectory in the proposition has finite total support exposure. Equation (4) then gives \(0<x_\infty<x_0\). Thus \(L\) does not even reach asymptotic fixation along these mixed collapsing trajectories. As support disappears, differential production and copying slow down. This limiting fraction describes vanishing total capacity, not a surviving population.

The all-\(H\) boundary has no invader in this model and is an exception to the global-collapse statement. Continued introduction of variants would require mutation, entry, or explicit switching independent of encounters.

## Selection compatibility still does not guarantee recovery

If \(\kappa<\eta\), an established upper \(H\) equilibrium is locally stable in the full model. This gives a nonempty set of nearby functioning initial conditions. If that equilibrium is strictly above a specified support floor, sufficiently small perturbations remain above that floor by local stability.

Depleted initial conditions can still collapse for every \(\kappa\). For the illustrative parameters \(a=9\), \(\delta=\eta=\mu=K=1\), \(u_H=.5\), \(u_L=.1\), the box

\[
0\le E\le .1,\qquad 0<C\le .001,\qquad 0\le x\le1
\]

is forward invariant. At \(E=.1\), \(\dot E\le9(.001)-.1=-.091\); throughout the box,

\[
\dot C/C\le u_H(.1)-1=-.95.
\]

Hence \(C\to0\) exponentially and then \(E\to0\). This statement does not require a specific copying direction.

At \(\kappa=\eta\), the mean effort is fixed by the initial composition. For these parameters, a pair of positive equilibria requires \(x>(.25-.1)/(.5-.1)=.375\), with the same basin and protected-floor qualifications as before.

## Interpretation and what remains external

The model identifies two measurable transmission channels whose effects oppose one another. A practice can generate replacement capacity more effectively while being copied less, because the criterion driving adoption counts a different outcome. Whether either channel dominates is a question about production, observations, and uptake—not a universal property of competition or human motivation.

The resulting research hypothesis is that adoption measures can predict practice prevalence while missing the stock consequences of the underlying production mechanism. To test it, vary exposure to immediate-cost comparisons while holding actual renewal technology and cost constant; separately alter what those comparisons reveal about capacity produced. Compare changes in adoption, gross replacement, and support over time.

The model endogenizes practice frequencies. It does not yet explain selection over \(\kappa\), control of the observation process, the public production technology, or the external feedstock. Those are explicit remaining questions. Altering \(\kappa\) can represent an intervention only after specifying its causal implementation and cost. The term “corrective capacity” does not establish that its actions are legitimate or ethically desirable.

## Reproducible illustration

The [verification script](verify_selection_and_replacement.py) and [recorded results](selection-and-replacement-checks.json) compare matched initial states \(E_0=2,C_0=3+\sqrt7,x_0=.99\) with copying response \(\kappa=.5\) or \(1.5\). The first approaches the stable high-effort regime; the second collapses under the proved conditions. Maximum state discrepancies under tighter integration tolerances are below 1.4e-10 for the recorded cases.

In the collapsing illustration, support initially increases from 2 to approximately 4.633 while the capacity that replenishes it declines. This is an actual stock increase inside the model, not a falsified measurement. It does not certify maintenance of the renewal process. At late times the share tends toward approximately .00147 while both absolute stocks vanish.

The [figure](practice-transmission.png) displays these trajectories. Independent proof review confirmed the aggregation, invasion eigenvalue, and extinction proof, and identified the strengthened interior-share consequence above.
