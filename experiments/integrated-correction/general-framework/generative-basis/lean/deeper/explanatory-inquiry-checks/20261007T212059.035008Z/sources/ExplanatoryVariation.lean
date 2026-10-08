import ExplanatoryNecessity

/-! Identification by available conjunction tests, followed by an actual
support-consuming gate-release history. Tests are not assumed physically free.
All results are relative to the declared interface and laws. -/
namespace Generative.ExplanatoryVariation

universe u v
variable {I : Type u} {Q : Type v}

def Response (active : Q → I → Prop) (value : I → Prop) (q : Q) : Prop :=
  ∀ i, active q i → value i

def Isolates (active : Q → I → Prop) (i : I) : Prop :=
  ∃ q, active q i ∧ ∀ j, active q j → j = i

def WitnessRecovery (active : Q → I → Prop) (i : I) : Prop :=
  ∀ value, value i ↔ ∃ q, active q i ∧ Response active value q

def Identifies (active : Q → I → Prop) (i : I) : Prop :=
  ∀ value other, (∀ q, Response active value q ↔ Response active other q) →
    (value i ↔ other i)

theorem witness_recovery_iff_isolation (active : Q → I → Prop) (i : I) :
    WitnessRecovery active i ↔ Isolates active i := by
  constructor
  · intro h
    obtain ⟨q, hqi, hresp⟩ := (h (fun j => j = i)).mp rfl
    exact ⟨q, hqi, hresp⟩
  · rintro ⟨q, hqi, hiso⟩ value
    constructor
    · intro hi
      exact ⟨q, hqi, fun j hj => (hiso j hj).symm ▸ hi⟩
    · rintro ⟨r, hri, hresp⟩
      exact hresp i hri

theorem isolation_implies_identification {active : Q → I → Prop} {i : I}
    (h : Isolates active i) : Identifies active i := by
  have hr := (witness_recovery_iff_isolation active i).mpr h
  intro value other he
  constructor
  · intro hi
    obtain ⟨q, hqi, hresp⟩ := (hr value).mp hi
    exact ((he q).mp hresp) i hqi
  · intro hi
    obtain ⟨q, hqi, hresp⟩ := (hr other).mp hi
    exact ((he q).mpr hresp) i hqi

theorem absent_isolation_profiles_agree {active : Q → I → Prop} {i : I}
    (h : ¬ Isolates active i) (q : Q) :
    Response active (fun j => j = i) q ↔ Response active (fun _ => False) q := by
  constructor
  · intro hr j hj
    have heq := hr j hj
    subst j
    exact h ⟨q, hj, hr⟩
  · intro hr j hj
    exact (hr j hj).elim

theorem absent_isolation_prevents_identification {active : Q → I → Prop} {i : I}
    (h : ¬ Isolates active i) : ¬ Identifies active i := by
  intro hi
  exact (hi (fun j => j = i) (fun _ => False)
    (absent_isolation_profiles_agree h)).mp rfl

theorem isolated_factor_transport {active : Q → I → Prop} {i : I}
    (h : Isolates active i) {value other : I → Prop}
    (he : ∀ q, Response active value q ↔ Response active other q) :
    value i ↔ other i := isolation_implies_identification h value other he

theorem all_responses_iff_all_factors {active : Q → I → Prop}
    (h : ∀ i, Isolates active i) (value other : I → Prop) :
    (∀ q, Response active value q ↔ Response active other q) ↔
      (∀ i, value i ↔ other i) := by
  constructor
  · intro he i
    exact isolated_factor_transport (h i) he
  · intro he q
    constructor
    · intro hr i hi
      exact (he i).mp (hr i hi)
    · intro hr i hi
      exact (he i).mpr (hr i hi)

def together : Unit → Bool → Prop := fun _ _ => True
def separate : Bool → Bool → Prop := fun q i => i = q

theorem together_has_no_isolation (i : Bool) : ¬ Isolates together i := by
  rintro ⟨q, _, h⟩
  have hfalse := h false True.intro
  have htrue := h true True.intro
  have bad : false = true := hfalse.trans htrue.symm
  cases bad

theorem separate_isolates (i : Bool) : Isolates separate i :=
  ⟨i, rfl, fun _ h => h⟩

theorem together_cannot_identify (i : Bool) : ¬ Identifies together i :=
  absent_isolation_prevents_identification (together_has_no_isolation i)

theorem separate_identifies (i : Bool) : Identifies separate i :=
  isolation_implies_identification (separate_isolates i)

