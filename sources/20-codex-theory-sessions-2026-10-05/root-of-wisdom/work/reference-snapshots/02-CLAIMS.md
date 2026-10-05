# Claim register for continued becoming

This register separates mathematical results from definitions, empirical hypotheses, and commitments. Entries can be revised with an explanation in the [research log](RESEARCH-LOG.md). “Derived” means established under the stated assumptions, not original, empirically validated, or universal without qualification.

## U01 Cumulative renewal constraint

**Status:** exact balance and necessary condition. For an absolutely continuous stock E with independently defined production and inputs R, losses L, and a fixed functional floor Emin, E(T)=E(0)+integral(R-L). Staying above the floor requires cumulative deficit at every time to be no greater than E(0)-Emin. A persistent deficit of at least epsilon exhausts this margin within margin/epsilon.

**Scope and failure conditions:** an inventory or a defensible functional stock; compatible units; all relevant inputs included; the chosen function still depends on this stock. A changing threshold, substitution, interrupted activity, or a different boundary requires a revised application. Long-run average balance alone is insufficient to prevent intermediate failure. This is established accounting, not a new conservation law for knowledge or authority.

## U02 Relative selection cannot certify absolute viability

**Status:** exact identification limit over the pure-selection model class. Transform n_i to a(t)n_i for a positive differentiable a and r_i to r_i+d(log a)/dt. Shares and relative growth rates are unchanged while total abundance changes. Share-only procedures therefore cannot universally certify absolute viability over this class.

**Scope and failure conditions:** this compares compatible models or trajectories, not automatically two solutions of one unchanged ecological model. Additional causal assumptions or observations can break the ambiguity. Source: [integrated foundation](../../../sources/15-codex-theory-conversations/2026-10-04-selection-and-generative-conditions.md) and the strengthened transformation statement in the [first continuation snapshot](../../../sources/15-codex-theory-conversations/2026-10-04-universal-constraints-and-maintained-correction.md).

## U03 Selection and renewal can move in opposite directions

**Status:** derived conditional result and checked illustration. In the foundation's model, costly maintenance loses under selection and indispensable support collapses; favorable selection can also coexist with collapse from depleted initial stocks. A stable positive maintenance equilibrium exists under a derived parameter threshold.

**Scope:** the stated two-type model, with fixed incentives and no alternative support production. [Proof and assumptions](../../../sources/15-codex-theory-conversations/2026-10-04-selection-and-generative-conditions.md); [numeric checks](regeneration-model-checks.json). These are not predictions about every competitive system.

## U04 Renewal and correction must be feasible in time

**Status:** derived necessary condition, with a checked restricted example. A reserve cannot cover more cumulative unavoidable loss than it contains. If effective correction needs time to detect, decide, mobilize, and act, the actual loss before correction must fit inside that reserve. Overlapping stages must not be double-counted.

**Evidence and scope:** the [observation memo](observability-and-correction.md) proves the loss lower-bound impossibility certificate and distinguishes it from an upper-bound policy certificate. A two-fault model has exact guarantee criterion diagnostic time plus repair latency no greater than reserve divided by deficit. [Backward-recursion verification](observability-checks.json) confirms five timing cases. Its equivalence is specific to that repair architecture; the general reserve inequality is only necessary.

## U05 Indistinguishable states can require incompatible interventions

**Status:** exact finite-model result in established partial-observation safety theory. An empty intersection of optimistic full-information safe first-action sets rules out an observation-based guarantee. A backward recursion on information sets is necessary and sufficient for finite-horizon safety under the stated finite model.

**Evidence and limits:** [proofs and references](observability-and-correction.md); [reproducible checks](verify_observability.py). A verified counterexample shows that nonempty first-action overlap is insufficient when later observations leave another conflict unresolved. Randomization cannot restore a probability-one guarantee here, but can affect other objectives. A failed guarantee does not mean every trajectory fails.

## U06 Corrective capacity needs maintained conditions

**Status:** derived and independently reviewed conditional model result. The paid-renewal model has decaying support and corrective capacity; support expenditure renews the corrector, which enables support replenishment. Below its threshold, all trajectories approach extinction. Above it, a stable positive equilibrium coexists with stable extinction. A protected support floor places an additional upper bound on fixed renewal effort.

**Evidence:** [mathematical memo](endogenous-renewal-math.md), [calculation](verify_endogenous_renewal.py), [results](endogenous-renewal-checks.json). Equilibrium residuals are below 9e-16 and maximum state discrepancies under tolerance refinement below 1.5e-9.

**Limits:** fixed allocation policy; declared external feedstock; unverified functional form; equilibrium existence does not prove protected transients or reachability from depleted initial states. Selection over the maintenance rule is not yet modeled. No originality claim.

## U07 Local growth at depletion does not characterize all viable regimes

**Status:** derived counterexample within the paid-renewal model. Extinction is locally stable for every positive parameter choice, while sufficiently strong joint-input renewal permits a stable positive state. Thus the linear dynamics at extinction alone cannot determine whether a functioning positive regime exists elsewhere.

**Implication and scope:** persistence, bootstrapping, recovery, and protected operation are separate questions. This is a familiar nonlinear threshold phenomenon, not a new universal reproduction number. [Details](endogenous-renewal-math.md).

## U08 Competing transmission channels can destabilize renewal

**Status:** derived conditional theorem with independent proof review. In a two-practice extension of the paid-renewal model, gross capacity production inherits the higher-effort practice while copying of immediate expenditure savings favors lower effort. The exact share equation is xdot=(eta-kappa)E(uH-uL)x(1-x). If copying dominates and lower effort is below the renewal threshold, every mixed trajectory loses support and capacity.

**Distinctive consequence:** the proof handles changing mean effort and gives a strictly interior limiting high-effort fraction at collapse. Universal adoption of neglect is unnecessary. In a checked illustration, support rises from 2 to about 4.633 before collapsing while replenishing capacity erodes.

