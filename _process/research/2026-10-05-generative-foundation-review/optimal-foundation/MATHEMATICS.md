# An optimal representation under an explicit causal contract

5 October 2026. Mathematical contribution to the revision of *Alignment as the Reproduction of Its Conditions*. This document does not edit or supersede the existing dossier. It supplies an alternative to presenting its eight-field evaluation tuple as foundational. The optimality results below have explicit objectives and comparison classes. They do not assert a unique optimal physical ontology or a universally best scientific theory.

## 1. What can now be established positively

The strongest defensible answer is not merely that unrestricted optimality is unavailable. Three useful optimality statements can be proved:

1. **Least information for the declared questions.** Merge exactly those histories having the same answers to every declared causal and evaluative query. This is the unique coarsest exact deterministic representation, up to re-encoding. Every other exact deterministic representation contains it as a function.
2. **A recursively maintainable predictive state.** When the queries include the continuation probabilities needed for conditioning on the actual next observation, the coarsest representation has a deterministic observation-based update. The state can be derived from response equivalence instead of chosen as a list of semantic categories.
3. **Fewest coordinates in a stated linear class.** If the history–test response matrix has finite rank \(r\), \(r\) independent test probabilities are an exact predictive basis with linear readouts and normalized linear updates. No ordinary linear-readout representation has fewer than \(r\) coordinates. With an explicit affine convention and a constant empty-test column, \(r-1\) variable coordinates suffice.

These are distinct optimization claims. They concern information refinement, recurrent prediction, and linear coordinate dimension, respectively. The unique coarsest strong quotient of a supplied finite physical Markov model is a fourth, different result already established in the dossier.

The proposed foundational object is therefore the **relationship between admissible interventions, available information, and retained consequences**. Coordinates are representations of that relationship. The earlier evaluation tuple can remain as a useful implementation and review checklist.

## 2. The basic factorization theorem

Let \(\mathsf H\) be a set of admissible contexts or histories. Let \(\Gamma\) be a declared query family. For each query \(\gamma\), let

\[
a_\gamma:\mathsf H\longrightarrow V_\gamma
\]

be its exact answer. Answers may be probabilities, distributions, intervention availability, current observed permissions, or vectors of consequences. Their existence comes from a supplied causal/evaluative contract; it is not inferred from having written their symbols.

Define the response profile and equivalence relation by

\[
Q_\Gamma(h)=(a_\gamma(h))_{\gamma\in\Gamma},
\qquad h\sim_\Gamma h'\iff Q_\Gamma(h)=Q_\Gamma(h').
\tag{1}
\]

A deterministic representation \(R:\mathsf H\to\mathsf R\) is **exact for \(\Gamma\)** when every answer can be decoded from it: \(a_\gamma=d_\gamma\circ R\). Equivalently, histories given the same representation must have the same answer to every declared query.

**Theorem 1: universal factorization and least retained information.** For every representation exact for \(\Gamma\), there is a unique map

\[
f:R(\mathsf H)\longrightarrow Q_\Gamma(\mathsf H)
\quad\text{such that}\quad Q_\Gamma=f\circ R.
\tag{2}
\]

Consequently the response-profile partition is the unique coarsest exact deterministic partition. When its image is finite, it has the fewest states among exact deterministic representations, and every other exact representation with that minimum finite number of states is bijectively equivalent to it.

