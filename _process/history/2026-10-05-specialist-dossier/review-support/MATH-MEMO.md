# Mathematical contribution memo for the specialist-review foundation

5 October 2026. Prepared by the mathematics-review subagent. This is a contribution and audit memo for the coordinating author, not independent human peer review. It separates exact results, assumptions, constructions, and substantive interpretation. No source files were edited.

## 1. What the combined mathematics can legitimately establish

The foundation has three distinct mathematical layers:

1. **Mechanism and balance:** specified events generate changing abundance, composition, support, and selectors. Exact balances constrain possible histories; conditional models exhibit collapse, renewal, thresholds, and multiple basins.
2. **Decision and implementation:** observations and actual action channels constrain timely safe control. Existence of a feasible policy differs from the behavior of the installed policy and the survival of its implementing conditions.
3. **Representation and transfer:** a proposed state must preserve the retained consequences of declared interventions. Structural dependency closure supplies a sufficient causal boundary; strong lumpability supplies an exact semantic test.

These layers can be joined in a finite monitored control model. The continuous examples do not automatically become special cases of that finite theorem: exact finite representability or an approximation bound is an additional obligation. Generality is a structural and conditional claim, not a derivation of every domain's laws or a proof of one uniquely necessary ontology.

## 2. Source audit and supporting results

The mathematical statements below were checked directly against:

- [Population and selection–renewal derivation](../../2026-10-04-integrated-evolution/integrated-dynamics.md).
- [Universal constraints](../../../../sources/15-codex-theory-conversations/2026-10-04-universal-constraints-and-maintained-correction.md).
- [Partial-observation safety and correction](../../2026-10-04-integrated-evolution/observability-and-correction.md).
- [Actual finite closure](../../../../experiments/integrated-correction/general-framework/closure-study/FORMAL.md).
- [Faithful quotient and finite grammar](../../../../experiments/integrated-correction/general-framework/generative-basis/formal/FORMAL.md).
- [Structural dependency closure](../../../../experiments/integrated-correction/general-framework/generative-basis/formal/STRUCTURAL-CLOSURE.md).

### 2.1 Event semantics precede selection equations

The supplied microscopic model has type counts \(X_i\), support state \(E\), and selector state \(S\). Birth of type \(j\) from type \(i\) occurs at rate \(X_i b_iQ_{ij}\); disappearance at \(X_id_i\); conversion \(i\to j\) at \(X_i k_{ij}\). Rates are nonnegative, \(Q\) is row stochastic, and \(k_{ii}=0\). Drift equations for \(E,S\), initial states, and regularity/nonexplosion conditions complete the process. Context-dependent rates make equations for expected counts generally unclosed.

Under a suitable density scaling and law-of-large-numbers hypotheses, the deterministic abundance model is

\[
\dot n_i=\sum_j n_jb_jQ_{ji}-n_id_i+
\sum_j(n_jk_{ji}-n_ik_{ij}).
\]

Do not describe this ODE as the exact expectation of the stochastic process without the necessary closure assumptions. Immigration, recombination, merging, and new type creation outside the represented catalogue need additional events.

For \(N=\sum_i n_i>0\), \(p_i=n_i/N\), and \(r_i=b_i-d_i\), summation and the quotient rule give exactly within this ODE:

\[
\dot N=N\bar r,
\quad
\dot p_i=p_i(r_i-\bar r)+\sum_jp_jb_j(Q_{ji}-\delta_{ji})
+\sum_j(p_jk_{ji}-p_ik_{ij}).
\]

For a differentiable contribution \(q_i\) to an independently identified support stock, write \(\dot E=R+N\bar q\). The product rule gives

\[
\dot{\bar q}=\operatorname{Cov}_p(q,r)+
\sum_i p_i\sum_j(b_iQ_{ij}+k_{ij})(q_j-q_i)+
\sum_i p_i\dot q_i,
\]

\[
\frac{d}{dt}(N\bar q)=N\left[\bar r\bar q+
\operatorname{Cov}_p(q,r)+\mathbb E_p[\mathcal Tq]+\mathbb E_p[\dot q]\right].
\]

The last derivative includes every context change on which contribution depends. The equations apply componentwise for several support stocks. They are accounting decompositions, not assumptions of a shared optimizer. Negative covariance alone is neither necessary nor sufficient for total support collapse; its effects can be offset by the other terms and by background renewal. The substantive empirical question is whether independently measured contributions and success exhibit the predicted relation.

### 2.2 Absolute support is not inferable from pure-selection shares

