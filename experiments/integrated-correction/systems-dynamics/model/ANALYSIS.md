# Equilibria basins and feedback in the funded verification model

This analysis examines the actual dynamics of the [four-state constitutional extension](../../constitutional-extension/model/CONSTRUCTION.md). It identifies its mixed equilibria, their instability, its two kinds of attracting regimes, and several distinct ways a trajectory can change outcome. It also finds a structural restriction: after a positive change of clock, the interior flow is strongly cooperative. The model therefore cannot have an attracting periodic orbit in its strict interior. Complexity of interpretation should not be confused with evidence of arbitrary complex dynamics.

These are properties of one specified deterministic model. Its financing rules, task distribution, production accounting and practice repertoire remain fixed. The model does not yet contain multiple changing goals, endogenous interpretation of evidence, evolution of its constitution, or a complete commons ecology. No previous sealed artifact is changed by this analysis.

## Equations and notation

Use state order \((x,C,G,h)\), where \(x\) is paying participation, \(C\) useful service capacity, \(G\) verification capacity, and \(h\) the share of contractors delivering maintenance and reporting truthfully within the stipulated two-practice repertoire. Let

\[
q(C)=\left(\frac C{K+C}\right)^2,\quad
p(G)=\frac G{L+G},\quad
r(C)=y_0+Aq(C),\quad D=hp(G),
\]

with \(0<A\le y_0\). Define positive constants

\[
a_C=\eta_C\lambda\tau,\quad
a_G=\eta_Gm(1-\lambda)\tau,\quad
v=(1-\lambda)\tau.
\]

The equations are

\[
\begin{aligned}
\dot x&=\kappa x(1-x)s,\qquad
s=Aq(C)D-\tau r(C),\\
\dot C&=a_Cxr(C)-\mu_CC,\\
\dot G&=a_Gxhr(C)-\mu_GG,\\
\dot h&=\nu h(1-h)vxr(C)(D-m).
\end{aligned}
\tag{1}
\]

Both shares remain in \([0,1]\), and both capacities are bounded. Thus a reinforcing loop in this model is not unbounded physical growth or mathematical blow-up. It changes participation, maintenance and the capacities they can finance within bounded stocks.

## The complete equilibrium catalogue

At any equilibrium with \(x>0\),

\[
x=\frac{\mu_CC}{a_Cr(C)},\qquad
G=\rho h C,\qquad
\rho=\frac{a_G\mu_C}{a_C\mu_G}.
\tag{2}
\]

The map \(C/r(C)\) is strictly increasing under \(A\le y_0\). Let \(C_R\) be the unique positive solution of \(a_Cr(C_R)=\mu_CC_R\), and put \(G_R=\rho C_R\). The following list exhausts equilibria in the physical domain, apart from coincidences at branch intersections.

**Depleted line.** Every point

\[
E_0(h_0)=(0,0,0,h_0),\qquad 0\le h_0\le1,
\tag{3}
\]

is an equilibrium. With no financed work, the contractor copying clock stops. It is inaccurate to represent all depletion as convergence to a single fully fraudulent point. The transverse eigenvalues are \(-\kappa\tau y_0,-\mu_C,-\mu_G\), with one zero eigenvalue tangent to the line. The line is locally attracting transversely; an individual point is not an isolated asymptotically stable equilibrium.

**Paying population with only fraudulent maintenance.**

\[
E_F=(1,C_R,0,0).
\tag{4}
\]

This boundary equilibrium has a positive user invasion eigenvalue \(\kappa\tau r(C_R)\), and three negative eigenvalues. It persists exactly on an invariant face that contains no bypass practice, but is not an attractor for nearby populations containing bypass.

**Full paying and delivered-maintenance equilibrium.**

\[
E_R=(1,C_R,G_R,1).
\tag{5}
\]

The earlier result applies: it is strictly stable precisely when

\[
Aq(C_R)p(G_R)>\tau r(C_R),\qquad p(G_R)>m.
\tag{6}
\]

**Mixed users with full delivered maintenance.** Set \(h=1\). A possible equilibrium has \(C=C_X\), where

