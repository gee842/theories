# A boundary sustained by the process it protects

Constructed model, 5 October 2026. This supplies an explicit maintenance mechanism beyond a phase-domain interface. It does not derive geometry, chemistry, reproduction, sensing, or experience from monism.

Let c be the abundance of an autocatalytic internal component and b the amount of a barrier around a supplied patch. Precursor and energy availability are held fixed over the modeled interval. Growth from supplied material occurs at per-capita rate r; ordinary loss occurs at rate delta; set A=r-delta>0. The barrier reduces leakage from ell to ell/(1+b), after choosing the unit of b. The internal component produces barrier material from a supplied precursor at rate beta*c. The barrier decays at rate mu*b. Density-dependent internal loss is q*c². All rates are positive:

\[
\dot c=\left[A-\frac{\ell}{1+b}\right]c-qc^2,\qquad
\dot b=\beta c-\mu b.
\tag{B1}
\]

The boundary has a specified causal role, rather than simply a name: its amount changes leakage. Its production depends on the internal process whose continuation it helps. The modeled variables refer to a local patch with assumed potential barrier geometry. Thus boundary function is endogenous, while spatial shape and material mechanisms remain premises.

The nonnegative quadrant is invariant. Since c-dot <= A*c-q*c², c is bounded above by max(c(0),A/q). Consequently b is bounded by max(b(0), beta*max(c(0),A/q)/mu). Positive c remains positive at finite times. No component is generated from c=0, so a seed must be supplied.

Set s=beta/mu and k=q/s. Positive equilibria obey b=s*c and

\[
kb^2-(A-k)b+(\ell-A)=0.
\tag{B2}
\]

If ell>A>k>0 and D=(A+k)²-4k*ell>0, there are two positive equilibria:

\[
b_\pm=\frac{A-k\pm\sqrt D}{2k},\qquad c_\pm=b_\pm/s.
\tag{B3}
\]

The origin is locally asymptotically stable since its Jacobian has eigenvalues A-ell<0 and -mu<0. At a positive equilibrium,

\[
J=\begin{pmatrix}-qc&\ell c/(1+b)^2\\\beta&-\mu\end{pmatrix},
\quad \operatorname{tr}J=-qc-\mu<0,
\quad \det J=\mu s c\left[k-\frac{\ell}{(1+b)^2}\right].
\tag{B4}
\]

Let g(b)=A-ell/(1+b)-kb. Multiplying by 1+b gives -k(b-b_-)(b-b_+). Thus g'(b_-) >0 and g'(b_+)<0. Since the bracket in the determinant is -g'(b), the lower equilibrium is a saddle and the upper equilibrium is locally asymptotically stable. Both a failed state and an operating state therefore exist under the same supplied rates. Large enough coordinated establishment can succeed where sufficiently small seeds decay; no claim that every positive initial condition succeeds is made.

For A=3, ell=15/4, q=beta=mu=1:

\[
(c_-,b_-)=(1/2,1/2),\qquad(c_+,b_+)=(3/2,3/2).
\]

At the upper state, each part supplies a condition needed by the other: maintained barrier limits leakage; internal production replaces degrading barrier. The structure is dependent on resource supply and remains an open process.

Two interventions distinguish this causal loop from a merely drawn boundary:

1. Stop barrier production by setting beta=0. Then b(t)=b(0)e^{-mu*t}. Because A<ell, eventually A-ell/(1+b) is bounded above by a negative number. The resulting differential inequality forces c(t) to zero. Alternatively, forcibly keep b=0; then c-dot <= -(ell-A)c and the core decays immediately.
2. After stopping barrier production, externally hold b=B>ell/A-1. The internal equation becomes logistic with positive growth A-ell/(1+B), so every positive c converges to [A-ell/(1+B)]/q. The outside intervention replaces a failed internal support. Holding this barrier requires a real external maintenance process, omitted by the clamp idealization.

The disruption and rescue establish a conditional causal function for the barrier. They do not imply that every sustained boundary is an organism. Continuous deterministic persistence also omits finite-population extinction.

Numerical trajectories illustrate an operating seed, a failing seed, disrupted maintenance, and external rescue. They are checked at two integration steps and against the analytic fixed points, bounds and intervention results. The general existence and stability conclusions follow from the algebra above, not the numerical trajectories.
