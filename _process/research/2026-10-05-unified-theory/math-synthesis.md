# Mathematical synthesis: relational generative continuation

Prepared 5 October 2026 after checkpoint `38f8022eab23e1c08c847163e2daec9a425549c6`. This is a mathematical integration memo, not a replacement of the preserved source sessions. General proofs below were re-derived from their assumptions; the separate executable checks verify finite instances and separation examples. No claim of mathematical priority, empirical universality, or proof-assistant certification is made.

## 1. Determination

The formal work can be unified as a theory of **which consequential continuations a situated process can realize, how its activity changes the conditions of those continuations, and when the actually installed process maintains or revises those conditions**.

The most compact defensible core is a relation among available interventions, actual information, and retained consequences. Resources, observation, authority, representation, selection, repair, and succession are not independently mandatory ontological coordinates. They are mechanisms that must be distinguished whenever they change the relevant continuation relation. This answers the search for an elegant foundation without declaring a small, permanently complete list of entities.

Its nontrivial explanatory content comes from restrictions on that relation: losses and supply bounds, inaccessible observations, payment precedence, shared constraints, feedback mechanisms, selection rules, and implementation costs. A freely adjustable transition kernel would only redescribe the outcome. The physical and institutional mechanisms supply the predictions and obstructions.

Four mathematical questions must stay distinct even inside one theory:

1. **Representation:** which distinctions must a description retain?
2. **Attainability:** does some admissible, informed and funded policy meet the declared requirements?
3. **Actual continuation:** does the installed process select, execute, reproduce and revise such behavior?
4. **Justification:** are the declared protections, affected parties and amendment procedures defensible?

The corpus substantially answers the first three in explicit classes. Mathematics does not derive the fourth from persistence. The new participant-protection model makes that non-implication constructive: shared production can persist while an affected participant loses the protected capacity.

The resulting theory should be presented as **one architecture with conditional mechanism theorems and a rigorous boundary of applicability**, not as one universal scalar law. Its economy lies in a common semantics and proof discipline. Its substantive plurality remains necessary.

## 2. Minimal formal kernel

Let \(h\) denote an admitted causal history of a process. A history is not automatically the history available to a participant. For participant \(i\), let \(I_i(h)\) be its delivered information and physically retained memory. Let \(\Pi(h)\) be the implementable continuation policies from that situation, including command permissions, memory, computation, expenses, delays and refusal outcomes. The same policy must be used across unresolved possibilities that share its information.

Let \(\theta\) index an explicitly admitted family of causal models. For a policy \(\pi\), write

\[
\Psi^{\pi,h}_\theta=(\mathcal T^{\pi,h}_\theta,P^{\pi,h}_\theta)
\]

for the retained admissible trace set and, where stochastic semantics is supplied, the retained trace law. Either component can be omitted if the question uses only the other. Keeping their roles explicit prevents a probability-one statement from silently becoming an all-path statement. Resource bills, delivered events, timing, protected consequences and amendment versions are included only as required by the question, but cannot be omitted when consequential.

Define the attainable response-profile set

\[
\mathscr R(h)=\{(\Psi^{\pi,h}_\theta)_\theta:\pi\in\Pi(h)\}.
\tag{K1}
\]

A declared evaluative contract \(\mathfrak A\) is a set of acceptable response profiles. It can conjunct plural requirements, specify limited risk, require periodic service, permit rest and legitimate termination, and include rules for amendment. Feasibility is

\[
\mathscr R(h)\cap\mathfrak A\ne\varnothing.
\tag{K2}
\]

This is a definition, not a prediction or an ethical derivation. A claim that an intervention expands capacity requires a **specified comparison** of attainable sets or protected tests and a demonstrated implementation map. Raw option count, entropy, diversity or dimensionality is not a universal measure of better continuation.

An actual institution or organism adds an installed mechanism \(\kappa\), with its code, memory, selection and revision dynamics included in the joint process. Its behavior is \(\Psi^{\kappa,h}\), not the maximization implicit in asking whether some \(\pi\) could succeed. A feasible alternative that no admitted mechanism selects or installs remains an unrealized possibility.

This kernel is minimal in the explanatory sense of avoiding redundant categories. Its formal minimum is separately supplied by the response-quotient theorem below. It is not asserted to be a uniquely necessary ontology of reality.

### Important distinctions about the kernel

- \(\mathscr R\) is invariant under faithful description of the same situation; it is generally changed by actual activity.
- Equal attainable sets do not imply equal effects for each named command. Swapping the names of two commands can preserve the attainable set while changing causal predictions. Mechanism analysis retains labelled command responses.
- A mathematical sufficient statistic need not be computable or affordable to the participants. The analyst's representation must not become their free hidden input.
- More free optional information cannot shrink attainable possibilities if every old policy remains implementable. A sensor purchase that consumes the response budget can shrink them. The comparison changes when physical costs change.
- A changing grammar or evaluator can be included in the process state. That is semantic accommodation, not proof that every future meaningful concept can be generated, evaluated or learned.