\[
Aq(C_X)p(\rho C_X)=\tau r(C_X),
\quad x_X=\frac{\mu_CC_X}{a_Cr(C_X)},
\quad G_X=\rho C_X.
\tag{7}
\]

There is at most one positive root. Any zero requires \(p(\rho C)>\tau\); above that point the left side minus the right side is strictly increasing. A finite positive root exists exactly when \((1-\tau)A>\tau y_0\). It belongs to the mixed physical branch only if \(x_X<1\), equivalently \(C_X<C_R\). Its dynamics within the \(h=1\) face have one unstable direction. The additional contractor invasion eigenvalue is

\[
-\nu v x_Xr(C_X)[p(G_X)-m].
\tag{8}
\]

Thus this equilibrium has one or two unstable directions depending on that sign; it is never a stable mixture.

**Mixed contractors with full paying participation.** Set \(x=1\), \(C=C_R\). An interior contractor share must have \(D=m\), giving

\[
h_H=\frac{m+\sqrt{m^2+4mL/(\rho C_R)}}2,
\quad G_H=\rho h_H C_R.
\tag{9}
\]

It is physical precisely when \(h_H<1\), or \(p(G_R)>m\). The \((G,h)\) block has negative determinant and is a saddle. The user-transverse eigenvalue is

\[
-\kappa\big[(m-\tau)Aq(C_R)-\tau y_0\big].
\tag{10}
\]

Again there are one or two unstable directions, not an attracting mixed regime.

**Fully mixed equilibrium.** If both practice shares are interior, \(D=m\) and \(s=0\). Therefore

\[
q_I=\frac{\tau y_0}{A(m-\tau)},\qquad
C_I=K\frac{\sqrt{q_I}}{1-\sqrt{q_I}},
\]

\[
x_I=\frac{\mu_CC_I}{a_Cr(C_I)},\qquad
h_I=\frac{m+\sqrt{m^2+4mL/(\rho C_I)}}2,
\qquad G_I=\rho h_I C_I.
\tag{11}
\]

This branch exists in the physical interior only when \(m>\tau\), \(0<q_I<1\), \(x_I<1\), and \(h_I<1\). It has exactly two real positive eigenvalues and two eigenvalues with negative real parts, as proved below. It is an index-two saddle, not a third attractor between healthy and depleted operation.

## Why the mixed equilibria are unstable

At a fully mixed equilibrium the Jacobian has the sign-structured form

\[
J=
\begin{pmatrix}
0&a&b&c\\
d&-e&0&0\\
f&g&-j&k\\
0&0&\ell&n
\end{pmatrix},
\tag{12}
\]

where all displayed letter coefficients are positive. The positive \(n\) expresses the direct effect of more genuine peers on their own selection. The useful-capacity relaxation satisfies \(e>0\) by the task-domain bound. The common dependence on \(D\) gives the exact relation \(c\ell=bn\).

Its characteristic polynomial is

\[
P(z)=
[z(z+e)-ad]\,[(z+j)(z-n)-k\ell]
-bz[f(z+e)+gd].
\tag{13}
\]

Each bracket has one positive root, denoted \(u,w\). At zero, \(P(0)=ad(jn+k\ell)>0\). At either positive bracket root, \(P<0\); at sufficiently large positive \(z\), \(P>0\). Thus there is a positive eigenvalue below \(\min(u,w)\) and another above \(\max(u,w)\).

There can be only two positive roots. The cubic coefficient of \(P\) is \(e+j-n\); its quadratic coefficient is

\[
ej-n(e+j)-k\ell-ad-bf.
\]

If the cubic coefficient is negative, the quadratic coefficient is also negative. With positive leading and constant coefficients, this precludes four sign changes in the polynomial coefficients. Descartes' rule, together with the two exhibited roots, gives exactly two positive roots. Moreover \(w>n\), because the second bracket at \(z=n\) equals \(-k\ell\). The sum of the remaining two roots is therefore less than \(-e-j\), and their product is positive. They are either both negative real roots or a conjugate pair with negative real parts.

