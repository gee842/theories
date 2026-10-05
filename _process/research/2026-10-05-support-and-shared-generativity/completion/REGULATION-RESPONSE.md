# Exact response of a joint assay to a physical reaction change

5 October 2026. AI-assisted mathematical continuation for Ren. This note connects the autonomous gate in [Physical regulation](PHYSICAL-REGULATION.md) to an exact comparison identity. It complements the [construction-lag theorem](REGULATION-LAG.md) and the [joint capability bridge](JOINT-CAPABILITY-BRIDGE.md). The identity is proved for a finite stopped version of the declared stochastic process, with an explicit qualification for the original unbounded reserve.

It does not assign a favorable value to regulation. For each specified joint test, it expresses the observed probability difference through the changed physical reactions and their conditional downstream effects. The signs remain to be calculated.

## 1. A common finite state space

Use the physical state \(x=(R,C,Y,D,F,G,GF,YG)\), conserved material \(N=R+C+Y+D+G+GF+2YG\), and total packet inventory \(U=F+GF\). Augment it by the finitely many counters or flags needed for the assay. For example, a test requiring at least \(j\) recyclings and \(b\) assemblies needs counters saturated at \(j\) and \(b\); any first-construction flag is updated when construction occurs. This augmentation records the law analytically and supplies no measurements to a physical controller.

Fix an integer cutoff \(K\ge U_0\). Use a common state set \(S_K\) containing all material configurations satisfying the conservation law, all \(U\le K\), and all relevant flag values. Add an absorbing overflow state \(\partial\). Every transition that would first leave \(U\le K\) goes to \(\partial\) at its original rate. No overflowing capture is reflected or suppressed. This is a mathematical stopping construction, not a new physical rule.

The state set must be closed under every compared generator, including states unreachable from the initial preparation under one particular arm. Separate reachable graphs cannot be subtracted as matrices without a common closed embedding. Finite material, bounded \(U\), and saturated counters make \(S_K\) finite.

Let \(L_i\), \(i\in\{0,1\}\), be the two finite generators acting on column vectors of functions:

\[
(L_i v)(z)=\sum_r a_{i,r}(z)
\big[v(T_r^Kz)-v(z)\big],
\qquad L_i v(\partial)=0.
\tag{1}
\]

Here \(z\) includes the flags, \(T_r^K\) updates both physical state and flags or sends the state to overflow, and every reaction in the union of the two repertoires is listed, with propensity zero when absent. Define

\[
P_i(t)=e^{tL_i},\qquad
(P_i(t)v)(z)=\mathbb E_{i,z}[v(Z_t)].
\tag{2}
\]

For a terminal joint assay, use an indicator \(f:S_K\to\{0,1\}\) with \(f(\partial)=0\). For example,

\[
f(z)=\mathbf 1_{\{J\ge j,\ B\ge b,\ F\ge f_* ,\ R+C+Y+YG\ge1\}},
\tag{3}
\]

where \(f_*\) is the declared free-packet threshold. Dependence on event counts is terminal dependence on their augmented coordinates, not an assumption of memoryless physical observations. The same identity holds for any bounded terminal function, but capability claims below concern these specified joint tests.

## 2. Finite semigroup response theorem

For every horizon \(H\ge0\), initial augmented state \(z_0\), and function \(f\),

\[
\boxed{
\big[P_1(H)f-P_0(H)f\big](z_0)
=\int_0^H
\big[P_1(t)(L_1-L_0)P_0(H-t)f\big](z_0)\,dt.
}
\tag{4}
\]

**Proof.** The finite matrices are bounded and their exponentials differentiable. Set \(Q(t)=P_1(t)P_0(H-t)\). Since a matrix commutes with its own exponential,

\[
Q'(t)
=P_1(t)L_1P_0(H-t)-P_1(t)L_0P_0(H-t)
=P_1(t)(L_1-L_0)P_0(H-t).
\]

Integrating from zero to \(H\), using \(Q(H)=P_1(H)\) and \(Q(0)=P_0(H)\), and applying to \(f\) proves (4). No commutation of \(L_0\) with \(L_1\) has been used. ∎

This order of operators matters: \(P_i\) acts on functions. Implementations that evolve row probability distributions must transpose or order their matrices consistently.

## 3. Construction as the sole changed reaction

For the absent-versus-responsive comparison from the common preparation

\[
x_0=(0,1,1,1,1,0,0,0),
\]

one can retain the responsive fuel and Y binding constants \(\alpha=\mu=4\) in both generators and set only the baseline construction coefficient to zero. With no initial gate, those baseline binding reactions remain inaccessible; its law from \(x_0\) is exactly the absent arm. They must nevertheless remain defined when calculating baseline conditional futures from states containing gate material.

Let \(L_1\) use construction coefficient \(\kappa>0\), and let \(L_0\) use zero, with all other reactions identical. Then

\[
\big[(L_1-L_0)v\big](z)
=\kappa RF\,[v(T_Gz)-v(z)],
\tag{5}
\]

where the physical construction update is

\[
T_Gx=x+(-1,0,0,0,-1,1,0,0).
\]

This update includes any construction counter or flag. Recycling and assembly counters do not increment during construction. Construction reduces \(U\), so it does not itself create overflow from an interior state.

