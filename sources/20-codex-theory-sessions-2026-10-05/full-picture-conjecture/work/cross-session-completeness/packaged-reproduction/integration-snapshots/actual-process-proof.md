# Finite closure under installed, partially informed rules

This note supplies an exact formal test for a restricted adaptive system whose information, implemented rules, renewal and succession are inside one transition process. It distinguishes the existence of a successful external policy from the continuation actually produced by the installed institution. The mathematics is standard finite-state probability and verification; the substantive construction is the explicit inclusion of those mechanisms in the state and kernel.

The result is not a proof of universal alignment. It is a way to make a proposed general account answer a finite, exact question before extending its scope. There is no requirement that the application use money, reproduction, one shared goal or an immortal truthful governor.

## 1. What must be inside the finite model

Let \(S\) be a finite state space. A state can include:

\[
s=(e,k,n,r,m,\phi,\psi,\ell).
\tag{1}
\]

The components record environmental or material conditions \(e\), retained skill and functional capacities \(k\), access and relationships \(n\), installed selection and revision rules \(r\), their memory \(m\), representations \(\phi\), optional evaluative commitments \(\psi\), and carrier or succession states \(\ell\). Components without a justified interpretation in the application should be omitted. In particular an ecosystem need not possess represented purposes.

Finite state is a deliberate restriction. Counters can represent bounded stocks, age classes, inquiry records, pending problems or remaining time. The state must carry the memory needed for a Markov description. A changing environment can be included as a finite stochastic state. Arbitrary history dependence, a continuously changing calendar, or open-ended discovery requires a different model or a justified approximation.

The installed process induces a time-homogeneous transition matrix

\[
K(s,s')=\Pr(S_{t+1}=s'\mid S_t=s),
\qquad\sum_{s'}K(s,s')=1.
\tag{2}
\]

Construct \(K\) from explicit events, in a declared order or as a joint event kernel:

1. Available experience produces an observation through the current information channel.
2. The installed rule and its actual memory generate a proposal or action.
3. Present authority and physical capability determine what is executed.
4. Execution, external inputs, depreciation and learning change material and skill conditions.
5. Selection, revision, entry and succession change personnel, rules, memory and represented concerns.

All five stages may depend on the state, but a decision maker's proposal cannot use hidden variables it has not observed. Formally, observationally identical local histories with the same installed memory must induce the same proposal distribution. The analyst can compute \(K\) on the full state without giving agents that information. Decentralized agents require locally admissible decision maps, not an unnoticed central observer with access to every private signal.

An implemented rule is genuinely endogenous when the last stage changes it through modeled events and the new rule changes later transitions. Merely appending an unused rule label to the state adds no mechanism. Likewise, a successor is not automatically competent: the acquisition or loss of relevant skill and records must be specified. A qualified outside entrant or a reliable physical mechanism can be a declared environmental input, but must not be silently introduced whenever the institution needs rescue.

## 2. Declare outcomes independently of institutional self-certification

Let \(C\subseteq S\) be an independently declared set of acceptable operating outcomes. It can be an intersection of several constraints, or the analysis can report several separate specifications. For example, a model might distinguish service quality, a material floor, burdens on different groups, and access to effective challenge. Combining incompatible commitments does not make them jointly feasible.

The current institution may use its own changing score or evaluative rule \(r,\psi\). Record that score separately. Renaming an outcome successful must not move it into \(C\) unless the analyst explicitly changes the specification and reports the consequences of doing so. Legitimate revision of a normative commitment is possible; it is not established by the fact that the current regime prefers the revision.

Safety need not mean that no mistake ever occurs. Recoverable error can lie inside \(C\); an irreversible loss, excessive delay or specified harm can lie outside it. What counts as failure is therefore stated through outcomes and timing, not inferred from a label such as capture or correction.

Let \(T_1,\ldots,T_q\subseteq S\) represent recurring events required for renewal or response. The intended property is

\[
\mathcal P:\quad S_t\in C\ \text{for every }t,
\quad\text{and each }T_j\text{ is visited infinitely often}.
\tag{3}
\]

