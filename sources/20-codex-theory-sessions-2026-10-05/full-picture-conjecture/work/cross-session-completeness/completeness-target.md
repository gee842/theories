# A defensible completeness target for a general theory of generation

Research note, 5 October 2026. This evaluates a theory intended to explain both successful and failed continuation. It does not substitute a demand that everything must continue.

## 1. Correcting the target

A general theory can be complete for an explicitly declared class of questions while permitting termination, repetition, injury, failed repair, ignorance, and exhausted possibilities. Explaining those outcomes is part of its task. It need not prove inexhaustible novelty, derive one unique physical mechanism, compel every moral opponent, or compute the answer to every possible instance.

The previous full-root audit correctly blocks particular stronger inferences: representation alone does not imply universal nontermination; the specified Wen motion does not produce infinitely many distinct field configurations; and no total exact algorithm solves every unrestricted computable continuation problem. **Those results do not, by themselves, show that a general success-and-failure theory is incomplete.** Using them as requirements for the latter would impose a stronger target than necessary.

Nor is using supplied mechanisms automatically a defect. General theories routinely state laws and exact relationships in terms of systems, inputs, objectives, and boundary conditions. A representation-independent characterization of what can be achieved may itself be the intended result. Whether it is mathematically novel, empirically useful, or a complete physical ontology is a different assessment. Agreement with a conventional model given the same information does not invalidate completeness: two equivalent formalisms should agree. A claim of superior prediction, explanatory economy, or a distinctive new empirical law needs its own evidence, but such superiority is not a logical prerequisite for relative completeness.

The useful target is:

> For every system in a declared domain and every declared generative objective, the theory represents the relevant situation without changing the actor's information or implementation possibilities, and characterizes exactly when that objective is attainable and when it is not.

This is relative completeness: relative to a domain, questions, interpretation, and admissible-controller standard. “Relative” states what is covered; it does not mean approximate or unreliable inside that coverage.

## 2. The policy correspondence theorem

Let \(M\) be a concrete model and \(E\) its representation. Their policies must already satisfy their respective observation, timing, resource, authorization, and implementation restrictions. In particular, a policy is one causal rule for the actor's available history, not a separate action selected with knowledge of the hidden situation.

Interpret completed runs of both models in a common semantic trace space \(\mathcal T\). Let

\[
L_M(\pi)\subseteq\mathcal T,
\qquad L_E(\sigma)\subseteq\mathcal T
\]

be all allowed traces of a policy, including the allowed initial uncertainty and environmental consequences. Deadlock and finite termination must be represented explicitly, rather than deleted so that a universal guarantee becomes vacuous. The trace interpretation retains exactly the events, protection labels, timing, costs, or novelty distinctions relevant to the declared objectives.

For a trace objective \(\Omega\subseteq\mathcal T\), define sure attainability by

\[
\operatorname{Win}_M(\Omega)
\iff \exists\pi\in\Pi_M:\ L_M(\pi)\subseteq\Omega.
\]

The following two contracts are sufficient for exact transfer:

\[
\tag{S}
\forall\sigma\in\Pi_E\ \exists\pi\in\Pi_M:
L_M(\pi)\subseteq L_E(\sigma),
\]

\[
\tag{C}
\forall\pi\in\Pi_M\ \exists\sigma\in\Pi_E:
L_E(\sigma)\subseteq L_M(\pi).
\]

The quantifier order is essential. One transferred policy must work for all its allowed consequences. The transfer must not choose different concrete policies after discovering which hidden state or future disturbance occurs.

**Theorem.** If (S) and (C) hold, then for every trace objective,

\[
\boxed{\operatorname{Win}_M(\Omega)
\iff\operatorname{Win}_E(\Omega).}
\]

**Proof.** If \(\sigma\) wins in \(E\), (S) gives an admissible \(\pi\) with
\(L_M(\pi)\subseteq L_E(\sigma)\subseteq\Omega\), so \(M\) wins. Conversely, if \(\pi\) wins in \(M\), (C) gives \(\sigma\) with
\(L_E(\sigma)\subseteq L_M(\pi)\subseteq\Omega\), so \(E\) wins. \(\square\)

There is also an exact converse when the objective family is **all** subsets of \(\mathcal T\). Suppose winning equivalence holds for all such objectives. For any \(\sigma\), take \(\Omega=L_E(\sigma)\). The represented model wins this objective, hence the concrete model has a policy satisfying (S). Taking \(\Omega=L_M(\pi)\) similarly proves (C). Thus these contracts characterize equality of attainable sure guarantees over the full objective family. For a smaller family such as safety and recurring progress, the contracts remain sufficient but need not be necessary.

