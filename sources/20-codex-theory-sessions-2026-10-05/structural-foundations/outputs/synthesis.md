# Structural foundations of continued transformation

Research synthesis for Ren, 5 October 2026. This session proposes a formal working language and tests its limits. It does not establish a new universal law, mathematical originality, empirical cross-domain validity, or a solution to AI alignment.

The strongest formulation is a theory of **feasible transformation under changing conditions of access**. A transformation can change not only an outcome, but also the resources, information, relationships, rules, and representations through which later transformations become available. The important mathematical object is therefore an admissible sequence or policy, with its timing and uncertainty, rather than an inventory of possible actions.

The provisional signature `S=(X,T,R,O)` identifies useful questions but is insufficient as a dynamics. We recommend a small controlled transition semantics with explicit decision information and typed annotations. Existing mathematics supplies the core tools. The research contribution to pursue is a disciplined account of the feedback between selected activity and the conditions of subsequent revision, tested through concrete mechanisms.

## What the proposed signature leaves unspecified

| Proposed component | What must be clarified |
|---|---|
| Configurations `X` | Distinguish the space of configurations from the actual configuration and from an actor's representation of it. State whether the analyst can describe all admitted configurations. |
| Transformations `T` | Distinguish physical execution, expressible proposals, institutionally permitted actions, information-feasible policies, and the action actually selected. |
| Enabling quantities and relations `R` | Typed stocks can have balance equations. Relationships, permissions, trust, and interpretation do not inherit additive conservation merely by sharing this letter. |
| Distinctions `O` | State who can distinguish what, through which channel, at which decision time, with which retained memory and public signals. |
| Update `Phi` | Specify possible outcomes, external influences, event timing, and which agent or environment controls each choice. Updating the tuple alone supplies no such mechanism. |

For example, a correct repair can be physically executable and officially permitted while remaining unusable for a guarantee because its choice depends on an unavailable distinction. Conversely, an unauthorized action can be physically possible. Treating both cases as membership or nonmembership in one transformation set loses the distinction the research needs.

The phrase “transformations that alter their own conditions of possibility” can therefore be retained, provided *possibility* is indexed to the relevant sense and observer. A rule change can alter future physical affordances, institutional standing, available distinctions, or the implemented selection process. Those are different causal claims.

## A small operational core

Use a model

\[
\mathcal M=(Q,A,W,\Delta,I),\qquad
q\xrightarrow{a,w}q' \;\Longleftrightarrow\; (q,a,w,q')\in\Delta.
\]

Here `Q` contains complete configurations at the model's chosen boundary; `A` contains action descriptions; `W` contains environmental choices; and `Delta` specifies the resulting transitions. `I_i(h)` is the decision information available to actor `i` after history `h`. A stochastic application replaces or supplements the outcome relation with a kernel and states its assumptions. The robust and probabilistic interpretations must not be silently exchanged.

The model also declares an initial configuration or uncertainty set, a nonempty disturbance class, and the controller class being assessed. Physically enabled actions must have defined outcomes against all admitted disturbances. Deadlock and invalid attempts need explicit semantics; a missing successor must not make a universal condition vacuously true.

A configuration can be decomposed for a particular application as

\[
q=(x,b,\ell,m,\rho),
\]

where `x` is the other represented configuration, `b` is a vector of typed accessible stocks, `ell` contains relationships and implementation rights, `m` contains retained records and controller memory, and `rho` contains active rule and representation descriptions. This decomposition is optional. The transitions, rather than the names, must establish what each component does.

Use separate predicates or interfaces for physical enabling, representable proposals, submission standing, institutional permission, and execution access. If a rule cannot physically be violated because a device blocks execution, represent that device in the transition mechanism. If violation is possible but sanctioned, represent the violation and its consequences. Formal permission itself does not establish legitimate authority.

The smallest useful language consists of configurations, typed actions and outcomes, available information, and explicitly quantified tests. Tuple length is not a proof of minimality. We are choosing a manageable semantic basis, not proving a unique ontology.

### Rules and representations can change within the model

Let transitions alter `rho`, which in turn affects subsequent action interpretation, information processing, and permission. The model may then represent an amendment to its amendment procedure or a change of the language in which amendments are expressed. Such self-reference does not require an infinite stack of separate dynamical laws if descriptions and interpreters are represented as state.

