# Adversarial formal architecture for a theory of scientific change

Research continuation, 5 October 2026. Read the preceding `outputs/theory-of-scientific-change.md` and the earlier formal audit. This memo advances the integration problem rather than repeating the earlier information, prefix-funding, and memory results. Mathematical statements below are conditional reconstructions, not claims of mathematical novelty. No new historical claims are introduced.

## 1. Strongest central thesis and its empirical exposure

A defensible central thesis is:

> Scientific practices change through coupled processes of generating candidate distinctions, admitting questions, constructing and checking methods, revising appraisal rules, and maintaining or losing the capacities that make these operations possible. Present success can change these capacities in ways that predictably alter later discovery.

The last sentence gives the thesis its most useful testable exposure. A list of coupled variables alone has no empirical content. A theory must specify the transition mechanisms, demonstrate that their parameters can be measured without reading off the outcome to be explained, and outperform an explicitly weaker model on interventions or new trajectories.

The aim should be **mechanistic completeness within a declared domain**, not an unrestricted derivation of everything called science. For a finite laboratory task, completeness means that every modeled change—new question, representation, test, adoption, method spread, rule edit, capability loss or rebuilding—has an implemented generating rule, an information interface, and a cost. It does not mean that those rules explain their own ultimate origin or exhaust human scientific life.

The framework becomes vacuous if an arbitrary latent "capacity" can be added after every failure, if a standard change can redefine every adverse result as success, or if the world-transition kernel is freely refitted to each history. Its concrete models must prohibit such repairs unless they create a new, separately evaluated model version.

## 2. A minimal state architecture, with explanatory debts visible

Let the analyst's state be

Z_t=(W_t, A_t, D_t, G_t, Q_t, M_t, V_t, U_t, B_t, N_t).

Here W is the target world's state; A is installed capability and accessible actions; D retained evidence; G the representation/proposal grammar; Q candidate and admitted questions; M implemented methods; V appraisal and admission procedures; U aims or protected constraints; B liquid budget and liabilities; and N membership, communication, and authority relations. Each investigator sees an explicitly specified observation h_t of this state, not Z_t itself.

This is still a schema. To obtain an executable theory one must specify at least: proposal generation G,D→Q; admission V,Q,B→selected work; design and execution A,M,B→actions; world and observation consequences; evidence retention; method and rule revision; resource renewal; and propagation between people or institutions. Proposed arrows must sometimes be absent or weak in rival models.

Do not create a model with an omniscient selection step that chooses whichever proposal the analyst knows to be best. Likewise, an agent cannot update its standard from its "true error rate" unless error truth is available through an explicitly modeled channel. External evaluation is legitimate, but it belongs to the experimenter, not silently to the investigator.

A practical audit is to label each transition **generated**, **selected from supplied alternatives**, **learned from supplied feedback**, or **externally changed**. All four are useful model components; confusing them inflates what the model explains.

## 3. Proposition A: a robust search gate can block a useful representation

Let X_1,...,X_k be independent fair bits, k≥2, and

Y=X_1 XOR ... XOR X_k XOR E,

where E is independent Bernoulli(epsilon), 0≤epsilon<1/2. The learner may use any Boolean predictor of a retained subset of features. Its declared objective is prediction risk plus lambda times the number of retained features. It begins with a constant predictor and accepts a one-feature extension only if estimated penalized risk strictly improves. It does not jump across rejected extensions.

**Claim.** In the exact-risk version, the learner never leaves the empty subset, although a k-feature predictor has lower penalized risk whenever

k lambda < 1/2-epsilon.

**Proof.** Conditional on any proper subset of the k bits, at least one unseen fair bit makes the parity fair, so every deterministic predictor based on that subset has risk 1/2. The empty representation has score 1/2; every singleton has score 1/2+lambda when lambda>0. With lambda=0 the strict-improvement rule still rejects the tie. Full parity has score epsilon+k lambda. Therefore all first steps fail while the complete combination can win.