/-- One relational configuration includes the two gates, release support and
the effect of passage. No independent observer or external intervention exists
as a primitive in this process. -/
structure GateState where
  leftOpen : Bool
  rightOpen : Bool
  support : Bool
  passed : Bool

inductive Event where
  | releaseLeft | releaseRight | pass

inductive GateStep : GateState → Event → GateState → Prop where
  | releaseLeft (l r d : Bool) :
      GateStep ⟨l, r, true, d⟩ .releaseLeft ⟨true, r, false, d⟩
  | releaseRight (l r d : Bool) :
      GateStep ⟨l, r, true, d⟩ .releaseRight ⟨l, true, false, d⟩
  | pass (c : Bool) :
      GateStep ⟨true, true, c, false⟩ .pass ⟨true, true, c, true⟩

def gates : Process GateState Event where
  step := GateStep

def leftBlocked : GateState := ⟨false, true, true, false⟩
def rightBlocked : GateState := ⟨true, false, true, false⟩
def passedState : GateState := ⟨true, true, false, true⟩

theorem initial_pass_blocked_left : ¬ Enabled gates leftBlocked .pass := by
  rintro ⟨t, h⟩
  cases h

theorem initial_pass_blocked_right : ¬ Enabled gates rightBlocked .pass := by
  rintro ⟨t, h⟩
  cases h

theorem release_left_then_pass :
    Trace gates leftBlocked [.releaseLeft, .pass] passedState :=
  .cons (.releaseLeft false true false) (.cons (.pass false) (.nil passedState))

theorem release_right_then_pass :
    Trace gates rightBlocked [.releaseRight, .pass] passedState :=
  .cons (.releaseRight true false false) (.cons (.pass false) (.nil passedState))

theorem release_left_wrong_gate_fails :
    ¬ Feasible gates rightBlocked [.releaseLeft, .pass] := by
  rintro ⟨t, h⟩
  obtain ⟨m, hrelease, htail⟩ := trace_cons_iff.mp h
  cases hrelease
  have hpass := trace_singleton_iff.mp htail
  cases hpass

theorem release_right_wrong_gate_fails :
    ¬ Feasible gates leftBlocked [.releaseRight, .pass] := by
  rintro ⟨t, h⟩
  obtain ⟨m, hrelease, htail⟩ := trace_cons_iff.mp h
  cases hrelease
  have hpass := trace_singleton_iff.mp htail
  cases hpass

theorem release_unavailable_without_support (l r d : Bool) :
    ¬ Enabled gates ⟨l, r, false, d⟩ .releaseLeft ∧
    ¬ Enabled gates ⟨l, r, false, d⟩ .releaseRight := by
  constructor <;> rintro ⟨t, h⟩ <;> cases h

theorem release_consumes_support {s t : GateState} {e : Event}
    (he : e = .releaseLeft ∨ e = .releaseRight) (h : gates.step s e t) :
    s.support = true ∧ t.support = false := by
  cases h with
  | releaseLeft => exact ⟨rfl, rfl⟩
  | releaseRight => exact ⟨rfl, rfl⟩
  | pass => rcases he with h | h <;> cases h

def TwoClosedInvariant (s : GateState) : Prop :=
  (s.support = true → s.leftOpen = false ∧ s.rightOpen = false) ∧
  (s.leftOpen = false ∨ s.rightOpen = false)

theorem two_closed_invariant_step {s t : GateState} {e : Event}
    (hi : TwoClosedInvariant s) (hs : gates.step s e t) : TwoClosedInvariant t := by
  cases hs with
  | releaseLeft l r d =>
    constructor
    · intro h
      cases h
    · exact Or.inr (hi.1 rfl).2
  | releaseRight l r d =>
    constructor
    · intro h
      cases h
    · exact Or.inl (hi.1 rfl).1
  | pass c =>
    rcases hi.2 with h | h <;> cases h

theorem two_closed_invariant_trace {s t : GateState} {word : List Event}
    (hi : TwoClosedInvariant s) (ht : Trace gates s word t) : TwoClosedInvariant t := by
  induction ht with
  | nil => exact hi
  | cons hs _ ih => exact ih (two_closed_invariant_step hi hs)

theorem one_support_cannot_open_two_closed {word : List Event} {t : GateState}
    (h : Trace gates ⟨false, false, true, false⟩ word t) :
    ¬ (t.leftOpen = true ∧ t.rightOpen = true) := by
  have hi := two_closed_invariant_trace (s := ⟨false, false, true, false⟩)
    ⟨fun _ => ⟨rfl, rfl⟩, Or.inl rfl⟩ h
  rintro ⟨hl, hr⟩
  rcases hi.2 with hf | hf
  · have bad : true = false := hl.symm.trans hf
    cases bad
  · have bad : true = false := hr.symm.trans hf
    cases bad