However, an analyst-level semantics still specifies what those descriptions mean and how changes occur. Moving a rule into a state variable establishes *representability*, not a causal explanation of its discovery, support, enactment, or legitimacy. A generator over a supplied grammar is a bounded generator. It is not unrestricted concept formation.

For a set-indexed family of representational spaces `Q_r`, the tagged union `Q* = disjoint union_r ({r} x Q_r)` can express changes between them in one fixed space. This is an encoding fact when the family and cross-space transitions are specified. It neither proves that future concepts are presently known nor captures discoveries outside the analyst's supplied family. An expanding formal state space and an expanding actor repertoire are not the same assertion.

### Information must include the memory actually available

An admissible rule has the form `pi_i(I_i(h))`. If two histories yield the same decision information, that rule gives the same distribution over next actions. Its random seed or persistent controller state cannot carry hidden information excluded from `I_i`.

Perfect recall is a substantive assumption. Adding an archive-maintenance bill to the physical state does not remove a solver's free memory of every past observation. To study forgetting or paid retention, constrain the policy to the retained register or include the controller's memory mechanism explicitly. The worked example below allows perfect recall and destroys an *unread* archive; it does not pretend that destruction erases knowledge already acquired.

### Capacity is indexed to a test and policy class

For a declared safe region `K`, target `G` contained in `K`, deadline `H`, nonempty current uncertainty set `B`, and admissible controller class `Pi_I`, define robust capacity by

\[
\operatorname{Cap}_{K,G,H}(B)=1
\iff
\exists\pi\in\Pi_I\;\forall q_0\in B\;\forall\text{ admitted environmental outcomes},
\quad q_t\in K\text{ for }0\le t\le H,\quad
\exists\tau\le H:\ q_\tau\in G.
\]

Condition the initial set on the declared current decision information and include any retained controller memory in its configurations. Budgets, observation costs, permission, and delayed prerequisites belong in admissibility and dynamics. A probability of recovery, an expected cost, or a realized trajectory is a different test. Safety only until target attainment is another valid specification; it coincides with safety through the horizon when the target is safely absorbing, as in the installation calculation below. The proposed capacity definition does not say that an actual organization discovers or uses the winning policy.

Four assessments should be kept distinct: a physically possible path; a permitted full-information policy against the declared disturbances; a policy that works using actual information and access against those disturbances; and the outcome distribution of the implemented selector. Counterfactual intervention capacity must additionally name what the intervention supplies. Giving an actor a new sensor or authority changes the assessed system.

## Three conditional constraints

### Support must be available at each required payment

For a nonnegative stock vector with compatible units, use a balance equation

\[
b_{t+1}=b_t+r_t-c_t+Nv_t-\lambda_t,
\]

where `r` records accessible inputs, `c` withdrawals, `Nv` explicitly modeled conversions, and `lambda` losses or discarded overflow. Telescoping yields

\[
\sum_{t<k}(c_t+\lambda_t-Nv_t)\le b_0+\sum_{t<k}r_t
\quad\text{for every prefix }k
\]

whenever `b_k >= 0`. This is an accounting identity plus a necessary condition. Use microsteps if an input arrives after a fee is due. Stocks held elsewhere count only after the route, right, and time of access are represented.

Conversions require enabling conditions. With zero units of both materials, the transformations `A -> B` and `B -> A` have total net change zero, but neither can start. A balanced final state equation does not establish an executable schedule. Similarly, a declared support can cease to be necessary when an alternative technology performs the function. The necessary condition belongs to the chosen function, substitution routes, boundary, and timescale.

The parent research's U01 and U16 already establish scalar prefix accounting and financing chronology. Our use is a typed, operational restatement with explicit conversion and reachability warnings, not a new conservation principle for institutions.

### Absent distinctions cannot guide differentiated responses

If `I(h)=I(h')`, then a policy using only that interface gives the same response distribution. More generally, for observation laws `P` and `Q` and any common response kernel `pi`,

\[
\operatorname{TV}(P\pi,Q\pi)\le\operatorname{TV}(P,Q).
\]

Thus identical permitted evidence cannot produce systematically different responses between the two worlds. The result does not forbid fresh experiments, changed observation channels, or environmental interactions that create a distinction. Those must be included in the subsequent information process.

The quantifiers matter:

\[
\forall\theta\;\exists\pi_\theta\text{ that succeeds}
\quad\not\Rightarrow\quad
\exists\pi\text{ using available information}\;\forall\theta\text{ it succeeds}.
\]

