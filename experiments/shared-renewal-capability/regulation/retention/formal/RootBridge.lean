import GenerativeCore
import Retention

/-!
The exact seven-event law is an instance of the repository's previously
checked relational generative core. No new causal or statistical assumption
is introduced by this transport.
-/

namespace EndogenousRetention

def rootProcess (k : Config) : Generative.Process State Event := ⟨Step k⟩

theorem trace_to_root {k : Config} {s t : State} {as : List Event}
    (h : Trace k s as t) : Generative.Trace (rootProcess k) s as t := by
  induction h with
  | nil => exact .nil _
  | cons hs _ ih => exact .cons hs ih

theorem trace_from_root {k : Config} {s t : State} {as : List Event}
    (h : Generative.Trace (rootProcess k) s as t) : Trace k s as t := by
  induction h with
  | nil => exact .nil _
  | cons hs _ ih => exact .cons hs ih

theorem trace_iff_root {k : Config} {s t : State} {as : List Event} :
    Trace k s as t ↔ Generative.Trace (rootProcess k) s as t :=
  ⟨trace_to_root, trace_from_root⟩

theorem root_trace_fuel_ledger {k : Config} {s t : State} {as : List Event}
    (h : Generative.Trace (rootProcess k) s as t) :
    t.f + t.e + spent as = s.f + s.e :=
  trace_fuel_ledger (trace_from_root h)

theorem root_trace_copy_budget {k : Config} {s t : State} {as : List Event}
    (h : Generative.Trace (rootProcess k) s as t) : copies as ≤ s.f + s.e :=
  trace_copy_budget (trace_from_root h)

theorem root_bootstrap_obstruction {k : Config} {s t : State} {as : List Event}
    (hc : s.c = 0) (hg : s.g = 0) (hf : s.f < 2)
    (h : Generative.Trace (rootProcess k) s as t) : t.c = 0 :=
  (bootstrap_under_two_fuel hc hg hf (trace_from_root h)).1

theorem root_witness_from_absence :
    Generative.Trace (rootProcess witnessConfig) initial witnessEvents finalState :=
  trace_to_root witness_from_absence

/-- Concatenation has exactly the same actual-state interface as the prior root. -/
theorem trace_append_iff {k : Config} {s t : State} {as bs : List Event} :
    Trace k s (as ++ bs) t ↔ ∃ u, Trace k s as u ∧ Trace k u bs t := by
  constructor
  · intro h
    obtain ⟨u, ha, hb⟩ := Generative.trace_append_iff.mp (trace_to_root h)
    exact ⟨u, trace_from_root ha, trace_from_root hb⟩
  · rintro ⟨u, ha, hb⟩
    exact trace_from_root (Generative.trace_append_iff.mpr
      ⟨u, trace_to_root ha, trace_to_root hb⟩)

#print axioms trace_to_root
#print axioms trace_from_root
#print axioms trace_iff_root
#print axioms root_trace_fuel_ledger
#print axioms root_trace_copy_budget
#print axioms root_bootstrap_obstruction
#print axioms root_witness_from_absence
#print axioms trace_append_iff

end EndogenousRetention
