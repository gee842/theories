# Plural correction: design and adversarial review

5 October 2026. Independent design review. This memo proposes checks and a deliberately constructed analytic example; it does not report results of the forthcoming plural-correction implementation. The physical and observation model is the existing finite recoverable-inquiry belief DAG. No root implementation or research record was edited.

## The useful change, and what it leaves supplied

Replace the earlier scalar objective with a question of simultaneous feasibility. For a policy π, retain the consequence vector

\[
v(\pi)=(F(\pi),H(\pi),C(\pi)),
\]

where F is terminal collapse probability, H is expected cumulative target-absent repair burden plus .05 per diagnostic, and C is expected cumulative expenditure minus actual output. All three are quantities to bound above. **C now excludes both terminal stock salvage and the former scalar collapse penalty.** Reusing the earlier `cost` metric would silently reintroduce the earlier preferences; use `expense - output` directly. Report terminal stock separately if needed.

“Service users,” “intervention subjects,” and “resource contributors” can name three symbolic roles associated with these requirements. The model contains no individual identities, incidence of payments, distribution of service, consent reports, or ownership of output. The roles need not be disjoint. Consequently it tests compatibility of supplied aggregate requirements, not interpersonal justice or actual constituency representation. The existing H also embeds a supplied internal exchange rate between diagnostics and target-absent interventions; give both components alongside its total. A target-absent repair can restore stock, so this remains a burden measure rather than a false-action count.

Joint feasibility does not require an agreed scalar ranking across F, H, and C. It does require acceptance of these particular quantities, thresholds, model, horizon, and admissible lotteries. An infeasibility certificate cannot determine which requirement ought to be relaxed. If an implementation minimizes C subject to the other bounds to select a witness, call that an explicit secondary selection rule rather than a discovered common utility. A zero-objective feasibility LP is sufficient to exhibit one policy; an arbitrary feasible solution is not automatically Pareto efficient.

