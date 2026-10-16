# Adversarial review of the unified formal core

5 October 2026. Reviewed `/Users/ren/theories/theories/becoming/chapters/FORMAL-CORE.md` after its twelve proofs were written. Read-only review of the canonical file; no canonical edits or commits. This supplements `work/math-synthesis.md` and the independent finite checks in `work/math-review/`.

## Determination

The core equations and main proofs are sound under their natural intended assumptions. F3's convergence proof is particularly economical and correct, including equality at the threshold; F9 handles labelled transition events correctly; F11's interchange of finite minima with increasing extended-real limits is valid. I found **one literally overstrong conclusion** in the finite-energy wording and **several assumptions that should be stated explicitly to make the claimed exact, implemented results self-contained**.

The required corrections are local. None calls for abandoning the unified architecture or fusing its different model classes. Proposed replacement text follows each finding.

## 1. Findings requiring precise wording

### 1.1 F3: finite cumulative activity does not exclude activity positive at every finite time

Current sentence: “This prevents indefinite positive machinery activity from finite work supply in this model.”

The displayed bound establishes that the integral of \(C\) is finite. It rules out a positive persistent floor and unbounded cumulative activity, but does not rule out \(C(t)>0\) for every finite \(t\).

**Counterexample:** set recycling flux \(J=0\), \(R(0)=0\), \(C(0)=1\), \(E(0)=0\). Then \(C(t)=e^{-bt}>0\) at every finite time, while \(b\int_0^\infty C\,dt=1\). This satisfies the bound exactly.

**Replace with:**

> This rules out unbounded cumulative machinery activity, and in particular any continuing regime with machinery bounded away from zero, from the stated finite initial support and work reserve. Activity can remain positive at every finite time while decaying to zero.

No change is needed to (F3.5).

### 1.2 F8: exact belief semantics and update sufficiency are needed for the iff

The theorem says exactly which information states admit a safe policy. “Post contains all compatible successors” alone permits an overapproximation, which proves a sound sufficient certificate but can incorrectly reject a winning situation. A generic finite summary can also merge distinguishable histories with incompatible future decisions.

**Counterexample to arbitrary summarization:** the controller observes whether the state is left or right. In left, only action L is safe; in right, only action R is safe. The actual controller wins from either observed state. A summary that merges both and a common-action recursion on that summary reject the guarantee. Exactness fails for the summary, not for the genuine observation policy.

**Add before (F8.1):**

> Here \(I\) is the exact set of physical states compatible with the actual observation/action history, or a proved equivalent sufficient information state. The available action interface and conditional update depend only on \(I\). The update \(\operatorname{Post}(I,a,o)\) is exactly the compatible successor information state, including every unsafe possibility; it is not an arbitrary conservative overapproximation. The state includes any persistent model label and memory required to preserve temporal dependence.

For a simple finite nondeterministic model the defining formula can be shown explicitly:

\[
\operatorname{Post}(I,a,o)=
\left(\bigcup_{x\in I}F(x,a)\right)\cap O^{-1}(o).
\]

The exactness proof is induction on history length: every member has a compatible predecessor path and every possible extension appears in the update. If an overapproximation is intentionally used instead, change “exactly” to a sound one-way guarantee and retain the distinct completeness qualification.

### 1.3 F8: abstract observation-history control and a paid restricted memory class are different

A fixed-point selector chooses an action using \(I\), and then stores and updates that information state. A mathematical belief state can require more memory than the specified actor has. Merely including resource variables in the plant state does not pay for an unmodeled belief-update machine.

The source `full-picture-conjecture/outputs/continuation-proof.md` explicitly distinguishes finite executable controller generation from physical affordability. The unified self-contained proof should retain the distinction.

**Add:**

> The theorem concerns observation-history policies with the information-state update and selector memory admitted by the stated policy class. Calling its witness physically implementable additionally requires those operations and their costs to be included in the modeled interface. A smaller externally restricted controller class may have a smaller feasible set.

