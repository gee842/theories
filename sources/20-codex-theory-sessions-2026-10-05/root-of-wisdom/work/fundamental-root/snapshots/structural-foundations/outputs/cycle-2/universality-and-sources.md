# Universality, changes of scale, and what must be preserved

Research memo, 5 October 2026. This memo develops the universality question raised while the second research cycle studies modular replacement and recurrent paid repair. It does not replace the first cycle's source audit.

Ren's motivating conjecture is preserved here: “I think it make sense this is universal, it appears across scale, across space time. This should be it.” This is a research hypothesis and direction, not evidence that the mathematical premises hold in every domain.

## The strongest supportable formulation

There is a defensible universal form: **when continued activity requires accessible prerequisites, a successful continuation must preserve or obtain those prerequisites along an executable sequence, and its choices cannot use distinctions unavailable to the choosing process.** Quantitative consequences follow when resources, timing, uncertainty, and access are specified.

This formulation supports research across scales. It does not imply the same behavior, threshold, or ethical assessment at every scale. A universal constraint can predict that scaling changes the outcome because demand, access, or delay scale differently. The new task is to identify what must be preserved for a result to transfer—and then test whether a proposed physical or institutional mapping preserves it.

Four senses of universality need separate claims:

| Claim | What would establish it | Current status |
|---|---|---|
| A logical or mathematical implication holds for every member of a specified class | Proof with explicit premises and quantifiers | Several accounting, information, and scheduling constraints qualify |
| A guarantee is unchanged by a relabeling or change of units | An invertible, property-preserving map of states, actions, information, and tests | Provable under the stated map |
| One description faithfully replaces another at a different resolution | A sound abstraction/refinement or intervention-preserving correspondence | Must be established for each abstraction; false in general |
| The same measured mechanism explains outcomes across empirical domains and scales | Independent operationalization, held-out intervention predictions, and evidence | Open research hypothesis |

The first two are already universal in a precise conditional sense. The latter two cannot be concluded from recurring verbal resemblance. This distinction sharpens the ambition: it asks for portable constraints with independently testable premises, rather than an exceptionless narrative.

## U1. A dimensionless obstruction survives unit and time changes

Consider a maintained function with accessible reserve margin `B>0` above its declared failure floor. Suppose, while the fault remains uncorrected:

- the reserve has net depletion rate at least `d>0`, after including all accessible inflows;
- every successful admissible correction requires at least elapsed time `L>0`;
- the function cannot switch to an unmodeled substitute before depletion;
- no other admissible route avoids that depletion or completes earlier.

Then a necessary condition for guaranteed correction before the reserve falls below its floor is

\[
dL\le B.
\]

**Proof.** Until a correction can finish, the reserve margin is at most `B-dt`. If `dL>B`, it crosses zero at `B/d<L`, before any successful correction is available. Equality depends on permitting completion exactly at the floor; use a strict inequality if the declared safety test forbids touching it. This is a necessary lower-bound certificate, not a sufficiency theorem. A feasible intervention still requires correct information, permission, and execution access.

Now change resource units by a positive factor `a` and time units by a positive factor `alpha`, without changing the physical process. The transformed quantities are

\[
B'=aB,\qquad L'=\alpha L,\qquad d'=\frac a\alpha d.
\]

The dimensionless obstruction

\[
\chi=\frac{dL}{B}
\]

is invariant: `chi'=chi`. The impossibility boundary `chi>1` therefore does not depend on measuring money in one currency unit or another, material in grams or kilograms, or time in minutes or hours. For `B=0`, use the inequality itself instead of dividing by zero.

For example, `B=6`, `d=2`, and `L=4` give `chi=4/3`; changing to thousandths of a resource unit and sixtieths of the original time unit gives `B'=6000`, `L'=240`, `d'=100/3`, and the same ratio. This calculation does not make trust, authority, or interpretation into conserved resources. It applies only where the required stock and net flow have been independently defined.