The parent record's U05 and U22 already establish versions of these limits. They are conditional information results, not a claim that more computation is always useless or that every unfamiliar proposal is worthwhile.

### Corrective prerequisites must fit one executable sequence

When a particular revision procedure requires discovery, authorization, and execution, every successful run must pass the corresponding prerequisites at the required times. Each prerequisite being individually reachable is insufficient. From one available token, either an information operation or an authorization operation may be affordable, while both together are impossible.

Nor is discovery before authorization a universal ordering. A standing permission may be secured in advance, a trial may itself generate discovery, or stages may overlap. The model must specify the actual causal dependencies. A proposed bottleneck is necessary only if every successful admissible route crosses it; a substitute route can invalidate that claim.

This constraint turns the broad phrase “maintain the capacity for correction” into a testable question: which successful policies remain feasible after current activity changes their future enabling conditions? It does not prescribe keeping every institution or every repair mechanism intact.

## Worked example with paid substitutes

A hidden fixed condition is either `0` or `1`. Applying its matching revision succeeds; applying the other irreversibly fails. The controller starts without knowing the condition or holding a permit. It has a visible reserve, an unread diagnostic archive, and a cheap authorization service. Every action prepays its cost.

| Action | Cost | Effect or prerequisite |
|---|---:|---|
| Inspect archive | 1 | Reveals the condition if the archive survives |
| Test afresh | 2 | Reveals the condition without the archive |
| Authorize | 1 | Supplies a permit if the cheap service survives |
| Rebuild authorization | 2 | Supplies a permit without that service |
| Apply 0 or 1 | 1 | Requires a permit in the authorized model; succeeds only if correctly matched |
| Routine activity | 1 | Destroys the unread archive and cheap service, revokes the permit, and preserves any already acquired diagnosis |

The destructive effects of routine activity are supplied causal assumptions. They represent one possible mechanism to test, not a claim about all routine work. The action grammar and perfect diagnostics are also supplied. No candidate invention is claimed.

Let `c_D` be the cheapest available diagnostic cost and `c_P` the cheapest permit cost. The exact thresholds are:

| Assessment | Minimum reserve with both cheap routes intact |
|---|---:|
| Successful physical execution chosen with full information, disregarding permission | 1 |
| Successful authorized execution chosen with full information | 2 |
| One authorized policy guaranteed to succeed in either hidden condition using available observations | 3 |

In general the third threshold is `c_D+c_P+1`. Every authorized successful path pays for a permit and execution. A robust common policy must also distinguish the conditions before execution, because the correct actions conflict and a mistaken attempt is irreversible. Only a diagnostic creates that distinction. These three expenses give a lower bound; inspecting, authorizing, and applying the indicated revision attain it. Authorization may precede inspection, so the proof does not assume a universal stage ordering.

After one initial routine action, both cheap routes disappear. The remaining route costs `2+2+1=5`; including routine itself, **six initial units** are necessary and sufficient. Substitution keeps revision possible at a higher cost. Starting from three units, robust correction is initially available and becomes unavailable after routine, although a favorable physical repair still exists.

At initial reserve two with the cheap service, authorization followed by a fair guess succeeds with probability one half in each condition. Thus failure of a guarantee does not mean every run fails. A controller that knows the condition can succeed at that same reserve. This is a quantifier separation, not a disagreement over bookkeeping.

The installed regime receives one explicitly supplied external unit before each later one-unit operating expense. It can therefore continue even if installation leaves reserve zero, conditional on that external input and timing. The code verifies installation; the subsequent loop is established by the balance identity `b'=b+1-1`. It does not prove self-renewal of the external source.

Finally, assign routine activity an immediate output score of two and other pre-revision actions zero. A supplied rule maximizing that score repeatedly chooses routine and exhausts an initial three-unit reserve in three actions. A winning policy existed but was never used. This demonstrates the distinction between capacity and its selection under an imposed rule; it does not explain the evolution or ethical merit of that rule.

The [proofs and countermodels](propositions-and-countermodels.md), [executable checker](verification/check_revision_model.py), and [exact results](verification/revision-model-results.json) preserve 32 reserve-and-route cases, 24 second-implementation policy-tree comparisons, eight routine-first cases, and 15,624 ledger cases. All assertions passed. The two policy computations share transition code and recursive logic; the analytic lower bounds and witness policies are the separate mathematical checks. These finite synthetic results are not empirical validation.

