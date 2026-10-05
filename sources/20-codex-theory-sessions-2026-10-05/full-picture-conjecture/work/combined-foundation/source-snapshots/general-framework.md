# A general framework for alignment and the reproduction of its conditions

5 October 2026. AI-assisted working synthesis responding to Ren's correction that the programme had narrowed too far into financial mechanisms. This is a research proposal within `experiments/`, not a replacement for the canonical theories or an empirical validation of their broad claims. The formulations below are assistant elaborations, not quotations attributed to Ren.

## The scope correction

The common object is **the coupled development of participants and practices, their relations and environment, and the conditions governing what can continue, change, and emerge**. Funding is one means of maintaining some of those conditions in some institutions. It is not the substrate of the general theory.

The previous studies established conditional results about fee collection, maintenance, reporting, and executable rule revision. Their explicit mechanisms made the propositions checkable, but they also narrowed the ontology: money became the main means of continuation, selection became payoff-based copying, and correction became a maintained service. Those are specializations. They cannot define life, ecosystems, politics, or human purposes in general.

The broader claim is:

> Participants and practices change the conditions of their own and others' continuation. Those changed conditions shape future participants, practices, relations, and—in systems that have them—interpretations and purposes. Alignment research should study which resulting regimes preserve or undermine declared conditions of coexistence, renewal, and effective revision across levels and generations.

This contains a descriptive architecture and a normative research question. It does not derive what ought to persist from what does persist. A durable coercive institution can be misaligned with affected people; a growing tumour can undermine the organism that supports it. Persistence alone does not establish alignment.

## A common architecture, with different mechanisms

Use an augmented state

\[
z=(x,e,n,r,\phi).
\]

- \(x\): the relevant participants, populations, practices, and their operational states;
- \(e\): material and ecological conditions, including regeneration and external inputs;
- \(n\): relations, boundaries, access, and interaction structure;
- \(r\): implemented mechanisms governing continuation, transformation, and interaction;
- \(\phi\): representations, memory, and plural evaluative relations, where the system possesses them.

In a smooth finite-dimensional specialization:

\[
\begin{aligned}
\dot x&=f(x,e,n,r,\phi;\xi),\\
\dot e&=g(x,e,n,r,\phi;\xi),\\
\dot n&=h(x,e,n,r,\phi;\xi),\\
\dot r&=k(x,e,n,r,\phi;\xi),\\
\dot\phi&=\ell(x,e,n,r,\phi;\xi).
\end{aligned}
\]

Here \(\xi\) denotes specified external influences. Stochastic, discrete, hybrid, spatial, and population-changing models can replace these equations. If the selected state omits causally relevant memory, a history-dependent model or a larger state is required. No equation is required to be an optimization step. No shared reward, scalar welfare function, potential landscape, or uniform learning rule is assumed.

The components have different meanings in different applications. In an institution, part of \(r\) might be an appointment procedure. In an organism, it might be an implemented regulatory mechanism. This does not make cellular regulation a constitution. Ecological changes to future selection can occur through \(e\) and \(n\) without any represented evaluator or goal. The equations should retain only components supported by the application, rather than inventing cognition for an ecosystem.

The distinction between game and meta-level is relational: one process changes actions within some conditions; another changes those conditions. Both belong to the same coupled system. More levels are needed only when omitted mechanisms matter. Putting a rule in the state does not imply that an institution rewrites physical law.

These symbols alone explain nothing. A scientific model must restrict the functions, specify what is observed, and derive outcomes or intervention effects that could turn out wrong.

## What is shared across the examples

The following are candidate mappings, not findings that every instance exhibits capture or the same dynamics.

| Domain | What can be retained or amplified | How subsequent conditions can change | What must be explained about continuation |
|---|---|---|---|
| Meritocracy | Candidates, credentials, assessment practices | Appointees influence standards, training, and future appointments | Whether evaluation remains informative and revisable through successive appointments |
| Bureaucracy | Routines, offices, categories, records | Procedures shape admissible evidence and who can change procedure | How competence, memory, error reporting, and effective appeal are reproduced |
| Democracy and politics | Coalitions, officeholders, public narratives, forms of participation | Office and organization alter agendas, access, institutions, and future contestation | How participation, contestability, implementation, and succession persist |
| Ecosystems | Organisms, lineages, community structures | Organisms alter habitat, resources, and interaction networks | How regeneration, diversity, and particular ecological functions change under those feedbacks |
| Living organization | Metabolic and regulatory processes; cellular organization | Processes maintain or alter boundaries, repair, and developmental conditions | How those processes are materially regenerated despite turnover and disturbance |
| AI systems and their institutions | Learned behaviours, models, evaluation methods, deployment practices | Deployment changes data and human practices; institutions change training, evaluation, and successor construction | How evidence, relevant competence, intervention, and revision survive repeated updates and succession |

