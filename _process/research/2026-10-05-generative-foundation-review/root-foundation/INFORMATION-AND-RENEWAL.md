# Information and the renewal of corrective capacity

Research development, 5 October 2026. This note connects a statistical limit on informed response to the physical reproduction of its information channel and means of execution. It extends the [adaptive optimum](../final-synthesis/ADAPTIVE-OPTIMUM.md) and [integrated theory](../final-synthesis/INTEGRATED-THEORY.md). The main result is an exact necessary and sufficient condition for indefinite operation in a specified class, together with a finite exhaustion bound valid for every admissible time-varying allocation. An explicit example attains that bound. A second example shows how endogenous selection can stabilize either adequate or inadequate information provision.

The claim is conditional and operational. It concerns reliable discrimination and executable response under declared laws of information loss and provision. It does not identify persistence with truth, ethical legitimacy, or a universal thermodynamic price of knowledge. The proofs are self-contained; the physical equations are modeling assumptions awaiting identification in an application.

## 1 Information must distinguish the cases that require different responses

Consider two equally likely circumstances, θ=0 and θ=1, requiring responses 0 and 1 respectively. Let the actual observation Y have finite conditional laws P₀ and P₁. A randomized response rule is a number r(y) in [0,1], the probability of choosing response 1 after y. Its average error is

\[
e(r)=\frac12\sum_y\bigl[P_0(y)r(y)+P_1(y)(1-r(y))\bigr].
\tag{E1}
\]

Define the distinguishability

\[
D(P_0,P_1)=\frac12\sum_y|P_0(y)-P_1(y)|.
\tag{E2}
\]

**Proposition E1.** The minimum average error over every response rule using this interface is

\[
e_* =\frac{1-D(P_0,P_1)}2.
\tag{E3}
\]

**Proof.** For each y, minimize the affine summand in (E1) by choosing the more likely circumstance. The minimum is one half of Σᵧ min{P₀(y),P₁(y)}. Since min{a,b}=(a+b−|a−b|)/2 and each law sums to one, the sum is 1−D. Randomization cannot lower an affine minimum. ∎