This is an application of established constrained-control and multi-objective verification machinery. Closest primary prior art includes [Huang, Li, and Guo (2014), finite-horizon constrained control via absorbing-MDP occupancy measures](https://doi.org/10.1016/j.orl.2013.12.009), [Poupart et al. (2015), constrained POMDP linear programming](https://cs.uwaterloo.ca/~ppoupart/publications/constrained-pomdps/poupart-aaai15-calp.pdf), and [Etessami et al. (2008), multi-objective MDP model checking](https://arxiv.org/abs/0810.5728). The latter addresses broader temporal properties, for which additional memory may be needed; that should not be confused with this finite augmented-state, additive-expectation problem. The contribution here can be a transparent controlled demonstration of plural feasibility and permission restrictions, not invention of vector optimization or a universal coordination theorem.

## Preserve one underlying DAG

Construct the unrestricted adaptive DAG once, including every original prefix-affordable action and its fixed transitions. Define all permission regimes as filters on those same action columns. Do not change the transition law, sensor, cash, initial state, information, horizon, or burden weights between regimes. Every retained action should preserve byte-for-byte or numerical identity of its stage consequences and transition probabilities.

The baseline information state remains `(remaining time, stock, cash, readiness, exact fault belief)`. The policy receives all passive stock/output evidence and its own actions. It never receives the hidden fault or retrospective truth about a target-absent intervention. Filtering actions must not alter Bayesian conditioning on retained observation branches.

Three restrictions have different meanings:

* **No diagnostic:** remove only actions with a paid diagnostic. Passive inference, direct repair, rebuilding, and apparatus support remain admissible. Support may become useless, but the optimizer should discover that.
* **No repair:** remove actions prescribing repair on any positive-probability observation branch. Diagnostics and support remain available. Keeping useless actions is harmless and makes the pure-removal comparison auditable.
* **Observable repair permission:** specify a rule based only on the available stock, cash, readiness, time, and **posterior immediately before the prescribed repair**. For a test action, evaluate the permission separately on each sensor-result branch. Removing all test prescriptions because the pre-test belief fails a threshold would confound the permission rule with denial of evidence-responsive action.

An observation-contingent prescription can be represented as one pre-test action, provided the chosen prescription is remembered until its sensor result and the allowed branches all satisfy the declared rule. Restricting a prescription on a genuinely zero-probability result is unnecessary; it must not create artifacts when priors are zero or one. The no-test/no-repair “drop and wait” action supplies a feasible fallback in every live state, so pure restrictions need not introduce artificial dead ends.

Rights language needs a scope sentence. These are externally supplied permission rules, not an implementation of consent negotiation, institutional enforcement, legitimacy, or changing authority. Their consequences can be evaluated without treating the action-expanding regime as ethically preferable. By set inclusion, removing actions cannot enlarge the attainable consequence set; this is a mathematical consistency property, not an empirical finding that fewer rights improve welfare.

## A minimal analytic example with a sharp certificate

Keep every physical parameter unchanged, but use horizon one and initial state x=1, b=8, ready=1, and fault probability p=1/2. These supplied conditions deliberately make depleted-stock intervention consequential. This is an illustrative construction, not a preregistered empirical discovery.

Consider retaining readiness, paying for a diagnostic, repairing only after a positive result, and otherwise doing nothing. A positive result has probability 1/2 and posterior fault probability .9; a negative result has probability 1/2 and posterior .1. Both repair branches are prefix-affordable: upkeep 1 + diagnostic 2 + possible repair 3 ≤ 8.

After repair, next stock is 3 with probability .9 and 1 with probability .1, hence expected output 5.6 and no collapse. Without repair after a negative result, damage probability is .17; next stock is 2 with probability .83 and zero with probability .17. Therefore

\[
F=\tfrac12(.17)=.085,\qquad
H=.05+\tfrac12(.1)=.10,
\]

\[
\operatorname{expense}=1+2+\tfrac12(3)=4.5,
\quad \operatorname{output}=\tfrac12(5.6)+\tfrac12(3.32)=4.46,
\quad C=.04.
\]

The bounds `(F ≤ .10, H ≤ .10, C ≤ .05)` are thus jointly feasible with the unrestricted action set.

Under no diagnostic, let r be the probability of repairing. There is no new observation before this one repair decision, so all randomized admissible policies satisfy

\[
F=.45(1-r),\qquad H=.5r,
\qquad F+.9H=.45.
\]

Support without testing can change C but cannot change this F/H identity. Since the proposed upper bounds require F+.9H ≤ .19, they are impossible under this restriction. Equivalently, H≤.10 forces F≥.36. This is an independent analytic separating certificate with weights `(1,.9,0)`, rather than an assertion based only on solver status.

A repair permission threshold `posterior ≥ .75` allows the positive-result repair and leaves the displayed witness feasible. Threshold `.95` forbids direct repair at prior .5 and both tested repair branches at posterior .9 or .1; every permitted one-round policy then has F=.45. The second rule destroys feasibility in this particular supplied situation. The calculation does not prove that .75 is a legitimate right, .95 an illegitimate one, or that diagnostic permission is universally necessary. It identifies precisely which available conditional action matters for these bounds.

Retain an easier initial state or looser-bound control in which no diagnostic is needed. Otherwise a constructed rights example could be mistaken for a universal requirement for testing. Likewise retain parameter/bound tuples where the unrestricted regime is infeasible; more permission cannot overcome every material or normative incompatibility.

## Occupancy LP and implementable policies

Let y(s,a) be the expected occupancy of an action at a live information state. Terminal states can have one dummy terminating action with no successors. Every state includes remaining time, so the graph is acyclic; early collapse terminates once rather than accumulating the collapse penalty repeatedly. With μ concentrated at the initial state, use

\[
\sum_a y(s,a)-\sum_{z,a}P(s\mid z,a)y(z,a)=\mu(s),
\qquad y(s,a)\ge0.
\]

Set terminal dummy F cost to one exactly for collapsed terminals, terminal C and H to zero, and live stage C/H to the declared values. The three bounds are linear functions of y. Equivalent terminal-inflow formulations are fine, but test against double counting and omitted early collapse.

An occupancy solution gives the randomized Markov rule

\[
\pi(a\mid s)=\frac{y(s,a)}{\sum_b y(s,b)}
\]

at positive-mass states. At zero-mass states, choose any permitted fallback action. Floating-point “almost zero” handling should not erase a small, economically important branch; report its tolerance and the independently recomputed discrepancy. This Markovization preserves the required additive expected outcomes because the finite belief state is sufficient under the specified known model. It does not preserve every correlation or every pathwise property of a history-dependent policy. In particular, hard individual harm caps or conditional subgroup guarantees may require additional state variables and constraints.

A local randomized policy is implementable using public model state and fresh policy randomness. Sampling an entire deterministic policy once at the start is another admissible approach, but merely mixing a few policies found by an arbitrary weight grid need not recover the full attainable set. It is important that a policy lottery is acceptable to the intended interpretation: satisfying expected burden across lotteries does not give each realized subject the same protection. Any claim of a pathwise right must instead be enforced by the action filter on every permitted branch.

## Certificates and verification requirements

For finite compact attainable set V under an action regime, incompatibility with upper-bound vector b admits nonnegative separating weights w such that

\[
L(w):=\min_\pi w\cdot v(\pi)>w\cdot b.
\]

These weights are a mathematical proof of incompatibility, not moral exchange rates or a common utility. Obtain them from a correctly signed LP dual or a phase-I feasibility problem, then independently compute L(w) by ordinary backward dynamic programming on the retained action DAG. If using a normalized common-slack phase-I LP, fix meaningful metric scales first: F, H, and currency are different units. Positive scaling changes the reported separator but not feasibility. Report the actual positive separation margin and numerical residual, not just “infeasible” from the solver.

The minimal checks are:

1. Independently reproduce the one-round witness and no-diagnostic identity above with elementary probabilities; test against both LP and policy evaluation.
2. At every state/action, verify normalized nonnegative transition probabilities, branchwise prefix finance, and the unchanged cash conservation identity. Confirm no hidden-state access enters either policy keys or permission filters.
3. Recover the policy from occupancy and propagate its state/action flow forward, separately from the LP matrix construction. Check terminal total probability one, flow residuals, permission violations zero, and all three metrics matching LP values.
4. Evaluate the recovered randomized policy backward as an additional independent route. For a small horizon, enumerate deterministic policies when tractable and compare their convex hull or scalar extrema with the LP.
5. Verify that each restricted attainable set is contained in the unrestricted set through pure column removal. Recheck an unrestricted witness after filtering: if it uses no removed action on a positive-probability path, it must remain feasible with identical outcomes.
6. For every infeasibility assertion, save nonnegative weights, threshold-weighted value, independently solved minimum weighted value, and a positive gap exceeding numerical error. A time limit or optimization failure is not an infeasibility certificate.
7. Report feasibility under modestly relaxed and tightened bounds, including boundary cases. Do not classify points separated only by the solver tolerance as robust substantive differences.

## What a restriction contrast can identify

If an unrestricted witness satisfies the bounds and a pure permission restriction has a valid infeasibility certificate, then the **specified restriction is sufficient to remove feasibility in this model and initial state**. It need not be the only removal with that effect. An action can serve several functions: a diagnostic consumes resources, adds burden, and changes evidence; repair changes both productive state and future beliefs. A no-diagnostic contrast therefore isolates access to that action, not a universal “informational cause” independent of costs and dynamics.

If the unrestricted regime is infeasible, the reason is a joint incompatibility among supplied dynamics, information, liquidity, horizon, and requirements. Calling that result purely “physical impossibility” is unwarranted. A separate perfect-information comparison can bound how much the information restriction matters, but changes the information model and must be explicitly labeled. Resource injections, free diagnostics, relaxed harm bounds, or delayed deadlines similarly answer different counterfactuals. Several changes may each restore feasibility, and their effects can interact; a unique physical/informational/authority decomposition is not available from the three action-removal contrasts alone.

This cycle can provide a rigorous distinction between an attainable shared constraint set, a conditional barrier imposed by a permission rule, and a certified incompatibility left even with the available action set. It cannot derive the requirements, settle disagreement about lotteries, or infer who should decide which constraint changes.

## Implementation audit and independent tests

5 October 2026. Reviewed `experiments/plural-correction/model.py` against its immutable copied upstream dynamics and created the specifically assigned `test_model.py`. No root model, analysis, or protocol file was edited. All nine tests pass under `/private/tmp/meta-attractor-plot-env/bin/python`.

The implementation constructs restrictions by removing original action columns on the same belief DAG. Its `repair_posterior_floor` is explicitly an **opening-belief permission rule** that can deny contingent response before evidence arrives; its separate `response_posterior_floor` applies after the actual diagnostic evidence. These differ intentionally. In the analytic example, an opening threshold .75 removes feasibility, while a response threshold .75 preserves the positive-result repair witness. Calling both simply “the same posterior threshold” would conceal the material timing difference.

Terminal collapse enters the occupancy consequence column through the probability of an immediately terminal successor, so early absorbing collapse is counted exactly once. Terminal stock salvage and the earlier weighted collapse penalty are absent from the three-vector; changing both scalar coefficients by orders of magnitude leaves the new flow and metric arrays identical. The raw physical model still retains those older fields, but they do not leak into this optimization.

The phase-I variable is unrestricted in sign. It minimizes the largest normalized bound violation, so a negative value reports strict simultaneous slack rather than an error. The three normalized dual weights sum to one; dividing by the chosen scales produces the raw separating weights. Backward `support` recomputes their minimum weighted attainable consequence independently of the LP flow construction. This makes positive separation a substantive certificate rather than a solver status. For an infeasible request, the displayed phase-I consequences belong to a policy minimizing normalized violation; they must not be described as a witness satisfying the original bounds.

The first reviewed implementation crashed when the initial state was already terminal, including initial stock zero or horizon zero. This was reported immediately. The root added analytical terminal-only handling, and the final tests verify its support values, feasibility and separation certificates, zero-action policy, forward evaluation, and least-burden result. The known boundary defect is resolved.

The independent test calculations include:

* Direct latent fault, sensor, and damage enumeration for thirty one-round initial-condition/permission combinations. This code does not call the model's diagnostic, production, or action-DAG builders to generate the comparison outcomes. Every action's F/H/C vector agrees, including prefix-poor states, supplied beliefs zero and one, and rebuilding without immediate testability.
* The supplied analytic policy `(F,H,C)=(.085,.10,.04)` and no-diagnostic identity `F+.9H=.45`. The latter gives separation `.45−(.10+.9×.10)=.26` with unnormalized weights `(1,.9,0)` independently of C.
* Infeasibility weights produced by the LP, checked against the independent minimum over latent-enumerated one-round actions. Opening-threshold, excessive response-threshold, no-diagnostic, and no-repair certificates all have positive margins.
* Normalized occupancies propagated **forward** under the extracted randomized policy, then compared with the LP vector and the implementation's backward evaluator on a three-round DAG. The independently recovered action occupancies, terminal probability one, and cash conservation all agree. The test deliberately mixes two occupancy solutions to exercise randomized policies.
* Exact submatrix identity under action removal, plus support-function monotonicity. An unchanged state/action retains identical probabilities and consequences across permission regimes.
* Perfect-sensor corner cases with prior zero or one: impossible sensor outcomes produce no repair branch; no hidden fault label appears in the public policy state. The ordinary sensor remains noisy and incurs the original pre-repair target-absence burden.
* Initial cash two/eight crossed with repair permission absent/present, holding stock one and prior one-half fixed. Only cash eight plus repair permission can satisfy the strict analytic bounds. All four cases become feasible under the displayed looser bounds. This demonstrates conditional complementarity, not a unique attribution of the failure to money or authority.

These checks validate the finite implemented calculations and information interface. They do not establish empirical calibration, interpersonal incidence of outcomes, or legitimacy of any supplied permission rule. No outstanding substantive implementation defect was found in this pass.
