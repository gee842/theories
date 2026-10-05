# Foundation before coordinates: optimality, interpretation, and prior art

Specialist positioning memo, 2026-10-05. Scope: foundational formulation, the strongest defensible meaning of optimality, relevant primary literature, and normative interpretation. This memo does not certify the accompanying mathematical implementation or establish empirical universality.

## Recommendation

Make the **intervenable process** primary, derive its **predictively necessary distinctions** relative to a declared interface, and retain the eight-tuple as an optional mechanistic realization. State normative commitments separately. This removes the apparent requirement that every system possess eight independent kinds of substance while preserving the existing theory's substantive contribution: selected activity can alter the conditions that enable activity, evaluation, correction, and future selection.

The strongest available optimality claim is exact and conditional: **for a fixed family of possible continuation experiments, the predictive-equivalence quotient is the coarsest deterministic sufficient summary of history, unique up to relabeling**. This is established causal-state and predictive-state mathematics. Its use here strengthens the foundation; it is not the novel alignment result.

## 1. Distinctions that should precede notation

**The process and its causal realization.** Physical, biological, institutional, and computational events occur and affect one another. The scientific task is to identify the dependencies needed for the question. A temporal input/output description is one observational and intervention boundary through that process; it neither derives spacetime nor implies that unobserved causes do not exist. Distributed events, spatial relations, delays, and shared causes can be represented when relevant. Adopting a single discrete clock is a scoped modeling choice.

**The inquiry contract, denoted Γ.** Declare the system boundary, histories available to each participant, outcome channels, interventions, horizon, disturbances, and the continuation questions that must be answered. Distinguish three different sets: interventions physically possible, interventions available to an actual controller, and interventions normatively permissible. An experiment used to define causal distinguishability need not be an authorized deployment action.

**The response law.** For each admissible history and experimental continuation, specify a coherent probability law over outcomes. Interventional responses must come from the causal model, experiments, or stated identification assumptions. Conditioning on an action chosen by an informed actor is not automatically the same law as externally imposing that action.

**The evaluation commitment, denoted E.** Identify whose interests and standing matter, protected outcomes and capabilities, acceptable risk, and legitimate revision procedures. A response law explains what happens; E evaluates it. The observer's decision to omit a harmed population is not a physical proof that the population is irrelevant.

The observer does not create the causal substrate. The observer does choose which distinctions a representation must preserve. This makes representation purpose-dependent without making empirical consequences arbitrary.

## 2. A precise optimality proposition

Here is a direct formulation for finite or countable recorded histories. It avoids additional measurability assumptions; continuous versions require their own regularity conditions.

Let \(\mathcal H_\Gamma\) be the admissible history domain and \(\mathcal T_\Gamma\) a specified family of continuation tests. A test includes the intervention protocol and the measurable outcome event. Let

\[
R_\Gamma(h)=\bigl(P_\Gamma(T\mid h)\bigr)_{T\in\mathcal T_\Gamma},
\qquad
h\sim_\Gamma h'\iff R_\Gamma(h)=R_\Gamma(h').
\]

Include currently relevant labels or intervention availability in the profile if those must also be preserved. Define \(\epsilon_\Gamma(h)=[h]_{\sim_\Gamma}\).

Call a deterministic history summary \(s:\mathcal H_\Gamma\to Z\) sufficient when every test probability can be recovered from \(s(h)\). Then there is a unique function on attained summary values

\[
f:s(\mathcal H_\Gamma)\longrightarrow
\mathcal H_\Gamma/\!\sim_\Gamma,
\qquad \epsilon_\Gamma=f\circ s.
\]

**Proof.** If \(s(h)=s(h')\), sufficiency gives identical responses to every declared test, hence \([h]=[h']\). Thus \(f(s(h))=[h]\) is well-defined and forced. Conversely, each test probability is constant on an equivalence class, so \(\epsilon_\Gamma\) is sufficient. Every sufficient partition therefore refines this quotient. Any two coarsest sufficient partitions induce the same equivalence and are isomorphic. □

This is a universal property within a specified representation problem. It yields the least number of attained classes among deterministic sufficient summaries. For a discrete random history, it also yields \(H(\epsilon_\Gamma(H))\leq H(s(H))\) when the entropies are defined. It does not minimize continuous differential entropy, source-code length, runtime, parameter precision, or the number of hidden states in a stochastic generator.

**Recursive state requires more than the partition definition.** The test family must include the observation events needed for updates and be closed under prefixing and residual continuation. For example, with fixed intervention sequences and positive denominator,

\[
P(w\mid hao,\operatorname{do}(v))
=\frac{P(ow\mid h,\operatorname{do}(av))}
{P(o\mid h,\operatorname{do}(a))}.
\]

Equal profiles then give equal updated profiles after the same action and observation. Off-support histories require separately specified continuation laws. Preserving adaptive policies requires nonanticipatory dynamics and preservation of the full observation information actually available to those policies. A summary computed using a central observer's privileged history must not be handed to a decentralized controller without justification.

