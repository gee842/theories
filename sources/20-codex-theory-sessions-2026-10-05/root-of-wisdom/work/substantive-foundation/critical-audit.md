# Constructive audit: from faithful representation to substantive law selection

Prepared 5 October 2026. This is an independent contribution to the current root inquiry, not a claim to have discovered a new law of physics. It builds on the existing consequence-preservation formalization.

## Positive candidate

**Actual couplings and constitutive constraints determine which changes are possible. Stable, closed patterns in those changes support effective laws. A distinction is causally indispensable at a given interface when erasing it changes the responses that interface can produce.**

The advance beyond coordinate covariance is to supply independently warranted constraints that rule out dynamics, then derive what remains. “Everything constrains possibilities” is too weak by itself: the constraints must be stated, tested independently, and strong enough to forbid alternative responses. The mathematically useful bridge is:

\[
\text{constitutive constraints}
\Longrightarrow \text{restricted generator family}
\Longrightarrow \text{response laws and indispensable distinctions}.
\]

This does not require pretending that one can derive actual coupling constants from logic. A law can be strongly selected in form while measurements still determine its parameters. Nor should “the world supplies distinctions” mean all distinctions have equal relevance: couplings, accessible interventions, and interfaces determine what can propagate where.

## A conditional selection theorem, not mere covariance

Consider a ring of \(N\ge5\) sites. Let \(p_i(t)\) be a nonnegative conserved density. Assume its evolution is:

1. linear and autonomous, \(\dot p=Gp\);
2. local to a site and its two nearest neighbors;
3. translation invariant;
4. reflection symmetric;
5. total-density conserving for all initial states;
6. positivity preserving for all nonnegative initial states.

**Theorem.** These requirements force

\[
\boxed{\dot p_i=D(p_{i-1}-2p_i+p_{i+1}),\qquad D\ge0.}
\]

Conversely, every such generator meets the requirements. Thus the law is fixed up to its nonnegative rate. If transport is independently observed, \(D>0\).

**Proof.** Locality and translation invariance give \(\dot p_i=a p_{i-1}+b p_i+c p_{i+1}\). Reflection gives \(a=c\). Conservation gives \(a+b+c=0\), hence \(b=-2a\). Positivity implies \(a,c\ge0\): start with unit density at one neighboring site and zero density at site \(i\), whose initial derivative cannot be negative. Set \(D=a\). Conversely, for \(D\ge0\), the generator is \(D(S+S^{-1}-2I)\), where \(S\) cyclically shifts the density. The exponential is \(e^{-2Dt}e^{Dt(S+S^{-1})}\), whose entries are nonnegative by the power series; its columns sum to one. The symmetry and locality properties are immediate. □

This is a substantive form-selection result. Two arbitrary laws cannot both survive all these constraints. The rate remains empirical; the microscopic explanation of the constraints may be deeper. A continuum diffusion equation follows only with additional smoothness and scaling assumptions; the finite theorem does not need that limit.

Some assumption failures have immediate, distinguishable effects:

| Changed assumption | Permitted alternative |
| --- | --- |
| Reflection symmetry absent | Unequal left and right rates produce directed transport. |
| Nearest-neighbor locality absent | Next-neighbor or long-range jumps change the generator and its response modes. |
| Conservation absent | A decay or growth term is permitted. |
| Positivity absent | Negative diffusion passes the remaining algebra but sends some nonnegative states negative. |
| Translation symmetry absent | Location-dependent conductances produce different local responses. |
| Autonomy absent | Time-dependent rates are permitted. |
| Linearity absent | Nonlinear fluxes can replace linear diffusion. |

The point is not that all reality is diffusion. The point is that a small, physically interpreted set of invariances and constraints can really select a law. This is a completed answer to one version of the previously missing bridge. Calling symmetry alone “the root” would omit the physical domain, positivity, conservation, locality, and composition assumptions doing the work.

