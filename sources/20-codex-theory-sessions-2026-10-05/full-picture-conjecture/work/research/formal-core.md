# A formal core that can fail: typed dynamics, situated control, and explicit abstraction contracts

Research memo, 5 October 2026. Prepared independently for the full-picture investigation. The source workspace was read only. The mathematical constructions below are finite special cases, with elementary proofs and counterexamples. They establish no universal completeness, novelty, or ethical authority.

## 1. Recommendation

Use a **family of typed, scoped, partially observed transition systems and checked maps between them**. Do not present one four-symbol signature as an already unified theory. The promising common structure is that material and institutional realizations of observation, memory, policy execution, evaluation, and revision can affect their own future feasibility. Whether a particular domain really has that structure must be established by a mapping with independently measured mechanisms.

The finite operational core is

\[
\mathcal M=(X,X_0,U,F,Y,h;\tau,\mathcal L),
\]

where:

- \(X\) is a declared state space and \(X_0\subseteq X\) the admitted initial states.
- \(U\) is an action/interface alphabet. \(F(x,u)\subseteq X\) gives possible successors. We initially assume finite sets and nonempty successor sets. Unavailable or invalid actions can lead to an explicit failure state; this avoids counting deadlock as vacuous safety.
- \(Y\) is an observation alphabet and \(h:X\to Y\) the observation channel in the first deterministic-observation treatment. A stochastic channel is a kernel, not merely another set of labels.
- \(\tau\) supplies types, units, and declared roles for coordinates and interfaces. A funding balance, a legal entitlement, an observation channel, and a relation of dependence are different kinds of objects even if they interact.
- \(\mathcal L\) is a specified collection of observables and predicates whose preservation matters. Examples are a resource quantity \(e:X\to\mathbb R\), a failure predicate, carrier identity, and an institutional permission predicate. Include only what the inquiry declares; \(\mathcal L\) is not a complete language of every possible meaning.

The core is deliberately prior to one optimizing objective. A control question appends a protected set \(K\), time horizon, disturbance interpretation, and policy class \(\Pi\). An economic question can append costs; a causal question must append intervention semantics. A resource balance is an additional constraint on \(F\), not a consequence of calling a state coordinate a resource.

This is a conventional operational language. Its potential value here is the disciplined comparison of renewal, evidence, revision, and institutional implementation. Its expressiveness alone supplies no prediction.

## 2. Why the earlier signature needs typing

\(S=(X,T,R,O)\) is a useful prompt for inspection, but currently underdetermines a mathematical object.

| Earlier term | Ambiguity | Replacement discipline |
|---|---|---|
| \(X\), configurations | Physical configurations, descriptions, or configurations of descriptions? | Declare the modeled boundary and state-sufficiency assumption; put description carriers in state when relevant. |
| \(T\), transformations | Action names, realized events, transition laws, possible functions, or available interventions? | Separate \(U\), the law/relation \(F\), its local implementation parameters, and a declared intervention family. |
| \(R\), resources/relations | Stocks with units, required inputs, causal relations, authority, and social recognition are conflated. | Use distinct typed quantities, relations, and predicates; justify conversion and dependence rules. |
| \(O\), distinctions | The actual channel, its possible outputs, a partition, a language, or an agent's represented categories? | Separate \(h\), \(Y\), memory, and semantic/model-carrier structure. |

Saying a transformation changes all four does not resolve these types. For example, a damaged sensor changes an effective observation channel, while changing the analyst's state vocabulary changes a representation of that channel. Those are not the same event. Either can be modeled, but they require different maps.

Open systems remain open. One can expose an environmental input \(d\) and write \(F(x,u)=\bigcup_{d\in D(x,u)}f(x,u,d)\). This represents a stipulated range of external influences; it does not prove that every cause has been included. The nondeterministic form forgets probabilities and therefore cannot by itself support expected-loss or frequency claims.

## 3. Put realizations inside without conflating functional roles

A useful state decomposition is illustrative rather than universal:

\[
x=(w,r,c_{\pi},c_m,c_v,c_o,\mu,\theta).
\]

Here \(w\) describes the remaining modeled world, \(r\) typed resources, \(c_\pi\) a policy carrier, \(c_m\) a world-model carrier, \(c_v\) an evaluative-standard carrier, \(c_o\) an observation apparatus, \(\mu\) memory, and \(\theta\) effective mechanism parameters. These carriers can be distributed across people, files, software, routines, and organizations. They need not be separable physical boxes.