Within pure selection \(\dot n_i=r_in_i\), let \(a(t)>0\) be differentiable. Then \(\widetilde n_i=a n_i\), \(\widetilde r_i=r_i+\dot a/a\) preserve every share \(p_i\) and relative growth rate. They need not preserve absolute abundance. Constant rates \((1,0)\) and \((-1,-2)\) with identical initial composition give the same share trajectory while the first population grows asymptotically if type 1 is present and the second vanishes.

This is nonidentification over a model class. It is not a symmetry of an arbitrary fixed ecological system whose environmental feedback changes relative rates, mutation, or birth-linked transmission. Additional validated information can resolve it. A theorem about shares cannot be generalized to every possible performance measure.

### 2.3 Budget and deadline constraints

For an absolutely continuous stock with exact balance \(\dot E=R-L\), the condition

\[
\int_0^t(L-R)\,ds\le E(0)-E_{\min}\qquad\text{for every }t\le T
\]

is equivalent to \(E(t)\ge E_{\min}\) throughout \([0,T]\). The single endpoint inequality is only necessary when losses can reverse. This is stock safety alone, not a sufficient certificate for all protected outcomes.

For vector stocks \(B\ge B_{\min}\), if one nonnegative weight vector \(y\) and \(\epsilon>0\) satisfy \(y^\top\dot B\le-\epsilon\) for **every admissible route** while the required activity and protected region persist, then no such route lasts longer than \(y^\top[B(0)-B_{\min}]/\epsilon\). Integrating proves the claim. A bound for one policy only assesses that policy. Functional substitution, imports, dormancy, or activity reduction must be included or explicitly excluded before applying it.

If no effective response can arrive before \(\tau\), and every relevant pre-response action has net loss at least \(d_-(t)\ge0\), then \(\int_0^\tau d_-\le E(0)-E_{\min}\) is necessary for reserve safety. Adequate reserve does not establish information, permission, execution, or subsequent maintenance. A sufficient policy certificate needs an upper loss bound for an actual admissible policy, all intermediate constraints, and a safe continuation. Lower bounds for impossibility and upper bounds for a safe construction must never be interchanged.

### 2.4 Two exact but distinct continuous mechanism examples

**Selection against maintenance.** The closed ODE

\[
\dot x=x(1-x)(\theta-c),\qquad
\dot N=N[aE-m-\gamma N-cx],\qquad
\dot E=\rho Nx(1-E/K)-\delta E
\]

has positive parameters and nonnegative initial conditions. If \(\theta<c\), \(N_0>0\), and \(x_0<1\), then \(x,E,N\to0\). Proof: \(E\) and \(N\) are bounded; \(x\to0\); hence \(Nx\to0\), which forces \(E\to0\), and eventually \(\dot N\le-mN/2\). The all-maintainer boundary \(x_0=1\) is an exception in the absence of invasion or mutation.

If \(\theta>c\), put \(M=m+c\), \(H=\delta K/\rho\). On \(x=1\), two positive equilibria exist precisely when

\[
aK>(\sqrt M+\sqrt{\gamma H})^2.
\]

Their abundance coordinates are roots of \(\gamma N^2-(aK-M-\gamma H)N+MH=0\). The lower root is a saddle; the upper is locally asymptotically stable; extinction remains locally stable. The strict inequality excludes the nonhyperbolic saddle-node equality. Favorable composition therefore permits renewal without guaranteeing rescue from depleted states. The frequency coordinate at \(N=0\) is an extension of the chart, not a meaningful observed population proportion.

**Correction renewing itself.** In the distinct model

\[
\dot E=\frac{aC}{1+C/K}-\delta E-uEC,
\qquad
\dot C=\eta uEC-\mu C,
\]

external feedstock is assumed available, all parameters are positive, and \(u>0\) is fixed effort. Set \(m=\mu/\eta\), \(A=a/m\), \(d=\delta/(uK)\). The quantity \(V=E+C/\eta\) obeys \(\dot V\le aK-\min(\delta,\mu)V\), so trajectories are bounded. Positive equilibria require \(E^*=m/u\) and

\[
C_\pm=\frac K2\left[A-1-d\pm\sqrt{(A-1-d)^2-4d}\right].
\]

Two exist exactly for \(A>(1+\sqrt d)^2\). The Jacobian trace is negative and determinant is \(\eta uCm[1-A/(1+C/K)^2]\): lower is a saddle, upper locally stable. The origin remains locally stable. Below the strict threshold, use

\[
W=E+C/\eta+\frac{\delta}{\eta u}\log(C/K),
\quad
\dot W=mK\left[\frac{Aq}{1+q}-q-d\right],\quad q=C/K.
\]

