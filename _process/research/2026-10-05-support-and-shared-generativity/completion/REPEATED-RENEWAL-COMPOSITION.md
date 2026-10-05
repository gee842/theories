# Repeated renewal requires the actual successor situation

5 October 2026. AI-assisted formal continuation after e214ecf. The previous turn completed the all-entrance first-replacement calculation. This note supplies the next composition contract and exact finite diagnostics. It does not turn that rare event into reliable operation. The [independent critique](REPEATED-RENEWAL-CRITIQUE.md) derives additional necessary bounds from the actual reaction law.

**Advance.** A renewal probability composes only through the situation actually left behind: support, relations, memory, time and spent resources. A scalar one-cycle success probability is insufficient, even if every state's one-cycle success mass is known. The appropriate object is a successful-cycle transition measure. Its iteration gives exact finite renewal probabilities and an explicit accumulated approximation bound. Its greatest fixed point characterizes indefinite successful continuation, but that characterization is a certificate target, not an explanation of why nature supplies a favorable kernel.

## 1. State, event and boundary

Work first with the declared classical stochastic realization, a nonexplosive process on a standard Borel state space. At successful cycle boundaries let x describe the full causally sufficient continuation situation. This can contain a center, its partners, installed machinery, external source condition, waste, accessible records and the state of its controller. Physical hidden state is not automatically available to a controller. A controller's actions remain restricted to its allowed information; its installed memory is part of the process. If a proposed reduced state is insufficient, retain a sufficient history or justified belief state instead of assuming Markov closure.

Choose a measurable organizational set S and one stopping rule for a completed cycle. The rule must specify what is delivered, what is protected during the excursion, which replacements count, and what permits the next cycle. A first failed return cannot be replaced silently by a later successful retry. If retries are intended, include their delays, costs and failures in the installed rule. A change of genotype, carrier, topology or controller may be allowed at return; exact identity need not be preserved. The allowed new situation must satisfy the declared successor conditions.

For original-carrier turnover, tag the carriers present at each admitted cycle entry and stop on the first organization after their required wear. Resetting these analyst tags at a completed cycle changes the next assay's reference carriers; it neither regenerates a physical carrier nor installs a free sensor. Continuous operation of every role during the excursion is a stronger event than the existing first-turnover assay and must be required explicitly if claimed.

A restored local fuel coordinate does not restore an external source, clear waste or reconstruct apparatus. Either those conditions are included in x and evolve, or a stated maintained boundary supplies them with an explicit work account. A finite source cannot be reset by writing the same subsystem coordinates at each cycle. This is where the user's relational emphasis becomes a mathematical requirement on the continuation law.

## 2. The successful-cycle kernel and exact composition

Let

\[
K(x,dy\,dt\,dc)
\]

be the subprobability law of a successfully completed next cycle, its actual successor y in S, duration t>0 and charged resource vector c≥0. Missing mass is failure or noncompletion. Gross external withdrawals, dissipated work or other monotone charged expenditures can be used as c; a net reserve difference that can be negative cannot be substituted into the following simple budget recursion. Physical reserves, exchanges and their every-prefix feasibility also remain in the state/event law.

The kernel is induced by one installed mechanism, or by one specified feasible policy with its memory included. It is not selected anew using inaccessible information at each boundary. Time-dependent support is included through calendar time/source state, or represented by a corresponding nonhomogeneous family of kernels. The kernel is a common continuation law only when the strong Markov or sufficient-history construction justifies it.

Write V_n(x,h,b) for the probability of n further successful cycles by remaining time h and within remaining nonnegative charged budget b. Put V_0=1 when h,b≥0, and V_n=0 outside that budget/time domain. Then

\[
V_{n+1}(x,h,b)=
\int_{t\le h,\ c\le b}
V_n(y,h-t,b-c)\,K(x,dy\,dt\,dc).
\tag{R1}
\]

Vector inequalities are componentwise. The law must already exclude any prefix that violates a nonmonotone safety or reserve constraint; a terminal test alone cannot enforce such protection.

**Proof.** Condition on the first completed cycle and its joint successor, duration and cost. On failure there are no n+1 consecutive successful cycles. On success the actual remaining budgets and continuation situation are those in (R1). The sufficient-state property supplies V_n for that continuation. Induction proves the formula for every finite n. No independence of cycle outcomes or identical return state is required.

Let F_p(dy dt dc) be the successful first-formation measure from the original preparation p. The unconditional probability of formation followed by n successful cycles is

