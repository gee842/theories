import Becoming.Courses

/-!
# Lasting and reaching on runs and courses

`Becoming.Lasting` states lasting a number of steps, exhaustion, never reaching and reaching for a
law of change under admissible disturbances, on its histories, and for a determined law on its
orbit; `Becoming.Viability` states where no course leaves a guard. The law under disturbances is
a process of the spine (`Viability.disturbed`): every run of it is the admissible history of its
moves (`Courses.run_history`, `Courses.run_admissible`) and every admissible history is a run
(`Courses.historyRun`). A determined law is a process too (`Law.process`), whose runs are its
orbits (`Branching.law_run_state`) and whose courses end on them (`Courses.trace_orbit`,
`Courses.orbit_trace`); every sequence is a run of the process in which every change is admitted
(`Courses.anyRun`). `Becoming.Courses` states the laws of lasting on courses; this module states
the rest on runs and courses, with no premise beyond what each theorem names.

* **Lasting on runs.** Given one admissible disturbance, a start lasts `n` steps exactly when
  every run of the disturbed process from it stays within the guard for its first `n` steps
  (`lasts_iff_runs`). On runs from within the guard, the guarded history of the run's moves agrees
  with the run at `n` exactly when the run stays within the guard up to `n` (`guarded_upto_iff`),
  and stops exactly when it does not (`guarded_none_iff`). A family that is a ladder and necessary
  is exactly what every course keeps within the guard (`courses_iff_of_exact`), and, given one
  admissible disturbance, a drained family holds every start whose courses stay within the guard
  (`drained_of_courses`). Being at a level of a drained family does not suffice: in `Collapse` a
  course of one disturbance leaves the guard from a start at level one (`collapse_leaves`).
* **The worst growth on runs.** Every run whose growth a monotone map bounds, from a start at or
  below `v`, stays at or below `θ` for its first `n` steps exactly when every run of the map's own
  process from `v` does (`stays_below_iff`).
* **Reaching on runs.** Given one admissible disturbance and a decided target, a start reaches the
  target within `n` steps exactly when every run of the disturbed process from it meets the target
  within `n` steps (`reaches_iff_runs`); so a family that is a funnel and a basin is exactly what
  meets the target on every run (`runs_iff_of_exact`). Reaching composes on runs
  (`reaches_trans_runs`). The direction from runs to reaching needs a decision: for the `Search`
  law it gives the limited principle of omniscience (`search_runs_need_decision`).
* **A determined law on its courses.** Lasting `n` steps is staying within the guard on every
  course of at most `n` moves of the law's process (`determined_lasts_iff_courses`); with a decided
  target, a course of at most `n` moves reaches it exactly when not every such course stays outside
  it (`reaches_iff_not_lasts_courses`), and without the decision that duality would eliminate
  double negation (`dual_needs_decision_courses`); a numeric variant for every course into a
  target would decide equality (`numeric_needs_decision_courses`). Reaching the target along
  courses from every seed rules out a closed set avoiding it that holds a seed
  (`reaches_excludes_courses`).
* **The admissible disturbance is needed.** With no admissible disturbance the disturbed process
  has no run, so every condition on its runs holds, while no configuration is in the kernel of the
  empty guard (`needs_admissible_runs`).

No ethical predicate, ranking or axiom occurs.
-/

namespace Becoming

open Generative Viability

universe u v w

namespace LastingRuns

/-! ## Lasting on runs of the disturbed process -/

section Disturbed

variable {S : Type u} {A : Type v} {f : S → A → S} {adm : A → Prop} {guard : S → Prop}

/-- A run of the disturbed process from `s` is the admissible history of its moves from `s`. -/
theorem run_history_from (r : Run (disturbed f adm)) {s : S} (start : r.state 0 = s) (k : Nat) :
    r.state k = history f s r.act k :=
  (Courses.run_history r k).trans (congrArg (fun x => history f x r.act k) start)

/-- **Lasting on runs.** Given one admissible disturbance, a start lasts `n` steps exactly when
every run of the disturbed process from it stays within the guard for its first `n` steps. -/
theorem lasts_iff_runs {a₀ : A} (h₀ : adm a₀) {n : Nat} {s : S} :
    Lasting.Lasts f adm guard n s ↔
      ∀ r : Run (disturbed f adm), r.state 0 = s → ∀ k, k ≤ n → guard (r.state k) :=
  (Lasting.lasts_iff_histories h₀).trans
    ⟨fun every r start k bound =>
      Eq.mpr (congrArg guard (run_history_from r start k))
        (every r.act (Courses.run_admissible r) k bound),
     fun every d admissible k bound => every (Courses.historyRun s d admissible) rfl k bound⟩

