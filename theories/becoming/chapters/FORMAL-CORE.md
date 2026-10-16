# Formal core of relational generativity

Companion to [the unified theory](../history/THEORY.md), 5 October 2026. These are self-contained proofs and scoped reconstructions of results developed across the preserved sessions. Most proof methods are standard. No claim of mathematical priority, empirical validation, or proof-assistant verification is made. Source families and the additional verification record are identified in [SOURCE-MAP](../history/SOURCE-MAP.md) and [SYNTHESIS-RECORD](../history/SYNTHESIS-RECORD.md).

These propositions concern activity and the conditions of its continuation. Particular models additionally specify observation, intervention, organization or evaluation. Each proposition states which distinctions it assumes. A theorem about a finite information game is not thereby a theorem about every chemical or social process.

## Definitions and conventions

A **joint situation** represents the relations and conditions relevant to a stated question. Where a model distinguishes participants, surroundings, retained records, decision mechanisms or obligations, their relations belong in that representation. The following conventions apply where those distinctions are used: a **history** records events relevant to the question; an **information state** retains what a specified actor or implemented coordinator can actually distinguish; a **policy** depends only on that information and its permitted memory.

An **evaluation specification** states the comparisons being made and their relevant conditions. Depending on the model, these may include reference functions or affected parties, admissible disturbances or probabilistic models, protected conditions, tasks and events, budgets, deadlines and revision rules. Its requirements can be plural and inconsistent. Feasibility does not justify the specification ethically.

A **support** is independently identified by a causal mechanism or intervention contrast, including relevant substitutes. It is not defined as whatever happens to accompany survival. A **regenerative effect** replenishes or reconstructs a specified support. A **generative effect** can more generally produce or reorganize conditions used by later activity. Both descriptions require a boundary, comparison, and horizon.

