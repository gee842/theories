# Research design: constraints on a situated rule controller

5 October 2026. Internal AI research-design memo. The earlier fixed-rule and target-following outcomes are already known. This document proposes discriminating comparisons for a new viability filter; it is not an externally registered protocol or a report of new experimental outcomes. Final implementation and mathematical statements should specify which proposed checks were actually performed.

## What the experiment should answer

The previous example shows that a capacity target can be feasible and locally stable while a target-following rule leaves its basin during the transition. A stronger claim now needs a comparison: can explicitly maintaining distinct operating conditions prevent that mechanism, and does a state-dependent filter add anything beyond a slower rule or a simple fixed cap?

The proposed controller should not be called a complete model of plural, evolving goals. It combines a supplied capacity target with separately declared lower bounds and an incentive margin. These concerns are not combined into one welfare score, which is useful. Their legitimacy, formation and revision are nevertheless outside the controller. They remain commitments declared by the analyst or authorized decision maker.

## The candidate and the exact scope of its certificate

The mathematical lead's candidate controls u=mdot with |u|≤.5. Its nominal command is

u_nom=εm(1−m)(T−G).

It projects this command onto

max{−.5,−2(m−.45)} ≤ u ≤ min{.5,Ddot+2(D−m−.02)},

where D=hG/(1+G), evaluated under the canonical dynamics. The proposed protected set requires

x≥.9, h≥.9, C≥2.5, G≥2.1, m≥.45, D−m≥.02.

The mathematical proof establishes feasibility and invariance from that set under its exact-state and exact-model assumptions. Its safety statement must be evaluated separately from target tracking. Preserving an operating set does not guarantee attaining every supplied target, minimizing expenditure or satisfying every affected person's concerns.

All comparisons must use the same actuator interface. A state-dependent filter must not obtain instantaneous jumps in m while its comparators are limited to finite adjustment rates. The shared bound here is |mdot|≤.5. Sampling, initialization, saturation and integration tolerance should also be common. The proposal is a filter on the rule's rate of change, not an instantaneous overwrite of the physical work requirement.

## Comparators that could defeat an inflated interpretation

| Controller | Why it matters |
|---|---|
| Fixed m=.5 | The existing institution can recover without adapting this rule. It may preserve functioning while missing a higher target. |
| Nominal fast target-following, clipped to the shared rate limit | Reproduces the known harmful feedback while matching actuator authority. |
| Slower target-following, clipped to the shared rate limit | Tests whether reducing response speed alone suffices. |
| Fast target-following with a fixed upper cap | Tests whether a simple conservative design achieves the same protection without a state-dependent filter. |
| State-dependent viability filter | Tests the proposed contribution while preserving the nominal command whenever its constraints permit. |

A fixed cap near .7 may already handle the reference target-four trajectory. Its success would be informative, not an obstacle to hide. Choose any tuned cap and slow response gain using a declared calibration set, then freeze them for held-out cases. Do not compare a carefully tuned filter against an arbitrary cap selected to miss the target. Conversely, a cap chosen separately after seeing each test trajectory is an oracle policy, not one transferable comparator.

State-dependent projection consumes more information than a target-only controller. In the idealized comparison, the same full state and parameters should be available to every controller, even if a simple comparator chooses not to use them. Claims about real deployability need an additional measurement study: the true honest-maintenance share h is not automatically observable in an institution. Its estimation, audit dependence and cost must be assessed rather than supplied for free under the label “feedback.”

## Matching resources without removing the mechanism

Match initial stocks, the task distribution, conversion and depreciation, payment rules, fee fraction, budget split, audit technology, measurement access and intervention permissions. Provide no additional replenishment flow to one arm. The honest share and payer share are state variables, not quantities to reset whenever a controller struggles.

Realized fee revenue F is partly an outcome of user participation. It need not remain equal across controllers. Forcing it to be equal after treatment would remove the very financing pathway being investigated or add an undeclared subsidy. Report revenue and expenditures alongside outcomes. Similarly, recording the total variation of m makes adjustment activity visible, but it does not convert an unpriced adjustment mechanism into a fully financed governance process. A monetary or labor cost for rule changes requires its own resource equation.

## A compact test matrix

The following cases are sufficient to distinguish basic claims; additional sweeps should answer a specific unresolved question.