The target sets must encode real events. A stationary state merely labeled “revision available” does not demonstrate repeated effective revision. A small monitor can record a new discrepancy, an implemented response, delivered training or a successor's acquisition of competence. Event-labeled transitions can equivalently be converted into finite monitor states.

For an obligation with a deadline, add a pending flag and finite age counter; crossing the deadline is an outcome outside \(C\). For an eventual-response obligation, a pending flag can be cleared only by the specified effective response. Recurring visits to the cleared state then have their intended meaning only under that declared monitor semantics. State visits alone do not establish that an arbitrary substantive obligation has been met.

## 3. Actual almost-sure safety is a greatest fixed point

Define

\[
W_0=C,\qquad
W_{n+1}=\{s\in W_n:K(s,W_n)=1\}.
\tag{4}
\]

The sequence stabilizes after at most \(|S|\) strict removals. Its limit

\[
\boxed{W_K(C)=\nu W\,[C\cap\{s:K(s,W)=1\}]}
\tag{5}
\]

is the greatest \(K\)-closed subset of \(C\).

**Safety proposition.** For an initial state \(s\),

\[
\Pr_s(S_t\in C\text{ for all }t)=1
\quad\Longleftrightarrow\quad s\in W_K(C).
\tag{6}
\]

**Proof.** Starting in a closed subset of \(C\), every next state stays there with probability one, proving sufficiency by induction. A removed state has a positive-probability transition to an earlier-removed state or to \(S\setminus C\). Following this finite chain of removals produces a finite positive-probability path to an unacceptable outcome. Its safety probability is therefore less than one. \(\square\)

This is a statement about the **installed kernel**. There is no maximization over alternative policies in (4). A system may possess a correctable error, a competent person and an available remedy, yet fail this test because its actual selection and revision rules give positive probability to a path that disables or refuses the remedy.

The result does not require a permanent carrier of a correct policy. Personnel, competence and rule succession can all change in \(K\). It does require that the modeled succession process, rather than an external reset, supplies whatever persistence the kernel exhibits.

## 4. Exact closure with regeneration and effective response

In the directed support graph of \(K\), draw an edge \(s\to s'\) exactly when \(K(s,s')>0\). A bottom strongly connected component, or bottom SCC, has no outgoing edge. These components are the finite chain's closed irreducible recurrent classes.

**Closure theorem.** From an initial state or support \(B_0\), property (3) holds with probability one exactly when:

1. Every state reachable from \(B_0\) by a positive-probability path lies in \(C\).
2. Every bottom SCC reachable from \(B_0\) intersects each target set \(T_j\).

**Proof.** Every finite Markov chain almost surely eventually enters a bottom SCC and then visits every state of that class infinitely often. If both conditions hold, it stays acceptable and revisits every required target. Conversely, a reachable unacceptable state gives a positive-probability safety violation. A reachable bottom SCC missing some target gives a positive-probability path after which that target is never visited again. \(\square\)

