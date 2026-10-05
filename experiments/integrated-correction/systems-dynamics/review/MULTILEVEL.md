# Situated goals, shared conditions and feedback across levels

5 October 2026. Conceptual and formal architecture prepared as an internal AI research memo. It distinguishes the conditional mechanisms already proved from a proposed broader class of networked adaptive games. It supplies neither a universal objective nor an empirical validation of that architecture.

## The object of explanation

The appropriate object is a system whose participants change their circumstances while those circumstances change their purposes, interpretations, capabilities and relationships. Treating everyone as optimizing one fixed quantity would omit part of the phenomenon. Treating every observation as unique and incomparable would omit the recurring causal relations that a useful theory can identify.

The middle position is a family of restricted, situated models. Each application declares its boundaries, causal mechanisms, resources, observations, legitimate concerns and time horizon. Shared formal structure consists of the types of dependence and the restrictions they impose, not identical coefficients, a universal hierarchy of levels or a single scalar good.

For this architecture, “commons” is used broadly for a **shared causal condition**. It may include replenishable water, trusted evidence, skill transmission, interoperable infrastructure, a usable environment or the ability to challenge decisions. This broad usage does not erase the distinctions among common-pool resources, public goods and excludable shared services: rivalry, exclusion, congestion and governance can give them different failure mechanisms. Dependence on a condition can connect people pursuing different ends. Its existence does not imply agreement about a global objective, nor that centralized optimization is desirable. Cooperation, contest, bargaining and protective constraints are possible mechanisms to investigate, not consequences of calling something a commons.

## A state description that keeps distinct questions separate

For a network of participants i and overlapping institutions g, use a state

S_t=(E_t,N_t,I_t,{R_i,t,Φ_i,t,b_i,t,≽_i,t}_i).

- E records material and functional conditions, with their production, depreciation and transfer accounts.
- N is the network of dependence, contact and access, including its current participant set. Different edges can carry goods, testimony, instruction, authority or contagion; they should not be collapsed merely because all can be drawn as lines. Entry, exit and succession require explicit events and transfers, not an assumption that every present actor persists indefinitely.
- I records implemented rules: admissible actions, actual decision rights, financing, evaluation, appointment, amendment and succession. It includes the mechanisms through which changes can become effective.
- R_i records a participant's operational resources and capacities.
- Φ_i=(O_i,M_i,L_i,A_i) records observation channels, representable causal models, rules admitting evidence and conceivable actions.
- b_i is belief within that frame. A new estimate within M_i is different from a revision of M_i or the discovery of an action outside A_i.
- ≽_i is the participant's current evaluative relation. It need not be complete, numeric or shared by others.

Organizational and societal variables can be aggregates of these states or additional causal states such as enforceable decision rights. The same resources must not be counted once at each level. Overlapping institutional membership does not create additional labor, money or evidence by itself.

A model becomes explanatory only when it supplies restricted update mechanisms. One possible schema is

o_i,t ∼ O_i(·|S_t,a_t),

a_i,t ∼ π_i(·|Φ_i,t,b_i,t,≽_i,t,R_i,t,I_t),

(E,N,R)_{t+1} ∼ P(·|S_t,a_t),

(Φ_i,b_i,≽_i)_{t+1} ∼ L_i(·|S_t,a_t,o_i,t,admitted testimony),

I_{t+1} ∼ K(·|S_t,a_t,proposals,implemented decisions).

The kernels must represent different mechanisms, not unrestricted functions selected after observing the desired answer. Policies shape the distribution of experience; experience can revise policies, representations and values; institutional rules can filter each route. Unanticipated novelty beyond the analyst's state space remains outside a finite implementation even when the model includes several possible discoveries.

## Multiple goals without hidden fixed weights

For a proposed action or policy, retain a vector of consequences z_i: for example livelihood, service quality, burden, discretion, environmental exposure and capacity to recover. Different participants can use different dimensions and interpret shared dimensions differently. A partial evaluative relation can prefer one vector, reject it or leave two vectors incomparable.

This does not uniquely determine behavior. A model must also specify a choice mechanism: aspiration thresholds, negotiation, lexicographic priorities, voting, deference, habit, experiments or a measured choice probability. Writing “Pareto” does not make an actual choice emerge when the alternatives trade off concerns. Similarly, a changing vector of scalar utility weights is only one special representation; it does not represent discovery of a previously absent concern or refusal to exchange a right for additional output.

Three kinds of change should be recorded separately:

1. A new observation changes belief about what an existing action does.
2. An encounter changes what an agent can represent or propose.
3. Reflection, social influence or coercion changes what the agent regards as acceptable or important.