**Robust finite-evidence version.** Suppose the absolute risk-estimation error is at most delta simultaneously for the baseline and every candidate considered. If lambda>2 delta, every singleton remains worse in estimated penalized risk. If additionally 1/2-epsilon-k lambda>2 delta, an available full-parity candidate remains better. Thus the result is not dependent on exact equality or numerical tie breaking. This is a conditional accuracy event; its probability requires a specified sampling and estimation model. If candidates are fitted using the same sample, a pointwise bound for one fixed predictor is insufficient; one needs a bound accounting for the whole finite search family or suitable independent evaluation.

This proposition generalizes the earlier two-feature illustration while identifying the actual mechanism: a constrained proposal/admission path. It does not say that the data contain no information, that all greedy procedures fail, or that human science maximizes predictive score. Permitting occasional multi-feature proposals, zero-cost neutral moves, or a different grammar can remove the trap. An empirical model must measure the gate rather than infer it only from failure.

The result also exposes dependence on the objective. An intervention-oriented question, mechanistic explanation, compression rule, or exploratory diversity criterion can value a proposed distinction before it improves prediction. Hence predictive lockout is a local mechanism within a broader theory, not the essence of scientific change.

## 4. Proposition B: local effective testability changes with feasible capability

For a declared question q, identify two contrasting packages theta_0,theta_1, a deadline d, liquid budget B, and admissible protocol class Pi(A,B,d). Protocols include observation, intervention, computation, stopping, and record use. Let P_i^pi be the resulting complete accessible-transcript law under theta_i.

Call q **locally effectively testable at (alpha,beta)** if there exists pi in Pi and a decision rule phi such that

E_0 phi ≤ alpha, and E_1(1-phi) ≤ beta.

This concerns achieving a declared error pair in the present feasible setting. It differs from logical falsifiability, asymptotic identification, and whether an investigator has conceived or admitted q. Using a supremum of total variation gives useful impossibility bounds, but is not by itself an exact characterization of every specified error pair.

**Monotonicity.** If Pi(A_0,B,d) is contained in Pi(A_1,B,d), the set of locally effectively testable questions cannot shrink. This requires that new capability leaves old protocols feasible and can be ignored without hidden cost. An expensive maintenance obligation, changed target, loss of privacy permission, or destructive intervention can break that inclusion.

**Strictness witness.** Suppose all transcripts under A_0 have the same law in theta_0 and theta_1, but A_1 additionally permits a priced, deadline-feasible observation Z with Z=0 in theta_0 and Z=1 in theta_1. Under A_0 no pair alpha+beta<1 is achievable; under A_1 both errors can be zero. This is a nontrivial change in effective testability, not just a change in willingness to investigate. If A_0 has an equivalent substitute channel, strictness disappears.

For empirical use, measure capability independently: executable instrument functions, calibration status, retained record schema, trained operators, time to procure or restore access, available permissions, and actual prices. Do not define capacity as "whatever would have prevented this observed failure." A separate benchmark can check whether an action is executable without using the scientific outcome whose explanation is at issue.

Finally, having a feasible protocol is not choosing it. A full explanatory account must join this proposition to a generated question and an implemented selection rule. Otherwise the theory establishes opportunity, not scientific behavior.

## 5. Proposition C: maintenance and reconstruction create exact hysteresis

Let C_t in {0,1} record whether a diagnostic capability is installed. Each period brings usable funding r_t. Maintenance costs m>0, reconstruction costs k>m. Funding cannot be banked or borrowed against future periods; there is no substitute or external restoration. A stipulated policy maintains whenever maintenance is affordable and reconstructs whenever reconstruction is affordable. Then

C_(t+1)=1 if [C_t=1 and r_t≥m] or [C_t=0 and r_t≥k],

and C_(t+1)=0 otherwise.

**Theorem.** For constant r with m≤r<k, states 0 and 1 are both absorbing. There are at least two stationary distributions, concentrated respectively on 0 and 1; long-run capability depends on initial condition. Increasing r from below m reconstructs capability only on reaching k. Decreasing r from above k loses capability only below m. Thus upward and downward transition thresholds differ by k-m.

