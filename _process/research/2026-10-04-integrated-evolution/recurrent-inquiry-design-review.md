# Recurrent inquiry and succession: two exact isolation modules

5 October 2026. Design and adversarial review; no simulation or new numerical result. This memo follows the completed bounded-discovery experiment. The coordinating agent has chosen two explicit modules: A, finite-horizon belief and inquiry-capacity control with freely retained memory; B, one succession with costly communication and correct inference from all surviving cues. They should remain separate until an integrated information and resource interface is specified.

The concrete next question is whether a shared-purpose controller pays to preserve the ability to investigate while sometimes deciding not to investigate, and whether a successor can benefit from selectively transmitted evidence without treating silence as a reset. A known diagnostic is an isolation assumption. It does not continue the previous experiment's generation and causal validation of candidate explanations.

## A. Inquiry capacity with a known changing need

Let hidden need \(H_t\in\{0,1\}\) follow a known Markov chain, with \(\alpha=P(H_{t+1}=1\mid H_t=0)\) and \(\beta=P(H_{t+1}=0\mid H_t=1)\). A response prevents a specified loss when need is present and costs \(k\). The belief is \(p_t=P(H_t=1\mid\text{available history})\). Without a new signal its one-step prediction is

\[
\Psi(p)=\alpha+(1-\alpha-\beta)p.
\]

Keep the observation interface explicit. If actual unmet-need loss, treatment success, or a cash balance reduced by that loss is observable, it supplies information and belongs in this filter. Otherwise state that the state-dependent consequence is scored by the evaluator and is not separately revealed to the decision maker. Known procurement and treatment expenses can remain observable because their amounts follow chosen actions. Silently ignoring an observable loss would inflate the value of a paid diagnostic.

Capacity can be ready or absent. A paid rebuild started when absent becomes usable next period; it cannot justify a same-period test. Upkeep preserves readiness. Specify whether an already ready device can be used before choosing to preserve it for the next period, or whether upkeep is required for current use. Either convention is coherent; changing conventions between arms is not.

Before coding, freeze the within-period order: available information, procurement decisions, diagnostic observation, response, consequence, and Markov transition. If a procurement decision can use the diagnostic result, it is a later decision node, not a pre-signal action with clairvoyant access. Do not let a successor receive a fabricated stationary prior in this module: the sufficient belief is explicitly retained for free.

### Negative evidence and an unsuccessful investigation

A diagnostic can return +, −, or \(\bot\), where the last denotes an independently failed or inconclusive measurement. Under the cleanest known likelihood, a successful observation reveals current need perfectly; measurement fails with known probability \(f\), independent of need. The posterior after + is one, after − is zero, and after \(\bot\) remains \(p_t\). All attempted tests incur their declared charge. The subsequent Markov prediction is still required after any result.

If implementation uses an always-successful perfect diagnostic, it can distinguish a negative result from **no inquiry**. It cannot claim to have simulated failed completed inquiries unless a failure symbol and likelihood are included. A state-dependent measurement failure would itself be informative and requires a different posterior.

Negative evidence can have value because it prevents unnecessary action. For a one-period problem with loss one and response cost \(0<k<1\), optimal loss without information is \(\min(p,k)\); after free perfect information it is \(pk\). With test cost \(d\) and uninformative failure probability \(f\), the one-period expected improvement from testing is

\[
(1-f)[\min(p,k)-pk]-d.
\]

This is a useful arithmetic check, not a universal claim that every negative investigation is valuable. Future decisions can change the testing decision in the dynamic problem. Preserve negative evidence with its date and likelihood; known need transitions make an old negative result less decisive over time. Retaining a calibrated belief is different from perpetually repeating the last conclusion.

### Exact optimization and the resource comparison

For a short horizon, solve the finite reachable belief/capacity decision tree by backward induction. With successful perfect measurements and uninformative failures, reachable beliefs are Markov predictions of the initial prior, zero, or one. This keeps the example small. An exact dynamic program means exact enumeration of modeled contingencies, not proof that the assumed transition model is true.

Separate outcome loss, ordinary response expense, tests, upkeep, and rebuilding. A local scalar sum is a declared shared purpose; it does not make these components ethically interchangeable outside the example. Check the returned total against the independently propagated expected components.

Use a per-period hard procurement cap for a first sharp comparison. If it covers only tests, upkeep, and rebuilds, ordinary response funding is a separately supplied condition. If the cap also covers response after a diagnostic, feasibility must hold for every possible result, not just expected expenditure. Expected-cost feasibility and a hard per-period cap answer different questions.

The strongest tractable comparator is the **best ex ante capacity schedule**, optimized under the same cap. Fix only its upkeep/rebuild decisions before observations; allow its diagnostic and response decisions to use the same Bayesian belief, observation likelihood, and free memory as the adaptive controller. Enumerate all feasible short-horizon schedules and optimize the remaining decisions for each. Comparing an adaptive controller with a single arbitrary periodic schedule would confound the value of adaptation with a poorly selected baseline.

