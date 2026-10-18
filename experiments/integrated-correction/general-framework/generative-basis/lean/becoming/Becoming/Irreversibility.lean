import Becoming.Unfolding

/-!
# Return belongs to the law, not to the occurring change

Whether a configuration can be returned to is a property of the whole law, not of a change that
occurs: the same change can occur under a law that returns and under one that does not, and a
reading that omits which configuration was reached cannot tell them apart.

* **No return from a dead end.** The core's dead end, one step from `false` into `true` with no
  continuation (`DeadEnd.law`), never returns from `true` to `false` (`deadEnd_no_return`).
* **The same change, a different return.** The dead end and the flip (`flip`, every configuration
  goes to its negation) both take the change from `false` to `true`; the flip returns from `true`
  to `false` and the dead end does not (`same_change_different_return`).
* **A constant reading hides the loss.** Read through the constant summary, every question about
  what the dead end can reach has the same answer from `false` and from `true`, yet it cannot
  return from `true` to `false` (`constant_reading_hides_loss`).

The laws of return these instantiate are `keeps_reach_iff_returns` and `not_returns_iff_loses`
(`Becoming.Recurrence`). `BecomingReversibility` states these witnesses of its `oneWay` and
`twoWay`; its `oneWay` is `DeadEnd.law`. No ethical predicate, ranking or axiom occurs.
-/

namespace Becoming

open Generative

namespace Irreversibility

/-- Every configuration goes to its negation. -/
def flip : Process Bool Unit := ⟨fun s _ t => t = !s⟩

/-- **The dead end never returns from `true` to `false`.** -/
theorem deadEnd_no_return : ¬ Reach DeadEnd.law true false :=
  fun path => Bool.noConfusion
    (Invariant.reach (P := DeadEnd.law) (I := fun y => y = true)
      (fun _ _ _ step _ => step.2) path rfl : false = true)

/-- **The same change, a different return.** Both laws take the change from `false` to `true`;
the flip returns from `true` to `false`, the dead end does not. -/
theorem same_change_different_return :
    Trace DeadEnd.law false [()] true ∧ Trace flip false [()] true ∧
      ¬ Reach DeadEnd.law true false ∧ Reach flip true false :=
  ⟨trace_singleton_iff.mpr ⟨rfl, rfl⟩, trace_singleton_iff.mpr rfl, deadEnd_no_return,
   ⟨[()], trace_singleton_iff.mpr rfl⟩⟩

/-- **A constant reading hides the loss.** Every question about the constant reading of what the
dead end reaches has the same answer from `false` and from `true`, yet it cannot return from
`true` to `false`. -/
theorem constant_reading_hides_loss :
    (∀ q : Unit → Prop,
      (∃ t, Reach DeadEnd.law false t ∧ q ((fun _ => ()) t)) ↔
        (∃ t, Reach DeadEnd.law true t ∧ q ((fun _ => ()) t))) ∧
      ¬ Reach DeadEnd.law true false :=
  ⟨fun _ => ⟨fun ⟨_, _, held⟩ => ⟨true, Reach.refl _ _, held⟩,
     fun ⟨_, _, held⟩ => ⟨false, Reach.refl _ _, held⟩⟩,
   deadEnd_no_return⟩

end Irreversibility

end Becoming
