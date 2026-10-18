import Becoming.Revision

/-!
# Revision runs: what the history of a run's lumpings selects, and the reconstruction steps

`Becoming.Revision` states that lumping through a jointly retained old and new reading gains
the new distinctions (`Registration.retained_gains`), and, of the reconstruction process
`Revising.P`, that the lumping with the link unformed cannot select between the two
reconstruction choices (`Revising.old_cannot_select_rebuild`) while forming the link keeps every
old distinction (`Revising.opened_keeps`). The history of a run's lumpings
(`Registration.History`) is defined of the run. This module states those laws of runs and steps.

* **The history through the first step is the retained reading.** Two inputs are alike in the
  history of a run's lumpings through step `1` exactly where the readings at the start and
  at step `1`, taken together, agree on them (`history_retained_iff`). So where the reading at
  step `1` tells apart two inputs the reading at the start merges, the history through every later
  step selects what the reading at the start cannot (`history_gains`).
* **The reconstruction process.** Every step of `Revising.P` forming the link from a configuration
  with the link unformed and the response false keeps every old distinction
  (`rebuild_opens_keeps`).

No ethical predicate, ranking or axiom occurs.
-/

namespace Becoming

open Generative

universe u v w z

namespace RevisionRuns

section Histories

variable {S : Type u} {A : Type v} {X : Type w} {V : Type z} {P : Process S A}

/-- **The history of a run's lumpings through step `1` is the retained reading**: two inputs
are alike in it exactly where the readings at the start and at step `1`, taken together, agree on
them. -/
theorem history_retained_iff (r : Run P) (obs : S → X → V) (x y : X) :
    Registration.History r (fun s a b => obs s a = obs s b) 1 x y ↔
      (obs (r.state 0) x, obs (r.state 1) x) = (obs (r.state 0) y, obs (r.state 1) y) :=
  ⟨fun h => (congrArg (fun a => (a, obs (r.state 1) x)) (h 0 (Nat.zero_le 1))).trans
      (congrArg (fun b => (obs (r.state 0) y, b)) (h 1 (Nat.le_refl 1))),
   fun same n le => match n, le with
    | 0, _ => congrArg Prod.fst same
    | 1, _ => congrArg Prod.snd same
    | k + 2, le => absurd (Nat.le_of_succ_le_succ le) (Nat.not_succ_le_zero k)⟩

/-- **Keeping the history gains what the start cannot select.** Where the reading at step `1` of a
run tells apart two inputs the reading at the start merges, some selection is through the history
of the run's lumpings through every step from `1` on and not through the reading at the
start. -/
theorem history_gains (r : Run P) (obs : S → X → V) {x y : X}
    (same : obs (r.state 0) x = obs (r.state 0) y) (different : obs (r.state 1) x ≠ obs (r.state 1) y)
    {t : Nat} (later : 1 ≤ t) :
    ∃ select, Learning.Training.Through (Registration.History r (fun s a b => obs s a = obs s b) t)
        select ∧
      ¬ Learning.Training.Through (fun a b => obs (r.state 0) a = obs (r.state 0) b) select :=
  match Registration.retained_gains same different with
  | ⟨select, through, lost⟩ =>
    ⟨select, Registration.through_history_later r
      (fun a b h => through a b ((history_retained_iff r obs a b).mp h)) later, lost⟩

end Histories

/-! ## The reconstruction process -/

/-- **Forming the link keeps every old distinction.** Every step of `Revising.P` forming the link
from a configuration with the link unformed and the response false keeps the lumping. -/
theorem rebuild_opens_keeps {s t : Revising.State} (step : Revising.P.step s (.rebuild true) t)
    (closed : s.2 = (false, false)) : Registration.Keeps Revising.alike s t :=
  match step with
  | ⟨n, _, moved⟩ =>
    have hs : s = (s.1, false, false) := congrArg (Prod.mk s.1) closed
    have ht : t = (n, true, false) :=
      moved.trans (congrArg (fun b => (n, true, b)) (congrArg Prod.snd closed))
    Eq.subst (motive := fun u => Registration.Keeps Revising.alike u t) hs.symm
      (Eq.subst (motive := fun u => Registration.Keeps Revising.alike (s.1, false, false) u) ht.symm
        (Revising.opened_keeps s.1 n))

end RevisionRuns

end Becoming
