import InquiryChoice

/-! Changing dependencies and the useful lifetime of an acquired description.
The inherited joint state is retained; dependency changes are explicit supplied
transitions. General error certificates and concrete charged histories have
separate scopes. -/
namespace ChangingDependency
noncomputable section
open ScaleRevision

/-- Errors in transported condition and anticipated loss both matter. -/
theorem forecast_error (a l recorded predicted α β : ℝ)
    (ha : |a-recorded| ≤ α) (hl : |l-predicted| ≤ β) :
    |(a-l)-(recorded-predicted)| ≤ α+β := by
  have h := abs_add_le (a-recorded) (predicted-l)
  rw [abs_sub_comm predicted l] at h
  have eq : (a-l)-(recorded-predicted) = (a-recorded)+(predicted-l) := by ring
  rw [eq]
  linarith

/-- Any finite sequence of stage errors has its stated cumulative bound. -/
theorem cumulative_error (actual predicted budget : Nat → ℝ)
    (h : ∀ i, |actual i-predicted i| ≤ budget i) (n : Nat) :
    |∑ i ∈ Finset.range n, (actual i-predicted i)| ≤ ∑ i ∈ Finset.range n, budget i := by
  calc
    _ ≤ ∑ i ∈ Finset.range n, |actual i-predicted i| := Finset.abs_sum_le_sum_abs _ _
    _ ≤ _ := Finset.sum_le_sum (fun i _ => h i)

/-- A bounded change after acquisition adds to the original sensor error. -/
theorem acquired_error_after_change (now sampled reading sensor driftBound : ℝ)
    (hchange : |now-sampled| ≤ driftBound) (hsensor : |sampled-reading| ≤ sensor) :
    |now-reading| ≤ sensor+driftBound := by
  have h := abs_add_le (now-sampled) (sampled-reading)
  have eq : now-reading = (now-sampled)+(sampled-reading) := by ring
  rw [eq]
  linarith

/-- At this finite horizon, per-stage loss bounds give a valid accumulated
interval even when the two losses differ. -/
theorem variable_two_stage_response (a lower upper S lo hi u l₁ l₂ : ℝ)
    (hr : InquiryChoice.robust a 2 lower upper S lo hi u)
    (h₁ : lo ≤ l₁ ∧ l₁ ≤ hi) (h₂ : lo ≤ l₂ ∧ l₂ ≤ hi) :
    0 ≤ u ∧ u ≤ S ∧ lower ≤ a-l₁-l₂+u ∧ a-l₁-l₂+u ≤ upper := by
  have h := hr ((l₁+l₂)/2) (by linarith [h₁.1,h₂.1]) (by linarith [h₁.2,h₂.2])
  dsimp [InquiryChoice.admissible,InquiryChoice.terminal] at h
  exact ⟨h.1,h.2.1,by linarith [h.2.2.1],by linarith [h.2.2.2]⟩

def certified (r E lower upper S u : ℝ) : Prop :=
  0 ≤ u ∧ u ≤ S ∧ lower ≤ r-E+u ∧ r+E+u ≤ upper

theorem certificate_transfers (r E lower upper S u actual : ℝ)
    (hc : certified r E lower upper S u) (he : |actual-r| ≤ E) :
    lower ≤ actual+u ∧ actual+u ≤ upper := by
  have h := abs_le.mp he
  dsimp [certified] at hc
  constructor <;> linarith [hc.2.2.1,hc.2.2.2]

theorem certificate_iff_interval (r E lower upper S u : ℝ) :
    certified r E lower upper S u ↔
      max 0 (lower-r+E) ≤ u ∧ u ≤ min S (upper-r-E) := by
  dsimp [certified]
  constructor
  · rintro ⟨hn,hs,hl,hu⟩
    exact ⟨max_le hn (by linarith),le_min hs (by linarith)⟩
  · rintro ⟨hlo,hhi⟩
    have l := max_le_iff.mp hlo
    have h := le_min_iff.mp hhi
    exact ⟨l.1,h.1,by linarith [l.2],by linarith [h.2]⟩

