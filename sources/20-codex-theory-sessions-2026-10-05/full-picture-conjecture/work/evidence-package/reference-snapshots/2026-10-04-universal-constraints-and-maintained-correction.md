# Universal constraints on continued becoming and maintained correction

Research continuation begun 4 October and completed 5 October 2026, Asia/Bangkok. Ren clarified that the target is a universal law or invariant useful for human coordination and AI development despite incomplete observability, then asked that findings, insights, and decisions be recorded as research proceeds. This document records the first continuation cycle. The conceptual direction is Ren's; the synthesis, proposed definitions, and mathematical derivations are AI-generated. Three agents developed and audited the results, with separate coordinating-agent calculation checks. This is not independent human peer review.

The strongest current result is a conjunction of constraints: continuing activity must remain supportable; information must permit a timely feasible response; and the mechanisms implementing that response need their own maintained conditions. We derived a tractable example of the last requirement and an exact finite-model account of the second. Their connection to selection and functional innovation is the next mathematical task. Universality remains the target; the exact results below have declared domains of validity.

The [research hub](../../_process/research/2026-10-04-integrated-evolution/README.md), [log](../../_process/research/2026-10-04-integrated-evolution/RESEARCH-LOG.md), and [claim register](../../_process/research/2026-10-04-integrated-evolution/CLAIMS.md) retain the ongoing genealogy. The [first integrated foundation](2026-10-04-selection-and-generative-conditions.md) remains the source for the population and selection–renewal equations.

## The target and the distinction it requires

The foundational target is to discover constraints on how transformation can continue when its enabling conditions can themselves be consumed, damaged, replaced, and regenerated. A universal structural principle could exclude impossible histories or interventions without forecasting every event.

The initial candidate is:

> Ongoing activity that depends on exhaustible enabling functions must retain access to those functions through renewal, substitution, or supported inputs before their loss prevents continuation. Selective success does not by itself establish that this requirement is met.

This concerns a dependency network, not individual self-sufficiency. The relevant support can be supplied by others. Its availability must be assessed across the declared boundary and horizon. A finite project may legitimately consume reserves; an ideal lossless support need not be continually replaced; an activity approaching dormancy can use a finite reserve over an infinite mathematical duration. Such cases constrain how the principle must be stated.

Its empirical content comes from identifying dependencies independently, then predicting what interventions change continuation. Defining “support” retrospectively as whatever accompanied survival would make it circular.

The proposed invariance is a relationship among activities and enabling functions that can survive changes in their carriers. It need not be a conserved scalar. It also need not produce one optimal direction: different viable transformations can remain incomparable. The human commitment to protecting agency, legitimate revision, and future generations supplies an explicit normative specification. Persistence alone does not establish those values.

## A quantitative restriction on every admissible history

For a stock with independently specified compatible units, let

\[
\dot E=R-L,\qquad E\ge E_{\min},
\]

where \(R\) includes replenishment and imports and \(L\) includes use and deterioration. Every trajectory preserving the specified floor must satisfy

\[
\boxed{\int_0^T[L(t)-R(t)]\,dt\le E(0)-E_{\min}}
\tag{1}
\]

at every relevant time \(T\). The proof is integration of the balance. A deficit of at least \(\varepsilon>0\), maintained until the floor is reached, exhausts the margin within \([E(0)-E_{\min}]/\varepsilon\). Long-run average balance alone does not prevent an earlier threshold crossing.

There is a useful network generalization. Suppose protected stocks \(B\) satisfy \(B\ge B_{\min}\). If there is a nonnegative weighting \(y\) and \(\varepsilon>0\) such that every admissible policy at the required activity level satisfies

\[
y^\top\dot B\le-\varepsilon
\tag{2}
\]

throughout the relevant region, no such trajectory can preserve the floors for longer than

\[
\frac{y^\top[B(0)-B_{\min}]}{\varepsilon}.
\tag{3}
\]

This follows by the same integration. The weights certify a shortage; they are not a scalar moral value. Substitution and alternative production routes must be included in the admissible set before (2) can exclude them. A bound proved for one policy cannot establish impossibility for all policies.