/-- **The guarded history of a run agrees with it exactly where it stays within the guard.** From
within the guard, the guarded history of a run's moves is the run's configuration at `n` exactly
when the run stays within the guard up to `n`. -/
theorem guarded_upto_iff [DecidablePred guard] (r : Run (disturbed f adm))
    (start : guard (r.state 0)) {n : Nat} :
    guardedHistory f guard (r.state 0) r.act n = some (r.state n) ↔
      ∀ k, k ≤ n → guard (r.state k) :=
  ⟨fun agree k bound => Eq.mpr (congrArg guard (Courses.run_history r k))
      ((Lasting.guarded_upto_iff start).mp
        (agree.trans (congrArg some (Courses.run_history r n))) k bound),
   fun within => ((Lasting.guarded_upto_iff start).mpr fun k bound =>
      Eq.mp (congrArg guard (Courses.run_history r k)) (within k bound)).trans
        (congrArg some (Courses.run_history r n)).symm⟩

/-- **The guarded history of a run stops exactly where the run leaves the guard.** From within the
guard, the guarded history of a run's moves stops by `n` exactly when the run leaves the guard by
`n`. -/
theorem guarded_none_iff [DecidablePred guard] (r : Run (disturbed f adm))
    (start : guard (r.state 0)) {n : Nat} :
    guardedHistory f guard (r.state 0) r.act n = none ↔ ¬ ∀ k, k ≤ n → guard (r.state k) :=
  (Lasting.guarded_none_iff start).trans
    ⟨fun leaves within => leaves fun k bound =>
        Eq.mp (congrArg guard (Courses.run_history r k)) (within k bound),
     fun leaves within => leaves fun k bound =>
        Eq.mpr (congrArg guard (Courses.run_history r k)) (within k bound)⟩

/-- **A family that is a ladder and necessary is exactly what every course keeps within the
guard.** -/
theorem courses_iff_of_exact {C : Nat → S → Prop} (ladder : Lasting.Ladder f adm guard C)
    (necessary : Lasting.Necessary f adm guard C) (n : Nat) (s : S) :
    (∀ plan t, Trace (disturbed f adm) s plan t → plan.length ≤ n → guard t) ↔ C n s :=
  Courses.lasts_iff_courses.symm.trans (Lasting.lasts_iff_of_exact ladder necessary n s)

/-- **A drained family holds what every course keeps within the guard**, given one admissible
disturbance. -/
theorem drained_of_courses {L : Nat → S → Prop} (drains : Lasting.Drains f adm guard L) {a₀ : A}
    (h₀ : adm a₀) {n : Nat} {s : S}
    (every : ∀ plan t, Trace (disturbed f adm) s plan t → plan.length ≤ n → guard t) : L n s :=
  Lasting.Necessary.of_lasts (Lasting.Drains.necessary drains h₀) n s
    (Courses.lasts_iff_courses.mpr every)

end Disturbed

/-- **Being at a level does not suffice, on courses.** In `Collapse`, the family "is `true`" is
drained for the guard "is `true`" and holds `true` at level `1`, yet some course of at most one
disturbance from `true` leaves the guard. -/
theorem collapse_leaves :
    Lasting.Drains Lasting.Collapse.step (fun _ => True) (fun b => b = true) (fun _ b => b = true) ∧
      ¬ ∀ plan t, Trace (disturbed Lasting.Collapse.step (fun _ => True)) true plan t →
        plan.length ≤ 1 → t = true :=
  ⟨Lasting.Collapse.level_not_lasting.1,
   fun every => Lasting.Collapse.level_not_lasting.2.2 (Courses.lasts_iff_courses.mpr every)⟩

/-! ## The worst growth on runs -/

section Growth

variable {V : Type w} {rel : V → V → Prop} {g : V → V}

/-- **The orbit is the worst growth, on runs.** Every run (of the process in which every change is
admitted) starting at or below `v` whose growth `g` bounds stays at or below `θ` for its first `n`
steps exactly when every run of the process of `g` from `v` does. -/
theorem stays_below_iff (refl : ∀ a, rel a a) (trans : ∀ a b c, rel a b → rel b c → rel a c)
    (mono : ∀ a b, rel a b → rel (g a) (g b)) {v θ : V} {n : Nat} :
    (∀ r : Run (Courses.anyChange V), rel (r.state 0) v →
        (∀ k, rel (r.state (k + 1)) (g (r.state k))) → ∀ k, k ≤ n → rel (r.state k) θ) ↔
      ∀ r : Run (Law.process g), r.state 0 = v → ∀ k, k ≤ n → rel (r.state k) θ :=
  have worst := Lasting.stays_below_iff refl trans mono (v := v) (θ := θ) (n := n)
  ⟨fun every r start k bound =>
    Eq.mpr (congrArg (fun y => rel y θ)
        ((Branching.law_run_state r k).trans (congrArg (fun x => Law.orbit g x k) start)))
      (worst.mp (fun x below grows => every (Courses.anyRun x) below grows) k bound),
   fun every r below grows => worst.mpr (every (Law.run g v) rfl) r.state below grows⟩

