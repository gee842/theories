# How change can maintain the capacity for further change

Research continuation for Ren, 5 October 2026. This develops the proposed foundation in which interactions produce structures, those structures reshape what can happen next, and some processes maintain that productive capacity. The aim remains a theory of everything. The account below specifies a candidate organizing principle and several conditional consequences; it does not claim to derive the actual laws of the universe from the existence of difference.

**The central proposal is that some products of change become conditions for further change. A process becomes recursively generative when its activity helps renew or transform the capacities that make further production possible.** Its surroundings belong in this account because they supply conditions, receive consequences, and can themselves be changed by the process.

This joins three earlier results: [interactions can select laws and force distinctions](root-of-wisdom-formalization.md), [structures and functional viewpoints can arise within shared dynamics](differentiation-and-viewpoints.md), and [productive continuity can survive material replacement](identity-through-change.md). The new emphasis is on the physically realized possibilities that a situation carries forward.

## What the minimal starting point provides

Difference and change are related but distinct. Two unequal quantities can remain fixed forever. Temporal change involves a difference between situations, together with a relation connecting them. For a dynamical foundation, a more useful minimal starting point is therefore: **there are distinguishable situations and transformations between them.** This is a proposed starting language, not a proof that it is metaphysically irreducible.

The existence of a transformation alone does not entail productive novelty. A two-state system can alternate forever without producing another mechanism. The substantive next premise concerns certain outcomes of transformation: they can participate in, enable, accelerate, block, or redirect later transformations.

A structure then has a causal role that can be investigated. Compare physically admissible preparations with and without that structure, keeping the relevant other conditions matched. If a specified response changes, the structure makes a difference to that response. If an operation becomes achievable within a stated time and resource budget, the structure provides a new effective capacity. An altered probability, an altered rate, and a previously unavailable operation are different results.

## Possibilities belong to a specified situation and dynamics

Let \(z\) describe a joint situation, including the relevant system, surroundings, resources, and retained mechanisms. Let \(L\) specify its dynamics. In a classical stochastic description,

\[
Z_{t+1}\sim K_L(\cdot\mid Z_t=z).
\tag{1}
\]

The kernel gives a conditional distribution of next situations. Repeated application gives a distribution of future trajectories, provided \(z\) retains the state and memory needed for this law. A snapshot that omits consequential memory does not satisfy that condition merely because we call it the present. A deterministic model is included as the special case assigning probability one to its prescribed successor. Equation (1) supplies notation, not the law itself; the form and physical interpretation of \(K_L\) still need justification.

Three meanings of possibility must remain visible:

| Question | Appropriate object |
|---|---|
| Which outcomes can occur under specified conditions? | The allowed outcomes or support of a transition law. |
| How likely are those outcomes? | A probability law, if probabilities are justified. |
| What can this situated system bring about? | Responses achievable through its actual sensing, operations, resources, and time. |

Uncertainty about the present or the law can also produce a distribution of predictions. Such uncertainty does not establish that physical reality itself branches. In a deterministic complete-state model, alternative futures can instead refer to explicitly varied preparations or interventions. For continuous distributions, a possible individual outcome need not have positive point probability.