theorem variation_requires_description_difference
    {E : Type u} {encode : GateState → E}
    {predict : E → List Event → Prop}
    (h : ∀ s word, predict (encode s) word ↔ Feasible gates s word) :
    encode leftBlocked ≠ encode rightBlocked := by
  intro he
  have hp := (h leftBlocked [.releaseLeft, .pass]).mpr ⟨passedState, release_left_then_pass⟩
  rw [he] at hp
  exact release_left_wrong_gate_fails ((h rightBlocked [.releaseLeft, .pass]).mp hp)

theorem pass_feasible_iff (l r c : Bool) :
    Feasible gates ⟨l, r, c, false⟩ [.pass] ↔ l = true ∧ r = true := by
  constructor
  · rintro ⟨t, h⟩
    have hs := trace_singleton_iff.mp h
    cases hs
    exact ⟨rfl, rfl⟩
  · rintro ⟨rfl, rfl⟩
    exact ⟨_, .cons (.pass c) (.nil _)⟩

theorem release_left_feasible_iff (l r : Bool) :
    Feasible gates ⟨l, r, true, false⟩ [.releaseLeft, .pass] ↔ r = true := by
  constructor
  · rintro ⟨t, h⟩
    obtain ⟨m, hs, ht⟩ := trace_cons_iff.mp h
    cases hs
    have hp := trace_singleton_iff.mp ht
    cases hp
    rfl
  · intro h
    subst r
    exact ⟨passedState, .cons (.releaseLeft l true false)
      (.cons (.pass false) (.nil _))⟩

theorem release_right_feasible_iff (l r : Bool) :
    Feasible gates ⟨l, r, true, false⟩ [.releaseRight, .pass] ↔ l = true := by
  constructor
  · rintro ⟨t, h⟩
    obtain ⟨m, hs, ht⟩ := trace_cons_iff.mp h
    cases hs
    have hp := trace_singleton_iff.mp ht
    cases hp
    rfl
  · intro h
    subst l
    exact ⟨passedState, .cons (.releaseRight true r false)
      (.cons (.pass false) (.nil _))⟩

def gateValue (l r i : Bool) : Prop := if i then r = true else l = true
def probeWord (i : Bool) : List Event :=
  if i then [.releaseLeft, .pass] else [.releaseRight, .pass]

theorem probe_matches_response (l r i : Bool) :
    Feasible gates ⟨l, r, true, false⟩ (probeWord i) ↔
      Response separate (gateValue l r) i := by
  have hr : Response separate (gateValue l r) i ↔ gateValue l r i := by
    constructor
    · intro h
      exact h i rfl
    · intro h j hj
      exact hj.symm ▸ h
  apply Iff.trans ?_ hr.symm
  cases i with
  | false => exact release_right_feasible_iff l r
  | true => exact release_left_feasible_iff l r

theorem support_not_restored_step {s t : GateState} {e : Event}
    (h : s.support = false) (hs : gates.step s e t) : t.support = false := by
  cases hs with
  | releaseLeft => cases h
  | releaseRight => cases h
  | pass => exact h

theorem support_not_restored_trace {s t : GateState} {word : List Event}
    (h : s.support = false) (ht : Trace gates s word t) : t.support = false := by
  induction ht with
  | nil => exact h
  | cons hs _ ih => exact ih (support_not_restored_step h hs)

theorem spent_support_prevents_future_release {s t : GateState} {word : List Event}
    (h : s.support = false) (ht : Trace gates s word t) :
    ¬ Enabled gates t .releaseLeft ∧ ¬ Enabled gates t .releaseRight := by
  have hc := support_not_restored_trace h ht
  cases t with
  | mk l r c d =>
    cases c with
    | false => exact release_unavailable_without_support l r d
    | true => cases hc

theorem unsupported_probe_infeasible (l r i : Bool) :
    ¬ Feasible gates ⟨l, r, false, false⟩ (probeWord i) := by
  intro h
  cases i <;> obtain ⟨t, ht⟩ := h <;>
    obtain ⟨m, hs, _⟩ := trace_cons_iff.mp ht <;> cases hs

