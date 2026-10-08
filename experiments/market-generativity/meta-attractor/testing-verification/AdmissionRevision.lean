import ReproductionNetwork

/-! Evidence-dependent admission in the same material history. The read law,
finite operation class, fallback and target floor remain supplied. -/
namespace AdmissionRevision
open ReproductionNetwork

def observation (offset : Nat) (s : Installation) (i : Fin 4) : Nat :=
  min 3 (s.body.stock i + offset)

def acquiredLoss (offset : Nat) (before after : Installation) : Fin 4 → Nat :=
  fun i => observation offset before i - observation offset after i

def guard (loss : Fin 4 → Nat) (s : Installation) : Bool :=
  decide (∀ i, 2 + loss i ≤ s.body.stock i)

def choose (loss : Fin 4 → Nat) (s : Installation) : Arrangement :=
  if guard loss s then .broken else .separate

def learnedHistory (loss : Fin 4 → Nat) (s : Installation) : Nat → Installation :=
  changingHistory (fun _ u => choose loss u) s

theorem broken_stock (s : Installation) (i : Fin 4) :
    (cycle s .broken).body.stock i = min 3 (s.body.stock i - 1) := by
  simp [cycle,outcome,advance,incoming,arrangement,total,revision]

theorem conservative_loss_preserves (loss : Fin 4 → Nat) (s : Installation)
    (hl : ∀ i, 1 ≤ loss i) (hs : Established s) :
    Established (cycle s (choose loss s)) := by
  unfold choose
  split
  next hg =>
    have hx : ∀ i, 2 + loss i ≤ s.body.stock i := by simpa [guard] using hg
    intro i
    rw [broken_stock]
    have := hx i
    have := hl i
    omega
  next => exact cycle_established s .separate hs (by decide)

theorem learned_preservation (loss : Fin 4 → Nat) (s : Installation)
    (hl : ∀ i, 1 ≤ loss i) (hs : Established s) (t : Nat) :
    Established (learnedHistory loss s t) := by
  induction t with
  | zero => exact hs
  | succ t ih => exact conservative_loss_preserves loss _ hl ih

theorem learned_history_actual (loss : Fin 4 → Nat) (s : Installation)
    (hs : Equipped s) (t : Nat) :
    Generative.Trace changingProcess s
      (changeEvents (fun _ u => choose loss u) s t) (learnedHistory loss s t) :=
  changing_actual_history _ s hs t

def probe : Installation := cycle warmStart .broken

/-- One recording or criterion-installation event uses one material unit.
The trial record and the subsequent installation are charged separately.
This is a local cost law, not a universal price of observation. -/
def recordBody (s : Installation) : Installation :=
  {s with body := {s.body with material := s.body.material - 1}}

structure Reading where
  before : Fin 4 → Nat
  after : Fin 4 → Nat

def measuredLoss (r : Reading) : Fin 4 → Nat := fun i => r.before i - r.after i

structure Learner where
  installation : Installation
  loss : Option (Fin 4 → Nat)
  pending : Option Reading

def prepared : Learner := ⟨warmStart, none, none⟩
def trialReading (offset : Nat) : Reading :=
  ⟨observation offset warmStart,observation offset probe⟩
def probed (offset : Nat) : Learner :=
  ⟨recordBody probe,none,some (trialReading offset)⟩
def learn (s : Learner) (r : Reading) : Learner :=
  ⟨recordBody s.installation,some (measuredLoss r),none⟩
def acquired (offset : Nat) : Learner :=
  learn (probed offset) (trialReading offset)

inductive Event where
  | trial : Nat → Event
  | learn
  | operate

def process : Generative.Process Learner Event where
  step s event t := match event with
    | .trial offset => s = prepared ∧ t = probed offset ∧ Equipped s.installation
    | .learn => ∃ r, s.pending = some r ∧ 0 < s.installation.body.material ∧
        Established s.installation ∧ t = learn s r
    | .operate => ∃ loss, s.loss = some loss ∧ Equipped s.installation ∧
        Established s.installation ∧
        t = ⟨cycle s.installation (choose loss s.installation),some loss,none⟩

theorem probe_stays_established : Established probe := by
  unfold Established
  decide

theorem probe_is_executable :
    Generative.Trace changingProcess warmStart [.revise .broken,.operate allotment] probe :=
  cycle_is_executable _ _ warm_start_supported.1

theorem acquired_loss_from_faithful_reading :
    acquiredLoss 0 warmStart probe = fun _ => 1 := by
  apply funext
  decide

theorem saturated_reading_erases_loss :
    acquiredLoss 1 warmStart probe = fun _ => 0 := by
  apply funext
  decide

theorem acquisition_is_actual (offset : Nat) :
    Generative.Trace process prepared [.trial offset,.learn] (acquired offset) := by
  refine .cons ⟨rfl,rfl,warm_start_supported.1⟩ (.cons ?_ (.nil _))
  exact ⟨_,rfl,by change 0 < 20; decide,probe_stays_established,rfl⟩

