# Connecting descriptions without losing the learner

6 October 2026. AI-assisted development following the [generative-grounding goal](GENERATIVE-GROUNDING.md). This study addresses **material dynamics → retained observations → response selection**, complementing the work that constructs selectors and updater mechanisms.

## The connection

Learning and decision-making can be realized by organized substrate dynamics. Explaining that realization requires relating descriptions at different scales: formed components, their operative arrangement, acquired evidence and subsequent responses. A description can preserve every physically available event sequence while losing the information an installed learner uses to choose among those events.

The missing mathematical connection is therefore precise: **when does an exact description of world possibilities remain exact after an observation-dependent controller is attached?**

## The result

Let a map summarize concrete world states. Suppose:

1. Every concrete step projects to an abstract step, and every abstract step lifts from each actual concrete predecessor that it represents.
2. Corresponding steps deliver the same complete observation to the controller.
3. Both descriptions retain the same controller and its actual inherited memory.

Then the map, extended to retain memory, preserves and lifts every finite controlled history, including its action/observation sequence and projected final world state with the same final memory. The [mathematical companion](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/CONTROLLED-REFINEMENT-MATH.md) proves this by composing the existing world-history and controller interfaces.

This is a sufficient contract for the declared finite histories. It does not assert that all observations must always be retained: a particular controller may ignore some differences. A less detailed representation is legitimate when its appropriate behavioral contract is separately established.

Compatible interfaces can be chained through several descriptions while retaining the same memory. This result uses the same action vocabulary and step granularity on both sides. Several molecular reactions implementing one learning operation would need a further mapping that accounts for those intermediate events and costs.

**Subsequent extension:** [protocol composition](PROTOCOL-COMPOSITION.md) supplies a conditional mapping for completed multi-event implementations, including physical boundary memory and intermediate cost accounts. It also proves why an exact account of completed operations can omit an admitted infinite internal execution. The extension does not turn completed-history equivalence into a guarantee that the operation finishes.

Resource accounts also need their own compatibility. A transported account preserves the costs and credits already represented by its law. It does not pay for a sensor, memory write or component that the law omitted.

## Why matching physical possibilities is insufficient

Consider a world with a hidden bit and fuel. Each permitted action costs one fuel unit, whatever the bit. A summary retaining only fuel preserves all physically available action sequences and their fuel costs.

Now attach a controller that probes, remembers the bit and chooses a corresponding response. If the summary also erases the probe's information, it no longer reproduces that controller's choices. With the bit true, the concrete controller can issue **probe → respond true**, while the erased channel makes the abstract controller issue **probe → respond false**.

The failure is informative: causal differences become relevant to a representation through the organization that senses, retains and uses them. No intention is attributed to individual molecules. The counterexample identifies a relation the higher-level description must preserve.

## How this helps the parallel derivation

| Existing contribution | What a subsequent composition must retain |
|---|---|
| [Formation of parts and selector assembly](MATERIAL-SELECTOR-COMPOSITION.md) | Actual typed parts, paid construction and inherited fuel; the joining recipes remain supplied. |
| [Formation and replacement of updater mechanisms](UPDATER-FORMATION.md) | The mechanism's effect on revision and its material history; its recyclable slots must not silently become the other model's consumed parts. |
| [Acquired teaching and prediction](../../../_process/history/2026-10-05-support-and-shared-generativity/completion/CONSEQUENCE-TO-LEARNING-INTEGRATION.md) | The complete acquired evidence, written memory, timing and actual sampling conditions. |
| This representation result | A proved world mapping together with observation and memory compatibility; budget and probability claims retain separate premises. |

This result does not claim those implementations are already one process. It gives the next construction a precise test for whether its descriptions agree about the learner. A one-way simulation or a restriction to particular histories can also be useful, provided it is stated at that weaker scope.

The next substantive bridge remains **formed, revisable machinery → acquired prediction → causal use in action under the same material and support history**. After that, the concern studies still require an explanation of how predictions about other centers enter evaluation. Private predictive accuracy alone does not supply that relation.

## Verification and scope

The [formal module](../../../experiments/integrated-correction/general-framework/generative-basis/lean/learning/ControlledRefinement.lean) uses the existing causal core and controller definitions. A fresh Lean 4.29.1 build passed **15 new theorem audits**: six general interface results and nine countermodel/account results. Ten have empty axiom dependencies; the other five use only the standard `propext` and/or `Quot.sound`. No proof holes or custom axioms are used. The [saved audit](../../../experiments/integrated-correction/general-framework/generative-basis/lean/learning/controlled-refinement-audit.txt) includes source and compiler hashes. Run `python3 check_controlled_refinement.py` in the existing learning directory to reproduce it.

The [separate review](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/CONTROLLED-REFINEMENT-REVIEW.md) records interpretation and integration limits. No new learning algorithm, physical law, empirical validation or mathematical novelty is claimed. The completed result is a compatibility theorem for supplied deterministic controllers and relational world dynamics, not a derivation of their origin or a completion of the unified foundation.