For the \(h=1\) mixed-user face, the corresponding cubic is

\[
z(z+e)(z+j)-ad(z+j)-b[f(z+e)+gd].
\tag{14}
\]

Its constant term is negative and its quadratic coefficient is positive; Descartes' rule gives exactly one positive root. The other two have positive product and negative sum, hence negative real parts. The remaining eigenvalue is the real number (8). The mixed-contractor face has one real positive and one real negative eigenvalue in its two-dimensional \((G,h)\) block, plus the negative capacity eigenvalue and the real number (10).

Consequently none of these equilibrium branches can produce a local Hopf bifurcation while it remains admissible in the strict parameter domain. Local stability changes found here involve real invasion eigenvalues crossing zero. This statement does not by itself rule out periodic orbits created by global mechanisms; the stronger interior-cycle restriction below uses a separate argument.

## Canonical equilibria and slow saddle transients

Use the audited witness \(y_0=1,A=.8,K=L=\mu_C=\mu_G=\kappa=1\), \(\tau=.15\), \(\lambda=m=.5\), \(\eta_C=800/29\), \(\eta_G=1600/29\), and \(\nu=10\). Approximate equilibrium values are listed in state order \((x,C,G,h)\).

| Equilibrium | State | Eigenvalues |
|---|---|---|
| Full operation | \((1,3,3,1)\) | \(-1,-.844828,-.12,-.271875\) |
| Fraudulent boundary | \((1,3,0,0)\) | \(-.844828,+.2175,-1,-.54375\) |
| Mixed users | \((.618029,1.680802,1.680802,1)\) | \(+.078692,-.900206,-1,-.077366\) |
| Mixed contractors | \((1,3,2.186141,.728714)\) | \(+.186532,-1.039020,-.844828,-.0075\) |
| Fully mixed | \((.923752,2.730300,2.035741,.745611)\) | \(+.006970,+.166976,-.850655,-1.036558\) |

The weakest positive mixed eigenvalue has reciprocal about 143 time units; the weakest stable mixed-contractor eigenvalue has reciprocal about 133. A long plateau near these saddles can therefore be a transient rather than another attractor. Simulation timeouts near basin boundaries must remain unclassified until the trajectory enters a proven region or a convergence test has sufficient support.

## Parameter variation and boundary branch exchanges

Hold all witness parameters fixed except \(m\). Then \(C_R=3\) and \(G_R=6m\). Full operation is strictly stable exactly when

\[
\boxed{\frac{29}{186}<m<\frac56.}
\tag{15}
\]

The lower endpoint is a user invasion threshold; the upper endpoint is a contractor invasion threshold. At neither endpoint does the full-operation equilibrium cease to exist. It changes stability while a mixed boundary branch meets it.

The additional branch intersections are

\[
m_1=\frac{29}{60}\simeq.4833333333,
\qquad
m_2=\frac{65-2\sqrt{505}}{30}\simeq.6685196631.
\tag{16}
\]

For \(m<m_1\), the physical mixed-contractor equilibrium has two unstable directions; for \(m>m_1\), it has one. The fully mixed branch enters the physical domain from it at \(m_1\). The mixed-user branch has one unstable direction below \(m_2\) and two above it; the fully mixed branch exits through it at \(m_2\). Hence the fully mixed branch is physical exactly for \(m_1<m<m_2\).

All four branch intersections are nondegenerate boundary transcritical exchanges in the smoothly extended equations: an invariant-face equilibrium persists, one real eigenvalue crosses zero, and a distinct mixed branch crosses the face with nonzero derivative. On the physical domain they appear as a branch entering or leaving the admissible region. They are not saddle-node disappearance of the full equilibrium and are not Hopf bifurcations.

For variation in \(\tau\) with \(m=.5\), the full capacities obey \(G_R=C_R\), with strictly increasing parameterization

\[
\tau(C_R)=
\frac{C_R}{(400/29)[1+.8(C_R/(1+C_R))^2]}.
\tag{17}
\]

The user-stable capacity interval lies between the two positive roots \(.6216963534\) and \(7.6237715158\) of

