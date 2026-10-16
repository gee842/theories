# A situated normative specification for the continuation framework

**Status: explicit candidate commitments, elementary conditional results, and a constructive decision procedure.** This note closes a specification gap; it does not claim that ethics has been derived from dynamics, that participants have adopted this procedure, or that the procedure has been empirically validated. It proposes no universal scalar objective. Its normative scope is human and AI institutions where questions of standing, justification and authority arise. Ecological regulation can be described by the general architecture without attributing those institutions or obligations to organisms.

## 1. What the existing theory already commits to

The existing [v7.3 normative statement](../../../../drafts/2026-10-02-iaseai-selecting-the-selectors/v7.3/src/core/10_s01.md) distinguishes values from theorems. Its V1–V5 concern shared purposes, protection from large-scale loss of life and irreversible loss of consequential human decision authority, meaningful contestation by affected parties, productive authority, and bounded competition that does not concentrate control over shared conditions. It separately distinguishes essential services from an incumbent organization's tenure. Standing for AI systems remains an explicitly open normative question; this note does not settle it by notation.

The [general framework](../README.md) adds two necessary cautions: persistence is not alignment, and changing a standard is not the same event as restoring a condition. The [alignment-on-cognition corpus](../../../../theories/alignment-selection-on-cognition/README.md) also distinguishes recorded refusal from consent, and effective agency from an autobiography maintained by an operator. These are the starting commitments, not conclusions established by a stability theorem.

Here is the proposed normative relation: **an institution should sustain the specified conditions of affected parties' lives and agency, while retaining effective, accountable ways for those parties to contest the institution's account of those conditions and change its direction.** “Specified,” “affected,” “agency,” and “accountable” require situated interpretation. The proposal permits replacement of practices, evaluators and institutions. It does not protect every existing preference, every available option, or every incumbent's survival.

The normative problem has two sides. A system may preserve an oppressive charter very reliably; it then fails the proposal's substantive commitments. A morally attractive charter may lack any dependable means of implementation; it then fails its practical commitments. Neither a good declared purpose nor self-maintenance establishes the other.

## 2. A charter is part of the modeled situation

For a declared domain and horizon, write a charter as

\[
\mathcal N=(P,S,\mathcal B,\{\succeq_i\}_{i\in P},\mathcal A,\mathcal U).
\]

- \(P\) names represented parties and claims, including disclosed proxies for parties unable to participate directly.
- \(S\) specifies standing: entry of claims, access to relevant reasons and evidence, response duties, and routes to challenge. Standing is distinct from voting weight, officeholding and veto power.
- \(\mathcal B\) specifies protected predicates over outcomes and their histories, including floors, deadlines and any explicitly permitted risk. These need not share a unit.
- \(\succeq_i\) is party \(i\)'s currently expressed, potentially incomplete evaluative relation over the proposals under consideration. There need be no common cardinal scale or complete ranking.
- \(\mathcal A\) specifies who can authorize ordinary decisions and amendments, how disagreement is resolved, and which changes require distinct treatment.
- \(\mathcal U\) records admitted empirical uncertainty, observation limits and the horizon of any assurance claim.

This is a disclosed normative reference, not a complete psychological description. A refusal, a missing response and an incomparable pair are different records. Silence must not be converted automatically into endorsement. Nor does an affected party's standing imply an unlimited right to prevent restraints on harms that party causes.

The implemented institution is another object. Let

\[
s_t=(y_t,r_t,\psi_t,g_t,v_t,\ell_t),\qquad
s_{t+1}\sim K(s_t,\text{proposals}_t,\text{disturbances}_t).
\]

Here \(y\) contains relevant physical and social conditions; \(r\) implemented rules; \(\psi\) current interpretations and evaluations; \(g\) the people, skills, time, records and facilities carrying review and execution; \(v\) the installed charter version; and \(\ell\) the retained decision and dissent record. Turnover and selection change \(g\), \(r\) and \(v\). The actual kernel may omit claims, alter records, install an unauthorized rule or fail to execute an authorized decision. Those events are model outcomes, not excluded by calling the system constitutional.