**What is substantive here?** The arithmetic is established. The empirical content is the claim that every usable correction needs at least `L`, that net depletion cannot be smaller than `d` before it completes, and that only `B` is accessible. Those premises can fail, for example, when a substitute is found or a shared diagnostic becomes available sooner. They must not be adjusted after every result merely to protect the theory.

## U2. Typed prefix accounting is invariant under compatible recoding

Let `b_k` be the vector of accessible resource margins after each relevant payment or receipt, with

\[
b_k=b_0+\sum_{t<k}v_t.
\]

Here each component has declared units and `v_t` includes all net changes at that microstep. Let `D` be a diagonal matrix with strictly positive entries. If `b'_0=Db_0` and `v'_t=Dv_t`, then

\[
b'_k=Db_k,\qquad b'_k\ge0\iff b_k\ge0.
\]

This follows by linearity and preservation of coordinatewise signs. A permutation of resource coordinates also preserves the test when costs, conversion rules, and enabling conditions are permuted consistently. Consequently, the exact minimum reserve frontier transforms by the same map, provided the action, observation, disturbance, and controller classes are unchanged by the recoding.

Changing time units preserves this result only when payment order, durations, deadlines, and disturbance constraints are transformed together. If “one diagnostic per minute” becomes “one per hour” while the rest of the process is held fixed, that is a changed system, not a coordinate transformation.

More generally, a strictly increasing time reparameterization preserves the order of events. It need not preserve a constant-duration or constant-rate assumption in its original numerical form. Guarantees can transfer after the entire timing test is transformed; preserving event order alone is insufficient for an unchanged numerical deadline.

## Why coarse-graining can fail

### C1. Temporal aggregation can erase the payment that blocks continuation

Start with reserve one and no borrowing. Compare two proposed two-step schedules:

- receive two, then pay two;
- pay two, then receive two.

Both have net change zero. The first is executable; the first operation of the second is unaffordable. A coarse transition recording only the interval's net resource change invents feasibility for the second schedule. No conservation law fails: the summary has discarded the prefix constraint.

Likewise, a repair that finishes at time one and a repair that finishes at time three can have the same initial and final physical state. With deadline two, only the first is timely. Untimed endpoint equivalence cannot preserve that capacity test. Clock-based transition models are an established way to represent such distinctions; their relevance is documented in source C2-L03 below.

### C2. Adding resource types loses accessibility and substitutability

Let two distinct resource types have initial amounts `(1,1)`. A required operation consumes `(2,0)`; no conversion or transfer exists. Total resources equal total cost, but the operation is impossible. Replacing the vector by its sum erases the missing first resource. A similar error occurs when summing reserves held by two institutions without a timely, permitted transfer route.

This remains an error even if both resources have the same accounting unit. Common units permit addition; they do not establish that every holder can spend the sum.

### C3. A replacement can preserve endpoints while destroying interaction

The first cycle established the relevant primary-source warning: component endpoint reachability can fail to capture repeated crossings of an interface. The same concern applies when a coarse institutional record keeps the final authorization but omits whether it was available before execution, or when a supplier replacement preserves gross output but removes a diagnostic interface. The current modular-replacement experiment is the appropriate concrete test. This memo does not repeat the earlier source survey.

### C4. Spatial scaling can change topology

The root agent's [checked scale countermodel](scale-and-deadline.md) considers `n` simultaneous hidden faults, one slot each for diagnosis, authorization, and execution, and `k` shared diagnostic slots per round. With downstream work parallel and strict stage precedence, the optimum completion time is

\[
T^*(n,k)=\lceil n/k\rceil+2.
\]

The root agent owns the model's proof and enumeration. This audit independently inspected both: the enumeration allocates stages using the pre-slot state, prevents same-slot chaining, and preserves the prepaid cash invariant; the lower bound and pipeline witness agree. Its role here is conceptual: dedicated diagnosis (`k=n`) and a shared diagnostic bottleneck (`k=1`) differ in topology even when every isolated module is repairable and per-module reserves and current output match. The same counting and precedence constraints explain the difference. A universal constraint therefore need not mean size-independent performance.

The diagnosis requirement must be justified by the guaranteed-repair objective. If guessing, unconditional universal repair, or an alternate sensor is allowed, it can invalidate the scheduling lower bound. A source of physical capacity is not automatically available to a policy under hidden faults.