This is an elementary semantic criterion, not a claim of a new theorem in control theory. The importance of respecting the controller's available information is established in the refinement literature; see [Reissig, Weber, and Rungger](https://arxiv.org/pdf/1503.03715). Our two-sided criterion explicitly adds the reverse obligation needed to preserve impossibility as well as possibility.

### Why a forward guarantee is insufficient

Let the concrete model have a policy with outcome set \(\{g\}\), while the representation offers only a policy with outcome set \(\{g,b\}\). Contract (S) holds. For objective \(\{g\}\), the concrete model wins and the representation loses. The abstraction is conservative and sound for positive guarantees, but incomplete.

Likewise, an injective state encoding is insufficient if it reveals hidden information. In two hidden situations requiring opposite actions, a fully revealing encoding allows a winning choice that the original actor cannot make. State representability does not itself establish a controller correspondence.

### Composition

Suppose \(M\), \(E\), and \(F\) share the same semantic trace interpretation, and each adjacent pair satisfies (S) and (C). For any policy in \(F\), use (S) first to obtain a policy in \(E\), then one in \(M\); the two trace inclusions compose. Starting with any policy in \(M\), the two (C) transfers compose in the other direction. Therefore \(M\) and \(F\) have identical attainable sure guarantees.

When actual causal transfer functions are supplied, compose those functions. The logical existence theorem alone does not establish a computable, affordable, or physically realizable adapter. Those requirements belong to the policy classes and transfer implementation contract.

## 3. Representation plus an exact solver yields relative completeness

Let \(\mathcal D\) be a declared model class and \(\Gamma(M)\) its objective family. Suppose:

1. Every \(M\in\mathcal D\) has a constructed representation \(E(M)\), with independently specified trace interpretation and objective translation.
2. The two admissible-policy contracts hold for each representation.
3. A characterization \(C(E,\Omega)\) is proved equivalent to winning in the represented model for every relevant objective.

Then

\[
\forall M\in\mathcal D\ \forall\Omega\in\Gamma(M):
C(E(M),\Omega)\iff\operatorname{Win}_M(\Omega).
\]

This is a compositional completeness result. If \(C\) is also an effective exact algorithm on the domain, it supplies an exact decision method there. If \(C\) is an implicit set-theoretic characterization, the conclusion is semantic completeness without an algorithmic guarantee. The earlier undecidability result limits the latter upgrade on unrestricted computable domains, not this semantic equivalence.

The representation and its contracts must be independently constructed or proved from local semantics. Defining \(E(M)\) by first assuming the desired winning answer would make the proposed method circular. Similarly, a theorem that assumes the missing semantic-preservation witness is a valid interface theorem, but does not discharge the coverage obligation for classes where that witness remains unconstructed.

## 4. A finite-domain bridge can be proved completely

For finite controlled transition models, the representation part has a direct construction.

Take a finite state set \(S\), finite observation and action alphabets, a state-observation map, a feasible-action relation, possible-successor sets, and specified initial uncertainty. Encode the states, observations, and actions by injective fixed-length binary words. Use only the code images as model carriers. Transport the feasible-action relation and successor table through the encodings, and encode observations through their own observation map. In particular, the observer receives the code of its original observation, not the code of the hidden state.

Encode a policy by decoding its observation/action history, applying the original policy, and encoding the resulting action. Decode a represented policy by the reverse procedure. Legal histories correspond by induction on their length; the possible next observations and actions correspond at each step. Infinite plays correspond by the same pointwise encoding, while finite maximal plays retain their terminal status. Consequently, corresponding policies have exactly equal interpreted trace sets in both directions.

Thus (S) and (C) both hold. This proof does not require that all processes succeed or have novel states: failures, cycles, and deadlocks are encoded equally faithfully.

Combining this encoding with the previously proved finite partial-observation safety and recurring-progress characterizations gives:

> Every finite model of that declared class has a binary representation preserving observation-consistent attainability and failure for safety and recurring-progress objectives, with a finite exact certificate/decision procedure supplied by the earlier constructions.

This is a completed mathematical bridge at that scope. It is not a new Lean certification, and it does not establish that every real process has a finite adequate model. Binary encoding also does not prove zero implementation overhead on physical hardware: if encoding, sensing, memory, or computation consumes consequential resources, those costs must be included in the original model or separately bounded.

The broader R-family representation programme may supply richer bridges. Its general object/operation representation result should be connected to this policy-and-objective contract explicitly rather than assumed to imply it from names or graph ancestry.

## 4A. An existing cross-session result already supplies a stronger bridge