The wave-function analogy is suggestive, but a quantum wave function contains complex amplitudes and relative phases; its interference behavior is not captured by an ordinary probability distribution. This report uses conditional possibilities without asserting that its notation is quantum mechanics. [IBM Quantum Learning](https://quantum.cloud.ibm.com/learning/en/modules/quantum-mechanics/superposition-with-qiskit).

The earlier other-session work makes the achievable-futures object precise. For a time horizon \(T\), write

\[
\mathcal A_T(z;L)
=\{\operatorname{Law}_L(Y_{0:T}\mid z,\pi):
\pi\in\Pi_T(z)\}.
\tag{2}
\]

Here \(Y\) denotes stated consequences and \(\Pi_T(z)\) contains physically implementable response policies. Information, memory, resources, timing, and the means of execution constrain that set. A mathematical controller with unavailable knowledge or machinery does not count. If a controller actually operates inside the system, its mechanism is part of the larger dynamics; the notation grants no actor outside reality.

Different structures can change both the transition probabilities and the implementable responses. Comparisons require shared outcome meanings and explicit resource and timing conditions. Building a useful structure can consume another resource, so it need not enlarge every aspect of \(\mathcal A_T\).

## A structure can become part of the mechanism

Separate a situation provisionally into ordinary variables \(x\), maintained structures \(c\), and surroundings \(e\). One illustrative deterministic description is

\[
\begin{aligned}
x_{t+1}&=F(x_t,c_t,e_t),\\
c_{t+1}&=G(x_t,c_t,e_t),\\
e_{t+1}&=H(x_t,c_t,e_t).
\end{aligned}
\tag{3}
\]

The first equation says that existing structures help determine what transformations occur. The second says those transformations can produce, replace, or alter the structures. The third includes changes to the surrounding conditions. These are dependent parts of one dynamics.

This captures the proposed feedback:

\[
\text{activity}
\longrightarrow\text{produced structures}
\longrightarrow\text{changed effective capacities}
\longrightarrow\text{further activity}.
\]

The distinctions acquire physical content only when the mechanisms in (3) are specified. Renaming arbitrary variables does not explain generativity. A formation mechanism, a discriminating intervention, and a resource account are stronger evidence than merely observing that something changed.

New effective capacities need not mean that fundamental laws changed. A new arrangement can enable an operation under the same underlying law. The operation may have been possible to construct from the earlier situation while unavailable for immediate use there. Thus novelty is stated relative to an initial repertoire, scale, and feasible horizon. Whether this language can capture genuinely open-ended novelty without a prelisted repertoire remains a further question.

## Maintaining productive capacity requires a physical account

Let \(c(t)\) be a nonnegative amount of a specified productive capacity. Separate its cumulative internal renewal \(R\), external provision \(E\), and loss \(D\):

\[
c(T)=c(0)+R(T)+E(T)-D(T).
\tag{4}
\]

If continuation requires \(c(T)\ge c_{\min}\), and losses satisfy \(D(T)\ge dT\) with \(d>0\), then

\[
\boxed{R(T)+E(T)\ge dT-[c(0)-c_{\min}].}
\tag{5}
\]

This follows directly by rearranging (4). A finite initial reserve cannot cover sustained loss indefinitely. If total external organizational provision is bounded, continued functioning requires unbounded cumulative internal renewal. The result concerns vulnerable capacities satisfying the stated loss condition; durable structures and dormant states with negligible loss need different accounting.

This condition does not make a subsystem independent of its surroundings. Internal rebuilding can depend on continuing external material and energy. Nor does sufficient total provision guarantee correct timing: a necessary repair delivered after collapse may be too late.

The earlier other-session work proves stronger, conditional network results: finite sets of vulnerable supports require recurrent outside provision or renewal cycles upstream of continued activity. A cycle alone does not establish adequate production rates. Its precise assumptions and bounds are retained in that source rather than claimed as new here.

## An existing model gives an exact threshold

The [maintenance investigation](nonseparation-and-selfhood.md) already supplied a simple mechanism. Two capacities, \(x\) and \(y\), produce one another using supplied resources and also disappear:

\[
\dot x=afy-\delta x-cx^2,
\qquad
\dot y=bx-\mu y.
\tag{6}
\]

Here \(a,b,\delta,\mu,c>0\) and the resource condition \(f>0\) is held fixed. The model supplies production laws and resources; it does not derive their physical origin or provide a closed material balance.

Starting with \(x>0,y=0\), we have \(\dot y=bx>0\): an existing capacity produces a second one. Once present, \(y\) contributes the previously inactive production term \(afy\) for \(x\). A product becomes part of the mechanism supporting further production. Disabling either productive link breaks this particular reciprocal support.

A positive maintained equilibrium exists exactly when

\[
\boxed{abf>\delta\mu.}
\tag{7}
\]

Its values are \(x^*=(abf/\mu-\delta)/c\) and \(y^*=(b/\mu)x^*\). The earlier report proves convergence from strictly positive initial conditions using a Lyapunov function. Starting with only \(x>0\) enters that positive region at positive time. These are inherited mathematical results, not newly performed experiments.

The threshold makes the proposal more than a circle drawn between two arrows. Reciprocal production must be strong enough relative to losses. It also separates two claims: a new capacity can appear transiently, yet the combined process may fail to sustain it. The initial creation of a possibility does not ensure its continuing realizability.

## Generativity concerns what a process can keep doing

Three distinctions prevent the proposal from collapsing into a count of futures:

1. **Diversity of outcomes is not productive capacity.** A constructed process can have two equally likely breakdown outcomes while a deterministic renewing process has one reliable continuation. The former has greater outcome entropy; the latter retains the relevant capacity.
2. **Persistence is not renewal.** A perfectly durable inert object can remain unchanged. A productive organization can maintain a similar visible state while repeatedly replacing worn components. Removing the replacement mechanism distinguishes their explanations.
3. **New capacity is not automatically sustainable.** A process can create a useful mechanism while exhausting the means to operate or repair it. The construction and its continuing support require separate accounts.

Under a specified model, one useful quantity is the probability that an actual operating policy preserves stated productive capacities through a finite horizon and completes their required renewal. Optimizing over implementable policies gives an attainable reliability bound; it does not show the system actually implements that policy. Neither quantity alone measures the invention of new kinds of capacity.

It is therefore useful to distinguish **renewing an existing productive organization** from **producing and sustaining a different productive organization**. The first can maintain generativity without continual innovation. The second makes transformation of the organization itself part of what it can do. More novelty at every instant is not required.

## How this approaches life and universal explanation

A candidate organizational criterion suggested by the proposal is:

> A living organization participates in renewing the material capacities through which it continues to act, produce, and respond within its surroundings.

This is a research criterion, not yet a complete biological definition. It requires work on which organization is being tracked, which supports it renews, how dormancy is handled, and how individual, collective, and lineage continuation differ. Having a nonempty future alone cannot establish life: inert remnants also have futures. A finite probability of eventual death also does not establish that a system is presently nonliving.

There is established related work. Montévil and Mossio analyze biological organization through constraints that act on processes and participate in maintaining one another. Their account distinguishes organizational interdependence from thermodynamic isolation. This provides a close predecessor for the renewal part of the proposal, rather than a proof of a universal law. [Montévil and Mossio, 2015](https://montevil.org/publications/articles/2015-mm-organisation-closure-constraints/).

Kolchinsky and Wolpert connect some system–environment correlations to persistence by intervening on those correlations. Their framework is explicitly applicable to living and nonliving systems, so this connection by itself does not classify life. It is relevant to the later question of when records become physically consequential for continuation. [Kolchinsky and Wolpert, 2018](https://arxiv.org/abs/1806.08053).

For the universal project, the candidate root is **the production and renewal of conditions for further transformation**. A universal account must also explain situations where structures are inert, decay, destroy other capacities, or fail to renew themselves. It cannot assume that everything tends toward greater generativity. Likewise, persistence alone establishes neither truth nor ethical value: one process can renew itself while damaging another's conditions of continuation.

The next demanding target is to derive, within one explicit dynamics, the formation of a structure that enables a new operation, the consequences for its surroundings, and the renewal or failure of the capacities needed to keep operating. The current account identifies those linked explanatory requirements. It preserves the ambition of a theory of everything while leaving the actual law and its physical justification as substantive work.

## Evidence and preservation

The [evidence record](generative-becoming-evidence.json) identifies the earlier proofs, the source passages consulted, new derivations, review scope, and preservation checks. The balance bound is an elementary algebraic consequence. The reciprocal-production threshold and convergence proof are inherited from the preserved maintenance report; their earlier exact checks were inspected rather than rerun. No new physical experiment, stochastic simulation, or empirical validation of a theory of life was conducted. This branch edits only its own new report and evidence record. The audit records before and after hashes, including a change detected in one pre-existing file outside these edits.
