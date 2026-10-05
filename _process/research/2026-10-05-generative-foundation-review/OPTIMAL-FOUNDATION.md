# A canonical foundation with proved representational optimality

Primary formal approach for Alignment as the Reproduction of Its Conditions. Specialist review draft, 5 October 2026.

Research direction: Yongxu Ren. AI-assisted synthesis and derivations prepared in response to the question of why a foundational theory should privilege a particular list of variables. Mathematical lineage is credited below. This document adopts a preferred architecture and proves specific optimality properties; it does not establish a uniquely best scientific theory or ethical objective.

## 1 The result and the choice it replaces

The primary formulation begins with situated processes, interventions available through specified interfaces, and consequences that an inquiry must preserve. Its state variables are derived from distinctions in those consequences. It does not begin by declaring resources, goals, authority, spacetime coordinates, or another inventory to be universally fundamental.

The criterion is exactness first and unnecessary distinctions second:

> Among deterministic representations that preserve every response required by a declared intervention and evaluation contract, choose the least informative representation. If a recursively updated predictor is required, also preserve its update. If linear predictive coordinates are required, minimize their number within that class.

These are optimization problems with solutions and proofs. They do not simultaneously minimize computation, data requirements, physical implementation cost, and explanatory difficulty.

Three results support the preferred formulation:

1. Histories with identical required responses form the unique coarsest exact deterministic representation, up to relabeling.
2. For a causally consistent family of action and observation tests closed under continuation, that representation updates recursively. If its test matrix has finite rank, a basis of test predictions supplies the minimum number of coordinates for exact linear readout.
3. For a supplied finite controlled Markov model, exact refinement characterizes the unique coarsest deterministic faithful Markov quotient. Finite rational transition tables make this an effective algorithm. This is a different comparison class from predictive history models.

The previous [mechanistic dossier](FOUNDATION.md) remains an alternative, interpretable way to specify models and requirements. Its eight-entry evaluation tuple is retained as an audit checklist. It is not the primary foundational axiom.

## 2 What the optimum selects

Three choices must remain separate: the real process and causal assumptions being investigated; the interventions, observations, interests, and consequences the inquiry must preserve; and the representation used to answer those questions.

The theorems solve versions of the representation problem given the other choices. They do not identify a true causal model from arbitrary observational data or determine whose interests should count. Excluding an affected party can make a model smaller without making the exclusion justified.

For this foundational task, preservation takes priority because we are testing whether a description erases distinctions required by its own claims. Resource-limited approximations can then be compared with the exact reference. This ordering is an explicit methodological choice.

Counting variable names is inadequate. A finite tuple can be encoded in one integer, while one real variable can have infinitely many distinguishable values. The principal ordering compares retained distinctions. Dimension is minimized only after restricting the decoder class.

## 3 Processes and operational contracts

Let \(\mathscr H\) be a specified set of histories at decision or assessment boundaries. A history can arise from an agent network, population process, spatial field, or recorded interaction. The first theorem is set theoretic. The constructive results use finite alphabets and countable histories; measurable continuous extensions require additional regularity.

Supply a causal model \(\mathcal M\), or an uncertainty model, assigning consequences to interventions. Also supply each participant's actual information and the rules governing intervention availability. Setting an action must be distinguished from observing a naturally chosen action. Unknown intervention responses remain unknown inputs; the equivalence construction does not discover them.

An operational contract \(\mathfrak C\) specifies named experiments and questions. Experiments can be open-loop action sequences or permitted adaptive protocols. Their consequences can include physical outcomes, delivery times, separate parties' burdens, amendments, or maintenance. Questions can concern event probabilities, joint distributions, and continuing obligations. This specifies types of relation, not a fixed inventory of universal coordinates.

Write \(\lambda(h)\) for current interface distinctions that must be retained, such as permissions or residual obligations. Write \(\rho_e(h)\) for the required response to experiment \(e\), including an inapplicable value where necessary. If uncertainty matters, retain labeled model-specific responses or use an explicit Bayesian model. Do not silently replace uncertainty by an average.

The response profile is
\[
R_{\mathfrak C}(h)
=\left(\lambda(h),(\rho_e(h))_{e\in\mathfrak C}\right).
\tag{N1}
\]
This profile need not be finite, known, learnable, or cheap to calculate. It defines fidelity before choosing a representation.

