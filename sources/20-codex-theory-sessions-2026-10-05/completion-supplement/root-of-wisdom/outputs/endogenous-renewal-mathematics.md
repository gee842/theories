# Mathematics of endogenous renewal and consequential feedback

Companion to [How renewal and regulation arise within a shared situation](endogenous-renewal-and-consequential-feedback.md), 5 October 2026. These are conditional mathematical results for specified models, not new empirical laws or a claim of priority in dynamical systems or control theory.

## Global formation and renewal theorem

Let \(a,b,k>0\), and consider nonnegative concentrations satisfying

\[
\dot R=kCD-aR,\quad
\dot C=aR-bC,\quad
\dot D=bC-kCD.
\tag{1}
\]

Interpretation: \(R\to C\) is assembly, \(C\to D\) is wear, and \(D+C\to R+C\) is powered renewal. Fixed energetic driving is incorporated into \(k\). This is an ideal kinetic model; a molecular implementation would need explicit species, reverse reactions where relevant, and thermodynamic accounting.

At a zero coordinate its derivative is nonnegative. Also \(R+C+D=M\) is constant. Polynomial local existence, invariance and boundedness therefore give global forward solutions on the nonnegative simplex.

Put \(d_*=b/k\). Then

\[
D(t)-d_*=[D(0)-d_*]\exp\left(-k\int_0^tC(s)\,ds\right).
\tag{2}
\]

Thus \(D\) is monotone toward \(d_*\) without crossing it, and has a limit \(\ell\). Eliminating \(R\) gives

\[
\dot C=a(M-D)-(a+b)C.
\]

The variation-of-constants formula for this stable scalar equation implies

\[
C(t)\longrightarrow \frac{a}{a+b}(M-\ell).
\tag{3}
\]

**Above threshold.** Suppose \(M>d_*\) and \(R(0)+C(0)>0\). Both \(D(0)\) and \(d_*\) are strictly below \(M\); therefore \(\ell\le\max(D(0),d_*)<M\). Equation (3) gives a positive limiting \(C\). If \(\ell\ne d_*\), then \(\dot D=kC(d_*-D)\) tends to a nonzero constant, contradicting the convergence of \(D\). Hence

\[
(R,C,D)\longrightarrow
\left(\frac{b}{a+b}(M-b/k),\frac{a}{a+b}(M-b/k),b/k\right).
\tag{4}
\]

**At or below threshold.** If \(M\le d_*\), then \(D\) increases toward \(\ell\le M\). Were \(\ell<M\), (3) would give positive limiting \(C\), while \(b-k\ell>0\). Then \(\dot D\) would tend to a positive constant, again a contradiction. Thus \(\ell=M\) and \(R,C\to0\), including at equality.

**Formation and inaccessible boundary.** When \(C(0)=0<R(0)\), \(\dot C(0)=aR(0)>0\); machinery forms without an initial machinery seed. When \(R(0)=C(0)=0\), no reaction occurs. Material in the all-degraded state cannot activate itself under this repertoire.

In coordinates \((C,D)\), the positive-equilibrium Jacobian is

\[
J_* = \begin{pmatrix}-(a+b)&-a\\0&-kC_*\end{pmatrix}.
\tag{5}
\]

Its eigenvalues are \(-(a+b)\) and \(-kC_*\). Near threshold from above, \(C_*\to0\), so the slower local return rate tends to zero. This is a model-specific prediction of slow recovery, not a universal diagnostic of collapse.

Near the all-degraded state the linearization on \((R,C)\) is

\[
J_0=\begin{pmatrix}-a&kM\\a&-b\end{pmatrix},\qquad
\lambda_+=\frac{-(a+b)+\sqrt{(a-b)^2+4akM}}2.
\tag{6}
\]

It becomes unstable precisely at \(kM>b\). Rate \(a\) changes the timing but not this threshold because this model has no alternative loss of usable material before assembly.

## A general bound on insufficient renewal

Let \(z(t)\ge0\) be an absolutely continuous vector of enabling capacities. Assume that, for all accessible states and almost every time,

\[
\dot z\le(B-L)z,
\tag{7}
\]

componentwise, where \(B\ge0\) is a fixed production upper bound and \(L=\operatorname{diag}(\delta_i)\) has every \(\delta_i>0\). There is no independent additive production in (7).

If \(\rho(L^{-1}B)<1\), the convergent nonnegative series gives

\[
(L-B)^{-1}=\sum_{n\ge0}(L^{-1}B)^nL^{-1}\ge0.
\]

Set \(w^\top=\mathbf1^\top(L-B)^{-1}>0\). Multiplication of (7) gives

\[
\frac{d}{dt}(w^\top z)\le-\mathbf1^\top z
\le-\frac{w^\top z}{\max_iw_i}.
\tag{8}
\]

Hence all capacities decay exponentially and

\[
\int_0^\infty\mathbf1^\top z(t)\,dt\le w^\top z(0).
\tag{9}
\]

If the production graph is acyclic, \(L^{-1}B\) is permutation-triangular with zero diagonal, hence nilpotent and of spectral radius zero. A productive cycle is therefore necessary for endogenous persistence in this class. Multiple cycles can combine; no statement about each separate cycle's gain follows.

With an independent source \(s(t)\ge0\), replace the right side of (7) by \((B-L)z+s\). The integrated bound gains \(\int_0^T w^\top s(t)\,dt\). Continued external production can therefore maintain a subcritical network. Nondecaying capacities, time-varying rates without uniform bounds, or unbounded superlinear production fall outside the assumptions. A subcritical linearization alone cannot replace the uniform inequality in (7).

