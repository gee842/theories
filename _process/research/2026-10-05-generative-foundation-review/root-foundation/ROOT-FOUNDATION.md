# The root of alignment as continuing realizability

Mathematical development for Alignment as the Reproduction of Its Conditions. Prepared 5 October 2026. Research direction: Yongxu Ren. AI-assisted derivation and internal review. This document advances the universal-core question beyond an analogy with backpropagation or an assertion that every change is selection.

Subsequent assessment: [physical scope, originality and measured performance](../foundation-assessment/ASSESSMENT.md) adds a stochastic support theorem, locates stronger prior competitors, and reports no primary gain in a new exploratory measured-data comparison. The conditional proofs below are retained; novelty, physical coverage and comparative performance should be read in light of that assessment.

The subsequent [plural-capacity extension](../history/root-foundation/PLURAL-CAPACITY.md) proves a broader conditional feasibility theorem without aggregating the protected requirements into one objective. It adds exact dual failure bounds and, for constant losses, an exact maximum service duration.

The advance has three parts. We identify an operational object that is invariant under faithful descriptions; derive when finite, vulnerable supports necessarily imply recurrent provision or renewal cycles; and prove an exact resource threshold for continuing informed action. These are conditional mathematical results. They do not identify persistence with truth, prove a universal ethical objective, or establish that every physical process realizes the full selection–renewal mechanism.

The revised core is:

> What a situated system can distinguish and bring about constrains its possible functioning. Continued functioning requires the continuation of the relevant possibilities. When their implementations have finite lifetimes or sustained losses, continuation beyond inherited support requires renewed provision. Under finite-network and vulnerability assumptions, that provision must trace to continuing outside sources or internal renewal cycles. When the function requires informed correction, the observation and execution capacities are among the conditions that must continue.

This develops a theory of conditions of possibility, not a new numerical constant of nature. Its force comes from exact implications and identifiable assumptions. The [previous integrated theory](../../../history/2026-10-05-specialist-dossier/final-synthesis/INTEGRATED-THEORY.md) remains the detailed account of selection, maintenance, bounded learning, participation, succession, and normative amendments.

## 1 The invariant is what the system can actually accomplish

For a declared physical or causal model family indexed by \(\theta\), let \(\Pi(h)\) be the policies implementable from actual history \(h\). This includes the real observation interface, available commands, memory, time, costs, and any modeled refusal. Let \(P_\theta^{\pi,h}\) be the law of the consequences retained by the inquiry. Define the attainable response-profile set

\[
\mathscr R(h)=\left\{\bigl(P_\theta^{\pi,h}\bigr)_\theta:
\pi\in\Pi(h)\right\}.
\tag{R1}
\]

One common policy must operate across unresolved possibilities. The definition does not grant a different policy for each hidden true world. Nor does it combine the consequences for different parties into one reward. A requirement is a specified acceptance set \(\mathscr A\) of profiles; its feasibility is the assertion \(\mathscr R(h)\cap\mathscr A\ne\varnothing\).

**Proposition R1 Faithful description preserves capability.** Suppose two descriptions preserve initial uncertainty, joint transition and observation laws, the meanings of interventions and retained consequences, and implementable policies in both directions. Then their attainable response-profile sets agree after the corresponding relabeling. Every feasibility question expressed through those profiles therefore has the same answer.

**Proof.** Transport a policy through the faithful interface mapping. Its initial law agrees, and induction on the actual history shows that each next action, observation, and state transition has the corresponding law. Thus every attainable profile in the first description is attained in the second. The inverse mapping supplies the reverse inclusion. Intersection with any corresponding acceptance set preserves nonemptiness. ∎

The [invariance companion](../history/root-foundation/INVARIANCE-AND-PRIOR-ART.md) states a finite hidden-state version precisely. This strengthens the interpretation of the earlier canonical representation: the relevant invariant is not the spelling or number of variables, but preserved distinctions and feasible consequences under actual interventions.

