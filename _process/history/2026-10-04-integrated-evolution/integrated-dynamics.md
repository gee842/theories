# Population change and the renewal of its enabling conditions

Research memo, 4 October 2026. AI-generated mathematical analysis for Ren's proposed integrated theory. This is a candidate foundation, not an established universal theory or a verified originality claim. It separates exact balances, mechanistic assumptions, and conditional results. Only this memo was edited by this agent.

## 1. Start with events rather than a supposed universal objective

The common structure is a population of reproducible or transmissible entities interacting with conditions that influence their persistence and reproduction. It does not require a scalar objective maximized by the whole system. The quantities that spread must be operationally specified: organisms, behavioral variants, organizational practices, deployed AI designs, or allocated activity. People, institutions, and biological cells cannot be interchanged without demonstrating the relevant mechanism and timescale.

Let the state be \(Y=(X,E,S)\): integer type counts \(X_i\), a vector of supporting conditions \(E\), and a vector of selector states \(S\). Selectors include encounter structure, access, evaluators, and decision rights where appropriate. A simple microscopic process has:

| Event | State change | Rate |
|---|---|---|
| Type \(i\) produces type \(j\) | \(X\mapsto X+e_j\) | \(X_i b_i(Y)Q_{ij}(Y)\) |
| Type \(i\) disappears | \(X\mapsto X-e_i\) | \(X_i d_i(Y)\) |
| Existing \(i\) changes to \(j\) | \(X\mapsto X-e_i+e_j\) | \(X_i k_{ij}(Y)\) |

Here \(b_i,d_i,k_{ij}\geq0\), \(Q\) is row stochastic, and \(k_{ii}=0\). Birth with inherited variation is distinguished from learning, switching, or conversion during an entity's lifetime. Simultaneous pair interactions, immigration, recombination, and organizational splitting or merging require additional events.

Between events let \(\dot E=F(Y,u,w)\), \(\dot S=H(Y,u,w)\), where \(u\) represents feasible interventions and \(w\) disturbances. The generator, for a smooth test function \(\phi\), is

\[
\begin{aligned}
\mathcal L\phi={}&F\cdot\nabla_E\phi+H\cdot\nabla_S\phi\\
&+\sum_{ij}X_i b_iQ_{ij}[\phi(X+e_j,E,S)-\phi(Y)]\\
&+\sum_iX_id_i[\phi(X-e_i,E,S)-\phi(Y)]\\
&+\sum_{ij}X_ik_{ij}[\phi(X-e_i+e_j,E,S)-\phi(Y)].
\end{aligned}
\]

This defines a piecewise deterministic Markov process once rates, domains, regularity, and initial conditions are supplied. It is a modeling language, not yet a closed empirical law. A diffusion approximation must derive its covariance from these events; independent, arbitrary noise added to share equations can violate the simplex or obscure extinction.

Under an appropriate density scaling \(X/\Omega\), regularity, and nonexplosion assumptions, a large-population limit yields deterministic abundances \(n_i\):

\[
\boxed{\dot n_i=\sum_jn_jb_jQ_{ji}-n_id_i
 +\sum_j(n_jk_{ji}-n_ik_{ij}),\qquad
\dot E=F(n,E,S,u,w),\qquad
\dot S=H(n,E,S,u,w).}
\tag{1}
\]

