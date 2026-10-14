import Becoming.Joint
import Becoming.Inquiry

/-!
# Assurance: when a plan secures its target

`InquirySufficiency.Completes P safe goal s plan` asks that every step of the plan be possible
and safe from every configuration the earlier steps can reach, and that every endpoint meet the
goal. This module states, for every process, when that holds.

* For every process, a plan that completes runs to an endpoint, every run of it is safe, and
  every endpoint meets the goal (`runs_of_completes`).
* **For every determined process** (`Becoming.Determined`: a move has at most one successor) the
  converse holds: a plan completes exactly when it runs, its run is safe and its endpoint meets
  the goal (`completes_iff_of_determined`). With no safety condition, a plan completes exactly
  when it runs and every endpoint meets the goal (`completes_iff_runs`).
* The converse fails for a process with two outcomes of one move: in `Branch`, both moves of
  `[(), ()]` run from `0` and every endpoint is `3`, yet the plan does not complete, because the
  first step can reach a configuration from which the second move is impossible
  (`Branch.runs_not_completes`).
* A **law of change** `f : S → A → S` read as a process (`ofMap f`) is determined, and a plan
  completes exactly when the goal holds at the configuration the law reaches
  (`completes_ofMap_iff`); for one move, exactly when it holds at `f s a`
  (`completes_ofMap_single`).
* A **partial law** `f : S → A → Option S` read as a process (`ofPartial f`) is determined; its
  traces are exactly the courses that `runPartial f` completes (`trace_ofPartial_iff`), and a
  plan completes exactly when that run ends in the goal (`completes_ofPartial_iff`).

No premise is added; every declaration has an empty axiom report.
-/

namespace Becoming

open Generative Generative.InquirySufficiency

universe u v

variable {S : Type u} {A : Type v}

namespace Assurance

/-- No safety condition. -/
def free : S → A → S → Prop := fun _ _ _ => True

/-- **Every completing plan runs, safely, into the goal.** Holds of every process. -/
theorem runs_of_completes {P : Process S A} {safe : S → A → S → Prop} {goal : S → Prop} {s : S}
    {plan : List A} (done : Completes P safe goal s plan) :
    (∃ t, Trace P s plan t) ∧ ∀ t, Trace P s plan t → SafeTrace P safe s plan t ∧ goal t :=
  match completes_has_actual_endpoint done with
  | ⟨t, path, _⟩ =>
    ⟨⟨t, path⟩, fun _ path' =>
      ⟨completes_all_actual_steps_safe done path', completes_every_actual_endpoint done path'⟩⟩

/-- The first step of a safe trace. -/
theorem safeTrace_head {P : Process S A} {safe : S → A → S → Prop} {s t : S} {a : A}
    {rest : List A} (st : SafeTrace P safe s (a :: rest) t) :
    ∃ m, P.step s a m ∧ safe s a m ∧ SafeTrace P safe m rest t := by
  cases st with
  | cons step condition tail => exact ⟨_, step, condition, tail⟩

/-- Under a determined process, a plan that runs safely into the goal completes. -/
theorem completes_of_runs {P : Process S A} (determined : Determined P)
    {safe : S → A → S → Prop} {goal : S → Prop} :
    ∀ {s : S} {plan : List A}, (∃ t, Trace P s plan t) →
      (∀ t, Trace P s plan t → SafeTrace P safe s plan t ∧ goal t) → Completes P safe goal s plan
  | _, [], ⟨_, path⟩, every => by
    cases path
    exact (every _ (.nil _)).2
  | s, a :: rest, ⟨t, path⟩, every => by
    cases path with
    | cons step tail =>
      refine ⟨⟨_, step⟩, fun m' step' => ?_⟩
      have same := determined s a _ m' step step'
      subst same
      refine ⟨?_, completes_of_runs determined ⟨t, tail⟩ fun t' tail' => ?_⟩
      · obtain ⟨m₀, step₀, condition, _⟩ := safeTrace_head (every t (.cons step tail)).1
        have again := determined s a m₀ _ step₀ step
        subst again
        exact condition
      · obtain ⟨safeTrace, reached⟩ := every t' (.cons step tail')
        obtain ⟨m₀, step₀, _, rest₀⟩ := safeTrace_head safeTrace
        have again := determined s a m₀ _ step₀ step
        subst again
        exact ⟨rest₀, reached⟩

