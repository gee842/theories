# Does this regulator address a demonstrated productive conflict?

5 October 2026. AI-assisted structural audit for Ren, continuing the study at repository commit `9aa1b3a`. This preserves the original models, protocols and negative regulator comparison. It adds mathematical distinctions and a conditional mechanism class; it does not alter the experiment or report a newly successful regulator.

**Finding.** In the original plant network, recycling is the only productive reaction that directly consumes free fuel. It converts a packet and degraded material into usable precursor R without reducing the declared work-equivalent stock. The supplied inhibitor therefore has not been shown to protect a second productive fuel demand. A lower free-fuel probability establishes loss of immediate packet availability; it does not by itself establish loss of subsequent productive capability. Conversely, stored R cannot be freely converted back into a packet, so this distinction does not make fuel availability irrelevant.

The full process still contains timing and allocation conflicts. This audit does not prove that faster recycling always helps it, or that inhibition can never help it. It identifies what is and is not already supplied by the reaction law.

## 1. What recycling actually changes

Use the notation and unit volume/packet size of the [stochastic realization](STOCHASTIC-REALIZATION.md). Temporarily omit the regulator. The original plant has material counts R,C,Y,D, fuel F, and total recycling intensity

\[
J=kFD(C+\theta Y).
\tag{1}
\]

Its two catalytic recycling channels have the same state increment

\[
T_{\rm rec}x-x=(+1,0,0,-1,-1)
\quad\text{in coordinates }(R,C,Y,D,F).
\]

For plant activity \(A=R+C+Y\) and reduced work-equivalent stock \(W=F+R+C+Y\), every recycling event therefore has

\[
\boxed{\Delta F=-1,\qquad \Delta R=+1,\qquad
\Delta A=+1,\qquad \Delta W=0.}
\tag{2}
\]

The packet is committed to a material form, rather than destroyed in this ledger. R has no intrinsic wear reaction, although the autonomous reactions \(R\to C\) and \(R+Y\to2Y\) can immediately begin committing it to structures that do wear. Calling R a stable intermediate refers only to the absence of its own wear channel; it does not grant an actor the ability to hold R indefinitely.

The exact work drift is

\[
\mathcal L_\theta W=(g-b)C-dY-\ell F.
\tag{3}
\]

Recycling does not enter (3) directly. At its successor state,

\[
\boxed{(\mathcal L_\theta W)(T_{\rm rec}x)
-(\mathcal L_\theta W)(x)=\ell.}
\tag{4}
\]

The transfer into R removes one packet from exposure to leakage without changing C or Y at that instant.

This also yields a local comparison theorem. Increase only the supplied coefficient \(\theta\) by \(\Delta\theta>0\), starting both processes at the same finite state. Then

\[
(\mathcal L_{\theta+\Delta\theta}-\mathcal L_\theta)W=0,
\]

\[
(\mathcal L_{\theta+\Delta\theta}^{\,2}-\mathcal L_\theta^{\,2})W
=k\Delta\theta FDY\,\ell.
\]

Consequently, as \(h\downarrow0\),

\[
\boxed{
\mathbb E_{\theta+\Delta\theta,x}W_h-
\mathbb E_{\theta,x}W_h
=\frac{k\Delta\theta FDY\,\ell}{2}h^2+O(h^3).
}
\tag{5}
\]

Meanwhile the first-order differences of expected free fuel and activity are respectively \(-k\Delta\theta FDYh\) and \(+k\Delta\theta FDYh\). These are compatible observations. They do not define a single ordering of the state. Formula (5) is not an assertion that W captures every useful function or that its finite-time expectation is globally monotone in \(\theta\).

The expansions are valid locally for this countable-state process: material is bounded, the total hazard is affine-bounded in F, and W can grow by at most the number of captured packets. The fixed-depth jump expansion used in the [lag proof](../../../history/2026-10-05-support-and-shared-generativity/completion/REGULATION-LAG.md), together with the corresponding moment bound from linear pure-birth domination, controls the remainder for this linear observable.

## 2. A restricted monotonicity theorem that makes the distinction exact

Consider the storage part of the mechanism under explicit restrictions. Let a fixed pool of M material units be either degraded D or usable R, with D=M−R. Let fuel arrive by the same locally finite exogenous counting process in two coupled systems. Fuel leaks at rate \(\ell F\); R has no wear, commitment, export or consumption channel. A common externally specified, locally bounded catalytic availability gives recycling rates

\[
c_i(t)(M-R_i)F_i,
\qquad 0\le c_0(t)\le c_1(t),\quad i=0,1.
\tag{6}
\]

The catalytic functions are nonnegative, predictable and locally bounded with respect to the common external history. They may depend on that history, but not on a hidden choice of different histories for the two systems. Any physical support needed to fix these functions belongs to this restricted module's assumptions. Define