This is standard safety plus generalized Büchi model checking. The underlying finite-chain fact is stated, for example, in [Christel Baier's probabilistic model-checking tutorial, slides 84–86](https://resources.mpi-inf.mpg.de/departments/rg1/conferences/vtsa17/slides/baier-vsta17-MC-final.pdf). The claimed contribution of this study is not a new Markov-chain theorem. It is an executable test of a model in which the conditions producing information, action, renewal and successor rules are represented together.

The theorem distinguishes three mechanisms often conflated: persistence of an operating state, recurring regeneration, and recurring effective response. A closed but unresponsive institution can satisfy (6) while failing (3). A frequently changing institution can satisfy a crude rule-change counter while failing a target that requires the change to address an independently recorded discrepancy.

## 5. Probabilities, rather than only yes-or-no guarantees

Finite-horizon safety has the exact recursion

\[
q_0(s)=\mathbf1_C(s),\qquad
q_{H+1}(s)=\mathbf1_C(s)\sum_{s'}K(s,s')q_H(s').
\tag{7}
\]

Thus \(q_H(s)\) is the probability that all states through \(H\) transitions remain in \(C\). For the submatrix \(Q=K[C,C]\), it is \(Q^H\mathbf1\) on \(C\). The sequence decreases to the infinite-horizon safety probability.

That limit need not be zero or one. It equals the probability of reaching \(W_K(C)\) before leaving \(C\). Indeed, an indefinitely safe trajectory almost surely eventually enters a bottom SCC contained in \(C\), and that SCC belongs to \(W_K(C)\).

For property (3), call a bottom SCC good when it is contained in \(C\) and intersects every \(T_j\). The exact success probability is the probability of reaching a good bottom SCC before leaving \(C\). Assign boundary value one on good classes, zero on \(S\setminus C\) and other bottom classes inside \(C\), then solve the finite linear hitting-probability equations on the remaining states. This separates a low-probability route to a functioning regime from a guarantee that the installed process realizes it.

Hitting probabilities alone do not supply a useful deadline. A system can respond eventually but too slowly for a particular need. Report finite-horizon probabilities, response-time distributions and independent violation types when those matter, rather than translating every positive probability of eventual success into effective corrigibility.

### From a validated transition-error bound to a finite-horizon guarantee

There is a positive route from empirical model assessment to a bounded risk claim. Suppose the modeled and actual processes use the same state representation and initial state. At every actual reachable history through time \(t<H\), assume the actual conditional distribution of the next state differs from the modeled conditional distribution by total variation at most \(\epsilon\in[0,1]\). For the present model the latter distribution is \(K(S_t,\cdot)\). The actual process need not itself be Markov: the bound must then hold conditioned on each relevant history, not merely after averaging histories with the same current state.

For every event \(A\) determined by the first \(H\) transitions,

\[
\boxed{
\left|\Pr_{\rm actual}(A)-\Pr_{\rm model}(A)\right|
\le1-(1-\epsilon)^H\le H\epsilon.
}
\]

To prove this established coupling bound, couple the two initial states identically. While their histories agree, use a maximal coupling of their conditional next-state distributions, which agrees with probability at least \(1-\epsilon\). The chance that the entire histories agree through \(H\) transitions is therefore at least \((1-\epsilon)^H\). Any path event has the same truth value when the paths agree; its probability difference is bounded by the probability of a disagreement. Independence of transition errors is not required. If the initial distributions instead differ by total variation at most \(\epsilon_0\), the same argument gives \(1-(1-\epsilon_0)(1-\epsilon)^H\le\epsilon_0+H\epsilon\).

Consequently a validated uniform transition bound would convert modeled finite-horizon success \(q_H\) into the lower guarantee \(\max\{0,q_H-[1-(1-\epsilon)^H]\}\). If success depends on delivered-work or revision events, the error bound must cover the joint event/state transition, or the event monitors must be included in the state. Accuracy of the marginal state transition alone need not validate omitted event claims.

This is a conditional validation criterion, **not an error bound inferred from the current study or its external data checks**. Average forecast error, held-out prediction improvement, or no observed failure does not establish a uniform total-variation bound over reachable histories. The observation coverage, uncertainty and transfer assumptions needed to certify such a bound remain empirical work. The result nevertheless states what sufficiently strong validation would buy at a declared finite horizon, rather than demanding unattainable proof from an unlimited failure-free record.

### A testable criterion for transfer between domains

Let a finite domain model have state space \(S_D\) and transition kernel \(K_D\). A proposed map \(\phi_D:S_D\to S\) to a shared abstract model \(K\) must do more than assign the same vocabulary to different objects. Require, throughout the reachable domain states,

\[
\sup_s\operatorname{TV}\!\left(
 (\phi_D)_\#K_D(s,\cdot),\ K(\phi_D(s),\cdot)
\right)\le\epsilon_D,
\]

where \((\phi_D)_\#K_D(s,B)=K_D(s,\phi_D^{-1}(B))\). Suppose the initial abstract state agrees and the declared outcome event is preserved by this map; for example, a domain constraint must satisfy \(C_D=\phi_D^{-1}(C)\) on the modeled region. Then for every mapped event \(A\) determined by \(H\) transitions,

\[
\left|\Pr_D\!\left((\phi_D(S_t^D))_{t=0}^H\in A\right)
-\Pr_K(A)\right|
\le e_D(H):=1-(1-\epsilon_D)^H.
\]

The projected domain process need not itself be Markov. Conditional on its complete abstract history, its next-state law is a mixture of projected domain rows in the current fiber of \(\phi_D\). Convexity of total variation keeps this mixture within \(\epsilon_D\) of the corresponding abstract row, so the preceding sequential coupling proof applies. For two domains mapped to the same \(K\), with the same abstract initial state and event, their event probabilities consequently differ by at most \(\min\{1,e_{D_1}(H)+e_{D_2}(H)\}\).

When \(\epsilon_D=0\) for every domain state, this is the familiar exact aggregation condition, or strong lumpability: all states in a fiber have the same next-fiber distribution. This is established Markov-chain mathematics, not a new universal theorem; the Kemeny–Snell condition is reproduced as Theorem 2.3 in [Tian and Kannan, *Lumpability and Commutativity of Markov Processes*](https://people.nmsu.edu/jtian/publications/2006-3.pdf). A bound restricted to the reachable region supports the corresponding restricted transfer claim, not aggregation from every possible initial state.

Passive transition agreement alone does **not** establish a shared causal mechanism or transferable governance. For an intervention claim, specify corresponding implementable interventions in both domains and require the bound for their transition kernels, uniformly over the intervention histories being compared. Observation and action maps must also preserve the information and implementation restrictions required by any transferred policy. Relevant events, including renewal, revision and independently declared normative outcomes, must be preserved directly or included in a monitored state; an abstraction that erases their differences cannot certify them. The maps, regions, intervention family and permissible errors are substantive hypotheses to test. None of the current external prediction checks estimates these uniform errors. This criterion states what would justify a bounded cross-domain claim without identifying money, reproduction, appointment, persistence or any other single domain variable as the universal substance.

## 6. Rare failure changes the infinite-horizon question

Suppose a declared irreversible failure can occur at each of a sequence of operating opportunities with conditional probability at least \(\epsilon>0\), given the complete history and survival so far. Independence is unnecessary. Survival through \(N\) such opportunities is at most

\[
(1-\epsilon)^N.
\tag{8}
\]

If opportunities continue infinitely often on indefinitely operating paths, indefinite survival has probability zero. In the simplest two-state example, an operating state moves to absorbing failure with probability \(\epsilon\) each round. Its finite-horizon survival is exactly \((1-\epsilon)^H\), and its mean time to failure is \(1/\epsilon\), although its infinite-horizon safety core is empty.

For example \(\epsilon=10^{-5}\) yields about 0.99005 survival over 1,000 rounds but zero probability of surviving forever. Long successful simulations do not contradict the latter statement. Conversely, recoverable disturbances need not destroy an almost-sure regeneration claim; what matters is the actual transition graph and declared outcome property, not the name of the disturbance.

If every apparently functioning regime retains a path to permanent skill loss, a finite test may therefore find high finite-horizon reliability and no infinite-horizon protected core. That is an informative result. A positive infinite-horizon theorem requires a genuinely closed acceptable recurrent structure under the stated disturbances, or a different specification such as recovery, finite-horizon reliability or tolerable frequency of violations.

Do not delete tiny positive transition probabilities when computing the support graph. Removing a rare edge changes the qualitative theorem. Empirical uncertainty about whether an edge is exactly absent is a substantive limitation of an almost-sure claim.

For a conservative uncertain-kernel safety check, let \(\mathcal P(s)\) be a nonempty set of possible next-state distributions at state \(s\). Replace (4) by

\[
\widehat W_{n+1}
=\{s\in\widehat W_n:\text{for every }p\in\mathcal P(s),\ p(\widehat W_n)=1\},
\qquad\widehat W_0=C.
\]

Its greatest fixed point guarantees safety even if an adversary chooses a permitted transition row anew at each visit. For a single unknown but fixed kernel this can be conservative: unrestricted row switching may combine transitions that no fixed candidate kernel possesses together. The recurrent-class theorem for a fixed Markov chain does not automatically transfer to this adversarial model, because the row selector may avoid a renewal event indefinitely. Additional game or fairness conditions would be required for liveness.

This distinction makes the empirical boundary explicit. Observing no leakage in a finite record does not establish that the leakage probability is exactly zero. If a credible uncertainty set contains a positive irreversible leakage path, the robust infinite-horizon guarantee can fail even while all supported finite-horizon estimates remain favorable.

## 7. External viability is a different fixed-point calculation

Construct a separate controlled comparison model using the same physical, informational and implementation mechanisms, but allow a hypothetical controller to choose among stated admissible proposals. Let

\[
P(s',o\mid s,a)
\]

be its finite transition-and-observation kernel. This comparator must state which decision choice is being substituted for the installed rule. It must not grant free authority to rewrite the institution or an observation unavailable to actual decision makers.

Under partial observation, a controller knows a support \(B\subseteq S\). Define

\[
\operatorname{Post}(B,a,o)
=\{s':\exists s\in B,\ P(s',o\mid s,a)>0\}.
\]

Let \(U(B)\) be the actions implementable throughout that support, or encode denied proposals explicitly in the execution kernel. Define sets of viable belief supports by

\[
\begin{aligned}
\mathcal V_0&=\{B\ne\varnothing:B\subseteq C\},\\
\mathcal V_{n+1}&=\{B\in\mathcal V_n:\exists a\in U(B)\ 
\forall o,\ \operatorname{Post}(B,a,o)\ne\varnothing\Rightarrow
\operatorname{Post}(B,a,o)\in\mathcal V_n\}.
\end{aligned}
\tag{9}
\]

The greatest fixed point characterizes **existence** of an observation-compatible policy guaranteeing safety in this finite controlled model. Sufficiency follows by selecting a witnessing action at every retained belief support. Necessity follows by induction on the finite safety horizon: a removed support lacks an action whose every possible observation successor remains viable. Randomizing among actions cannot restore probability-one safety when every action has a positive-probability unsafe continuation.

This is a qualitative safety statement; support alone generally does not determine optimal finite-horizon success probabilities, for which posterior weights can matter. Decentralized information restrictions may require a richer strategy model than one common belief support.

Where the comparator can reproduce the installed policy with the same information and action constraints, actual probability-one safety implies external viability. The converse does not hold. The installed process may not discover, select, maintain, transmit or implement the witnessing policy. Writing \(\exists\pi\) does not supply any of those mechanisms.

A fully observed controller is an additional relaxation. Two hidden situations can each possess a safe action while requiring different actions under identical observations. Then singleton supports can be viable but their union is not. More reasoning over the same nondiscriminating observations cannot repair that obstruction. Additional timely information, a common safe action, a physical buffer or a revised uncertainty specification is needed.

## 8. A conditional succession corollary for the proposed test

Consider skill \(k\in\{0,1,2\}\) and an installed practice \(q\in\{V,A\}\). Practice \(V\) performs ordinary work without training. Practice \(A\) trains when \(k=1\), increasing pre-turnover skill to two, and performs inquiry when \(k=2\). Inquiry and ordinary work do not increase skill. Training requires at least one existing skilled carrier. After work, a turnover event removes at most one carrier. Suppose that, whenever skill is positive, an event actually removing one carrier has conditional probability at least \(\delta_0>0\).

When post-turnover skill is one, the new incumbent is of practice \(A\) with probability \(w_q/(1+w_q)\), where \(0\le w_q\le w_{\max}<\infty\). The weight may depend on the preceding installed rule. The alternative \(V\) therefore has conditional appointment probability at least \(1/(1+w_{\max})\). At zero skill there is no external restoration in this version.

**Corollary.** From every positive-skill state, the probability of reaching zero skill within the next two steps is at least

\[
\boxed{p_* = \delta_0^2/(1+w_{\max})>0.}
\tag{10}
\]

Consequently

\[
\Pr(\text{skill stays positive through }2n\text{ steps})
\le(1-p_*)^n,
\tag{11}
\]

the actual almost-sure safety core for \(C=\{k\ge1\}\) is empty, and zero skill is reached almost surely. A coarse bound on its expected hitting time is \(2/p_*\).

**Proof.** If \(k=1,q=V\), the first decrement already produces zero skill with probability at least \(\delta_0\ge p_*\). In every other positive-skill case, pre-turnover skill is two. A first decrement, followed by a volume appointment, produces \(k=1,q=V\) with probability at least \(\delta_0/(1+w_{\max})\). A further decrement gives zero skill with conditional probability at least \(\delta_0\). Multiplying conditional bounds proves (10); independence is unnecessary. Applying the same bound after every surviving two-step block proves (11). Summing the survival bound gives the expected-time bound. \(\square\)

The denominator uses **post-turnover** skill in the appointment rule. If the implementation instead assigns weight \(2w_q\) using pre-turnover skill two, the uniform denominator becomes \(1+2w_{\max}\). The distinction must be settled in the event order, not hidden by a general label such as succession.

The same physical system admits a skill-preserving policy if the controller observes \(k\) and can choose the stated work portfolios: train at one and inquire at two. Its pre-turnover skill is always two, and loss of at most one leaves skill positive. Thus externally controllable viability can be nonempty while the installed institution's infinite-horizon safety core is empty. This is the precise missing implication between having a feasible preserving policy and reproducing that policy through actual succession.

Starting with practice \(A\) and positive skill, perfect transmission of \(A\) at every positive-skill succession supplies a positive boundary case by the same case split. This does not rescue an initial volume practice already at skill one. The zero appointment leak is an assumption, not a property certified by observing many successful appointments. Adding restorative entry at zero can instead support recurrent recovery, but does not restore the stricter property that skill never reaches zero. Actual outcome-dependent wear or withdrawal can change quantitative risk through \(\delta\); the bound needs only a uniform positive lower probability of real skill loss.

This asymptotic depletion theorem also applies when the two appointment weights are equal. It therefore does not, by itself, establish that criterion-dependent feedback causes depletion or that such feedback is necessary for it. That channel's additional explanatory contribution must be tested through finite-horizon risk, response quality and controlled changes to criterion inheritance. The theorem isolates failure to preserve an available practice under recurrent succession, not a universal law of institutional capture.

## 9. Requirements for the concrete nonfinancial test

The next finite construction should make the formal test substantive:

- Installed criteria must change which work or successor is retained, and succession or experience must in turn be able to change those criteria.
- Inquiry, ordinary work and transmission of skill must be distinguishable activities with declared opportunity costs. Training is not an automatic by-product of filling an office.
- Available evidence must limit the installed decision rule. The analyst's hidden-state access must not leak into that rule.
- Revision requires both an informative event and an implemented change; neither alone counts as correction.
- Material or skill depletion and renewal must have actual state transitions. Initial competence must not be replaced by an immortal evaluator or a rescue reset.
- Independent consequences and the institution's changing score must be recorded separately. Optional plural requirements remain separate unless a justified choice procedure combines them.
- Report actual-kernel safety and recurrence, finite-horizon success, and externally controlled viability as different quantities. Preserve rare failure paths and report what the chosen horizon can miss.

A construction satisfying these requirements, together with its exact support graph and probabilities, would join several previously separate modules in one restricted model. It would validate that model's internal mathematics and implementation. Whether its transitions explain meritocracy, bureaucracy, democratic institutions, organisms or AI development still requires domain-specific evidence. The legitimacy of protected outcomes and permissible revisions also remains an explicit normative question. Finite formal closure makes those limits inspectable; it does not eliminate them by definition.