For (1), take \(z=(R,C)^\top\),

\[
B=\begin{pmatrix}0&kM\\a&0\end{pmatrix},\qquad
L=\begin{pmatrix}a&0\\0&b\end{pmatrix}.
\]

Since \(D\le M\), (7) holds globally, and \(\rho(L^{-1}B)=\sqrt{kM/b}\). Thus the general theorem proves subcritical decay in the same resource model. The exact nonlinear analysis adds the critical case and supercritical global attraction. Supercritical gain by itself would not establish boundedness or an attractive positive equilibrium in an arbitrary model.

## Energy remains inside the dependency account

For arbitrary nonnegative recycling flux \(J\), the active material \(A=R+C\) satisfies \(\dot A=J-bC\). Suppose a nonnegative work reserve \(E\) supplies the reaction at fixed cost \(\varepsilon>0\) per unit recycled, with \(\dot E=-\varepsilon J\) and no replenishment. Recycling ceases when the reserve is exhausted. Then

\[
\frac{d}{dt}\left(A+\frac E\varepsilon\right)=-bC,
\qquad
b\int_0^TC(t)\,dt\le A(0)+\frac{E(0)}\varepsilon.
\tag{10}
\]

Extending the account to include the energy supply exposes this dependency rather than removing it. The positive fixed regime in (4) assumes maintained driving. This simple work budget is not a complete microscopic thermodynamic model; entropy production and actual chemical free energies require further specification.

## Finite particle survival is a different claim

For fixed finite \(N\) material units in volume \(V\), the corresponding continuous-time Markov chain has propensities

\[
a n_R,\qquad b n_C,\qquad (k/V)n_Cn_D.
\]

The state \((0,0,N)\) is absorbing. Every other state can reach it through a finite sequence of positive-rate reactions: assemble all remaining \(R\), then degrade all \(C\), with no intervening recycling. The finite chain has no other closed communicating class, so absorption occurs almost surely with finite expected absorption time.

The deterministic concentration limit and infinite-time behavior of a finite population are different limits. No lifetime scaling was calculated here. A finite-state graph check confirms reachability for \(N=8\), while the analytic argument covers every finite \(N\). Immigration or a spontaneous powered \(D\to R\) route would alter the absorbing-state premise and requires a different analysis.

## Consequential differences must reach effective correction

This separate local model asks what regulation needs once response pathways are available. Let \(e=(e_1,e_2)\) be signed departures of two indispensable supports from positive reference levels, and \(u\) departures in repair activity. Define

\[
P_+=\frac12\begin{pmatrix}1&1\\1&1\end{pmatrix},\qquad
P_-=\frac12\begin{pmatrix}1&-1\\-1&1\end{pmatrix}.
\]

For \(a,b,\kappa,\gamma>0\) and \(h\ge0\), take

\[
\dot e=ae-bu,\qquad
\dot u=\kappa(P_++hP_-)e-\gamma u.
\tag{11}
\]

Here \(a>0\) means uncorrected departures amplify. The coefficient \(h\) is effective responsiveness to the difference mode, including its routing into action. These parameters are local response coefficients, not the chemical rates in (1).

Writing \(g=b\kappa\), the common and difference modes have characteristic polynomials

\[
\lambda^2+(\gamma-a)\lambda+(g-a\gamma),\qquad
\lambda^2+(\gamma-a)\lambda+(gh-a\gamma).
\]

All modes decay exactly when

\[
\boxed{\gamma>a,\qquad g>a\gamma,\qquad gh>a\gamma.}
\tag{12}
\]

For \(a=1,\gamma=2,g=6\), the common eigenvalues are \((-1\pm i\sqrt{15})/2\). With \(h=0\), the hidden difference eigenvalues are \(1,-2\). With \(h=1/2\), they become \((-1\pm i\sqrt3)/2\), and the whole local system is stable. The independent numerical check forms the full four-dimensional matrix before computing its eigenvalues.

A stronger limitation does not depend on choosing the controller in (11). Consider the exact linear plant

\[
\dot e=aIe-Hu,\qquad y=e_1+e_2,
\tag{13}
\]

with \(a>0\), fixed actuation matrix \(H\), and any deterministic causal controller using only \(y\)'s history, for which the closed-loop dynamics are well posed. Give it the same internal initial state for two plants differing initially by \(\epsilon(1,-1)\). Their identical observation histories produce identical commands, while their difference remains

\[
\delta e(t)=\epsilon e^{at}(1,-1).
\tag{14}
\]

Both trajectories cannot converge to the same reference. No controller with that fixed information and actuation structure can stabilize every nearby initial state. Additional sensing, or probing that changes the plant's observation coupling, can remove the premise of indistinguishability. This result concerns an unstable hidden mode; harmless hidden differences need not be reconstructed for regulation.

Equation (11) supplies the response pathway and does not explain how it formed or how its energetic costs are paid. It gives a stability condition and a failure mechanism, not an allostasis or moral theory. Together with (1), it identifies the next integration problem: endogenous construction and renewal of pathways that reveal destabilizing differences and support a restoring response.

## Verification and source status

The [evidence record](endogenous-renewal-evidence.json) distinguishes analytic proofs, finite arithmetic checks, numerical illustrations, source readings and collaborating-agent review. The mathematical derivations here stand on their stated assumptions. Related primary publications cited in the main report provide context and physical examples, not proof of these exact model equations or of universal 善.