If a new contract keeps every old test and adds more interventions, observations, or affected-outcome questions, its equivalence can only refine the old one. Minimality is therefore stable as a relative statement, while a changed inquiry can legitimately demand a richer state.

## 3. What optimality cannot mean

| Criterion | Defensible result | Restriction |
|---|---|---|
| Exact deterministic predictive summary | Coarsest sufficient history partition | Fixed response law and test family |
| Number of linear predictive coordinates | Rank of the system-dynamics matrix gives minimum linear predictive dimension | Linear readout convention; distinguish linear from affine coordinates and normalization |
| Bisimulation quotient | Coarsest behavior-preserving quotient within the stated transition-model class | Choice of labels, actions, observation rights, and equivalence matters |
| Smallest arbitrary hidden generator | Different optimization problem | Predictive quotient need not minimize it |
| Fastest, easiest to learn, most interpretable model | No conclusion from the quotient theorem | Resource, data, and explanation criteria must be added |
| Best moral or political arrangement | No conclusion from predictive minimality | Requires explicit normative premises and evidence |

A simple witness shows why the hidden-generator distinction matters. At initialization choose \(\Theta\in\{1/4,3/4\}\) with equal probability, then repeatedly emit independent Bernoulli\((\Theta)\) outputs. This has a two-state hidden generator with self-loops. After a finite recorded history of length \(n\) containing \(k\) ones, the posterior odds are \(3^{2k-n}\), and

\[
P(O_{n+1}=1\mid h)
=\frac14+\frac12\frac{3^{2k-n}}{1+3^{2k-n}}.
\]

These probabilities take infinitely many different values over finite histories. Any exact deterministic history predictor therefore needs infinitely many distinguishable predictive values, although the stochastic generator has two hidden states. This example concerns finite histories from an initialized experiment; it does not make the same claim about conditioning on a stationary, infinite observed past. Nor does it imply infinite linear dimension: infinitely many predictive states can lie in a finite-dimensional coordinate space.

Likewise, counting unconstrained real-valued variables is not a meaningful universal simplicity criterion: a scalar can encode many coordinates if arbitrary precision and decoding are free. Predictive minimality does not establish minimal mechanism, causal identifiability, compositional transparency, or efficient discovery from finite data.

## 4. Keep the eight-tuple as a substantive realization

The tuple \((x,e,c,a,m,\phi,\psi,r)\) names useful causal roles: activity, environment, capacity, authority, memory, representation, commitments, and rules. Preserve it as an explicit realization when those distinctions support intervention, diagnosis, or explanation. It need not be the canonical predictive state, and its components need not be independent or irreducible.

The theory should connect this realization to the interface by specifying how histories and interventions arise and which outcome laws the realization generates. A compressed predictor may answer every selected outcome question while hiding the local mechanism that destroys an institution's correction capacity. If the purpose includes intervening on that mechanism, add the corresponding intervention and outcome tests or retain the mechanistic model. Predictive compression alone does not discover the causal architecture of reproduction.

The central generative claim also must not become the tautology that successful systems possess whatever success requires. Define an enabling function independently through specified disruption/restoration tests, then investigate whether selected activity changes its availability, whether those changes alter subsequent selection, and whether the resulting feedback explains persistence or failure. The conditional mathematics can be complete while these domain-specific causal links remain empirically testable.

## 5. Endogenize commitments without identifying change with legitimacy

Actor goals, evaluative vocabularies, and installed amendment rules can be outcomes of the process. Their evolution may depend on learning, deliberation, selection, coercion, or institutional inheritance. An equation for \(\psi_{t+1}\) can describe all these causes without endorsing any of them.

The public evaluation E may itself permit change through a specified procedure that protects standing, dissent, evidence, and legitimate revision. This is a normative commitment to a revision process, not a hidden assumption of one immutable final utility. But no update becomes justified merely because the modeled system produced it. Preserve the distinction between an actual amendment and an amendment satisfying the declared legitimacy criteria. Version changes to E and retain enough history to prevent new standards from retrospectively erasing earlier injury.

The repository's earlier [public-normative plan](../../../../sources/06-zhishan/shengsheng/生生不息论v2/PLAN-v2.md) already distinguishes a generative account from public commitments and rejects deriving a unique morality from survival. Its [constitutive inquiry argument](../../../../sources/07-shengsheng-buxi/downloads-2026-07-08/2026-08-09-生生不息论-证明篇-v0.6.md) supplies a conditional necessity: sustained inquiry requires conditions that keep inquiry possible. Neither argument makes every self-reproducing order good. Those distinctions should survive the new mathematical presentation.

## 6. Primary-source positioning

The following are the closest foundations, rather than an exhaustive bibliography. Classical theorem descriptions were checked against the papers; the two newest preprints were checked at abstract and scope level only.