Promotion, reproduction, habituation, imitation, survival, and model updates are distinct mechanisms. Differential continuation is a common question we can ask about them; a replicator equation is not automatically a valid description of all of them. Drift, accidents, external support, historical contingency, and physical constraints also require representation where they matter.

The framework can therefore include local optimization, but also habit, bargaining, aspiration, development, selection without foresight, and incomplete or conflicting goals. Human purposes can change through experience, relationships, learning, and coercion. A model should distinguish these mechanisms instead of interpreting every behavioural change as revealed preference.

## Where the meta-attractor claim belongs

Endogenous conditions allow several possibilities: coexistence, recurrent adjustment, cycles, competing basins, collapse, or persistent dominance. Positive feedback by itself establishes none of these.

The narrower hypothesis associated with a harmful meta-attractor is that a practice's continuation increases its influence over subsequent conditions, those changes reinforce its continuation, and the resulting regime reduces specified alternatives or means of effective revision. This is a hypothesis about a feedback structure and its consequences. Concentration alone does not establish it; successful coordination can also concentrate effort.

If a model uses the word *attractor* mathematically, it must identify an invariant attracting object and an appropriate basin under stated dynamics. A feedback motif or a temporary trend is not sufficient. For changing or stochastic environments, specify whether the object is a metastable regime, an invariant distribution, a random attractor, or merely an observed persistence pattern. There need not be a scalar landscape whose gradient drives everything.

The scientific bridge across domains is therefore a **restricted feedback mechanism**, not the claim that every domain has the same attractor. Different systems may share a mathematical feedback motif while differing in its sign, strength, delay, saturation, boundary conditions, and normative meaning.

## What makes the common mathematics useful

A simple established stability calculation illustrates the gain from treating levels jointly. Near a candidate regime, suppose two deviations satisfy

\[
\dot u=-\alpha u+\beta v,\qquad
\dot v=\gamma u-\delta v,
\qquad \alpha,\delta>0,\quad\beta,\gamma\geq0.
\]

Each component has a restoring response when the other is held fixed. Together they are locally asymptotically stable when \(\beta\gamma<\alpha\delta\), and unstable when \(\beta\gamma>\alpha\delta\). At equality, linearization is inconclusive about nonlinear stability. In the exact linear system equality produces a zero eigenvalue and loss of asymptotic stability.

This gives a concrete cross-domain question: **are restoring processes strong enough for the feedbacks that connect levels?** Neither current performance nor the presence of a functioning repair mechanism answers it. The coefficients must be estimated or justified for each application. This is established dynamical-systems mathematics, not a new universal law or evidence that every failure has this form. The [formal review](review/FORMAL-CORE.md) develops a more general sufficient comparison bound and a nonlinear example.

A second useful distinction concerns changing standards. If a declared condition is \(b(y,r)\geq0\), where \(y\) records independently measured conditions and \(r\) includes a revisable standard, then

\[
\dot b=\nabla_y b\cdot\dot y+\nabla_r b\cdot\dot r.
\]

Increasing measured compliance by changing \(r\) is mathematically different from improving \(y\). Revision can be justified; it can also conceal deterioration. A descriptive equation cannot decide which. Research must preserve the measurements and the reasons for revision, and specify whose requirements are represented.

## Alignment must itself have a continuation mechanism

A performance measure describes an outcome. A budget can describe an available means. Neither establishes how relevant conditions are reproduced after turnover, disturbance, changing circumstances, or intervention.

For each application, ask what physically or socially carries the following functions, where relevant:

1. Regeneration of the conditions on which participants depend.
2. Transmission or reconstruction of relevant capacities across replacement and succession.
3. Contact between consequential changes and responses that can address them.
4. Effective means of modifying harmful dynamics rather than merely reporting them.
5. Formation and revision of represented purposes and evaluative standards, in systems that possess them.

These are questions about mechanisms, not five universal substances or guaranteed desirable functions. Biological repair and institutional appeal need different accounts. They cannot be treated as the same process simply by calling both correction. Environmental support may be indispensable; no open system must be self-sufficient to qualify as persistent.

For human and AI alignment, the normative layer must additionally specify affected parties, plural commitments, permissible tradeoffs, and how contested changes gain legitimacy. Protecting current authority or achieving indefinite survival is insufficient. Effective revisability is a proposed commitment of this programme, not a value derived from a stability theorem.

## Discriminating research tests

1. **Changing the link from present success to future conditions.** Compare models or experimental regimes with matched initial state and current performance, while varying a specified channel through which retained practices alter subsequent criteria or interaction conditions. A claim about self-reinforcing closure predicts a change in persistence and effective revision in the specified regime. If a fixed-conditions model predicts equally well under these interventions, the extra recursive mechanism has not earned its place.
2. **Turnover and regeneration.** Compare systems with similar current outputs and capacities but different measured mechanisms of replacement, transmission, or regeneration. Specify the perturbation and horizon in advance. Predict which conditions will persist through turnover, instead of retrospectively labelling every surviving system well aligned.
3. **Coupling and timescale.** Estimate within-level restoring responses and cross-level responses separately, then test the resulting joint stability or transition prediction. For models with delayed or changing feedback, use the appropriate analysis; a two-dimensional equilibrium threshold cannot be transported unchanged to those systems.