\[
29C_R^3-233C_R^2+87C_R+29=0.
\]

Contractor stability further requires \(C_R>1\). Thus full operation is strictly stable exactly for

\[
\boxed{.0604166667=29/480<\tau<.3400907365.}
\tag{18}
\]

The fully mixed branch is physical for

\[
1/12<\tau<.1586475628.
\tag{19}
\]

At the upper value, \(C_R=(51+4\sqrt{110})/29\simeq3.2052535837\). These numerical endpoints arise from the specified nonlinearities and accounting; they are not estimated social constants.

## A cooperative structure hidden by the physical clock

Some off-diagonal derivatives in the original clock change sign. For example, increasing current receipts accelerates fraudulent copying when \(D<m\), and accelerates genuine copying when \(D>m\). A signed feedback diagram that ignores this state dependence is misleading.

There is nevertheless an exact orbit-level simplification. In the strict interior, define funded time by

\[
\frac{d\theta}{dt}=xr(C)>0,
\qquad b(C)=\frac{Aq(C)}{r(C)}.
\]

Then

\[
\begin{aligned}
\frac{dx}{d\theta}&=\kappa(1-x)[b(C)D-\tau],\\
\frac{dC}{d\theta}&=a_C-\frac{\mu_CC}{xr(C)},\\
\frac{dG}{d\theta}&=a_Gh-\frac{\mu_GG}{xr(C)},\\
\frac{dh}{d\theta}&=\nu v h(1-h)(D-m).
\end{aligned}
\tag{20}
\]