**Evidence and scope:** [proof](practice-transmission-model.md), [checks](selection-and-replacement-checks.json). The copying law, inheritance, external feedstock, and constant response parameter are assumptions. It is resistance to a specified alternative, not an ESS against every possible mutant.

## U09 Paid contributor returns can conflict with shared renewal

**Status:** derived restricted allocation model. A fraction of actual output rewards contributors and the remainder renews shared support. Current-return imitation and claim costs yield explicit invasion signs and stable mixtures. Too little retention can leave viable maintenance invasible; too much can favor full contribution while starving shared support.

**Evidence:** [derivation](selection-of-renewal.md), [checks](selection-and-replacement-checks.json). The worked strict-support interval is (10-sqrt(5))/19 < phi < 3/5; the nonhyperbolic join at phi=5/9 needs a separate one-sided stability argument, supplied after review.

**Limits:** fixed operating scale, divisible flow, private operating budgets not fully closed, fixed appropriation rule, and enforcement effectiveness assumed rather than established by its fee. No universal optimal retention fraction or political prescription follows.

## U10 Selected adoption need not complete functional replacement

**Status:** exact result in a delayed-maturation model. Logistic adoption with an already mature seed, fixed maturation lag, and immediate predecessor retirement can create a temporary renewal deficit despite positive adoption advantage and superior mature productivity. The integrated maximum deficit gives the necessary and sufficient initial reserve for this specified transition.

**Evidence:** [proof and formulas](replacement-and-establishment.md), [checks](selection-and-replacement-checks.json). In the worked example, .729169 reserve is required; .5 crosses its floor while adoption is approximately 58.47%.

**Limits:** exogenous adoption advantage, fixed demand, reliable maturation, no upper storage cap over the transition, and irreversibility at the declared floor. Other retirement policies or earlier failure of the predecessor can reverse conclusions about adoption speed.

## U11 Pending work has a schedule independent accounting identity

**Status:** established occupancy-time identity specialized to functional replacement. If every later adopter spends L units of time maturing and a mature seed epsilon already exists, total pending-capacity time is L(1-epsilon), independent of any monotone complete adoption schedule. Heterogeneous durations give the cohort-weighted integral instead.

**Evidence:** [Tonelli derivation and primary Little-law reference](replacement-and-establishment.md). Quadrature checks at four rollout speeds give the same 1.98 integrated overlap while peak extra capacity changes.

**Limits:** this equals duplicate-service time under full predecessor retention. It is a sufficient handoff protocol, not a universal minimum. Actual implementation also needs financing, peak capacity, and authority. The identity is not claimed novel.

## U12 Shared interests can coexist with attracting loss of a frame

**Status:** derived conditional result. In the specified policy-and-frame system, qdot=q(1-q)(bz-c) and zdot=lambda q(1-z)-mu z, exclusion (0,0) is locally asymptotically stable even when the actual common benefit b exceeds cost c. If lambda(b-c)>mu c, a stable full-activity equilibrium coexists with an interior saddle. The system produces the diagnostic experience that sustains its own evaluation; nearby partly active states can approach exclusion.

**Evidence:** [synthesis](../../../sources/15-codex-theory-conversations/2026-10-05-formation-and-revision-of-frames.md), [mathematical audit](situated-frame-math-audit.md), [checks](situated-frame-checks.json). An initial numerical prediction that q=.05,z=.9 would escape failed; that case and the failure from z=1 at the same q remain recorded. Matched q=.1 illustrations were selected after checking basins.

**Limits:** two analyst-specified representations, reliable acquisition, aggregate represented-return policy adjustment, positive frame loss, available funding and authority, and fixed common purposes. Familiar prediction error tending to zero is established for an explicit auxiliary error law. This is not an account of unrestricted novelty or changing values. Common-interest learning failures have close prior art.

## U13 Local amplification of a revision loop depends on conversion and loss rates

**Status:** standard local stability result applied to effective proposal origination. Adding beta z(1-q) to the inquiry equation gives the closed-state Jacobian [[-c,beta],[lambda,-mu]]. Exclusion locally attracts when beta lambda<c mu and is unstable when beta lambda>c mu. The statement extends to continuously differentiable systems with this Jacobian at the equilibrium; equality depends on nonlinear terms.

**Evidence:** [same-model origination extension](situated-frame-math-audit.md) and [checked weak and strong origination trajectories](situated-frame-checks.json). The benefit b drops out of this linearization while still influencing nonlinear persistence and the basin structure.

**Limits:** rates must correspond to independently identified mechanisms. Beta combines effective proposal origination and any assumed enactment access; it does not independently identify authority or legitimacy. This is not a universal ethical gradient, a new stability theorem, or evidence that every socially valuable proposal should spread.

## U14 Protected inquiry can have a finite escape threshold and a recurring cost

**Status:** exact bifurcation and conditional intervention result in the beta=0 system with qdot=(1-q)[q(bz-c)+u]. Under baseline bistability, the low attractor and saddle merge at u_SN=(mu/lambda)(sqrt(b)-sqrt(b-c))^2. A strict larger introduction rate yields convergence to the high equilibrium; equality leaves a semistable state. Reaching both unassisted saddle coordinates, with at least one strict, is a sufficient condition for withdrawing protection without relapse in the unchanged model.

**Evidence:** [proof](situated-frame-math-audit.md), [source](../../../sources/15-codex-theory-conversations/2026-10-05-formation-and-revision-of-frames.md), [numerical record](situated-frame-checks.json). An absent-benefit comparison b=0 converges to q*=u/c for 0<u<c and q0<1, imposing trial cost u per time without modeled benefit. The exact q0=1 boundary remains invariant and pays c. Blocking successful evidence uptake prevents retained coverage despite protected activity.

