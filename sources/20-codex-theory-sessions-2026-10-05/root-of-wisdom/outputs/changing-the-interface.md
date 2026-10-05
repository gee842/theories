# How an organization can change its own interface

Research continuation for Ren, 5 October 2026. All earlier work is preserved. This advances the [differentiation investigation](differentiation-and-viewpoints.md) by putting sensing, selective exchange, conversion, and the cost of changing them into one executable process.

**The result is an integrated example of continuing operation through a change in organization.** A system changes which property it can sense, which resource its boundary admits, and which conversion it can perform. The change uses its own reserve and takes time. Under a stated environmental contract, it can repeat these changes indefinitely while every permanently fitted interface fails some permitted environment. Removing any one of the three kinds of change removes that guarantee.

This is a conditional construction within our inquiry, not a claim of a new law of nature. It supplies a repertoire of two interfaces and a rebuilding mechanism. It does not derive organisms from monism, invent an unforeseen third capability, or explain experience or moral judgment.

## One process with a changeable relation to its surroundings

The environment offers resource A, resource B, or both. Each resource has a current binary processing property, \(h_A\) or \(h_B\), which can change independently at every time step. To convert a resource, the system must apply the setting matching its current property.

The system has room for one receptor, one selective transporter, and one converter. Each can be fitted for A or B. A coherent interface fits all three to one type \(q\). The resource roles are distinct:

| Component | What it supplies | What remains impossible without it |
|---|---|---|
| Receptor | Detects whether its resource is present and, if present, reads its current processing property. | The other resource's independently varying property cannot be inferred from this receptor's record. |
| Transporter | Admits its fitted resource across the exchange boundary. | Information alone cannot admit the other resource. |
| Converter | Converts its fitted admitted resource when the setting is correct. | Admitting a resource alone does not make it usable. |

Boundary change here means changing selective exchange. Spatial shape, membrane chemistry, and the initial construction of the system are not modeled. The one-slot limits are explicit physical-budget premises. A device permanently containing both complete interfaces is outside this comparison class.

The system carries a reserve \(r\), capped at \(C\). Every operating or rebuilding step costs one unit. Correct conversion yields two units; absent input or an incorrect setting yields none. The update is

\[
\boxed{r_{t+1}=\min(C,r_t-1+I_t),\qquad I_t\in\{0,2\}.}
\tag{1}
\]

Maintenance and incoming production are accounted together, then storage is capped. This is not the different rule that caps intake before paying maintenance. Excess production is discarded. The reserve is an abstract usable resource with stipulated conversion and cost rates, not a universal unit of physical value.

At zero reserve, the system can no longer sense, convert, or rebuild. Zero is absorbing. Continued operation means \(r\ge1\) after every step. This requirement has a causal role in the transition rules, rather than being a reward attached to otherwise unchanged behavior.

Rebuilding to the other coherent interface takes two steps with no intake and costs one unit on each. The old receptor can detect absence at the initiating decision. The next step completes rebuilding without a new reading; the new receptor becomes usable on the following step. The rebuilding rule and templates are supplied mechanisms. Their physical origin is not derived.

The controller is simple: if the installed resource is present, read its property and convert with the matching setting; if absent, rebuild to the other interface. During a rebuild, complete it. There is no forecast, global resource sensor, or access to the other resource's hidden property.

## A transition that pays its own costs

Take capacity \(C=3\), initial reserve 3, and either coherent interface fully fitted and ready, with no rebuild underway. Start at the beginning of an availability phase, and assume each phase lasts at least four steps. Processing properties may change arbitrarily at every step; only resource availability has this dwell constraint.

If the current interface still has input, correct conversion holds the full reserve at 3. If its input disappears, the other resource must be present under the declared environment model. The transition is:

| Step in the new phase | Activity | Intake | Reserve afterward |
|---|---|---:|---:|
| Start | Old interface, full reserve | — | 3 |
| 1 | Begin rebuilding | 0 | 2 |
| 2 | Finish rebuilding | 0 | 1 |
| 3 | Read and convert through the new interface | 2 | 2 |
| 4 | Read and convert again | 2 | 3 |

The organization remains operational throughout, and two productive steps replenish what rebuilding spent. It therefore delivers the same full starting reserve needed for another change.

**Sufficiency theorem.** Under these conditions, the controller remains operational indefinitely for every permitted availability sequence and every sequence of processing properties.

**Proof.** During any four-step constant-availability block starting with reserve 3, the controller either already has a usable interface and stays full, or completes the displayed transition. In either case it ends with reserve 3 and a present resource fitted. Further steps in that phase keep it full. Induct on availability phases. Correct settings follow from the actual receptor reading, so arbitrary processing-property changes do not break the argument. ∎

