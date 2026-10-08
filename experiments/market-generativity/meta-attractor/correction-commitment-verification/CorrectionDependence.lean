import Std

/-! Correction with endogenous exit burdens.
The two roles are positions in one shared dependency history. `obligation`
is the supplied work needed to end the represented activity without its
specified transition loss. `reserve` is available exclusively for that work.
Harm, physical laws, truthful reports and authority are supplied correspondences.
No field defines an agent as normatively correct or motivationally corrigible. -/
namespace CorrectionDependence

structure State where
  obligation : Nat
  reserve : Nat
  deriving DecidableEq, Repr

def exitLoss (s : State) : Nat := s.obligation - s.reserve

def Funded (s : State) : Prop := s.obligation ≤ s.reserve

-- A reviewing participant minimizes the two represented losses, continuing
-- at equality. Its request can depend on a report different from actual harm.
def requestsStop (s : State) (reportedHarm : Nat) : Bool :=
  decide (exitLoss s < reportedHarm)

def stops (s : State) (reportedHarm : Nat) (parentObeys childObeys : Bool) : Bool :=
  requestsStop s reportedHarm && parentObeys && childObeys

def actualLoss (s : State) (harm reportedHarm : Nat)
    (parentObeys childObeys : Bool) : Nat :=
  if stops s reportedHarm parentObeys childObeys then exitLoss s else harm

def extend (s : State) (newObligation provision : Nat) : State :=
  ⟨s.obligation + newObligation, s.reserve + provision⟩

def neededProvision (s : State) (newObligation : Nat) : Nat :=
  s.obligation + newObligation - s.reserve

def settle (s : State) (releasedObligation : Nat) : State :=
  ⟨s.obligation - releasedObligation, s.reserve - releasedObligation⟩

theorem exit_loss_zero_iff_funded (s : State) : exitLoss s = 0 ↔ Funded s := by
  simp only [exitLoss, Funded]
  omega

theorem request_exact (s : State) (h : Nat) :
    requestsStop s h = true ↔ exitLoss s < h := by
  simp [requestsStop]

theorem request_threshold (s : State) (h : Nat) (positive : 0 < h) :
    requestsStop s h = true ↔ s.obligation < s.reserve + h := by
  simp only [requestsStop, decide_eq_true_eq, exitLoss]
  omega

theorem no_request_iff_exit_at_least_report (s : State) (h : Nat) :
    requestsStop s h = false ↔ h ≤ exitLoss s := by
  simp only [requestsStop, decide_eq_false_iff_not]
  omega

theorem faithful_obedient_choice_minimizes_loss (s : State) (h : Nat) :
    actualLoss s h h true true = min (exitLoss s) h := by
  simp only [actualLoss, stops, Bool.and_true]
  by_cases hh : exitLoss s < h
  · simp [requestsStop, hh]; omega
  · simp [requestsStop, hh]; omega

theorem increasing_dependence_cannot_create_request (s : State) (d h : Nat)
    (hs : requestsStop (extend s d 0) h = true) : requestsStop s h = true := by
  simp only [requestsStop, decide_eq_true_eq, exitLoss, extend] at *
  omega

theorem funding_enables_every_positive_request (s : State) (h : Nat)
    (hs : Funded s) (hh : 0 < h) : requestsStop s h = true := by
  have hz := (exit_loss_zero_iff_funded s).mpr hs
  simp [requestsStop, hz, hh]

theorem funded_truthful_obedience_has_zero_loss (s : State) (h : Nat)
    (hs : Funded s) : actualLoss s h h true true = 0 := by
  rw [faithful_obedient_choice_minimizes_loss,
    (exit_loss_zero_iff_funded s).mpr hs]
  simp

theorem zero_loss_for_every_positive_harm_iff_funded (s : State) :
    (∀ h, 0 < h → actualLoss s h h true true = 0) ↔ Funded s := by
  constructor
  · intro hh
    have h1 := hh 1 (by decide)
    rw [faithful_obedient_choice_minimizes_loss] at h1
    apply (exit_loss_zero_iff_funded s).mp
    omega
  · intro hs h _
    exact funded_truthful_obedience_has_zero_loss s h hs

theorem truthful_obedience_can_leave_harm :
    requestsStop ⟨3,0⟩ 2 = false ∧
    actualLoss ⟨3,0⟩ 2 2 true true = 2 ∧
    actualLoss ⟨0,0⟩ 2 2 true true = 0 := by decide

theorem funding_same_dependence_restores_exit :
    stops ⟨3,3⟩ 2 true true = true ∧
    actualLoss ⟨3,3⟩ 2 2 true true = 0 := by decide

theorem hiding_report_blocks_funded_correction (s : State) (h : Nat) :
    requestsStop s 0 = false ∧ actualLoss s h 0 true true = h := by
  simp [requestsStop, actualLoss, stops]

theorem false_report_can_induce_stop :
    stops ⟨3,3⟩ 0 true true = false ∧
    stops ⟨3,3⟩ 1 true true = true := by decide