## 3. Strongest results and their precise roles

### T1. Least-information exact representation and its revision

For declared queries \(\Gamma\), let \(a_\gamma(h)\) be the answer supplied by the causal and evaluative contract. Define

\[
Q_\Gamma(h)=(a_\gamma(h))_{\gamma\in\Gamma},\qquad
h\sim_\Gamma h'\iff Q_\Gamma(h)=Q_\Gamma(h').
\]

**Theorem.** Every deterministic representation \(R\) from which all answers can be decoded factors onto \(Q_\Gamma\): there is a unique \(f\) on \(R\)'s image with \(Q_\Gamma=f\circ R\). Therefore \(Q_\Gamma\) is the unique coarsest exact deterministic representation up to recoding.

**Proof.** Set \(f(R(h))=Q_\Gamma(h)\). Equal representations have equal decoded answers, so the assignment is well-defined; each image point has a representative, proving uniqueness. The response profile itself decodes every answer. Thus every exact partition refines its partition.

For controlled observation tests, continuation closure adds recursion. If \(d(h,\tau)\) is the probability of a finite test under imposed actions, then

\[
d(huo,\tau)=\frac{d(h,(u,o)\tau)}{d(h,(u,o))},
\qquad d(h,(u,o))>0.
\]

Equal profiles have equal numerators and denominators; hence the common actual observation produces the same updated profile. This requires the needed continuation and conditioning queries. An arbitrary collection of current summaries need not be recursively sufficient. Hidden protected outcomes require joint audited continuation queries; they must not be silently added to the participant's observations.