end Growth

/-! ## Reaching on runs of the disturbed process -/

section Reaching

variable {S : Type u} {A : Type v} {f : S → A → S} {adm : A → Prop} {target : S → Prop}

/-- **Reaching on runs.** Given one admissible disturbance and a decided target, a start reaches
the target within `n` steps exactly when every run of the disturbed process from it meets the
target within `n` steps. -/
theorem reaches_iff_runs [DecidablePred target] {a₀ : A} (h₀ : adm a₀) {n : Nat} {s : S} :
    Lasting.Reaches f adm target n s ↔
      ∀ r : Run (disturbed f adm), r.state 0 = s → ∃ k, k ≤ n ∧ target (r.state k) :=
  (Lasting.reaches_iff_histories h₀).trans
    ⟨fun every r start => match every r.act (Courses.run_admissible r) with
      | ⟨k, bound, inside⟩ =>
        ⟨k, bound, Eq.mpr (congrArg target (run_history_from r start k)) inside⟩,
     fun every d admissible => every (Courses.historyRun s d admissible) rfl⟩

/-- **A family that is a funnel and a basin is exactly what meets the target on every run**, given
one admissible disturbance and a decided target. -/
theorem runs_iff_of_exact [DecidablePred target] {a₀ : A} (h₀ : adm a₀) {C : Nat → S → Prop}
    (funnel : Lasting.Funnel f adm target C) (basin : Lasting.Basin f adm target C) (n : Nat)
    (s : S) :
    (∀ r : Run (disturbed f adm), r.state 0 = s → ∃ k, k ≤ n ∧ target (r.state k)) ↔ C n s :=
  (reaches_iff_runs h₀).symm.trans (Lasting.reaches_iff_of_exact funnel basin n s)

/-- **Reaching composes on runs.** Where every configuration of a region reaches the target within
`k` steps and a run begins at a configuration reaching the region within `m`, the run meets the
target within `k + m` steps. -/
theorem reaches_trans_runs {B : S → Prop} {k m : Nat}
    (onward : ∀ x, B x → Lasting.Reaches f adm target k x) (r : Run (disturbed f adm))
    (reaches : Lasting.Reaches f adm B m (r.state 0)) :
    ∃ j, j ≤ k + m ∧ target (r.state j) :=
  Courses.Reaches.runs r (Lasting.Reaches.trans onward reaches)

end Reaching

/-- **Reaching from runs needs a decision.** If, for the `Search` law, meeting the target within
one step on every run of its disturbed process from before the choice gave reaching it, the
limited principle of omniscience would hold. -/
theorem search_runs_need_decision
    (converse : ∀ g : Nat → Bool,
      (∀ r : Run (disturbed Lasting.Search.step (fun _ => True)), r.state 0 = none →
          ∃ k, k ≤ 1 ∧ Lasting.Search.found g (r.state k)) →
        Lasting.Reaches Lasting.Search.step (fun _ => True) (Lasting.Search.found g) 1 none)
    (g : Nat → Bool) : (∃ b, g b = true) ∨ ∀ a, g a = false :=
  Lasting.Search.histories_need_decision
    (fun g every => converse g fun r start =>
      match every r.act (Courses.run_admissible r) with
      | ⟨k, bound, inside⟩ =>
        ⟨k, bound, Eq.mpr (congrArg (Lasting.Search.found g) (run_history_from r start k)) inside⟩)
    g

/-! ## A determined law on its courses -/

section Determined

variable {S : Type u} {next : S → S}

/-- **For a determined law, lasting is staying within the guard on every course of its
process**: a start lasts `n` steps exactly when every course of at most `n` moves of the law's
process from it ends within the guard. -/
theorem determined_lasts_iff_courses {guard : S → Prop} {n : Nat} {s : S} :
    Lasting.Lasts (Lasting.determined next) (fun _ => True) guard n s ↔
      ∀ plan t, Trace (Law.process next) s plan t → plan.length ≤ n → guard t :=
  (Lasting.lasts_iff_histories (a₀ := ()) trivial).trans
    ⟨fun every _ _ path bound =>
      Eq.mpr (congrArg guard
          ((Courses.trace_orbit path).trans (Lasting.orbit_eq_history next s (fun _ => ()) _)))
        (every (fun _ => ()) (fun _ => trivial) _ bound),
     fun every d _ k bound =>
      Eq.mpr (congrArg guard (Lasting.orbit_eq_history next s d k).symm)
        (every _ _ (Courses.orbit_trace next k s)
          (Eq.mpr (congrArg (· ≤ n) (Courses.length_units k)) bound))⟩