Write the conditional baseline success probability with \(s\) remaining units of time as

\[
u_0(s,z)=\big[P_0(s)f\big](z).
\tag{6}
\]

Equations (4) and (5) give the exact decomposition

\[
\boxed{
\widehat p_1(H)-\widehat p_0(H)
=\int_0^H
\mathbb E_{1,z_0}\!\left[
\kappa R_tF_t
\left\{u_0(H-t,T_GZ_t)-u_0(H-t,Z_t)\right\}
\right]dt,
}
\tag{7}
\]

with integrand zero at overflow and \(\widehat p_i(H)=[P_i(H)f](z_0)\).

The bracket compares two physical states at the same remaining horizon: one with a packet and usable plant unit consumed to form a gate, the other without that construction. The conditional future incorporates fuel sequestration, dissociation, inhibition, retained bound reproduction, leakage, structural wear, and later productive reactions. It therefore includes the construction cost through the actual state change. No separately assigned scalar reward or arbitrary penalty is required.

In this particular decomposition, the conditional futures use the baseline rule: existing gate material may bind and wear, but no further construction occurs under \(u_0\). Meanwhile the outer distribution is generated by the fully constructing process and includes histories with repeated construction. Together these two terms yield the exact total difference; the bracket alone is not a claim that later constructions have been ignored by the comparison.

The integrand can have both signs across states and remaining horizons. A fuel-dependent occupancy response in an isolated binding assay does not determine those signs. Calling the gate beneficial, or stipulating that the integral is positive, supplies no independent explanation. Evaluating this identity can instead locate which physical situations contribute to a computed gain or loss and how their frequencies matter.

Comparing the other arms can also use (4), but \(L_1-L_0\) then includes every changed propensity. For example, responsive versus inhibitor changes fuel association rather than construction; responsive versus burden changes both association channels. It would be incorrect to retain only the construction term for those comparisons.

## 4. Returning to the process with unbounded fuel

The proof above is finite-dimensional. It does not assert an unrestricted operator identity for unbounded generators on the original countable state space.

Couple each stopped chain to its corresponding physical chain up to the first overflow time \(\tau_K\). Let \(p_i(H)\) be the original success probability for the same joint assay and let

\[
o_i(H)=\Pr_i(\tau_K\le H).
\]

Since the stopped chain assigns failure to overflow,

\[
0\le p_i(H)-\widehat p_i(H)\le o_i(H).
\tag{8}
\]

The overflow-state mass of the exact finite chain equals \(o_i(H)\). Alternatively, an independent analytic bound is available. Total inventory satisfies

\[
U_t\le U_0+K_{{\rm candidate},i}(t),
\]

where candidate captures have Poisson rate \(g_iN\); binding and dissociation preserve \(U\), and construction, recycling, and leakage only reduce it. Thus

\[
o_i(H)\le\varepsilon_i(K,H)
:=\Pr\!\left\{\operatorname{Poisson}(g_iNH)\ge K-U_0+1\right\}.
\tag{9}
\]

If \(\Delta_K\) denotes the exact finite integral in (7), the physical probability difference satisfies the sharper asymmetric enclosure

\[
\boxed{
\Delta_K-o_0(H)
\le p_1(H)-p_0(H)
\le\Delta_K+o_1(H).
}
\tag{10}
\]

One may replace \(o_i\) by any validated upper bound such as \(\varepsilon_i\). The error on the lower side belongs to the baseline arm; the error on the upper side belongs to the modified arm. As \(K\to\infty\) at fixed \(H\), (9) tends to zero. Hence the finite response values converge to the true probability difference. This conclusion does not require, and does not by itself establish, term-by-term passage of the integrand to an infinite-generator formula.

Numerical matrix exponentials and numerical quadrature introduce additional errors. If a computed response value has a verified absolute error \(\eta\), enlarge (10) by \(\eta\) on both sides. If instead two independently computed success probabilities have errors \(\eta_0,\eta_1\), use \(\eta_0+\eta_1\) for their difference. Overflow bounds alone do not make ordinary floating-point output a rigorous certificate. The current [regulator experiment protocol](../../../../experiments/shared-renewal-capability/regulation/PROTOCOL.md) states that distinction explicitly.

## 5. What this finishes and what remains a separate claim

The response identity connects a change of declared physical mechanism to the probability of a joint consequence, with resource costs, construction delay, environmental support, and ensuing interactions retained in the same process. It is an exact diagnostic interface; it is not a theorem that the interface's value has a favorable sign.

Each assay has its own \(f\), conditional future \(u_0\), and response. A reliable capability-region comparison must check the joint profiles at the declared common reliability. Region inclusion is neither implied by an improved recycling probability nor equivalent to monotonicity of every success probability. For a finite assay vocabulary, inclusion means that every profile certified in the baseline also clears the reliability threshold in the modified process; strict expansion additionally needs at least one new certified profile. Proofs or numerical certificates must account for threshold uncertainty.

The comparison concerns installed autonomous processes under the stated initial preparation and support. It does not optimize over all physically possible controllers, derive the reaction repertoire, or identify an ethical ordering. Further positive results must come from the dynamics or verified probabilities, rather than being inserted into the meaning of the word regulation.
