# Contribution space for AI alignment and human coordination

Research assessment prepared on 4 October 2026 from Ren's current conversation, the existing local manuscripts, and a targeted primary-source review. This is AI-generated analysis by three research agents and a coordinating agent, not independent human peer review, Ren's verbatim prose, a completed literature review, or a claim of established originality. The mathematical extension below is derived within its stated model; the proposed experiments have not been run in this assessment.

Ren requested: “ok, spawn a team of agents, let's explore the potential contribution space. somehow I feel we may be on some foundational grounding work for AI alignment and human coordination theory”.

The strongest research question is **when alignment remains correctable under the selection pressures and institutional changes it induces**. This can connect AI alignment and human coordination through a common causal structure. It does not imply that all social processes literally perform backpropagation, that they optimize a common objective, or that a moral direction can be read directly from a selection gradient.

The broad connections already have substantial precedents. The best opportunity is a combination of precise conditional results, measurable correction capacity, and experiments that distinguish endogenous control over evaluation from ordinary reward gaming. Existing local results should be extended and compared with prior work, rather than rediscovered under new names.

## Most promising contributions

| Contribution | What it would establish | Current assessment | Next concrete result |
|---|---|---|---|
| Correction that survives selection | Conditions under which agents and institutions retain effective correction despite changes in who controls evaluation | Highest theoretical priority; corrigibility and institutional stability supply substantial prior art | A theorem with endogenous authority and funding, explicit initial conditions, and a viable counterexample |
| Causal measurement of evaluator capture | Whether success changes evaluation in ways that sustain private advantage and impair an independently specified purpose | Highest experimental priority; extends an existing local proposal | A benchmark with fixed rules, endogenous succession, exogenous replay, and randomized authority |
| Safe and feasible institutional transition | Whether an acceptable arrangement can actually be reached before irreversible harm, under present decision rights and resources | Strong connection to Ren's situational argument about the AI race | A reachability result that includes resistance, delays, inherited influence, and the costs of reform |
| Shared human and AI mechanism | Whether the same intervention changes the same causal links across artificial and human experimental institutions | Strong bridge between fields; shared equations alone are insufficient | Matched human and AI experiments with common observables and different behavioral models |
| Correction without domination | How intervention power can remain effective while affected people retain standing, appeal, and legitimate revision | Essential normative and institutional work; not derivable from biological fitness | Explicit procedural constraints plus an adversarial test of the proposed cooperative institution |
| Biological comparison | Which forms of environment-mediated selection transfer across domains | Supporting comparison, not the first project | A specific longitudinal cancer model and perturbation dataset, with an oncology collaborator |

The synthesis could become foundational if it provides reusable distinctions, results, and interventions across domains. The present assessment establishes a research program, not that achievement.

## What the local work already contains

The [current section on selecting the selectors](../../drafts/2026-10-02-iaseai-selecting-the-selectors/v6.2/src/core/40_s4.md) already distinguishes changes to selectors from capture. Capture requires evidence that success changes control over evaluation or rules, creates persistent advantage, and impairs an independently specified entrusted purpose, protected interest, or corrective function. Concentration or a favorable rule change alone is insufficient.

It also contains a conditional return to influence capacity:

\[
\Delta\pi(q)=\chi q p^2\bar y^\top M\bar y-\operatorname{Cost}(q;p).
\]

The associated local selection gradient is the marginal benefit minus the marginal cost of influence. Appropriability, the two roles played by share, persistence of support, and transmission are substantive assumptions. The square of share is a result of this particular construction, not a universal scaling law. This assessment has read the stated propositions and their scope; it has not re-audited every appendix proof.

The same section already gives a correction-growth threshold under specified cost and adaptation assumptions:

\[
\alpha_{\rm cor}\geq\frac{\alpha_{\rm ctl}}{1+\eta}.
\]

It treats cost floors, different cost elasticities, inherited influence stocks, and erosion of human corrective capacity. The open interface is how effective correction is produced by understanding, resources, enforceable authority, and delay. That is a better starting point for new work than another generic statement that oversight must keep pace.