**Proof.** In state 1 the first affordability condition holds; in state 0 neither condition holds. This establishes both absorbing states and their stationary point masses. The two threshold statements follow by applying the appropriate affordability inequality along each path.

**Inquiry consequence.** Combine this relay with Proposition B's strictness witness. During a later inquiry episode, C=1 permits an affordable informative assay within the deadline, while C=0 cannot reconstruct in time. The two histories then have different achievable error guarantees despite identical current funding flows. For example, m=1,k=3,r=2 sustains an installed capability but cannot rebuild it. A temporary decline below 1 can therefore leave a lasting diagnostic deficit after funding returns to 2.

There is a precise state caveat: the histories have identical **liquid funding and potentially identical incumbent performance**, not identical complete structural state. Installed capability differs and can be measured. If R in S already includes durable capital and skills, it is false to call the complete current R identical. History matters to a compressed present description; this model does not violate the Markov property once the relevant state is included.

The nonbanking, no-credit, no-substitute, and no-restoration assumptions do real work. If an inactive institution can accumulate unspent r>0 indefinitely, it can eventually afford k. Then permanent trapping disappears, though delay or a finite deadline can still matter. A historical application must verify the actual funding and rebuilding constraints rather than smuggling irreversibility into the model.

**Rare restoration extension.** At fixed intermediate funding, replace strict absorption by a per-period restoration probability rho>0 from state 0 and a loss probability eta>0 from state 1, with 0<rho,eta<1. The transition matrix is

[[1-rho,rho],[eta,1-eta]].

Its unique stationary capability probability is rho/(rho+eta), derived by balancing the two probability flows. Starting in state 0, the expected wait to first restoration is 1/rho and restoration by T periods has probability 1-(1-rho)^T. There is no permanent absorbing trap. When rho is very small, long-lived deficits are **metastability or finite-horizon inaccessibility**, not strict nonergodicity. These distinctions should survive into any user-facing claim.

The result is not evidence that science always exhibits hysteresis. It supplies a minimal mechanism, independently measurable cost thresholds, an observable funding-cycle prediction, and clear interventions—startup grants, credit, transferable skills, substitutes—that can remove or narrow the loop.

## 6. Learning and propagation are causally different even when shares match

Observed method prevalence cannot by itself identify its mechanism. Let x(t) be the proportion using a method. Differential expansion or replacement with advantage s>0 can produce the supplied law

x_dot=s x(1-x).

The same trajectory arises in a fixed membership population with no differential expansion when nonusers switch at per-person rate a(t)=s x(t), with no reverse switching, because x_dot=a(t)(1-x). One story concerns propagation through expansion; the other concerns within-person adoption. Aggregate method shares alone do not distinguish them.

The labels are operational here. Social imitation, strategic compliance, and learning from evidence can all cause within-person switches but should not automatically be equated. Useful records include stable actor identities, entry and exit, resource shares, elicited beliefs, observed methods, evidence received, and changes in rewards. An agent may change its published method without changing its belief; recording only publications hides that difference.

The same caution applies to timescales. Belief updating, experiment execution, standard revision, training, instrument depreciation, and institutional replacement have different measured delays. The architecture does not prove a universal ordering. A fast-learning/slow-institution approximation requires observed separation of timescales and may fail near deadlines, resource collapse, or large feedback changes. A model should use explicit clocks or event hazards, not attribute all slow change to irrational resistance.

## 7. Semantics, changing observables, aims, and self-application

**Semantics.** A novel token or partition is not automatically a new scientific concept. Operationally, the model can show that it permits new distinctions, supports reliable predictions or interventions, links measurements, or compresses a declared task. Its referential meaning and relation to earlier concepts require correspondence rules. A claimed improvement is especially suspect when the new representation silently changes which object or population is being evaluated.

