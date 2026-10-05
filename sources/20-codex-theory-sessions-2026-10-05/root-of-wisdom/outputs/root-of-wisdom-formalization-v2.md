# An invariant foundation for understanding and wise action

Revised for Ren on 5 October 2026. The aim is a compact, fundamental principle with indispensable assumptions, invariant consequences, and genuine explanatory force. The earlier judgment architecture is preserved as [the first formalization](root-of-wisdom-formalization-v1.md). This revision seeks the principle beneath that architecture.

**The strongest mathematical core supported by the current work is preservation of consequences across descriptions, together with a precisely irreducible representation of those consequences.** It has an exact theorem and constructive finite realizations. We have not established that it selects the actual laws of the universe or uniquely grounds every moral judgment. Those are substantive parts of the requested ambition, and remain in view.

## The proposed fundamental principle

> An adequate description preserves the consequences of the changes it claims to describe. Its irreducible content consists of distinctions whose removal would change those consequences.

“Consequences” must have an interpretation established independently of a model's preferred answer. They can include observations, physical outcomes, costs, permissions, or effects on affected beings. An intervention is a specified change in the process, not merely a change in its description.

This principle has two directions. It allows us to remove distinctions that never affect the declared consequences. It prohibits removing distinctions that can make such a difference. It also prohibits granting an actor knowledge or powers simply because the analyst's representation contains them.

This is a proposed foundational interpretation of the mathematics below. The mathematics concerns exact representations of declared processes; the philosophical claim that this identifies the deepest root requires further argument.

## The invariant equation

For a deterministic controlled process, let:

- \(X\) be its possible states;
- \(A\) be a specified family of interventions;
- \(T_a:X\to X\) be the effect of intervention \(a\);
- \(c:X\to Y\) be the independently interpreted consequences or answers we retain;
- \(q:X\twoheadrightarrow Q\) be a proposed description, possibly merging states.

The exact equations are

\[
\boxed{
q\circ T_a=\bar T_a\circ q\quad(\forall a\in A),
\qquad
c=\bar c\circ q.
}
\tag{1}
\]

The first says that changing the real process and then describing it gives the same represented state as changing its description using the represented law. The second says the description still answers the retained questions correctly. Both are necessary for the claimed exact representation. The question includes all states in the declared domain, not only those encountered in a successful demonstration.

For this theorem, interventions are total maps in a common action vocabulary. Processes with partial availability need an explicit interface for available actions and denied or terminal outcomes. That interface must be preserved; it is not supplied for free by the equation.

For a bijective change of coordinates, transporting the whole law makes (1) automatic. For a proposed state-merging description, it is a substantive test: two states assigned the same description must have the same retained consequences and lead to the same next description under each intervention. A change of coordinates, a symmetry of a fixed law, and a faithful reduction are different claims.

## The irreducible content can be derived

Let \(A^*\) denote finite intervention sequences, including the empty sequence. Write \(T_w\) for executing sequence \(w\) in order. Define

\[
x\sim y
\quad\Longleftrightarrow\quad
\forall w\in A^*:\ c(T_wx)=c(T_wy).
\tag{2}
\]

Thus two states are equivalent exactly when every declared future intervention test gives the same retained answer. Define

\[
\boxed{Q_{\min}=X/{\sim}.}
\tag{3}
\]

**Theorem.** This quotient is the coarsest exact state description preserving all the declared future answers. It satisfies (1). Every other exact state description satisfying (1) distinguishes at least the same equivalence classes. Minimal descriptions of this kind are unique up to renaming.

**Proof.** Equality of all test answers makes \(\sim\) an equivalence relation. The empty sequence ensures \(c(x)=c(y)\) when \(x\sim y\). Prepending an intervention to every future test gives \(T_a x\sim T_a y\). Consequently \(\bar T_a([x])=[T_a x]\) and \(\bar c([x])=c(x)\) are well-defined and satisfy (1).

Now let \(r:X\twoheadrightarrow Z\) be any other exact description satisfying (1). If \(r(x)=r(y)\), induction over the intervention sequence gives equal represented successor states and hence equal retained answers for every sequence. Therefore \(x\sim y\). The map \(f:Z\to Q_{\min}\), defined by \(f(r(x))=[x]\), is well-defined and satisfies \(q_{\min}=f\circ r\). Thus every exact description can be reduced to this one. No two different classes of \(Q_{\min}\) can be merged: some finite intervention sequence distinguishes their answers. □

This is an exact, warranted meaning of **irreducible**. It concerns state distinctions relative to stated interventions and consequences. It does not prove the shortest possible formula, the smallest set of axioms in every language, or the ultimate ontology of the world.

