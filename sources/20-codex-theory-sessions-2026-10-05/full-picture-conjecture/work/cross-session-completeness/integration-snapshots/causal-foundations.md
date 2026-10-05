# Formal results for causally embedded revision

This appendix proves conditional results used in the [research synthesis](causal-foundations.md). The central result states when a smaller representation preserves specified intervention predictions; the other results delimit identification, finite memory, universal announced prediction, and the content of a bare dynamical description. These are elementary derivations or applications of established ideas, with no novelty claim.

The examples assume finite classical systems where stated. Their validity does not establish that all physics, cognition, institutions, or ethical judgment have this form. Source scope and open assumptions are recorded in [Sources and claims](sources-and-claims.md).

## The smallest useful formal commitment

Represent a bounded, discrete-time system by a state

\[
z_t=(w_t,c_t,r_t)\in Z,
\]

where `w` records the remaining modeled world, `c` the material configuration supporting observation and control, and `r` declared enabling resources. This is a modeling partition, not an assertion that the components have separate ontological kinds. Institutional `c` can extend across people, documents, software, and practices. Its functional readouts may include a world model `m(c)`, policy `π(c)`, evaluative purpose `g(c)`, and mechanism configuration `κ(c)`. These readouts need not be independent or occupy disjoint physical substrates. A Cartesian product is not required: only physically admitted triples belong to Z.

A world model supplies represented consequences or relationships. A policy supplies an information-to-action rule. An evaluative purpose supplies a ranking, target, or acceptance criterion used by some process. These roles are distinct even where one physical state supports all three. Merely naming a state component “a model” establishes no semantic correctness. A proposed interpretation needs a decoding rule, a task or referent, and evidence that the decoded content is used in the claimed causal role.

One possible operational factorization uses observations O, internal actions A, and updates:

\[
O_t=o(z_t,U_t^O),\quad
A_t=p(c_t,O_t,U_t^A),\quad
z_{t+1}=F(z_t,O_t,A_t,U_t^F).
\]

Model updating, policy revision, changed purposes, replacement of observation channels, and reorganization of institutions occur through the next `c`. Resource consumption and renewal occur through the next `r`. A kernel K(z′|z) can summarize the closed-loop process if z is sufficient for the modeled future and the noise assumptions support that Markov property. Time independence and finiteness are additional assumptions, not consequences of physical realization. History augmentation can make an arbitrary process Markov on a growing state space; it does not establish a finite sufficient state or a practically usable theory.

The factorization chooses an event order. It is a tractable subclass, not a proof that every physical process has such a discrete causal ordering. Dependence among noise variables must be represented or acknowledged. The variables called exogenous are external to this model's equations, not necessarily external to the world.

### Intervention semantics must be supplied separately

For an admitted intervention protocol i, let P^i(z′|z) denote the causal transition kernel that protocol produces. **Do not equate this automatically with an observational conditional distribution.** A physical implementation, modular structural model, randomization argument, or other identification assumptions must justify the interpretation. A kernel by itself specifies transition probabilities; it does not uniquely supply the effects of changing mechanisms or the coupling among unrealized alternatives.

The ordinary internal action A is produced inside the causal account. An intervention index i belongs to the analyst's comparison of protocols. When an actual experiment occurs, the equipment, selection procedure, action, costs, and side effects can all be included in a larger state. This removes the need for an actor outside nature while preserving the need to say which protocol is varied and what is held fixed. Conditioning on an endogenous choice still differs from replacing its assignment mechanism.

### Effective mechanism change as state change

If mechanism settings κ range over a declared set and the next process state obeys `x′=F_κ(x)`, while `κ′=R(x,κ)`, the augmented update is simply

\[
(x,\kappa)\longmapsto(F_\kappa(x),R(x,\kappa)).
\]

Thus a fixed update rule can implement changing effective mechanisms. This is a representation construction, not a substantive law of self-organization. It says neither that fundamental physical laws change nor that mechanism changes are fictitious. At a declared interface, replacing κ can change the responses to interventions. Conversely, a microscopic change that preserves those responses need not count as a change in effective mechanism.

