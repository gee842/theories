# Causal formalisms, embedded observers, and representation limits

Research memo, 5 October 2026. Prepared for the dedicated causal-foundations investigation. This is a scoped technical contribution, not an independent final synthesis or claim of novelty. The existing integrated-evolution README and claim register were consulted read-only. No files there were changed.

## Principal findings

1. Including observers, controllers, evaluative variables, and their update processes inside a causal model is mathematically straightforward in many classical dynamical model classes. It does not establish universal physical closure, identify the true model, or justify the model's ethical criteria.
2. A DAG represents one useful causal model class. Feedback between recurring components is compatible with a time-indexed DAG when effects follow a well-founded event ordering. Cyclic equilibrium models and continuous-time dynamics require their own solvability and intervention assumptions.
3. A physical procedure that changes a variable is not automatically the ideal intervention that changes only that variable's assignment mechanism. Its side effects, selection rule, information, resources, and duration matter.
4. Representation-invariant claims require an explicit equivalence or abstraction relation. Matching ordinary observations is too weak; matching all intervention distributions still need not preserve individual counterfactuals.
5. The most useful restricted foundation is an obligation to account for the realization and limitations of observation and revision. If the only content is that all change is some larger state transition, it imposes no discriminating empirical constraint.

## Primary-source precedents and precise scope

The summaries in this section are deliberately short. All links are primary papers, their author copies, or proceedings. Later elementary examples and propositions are worked derivations for this memo, rather than claims of newly discovered mathematics.