## Composition and equivalence across implementations

Two components with disjoint resources, compatible actions and clocks, independent transitions, and local safety-preserving controllers maintain the product of their safe regions. The proof is componentwise induction. The independence assumptions do the work. If both components instead spend the same one-unit reserve, two separately feasible one-unit tasks need not be jointly feasible.

Conversely, connection can create a missing circulation or information route. In open Petri nets, endpoint reachability summaries need not compose exactly because a joint execution can pass back and forth across a boundary. The primary result is in [Baez and Master, section 6](https://arxiv.org/html/1808.05415v6); the detailed source audit is in the [literature map](literature-map.md).

Even matching all ordinary completed event traces can lose a control guarantee. One system performs `a` and then lets its controller choose `b` or `c`. Another performs `a` while the environment commits it to a branch where only `b`, or only `c`, remains possible. Both admit exactly the traces `{ab,ac}`. Only the first can guarantee `b`. The [foundation checker](verification/check_foundation_examples.py) enumerates this example.

A useful replacement criterion must preserve the interface relevant to the claim. The [formal foundations memo](formal-foundations.md) proves a sufficient finite-horizon criterion: map concrete information to abstract information without hidden-state access; implement each abstract policy action uniformly from the concrete information; match every concrete successor to an allowed abstract successor; and preserve safety, target, timing, and relevant budgets. An abstract winning policy then lifts by induction. This is a restricted application of established [alternating refinement reasoning](https://www.cis.upenn.edu/~alur/Concur98.html), not a new general equivalence theorem.

The important research obligation is to exhibit such a correspondence or a direct intervention test. Renaming a payment, chemical feedstock, and authorization link “support” does not establish that a theorem about one transfers to the others.

## Selection is a mechanism within the core

Selection requires a specified contribution or transmission relation. For initial weights `p_i` and nonnegative differential contributions `w_i`, with positive mean contribution, an elementary selection step is

\[
\widetilde p_i=\frac{p_iw_i}{\sum_jp_jw_j}.
\]

A separate transmission kernel can map these contributions into successor configurations. The model must identify what is copied, retained, or replaced, and what determines the weights. A learning algorithm, market, population, and deliberative institution do not become the same algorithm merely because each changes a distribution.

Multiplying every `w_i` by the same positive factor leaves normalized shares unchanged. It changes absolute contributions. This elementary ambiguity is why share-only success cannot establish absolute renewal; the parent record already formalizes a continuous-time version as U02. Resource dynamics and support dependencies require additional observations and assumptions.

The classical selection decomposition supplies accounting for differential contribution and transmitted change; it does not by itself supply the causal dynamics. See [Price's original paper](https://sites.santafe.edu/~altenber/LIBRARY/REPRINTS/Price_selection_Nature.1970.pdf). Feedback from selected activity to resource environments is also established subject matter, including [niche-construction models](https://pmc.ncbi.nlm.nih.gov/articles/PMC17873/). The present target must therefore earn its value through an explicit interaction, invariant, discriminating prediction, or useful abstraction.

## Continued becoming and ethical commitments

This core can represent persistence, renewal, recovery, replacement, changed rules, and newly admitted descriptions. It does not reduce continued becoming, 生生, to the survival of one fixed identity. A function may continue through different carriers; one carrier may persist while disabling others' future agency. A model that forbids all replacement would prejudge the question.

A workable operational proposal is a **profile of tested capacities**: which functions can be maintained, which failures can be corrected, which successors can establish themselves, and which evaluative or representational revisions can become effective under declared conditions. This profile is partial and situated. It is not a definition exhausting the philosophical meaning of 生生, and no translation is being asserted as canonical.

Persistence, novelty, and reachability cannot supply an ethical order on their own. A stable coercive arrangement can persist; adding new ways to coerce can enlarge its reachable state set. A peaceful retirement can end an organization while preserving the people and functions that mattered. The protected functions, affected parties, standing to contest, and limits on harmful revision must be explicitly defended.

Under a fixed objective and unchanged costs, adding purely optional controller actions that can be ignored cannot shrink its feasible policy set. That weak mathematical monotonicity must not be misreported as ethical improvement. New adversarial actions, unavoidable burdens, altered incentives, or omitted stakeholders change the comparison.

## What this offers AI alignment and human coordination

The immediate use is diagnostic. Ask whether consequential experience can become an effective reason for change through the system's actual information, proposal, decision, and implementation channels. Track how present activity changes those channels. This framing distinguishes improving prediction inside a supplied representation from gaining a route to challenge that representation.

| Structural question | Possible AI interpretation | Possible human coordination interpretation |
|---|---|---|
| What distinguishes relevant conditions? | Evaluation data, monitoring, retained evidence | Situated experience, records, testimony |
| What can be proposed and interpreted? | Supplied policy or model grammar, update interface | Available concepts, agendas, evidence rules |
| Who can authorize a change? | Control of deployment or update credentials | Standing, voting, appeal, amendment procedures |
| What makes implementation feasible? | Compute, operators, access, rollback infrastructure | Funds, skills, time, physical and organizational access |
| How is future correction affected? | Updates altering monitors, incentives, or intervention channels | Current success changing inquiry support, archives, or decision rights |

These are candidate mappings. They require measured mechanisms before a formal claim transfers. A credential and a legitimate mandate are not interchangeable. Multiple actors also have separate information: giving an analyst their combined knowledge supplies a stronger coordinator than the institution may possess. Communication, disagreement, incentives, and contested authority require explicit treatment.

Maintaining a correction mechanism is already part of the [corrigibility research agenda](https://intelligence.org/files/Corrigibility.pdf). The present structure can expose an unmaintained prerequisite or a missing implementation route. It does not establish that a proposed correction reflects human values, that a controller will cooperate with it, or that the authority invoking it is legitimate. Preserving an initial objective through self-modification likewise does not validate that objective; relevant formal results have explicit fixed-reference assumptions, as in [Everitt and colleagues](https://www.hutter1.net/publ/selfmod.pdf).

## Focused literature map and evidential status

The [full literature map](literature-map.md) records twelve core source groups with access limitations and precise mismatches. The most useful connections are:

- [Ashby](https://ashby.info/Ashby-Introduction-to-Cybernetics.pdf): behavioral structure across implementations is an established starting point.
- [Interface automata](https://research-explorer.ista.ac.at/record/4622), [open Petri nets](https://arxiv.org/abs/1808.05415), and alternating refinement: boundaries, interaction, and control must survive abstraction.
- [Autocatalytic sets](https://link.springer.com/article/10.1186/1759-2208-3-5): structural mutual enabling differs from funded, timed operation.
- [Partial-observation games](https://arxiv.org/abs/1107.2141) and [interactive unawareness](https://faculty.econ.ucdavis.edu/faculty/schipper/unaw.pdf): unavailable evidence and unavailable expressive distinctions need separate treatment.
- [Institutional grammar](https://www.cambridge.org/core/journals/american-political-science-review/article/abs/grammar-of-institutions/7D37CD3BC5ED2D9FD57D2EE292958F47), [reflective rewriting](https://www.sciencedirect.com/science/article/pii/S1571066105825538), selection, and corrigibility: rules, rule change, transmission, and maintained correction each have substantial prior art.

The report's balance identities, information bounds, finite reachability arguments, and refinement proof are conditional mathematics. The chosen capacity profile and semantic core are modeling proposals. The costs and transition table are constructed assumptions. Claims that these variables predict actual institutional or AI outcomes are empirical hypotheses still requiring tests. Shared agency and legitimate revision are explicit normative commitments. None of these evidential categories substitutes for another.

## Concrete next target

First test a proposed capacity summary under component replacement. Couple a small productive process to a paid inspect-authorize-implement process. Compare a replacement that satisfies the interface-preserving criterion with one matching current output but erasing an interaction or decision-relevant record. Seek a proof of transfer in the first case and an exact counterexample in the second.

Then make correction recurrent: it should help renew the productive support that pays for future correction. Allow paid standby, suspension, rebuilding, and replacement. The quantitative target is an explicit frontier relating reserve, rebuilding delay, and disturbance spacing, compared against the best reserve-only or suspend-and-restart controller. A no-hazard case and a fixed-fault perfect-recall case must expose unnecessary repeated inquiry.

The [next research protocol](next-research-target.md) specifies timing, controls, resource matching, and the distinction between finite-horizon evidence and indefinite recurrent guarantees. It is unrun. Its purpose is to turn the structural language into a discriminating result, while keeping conceptual discovery, changing purposes, empirical transfer, and legitimacy open rather than solving them by notation.
