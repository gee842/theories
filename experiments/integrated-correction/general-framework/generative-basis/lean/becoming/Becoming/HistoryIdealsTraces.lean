import Becoming.HistoryIdeals

/-!
# The histories of a process's words: the word half of `HistoryIdeals` on its traces

`Becoming.HistoryIdeals` reads histories as ideals twice: on the stretches of a process's runs
(`Stretches`, configurations and moves together), and on words of moves ordered by prefix, for
words of any type (`HistoryIdeals`). The word half was stated of words alone. Here the words are
the courses a process can take from a configuration (`Feasible`, the words of its traces), so the
word half is a law of the process's histories read by their moves only.

* **Which ideals of feasible courses are histories of the process.** An ideal of courses feasible
  from `s` that settles, or goes on with a course of each length picked, is a history of the
  process from `s`: one feasible course, or a sequence of moves every initial course of which is
  feasible from `s` (`classification`, `HistoryIdeals.classification` with
  `HistoryIdeals.history_within_iff` on the prefix-closed language of feasible courses). A
  feasible course settles as a history of the process (`course_settles`,
  `HistoryIdeals.principal_hasLongest`).
* **A run's moves go on.** The moves of every run are a history of the process from the run's
  start that goes on (`run_goesOn`, `HistoryIdeals.trace_goesOn`): each of its initial courses is
  the trace of the run's first steps (`run_initial_trace`).

* **The converse fails.** A sequence of moves every initial course of which is feasible need not be
  the moves of a run: in a process that from no configuration goes to any count and then counts
  down, every course of `()`s is feasible from the start and no run starts there
  (`history_without_run`). Each course ends where the next move is not possible; a run would need
  one configuration at each step continuing all of them. That is the difference between the word
  half and the stretches of runs (`Stretches`), where the configurations are part of the history.

No premise; every declaration has an empty axiom report.
-/

namespace Becoming

open Generative HistoryIdeals

universe u v

namespace HistoryIdealsTraces

variable {S : Type u} {A : Type v}

/-- A history of a process from `s`: a course feasible from `s`, or a sequence of moves each
initial course of which is feasible from `s`. -/
def HistoryOf (P : Process S A) (s : S) (h : History A) : Prop :=
  WithinLanguage (Feasible P s) h

/-- **An ideal of courses feasible from `s` that settles, or goes on with a course of each length
picked, is a history of the process from `s`.** -/
theorem classification (P : Process S A) (s : S) {I : Ideals.Ideal (prefixOrder A)}
    (feasible : Ideals.Within (prefixOrder A) (Feasible P s) I)
    (decided : HasLongest I ∨
      ∃ pick : Nat → List A, (∀ n, I.mem (pick n)) ∧ ∀ n, n < (pick n).length) :
    ∃ h : History A, Ideals.Ideal.Same I (historyIdeal h) ∧ HistoryOf P s h :=
  match HistoryIdeals.classification decided with
  | ⟨h, same⟩ =>
    ⟨h, same, (history_within_iff (HistoryLanguages.feasible_prefixClosed P s) h).mp
      fun w hw => feasible w ((same w).mpr hw)⟩

/-- **A feasible course settles as a history of the process.** -/
theorem course_settles (P : Process S A) (s : S) {w : List A} (feasible : Feasible P s w) :
    HasLongest (Ideals.principal (prefixOrder A) w) ∧ HistoryOf P s (.finite w) :=
  ⟨principal_hasLongest w, feasible⟩

/-- **Each initial course of a run's moves is the trace of its first steps.** -/
theorem run_initial_trace {P : Process S A} (r : Run P) :
    ∀ (k n : Nat) (a : Nat → A), (∀ m, a m = r.act (n + m)) →
      Trace P (r.state n) (initialWord a k) (r.state (n + k))
  | 0, _, _, _ => .nil _
  | k + 1, n, a, same =>
    have shift : n + 1 + k = n + (k + 1) := (Nat.succ_add n k).trans (Nat.add_succ n k).symm
    have first : P.step (r.state n) (a 0) (r.state (n + 1)) :=
      Eq.subst (motive := fun x => P.step (r.state n) x (r.state (n + 1))) (same 0).symm (r.step n)
    have rest := run_initial_trace r k (n + 1) (fun m => a (m + 1))
      (fun m => (same (m + 1)).trans
        (congrArg r.act ((Nat.add_succ n m).trans (Nat.succ_add n m).symm)))
    .cons first (Eq.subst (motive := fun x =>
        Trace P (r.state (n + 1)) (initialWord (fun m => a (m + 1)) k) (r.state x)) shift rest)

/-- **A run's moves are a history of the process from its start, and it goes on.** -/
theorem run_goesOn {P : Process S A} (r : Run P) :
    GoesOn (traceIdeal r.act) ∧ HistoryOf P (r.state 0) (.infinite r.act) :=
  ⟨trace_goesOn r.act, fun n =>
    ⟨_, run_initial_trace r n 0 r.act (fun m => congrArg r.act (Nat.zero_add m).symm)⟩⟩

/-! ## A history of words need not be a run's moves -/

/-- From no configuration the process goes to any count; from a count it counts down by one, and
from zero it does not go on. -/
def countdown : Process (Option Nat) Unit where
  step s _ t := match s with
    | none => match t with
      | none => False
      | some _ => True
    | some 0 => False
    | some (n + 1) => match t with
      | none => False
      | some m => m = n

theorem countdown_down : ∀ k, Trace countdown (some k) (initialWord (fun _ => ()) k) (some 0)
  | 0 => .nil _
  | k + 1 => .cons (show countdown.step (some (k + 1)) () (some k) from rfl) (countdown_down k)

/-- A run of the countdown is never at a count. -/
theorem countdown_ends (r : Run countdown) : ∀ k m, r.state m ≠ some k := by
  intro k
  induction k with
  | zero =>
    intro m h
    have st : countdown.step (r.state m) (r.act m) (r.state (m + 1)) := r.step m
    rw [h] at st
    cases hn : r.state (m + 1) with
    | none => rw [hn] at st; exact st
    | some _ => rw [hn] at st; exact st
  | succ k ih =>
    intro m h
    have st : countdown.step (r.state m) (r.act m) (r.state (m + 1)) := r.step m
    rw [h] at st
    cases hn : r.state (m + 1) with
    | none => rw [hn] at st; exact st
    | some j =>
      rw [hn] at st
      exact ih (m + 1) (hn.trans (congrArg some st))

/-- **A history of a process's words need not be the moves of a run**: every initial course of
the unending sequence of moves is feasible from no configuration, and no run starts there. -/
theorem history_without_run :
    HistoryOf countdown none (.infinite fun _ => ()) ∧ ¬ ∃ r : Run countdown, r.state 0 = none :=
  ⟨fun n => match n with
    | 0 => ⟨none, .nil none⟩
    | k + 1 => ⟨some 0, .cons (show countdown.step none () (some k) from trivial) (countdown_down k)⟩,
   fun ⟨r, h⟩ => by
    have st : countdown.step (r.state 0) (r.act 0) (r.state 1) := r.step 0
    rw [h] at st
    cases hn : r.state 1 with
    | none => rw [hn] at st; exact st
    | some j => exact countdown_ends r j 1 hn⟩

end HistoryIdealsTraces

end Becoming
