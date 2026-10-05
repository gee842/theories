# An exact example of endogenous differentiation

Prepared 5 October 2026. This is an additive audit for the current inquiry, not an edit to either retained theory. It establishes formation and stability of phase domains under supplied dynamics. It does not establish the origin of organisms, experience, the substrate, or cosmological monism.

## Main result

The same deterministic law at every location can support several stable, spatially differentiated states. A partition need not be supplied as a label in the law: interactions and the realized state can determine it. Which symmetry-related state occurs still depends on a supplied perturbation/history. Perfect symmetry remains perfect under a unique symmetric deterministic evolution.

The smallest useful spatial construction here uses four identical sites on a ring. Unlike the previous four-site exchange example, it has no privileged pair partition or different within-pair and between-pair rates. It contains only four equivalent nearest-neighbor edges. Its stable low-energy phase domains emerge from nonlinear dynamics.

## Definitions and assumptions

Let the ring edges be (1,2), (2,3), (3,4), (4,1), and let L be its positive graph Laplacian:

\[
L=\begin{pmatrix}2&-1&0&-1\\-1&2&-1&0\\0&-1&2&-1\\-1&0&-1&2\end{pmatrix}.
\]

The dimensionless order parameter x_i may be positive or negative. It is not asserted to be a nonnegative abundance or a globally bounded concentration. Restrict preparations to \(\sum_i x_i=0\). For a supplied parameter \(\kappa>0\), define

\[
F(x)=\frac14\sum_{i=1}^4(x_i^2-1)^2+\frac\kappa2 x^TLx,
\qquad
\mu_i=\frac{\partial F}{\partial x_i}=x_i^3-x_i+\kappa(Lx)_i,
\qquad
\boxed{\dot x=-L\mu.}
\tag{1}
\]

The local term favors two states. The edge term penalizes unlike neighbors. Conservative movement follows chemical-potential differences. These are substantive supplied mechanisms. The model presupposes spatial sites, adjacency, a scalar order parameter, a constitutive potential, mobility, and initial data. It explains a domain partition within that substrate; it does not derive the substrate from an undifferentiated absolute.

This is a finite graph construction in the phase-field/phase-separation tradition. Cahn and Hilliard's 1958 primary abstract describes a free-energy functional combining a homogeneous-composition term with a gradient term and its use in studying interfaces. Only that abstract was verified for this historical attribution, not the whole paper: [Cahn and Hilliard, 1958](https://doi.org/10.1063/1.1744102). The particular four-site proof below is derived directly here; no historical novelty is claimed.

## Conservation, dissipation, and existence

Since \({\bf1}^TL=0\), the total order parameter is conserved. Further,

\[
\boxed{\dot F=-\mu^TL\mu=-\sum_{\{i,j\}\in E}(\mu_i-\mu_j)^2\le0.}
\tag{2}
\]

The quartic potential makes F coercive. Therefore solutions remain in compact sublevel sets. The polynomial vector field is locally Lipschitz, so each initial state has a unique solution, extending for all forward time. Stationarity requires all chemical potentials equal; it does not require all x_i equal.

## Exact global-minimum theorem

On the zero-mean subspace, the Laplacian eigenvalues are 2, 2, and 4. Put \(r^2=\sum_i x_i^2\). The spectral inequality and Cauchy–Schwarz give

\[
x^TLx\ge2r^2,
\qquad
\sum_i x_i^4\ge\frac{r^4}{4}.
\]

Consequently,

\[
F(x)\ge 1+(\kappa-\tfrac12)r^2+\frac{r^4}{16}.
\tag{3}
\]

If \(\kappa\ge1/2\), the unique minimizer is \(x=0\). If \(0<\kappa<1/2\), the lower bound is minimized at

\[
r^2=4(1-2\kappa),\qquad F_{\min}=1-(1-2\kappa)^2.
\]

Equality in the fourth-power inequality requires every \(|x_i|\) equal. Equality in the spectral inequality requires membership in the eigenvalue-2 eigenspace, whose vectors are \((p,q,-p,-q)\). Joint equality therefore leaves exactly four states:

\[
\boxed{x^*=\sqrt{1-2\kappa}\;\sigma,
\quad \sigma\in\{(+,+,-,-),(-,+,+,-),(-,-,+,+),(+,-,-,+)\}.}
\tag{4}
\]

