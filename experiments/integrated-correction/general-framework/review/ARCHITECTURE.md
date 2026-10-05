# A general architecture for situated selection and regeneration

5 October 2026. Internal conceptual and formal synthesis. This memo restores the scope of the wider research programme after a deliberately narrow sequence of financial examples. It proposes a common modeling architecture and discriminating hypotheses; it does not present a universal empirical law or certify the programme's novelty.

## The general object

The programme concerns **how ways of acting and relating persist, spread and alter the conditions under which later ways of acting and relating become possible**. Finance is one implementation of that process. Promotion, appointment, attention, imitation, authorization, inheritance, learning, deployment, survival and reproduction can provide other forms of continuation or amplification.

The organizing question is not whether everything maximizes money, or even whether everything optimizes something. It is whether the processes that retain and amplify forms of activity also maintain or transform their own material, relational, cognitive and institutional conditions. Those transformations can support correction, cooperation and diversity; they can also suppress alternatives, undermine renewal or entrench a narrow way of succeeding. Which occurs is a question for a specified model and evidence.

This is continuous with the corpus's [meta-attractor account](../../../../theories/meta-attractor/README.md), [selection-on-cognition account](../../../../theories/alignment-selection-on-cognition/README.md), [central claim](../../CENTRAL-CLAIM.md) and [multilevel architecture](../../systems-dynamics/review/MULTILEVEL.md). The recent money-and-fee model is a controlled example of one loop inside that architecture. It is not the definition of the architecture or the only available mechanism of institutional continuation.

The earlier formal layer often represented selection by a scalar proxy σ. The broader architecture should permit a **selection-condition state** rather than require such a score. An evaluation procedure, a coalition-dependent appointment rule and an organism's density-dependent reproduction law can all affect continuation without sharing one scalar objective or one optimizing decision-maker.

## State and mechanism: what the common grammar contains

Use a relational state

`S_t = (X_t, N_t, {n_t^ℓ}_ℓ, C_t, Φ_t, ≽_t)`.

The components have distinct roles:

- **X:** physical, ecological, bodily and functional conditions. Examples include energy, nutrients, equipment, skills, maintained records and available time. Their meaningful units remain distinct.
- **N:** typed relations among carriers and environments. Dependence, testimony, trust, authority, exchange, teaching, predation and reproduction are different edge types, even when one graph represents them together. The node and edge sets can change.
- **n^ℓ:** a distribution or measure of carriers and practices of a specified type ℓ. A type might be occupied managerial roles, instances of an organizational routine, deployed AI systems, or biological lineages. Do not add cells, offices and software deployments into one unexplained count.
- **C:** current conditions of continuation and amplification. In institutions, these may include evaluation, appointment, permission, inheritance and amendment arrangements. In ecology, they include the mechanisms and environmental conditions affecting survival and reproduction. Some are represented rules; many are not.
- **Φ:** observation channels, distinctions, frames, causal models and conceivable responses where a system actually has such capacities. A change in belief within a frame differs from discovering a new distinction or response. This component is optional for systems without the relevant representational organization.
- **≽:** situated evaluative relations where agents have concerns, commitments or goals. They may be plural, incomplete, contested and changing. They need not be represented by a shared utility function. A biological population need not possess an evaluative relation merely because reproduction differs among its members.

Practices include more than individually chosen actions. A hiring routine, a method of justification, a learned response, a growth pattern or a way of transmitting skills can persist through different carriers. A practice should nevertheless be identified in independently observable terms. Calling every successful event an instance of the same practice after seeing the outcome would make the account circular.

One possible event-level factorization is

```
observations      o_t             ~ O(· | S_t, a_t)
actions/activity  a_t             ~ B(· | S_t, available history)
world/relations   (X,N)_{t+1}     ~ P(· | S_t, a_t, o_t)
practice carriers {n^ℓ}_{t+1}    ~ T(· | S_t, a_t, o_t, consequences)
conditions/frames/concerns
                  (C,Φ,≽)_{t+1} ~ H(· | S_t, a_t, o_t, consequences,
                                        retained carriers, admitted challenges)
```

This is a schema for specifying mechanisms, not an assertion that every application has this temporal order. A concrete model can use continuous dynamics, simultaneous equations, asynchronous events or delay terms. If the current state omits relevant history, a Markov update is only an approximation and must be justified.

The activity law B need not take the form `argmax utility`. It can represent habit, deliberation, bargaining, aspiration, imitation, reflex, chemical reaction or a measured stochastic response. Differences in behavior can arise from what is observable and imaginable, not only from incentives over a fixed menu.

## Differential continuation without a universal fitness or utility

