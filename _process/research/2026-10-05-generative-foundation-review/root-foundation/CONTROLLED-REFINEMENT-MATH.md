# Exact representation in the presence of a learner

6 October 2026. AI-authored mathematical companion to the [canonical interface](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/CONTROLLED-REFINEMENT.md). This advances **material process → observation-dependent response → compatible composition**. The mechanism, channel and controller remain supplied. The argument specializes the repository's existing finite-history lifting theorem; it is not a new general theory of learning.

## 1. The missing premise

The [causal core](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/GenerativeCore.lean) represents admissible event histories. The [controller interface](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/learning/ControllerRevision.lean) restricts those events by memory-dependent commands and updates memory from observations. An exact representation of the first does not automatically remain exact after the second is attached.

Let \(P\) have states \(S\), let \(Q\) have states \(T\), and let both use actions \(A\). A proposed representation \(q:S\to T\) is locally exact when, for every concrete state \(s\), action \(a\) and abstract successor \(u\),

\[
Q(qs,a,u)\quad\Longleftrightarrow\quad
\exists t\;[P(s,a,t)\land qt=u]. \tag{1}
\]

This is exactness from **each actual representative**. A quotient constructed by collecting edges from different representatives need not satisfy (1).

Let complete observation channels be \(O_P:S\times A\times S\to O\) and \(O_Q:T\times A\times T\to O\). The additional compatibility premise is

\[
P(s,a,t)\Longrightarrow O_P(s,a,t)=O_Q(qs,a,qt). \tag{2}
\]

Only admitted concrete events are constrained. The channel includes every input used by this controller's update: an unrecorded resource reading, clock or physical interaction cannot silently be excluded.

The same deterministic controller is used on both sides, with command \(\pi:M\to A\) and update \(U:M\times O\to M\). Its inherited memory is retained, not reset. A controlled step is

\[
(s,m)\xrightarrow{(a,o)}(t,n)
\Longleftrightarrow
P(s,a,t)\land a=\pi(m)\land o=O_P(s,a,t)\land n=U(m,o).
\]

Define \(\widehat q(s,m)=(qs,m)\).

## 2. Controlled representation theorem

**Theorem.** Under (1) and (2), \(\widehat q\) is locally exact between the two controlled processes. Consequently, for any concrete initial pair \(p\), finite action/observation word \(w\), and abstract final pair \(r\),

\[
\operatorname{Trace}_{Q_C}(\widehat q p,w,r)
\Longleftrightarrow
\exists t\;[\operatorname{Trace}_{P_C}(p,w,t)\land\widehat q t=r]. \tag{3}
\]

Both directions preserve the complete event word. The endpoint retains the abstract world state and **exactly the final memory**, including its causal dependence on the inherited memory.

**Proof.** A concrete controlled step projects by (1); (2) preserves its observation, so its chosen action and updated memory satisfy the same controller equations. Conversely, lift the abstract world edge from the particular concrete predecessor using (1). Its observation agrees by (2). Pair its concrete successor with the abstract successor's memory; the same update equation makes this a valid concrete controlled step. These two directions establish local exactness for \(\widehat q\). Apply `local_exact_iff_trace_exact` from the existing core to obtain (3). Existentially quantifying the endpoint gives equivalence of finite controlled-word feasibility. ∎

The lifted endpoint is **some** concrete successor in the specified fibre. The result does not assert that every representative is reachable. Nor does a feasible controlled history mean that every nondeterministic outcome succeeds: the underlying world law remains a relation and the statement is existential.

These premises are sufficient. They are not all necessary for a particular controller's command behavior. A controller may never choose some actions, and it may ignore some observation differences. Exactness of action/observation-labelled histories is a stronger contract than equality of action-only behavior. Coarsening the observations or changing the memory representation would require another explicitly justified mapping.

The action vocabulary and step granularity are shared. A sequence of molecular reactions implementing one abstract learning update needs an additional event/trace mapping, including the intermediate costs. This theorem does not identify a multi-reaction implementation with a single instantaneous step.

Compatible interfaces can also be chained: if \(q\) and \(r\) each satisfy local exactness and preserve the relevant observations, their composite \(r\circ q\) does too. For lifting, first lift through \(r\), then through \(q\) from the actual concrete predecessor. Observation equalities compose along the projected edge. Thus the same controlled-history result applies through several already certified descriptions without resetting memory between them.

## 3. A testable obstruction to a proposed summary

Equation (2) implies that two admitted concrete edges with the same projected predecessor, action and projected successor have the same observation. Otherwise the single abstract edge would need to supply two different values through its declared deterministic observation channel.

Thus an observation difference across such a pair refutes that channel factorization. It does not refute the substrate account. It says the proposed summary, channel or controller interface needs revision.

## 4. A paid counterexample

Take a concrete world state consisting of a persistent Boolean bit and a natural-number fuel stock. Every action consumes one unit when fuel is positive and preserves the bit. The abstract state retains only fuel, with the same available actions and the same unit decrement. Forgetting the bit therefore satisfies (1): every abstract action lifts from every concrete bit value, and all unrestricted finite action possibilities are retained.

A supplied controller first probes, stores the returned bit, and then chooses the corresponding response. The concrete probe reports the bit. An abstract probe that always reports `false` fails (2) at the `true` state. Starting with two fuel units and the same uninitialized memory, the concrete `true` world admits the controlled command sequence **probe → respond true**; the abstract controller instead commands **probe → respond false**. This is a difference in action behavior, not merely a renamed observation label.

Both world descriptions preserve the unit-cost account. The failure is caused by lost information, despite exact world possibilities and matching fuel expenditure. The counterexample supplies its probe and memory mechanism; it is a diagnostic of representation, not a claim that this hardware forms spontaneously.

## 5. Resource transport and its limit

An independently established abstract support law can be pulled back along the world-step-preserving map and then restricted to controlled steps, using the existing `sustain_law_pullback` and `closed_loop_account_law` results. For example, if

\[
b_Q(qt)+d_Q(qs,a,qt)\le b_Q(qs)+c_Q(qs,a,qt)
\]

holds on the abstract edge, the same inequality holds for the pulled-back concrete account and on its controlled edges.

To identify this with an independently specified material budget, its reserve, expenditure and credit must agree with those pullbacks on the relevant states and edges. Otherwise the theorem preserves only the declared account. It cannot invent omitted formation, sensing, memory-writing, maintenance or delivery costs. Observation compatibility and budget compatibility are separate obligations.

## 6. What this closes

The result supplies a checked criterion for transporting the behavior of an already specified learner through a world representation. It joins two existing mathematical interfaces, rather than adding another synthetic learner.

It does **not** assert a mapping between the typed-part selector construction, recyclable-slot updater construction and paid predictive learner. Their actual laws must establish the premises, or a weaker one-way/restricted mapping must be stated. Probability transport additionally requires compatible transition probabilities; finite possibility equivalence does not supply them. Hardware origin, calibration, shared evaluative use, empirical adequacy and the full foundation remain further obligations.

The formal implementation and its verification record are linked from the canonical interface. An independent collaborating-AI review records the accepted scope and any repairs separately.
