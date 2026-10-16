# Cross review of the root and information results

Reviewed 5 October 2026: [Information and renewal](INFORMATION-AND-RENEWAL.md) and [Root foundation](ROOT-FOUNDATION.md). This is an internal adversarial mathematical review, not independent specialist validation or empirical confirmation.

## Overall finding

The main proofs survive review under their stated pointwise capacity and resource requirements. The control-independent exhaustion certificate genuinely covers arbitrary measurable, adaptive, and randomized allocation schedules path by path. The attainable interval includes its endpoints; the five-unit service deadline is attained by the displayed witness. The selection example has two locally asymptotically stable equilibria of the reliability–practice subsystem, an intervening saddle, and two proved invariant subsets of its basins. It does not establish a global basin classification, and neither document claims one.

One risk-quantifier clarification should be made before delivery. No change to the equations or proofs is needed if the intended requirement remains the continuously imposed capacity floor.

## Clarify conditional accuracy and continuous service

The information note states that the channel meets its per-demand error tolerance exactly when \(c\ge c_*\), and subsequently permits history-dependent random controls. For a fixed channel state, the statement is correct. Across random operating histories, the corresponding theorem needs accuracy conditional on each realized **pre-demand** history, including any prior controller randomization. A marginal risk bound averaged over operating histories would instead depend on \(\mathbb E[c]\) at a demand and would not imply a pointwise floor.

For example, a channel with reliability \(0.9\) or \(0.1\), each with probability one half, has marginal optimal error \(0.25\). It meets that marginal tolerance despite violating the floor \(c\ge0.5\) in half the histories. This is a counterexample to equivalence of the two risk specifications, not a counterexample to Theorem E2: E2 explicitly requires the pointwise floor.

Similarly, the proof requires \(c(t)\ge c_*\) at every time in the acceptable interval. If accuracy were only required at a sparse sequence of scheduled demand times, temporary degradation between demands would define a different control problem. The impossibility bound should not be transferred to that problem without another proof.

**Suggested insertion after (E6), and an abbreviated version after (R6):**

> The accuracy requirement is conditional on every realized pre-demand history, including the controller's prior randomization. The operating problem below imposes the reliability floor continuously, including between scheduled demands. Averaging accuracy across different operating histories, or requiring it only at isolated demand times, defines a different problem.

If this is not the intended specification, the theorem should retain its present capacity-floor language and the broader error interpretation should be withdrawn. The present proofs do not establish the corresponding unrestricted marginal-risk or demand-only optimum.

## Mathematical checks

For \(u\in[0,1]\), the physical equations have a unique absolutely continuous trajectory for each realized measurable control schedule. Starting with \(c<1\), finite-time comparison with maximal repair keeps the logarithmic certificate finite. Its derivative holds almost everywhere, which is enough to integrate the inequality. The cancellation of \(u\) therefore does not assume a stationary, open-loop, or deterministic policy.

On the safe region,

\[
\dot W=1-q/s-\delta c/[\alpha(1-c)]
\le u_{\rm execution}-u_{\rm information}.
\]

The right-hand side is negative when the feasible interval is empty, and \(W\ge0\) gives the finite deadline. At equality of the two allocation thresholds, the constant common allocation preserves both boundaries, so the feasibility inequality is correctly non-strict. The singular initial case \(c=1\) is correctly separated: positive loss moves it below one at any positive time, after which the necessity proof applies.

Exact fraction arithmetic independently confirmed the interval \([2/3,3/4]\), minimum sustainable error \(1/11\), stricter reliability \(24/29\), allocation \(4/5\), and reserve decline \(-1/5\). The latter reaches zero exactly at time five, with reliability held at its floor. The endpoint remains safe; continuing for any additional positive duration is impossible under the theorem.

For the selection example, the two eigenvalue pairs are \((-4,-1/4)\) and \((-26/5,-1/26)\). The interior Jacobian has determinant \(-1/6\), so it is a saddle. The lower rectangle has nonpositive outward boundary derivatives and decreasing practice share; its limiting constant-coefficient reliability equation forces convergence to the low equilibrium. The upper rectangle gives the analogous high-equilibrium convergence. These arguments establish genuine bistability of the stated subsystem, not merely two stationary points. Because the reserve grows, they are not equilibria of the full three-dimensional state; the information note states this correctly.

## Scope of the integrated claim

The root document preserves the necessary qualifications. Its capability invariant is invariant under faithful redescription, not constant over physical time. Its finite-lifetime conclusion requires a finite adequate type description, finite lifetime bounds, required live parents, and no later external organizational entries. Its cumulative-loss version explicitly requires productive vulnerability, so a durable supplier does not silently get counted as renewed. Neither cycle theorem implies sufficient flow, feasible timing, full mutual closure, or differential selection.

The information theorem supplies a substantive bridge from independently specified correctness to maintained physical discrimination and execution. It does not define truth as persistence. Joining the results remains conditional on an application implementing its observation and execution capacities through supports satisfying the turnover premises; that bridge is stated rather than assumed universal.

No correction is needed to the integrated universal claim beyond making the accuracy and service-time quantifiers explicit as above. The prior empirical limits and lack of an exhaustive originality assessment remain correctly disclosed.

## Resolution after revision

The issue is resolved. Re-read the revised information note, Sections 2–4, and root document, Section 4. Both now explicitly condition accuracy on the realized pre-demand history and channel reliability, impose continuous readiness, and distinguish marginal risk and known isolated demand times from the proved operating requirement. The original findings above are retained as the audit trail, not as unresolved requests.

The newly added scheduled-assessment counterexample also checks. Full-maintenance and no-maintenance intervals give the exact recurrence \(h_{n+1}=(6/7)(1-e^{-7})+e^{-8}h_n\). The first assessment reliability is approximately 0.857116; every later assessment is above 0.856361, hence above \(24/29\approx0.827586\). The limiting assessment reliability is approximately 0.856649, while the intervening low point approaches 0.315143. The execution reserve starts at one, loses one during each maintenance interval, gains three during each subsequent interval, and never becomes negative. This confirms the intended strict separation between sampled accuracy and continuous readiness.

The routing example in [Turnover and closure](TURNOVER-AND-CLOSURE.md) now explicitly specifies \(\alpha_{12}=\alpha_{21}=1\), so \(b_1=b_2=1/2\) yields the displayed off-diagonal matrix and spectral radius without an implicit routing coefficient. No unresolved blocking finding remains from this review. The review verifies these scoped arguments and calculations; it does not establish their empirical applicability.
