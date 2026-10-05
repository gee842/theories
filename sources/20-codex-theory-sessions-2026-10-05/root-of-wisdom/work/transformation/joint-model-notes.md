# A resource-limited organization that changes its interface

Constructed mathematical model, 5 October 2026. This is a conditional existence proof, not a fitted biological or physical experiment. No earlier output was modified.

## The explanatory target

The earlier models supplied a fixed sensor, actuator, and vulnerability. This construction joins three changes in one continuing process: which distinctions a receptor makes available, which conversion action can acquire support, and which substances the material interface admits. A fixed physical configuration cannot continue through the specified resource history. A fixed, locally informed program that actually rebuilds that configuration can.

The comparison is physical. Reconfiguration is itself describable by a larger fixed state-transition law. The result does not establish a computational capacity beyond fixed algorithms or eliminate the need to supply a repertoire of possible configurations.

## Supplied structure and fair resource constraints

There are two substrate families, A and B. At each tick the available families are one of `{A}`, `{B}`, or `{A,B}`. These availability sets occur in phases lasting at least four ticks. Initial time is the first tick of a phase. This initialization condition matters: minimum full phase length alone does not bound the residual length of a phase already underway.

Each available family has a current processing bit, `h_A` or `h_B`. It specifies which of two conversion settings produces usable input from that family's current form. The bits can vary arbitrarily every tick and independently of each other. They are not regime labels freely visible to the controller.

The organization has a continuing core, a reserve `r` with capacity three, and three physical module slots:

| Slot | A module does | B module does |
|---|---|---|
| Receptor | Reports A's presence and, when present, `h_A`. | Reports B's presence and, when present, `h_B`. |
| Transporter | Admits A. | Admits B. |
| Converter | Converts admitted A with a chosen processing setting. | Converts admitted B with a chosen processing setting. |

Each slot holds at most one module. A universal module that handles both families is not in the supplied repertoire; keeping both sets installed violates the slot constraint. These are explicit model premises, not a theorem that actual organisms or all possible hardware must face the same tradeoff.

A ready organization normally aligns all three slots with one family `q`. It can choose processing setting `a=0` or `a=1`. Input is two units exactly when transporter and converter types agree on an available family and `a=h_q`; otherwise input is zero. A mismatched setting is unproductive, rather than instantly fatal. Every tick consumes one unit for maintaining the core and interfaces. Reserve after the combined input/maintenance balance is

\[
r' = \min(3,\ r-1+I), \qquad I\in\{0,2\}.
\]

Input may pay current maintenance before surplus storage is clipped; this is not `min(3,r+I)-1`. Zero reserve is absorbing and disables all further operation. Continued functioning means `r>=1` after every tick. The dynamics therefore supply the specified functional criterion through the continued availability of sensing, actuation, and rebuilding. The model does not derive the ethical desirability of indefinite continuation.

Rebuilding removes and replaces the three modules. It occupies two whole ticks, with no input on either tick and one unit of maintenance per tick. The initiating decision can read the old receptor. The second rebuild tick supplies no observation; the new receptor becomes usable at the start of the next tick. An orientation flag retained by the continuing core determines which set is being installed. There is no instantaneous change, free harvest during reconstruction, reset of reserves, or resurrection after failure.

This modifies the selective material coupling at the boundary. It does not derive a spatial compartment, its supporting substrate, or new module designs from undifferentiated matter. The remaining enclosure and core are supplied; their operation depends on reserve.

## The implemented local policy

Initially, `r=3` and either aligned interface may be fitted. The policy is:

1. If a rebuild is underway, complete its second tick.
2. Otherwise read the currently fitted receptor. If its family is present, choose the reported processing setting and harvest.
3. If the receptor reports absence, begin rebuilding the other family's interface.

There is no global phase clock or access to the other processing bit. The assumption that at least one family is available makes absence of the currently fitted family a warranted reason to try the other; it is not a discovery of an unmodeled substrate. Current processing bits are read before that tick's selected conversion action.

