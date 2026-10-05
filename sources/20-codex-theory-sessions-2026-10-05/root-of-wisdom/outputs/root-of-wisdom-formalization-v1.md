# A formal model of the practical root of wisdom

First formalization for Ren, 5 October 2026. This develops the candidate from the [cross-session assessment](root-of-wisdom-cross-session-assessment.md): concern for affected beings, understanding of the situation, and judgment about one's response can correct one another.

**We can formalize this candidate as a family of processes for judgment, discovery, and reasoned revision.** We can prove conditional results about those processes. Identifying them with wisdom's unique or sufficient root remains a philosophical and empirical hypothesis. The definitions below do not settle that hypothesis by naming a variable “wisdom.”

## The state of a situated judgment

Represent the inquirer's current situation by

\[
S=(L,H,\mathcal M,N,F,D).
\]

| Symbol | Meaning |
| --- | --- |
| \(L\) | The language of available distinctions: beings, circumstances, consequences, and possible responses, with their intended interpretations. |
| \(H\) | Accessible evidence and observations, including testimony and practical encounters. Their interpretation may be disputed. |
| \(\mathcal M\) | The empirical possibilities currently admitted under the evidence and assumptions. |
| \(N\) | Normative commitments: whose interests count, protections, priorities, obligations, and unresolved conflicts. |
| \(F\) | Responses or policies presently feasible given information, time, means, and authority. |
| \(D\) | The retained record of claims, objections, decisions, outcomes, and reasons for revision. |

Responses can include acting, refraining, investigating, seeking help, refusing, or stopping. Inquiry consumes time and means and can change later possibilities. A recommendation about what someone else ought to do must be distinguished from an action available to the inquirer.

The empirical model set must not silently become empty and then certify every action by vacuous universal quantification. An empty set signals an inconsistent or inadequate account requiring an explicit diagnosis. Nor does nonemptiness imply that the actual situation is represented.

The meaning of a term in \(L\), the adequacy of \(\mathcal M\), the legitimacy of \(N\), and the accuracy of \(F\) are claims with grounds and limits. Writing them as symbols supplies none of those grounds automatically.

## The proposed root as a formal architecture

Define a candidate architecture

\[
\boxed{\mathfrak R=(\mathcal J,\mathcal G,\mathcal U)}.
\]

Its three components have different jobs:

\[
\mathcal J(S)\subseteq F
\]

is a **judgment correspondence**: the responses supported under the declared evidential and normative standards. Multiple responses may remain defensible; there need not be one scalar score or a unique best act. An empty set can expose conflicting demands or the absence of a satisfactory option. It does not prove that the person lacks wisdom. In a computational implementation, failure to find an option is also distinct from a proof that none exists.

\[
\mathcal G(S)\subseteq\mathcal P
\]

is a **generator of proposals**, where \(\mathcal P\) includes candidate explanations, inquiries, responses, and changes of representation or standards. Generating a proposal does not establish its truth, moral merit, feasibility, or priority. A concrete generator must specify its operations; a symbol is not a solution to unrestricted discovery.

