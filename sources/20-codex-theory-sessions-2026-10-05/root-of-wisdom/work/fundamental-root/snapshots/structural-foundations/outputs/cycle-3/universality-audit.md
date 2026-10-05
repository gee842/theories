# Universality audit: one constraint, different scales and outcomes

Research audit, 5 October 2026. This memo challenges and strengthens the proposed architecture. It reads the first-cycle [formal foundations](../formal-foundations.md), the [second-cycle synthesis](../cycle-2/synthesis.md), and the earlier [universality memo](../cycle-2/universality-and-sources.md) as provisional research. The user's cross-scale conjecture remains a motivating hypothesis. Nothing here establishes a new universal empirical law, a novelty claim, or an AI alignment solution.

## 1. The strongest overall architecture

The defensible common structure is an **implementation constraint**: a specified activity can continue or be revised only along sequences executable with the resources, information, access, and time available to the processes making the relevant choices. The consequences can differ across scales because the dependency structure, competing demands, access, and delay differ. This common constraint does not imply that actual selection preserves future capacity, that every system faces fresh uncertainty, or that continued existence is the right objective.

The existing controlled process `M=(Q,A,W,F,{I_i},Π)` can support the larger picture if four additional objects remain explicit:

| Object | Question it answers | What it cannot supply by itself |
|---|---|---|
| Declared test profile `T` | Which function, safety condition, affected agents, horizon, and disturbance class are being evaluated? | Agreement or legitimacy of that evaluation |
| Implemented selector or joint protocol `σ` | Which admissible operations are actually attempted, using whose current information? | The best achievable capacity |
| Environmental mechanism or class `ν∈N` | Which inputs occur, or against which inputs is a guarantee claimed? | A probability law merely from a set of possibilities |
| Description/scale map `r` with an implementation certificate | Which tests, interventions, policies, and timing claims transfer between descriptions? | Automatic equivalence of any two levels called “the same system” |

For a numerical test, distinguish actual performance `J_T(M,σ,ν)` from the robust benchmark

\[
V_T(M)=\sup_{\pi\in\Pi}\inf_{\nu\in N}J_T(M,\pi,\nu).
\]

For the existing Boolean test, distinguish the actual protocol's success from `Cap_T(M)=1`. A winning controller is a witness to possible implementation. It is not an explanation of why that controller is discovered, adopted, authorized, retained, or transmitted. Nor does a stochastic success probability establish a robust guarantee. These distinctions should be visible in every cross-domain use of the framework.

The overall architecture is therefore a family of controlled, evaluated processes with certified maps between selected descriptions. It need not be a single sequence of levels, a universal scalar score, or an all-encompassing material ontology. Different observers can require overlapping, incomparable descriptions.

## 2. What “universal” could mean

There are three supportable readings and one unestablished reading.

1. **Conditional mathematical universality.** Prefix solvency, indistinguishability restrictions, and precedence bounds hold for every model satisfying their premises. Their proofs are universal over that class, including unfamiliar implementations.
2. **Representation invariance.** A coordinate or unit change preserves a test if it transports all relevant structures. The earlier dimensionless ratio `dL/B` is invariant under compatible resource and time-unit changes, for `B>0`.
3. **Certified cross-scale transfer.** A particular refinement map transports a policy or obstruction when its proof obligations hold. One-way guarantee transfer is weaker than equivalence; neither follows from matching current output.
4. **Empirical universality.** The same independently measured mechanism explains outcomes across biological, institutional, computational, and other domains. This remains a hypothesis. It requires evidence beyond mathematical representability or recurring vocabulary.

The first reading can be thin: “an operation needs its prerequisites” is almost definitional if prerequisites are identified only after seeing whether it worked. It gains explanatory content when prerequisites and substitutes are independently specified, intervention consequences are predicted in advance, and some observations could reject the proposed model. A universal conditional theorem and a falsifiable empirical bridge are different contributions that can work together.

There is no established universal tendency toward larger menus, indefinite survival, perpetual diagnosis, optimal repair, or protection of human agency. A one-shot task may rationally consume its final reserve and terminate. A stable known environment may make recurring diagnosis unnecessary. A viable system can receive support from outside its chosen boundary. Such cases fit the constraint while defeating stronger narratives attached to it.

