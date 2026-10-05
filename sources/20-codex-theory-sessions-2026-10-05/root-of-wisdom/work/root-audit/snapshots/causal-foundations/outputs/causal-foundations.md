# Causal foundations of observers and revisable institutions

Research synthesis for Ren, 5 October 2026.

The strongest defensible version of the proposal is a **constraint on explanation**: when an explanation depends on observing, choosing, remembering, evaluating, or revising, those activities must have realizable conditions within the modeled world or explicitly declared support from outside its boundary. Their reliability cannot follow merely from calling them an observer, policy, institution, or correction mechanism.

This constraint is useful, but it is not yet a complete theory. Saying that everything is causally realized does not specify which changes are possible, which observations discriminate them, which arrangements can repair themselves, or which purposes deserve support. Those questions require a model, an intervention interface, a timescale, evidence, and evaluative commitments. Causal embedding becomes informative when it produces a discriminating prediction or an impossibility result under independently specified assumptions.

The claim that causality is “the furthest we can go” therefore has a qualified answer. It is a plausible stopping point for a particular demand: do not explain action by placing a causally effective chooser outside the account. It is not an established final ontology, a proof that causal language is irreducible, or a source of ethical obligations.

The accompanying [formal results](formal-results.md) give precise propositions, proofs, finite counterexamples, and verification details. [Sources and claims](sources-and-claims.md) distinguish established precedents, our elementary derivations, proposals, and open questions. These are research findings, not empirical validation of institutions or AI alignment.

## What the existing research already establishes

The reference research under `/Users/ren/theories` supplies a substantial starting point. Its claim register distinguishes resource feasibility, actionable information, institutional enactment, renewal, inheritance, and normative commitment. In particular:

- U05 shows how observationally indistinguishable situations can require incompatible safe responses.
- U12 and U13 model feedback between activity and retained understanding, including attracting exclusion despite common interests.
- U20 shows that a summary adequate under one model can discard evidence needed after model expansion.
- U24 separates positive average inquiry returns from the ability to survive recurrent funding shortfalls.
- N01 explicitly separates shared agency and legitimate revision from mere persistence.

Those results already constrain causally embedded agents. Their recurring limitation is equally instructive: candidate grammars, recognition rules, diagnostic mechanisms, and common purposes often remain supplied by the analyst. Putting their formation and revision inside the account is a legitimate next step, but renaming them as state variables does not explain how they arise.

This synthesis develops the methodological foundation of that next step. It does not rerun or independently validate the reference workspace's experiments, and it does not modify that workspace.

## Several different commitments are at stake

“One causal world” can mean several things. They should not be treated as interchangeable.

| Commitment | What it says | What it does not establish |
|---|---|---|
| Realization within a system | A particular memory, policy, or institution operates through actual processes and relations | That its best explanation must use microscopic vocabulary |
| Embedding in a causal model | The model includes relevant effects of sensing, acting, and revision, with declared boundary inputs | Complete knowledge or a description of the entire universe |
| Physical causal closure | Physical effects have adequate physical causal accounts, under a specified formulation | Determinism, causal sufficiency of an observed variable set, or agreement on values |
| One interconnected world | The observer and what it observes participate in a shared world | Substance monism, a unique causal graph, or the absence of useful distinctions and levels |
| Organizational closure | Specified enabling constraints contribute to maintaining one another | Thermodynamic isolation or universal physical closure |

A causal model may be stochastic, contain unobserved causes, and describe an open subsystem. Conversely, a deterministic transition rule need not tell an observer what would happen under interventions it has never encountered. These distinctions prevent “causally realized” from silently becoming “fully known,” “fully controllable,” or “equally influential.”

An institution also need not occupy one compact physical location. Its policy may be realized across records, people, software permissions, budgets, and recurring practices. The functional boundaries have to be justified for the question being asked. A document announcing a right and a mechanism that actually allows someone to exercise it can have different causal roles.

Montévil and Mossio's work on closure of constraints is a close precedent for reciprocal maintenance. They distinguish changing processes from constraints conserved over relevant operating timescales, while those constraints are themselves maintained through other processes. This is a biological organizational proposal, not a proof that every feedback cycle is alive, self-sufficient, or legitimate. The accessible author-uploaded [primary article](https://www.researchgate.net/publication/262486802_Biological_organisation_as_closure_of_constraints) supports this limited comparison.

## A minimal model with the observer inside

For a finite, discrete-time laboratory, write the state as

