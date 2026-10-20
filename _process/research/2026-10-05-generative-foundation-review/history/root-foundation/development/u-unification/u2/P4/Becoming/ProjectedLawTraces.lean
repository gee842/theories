import Becoming.Mechanism
import SystemsOrganization

/-!
# Projected laws on the traces of deterministic processes

`SystemsOrganization` states, for every deterministic action law `next : S → A → S`, when a
projection `p : S → Q` commutes with a reduced law (`Commuting`), and gives finite examples of
local copy cells under two wirings and of a device formed inside one law. Its process
`SystemsOrganization.deterministic next` admits exactly the steps of `next`, and its traces are
exactly the evaluations of `next` along a word (`SystemsOrganization.deterministic_trace_iff`).
This module reads the module's notions on that process and states its results of its traces,
proved through the module's theorems.

* **A reduced law is a process the step factors through.** A projection commutes with a reduced
  law exactly where the step of the process factors through it into the reduced process
  (`commuting_iff_factors`), and its fibres are consistent exactly where configurations alike
  under it go alike (`fibre_iff_goAlike`, `Becoming.Mechanism`'s `GoAlike`).
* **Exactly where it maps every trace.** A projection commutes with a reduced law exactly where it
  takes every trace of the process to a trace of the reduced process with the same word
  (`commuting_iff_traces`); such projections compose (`traces_compose`), and two component
  equations of the actual law carry every trace to a trace of the coupled law
  (`coupled_trace`).
* **Same cells, different recurrence.** Under the straight wiring the copy cells rest at
  `(true, false)`; under the crossed wiring they do not rest there and return after two steps
  (`wiring_recurrence`). Under the crossed wiring configurations alike in their left cell do not
  go alike (`left_not_goAlike`), so no determined process on the left cell admits the steps read
  through it (`left_carries_no_law`, through `Becoming.Mechanism.carries_law_iff`).
* **Formation draws on the spare and the fuel**: every assembly step from the raw device reaches
  a device without the spare and without fuel (`assembly_draws`).

No ethical predicate, ranking or axiom occurs.
-/

namespace Becoming

open Generative

namespace ProjectedLawTraces

open SystemsOrganization

universe u v w z

variable {S : Type u} {Q : Type v} {R : Type w} {A : Type z}

/-! ## A reduced law as a process -/

/-- **A projection commutes with a reduced law exactly where the step factors through it** into
the reduced process. -/
theorem commuting_iff_factors {next : S → A → S} {reduced : Q → A → Q} {p : S → Q} :
    Commuting next reduced p ↔ FactorsThrough (deterministic next) p (deterministic reduced) :=
  ⟨fun commutes s a _ step => (congrArg p step).trans (commutes s a),
   fun factors s a => factors s a (next s a) rfl⟩

/-- **The fibres of a projection are consistent exactly where configurations alike under it go
alike** under the process. -/
theorem fibre_iff_goAlike {next : S → A → S} {p : S → Q} :
    FibreConsistent next p ↔ GoAlike (deterministic next) p :=
  ⟨fun consistent s s' a _ _ same step step' =>
      (congrArg p step).trans ((consistent s s' same a).trans (congrArg p step').symm),
   fun alike s s' same a => alike s s' a (next s a) (next s' a) same rfl rfl⟩

/-! ## Traces -/

/-- **A projection commutes with a reduced law exactly where it takes every trace of the process
to a trace of the reduced process** with the same word. -/
theorem commuting_iff_traces {next : S → A → S} {reduced : Q → A → Q} {p : S → Q} :
    Commuting next reduced p ↔
      ∀ s word t, Trace (deterministic next) s word t →
        Trace (deterministic reduced) (p s) word (p t) :=
  ⟨fun commutes s word t path =>
     (deterministic_trace_iff reduced (p s) (p t) word).mpr
       ((congrArg p ((deterministic_trace_iff next s t word).mp path)).trans
         (commuting_iff_all_words.mp commutes s word)),
   fun carries => commuting_iff_all_words.mpr fun s word =>
     (deterministic_trace_iff reduced (p s) _ word).mp
       (carries s word _ ((deterministic_trace_iff next s _ word).mpr rfl))⟩

/-- **Projections carrying every trace compose.** -/
theorem traces_compose {next : S → A → S} {middle : Q → A → Q} {last : R → A → R}
    {p : S → Q} {q : Q → R}
    (hp : ∀ s word t, Trace (deterministic next) s word t →
      Trace (deterministic middle) (p s) word (p t))
    (hq : ∀ s word t, Trace (deterministic middle) s word t →
      Trace (deterministic last) (q s) word (q t)) :
    ∀ s word t, Trace (deterministic next) s word t →
      Trace (deterministic last) (q (p s)) word (q (p t)) :=
  commuting_iff_traces.mp
    (commuting_composes (commuting_iff_traces.mpr hp) (commuting_iff_traces.mpr hq))

/-- **Two component equations of the actual law carry every trace to a trace of the coupled
law**, the components of each configuration together. -/
theorem coupled_trace {next : S → A → S} (p : S → Q) (q : S → R)
    (left : Q → R → A → Q) (right : Q → R → A → R)
    (hp : ∀ s a, p (next s a) = left (p s) (q s) a)
    (hq : ∀ s a, q (next s a) = right (p s) (q s) a)
    {s t : S} {word : List A} (path : Trace (deterministic next) s word t) :
    Trace (deterministic (coupledNext left right)) (p s, q s) word (p t, q t) :=
  (deterministic_trace_iff (coupledNext left right) (p s, q s) (p t, q t) word).mpr
    ((congrArg (fun x => (p x, q x)) ((deterministic_trace_iff next s t word).mp path)).trans
      (coupled_components_preserve_history p q left right hp hq s word))

/-! ## Same cells, different wiring -/

/-- **Same cells, different recurrence.** Under the straight wiring the copy cells rest at
`(true, false)`; under the crossed wiring they do not rest there and return after two steps. -/
theorem wiring_recurrence :
    Trace (deterministic (routed false)) (true, false) [()] (true, false) ∧
      ¬ Trace (deterministic (routed true)) (true, false) [()] (true, false) ∧
      Trace (deterministic (routed true)) (true, false) [(), ()] (true, false) :=
  ⟨(deterministic_trace_iff (routed false) _ _ [()]).mpr
      same_cells_different_collective_recurrence.1.symm,
   fun path => same_cells_different_collective_recurrence.2.1
      ((deterministic_trace_iff (routed true) _ _ [()]).mp path).symm,
   (deterministic_trace_iff (routed true) _ _ [(), ()]).mpr
      same_cells_different_collective_recurrence.2.2.symm⟩

/-- **Under the crossed wiring, configurations alike in their left cell do not go alike.** -/
theorem left_not_goAlike : ¬ GoAlike (deterministic (routed true)) (fun s => s.1) :=
  fun alike => no_autonomous_left_law
    ((reduced_law_exists_iff (routed true) (fun s => s.1) (fun x => (x, false)) fun _ => rfl).mpr
      (fibre_iff_goAlike.mpr alike))

/-- **No determined process on the left cell admits the steps of the crossed wiring read through
it.** -/
theorem left_carries_no_law :
    ¬ ∃ P : Process Bool Unit, Determined P ∧
      FactorsThrough (deterministic (routed true)) (fun s => s.1) P :=
  fun found => left_not_goAlike (carries_law_iff.mp found)

/-! ## Formation inside one law -/

/-- **Formation draws on the spare and the fuel**: every assembly step from the raw device reaches
a device without the spare and without fuel. -/
theorem assembly_draws {t : Device} (step : organization.step raw .assemble t) :
    raw.spare = true ∧ t.spare = false ∧ raw.fuel = 1 ∧ t.fuel = 0 :=
  Eq.subst (motive := fun x => raw.spare = true ∧ x.spare = false ∧ raw.fuel = 1 ∧ x.fuel = 0)
    step.2.2.2.symm formation_consumes_spare_and_fuel

end ProjectedLawTraces

end Becoming