**New observables and closure.** A fixed feature table models recombination, not invention of a sensor. Instrument construction can instead be modeled as action sequences that alter later observation channels, with unknown consequences learned through use. A generative programming language may permit unbounded constructions. Nevertheless the analyst has supplied the transition and interpretation rules at some level. This is a scope boundary, not a proof that modeling novelty is impossible: novelty to an investigator need not be novelty outside every analyst-defined possibility space.

**Aim change.** A model can explain why a population adopts a goal through negotiation, selection, practical pressure, or learning about its consequences. It does not infer that the goal is ethically legitimate from its prevalence or survival. Nor must every local comparison use one immutable scalar. Constraints and partial orderings can warrant some changes while leaving real tradeoffs unresolved. An explanatory mechanism still needs a rule for how the particular agents actually act when preferences conflict.

**Reflexive checking.** A finite process can evaluate a rule while provisionally holding some checks fixed, then later inspect those checks. It need not complete an infinite prior certification chain. But common corruption of a method and its checker can make apparent agreement uninformative; changing standards after every failure can erase adverse outcomes. Versioned targets, prospectively recorded claims, and independently informative checks address specified failure routes, not every possible error. The theory receives no immunity from this requirement.

## 8. Minimal model comparison and empirical identification

Use three nested models of the same restricted task:

- F: capability is fixed and current observations determine learning.
- E: capability may decline exogenously at measured rates, independently of the community's allocation decisions.
- C: present allocation, retention, and reward choices alter maintenance and reconstruction, which alter later accessible tests.

All models should share the candidate grammar and as many other parameters as possible. Fit training episodes, freeze parameters, then predict randomized intervention episodes. C must earn its extra degrees of freedom by predicting an interaction or trajectory that F and E miss without post-hoc retuning.

A minimal experiment independently varies (i) a reward rule favoring short-term output, (ii) protected maintenance or restoration access, and (iii) whether a later task requires the capability. Include stable or substitute-channel tasks. Record capability before the later task, test executability, actual funding and expense, candidate generation, admission, diagnostic error, and discovery delay. A short-term-success metric must be defined independently of the later evaluation target so their potential divergence is visible rather than built into the outcome label.

The specific prediction is that reward-driven withdrawal produces a later deficit especially when it removes a capability uniquely needed for the later distinction, and that timely protected access attenuates this deficit. A temporary funding cycle should yield the distinct maintenance/reconstruction thresholds only if the relay assumptions hold. Examine aggregate costs: protection may improve later diagnosis yet lose overall under a short horizon or expensive maintenance.

Randomization identifies effects of the assigned interventions in this task. It does not automatically identify the capability-mediated path. Reward changes may also alter effort, risk tolerance, staffing, or reporting. To isolate mediation, directly randomize access/restoration where feasible, or state and defend the extra assumptions needed for observational mediation. Measure the mediator independently of the outcome. A restored device with no trained operator is not the same intervention as restoring effective access.

Evidence against C includes failure to predict the pre-task capacity change, absence of the interaction under its specified conditions, successful substitution omitted by the theory, incorrect reconstruction-cost estimates, or F/E achieving equal predictive performance with fewer assumptions. If randomized reward changes do not affect allocation as posited, the proposed social mechanism fails even though the mathematical relay remains correct.

A simulation establishes model implications and can expose accounting or logic errors. Human task evidence tests limited behavioral mechanisms. Institutional data require independent measures, case-selection rules, and causal identification appropriate to their setting. These are different evidential achievements; none should be relabeled as a full empirical theory on the strength of the others.

## 9. Recommended claim boundary

The constructive result is a **conditional theory architecture with independently testable modules**. It can join representation search, practical testability, hysteresis, rule revision, and propagation without reducing all change to prediction or declaring a single fixed meta-standard. The new empirical claim should concern whether endogenous changes in access explain future inquiry beyond simpler alternatives.

The framework is too broad to test as a single sentence. Its restricted mechanisms need not be. The next publication-quality claim, if eventually warranted, should identify a measured gate, a priced capability, a predicted transition, a rival model, and an intervention that distinguishes them.