Since the maximum of \(Aq/(1+q)-q\) on \(q\ge0\) is \([\max(\sqrt A-1,0)]^2\), strict subthreshold parameters imply \(\dot W\le-\kappa<0\). As \(E+C/\eta\ge0\), this forces \(\log(C/K)\to-\infty\) at least linearly, hence \(C\to0\); comparison then gives \(E\to0\). Boundary cases \(C=0\) follow directly. This proof does not cover threshold equality.

A locally stable positive equilibrium strictly above \(E_{\min}>0\) exists exactly when \(A>1\) and

\[
\frac{\delta}{K(\sqrt A-1)^2}<u<\frac{\mu}{\eta E_{\min}}.
\]

This is an equilibrium existence statement. It does not establish transient safety, accessibility from a given state, that selection installs this effort, or that feedstock persists. The two examples have related causal structure but are not already one fitted or universally derived model.

## 3. Suggested integrated finite-system proposition

This is a legitimate new *combination of existing results*, not a new universal dynamical law. It can serve as the formal center of the review file.

### 3.1 Contract and assumptions

Let \(S,U,Y\) be finite sets. For every proposed action \(u\), \(K_u\) is a stochastic kernel on \(S\). The state includes all declared memory, pending repair, selection-rule state, resource, access, authority, and event-monitor coordinates required for a Markov description. All proposals are defined; denied proposals have their explicitly modeled consequences. Alternatively, enabled-action sets are preserved explicitly without granting unobserved availability to the controller.

Let \(h:S\to Y\) be the actual observation map of the controller. Let \(C\subseteq S\) be an independently declared acceptable set and \(T_1,\ldots,T_q\subseteq S\) finite monitor targets for genuinely required recurring events. Neither \(C\) nor these monitors is inferred from the installed system's self-evaluation. Plural outcomes need not be collapsed into a scalar utility.

Let \(q:S\twoheadrightarrow\bar S\) preserve \(h\), \(C\), every \(T_j\), relevant permission distinctions, and any other outcome label. Assume intervention-wise row equality:

\[
q(s)=q(t)\implies K_u(s,q^{-1}(\bar z))=K_u(t,q^{-1}(\bar z))
\quad\text{for every }u,\bar z.
\tag{F}
\]

This defines \(\bar K_u\). Boundary disturbances can be incorporated into \(S\), included as explicitly conditioned modes, or treated robustly by taking the union of their supported successors. A hidden environment that chooses inputs using omitted state distinctions invalidates the simple path-law conclusion unless its generation mechanism is preserved too.

Information and decision rights are part of this contract. Keeping an outcome in \(q\) does not mean the controller observes it. For multiple agents, replace \(h\) by separate local observations and preserve the decentralized policy class. The belief recursion below, as written, is for one decision process using the declared common observation history; it does not solve general decentralized synthesis.

### 3.2 Clause A: representation preserves permitted consequences

Under corresponding initial distributions and the same observation-history-based randomized action policy, the fine process projected through \(q\) and the quotient have exactly equal path laws. Therefore they agree on every measurable retained event, including all finite safety deadlines and safety plus recurring renewal:

\[
\mathcal P=\{S_t\in C\ \forall t\}\cap\bigcap_j\{S_t\in T_j\ \text{infinitely often}\}.
\tag{P}
\]

Proof: condition on each fine history; (F) makes the conditional next-block row depend only on the current block and selected input. Mixing over compatible fine histories leaves the row unchanged. Observations and corresponding policies give the same input law. Induction equates all finite cylinder probabilities, which determine the path measure on the countable product of finite alphabets. This proof does not require independent module noise; the supplied kernels must already be the correct joint laws.

### 3.3 Clause B: possible safe control under actual information

Define \(F(s,u)=\{s':K_u(s,s')>0\}\). From an information set \(B\) after a common observed history, let

\[
\Phi(B,u,y)=\left(\bigcup_{s\in B}F(s,u)\right)\cap h^{-1}(y).
\]

Use the quotient analogue \(\bar\Phi\). Condition (F) implies

\[
q(F(s,u))=\bar F(q(s),u),\qquad
q(\Phi(B,u,y))=\bar\Phi(q(B),u,y).
\tag{I}
\]

The first equality follows because a block has positive summed transition probability exactly when it contains a positive-probability successor. The second follows by taking unions and using the fact that \(h\) factors through \(q\).

Define