For each declared carrier type, a useful general representation of the expected continuation process is

`E[n^ℓ_{t+1}(A) | S_t] = ∫ M^ℓ_t(A | p,S_t) n^ℓ_t(dp) + I^ℓ_t(A)`.

Here p is a practice or carrier description, A is a set of successor descriptions, M is a nonnegative continuation/transmission kernel, and I records entry from outside the tracked population. M may include survival, duplication, appointment, reassignment, learning and transformation. The actual population can be stochastic around this conditional expectation.

When meaningful, write `M(A|p,S)=w(p,S)Q(A|p,S)`, where w is expected retained or successor mass and Q describes its type distribution. The number w is an **outcome rate in specified units**. It is not automatically a utility, represented goal, moral value or quantity any participant maximizes. Different types can have different rates, horizons and channels. Attention shares, reproduction counts and authority rights should remain distinct unless an explicit conversion mechanism relates them.

This equation alone predicts very little: any positive continuation operator can be written in such a form. Explanatory content comes from restrictions on M, independently specified mechanisms, observable bridge variables and consequences that could have turned out otherwise. Random drift, neutral coexistence, changing niches and feedback that reverses an advantage are all allowed. Continuation does not imply progress; differential continuation does not imply a monotonic increase in any global score.

The distinctive recursive link is that M depends on S, while retained practices change S. In institutional cases this can include control over evaluation, appointment and representation. In ecological cases, organisms can change habitats and resource cycles that alter later reproduction. The latter does not require an evaluator, a rewritten rulebook or an intention to control evolution.

## Lifecycle, succession and environmental openness

Continuing a process is different from keeping every present carrier alive. A functional practice can disappear while an organization retains its name, or persist through complete replacement of its members. The transmission kernel must therefore specify what a successor actually acquires: a skill, record, dependency, permission, obligation, material resource or developmental organization. Filling an office does not by itself transfer its competence. Copying an artifact does not necessarily preserve the circumstances that made its behavior useful.

For an institutional succession claim, trace both the transfer of effective decision rights and the reproduction of the means to exercise and contest them. For a biological claim, specify the scale and mode of development, inheritance and replacement. A persistent population count is insufficient evidence that the relevant function has been transmitted. Tests should include loss and replacement of carriers, rather than only small perturbations around indefinitely surviving incumbents.

The modeled system is open. Energy, materials, people, signals, disturbances and constraints can enter from the surrounding environment. These influences can determine an outcome more strongly than the internal selection loop. The framework is not an attempt to explain every change as selection: transport, physical reaction, random disturbance, development and an imposed institutional decision can require their own causal accounts. Selection becomes an explanation only where a specified difference in continuation or amplification actually does causal work.

A finite model also has a boundary of expressibility. It can let agents discover distinctions the analyst has represented, change their relations among existing concerns, or enlarge a vocabulary within a declared construction process. It does not thereby enumerate every future novelty or contain the real world in advance. Endogenous frames and an open environment make model revision part of the research programme; they do not exempt its present, bounded claims from being tested.

## Regeneration and constraints without reducing everything to money

For a measurable stock k, accounting can take the form

`X^k_{t+1} − X^k_t = inflow^k + regeneration^k − use^k − loss^k`.

Examples include trained hours produced and lost, equipment repaired and worn, nutrients replenished and consumed, or records created and destroyed. The processes producing these terms must be specified. A higher-level organization does not acquire additional time, energy or information merely because the same resource is counted again at another level.

Money is one routing and accounting device for some of these processes. It is not their general substrate. A bureaucracy may retain review capacity through protected appointments and work allocation. A community may reproduce a practice through teaching and recognition. An organism maintains a regulatory system through metabolism. The relevant question is whether the necessary processes and access relations continue, not whether every case has a fee.

Not every relevant property is an additive stock. Trust, legitimacy, meaning and a decision right can require relational or logical conditions rather than a conservation equation. Their continuation should still have a mechanism, but forcing them into a scalar resource inventory would discard the distinction the framework is meant to preserve.

Likewise, plural concerns need not be collapsed into one target. Participants may evaluate consequence vectors using different partial relations, nontradeable constraints or procedures for negotiating disagreements. A family of viability conditions can express a declared commitment, but an empty intersection is a real conflict, not an invitation to conceal the conflict in weights. The commitments and their revision procedure remain normative choices; survival and popularity do not establish legitimacy.

