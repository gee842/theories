# Investigating the full picture

Research synthesis for Ren, 5 October 2026, Asia/Bangkok.

*Continuation:* the subsequent [access-and-correction study](access-and-correction.md) now supplies an exact counterexample, a conditional pooling theorem, and a model-revision consequence. This first-cycle synthesis retains its original scope; see the [updated research record](research-record.md) for current experiment status.

**The strongest defensible result is a way to connect partial accounts while making the losses in each connection explicit. It is not yet a complete theory of becoming.** The existing results support conditional constraints on continued activity: enabling functions must remain accessible; relevant distinctions must support a timely response; and the people, records, policies, and institutions implementing that response have conditions of operation of their own. They do not establish that every phenomenon, every cultural account, or every ethical obligation is a projection of one discovered structure.

There is nevertheless a precise version of the central idea worth pursuing: **an account can include the processes that produce, apply, and revise accounts.** Its observers need not stand outside the world. Its representations can be partial, costly, socially distributed, and causally consequential. This requires neither omniscient observers nor a universally complete causal graph. It does require distinguishing a representation's physical carrier, its interpreted content, its accuracy, and the legitimacy of acting through it.

This session develops a typed formal core, proves limited preservation results, checks positive and failed mappings, audits the inherited claims, and compares a deliberately small set of primary texts. The calculations are constructed examples and checks of conditional mathematics. They are not new empirical evidence about human institutions or AI alignment, and no mathematical or historical priority is claimed.

## What completeness could mean

The phrase “full picture” currently combines five different ambitions. They need separate success conditions.

| Ambition | Precise question | What can be established here |
|---|---|---|
| Ontological coverage | Does the account include every kind of entity or process that exists? | Coverage of a declared domain can be audited. Unrestricted coverage of reality is not established by a finite list of successful examples or by calling the state space “everything.” |
| Explanatory integration | Do the accounts share mechanisms, constraints, or justified translations that explain something beyond each separately? | Derive results across stated model classes; show which assumptions do the work; predict intervention effects across held-out cases. Common terminology alone does not meet this criterion. |
| Formal expressive capacity | Can the language represent the target distinctions and transformations? | Prove representation results for specified classes, such as finite controlled processes. Encoding a process does not identify its laws, make its predictions computable, or explain its meaning. |
| Predictive constraint | Does the theory exclude outcomes or procedures before they are observed? | State independently measured dependencies, boundaries, interventions, and error tolerances. Test forbidden outcomes or failed forecasts. This is the most direct route to empirical progress. |
| Ethical adequacy | Does the account give defensible protection to affected people, agency, and future possibilities? | Make commitments and conflicts explicit; test whether proposed actions satisfy them. Dynamics can constrain feasibility and consequences without selecting the right commitments. |

These dimensions can diverge. A very expressive language can make no predictions. A successful predictor can omit the production of its own observations. A comprehensive causal description can still fail to justify a choice between domination and shared agency.

The attainable near-term target is **scoped completeness**: for specified questions, interventions, horizons, affected parties, and disturbance classes, account for the distinctions needed to answer those questions, including how those distinctions are acquired and revised. This is a proposed research standard, not a retreat that settles the larger ontological ambition. The larger ambition remains unresolved until a principled reason is given that no relevant kind of phenomenon has been omitted. A family of models is only a means toward integration: the positive conjecture is that a fixed account of how correction is supported and enacted can predict recovery in a second setting from independent measurements, without inventing new mechanisms after seeing its outcomes.

## Three kinds of change must be distinguished

**World change** occurs when a process alters stocks, organisms, tools, institutions, or practices. A repaired sensor changes what can subsequently be observed. A new rule changes who can authorize an action.

**Model revision** changes an agent's representation, hypothesis family, concepts, or evaluative standard. When its carrier changes, this is also an event in the world. But changing an equation on a page does not by itself change the process described by that equation.

**Abstraction** changes the level or resolution of a description. Replacing individual abundances by population shares can discard information without changing any organism. Its adequacy depends on what the new description is expected to preserve.

Consequently “invariant” also needs a type. A conserved quantity stays numerically constant. A controlled invariant region can be maintained by a suitable policy. A representation invariant is a statement preserved by a specified translation. A model-class constraint holds for every process satisfying declared assumptions. Most promising results here are of the last two kinds; they are not universal conserved quantities.