Normative assessment compares this actual history to a stated charter and to explicitly disputed alternatives. The charter is not an invisible controller that makes the history comply. Different justified-looking charters can assess the same history differently; that disagreement must remain visible.

**Counterexample: durable and revisable is not sufficient.** An institution can renew its reviewers indefinitely, accurately measure two groups' outcomes, and repeatedly revise operational rules in response to the first group's changing needs while knowingly maintaining an avoidable injury to the second group. Its rules really change, its information need not be false, and its continuation mechanism can work. A charter protecting the second group's bodily safety rejects the arrangement even when the installed criterion accepts it. Adding more operational revisability does not supply the missing standing or substantive protection. If “revisability” is instead defined to include those protections, its normative content has been put into the premise and must be disclosed.

### Standing beyond the currently powerful

An operational claim to standing should identify a causal exposure or dependence, the claim's bearer, the represented concern and the means of challenge. Power, current participation and ability to pay are not sufficient membership criteria under this proposal. An access threshold used to make a study finite is a disclosed limitation, not proof that excluded effects do not matter.

Future parties cannot express contemporaneous consent. A present representative can make a defeasible claim on their behalf, record its empirical basis, and preserve conditions under which later people can revise it. That is representation under uncertainty, not future consent. Nonhuman dependence can enter through stated protections of habitats, organisms or ecological functions. Whether those protections recognize intrinsic standing, human dependence, or both is a substantive commitment that must be named. Ecological persistence alone does not decide the issue.

No finite registry guarantees that it has found every affected party. New claims need an entry route, and the resources and permissions that make entry effective belong in \(g\) and \(K\). A registry closed by the people it benefits is itself a candidate failure mechanism.

## 3. Floors, disagreement and feasible choices

A nontradeable floor is a constraint within a declared decision domain and constitutional version. For example, an institution might protect separate bounds on avoidable injury, access to essential service and timely appeal. Extra output in one dimension does not cancel a recorded breach in another. The institution may dispute or amend the floor through a different procedure, but must not describe that amendment as having satisfied the old floor.

Protected does not mean physically guaranteed. A floor may already be breached, may be infeasible under available actions, or may be uncertifiable from current evidence. These are different findings. Status quo and delay are actions with consequences; they are not automatically safe fallbacks.

**Result 1: a finite penalty is not generally an absolute floor.** Suppose a safe option has benefit zero and no violation. The available unsafe options can provide arbitrarily large benefit \(B\), each with the same floor violation \(\delta>0\). Any score of the form \(B-\lambda\delta\), for finite fixed \(\lambda\), prefers some unsafe option: choose \(B>\lambda\delta\). Thus this class of compensatory scores cannot implement the declared nontradeability over that option domain.

This elementary result does not rule out optimization, all scalar representations, or exact penalty methods under additional assumptions. If benefit differences have a known bound and violations have a positive minimum size, a sufficiently large penalty can reproduce the finite decision ranking. Hard feasibility restrictions and explicitly prioritized constraints are also available. The point is to state which meaning is intended rather than quietly convert a floor into a price.

For a finite proposal set \(U\), let \(U_{\mathcal N}(s)\) be the proposals that meet the declared resource, physical, informational and authorization conditions under the stated uncertainty. This is a **conditional admissibility assessment**; it is neither universal moral permission nor a claim of complete observation. Once a candidate set is nonempty, retain its nondominated proposals under the parties' disclosed relations:

\[
a\succ_P b\quad\Longleftrightarrow\quad
\bigl(\forall i,\ a\succeq_i b\bigr)
\land\bigl(\exists j,\ a\succeq_j b\ \text{and not } b\succeq_j a\bigr).
\]

