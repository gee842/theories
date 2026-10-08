import ScaleRevision

/-! Inquiry and immediate response compared at a common horizon. All record,
condition, support and work changes occur within the inherited joint state.
The local constant-loss and additive-response laws remain explicit inputs. -/
namespace InquiryChoice
noncomputable section
open ScaleRevision

def terminal (a H l u : ℝ) : ℝ := a - H*l + u
def admissible (a H lower upper S l u : ℝ) : Prop :=
  0 ≤ u ∧ u ≤ S ∧ lower ≤ terminal a H l u ∧ terminal a H l u ≤ upper

def robust (a H lower upper S lo hi u : ℝ) : Prop :=
  ∀ l, lo ≤ l → l ≤ hi → admissible a H lower upper S l u

def leastDose (a H lower hi : ℝ) : ℝ := max 0 (lower-a+H*hi)
def mostDose (a H upper S lo : ℝ) : ℝ := min S (upper-a+H*lo)

theorem robust_iff_interval (a H lower upper S lo hi u : ℝ)
    (hH : 0 ≤ H) (horder : lo ≤ hi) :
    robust a H lower upper S lo hi u ↔
      leastDose a H lower hi ≤ u ∧ u ≤ mostDose a H upper S lo := by
  constructor
  · intro h
    have hh := h hi horder le_rfl
    have hl := h lo le_rfl horder
    dsimp [admissible, terminal] at hh hl
    dsimp [leastDose, mostDose]
    exact ⟨max_le hh.1 (by linarith [hh.2.2.1]), le_min hh.2.1 (by linarith [hl.2.2.2])⟩
  · rintro ⟨hmin, hmax⟩ l hlo hhi
    have hm := max_le_iff.mp hmin
    have hx := le_min_iff.mp hmax
    have hmullo := mul_le_mul_of_nonneg_left hlo hH
    have hmulhi := mul_le_mul_of_nonneg_left hhi hH
    dsimp [admissible, terminal]
    exact ⟨hm.1, hx.1, by linarith [hm.2], by linarith [hx.2]⟩

theorem robust_exists_iff (a H lower upper S lo hi : ℝ)
    (hH : 0 ≤ H) (horder : lo ≤ hi) :
    (∃ u, robust a H lower upper S lo hi u) ↔
      leastDose a H lower hi ≤ mostDose a H upper S lo := by
  constructor
  · rintro ⟨u, hu⟩
    have h := (robust_iff_interval a H lower upper S lo hi u hH horder).mp hu
    exact h.1.trans h.2
  · intro h
    exact ⟨_, (robust_iff_interval a H lower upper S lo hi _ hH horder).mpr ⟨le_rfl,h⟩⟩

theorem minimal_robust_dose (a H lower upper S lo hi u : ℝ)
    (hH : 0 ≤ H) (horder : lo ≤ hi)
    (hu : robust a H lower upper S lo hi u) : leastDose a H lower hi ≤ u :=
  ((robust_iff_interval a H lower upper S lo hi u hH horder).mp hu).1

/-- A uniform response cannot distinguish histories giving the same observation. -/
theorem indistinguishable_conflict {X O U : Type} (obs : X → O)
    (allowed : X → U → Prop) (x y : X) (same : obs x = obs y)
    (conflict : ∀ u, ¬ (allowed x u ∧ allowed y u)) :
    ¬ ∃ policy : O → U, ∀ z, allowed z (policy (obs z)) := by
  rintro ⟨policy, good⟩
  exact conflict (policy (obs x)) ⟨good x, by simpa only [same] using good y⟩

/-- Each observed class must have a common action. Existence is not an
algorithm or a claim that class membership/calibration is acquired for free. -/
theorem observed_class_policy_iff {X O U : Type} [Nonempty U]
    (obs : X → O) (allowed : X → U → Prop) :
    (∃ policy : O → U, ∀ x, allowed x (policy (obs x))) ↔
      ∀ o, ∃ u, ∀ x, obs x = o → allowed x u := by
  constructor
  · rintro ⟨policy, good⟩ o
    exact ⟨policy o, fun x h => by simpa only [h] using good x⟩
  · intro h
    classical
    choose policy good using h
    exact ⟨policy, fun x => good (obs x) x rfl⟩