## U3. What transfers under a behavioral correspondence

For exact invariance, an implementation change must transport more than state labels. It must transport:

1. admitted initial conditions, actions, and possible outcomes;
2. which choices belong to the controller and which to the environment;
3. the distinctions and memory available when each choice is made;
4. the costs, payment order, durations, permissions, and interfaces relevant to the test;
5. the safety region, target, and deadline;
6. the policy class, including permitted randomization and finite-memory limits.

If there is an invertible correspondence preserving those items, a winning policy can be translated in both directions, and the corresponding capacity judgments agree. The proof transports a policy through the correspondence and inductively matches its possible histories; the safety and target tests then coincide. For probabilities, the correspondence must also transport the outcome kernels. This is an elementary invariance argument, not a new theorem of universal dynamics.

A noninvertible abstraction requires a directional result. For a sound guarantee, every admitted concrete outcome of the refined controller must be covered by the abstract analysis, and abstract actions must be implementable using concrete information. If an abstraction merely combines all transitions that are possible in *some* concrete state, it can supply an action sequence no single observation-feasible implementation can execute. Reverse transfer needs additional conditions and must not be assumed.

The resource and timing conditions remain universal for their model class even when an abstraction is unsound. What fails then is the proposed bridge between descriptions.

## Empirical transfer criteria that could be wrong

An empirical claim worth testing is: **measured prerequisite structure and accessibility predict recovery under specified interventions beyond what current output and aggregate reserves predict.** This is deliberately narrower than “all scales obey the same social law.”

Before testing two domains or scales, register the following:

- **Boundary and units.** Define the protected function, floor, resource margins, inflow routes, outside support, and substitute technologies. State which relations are Boolean or procedural rather than additive stocks.
- **Operational information.** Measure what can be observed and retained before decisions, including public action traces. A convenient analyst dataset is not automatically information available to the actor.
- **Control and authority.** Specify who may choose each action, what unauthorized action remains physically possible, and whether an intervention supplies new standing or only new information.
- **A mapping of interventions.** Match such operations as delaying replenishment, revealing a fault, changing diagnosis concurrency, supplying execution access, or replacing an interface. Similar untreated outcomes alone do not establish equivalent mechanisms.
- **A frozen prediction.** Predict a threshold, direction, or feasible/infeasible classification on held-out interventions. Specify tolerances and measurement uncertainty before seeing the result.
- **Defeat conditions.** A previously omitted available substitute, repeated prediction failure after measured resource matching, or identical recovery when the alleged bottleneck is removed counts against the proposed mapping or mechanism. Do not preserve it by unrestricted relabeling.

Useful controls include a fully revealed fault, a fixed fault that needs only one remembered diagnosis, harmless disturbance, a substitute provider, and a disturbance outside the promised class. If fresh decision-relevant uncertainty is absent, repeated diagnostic maintenance may have no informational function. That is a substantive null result, not a failure of the observation constraint.

A finite set of successful observations cannot verify a guarantee against every allowed disturbance. Conversely, a single correctly measured counterexample can reject a concrete claimed guarantee. Statistical predictive performance and exact game-theoretic guarantees require different evidence.

## Four new primary-source anchors

### C2-L01 — Energy games distinguish prefix sufficiency from average return