Alternatively impose directly that the exact information-state machine and all selected witnesses are physically implementable within the charged interface. This is a stronger assumption, not a consequence of state finiteness.

### 1.4 F11: the choosing actor must know the delivered configuration

The recurrence minimizes separately at each \((z,q)\). That is correct if \(z\) is known to the decision-maker or is itself an exact information state. If \(z\) is hidden physical state, it can grant the controller the wrong quantifier order.

**Add to the first paragraph:**

> The delivered configuration \(z\) is observed by the choosing actor, or is a sufficient information state it can actually retain and update. Each option's resource feasibility is exactly a threshold condition \(r\ge c(z,q,a)\), after which the delivered reserve is \(r-d(z,q,a)\) and the delivered configuration is \(f(z,q,a)\). These laws have no omitted dependence on the reserve.

This makes precise what “faithfully encode” must guarantee. Also specify \(d\in\mathbb R\) is finite; it may be negative because receipts can exceed expenditures. Define \(\min\varnothing=+\infty\).

**Why this matters:** with two unobserved configurations requiring opposite free actions, the statewise recursion returns zero reserve for both even though no common observation-based policy succeeds. Likewise a resource cap or upper-threshold permission can invalidate the upward-closed feasible set \([H_n(z),\infty)\); the scalar recurrence presumes that shape.

### 1.5 F9: transition recurrence is not by itself indefinite physical-time operation

The finite theorem is correct as written for runs in the transition relation. To use it as a physical continuation theorem, the durations must not admit Zeno execution.

**Add after the theorem:**

> This proves recurrence in transition count. Continued recurrence over unbounded physical time additionally requires the sum of elapsed durations on every infinite admitted run to diverge. A uniform bound on physical waiting time requires corresponding duration bounds. All paths of the specified relation are included; a fairness restriction on infinite paths would require its own liveness argument.

Example: event delivered at every step of durations \(2^{-n}\) gives infinitely many labelled deliveries before time one. Every finite rank condition can hold while no unbounded physical-time operation is shown.

### 1.6 F6 and F10: two small logical qualifiers

F6.2 gives **asymptotic/exponential stability**, not every possible meaning of “stability.” At equality a mode may be marginally Lyapunov stable but fails attraction. Replace “stability exactly when” by “exponential stability exactly when.”

In F10, “the conditional bound is necessary” should read “the uniform conditional bound is the hypothesis used.” The stated bound is sufficient for the geometric tail estimate; it is not necessary for almost-sure eventual failure. For example, conditional hazards \(1/(t+2)\) have no uniform positive lower bound while their survival product tends to zero. Even an unconditional geometric tail can arise from a geometrically distributed countdown revealed at initialization, whose sufficiently long conditional countdown histories have zero failure probability during the next fixed number of steps.

## 2. Requested proofs checked in detail

### F3: convergence and threshold

Let \(d_*=b/k\). Invariance and conservation are correct. Equation (F3.2) is exact because \(\dot D=-kC(D-d_*)\). Thus \(D\) remains between \(D(0)\) and \(d_*\), within the simplex, and has a limit \(\ell\).

The linear forced equation for \(C\) has convergent forcing \(a(M-D(t))\). Variation of constants gives \(C\to a(M-\ell)/(a+b)\). Above threshold with \(R(0)+C(0)>0\), both interval endpoints \(D(0)\) and \(d_*\) are strictly below \(M\); therefore \(\ell<M\), and the positive limit of \(C\) forces \(\ell=d_*\). At or below threshold, \(D\) is nondecreasing with limit at most \(M\); an alleged \(\ell<M\) forces \(\dot D\) to a strictly positive limit even at the equality \(M=d_*\), a contradiction. The all-degraded boundary is handled separately. The stated triangular equilibrium Jacobian is correct.

No positivity, global basin or critical-equality step is missing. The only F3 correction is the interpretation of finite integrated activity in §1.1.

