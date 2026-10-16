# Invariant capability, information, and the physical scope of the root claim

Specialist development memo, 5 October 2026. This memo supplies exact finite propositions and prior-art positioning for the proposed root of *Alignment as the Reproduction of Its Conditions*. The proofs are elementary consequences of established probability, decision, and control theory; no priority claim is made for them. Their role is to make the integration precise.

## 1. Strongest defensible direction

The proposed root should concern **the conditions of possible continuation and correction**, together with the processes that transform those conditions. Selection and renewal are substantive realizations of this structure where differential continuation and vulnerable supports occur. Neither word should be defined so broadly that every physical change satisfies it by verbal stipulation.

A useful central claim is:

> Continued functioning and reliable correction are constrained by what a situated system can actually distinguish and bring about. Those constraints are invariant under faithful changes of description. When the relevant capacities face uncompensated loss, their continued availability requires provision, substitution, or altered dependence. Systems that modify the conditions of their own future functioning create an endogenous problem of reproducing or revising those conditions.

The invariance clause and conditional necessities can have mathematical force. Their instantiation and causal importance in a particular domain remain scientific questions. A dependency structure, a differential-selection mechanism, and a closed feedback loop are not interchangeable claims.

## 2. The invariant is a set of attainable response profiles

Fix an initial situation \(\iota\), an unresolved model or circumstance index \(\theta\in\Theta\), and a common class \(\Pi(\iota)\) of physically executable and contract-permitted policies. A policy can use only its actual delivered information. Let \(P^{\pi,\iota}_{\theta}\) be its trajectory law, including any outcomes, costs, delays, amendments, and protected events required by the inquiry.

Define the attainable response-profile set

\[
\mathscr R(\iota)
=\left\{\left(P^{\pi,\iota}_{\theta}\right)_{\theta\in\Theta}:
\pi\in\Pi(\iota)\right\}.
\tag{I1}
\]

The same policy appears across all unresolved circumstances. Allowing a separate clairvoyant policy for each \(\theta\) would enlarge the set without supplying the missing information.

A task \(\tau\) is an acceptance set \(\mathfrak A_\tau\) of response profiles. It may impose multiple risk, burden, participation, deadline, and continuation requirements without a weighted common utility. Its feasibility is exactly

\[
\tau\text{ is feasible at }\iota
\quad\Longleftrightarrow\quad
\mathscr R(\iota)\cap\mathfrak A_\tau\ne\varnothing.
\tag{I2}
\]

This formulation is descriptive until the evaluation contract identifies which tasks are acceptable. The fact that an action is executable neither authorizes it nor makes it good.

The set (I1) is not a substitute for a mechanism. It summarizes what all allowed mechanisms and policies can achieve at a specified interface. The mechanism model explains how this set changes when resources, information channels, participants, or installed rules change.

## 3. Exact transport under faithful descriptions

Here is a constructive finite version of description invariance. It accommodates hidden physical states and hidden audit outcomes without granting either to the controller.

For each \(\theta\), let a model have finite physical states \(S\), actions \(A\), delivered observations \(O\), audit outputs \(Z\), an initial joint law \(\mu_\theta(s,o_0)\), and kernel

\[
K_\theta(s',o,z\mid s,a).
\tag{I3}
\]

The controller uses its observed history \(h_t=(o_0,a_0,o_1,\ldots,a_{t-1},o_t)\). Permissions \(U(h_t)\) and initialization of controller memory are part of the supplied policy class. If memory or computations incur costs, retain their actual implementation in that class and record the costs in the required trajectory. No unlimited implementation ability is inferred from a stochastic policy formula.

Suppose a second description has bijections \(\phi:S\to S'\), \(\alpha:A\to A'\), \(\beta:O\to O'\), and \(\gamma:Z\to Z'\), with corresponding model labels, such that

\[
\begin{aligned}
\mu'_\theta(\phi(s),\beta(o_0))&=\mu_\theta(s,o_0),\\
K'_\theta(\phi(s'),\beta(o),\gamma(z)\mid\phi(s),\alpha(a))
&=K_\theta(s',o,z\mid s,a).
\end{aligned}
\tag{I4}
\]

Assume permissions, controller implementations, budgets, clocks, and normative labels transport as well. In particular, an action rename cannot depend on an unobserved physical state. Let \(T\) be the induced trajectory bijection.

**Proposition I1: faithful description transport.** Each admissible policy transports to an admissible policy by

\[
\pi'(\alpha(a)\mid T(h_t))=\pi(a\mid h_t),
\tag{I5}
\]

and their trajectory laws satisfy

\[
P^{\pi',\iota'}_\theta=T_*P^{\pi,\iota}_\theta.
\tag{I6}
\]

Consequently,

