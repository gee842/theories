# Selection and the renewal of generative conditions

Foundation draft 0.1, 4 October 2026. Prepared in response to Ren's request for deep, holistic development of equations describing what spreads together with what makes continued becoming possible across biological, human, and AI systems. The conceptual direction is Ren's; this document is AI-generated synthesis and mathematical analysis, not his verbatim prose. Three research agents examined dynamics, generative capacities, and cross-domain validity; the coordinating agent integrated their findings and checked the illustrative model. Separate agents are not independent human peer review.

**Working thesis.** Reproduction, learning, and selection change the prevalence of forms while changing the conditions through which subsequent forms can arise, persist, respond, repair, and transform. A useful theory must explain both processes together. Regeneration occurs through the renewal of specified enabling functions; degeneration occurs through their loss. Neither can be inferred from competitive success alone.

This draft provides a common model architecture, exact accounting relations, proposed operational definitions, conditional results, and a program of empirical tests. It does not establish a universal law of society, a complete formalization of 生生, a solution to AI alignment, or the originality of its mathematical ingredients. The intended foundational contribution is a restrictive and testable integration, not an unrestricted equation that can fit any story.

## The distinctions the theory must preserve

Three objects must remain separate: actual dynamics, counterfactual capacities, and the justification of what deserves protection. A process may reproduce successfully while exhausting its support; it may retain a possible remedy while losing the institutions that would implement it; it may remain stable while denying affected people legitimate recourse.

The [corpus definition of 生生](../../GLOSSARY.md) concerns actualization that also preserves, restores, or creates the conditions for another round of generation. It permits metabolism, death, replacement, rest, and transformation. It does not require one identity to persist forever, or population, diversity, novelty, complexity, or efficiency to increase monotonically. The existing four criteria, six protection functions, and seven gauges remain distinct formulations that need reconciliation; this draft does not silently replace them with a single score.

Five distinctions organize the mathematical work:

1. **Composition and scale.** What fraction follows a practice differs from how much population or activity remains.
2. **Stocks and renewal.** An accumulated resource can remain large after its replenishment mechanism has failed.
3. **Persistence and recovery.** A functioning system can lose the ability to withstand or recover from disturbance.
4. **Possible and delivered action.** An available policy need not be selected, funded, authorized, or executed.
5. **Descriptive and protected capacities.** The ability to reproduce or exercise control is not automatically a capacity that ought to be preserved.

## State and elementary mechanisms

Begin with a declared system boundary, time horizon, carrier, and transmission mechanism. Let

\[
Y=(n,E,S),
\]

where \(n_i\) is the absolute abundance of type \(i\), \(E\) records enabling stocks and functional capacities, and \(S\) records the conditions shaping selection and transition. Types may describe genotypes, practices, organizational forms, or deployed policies, but the carrier and its unit must be specified separately in each application. \(E\) and \(S\) are causal roles: if one physical variable performs both roles, it is one state variable, not two independent copies.

Material stocks, machinery, knowledge, and authority require different units and production relations. A network, age structure, belief state, or historical memory belongs in an expanded state whenever the proposed aggregate variables cannot predict their own subsequent change. The concise notation is not permission to hide causally necessary variables.

Three elementary events give a useful starting point:

| Event | Mechanism | Rate specification |
|---|---|---|
| Reproduction with variation | A carrier of type \(i\) produces a new carrier of type \(j\) | \(n_i b_i(Y)Q_{ij}(Y)\) |
| Disappearance | A carrier of type \(i\) is removed | \(n_i d_i(Y)\) |
| Within-carrier change | A carrier changes from \(i\) to \(j\) without adding a carrier | \(n_i k_{ij}(Y)\) |

The rates \(b_i,d_i,k_{ij}\) are nonnegative and \(\sum_jQ_{ij}=1\). Learning, imitation, replacement, and birth are not assumed identical. Pairwise interactions, recombination, entry, migration, merging, and splitting require the corresponding additional events. “Fitness” should be derived from these independently specified mechanisms rather than inferred retrospectively from success and then used to explain that same success.

For integer counts, these events define a stochastic process coupled to changes in \(E\) and \(S\). Finite populations can become extinct by chance even where a deterministic approximation predicts persistence. With appropriate scaling and regularity assumptions, the deterministic balance is

\[
\boxed{
\begin{aligned}
\dot n_i
&=\sum_jn_jb_jQ_{ji}-n_id_i
  +\sum_j(n_jk_{ji}-n_ik_{ij}),\\
\dot E&=F(n,E,S,u,w),\\
\dot S&=H(n,E,S,u,w).
\end{aligned}}
\tag{1}
\]

