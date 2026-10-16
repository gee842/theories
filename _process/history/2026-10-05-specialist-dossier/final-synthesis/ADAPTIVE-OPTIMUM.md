# An exact adaptive optimum under limited information and revisable requirements

Research development, 5 October 2026. This closes a specified controller-synthesis problem, not unrestricted alignment or causal discovery. It extends the [mechanistic dossier](../FOUNDATION.md) and [canonical representation](../OPTIMAL-FOUNDATION.md) with an implementable finite-horizon policy, paid learning, explicit amendment records, and a statistically qualified model-update rule.

## 1. The problem being solved

Fix a finite horizon H, finite action and actual-observation alphabets, and a finite library of candidate controlled models m ∈ M. Each model has a finite hidden state space X_m, a rational initial distribution, and rational joint kernels

\[
K_m(x',o\mid x,a).
\tag{A1}
\]

The observation packet o contains only information actually delivered to this controller. The latent model index remains fixed. A candidate can itself include changing physical modes, preferences, or rules in x; unmodeled drift is not covered by calling the index fixed. Disturbances and other actors must have their specified effects included in the kernels or an explicitly enlarged uncertainty class.

An observed history h determines the permitted action set A(h), the public specification version e(h), and a nonnegative integer charge c(h,a), paid before action a. Charges include the declared costs of experiments, observation processing, communication, amendment processing, maintenance, and action. Long actions are expanded into their actual stages when intermediate hazards or deadlines matter.

A(h) describes commands actually available through the interface. If whether an attempted command succeeds depends on hidden permission or capacity, refusal or failure belongs in the transition and observation law; the controller is not given the hidden availability bit for free.

Plural requirements are conjunctive predicates on a finite product of physical and monitoring states. Write G_e for the acceptable set at a stage and T_e for the acceptable terminal set. Monitors can track each party's burden, outstanding duties, authorized version transitions, elapsed response time, and delivered renewal events. A missed bounded renewal deadline enters a failing state. Thus indefinitely waiting or freezing the institution does not satisfy a renewal requirement. Justified withdrawal can be a separate acceptable terminal outcome if the contract explicitly permits it.

The update e(hao) is specified from the public record. Actual installed preferences and amendment events remain physical variables. The acceptance test distinguishes an actual amendment from conformity with the declared amendment procedure, including carried obligations. Procedure conformity does not prove that the procedure is ethically justified or that a reported consent signal was voluntary. Hidden coercion must remain an uncertain monitored fact if it matters.

This is a single controller with a declared information interface. It is not arbitrary decentralized synthesis. A central evaluator's additional information cannot be inserted into h.

## 2. Information states without a true-state oracle

Compute the unnormalized hidden-state weights using only the candidate tables and observed history:

\[
v_m^\emptyset(x)=\mu_m(x),\qquad
v_m^{hao}(x')=\sum_xv_m^h(x)K_m(x',o\mid x,a),
\qquad L_m(h)=\sum_xv_m^h(x).
\tag{A2}
\]

The action likelihood is omitted because the same controller, using the same actual history, chooses actions under every candidate. This is a controlled likelihood, not conditioning on a hidden-state-aware action oracle.

For a declared retained-model rule C(h), define

\[
B(h)=\{(m,x):m\in C(h),\ v_m^h(x)>0\}.
\tag{A3}
\]

Initially use all candidates with positive initial support. In the hard-guarantee version, C(h) consists of candidates with L_m(h)>0; no positive-likelihood model is statistically discarded. In the confidence version below, the retention rule is fixed in advance and may reject positive-likelihood models at an explicitly accepted error level.

All monitor states, including unobserved violations, belong in x when required. The controller tests whether *every* pair in B(h) is acceptable; it does not learn which pair is actual. For the hard version the equivalent support update is

\[
\Phi(B,a,o)=\{(m,x'):\exists(m,x)\in B, K_m(x',o\mid x,a)>0\}.
\tag{A4}
\]

Keeping m in the state prevents switching to a different model at each step. Every finite supported trace has a witness in one fixed candidate model. An expected-cost minimax problem with nonrectangular model uncertainty would need a different argument; the theorem below optimizes worst supported-path cost.

## 3. The exact resource optimum

Let O(h,a) contain observation packets with positive probability under some retained pair. Nonempty B(h) is **safe** when every pair satisfies G_e(h), and **terminally acceptable** when every pair also satisfies T_e(h). Let h' = hao, and retain in O⁺(h,a) only packets for which B(h') is nonempty.

