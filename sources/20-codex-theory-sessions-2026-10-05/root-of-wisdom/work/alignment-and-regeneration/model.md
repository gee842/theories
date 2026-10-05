# Reuse and next mechanism: who renews the rules of renewal?

Working audit, 5 October 2026. This memo is a scope correction and next-test specification, not a new empirical result or a claim of mathematical priority.

## Results to reuse

The local report `outputs/regulating-generative-conditions.md` already derives the elementary covariance identity connecting an independently specified generative score with differential continuation. That identity does not explain why renewal would be selected.

The more developed cross-session source `/Users/ren/theories/_process/research/2026-10-05-generative-foundation-review/FOUNDATION-ALTERNATIVE-ORIGINAL.md`, §7.3, supplies that mechanism's first failure cases. Maintainers pay a cost, their share changes under differential returns, and actual maintenance depends on their absolute abundance. Inadequate relative returns cause composition, support, and activity to collapse. Favorable relative returns can establish a regenerative regime while depleted initial states still fail to recover. Repeating a simpler logistic frequency equation with a shared stock would add little.

`/Users/ren/theories/_process/research/2026-10-04-integrated-evolution/selection-of-renewal.md` goes further: rewards are retained shares of actual production, enforcement/claiming has a stated private cost, practice replacement responds to current return, and both production and replacement slow as support vanishes. Too little retention fails to sustain contributors; too much leaves insufficient common renewal. For its illustrative parameters, stable selected equilibria above the declared support floor occur exactly for

\[
\frac{10-\sqrt5}{19}<\phi<\frac35.
\]

This is an equilibrium-feasibility interval, not a guarantee of safe passage from every initial state. The source explicitly says that the allocation rule \(\phi\) remains a parameter; institutional effectiveness and persistence have not been derived. Charging an enforcement fee alone does not demonstrate enforcement capacity.

The same directory contains `continuing-participation-math.md`, `continuing-participation-design-review.md`, and `continuing-participation-prior-art.md`. Search and the inspected design/prior-art passages establish that dynamic refusal, financing, and participant-specific continuation losses already receive attention. Their presence prevents treating “add participant consent” as an unexplored general discovery. The mathematical file itself was not audited in this memo.

## The sharper target

**Explain when a process that maintains shared renewal also maintains affected participants' capacity to question and alter the rules governing that renewal.**

The discriminating comparison holds current output and aggregate persistence equal, while varying whether affected participants retain effective routes to evidence, refusal, repair, and justified rule revision. These are distinct measurements: a right written into a rule does not itself provide the resources, information, or authority required to use it.

The rule-making process should have its own material carriers, operating cost, replacement or succession process, and exposure to differential continuation. A fixed benevolent controller or an unexplained appropriation parameter would leave the central mechanism supplied. Existing work already addresses some pieces; the useful advance is a specified coupling that can be causally separated and tested.

The mechanism can fail in at least three distinguishable ways:

1. A locally successful practice depletes shared productive support.
2. A materially sustainable arrangement deprives some participants of effective agency or recourse.
3. An arrangement initially protects renewal and recourse, but replacement of its rule-making carriers removes those protections.

These are not synonyms. Maintaining shared production does not by itself rule out domination, and preserving an institutional label does not establish continuity of its corrective capacity.

## A bounded analytical extension: selection over retention traits

The existing appropriation model can expose why keeping the rule external matters without relabeling that external rule as endogenous authority. Suppose all carriers contribute, so each produces \(v=B/(h+1)\) per active time. Two inherited, physically embodied retention traits have \(\phi_L<\phi_H\), and \(p\) is the high-retention share. Using the already supplied imitation mechanism and cost law gives

\[
\begin{aligned}
\dot p&=\nu g(E)p(1-p)(\phi_H-\phi_L)(v-\kappa),\\
\dot E&=g(E)v[1-(1-p)\phi_L-p\phi_H]-\delta E,
\qquad g(E)=\frac{E}{L+E}.
\end{aligned}
\]

Here each carrier retains its own fraction of its own stipulated output. Private retained output plus public renewal equals gross output. The enforcement charge remains a private budget cost whose financing requires an application-specific account, as in the predecessor. This extension does not model collective lawmaking, fraud prevention, consent, or authority.