These are four phase-labeled states and two partitions when the phase labels are ignored. Each state has two connected phase domains and two interface edges. The laws contain no preferred one of these cuts. At \(\kappa=0\), excluded from this theorem's strict low-parameter case, the spectral constraint disappears and all six balanced sign patterns minimize F, including checkerboards. This endpoint matters.

An exact nonnegative remainder helps audit the proof. For \(q=1-2\kappa>0\),

\[
F-(1-q^2)=\frac{(r^2-4q)^2}{16}
+\frac14\left(\sum_i x_i^4-\frac{r^4}{4}\right)
+\frac\kappa2\left(x^TLx-2r^2\right).
\tag{5}
\]

Every term is nonnegative on the zero-mean subspace. The result is a full global-minimum classification, not just a linear instability calculation.

The threshold extends beyond this four-site example. For any finite connected undirected weighted graph with n sites and positive second Laplacian eigenvalue \(\lambda_2\), use the same energy and conservative dynamics on the zero-mean subspace. Then

\[
F\ge\frac n4+\frac{\kappa\lambda_2-1}{2}r^2+\frac{r^4}{4n}.
\]

If \(\kappa\lambda_2\ge1\), the homogeneous state is the unique global minimum. If \(\kappa\lambda_2<1\), a sufficiently small multiple of a \(\lambda_2\)-eigenvector has energy below the homogeneous state's energy. Coercivity ensures a global minimizer exists, so every global minimizer in this regime is nonconstant. The homogeneous state is also linearly unstable. These conclusions do not require a flat sign-valued eigenvector. If the graph does have a balanced vector \(\sigma\in\{-1,+1\}^n\) with \(L\sigma=\lambda_2\sigma\), then simultaneous equality yields the explicit global minimizers \(\sqrt{1-\kappa\lambda_2}\,\sigma\), with all admissible such sign vectors included. The ring supplies a case where that complete classification is elementary. A general nonconstant minimizer is a differentiated pattern; the theorem alone need not give an organism-like boundary or a preferred number of domains.

## Formation and nonlinear saturation

At x=0, the linearized growth rate for a Laplacian eigenmode with eigenvalue \(\lambda\) is

\[
\boxed{g(\lambda)=\lambda(1-\kappa\lambda).}
\tag{6}
\]

The two eigenvalue-2 modes become unstable below \(\kappa=1/2\). In \(1/4<\kappa<1/2\), the alternating eigenvalue-4 mode is linearly damped while those two longer modes grow. No particular orientation is selected by the law.

For any of the four sign patterns \(\sigma\) in (4), the line \(x(t)=a(t)\sigma\) is exactly invariant. Substitution gives

\[
\boxed{\dot a=2a(q-a^2),\qquad q=1-2\kappa.}
\tag{7}
\]

For \(q>0\), \(a(0)\ne0\), and \(s_0=a(0)^2\),

\[
a(t)^2=\frac{q}{1+(q/s_0-1)e^{-4qt}},
\qquad \operatorname{sgn}a(t)=\operatorname{sgn}a(0).
\tag{8}
\]

Thus an arbitrarily small nonzero seed along such a mode grows and saturates at a nonzero differentiated state. For a concrete dimensionless choice, \(\kappa=1/4\) gives \(q=1/2\); taking \(a(0)=1/100\) yields

\[
a(t)=\sqrt{\frac{1/2}{1+4999e^{-2t}}}.
\]

The seed specifies the initial bias; it is not generated from a featureless state by assertion. The exact trajectory demonstrates a possible formation process. It does not establish convergence to a global minimum from every nonzero initial state.

## Stability, persistence, and dissolution

At each state in (4),

\[
\nabla^2F=(2-6\kappa)I+\kappa L.
\]

Restricted to conserved zero-mean perturbations, its eigenvalues are \(2-4\kappa\) twice and \(2-2\kappa\). All are positive for \(0<\kappa<1/2\). The dynamical eigenvalues are \(-4+8\kappa\) twice and \(-8+8\kappa\). These minima are therefore locally asymptotically stable, with open basins within the conserved subspace. Small allowed disturbances relax back: stable persistence is established, although active repair, reproduction, and metabolic self-maintenance are not.

