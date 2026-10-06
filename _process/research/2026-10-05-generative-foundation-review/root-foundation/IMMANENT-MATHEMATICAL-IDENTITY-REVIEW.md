# Review: mathematical identity under expanding situated interfaces

6 October 2026. AI-authored proof and counterexample review for the named connection **retained distinctions → compositional mathematical identity → revision as interventions and questions expand**. This applies the [project-wide nondual method](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/NONDUAL-METHOD.md). It reviews a proposed mathematical interface, not a new physical learner, empirical observation, Lean verification or proof of nondual ontology.

## 1. What is inherited, and what this review adds

[Mathematics structural results](MATHEMATICS-STRUCTURAL-RESULTS.md) already proves the canonical exact behavioral quotient (M1), factorization of exact representations (M2), the local congruence criterion (M3), finite distinguishing bounds (M4), and richer-output refinement with its canonical surjection (M7). Its three-state chain already shows that equal present outputs need not support compositional updating. These are not new findings of the present round.

[Abstraction acquisition](ABSTRACTION-ACQUISITION-MATH.md) additionally proves how an installed observation-table learner acquires suffix distinctions, repairs consistency, constructs a minimal candidate and conditionally certifies all-word correctness under a valid state bound and exact experiment interface. The actual learner need not possess the complete behavioral relation when its finite table is first formed. Its retained finite evidence and the analyst's universal response function must remain distinct.

The useful next result is the organization of exact quotients across **jointly expanding action and question interfaces**, including their directed union, finite stabilization under an additional finite-quotient hypothesis, and an obstruction to turning every compatible collection of partial descriptions into an actual state. The component arguments are elementary extensions of the inherited quotient results, with no mathematical priority claimed.

## 2. Fix the same relevant unfolding before comparing interfaces

Let an ambient deterministic process have a fixed carrier S, action set A, and total transitions δ_a:S→S for a∈A. S retains the conditions on which the claimed responses depend: retained changes, environmental conditions, resources, current access and affected organizations when relevant. A label need not name an intentional actor's choice. The process is a local mathematical representation; these choices are not declared fundamental independent substances.

For each index i in a nonempty directed poset I, let A_i⊆A be an intervention repertoire and Q_i a family of questions q:S→O_q. Directed means every finite collection of indices has a common upper bound. Require i≤j to imply A_i⊆A_j and Q_i⊆Q_j. Question names refer to the same maps at every stage, and common actions retain their transitions. This compares increasingly rich interfaces to one process; it does not silently change the process between stages.

A context is a pair (w,q), with w a finite word in A_i and q∈Q_i. Its response is

\[
R_{w,q}(s)=q(\delta^*(s,w)).
\]

Endpoint questions can include a retained record of an earlier event or a tuple of relevant consequences. Outputs at every prefix are included because every prefix is also a word. A terminal observation alone does not automatically retain every consequence experienced during a path. The chosen state and question interface must actually preserve any such consequence claimed by the application.

If an intervention is sometimes denied, an explicit totalized denied transition is usable only with its actual effects and distinguishable outcomes preserved; a denied operation does not become physically possible. A contextual response is a conditional result under that declared interface. No theorem here gives a learner simultaneous access to every context, a free reset, or resources for its execution. Forming new access is a further actual history; merely adding its label to A_i does not construct that access.

Define

\[
s\equiv_i t
\quad\Longleftrightarrow\quad
\forall w\in A_i^*\ \forall q\in Q_i,
\ R_{w,q}(s)=R_{w,q}(t).
\tag{I1}
\]

Empty Q_i yields the indiscrete relation. An empty A_i still admits the empty word and thus the present questions. All following statements cover these cases.

## 3. Refinement and canonical passage between exact abstractions

**Proposition I1.** Relation ≡_i is the coarsest equivalence preserving every q∈Q_i and stable under every δ_a with a∈A_i. The quotient B_i=S/≡_i carries well-defined questions and those actions. For i≤j there is a unique surjection

\[
\pi_{ji}:B_j\longrightarrow B_i,
\qquad [s]_j\longmapsto[s]_i,
\tag{I2}
\]

