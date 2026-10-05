# Mathematics of shared generative direction

Companion to [Formalizing a direction toward shared generativity](shared-generative-direction.md), 5 October 2026. The three constructions below address capability comparison, statistical direction, and a shared renewal mechanism. They do not constitute a derived reduction from one model to another.

**Joint capacity and exact inclusion.** Fix a horizon, independently specified functions, required tests, and protected supports. Let \(q\ge0\) be a profile delivered jointly by an implementable protocol. In a linear assay model suppose the exact regions are nonempty bounded polytopes

\[
\mathcal C_- =\{q\ge0:A_-q\le b_-\},
\qquad \mathcal C_+ =\{q\ge0:A_+q\le b_+\}.
\]

Budgets include maintenance, shared resources, time, and the costs of any preceding transformation. A linear description requires executable schedules and valid kinetics. If aggregate constraints omit temporal bottlenecks, their polytope is only a relaxation, not the capacity region.

Inclusion \(\mathcal C_-\subseteq\mathcal C_+\) holds if and only if every new constraint row \(a_i^+\) has a certificate \(z_i\ge0\) satisfying

\[
\boxed{A_-^{\mathsf T}z_i\ge(a_i^+)^{\mathsf T},
\qquad b_-^{\mathsf T}z_i\le b_i^+.}\tag{1}
\]

Sufficiency follows by multiplication: for old feasible \(q\),
\(a_i^+q\le z_i^{\mathsf T}A_-q\le z_i^{\mathsf T}b_-\le b_i^+\).
Conversely, inclusion bounds the maximum of \(a_i^+q\) over the old region by \(b_i^+\). Finite linear-programming strong duality gives a dual optimum with precisely (1). These are standard linear-programming tools applied to the proposed operational object. They do not assert that physical dynamics optimize a capability score. Strict inclusion additionally requires a witness \(q\in\mathcal C_+\setminus\mathcal C_-\).

For

\[
\mathcal C(m,e)=\{q\ge0:q_1+q_2\le m,\ q_1+2q_2\le e\},
\]

the sharp criterion is

\[
\boxed{m_+\ge\min(m_-,e_-),\qquad
e_+\ge\min(2m_-,e_-).}\tag{2}
\]

Indeed the two right sides are the respective maxima of \(q_1+q_2\) and \(q_1+2q_2\) on the old region. The first is attained by \((\min(m_-,e_-),0)\); the second by \((0,\min(m_-,e_-/2))\). Thus \((4,4)\to(3,6)\) gives incomparable regions, witnessed by lost profile \((4,0)\) and gained profile \((0,3)\). The change \((4,4)\to(4,6)\) gives strict inclusion. Equal assay horizons do not erase elapsed time: a common original deadline requires deducting the time used before the later assay.

