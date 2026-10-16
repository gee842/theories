# Observability, safe action, and the time remaining for correction

Research memo, 4 October 2026. AI-generated mathematical synthesis for the integrated selection–renewal project. This memo supplies a finite-horizon formulation, elementary proofs, and a worked counterexample. The mathematical ingredients are established partial-observation control and safety-game ideas; no originality claim is made for them. The prospective contribution is their explicit coupling to maintained information, authority, repair capacity, and reserves in the selection–renewal framework.

## Position within the foundation

The [foundation draft](../../../sources/15-codex-theory-conversations/2026-10-04-selection-and-generative-conditions.md) distinguishes actual conditions from their measurements, feasible correction from implemented correction, and absolute support from relative success. Its existing identification example shows that identical composition trajectories can accompany recovery or collapse. The result developed here concerns a different limit: even when every plausible physical state is individually recoverable, the controller may lack an observation-based policy that recovers all of them before the opportunity closes.

The organizing statement is:

> Guaranteed correction requires either a common safe response across the states still considered possible, or sufficiently early evidence to distinguish states requiring incompatible responses. Resources and authority must keep that possibility open until the response can take effect.

This requires action-relevant information, not complete observation of the world. Many uncertain states need the same safe response. Conversely, a small uncertainty about a binding constraint can be decisive. A scalar prediction error, confidence score, or information quantity does not establish whether the remaining uncertainty changes the safe action.

## A finite-horizon model with continuing observations

Use a finite state space \(X\), finite action set \(U\), observation set \(Y\), and protected set \(K\subseteq X\). An action has a nonempty set of possible successors

\[
x_{t+1}\in F(x_t,u_t),\qquad y_t=h(x_t).
\tag{1}
\]

The transition relation includes the declared disturbances and model uncertainty. For a stochastic model, taking its positive-probability support gives this finite-horizon robust formulation. It concerns guarantee against every allowed transition, not maximization of average reward. An unavailable action can be represented as a transition to an absorbing failure state. If action availability is itself visible, that observation belongs in \(h\).

The state must include whatever makes the model Markovian: time, reserves, pending repairs, diagnostic delays, actuator condition, and authority can all be state components. The controller observes its own executed actions and the observation history, but not hidden state. A deterministic policy is

\[
u_t=\pi_t(y_0,u_0,y_1,\ldots,u_{t-1},y_t).
\tag{2}
\]

A randomized policy maps this same history to a distribution on actions; its private randomness supplies no information about the hidden state. Safety for \(\ell\) remaining transitions means remaining in \(K\) at the present time and after every one of those transitions. The protected set expresses the declared objective; mathematics does not determine its ethical legitimacy.

Let \(B_t\) be the set of states consistent with the full observed history. It is an information set, also called a belief support, without an assigned probability distribution. After action \(u\) and observation \(y\), it updates as

\[
\Phi(B,u,y)=\left(\bigcup_{x\in B}F(x,u)\right)\cap h^{-1}(y).
\tag{3}
\]

Only nonempty updates represent possible observations. This update includes information obtained through action. A safe diagnostic experiment is an available action with informative successors, not an exception to the model.

## Exact criterion: viability of the information set

Define collections of winning information sets recursively:

\[
\begin{aligned}
\mathfrak W_0&=\{B:\varnothing\ne B\subseteq K\},\\
\mathfrak W_{\ell}
&=\left\{B:\varnothing\ne B\subseteq K,\ 
\exists u\in U\ \forall y\text{ with }\Phi(B,u,y)\ne\varnothing,
\ \Phi(B,u,y)\in\mathfrak W_{\ell-1}\right\}.
\end{aligned}
\tag{4}
\]

**Proposition 1 — exact finite-horizon safety criterion.** An observation-based policy guarantees safety for \(\ell\) transitions from every state in \(B\) if and only if \(B\in\mathfrak W_\ell\).

**Proof.** With zero remaining transitions, the criterion is exactly \(B\subseteq K\). For the induction step, the controller must take one common first action for the entire information set. Every observation that action can produce must lead to an information set permitting safety for the remaining \(\ell-1\) transitions. This is necessary. It is sufficient because the controller can choose a witnessing first action and then use the corresponding inductively safe policy for each observed successor information set. The model is finite, so these choices define a policy. ∎

Define the available safe actions at that information set by

\[
U^{\mathrm{obs}}_\ell(B)=
\{u:\Phi(B,u,y)\in\mathfrak W_{\ell-1}
\text{ for every possible }y\}.
\tag{5}
\]