A full labeled intervention-response model contains more information than the attainable set. For example, swapping which of two action labels produces zero and one leaves the set of achievable outcome distributions unchanged while changing the prediction for each named intervention. Capability equivalence therefore does not certify the causal identity of an action. The companion supplies the exact witness.

An improved sensor enlarges capabilities only when the old policies remain implementable. If receiving its output consumes the deadline or the reserve needed for action, the physical modification may shrink \(\mathscr R\). The mathematical value of additional free information and the physical cost of supplying information are separate questions.

The set \(\mathscr R\) is not generally constant in time. It is invariant under faithful redescription of the same situation. Activity can enlarge or shrink the next situation's attainable set by changing skills, resources, permissions, models, and social relations. That change is the object the generative theory needs to explain.

## 2 The time scale argument yields a finite theorem

The earlier discussion left open whether extending time necessarily reveals renewal. A finite-lifetime model gives a stronger answer than the statement that a function needs its conditions.

Consider \(n\) named types of functional support. Every instance of type \(i\) has a maximum unrenewed lifetime \(\tau_i>0\). A renewal is treated as a new instance for this accounting. Initial instances were established no later than time zero. Every later establishment of type \(i\) requires at least one currently functioning earlier parent instance of a permitted type \(j\). Draw the edge \(j\to i\). There is no later external entry of an organizational support instance. Physical matter and energy inputs may remain boundary assumptions, but any input that actually supplies a functioning instance or resets its lifetime must be counted.

The type set, lifetime bounds, and parent relations must be specified independently. Self-renewal is a self-loop; calling the same carrier by the same name does not erase its renewal event. Processes have no infinite event accumulation in finite time. Multiple parents and redundant supply routes are permitted; the graph includes the possible required parent relations.

**Theorem R2 Acyclic support has a finite continuation deadline.** If the type graph is acyclic, define in topological order

\[
d_i=\tau_i+\max\bigl(\{0\}\cup\{d_j:j\to i\}\bigr).
\tag{R2}
\]

Every functioning instance of type \(i\) expires no later than \(d_i\). Consequently no tracked support can remain functioning after

\[
D=\max_i d_i\le\sum_{i=1}^n\tau_i.
\tag{R3}
\]

**Proof.** A source type has only its initial instances, all expiring by \(\tau_i\). Suppose all predecessor bounds have been established. Any later type-\(i\) instance must be created while at least one predecessor still functions, so its creation time is no later than the maximum predecessor expiry. Adding its lifetime proves (R2). Topological induction completes the argument. The recursion sums lifetimes along directed paths; an acyclic path visits each type at most once, proving (R3). ∎

For a chain with lifetime bounds two, three, and five time units, the last possible functional expiry is bounded by ten. Observing continuation after ten would refute the jointly specified acyclic, bounded-lifetime, closed-entry model. At least one proposed lifetime, dependency, type restriction, entry boundary, or acyclicity claim would need correction.

**This is a precise version of the time scale insight:** if a finite vulnerable organization persists beyond the entire acyclic inheritance horizon, an account containing only one-way inherited support is inadequate. It must include a renewal cycle or a violation of the stated boundary assumptions. A short observation window can conceal this necessity.

A type-level renewal cycle is compatible with ordinary forward causation. Every individual event is caused by earlier events; the repeated type labels form the cycle across time. The theorem does not require an event to cause itself in its own past.

Cycles are necessary under these premises, but not sufficient for functioning. They may be too slow, too weak, inaccessible from the initial state, or unable to supply all jointly required functions. The previous mechanism and feasibility results address those further questions. Nor must every maintained component lie on a cycle: some can receive support downstream from one.

## 3 Sustained loss gives a second route to recurrent closure

Bounded lifetimes are sometimes inappropriate. Another formulation uses finite stocks with explicit provision. For finitely many support types, write cumulative balances

\[
C_i(t)=C_i(0)+E_i(t)+\sum_jR_{ji}(t)-L_i(t),
\qquad C_i(t)\ge0.
\tag{R4}
\]