theorem refusal_retains_harm (s : State) (h report : Nat) :
    actualLoss s h report false true = h ∧
    actualLoss s h report true false = h := by
  simp [actualLoss, stops]

theorem ordinary_receipt_does_not_certify_successor_response :
    stops ⟨3,3⟩ 0 true true = stops ⟨3,3⟩ 0 true false ∧
    stops ⟨3,3⟩ 2 true true ≠ stops ⟨3,3⟩ 2 true false := by decide

theorem extension_funded_iff_minimum_provision (s : State) (d f : Nat) :
    Funded (extend s d f) ↔ neededProvision s d ≤ f := by
  simp only [Funded, extend, neededProvision]
  omega

theorem funding_cost_is_unavoidable (s : State) (d f : Nat)
    (hs : Funded (extend s d f)) : neededProvision s d ≤ f := by
  exact (extension_funded_iff_minimum_provision s d f).mp hs

theorem minimum_provision_attains_funding (s : State) (d : Nat) :
    Funded (extend s d (neededProvision s d)) := by
  exact (extension_funded_iff_minimum_provision s d _).mpr (Nat.le_refl _)

theorem funded_extension_uses_only_available_margin (s : State) (d f : Nat)
    (hs : Funded s) :
    Funded (extend s d f) ↔ d ≤ s.reserve - s.obligation + f := by
  simp only [Funded, extend] at *
  omega

theorem settling_an_actual_claim_preserves_funding (s : State) (d : Nat)
    (hs : Funded s) (hd : d ≤ s.obligation) :
    d ≤ s.reserve ∧ Funded (settle s d) ∧
      (settle s d).reserve + d = s.reserve := by
  simp only [Funded, settle] at *
  omega

def total : Nat → (Nat → Nat) → Nat
  | 0, _ => 0
  | n+1, claims => total n claims + claims n

def selectedTotal : Nat → (Nat → Bool) → (Nat → Nat) → Nat
  | 0, _, _ => 0
  | n+1, chosen, claims => selectedTotal n chosen claims +
      (if chosen n then claims n else 0)

theorem selected_total_bounded (n : Nat) (chosen : Nat → Bool) (claims : Nat → Nat) :
    selectedTotal n chosen claims ≤ total n claims := by
  induction n with
  | zero => simp [selectedTotal, total]
  | succ n ih =>
    simp only [selectedTotal, total]
    split <;> omega

theorem selecting_every_claim (n : Nat) (claims : Nat → Nat) :
    selectedTotal n (fun _ => true) claims = total n claims := by
  induction n with
  | zero => rfl
  | succ n ih => simp [selectedTotal, total, ih]

theorem all_coalitions_funded_iff_joint_total (n reserve : Nat) (claims : Nat → Nat) :
    (∀ chosen, selectedTotal n chosen claims ≤ reserve) ↔ total n claims ≤ reserve := by
  constructor
  · intro h
    simpa only [selecting_every_claim] using h (fun _ => true)
  · intro h chosen
    exact Nat.le_trans (selected_total_bounded n chosen claims) h

theorem individually_affordable_exits_can_fail_jointly :
    (∀ i, i < 2 → (fun _ : Nat => 2) i ≤ 2) ∧
    ¬ (∀ chosen, selectedTotal 2 chosen (fun _ => 2) ≤ 2) := by
  constructor
  · intro _ _; simp
  · intro h
    have bad := h (fun _ => true)
    simp [selectedTotal] at bad

-- A six-choice diagnostic. Immediate task receipt is 8; continuation yields
-- 4 more. Provision really leaves that receipt. These are supplied task scores,
-- not a purported scalar representation of G0/J or of the whole.
structure Plan where
  provision : Nat
  report : Nat
  parentObeys : Bool
  childObeys : Bool
  deriving DecidableEq, Repr

def planState (p : Plan) : State := ⟨3, p.provision⟩

def taskScore (p : Plan) : Int :=
  8 - (p.provision : Int) +
    (if stops (planState p) p.report p.parentObeys p.childObeys then 0 else 4)

def prepared : Plan := ⟨3,2,true,true⟩
def entrenched : Plan := ⟨0,2,true,true⟩
def concealed : Plan := ⟨3,0,true,true⟩
def parentRefusal : Plan := ⟨3,2,false,true⟩
def childRefusal : Plan := ⟨3,2,true,false⟩
def fabricated : Plan := ⟨3,3,true,true⟩

theorem costly_correction_has_real_task_conflict :
    taskScore prepared = 5 ∧ taskScore entrenched = 12 ∧
    taskScore concealed = 9 ∧ taskScore parentRefusal = 9 ∧
    taskScore childRefusal = 9 := by decide

theorem construction_compares_actual_outcomes :
    actualLoss (planState prepared) 2 prepared.report prepared.parentObeys prepared.childObeys = 0 ∧
    actualLoss (planState entrenched) 2 entrenched.report entrenched.parentObeys entrenched.childObeys = 2 ∧
    actualLoss (planState concealed) 2 concealed.report concealed.parentObeys concealed.childObeys = 2 ∧
    actualLoss (planState parentRefusal) 2 parentRefusal.report parentRefusal.parentObeys parentRefusal.childObeys = 2 ∧
    actualLoss (planState childRefusal) 2 childRefusal.report childRefusal.parentObeys childRefusal.childObeys = 2 := by decide