**Limits:** u is an introduction rate, not a resource bill. Trial cost is cq; a separate analytic protection-stock extension requires additional maintenance funding and is not among the simulated cases. The sufficient duration and budget are not claimed minimal. Reliable evidence and enforceable funding remain assumptions; harmful or false proposals require further mechanisms.

## U15 Fresh confirmation separates exploratory search from acceptance error

**Status:** established concentration and multiplicity result, applied to the implemented discovery procedure. Conditional on a nominated predicate, independent binary outcomes from fixed-size randomized groups give a one-sided Hoeffding bound for the difference in failure rates. Accepting only when the lower bound exceeds action cost, with four fresh attempts each assigned alpha=.05/4, bounds the probability of any nonbeneficial policy acceptance by .05. The 73 discovery-only candidates do not require another multiplicity penalty for the independently confirmed nominee.

**Evidence and limits:** [implementation audit](candidate-discovery-math.md) and [synthesis with formula](../../../sources/15-codex-theory-conversations/2026-10-05-discovery-before-demonstrated-returns.md). The cash-dependent schedule preserves independence in this stationary, independent-unit model because it cannot select on remaining attributes or unseen outcomes. Reused confirmation data, outcome-dependent stopping, drift, carryover, or informative missingness require a different argument. Zero observed false acceptance is not a proof of zero error. This result is not claimed novel.

## U16 Funding must be available when a valid procedure incurs its costs

**Status:** necessary accounting constraint for a specified procedure. If a result due by T requires observations initiated by T−ell, expenditure necessarily prepaid by the last such initiation must fit within funding available by T−ell. Other necessary expenses through producing the result must fit within funding available by T. Available funding includes initial reserves and permitted credit. Analysis fees paid after observation must not automatically be charged to the earlier deadline.

**Evidence:** the [implemented financing certificate](../../../sources/15-codex-theory-conversations/2026-10-05-discovery-before-demonstrated-returns.md) prepays 42.97 units for the first full discovery-and-confirmation procedure. A schedule allocating only 23 over the entire horizon cannot complete it. For a report by block 24 with delay two, this protocol needs the 42.97 by block 22; the specified allocation family reaches this necessary boundary near rho=.8153055884.

**Limits:** procedure-specific costs and payment timing, no unmodeled free evidence, and identified resources. Passing the budget bound does not ensure adequate candidates, information, power, or implementation. A cheaper valid procedure or alternative support changes the bound. The numerical boundary is not a universal phase transition, an emergent institutional attractor, or a reason to preserve one particular organization.

## S01 Bounded discovery and separate institutional gates work in a synthetic benchmark

**Status:** computational result with frozen held-out evaluation, not an empirical social claim. Across 256 independent seed clusters in a symmetric conjunction task, protected inquiry validated and deployed the useful contextual policy by the declared cutoff in 256/256 hazard-present worlds. Removing institutional standing or deployment authority preserved the first validated evidence and prevented deployment. No policy passed in 256 protected absent-hazard worlds, where inquiry cost 150.49 per run. Less severe funding schedules produced eventual but sometimes late evidence.

**Evidence:** [protocol, tests, frozen inputs, results, and analysis](../../../experiments/situated-discovery/README.md). Fourteen arms and two hazard conditions share randomness within each seed, so the 7,168 trajectories are not independent replications. Failure under the severe budget and expiring-link controls was forced by the supplied constraints. Gate effects were programmed controls, not discovered political regularities.

**Limits:** a strong planted effect, finite analyst-supplied grammar, known actions, fixed common purposes, independent cases, a calendar funding rule, and free indefinite retention after linkage. There is no physical irreversibility at the timeliness cutoff, paid archive, successor learning, endogenous veto, or post-discovery renewal policy. Synthetic success does not establish unrestricted concept formation, human coordination validity, or alignment.

## U17 Maintaining inquiry can have value when current testing has none

**Status:** standard finite-horizon Bellman comparison and an exact conditional certificate. After a posterior q, keeping ready capacity is strictly preferable when feasible and its upkeep m is less than V(T(q),absent)−V(T(q),ready). Rebuilding cost and lag enter those continuation values. A two-period example begins with certain absence, so a current test is useless; paying .1 to keep testing available reduces total expected loss from 2 to 1.9.

**Evidence:** [derivation and implementation audit](recurrent-inquiry-math.md), [source](../../../sources/15-codex-theory-conversations/2026-10-05-recurrent-inquiry-and-inherited-evidence.md), and [exact calculations](../../../experiments/recurrent-inquiry/results/analysis.json). The model charges diagnostics, upkeep, rebuilding, and response costs, and distinguishes a valid negative from an uninformative diagnostic failure.

**Limits:** supplied Markov process, fixed common loss, known diagnostic, free retained sufficient belief, no passive state-revealing outcomes, and an exogenous per-period inquiry allowance. This is endogenous expenditure within a supplied planning rule, not the emergence or selection of that rule. High maintenance expense, insufficient resources, immediate free replacement, or no future use can remove the advantage. Zero terminal value explains terminal abandonment; it is not evidence of degeneration.

## U18 Historical truth and current decision relevance can separate

**Status:** exact prediction and decision-value identities in the specified binary Markov model. A perfect negative observation followed by j unobserved transitions gives current need probability [1−(1−2h)^j]/2. Under stationary prior, gross value of the old exact state for one response is (L/4)[(1−2h)^j−abs(1−2c/L)]_+. A record can remain truthful and statistically predictive after it ceases to change this decision.

**Evidence and limits:** [proof](recurrent-inquiry-math.md) and [computed aging comparisons](../../../experiments/recurrent-inquiry/results/analysis.json). In the implemented h=.1,c/L=.4 example, the priced reliable handoff ceases to pay at age four, but gross decision value reaches zero only at age eight. This uses a known change model, not learning that a model is wrong. Different future questions, accountability, or new interpretations may still make raw records valuable. No general license to discard archives follows.

