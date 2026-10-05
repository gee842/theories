# Direction, renewal and the limits of monotone progress

5 October 2026. AI-assisted formal clarification for Ren's descriptive direction-of-reality proposal. This note sharpens the quantifiers of the [common specification](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/FORMAL-SPECIFICATION.md); it does not replace the positive research objective with a counterexample. The finite-state propositions below are elementary consequences of the stated generator, not new laws of physics.

## 1. Three different observations

A coupled situation can deliver a function repeatedly without acquiring ever greater capacity. It can acquire a useful capacity while losing another. A population of observations can become dominated by enduring situations even when no situation improves. These claims concern different probability laws.

Keep the assessed functions, reliability, future assay horizon and information access fixed when testing temporal improvement. Let K(x) be the resulting capability region for a fully specified operational preparation x. This can be a preparation incorporating an accessible record and its uncertainty; it is not permission to disclose hidden physical state for free. A finite-state result applies only when the stipulated state is sufficient for the actual process and K. For a finite set of assay profiles, K takes values in a finite partially ordered collection, ordered by inclusion. A finite operational state space also makes the image of any fixed K finite.

There are at least four legitimate targets:

1. An intervention improves a specified joint delivery by a specified deadline.
2. Actual trajectories repeatedly renew a specified function, paying each replacement cost.
3. One physical arrangement has a more favorable stationary distribution of capabilities than another.
4. An unchanged process has a temporal increase in its capability distribution, for declared preparations and times.

The [allocation theorem](ALLOCATION-CONTROL.md) addresses target 1. A physical return construction can address target 2. The earlier [birth–death theorem](../outputs/shared-generative-direction-mathematics.md) conditionally addresses target 3. None alone proves target 4 or a universal direction. The question whether a common physical mechanism explains favorable results across these targets remains open.

## 2. Exact balance for every capability threshold

Consider a finite continuous-time Markov chain with generator Q and distribution p_t. For an upward set U of capability regions, write

\[
A_U=\{x:K(x)\in U\},\qquad f_U(x)=1_{A_U}(x).
\]

Its exact probability balance is

\[
\frac{d}{dt}\Pr(K(X_t)\in U)
=\sum_{x\notin A_U,y\in A_U}p_t(x)q_{xy}
-\sum_{x\in A_U,y\notin A_U}p_t(x)q_{xy}.
\tag{1}
\]

This follows by expanding p_t Q f_U; internal transitions cancel. The right side is entry across the threshold minus exit across it. It includes actual formation, loss, repair and displacement only insofar as those events are present in Q. Naming an entry “generative” does not make the first sum larger.

Temporal stochastic improvement over an interval requires (1) to be nonnegative for every upward U throughout that interval. An endpoint comparison needs the time integral to be nonnegative; it need not have a nonnegative instantaneous sign. An increase for one threshold does not settle the others. Testing all threshold probabilities concerns the random region K(X_t), which differs from testing the probability of one assay outcome.

## 3. Finite recurrence rules out a nontrivial increase from every state

**Proposition.** Suppose Q is irreducible on a finite state space. If a real state function f satisfies Qf(x) >= 0 for every x, then f is constant. Consequently, if the capability distribution is stochastically no worse at every positive time than at time zero, from every initial state, K is constant across states. A strict universal increase is impossible in this class.

**Proof.** The stationary distribution pi is strictly positive and pi Q = 0. Thus 0 = pi Qf, and nonnegativity forces Qf(x) = 0 everywhere. At a maximum of f, every summand q_xy[f(y)-f(x)] is nonpositive. Equality forces all outgoing neighbors with positive rate to share that maximum. Reachability propagates it to every state.

For the capability assertion, stochastic nondecrease from each delta_x gives exp(tQ)f_U(x) >= f_U(x) for every upward U. Differentiate at zero to get Qf_U >= 0. The first result makes every f_U constant. Upward sets separate distinct elements of a finite partial order, so K must be constant. The same argument applies inside each closed irreducible class of a finite reducible chain. Transient changes between classes are not excluded. QED.

This does not rule out improvement from an initially poor preparation toward a stationary distribution. It does not rule out comparison between different stationary distributions. It does not cover an unbounded expanding state space, nonstationary source schedule, or growing physically implemented records by pretending they are a finite stationary chain. Such extensions must specify their own resources and state rather than borrowing this result or claiming to escape it by vocabulary alone.

The conclusion is practical: continued paid renewal and capability accumulation are different research claims. A maintained regime can be an explanatory success even when its capacity distribution has stopped changing. It would not, by itself, finish the user's stronger direction claim.

## 4. Sustained dissipation is compatible with stationary capability

For a minimal example, take three states in a ring, with clockwise rate a and counterclockwise rate b, where a,b > 0 and a != b. The stationary law is uniform. Each clockwise edge has stationary net current (a-b)/3; a physically driven interpretation requires the corresponding nonzero cycle affinity, 3 log(a/b).

