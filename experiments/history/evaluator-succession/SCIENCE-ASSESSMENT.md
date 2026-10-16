# Scientific assessment of the evaluator succession model

The current model is a useful controlled mechanism model. It is not established as optimal, a leading general theory, or a new foundation for alignment. A targeted comparison with primary research finds close predecessors to its strongest qualitative result. A deeper audit nevertheless produces a more precise contribution target: **measure when success under current rules ceases to identify rule makers whose decisions support useful correction**.

This assessment was prepared for Ren on 5 October 2026 Bangkok time, using three AI research reviews, direct inspection of the implementation, primary literature, and exact enumeration at saved experimental states. It is not human peer review or an exhaustive novelty search. The existing sealed experiments and their contradicted predictions remain unchanged. Formal derivations and diagnostic details are in [Authority weights and the direction of correction](STRUCTURAL-RESULTS.md).

## What the model presently establishes

The [matched-state experiment](BRANCH-REPORT.md) identifies the total effect of changing future appointments inside one synthetic game. It holds inherited state fixed and preserves paired randomness. This is stronger than comparing separately evolved institutions, but it does not establish validity outside the model or distinguish every causal pathway within it.

| Scientific criterion | Present status |
|---|---|
| Reproducibility | Preserved protocols, source hashes, checkpoints, complete trajectories, paired analysis, and explicit failed predictions |
| Causal identification inside the model | Strong for the specified total appointment-policy intervention; now supplemented by exact conditional governor enumeration |
| Explanatory scope | One mechanism linking beneficiaries of a rubric to authority over that rubric |
| Structural robustness | Not established across behavioral rules, uncertainty, parameter regimes, institution types, or shock processes |
| Prediction outside the model | No human, biological, or trained-agent validation |
| Novelty | Broad feedback, entrenchment, and adaptability claims have close precedents; novelty of a narrower diagnostic or theorem needs further comparison |
| Optimal institutional design | No optimization over a defined policy class and objective; no evidence that either pure appointment policy is optimal |

Many worlds give precise averages under the chosen specification. They do not independently validate the specification. A scientific model can be valuable because it isolates a mechanism; adding realism or complexity does not automatically improve it. A claim of superiority would need an explicit task, competing models, and evidence that this model performs better on that task.

## The closest existing foundations

The strongest predecessor is Acemoglu, Egorov, and Sonin's *Political Selection and Persistence of Bad Governments* (2010). Their model explains how incumbency veto can sustain poor governments and why adaptability to shocks can differ from performance under fixed conditions. Our stable-demand advantage and changed-demand disadvantage therefore cannot be presented as discovery of that distinction. Their forward-looking equilibrium analysis also addresses strategic behavior absent from our current simulation. [Primary paper](https://economics.mit.edu/sites/default/files/publications/Political%20Selection%20and%20Persistence%20of%20Bad%20Governm.pdf).

Several additional bodies of mathematics are directly relevant:

