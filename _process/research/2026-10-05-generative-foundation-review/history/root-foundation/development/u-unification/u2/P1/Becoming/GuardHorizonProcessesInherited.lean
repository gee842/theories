import Becoming.GuardHorizonProcesses

/-!
# A guard kept over a horizon: the laws of `CorrectionInfrastructure` that inherit axioms

`GuardHorizonProcesses` reads the step relation of `CorrectionInfrastructure` as the step of a
process and a deterministic law with free moves `next : S → A → S` as the process
`Viability.disturbed next (fun _ => True)`; there a choice of moves stays within the guard over `n`
steps exactly when its course is a trace of the law's process kept within the guard
(`GuardHorizonProcesses.pathSafe_iff`), and keeping the guard under the law is keeping it in the
law's process (`GuardHorizonProcesses.dViable_iff`). This module states, on those readings, the
laws of `CorrectionInfrastructure` whose proofs there use `propext`, `Quot.sound` or
`Classical.choice`.

* **Acceptance after restricting the moves.** For every process, a choice best by the score with
  acceptance among moves admissible for keeping the guard `n` more steps accepts, is enabled, leads
  only to configurations keeping the guard `n` more steps, and has the best base score among the
  admissible moves (`shielded_choice`).
* **Values computed within the guard.** Under a value function certified step by step within the
  guard (`Bellman`), every choice of moves whose course is a trace of the law's process kept within
  the guard returns at most the value (`kept_return_le`). Where the choice is best by the score with
  acceptance at every configuration keeping the guard, from every configuration that keeps the
  guard for `n` steps in the law's process its course is such a trace and returns exactly the value
  (`recomputed_kept`), and the choice accepts at each such configuration (`recomputed_accepts`).
* **Choosing from readings.** A choice of admissible moves can be made from a reading of the
  configurations exactly when each reading has one move admissible at every configuration giving it
  (`uniform_iff`).

Which guard marks what an activity needs, the scores and the value function are supplied with each
application. No ethical predicate or ranking occurs. Inherited axioms: `propext` and `Quot.sound`
from `CorrectionInfrastructure.shielded_acceptance_composition`,
`CorrectionInfrastructure.bellman_bounds_every_safe_policy`,
`CorrectionInfrastructure.dynamically_recomputed_composition` and
`CorrectionInfrastructure.dynamic_composition_accepts_at_every_viable_decision`;
`Classical.choice` from `CorrectionInfrastructure.uniform_policy_iff_fiber_feasible`.
-/

namespace Becoming

open Generative

namespace GuardHorizonProcessesInherited

open CorrectionInfrastructure GuardHorizonProcesses

variable {S A : Type} (P : Process S A) (guard : S → Prop)

/-! ## Acceptance after restricting the moves -/

/-- **A choice best by the score with acceptance among the moves admissible for keeping the guard
`n` more steps accepts, is enabled, leads only to configurations keeping the guard, and has the
best base score among the admissible moves.** -/
theorem shielded_choice {n : Nat} {s : S} {q : A → Int} {bonus : Int} (positive : 0 < bonus)
    {x : A × Bool}
    (best : Best (fun y : A × Bool => Admissible P.step guard n s y.1) (AcceptScore q bonus) x) :
    x.2 = true ∧ Enabled P s x.1 ∧ (∀ t, P.step s x.1 t → Viable P.step guard n t) ∧
      ∀ a, Admissible P.step guard n s a → q a ≤ q x.1 :=
  shielded_acceptance_composition P.step guard n s q bonus positive x best

/-! ## Values computed within the guard -/

variable (next : S → A → S)

/-- **Under a value function certified step by step within the guard, every choice of moves whose
course is a trace of the law's process kept within the guard returns at most the value.** -/
theorem kept_return_le {reward : S → A → Int} {V : Nat → S → Int}
    (bellman : Bellman next guard reward V) (policy : Nat → S → A) {n : Nat} {s : S}
    (kept : Kept (Viability.disturbed next fun _ => True) guard s (moves next policy n s)
      (last next policy n s)) :
    Return next reward policy n s ≤ V n s :=
  bellman_bounds_every_safe_policy next guard reward V bellman policy n s
    ((pathSafe_iff guard next policy n s).mpr kept)

/-- **A choice best by the score with acceptance at every configuration keeping the guard: from
every configuration keeping the guard for `n` steps in the law's process, its course is a trace of
the process kept within the guard and returns exactly the value.** -/
theorem recomputed_kept {reward : S → A → Int} {V : Nat → S → Int}
    (bellman : Bellman next guard reward V) {bonus : Int} (positive : 0 < bonus)
    (choose : Nat → S → A × Bool)
    (optimal : ∀ n s, DViable next guard (n + 1) s →
      Best (fun x : A × Bool => DAllowed next guard n s x.1)
        (AcceptScore (fun a => reward s a + V n (next s a)) bonus) (choose n s))
    {n : Nat} {s : S} (viable : Viable (Viability.disturbed next fun _ => True).step guard n s) :
    Kept (Viability.disturbed next fun _ => True) guard s (moves next (fun k t => (choose k t).1) n s)
        (last next (fun k t => (choose k t).1) n s) ∧
      Return next reward (fun k t => (choose k t).1) n s = V n s :=
  match dynamically_recomputed_composition next guard reward V bellman bonus positive choose optimal
      n s ((dViable_iff guard next n s).mpr viable) with
  | ⟨safe, value⟩ => ⟨(pathSafe_iff guard next _ n s).mp safe, value⟩

/-- **A choice best by the score with acceptance among the moves after which the law's process
keeps the guard `n` more steps accepts.** -/
theorem recomputed_accepts {reward : S → A → Int} {V : Nat → S → Int} {bonus : Int}
    (positive : 0 < bonus) (choose : Nat → S → A × Bool) {n : Nat} {s : S}
    (best : Best
      (fun x : A × Bool => Viable (Viability.disturbed next fun _ => True).step guard n (next s x.1))
      (AcceptScore (fun a => reward s a + V n (next s a)) bonus) (choose n s)) :
    (choose n s).2 = true :=
  dynamic_composition_accepts_at_every_viable_decision next guard reward V bonus positive choose n s
    ⟨(dViable_iff guard next n _).mpr best.1,
     fun x allowed => best.2 x ((dViable_iff guard next n _).mp allowed)⟩

/-! ## Choosing from readings -/

/-- **A choice of admissible moves can be made from a reading of the configurations exactly when
each reading has one move admissible at every configuration giving it.** -/
theorem uniform_iff {O : Type} (read : S → O) (n : Nat) :
    UniformPolicy read (Admissible P.step guard n) ↔
      ∀ o, ∃ a, ∀ s, read s = o → Admissible P.step guard n s a :=
  uniform_policy_iff_fiber_feasible read (Admissible P.step guard n)

end GuardHorizonProcessesInherited

end Becoming
