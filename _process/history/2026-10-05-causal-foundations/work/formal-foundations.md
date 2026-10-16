# Formal foundations: embedded revision, abstraction, and finite limits

Research memo, 5 October 2026. Prepared for integration into the causal-foundations session. All mathematical claims below are conditional; none is claimed novel. The existing integrated-evolution README and claim register were read as reference only. In particular, its U05 already establishes an indistinguishability limit for safe action, and its later inheritance work already identifies query-relative information loss. The present memo does not relabel those insights as discoveries.

## 1. The smallest useful formal commitment

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

## 2. Proposition A: precisely what an abstraction preserves

**Status:** elementary action-wise strong lumpability / controlled-process quotient, closely related to stochastic bisimulation and causal abstraction.

Let Z and X be finite, h:Z→X surjective, and I a finite set of admitted intervention labels. Assume every i∈I is admitted in every state. The result also works with state-dependent admissibility if the available labels are identical throughout each fiber h⁻¹(x), or if failed/unavailable attempts are explicitly included in the transition law.

There exists a family of macro kernels \(\bar P^i(x'\mid x)\) satisfying

\[
\sum_{z':h(z')=x'}P^i(z'\mid z)
=\bar P^i(x'\mid h(z))\tag{A1}
\]

for all z,i,x′ **if and only if** each left side is the same for every pair z₁,z₂ with h(z₁)=h(z₂). For any initial distribution μ, and any one fixed protocol-selection policy that depends only on the macro-observation history, the joint macro path law generated by the microscopic process equals the path law from \(h_*\mu\) and \(\bar P\), provided observation channels factor through h and are coupled with the same chronology in both models.

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

with matching initial macro distributions, the same macro-observation policy, exact factored observation channels, and 0≤ε≤1. Then the TV distance between joint macro path laws over H transitions is at most

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

## 3. Proposition B: shared dynamics does not identify causal meaning

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

**Primary precedent.** [Pearl (2009), *Causal inference in statistics: An overview*](https://ftp.cs.ucla.edu/pub/stat_ser/r350-reprint.pdf) explains the structural assumptions used for intervention and counterfactual queries; section 4 develops counterfactual analysis. The explicit bit models and their arithmetic above are independently checked examples, not attributed as quotations or as a new theorem.

## 4. Proposition C: preserving answers is relative to future questions

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

## 5. Proposition D: an announced exact prediction can defeat its own guarantee

**Status:** elementary diagonal counterexample with explicit interface assumptions.

Consider any physical or computational protocol required to announce a bit b before a responsive system produces its final bit y. Suppose the responder receives b and the admitted system class contains the rule y=1−b. No predictor can be correct on every member of that class while always announcing such a bit before the response.

**Proof.** On that responder, correctness requires b=y=1−b. Neither Boolean value satisfies this equation. Randomizing which bit is announced does not help: each realized announcement is contradicted. □

There is no contradiction in the deterministic dynamics: the combined system evolves perfectly well, with a mistaken prediction. The contradiction is in the joint demand for universality, exact advance announcement, and an admitted response that negates that announcement.

**Limits and counterexamples to overstatement.** Predictors can succeed for restricted system classes, predict aspects unaffected by their output, keep predictions inaccessible to the responder, give useful probabilities, or identify conditions rather than a universally correct exposed bit. A responder copying b creates no such contradiction. Internal self-models and useful reflexive control are therefore allowed. Replacing exact bit prediction by distributional prediction changes the problem; for example, a responder drawing Bernoulli(1−p) has a self-consistent forecast p=1/2.

**Primary precedent, carefully delimited.** [Wolpert (2008), *Physical limits of inference*](https://arxiv.org/abs/0708.1362) models physical inference through setup/conclusion functions. Its Proposition 1(ii) and Theorem 1 establish different, broader formal limits under its own definitions; Theorem 1 specifically requires setup-distinguishability. This memo proves only the elementary announced-bit result. The paper itself cautions that restricted inference tasks can be possible; it should not be cited as making ordinary prediction impossible.

## 6. How to classify revisions without treating every difference as structural

These are operational distinctions, relative to declared interfaces and timescales:

| Change | Sufficient description | What it does not establish |
|---|---|---|
| Ordinary state | z changes under the current effective response family | A changed effective mechanism |
| Effective mechanism | The intervention-to-outcome response family changes at the fixed interface | A change in fundamental laws |
| Representation | Decoder, categories, retained distinctions, or model family changes | Improved truth or recovered erased information |
| Policy | The information-to-action response changes | A new world model or purpose |
| Evaluative purpose | The actual ranking/acceptance procedure changes | Ethical progress or legitimate consent |
| Material realization only | Microscopic changes preserve the declared response family | No microscopic change occurred |

To compare two mechanism settings κ, fix the intervention set I, initial conditions/context class C, observation/outcome map h, horizon H, and a tolerance. Call them equivalent for that specification if their declared outcome path distributions agree (or stay within tolerance) across I and C. Enlarging I, changing h, or lengthening H can break equivalence. This is the expected behavior of a relative notion, not an inconsistency.

Goal representations g are ordinary causal variables in the dynamics; normative evaluation of a goal revision is an additional question. If one assesses g′ using only g′, any successful alteration of standards can certify itself. If one assesses g′ using a fixed criterion J, J is an explicit supplied commitment. If an institutional procedure revises J, the legitimacy of that procedure remains a normative premise or further object of argument. Endogenizing evaluation does not eliminate this distinction.

## 7. What the framing adds, and what it leaves open

The strong defensible methodological demand is **explanatory inclusion**: the processes through which distinctions are detected, predictions formed, actions selected, rules maintained, and purposes revised should themselves be included wherever their operation changes the outcome being explained. It rules out treating observation, archives, computation, authority, or revision as costless infallible capacities by default.

By itself the assertion that everything can be placed in one state-transition description is weak. Almost any recorded process can be represented using sufficiently rich histories and a retrospectively fitted transition rule. A useful theory must restrict the variables, law family, feasible interventions, observation channels, resources, and admissible approximation error independently of the result. Those restrictions generate predictions that can fail.

Concrete failure criteria include: a proposed abstraction fails an admitted intervention; a proposed finite memory is insufficient for its declared queries; an allegedly available repair lacks required physical resources or access; a specified policy class cannot distinguish states requiring incompatible responses; or a reported self-prediction guarantee includes a feasible response that defeats it. Failure of a particular formalization does not disprove causal realization itself.

Physical realization, causal closure, and classical finite-state causal modeling are distinct theses. This memo assumes a useful finite classical representation for the examples. It provides no argument that this covers quantum causal scenarios, all continuous dynamics, universal causal closure, consciousness, the ontology of laws, or the ultimate constitution of possible worlds. [Bongers et al. (2021), *Foundations of structural causal models with cycles and latent variables*](https://arxiv.org/abs/1611.06221) establish solvability-dependent results for cyclic SCMs; feedback does not invalidate causal modeling, but cycles require explicit conditions rather than automatic DAG assumptions.

The phrase “furthest we can go” therefore receives no mathematical endorsement here. A causal account can be a broad explanatory framework while leaving ontology underdetermined, empirical models fallible, and ethical purposes explicitly unsettled. The propositions constrain particular realizations and claims. They do not derive a universal direction of becoming, moral value from persistence, or alignment from causal connectedness.

## 8. Verification and remaining work

`work/verify_formal_foundations.py` uses only Python's standard library, exact rational arithmetic, and exhaustive finite enumeration. `work/formal-foundations-checks.json` records all checks as passed. Checks validate the worked finite examples; the general results rest on their stated proofs, not on simulation.

Open research priorities: test approximate intervention-preserving abstractions on a specified maintenance/revision system; specify competing purposes and rights without equating them to one scalar; model the costs and dynamics of acquiring a better representation; and distinguish protocol identification from proof that a physical intervention actually realizes that protocol. No external correspondence or changes to the reference workspace were made.

## Review addendum: observation-dependent memory updates

The synthesis's within-period update should in general be `K(z′|z,o,a)`, because an observation can alter stored evidence even when the chosen external action is unchanged. My initial functional equation F(z,O,A,U) permits this. Proposition A above deliberately imposes a narrower independent observation channel for its simple `P^i(z′|z)` statement; that assumption should not silently be extended to every system in the general proposal.

A general observation-first form replaces that restriction by two conditional compatibility conditions:

\[
O(o\mid z)=\bar O(o\mid h(z)),
\]

and, for every supported observation o and admitted i,

\[
h_*K^i(\cdot\mid z,o)=\bar K^i(\cdot\mid h(z),o).
\]

With approximate conditional equality uniformly bounded by ε in TV, the same sequential-coupling proof gives path-law distance at most `1−(1−ε)^H≤Hε`. The policy may select i after seeing o; observations are coupled first, actions second, and next states third. An equivalent implementation is to augment state with the realized observation and use explicit sensing/decision phases. These are ordinary causal experiments: the current observation law must not depend on the intervention chosen only afterward.

Matching only separate observation and next-state marginals does not suffice. Let o be a fair bit, and compare the updates `x′=o xor i` and `x′=(1−o) xor i`. Every fixed-i next-state marginal is fair, and both observation marginals are fair. Nevertheless the policy i=o produces x′=0 in the first model and x′=1 in the second. The missing quantity is observation/transition dependence.

For **exact** matching, preserving the full joint `(o,x′)` distribution for every fixed i is an alternative sufficient condition. For an **approximate** theorem with observation-adaptive i, a TV bound on each fixed-i joint distribution alone need not preserve the same ε constant: the policy can select the action whose error is concentrated on the observation just received. For example, compare `x′=0` with `x′=1{o=i}`, with o fair and i binary. Each fixed-i joint discrepancy is 1/2, but i=o yields a path discrepancy of 1 in one step. Use the conditional uniform bound above, or directly bound all admitted observation-adaptive one-step protocols.

The synthesis's claim about all nine perfect interventions on two observed binary variables (A,Y) in the counterfactual example is correct: the null intervention, two A settings, two Y settings, and four joint settings all agree. Under do(Y=y), both models retain fair A. This does not include interventions on latent U.