These are established balance arguments. Their role in this program is to constrain the mechanistic account of what selection does to its enabling conditions, and to distinguish sufficient resources in principle from a route that can be reached in time.

## An exact invariance of relative success

For pure selection, \(\dot n_i=r_i n_i\), define \(N=\sum_i n_i>0\) and \(p_i=n_i/N\). For any positive differentiable \(a(t)\), the transformation

\[
\widetilde n_i=a(t)n_i,\qquad
\widetilde r_i=r_i+\frac{d}{dt}\log a(t)
\tag{4}
\]

leaves every share and relative growth rate unchanged while replacing \(N\) with \(aN\).

Thus a procedure observing only shares and relative advantages cannot universally certify absolute viability over this model class. For example, two types with constant rates \((1,0)\) have the same share trajectory as types with rates \((-1,-2)\) and the same initial composition; total abundance grows in the first case when the first type is present, and vanishes in the second.

This compares compatible models. It does not assert that adding a common term leaves trajectories unchanged in any fixed ecological model: changed abundance can subsequently alter relative rates, mutation, or transmission. Additional validated assumptions can remove the ambiguity. A success measure incorporating an adequate viability certificate is also outside the impossibility claim.

## Incomplete observation changes what is possible

The relevant question is whether the states compatible with the available evidence admit a common safe continuation. Complete state knowledge is unnecessary when they do.

For a finite model, let \(X\) be states, \(U\) actions, \(K\subseteq X\) protected states, and \(F(x,u)\) the nonempty set of possible successors. Observation is \(h(x)\). Put unavailable actions into an absorbing failure state. Time, reserves, information channels, authority, and pending interventions belong in \(x\) when they affect transitions.

An information set \(B\) contains states consistent with the entire observed history. Its update is

\[
\Phi(B,u,y)=
\left(\bigcup_{x\in B}F(x,u)\right)\cap h^{-1}(y).
\tag{5}
\]

The finite-horizon safe information sets obey

\[
\begin{aligned}
\mathfrak W_0&=\{B:\varnothing\ne B\subseteq K\},\\
\mathfrak W_{\ell}
&=\{B:\varnothing\ne B\subseteq K,\ 
\exists u\in U\
\forall y\text{ with }\Phi(B,u,y)\ne\varnothing,\
\Phi(B,u,y)\in\mathfrak W_{\ell-1}\}.
\end{aligned}
\tag{6}
\]

An observation-based policy guarantees safety for \(\ell\) transitions exactly when \(B\in\mathfrak W_\ell\). The proof is induction: the same observed history requires a common first action; every possible next observation must leave a safe remaining policy. This incorporates ongoing observations and active sensing.

A useful impossibility certificate is simpler. Let \(U^{\rm full}_\ell(x)\) be the first actions allowing safety for \(\ell\) transitions from \(x\), optimistically granting full information thereafter. If

\[
\boxed{\bigcap_{x\in B}U^{\rm full}_\ell(x)=\varnothing,}
\tag{7}
\]

no observation-based policy can guarantee safety. Each physical state can be individually recoverable while their unresolved information set is not. A nonempty intersection is not sufficient: a shared first action can lead to an unresolved later conflict. Equation (6) supplies the full test.

Randomization does not restore a probability-one guarantee for this finite-state, finite-action, finite-horizon safety problem. An action used with positive probability must still be safe for all compatible states to support that guarantee. This does not imply that randomization is useless for other objectives or that failure of a guarantee predicts certain failure.

These are established partial-observation control ideas, with detailed proofs and primary references in the [observability memo](../../_process/research/2026-10-04-integrated-evolution/observability-and-correction.md). Their prospective use here is to represent sensing and intervention availability as conditions that can themselves be maintained or lost.

## The deadline is for a feasible commitment

If every relevant action leaves a net deficit at least \(d_-(t)\ge0\) until effective correction at time \(\tau\), avoiding the support floor requires

\[
\int_0^\tau d_-(t)\,dt\le E_0-E_{\min}.
\tag{8}
\]

This is necessary, not sufficient. A sufficient policy certificate additionally needs adequate information, admissible implementation, bounds on all losses, and safe continuation after correction. Sequential detection, decision, mobilization, and repair times add; overlapping stages require their actual critical path.

