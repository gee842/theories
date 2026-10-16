# Review of recurrent support and information integration

Internal mathematical cross-review, 5 October 2026. Reviewed [Turnover and closure](TURNOVER-AND-CLOSURE.md) and [Root foundation](ROOT-FOUNDATION.md), including their use of [Information and renewal](INFORMATION-AND-RENEWAL.md). This is a review of the conditional arguments, not empirical validation or an independent priority assessment.

## Findings requiring clarification

**1 The exact information threshold requires continuous readiness.** Theorem R4 is correct for its simultaneous inequalities c(t)≥c* and b(t)≥0 at every time. However, Section 4 first introduces accuracy as a per-task requirement, which can be read as accuracy only at known discrete demand times. That weaker requirement does not imply the continuous capacity floor used in the proof. Add an explicit sentence that service must be ready at every time, or that a demand may arrive at any time. If only a specified sparse schedule matters, a different scheduling problem must be solved.

A concrete counterexample to the broader discrete-demand interpretation uses exactly the strict example's parameters: α=6, δ=1, s=4, q=1, ε=5/58, c*=24/29, initial c=c* and b=1. Set u=1 for one time unit, then u=0 for one time unit, repeating. Issue demands only at times 1,3,5,…, the ends of the full-maintenance intervals. After every such interval,

\[
c_{\rm demand}=\frac67+\left(c_{\rm start}-\frac67\right)e^{-7}
\ge\frac67(1-e^{-7})>\frac{24}{29}.
\]

The strict inequality follows from e⁷>1+7+49/2>29 and (6/7)(1−1/29)=24/29. Thus every demanded response has the required error guarantee. Each maintenance interval spends one reserve unit, and each off interval adds three, so b remains nonnegative and gains two units per cycle. Indefinite demanded service is possible, although u_min=4/5>u_max=3/4. The channel falls below its floor between demands, so this is **not** a counterexample to continuous readiness or the stated differential certificate. It shows why the quantifier over time must remain explicit. An eight-cycle numerical check corroborated these exact inequalities; the proof does not depend on that simulation.

**2 Specify the routing coefficients in the spectral witness.** The final numerical example of Turnover Section 5 says that two-way routing and b₁=b₂=1/2 give B with off-diagonal entries 1/2. This additionally needs α₁₂=α₂₁=1 and zero diagonal routing. With the same routing graph and b values but α₁₂=α₂₁=4, the spectral radius is two instead. The theorem is correct; the witness currently leaves its numerical routing assumption implicit.

## Results that withstand the counterexample search

**Finite episode lifetime bound.** The topological induction is valid. It allows arbitrarily many initial episodes and arbitrarily many finite births: all initial birth times are at most zero, and every post-zero birth has a live predecessor. In a finite acyclic type graph, no parent chain can traverse more than the graph's finite path length. The bound concerns the end time of functioning episodes, not their number. AND requirements do not invalidate the conservative maximum bound; retaining any actually necessary live parent gives the needed inequality. Omitted persistent intermediates or spontaneous organization evade the theorem only by violating a stated premise.

**Recurrent support ancestry.** Finite dimensionality and finite initial reserves force at least one unbounded incoming provision when loss is unbounded. Productive vulnerability then allows the predecessor step to be repeated. Without it, a durable supplier feeding a vulnerable dependent is a real counterexample; the document already presents this. The external-source alternative, downstream noncyclic vertices, non-simultaneous edges, finite total loss, and infinitely many novel support types are all treated correctly. The theorem establishes recurrent ancestry, not full organizational closure or favorable selection.

**Spectral obstruction.** Substituting the nonnegative bounds yields

\[
S_i\le a_i+b_iL_i
\le a_i+b_i[c_i(0)+e_i]+\sum_jb_i\alpha_{ji}S_j,
\]

so the indexing Bᵢⱼ=bᵢαⱼᵢ is correct. With ρ(B)<1, multiplication by the nonnegative inverse preserves the componentwise inequality and bounds S uniformly. Routing and the capacity balance then bound every Lᵢ uniformly. No rate equation, lower growth bound, or simultaneous attainment of the routing limits is needed. Positive changes of service units give the claimed similarity transformation. The condition ρ(B)≥1 is only necessary under these bounds; the document correctly declines to interpret it as sufficient continuation or an exact nonlinear bifurcation threshold.

**Integration with the information theorem.** The information and execution obstruction is a separate statement from the turnover graph theorem. Combining them is justified only after an application establishes that the relevant information and execution supports meet the finite-type lifetime or productive-vulnerability premises. Root Section 6 states this condition explicitly. No unjustified implication from information loss to full mutual closure was found. Root R4 permits q≥s even though its companion assumes q<s; this is harmless because then u_max≤0<u_min and the necessity proof still establishes impossibility. The claimed feasible interval remains empty.

## Deadline endpoints

The lifetime theorem safely says that no relevant functioning occurs **after** D. Whether the endpoint D itself is functioning depends on the convention for an episode's expiration. No stricter assertion is needed, and the current theorem uses the correct formulation.

The information theorem similarly establishes that an acceptable interval cannot extend **beyond** T=W(0)/Δ. Equality can be attained with both requirements still satisfied at the endpoint. In the sharp example, c(5)=c* and b(5)=0; the allocation cannot continue for any positive additional duration while preserving both inequalities. It would be incorrect to say that an inequality must already be violated at or before time five. The current root text says an upper bound of five that is attained, which is consistent. Keep this endpoint distinction in summaries and figures.

The perfect initial channel c(0)=1 is correctly handled by starting the finite certificate at a positive time. Positive loss and bounded maintenance imply that c immediately becomes less than one; a finite initial reserve stays finite on any finite interval. The logarithmic singularity therefore does not enable indefinite operation in the infeasible parameter regime.

## Assessment

No mathematical blocker was found in the lifetime, recurrent-support, spectral, or continuous-readiness theorems under their stated premises. Clarification 1 protects the interpretation of the operational optimum against a genuine scheduling counterexample. Clarification 2 completes an otherwise valid numerical witness. None of these results establishes that all physical systems share the premises, or that successful support reproduction certifies truth or moral legitimacy.

## Resolution after correction

Both findings are resolved in the corrected documents. Root Section 4 now explicitly requires conditional accuracy for each realized history and current reliability, continuous readiness, and both physical inequalities along every realized effort schedule. It distinguishes this from marginal accuracy or accuracy only at known isolated times. Information Sections 2 and 3 contain the same qualification, and Section 4 preserves the sparse-assessment counterexample rather than suppressing it. Turnover Section 5 explicitly sets α₁₂=α₂₁=1 in the numerical routing example.

The new assessment recurrence is correct. Starting from an assessment reliability hₙ, one off interval yields e⁻¹hₙ, and the next full-maintenance interval yields

\[
h_{n+1}=\frac67(1-e^{-7})+e^{-8}h_n.
\]

Its fixed point is [(6/7)(1−e⁻⁷)]/(1−e⁻⁸), approximately 0.8566486176, consistent with the document's rounded 0.85665. The first assessment exceeds 24/29 because full maintenance moves the initial value toward 6/7; all later assessments exceed the strict lower bound already proved above. Sequential integration and the recurrence were checked numerically for ten iterations, and the strict lower-bound argument was checked using exact fractions. Reserve changes and the deadline endpoint statements remain correct.

No unresolved finding remains from this review. This resolution certifies the reviewed scope and calculations; it does not enlarge the physical class covered by the assumptions.
