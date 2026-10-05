# Paid correction and the selection of its funding practice

This note constructs one conditional mechanism in which useful contextual evidence, executable revision, paid institutional capacity, and copying of an operating policy form a closed feedback loop. Correction is not supplied by an inexhaustible outside controller. The same model permits a self-maintaining funded regime and loss of that regime. An exact threshold combines the privately recoverable benefit of a contextual response, the cost of replacing capacity, and the financing fraction.

The construction is a research result derived for this project, not an established novelty claim or an empirical finding. Its fixed task family, benefit attribution, membership access, and budget commitment remain constitutive assumptions. It concerns the survival of a financed correction service and its funding practice, not the endogenous legitimacy or uninvadability of a constitution. Losing the modeled institution is not equivalent to extinction of society.

## A contextual task and observable output

Each carrier repeatedly encounters an independently sampled context, L or R with equal probability. A baseline action, chosen without information about the current context, receives an output increment \(\Delta>0\) when appropriate to that context and zero otherwise. There is also a nonnegative background output \(b\). Baseline expected output is therefore

\[
y_0=b+\Delta/2>0.
\]

A noisy test names the appropriate action with probability \(\alpha\in(1/2,1]\). It can be used only when both a test-delivery channel and an implementation channel function. These channels have conditionally independent success probability \(C/(K+C)\), where \(C\ge0\) is a stock of paired staff and infrastructure and \(K>0\) is its half-saturation scale. Thus

\[
q(C)=\left(\frac C{K+C}\right)^2,
\qquad B=\Delta(\alpha-1/2)>0.
\]

If either channel fails, the carrier uses the baseline action. If both work, it follows the noisy test. The expected extra output is exactly \(Bq(C)\). This is a bounded family of contextual inference-and-action tasks, not open-ended discovery or a moral oracle. In particular, \(B\le y_0\); a perfect test is not required.

The single stock is explicitly a **paired** service package: its conversion cost pays for both kinds of capacity. Two independent stocks with separate depreciation would be a different model. Separate channel impairment can be represented by multiplying \(q\) by factors \(e,a\in[0,1]\); the results below then replace \(B\) by \(eaB\).

## Allocation and funding policies

The share \(x\in[0,1]\) uses policy R. A carrier using R joins the funded service, obtains its testing and implementation access, and pays a fixed fraction \(\tau\in(0,1)\) of its direct receipts into capacity replacement. Policy D retains the baseline action and pays no fee. Joining or leaving changes access; D does not get the direct test-and-act service for free. The physical or contractual possibility of this exclusion, receipt measurement, and execution of the funding commitment are assumptions, not conclusions about political authority.

A fraction \(\chi\in(0,1]\) of the additional output can be retained by its R carrier. The rest is shared equally as a common spillover. Define

\[
A=\chi B,\qquad 0<A\le B\le y_0,
\qquad r(C)=y_0+Aq(C),
\qquad S(x,C)=(1-\chi)xBq(C).
\]

The observable expected private returns are

\[
U_R=(1-\tau)r(C)+S(x,C),
\qquad U_D=y_0+S(x,C).
\]

Their difference is derived from output receipts and an actual payment:

\[
s(C):=U_R-U_D=(1-\tau)Aq(C)-\tau y_0.
\tag{1}
\]

The total flow paid to replace capacity is \(F=\tau x r(C)\). Gross aggregate output is \(y_0+xBq(C)\). Aggregate consumption plus that payment equals gross output exactly:

\[
xU_R+(1-x)U_D+F=y_0+xBq(C).
\tag{2}
\]

There is no free reward for a practice labeled corrective. Common spillovers do not independently finance the service. A world with more shared benefit and less recoverable direct benefit can therefore make a useful service harder to sustain under this particular funding arrangement.

## Dynamics from funding and copying

Paid replacement converts output into capacity at rate \(\eta>0\); capacity depreciates at rate \(\mu>0\). Carriers copy the practice of a sampled carrier at a rate proportional to its positive return advantage. The per-carrier switching rates are

\[
k_{D\to R}=\kappa x[s(C)]_+,
\qquad
k_{R\to D}=\kappa(1-x)[-s(C)]_+,
\]

where \(\kappa>0\). After averaging repeated task outcomes and taking the deterministic population approximation, the closed state equations are