## U19 Successor inference must condition on every surviving information channel

**Status:** Bayes conditioning and exact one-step communication result. A missing message can depend on the predecessor's information, delivery failure, or other constraints. The successor's posterior must use that likelihood and all specified visible cues. With perfect private binary knowledge, reliable agreed disclosure, common cue-conditioned prior q, setup fee f0 and payload fee f, opening the channel pays exactly when the old state's decision value exceeds f0+f min(q,1−q). Sending the rarer state can reveal both because silence identifies the other.

**Evidence:** [derivation, delivery-erasure extension, and concavity proof](recurrent-inquiry-math.md), [handoff calculations](../../../experiments/recurrent-inquiry/results/analysis.json). The four deterministic disclosure rules suffice even against hidden send randomization in the specified one-step model. Fully revealing public cues remove the incremental benefit of transmission. Delivery failures weaken the inference from silence.

**Limits:** common purpose and known protocol, specified public cue, truthful messages, and no observable private attempted-message bill. Setup is selected from public information before private-state-dependent disclosure. These are paid communication results, not indefinite archive maintenance, a joint succession model, or an ethical duty of disclosure. Resetting a successor to ignorance despite informative surviving traces would be a modeling restriction requiring its own justification.

## S02 Adaptive inquiry allocation improves selected cases at matched expected inquiry expenditure

**Status:** exact finite-model numerical result, exploratory rather than held-out or empirical. In eight eight-period examples, adaptive capacity decisions reduce operating loss relative to the best ex ante lottery over all 128 capacity schedules, even though both permit adaptive randomized tests and the comparison matches expected inquiry expenditure. The matched budget binds in every case. Operating-loss differences range .007655–.083365. The representative adaptive total is 2.226351 versus 2.309716 for the matched calendar lottery.

**Verification:** [protocol, code, five tests, complete records, and figure](../../../experiments/recurrent-inquiry/README.md). Independent Lagrange-dual checks reproduce two comparator optima within 2.6e−10. Four limiting controls have no adaptive advantage. The stationary but unknown state with unreliable diagnostic still benefits from adaptive stopping; a stationary perfect-diagnostic control added after review removes that gap.

**Limits:** equal expected inquiry costs, not pathwise spending or total operating expenditure. The weak advantage follows from nesting of policy classes; strict gaps are selected conditional examples, not evidence that real institutions adopt the better rule. The diagnostic is supplied, belief is free to retain, and the separate handoff module is not dynamically integrated. Five tests and AI review do not constitute human peer review or alignment validation.

## U20 A sufficient summary can cease to suffice after model expansion

**Status:** established model-relative information constraint with an exact constructed counterexample. For a complete contiguous binary history under an unknown constant symmetric switching rate, final state, transition count K, and length N preserve the full posterior prediction. Histories 00010 and 01000 both end at zero with K=2,N=4. Under equal-prior slow-then-fast and fast-then-slow models, however, they predict next need .44835 and .05165 and recommend opposite actions at threshold .3. Their identical total-count summary contains no information about regime order in that specified family.

**General decision criterion:** for finite history X, summary T, and specified future binary event Y, put pX=P(Y=1|X), pT=E[pX|T]. Expected minimum loss using T is at least that using X at every binary-response threshold. Equality at every threshold holds exactly when pX is a function of T, up to null events. This follows from conditional concavity, not a novel theorem. A noninjective summary cannot answer every arbitrary question about the original record.

**Evidence:** [proofs and primary precedents](model-revision-inheritance-math.md), [source](../../../sources/15-codex-theory-conversations/2026-10-05-inherited-evidence-under-model-revision.md), [verification](../../../experiments/revisable-inheritance/README.md).

**Limits:** fixed joint model, losses, and feasible actions for the information comparison; costs excluded from gross information value. The declared timestamps, fair initial distribution, and observation process matter. Timed counts match raw-record value in the implemented families; raw preservation is not uniquely required or always worth its price. Recurring states and mechanisms remain possible. This is not a proof that history never repeats or that the model itself has been discovered.

## U21 Bayesian updating within a finite family does not admit an excluded model

**Status:** exact support constraint. In the two positive-likelihood switching models, prior probability zero for one candidate remains zero after any finite observation sequence. For positive prior epsilon, posterior odds can grow; over N transitions their maximum is epsilon/(1−epsilon) times 9^N. This bounds which decisions finite evidence can change without treating a small prior as permanent exclusion.

**Evidence and limits:** [derivation](model-revision-inheritance-math.md). The result concerns an excluded member of a finite model family, not a single point under a continuous prior. Introducing a model, revising a prior, receiving a new observation, and updating within the admitted family are distinct operations. The present experiment supplies model admission; it does not explain why an institution permits it or discovers the alternative.

## S03 Joint inquiry and successor action can use capacity as an information channel

**Status:** exact finite-team calculation with endogenous inspection, channel opening, readiness, disclosure, and current diagnosis, conditional on a supplied model family and fixed retained format. A six-decoder search per public state solves the declared decision problem and conditions correctly on readiness and silence. Under base prices, total expected losses for public-last-only/count/timed/raw formats are .275/.284/.27037/.27037 in the ordered family. Total-count retention has a cost but does not distinguish regime orientation, so it is not inspected.

**Additional mechanism:** with payloads and current diagnosis prohibited, paid readiness alone can encode retained ordering. An independently derived ordered-family policy has operating loss .25259328125 and total .270442609375 after positive retention, inspection, and readiness fees, matching the computed optimum. This is a signaling effect, not the future testing option value of U17. A sender with only the uninformative old summary cannot recover erased orientation by signaling from it; enabling a fresh test can add new information.