\[
\mathfrak W_0=\{B:\varnothing\ne B\subseteq C\},
\quad
\mathfrak W_{H+1}=\{B\subseteq C, B\ne\varnothing:
\exists u\ \forall y,\ \Phi(B,u,y)\ne\varnothing\Rightarrow\Phi(B,u,y)\in\mathfrak W_H\}.
\]

Then an admissible observation-based policy guarantees safety through \(H\) transitions from every \(s\in B\) iff \(B\in\mathfrak W_H\), and

\[
B\in\mathfrak W_H\quad\Longleftrightarrow\quad q(B)\in\bar{\mathfrak W}_H.
\tag{V}
\]

The first claim follows by induction on a common first action and every ensuing observation; the second by the same induction using (I), with base case given by preservation of \(C\). Randomization cannot enlarge sure-safe winning sets for this finite-horizon safety objective: every positive-probability action must be safe for all compatible states. A failed guarantee is not a prediction of inevitable failure.

Initial information sets must be interpreted after the available initial observation. If an initial prior support spans different immediately observable values, condition separately on each value rather than artificially requiring a common first action across already distinguishable states.

### 3.4 Clause C: actual persistence of an installed finite process

Now specify a finite installed controller, including its memory and rule succession, and its actual observation-admissible proposal and update maps. Combine these with the plant, execution gates, and boundary process to obtain a finite time-homogeneous closed-loop kernel \(K^{\mathrm{inst}}\) on the augmented state. This is an additional supplied mechanism, not a choice optimized by the theorem. Ensure that the lifted quotient also preserves its updates. This follows, for example, for finite controller memory retained exactly, when proposal and memory-update laws depend only on preserved observations and memory and their joint noise assumptions are respected.

For an initial support \(B_0\), the installed process satisfies (P) almost surely iff:

1. every positive-probability reachable state lies in \(C\); and
2. every reachable bottom strongly connected component of the support graph of \(K^{\mathrm{inst}}\) meets every \(T_j\).

Proof: every finite homogeneous Markov chain almost surely reaches a bottom recurrent class and then visits each state in that class infinitely often. A reachable state outside \(C\) or reachable bottom class missing a target has a positive-probability path witnessing failure. Conversely the two graph conditions imply (P) with probability one. By Clause A, its truth and probability agree on a faithful quotient of the installed process.

This joins actual renewal, faithful representation, and observation-restricted control in one mathematical architecture. Crucially, (V) is an **existence** result; it does not imply the installed rule satisfies the graph test. A safe alternative policy can exist while the installed process neglects, disables, or refuses it. Conversely, actual almost-sure renewal is stronger than the mere availability of replacement resources.

The property is conditional on the monitor semantics. Repeatedly visiting a state called “correction available” is not repeated effective correction. Requests with deadlines need pending/age monitors, and failure to respond in time must be represented. Functions that need no ongoing replacement should not be assigned an artificial recurring obligation.

### 3.5 Clause D: a constructive sufficient route to (F)

Suppose \(S\subseteq\prod_{i\in I}S_i\), finite, and

\[
z_i^+=F_i^u(z_{\operatorname{Pa}_i^u},\eta),\qquad\eta\sim\nu_u,
\]

with fresh joint noise whose conditional law, given the mode and history, does not depend on omitted state. Modules may share arbitrarily correlated noise. Every actual state read must appear among parents, including guards, permissions, preservation branches, selector states, and noise-law selectors. All next-state updates use the old state, or sequential updates have been expanded into their true dependencies.

Start with coordinates \(R_0\) determining retained labels, observations, permissions, and controller memory. Iterate

\[
R_{n+1}=R_n\cup\bigcup_{i\in R_n,u}\operatorname{Pa}_i^u.
\]

This terminates at the least parent-closed set \(R_*\). The projection \(q(z)=z_{R_*}\) satisfies (F): under identical mode and identical joint noise, equal retained old states have exactly equal retained next states. This is a pathwise coupling proof and retains joint correlations. Cycles close finitely without introducing a distinct controller of each controller.

The closure is a sufficient syntactic boundary, not necessarily a minimal predictive representation. A syntactic dependency may cancel, or admissible state constraints may make it redundant. The closure does not establish actual renewal, favorable behavior, empirical correctness of the supplied mechanisms, or legitimacy of the retained labels. It supplies Clause A, not Clause C's graph conditions.

## 4. Critical interpretation checks for the final review file