/-- **For every determined process, a plan completes exactly when it runs, its run is safe and
its endpoint meets the goal.** -/
theorem completes_iff_of_determined {P : Process S A} (determined : Determined P)
    {safe : S → A → S → Prop} {goal : S → Prop} {s : S} {plan : List A} :
    Completes P safe goal s plan ↔
      (∃ t, Trace P s plan t) ∧ ∀ t, Trace P s plan t → SafeTrace P safe s plan t ∧ goal t :=
  ⟨runs_of_completes, fun ⟨runs, every⟩ => completes_of_runs determined runs every⟩

/-- Every trace is safe under no safety condition. -/
theorem safeTrace_free {P : Process S A} : ∀ {s t : S} {plan : List A},
    Trace P s plan t → SafeTrace P free s plan t
  | _, _, [], .nil _ => .nil _
  | _, _, _ :: _, .cons step tail => .cons step trivial (safeTrace_free tail)

/-- **With no safety condition, a plan of a determined process completes exactly when it runs
and every endpoint meets the goal.** -/
theorem completes_iff_runs {P : Process S A} (determined : Determined P) {goal : S → Prop}
    {s : S} {plan : List A} :
    Completes P free goal s plan ↔ (∃ t, Trace P s plan t) ∧ ∀ t, Trace P s plan t → goal t :=
  ⟨fun done => ⟨(runs_of_completes done).1, fun t path => ((runs_of_completes done).2 t path).2⟩,
   fun ⟨runs, every⟩ =>
    completes_of_runs determined runs fun t path => ⟨safeTrace_free path, every t path⟩⟩

/-! ## The converse needs determinacy -/

namespace Branch

/-- From `0` one move reaches `1` or `2`; from `1` it reaches `3`; from `2` nothing. -/
def process : Process Nat Unit :=
  ⟨fun s _ t => (s = 0 ∧ (t = 1 ∨ t = 2)) ∨ (s = 1 ∧ t = 3)⟩

theorem two_ne_zero : (2 : Nat) ≠ 0 := fun h => Nat.noConfusion h
theorem two_ne_one : (2 : Nat) ≠ 1 := fun h => Nat.noConfusion (Nat.succ.inj h)
theorem one_ne_zero : (1 : Nat) ≠ 0 := fun h => Nat.noConfusion h

/-- Nothing is possible from `2`. -/
theorem stuck (t : Nat) : ¬ process.step 2 () t
  | .inl ⟨at0, _⟩ => two_ne_zero at0
  | .inr ⟨at1, _⟩ => two_ne_one at1

/-- Every run of the two moves from `0` ends at `3`. -/
theorem ends_three : ∀ t, Trace process 0 [(), ()] t → t = 3 := by
  intro t path
  cases path with
  | cons first rest =>
    cases rest with
    | cons second last =>
      cases last
      rcases first with ⟨_, to1 | to2⟩ | ⟨at1, _⟩
      · subst to1
        rcases second with ⟨at0, _⟩ | ⟨_, to3⟩
        · exact absurd at0 one_ne_zero
        · exact to3
      · subst to2
        exact absurd second (stuck _)
      · exact absurd at1 (fun h => one_ne_zero h.symm)

/-- **The two moves run from `0` and every endpoint is `3`, yet the plan does not complete:**
the first move can reach `2`, where the second is impossible. -/
theorem runs_not_completes :
    ((∃ t, Trace process 0 [(), ()] t) ∧ ∀ t, Trace process 0 [(), ()] t → t = 3) ∧
      ¬ Completes process free (fun t => t = 3) 0 [(), ()] :=
  ⟨⟨⟨3, .cons (.inl ⟨rfl, .inl rfl⟩) (.cons (.inr ⟨rfl, rfl⟩) (.nil _))⟩, ends_three⟩,
   fun done => match (done.2 2 (.inl ⟨rfl, .inr rfl⟩)).2.1 with
     | ⟨t, step⟩ => stuck t step⟩

/-- The process is not determined. -/
theorem not_determined : ¬ Determined process :=
  fun determined => two_ne_one (determined 0 () 2 1 (.inl ⟨rfl, .inr rfl⟩) (.inl ⟨rfl, .inl rfl⟩))

end Branch

/-! ## Laws of change -/

