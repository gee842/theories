import Becoming.Courses

/-!
# Candidate runs: cross-situational resolution step by step along a run

`Becoming.CrossSituational` states what a form names when read across the records of the
occasions it was met: a record bearing on the form keeps exactly the candidates it offers, one not
bearing on it changes nothing, and under coverage a unique candidate is the target, while one
record omitting the target can leave a wrong meaning as the only candidate. `Becoming.Courses`
reads the moves of a run as its records (`Courses.run_candidates_append`,
`Courses.run_resolves_iff`). This module states those laws step by step along a run.

* **Each move of a run narrows the candidates by itself.** The record after `n + 1` moves is the
  record after `n` and the move at `n` (`window_succ`); a move bearing on the form keeps exactly the
  candidates it offers (`run_step_bearing`), and a move not bearing on it leaves them as they were
  (`run_step_other`).
* **Coverage along a run.** Where the target is in the repertoire and every bearing move of the
  first `n` offers it, a unique candidate after `n` moves is the target
  (`run_resolved_is_target`). Coverage cannot be dropped: on every run of a process with one move,
  the first move, read as the record that offers only `1`, omits the target `0` and leaves `1` the
  only candidate (`run_omitted`).

No ethical predicate, ranking or axiom occurs.
-/

namespace Becoming

open Generative CrossSituational

universe u v w

namespace CandidateRuns

variable {S : Type u} {A : Type v} {P : Process S A} {M : Type w}

/-- **The record of a run after `n + 1` moves is its record after `n` and the move at `n`.** -/
theorem window_succ (run : Run P) (n : Nat) :
    run.window 0 (n + 1) = run.window 0 n ++ [run.act n] :=
  (Courses.window_append run n 0 1).trans
    (congrArg (fun i => run.window 0 n ++ run.window i 1) (Nat.zero_add n))

/-- **A move of a run bearing on the form keeps exactly the candidates it offers.** -/
theorem run_step_bearing (bears : A → Bool) (offers : A → M → Bool) (run : Run P) (rep : List M)
    (n : Nat) (bearing : bears (run.act n) = true) :
    candidates bears offers rep (run.window 0 (n + 1)) =
      List.filter (offers (run.act n)) (candidates bears offers rep (run.window 0 n)) :=
  (congrArg (candidates bears offers rep) (window_succ run n)).trans
    (candidates_snoc_bearing rep (run.window 0 n) bearing)

/-- **A move of a run not bearing on the form leaves its candidates as they were.** -/
theorem run_step_other (bears : A → Bool) (offers : A → M → Bool) (run : Run P) (rep : List M)
    (n : Nat) (other : bears (run.act n) = false) :
    candidates bears offers rep (run.window 0 (n + 1)) =
      candidates bears offers rep (run.window 0 n) :=
  (congrArg (candidates bears offers rep) (window_succ run n)).trans
    (candidates_snoc_other rep (run.window 0 n) other)

/-- **Under coverage along a run, a unique candidate is the target.** Where the target is in the
repertoire and every bearing move of the first `n` offers it, the only candidate after `n` moves,
if there is one, is the target. -/
theorem run_resolved_is_target {bears : A → Bool} {offers : A → M → Bool} (run : Run P) (n : Nat)
    {rep : List M} {t e : M} (available : t ∈ rep)
    (covered : ∀ a, a ∈ run.window 0 n → bears a = true → offers a t = true)
    (resolved : candidates bears offers rep (run.window 0 n) = [e]) : e = t :=
  resolved_is_target available covered resolved

/-- **Coverage cannot be dropped.** On every run of a process with one move, the first move, read
as the record bearing on the form that offers only `1`, does not offer the target `0`, and leaves
`1` the only candidate of the repertoire `[0, 1]`. -/
theorem run_omitted {P : Process S Unit} (run : Run P) :
    Omitted.offers (run.act 0) 0 = false ∧
      candidates (fun _ : Unit => true) Omitted.offers [0, 1] (run.window 0 1) = [1] :=
  ⟨Omitted.target_uncovered, Omitted.wrong_unique⟩

end CandidateRuns

end Becoming