/-- **For a determined law and a decided target, a course reaches the target exactly where not
every course stays outside it**: some course of at most `n` moves of the law's process ends in the
target exactly when not every such course ends outside it. -/
theorem reaches_iff_not_lasts_courses {target : S → Prop} [DecidablePred target] {n : Nat}
    {s : S} :
    (∃ plan t, Trace (Law.process next) s plan t ∧ plan.length ≤ n ∧ target t) ↔
      ¬ ∀ plan t, Trace (Law.process next) s plan t → plan.length ≤ n → ¬ target t :=
  Courses.course_reaches_iff_orbit.trans (Lasting.reaches_iff_orbit.symm.trans
    (Lasting.reaches_iff_not_lasts.trans
      ⟨fun not_lasts every => not_lasts (determined_lasts_iff_courses.mpr every),
       fun not_every lasts => not_every (determined_lasts_iff_courses.mp lasts)⟩))

/-- **The duality on courses needs a decision.** If, for every target, not every course of no
moves staying outside it gave a course of no moves into it, double negation would be
eliminated. -/
theorem dual_needs_decision_courses {s : S}
    (dual : ∀ target : S → Prop,
      ¬ (∀ plan t, Trace (Law.process next) s plan t → plan.length ≤ 0 → ¬ target t) →
        ∃ plan t, Trace (Law.process next) s plan t ∧ plan.length ≤ 0 ∧ target t)
    (p : Prop) : ¬ ¬ p → p :=
  Lasting.dual_needs_decision (next := next) (s := s)
    (fun target not_lasts =>
      match dual target (fun every => not_lasts (every [] s (.nil s) (Nat.le_refl 0))) with
      | ⟨[], _, .nil _, _, inside⟩ => inside
      | ⟨_ :: _, _, _, bound, _⟩ => absurd bound (Nat.not_succ_le_zero _))
    p

/-- **The numeric form on courses needs a decision.** If every course of a determined law's
process into a target within `n` moves gave a numeric variant at most `n` at the start, equality
of configurations would be decided. -/
theorem numeric_needs_decision_courses
    (numeric : ∀ (next : S → S) (target : S → Prop) (n : Nat) (s : S),
      (∃ plan t, Trace (Law.process next) s plan t ∧ plan.length ≤ n ∧ target t) →
        ∃ V : S → Nat, V s ≤ n ∧ ∀ x, V x ≤ n → target x ∨ V (next x) < V x)
    (x y : S) : x = y ∨ ¬ x = y :=
  Lasting.numeric_needs_decision
    (fun next target n s found => numeric next target n s (Courses.course_reaches_iff_orbit.mpr found))
    x y

/-- **Reaching from every seed along courses rules out a closed set avoiding the target that holds
a seed.** -/
theorem reaches_excludes_courses {target seed : S → Prop}
    (reaches : ∀ s, seed s → ∃ t, Reach (Law.process next) s t ∧ target t) :
    ¬ ∃ K : S → Prop, (∃ s, seed s ∧ K s) ∧ (∀ x, K x → ¬ target x) ∧
      ∀ x, K x → K (next x) :=
  Lasting.reaches_excludes fun s seeded => match reaches s seeded with
    | ⟨_, reach, inside⟩ => match Courses.reach_iff_orbit.mp reach with
      | ⟨n, at_n⟩ => ⟨n, Eq.mpr (congrArg target at_n) inside⟩

end Determined

/-! ## The admissible disturbance is needed -/

/-- **Without an admissible disturbance, conditions on runs constrain nothing.** The process that
keeps the one configuration under disturbances none of which is admissible has no run, so every
run of it stays within the empty guard, while the configuration is not in the kernel of the empty
guard. -/
theorem needs_admissible_runs :
    (∀ r : Run (disturbed (fun (s : Unit) (_ : Unit) => s) (fun _ => False)), ∀ n,
        (fun _ : Unit => False) (r.state n)) ∧
      ¬ Kernel (disturbed (fun (s : Unit) (_ : Unit) => s) (fun _ => False)) (fun _ => False) () :=
  ⟨fun r => Viability.needs_admissible.1 r.act (Courses.run_admissible r),
   fun kept => Viability.needs_admissible.2 (match kernel_iff_certificate.mp kept with
    | ⟨K, held, cert⟩ =>
      ⟨K, held, (certificate_disturbed_iff.mp cert).1, (certificate_disturbed_iff.mp cert).2⟩)⟩

end LastingRuns

end Becoming
