# Endogenous renewal with a paid, self-maintaining corrector

Mathematical working memo, 4 October 2026. AI-generated derivation for Ren's foundational research program. This file develops one deliberately restricted model; it does not assert originality, empirical validation, a universal social law, or a solution to AI alignment. The root research agent is separately checking the derivation and numerical illustrations.

## Purpose and relationship to the earlier work

The [integrated dynamics memo](integrated-dynamics.md) models a maintenance practice whose relative return is changed by a fixed compensation parameter. The [earlier authority extension](../../../sources/15-codex-theory-conversations/2026-10-04-alignment-coordination-contribution-space.md) makes authority erodible but gives its rebuilding an externally fixed rate.

This model replaces permanently supplied correction capacity with a stock that must participate in financing and rebuilding itself. Its strongest result is an explicit condition for a stable positive support–correction system, together with a resource-floor constraint that places an upper bound on maintenance intensity. A positive equilibrium can coexist with an attracting depleted state.

The allocation rule remains fixed. This is one step toward endogenous institutions, not a model of selection over the rule itself.

## 1. Mechanism, units, and boundary

Let \(E\geq0\) be a spendable support stock, and \(C\geq0\) a stock of functional corrective capacity. Both stocks deteriorate. An operating corrector helps replenish support from a declared external feedstock or environmental opportunity, and expends support to replace, train, or repair corrective capacity.

Take

\[
\boxed{
\begin{aligned}
\dot E&=\frac{aC}{1+C/K}-\delta E-uEC,\\
\dot C&=\eta uEC-\mu C.
\end{aligned}}
\tag{1}
\]

Parameters \(a,K,\delta,\eta,\mu\) are strictly positive. The policy parameter \(u>0\) is constant within a run and may be bounded by \(u_{\max}\). Interpret

\[
v=uEC
\]

as the paid operating and replacement effort, measured in support units per time. Spending \(v\) consumes \(E\); the same activity renews \(C\) at conversion rate \(\eta v\). The loss rates are \(\delta E\) and \(\mu C\). The gross support input

\[
P(C)=\frac{aC}{1+C/K}
\]

is enabled by corrective capacity and bounded above by \(aK\).

The units are compatible: \(a\) has units \(E/(C\,\mathrm{time})\), \(K\) has units \(C\), \(u\) has units \(1/(C\,\mathrm{time})\), and \(\eta\) has units \(C/E\).

This is an open system. The term \(P(C)\) is an input or functional restoration process, not energy created by the corrector. Its external source, conversion technology, and opportunity set are assumed available over the horizon. They would require additional state variables if their depletion matters. There is no external injection of \(C\): when \(C=0\), it cannot reappear within this model. That assumption captures reliance on inherited organizational capacity, but excludes spontaneous invention, immigration, or outside institution building.

The positive feedback is functional rather than uniformly positive in every marginal derivative. \(C\) enables gross support renewal, but more \(C\) also increases spending. At high \(C\), its net marginal effect on \(E\) can be negative. This is precisely why explicit costs matter.

## 2. Positivity, accounting, and boundedness

At \(E=0\), \(\dot E=P(C)\geq0\). At \(C=0\), \(\dot C=0\). Thus the nonnegative quadrant is invariant. Positive \(C\) remains positive at every finite time, since

\[
C(t)=C(0)\exp\left(\int_0^t[\eta uE(s)-\mu]\,ds\right).
\]

Define an accounting quantity

\[
V=E+\frac{C}{\eta}.
\]

The paid conversion cancels exactly:

\[
\boxed{\dot V=P(C)-\delta E-\frac{\mu}{\eta}C.}
\tag{2}
\]

Consequently, with \(\lambda=\min(\delta,\mu)>0\),

\[
\dot V\leq aK-\lambda V,
\qquad
V(t)\leq V(0)e^{-\lambda t}+\frac{aK}{\lambda}(1-e^{-\lambda t}).
\tag{3}
\]