The newly inspected generative-basis study contains more than an unrestricted encoding claim. Its [structural closure theorem](/Users/ren/theories/experiments/integrated-correction/general-framework/generative-basis/formal/STRUCTURAL-CLOSURE.md) derives a sufficient state boundary from supplied local mechanisms. Its [formal note](/Users/ren/theories/experiments/integrated-correction/general-framework/generative-basis/formal/FORMAL.md) supplies an exact quotient test, a coarsest faithful partition, controlled composition rules, and a finite rational-kernel compiler. These results should count toward the completeness assessment; treating their entire bridge as absent would be inaccurate.

The next proposition explicitly connects those results to this session's finite safety and recurring-progress characterization. It closes the mathematical interface between them at a declared scope.

### Finite quotient-to-controller completeness

Fix a nonempty finite state set \(S\), finite controller actions \(U\), finite boundary inputs \(D\), and rational stochastic transition kernels \(P_{u,d}(s,t)\). Include finite event monitors in \(S\) when needed. There is one centralized decision maker with its **specified possibly partial observation** \(o(s)\), using a deterministic causal policy. Admissible actions and boundary inputs must obey the same permissions in both models. For the finite decision theorem, boundary inputs range adversarially over every declared allowed choice, or a supplied finite boundary process is included in the state. An endogenous boundary process with additional hidden dependencies must itself be included in the model. Transfer also holds for the same externally fixed input sequence, but an arbitrary nonperiodic infinite sequence does not by itself supply a finite model for the decision algorithm.

Let \(q:S\twoheadrightarrow Q\) preserve the protected label, progress label, the actor's observation, and the relevant action/input permissions. Suppose that for every permitted \((u,d)\), every \(s\in S\), and \(b\in Q\),

\[
\tag{L}
\sum_{t:q(t)=b}P_{u,d}(s,t)
=\bar P_{u,d}(q(s),b).
\]

The structural-closure result supplies (L) for its declared common-noise circuit class when the seeds include these labels, observations, and permission tests. Alternatively, the partition-refinement construction supplies it directly from the finite kernels. Set the quotient actor's observation to \(\bar o(q(s))=o(s)\); **do not reveal \(q(s)\) itself to the actor** unless the original observation already reveals it.

Interpret “sure” literally as every path made of positive-probability transition edges and every declared adversarial input choice. This includes infinite paths whose individual probability is zero. Equality of probability-one guarantees must not be silently substituted for this objective.

**Support lifting.** For every fine state \(s\), permitted input pair, and quotient block \(b\),

\[
\bar P_{u,d}(q(s),b)>0
\iff
\exists t\in S:\ q(t)=b\ \land\ P_{u,d}(s,t)>0.
\]

This follows from (L): a finite sum of nonnegative terms is positive exactly when at least one term is positive. Crucially, it holds for **each fine state** in the source block, rather than merely for some representative.

Fix a policy using only the declared observation history and its own action history/memory, and use that same policy in the quotient. Every fine support path projects to a quotient support path. Conversely, take a quotient support path, its input sequence, and any fine initial state in the corresponding permitted initial block. At each step the lifting equivalence supplies a positive-probability fine successor in the required next block. Choosing the first such successor in a fixed enumeration of \(S\) recursively constructs an infinite lift. Corresponding observations and permissions agree at every step, so the policy chooses the same controller action throughout. The lift requires no extra information in the controller: it is an existence proof for possible environment paths, not a new control rule.

With initial uncertainty \(B_0\subseteq S\), use \(q(B_0)\) in the quotient. A quotient path starts in some \(q(s_0)\) with \(s_0\in B_0\), and the preceding construction lifts it from that state. Thus the fine and quotient models have exactly the same retained **support-path sets under each admissible observation-based policy**. Finite deadlocks must retain their terminal status through the permission contract; they cannot be discarded.

It follows that (S) and (C) hold here with equality of retained trace sets. Therefore, for any initial uncertainty and retained safe/progress labels,

\[
\boxed{\begin{aligned}
&\text{an observation-based policy surely preserves safety and visits progress infinitely often in }M\\
&\quad\iff\text{such a policy exists in its faithful quotient }E(M).
\end{aligned}}
\]

The preceding safety-only equivalence also follows. The finite imperfect-information constructions in `continuation-proof.md` and `progress-proof.md` then give an exact decision and certificate for this stated class. A losing result means no policy with that same information and execution contract attains the sure objective; it does not mean that every stochastic run fails or that no probability-one policy exists.

### Composed result already supported by the research

For supplied finite rational mechanisms in this class, the combined construction is:

1. Expand retained event monitors and include protection, progress, observations, and permissions in the question.
2. Derive a sufficient boundary by dependency closure when the structural hypotheses hold, or compute a faithful partition directly from the full finite kernels.
3. Preserve the participant's actual observation map and use the support-lifting result above.
4. Apply the finite safety/recurring-progress construction to obtain an exact answer, a winning controller when possible, and the corresponding obstruction when impossible.
5. If a finite generating program is desired, apply the rational-kernel compiler at its declared macrostep interface.