**Evidence:** [protocol, code, five tests, cases, and figure](../../../experiments/revisable-inheritance/README.md), [design and implementation audit](model-revision-inheritance-design-review.md). The decoder optimization agrees with independent exhaustive sender enumeration on smaller cases and six additional N=4 count-format cases. All retained-format and model-family cases include their actual costs; this is not a spending-matched comparison. Equal-cost timed/raw formats have equal optimum values.

**Limits:** one handoff and one future action, fixed common losses, known truthful protocol, a supplied perfect current diagnostic, and a common public endpoint. Archive formats are fixed counterfactual comparisons before a later family is supplied; an earlier best-format policy needs uncertainty over future questions. Historical acquisition and indefinite memory renewal remain exogenous. No empirical historical or institutional validation, unrestricted representation formation, or normative alignment theorem is established.

## U22 An archive-only admission rule cannot identify an absent distinction

**Status:** exact information constraint, an application of established total-variation bounds. For the entire permitted observation D and any randomized admission rule g(D), the difference in admission probability between two worlds is at most TV of their observation laws. Equal laws imply equal admission probability. A gate with size at most alpha in one cannot have power above alpha in an observationally identical world where the candidate would help.

**Certificate:** the four-world construction has identical joint routine (K,Z,Y) distributions, even with one later outcome per independent window. Two pairs also share complete four-switch-window/endpoint laws while differing in whether order predicts later need. A historical anomaly gate is therefore unable to distinguish usefulness within either pair. Fresh word/outcome pairs add the missing information. The claim concerns a specified observation interface; it does not extend to arbitrary complete histories already containing that link, overlapping windows, repeated outcomes, or other informative public cues.

**Evidence and limits:** [mathematical proof and implementation audit](prospective-revision-math.md), [source synthesis](../../../sources/15-codex-theory-conversations/2026-10-05-questions-without-anomalies.md). This extends the earlier observation constraint to admission of investigation; it is not a claim of mathematical novelty. The candidate is supplied in a grammar, and absent historical anomaly does not establish either safety or uselessness of a proposal.

## U23 Prospective preservation has a priced continuation threshold

**Status:** exact expected-loss identity within the declared workflow. Retaining m order records before a later question arrives costs m*c_a. With continuation-question probability lambda, admission R_w=A_w+(1−A_w)*eta, fresh validation probability V_w, cohort cost L*c_v, subsequent H decisions, gross candidate gain Delta_w, and ongoing order cost f, incremental loss is C_w=m*c_a+lambda*R_w*[L*c_v+V_w*H*(f−Delta_w)]. Worldwise products must precede prior averaging. All tested and untested expenses follow the specified chronology.

**Consequence:** audit-first preservation pays exactly when its prior-averaged downstream benefit, weighted by question probability, exceeds its prepaid cost. Expected loss is affine in the independent challenge probability eta. An endpoint eta=0 or 1 minimizes scalar Bayes risk; eta=1 makes paid positive audit quotas redundant relative to direct validation. Minimax regret can favor an ex ante lottery. Hard branch budgets remain necessary independently of the question probability.

**Limits:** two supplied questions with an independent arrival law, fixed candidate, fixed audit and validation sizes, known response efficacy, and common declared losses. This is neither the optimal policy over all experiments nor a universal case for maximum memory or maximum inquiry. A current-task-only retention rule chooses m=0; combining it with an audit-required gate creates invariant exclusion by construction, not an empirically established attractor.

## S04 A paid direct question can reveal usefulness that an anomaly gate misses

**Status:** exact exploratory finite calculation. Under base prices, in world U, audit-28 adoption probability is .02719406 while direct fresh validation reaches .93837537. Including a .5 probability of the later question, all screened validation records, and deployment ordering costs, incremental loss is +.46584157 versus −3.24909019. World T supplies the opposite counterexample: a genuine historical anomaly that does not justify the candidate. Validation tests net ongoing benefit using p*=c+f/tau_min, and does not certify recovery of sunk investigation costs.

**Evidence:** [protocol, code, six tests, full comparisons, controls, and figure](../../../experiments/prospective-revision/README.md). At baseline, 130 workflows and 286 declared priors give direct/no-inquiry/audit winners 233/49/4. These are counts on an exploratory prior grid, not real-world frequencies. The finite-workflow minimax lottery has worst regret .841001 versus 1.024563 for the best pure choice, with primal/dual agreement within 2.7e−15. Independent elementary audit/validation/cost calculations agree within 5.3e−14.

**Controls and limits:** five question probabilities, six true-net-zero/test-boundary controls, and thirteen one-parameter controls remain recorded. Tight caps can leave no inquiry as the sole feasible workflow, making same-class regret zero despite missed beneficial action. Original and revised inputs are retained. This is a single constructed episode with independent windows and fresh targets, supplied funding and grammar, fixed evaluative commitments, and no empirical institutional or AI deployment validation.

## U24 Recurrent shortfalls can eliminate inquiry despite positive mean returns

**Status:** conditional survival theorem, an application of established ruin and absorbing-chain mathematics. If, conditional on every surviving history, a block of L rounds has probability at least epsilon>0 of causing inquiry shutdown, then Pr(T>nL)<= (1−epsilon)^n and E[T]<=L/epsilon. Bounded accessible reserves, a positive unavoidable active expense, uniformly possible sufficiently long funding shortfalls, and no post-shutdown replenishment imply this condition. Independent periods are not required.

**Certificate:** cost one, cap two, return three with probability one-half and zero otherwise gives uncapped expected net income +.5, yet almost-sure shutdown and mean lifetime six. It does not have positive reserve drift at the cap. For the implemented data-generated inquiry procedure, cap-eight lifetime is 98.6084; cap 32 raises it above a million and gives 99.914% survival through 1,000 projects. Infinite-horizon failure alone says little about immediate practical risk.