The distinctions are functional:

- A policy's realized execution relates accessible information and memory to action.
- A world model supplies represented relations, predictions, or counterfactual claims; its presence does not establish their truth.
- An evaluator realizes a procedure for judging outputs or changing permissions; its current judgment is a causal fact, distinct from the legitimacy of that judgment.
- An observation apparatus generates signals under physical and institutional constraints.

A decoding/realization relation connects a carrier to one of these roles. It must be specified and checked. A string that says “maintain inquiry” is not already an effective maintenance policy; a score stored in a file is not already authority to act. Effective execution can depend on resources, access, and institutional recognition.

The open interface \(u\) is not an assumption that a disembodied agent can choose anything. A study of the installed system constrains \(u\) to actions actually generated by its realized controller; revisions of that controller are transitions with costs and preconditions. A study of possible interventions declares which replacements are available and to whom. The same carrier can function as a controller in one system decomposition and part of the plant in another. Those views must agree on the shared execution traces if claimed equivalent.

**Implementation caveat.** The unrestricted history-policy class \(u_t=\pi_t(y_0,u_0,\ldots,y_t)\) permits ideal memory and computation. Including some resource coordinates in \(X\) does not automatically charge for that ideal controller. A physical implementability claim must either include finite controller/memory states, update rules, failure modes, and costs in \(X\), or provide an explicit realization certificate for the selected policy. This issue is directly relevant to the earlier research's separation of free sufficient belief from paid inheritance.

## 4. Mechanism change and state-space change