The worked counterexample has two indistinguishable faults needing incompatible irreversible repairs. Reserve lasts ten time units; repair takes three; diagnosis identifies the fault at time eight. A timely commitment must occur by seven. Both faults are individually recoverable, but no policy using the available observations can guarantee recovery. The best worst-case success probability is one-half for this two-recipe case.

Diagnosis at seven, one extra unit of the binding reserve, or repair taking two units restores feasibility. Extra funding that changes none of these transitions does not. Completion exactly at the floor is allowed in this example. [Backward-recursion code](../../_process/research/2026-10-04-integrated-evolution/verify_observability.py) and [saved results](../../_process/research/2026-10-04-integrated-evolution/observability-checks.json) make these statements reproducible.

The conceptual consequence is that a loss of actionable information can destroy recoverability before physical support is exhausted. It is equally important to preserve a common safe fallback, where one exists. No universal claim that more surveillance or more information is ethically desirable follows.

## A repair mechanism that must renew itself

The earlier models left an incentive parameter or an authority-rebuilding rate fixed. This cycle endogenizes one part of that support. Let \(E\) be spendable support and \(C\) functional corrective capacity. Both decay. Corrective capacity enables replenishment from declared external feedstock; effort consumes support to renew capacity:

\[
\boxed{
\begin{aligned}
\dot E&=\frac{aC}{1+C/K}-\delta E-uEC,\\
\dot C&=\eta uEC-\mu C.
\end{aligned}}
\tag{9}
\]

All parameters are positive and \(u\) is fixed effort intensity. The same transfer \(uEC\) debits support and, after conversion \(\eta\), credits capacity. No correction capacity appears spontaneously at \(C=0\). The input is an open-system boundary assumption, not energy created from nothing.

The quantity \(V=E+C/\eta\) satisfies

\[
\dot V=\frac{aC}{1+C/K}-\delta E-\frac{\mu}{\eta}C
\le aK-\min(\delta,\mu)V,
\tag{10}
\]

so trajectories remain bounded. This accounting relation is specific to the explicit conversion mechanism.

Write \(m=\mu/\eta\), \(A=a/m\), and \(d=\delta/(uK)\). There are two distinct positive equilibria exactly when

\[
A>(1+\sqrt d)^2.
\tag{11}
\]

They satisfy

\[
E^*=\frac{m}{u},\qquad
C_\pm=\frac K2\left[A-1-d\pm
\sqrt{(A-1-d)^2-4d}\right].
\tag{12}
\]

The lower is a saddle; the upper is locally asymptotically stable; extinction remains locally asymptotically stable. Equality in (11) gives one positive nonhyperbolic equilibrium.

Strictly below the threshold all trajectories converge to extinction. One proof uses

\[
W=E+\frac C\eta+\frac{\delta}{\eta u}\log(C/K).
\]

For \(q=C/K>0\),

\[
\dot W=mK\left[\frac{Aq}{1+q}-q-d\right].
\]

The maximum of the first two bracketed terms over \(q\ge0\) is \([\max(\sqrt A-1,0)]^2\). Below threshold, \(\dot W\) is bounded above by a strictly negative constant. Since \(E+C/\eta\ge0\), this forces \(\log(C/K)\) toward minus infinity at least linearly. Thus \(C\to0\), and \(\dot E\le aC-\delta E\) gives \(E\to0\). The cases \(C=0\) and \(u=0\) follow directly. The equality case is excluded.

Now require a protected support reserve \(E^*>E_{\min}>0\). A locally stable positive equilibrium with that reserve exists precisely when \(A>1\) and

\[
\boxed{
\frac{\delta}{K(\sqrt A-1)^2}
<u<
\frac{\mu}{\eta E_{\min}},
}
\tag{13}
\]

provided the interval is nonempty. Too little fixed effort cannot maintain correction; sufficiently high fixed effort produces a stable positive equilibrium below the protected support floor.

![Support and corrective capacity at stable equilibria](/Users/ren/theories/_process/research/2026-10-04-integrated-evolution/endogenous-renewal-tradeoff.png)