**Evidence and limits:** [proofs, finite-chain equations, and independent high-precision checks](inquiry-renewal-math.md), [source](../../../sources/15-codex-theory-conversations/2026-10-05-renewal-of-inquiry.md). The modeled service may lose access while the wider institution keeps producing. Dormancy, restart, access to other reserves, unbounded buffers, declining hazards, finite duties, or a reliable productive allocation change the result. The theorem neither makes permanent inquiry desirable nor derives an ethical objective or a universal optimum budget.

## U25 Bounded one-time improvement credits cannot fund unlimited recurring expense

**Status:** exact telescoping accounting constraint. If a monotone score V_t is bounded above and one-time grants satisfy 0<=G_t<=gamma*(V_(t+1)−V_t), total credited resources are at most gamma*(Vmax−V0). With initial reserve b0 and active expense at least c, M funded rounds require M*c<=b0+gamma*(Vmax−V0).

**Interpretation and limits:** successful improvement can exhaust this funding base, but the bound does not prove continued inquiry necessary after a task is solved. Recurring royalties, continuing productive benefits, or genuinely new problems supply different bases. Bounded V alone is insufficient if V can fall and the sum of positive improvements is unbounded. This is a separate analytic module, not a claim that S05's iid new-project experiment has bounded total improvement. See the [mathematical memo](inquiry-renewal-math.md).

## S05 Observed credit and recognition renew inquiry differently from its value

**Status:** exact exploratory finite procedure. Participants' local counts generate a candidate; independent validation gates adoption, and a third monitoring cohort supplies observable credit. No hidden true effect is used for grants. In the useful iid-project world, expected social value per active round is +1.037754 after retainer and inquiry burden, and uncapped expected grant after expense is +.866262. At cap eight, credit-only funding has mean lifetime 98.6084 and survival after 1,000 rounds .00002015. A narrow ledger recognizes only context A while preserving per-active evidence, deployment, and value; mean lifetime drops to 20.3577.

**Paid comparison:** a one-unit floor paid from a supplied six-unit productive output maintains active inquiry and permits restart. A constant grant of 5r matches nominal expected grant per active round and maintains the useful main case, but does not match capped deposits, realized cumulative expenditure, or inactive funding; r is supplied. A subcost floor permits intermittent restart. All cash flows include treasury spill and satisfy the conservation identity.

**Counterweights:** without beneficial changes, the protected procedure adds 1,050.04 expected loss over 1,000 rounds versus 8.40 before credit-only shutdown. In the .39 near-null control, continued inquiry yields 11.77 expected false adoptions in 1,000 rounds despite valid per-project tests. Agenda diversion is imposed, not strategically generated. Funding paths are endogenous, but the funding and recognition rules, productive floor, candidate grammar, response efficacy, and norms remain supplied.

**Evidence:** [protocol, code, six tests, all 480 grid cases, twelve full baseline traces, benchmarks, controls, and figure](../../../experiments/inquiry-renewal/README.md); [independent implementation audit](inquiry-renewal-design-review.md) and [primary-literature audit](inquiry-renewal-prior-art.md). Independent rational and high-precision checks agree; largest reported lifetime relative discrepancy at cap 32 is about 5.3e−11. Original results remain preserved after a generic cost-consistency guard and explicit additional controls. This is neither empirical validation nor a model of evolving institutions or unrestricted concept formation.

## U26 Reliable reopening requires discriminating information before its deadline

**Status:** established information inequality applied to recoverable inquiry. Let P0 and P1 be the complete observable-transcript laws under the same policy in healthy and hazardous worlds. If reopening probability is at most alpha under P0 and at least 1−beta under P1, with alpha<1−beta, KL(P1||P0)>=kl(1−beta,alpha). If ordinary observations supply at most Io divergence and at most n paid observations each supply conditional divergence at most D, necessarily nD+Io>=kl(1−beta,alpha).

**Assumptions and limits:** include inherited history, passive production, internal randomization, action-dependent observations, and elapsed-time dynamics. An information upper bound and suitable absolute continuity must actually hold; perfect identifying observations can make KL infinite. This is necessary, not sufficient, for timely affordable correction. Identical observations limit discrimination, not the possibility of calendar reopening. Under summable per-episode alpha levels and uniformly bounded information per genuinely new episode, uniform positive detection power cannot persist indefinitely. This is not an impossibility of learning one stationary fact or all time-uniform inference.

**Evidence:** [derivation and primary-source relationship](recoverable-inquiry-math.md), [synthesis](../../../sources/15-codex-theory-conversations/2026-10-05-recoverable-inquiry.md). The finite DP does not implement an indefinite alpha-spending guarantee.

## U27 A positive mature surplus can coexist with an unaffordable recovery bridge

**Status:** exact conditional trajectory certificate using resource integration. Under xdot=g−delta*x and bdot=kappa*x−o−m after correction, let x*=g/delta, A=kappa*x*−o−m>0 and D=kappa*(x*−xc). If D>A and the cash cap does not bind during the dip, the minimum cash needed at correction is (D−A−A*log(D/A))/delta. If D<=A, no initial cash dip occurs.

**Assumptions and limits:** productive stock must separately stay above its required floor; all earlier repair payments must already have been financed. Environmental support and the technology are supplied. Negative long-run A exhausts any finite reserve on this trajectory. This is a separate continuous certificate, not an equation fit to the discrete experiment or a proof of institutional viability.

**Evidence:** [proof](recoverable-inquiry-math.md) and [source](../../../sources/15-codex-theory-conversations/2026-10-05-recoverable-inquiry.md). The broader principle is that expected eventual returns do not certify every prefix payment.

## U28 Recurrent fixed positive burdens cannot have a finite undiscounted lifetime total