This mode of explanation has a strong established analogue in effective field theory. Weinberg's account describes constructing interactions constrained by degrees of freedom, symmetries, quantum principles, and the target scale; finite predictions at a chosen order do not require fixing every possible higher-order term. The broader theory is not inferred from covariance alone. [Steven Weinberg, *On the development of effective field theory*](https://link.springer.com/article/10.1140/epjh/s13129-021-00004-x).

## How a real coupling supplies a consequential distinction

A second result bridges microscopic dynamics, effective laws, and missing possibilities. Consider two coupled dissipative coordinates with an applied input:

\[
\dot x=-kx-gy+u(t),\qquad \dot y=-gx-\kappa y,
\]

where \(\kappa>0\) and, for stable unforced relaxation, \(k\kappa>g^2\). These equations can be generated by the quadratic energy \(V=(kx^2+2gxy+\kappa y^2)/2\) with unit mobility; this is a stipulated physical model, not a universal premise.

Eliminating \(y\) exactly gives

\[
\boxed{
\dot x(t)=-kx(t)+g^2\!\int_0^t e^{-\kappa(t-s)}x(s)\,ds
-g e^{-\kappa t}y_0+u(t).
}
\]

The visible law inherits both history dependence and a term carrying the hidden initial condition. The derivation is the elementary solution of \(\dot y+\kappa y=-gx\), followed by substitution. It requires no statistical assumption.

Two full states with the same visible \(x\) but different \(y\) have initial derivative difference \(-g\Delta y\). Therefore, if \(g\ne0\), merging those states loses an immediately testable distinction for the \(x\)-response. If \(g=0\), \(y\) is irrelevant to the entire \(x\)-trajectory for the same input, and the merge is exact. **The physical coupling, not a preference for a richer vocabulary, decides this difference.**

After a transient, a fast hidden coordinate approximately follows \(y\approx-gx/\kappa\), giving

\[
\dot x\approx-\left(k-\frac{g^2}{\kappa}\right)x+u.
\]

This approximate law is justified quantitatively. Integration by parts gives the exact remainder relative to the displayed approximation:

\[
r(t)=-g e^{-\kappa t}\left(y_0+\frac g\kappa x_0\right)
-\frac{g^2}{\kappa}\int_0^t e^{-\kappa(t-s)}\dot x(s)\,ds.
\]

Hence, whenever \(M_t=\sup_{0\le s\le t}|\dot x(s)|\) is finite,

\[
|r(t)|\le |g|e^{-\kappa t}\left|y_0+\frac g\kappa x_0\right|
+\frac{g^2}{\kappa^2}(1-e^{-\kappa t})M_t.
\]

Thus a state-merging description may be excellent at one time scale and wrong for fast interventions. This yields a concrete discovery rule: vary the preparation or intervention rate; residual dependence on supposedly irrelevant history exposes a lost variable or memory channel. It does not guarantee discovery of variables outside the available interventions.

