# 慧根 as an entire generative theory: necessity of the root and all descendants

6 October 2026. AI-authored constructive continuation of Ren's stronger request: pursue an entire necessary generative core capable of extending into indefinitely many insights, rather than stopping at compatibility with selected conditions. Here 慧根 names Ren's proposed philosophical root; it is not asserted to be the historical meaning of every use of that term. The named connection is **necessary generative conditions → a premise-preserving generator → necessity of the entire generated theory → materially realized inquiry and judgment**.

**New result:** we now have a kernel-checked theorem covering the whole generated theory at once:

\[
\boxed{\text{Every generated descendant is necessary for inquiry}
\quad\Longleftrightarrow\quad
\text{Every starting premise is necessary for inquiry}.}
\tag{H1}
\]

The equivalence applies to the explicit truth-preserving rules below, with local assumptions retained. It is not a certification of the present philosophical root's necessity. It makes that larger target precise and reduces its unbounded downstream obligation to identifiable starting commitments and rules. The package also checks genuinely different, arbitrarily indexed information and support constraints, using the repository's actual process/trace definitions. This gives a constructive example of a finite generative core whose operational consequences have no fixed finite upper index.

The [formal package](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/README.md) passes **27 new declaration audits**, alongside **23 rebuilt inherited declarations**, in a fresh Lean 4.29.1 build. The claims proved, imported hypotheses and philosophical work remaining are separated below.

## 1. What this adds to the earlier 慧根 work