commuting with the projections from S. It preserves every action and question in interface i. The maps satisfy π_ii=id and π_ki=π_ji∘π_kj for i≤j≤k.

**Proof.** Equality of response functions is an equivalence. The empty word preserves present questions. If s≡_i t, then for a∈A_i and any (w,q), equality at the context (aw,q) gives equality at (w,q) from δ_a(s) and δ_a(t). Thus ≡_i is action-stable. Conversely any stable equivalence preserving present questions preserves them after every finite word by induction, hence is contained in ≡_i. This is the inherited M1 argument with a family of outputs. Inclusion of contexts gives ≡_j⊆≡_i, making (I2) well-defined; every class has a representative, making it onto. Its prescribed values force uniqueness, preservation and the two composition identities. ∎

The direction matters: the richer exact abstraction maps **onto the poorer one**. There is generally no converse reconstruction from an old retained class to the new one. Moreover π_ji is a homomorphism only for the common old actions; B_i need not admit any well-defined operation for a newly added action.

The inherited M2 factorization extends without change: if a retained encoding e:S→Z admits decoders for every context of interface i, then ker(e)⊆≡_i and a unique surjection e(S)→B_i sends e(s) to [s]_i. To obtain a homomorphism from an actual updating representation, one also needs its update law to commute with the physical δ_a. Response exactness alone does not install, compute or fund that update law.

**Specific revision obligation.** If s≡_i t but a new context distinguishes them, no decoder of their old common class can answer that context correctly in both cases. An implementation must acquire an additional distinction, retain previously omitted information, or narrow its claimed scope. This need not make its old answer wrong for the old interface. If the physical law itself changes, interface refinement alone is inapplicable; a common enlarged state must represent that change or a separate correspondence must be proved.

## 4. Joint contextual sufficiency and its finite case

Write A_∞=⋃_i A_i and Q_∞=⋃_i Q_i, and define ≡_∞ by all finite A_∞-words and Q_∞-questions.

**Proposition I2.**

\[
\equiv_\infty=\bigcap_{i\in I}\equiv_i.
\tag{I3}
\]

Consequently the map

\[
J:S/{\equiv_\infty}\longrightarrow\prod_{i\in I}B_i,
\qquad J([s]_\infty)=([s]_i)_{i\in I}
\tag{I4}
\]

is well-defined and injective. If the union contexts separate all distinct elements of S, then ≡_∞ is equality, and their joint profile recovers the represented state uniquely.

**Proof.** Agreement on union contexts implies agreement at every stage. Conversely fix a finite word w over A_∞ and q∈Q_∞. Each of its finitely many letters and q occurs at an index. Directedness gives a common upper bound containing all of them, so (w,q) is already a context at that stage. Agreement at all stages therefore gives agreement at this context, proving (I3). Equality of every component in (I4) is exactly (I3), proving injectivity. Pair separation is precisely the assertion that the intersection is the diagonal. ∎

Directedness has work to do. Without it, separate interfaces {a} and {b} need not contain the mixed context ab; agreement on each separate repertoire does not guarantee agreement under their compositions. Likewise mere agreement on a list of performed tests is not agreement under every context of its generated interface.

**Proposition I3.** If the final quotient S/≡_∞ has a finite number n of classes, then there is some stage i₀ with ≡_i₀=≡_∞. Every later stage has the same equivalence. No numerical deadline for reaching i₀ follows without a bound on when informative contexts enter the interface.

**Proof.** If n≤1, all ≡_i equal ≡_∞ already. Otherwise choose one representative from each of the finitely many final classes. For each pair choose a union context distinguishing them. There are at most n(n−1)/2 witnesses. Each witness lies at a stage by the proof of I2; a common upper bound i₀ contains them all. All elements of a final class agree on every union context. Hence these witnesses distinguish any two different final classes, not just the chosen representatives. Therefore ≡_i₀⊆≡_∞. The reverse inclusion always holds. Later equivalences lie between those equal relations. ∎

