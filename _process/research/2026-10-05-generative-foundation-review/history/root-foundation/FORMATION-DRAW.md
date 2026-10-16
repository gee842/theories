# Formation and recovery draw what every native operation draws

7 October 2026. AI-assisted continuation of the [contact-formation track](CONTACT-FORMATION-LAW.md), which listed "applying the native interface draw to recovery and formation" as supplied. It follows the [nondual method](../../../../theories/becoming/chapters/NONDUAL-METHOD.md): formation and recovery are treated as operations of the same activity as the native commands, so the question is whether that activity has one draw law or several.

**Formal status:** [FormationDraw.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/FormationDraw.lean), 27 declarations, every axiom report empty. It imports `FormationClosure` and `PhasePeriodSelection` unchanged and reuses `sensing_command_draws`. It is checked by [check_stock_derivation.py](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/check_stock_derivation.py).

## Transition addressed

Native draw law → draw of formation and recovery.

## What is derived

| Result | Lean statement |
|---|---|
| The native activity has one draw law: every completed operation draws `draw`, a probe making two operations (before and after its conversion); `draw` stays fixed | `native_operation_draw` (uses `sensing_command_draws`) |
| Formation and recovery stated with an open draw; with `draw` they are exactly the supplied ones | `formWith`, `recoverWith`, `formWith_native`, `recoverWith_native`, `processWith_native_step` |
| The closure process keeps one draw law for all its events, and a completed history draws its operations times `draw` | `closure_one_draw_law`, `closure_trace_draw` |
| **Any single draw law of the extended process is the native one**, on every state where a native advance completes | `one_law_is_native_draw` |
| Under a single draw law, formation and recovery must draw `draw` wherever they and a native command both complete | `one_law_forces_formation_draw`, `one_law_forces_recovery_draw` |
| A formation that draws nothing leaves the extended process with no single draw law | `free_formation_breaks_one_law` |

## Status of the input

**Derived, relative to a stated claim.** The claim is that the extended process has one draw law for all its operations, as the native activity already has for its four commands. Under it the formation and recovery draw is forced to be `draw`. Without it, the countercase shows that a separately chosen draw is consistent with the native commands, but splits the process into two draw laws, one for native commands and one for formation. That split is exactly the kind of independent starting point the project's method asks to make accountable; here it is shown to be avoidable, and what it would cost is stated.

Still not derived: why each operation draws `16384 + live + workspace + 2` ticks (the inherited per-operation draw), and the scope restriction to states where a native command also completes. On states where formation completes but no native command can, a single law does not constrain the formation draw.

## What would change the account

A native command whose draw differs from `draw` on the same state. Then the native activity itself would have no single draw law and this argument would not apply.

## Reproduce

From `experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/` with Lean 4.29.1 on `PATH`: `python3 check_stock_derivation.py`.