theorem uncertainty_requires_tolerance (r E lower upper S u : ℝ)
    (h : certified r E lower upper S u) : 2*E ≤ upper-lower := by
  dsimp [certified] at h
  linarith [h.2.2.1,h.2.2.2]

theorem smaller_error_preserves_certificate (r small large lower upper S u : ℝ)
    (horder : small ≤ large) (h : certified r large lower upper S u) :
    certified r small lower upper S u := by
  dsimp [certified] at *
  exact ⟨h.1,h.2.1,by linarith [h.2.2.1],by linarith [h.2.2.2]⟩

/-- This readout acquires the current condition as well as the decrement.
Two scalar channels, their exactness and one operation tariff are supplied. -/
def readBody (s : State) : State :=
  let t := probeBody {} s
  {t with view := {t.view with second := t.b, fine := true}}

def retainedCondition (s : State) : ℝ := s.view.total-s.view.second

def selectedDose (target horizon upperLoss : ℝ) (s : State) : ℝ :=
  max 0 (target-retainedCondition s+horizon*upperLoss)

inductive Event where
  | read | shift (newLoss : ℝ) | stale | bounded | refreshed | refreshedBound | wait

def advance (s : State) (e : Event) : State :=
  if s.stopped then s else
  match e with
  | .read => paid s readBody
  | .shift l => {s with b := l}
  | .stale => paid s (InquiryChoice.deliverBody (selectedDose 7 2 s.view.loss s))
  | .bounded => paid s (InquiryChoice.deliverBody (selectedDose 7 2 3 s))
  | .refreshed => paid s (InquiryChoice.deliverBody (selectedDose 7 1 s.view.loss s))
  | .refreshedBound => paid s (InquiryChoice.deliverBody (selectedDose 7 1 3 s))
  | .wait => drift s

def run (s : State) (es : List Event) : State := SystemsOrganization.evolve advance s es

def start : State := InquiryChoice.start 12 1 5 3132

def staleRoute : List Event := [.read,.shift 3,.stale,.wait]
def boundedRoute : List Event := [.read,.shift 3,.bounded,.wait]
def refreshRoute : List Event := [.read,.shift 3,.read,.refreshed]

theorem read_obtains_condition_and_loss (s : State) :
    retainedCondition (readBody s) = (readBody s).a ∧
    (readBody s).view.loss = loss s := by
  dsimp [retainedCondition,readBody,probeBody,total,drift]
  constructor <;> ring

theorem run_is_core_trace (s : State) (es : List Event) :
    Generative.Trace (SystemsOrganization.deterministic advance) s es (run s es) :=
  (SystemsOrganization.deterministic_trace_iff _ _ _ _).mpr rfl

theorem changed_dependency_keeps_timestamp (s : State) (l : ℝ)
    (h : s.stopped = false) :
    (advance s (.shift l)).stage = s.stage ∧
    (advance s (.shift l)).view = s.view := by simp [advance,h]

theorem run_work_conserved (s : State) (es : List Event) :
    workTotal (run s es) = workTotal s := by
  have one : ∀ s e, workTotal (advance s e) = workTotal s := by
    intro s e
    cases e <;> simp only [advance] <;> split
    all_goals first | rfl | exact paid_work_conserved s _ (fun _ => rfl) |
      exact paid_work_conserved s _ (InquiryChoice.deliver_work_conserved _)
  induction es generalizing s with
  | nil => rfl
  | cons e es ih => exact (ih (advance s e)).trans (one s e)

set_option maxRecDepth 32768
set_option maxHeartbeats 4000000

theorem current_stamp_can_have_wrong_forecast :
    let s := run start [.read,.shift 3]
    s.view.atStage = s.stage ∧ forecast s.view = 10 ∧ s.a-loss s = 8 := by
  norm_num [run,start,InquiryChoice.start,SystemsOrganization.evolve,advance,paid,
    RemainingDependency.charge,RemainingDependency.tariff,readBody,probeBody,total,drift,loss,forecast]

