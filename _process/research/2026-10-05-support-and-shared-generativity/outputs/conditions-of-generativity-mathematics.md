# Mathematics of supplied conditions and continued renewal

Companion to [Generativity through supporting conditions](conditions-of-generativity.md), 5 October 2026. These results extend the previously constructed renewal model. They are conditional mathematical results rather than fitted biological or planetary laws.

## Model and accounting

For \(a,b,k,\ell,\varepsilon>0\), nonnegative supplied usable power \(P(t)\), and finite nonnegative initial values, set

\[
J=kECD,\quad
\dot R=J-aR,\quad
\dot C=aR-bC,\quad
\dot D=bC-J,\quad
\dot E=P(t)-\ell E-\varepsilon J.
\tag{1}
\]

The material account has \(M=R+C+D>0\) constant. \(E\) is available work, not total conserved energy. Its input presupposes capture and conversion. All coordinate boundary derivatives are nonnegative. For bounded power \(P(t)\le P_{\max}\), comparison gives

\[
E(t)\le\frac{P_{\max}}\ell+
\left(E(0)-\frac{P_{\max}}\ell\right)_+e^{-\ell t}.
\tag{2}
\]

Thus solutions exist for all positive times and remain bounded. Let \(A=R+C\) and \(H=E+\varepsilon A\). Then

\[
\dot H=P(t)-\ell E-\varepsilon bC,
\]

\[
\ell\int_0^TE\,dt+\varepsilon b\int_0^TC\,dt
\le H(0)+\int_0^TP(t)\,dt.
\tag{3}
\]

For bounded operation with existing time averages, integrating the exact identity gives

\[
\overline P=\ell\overline E+\varepsilon b\overline C.
\tag{4}
\]

This is stronger than the activity upper bound \(\varepsilon b\overline C\le\overline P\). It does not make an average supply sufficient for a particular time-dependent regime.

## Equilibria under constant supply

For constant \(P\), the inactive equilibrium is \((R,C,D,E)=(0,0,M,P/\ell)\). At a positive equilibrium,

\[
R_*=\frac ba C_*,\quad E_*D_*=\frac bk,\quad
C_* = q_0(M-D_*),\quad q_0=\frac a{a+b}.
\]

The power equation becomes

\[
P=\frac{\ell b}{kD_*}+\varepsilon bq_0(M-D_*).
\tag{5}
\]

The right side is strictly decreasing in \(D_*\in(0,M]\), taking values from infinity down to

\[
P_c=\frac{\ell b}{kM}.
\tag{6}
\]

Consequently a unique positive equilibrium exists precisely when \(P>P_c\). Set \(A_0=\ell b/k\) and \(B_0=\varepsilon bq_0\). Its \(D_*\) is the positive root of

\[
B_0D_*^2+(P-B_0M)D_*-A_0=0.
\]

The equilibrium machinery amount increases with \(P\), approaching \(q_0M\). To maintain a specified equilibrium level \(0<c<q_0M\), the required constant power is exactly

\[
P(c)=\frac{\ell b}{k(M-c/q_0)}+\varepsilon bc.
\tag{7}
\]

The work cost \(\varepsilon\) affects finite active levels but not the infinitesimal activation threshold: the recycling load tends to zero with \(C\). This feature depends on the chosen kinetics and is not a general statement that construction or activation is free.

## Positive equilibrium stability

Eliminate \(R=M-C-D\). At a positive equilibrium define

\[
\alpha=a+b,\quad p=kE_*C_*>0,\quad q=kD_*C_*>0,
\quad s=p+\ell+\varepsilon q.
\]

The Jacobian in \((C,D,E)\) is

\[
\begin{pmatrix}
-\alpha&-a&0\\
0&-p&-q\\
-\varepsilon b&-\varepsilon p&-\ell-\varepsilon q
\end{pmatrix}.
\]

Its characteristic polynomial is

\[
\lambda^3+(\alpha+s)\lambda^2
+(\alpha s+p\ell)\lambda
+\alpha p\ell+a\varepsilon bq.
\tag{8}
\]

All coefficients are positive, and the remaining cubic Routh–Hurwitz inequality has gap

\[
\begin{aligned}
&(\alpha+s)(\alpha s+p\ell)-(\alpha p\ell+a\varepsilon bq)\\
&=\alpha^2(p+\ell)+\varepsilon q(\alpha^2-ab)
+\alpha s^2+sp\ell>0.
\end{aligned}
\]

Thus the positive equilibrium is locally asymptotically stable. Global attraction above threshold is not established here. The all-degraded material boundary remains invariant even when power exceeds the threshold.

## Global depletion at and below threshold

For constant \(P<P_c\), (2) eventually bounds \(E\) by some constant \(\widehat E<b/(kM)\). Since \(D\le M\), \(z=(R,C)^\top\) then satisfies

\[
\dot z\le\begin{pmatrix}-a&kM\widehat E\\a&-b\end{pmatrix}z.
\]

