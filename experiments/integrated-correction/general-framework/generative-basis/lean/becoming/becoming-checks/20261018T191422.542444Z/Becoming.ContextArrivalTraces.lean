import Becoming.Context

/-!
# Arrival in a context along traces of the evolving law

`Becoming.Context` keeps a context beside the configuration and lets both change by one joint
relation (`evolvingLaw R`, a process on context and configuration). Which contexts support an
endpoint is derived from the common history: `Arrives R initial s word t j` holds where a trace of
`evolvingLaw R` from an initial context and `s` reaches context `j` at `t`, and one step of it is
`Advance` (`arrives_singleton`). This module states its step laws of those traces.

* **A step from a supported context arrives**: a step of the evolving law from a context in the
  support is a one-step trace arriving at its target context (`step_arrives`).
* **No support, no arrival**: from an empty support no one-step trace arrives
  (`empty_support_no_arrival`).
* **A context changes with the step**: in `ChangingContext.relation`, the one-step trace from
  context `false` at 0 arrives at 1 in the different context `true` (`changed_context_arrives`).

`BecomingCompatibility` states these of its `evolving`, `Arrives`, `Advance` and
`changingRelation`, which are the core's by definition (`Becoming.Bridge`, `…_by_core`); its
`empty_support_cannot_advance`, `actual_step_supplies_advance` and `changed_context_is_formed`
are these laws' one-step forms. This module imports nothing outside the core. No ethical
predicate, ranking or axiom occurs.
-/

namespace Becoming

namespace ContextArrivalTraces

open Generative

universe u v w

variable {I : Type u} {S : Type v} {A : Type w}

/-- **A step of the evolving law from a supported context arrives at its target context.** -/
theorem step_arrives (R : I → S → A → I → S → Prop) {possible : I → Prop} {i j : I} {s t : S}
    {a : A} (supported : possible i) (step : (evolvingLaw R).step (i, s) a (j, t)) :
    Arrives R possible s [a] t j :=
  arrives_singleton.mpr ⟨i, supported, step⟩

/-- **From an empty support no one-step trace of the evolving law arrives.** -/
theorem empty_support_no_arrival (R : I → S → A → I → S → Prop) (s : S) (a : A) (t : S) (j : I) :
    ¬ Arrives R (fun _ => False) s [a] t j :=
  fun ⟨_, unsupported, _⟩ => unsupported

/-- **The context changes with the step**: the one-step trace of `ChangingContext.relation` from
context `false` at 0 arrives at 1 in context `true`, which differs from `false`. -/
theorem changed_context_arrives :
    Arrives ChangingContext.relation (fun i => i = false) 0 [()] 1 true ∧ (true : Bool) ≠ false :=
  ⟨step_arrives ChangingContext.relation rfl (Or.inl ⟨rfl, rfl, rfl, rfl⟩),
   fun same => Bool.noConfusion same⟩

end ContextArrivalTraces

end Becoming