In the hard version, O⁺=O. In the confidence version an empty updated set means certificate exhaustion. The controller follows a predeclared fallback then; the theorem makes no physical-success claim on that exceptional event. The fallback must itself be implementable and budget-limited, for example a specified zero-charge stop command. Such a command is not assumed to make the world safe. If fallback requires a reserve, include that reserve in the charged action cost or terminal budget test.

Define J_n(h), for n remaining actions, as follows. At a nonempty unsafe node it is ∞. At a safe terminal-depth node,

\[
J_0(h)=\begin{cases}0,&B(h)\subseteq T_{e(h)},\\\infty,&\text{otherwise.}\end{cases}
\tag{A5}
\]

At a safe nonterminal node,

\[
J_n(h)=\min_{a\in A(h)}\left[c(h,a)+
\max_{o\in O^+(h,a)}J_{n-1}(hao)\right].
\tag{A6}
\]

Use max ∅ = 0 at certificate-exhaustion-only branches and min ∅ = ∞. On other branches ordinary extended-nonnegative arithmetic applies. An early completed process can have an explicitly modeled zero-charge absorbing action so that the horizon means “by H.” There is no implicit free action for an unfinished duty.

**Theorem A1 — least operating budget and an actual-information controller.** In the hard version, J_H(∅) is the least initial operating budget for a policy that satisfies all prefix requirements and terminal requirements on every supported H-step trajectory of every candidate model. In the confidence version, it is the least budget among policies admitting the specified stepwise retention certificate: all retained pairs are acceptable at every nonempty reachable information node, terminal retained pairs satisfy T, and certificate-exhaustion branches use the stipulated fallback. For either version, if J_H is finite, choosing a minimizing action at each reached node gives a deterministic policy using only actual history. No randomized policy improves the worst-path optimum.

**Proof.** There are finitely many action-observation histories of depth at most H. The claim at depth zero is (A5). At a safe node, any admissible policy must choose an action a and pay its charge before observing the outcome. Every retained nonempty child requires at least its inductively established budget; a worst supported child therefore imposes the right-hand lower bound in (A6). Conversely, reserve that bound, pay c, and use an optimal child policy selected by the observation actually received. This satisfies every child certificate. Taking the minimum proves equality. A randomized action with positive probability must also meet the same worst-path requirement, so randomization cannot lower the minimum. ∎

The remaining balance is updated by b⁺=b−c(h,a). The proof establishes nonnegativity along all retained continuations and pays for an action even when its observation subsequently exhausts the certificate. Under the hard version, finite positive-support trajectories have positive probability; the pathwise conditions are consequently equivalent to probability-one satisfaction through the finite horizon under every candidate's supplied initial distribution.

This is a real optimum, but its scalar is an explicitly chosen operating resource, not an aggregate moral value. If several resources cannot be substituted, replace the scalar by a bounded vector budget. The recursion is then “there exists one affordable action such that every child budget lies in its viable set.” Finite lattice enumeration gives the exact viable set and its Pareto-minimal budget vectors, without collapsing protected requirements into one reward.

**Implementation boundary.** Rational tables, a finite history tree, and a computable retention rule make the construction effective. Full history may be retained, or an exact finite sufficient record can be used. The executor's update/storage costs must be included in c or reserved explicitly. Offline construction cost and table storage also require a supplied implementation budget; the value above minimizes operating charges within the declared interface and executor, not total complexity over all possible programs. The tree may be exponentially large. A finite mathematical description does not by itself promise affordable implementation.

## 4. Learning with an explicit confidence cost

Choose fixed positive rational mixture weights w_m summing to one, and define Q(h)=Σ_m w_mL_m(h). For L_m(h)>0 put

\[
E_m(h)=Q(h)/L_m(h).
\tag{A7}
\]

Given a rational error allowance 0<δ<1, retain

\[
C_\delta(h)=\{m:L_m(h)>0\text{ and }E_m(g)<1/\delta
\text{ for every prefix }g\preceq h\}.
\tag{A8}
\]

The running maximum makes removal irreversible within this episode. It does not use the true model. Hidden-state filtering in (A2) is essential; a support set alone does not contain the likelihood weights needed for this update.

**Lemma A2 — simultaneous-in-time true-model retention.** If one candidate m* supplies the actual controlled law, then, under any history-adapted choice of actions,

\[
P_{m^*}\{m^*\in C_\delta(H_t)\text{ for every }t\}\ge1-\delta.
\tag{A9}
\]