\[
z_t=(w_t,c_t,r_t).
\]

Here \(w\) describes the relevant situation, \(c\) the controllers and institutions, and \(r\) the resources and access conditions. This is a modeling decomposition, not a claim that nature arrives divided into three independently manipulable parts.

Read from \(c_t\) the observer's current represented model \(m_t\), policy \(\pi_t\), evaluative commitments \(g_t\), and implementation arrangements \(\kappa_t\). These are **functional readouts**; they can share a physical realization. The ability to distinguish their roles does not imply that one can change each independently.

A simple within-period ordering is

\[
o_t\sim O(\cdot\mid z_t),\qquad
a_t\sim\pi_{c_t}(\cdot\mid o_t),\qquad
z_{t+1}\sim K(\cdot\mid z_t,o_t,a_t).
\]

Memory of earlier observations lives in \(c_t\). The transition can change the sensor, retained evidence, represented model, policy implementation, goal register, institutional gates, and resources. To represent sensing costs or failures adequately, the state can include separate sensing and decision phases. Independent random draws in this simple factorization are assumptions; shared causes must be included or represented through a suitable joint law.

The ordinary closed-loop transition is obtained by composing these steps. No second chooser must sit outside the dynamics to choose the policy. A learning program can modify a policy program while a larger fixed transition rule describes both. A distributed institution can do the same through collective processes.