## 3. Four changes of scale require different mathematics

| Operation | What changes | Minimum relevant obligation |
|---|---|---|
| Relabeling or changing units | Coordinates for the same behavior | Invertible transport of transitions, interfaces, annotations, and tests |
| Spatial composition or replication | Number of components and their couplings | Shared-resource accounting, concurrency, interference, access, and workload assumptions |
| Temporal abstraction | Several local steps become one macro-action | Executable local protocol, intermediate safety and solvency, observation timing, termination and duration bounds |
| State coarse-graining | Several detailed states receive one description | Sufficient distinctions for the declared predictions and choices, or an explicit approximation/error model |

A change in number of modules is not normally a change of units. In the checked [shared-diagnosis model](../cycle-2/scale-and-deadline.md), `n` simultaneous repairs with `k` shared diagnostic slots per round require `ceil(n/k)+2` rounds under its stage assumptions. Dedicated and shared diagnosis can therefore differ despite equal funds per module. Counting and precedence remain valid; the topology has changed.

Similarly, a macro-action is not merely an edge connecting its start and finish. An interrupted, unaffordable, or unauthorized intermediate step can defeat the proposed implementation. The options framework already treats temporally extended actions as closed-loop policies; it is relevant prior art, but it does not automatically discharge this project's additional payment, authority, deadline, and intermediate-safety obligations. [Sutton, Precup, and Singh, 1999](https://people.eecs.berkeley.edu/~russell/classes/cs294/f05/papers/sutton%2Bal-1999.pdf).

Composition also changes the boundary: an environment assumed to supply an input to one component may become another component whose ability and willingness to supply it need proof. Compatibility with one passive environment is weaker than compatibility under every admitted surrounding protocol. Conversely, requiring preservation in every imaginable context may be unnecessarily strong; declare the contexts relevant to the research claim.

## 4. Coarse-graining can require memory

Consider the deterministic detailed cycle

\[
a\to b\to c\to a,
\qquad \phi(a)=\phi(b)=0,\quad\phi(c)=1.
\]

With a uniformly random initial phase, both coarse histories below occur with positive probability:

| Previous and current coarse labels | Current detailed state | Next coarse label |
|---|---|---|
| `1,0` | `a` | `0` with probability one |
| `0,0` | `b` | `1` with probability one |

The current coarse label `0` is therefore not a sufficient Markov state. A model assigning it one history-independent next-step law cannot reproduce both conditions. The pair of previous/current labels repairs the prediction in this example. More generally one must retain sufficient history or other state, allow history-dependent macro-dynamics, or declare an approximation.

This example does not derive an energy cost of memory, nor show that information physically disappears. It shows a failure of a particular description. If an actor must use the repaired statistic, its access, update, and retention have to be implemented; the analyst's knowledge of the phase is not automatically the actor's memory.

### A small exact closure criterion

Let a finite controlled process have kernel `P(x'|x,a)` and projection `φ:X→Y`. Suppose states in each block have identical admissible action menus and, for each admitted action, identical probabilities into every target block:

\[
\sum_{x':\phi(x')=y'}P(x'\mid x,a)
=\overline P(y'\mid\phi(x),a).
\]

Then the projected next-state law conditional on macro-history and current action is `P̄`. Proof: condition on each compatible detailed state; all mixture terms give the same block probability. Induction preserves finite macro-trace laws for controllers using the same macro-information. A controller with its own history dependence still requires that history or memory in the closed-loop state. Safety and goals must also be block-compatible.