The theorem permits infinite state spaces. When states and interventions are finite and their tables are available, start by grouping states with equal \(c\). Repeatedly split a group whenever an intervention sends its members into different current groups. Splitting terminates and yields exactly \(Q_{\min}\). This constructs the result rather than presupposing which states may be merged.

## A distinction that looked irrelevant becomes necessary

Suppose two machines currently display the same warning. Waiting leaves each unchanged. Applying repair leads to a safe outcome in the first and a dangerous outcome in the second. The warning alone is an adequate description for the passive observations in this example. It is inadequate for the repair question: a single represented state cannot have both required deterministic repair outcomes.

Equation (1) fails for that proposed merge. Equation (2) identifies the missing distinction because the one-step test “repair” separates the two states. No increase in confidence about their identical warning fixes the problem.

The same structure applies to an omitted permission, a hidden dependency, or a burden borne by someone absent from the current account—provided the corresponding intervention or consequence is correctly specified. The equation helps diagnose the omission once those possibilities are expressible. It does not automatically invent the instrument, concept, or ethical recognition needed to expose it.

There is also a useful refinement result. If we add interventions or retained questions while preserving all the old ones, the new equivalence can only become finer. Previously equivalent states may separate; previously distinguished states cannot become equivalent under this unchanged old evidence contract. Replacing a mistaken question is a different operation and need not obey that refinement order.

This explains how one invariant requirement can govern expanding understanding without requiring one final, permanently sufficient model.

## Probabilities and actual agency

For a finite stochastic process, let \(P_a\) be its transition matrix and \(C\) the indicator matrix of a proposed partition: \(C_{x,z}=1\) exactly when \(q(x)=z\). The corresponding exact one-step condition is

\[
\boxed{P_aC=C\bar P_a\quad(\forall a),\qquad c=\bar c\circ q.}
\tag{4}
\]

It says that states sharing a description have the same probabilities of entering each next description under the same intervention. With the appropriate initial distribution and compatible observations and policies, this preserves the retained finite path laws. The recent generative-basis work constructs a coarsest stable partition for this stronger quotient requirement.

Do not identify stochastic equality of future output distributions with this partition condition without proof. The deterministic minimality argument above cannot simply be transferred unchanged to every probabilistic or decentralized representation class.

Agency introduces a further obligation. Let \(L_M(\pi)\) be the possible interpreted traces of an admissible policy in the original model, and \(L_E(\sigma)\) those in its representation. Admissibility includes the actual information, timing, means, and permissions. The newest completeness bridge proves that the two contracts

\[
\forall\sigma\ \exists\pi:\ L_M(\pi)\subseteq L_E(\sigma),
\qquad
\forall\pi\ \exists\sigma:\ L_E(\sigma)\subseteq L_M(\pi)
\tag{5}
\]

are equivalent to preserving attainability for **every** sure trace objective. Sufficiency follows by inclusion; necessity follows by choosing each policy's trace set as the objective. Finite termination and deadlock must remain represented. For a narrower objective family, (5) is sufficient but may be stronger than necessary. For probabilistic objectives, preserve the relevant probability laws as well.

This is how the invariant reaches practical judgment: a model must preserve what an actor can actually guarantee, including failures and limitations. Describing a hidden state does not entitle the actor to observe it. Knowing a successful response exists does not supply its means of execution.

## The latest work already connects the mechanisms

The newest full-picture report materially changes the earlier status. Its constructed process joins paid inquiry, candidate formation, fresh checks, evaluator revision, installation, ordinary service, archive maintenance, training, and succession. The source reports 486 reachable states and 506 transitions in its baseline certificate, with separately analyzed failures when mechanisms are removed or corrupted.

Its general installed-process theorem is also stronger than the earlier component list. For a declared totalized transition system, all actual paths from the declared initial states preserve protection and repeatedly deliver each required event exactly when there is a closed safe region containing every declared initial state and, for each event, a well-founded rank decreasing on every step that does not deliver it. The state space can be infinite, and installed controllers and evaluators can change. An indefinitely missing event would force an impossible infinite descent. The converse constructs ranks from the absence of such a path, under the stated ordinary set-theoretic assumptions.

This characterization addresses the process actually installed. It does not quietly replace a failing process with an ideal controller. Its protection and event interpretations remain explicit premises; recurrence need not be required when the relevant duty is completion, rest, refusal, or exit. Mathematical ranks are certificates, not unobserved information granted to the actor.

The newer scientific-inquiry work also integrates continuing service, complaints, paid inquiry, mandate revision, fresh testing, and upkeep. A separate successor experiment reports actual AI responses showing a bounded benefit from timely feedback and usable corrective handoffs, while a conventional learner also solves its supplied rule family. Its queue experiment gives a concrete failure of treating coupled financing and permission effects as independent factors.