Initial stocks are finite. \(E_i\) is cumulative external provision, \(R_{ji}\) cumulative internal provision from \(j\), and \(L_i\) cumulative loss. All cumulative provision and loss terms are nonnegative, nondecreasing, and finite on finite intervals. Internal provision must be causally justified; arbitrary retrospective credit assignment does not identify a support relation.

If \(L_i(t)\to\infty\), balance forces unbounded cumulative provision to \(i\). Since there are finitely many inputs, either its external provision is unbounded or at least one internal supplier contributes an unbounded amount. To follow that supplier backward, an additional assumption is indispensable: **a supplier providing unbounded cumulative internal service must itself face unbounded cumulative loss of a tracked capacity.** A permanently durable supplier would not satisfy this productive-vulnerability premise.

**Theorem R3 Recurrent support ancestry.** Under these assumptions, every node with unbounded cumulative loss is downstream, in the graph of unbounded cumulative internal provision, from an external recurrent source or a directed internal cycle.

**Proof.** Start from the node. If its external provision is unbounded, stop. Otherwise choose an internal predecessor with unbounded provision. Productive vulnerability gives unbounded loss for that predecessor, so repeat. A backward path in a finite graph either encounters an external recurrent source or repeats a node, creating a cycle. Reversing the traversed edges gives a forward provision path to the original node. ∎

This proof does not assume that all edges operate simultaneously, or that one time-independent equilibrium exists. It is a statement about recurrent provision across the observation horizon. Unbounded cumulative flow alone does not imply a positive limiting average rate or bounded gaps between renewals.

Without recurrent external organizational supply, the theorem requires an internal cycle upstream. It does not require energetic isolation: externally supplied energy can be indispensable even when the organization of its conversion is internally renewed. Conversely, merely declaring an input to be “background” does not make its organizational contribution disappear.

An infinite acyclic succession of new supplier types, a durable catalyst, a finite total loss, or recurring external establishment can evade this conclusion by violating a premise. These are explicit alternatives, not defects to hide by broadening the word selection. The [turnover companion](TURNOVER-AND-CLOSURE.md) gives the full scope and examples.

The companion also supplies a quantitative obstruction. If independently measured service and replacement bounds imply \(S(t)\le k+BS(t)\), with finite nonnegative \(k\) and nonnegative \(B\), then \(\rho(B)<1\) implies

\[
S(t)\le (I-B)^{-1}k.
\tag{R4a}
\]

The inverse is nonnegative because it equals \(\sum_{m\ge0}B^m\). Under the companion's routing and loss bounds, total turnover is then bounded too. Thus a cycle can exist while remaining incapable of sustaining unbounded turnover. For this bound, \(\rho(B)\ge1\) is necessary for unbounded service, but is not sufficient. Positive changes of service units give \(B'=DBD^{-1}\) and preserve the spectral radius. This is another exact invariance, with explicit conversion coefficients rather than an assumption that all forms of support share one unit.

## 4 Informed action has a joint information and execution boundary

The preceding results apply to any specified vulnerable function. To connect them to reasonableness, specify a modest epistemic function: correctly respond to a fresh circumstance by an operational deadline. This concerns factual responsiveness, not the truth of every proposition or the justice of every aim.

For two equally likely circumstances with observation laws \(P_0,P_1\), the smallest classification error is

\[
e^*=\frac{1-\operatorname{TV}(P_0,P_1)}2.
\tag{R5}
\]

For finite observations, choose the more likely circumstance at each observation; the resulting error is \(\frac12\sum_o\min(P_0(o),P_1(o))\), which equals (R5). Thus a required error limit imposes an information distinction; mere internal confidence cannot substitute for it.

Now make the channel and execution physically vulnerable. At each task the true context is a fresh fair bit, independent of the preceding record. With probability \(c\), an observation reveals the bit exactly; otherwise it reports an erasure. The erasure carries no information about the bit. The channel is an explicit modeling choice, not a claim that all knowledge is an erasure channel.