\[
(S,x,S',\rho)\in\mathcal U
\]

is a **reasoned revision relation**. A challenge \(x\)—an observation, consequence, objection, argument, or discovered alternative—can warrant moving from \(S\) to \(S'\), with an inspectable record \(\rho\). A relation permits several reasonable revisions or an unresolved challenge. It avoids pretending that every value conflict has a uniquely correct computable update.

The record identifies what changed, why, which earlier consequences and objections remain relevant, and what remains uncertain. Empirical claims require suitable evidence; normative changes require normative reasons; changed means require actual capabilities. One kind of support cannot silently substitute for another. Recording a reason makes it examinable; it does not certify its truth or legitimacy.

This is a specification of a family of processes. A particular implementation still needs actual generators, assessment procedures, revision rules, and resource accounting. The other sessions implement several bounded members of that family, not the complete architecture for every situation.

## What makes the correction mutual

The architecture proposes the following dependencies:

\[
N\longrightarrow\text{what is investigated},\qquad
\mathcal M\longrightarrow\text{how concern can be served},\qquad
\text{contemplated responses}\longrightarrow\text{new empirical and ethical questions}.
\]

An implementation must demonstrate these dependencies in appropriate contrasts. Holding other inputs fixed, changing a protected interest can change which inquiry matters; changing an empirical possibility can change the defensible response; discovering that a response is unavailable can redirect inquiry or reveal an impossible demand. Merely allowing every variable to change does not establish mutual correction.

Revisions can also change the interpretation language, the candidate generator, or the assessment procedure itself. Preserve their versions and the reasons for amendment in \(D\). This does not require an infinite chain of prior certificates: the current standards are explicit and fallible. A fixed standard leaves a foundational commitment; unconstrained replacement of every standard can rationalize anything. The formalization acknowledges that tension.

Openness to revision is a capacity. No rule requires constant investigation or actual revision on every occasion. An immediate, settled, or tacit response may already be warranted. Cultivation concerns how this capacity develops across experience, not whether a person consciously executes these symbols.

## The ethical commitments enter explicitly

The ethical proposal inherited from the other session is 共同生成, with fallible 良知. Two limited formal constraints express part of its proposed concern. Neither is derived from physical dynamics.

**Non-arbitrary identity.** If a permutation \(\sigma\) exchanges only identities irrelevant to the moral comparison while preserving all relevant circumstances, an ordering of outcomes should satisfy

\[
y\succeq_N y'\quad\Longleftrightarrow\quad
\sigma y\succeq_N\sigma y'.
\]

Which differences are morally relevant needs argument. This requirement cannot make an excluded being appear in the domain by itself.

**Positive consideration.** In a comparison where only burdens differ, reducing one considered being's burden without increasing anyone else's should count in favor of the change. For a stipulated vector of nonnegative burdens, one possible formal constraint is

\[
h_i(y)\le h_i(y')\ \forall i,\quad
h_j(y)<h_j(y')\ \text{for some }j
\quad\Longrightarrow\quad y\succ_N y',
\]

holding every other morally relevant feature equal. This simplified comparison does not make all goods commensurable or specify how to resolve competing obligations. Moral standing must also not depend on ability to speak, produce, reciprocate, or participate in the procedure.

These commitments allow genuine moral development, including recognition of previously excluded beings. They require reasons for changes; they do not require every new commitment to win under the very old standard it challenges. Preserve the disputed consequences and explain the disagreement instead of declaring improvement solely because a new score is larger.

## A precise theorem about justified response under uncertainty

Consider a terminal decision, with a nonempty finite set \(W\) of possible situations and observation map \(O:W\to H\). The same observation means the actor cannot distinguish those situations before acting. Let \(A\) be a finite common action vocabulary, \(F(h)\subseteq A\) the actions feasible in every represented situation consistent with observation \(h\), and

\[
B_N(w)\subseteq A
\]

the actions meeting the specified normative requirements in situation \(w\). Consequences and admissibility are inputs to this example; they are not defined by whether our proposed root chooses the action.

For every reachable observation, set

\[
\boxed{
\mathcal J(h)=F(h)\cap
\bigcap_{w:O(w)=h} B_N(w).
}
\]

**Proposition.** A deterministic observation-based policy that is feasible and meets those requirements in every \(w\in W\) exists if and only if \(\mathcal J(h)\ne\varnothing\) for every reachable observation \(h\).

**Proof.** If a policy \(\pi\) works, then its single action \(\pi(h)\) must be feasible and acceptable in every situation with that observation, so it belongs to the intersection. Conversely, when every intersection is nonempty, choose an element for each reachable observation. There are finitely many such observations. The resulting policy works in every represented situation. □

This makes the coupling substantive: understanding determines which situations must be considered together; concern determines the requirements; available means constrain the response. Good intentions, accurate descriptions, and available actions considered separately need not produce a compatible policy.

This is a result about guaranteed acceptability in the supplied finite model. It is not a rule that wise people must refuse every uncertain risk. Risk permissions, unavoidable losses, expected benefits, and unresolved obligations need a stated alternative decision criterion. The theorem also does not address an omitted world, harm, or affected being.

## How inquiry changes the theorem

A harmless costless observation that only splits existing observation classes, while leaving actions and consequences unchanged, can preserve every previously certified policy: ignore the extra information and use the old response. It may also enable a policy where no common action previously existed.

Real inquiries need not satisfy those assumptions. They can consume the means needed for action, introduce risk, change obligations, or reveal that the old acceptability calculation omitted a harm. Their full consequences belong in the model.

For example, suppose there are two indistinguishable situations and two possible remedies:

| Situation | Acceptable remedy |
| --- | --- |
| Left | \(a\) |
| Right | \(b\) |

No immediate remedy is guaranteed acceptable. A perfectly discriminating probe followed by the indicated remedy works if the probe costs one unit, either remedy costs one unit, and two units are available. With one unit, the same probe reveals the answer but leaves no means to implement it. Add a feasible response acceptable in both situations and inquiry becomes unnecessary for this guarantee.

These conclusions concern the stipulated requirements. When none can be satisfied, an actor may still judge wisely about unavoidable loss, refusal, help, or the need to change the constraints. The mathematical failure of a guarantee is not a verdict on the person's wisdom.

## Two further limits that can be proved

**Complete facts and symmetric concern do not uniquely determine moral judgment.** Take two outcomes with known burden vectors \(a=(0,5)\) and \(b=(3,3)\). On nonnegative burdens, both

\[
V_1(h)=h_1+h_2,\qquad V_2(h)=h_1^2+h_2^2
\]

are symmetric and strictly increase when one burden increases with the other unchanged. Minimizing \(V_1\) favors \(a\), since \(5<6\); minimizing \(V_2\) favors \(b\), since \(18<25\). Therefore those facts and limited ethical constraints leave the choice unsettled. These scores are countermodels, not proposed complete moral theories.

**A shared best response eliminates the instrumental benefit of a costly pure-information query.** For this proposition only, suppose a fixed utility \(u\), action set \(A\), and finite current possibility set admit an action \(a^*\) with

\[
u(a^*,w)\ge u(a,w)\quad\text{for every }w,a.
\]

A query returns signal \(Y\) and costs \(c>0\) in that same utility. Fix any probability distribution over the current situations and any conditional signal law for the query; these define the expectations below. The query changes no state, available action, consequence, or obligation. For any later response rule \(d(Y)\), pointwise optimality and expectation give

\[
\mathbb E[u(d(Y),w)]-c
\le\mathbb E[u(a^*,w)]-c
<\mathbb E[u(a^*,w)].
\]

Thus immediate action strictly dominates the query. At zero cost the query cannot improve this utility. This result is conditional on the represented possibilities and purposes; a missing consequence, independent duty to inquire, or inquiry that changes feasible actions can invalidate its premises.

## What the formalization cannot guarantee

If two situations produce identical complete observation histories under every permitted inquiry policy, a deterministic process restricted to those histories produces the same judgment in both; a randomized process produces the same distribution. Equality merely of isolated marginal observations is insufficient for this premise. If the two situations require disjoint responses, no such process can guarantee success in both. More internal reflection alone cannot supply the missing distinction. New access or a response acceptable across both may change the problem.

This does not make all omissions undiscoverable. The cross-session work supplies examples of richer records, new combinations of existing distinctions, protected access to evidence, and revision of admission rules. It does mean that \(\mathcal G\) and \(\mathcal U\) require mechanisms and contact with the world. Their presence in an equation is not a completeness certificate.

Likewise, a single feasible action can produce identical behavior in a wise and an unwise person. Outcomes depend on opportunity and circumstances as well as judgment. Neither one good outcome nor one failure identifies the capacity described by the proposed root.

## What has been achieved

We now have a formal state, a judgment correspondence, a proposal generator, a reasoned revision relation, explicit ethical premises, and elementary propositions constraining their use. The finite decision theorem was checked against direct policy enumeration in all 2,560 combinations of acceptable-action tables and observation partitions for three situations and three actions. All matched: 1,289 admitted a policy and 1,271 did not. A further 80 exact cases checked a bounded query extension with resource, deadline, permission, and informativeness constraints. These finite checks corroborate the construction; the general finite result rests on the proof above. Verification and exact examples are preserved in the [check record](root-of-wisdom-formalization-checks.json).

The central remaining hypothesis is that the reciprocal connection among concern, understanding, and judgment explains a practical source of wisdom. Establishing that requires independently specified contrasts, prospective applications, comparison with serious alternatives, and attention to cultivation. More symbols cannot discharge those obligations.

This formalization therefore supports a precise claim: **we have specified a family of situated, ethically committed, corrigible judgment processes and established conditional limits on some of their decisions.** Whether that family captures “the root” remains open to argument and evidence.

## Relation to the other sessions

This is a new integration of the [cross-session assessment](root-of-wisdom-cross-session-assessment.md), whose [evidence record](root-of-wisdom-cross-session-evidence.json) preserves the sources. The sources supply protected-policy constructions, separate mechanisms of access and correction, paid evaluator revision, implemented admission-rule changes, and the explicit ethical proposal. The architecture and notation here are our proposed synthesis. The proofs above are self-contained elementary arguments; no claim of mathematical novelty or universal decision procedure is made.