/-- Restricting admissible valuations by a warranted coupling changes what is
identifiable. The unrestricted isolation requirement is not universal physics. -/
theorem coupled_response_recovers (value : Bool → Prop)
    (hc : value false ↔ value true) : Response together value () ↔ value false := by
  constructor
  · intro h
    exact h false True.intro
  · intro h i _
    cases i with
    | false => exact h
    | true => exact hc.mp h

theorem coupled_identification_without_isolation (value other : Bool → Prop)
    (hv : value false ↔ value true) (hw : other false ↔ other true)
    (he : Response together value () ↔ Response together other ()) :
    (value false ↔ other false) ∧ ¬ Isolates together false := by
  exact ⟨(coupled_response_recovers value hv).symm.trans
    (he.trans (coupled_response_recovers other hw)), together_has_no_isolation false⟩

theorem release_left_erases_old_left (r d : Bool) :
    gates.step ⟨false, r, true, d⟩ .releaseLeft ⟨true, r, false, d⟩ ∧
    gates.step ⟨true, r, true, d⟩ .releaseLeft ⟨true, r, false, d⟩ :=
  ⟨.releaseLeft false r d, .releaseLeft true r d⟩

theorem already_open_probe_also_succeeds :
    Trace gates ⟨true, true, true, false⟩ [.releaseLeft, .pass] passedState :=
  .cons (.releaseLeft true true false) (.cons (.pass false) (.nil passedState))

theorem original_left_from_completed_probe_impossible :
    ¬ ∃ read : GateState → Prop, ∀ s t,
      Trace gates s [.releaseLeft, .pass] t → (read t ↔ s.leftOpen = true) := by
  rintro ⟨read, h⟩
  have hp := (h ⟨true, true, true, false⟩ passedState already_open_probe_also_succeeds).mpr rfl
  have bad : false = true := (h leftBlocked passedState release_left_then_pass).mp hp
  cases bad

end Generative.ExplanatoryVariation

#print axioms Generative.ExplanatoryVariation.witness_recovery_iff_isolation
#print axioms Generative.ExplanatoryVariation.isolation_implies_identification
#print axioms Generative.ExplanatoryVariation.absent_isolation_profiles_agree
#print axioms Generative.ExplanatoryVariation.absent_isolation_prevents_identification
#print axioms Generative.ExplanatoryVariation.isolated_factor_transport
#print axioms Generative.ExplanatoryVariation.all_responses_iff_all_factors
#print axioms Generative.ExplanatoryVariation.together_has_no_isolation
#print axioms Generative.ExplanatoryVariation.separate_isolates
#print axioms Generative.ExplanatoryVariation.together_cannot_identify
#print axioms Generative.ExplanatoryVariation.separate_identifies
#print axioms Generative.ExplanatoryVariation.initial_pass_blocked_left
#print axioms Generative.ExplanatoryVariation.initial_pass_blocked_right
#print axioms Generative.ExplanatoryVariation.release_left_then_pass
#print axioms Generative.ExplanatoryVariation.release_right_then_pass
#print axioms Generative.ExplanatoryVariation.release_left_wrong_gate_fails
#print axioms Generative.ExplanatoryVariation.release_right_wrong_gate_fails
#print axioms Generative.ExplanatoryVariation.release_unavailable_without_support
#print axioms Generative.ExplanatoryVariation.release_consumes_support
#print axioms Generative.ExplanatoryVariation.two_closed_invariant_step
#print axioms Generative.ExplanatoryVariation.two_closed_invariant_trace
#print axioms Generative.ExplanatoryVariation.one_support_cannot_open_two_closed
#print axioms Generative.ExplanatoryVariation.variation_requires_description_difference
#print axioms Generative.ExplanatoryVariation.pass_feasible_iff
#print axioms Generative.ExplanatoryVariation.release_left_feasible_iff
#print axioms Generative.ExplanatoryVariation.release_right_feasible_iff
#print axioms Generative.ExplanatoryVariation.probe_matches_response
#print axioms Generative.ExplanatoryVariation.support_not_restored_step
#print axioms Generative.ExplanatoryVariation.support_not_restored_trace
#print axioms Generative.ExplanatoryVariation.spent_support_prevents_future_release
#print axioms Generative.ExplanatoryVariation.unsupported_probe_infeasible

#print axioms Generative.ExplanatoryVariation.coupled_response_recovers
#print axioms Generative.ExplanatoryVariation.coupled_identification_without_isolation
#print axioms Generative.ExplanatoryVariation.release_left_erases_old_left
#print axioms Generative.ExplanatoryVariation.already_open_probe_also_succeeds
#print axioms Generative.ExplanatoryVariation.original_left_from_completed_probe_impossible