The initial phase condition matters. Starting with the wrong interface near the end of an already running phase can direct a rebuild toward an input that disappears before rebuilding finishes. The evidence record includes that counterexample. Starting with a ready, matched interface and full reserve at any phase position is another sufficient entry condition: the first mismatch then occurs at a subsequent phase boundary.

This establishes recurring transformation, not one rescue financed by an unreplenished initial endowment. It remains adaptation within a supplied finite repertoire.

## The timing limit is sharp at this capacity

Four-step phases are not merely convenient for the displayed controller. **At capacity 3, alternating A-only and B-only phases of three steps defeat every controller, even one with complete foreknowledge.**

To see this, consider the first \(n\) such phases. Each phase needs at least one successful conversion: three consecutive steps without intake exhaust the maximum reserve. Choose one successful conversion per phase. Their alternating resource types require at least \(n-1\) completed interface changes between them. Each change occupies two steps without intake. The number \(H\) of successful conversions therefore satisfies

\[
H\le3n-2(n-1)=n+2.
\]

Ignoring discarded excess production can only overestimate the remaining reserve, so

\[
r_{3n}\le3+2H-3n\le7-n.
\]

At \(n=7\), the reserve cannot remain positive. This contradicts uninterrupted continuation. The argument grants perfect knowledge of every processing property and all future resource changes; insufficient time still defeats the system. An independent exhaustive enumeration of every permitted action history tightens failure for this particular schedule to step 14. The analytic bound of 21 steps is conservative.

Consequently, with capacity 3 and the supplied actions and initialization, a minimum phase length of four is both necessary and sufficient for a guarantee over the whole environmental class. The result does not establish the same threshold for larger stores, faster rebuilding, or additional capabilities.

## Why the resources and all three changes are necessary

**A reserve below three cannot fund this transition without interruption.** Two rebuilding steps remove two units with no intake, while one unit must remain. Capacity \(C\le2\) therefore prevents every uninterrupted rebuild, even with perfect foresight. An indefinitely sustained opposite-resource phase defeats any permanently fitted type, so no controller with that capacity and these actions can guarantee continuation across the permitted environments.

Matched operation can nevertheless continue from reserve 1 or 2 and build up its reserve if the environment allows time. The difference is between current functioning and immediately executable transformation. The rule does not claim that a temporarily low reserve can never recover.

**A permanently fitted interface cannot handle the whole environmental class.** Fixing transport or conversion to A prevents intake in a sufficiently long B-only phase, and conversely. This remains true even if software is arbitrarily sophisticated and the processing properties are perfectly known. Maintenance exhausts the finite reserve.

**Transport and conversion changes alone do not suffice.** Suppose they change to B but the receptor remains fixed to A. In a B-only phase the receptor gives the same absence record whether \(h_B=0\) or \(h_B=1\). Those possibilities require incompatible conversion settings. Past guesses cannot reveal a fresh independently varying property. No policy using that information can guarantee successful conversion across all allowed property sequences. A sequence of unsuccessful attempts exhausts the reserve.

Thus observation, access, and conversion play independently necessary roles in this construction. Their joint change is more than relabeling a resource. Sensor-only change cannot supply transport and conversion; conversion-only change cannot supply access or the relevant observation.

The comparator must remain precise. The transforming controller has a fixed overall program whose state includes its installed interface. The result does not show that changing hardware defeats every fixed algorithm or changes the laws of nature. It shows why a permanently fitted, resource-matched interface is insufficient in this environment class.

## What becomes consequential changes with the organization

When both resources are present, an A interface can operate correctly using \(h_A\) while ignoring \(h_B\). A B interface reverses that relationship. The two observations are not just different names for the same information: the properties vary independently.

The same world therefore supports different consequence-relevant distinctions for different organizations. Changing the organization changes both the property needed for successful action and the physical channel through which that property is available. This gives concrete content to the proposed relation between individuation and significance.

It also reveals a limit of correcting beliefs alone. A system may correctly infer that it needs B while lacking the transporter, converter, sensor, or reserve needed to use it. Conversely, installing a converter without access to the necessary property leaves an information problem. Repair can require changing the interaction through which knowledge and action become possible.

This is functional significance relative to the specified continuing organization. The model does not derive a moral obligation to preserve it, show that it experiences concern, or explain how a new purpose forms. The physical stakes and the ethical evaluation of those stakes remain different questions.

## From an acceptable next action to a viable course of action

The earlier single-decision criterion asked whether situations sharing a record have any acceptable action in common. That remains exact for its stated question. It is insufficient for an extended process: a safe next step can leave no viable next step afterward.

We can now give a complete finite-model criterion. Include world state, installed hardware, resources, memory, and transition stage in a finite state space \(X\). Let \(\mathcal K\subseteq X\) contain the acceptable continuing states. Observations come from the actual installed interface. A belief \(B\) is the nonempty set of states compatible with the available observation-action history; it is a possibility set, not an assumption that the system explicitly reasons in this notation.