These results supply realizations, counterexamples, and bridges. This revision inspected their reports and selected proofs; it did not rerun their full simulations or model-response experiments. Their completed contributions should count. Their existence does not establish that the present interpretation is the unique explanation of them.

## Which assumptions are indispensable

The following witnesses show independence of requirements for this exact representation contract, not absolute irreducibility of every possible foundation.

| Remove this requirement | What can then go wrong |
| --- | --- |
| Retained consequences \(c=\bar c q\) | Identity dynamics allow a one-state quotient even when the two real states have different current harms. Transition preservation alone misses the harm. |
| Preservation of every admitted intervention | The two machines agree under waiting and diverge under repair. Checking only ordinary behavior approves a false merge. |
| Transition compatibility | Two presently equal outputs can conceal different next outcomes. A static summary fails as a law of change. |
| Actual information and permission constraints | A model can prescribe different responses in two situations the actor cannot distinguish, or prescribe an unavailable intervention. |
| Independent meaning and empirical warrant | Two internally coherent accounts can describe different worlds. Algebraic consistency does not establish which account applies. |

Several tempting claims fail more broadly. If a scalar quantity is required to be invariant under every map of a nonempty state set to itself, constant maps force that quantity to be constant. Meaningful invariance therefore needs a stated transformation class. If every possible state predicate must be recoverable, every distinct state must remain distinct. This blocks universal lossless merging of states, not compact generative laws.

Finally, covariance does not select a dynamics. The identity map and a bit-flip map each admit a perfectly consistent change of coordinates, yet predict different changes. Every process admits its own identity description. Consequently equations (1)–(4) constrain faithful descriptions but do not by themselves choose the world's physical law.

## Relation to wisdom and truth

This revision places the earlier judgment architecture downstream of a stronger foundation. Before evaluating a response, ask whether the representation preserves the distinctions that can change its consequences and whether its policy claims respect actual agency. The generator and revision mechanisms then help repair failures of that contract.

Ethical judgment also asks which consequences deserve concern. The existing proposal of 共同生成 supplies a substantive direction: non-arbitrary consideration of affected beings, including those unable to argue or reciprocate. Its fallible 良知 can bring neglected interests into view. An invariant description can serve either protective or exploitative purposes; the normative direction needs its own reasons. Its absence from a dynamics equation does not make ethical reasoning meaningless.

We should distinguish a truth about a mathematical structure, a true empirical law of a domain, and an ultimate account of reality and value. The quotient and transfer theorems establish the first. Particular applications require evidence for the second. They do not establish the third by increasing their own abstraction.

Your Maxwell analogy sets a demanding but useful target: compact substantive laws whose consequences can be derived and tested. The present work supplies a structural invariant, an exact minimality theorem, and constructive realizations. A comparable claim to a law of reality would additionally need an independently specified principle selecting and explaining actual mechanisms, with consequences that competing mechanisms would violate. No result here rules out such a deeper foundation; no reviewed result establishes it.

Our strongest justified conclusion is therefore: **we have reached an exact invariant foundation for a declared class of understanding and action, with a proved form of irreducibility. We have not yet established the most fundamental universal truth.** The outstanding issue is substantive selection and grounding of the laws and morally relevant consequences, rather than adding more components to the earlier tuple.

## Verification and sources

The accompanying [evidence record](root-of-wisdom-fundamental-evidence.json) preserves source snapshots and hashes, targeted audits, a reproducible finite verification, and the limits of each check. It distinguishes copying a source from reading it exhaustively.

The finite check covers all 5,832 systems with three states, two total interventions, and binary retained outputs. It compares partition refinement with direct enumeration of all five partitions and checks that distinct resulting classes have a finite distinguishing intervention sequence. A separate five-state chain checks all 52 partitions and a distinction requiring three successive interventions, exercising a deeper refinement than the exhaustive three-state cases. These checks support the implementation; the general minimality claim rests on the proof above. They are not a behavioral experiment or an empirical test of a universal root.

Principal cross-session sources are `full-picture-conjecture/outputs/combined-foundation.md`, `combined-process-proof.md`, and `completeness-bridge.md`; `generative-basis/FORMAL.md` and `STRUCTURAL-CLOSURE.md`; `scientific-principles/outputs/integrated-scientific-inquiry.md`; and `sin/outputs/experiment-report.md`. Earlier causal and structural reports remain part of the preserved evidence. Source workspaces were read without modification.

The mathematical approach has established precedents. Property-preserving abstraction and controller transfer are treated in [Tabuada and Pappas on Hamiltonian control systems](https://www.seas.ucla.edu/~tabuada/Papers/Hamilton.pdf) and [Reissig, Weber, and Rungger on feedback refinement](https://arxiv.org/abs/1503.03715). Those sources support the lineage and the importance of a correct interface; they do not establish our philosophical identification of the invariant with a root of wisdom. No priority claim is made.