### F8: elimination and quantifiers

With the exact-update and policy-class assumptions in §1.2–1.3, the theorem is correct. One common action precedes all possible observations; unsafe possibilities are retained. The recursion's use of \(I\in W_n\), rather than \(I\in S\), gives the same descending sequence: if \(\Phi\) is the ordinary predecessor operator, monotonicity and initialization at \(S\) give \(\Phi(W_n)\subseteq W_n\) at each stage.

The necessity proof can equivalently establish by backward induction that \(W_n\) is the set winning for \(n\) transitions. Finiteness of the information-state set yields stabilization and a stationary selector on that set. This stationary selector may still represent substantial controller memory relative to raw observations. No hidden-model switching is allowed when the model label is persistent.

The proof does not establish recurring progress; the document correctly keeps F9 and additional event conditions separate.

### F9: labelled transition ranks

Both directions are correct for the total all-path installed relation. Sufficiency uses a strictly descending rank on a suffix with no corresponding event. Necessity takes the reachable set and excludes a directed cycle in the event-free subgraph. Longest-path length decreases on each such edge.

The explicit treatment of parallel transitions with different labels is correct and important. Deleting a non-delivering edge because its endpoints also have a delivering edge would invalidate necessity and sufficiency. A safe self-loop with an event-free alternative correctly fails the certificate.

Ranks may increase on their event, and different event types can use different ranks. Their proofs share one installed process and invariant; no incompatible successful controllers are spliced together. Infinite-state ordinal ranks are a valid semantic extension under the source's well-foundedness and choice assumptions, while finite effectiveness remains separately qualified.

The independent script `work/math-review/check_integration.py` checks the finite event-rank equivalence against separate cycle detection on all 225 total two-state event-labelled graphs and both stated safe sets. It passed all 450 cases.

### F11: finite minimization and increasing limits

Let \(T\) be the displayed reserve operator. With finite \(Q,A\), finite real \(c,d\), and \(\min\varnothing=\infty\), it is monotone on \([0,\infty]^Z\), and \(T0\ge0\). Therefore \(H_n=T^n0\) increases.

For every fixed action, \(d+H_n(f)\) increases to \(d+H_\infty(f)\), with the ordinary convention \(d+\infty=\infty\). Finite maxima commute with this limit. Finite minima do too: choose a minimizing action at each \(n\); some action is selected along an infinite subsequence. Monotonicity makes its limit equal the limiting minimum. This proves

\[
T(\sup_n H_n)=\sup_n T(H_n)=\sup_n H_{n+1}=H_\infty.
\]

Where \(H_\infty(z)<\infty\), every task has a minimizing action of finite required reserve. Its successor threshold is finite because adding finite \(d\) cannot make an infinite threshold finite. The stationary choice keeps the reserve above the corresponding successor threshold, proving one indefinite policy exists, not merely a different policy for each finite horizon. Where \(H_\infty(z)=\infty\), every finite initial reserve fails some finite-horizon necessary condition. The example's post-episode reserves 7, 5, 3 and inability to prepay the fourth five-unit bill are correct.

Finiteness of actions is load-bearing for this limit step. A choice among finite countdowns of arbitrary length can pass every finite horizon but fail every infinite horizon; finite minima prevent that escape. Negative net cost is allowed but does not cause any failure of monotonicity. Storage caps, unobserved delivered configurations and unmodeled reserve-dependent availability are outside this recurrence.

## 3. Remaining results