Its best per-task error, conditional on each realized history before the task observation and the current channel reliability, is \((1-c)/2\). We require continuous readiness: this conditional error must remain at most \(0<\varepsilon<1/2\) at every time when a demand could arrive. This requires

\[
c\ge c_*:=1-2\varepsilon.
\tag{R6}
\]

Let \(u(t)\in[0,1]\) be effort allocated to maintaining this channel. The remaining effort replenishes an execution reserve \(b\). A continuous operating model is

\[
\dot c=\alpha u(1-c)-\delta c,
\qquad
\dot b=s(1-u)-q,
\tag{R7}
\]

where \(\alpha,\delta,s,q>0\). Error is evaluated probabilistically at each task; it is not a guarantee that no individual answer is ever wrong. The reserve represents the separate ability to provide the required service, with \(b\ge0\). The effort law may depend on the available history. Both inequalities must hold continuously for each realized effort schedule. A marginal error averaged across histories, or accuracy required only at known isolated demand times, defines a weaker problem and does not imply this pointwise floor. Both requirements must be satisfied, rather than traded away inside one score.

Define

\[
u_{\min}=\frac{\delta c_*}{\alpha(1-c_*)},
\qquad
u_{\max}=1-\frac qs.
\tag{R8}
\]

**Theorem R4 Exact indefinite feasibility boundary.** From an initial \(c(0)\in[c_*,1)\) and finite \(b(0)\ge0\), there exists a policy maintaining both requirements indefinitely if and only if

\[
u_{\min}\le u_{\max}.
\tag{R9}
\]

If the inequality holds, any constant \(u\in[u_{\min},u_{\max}]\) is sufficient. If it fails, no adaptive or time-varying policy can avoid failure indefinitely.

**Proof of sufficiency.** At \(c=c_*\), effort at least \(u_{\min}\) makes \(\dot c\ge0\), while at \(c=1\) the derivative is \(-\delta<0\); hence \([c_*,1]\) is invariant. Effort at most \(u_{\max}\) makes \(\dot b\ge0\). The interval lies inside \([0,1]\) whenever it is nonempty because \(u_{\min}>0\) and \(u_{\max}<1\). ∎

**Proof of necessity and a finite deadline.** As long as both requirements hold, the auxiliary quantity

\[
W=\frac bs+
\frac1\alpha\log\frac{1-c_*}{1-c}
\ge0
\tag{R10}
\]

has derivative

\[
\dot W=u_{\max}-\frac{\delta c}{\alpha(1-c)}
\le u_{\max}-u_{\min}.
\tag{R11}
\]

The control cancels. If \(d=u_{\min}-u_{\max}>0\), a trajectory cannot remain acceptable beyond \(W(0)/d\), because the upper bound on \(W\) would become negative. This applies pathwise to admissible effort schedules. The initial perfect-channel case \(c(0)=1\) can be handled after a positive time: \(\delta>0\) makes it immediately imperfect, restoring the finite expression. ∎

The logarithmic term is an accounting device for usable reliability reserve, not a utility or thermodynamic entropy. No universal energy-per-truth cost is claimed. The coefficients are application-specific physical or organizational rates that would need measurement.

### An exact deadline that adaptation cannot evade

Take \(\alpha=6,\delta=1,s=4,q=1\). At tolerated error \(\varepsilon=1/10\), the viable effort interval is

\[
2/3\le u\le3/4.
\tag{R12}
\]

The smallest indefinitely sustainable error in this model is \(1/11\). Demand the stricter \(\varepsilon=5/58\), so \(c_*=24/29\) and \(u_{\min}=4/5>3/4=u_{\max}\). From \(c(0)=c_*\) and \(b(0)=1\), equation (R11) gives the exact upper bound of five time units. Constant effort \(u=4/5\) keeps the channel exactly at the required accuracy and spends reserve at rate \(1/5\), attaining that bound. Every policy eventually loses either the accuracy guarantee or executable service; rearranging effort cannot create a missing resource.