Alignment can be formulated as a normative relation between an implemented process, the situated commitments it is meant to answer to, and the people or conditions affected by it. Its content requires an account of standing, disagreement and legitimate revision. It is not another name for persistence: a destructive or coercive arrangement can be dynamically stable. Nor does changing the declared standard establish improvement in the world. If both state x and an evaluative standard ψ change, movement of a satisfaction boundary `b(x,ψ)` contains both `∇_x b·xdot` and `∇_ψ b·ψdot`; these contributions should be recorded separately. Lowering a standard must not be reported as material regeneration or improved consequences.

## Meta-attractors are a particular regime, not the entire model class

The general architecture permits several forms of feedback. A meta-attractor hypothesis concerns a more restricted loop:

`retained practices → selection conditions/frames → differential continuation → retained practices`.

Its empirically interesting version requires more than observing persistence. One must show that a practice's continuation causally changes future selection conditions in a way that helps reproduce that practice or its influence. If the claim additionally concerns destructive entrenchment, it must also identify the capacities or alternative forms whose effective continuation is reduced.

The enlarged dynamics can have attracting sets, cycles, metastable regimes, several basins, dispersal or collapse. Positive feedback on one path does not prove an attractor, an ever-deepening basin or inevitable dominance. Under a changing external environment, a finite-time persistent regime may be the appropriate object instead of an autonomous asymptotic attractor. A mathematical attractor claim needs a specified dynamics, state space and stability notion.

This preserves the core insight while avoiding an old overextension: not every ecosystem, democracy, learning process or living system is a destructive meta-attractor. They are candidate domains for the common architecture. Whether a reinforcing selection loop exists, whether it dominates competing loops, and whether its effects are harmful are separate questions.

“Correction” is similarly relational. It concerns an observable discrepancy and an available response relative to some declared concern, function or commitment. An ecology can exhibit stabilizing regulation without anyone judging a deviation wrong. A political institution can consciously dispute both the diagnosis and the desired response. Treating these as literally identical would erase their most relevant differences.

## Concrete cross-domain mappings

The following are modeling translations, not claims that the listed mechanisms dominate every instance.

| Domain | Carriers or practices | Continuation/amplification channel | Feedback into later conditions | Conditions requiring regeneration |
|---|---|---|---|---|
| Merit-based selection and professional review | Candidates, evaluative routines, styles of work | Promotion, appointment, recommendation, access to consequential assignments | Appointees influence rubrics, evidence standards, training and future appointments | Reviewer time, domain skill, records, independence of challenge, replacement of evaluators |
| Bureaucracy | Offices, procedures, reporting routines | Authorization, staffing, precedent, compliance and routine adoption | Retained offices alter categories, reporting requirements and discretionary permissions | Administrative competence, usable records, operational capacity and avenues of appeal |
| Democracy and politics | Coalitions, parties, officeholders, organizing practices | Votes, membership, appointment, agenda access and public attention | Elected or influential actors affect electoral rules, participation channels, public narratives and succession | Participation, organizing capacity, trustworthy information, contestability and legitimate transfer of authority |
| Cultural practice or community coordination | Norms, skills, stories and ways of resolving disputes | Teaching, imitation, recognition, participation and succession | Practices form what participants notice, expect and can transmit next | Time together, practical skill, memory, relationships and access for newcomers |
| AI development and deployment | Learned behaviors, models, evaluation procedures and organizations | Parameter updates, model selection, deployment, copying and successor construction | Deployed systems alter data, tasks, evaluators, institutions and later training/deployment choices | Evaluation competence, informative data, compute, implementation authority and effective challenge |
| Ecology | Organisms, lineages, traits and interaction patterns | Survival, reproduction, dispersal and establishment | Organisms alter resources, habitats, symbioses and encounter networks that affect subsequent continuation | Energy flow, nutrient cycles, habitat structure and relevant reproductive conditions |
| Living regulation at a declared biological scale | Cells, regulatory processes or functional organizations | Persistence, replacement, development and replication at the relevant scale | Activity changes internal and external conditions affecting later activity and continuation | Metabolic inputs, repair, boundary maintenance and reproduction of functional organization |

Politics and ecology share feedback and continuation structures while differing in agency, institutions and normativity. Votes are not births; promotion is not genetic inheritance; a gradient update is not an election. A valid comparison supplies the bridge mapping and retains the differences that determine the prediction.

## A nonfinancial illustration with an explicit feedback test

Consider an organization with a fixed number of senior appointments. Let a be the fraction occupied by carriers of practice A, and let s be a feature of the review process that gives A more appointment advantage when it increases. No money or monetary return is required.

A deliberately small candidate model is

`a_{t+1} = logistic(logit(a_t) + β(2s_t−1))`,

`s_{t+1} = (1−ρ)s_t + ρa_t`, with β>0, 0<ρ≤1 and 0<a,s<1.