**Status:** elementary lower bound. If every inquiry incurs burden at least h0>0 and lifetime inquiry count is N, expected lifetime burden >=h0*E[N]. Infinite expected inquiry count therefore precludes a finite expected undiscounted total under this premise.

**Limits:** finite horizons, average rates, discounting, diminishing per-test burdens, finitely many future needs, sufficient passive observations, and permanent resolution change the requirement. A finite-horizon expected burden is not lifetime FWER, FDR, or a pathwise cap. The claim does not decide which criterion is legitimate.

**Evidence:** [derivation](recoverable-inquiry-math.md); explicit criterion used in [protocol](../../../experiments/recoverable-inquiry/PROTOCOL.md).

## S06 Paid diagnostic access can be restored selectively from endogenous production

**Status:** exact finite synthetic decision result to reported floating-point tolerance. The controller sees all ordinary stock/output evidence, may repair directly, and must prefinance upkeep, lagged rebuilding, diagnosis, and repair from earned revenue. At H=8 and expected burden allowance .02, adaptive access has cost −43.12729236 versus −42.90810814 with no paid test; collapse probabilities are .12438943 and .17517617. Expected tests .13752974 and rebuilds .29575234 are paid. The selected trace drops initial readiness, later rebuilds after deterioration, and conducts its first within-horizon paid test. It is not a negative-test→pause→retest demonstration.

**Counterweights and scope:** seventeen of eighteen initial development cases use no paid tests; at H=8 allowance .05, adaptive/no-test results coincide without paid diagnosis. The uninformative-test control also matches no-test. Initial cash two and initial unreadiness do not change the highlighted optimum; lower stock or output remove paid diagnosis in the chosen controls. Compulsory service has minimum burden .371175 and is infeasible at .02. The target-absent repair burden is not complete harm because repair can restore stock without that fault; collapse remains possible. Purposes, probability model, repair technology, authority, free belief retention, and finite horizon are supplied. Equal starting resources do not imply equal realized spending.

**Evidence:** [protocol, code, all 34 cases, preserved development, seven independent tests, policy traces, and inspected figures](../../../experiments/recoverable-inquiry/README.md). Independent one-period mixtures and two-period occupancy LPs validate the recursion. Maximum declared-case primal–dual gap is 8.81e−9; maximum cash-ledger residual is 7.11e−15. An ex ante lottery meets the expectation constraint; individual policies need not. The robust viability recursion and continuous bridge certificate remain separate analytic modules. No empirical generalization, infinite-horizon guarantee, or novelty claim is established.

## U29 Plural expected requirements admit a common feasibility witness or separating obstruction

**Status:** established finite convex-feasibility theorem applied to correction. Finite deterministic observation-history policies and admissible ex ante lotteries generate a compact convex set Z of expected consequence vectors. Bounds z<=b are feasible iff min_policy w·z<=w·b for every nonnegative w. A positive separating gap proves incompatibility within that policy class. For any threshold relaxation Delta>=0 to restore feasibility, w·Delta must cover that gap; this is necessary, generally not sufficient.

**Assumptions and limits:** one common executable policy, finite expectations, declared admissibility, and permitted randomization. Separating weights are mathematical witnesses, not agreed moral weights. The convex argument also allows each coordinate to be evaluated under a different declared model/prior when every evaluator uses the same policy and independent commonly specified randomizer; that extension is not implemented by the common-model occupancy LP. Individually or even pairwise attainable bounds need not be jointly attainable: hull{(1,0,0),(0,1,0),(0,0,1)} cannot meet (.3,.3,.3), though every pair can. Expected-vector feasibility does not imply individual or pathwise protection.

**Evidence:** [proofs and prior-art positioning](plural-correction-math.md), [research synthesis](../../../sources/15-codex-theory-conversations/2026-10-05-plural-requirements-and-attainable-correction.md). Multiobjective control, occupancy geometry and nonnegative separation are established methods, not new mathematical results claimed here.

## U30 Correction permissions can remove joint feasibility and enabling conditions can be complements

**Status:** exact set inclusion and constructed counterexamples. Pure action removal with all other dynamics, information, resources and consequence definitions fixed shrinks the attainable set. In the one-period inherited model, testing then repairing on a positive result gives (F,H,C)=(.085,.10,.04). Without diagnosis, every policy obeys F+.9H=.45, incompatible with F<=.10,H<=.10. The posterior threshold .75 admits the response after diagnosis but blocks it when applied to the opening belief .5. A .95 post-test threshold blocks it too.

**Complementarity:** with stock one, prior one-half, cash two and repair prohibited, neither funding to eight nor repair permission alone meets bounds (.10,.10,.05). Both together do. An ineffective isolated relaxation therefore need not identify an irrelevant enabling condition.

**Limits:** pure action inclusion does not describe political changes that alter cooperation, trust or available resources. A missing diagnostic can arise from different causes; the attainable set does not identify its provenance. Supplied permission rules are not proved legitimate or illegitimate. A restriction can protect omitted consequences. Extra initial capital is not charged to C in this comparison; acquiring it would require explicit accounting.

**Evidence:** [analytic construction and nine independent tests](../../../experiments/plural-correction/README.md), [design audit](plural-correction-design-review.md). Effects are conditional toy results, not estimates of institutional prevalence or a general case for relaxing protections.

## U31 Initial expected acceptability need not survive continuing refusal rights

**Status:** separate analytic counterexample and necessary continuation condition. A public fair coin assigns correction losses (0,2) or (2,0); fixed refusal yields (1.1,1.1). Before revelation both prefer expected losses (1,1), meeting bounds (1.05,1.05) under implementation. After revelation the party facing two prefers refusal, so those bounds are unattainable with voluntary continuation when that party can unilaterally trigger the stated fallback and no compensation, commitment or alternative response is available.

