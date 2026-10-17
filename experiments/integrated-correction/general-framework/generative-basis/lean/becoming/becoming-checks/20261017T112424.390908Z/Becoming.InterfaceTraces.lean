import Becoming.Bridge
import AlignmentInquiry

/-!
# A probing interface is a process, and a plan's execution is a trace of it

`AlignmentInquiry` supplies a finite contingent planner over an interface: from a configuration a
probe of a query returns an answer and the configuration after it, a response returns the next
configuration, and a plan probes its query and responds by the branch of the answer
(`AlignmentInquiry.run`). This module reads the interface as a process of the spine: its moves are
a probe of a query with its answer, and a response (`process`). A plan's execution is then
exactly a trace of two moves, the probe with the answer received and the response that answer
selects (`run_iff_trace`), so a plan passes at a configuration exactly where such a trace reaches
an achieved configuration (`passes_iff_completes`), and a plan is valid for a listed belief
exactly where the belief is not empty and the plan completes from each configuration listed
(`valid_iff`).

* `process`: the interface's moves as a process; the answer is part of the probing move.
* `Completes`: a trace of the plan's two moves from a configuration reaches an achieved one.
* `run_iff_trace`, `passes_iff_completes`, `valid_iff`: the exactness of the reading.

No ethical predicate, ranking or axiom occurs.
-/

namespace Becoming

open Generative AlignmentInquiry

namespace InterfaceTraces

variable {S Q A : Type}

/-- **The interface as a process.** Probing query `q` with answer `b` moves to the configuration
the probe returns with that answer; responding with `a` moves to the configuration the response
returns. -/
def process (m : Interface S Q A) : Process S (Sum (Q × Bool) A) :=
  ⟨fun s x t => match x with
    | .inl (q, b) => m.probe s q = some (b, t)
    | .inr a => m.respond s a = some t⟩

/-- The two moves of a plan given an answer: probe its query with that answer, then respond by
the branch the answer selects. -/
def moves (p : Plan Q A) (answer : Bool) : List (Sum (Q × Bool) A) :=
  [.inl (p.query, answer), .inr (branch p answer)]

/-- A plan completes from a configuration: a trace of its two moves reaches an achieved
configuration. -/
def Completes (m : Interface S Q A) (p : Plan Q A) (s : S) : Prop :=
  ∃ answer t, Trace (process m) s (moves p answer) t ∧ m.achieved t = true

theorem run_none {m : Interface S Q A} {p : Plan Q A} {s : S}
    (h : m.probe s p.query = none) : run m p s = none := by
  unfold run
  rw [h]
  rfl

theorem run_some {m : Interface S Q A} {p : Plan Q A} {s after : S} {answer : Bool}
    (h : m.probe s p.query = some (answer, after)) :
    run m p s = m.respond after (branch p answer) := by
  unfold run
  rw [h]
  rfl

/-- **A plan's execution is a trace of the interface's process.** The plan's run from `s` ends
at `t` exactly when a trace of its two moves, for the answer the probe gives, leads from `s`
to `t`. -/
theorem run_iff_trace (m : Interface S Q A) (p : Plan Q A) (s t : S) :
    run m p s = some t ↔ ∃ answer, Trace (process m) s (moves p answer) t :=
  match h : m.probe s p.query with
  | none =>
    ⟨fun ran => (nomatch (run_none h).symm.trans ran),
     fun ⟨_, .cons probed _⟩ => nomatch h.symm.trans probed⟩
  | some (answer, after) =>
    ⟨fun ran => ⟨answer, .cons h (.cons ((run_some h).symm.trans ran) (.nil t))⟩,
     fun ⟨answer', .cons (m := mid) probed (.cons responded rest)⟩ =>
      match rest with
      | .nil _ =>
        have same : (answer, after) = (answer', mid) := Option.some.inj (h.symm.trans probed)
        have sameAnswer : answer = answer' := congrArg Prod.fst same
        have sameAfter : after = mid := congrArg Prod.snd same
        (run_some h).trans (by subst sameAnswer; subst sameAfter; exact responded)⟩

/-- **A plan passes at a configuration exactly where it completes there.** -/
theorem passes_iff_completes (m : Interface S Q A) (p : Plan Q A) (s : S) :
    passes m p s = true ↔ Completes m p s :=
  match ran : run m p s with
  | none =>
    ⟨fun passed => Bool.noConfusion
        ((show passes m p s = false from congrArg (fun o => o.any m.achieved) ran).symm.trans
          passed),
     fun ⟨_, t, path, _⟩ => nomatch ran.symm.trans ((run_iff_trace m p s t).mpr ⟨_, path⟩)⟩
  | some t =>
    ⟨fun passed => match (run_iff_trace m p s t).mp ran with
      | ⟨answer, path⟩ => ⟨answer, t, path,
          (show passes m p s = m.achieved t from congrArg (fun o => o.any m.achieved) ran).symm.trans
            passed⟩,
     fun ⟨_, t', path, achieved⟩ =>
      have reached : some t = some t' := ran.symm.trans ((run_iff_trace m p s t').mpr ⟨_, path⟩)
      (show passes m p s = m.achieved t from congrArg (fun o => o.any m.achieved) ran).trans
        ((congrArg m.achieved (Option.some.inj reached)).trans achieved)⟩

/-- **A plan is valid for a listed belief exactly where the belief is not empty and the plan
completes from every configuration listed.** -/
theorem valid_iff (m : Interface S Q A) (states : List S) (p : Plan Q A) :
    valid m states p = true ↔ states ≠ [] ∧ ∀ s, s ∈ states → Completes m p s :=
  match states with
  | [] => ⟨fun v => Bool.noConfusion v, fun ⟨nonempty, _⟩ => absurd rfl nonempty⟩
  | s :: rest =>
    have unfolded : valid m (s :: rest) p = (s :: rest).all (passes m p) := rfl
    ⟨fun v => ⟨fun e => (nomatch e), fun x mem =>
        (passes_iff_completes m p x).mp (list_all_true_iff.mp (unfolded.symm.trans v) x mem)⟩,
     fun ⟨_, all⟩ => unfolded.trans (list_all_true_iff.mpr fun x mem =>
        (passes_iff_completes m p x).mpr (all x mem))⟩

end InterfaceTraces

end Becoming