**Proof.** Under candidate m, E_m starts at one and is a nonnegative supermartingale on its positive-likelihood histories. Conditional on h and the chosen action, summing Q(hao)/L_m(hao) against the null's next-observation probabilities yields at most Q(h)/L_m(h): observations impossible under m can only remove mixture mass. Adaptive action selection causes no extra factor because it is common across hypotheses conditional on actual history. The nonnegative-supermartingale maximal inequality bounds threshold crossing by δ. A true candidate's likelihood is positive almost surely at every finite realized prefix. ∎

No union over candidate indices is needed for a guarantee uniform over which *one* candidate is true. Multiple independently asserted properties or model resets require their own error accounting.

**Theorem A3 — confidence-adaptive safety and its exact scope.** Run the minimizing retention-certificate controller of A1 using (A8). If J_H(∅) is finite, the declared budget is available, and the actual controlled law is a candidate, then the probability of any monitored prefix or terminal failure through H is at most δ.

**Proof.** On the event in (A9), the actual hidden pair belongs to B at every reached node, which never exhausts. The stepwise certificate therefore implies each physical requirement, the terminal requirement, and the operating-budget bound. Any violation is contained in the true-model-exclusion event. ∎

This is **not** sure safety and is **not** an optimality theorem over every δ-safe policy. A1 is exact among policies satisfying the fixed retention certificate. That certificate can be conservative, and the mixture/threshold design has not been optimized. It can still authorize actions previously blocked by a positive-likelihood alternative, at a quantified statistical risk. It does not guarantee that informative safe experiments exist or that a deadline can be met.

Model misspecification or unmodeled drift breaks (A9); the controller cannot certify the library's truth from the library alone. New candidates or changed data laws require a justified new confidence construction. A sequence of conditional-valid episode restarts with error allocations δ_j has total exclusion risk at most Σ_jδ_j by a union bound, including adaptive restart times when conditional validity at those times has been established. Simply resetting a counter or retaining an obsolete likelihood formula does not establish that validity.

## 5. Exact worked witness: the price and limit of diagnosis

There are two hidden fixed models, L and R, initially indistinguishable. The process is unfinished and safe. Actions are **left**, **right**, **probe**, and **wait**. Left completes safely in L but harms a protected party in R; right completes safely in R but harms a protected party in L. Each costs one. A perfect probe costs one, preserves safety, and produces the actual model's letter. Wait costs zero and preserves the unfinished state. Completion then has an absorbing zero-cost action. Both protected-party safety and completion by the deadline are required.

After a perfect probe, B is a singleton, and one matching completion action has value one. Initially each immediate completion has an unsafe child. At two remaining steps,

\[
J_2(\{L,R\})=1+\max\{J_1(\{L\}),J_1(\{R\})\}=2.
\tag{A10}
\]

The policy is probe, read the received letter, then choose the corresponding completion. Budget one or a one-step deadline is infeasible. Waiting cannot satisfy completion. Thus two is an attained lower bound, not merely the cost of one proposed policy. If the model were known initially, the optimum would be one in either world. Individually feasible worlds do not imply a feasible common first action under limited information.

Two exact variants expose the boundary:

| Probe specification | Hard safe completion within a finite deadline |
|---|---|
| Perfect, safe, one unit | Feasible exactly when at least two steps and two units are available |
| Positive probability of immediate harm in either retained model | Infeasible: the probe itself violates hard safety |
| Safe but noisy, with P_L(l)=3/4 and P_R(l)=1/4, independent across probes | Infeasible for every finite horizon: both models have positive likelihood after every finite signal sequence |

For the noisy case, every terminal history still requires incompatible completion actions. Randomization cannot make both wrong-action probabilities zero. Learning in probability does not remove this support-level obstruction before a finite deadline.

The confidence rule changes what can be certified on particular histories. With equal mixture weights and four l signals, L_L=81/256 and L_R=1/256. Hence E_R=41 and E_L=41/81. At δ=1/40, R is rejected and L retained, so a left completion can be certified from that history, after paying four probe units and one completion unit. Under R that misleading four-signal event has probability 1/256. This calculation is illustrative; it does not prove feasibility from the initial node at a five-step deadline. Mixed signal histories may retain both candidates. Requiring completion on every retained branch can still give J_5=∞.

Exact rational arithmetic verified these likelihood values. A separate finite recursion check gave perfect-probe values ∞, 2, 2 at horizons 1, 2, 3 and noisy-probe values ∞ at horizons 1 through 6. These checks support the worked calculation; the support argument establishes the claim for every finite horizon.

## 6. The impossibility and the safe-information criterion

**Proposition A4 — incompatible-action obstruction.** At an actual information node, suppose two retained possible worlds require disjoint sets of actions for satisfying the next unavoidable requirement. If no available, sufficiently funded action safely postpones that requirement while producing distinctions permitting compatible continuation, no hard-safe policy exists.