The first equation specifies promotion or succession odds. The second says that incumbents' practices affect future evaluation. Neither equation is a definition of merit, and neither establishes that A is harmful. Those must be assessed separately. The point is that the same recursive architecture exists with appointments and rule influence as its channels, entirely without a fee mechanism.

At the symmetric state a=s=1/2, the linearized update is

`[[1, β/2], [ρ, 1−ρ]]`.

Its characteristic polynomial evaluated at eigenvalue 1 is `−βρ/2<0`; because the polynomial tends to positive infinity for large positive eigenvalue, there is an eigenvalue above one. The coupled symmetric state is unstable in this specified model. This is an elementary illustration, not an empirical finding or new stability theorem.

The test is to estimate both links independently. Appointment advantage at fixed evaluation rules does not establish incumbent control over later rules. Change who can amend the rubric while holding the current rubric and appointment resources fixed. If the resulting propagation matches a model with the second link absent just as well, the proposed selection-on-selection mechanism has not earned explanatory weight. If frames rather than deliberate favoritism mediate the second link, measure what appointees treat as admissible evidence, not only whom they reward.

This also exposes a necessary contrast. Keeping selection rules fixed can leave strong first-order selection intact. The hypothesis concerns their endogenous reinforcement, not the claim that all selection disappears when one feedback link is blocked.

## What is testable, and what is only expressivity

Four claim levels should remain separate:

1. **Representation:** a domain can be encoded in this grammar. This establishes a language for comparison, not predictive success.
2. **Mechanism:** identified practices causally alter identified continuation conditions, capacities or frames. These links can be tested in a particular domain.
3. **Conditional dynamics:** specified mechanisms imply persistence, reversibility, depletion, multistability or a particular response to intervention. This requires proofs or appropriate numerical evidence for the stated model.
4. **Transfer:** a mechanism-level relationship predicts an independently measured response in another domain after a justified bridge mapping. This is the strongest substantive generality claim and needs evidence beyond relabeling the variables.

Promising tests include:

| Conditional hypothesis | Discriminating intervention or comparison | What would weaken the claim |
|---|---|---|
| Success entrenches a practice through later control of its evaluation conditions | Change amendment or appointment rights while holding initial selection criteria and operational resources fixed | Fixed-rule models predict persistence and reform outcomes equally well; the alleged feedback link has no independent effect |
| A visible improvement can conceal erosion of future response capacity | Match current measured output, then compare replenishment of domain-relevant evidence, skill, replacement or implementation capacity | Added regeneration variables do not predict recovery or response to a held-out disturbance beyond simpler stock/output models |
| Selected frames shape which corrective information can matter | Change admission of a specified diagnostic distinction while separately measuring access to action and evaluator succession | Behavior changes are fully explained by resources, ordinary beliefs or coercion, with no added role for representation or admission |
| More informative signals cannot improve realized response when the relevant implementation route is blocked | Independently vary information quality and effective decision or execution access | The predicted interaction is absent, or the allegedly blocked route was not actually needed |
| Local adaptation can undermine a shared continuation condition | Manipulate a specified local retention advantage while measuring its downstream effect on renewal and later retention | Renewal does not respond as predicted, compensating mechanisms dominate, or the proposed local advantage does not govern actual continuation |

These are proposed research designs, not confirmed cross-domain regularities. Each requires a defined horizon, units, competing explanations and an observable intervention. Historical or ecological cases may require quasi-experimental or mechanistic evidence rather than direct intervention. The architecture should make those requirements clearer, not exempt itself because the world is situated.

## What the recent financial construction contributes

The funded-governance construction fixes a particular carrier population, task, receipt mechanism, material conversion law and imitation rule. It shows that one institution can reproduce specified feedback capacities from actual operating output while coping with a declared set of noncontributing practices and minority reporting attacks. It also separates maintained machinery from truthful use: lying maintainers can have the same monetary return as truthful maintainers.

That is one rigorous witness for a general research question. The transferable issue is the relationship among **continuation, influence over continuation, access to informative response, and regeneration of their enabling conditions**. The fee, scalar output, binary task and financial imitation law are specialization choices. Other domains require their own mechanisms and units, rather than an assumption that everything secretly behaves like a market.

The framework can therefore encompass meritocracy, bureaucracy, democracy, politics, ecosystems, AI and living organization in principle. The scientific ambition is to discover which coupled mechanisms recur and which distinctions explain their different trajectories. It does not require all systems to have one goal, all life to optimize, or every phenomenon to instantiate the same attractor. A useful general theory should tell us when its narrower mechanisms apply, when they do not, and what observations could change that judgment.