Let \(\mathcal B_{\mathcal K}\) be the nonempty beliefs contained in \(\mathcal K\) that share a current observation. For action \(a\), let \(P(B,a)\) contain every permitted successor from every state in \(B\). After observation \(o\), let \(U(B,a,o)\) be the successors compatible with that observation. Define

\[
\boxed{
\Phi(W)=\left\{B\in\mathcal B_{\mathcal K}:\exists a,
\ P(B,a)\subseteq\mathcal K,
\quad U(B,a,o)\ne\varnothing\Rightarrow U(B,a,o)\in W
\ \text{for every }o\right\}.}
\tag{2}
\]

Start with all nonempty safe beliefs that share a current observation. Repeatedly apply \(\Phi\), deleting beliefs from which no common action can keep every possible successor within the remaining set. Because the model is finite, this process stops.

**The fixed point contains exactly the initial beliefs from which some history-based controller can guarantee indefinite safety against every allowed disturbance.** At a surviving belief, choose its witnessing action and repeat. A deleted belief loses its guarantee at a finite horizon. The full proof is preserved in the evidence record, with an independent exhaustive check on small systems.

Unavailable actions must lead to failure in this construction; they cannot silently remove inconvenient possible worlds. Rebuilding costs, delays, sensor changes, and intermediate failures must be included in the transitions. The criterion concerns indefinite safety under a supplied model, not guaranteed discovery of unknown world states or eventual completion of every worthwhile task.

Two counterexamples sharpen its meaning. A safe probe can reveal which of two otherwise indistinguishable situations requires action 0 or 1, making success possible. The same informative probe fails as a repair if performing it destroys the organization in one possible situation. A distinction can be describable and even measurable in principle while remaining inaccessible through a viable inquiry.

## Connections to the other work

The other session's [generative-health result](/Users/ren/theories/_process/research/2026-10-05-generative-health/ANSWER.md) already proves that an incumbent can operate forever while leaving no resource margin to establish a specified successor. Its [discovery continuation](/Users/ren/theories/_process/research/2026-10-05-generative-health/discovery/ANSWER.md) charges generation, validation, and installation to the same budget as their supporting capacities. Those results are inherited here, not rediscovered claims. Our added mechanism changes the actual observation and conversion interface, with independent necessity checks and repeated paid transitions.

The [identity-through-change investigation](identity-through-change.md) supplies another restriction. The reserve stays positive along this model's actual rebuilding history; zero is absorbing. A later replacement with the same state is not being counted as uninterrupted continuation. Nor does the model's adequacy for future control answer every historical question. A sufficient action record is not automatically a complete representation of truth.

There is established conceptual precedent. Di Paolo distinguishes continued self-production from regulation of trends toward losing viability, and considers changes to the regulatory processes themselves. The present finite mechanism gives a small explicit realization of selected functional questions; it is not offered as a new origin of that research program or as a complete instance of biological autopoiesis. [Di Paolo, 2005](https://ezequieldipaolo.net/wp-content/uploads/2011/10/autopoiesis_teleology_2005.pdf).

The source record distinguishes completed other-session results from a saved discovery module whose chat was still active when inspected. Those other-session checks were not rerun here.

## The advance in the theory

The earlier branch explained maintained differentiation and distinct functional viewpoints. This branch shows that **continuation can require changing the organization that supplies the viewpoint and its actions**. The transition itself is part of what must be feasible.

The useful explanatory object is therefore a situated course of possible activity: what the organization can distinguish now, what it can do, and which changes it can reach while preserving the stated conditions of continuation. A static picture of its present capacities can conceal a blocked transition or a future dead end.

This sharpens the wisdom inquiry without identifying wisdom with survival. Better understanding may require another observation, another available response, or reconstruction of the interface through which observations and responses occur. Evaluating whether that reconstruction should preserve the current organization, protect other participants, or support a different successor requires additional factual and ethical reasons. Changing the success criterion after failure must be acknowledged as changing the question.

No deeper metaphysical root is declared from this example alone. The supported advance is a paid mechanism of changing access and capability, a separation from permanently fitted configurations, and a multi-step criterion for continued action under partial information. These results make the proposed relation among unity, differentiated organization, and changing viewpoints more specific and testable.

## Verification and preservation

The [evidence record](changing-the-interface-evidence.json) contains the model, proofs, check programs, source scopes, comparative traces, and preservation hashes. All 28 pre-existing output files remain unchanged.

Exact checks cover the local transition and A/B symmetry rules, all processing-property histories over the four-step repair block, module restrictions, and complete finite-state reachability under the phase contract. A separate finite audit compares the general safety recursion with exhaustive policy enumeration and checks the three-step timing obstruction over every permitted action history. These are constructed mathematical and executable results, not a new biological or human-subject experiment.
