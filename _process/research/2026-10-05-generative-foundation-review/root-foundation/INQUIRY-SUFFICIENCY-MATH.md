# Sufficient inquiry in a changing situation

6 October 2026. AI-authored conditional composition of existing results under the [nondual method](../../../../theories/becoming/chapters/NONDUAL-METHOD.md). Named connection: **acquired understanding → feasible further activity → changed conditions of sufficiency**. This note does not install a stopping rule or derive a criterion of acceptable action from a numerical score. It connects a standard bounded contingent-policy argument to a newly isolated implication of an existing actual learner history.

The [earlier permission/choice result T13](HUIGEN-REASON-TRANSPORT.md#t13-exact-sufficiency-for-permission-and-for-choosing) already establishes the common-response condition under partial evidence. The [experimental-access mathematics D1](EXPERIMENTAL-ACCESS-MATH.md) already propagates candidate configurations through actions before filtering observations. The [application contract](EVALUATIVE-APPLICATION-MATH.md#5-composition-with-the-actual-paid-trace-and-addressed-claims) already warns that inquiry changes available opportunities. The following makes their dynamic composition explicit. The recurrence is standard finite contingent planning, not a new algorithm or proof of generative theory's exclusive explanatory power.

## 1. Start with the activity whose continuation is at issue

The investigated configuration includes whatever affects the declared continuation: the current process, operative contacts, retained information, other affected activity, timing, resources and relevant constraints. These are conditional modeling choices within the situation, not a foundational decomposition into an independent knower and world.

For this bounded representation let \(X\) be the configuration set, complete with respect to the declared continuation contract, and let a nonempty finite \(B\subseteq X\) represent all configurations still admitted by the accessible evidence. Its members share the inquirer's present accessible information, including relevant retained history; any available distinction must participate in that information state. It must include the actual represented configuration for an all-member guarantee to apply. Empty compatibility is model failure or inconsistent premises, not universal permission by vacuity. Completeness relative to this contract is not a claim to represent every aspect of generative reality.

For an inquiry operation \(q\), let

\[
T_q(x)\subseteq Y\times X
\]

be its finite set of possible observation/successor pairs. This finite-successor condition ensures that every branch below remains finite. Undefined operations have \(T_q(x)=\varnothing\); modeled failure with an actual effect is instead a pair containing that effect. Let \(P_q(x,y,x')\) state the independently specified prefix conditions this execution must preserve. It may express a physical continuation condition, a scoped legitimate constraint, or both where justified; no universal ethical meaning is built into the symbol.

Let \(D(x)\) be the set of terminal responses that are feasible and meet the particular declared continuation requirement from \(x\), including their own effects and execution conditions. Membership requires the response contract to hold for **every admitted outcome of the response**, not merely one favorable execution. A response is one and the same executable operation or specified finite sequence across the configurations, not an outcome label realized by a different hidden-state-dependent plan in each. The claim requires \(\exists r\,\forall x\), not merely \(\forall x\,\exists r_x\). Relevant earlier effects remain in the configuration/history; a favorable endpoint cannot erase a violated prefix condition. Terminal means ending this bounded inquiry episode, not ending all activity. Doing nothing, declining, waiting or performing another test is not automatically in \(D(x)\); each has actual consequences to assess. If an inquiry itself completes the relevant undertaking, a suitable completed-state response can represent that fact.

These sets do not derive the requirement, its authority or its relevance. They express it so that the informational and dynamic implications can be tested. The origin and warranted revision of a criterion remain substantive questions. Merely calling every favorable output acceptable would assume the connection being investigated.

## 2. Ambiguity is compatible with sufficient understanding

The inherited common-response condition is

\[
C(B)=\bigcap_{x\in B}D(x).
\tag{S1}
\]

A particular response can be certified across the admitted situations exactly when it is in \(C(B)\). A singleton is unnecessary: different configurations can support the same response. Conversely, a singleton does not make \(D(x)\) nonempty or make a currently unavailable response occur. This is a semantic condition; identifying and realizing its members requires an actual mechanism.

For a factual question \(f\), exact answerability similarly requires constancy of \(f\) on \(B\). That criterion is already established in the [earlier scientific inquiry study](SCIENTIFIC-INQUIRY-CONDITIONS.md). It does not imply that every action associated with the answer is feasible or warranted. A correct next-reading forecast, an executable observation and an appropriate next undertaking are distinct claims within the same situation.

If \(B'\subseteq B\) refers to the **same configurations and response sets**, then \(C(B)\subseteq C(B')\). This static monotonicity must not be applied to actual inquiry that changes the configurations. The changed state can remove an action, fulfill its purpose, alter its relevance or create a new demand.

## 3. Inquiry transports possibilities before sorting them by evidence

The current branch after observation \(y\) is

\[
B_{q,y}=\{x':\exists x\in B,\ (y,x')\in T_q(x)\}.
\tag{S2}
\]

This is a set of successor configurations, not a subset of old labels held fixed. The observation \(y\) includes all newly accessible information on which this policy may branch; recording only a sensor bit while ignoring an accessible changed counter would describe a weaker interface. Model identities and causal histories must remain in \(x'\) wherever later interpretation depends on them. Configurations that merge may be represented together only when the represented future no longer depends on their distinction.

Call \(q\) admissible from \(B\) when it is available at every \(x\in B\), every modeled outcome satisfies its prefix condition, and the operation includes the actual means of producing and retaining the observation needed by later decisions. The last clause concerns the represented execution contract; an analyst's external log is not automatically accessible evidence. Resource bounds alone do not establish that a query or decoder is installed.

The decomposition into inquiry then terminal response is local to this analysis. Inquiry may also transform the condition it is investigating. Its effects are retained in \(T_q\), \(P_q\) and \(D\), rather than removed by calling it observation.

## 4. A finite contingent continuation criterion

Assume finite query, observation and terminal-response repertoires. Consider deterministic strategies that use only the retained observations, issue at most \(n\) inquiry operations, and then take one terminal response. Their physical implementation is an additional obligation; this section characterizes permitted finite policy trees over the specified interface.

Define

\[
W_0(B)\iff C(B)\ne\varnothing,
\]

\[
W_{n+1}(B)\iff
C(B)\ne\varnothing
\ \lor\
\exists q\left[
q\text{ is admissible from }B
\ \land\
\forall y\ (B_{q,y}\ne\varnothing\Rightarrow W_n(B_{q,y}))
\right].
\tag{S3}
\]

**Conditional equivalence.** \(W_n(B)\) holds exactly when a finite observation-contingent policy tree with at most \(n\) inquiry operations satisfies all specified prefix conditions and finishes with a response in \(D(x)\) for every execution from every \(x\in B\).

**Proof.** At depth zero the same terminal response must work in every admitted configuration, exactly (S1). At positive depth a successful tree either responds immediately or begins with one common query: it cannot branch on a hidden actual state before obtaining a distinguishing observation. That query must be available and satisfy all prefix conditions. After observing \(y\), its subtree must work from every possible successor in (S2), giving \(W_n\) by induction. Conversely, an immediate common response supplies a successful leaf. Otherwise choose the query in (S3) and, for each of its finitely many nonempty observation branches, an inductively supplied subtree. Their combination has the required bound and guarantees. ∎

This is a universal finite-path guarantee, not probability-one eventual success under a stochastic law. In particular, a positive chance of eventually escaping a loop does not give a bounded tree that succeeds on every admitted outcome sequence. The [primary comparison](INQUIRY-SUFFICIENCY-COMPARATORS.md) specifies the relationship to established partially observed planning.

For finite repertoires, random choice does not add a zero-error bounded tree when no deterministic one exists: every positive-probability query or response in such a guaranteed strategy must satisfy the same branchwise conditions. Choosing one such option recursively produces a deterministic tree. This statement assumes the same available interface and modeled outcomes. It does not deny benefits of randomization for approximate or probabilistic guarantees, whose established examples remain in [reason transport](HUIGEN-REASON-TRANSPORT.md).

Equation (S3) is not a new native event law or a proof that the present learner computes it. A policy tree may require unavailable memory, planning or actuation. Full implementation claims must put those operations and their effects into the configuration/transition account and exhibit their actual construction and use. Nor does \(W_n\) select a uniquely best tree when several satisfy the requirement.

## 5. The existing history makes the change concrete

The [mechanism reconstruction](INQUIRY-SUFFICIENCY-MECHANISM.md) identifies the actual `four_feedback` prefix in the earlier method learner. After acquisition readings `010`, its compatible candidates are the learned three-state and generated four-state models, both at their respective state zero with normal reading parity. Both predict zero after the next advance. Thus that particular next-reading question has an exact common answer despite two surviving models.

The actual next action/read yields zero and removes neither candidate. It advances both to their respective state one. Now a further advance predicts one in the three-state candidate and zero in the four-state candidate. The rolling next-reading question has become unresolved, although no retained observation became false and no candidate was added. The first correctly answered question concerned an earlier position; it must not be silently transferred to the new position.

This is a concrete consequence of propagating the situation in (S2). Counting candidates, or filtering identities without their current states, would miss it. It is not evidence that acquiring a correct observation intrinsically decreases knowledge. The current situation and the question indexed to it changed together.

These source candidates represent the future-reading projection, not the full configuration/requirement interface of (S3). The calculation is therefore an exact instance of changing question-relative answerability, not a demonstrated \(W_n\) policy in the physical learner. Applying the full recurrence would also require its actual controller, support, action effects and declared continuation contract to be represented and checked.

The original routine continues until a singleton, compacts one model and performs its later test. Its model-acquisition claim concerns all future readings within the admitted stable class; one-step agreement does not meet that stronger task. We have not installed a response-agreement reader or proved that earlier termination is executable in that routine. The result identifies sufficient content for a particular question, not a free shortcut around the actual protocol, a refutation of its stated purpose, or a recommendation to replace the full research goal with next-step prediction.

A separate saved exact-budget fixture, with its declared prior reduction of the available reserve, reaches a correct retained four-state model, confirms its next use and ends with zero local fuel. This is a boundary comparison, not the ordinary `four_feedback` endpoint. Under that source's unchanged tariffs, every native action or reading requires at least one quarter unit. No further nonempty native command sequence can begin there. This separates exact retained content from continuing operational capacity. It does not exclude passive persistence, outside support or different mechanisms, and does not prove the earlier inquiry was normatively excessive.

## 6. What this advances and leaves unresolved

The previous [inquiry-interface round](INQUIRY-INTERFACE-ARGUMENT.md) showed acquired consequences changing the duration of actual inquiry under a supplied singleton criterion. This round now identifies why singleton count is not itself the general meaning of sufficient inquiry. Sufficiency is relative to a concrete question or continuation, its horizon, what the activity has already changed, and the means still available.

The exact common-response theorem was already known here; the new source implication is the same-history loss of **rolling next-question agreement** through a truthful, non-eliminating step, together with the separate exhausted-but-exact endpoint. The dynamic composition spells out how to preserve these relations in a larger account. It adds no universal reward, no new guarantee of ethical adequacy and no installed stopping controller.

The remaining formative connection is **how an organized activity acquires and revises which unresolved differences matter to its further continuation**, including the consequences of continuing to investigate. A future construction must show relevant effects changing an operative criterion and later activity depending on that change. It must also retain occasions when a criterion hides a relevant difference or preserves a programme at the expense of what justified it. That is the particular mechanism still to explain; another supplied sufficiency predicate or a renamed higher controller would not do so.