Here \(u\) denotes actions that are actually feasible under the current information, resources, and authority; \(w\) denotes disturbances. If action selection is part of the problem, its policy must itself be included in the dynamics. A free external controller cannot stand in for the institution whose persistence we seek to explain.

Equation (1) is generally a large-population approximation, not an exact equation for expected stochastic counts. Nonlinear rates introduce correlations and higher moments. The [mathematical memo](../../_process/research/2026-10-04-integrated-evolution/integrated-dynamics.md) gives an explicit event generator. [Champagnat, Ferrière, and Méléard](https://arxiv.org/abs/math/0510453) supply a primary precedent for deriving different deterministic and stochastic limits from individual events; [Bhat](https://arxiv.org/abs/2406.10739) develops a related finite-population field theory.

For continuous traits, sums become kernels and, under suitable small-step assumptions, drift and diffusion. A diffusion term is not a general theory of creativity. Variable-length programs, graphs, or genomes can represent unbounded structural possibilities, but their accessible transitions and functional meaning still require explanation. [Taylor's analysis of open-ended evolution](https://arxiv.org/abs/1806.01883) helps distinguish exploration within a representation from expansion and transformation of accessible possibilities.

## The equations for what spreads

Assume no external entry for this reduction. Let

\[
N=\sum_i n_i>0,\quad p_i=\frac{n_i}{N},\quad
r_i=b_i-d_i,\quad \bar r=\sum_i p_ir_i.
\]

Summing (1) and differentiating the shares gives the exact identities within the deterministic model:

\[
\boxed{\dot N=N\bar r,}
\tag{2}
\]

\[
\boxed{\dot p_i=p_i(r_i-\bar r)
 +\sum_jp_jb_j(Q_{ji}-\delta_{ji})
 +\sum_j(p_jk_{ji}-p_ik_{ij}).}
\tag{3}
\]

Selection, inherited variation, and within-carrier change therefore contribute differently. Without variation or switching, (3) is the replicator equation. These relationships belong to established evolutionary mathematics, including [Page and Nowak's unification](https://www.homepages.ucl.ac.uk/~ucackmp/Publications_files/unifying.pdf).

**An identification limit.** At the same full state, a common addition to every net growth rate cancels from the selective part of (3), while changing (2). Entire share trajectories remain identical only when the altered abundance or environment does not subsequently change relative rates or transition terms. This restriction matters: environmental feedback can make initially invisible damage visible later. Even in the restricted class, however, shares alone cannot identify absolute viability. The fully specified model below demonstrates identical improving share trajectories with opposite long-run outcomes under the same parameters.

General game dynamics need not ascend a common scalar objective. Cycles and history dependence are admissible outcomes. A local selection gradient describes differential spread; a Lyapunov function, where one exists, describes a property of the stated dynamics. Neither supplies a moral gradient.

## Coupling selection to renewal

For a specified support stock \(E_\alpha\), use the accounting form

\[
\dot E_\alpha=R_\alpha(E,t)+N\bar q_\alpha,
\qquad \bar q_\alpha=\sum_i p_iq_{i\alpha}(Y,t).
\tag{4}
\]

\(R_\alpha\) records identified background renewal, loss, and boundary inputs. \(q_{i\alpha}\) is a type's net contribution per unit abundance, in stock-per-carrier-per-time units. It may be positive or negative and may change with context. This decomposition must follow a defensible process model. Interactions do not always admit a unique allocation of contribution to individual types; an arbitrary accounting allocation is not a causal estimate.

The factor \(N\) is essential unless exposure has explicitly been held fixed or normalized. The same composition at ten and a billion active carriers can exert different loads. Local replenishment financed by depletion outside the boundary also needs to be recorded before claiming regeneration at the larger scale.

Define

\[
(\mathcal Tq_\alpha)_i
=\sum_j(b_iQ_{ij}+k_{ij})(q_{j\alpha}-q_{i\alpha}).
\]

Equations (2)–(3) and the product rule yield

\[
\boxed{
\frac{d\bar q_\alpha}{dt}
=\underbrace{\operatorname{Cov}_p(q_\alpha,r)}_{\text{selection}}
+\underbrace{\mathbb E_p[\mathcal Tq_\alpha]}_{\text{transmission and switching}}
+\underbrace{\mathbb E_p[\dot q_{i\alpha}]}_{\text{changing context}}.}
\tag{5}
\]

The final derivative follows changes in abundance, environment, technology, and selectors along the trajectory. For total contribution \(J_\alpha=N\bar q_\alpha\),

\[
\boxed{
\dot J_\alpha=N\left[
\bar r\bar q_\alpha+\operatorname{Cov}_p(q_\alpha,r)
+\mathbb E_p[\mathcal Tq_\alpha]
+\mathbb E_p[\dot q_{i\alpha}]
\right].}
\tag{6}
\]

This is a Price-style balance specialized to renewal, not a claimed new universal theorem. It identifies distinct sources of improvement or deterioration: what selection favors, what transmission changes, what growing scale does, and how the effectiveness of practices changes.

For each support function, \(A_\alpha=\operatorname{Cov}_p(q_\alpha,r)\) is a candidate diagnostic of the selective contribution to changing renewal. It is not an overall alignment score. Positive covariance can favor less damaging types while every type still imposes a net loss; negative covariance can be outweighed by renewal elsewhere. Neither sign alone establishes collapse, recovery, or justice. Measuring this term independently and testing whether it predicts later support dynamics would give the hypothesis empirical content.

Material submodels can additionally impose stoichiometric balances, for example \(\dot B=Av+I-L\), where reaction fluxes \(v\), external inputs \(I\), and losses \(L\) have compatible units. Functional capacity can follow \(\dot C_\alpha=P_\alpha-L_\alpha\). A stable capacity can depend on continuous production replacing continuous loss. Material conservation does not imply fictitious conservation laws for truth, authority, or useful knowledge.

## Continued becoming as a profile of capacities

The equations describe trajectories. To evaluate the conditions for continued becoming, specify a family of tests indexed by affected parties or reference systems, required functions, disturbances, budgets, deadlines, and failure tolerances. Let \(\mathcal K\) encode independently justified protected constraints.

Define \(\mathcal C_{\mathcal E}(Y)\) as the set of tests that can be accomplished from state \(Y\), using actual information, resources, and decision rights, within the specified time and reliability bounds. A test may concern renewal, recovery, revision, transmission to successors, or demonstration of a new useful function. This is a proposed operationalization, not the complete meaning of 生生.

At a fixed specification, inclusion

\[
\mathcal C_{\mathcal E}(Y')\supseteq\mathcal C_{\mathcal E}(Y)
\tag{7}
\]

means that the protected tests attainable before remain attainable afterwards. Many transitions are incomparable. Raw option counts are inadequate, and dangerous powers need not be included among protected capabilities. Legitimate transformation may remove a harmful capability or retire an obsolete form.

For each test, distinguish the best feasible outcome from the outcome under actual evolving policies. An optimizer over controls establishes possibility; it does not establish implementation. The gap can be caused by lost understanding, authority, resources, incentives, or time. [Viability-based resilience analysis](https://ecologyandsociety.org/vol9/iss2/art8/print.pdf) provides established tools. The prospective extension is to endogenize the institutions and resource flows that make controls feasible and selected.

Successor transmission can be modeled by a kernel over replacement, reproduction, training, or institutional succession. Finite-generation recursion then asks whether successors inherit functioning renewal mechanisms and can transmit them again. It need not preserve identity or shape. It also cannot certify regeneration unless the state records renewal functions and the constraints specify what is protected; otherwise a frozen state qualifies automatically.

An operational regenerative episode restores or establishes specified renewal mechanisms and protected capacities over the declared horizon. A degenerative episode weakens them relative to an explicit comparison. These are proposed definitions. Temporary loss can accompany regeneration when a permitted transition restores functions by a deadline; some protected constraints may remain inviolable throughout. Infinite-horizon survival is not assumed for finite organisms or systems facing accumulating hazards.

In human and AI settings, agency, standing, distribution of burdens, and legitimate revision are explicit ethical commitments. A stable prison can satisfy persistence and reproduction conditions while failing these commitments. An innovative exploitative system can invent continually while shrinking others' protected capacities. The equations do not resolve that normative choice.

## A minimal model with degeneration and regeneration

The following model is deliberately small enough to analyze. It isolates a mechanism; it is not fitted to biological, social, or AI data and has no verified originality claim.

Let \(x\) be the share of maintainers, \(N\) total abundance or consistently defined activity, and \(E\) a maintained support stock. Maintainers pay cost \(c>0\); both types depend on support. A parameter \(\theta\geq0\) changes the relative return through net growth terms

\[
r_R=aE-m-\gamma N-c+\theta(1-x),\qquad
r_D=aE-m-\gamma N-\theta x.
\]

The weighted transfer terms cancel. They balance growth effects, not automatically physical money, matter, or energy; a literal tax/subsidy interpretation needs compatible conversion efficiencies and enforcement costs. With all other parameters positive,

\[
\boxed{
\begin{aligned}
\dot x&=x(1-x)(\theta-c),\\
\dot N&=N[aE-m-\gamma N-cx],\\
\dot E&=\rho Nx(1-E/K)-\delta E.
\end{aligned}}
\tag{8}
\]

Renewal depends on absolute maintenance \(Nx\). \(E\) is functional support, not energy created from nothing. The model assumes the physical throughput needed for maintenance remains available within its applicable regime; a complete material model must include that throughput. No constant external injection of \(E\) is assumed. Fixed \(\theta\) isolates an incentive mechanism; the persistence of the institution implementing it is not proved.

For \(0\leq E_0\leq K\), \(E\) stays in that interval. \(N\) stays nonnegative and bounded by logistic comparison. The mathematical extension of \(x\) at \(N=0\) has no empirical interpretation as a living population.

**Conditional result 1.** If \(\theta<c\), \(N_0>0\), and \(x_0<1\), then \(x\to0\), \(E\to0\), and \(N\to0\). The logistic share equation makes maintenance disappear. Bounded \(N\) implies \(Nx\to0\); the support equation then gives \(E\to0\). Eventually \(aE<m/2\), forcing \(N\) to decline exponentially. This result relies on costly maintenance, indispensable shared support, no alternative renewal, and the specified competitive advantage. The all-maintainer boundary is an exception because this version has no mutation or invasion.

**Conditional result 2.** If \(\theta>c\), maintainers spread whenever present, but this does not guarantee recovery. On \(x=1\), define \(M=m+c\) and \(H=\delta K/\rho\). There are two distinct positive equilibria precisely when

\[
\boxed{aK>(\sqrt M+\sqrt{\gamma H})^2.}
\tag{9}
\]

They are

\[
N_\pm=\frac{aK-M-\gamma H
\pm\sqrt{(aK-M-\gamma H)^2-4\gamma HM}}{2\gamma},
\qquad E_\pm=\frac{KN_\pm}{H+N_\pm}.
\tag{10}
\]

The lower equilibrium is a saddle and the upper one is locally asymptotically stable. The additional share eigenvalue is \(-(\theta-c)\). Extinction remains locally asymptotically stable too. At equality in (9) there is one positive nonhyperbolic equilibrium; below it there is no positive equilibrium on this boundary. The [mathematical memo](../../_process/research/2026-10-04-integrated-evolution/integrated-dynamics.md) supplies the derivation.

Thus favorable selection and adequate regenerative stocks are different requirements. Some disturbances are repaired near the positive equilibrium; sufficiently depleted states can remain in the extinction basin. We have not derived the full global basin boundary. More compensation also need not improve survival monotonically: faster maintenance adoption raises both support production and its immediate cost. The positive equilibrium values do not depend on \(\theta\) once everyone maintains; the parameter changes composition and its path.

![Illustrative trajectories separating maintainer share, abundance, and support](/Users/ren/theories/_process/research/2026-10-04-integrated-evolution/regeneration-regimes.png)

The illustration uses \(a=5,m=.8,c=.2\) and \(\gamma=\rho=\delta=K=1\). Then \(N_+\approx2.618\) and \(E_+\approx.724\). From \((x,N,E)=(.9,2.5,.7)\), \(\theta=.1\) leads to collapse and \(\theta=.4\) approaches the positive equilibrium. With \(\theta=.4\) but depleted initial stocks \((.9,.05,.05)\), the same maintainer-share trajectory accompanies collapse. This is an illustration of the specified dynamics, not empirical evidence for a social prediction.

Collapse from the displayed depleted start also has an analytic certificate. For these parameters, the box \(0<N\leq.05,\ 0\leq E\leq.05,\ 0\leq x\leq1\) is forward invariant: throughout it, \(\dot N/N\leq5(.05)-.8=-.55\), and at its upper support boundary, \(\dot E\leq.05(.95)-.05=-.0025\). The other boundaries point inward or are invariant. Thus \(N\to0\) exponentially; the support equation then implies \(E\to0\). This proves collapse for this initial condition independently of the finite numerical horizon.

The numerical check used the exact logistic share solution, positive logarithmic population and support coordinates, equilibrium residuals, Jacobian eigenvalues, and tighter integration tolerances. Maximum state discrepancies under tolerance refinement were below \(6\times10^{-10}\). [Saved checks](../../_process/research/2026-10-04-integrated-evolution/regeneration-model-checks.json) and the [reproducible calculation](../../_process/research/2026-10-04-integrated-evolution/verify_regeneration_model.py) accompany the figure. These checks support the illustrative computation; they do not establish model validity or originality.

## How the selection conditions themselves persist

Equation (8) leaves \(\theta\) fixed. Equation (1) exposes the next question through \(\dot S=H\): who maintains, finances, appoints, and revises the mechanism that changes the returns to maintenance?

The existing [selector manuscript](../../drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/src/core/40_s4.md) already derives conditional selection for influence over correctors. Its return depends on appropriability, persistence, carrier share, costs, and transmission. Its correction-rate result depends on particular cost elasticities and adaptation conditions. Those are special cases to connect to this framework, not universal exponents to impose on every system.

The [earlier contribution assessment](2026-10-04-alignment-coordination-contribution-space.md) adds an illustrative model in which selected influence erodes effective authority despite adequate nominal oversight. In the integrated state, authority and knowledge are maintained capacities with their own production and loss terms. Evaluation quality is an observation process; reported condition \(y=h(E,S)+\epsilon\) must be distinguished from actual support. The same successful actor can affect both the physical condition and how it is reported.

This yields three coupled obligations for a proposed intervention: make relevant maintenance viable under selection; reach a state with enough absolute support and repair capacity; and sustain the institutions implementing the change under their own incentives. Each can fail independently. Explaining the third requires mechanisms and comparative cases rather than an indefinitely guaranteed supervisor.

Regeneration is compatible with some competitive arrangements; coordination inside one organization can harm outsiders. The theory must identify the returns, externalities, boundaries, and constraints that distinguish those outcomes. A cooperative proposal should face the same tests for capture, dependency, and loss of revision as the arrangement it seeks to replace.

## Transfer across biological human and AI systems

The claim of a shared foundation has three levels: common vocabulary, a verified mapping to the same restricted mathematical structure, and successful transport of intervention predictions. The third is the research target. Similar phase portraits alone are insufficient.

| Role | Biological case | Human institutional case | AI ecosystem case |
|---|---|---|---|
| What spreads | Inherited cell variants | Practices through observed adoption or organizational succession | Policies or designs through deployment, replacement, and allocation |
| Absolute scale | Cells per volume | Number or intensity of relevant activities, with units fixed in advance | Deployed instances, task volume, or compute allocation with its actual allocation law |
| Enabling conditions | Resources, tissue function, public-good production | Infrastructure, ecological stocks, skills, shared evidence, enforceable access | Compute and energy, data quality, human expertise, evaluation access and authority |
| How selection changes | Environment and encounter structure change reproductive returns | Success changes access, rules, funding, or appointments | Deployment changes data and tasks; successful lineages may influence evaluation |
| Independent outcomes | Recovery, absolute abundance, host function, extinction | Regeneration of functions, distribution of burdens, successful legitimate remedies | Independently assessed usefulness, repair after adverse evidence, implemented authorized correction |

Biological reproduction and human adoption cannot simply be assigned the same rates. Weight updates inside one AI differ from selection among AI designs. Money and compute shares change through allocation and transfer, not necessarily reproduction. People are rights-bearing participants, not morally ranked carrier types.

A strong biological anchor is [Sanchez and Gore's yeast experiment](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1001547). It measured composition and abundance over generations: some small populations collapsed while cooperation frequency increased, while larger populations reached coexistence. Similar equilibrium density could conceal reduced resilience. These observations support the need for separate variables; they do not validate equation (8). Cancer requires a particular cell–environment–host model and independent host outcomes, not a universal attractor shape or a moral analogy about human groups.

[Ostrom, Walker, and Gardner's experiments](https://www.wtf.tw/ref/ostrom_1992.pdf) provide a human precedent for manipulating communication and sanctioning in resource governance. [Performative prediction](https://proceedings.mlr.press/v119/perdomo20a.html) supplies a formal AI example in which decisions change later data distributions. Neither is by itself evidence for every feedback in the integrated model.

## Existing foundations and the prospective contribution

The event model, replicator reduction, Price identities, ecological public goods, niche construction, viability, and institutional feedback have substantial prior art. [Hauert, Holmes, and Doebeli](https://pmc.ncbi.nlm.nih.gov/articles/PMC1634915/) couple evolutionary games to variable population density. [Weitz and colleagues](https://pmc.ncbi.nlm.nih.gov/articles/PMC5127343/) analyze strategy–environment feedback with several possible dynamical regimes. [Harré](https://arxiv.org/abs/2507.13616) explicitly connects institutional evolution and AI governance. Broad integration alone therefore cannot be presented as a first discovery.

Biological work on [closure of constraints](https://montevil.org/publications/articles/2015-mm-organisation-closure-constraints/) asks how functioning processes maintain the constraints enabling them. This technical “closure” can support responsiveness and renewal; it must not be confused with the normative 闭 in Ren's vocabulary. Structural interdependence still requires adequate rates, resources, and resilience.

The prospective contribution is more specific: connect independently measured renewal and intervention capacities to endogenous selection, derive useful conditions for their persistence and loss, and test whether the resulting restrictions travel across domains. The exact renewal balance, the maintained-stock example, and the authority extension provide starting points, with originality still to be audited result by result.

## Tests and counterexamples that constrain the theory

An empirical program should record absolute exposure, composition, support stocks, maintenance flows, rule changes, and intervention timing. It should test closure: if history or hidden composition predicts changes after conditioning on the proposed state, the state description is insufficient.

The first discriminating tests are:

1. Vary total abundance at matched composition, then support stock at matched abundance. Test whether the predicted recovery boundary is observed.
2. Withdraw and restore maintenance at several delays. Test whether current output conceals loss of recovery capacity and whether repair arrives too late.
3. Change returns to maintenance independently of direct support. Separate selection-mediated effects from subsidies that simply replenish the stock.
4. Randomize authority over evaluation separately from performance where feasible. Test whether nominal oversight survives changes in who controls it.
5. Estimate a restricted model in one setting and predict withheld interventions, then test a mapped mechanism in another setting with independently estimated parameters.

For AI evaluator succession, retain fixed-rule, endogenous-amendment, exogenous-replay, and randomized-authority conditions. Include legitimate beneficial amendments and independent outcome measures. The local [20-seed pilot](../../drafts/2026-10-02-iaseai-selecting-the-selectors/experiment/PREDICTIONS-2.md) failed its P1 prediction; that negative result remains part of the record. Its revised design has no saved run identified in the existing plan. This work ran only the illustrative mathematical checks, not a new benchmark or human experiment.

The framework must accommodate stable coexistence, successful competitive maintenance, collapse despite increasing cooperation, transient damage during legitimate regeneration, inventive exploitation, and institutions that remain stable while denying recourse. If it explains only decline, it is missing mechanisms. If every possible outcome can be explained after choosing new functions, it has insufficient predictive restriction.

## What is established in this draft

| Statement | Status |
|---|---|
| Population change can be derived from specified reproduction, disappearance, and transition events | Established framework; application requires explicit assumptions |
| Equations (2)–(6) follow from the stated deterministic balance | Exact identities within the model; not independent empirical laws |
| Relative shares alone can fail to identify absolute viability | Derived identification limit with stated restrictions and a concrete example |
| Equation (8) supports collapse, stable regeneration, and failed rescue despite favorable selection | Conditional analytic results; numerical illustration verified |
| Regeneration can be operationalized through maintained and transmissible capacity profiles | Proposed definition requiring public and scientific scrutiny |
| The same restricted mechanisms explain biological, human, and AI outcomes | Research hypothesis requiring separate mappings and intervention tests |
| Preserving protected capacities supplies a complete ethical theory or solves alignment | Not established |

The next theoretical task is to make selector maintenance endogenous without assuming its success, while preserving tractability. The next empirical task is to identify which additional observations beyond current performance reveal lost regenerative and corrective capacity. Those tasks should determine how the theory grows.

## Supporting research records

- [Mathematical foundation](../../_process/research/2026-10-04-integrated-evolution/integrated-dynamics.md)
- [Generative capacities and normative boundaries](../../_process/research/2026-10-04-integrated-evolution/generative-capacity.md)
- [Cross-domain audit](../../_process/research/2026-10-04-integrated-evolution/cross-domain-audit.md)
- [Earlier contribution map](2026-10-04-alignment-coordination-contribution-space.md)
- [Numerical checks](../../_process/research/2026-10-04-integrated-evolution/regeneration-model-checks.json)
- [Figure as SVG](../../_process/research/2026-10-04-integrated-evolution/regeneration-regimes.svg)