/-- With nonnegative loss, the end of an unassisted wait is its lowest level. -/
theorem waiting_floor (a l d floor : ℝ) (hl : 0 ≤ l)
    (h : floor ≤ a-d*l) : ∀ t, 0 ≤ t → t ≤ d → floor ≤ a-t*l := by
  intro t _ ht
  have hm := mul_le_mul_of_nonneg_right ht hl
  linarith

theorem early_support_dominates_before_delivery (a l u t : ℝ) (hu : 0 ≤ u) :
    a-t*l ≤ a-t*l+u := by linarith

theorem same_horizon_same_dose (a l u : ℝ) :
    (a-l+u)-l = (a-l)-l+u := by ring

/-- A source-bounded additive response, retaining the prior work charger. -/
def deliverBody (u : ℝ) (s : State) : State :=
  if 0 ≤ u ∧ u ≤ s.source then
    {s with a := s.a - loss s + u, source := s.source - u, stage := s.stage + 1, delivered := s.delivered + u}
  else {drift s with stopped := true}

inductive Event where
  | sense | give (u : ℝ) | respond | wait

def advance (knownInitial target : ℝ) (s : State) : Event → State
  | .sense => if s.stopped then s else paid s (probeBody {})
  | .give u => if s.stopped then s else paid s (deliverBody u)
  | .respond => if s.stopped then s else
      paid s (deliverBody (max 0 (target-knownInitial+2*s.view.loss)))
  | .wait => if s.stopped then s else drift s

def run (knownInitial target : ℝ) (s : State) (es : List Event) : State :=
  SystemsOrganization.evolve (advance knownInitial target) s es

def start (a l S : ℝ) (fuel : Nat := 2088) : State :=
  { a := a, b := l, source := S, coupled := true,
    account := {fuel := fuel, live := 8, peak := 10, capacity := 32} }

def immediate (u : ℝ) : List Event := [.give u, .wait]
def inquire : List Event := [.sense, .respond]

def chooseRoute (a lower upper S lo hi : ℝ) (fuel : Nat) : List Event :=
  if leastDose a 2 lower hi ≤ mostDose a 2 upper S lo then
    immediate (leastDose a 2 lower hi)
  else if 2088 ≤ fuel ∧ 0 ≤ a-hi then inquire else []

theorem run_is_core_trace (a target : ℝ) (s : State) (es : List Event) :
    Generative.Trace (SystemsOrganization.deterministic (advance a target)) s es
      (run a target s es) :=
  (SystemsOrganization.deterministic_trace_iff _ _ _ _).mpr rfl

theorem deliver_work_conserved (u : ℝ) (s : State) :
    workTotal (deliverBody u s) = workTotal s := by
  unfold deliverBody
  split <;> rfl

theorem run_work_conserved (a target : ℝ) (s : State) (es : List Event) :
    workTotal (run a target s es) = workTotal s := by
  have one : ∀ s e, workTotal (advance a target s e) = workTotal s := by
    intro s e
    cases e <;> simp only [advance] <;> split
    all_goals first | rfl | exact paid_work_conserved s _ (fun t => rfl) |
      exact paid_work_conserved s _ (deliver_work_conserved _)
  induction es generalizing s with
  | nil => rfl
  | cons e es ih => exact (ih (advance a target s e)).trans (one s e)

theorem two_losses_have_no_common_immediate_dose :
    ¬ ∃ u, admissible 8 2 7 8 5 1 u ∧ admissible 8 2 7 8 5 3 u := by
  rintro ⟨u,h1,h3⟩
  dsimp [admissible,terminal] at h1 h3
  linarith [h1.2.2.2,h3.2.2.1]

-- One compiled definition unfolding set is shared by exact witnesses below.
set_option maxRecDepth 32768
set_option maxHeartbeats 4000000

theorem low_loss_inquiry :
    let s := run 8 7 (start 8 1 5) inquire
    s.a = 7 ∧ s.source = 4 ∧ s.delivered = 1 ∧ s.stage = 2 ∧
      s.account.spent = 2088 ∧ s.stopped = false := by
  norm_num [run, inquire, SystemsOrganization.evolve, advance, start, paid,
    RemainingDependency.charge, RemainingDependency.tariff, probeBody, drift,
    loss, total, deliverBody]