The compiler's branch probabilities remain supplied mechanism parameters. Its exact kernel preservation and the same support argument preserve the declared macrostep objectives; intermediate observations, harms, timing, instruction costs, and permissions must be modeled if they matter. The procedure need not produce compression, a pleasant outcome, or a globally inexhaustible process to be complete for its stated questions.

This result establishes **finite relative completeness for representation, reduction, and sure safety/recurring-progress attainability under the checked interface**. It is stronger than saying that a bridge is merely conceivable. It is still narrower than a complete algorithm for arbitrary decentralized information structures, arbitrary infinite-state models, every probabilistic objective, or all empirical mechanisms. The source's path-law theorem can preserve a specified decentralized policy profile, but that fact alone does not supply a complete decentralized synthesis algorithm.

## 5. How the other sessions change the completeness assessment

The saved [missing-possibilities synthesis](/Users/ren/Documents/Codex/2026-10-05/root-of-wisdom/outputs/noticing-missing-possibilities.md) supplies a bounded constructive route from records to previously unused conditional policies. It distinguishes the current working model, the candidate language, and available experience. Its four-attribute example shows that exhaustive evaluation of the original 73 candidates can still omit a useful policy; expanding the composition grammar removes that particular omission.

In the theorem above, such a restricted grammar can fail (C): a successful source policy has no represented admissible counterpart. Inaccessible or unlinked observations can instead prevent an epistemic transfer or identification claim. These are different failures. A syntax capable of representing the useful policy does not ensure that the inquirer will construct, test, select, fund, and enact it.

The [scientific-change formal results](/Users/ren/Documents/Codex/2026-10-05/scientific-principles/outputs/scientific-change-formal-results.md) add a second useful distinction. A policy language may contain a valuable full interaction while a rule requiring strict improvement at every intermediate expansion prevents reaching it. This is a restriction on the allowed discovery procedure, not necessarily on the underlying language's expressive coverage. Treat the discovery procedure as part of the controlled system when the question concerns effective inquiry. Its result then depends on the declared protocol budget, deadline, capabilities, and admission rules.

These results narrow the gap rather than certify that no gap remains. They provide specific candidate-generation, observation, revision, and validation mechanisms. They do not claim enumeration of every meaningful concept or automatic adequacy for all future questions. Requiring that unlimited guarantee would again exceed the scoped constructive claims.

## 6. Concrete completion obligations

The general success-and-failure theory needs an explicit ledger for the following obligations:

| Obligation | What closes it |
| --- | --- |
| Domain | An independently described class of processes, including failure cases, rather than “the processes where the theory works.” |
| Questions | A declared objective family: safety, recurring progress, specified novelty, costs, or others, kept distinct. |
| Observation and execution | Actors' information and realizable policy classes specified without giving them hidden knowledge or free resources. |
| Representation | A construction for every domain member, with faithful traces and objective interpretation. |
| Two-way strategy coverage | Both contracts, or weaker sufficient contracts proved for the restricted objective family. |
| Characterization | A theorem computing or semantically characterizing both attainability and nonattainability. |
| Composition | Verified preservation when mechanisms, observers, resource accounts, and learning procedures are combined. |
| Application | Evidence that a concrete empirical situation falls within the model and interpretation contract at the accuracy claimed. |

For stochastic expected-loss or chance-constrained questions, possible-trace sets alone are insufficient. The correspondence must also preserve the relevant probabilities or attainable outcome laws. A sufficient analogue is equality of the sets of attainable probability measures under admissible policies, with matching objective functionals. That transfers every declared functional and its attainable values; a sure-winning theorem alone must not be claimed to do this.

Public normative commitments can specify the protection objective openly. A complete conditional account of means does not require deriving that commitment from bare motion. A stronger claim that the commitment is uniquely justified remains a separate philosophical obligation, not an implicit prerequisite for all operational completeness.

## Determination

The reports already establish exact success-and-failure results for substantial declared finite classes. The newly inspected cross-session generative-basis results supply constructive structural closure, exact finite reduction, and rational-kernel generation. The support-lifting theorem above completes their explicit interface with this session's finite observation-based safety and recurring-progress constructions. That is a defensible sense in which a part of the general theory is complete.

The reviewed materials do not yet certify coverage of every intended real process and every intended objective. The missing work should be stated as specific domain, strategy, objective, composition, and application obligations. Universal nontermination, endlessly novel configurations, unique physical dynamics, and universal moral agreement should not be demanded unless those are separately retained claims of the theory.
