# Situated cognition and the capacity to revise evaluations

Ren's clarification on 5 October 2026 changes the modeling task: the purpose is to develop an orienting account of situated systems whose goals and cognitive models arise through interaction with their environments. A model can expose consequential relations and guide intervention without representing the whole world or supplying one objective for it.

The next substantive extension is to make the production of experience, interpretation, and possible proposals part of the dynamics. The current benchmark models informed conflict over a shared, fully visible usefulness function. A broader account must also explain how sincere attempts to improve a situation can reproduce the frame that prevents a needed change from becoming recognizable.

This note develops a model architecture, elementary conditional results, and a discriminating experimental design. It reports no new trajectory experiment. The conceptual direction is Ren's; the formal synthesis is AI-generated and reviewed by three AI research agents. Existing experiments and canonical theory remain unchanged.

## General structure with situated content

A useful common structure is reciprocal formation:

\[
\text{environment and institutions}
\longrightarrow \text{experience and cognitive frames}
\longrightarrow \text{action and evaluation}
\longrightarrow \text{changed environment and institutions}.
\]

The arrows identify causal questions. They do not claim that every application has the same variables, values, dynamics, or response. Institutional formation is not deterministic programming: reflection, dissent, migration, discovery, and unanticipated events can alter the process. Their availability is itself something to investigate.

This extends the existing [selection and generative conditions draft](../../sources/15-codex-theory-conversations/2026-10-04-selection-and-generative-conditions.md), which separates what spreads from the conditions supporting further generation. It also respects [Keep the Possibility Space Open](../../theories/keep-the-possibility-space-open/README.md): openness there is responsiveness and revisability in a situation, not a count of options or a quantity to maximize. The diagnostics below are partial operational questions, not replacements for that concept.