**Proof.** The controller must use the same action distribution at indistinguishable histories. Every action in its support fails in at least one possible world unless it enters a child with a feasible continuation. Under the premise no such action exists. This is exactly the empty finite-valued action set in (A6). ∎

The criterion is not “maximize information.” An informative experiment is useful only if its entire paid execution preserves the applicable conditions and every resulting information state admits the required continuation. A damaging experiment can have more information and no admissible value. Conversely, a policy may act safely without identifying the true model when all remaining models share a feasible action.

## 7. Representation and normative amendments

Let an old retained record q(h) merge h and g, while a new required query r satisfies r(h)≠r(g). There is no function f with r=f∘q: it would have to give two answers at the same argument. Adding a field name or adopting a finer canonical state cannot restore the lost distinction. A fresh observation may recover it only if the process still makes it observable, and its cost and hazard belong in the controller model.

Prepared amendments from a finite library can be handled by retaining the necessary monitors, records, and public version state from the beginning. A genuinely new query may require extending the causal model and initializing its new information set from the actual retained record. That set must include every compatible past, not the true past supplied by an analyst. If its robust value is infinite, an amendment is not currently implementable under the unchanged deadline, resource, and safety requirements.

The acceptance rules themselves remain explicit normative premises. Changing them can create feasibility, but that is not improvement under the old requirements. Preservation of standing, recorded dissent, procedure conformity, and surviving obligations can be required by monitors; whether these are sufficient for legitimate political revision is not proved by a controller theorem.

## 8. A limited infinite-horizon corollary

Suppose the hard version has a finite sufficient information configuration z containing its support set, public amendment version, all bounded deadline monitors, and bounded resource balances. Its update and permissible actions must be history-independent given z. Let Safe contain configurations whose entire hidden support is acceptable. Define

\[
W_0=\mathrm{Safe},\qquad
W_{k+1}=\{z\in W_k:\exists a\in A(z),\ \forall o\text{ supported},\ F(z,a,o)\in W_k\}.
\tag{A11}
\]

Finite iteration reaches W∞. A configuration belongs to W∞ exactly when an actual-information policy can maintain sure safety forever. Choosing a witnessing action gives a finite-memory policy. For the converse, every removed configuration has a finite removal rank; against any chosen action a supported continuation descends to a smaller rank and eventually violates safety.

Because bounded renewal deadlines are inside Safe, this corollary can require repeated actual renewal instead of mere nontermination. It does not express every unbounded liveness obligation, and an arbitrary likelihood-running-max state need not be finite. Neither repeating a finite-horizon plan nor repeatedly recomputing it proves perpetual viability without such a maintained invariant.

## 9. Mathematical lineage and remaining review questions

The components are established methods assembled for the reproduction-of-conditions problem: finite partially observed planning, support-based safety games, dynamic programming, likelihood-ratio testing, and explicit monitored specifications. The self-contained proofs above support their stated finite scope; no claim of a new general game-theoretic or statistical theorem is made.

For the boundary of information-state sufficiency, [Chatterjee and Doyen, *Partial-Observation Stochastic Games: How to Win when Belief Fails*](https://arxiv.org/abs/1107.2141), shows why simple belief-based claims do not extend indiscriminately to general stochastic reachability games. Our finite-history recursion and finite-deadline safety contract deliberately avoid that generalization. For time-uniform statistical validity, see [Howard et al., *Time-uniform Chernoff bounds via nonnegative supermartingales*](https://arxiv.org/abs/1808.03204) and [*Time-uniform, nonparametric, nonasymptotic confidence sequences*](https://arxiv.org/abs/1810.08240). The finite-model mixture proof here uses the underlying maximal-inequality principle, rather than asserting that a particular confidence-sequence formula identifies a misspecified world.

Review should verify:

- Are the candidate initial laws, observation packets, fixed-model tags, and monitor transitions the actual ones?
- Does the implementation retain and pay for the records and likelihood computations that its decisions require?
- Do the monitors preserve duties across version changes and require substantive renewal events rather than labels?
- Is any statistical pruning presented with its exclusion allowance and its fixed certificate comparison class?
- Can every claimed informative action be executed safely and on time in every retained world?
- Is a terminal withdrawal explicitly justified, rather than silently substituted for a requested capability?

The achieved result is a solved, finite, resource-accounted adaptation problem with an exact operating optimum and a precise learning-risk boundary. Its applicability still depends on defensible causal models, adequate observations, and explicit normative requirements.