Using the standard Markov-jump entropy-production expression, its stationary entropy production in units of Boltzmann's constant is

\[
\dot S_{\rm tot}/k_B=(a-b)\log(a/b)>0.
\tag{2}
\]

Every fixed capability-threshold probability is nevertheless constant in the stationary ensemble. A nonconstant ordering of those states cannot increase from every state, by the preceding proposition. A cumulative count of completed cycles can grow; that is an accumulated delivery, not an increase in current capability. If a device physically records that count, its memory and renewal belong in the enlarged model.

The rate-ratio and entropy-production framework is standard; see Seifert, [*Stochastic thermodynamics, fluctuation theorems, and molecular machines*](https://arxiv.org/pdf/1205.4176), sections 6.2–6.4, especially equations 128 and 139. The three-state calculation here is our explicit substitution into that framework. Positive dissipation alone supplies no theorem that capability regions expand.

## 5. Survival conditioning can manufacture an apparent direction

Take two initially equally likely coupled preparations A and B. They retain their respective capabilities until irreversible loss, with loss rates 0 < delta_A < delta_B, and never transform into one another. Suppose A has the larger assessed region. Then

\[
\Pr(X_t=A)=\tfrac12 e^{-\delta_A t}
\quad\text{decreases, while}\quad
\Pr(X_t=A\mid\text{not lost})
=\frac{1}{1+e^{-(\delta_B-\delta_A)t}}
\quad\text{increases}.
\tag{3}
\]

No useful structure forms in this example. The changing composition of survivors is a real descriptive effect, but it must not be reported as formation, an unconditional improvement, or a mechanism explaining new possibilities. It may be one term in an evolutionary explanation once actual formation, transmission and shared effects have also been derived.

## 6. Consequence for the finite shared-renewal specimen

In the current finite-material model with positive wear/leakage and no productive immigration, the previously proved absorption result applies. At the all-D, zero-packet state, every future assay requiring productive plant activity fails. Let T_loss be the absorption time, and restrict every allowed future protocol to the installed repertoire without added restart. More precisely, the loss set must remain invariant under every admissible continuation, and changing a continuation cannot change the posterior law of the already realized past. With accessible record G_t, write r_t = Pr(T_loss > t | G_t). Every productive future assay has conditional success probability at most r_t, uniformly over those protocols. Hence, at fixed reliability alpha > 0, any nonempty region of such productive assays requires r_t >= alpha. For any upward threshold U excluding the empty productive region,

\[
\Pr(\mathbf C_t\in U)\le \Pr(r_t\ge\alpha)
\le \frac{\Pr(T_{\rm loss}>t)}{\alpha}\longrightarrow0.
\tag{4}
\]

The second inequality is Markov's inequality and the conditional-expectation identity. If absorption status is fully observed, the sharper bound Pr(T_loss > t) holds. This distinction prevents an analyst from confusing actual hidden loss with the accessible preparation's capability. The result concerns those productive assays, not every conceivable capability of inert material. A continuing incident source does not restart the process after the machinery needed to capture it has disappeared.

Finite repeated delivery can still have positive probability and can be strongly improved by a paid mechanism. The [allocation gain](ALLOCATION-CONTROL.md) is therefore compatible with eventual loss. To study maintained stochastic activity, we must explicitly add and pay for a restart source, a growing system, or another mechanism that changes the absorption premise. Increasing the capture coefficient alone does not do so.

## 7. What the next positive proof must supply

Use actual return and loss kernels from the physical event process. Record delivery during each excursion, its duration, work drawn from the source, depletion, and the entry-state distribution for the next excursion. A repeated-success claim must compose the conditional laws of those actual entries. Separate successful return probability from expected duration and from the distribution conditional on return. Do not replace these with a favorable birth–death chain until its closure and capability ordering are justified.

For architecture formation, put the molecule, template or apparatus that enables fabrication into the same state and generator. A law can specify how that apparatus forms; a particular useful apparatus must not be silently present in a preparation declared to start without it. Fundamental laws remain premises at this modeling level. Explaining organization under a common law is a different task from deriving that law.

The strong practical target remains: derive a favorable formation-and-retention balance from independently specified physical conditions, while predicting when costs, wear or competing uses reverse it. Carry the resulting law into a common plural assay, compare alternatives, and test a discriminating empirical prediction. Equations (1)–(4) constrain what a correct result can mean; they do not establish the favorable balance or its universality.

## Provenance and verification scope

Read the current specification's actual-dynamics/direction section, the existing birth–death result, physical regulation accounting, and allocation-control theorem. The new statements are analytic deductions, with no simulation or empirical study in this note. The cited Seifert source was inspected at the indicated sections; no claim of a whole-paper review is made. Independent mathematical review is recorded separately when complete.
