# From formed parts to a changing selector

6 October 2026. AI-assisted development following Ren's instruction to continue the [unified generative foundation](GENERATIVE-GROUNDING.md). The named connection is **actual part formation → resource-dependent assembly of a response-selection module → use, maintenance and replacement through its consequences**.

This joins two existing constructions through an explicit material interface. It does not infer an entire learning architecture from resource accounting. The component recipes, source-access protocol and consequence-to-maintenance coupling remain declared local laws.

## 1. What was missing between the existing results

The [formed-variant construction](../../../_process/history/2026-10-05-support-and-shared-generativity/completion/FORMED-VARIANT-SELECTION-INTEGRATION.md) starts without response variants and produces them through resource-dependent formation and copying. The [selector-revision construction](SELECTOR-REVISION.md) permits assembly and replacement of a response mapping. Each retains its own costs. Their separate validity does not establish that the output of the first can construct and operate the second.

The previous [support bridge](LEARNING-INTERFACE.md#5-joining-the-general-account-to-actual-formation) exposed an immediate obstruction: the original formation-to-copy witness ends with no energy left. A newly named learning stage cannot inherit its formed parts together with the original, already-spent fuel. The models also use different source units: one source unit in the formation account carries one support unit, whereas a packet in the selector example carries four.

The new construction retains the actual parts and stocks across that boundary. It adds a part requirement to assembly, so an affordable abstract operation can still be impossible when the required component type is absent.

## 2. The composed law and its supplied interface

Preparation follows the existing `FormedSelection` event law. A hidden environmental regime is carried separately; preparation events neither inspect nor change it. There are initially no free A or H parts and no resident module.

At handoff, the operational state retains common fuel, local fuel, free A and H, the resident and site condition. For packet size \(p>0\), the original source stock \(s\) is represented as

\[
s=pq+r,\qquad 0\le r<p.
\]

The packet count is \(q\), and the remainder \(r\) remains in the state and energy account. This changes the accounting denomination without creating fuel. Access to packets of that size is a supplied part of the operational protocol; the identity does not prove a physical batching or delivery mechanism. No initial selector is installed at handoff: its lease is zero, so a trial requires a later assembly event.

The declared component recipes are:

- two free A parts assemble the `false` response mapping;
- two free H parts assemble the `true` response mapping.

Assembly also pays the existing selector fuel cost. It moves its two parts from free inventory to incorporated inventory. Parts of expired modules remain accounted for and do not become free merely because the next assembly needs them. Which recipe is available depends on actual stocks, not on the hidden regime or an analyst's desired winner.

Each operational step projects to a step of the existing selector law. Its response, trial consequence, fuel payment, maintenance, expiry and reversal are preserved. The reverse implication requires the appropriate parts: the new process restricts assembly possibilities. This is a material refinement of the declared operational law, not an unconditional equivalence of all histories.

Preparation and operation are sequential stages. Preparation chemistry does not continue concurrently after handoff in this model. A real implementation would need to establish this schedule or account for continuing reactions. This explicit staging permits a finite joined proof without claiming an exact kinetic reduction of one chemistry to the other.

## 3. Support and component constraints are distinct

Let \(A_0,H_0\) be the free component counts at an operational starting state. Let \(N_f(w)\) and \(N_t(w)\) count the two kinds of assembly in an operational history \(w\). Every such history must satisfy

\[
2N_f(w)\le A_0,\qquad 2N_t(w)\le H_0.
\]

The stronger checked result is an **if-and-only-if construction criterion**. For a fixed inherited operational state and a proposed selector history with a specified endpoint, a material history projecting to that same history and endpoint exists exactly when:

1. the history is admitted by the existing selector law; and
2. both cumulative component demands above fit the inherited free stocks.

The first condition preserves the selector law's actual payments and consequences. The second supplies the precise additional construction obligation. Since components are consumed without replenishment in this operational phase, the cumulative bounds also suffice at every assembly prefix. This is `material_trace_lift_iff`; the theorem is not restricted to the concrete witness below.

An available fuel balance cannot manufacture missing components, and total material cannot substitute for the required type. Conversely, enough parts cannot pay an unaffordable operation. A positive-lease selector reached from the dormant handoff necessarily has at least two parts in incorporated inventory, so the model cannot obtain operative hardware by changing a flag without its construction.

During operation, the sum of free parts, resident material and incorporated parts remains constant. Closed support includes common fuel, packet energy, the retained remainder and the retained local store. Trial expenditure, maintenance and unused packet loss are charged to the same history. A source packet lost after an unsuccessful trial is not silently available for the retry.

This adds an organizational restriction to the candidate root: a history can have sufficient aggregate support while lacking the particular relations and component stocks needed to realize a proposed continuation. A higher-level response law therefore needs a construction interface as well as a numerical budget.

## 4. A single formation-to-revision history

Start with material capacity five, common fuel twelve, source eighteen, no variants, no resident and a damaged capture site. The regime is initially `false`. The existing formation law admits:

**Form H twice → form A → associate A → repair → capture → copy A locally → capture → copy A locally.**

This ends with two free A, two free H and one active resident, together with fuel seven and source sixteen. Both H formations must precede repair: formation in this law requires a damaged site. An initially proposed ordering with a late H formation was rejected by that guard. Event ordering is a causal condition, not a detail that total expenditures can replace.

Two actual captures fund the two local A copies. Preparation spends seven of the original thirty support units. The remaining sixteen source units become four selector packets of four units, with no remainder. Its selector projection is exactly the initial state of the earlier checked reversal witness.

The continuation is:

| Event | Fuel afterward | Source packets | What changes |
|---|---:|---:|---|
| Assemble using two A | 6 | 4 | The initially absent mapping becomes operative. |
| Productive trial | 7 | 3 | Actual capture pays maintenance. |
| Environment reverses | 7 | 3 | The mapping and resources are retained. |
| First unsuccessful trial | 5 | 2 | No return arrives; the old module wears. |
| Second unsuccessful trial | 3 | 1 | Its remaining lease expires. |
| Assemble using two H | 2 | 1 | A different mapping is constructed from remaining parts. |
| Productive trial | 3 | 0 | The new mapping captures and renews. |

The five material units now comprise one resident, two incorporated A and two incorporated H. Operational expenditure and lost packets account for twenty support units. Seven spent in preparation, twenty in operation and three remaining equal the original thirty. Neither reversal nor reconstruction resets the stocks.

This is a feasible history with a witnessed change of mapping inside the continuing compartment. Its existential proof does not force the assembly choices, supply their probabilities or guarantee recovery. The alternative H parts have a useful later role under the new recipe even though they do not repair the original site; the model does not identify one intrinsically best component type across all contexts.

## 5. Failure boundaries and verification

The exhausted earlier witness cannot pay for this assembly. A funded state with the wrong component type can admit an assembly in the abstract selector model while blocking it in the material construction. Too few source packets, too little prepaid fuel or a failed formation order can likewise prevent the joined path. These failures are part of the result.

A further checked history begins at the same prepared state, assembles the wrong H-based mapping, undergoes two unsuccessful trials, and then constructs the correct A-based mapping. It ends with **one fuel unit and two source packets**. The correct next trial requires two prepaid fuel units, so the eight units still contained in the packets cannot fund access to themselves. Correcting the mapping does not undo the material costs of reaching it. This refutes any inference that the constructible alternatives inevitably yield useful recovery.

The [Lean package](../../../experiments/integrated-correction/general-framework/generative-basis/lean/learning/construction/README.md) records **40 new theorem audits**, checked with Lean 4.29.1 alongside 82 inherited audits. Two new results report empty axiom dependencies; the other 38 use only the standard `propext` and/or `Quot.sound`. There are no proof holes or custom axioms. The [mathematical companion](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/CONSTRUCTED-LEARNING-MATH.md) gives the state interface, ledgers and witnesses. The [separate internal review](../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/CONSTRUCTED-LEARNING-REVIEW.md) checks the construction and its limits.

The independent finite check passes 6,480 handoff cases, the complete operational graph of 194 states and 510 labelled edges reachable from the main prepared state, and six counterchecks. A 456-case initial-stock grid also checks the declared joined word, without being presented as an all-stock theorem. These are checks of this synthetic law, not empirical evidence of a chemical implementation. Standard arithmetic and transition-refinement methods are used without a mathematical novelty claim.

## 6. What the next derivation can use

The input to resource-dependent module assembly now has a checked producer: an actual earlier history forms the required parts and leaves a specified reserve. Abstract assembly has a concrete component restriction. The operational history is connected through the actual successor rather than through a fresh example initialization.

The remaining premises are more precise: recipes that make these parts function as response mappings, a staged source-access protocol, sensory transduction, and the rule linking actual capture to maintenance. Their presence is not derived from distinction or conservation alone. The construction forms instances of the response module under those laws; it does not yet derive the complete sensing and updating architecture or its variation.

The subsequent [material-updater composition](MATERIAL-UPDATER-COMPOSITION.md) now carries the consumable component discipline into alternative updater formation. It gives selector and updater construction a shared stock and proves an exact history criterion, including a funded continuation blocked by spent components. This realizes a restricted updater law under explicit recipes; it does not equate consumable parts with recyclable slots. The next shared bridge is formed sensing/updating machinery acquiring and correcting predictions and causally using them in resource-dependent action. That work must retain the component, support and information interfaces already established. Private reconstruction and shared concern remain different explanatory obligations within the same foundation.