| Primary work | Existing contribution | Implication for this project |
|---|---|---|
| [Barberà and Jackson, Choosing How to Choose](https://bse.eu/sites/default/files/working_paper_pdfs/57.pdf), author working paper revised 2003 | Formalizes constitutions that survive amendment under their own rules | The survival of rules for choosing rules already has a formal equilibrium treatment; our appointment constitution remains externally fixed |
| [Tilman, Plotkin, and Akçay, Evolutionary Games with Environmental Feedbacks](https://pmc.ncbi.nlm.nih.gov/articles/PMC7021758/), 2020 | Couples strategies with environments that alter payoffs and characterizes multiple dynamical regimes | A general mathematical bridge across ecological and institutional feedback exists; different structures need not share an attractor |
| [Perdomo et al., Performative Prediction](https://proceedings.mlr.press/v119/perdomo20a.html), 2020 | Models predictions changing the outcomes or distributions on which they are evaluated | Evaluation participating in its own evidence-generating process is established territory |
| [Everitt et al., Reward Tampering Problems and Solutions](https://arxiv.org/abs/1908.04734), revised 2021 | Uses causal influence diagrams to characterize incentives to alter reward functions and inputs | Evaluator appointments can be studied as a specific route to control over evaluation; the broad alignment connection is not new |
| [Carroll et al., AI Alignment with Changing and Influenceable Reward Functions](https://proceedings.mlr.press/v235/carroll24a.html), 2024 | Models changing preferences, influence over them, and difficulties across candidate alignment objectives | A fixed, externally supplied usefulness function bypasses an important alignment problem |
| [Itao and Kaneko, Self-organized Institutions in Evolutionary Dynamical-systems Game](https://arxiv.org/abs/2501.07249), 2025 | Models emergent norms and punishment through decision rules interacting with resource dynamics | Endogenous institutions and their persistence are an active, already formalized research area |

These are selected comparators, not a ranking of the entire field. Their results are conditional on their own assumptions. What may be distinctive here is a specific, testable decomposition connecting evaluation, allocation, appointment, and rule revision, followed by evidence that it adds explanatory or predictive value beyond those frameworks.

## A more accurate description of our mechanism

Our implementation chooses governors using contract shares generated by the current rubric. It does not select them for independently measured expertise in evaluating others. All governors have the same information and computational capacity. The model therefore tests **giving current beneficiaries authority over the rules producing their benefits**. It cannot establish that selecting competent evaluators is inferior to random selection.

Every governor already evaluates the exact current usefulness signal, including the changed demand. An amendment is valued through its personal allocation benefit plus a fixed concern for common usefulness, minus its cost. Rejecting a useful correction can therefore be an informed choice with private benefits. Knowing a correction, wanting it, and having authority to implement it are separate conditions.

The protected branch adds enforceable constraints: a veto of harmful changes and compulsory implementation of a qualifying reference correction. It has no superior information in the implementation. Its ordinary counterparts also evaluate the true usefulness of the same proposals. The branch demonstrates what those enforcement assumptions accomplish, not where sustainable enforcement comes from.

The authority memory has a half-life of only \(\log(.5)/\log(.75)=2.41\) epochs. The persistence observed many epochs later cannot be attributed to an unchanged memory of preshock success alone. Current allocations under the still-favorable rubric continually renew that authority signal. A no-memory ablation is still needed to determine how much the memory term contributes.

Agents do not anticipate future appointment benefits or strategically invest in power. There is no accumulated wealth, entry, extinction, or learning of a power-seeking policy. Governors judge amendments on frozen submissions rather than anticipating production responses. These choices isolate a simple feedback mechanism while leaving major alternative explanations and extensions open.

## An exact quantity that goes beyond the outcome plots

At one fixed state, let \(\pi_i\) be the chance that agent \(i\) governs and \(m_i\) the expected immediate usefulness change under that agent's actual decision rule. Then

\[
\mathbb E[\Delta W\mid\pi]-\mathbb E[\Delta W\mid\text{uniform}]
=\operatorname{Cov}_{i\sim U}(n\pi_i,m_i).
\]

This elementary identity is not a novelty claim. It makes a useful distinction: concentrated authority helps locally when it favors beneficial decision makers and hurts when it favors less beneficial ones. Concentration by itself does not specify which case holds.

We computed every possible governor's decisions at the first postfork production epoch and the first subsequent reference-offer epoch, using the saved worlds. Both hypothetical appointment policies faced exactly the same state in each calculation. The covariance was positive on average under stable demand and negative after the demand change, from both source histories. At the first reference offer after success-based history, the same states yielded expected immediate gains of **0.007188 under success-based appointment and 0.075304 under uniform appointment**. This is an exploratory local diagnostic, not a new confirmatory experiment or a decomposition of the full long-run policy effect.

The mathematics also produces two exact controls. Removing governors' personal allocation stake makes their choice distributions identical, so appointment policies must produce identical production and rubric paths under shared draws. Permuting appointment weights among identities preserves concentration, while its average immediate effect equals uniform appointment. These controls identify the coupling between authority and divergent interests as necessary for the particular mechanism implemented here.

In a restricted smooth, memoryless version, weighting appointment by allocation adds a gradient term that favors concentration of allocations. This offers one conditional explanation for accumulation pressure without assuming agents directly enjoy domination. It is not a universal law: private interests, the appointment link, behavioral approximations, and constraints matter. The derivation and a counterexample to uniform governance guaranteeing welfare improvement appear in the [technical note](STRUCTURAL-RESULTS.md).

## The deeper mathematical framing

The most defensible common structure is coupled adaptation: behavior changes rewards and institutions, while those rewards and institutions change subsequent behavior. That does not require a single scalar objective. Even a smooth two-agent version of our allocation game generally has unequal cross-partials in its joint learning field, so it cannot be ordinary gradient ascent on one shared potential. [Differentiable game mechanics](https://proceedings.mlr.press/v80/balduzzi18a.html) formalizes the broader distinction between potential and non-potential interactions.

A proposed schema for organizing further work is

\[
x_{t+1}=F(x_t,r_t,e_t),\quad
\pi_t=Q_{\phi_t}(\text{performance history}),\quad
r_{t+1}\sim K(\,\cdot\mid x_t,r_t,e_t,\pi_t),
\]

where \(x\) is behavior, \(r\) the evaluation rule, \(e\) the environment, and \(\phi\) the constitution determining how authority is assigned. This is a modeling template, not a new theorem. The current benchmark allows \(r\) to change but fixes \(\phi\) from outside. A fuller model would examine the incentives and resources that sustain or amend \(\phi\) itself.

For alignment, a substantive candidate requirement is that the process for revising objectives retain enough independence, information, and implementation capacity to correct mistakes. Existing assistance-game research additionally addresses uncertainty and disagreement over objectives: [Cooperative Inverse Reinforcement Learning](https://arxiv.org/abs/1606.03137) and [Multi-Principal Assistance Games](https://arxiv.org/abs/2012.14536). Our supplied common usefulness function does not solve those problems. Dynamics can tell us how a chosen objective changes; it cannot by itself determine whose values should define that objective.

The attractor language also needs refinement. The simple authority ODE has a locally stable positive equilibrium whenever it exists under linear tracking, with no periodic orbits in the positive quadrant. In the stochastic benchmark, full-support choices and recurring reference offers prevent an indefinitely absorbing class that excludes the reference rubric. Neither fact rules out damaging delay or relapse. The next useful objects are correction-time distributions, relapse rates, and the duration of harmful regimes relative to environmental change. A proposed ratio of correction time to environmental timescale would be a hypothesis to investigate, not an established universal threshold.

The same distinction matters for the original cancer analogy: a transferable structural theory needs an explicit mapping of state variables, selection, environmental modification, and correction mechanisms, plus domain evidence. No result from this institutional game establishes a cancer attractor shape.

## The next model should discriminate among explanations

The next step should preserve a small interpretable core and change assumptions that can overturn the explanation. These are proposed tests, not completed experiments:

1. **Validate the conflict pathway.** Implement the exact common-interest null and authority-identity permutations before adding complexity. Appointment effects that survive the null would indicate an implementation error or an additional modeled pathway.
2. **Separate competence from incumbent benefit.** Compare rubric-share appointments with an independently measured, allocation-independent contribution signal while matching selection concentration. Using current share multiplied by usefulness would contaminate the new signal with the old rubric.
3. **Test foresight.** Let governors assess candidate rules after a fixed number of production-response rounds. This distinguishes conflict persisting despite anticipated adaptation from artifacts of evaluating reforms on old behavior.
4. **Compare adaptive policies.** Evaluate mixtures of success-based and uniform appointment, caps, turnover, and recent evidence across different shock sizes and frequencies. Neither pure policy has been optimized. Keep evaluation environments separate from environments used to choose the policy.
5. **Make safeguards contestable.** Model costs, financing, appointment reform, and resistance to enforcement; test whether a useful correction institution survives incentives to weaken it.
6. **Establish external discrimination.** Derive a prediction that competing models do not share, then test it using organizational data, controlled human experiments, or agents that learn rather than follow stipulated logit responses.

The strongest current contribution target is a theory of **when and why selection through existing evaluations selects against useful revision of those evaluations**, with measurable conditions and robust intervention boundaries. The exact local identity and matched-state design provide tools for that program. Scientific novelty and generality must be earned by results that survive these comparisons.