**Changing effective mechanisms in a fixed representation.** If \(\theta\) includes a sensor design, policy program, network topology, or institutional rule, the joint transition law can update \(\theta\). The effective subsystem law then changes from \(F_\theta\) to \(F_{\theta'}\) while the joint modeling law remains fixed. No changing fundamental physics is implied.

**Changing schemas within a supplied grammar.** Let \(\Sigma\) be a declared collection of schemas, with state types \(X_\sigma\). The disjoint union

\[
X^*=\coprod_{\sigma\in\Sigma}\{\sigma\}\times X_\sigma
\]

can represent additions of objects, dimensions, links, or representational categories, with transitions between schema-indexed states. This handles variable populations, graphs, and programs when the grammar and transition interpretation are supplied.

**Revision beyond the current grammar.** If researchers discover an omitted variable or intervention kind, they may replace the model and seek a partial comparison map on the overlap. Encoding all earlier and later models as strings is possible for a specified coding scheme, but does not prove that the encoding anticipates every future distinction or preserves its meaning. A model family can document situated revision without claiming a complete list of possible revisions.

The candidate core therefore admits its own records, authors' models, and revision procedures as modeled processes. It does not certify the truth of its own boundary, realization relations, or future adequacy. “Includes a representation of its construction” is weaker than “completely represents every condition of its construction.”

## 5. Four kinds of map that should not be conflated

**Projection.** A function \(q:X\to Z\), usually surjective onto its image, merges states. It preserves only facts constant on each fiber \(q^{-1}(z)\) by definition. It need not preserve dynamics, causality, decisions, or values. A coordinate projection is one special case.

**Abstraction.** A projection plus an abstract model and a preservation contract. Exact transition preservation, conservative safety preservation, equality of a specified probability law, and approximation with a numerical error bound are different contracts. An abstraction can be valid for one question and invalid for another.

**Interpretation.** An assignment from domain entities, practices, or statements to formal roles, with bridge claims linking observations and interventions to the model. For example, interpreting an appropriation rule as the allocation parameter in a reserve balance requires evidence about payment timing and who can use the funds. A cultural interpretation can preserve a conceptual relation without preserving causal laws. Such an interpretation is an argued reading, not automatically a quotient map.

In logic, a stronger technical notion can specify a sentence translation \(t:L_A\to L_B\) and a model map \(I\) satisfying \(M\models t(\varphi)\iff I(M)\models\varphi\). That is a stated satisfaction-preservation result within the languages and model classes. It does not by itself validate an empirical interpretation or translate everything a cultural text means.

**Equivalence.** Always append “with respect to what.” Same observed traces, same action-conditioned probabilities, bisimulation, isomorphism, and equality of optimal value for one reward are different relations. A bijective change of coordinates with commuting dynamics is a very strong equivalence. Equal observational behavior need not preserve intervention effects. Equal value for one task need not preserve other interests.

## 6. Proposition A: exact quotients preserve a declared safety problem

Consider finite concrete and abstract systems with common actions \(U\), observation alphabet \(Y\), nonempty successor sets, and a surjection \(q:X\to Z\). Suppose, for every \(x,u\),

\[
q(F(x,u))=\bar F(q(x),u),\qquad
h(x)=\bar h(q(x)),\qquad
K=q^{-1}(\bar K). \tag{A1}
\]

These are three distinct assumptions: exact action-conditioned transitions, preserved observation channel, and preserved protected predicate. If invalid actions are represented by failure transitions, their failures must also be preserved. Otherwise require identical action availability on fibers.

For any nonempty initial information set \(B\) consistent with one initial observation and any finite horizon \(n\), a common observation-history policy guarantees concrete safety from \(B\) iff it guarantees abstract safety from \(q(B)\). Consequently a safe policy exists in any fixed common class of such policies on one side iff it exists on the other. If that class requires physical implementation, the required controller-realization correspondence is an additional assumption.

**Proof.** Every concrete trajectory projects to an abstract trajectory by the first equality, with identical action and observation histories by the second. Conversely, choose any abstract trajectory beginning in \(q(B)\). Choose a concrete initial state in \(B\) over its initial state. At each step the first equality provides a concrete successor over the selected abstract successor, even after the preceding concrete choices. Induction lifts the whole finite trajectory. The common observation policy chooses the same actions along both trajectories. The third equality makes each corresponding state safe or unsafe together. Hence all trajectories satisfy safety on one side exactly when all do on the other. Quantifying over the common policy class yields the existence claim. ∎

The relation “\(q(x)=q(x')\)” is an action- and observation-preserving bisimulation in this finite setting: each transition on one side can be matched within the same successor fiber on the other. This justifies the equivalence for the declared interface; it does not make the two physical states identical. The proof also preserves other finite trace predicates expressible using preserved labels. It does not preserve probabilities unless a probabilistic contract is added.

For finite stochastic systems the relevant exact condition is, for every \(u,z'\),

\[
\sum_{x':q(x')=z'}P(x'\mid x,u)=\bar P(z'\mid q(x),u). \tag{A2}
\]

The left side must be independent of which representative \(x\) in a fiber is chosen. With matching initial pushforward, output channels, and an observation policy, induction gives matching projected finite trajectory probabilities. This is an action-wise strong lumpability condition. Support equality alone is insufficient: probabilities .01 and .99 have the same positive support.

### Positive worked mapping: carrier replacement with the same function

Let \(X=\{0,1,2,3\}\times\{A,B\}\), with state \((e,c)\). Energy levels 1–3 are safe; 0 is absorbing failure. The carrier \(c\) can change. There are two actions:

| Current energy | consume | charge |
|---:|---:|---:|
| 0 | 0 | 0 |
| 1 | 0 | 2 |
| 2 | 1 | 3 |
| 3 | 2 | 0 |

Consumption keeps the carrier; charging switches A and B when energy is positive. Charging at 3 destroys this toy system by overcharging. The observer receives only “failed” or “running,” so it cannot directly see the positive energy level or carrier identity. Map \(q(e,c)=e\), take the table as \(\bar F\), and use the same running/failed observation rule. Every condition in (A1) holds.

What survives: the exact possible energy traces, actions, alarms, and safety of every common policy. What is discarded: carrier identity and its switching history. A belief \(\{1,2\}\) is safe indefinitely by alternating charge and consume; so is \(\{2,3\}\) with the reverse initial choice. A belief \(\{1,3\}\) has no safe first action. The quotient preserves both success and impossibility.

The computation checked all 16 state/action commutation conditions and 396 belief/horizon safety equivalences: 66 nonempty observation-homogeneous concrete information sets at horizons 0–5. This confirms the small implementation against the general elementary proof. It is not evidence that real replacement technologies have identical dynamics. If carrier B has a different charging latency, efficiency, damage rate, authority, or recognition, those conditions must be modeled and rechecked.

## 7. Proposition B: a conservative abstraction transports safety in one direction

Exact quotients can be too demanding. Let \(q:X\to Z\) and let the abstract action alphabet be a subset of the concrete alphabet. Suppose:

1. Every action the abstract controller may choose at an abstract state is executable at every concrete state in that fiber.
2. \(q(F(x,u))\subseteq\bar F(q(x),u)\) for these actions.
3. \(q^{-1}(\bar K)\subseteq K\).
4. The concrete controller can obtain the abstract observation: \(\bar h(q(x))=g(h(x))\) for a declared function \(g\).

If an abstract observation policy guarantees \(\bar K\)-safety from an abstract initial set containing \(q(B)\), its implementation using \(g\) and the same actions guarantees \(K\)-safety from \(B\), assuming that implementation is available.

**Proof.** Action executability makes each concrete step available. By induction each projected concrete execution is an allowed abstract execution under the same abstract observation/action history. Abstract safety puts every projected state in \(\bar K\); the inverse-image inclusion puts every concrete state in \(K\). ∎

This proves a sufficient safety certificate. Extra abstract transitions or an overly small \(\bar K\) can create spurious failures, so abstract inability to guarantee safety need not prove concrete impossibility. Reissig, Weber, and Rungger's feedback refinement work gives a general prior treatment of controller transfer; the elementary statement here is intentionally narrower and also spells out the observation interface.

For action renaming or a many-to-one action abstraction, supply an implementation map \(\rho\). The selected concrete action must be determined by information available to the controller. An assertion \(\forall x\exists u_x\) is insufficient when different indistinguishable \(x\)'s require incompatible \(u_x\). If \(\rho\) consults the hidden concrete state, the proposed lift secretly adds information.

### Failed mapping: “there is a repair” loses who can choose it

There are two hidden safe states L and R, with the same observation, and failure \(\bot\). Both actions are available:

| State | action L | action R |
|---|---|---|
| L | L | \(\bot\) |
| R | \(\bot\) | R |
| \(\bot\) | \(\bot\) | \(\bot\) |

Let \(q(L)=q(R)=z\), \(q(\bot)=\bar\bot\). Each hidden state is safe forever when fully known. But no observation-based action is safe from the information set \(\{L,R\}\), already at one step.

The tempting quotient “\(z\) has a successful repair” is false as a control certificate. It substitutes \(\forall x\exists u\) for \(\exists u\forall x\). The conservative abstract transition for each action is \(\{z,\bar\bot\}\), making the failure visible. An implementation map that chooses L in hidden state L and R in hidden state R is unavailable to this observer.

Randomizing equally attains worst-case success probability one-half in this one-step example, not a guarantee. The finite verification confirms separate viability and failure of joint observation-based viability. This directly instantiates the earlier claim U05, rather than being a new law.

### Failed mapping: exact dynamics do not preserve the protected interest

Take two states “healthy” and “harmed,” each with only a self-loop. Map both to one abstract state. This is an exact transition and observation quotient if the observable labels agree. But for \(K=\{\text{healthy}\}\), no abstract set has inverse image equal to \(K\): the only inverse images are empty and both states. The safe predicate cannot be transported by this map.

Thus a quotient that preserves institutional output, persistence, or score can still erase a harmed person's condition. A normative preservation claim needs its own labels and assumptions. It cannot be inferred from structural equivalence on the labels chosen by an evaluator.

## 8. Aggregation may discard memory or intervening failure

Let a perfectly known deterministic Markov system cycle \(a\to b\to c\to a\), and observe \(q(a)=q(b)=0, q(c)=1\). With an initially uniform state, possible three-observation histories are 001, 010, and 100. At the second time, both histories 00 and 10 end in current observation 0, but their next observations are respectively 1 and 0. Therefore the current compressed state is not a sufficient first-order Markov state. The transition sums out of a and b to the “1” fiber differ (0 versus 1), violating (A2).

There are several valid responses, with different costs: retain history, add an information/belief state, use a non-Markov abstract model, or adopt a conservative nondeterministic model \(0\to\{0,1\}\). The last option preserves possible steps but adds impossible longer histories. Calling the same output a complete state would be the error.

Time aggregation is a separate issue. A concrete sequence with resource levels \(1\to0\to2\) can appear as a harmless increase \(1\to2\) when sampled every two steps. Endpoints do not preserve “never reach zero.” A macro-action abstraction must include its duration, all relevant intermediate safety conditions, incurred costs, and observation opportunities. This is why replacement latency and prefix liquidity cannot be silently discarded when mapping renewal models.

## 9. Proposition C: unrestricted future questions defeat any noninjective summary

Let \(H\) be the set of histories and \(s:H\to Z\) a noninjective summary. Then there is a binary future question \(f:H\to\{0,1\}\) for which no function \(g:Z\to\{0,1\}\) satisfies \(f=g\circ s\).

**Proof.** Choose distinct histories \(h_0,h_1\) with the same summary. Set \(f(h_0)=0\) and \(f(h_1)=1\), defining \(f\) arbitrarily elsewhere. A function of their common summary cannot return both values. Under equal prior mass on those two histories, even a randomized answer using the summary alone has average error one-half. ∎

This is an elementary logical limit, not a claim that every discarded detail will matter or that preserving all records is ethically or economically justified. For a declared family \(\mathcal Q\) of questions, the exact condition is weaker: each \(f\in\mathcal Q\) must be constant on every fiber. A summary can be perfectly sufficient for that family and cost less than the raw history. Expanding \(\mathcal Q\) can break sufficiency. New observation can also answer a question without reconstructing the lost history.

This links the previous U20 result about homogeneous versus time-varying switching models to the full-picture conjecture: future-proof sufficiency cannot be claimed without delimiting the future questions. It does not prohibit a theory from representing its own known compression and limits.

## 10. What can be invariant, and what cannot

The phrase “invariant under transformation” is incomplete until a transformation class is declared.

- Under bijective coordinate changes with commuting dynamics and transported predicates, trace properties are invariant by construction.
- Under Proposition A's exact quotient, the declared safety problem and preserved trace predicates are invariant. Carrier identity and unlisted interests are not.
- Under Proposition B's conservative abstraction, a certificate transfers in one direction. This is preservation, not equality of all properties.
- Under a unit conversion \(e'=\alpha e\), \(\alpha>0\), scaling both flows and the protected floor preserves the reserve inequality. Under an arbitrary nonlinear map, the additive balance needs a chain-rule transformation and may cease to have the same form.
- Under arbitrary model replacement there is no nonconstant invariant common to all objects if every object can be replaced by every other: invariance forces \(I(M)=I(N)\) for every pair. Restricting transformations is what makes a nontrivial invariant possible.

The resource balance and observation-limit results in the source record are not consequences of one another. Their common expression in \(X,F,h\) is organizational integration; a theorem linking them requires further joint assumptions about when information, resources, and authority permit the same action.

## 11. How the existing claims map into the core

| Earlier claims | Additional structure required | What this core contributes | What it does not establish |
|---|---|---|---|
| U01, U04, U16: reserve and deadline balances | Typed stock, identified flows, timing, protected floor, feasible action set | Explicit prefix-safe predicates and transition constraints | An accounting law for knowledge, legitimacy, or all resources |
| U02: shares do not identify total viability | Projection from absolute populations to shares; admissible model family | A concrete case where the viability predicate is not constant on fibers | That every observed correlation conceals collapse |
| U05: incompatible hidden responses | Observation channel and action-conditioned transitions | Proposition A/B transport and the hidden-repair counterexample | That more generic data or funds always resolve the conflict |
| U10–U11: functional replacement and pending work | Carrier cohorts, duration, work accounting, finance | Distinguishes carrier projection from retained function and intermediate safety | Safe handoff without latency/cost preservation |
| U20–U22: inherited evidence and admission limits | Histories, summary channel, candidate question family | Proposition C and non-Markov counterexample | Obligation to preserve every detail or automatic discovery of omitted questions |
| U24–U27: shutdown, recognition, recovery bridge | Stochastic law, reserves, credit rule, restart inputs | Typed separation of value, measured credit, access, and productive support | Empirical law of institutions or universal shutdown theorem |
| N01: agency and legitimate revision | Explicit protected interests, standing, procedures, conflicts | Prevents silent erasure during a map | A derivation of ethics from persistence |

## 12. Rejected formulations and remaining gaps

1. **Rejected: “Everything is a configuration and transformation, so the theory is complete.”** A notation that can label everything may still forbid nothing. Predictive content is in constrained transition/intervention laws, not the vocabulary.
2. **Rejected: “Any projection of a Markov world is a Markov world.”** The three-cycle counterexample refutes it.
3. **Rejected: “Each hidden case has a solution, so the observer has a solution.”** The hidden-repair example refutes it.
4. **Rejected: “Preserving behavior preserves what matters ethically.”** Preserved behavior is relative to declared labels; the healthy/harmed quotient refutes the unrestricted statement.
5. **Rejected: “Putting the evaluator in the state makes its evaluation authoritative.”** It makes its causal role representable, not justified.
6. **Rejected: “Changing a system's effective transition rule requires changing fundamental laws.”** Updating implemented parameters inside a joint model is enough for many cases; the joint model itself remains a hypothesis.
7. **Rejected: “A complete encoding of all models is a complete model of the world.”** Syntactic inclusion does not supply empirical truth, usable computation, or complete semantics.
8. **Gap: composition.** Arbitrary observation/transition interfaces are not automatically closed under feedback, shared noise, or simultaneous interactions. State augmentation, explicit internal variables, and timing conventions may be needed. Do not claim unrestricted compositionality for this minimal signature.
9. **Gap: causal structure.** A transition table alone supplies no account of which components can be separately intervened on. Causal abstraction needs an intervention map and a commuting distributional claim for the specified interventions.
10. **Gap: physical feasibility of the theorist.** A finite proof is a conditional statement in a metalanguage; modeling the proof's storage and uptake does not establish an internally accessible, omniscient validator. Work can proceed through bounded records and revision without claiming one.
11. **Gap: open-ended agency and normative conflict.** Current models can encode supplied alternatives and interests. They do not derive new legitimate interests, resolve conflicts, or ensure that excluded people can revise their representation.

## 13. Concrete next test

Extend one existing paid-inquiry model with two physically different evaluator carriers and a successor handoff. Construct three candidate summaries before observing results: (i) current score/output only, (ii) score plus reserve and current policy, and (iii) reserve, pending latency, relevant inherited evidence, action permissions, and evaluator-carrier state. Enumerate action-conditioned transitions in a finite version.

For each map, first test action availability, transition commutation, observation transport, protected-interest transport, and prefix costs. Where exactness fails, build a conservative abstraction and compare its safety certificate with the concrete belief-state calculation. Then remove only the distinctions demonstrated to be irrelevant. Freeze this map and test held-out parameter settings, including a successor with a different latency, a changed recognition rule, and an interest omitted by the original score.

Predictions that can fail: the declared exact map must preserve every checked action-conditioned projected trajectory law; the conservative map must never certify a concrete unsafe policy under its assumptions; including the hypothesized handoff variables should repair the particular failures they are meant to explain. If no useful reduction works, or the added variables fail to restore the claimed relation, reject that mapping or the finite model. Do not expand the state retrospectively and count the old prediction as confirmed.

This test distinguishes a reusable structure with genuine preservation content from unrestricted redescription. It is intentionally smaller than proving that every scientific or cultural account is a projection of one complete structure.

## 14. Evidence record and primary-source anchors

Read-only local references: the integrated-evolution README and claim register; its observability-and-correction memo; replacement-and-establishment memo; and model-revision-inheritance-math memo. They already distinguish conditional results from empirical hypotheses and normative commitments. No source file was modified.

- Reissig, Weber, and Rungger, *Feedback Refinement Relations for the Synthesis of Symbolic Controllers*, IEEE TAC 62(4), 2017; accessible [author preprint](https://arxiv.org/html/1503.03715). Definition V.2 and the controller-refinement results substantiate the established lineage for conservative action/transition preservation. The article also makes implementation information and composition issues explicit. Proposition B above is a small independently proved special case, with its own observation assumption, not a claim to reproduce their entire theorem.
- Chatterjee, Doyen, Henzinger, and Raskin, *Algorithms for Omega-Regular Games with Imperfect Information*, [2006 primary technical report](https://www2.eecs.berkeley.edu/Pubs/TechRpts/2006/EECS-2006-89.pdf). This anchors observation-history strategies and established incomplete-information game methods. The present computations use only finite-horizon sure safety and make no general statement about randomization for all objectives.
- Ravindran and Barto, *SMDP Homomorphisms: An Algebraic Approach to Abstraction in Semi-Markov Decision Processes*, IJCAI 2003, [author-hosted paper](https://wsai.iitm.ac.in/~ravi/papers/IJCAI03.pdf), also indexed on [Barto's publication page](https://people.cs.umass.edu/~barto/pubs-Barto.html). This is a prior-art anchor for algebraic abstraction in sequential decision processes. The search-indexed author text was available; direct PDF extraction returned an error in this run, so no claim here depends on an unchecked detailed theorem from it.

All derivations in sections 6–9 can be checked directly without appealing to those papers. The accompanying `formal_verify.py` uses the standard library and writes `formal_checks.json`. Result: 16 exact transition checks, 396 finite safety-equivalence checks, the incompatible-action example, the history-loss example, and an explicit false safety certificate from the healthy/harmed quotient passed. These are proof-supporting toy calculations, not empirical findings.