\[
Q_i=R_i+F_i.
\]

**Storage comparison theorem.** From the same initial state there is a coupling with

\[
\boxed{R_1(t)\ge R_0(t),\qquad Q_1(t)\ge Q_0(t)
\quad\text{for every }t\ge0.}
\tag{7}
\]

Therefore every increasing function or upward joint assay of \((R,Q)\) is at least as favorable under faster recycling, within these restrictions.

**Proof.** Couple common arrivals. Couple the two recycling clocks at the smaller of their current rates and allow the excess clock to act in its own system; do the same for leakage clocks. A recycling jump raises R by one and leaves Q unchanged. At a boundary where \(R_1=R_0\) and \(Q_1\ge Q_0\), one has \(F_1\ge F_0\), so the faster system's recycling rate is at least the slower system's. An unmatched jump cannot then make \(R_0>R_1\). Away from that boundary, a one-unit jump of the slower system cannot cross the integer gap.

A leakage jump lowers Q by one and leaves R unchanged. At a boundary where \(Q_1=Q_0\) and \(R_1\ge R_0\), one has \(F_1\le F_0\), so the faster system's leakage rate is no greater. An unmatched leak cannot then make \(Q_1<Q_0\). The integer-gap argument handles the remaining states. Common arrivals preserve both inequalities. On each finite interval, recycling and leakage together consume no more packets than initially present plus the locally finite arrivals, which also establishes nonexplosion. ∎

Free fuel \(F=Q-R\) is not increasing in this partial order. Faster recycling can reduce it even while increasing stable usable stock and total retained work in the module. This is a concrete reason that a free-fuel assay and a productive-stock assay answer different questions.

The theorem does not cover the original full network: R is automatically committed to C or Y, those structures wear, catalytic populations evolve, and capture depends on C. It also excludes gate construction. Removing any of these restrictions requires a new coupling or another proof; the module theorem cannot be promoted to global dominance by analogy.

## 3. What the supplied inhibitor changes—and what it does not

For the [G/GF/YG network](../../../history/2026-10-05-support-and-shared-generativity/completion/PHYSICAL-REGULATION.md), write

\[
L=Y+YG,\quad T=G+GF+YG,\quad U=F+GF,
\quad K=\kappa RF.
\]

The exact drift identities include

\[
\mathcal LR=J-aR-\beta RL-K,
\qquad
\mathcal LL=\beta RL-dL,
\]

\[
\mathcal LA=J-bC-dL-K,
\quad A=R+C+Y+YG,
\]

\[
\mathcal LW=gC-\ell F-\ell_bGF-K-bC-dL-\delta T.
\tag{8}
\]

Binding \(G+Y\to YG\) preserves L, A, U, W, C and F. It reduces the immediate recycling intensity by \(k\theta FD\). It does not remove Y's reproductive channel, because the model explicitly retains \(R+YG\to Y+YG\).

At a fixed current state, the hazards for a usable precursor to be assigned to C, Y or G are proportional to

\[
\boxed{a:\beta L:\kappa F.}
\tag{9}
\]

For example, conditional on a current jump being a C-or-Y allocation event, its C probability is \(a/(a+\beta L)\). Binding Y changes neither this ratio nor which product an already supplied R can form. This is a statement about competing instantaneous propensities; other events can change L or F before the next allocation occurs. In the well-mixed network, an R produced by Y-catalyzed recycling is not earmarked for Y, and an R produced by C-catalyzed recycling is not earmarked for C.

There is genuine competition between C assembly, Y reproduction and gate construction for R. The selected inhibitor does not directly regulate the C-versus-Y branch. It instead regulates the supply of their common precursor. Indirect effects through later population changes are possible, but their sign has not been established by (9).

In the original network, the fuel-consuming plant channel is recycling. C assembly and Y reproduction need R, not an additional packet. G adds a second direct fuel demand—its own construction. Thus the extension creates an additional resource competitor before establishing that its regulation protects a pre-existing fuel-dependent productive task.

This matters even for the work calculation. In the full G network,

\[
(\mathcal LW)(T_{\rm rec}x)-(\mathcal LW)(x)
=\ell-\kappa(F-R-1).
\tag{10}
\]

The new term is the change in the automatic construction hazard, since recycling sends \(RF\) to \((R+1)(F-1)\). Recycling can thereby expose newly available R to a costly G-building channel. A benefit obtained by suppressing that self-created burden would be a real comparison within the extension, but it would not establish that the original plant needed the inhibitor to solve an independent fuel-allocation problem.

Neither (8) nor (10) proves that every regulator effect is harmful. The completed [negative comparison](../../../history/2026-10-05-support-and-shared-generativity/completion/REGULATION-REVIEW.md) remains the evidence for its declared cases. The present audit diagnoses a missing demonstrated opportunity, rather than deriving all those numerical inequalities from a single drift sign.