**Condition and limits:** at a reached history h where i may refuse, their expected remaining continuation loss must be no greater than the specified refusal loss. This is necessary for voluntary continuation and sufficient only against exit deviations under further stated execution/tie assumptions. It does not prove truthful reporting, obedience, legitimate rights or agreement about the model. The productive experiment does not yet implement strategic parties, compensation or this continuing-participation constraint. History compression must preserve disclosed lottery outcomes and other information relevant to refusal.

**Evidence:** [primary-literature audit and analytic extension](plural-correction-prior-art.md), [source](../../../sources/15-codex-theory-conversations/2026-10-05-plural-requirements-and-attainable-correction.md). The example instantiates established participation logic and is not claimed as new bargaining mathematics.

## S07 Joint correction requirements can be feasible with diagnostic access and infeasible without it

**Status:** finite synthetic feasibility calculation on an unchanged copy of the preceding physical model. Replace the old weighted objective with the vector of collapse probability F, target-absent/test burden H, and expenditure minus output C. At six periods, bounds (.02,.02,−30) admit a full-access witness (.018232591,.018232591,−30.017674090), but no policy without paid diagnosis. Loosening H to .03 admits both modes; tightening F to .01 with H=.02 excludes even full access. Surviving actions retain identical transitions and costs.

**Evidence:** [protocol, implementation, all results, tests, and inspected figure](../../../experiments/plural-correction/README.md). All 252 declared grid queries, 22 detailed comparisons (overlapping the grid), and 84 frontier queries are retained. Nine independent tests cover latent enumeration, the exact one-period witness/separator, conditional permissions, action inclusion, forward/backward policy reconstruction, finance/permission complementarity and terminal-only graphs. Maximum flow residual 1.01e−15, independent policy discrepancy 2.49e−14, and primal–dual discrepancy 5.21e−17; no unresolved case. These are floating-point checks, not empirical or interval-arithmetic certificates.

**Limits:** thresholds were chosen after exploration, with common known probabilities and a central executable policy. Aggregate F/H/C do not represent individual exposure, ownership or negotiated preferences. Burden has a supplied internal weighting; target-absent repair can be useful. A phase-I policy for an infeasible tuple is a violating diagnostic point, not an acceptable recommendation. Feasible grid counts do not measure real institutional quality. Separate heterogeneous-belief and continuation-participation results are not implemented in this production model.

## H01 Capacity measures predict recovery beyond current output

**Status:** empirical hypothesis. At matched current output, independently measured renewal and intervention capacity should help predict recovery after specified disturbances. Failure to improve withheld intervention predictions would count against the chosen capacity measures.

## H02 Endogenous authority changes correction outcomes

**Status:** empirical hypothesis with an earlier negative pilot retained. Match resources and information while varying how authority over evaluation is assigned and renewed. The earlier local pilot failed its P1 prediction; the revised design has no new run in this cycle. See the [earlier contribution map](../../../sources/15-codex-theory-conversations/2026-10-04-alignment-coordination-contribution-space.md).

## H03 Observation and uptake can change transmission independently of production

**Status:** empirical hypothesis suggested by U08. Hold renewal technology and actual cost fixed while changing exposure to immediate-cost comparisons and their disclosure of replacement capacity. Measure copying, gross renewal, and stock outcomes independently. A wrong predicted adoption sign or unchanged copying under the manipulation counts against the specified uptake mechanism.

## H04 Functional establishment depends on the handoff policy

**Status:** empirical hypothesis suggested by U10 and U11. At matched initial reserve, adoption advantage, and maturation process, change whether predecessor retirement follows adoption or verified successor readiness. Measure function, overlap costs, peak capacity, and floor crossings. Failure despite verified provision of the allegedly sufficient conditions refutes the mapped model or exposes a missing constraint.

## H05 Institutional reproduction of evidence changes correction under common interests

**Status:** empirical hypothesis still untested; a restricted synthetic instance is implemented as S01. At matched initial performance and common aims, compare endogenous versus protected inquiry and record retention while separating candidate formation, evidence admission, and enactment. The full hypothesis predicts changes mediated by the proposed inquiry or inheritance links, including possible relapse after short interventions. No-hazard and false-candidate controls must expose costs and mistaken revision. S01 implements candidate generation, testing, and separate gates, but uses prescribed funding and free persistence after records are linked; it does not test the full endogenous reproduction mechanism.

**Failure criteria:** identical behavior after the relevant feedback is removed supports static misspecification rather than the proposed reproduction mechanism; disappearance of the effect after resource matching favors a resource explanation; externally inserting the correct proposal does not demonstrate discovery. See the [experiment design](situated-frame-experiment-audit.md). The earlier two-state calculations are not a run of this richer test; the subsequent synthetic experiment only partially implements it. Equal potential resource allowances in S01 do not imply equal actual inquiry expenditure.

## P01 Generative capacity is a profile of protected functions

**Status:** proposed operational definition. Renewal, recovery, revision, succession, and useful transformation are evaluated against explicit tests, stakeholders, budgets, disturbance classes, deadlines, and protected constraints. This is not a complete formalization of 生生 or a uniquely complete list.

## N01 Shared agency and legitimate revision deserve protection

**Status:** explicit normative commitment. The physics or mathematics of persistence does not determine whose interests count. Stable coercion, domination, and inventive exploitation are counterexamples to treating viability or novelty as sufficient ethical criteria.

## Claims deliberately not accepted

- All evolution, markets, bureaucracy, and backpropagation are literally the same algorithm.
- Selection always optimizes a global objective, or always produces degeneration.
- Every beneficiary must maintain all of its own supports.
- Greater diversity, complexity, growth, or option count is always regenerative.
- A universal cancer attractor or a universal ethical gradient has been established.
- This integration is already novel, empirically validated across domains, or a solution to AI alignment.

These exclusions preserve specific questions for evidence; they do not rule out stronger results after further work.