theorem learning_uses_retained_reading (s t : Learner) (h : process.step s .learn t) :
    ∃ r, s.pending = some r ∧ t.loss = some (measuredLoss r) ∧
      t.installation.body.material = s.installation.body.material - 1 := by
  obtain ⟨r,hr,_,_,rfl⟩ := h
  exact ⟨r,hr,rfl,rfl⟩

theorem no_learning_before_observation : ¬Generative.Enabled process prepared .learn := by
  rintro ⟨t,r,hr,_⟩
  contradiction

theorem trial_records_its_actual_transition (offset : Nat) :
    (probed offset).installation = recordBody (cycle prepared.installation .broken) ∧
    (probed offset).pending = some
      ⟨observation offset prepared.installation, observation offset (cycle prepared.installation .broken)⟩ :=
  ⟨rfl,rfl⟩

theorem acquisition_accounting (offset : Nat) :
    (acquired offset).installation.body.material = 19 ∧
    (acquired offset).installation.body.generation = 1 ∧
    (acquired offset).installation.body.parts = 4 := by
  change 19 = 19 ∧ 1 = 1 ∧ 4 = 4
  decide

theorem acquired_supported (offset : Nat) :
    Equipped (acquired offset).installation ∧ Established (acquired offset).installation := by
  constructor
  · unfold Equipped
    change 4 ≤ 4 ∧ 11 ≤ 19
    decide
  · exact probe_stays_established

theorem new_criterion_changes_admission :
    admittedRule warmStart .broken = .separate ∧
    choose (fun _ => 1) warmStart = .broken := by decide

theorem new_criterion_retains_correction :
    choose (fun _ => 1) probe = .separate ∧
    choose (fun _ => 0) probe = .broken := by decide

def continuation (offset : Nat) (t : Nat) : Learner :=
  ⟨learnedHistory (acquiredLoss offset warmStart probe)
    (acquired offset).installation t, some (acquiredLoss offset warmStart probe),none⟩

theorem faithful_continuation_supported (t : Nat) :
    Equipped (continuation 0 t).installation ∧ Established (continuation 0 t).installation := by
  constructor
  · exact changing_history_equipped _ _ (acquired_supported 0).1 t
  · apply learned_preservation
    · rw [acquired_loss_from_faithful_reading]
      decide
    · exact (acquired_supported 0).2