This does not produce a finite executable certificate when the witnesses, laws or completeness of the final scope are unknown. The finite set of witness questions need not itself be closed under action-prefixing, even though its kernel equals the complete stable relation on the stipulated S. To certify that fact from a table still requires the inherited exactness obligations. In an expanding chain there can be at most n−1 strict class refinements from a single class, but arbitrarily many uninformative stages between them.

## 5. History identity is not operation identity

Fix one interface (A,Q), initial state s₀, and its action-reachable carrier S₀. Write ≡ for its complete contextual state equivalence. The induced history equivalence

\[
h\sim h'\quad\Longleftrightarrow\quad
\delta^*(s_0,h)\equiv\delta^*(s_0,h')
\]

is stable under appending the same word. It need not be stable under prefixing a word. It therefore yields a system of reached behavioral states, not in general a quotient monoid of interchangeable operations.

**Counterexample.** Let the output say whether the entire word executed from the initial state is exactly ab. A finite deterministic machine for the language {ab} realizes this response. Histories b and aa both have empty accepting residual: no suffix can make either total word ab. Thus b∼aa. But prefix a gives ab, accepted, versus aaa, rejected. Treating their old history equality as substitutability inside arbitrary compositions would be false.

For operation identity on behavioral states, define instead

\[
u\simeq v\quad\Longleftrightarrow\quad
\forall s\in S_0,\quad
\delta^*(s,u)\equiv\delta^*(s,v).
\tag{I5}
\]

**Proposition I4.** Relation ≃ is exactly equality of the transformations induced by words on S₀/≡. It is a two-sided congruence on words. Equivalently,

\[
u\simeq v\quad\Longleftrightarrow\quad
\forall x,y\in A^*\ \forall q\in Q,
\ q(\delta^*(s_0,xuy))=q(\delta^*(s_0,xvy)).
\tag{I6}
\]

**Proof.** Action-stability of ≡ makes every word act on its quotient, so (I5) is equality of the resulting maps. For prefix x, reachability ensures δ*(s,x)∈S₀, where the hypothesis can be applied. For suffix y, action-stability carries the endpoint equivalence along y. Thus xuy≃xvy whenever u≃v, proving the two-sided property. Every reachable s is δ*(s₀,x) for some x, and ≡ compares all suffixes y and questions q; substitution gives exactly (I6). ∎

The word quotient embeds as the generated transformation monoid on S₀/≡, with chronological convention δ*_{uv}=δ*_v∘δ*_u. It identifies operations that have the same behavior on every reachable starting class. It does not identify physically different event histories, costs or effects that the declared questions omit. If those are relevant, enlarge the interface and reconsider the identity.

This distinction prevents the new contextual account from silently claiming the stronger [uniform action-word reconstruction](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/MATHEMATICAL-ROOT-FRONTIER.md#a-positive-reconstruction-of-operations). That reconstruction ranges over every deterministic action system and every action-preserving map and forces a unique word. Here one specified system may impose additional behavioral identities between different words. Their quantifier scopes differ.

## 6. Strongest counterexamples and scope checks

**C1. Present agreement is not compositional identity.** Reuse the inherited three-state chain: S={0,1,2}, a sends 0↦1↦2↦2, and q=(0,0,1). Present questions merge 0 and 1, but applying a separates their q-answers. Thus the kernel of an arbitrary current observation is not necessarily a transition congruence. Closing the question under actual action contexts supplies the required criterion; calling an arbitrary label “meaning” does not.

**C2. New interventions can require new distinctions without any new present question.** Use the same state set, question and a-transition, with ambient actions {e,a} and δ_e=id_S. The old repertoire {e} has quotient {{0,1},{2}}. Expand it to {e,a} while keeping q fixed. Now all three states are distinguished. There can be no a-update on the old quotient commuting with the original dynamics: the old common class of 0 and 1 would have to map both to that class and to {2}. This is the action-expansion part not supplied by richer-output M7 alone.

**C3. Pair-separating partial descriptions do not realize every compatible limit.** Let S=ℕ, with only the identity action, and let stage k≥1 contain q_1,…,q_k where q_j(n)=min(n,j). Its quotient is represented by {0,…,k}; value k is the whole tail n≥k. Later-to-earlier maps are truncations min(m,k). These contexts jointly separate all natural numbers, so I2 recovers each represented state uniquely. Nevertheless the compatible profile whose kth component is k has no preimage in ℕ: it would require n≥k for every k. Thus J is not generally onto even the subset of tuples satisfying every compatibility equation. An ideal completed state or infinite element would be additional mathematical content. This is a formal representation counterexample, not evidence that generative reality lacks limits or infinite structures.

**C4. Omitting another center preserves only the reduced question.** If S retains a recipient's ongoing organization but Q_i asks only for an actor's current display, the quotient may merge states with different recipient continuations. This does not make those differences unreal or ontologically external. It limits the abstraction's question coverage. Conversely merely adding a freely chosen “recipient significance” label does not establish a genuine generative relationship. A proposed new question needs identification through the actual condition and its continuations, with independently specified rival tests.

**C5. An analyst's complete profile is not an acquired record.** I2 quantifies over contexts no finite learner may have executed. The prior observation-table construction supplies one conditional acquisition bridge with an explicit bound, reset and experiment interface. The present theorem neither removes those conditions nor generalizes that construction to arbitrary directed systems, unavailable interventions or infinite storage.

## 7. Nondual interpretation and remaining proof obligations

The positive connection is that the same activity can differentiate a retained record, the effects its future use preserves, and the contexts that test it. Compositional identity concerns substitutability in those actual modeled relationships. It need not be an externally conferred label. A model can omit such a relationship; that omission is not a demonstration that the relationship lies outside generative reality.

The mathematical propositions do not make an arbitrary family Q_i faithful by definition. Nor does the word “accessible” prove that a whole-word experiment is available from every state: changing resources, guards and the instrument's own effects belong in the relevant state and transition law. The whole-episode account should state which questions preserve the formed record's provenance, its use, changed conditions and the consequences for each relevant center. No universal positive cost, market exchange or fixed scalar success score is assumed by these propositions.

The strongest remaining objections are concrete:

1. **Context selection:** why are these actions, substitutions and questions the appropriate scope of the mathematical identity claim? If a target-relevant continuation distinguishes merged states, the claimed exactness is false for that larger target. If the expanded context changes the target itself, say so rather than treating it as a simple refutation of the old local abstraction.
2. **Formation and authority:** what actual history forms, retains and revises the interpreter and its access? This is an explanatory obligation within generative activity, not a demand for an external meaning-giver. An analyst's derivative closure does not perform that history.
3. **Changes of domain:** comparisons above retain one carrier and common laws. A construction introducing new kinds of states, objects, operations or quantification requires explicit embeddings or correspondence and preservation proofs. Canonical surjections on a fixed carrier cannot silently justify such enlargement.
4. **Mathematical necessity:** contextual identity supplies conditional exactness and canonical quotients; it does not prove that the root uniquely selects all intended realization classes, identity criteria, quantifier ranges or closure principles. The [frontier reconstruction and Beth/diagonal results](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/MATHEMATICAL-ROOT-FRONTIER.md) retain their precise scopes. A rival to the richer constitutive proposal must preserve the claimed independently specified relationship or show a genuine misdescription, rather than toggle a detached predicate in a weaker reduct.

Acceptance should therefore state the result as **exact mathematical identity, refinement and joint recovery relative to a consequence-preserving contextual interface**. The word “full” means the declared carrier and union interface, not all reality. The next stronger empirical or mechanistic contribution would show how relevant contexts become available and alter the retained distinction within one continuing history, while the next foundational contribution would justify their scope and necessity. Neither is supplied by the quotient theorem alone.

## 8. Independent acceptance of the completed synthesis and finite checker

This reviewer subsequently read the complete [separately authored mathematical note](IMMANENT-MATHEMATICAL-IDENTITY-MATH.md), the [canonical synthesis](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/IMMANENT-MATHEMATICAL-IDENTITY.md), and the finite package's [protocol](../../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/identity/PROTOCOL.md), [checker source](../../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/identity/check.py) and [saved result](../../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/identity/results.json). This is independent AI-assisted internal review of different authors' work, not human peer review. The review did not rerun the finite enumeration or any earlier scientific experiment.

**Mathematical acceptance.** The separate note's I1–I8 are accepted at their stated scopes. Its partial-action extension explicitly distinguishes undefinedness from every defined answer, including when the question family is empty. This supports the claimed domain-preserving congruence and projection. Its two-sided operation proof correctly treats undefined prefixes and quantifies over all reachable starts; state residual equality is not substituted for operation equality. Directedness supplies a common stage for the finitely many letters in each word, and the union-question proof then handles each coordinate. The inverse-limit condition is exactly simultaneous realization of the compatible class fibers. Compactness plus closed fibers and finite final quotient are two correctly distinct sufficient routes. The finite-support sequence example uses coordinate flips, so it does not accidentally reveal unobserved future coordinates through a shift action.

One precision was requested and repaired before acceptance: I8 now requires a **nonempty** class of faithful realizations. Without that requirement, validity in every member of an empty class would be vacuous and would not imply validity in the comparison structure. The pointwise isomorphism transport argument itself was correct. The uniform finite bound corollary in I7 also passes: N+1 distinct final classes would require a stage separating their finitely many pairs, contradicting the bound N. Stabilization concerns equivalence classes, not a final inventory of actions, known deadline or acquired stopping certificate.

**Canonical acceptance.** The synthesis preserves the distinction between new evidence within the old scope, expansion of scope, and an actual change of process law. It expressly declines to induce a newly accessible action on a coarse quotient when congruence fails. It separates one-system equations from the earlier all-systems unique-word result, and contextual state identity from two-sided operation identity. Its infinite-tail example claims only the failure of automatic realization in the declared carrier; it does not refute immanent constitution by toggling a detached semantic label. No unconditional mathematical necessity or universal ontology is claimed.

The synthesis credits the actual earlier acquisition and method-formation histories, instead of claiming the finite checker forms a learner. The cited acquisition account independently records a retained three-state model followed by a five-action word absent from its observed words of length zero through four, and an actual packet transfer. The text correctly limits this model to the stationary phase/readiness projection. It does not identify its resource-consuming apparatus with a stationary three-state machine, splice it into the distinct core/tree episode as one proved physical successor, or promote local payment vocabulary to a generative primitive. Supplied recipes are unresolved dependencies of local explanations, not thereby external to generative reality.

**Finite checker acceptance.** The protocol's exhaustive family size follows independently from the formula (n+1)^(2n)·2^n: each of the 2n action entries has n successor choices plus undefinedness, and the n states have Boolean outputs. This gives 8, 324 and 32,768, totaling **33,100 processes** and **99,300 two-algorithm comparisons** across three interfaces. The saved counts of strict refinements are **9,736 action refinements** and **5,202 question refinements**; this review checked how the code counts them and their saved values, without independently recomputing those two aggregate numbers.

The descending-relation algorithm and the separate pair-search algorithm correctly detect both answer disagreement and unequal action domains. Exhaustive partitions test the greatest-congruence characterization, while each interface's congruence and the class map validate preservation under common actions. The saved new-action witness is genuine: the first action is undefined at both states and the old outputs are equal, so the old interface merges them; the second action is undefined at state 0 and reaches state 0 from state 1, so it cannot descend to that merged class. The separate recognizer reaches the same dead state after b and aa while its prefixed outputs are 1 and 0. The min(n,k) loop is correctly labeled a finite illustration, not a computational proof of the infinite intersection claim. The saved SHA-256 bindings match the inspected checker and protocol bytes.

No outstanding proof or canonical-scope correction remains after the nonempty-class repair. The contextual choices, actual formation of access, correspondence of questions to relevant consequences, and stronger selection of mathematical realization/closure conditions remain the stated explanatory work; neither this acceptance nor the enumeration discharges them.
