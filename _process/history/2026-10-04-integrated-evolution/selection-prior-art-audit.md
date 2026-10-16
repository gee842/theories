# Selection over renewal practices: bridge, prior art, and falsifiers

5 October 2026, Asia/Bangkok. AI-generated research memorandum for the next cycle of Ren's integrated theory. This memo audits the proposed connection between maintained conditions and selection over the practices maintaining them. It is a targeted review, not a complete novelty search. No new experiment was run, and no pending mathematical model is certified here.

## The bridge that should be modeled

The most useful next step is **invasion analysis in an explicitly maintained resident environment**, followed by a separate analysis of establishment, institutional replacement, and continued viability. A policy can maintain a functioning system when imposed, lose to a rare alternative, and remain institutionally difficult to replace—or the converse. Calling all these properties “stability” obscures the mechanism.

| Property | Precise question | What it does not establish |
|---|---|---|
| Viability under a policy | Does the specified trajectory retain the protected functions over the required horizon? | Resistance to competing policies |
| Ecological attraction | Do nearby states return under the same policy? | Selection of that policy |
| Rare-invasion resistance | Do sufficiently rare alternatives fail to increase in the resident environment? | Resistance to coalitions, large mutations, or finite shocks |
| Evolutionary convergence | Do the specified mutation/adoption dynamics approach this policy? | That the destination resists invasion or meets protected constraints |
| Reachable replacement | Can available actors establish the alternative, with current authority and reserves, before failure? | Long-term retention after establishment |

Do not infer an evolutionarily stable strategy merely from ecological local stability or a vanishing selection gradient. With neutral invasion fitness, higher-order frequency effects matter. Positive rare-invasion fitness establishes initial increase under stated conditions, not eventual fixation: coexistence and environmental reversal remain possible.

Let resident renewal policy be \(u\), its stable maintained environment \(Z_u^*=(E_u^*,C_u^*,S_u^*)\), and a rare variant use \(v\). Specify its demographic or allocation mechanism before defining fitness. In a variable population with the resident at equilibrium,

\[
f(v;u)=r(v;Z_u^*)
\]

is the rare variant's growth exponent when its effect on the shared environment vanishes at rarity. In a fixed-size replacement model, use the corresponding relative payoff or linearized invasion exponent instead. A local selection gradient is

\[
g(u)=\left.\partial_v f(v;u)\right|_{v=u}.
\]

The environment is the resident environment for this derivative. Differentiating the resident equilibrium as though a rare mutant immediately changed the whole population to its policy overcounts public benefits. Private or locally inherited environmental effects must be retained if they remain non-negligible at rarity. For cyclic or stochastic resident dynamics, replace the equilibrium formula with the appropriate long-run invasion exponent; a fictitious equilibrium is not a valid shortcut.

## Strongest formal precedents and their implications