Let \(J_{\mathrm{adapt}}(B)\) and \(J_{\mathrm{schedule}}(B)\) be optimal expected total costs at cap \(B\). The schedule class is contained in the adaptive class, so

\[
J_{\mathrm{adapt}}(B)\le J_{\mathrm{schedule}}(B)
\]

is a policy-class inclusion result. A strict improvement and its mechanism remain numerical questions. Sweep the cap, report the difference and every cost component, and describe this as a feasibility-matched comparison. Equal caps do not establish equal actual or expected spending. Optimal cost cannot increase when the cap is relaxed, but testing frequency need not move monotonically.

If a genuinely spending-matched result is needed, add an expected-procurement frontier:

\[
F(R;B)=\min_\pi\mathbb E_\pi[\text{unmet-need loss + response cost}]
\quad\text{subject to}\quad
\mathbb E_\pi[\text{test + upkeep + rebuild expense}]\le R
\]

and the same hard cap \(B\). The finite belief-state model admits an occupancy-measure linear program; fixed capacity schedules can be enumerated and their feasible frontiers compared. State whether ex ante randomization among schedules is allowed; it convexifies the attainable set and must be handled consistently. This optional calculation is preferable to calling two policies matched because their average spending happens to be close. It is not necessary for the first cap-based result.

The decisive capacity witness is a positive-probability reachable state where the optimum pays upkeep but does not test, with a strictly worse counterfactual if upkeep is forbidden there. A plotted average of fewer than one test per period is insufficient: it could mix permanently active and permanently abandoned histories. Report the particular belief, capacity, remaining horizon, chosen action, action-value gap, and its occupancy probability. Separately compare maintaining capacity with rebuilding after a gap; a one-period lag is meaningful only if a lost opportunity can actually occur during it.

Finite-horizon abandonment near the terminal date can be optimal because future capacity has no terminal value. It is not evidence of institutional degeneration. Check early decisions under a longer horizon or clearly limit the result to the finite task. Countercases should include prohibitive test costs, a perfectly informative free signal, static need, and zero rebuild delay/cost. The findings should change when the mechanisms supporting them disappear.

## B. A paid message at one succession

Use a small common-interest communication team. The outgoing actor privately knows a binary state \(H\); both actors know a joint distribution of \(H\) and a publicly visible inherited cue \(C\). State whether the sender also observes \(C\). The sender can publish its truthful state at cost \(a\) or send no message. The successor chooses a response after observing \(C\) and the message, including its absence.

If the sender observes both binary variables, a deterministic publication policy has four binary decisions, hence sixteen possibilities. Enumerate them. For each, compute the successor's best response and exact expected loss plus publication expenditure. An independent brute-force enumeration of the receiver's finite decision rules can verify the result. With an unconstrained expected-cost objective, random mixing of complete deterministic team policies cannot improve on the best pure policy.

For an agreed transmission policy \(\sigma\), the correct posterior is

\[
P(H=h\mid C=c,M=m)
\propto P(H=h,C=c)P_\sigma(M=m\mid h,c).
\]

In particular, \(M=\varnothing\) uses its actual likelihood. Only positive-probability observations need an operational posterior. If policy \(\sigma\) is optimized and publicly known, silence is usually not missing-at-random. Nor may the successor ignore the inherited cue merely because no paid message was received.

A sharp sanity check is selective publication: with perfect sender knowledge, a reliable known communication opportunity, and a publicly understood policy, publishing in just one state can distinguish both states. Silence identifies the other. This can cost less than always publishing. It is a valid signaling result, but relies on the availability of a reliable omission channel. If sender absence, channel failure, an unknown transmission policy, or an unobserved deadline can also cause silence, include those possibilities in its likelihood. The conclusion should then change when silence becomes ambiguous.

Any cash balance, capacity level, visible action, publication timing, or document length available to the successor is also a potential signal. Either include it in \(C\) and the joint distribution, make it independent of private information by design, or remove it from the interface. Do not say the successor has forgotten while leaving it enough correlated public state to recover the supposedly erased information. Conversely, a computational policy that ignores an available cue is a restricted comparator, not a Bayesian no-archive optimum.

Report expected decision loss, publication probability, publication expenditure, and posterior/actions for every realized cue-message pair. Compare no publication, always publication, and optimized contingent publication over a cost sweep. High communication cost or a sufficiently informative public cue should make publication unnecessary in some regimes. A zero-message optimum need not mean loss of usable information.

This module prices publication at one handoff. It does not price the production of the sender's knowledge, the message infrastructure, long-term archive storage, semantic comprehension, repeated succession, or the upkeep of the shared model. It cannot yet establish a law of paid memory renewal. In particular, free reliable silence and a fixed truthful vocabulary are supplied institutional conditions.

## What these two modules can establish

Module A can isolate the value of maintaining an investigative option separately from using it, and distinguish informative absence of need from an uninformative inquiry failure. Module B can isolate paid transmission, surviving public information, and the information carried by withholding a message. A combined model must derive the public cue from the earlier decision process and carry its observation likelihood into succession. Merely connecting the modules while resetting beliefs would not do this.