1. **Shalizi and Crutchfield (2001), computational mechanics.** Causal states group pasts with identical future distributions. Theorem 1, the refinement lemma, and subsequent minimality/uniqueness results establish the relevant lineage for sufficient predictive partitions. Our contract-dependent theorem should be presented as a scoped adaptation of this established idea. [Primary paper](https://arxiv.org/abs/cond-mat/9907176).

2. **Barnett and Crutchfield (2015), the ε-transducer.** This is the directly relevant input/output extension. Its maximal-prescience, minimal-complexity, and uniqueness results apply to declared channel processes and rival partitions of joint histories; the complexity statement depends on the input process. This is the strongest classical reference for controlled predictive state. It is not a proof that passive data identify arbitrary interventions. [Primary paper](https://arxiv.org/abs/1412.2690).

3. **Singh, James, and Rudary (2004), predictive state representations.** The system-dynamics matrix has histories as rows and continuation tests as columns. Lemmas 4–5 and Theorem 6 relate its rank to minimum linear predictive dimension. Section 5 explicitly distinguishes nonlinear sufficient prediction coordinates. Consequently, “minimum number of states,” “minimum linear dimension,” and “minimum nonlinear coordinates” must not be interchanged. [Primary paper](https://arxiv.org/abs/1207.4167).

4. **Givan, Dean, and Greig (2003), MDP equivalence and minimization.** This supplies established model-minimization and bisimulation foundations for the dossier's finite controlled reductions. It concerns equivalences on specified transition systems; it does not remove the need to declare observations, labels, and allowed control. [Author-hosted paper](https://engineering.purdue.edu/~givan/papers/mm.pdf).

5. **Rosas, Boyd, and Baltieri (2025), AI in a vat.** This is unusually close AI-safety prior art. Its Theorem 3 identifies the minimal bisimulation of a predictive world model with its ε-transducer; Corollary 2 gives predictive-model minimality. It also distinguishes predictive from more general world models and studies efficiency/interpretability tradeoffs. Any claim that our work newly establishes the uniquely optimal predictive world model would conflict with this precedent. [Official proceedings record](https://rlj.cs.umass.edu/2025/papers/Paper367.html).

6. **Baez and Pollard (2017), compositional reaction networks.** Open reaction networks compose through explicit boundary ports, with functorial dynamical and steady-state semantics. This is useful if the project assembles local enabling processes into larger mechanisms. It supports disciplined composition, not a universal ontology or moral inference. A steady-state equivalence does not by itself preserve transient hazards. [Primary paper](https://arxiv.org/abs/1704.02051).

7. **Boyd, Nowak, Hyland, Baltieri, and Rosas (2025; revised 2026), From monoliths to modules.** This preprint develops decomposition of transducer world models into sub-transducers on distinct input/output subspaces. It is material prior art for claims about deriving modular architectures or distributed inference from the process representation. Its detailed factorization conditions need review before importing the construction. [Primary preprint](https://arxiv.org/abs/2512.02193).

8. **Baltieri, Torresan, Zhang, Boyd, and Rosas (2026), World models of environment, agent and joint agent-environment systems.** This preprint distinguishes the environment channel, agent channel, and realized joint process, and reports canonical constructions under closed-loop support restriction. It exhibits a finite restricted model despite an infinite unrestricted environment model. The practical implication for our framing is that observed success under installed coupling cannot establish robustness under omitted interventions. The paper is very close prior art for boundary- and coupling-dependent canonical state. [Primary preprint](https://arxiv.org/abs/2608.20401).

## 7. Proposed claim and review questions

**Proposed claim.** We formulate alignment as a property of an intervenable, historically evolving process whose activity can transform the conditions of future activity, correction, and evaluation. Relative to an explicit inquiry contract, established predictive-state mathematics supplies a canonical sufficient representation and precisely delimits compression. A separate causal realization identifies reproduction mechanisms, and explicit public commitments govern the assessment and legitimate revision of their consequences. The proposed contribution is the integration and operational consequences of these layers, not the discovery of predictive minimality or a unique ontology.

Before describing the resulting formulation as optimal, reviewers should be able to answer:

- Which histories, channels, tests, and interventions define the equivalence, including interventions excluded by current institutional power?
- Is the claim about all admissible continuations, the installed controller, or only continuations present in observed data?
- Which minimality class is intended: deterministic predictive partitions, linear coordinates, causal mechanisms, or computational implementations?
- Are observation restrictions preserved for each participant, rather than replaced by centralized access?
- Are enabling dependencies tested independently of success, and are reproduction claims causal rather than definitional?
- Does changing the normative commitment remain distinguishable from improving outcomes under a commitment?
- Which integration results go beyond the cited foundations, and which are already established mathematics?

With those answers explicit, the foundation can be stronger than the eight-tuple alone without claiming a model that is best for every scientific or normative purpose.