With reflexive transitive relations on a finite set, this strict dominance relation is acyclic, so a nonempty admissible set has at least one nondominated member. That simple construction preserves incomparability. It does not choose a unique action, turn unexpressed concerns into assent, or prove that unanimity is achievable. A declared, contestable decision rule must resolve remaining disagreements, including burdens imposed on dissenters. Majority choice, consent for a particular intervention, delegated judgment and randomized allocation are different normative options, not interchangeable implementations of a mathematical optimum.

If \(U_{\mathcal N}(s)\) is empty, the procedure must report the conflict. It can seek additional capacity, change the proposal, question a factual premise, or invoke an explicitly authorized emergency process. It cannot truthfully certify all floors by choosing a convenient scalar score. Where some breach is unavoidable, the decision and dissent remain recorded as such; mathematical infeasibility does not itself determine who should bear the loss.

### The formation model gives an explicit conflict after discovery

The accompanying [formation construction](FORMATION.md) retains expected physical harm \(h_x\) separately in each of four binary-attribute contexts and an action burden \(B=\Pr(a=1)\), with commitments

\[
h_x\le r\quad\text{for every context }x,\qquad B\le b.
\]

In its stated binary task with noise \(\nu\) and equal harm ceiling \(r\in[\nu,1/2)\), adequate representation, evidence and execution still require a minimum action-1 burden

\[
b_{\min}=\frac{1-\nu-r}{2(1-2\nu)}.
\]

For \(\nu=.1\) and \(r=.2\), this is \(7/16=.4375\). Burden ceilings .50 and .45 permit a feasible response; .40 does not. The constructive rule has two harm values, \(\nu\) and \(r\), over the four contexts. These are expected consequences under the stated stationary population, not a promise that every realized batch satisfies a pathwise quota. The bound is a property of that task, not a universal tradeoff. Its normative lesson is precise: a stricter burden protection can conflict with the accepted harm protections even after the relevant distinctions have been discovered and action is available. More deliberation or better representation cannot by itself remove this physical feasibility conflict.

Relaxing \(r\), relaxing \(b\), changing the available interventions and reducing their actual harm or burden are four different moves. The first two amend commitments; the latter two alter capabilities or consequences. A decision can reasonably consider all four, but should not report a relaxed commitment as a physical improvement. Nor does the inequality itself decide which commitment should change or whose consent is required. If the charter changes, equation (1) below and the versioned history keep the changes distinct.

## 4. Revision can be learning, accommodation or coercion

Goals and representations are formed in relationships. Their change is not inherently suspicious, and keeping a person's current expressed preferences fixed is not a general protection of agency. New testimony can reveal an excluded harm; encounters can change a person's conception of a good life. Conversely, threats, dependency and restricted alternatives can produce sincere adaptation to mistreatment.

For a measured condition \(y\), an evaluative standard \(\psi\), and an expressed margin \(b(y,\psi)\), a discrete change has the exact decomposition