\[
\boxed{
\dot x=\kappa x(1-x)s(C),\qquad
\dot C=\eta\tau x\,[y_0+Aq(C)]-\mu C.
}
\tag{3}
\]

Copying depends on current measured private returns, not on a welfare term or foresight about institutional survival. Averaging, imitation, and a constant carrier population are behavioral assumptions. Finite populations can lose R through stochastic absorption; the differential equations do not guarantee survival under such noise.

The domain \([0,1]\times[0,\infty)\) is invariant. At \(C=0\), inherited R carriers can use their baseline receipts to rebuild capacity, since \(\dot C=\eta\tau xy_0\). At \(x=0\), R cannot reappear through copying alone. This distinction permits financing after infrastructure loss but excludes spontaneous recreation of a vanished operating practice.

Since \(q\le1\),

\[
\dot C\le\eta\tau(y_0+A)-\mu C.
\tag{4}
\]

All solutions are bounded and exist for all future time. The renewable supply of task opportunities and the conversion technology are maintained environmental assumptions. There is no separate ecological support stock in this minimal model.

## Capacity at a fixed prevalence

For fixed \(x>0\), put

\[
h_x(C)=\eta\tau x r(C)-\mu C.
\]

There is exactly one positive root \(C_x\), and it is asymptotically stable for the scalar capacity equation. To prove this, divide by \(C>0\):

\[
\frac{h_x(C)}C
=\eta\tau x\left[\frac{y_0}C+
\frac{AC}{(K+C)^2}\right]-\mu.
\]

The derivative of the bracket is

\[
-\frac{y_0}{C^2}+\frac{A(K-C)}{(K+C)^3}<0.
\tag{5}
\]

For \(C\ge K\) the sign is immediate. For \(0<C<K\), use \(A\le y_0\) and \(C^2(K-C)<(K+C)^3\). The quotient goes from positive infinity to \(-\mu\), proving uniqueness. At its zero, \(h_x'(C_x)=C_x(h_x/C)'<0\). Write \(C_R=C_1\) for the full-R equilibrium capacity.

The task-derived bound matters. Arbitrarily large upside \(A/y_0\), outside this task family, can produce several positive capacity roots. No uniqueness claim is made for that extension.

## Exact selection and financing threshold

First suppose

\[
q_s:=\frac{\tau y_0}{(1-\tau)A}<1.
\]

The unique capacity at which the two practices have equal private returns is

\[
C_s=K\frac{\sqrt{q_s}}{1-\sqrt{q_s}}.
\tag{6}
\]

The prevalence that exactly funds this capacity is

\[
x_s=\frac{\mu C_s}{\eta\tau r(C_s)}
=\frac{\mu C_s(1-\tau)}{\eta\tau y_0}.
\tag{7}
\]

At \(x=1\), uniqueness of the capacity root gives

\[
C_R>C_s
\quad\Longleftrightarrow\quad
h_1(C_s)>0
\quad\Longleftrightarrow\quad x_s<1.
\tag{8}
\]