/-- A law of change read as a process: the move `a` takes `s` to `f s a`. -/
def ofMap (f : S → A → S) : Process S A := ⟨fun s a t => t = f s a⟩

theorem ofMap_determined (f : S → A → S) : Determined (ofMap f) :=
  fun _ _ _ _ step step' => step.trans step'.symm

/-- **Under a law of change, a plan completes exactly when the goal holds where the law
takes the configuration.** -/
theorem completes_ofMap_iff (f : S → A → S) {goal : S → Prop} :
    ∀ (s : S) (plan : List A), Completes (ofMap f) free goal s plan ↔ goal (plan.foldl f s)
  | _, [] => Iff.rfl
  | s, a :: rest =>
    ⟨fun ⟨_, every⟩ => (completes_ofMap_iff f (f s a) rest).mp (every (f s a) rfl).2,
     fun held => ⟨⟨f s a, rfl⟩, fun t step => by
       have moved : t = f s a := step
       subst moved
       exact ⟨trivial, (completes_ofMap_iff f (f s a) rest).mpr held⟩⟩⟩

/-- **One move of a law of change secures a target exactly when the target holds at the
successor.** -/
theorem completes_ofMap_single (f : S → A → S) {goal : S → Prop} (s : S) (a : A) :
    Completes (ofMap f) free goal s [a] ↔ goal (f s a) :=
  completes_ofMap_iff f s [a]

/-! ## Partial laws -/

/-- A partial law read as a process: the move `a` takes `s` to `t` where `f s a = some t`. -/
def ofPartial (f : S → A → Option S) : Process S A := ⟨fun s a t => f s a = some t⟩

theorem ofPartial_determined (f : S → A → Option S) : Determined (ofPartial f) :=
  fun _ _ _ _ step step' => Option.some.inj (step.symm.trans step')

theorem none_ne_some {α : Type u} {x : α} : (none : Option α) ≠ some x :=
  fun same => nomatch same

/-- Running a partial law along a course; `none` where a move is impossible. -/
def runPartial (f : S → A → Option S) : S → List A → Option S
  | s, [] => some s
  | s, a :: rest => (f s a).bind fun t => runPartial f t rest

/-- **The traces of a partial law are exactly the courses its run completes.** -/
theorem trace_ofPartial_iff (f : S → A → Option S) :
    ∀ {s t : S} {plan : List A}, Trace (ofPartial f) s plan t ↔ runPartial f s plan = some t
  | s, t, [] =>
    ⟨fun path => match path with | .nil _ => rfl,
     fun ran => match (Option.some.inj ran : s = t) with | rfl => .nil s⟩
  | s, t, a :: rest =>
    ⟨fun path => match path with
      | .cons (m := m) step tail =>
        show (f s a).bind (fun u => runPartial f u rest) = some t from
          (congrArg (fun o => o.bind fun u => runPartial f u rest) step).trans
            ((trace_ofPartial_iff f).mp tail),
     fun ran =>
      match moved : f s a with
      | none => by
          have impossible : (f s a).bind (fun u => runPartial f u rest) = some t := ran
          rw [moved] at impossible
          exact absurd (show (none : Option S) = some t from impossible) none_ne_some
      | some m => by
          have onward : (f s a).bind (fun u => runPartial f u rest) = some t := ran
          rw [moved] at onward
          exact .cons moved ((trace_ofPartial_iff f).mpr onward)⟩

/-- **Under a partial law, a plan completes exactly when its run ends in the goal.** -/
theorem completes_ofPartial_iff (f : S → A → Option S) {goal : S → Prop} {s : S}
    {plan : List A} :
    Completes (ofPartial f) free goal s plan ↔ ∃ t, runPartial f s plan = some t ∧ goal t :=
  ⟨fun done =>
    match runs_of_completes done with
    | ⟨⟨t, path⟩, every⟩ => ⟨t, (trace_ofPartial_iff f).mp path, (every t path).2⟩,
   fun ⟨t, ran, reached⟩ =>
    (completes_iff_runs (ofPartial_determined f)).mpr
      ⟨⟨t, (trace_ofPartial_iff f).mpr ran⟩, fun t' path' =>
        have same : some t' = some t := ((trace_ofPartial_iff f).mp path').symm.trans ran
        (Option.some.inj same : t' = t) ▸ reached⟩⟩

end Assurance

end Becoming