This is a quantitative connection between informed correction and reproduction of its conditions. It is stronger than saying that information is useful, and more limited than a universal law of rationality.

The timing requirement is essential. Under the same stricter accuracy target, a system that is assessed only at selected times can alternate a full-maintenance interval with an execution-provision interval and meet accuracy at the ends of maintenance indefinitely, while falling below the accuracy floor between assessments. The information companion gives the explicit schedule. Passing those scheduled tests does not establish continuously available correction. This is a mathematical distinction between two service claims; whether an actual institution or AI system exploits that distinction is an empirical question.

## 5 Selection can reproduce either adequate or inadequate correction

The feasibility interval says what could be maintained. A separate mechanism must explain what is actually maintained. The information companion supplies a constructed selection model with \(u(x)=1/2+x/5\):

\[
\dot c=6u(x)(1-c)-c,
\qquad
\dot x=x(1-x)(5c-4).
\tag{R13}
\]

Here \(x\) is the share of a higher-renewal practice. The declared selection law favors that practice only when reliability is already sufficiently high. The two locally attracting equilibria are

\[
(c,x)=(3/4,0),\qquad (c,x)=(21/26,1),
\tag{R14}
\]

separated locally by the saddle at \((4/5,5/6)\). At required error \(1/10\), the lower equilibrium fails the accuracy condition while the upper one satisfies it. Both can reproduce their own practice-selection conditions. The companion verifies stability and provides explicit invariant regions; it does not claim a complete global basin classification.

Thus selection–renewal feedback can generate both persistent epistemic failure and persistent adequate response. Its presence does not select truth automatically. A theory of alignment must assess which independently specified function is maintained and how transitions between regimes can actually be implemented.

## 6 What the three results establish together

The results can be joined under their common application assumptions:

1. A required response profile must belong to the system's attainable set; no faithful change of description alters this feasibility.
2. If the response requires discriminating circumstances, actual observation channels must provide the corresponding distinction, and execution must remain feasible.
3. If those capacities are implemented by finitely many support types satisfying the lifetime or productive-vulnerability premises, their continuing provision must have the recurrent ancestry described in R2 or R3.
4. Supplied selection and renewal mechanisms can then explain which feasible or infeasible regimes the actual system enters and retains.

This yields the more substantive conditional conclusion:

> Sustained informed correction by a finite vulnerable organization requires recurrent provision of its ability to distinguish relevant circumstances and execute responses. Beyond the acyclic inheritance horizon, that provision must involve continuing organizational input from outside the modeled system or internal renewal cycles in its support ancestry.

The conclusion is a necessity, not a promise that the required capacities or cycles exist. It is universal over the stated class. It does not require a uniform human purpose, literal biological reproduction, centralized optimization, or a special financial vocabulary.

It also does not say that every physical event is selection. A selected response can transform the capacities governing future selection; that return path is a substantive causal mechanism to identify. A renewal cycle somewhere upstream does not prove that all maintained components mutually reproduce one another, or that all organizational change follows a selection gradient.

## 7 Truth and reasonableness acquire an operational bridge

The theory can analyze three distinct questions: whether a claim corresponds to an independently specified circumstance, whether available evidence distinguishes the relevant alternatives, and whether a response can be executed and continued. It does not answer the first merely by proving the third.

An institution can maintain confidence while losing access to discriminating observations. A system can preserve an accurate record whose meaning no successor can use. An organization can remain viable while systematically imposing unacceptable burdens on others. These possibilities are consistent with renewal and are reasons to retain separate outcome, information, execution, and normative conditions.

Reasonableness, when it means being responsive to evidence and feasible consequences, therefore has material conditions. Sustaining those conditions becomes an explicit part of the theory. When reasonableness means moral justification, the evaluation still needs an account of whose interests count, permissible burdens, and legitimate revision. Physical persistence cannot settle those questions by itself.

Mathematical truth is also not identical to the survival of a physical proof record. A record's loss can destroy our access to a proof without changing the mathematical proposition. Our account concerns the realized capacity for inquiry, justified belief, and action; it is not a definition of truth as whatever survives.