There is established mathematics for parts of this structure. In [Berk–Nash equilibrium](https://arxiv.org/abs/1411.1152), agents fit possibly misspecified models to evidence whose distribution depends on their actions. [Games with unawareness and discovery](https://faculty.econ.ucdavis.edu/faculty/schipper/sceunaw.pdf) allow discovered actions to change an agent's representation of the game. These frameworks supply precise tools while retaining explicit limits on what their analysts represent.

## Distinguish the frame from beliefs within it

For a particular application, represent an agent's frame as

\[
\Phi_{i,t}=(O_{i,t},\mathcal M_{i,t},E_{i,t},\mathcal A_{i,t},\preceq_{i,t}).
\]

| Component | Question it records |
|---|---|
| Observation channel \(O\) | What can be encountered, recorded, or measured? |
| Model class \(\mathcal M\) | Which distinctions and causal explanations can be expressed? |
| Evidence rules \(E\) | Which observations or testimony can count as reasons? |
| Conceivable actions \(\mathcal A\) | Which responses can be proposed at all? |
| Evaluative relation \(\preceq\) | What matters, to whom, and which tradeoffs remain unresolved? |

Beliefs \(b_{i,t}\) within a model class are a separate object. Available implementation authority and resources are separate again: imagining a response does not make it feasible. The evaluative relation need not be a complete ranking or a numerical utility function.

A local model can specify how action changes the environment and institutions, and how those changes alter frames, beliefs, and evaluative commitments. For example,

\[
a_{i,t}\sim\pi_i(\Phi_{i,t},b_{i,t},h_{i,t}),\qquad
(x_{t+1},I_{t+1})\sim P(\cdot\mid x_t,I_t,a_t),
\]
\[
(\Phi_{i,t+1},b_{i,t+1})
\sim L_i(\cdot\mid\Phi_{i,t},b_{i,t},\text{available experience},I_t).
\]

Here \(x\) describes the represented environment, \(I\) institutions, and \(h\) available history. These equations are a schema, not an explanation until the channels and update mechanisms are specified. An unknown category cannot be recovered just by assigning it a variable in notation. A tractable study may represent a few possible discoveries for the analyst while the agents cannot yet represent them; that does not capture all real novelty.

The distinction permits different diagnoses. A person may recognize a harm and prefer it, care about it but misidentify its cause, understand it but lack standing, or lack the concepts needed to formulate it. Replacing people, correcting an estimate, changing incentives, admitting testimony, and changing decision rights intervene on different mechanisms.

## Accurate prediction can coexist with an inability to learn

Consider two possible environments with the same initial distribution of available histories. Suppose every institutionally available action, at every reachable history, produces the same distribution of the next represented observation in both environments. Any policy based only on those histories then induces identical observed-history distributions for every finite horizon.

The proof is induction. Conditional on the same history, the policy gives the same action probabilities. The next-observation distributions are equal by assumption. Multiplying and summing preserves equality at the next step.

Consequently, no learner using only those histories can distinguish the two environments. If a Bayesian model contains both possibilities, their posterior odds remain their prior odds. More computation or a larger quantity of the same nondiscriminating evidence cannot supply the missing information. A useful intervention must change what can be tried, observed, represented, or admitted as evidence so that the relevant distinction can appear.

This is an elementary identification result, not a claim that institutions always suppress truth. The assumptions can be false: an external shock, dissident observation, or unexpected outcome may distinguish the environments. The result tells us which channel must be examined rather than assuming better prediction automatically supplies correction.

It also suggests a testable pattern: prediction can improve on the experiences an institution repeatedly generates while judgment about excluded alternatives remains wrong. This connects with the existing self-confirmation literature. It should not be interpreted as proving that every unfamiliar alternative is useful.

## A response can exist without being available to a situated agent

Two statements must be distinguished:

\[
\forall\theta\;\exists\sigma_\theta:
\text{the response works in context }\theta,
\]
\[
\exists\sigma\text{ using available observations and authority}\;\forall\theta:
\text{the response works in context }\theta.
\]

The first permits a different response chosen by someone who knows the context. The second requires a feasible policy that can distinguish and respond to the situation. The first does not imply the second.

An exact example isolates this difference. There are two contexts, L and R, and a decision deadline. Action L satisfies the declared recovery condition only in context L; action R does so only in context R. Passive observations are identical. A reliable probe, when available, reveals the context before the deadline. Authority either allows both responses or restricts implementation to L. Assume the probe uses no other scarce resource and creates no harm.

| Available information | Implementation rights | Best worst-case recovery probability |
|---|---|---:|
| Passive observations only | L only | 0 |
| Reliable probe | L only | 0 |
| Passive observations only | L and R | 1/2 |
| Reliable probe | L and R | 1 |

With both actions but no informative probe, any randomized rule chooses L with some probability \(p\). Its two recovery probabilities are \(p\) and \(1-p\); their minimum is at most \(1/2\), attained at \(p=1/2\). With a timely signal and both rights, choosing the indicated action succeeds in either context. Restricted authority fails in R regardless of information.

The table is an analytic capacity bound, not a prediction that actual decision makers choose the best policy. Its recovery condition is deliberately local, not a social welfare function. If the probe arrives after the irreversible decision, its information is useless for this deadline. If it is noisy, dangerous, costly, or manipulable, the model must change. The example demonstrates that discoverability, authority, and timing can complement one another; none alone guarantees correction.

## Plural consequences can guide comparison without a total score

The earlier authority covariance identity extends componentwise. At a fixed state, let \(m_i^\theta\in\mathbb R^d\) describe the consequences of appointing agent \(i\) under empirical model \(\theta\). Coordinates may describe different affected groups, environmental conditions, or specified recovery events. For a full-support baseline appointment policy \(\rho\),

\[
M_\pi^\theta-M_\rho^\theta
=\sum_i(\pi_i-\rho_i)m_i^\theta
=\operatorname{Cov}_{i\sim\rho}\left(\frac{\pi_i}{\rho_i},m_i^\theta\right).
\]

No weighting of the dimensions is required. After declaring their orientation, one can ask whether every component is nonnegative under every considered empirical model. Where that holds, the intervention passes this specified comparison. Where some components improve and others deteriorate, it exposes a tradeoff instead of assigning it a hidden exchange rate.

For example, \(m_1=(1,-1)\) and \(m_2=(-1,1)\) mean that transferring authority between the two improves one concern and worsens another. The appropriate result is incomparability under componentwise comparison. Choosing the dimensions and acceptable tradeoffs remains a substantive, revisable judgment. Empirical model uncertainty must stay distinct from disagreement about values.

For the current finite-logit benchmark, a particularly relevant consequence is the probability of correcting a specified problem before a deadline while respecting specified conditions. Mere reachability is too weak: every valid amendment remains possible even when it is very unlikely to occur soon enough. Recovery probabilities, delay, and relapse should remain a profile of concerns rather than an obligatory aggregate score. [Viability theory](https://link.springer.com/book/10.1007/978-3-642-16684-6) provides an established formal approach to feasible evolution under declared constraints without requiring a scalar maximand.

## Closure can occur at the level of what can be revised

The earlier benchmark's non-absorption argument depends on a reference correction returning from outside the ordinary decision process at regular intervals. Every governor then has some probability of selecting it. That guarantee was supplied by the experiment.

An endogenous-frame model changes the issue. Let \(B\) contain states in which a consequential distinction is absent from the institutional frame. Suppose every evidence, learning, replacement, and proposal transition available from \(B\) preserves that absence. Then

\[
P(S_{t+1}\in B\mid S_t\in B)=1.
\]

Starting in \(B\), the system remains there almost surely under those assumptions. Random selection among all currently conceivable options does not introduce an option outside that set. The system may change personnel, optimize rapidly, or revise many rules while preserving the same exclusion.

This is a conditional invariance argument, not evidence that real institutions have permanently closed boundaries. Occasional outside discovery would instead make escape possible; the important questions would be its rate, cost, credibility, and ability to change action. Nevertheless, it identifies a concrete extension of the meta-attractor account: the recurring pattern can lie in the way a system reproduces its limits on revision, even while its particular rules and occupants change.

The next model must therefore explain how counterexamples and new proposals enter. A reference option that reliably arrives already solves a substantial part of that problem by assumption.

## A small experiment that separates the mechanisms

The next experiment should hold evaluative commitments fixed initially so that epistemic formation can be distinguished from changing values. It should then vary access to consequential distinctions and effective revision rights. Adding every endogenous layer at once would obscure the causal result.

Start from matched states and remove governors' personal allocation stakes. Introduce one outcome variable absent from the default frame, with independently variable access to evidence about it. Specify contextual acceptable ranges and report outcomes separately. Keep scientific access to the true simulated process distinct from what agents can observe. Cross appointment policy with access to evidence and model revision, keeping implementation rights separately controllable.

Four conditional predictions discriminate among explanations:

1. If all governors share the same closed frame, beliefs, interests, and decision rule, appointment changes alone still have no effect.
2. If governors have different frames or informative experiences, appointments can affect outcomes even without private allocation conflict. The old common-interest null required identical candidate evaluations as well as common interests.
3. If informative testimony cannot lead to an authorized action, improving knowledge need not improve timely recovery.
4. Restoring common information, a shared model, and identical interests should recover the old exact null.

Include a condition where the proposed hazard is absent, and charge for trials and mistaken interventions. Otherwise a protected discovery channel could be beneficial by construction. Report learning about familiar situations separately from counterfactual prediction, proposal coverage, decision delay, recovery, and burdens imposed on affected parties. These predictions are a proposed design, not completed results or claims of novelty.

## What an orienting model should make visible

The reusable question becomes: **what consequential experience cannot presently become an effective reason to change this system, and through which mechanism is that route blocked?**

This question can guide inquiry without a complete world model. It directs attention to evidence channels, conceptual limits, incentives, standing, resources, and deadlines. Which experience matters, which intervention is justified, and which constraints deserve protection must be worked out in the situation, with those affected able to contest the account.

More information, more options, and more revision are not automatically beneficial. False evidence, destructive experiments, manufactured doubt, coercive preference change, and endless reopening can undermine the very capacities at issue. The relevant concern is a credible route for learning and justified revision, including the ability to resist such attacks. It is not maximizing openness under a new numerical label.

For AI alignment, this suggests examining how AI changes the surrounding capacity to notice consequences, form alternatives, contest evaluations, and enact justified corrections, alongside how well it follows present instructions. That is a proposed direction for evaluation and design. It is not a complete alignment criterion: legitimate disagreement and protection from harmful actors remain substantive problems.

The theory itself belongs inside this account. If its vocabulary becomes mandatory, excludes consequences it cannot represent, or insulates its users from challenge, it can reproduce the failure it describes. An orienting model earns its usefulness by revealing where its own description needs revision as well as where an institution does.