## Indefinite continuation theorem

**Theorem.** With capacity and initial reserve three, initialization at a phase's first tick, arbitrary initial aligned interface, arbitrary processing bits, and every availability phase lasting at least four ticks, the implemented local policy never reaches zero reserve.

**Proof.** At a phase's start assume reserve three and an aligned ready interface. If that family is present, each harvest gains one net unit before clipping, so reserve stays three throughout the phase. If it is absent, the other family is present and remains present through the phase. Two rebuild ticks and two successful harvests produce the exact reserve path

\[
\boxed{3\to2\to1\to2\to3.}
\]

After those four ticks the fitted family is present and reserve is three. Any additional ticks preserve that state. The phase ends with the induction conditions restored. The initial state satisfies them, establishing the claim for every finite prefix and therefore every admitted infinite history. The current processing bits cannot break the argument because every harvest uses the corresponding current receptor report. □

Four-tick dwell is a sufficient contract for this local policy. At capacity three it is also sharp for a guarantee over all allowed availability histories, as the resource-counting proof below establishes. That necessity is not inferred merely from failure of the reactive policy.

The initialization condition also has a checked counterexample. Start with A fitted and reserve three, but with only one B-only tick left in an old phase. The first rebuild tick leaves reserve two. The world changes to A-only during the second rebuild tick; the new B interface comes online with reserve one. It then detects absence and cannot begin another rebuild without reaching zero. Every complete phase could still have length at least four. Thus arbitrary starting phase age cannot be silently added to the theorem.

## Why every fixed physical configuration fails

Use one common environment: four A-only ticks, four B-only ticks, and repeat. Give a fixed configuration perfect knowledge of all processing bits and any software or memory it wants. If its transporter and converter have different types, it never receives usable input. If both have type A, the B-only phase yields no input; if both have type B, the A-only phase yields no input. In either case reserve at most three reaches zero by the third tick of an opposite phase. A sensor cannot compensate for the absent physical conversion path.

This proves failure for all fixed choices of the three supplied modules, including mixed choices. Permitting the program to rebuild a slot changes the physical configuration and is exactly the capability under investigation; such a fixed program is not excluded from the successful class.

The comparison traces are:

| Configuration or intervention | First failure tick on A×4, B×4, A×4 | Reason |
|---|---:|---|
| Complete reconfiguration | None; final reserve 3 | Both changes preserve the path `3,2,1,2,3`. |
| Fixed A | 7 | B cannot supply usable input. |
| Fixed B | 3 | A cannot supply usable input. |
| Receptor frozen at A, remaining implemented controller retained | 7 | After switching the other modules to B, B's presence and processing bit remain unavailable. |
| Transporter frozen at A | 7 | B cannot cross the material interface. |
| Converter frozen at A | 7 | Admitted B cannot be converted. |

The intervention trajectories alone concern the implemented controller. The following arguments establish the broader limitations.

## Independent causal roles and a changing relevant distinction

**Transport and conversion.** If either module remains permanently A while only B is available, no choice of the other module, either sensor, or either processing setting can produce input. Even perfect external information cannot repair that material limitation. The same holds with A and B exchanged.

**Sensing.** Hold the transporter and converter at B, the receptor at A, and let only B be available. Two situations with `h_B=0` and `h_B=1` produce the same absent-A record. At reserve one, their safe harvest action sets are `{0}` and `{1}`. Rebuilding or waiting also reaches zero from reserve one. There is no action safe in both situations. The B receptor resolves the difference. For any deterministic controller lacking that observation, a permitted sequence of B processing bits can oppose every selected setting and keep input zero. Randomization cannot give a guarantee over all allowed histories and outcomes. This is an information limitation, not a low-quality policy claim.

The receptor changes more than a label. With A installed, it reveals `h_A` and leaves independent `h_B` unobserved. With B installed, the reverse holds. Under an A-compatible material organization, `h_A` changes which action produces support, while `h_B` does not affect that immediate conversion. After reconstruction the relevant processing distinction reverses. The need for the distinction follows from the specified supporting reaction; a separate rule does not award points merely for adopting a new viewpoint.