## 8 New discriminating consequences

The root becomes scientifically useful through commitments made before inspecting outcomes:

- A proposed finite acyclic account with measured lifetimes predicts a finite continuation ceiling. Longer operation calls for a specified correction to that account, such as an omitted renewal edge or external establishment route.
- In the erasure-channel operating model, separately measured rates predict the maximum sustainable accuracy and a finite failure deadline when demands exceed it. Changing only the effort schedule cannot cross the proved boundary; changing technology, support supply, demand, or the observation model can.
- A present accuracy measurement can coexist with eventual failure because finite reliability and execution reserves temporarily hide an unsustainable allocation. Current performance is not a certificate of continued performance.
- A gain in informational precision can reduce implementable capability when acquiring it consumes needed time or resources. The direction of its practical effect must be assessed in the paid process.
- Stable renewal can preserve an inadequate correction regime. Establishing a favorable attractor and identifying a feasible path into its basin are different intervention tasks.

These are proposed application tests, not reported empirical discoveries. The earlier mixed evidence and unrun prospective handoff experiment remain unchanged.

## 9 Existing science and what this development adds

The ingredients have important predecessors. [Blackwell's comparison of experiments](https://doi.org/10.1214/aoms/1177729032) relates information structures to decision possibilities. [Montévil and Mossio](https://montevil.org/publications/articles/2015-mm-organisation-closure-constraints/) analyze biological organization through mutually maintained constraints at different timescales. [Steel and Hordijk](https://arxiv.org/html/1801.03953v2) give precise cycle and autocatalytic-set results in elementary chemical reaction systems. The elementary finite-graph cycle lemma is not new.

The information–viability connection is also established. [Kolchinsky and Wolpert](https://arxiv.org/abs/1806.08053) define a form of semantic information using interventions on correlations relevant to continued existence. [Sowinski and colleagues](https://arxiv.org/abs/2304.03286) demonstrate information thresholds in a resource-foraging model. Our work does not originate the claim that information can have physical significance for persistence.

The advance within this project is the precise join: faithful capability invariance, turnover-derived renewal ancestry, finite acyclic deadlines, a quantitative obstruction to insufficient renewal cycles, and an exact joint observation–execution feasibility bound. This replaces an assertion of universal feedback with stated necessity conditions and a quantitative bridge to informed correction. The particular combination and derivations warrant specialist scrutiny; no exhaustive priority claim has been established.

## 10 Review materials

- [Review entry point](README.md): result map, resolved cross-review findings, exact checks, provenance, and questions for external specialists.
- [Turnover and closure](TURNOVER-AND-CLOSURE.md): lifetime theorem, recurrent-flow theorem, counterexamples, and relation to existing closure results.
- [Information and renewal](INFORMATION-AND-RENEWAL.md): statistical distinction bound, paid maintenance and execution theorem, deadline, and endogenous-selection witness.
- [Invariance and prior art](../history/root-foundation/INVARIANCE-AND-PRIOR-ART.md): exact policy transport, capability order, information comparison, and distinctions between capability and causal equivalence.

Three internal cross-reviews checked the assembled arguments. The final revision makes the history-conditional, continuous-readiness requirement explicit and includes the scheduled-assessment counterexample; it also supplies the previously implicit routing coefficients in the spectral example. The [exact checks](../history/root-foundation/EXACT-CHECKS.json) pass 28 groups of finite enumerations and rational calculations. The [readiness figure](../history/root-foundation/continuous-readiness.png) illustrates the counterexample using analytic model trajectories. These checks and reviews are neither empirical validation nor independent human peer review.

The universal claim is strongest when its quantifiers remain visible. The invariant is what can be realized through the actual interface; the necessity is continued provision under vulnerability; the explanatory work is identifying the mechanisms and their regimes. Whether these premises exhaust the physically relevant cases remains a scientific question rather than a result produced by changing the meaning of universality.