**Proof.** Set \(f(R(h))=Q_\Gamma(h)\). If \(R(h)=R(h')\), exactness makes every component answer equal, so this definition is independent of the representative. Every point of \(R(\mathsf H)\) has a representative, proving uniqueness. Thus every exact partition refines the response partition. The response partition is itself exact by coordinate projection, establishing leastness and uniqueness. Surjectivity of \(f\) proves the finite cardinality bound; equality of finite cardinalities makes \(f\) a bijection. ∎

This proof establishes a universal property, not an efficient discovery algorithm. It is elementary sufficient-statistic/quotient reasoning. The full response profile can be infinite and expensive to calculate. For infinite state sets, equal cardinalities alone do not imply equivalent partitions; the refinement/factorization statement is the stronger appropriate claim.

**Corollary 1: memory entropy.** Choose any probability law \(\mu\) on a countable history set. For discrete representations with the stated entropy quantities defined,

\[
H_\mu(Q_\Gamma)\le H_\mu(R).
\tag{3}
\]

When both entropies are finite, the chain rule gives \(H(R)=H(Q_\Gamma)+H(R\mid Q_\Gamma)\). Equality holds exactly when \(R\) is itself determined by \(Q_\Gamma\), up to \(\mu\)-null histories. This is a distribution-relative memory claim, not a bound on computing the representation or describing its decoder. A sampled history distribution does not identify which counterfactual histories the exact contract must preserve.

**Corollary 2: invariance under re-encoding.** Suppose a bijection of histories and corresponding relabeling of queries preserve every answer. Then the induced response quotients are isomorphic. Spatiotemporal descriptions, graph descriptions, and stock/flow coordinates can therefore represent the same operational object when such a preservation correspondence is actually established. A coordinate change alone does not establish that interventions or information restrictions correspond.

**Corollary 3: expansion of the question.** If \(\Gamma\subseteq\Gamma'\), then \(\sim_{\Gamma'}\) refines \(\sim_\Gamma\). Previously merged histories may become distinguishable; the opposite cannot occur while all old queries and their meanings are retained. This is a precise form of situated optimality. It does not require a final fixed list of every future concern.

## 3. A causal and informational contract for recursive prediction

Theorem 1 permits arbitrary queries. Such a representation need not have a well-defined recursive update. A precise stronger result follows for controlled continuation queries.

We first use one **actual observation interface**, not an omniscient controller. Let \(U\) and \(O\) be finite alphabets of declared input proposals and delivered observations. A history has the form

\[
h=(o_0,u_0,o_1,\ldots,u_{t-1},o_t).
\]

Only positive-probability histories under some allowed intervention sequence are included in \(\mathsf H\). Initial observations have already been received. We may also include finitely many observable current contract labels \(\ell(h)\), such as displayed action permissions. Any next value of such a retained label must be included in the next observation packet, or its update must be included explicitly in the query contract. One must not silently assume the agent sees an unobserved safety or normative state.

The model supplies a causal next-observation kernel

\[
p(o\mid h,u),\qquad \sum_o p(o\mid h,u)=1.
\tag{4}
\]

The law can depend on the entire history; finite-state Markov structure and stationarity are not assumed. Histories retain the calendar or elapsed time whenever it affects the supplied law. All input proposals in \(U\) have specified responses; refusal or non-execution may be explicit observations. This convention does not make prohibited proposals legitimate. The permissible policy class and its permissions remain separately specified and preserved.

An action/observation **test** is a finite word

\[
\tau=(u_1,o_1,\ldots,u_n,o_n).
\]

Its success probability after \(h\) is

\[
d(h,\tau)=\prod_{k=1}^n
p(o_k\mid h u_1o_1\cdots u_{k-1}o_{k-1},u_k),
\qquad d(h,\varnothing)=1.
\tag{5}
\]

The inputs in (5) are **imposed** interventions. This is not generally the observational conditional probability of outputs given future actions in data generated by a feedback policy. Conditioning on a future action can condition on information acquired along the way. The causal response law must be supplied or identified under additional assumptions.

If a test encounters a zero-probability prefix, its probability is zero; later conditional rows on that impossible history need not be defined. Equivalently, assign arbitrary rows outside the admitted history set and stop treating them as identified causal claims. This convention makes (5) well-defined without claiming to condition on a null observation.

Define \(Q(h)\) by all these test probabilities, together with the retained current observable labels. The query family includes every finite continuation and every prefix needed below.

## 4. The recursive optimality theorem

**Theorem 2: minimal exact controlled predictor.** For the contract of Section 3:

1. If \(Q(h)=Q(h')\), then the next-observation distributions agree for every input.
2. Whenever that common next-observation probability is positive,
   \[
   Q(huo)=Q(h'uo).
   \tag{6}
   \]
3. Hence there are well-defined functions
   \[
   \widehat p(o\mid q,u),\qquad \delta(q,u,o),
   \]
   with \(Q(huo)=\delta(Q(h),u,o)\) on all possible updates. The predictor is driven only by the actual input and delivered observation.
4. Every exact deterministic predictor whose state is a function of the admitted history refines \(Q\). Therefore \(Q\) is the unique coarsest recursively updateable exact predictor, up to state naming. If its image is finite, it has the minimum number of states in this class.

**Proof.** The one-step tests give statement 1. For any continuation test \(\tau\), causality and the product rule give

\[
d(huo,\tau)=\frac{d(h,(u,o)\tau)}{d(h,(u,o))}
\quad\text{whenever }d(h,(u,o))>0.
\tag{7}
\]

Both numerator and denominator agree at equivalent histories. Thus every continuation probability agrees after the common observed extension. Retained next labels agree because they are delivered in the observation packet or explicitly preserved by the stipulated update contract. This proves (6) and makes \(\delta\) independent of the representative. Transitions with zero denominator never occur from the given predictive state; assign arbitrary values there without treating them as identified predictions. Iterating \(\widehat p\) and \(\delta\) reproduces every finite test probability by (5). Every exact competing representation must refine \(Q\) by Theorem 1, while \(Q\) itself is recursive, proving statement 4. ∎

There is a finite such exact predictor **if and only if** this response equivalence has finitely many classes. The reverse implication is the construction above; the forward implication is the finite cardinality bound. A finite number of generating rules does not guarantee this property.

The theorem is a controlled, stochastic residual-future construction in the tradition of Nerode equivalence, causal states, and predictive-state representations. It does not claim a newly discovered general minimization principle. Its role here is to replace unexplained coordinate choice with a declared preservation problem and an exact least-information solution.

### 4.1 Why arbitrary selected queries are not enough

Suppose a representation retains only the next-observation probability. Two contexts both emit zero on the next step; after that common observation, one emits zero forever and the other emits one forever. Their one-step answer profiles agree now but differ after the same update. No deterministic update of the one-step profile can reproduce both.

The missing condition is continuation closure. One can repair a finite query family by adding the prefix/conditioning queries needed to update it, potentially without termination. It is not valid to assume every coarsest answer profile is already a state of a generative Markov process.

### 4.2 From imposed input words to adaptive policies

Fix an observation-admissible continuation policy, including its initial memory and independent private randomization. For a realized finite action/observation path, the joint probability under that policy is

\[
d(h,(u_1,o_1,\ldots,u_n,o_n))
\prod_{k=1}^n
\pi_k(u_k\mid o_{1:k-1},u_{1:k-1},m_0).
\tag{8}
\]

Here \(m_0\) includes any permissible past information the continuing controller retains. The causal response factor and the policy factors are the same in an exact predictive implementation started from the corresponding history and memory. Summing path probabilities proves equality of every finite event under that continuation policy. Consistent finite-cylinder probabilities determine the infinite path law, so measurable infinite-horizon events agree too.

This does not mean that two distinct pasts assigned the same predictive environment state must cause one fixed historical policy to choose the same next action. The policy may remember different past experiences. Exact prediction preserves the environment's response to each admitted input; the controller's initial memory and information interface must also correspond before equating closed-loop behavior. A minimum predictor is not automatically a minimum controller or a complete institutional state.

### 4.3 Connection to feasible alignment requirements

Suppose the contract retains every event needed by an acceptance requirement \(\mathfrak A\), expressed as a set of admissible path laws, and preserves the permitted continuation-policy class with its initial information and memory. Then
\[
\{\pi:P_h^\pi\in\mathfrak A\}
=\{\pi:P_{Q(h)}^\pi\in\mathfrak A\}.
\]
This follows policy by policy from path-law equality. Thus the representation preserves existence of a successful permitted policy, plural conjunctions of requirements, and the evaluation of an explicitly installed policy. It does not make the installed policy successful or select the ethical requirement. If the requirement depends on previously incurred harm, current hidden status, or private memories, those distinctions must be represented in the contract as specified below. A summary of the single Boolean answer “some policy succeeds” would generally be too weak to recover which action is usable.

## 5. Protected but unobserved outcomes

Protected consequences may be unknown to the controller. They must not be added to its observations merely to obtain the update theorem.

Let \(Z\) be a finite alphabet of audit outcomes or event-monitor values, not necessarily observed. A supplied causal model can define all finite joint continuation laws

\[
D_h^{u_{1:n}}(o_{1:n},z_{1:n}).
\tag{9}
\]

They must be normalized, projectively consistent, and nonanticipating in the imposed inputs. They must also be **compatible with conditioning on the actual interface**: the future law after the history \(huo\) is obtained by conditioning on the delivered observation \(o\), summing over the first unobserved audit value, and then discarding the first step. Thus, for a future event \(A\) and a later imposed input word \(v\),

\[
D_{huo}^{v}(A)
=\frac{\sum_zD_h^{uv}(O_1=o,Z_1=z,\mathrm{tail}\in A)}
{\Pr_h^u(O_1=o)}
\tag{10}
\]

when the denominator is positive. These requirements hold for conditional laws derived consistently from one supplied causal process. They need not hold for a collection of independently fitted prediction tables.

Include all probabilities in (9), their observable marginals, and the conditioning queries in the response profile. Equation (10) proves recursive update of that **forecast profile** using only \((u,o)\). Theorem 1 gives its least-information property. Adaptive policies depending only on observations preserve the protected-event forecasts too: the policy factors in (8) do not depend on hidden \(z\), so they can be multiplied into the corresponding joint audited path law and summed.

Current hidden status, previously incurred harm, and elapsed obligations need their corresponding conditional queries or event monitors, including the joint queries required for updating them after observations. Equality of future observable laws alone does not preserve these additional facts.

This distinction is essential: a forecast profile that updates without seeing audit outcomes is not necessarily a Markov generator that can sample an audit outcome each step independently conditional on that profile.

**Counterexample.** Draw a hidden fair bit \(B\) once and retain it forever. Every observation is a constant, while the audit value is \(Z_t=B\) at every step. All admitted observation histories have the same future-response profile. It correctly predicts \(\Pr(Z_1=Z_2=1)=1/2\). A one-state generator that instead samples each audit output from its one-step marginal predicts \(1/4\), which is wrong. Generating the joint audit process requires preserving its hidden correlation, or generating from its full joint continuation law. The observer's minimum predictive information and the generator's hidden physical memory are different objects.

An analyst-full-history construction can instead condition on all audit values and obtain a recursive generator of the joint process. But that construction has more information than the actual participant and cannot be used to enlarge its permitted policy class.

For several participants, retain each local delivered-history map and policy restriction. A centralized analyst profile may preserve their joint process without being available to any participant. The present single-interface recursion is not a solution to general decentralized state estimation or synthesis.

## 6. Deriving an optimal coordinate basis in a linear class

A response profile is representation-independent but may have infinitely many coordinates. Under a further finite-rank condition, actual test coordinates can be selected by a theorem.

First take the query family to be all observable action/observation tests from Section 3, including the empty test. Form the **system-dynamics matrix**

\[
\mathsf D(h,\tau)=d(h,\tau),
\tag{11}
\]

with one row per history and one column per finite test, including the empty test. Its real rank means the dimension of the span of its columns as functions on histories. This can be infinite. For finite rank \(r\), choose \(r\) actual test columns \(\tau_1,\ldots,\tau_r\) forming a basis, and define

\[
q(h)=\big(d(h,\tau_1),\ldots,d(h,\tau_r)\big).
\tag{12}
\]

The empty-test column is the nonzero constant function one; the basis may therefore be chosen to include it.

If present observable labels are additional requirements not already determined by these future predictions, append their categorical indicator queries and all required joint prefix queries before measuring rank. The same proof applies to that enlarged, continuation-closed query matrix. Without this addition, the rank claim optimizes prediction of the future observable channel, not preservation of independently required current labels.

**Theorem 3: exact linear dimension and update.** If \(\operatorname{rank}\mathsf D=r<\infty\), then:

1. For every test \(\tau\), there is a fixed vector \(a_\tau\in\mathbb R^r\) such that \(d(h,\tau)=q(h)a_\tau\) for all admitted histories.
2. On a possible next observation,
   \[
   q_j(huo)=\frac{q(h)a_{(u,o)\tau_j}}{q(h)a_{(u,o)}}.
   \tag{13}
   \]
3. Any representation \(x(h)\in\mathbb R^d\) with ordinary linear test readouts \(d(h,\tau)=x(h)b_\tau\) has \(d\ge r\).
4. Under an affine-readout convention \(d(h,\tau)=b_{\tau,0}+x(h)b_\tau\), the minimum number of variable coordinates is \(r-1\).

**Proof.** Basis expansion proves statement 1. Equation (7) and the linear expansions of its numerator and denominator prove statement 2; division is only performed at a positive probability. For statement 3, every column of \(\mathsf D\) lies in the span of the \(d\) coordinate functions of \(x\), so its rank cannot exceed \(d\). For statement 4, adjoining the constant function to any affine representation gives at most \(d+1\) independent functions, implying \(d\ge r-1\). Conversely, choose a basis containing the constant empty-test column, remove that fixed coordinate from the stored vector, and absorb it into the affine intercepts. This supplies \(r-1\) variable coordinates. ∎

The chosen basis is generally **not unique**; all bases span the same response space and are related by invertible linear transformations when represented in the same convention. The response-equivalence quotient, not a particular basis, is the invariant object.

Equation (13) is valid on reachable predictive states, where the decoded test probabilities are coherent. Arbitrary points of \(\mathbb R^r\) need not represent valid probability laws. Linear coefficients may be negative. Rank minimality is not minimum nonnegative HMM dimension, minimum probabilistic automaton size, or a guarantee that a chosen low-rank estimate is realizable.

The proof extends to additional protected-test columns when the enlarged query family contains the joint prefix/conditioning operations used in the update. It is not enough merely to append a few hidden-outcome expectations and assume the observation update remains closed.

This theorem provides a concrete answer to “why these variables?” under one honest objective: choose a basis of independently necessary future-response functions. It does not assert that linear readout is optimal for all computational tasks, that exact real coordinates have finite bit cost, or that a nonlinear one-coordinate encoding cannot contain the same information.

## 7. Four different minimality problems

| Representation problem | Exact object retained | Optimality actually available |
|---|---|---|
| General test profile | Answers to the declared queries | Unique coarsest deterministic sufficient partition |
| Actual-history predictor | Causal continuation laws under the actual observation interface | Coarsest recursively updateable predictive partition when continuation closed |
| Linear predictive basis | Test probabilities with linear readouts | Rank-many ordinary linear coordinates, or rank minus one affine variable coordinates |
| Finite physical-state quotient | Current labels and next-block probabilities for every intervention | Unique coarsest strong-lumpable/bisimulation partition of that supplied state model |

None is generally interchangeable with minimum hidden generative-state count or minimum scientific description length.

### 7.1 Equal observable futures need not imply strong lumpability

Let physical states \(A,B\) have the same current label. Let \(C,D,E\) share another label; \(G,H\) have distinct labels and are absorbing. Set

\[
A\to C,\quad B\to\tfrac12D+\tfrac12E,
\quad C\to\tfrac12G+\tfrac12H,
\quad D\to G,\quad E\to H.
\]

The complete observable-label futures from \(A\) and \(B\) agree. Nevertheless a label-preserving strong quotient cannot merge \(C,D,E\), whose next-label probabilities differ. It then cannot merge \(A,B\), whose next-block laws differ. Strong physical-state lumpability imposes a stronger internal Markov contract than output-trace prediction. The same fine state model can therefore have different correct minima under different preservation questions.

### 7.2 A finite generator can require infinitely many predictive classes

Let a hidden persistent type \(\Theta\in\{0,1\}\) be initially equiprobable. Conditional on type, observations are independent Bernoulli with parameter \(1/4\) or \(3/4\). After \(n\) consecutive ones,

\[
\Pr(\Theta=1\mid 1^n)=\frac{3^n}{1+3^n}.
\]

The next-one predictions are distinct for every \(n\), so exact history prediction requires infinitely many predictive equivalence classes despite a two-state hidden generator. Their forecasts are nevertheless affine in one posterior coordinate: the test matrix has rank two, counting its constant coordinate. Predictive class count, linear dimension, and hidden generator size answer different questions.

### 7.3 Approximation is a different optimization problem

An error tolerance does not automatically define an equivalence relation: approximate agreement can be nontransitive. For example, probabilities \(0,.1,.2\) are pairwise within .1 along adjacent pairs but not between the endpoints. Approximate compression requires a loss, a history/intervention weighting or worst-case class, admissibility constraints, and a complexity measure. Different choices can have different optima or incomparable compromises. The exact theorems do not select those tradeoffs.

## 8. Unknown models and endogenous evaluation

### 8.1 Model uncertainty must enter the response contract

For one fixed known causal law, the theorems above apply directly. For Bayesian uncertainty, use the posterior predictive causal law derived from the specified prior and actual history. Its update includes any history-dependent posterior weights. There is no license to average model-wise response profiles using the original prior after informative observations.

The two-type example gives a simple failure witness. Within each fixed type model the future law is independent of past observations. A vector storing only each model's separate future law is therefore constant across histories. Yet histories 1 and 0 imply posterior weights \(3/4\) and \(1/4\), and different predictive mixtures. The constant model-wise profile cannot update the Bayesian predictor. Retain posterior weights or directly retain the full posterior predictive response profile.

A robust analysis can instead retain answers separately for each admitted model, together with model compatibility and whatever information-state update its uncertainty semantics requires. This is a different contract. Unions of possible outputs, a common partition, and identical stochastic predictions are different objects. A model excluded by the original class is not covered by its optimality theorem.

### 8.2 Evaluation can change inside the causal process

Representations of harm, commitments, membership, authority, and admissible revision can themselves be outputs or latent state in the causal model. Queries may concern how those commitments were formed, whose challenges remained possible, and whether a revision was implemented. In this way evaluation formation can be endogenous without assuming that whatever standard emerges is justified.

An evaluative query contract still declares what its questions mean. If a new concern or participant adds a genuinely new test while retaining old ones, Corollary 3 prescribes refinement. This is not a defect of the optimum; it is the mathematical consequence of changing the preservation problem.

Allowing every possible future history query forces the exact representation to retain every distinguishable history: the indicator query \(\mathbf1\{h=h_0\}\) separates any omitted distinction. A useful optimal model is therefore relative to an explicit, revisable scope. The choice of that scope remains scientific and normative work.

## 9. Relation to space, time, and the prior tuple

Spacetime can provide a substrate for the causal history model. Locations, propagation times, causal order, material fields, distance, access, and spatially distributed action can enter the kernels and tests. They are retained whenever omitting them changes a required response. If a symmetry preserves every permitted intervention and retained consequence, the quotient can remove the corresponding coordinate dependence. If a new spatial target breaks that symmetry, the query expansion refines the quotient.

This is more defensible than declaring either spacetime or a list of social variables universally optimal. Neither the names of coordinates nor their number establishes explanatory completeness.

The earlier tuple

\[
\mathcal E=(A,\mathcal D,\mathcal T,\mathcal K,\mathcal U,\mathcal B,H,\varepsilon)
\]

can remain as an alternative **contract-building checklist**. Its entries prompt the author to identify affected parties, disturbance hypotheses, functional tests, protected constraints, policy permissions, resources, timing, and tolerated risk. They help prevent important omissions but are neither independent primitives nor required coordinate blocks of the optimal state. Resource limits can be encoded in transitions and tests; timing can appear in histories and outcomes; affected-party concerns can index separate acceptance predicates.

The least-information response representation is derived only after that substantive specification. It does not discover which parties deserve standing or which causal laws are true. The theory's distinctive explanatory work remains the constraints connecting activity to the generation, depletion, and renewal of these consequential mechanisms.

## 10. What the optimality statements do not buy

- **No causal identification from passive fit.** Equal behavior under historically used actions need not imply equal response under a new intervention. Counterfactual laws are inputs to, or empirical targets of, the preservation claim.
- **No free algorithm.** Equality of infinite response profiles may be uncomputable or statistically undecidable from a finite record in unrestricted model classes. Finite exact models or finite-rank assumptions can provide tractable special cases, not a universal learner.
- **No globally optimal description language.** A compact physical mechanism can be scientifically more explanatory than a large response table even when both induce the same optimum predictive partition.
- **No automatic recursive closure for arbitrary values.** A profile of present expected utilities can lose the distinctions needed to update later outcomes, especially under new information or changing obligations.
- **No hidden knowledge for agents.** Full analyst histories, posterior forecast states, physical hidden states, and participants' own histories must remain distinct.
- **No fixed final evaluation.** Exactness and optimality are conditional on the declared questions. Legitimate expansion can require more retained information.
- **No new universal alignment theorem.** The optimal representation preserves the specified causal/evaluative problem. Actual installed renewal and normative justification still require the separate results and commitments in the dossier.

These limits identify the optimization problem's boundary while leaving a substantive positive result: a required distinction has an explicit separating query; an unnecessary one can be removed with a preservation proof.

## 11. Primary-source lineage checked for this note

The construction uses established predictive-state and reduction ideas. The proofs above are stated directly because our finite-history, explicitly causal, and information-separated contract is more specific than a generic appeal to “optimal prediction.”

1. **Shalizi and Crutchfield, *Computational Mechanics: Pattern and Prediction, Structure and Simplicity* (2001).** Their causal-state construction establishes predictive sufficiency, minimality, and uniqueness under its process assumptions. Our elementary factorization and entropy arguments make the chosen scope explicit without importing stationarity or infinite-past assumptions. [Primary preprint](https://arxiv.org/abs/cond-mat/9907176).
2. **Barnett and Crutchfield, *Computational Mechanics of Input-Output Processes: Structured transformations and the epsilon-transducer* (2015; corrected preprint 2016).** Sections VI–IX treat input/output causal states, reproduction, and optimality; later sections distinguish history and generator presentations and discuss infinite-state cases. The original development has its own stationarity and channel assumptions. [Primary full text](https://arxiv.org/html/1412.2690), [author PDF](https://csc.ucdavis.edu/~cmg/papers/et1.pdf).
3. **Littman, Sutton, and Singh, *Predictive Representations of State* (NIPS 2001 proceedings).** State represented by multi-step action-conditional predictions is established prior work; its linear predictive representation is the direct precedent for the test-basis formulation here. [Official proceedings paper](https://proceedings.neurips.cc/paper/2001/file/1e4d36177d71bbb3558e43af9577d70e-Paper.pdf).
4. **Givan, Dean, and Greig, *Equivalence Notions and Model Minimization in Markov Decision Processes* (2003).** Controlled stochastic bisimulation and finite-model minimization support the dossier's separate strong-quotient theorem. [Author manuscript](https://cs.brown.edu/people/tdean/publications/archive/GivanetalAIJ-03.pdf).

The “Nerode” description names the residual-future/right-congruence lineage; no priority claim for a new automata-minimization theorem is made. This note proves the exact version it uses rather than relying on an unverified universal extension.

## 12. Recommended claim for specialist review

> For a declared causal and evaluative contract, the response-equivalence construction gives the unique least-information deterministic representation preserving every required answer. When the contract is closed under actual observation updates, this representation is recursively maintainable. When its test-response matrix has finite rank, an exact coordinate basis of provably minimal linear dimension can be derived. The earlier semantic tuples are useful ways to specify a problem; they are not its uniquely necessary state variables.

This is an actual optimality claim with a proved objective and comparison class. The subsequent scientific task is to specify informative causal contracts and mechanism restrictions, identify their response laws, and test whether the resulting representation explains and improves the maintenance of alignment's conditions.