\[
\begin{aligned}
b(y',\psi')-b(y,\psi)
={}&[b(y',\psi)-b(y,\psi)]\\
&+[b(y',\psi')-b(y',\psi)].
\end{aligned}
\tag{1}
\]

The first term measures the outcome change under the previous standard; the second measures the effect of revising the standard at the new outcome. This is an arithmetic identity, not an ethical ranking. Reversing the order allocates any interaction differently, so the report should declare its order and retain both measurements. Neither decomposition identifies the reasons for revision.

**Counterexample: approval is not recovery.** Let a measured condition decline as \(y_t=2^{-t}\), while the accepted floor follows \(a_t=2^{-t-1}\). Every new compliance margin \(y_t-a_t\) is positive; every fixed positive original floor is eventually crossed. Whether a lower floor is justified requires an explicit argument. Repeatedly relabeling the margin cannot establish material regeneration.

**Counterexample: endpoint agreement does not identify legitimacy.** Two people can end with the same stated ranking and behavior, one after voluntary discussion and one after an undisclosed credible threat. If the available record contains only that endpoint, no classifier on that record can distinguish the histories. A system that calls every stable preference “authentic” has assumed away this distinction. More informative process records may help, but there is no perfect observer of consent inside the present models.

The proposed operational response is to retain the grounds and conditions of a consequential revision: what new evidence or experience became available, whose options and dependence changed, what refusal or dissent was expressed, which claims were omitted, and which obligations were explicitly relaxed. A recorded override is an override, even if the institution regards it as justified. These records support contestation; possessing a record does not itself make the decision legitimate.

Past standards need not bind forever. Otherwise new concerns or corrections to past injustice could become impossible. A versioned comparison preserves the fact that an obligation was revised without requiring every historical obligation to remain simultaneously enforceable. The burden of justification for that revision is normative and institutional, not supplied by equation (1).

## 5. A constructive amendment procedure with fallible carriers

Consider an institution with a finite number of work, inquiry and teaching opportunities. A credible procedure must allocate some of them to maintaining the ability to review decisions, record reasons, execute changes and train successors. A review that uses unavailable staff time is a failed implementation, even if its formal authorization is impeccable.

The following is a candidate procedure, not a universally legitimate constitution:

**First, a claim becomes a proposal with an identified consequence and bearer.** An affected party or disclosed representative can submit it through specified access routes. Admission, representation and response time are independently observable events. Exclusion can occur at any of them. The procedure records unresolved claims and their delays rather than treating absence from the agenda as absence of concern.

**Second, the institution distinguishes a changed fact, a changed interpretation, a changed objective and a changed decision right.** A proposal can contain several. It carries a versioned comparison of independently observed conditions, current floors, proposed floors and the reasons for change. A new concern can be admitted without translating it into the incumbent's preferred metric.

**Third, a review with declared capacity considers alternatives and disagreement.** Review assignments, conflicts of interest, missing evidence and available replacement personnel are recorded. The admissible set and nondominated set above can structure the comparison. A temporary trial can be useful when genuinely reversible; merely naming a trial does not make its harms reversible. Resource use and decision delay enter the assessment alongside the intervention's expected effects.

**Fourth, authorization and execution are separate events.** The installed rule determines whose decisions can be enacted, but the actual mechanism may fail. A proposal that changes standing or the amendment procedure is evaluated and labeled as such; it cannot acquire approval merely by deleting its opponents from the new electorate and applying the new rule retrospectively. This is a proposed restriction on validity. Whether actual actors can circumvent it is a question for the transition law and evidence.

**Finally, successor formation and reopening are part of continuation.** Records must remain usable, inquiry and execution skills must be transmitted or reconstructed, and a successor can challenge the prior decision through the stated routes. Neither the incumbent panel nor its doctrine is permanent. The institution tracks delivered replacement capacity rather than counting promised training or formal offices as renewal.

There is no unpaid, infallible supervisor above these stages. The same endogenous system appoints reviewers, maintains records and permits amendments; strategic suppression, inattention, exhaustion and corrupt succession must remain possible transitions. The normative reference identifies when such a transition violates a commitment. It does not causally block the transition. A domain model must supply and test the actual resistance or recovery mechanism, with explicit environmental support where needed.

**Result 2: continually fallible amendment does not guarantee permanent revisability.** Let \(A_n\) mean that protected standing has never been irreversibly lost through the first \(n\) amendment opportunities. Suppose, conditional on every surviving history before opportunity \(n\), the chance of irreversible loss is at least a stated \(\varepsilon_n\in[0,1]\). Then

\[
\Pr(A_n)\leq\prod_{j=1}^{n}(1-\varepsilon_j).
\tag{2}
\]

Proof: conditional survival at opportunity \(n\) is at most \(1-\varepsilon_n\) on \(A_{n-1}\). Taking expectations and applying induction proves the bound. No independence assumption is needed. If \(\sum_n\varepsilon_n=\infty\), the bound tends to zero; a uniform positive hazard is a special case.

This is a restriction on indefinite assurance, not a recommendation to prohibit amendments. Finite horizons, recoverable failures, protected reachable subsets and declining hazards yield different questions. Recoverable exclusion is still a violation of a never-excluded commitment. Recovery can meet a separately stated restoration obligation, whose delay and burden must be measured. A summable upper bound on per-opportunity failure probabilities can support a union-bound assurance, but cannot establish that a procedure deserves its authority.

An unchangeable guardian avoids neither side of the problem: it can enforce an unjust charter, and its own persistence still needs explanation. Conversely, unrestricted power to erase all protections is inconsistent with an unconditional promise that those protections endure under every permitted amendment. The bounded constructive target is a procedure that allows specified revisions while maintaining specified protections over stated conditions and horizons, with failures and revisions of those protections openly assessed.

## 6. A concrete plural decision and an amendment failure

Consider four hypothetical service routines. Adequacy is measured separately for two affected groups; capacity is a separately measured ability to investigate and execute later corrections. Numbers illustrate a decision, not fitted social measurements.

| Routine | Completed cases | Group 1 adequacy | Group 2 adequacy | Corrective capacity |
|---|---:|---:|---:|---:|
| A | 100 | .95 | .55 | .90 |
| B | 80 | .85 | .85 | .90 |
| C | 110 | .90 | .80 | .40 |
| D | 75 | .80 | .90 | .90 |

Suppose the current charter protects adequacy of at least .80 for each group and capacity of at least .80. B and D meet these point-estimate constraints; A and C do not. Group 1 can prefer B, group 2 D, and administrators can prefer B's case volume. There is genuine residual disagreement, even after the floors are imposed. The method identifies that disagreement instead of silently resolving it through a sum of cases and adequacy scores.

An incumbent can make A appear compliant by reducing group 2's floor to .50, or make C appear compliant by reducing the capacity floor to .30. Neither amendment changes the table's underlying consequences. If group 2 loses standing before the vote, subsequent unanimous approval among those remaining is not consent by group 2. If the capacity reduction eliminates successor reviewers, a formally open appeal route may cease to function after turnover. These are concrete links between normative specification and the general theory's selection, representation and regeneration mechanisms.

A legitimate amendment could also expand the table: newly admitted testimony might reveal a previously unmeasured harm caused by B and D. Protecting the old menu against all revision would then defeat the purpose of contestability. The procedure must admit the concern and reconsider feasible responses, while reporting which previous commitments still hold. If new constraints make every routine unacceptable, that is a substantive conflict to address, not proof that the new concern should be discarded.

## 7. What can be validated, and what remains a human commitment

This specification permits falsifiable implementation claims. A protected claim-entry route can be tested for whether equally situated claims receive different admission after controlling the claimed relevance. Review capacity and turnover can be varied while separately observing unresolved claims, actual reversals, execution and loss of records. Matched final approval can be compared with process histories to test whether endpoint agreement conceals different refusal and dependency conditions. Amendment reports can be checked against equation (1), and finite-horizon failure claims against the actual modeled or observed hazards. Such tests must disclose measurement limits and appropriate research protections; none has been conducted by this note.

Validation can establish that a procedure behaves as specified, that it maintains a chosen protection in a bounded model, or that participants judge its burdens and decisions acceptable under a studied process. It cannot establish from those facts alone that the represented parties are exhaustive, the floors are morally correct, a majority has unlimited authority, or future people have consented. Nor can selecting a stable preference-update mechanism settle whether its influence is legitimate.

The remaining commitments therefore have to be adopted, challenged or revised by people: the domain of standing; treatment of future and nonhuman interests; protected losses; permissible exceptions and risk; decision rights when acceptable interests conflict; and what counts as a legitimate amendment. The existing manuscript has already proposed some answers through V1–V5. This note makes their operational consequences and unresolved choices more explicit rather than replacing them with an allegedly neutral optimum.

**Completion relative to scope** would mean that a declared application supplies those commitments, its actual review and implementation mechanisms, observable consequences, finite assurance boundaries, a treatment of disagreement, and tests of its failure modes. It would not mean that a universal ethics had been proven or that the normative layer could never require revision. The present contribution is a transparent candidate specification and two elementary constraints on its implementation; adoption, domain-specific calibration and empirical validation remain separate work.