The exact role of hidden variables, memory, and forcing in reduced equations has established general counterparts in projection methods. The cited recent paper proves generalized Langevin results under explicit operator and evolution assumptions; our finite linear example above is independently derived and makes no claim to all nonlinear systems. [Widder, Zimmer and Schilling, *On the generalized Langevin equation and the Mori projection operator technique*](https://arxiv.org/abs/2503.20457).

## Where stable constraints and self-maintenance help

An entity's ongoing functioning can supply another non-arbitrary consequence interface: the conditions under which it can continue a specified organization. For a declared set \(K\) of functioning states, dynamics and admitted actions determine the viability kernel

\[
K_\infty=\nu Z\,[K\cap\operatorname{Pre}(Z)],
\]

with the quantifiers in \(\operatorname{Pre}\) explicitly fixing control and disturbance assumptions. A distinction that changes membership in this kernel, or changes which action can keep the process there, matters to that functioning. This connects actual causal structure with consequences that a self-maintaining system has practical reason to track.

It does not turn persistence into an ethical criterion. A parasite, harmful institution, or self-replicating program can preserve itself by damaging others. A valuable process can also appropriately end. The earlier reports' provisions for completion, rest, refusal, and exit should remain. Physical viability supplies stakes for specified processes; moral concern asks which stakes deserve weight and why.

## Failure tests that keep the principle substantive

1. **All maps fit.** If the principle accepts every transition table by redefining its constraints afterward, it explains nothing about law selection. State constraints before deriving or testing the response law.
2. **Survival certifies truth.** A stable system may have a biased self-model, or preserve a useful falsehood because omitted costs fall outside its boundary. Viability of the carrier is not accuracy of its representation.
3. **Predictability certifies goodness.** The same faithful model can support care or exploitation. Moral consequence selection requires reasons concerning affected beings; no diffusion or reduction theorem supplies those reasons.
4. **Every hidden degree of freedom is indispensable.** Decoupled or response-equivalent hidden states can be merged. Coupling strength, cancellation, reachable preparations, and scale determine whether a distinction matters to the declared interface.
5. **Apparent closure proves exact closure.** Short passive observations may miss preparation-dependent responses. The coupled-coordinate example constructs that failure.
6. **Selection of effective laws explains the ultimate laws.** Deriving a reduced law from independently supported microscopic dynamics is explanatory progress. It does not explain why those microscopic dynamics hold everywhere. Avoid making success at the first task depend on pretending to have finished the second.

## Recommendation to the main synthesis

Lead with the positive result: **we can now exhibit how physical constraints select a law and how actual couplings select indispensable distinctions.** The invariant description theorem remains the correctness condition for the resulting model. It is downstream of a generative account, rather than a substitute for it.

The compact candidate is: **understand a process through the constraints that generate its possible responses, retaining exactly the distinctions needed for those responses and revising the boundary when interventions reveal dependence beyond it.** This is a strong organizing principle with mathematical realizations and empirical obligations. Treating it as a general root of understanding is a philosophical proposal; the two derivations above are exact conditional results. The next genuinely scientific step is choosing a nontrivial domain, identifying its independently measured constraints, deriving held-out intervention predictions, and comparing credible alternatives. More generic toy examples alone would not establish universality.

## Completed exact verification

`verify_diffusion.py` constructs all 25 entries of an arbitrary five-site generator as independent rational unknowns, then imposes locality, translation, reflection, and column conservation as separate linear equation sets. Exact rational elimination gives rank 24 and a one-dimensional nullspace, generated by the cycle Laplacian. Removing locality, translation, reflection, or conservation gives solution dimensions 2, 5, 2, and 2, respectively. Explicit rational matrices satisfy every other tested property while violating exactly the removed property. A negative diffusion coefficient fails positivity on a point-mass initial state.

Writing \(B p=(p_{i+1}-p_i)_i\), the check verifies exactly that \(L=-B^\top B\). Thus, with conserved mean \(\bar p\),

\[
\frac{d}{dt}\frac12\sum_i(p_i-\bar p)^2
=-D\sum_i(p_{i+1}-p_i)^2.
\]

For \(D>0\), equality holds only for a uniform density. General Fourier modes \(v_i=e^{2\pi\mathrm{i}ji/N}\) have eigenvalues

\[
\lambda_j=D(e^{2\pi\mathrm{i}j/N}+e^{-2\pi\mathrm{i}j/N}-2)
=-4D\sin^2(\pi j/N).
\]

Every nonconstant mode therefore decays exponentially. For \(N=5\), the independently computed exact characteristic polynomial is \(\lambda(\lambda^2+5\lambda+5)^2\) at \(D=1\), agreeing with eigenvalues \(0\) and \((-5\pm\sqrt5)/2\), the latter each twice. These results establish equalization under the stated finite dynamics; they do not assume that all physical processes equalize.

Results are preserved in `diffusion-checks.json`. All exact assertions passed. The symbolic general theorem, the exact five-cycle algebra, and the physical applicability of its assumptions are three separate claims.