This is the controlled aggregation idea behind stochastic bisimulation, not a new result. Givan, Dean, and Greig additionally prove optimal-policy transfer for their finite MDPs with compatible rewards and discounted evaluation. [Full primary paper](https://cs.brown.edu/people/tdean/publications/archive/GivanetalAIJ-03.pdf), §3 and Theorem 7.

The condition is deliberately strong: it works uniformly across detailed states in a block. An aggregation that happens to work under one initial distribution and one policy may fail under an intervention that changes either. A microstate-informed controller can also choose different actions inside a block; the statement above does not secretly give that information to a macro-controller.

### Predictive sufficiency is not free operational memory

For a declared family of future experiments, histories can be grouped when every admitted continuation experiment has the same outcome law from them. This suggests a test-relative statistic `Z(h)`. To use it as controller state, one additionally needs an implementable recursive update from the current statistic, action, and new observation, with the required acquisition, storage, precision, and update costs included.

These are distinct demands: statistical adequacy, computational maintainability, and affordability. An exact real-valued probability vector is not automatically finite-bit memory. A sufficient statistic for today's tests or model need not remain sufficient after new actions, measurements, or objectives are introduced.

Predictive state representations supply relevant prior art: state can be expressed through predictions of future action-conditional observation tests, rather than solely through a fixed-length past or latent-state labels. The finite-POMDP representation result does not make inference, precision, or retention free, or establish adequacy for unrestricted future model revision. [Littman, Sutton, and Singh, 2001](https://proceedings.neurips.cc/paper/2001/file/1e4d36177d71bbb3558e43af9577d70e-Paper.pdf).

## 5. Cross-scale control needs an implementable interface

There are two separate questions: can the abstract analysis describe every relevant concrete outcome, and can the concrete controller implement the abstract decision using information it actually receives? An existentially matching abstract state can answer the first while failing the second.

Reissig, Weber, and Rungger give concrete counterexamples in which an alternating simulation requires unavailable detailed-state information or extra controller memory under symbolic-only implementation. Their feedback refinement relation strengthens the interface conditions: abstract admissible inputs remain concrete-admissible and every quantization of a concrete successor is covered. Their theorems establish closed-loop behavior inclusion and controller transfer for that architecture. This is a targeted qualification, not a claim that alternating simulation is generally invalid. [Full primary text](https://arxiv.org/html/1503.03715), §IV, Definition V.2, and Theorems V.4 and VI.3.

The current framework should therefore retain an explicit implementation certificate for each scale map:

- how the macro-decision information is obtained from permitted local information;
- how a macro-action becomes a local protocol, including who owns each choice;
- how every admitted local outcome and interruption is covered;
- how intermediate resource, authority, safety, and timing obligations are met;
- which real memory carries protocol state between decisions;
- which tests transfer, in which direction, and with which bounds.

No additional controller memory should be inferred from an analyst's proof witness. Repeated refinement requires compatible observation and memory implementations at every boundary, as well as composition of resource and time bounds. If intermediate observations enable useful local adaptation, either include that adaptation in the protocol or admit that the chosen abstraction has discarded capacity.

Causal scale consistency is a related but different obligation. The previous memo documents a primary framework in which changing description commutes with a specified mapping of interventions. Such an intervention map does not establish that a timed controller can afford, observe, or exercise the intervention. [Rubenstein and colleagues, 2017](https://arxiv.org/html/1707.00819). Control transport and intervention consistency should be connected where useful, without identifying them.

## 6. Selection is the largest missing bridge

The framework currently gives strong ways to compare feasible capacity. It has not yet supplied a general mechanism explaining actual selection.

An elementary countermodel makes the gap explicit. At reserve state `b=1`, action `maintain` emits one unit of current output and returns to `b=1`; action `extract` emits two units and goes to absorbing `b=0`, where the protected continuing function is unavailable. The process has indefinite-maintenance capacity. A selector maximizing only immediate output chooses `extract` and loses that capacity. Another selector chooses `maintain`. Identical feasible structure can therefore have opposite realized persistence. The statement concerns the declared function, not a moral ranking of the outputs.

To explain why one selector prevails, specify the feedback mechanism. Examples of distinct possibilities are an agent's reward/update rule, a political appointment procedure, a market financing rule, imitation, and differential reproduction with transmission. The latter additionally needs a population, contribution or descendant relation, and a mechanism connecting traits or practices to successors. Naming all of these “selection” does not make their causal structure interchangeable. The earlier literature memo already separates Price-style population accounting from control optimization.

Endogenizing selector code within `q` is useful but insufficient. A transition `σ→σ'` must have a generating mechanism, accessible information, and implementation costs. A simulation that repeatedly replaces `σ` with an externally computed optimal policy models intervention by the analyst unless that optimizer and its inputs are inside the system.

Three explicit research bridges are therefore still needed:

1. **Adoption:** how an available capacity-preserving protocol becomes the actual protocol under the incentives and information of the relevant agents.
2. **Persistence and transmission:** how that protocol or its functional equivalent survives turnover, copying error, competitive pressures, and changing participants.
3. **Revision:** how the system discovers and installs a different protocol when its old test, representation, or environment ceases to fit.

No theorem says these bridges always favor preserved revision capacity. Some selection environments reward extraction, concealment, or externalizing maintenance costs. Such outcomes can be central predictions of a specified model; they cannot be excluded by the definition of feasibility.

## 7. Endogeneity, observers, and boundaries

Putting observation procedures and institutional rules into the state allows transitions to change later information and permissions. It does not remove the modeler's boundary or vocabulary. An object-level revision encoded in `F` differs from an analyst changing `F` after encountering an omitted phenomenon. The fixed-ambient representation lemma establishes expressibility, not predictive completeness or a method for inventing every future concept.

An observer has at least three roles that should not be conflated: the scientist who describes the state, a participant who receives a decision interface, and an evaluator who chooses which outcomes matter. A variable visible to the scientist can be hidden from all participants. An institution's joint records can contain a distinction no single authorized participant can use in time. Pooling participant information is a stronger protocol unless timely communication and authority to act are modeled.

Boundary changes should carry an assumption ledger. External inflow, a trusted authorization service, a stable clock, an accurate model, and a functioning communication channel are all possible boundary assumptions. Bringing one inside the system adds obligations to explain its supply and failure; leaving it outside is legitimate if the empirical claim stays conditional on it. Universal constraint language should not imply that each subsystem must recreate all its own prerequisites or that the total universe has an external repair controller.

Nor is every enabling relation a conserved quantity. Authorization may be a rule-governed relation; trust may affect belief and action; a resource stock has units and balance equations. They may interact through transitions without being reducible to a single additive “capacity substance.” Their operationalizations should survive intervention tests rather than merely share a label.

## 8. How the empirical claim could fail

A useful empirical target is: **independently measured prerequisite accessibility, timing, and information improve held-out recovery predictions beyond current output, total reserves, and size alone.** Test it within domains first, then test specified transport maps between domains.

| Proposed claim | Discriminating observation or intervention |
|---|---|
| A diagnostic bottleneck sets a recovery deadline | Increasing diagnostic concurrency should shift the registered frontier; an already available alternate sensor can defeat the premise |
| Repeated fresh uncertainty makes retained correction infrastructure valuable | Fully reveal the fault, hold it fixed with retained information, or remove the hazard; benefits should change as the specified mechanism predicts |
| Reserve accessibility matters beyond aggregate reserves | Vary transfer/authorization delay while holding totals fixed; unchanged outcomes where a large effect was predicted challenge the mapping |
| A macrostate is predictively sufficient | Condition on distinct histories reaching that macrostate; persistent differences in next-step laws reject the proposed closure |
| A replacement preserves tested capacity | Run interventions that use its boundary interface, interrupt it, or vary timing; ordinary-output matching is insufficient |
| The actual selector maintains viable correction capacity | Record choices and update/transmission rules; feasible winning policies that are systematically not adopted reject the behavioral prediction |

Register the boundary, parameter estimates, uncertainty class, permitted policy information, intervention mapping, benchmark, and tolerance before evaluating held-out outcomes. Decide whether a failure rejects a parameter estimate, a scale map, or the proposed causal mechanism. Do not rescue every result by adding an unmeasured latent stock or redefining the protected function after the fact.

Repeated successful examples support a mechanism with a domain of applicability. They do not verify an all-disturbance guarantee or universal empirical scope. Conversely, one correctly measured failure can refute a particular exact guarantee while leaving a more limited statistical model useful. Negative controls are essential: a null effect when the alleged uncertainty or access obstruction has been removed can be the expected result.

## 9. Normative separation is part of the formal architecture

The protected set, prohibited operations, distribution of burdens, legitimate authority, and acceptable ending conditions are evaluative inputs. Feasibility cannot select them without further premises. A coercive institution may preserve itself effectively; this does not justify preserving it. Removing a destructive action can reduce an unrestricted action menu while improving the desired outcome. A safe shutdown or transfer to a successor can count as success under a suitable test.

For AI systems, preserving a capacity to revise or accept correction is useful only relative to who can correct what, with which information, safeguards, and authority. Maintaining a correction channel does not prove that its operator has the right goal, that the model of consequences is adequate, or that a powerful system will use that channel as intended. The project can study necessary or sufficient conditions for particular corrigibility mechanisms without presenting a general alignment solution.

These statements are reasons to parameterize the evaluation openly, not reasons to abandon structural analysis. They prevent an implementation theorem from silently carrying a political or ethical conclusion.

## 10. Status and next discriminating work

| Layer | Established or directly checkable here | Missing bridge |
|---|---|---|
| Executability | Prefix feasibility, precedence, and information-uniformity restrictions | Correct empirical boundary and operational measurements |
| Cross-scale description | Conditional invariance and directional policy transfer | Certified maps for each proposed coarse description |
| Memory | Explicit example of failed macro-Markov closure; restricted sufficient closure criterion | Affordable learned statistics under changing models and tests |
| Recurrent correction | Synthetic paid-repair and scheduling frontiers under fixed rules | Robustness to richer production, substitutes, and distributed decisions |
| Endogeneity | Representable changes of code, rules, and access within a declared semantics | Actual discovery/adoption/update mechanisms and analyst-level model revision |
| Selection | Actual selector can be modeled separately from feasible capacity | A tested explanation of which selectors persist and transmit |
| Normativity | Safety, rights, targets, and ending conditions can be explicit | Justification and agreement; no inference from persistence alone |

The most discriminating next step is to connect the integrated multiscale feasibility model to **two explicit selector mechanisms on the same physical process**. One can favor current output; another can respond to a measured future-loss signal with paid delay and imperfect information. Hold the process and evaluation fixed, derive when each selector adopts or abandons repair infrastructure, and test whether the predicted selection outcome survives a certified change of description. Include a regime in which maintenance is unnecessary, and one in which shutdown or replacement satisfies the declared objective. This closes more of the explanatory gap than another illustration of a feasibility constraint alone.

## Primary-source access record for new connections

| Source | Inspected evidence | Exact role and limitation |
|---|---|---|
| Givan, Dean, Greig (2003), [*Equivalence Notions and Model Minimization in Markov Decision Processes*](https://cs.brown.edu/people/tdean/publications/archive/GivanetalAIJ-03.pdf) | Author-hosted full PDF; definitions, stochastic-bisimulation section, Theorems 4–7, related proofs | Controlled aggregation precedent; its policy result has a specified MDP/reward scope |
| Littman, Sutton, Singh (2001), [*Predictive Representations of State*](https://proceedings.neurips.cc/paper/2001/file/1e4d36177d71bbb3558e43af9577d70e-Paper.pdf) | Proceedings full PDF; abstract, predictive tests, finite-POMDP representation argument | Predictive state precedent; implementation and physical costs are separate |
| Reissig, Weber, Rungger (2017; preprint 2015), [*Feedback Refinement Relations for the Synthesis of Symbolic Controllers*](https://arxiv.org/html/1503.03715) | Full HTML; §IV counterexamples, Definition V.2, Proposition V.3, Theorems V.4 and VI.3 | Closest control-interface precedent; stated implementation architecture matters |
| Sutton, Precup, Singh (1999), [*Between MDPs and Semi-MDPs: A Framework for Temporal Abstraction in Reinforcement Learning*](https://people.eecs.berkeley.edu/~russell/classes/cs294/f05/papers/sutton%2Bal-1999.pdf) | Academic-hosted full PDF retrieved; abstract/introduction inspected; extraction is imperfect | Related macro-action architecture only; no theorem-level safety or resource claim imported |

The causal-consistency source is reused from the previous cycle, whose [access record](../cycle-2/universality-and-sources.md) states the inspected definitions and qualifications. The architecture above integrates established ingredients and explicitly identified research proposals. It makes no priority claim.