The preserved [root-of-wisdom synthesis](../../../../sources/20-codex-theory-sessions-2026-10-05/root-of-wisdom/outputs/root-of-wisdom-synthesis.md#formal-limits-without-exaggerated-conclusions) already explains that a finite rule can admit unbounded extension. It also gives the established result that a uniformly effective nested sequence of sound arithmetic theories has a sound, effectively enumerable and still incomplete union. The [research ledger, R1–R5](../../../../sources/20-codex-theory-sessions-2026-10-05/root-of-wisdom/outputs/research-ledger.md#claim-register) already separates unbounded extension, represented distinctions, common policies and ethical purpose. We inherit those results rather than rename them as new discoveries.

That earlier work answers whether sound extension is possible and why it need not become complete. The present question is different: **if the starting conditions are necessary for scientific inquiry, does that necessity extend to the whole theory they generate?** H1 answers yes for the checked generator, and its reverse direction makes the remaining burden exact. Productive generation cannot make an unsupported starting premise necessary, because that premise is itself a member of the generated theory.

The philosophical ambition is therefore neither incoherent nor answered merely by saying that each example is conditional. A whole indefinitely extensible theory can inherit necessity. We must identify the root that deserves that status, keep the actual dependencies of its descendants, and distinguish its sound generated conclusions from hypotheses merely proposed by an intelligent process.

## 2. Precise objects: root, inquiry and generation

Let \(W\) be a declared class of interpreted situations, and let \(I(w)\) mean that the independently specified inquiry capability occurs in situation \(w\). The criterion \(I\) is supplied before the necessity argument; it is not defined as agreement with our theory. A formula is a predicate on \(W\). A root is a family of formulas \(B_i\), indexed by \(i\).

Define

\[
\operatorname{Nec}_I(p)\;\Longleftrightarrow\;
\forall w\,[I(w)\Rightarrow p(w)].
\tag{H2}
\]

For any nonempty intended inquiry class, this says that every actual realization of the capability satisfies the condition. The formal equivalence remains valid for an empty class, but would then be vacuous and establish no substantive scientific necessity. A real application must identify at least one realization and the relevant alternatives.

The checked judgment \(B;\Gamma\vdash p\) records a **finite proof** of \(p\) from the root and the finite list of local hypotheses \(\Gamma\). Its eight constructors are:

1. use a named root premise;
2. use a named local hypothesis;
3. introduce an implication by discharging its antecedent;
4. apply an implication to its antecedent;
5. combine two established claims by conjunction;
6. extract the left conjunct;
7. extract the right conjunct;
8. instantiate an already established universally quantified natural-number claim at one particular natural number.

These are explicit rules of a small calculus, not a proposal to reduce all discovery to eight conscious human operations. The formulas have a semantic interpretation, and soundness is checked relative to that interpretation. The file does not supply a parser, a complete proof search, a universal estimator, or a method for deciding every true statement.

The **entire generated theory** is

\[
\operatorname{Gen}(B)=\{p:B;\varnothing\vdash p\}.
\tag{H3}
\]

There is no maximum proof depth in this definition. Every particular proof is finite. An unbounded family of possible finite derivations is different from one physically completed infinite computation. Universally quantified formulas can be supplied and instantiated without an infinite list of separate root premises; Section 5 implements this with precisely two such formulas.

## 3. The whole-theory necessity theorem

**H3a — Soundness with premises.** For every proof \(B;\Gamma\vdash p\), every situation satisfying all \(B_i\) and every member of \(\Gamma\) satisfies \(p\).

**Proof.** Induct on the finite proof tree. The first two cases read the appropriate assumption. Implication introduction evaluates its subproof with the added antecedent; implication application uses both established inputs. Conjunction formation and extraction preserve truth. Universal instantiation uses the established universal claim at its specified index. No case removes a hypothesis except by making it the antecedent of an implication. ∎

**H3b — Entire necessity, in both directions.**

\[
\bigl[\forall p\in\operatorname{Gen}(B),\operatorname{Nec}_I(p)\bigr]
\Longleftrightarrow
\bigl[\forall i,\operatorname{Nec}_I(B_i)\bigr].
\tag{H4}
\]

**Proof.** From right to left, every situation realizing \(I\) satisfies the root, and H3a applies to every closed proof. The proof length is arbitrary, so one argument covers the whole generated theory. From left to right, each \(B_i\) has the one-step closed proof that reads it from the root. Necessity of the entire theory therefore includes necessity of every starting premise. ∎

This is the constructive form of “whatever the root generates, science cannot contradict,” when *generates* means this sound, premise-preserving derivation and *science* means a correct account under the same independently identified interpretation. A contradicting empirical claim does not defeat a mathematical implication merely by being labeled scientific. Nor may we dismiss a contrary observation: it can show that the proposed root, application assumptions, measurement or interpretation was wrong. If a purported realization truly violates a claimed necessary root premise, H4 requires revising that root; no longer descendant proof can repair it.

**H3c — Local premise preservation.** If every root premise is necessary and \(B;\Gamma\vdash p\), then

\[
\operatorname{Nec}_I\bigl((\bigwedge\Gamma)\Rightarrow p\bigr).
\tag{H5}
\]

Only if every local hypothesis is also independently necessary on the claimed inquiry class can the conclusion be promoted to \(\operatorname{Nec}_I(p)\). Alternatively, a local hypothesis can be established for an actual particular situation, giving a justified application there rather than a universal necessary fact. The formal context is a list with an explicit length; it is an upper bound on the declared local premise count, not a theorem that every listed premise is irredundant.

**H3d — Generation can build reusable generators.** A closed derived lemma can be added as a reusable premise, and every subsequent closed descendant remains necessary. This is checked by proving the enlarged basis necessary and applying H4 again. Thus proved results can become tools for further proof construction. The theorem covers this increase in the available rules without requiring every future proof to be written out in advance. It does not authorize a new empirical premise or a new norm merely because a learning process proposes it.

The logic of these arguments is established proof theory. The contribution is a checked necessity-propagation interface tied to this repository's explicit generative constraints and current whole-root claim, not a claim of priority for deductive soundness.

## 4. The negative witness shows why the local-premise boundary is substantive

Take two interpreted worlds, \(w=\mathrm{false}\) and \(w=\mathrm{true}\). Let inquiry occur in both, and let the one root premise be true in both. Let a further claim \(E(w)\) assert \(w=\mathrm{true}\).

The checker establishes all four facts:

- \(B;[E]\vdash E\): the claim follows with exactly one declared local premise.
- \(B;\varnothing\vdash E\Rightarrow E\): discharging that premise yields a sound conditional.
- \(E\) is not necessary for this inquiry class: the false world is a counterexample.
- \(B;\varnothing\nvdash E\): the whole sound generated theory cannot contain the unsupported unconditional claim.

This is not a objection to generative closure. It identifies the precise invalid step that would corrupt it: converting a conditional descendant into an unconditional root truth. A response recipe, sensor calibration, positive ethical anchor or historical regularity occupies this logical place when it has been supplied without a necessity argument. Keeping it in the antecedent lets the full conditional result belong to the sound theory; erasing it does not.

Likewise, causally generating a belief is different from generating a warranted theorem. Both true and false records can be physically produced. Causal efficacy explains why a token appears and matters; sound derivation explains why its interpreted content follows. A generative foundation must explain their relation without identifying them by definition.

## 5. A finite core with unbounded, operationally different descendants

The formal package instantiates the abstract result with informative constraints rather than only logical identities.

### 5.1 An exact family of observation limits

Let an unresolved hidden state be a natural number \(x\). An observation interface of capacity \(n\) reports

\[
o_n(x)=\min(x,n).
\tag{H6}
\]

It retains exact values below \(n\) and merges all values at least \(n\). The question at threshold \(k\) is whether \(x\le k\). Let \(Q_k(n)\) mean that **one common Boolean decoder** of \(o_n(x)\) answers this question correctly for every hidden \(x\).

The kernel-checked exact characterization is

\[
\boxed{Q_k(n)\Longleftrightarrow k<n.}
\tag{H7}
\]

If \(k<n\), the explicit decoder answers whether the reported value is at most \(k\). If \(n\le k\), hidden states \(k\) and \(k+1\) have identical report \(n\) and opposite correct answers, so no common decoder succeeds. This is the earlier representation-fiber obstruction made constructive for an unbounded family; it does not claim a new general information theorem.

For every \(k<l\), the capacity \(n=k+1\) answers threshold \(k\) but cannot answer threshold \(l\). The corresponding capability sets are therefore pairwise different. These are not infinitely many cosmetic rewritings of one particular answer: distinct interface capacities change which distinct questions can be resolved. The sufficiency decoder is given explicitly, although material construction, execution time and installation still require their actual laws.

### 5.2 An exact family of support limits on the existing process core

The new spending process uses the inherited [GenerativeCore](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/GenerativeCore.lean) definition, with natural fuel state and the declared event law \(s=t+1\): every event consumes one unit. For every actual action word \(a\),

\[
\operatorname{Trace}(s,a,t)\Longleftrightarrow s=t+|a|,
\qquad
\operatorname{Feasible}(b,a)\Longleftrightarrow |a|\le b.
\tag{H8}
\]

The necessity direction invokes the existing [Depletion](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/Depletion.lean) trace bound; the new sufficiency argument constructs the remaining stock. At every budget \(b\), a \(b\)-event history is feasible and a \(b+1\)-event history is excluded. Again there is no fixed largest index, and different horizons demand different actual reserves.

The unit spending law is a supplied realization. The theorem does not conclude that every thought costs one unit, that every process depletes, or that no physical process can renew itself. Those would contradict the supplied scope. The universal descendant is the implication from that law and trace claim to its resource restriction.

### 5.3 The whole generated local theory

A scenario contains capacity, query threshold, fuel and horizon. The package supplies exactly **two quantified root formulas** for this declared interface class:

\[
B_0:\ \forall k,\ Q_k(n)\Rightarrow k<n;
\qquad
B_1:\ \forall m,\ \operatorname{Feasible}(b,m)\Rightarrow m\le b.
\tag{H9}
\]

Both are proved, rather than introduced as custom Lean assumptions. Universal instantiation produces a finite derivation of every threshold contract and every horizon contract. The package then proves that **every closed descendant of these two root formulas is valid on the declared scenario class**. This includes every future finite composition using the checked rules, not just the audited examples.

It also checks a joined derivation with **two explicit local hypotheses**—successful threshold discrimination and an actual repeated spending trace. Its conclusion is the conjunction of the information and reserve restrictions. Discharging the two premises produces the corresponding closed nested implication. Two independently necessary constraints are thereby retained together; this does not claim that the separate witnesses construct one jointly affordable sensing-and-action apparatus. Such a joint realization needs an actual compatible process, as required by [the repository's composition principle](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/PROTOCOL-COMPOSITION.md).

All valid theorems are true throughout their model class; one should not demand that valid theorems have different truth values there to count as informative. Here “operationally different” is established by the pairwise distinct question-capability predicates and exact budget/horizon exclusions. This is an unbounded family of substantive constraints. It is not a proof that indefinitely listing them increases practical or ethical wisdom.

## 6. The exact route from this construction to the entire proposed root

H4 is a reduction of the whole-theory task, not a proof that every candidate starting principle already passes. The [current minimal grounding](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/GENERATIVE-GROUNDING.md#minimal-grounding-and-universal-scope) names consequential differentiation, structured interaction, and composition with possible recurrence. The [premise ledger](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/FOUNDATION-PREMISES.md) already distinguishes these from informative laws, recipes, empirical identifications and ethical reasons. To make the **entire proposed root**, rather than just H9, necessary, the following obligations must each be discharged or kept as explicit antecedents:

| Proposed part of the entire account | Exact necessity or derivation still needed | What cannot substitute for it |
|---|---|---|
| Consequential differentiation | Show that the independently specified empirical-discrimination capability requires a difference accessible through its full information interface; determine which stronger claims about observer-independent differences this warrants | Using different words in an argument does not establish every proposed ontology of difference |
| Structured interaction and models within reality | Establish the relevant dependences and show that the model's use in judgment/action is included in the causal account; justify any stronger universal causal formulation | A transition representation can encode a supplied history without establishing its physical law |
| Composition and recurrence | Preserve actual intermediate conditions for joined inquiry; derive any recurrence claim from separately established continuing-demand/lifetime premises | A single successful judgment does not require an internally self-renewing organism |
| Organizational significance and regulation | Derive the relevant consequence-sensitive mechanism from dependency laws, with material formation and retained effects | Naming the analyst's success score does not install the mechanism that responds to it |
| Learning and revision of selectors | Show how evidence changes and selects actual rules, including which rules can themselves change and what pays for that change | A freely supplied correct decoder or reward bypasses the capacity being derived |
| Warrant and calibration | Identify the admitted error class, complete observations, target correspondence and grounds for the law restriction; construct tests where correction is claimed | A sound theorem cannot establish its empirical calibration by asserting that the theorem was generated |
| Shared concern and ethical reasons | Supply an independent argument for the relevant center, positive grounds and valid reason-transfer relation, then derive their causal formation and revision | Accurate self-regulation and survival do not entail another center's standing or its consideration |
| Wisdom and continuing growth | Join warranted understanding, justified purposes and feasible revisable action; distinguish sound extension from completeness and infinite execution | An unbounded list of mathematical instances is not itself increasingly wise judgment |

This table does not impose premise-free physics or unique ontology as a new completion condition. Local law inputs are legitimate. The entire theory can include their **universally sound conditional consequences**, together with correctly labeled empirical findings and open hypotheses. What H4 does not permit is treating those different statuses as one unqualified necessary conclusion.

The practical route to Ren's stronger target is to identify a compact necessary basis and an explicit generative rule system, translate the substantive current theory into derivations with its actual local inputs, and investigate which remaining premises can themselves be generated or independently justified. Where a premise is contingent, the resulting necessity attaches to the implication; where it is constitutive of the inquiry class, its necessity can propagate unconditionally. The hypothesis count and its semantic role must survive every translation.

This is why the current [recipient evidence](../../2026-10-05-concern-theory/RECIPIENT-IDENTIFICATION-INTEGRATION.md) and [reason-replay](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/RECORDED-REASONS.md) interfaces matter to the whole-root question. They replace some supplied downstream capacities with actual producers. But no-false-positive target laws, context identity, relevance grounds and paid apparatus retain their distinct roles. They can become antecedents of further necessary theorems immediately; their unconditional necessity requires the corresponding further arguments.

## 7. What “infinity of wisdoms” can now mean precisely

There are four different extensions:

1. **Proof extension:** no fixed bound on the number or depth of sound finite consequences. H4 covers the entire closure.
2. **Operational extension:** new indices correspond to genuinely different questions, capacities and exclusions. H7–H9 give a checked unbounded family.
3. **Realized epistemic extension:** an actual inquirer acquires warranted information and expands what it can establish or do. The information, resources, acquisition and implementation must be constructed.
4. **Wise extension:** improved judgment about what deserves concern and appropriate action. Justified ends, affected centers and practical context must enter, beyond correct prediction or more statements.

The first two are now concretely realized in the formal account. The third and fourth remain connected derivation tasks, partly advanced by the existing material, learning, recipient and reason studies. Their distinctness does not make a common root impossible. It specifies what a root claiming to generate all four must generate, instead of assuming that mathematical infinity performs the later transitions.

Soundness of every generated conclusion also does not require that every truth be generated. The inherited incompleteness argument is compatible with Ren's one-way claim: indefinitely many necessary insights can arise from a root without that root deciding all possible statements. A fallible conjecture generator may help discover candidates outside the current proof closure, but acceptance needs evidence or proof appropriate to their status. Discovery and certification can belong to one generative process without becoming the same operation.

## 8. Verification, contribution and next bridge

The [verification record](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/verification.json) freezes the exact sources and compiler hashes, compiles inherited dependencies in a fresh temporary directory and reports all declaration dependencies. The new proofs use only disclosed standard Lean foundations: `propext`, `Classical.choice` and `Quot.sound`, depending on the declaration. There are no custom axioms, admitted proofs or unchecked computational shortcuts in the accepted source. The source checks, compiler and its ordinary type theory remain trusted infrastructure. “Kernel checked” does not certify the interpretation of a scientific instrument or establish a philosophical premise by itself.

The **new contribution** is the explicit equivalence between necessity of the whole generated theory and necessity of its basis, with local contexts retained, reusable derived rules, and a checked unbounded operational witness connected to the existing generative process core. The general mathematics is elementary and established in kind. Prior sound-extension and information-fiber results are credited above. No new empirical measurements, priority claim or completed universal wisdom theorem is made.

**Internal integration review, 6 October 2026:** the proof-study author independently checked [the canonical synthesis, Sections 2–5](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/HUIGEN.md#2-the-exact-transfer-theorem) against the accepted source and reviewed the [symmetry package](../../../../experiments/integrated-correction/general-framework/generative-basis/necessity-symmetry/README.md), its code and saved report. No mathematical or scope blocker was found. The synthesis preserves the nonempty inquiry class, premise discharge, whole-closure quantifier and operational meaning of the infinite family. The separate symmetry count is exactly \(2^1+2^4+2^9+2^{16}=66{,}066\), with saved invariant counts 2, 4, 4, 4; its current source hash matches the report. The two-orbit argument applies to homogeneous contexts with at least two centers, and the singleton exception is preserved. These are separate internal checks, not another run or empirical confirmation. The closure package remains 27 new and 23 inherited audits; the symmetry enumeration is not a Lean theorem count.

The next central task is **candidate necessary basis → premise-tracked derivations of the current substantive theory**, beginning with the unresolved calibration and reason interfaces. A decisive positive result would discharge a currently supplied capacity through an actual producer while preserving its interpretation and paying its costs. A decisive negative result would exhibit an independently adequate inquiry violating a proposed root premise under unchanged meanings, or show that a claimed descendant needs an extra undischarged premise. H4 makes both outcomes consequential for the entire root, rather than leaving them as isolated exceptions.

The strongest progress is therefore about the whole: **a finite necessary root can support an entire indefinitely extensible necessary theory; all its properly generated descendants inherit that necessity. We now have an exact checked construction of that architecture, substantive infinite families inside it, and a finite, inspectable account of what the proposed broader root still has to establish.**

## 9. One coherent interpretation can cover the unbounded closure

**Lean migration, 8 October 2026:** [The checked continuation](DEDUCTIVE-FOUNDATION-TEST.md#20-one-coherent-interpretation-for-a-finitely-based-whole) now implements the finite-basis H10–H11 reduction and the separate-row H12 control in the unchanged calculus, including the empty-basis case and conditional local contexts. [Ten new theorems / 12 new empty audits](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/joint-interpretation-verification.json) pass with 12 inherited empty audits. The infinite-basis example, compactness discussion and H13 below remain at their historical hand-proof scope; this notice does not retroactively certify them or the substantive foundation.


6 October 2026. Further hand arguments, not additions to the preceding Lean package. The named connection is **a necessary root across different representations → a meaning-preserving whole generated theory**. The [mathematical comparison](MATHEMATICS-UNIQUENESS-RESOLUTION.md#u6-equivalence-and-shortest-description-require-a-declared-comparison) already distinguishes equivalent presentations from a unique ultimate explanation. The present extension addresses the quantifiers needed for Ren's whole-theory claim. None of these statements establishes necessity of the substantive root by itself.

### H10. Whole interpretation and finite-basis reduction

For each independently admitted inquiry realization \(I\), let \(A_I\) be a declared class of admissible interpretations of the root language in that realization. These interpretations may use different notations, carriers and encodings. Admissibility must be justified by the independently specified questions and meanings, not defined as making the root true. Write \(V_{I,\tau}(p)\) for the truth of the interpreted claim. Each candidate \(\tau\) must retain local premises and make every rule of the declared generator truth-preserving on its intended domain. A finite collection of successful translated proofs does not by itself establish that global rule condition.

For any fixed \(I,\tau\), the proof of H3a then gives

\[
\bigl[\forall b\in B,\ V_{I,\tau}(b)\bigr]
\ \Longleftrightarrow\
\bigl[\forall q\in\operatorname{Gen}(B),\ V_{I,\tau}(q)\bigr].
\tag{H10}
\]

Root inclusion proves one direction; finite-proof induction proves the other. With a local context \(\Gamma\), the corresponding conclusion still depends on \(\Gamma\); an interpretation cannot make an empirical law or ethical premise disappear. The same interpretation must serve the whole derivation, although different realizations can require different faithful maps.

Suppose further that \(B=\{b_1,\ldots,b_m\}\) is finite and nonempty, conjunction introduction belongs to the generator, and every candidate interpretation reads finite conjunctions faithfully. Then for each \(I\) the following are equivalent:

\[
\begin{aligned}
&\exists\tau\in A_I\ \forall q\in\operatorname{Gen}(B):V_{I,\tau}(q),\\
&\exists\tau\in A_I:V_{I,\tau}(b_1\land\cdots\land b_m),\\
&\forall q\in\operatorname{Gen}(B)\ \exists\tau\in A_I:V_{I,\tau}(q).
\end{aligned}
\tag{H11}
\]

**Proof.** A common interpretation gives the pointwise condition. That condition applies in particular to the derived conjunction of all root premises. Its witnessing interpretation satisfies every root premise, hence H10 gives the whole closure in that one interpretation. ∎

This is a positive reduction of the infinite obligation: jointly interpret the finite root and establish the generator's soundness, rather than search through every descendant separately. A common interpretation means semantic coherence, not that one finite agent must store, know or execute every descendant. It gives no effective search for the right interpretation and no empirical certificate for its admissibility. The same argument applies when an infinite presentation has a finite generating basis inside its closure and that basis generates the entire claimed theory. A finitely written schema with infinitely many independent instances is not automatically such a finite basis.

### H12. What claim-by-claim matching can and cannot establish

Checking an inventory one row at a time is weaker than the last line of H11. For example, take a target valuation with \(x\) true and \(y\) false, and two candidate compositional interpretations of source atoms \(p,q\): the first maps them to \(x,y\), the second to \(y,x\). Each root row in \(B=\{p,q\}\) can separately be made true, but neither interpretation satisfies both. The conjunction \(p\land q\) exposes the mismatch. This is a counterexample to separate-row matching, **not** to H11's condition over every member of a conjunction-closed theory. Independent reference constraints might exclude one or both maps before this test; the example does not certify either map as scientifically faithful.

A genuine failure for the entire closure is possible when the finite-basis condition is absent. Use a finitary propositional language with independent atoms \(p_0,p_1,\ldots\), root \(B=\{p_k:k\in\mathbb N\}\), and ordinary sound propositional inference. Restrict candidate interpretations to \(\tau_n\), where \(p_k\) is true exactly when \(k\le n\). Every particular finite derivation uses finitely many root atoms. Choosing \(n\) at least their maximum makes those premises, and hence its conclusion, true; if none is used, any \(n\) suffices. Thus every member of the full closure has some witnessing \(\tau_n\). No single candidate satisfies the entire root, since \(p_{n+1}\) is false under \(\tau_n\).

The missing all-true interpretation is deliberately outside this declared candidate family. This is not a contradiction or a refutation of ordinary logical compactness: the family is restricted. More generally, put \(S_q=\{\tau\in A_I:V_{I,\tau}(q)\}\). Faithful finite conjunction and pointwise truth give these sets the finite-intersection property. If \(A_I\) is compact in a topology making each \(S_q\) closed, a common interpretation exists. A finite nonempty candidate family is a simple sufficient case. Those are additional conditions, not consequences of calling a theory generative. Adding a universally quantified root sentence requiring all \(p_k\) would also change the test: no \(\tau_n\) satisfies that sentence. Neither device is a free repair to an independently restricted scientific interpretation.

### H13. The operational invariant is a preserved question

The earlier information obstruction has a representation-independent form. Let a complete accessible observation be \(O:X\to Y\), and let the required answer be \(f:X\to Z\). Exact deterministic inquiry succeeds when some \(d:Y\to Z\) has \(d\circ O=f\). For a bijective recoding \(h:Y\to Y'\), the recoded observation \(O'=h\circ O\) admits \(d'=d\circ h^{-1}\), with the same composite answer. Existence of a decoder is therefore invariant under this recoding. This is a mathematical representation result; a physically implemented recoder may have costs and failure modes needing a separate account.

By contrast, if a proposed coarsening \(c:Y\to Y'\) makes \(c(O(x))=c(O(x'))\) while \(f(x)\ne f(x')\), no decoder through that coarsened interface succeeds on both inputs. The target distinction, rather than the source's preferred names, does the necessary work. Preserving one query may still erase distinctions required by another. A philosophical account need not contain our data structure literally, but it cannot claim that exact answer through the same complete interface while discarding an indispensable distinction.

### H14. A faithful mathematical interpretation is not an acquired capacity

For an exact finite example, suppose a sensor reports \(y=x\mathbin{\oplus}\theta\), with hidden bit \(x\), fixed polarity \(\theta\), and exclusive-or \(\oplus\). For each specified polarity there is an exact decoder \(d_\theta(y)=y\mathbin{\oplus}\theta\). But an agent receiving only \(y\), with no other accessible polarity information, cannot decode uniformly across both polarities: \((x,\theta)=(0,0)\) and \((1,1)\) give the same report and different correct answers. Thus the external existence of a suitable interpretation does not supply calibration to the actual learner. A claimed acquired capability must produce that information or retain it as an explicit local premise, together with any required resources. This reuses the earlier information-fiber obstruction; it is not a counterexample to a theorem restricted to already adequate inquiry.

Preserving passive observations alone is also insufficient when an account claims intervention answers. Consider a fair exogenous bit \(Z\) and two stipulated equation systems: \(X=Z,\ Y=X\), and \(X=Z,\ Y=Z\). Their passive joint distributions on \(X,Y\) agree. Under the declared intervention that replaces the equation for \(X\) by \(X=1\), the first system has \(Y=1\), whereas the second leaves \(Y=Z\). Observational agreement therefore does not establish preservation of those intervention claims. This elementary constructed example assumes the stated equations and intervention semantics; it does not identify the causal structure of any measured physical system.

Both examples matter to the ongoing evaluative join. An analyst's mapping from recipient records to a relevant condition cannot stand in for the learner's acquired access to that condition. Nor can matching action rates certify that two mechanisms preserve the same patient, reasons, permission or response to changed evidence. The [finite evaluative contract](HUIGEN-FULL-THEORY-AUDIT.md#applicability-transfer-and-costly-choice) remains the accepted immediate causal test; this extension explains why its interpretation and acquisition requirements are part of the whole-theory argument.

### Meaning and necessity remain separate obligations

H10–H13 permit nonidentical descriptions without weakening a valid common constraint. They do not identify every scientific theory with ours, force a unique ontology, or show that all target logics use the same consequence relation. The assumed rule semantics must be justified for each claimed interpretation; the hand proofs themselves use an ordinary mathematical metatheory.

Crucially, \(\forall I\exists\tau\) establishing a root representation is weaker than establishing the truth of every intended claim about actual patients, interventions or reasons. Merely relabeling an actor's stock as a recipient's good, or an enabled command as moral authority, does not establish the claimed relation. A substantive reduction or identity needs its own justification. Independently fixed reference and semantic adequacy must connect the interpreted formulas to the claims whose necessity is at stake. Agreement of all independently admissible interpretations on the relevant anchored fragment is one sufficient way to remove interpretive ambiguity; arbitrarily selecting the favorable one is not.

The [philosophical admissibility assessment](HUIGEN-NECESSITY-ARGUMENTS.md#10-necessity-across-representations-without-trivial-containment) states those conditions and the primary comparisons. For the full foundation, the resulting next test is joint: identify a candidate finite basis, one faithful interpretation per admitted inquiry realization, sound generation and actual coverage of the substantive claims. A successful translation of selected claims cannot discharge omitted local premises or the unresolved normative grounds.