For \(a=9\), \(\delta=\eta=\mu=K=1\), and \(E_{\min}=1\), the interval is \(0.25<u<1\). At \(u=.5\), the stable positive equilibrium is approximately \((E,C)=(2,5.646)\). At \(u=1.5\), it is \((.667,7.241)\): more corrective capacity accompanies insufficient protected support. These are model units and illustrative parameters, not an estimate for institutions.

The [derivation](../../_process/research/2026-10-04-integrated-evolution/endogenous-renewal-math.md) and [reproducible calculation](../../_process/research/2026-10-04-integrated-evolution/verify_endogenous_renewal.py) include equilibrium checks, stability, boundedness, and simulated trajectories. [Recorded numerical checks](../../_process/research/2026-10-04-integrated-evolution/endogenous-renewal-checks.json) have equilibrium residuals below 9e-16 and maximum state changes below 1.5e-9 under tolerance refinement. A separate invariant rectangle certifies collapse from the illustrated depleted start.

Three limits are essential. Existence of a protected equilibrium does not prove safe transient motion or reachability from every initial condition. Fixed \(u\) does not explain who chooses it or why it persists under selection. External feedstock remains a boundary condition whose long-term viability is not established. This result closes one dependency inside the model and exposes the next ones.

## What this adds to the foundational direction

The results separate questions that an aggregate success score can obscure:

1. **Support feasibility:** is there any admissible way to cover indispensable losses?
2. **Dynamic reachability:** can such a regime be reached before binding reserves fail?
3. **Actionable knowledge:** do available observations distinguish incompatible responses in time, or permit a common safe continuation?
4. **Implementation:** can an authorized policy actually deliver the required action?
5. **Renewal and succession:** do the mechanisms providing those capacities continue functioning through loss and replacement?
6. **Selection:** do the rules and practices meeting these conditions persist when competing alternatives can spread?

These are connected tests, not an asserted complete taxonomy. A positive result at one level does not establish the next. The paid-renewal example is especially clear: functioning can persist from one initial state but fail to restart from another, and a stable positive state can still violate a protected floor.

The initial “right gradient” intuition therefore becomes more precise. Universal restrictions may define directions that are infeasible or destroy required capacities, while leaving several permissible directions. They do not select a unique social objective. Continued becoming also needs tests for actual renewal, succession, and useful transformation: safety of a frozen state is not sufficient.

## Existing foundations and what remains to discover

[Chemical Organization Theory](https://arxiv.org/abs/q-bio/0501016) already connects sets of mutually producing components, feasible maintenance, and changing organizations. [Fontana and Buss](https://scholar.harvard.edu/files/walterfontana/files/arrival.pdf) investigated constructive emergence of organizations in addition to selection among existing forms. [Montévil and Mossio](https://montevil.org/publications/articles/2015-mm-organisation-closure-constraints/) analyze mutually maintained constraints. Partial-observation safety and viability theory supply much of the control mathematics. The [prior-art audit](../../_process/research/2026-10-04-integrated-evolution/universality-prior-art-audit.md) records the overlap and counterexamples.

The proposed contribution is to connect selection to the production and loss of these effective conditions, then derive and test intervention restrictions. The next model should make the choice and renewal of effort, sensing, and authority endogenous. It must allow successful correction, capture or neglect, legitimate institutional replacement, and functional substitution. A permanently reliable chooser would leave the main institutional question unresolved.

The next discriminating experiment should separate three causes at matched current performance: lost support, lost actionable information, and lost enforceable authority. Intervene on each independently and test which restores correction before the deadline. A further comparison should distinguish temporary subsidy from a replacement process that can withstand another disturbance after the subsidy ends. No such new empirical experiment was run in this cycle.

## Status at the end of this cycle

The cumulative-balance restriction and selection invariance are exact within their stated classes. Finite-horizon safety under partial observation has an exact recursive characterization. The paid-renewal model has conditional threshold and stability results, independently reviewed and numerically checked. Their cross-domain mappings, empirical usefulness, and originality as an integration remain research questions. The ongoing log preserves both positive results and limits so the north star can guide discovery without predetermining its conclusions.