\[
\mathscr R'(\iota')=T_*\mathscr R(\iota).
\tag{I7}
\]

Every task remains feasible or infeasible when its acceptance set transports by the same map. In particular, continuation probabilities, viability regions over corresponding initial situations, independently specified burdens, and optimum values of faithfully transported costs agree.

**Proof.** Initial cylinder probabilities agree by the first equality in (I4). At each step, the policy factor agrees by (I5) and the transition factor agrees by the second equality in (I4). Induction proves equality for every finite cylinder. For infinite trajectories on finite alphabets, cylinder probabilities determine the path law. The bijections and transported policy class give the reverse construction. This proves (I6) and (I7), after which intersection with the corresponding acceptance set proves feasibility equivalence. ∎

The result is not the discovery of a new conservation law. It is an operational consistency condition: a mere change of coordinates cannot create an intervention, reveal a hidden observation, replenish a reserve, or authorize an action. A purported change of description that changes one of these has changed the modeled situation.

For a noninvertible reduction, equality requires more work. A faithful controlled quotient must preserve the required outcome labels, transition probabilities into quotient blocks for every relevant action, and actual observation interfaces. It must also establish policy lifting and preservation of the controller's attainable response set. State lumpability by itself does not entitle an observer to know the quotient state. One-way simulation generally yields only a corresponding inclusion or guarantee-transfer statement. These are the issues handled by controlled bisimulation and model-homomorphism methods, rather than arbitrary coarse-graining.

## 4. Two different orders: information and executable capability

The preceding construction identifies two orders that the theory must not collapse.

### 4.1 Capability order

For two situations with a common consequence space and common unresolved circumstances, define

\[
\iota_1\preceq_C\iota_2
\quad\Longleftrightarrow\quad
\mathscr R(\iota_1)\subseteq\mathscr R(\iota_2).
\tag{I8}
\]

This is a preorder. It means that every attainable response profile in the first situation can be matched in the second. It is stronger than improving one reward and does not require selecting such a reward.

**Proposition I2: universal task monotonicity.** Under (I8), every task feasible in situation 1 is feasible in situation 2. Conversely, if the task family contains every subset of the response-profile space, universal feasibility implication establishes (I8).

**Proof.** Any profile witnessing a nonempty intersection in (I2) remains in the larger set. Conversely, choose the singleton acceptance set containing an arbitrary profile attainable at situation 1. Its feasibility at situation 2 places that profile in the second attainable set. ∎

The converse uses an exceptionally rich task family, including singleton law profiles. Restricting tasks to a small list of practical thresholds may identify a weaker order. If one allows only expected-payoff comparisons, convexification and closure can matter; the exact set statement above should not be silently replaced by such comparisons.

The order is partial rather than a universal scalar gradient. One system may retain emergency action while another retains extensive deliberation. Unless one can reproduce all the other's relevant capabilities, neither dominates. A selection mechanism maximizing a narrower score can move downward in this order or produce incomparable tradeoffs.

### 4.2 Information order

For a finite one-stage problem, let an experiment \(E\) deliver signal \(x\) with law \(E_\theta(x)\). Let \(F\) deliver \(y\). Suppose a state-independent stochastic garbling \(G(y\mid x)\) satisfies

\[
F_\theta(y)=\sum_xE_\theta(x)G(y\mid x)
\quad\text{for every }\theta.
\tag{I9}
\]

Then \(E\) is at least as informative as \(F\) in the Blackwell sense.

**Proposition I3: information dominance gives capability inclusion when simulation is physically available.** Suppose the action sets, consequence law conditional on \((\theta,a)\), deadlines, permitted randomization, and implementation resources are the same; the signal acquisition does not alter those quantities; and implementing the garbling is allowed within the supplied resources. For every decision rule \(\delta_F(a\mid y)\), define

\[
\delta_E(a\mid x)=\sum_yG(y\mid x)\delta_F(a\mid y).
\tag{I10}
\]

The conditional action laws, and therefore all required action-dependent consequence laws, agree for every \(\theta\). Thus the attainable sets obey \(\mathscr R_F\subseteq\mathscr R_E\).

**Proof.** Substitute (I10), interchange the finite sums, and use (I9). The consequence laws then agree by their common conditional kernel. ∎

The relevant consequence contract here omits the raw signal identity unless that identity is itself simulated and included. If acquisition damage, costs, or privacy disclosure are required consequences, they must be preserved too; they cannot be erased to prove an information advantage.

Blackwell's result already establishes the statistical lineage. The alignment interpretation is that inference, storage, communication, attention, and action have physical implementations. Richer information is harmless only when the old executable policies remain available. If sensing consumes the only resource needed to act, a more informative post-sensing signal can accompany a smaller capability set. If sensing is optional and the old path genuinely remains available, choosing not to sense restores the inclusion; optional information is not thereby detrimental.