Krishnendu Chatterjee, Laurent Doyen, Thomas A. Henzinger, and Jean-François Raskin (2010), “Generalized Mean-payoff and Energy Games.” [Full primary text](https://arxiv.org/html/1007.1669); [published proceedings](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.FSTTCS.2010.505).

Energy objectives require all coordinatewise running sums plus initial credit to remain nonnegative. Mean-payoff objectives constrain long-run averages. The paper gives exact strategy results for its finite, turn-based, fully observed weighted games.

**Important audit limit:** its §3 Remark 1 shows that restricting the adversary to memoryless strategies can give a wrong answer for a *fixed* initial credit even though memoryless spoiling suffices for the unknown-credit question. Minimum-reserve calculations must therefore retain the declared adversarial policy class. The paper's finite-memory existence result does not price memory maintenance or prove the same result for partially observed systems.

**Access:** full HTML inspected at definitions, Lemmas 2–3, and Remark 1. The computational results are prior art, not claimed as this session's contribution.

### C2-L02 — Consumption games expose what a replenishment transition assumes

Tomáš Brázdil, Krishnendu Chatterjee, Antonín Kučera, and Petr Novotný (2012), “Efficient Controller Synthesis for Consumption Games with Multiple Resource Types.” [Author-hosted full paper](https://www.fi.muni.cz/usr/kucera/papers/cav2012.pdf); [preprint](https://arxiv.org/abs/1202.0796).

A finite control graph has multiple resource loads and transitions that consume or reload them. Reloads marked by `omega` allow a resource to be increased to an arbitrarily high level; the analysis distinguishes safety and bounded-cover requirements.

**Transfer and limit:** renewable opportunities are already central in synthesis of resource-dependent controllers. But a reload primitive is not itself an endogenous production mechanism. Our study must charge its productive inputs, delay, and access, or declare them as boundary assumptions. Such additions can change the model class and invalidate direct import of algorithmic complexity or strategy results.

**Access:** full author PDF inspected at abstract, introduction, and model definitions. This memo uses it to identify assumptions, not as a theorem about paid institutional regeneration.

### C2-L03 — Timed automata make real-time tests part of the semantics

Rajeev Alur and David L. Dill (1994), “A Theory of Timed Automata,” *Theoretical Computer Science* 126(2), 183–235. [Publisher record](https://doi.org/10.1016/0304-3975(94)90010-8); [author-hosted PDF](https://www.cis.upenn.edu/~alur/TCS94.pdf).

The framework augments transition graphs with real-valued clocks and timing constraints, representing the times associated with events. This is a direct precedent for treating correction deadlines and delays as part of behavior, not annotations dispensable under abstraction.

**Transfer and limit:** the elementary deadline counterexample above needs no deep result from this paper. Particular region-quotient, language-inclusion, or refinement theorems must be cited with their own assumptions; no arbitrary temporal averaging is justified by the existence of a finite abstraction in a restricted formalism.

**Access:** primary publisher abstract and indexed excerpts from the author PDF were retrieved. Direct PDF opens failed twice, so this memo does not claim inspection of the full proof or import a theorem-level result.

### C2-L04 — Cross-scale causal consistency requires mapped interventions

Paul K. Rubenstein, Sebastian Weichwald, Stephan Bongers, Joris M. Mooij, Dominik Janzing, Moritz Grosse-Wentrup, and Bernhard Schölkopf (2017), “Causal Consistency of Structural Equation Models.” [Full primary text](https://arxiv.org/html/1707.00819); [version record](https://arxiv.org/abs/1707.00819).

Definition 3 requires a state mapping and a surjective, order-preserving mapping of admitted interventions, with matching pushed-forward interventional distributions. Theorem 6 formalizes consistency under that transformation. The paper emphasizes that exactness depends on the chosen intervention set.

**Transfer and limit:** this supplies a precise precedent for asking whether an intervention commutes with changing descriptive scale. It is a framework for structural equation models, not directly a proof of strategy transfer in our timed partially observed games. Equality of its declared distributions also does not, by itself, establish physical affordability, information access, or legitimate authority for an intervention.

**Access:** full HTML inspected at Definition 3, Theorem 6, §4.5, and the intervention-set qualification preceding the examples.

## Research decision

Pursue **universal conditional constraints plus tested transfer maps**. Treat recurrence across scale, space, and time as motivation to search for those maps. In this cycle, exact modular replacement and shared-diagnostic scaling can establish where the map succeeds or fails. Recurrent paid repair can then test whether preservation of correction prerequisites changes the reserve frontier under declared uncertainty.

This retains the force of Ren's conjecture: the same structural obstruction can occur in many implementations. It also makes the conjecture stronger to investigate, because success requires the accounting, information, timing, and access correspondences to predict interventions rather than merely redescribe outcomes.