**P1 — Pearl, 2009, *Causal inference in statistics: An overview*.** Sections 3.2–3.2.1, printed pp. 107–109, formulate autonomous structural assignments and intervention by equation replacement. Section 3.4, Definition 4 and equation (27), printed p. 120 (PDF p. 25), defines a unit counterfactual by solving the modified model while holding the background context fixed. This supplies semantics conditional on a structural model; it is not a derivation of a physical intervention from observational covariance. The paper explicitly separates causal assumptions from statistical information. [Author PDF](https://web.cs.ucla.edu/~kaoru/SS-2009-57-Sup.pdf), [DOI](https://doi.org/10.1214/09-SS057).

**P2 — Bongers, Forré, Peters, and Mooij, 2021, *Foundations of Structural Causal Models with Cycles and Latent Variables*.** The published article is *Annals of Statistics* 49(5), 2885–2915. In the checked extended author version, §3 treats solvability, §4 distinguishes observational/interventional/counterfactual equivalence, and §8 defines simple SCMs. Definition 8.1, PDF p. 25, requires unique solvability with respect to every subset of endogenous variables. Proposition 8.2 establishes closure under marginalization, perfect intervention, and the twin construction; Corollary 8.3 gives unique distributions and the general directed Markov property. Standard directed/d-separation properties require additional conditions specified there. Arbitrary cyclic SCMs lack these guarantees. The source's §4 Proposition 4.6 orders the equivalence notions without equating them. [Extended author PDF](https://arxiv.org/pdf/1611.06221), [published PDF](https://staff.fnwi.uva.nl/j.m.mooij/articles/21-AOS2064.pdf), [DOI](https://doi.org/10.1214/21-AOS2064). Numbering above is for the checked 75-page extended PDF, not asserted to match the 31-page published layout.

**P3 — Mooij, Janzing, and Schölkopf, 2013, *From Ordinary Differential Equations to Structural Causal Models: the deterministic case*.** Section 2.2, PDF pp. 2–3, models clamping through added negative-feedback terms and an ideal infinite-gain limit; the physical controller can thus be added to the system. Section 2.3 defines strong global equilibrium stability and discusses weaker domains. Theorem 2, PDF p. 7, connects intervened ODE equilibria and SCM solutions under explicit structural-stability assumptions. These are conditional equilibrium results, not a claim that every ODE is adequately represented by a static SCM. [Paper](https://arxiv.org/pdf/1304.7920).

**P4 — Sokol and Hansen, 2014, *Causal interpretation of stochastic differential equations*.** Definition 2.4, checked preprint pp. 8–9, defines an intervention by substituting a coordinate function into the remaining SDE. Section 4 relates this construction to Euler-scheme structural models and makes clear that the driving noise is assumed not to be directly changed. Example 4.6, pp. 15–16, shows why algebraically related stochastic descriptions can yield inappropriate intervention interpretations. Theorem 5.3, p. 18, identifies postintervention distributions from the generator under its Lévy-noise, Lipschitz, and initial-law conditions. Identification from a generator is not automatically identification from arbitrary finite observational data. [Paper](https://arxiv.org/pdf/1304.0217).

**P5 — Rubenstein et al., 2017, *Causal Consistency of Structural Equation Models*.** Definition 3, PDF p. 4, requires a surjective, order-preserving intervention map and equality between pushed-forward low-level interventional distributions and high-level distributions. Lemma 5 establishes composition; Theorem 6 formalizes causal consistency. Their SEM definition explicitly names allowed interventions and assumes unique solutions for them. The framework treats marginalization, aggregation, and dynamical-to-equilibrium descriptions together. It does not say arbitrary aggregation is valid. [Paper](https://arxiv.org/pdf/1707.00819).

**P6 — Beckers and Halpern, 2019, *Abstracting Causal Models*.** Example 3.4 and Definition 3.5, PDF p. 4, show why a favorable distribution and very weak intervention set can make exact transformation too permissive. Definition 3.7/Theorem 3.8, PDF p. 5, use a shared context map for all interventions. Definitions 3.12–3.14, PDF pp. 5–6, constrain the intervention map using the state map and define stronger abstraction. The distinctions directly answer what must be fixed before a representation-invariance claim has content. [Author PDF](https://www.cs.cornell.edu/home/halpern/papers/abstraction.pdf), [proceedings/DOI](https://doi.org/10.1609/aaai.v33i01.33012678).

**P7 — Beckers, Eberhardt, and Halpern, UAI 2019 / proceedings 2020, *Approximate Causal Abstractions*.** The paper extends exact abstraction by comparing discrepancies between intervention predictions, using a specified metric. Section 3 and Propositions 3.3–3.4 connect zero-error cases to exact abstraction. Choice of metric and which errors count are application-dependent. An approximate macro description can therefore be justified without identifying every microscopic change as a mechanism change. [Proceedings](https://proceedings.mlr.press/v115/beckers20a.html), [open full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC6779476/).

**P8 — Dawid, 2021, *Decision-theoretic foundations for statistical causality*.** Section 2, checked preprint pp. 3–4, represents observational and interventional regimes using a non-stochastic regime indicator and treats transfer between them as a substantive stability assumption. Sections 7–9 develop conditions related to ignorability. This provides a primary precedent for causal decision analysis that does not make a joint distribution over all individual counterfactuals its primitive requirement. A regime label indexes questions; it need not be a literally uncaused physical object. [Paper](https://arxiv.org/pdf/2004.12493).

**P9 — Mishra, Fox, and Wooldridge, 2024, *Characterising Interventions in Causal Games*.** The abstract and opening sections explain why agents' knowledge of an intervention and whether policies are selected before or after it matter to the query. Their framework explicitly has decision and utility variables. The limited lesson here is that adapting a policy to an intervention and holding the policy fixed are different causal comparisons. The paper does not establish that utilities are morally legitimate. [Paper](https://arxiv.org/pdf/2406.09318).

**P10 — Oreshkov, Costa, and Brukner, 2012, *Quantum correlations with no causal order*.** The paper's process-matrix framework assumes local quantum operations without assuming a predefined global ordering and constructs correlations inconsistent with definite-order constraints. This is a mathematical warning against assuming a single classical DAG formalism is forced by the concept of causality. It is not a proof that ordinary institutional feedback lacks temporal order, a proof that our whole universe violates causal order, or an empirical refutation of every refined event DAG. [Primary publication](https://www.nature.com/articles/ncomms2076).

## A modest formal embedding

For a finite discrete-time model, let the physical state be

\[
Z_t=(W_t,C_t,R_t),\qquad C_t=(M_t,\Theta_t,G_t).
\]

Here \(W_t\) is the surrounding modeled world, \(M_t\) is a memory/model realization, \(\Theta_t\) is a controller configuration, \(G_t\) is a realized evaluative configuration, and \(R_t\) is a resource state. The functional roles do not require disjoint neural or institutional substrates; the decomposition is an analyst's chosen representation and must be justified for its use. A concrete construction with explicit within-step order is

\[
O_t=h(Z_t,N_t),\qquad
A_t=\pi(M_t,\Theta_t,G_t,O_t,V_t),
\]
\[
Z_{t+1}=F(Z_t,O_t,A_t,E_t).
\]

Noise variables need not be independent unless the model assumes it; shared causes can be represented explicitly. The observation available to this agent is \(O_t\), not \(Z_t\). A description of consequences encoded by \(M_t\) and an action-selection rule realized by \(\Theta_t\) remain different roles even when one physical process implements both. Institutional realizations may distribute these roles over people, records, procedures, and software.

This representation already permits observations to alter the model, controller, goals, resources, or environment. It makes no promise that an update improves anything: improvement requires a criterion, and adoption of a criterion is a separate process from its justification.

**Time-indexing proposition.** For a finite horizon, if each assignment uses only earlier times or an acyclic within-time ordering such as \(Z_t\prec O_t\prec A_t\prec Z_{t+1}\), the unfolded assignment graph is acyclic. Proof: every directed edge increases the lexicographic order (time, within-time phase), whereas a directed cycle would have to return to its starting rank. Recurrence of the *same component type* at different times does not violate the proposition.

**Limits.** This does not prove that arbitrary continuous-time dynamics, instantaneous constraints, equilibrium relations, or an unbounded universe admit this finite representation. It also does not prove causal sufficiency of the selected variables. An arbitrary observed stochastic process can be represented by history-conditioned kernels; that representation alone gives no authority to interpret kernel replacement as a physical intervention. Acyclicity is not a substitute for intervention semantics.

**Exogeneity versus physical externality.** A variable left outside the modeled assignment system is exogenous relative to that model. One may enlarge the boundary to model its generation. This change in boundary does not establish that every variable has been included, or that the enlarged model is true. Conversely, representing an intervention regime as an index does not commit the scientist to a supernatural source of action.

## Internal interventions: what the embedding does and does not supply

An ideal intervention is an operation on a causal model, such as replacing \(A_t=\pi(\cdots)\) by \(A_t=a\) or by a new policy \(A_t=\tilde\pi(H_t)\). A realizable intervention is a physical procedure within a larger world. Their equivalence is an additional modeling claim.

A transparent sufficient construction is an augmented mechanism

\[
X=\begin{cases}f(P,U)&J=\mathrm{idle},\\x&J=\mathrm{clamp}(x),\end{cases}
\quad Y=g(X,V).
\]

If setting the mode to \(\mathrm{clamp}(x)\) leaves the law of \(V\) and assignment for \(Y\) unchanged, the reduced response distribution equals the ideal \(\operatorname{do}(X=x)\) distribution. The proof is direct substitution. In a physically enlarged model, a controller can generate \(J\). Mere conditioning on the controller's naturally chosen mode is still not equivalent to setting that mode when mode choice and outcomes share causes.

**Side-effect counterexample.** Let a device mode \(J\) determine \(X=J\), a collateral variable \(B=J\), and output \(Y=X+B\). From baseline \(J=0\), the ideal \(\operatorname{do}(X=1)\) yields \(Y=1\), while operating the actual device via \(\operatorname{do}(J=1)\) yields \(Y=2\). Both are causally ordinary processes; they answer different questions. Therefore putting the intervention device inside the world does not make every variable-setting action a surgical intervention.

**Feasibility.** A hypothetical intervention may be well defined in a model while physically unavailable to a particular agent, unavailable within its budget, or impossible at that precision. A realizability claim should name a protocol, available information, resource requirements, side effects, duration, and the family of contexts in which it approximates the modeled intervention. Perfect clamping may be an idealization; P3 supplies an explicit feedback interpretation.

For adaptive systems, also name the time of implementation and which update rules remain active. Replacing today's action, replacing the future policy, rewriting stored beliefs, changing incentives, and altering goal-update procedures are distinct operations.

## Four changes that must remain distinct

**State change:** a different value under the same chosen effective transition family, observation map, and evaluation rule.

**Effective mechanism change:** a changed response family under some specified interventions and contexts at the chosen scale. One possible operational criterion is a difference between \(K_c^i\) and \(K_{c'}^i\) for some allowed intervention \(i\), holding fixed the agreed input/output interface. Whether this is substantial may depend on an explicit error tolerance and time horizon.

**Representation change:** a different internal encoding or analyst's map of the world. It can improve or worsen predictions while the modeled environmental response family remains the same. Its physical realization nevertheless changes some local states. Confusing these descriptions would make every act of thinking a change to every mechanism under discussion.

**Evaluative-purpose change:** a changed criterion used to select or judge outcomes. It can change action even when predictions remain fixed. Its occurrence does not establish its legitimacy.

A simple demonstration of the descriptive boundary is

\[
x_{t+1}=f_{\theta_t}(x_t,a_t),\qquad
\theta_{t+1}=u(\theta_t,x_t,a_t).
\]

Relative to the reduced \(x\)-model, updating \(\theta\) changes the effective mechanism. Relative to the enlarged \((x,\theta)\)-model, both transitions are one fixed function \(F\). This is an exact bookkeeping observation for this specified family, not proof that fundamental physical laws are immutable or that every future mechanism lies in a known family. Encoding an arbitrary future into an enlarged initial state would add representational coverage without adding prediction or explanation.

An ordinary change of an argument or a noise realization is not automatically a change in effective causal structure. Nor must a mechanism change alter graph topology: \(Y=aX+U\) with nonzero coefficients \(a=1\) and \(a=2\) has the same parent relation but different response magnitudes.

## Counterexamples that delimit broad causal claims

### Cycles need solution conditions

For binary variables, \(X=1-Y,\ Y=X\) has no solution; \(X=Y,\ Y=X\) has two. A directed cycle by itself supplies neither existence nor uniqueness.

More strongly, over the reals,

\[
X=Y+Z,\quad Y=X,\quad Z=X+1
\]

has exactly one solution \((-1,-1,0)\). Substituting \(Y=X\) forces \(Z=0\), then \(Z=X+1\) fixes the remaining values. But \(\operatorname{do}(Z=1)\) leaves \(X=Y+1\) and \(Y=X\), requiring \(X=X+1\). Thus unique observational solvability does not imply intervention solvability. The finite enumeration in the checks file is only a sanity check; the algebra proves the real-valued claim.

### An equilibrium does not contain the dynamics

The ODEs \(\dot x=-x\) and \(\dot x=x\) both have unique equilibrium \(x=0\), but it attracts nonzero initial conditions in the first and repels them in the second. An equilibrium equation alone cannot establish stability, speed, response to transient inputs, or maintenance cost. P3's stability restrictions have substantive work to do.

### Aggregation can erase intervention meaning

Let independently settable inputs \(X_1,X_2\in\{0,1\}\) produce \(Y=X_1-X_2\). The macro quantity \(S=X_1+X_2\) takes value 1 under both micro interventions \((X_1,X_2)=(1,0)\) and \((0,1)\), but their outputs are 1 and −1. An intervention called “set \(S=1\)” has no implementation-independent output in this family. One may define a protocol or lottery over implementations; its distribution is then part of the intervention's meaning.

### Even every perfect-intervention distribution can miss counterfactual structure

Let \(U_A,U\) be independent fair bits and \(A=U_A\). Consider

\[
M_1:\ Y=U,\qquad M_2:\ Y=A\mathbin{\mathrm{xor}}U.
\]

The models have identical joint observational distributions of \((A,Y)\). They also have identical distributions under each of the nine perfect intervention regimes: no intervention, either value of \(A\), either value of \(Y\), or any joint setting of both. However, under the shared-context counterfactual semantics,

\[
M_1:\ P(Y_0=Y_1)=1,\qquad M_2:\ P(Y_0=Y_1)=0.
\]

This is because \((Y_0,Y_1)=(U,U)\) in the first model and \((U,1-U)\) in the second. Therefore any claim that intervention-distribution preservation by itself preserves individual counterfactuals is false. This elementary construction illustrates P2's distinction among equivalence notions. All nine regimes were checked by exact enumeration; see `causal-formalisms-checks.json` and `verify_causal_formalisms.py`.

### State aggregation need not yield a closed macro dynamics

Let \(X'_{1}=X_2\), \(X'_2=X_2\), and retain only \(Y=X_1\). The microstates \((0,0)\) and \((0,1)\) have the same current macrostate \(Y=0\) but different next macrostates. No single deterministic \(Y'=F(Y)\) can represent both. A stochastic closure may work for a specified distribution of hidden states but is not automatically stable to changing policies or initial conditions.

## Representation invariance with explicit scope

For low- and high-level causal models \(L,H\), a state map \(\tau\), and an intervention map \(\omega\), the distributional commuting condition is

\[
\tau_*P_L^i=P_H^{\omega(i)}\quad\text{for all }i\in\mathcal I_L.
\]

P5 supplies a precise version with a surjective, order-preserving \(\omega\). If an outcome is genuinely macro-defined, \(q_L=q_H\circ\tau\), its distribution and integrable expectation agree under matched interventions. Proof: both are pushforwards or expectations of the same pushed-forward measure. Claims about omitted distinctions are not covered.

A stronger, pointwise compatibility condition is

\[
\tau\bigl(L(u,i)\bigr)=H\bigl(\tau_U(u),\omega(i)\bigr)
\quad\text{for every admitted }(u,i).
\]

With a shared context map and its pushed-forward context distribution, applying this equation jointly to a finite family of interventions preserves the corresponding joint macro counterfactual outcomes. Proof: for each context, every coordinate in the intervention-indexed outcome vector agrees, then push forward the context measure. This conclusion uses the stronger pointwise hypothesis; it does not follow from matching each marginal intervention law separately. P6 provides the relevant compatibility precedent. Claims involving conditioning additionally require that the evidence event be represented by the same map and have appropriate positive probability, or an agreed regular conditional version.

**Relabeling is not arbitrary variable mixing.** Coordinatewise invertible recodings, with all interventions transported consistently, preserve minimal functional dependency relations. An arbitrary invertible map of the entire state space can preserve the dynamical system while changing what counts as an atomic intervention on one coordinate. Example: from \(X=U, Y=X\), set \(Z_1=X, Z_2=Y-X\). Observationally \(Z_2=0\), but \(\operatorname{do}(Y=c)\) maps to \(Z_2=c-Z_1\), a functional constraint rather than a constant setting of one new coordinate. A graph-invariance claim must therefore name its allowed maps.

**A finite controlled-process sufficient condition for preservation over time.** Let \(P(x'\mid x,a)\) be a micro transition kernel; \(y=\tau(x)\); let \(b=\alpha(a)\) label macro actions. Suppose, for every admitted microstate and action,

\[
\sum_{x':\tau(x')=y'}P(x'\mid x,a)
=Q(y'\mid\tau(x),\alpha(a)),
\]

and every declared feasible macro action has a specified admissible implementation rule using only the implementer's available information, selecting feasible micro actions with the required \(\alpha(a)=b\). A policy using only macro history, with any such implementation, then produces the same macro trajectory distribution as \(Q\), from pushed-forward initial states. Proof: condition on the micro history; the displayed identity removes dependence on its hidden details. Apply the same macro policy and induct on time. This is an elementary controlled lumpability condition, not a novelty claim. Pointwise existence of some feasible action in each hidden state is insufficient: the implementer might be unable to tell which action is feasible. The information-admissible lifting rule is needed for an achievability claim.

Consequently finite-horizon survival, reachability, or revision success events are preserved only when those events, feasible actions, and policy information are macro-defined. Omitting the resource that makes an action feasible, the information used to choose it, or the mechanism by which an action is implemented can destroy the result. A one-step observational fit is insufficient.

## Recommended claims and remaining assumptions

The defensible claim is: **within a declared causal model class, investigators can represent the production, use, and revision of observations, models, policies, and evaluative rules as interacting processes; meaningful constraints then concern information, feasible interventions, dynamics, resources, and the invariances that survive specified changes of representation.**

This is a modeling discipline plus a source of conditional theorems. To become a testable theory, a particular model must predict differences between feasible interventions that some admissible data could contradict. To become an explanatory framework, it must identify compressions and mechanisms that add understanding beyond recording a trajectory. To become ethical grounding, it would need arguments not supplied by causal realization itself.

The assumption register should at least distinguish: (a) physical realization versus universal physical causal closure; (b) a classical stochastic/deterministic representation versus a uniquely privileged formalism; (c) well-posedness under the particular intervention family; (d) stable meanings and physical implementations of interventions; (e) sufficient boundary and state variables for the query; (f) specified observation and memory limits; (g) empirical validity of any chosen abstraction; and (h) explicit evaluation criteria whose legitimacy is not inferred from persistence.

Falsification or loss of informativeness has several forms. A protocol may systematically disagree with its predicted intervention law. Two micro implementations assigned the same macro intervention may diverge beyond tolerance. A supposedly sufficient macrostate may fail the closure test. A proposed update mechanism may require unavailable observations or resources. Alternatively, a formulation may fit every possible outcome by unrestricted changes to hidden state or mechanism; that is not a successful empirical theory but an underconstrained description.

“The furthest we can go” should therefore be retained as an open philosophical conjecture. The papers checked here establish powerful conditional formalisms; none proves that causality is the final ontological vocabulary, that a global model can be internally recovered, or that moral value follows from causal connectedness.