**Proposition.** Assume \(v>\kappa\), \(0\le\phi_L<\phi_H=1\), \(\nu,L,\delta>0\), finite \(E_0>0\), and \(p_0\in(0,1]\). Then \(E(t)\to0\), even if the low-retention resident alone would have maintained a positive support floor. If \(E_0\ge E_{\min}>0\), the trajectory leaves \(E\ge E_{\min}\) after a finite time. For \(p_0\in(0,1)\), replacement halts at a limiting mixture with \(p_\infty<1\) as activity disappears.

**Proof.** The domain \(0\le p\le1,E\ge0\) is invariant. Since \(\dot E\le v-\delta E\), support is bounded; since \(\dot E\ge-\delta E\), it stays positive at every finite time. If \(p_0=1\), \(E=E_0e^{-\delta t}\), proving the claim. Otherwise use active time \(\tau=\int_0^t g(E)\,dt\). If \(\tau\) is finite, the renewal input is nonnegative, bounded by \(v g(E)\), and integrable. Its convolution with the exponentially decaying support kernel tends to zero, so \(E\to0\). If \(\tau\) is infinite, the first equation is a logistic equation in active time with strictly positive coefficient, giving \(p\to1\). Then

\[
\dot E\le E\left[\frac{v(1-p)(1-\phi_L)}L-\delta\right]
\]

is eventually at most \(-\delta E/2\). Since \(g(E)\le E/L\), exponential decay then makes remaining active time finite, contradicting the assumption. Thus total active time is finite. A logistic equation evolved through finite active time leaves \(p_\infty<1\) from an interior initial state. Convergence of support to zero implies departure below any positive floor in finite time. ∎

The failure does not require higher retainers to become literally the entire population. Their cumulative spread can reduce replenishment enough to suppress the activity that would otherwise continue replacement.

### A funded illustration without a simulation

Take \(B=4,h=1\), hence \(v=2\), and set

\[
\phi_L=\tfrac12,\quad \phi_H=1,\quad
c=\tfrac12,\quad \kappa=\tfrac15,\quad
\delta=1,\quad L=\tfrac1{10}.
\]

Every carrier contributes; the two traits differ only in their retained fraction. Their net private returns per active time are

\[
u_L=v\phi_L-c-\kappa\phi_L=\tfrac25,
\qquad
u_H=v\phi_H-c-\kappa\phi_H=\tfrac{13}{10}.
\]

Thus both pay their stated maintenance and retention costs from their retained output, and \(u_H-u_L=9/10>0\). Retention remains physically implementable by stipulation; affording its charge does not derive an enforcement institution.

The pure-low-retention resident has

\[
E_L^*=\frac{v(1-\phi_L)}\delta-L=\frac9{10}.
\]

Its ecological eigenvalue is \(-\delta E_L^*/(L+E_L^*)=-9/10<0\), so support restores small perturbations when composition is fixed. For a declared floor \(E_{\min}=7/10\), it has a strict positive margin. Any introduced high-retention share \(p_0\in(0,1]\), however, eventually drives support below that floor by the proposition. Starting at \(E=9/10\), its immediate support derivative is \(-9p_0/10\). The relative selection coefficient before multiplication by \(\nu g(E)\) is \(9/10\).

This example demonstrates **contributors whose individual success erodes common renewal**. It does not assign permanent moral identities to either trait: the result depends on the technology, allocation, costs, copying rule, and boundary. Lower retention is beneficial to the specified support stock here; nothing in these equations measures agency, suffering, legitimacy, or all effects on other beings.

This is a proved conditional corollary of the predecessor's supplied technology and revision law, not a general law of institutions. It identifies why selecting productive practices under a fixed allocation rule is different from allowing appropriation traits themselves to change. It is a first mechanism result for the new direction; correction and participant recourse remain outside these dynamics.

## Relation to 善 and 恶

The descriptive model should retain its independently specified quantities: production, replacement, support, burdens, access to correction, and participant-level capacities. Calling an increase in a chosen aggregate “good” would conceal the decision about whose capacities count. The user's proposed ethical bridge is best investigated by asking whether a process renews worthwhile possibilities for affected beings, and how those beings can contest the account. This remains an ethical commitment plus a causal investigation; reproduction alone does not entail it.

No new simulation or empirical test was run for this memo. Earlier output files were not edited.