No substantive property can survive completely unrestricted transformations. If a class contains a model satisfying a property and another violating it, and every replacement is permitted, replacing the former by the latter defeats invariance. A useful invariance claim must therefore name its allowed transformations and what those transformations preserve.

## A candidate formal core

The provisional signature \(S=(X,T,R,O)\) is a good checklist but an underspecified mathematical object. It mixes possible configurations, changes, enabling conditions, and accessible distinctions. In particular, a resource quantity, an access relation, a legal permission, and an observation channel are different kinds of object. A single symbol must not silently identify them.

For the finite robust-control results, use the following deliberately modest core:

\[
\mathcal M=(Z,A,F,h).
\]

- \(Z\) is a set of typed process states, including any variables needed for the declared future questions.
- \(A\) is a set of action labels. Joint actions and institutional procedures can be represented, but a single controller is the initial specialization.
- \(F(z,a)\) is a nonempty set of possible next states. An unavailable action leads to a distinguished failure state; alternatively availability can be an explicit relation.
- \(h:Z\to Y\) specifies the observation available at a decision point. A policy chooses from observed histories, not from hidden components of \(z\).

A stochastic specialization replaces \(F\) with a transition kernel and may use an observation kernel. A continuous model needs additional time, regularity, and solution assumptions. These specializations are related tools, not automatically equivalent objects.

Resource accounts, access relations, clocks, and normative specifications are attached explicitly. For example,

\[
z=(x,b,r,m,p,e,d),
\]

where \(x\) records productive conditions, \(b\) accessible resource accounts, \(r\) readiness, \(m\) a model carrier, \(p\) a policy carrier, \(e\) an evaluator or institutional-rule carrier, and \(d\) pending work and deadlines. This list is illustrative, not a universal decomposition. Quantities require units and accounting rules; permissions and standing require relations among actors and actions. They cannot all be added into one “capacity” scalar.

A policy's functional role is to map available information to action. A world model's role is to represent dependencies and consequences. A stored instruction may implement one, both, or neither, depending on how it is used. Institutions can distribute these roles across people, documents, software, procedures, and material infrastructure. Merely adding variables named “belief” and “authority” does not identify their real mechanisms.

One possible explicit chronology is

\[
y_t\sim H(\cdot\mid z_t),\qquad
a_t\sim\operatorname{Execute}(p_t,m_t,e_t,y_t),\qquad
z_{t+1}\sim K(\cdot\mid z_t,a_t).
\]

The state update may change the carriers that determine later observation, action, and evaluation. The realized policy is then endogenous. When studying alternatives, the analyst must state which policy edits are physically and institutionally implementable. Optimizing over every mathematical policy would otherwise give the actor capabilities it does not possess.

The model is **open**: external inputs and unresolved mechanisms may remain boundary conditions. Moving a boundary outward does not prove that all causes have been included. A family \(\{\mathcal M_\theta\}\) can represent uncertainty about transitions, observations, or organization. Guarantees are relative to that family; they do not certify the family's exhaustiveness.

If anticipated organizations use different state types, introduce a schema index \(\sigma\) and a disjoint union \(Z=\coprod_\sigma Z_\sigma\), with specified transitions between schemas. This handles such cases as a new sensor type, a new record format, or a revised action vocabulary. It places the allowable changes in a larger supplied language. It does not demonstrate unrestricted concept formation or capture of every future ontology.

### Evaluation remains an explicit input

Let \(N\) specify protected predicates, affected parties, horizon, burdens, and acceptable risk. A simple safety question uses \(K_N\subseteq Z\). A richer question evaluates a vector such as failure probability, inquiry cost, intervention burden, distribution of access, and opportunities for appeal.

An institution's current evaluator \(e_t\) is something whose operation can be explained. The justification of the researcher's specification \(N\) is a different question. If an institution lowers its own standard after harming someone, the causal fact of revision does not establish improvement. Conversely, a justified revision need not preserve every old standard. The account must state how revisions are assessed and leave real disagreement visible.

## What a mapping promises

Use four distinct terms.