theorem high_loss_inquiry :
    let s := run 8 7 (start 8 3 5) inquire
    s.a = 7 ∧ s.source = 0 ∧ s.delivered = 5 ∧ s.stage = 2 ∧
      s.account.spent = 2088 ∧ s.stopped = false := by
  norm_num [run, inquire, SystemsOrganization.evolve, advance, start, paid,
    RemainingDependency.charge, RemainingDependency.tariff, probeBody, drift,
    loss, total, deliverBody]

theorem shared_evidence_selects_inquiry :
    chooseRoute 8 7 8 5 1 3 2088 = inquire := by
  norm_num [chooseRoute, leastDose, mostDose]

theorem wide_tolerance_selects_immediate :
    chooseRoute 8 3 8 5 1 3 2088 = immediate 1 := by
  norm_num [chooseRoute, leastDose, mostDose]

theorem immediate_is_robust_with_wider_tolerance : robust 8 2 3 8 5 1 3 1 := by
  apply (robust_iff_interval _ _ _ _ _ _ _ _ (by norm_num) (by norm_num)).mpr
  norm_num [leastDose,mostDose]

theorem immediate_uses_less_work :
    let s := run 8 3 (start 8 3 5) (immediate 1)
    s.a = 3 ∧ s.stage = 2 ∧ s.account.spent = 1044 ∧ s.account.fuel = 1044 := by
  norm_num [run, immediate, SystemsOrganization.evolve, advance, start, paid,
    RemainingDependency.charge, RemainingDependency.tariff, drift, loss, deliverBody]

theorem inquiry_can_cross_floor_before_response :
    let s := run 2 1 (start 2 3 5) [.sense]
    s.a = -1 ∧ s.stage = 1 ∧ s.view.loss = 3 := by
  norm_num [run, SystemsOrganization.evolve, advance, start, paid,
    RemainingDependency.charge, RemainingDependency.tariff, probeBody, drift, loss, total]

theorem early_response_keeps_floor :
    let s := run 2 1 (start 2 3 5) (immediate 5)
    s.a = 1 ∧ s.stage = 2 ∧ s.source = 0 ∧ s.account.spent = 1044 := by
  norm_num [run, immediate, SystemsOrganization.evolve, advance, start, paid,
    RemainingDependency.charge, RemainingDependency.tariff, drift, loss, deliverBody]

theorem selector_rejects_unsafe_inquiry : chooseRoute 2 1 2 5 1 3 2088 = [] := by
  norm_num [chooseRoute, leastDose, mostDose]

theorem selector_rejects_unfunded_inquiry : chooseRoute 8 7 8 5 1 3 1044 = [] := by
  norm_num [chooseRoute, leastDose, mostDose]

/-- This counterexample is deliberate: current-headroom and work guards are
insufficient to certify the post-query support requirement. -/
theorem selected_inquiry_can_lack_support :
    chooseRoute 8 7 8 4 1 3 2088 = inquire ∧
    (run 8 7 (start 8 3 4) inquire).stopped = true ∧
    (run 8 7 (start 8 3 4) inquire).a = 2 := by
  norm_num [chooseRoute, leastDose, mostDose, run, inquire,
    SystemsOrganization.evolve, advance, start, paid,
    RemainingDependency.charge, RemainingDependency.tariff, probeBody, drift,
    loss, total, deliverBody]

/-- Exact post-query calibration admits an individually fitted correction. -/
theorem adaptive_dose_admissible (a H lower upper S lo hi l : ℝ)
    (hH : 0 ≤ H) (hl : lo ≤ l) (hh : l ≤ hi)
    (hbounds : lower ≤ upper) (hs : 0 ≤ S)
    (hupper : a-H*lo ≤ upper)
    (hsupply : leastDose a H lower hi ≤ S) :
    admissible a H lower upper S l (leastDose a H lower l) := by
  have hmlo := mul_le_mul_of_nonneg_left hl hH
  have hmhi := mul_le_mul_of_nonneg_left hh hH
  have cap : lower-a+H*hi ≤ S := (le_max_right 0 _).trans hsupply
  dsimp [admissible, terminal, leastDose]
  constructor
  · exact le_max_left _ _
  constructor
  · exact max_le hs (by linarith)
  by_cases h : 0 ≤ lower-a+H*l
  · rw [max_eq_right h]
    constructor <;> linarith
  · rw [max_eq_left (le_of_not_ge h)]
    constructor <;> linarith