**Environmental feedback and evolutionary extinction.** [Tilman, Plotkin, and Akçay 2020](https://www.nature.com/articles/s41467-020-14531-6) derive strategy–environment dynamics whose regimes depend on incentives and relative timescales. [Gyllenberg and Parvinen 2001](https://www.sciencedirect.com/science/article/pii/S0092824001902538) analyze evolutionary suicide: adaptation can lead a previously viable population to extinction under specified model and bifurcation conditions. This directly occupies the general claim that individually favored change can undermine persistence. Their necessary conditions should not be generalized beyond the analyzed class; our prospective contribution must specify additional maintained correction, observability, or authority mechanisms.

**Selection of the incentives themselves.** [Akçay and Roughgarden 2011](https://pmc.ncbi.nlm.nih.gov/articles/PMC3107625/) provide the closest constructive bridge. A fast behavioral layer responds to payoff changes, while a slower genetic layer selects the traits changing those payoffs. Incentive-providing variants can invade under particular cost and response conditions; complete alignment is not guaranteed. The prospective model should therefore include the chain

\[
\text{rule change}\rightarrow\text{behavioral response}
\rightarrow\text{private return}\rightarrow\text{transmission}.
\]

Simply rewarding a rule for collective goodness would assume the outcome. Conversely, assuming partners never respond would rule out a known route to selected cooperation. A useful new result could identify how response latency or loss of shared support interrupts this chain before a beneficial rule can establish.

**Selection can destroy its enabling structure.** [Akçay 2018](https://www.nature.com/articles/s41467-018-05130-7) models social connections that are inherited or made randomly. Conditions supporting cooperation can select network changes that undermine it; connection costs can prevent this feedback, while reducing benefits. This is a particularly close precedent for “a safeguard works initially but successful behavior erodes the conditions sustaining it.” It also prevents treating assortment as a free, permanently fixed rescue parameter. [Stewart and Plotkin 2014](https://arxiv.org/abs/1402.6628) similarly show that coevolving payoffs can reverse conclusions from a fixed game.

**Rules change who can change rules.** [Acemoglu, Egorov, and Sonin 2012](https://www.aeaweb.org/articles?id=10.1257%2Faer.102.4.1446) explicitly model current choices changing future political power. Under their assumptions, an efficiency-improving transition can be blocked because of further transitions it enables. Therefore physical reachability and payoff desirability do not imply institutional reachability. This is the relevant precedent for representing authority and the feasible transition relation as states, rather than granting an external planner every safe action.

## Appropriation and multilevel structure

For illustration only, suppose per-carrier fitness has the form

\[
r_i=b(E)+\chi h(u_i,E)-c(u_i)-D(N),
\]

where \(\chi\) is the retained private fraction of an identified benefit. At a resident equilibrium and under well-mixed rarity, the direct gradient is

\[
g(u)=\chi\,\partial_u h(u,E_u^*)-c'(u).
\]

The common environmental benefit cancels from the immediate comparison. If \(\chi=0\) and \(c'>0\), reducing renewal is favored in this restricted construction. This is a standard public-good mechanism, not a universal result about maintenance. Excludable benefits, association with descendants, local effects, conditional reciprocity, foresight, or institutional rewards can change the invasion calculation. Each needs a causal mechanism and costs; none should be inserted as an unexplained “alignment” coefficient.

[Cooney, Levin, Mori, and Plotkin 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC10193939/) supplies an explicit multilevel route: nested birth–death events become dynamics within and among groups. A corresponding schematic density equation is

\[
\partial_t p(z,t)=-\nabla_z\cdot[F(z)p(z,t)]
+\lambda\,[G(z)-\bar G]p(z,t),
\]

where \(z\) must include relevant internal composition and support stocks, \(F\) is within-group change, and \(G\) describes actual group reproduction or replacement. A group merely producing more output does not undergo group selection unless output changes its representation through an identified process. For smooth \(h\), suitable boundaries, and no omitted events,

\[
\frac{d\mathbb E[h]}{dt}=\mathbb E[\nabla h\cdot F]
+\lambda\operatorname{Cov}(h,G).
\]

This separates within-group erosion from among-group representation. It does not imply group selection maximizes social welfare. Migratory mixing, group splitting, and transmission errors require additional terms. Deleting the support coordinates to retain only a group's cooperative share can destroy dynamical closure.

Human adoption need not imitate biological reproduction. [Tilman et al. 2023](https://arxiv.org/abs/2108.00047) shows one explicit alternative: costly forecasting can be selected in a changing environment and alter its oscillations. This is a counterexample to models treating all adaptation as permanently myopic. Keep the behavioral update mechanism open to evidence.

## A discriminating experiment

Use a resource-and-repair environment with independently measured support \(E\), maintenance capacity \(C\), and carrier payoffs. Start with scripted artificial agents so that costs, inherited rules, and true task quality can be separately manipulated; only then consider a matched human study. Do not describe a simulation of stipulated payoffs as empirical validation of real institutions.

**Stage A: certify ecological behavior.** Impose a fixed renewal policy and estimate its recovery region from several initial \((E,C)\). This identifies whether the policy is physically viable before testing whether it spreads. Use separate data to estimate costs and private versus public returns.

**Stage B: challenge with variants.** Introduce quality-matched variants that reduce renewal or alter who receives its benefits. Factorially vary private retention of maintenance benefits and association among carriers while keeping aggregate production technology fixed. Measure early log-relative growth, actual maintenance flows, absolute abundance, and support trajectories. Introduce variants both rarely and as finite coalitions. A measured positive invasion exponent followed by coexistence should be recorded as successful invasion, not fixation.

**Stage C: allow rule succession.** Compare fixed authority, inherited authority tied to success, and random or rotating authority; include exogenous replay of comparable amendments. Include beneficial amendments. In a response-disabled control, agents cannot change behavior after an amendment; this tests whether apparent returns came through behavioral uptake or merely changed scores. Vary amendment-to-response latency independently of initial support buffers. Assess remedies with an independent metric not controlled by the successful lineage.

Three preregistered contrasts can discriminate mechanisms:

1. **Appropriation mechanism:** changing retained marginal benefits changes invasion signs in the predicted direction at matched support. A sign change without a changed private return points to an omitted channel; no predicted sign change rejects the specified payoff mechanism.
2. **Uptake mechanism:** a rule's selective advantage disappears when the induced behavioral response is blocked, but persists when only irrelevant reporting changes are blocked. If amendment advantage remains without response or real benefit, score manipulation or privileged allocation is a better explanation.
3. **Replacement-window mechanism:** independently estimated invasion/response rates and depletion bounds predict whether a beneficial alternative establishes before protected support fails. A larger reserve or shorter response delay should rescue the specified blocked transition without changing its long-run invasion sign. Failure of these interventions rejects the timing model or its asserted bottleneck.

Predict both successes and failures on withheld combinations. Test alternatives including baseline quality differences, ordinary congestion, drift, fixed external deterioration, and direct resource transfers masquerading as incentive effects. If cooperative practice does not erode despite a measured negative gradient, examine migration, recurrent entry, behavioral switching, or misspecified transmission before treating the theory as confirmed.

## Existing evidence and scope of the prospective contribution

The [earlier rubric pilot](../../../drafts/2026-10-02-iaseai-selecting-the-selectors/experiment/PREDICTIONS-2.md) was inspected again. P1 failed across 20 seeds: mean capacity did not fall in REPLAY or FAST, although P2–P4 held. Its design-2 document proposes changes after the failure; this memo did not run them. New simulated results cannot overwrite that negative record.

There is empirical precedent for changing payoff structures, beyond theory: [Venkataraman et al., online 2024 / issue 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC11696675/) reports resource-dependent changes in yeast interactions, including altered benefit retention and hybrid formation. This supports measuring evolving interaction mechanisms, not claiming that our institutional model has been validated. The paper's broad claim that evolutionary game theory requires rational agents is not a premise we adopt.

The most promising result is therefore narrower than discovering selection over rules: **a mechanistic relation connecting invasion advantage, the time needed for behavioral or institutional uptake, and the remaining viable transition window when repair capacity itself must be maintained**. The source of the advantage, its transmission, the affected support functions, and the authority to enact replacement must all be specified. A theorem proving only that an assigned favorable payoff increases a trait would add little.
