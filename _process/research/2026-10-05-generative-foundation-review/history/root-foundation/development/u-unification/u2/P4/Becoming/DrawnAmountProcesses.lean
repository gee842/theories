import Becoming.Frame
import RelationalOrganization

/-!
# Continuations drawing on one amount as steps of a process

`RelationalOrganization` stipulates four continuations (`Form`) of one shared history with an
available amount of six: the idle continuation draws nothing, the two working routes draw two,
and overbuilding draws five (`spent`); what remains is `remaining f = 6 - spent f`, and the basis
holds where at least two remain (`basis`). The evident reading is a process on the amount whose
moves are the continuations, each step drawing what the continuation draws (`draw`). From the
shared amount the step by a continuation reaches exactly what remains after it (`draw_step_iff`).
This module states the module's results that carry an empty axiom report of the steps of that
process and proves them through them.

* **The basis is read off the configuration reached.** A step from the shared amount reaches a
  configuration of at least two exactly where the continuation keeps the basis
  (`basis_after`).
* **A step rests exactly where it draws nothing**, within the amount (`rests_iff_free`). The idle
  continuation's step from the shared amount rests, and the left route's step changes the
  configuration (`idle_rests_left_changes`): forming the route uses the free occasion.

The module's other results, its comparison of continuations (`better`, `Frontier`, `Required`)
and its report judgements, carry `propext`, `Quot.sound` or `Classical.choice` in their axiom
reports; `Becoming.DrawnAmountProcessesInherited` states them of the same steps and of the frame
of the continuations. No ethical predicate, ranking or axiom occurs.
-/

namespace Becoming

open Generative

namespace DrawnAmountProcesses

open RelationalOrganization

/-- The continuations as moves on the amount: each step draws what the continuation draws. -/
def draw : Process Nat Form := ⟨fun a f b => b = a - spent f⟩

/-- **From the shared amount, the step by a continuation reaches exactly what remains after
it.** -/
theorem draw_step_iff {f : Form} {b : Nat} : draw.step 6 f b ↔ b = remaining f :=
  Iff.rfl

/-- **The basis is read off the configuration reached**: a step from the shared amount reaches a
configuration of at least two exactly where the continuation keeps the basis. -/
theorem basis_after {f : Form} {b : Nat} (step : draw.step 6 f b) : 2 ≤ b ↔ basis f :=
  Eq.subst (motive := fun x => 2 ≤ x ↔ basis f) step.symm
    (amount_sensitive_repair_recovers_the_local_basis f)

/-- Within the amount, drawing leaves the amount as it was only where nothing is drawn. -/
theorem eq_zero_of_sub_eq : ∀ {a x : Nat}, x ≤ a → a - x = a → x = 0
  | _, 0, _, _ => rfl
  | 0, _ + 1, within, _ => absurd within (Nat.not_succ_le_zero _)
  | a + 1, x + 1, _, same =>
    absurd (Nat.le_trans (Nat.le_of_eq (same.symm.trans (Nat.succ_sub_succ a x)))
      (Nat.sub_le a x)) (Nat.not_succ_le_self a)

/-- **A step rests exactly where it draws nothing**, within the amount. -/
theorem rests_iff_free {a b : Nat} {f : Form} (within : spent f ≤ a) (step : draw.step a f b) :
    b = a ↔ freeOccasion f () :=
  ⟨fun rests => eq_zero_of_sub_eq within (step.symm.trans rests),
   fun free => step.trans (congrArg (a - ·) free)⟩

/-- **The idle continuation's step from the shared amount rests, and the left route's step
changes the configuration**: forming the route uses the free occasion. -/
theorem idle_rests_left_changes :
    (∀ b, draw.step 6 .idle b → b = 6) ∧ (∀ b, draw.step 6 .left b → b ≠ 6) :=
  ⟨fun _ step => (rests_iff_free (Nat.zero_le 6) step).mpr formation_has_a_real_loss.1,
   fun _ step rests => formation_has_a_real_loss.2
     ((rests_iff_free (Nat.le_of_ble_eq_true rfl) step).mp rests)⟩

end DrawnAmountProcesses

end Becoming