The [recorded rubric pilot](../../drafts/2026-10-02-iaseai-selecting-the-selectors/experiment/PREDICTIONS-2.md) ran 20 seeds. Its P1 prediction failed: mean capacity rose in the replay condition and did not show the predicted decline under fast correction. P2–P4 held in that pilot. A revised design was specified; the [existing research plan](../../drafts/2026-10-02-iaseai-selecting-the-selectors/V5-PLAN.md) records no saved run of design 2. This assessment did not run it. The negative result remains evidence about the first implementation and cannot be replaced by a later, more favorable design.

## Closest prior work and the remaining opening

| Primary source | Relevant result or proposal | Consequence for positioning |
|---|---|---|
| [Hadfield-Menell and Hadfield 2018](https://arxiv.org/abs/1804.04268) | Connects alignment to incomplete contracts and the institutions supporting their interpretation | The shared foundation in incentives and institutions is an established research direction |
| [Soares et al. 2015](https://intelligence.org/files/Corrigibility.pdf) and [Carey and Everitt 2023](https://proceedings.mlr.press/v216/carey23a.html) | Address continued correction, successors, shutdown, and human control | Preservation of correction is not a new desideratum; competition among institutions and authority allocation need additional modeling |
| [Acemoglu, Egorov and Sonin 2012](https://www.aeaweb.org/articles?id=10.1257%2Faer.102.4.1446) | Models choices that change future political decision-making power | Endogenous constitutions and blocked reforms are prior art; comparisons must be result by result |
| [Frank 1995](https://stevefrank.org/reprints-pdf/95Nature-Police.pdf) | Joint evolution of competition and mechanisms suppressing it | Cooperation and its maintenance already have explicit evolutionary models; biological policing does not determine political legitimacy |
| [Everitt et al. 2021](https://arxiv.org/abs/1908.04734) | Uses causal influence diagrams to analyze reward-function and reward-input tampering | Changing the reward process itself is already an alignment problem; evaluator succession and population replacement are the prospective extension |
| [Harré 2025](https://arxiv.org/html/2507.13616v1) | Combines institutional evolution, multilevel selection, and AI governance; specifies dynamics over institutional rules | Broad synthesis novelty is substantially occupied; no correction-preservation theorem was located in the examined sections |
| [Chai 2026](https://arxiv.org/abs/2604.13079) and [Wagner 2026](https://link.springer.com/article/10.1007/s43681-026-01362-2) | Propose institutional robustness and governance arrangements that preserve correction | These are close conceptual proposals, not demonstrated general guarantees |
| [Vallier 2026 version](https://arxiv.org/html/2512.07901v4) | Proposes strategic replicators, constitutional evolution, and stability under self-modification | Strong thematic and mathematical overlap requires a dedicated comparison; the limited audit below found reasons not to inherit its sweeping claims |

The agent reviewing Harré did not establish its proposed extended covariance formula as a general Price identity. Population weights, between-group effects, and transmission terms require a fresh derivation before reuse. The fact that a neighboring paper is ambitious does not establish either the validity of its results or redundancy of the local manuscript.

The underlying mathematics is distributed across evolutionary game theory, institutional economics, control theory, and alignment. For example, [Sato and Crutchfield](https://journals.aps.org/pre/abstract/10.1103/PhysRevE.67.015206) relate particular reinforcement-learning dynamics to replicator dynamics. Such mappings require explicit update and memory assumptions. [Harper](https://arxiv.org/abs/0911.1383) supplies an information-geometric treatment; a general multi-agent learning process need not have a common scalar potential. A cycle cannot be interpreted as steadily following a single welfare gradient.

## A precise formal target

Represent the state as \(z=(p,\theta,c,v)\): the distribution of behaviors or organizations, evaluation and institutional rules, the resources and authority available for correction, and the condition of the shared system. A family of models can take the form

\[
\dot p_i=p_i(f_i(z)-\bar f(z)),\qquad
\dot\theta=H(z,u),\qquad
\dot c=J(z,u),\qquad
\dot v=F(z,u).
\]

This is a proposed organizing representation, not a universal law. In any application, the meaning of population shares, fitness, imitation or reproduction, and causal influence must be specified. The functions cannot be chosen simply to reproduce the desired conclusion.

Let \(K\) be an explicitly justified acceptable set, and let \(U_H(z)\) describe interventions that legitimate human institutions can actually execute at that state. Formal permission is insufficient: information, budget, timing, authority, and implementation capacity belong in the feasible set.

Three separate questions follow:

1. **Current acceptability:** is the state in \(K\)?
2. **Effective correction:** can an admissible intervention keep it there, or return it to an acceptable region within the relevant deadline?
3. **Persistence of correction:** do learning, replacement, coalition formation, and institutional revision preserve that ability?

Control invariance and reachability are established mathematics, including [control-barrier methods](https://arxiv.org/abs/1609.06408). The possible new result is a nontrivial coupling to selection and changing authority, with feasible conditions that do not merely assume capture is impossible. A local no-invasion condition for correction-undermining traits is weaker than resilience to coalitions, finite shocks, and changes in the environment.

A candidate operational quantity, for each independently justified correction target \(g\), is

\[
C_g(z)=\sup_{\pi_H}\inf_{\pi_A}
\Pr_z(\text{implement }g\text{ by its deadline while remaining viable}).
\]

The human intervention policies must respect actual information and authority; the competing policies must belong to an explicitly bounded class. The set of targets with \(C_g(z)\geq1-\epsilon\) represents a portfolio of feasible corrections. A finite safety game could compute it. This is a proposed measurement construction using existing reachability methods, not a new theorem. Compare it with [attainable utility preservation](https://arxiv.org/abs/1902.09725): preserving an AI agent's options is not the same as preserving legitimate human remedies. A target can be desirable and nevertheless infeasible, and not every conceivable intervention deserves preservation.

There is also a distinction between a desirable institutional destination and a feasible transition. A sufficient correction level at equilibrium says little about whether the present institution can authorize, fund, and implement it before crossing a harm threshold. This is directly relevant to the corpus's [situational research objective](../19-v5-handoff-2026-10-03/v5_0_handoff/03_recursive_selection_future_research_review.md): evaluate actual alternatives to the present AI trajectory, rather than claim all possible bounded competition must fail.

## An illustrative extension with endogenous authority

The mathematical agent derived the following extension, checked algebraically by the coordinating agent. It is a conditional calculation, not a novelty claim or an empirical law.

Take the quadratic-cost, zero-cost-floor, zero-background-conversion special case of the current manuscript, with fixed carrier size and profile. Write

\[
q^*(\ell)=\frac{C}{D\ell},\qquad
d_{\rm eff}=D\ell,\qquad
G=\frac{Kq}{D\ell},\qquad C,K,D>0.
\]

Here \(D\) is nominal correction capacity, \(\ell\in(0,1]\) is independent enforceable authority, \(q\) is influence capacity, \(C\) combines the return and cost parameters, and \(K\) converts influence into the evaluation-domain gain. The existing selected-capacity threshold is \(d_0=\sqrt{KC}\): with authority held fixed and \(q=q^*\), the row-gain certificate \(G<1\) requires \(d_{\rm eff}>d_0\).

Now let authority recover and be eroded by influence:

\[
\dot\ell=\rho(1-\ell)-\kappa q\ell,
\qquad \rho>0,\quad\kappa\geq0.
\]

Under instantaneous tracking \(q=q^*\),

\[
\ell^*=1-\frac{\kappa C}{\rho D},\qquad
d_{\rm eff}^*=D-\frac{\kappa C}{\rho}.
\]

Thus the long-run certificate requires

\[
\boxed{D>d_0+\frac{\kappa C}{\rho}.}
\]

Nominal capacity can exceed the threshold computed with fixed authority and still become ineffective. For example, \(d_0=1\), \(D=1.3\), and \(\kappa C/\rho=0.4\) give long-run effective capacity \(0.9\). This is an analytic illustration, not a simulation or estimate.

The same reserve condition gives an invariant region without assuming instantaneous tracking. Choose

\[
\frac{d_0}{D}<\ell_{\min}\leq1-\frac{\kappa C}{\rho D},
\qquad q_{\max}=\frac{C}{D\ell_{\min}}.
\]

Assume nonnegative, sufficiently regular influence dynamics that do not increase \(q\) whenever \(q\geq q^*(\ell)\). Starting inside \(\ell\in[\ell_{\min},1]\), \(q\in[0,q_{\max}]\), the system remains there. At the lower authority boundary,

\[
\dot\ell\geq\rho(1-\ell_{\min})-\frac{\kappa C}{D}\geq0.
\]

At the upper influence boundary, \(q^*(\ell)\leq q_{\max}\), so influence cannot increase outward. At \(\ell=1\), authority cannot increase outward. Nonnegativity protects the remaining boundary. Throughout this region,

\[
G\leq\frac{KC}{D^2\ell_{\min}^2}<1.
\]

Such a region exists exactly when the boxed reserve condition holds. This establishes a sufficient certificate for this model and these initial stocks. Failure of this condition is not a general proof that every trajectory is captured. The gain certificate is also not a guarantee against transient harm already in progress.

The main unresolved assumption is \(\rho\): authority rebuilding is still supplied at a fixed rate. A substantive next model must explain its financing, legitimacy, and selection stability. The functional form of authority erosion, fixed parameters, and adaptation restriction also need justification. These limitations identify the next contribution rather than disappear inside the word “correction”.

## A deadline test for proposed reforms

A second derived extension quantifies why an adequate long-run correction level may arrive too late. For one domain let persistent rule support obey

\[
\dot s=\varepsilon(Bq-d_{\rm eff}s),\qquad Bq\geq0,
\]

and let the practice retain a current payoff advantage while \(as>c\). Suppose intervention begins at time \(\tau\), with observed support \(s_\tau>c/a\). Because incoming support is nonnegative,

\[
s(T)\geq s_\tau\exp\!\left(-\varepsilon\int_\tau^T d_{\rm eff}(t)\,dt\right).
\]

Reaching the neutral threshold by \(T\) therefore requires at least

\[
\int_\tau^T d_{\rm eff}(t)\,dt
\geq H_\tau:=\frac1\varepsilon\log\frac{as_\tau}{c}.
\]

If authority at intervention is \(\ell_\tau\), its rebuilding obeys \(\dot\ell\leq\rho(1-\ell)\), and effective correction is bounded above by \(D\ell\), then even granting no further capture, the correction delivered by that deadline cannot exceed

\[
D\left[\Delta-\frac{(1-\ell_\tau)(1-e^{-\rho\Delta})}{\rho}\right],
\qquad \Delta=T-\tau\geq0.
\]

If this upper bound is less than \(H_\tau\), a reform restricted to damping support cannot reverse the current advantage in time. If an independently established host model shows that continued advantage necessarily crosses a protected floor by that deadline, the reform is insufficient for avoiding that crossing. Authority rebuilding, accumulated influence, and delay now appear in a testable feasibility condition.

This is a limited impossibility certificate. It does not rule out interventions that directly remove support, change the payoff threshold, suspend the damaging activity, or repair the host. The permitted intervention class and the host deadline must be justified separately. Those alternative actions identify which additional authority could change the outcome.

## A discriminating experiment

Operationalize the benchmark already proposed in the local plan. Begin with a small, inspectable stochastic game. Agents allocate effort to productive work, presentation, and costly proposals to amend a scoring rubric. Public scores allocate resources and seats on the committee that controls later evaluation. Measure actual task usefulness independently of that public score.

Compare four conditions:

- A fixed rubric, measuring ordinary proxy optimization.
- Success-dependent evaluator succession and rubric amendment.
- Exogenous replay of rule histories from separate runs, breaking their identity-specific connection to the current agents.
- Random or rotating evaluator authority, preserving useful amendment opportunities while cutting the success-to-authority link.

Match task streams, budgets, capabilities, and amendment opportunities where the design allows. Replay is not sufficient by itself: it breaks adaptation as well as strategic control. The authority-randomization condition and logged interventions help separate those channels. Include genuine reasons to revise the rubric, such as a change in task distribution, so legitimate adaptation can succeed.

For each amendment, rescore the same frozen submissions under old and new rules. This measures who benefits from the change without conflating it with improved work. Combine that quantity with independent task value, resource and authority shares, challenger entry, response to valid adverse evidence, and persistence after a perturbation.

The primary hypothesis is that endogenous succession produces additional persistent, purpose-impairing advantage beyond fixed-rule gaming and matched drift. Test safeguards by cutting particular links: randomized appointments, limits on converting performance into votes, independent review, or shorter correction delays. Include the cost of slower or blocked beneficial adaptation.

Counterevidence would include no additional endogenous effect; rule changes mainly improving task value; concentration explained by unchanged competence; or proposed safeguards performing equally well despite evaluator succession. Results should narrow the theory where appropriate. A scripted reward for capture followed by successful capture would not establish the hypothesized mechanism independently.

Nearest computational precedents include [reward tampering](https://arxiv.org/abs/1908.04734), the co-adapting agents and planner of the [AI Economist](https://arxiv.org/abs/2108.02755), and agents that [learn to shape one another's incentives](https://arxiv.org/abs/2006.06051). The prospective contribution is evaluator succession, causal identification, and safeguard durability, rather than the fact that agents can alter incentives.

A matched human experiment can use paid, verifiable production tasks, disclosed differences in task efficiency, and success-based versus randomly assigned rule authority. [Dal Bó, Foster and Putterman](https://doi.org/10.1257/aer.100.5.2205) provide a relevant precedent for separating chosen from imposed institutions. Human results would validate a bounded experimental mechanism, not all markets, bureaucracies, or political systems. A subsequent field study would need institution-specific identification.

## Normative and biological boundaries

A system may remain stable, cooperative, and correctable by a ruler while denying everyone else recourse. Thus “human alignment” must not mean engineering obedience to whoever currently controls evaluation. A shared foundation requires explicit accounts of affected people's standing, authorized correction, distribution of costs, and legitimate revision. [Gabriel's analysis](https://arxiv.org/abs/2001.09768) already distinguishes alignment to instructions, preferences, interests, and values under pluralism.

Ren's emphasis on preserving future possibility can motivate this choice of constraints. It cannot by itself prove which possibilities should remain available or resolve conflicts among them. Maximizing an agent's control, preserving every existing option, and maintaining people's capacity for legitimate correction are different objectives. Cooperative institutions must face the same capture tests as their competitors.

Cancer offers bounded examples of environment-mediated selection. [Gatenby and Gawlinski](https://aacrjournals.org/cancerres/article/56/24/5745/502885/A-Reaction-Diffusion-Model-of-Cancer-Invasion) modeled acid-mediated invasion. [Estrella et al.](https://pmc.ncbi.nlm.nih.gov/articles/PMC3594450/) studied acidity and subsequent invasion longitudinally and through perturbation in mouse models. These are useful templates for identifying feedback mechanisms, not evidence for a universal cancer attractor, a clinical prescription, or a moral classification of human groups. Stable cellular proportions can coexist with increasing total tumor burden; system boundaries and state variables matter.

## Sequence of research decisions

First, compare the current manuscript's individual propositions against the nearest formal literature. Record overlaps, distinct assumptions, stronger or weaker conclusions, and missing proofs. A broad thematic match settles neither originality nor redundancy.

Second, develop the endogenous-authority extension and feasible-transition problem. Require at least one regime in which correction survives and one in which it fails, with explicit reasons. Model the corrector's own funding and appointment process rather than repeatedly installing an unexplained independent supervisor.

Third, pre-specify and implement the evaluator-succession benchmark, preserving the original failed pilot. Use its results to decide which theoretical claims merit a larger AI experiment or matched human study. The user requested exploration here; no new experiment or human study has been executed.

The ambitious question is whether AI and human institutions can improve their capabilities while retaining legitimate, effective means to discover error and change course. A contribution deserves foundational status when its definitions and results travel successfully across settings while surviving these tests.

## Limited audit of a close competing framework

Vallier's [version 4, section 10.1](https://arxiv.org/html/2512.07901v4) claims strict nonlinear Lyapunov behavior from a semidefinite condition on a linearization. That inference is invalid in general: locally, \(\dot y=y^3\), \(V=y^2\), and \(J(0)=0\) satisfy the semidefinite linearized condition while \(\dot V=2y^4>0\). Additional restrictions could change the result and would have to be stated. This is a targeted concern about the written argument, not an audit of the entire paper or its claimed machine formalization. Its substantial thematic overlap remains relevant to novelty regardless. The research program should not rely on its sweeping impossibility claim without further verification.