The comparison matrix has negative trace and positive determinant, so its eigenvalues have negative real parts. Its nonnegative propagator bounds the physical state, proving exponential active-material decay after a finite transient.

At \(P=P_c\), write \(\bar E=b/(kM)\) and

\[
\delta(t)=kM(E(0)-\bar E)_+e^{-\ell t}.
\]

Using \(D=M-A\), one obtains

\[
\dot A\le-\frac bM CA+\delta(t)A.
\tag{9}
\]

Hence \(A(t)\exp[-\int_0^t\delta(s)ds]\) is nonincreasing. Since \(\delta\) is integrable, \(A\) has a limit \(L\). If \(L>0\), the equation \(\dot C=aA-(a+b)C\) gives \(C\to aL/(a+b)>0\). Inequality (9) would then force \(\dot A\) eventually below a negative constant, a contradiction. Thus \(A\to0\).

In both cases, \(R,C\to0\), \(D\to M\), and \(E\to P/\ell\). The result permits initial transient growth and arbitrarily large finite initial reserves. It does not imply finite-time disappearance.

## Equal mean supplied power with different outcomes

Take \(a=b=k=\ell=\varepsilon=M=1\). Constant power \(P=6/5\) has the locally stable active equilibrium

\[
R_*=C_*=\frac{17-\sqrt{249}}{20},\quad
D_*=\frac{\sqrt{249}-7}{10},\quad
E_*=\frac{7+\sqrt{249}}{20}.
\tag{10}
\]

Now let \(P=12/5\) for 30 time units and zero for 30, repeated with period 60. Its mean is still \(6/5\). We prove global active-material depletion under this schedule.

Equation (2) implies that eventually \(E\le2.41\). Start at the next bright interval. This bound remains valid during brightness; in darkness \(\dot E\le-E\), so after four dark units \(E\le2.41e^{-4}\). Since \(D\le1\),

\[
\dot z\le A(E)z,\qquad
A(q)=\begin{pmatrix}-1&q\\1&-1\end{pmatrix}.
\]

Its nonnegative transition matrices allow comparison with a constant upper coefficient \(h=2.41\) over the first 34 units and \(he^{-4}\) over the remaining 26. Each later complete period therefore obeys

\[
z_{n+1}\le Qz_n,\qquad
Q=e^{26A(he^{-4})}e^{34A(h)}.
\tag{11}
\]

Put \(r=\sqrt h\), \(d=re^{-2}\). Direct matrix exponentiation gives

\[
\operatorname{tr}Q=e^{-60}\left[
2\cosh(34r)\cosh(26d)
+\left(\frac rd+\frac dr\right)\sinh(34r)\sinh(26d)
\right].
\]

Since \(\cosh x\le e^x\) and \(\sinh x<e^x/2\) for positive \(x\),

\[
\operatorname{tr}Q<
\left[2+\frac{e^2+e^{-2}}4\right]
\exp[-60+34r+26d]
<0.671<1.
\tag{12}
\]

The numerical margin is not essential to the proof. Elementary rational bounds \(r<1.553\), \(e^{-2}<0.136\), and \(e^2<7.4\) bound the exponent below \(-1.69\) and the prefactor below \(3.884\). The first four terms of the exponential series give \(e^{1.69}>3.884\), proving the product is below one without relying on floating-point precision. The accompanying checker verifies these bounds using rational arithmetic and Taylor remainder estimates.

The matrix \(Q\) has positive entries and positive determinant \(e^{-120}\), hence two positive real eigenvalues. Therefore \(\rho(Q)<\operatorname{tr}Q<1\), and repeated comparison forces \(z_n\to0\) exponentially. Bounded propagation inside a period extends decay to all times.

This proves \(R,C\to0\), \(D\to1\) for every finite initial reserve. Energy approaches the nonzero periodic inactive reserve trajectory; it does not vanish. Continuous concentrations need not hit zero in finite time.

The contrast compares identical average supplied usable power, not merely an effective reaction-rate coefficient. Simulations illustrate it from the same initial state (10), with equal total input over every complete period. Neither time units nor coefficients are fitted to Earth or biology. A different store, wear law, or route out of the all-degraded state can change the outcome.

## Relation to entropy and the larger setting

For an open thermodynamic account, the entropy balance is

\[
\dot S=\dot S_{\rm in}-\dot S_{\rm out}+\sigma,\qquad\sigma\ge0.
\]

If \(S(T)-S(0)\) is sublinear in \(T\) and the relevant averages exist, net entropy export equals internal production on average. The reserve model does not explicitly calculate these fluxes. Its \(P\), losses and work cost must be realized by physical exchanges consistent with that balance. See the primary thermodynamic source in the main report.

## Verification scope

The [evidence record](conditions-of-generativity-evidence.json) records exact arithmetic checks of equilibria, the characteristic polynomial and stability gap; independent period-matrix calculations; the rational contraction certificate; two numerical time steps; visual inspection; and review. The simulations do not substitute for the proofs or establish unproved positive global attraction. Prior theories remain unchanged.