The first concrete nonfinancial institutional test could study appointment and evaluation: match initial competence and performance, vary appointees' control over future criteria, and independently track competence, admission of discrepant evidence, succession, and real revisability. A separate ecological model could examine organism–habitat feedback. Its state variables, interventions, and protected functions would need their own justification. A common symbol or curve shape would not establish equivalent mechanisms.

## Scientific standing and provenance

This architecture connects to existing cybernetics, viability theory, evolutionary and ecological dynamics, institutional analysis, and learning in changing environments. In particular, environmental-feedback games already derive coexistence, bistability, and cycles from reciprocal changes in strategies and environments: [Tilman, Plotkin and Akçay (2020)](https://www.nature.com/articles/s41467-020-14531-6). The general presence of such feedback is not an originality claim.

In machine learning, [Perdomo and colleagues' performative prediction framework (2020)](https://proceedings.mlr.press/v119/perdomo20a.html) explicitly treats predictions that change the outcomes and distributions encountered later. It supplies another specific mathematical predecessor, while retaining assumptions about prediction and risk that should not be imposed on all the other domains.

The proposed contribution is a more specific integration: mechanisms of continuation and selection, changes to the conditions of later continuation, formation of cognition and purposes where applicable, and the regeneration or erosion of effective revision. Its value must be demonstrated by restricted models and discriminating tests beyond the financial example. Neither universality nor a solution to AI alignment has been established.

Local lineage and reviews:

- [Meta-attractor theory](../../../theories/meta-attractor/README.md), especially its distinction between success within a game and influence over future conditions.
- [Alignment as selection on cognition](../../../theories/alignment-selection-on-cognition/README.md), with its stated terminology and unresolved claims.
- [Existing multilevel formulation](../systems-dynamics/review/MULTILEVEL.md), including plural goals and the two-level feedback example.
- [Architecture review](review/ARCHITECTURE.md).
- [Formal core review](review/FORMAL-CORE.md).
- [Generality and prior-art review](review/GENERALITY.md).
- [The financial specialization and its extensions](../README.md). Their proved thresholds remain specific to their equations and premises.

The three reviews are AI-assisted analyses, not independent human peer review. This synthesis repairs the scope of the research programme. It does not close its remaining empirical, normative, or mathematical gaps.

## Subsequent integration and validation study

The [endogenous-continuation study](closure-study/README.md) now joins inquiry, admitted memory, implemented response, skill regeneration, changing appointment criteria, and succession in one nonfinancial finite model. It supplies an exact finite-state criterion for actual persistence and renewal, and distinguishes that property from existence of an externally preserving policy. Conditional proofs and exhaustive computations expose rare-failure paths, recurrent recovery, and a case where criterion reinforcement prolongs correction. This advances internal integration and validation; its mechanisms remain stipulated and its broad empirical and normative claims remain open.

The subsequent [gap-resolution dossier](gap-resolution/README.md) adds bounded frame formation, explicit plural feasibility and commitment revision, and a coupled finite study of discovery, training, succession and reopening learned rules. It also supplies an intervention-identification analysis, a situated normative specification, and public institutional reanalysis. The data support an immediate information effect but leave the tested one-round effect on later information investment inconclusive. The dossier preserves that limit, the earlier failed primary microbial prediction criterion, and the distinction between an explicit cross-domain transfer condition and evidence that satisfies it.

The [reproduction-test continuation](reproduction-test/README.md) now distinguishes a feedback model from a calibrated outcome-insensitive turnover rival, proves a conditional assurance for retained evidence, and demonstrates failure of the same evidence-pooling rule after environmental reversal. A second public institutional reanalysis finds a positive contrast on retained agreements but predominantly unchanged rules, leaving repeated renewal unidentified; its session treatment schedule also limits causal interpretation. A prospective successor-handoff experiment specifies how to test the missing route. These results sharpen the difference among persistence, actual renewal, and continued validity under change.

The [generative-basis study](generative-basis/README.md) pursues formal completeness directly. It proves a conditional finite generating result, an exact intervention-preserving reduction criterion, and a structural dependency-closure theorem for supplied local mechanisms. A complete ten-coordinate example shows how conditions of conditions can close through feedback, while a new authority intervention makes a previously irrelevant coordinate consequential. Exact computation and separate AI-assisted reviews check the proofs and finite witnesses. This establishes a bounded formal foundation without treating representational closure as proof of desirable persistence or claiming that supplied mechanisms explain every domain.