- **F1:** transfer cancellation and the autonomy witness are correct for fixed symmetric nonnegative weights and freely variable exterior preparations. Adding “fixed” to the weight description avoids any ambiguity about state-dependent exchange laws.
- **F2:** the integrated identity and prefix equivalence are exact. The positive-deficit deadline applies if operation continues that long; stopping earlier does not force the stock itself to reach the floor.
- **F4:** the nonnegative inverse has the correct order, \((L-B)^{-1}=\sum_n(L^{-1}B)^nL^{-1}\). Its zeroth term gives strictly positive components of \(w\). The weighted differential and integral bounds, acyclic nilpotence and \(\sqrt{kM/b}\) chemical comparison are correct. Absolute continuity/global existence of the admitted trajectory is implicit and can be named.
- **F5:** factorization, expanded-question obstruction and common minimizer criterion are correct. The text properly avoids confusing predictive minimality with physical generator size or implemented memory cost.
- **F6:** indistinguishability and unstable aggregate-hidden-mode arguments are correct, with causal well-posedness explicitly included. Use the asymptotic/exponential qualifier in §1.6.
- **F7:** nine-round participant arithmetic, eleven carrier units, recurring funding \(11/9\), prefunded cap three, least initial \(23/9\) and delay inequality are internally consistent with the stated timing conventions. The claimed sharpness is explicitly protocol-relative. Sufficiency at the threshold is shown, and no unrestricted institutional optimum is claimed.
- **F10:** the finite CTMC absorption proof is correct: every nonabsorbing state has a positive-probability finite route to the all-degraded state, so no other closed class exists. Finite state and positive finite holding rates in active states give finite expected absorption time. The general block proof is correct under its sufficient uniform conditional bound.
- **F12:** opposite task rankings, the sum-one joint infeasibility witness, the expressiveness limitation and the halting reduction are correct. The last theorem distinguishes unrestricted finite data from a certified finite deterministic recurrence. No impossible universal incompleteness conclusion is smuggled into the narrower algorithmic limit.

## 4. Proposed compact additions after F2

These additions would improve completeness. F2 alone is a stock identity and F4 covers a fixed global linear production bound. The two following results add renewal ancestry without linear production assumptions and an exact adaptive feasibility theorem for plural capacities. They are reconstructions of already preserved work, not new external evidence.

### Proposed F2b: recurrent support ancestry under sustained loss

For finitely many independently identified support types, let

\[
C_i(t)=C_i(0)+E_i(t)+\sum_jR_{ji}(t)-L_i(t)\ge0.
\tag{F2b.1}
\]

Initial stocks are finite; cumulative external provision \(E\), internal provision \(R\), and losses \(L\) are nonnegative, nondecreasing and finite on bounded intervals. Assume **productive vulnerability**: any internal supplier delivering unbounded cumulative service itself faces unbounded loss of a tracked capacity.

**Theorem.** Every support with unbounded cumulative loss is downstream, along unbounded internal-provision edges, from either an unbounded external source or a directed internal cycle.

**Proof.** Unbounded loss and nonnegative stock require unbounded provision. With finitely many inputs, at least one is unbounded. Stop if that input is external; otherwise move to its internal supplier. Productive vulnerability permits repeating the argument. A backward path in a finite graph either reaches an external source or repeats a node, producing a cycle with a forward provision path to the original support. ∎

The theorem does not require every component to lie on the cycle, simultaneous edge operation, a positive average renewal rate or an equilibrium. A cycle may remain too weak, too slow or inaccessible. Infinite acyclic succession, a durable supplier, finite total loss or continuing external organizational input invalidate different premises. Source: `/Users/ren/theories/_process/research/2026-10-05-generative-foundation-review/root-foundation/ROOT-FOUNDATION.md`, R3, and `TURNOVER-AND-CLOSURE.md`.

**Optional finite-lifetime companion.** If every instance of each of finitely many support types lasts at most \(\tau_i\), every new instance needs a functioning earlier parent, and no later organizational instance enters externally, an acyclic type graph has expiry bounds

\[
d_i=\tau_i+\max(\{0\}\cup\{d_j:j\to i\}),
\qquad \max_i d_i\le\sum_i\tau_i.
\]

Topological induction proves the bounds. Renewal counts as a new instance; a type-level cycle is consistent with forward temporal causation. The bound cannot be applied without independently justified lifetime and parent conditions. Source: the same file, R2.