\[
\int_{t\le H,c\le B}V_n(y,H-t,B-c)F_p(dy\,dt\,dc).
\tag{R2}
\]

Failed preparation remains in the denominator. The [full-successor result](FULL-SUCCESSOR-RESULT.md) evaluates a one-cycle version of this composition for its declared event. Its gate totals do not expose the complete reusable marked kernel, and do not determine (R2) for n≥2. Conditional normalizations and resetting the clock/source would change the event.

The existing exact-return expression r(T)^n is recovered only when each successful cycle returns to the same adequate situation and law, with the same per-cycle time allowance T and compatible repeated funding. It certifies a restrictive event by total time nT. It generally differs from the more permissive global-deadline integral (R1).

This is standard Markov-renewal structure specialized to the present physical ledger and event semantics. The conditioning argument above is supplied in full; no asymptotic renewal theorem is assumed. For the standard state/sojourn-time formulation, see [Alsmeyer, *On the Markov Renewal Theorem*, corrected version, introduction](https://www.uni-muenster.de/Stochastik/alsmeyer/MRTheorem1.pdf). Reading scope: introductory kernel definition and dependence conditions; no external asymptotic theorem is used as evidence for this physical model.

## 3. Reliability and error budgets

For an installed sequence, let A_k mean that its first k cycles succeeded within all declared constraints. Suppose on every reachable successful history the conditional next-cycle failure probability is at most ε_k∈[0,1], with the successful successor remaining inside the domain on which the next bound holds. Then

\[
\Pr(A_n)\ge\prod_{k=1}^n(1-\epsilon_k)
\ge1-\sum_{k=1}^n\epsilon_k.
\tag{R3}
\]

This is a conditional bound, not an independence assumption: E[1_Ak times conditional success] gives the induction. Every timing, resource and maintenance premise needed by the row bound must continue to hold at the actual entries. Proving a bound only at one favorable prepared organization is insufficient.

Conversely, if next-cycle failure is at least δ_k∈[0,1] on every such history, then Pr(A_n)≤∏(1−δ_k). A fixed δ>0 implies zero probability of infinitely many consecutive successful cycles. Summable, actually realizable upper risks ε_k with their product positive can give a positive infinite-cycle lower bound, but only if the process is defined at all those epochs, cumulative cycle times diverge and the necessary support remains feasible. Writing a summable budget does not construct the growing protection, source or learner that realizes it. If Σ ε_k≤ε<1, (R3) gives at least1−ε on the intersection of all finite success events. Finite-time failure or infinitely many cycles in finite time is excluded by the stated model assumptions, not by that algebra.

A useful error contract follows on the augmented state z=(x,h,b), with an absorbing cemetery outcome completing each subkernel to a probability kernel. The terminal success indicator is0 at the cemetery and1 on the admissible live domain. Let the actual and approximate cycle kernels differ, uniformly on every reachable z, by at most η_k in total variation. For 0≤f≤1 their operator difference is then at most η_k. Telescoping the product of the operators gives

\[
|\Pr(A_n)-\widehat{\Pr}(A_n)|
\le\min\{1,\eta_{\rm formation}+\sum_{k=1}^n\eta_k\}.
\tag{R4}
\]

Formation error is omitted when preparation is exact. Every Markov operator is a contraction for the sup norm; induction bounds the difference one stage at a time. This applies to the complete marked transition law, including failed outcomes. Accuracy of a single success total or of a conditional-on-success state law does not establish the required bound. Neither the old seven-capture reversible certificate nor the one-cycle full-successor certificate currently provides these uniform row errors for repeated operation.

## 4. Exact diagnostics: equal one-cycle answers can hide opposite continuations

On states ready and depleted, take successful-cycle kernels with duration1 and charged cost1 for each successful transition:

\[
K_A=\begin{pmatrix}0.9&0\\0&0\end{pmatrix},
\qquad
K_B=\begin{pmatrix}0&0.9\\0&0\end{pmatrix}.
\tag{R5}
\]

Each has success mass (0.9,0) by starting state. An observation of only success, duration and charged cost from a fresh ready preparation gives the same full one-cycle law. But two-cycle success is0.81 for A and0 for B. The successful successor's support state differs. These are abstract finite kernels, not two identified chemistries or fits to the RNA observations. They establish the missing identification requirement. Observing that successor state would separate them.

A second exact diagnostic retains correlated time and cost. From ready, successful atoms are (probability0.6, ready, time1, cost2) and (0.3, repairable, time2, cost1). From repairable they are (0.5, ready, time1, cost1) and (0.25, repairable, time3, cost2). The four two-cycle success paths have respectively probabilities0.36,0.18,0.15,0.075; durations2,3,3,5; costs4,3,2,3. Consequently:

| Global deadline | Charged budget | Two-cycle success |
|---:|---:|---:|
| 3 | 3 | 0.33 |
| 5 | 4 | 0.765 |
| 2 | 4 | 0.36 |
| 5 | 2 | 0.15 |

The [exact record](../../../../experiments/shared-renewal-capability/renewal-composition/README.md) compares the marked recursion to these explicit rational path sums and checks finite examples of (R4). It does not substitute finite diagnostics for the general conditioning/contraction proofs. It adds no empirical data or positive physical-regeneration example.

Task identification therefore extends from a scalar J to the functionals actually claimed: two models that agree on all supplied observations must agree on each claimed V_n and support quantity, or the compatible ranges must be retained. Unique microscopic parameters remain unnecessary; a task-preserving equivalence for one cycle may fail for a repeated task. Discovering that distinction can require a new test even when every old one-cycle prediction remains correct.

## 5. Infinite continuation and its limits

Suppress explicit budget/time marks only when the full source, memory and support situation still lies in x and the declared cycle rule remains adequate. Define the substochastic operator Kf(x)=∫f(y)K(x,dy), with unsuccessful/nonfinite cycles absent. Then

\[
v_n=K^n\mathbf1\downarrow v_\infty,
\qquad Kv_\infty=v_\infty.
\tag{R6}
\]

Here v_infty is the probability of infinitely many consecutive successful cycles; assume their boundary times diverge on that event. The sequence decreases because K1≤1 and K is positive. Dominated convergence gives the fixed-point identity. Every 0≤g≤1 satisfying Kg=g has g=K^ng≤K^n1 for all n, so g≤v_infty. Thus v_infty is the greatest bounded fixed point in[0,1].

An independently specified certificate h with 0≤h≤1 and h≤Kh gives h≤K^nh≤K^n1 and hence h≤v_infty. The certificate has explanatory content only if h and the inequality can be derived from independently characterized structure, rates and support. Choosing h=v_infty after solving the same problem is a characterization, not a mechanism or a universal directional law. A finite system with a uniform cycle-loss probability has v_infty=0 even with repeated positive return paths. A maintained population with restart can continue delivering functions while the stricter event of no failed cycle has probability0; that is another event with its restart mechanism charged.

Capability order is stronger still. A bound for repeated one-task success does not show that the whole region of jointly available functions expands. Maximizing over protocols at each hidden state would also change an installed-dynamics statement into a feasibility statement. Actual architecture formation, useful prevalence and changing assay vocabulary remain separate obligations.

## 6. Consequences for the current physical branches

The [rate-derived critique](REPEATED-RENEWAL-CRITIQUE.md) identifies a stronger obstruction in the existing four-slot forward chemistry: each organizational return again has only one Y lineage carrier. Before its first descendant is born, the productive birth rate is at most3β and the original carrier's wear rate is d. This yields a uniform per-cycle success upper bound3β/(3β+d), independent of fuel reserve or capture rate. At unit rates, n full turnovers have probability at most(3/4)^n from an entered organization. This is a restriction of the actual architecture, not an arbitrary unfavorable kernel.

The inherited-reserve ledger separately requires at least6n fresh captures when the final organizational reserve is no lower than the first. Intermediate reserve changes telescope; they need not all be nonnegative. While the productive lineage exists, at most three slots can be uncharged capture machinery, so the fresh-capture intensity is at most3g. A Poisson upper tail for at least6n captures by H is another necessary bound. These bounds can be combined by taking their minimum; multiplying them would invent independence. The critique gives the exact hypotheses, finite-deadline strengthening and calculated thresholds.

The RNA one-stage task also does not yet close a renewal cycle. Uniformly discarding four-fifths of whole droplets leaves counts inside a retained droplet unchanged. Requiring another fivefold increase relative to that new start forces geometric growth inside a fixed capacity. For the same two-RNA r>1 law with no partition/reset, n successive D-fold rounds require D^n h0+D^(nr)p0<C; simply raising the old one-stage J to the nth power is invalid. Fusion, partition and replenishment can restore an occupancy scale, but their complete joint transition law and support account must be included. The continuing relational organization may span several daughter compartments; preserving one original droplet label is a different claim.

The next positive result must therefore change and identify the relevant mechanism: remove or mitigate the singleton-lineage bottleneck, establish a paid restart or larger coupled continuation, or identify a real mixing/partition process whose output is a valid next preparation. The [new RNA evidence investigation](RNA-REPEATED-RENEWAL-EVIDENCE.md) addresses that concrete transfer interface. A positive result must retain failed preparations and the full environmental cost, then satisfy a meaningful declared repeated-task reliability. The broader goal remains active; this composition and the new obstruction specify what successful work must overcome.


## 7. A source-anchored transfer consequence: mixing has no fixed sign

The new [physical evidence audit](RNA-REPEATED-RENEWAL-EVIDENCE.md) identifies a concrete candidate for the missing transfer stage. In the inspected Ledoux et al. author version (PDF p8, equations2–3), a compartment after dilution is redrawn with a Poisson total and multinomial species allocation. Conditional on its current population field, Poisson splitting makes its two species counts independent with means

\[
\lambda_{H,i}=(1-s)h_i+s\bar h,
\qquad\lambda_{P,i}=(1-s)p_i+s\bar p.
\tag{R7}
\]

For the diagnostic below set d=1 and examine mixing without a deletion step, so the bars are the exact means of the given population field. This is a declared restriction of the source transfer model, not its fivefold RNA protocol. With d>1 the source uses the before-dilution means divided by d for the pool contribution; those need not equal a finite population’s realized mean after random deletion. No such equality is assumed here. The local intensity sum equals the Poisson-total parameter, and multiplying the Poisson mass by the multinomial mass factorizes into the two Poisson masses. This is a model law for mixing and sampling, not a directly measured molecular transition law. In particular, it preserves the material mean under the stated field, not the realized finite total on every redraw.

Consider the new, deliberately narrower assay that the next compartment contains at least one of both species. Its conditional probability is

\[
\psi_s(h_i,p_i)=(1-e^{-\lambda_{H,i}})(1-e^{-\lambda_{P,i}}).
\tag{R8}
\]

Co-occupancy is a possible prerequisite for a partner-dependent task. It does not require growth, sustained functioning, net replacement or renewal of the supplied apparatus. Its observation and the physical mixing cost still need an implemented assay and ledger. It therefore cannot replace the existing renewal target.

Take equally many compartments of two kinds, with a>0. Two fields have identical complete separate H and P occupancy distributions:

- Segregated: (a,0) and (0,a).
- Co-located: (a,a) and (0,0).

Both have means a/2 for each species. At s=0 the source redraw still samples Poisson counts around the local field; it is not a deterministic identity operation. The segregated field has joint occupancy0, while the co-located field has joint occupancy (1/2)(1−e^(−a))². At s=1 both yield (1−e^(−a/2))². Thus complete mixing improves the segregated field, but its sign for the co-located field is determined exactly by

\[
\Delta_{\rm co}=(1-u)^2\left[1-\frac{(1+u)^2}{2}\right],
\qquad u=e^{-a/2}.
\tag{R9}
\]

It is negative for 0<a<2ln(1+sqrt(2)), zero at that boundary, and positive above it. Integer preparations a=1 and a=2 fall on opposite sides. In the lower regime, concentrating both partners together protects their meeting probability; in the higher regime, spreading them across empty compartments more than compensates for that loss of concentration. This explanation follows from the common specified transfer law and the joint initial field, with no assigned preference for either arrangement.

The [separate exact calculation](../../../../experiments/shared-renewal-capability/renewal-composition/mixing-check.json) encloses these probabilities by rational Taylor bounds and checks finite Poisson-splitting identities. For a=1, co-located success decreases from approximately0.199788 to0.154818, while segregated success increases from0 to0.154818. For a=2, co-located success increases from approximately0.373823 to0.399576. These are probabilities in the declared transfer model, not observed biological frequencies.

This is a prospective *model consequence* of a published closure, derived after reading its source. It is not a new physical experiment, a fitted transfer kernel, or a joint-capability order. The paper's dye measurements assess a different fluorescence-packet transformation and exclude sufficiently dim droplets; those data do not directly validate (R7)–(R9) for RNA co-occupancy. The measured stirring-to-model correspondence, molecular costs and empty-compartment denominator must be established for that use. The result supplies a precise possible test of consequential joint structure: old marginal occupancy data agree exactly while the same mixing operation has opposite effects on a new joint assay. New measurements could test this closure before it is composed with replication and repeated renewal.