A finite κ-set predeclares the available effective mechanisms. Using arbitrary strings or programs enlarges what can be generated, but still supplies an interpreter and physical capacities. No finite-state example establishes unrestricted novelty, conceptual completeness, or the ability to represent all future purposes.

## Proposition A on precisely what an abstraction preserves

**Status:** elementary action-wise strong lumpability / controlled-process quotient, closely related to stochastic bisimulation and causal abstraction.

Let Z and X be finite, h:Z→X surjective, and I a finite set of admitted intervention labels. Assume every i∈I is admitted in every state. The result also works with state-dependent admissibility if the available labels are identical throughout each fiber h⁻¹(x), or if failed/unavailable attempts are explicitly included in the transition law.

There exists a family of macro kernels \(\bar P^i(x'\mid x)\) satisfying

\[
\sum_{z':h(z')=x'}P^i(z'\mid z)
=\bar P^i(x'\mid h(z))\tag{A1}
\]

for all z,i,x′ **if and only if** each left side is the same for every pair z₁,z₂ with h(z₁)=h(z₂). For any initial distribution μ, and any one fixed protocol-selection policy that depends only on the macro-observation history, the joint macro path law generated by the microscopic process equals the path law from \(h_*\mu\) and \(\bar P\), under the independent observation chronology stated below, or the stronger conditional or joint compatibility stated in the final section.

A particularly simple sufficient observation condition is \(O_t\sim Q(\cdot\mid h(z_t))\), with its specified randomization independent of the next transition conditional on state and chosen intervention. If observation and transition noise have additional dependence, preserve their joint kernel instead of assuming that matching their separate marginals is enough.

Declared outcomes must also factor through h. A finite-horizon payoff \(L=\ell(x_0,i_0,x_1,\ldots,x_H)\) has equal distribution and expectation in the two models. This includes a specified safety event or repair event expressible in macro variables. It does not include unrepresented microscopic harm or costs.

**Proof.** Necessity follows by choosing a point-mass initial condition at each of z₁ and z₂ and making intervention i for one step. For sufficiency, define \(\bar P^i\) by the common sum. This is a probability kernel. Conditional on any compatible macro history and chosen i, the microscopic conditional distribution is a mixture over the current fiber. Every member of that mixture has the same pushed-forward next-state distribution by (A1); hence the mixture does too. Factored observation channels and the common history-based policy give the same next observation and action distributions. Induction establishes the finite path law. A measurable function of that path therefore has the same law. □

**What is not claimed.** An unrestricted microscopic controller can inspect information omitted by h and can select interventions using it. Such controllers are not automatically identified with the specified macro-observation policy class. The theorem is not a claim about equal optimal values over differently informed policy classes. It also preserves interventional path distributions, not every cross-world counterfactual.

**Matrix form.** If H(z,x)=1{h(z)=x}, condition (A1) is

\[
P^iH=H\bar P^i\quad\text{for every admitted }i.
\]

This makes the class of representation transformations explicit. A bijective state relabeling h always has the corresponding transformed kernel; intervention labels, observation channels, and evaluative quantities must be transformed consistently. Such isomorphism invariance is exact but modest. A many-to-one h is substantive: it must satisfy (A1). Under arbitrary coarsening, no nonconstant property can generally survive; the constant map erases every distinction.

### Approximate extension useful for testing

Suppose a proposed macro family satisfies, uniformly for each z and admitted i,

\[
\left\|h_*P^i(\cdot\mid z)-\bar P^i(\cdot\mid h(z))\right\|_{TV}\le\varepsilon,
\]

with matching initial macro distributions, the same macro-observation policy, exact factored observation channels with the independent chronology specified in Proposition A, and 0≤ε≤1. Then the TV distance between joint macro path laws over H transitions is at most

\[
1-(1-\varepsilon)^H\le H\varepsilon.
\]

**Proof.** Until the two macro histories diverge, couple the common observation and policy randomization identically. Convexity preserves the ε bound after conditioning on a macro history and mixing over its microscopic states. A maximal coupling of the next macro states fails with probability at most ε. The probability of no failure through H transitions is at least (1−ε)^H. Coupling bounds path-law TV by the probability of any failure. □

For a path outcome bounded in [0,1], the expectation discrepancy obeys the same bound. If observations or interventions themselves are only approximately preserved, their errors also need accounting. An average one-step fit over a convenient training distribution does **not** establish the uniform bound; unvisited microscopic states may defeat the abstraction.

### Worked exact and failed abstraction

Let z=(x,n)∈{0,1}², h(z)=x, and i∈{0,1}. Set

\[
\Pr(x'=1\mid z,do(i))=(1+x+i)/4,\qquad n'=n\mathbin{\mathrm{xor}}i.
\]

The nuisance bit changes, but the macro response is independent of n. Equation (A1) holds. The verification script checks all eight state/intervention combinations and all 64 deterministic two-step full-macro-history policies from all four initial microstates (256 path-law comparisons), using exact rational arithmetic.

Now change the i=1 response to x′=n. States (0,0) and (0,1) share macro state zero but their next-macro success probabilities are zero and one. The quotient fails. Averaging n under a selected observational distribution could still produce a plausible macro transition; it would not establish intervention-relative equivalence for both realizations.

**Primary precedents and scope.** [Givan, Dean, and Greig (2003), *Equivalence notions and model minimization in Markov decision processes*](https://cs.brown.edu/people/tdean/publications/archive/GivanetalAIJ-03.pdf), section 3.2 and Theorems 5–7, develop stochastic bisimulation preserving block transitions, rewards, and appropriate policy/value properties. The present proof is a simpler finite kernel statement. [Rubenstein et al. (2017), *Causal Consistency of Structural Equation Models*](https://arxiv.org/abs/1707.00819), Definition 3 and Theorem 6, formulate consistency via state and intervention maps. [Beckers and Halpern (2019), *Abstracting Causal Models*](https://www.cs.cornell.edu/home/halpern/papers/abstraction.pdf), criticize permissive mappings and distinguish stronger abstraction conditions. Our kernel theorem must not be identified with all of their structural definitions.

## Proposition B on why shared dynamics does not identify causal meaning

**Status:** two elementary counterexamples to universal identification; no novelty claim.

### B1. Identical observation, different intervention

Let U be a fair bit. Model B1 has X=U and Y=X. Model B2 has X=U and Y=U. Both produce exactly the same observational distribution: (X,Y) equals (0,0) or (1,1) with probability one half each. Under do(X=1), B1 has Y=1 with certainty; B2 has Y=1 with probability one half.

Therefore no procedure given only that joint observational law can always choose the correct intervention prediction over this model class. If it gives one answer on the common input it must fail on at least one model. More data of the same observational kind do not remove the ambiguity. Experimental variation or justified structural restrictions can.

### B2. Even all treatment marginals need not determine same-unit counterfactuals

Let treatment X be randomized independently of U, both fair bits. In B3 set Y=U for both treatments. In B4 set Y=U xor X. Both have independent fair X,Y observationally, and in both

\[
\Pr(Y=1\mid do(X=0))=\Pr(Y=1\mid do(X=1))=1/2.
\]

Nevertheless B3 has \(\Pr(Y_0\ne Y_1)=0\), whereas B4 has \(\Pr(Y_0\ne Y_1)=1\). Given factual X=0,Y=0, the counterfactual Y₁ equals zero in B3 and one in B4. Treatment-response marginals do not specify how the same latent individual is coupled across treatments. This example concerns the complete family of X-treatment interventions in this simple model, not an unspecified family of every conceivable experiment.

**Implication.** An internal observer being part of the same world does not automatically tell it what would happen under a different policy, much less what would have happened to this particular system under an unrealized history. The analyst's own causal model requires assumptions too. A transition model, an intervention model, and a counterfactual model are different levels of supplied structure.

**Primary precedent.** [Pearl (2009), *Causal inference in statistics: An overview*](https://ftp.cs.ucla.edu/pub/stat_ser/r350-reprint.pdf) explains the structural assumptions used for intervention and counterfactual queries; section 3.4 develops counterfactual analysis. The explicit bit models and their arithmetic above are independently checked examples, not attributed as quotations or as a new theorem.

## Proposition C on preserving answers is relative to future questions

**Status:** elementary pigeonhole / exact-encoding result. It formalizes, rather than supersedes, the reference workspace's evidence-inheritance distinction.

Let H be a finite set of possible histories, Q a declared set of later queries, and a:H×Q→A the required correct answer. Define

\[
h\sim_Q h'\quad\Longleftrightarrow\quad
 a(h,q)=a(h',q)\text{ for every }q\in Q.
\]

A memory encoder e:H→M admits a decoder d:M×Q→A answering every query exactly if and only if

\[
e(h)=e(h')\quad\Longrightarrow\quad h\sim_Qh'.
\]

Consequently the smallest possible number of memory states is the number of distinct Q-answer vectors, namely |H/∼Q|. A b-bit memory can provide the guarantee only if \(2^b\ge|H/\sim_Q|\).

**Proof.** If two histories share a code, the decoder receives the same input for any given query and must give the same answer. Thus their answer vectors must coincide. Conversely, assign one code to each distinct answer vector and decode its query component. This uses exactly one state per equivalence class and meets the lower bound. □

Randomized encoding with zero error for every history and query cannot evade the bound: two different answer classes must have disjoint supports over memory states. Any shared memory value of positive probability would require the same decoder output to be two different answers for a separating query. All information available at decoding time, including shared random seeds if accessible and informative, belongs in the decoding inputs; hidden auxiliary storage is not free.

**Example.** Histories are 00,01,10,11. If the only future query is parity, one bit suffices. If the later query may ask either coordinate, all four answer vectors differ, so two bits are required for universal zero-error recovery. The script enumerates all sixteen encoders into one bit and all sixteen decoders for the two queries. None is error-free; the smallest error under uniform histories and uniform queries is 1/4. Storing both bits permits exact recovery.

**Limits.** This does not imply that every history should be preserved. Approximate answers, restricted likely queries, costs, external remeasurement, and deliberate forgetting can change the optimal choice. It says that reinterpreting a code cannot universally reconstruct distinctions which the code erased. Adding a new query class can invalidate an old sufficient representation without any physical law changing.

## Proposition D on how an announced exact prediction can defeat its own guarantee

**Status:** elementary diagonal counterexample with explicit interface assumptions.

Consider any physical or computational protocol required to announce a bit b before a responsive system produces its final bit y. Suppose the responder receives b and the admitted system class contains the rule y=1−b. No predictor can be correct on every member of that class while always announcing such a bit before the response.

**Proof.** On that responder, correctness requires b=y=1−b. Neither Boolean value satisfies this equation. Randomizing which bit is announced does not help: each realized announcement is contradicted. □

There is no contradiction in the deterministic dynamics: the combined system evolves perfectly well, with a mistaken prediction. The contradiction is in the joint demand for universality, exact advance announcement, and an admitted response that negates that announcement.

**Limits and counterexamples to overstatement.** Predictors can succeed for restricted system classes, predict aspects unaffected by their output, keep predictions inaccessible to the responder, give useful probabilities, or identify conditions rather than a universally correct exposed bit. A responder copying b creates no such contradiction. Internal self-models and useful reflexive control are therefore allowed. Replacing exact bit prediction by distributional prediction changes the problem; for example, a responder drawing Bernoulli(1−p) has a self-consistent forecast p=1/2.

**Primary precedent, carefully delimited.** [Wolpert (2008), *Physical limits of inference*](https://arxiv.org/abs/0708.1362) models physical inference through setup/conclusion functions. Its Proposition 1(ii) and Theorem 1 establish different, broader formal limits under its own definitions; Theorem 1 specifically requires setup-distinguishability. This appendix proves only the elementary announced-bit result. The paper itself cautions that restricted inference tasks can be possible; it should not be cited as making ordinary prediction impossible.


## Proposition E on fitting any finite trace

**Status:** elementary construction showing lack of empirical restriction.

Given any finite observed sequence \(x_0,\ldots,x_T\), introduce distinct states \(z_t=(t,x_t)\), define \(F(z_t)=z_{t+1}\) for \(t<T\), and let \(F(z_T)=z_T\). Projection onto the second coordinate reproduces the sequence exactly. Timestamping distinguishes states even if the same observed value recurs.

Consequently the assertion that there exists some state space and update law reproducing a history cannot, by itself, rule out any finite observed history. Calling a coordinate an observer does not strengthen this restriction. This construction is not identification of the true causal process and gives no intervention predictions. Restrictions on variables, update families, resources, information, and interventions must be supplied independently of the trace if the model is to face a discriminating test.

## Proposition F on descriptive and evaluative underdetermination

**Status:** logical observation conditional on no additional normative premises; not a complete metaethical theorem.

Suppose a descriptive model permits outcomes \(u\) and \(v\). An external assessment can rank \(u\) above \(v\), or rank \(v\) above \(u\), without changing the descriptive transition equations. Those equations alone therefore do not select the assessment. Even if the model includes every realized evaluative statement and goal update, identifying the judgments that occur is different from establishing which judgments have justified authority.

This does not establish that moral truths are impossible, that values are arbitrary, or that causal facts do not matter to practical reasoning. Once commitments are specified, causal evidence can show that an action fails them. The institutional example illustrates this distinction concretely: reversing the goal achieves its new internal criterion with probability one while reducing success on the original criterion to zero.

## Additional counterexamples with direct calculations

### Effective response and represented response

For binary physical wiring \(q\), represented wiring \(m\), and goal \(g\), define \(a=g\oplus m\) and \(x'=a\oplus q\). Then \(x'\oplus g=m\oplus q\), proving that the declared target is reached exactly when \(m=q\). The truth table covers all eight assignments. A change in \(q\) changes the physical response to fixed action; a change in \(m\) changes the controller's response to its information; changing \(g\) changes the target. The same action-to-outcome graph can hold across different wiring modes.

### Observational solvability and intervention solvability

Over the reals, \(X=Y+Z\), \(Y=X\), \(Z=X+1\) imply \(Z=0\) and \(X=Y=-1\). This proves uniqueness directly. Under \(do(Z=1)\), the remaining equations instead imply \(X=X+1\), which is impossible. Finite enumeration is only a sanity check; this algebra proves the general assertion.

### Physical devices and ideal interventions

Let a device setting determine \(X=J\), a collateral effect \(B=J\), and outcome \(Y=X+B\). From baseline \(J=0\), ideal \(do(X=1)\) produces \(Y=1\), whereas operating the device through \(do(J=1)\) produces \(Y=2\). The second protocol cannot be identified with the first without accounting for the collateral pathway.

### Aggregated intervention ambiguity

Let \(Y=X_1-X_2\) and \(S=X_1+X_2\), with binary independently settable inputs. Both \((X_1,X_2)=(1,0)\) and \((0,1)\) implement \(S=1\), but produce outputs 1 and -1. Thus a macro intervention named “set S to one” does not have an implementation-independent effect here. A particular implementation or lottery can define it, but that choice is part of its meaning.

### Mutual dependence and restart

The update \((A,B)\mapsto(B,A)\) preserves both \((0,0)\) and \((1,1)\) and swaps the other two states. A strongly connected dependency graph therefore does not imply recovery from a depleted state. A restart route must actually be present in the dynamics and available under the information and resource constraints.

## Verification record

All three retained verification programs use Python's standard library and exact finite arithmetic or enumeration. Root reran them after reviewing the proofs. The general propositions rest on the written arguments; finite examples do not prove unrestricted results.

| Check | Scope | Result |
|---|---|---|
| Controlled quotient | Eight state and intervention combinations | Exact equality |
| Macro path preservation | All 64 deterministic two-step macro-history policies from each of four initial microstates | 256 exact comparisons passed |
| Failed quotient | Two states in one macro group under one intervention | Next-state probabilities 0 and 1 |
| Observational identification | Same observed law, different intervention response | Success probabilities 1 and 1/2 |
| Counterfactual identification | All nine perfect-intervention regimes on the two observed binary variables | Equal distributions; probability of changed individual outcome 0 versus 1 |
| One-bit archive | 16 encoders and 16 decoders for four histories and two coordinate queries | No zero-error code; minimum uniform query error 1/4 |
| Announced prediction | Both announced bits with an opposite-bit responder | Both guarantees fail |
| Wiring and represented wiring | All eight binary assignments | Matches target exactly when representation matches wiring |
| Institutional procedure | Six arrangements, each in both possible hidden conditions | Success rates 1, 1/2, 1/2, 1/2, 1/2, 0 |
| Internal amendment | Blocked deployment with a three-unit budget, in both hidden conditions | Success 1 with the amendment channel, 1/2 without it |
| Mutual-dependence update | All four binary states | No restart from zero state |

The approximate-abstraction bound is proved by coupling, not validated by a fitted simulation. The trace-fitting and evaluative propositions are constructive logical arguments. No empirical measurements, trained-model benchmark, or human peer review were conducted.

Reproduction files are retained in this task's `work/` directory: `verify_formal_foundations.py`, `verify_causal_formalisms.py`, and `verify_examples.py`, together with their JSON results. Run these programs with Python 3 from the task directory. They require no third-party packages. The scripts are calculations supporting this document, not additional scientific evidence.

## Assumptions required to use the abstraction theorem

A mathematical label for a protocol is not proof of its implementation. If a macro action corresponds to different micro actions, specify a feasible rule that selects its implementation using the implementer's available information. The existence of some successful action in each hidden state does not imply that the actor can choose the right one. One can instead define each intervention label as an already specified complete protocol, with its failures, internal decision rules, costs, and timing included in the transition.

The observation condition also concerns chronology. If a sampled observation is stored in the next memory state, or observation and transition noise are correlated, matching an observation marginal and an unconditional state-transition marginal separately is insufficient. Include the observed sample in the current state, use the appropriate conditional transition, or preserve the joint observation-transition kernel. Proposition A assumes the simple independent chronology it explicitly states; a different chronology requires the corresponding stronger matching condition.

For an explicit observation-first generalization, require \(O(o\mid z)=\bar O(o\mid h(z))\) and, for every supported observation and admitted intervention,

\[
\left\|h_*K^i(\cdot\mid z,o)-\bar K^i(\cdot\mid h(z),o)\right\|_{TV}\le\varepsilon.
\]

The same policy selects its intervention after the same preserved observation. Coupling that observation and policy choice identically, then using the conditional bound to couple the next macro state, gives the same \(1-(1-\varepsilon)^H\) bound by induction. The exact case is \(\varepsilon=0\). This formulation permits observation-dependent memory updates. Exact equality of appropriate joint kernels can also establish exact preservation, but a small fixed-intervention joint error alone need not give the same error bound under observation-adaptive choice; the conditional requirement avoids that gap.

For a counterexample to separate-marginal matching, take a fair observation \(o\). Let one system produce \(x'=o\oplus i\) and another \(x'=(1-o)\oplus i\). Under each fixed \(i\), both observation marginals and both next-state marginals are fair. Choosing \(i=o\) nevertheless makes the first outcome always zero and the second always one. Their joint observation-transition relationships differ.

Other assumptions remain empirical: sufficient state, correct kernel estimates, stable intervention implementation, chosen observation and outcome maps, stated horizon, and boundary support. The theorem certifies the implication from those assumptions. It does not certify that a real institution satisfies them.