The criterion is therefore \(B\subseteq K\) and \(U^{\mathrm{obs}}_\ell(B)\ne\varnothing\). It accounts for all future observations, not only the present ambiguity. It is exact for the declared finite model and horizon. An incomplete transition model or an information set that excludes the actual state invalidates its guarantee.

This is a specialization of established partial-observation safety machinery. Chatterjee, Doyen, Henzinger, and Raskin develop observation-history strategies, information-set updates, and algorithms for games with incomplete information; their 2006 report explicitly distinguishes sure safety from more general objectives for which randomization changes what is achievable. [Primary report](https://www2.eecs.berkeley.edu/Pubs/TechRpts/2006/EECS-2006-89.pdf)

## A simple impossibility certificate

First compute the more optimistic full-information viability sets:

\[
\begin{aligned}
V_0&=K,\\
V_\ell&=\{x\in K:\exists u\in U,\ F(x,u)\subseteq V_{\ell-1}\},\\
U^{\mathrm{full}}_\ell(x)
&=\{u\in U:F(x,u)\subseteq V_{\ell-1}\}.
\end{aligned}
\tag{6}
\]

An action in \(U^{\mathrm{full}}_\ell(x)\) leaves some safe continuation available to a controller given full state information thereafter. That makes the set optimistic relative to the actual information restriction.

**Proposition 2 — incompatible required responses.** Suppose \(\ell\ge1\), \(B\subseteq K\), and

\[
\boxed{\bigcap_{x\in B}U^{\mathrm{full}}_\ell(x)=\varnothing.}
\tag{7}
\]

Then no observation-based policy guarantees safety for \(\ell\) transitions from every state in \(B\). This can hold even when \(B\subseteq V_\ell\): each physical state is individually viable, but their unresolved combination is not viable for the controller.

**Proof.** A common observation history requires a common first action \(u\). By (7), some compatible state \(x\) makes that action leave a possible successor outside \(V_{\ell-1}\). Even a subsequent controller with full information cannot guarantee safety from that successor. The observation-based controller therefore cannot guarantee it either. ∎

The converse does not hold: a nonempty intersection of these full-information action sets need not yield an observation-based safe policy. A common first action may preserve each state's individual viability while leading to another unresolved conflict before the horizon ends. Equation (4), not intersection alone, supplies the sufficient condition.

Randomization cannot restore a probability-one guarantee in this finite-horizon setting. With finitely many actions, some action receives positive probability. If no action is safe for the whole information set, a compatible initial state and allowed continuation make that action fail with positive probability. In a finite stochastic model, every allowed finite path in the transition support has positive probability. This argument is not a general claim that randomization is useless for partial-observation reachability, expected reward, or infinite-horizon objectives.

For the special case of one irrevocable choice between two hidden states with disjoint successful action sets \(A_1,A_2\), a randomized choice \(\mu\) obeys

\[
\min\{\Pr(\mathrm{success}\mid 1),\Pr(\mathrm{success}\mid 2)\}
\le \min\{\mu(A_1),\mu(A_2)\}\le\tfrac12.
\tag{8}
\]

This quantitative bound applies to that commitment structure; empty intersection across an arbitrary number of sets does not automatically imply the same one-half bound.

## Information must arrive before the commitment deadline

Consider a support reserve \(e\) with a protected floor \(e_{\min}\). Until an intervention becomes effective, suppose every admissible action leaves an unavoidable nonnegative net deficit bounded below by \(d_-(t)\):

\[
\dot e(t)\le-d_-(t),\qquad d_-(t)\ge0.
\tag{9}
\]

If effective correction cannot occur before \(\tau\), a necessary reserve condition is

\[
\boxed{\int_0^\tau d_-(t)\,dt\le e_0-e_{\min}.}
\tag{10}
\]

Violation proves that the reserve cannot stay above its floor through the delay. Equality requires special care: whether effective correction exactly at the floor succeeds depends on the model's boundary and timing conventions. With signed deficits that can become negative, one must check every intermediate cumulative deficit, not only its value at the endpoint.

This condition is necessary, not sufficient. Enough reserve does not establish that the right response is identifiable, authorized, physically possible, or compatible with other constraints. Conversely, (9) must be a bound valid for every relevant pre-correction action before its violation can establish impossibility. A deficit under one chosen policy only evaluates that policy.

For a diagnosis-then-repair architecture with sequential delays, write

\[
\tau=\tau_{\mathrm{information}}+
\tau_{\mathrm{decision}}+
\tau_{\mathrm{mobilization}}+
\tau_{\mathrm{repair}}.
\tag{11}
\]

If some stages overlap, use the actual critical path instead of this sum. Informational delay means time to distinguish states that require incompatible responses, not time to observe every state variable. An active test can shorten it, but its reserve cost and risk belong in the same dynamics.

A converse reserve certificate needs an upper bound \(d_+(t)\) for an explicit feasible policy: if its maximum cumulative loss before completion fits inside the reserve, all other constraints hold, and its post-completion trajectory stays in the protected set, that policy is safe. The lower-bound impossibility test and upper-bound policy certificate must not be interchanged.

## Worked example: a diagnosis arrives one unit too late

Let a system have a fixed hidden fault \(\sigma\in\{-1,+1\}\). A functioning reserve starts at \(e_0=10\), has protected floor zero, and declines at one unit per unit time until a correct repair finishes. Other repair supplies and funding, denoted \(B\), are available in any desired quantity; they do not shorten the specified diagnostic or physical completion times.

There are two mutually incompatible repair recipes \(a\in\{-1,+1\}\). Starting one is an irreversible commitment. It takes \(L=3\) units of time. If \(a=\sigma\), completion stops the reserve loss; otherwise it causes failure. The recipes cannot safely be combined, reversed after initiation, or accelerated by spending \(B\). No common prophylactic response or pause is available in this example. Those are substantive assumptions; changing them is one way to change the result.

Before \(t=8\), all observations, including reserve level and repair supplies, are identical in the two hidden states. No available action provides an earlier safe diagnosis. At \(t=8\), a diagnostic reveals \(\sigma\) perfectly. The system must remain safe beyond \(t=10\). Correct completion exactly at \(t=10\) is allowed to stop loss at the floor.

Both states are individually viable: a fully informed controller starts the correct recipe immediately and completes it at \(t=3\), with reserve seven. For the actual controller, however,

\[
T_{\mathrm{reserve}}=10,\qquad
t_{\mathrm{latest\ commitment}}=10-3=7<8=\tau_{\mathrm{information}}.
\tag{12}
\]

Any policy that waits for the diagnosis finishes no earlier than \(t=11\), after reserve failure. Any policy that commits in time must choose before the states are distinguishable. At the final commitment time the successful action sets are \(\{-1\}\) and \(\{+1\}\), so (7) rules out a guarantee. By (8), the best worst-case success probability is one-half, achieved by an unbiased choice made in time. A deterministic policy fails in one of the two states. Everybody can share the same safety objective; the failure requires no bad intention, conflicting incentive, or lack of generic funds.

This example proves no universal irrelevance of resources. The binding reserve is precisely a resource that can buy the missing time. Increasing \(e_0\) from ten to eleven permits diagnosis at eight and completion at eleven. Earlier information, shorter physical repair time, a reversible intervention, or a common safe fallback can also change feasibility. Arbitrarily abundant resources help only through the transitions they can actually change before the deadline.

For this particular model, with perfect revelation at \(\tau_I\), constant deficit \(d>0\), no earlier informative action, and completion latency \(L\), the exact guarantee criterion is

\[
\boxed{\tau_I+L\le\frac{e_0-e_{\min}}{d}.}
\tag{13}
\]

It is sufficient because the controller waits safely for revelation and starts the correct repair. It is necessary because later revelation leaves only indistinguishable incompatible commitments before the latest feasible start. This equivalence belongs to this explicitly specified architecture, not to all repair systems.

I independently checked the integer-time instance by finite-horizon backward recursion over information sets through time twelve. The transition model included irreversible initiation, the pending-completion timer, diagnostic revelation, and absorbing failure. The results matched (13):

| Revelation time | Initial reserve | Completion latency | Guaranteed safe policy |
|---:|---:|---:|:---|
| 8 | 10 | 3 | No |
| 7 | 10 | 3 | Yes |
| 8 | 11 | 3 | Yes |
| 8 | 10 | 2 | Yes |
| 0 | 10 | 3 | Yes |

The [standard-library Python verification](verify_observability.py) and [saved results](observability-checks.json) make these checks reproducible. Run `python3 verify_observability.py` from this directory; it regenerates the results file. The script also checks correct completion exactly at the reserve floor, failure after the deadline, irreversible initiation, and continuing diagnostic observations during a pending repair.

A separate two-transition example checks why overlapping full-information first-action sets are insufficient: two hidden states both permit the first action `advance`, but its indistinguishable successors require opposite final responses. Each initial state is individually viable, yet no observation-based guarantee exists. Revealing the state after `advance` restores the guarantee. The verification checks both versions using the same backward recursion.

These checks support the worked calculations, not empirical claims about any biological or institutional system.

## Noisy evidence and ongoing sensing

Exact indistinguishability is a sharp limiting case. In the two-recipe commitment problem, let \(P_+\) and \(P_-\) be the laws of all evidence available by the last feasible commitment time under a specified sensing procedure. With equal prior weights, every randomized decision rule has average error at least

\[
\boxed{\Pr(\mathrm{error})\ge
\frac{1-\operatorname{TV}(P_+,P_-)}{2}.}
\tag{14}
\]

To see this, let \(q(z)\in[0,1]\) be the probability of choosing \(+1\) given evidence \(z\). Average success is \(\tfrac12[1+\mathbb E_{P_+}q-\mathbb E_{P_-}q]\), which is at most \((1+\operatorname{TV})/2\). This is the standard binary-testing bound, restated here for the repair deadline. It is not a new statistical result.

If sensing is controlled, its evidence laws depend on the sensing policy. Applying (14) to one passive sensor does not rule out a better active test. A policy-independent impossibility bound requires a total-variation bound holding for every admissible pre-deadline sensing policy, with sensing cost, delays, and safety constraints included. Common safe fallback actions would also change the decision problem. Continuing observations matter whenever they can arrive before an irreversible commitment or permit a safe revised continuation; equation (4) already handles that case.

## What can be measured without a complete model

The framework suggests the following observable or conservatively estimable quantities:

- **Action-relevant uncertainty:** which plausible conditions require incompatible repairs, and which observations can distinguish them?
- **Common safe continuations:** whether a pause, reversible probe, reduced operating rate, or fallback remains feasible across the plausible states.
- **Binding reserves:** margins above independently specified failure floors; generic assets should not be substituted without a demonstrated conversion path.
- **Net loss and renewal bounds:** rates during diagnosis, authorization, mobilization, and repair, including the cost of obtaining evidence.
- **Latest feasible commitment:** the last start time that leaves an actual repair path, rather than merely the time of visible collapse.
- **Delivered correction latency:** observed times from first actionable evidence to authorized action and completed effect; not nominal response targets.
- **Reliability of the information set:** evidence that actual states and disturbances are covered, including channels for discovering omitted failure modes.

For a declared repair route, a useful diagnostic is the margin between latest feasible commitment and the earliest time adequate evidence plus authorization can be delivered. A negative margin is an impossibility certificate only if those times are justified bounds and no alternative common-safe route exists. A positive margin is a candidate opportunity, not a guarantee of implementation.

Biological, human, and AI applications should instantiate these causal roles separately. A stock of generic resources cannot substitute for a lost sensing channel or expired response opportunity without a mechanism that changes the relevant transitions. In AI deployment, maintained evaluation competence, independent evidence, actual intervention authority, and rollback or repair time are possible model variables. Their empirical adequacy must be tested; their inclusion is not itself a proof of alignment.

## Literature and contribution boundary

Three primary anchors delimit the established mathematics:

1. [Chatterjee, Doyen, Henzinger, and Raskin, *Algorithms for Omega-Regular Games with Incomplete Information* (2006 report)](https://www2.eecs.berkeley.edu/Pubs/TechRpts/2006/EECS-2006-89.pdf): observation-based strategies, information-set updates, and sure versus almost-sure winning. The elementary recursion and impossibility certificate above belong to this established line of work.
2. [Carr, Jansen, Junges, and Topcu, *Safe Reinforcement Learning via Shielding under Partial Observability* (AAAI 2023)](https://ojs.aaai.org/index.php/AAAI/article/download/26723/26495): shields based on POMDP belief supports demonstrate that useful safety restrictions can sometimes be computed without exact transition probabilities, provided the necessary transition structure is known. This does not eliminate model coverage assumptions or imply that every partial-observation problem is solvable.
3. [Dean, Taylor, Cosner, Recht, and Ames, *Guaranteeing Safety of Learned Perception Modules via Measurement-Robust Control Barrier Functions* (2021)](https://proceedings.mlr.press/v155/dean21a/dean21a.pdf): continuous-control safety with state-estimation uncertainty supplies a complementary route beyond finite-state models. Its guarantees likewise depend on stated error and dynamics assumptions.

The proposed integration is to model the production and possible degradation of the sensing, deliberation, authority, and repair mechanisms inside the same evolving system. The conditions under which those mechanisms remain funded, competent, authorized, and responsive are the remaining selection–renewal problem. A theorem assuming a permanently available controller cannot settle that problem.

The descriptive result is a constraint on what a controller can guarantee with given information and time. Choosing the protected set, assigning standing to affected people, and determining legitimate authority remain normative and institutional work. More observation is not automatically better in every ethical sense; the formal requirement is enough legitimate action-relevant evidence, or a common safe continuation, before the opportunity for correction closes.