**Effective capacity** concerns what can actually occur under the conditions represented. Depending on the question, those conditions may include available means, information, timing, access and authority. Under fixed laws, complete future reachability satisfies \(\operatorname{Reach}(z')\subseteq\operatorname{Reach}(z)\) whenever \(z'\) is reachable from \(z\): concatenate the path to \(z'\) with any path from it. A tool can enlarge immediate or budget-limited executable capacity without enlarging that all-time reachability set. This prevents an equivocation in “opening possibilities.”

Models requiring continuing duties are totalized: failure, denied action, exhaustion, or deadlock has an explicit successor, usually a failure sink. Finite projects can instead have legitimate terminal outcomes. A formal absorbing terminal state does not claim that physical activity continues there.

## F1 Boundary consistency and conditional autonomy

Let a finite collection of sites obey

\[
\dot x_i=s_i+\sum_j j_{ij},\qquad j_{ij}=-j_{ji}.
\]

For any subset \(S\), with \(X_S=\sum_{i\in S}x_i\),

\[
\dot X_S=\sum_{i\in S}s_i+
\sum_{i\in S,\,j\notin S}j_{ij}.
\tag{F1.1}
\]

**Proof.** Sum the site equations. Every internal current has the oppositely signed partner, so internal terms cancel. All remaining transfers cross the boundary. Summing this identity over disjoint regions reproduces the identity for their union. ∎

For symmetric exchange \(j_{ij}=w_{ij}(x_j-x_i)\), \(w_{ij}=w_{ji}\ge0\), and no source terms, a proper region has an autonomous exact vector equation \(\dot x_S=f_S(x_S)\) valid for all nonnegative preparations iff all crossing weights vanish.

**Proof.** With no crossing weight, internal equations close. If \(w_{ij}>0\) crosses the boundary, hold every internal coordinate fixed and vary \(x_j\). The derivative of internal coordinate \(i\) changes. No single function of the fixed internal vector can supply both derivatives. ∎

**Scope.** This is an exact dependence result for this exchange class, not a proof of universal direct interconnection. Approximate autonomy, fixed exterior conditions, and other laws require separate analysis. A zero current at equilibrium does not prove independence under intervention. Conservation accounting does not prove predictive closure of the aggregate. Source: [S2](../history/SOURCE-MAP.md).

## F2 Renewal is a prefix condition

Let \(C\) be absolutely continuous with \(\dot C=R-L\) almost everywhere, and require \(C(t)\ge c\). Then this requirement on \([0,T]\) is equivalent to

\[
\int_0^t(R-L)\,ds\ge c-C(0)
\quad\text{for every }t\in[0,T].
\tag{F2.1}
\]

**Proof.** Integrate the differential identity. Both implications are immediate. ∎

If \(L-R\ge\delta>0\) while operation continues and initial slack is \(C(0)-c\), the floor is reached by time \((C(0)-c)/\delta\). Continued loss beyond that point violates the floor. If total indispensable loss diverges while initial stock and cumulative provision remain finite, indefinite operation above the floor is impossible.

For a discrete quantity obeying the same balance law, every prefix must leave at least the required amount available. A later addition cannot make an earlier operation feasible. Storage limits, conversion losses and unavailable reserves can impose further restrictions.

**Counterexample to averages alone.** Begin with one unit; an operation requires two before three more become available. The eventual total is sufficient, but the earlier operation is infeasible without an additional timely supply or the possibility of delaying the operation. Adding either changes the model. Source: [S5, S8](../history/SOURCE-MAP.md).

### F2a Recurrent provision in a finite support network

For finitely many tracked capacities, suppose

\[
C_i(t)=C_i(0)+E_i(t)+\sum_jR_{ji}(t)-L_i(t)\ge0.
\]

Initial stocks are finite. Cumulative external provision \(E_i\), internal provision \(R_{ji}\), and losses \(L_i\) are nonnegative, nondecreasing, and finite on bounded intervals. Assume **productive vulnerability**: any internal supplier delivering unbounded cumulative service itself incurs unbounded loss of a tracked capacity.

Then every node with unbounded loss is downstream of an unbounded external supplier or a directed cycle of unbounded internal provision.

**Proof.** Unbounded loss requires unbounded total provision by the balance identity. With finitely many inputs, some input is unbounded. If it is external, stop. Otherwise productive vulnerability applies to the supplying node, and the argument repeats backward. In a finite graph this chain reaches an external source or repeats a node, yielding the stated cycle. ∎

For another useful version, suppose each instance of support type \(i\) lasts at most \(\tau_i\), every later instance needs a still-functioning permitted parent, no organizational instances arrive externally, and the finite type graph is acyclic. Topological induction bounds the last possible expiry of type \(i\) by

\[
d_i=\tau_i+\max(\{0\}\cup\{d_j:j\to i\}).
\]

All supports disappear by \(\max_i d_i\le\sum_i\tau_i\). A cycle avoids this particular obstruction but can still fail through insufficient rates or resources. Infinite acyclic succession, perfectly durable providers, summable losses, or continuing external provision violate different assumptions. Source: [S5](../history/SOURCE-MAP.md).

### F2b Joint sustainable capacity and a failure deadline

Let protected margins \(v\ge0\) and typed reserves \(b\ge0\) obey

\[
\dot v=Mu-\rho(v),\qquad \dot b=p-Qu.
\]

The actually implementable fixed activity set \(U\) is nonempty, compact, and convex; every constant activity in it is executable. Matrices \(M,Q\) and inflow \(p\) are fixed. The locally Lipschitz loss law obeys \(\rho_i(v)\ge r_i\) throughout the safe orthant and equals \(r_i\) whenever \(v_i=0\). Initial margins and reserves are finite. All modeled evolution is well posed.

Define

\[
\mathcal F=\{u\in U:Mu\ge r,\ Qu\le p\}.
\tag{F2.2}
\]

**Theorem.** Indefinite protection from any finite safe initial state is possible iff \(\mathcal F\ne\varnothing\). If it is empty, no adaptive activity policy can protect indefinitely from any finite safe initial state.

**Proof.** A constant member of \(\mathcal F\) gives inward or tangent derivatives at every protected face and nonnegative reserve derivatives, so the safe orthant is invariant. Conversely, integration of a safe trajectory through \(T\) gives

\[
M\bar u_T\ge r-v(0)/T,\qquad Q\bar u_T\le p+b(0)/T.
\]

Convexity puts the time average in \(U\). Compactness supplies a convergent subsequence as \(T\to\infty\); its limit belongs to \(\mathcal F\). ∎

If \(\mathcal F\) is empty, convex separation gives nonnegative \(\lambda,\mu\), not both zero, and

\[
\beta=\min_{u\in U}\{
\lambda^\top(r-Mu)+\mu^\top(Qu-p)\}>0.
\]

The weighted available margin \(W=\lambda^\top v+\mu^\top b\) satisfies \(\dot W\le-\beta\). Every safe duration therefore obeys

\[
T\le\frac{\lambda^\top v(0)+\mu^\top b(0)}{\beta}.
\tag{F2.3}
\]

The multipliers identify a joint shortage; they are not ethical weights assigning the relative worth of participants. For example, with two losses \(2/5\), \(u_1+u_2\le1\), inflow \(3/5\), and resource use \(u_1+u_2\), total margin declines at rate \(1/5\). Initial margins \((1/10,1/10)\) and reserve \(1/5\) give duration at most two. Constant \(u_1=u_2=7/20\) attains two. Each function is sustainable alone; both together are not.

The theorem requires real convex implementability. If only \((1,0)\) or \((0,1)\) is executable, it cannot grant the midpoint as a simultaneous action at zero margins. State-dependent access and nonuniform minimum loss also require different analysis. Source: [S5](../history/SOURCE-MAP.md).

## F3 Formation of a maintained regenerative organization

Let \(a,b,k>0\), \(R,C,D\ge0\), and

\[
\dot R=kCD-aR,\quad \dot C=aR-bC,\quad \dot D=bC-kCD.
\tag{F3.1}
\]

The nonnegative simplex \(R+C+D=M\) is invariant. The boundary derivatives are inward or tangent, and the sum of derivatives is zero; bounded polynomial dynamics give global forward existence.

Write \(d_*=b/k\). Direct integration yields

\[
D(t)-d_*=[D(0)-d_*]\exp\left[-k\int_0^t C(s)\,ds\right].
\tag{F3.2}
\]

Hence \(D\) is monotone toward \(d_*\), without crossing, and has a limit \(\ell\). Since

\[
\dot C=a(M-D)-(a+b)C,
\]

the variation-of-constants formula gives

\[
C(t)\longrightarrow\frac a{a+b}(M-\ell).
\tag{F3.3}
\]

**Theorem.** If \(M>d_*\) and \(R(0)+C(0)>0\), every such solution converges to

\[
\left(\frac b{a+b}(M-d_*),\frac a{a+b}(M-d_*),d_*\right).
\tag{F3.4}
\]

If \(M\le d_*\), all solutions converge to \((0,0,M)\). The all-degraded initial state remains fixed at any \(M\).

**Proof.** Above threshold with active initial material, both \(D(0)\) and \(d_*\) are below \(M\). Thus \(\ell<M\), and (F3.3) gives a positive limit for \(C\). If \(\ell\ne d_*\), \(\dot D=kC(d_*-D)\) converges to a nonzero constant, contradicting convergence of \(D\). Hence \(\ell=d_*\). Below or at threshold, \(D\) increases with limit at most \(M\). If \(\ell<M\), then \(C\) has a positive limit and \(b-k\ell>0\); again \(\dot D\) has a positive limiting value, a contradiction. Thus \(\ell=M\). Conservation supplies the remaining coordinate limits. ∎

If \(C(0)=0<R(0)\), then \(\dot C(0)>0\): machinery forms without a machinery seed. At a positive equilibrium, the Jacobian in coordinates \((C,D)\) is

\[
\begin{pmatrix}-(a+b)&-a\\0&-kC_*\end{pmatrix}.
\]

Both eigenvalues are negative, and the slower one approaches zero at the threshold. Formation and regulation are consequences of the stated reactions. Their availability and energetic driving are premises.

**Finite energy bound.** Replace \(kCD\) by any nonnegative recycling flux \(J\) that consumes reserve \(E\ge0\) at rate \(\varepsilon J\), where \(\varepsilon>0\): \(\dot E=-\varepsilon J\), with no replenishment. Then

\[
\frac{d}{dt}(R+C+E/\varepsilon)=-bC,
\quad
b\int_0^T C\,dt\le R(0)+C(0)+E(0)/\varepsilon.
\tag{F3.5}
\]

This rules out unbounded cumulative machinery activity and therefore any positive long-run average maintained indefinitely by finite work supply. Activity can remain positive at every finite time while declining fast enough to have a finite integral. The result is resource accounting, not a complete thermodynamic derivation. Source: [S3](../history/SOURCE-MAP.md).

## F4 A uniform obstruction to endogenous renewal

Let \(z(t)\ge0\) satisfy componentwise

\[
\dot z\le(B-L)z,
\]

where \(B\ge0\) is constant and \(L\) is positive diagonal. There is no independent additive supply. If \(\rho(L^{-1}B)<1\), set

\[
w^\top=\mathbf1^\top(L-B)^{-1}>0.
\]

The inverse exists and is nonnegative because

\[
(L-B)^{-1}=\sum_{n\ge0}(L^{-1}B)^nL^{-1}.
\]

It follows that

\[
\frac{d}{dt}(w^\top z)\le-\mathbf1^\top z
\le-\frac{w^\top z}{\max_iw_i}.
\tag{F4.1}
\]

Thus all capacities decay exponentially, and

\[
\int_0^\infty\mathbf1^\top z\,dt\le w^\top z(0).
\tag{F4.2}
\]

**Proof.** Multiply the componentwise bound by \(w^\top\), use \(w^\top(L-B)=\mathbf1^\top\), and integrate the scalar differential inequality. ∎

If the production graph is acyclic, its weighted adjacency is permutation-triangular with zero diagonal, so \(L^{-1}B\) is nilpotent and has spectral radius zero. A productive cycle is necessary for endogenous persistence **in this class**. Multiple cycles can combine; no separate cycle-gain test has been proved here. For the reaction model, the global upper-bound matrix gives \(\rho(L^{-1}B)=\sqrt{kM/b}\).

An additive source \(s(t)\) adds \(\int w^\top s\) to the integrated budget. A subcritical local linearization cannot replace the global inequality. Supercritical gain alone does not ensure boundedness, a positive equilibrium, or attraction. Source: [S3](../history/SOURCE-MAP.md).

## F5 Faithful questions and the limits of compression

Let \(H\) be histories and \(\mathscr R:H\to Y\) the complete response profile for a declared question family. Define \(h\sim h'\) iff \(\mathscr R(h)=\mathscr R(h')\).

**Minimality.** The quotient \(H/{\sim}\) is an exact representation of these profiles, and every other exact deterministic representation \(s:H\to Z\) admits a well-defined map from its image onto this quotient.

**Proof.** Exactness means \(\mathscr R=d\circ s\) for a decoder \(d\). If \(s(h)=s(h')\), the response profiles are equal, so the histories belong to the same equivalence class. Therefore \(s(h)\mapsto[h]\) is well-defined and surjective on classes. Conversely the quotient decodes to \(\mathscr R\) by construction. ∎

This is informational minimality for fixed questions. It is not necessarily minimum computation, description length, storage in bytes, or a finite recursive representation. Recursive updating additionally requires that equivalent histories have compatible next-action meanings and equivalent updated classes after corresponding observations. A causal intervention profile must preserve actions, output laws, resource consequences, and relevant histories—not just one current prediction.

**Question expansion.** If \(s(h)=s(h')\) but a new question \(q\) has \(q(h)\ne q(h')\), no decoder using only \(s\) can answer \(q\) exactly on both. This does not imply every omission matters or that raw retention is always best. New evidence, a different interface, or an enriched summary may remove the obstruction at a cost.

**Decision adequacy.** For a finite family of situations merged into representation value \(r\), a single action is exactly optimal in every situation iff

\[
\bigcap_{m:\,s(m)=r}\operatorname*{argmin}_a L_m(a)\ne\varnothing.
\tag{F5.1}
\]

The condition is simply that an action can be chosen from the common set of minimizers. Exact identification of every loss is stronger than needed. Randomization can change regret or risk objectives, but cannot attain simultaneous exact minima with an empty common minimizing support.

Historical questions have their own profiles: identical present state and future behavior need not identify past continuity or ancestry. Records or tracers must carry that information. Sources: [S1, S5–S7](../history/SOURCE-MAP.md). Closely related minimal predictive representations are established in [Shalizi and Crutchfield](https://arxiv.org/abs/cond-mat/9907176).

**Later relational witness.** The [mixing diagnostic](../../../_process/history/2026-10-05-support-and-shared-generativity/completion/REPEATED-RENEWAL-COMPOSITION.md#7-a-source-anchored-transfer-consequence-mixing-has-no-fixed-sign) gives identical separate species distributions with different joint arrangements and opposite responses to complete mixing in a stated low-occupancy regime. The missing relation matters to the declared co-occupancy task. This conditional transfer-model example supports F5's representation requirement; it neither demonstrates learning of that distinction nor establishes biological renewal.

## F6 Consequential differences must reach action

Suppose two admissible worlds produce the same accessible history for a deterministic causal controller up to a decision deadline. Suppose their sets of safe immediate actions are disjoint, and no admissible safe probe can distinguish them before that deadline. No policy based on those histories guarantees safety in both.

**Proof.** The controller makes the same decision at the identical history. The decision belongs to at most one of the disjoint safe sets. For a randomized controller, sure protection requires its action support to lie in their intersection, which is empty. ∎

The quantifier distinction is

\[
\forall m\ \exists\pi_m\quad\not\Rightarrow\quad
\exists\pi\ \forall m.
\tag{F6.1}
\]

This is a counterexample template, not a claim that every uncertain problem is insoluble. A common safe action, more time, a reversible probe, an informative anchor, or a change in requirements can remove a premise.

**Aggregate-feedback example.** In the exact linear plant

\[
\dot e=aIe-Hu,\quad y=e_1+e_2,\quad a>0,
\]

take two initial states differing by \(\epsilon(1,-1)\), with identical controller memory. Equal commands preserve the difference \(\delta e(t)=\epsilon e^{at}(1,-1)\) and equal measured sums. By causal well-posedness the identical histories induce those equal commands. Both trajectories cannot approach the same target. No deterministic causal controller restricted to that measurement can stabilize every nearby state.

For the specific two-mode response law

\[
\dot e=ae-bu,\quad
\dot u=\kappa(P_++hP_-)e-\gamma u,
\]

where \(P_+\) and \(P_-\) project onto common and difference modes, \(g=b\kappa\), and \(h\ge0\), the mode polynomials are

\[
\lambda^2+(\gamma-a)\lambda+g-a\gamma,
\quad
\lambda^2+(\gamma-a)\lambda+gh-a\gamma.
\]

The quadratic stability criterion gives asymptotic, equivalently exponential, stability exactly when

\[
\gamma>a,\quad g>a\gamma,\quad gh>a\gamma.
\tag{F6.2}
\]

Observation, routing, actuation gain, and timing all matter. The specific law does not explain how the channel forms or obtains the means its operation requires. An unobservable stable mode need not be reconstructed to stabilize the relevant system. Sources: [S3, S6–S7](../history/SOURCE-MAP.md).

## F7 Funding a recurring correction process

Use the finite protocol in [S4](../history/SOURCE-MAP.md). Production is ten per round while shared support remains at least two. Both rules replenish its two units of wear, reserve \(f\) for a corrective carrier, and leave the participant three under F or one under X. The participant consumes two per round, has cap six, and must end each round with at least one.

X is selected without a binding mandate. File at reserve at most four when X is active; filing costs the participant one, and two X rounds including the filing round precede restoration. F then operates until reserve six, when the mandate ends. The carrier pays one upkeep before each production and two more when filing occurs. If upkeep fails, its gate ceases to work. Current ordinary needs can use current allocation; filing and carrier bills are prefunded. There is no borrowing or automatic reconstruction of a failed carrier.

From participant reserve six, the cycle is

\[
(6,5,4,2,1,2,3,4,5,6).
\tag{F7.1}
\]

There are four X rounds and five F rounds: participant receipts are nineteen, ordinary consumption eighteen, and filing cost one. The participant returns to the actual initial reserve without a reset subsidy.

**Recurring finance.** Every completed cycle costs the carrier eleven and receives \(9f\). If \(f<11/9\), each successful cycle spends a fixed positive deficit; a finite starting reserve cannot fund infinitely many. Conversely at \(f=11/9\), cap three and reserve three before filing sustain the cycle: filing leaves \(11/9\) after current receipt, and the following eight ordinary rounds each add \(2/9\), restoring three before the next claim.

**Liquidity.** A filing requires three prefunded units, so \(K\ge3\). From the stated initial phase, two ordinary rounds precede the first filing. At the threshold, the least sufficient initial reserve is \(3-4/9=23/9\). Starting lower cannot pay the claim when required; delaying it breaches the participant floor under this protocol.

**Delay.** If filing occurs at reserve \(h\), costs \(c\), and there are \(d\ge1\) integer X rounds including the filing round before restoration, the minimum reserve is \(h-c-d\). Thus the participant floor one requires

\[
h\ge1+c+d.
\tag{F7.2}
\]

The main example meets equality. Earlier filing at five improves the floor but gives a seven-round cycle, requiring \(f\ge9/7\). These are protocol-specific sharp thresholds, not an optimum over all institutions.

The prefunded bills, storage cap, trigger, release rule, initial phase, supplied funding stream, and binding authority are all load-bearing. A permanent effective F rule could avoid claims; its selection and maintenance would be a different model. Production can persist while the participant is lost, so the protection premise cannot be inferred from productive necessity.

## F8 Exact finite feasibility under actual information

Let a finite model have a finite set of possible information states \(\mathcal I\). Include in the physical state all finite memory needed for Markov transitions, resources, deadlines, persistent uncertain model labels, and obligations. Let \(S\subseteq\mathcal I\) contain exactly those information states whose compatible physical states satisfy the protection requirement. Let \(A(I)\) be the implemented action set under the common information, with unsuccessful attempts represented rather than erased.

Here \(I\) is the exact observation-history compatibility set, or a proved sufficient equivalent, and action availability depends only on this represented information. Let \(\operatorname{Post}(I,a,o)\) be exactly the compatible successors after action \(a\) and possible observation \(o\), with updates determined by \(I,a,o\). Initial-state uncertainty and disturbance updates must preserve the declared model's temporal dependence. Impossible observations have empty successor sets and are ignored. Any relevant intermediate unsafe microstep must be explicitly represented or excluded by a proved prefix contract. Conservative overapproximations support a sufficient certificate but generally lose the necessity direction of the theorem below.

Set

\[
W_0=S,\qquad
W_{n+1}=\{I\in W_n:\exists a\in A(I),\ 
\forall o\text{ possible},\ \operatorname{Post}(I,a,o)\in W_n\}.
\tag{F8.1}
\]

**Theorem.** The stabilized finite fixed point \(W_*\) consists exactly of information states from which an observation-admissible policy guarantees indefinite safety against all admitted outcomes.

**Proof.** At each retained information state choose a witnessing action. Every successor remains in \(W_*\subseteq S\), so induction gives safety. For necessity, induction on \(n\) shows that every state removed by stage \(n\) lacks a policy safe through the corresponding finite horizon: every available first action has some possible successor already losing at a shorter horizon. A state admitting perpetual safety could never be removed. Finiteness makes iteration terminate. ∎

For horizon \(H\) and terminal obligations \(T_H\), use \(W_H=S_H\cap T_H\) and the analogous backward recursion. Optimization of a specified cost over retained actions is a separate conditional dynamic program. The policy must be implemented; computing it does not establish adoption.

This theorem is for one implemented information architecture. It does not turn a decentralized problem into a centralized one by granting actors each other's private observations. Safety also does not entail recurring service, discovery, fairness, or ethical legitimacy. Sources: [S5–S8](../history/SOURCE-MAP.md); related safety-learning work includes [Moldovan and Abbeel](https://arxiv.org/abs/1205.4810) and [Heim and colleagues](https://proceedings.mlr.press/v100/heim20a.html).

For the claim about physical execution, the exact information-state update and witnessing action table must be implementable within the declared memory, computation, and resource interface. If these operations and their enabling conditions have not been represented, the theorem characterizes abstract observation-history feasibility only. A proof of finite memory does not show how its carrier forms or is maintained.

## F9 The joint installed process including its own revision

Fix the actual controller or interacting controllers, their real information restrictions, and their revision mechanism. Write the total installed transition relation

\[
z\xrightarrow{\gamma}z',
\]

where the label \(\gamma\) records actual delivered events, resource effects, and elapsed time. Code, evaluators, representations, carriers, and rule versions may be coordinates of \(z\) and change through these transitions. Their interpretation must change the operative behavior when relevant. An unused variable named “revision” supplies no mechanism.

Let \(B\) be the initial set, \(K\) the independently specified acceptable set, and \(E_1,\ldots,E_q\) required **transition events**. Require every admitted run to remain in \(K\) and each \(E_j\) to occur infinitely often. Recurrence is imposed only where the duty actually calls for it; many legitimate finite tasks or dormant functions do not.

**Finite installed-process theorem.** If the reachable graph is finite, the requirement holds iff there is a set \(A\) and natural-number ranks \(r_j\) satisfying

\[
B\subseteq A\subseteq K,
\quad
z\in A\land z\xrightarrow{\gamma}z'\Rightarrow z'\in A,
\tag{F9.1}
\]

\[
z\in A\land z\xrightarrow{\gamma}z'\land\neg E_j(\gamma)
\Rightarrow r_j(z')<r_j(z).
\tag{F9.2}
\]

Ranks may reset or increase when their event occurs. They are proof witnesses, not free information supplied to the controller.

**Sufficiency.** Closure and containment give safety by induction. If an event occurred only finitely often, every transition after its final occurrence would strictly decrease a natural number. This is impossible indefinitely. The argument applies separately to each event within the same joint process. ∎

**Necessity.** Take \(A\) to be the reachable states; it is closed and safe. For each \(j\), retain the edges with a label not delivering \(E_j\). This graph has no directed cycle, since a reachable cycle could be repeated forever without delivering that event. Its longest-path lengths supply decreasing natural-number ranks. Parallel transitions with identical endpoints must retain their different labels: an event-free alternative cannot be discarded because another edge delivers the event. ∎

The equivalent finite algorithm checks all reachable states for safety and each event-free graph for cycles. Recurrence here is counted in transitions; its interpretation as indefinitely continuing physical activity additionally requires that the elapsed durations sum to infinity on every infinite run. In an infinite state space the semantic counterpart uses ordinal ranks and well-founded relations; it need not be effectively computable or give a uniform finite latency bound. The source proves that more general result. This synthesis's executable checks concern finite examples.

**Joint composition.** If local transition rules cover every actual transition—including disturbances, denial, replacement, and revision—and each preserves one common invariant and decreases the relevant ranks on its event-free transitions, their union satisfies the theorem. The invariant must include shared resource and permission compatibility. A pair of individually safe policies requiring the same last resource unit is not a joint policy.

This provides the formal bridge among regeneration, inquiry, selection, and succession. It certifies the process that actually carries the obligations through its changes. It does not infer success from the existence of a different good controller, and it does not prove that the installed rule or ethical specification is legitimate. Sources: [S5, S8](../history/SOURCE-MAP.md). Compositional invariant reasoning has established precedent in [Chen and colleagues](https://arxiv.org/abs/1810.10636).

## F10 Stable regeneration and indefinite survival are different

Consider the finite continuous-time particle version of (F3.1), with total count \(N\) in volume \(V\) and reaction rates

\[
a n_R,\qquad b n_C,\qquad (k/V)n_Cn_D.
\]

The all-degraded state \((0,0,N)\) is absorbing. Every other state reaches it with positive probability through a finite sequence that first assembles remaining usable material, then wears all machinery, with no intervening recycling. The chain is finite and has no other closed class. Therefore it reaches that absorbing state almost surely with finite expected absorption time.

The deterministic concentration approximation and the infinite-time limit of a finite particle system are different limits. The deterministic attractor does not establish permanent finite-population survival. Immigration or a powered spontaneous reactivation route would change the premise. No lifetime-scaling theorem is claimed here. Source: [S3](../history/SOURCE-MAP.md).

More generally, if every safe history has conditional probability at least \(p>0\) of failure within the next \(m\) steps, then

\[
\Pr(T>km)\le(1-p)^k.
\tag{F10.1}
\]

**Proof.** Condition successively on survival to each block boundary and apply the uniform bound. Independence between blocks is unnecessary; the uniform conditional bound is the sufficient hypothesis used. ∎

Large reserves or small \(p\) can support high finite-horizon reliability while the infinite-horizon probability is zero. Conversely, a finite stochastic chain's almost-sure recurring event may admit an event-free infinite path of probability zero, so the sure-rank criterion in F9 is stronger.

<a id="f11-succession-must-finance-the-delivered-next-state"></a>

## F11 Succession must sustain the delivered next state

Let \(Z\) be finite delivered configurations, \(Q\) finite nonempty task sets, and \(A(z,q)\) finite feasible response options. The task is announced before its response is chosen. Option \(a\) has peak required reserve \(c(z,q,a)\ge0\), net expenditure \(d(z,q,a)\) after actual receipts, and successor configuration \(f(z,q,a)\). Receipts' timing is included in the peak; no hidden credit is granted. An empty action set means impossibility. Assume these summaries faithfully encode every within-episode prefix and no capacity cap or resource-dependent option has been omitted.

The delivered configuration \(z\) is observed by the selecting actor, or is an exact implementable information state for this decision. Each listed option is executable at reserve \(r\) exactly when \(r\ge c\), and leaves reserve \(r-d\) and delivered configuration \(f\). The selector and any memory or computation it needs belong to the stated executable options. Hidden-state choices or additional reserve-dependent restrictions would invalidate this recurrence unless included in the state and option summaries.

Set \(H_0(z)=0\). The minimum reserve for \(n+1\) episodes against every admitted task sequence is

\[
H_{n+1}(z)=\max_q\min_{a\in A(z,q)}
\max\{c(z,q,a),\ d(z,q,a)+H_n(f(z,q,a)),\ 0\}.
\tag{F11.1}
\]

**Proof.** With current reserve \(r\), the current response requires \(r\ge c\). It leaves \(r-d\), which must be at least the successor's required reserve. Thus precisely the inner maximum is needed for that option. Choose the cheapest admissible option after the observed task; the worst task supplies the outer maximum. Induct from the empty duty. ∎

The sequence is nondecreasing. In the finite-action setting, the limit \(H_\infty\in[0,\infty]^Z\) satisfies the same recurrence, because finite minima and maxima commute with monotone limits. Wherever it is finite, choose a minimizing option and maintain \(r\ge H_\infty(z)\). The inner inequalities ensure sufficient reserves throughout the episode and leave \(r-d\ge H_\infty(f)\). This is an inductive indefinite-succession certificate, assuming infinitely many episodes cannot finish in finite physical time. If \(H_\infty(z)=\infty\), no finite initial reserve satisfies all finite horizons and hence none guarantees every infinite task sequence.

**Example.** Both processes start with nine units of reserve, consume five in producing the first answer and transferring the resulting state, and receive three afterward. A process requiring five units each time has post-episode reserves of seven, five, three; it cannot begin a fourth episode. A process delivering an interface whose later episodes require three units continues at reserve seven with replenishment of three each time. First answer, first consumption, and supply match. The delivered successor configuration differs.

The example's costs are stipulated; it is not a fit to the separate circuit experiment. Stochastic tasks, observation before or after task disclosure, storage limits, or infinite action repertoires require different analysis. Source: [S9](../history/SOURCE-MAP.md).

**Later stochastic composition.** The [repeated-renewal result](../../../_process/history/2026-10-05-support-and-shared-generativity/completion/REPEATED-RENEWAL-COMPOSITION.md) supplies a separate extension for an installed stochastic process: a successful-cycle measure retains the actual successor, elapsed time and charged expenditure, and its conditional recursion gives finite repeated-task probabilities. Equal one-cycle success totals can conceal different continuations. Its source, information, closure and every-prefix feasibility assumptions remain explicit; it does not change F11's deterministic task-choice quantifiers or supply reliable physical renewal by itself.

<a id="f12-limits-of-a-universal-ranking-and-a-complete-evaluator"></a>

## F12 Scope of task rankings and limits of complete evaluation

**Opposing task rankings.** Suppose at the same budget method A succeeds on some task that D fails, while D succeeds on another that A fails. A next-task distribution concentrated on the first ranks A above D; one concentrated on the second reverses the ranking. No fixed strict ordering or tie preserves both task-dependent success comparisons. The result concerns an ordering required to reproduce every such comparison while omitting its task conditions. It does not exclude a universal criterion applied to whole generative situations or justify any particular criterion. The matched inheritance experiment supplies exactly the task-ranking premise. [S9](../history/SOURCE-MAP.md)

**Joint requirements.** Policies with consequence vectors \((1,0,0),(0,1,0),(0,0,1)\) can meet any pair of zero-loss demands, but cannot make all three losses at most \(0.3\), even with randomization: their sum is always one. Pairwise compatibility is weaker than joint feasibility. A convex separation certificate can establish infeasibility in its appropriate finite model; it does not settle whose requirement should change. [S13](../history/SOURCE-MAP.md); established multiobjective verification is treated by [Etessami and colleagues](https://arxiv.org/abs/0810.5728).

**Unrestricted representation.** For any transition relation \(T\), set \(J(x)=\{y:xTy\}\) and let enactment select a member. This generic schema represents both continuing and terminating processes. A property that fails for an admitted relation cannot be derived from the schema's expressiveness alone. A substantive theory must constrain its mechanisms or independently justify its application. [S8](../history/SOURCE-MAP.md)

**Unrestricted effective completeness.** Given a program, build a deterministic process that simulates one computation step per transition and enters failure when the program halts. A terminating exact algorithm deciding perpetual safety for every such process would decide nonhalting and hence halting. The diagonal contradiction rules out such an algorithm. Finite-state exact methods, incomplete sound certificates, and a general semantic theory remain possible. This theorem is a limit on a combination of scope, exactness, and guaranteed computation; it is not a proof that no universal explanatory theory can exist. [S8](../history/SOURCE-MAP.md)

**Finite evidence and indefinite futures.** Over unrestricted transition laws, a fixed finite eventful record is compatible with a continuation law that later stops and another that continues. Infinite continuation needs additional structural assumptions or a certificate for a known law; it cannot be inferred solely from the record's length. A verified recurring cycle in a known finite deterministic system is a different case.

## F13 Faithful implementation joins models without changing their questions

Suppose an abstract action is implemented by a concrete causal procedure using only the corresponding available observations. At every reachable concrete state and relevant procedure memory, require that the procedure terminates, has sufficient resources and respects the protected conditions at every intermediate stage, meets its deadline, and matches the abstract joint response in successor state, observations, delivered events, costs, and elapsed time. Use equality of probability laws for probabilistic claims, or a proved path-preserving relation for sure claims. Include the actual actor's decision and any refusal or environmental choice in the correspondence.

Then every admissible abstract policy lifts to a concrete policy with the same retained responses and guarantees.

**Proof.** Replace each abstract decision with its implementing procedure. It is causally executable by assumption. At each boundary the joint-response correspondence preserves the information available to the next decision and the monitored consequences. Induction gives the correspondence at every finite prefix. For supported infinite paths, the stated path correspondence and nonaccumulating physical time preserve the continuing claim. For stochastic processes, consistent finite-dimensional laws determine the corresponding measurable path law under the usual path-space assumptions. ∎

A reverse causal implementation correspondence gives equality of attainable response sets and permits transferring impossibility statements. A one-way sound abstraction can supply useful sufficient policies while losing concrete alternatives; its failure need not imply concrete impossibility.

Matching separate marginals is insufficient when consequences depend on correlations. Matching successful endpoints is insufficient when an intermediate operation lacks the resources it requires. Matching ordinary trajectories is insufficient if the abstraction grants an outside planner a choice that is actually made by a refusing participant. These conditions are how separate models can be joined without silently changing the problem. Sources: [S5, S8](../history/SOURCE-MAP.md).

**Quantified finite stochastic approximation.** [Repeated-renewal composition R4](../../../_process/history/2026-10-05-support-and-shared-generativity/completion/REPEATED-RENEWAL-COMPOSITION.md#3-reliability-and-error-budgets) bounds finite-horizon success error by the formation error plus the accumulated uniform total-variation errors of the full marked continuation kernels, capped at one. Matching isolated success totals cannot supply those row bounds. This sharpens a particular stochastic interface without proving that the existing physical and strategic models satisfy it. The [integration review](../../../_process/history/2026-10-05-repository-reconciliation/three-session-integration/PHYSICAL-BRANCH-REVIEW.md) records the accepted scope.

<a id="f14-noninstrumental-patient-reasons-and-paid-response"></a>

## F14 Noninstrumental patient reasons and realizable response

**Joint-occurrence continuation, 6 October 2026.** The current [一体之仁 account](NONINSTRUMENTAL-CONCERN.md#一体之仁的生成解释) adds a complementary representation requirement to this historical contract. [CoupledOccurrence](../../../experiments/integrated-correction/general-framework/generative-basis/lean/CoupledOccurrence.lean) decorates each original step with a selected report of that same before/event/after occurrence. Decoration and erasure preserve the original traces; composition requires the actual shared intermediate state. [CoupledConcernHistory](../../../experiments/integrated-correction/general-framework/generative-basis/noninstrumental-concern/CoupledConcernHistory.lean) applies it to unchanged plasticity histories, including actual formed response, active/frozen feedback, unavailable readout and a transient-decrease obstruction for one specified endpoint/current-record summary. The reports are analyst descriptions; causal formation comes from the inherited law, and recipient stock is not identified with experience. [Mathematics and verification](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/YITI-REN-COFORMATION-MATH.md) distinguish this additive interface from proving ethical grounds or installing acquired target revision. The earlier C1/C2 results below retain their scope.

The [noninstrumental-concern extension](NONINSTRUMENTAL-CONCERN.md) adds an explicitly conditional ethical interpretation to the same `Generative.Process`/`Trace` core. It does not alter F1–F13 or infer ethical truth from the causal interface. The concrete realization has one responder, two separately indexed patients, a formed carrier, acquired packets, selected commands, current authority and a consumable fuel account. A packet retains the patient, episode, means version and observed content. Faithful reading, live condition checks, recipes and scheduling remain supplied.

Let \(c(s,i)\) be the patient condition in state \(s\). Keep `Realized`, `Bad` and `Merit` independently interpreted. The explicit contracts are

\[
\mathrm{C1}:\quad \mathrm{Realized}(c)\land c.\mathrm{burden}>0
\Rightarrow\mathrm{Bad}(c),
\qquad
\mathrm{C2}:\quad\mathrm{Bad}(c(s,i))\land\mathrm{Eligible}(s,i)
\Rightarrow\mathrm{Merit}(s,i).
\]

`Realized` must identify the independently warranted patient domain; positive numerical burden alone is not evidence of experience or badness. `Merit` concerns the available patient-directed option and is not defined to equal eligibility. C2 is the substantive, philosophically defended bridge to a contributory moral reason, not a theorem of C1 or of survival.

For this realization, eligibility provides a sufficient condition for a specified `servicePlan`: positive outstanding burden, permission, and fuel covering its remaining operations. The plan costs 6 before carrier formation, 4 with a carrier but no usable record, 3 with a usable stored record, and 2 with a usable selected command. These are exact costs of that plan. A theorem beginning at an arbitrary cached state does not certify how its cache was obtained; the explicit histories from an empty cache include the actual read and its fuel consumption. These costs are not asserted to be the minimum over all possible plans from arbitrary typed states; an injected cache before formation is a retained counterexample to that stronger claim.

**Conditional composition.** Under C1, C2, realized patient conditions and eligibility, the option has the stipulated moral merit and its specified plan has an actual trace. At the endpoint the same patient's modeled burden is zero, its episode identity is preserved, and endpoint fuel plus the fuel consumed by the plan equals the actual starting fuel. The conclusion is existence and conditional interpretation of this realizable response, not inevitable execution under every schedule or a complete ranking of all options.

**Proof.** C1 supplies the patient-local premise and C2 supplies merit. Case analysis on the carrier and usable cached stages constructs the remaining plan without charging completed stages again. Each step has the required incoming fuel, uses the preceding actual state and respects the current packet/authority guards. The final action changes the selected patient's burden while preserving the episode. Induction on the trace gives the exact account; the local law also instantiates the inherited `ResourceContinuation.SustainLaw`. The proof implementation and explicit witnesses are in the [Lean package](../../../experiments/integrated-correction/general-framework/generative-basis/noninstrumental-concern/README.md).

**Preservation and limits.** Changing only the private-reward metadata, prior-role flag or prior adoption flag preserves the patient condition, designated-plan eligibility and the baseline merit supplied by C2. This does not preserve every possible additional role-based reason, and the reward metadata is not usable fuel. Revoking permission or refusing an action preserves the patient condition but can block this operation. Changes to episode or means make the old packet unusable; restoring permission does not resurrect a retired selection. Lack of an acquired packet differs from an acquired report of zero burden. Two individually supported patient options can require more fuel than is available for their specified joint service sequence; no aggregate ranking or erased patient follows.

A second interpretation assigns the independent `Merit` relation false everywhere while preserving the causal process and a formal positive-burden interpretation. It violates C2 on an eligible case. This is an exact non-entailment witness for the listed causal and patient-local premises, not a demonstration that a fully adequate ethical theory may disregard patients. Conversely, the defined interpretation `candidateMerit` satisfies C2 by construction; it is a consistency witness, not independent evidence for C2. These two checks prevent the operational integration from masquerading as a proof of its ethical ground.

**F14 root-derivation audit, 6 October 2026.** The [subsequent proof attempt](NONINSTRUMENTAL-CONCERN.md#9-实际尝试从根基消除-c2) fixes a patient event while varying eligible execution positions. Universal baseline reasons are exactly equivalent to (i) at least one reason-bearing eligible position for every bad event having any eligible position, and (ii) reason preservation between eligible positions at that event. Event-only factorization is equivalent to (ii) and also permits all reasons to be false. The [new Lean module](../../../experiments/integrated-correction/general-framework/generative-basis/noninstrumental-concern/RootGrounding.lean) proves the exact adaptation to the existing C2: replacing that parameter with these two conditions relocates its content rather than discharging it. An actual empty-origin relation-record trace and a separate never-agent patient countermodel retain the distinction between generated relations, whole-history relabeling, event anchors and fixed-event substitution. Its service adapter additionally requires the same patient-event interpretation across local instances; it does not join their resources into one multi-actor history. These are dependency and countermodel results, not a proof of C1/C2 or an assumption-free root.

## F15 History-conditioned representation and orientation limits

The [existing Lean entry point](../../../experiments/integrated-correction/general-framework/generative-basis/lean/GenerativeModel.lean) now imports [GeneratedSelf](../../../experiments/integrated-correction/general-framework/generative-basis/lean/GeneratedSelf.lean) and [EthicalOrientation](../../../experiments/integrated-correction/general-framework/generative-basis/lean/EthicalOrientation.lean). They retain the original `Process` and `Trace` and add no primitive dynamics or ethical premise.

For a declared process and initial state, let `Residual P s h w := Feasible P s (h ++ w)`. A record `r` admits an interpreter exact for all finite residual futures iff `r h = r k` implies agreement of those futures. The reverse direction constructs an interpreter by existentially pooling histories with the same record; no choice axiom is needed. The result concerns an exact information contract, not its physical acquisition, decidability, cost or universal necessity for selfhood.

The already-defined toggle law reaches different endpoints after zero and one event while retaining identical residual profiles. Consequently a profile-only decoder cannot recover both phases. The same law has zero-event and two-event histories with the same endpoints and profiles; event-count ordering and its converse are coherent and annotation-independent but rank them oppositely. Coherence and annotation-independence therefore do not select a growth direction. This does not identify event count with morality or prove that richer ethical grounding is impossible.

Continuation inclusion is independently a factual preorder with synchronous-composition and exact-projection preservation. A toggle cycle also excludes strict transitive improvement on every allowed state transition, without excluding an evaluative distinction between actions.

The [integration record](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/SELF-FOUNDATION-LEAN-INTEGRATION.md) and [independent review](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/SELF-FOUNDATION-LEAN-REVIEW.md) accept 43 additions with empty axiom dependencies in a 14-module, 162-declaration build. F14 retains its separate C1/C2 contracts. Endogenous self formation, experiential realization and moral justification remain open; this section does not complete the assumption-free foundation.

**Outcome-sensitive extension.** [OutcomeContinuation](../../../experiments/integrated-correction/general-framework/generative-basis/lean/OutcomeContinuation.lean) retains a declared endpoint readout in the residual relation. Exact interpretation is equivalent to preserving all those readout distinctions; forgetting the readout recovers feasibility. The [native-record bridge](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/ACQUIRED-RECORD-INTEGRATION.md) proves that the existing predictor's score follows its actual write transcript and connects its readout to an enabled executed command. Thirty-two distinct added audits are empty across the structural and concrete checks. All earlier laws remain unchanged; supplied sensing/updating rules and independent ethical grounds remain open. This complements F16's action-effect interpretation and typed material ancestry without importing its inherited proof dependencies into the strict structural build.

**Receipt interpretation and temporal scope.** [The next extension](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/RECEIPT-IDENTIFICATION-INTEGRATION.md) proves exact identification under the unchanged action/receipt relation: success identifies the event-time regime; failure with unknown availability does not. A fixed-regime record is compatible exactly when its successful actions agree with that regime. In the actual guaranteed-availability process, every enabled event immediately after work must be write, deriving freshness for an actual next update. The same existing history later preserves memory through reversal and reaches opposed successes, refuting fixed-regime pooling. [GenerativeReceiptModel](../../../experiments/integrated-correction/general-framework/generative-basis/lean/GenerativeReceiptModel.lean) exposes this join through a separate 24-module build with 32 new empty-dependency audits. There is no liveness guarantee, installed partial controller, stochastic-law extension or derivation of the supplied receipt/guard law.

## F16 Acquired action-effect representation in the continuing organization

The [acquisition entry](../../../experiments/integrated-correction/general-framework/generative-basis/lean/GenerativeAcquisitionModel.lean) imports the F15 structural model and the unchanged material-backed prediction chain. Its local process already instantiates `Generative.Process`; composition preserves the actual intermediate states rather than reinitializing the learner.

The acquired finite score represents the two candidate-action receipts under the inherited noiseless binary law. A full typed-formation history reaches the installed learner. Its retained score becomes accurate, survives a regime change and becomes inaccurate. A reached record correction establishes exactness of both response-function forecasts, changes the next command and leaves the already executed action unchanged. The enabled next action obtains support; the subsequent record update and completion renew the same organization's time-limited support, called leases in this local model. Three entry theorems compose this continuation through the original material-backed final state.

This discharges a missing partial-representation/use interface, not the origin of the physical partition, decoder, writer, functional recipe or initial resources. The analytical two-action readout is not a claim that both alternatives can be executed from the same unchanged state. The actual command consumes the existing score. Recipient labels remain supplied in their separate comparison; no recipient history is silently joined to the actor's support history.

The [mechanism note](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/SELF-ACQUISITION-BRIDGE.md), [verification](../../../experiments/integrated-correction/general-framework/generative-basis/lean/acquired-perspective/verification.json) and [independent audit](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/COMPLETE-FOUNDATION-DERIVATION-AUDIT.md) record the result and inherited proof dependencies. No new axiom or physical law is introduced; concrete proofs retain standard dependencies from the original physical chain. The unchanged F15 check retains its empty-new-dependency guarantee.

The remaining formation bridge is acquired attribution of own/world effects without supplying the correct partition. The separate ethical bridge remains C1/C2: accurate representation and successful renewal do not establish patient badness or a response-directed reason. These limits preserve the no-assumptions requirement rather than declare the complete foundation attained.

## F17 Nondual descriptions and formed overlapping ranges

The existing `Process State Action` contains no primitive subject/object or actor/patient partition. The [nondual extension](../history/DEEPER-GENERATIVE-ROOT.md#10-nondual-core-and-derived-positions) develops that architecture without introducing an ethical premise into the core. Its generic module imports only `GenerativeCore`; the old patient-grounded contract connects to it through a separate downstream adapter.

Given a process \(P\) and a supplied description \(\rho:S\to D\), let \(\widehat S=\{(s,d)\mid d=\rho(s)\}\), and let a presented event hold precisely when it holds between the forgotten states. Then

\[
\operatorname{Trace}_{\widehat P}(\widehat s,w,\widehat t)
\iff \operatorname{Trace}_{P}(s,w,t).
\]

For the existing `OutcomeResidual` interface, transporting a declared endpoint observation by the same forgetting map also preserves every stated finite continuation/outcome question. The additive [public entry](../../../experiments/integrated-correction/general-framework/generative-basis/lean/GenerativeNondualModel.lean) imports `GenerativeOutcomeModel` unchanged and proves this connection. The `ActualHistory` carrier permits descriptions of realized start/word/end records with a `Trace` proof; it does not retain a separately readable sequence of hidden intermediate states or distinguish every nondeterministic branch. A role-report exactness criterion applies the inherited fiber criterion to a specified role/effect profile. These are conservative mathematical readouts, not acquired internal self-models.

A [conditional formation](../../../experiments/integrated-correction/general-framework/generative-basis/noninstrumental-concern/NondualFormation.lean) gives more than an arbitrary relabeling: initially absent connections form overlapping effective source ranges \(\{0,1\}\to3\) and \(\{1,2\}\to4\), actual events exercise both, and disconnecting indispensable links removes capability while preserving the post-event activation pattern. Repeating one source does not simulate two distinct contributors. A separate actual continuation connects site 3, previously affected, as a necessary contributor to site 4. Site identities, initial activation and link/pulse laws are supplied; the construction does not derive experience, an organism or a favorable orientation.

The downstream adapter proves that a situational ethical contract pulls back to role descriptions and reflects back when the relevant situations are covered. The legacy C2 is one such contract. This locates its assumptions in the extension; it does not establish their truth or eliminate their normative content. [Mathematics, checks and review](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/NONDUAL-CORE-INTEGRATION.md) distinguish this formal integration from a completed self/ethical foundation.

**Joint episode and core/tree rearticulation.** The [nondual continuation](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/CORE-TREE-CONTINUATION.md) now reconstructs the existing actual rent/work/write/finish trace with one receipt jointly governing retained revision, exact fuel effects and support renewal/depletion. A fixed enacted coupling cannot produce an independently flipped receipt under that law. Separately, the existing inquiry calculus admits constructive substitution of every reused branch by its original derivation: replacing a basis by its whole closed derived tree preserves all contextual conclusions, and arbitrary branch addition is conservative iff that branch was already closed-derivable. The additive [model entry](../../../experiments/integrated-correction/general-framework/generative-basis/lean/GenerativeCoreTreeModel.lean) preserves F15–F17 and exposes both scoped results. All eleven new audits are empty. The physical model does not thereby execute the proof calculus, and neither result proves a nondual ontology or completes formation of the sensing/update relationships.

## F18 Constructive sufficiency through transforming inquiry

The existing generative process admits an exact constructive criterion for a bounded inquiry followed by an executable response. A query transports every compatible configuration through its actual step before filtering its acquired outcome. It must be enabled for each candidate and preserve the declared intermediate condition on every successor. A terminal response is one finite action sequence, common to the remaining candidates, whose every prefix can continue and whose every admitted endpoint meets the requirement.

The [Lean theorem `sufficiency_iff_bounded_policy`](../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/InquirySufficiency.lean) equates the explicit empty/live-branch recurrence with existence of an independently defined finite policy at a fixed inquiry-depth bound. Actual execution remains a native trace, and separate theorems establish execution existence, endpoint adequacy and every-step preservation. Empty initial evidence is excluded. Exact finite candidate lists decide branch nonemptiness without a logical axiom; under bounded branch classification the constructive recurrence agrees with the older implication form.

The [public entry](../../../experiments/integrated-correction/general-framework/generative-basis/lean/GenerativeInquirySufficiencyModel.lean) passes 17 new empty-dependency audits in an 18-module build. [Mathematical scope](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/INQUIRY-SUFFICIENCY-LEAN-MATH.md) and [review](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/INQUIRY-SUFFICIENCY-LEAN-REVIEW.md) preserve a key limit: finite observation labels alone do not decide arbitrary predicate-valued branch nonemptiness. The theorem asserts no physical law, calibration, ethical goal or acquired stopping mechanism. These are conditional contracts within one changing process; an application must identify and justify them.

**Derived finite classification, 6 October 2026.** [FiniteInquiryClassification](../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/FiniteInquiryClassification.lean) constructs an exhaustive `Fin size` carrier and exact lists of all successors compatible with each acquired outcome. Executable transition and candidate membership yield branch classification at every finite depth. The Boolean-table specialization derives those decisions from its representation data, so the policy equivalence needs no supplied classification, coverage or decidability proof. It does not infer decidability from finite observation labels alone or justify truncating an unbounded native process. The [public finite entry](../../../experiments/integrated-correction/general-framework/generative-basis/lean/GenerativeFiniteInquiryModel.lean) extends the conservatively repaired core; all current audited dependencies are empty. [Integration and remaining premises](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/CONSTRUCTIVE-DEPENDENCY-REMOVAL-INTEGRATION.md) preserve the conditional interpretation and distinguish it from acquired criterion formation.

### Attainable questions within that same inquiry

[The constructive continuation](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/ATTAINABLE-QUESTIONS-LEAN-INTEGRATION.md) reuses `Policy`, native `After` and the progress/safety contract. Terminal-leaf agreement specifies which question the actual observation path identifies. Coarsening preserves attainability; one shared policy identifies two questions exactly when it identifies their common refinement. Two separately available policies supply no such implication. A missing refinement rules out any attainable common upper question, hence a greatest member in any question family containing that pair.

The one-packet comparison proves, for every answer function on retained initial labels A/B/C, that attainability is equivalent to `f B = f C ∨ f A = f C`. This covers arbitrary finite adaptive policies, common noninformative controls and depleted denials. Thus A? and B? are separately attainable while their join and C? are not. All source consumption and initial-target distinctions used in that argument are retained. Positive logical attainability in the permissive comparison is not a funded native-controller theorem.

Sequential composition is proved by attaching admissible inquiries to the first tree's actual reached leaves. Native progress and prefix conditions continue to hold; fixed-target preservation prevents a changed current question from replacing the initial one. The [public entry](../../../experiments/integrated-correction/general-framework/generative-basis/lean/GenerativeAttainableQuestionsModel.lean) passes 307 empty audits, including 80 additions. K2a's finite-family converse, full native refinement, arbitrary physical restoration and criterion formation retain their separate proof or application obligations.

### Deriving the inquiry certificates

[The next constructive continuation](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/DERIVED-INQUIRY-PREMISES.md) derives the finite application certificates rather than accepting them. For a sound prefix, the continued policy identifies the final question exactly when its actual reached-leaf continuations do. The prefix need not already identify it, and global agreement preservation is unnecessary. Historical-target use still requires preserving the original target; a concrete witness proves this along all admitted traces while falsifying the old global requirement.

An executable finite search now returns an actual policy and proof, or excludes every policy through the requested depth. Its composed interface also calculates initial nonemptiness and prefix soundness, searches each actual reached leaf, and certifies the final composite without supplied `live`, `first`, `later` or `preserved` proofs. Rejection concerns the specified prefix and per-leaf bound. The unchanged one-packet comparison uses a nontrivial packet-access condition; its exact all-finite-policy obstruction remains. Finite law/question data and physical correspondence remain explicit, and this does not install the search within the original apparatus or ground a query's ethical significance.

### Deriving the local process law

[The native-law continuation](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/PROCESS-LAW-DERIVATION.md) derives the calibrated one-packet probe interface from the preserved executable apparatus. Equality of native two-probe profiles is equivalent to equality of the represented A/B/C target class. Native completion is equivalent to sequential capacity, dispatch-funding, source and receipt-funding guards, with conversion and any actual arrival preceding receipt acquisition. For a known phase, at most two paid rotations and the completed probe form a native trace whose projected endpoint consumes the packet and whose calibrated receipt matches the macro response. The direct schedule guard is equivalent to the native prefix/probe guards; it is not an observable admission policy.

Source-zero denial in the old permissive comparison remains extra access; the native call cannot complete. A completed probe from twenty units leaves another packet, preserving the counterexample to extending the six-state projection. The [combined public entry](../../../experiments/integrated-correction/general-framework/generative-basis/lean/GenerativeDerivedProcessLawModel.lean) passes 599 empty-dependency audits. Its inherited cycle, transfer gate, tariff and physical calibration remain upstream explanatory inputs. Neither arbitrary macro-control realization nor assumption-free universal dynamics follows.

## The unified theorem and its precise force

Within a declared finite joint model, actual protected recurring operation has the exact installed-process certificate F9. Where selecting a controller is part of the task, F8 supplies the safety feasibility layer; recurring duties require their additional event conditions. F1 preserves dependencies across boundaries. F2 and F11 constrain resource availability through time and succession. F3–F4 demonstrate and limit endogenous renewal. F5–F6 constrain what a situated response can know and do. F7 embeds correction in its own continuing budget. F10 and F12 prevent the resulting certificates from being mistaken for unrestricted survival, universal value, or a complete effective account of all futures.

F13 states the implementation obligation when transferring these claims between representations. The unity is a composition with explicit interfaces and joint assumptions. It is neither a derivation of all these mechanisms from one empty transition symbol nor an empirical assertion that all actual systems satisfy their premises. Establishing the strongest physical and ethical interpretations remains a substantive research task.

F14 supplies a further patient-grounded interpretation and an implementation with specified fuel requirements under C1/C2. It makes this ethical interface part of the common formal account while preserving its additional premises, separate realization scope and unresolved stronger necessity. It is not an extra hidden premise of the preceding F1–F13 results.