This is the standard total-variation characterization of binary testing, not a new theorem of this project; see [Yihong Wu's statistical information theory notes, Theorem 4.2](https://www.stat.yale.edu/~yw562/teaching/598/lec04.pdf). Its role here is to give an operationally calibrated requirement on an information channel. An average error requirement e≤ε<1/2 necessitates D≥1−2ε. A separate worst-case error bound for each circumstance implies the same necessity, although equality need not be attainable for an arbitrary asymmetric channel.

If the observation is subsequently processed through a channel that does not know θ except through Y, its distinguishability cannot increase: expanding the difference of the processed laws and applying the triangle inequality gives D(P₀K,P₁K)≤D(P₀,P₁). More computation can help implement a better decoder, but cannot create distinctions absent from the actual input. This leaves open the possibility of gathering an additional observation or changing the environment; those are new causal inputs.

## 2 An exact channel linking accuracy to physical capacity

At each demand, the circumstance θ is a fresh fair bit independent of all earlier circumstances and the controller's past. The controller receives the correct bit with probability c and an erasure symbol ? with probability 1−c. Conditional on c, erasure is independent of θ. Thus

\[
P_0^c=(c,0,1-c),\qquad P_1^c=(0,c,1-c)
\tag{E4}
\]

on the alphabet {0,1,?}. Here c∈[0,1] is a physical reliability parameter, not a belief or a number of bits. For this channel D(P₀ᶜ,P₁ᶜ)=c and

\[
e_*(c)=\frac{1-c}{2}.
\tag{E5}
\]

The same minimum holds for worst-case error across the two circumstances if randomized decisions are permitted: follow an observed bit and choose a fair random response after erasure. Its error is (1−c)/2 in each circumstance. The average-error lower bound proves no rule can have a smaller maximum error. Any implementation cost of decoding or randomization belongs in the service costs below.

Fix an error tolerance 0<ε<1/2 and write

\[
c_* =1-2\varepsilon.
\tag{E6}
\]

The channel can meet the specified per-demand error tolerance exactly when c≥c*. The guarantee is conditional on each realized pre-demand history and current channel reliability; it does not merely average accuracy across different histories. This is a probability requirement, not a guarantee that every realized response is correct. The new circumstance is independent of history, so additional memory of past demands cannot improve (E5). Persistent or predictable circumstances would define a different problem in which historical information can help.

The capacity laws below evolve in continuous service time. Equations (E4)–(E5) specify the channel that would be available to a demand at any such time; they do not posit an uncountable collection of physically simultaneous independent queries. A real implementation must specify its demand schedule and calibrate costs at that rate.

## 3 Accuracy and execution draw on a shared source of provision

Let u(t)∈[0,1] be the fraction of an available provisioning input assigned to maintaining the observation channel. The remainder supplies the means of executing responses. Assume

\[
\dot c=\alpha u(1-c)-\delta c,
\qquad
\dot b=s(1-u)-q,
\tag{E7}
\]

where α,δ,s>0 and 0<q<s. The execution reserve is b≥0. The term δc represents loss of channel reliability, and αu(1−c) represents saturating repair or replacement. The provision rate s(1−u) and expenditure rate q are measured in the same units of executable support per unit time. The expenditure includes the stipulated costs of sensing, processing, and service at the declared demand rate. The model assumes responses can be executed while this reserve remains nonnegative. Its rights, permissions, and actuator reliability are fixed premises here, not inferred from the budget.

Controls may be any measurable functions of time and accessible history, including randomized controls. The impossibility result below holds pathwise for every realized allocation. Initial reserves are finite, with c(0)∈[c*,1) and b(0)≥0. We require continuous readiness: both c(t)≥c* and b(t)≥0 must hold at all times, so the stated conditional accuracy is available whenever a demand arrives. Accuracy required only at known isolated demand times is a weaker problem to which the necessity theorem does not apply. Demands cannot simply be dropped to reduce q while retaining the same service claim.

Define

\[
u_{\rm information}=\frac{\delta c_*}{\alpha(1-c_*)},
\qquad
u_{\rm execution}=1-\frac qs.
\tag{E8}
\]

**Theorem E2.** Indefinite satisfaction of both requirements is possible from any finite initial state in the stated safe region if and only if

\[
\boxed{u_{\rm information}\le u_{\rm execution}.}
\tag{E9}
\]

When (E9) holds, every constant allocation in [u_information,u_execution] suffices. If it fails, no adaptive or time-varying allocation can satisfy both requirements indefinitely. More precisely, if Δ=u_information−u_execution>0, every interval of acceptable service has length at most

\[
\boxed{
T\le \frac{\displaystyle b(0)/s+
\frac1\alpha\log\!\frac{1-c_*}{1-c(0)}}{\Delta}.
}
\tag{E10}
\]

**Proof of sufficiency.** At c=c*, equation (E7) gives ċ=α(1−c*)(u−u_information)≥0. At c=1 its derivative is −δ<0. Thus [c*,1] is forward invariant. Meanwhile ḃ=s(u_execution−u)≥0. A constant allocation in the declared interval preserves both requirements from every admissible initial state. It needs no hidden-context observation or knowledge of the true bit. ∎

**Proof of necessity and the deadline.** On the safe region with c<1, introduce the nonnegative reserve certificate

\[
W(c,b)=\frac bs+\frac1\alpha\log\!\frac{1-c_*}{1-c}.
\tag{E11}
\]

It has units of time and combines available execution support with reliability above the required floor. It is a proof certificate, not a utility function and not a claim that actual resources can be exchanged reversibly. Along every trajectory of (E7),

\[
\begin{aligned}
\dot W
&=(1-u)-q/s+u-\frac{\delta c}{\alpha(1-c)}\\
&=u_{\rm execution}-\frac{\delta c}{\alpha(1-c)}\\
&\le u_{\rm execution}-u_{\rm information}=-\Delta.
\end{aligned}
\tag{E12}
\]

The control cancels. While both requirements hold, W≥0, so integration gives 0≤W(T)≤W(0)−ΔT, yielding (E10). For Δ>0, indefinite service is impossible for every finite initial reserve and every control schedule. This proves necessity. ∎

The exclusion of c(0)=1 avoids the logarithm's singularity, not a physical loophole. With δ>0, even maximal repair satisfies ċ≤α(1−c)−δc, whose solution starting at one is strictly below one at every positive time. An arbitrary bounded control therefore immediately enters c<1. Apply the impossibility proof from any subsequent time with finite b. Sufficiency includes c(0)=1 directly.

Equivalently, the smallest error tolerance permitting indefinite service in this model is

\[
\boxed{
\varepsilon_{\min}
=\frac{\delta}{2[\alpha(1-q/s)+\delta]}.
}
\tag{E13}
\]

This is an attained optimum for the specified model and simultaneous requirements. It is not a universal optimal accuracy of embodied intelligence. Changing the technology, supplied resources, demand rate, allowable delay, or service obligation changes the optimization problem.

## 4 Exact witnesses and a sharp exhaustion time

Take α=6, δ=1, s=4 and q=1. For ε=1/10, the required reliability is c*=4/5. The exact feasible interval is

\[
\frac23\le u\le\frac34,
\qquad \varepsilon_{\min}=\frac1{11}.
\tag{E14}
\]

For constant u the reliability equilibrium is c∞=6u/(6u+1). Three choices show why maximizing information provision alone is insufficient.

| Allocation u | Equilibrium c∞ | Minimum response error | Execution reserve change per unit time |
|---|---|---|---|
| 1/2 | 3/4 | 1/8 | +1 |
| 7/10 | 21/26 | 5/52 | +1/5 |
| 9/10 | 27/32 | 5/64 | −3/5 |

The middle choice meets both requirements indefinitely from the safe region. The first eventually violates accuracy; the last improves accuracy while consuming any finite execution reserve. Equilibrium values do not excuse an unsafe initial condition or a transition that violates a deadline.

For a stricter tolerance ε=5/58, c*=24/29 and u_information=4/5>u_execution=3/4. Starting from c(0)=c* and b(0)=1, equation (E10) gives T≤5. The constant allocation u=4/5 keeps c exactly at its floor and gives b(t)=1−t/5. It therefore attains T=5 exactly. No history-dependent allocation can extend this service horizon. At that time the state remains on the permitted boundary; service cannot continue for any positive additional duration without violating at least one requirement.

All rational values in this section were checked using exact fraction arithmetic. The eight deterministic decoders on {0,1,?} were enumerated at c=4/5: their minimum average error is exactly 1/10, attained by the two decoders that follow each observed bit and choose either fixed answer on erasure. Fair randomization of those two decoders also gives worst-case error 1/10 across circumstances. These are constructed checks of calculations, not empirical observations.

### Why scheduled tests do not establish continuous readiness

The timing qualification has a concrete counterexample. Retain ε=5/58, start at c(0)=24/29 and b(0)=1, and alternate u=1 for one time unit with u=0 for one time unit. Assess accuracy only at times 1,3,5,…, the ends of full-maintenance intervals. The first assessment meets the accuracy floor, because during full maintenance c moves toward 6/7>24/29. For subsequent assessment reliabilities hₙ, the exact recurrence is hₙ₊₁=(6/7)(1−e⁻⁷)+e⁻⁸hₙ. Every such value is greater than (6/7)(1−e⁻⁷)>24/29, and their limit is approximately 0.85665. Meanwhile b decreases by one during maintenance and increases by three during the other interval; it remains nonnegative and gains two per cycle. These scheduled assessments and execution therefore remain feasible indefinitely. Reliability falls below the continuous floor between assessments. No contradiction arises: the exact iff theorem protects a stronger temporal requirement. Keeping the same q even in this weaker construction makes the counterexample conservative with respect to execution expenditure.

## 5 The obstruction extends beyond this particular repair equation

Suppose instead that, on an acceptable interval c≥c*,

\[
\dot c=a(c)u-\ell(c),\qquad \dot b=s(1-u)-q,
\tag{E15}
\]

with a(c)>0. Assume the ratio r(c)=ℓ(c)/a(c) is bounded below there by r*, and that the following integral is finite at the initial state:

\[
V(c)=\int_{c_*}^{c}\frac{dz}{a(z)}.
\tag{E16}
\]

Then W=b/s+V(c)≥0 on the safe region, and

\[
\dot W=1-q/s-r(c)\le1-q/s-r_*.
\tag{E17}
\]

If r*>1−q/s, every acceptable interval has duration at most W(0)/[r*−(1−q/s)]. This conditional exhaustion result needs neither a scalar social goal nor an assumption that the controller optimizes W. It follows from the two balances and their shared allocation. Existence, uniqueness, and boundary behavior of an application must also be checked. The general inequality is a necessity result; a sufficiency claim needs a feasible allocation and an invariant operating region, as explicitly supplied in Theorem E2.

## 6 Endogenous selection can preserve or destroy its information conditions

Existence of a feasible allocation does not imply it will be installed. For a constructed example, retain α=6, δ=1, s=4, q=1 and ε=1/10. Let x∈[0,1] be the prevalence of a practice providing more maintenance. Assume

\[
u(x)=\frac12+\frac{x}{5},
\quad
\dot c=6u(x)(1-c)-c,
\quad
\dot x=x(1-x)(5c-4).
\tag{E18}
\]

The last equation is an explicit selection mechanism: the advantage of the practice rises with the operative information channel. One possible application would interpret 5c−4 as recognized benefit minus an adoption disadvantage, but that interpretation requires independent measurement. It is not a deduction that every institution uses this selection law. These selection quantities need not equal the physical provisioning costs in (E7).

There are two locally asymptotically stable boundary equilibria for the (c,x) subsystem:

\[
(c_L,x_L)=(3/4,0),\qquad
(c_H,x_H)=(21/26,1),
\tag{E19}
\]

and an interior saddle at

\[
(c_\dagger,x_\dagger)=(4/5,5/6).
\tag{E20}
\]

**Proof.** At x=0 and x=1, solve ċ=0. The two eigenvalues at the low equilibrium are −4 and −1/4; those at the high equilibrium are −26/5 and −1/26. At an interior equilibrium, ẋ=0 requires c=4/5, and ċ=0 then requires u=2/3, so x=5/6. The interior Jacobian in coordinates (c,x) is

\[
\begin{pmatrix}
-5&6/25\\
25/36&0
\end{pmatrix},
\tag{E21}
\]

with determinant −1/6. It therefore has one positive and one negative eigenvalue. ∎

Two explicit invariant regions establish the practical consequence without requiring a numerical basin plot. If initially c<4/5 and x<5/6, neither upper boundary can be crossed outward: at c=4/5 the reliability derivative is nonpositive, and at x=5/6 the selection derivative is nonpositive. Within this region x decreases. Its limiting value must be zero, because any positive limit below 5/6 would give a reliability equilibrium below 4/5 and a persistent negative selection rate. Consequently c→3/4. Conversely, starting with c>4/5 and x>5/6 keeps the system above both thresholds; x increases to one and c→21/26. The remaining portions of the state space need not lie in these rectangular subsets of the basins.

The low regime delivers minimum error 1/8 and fails the declared accuracy standard; the high regime delivers 5/52 and meets it. In both cases the execution reserve grows because u(x)≤7/10<3/4. Thus the failure in the low regime concerns the reproduction and selection of informative correction, not a lack of external input in this example. Moving only the nominal accuracy target cannot create an operative information channel. Establishment may require an intervention in reliability, practice prevalence, or the actual selection mechanism, with its own cost and permissions.

These are attractors of the (c,x) subsystem. Since b grows, they are not fixed points of the full three-dimensional state. No claim of a universal attractor topology or universal selection law follows.

## 7 What is invariant and what must be discovered

The operational error and feasibility claims are invariant under a faithful change of coordinates: transforming c to another one-to-one variable and transforming its dynamics and requirement together preserves the same feasible trajectories and deadlines. The logarithm in (E11) is a convenient mathematical certificate; its coordinate expression is not itself proposed as a universal physical constant. Changing the time unit rescales all rates and the numerical deadline consistently without changing the inequality between required and available allocation. Extending the horizon reveals reserve exhaustion already entailed by the model.

The synthesis is stronger than the claim that an uninformed reasoner can be wrong. It shows how a required degree of discrimination implies a minimum maintenance demand, how that demand competes with executing the resulting decisions, and how a finite reserve bounds the duration of apparently adequate performance. An endogenous selection mechanism can then stabilize either side of the resulting quality threshold. Each arrow is specified rather than inferred from the existence of change alone.

To use this result scientifically, an application must independently estimate the observation law, the response requirement, channel turnover, maintenance efficacy, service costs, and available interventions. The channel must include all information actually accessible to the decision maker. A useful falsification is that the maintained channel fails to predict the measured discrimination error, that an omitted information source bypasses the alleged threshold, or that a purported maintenance intervention does not change the channel as modeled. Persistence of a belief, reported confidence, and actual discrimination must be measured separately.

The two protected requirements remain conjunctive. The proof does not turn accuracy and execution into a common moral objective. More parties, asymmetric errors, prohibited actions, and service deadlines require the corresponding separate constraints. An ethically unacceptable system may satisfy these operational requirements; acceptable targets and legitimate amendments still need substantive justification.

## 8 Relation to prior work and the remaining limit

Information as a physical condition of viability is established territory. [Kolchinsky and Wolpert, 2018](https://arxiv.org/abs/1806.08053) define a form of semantic information through interventions on system–environment correlations and their contribution to continued existence. [Sowinski and colleagues, 2023](https://arxiv.org/abs/2304.03286) study resource-gathering agents and a sensor-noise threshold beyond which expected lifetime sharply declines. These are close conceptual predecessors. The present note does not claim to originate information–viability coupling or a general definition of meaning.

The specific development here is the connection between a calibrated decision-error threshold, explicit turnover of the information channel, a separately protected finite execution reserve, and a control-independent exhaustion certificate. It supplies an exact feasible interval, a sharp finite witness, and an explicit selection trap for review. Its originality relative to the full literature remains unestablished.

The result concerns conditions for reliably responding to particular truths about a modeled world. It does not define truth as whatever supports survival. A perfectly maintained channel may report facts irrelevant to ethical action, and a persistent false belief may be harmless to a system's continuation. Nor does the note prove a model-independent energetic cost per true belief: its costs are stipulated physical coefficients that must be calibrated.

Finally, the proof does not certify unrestricted future novelty. If new circumstances, new required responses, or new channels appear, the earlier statistical and physical contracts may fail. A representation theorem can preserve a declared class of questions, and the adaptive method can operate over a declared model family. Neither can guarantee distinctions about arbitrary unmodeled cases. The stronger root supported here is precise: continuing informed correction is possible only while the conditions enabling both discrimination and execution remain jointly reproducible under the actual resource and information constraints.