theorem stale_response_misses_target :
    let s := run start staleRoute
    s.a = 5 ∧ s.stage = 3 ∧ s.delivered = 0 ∧ s.source = 5 ∧ s.account.spent = 2088 := by
  norm_num [run,start,InquiryChoice.start,staleRoute,SystemsOrganization.evolve,advance,paid,
    RemainingDependency.charge,RemainingDependency.tariff,readBody,probeBody,total,drift,loss,
    InquiryChoice.deliverBody,selectedDose,retainedCondition]

theorem bounded_response_meets_target :
    let s := run start boundedRoute
    s.a = 7 ∧ s.stage = 3 ∧ s.delivered = 2 ∧ s.source = 3 ∧ s.account.spent = 2088 := by
  norm_num [run,start,InquiryChoice.start,boundedRoute,SystemsOrganization.evolve,advance,paid,
    RemainingDependency.charge,RemainingDependency.tariff,readBody,probeBody,total,drift,loss,
    InquiryChoice.deliverBody,selectedDose,retainedCondition]

theorem bounded_response_covers_variable_losses :
    ∀ l₁ l₂ : ℝ, 1 ≤ l₁ → l₁ ≤ 3 → 1 ≤ l₂ → l₂ ≤ 3 →
      7 ≤ 11-l₁-l₂+2 ∧ 11-l₁-l₂+2 ≤ 11 := by
  intro l₁ l₂ h₁ h₂ h₃ h₄
  constructor <;> linarith

theorem refresh_meets_same_horizon :
    let s := run start refreshRoute
    s.a = 7 ∧ s.stage = 3 ∧ s.delivered = 2 ∧ s.source = 3 ∧ s.account.spent = 3132 := by
  norm_num [run,start,InquiryChoice.start,refreshRoute,SystemsOrganization.evolve,advance,paid,
    RemainingDependency.charge,RemainingDependency.tariff,readBody,probeBody,total,drift,loss,
    InquiryChoice.deliverBody,selectedDose,retainedCondition]

theorem refresh_is_useful_when_loss_stays_low :
    let s := run start [.read,.shift 1,.read,.refreshed]
    s.a = 9 ∧ s.delivered = 0 ∧ s.source = 5 ∧ s.stage = 3 := by
  norm_num [run,start,InquiryChoice.start,SystemsOrganization.evolve,advance,paid,
    RemainingDependency.charge,RemainingDependency.tariff,readBody,probeBody,total,drift,loss,
    InquiryChoice.deliverBody,selectedDose,retainedCondition]

theorem changed_reading_can_still_meet_target :
    let s := run start [.read,.shift 1,.read,.shift 3,.refreshed]
    s.a = 7 ∧ s.delivered = 0 ∧ s.view.loss = 1 := by
  norm_num [run,start,InquiryChoice.start,SystemsOrganization.evolve,advance,paid,
    RemainingDependency.charge,RemainingDependency.tariff,readBody,probeBody,total,drift,loss,
    InquiryChoice.deliverBody,selectedDose,retainedCondition]

/-- A larger subsequent change actually breaks the lower target. -/
theorem unbounded_change_defeats_refresh :
    let s := run start [.read,.shift 1,.read,.shift 4,.refreshed]
    s.a = 6 ∧ s.delivered = 0 ∧ s.view.loss = 1 ∧ s.stage = 3 := by
  norm_num [run,start,InquiryChoice.start,SystemsOrganization.evolve,advance,paid,
    RemainingDependency.charge,RemainingDependency.tariff,readBody,probeBody,total,drift,loss,
    InquiryChoice.deliverBody,selectedDose,retainedCondition]

theorem narrow_tolerance_defeats_old_bound :
    ¬ ∃ u, 0 ≤ u ∧ u ≤ 5 ∧ 7 ≤ 11-3-3+u ∧ 11-1-1+u ≤ 9 := by
  rintro ⟨u,_,_,hlo,hhi⟩
  linarith