A sharp example: a binary state requires the matching action. One unit of energy is needed to perform either action, and the system initially has one unit. A passive, costless uninformative signal permits a randomized answer. A mandatory perfect measurement costing that unit leaves no energy for either answer. The second measurement dominates statistically but the overall intervention can no longer implement the required response. The distinction concerns different acquisition protocols, not a refutation of Blackwell's theorem.

## 5. All-task capability is weaker than full labeled causal equivalence

This distinction is necessary to prevent an attractive but false universality claim.

**Proposition I4: capability equivalence does not identify the complete intervention-response law.** Let there be one circumstance, two actions \(A=\{0,1\}\), and a binary outcome. Model M returns \(Z=a\), while model N returns \(Z=1-a\). Both permit all randomized action choices at equal cost. If the consequence contract concerns only \(Z\), both models attain exactly all Bernoulli outcome laws:

\[
\mathscr R_M=\mathscr R_N
=\{\operatorname{Bernoulli}(p):0\le p\le1\}.
\tag{I11}
\]

They agree on feasibility of every acceptance set of outcome laws. Yet the same labeled intervention \(\operatorname{do}(a=0)\) produces opposite outcomes. ∎

A faithful action relabeling makes them isomorphic, but if action names refer to fixed physical interventions, their causal answers differ. If the action trace or action-specific cost is part of the protected outcome contract, the capability sets can differ as well.

Therefore three levels must remain distinct:

1. Equivalent answers to the currently chosen tasks.
2. Equivalent sets of all attainable response profiles under a specified consequence interface.
3. Equivalent laws under each correspondingly labeled intervention or policy, including required action and cost traces.

The canonical response quotient in [the primary foundation](../../../history/2026-10-05-specialist-dossier/OPTIMAL-FOUNDATION.md) is based on declared labeled response questions. The capability set is valuable for action and alignment, but cannot replace that stronger predictive contract while retaining all its conclusions.

## 6. What follows for truth, reasonableness, and universality

The theory can establish necessary conditions for operationally defined abilities, such as answering a declared class of questions with bounded error, responding safely to distinguishable hazards, or retaining the ability to amend mistaken policies. It does not follow that persistence is truth or that reproduction is justification.

A minimal counterexample is enough: two machines execute exactly the same maintenance and action policies, but one contains an unread proposition that is false and the other a proposition that is true. Their maintenance dynamics can be identical. Unless truth of that proposition affects the task or implementation, persistence cannot distinguish them. Similarly, two persistent institutions can impose very different burdens on affected people. Evaluation requires preserving those people and burdens in the contract, not inferring legitimacy from durability.

The strongest productive reading of “reasonableness” is **the continued capacity to respond adequately to relevant differences in the world**. Its physical conditions include both distinguishing those differences and being able to act on them. The two orders above show why information without actionable capacity, or capacity without necessary information, can fail. This is a bridge from an operational epistemology to the reproduction of its conditions. It is not a definition of every philosophical sense of reason.

There is already direct physical prior art for part of this bridge: Kolchinsky and Wolpert define semantic information through interventions on correlations needed for persistence, and Sowinski and colleagues study information thresholds in a foraging model. We should distinguish their chosen viability criteria from our separately declared factual-answer and plural-acceptability contracts. A correlation can be causally useful to persistence without certifying every proposition represented by the system. Conversely, knowledge can be factually correct while its acquisition is unaffordable or its disclosure harmful.

There are at least four kinds of universality:

| Claim | Present status |
|---|---|
| Every instance satisfying the formal premises satisfies the theorem | Mathematical universality, established by the proofs |
| A faithful coordinate change preserves the specified operational consequences | Mathematical invariance, established for the stated transports |
| Every physical organization instantiates a particular selection–renewal loop | A substantive physical hypothesis, not entailed by the first two rows |
| One criterion supplies all factual truth or moral justification | Not established; persistence counterexamples block this inference |

Changing temporal units cannot manufacture a missing causal link. Extending a horizon or expanding a boundary can reveal slower maintenance and selection that a narrower description omitted. Such discovery supplies evidence for a richer model; it does not follow solely from formal reparameterization. The representation invariant should not be confused with a new numerical physical constant or with a conserved quantity along trajectories.

## 7. Primary-source positioning

The following sources establish important antecedents. Source descriptions are deliberately limited to the claims checked here; this is not an exhaustive novelty search.

