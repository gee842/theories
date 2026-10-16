# Mathematics of renewing access to support

Companion to [Renewing access to supporting conditions](renewing-access-to-support.md), 5 October 2026. These are results for a constructed deterministic model. They do not establish a universal direction of reality or a complete molecular thermodynamics.

**Model and domain.** Let \(a,b,k,\ell,\varepsilon,M>0\), \(I\ge0\), \(0<\eta\le1\), and \(g=\eta I/M\). For nonnegative \(R,C,D,E\) with \(R+C+D=M\), define

\[
J=kECD,
\quad \dot R=J-aR,
\quad \dot C=aR-bC,
\quad \dot D=bC-J,
\quad \dot E=gC-\ell E-\varepsilon J.
\tag{1}
\]

At each zero coordinate its derivative is nonnegative. Material is conserved, and

\[
0\le gC\le \eta I\le I,
\qquad \dot E\le\eta I-\ell E.
\]

Consequently the nonnegative material simplex is invariant, energy remains bounded by \(\max\{E(0),\eta I/\ell\}\), and solutions exist for all nonnegative time. Captured input depends on current machinery; its maximum remains limited by incident support.

The exact budget for \(H=E+\varepsilon(R+C)\) is

\[
\boxed{\dot H=(g-\varepsilon b)C-\ell E.}\tag{2}
\]

This accounts for reserve loss, recycling work, and conversion of active material into degraded material. The model treats \(R\) as already usable for assembly. Equation (2) is a reduced work-equivalent budget; it is not an independent derivation of chemical free energies, heat flows, or entropy production.

**Positive equilibrium fold.** Write

\[
s=\frac{a+b}{a},\qquad v=g-\varepsilon b.
\]

At a positive equilibrium \(J_*=bC_*\), so

\[
R_*=(b/a)C_*,\quad D_*=M-sC_*,\quad
E_*=(v/\ell)C_*,\quad kE_*D_*=b.
\]

It follows that \(v>0\) and

\[
C_*(M-sC_*)=\frac{\ell b}{kv}.
\]

The left side is a concave quadratic, with maximum \(M^2/(4s)\) on the admissible interval \(0<C_*<M/s\). Thus the fold occurs at

\[
\boxed{g_f=\varepsilon b+\frac{4s\ell b}{kM^2}.}\tag{3}
\]

For \(g>g_f\) there are two positive equilibria with

\[
C_\pm=\frac{M\pm\sqrt{M^2-4s\ell b/(kv)}}{2s}.\tag{4}
\]

At equality they merge; below it there is no positive equilibrium. This statement concerns equilibria. It does not exclude every possible nonstationary active attractor below the fold.

**Local stability.** At the inactive equilibrium \((R,C,D,E)=(0,0,M,0)\), use coordinates \((R,C,E)\). The Jacobian is lower triangular with diagonal \((-a,-b,-\ell)\). Thus inactivity is locally asymptotically stable for every finite \(g\).

At a positive equilibrium use coordinates \((C,D,E)\), eliminating \(R=M-C-D\). Put

\[
\alpha=a+b,\quad p=kE_*C_*>0,\quad q=kD_*C_*>0,
\quad u=p+\ell+\varepsilon q.
\]

The Jacobian and characteristic polynomial are

\[
L=\begin{pmatrix}
-\alpha&-a&0\\
0&-p&-q\\
v&-\varepsilon p&-\ell-\varepsilon q
\end{pmatrix},
\]

\[
\det(\lambda I-L)=\lambda^3+(\alpha+u)\lambda^2+
(\alpha u+p\ell)\lambda+\alpha p\ell-avq.
\tag{5}
\]

The constant term simplifies to

\[
\alpha p\ell-avq=akvC_*(2sC_*-M).
\]

On the lower branch it is negative. Descartes' sign rule gives exactly one positive real root. The remaining roots have negative real parts: after factoring the positive root \(r\), the remaining quadratic has positive constant \(-[\alpha p\ell-avq]/r\) and positive linear coefficient \(\alpha+u+r\). Thus the lower branch is a saddle.

On the upper branch all coefficients are positive, and the Routh–Hurwitz gap is

\[
(\alpha+u)(\alpha u+p\ell)-(\alpha p\ell-avq)
=\alpha^2u+\alpha u^2+up\ell+avq>0.
\]

The upper branch is locally asymptotically stable. At the fold there is one zero eigenvalue and two with negative real parts. For \(g>g_f\), the inactive and upper active equilibria therefore coexist as locally asymptotically stable states. The proof neither identifies their complete basins nor makes \(C_-\) a scalar activation threshold for all preparations.

**Formation and a certified failure region.** If \(C(0)=E(0)=0<R(0)\), then

\[
\dot C(0)=aR(0)>0,\qquad \ddot E(0)=gaR(0).
\]

For \(g>0\), machinery formation therefore precedes energy accumulation. This local statement does not itself prove successful long-term renewal.