These are large-population approximations, not generally exact equations for expected stochastic counts: nonlinear rates create moment-closure terms. The derivation program has strong precedent in [Champagnat, Ferrière and Méléard](https://arxiv.org/abs/math/0510453), who obtain different deterministic and stochastic limits from individual birth, death, and mutation processes. [Bhat's finite-population field theory](https://arxiv.org/abs/2406.10739) is a close contemporary mathematical reference.

Continuous traits replace sums with transition kernels; diffusion requires small local jumps and a smooth trait geometry. Potentially new programs, networks, or biological structures can be represented by a countable or structured state space. A kernel restricted to a fixed catalog cannot explain the arrival of types outside that catalog. Even an unbounded representation does not by itself explain meaningful innovation. [Taylor](https://arxiv.org/abs/1806.01883) distinguishes relevant forms of open-ended innovation. Keeping the kernel and its enabling resources explicit is preferable to labeling any diffusion term “creativity.”

## 2. Exact reductions and the selection–renewal balance

For \(N=\sum_i n_i>0\), \(p_i=n_i/N\), and \(r_i=b_i-d_i\), summing (1) gives

\[
\dot N=N\bar r,
\qquad
\dot p_i=p_i(r_i-\bar r)
+\sum_jp_jb_j(Q_{ji}-\delta_{ji})
+\sum_j(p_jk_{ji}-p_ik_{ij}).
\tag{2}
\]

Without mutation and switching, this is the replicator equation. Its derivation explains why relative advantage and absolute viability differ. [Page and Nowak](https://www.homepages.ucl.ac.uk/~ucackmp/Publications_files/unifying.pdf) connect these deterministic formulations and Price identities; an accounting identity alone does not provide dynamically sufficient closure.

**Result A: exact decomposition of changing regenerative contribution.** Let \(q_i(Y,t)\) be each type's measured net contribution to one support stock per unit abundance, possibly negative. Write

\[
\dot E=R(E,t)+N\bar q,\qquad
\bar q=\sum_i p_iq_i.
\]

Here \(R\) includes separately identified background renewal, losses, and external inputs. Let

\[
(\mathcal Tq)_i=\sum_j(b_iQ_{ij}+k_{ij})(q_j-q_i).
\]

Then the product rule and (2) give

\[
\boxed{\dot{\bar q}
=\operatorname{Cov}_p(q,r)
+\mathbb E_p[\mathcal Tq]
+\mathbb E_p[\dot q_i].}
\tag{3}
\]

The last derivative follows the full changing context along the trajectory, including changes in abundance, environment, selectors, and technologies when \(q_i\) depends on them. For the total population contribution \(J=N\bar q\),

\[
\boxed{\dot J=N\left[
\bar r\bar q+\operatorname{Cov}_p(q,r)
+\mathbb E_p[\mathcal Tq]+\mathbb E_p[\dot q_i]
\right].}
\tag{4}
\]

Thus \(\ddot E=R_E\dot E+R_t+\dot J\) for this scalar representation. Equations (3)–(4) distinguish changes due to selection, transmission or switching, contextual effectiveness, and total scale. They make the central hypothesis measurable without assuming it true: are independently measured regenerative contributions positively or negatively associated with reproductive success, and do the other terms offset that association?

Negative covariance is only a component. It does not prove degeneration: background renewal, technological improvements, switching, or higher total maintenance can compensate. Positive covariance likewise does not establish adequate regeneration, a protected viability floor, or justice. Contributions require causal measurement, not a label assigned after observing success. This is a Price-style identity specialized to a support balance, not a proposed new general theorem.

**Result B: share-only data cannot generally identify viability.** A common addition to all \(r_i\) cancels the instantaneous selective term at the same full state. Entire share trajectories remain equal only under additional conditions, such as relative rates depending solely on \(p,S,t\) and an unchanged selector path. If altering common growth changes the environment and subsequently relative payoffs, trajectory equivalence fails. Mutation tied to birth rates can also break equivalence. Even in the restricted class without those complications, identical \(p(t)\) can accompany population growth or extinction. The explicit model below provides a stronger example: identical improving composition can accompany either recovery or collapse under the same parameters, depending on absolute initial stocks.

## 3. A fully specified example with renewal and degeneration

Consider maintainers \(R\) and nonmaintainers \(D\). These name practices, not fixed kinds of people. Maintainers pay a cost \(c>0\) to sustain a functional stock \(E\). Both depend on that stock. A transfer parameter \(\theta\geq0\) compensates maintainers through the following net growth rates:

\[
r_R=aE-m-\gamma N-c+\theta(1-x),\qquad
r_D=aE-m-\gamma N-\theta x,
\]

where \(x=n_R/N\), all other parameters are positive, and \(N=n_R+n_D\). Transfers balance exactly: \(x\theta(1-x)-(1-x)\theta x=0\). They alter relative incentives, not average resources. The closed system is

\[
\boxed{
\begin{aligned}
\dot x&=x(1-x)(\theta-c),\\
\dot N&=N[aE-m-\gamma N-cx],\\
\dot E&=\rho Nx(1-E/K)-\delta E.
\end{aligned}}
\tag{5}
\]

Production of functional stock depends on the absolute number of maintainers \(Nx\), not merely their share. There is no constant injection of \(E\). Stock saturates, deteriorates, and can be repaired. This is endogenous maintenance within the chosen boundary. It does **not** mean energy or matter is created: throughput and physical inputs must be added for a thermodynamically closed account. The cost \(c\) is a capacity cost, not a stoichiometric derivation. Transfers also need implementation: fixing \(\theta\) isolates one mechanism and does not assume a real institution can enforce it for free or indefinitely.

The region \(0\leq x\leq1,N\geq0,E\geq0\) is invariant. For nonnegative initial data, \(E\leq E_{\max}=\max(E_0,K)\), and \(N\) is bounded above by \(\max(N_0,aE_{\max}/\gamma)\). At \(N=0\), a frequency has no empirical meaning; count variables should be used for extinction claims.

**Result C1: selection against maintenance causes collapse in this model.** If \(\theta<c\), \(N_0>0\), and \(x_0<1\), then

\[
x(t)\longrightarrow0,\quad E(t)\longrightarrow0,\quad N(t)\longrightarrow0.
\]

Proof: the logistic equation for \(x\) implies exponential decay when \(0<x_0<1\); \(x_0=0\) is immediate. Boundedness of \(N\) implies \(Nx\to0\). The inequality \(\dot E\leq\rho N_{\max}x-\delta E\) gives \(E\to0\). Once \(aE<m/2\), \(\dot N\leq-mN/2\), proving extinction. This conclusion uses cost, dependency, and maintenance assumptions that could be empirically false in a given application. It is not a claim that selection generally destroys its environment. The isolated all-maintainer boundary \(x_0=1\) is an exception because this version lacks mutation or invasion.

**Result C2: compensation permits regeneration but does not guarantee rescue.** Suppose \(\theta>c\), so any initially present maintainers approach share one. On \(x=1\), set

\[
M=m+c,\qquad H=\frac{\delta K}{\rho}.
\]

There are two distinct positive equilibria precisely when

\[
\boxed{aK>(\sqrt M+\sqrt{\gamma H})^2.}
\tag{6}
\]

Their coordinates are

\[
N_\pm=\frac{aK-M-\gamma H
\pm\sqrt{(aK-M-\gamma H)^2-4\gamma HM}}{2\gamma},
\qquad E_\pm=\frac{KN_\pm}{H+N_\pm}.
\tag{7}
\]

To derive them, substitute the environmental nullcline \(E=KN/(H+N)\) into the population nullcline \(aE-M-\gamma N=0\). At a positive equilibrium the two-dimensional Jacobian has negative trace and determinant

\[
N(\delta+\rho N/K)
\left[\gamma-\frac{aKH}{(H+N)^2}\right].
\]

The lower equilibrium is a saddle; the upper is locally asymptotically stable. The additional eigenvalue in the three-dimensional system is \(-(\theta-c)\), so the upper equilibrium remains locally stable against small compositional disturbances. Meanwhile \((x,N,E)=(1,0,0)\) has eigenvalues \(-(\theta-c),-M,-\delta\): extinction remains locally stable. Equality in (6) is a nonhyperbolic saddle-node case; the strict claims above do not include it.

This establishes a regenerative basin and a depleted basin under the **same** favorable selection regime. Small shocks within the positive equilibrium's basin recover: a stronger property than unperturbed stationary survival. Larger shocks can cross a basin boundary and fail to recover. We have proved local recovery, not a universal disturbance budget or an exact three-dimensional separatrix.

With \(c=.2,m=.8,\gamma=\rho=\delta=K=1,a=5\), the equilibria have \(N_\pm=(3\pm\sqrt5)/2\), approximately \(.382,2.618\), and \(E_\pm\approx.276,.724\). Use \(\theta=.1\) versus \(.4\) to compare degenerative and regenerative selection. Under \(\theta=.4\), neighborhoods of both the positive equilibrium and extinction can use the same \(x_0<1\) sufficiently close to one. Their entire \(x(t)\) trajectories are identical, yet one restores maintained stock and the other collapses. This proves the share-only nonidentifiability claim within a closed model.

The structural precedent is ecological public goods, positive density dependence, and evolution toward extinction. [Tilman, Plotkin and Akçay](https://pmc.ncbi.nlm.nih.gov/articles/PMC7021758/) already analyze broad classes of strategy–environment feedback and regime changes. [Gyllenberg and Parvinen's 2001 paper](https://researchportal.helsinki.fi/en/publications/necessary-and-sufficient-conditions-for-evolutionary-suicide) is a relevant evolutionary-extinction reference; its existence and bibliographic details were verified here, not all of its theorem assumptions. Equation (5)'s originality has not been established.

## 4. What this does and does not ground

The strongest shared claim is conditional: the same measured relationship among costly maintenance, private advantage, shared dependence, and finite regeneration can produce analogous dynamics in different domains. A biological example might concern production of a shared support factor; a human example might concern maintenance of an infrastructure or knowledge commons; an AI example might concern investment in evaluation or shared training-data quality. Each mapping needs separately estimated rates and intervention tests. Cancer requires a particular cell, host, and environmental model; there is no universal cancer attractor here.

Equation (5) is a diagnostic model of a maintenance failure. It lacks spatial structure, turnover of selectors, heterogeneous beneficiaries, repair technologies, and new types. Endogenizing \(\theta\) through \(\dot S=H\) is the next module, including the resources and authority required for enforcement and the effects of success on those resources. It should not be given a favorable sign by definition. A cooperative countercase must remain possible: cheap maintenance, private returns to maintenance, reliable transfers, background renewal, or innovations that remove the dependency can all change the conclusion.

生生 can motivate investigating maintained capacities, recovery, and the creation of further possibilities. A single positive stock, stable equilibrium, or rising diversity index is not its complete mathematical equivalent. Openness to innovation, ecological viability, human standing, and legitimate revisability are distinct observables or constraints, potentially in tension. No moral ordering or universal ascent gradient follows from (1)–(7).

Coarse-graining is a substantive obligation. Aggregating entities into types preserves (1) only when conditional rates can be represented at that level, or when closure errors are measured. Aggregating over resources may hide the binding constraint. Mutation and learning can change labels without reproducing entities; adoption shares, wealth shares, and counts require different event mechanisms. The most useful next evidence is therefore simultaneous observation of absolute activity, composition, support stocks, maintenance flows, selector changes, and recovery after perturbation—not another fit to relative success alone.