## 4. Readiness is consequential, but needs a functional interpretation

The existing \(F_H\ge1\) test is an honest test of immediately available fuel. Its lower probability is not merely a change of names: there is no supplied \(R\to D+F\) reaction that reverses the commitment. A packet-consuming task can distinguish the states. However, a delivered assembly task can distinguish them in the opposite direction: an R can enter \(R\to C\) directly, while a packet still needs degraded material, a catalyst, and a recycling event to supply that R.

The original short-time comparison establishes a delivery/readiness tradeoff. It does not demonstrate that lower F harms every continuation, nor that withholding recycling improves some downstream delivered function after regulation costs. That latter opportunity was not established before testing the proposed G architecture.

A functional continuation assay can stay inside the existing repertoire. For fixed horizons H and \(\tau\), for example, test the joint event

\[
\left\{J_H\ge j,\ B_H\ge b,\
B_{H+\tau}-B_H\ge1,\
A_s\ge1\ \text{for }0\le s\le H+\tau\right\}.
\tag{11}
\]

The second assembly must actually occur during the continuation interval. It may be funded by stored R or by later recycling; the test does not decide in advance that a packet is the superior preparation. The time boundary resets an analyst's event count, not a costless physical controller. Other common assays can require specified surviving C/Y structures or reliable recovery from an explicitly modeled common disturbance. Their resource and time requirements must be stated before interpreting the result.

If the intended benefit is preserving fuel for a *different* productive function, that function needs an actual reaction or implementable task in the model. Its inputs, products, time window, and common availability to both arrangements must be specified. Counting regulator molecules or favorable binding occupancy does not supply such a delivered function. Adding it would extend the model and assay vocabulary; it would not reverse the already completed eight-profile comparison.

## 5. Where an actual opportunity appears in the response identity

For a declared terminal joint assay f and the finite common-state construction of [Regulation response](../../../history/2026-10-05-support-and-shared-generativity/completion/REGULATION-RESPONSE.md), let \(u_0(s,z)=P_0(s)f(z)\). The exact change from modifying recycling intensity contains terms of the form

\[
\Delta J(z)\,[u_0(s,T_{\rm rec}z)-u_0(s,z)].
\tag{12}
\]

The bracket is not determined by the decrement in F or the increment in R alone. Near a task that specifically needs a free packet it can be negative; near a task that needs usable R it can be positive. Determining that sign in the actual process is precisely the missing functional calculation.

For the real constructed gate, one must retain the construction, binding, dissociation and wear changes in the full generator response, rather than replacing them with a free change of J. Its contributions are averaged along the changed process, with the conditional futures evaluated as specified in the exact identity. This includes which states the mechanism actually visits and the time left to repay construction.

The identity can locate a favorable or unfavorable opportunity. Defining an opportunity as a positive value of its integral would not explain its existence. A mechanistic certificate must instead derive the relevant resource conflict and its rates.

## 6. A conditional opportunity certificate for a finite kinetic module

The following proposition gives a class criterion. It is a conditional kinetic module, not a newly successful integrated construction model or a claim that the present G network satisfies the class. Its physical application requires a separately supplied reaction graph and ledger. It also provides a way to reject an unsuitable graph before a parameter search.

Fix one joint delivery event. Suppose a closed reaction module, or an **exact** Markov lumping of its full physical states, has:

- An unregulated opportunity state S, with completed joint delivery at total rate a and irreversible loss of that delivery opportunity at total rate b.
- A construction reaction at finite total propensity \(\gamma>0\), taking S to a built-but-unbound state B. Its material and packet debits are included in B. The joint delivery remains physically feasible after those debits. For a single state with the existing fabrication reaction, \(\gamma=\kappa RF\); the propensity is distinct from its mass-action coefficient.
- From B, delivery at rate \(a_B\), irreversible opportunity loss at rate \(b_B\), and inhibitor binding to state I at finite rate \(\mu\).
- From I, delivery at rate \(a_I\), irreversible opportunity loss at rate \(b_I\), and dissociation to B at rate \(\nu\).

Delivery and loss are absorbing for this episode's test. The word irreversible must be justified by the physical state and declared episode: for example, a required non-substitutable substrate has been committed to a product with no return path. It cannot be assigned merely because an event was called undesirable. Likewise, all displayed rates must be calculated from reaction propensities and physical states. If a block contains several microstates, exact lumping requires its total exit rates to each other block to be constant across those microstates. Without that property, use the full generator; substituting fitted constant rates does not make this an exact reduction.