For causal questions we additionally specify a family of intervention protocols \(i\in\mathcal I\), with kernels \(P^i(z'\mid z)\). A transition estimated from ordinary observation is not automatically one of these intervention kernels. Nor does the symbol \(i\) imply that this observer can implement it. A real intervention may take several steps, consume resources, require another actor's cooperation, or fail. Its implementation belongs in the state trajectory when that matters.

The complete analysis also declares an observation interface, allowed protocols, initial conditions, horizon, resource accounting, and an outcome question. Without those declarations the model is a container for possible explanations, not an explanation of a particular result.

The finite model cannot describe unrestricted conceptual novelty by assumption. It can represent a supplied space of possible programs or hypotheses and their endogenous selection. Making this space countably unbounded still does not give a finite observer an exhaustive grammar, unlimited computation, or an explanation of semantic content. The distinction between what the modeler can describe and what an agent can discover remains essential.

Calling a variable a model or belief also needs justification: specify what its values represent and how that content participates in action or revision. An interpretation theorem alone can be weak evidence for learning. A recent [good-regulator theorem for embodied agents](https://arxiv.org/html/2508.06326v1), for example, admits a doorstop's trivial model under its formal interpretation. That is a useful warning against reading rich cognition into every regular causal response.

## Four changes that should remain distinct

| Change | Operational question | Example |
|---|---|---|
| State | Did the current configuration change? | A room warmed or a reserve fell |
| Effective mechanism | Did the response to a specified intervention change at the chosen scale? | Rewiring an actuator reverses its response |
| Representation | Did the observer change the distinctions or consequence model it uses? | Calibration reveals the reversed wiring |
| Evaluative purpose | Did the ranking of possible outcomes change? | A target is changed from heating to cooling |

All four may be state changes in a sufficiently inclusive model. Their explanatory roles remain different. Moreover, changing the analyst's coordinates is different from physically changing an observer's stored representation.

A binary example makes this precise. Let physical wiring be \(q\in\{0,1\}\), represented wiring be \(m\), and target be \(g\). The controller chooses \(a=g\oplus m\); the actuator produces \(x'=a\oplus q\), where \(\oplus\) is exclusive OR. Then \(x'=g\) exactly when \(m=q\).

Changing \(q\) changes the actual action-to-outcome response. Changing \(m\) changes the controller's interpretation and resulting policy while leaving that response fixed. Changing \(g\) changes the target. A change to an irrelevant hardware bit need change none of these effective relations. All eight combinations of \((q,m,g)\) were checked by exact enumeration.

Even a causal graph is too coarse to identify every mechanism change: both wiring modes retain an arrow from action to outcome while its functional effect reverses. Conversely, microscopic reorganization need not alter any response relevant to the intervention family. “The causal structure changed” therefore needs a declared level, variables, interventions, and resolution.

The earlier signature \(S=(X,T,R,O)\) remains useful as a description of effective possibilities. At a given state, \(T\) can mean realizable action protocols, \(R\) their enabling conditions, and \(O\) accessible distinctions. Activity can alter that description. However, \(S_{t+1}=\Phi(S_t,e_t)\) is not automatically a closed evolution law: different physical situations can share the same \(S_t\) and have different next possibilities. It needs a closure test, extra memory, or an explicit approximation. An unobserved residual \(e_t\) that absorbs every mismatch cannot by itself rescue the proposal's predictive content.

## Causal graphs and feedback have limited jurisdictions

A DAG is a directed acyclic graph. Recurrent interactions such as observation influencing action and action influencing later observation can be represented by an acyclic graph of temporally ordered events under an appropriate update model. This does not establish that every causal relation in every physical theory fits one universal event DAG.

An unrolled graph also depends on the time resolution. An instantaneous equilibrium model and an explicit dynamical model need not preserve the same interventions. Cyclic structural causal models are possible, but existence and uniqueness of solutions, and their persistence after intervention, require care. [Bongers and colleagues](https://arxiv.org/abs/1611.06221) develop these distinctions and identify classes with stronger closure properties.

For example, the simultaneous real equations \(X=Y+Z\), \(Y=X\), and \(Z=X+1\) have the unique solution \((-1,-1,0)\). Replacing the third equation with \(Z=1\) leaves \(X=Y+1\) and \(Y=X\), which have no solution. Observational solvability alone does not validate every proposed surgical intervention.

Continuous-time differential equations, stochastic processes, hybrid systems with discrete changes and continuous flows, and constraint models can be better descriptions for other tasks. Primary work connects [ODE equilibria to SCMs under stability assumptions](https://arxiv.org/abs/1304.7920) and supplies [intervention semantics for specified stochastic differential equations](https://arxiv.org/abs/1304.0217). The finite model here is a place to prove bounded claims. It is not a competition to replace all those formalisms with one notation.

## Internal interventions and counterfactuals

An intervention need not originate outside the universe. A randomized trial can be implemented by a physical randomizer, people, and equipment. Relative independence between that assignment and relevant disturbances is a local modeling assumption. Shared membership in one world does not either establish or rule out that independence.

There are nevertheless two separate questions: what follows if a modeled mechanism is replaced, and whether an embedded actor can carry out a protocol that realizes that replacement. An ideal intervention can be mathematically meaningful without being presently affordable or feasible. If a protocol affects other modeled pathways, the claimed ideal intervention may also be an inaccurate description of its effects.

Counterfactual comparison adds another distinction. Consider independent fair bits \(A,U\). Model one has \(Y=U\); model two has \(Y=A\oplus U\). They agree on the observational distribution of \((A,Y)\) and on all perfect-intervention distributions over these two variables. Yet the first says \(Y_0=Y_1\) for each unit, while the second says \(Y_0\ne Y_1\). Both keep the same \(U\) across their own alternative interventions. Thus even knowing all these intervention marginals does not identify the coupling between incompatible possibilities.

This is an elementary counterexample, not a new theorem. It shows why “the world is causal” cannot settle counterfactual meaning without further structure. It also limits what an abstraction that preserves intervention distributions can promise.

## What can remain invariant under representation changes

Two precise classes are defensible.

First, a bijective relabeling preserves a model's predictions when the transition law, observations, intervention labels, admissibility rules, and outcome criteria are transported consistently. This is exact but modest: changing labels should not change the question's answer. Arbitrary coordinate mixing need not preserve a variable graph or the interpretation of intervening on one coordinate.

Second, a many-to-one map \(q:Z\to\bar Z\) can preserve declared intervention predictions if states placed in the same group have the same distribution over next groups under every admitted intervention. In symbols,

\[
\sum_{z':q(z')=\bar z'}P^i(z'\mid z)
=\bar P^i(\bar z'\mid q(z)).
\]

This condition is required throughout each group, with compatible action availability, observations, and initial distributions related by the same map. The observation and transition chronology also matters: if the next state stores the current observation, include that observation in the decision state or require the matching condition separately for each supported observation. Matching separate observation and transition marginals is insufficient.

Under the same policy using the preserved observations, these conditions imply equality of finite path distributions. Any safety or outcome event defined on those paths then has the same probability. The appendix proves the statement and an approximate version: a uniform conditional one-step discrepancy at most \(\varepsilon\), measured in total variation, yields a horizon-\(H\) path discrepancy at most \(1-(1-\varepsilon)^H\le H\varepsilon\). Total variation bounds the difference in probability assigned to any event. A good average fit to training data does not establish this uniform bound.

An abstraction can be valid for routine operations and fail when repair becomes an allowed intervention. Its adequacy is therefore relative to the intended questions and interventions. It need not preserve arbitrary microscopic detail, every possible future question, or performance available to a controller that sees additional microscopic information. This is the relevant connection to [causal consistency](https://arxiv.org/abs/1707.00819) and [causal abstraction](https://www.cs.cornell.edu/home/halpern/papers/abstraction.pdf).

This provides a substantive answer to the invariance question: preserve specified response distributions and outcome claims across a defined class of transformations. Neither graph shape nor an unrestricted claim about “the same causal structure” is an adequate replacement for that definition.

## Which arrangements can maintain and revise themselves

A bare transition system permits too much. A stone, a stable coercive institution, and a learning community can all be embedded in dynamics. To study revisability, specify the functions and tests that distinguish the cases.

For a declared disturbance family and horizon, maintenance means that specified enabling functions remain available. Discovery means that a candidate is generated or selected from available evidence and a declared search process; inserting a correct answer from the analyst does not demonstrate discovery. Revision means that a reachable process changes a specified arrangement. Useful revision additionally meets an independently declared outcome criterion. Legitimate revision requires an account of affected parties and acceptable procedures; physical access alone is insufficient.

The operative question becomes:

> From this information and resource state, can an implemented process acquire the needed distinction, construct and evaluate a response, enact it in time, and leave the required continuation functions available?

A graph showing a cycle of mutual support cannot answer this. For instance, \(A_{t+1}=B_t\) and \(B_{t+1}=A_t\) give a strongly connected dependency graph. The state \((1,1)\) persists, but \((0,0)\) cannot restart itself, and the other states alternate. Reciprocal dependence is not a sufficient certificate of renewal, recovery, learning, or value.

Information imposes an independent restriction. If two states share the entire available evidence and require incompatible actions before a deadline, no evidence-based policy can guarantee the correct action in both. More computation on the same evidence cannot fix the distinction. New observations, a common safe fallback, a longer deadline, or changing the available actions may fix it. This restates the reference research's U05 in the embedded setting.

Finite memory imposes another boundary. An archive can answer all questions in a declared family exactly only if it retains the distinctions that separate their answers. Expanding the question family may invalidate an earlier sufficient summary. There is no theorem requiring maximum memory: costs, privacy, and available fresh measurements still matter.

Self-reference also has a narrow exact limit. A predictor cannot always announce a correct next binary action to a system that reliably chooses the opposite of the announced bit. This does not rule out useful self-models, restricted accurate predictions, or prediction whose release does not trigger such a response. [Wolpert's inference-device analysis](https://arxiv.org/abs/0708.1362) provides a broader primary precedent under its own precisely defined inference conditions.

## A worked institutional example

Consider a small institution facing a hidden fair binary condition \(\theta\). It has two responses, 0 and 1, and a supplied current goal of matching the condition. Its routine response is 0. A reliable probe costs one unit; deploying a response selected from its result costs one more. An admitted record updates institutional memory. Enactment additionally requires an operative permission gate. The entire procedure is a fixed program represented within the institution's state.

This is intentionally small enough to inspect fully. The probe and action grammar are supplied; this is not discovery of an unforeseen concept. Exact enumeration gives:

| Arrangement | Probability of matching the condition |
|---|---:|
| Probe, record admission, enactment access, and two units available | 1 |
| Probe unavailable | 1/2 |
| Probe works but its record cannot update institutional memory | 1/2 |
| Evidence is retained but deployment is blocked | 1/2 |
| Only one unit is available, insufficient for both steps | 1/2 |
| Full capacity, but goal is changed to choose the opposite condition | 0 |

The last arrangement meets its changed internal objective perfectly while failing the original declared criterion completely. Goal revision belongs in the causal account, but the account does not decide that the new objective is better. The table compares specified arrangements and initial budgets; actual spending differs when a step is unavailable. It is not a matched-expenditure empirical experiment.

A further exact trajectory makes revision itself internal. Start with deployment blocked and three units available. The program first pays one unit to probe and retain the result. When it has a record and detects the blocked gate, it requests an amendment through a supplied amendment channel. If that channel is operative, the request consumes one unit and changes the deployment gate from closed to open. The program then spends its last unit deploying the record-responsive action. It succeeds in both hidden conditions. With the same budget but no operative amendment channel, it retains the correct evidence yet falls back to response zero and succeeds with probability one half.

The record, request, changed permission, action, and resource debits all occur under one fixed staged transition rule; an outside analyst does not choose the amendment after seeing the hidden condition. The changed gate is an effective mechanism change inside that fixed larger process. The amendment channel and its upkeep over this short episode remain supplied. This example demonstrates a reachable revision of a rule, not the optimal amendment policy, unrestricted discovery, or legitimacy of the revised authority.

The example shows why information, recognition, enactment, resource access, and purposes cannot be replaced by a single measure of intelligence or connectedness. It also shows what remains open: the procedure does not explain where the probe came from, why standing and permissions persist, how shared goals were agreed, or how another response enters the grammar. Those omissions are visible boundary assumptions rather than hidden achievements.

For an AI system the corresponding roles might be retained evidence, predictive representation, action policy, evaluation criteria, tool permissions, and the update process. Making them causally explicit helps locate failure modes. It does not establish that the model's internal reward represents human interests, that self-modification preserves commitments, or that all relevant stakeholders can challenge its actions.

## How to test whether the framework adds explanatory value

The unrestricted assertion “all these events have causes” admits no discriminating test by itself. A specified realization claim can be tested: disrupting a proposed memory carrier while preserving declared alternatives should produce the predicted change. A specified closure claim can fail when unmodeled influences systematically alter intervention responses. Failure of one model, however, does not directly refute physicalism.

A useful next experiment would compare three models of one bounded revising system: a fixed external policy, a changing policy with externally guaranteed support, and a policy whose evidence channels, enactment access, and support renewal are themselves modeled. Fit each using the same training observations. Before seeing outcomes, declare interventions that disable or restore particular links, held-out disturbance regimes, horizon, loss measures, and tolerances.

The embedded account earns its additional complexity if it predicts intervention outcomes or relapse that the simpler accounts miss. Match resources and measurements where the causal comparison requires them, and record unavoidable differences rather than treating equal grants as equal expenditure. Include a null regime in which further inquiry has no benefit, a misleading-candidate regime, and a harmless microscopic perturbation predicted to leave the effective mechanism unchanged.

For representation claims, fit a proposed abstraction on one dataset and test its predicted response distributions under held-out implementations of the declared interventions. Also test a deliberately omitted intervention. Failure under the latter can establish a useful boundary; failure within the declared family and tolerance counts against the abstraction.

For discovery, withhold correct candidate labels from the learner and log what evidence and search operations produce candidates. A supplied grammar can support a bounded discovery claim. It cannot support unrestricted concept formation. For changing goals, evaluate both the system's current goal and stable, separately declared stakeholder criteria, so changing the evaluator cannot automatically count as progress.

The research direction becomes uninformative if every failure is accommodated by unconstrained hidden state, if effective mechanisms are redescribed only after outcomes are known, if “revision” includes every fluctuation, or if the assessment criterion moves whenever the system fails it. These are failure conditions for the explanatory program, not only implementation mistakes.

## What remains of the foundational conjecture

| Reading of the conjecture | Assessment |
|---|---|
| Ontological commitment | A coherent possibility, not established by the models. The status of laws, causal direction, consciousness, and modality remains open. |
| Explanatory framework | Strongest defensible reading. It forces the conditions of observing and revising into the explanation or into explicit boundary assumptions. |
| Empirically testable theory | Only after mechanisms, interventions, observables, outcomes, and failure criteria are specified. The general framing alone is too permissive. |
| Ethical grounding | Insufficient. It can constrain feasible means and expose consequences, but connectedness and persistence do not determine whose interests count. |

There is no need for an infinite hierarchy of separate choosers simply because a policy or revision rule can change. Their physical carriers can be states of one encompassing process. But that mathematical possibility does not prove that a final, accessible, finite description exists. Adding an update rule raises questions about that rule's realization and adequacy; it does not answer them automatically.

Nor is causal language demonstrably the deepest available language. One can still ask what fixes possible interventions, how causal asymmetry arises, why particular laws hold, how system boundaries are selected, and what makes a representation about something. Some of these questions may be addressed through causal models; others concern the interpretation and justification of those models. The investigation does not settle that boundary.

The strongest formulation is therefore:

> Study the realizable conditions under which processes can preserve, discover, and revise their own means of observing and acting. Require claims to survive specified changes of representation and to face tests under declared interventions. Keep the value and legitimacy of the resulting changes open to explicit evaluation.

This is compatible with the broader concern for 生生 as continued becoming, renewal, and succession. It supplies feasibility and knowledge constraints on such a project. It does not establish nonduality, universal causal closure, mathematical novelty, a universal social law, or a solution to AI alignment.