Let \(A=R+C\) and choose \(r>0\) satisfying

\[
\frac{gr}{\ell}<\frac{b}{kM}.
\]

The region

\[
A\le r,\qquad E\le\frac{gr}{\ell}\tag{6}
\]

is invariant. On its energy boundary,
\(\dot E\le gr-\ell E=0\). Throughout it,

\[
\dot A=C(kED-b)\le-\delta C,
\qquad \delta=b-\frac{kgMr}{\ell}>0.
\tag{7}
\]

Thus \(\int_0^\infty C(t)\,dt<\infty\). Bounded derivatives make \(C\) uniformly continuous, hence \(C\to0\). Also \(A\) decreases to a limit \(A_\infty\), so \(R=A-C\to A_\infty\). If \(A_\infty>0\), then \(\dot C=aR-bC\) is eventually bounded below by a positive constant, contradicting \(C\to0\). Therefore \(R\to0\). Finally \(\dot E\le gC-\ell E\) and \(E\ge0\) imply \(E\to0\). Material conservation gives \(D\to M\).

For unit \(a,b,k,\ell,\varepsilon,M,\eta\) and \(I=g=17\), the fold is 9 and

\[
C_\pm=R_\pm=\frac{1\pm1/\sqrt2}{4},\quad
D_\pm=1-2C_\pm,\quad E_\pm=16C_\pm.
\]

The upper equilibrium is approximately \((0.4267766953,0.4267766953,0.1464466094,6.8284271247)\). Taking \(r=0.01\) proves collapse from \((0.01,0,0.99,0)\), since \(E\le0.17\) and \(\dot A\le-0.83C\). The trajectory from \((1,0,0,0)\) approaches the upper equilibrium numerically. Its basin entry is a numerical illustration, not an analytic conclusion of the stability theorem.

**Restartability depends on the repertoire.** Equation (1) directly makes \(R=C=0\) invariant, for any nonnegative initial energy and incident support. Consequently increased light alone cannot restore these variables from complete absence. In chemical reaction networks the analogous structural criterion is a siphon: every reaction producing a species in the set requires a species in it as a reactant. Under mass-action kinetics its empty face is invariant. This standard result is recorded in [Shiu and Sturmfels, Proposition 2.1](https://people.tamu.edu/~annejls/SiphonsInCRNs.pdf). Adding an independent production route removes the premise. We do not claim a new general network theorem or identify the energy coordinate literally with a chemical species.

**Exact functional succession.** Replace \(C\) by \(X+Y\), with

\[
\begin{aligned}
J&=kED(X+Y),&\dot R&=J-aR,\\
\dot X&=-bX,&\dot Y&=aR-bY,\\
\dot D&=b(X+Y)-J,&\dot E&=g(X+Y)-\ell E-\varepsilon J.
\end{aligned}\tag{8}
\]

Then \(C=X+Y\) obeys equation (1) exactly and \(R+X+Y+D=M\). Initialize its aggregate at the upper equilibrium, with \(X(0)=C_*\) and \(Y(0)=0\). The exact solution is

\[
X(t)=C_*e^{-bt},\qquad Y(t)=C_*(1-e^{-bt}),\tag{9}
\]

while \(R,D,E,C\), captured power \(gC\), and renewal flux \(bC\) stay constant.

To distinguish the two forms operationally, add a catalytic channel available only to \(Y\):

\[
S+Y\longrightarrow T+Y,\qquad
\dot S=-hYS,\qquad \dot T=hYS,\qquad h>0.
\]

For \(S(0)=S_0>0\),

\[
S(t)=S_0\exp\!\left[-hC_*\left(t-\frac{1-e^{-bt}}b\right)\right],
\qquad T(t)=T_0+S_0-S(t).\tag{10}
\]

The new flux is zero initially and positive at every finite \(t>0\). Its total conversion is bounded by \(S_0\); as \(S\to0\), the flux vanishes. Assume this conversion is downhill and releases its available energy as heat. Tracking a supplied work-potential \(q_0S\), with \(q_0>0\), gives the optional reduced budget

\[
\frac{d}{dt}[E+\varepsilon(R+X+Y)+q_0S]
=(g-\varepsilon b)(X+Y)-\ell E-q_0hYS.
\]

The successor route, extra catalytic ability, equal formation and maintenance costs, and absence of interference between functions are model assumptions. The construction proves continued renewal with a newly active transformation within a supplied repertoire. It does not derive new chemistry, unlimited innovation, or increased total generativity of the wider environment.

**Verification scope.** The accompanying checks use exact rational arithmetic for 486 equilibrium and characteristic-polynomial cases, including both branches. They verify the budget identity and fold relation, compare numerical trajectories at two step sizes, check material conservation and nonnegativity, and substitute the succession solution into its vector field. General conclusions rest on the written arguments above. The checks are reproducibility support, not external scientific validation. See the [evidence record](renewing-access-to-support-evidence.json).