The mathematical foundations are established: [Smallwood and Sondik's finite-horizon partially observed control](https://pubsonline.informs.org/doi/pdf/10.1287/opre.21.5.1071) supplies the belief-state decision framework; [Nayyar, Mahajan, and Teneketzis's common-information approach](https://arxiv.org/abs/1209.1695) addresses control with shared and private histories. The contribution target is an explicit, independently checkable combination of resource feasibility and information interfaces for the research program. These modules neither recreate bounded concept generation nor prove a universal gradient of ethical coordination.

## Implementation audit: recurrent-inquiry model

Reviewed `experiments/recurrent-inquiry/model.py`, `test_model.py`, `PROTOCOL.md`, `analyze.py`, and the saved `results/analysis.json` on 5 October 2026. No substantive implementation error was found in the inspected comparisons. This section records independent code inspection and targeted exact calculations; it does not convert exploratory parameters into a preregistered experiment. No code or result file was edited.

**The stronger calendar comparator is implemented.** At horizon eight, `calendars` enumerates all 128 possible next-period readiness schedules with terminal readiness zero. Discarding terminal capacity is valid here because it has no salvage value and costs are nonnegative. Each schedule has a nonnegative source weight; the weights sum to one before any private observation. Its own time-belief occupancy variables conserve that source flow. Therefore the LP cannot select a calendar after learning the diagnostic result.

Within each schedule, occupancy may split between testing and not testing at the same available belief. This implements randomized, observation-adaptive diagnostics rather than one deterministic test policy per calendar. Readiness and upkeep/rebuilding expense remain fixed by that calendar. The pooled expected expenditure constraint applies across the complete lottery. Every included action separately obeys the per-period procurement cap; randomization cannot hide a branch that exceeds the cap. Bayes-optimal treatment can be eliminated analytically because it affects neither future need nor observations and has a separate available operating budget.

The eight saved expenditure-constrained solutions use their allowance to floating-point precision. Thus “equal expected inquiry expenditure” is accurate for these rows, although the implemented constraint is generally an upper bound and need not bind in another parameter setting. Pathwise spending remains unequal. The saved operating-loss advantages range from approximately .007655 to .083365 over eight periods; the comparator's additional randomization has already been allowed and does not erase them.

**Independent optimization check.** I recomputed two selected constrained values through the Lagrange dual

\[
\sup_{\eta\ge0}\left\{
\min_{\text{calendar, adaptive tests}}
\mathbb E[\text{operating loss}+\eta\,\text{inquiry cost}]
-\eta R\right\}.
\]

For each multiplier, the inner minimization used exhaustive calendar-specific Bellman solutions, a different calculation from occupancy-flow assembly. In saved grid row 2 (zero based: \(h=.05,m=.06,K=.08\)), the dual yielded 2.021340383856529 versus LP 2.021340384106725, a difference below \(2.6\times10^{-10}\). In row 4 (\(h=.15,m=.015,K=.08\)), it yielded 1.912002060456582 versus LP 1.912002060467712, a difference below \(1.2\times10^{-11}\). The unconstrained exhaustive Bellman minimum agreed with the corresponding LP within \(5\times10^{-16}\). These checks support the reported optimal comparator values; they are not independent validation of the physical assumptions.

**Information sets and the stale-model example.** The policy uses last successful diagnosis and its age, not the evaluator's hidden loss. Under state-independent diagnostic failure, an exogenous symmetric Markov process, and actions that do not alter that process, this pair is sufficient for current need. Upkeep decisions are allowed after the diagnostic, exactly as the protocol declares. The procurement cap covers inquiry; treatment expense is counted in the objective but supplied separately.

`evaluate` uses the true transition rate to propagate the distribution and score consequences, while its decisions and treatment choices use the planner's assumed rate. The stale illustration therefore compares an agent incorrectly assuming \(h=0\) with one supplied the true \(h=.1\), starting from a known negative. It does not model discovery of the changing transition law, endogenous dogmatism, or selection of a doctrine. The off-believed-path observation check appropriately raises an error rather than silently assigning a response; the particular saved stale path performs no tests, so that limitation does not invalidate its result. A general misspecification study would need policies specified on every observation that has positive probability in the real environment.

**Controls and communication scope.** Zero adaptive gaps for wholly unpredictable need, an uninformative diagnostic, and prohibitively expensive capacity are consistent with the implementation. Static need alone does not imply a zero gap: when a diagnostic can fail, the adaptive policy can stop maintaining capacity after the first success but preserve it after failure. An additional independent calculation with \(h=0\) and diagnostic success one gave adaptive total 1.68 and calendar total 1.6800000000000002, isolating that explanation.

The handoff calculation now pays a setup fee even when an established channel stays silent and correctly pools intentional silence with failed delivery. Opening the channel is chosen from the public cue before state-dependent disclosure, preventing setup itself from becoming an unpriced private signal. Its probabilities concern a past state; the known transition law then ages that evidence. The declared observation interface must continue to exclude an itemized private sending bill, since such a bill could reveal attempted publication despite failed delivery. This is a paid one-time communication comparison, not an integrated renewal model of archives or succession.
