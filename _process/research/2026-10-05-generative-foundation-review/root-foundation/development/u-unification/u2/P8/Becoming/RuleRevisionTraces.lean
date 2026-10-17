import Becoming.Bridge

/-!
# Revised rules as actions of one process

`OpenFutureRevision` has a local arrangement of two unfinished configurations and two formed
outcomes, where each response rule advances the configuration (`advance`) and carries a count
of remaining steps (`remaining`). Each rule is one action of a process whose step under the rule
is that rule's advance (`process`, exact by `step_iff`), and the outcome a configuration realizes
makes it a frame (`frame`). This module states the module's revision results of that process's
traces, and its revising sequence as a run (`revising`).

* **A revision changes the formed outcome within the handoff bound.** From the left-ready
  configuration, the left rule then the direct-right rule is a trace ending in the right outcome,
  the left rule twice a trace ending in the left outcome, and the direct-right rule's remaining
  count at the right-ready configuration is within the left rule's (`changed_form`).
* **The formed outcome is not fixed.** From the right-ready configuration each of the two rules
  is a one-step trace ending where some outcome is realized, and no outcome is realized at the end
  of every such trace (`outcome_not_fixed`).
* **The revising sequence is a run** of the process, choosing at each step the rule
  `restartChoice` gives (`revising`, `revising_state`).
* **Generation by bound on a family of runs.** `OpenFutureRevision.generation_by_bound` hands a
  remaining-step certificate between revised rules along one history; `Becoming.Bridge` gives
  its positive relevance under the continuation condition for any family of histories
  (`revised_generation_by_bound_of_unrestricted`). Read on a family of runs of any process, the
  histories being the runs' configurations, each admitted run forms, within the bound, content
  absent before it and positively relevant under the continuation condition
  (`generation_by_bound_on_runs`).

The continuation condition occurs only as a hypothesis. No ethical predicate is asserted and no
axiom occurs.
-/

namespace Becoming

namespace RuleRevisionTraces

open Generative OpenFutureRevision

/-- Each rule as one action: the step under a rule is that rule's advance. -/
def process : Process Stage Rule := ⟨fun s p t => t = advance p s⟩

/-- The process with the outcome each configuration realizes. -/
def frame : Frame Stage Rule Bool := ⟨process, realizes⟩

/-- The process's step under a rule is exactly that rule's advance. -/
theorem step_iff {s t : Stage} {p : Rule} : process.step s p t ↔ t = advance p s :=
  Iff.rfl

/-- The revising sequence as a run: at each step the rule `restartChoice` gives. -/
def revising : Run process :=
  ⟨revisingRun, fun n => restartChoice (revisingRun n), fun _ => rfl⟩

/-- The run's configurations are the revising sequence. -/
theorem revising_state (n : Nat) : revising.state n = revisingRun n :=
  rfl

/-- **A revision changes the formed outcome within the handoff bound.** -/
theorem changed_form :
    Trace process .leftReady [.left, .directRight] .formedRight ∧
    Trace process .leftReady [.left, .left] .formedLeft ∧
    remaining .directRight .rightReady ≤ remaining .left .rightReady :=
  match changed_form_with_valid_handoff with
  | ⟨first, handoff, direct, left⟩ =>
    ⟨.cons first.symm (.cons direct.symm (.nil _)), .cons first.symm (.cons left.symm (.nil _)),
     handoff⟩

/-- **The formed outcome is not fixed**: from the right-ready configuration each of the two rules
is a one-step trace ending where some outcome is realized, and no outcome is realized at the end
of every such trace. -/
theorem outcome_not_fixed :
    (∀ p : Bool, ∃ t q, Trace process .rightReady [if p then .directRight else .left] t ∧
      frame.realized t q) ∧
    ¬ ∃ q, ∀ (p : Bool) t, Trace process .rightReady [if p then .directRight else .left] t →
      frame.realized t q :=
  ⟨fun p => match OpenFutureRevision.realized_form_need_not_be_fixed.1 p with
     | ⟨q, holds⟩ => ⟨_, q, trace_singleton_iff.mpr rfl, holds⟩,
   fun ⟨q, all⟩ => OpenFutureRevision.realized_form_need_not_be_fixed.2
     ⟨q, fun p => all p _ (trace_singleton_iff.mpr rfl)⟩⟩

/-- **Generation by bound on a family of runs.** Where along each admitted run the remaining-step
certificate falls at every unfinished step and is handed over within its bound, and every
completion forms content absent before, each admitted run forms, within the bound, such content,
positively relevant under the continuation condition. -/
theorem generation_by_bound_on_runs {S A H Q F Pos : Type} {P : Process S A} (r : H → Run P)
    (admitted : H → Prop) (rank : H → Nat → S → Nat) (completed : H → Nat → Prop)
    (decideEvent : ∀ h, DecidablePred (completed h))
    (appears : H → Nat → Q → Prop) (generative : Q → Prop) (before : H → Q → Prop)
    (bound : Nat) (initial : ∀ h, admitted h → rank h 0 ((r h).state 0) ≤ bound)
    (localStep : ∀ h, admitted h → ∀ n, ¬ completed h n →
      rank h n ((r h).state (n + 1)) < rank h n ((r h).state n))
    (handoff : ∀ h, admitted h → ∀ n, ¬ completed h n →
      rank h (n + 1) ((r h).state (n + 1)) ≤ rank h n ((r h).state (n + 1)))
    (correspondence : ∀ h, admitted h → ∀ n, completed h n →
      ∃ q, generative q ∧ appears h n q ∧ ¬ before h q)
    {sig : Pos → Nat → F → Prop} (unrestricted : Unrestricted sig)
    (formation : Q → F) (step : Q → Nat) :
    ∀ h, admitted h → ∃ q,
      (generative q ∧ (∃ n, n ≤ bound ∧ appears h n q) ∧
        ∀ p, sig p (step q) (formation q)) ∧ ¬ before h q :=
  revised_generation_by_bound_of_unrestricted admitted (fun h => (r h).state) rank completed
    decideEvent appears generative before bound initial localStep handoff correspondence
    unrestricted formation step

end RuleRevisionTraces

end Becoming