### Proposed F2c: plural capacity and a certificate of unavoidable deficit

Let nonnegative capacity margins \(v\) and distinct reserves \(b\) obey

\[
\dot v=Mu-\rho(v),\qquad \dot b=p-Qu.
\tag{F2c.1}
\]

Assume \(U\), the actually executable activity set, is nonempty, compact, convex and fixed, with constant activities permitted; \(M,Q,p\) are fixed. Let \(\rho\) be locally Lipschitz on a neighborhood of the safe orthant and satisfy \(\rho_i(v)\ge r_i\) for all safe \(v\), with equality whenever \(v_i=0\). Initial margins and reserves are finite. These assumptions include a minimum loss on each protected boundary and physically realizable fractional activity; neither follows from calling something a capacity.

Define

\[
F=\{u\in U:Mu\ge r,\ Qu\le p\}.
\tag{F2c.2}
\]

**Theorem.** Indefinite preservation from any finite safe initial state is possible iff \(F\ne\varnothing\). A constant activity in \(F\) suffices; if \(F\) is empty, no adaptive schedule preserves all requirements indefinitely from any finite safe initial state.

**Proof.** A constant feasible activity makes every capacity floor-face derivative nonnegative and every reserve derivative nonnegative, so the safe orthant is invariant. Bounded controls and the global lower loss bound prevent upward finite-time escape along a safe trajectory. Conversely, average any safe activity over \([0,T]\). Integration gives

\[
M\bar u_T\ge r-v_0/T,\qquad Q\bar u_T\le p+b_0/T.
\]

Convexity puts the average in \(U\), and compactness supplies a convergent subsequence for \(T\to\infty\). Its limit belongs to \(F\). ∎

If \(F=\varnothing\), strong separation of the compact convex net-rate set from the nonnegative orthant supplies nonnegative \(\lambda,\mu\), not both zero, with

\[
\beta=\min_{u\in U}
\{\lambda^T(r-Mu)+\mu^T(Qu-p)\}>0.
\]

Then \(W=\lambda^Tv+\mu^Tb\ge0\) on any safe interval and \(\dot W\le-\beta\), giving the finite deadline

\[
T\le\frac{\lambda^Tv_0+\mu^Tb_0}{\beta}.
\tag{F2c.3}
\]

The weights certify joint shortage; they are not a common ethical utility or permission to exchange one protected violation for another. For constant losses, the infimum of these bounds gives the exact maximum service duration: time-averaging gives necessity, and executing a feasible average constantly traces a safe straight segment between the endpoints.

**Exact example.** Two capacities each lose \(2/5\); activities satisfy \(u_1,u_2\ge0\), \(u_1+u_2\le1\). One resource receives \(3/5\) and spends \(u_1+u_2\). Each capacity alone is sustainable, but their joint continuing demand is \(4/5>3/5\). From margins \((1/10,1/10)\) and reserve \(1/5\), the sum of all three margins decreases at rate \(1/5\), so duration is at most two. Constant \(u_1=u_2=7/20\) attains exactly two.

State-dependent availability, unavailable convex mixtures, and interior states with less loss than the stated boundary minimum require different analysis. The theorem does not choose the protected floors. Source: `/Users/ren/theories/_process/research/2026-10-05-generative-foundation-review/root-foundation/PLURAL-CAPACITY.md`.

## 5. Delivery and audit scope

This review re-derived the central proofs and supplied explicit counterexamples where wording was too broad. It did not rerun unchanged source study scripts, edit canonical files, or claim empirical verification. Its finite certificate/finance check results remain in `work/math-review/results.json`; no new experiment is implied.

The highest-priority repairs are F3's integrability wording and F8's exact information/update/implementation contract. F11 should explicitly state full observation or sufficient information-state control. F9's physical-time sentence and the small stability/conditional-bound qualifiers then make the document accurately self-contained.