For a nonempty model family \(\mathfrak M(\iota)\), a common implementable policy class \(\Pi(\iota)\), and an acceptable set of trajectory laws \(\mathfrak A_\tau\), a robust capacity statement is
\[
\tau\in\mathcal C_{\mathfrak M,\mathfrak C}(\iota)
\quad\Longleftrightarrow\quad
\exists\pi\in\Pi(\iota)\ 
\forall M\in\mathfrak M(\iota):
P_M^{\pi,\iota}\in\mathfrak A_\tau.
\tag{N2}
\]
The laws are assumed well-defined. The policy is the same across unresolved possibilities. Bayesian evaluation, different participant beliefs, and decentralized strategies need their corresponding contracts; (N2) does not replace them.

The acceptance sets can keep several requirements separate. Expected burden, deadline reliability, and conditional participation need not be added into one reward. Their justification is supplied explicitly, not derived by compression.

## 4 The canonical representation theorem

Define
\[
h\sim_{\mathfrak C}g
\quad\Longleftrightarrow\quad
R_{\mathfrak C}(h)=R_{\mathfrak C}(g),
\qquad q_*(h)=[h]_{\mathfrak C}.
\tag{N3}
\]
A deterministic representation \(q:\mathscr H\to Q\) is exact when a decoder satisfies
\[
R_{\mathfrak C}=d_q\circ q.
\tag{N4}
\]
Order representations by information: \(q_1\preceq q_2\) if \(q_1=f\circ q_2\) for some function \(f\). Thus \(q_2\) distinguishes at least everything \(q_1\) does.

**Theorem N1 Canonical exact representation.** The map \(q_*\) is exact and is a least element among all exact deterministic representations:
\[
q_*\preceq q\quad\text{for every exact }q.
\tag{N5}
\]
Every other least exact representation is related to it by a bijection on attained values.

**Proof.** Responses are constant on each class, so \(d_*([h])=R_{\mathfrak C}(h)\) is well-defined. For exact \(q\), equality \(q(h)=q(g)\) implies equality of decoded responses and hence \(h\sim g\). Therefore \(f(q(h))=[h]\) is well-defined, giving \(q_*=f\circ q\). Two least exact representations factor through one another, induce identical partitions, and consequently have bijective attained values. ∎

If the quotient has finitely many classes, no exact deterministic summary has fewer attained values. For any history distribution giving discrete representation variables with finite entropy,
\[
\operatorname H(q_*(H))\le\operatorname H(q(H)).
\tag{N6}
\]
This follows because \(q_*(H)\) is a function of \(q(H)\) and
\(\operatorname H(q(H))=\operatorname H(q_*(H))+
\operatorname H(q(H)\mid q_*(H))\).
Factorization requires no history distribution; entropy optimality does.

The result is invariant under faithful re-encoding. A bijection of histories and corresponding relabeling of questions that preserves every response carries equivalence classes bijectively to equivalence classes. This follows immediately from (N3). A spatial-field description and a network description can therefore yield the same operational object when their intervention and observation correspondence is established; changing coordinates alone does not establish that correspondence.

This theorem derives which distinctions must remain. It does not make a response table a causal explanation. Explanation still requires restrictions on how activity generates, depletes, restores, or changes its enabling mechanisms.

## 5 When the representation updates recursively

A profile answering only today's questions need not support tomorrow's update. Recursive representation needs a contract closed under relevant continuations.

Consider one actual action and observation interface with finite alphabets \(\mathcal A,\mathcal O\). Histories contain its observed record and required initialization. Variable permissions may be reported in observations, with refused proposals represented explicitly. Time dependence may be retained through histories or clocks; stationarity is not assumed merely to obtain a finite state.

For action word \(a_{1:n}\) and observation word \(o_{1:n}\), write
\[
p_h(o_{1:n}\Vert a_{1:n})
\tag{N7}
\]
for the causal probability of those observations when the actions are supplied from history \(h\). The double bar means intervention, not conditioning on naturally chosen future actions. Assume causal consistency and extension rules.

Use all finite action and observation tests, including the empty test. For the pure predictive contract, histories are equivalent when every probability (N7) agrees. Additional exact current labels must be determined by the actual observed history. Their next values must be delivered in the observation packet or have a preserved observation-based update. An unobserved current label instead requires a conditional assessment; it cannot be made known merely by adding a forecast of its future value.

**Theorem N2 Recursive predictive state.** If \(h\sim g\), the next-observation distributions agree for every action. For a common action \(a\) and observation \(o\) of positive probability,
\[
hao\sim gao.
\tag{N8}
\]
Thus
\[
q_*(hao)=F(q_*(h),a,o)
\tag{N9}
\]
is well-defined. It is the least exact deterministic recursively updated predictor in this class.