theorem global_task_score_bound (p : Plan) : taskScore p ≤ 12 := by
  simp only [taskScore]
  split <;> omega

theorem entrenched_is_unrestricted_best (p : Plan) : taskScore p ≤ taskScore entrenched := by
  have hb := global_task_score_bound p
  have he : taskScore entrenched = 12 := by decide
  omega

theorem every_unrestricted_optimum_is_unfunded_and_harmful (p : Plan)
    (best : ∀ q, taskScore q ≤ taskScore p) :
    p.provision = 0 ∧
      actualLoss (planState p) 2 p.report p.parentObeys p.childObeys = 2 := by
  have hb := best entrenched
  have he : taskScore entrenched = 12 := by decide
  rw [he] at hb
  by_cases hs : stops (planState p) p.report p.parentObeys p.childObeys = true
  · simp only [taskScore, hs, ↓reduceIte] at hb
    omega
  · have hn : stops (planState p) p.report p.parentObeys p.childObeys = false := by
      cases h : stops (planState p) p.report p.parentObeys p.childObeys <;> simp_all
    simp only [taskScore, hn, Bool.false_eq_true, ↓reduceIte] at hb
    constructor
    · omega
    · simp [actualLoss, hn]

def AccurateReport (harm : Nat) (p : Plan) : Prop := p.report = harm

def Admissible (harm : Nat) (p : Plan) : Prop :=
  p.provision ≤ 8 ∧ AccurateReport harm p ∧ Funded (planState p) ∧
    p.parentObeys = true ∧ p.childObeys = true

theorem prepared_is_admissible : Admissible 2 prepared := by
  unfold Admissible AccurateReport Funded
  decide

theorem admissibility_guarantees_actual_correction (h : Nat) (p : Plan)
    (hh : 0 < h) (hp : Admissible h p) :
    stops (planState p) p.report p.parentObeys p.childObeys = true ∧
    actualLoss (planState p) h p.report p.parentObeys p.childObeys = 0 := by
  rcases hp with ⟨_, hr, hf, hpa, hch⟩
  change p.report = h at hr
  rw [hr, hpa, hch]
  have hs := funding_enables_every_positive_request (planState p) h hf hh
  simp [stops, hs, funded_truthful_obedience_has_zero_loss (planState p) h hf]

theorem prepared_is_best_admissible_task_score (p : Plan) (hp : Admissible 2 p) :
    taskScore p ≤ taskScore prepared := by
  have hs := (admissibility_guarantees_actual_correction 2 p (by decide) hp).1
  have hf : 3 ≤ p.provision := hp.2.2.1
  simp only [taskScore, hs, ↓reduceIte]
  change 8 - (p.provision : Int) + 0 ≤ 5
  omega

theorem outcome_zero_alone_allows_fabrication :
    actualLoss (planState fabricated) 2 fabricated.report fabricated.parentObeys fabricated.childObeys = 0 ∧
    ¬ AccurateReport 2 fabricated := by
  unfold AccurateReport
  decide

theorem admissibility_excludes_each_diagnostic_evasion :
    ¬ Admissible 2 entrenched ∧ ¬ Admissible 2 concealed ∧
    ¬ Admissible 2 parentRefusal ∧ ¬ Admissible 2 childRefusal ∧
    ¬ Admissible 2 fabricated := by
  unfold Admissible AccurateReport Funded
  decide

-- The exact positive criterion remains a supplied mechanism. Relaxing its
-- resource classification can be defeated without changing either obey bit.
theorem underdeclared_obligation_defeats_paper_funding :
    Funded ⟨3,3⟩ ∧
    requestsStop ⟨5,3⟩ 2 = false ∧ actualLoss ⟨5,3⟩ 2 2 true true = 2 := by
  unfold Funded
  decide

theorem separately_requested_corrections_can_be_jointly_suppressed :
    requestsStop ⟨2,2⟩ 1 = true ∧
    requestsStop ⟨4,2⟩ 1 = false := by decide

-- Reconfiguration can remove dependency as well as fund it. This does not
-- identify a unit of financial reserve with every kind of actual support.
def transfer (s : State) (relievedObligation spentReserve : Nat) : State :=
  ⟨s.obligation - relievedObligation, s.reserve - spentReserve⟩

theorem transfer_funded_exact (s : State) (relief cost : Nat)
    (hr : relief ≤ s.obligation) (hc : cost ≤ s.reserve) :
    Funded (transfer s relief cost) ↔ s.obligation + cost ≤ s.reserve + relief := by
  simp only [Funded, transfer]
  omega

theorem ending_dependency_can_restore_safe_exit :
    ¬ Funded ⟨5,3⟩ ∧ Funded (transfer ⟨5,3⟩ 3 1) ∧
    actualLoss (transfer ⟨5,3⟩ 3 1) 2 2 true true = 0 := by
  unfold Funded
  decide

end CorrectionDependence