- **Blackwell (1951), *Comparison of Experiments*.** Gives the comparison of experiments through attainable risks and stochastic sufficiency. It is direct prior art for the simulation argument and the connection between informative experiments and decision possibility. The 1953 continuation strengthens the equivalence theory; the elementary forward direction used above does not require its converse. [Original Berkeley proceedings paper](https://digicoll.lib.berkeley.edu/record/112749/files/math_s2_article-08.pdf), [1953 journal record](https://doi.org/10.1214/aoms/1177729032).
- **Shalizi and Crutchfield (2001), *Computational Mechanics: Pattern and Prediction, Structure and Simplicity*.** Develops predictive equivalence, optimality, and uniqueness of causal-state representations. These are established foundations of the earlier dossier's minimal representation claims. [Primary paper](https://arxiv.org/abs/cond-mat/9907176).
- **Barnett and Crutchfield (2015), *Computational Mechanics of Input-Output Processes*.** Extends the predictive-state construction to stochastic input/output channels. It is particularly close prior art for an intervention-sensitive representation architecture, with the appropriate causal and interface assumptions separately supplied. [Primary paper](https://arxiv.org/abs/1412.2690).
- **Ravindran and Barto (2003), *SMDP Homomorphisms: An Algebraic Approach to Abstraction in Semi-Markov Decision Processes*.** Supplies a formal abstraction framework for sequential decision systems. Its role here is to locate faithful reduction and policy transfer within established control abstractions; its reward-oriented setting does not itself settle plural normative acceptance. [Author-hosted proceedings paper](https://www.cse.iitm.ac.in/~ravi/papers/IJCAI03.pdf).
- **Montévil and Mossio (2015), *Biological Organisation as Closure of Constraints*.** Separates changing processes from relatively conserved constraints at a relevant timescale, and characterizes biological organization through interdependent maintenance. This is substantive prior art for reproducing enabling conditions and the user's timescale argument. It does not identify every physical change with organizational closure. [Author-hosted article](https://montevil.org/publications/articles/2015-mm-organisation-closure-constraints/).
- **Conant and Ashby (1970), *Every Good Regulator of a System Must Be a Model of That System*.** Proves a model requirement for successful, simple regulation under explicit assumptions. It is a close cybernetic antecedent, not authorization to claim every successful actor has a complete world model. Our limited-information and policy-feasibility results should be compared with its exact hypotheses. [Original article DOI](https://doi.org/10.1080/00207727008920220), [article facsimile](https://theisticscience.com/papers/tree/BioRegulation/Conant-IJSS1970.pdf).
- **Kolchinsky and Wolpert (2018), *Semantic Information, Autonomous Agency, and Nonequilibrium Statistical Physics*.** Defines semantic information as system–environment correlation causally required for maintaining existence, using correlation-scrambling interventions and a low-entropy viability criterion. This is direct antecedent work for a physical relationship between information and persistence. Its operational notion of semantic value should not be silently equated with all propositional truth or with normative justification. [Primary paper](https://arxiv.org/abs/1806.08053).
- **Sowinski et al. (2023), *Semantic Information in a Model of Resource Gathering Agents*.** Studies a resource forager whose expected lifetime depends on sensor-mediated interaction with its environment. Counterfactual sensor noise reveals a threshold beyond which lifetime declines substantially. This is close precedent for information-dependent continuation thresholds. The model-specific threshold is not an assertion that all physical systems share one universal numerical threshold. [Primary paper](https://arxiv.org/abs/2304.03286).

The potentially distinctive contribution is the integration of physically sustained information and action, plural acceptance, selection-induced transformation of the capability set, and legitimate revision and succession. Predictive minimality, description invariance, or the claim that information aids decision under suitable conditions are not new discoveries.

## 8. A concrete advance for the integrated theory

The root can now be organized without selecting a privileged inventory of variables:

\[
\text{situated physical process}
\longrightarrow
\text{actual information and executable policies}
\longrightarrow
\mathscr R(\iota)
\longrightarrow
\text{plural feasibility judgments}.
\tag{I12}
\]

Activity changes the initial situation for subsequent decisions, including resources, participants, information channels, and installed selection or amendment rules. Hence it changes the later attainable set. The mechanism question is **how present activity changes what becomes possible later**, and whether the realized dynamics preserve or restore the particular capacities that the evaluation contract requires.

This supplies an invariant target for the existing renewal and selection models. It does not dictate maximal expansion of every capability: some capabilities enable harm, some exclude each other, and creating one can consume another. Alignment requires assessed continuation and revision of the relevant abilities, with burdens and standing visible. The overall mathematical object is generally a feasible set and partial order, not one natural scalar gradient.

The theory's further scientific task is to derive nontrivial restrictions on the evolution of \(\mathscr R\) from mechanisms whose assumptions can be checked independently. That is where the account can explain collapse, lock-in, repair, learning, and institutional succession instead of merely redescribing successful continuation.