Inclusion is a partial order on regions. On physical states it is a preorder; quotient by \(w\sim w'\) when their assessed regions agree to obtain a partial order. For regimes ordered in this way, a probability law \(\nu\) stochastically dominates \(\rho\) if \(\nu(U)\ge\rho(U)\) for every upward-closed set \(U\). This defines a stronger comparison than improvement in one chosen scalar. It remains relative to the assay order.

**A conditional stationary direction theorem.** Consider an irreducible continuous-time birth–death chain on ordered levels \(\{0,\ldots,N\}\), with positive rates \(\lambda_n\) from \(n\) to \(n+1\) and \(\mu_n\) from \(n\) to \(n-1\), where the respective adjacent states exist. Interpreting strict improvement in level as strict capacity improvement requires distinct, strictly nested assessed regions. A physical interpretation also requires Markov closure; numbers of different structures alone need not satisfy these requirements.

The finite chain has a unique stationary distribution

\[
\pi_n=\frac1Z\prod_{j=0}^{n-1}\frac{\lambda_j}{\mu_{j+1}},
\qquad \pi_0=1/Z.\tag{3}
\]

Substitution proves adjacent balance \(\pi_n\lambda_n=\pi_{n+1}\mu_{n+1}\); summing incoming and outgoing flows proves stationarity. Standard finite irreducibility gives uniqueness and convergence. In this reduced chain adjacent stationary currents vanish; that does not imply thermodynamic equilibrium of an underlying driven physical system.

Compare two rate sets labeled \(F\) and \(0\). If

\[
\boxed{\frac{\lambda_n^F}{\mu_{n+1}^F}
\ge\frac{\lambda_n^0}{\mu_{n+1}^0}
\quad (0\le n<N),}\tag{4}
\]

then \(r_n=\pi_n^F/\pi_n^0\) is nondecreasing, because its successive ratio is the quotient of the two sides of (4). Moreover \(\sum_n\pi_n^0r_n=1\). For every increasing \(h\),

\[
\begin{aligned}
\mathbb E_Fh-\mathbb E_0h
&=\operatorname{Cov}_{\pi^0}(h,r)\\
&=\frac12\sum_{i,j}\pi_i^0\pi_j^0(h_i-h_j)(r_i-r_j)\ge0.
\end{aligned}\tag{5}
\]

Taking threshold indicators proves stationary stochastic dominance. A strict improvement in at least one ratio makes \(r\) nonconstant and gives strict improvement for \(h(n)=n\). Condition (4) is sufficient for stochastic dominance and characterizes this monotone likelihood-ratio comparison; it is not asserted necessary for every form of stochastic dominance.

Formation need not increase. The exact three-level examples are:

| Case | Formation rates | Loss rates | Stationary probabilities | Mean level |
|---|---|---|---|---|
| Baseline | \((5/2,2)\) | \((1,2)\) | \((1/6,5/12,5/12)\) | \(5/4\) |
| Lower formation and lower loss | \((5/2,7/4)\) | \((1/2,1)\) | \((4,20,35)/59\) | \(90/59\) |
| Lower formation alone | \((5/2,7/4)\) | \((1,2)\) | \((16,40,35)/91\) | \(110/91\) |

The positive case raises the mean by \(65/236\); the negative case lowers it by \(15/364\). These rates are phenomenological assumptions. They have no independently established energy or construction-cost derivation in this example.

Finite-time dominance does not follow. From common initial level 1,

\[
\Pr_F(n_t\ge2)=\tfrac74t+O(t^2),\qquad
\Pr_0(n_t\ge2)=2t+O(t^2).
\tag{6}
\]

The favorable stationary mechanism initially has the smaller probability of level 2. Thus a finite-horizon claim requires a separate calculation. The equilibrium law includes level 0 without conditioning on survivors. Its positive restart rate is supplied. If \(\lambda_0=0\), level 0 is absorbing; with all downward rates positive, the finite chain reaches it almost surely and has limiting law concentrated there.

**A shared renewal mechanism.** Let \(R,C,Y,D,E\ge0\), with fixed material \(M=R+C+Y+D>0\). Set \(g=\eta I/M\), \(0<\eta\le1\), and positive \(a,b,\beta,d,k,\ell,\varepsilon\), with \(\theta\ge0\). Define

\[
J=kED(C+\theta Y),
\]

\[
\begin{aligned}
\dot R&=J-aR-\beta RY,&\dot C&=aR-bC,\\
\dot Y&=Y(\beta R-d),&\dot D&=bC+dY-J,\\
\dot E&=gC-\ell E-\varepsilon J.
\end{aligned}\tag{7}
\]

The nonnegative region is invariant; material is conserved; and \(\dot E\le\eta I-\ell E\) bounds the reserve. Machinery \(C\) captures input with \(gC\le I\). Both forms can contribute to powered recycling when \(\theta>0\), but compete for the same usable material. The exact reduced budget is

\[
\boxed{\frac{d}{dt}[E+\varepsilon(R+C+Y)]
=gC-\ell E-\varepsilon(bC+dY).}\tag{8}
\]

The added form imposes a tracked wear burden. As in the previous report, this is reduced energetic accounting with supplied assembly and catalytic capabilities, not a full molecular realization.

At a resident equilibrium with \(Y=0\), linearizing the \(Y\) equation gives the invasion eigenvalue

\[
\boxed{\lambda_Y=\beta R_*-d.}\tag{9}
\]

Derivatives of that equation with respect to resident coordinates vanish at \(Y=0\), so it forms a triangular block in the full linearization. The all-degraded situation instead has \(\lambda_Y=-d\). Existing renewal can therefore change the sign of the growth exponent of a seeded additional process.

For

\[
M=a=b=k=\ell=\varepsilon=\theta=d=\eta=1,
\quad\beta=4,\quad I=g=73/6,
\]

the resident equilibrium has

\[
R_*=C_*=(1+\sqrt{19/67})/4,
\qquad\lambda_Y=\sqrt{19/67}>0.
\]

It is stable within the resident face but unstable to this additional coordinate. There is also an exact joint equilibrium

\[
\boxed{(R,C,Y,D,E)=(1/4,1/4,1/8,3/8,8/3).}\tag{10}
\]

At that point \(J=3/8\), replacement rates are \(aR=bC=1/4\) and \(\beta RY=dY=1/8\), and captured power \(73/24\) equals reserve loss \(64/24\) plus renewal work \(9/24\).

Eliminating \(D=M-R-C-Y\), the Jacobian in coordinates \((R,C,Y,E)\) is

\[
L=\begin{pmatrix}
-5/2&0&-1&9/64\\
1&-1&0&0\\
1/2&0&0&0\\
1&73/6&0&-73/64
\end{pmatrix}.
\]

Its characteristic polynomial is

\[
\lambda^4+\frac{297}{64}\lambda^3+
\frac{877}{128}\lambda^2+\frac{265}{128}\lambda+\frac{73}{128}.
\]

Writing the coefficients as \(1,A,B,C_0,D_0\), all are positive and

\[
AB-C_0=\frac{243509}{8192}>0,
\]
\[
ABC_0-C_0^2-A^2D_0=\frac{51651371}{1048576}>0.
\]

The quartic Routh–Hurwitz criterion proves local asymptotic stability. Starting near the resident state with a seed \(Y=10^{-4}\), deducted from \(D\), two numerical step sizes approach (10). This is a numerical connecting trajectory; invasion and local stability alone do not prove global convergence.

Equation (9) is independent of \(\theta\): the invader's initial growth does not require a contribution to recycling. Its positive renewal contribution is an assumed chemistry. Also \(Y=0\) is invariant, so a seed or additional formation route is required. The resident machinery falls from about 0.383 to 0.25 in coexistence, and these states need not be ordered by inclusion of their full capability regions. The construction proves one compatible joint renewal regime, without equating diversity, total throughput, or local survival with general capacity expansion.

**Scope of the proposed direction.** For a declared physical class, compare intact shared renewal to a specified feasible alteration, under declared inputs and preparations. The candidate claims an upward shift of the resulting capacity distribution. Equations (1)–(2) give a test of capability ordering; (3)–(6) supply a conditional directional theorem; (7)–(10) supply a mechanism of enabling and coexistence. Deriving favorable transition ratios from physical mechanisms, validating the assay order and Markov closure, and establishing prevalence across actual systems remain separate obligations.

Checks include exact rational arithmetic for 625 inclusion comparisons, all three stationary distributions, material and budget identities, the coexistence equilibrium and characteristic polynomial, and numerical step comparison for the seeded trajectory. They supplement the proofs and do not establish empirical universality. See the [evidence record](shared-generative-direction-evidence.json).