The distinction between global and local minima is material. When \(0<\kappa<1/4\), a checkerboard equilibrium \(\sqrt{1-4\kappa}(+,-,+,-)\) also exists. It is locally asymptotically stable for \(\kappa<1/5\), although not globally minimal. No generic-global-convergence claim is made, and a lower-energy state need not be reached from every preparation.

If the parameter is set to \(\kappa>1/2\), every zero-mean state converges to the homogeneous state. Indeed, with \(r^2=\|x\|^2\),

\[
\tfrac12\frac{d}{dt}r^2
=-x^TLx^{\circ3}+x^TLx-\kappa x^TL^2x
\le -2(2\kappa-1)r^2,
\]

where \(x^TLx^{\circ3}=\sum_E(x_i-x_j)(x_i^3-x_j^3)\ge0\) and \(x^TL^2x\ge2x^TLx\ge4r^2\). Hence

\[
\|x(t)\|\le e^{-2(2\kappa-1)t}\|x(0)\|.
\tag{9}
\]

At the critical value \(\kappa=1/2\), convergence to zero still follows from compactness and the fact that this norm decrease can vanish only when all x_i agree, hence when x=0 on the conserved subspace. The parameter change supplies a specific condition under which a previously stable boundary dissolves; the model does not explain what physically changes that parameter.

## Symmetry lemma: what unity does and does not imply

Let a group act linearly on a state space and let a locally Lipschitz vector field obey \(f(gx)=gf(x)\). If \(gx_0=x_0\), then g applied to the solution is a solution with the same initial state. Uniqueness implies \(gx(t)=x(t)\) for all times of existence. Thus a deterministic symmetric law cannot move an exactly symmetric initial state out of its symmetry class.

The ring equations are equivariant under all ring rotations and reflections, and under \(x\mapsto-x\). The perfectly homogeneous zero-mean preparation x=0 remains there forever even in the unstable regime. In an ensemble with symmetry-invariant noise and initial distribution, the distribution can retain symmetry while individual realizations have differentiated patterns. Noise must itself be specified; it is not part of equation (1).

This distinction is historically explicit in [Turing, 1952, section 4](https://dosequis.colorado.edu/Courses/MethodsLogic/papers/Turing1952.pdf): initially small irregularities matter when a homogeneous state becomes unstable. The primary abstract and section 4 were read for this attribution. Our phase-separation model is not Turing's two-species reaction–diffusion mechanism.

## What counts as the endogenous boundary

For a settled nonzero state in (4), infer phases from the sign of x_i. Connected regions of the same sign are the phase domains; edges across opposite signs are their interfaces. Those relations are read from the evolved state. No pair labels, permanent walls, or different coupling rates are inserted for the two resulting domains.

Their interface is a physical difference in the modeled state, not merely a verbal partition. But mobility across every ring edge remains fixed and positive. A phase interface here is not an impermeable membrane or a proof of subsystem autonomy. At equilibrium the chemical potentials agree and net currents vanish; perturbing one region still changes the larger coupled dynamics. Distinguishing a persistent pattern from a dynamically independent unit is essential.

The explanation supplies a particular chain: local alternatives plus common constraints and interactions make some differences grow; nonlinear saturation stabilizes some of them; the realized stable differences define domains and interfaces. “One common law” does not entail “one uniform state.” “A common process” does not entail “a featureless initial state.”

## Relation to the prior work and next burden

The prior exchange construction justified a pair partition by a supplied separation of coupling rates. This construction derives a phase partition without prespecifying that pair structure. The prior mutually supporting-component model established maintenance through material turnover; that work remains separate. Combining a domain-formation mechanism, a maintained boundary, resource use, locally available information, and action in one model would be further work. No claim is made that placing two separate models side by side already derives an organism or viewpoint.

A useful candidate synthesis is: **differentiated units are stabilized histories of a shared process under actual constraints; their boundaries are outcomes with conditions, rather than exemptions from those conditions.** This is a philosophical interpretation motivated by the conditional constructions. Its application beyond this model needs substantive mechanisms and evidence.

The accompanying exact rational checks target algebra, the global energy remainder, invariant-mode dynamics, symmetry, and endpoints. Their finite coverage supports error detection; the displayed proofs establish the general claims.