Since \(b'(C)=Ay_0q'(C)/r(C)^2>0\), all off-diagonal derivatives of (20) are nonnegative. Its dependency graph is irreducible for \(0<x,h<1\) and \(C,G>0\). Thus the transformed flow is strongly cooperative. This is an established class of positive-feedback systems; [Hirsch's primary analysis](https://escholarship.org/content/qt67z7c17v/qt67z7c17v.pdf) studies its convergence properties and exclusion of attracting periodic solutions.

For this model, the exclusion can be seen directly. A hypothetical interior periodic orbit has a strictly positive variational monodromy matrix. Its principal eigenvalue is simple and has a positive eigenvector. The tangent vector has multiplier one. It cannot be the principal positive eigenvector: a one-signed tangent would remain one-signed under the positive variational flow, forcing every coordinate to move monotonically around a closed orbit. Consequently the principal multiplier exceeds one, and the periodic orbit is unstable. The positive clock change preserves closed orbits and their orbital stability because \(xr(C)\) is bounded away from zero on such an orbit.

Therefore the fixed-rule model has **no attracting periodic orbit in its strict interior**. We have not proved that every trajectory converges, ruled out unstable periodic orbits, or classified all boundary heteroclinic connections. On a depletion path, total funded time can be finite, so a generic convergence theorem for the rescaled interior cannot simply be applied to all physical-time trajectories.

## What the basin geometry permits us to say

The full-operation recovery basin is upward closed in componentwise state order. Suppose one positive initial state converges to \(E_R\), and another starts with at least as much of every component. In funded time the second trajectory dominates the first by cooperativity. Its \(x,h\) therefore approach one, and its funded clock continues indefinitely. Original-time scalar comparison gives \(\limsup C\le C_R\); the verification equation then gives \(\limsup G\le G_R\). Domination of the recovering trajectory supplies the reverse lower limits, proving convergence to the same \(E_R\).

Thus at fixed \(C_0,G_0\), a basin slice over \((x_0,h_0)\) must have an upper-set recovery region. A numerical pattern in which a strictly larger initial share pair loses while a smaller pair provably recovers would reveal numerical error, inadequate time classification, or a changed model. This order comparison uses the common funded clock; it does not assert componentwise ordering at equal physical times.

The comparison holds for already available initial stocks under unchanged rules. It neither pays the cost of creating those stocks nor establishes that expanding verification or authority is generally desirable. Its monotone structure is a substantive property of this particular technology and threat repertoire.

The two index-one boundary saddles and the index-two interior saddle help explain why the basin boundary can have multiple limiting failure directions. Their stable manifolds are natural candidates for pieces and intersections of the separatrix. The equilibrium analysis alone does not prove the full global separatrix; the numerical atlas should present its slice as a slice and retain uncertified points.

Crossing that separatrix under a finite disturbance is different from changing equilibrium stability. The earlier model already has an attracting funded region and a normally attracting depleted line at the same parameters. A sufficiently large shock can switch basins while every parameter and the healthy equilibrium's local stability remain unchanged.

## A specified feedback controller changes the model class

As a separate, explicitly added controller, suppose a manager adjusts the maintenance fraction to approach a verification target:

\[
\dot m=\varepsilon m(1-m)(G_{\rm target}-G),\qquad\varepsilon>0.
\tag{21}
\]

This manager pursues one measured quantity. It is not spontaneous optimization by society or a representation of plural purposes. It introduces a negative feedback edge absent from the funded-time cooperative system: higher \(G\) reduces \(m\), whereas higher \(m\) raises maintenance input but reduces genuine contractors' retained pay.

For the canonical coefficients, the clean equilibrium is

\[
x=h=1,\quad C=3,\quad G=G_{\rm target},\quad
m_*=G_{\rm target}/6.
\]

It has strict user and contractor margins when

\[
29/31<G_{\rm target}<5.
\tag{22}
\]

The user, contractor, and useful-capacity eigenvalues decouple triangularly from the remaining \((G,m)\) block,

\[
\begin{pmatrix}
-1&6\\
-\varepsilon m_*(1-m_*)&0
\end{pmatrix},
\qquad
z^2+z+6\varepsilon m_*(1-m_*)=0.
\tag{23}
\]

Thus the clean equilibrium remains locally stable for every \(\varepsilon>0\) satisfying (22). At \(\varepsilon=[24m_*(1-m_*)]^{-1}\), its two real decay rates become a complex damped pair. This is a node-to-focus change, not a Hopf bifurcation or loss of local stability.

A finite excursion can still cross a basin boundary. For \(G_{\rm target}=4\), an explicit forward-invariant loss-entry region is

\[
x<1,\quad h\le.1,\quad m\ge.9,
\quad G\le1,\quad C\le108/29.
\tag{24}
\]

Here \(D\le.1<\tau\), so user advantage is at most \(-\tau y_0\); \(h\) decreases, and \(m\) increases because \(G<4\). At the upper \(G\) face, the input is at most \(108/145\simeq.744828<1\), and the upper \(C\) face also points inward. It follows that \(x,C,G\to0\) and \(m\to1\). The share \(h\) can freeze at a small positive value as work disappears.

Consequently numerical entry into (24) certifies operating collapse even though the desired clean equilibrium is locally stable. If a faster controller causes this entry while a slower controller reaches the target from the same initial state, the finding is feedback-induced basin loss through finite overshoot. It should not be presented as a Hopf transition or automatically as the standard form of exogenously forced rate-induced tipping.

## Scope for a broader systems account

The current four-state model already couples two levels: user-level private returns determine participation and receipts, while an institution funded by those receipts alters the opportunities and returns facing later users and contractors. This is more than independent local optimization under fixed effective conditions. But its meta-level rules \(\tau,\lambda,m,\chi\), admissible actions, output accounting, and task family are still fixed parameters. Even the added controller (21) has an externally specified target and update rule.

The common spillover is a modeled consequence, not a distinct dynamically maintained commons stock. Both copying populations respond to scalar private receipts. Multiple legitimate purposes, changing contextual judgments, disagreements about what evidence means, and endogenous goals are not established by calling the resulting feedback a meta-attractor. They require explicit additional state, observation and decision structures, with their normative commitments kept distinct from resource bookkeeping.

The useful systems conclusion is therefore conditional and specific: the same institution can have multiple basins; selection, capacity and verification reinforce each other; a resource or incentive change can move a basin boundary or alter an invasion eigenvalue; and a controller that improves one measured quantity can leave the region that sustains the process generating that quantity. Each of those claims has a different mathematical test.