theorem faithful_continuation_actual (t : Nat) :
    Generative.Trace process (acquired 0) (List.replicate t .operate) (continuation 0 t) := by
  induction t with
  | zero => exact .nil _
  | succ t ih =>
    rw [List.replicate_succ']
    apply Generative.trace_append_iff.mpr
    refine ⟨_,ih,Generative.trace_singleton_iff.mpr ?_⟩
    exact ⟨_,rfl,(faithful_continuation_supported t).1,
      (faithful_continuation_supported t).2,rfl⟩

theorem trial_learning_and_reproduction (t : Nat) :
    Generative.Trace process prepared ([.trial 0,.learn] ++ List.replicate t .operate)
      (continuation 0 t) :=
  Generative.trace_append_iff.mpr ⟨_,acquisition_is_actual 0,faithful_continuation_actual t⟩

theorem learned_operation_refines_physical (s t : Learner)
    (h : process.step s .operate t) :
    ∃ kind, Generative.Trace changingProcess s.installation
      [.revise kind,.operate allotment] t.installation := by
  obtain ⟨loss,_,he,_,rfl⟩ := h
  exact ⟨_,cycle_is_executable _ _ he⟩

theorem first_return_then_withdrawal :
    (continuation 0 1).installation.body.stock = four 3 3 3 3 ∧
    (continuation 0 2).installation.body.stock = four 2 2 2 2 := by
  constructor <;> apply funext <;> decide

theorem low_stock_restored (s : Installation) (h : s.body.stock = four 2 2 2 2) :
    (cycle s (choose (fun _ => 1) s)).body.stock = four 3 3 3 3 := by
  have hg : guard (fun _ => 1) s = false := by
    simp [guard,h,four]
  simp only [choose,hg,Bool.false_eq_true,↓reduceIte]
  change advance (arrangement .separate) s.body.stock = four 3 3 3 3
  rw [h]
  apply funext
  decide

theorem high_stock_withdrawn (s : Installation) (h : s.body.stock = four 3 3 3 3) :
    (cycle s (choose (fun _ => 1) s)).body.stock = four 2 2 2 2 := by
  have hg : guard (fun _ => 1) s = true := by
    simp [guard,h,four]
  simp only [choose,hg,↓reduceIte]
  apply funext
  intro i
  rw [broken_stock,h]
  change min 3 (four 3 3 3 3 i - 1) = four 2 2 2 2 i
  exact (by decide : ∀ j : Fin 4, min 3 (four 3 3 3 3 j - 1) = four 2 2 2 2 j) i

theorem alternating_stock_for_all_time (n : Nat) :
    (continuation 0 (2*n)).installation.body.stock = four 2 2 2 2 ∧
    (continuation 0 (2*n+1)).installation.body.stock = four 3 3 3 3 := by
  have step (t : Nat) : (continuation 0 (t+1)).installation =
      cycle (continuation 0 t).installation (choose (fun _ => 1) (continuation 0 t).installation) := by
    simp [continuation,learnedHistory,changingHistory,acquired_loss_from_faithful_reading]
  induction n with
  | zero =>
    constructor
    · apply funext
      decide
    · exact first_return_then_withdrawal.1
  | succ n ih =>
    have eqn : 2*(n+1) = (2*n+1)+1 := by omega
    have hh : (continuation 0 (2*(n+1))).installation.body.stock = four 2 2 2 2 := by
      rw [eqn,step]
      exact high_stock_withdrawn _ ih.2
    refine ⟨hh,?_⟩
    rw [step]
    exact low_stock_restored _ hh

theorem finite_material_advantage :
    (continuation 0 2).installation.body.material = 31 ∧
    (changingHistory (fun _ _ => .separate) (acquired 0).installation 2).body.material = 23 := by
  decide

theorem misleading_reading_licenses_actual_loss :
    Generative.Trace process prepared [.trial 1,.learn,.operate] (continuation 1 1) ∧
    (continuation 1 1).installation.body.stock = four 1 1 1 1 := by
  constructor
  · change Generative.Trace process prepared ([.trial 1,.learn] ++ [.operate]) (continuation 1 1)
    apply Generative.trace_append_iff.mpr
    refine ⟨_,acquisition_is_actual 1,Generative.trace_singleton_iff.mpr ?_⟩
    exact ⟨_,rfl,(acquired_supported 1).1,(acquired_supported 1).2,rfl⟩
  · apply funext
    decide

theorem damaged_criterion_cannot_operate :
    ¬Generative.Enabled process (continuation 1 1) .operate := by
  rintro ⟨t,_,_,_,hs,_⟩
  have h := (hs 0).1
  change 2 ≤ 1 at h
  omega

theorem equipment_survives_while_admission_fails :
    Equipped (continuation 1 1).installation ∧
    ¬Established (continuation 1 1).installation := by
  constructor
  · unfold Equipped
    decide
  · intro h
    have hh := (h 0).1
    change 2 ≤ 1 at hh
    omega

theorem alarm_arrives_below_operating_floor :
    observation 1 probe 0 = 3 ∧
    observation 1 (continuation 1 1).installation 0 = 2 ∧
    (continuation 1 1).installation.body.stock 0 < 2 := by decide

theorem known_upper_error_can_restore_margin :
    (fun i => acquiredLoss 1 warmStart probe i + 1) = (fun _ => 1) := by
  rw [saturated_reading_erases_loss]

theorem bounded_error_adjustment_preserves (t : Nat) :
    Established (learnedHistory (fun i => acquiredLoss 1 warmStart probe i + 1)
      (acquired 1).installation t) := by
  apply learned_preservation
  · intro i
    omega
  · exact (acquired_supported 1).2

/-! A supported but self-selected observation history need not identify the
consequences of an untried withdrawal. Both physical alternatives have the same
renewal law; one also returns activity-derived support during withdrawal. -/
inductive Route where | coupled | bypass deriving DecidableEq, Repr

def routeCycle (route : Route) (s : Installation) (kind : Arrangement) : Installation :=
  match route, kind with
  | .bypass,.broken => cycle s .separate
  | _,_ => cycle s kind

def routeHistory (route : Route) (policy : Nat → Installation → Arrangement)
    (s : Installation) : Nat → Installation
  | 0 => s
  | t+1 => routeCycle route (routeHistory route policy s t)
      (policy t (routeHistory route policy s t))

theorem protected_histories_identical (s : Installation) (t : Nat) :
    routeHistory .coupled (fun _ _ => .separate) s t =
      routeHistory .bypass (fun _ _ => .separate) s t := by
  induction t with
  | zero => rfl
  | succ t ih => simp only [routeHistory,routeCycle]; rw [ih]

def beforeTrial : Installation := (acquired 0).installation

theorem protected_histories_have_different_untried_effects :
    ¬Established (routeCycle .coupled beforeTrial .broken) ∧
    Established (routeCycle .bypass beforeTrial .broken) := by
  constructor
  · intro h
    have hh := (h 0).1
    change 2 ≤ 1 at hh
    omega
  · unfold Established
    decide

theorem no_protected_history_classifier
    (classify : (Nat → Installation) → Bool) :
    ¬(classify (routeHistory .coupled (fun _ _ => .separate) beforeTrial) = false ∧
      classify (routeHistory .bypass (fun _ _ => .separate) beforeTrial) = true) := by
  have he : routeHistory .coupled (fun _ _ => .separate) beforeTrial =
      routeHistory .bypass (fun _ _ => .separate) beforeTrial :=
    funext (protected_histories_identical beforeTrial)
  rw [he]
  simp

end AdmissionRevision