One must not generalize that dependence to every possible sense of significance. The supplied material repertoire, vulnerability, and preservation criterion still delimit the conclusion. The model does not generate arbitrary purposes or establish moral reasons from metabolism.

## Present operation and realizable transformation separate

A correctly matched organization with reserve one, two, or three can harvest successfully in the current tick. But initiating a two-tick rebuild from reserve one or two necessarily reaches zero before the new interface can supply input. Correctly recognizing the needed change does not create the resources to carry it out.

**Exact resource threshold.** Under the supplied rebuild primitive, a reserve capacity at most two makes every reconstruction fatal, irrespective of the controller's information or foresight. Without reconstruction, the alternating A/B environment eventually defeats any fixed physical configuration. Thus capacity at least three is necessary for guaranteed continuation through that environment. Capacity three is sufficient under the stated dwell and initialization contract.

The controller's guarantee depends on recovering its reserve before the next disturbance. It preserves not only present conversion but the ability to traverse a temporary interruption in input. The successful history never visits the absorbing state, so the persistence proved is uninterrupted continuation of the modeled core. An independently initialized copy would be a different history.

**Sharp timing contract at capacity three.** Let pure A and pure B phases alternate every three ticks. Suppose an arbitrary allowed controller survives `n` complete phases, starting ready with reserve three. Every phase must contain a successful harvest: three ticks without one exhaust capacity three. Select one successful harvest per phase. Their family types alternate, so between successive selected harvests there must be at least one completed reconstruction. There are therefore at least `n-1` reconstructions, consuming `2(n-1)` ticks without harvest. If `H` denotes successful harvests during these `3n` ticks,

\[
H\le3n-2(n-1)=n+2,
\qquad
r_{3n}\le3+H-(3n-H)\le7-n.
\]

Clipping surplus at capacity can only reduce this upper bound. At seven phases, survival requires reserve at least one but the bound is zero. This contradiction applies even with perfect foresight and anticipatory reconstruction. It proves that a universal minimum-dwell guarantee cannot be reduced to three at capacity three. Independent exhaustive propagation over all harvest, wait, and reconstruct histories in the [limits audit](limits-audit.md) finds no history survives tick fourteen; the simpler twenty-one-tick analytical bound is not claimed sharp. Capacity four changes this particular counterexample: a fixed interface can bridge each three-tick absence while remaining positive. The stated necessity is specific to capacity three and the stipulated actions.

## Verification

`check_joint_model.py` uses integer arithmetic and the Python standard library. `joint-model-checks.json` contains complete traces and scopes.

- 192 local rule cases include every reserve, interface, rebuilding state, availability set, and pair of current processing bits.
- 192 type-swap cases verify that exchanging A and B commutes with the complete law.
- 1,536 four-tick blocks cover every independent processing-bit history in each aligned initial-interface and fixed-availability case.
- 128 physical-module ablation cases verify zero intake under frozen incompatible transport or conversion.
- Four same-record/different-safe-action witnesses verify the sensing limitation.
- Exhaustive finite-state reachability for the implemented policy and all allowed phase changes finds 24 reachable states and 36 edges at minimum dwell four, no dead state, and minimum reserve one. Processing bits are soundly quotiented after the local checks establish identical controlled successors for all values. At minimum dwell three, the graph has two reachable dead states; at dwell two it has eight. Those graph counts concern this policy. The broader impossibility at capacity three and minimum dwell three is separately proved above and checked by the independent limits audit.
- Six comparison trajectories, an insufficient-initial-reserve trajectory, and the unknown-initial-phase-age counterexample are recorded.

The finite graph covers arbitrarily long histories by exploring every reachable node and allowed successor, rather than stopping after a sample time horizon. The displayed induction proves the general four-tick result independently of that enumeration.
