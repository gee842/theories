import ClosedLoopValuation -- 脊柱上 / On the spine (I4, 2026-10-16): `Becoming.Gated.kept_along`, `Becoming.Assurance.trace_ofPartial_iff` — 脊柱的律更一般 / the spine law is more general; MODULE-CLASSIFICATION.md
import FormationClosure

/-!
# Valuation development inside the generative core

`ValuationDevelopment` describes an organization by a selection law, a retention
law and a consequence law, and runs it along a list of presented conditions.
This module places every such organization inside the generative core: each one
induces a core `Process` whose finite `Trace`s are exactly its runs. The
valuation universals then become statements about core histories.

Under that embedding, the valuation package's "no retention, no history" result
and the formation law's "retained coordinate, constant law" result are one
theorem: if every step retains a coordinate and the selective disposition reads
only that coordinate, the disposition is the same after every history. History-
dependent valuation therefore requires a coordinate that the organization's own
activity changes. This is the general form of what the native port shows
concretely: its formation disposition develops because inquiry changes the
retained reading, while its contact class develops only through formation.
-/

namespace Generative.ValuationInCore

open Generative ValuationDevelopment FormationLaw

universe u

variable {M X A C : Type}

/-- The core process of an organization in a consequence law: one step per
presented condition, to the retained condition the encounter leaves. -/
def orgProcess (o : Org M X A C) (w : World X A C) : Process M X where
  step m x m' := m' = o.next w m x

theorem orgProcess_total (o : Org M X A C) (w : World X A C) (m : M) (x : X) :
    Enabled (orgProcess o w) m x :=
  ⟨o.next w m x, rfl⟩

/-- Core histories of the organization are exactly its runs. -/
theorem trace_iff_run (o : Org M X A C) (w : World X A C) (m m' : M) (xs : List X) :
    Trace (orgProcess o w) m xs m' ↔ o.run w m xs = m' := by
  induction xs generalizing m with
  | nil =>
    constructor
    · intro trace
      cases trace
      rfl
    · intro same
      cases same
      exact .nil m
  | cons x rest ih =>
    constructor
    · intro trace
      cases trace with
      | cons step tail =>
        cases step
        exact (ih _).mp tail
    · intro ran
      exact .cons rfl ((ih (o.next w m x)).mpr ran)

theorem run_is_trace (o : Org M X A C) (w : World X A C) (m : M) (xs : List X) :
    Trace (orgProcess o w) m xs (o.run w m xs) :=
  (trace_iff_run o w m _ xs).mpr rfl

/-- One theorem for both packages: a disposition that reads only a coordinate
every step retains is the same after every history. -/
theorem retained_disposition_constant {K : Type} (o : Org M X A C) (w : World X A C)
    (π : M → K) (retains : Retains (orgProcess o w) π)
    (reads : ∀ m m', π m = π m' → o.select m = o.select m') (m : M) (xs : List X) :
    o.select (o.run w m xs) = o.select m :=
  reads _ _ (trace_retains retains (run_is_trace o w m xs))

/-- Such an organization has no history-dependent valuation. -/
theorem retained_disposition_not_history_dependent {K : Type} (o : Org M X A C)
    (w : World X A C) (π : M → K) (retains : Retains (orgProcess o w) π)
    (reads : ∀ m m', π m = π m' → o.select m = o.select m') :
    ¬ historyDependent o w := by
  rintro ⟨m, xs, x, changed⟩
  exact changed (congrFun (retained_disposition_constant o w π retains reads m xs) x)

/-- History-dependent valuation needs a coordinate the organization's own activity
changes: no retained coordinate can carry the whole disposition. -/
theorem history_dependence_needs_changed_coordinate {K : Type} (o : Org M X A C)
    (w : World X A C) (dependent : historyDependent o w) (π : M → K)
    (reads : ∀ m m', π m = π m' → o.select m = o.select m') :
    ¬ Retains (orgProcess o w) π :=
  fun retains => retained_disposition_not_history_dependent o w π retains reads dependent

/-- The valuation package's own "no retention, no history" result is the case
in which the coordinate is the whole retained condition. -/
theorem no_retention_is_retained_identity (o : Org M X A C) (w : World X A C)
    (fixed : ∀ m x a c, o.retain m x a c = m) : Retains (orgProcess o w) id := by
  intro m x m' step
  cases step
  exact fixed _ _ _ _

end Generative.ValuationInCore

#print axioms Generative.ValuationInCore.orgProcess
#print axioms Generative.ValuationInCore.orgProcess_total
#print axioms Generative.ValuationInCore.trace_iff_run
#print axioms Generative.ValuationInCore.run_is_trace
#print axioms Generative.ValuationInCore.retained_disposition_constant
#print axioms Generative.ValuationInCore.retained_disposition_not_history_dependent
#print axioms Generative.ValuationInCore.history_dependence_needs_changed_coordinate
#print axioms Generative.ValuationInCore.no_retention_is_retained_identity
