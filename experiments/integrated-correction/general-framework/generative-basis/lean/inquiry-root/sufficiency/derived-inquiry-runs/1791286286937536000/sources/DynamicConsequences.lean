import DynamicSymmetry

/-!
# Primitive laws, endpoint-sensitive traces, and feasible words

Pointwise equality of step permissions is equivalent to agreement on every
finite labelled trace with both endpoints retained. One-action traces recover
the primitive law. In contrast, forgetting endpoints can lose that distinction:
every total process permits every finite action word, and the existing static
and toggle laws disagree on endpoints despite identical word feasibility.

The counterexample is closed on the existing Bool/Unit models. The general
totality result retains its explicit hypothesis; this file does not assert that
all processes are total, recover erased information, or identify physical laws.
-/

namespace Generative.Deeper

universe u v

/-- Pointwise agreement on primitive steps, without equality of propositions. -/
def SameSteps {State : Type u} {Action : Type v}
    (P Q : Process State Action) : Prop :=
  ∀ s a t, P.step s a t ↔ Q.step s a t

theorem same_steps_iff_endpoint_traces
    {State : Type u} {Action : Type v} (P Q : Process State Action) :
    SameSteps P Q ↔
      ∀ s (word : List Action) t, Trace P s word t ↔ Trace Q s word t := by
  constructor
  · intro h s word t
    constructor
    · intro hp
      exact trace_map (P := P) (Q := Q) (f := fun x => x)
        (fun s a t hs => (h s a t).mp hs) hp
    · intro hq
      exact trace_map (P := Q) (Q := P) (f := fun x => x)
        (fun s a t hs => (h s a t).mpr hs) hq
  · intro h s a t
    constructor
    · intro hp
      exact trace_singleton_iff.mp
        ((h s [a] t).mp (trace_singleton_iff.mpr hp))
    · intro hq
      exact trace_singleton_iff.mp
        ((h s [a] t).mpr (trace_singleton_iff.mpr hq))

theorem same_steps_feasible_iff
    {State : Type u} {Action : Type v} {P Q : Process State Action}
    (h : SameSteps P Q) (s : State) (word : List Action) :
    Feasible P s word ↔ Feasible Q s word := by
  have htrace := (same_steps_iff_endpoint_traces P Q).mp h
  constructor
  · intro hp
    obtain ⟨t, ht⟩ := hp
    exact ⟨t, (htrace s word t).mp ht⟩
  · intro hq
    obtain ⟨t, ht⟩ := hq
    exact ⟨t, (htrace s word t).mpr ht⟩

/-- The hypothesis supplies each next step; finite induction constructs its trace. -/
theorem feasible_of_step_total
    {State : Type u} {Action : Type v} {P : Process State Action}
    (htotal : StepTotal P) (s : State) (word : List Action) :
    Feasible P s word := by
  induction word generalizing s with
  | nil => exact ⟨s, .nil s⟩
  | cons a word ih =>
    obtain ⟨t, hst⟩ := htotal s a
    obtain ⟨r, htr⟩ := ih t
    exact ⟨r, .cons hst htr⟩

theorem total_processes_same_feasible
    {State : Type u} {Action : Type v} {P Q : Process State Action}
    (hp : StepTotal P) (hq : StepTotal Q) (s : State) (word : List Action) :
    Feasible P s word ↔ Feasible Q s word := by
  constructor
  · intro _
    exact feasible_of_step_total hq s word
  · intro _
    exact feasible_of_step_total hp s word

theorem static_toggle_same_feasible (s : Bool) (word : List Unit) :
    Feasible static s word ↔ Feasible toggle s word :=
  total_processes_same_feasible static_total toggle_total s word

theorem static_toggle_singleton_endpoints_differ :
    Trace static false [()] false ∧ ¬ Trace toggle false [()] false := by
  constructor
  · exact trace_singleton_iff.mpr (static_event false)
  · intro h
    exact toggle_always_changes (trace_singleton_iff.mp h) rfl

theorem static_toggle_not_endpoint_trace_equivalent :
    ¬ (∀ s (word : List Unit) t,
      Trace static s word t ↔ Trace toggle s word t) := by
  intro h
  exact static_toggle_singleton_endpoints_differ.2
    ((h false [()] false).mp static_toggle_singleton_endpoints_differ.1)

theorem static_toggle_not_same_steps : ¬ SameSteps static toggle := by
  intro h
  exact static_toggle_not_endpoint_trace_equivalent
    ((same_steps_iff_endpoint_traces static toggle).mp h)

/-- Endpoint erasure hides a difference even between the existing symmetric laws. -/
theorem word_feasibility_does_not_determine_endpoints :
    (∀ s (word : List Unit), Feasible static s word ↔ Feasible toggle s word) ∧
      Trace static false [()] false ∧ ¬ Trace toggle false [()] false :=
  ⟨static_toggle_same_feasible, static_toggle_singleton_endpoints_differ⟩

end Generative.Deeper

#print axioms Generative.Deeper.same_steps_iff_endpoint_traces
#print axioms Generative.Deeper.same_steps_feasible_iff
#print axioms Generative.Deeper.feasible_of_step_total
#print axioms Generative.Deeper.total_processes_same_feasible
#print axioms Generative.Deeper.static_toggle_same_feasible
#print axioms Generative.Deeper.static_toggle_singleton_endpoints_differ
#print axioms Generative.Deeper.static_toggle_not_endpoint_trace_equivalent
#print axioms Generative.Deeper.static_toggle_not_same_steps
#print axioms Generative.Deeper.word_feasibility_does_not_determine_endpoints