These can interact but are not interchangeable. Apparent preference change may instead reflect reduced options, a new prediction or coerced compliance. Identifying the mechanism requires observations and interventions beyond a new action choice alone.

The modeler's evaluative commitments remain separate from the participants' modeled relations. Describing how an institution changes people's values does not justify the change. An assessment can state several protected conditions and report disagreement rather than infer legitimacy from persistence or popularity. Those protected conditions are substantive commitments requiring public justification and revision; mathematics does not choose them automatically.

## Why locally improving subsystems can destabilize the whole

An elementary two-level linearization makes the issue precise without a common objective. Let u describe a local adaptation deviation and v a change in the environment or institution that selects it:

udot=−αu+βv,

vdot=γu−δv,

with α,δ>0. Holding the other level fixed, both deviations decay. Together the characteristic polynomial is

λ²+(α+δ)λ+αδ−βγ.

If βγ>αδ, the full system has a positive eigenvalue despite each isolated subsystem's restoring response. If βγ<αδ, this two-state system is locally asymptotically stable. The boundary requires separate analysis. This is established feedback mathematics, not a new universal law.

The distinction is useful: better performance of each component under a fixed background need not improve the coupled system. Conversely, interaction need not produce degeneration; the sign, strength and timescale of the links matter. A concrete empirical test perturbs the local policy while measuring the induced institutional response, then perturbs the institution while measuring the local response. Measuring α and δ alone misses the cross-level loop.

In a larger model, the relevant Jacobian has blocks for local adjustment, shared conditions, cognition and institutional revision. Stability is a property of their composition. A joint dynamics need not be the gradient of one potential, and a policy intervention changes several blocks at once. A partial derivative with respect to one abstract coefficient is not automatically the effect of an implementable reform.

## A concrete connection already present in our model

The four-state paid-verification model is an exact restricted instance, although it retains fixed return-based goals:

user practices → collected output F → paid capacities C and G,

G and custodian practices h → effective checking D,

D → returns to paying, bypassing, maintenance and fraud → subsequent practices.

The two populations have different local concerns and different decision roles. Their coupled operation can maintain or destroy the capacities needed for either activity. Resource flow and effective checking mediate the feedback; no central system optimizer makes it work. The model proves a favorable regime and failure regimes under the same declared mechanisms.

Nevertheless, its task, fee τ, budget split λ, work requirement m, receipt categories and private-return comparison remain fixed. It represents endogenous operation of a specified institution, not the formation of all its purposes or rules. The existing situated-frame model separately demonstrates a paid inquiry/awareness loop but keeps a common fixed benefit. Neither result should be relabeled a completed account of plural evolving values.

## A concrete next-level feedback: revising the work rule

Allow a manager to revise the required maintenance fraction m in response to a verification-capacity target G_target:

mdot=εm(1−m)(G_target−G), with ε>0.

This rule changes a parameter of the lower-level game in response to the state generated by that game. A verification shortfall leads it to require more maintenance from each contract. That increases the amount delivered by an honest contractor but also reduces the contractor's retained compensation; the honesty margin is D−m. Less honest maintenance then reduces verification, potentially prompting a further increase in m.

The controller assumes accurate observation of G and executable, unpriced rule adjustment. Its target and update law remain supplied from outside the operating dynamics, and it continues to update after the service's fee base collapses. That continuing governance capability is an added primitive, not a newly proved self-financing institution. Endogenizing one rule does not endogenize its target or explain how plural purposes are formed.

This is a precise two-way interaction between operational selection and governance revision. It is deliberately a **single-goal feedback rule**, not a formalization of situated plural judgment. The coordinating agent's numerical comparison uses the same starting state x=.94, h=.93, C=2.7, G=2.4 and m=.5. With G_target=4, ε=.1 recovers to x=h=1, C=3, G=4 and m=2/3, whereas ε=1 loses payer participation and both capacities while m approaches one. A comparison target G_target=3.6 recovers even at ε=10, so rapid response is not universally harmful.

The mathematical lead separately establishes that the desired full-participation equilibrium remains locally stable at every positive response speed in the admitted parameter range. The failed trajectory therefore concerns the global basin and an overshooting transient, not a demonstrated Hopf bifurcation or a universally destabilizing gain threshold. This matters: a feasible, locally stable destination does not establish that the rule reaches it from the situation in which it is deployed.

A useful plural diagnostic keeps two concerns distinct at the current state:

- Preserve a declared honest-maintenance incentive margin D−m≥δ_h>0.
- Do not deplete verification capacity immediately: Gdot≥0.