/-- The second-stage guard repairs the support omission in chooseRoute.
It remains an idealized, supplied selector with no charged selection overhead. -/
def guardedRoute (a lower upper S lo hi : ℝ) (fuel : Nat) : List Event :=
  if 0 ≤ lo ∧ lo ≤ hi ∧ 0 ≤ a ∧ 0 ≤ lower ∧ lower ≤ upper ∧
      0 ≤ S ∧ 1044 ≤ fuel then
    if leastDose a 2 lower hi ≤ mostDose a 2 upper S lo then
      immediate (leastDose a 2 lower hi)
    else if 2088 ≤ fuel ∧ 0 ≤ a-hi ∧ a-2*lo ≤ upper ∧
        leastDose a 2 lower hi ≤ S then inquire else []
  else []

theorem guarded_inquiry_has_feasible_correction (a lower upper S lo hi l : ℝ)
    (fuel : Nat) (h : guardedRoute a lower upper S lo hi fuel = inquire)
    (hl : lo ≤ l) (hh : l ≤ hi) :
    admissible a 2 lower upper S l (leastDose a 2 lower l) ∧ 0 ≤ a-l := by
  unfold guardedRoute at h
  split at h
  · rename_i base
    split at h
    · simp [immediate, inquire] at h
    · split at h
      · rename_i query
        exact ⟨adaptive_dose_admissible a 2 lower upper S lo hi l (by norm_num)
          hl hh base.2.2.2.2.1 base.2.2.2.2.2.1 query.2.2.1 query.2.2.2,
          by linarith [query.2.1]⟩
      · simp [inquire] at h
  · simp [inquire] at h

theorem guarded_immediate_is_robust (a lower upper S lo hi u : ℝ) (fuel : Nat)
    (h : guardedRoute a lower upper S lo hi fuel = immediate u) :
    robust a 2 lower upper S lo hi u := by
  unfold guardedRoute at h
  split at h
  · rename_i base
    split at h
    · rename_i feasible
      have eq : leastDose a 2 lower hi = u := by simpa [immediate] using h
      rw [← eq]
      exact (robust_iff_interval a 2 lower upper S lo hi _ (by norm_num) base.2.1).mpr ⟨le_rfl, feasible⟩
    · split at h <;> simp [inquire, immediate] at h
  · simp [immediate] at h

theorem repaired_selection_retains_useful_inquiry :
    guardedRoute 8 7 8 5 1 3 2088 = inquire := by
  norm_num [guardedRoute, leastDose, mostDose]

theorem repaired_selection_rejects_insufficient_support :
    guardedRoute 8 7 8 4 1 3 2088 = [] := by
  norm_num [guardedRoute, leastDose, mostDose]

end
end InquiryChoice

#print axioms InquiryChoice.robust_iff_interval
#print axioms InquiryChoice.robust_exists_iff
#print axioms InquiryChoice.minimal_robust_dose
#print axioms InquiryChoice.indistinguishable_conflict
#print axioms InquiryChoice.observed_class_policy_iff
#print axioms InquiryChoice.waiting_floor
#print axioms InquiryChoice.early_support_dominates_before_delivery
#print axioms InquiryChoice.same_horizon_same_dose
#print axioms InquiryChoice.run_is_core_trace
#print axioms InquiryChoice.deliver_work_conserved
#print axioms InquiryChoice.run_work_conserved
#print axioms InquiryChoice.two_losses_have_no_common_immediate_dose
#print axioms InquiryChoice.low_loss_inquiry
#print axioms InquiryChoice.high_loss_inquiry
#print axioms InquiryChoice.shared_evidence_selects_inquiry
#print axioms InquiryChoice.wide_tolerance_selects_immediate
#print axioms InquiryChoice.immediate_is_robust_with_wider_tolerance
#print axioms InquiryChoice.immediate_uses_less_work
#print axioms InquiryChoice.inquiry_can_cross_floor_before_response
#print axioms InquiryChoice.early_response_keeps_floor
#print axioms InquiryChoice.selector_rejects_unsafe_inquiry
#print axioms InquiryChoice.selector_rejects_unfunded_inquiry
#print axioms InquiryChoice.selected_inquiry_can_lack_support
#print axioms InquiryChoice.adaptive_dose_admissible
#print axioms InquiryChoice.guarded_inquiry_has_feasible_correction
#print axioms InquiryChoice.guarded_immediate_is_robust
#print axioms InquiryChoice.repaired_selection_retains_useful_inquiry
#print axioms InquiryChoice.repaired_selection_rejects_insufficient_support