/-- A second change within [1,3] defeats a freshly acquired intermediate reading. -/
theorem within_bound_change_defeats_exact_refresh :
    let s := run start [.read,.shift 2,.read,.shift 3,.refreshed]
    s.a = 6 ∧ s.delivered = 0 ∧ s.view.loss = 2 ∧ s.stage = 3 := by
  norm_num [run,start,InquiryChoice.start,SystemsOrganization.evolve,advance,paid,
    RemainingDependency.charge,RemainingDependency.tariff,readBody,probeBody,total,drift,loss,
    InquiryChoice.deliverBody,selectedDose,retainedCondition]

/-- A necessary deadline for this symmetric uncertainty certificate; actual
source or sign constraints can cause loss of certification earlier. -/
theorem error_growth_budget (r sensor rate age lower upper S u : ℝ)
    (h : certified r (sensor+rate*age) lower upper S u) :
    2*rate*age ≤ upper-lower-2*sensor := by
  have hwidth := uncertainty_requires_tolerance r (sensor+rate*age) lower upper S u h
  nlinarith

/-- Reacquisition followed by a bound on subsequent change covers every pair
of losses in [1,3], not only the endpoint examples. -/
theorem bounded_refresh_covers_variable_losses (first second : ℝ)
    (hfirst : 1 ≤ first ∧ first ≤ 3) (hsecond : 1 ≤ second ∧ second ≤ 3) :
    let u := max 0 (7-(11-first)+3)
    0 ≤ u ∧ u ≤ 5 ∧ 7 ≤ 11-first-second+u ∧ 11-first-second+u ≤ 9 := by
  have h : 0 ≤ 7-(11-first)+3 := by linarith [hfirst.1]
  dsimp only
  rw [max_eq_right h]
  exact ⟨h,by linarith [hfirst.2],by linarith [hsecond.2],by linarith [hsecond.1]⟩

theorem bounded_refresh_repairs_actual_failure :
    let s := run start [.read,.shift 2,.read,.shift 3,.refreshedBound]
    s.a = 7 ∧ s.delivered = 1 ∧ s.source = 4 ∧ s.stage = 3 ∧
      s.account.spent = 3132 := by
  norm_num [run,start,InquiryChoice.start,SystemsOrganization.evolve,advance,paid,
    RemainingDependency.charge,RemainingDependency.tariff,readBody,probeBody,total,drift,loss,
    InquiryChoice.deliverBody,selectedDose,retainedCondition]

end
end ChangingDependency

#print axioms ChangingDependency.forecast_error
#print axioms ChangingDependency.cumulative_error
#print axioms ChangingDependency.acquired_error_after_change
#print axioms ChangingDependency.variable_two_stage_response
#print axioms ChangingDependency.certificate_transfers
#print axioms ChangingDependency.certificate_iff_interval
#print axioms ChangingDependency.uncertainty_requires_tolerance
#print axioms ChangingDependency.smaller_error_preserves_certificate
#print axioms ChangingDependency.read_obtains_condition_and_loss
#print axioms ChangingDependency.run_is_core_trace
#print axioms ChangingDependency.changed_dependency_keeps_timestamp
#print axioms ChangingDependency.run_work_conserved
#print axioms ChangingDependency.current_stamp_can_have_wrong_forecast
#print axioms ChangingDependency.stale_response_misses_target
#print axioms ChangingDependency.bounded_response_meets_target
#print axioms ChangingDependency.bounded_response_covers_variable_losses
#print axioms ChangingDependency.refresh_meets_same_horizon
#print axioms ChangingDependency.refresh_is_useful_when_loss_stays_low
#print axioms ChangingDependency.changed_reading_can_still_meet_target
#print axioms ChangingDependency.unbounded_change_defeats_refresh
#print axioms ChangingDependency.narrow_tolerance_defeats_old_bound
#print axioms ChangingDependency.within_bound_change_defeats_exact_refresh
#print axioms ChangingDependency.error_growth_budget
#print axioms ChangingDependency.bounded_refresh_covers_variable_losses
#print axioms ChangingDependency.bounded_refresh_repairs_actual_failure