For hV>0, these require

μ_G G/(η_G hV) ≤ m ≤ D−δ_h.

If the interval is nonempty, a situated governance procedure can select within it using its other priorities. If it is empty, **no present choice of m meets both concerns**. More funding, different technology, a different participant mixture, reduced workload or an explicitly accepted tradeoff is required. The empty interval reveals a conflict that maximizing a single verification score could conceal.

Payer participation supplies a third distinct condition, A q(C)D−τr(C)≥δ_x if a positive current participation margin is protected. At a fixed state this expression does not depend on m. Changing the maintenance requirement can influence future h and G, but cannot instantly repair an already negative payer margin. A governance rule should report that infeasibility rather than label any change in m a simultaneous solution to all three concerns.

This is an instantaneous feasibility calculation. It is not a guarantee under adjustment delays, unobserved states or strategic manipulation, nor an optimum over all social concerns. With the reference full-participation state, C=3 and the original conversion parameters, η_G V=6. At zero strict margin the inequalities reduce to G/6≤m≤G/(1+G); their strict intersection requires G<5. That bound comes from this task and contract, not a universal limit on institutional capacity.

A temporarily empty interval also does not prove eventual failure. The institution could consume a reserve, permit a temporary stock decline, or change another condition and later recover. In the lower-target fast-response comparison, the interval is briefly empty but the trajectory recovers. The interval is a profile of simultaneous current constraints, not a replacement for dynamic analysis.

## Tests that discriminate among explanations

The next comparisons should preserve different outcome dimensions and manipulate the intended mechanism:

| Hypothesis | Intervention | Measurements that distinguish it |
|---|---|---|
| A local target induces harmful rule revision through delayed maintenance | Vary revision speed at the same capacity target and initial state | Work requirement, custodian returns, delivered work, verification and user participation over time |
| A representation limits which consequences can become reasons | Admit a previously excluded diagnostic observation while holding resources and interests fixed | New distinctions expressed, counterfactual prediction, proposal entry and authorized response |
| An action change reflects altered values rather than new information or pressure | Hold beliefs and feasible options fixed while varying a declared social-learning or deliberation process | Separate elicitation of evaluative relations, refusal rights and choices under unchanged material incentives |
| A shared condition is degraded by local selection | Change who bears a specified downstream consequence while holding its physical effect fixed | Local practice change, cross-network exposure, absolute shared stock and recovery after disturbance |
| A plural feasibility rule avoids hidden conflict | Compare a target-only rule with an explicit constraint-based choice procedure at matched resources | Separate protected-condition breaches, target attainment, false interventions, burdens and unresolved conflicts |

These are proposed designs. Values cannot literally be held fixed by decree in a human experiment; the relevant assumptions require measurement and uncertainty. A null result or an improvement under a simpler account should redirect the theory. Report structural robustness, intervention effects and failures separately from how many simulated worlds were run.

The broader contribution target is therefore a theory of **how situated agents and the conditions that form them reproduce or revise one another across levels, and when their interacting adaptations preserve the capacities for further response**. The present theorems establish bounded pieces of that claim. They do not yet integrate open-ended goal formation, network change, material regeneration, institutional succession and legitimacy in a single validated model.

## Implementation review of the systems analysis

I read `analyze_system.py` and its saved `results/analysis.json`. No blocking discrepancy was found in the implemented adaptive rule or the instantaneous feasible interval. Integrating the log odds of m with derivative ε(G_target−G) correctly implements the stated physical m equation. At the desired equilibrium, the capacity eigenvalue is −49/58. The remaining G,m block is [[−1,6],[−εm_*(1−m_*),0]], whose trace is negative and determinant positive at every ε>0 and interior m_*. The separately computed payer and custodian margins are positive at the two chosen targets.

The lower-target fast comparison reaches approximately m=.98772 during its transient, briefly violating the fixed-m stability interval, yet recovers. Neither an instantaneous crossing of that fixed-rule threshold nor the briefly empty current-feasibility interval proves irreversible loss. The failed higher-target path instead numerically enters a stronger joint loss region at the sample time 21.6; the analytical region condition, once satisfied by an exact trajectory, establishes its continuation.

The basin map labels numerical entry into proved recovery or loss regions on the specified slice C=G=3. Its half-step comparison has no classification disagreements, and 32 adaptive-solver spot checks agree. Those checks support the numerical classification. They do not constitute interval-arithmetic validation of the trajectories, the entire basin boundary or unsampled initial conditions. The saved output appropriately records that distinction.
