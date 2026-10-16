# When finite grounds warrant coherent completion

6 October 2026. AI-authored hand proofs for **independently specified finite grounds of exclusion → the admissible completed domain**. This continues [ideal completion](MATHEMATICAL-ADMISSIBILITY-MATH.md), under the [nondual method](../../../../theories/becoming/chapters/NONDUAL-METHOD.md). Formation, exclusion, approximation and mathematical reflection are relations within the investigated activity. An explicit decomposition should preserve those relations rather than convert a limitation of a projected representation into a defect of the fuller account.

The previous theorem established that faithful compact approximations, directed completeness and generation by those approximations uniquely determine an ideal completion. The present question is why one should require that completion for a particular subject. There is a precise conditional answer: **if exclusion must be justified by a finite incompatible approximation, the admitted completed objects are exactly all ideals made from the permitted finite approximations**. The theorem classifies that admission role; it does not prove that every legitimate mathematical or practical requirement has it.

The arguments use ordinary classical set mathematics, including the full ambient ideal space. They are standard order-theoretic and safety-property mechanisms, not claims of mathematical priority, newly compiled formal proofs or empirical validation. No learner, evaluator or new physical event law is installed. The [earlier finite-character closure theorem](MATHEMATICS-CLOSURE-RESOLUTION.md#1-positive-rules-give-a-unique-least-admissible-carrier) concerns closure operators on subsets; the following instead characterizes families of completed approximation profiles by their grounds of exclusion.

## 1. Partial admissibility and finite refutation

Fix the nonempty poset \(P\) of approximations from the preceding note. Its order and interpretation are supplied by the particular construction under investigation. Let

\[
X=\operatorname{Idl}(P)
\]

be the poset of nonempty directed lower subsets of \(P\), ordered by inclusion. Its nonempty directed suprema are unions. Write \(\eta(p)=\downarrow p\) for the principal ideal representing a finite approximation. These definitions and their properties are proved in [A1–A3](MATHEMATICAL-ADMISSIBILITY-MATH.md#2-a-completion-with-exactly-the-original-compact-approximations).

A proposed admissibility class is any subset \(C\subseteq X\), possibly empty. The issue is **admissibility as a partial or completed approximation profile**, not whether a finite prefix is already a finished accepted output. A partial construction can remain admissible without satisfying a requirement to finish. Conflating those two predicates would make the hereditary condition below inappropriate by definition.

Say exclusion has a **finite refutation** when

\[
I\notin C\quad\Longrightarrow\quad
\exists p\in I\quad
\forall J\in C\;(p\notin J).
\tag{W1}
\]

Thus an excluded profile contains a particular approximation that no admitted profile can include. The witness concerns an actual incompatible finite content, not an externally attached failure label. This is a semantic existence condition. It does not yet supply an algorithm recognizing such witnesses, a bound on how soon one will be found, or a physically available observation of it.

For comparison, call \(C\) **Scott-closed** when:

1. it is lower under inclusion: \(I\in C\) and \(J\subseteq I\) with \(J\in X\) imply \(J\in C\); and
2. the union of every nonempty inclusion-directed family of members of \(C\) is again in \(C\).

The first condition says that removing positive approximate content does not create an incompatibility. The second says that a coherent directed accumulation of permitted contents receives no new exclusion solely at its limit. Neither condition is automatic for all goals or predicates.

## 2. An exact characterization of finite-grounded admission

### Theorem W1 — Finite refutation, directed closure and the permitted basis

For every \(C\subseteq\operatorname{Idl}(P)\), the following are equivalent:

1. \(C\) satisfies finite refutation (W1).
2. \(C\) is Scott-closed.
3. There is a lower subset \(Q\subseteq P\) such that
   \[
   C=\{I\in\operatorname{Idl}(P):I\subseteq Q\}
   =\operatorname{Idl}(Q).
   \tag{W2}
   \]

Here \(\operatorname{Idl}(Q)\) is identified with its ideals as subsets of \(P\). Because \(Q\) is lower, those are exactly the ideals of \(P\) contained in \(Q\). If \(Q\) is empty, its ideal space is empty under the nonempty-ideal convention. The subset \(Q\) is unique and satisfies

\[
Q=\{p\in P:\eta(p)\in C\}=\bigcup_{I\in C}I.
\tag{W3}
\]

**Proof, 1⇒2.** If \(I\in C\) and \(J\subseteq I\) were excluded, W1 would give \(p\in J\) occurring in no admitted ideal. But \(p\in I\), a contradiction. Thus \(C\) is lower. Let \(\mathcal D\subseteq C\) be nonempty and directed, and set \(I=\bigcup\mathcal D\). If \(I\notin C\), W1 gives \(p\in I\) occurring in no member of \(C\). Some \(J\in\mathcal D\) contains \(p\), again a contradiction. Thus \(C\) is closed under directed unions.

**Proof, 2⇒3.** Define \(Q=\{p:\eta(p)\in C\}\). If \(p\leq q\in Q\), then \(\eta(p)\subseteq\eta(q)\), so lower closure puts \(p\) in \(Q\). If \(I\in C\), then for every \(p\in I\) its principal ideal lies below \(I\), hence belongs to \(C\); therefore \(I\subseteq Q\). Conversely, if \(I\subseteq Q\), each \(\eta(p)\), \(p\in I\), belongs to \(C\). These principals form a nonempty directed family with union \(I\), so \(I\in C\). This gives (W2). Its first expression shows that every member of \(C\) contributes only elements of \(Q\), while \(p\in Q\) contributes \(p\) through \(\eta(p)\in C\); hence the union identity in (W3).

**Proof, 3⇒1 and uniqueness.** If \(I\notin C\), choose \(p\in I\setminus Q\). No admitted ideal can contain \(p\), since all are contained in \(Q\), proving W1. For any lower \(Q\), the principal ideal \(\eta(p)\) is contained in \(Q\) exactly when \(p\in Q\), so (W2) determines \(Q\) uniquely. ∎

The implication with explanatory force is now explicit: **fix the permitted finite content \(Q\), and require that every exclusion have a finite incompatible witness; then the admitted domain is forced to be \(\operatorname{Idl}(Q)\)**. It is not necessary to supply the completed carrier separately. But the finite-refutation requirement is itself a substantive restriction on what this subject counts as an exclusion. A global requirement can legitimately decline it.

One can state the same result as two separate obligations: admitted profiles have only permitted finite approximations, and a profile with only permitted finite approximations is not rejected for some further limit-only reason. The second is not entailed by the first. W1 characterizes their combination; it does not hide that combination inside the word “finite.”

## 3. The least finite-refutable enlargement preserves exactly the finite content

### Theorem W2 — The least Scott-closed hull

For arbitrary \(C\subseteq X\), define

\[
Q_C=\bigcup_{I\in C}I.
\tag{W4}
\]

Then the least Scott-closed subset of \(X\) containing \(C\) is

\[
\operatorname{cl}_{\mathrm S}(C)
=\operatorname{Idl}(Q_C).
\tag{W5}
\]

It introduces no finite approximation absent from every member of \(C\).

**Proof.** A union of lower subsets is lower, so \(Q_C\) is lower. Every \(I\in C\) lies in \(\operatorname{Idl}(Q_C)\), and W1 makes the latter Scott-closed. If \(E\) is another Scott-closed family containing \(C\), W3 gives \(E=\operatorname{Idl}(Q_E)\), with \(Q_C\subseteq Q_E\). Hence \(\operatorname{Idl}(Q_C)\subseteq E\), proving leastness. Finally, W3 applied to the hull gives its union exactly \(Q_C\). ∎

This is a completion of the **admission class**, not a claim that its added profiles satisfy every former requirement. If the original \(C\) enforced a genuinely global condition, taking (W5) can remove that condition. It is appropriate only if the intended question has been restricted to the finite content and its coherent completion.

Nor does (W5) arbitrarily combine incompatible pieces. A new member must still be directed. For example, with finite subsets of \(\{a,b\}\) as \(P\), let \(C\) contain just the principal ideals of \(\{a\}\) and \(\{b\}\). Their union contains \(\varnothing,\{a\},\{b\}\) but not \(\{a,b\}\). No ideal of that union can contain both singletons, since it lacks a common upper bound for them. The hull does not add their forbidden finite combination.

## 4. Independently given finite prohibitions

Suppose a set \(F\subseteq P\) specifies finite forbidden contents through independently stated construction rules. Define

\[
Q_F=\{p\in P:\nexists b\in F\ (b\leq p)\}.
\tag{W6}
\]

It is lower: weakening an approximation cannot create a previously absent forbidden subapproximation. A completed profile respects the prohibitions exactly when it contains no member of \(F\).

### Corollary W2a — The maximal class respecting finite prohibitions

The family of all ideals respecting those prohibitions is

\[
\{I\in X:I\cap F=\varnothing\}
=\operatorname{Idl}(Q_F).
\tag{W7}
\]

It is the largest admissibility class excluding every profile that contains a specified forbidden content. It is the unique such finite-refutable class whose permitted principal approximations are exactly \(Q_F\).

**Proof.** If \(I\cap F=\varnothing\) and \(p\in I\), then no \(b\in F\) can lie below \(p\), because lower closure would put \(b\) in \(I\). Thus \(I\subseteq Q_F\). Conversely, if \(I\subseteq Q_F\), it cannot contain a forbidden \(b\), since \(b\leq b\). The maximality statement follows from the first expression of (W7); uniqueness with the stated principal classification follows from W1. ∎

The prohibitions alone allow stricter subclasses. For example, one can separately require eventual completion or fairness even when no finite violation occurs. Requiring rejection **only** on the specified finite grounds selects the maximal class (W7). That is an intelligible role for this mathematical subject, not an inference that every relevant criterion in every inquiry must use maximal admission.

In a full concrete event-history representation, a failed transition rule, a violated finite dependency or an exceeded explicit counter condition can be such a finite ground. If those are the complete declared grounds of invalidity, the completion introduces no new event-law violation: any such violation would already occur in a finite approximant. This argues for ideal completion as the subject “all coherent histories respecting these finite event laws.” It does not establish indefinite physical enactment, a computable selection procedure, or fulfillment of an additional global purpose.

## 5. Infinite-word admissibility and forbidden prefixes

Let \(\Sigma\) be a nonempty alphabet, and consider infinite words \(\Sigma^{\mathbb N}\). No finite-alphabet or compactness assumption is needed for the following equivalence. For a finite word \(u\), write

\[
[u]=\{\alpha:u\text{ is a prefix of }\alpha\}
\]

for its cylinder. These cylinders form a basis for the usual prefix topology, equivalently the product topology with a discrete alphabet. For \(K\subseteq\Sigma^{\mathbb N}\), define

\[
\operatorname{Pref}(K)=\{u:\exists\alpha\in K\ (u\text{ prefixes }\alpha)\}.
\tag{W8}
\]

### Theorem W3 — Finite bad prefixes characterize closed word properties

The following are equivalent:

1. If \(\alpha\notin K\), some finite prefix \(u\) of \(\alpha\) has \([u]\cap K=\varnothing\).
2. \(K\) is closed in the prefix topology.
3. \(K\) is exactly
   \[
   \{\alpha:\text{every finite prefix of }\alpha\text{ lies in }\operatorname{Pref}(K)\}.
   \tag{W9}
   \]

For arbitrary \(K\), the right side of (W9) is its topological closure.

**Proof.** Every admitted word has its prefixes in \(\operatorname{Pref}(K)\). Condition 1 excludes precisely those other words having a prefix absent from that set, proving its equivalence with 3. A word lies outside the closure of \(K\) exactly when some basic neighborhood \([u]\) containing it is disjoint from \(K\). This proves equivalence with 2 and the closure formula. ∎

This is the standard safety-property characterization: a violated property has a finite bad prefix beyond which no continuation repairs that violation. “Safety” here is the technical classification of a history property, not an ethical judgment that the behavior is harmless or an adequate complete specification of a system.

For an arbitrary prefix-closed finite-word language \(H\), its infinite boundary

\[
\partial H=\{\alpha:\alpha\mathbin{\upharpoonright}n\in H\text{ for every }n\}
\tag{W10}
\]

is closed by W3's bad-prefix argument. But \(H\) need not equal \(\operatorname{Pref}(\partial H)\). A finite dead end can belong to \(H\) without any infinite extension in \(H\); for example \(H=\{\epsilon,0\}\) has empty boundary. The ideal completion retains the finite admitted histories as well as the infinite boundary. One must not discard those finite objects or silently add an infinite-extension premise when applying the word theorem.

If \(K\) is nonempty and closed, its finite prefixes together with \(K\) form exactly \(\operatorname{Idl}(\operatorname{Pref}(K))\) under the earlier word/ideal correspondence. For empty \(K\), its prefix set and this ideal space are empty. Conversely, a nonempty finite-history ideal space can have empty infinite boundary. The infinite-only and finite-plus-infinite questions therefore have different carriers even though their finite-refutation arguments correspond.

## 6. Substantive global criteria that completion does not preserve

### Example W4 — Finite termination

Take unary finite words ordered by prefix, so \(X\) consists of \(\epsilon,a,a^2,\ldots,a^\infty\). Let \(C\) contain exactly the finite words. Every finite approximation is permitted, but \(a^\infty\) is excluded. No finite prefix refutes it, since that prefix is itself admitted. The increasing chain of finite words has an excluded supremum. Consequently \(C\) is lower but not Scott-closed, and its hull is all of \(X\).

If the intended subject requires termination, that additional criterion is legitimate and the hull no longer preserves the full subject. The example does not show that one can execute an infinite run. It shows that the particular termination predicate is a global restriction not captured by finite refutation in this approximation order.

### Example W5 — Infinite recurrence or fairness

Take binary words and let \(C\) contain all finite words and exactly those infinite words with infinitely many occurrences of 1. Its finite content is all binary finite words, because every finite word can be followed by infinitely many 1s. Yet \(0^\infty\) is excluded and has no finite forbidden prefix. Thus \(C\) is lower but not Scott-closed, and its Scott-closed hull admits all finite and infinite binary words.

The property can represent a separately justified recurrence requirement, such as infinitely many designated service events, when the symbols have that meaning. No finite history proves that another such event will never occur. Completing only its finite restrictions therefore drops the recurrence obligation. One must preserve that obligation separately or choose a richer specification; one cannot claim that finite coherence already proves it.

The corresponding infinite-word class is dense in the prefix topology and has closure all infinite binary words. This is a concrete substantive difference in the histories admitted, not an uninterpreted predicate toggled while claiming to keep the same target.

### Example W6 — Effective realizability

Let \(C\) contain every finite binary word and only computable infinite binary words. Every finite word has a computable extension, for example by appending zeros forever. A noncomputable infinite word is excluded, but none of its finite prefixes rules out a computable extension. Hence this \(C\) also fails finite refutation and has full ideal space as its hull.

The existence of noncomputable binary words follows, for example, because there are only countably many finite programs and uncountably many binary sequences by diagonalization. This uses the declared classical background; it is not an effective procedure producing an arbitrary such word. Requiring effective realization is another legitimate admission role, different from accepting every coherent finite profile. The earlier [effective-completion distinction](MATHEMATICAL-ADMISSIBILITY-MATH.md#7-effective-construction-and-full-admission-remain-different) preserves its exact scope.

## 7. Finite witness is not an effective test, and projection can remove the witness

W1 and W3 quantify over finite witnesses; neither says their forbidden status is decidable or even computably enumerable. An arbitrary forbidden-prefix set can encode noncomputable information. A procedure that recognizes every bad prefix requires an additional effective presentation and access to the relevant finite history. Even with such a procedure, a permitted infinite history need never receive a final certificate after finitely many observations: no violation so far is not a completed verification of all future prefixes.

Full state history matters to the claimed target. The previous [countdown counterexample](MATHEMATICAL-ADMISSIBILITY-MATH.md#counterexample-a4a--every-finite-observable-prefix-without-one-infinite-run) has one initial choice of a finite counter, followed by at most that many ticks. Projected words \(ca^n\) have a finite execution for every \(n\), but \(ca^\infty\) has no single concrete execution. Therefore actual infinite realizability of those **projected** words is not completely determined by their finite feasibility. An unobserved counter choice constrains continuation across the prefixes.

In a representation retaining the concrete choice and each state transition, the valid finite runs already have the required relationship: a proposed continuation past that chosen counter violates a finite transition condition. The finite and infinite objects are then coherent concrete paths, and an infinite abstract word must still be lifted to such a path before the theorem speaks to its physical model. The earlier finite-initial, finitely branching lifting theorem gives a sufficient mathematical condition for that lift. These are alternative ways to make the representation accountable; neither is a proof that every physical process has an infinite continuation.

Thus a failure of finite refutation can have different explanations. A desired global property may genuinely exceed the finite-local role. Or an impoverished observation projection may have omitted the state relation that makes the relevant failure finite. The positive nondual account must be reconstructed before deciding which diagnosis applies. Enlarging the description to include irrelevant or inaccessible hidden labels would not by itself establish the intended relation either.

## 8. The warranted role and its rival interpretation

The strongest positive inference is conditional but substantive:

> If the intended mathematical subject comprises coherent extensions of independently specified finite constructions, and its complete grounds of exclusion are finite incompatibilities in that structure, the admitted completed domain is forced to be the ideal completion of its permitted finite basis.

The theorem answers which completion fits this role and why another carrier with the same role cannot introduce different completed admissions. The role can be justified where the inquiry expressly concerns everything compatible with the complete finite event-law restrictions. It is inappropriate as a purported solution to a task whose independently established target also requires termination, fairness, effective realization or another global condition. The examples do not refute those targets; they distinguish them.

This argument still quantifies over the full ambient ideal space and its subsets. It identifies the admissible portion of that mathematical space once the finite-refutation role is fixed. It does not derive that background universe from a mathematics-free root, nor establish that every coherent mathematical profile is physically or metaphysically instantiated. The finite criteria do not create an effective inventory of all admitted infinite objects.

A substantive structural alternative interprets \(P\) as an abstract approximation poset, admissibility as a lower directed-closed class, and ideal completion as its standard mathematical construction. It preserves the same permitted finite contents, all completed profiles, universal properties and finite-refutation equivalence. It can also investigate or reproduce the formation of approximations, their meaningful relations and situated mathematical practices using the same event and learning mechanisms, while declining the claim of ultimate generative priority. The generative account must therefore be compared with that stronger alternative, not credited with exclusive access to explanations of formation merely because it emphasizes them. W1–W3 do not prove that the structural interpretation is impossible or derive its ontology from our root. To establish unique ultimate constitution, the account would need an additional argument showing that this alternative depends on the generative grounding or fails to explain independently specified features of the same target.

That is not a reason to discard the positive result. It locates what the mathematical proof settles: within the finite-refutation role, completion is forced rather than independently selected. It also locates what would revise the account: a finite incompatibility omitted from the basis, a legitimate limit-only restriction mistakenly erased by completion, a projection failing to preserve coherent realization, or a purported counterexample satisfying the complete hypotheses but violating W1–W3.

## 9. Antecedents and validation scope

The poset proof uses the principal compact basis established in the [ideal-completion note](MATHEMATICAL-ADMISSIBILITY-MATH.md) and standard Scott-closed-set reasoning. The infinite-word theorem is the familiar characterization of safety through finite bad prefixes and closed sets; primary antecedents and inspected passages are recorded in the [companion source review](COMPLETION-WARRANT-SOURCES.md). That review identifies Alpern and Schneider's finite-prefix and topological characterizations, Abramsky and Jung's Scott-closed-set definition, and a substantive structuralist comparison. The purpose is to expose the admissibility contract in the generative argument, not rename established mathematics as a novel theorem.

Validation here is by the explicit hand proofs and independent mathematical review. Finite examples explain the distinctions; enumerating a finite set of words would not verify the statements about all ideals or infinite histories. No scientific model, source law, runtime experiment or prior Lean proof is altered by this note.