| Term | Required content | What it does not establish by itself |
|---|---|---|
| Interpretation | A justified assignment of formal objects to phenomena, supported by measurement and contextual argument. | A cultural interpretation is not automatically a mathematical map between fully specified models. |
| Projection | A declared map \(q:Z\to\bar Z\), often many-to-one, with its retained questions named. | Every projection is not a dynamically adequate abstraction. |
| Abstraction | A projection plus an explicit preservation contract for transitions, observations, actions, costs, or predicates. | Preserving observations does not automatically preserve interventions, safety, or legitimacy. |
| Equivalence | Agreement under a specified class of queries or experiments. Isomorphism is a strong special case with invertible structure-preserving maps. | Equivalence for one interface or objective is not identity in every respect. |

For stochastic dynamics, exact aggregation uniformly over initial states and allowed actions requires, for every such action and any two states merged by \(q\), equal pushed-forward next-state laws. Otherwise the same macrostate can have different futures depending on a distinction the macrostate erased. A restricted initial distribution can sometimes support a weaker aggregation; that is a narrower contract. For causal abstraction, one must also specify an intervention map and check that intervening then projecting agrees with projecting then making the corresponding intervention. These requirements have close established precedents in [Beckers and Halpern's causal abstraction theory](https://arxiv.org/html/1812.03789v4). Their distinctions also warn that a convenient distribution or overly flexible intervention map can hide important differences.

Recent work extends causal abstraction to transformations of mechanisms, rather than only setting variables. That makes it relevant to changes in policies and organization, but it still requires explicit models and mappings; it does not establish universal coverage. See [Geiger and colleagues, definitions 11 and 25](https://www.jmlr.org/papers/volume26/23-0058/23-0058.pdf).

### An exact safety preservation result

Consider two finite systems with the same action labels. Let \(q:Z\to\bar Z\) be surjective and suppose, for every state and action,

\[
q(F(z,a))=\bar F(q(z),a),\qquad
h=\bar h\circ q,\qquad
K_N=q^{-1}(\bar K_N).
\]

Unavailable actions must correspond too, for example through the same failure-state construction. The first equality preserves all possible successors; the second preserves exactly the available observations; the third preserves the protected criterion.

Let \(B\) contain the states compatible with an observed history. After action \(a\) and observation \(y\),

\[
\Phi(B,a,y)=\left(\bigcup_{z\in B}F(z,a)\right)\cap h^{-1}(y).
\]

Define \(W_0\) as the nonempty information sets contained in \(K_N\). An information set belongs to \(W_{n+1}\) exactly when it is safe now and some common action leads, under every possible next observation, into \(W_n\).

**Proposition.** Under the displayed conditions, \(B\in W_n\) if and only if \(q(B)\in\bar W_n\), for every finite horizon \(n\).

**Proof.** Safety agrees at horizon zero because \(K_N\) is the inverse image of \(\bar K_N\). The transition and observation equalities give \(q(\Phi(B,a,y))=\bar\Phi(q(B),a,y)\). Both recursions therefore quantify over the same actions and observation branches. Induction proves the claim. No actor is assumed to observe the hidden state or the mathematical image \(q(z)\).

This is an instance of established abstraction and safety reasoning. It identifies a genuine fragment that can be shared between different implementations. It does not claim that every proposed projection satisfies the conditions.

The displayed recursion allows an ideal controller to use the entire observation history. It establishes attainable safety, not what the installed policy carrier actually does. Memory, computation, policy-editing authority, and execution costs must be represented or an implementation certificate supplied before the result is claimed for a physical institution or device. For a restricted controller class, use the same realizable policy class on both sides and verify its correspondence.

A weaker overapproximation can certify safety in one direction if every abstract action can be implemented using the concrete actor's available information, all resulting concrete successors map into the abstract successor set, and abstract safety implies concrete safety. An abstract failure may then be spurious. A state-dependent action translation that secretly requires hidden state is not an implementable policy.

### A positive worked projection

Let a device state be \((E,c)\), where charge \(E\in\{0,1,2,3\}\) and casing label \(c\in\{0,1\}\). Charge zero is absorbing failure. At positive charge, “consume” lowers charge by one. “Charge” raises it by one, except that charging at three causes overcharge failure; charging also toggles the casing label. The controller observes only alive versus failed. Protection means \(E>0\).

The projection \(q(E,c)=E\) forgets casing. It preserves each action's charge effect, the observation, and protection, so the proposition applies. The casing remains a real changing feature; it is irrelevant to this particular question under the specified dynamics.

Enumeration checks all 16 state–action transitions and 396 safety comparisons across 66 observation-compatible information sets and horizons zero through five. They agree. This is finite verification of the example, in addition to the general proof. If casing affected charging, communication, repair cost, or a protected obligation, the same projection could fail.

### Four failed projections

**Alive alone loses controllability.** In that device, states \(E=1\) and \(E=3\) are both alive. The former needs charging; the latter needs consuming. Each can be kept alive individually, but an actor uncertain between them has no safe first action. “Currently functioning” does not determine “able to continue functioning.”

**Total resources lose access.** Accounts \((1,4)\) and \((0,5)\), ordered as accessible cash and barred treasury, both total five. A necessary immediate action costs one; transfers are prohibited and income arrives later. Only the first state can act. A total-stock projection erases an enabling relation even though it retains every unit of money.

**Present observations lose temporal dependence.** In a deterministic cycle \(a\to b\to c\to a\), observe zero at \(a,b\) and one at \(c\). A current zero following one must be followed by zero; a zero following zero must be followed by one. There is no exact first-order deterministic state model using the current observation alone. The appropriate history or a richer state repairs this particular loss.

**Equal observation laws lose causality.** Let \(U\) be a fair bit. Model A has \(X=U,Y=X\); model B has \(X=U,Y=U\). Both naturally produce \((X,Y)=(0,0)\) and \((1,1)\) with probability one half. Under \(do(X=1)\), however, \(P(Y=1)\) is one in A and one half in B. Perfect observational agreement cannot transport the intervention claim. This is an exactly enumerated constructed example, not a claim about a measured system.

There is a fifth, normative failure: states giving one unit of protection to A and none to B, or vice versa, have the same total. The predicate “A receives at least one unit” differs. No evaluation depending only on the total can recover that distinction. Whether that predicate ought to be protected is a separate normative judgment.

## What the inherited results establish

The original register contains U01–U28, S01–S06, H01–H05, P01, and N01. Their labels do not put them at the same evidential level. Some U claims are accounting identities or general information bounds; others concern particular nonlinear equations. S claims are synthetic calculations, not field findings. The full mapping and independent checks are retained in the accompanying [research record](research-record.md).

| Result group | Established content | Unproved extension |
|---|---|---|
| Selection and support, U01–U11 | Relative success can conceal loss of absolute scale; specified renewal systems have thresholds and vulnerable transitions; replacing a carrier takes time and resources. | Selection universally undermines renewal, or every successful system renews all its own supports. |
| Observation and correction, U04–U05, U26 | Some indistinguishable conditions require incompatible responses; finite safety can be computed on information sets; reliable discrimination requires enough information. | Every uncertainty requires a new measurement, or each necessary bound jointly guarantees correction. A common safe action may suffice without discrimination. |
| Frames and model revision, U12–U15, U20–U23 | Supplied frames can sustain exclusion; a sufficient old summary can fail under a larger model family; updating cannot introduce an excluded finite hypothesis. | Unrestricted discovery of new concepts, explanation of every institution's standards, or proof that history cannot recur. |
| Inquiry and inheritance, U16–U19, U24–U28 | Payments must be feasible in sequence; readiness has conditional option value; signals include silence and visible investment; capped reserves can fail despite positive mean income; recovery may require a cash bridge. | Permanent inquiry is always desirable, more archives are always better, or closing a particular provider necessarily destroys future inquiry. |
| Synthetic integrations, S01–S06 | Small models join discovery, gates, priced memory, credit, recognition, and selective rebuilding in different combinations. | One experiment has jointly made model formation, norms, authority, technology, and all enabling resources endogenous. None has. |
| Empirical hypotheses, H01–H05 | Testable proposals about capacity, authority, transmission, handoffs, and evidence production. | Cross-domain empirical confirmation; one earlier authority pilot failed its prediction. |
| P01 and N01 | A proposed capacity profile and an explicit commitment to shared agency and legitimate revision. | A complete definition of 生生 or a derivation of ethics from dynamics. |

Three short derivations show both the connection and its limits.

### Renewal constrains every relevant prefix

For a defensibly measured stock with \(\dot E=R-L\) and fixed floor \(E_{\min}\), integration gives

\[
\int_0^t(L-R)\,ds\le E(0)-E_{\min}
\]

at every time while protection holds. A persistent deficit at least \(\epsilon>0\) exhausts that margin within \((E(0)-E_{\min})/\epsilon\). It is not enough that later profits offset earlier losses. Positive changes of units preserve the inequality if stocks, flows, and floors change together. Arbitrarily combining unlike resources or removing access restrictions does not.

This is established accounting, conditional on a real dependency. Defining “support” afterward as whatever was present when activity continued would make the principle circular. Substitution, imports, dormancy, changing functional demands, and finite tasks must be represented before applying it.

### Selection can erase absolute scale

For pure selection \(\dot n_i=r_i n_i\), let \(p_i=n_i/\sum_jn_j\). For any positive differentiable \(a(t)\),

\[
\widetilde n_i=a(t)n_i,\qquad
\widetilde r_i=r_i+\frac{d\log a}{dt}
\]

preserve every share and pairwise growth advantage, while changing total abundance. Starting both types at one, rates \((1,0)\) give \(N=e^t+1\); rates \((-1,-2)\) give \(\widetilde N=e^{-t}+e^{-2t}\). The shares are identical and the totals have opposite long-run behavior.

This is a model-class identification limit. It compares compatible dynamics and does not claim that a density-dependent ecological model is unchanged by rescaling its populations. Observing absolute scale or validating additional dynamics can resolve the ambiguity.

### Historical compression is relative to future questions

The inherited example compares records 00010 and 01000. Both end at zero and contain two switches in four transitions. For an unknown constant symmetric switching rate, that count and endpoint preserve the specified prediction. Admit instead equally likely slow-then-fast and fast-then-slow models, with rates .05 and .45 and the latest rate continuing. The next-state probabilities become .4483516109 and .0516483891, respectively. At action threshold .3 they require opposite responses. These values and the equality of the count distributions were independently recomputed here.

The records did not become false. The admitted model family changed, making an erased distinction relevant even to the same next-state prediction. New future questions can create another such loss. In this example early and late counts repair the problem; complete raw retention is not uniquely necessary. Even raw records omit unmeasured context. The result establishes neither an obligation to retain everything nor a theory of how the new model family was conceived.

## A checked limit on combining constraints

A sensor reports a binary condition with sensitivity and specificity .9, independently on each use. There is no other informative observation. Require false reopening probability at most .05 and detection probability at least .9.

The inherited information inequality requires

\[
n\,\mathrm{kl}(.9,.1)\ge\mathrm{kl}(.9,.05),
\]

where \(\mathrm{kl}\) is binary relative entropy in natural-log units. The two divergences are 1.7577796619 and 2.3762054022, so this lower bound only requires \(n\ge2\).

But **two observations are insufficient even with randomized decisions**. Under the healthy and hazardous conditions, two positives have probabilities .01 and .81. Mixed outcomes have probability .18 in both. At false-positive allowance .05, the best randomized rule accepts every double positive and accepts a fraction \(2/9\) of mixed outcomes, using the remaining .04 allowance. Its maximum detection probability is .85; the deterministic maximum is .81. Accepting any double negative instead is worse because its likelihood ratio is lower. Any adaptive procedure using at most two observations can be simulated from the full two-observation transcript, so stopping early does not evade this bound.

Three observations with at least two positives as the trigger achieve false reopening .028 and detection .972. Thus an observation cap of two can pass the KL bound and every separately specified two-observation payment check while failing the actual requirement. Exact policy construction or a complete feasibility recursion is stronger than checking a list of necessary inequalities.

Two further independent numerical checks make the support issue concrete:

- Cost one, reserve cap two, and independent returns of three with probability one half each active round give positive uncapped mean net income .5, but mean time to irreversible inquiry shutdown is six rounds from a full reserve. Overflow is inaccessible and no restart is allowed. Removing either restriction changes the question.
- With recovery cash flow \(\dot b=1-3e^{-t}\), the mature margin is positive, but the minimum initial cash bridge is \(2-\log3=.9013877113\). Later profitability cannot finance an earlier forbidden deficit.

These are useful restrictions on possibilities. None chooses whose activities deserve support.

## Including the construction of the picture

A situated observer can store records, execute an imperfect inference procedure, publish a claim, change another actor's behavior, receive consequences, and revise its procedure. All those events can be represented inside a process model. There is no need for the observer to contain a complete copy of the world, or for the model to include a complete model of itself at every level. A finite carrier and its operations can be represented without recursively expanding all its interpreted contents.

The present research can be treated similarly: the inputs, source choices, formal grammar, agents, calculations, and resulting report are a partial record of its own production. That record is not a complete causal account of why this inquiry occurred or a self-certification of its conclusions. A mathematical proof uses stated premises and inference rules; the applicability of those premises to the world still needs evidence.

**Self-inclusion does not imply universal self-prediction.** Suppose a predictor must announce a definite bit \(b\) predicting an actor's next bit, and the actor sees that announcement and outputs \(1-b\). Both possible forecasts fail. The restriction applies to certain public deterministic predictions in a class admitting such responses. It says nothing against private forecasts, restricted actors, useful probabilities, or fallible self-modeling.

Self-reference is also not generally incoherent. [Fallenstein, Taylor, and Christiano](https://arxiv.org/html/1508.04145v1) construct reflective oracles that answer some self-referential probability queries using randomization at the relevant boundary. This is a formal consistency result under strong oracle assumptions, not a practical procedure giving real institutions complete self-knowledge.

Similarly, feedback can be unrolled in time when the specified chronology supports it. It is not enough to draw arrows around a loop and declare a universal DAG. The instantaneous Boolean equations \(x=y,y=x\) have two solutions; \(x=1-y,y=x\) have none. Explicit lagged updates define different, potentially well-posed processes. Time indexing does not choose an equilibrium or prove causal closure. Changing an effective mechanism through reorganization also need not change fundamental physical laws.

An omniscient external evaluator is therefore unnecessary for the proposed practice of situated, revisable inquiry. An analytical metalevel remains: we stipulate and assess models, interpretations, and proof rules. This is not a claim to have abolished that distinction or established an external infallible standpoint. Nothing established here supplies an unconditional certificate that the account covers every possible omitted distinction and validates every one of its own standards. Finite cross-checking and openness to challenge improve warranted confidence; they do not become a view from nowhere.

## Primary accounts and the limits of their connections

These sources were chosen for distinct jobs: selection, abstract regulation, inquiry, institutional revision, and generation through change. This is not a representative survey of cultures or evidence of independent convergence. The interpretations below are ours, not hidden formal theories attributed to the authors.

**Darwin.** In the first edition of *On the Origin of Species*, chapters III–IV discuss dependence and reproductive success, including relations among hosts, parasites, and dispersers; chapter VI does not equate adaptation with universal benefit. We can interpret organisms and environments as states and reproduction, death, and dispersal as transitions. That preserves a conditional question about descendants, provided inheritance and ecological relations are actually modeled. It does not turn institutional imitation into biological inheritance or make reproductive success an ethical criterion. [Primary text, especially pp. 62–63, 80–83, 200–202](https://darwin-online.org.uk/content/contentblock?basepage=1&itemID=F373&viewtype=text).

A constructed mapping failure sharpens this connection. Put A on a site producing two descendants and B on a barren site, then exchange their sites. Let the next generation consist only of those descendants. Both starting type-frequency vectors are \((.5,.5)\); the next A frequencies are one and zero. A frequency-only description cannot preserve these dynamics. Retaining the type–site association repairs this example. Shared selection vocabulary alone does not.

**Ashby.** *An Introduction to Cybernetics* develops transformations, coupled systems, simplifications, and regulation of selected essential variables. It explicitly treats the experimenter as coupled to the studied system and distinguishes observational behavior from internal connections. This is close prior art for several ambitions here. Its treatment also makes the protected variables and acceptable ranges inputs to a regulation problem. Our proposed focus is to track changes in the means of observing, selecting, and maintaining those specifications, while retaining explicit limits. That is a research proposal, not a claim that Ashby lacked feedback or adaptive regulation. [Primary text, sections 4/6, 6/2, 6/7, 6/13–6/16, 10/4–10/7, 12/1](https://ashby.info/Ashby-Introduction-to-Cybernetics.pdf).

**The Xici.** In *Yijing*, *Xici* I.5, 生生之謂易 can provisionally be glossed “generation upon generation is called change.” The surrounding text includes yin/yang, goodness, nature, virtue, qian/kun, and divination. Other passages connect figures, judgments, and conduct. A partial interpretation can preserve continuing generation and representations used within change. A replenishment equation discards much of that setting, so it is not a faithful equivalent of 生生. The Chinese text was inspected; this gloss is our provisional rendering, not a verified definitive translation. Authorship, dating, and historical priority are not adjudicated. [Primary Chinese text, stable revision](https://zh.wikisource.org/w/index.php?title=易傳/繫辭上&oldid=2611140).

A six-bit encoding can preserve the combinatorics of six-line figures and stipulated line changes. It cannot establish the truth of social or cosmological interpretations assigned to them. This separates exact symbolic encoding from causal and ethical warrant.

**Dewey.** In chapter VI of *Logic: The Theory of Inquiry*, inquiry forms a definite problem within an unsettled situation; ideas anticipate consequences and require embodied symbols; resolution involves operations on conditions. We can represent problem descriptions, tests, and changed circumstances within a causal process. A posterior over a fixed hypothesis list captures only one restricted aspect. The formal core does not explain the qualitative unity of a lived situation merely by naming a state variable for it, nor imply that every difficulty is algorithmically resolvable. [Primary chapter scan, printed pp. 101–119](https://thehangedman.com/teaching-files/pragmatism/dewey-logic2.pdf).

**Ostrom.** Her 2010 revised Nobel lecture distinguishes frameworks, theories, and models, and connects action situations, rules in use, outcomes, and evaluation. Participants' opportunities to revise rules are part of the institutional question. This supports modeling authority and revision as actual mechanisms rather than treating an institution as a single policy. It does not supply a universal optimal rule or remove the need to measure enforcement and practical access. [Primary article, especially pp. 646–648, 651–653, 663–664](https://web.pdx.edu/~nwallace/EHP/OstromPolyGov.pdf).

These accounts place different demands on an integration. Descendant number, warranted resolution of a problem, reliable resource provision, and a cosmological evaluation are not interchangeable success criteria. A model can examine their relations, but cannot erase the difference by calling them all “fitness.” Nor are neutral dynamics automatically faithful to a text whose claims include substantive evaluative or divinatory commitments. Those commitments need argument, qualification, or rejection.

## What could break the proposed synthesis

The present core can encode many things while explaining few of them. Its main risks are therefore identifiable.

| Challenge | Why it matters | What would count as progress or failure |
|---|---|---|
| Unrestricted novelty | A supplied schema grammar already anticipates the kinds of revision the model can express. | Demonstrate generalization to independently proposed new distinctions; record when new primitives must be added. Endless ad hoc additions weaken a completeness claim. |
| Experience and meaning | A carrier state does not by itself explain experience, reference, or correct interpretation. | Give an adequate semantic or experiential account for a limited target. Merely labeling a variable “meaning” fails. |
| Distributed conflict | A single-controller safety recursion does not establish what strategic actors with different observations and purposes can coordinate on. | Specify communication, incentives, bargaining, and authority; test against noncooperative alternatives. A centralized optimum is not an implementation proof. |
| Unmodeled mechanisms | Hidden causes or changing boundary conditions can invalidate a transition model. | Predict interventions under frozen assumptions. A verified discrepancy rejects the mapping or dynamics; it must not simply be renamed “more transformation.” |
| Purely retrospective explanation | A flexible language can describe every outcome after the fact. | Freeze measured variables, mapping, and predictions before seeing outcomes. State what the model excludes. |
| Static resource explanation | Apparent benefits of recognition or inquiry may come only from spending more. | Match actual expected spending where relevant, preserve information channels, and remove the feedback mechanism separately. Equal starting budgets are insufficient. |
| Normative loss through aggregation | Equal output or persistence can coexist with unequal protection and suppressed appeal. | Retain stakeholder-specific predicates and participation relations when those matter to the question. Numerical equivalence alone fails. |
| Technical scope | Finite classical state/action models do not establish an account of all continuous, quantum, or noncomputable phenomena. | Supply appropriate semantics and separate representation theorems if those domains become targets. Calling them states supplies no such theorem. |

The strongest rival interpretation is that this is an organized application of control theory, statistical decision theory, causal modeling, and institutional analysis. That interpretation currently fits the evidence. A stronger unification earns its place only by deriving a useful constraint, transfer, or failed-case prediction that separate models would otherwise miss, with fewer independent assumptions or demonstrably better transport. Agreement among research agents is no substitute for that result.

There is also a direct challenge to “more possibilities is better.” Duplicating action labels increases their count without adding an attainable outcome. Adding coercive options can increase reachable states while damaging other people's agency. A meaningful capacity measure must quotient irrelevant duplicates and specify whose possibilities, at what costs, under which protections.

## What causal structure can contribute to alignment and coordination

Causal analysis can identify whose actions affect whose conditions, which signals become evidence, who can challenge an interpretation, what a repair costs, and whether future revision remains feasible. It can expose a system that appears successful while consuming the means to evaluate or correct its behavior. It can also show when maintaining inquiry produces cost without benefit and when a dormant capability can be rebuilt in time.

Those contributions matter for alignment, but they do not solve it. A perfectly renewable institution can be coercive. An AI system can preserve its evaluators while manipulating the evidence they see. An increased range of feasible actions can empower one actor at others' expense. Physical realization of an evaluator explains how its judgments arise; it does not establish their authority or truth.

Formally, the same transition model can be paired with two different evaluative orderings that prefer different attainable outcomes. Without a further normative premise, neither ordering follows from the transition equations. This is a statement about what these equations entail, not a purported resolution of every metaethical debate.

For this program, the commitment to shared agency, legitimate revision, and future generations remains explicit. Its practical specification should identify affected parties, contestability, protections during transitions, and acceptable burdens. Some conflicts may remain incomparable rather than reduce to a scalar. Modeling the evolution of those commitments is valuable; endorsing every evolved commitment would be a separate and unjustified step.

## The next discriminating test

The next test should target a precise abstraction claim, rather than add another domain to a vocabulary list. Begin with a finite maintained-reservoir process with productive stock, diagnostic readiness, and two accounts with distinct access rights. First isolate whether aggregating cash erases attainable correction. Then add record formats and separate proposal, admission, and enactment roles as independently checked extensions. Compare the aggregate output-and-total-cash description with the richer description of attainable correction.

Freeze both descriptions and their intervention maps before evaluation. Construct cases with equal current output and total resources but different access, retained evidence, or revision authority. Compute attainable vectors of failure probability, cost, intervention burden, and timely recovery. A merged pair with different vectors is an exact counterexample to the coarse abstraction. Add only the implicated distinction and test whether the repaired map preserves the entire declared intervention family.

The more demanding stage changes how observed outcomes earn recognition and replenish diagnostic access. Compare feedback-based support with an externally replayed schedule at matched expected expenditure and comparable observation access. Include cases with no useful new question, an uninformative diagnostic, free immediate rebuilding, and nonbinding authority. These controls distinguish an endogenous correction mechanism from extra money, a static gate, or a planted effect.

This single simulator first tests an abstraction. A second stage must test transfer to an independently implemented process with different dynamics. One sharply restricted prediction is \(R_{fa}=p_fq_a\): finance condition \(f\) enables a timely valid recommendation with probability \(p_f\), and enactment condition \(a\) then delivers effective timely repair with conditional probability \(q_a\). If recovery requires both gates, there is no alternative route, and each intervention leaves the other gate unchanged, the interaction is \(R_{11}-R_{01}-R_{10}+R_{00}=(p_1-p_0)(q_1-q_0)\). This is elementary probability. The testable claim is that independently measured gate quantities predict target recovery outcomes without refitting the mechanism. Direct repair, anticipation, or changed recommendation quality can defeat that application.

The [next-test protocol](next-test.md) specifies stages, horizons, outcome criteria, controls, and rejection conditions; a complete transition table and uncertainty procedure still need to be frozen before execution. It has not yet been run. The finite projection checks and diagnostic counterexample in this report have been run. Success in two simulators would support a scoped transfer claim, not empirical institutional adequacy; a subsequent independently measured application would still be required.

The conjecture worth carrying forward is therefore demanding but bounded: **within the registered target class, a fixed account of how correction is supported and enacted will predict target recovery probabilities and intervention effects from independently measured local mechanisms, without adding a mechanism after viewing the target outcomes.** A failed prediction rejects that registered application. Preservation theorems explain why successful translations can work; they do not establish that real translations satisfy their premises. Universal completeness, unrestricted novelty, and ethical adequacy remain open questions.