1. **Known difficult target:** T=4 from the common state (.94,.93,2.7,2.4,m=.5). Its slow-success/fast-failure history is known and serves as a regression case, not fresh confirmation.
2. **Known countercase:** T=3.6, including fast nominal response. The earlier fast rule recovers, preventing an inference that rapid adjustment itself is universally harmful.
3. **Near a protected boundary:** choose starts within the certified set, including its low-capacity/lower-share faces. This tests the construction where constraint intervention is meaningful instead of only near the favorable equilibrium.
4. **A legitimate target change:** apply a declared sequence of attainable targets without changing the physical or payment model. This tests responsiveness to revised instructions. It does not explain where the revised purposes originate.
5. **An incompatible target:** T=6. In the canonical full-participation state C=3 and G=6m. A steady G=6 would require m=1, which violates the positive honesty margin. The appropriate outcome is maintained constraints with unmet target or an explicit infeasibility report—not “all objectives achieved.”

Any starts or disturbances chosen specifically to expose the new filter should be labeled exploratory. Held-out initial states and target schedules should be selected by a reproducible rule before comparing their outcomes. A disturbance is inside the proof's scope only if its treatment and size satisfy the theorem's actual assumptions; a certificate for continuous exact dynamics does not automatically cover an instantaneous jump out of its set.

## Out-of-region and misspecification checks

The filter must return its actual admissible control interval and report when it is empty. An arbitrary fallback that violates one bound cannot still be described as a certified intervention.

At minimum, preserve these boundaries:

- A low initial honest share, such as h=.49, lies outside the proposed protected set. Existing results show that infrastructure alone cannot generally repair that condition under the fixed rules. Failure there is not a failure of an inside-set guarantee, and success in one such case does not extend the theorem.
- Depleted productive capacity and low participation can leave too little revenue to maintain verification. A controller acting only through m cannot silently replace the missing resources.
- If the controller uses estimated h, G or funding, test declared measurement errors or delays separately. The exact-model certificate is not automatically robust to them. A robust version would need bounded observation/model uncertainty in its feasibility proof and would need to charge the observation process where relevant.
- The nominal policy still presumes executable rule changes and a functioning observation-to-command channel. The viability filter has not demonstrated that those governance capabilities remain financed or politically available.

No controller should be credited with recovery by clamping a state to a boundary, resetting personnel, adding reserves or discarding required service. Such an intervention may be useful, but its actual input and cost must be recorded separately.

## Keep an outcome profile rather than manufacture a winner

Report distinct quantities:

- Minimum x,h,C,G and minimum D−m, together with any breaches of the declared set.
- Delivered maintenance and its actual funding; user and contractor private-return gaps; duration and depth of negative gaps.
- Target error, time to a declared tolerance, overshoot and which targets remain unachieved.
- Collected fees, maintenance expenditure, fraudulent receipts, withheld reserve and externally supplied resources, if any.
- Total variation of m and time at actuator or constraint limits.
- Infeasible control intervals, measurement failures and imposed interventions.

Do not combine these into one success number without an explicit decision about tradeoffs. A fixed rule can be safer but slower, or use fewer revisions while missing a target. The correct finding can be an unresolved comparison rather than a single optimal policy. The present variables also omit privacy, legitimate appeal, coercive burdens and many distributive concerns, so this profile is not a complete social evaluation.

## Two claims that a discriminating study could reject

**Claim 1: the maintenance-incentive pathway matters beyond capacity shortfall.** Under the specified contract, the relative return to genuine work is V(D−m). At comparable fee revenue and task conditions, changes in the work requirement or enforceable detection should alter actual delivery in the direction predicted by this gap, rather than only through the total nominal maintenance budget. A controlled task study can vary m and executable detection independently and measure delivered work, false claims and subsequent fee participation. If a fitted, independently measured gap does not predict the response—or changes in the response are explained entirely by physical workload—the proposed behavioral pathway lacks support in that application. Human commitments or agent foresight can change the update law; the model does not treat private-money maximization as universal psychology.

**Claim 2: observing the joint state adds useful control beyond a simple fixed precaution.** On a declared held-out set with the same actuator and resource assumptions, the state-dependent filter should preserve its stated conditions while satisfying feasible target requests across circumstances that defeat a single calibrated fast rule or fixed cap. This comparative advantage is a hypothesis, not supplied by the invariance theorem. If a calibrated fixed cap or slower controller matches the outcome profile within a declared practical margin, then the evidence supports a simpler precaution and the new filter's certificate, not its necessity or superiority.

For AI alignment and coordination, the practical question is whether improving a locally measured objective preserves the human and institutional processes that produce, scrutinize and revise its implementation. The proposed study isolates one part of that question. It does not establish that every goal must be fixed, that plural values can be reduced to these margins, or that the policy maintaining an institution is entitled to decide its purposes.
