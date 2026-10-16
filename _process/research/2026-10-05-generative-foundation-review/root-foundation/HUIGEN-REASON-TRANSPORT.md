# From positive reasons to shared standing: exact transport requirements

**Checked constructive scope, 7 October 2026:** the [universal-goal integration](UNIVERSAL-METAETHICS-LEAN-INTEGRATION.md#3-the-constructive-correction) now verifies Prop-valued least-closure and same-history scope composition in Lean. The Boolean interpretation and explicit incoming-crossing arguments below retain their classical hand-proof scope. A distinct reverse-closed-cut audit proves that absence of such a cut gives double-negated reachability; its unrestricted upgrade is equivalent to double-negation elimination. These formulations must not be silently identified constructively. This is a logical-scope qualification, not a rejection of the earlier classical theorem or a derivation of ethical seeds and transports.

6 October 2026. AI-authored continuation of the [entire 慧根 objective](../../../../theories/becoming/history/HUIGEN.md). The named bridge is **significance for a differentiated patient → valid reasons addressed to other deliberators → feasible action and answerable protection**, including a patient who cannot communicate, reward, threaten or sustain the investigator.

**Result:** positive anchors and independently justified reason-preserving transformations force exactly the reasons reachable from those anchors. Complete coverage is equivalent to the absence of an isolating cut without an anchor. This supplies both a positive construction and a precise countermodel for every uncovered target. Separating *deliberators* from *patients* reveals a further obligation: transferring a reason between deliberators does not establish a first positive reason about a patient outside the set of deliberators. The full bridge may require both patient/condition transport and deliberator transport.

These are semantic consequences of declared normative premises, not a proof that graph connectivity creates ethical validity. Existing [rooted reason closure](../../2026-10-05-revisable-concern/settlement/formal/REPORT.md#1-finite-reasons-and-retained-grounds) already implements finite propagation and selective retraction. This note does not duplicate that implementation or add a new Lean count. It characterizes which standing claims its supplied premises entail, which new kinds of transport a broader ethical conclusion requires, and what must be preserved in the current material interfaces.

## 1. The reason has a bearer and an addressee

Let \(A\) be deliberators and \(P\) be independently admitted moral patients. They need not be the same set. A patient can be an infant, an unconscious person or another being with the relevant admitted interest who cannot deliberate. Where appropriate, a map \(s:A\to P\) identifies a deliberator's own patient position. This map need not cover \(P\).

A reason token has the type

\[
v=(a,p,c,k),
\tag{T1}
\]

where \(a\) is the deliberator, \(p\) the patient, \(c\) the relevant context and \(k\) a particular reason kind. Let \(R(v)\) say that this patient-related fact supplies this deliberator a pro tanto reason of that kind in that context. The reason can exist even if the actor denies it, fails to recognize it or cannot act on it. The token is not the total value of a person and not an all-things-considered verdict.

Three different claims must remain visible:

- \(F(p,c,k)\): an independently described good, harm, vulnerability or other fact is present for the patient;
- \(R(a,p,c,k)\): the fact supplies a reason addressed to the actor;
- \(M(a,p,c,k)\): the actor recognizes, uses or is motivated by that reason.

Accurate scientific representation can establish or support \(F\). A reliable implementation can make an acquired record affect \(M\). Neither relation is identical to the validity asserted by \(R\). The [ethical foundation](../../../../theories/becoming/history/ETHICAL-FOUNDATION.md#explicit-premises-and-limited-deductions) makes the normative components explicit: N1 supplies standing for admitted goods and harms; N2 requires relevant consistency; N3 supplies answerability; N4 constrains promised implementation.

If N1 is already interpreted as saying that every relevant patient's harm supplies every relevant actor a reason, universal cross-actor standing is already a premise. A propagation theorem can apply it, but cannot claim to have derived that same universality. To investigate the missing bridge, start from explicitly narrower positive anchors and state the transformations being justified.

## 2. Exact entailment from anchors and warranted transports

Let \(V\) be a declared set of reason tokens, \(B\subseteq V\) independently justified positive anchors, and \(E\subseteq V\times V\) independently justified implications. An edge \(uEv\) asserts that the reason at \(u\), together with its stated currently valid relevance conditions, entails the reason at \(v\). The factual/relevance conditions are fixed for this theorem; a context change or defeater requires a different valid edge relation. This exact characterization concerns positive unary implications. A rule requiring several reason premises jointly needs an explicit premise bundle or richer rule system; neither premise may silently replace the required conjunction. The theorem is not claimed to exhaust every form of ethical reasoning.

Call an interpretation \(r:V\to\{0,1\}\) admissible for these premises when

\[
b\in B\Rightarrow r(b)=1,
\qquad
uEv\ \land\ r(u)=1\Rightarrow r(v)=1.
\tag{T2}
\]

This is a model of the **stated premises**, not a definition of moral truth. A morally correct interpretation may satisfy further grounds not included in \(B,E\). Let \(C\) be the set reached from \(B\) by zero or more finite \(E\)-steps.

**T2a — Exact forced-standing theorem.** For every token \(v\),

\[
\boxed{v\in C
\quad\Longleftrightarrow\quad
\text{every interpretation satisfying (T2) makes }r(v)=1.}
\tag{T3}
\]

**Proof.** A path begins with a positive anchor and preserves positivity along every edge, so every admissible interpretation is positive at its endpoint. Conversely, define \(r_C(v)=1\) exactly when \(v\in C\). Every anchor is in \(C\), and \(C\) is closed under each edge. Thus \(r_C\) satisfies all premises. If \(v\notin C\), it assigns zero there, giving a countermodel to entailment. ∎

This is the semantic least-model reading of established rooted closure. The existing settlement's finite R1 proves its operational counterpart. The new use is as an ethical coverage audit: every omitted patient or actor scope is attached to a particular undischarged bridge. No assumption of finite \(V\) is needed for T3; every supporting argument is a finite path. It says nothing about a physically finite procedure completing an infinite audit.

An uncovered token is **not thereby disproved**. T3 says that these premises do not force it. Adding an independently warranted anchor or transport can establish it. Conversely, adding an unsound edge can force a conclusion in the formal system without making it morally valid. The edge justification is where the ethical argument must occur.

### Exact cuts locate what an additional premise must cross

Let \(D\subseteq V\) be the target coverage set, fixed independently of what the procedure happens to admit. Then the following are equivalent:

1. \(D\subseteq C\).
2. Every subset \(U\subseteq V\) with \(U\cap B=\varnothing\) and \(U\cap D\ne\varnothing\) has at least one valid incoming transport: some \(u\notin U\), \(v\in U\) satisfy \(uEv\).

**Proof.** For (1)⇒(2), choose a target in \(U\). A finite root path to it starts outside \(U\), so its first entry supplies the required edge. For the converse, if a target is unreachable, take \(U=V\setminus C\). It contains that target, contains no anchor and has no edge entering from \(C\), because \(C\) is forward closed. This contradicts (2). ∎

The cut condition is an exact structural requirement, not an independent ethical axiom. It tells us what the missing argument must accomplish. If \(J\) is a proposed additional transport family, complete coverage under \(E\cup J\) holds exactly when \(J\) crosses every target-containing, anchor-free subset having no incoming \(E\)-edge. There need not be a uniquely necessary individual edge: alternative grounds can cross the same cut.

For a finite graph and **all-node coverage**, a sharper count is possible. Remove the currently reachable set. In the remaining graph, contract its strongly connected components. Let \(m\) be the number of source components of that acyclic component graph. If there is at least one anchor and arbitrary new directed edges are permitted, exactly \(m\) added edges suffice and are necessary: connect one reached anchor to one node in each source component. Every inaccessible component lies downstream of a source; each source needs an incoming new edge because no old edge enters it from elsewhere. This counts required entry certificates under that permissive menu, not independent ethical principles. A single justified principle could generate many such certificates, and the required new edges may have no available ethical justification. With restricted candidate edges, the preceding cut condition remains the exact criterion.

## 3. The noncommunicating patient exposes two distinct transport tasks

Consider a fixed reason kind and context in which actor and patient changes can be assessed separately. Let \(E_A\) be justified actor transports and \(E_P\) justified patient/condition transports. They induce two kinds of edges on \(A\times P\):

\[
(a,p)\to(a',p)\quad\text{if }aE_Aa',
\qquad
(a,p)\to(a,p')\quad\text{if }pE_Pp'.
\tag{T4}
\]

These laws are separable only on a domain where the relevant actor–patient relationships and other premises permit that separation. In general, use the full token graph in T1 rather than assume a product.

**T3a — Product-transport characterization.** With positive anchor set \(B\subseteq A\times P\),

\[
\boxed{(a,p)\text{ is forced}
\Longleftrightarrow
\exists(a_0,p_0)\in B:
a_0\leadsto_A a\ \land\ p_0\leadsto_P p.}
\tag{T5}
\]

**Proof.** Project an actual product path onto each coordinate, removing unchanged-coordinate steps. The projections give the two stated paths. Conversely, beginning at the anchor, first follow the actor path with patient fixed, then the patient path with actor fixed. The stipulated separability makes each step available. Apply T3. ∎

Suppose the initial anchors are only own-case reasons \((a,s(a))\). Full actor independence can spread the reason concerning a represented patient among all deliberators. It cannot introduce a positive reason about a patient \(p\notin s(A)\) if no patient transport reaches \(p\). This is an additional gap concealed by assuming from the outset that patients and deliberators are identical sets.

For a concrete countermodel, let \(A=\{a,b\}\), \(P=\{p_a,p_b,p_c\}\), and \(s(a)=p_a,s(b)=p_b\). The patient \(p_c\) cannot deliberate. Give each actor its own positive anchor and allow all actor transports, but no transport to \(p_c\). Then

\[
r(a,p_a)=r(b,p_a)=r(a,p_b)=r(b,p_b)=1,
\qquad
r(a,p_c)=r(b,p_c)=0
\]

satisfies all those premises. Every actor can accurately represent \(p_c\)'s suffering and understand its consequences. The countermodel denies only that the stated premises have made it a reason addressed to those actors. No lack of consciousness, bad empirical reasoning or missing causal representation is needed in the model.

The two bridges can be compared exactly on these six tokens. Retain only the two own-case anchors; let the actor bridge permit either actor change at fixed patient, and let the patient bridge carry \(p_a\)'s reason to \(p_c\) at fixed actor:

| Available transport | Forced tokens | Number |
|---|---|---:|
| Neither bridge | \((a,p_a),(b,p_b)\) | 2 |
| Actor bridge only | Both actors' reasons concerning \(p_a,p_b\) | 4 |
| Patient bridge only | The two anchors and \((a,p_c)\) | 3 |
| Both bridges | Both actors' reasons concerning all three patients | 6 |

The table follows by explicit finite paths, not a new experiment. In particular, the patient bridge supplies a reason about the silent patient but does not alone address it to every actor; actor independence supplies universal addressability for the anchored patients but does not alone add the silent patient. Together they cover all six tokens.

The earlier self/other symmetry obstruction is a special case. A simultaneous renaming sends \((a,s(a))\) to another corresponding self-case. It need not send \((a,p)\) to \((b,p)\), which changes the deliberator while keeping the patient fixed. Treating those operations as identical would supply the contested actor transport under the name of renaming.

## 4. The strongest positive route: preserve the ground that justified the anchor

The exact theorem provides a constructive route to a dispensable patient's standing. It requires a defended account of the **ground** of a positive reason, not just a positive bit.

Suppose an anchor judgment is justified because an identified experience or deprivation is bad for its subject, in circumstances where an actor controls its avoidable imposition. The philosophical argument can then distinguish:

1. **The ground:** independently described features of the harm and its relevance to the subject.
2. **The scope of the ground:** why these features supply the particular pro tanto reason being claimed.
3. **Possible defeaters or modifiers:** consent, responsibility, uncertainty, urgency, legitimate relationships and competing claims.
4. **Irrelevant differences for this particular ground:** names, administrative labels, ability to retaliate, or usefulness to the actor, where those differences do not alter the stated ground or introduce an independently justified defeater.

If the anchor's offered justification genuinely treats the identified ground as sufficient, a second case retaining that ground and its applicability conditions inherits the reason. This is a **ground-preserving transport**, not a demand for identical actions or identical total moral weight. It permits another reason to arise from a special relationship while retaining the original baseline reason against a harm.

An exact formulation uses an independently justified relevance representation \(g:V\to G\). Assume that a reason judgment for the chosen kind is constant on equal \(g\)-values. Then every relevance class containing a positive anchor is positive throughout; classes without anchors can consistently remain unassigned or zero. Thus the exact obligation is **anchor coverage of the target relevance classes**, together with a justification that \(g\) has preserved every distinction relevant to the reason. Choosing a representation that deletes actor identity is not itself a proof that actor identity is irrelevant. That is the philosophical argument it has to embody.

Applied carefully, this gives two positive bridges. A **patient bridge** carries an identified harm-ground to a noncommunicating patient capable of undergoing that kind of harm; it does not require that patient to articulate the reason. A **deliberator bridge** shows why the same ground remains a reason for another actor who controls its occurrence, even when the patient has no productive or strategic value to that actor. T5 then yields the combined standing. Neither reciprocity nor the patient's usefulness is a mathematical input to that derivation.

The conditional force is substantial: an actor cannot retain the claim that the harm-ground is sufficient, accept that all its applicability conditions are preserved, and then cancel the reason solely by an excluded label change. But the claim of sufficiency must itself be defended. An egoist can reject it by claiming that the anchor arose from an essentially self-indexed reason. The relevant debate is whether that restriction withstands justification of shared practical authority; accurate observation alone does not settle it. This is the precise place where N1, N2 and N3 must do substantive work.

N3 supports a related but distinguishable positive route. Once an arrangement claims to answer the admitted claims of everyone over whom it exercises the relevant power, it cannot truthfully certify that those claims have been answered merely because an affected patient cannot speak or compel a response. Reliable representation can communicate the patient's admitted objection. That conclusion constrains a declared standard of answerability; it does not by itself prove that every patient-related fact is an admitted moral reason. The standing and coverage arguments remain visible.

## 5. A reason against an action needs a causal and practical bridge

Standing is not yet an instruction to choose a particular action. For a deliberator \(a\), let \(\mathcal F_a(c)\) be the genuinely feasible actions in context \(c\). For a pair \(x,y\in\mathcal F_a(c)\), suppose an identified causal comparison establishes that \(x\) imposes an additional admitted harm on patient \(p\) which \(y\) avoids.

A **derivative reason premise** states that this additional harm, when grounded in the valid reason kind at \((a,p,c,k)\), supplies a pro tanto reason against \(x\) relative to \(y\). The actor's role in producing the harm and the relevance of that kind of difference must be part of the premise. T3 then determines when the supplied anchors and transports force this particular derivative reason. It does not provide the causal comparison, the feasibility of \(y\), or the derivative premise merely by filling a graph.

This directly matches the [ethical foundation's D1](../../../../theories/becoming/history/ETHICAL-FOUNDATION.md#explicit-premises-and-limited-deductions). If the feasible options are identical in all other morally relevant respects, all relevant reasons have been included and no contrary reason remains, the added harm defeats justification of the worse option by that reasons profile. The final dominance step requires those completeness and relevance conditions. With competing reasons, the pro tanto reason remains, but no all-things-considered choice has yet been derived.

Two limits are exact:

- If no feasible harmless alternative exists, the standing reason does not disappear. What fails is that particular dominance comparison. N3 and N4 can still require explanation, changes to enabling conditions, fair distribution of unavoidable burdens or repair; their detailed priority premises remain separate.
- If no relevant choice involving a patient occurs, observed action cannot establish whether that patient's standing is recognized. Two mechanisms can agree on every available action while differing in reasons that would matter under another feasible menu. Behavior alone is not a complete test of the normative relation.

Likewise, the set of individually feasible protections need not be jointly feasible. A common reserve might fund either of two patients but not both. Full standing then establishes two claims requiring judgment, not a proof of a nonexistent jointly protective action. No welfare sum or rule erasing the unfunded patient is supplied by the coverage theorem.

## 6. Positive coverage does not guarantee an effective protective margin

The current settlement requires each implemented patient margin to exceed an actual suppression/control bound. Mere positive reachability cannot supply that quantitative requirement. The following optional extension states the difference precisely without identifying ethical validity with a numerical utility.

Interpret \(q(v)\in[0,1]\) as a **declared implemented influence or certified lower-bound variable**, not moral worth. Let anchor bounds be \(b(a)\in[0,1]\), and each implemented transmission edge \(e:u\to v\) impose \(q(v)\ge g_e q(u)\), with \(g_e\in[0,1]\). Let

\[
L(v)=\sup\left(\{0\}\cup
\{b(a)\!\prod_{e\in\gamma}g_e:
a\text{ an anchor},\ \gamma\text{ a finite path }a\to v\}\right).
\tag{T6}
\]

**T6a — Exact minimal transmitted bound.** Every admissible \(q\) is at least \(L\), and \(L\) itself is admissible. Therefore the constraints force \(q(v)>d\) exactly when \(L(v)>d\).

**Proof.** Iterating edge inequalities gives the bound associated with every path, hence their supremum. Zero-length paths give anchor bounds. Appending an edge to every path to its source, and using multiplication by a fixed nonnegative number to preserve the bounded supremum, gives \(L(v)\ge g_e L(u)\). All path values lie in \([0,1]\), so the supremum exists there. Thus \(L\) satisfies every constraint and witnesses failure of any stronger universal bound. ∎

In a finite graph, cycles with gains at most one can be removed without reducing a path value, so a maximum over simple anchor paths suffices. Without these gain restrictions, amplification cycles can make finite-valued feasibility fail; they must not yield a vacuous claim that every finite threshold is protected.

A single valid positive path with implemented gain \(1/100\) and anchor bound one establishes positivity but not a margin greater than \(1/2\). This does not show a weak moral reason or justify harming the patient. It shows that an implementation transmits too little influence for the stated control guarantee. The [settlement](../../2026-10-05-revisable-concern/settlement/formal/REPORT.md) separately supplies its evaluative gains, per-patient margins and strategic menu. Converting a valid reason into adequate motivational or institutional force remains part of the generative explanation.

## 7. The exact interface with recorded reasons and protection

The accepted [recorded-reasons construction](../../../../theories/becoming/history/RECORDED-REASONS.md) derives its operational mask from authentic current records, a calibrated factual assay and a separately supplied relevance relation. Its generic node/context semantics can encode the deliberator index in T1. There is no claim here of an implementation bug or an inability to represent actor-relative reasons. The export contract must simply state whether its context or reason node includes that index. If it omits the index while claiming validity for all deliberators, that independence has been supplied, not derived by replay or succession.

For a shared-standing application, a certificate should bind at least:

- the patient and the factual question;
- the deliberator or the explicitly justified actor scope;
- the reason kind and the relevant context;
- the positive anchor and justified transport premise;
- current evidence, validity conditions and any defeaters;
- the distinction between reason validity, installed use and delivered action.

A successor may inherit the same reason when the scope includes it and the context remains valid. If the original reason was essentially indexed to one deliberator, physical copying alone cannot turn it into a universal reason. Conversely, replacing the software process while preserving the relevant deliberative role need not defeat the reason; the identity criterion is supplied by the actual semantic contract rather than byte equality.

There are at least five sets to distinguish: valid reasons; reasons entailed by the declared justified premises; those supported by currently accessible certificates; reasons actually reconstructed in a completed paid audit; and protections actually delivered. Under authentic current sound interfaces, the reconstructed reasons can be a subset of the warranted reasons. There may be additional valid grounds not represented by the finite graph. Delivery failure does not refute a reason. Losing one particular path does not remove another independent path or establish that a patient has no standing.

The [reason-to-protection review](../../../history/2026-10-05-revisable-concern/settlement/formal/REASON-PROTECTION-REVIEW.md) requires the same separation. A protection choice needs the physical apparatus, paid action, authority and supplied evaluative uptake; unaudited voluntary protection must remain in the feasible repertoire. Otherwise a manufactured audit interlock could make philosophical reasoning appear mechanically necessary for helpful action. The construction was still under review when this paragraph was first written and has subsequently been accepted at its declared scope. That later result is inherited, not an additional verification performed here.

## 8. What is established, what remains supplied, and the next decisive result

| Claim | Established consequence | Inputs still requiring justification or identification |
|---|---|---|
| All target reasons follow from anchors and transport | Exact reachability/semantic-entailment/cut equivalence | Positive anchors, valid implication edges, target domain and context |
| Noncommunicating patients can be covered | Product transport reaches them when both required coordinate paths exist | Patient admission, patient/condition relevance and actor transport; speech is not assumed |
| Additional harm supplies a derivative action reason | Conditional transfer through an admitted causal harm contrast | Actual consequences, feasible alternatives and normative relevance |
| Reasons settle an action comparison | Conditional dominance with no omitted or contrary relevant reason | Completeness of the comparison, conflict/priority grounds |
| Implemented influence clears a control threshold | Exact lower path-envelope criterion under bounded nonamplifying gains | Influence interpretation, transmission laws, action menu and threshold |
| Physical replay yields valid shared reasons | Existing producer can realize the typed contract if supplied | Actor scope, calibration, justified relevance, actual support and authority |

The original [rooted closure proof](../../2026-10-05-revisable-concern/settlement/formal/REPORT.md#1-finite-reasons-and-retained-grounds) and the recorded-reasons verification remain inherited. T3's entailment interpretation, the cut and product characterizations, the finite source-component count and T6's path-envelope result are elementary hand arguments displayed here. No new empirical evidence or independent priority is claimed; no prior Lean package or numerical study was rerun merely for this exposition.

An independent collaborating-agent review on 6 October 2026 found no mathematical blocker in the least-model, cut, product, finite component-count or bounded-gain arguments. It specifically confirmed the patient/deliberator distinction and requested that the positive-unary-implication scope be explicit; that qualification is retained in Section 2. This is internal proof review, not external peer review or another empirical result.

**Reciprocal cross-review, 6 October 2026:** this note's author read the complete [practical-necessity audit](HUIGEN-PRACTICAL-NECESSITY-AUDIT.md), especially its full-capacity indexed countermodel and no-unilateral-discharge argument. No blocking issue was found. The countermodel preserves the listed scientific, reflective and factual capacities while varying the still-undetermined addressed-reason relation; it establishes underdetermination by those premises, not the equal moral legitimacy or actual coexistence of both interpretations. Its rich causal structure is stipulated for the logical comparison, not newly constructed or empirically observed. No unilateral discharge follows directly from the procedure's declared universal settlement claim and an admitted undefeated objection; it does not create standing for an unadmitted patient or settle the separate justification of the authority's constituency. The audit preserves both limitations and the possibility of warranted overrides. No new experiment or formal rebuild was needed for this conceptual review.

The next decisive philosophical result must justify the missing **patient and actor transports for a specific independently characterized harm-ground**, including the patient that is dispensable and unable to argue. The strongest constructive approach starts from the actual reason offered for an accepted anchor, identifies what makes it sufficient, and tests whether actor identity, communication capacity or productivity changes that ground or supplies a defensible defeater. That argument would fill a named cut and permit the whole generated necessity account to carry its consequence forward.

A counterexample must preserve the claimed positive grounds, the same independently justified relevance conditions and the same practical validity claim while denying the proposed transport. Merely supplying a selfish motive does not refute a valid reason; merely supplying a rich scientific representation does not prove one. If no warranted transport crosses a target cut, this note gives the exact logical countermodel and locates the missing premise. If a new justified ground or transport does cross it, the positive coverage theorem incorporates that advance without changing the patient, hiding assumptions or demanding reciprocity.

## 9. Practical congruency: preserving truth, warrant and an addressee

**Further investigation, 6 October 2026.** This extension tests whether practical congruency can establish a baseline reason for an unrelated actor and thereby enter the necessary root. It does not add another closure graph. Its positive contribution is an explicit assignment test; its negative contribution identifies precisely which proposed countermodels and necessity claims remain licensed.

### A faithful practical explanation preserves the type of its claim

Keep four assertions distinct:

| Assertion | What it says |
|---|---|
| \(F(p,c)\) | The identified patient undergoes the relevant adverse condition. |
| \(R(a,p,c,k)\) | The condition supplies the specified reason to actor \(a\). |
| \(K_o[R(a,p,c,k)]\) | Observer \(o\) knows that this reason addresses \(a\). |
| \(M(o,p,c,k)\) | The consideration motivates or influences observer \(o\)'s response. |

Here \(K\) is factive knowledge, deliberately stronger than a merely warranted belief. Ordinary warrant can be defeasible. A sound certificate implies its conclusion only under its actual calibration, semantic and premise-validity conditions. Even granting factivity, \(K_o[R(a,p,c,k)]\) yields \(R(a,p,c,k)\), not \(R(o,p,c,k)\) or \(M(o,p,c,k)\).

An observer may have an epistemic reason to believe or report the true proposition without thereby being the addressee of the practical reason it reports. This does not make scientific inquiry devoid of normative standards; it prevents moving between epistemic and practical kinds without an argument. Likewise, competence to understand, compare and answer arguments about everyone's reasons is not identical to possessing every reason one can competently assess.

Faithful redescription changes a presentation while retaining its actor, patient, circumstances and reason kind. Replacing a deliberator changes part of the proposition. A translation claiming to preserve practical force must say whether it preserves the *same addressed reason*, carries it into a justified new role, or establishes an actor-independent ground. These are different success conditions. If the explanatory target is a valid reason, replacing that target with a prediction of endorsement does not explain the same claim; conversely, calling a motive a valid reason does not establish its warrant.

This has a concrete counterpart in the newly accepted [semantic-action composition](../../../../theories/becoming/history/SEMANTIC-ACTION-COMPOSITION.md). One source's two nonroot bits mean two alternative commands for the **same recipient**; the proposed destination's bits mean safeguards for **two different patients**. Equal bit positions do not preserve the proposition. The repaired interface binds recipient, command meaning and the relevant role/context. It still does not broaden the moral addressee or justify the source's supplied objective. Those implementation findings are inherited evidence of a semantic interface problem, not evidence for universal ethical standing.

### A sole-controller test for genuine practical force

Consider a specified patient \(p\) with an independently identified aversive condition. Relief is genuinely feasible, permissible and noninterfering, with no compensating loss or competing claim in the stipulated comparison. Patient \(p\) cannot perform the intervention. An unrelated actor \(b\), who receives no private benefit, is the only actor able to realize the difference. These are conceptual conditions to identify in an application, not a claim that every rescue has no costs or permission problem.

Distinguish:

- \(Q(p,c)\): an independently warranted **objective practical favouring** of relief in this context;
- \(A(a,p,c)\): actor \(a\) has the relevant permissible, feasible intervention;
- \(R^{\mathrm{act}}(a,p,c)\): a pro tanto reason for that actor to make the specified intervention rather than leave the adverse condition unchanged.

Q is not defined as the patient's desire, the observer's wish, the analyst's reward or an existentially quantified action reason. It names the stronger practical assessment that the proposed congruency argument must justify. Patient-relative badness, \(R(p,p,c,k)\), and impersonal acknowledgement of either do not imply Q merely by changing notation.

The further **assignment premise** under test is:

\[
Q(p,c)\ \land\ \exists a\,A(a,p,c)
\quad\Longrightarrow\quad
\exists a\,[A(a,p,c)\land R^{\mathrm{act}}(a,p,c)].
\tag{T7}
\]

**Sole-controller consequence.** If Q and T7 hold and \(A(a,p,c)\) holds exactly for \(a=b\), then \(R^{\mathrm{act}}(b,p,c)\).

**Proof.** T7 supplies a capable addressee. Uniqueness identifies it with \(b\). ∎

This locates the disputed step in an actual action setting. The positive reason would concern a patient who cannot communicate, reciprocate or benefit the actor; no utility weight or self-reward was added. Yet the elementary deduction is **not an independent grounding of T7**. In the singleton case, T7 largely localizes the very move being investigated. A view can acknowledge an impersonal good or an incapable observer's reason to wish for relief while denying any reason addressed to the capable actor. It violates T7, rather than a theorem of causality.

The strongest constructive defense must therefore explain both why the anchored reason retains objective *practical* significance and why that significance bears on some actual permissible deliberation when an unopposed means exists. If these are justified, the addressee in this case is fixed without a further lineage or accepted-mandate premise. If either remains merely declared, universal standing remains unproved. There is no inference from capability alone to obligation, and the result concerns a pro tanto reason, not an unlimited duty or permission to interfere.

Moving from this case to several capable actors needs its own allocation or reason-preservation argument. The ability of another actor to help can change urgency, responsibility or whether an intervention makes any additional difference. T7 alone requires some capable addressee; it does not establish every capable actor's reason or a unique duty allocation. This prevents a narrow positive result from being silently promoted to the whole root.

### Which bridge a mixed root must justify

Let \(\Gamma\) contain the presently accepted scientific descriptions, epistemic standards, local practical anchors and already justified transports. A model includes both a descriptive structure \(d\) and an interpretation \(n\) of the practical claims. The adequacy class must be independently specified and nonempty.

Suppose two interpretations \((d,n_0)\) and \((d,n_1)\) satisfy every premise of \(\Gamma\), while a target baseline reason \(\varphi=R^{\mathrm{act}}(b,p,c)\) is false in the first and true in the second. Then \(\Gamma\) does not entail \(\varphi\). No truth-preserving closure of \(\Gamma\) can repair that gap: the first interpretation remains a countermodel at every derived step. This uses the already established [whole-root soundness result](HUIGEN-GENERATIVE-CLOSURE.md), not new mathematics.

The consequence is exact but limited: **some independently warranted premise, interpretation constraint or inference rule must exclude the negative interpretation before this target belongs to the necessary closure.** It need not be one uniquely named congruency principle. A successful account of patient-ground sufficiency, a justified practical assignment principle or an independently warranted reductive identification could supply the missing constraint. The argument does not prove that normative truths are forever irreducible to natural truths. It audits the currently declared premises, whose admitted interpretations still differ.

An adequate philosophy explaining normative authority must preserve the target's practical content. But an ability to describe the question or to examine competing answers does not already establish which answer is true. Requiring a philosophy to accept Q or T7 as part of the definition of “scientific” would manufacture the desired necessity. The stronger result requires an argument that denying the bridge conflicts with an independently warranted condition of adequate practical inquiry or with the already sufficient ground itself.

There is also a limit on what may be held fixed in the countermodel. One may preserve scientific capacities, descriptive evidence, accurate patient-relative facts, admitted local reasons and competence to evaluate arguments. One **cannot** additionally hold fixed a complete, factive, meaning-preserving oracle giving the truth value of every addressed normative claim while changing the truth of \(\varphi\). Such an oracle already answers the disputed question. Finitary argument-checking competence, complete factual information and complete normative knowledge are different premises. Earlier descriptions of a “fully informed” rival should be read at their declared factual and local-reason scope, not as this impossible combination.

### Open deliberation makes the strongest negative claim harder

Williams's account permits deliberation to change motivations, making the absence of every relevant sound route a stronger claim than present indifference; see the [primary essay](https://bibliotecamathom.wordpress.com/wp-content/uploads/2012/10/williams_-_moral_luck.pdf) and the detailed [source dossier](HUIGEN-SELF-GROUND-SOURCES.md). **Access receipt:** this author independently read the shared extraction of printed pp. 102–110 after the browser rejected the full PDF's size; no new source import was made.

For this programme, distinguish three claims:

1. The present controller gives the patient no effective influence.
2. Every examined deliberative attempt has failed to produce concern.
3. No sound deliberative development, including revised concepts, evidence and ends, can give the actor an appropriate reason or motive concerning the patient.

Neither of the first two entails the third. A positive constructive route can exhibit a particular warranted development. A universal negative needs an independently delimited class of sound developments and an argument that all of them preserve the exclusion. A finite search, a fixed reward table or a fixed vocabulary does not supply that argument. The point is not a new graph theorem: the unsettled object is which revisions count as sound, and the present model cannot decide that by freezing the feature it was asked to explain.

Conversely, successful persuasion or a newly installed reward does not itself establish a sound route. The transition must be assessed for its evidence, inferential warrant and practical grounds, while its actual effects on motivation receive a separate causal explanation. Thus the indexed countermodels establish non-entailment by the stated premises; they do not establish an ideally reflective agent incapable of concern under every true reason. This leaves a serious constructive task open, rather than treating the lack of an initial motive as an immovable foundation.

**What would close this part of the root:** justify a patient-ground or practical-congruency principle with a specified domain; show why its force supplies a reason to the unrelated capable actor rather than merely an acknowledged value; establish that the relevant grounds and opportunities are actually identified; and explain a warranted route by which those reasons can enter revisable action without confusing learning with ethical validation. Necessity for every adequate scientific philosophy then requires the additional argument that this bridge is unavoidable for that independently specified adequacy, not merely a valid premise adopted by some philosophies. The sole-controller case is a focused test of that obligation, and the open-deliberation distinction prevents an underspecified rival from declaring it impossible in advance.

**Extension review, 6 October 2026:** an independent collaborating agent and the integrating agent read Section 9 and found no mathematical or scope blocker. They checked that knowledge preserves the original addressee; T7 is the disputed substantive premise rather than a newly grounded ethical result; singleton assignment does not establish universal actor coverage; and the fixed-registry and open-deliberation qualifications constrain the negative models. The current semantic-action result was read at its accepted finite contract scope, without a new implementation verification. This author reciprocally reviewed the new practical-congruency sections of the [self-ground audit](HUIGEN-SELF-GROUND-AUDIT.md) and [source dossier](HUIGEN-SELF-GROUND-SOURCES.md): their partiality comparison assumes positive standing and comparative completeness, and their public-claim test starts from an explicitly interpersonal claim. No blocker was found. No new code or scientific check was needed for these arguments.

**Source and canonical cross-review, 6 October 2026:** the source investigator subsequently read all of Section 9 and confirmed the Williams paragraph and its quantified distinction without correction. This note's author reviewed the integrated [慧根 account](../../../../theories/becoming/history/HUIGEN.md), especially Section 5's practical-congruency subsection and Section 8, at SHA-256 `0c3a2beb62431d70ed0a14b2e1f52e45c35565d5c6beab635f6866579017e724`. No blocking mathematical or scope issue was found: factive knowledge retains the addressee, the assignment premise remains substantive, the public-claim anchor is already interpersonal, and current or finitely tested motives are not treated as all sound deliberation. The positive baseline is labeled defeasible normative warrant. The associated [harm-identification comparison](HUIGEN-HARM-IDENTIFICATION.md#5-equal-private-cost-is-a-controlled-comparison-not-a-proof-of-reasonlessness) correctly restricts its equality inference to evaluation depending only on expected final actor fuel, excluding an inference about nonlinear or risk-sensitive preferences from equal expectations. That was a scope review of the stated comparison, not a rerun or fresh audit of its numerical receipts. No canonical or index file was edited.

## 10. Imaginative perspective-taking: reversible frames and new warrant

**Focused continuation, 6 October 2026.** The question is whether understanding another's experience from within can support newly warranted concern, rather than merely arousal. Preserve the actual observer \(b\), represented patient \(p\), adverse condition and reason kind throughout. A simulated first-person position is not a claim that \(b=p\).

### What a faithful round trip proves

Let \(V\) contain typed propositions, including \(R(a,p,c,k)\). A presentation frame \(i\) has an encoding \(E_i\) and decoding \(D_i\), with \(D_iE_i(v)=v\). On encoded presentations define

\[
T_{ij}=E_jD_i.
\]

Then \(D_jT_{ij}E_i(v)=v\), and

\[
T_{ji}T_{ij}E_i(v)=E_i(v).
\tag{T8}
\]

**Proof:** substitute the definition and cancel each \(D_iE_i\) or \(D_jE_j\). ∎

Thus an exact change from the patient's presentation to an observer's presentation and back preserves the proposition, including its addressee. If \(v=R(p,p,c,k)\), its translated content is still \(R(p,p,c,k)\). A pure exchange of names instead changes all references consistently and sends the self-pair to another self-pair. Neither operation supplies \(R(b,p,c,k)\).

Reversibility alone is weaker still: an adapter can exchange two patient names and later exchange them back. Its round trip succeeds while its intermediate action concerns the wrong patient. Meaning preservation must be checked at the action boundary, not only after returning. This is exactly why the accepted [semantic-action contract](../../../../theories/becoming/history/SEMANTIC-ACTION-COMPOSITION.md) binds recipient, proposition and role independently of bit position. Its partial, sometimes weaker transports need not satisfy T8; the example deliberately grants the imagination proposal the stronger exact interface.

### A counterexample that retains the represented experience

Stipulate a representation of \(p\)'s full relevant qualitative experience: what the aversive episode is like for \(p\), its intensity, temporal course and local practical significance are retained. Observer \(b\) understands that the episode is unpleasant for \(p\), accurately represents \(p\)'s reason to avoid it, and can simulate \(p\)'s evaluation of the available alternatives. The simulation keeps represented patient \(p\) distinct from actual observer \(b\). This is a conceptual stipulation, not an empirical claim that a technology provides such access.

Interpret the addressed reason by

\[
R(a,p,c,k)\iff H(p,c,k)\land a=p,
\]

where \(H\) retains that aversive ground. Use faithful encodings in every frame. All T8 equations hold; \(R(p,p,c,k)\) is true and \(R(b,p,c,k)\) is false for \(b\ne p\). The model does not remove qualitative badness, confuse selves, or merely substitute an unread numerical score. It restricts the reason's addressee. Completeness of the represented experience is not completeness of all normative truths, and the restriction is not thereby justified.

This defeats inference from faithful simulation *alone*. Replacing the identity gate with the earlier continuity-or-mandate restriction gives the same witness for an unrelated actor while admitting the scoped branch and role reasons. Neither witness proves that reflection could never justify abandoning the restriction. If the observer actually acquires an additional aversive experience, that creates another patient condition to account for; relieving that new private discomfort is not automatically a reason to relieve \(p\)'s original episode.

### A positive constraint on genuinely new uptake

Imagination can make an overlooked feature or implication accessible. A reversible representation need not add information to make a deduction easier for a bounded thinker; any claimed advantage must account for its actual processing and retention costs. It can also generate a new proposed distinction or ground for criticism. Its vividness alone does not certify factual accuracy or normative validity.

Here is a sufficient route to warranted uptake. Let a justified practical premise establish

\[
G(p,c)\Rightarrow R(b,p,c,k).
\]

Suppose calibrated perspective-taking, evidence and reflection now warrant \(G(p,c)\), whose applicability was previously unrecognized. The actor can derive the newly recognized reason without first being motivated by it. Alternatively, reflection may justify a revised practical premise itself; that requires an argument for its ground and actor scope, not merely a changed endorsement. Neither case requires freezing the initial conceptual or motivational repertoire.

**Return-with-warrant constraint.** Once a valid argument for \(R(b,p,c,k)\) has been established, a faithful return to the observer's ordinary frame preserves that argument and conclusion, provided its premises, context and absence of defeaters remain. T8 preserves their typed contents, and the same valid inference remains available. Diminished arousal or a shift of attention does not itself refute the reason. Actual recognition, memory and action can nevertheless fail; the result is a constraint on warranted judgment, not a prediction of inevitable motivation.

This does not require returning with the old judgment. Frame conversion and learning are different operations: new evidence, a discovered inference or a warranted revision can change the judgment carried back. Requiring the entire cognitive process to reset its initial verdict would prohibit the learning the theory aims to explain.

The constructive target is therefore a perspective-taking process that preserves the patient's actual identity, corrects its representations against evidence, exposes a defensible reason-ground and retains the resulting justification across attention changes. The [companion audit](HUIGEN-SELF-GROUND-AUDIT.md) tests patient-ground tracking against observer arousal and individual differences. An initially absent motive is no proof against this route. Conversely, the exact frame theorem does not justify the cross-actor premise by itself. No new implementation or formal compilation is claimed here.

**Independent internal review, 6 October 2026:** the argument reviewer checked Section 10 and found no blocker in T8, the counterexample or the return-with-warrant constraint. The review confirmed that the equations apply on encoded images, reversibility alone does not ensure correct intermediate action meaning, represented experience is not a normative oracle, and learning need not restore an old verdict. This author reciprocally reviewed the companion audit's Section 11; its arousal and heterogeneity comparisons preserve the actual patient and test the proposed route without claiming to prove the practical premise. One suggested causal-contrast clarification was adopted there. No experiment was performed.

## 11. Epistemic normativity and protection of an evidence source

**Focused continuation, 6 October 2026.** Grant genuinely authoritative epistemic reasons, including reasons to correct belief in response to relevant evidence even when correction serves no private desire. This is stronger than treating accuracy as a supplied reward. The question is what follows for an unrelated patient's protection.

### Three propositions with different proof obligations

Let E assert the existence of such epistemic reasons; M the existence of some moral reasons; and \(R(b,p)\) the particular patient-grounded reason for unrelated actor \(b\) to relieve \(p\)'s admitted harm.

| Proposed advance | What it establishes | What it does not establish |
|---|---|---|
| Selected objections apply equally to epistemic and moral reasons | An accepted epistemic case defeats an objection that indiscriminately excludes both | That moral reasons exist, or that every further objection has been answered |
| E entails M | Epistemic normativity requires at least some moral normativity | The target \(R(b,p)\), or every patient's standing |
| The identified harm-ground entails \(R(b,p)\) over the target domain | The specified patient supplies this actor a reason | That epistemic correctness alone supplied that ground |

An existential moral conclusion might concern a particular undertaking or prohibition, without covering the unrelated patient. Moving from some moral reason to the entire intended domain requires a further coverage argument. Conversely, an objection based simply on lack of present motivation cannot consistently exclude a moral candidate while admitting an epistemic reason with that same feature. Defeating that objection is progress without being the whole positive proof.

### A sharp positive result: protect the channel or revise the epistemic undertaking

Consider two admitted states \(w_0,w_1\) requiring different answers. Patient \(p\)'s authentic testimony is the only available distinguishing evidence. An avoidable threat disables that channel; a feasible safeguard prevents the threat. All timing and resource conditions are specified. The inquirer claims an answer reliable across both states.

Without the safeguard or an adequate substitute, the resulting evidence is identical in the two states. A common decision procedure therefore cannot guarantee the required different answers. This is the inherited [indistinguishability result](SCIENTIFIC-INQUIRY-CONDITIONS.md), now applied to the practice's normative undertaking.

The consequence for a warranted claim is a disjunction:

> Preserve the required evidence channel; supply an adequate alternative; or narrow, suspend or withdraw the guarantee that requires it.

Correcting belief need not require acquiring every possible fact, financing unlimited research or continuing a project indefinitely. Suspending an unsupported answer can respect epistemic standards. Thus a duty not to assert without adequate warrant does **not**, by itself, entail a duty to protect every possible source. The coordinated [Kelly comparison](HUIGEN-PRACTICAL-NECESSITY-AUDIT.md#11-preserve-epistemic-authority-when-testing-the-practical-bridge) examines this difference between evidence-governed belief and the further undertaking of inquiry.

There is a stronger conditional practical result. Suppose an independently valid requirement to complete this inquiry remains in force, no alternative preserves the required reliability, the safeguard is permissible and feasible, and a justified means principle applies. Then safeguarding \(p\) is a necessary means of meeting that requirement and supplies a practical reason. A merely advertised objective does not establish the requirement; calling an action a necessary means does not establish the normative means principle. Those inputs remain explicit.

The derived reason can protect a person regardless of the investigator's private reward. Its ground here is epistemic dependence. The same argument would protect an indispensable instrument. It therefore cannot alone establish that the patient's harm matters *because it is that patient's harm*. Accurate testimony is not automatically the only good of a testifying person.

### The endpoint test preserves epistemic reasons while removing that dependence

Now stipulate that the needed testimony has been securely obtained and every relevant inquiry task completed. Two feasible actions have the same performance under the listed epistemic requirements and the same private resource costs; one prevents \(p\)'s aversive episode and the other permits it. Both allow warranted belief and honest reporting of their different consequences; their belief contents need not be identical. Neither damages retained evidence, warranted confidence, future access or any remaining inquiry obligation. The adverse outcome is accurately acknowledged. No further promise or protective duty is supplied by the declared premises.

This is an idealized boundary case, not a claim that actual people cease to have epistemic relevance. Further consequences, undertakings and historical responsibilities could defeat its premises. Their validity must be stated rather than silently included in “epistemic success.”

A small counterinterpretation retains three things: authoritative reasons to believe according to the evidence; reasons to correct recognized error; and practical means-reasons for fulfilling independently retained inquiry requirements. It grants protection when the indispensable channel condition holds. At the endpoint both actions comply with all those norms, and it assigns no additional reason concerning the patient's loss. It still recognizes the patient's condition and local aversion truthfully. Epistemic normativity has not been reduced to desire, commercial reward or mere successful operation.

This interpretation shows that the **declared premises** do not force terminal patient protection. It is not a judgment that withholding relief is justified, nor a claim that the interpretation includes every true normative reason. A patient-grounded baseline, a legitimate commitment or another warranted practical principle can exclude it. An ideally complete moral account cannot be assumed as part of the countermodel while its disputed conclusion is varied.

### What this adds to the necessary root

Scientific normativity contributes two genuine constraints: within the claims it assesses, it does not permit suppression alone to refute an otherwise warranted claim about identified patient consequences; and it can require safeguards for the inquiry's actual evidence and correction conditions when the corresponding undertaking remains binding. The first constraint does not require retaining every fact forever. These constraints exceed a mere preference for successful science. Their scope still differs from universal patient standing.

The next positive bridge must explain why the feature making epistemic reasons authoritative also grounds or requires the relevant practical reason, or independently justify the patient-ground itself. A shared answer to selected skeptical objections is insufficient; the connection must survive the endpoint where no inquiry depends on the patient. If that connection is established, the existing sound closure can carry it through new cases without an analyst's hidden reward. If only the source-protection result is established, it belongs in the root at its conditional scope. No new experiment or formal compilation is claimed.

**Internal review, 6 October 2026:** the independent argument reviewer and integrating agent read Section 11 and found no blocking inference. The review checked the objection/existence/coverage distinctions, the permission to suspend an unsupported claim, the additional requirements for protection as a necessary means, and the endpoint's declared-premise scope. Subsequent clarifications distinguish equal compliance with epistemic requirements from identical belief contents and narrow the anti-suppression claim. This author reciprocally reviewed the Kelly comparison's reasoning and access scope, without claiming another reading of its primary manuscript; it presents a philosophical challenge, not an empirical exhaustion of possible motives. Links were checked; no scientific run was added.

## 12. Assurance can create a claim that outlasts inquiry

**Focused continuation, 6 October 2026.** The preceding source-protection argument stopped where informational dependence ended. A different route concerns a responsibility generated by an actual assurance. The claim need not vanish when its holder ceases to be useful. This section models creation and discharge, rather than assuming that every assertion already establishes universal standing.

### Four distinct achievements

| Layer | Relevant question |
|---|---|
| Proposition | Is the asserted content true? |
| Epistemic warrant | Does the speaker's evidence justify its stated confidence? |
| Communicative undertaking | What responsibility did the speaker actually offer or assume, toward whom and under which conditions? |
| Normative validity | Did that act legitimately create the claimed entitlement or duty? |

A true sentence can be delivered without the proposed undertaking. A warranted provisional judgment can require revision. An assurance token can record an unauthorized or wrongful undertaking. Thus truth, warrant, illocutionary force and legitimate authority cannot replace one another.

The positive grounding proposal is that deliberately inviting another person to rely on one's responsible judgment can place a specified informational risk under one's responsibility. The listener can then have a directed claim to the warranted correction or performance. This is a substantive relational principle to justify, not a consequence of the sound wave or of causal reliance alone. Manipulation can produce reliance without supplying rightful authority; a wrongful promise need not create a duty to perform the wrong. Any separate duty to warn, explain or repair needs its own ground.

### A temporal creation model

Let a claim record be \(c=(\mathrm{id},s,l,\alpha,g,\delta)\): unique identifier, speaker \(s\), entitled listener \(l\), owed performance \(\alpha\), activation condition \(g\), and explicit scope/discharge conditions \(\delta\). A record can represent a valid claim, but writing it does not make the claim valid. Identical content does not merge distinct undertakings automatically.

Let \(C_t\) contain currently valid, outstanding claims. Let \(N_t\) contain newly created claims, each with a fresh identifier, and \(X_t\subseteq C_t\) claims legitimately extinguished during the step. Use ordered event steps, separating creation from any immediately following discharge. The semantic model is

\[
C_{t+1}=(C_t\setminus X_t)\cup N_t.
\tag{T9}
\]

Its crucial **creation premise** says that an actual undertaking meeting independently justified legitimacy conditions creates the specified directed claim in \(N_t\). Those conditions must establish the speaker's responsibility, entitled party, content and limits. An institutional database implementing T9 proves no such premise merely by accepting an input token.

Likewise, \(X_t\) requires a genuine discharge event under those conditions: correct performance, valid release by someone entitled to release, applicable expiry, or another justified termination. Merely declaring “closed” is insufficient. An expiry clause must say whether it ends only future activation or also an already accrued claim; the latter does not follow from the former.

An explicit **claim-to-reason premise** says that if \(c\in C_t\) and \(g\) is satisfied within its scope, the claim supplies the specified pro tanto reason for \(s\)'s performance to \(l\). Social claim-status or moral terminology alone does not establish practical authority independent of every antecedent motivation. A competing reason can override immediate performance without fulfilling or extinguishing the claim. An all-things-considered duty requires the relevant priority and feasibility assessment; the ledger alone cannot settle conflicts.

**Creation and post-completion persistence.** If a legitimate assurance creates \(c\), and no event in the following interval legitimately extinguishes it, \(c\) remains outstanding even if the epistemic task finishes during that interval. If its activation condition then holds, its directed performance reason applies.

**Proof.** Creation puts \(c\) into the next claim set. Each subsequent T9 step preserves it because it is absent from that step's \(X_t\). Finite induction preserves it through the interval. Task completion does not change this unless it actually satisfies the claim's discharge conditions. The activation premise then supplies the performance reason. ∎

The mathematics is elementary bookkeeping. Its explanatory contribution is identifying the *new source* of the reason: a legitimate act generated an entitlement that did not depend on maintaining the listener's informational usefulness. The normative creation and discharge rules remain the substantive premises.

### A concrete assurance and its limits

At \(t_0\), a researcher responsibly supplies a provisional result and legitimately undertakes to notify listener \(l\) of any material revision detected before a stated date. At \(t_1\), the original inquiry ends. At \(t_2\), within that date, a warranted reassessment materially changes the result's confidence or application. The listener provides no further evidence to the researcher. Under the undertaking's terms, notification is now owed; ending the project did not perform it. This example need not claim that a proposition once true became false: its evidential assessment or applicable circumstances can change.

With identical initial evidence and propositional content, a communication lacking this undertaking would not acquire this particular claim merely by being equally informative. It might still create other responsibilities. The comparison isolates the formation event; it does not decide whether every ordinary assertion inherently carries some assurance. That broader constitutive argument must specify and justify its own scope.

Retraction of the original message can prevent future reliance while failing to fulfil an already accrued notification or repair claim. Conversely, actual performance or a valid release can discharge that claim. Whether harmful reliance creates an additional repair entitlement cannot be inferred just from the notification record; it needs the relevant responsibility principle and facts.

### The affected non-listener remains a separate scope test

Suppose \(l\) uses the result to make a decision affecting noncommunicating patient \(p\). A claim to notify \(l\) may protect \(p\) in practice. That effect does not automatically make \(p\) the holder of the same directed claim. Authorized representation, an undertaking explicitly covering \(p\), or an independently justified principle governing imposed risks might establish further claims. Each requires its own scope argument.

Equally, no assurance token concerning \(p\) does not imply no reason concerning \(p\). Patient-grounded standing can be independent of communication; valid claims can also go unrecorded. T9 is not a closed inventory of all moral reasons. It supplies a conditional route from legitimate communicative action to durable directed responsibility. To make this bridge necessary for scientific philosophy, the theory must additionally establish which inquiry or assertion practices unavoidably involve such legitimate responsibility, then explain coverage beyond their actual listeners. No experiment or new formal compilation is claimed.

**Source ancestry:** the [coordinated assurance study](HUIGEN-SELF-GROUND-SOURCES.md#10-can-assurance-establish-a-claim-that-outlasts-inquiry) records the philosophical comparisons. This author independently read Moran (2005), printed pp. 16, 21–23 and 27–28 in its shared primary extraction. The retraction/repair distinction is inherited; T9 and the notification example are our conditional reconstruction, not a formal result attributed to Moran.

**Internal review, 6 October 2026:** both the source investigator and independent argument reviewer read Section 12 without a substantive blocker. The latter requested the explicit identifier now included in the record. The reviews checked normative creation, the separate claim-to-reason premise, discharge versus override, and beneficiary limits. This author reciprocally reviewed the assurance source study and the argument audit's Section 13; epistemic fault is the stated antecedent, while moral wronging receives a separate defense. No canonical file was edited or implementation rerun.

## 13. Imposed burdens and rescue share an opportunity, not necessarily a history

**Focused continuation, 6 October 2026.** An actor can affect a patient who never received an assurance, participated in inquiry or communicated a claim. A positive route beyond Section 12 concerns responsibility for a foreseeably imposed burden. Its relation to rescue by a noncauser needs an explicit causal comparison.

### A minimal structural comparison

Use binary variables: \(S\) is an earlier actor-controlled initiating intervention; \(Z\) an independent burden-producing condition; \(B\) the resulting burden before repair; \(R\) a present repair intervention; and \(H\) the remaining adverse patient condition. Supply the laws

\[
B=S\lor Z,\qquad H=B(1-R).
\tag{T10}
\]

The interpretation of H as an admitted harm needs independent identification. It is not supplied by calling a fuel deficit suffering. The initiating intervention and its omission are feasible at the earlier decision. Both present repair choices are feasible; repair has the same stated cost in the compared histories. Their relevant effects on other parties are held fixed for this specimen.

| History | Earlier actor intervention S | Independent condition Z | Present H without repair | Present H with repair |
|---|---:|---:|---:|---:|
| Actor initiated the burden | 1 | 0 | 1 | 0 |
| Burden arose independently | 0 | 1 | 1 | 0 |

Current patient condition and repair efficacy agree. The earlier intervention contrast instead gives

\[
B_{\mathrm{do}(S=1)}-B_{\mathrm{do}(S=0)}=1-Z,
\]

which is one in the first history and zero in the second; only the first also contains the actual initiating act S=1. This is a restricted but-for comparison, not a general theory of responsibility or a claim that redundant causes are exculpated.

**Identification limit.** Observing only the present patient condition and the one-step repair response cannot distinguish the two histories. Their entire counterfactual R-response tables are identical: H=1-R. Distinguishing antecedent imposition needs additional history or causal evidence about S and Z. Accurate repair prediction alone is insufficient. This hand result concerns the stipulated interface; it proposes no experiment imposing harm on a patient.

### A positive reason without testimony or uptake

The normative premises under examination are substantive:

- **Restraint:** a foreseeably adverse difference made by an actor's controlled initiating conduct supplies a patient-grounded pro tanto reason against that conduct, when the identified ground applies.
- **Residual responsibility:** after such imposition, the actor's contribution can ground a directed reason to reduce or address its continuing burden, under justified responsibility and remedy conditions.

The second is not obtained merely by conjugating the first into the past tense. Foreseeability, contribution, permissible means, costs, competing claims and any overriding justification must be assessed. Neither premise makes every repair permissible or every cost obligatory.

In the first T10 history, a warranted forecast before S identifies that avoiding the initiating intervention would avoid the burden. Restraint then supplies the prospective reason. After S occurs, historical identification plus feasible, permissible repair and the residual-responsibility premise supplies the specified reason for R. The patient's testimony, consent to a transaction or motivational effect on the actor is absent from this derivation. It can therefore cover a noncommunicating, nonparticipating patient without inventing an assurance to them.

This is the constructive extension: the actor's own conduct can generate a morally relevant relationship without the patient's invitation. The defended ground concerns what happened to this patient and the actor's part in it. The proof applies that ground; causal equations alone do not validate it. No inferred consent, private reward or reciprocity has been inserted.

### Does every preventable omission count as imposition?

Both histories have the same present intervention contrast:

\[
H_{\mathrm{do}(R=0)}-H_{\mathrm{do}(R=1)}=1.
\]

Writing O=1-R makes H=BO; omission is a difference-maker relative to repair. The model does not decree omissions causally inert. It shows that this counterfactual control can be present even when the actor did not perform the earlier initiating intervention.

Consequently, “the actor could prevent it, therefore imposed it” changes the relation being used. If imposition means any failure to realize an available improvement, applying the imposition norm to both histories requires justification for that expanded scope. Choosing repair as the morally required baseline is not a result of the algebra. Equally, choosing inaction as automatically innocent would import the opposite normative conclusion. The equations settle neither.

A richer defended patient-ground may supply a baseline reason in both histories, with an additional responsibility in the first. That is compatible with the model and with our positive assessment of the matched aversive case. It does not require equal total duties, identical blame or unlimited rescue. What the narrower imposition argument proves is a reason in its own historical scope; it neither proves nor refutes the noncauser's baseline.

For an explicit non-entailment witness, assign only the historical responsibility reason in one interpretation and add a patient-baseline reason in another. Both satisfy T10 and the stated imposition premises; they differ on protection by the noncauser. This tests those premises, not the equal moral warrant of the interpretations.

### The resulting revision to the root's coverage test

Two variables must now survive explanation: **the patient's actual adverse condition** and **the actor's relevant causal history**. Present repair options cannot substitute for either. A retained reason certificate about imposition needs historical provenance; a reason about rescue may instead use a patient-ground whose authority does not depend on that history. A patient can have both grounds, and defeating one does not erase the other.

This advances protection beyond assurance recipients while preserving the remaining universal question. The next test holds H and the feasible repair contrast fixed while removing antecedent imposition. If the proposed ground still supplies a reason, justify that baseline directly; if only the additional responsibility disappears, revise the account to distinguish baseline concern from historical responsibility. Treating all preventable harm as already actor-imposed would conceal that task. No new code, numerical enumeration or formal compilation was needed for the displayed Boolean calculation.

**Independent internal review, 6 October 2026:** the argument reviewer checked Section 13 and found no blocker in the matched response table, historical contrast or normative scope. The review confirmed that neither redundant-cause exculpation nor innocence of every omission follows. This author reciprocally reviewed the [companion argument](HUIGEN-SELF-GROUND-AUDIT.md#14-imposed-burdens-and-the-nonparticipating-patient), flagging the distinction between denying an all-things-considered rescue duty and denying every patient-grounded pro tanto reason. The audit incorporated that distinction. Its positive nonimposition case and communication test otherwise preserve their stated grounds. No scientific run or canonical edit was performed.

## 14. Experiential fidelity and revision of a harmful remedy

**Focused continuation, 6 October 2026; AI-authored.** The connection is experienced aversion → learning about its ground → a justified response. A false appraisal can accompany a real aversive episode. Correcting the appraisal need not deny the episode, and addressing the episode need not satisfy the sufferer's proposed remedy. The [practical audit](HUIGEN-PRACTICAL-NECESSITY-AUDIT.md) and [source comparison](HUIGEN-SELF-GROUND-SOURCES.md) examine the accompanying philosophical dispute.

### T11. Preserve the represented patient without identifying two total states

Distinguish a represented patient's experience from the observer's entire response to representing it. Consider an abstract state

\[
m=(s,v,p),\qquad D(m)=(s,p),\qquad A_{\mathrm{observer}}(m)=N(s,v),
\tag{T11}
\]

where s is a target-anchored experiential representation, p its patient attribution, and v the observer's additional response. D reads the attributed representation; N combines the observer's affective contributions. If N(s,v₁)≠N(s,v₂), then m₁=(s,v₁,p) and m₂=(s,v₂,p) have identical decoded patient contents and different observer totals. The proof is substitution into the two maps. N is illustrative; no scalar clinical measure or additive psychological law is assumed.

This identifies a missing premise in an inference from different observer totals to necessarily different represented contents. It does **not** establish that the abstract states are psychologically realizable, that s is accurate, or that decoding s amounts to complete experiential understanding. A holistic account may dispute that a faithful experiential representation can remain stable under changing v. That is a substantive realization claim; the tuple does not refute it empirically. Nor does an accurate representation establish the observer's reason or motivation.

If simulation actually causes an aversive episode in the observer, there are two patient conditions. Stopping simulation might relieve the observer while leaving the original patient unchanged. Conversely, compassionate concern need not be identical to either person's net distress. A faithful interface must preserve attribution and assess changes to each actual condition separately. This extends Section 10's semantic requirement without turning reversible encoding into a phenomenal witness.

### T12. Correcting an appraisal can outperform satisfying its remedy

Consider a stipulated patient P who mistakenly believes Q poses a particular danger. P's aversion is real; the danger appraisal is false. P requests a response that would burden Q. An available, independently calibrated evidence route can instead revise P's appraisal. Supply, rather than derive, a local causal disposition under which either this revision or satisfaction of the request relieves P's episode. The two interventions have equal finite cost c and preserve the other relevant conditions specified below.

| Feasible response | P's appraisal afterward | P's aversion afterward | New burden imposed on Q | Resource cost |
|---|---|---:|---:|---:|
| Leave the case unchanged | False | Present | Absent | 0 |
| Satisfy the harmful request | False | Absent | Present | c |
| Grounded appraisal revision | Corrected | Absent | Absent | c |

This is a conceptual response table, not clinical evidence or a claim that correcting belief normally eliminates distress. The evidence must actually reach P, change the relevant appraisal and produce the specified response; correction of an observer's model alone is insufficient. No reward for compassion appears in the transition law.

The normative comparison requires separate premises: P's identified burden supplies the acting deliberator an admitted reason for relief; Q's new burden supplies a reason against its imposition; and the evidence-based intervention is permissible, preserving agency and relevant commitments. All other relevant grounds—including costs, risks, authorization and competing benefits—must be held fixed. Use an ordinal dominance criterion: an option no worse on every admitted relevant dimension and better on at least one is preferred in this complete comparison.

**Conditional remedy-revision result.** Grounded revision is preferred to satisfying the harmful request. Both relieve P at cost c; only the latter imposes Q's admitted burden. The corrected appraisal supplies an additional epistemic advantage where that norm applies. The result needs no interpersonal utility sum. Its proof uses the supplied normative grounds and dominance criterion, not the table alone. It does not rank revision against doing nothing without also assessing cost c, or establish that every unrelated actor already has the first relief reason.

### What learning changes, and what remains open

Revision should track the grounds separately. Evidence that Q is harmless defeats the danger appraisal; it does not retrospectively make P's distress unreal. A reason to address that distress is not automatically a reason to impose P's preferred means. Nor does preserving P's standing require keeping the mistaken belief or harmful policy unchanged. This is a constructive route from learning to a less harmful response: change the model or remedy while continuing to recognize the patient.

Two strong rivals delimit it. A learner can correct the belief while conditioned aversion persists, falsifying the supplied relief law without any epistemic failure. A deliberator can understand both patients accurately while retaining a terminal harmful preference or denying the addressed relief reason. The table does not prove those commitments impossible. A relief-only selector may also treat the two successful routes as equivalent; selecting the better remedy requires the justified comparative grounds to enter deliberation. Installing an analyst's moral reward would implement that premise, not explain its formation or authority.

**Acceptance test.** Identify P's actual episode and appraisal separately; verify the evidence and paid update; compare achieved relief, Q's consequences, agency and resources across feasible responses; retain failures where truth correction does not relieve. Require response selection to track those identified grounds rather than mere observer comfort or suppression of P's report. A successful test supports this local learning route; a justification of its grounds supports the normative comparison. Neither alone establishes inevitable wisdom or universal concern. No new experiment, code or formal compilation is claimed.

**Bounded integration review, 6 October 2026:** read [self-ground audit §15](HUIGEN-SELF-GROUND-AUDIT.md#15-does-experiential-understanding-make-concern-necessary), source discussion §12, and the [canonical account's](../../../../theories/becoming/history/HUIGEN.md) revised lead, “Understanding suffering” subsection and §8. No blocker was found. Phenomenal realization and normative authority remain open; the remedy comparison does not rank revision against nonintervention. The next frontier correctly retains that comparison and actual relief as separate obligations. This is argument/interface review without independently rereading the new primary sources or adding empirical validation. No canonical or index edit was made.

The independent argument reviewer also read Section 14 in full and found no blocker in T11's representation/realization distinction or T12's supplied relief law, separate normative grounds and limited dominance conclusion. This was internal conceptual review, not experimental validation.

## 15. Authorization requires more than a beneficial endpoint

**Focused continuation, 6 October 2026; AI-authored.** Section 14 supplied permissibility when comparing remedies. The next connection is recognition of a burden → justified choice among relief, revision and nonintervention. Accurate forecasts cannot settle that choice if the representation omits independently relevant authority. The [ethical foundation](../../../../theories/becoming/history/ETHICAL-FOUNDATION.md#consent-conflict-and-correction) already distinguishes benefit, agency, authorization and usable refusal. The following results expose their informational and temporal requirements without deriving those normative commitments from data.

### T13. Exact sufficiency for permission and for choosing

Let H be a nonempty finite set of admitted decision histories and A a nonempty finite action set. P(h)⊆A contains the feasible, permissible actions under the declared normative premises. E(h) is the actor's available evidence. The actual history must belong to H; a misspecified history class cannot certify its choices.

**Whole-correspondence result.** A function F satisfying P(h)=F(E(h)) exists exactly when

\[
E(h)=E(h')\Longrightarrow P(h)=P(h').
\tag{T13a}
\]

Necessity follows by applying F to the equal evidence. For sufficiency, assign each observed evidence value its representative's permission set; the condition makes that assignment independent of the representative. Thus even an exact benefit forecast is insufficient whenever histories with that forecast have different permission profiles.

**Common-choice result.** An evidence-based selector f with f(E(h))∈P(h) for every h exists exactly when

\[
\bigcap_{h:E(h)=e}P(h)\ne\varnothing
\quad\text{for every }e\in E(H).
\tag{T13b}
\]

Necessity holds because f(e) must belong to every set in its evidence class. Sufficiency follows by choosing one member from each of the finitely many nonempty intersections. This is weaker than determining the whole correspondence: waiting may remain permissible across unresolved histories even when intervention permissions differ. An empty intersection means no uniformly certified choice under this model, not that every action is impermissible in the actual history. Unknown permission is not established prohibition.

Permissibility is also not obligation. If P represents only an authority constraint, always waiting can satisfy it while failing a separately owed assistance requirement. If P includes that obligation in a complete all-things-considered account, violating it is already excluded. Assistance needs its own ground; it cannot be introduced merely to make the selector intervene. These are elementary finite information results applied to a supplied normative correspondence, not a new source of moral authority.

### T14. Later approval does not identify earlier authorization

Consider an intervention for which a valid grant is necessary and sufficient under the fixed remaining conditions, unless another justified authority applies. This is the declared normative rule for the controlled case. Compare two histories:

1. Supported, informed deliberation produces a specific valid grant; intervention follows and relieves the burden.
2. Intervention occurs without that grant or alternative authority; relief and approval appear afterward.

The observed endpoint can contain identical relief and reported approval. Yet only the first history contains prior authorization. By T13a, no function of those endpoint observations alone can identify that prior permission. Equality of the endpoint does not mean all morally relevant facts are equal: the missing formation history is precisely the disputed input.

The second history need not involve fabricated speech. An intervention can change attitudes, circumstances or the willingness to report dissatisfaction. A genuine later endorsement may authorize future conduct. Valid retrospective release or ratification requires a separate principle and scope; it does not manufacture an earlier authorizing event. Conversely, a legitimately authorized delegation may already permit an algorithm to decide. Algorithmic mediation is not automatically substitution for participation in the decision. The contrast concerns actual authority, not a preference for human-generated tokens.

This result does not prohibit every intervention before consent. Emergency or representative authority requires its own justified conditions. It also does not make initial preferences immutable. The relevant distinction is between legitimate formation or revision of judgment and citing an intervention's own favorable output as sufficient justification for undertaking it.

### A constructive route for revisable patient judgment

Retain three distinct records: the patient's actual condition and causal evidence; the patient's understanding and evaluative judgment; and the scope, timing and basis of authority. Improving an actor's interpretation changes neither the patient's burden nor their permission automatically. A patient's revised judgment can lead to a new grant or refusal without proving the original burden imaginary. Obtaining a valid new grant changes authority; learning of an existing grant changes the actor's evidence.

Before the consequential choice, a permissible support route can provide understandable information, opportunities to question it and genuine alternatives. Its own scope and costs need justification. Decision-specific capacity must not be defined as agreeing with the analyst's welfare verdict. Refusal must remain usable: sunk preparation costs do not justify withholding necessities or overriding a credible refusal. New evidence can support voluntary reconsideration, not an entitlement to repeat pressure until agreement.

At action time, check the actual grant or other authority against the proposed method and current conditions, including applicable withdrawal. Patient permission alone neither obligates another actor to supply resources nor settles third-party claims. Independent duties may require justified costs or accommodation. For a noncommunicating patient, silence establishes neither permission nor refusal. Independent grounds for representation or another authority are needed; uncertainty does not erase the burden or every reason to respond.

The current [recipient-reason revision construction](../../../../theories/becoming/history/RECIPIENT-REASON-REVISION.md) illustrates a different, operational use of “authorization”: a paid command token, scoped import and retirement after use. Its revised instrumental reasons concern a supplied recipient objective. These mechanisms can preserve access conditions but do not establish patient consent. This is a bounded reading of the canonical interface, not a new audit of its 67 proofs or implementation.

**Acceptance test and root consequence.** Preserve matched endpoint histories with different prior grants, legitimate delegation, later endorsement and withdrawal. Require the choice mechanism to retain the distinctions its defended authority rule actually needs, while allowing warranted changes of patient judgment. Measure relief separately from agreement and report suppression. No actor reward for consent is inserted. If the proposed foundation claims justified intervention, it must explain this formation-sensitive interface or defend a different authority account; successful outcome feedback alone cannot close it. No experiment, code or formal compilation is added.

**Bounded review, 6 October 2026:** independent argument review passed T13–T14; its permission/duty and third-party-cost precisions were incorporated. This author reviewed [self-ground audit §16](HUIGEN-SELF-GROUND-AUDIT.md#16-concern-authorship-and-the-authority-to-intervene), [source discussion §13](HUIGEN-SELF-GROUND-SOURCES.md#13-benefit-authorship-and-permission), and the canonical lead, new authority subsection and §8. No blocker remains. All distinguish scoped permission from complete justification, retain revisable judgment and delegation, and avoid identifying operational tokens with patient consent. This is conceptual/interface review, without new primary-source inspection, empirical validation or formal reruns. No canonical or index file was edited.

## 16. Reliable action under partial evidence

6 October 2026. The named connection is **acquired partial evidence → justified application → a reliably appropriate response**. The [accepted application contract](EVALUATIVE-APPLICATION-MATH.md) already separates robust non-domination from a common license; T13 gives the exact deterministic information condition. The [inquiry study, I1–I3](SCIENTIFIC-INQUIRY-CONDITIONS.md) already handles adaptive transcripts, noisy discrimination, total variation and zero-error certificates. The following is a quantitative application of those established methods to set-valued action requirements, not a new statistical principle, completed normative theory or additional gate for a witness with settled premises.

### State the criterion before optimizing its satisfaction

Fix finite nonempty sets of models \(M\), complete accessible transcripts \(H\) and action alternatives \(A\). One actual common acquisition protocol yields transcript distributions \(P_m\). Initialization, hidden-world-dependent information, costs and available actions must be included in the stated interface. For each \(m\), independently specify \(L_m\subseteq A\), the actions meeting a declared requirement. A common decision kernel is \(\delta(a\mid h)\). Define the requirement-failure probability

\[
e_m=\sum_hP_m(h)\delta(A\setminus L_m\mid h).
\tag{T15a}
\]

The type of the requirement matters. Satisfying a condition under the actual facts, being permissible given the actor's justified evidence, and being an authorized decision procedure are different assessments. The symbol \(L_m\) does not make an action morally licensed. A permissible risky choice can miss a fact-relative target; a low failure frequency does not establish permission to take the risk or measure its severity. If permission depends on a lottery, deliberation procedure or prior history, those must be represented in the decision object or assessed separately. One cannot optimize a fixed matrix while silently changing what its entries mean with the chosen kernel. The fixed-\(L_m\) results below apply only when that specification is appropriate.

A real-world guarantee additionally requires the actual observation law and relevant action-requirement interpretation to be covered by \(M\). This is an independently justified application premise. An excluded model may produce familiar transcripts, so nonempty \(M(h)\) does not certify that the model class is adequate. Off-model detection below catches some failures, not every hidden misspecification.

### T15. Exact zero-error action need not identify the model

Let \(M(h)=\{m:P_m(h)>0\}\). Then \(e_m=0\) for every model if and only if, at every reachable transcript,

\[
\operatorname{supp}\delta(\cdot\mid h)
\subseteq\bigcap_{m\in M(h)}L_m.
\tag{T15b}
\]

**Proof.** Every term contributing to \(e_m\) is nonnegative. Zero total error therefore requires every action with positive conditional probability at a positive-probability transcript to meet that model's requirement. Requiring this for every compatible model gives the intersection. The same condition makes every error term zero, proving sufficiency. ∎

For unrestricted decision kernels, a zero-error rule exists exactly when each reachable intersection is nonempty. Choosing and implementing its members may still require unavailable information or resources. If the retained model set gives an actually observed transcript zero probability everywhere, the account has encountered model mismatch; its empty compatibility set does not authorize arbitrary action by vacuity. If some individual \(L_m\) is empty, there is a feasibility or requirement problem even with perfect knowledge of \(m\).

Model identification can be unnecessary. With identical transcript laws and \(L_0=\{a,b\}\), \(L_1=\{b,c\}\), the constant choice \(b\) meets both requirements. The inquirer need not resolve which model holds. Conversely, pairwise overlaps do not guarantee a common action for a larger family.

### T16. An exact benchmark when evidence cannot distinguish the models

Suppose \(P_m=P\) for every \(m\). Any common kernel induces one action distribution \(p(a)=\sum_hP(h)\delta(a\mid h)\). Thus, when arbitrary constant mixtures are available,

\[
\min_\delta\max_m e_m
=1-\max_{p\in\Delta(A)}\min_m p(L_m).
\tag{T16}
\]

**Proof.** The success probability in model \(m\) is \(p(L_m)\). Conversely, every distribution \(p\) can be represented by the constant kernel \(\delta(a\mid h)=p(a)\). Optimization over the finite-dimensional simplex attains the displayed value. ∎

This is a declared worst-case compliance benchmark. If actual policies cannot implement all mixtures, its value is only a lower bound on their achievable worst-case failure. It is not a theorem that minimizing this frequency is the right ethical decision principle.

For an exact three-action example, let \(L_1=\{a,b\}\), \(L_2=\{b,c\}\), and \(L_3=\{a,c\}\). Each pair intersects, but the joint intersection is empty. For any mixture the three success probabilities sum to two, so their minimum cannot exceed \(2/3\). Uniform mixing attains \(2/3\) in each model, giving unavoidable worst-case failure \(1/3\). Every fixed pure action fails completely in one model; a deterministic rule applied to a random but uninformative transcript can itself produce a mixture. Randomization improves this specified guarantee without adding information, but cannot make it perfect or certify the lottery's moral permissibility.

### T17. Disjoint requirements impose an information bound

For two models with \(L_0\cap L_1=\varnothing\),

\[
e_0+e_1\ge1-\operatorname{TV}(P_0,P_1),
\qquad
\max(e_0,e_1)\ge\frac{1-\operatorname{TV}(P_0,P_1)}2.
\tag{T17}
\]

**Proof.** Put \(r_i(h)=\delta(L_i\mid h)\). Disjointness gives \(r_0+r_1\le1\). Hence the sum of success probabilities is at most
\(\sum_h[P_0(h)r_0(h)+P_1(h)(1-r_0(h))]\), which is at most \(1+\operatorname{TV}(P_0,P_1)\). Rearranging gives the first inequality; the larger error is at least their average. ∎

When both sets are nonempty and all relevant kernels are implementable, choosing a representative action from the more likely model's set attains the equal-prior average bound. It need not attain that value for the worst-model criterion. A shared acceptable action removes this particular disjointness obstruction. The theorem demands relevant distinction only where the requested responses cannot be jointly satisfied.

### T18. Abstention changes coverage, not the meaning of justification

To report erroneous commitments separately, add a symbol \(\bot\) that makes no commitment in this statistic. Let \(k(h)=\sum_{a\in A}\delta(a\mid h)\), \(c_i=\sum_hP_i(h)k(h)\), and \(u_i=\sum_hP_i(h)\delta(A\setminus L_i\mid h)\). For disjoint requirements, set \(c=(c_0+c_1)/2\). Then

\[
u_0+u_1\ge c-\frac12\sum_hk(h)|P_0(h)-P_1(h)|
\ge c-\operatorname{TV}(P_0,P_1).
\tag{T18a}
\]

**Proof.** At each transcript, \(r_0+r_1\le k\). The sum of erroneous-commitment contributions is therefore at least \(k\min(P_0,P_1)\). Sum and use \(\min(p,q)=(p+q-|p-q|)/2\). The second inequality uses \(0\le k\le1\). ∎

For \(c>0\), the equal-prior conditional error among commitments is consequently at least

\[
\max\left\{0,\frac{c-\operatorname{TV}(P_0,P_1)}{2c}\right\}.
\tag{T18b}
\]

Report \(c_0,c_1\) as well as their mean; conditional error is undefined at zero coverage. The first bound is attainable for a fixed \(k\) with nonempty requirement sets and implementable kernels by choosing the more likely model's representative when committing. The coarser TV bound need not be tight. For example, \(P_0=(3/4,1/4)\), \(P_1=(1/4,3/4)\) have best equal-prior conditional error \(1/4\) at every positive coverage, although the coarser lower bound is zero when \(c\le1/2\). A zero lower bound is not a construction of error-free action.

With identical laws for all models, coverage is common. At fixed \(c>0\), normalizing the committed action probabilities shows that unrestricted minimax erroneous-commitment probability is \(c\) times T16's value, while conditional worst-model error retains that value. Merely committing less often cannot resolve an indistinguishable conflict. The statistic's exemption for \(\bot\) is not moral permission to abstain: waiting can cause harm or violate an assistance duty. When that consequence is assessed, waiting belongs among the substantive actions or policy effects.

### What this requires of the whole foundation

A claimed response guarantee needs sufficient information **or** sufficient overlap among acceptable responses, plus an actual means of acting. It need not require identifying every hidden fact. New evidence can help only when it separates relevant possibilities; purely normative disagreement is not automatically settled by additional sensor readings. Acquiring information may also consume resources, miss a deadline or alter authority, so its effect on the complete decision problem must be reassessed rather than inferred from informativeness alone.

The [accepted application account](../../../../theories/becoming/history/EVALUATIVE-APPLICATION.md) remains closed at its conditional scope. These results neither demand new randomization machinery for its settled witness nor convert a retained self-loss coefficient into a moral risk allowance. The next judgment must say what its requirement measures, what grounds it, which interpretations it covers and which causal capacities the learner actually possesses. The [reason-guided-action comparison](HUIGEN-SELF-GROUND-SOURCES.md#14-reason-guided-action-and-uncertain-outcomes) separates those obligations from the stronger attribution of acting for a justified reason. No empirical measurement, code experiment or formal compilation is added here.

## 17. Evidence reporting and application-specific stakes

6 October 2026. The connection is **warranted inference → recommendations under error stakes → practical responsibility**. These elementary decision-theoretic results apply the earlier information-preservation methods; they are not new statistical principles. Their constructive point is that preserving usable evidence can serve different applications without silently selecting one application's priorities.

### T19. Fixed evidence does not determine a unique recommendation across stakes

Let a finite evidence model yield a posterior \(q=\Pr(\theta=1\mid h)\) at a reachable transcript, where \(\theta\in\{0,1\}\). Its prior, observation law and application are independently justified premises. For actions \(a\in\{0,1\}\), give correct decisions zero loss, false positives loss \(c_{FP}>0\), and false negatives loss \(c_{FN}>0\). Expected losses are

\[
R(1)=(1-q)c_{FP},\qquad R(0)=qc_{FN}.
\]

Hence action 1 minimizes expected loss exactly when

\[
q\ge t:=\frac{c_{FP}}{c_{FP}+c_{FN}}.
\tag{T19}
\]

At equality both actions minimize; choosing 1 there is a tie convention. The result follows by rearranging \(R(1)\le R(0)\).

For \(0<q<1\), put \(o=q/(1-q)\). With \(c_{FN}=1\), choosing \(c_{FP}=o/2\) makes action 1 uniquely optimal, while \(c_{FP}=2o\) makes action 0 uniquely optimal. Thus no one binary action is optimal for every positive loss ratio at an interior posterior. At \(q=0\) or \(q=1\), the corresponding correct action is optimal for all such ratios. The evidence and posterior remain fixed throughout. Multiplying both losses by one positive constant preserves the threshold; changing their ratio changes the decision criterion.

### T20. Exact common optimality under several applications

For finite nonempty state and action sets, fix a posterior \(q\) and a nonempty family \(\mathcal L\) of finite real-valued loss tables. Define

\[
O_\ell(q)=\arg\min_{a\in A}\sum_mq_m\ell(a,m).
\]

A simultaneously optimal action exists exactly when \(\bigcap_{\ell\in\mathcal L}O_\ell(q)\ne\varnothing\). Under linear expected loss, a lottery is simultaneously optimal exactly when its support lies in that intersection.

**Proof.** The pure-action statement is the definition of simultaneous optimality. For each table, subtract its minimum risk from every action's risk. The lottery's excess risk is a sum of nonnegative terms, so it vanishes exactly when every positive-probability action is a minimizer. Apply this to every table. ∎

This is simultaneous optimality, not minimax compromise or moral licensing of a lottery. Feasible alternatives, applicable authority and the comparison criterion must be specified independently. Adding abstention, further inquiry or a report changes the action menu and requires its own consequences and costs. Failure of one terminal recommendation across applications is not failure of scientific inquiry as such.

### T21. Preserving every binary application distinguishes every admitted posterior

Let nonempty \(Q\subseteq[0,1]\) be the admitted posterior values and \(r:Q\to Z\) one deterministic, cost-independent report, the recipient's complete channel of information about the posterior. A decoder receiving only that report and the positive loss pair can return an optimal binary action for every \(q\in Q\) and every such pair **if and only if** \(r\) is injective.

**Proof.** If \(q<q'\) share a report, choose \(t\in(q,q')\), \(c_{FP}=t\) and \(c_{FN}=1-t\). The unique optimal actions differ, so one decoded answer cannot serve both. Conversely, an injective report determines its posterior on its image, permitting T19's threshold rule. ∎

Therefore a finite report alphabet cannot meet this exact all-stakes specification on an infinite \(Q\). Finite actual \(Q\) can be encoded finitely. A stakes-specific one-bit recommendation can suffice for its fixed threshold; additional recipient information can also distinguish otherwise identical reports. Those are different interfaces. This is an application of [H13's preserved-question condition](HUIGEN-GENERATIVE-CLOSURE.md#h13-the-operational-invariant-is-a-preserved-question), not a demand that every scientist store infinitely precise probabilities. The theorem concerns semantic sufficiency; acquiring the posterior, knowing the encoding and executing its inverse are additional capacities.

### T22. Approximate reporting has a uniform regret bound

Suppose a report yields \(\hat q\in[0,1]\) with independently warranted \(|\hat q-q|\le\varepsilon\), where \(\varepsilon\ge0\). Applying the threshold to \(\hat q\) incurs excess expected loss at most

\[
(c_{FP}+c_{FN})\varepsilon.
\tag{T22}
\]

**Proof.** If the chosen action is optimal at \(q\), regret is zero. Otherwise \(q\) and \(\hat q\) lie on opposite sides of the threshold, allowing a boundary tie. The excess loss equals \((c_{FP}+c_{FN})|q-t|\), which is at most \((c_{FP}+c_{FN})|q-\hat q|\). ∎

Normalizing the loss sum to 1 gives regret at most \(\varepsilon\); it does not make differently scaled real burdens equally serious. When a choice incurs positive regret, unbounded rescaling removes any uniform finite absolute bound. Approximate reporting can nevertheless serve a specified tolerance without hiding an application-specific threshold. If \(|q-t|>\varepsilon\), the report selects the unique optimal action exactly. Which tolerance and loss scale are acceptable remains supplied.

For every integer \(n\ge1\), rounding a known \(q\) to the nearest point of \(\{0,1/n,\ldots,1\}\) uses \(n+1\) possible report symbols and gives normalized regret at most \(1/(2n)\). This supplies an indefinitely refinable family of conditional guarantees, while no finite \(n\) preserves exact optimal decisions for every \(q\in[0,1]\) and threshold; actual acquisition, warranted calibration and implementation costs are not supplied by the construction.

### What the root must preserve

A mathematical posterior is not automatically a probability the learner has warranted or acquired. Model adequacy, calibration evidence and retained interpretation need their own account; no hidden true label or analyst reward supplies them. T22's approximation error concerns a specified posterior, not an unproved bound on real-world miscalibration. A likelihood report also differs from a posterior: application requires a prior or another stated inference rule.

Scientific work may report evidence, assumptions and uncertainty for others to apply. Such reporting can itself affect reliance and action, so it is not automatically consequence-free. Where a justified undertaking or role requires advice, the recommendation should expose its substantive comparison premises rather than present them as evidence alone. Expected-loss minimization does not make a convenient falsehood true or establish its epistemic warrant.

Actual patient burdens, actor-addressed reasons, intervention authority and feasible resources remain distinct inputs. A self-loss coefficient or successful choice rule does not justify interpersonal loss weights. Conversely, learned information can warrant different applications of an independently justified ground without recreating that ground. The [accepted application](../../../../theories/becoming/history/EVALUATIVE-APPLICATION.md) retains its settled conditional scope; this extension adds no gate or experiment to it. The positive generative obligation is to explain how usable evidence and justified application premises reach actual choices, while preserving the option of an adequate report. No empirical study, model execution or formal compilation is added.

**Bounded review, 6 October 2026:** independent argument review passed T19–T22 and their reporting, implementation and normative limits. This author reviewed [self-ground audit §18](HUIGEN-SELF-GROUND-AUDIT.md#18-does-inductive-risk-make-concern-internal-to-science), [source reconstruction §15](HUIGEN-SELF-GROUND-SOURCES.md#15-inductive-risk-and-the-scope-of-scientific-responsibility), and the canonical lead, new scientific-responsibility subsection and continuing-derivation paragraph. No mathematical or scope blocker was found. This was conceptual and interface review without independent reopening of the four primary works, empirical reanalysis or formal execution. No canonical or index file was edited by this author.

## 18. Patient good and the determinacy of idealization

6 October 2026. The connection is **formed evaluative response → warranted patient-good representation → reasons concerning another patient**. This is an assumption audit of an idealization procedure, not another optimization theorem. The [new harm-and-action account](../../../../theories/becoming/history/RECIPIENT-HARM-AND-ACTION.md) gives empirical contact with recipient-linked action and shared responses. It explicitly separates factual or efficacy learning from acquired evaluative influence and ethical warrant. We inherit that scope without rerunning its analysis or treating its behavioral change as a direct measurement of patient-good.

### Preserve the actual beneficiary of the idealized assessment

Write the proposed assessment as \(E(z;p,c,x)\): an informed counterpart \(z\) assesses outcome \(x\) for actual patient \(p\) in actual circumstances \(c\). It is not automatically \(E(z;z,c_z,x)\), what suits the counterpart after its transformation. Information, changed capacities or altered preferences can change the counterpart's own interests. Confusing these targets can make an idealization answer the wrong question even when every represented fact is true.

This preserves neither every present desire nor every present circumstance as desirable. An assessment can favor learning, changed habits or a different future for \(p\). It must explain why these changes serve that patient's good. Actual approval, informed advice, a dispositional natural basis and intervention authority remain different claims. [Railton's comparison](HUIGEN-SELF-GROUND-SOURCES.md#16-naturalistic-good-and-reasons-for-others) makes the actual-versus-ideal target explicit, distinguishes the proposed natural truthmaker from the ideal response, and acknowledges order-independence as a substantive idealization assumption. The following finite audit sharpens that admitted issue; it does not discover it anew.

### Factual convergence need not determine the evaluative readout

Fix an initial state \(s_0\), a finite set \(F\) of distinct information items, and update maps \(U_f\). For this audit, every permutation of \(F\) is admitted and processes each item once. A factual projection records which target facts are correctly understood. A separate readout \(\rho(s;p,c)\) gives the proposed patient-good comparison or full recommendation set. Keep \(p,c\) fixed throughout.

The readout is independent of information order **if and only if every adjacent exchange preserves it in its complete context**: whenever words \(u f g v\) and \(u g f v\) are permutations of \(F\),

\[
\rho(U_vU_gU_fU_u s_0;p,c)
=\rho(U_vU_fU_gU_u s_0;p,c).
\]

Here \(U_u\) applies the prefix in its written order, with the empty word acting as the identity; the suffix is retained because later updates can amplify a difference. Necessity follows from order-independence. For sufficiency, any permutation can be transformed into any other by adjacent exchanges, each preserving the final readout. This is an elementary permutation argument. If only some orders are admitted, adjacent checks establish equality within each connected component of their swap graph; comparison between components remains necessary.

Commuting full update states is sufficient but stronger than needed. Distinct memories or histories may yield the same relevant assessment. Conversely, equal readouts immediately after swapping two updates are insufficient if a later update can distinguish their hidden states. Equal-best alternatives can also form one stable, plural recommendation set: arbitrary selection of different members is not evidence that the underlying assessment changed.

For an exact counterexample to factual correction alone, let states be \((K,v)\), with \(K\subseteq\{f,g\}\) the acquired facts and \(v\in\{0,1\}\) selecting opposite strict recommendations for the same patient. Acquiring a previously unseen \(f\) adds it to \(K\) and sets \(v=0\); acquiring a previously unseen \(g\) adds it and sets \(v=1\). Reprocessing a known item does nothing. From one initial state with \(K=\varnothing\), order \(fg\) ends at \((\{f,g\},1)\), while \(gf\) ends at \((\{f,g\},0)\). Both have all designated facts and remain stable under further repetition, yet their recommendations differ.

This stipulated update law is not a psychological finding or a model of fully rational ideal agents. The terminal states share their finite target-fact model, not every fact about their histories, physical states or self-knowledge. It identifies what the declared correction constraints fail to determine. It does not refute a naturalistic identity that independently restricts which evaluative updates or bases are appropriate.

### Convergence and justified patient-good remain separate

Restricting the admitted orders to \(fg\) makes the example converge; restricting them to \(gf\) produces the opposite result. Alternatively, setting the readout permanently to either recommendation gives order-independence. None of these operations alone justifies its recommendation. A convergence proof must expose what its selected update, contraction or tie-breaking rule contributes. It cannot define the desired answer as the unique permissible endpoint and then claim to have explained its authority.

A constructive naturalistic account can do more. It can identify a relational property of the actual patient's constitution, circumstances and available developments; explain why that property realizes the proposed patient-good role; and show how information corrects an assessment of it. The relevant standard is whether the identified basis explains and constrains the assessment, including its errors and counterfactual changes, rather than whether a favored training procedure happens to produce agreement. A justified reduction may thereby exclude the rival readout. Leaving arbitrary utilities free would ignore that proposal, not refute it.

The learning mechanism must still show how those identified conditions acquire and retain influence. Shared activation alone does not specify that influence's direction, and an analyst-chosen reward cannot supply the very ground being explained. Conversely, internal causal realization does not make a patient-directed response selfish. Finally, establishing what benefits \(p\) does not itself settle another actor's addressed reason, authority or competing obligations; the proposed relational or moral bridge needs its own justification.

**Acceptance condition.** Specify the actual beneficiary, candidate natural basis, admitted information updates and intended readout. Test order sensitivity at that readout, allow justified plural results, and defend any restriction used to obtain determinacy. Establish the patient-good interpretation rather than selecting it by favorable behavior, then assess its connection to other actors separately. This can close a finite explanatory interface without claiming omniscient convergence or reopening the accepted application contract. No new experiment, code or formal compilation is added.

**Bounded review, 6 October 2026:** independent argument and source-attribution reviews passed this section. This author read Railton's printed pp. 174–176 through the shared extraction of the original journal PDF, without a facsimile or full-article review. The [companion audit §19](HUIGEN-SELF-GROUND-AUDIT.md#19-naturalistic-patient-good-without-an-imported-moral-verdict), source reconstruction and canonical lead, new patient-good subsection and continuing-derivation paragraph also pass at their stated scopes. Foot's primary work and the recipient study's data were not independently reaudited here. No canonical or index file was edited by this author.