Thus a full-R funded equilibrium is strictly resistant to replacement by D precisely when \(q_s<1\) and \(x_s<1\). Its two eigenvalues are \(-\kappa s(C_R)<0\) and \(h_1'(C_R)<0\), so it is locally asymptotically stable relative to the physical domain. If \(q_s\ge1\), then \(s(C)<0\) for every finite \(C\), excluding strict selection resistance.

These conditions give an explicit financing window. Put \(z=\sqrt{q_s}\in(0,1)\). Then

\[
\tau=\frac{Az^2}{y_0+Az^2},\qquad
C_s=K\frac z{1-z},\qquad
x_s=\frac{\mu K}{\eta A z(1-z)}.
\tag{9}
\]

Because \(\max_{0<z<1}z(1-z)=1/4\), some fixed financing fraction supports a strictly selected funded equilibrium if and only if

\[
\boxed{\eta\chi B>4\mu K.}
\tag{10}
\]

When (10) holds, define

\[
z_\pm=\frac{1\pm\sqrt{1-4\mu K/(\eta A)}}2,
\qquad
\tau_\pm=\frac{Az_\pm^2}{y_0+Az_\pm^2}.
\]

The exact interval for strict selection resistance is

\[
\boxed{\tau_-<\tau<\tau_+.}
\tag{11}
\]

Too little funding produces too little functioning capacity to justify its fee. Too much funding leaves too little privately retained gain to keep R selected. The factor four comes from the stipulated paired-channel technology; it is not a proposed universal constant. The interval is a feasibility result, not a prescription to maximize a social objective or adopt its midpoint.

At any full-R equilibrium, the same threshold has a direct resource interpretation:

\[
s(C_R)=Aq(C_R)-\frac{\mu C_R}{\eta},
\qquad
\frac{Aq(C)}C=\frac{AC}{(K+C)^2}\le\frac A{4K}.
\tag{12}
\]

The maximum recoverable correction benefit per unit capacity must exceed its replacement cost. This comparison uses actual produced output and the paid conversion law.

## Persistence and loss under the same parameters

Assume a fee strictly inside (11). The set

\[
\mathcal R=\{(x,C):x_s\le x\le1,\ C\ge C_s\}
\tag{13}
\]

is forward invariant. On \(C=C_s\), \(\dot C=\eta\tau r(C_s)(x-x_s)\ge0\). Throughout the set \(s(C)\ge0\), so \(x\) is nondecreasing. The bounds (4) control the unbounded upper edge.

Every trajectory in \(\mathcal R\) other than the corner \((x_s,C_s)\) converges to \((1,C_R)\). Here is a direct proof. If a trajectory does not start on \(x=1\), the inward boundary conditions and strict inequalities make \(x>x_s\) after some finite time, unless it is the corner equilibrium. As \(x\) is bounded and nondecreasing, it has a limit \(\ell\). If \(\ell<1\), the logit identity

\[
\frac{d}{dt}\log\frac{x}{1-x}=\kappa s(C)
\tag{14}
\]

and bounded derivatives imply \(s(C)\to0\), hence \(C\to C_s\). The capacity equation then has a limiting derivative \(\eta\tau r(C_s)(\ell-x_s)\), which must vanish. This requires \(\ell=x_s\), contradicting the preceding strict increase. Therefore \(x\to1\). Scalar comparison with \(h_{1-\epsilon}\) and \(h_1\), followed by \(\epsilon\downarrow0\), yields \(C\to C_R\). For \(x=1\), scalar convergence follows directly.

The corner is an exact saddle. At \((x_s,C_s)\), the Jacobian has entries \(J_{11}=0\),

\[
J_{12}=\kappa x_s(1-x_s)s'(C_s)>0,
\qquad J_{21}=\eta\tau r(C_s)>0,
\]

so its determinant is \(-J_{12}J_{21}<0\).

There is also an explicit loss basin under these same parameters. Choose \(0<c_\ell<C_s\), and

\[
0<x_\ell<\min\left(1,
\frac{\mu c_\ell}{\eta\tau r(c_\ell)}\right).
\tag{15}
\]

The rectangle \(0\le x\le x_\ell,\ 0\le C\le c_\ell\) is invariant. Its upper capacity edge points inward, and its upper prevalence edge has \(s(C)\le s(c_\ell)<0\). Within it,

\[
\dot x\le-\kappa[-s(c_\ell)](1-x_\ell)x,
\]

so \(x\to0\) exponentially. Then \(\dot C\le\eta\tau(y_0+A)x-\mu C\) gives \(C\to0\). Independently, the Jacobian at \((0,0)\) has eigenvalues \(-\kappa\tau y_0\) and \(-\mu\), so the depleted state is always locally asymptotically stable.

These facts prove coexistence of attraction basins, not their entire boundary. The saddle supplies a separatrix candidate, whose full continuation requires additional analysis.

## Strictly insufficient recoverable benefit causes global loss

Suppose \(\eta A<4\mu K\). For every fixed \(\tau\in(0,1)\), (12) gives \(s(C_R)<0\). The actual capacity satisfies \(\dot C\le h_1(C)\), so scalar comparison implies \(\limsup C(t)\le C_R\). By continuity and monotonicity of \(s\), eventually \(s(C(t))\le-\epsilon<0\). For any initial \(x(0)<1\), the logit identity (14), or the invariant boundary \(x=0\), gives \(x\to0\). The linear capacity comparison again gives \(C\to0\).

Thus strictly below the threshold, arbitrarily large initial capacity can delay but cannot prevent loss when D is present. The exception \(x(0)=1\) is substantive: purely imitative dynamics cannot introduce an absent alternative, so the full-R boundary remains invariant even when it is invasible. Equality \(\eta A=4\mu K\) and financing endpoints have nonhyperbolic cases and are not included in this strict result. For parameters above the threshold but fees strictly outside the closed interval \([\tau_-,\tau_+]\), the same argument applies because \(s(C_R)<0\).

## Finite initiation without a permanent subsidy

The existence of a functioning basin does not pay for entry. One explicit sufficient initiation cost can nevertheless be bounded. Assume the favorable parameter and fee conditions, an inherited \(x_0>0\), a target \(x_T\in(x_s,1)\), and a reserve \(C_1>C_s\). Put

\[
g_1=s(C_1)>0,
\qquad
T=\frac{[\operatorname{logit}(x_T)-\operatorname{logit}(x_0)]_+}
{\kappa g_1}.
\]

If a one-time installation creates

\[
C_{\rm seed}\ge C_1 e^{\mu T},
\tag{16}
\]

then \(\dot C\ge-\mu C\) ensures \(C(t)\ge C_1\) until \(T\). Consequently (14) gives \(x(T)\ge x_T\); the trajectory has entered \(\mathcal R\) and thereafter converges to \((1,C_R)\) without further subsidy. If \(x_0\ge x_T\), take \(T=0\).

Under the same exact conversion technology and with no additional installation cost, the direct expenditure for this chosen seed is

\[
\frac{[C_{\rm seed}-C_{\rm initial}]_+}{\eta}.
\tag{17}
\]

This is a sufficient, often very conservative, stock-injection construction. It assumes an authorized instantaneous installation, an actual source of its finite expenditure, and no additional installation cost; it does not derive political authorization or an optimal transition. It cannot regenerate R from \(x_0=0\) through imitation. The growth of R during the transition is endogenous copying of its net returns, not a forced change of its prevalence.

## Negative controls and constitutional residue

If either evidence or implementation is disabled while the fee still applies, then \(q=0\), \(s=-\tau y_0<0\), and every initial \(x<1\) leads to \(x,C\to0\). Resources must continue to be charged in this control; silently removing the fee would change the question.

If D receives the same direct service free of charge, then its return becomes \(r(C)+S\), while R retains \((1-\tau)r(C)+S\). The advantage is now \(-\tau r(C)<0\). Again every initial \(x<1\) loses R and ultimately the capacity. This is an important limitation: the model does not solve financing a nonexcludable public correction service. Other institutions could finance such a service, but would require new mechanisms.

The selection of R is not selection over every constitutional parameter. The fee \(\tau\), recoverability \(\chi\), receipt accuracy, exclusion technology, and the paired conversion law remain fixed. Fraudulent receipts, appropriation of the funding pool, hostile removal of access rights, competing fee schedules, coordinated invaders, changing task distributions, and manipulation of what is counted as output are outside the theorem. The operating package has endogenous financing and prevalence; the constitution enabling that package does not acquire its own survival proof by implication.

## A noisy task witness

Take \(b=0\), \(\Delta=2\), \(\alpha=.9\), \(\chi=1\), so \(y_0=1\), \(B=A=.8\). Let \(K=\mu=\kappa=1\), \(\eta=10\), and \(\tau=1/6\). The financial threshold is \(\eta A=8>4\), and

\[
C_s=1,\qquad x_s=1/2.
\]

The full-R capacity is the unique positive root of

\[
3C^3-3C^2-7C-5=0,
\]

namely \(C_R\simeq2.317295406891336\). At that equilibrium, \(q\simeq.4879715551684846\) and the R net-return advantage is approximately \(.15864770344565637\). The strict financing interval is approximately

\[
.016867880450547195<\tau<.36822528725131615.
\]

Initial conditions \((x,C)=(.6,1.2)\) lie in the certified recovery region. A certified loss rectangle is \(x\le.25, C\le.5\), because the upper-edge funding limit is \(x\le27/98\) and \(s(.5)=-5/54\). Thus \((.2,.4)\) loses the institution under exactly the same parameters. These numbers are model witnesses, not measurements. This particular witness uses fully retained direct benefit; examples with public spillovers have \(\chi<1\) and the threshold applies unchanged through \(A=\chi B\).