**Proof.** One-step tests give identical denominators. For every continuation test,
\[
p_{hao}(v\Vert u)=
\frac{p_h(ov\Vert au)}{p_h(o\Vert a)}.
\tag{N10}
\]
The numerator and denominator agree at \(g\), so all continuation predictions agree. The update is therefore well-defined. Theorem N1 makes it least among all exact deterministic predictors, including recursively updated competitors. ∎

Impossible observations require a separate extension. For a shared residual policy using this actual observation record and the same initialized controller memory, equality of controlled tests also preserves adaptive finite path laws. Each path probability multiplies the policy's action probabilities by the controlled observation probabilities at successive prefixes. Both agree. Finite cylinder laws determine infinite path laws on finite alphabets.

An analyst's joint history is not automatically available to a participant. Updating on every private signal does not yield an executable individual predictor without communication. Unobserved protected events may be assessed by an evaluator, but they must not become observations available to the policy merely by being recorded in the model.

Recursion is an existence statement, not yet an effective implementation. Supplied response laws may be noncomputable, and exact real arithmetic may be unavailable. Execution requires effectively represented initial states, probabilities, and update operations, together with a resource and precision contract. Finite rational models provide one concrete computable class.

### 5.1 Protected outcomes that the participant cannot observe

For hidden audit outcomes \(z\), preserve the joint future laws of observations and audit outcomes, rather than only observation marginals. If those laws come consistently from one causal model, the forecast after action \(a\) and delivered observation \(o\) is obtained by conditioning on \(o\) and summing over the hidden first audit value:
\[
\rho_{hao}^{\,v}(A)=
\frac{\sum_z P_h^{av}(O_1=o,Z_1=z,\mathrm{tail}\in A)}
{P_h^a(O_1=o)}.
\tag{N10a}
\]
Here \(v\) supplies the subsequent action word and \(A\) is a future joint audit and observation event. Positive denominators, causal consistency, and all required conditioning queries are assumed. Equal joint forecast profiles then have equal updated profiles without revealing \(z\). Current hidden status and previously incurred harm need their own conditional queries and update closure. The [mathematical development](optimal-foundation/MATHEMATICS.md#5-protected-but-unobserved-outcomes) gives this extension in detail.

This forecast profile is not necessarily a Markov generator of audit outcomes. For a hidden fair bit \(B\) fixed forever, constant visible observations, and \(Z_t=B\), one observed-history profile correctly forecasts \(\Pr(Z_1=Z_2=1)=1/2\). Independently sampling the one-step audit marginal from that single profile would instead give \(1/4\). Generation must preserve the hidden correlation, even though updating the observer's forecasts does not reveal the bit.

## 6 A minimum number of predictive coordinates

Form the system dynamics matrix
\[
D(h,t)=p_h(t),
\tag{N11}
\]
with histories as rows and finite action and observation tests as columns. The empty-test column is one. Rank means algebraic column rank over the reals, not an unvalidated rank estimate from a finite dataset.

This matrix concerns the observed test family just defined. Extra current labels or protected outcomes require their additional queries and every conditioning query needed for update before claiming a dimension optimum for that larger contract. The original observed-channel rank alone does not establish it.

**Theorem N3 Minimum linear predictive dimension.** If \(\operatorname{rank}D=r<\infty\), choose \(r\) independent test columns \(t_1,\ldots,t_r\) spanning its column space. Put
\[
x(h)=(p_h(t_1),\ldots,p_h(t_r))^\top.
\tag{N12}
\]
Every test has a linear readout
\[
p_h(t)=w_t^\top x(h).
\tag{N13}
\]
No exact representation with ordinary linear readouts for all tests uses fewer than \(r\) real coordinates.

**Proof.** Spanning gives (N13). Conversely, a \(d\)-coordinate representation with linear decoders gives \(D=XW\), hence \(\operatorname{rank}D\le d\). The proposed construction attains \(d=r\). ∎

For prefixed test \(ao\,t_j\), the observed update is
\[
x_j(hao)=
\frac{w_{ao\,t_j}^\top x(h)}{w_{ao}^\top x(h)}
\tag{N14}
\]
on positive-probability observations. The predictor operates on its valid set of probability states; arbitrary vectors in \(\mathbb R^r\) need not be valid.

The basis is not unique; bases are related by an invertible linear transformation. With affine instead of ordinary linear readout, the constant can be placed outside the variable vector, allowing \(r-1\) variable coordinates. This is also minimal in the affine class: \(d\) variable coordinates plus a constant give \(\operatorname{rank}D\le d+1\). Arbitrary nonlinear encodings, nonnegative latent-state realizations, finite-precision storage, and computational runtime are different comparison classes.

These are established predictive-state principles, developed by [Littman, Sutton, and Singh](https://proceedings.neurips.cc/paper/2001/file/1e4d36177d71bbb3558e43af9577d70e-Paper.pdf) and through the system dynamics matrix by [Singh, James, and Rudary](https://arxiv.org/abs/1207.4167). Their role here is to derive coordinates from a process rather than assert a privileged vocabulary.

## 7 A separate optimum for finite physical models

For finite states \(S\) and controlled kernels \(K_a\), retain protected labels, every participant's observations, and permissions. A deterministic quotient \(q:S\to Q\) is faithful when these objects factor through \(q\) and
\[
q(s)=q(t)\Longrightarrow
\sum_{v:q(v)=b}K_a(s,v)
=\sum_{v:q(v)=b}K_a(t,v)
\quad\text{for all }a,b.
\tag{N15}
\]

Start with the partition by the retained interface and labels. Repeatedly split blocks by their next-block probability vectors under every action.

**Theorem N4 Coarsest exact Markov quotient.** Refinement terminates at the unique coarsest faithful deterministic quotient for this supplied contract.

**Proof.** Every strict split increases block count, so termination is finite. The terminal equal block rows define a quotient kernel. Every faithful competitor refines the initial partition. If it refines a current partition, equality of its finer block rows implies equality of sums into current blocks, so it also refines the next split. Induction proves every faithful competitor refines the terminal partition. This proves leastness and uniqueness. ∎

This is controlled probabilistic bisimulation or strong lumpability, already used in [Section 12 of the dossier](FOUNDATION.md#12-faithful-representation-and-constructive-closure). It is not newly discovered mathematics.

Its comparison class matters. A physical-state quotient cannot merge states with different next-block laws. A history predictor can retain conditional distributions over hidden states. Another latent generative model may be smaller. Theorems N1, N3, and N4 do not minimize all these different objects simultaneously.

## 8 An exact example that retains space through delay

An active configuration is \((r,d,j)\): remaining reserve \(r\in\{1,2\}\), travel delay \(d\in\{1,2\}\), and a decorative badge \(j\in\{0,1\}\). Add absorbing states failed and safe, giving ten fine states.

Wait consumes one reserve unit and enters failed when none remains. Dispatch completes an indivisible repair trip and enters safe exactly when \(r\ge d\); otherwise it enters failed. Completion at the reserve boundary succeeds.

Dispatch is a macrostep recording timely completion. Intermediate intervention, exact arrival-time reports, and hazards during travel are excluded. Claims about them need an expanded interface. The retained current observation is active, failed, or safe. Hidden \(r,d\) values do not become controller observations.

Theorem N4 yields six classes: failed, safe, and four active classes indexed by \((r,d)\), with the badge values merged.

A direct lower bound confirms optimality. Absorbing labels cannot merge with one another or active. Different active reserves are distinguished by waiting once. At a common reserve \(r\), waiting \(r-1\) times and dispatching distinguishes delay one from delay two. Thus all four \((r,d)\) combinations require different classes. The badge can be discarded because transitions never read it.

An exhaustive check enumerated all 4,140 partitions of the eight active states with absorbing labels fixed. Exactly nine satisfy the contract; exactly one has the minimum six blocks. Every faithful partition refines it. The [results](optimal-foundation/EXACT-CHECKS.json) and [verification procedure](optimal-foundation/verify_optimality.py) are included.

This contract distinguishes physical arrangements through the delay they induce. If geography also changes capacity, communication, exposure, jurisdiction, or later interventions, those consequences create further distinctions. Spacetime is a valid substrate; it is neither excluded nor automatically required in unreduced coordinate form.

## 9 Finite physical state need not give finite predictive memory

Let hidden fixed \(\theta\in\{1/3,2/3\}\) have equal prior probabilities, with conditionally independent \(Y_t\sim\mathrm{Bernoulli}(\theta)\). There are two physical latent states.

After \(n\) observations all equal one,
\[
\Pr(\theta=2/3\mid1^n)=\frac{2^n}{1+2^n},
\qquad
\Pr(Y_{n+1}=1\mid1^n)
=\frac{1+2^{n+1}}{3(1+2^n)}.
\tag{N16}
\]
The latter increases strictly with \(n\), so infinitely many histories have distinct exact predictions. The observer cannot replace uncertainty with one known physical state.

Nevertheless, the test matrix has rank two. Every test probability is affine in the posterior weight; the constant and next-one columns are independent. One posterior coordinate with affine readout, or two ordinary linear coordinates including normalization, suffice. Infinite predictive classes and finite linear dimension are compatible. Exact real-valued memory is not finite-bit memory.

The accompanying rational calculation checks thirteen predictions. Strict monotonicity of (N16), not that finite computation, establishes infinite distinctness.

## 10 Changing questions changes the optimal representation

If \(\mathfrak C'\) retains every old question and adds distinctions, then
\[
\mathfrak C\subseteq\mathfrak C'
\Longrightarrow
\sim_{\mathfrak C'}\subseteq\sim_{\mathfrak C},
\qquad q_*^{\mathfrak C}=f\circ q_*^{\mathfrak C'}.
\tag{N17}
\]
Equality of the larger profile entails equality of its restriction. Thus a new participant, intervention, or question can require a finer optimal representation.

The reverse recovery is generally impossible. If an old class merges histories distinguished by a new question, its shared old value cannot determine different new answers. Retained records or fresh evidence may be necessary. This motivates analysis of revisability costs; it does not establish an unconditional duty to retain everything.

If every indicator query \(1\{h=h_0\}\) is permitted, no distinct histories can merge. Preserving every arbitrary future question yields the identity partition. Universal question preservation and nontrivial compression cannot both be required over unrestricted histories.

The system's actual criteria can change inside the causal model. Amendment, enforcement, and transmission become events. Whether an amendment is legitimate remains an explicit assessment. Relaxing a standard cannot silently count as improvement in the physical consequences previously assessed.

## 11 Connection to the generative foundation

Canonical representation disciplines the generative theory; prediction alone does not replace it.

For a continuation requirement, the scientific question is which mechanisms make the required responses possible and how activity changes those mechanisms. Activity may deplete action-supporting stocks, alter who can intervene, remove a measurement channel, establish a successor, or modify future selection rules. These mechanisms matter when they alter relevant responses or their availability.

The mechanistic dossier supplies restrictions with discriminating consequences: prefix deficits must fit reserves; action under uncertainty can fail despite individual recoverability of every hidden state; selection changes renewal; a successor can arrive too late; initial agreement can fail after assignment; and installed behavior need not realize an available corrective policy.

A representation must preserve the tests distinguishing these outcomes. Independently supported mechanisms then explain their response laws. The activity–conditions feedback is not proved merely because a canonical predictor exists; every specified process has a response profile. Scientific content comes from its dependencies, rate restrictions, substitutes, and intervention predictions.

Actual restoration, succession, and revision events belong in the contract when continuation depends on them. Repeatedly labeling a state “correction available” does not establish that correction occurs. This connects representational optimality to the installed-process safety and renewal theorem in the dossier.

## 12 The retained alternative approach

The original tuple remains:
\[
\mathcal E=(A,\mathcal D,\mathcal T,\mathcal K,\mathcal U,\mathcal B,H,\varepsilon).
\tag{N18}
\]
It is an interpretable way to construct a contract:

| Component | Role in the primary formulation |
|---|---|
| Affected parties \(A\) | Indexed outcomes, standing, participation questions |
| Disturbances \(\mathcal D\) | Boundary inputs or model uncertainty |
| Functions \(\mathcal T\) | Continuation, recovery, establishment, performance questions |
| Constraints \(\mathcal K\) | Acceptable events or trajectory laws |
| Interventions and information \(\mathcal U\) | Actual interfaces and permitted policy class |
| Resources \(\mathcal B\) | State dynamics, feasibility, dated implementation tests |
| Horizons \(H\) | Temporal tests and event monitors |
| Failure tolerance \(\varepsilon\) | Probability and robustness requirements |

A budget can be a balance and an action constraint; a deadline can be a clock monitor; a spatial restriction can affect both dynamics and access. Consistent consequences matter more than a fixed partition of semantic roles.

The dossier's semantic state tuple likewise remains useful for finding mechanisms. It directs attention to observation, authority, memory, purposes, and rules without treating them as irreducible substances. Mechanistic coordinates may be easier to interpret and intervene upon than a smaller predictive representation.

## 13 Approximation and other limits

If a summary merges histories whose event responses differ by \(\delta>0\), every common predicted probability has error at least \(\delta/2\) on one of them. Otherwise the triangle inequality would contradict their separation. This bounds the consequence of discarding a relevant distinction.

Approximate preservation needs its own error and cost criterion. Near-equivalence is not transitive: probabilities \(0,.4,.8\) have adjacent differences below .5 but endpoint difference above .5. There need not be a unique coarsest approximate partition. A constrained optimization or Pareto comparison is required.

Further limits are substantive:

- An exact representation of a wrong causal model preserves its mistakes. Observational equality does not ensure equality after intervention.
- A minimum predictor need not be easiest to learn, explain, simulate, or repair.
- One installed controller can restrict the reachable process far more than the full intervention family. Its smaller model does not establish robustness to controller change.
- Each participant's information remains separate unless communication is modeled. Pooled sufficiency is not decentralized implementation.
- Endpoint agreement does not identify voluntary revision, coercion, or exclusion. Those histories and alternatives must be protected when relevant.
- Component marginal laws do not determine joint behavior under shared disturbances. Composition needs compatible joint interfaces.

The established optimum concerns exact representation under a declared contract and comparison class. It does not establish optimal causal discovery, unlimited concept formation, ethically optimal evaluation, or the universally best scientific theory.

## 14 Established lineage and candidate contribution

| Primary source | Established connection |
|---|---|
| [Shalizi and Crutchfield, Computational Mechanics](https://arxiv.org/abs/cond-mat/9907176) | Predictive sufficiency, minimality, uniqueness |
| [Barnett and Crutchfield, Input Output Processes](https://arxiv.org/abs/1412.2690) | Controlled processes and predictive transducers |
| [Littman, Sutton, and Singh, Predictive Representations of State](https://proceedings.neurips.cc/paper/2001/file/1e4d36177d71bbb3558e43af9577d70e-Paper.pdf) | Action-conditional predictive coordinates |
| [Singh, James, and Rudary, Predictive State Representations](https://arxiv.org/abs/1207.4167) | System dynamics matrix and rank |
| [Givan, Dean, and Greig, Model Minimization](https://cs.brown.edu/people/tdean/publications/archive/GivanetalAIJ-03.pdf) | Controlled equivalence and finite reduction |
| [Shalizi, Random Fields on Networks](https://arxiv.org/abs/math/0305160) | Local predictive sufficiency for spatially distributed fields |
| [Rosas, Boyd, and Baltieri, AI in a Vat](https://rlj.cs.umass.edu/2025/papers/Paper367.html) | Predictive world-model minimality and memory versus interpretation tradeoffs |
| [Baltieri and colleagues, Environment Agent and Joint Models](https://arxiv.org/abs/2608.20401) | A 2026 preprint distinguishing environment, agent, and realized joint channels, including support-dependent model reduction |

“Causal state” in predictive modeling does not itself identify physical intervention mechanisms from passive data. Here intervention responses are supplied or independently identified.

The 2026 preprint is cited at abstract and scope level, not as a verified import of all its theorems. Its distinction between an unrestricted channel and the process reachable under one installed coupling directly bears on the intervention-coverage limit in Section 13. The companion prior-art memorandum also identifies recent work on modular transducer decomposition; detailed use of those constructions would require their additional interface conditions.

The candidate contribution is the integration of these formal disciplines with the reproduction of alignment's conditions: whose consequences count, how correction and participation remain executable, how carriers are replaced, and how commitments and representations change. The minimality and rank principles themselves are established prior art.

## 15 Review status

The primary approach now has a proved representational optimum rather than an asserted universal variable list. Under continuation assumptions it yields a recursively defined predictor; finite rank yields minimum linear dimension; finite rational controlled models admit a computable optimal faithful quotient. These claims remain separate from the truth and completeness of the causal model being represented.

The [mathematical development](optimal-foundation/MATHEMATICS.md), [adversarial audit](optimal-foundation/ADVERSARIAL.md), and [foundational and prior-art analysis](optimal-foundation/FOUNDATIONS-PRIOR-ART.md) preserve the preparation work. AI review is not independent human peer review.

The ten-state example was checked by refinement and exhaustive partition enumeration. The hidden-state example used rational arithmetic. These are constructed verifications, not new empirical evidence. The original mechanistic approach is retained in full, and its prior evidence retains its previous limits.