To represent formation from absence, S must be realized by states with all regulator forms absent, and the transition to B must be an actual permitted fabrication path with its material, fuel and time costs. If fabrication needs intermediate states rather than one exponential reaction, those states must be retained or exactly eliminated; an assigned construction clock is not a derivation. None of these realization requirements is established by drawing the three-state module.

Assume \(a+b>0\), \(a_B+b_B>0\), \(a_I+b_I>0\), and finite nonnegative coefficients. Let \(p_0\) and \(p_1\) be eventual episode success probabilities from S without and with construction, respectively. First-step equations give

\[
p_0=\frac{a}{a+b},\qquad
p_B=\frac{a_B+\mu p_I}{a_B+b_B+\mu},\qquad
p_I=\frac{a_I+\nu p_B}{a_I+b_I+\nu}.
\]

Writing \(s_B=a_B+b_B+\mu\) and \(s_I=a_I+b_I+\nu\), solve these equations to obtain

\[
p_B=\frac{a_Bs_I+\mu a_I}{s_Bs_I-\mu\nu},
\qquad
\boxed{p_1-p_0=\frac{\gamma}{a+b+\gamma}(p_B-p_0).}
\tag{13}
\]

The denominator is positive under the stated premises. Therefore paid regulation improves this joint delivery probability exactly when the **derived physical rates** satisfy

\[
\boxed{(a+b)(a_Bs_I+\mu a_I)
>a(s_Bs_I-\mu\nu).}
\tag{14}
\]

This condition compares physical completion and opportunity-loss kinetics after resource debits. It does not insert a scalar value for goodness, assume optimal control, or suppose that every binding response is beneficial.

A transparent subclass makes the rate tradeoff explicit. Suppose \(a,b>0\), the stipulated post-construction completion rates are \(a_B=a_I=\chi a\), with \(0<\chi\le1\); unbound loss remains \(b_B=b\); and binding reduces a physically identified competing-loss reaction to \(b_I=r b\), with \(r\ge0\). A physical application must derive \(\chi\) and r from the changed substrate counts and reaction access. A reduction to \(\chi a\) is only a kinetic burden; it does not by itself provide a complete material/work ledger or realize paid fabrication. Algebra reduces (14) to

\[
\boxed{\mu(\chi-r)>
(1-\chi)(\chi a+r b+\nu).}
\tag{15}
\]

For \(\chi<1\), this requires \(r<\chi\): inhibition must reduce the competing-loss hazard proportionally more than the construction debit reduces productive completion. Finite binding must then be fast enough to overcome the cost and dissociation. This is a kinetic and stoichiometric opportunity condition; a correct fuel-response sign alone is insufficient. When r is not below \(\chi\), no finite increase of the binding rate can meet (15) within this subclass.

All rates, including construction and binding, remain finite. Under the absorption assumptions, eventual success is the limit of finite-horizon success. If (14) is strict, improvement therefore occurs at some finite horizon. It need not occur at all horizons. In fact the local difference from S is

\[
p_1(h)-p_0(h)=\frac{\gamma(a_B-a)}2h^2+O(h^3),
\tag{16}
\]

so the stipulated burden \(a_B<a\) produces an early disadvantage even when a later advantage follows from (14). This retains a finite construction delay and a kinetic disadvantage. Physical payment still requires the separate state-level ledger and realized fabrication path just specified.

The proposition is for one jointly defined episode, not indefinite survival or an entire capability region. Several joint profiles require their own common assays and checked probability bounds. A larger region at a chosen reliability follows only if the required profiles actually clear that threshold; a favorable result for one profile is not enough.

As an arithmetic check, 200 exact-rational parameter cases verified the first-step equations, the equivalence of (14) and (15) in the stated subclass, and the generator coefficient in (16). The displayed derivations supply the general proofs; these checks do not identify a physical realization of the class.

## 7. Consequence for the present research line

The existing model supplies material competition, irreversible commitment, delayed effects and paid binding. It does not yet supply the demonstrated downstream opportunity required to interpret fuel inhibition as useful regulation. Specifically, its selected gate leaves the R-to-Y competitive branch active, suppresses production of the common precursor, and consumes the same precursor and fuel to construct itself. No identification of the present process with the favorable mechanism class above has been proved.

The defensible next explanatory claim is consequently conditional: a physically realized paid regulator needs an accessible loss of future productive opportunity that its inhibition can avert strongly enough to repay its costs. Equations (13)–(16) identify a precise rate condition in one conditional kinetic module. They do not establish a new physically realized net gain or close the physical-to-capability interface. Establishing the physical states, ledger, initial absence and exact reduction—or demonstrating a functional continuation advantage directly in the full generator—remains necessary for this particular architecture.

This audit neither treats fuel preservation as an end in itself nor dismisses it. It distinguishes immediately available packets, committed usable material, and reliably completed further activity. The coupled physical process and the common joint task determine how those states differ.