If \(\Gamma\subseteq\Gamma'\), the new partition refines the old one. An erased distinction cannot in general be decoded when a new concern makes it relevant. Example: \(h\in\{0,1,2,3\}\), old representation \(h\bmod2\), new query \(\lfloor h/2\rfloor\). Old storage merges 0 with 2 but the new answer separates them. Re-observation or raw retained evidence is necessary unless some other channel supplies the missing distinction.

**Role in unification:** this gives an exact, situated sense of elegance. A concern or mechanism is retained because an explicit separating question needs it. It does not imply minimum scientific description length, minimal physical memory, or universal optimality. Finite-rank linear predictive bases, physical-state strong quotients and minimal hidden generators are different optimization problems.

**Primary corpus source:** `/Users/ren/theories/_process/research/2026-10-05-generative-foundation-review/optimal-foundation/MATHEMATICS.md`, sections 2–8.

### T2. Faithful causal implementation preserves capability

Suppose a concrete process and an abstraction have compatible actual information interfaces. Every abstract action has a causal concrete adapter that terminates, respects all internal payment/safety prefixes and deadlines, and has the same joint law or supported outcomes for the next retained state, observations, events and time. Matching must hold at every reachable implementation state and adapter memory, not merely after averaging away relevant memory.

**Theorem.** Every admissible abstract policy lifts to a concrete policy preserving the retained response. Thus abstract attainability implies concrete attainability. A reverse implementation map gives equality of attainable sets and transfers impossibility statements as well.

**Proof.** Compose each policy decision with its adapter. At each boundary the policy uses only permitted history; the adapter implements the decision causally. The local joint-response match gives the next retained-history match. Induction gives every finite trace match. For probability laws, consistent finite-cylinder laws determine the corresponding measurable infinite-path law. For sure objectives, explicitly preserve admissible supported paths; in the supplied finite strong-quotient setting, every abstract supported path lifts stepwise to a concrete supported path.

This joins the structural-foundations transport results to the full-picture completeness bridge. Matching separate marginals is insufficient when harms depend on correlations. Matching successful ordinary traces without preserving who chooses versus who may refuse is insufficient for control.

**Primary sources:** `structural-foundations/outputs/cycle-3/constraint-transport.md`; `cycle-4/selection-and-scale.md`; `full-picture-conjecture/outputs/general-access-theorem.md`, local refinement lemma; `completeness-bridge.md`, especially sections 2–4A, under the snapshot root given in §8.

### T3. Continued vulnerable functioning requires recurrent provision

There are two related but distinct results.

**Bounded-lifetime version.** There are finitely many functional support types. Each instance of type \(i\) lasts at most \(\tau_i\); every later instance requires a still-functioning earlier parent of a permitted type. Renewal counts as a new instance. No later organizational instance enters from outside. If the type graph is acyclic,

\[
d_i=\tau_i+\max(\{0\}\cup\{d_j:j\to i\})
\]

bounds the expiry of every type-\(i\) instance, and all supports expire by \(D=\max_i d_i\le\sum_i\tau_i\).

**Proof.** Source types can only use their initial instances. Topological induction bounds each descendant's latest creation by its predecessors' latest expiry and then adds its lifetime. Every directed path visits each type at most once.

**Unbounded-loss version.** For finitely many tracked capacities,

\[
C_i(t)=C_i(0)+E_i(t)+\sum_jR_{ji}(t)-L_i(t)\ge0.
\]

Initial capacities are finite; cumulative flows are nonnegative, nondecreasing and finite on bounded intervals. Assume productive vulnerability: an internal supplier delivering unbounded cumulative service itself suffers unbounded loss of a tracked capacity. Then every node with unbounded loss is downstream of an unbounded external supplier or a directed cycle of unbounded internal provision.

**Proof.** Unbounded loss demands unbounded provision. With finitely many inputs, some input is unbounded. If it is external, stop. Otherwise productive vulnerability permits repeating the argument at the internal predecessor. In a finite graph the backward chain reaches an external source or repeats a node.

**What this establishes:** recurrent support ancestry is necessary in the stated vulnerable finite class. It does not require every component to be on a cycle, every cycle to operate at once, or every transformation to be selection. Cycles can be too slow or weak and fail to support the required function. Infinite acyclic succession, a perfectly durable supplier, finite total loss and continuing external organizational supply are explicit alternatives that violate different premises.

**Primary source:** `/Users/ren/theories/_process/research/2026-10-05-generative-foundation-review/root-foundation/ROOT-FOUNDATION.md`, R2–R3; `TURNOVER-AND-CLOSURE.md`.

### T4. Plural protected capacities have an exact sustainable set and dual failure deadline

Let margins \(v\ge0\) and typed reserves \(b\ge0\) obey

\[
\dot v=Mu-\rho(v),\qquad \dot b=p-Qu.
\]

Assume the actually implementable activity set \(U\) is nonempty, compact, convex and fixed; constants in \(U\) are executable; \(M,Q,p\) are fixed. The locally Lipschitz loss law satisfies \(\rho_i(v)\ge r_i\) everywhere in the safe orthant and \(\rho_i(v)=r_i\) on its floor face \(v_i=0\). Initial margins and reserves are finite.

Define

\[
F=\{u\in U:Mu\ge r,\ Qu\le p\}.
\]

**Theorem.** All requirements can be maintained indefinitely from any finite safe initial state iff \(F\ne\varnothing\). A constant member of \(F\) suffices. If \(F=\varnothing\), no adaptive policy succeeds indefinitely from any finite safe initial state.

**Proof.** A constant feasible activity makes every floor-face derivative inward or tangent and every reserve derivative nonnegative, so the orthant is invariant. Conversely, integrate a safe path to time \(T\). Its average activity belongs to \(U\) and satisfies

\[
M\bar u_T\ge r-v_0/T,\qquad Q\bar u_T\le p+b_0/T.
\]

Compactness gives a convergent subsequence as \(T\to\infty\), whose limit lies in \(F\).

When \(F\) is empty, convex separation supplies nonnegative \(\lambda,\mu\), not both zero, with

\[
\beta=\min_{u\in U}\{\lambda^T(r-Mu)+\mu^T(Qu-p)\}>0.
\]

The weighted margin \(W=\lambda^Tv+\mu^Tb\) satisfies \(\dot W\le-\beta\). Therefore

\[
T\le\frac{\lambda^Tv_0+\mu^Tb_0}{\beta}
\]

for every safe interval. These multipliers certify a joint shortage; they are not ethical utility weights. For constant losses, the infimum of these bounds is the exact maximum service duration, because any feasible average can be executed constantly along the straight segment between safe endpoints.

**Exact example checked:** two capacities each lose \(2/5\), \(u_1+u_2\le1\), resource inflow \(3/5\), resource use \(u_1+u_2\); margins \((1/10,1/10)\), reserve \(1/5\). The joint weighted margin loses \(1/5\) regardless of activity, giving duration at most 2. Constant \(u_1=u_2=7/20\) attains exactly 2. Each capacity could be sustained alone; the conjunction cannot persist.

The theorem does not survive arbitrary removal of convex implementability, fixed availability or minimum-loss assumptions. With only \((1,0)\) and \((0,1)\) available, losses \((1/2,1/2)\), and zero margins, the unavailable midpoint cannot be treated as an executable simultaneous activity. State-dependent availability can make a feasible envelope action inaccessible. An interior protected state with zero loss can invalidate a criterion using positive floor loss as a global lower bound.

**Primary source:** `/Users/ren/theories/_process/research/2026-10-05-generative-foundation-review/root-foundation/PLURAL-CAPACITY.md`.

### T5. Access, order and capacity have an exact financial realization

This is a specific mechanism theorem, not the universal form of all resources. Cash capacity is \(C\), initial cash \(b_0\), treasury \(t_0\). Each event supplies nonnegative income \(i_j\), then permits fee-free treasury-to-cash transfer of at most \(r_j\), then demands an atomic bill \(c_j\). Overflow is retained in treasury; there is no cash-location-dependent risk or shared transfer quota.

Let \(N_j=b_0+t_0+\sum_{k\le j}(i_k-c_k)\). Maximum achievable postpayment cash satisfies

\[
B_0=b_0,\qquad B_j=\min\{C,N_{j-1}+i_j,B_{j-1}+i_j+r_j\}-c_j.
\]

**Theorem.** A schedule is payable iff this greedy recurrence never becomes negative. It maximizes cash after every feasible payment and needs no future knowledge. Equivalently all total-funds prefixes, accessible-funds prefixes, and storage windows satisfy

\[
\begin{aligned}
\sum_{k=1}^jc_k&\le N_0+\sum_{k=1}^ji_k,\\
\sum_{k=1}^jc_k&\le b_0+\sum_{k=1}^j(i_k+r_k),\\
\sum_{k=s}^jc_k&\le C+\sum_{k=s+1}^j(i_k+r_k),\quad1\le s\le j.
\end{aligned}
\]

**Proof.** For fixed total the maximal next prepayment cash is the displayed minimum, which is nondecreasing in previous cash. Induction proves greedy dominance. Unrolling the minimum recurrence yields the three displayed classes of inequalities.

This demonstrates why the general theory should retain causal access and temporal order rather than make them philosophical slogans. Equal total funds can differ in feasibility; an entire round's bill can exceed cash capacity if separate atomic bills admit refill. With unlimited refill before each bill, and the other assumptions maintained, total funds plus each bill's cap condition suffice. The simplification is derived under a mechanism contract.

**Independent check:** brute-force lawful transfers, the recurrence and the inequality characterization agree on 22,338 finite integer schedules. Original theorem covers nonnegative reals and arbitrary finite length; this check does not replace its proof.

**Primary source:** `full-picture-conjecture/outputs/general-access-theorem.md`.

### T6. Exact attainable safety under actual information

For a finite transition system \((X,A,F,Y,h,K)\), each \(F(x,a)\) is nonempty; unavailable commands and deadlocks have explicit losing outcomes unless termination is accepted. Let \(B\) be the set of still-possible states after the actual observation history. The exact update is

\[
\operatorname{Upd}(B,a,y)=\bigcup_{x\in B}F(x,a)\cap h^{-1}(y).
\]

The intersection is taken after the union. Unsafe possible states must never be deleted before testing safety. Let \(\mathscr B_K\) contain the nonempty safe observation-homogeneous sets. Define

\[
\Phi(W)=\{B\in\mathscr B_K:\exists a\ \forall y,\ 
\operatorname{Upd}(B,a,y)\ne\varnothing\Rightarrow
\operatorname{Upd}(B,a,y)\in W\}.
\]

**Theorem.** \(B_0\in\nu W\,\Phi(W)\) iff an actual observation-history policy guarantees indefinite safety. In the finite case, descending elimination terminates and supplies a finite belief-memory controller or a finite failure-rank certificate.

**Proof.** Updates contain exactly the states compatible with the full delivered history, by induction on path extension. A fixed-point witness selects one common action whose every possible update stays inside the invariant family, proving safety inductively. Conversely the beliefs admitting a winning policy are postfixed, using the first action and each residual strategy. Finiteness makes backward finite-horizon elimination stabilize; the first removal stage yields the bound for a counterpath against every policy.

The key quantifier is \(\exists a\ \forall x\in B\), not \(\forall x\in B\ \exists a\). Two indistinguishable situations requiring different immediate safe actions can each be individually repairable while the joint guarantee is impossible. A safe informative action before the deadline can change that; more computation over an unchanged indistinguishable history cannot.

Finite or bounded recurring obligations can be added with monitors. General partially observed recurrence needs more care: beliefs need not become subsets of the target for every real path to visit it repeatedly. The source's outstanding-obligation construction handles the finite sure-recurrence problem. A hidden two-state alternation visits either target indefinitely even though the belief remains the full pair.

Infinite-state existence extends through a greatest fixed point with set-theoretic choice. A finite algorithm, finite memory, measurable selector and physically affordable implementation do not follow. Infinite initial action branching can satisfy every finite horizon by choosing a longer finite countdown while admitting no infinite survival policy. Finite action choices restore the safety horizon interchange but not finite memory in infinite state.

**Primary source:** `full-picture-conjecture/outputs/continuation-proof.md`; recurrence refinement in its appendix and `progress-proof.md`.

### T7. The actual combined process has an exact invariant-and-rank characterization

Let \(Z\) include the physical system, installed controllers, permitted memories, evidence carriers, grammar, evaluators, commitments, permissions, resources, succession and phase monitors whenever needed. These are roles, not fixed universal coordinates. Let

\[
z\xrightarrow{\gamma}z'
\]

be its actual totalized microstep relation. It already contains the installed actors' decisions, every admitted environmental outcome, refusals and failures. Let \(K\) be the declared acceptable set and \(E_j(\gamma)\) the independently interpreted delivered events required to recur.

**Theorem.** Every actual run from \(B\) stays in \(K\) and delivers every \(E_j\) infinitely often iff there is \(H\) and ordinal-valued ranks \(\rho_j\) with

\[
B\subseteq H\subseteq K,\quad\Delta(H)\subseteq H,
\quad\neg E_j(\gamma)\Rightarrow\rho_j(z')<\rho_j(z)
\]

for every actual step from \(H\).

**Proof of sufficiency.** Closure gives safety by induction. If an event occurred finitely often, the suffix after its last occurrence would be an infinite strictly decreasing ordinal chain, impossible. Ranks may reset on a delivered event.

**Proof of necessity.** Take \(H\) to be the actually reachable set. For each event, its no-event relation on \(H\) has no infinite forward chain, since such a chain can be prefixed by a reachable path and would refute recurrence. Under the stated choice/well-founded recursion convention, give each state the supremum of its no-event successors' ranks plus one. This is an ordinal rank decreasing on each no-event edge.

For finite \(H\), each no-event graph must be acyclic and natural-number longest-path ranks suffice. For infinite \(H\), ordinal ranks can prove eventual service without any uniform finite delay. Positive physical-time continuation additionally needs time divergence: infinitely many internal steps must not accumulate in finite physical time.

This is the best unifying theorem presently available. It covers **one actual process containing its governors**, rather than an endless tower of ideal external governors. Each component must preserve the same joint invariant and decrease the relevant ranks or deliver their events. Its shared ledgers, real dispatch, microstep prefixes, installation and succession must all agree. An evolving verifier has to preserve the admitted proof contract; self-revision does not certify its own interpretation or empirical truth without assumptions.

The constructive sufficiency direction is useful: write independently checkable phase assertions and ranks. The existential necessity direction alone does not give an algorithm for arbitrary programs. Calling the set of successful states an invariant without proving local transitions would be circular certification.

**Independent check:** rank construction agrees with separate reachable-cycle analysis on all 225 total two-state event-labelled graphs and both safe sets, 450 cases. Parallel event and no-event edges with identical endpoints remain distinguishable; reporting an event on one branch cannot erase another event-free branch.

**Primary source:** `full-picture-conjecture/outputs/combined-process-proof.md`, Theorem C and local contracts; predecessor `structural-foundations/outputs/cycle-6/revision-and-scale.md`, R6.1.

## 4. A composed theorem for relational generative continuation

The results can be combined without pretending that every special mechanism has identical equations.

**Conditional composition theorem.** Suppose:

1. The actual process is defined with its permitted local information, physically executable actions and all relevant consequences; deadlocks and legitimate endings are explicit.
2. The protected set and recurring events have independently stated meanings, and amendment rules retain relevant historical obligations.
3. A concrete joint invariant and event-specific ranks satisfy T7, including every actual controller, evaluator, maintenance and succession transition; physical time diverges.
4. Any abstraction used in the certificate preserves the required causal/information/time contract through T2.
5. Any indispensable vulnerable capacities satisfy the finite support and productive-vulnerability conditions of T3.

Then the actually installed process has protected recurring continuation in physical time, its faithful descriptions preserve that result, and every indispensable capacity with unbounded loss has recurrent support ancestry from continuing external supply or an internal renewal cycle. If its capacities additionally obey T4, its sustainable activity set must be nonempty. If a payment module obeys T5, every required branch must satisfy the three funding/access/storage inequalities. If a response requires incompatible actions across indistinguishable possibilities, T6 identifies the information obstruction unless an executable informative route changes the state before the deadline.

**Proof.** T7 gives actual protection and recurrence; time divergence connects it to indefinite physical duration. T2 transports the certificate through the stated abstraction. Apply T3 separately to each indispensable unbounded-loss support. An infinite safe trajectory satisfies T4's integrated inequalities, so compactness implies the sustainable activity set is nonempty. T5 and T6 provide exact restrictions on the indicated modules. All conclusions concern the same actual process and the same joint protections.

This is a real integration, but its theorem is an assembly of scoped implications rather than a newly discovered universal law. Some situations need only a subset. A finite task ending well need not renew forever. A common robust action may remove any need to discriminate the hidden regime. A durable support need not be repaired. The framework tests when a mechanism is necessary rather than demanding every mechanism everywhere.

## 5. Mechanisms explaining which feasible regime is reproduced

Viability and certification leave a causal question: why does the actual selection mechanism retain one policy instead of another? The continuous model and finite structural experiments supply complementary answers.

In the continuous renewal model,

\[
\dot E=P(C)-\delta E-\bar uEC,\qquad
\dot C=(\eta\bar uE-\mu)C,\qquad
\dot x=(\eta-\kappa)E(u_H-u_L)x(1-x).
\]

Here support-to-capacity production inherits renewal effort, while copying responds to immediate expenditure saving. For strictly increasing bounded strictly concave \(P\), set \(m=\mu/\eta\), \(H=\max_C(P(C)-mC)\). When \(H>0\), critical effort is \(u_c=\delta m/H\). A pure-effort equilibrium satisfies \(E^*=m/u\) and \(P(C^*)-mC^*=\delta m/u\). Strict concavity gives a lower saddle and an upper ecological attractor for \(u>u_c\). The practice eigenvalue makes only the selection-favored upper equilibrium attracting in the full system when \(\kappa\ne\eta\).

This derivation genuinely explains a regime difference from supplied reproduction and copying events. It does not stipulate that a viable rule is chosen. The logit equation shows selection runs on accumulated support exposure. If selection favors a subcritical effort, the supplied logarithmic Lyapunov comparison gives collapse from every mixed start; the limiting favorable share need not reach one because absolute capacity disappears first. Even on the favorable side, depleted initial conditions can collapse. A locally attracting positive equilibrium is not a universally reachable rescue.

The strongest design lesson is plural rather than maximization: higher effort raises upper-branch capacity but lowers support \(E^*=m/u\). In the exact \(P(C)=9C/(1+C)\) example with unit \(\eta,\mu,\delta\), protections \(E>3/2\) and \(C>6\) require \(7/12<u<2/3\). Effort \(5/8\) satisfies both; effort 1 violates support protection. This was rechecked independently.

The finite structural models add physically explicit stages absent from the continuous model: adoption, paid diagnosis, report retention, evaluator revision, hardware inheritance, timed transfer and actual funded birth counts. They show that:

- a one-cycle terminal-cash selector can leave the viable region after a successful cycle, while a two-cycle selector establishes a sustainable design;
- correct identification can arrive after affordable installation has become impossible;
- a selected program can succeed with inherited hardware and fail without it;
- expected fitness or expected offspring cannot determine extinction without the distribution and dependence structure;
- an endowed robust mixture can sometimes sustain either regime without diagnosis, preventing an overclaim that information acquisition is always necessary.

The models share the same causal architecture but have different supplied technologies, prices, interfaces and boundaries. They should be **embedded and compared**, not have parameter-specific thresholds multiplied or averaged into a universal constant.

**Primary sources:** final-synthesis/`MECHANISM-MATH.md`; structural cycles 4–6 claim registers and their named proof companions.

## 6. New completion supplement: how it fits without changing the proof hierarchy

The supplement is preserved at `/Users/ren/theories/sources/20-codex-theory-sessions-2026-10-05/completion-supplement/root-of-wisdom/`.

Its three-reaction model supplies a stronger **formation witness** than a model that starts with positive renewal machinery: \(R\to C\), \(C\to D\), and powered \(D+C\to R+C\). It includes an assembly route so \(C\) can form when initially zero but \(R>0\). It therefore addresses an earlier formation gap inside a supplied reaction repertoire. The detailed new-mathematics audit belongs to the direction-review work; this memo uses only its declared embedding and scopes.

The reported threshold \(kM>b\), restoring relation \(\dot D=-kC(D-b/k)\), and nonnegative-network decay obstruction explain emergence of a maintained regime in that reaction class. They do not remove the energy boundary or manufacture a reaction repertoire. The all-degraded initial state is still absorbing. The finite-particle stochastic counterpart can become extinct almost surely despite the deterministic attractor. These distinctions are compatible with T3 and with the sure/probabilistic distinctions of T7.

The new `regeneration-and-effective-correction.md` is a particularly strong bridge between normative plurality and implemented recurrence. Shared support stays productive under both rules while a dispensable participant's reserve can vanish. A materially maintained claim route with actual binding authority yields a nine-round recurrent correction cycle. Its reported thresholds separate average funding \(f\ge11/9\), prefunding store \(K\ge3\), and participant timing \(h\ge1+c+d\). These are respectively a recurrent balance condition, an access/storage prefix condition and a protected deadline condition. They fit T4/T5/T7 structurally, although their exact numbers belong solely to the supplied protocol.

Its ethical premise is explicit: the affected participant matters independently of contribution to shared production. That premise belongs in \(\mathfrak A\), not in a theorem purporting to derive goodness from persistence. The installed replacement rule, automatic filing, funding stream and binding gate remain supplied. The model is a constructive proof of compatibility and failure separation, not proof that all societies spontaneously create or defend such a route.

## 7. Incompatibilities and counterexamples the unified text must retain

| Proposed collapse of distinctions | Exact obstruction or counterexample | Required repair |
|---|---|---|
| Persistence = acceptable generativity | Productive whole persists while dispensable participant loses capacity. Stable coercion is compatible with renewal. | Declare protected affected-party consequences independently. |
| Some successful policy = actual successful system | Available `retain` action is safe while installed rule selects `consume`, reaching failure. Structural one-cycle planner gives a nontrivial finite example. | Model selection, installation and reproduction of the actual rule. |
| Each need can be met = all needs jointly met | Two individual capacity demands exceed shared resource inflow; exact T4 deadline two. | Joint invariant and one consistent resource ledger. |
| Aggregate funds = payable action | Cash zero, treasury one, bill one, no permitted transfer fails despite total one. | Access, atomic bills, payment order, capacity and permission. |
| More information = more executable correction | Paid diagnostics spend the reserve required for installation. | Price sensing and retain delivery deadlines; preserve old policy feasibility before claiming inclusion. |
| Every correction needs diagnosis | The structural cycle-6 robust mixture survives both regimes under its specified initial resources. | Information is necessary only where no common adequate action exists. |
| A coarsest predictor = smallest physical generator | Persistent hidden bit can have a one-profile observer prediction but still requires correlated hidden generation; two hidden-state generators can induce infinitely many predictive classes. | Specify the optimization class and what histories/outcomes are retained. |
| One-step summaries = recursively adequate state | Same next observation, different subsequent futures. | Continuation/conditioning closure. |
| One-way abstraction = equivalent feasibility | Abstract safe policies may lift even when concrete extra policies succeed where abstraction fails. | Two-way policy correspondence for equivalence or transferred impossibility. |
| Same ordinary traces = same agency | A controller can choose `b` versus an environment that may choose `b` or `c`; both may have ordinary traces `{ab,ac}`. | Preserve control, refusal and information structure. |
| Safety = recurring generation | Safe self-loop delivers no work, maintenance or novelty. | Independently interpreted event obligations, where warranted. |
| Recurrence = novelty | One service event can repeat forever with no new kind of result. | Add explicit novelty questions; do not inherit an open-ended novelty theorem. |
| Positive deterministic equilibrium = immortal finite system | Absorbing failure with uniformly positive bounded-block probability implies eventual extinction almost surely. | State scale, stochastic assumptions, horizon and the intended reliability claim. |
| Good finite-horizon behavior = one indefinite policy | Unbounded initial choice of a finite countdown passes each selected finite horizon but all actual choices eventually fail. | Finite action/compactness assumptions or an actual invariant. |
| Productive cycle = sufficient renewal | Cycles can have subcritical gain or unaffordable timing. | Quantitative rate, accessible reserve and causal execution conditions. |
| Closure = energetic or explanatory self-sufficiency | Powered recycling, production feedstock and supplied rule grammars remain boundaries. | State which mechanisms are endogenous and which remain inputs. |
| Proof of a supplied evaluator = legitimacy | A sound computation may enforce a coercive standard; revision can erase labels without repairing past consequences. | Retain versioned obligations and an independently defended amendment contract. |

These are not peripheral caveats. They determine the theory's type discipline: which statements may legally be connected and which require an additional bridge.

## 8. Source map and genealogy

Snapshot root for the following short paths is `/Users/ren/theories/sources/20-codex-theory-sessions-2026-10-05/`. All readings below are preserved originals; none was edited.

| Integration role | Precise source |
|---|---|
| Corpus interpretation; avoid lossy consolidation and a forced single root | `/Users/ren/theories/_process/BRIEF.md` |
| Coarsest response representation, recursive observation update, rank-minimal predictive bases, incompatible minimalities | `/Users/ren/theories/_process/research/2026-10-05-generative-foundation-review/optimal-foundation/MATHEMATICS.md` |
| Attainable-profile invariance, lifetime and loss ancestry, information/execution boundary | `/Users/ren/theories/_process/research/2026-10-05-generative-foundation-review/root-foundation/ROOT-FOUNDATION.md` |
| Plural sustainable activity theorem and exact dual duration | `/Users/ren/theories/_process/research/2026-10-05-generative-foundation-review/root-foundation/PLURAL-CAPACITY.md` |
| Selection–renewal mechanism, concave production threshold, local stability, global subcritical collapse | `/Users/ren/theories/_process/research/2026-10-05-generative-foundation-review/final-synthesis/MECHANISM-MATH.md` |
| Finite adaptive policy optimum and support-retention limits | `/Users/ren/theories/_process/research/2026-10-05-generative-foundation-review/final-synthesis/ADAPTIVE-OPTIMUM.md` (integration architecture; detailed proof audit retained in its sibling `MATHEMATICAL-REVIEW.md`) |
| Integrated formulation and causal-identification counterexample | `/Users/ren/theories/_process/research/2026-10-05-generative-foundation-review/final-synthesis/INTEGRATED-THEORY.md` |
| Structural claim status across six rounds | `structural-foundations/outputs/CLAIMS.md` and `cycle-2/CLAIMS.md` through `cycle-6/CLAIMS.md` |
| Physical implementation, memory, control-versus-trace counterexample | `structural-foundations/outputs/formal-foundations.md`; `propositions-and-countermodels.md` |
| Prefix-safe protocol refinement and composition | `structural-foundations/outputs/cycle-3/constraint-transport.md` |
| Actual selection, stochastic path laws, approximate finite-horizon transfer | `structural-foundations/outputs/cycle-4/selection-and-scale.md` |
| Absolute funded population counts, branching dependence, extinction | `structural-foundations/outputs/cycle-5/population-and-scale.md`; `funded-selection.md` |
| Paid evaluator revision and robust no-diagnosis countercontrol | `structural-foundations/outputs/cycle-6/evaluator-revision.md`; `paid-revision.md`; `revision-and-scale.md` |
| Exact finance and causal scheduler refinement | `full-picture-conjecture/outputs/general-access-theorem.md` |
| Exact sure safety, finite failure ranks, infinite-branching and memory limits | `full-picture-conjecture/outputs/continuation-proof.md` |
| Actual delivered recurrence and its partial-observation obligation state | `full-picture-conjecture/outputs/progress-proof.md` |
| Two-way policy preservation; finite relative completeness | `full-picture-conjecture/outputs/completeness-bridge.md` |
| Actual installed self-revising process; joint invariant and well-founded ranks | `full-picture-conjecture/outputs/combined-process-proof.md` |
| New endogenous formation witness and hidden consequential mode | `completion-supplement/root-of-wisdom/outputs/endogenous-renewal-and-consequential-feedback.md`; mathematical details in `endogenous-renewal-mathematics.md` |
| New recurrent participant protection with paid usable correction | `completion-supplement/root-of-wisdom/outputs/regeneration-and-effective-correction.md` |

The mathematical ancestry is explicit in the sources: sufficient statistics and predictive-state representations; controlled bisimulation and refinement; viability and partial-observation games; well-founded termination/progress; convex separation; positive systems and renewal/selection dynamics. The contribution of this synthesis is organizing those tools around the reproduction and justified revision of the conditions of consequential continuation. It should not relabel those established mathematical results as newly invented laws.

## 9. Verification record and remaining work

Independent check files are `/Users/ren/Documents/Codex/2026-10-05/fo/work/math-review/check_integration.py` and `results.json`. They use only the standard library and do not import or change source artifacts. The run passed:

- 22,338 finite finance schedules, comparing explicit search over lawful transfers against both the greedy recurrence and the three inequality classes;
- 450 total two-state installed-process/safety cases, comparing finite decreasing-rank construction against separate reachable no-event-cycle detection;
- 10 groups of exact or algebraic separation witnesses, including plural deficits, information versus hidden-state action, actual versus available control, refinement of erased distinctions, safe stagnation, and event-label preservation.

The proofs in T1–T7 were re-derived above. The checks test small instances and implementation interpretations; they are not a mechanical verification of every general theorem. The new chemistry/control proof is being audited separately and is not silently counted among these checks.

The strongest unified formal claim is therefore ready now. Remaining research is also well-typed: identify real mechanism parameters; test transfer under withheld interventions; explain formation of new candidate and observation repertoires; establish safe access from outside a viable regime; defend affected-party standing and amendment procedures; and determine where stochastic lifetime rather than indefinite sure protection is the relevant question. None of those gaps prevents a coherent current theory, provided they remain declared gaps instead of being filled by the words “generative,” “optimal,” or “universal.”