All trajectories are bounded and exist for all future time. \(V\) is a converted accounting stock, not a claim that institutional capacity obeys a universal conservation law. Equation (2) is exact because model (1) explicitly charges the same transfer to its source that it credits, after conversion, to its destination.

## 3. Exact positive-equilibrium threshold

Put

\[
m=\frac{\mu}{\eta},
\qquad
A=\frac{a}{m}=\frac{a\eta}{\mu},
\qquad
d=\frac{\delta}{uK}.
\tag{4}
\]

At any positive equilibrium, the correction equation requires

\[
\boxed{E^*=\frac{m}{u}.}
\tag{5}
\]

This fixes the support concentration at which paid renewal just replaces corrective depreciation. The remaining equilibrium equation is

\[
h(C):=\frac{aC}{1+C/K}-mC=\frac{\delta m}{u}.
\tag{6}
\]

The left side is support production net of the support needed to replace corrective decay. The right side is the remaining loss of support itself.

Writing \(c=C/K\), equation (6) becomes

\[
c^2-(A-1-d)c+d=0.
\tag{7}
\]

There are two distinct positive solutions exactly when

\[
\boxed{A>(1+\sqrt d)^2.}
\tag{8}
\]

To see why this is the relevant discriminant condition, positive roots require \(A-1-d>0\), and two distinct real roots require \(A-1-d>2\sqrt d\). Combining the conditions gives (8), excluding the other algebraic discriminant branch with nonpositive roots.

Equivalently, define

\[
\boxed{
u_{\mathrm{crit}}=
\frac{\delta}{K(\sqrt A-1)^2}
\quad\text{when }A>1.
}
\tag{9}
\]

A pair of positive equilibria exists exactly when \(A>1\) and \(u>u_{\mathrm{crit}}\). If \(A\leq1\), no finite positive intensity suffices. If a policy ceiling applies, positive equilibria are possible only when \(u_{\max}>u_{\mathrm{crit}}\).

The equilibria are

\[
\boxed{
E_\pm=\frac{m}{u},
\qquad
C_\pm=\frac K2\left[
A-1-d\pm\sqrt{(A-1-d)^2-4d}
\right].
}
\tag{10}
\]

At equality in (8), the roots meet at

\[
C_{\mathrm{fold}}=K(\sqrt A-1),
\qquad
E_{\mathrm{fold}}=
\frac{Km}{\delta}(\sqrt A-1)^2.
\tag{11}
\]

There is then one positive nonhyperbolic equilibrium; the strict stability claims below do not include that case.

### An equivalent net-renewal interpretation

When \(a>m\), \(h(C)\) has its unique positive maximum at \(C_{\mathrm{fold}}\), and

\[
\boxed{
\max_{C\geq0}h(C)
=K(\sqrt a-\sqrt m)^2.
}
\tag{12}
\]

Thus condition (8) is also

\[
\boxed{
K(\sqrt a-\sqrt m)^2>\frac{\delta m}{u}.
}
\tag{13}
\]

The maximal support surplus after replacing the corrector must exceed the unavoidable support loss at the renewal concentration. This is a concrete feasibility condition, rather than “repair capacity exceeds damage” with repair supplied free of charge.

## 4. Stability, recovery, and depletion

The origin has Jacobian

\[
J_0=
\begin{pmatrix}
-\delta&a\\
0&-\mu
\end{pmatrix}.
\]

It is locally asymptotically stable for every parameter choice. A tiny amount of \(C\) cannot rebuild itself when \(E\) is also tiny: its paid renewal is second order in the two stocks.

At a positive equilibrium,

\[
J_*=
\begin{pmatrix}
-\delta-uC_*&
\dfrac{a}{(1+C_*/K)^2}-m\\
\eta uC_*&0
\end{pmatrix}.
\tag{14}
\]

Its trace is strictly negative and its determinant is

