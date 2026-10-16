import Becoming.Sampling

/-!
# Tower: continuous time as ever-finer discrete readings

Ren decided on 12 October 2026 that continuous time is built in the core as a tower of
ever-finer discrete readings, linked by the coarse-graining of `Becoming.Sampling`, a law of
continuous time being a law at every level of the tower; real-valued time is a later
correspondence in the periphery. The core takes no real numbers, so it stays pure.

* **A tower.** Readings at levels `0, 1, 2, …`, each a web and a flow; level `n` is level
  `n + 1` read at strictly increasing times `refine n` (`Tower`). A step `s` of level `0` is
  the step `reads n s` of level `n` (`Tower.reads`), and level `0` is level `n` read at those times
  (`Tower.web_zero`, `Tower.level_zero`).
* **Laws at every level.** Balance with each relatum listed once, and dissipation, pass from
  each level to the coarser one (`Tower.balances_coarser`, `Tower.dissipative_coarser`), as
  `Becoming.Sampling` shows for one coarse step.
* **Change bounded however finely divided.** A stretch of level `0` read at any level `n`:
  under a census of what stands at level `n`, where what stands is not refuted to run down at
  each fine step of it, the fine steps at which the total standing falls, which are the steps
  at which some standing changes, number at most the total standing of level `0` at the
  stretch's start (`Tower.changes_within`). The bound does not depend on `n`: dividing time
  more finely adds no change. This rests on the laws of one step (`Flow.runsDown_bounds_change`)
  and on the least loss per exchange, with no premise added.

Not done: real-valued time, which is a later periphery correspondence; towers with no
coarsest level; the exact form of the bound as levels refine.
-/

namespace Becoming

variable {F C : Type} [DecidableEq F]

/-- A tower of readings: at each level a web and a flow, level `n` being level `n + 1` read at
the strictly increasing times `refine n`. -/
structure Tower (F C : Type) [DecidableEq F] where
  web : Nat → Web F C
  flow : Nat → Flow F C
  refine : Nat → Nat → Nat
  strict : ∀ n, Strict (refine n)
  web_sample : ∀ n, web n = (web (n + 1)).sample (refine n)
  flow_sample : ∀ n, flow n = (flow (n + 1)).sample (refine n)

namespace Tower

variable (T : Tower F C)

/-- The step of level `n` at which step `s` of level `0` is read. -/
def reads : Nat → Nat → Nat
  | 0 => fun s => s
  | n + 1 => fun s => T.refine n (reads n s)

/-- The readings of level `0` are those of level `n` at the times `reads n`. -/
theorem web_zero : ∀ n, T.web 0 = (T.web n).sample (T.reads n)
  | 0 => rfl
  | n + 1 => (web_zero n).trans (congrArg (fun W => W.sample (T.reads n)) (T.web_sample n))

/-- So a level of level `0` is the level of level `n` at the step that reads it. -/
theorem level_zero (n s : Nat) (c : C) : (T.web 0).level s c = (T.web n).level (T.reads n s) c :=
  congrArg (fun W : Web F C => W.level s c) (T.web_zero n)

/-- The times `reads n` are strictly increasing. -/
theorem reads_strict : ∀ n, Strict (T.reads n)
  | 0 => fun s => Nat.lt_succ_self s
  | n + 1 => show Strict (fun s => T.refine n (T.reads n s)) from
    Strict.comp (T.strict n) (reads_strict n)

/-- Balance with each relatum listed once passes to the coarser level. -/
theorem balances_coarser {n : Nat} (once : (T.flow (n + 1)).Once)
    (balances : (T.flow (n + 1)).Balances (T.web (n + 1))) : (T.flow n).Balances (T.web n) :=
  Eq.subst (motive := fun L => L.Balances (T.web n)) (T.flow_sample n).symm
    (Eq.subst (motive := fun W => ((T.flow (n + 1)).sample (T.refine n)).Balances W)
      (T.web_sample n).symm (Flow.sample_balances (T.refine n) (T.strict n) once balances))

/-- So does dissipation. -/
theorem dissipative_coarser {n : Nat} (dissipative : (T.flow (n + 1)).Dissipative) :
    (T.flow n).Dissipative :=
  Eq.subst (motive := fun L => L.Dissipative) (T.flow_sample n).symm
    (Flow.sample_dissipative (T.refine n) dissipative)

/-- Change bounded however finely divided: a stretch of `N` steps of level `0` from `S`, read
at level `n`, under a census of what stands at level `n` and with what stands not refuted to
run down at each fine step of it, has at most as many fine steps at which the total standing
falls as the total standing of level `0` at `S`. The bound is the same at every level. -/
theorem changes_within {n S N : Nat} {stand : Nat → List C}
    (census : (T.web n).StandingCensus stand)
    (runs : ∀ t, t ∈ steps (T.reads n S) (T.reads n (S + N) - T.reads n S) →
      ¬¬ (T.flow n).RunsDown (T.web n) t) :
    count (steps (T.reads n S) (T.reads n (S + N) - T.reads n S))
        (fall fun t => (T.web n).stock (stand t) t) ≤
      (T.web 0).stock (stand (T.reads n S)) S :=
  Nat.le_trans (Nat.le_add_left _ _)
    (Nat.le_trans (Flow.runsDown_bounds_change census runs)
      (Nat.le_of_eq (total_congr_on fun c _ => (T.level_zero n S c).symm)))

end Tower

end Becoming