- **Three meanings of closure:** structural dependency closure, semantic interventional closure, and actual safety/renewal closure are different. The first can imply the second; neither implies the third without additional dynamics.
- **Actual versus potential:** an available safe response, a positive equilibrium, and an installed regime that safely reaches and maintains it are separate claims.
- **Pointwise feasibility versus usable information:** defining capacity by “there exists an observation-based policy from full state \(z\)” still allows a different constant policy to be selected for each hidden \(z\). This can overstate what the participant can attain from its evidence. Define the profile at an information state \(B\), a specified initial belief, or require one common policy uniformly over the stipulated initial uncertainty. Pointwise existence is a legitimate optimistic benchmark only if labeled as such.
- **Infinite horizons:** an irreducible finite class with even a tiny exit to absorbing harm is not closed. If each continuing opportunity has conditional irreversible hazard at least \(\epsilon>0\), survival through \(n\) opportunities is at most \((1-\epsilon)^n\), without independence. Do not trim rare positive edges.
- **Approximation:** uniform per-history conditional total-variation error \(\epsilon\) gives finite-horizon path-event error at most \(1-(1-\epsilon)^H\le H\epsilon\). Average prediction accuracy or a finite failure-free record does not establish this bound, and it does not yield an infinite-horizon recurrence theorem.
- **Uncertainty:** robust safety for a set of row choices permits adversarial switching and can be conservative for one unknown fixed kernel. The fixed-chain bottom-class recurrence theorem does not transfer automatically to adversarially changing kernels.
- **Selection:** Price-style decomposition and common-growth invariance are restricted but exact. They do not prove that domination, accumulation, or competition is unavoidable or universally selected.
- **Normativity:** preserving outcomes, reported commitments, consent observations, and authority in a model does not derive their legitimacy. Endogenous approval is not independent validation. Ethical conclusions need explicit bridge commitments beyond persistence.
- **Generativity:** a finite rational instruction grammar exactly generates finite rational kernels at atomic macrostep boundaries, but arbitrary transition probabilities remain supplied data. That result proves expressiveness, not explanatory compression or causal identification.
- **Open-endedness:** finite rules may generate an unbounded counter and require infinitely many predictive states. Finite generative principles and a finite sufficient state are distinct claims.
- **Uniqueness:** the coarsest deterministic faithful partition for one fixed finite model/contract is unique. That is not uniqueness of the theory's ontology, ethical specification, or physical explanation.
- **Specialist-review language:** “a mathematically grounded general generative foundation” is defensible when defined as the linked causal architecture and conditional consequences above. “The complete unique universal root has been proved” is not supported by these results.

## 5. Review assessment

I found no blocking mathematical error in the source results listed here within their stated assumptions. The integrated proposition above makes a stronger and more organized connection than quoting the results separately, but its ingredients are established balance, stochastic reduction, partial-observation safety, and finite-chain recurrence mathematics. Its prospective contribution is the way mechanisms generating and maintaining correction, authority, and succession are included in the same audited process while plural normative specifications remain explicit.

The most valuable claim to put before specialists is consequently precise: **these results supply a common mathematical architecture for analyzing how activity changes its own enabling conditions, when information and implementation permit preservation or replacement, and whether the installed process actually reproduces the required capacities through time.** Whether a particular domain fits that architecture, and whether the integration improves prediction or intervention relative to existing theories, are additional scientific questions.

## 6. Audit of the assembled review draft

I read the initial assembled `FOUNDATION.md` through §13 (the 728-line version available during drafting). In addition to the source results, I checked:

- the plural-feasibility linear-programming dual and its sign conventions;
- finite permanent-exit consistency and reach-weighted participation constraints;
- the binary-context harm/burden frontier;
- the logistic adoption and maturation-delay condition and integrated reserve certificate;
- the partial-observation feasibility transfer in the integrated theorem;
- the installed-process safety/recurrence criterion and finite-horizon coupling bound.

No blocking algebraic or theorem error was found in those portions. I sent the author the following precision requests, whose incorporation should be checked against the final file:

1. Define information-constrained capacity at a common initial information state or belief, not pointwise existence of a separately chosen policy for each hidden full state.
2. Condition initial information sets on observations already available.
3. A covariance-only mean-trait increase needs fixed trait values and selection dynamics without additional trait-changing terms; faithful offspring transmission alone does not exclude within-carrier change.
4. Require at least one executable policy for the occupation-measure set to be nonempty and the minimax slack optimum finite and attained.
5. State matched initial distributions for the displayed per-transition coupling bound, and treat initial mismatch separately.
6. State the fresh joint-noise assumption unambiguously: the common law is fixed conditional on the declared input; hidden persistent past dependence must enter state or the boundary model.

This mathematical audit checks stated internal implications. It does not constitute empirical validation, an originality determination, or endorsement of the dossier's normative commitments.