\[
\boxed{\det J_*=-\eta uC_*h'(C_*).}
\tag{15}
\]

On the lower root \(h'(C_-)>0\), so the determinant is negative: that equilibrium is a saddle. On the upper root \(h'(C_+)<0\), so the determinant is positive and the trace is negative: that equilibrium is locally asymptotically stable.

Therefore, when (8) holds, both the origin and the upper positive equilibrium have attracting neighborhoods. The same resources, technology, depreciation rates, and paid allocation rule support recovery from some initial conditions and depletion from others.

This proves a basin distinction, not the exact global basin boundary. Small disturbances near the upper equilibrium recover. Large disturbances can place the system in the origin's basin. The presence of a positive equilibrium does not establish that the present state can reach it before an independently specified failure deadline.

For additional phase-plane control, use the Dulac multiplier \(B(E,C)=1/C\) in the strictly positive quadrant:

\[
\frac{\partial(B\dot E)}{\partial E}
+\frac{\partial(B\dot C)}{\partial C}
=-\frac{\delta}{C}-u<0.
\tag{16}
\]

There are no periodic orbits wholly within that quadrant. A stronger explicit global extinction proof, supplied by the coordinating agent's independent algebraic audit, avoids relying on a phase-plane limit-set argument.

For \(u>0\) and \(C(0)>0\), define

\[
W=E+\frac C\eta+
\frac{\delta}{\eta u}\log\frac CK.
\tag{16a}
\]

The logarithm is dimensionless. \(W\) need not be nonnegative and is not used as a positive-definite Lyapunov function. Its derivative cancels the support-loss term:

\[
\dot W=h(C)-\frac{\delta m}{u}
=mK\left[\frac{Aq}{1+q}-q-d\right],
\qquad q=\frac CK.
\tag{16b}
\]

The maximum of \(Aq/(1+q)-q\) on \(q\geq0\) is
\((\max(\sqrt A-1,0))^2\). Strictly below the positive-equilibrium threshold, put

\[
\sigma=d-(\max(\sqrt A-1,0))^2>0.
\]

Then \(W(t)\leq W(0)-mK\sigma t\). Since \(V=E+C/\eta\geq0\),

\[
\frac{\delta}{\eta u}\log\frac{C(t)}K
=W(t)-V(t)
\leq W(0)-mK\sigma t.
\]

It follows that

\[
\boxed{
C(t)\leq
C(0)\exp\left(\frac{\eta u}{\delta}V(0)\right)
\exp\left(-\frac{\mu uK\sigma}{\delta}t\right).
}
\tag{16c}
\]

Thus \(C\) decays exponentially. The inequality
\(\dot E\leq aC-\delta E\) then proves \(E\to0\). If \(C(0)=0\), the conclusion follows directly from the invariant boundary; if \(u=0\), \(C\) decays at rate \(\mu\) and the same comparison handles \(E\).

This global extinction theorem excludes equality at the fold, where \(\sigma=0\) and a positive nonhyperbolic equilibrium exists. It includes all initial nonnegative stocks strictly below the parameter threshold: a larger inherited reserve can delay depletion but cannot sustain this model indefinitely.

## 5. A resource floor produces a bounded feasible intensity range

Suppose \(E\geq e_{\min}>0\) is a protected support constraint. Positive-equilibrium existence and satisfaction of that floor are distinct requirements.

From (5),

\[
E_+\geq e_{\min}
\quad\Longleftrightarrow\quad
u\leq\frac{m}{e_{\min}}.
\tag{17}
\]

Consequently a stable positive equilibrium with a strict support margin exists exactly when

\[
\boxed{
A>1,\qquad
u_{\mathrm{crit}}<u<
\frac{m}{e_{\min}},
\qquad u\leq u_{\max}.
}
\tag{18}
\]

There is some such intensity if and only if

\[
\boxed{
A>1,\qquad
u_{\mathrm{crit}}<
\min\left(u_{\max},\frac{m}{e_{\min}}\right).
}
\tag{19}
\]

Equality at \(u=m/e_{\min}\) places the equilibrium exactly on the support floor, with no reserve margin. Equality at \(u=u_{\mathrm{crit}}\) is the nonhyperbolic fold. Neither endpoint supplies the interior robustness claimed in (18).

The upper correction branch \(C_+(u)\) strictly increases with \(u\). This follows by differentiating (6): \(h'(C_+)\,dC_+/du=-\delta m/u^2\), with \(h'(C_+)<0\). Meanwhile \(E_+(u)=m/u\) strictly decreases.

Thus greater operating intensity can increase maintained corrective capacity while reducing support reserves. Crossing the support floor means failure of the declared protection specification; it does not mean mathematical extinction under the unmodified differential equations.

If a correction floor \(C\geq c_{\min}>0\) is also required, then:

1. If \(c_{\min}\leq C_{\mathrm{fold}}\), every upper-branch equilibrium strictly above the fold has \(C_+>c_{\min}\), apart from equality at the excluded fold.
2. If \(C_{\mathrm{fold}}<c_{\min}<K(A-1)\), a strict correction margin requires
   \[
   u>\frac{\delta m}{h(c_{\min})}.
   \tag{20}
   \]
3. If \(c_{\min}\geq K(A-1)\), no finite \(u\) achieves a strict correction margin, since \(C_+(u)\to K(A-1)\) as \(u\to\infty\).

Combine this lower bound with (18); maintaining two protected stocks can leave an empty interval even when positive equilibria exist.

These are equilibrium feasibility conditions. A stable equilibrium strictly inside the protected set gives a sufficiently small forward-safe neighborhood by Lyapunov stability. We have not shown that every initial point satisfying the floors remains above them. Transients, depletion basins, and intervention delays remain separate questions.

### Root-agent illustration parameters

For \(a=9\) and \(\delta=\mu=\eta=K=1\), \(A=9\), \(m=1\), and \(u_{\mathrm{crit}}=1/4\). With \(e_{\min}=1\), stable positive equilibria have a strict support margin for

\[
\frac14<u<1.
\]

At \(u=1/2\),

\[
E^*=2,\qquad C_\pm=3\pm\sqrt7.
\]

At \(u=.2\), no positive equilibrium exists. At \(u=1.5\), a stable positive equilibrium exists but its support coordinate is \(2/3<e_{\min}\). These are analytical examples, not empirical estimates. The root agent is validating the corresponding numerical trajectories separately.

## 6. Why a universal linear spectral threshold would miss this example

For a genuinely linear, positive renewal network

\[
\dot z=(B-D)z,
\qquad B\geq0,\quad D=\operatorname{diag}(d_i)>0,
\]

the familiar threshold is the spectral radius of the lifetime production matrix \(BD^{-1}\) (equivalently \(D^{-1}B\)). Below one, decay dominates linear regeneration; above one, the linear system has an expanding mode. Saturation, resource limits, and finite shocks require further analysis. The next-generation construction has established primary precedent in [van den Driessche and Watmough](https://watmough.ext.unb.ca/papers/mgroup.pdf); positive-system graph conditions are studied by [Duan, Jafarpour, and Bullo](https://arxiv.org/abs/1905.05868). These are prior mathematics, not results introduced here.

Model (1) shows a limitation of that attractive organizing quantity. Its linearization at the origin has only the edge from \(C\) to \(E\); the return edge is the product \(EC\), and vanishes to first order. Taking

\[
B_0=
\begin{pmatrix}0&a\\0&0\end{pmatrix},
\qquad D_0=\operatorname{diag}(\delta,\mu),
\]

gives

\[
\rho(B_0D_0^{-1})=0
\]

for every parameter choice, including choices with an attracting positive equilibrium.

Hence a linear reproduction threshold at the depleted state cannot characterize all self-maintaining regimes. Here the relevant mechanism needs two jointly present ingredients and a finite stock configuration. A directed interaction graph loses that joint requirement unless it is represented as a higher-order reaction or dependency.

This is a concrete reason to retain separate questions about whether a renewal organization can be sustained once established and whether it can arise or recover from a given depleted state. The spectral threshold remains useful within its linearization assumptions; it is not a universal replacement for nonlinear feasibility and basin analysis.

## 7. Prior art and contribution status

The ingredients are established. [Holland, DeAngelis, and Bronstein (2002)](https://doi.org/10.1086/338510) analyze how separate, density-dependent benefits and costs shape mutualistic dynamics, including saturating and unimodal net effects. [Holland and DeAngelis (2010)](https://pubs.usgs.gov/publication/70003826) connect resource supply and consumption in mutualistic interactions; their framework permits both supportive relationships and overexploitation. These precedents directly caution against claiming that the presence of a beneficial dependency implies uniformly positive feedback or stability.

[Wagner et al. (2017)](https://chemistry-europe.onlinelibrary.wiley.com/doi/10.1002/cphc.201601293) study bistability in specified self-replication and autocatalytic systems. Its reaction-order conclusions concern its own models and should not be imported unchanged into the institutional interpretation here.

The derivation in this memo was performed for the stated model during this research session. The equation's appearance elsewhere has not been exhaustively investigated. Its prospective contribution to the local program is a compact, auditable coupling of paid correction, depreciation, inherited capacity, support reserves, and a limit on intensity. The square-root threshold is a consequence of the chosen rational production law, not a proposed universal exponent.

## 8. Assumptions, countercases, and tests

**Selection over the allocation rule is absent.** Fixed \(u\) is a constitutive mechanism, not a supervisor stock. Nonetheless, whether competing actors preserve this rule is a different open problem. A later selection module must give both beneficial and harmful rule changes genuine possibilities and charge their implementation costs.

**Support renewal is an assumed causal benefit.** The term \(P(C)\) would be false if the supposed corrector merely records problems, extracts rents, or shifts damage outside the boundary. It must be estimated independently of the label “correction.”

**Corrector reproduction requires inherited capacity.** A bootstrap term independent of \(C\), outside assistance, or institutional rebuilding from another carrier can remove the absorbing boundary and alter bistability. These are substantive alternatives, not violations of a universal principle.

**Functional form matters.** Saturation in support production and bilinear paid renewal produce the specific threshold and basin structure. Linear low-density cross-production can instead destabilize the origin when a loop-gain threshold exceeds one. Other constraints, delays, or spatial structures can create oscillations absent from this planar model.

**The state is not a complete theory of legitimacy.** A durable coercive apparatus can satisfy these stock equations. Whose corrections count, whose support is consumed, and which actions are legitimate require additional variables and justified constraints.

**Finite stochastic systems may go extinct.** Local stability of the deterministic upper equilibrium does not imply survival forever under demographic noise or large shocks.

Prioritized tests:

1. Check algebra, positive-domain invariance, eigenvalue signs, and the stated no-cycle calculation independently.
2. Numerically compare low intensity, feasible intensity, excessive intensity relative to a specified floor, and depleted initial conditions under identical feasible intensity.
3. Test whether the paid-flow accounting can be observed: support spent, corrective capacity replaced, and independently measured support renewal should fit the same transfer relation.
4. Estimate the depletion rates and the full net-renewal curve \(h(C)\), rather than only the final equilibria. The threshold predicts that a positive state disappears when its maximum falls below required support loss.
5. Perturb both initial stocks separately. A failure to find the predicted basin distinction, where the functional assumptions are otherwise verified, would count against this model.
6. Test alternatives with spontaneous rebuilding, bounded effort, different saturation, and endogenous allocation. Record which conclusions persist and which were consequences of the minimal assumptions.

The strongest present result is conditional: correction can be a maintained internal capacity with real costs, yet stable operation requires both sufficient renewal intensity and adequate support reserves. Parameter feasibility, current-state recoverability, the persistence of the allocation rule, and normative legitimacy remain different propositions.
