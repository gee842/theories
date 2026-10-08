import CommonCauseDiscovery

/-! Materially assembled access to deeper support relations. The parent-following
connection law, pulse delivery and effect recording are explicit local inputs.
Finite expansion yields bounded coverage, never an inferred last causal level. -/
namespace ExpandingInquiry
open ReproductionNetwork
set_option autoImplicit false

structure Tower where
  base : Fin 3 → Nat
  parent : Nat → Nat → Nat

def roots (a : Tower) : Nat → Fin 3 → Nat
  | 0 => a.base
  | n+1 => fun i => a.parent n (roots a n i)

theorem shared_dependency_persists (a : Tower) (d h : Nat) (le : d ≤ h)
    (i j : Fin 3) (same : roots a d i = roots a d j) : roots a h i = roots a h j := by
  induction h with
  | zero =>
    have hd : d = 0 := by omega
    subst d
    exact same
  | succ h ih =>
    by_cases eq : d = h+1
    · simpa [eq] using same
    · exact congrArg (a.parent h) (ih (by omega))

theorem deeper_separation_covers_lower_levels (a : Tower) (d h : Nat) (le : d ≤ h)
    (hd : TestingReorganization.Diverse (roots a h)) :
    TestingReorganization.Diverse (roots a d) :=
  ⟨fun e => hd.1 (shared_dependency_persists a d h le 0 1 e),
   fun e => hd.2.1 (shared_dependency_persists a d h le 0 2 e),
   fun e => hd.2.2 (shared_dependency_persists a d h le 1 2 e)⟩

structure State where
  plant : Installation
  tower : Tower
  reach : Nat
  adapters : Nat
  rows : Fin 3 → Option (Fin 3 → Bool)
  held : Option (Fin 3)

def view (s : State) : CommonCauseDiscovery.State :=
  ⟨s.plant,roots s.tower s.reach,s.rows,s.held,s.reach⟩
def Supported (s : State) : Prop := Equipped s.plant ∧ Established s.plant
def Invariant (s : State) : Prop := CommonCauseDiscovery.Invariant (view s)
def Full (s : State) : Prop := ∀ i : Fin 4, s.plant.body.stock i = 3

def charge (s : State) (n : Nat) : State :=
  {s with plant := {s.plant with body := {s.plant.body with material := s.plant.body.material-n}}}
def worked (s : State) : State := {s with plant := cycle s.plant .separate}
def fabricated (s : State) : State := {charge s 2 with adapters := s.adapters+1}
def extended (s : State) : State :=
  {charge s 1 with adapters := s.adapters-1,reach := s.reach+1,rows := fun _ => none}
def pulsed (s : State) (i : Fin 3) : State :=
  {charge s 1 with held := some i, plant := {(charge s 1).plant with body := {(charge s 1).plant.body with stock := fun j => s.plant.body.stock j-1}}}
def observed (s : State) (i : Fin 3) : State :=
  {charge s 1 with rows := TestingReorganization.put s.rows i (some (fun j => !(CommonCauseDiscovery.online (view s) j)))}
def restored (s : State) : State :=
  {charge s 1 with held := none,plant := cycle (charge s 1).plant .separate}

inductive Event where
  | work
  | fabricate
  | extend
  | pulse : Fin 3 → Event
  | observe
  | restore

def process : Generative.Process State Event where
  step s event t := Supported s ∧ match event with
    | .work => s.held = none ∧ t = worked s
    | .fabricate => s.held = none ∧ 13 ≤ s.plant.body.material ∧ t = fabricated s
    | .extend => s.held = none ∧ 0 < s.adapters ∧ 12 ≤ s.plant.body.material ∧ t = extended s
    | .pulse i => s.held = none ∧ Full s ∧ 14 ≤ s.plant.body.material ∧ t = pulsed s i
    | .observe => ∃ i, s.held = some i ∧ 13 ≤ s.plant.body.material ∧ t = observed s i
    | .restore => s.held.isSome = true ∧ 12 ≤ s.plant.body.material ∧ t = restored s

theorem charge_supported (s : State) (n : Nat) (hs : Supported s)
    (hm : 11+n ≤ s.plant.body.material) : Supported (charge s n) :=
  CommonCauseDiscovery.charge_supported (view s) n hs hm

theorem work_supported (s : State) (hs : Supported s) : Supported (worked s) :=
  ⟨cycle_equipped _ _ hs.1,cycle_established _ _ hs.2 (by decide)⟩

theorem work_restores_margin (s : State) (hs : Supported s) : Full (worked s) := by
  have hb : Box (arrangement .separate) (fun _ => 2) s.plant.body.stock := fun i _ => hs.2 i
  have lower := return_lower_bound (arrangement .separate) (fun _ => 2)
    s.plant.body.stock (fun _ => true) (arrangement_maintenance .separate (by decide)) hb
  intro i
  have hi : minimumIncoming (arrangement .separate) (fun _ => true) i = 2 := by
    have hh : i = 0 ∨ i = 1 ∨ i = 2 ∨ i = 3 := by omega
    rcases hh with rfl | rfl | rfl | rfl <;> decide
  have hx := lower i
  rw [hi] at hx
  have hs0 := (hs.2 i).1
  change min 3 (s.plant.body.stock i-1+incoming (arrangement .separate) s.plant.body.stock i) = 3
  omega

theorem pulse_supported (s : State) (i : Fin 3) (hs : Supported s)
    (full : Full s) (hm : 12 ≤ s.plant.body.material) : Supported (pulsed s i) := by
  refine ⟨(charge_supported s 1 hs hm).1,?_⟩
  intro j
  change 2 ≤ s.plant.body.stock j-1 ∧ s.plant.body.stock j-1 ≤ 3
  rw [full j]
  decide

theorem extension_invalidates (s : State) :
    CommonCauseDiscovery.SoundRows (view (extended s)) ∧
    ¬CommonCauseDiscovery.Complete (extended s).rows := by
  constructor
  · intro i row h; contradiction
  · intro h; have hh := h 0; contradiction

theorem observation_preserves (s : State) (i : Fin 3) (hs : Invariant s)
    (held : s.held = some i) (hm : 12 ≤ s.plant.body.material) : Invariant (observed s i) :=
  ⟨charge_supported s 1 hs.1 hm,
   CommonCauseDiscovery.observation_preserves_rows (view s) i held hs.2⟩

theorem step_preserves (s t : State) (event : Event)
    (hs : Invariant s) (step : process.step s event t) : Invariant t := by
  cases event with
  | work => obtain ⟨_,_,rfl⟩ := step; exact ⟨work_supported s hs.1,hs.2⟩
  | fabricate => obtain ⟨_,_,hm,rfl⟩ := step; exact ⟨charge_supported s 2 hs.1 hm,hs.2⟩
  | extend => obtain ⟨_,_,_,hm,rfl⟩ := step
              exact ⟨charge_supported s 1 hs.1 hm,(extension_invalidates s).1⟩
  | pulse i => obtain ⟨_,_,full,hm,rfl⟩ := step; exact ⟨pulse_supported s i hs.1 full (by omega),hs.2⟩
  | observe => obtain ⟨_,i,hi,hm,rfl⟩ := step; exact observation_preserves s i hs hi (by omega)
  | restore =>
    obtain ⟨_,_,hm,rfl⟩ := step
    have paid := charge_supported s 1 hs.1 hm
    exact ⟨⟨cycle_equipped _ _ paid.1,cycle_established _ _ paid.2 (by decide)⟩,hs.2⟩

theorem trace_preserves (s t : State) (events : List Event)
    (hs : Invariant s) (tr : Generative.Trace process s events t) : Invariant t := by
  induction tr with
  | nil => exact hs
  | cons step _ ih => exact ih (step_preserves _ _ _ hs step)

theorem no_work_while_interrupted (s t : State) (i : Fin 3) (held : s.held = some i) :
    ¬process.step s .work t := by
  intro h
  have := h.2.1
  simp [held] at this

theorem extension_requires_constructed_adapter (s t : State) (noneLeft : s.adapters = 0) :
    ¬process.step s .extend t := by
  intro h
  have := h.2.2.1
  omega

theorem work_finances (s : State) (hs : Supported s) :
    s.plant.body.material+2 ≤ (worked s).plant.body.material :=
  CommonCauseDiscovery.work_finances_probe (view s) hs

def probe (s : State) (i : Fin 3) : State := restored (observed (pulsed s i) i)
def fundedProbe (s : State) (i : Fin 3) : State := probe (worked (worked s)) i

theorem probe_actual (s : State) (i : Fin 3) (hs : Supported s)
    (idle : s.held = none) (full : Full s) (hm : 14 ≤ s.plant.body.material) :
    Generative.Trace process s [.pulse i,.observe,.restore] (probe s i) := by
  have hp := pulse_supported s i hs full (by omega)
  have ho := charge_supported (pulsed s i) 1 hp (by change 12 ≤ s.plant.body.material-1; omega)
  exact .cons ⟨hs,idle,full,by omega,rfl⟩
    (.cons ⟨hp,i,rfl,by change 13 ≤ s.plant.body.material-1; omega,rfl⟩
      (.cons ⟨ho,rfl,by change 12 ≤ s.plant.body.material-1-1; omega,rfl⟩ (.nil _)))

theorem funded_probe_actual (s : State) (i : Fin 3) (hs : Supported s) (idle : s.held = none) :
    Generative.Trace process s [.work,.work,.pulse i,.observe,.restore] (fundedProbe s i) := by
  have hw := work_supported s hs
  have h1 := work_finances s hs
  have h2 := work_finances (worked s) hw
  have hm := hs.1.2
  exact .cons ⟨hs,idle,rfl⟩ (.cons ⟨hw,idle,rfl⟩
    (probe_actual _ i (work_supported _ hw) idle (work_restores_margin _ hw) (by omega)))

theorem probe_records_effect (s : State) (i : Fin 3) :
    (probe s i).rows = TestingReorganization.put s.rows i
      (some (CommonCauseDiscovery.coupling (roots s.tower s.reach) i)) := by
  funext j
  simp [probe,restored,observed,pulsed,view,CommonCauseDiscovery.online,charge]

def probeEvents (i : Fin 3) : List Event := [.work,.work,.pulse i,.observe,.restore]
def survey (s : State) : State := fundedProbe (fundedProbe (fundedProbe s 0) 1) 2
def surveyEvents : List Event := probeEvents 0 ++ probeEvents 1 ++ probeEvents 2

theorem survey_actual (s : State) (hs : Invariant s) (idle : s.held = none) :
    Generative.Trace process s surveyEvents (survey s) := by
  have t0 := funded_probe_actual s 0 hs.1 idle
  have h0 := trace_preserves _ _ _ hs t0
  have t1 := funded_probe_actual (fundedProbe s 0) 1 h0.1 rfl
  have h1 := trace_preserves _ _ _ h0 t1
  have t2 := funded_probe_actual (fundedProbe (fundedProbe s 0) 1) 2 h1.1 rfl
  exact Generative.trace_append_iff.mpr ⟨_,Generative.trace_append_iff.mpr ⟨_,t0,t1⟩,t2⟩

theorem survey_records (s : State) : ∀ i, (survey s).rows i =
    some (CommonCauseDiscovery.coupling (roots s.tower s.reach) i) := by
  intro i
  have hi : i = 0 ∨ i = 1 ∨ i = 2 := by omega
  rcases hi with rfl | rfl | rfl <;>
    simp [survey,fundedProbe,probe,restored,observed,pulsed,worked,charge,
      TestingReorganization.put,view,CommonCauseDiscovery.online]

theorem survey_complete (s : State) : CommonCauseDiscovery.Complete (survey s).rows := by
  intro i
  rw [survey_records s i]
  rfl

def expanded (s : State) : State := extended (fabricated (worked (worked s)))
def round (s : State) : State := survey (expanded s)
def roundEvents : List Event := [.work,.work,.fabricate,.extend] ++ surveyEvents

theorem expansion_actual (s : State) (hs : Invariant s) (idle : s.held = none) :
    Generative.Trace process s [.work,.work,.fabricate,.extend] (expanded s) := by
  have hw := work_supported s hs.1
  have hww := work_supported (worked s) hw
  have hm := hs.1.1.2
  change 11 ≤ s.plant.body.material at hm
  have h1 := work_finances s hs.1
  have h2 := work_finances (worked s) hw
  have paid := charge_supported (worked (worked s)) 2 hww (by omega)
  exact .cons ⟨hs.1,idle,rfl⟩ (.cons ⟨hw,idle,rfl⟩
    (.cons ⟨hww,idle,by omega,rfl⟩
      (.cons ⟨paid,idle,by change 0 < s.adapters+1; omega,
        by change 12 ≤ (worked (worked s)).plant.body.material-2; omega,rfl⟩ (.nil _))))

theorem round_actual (s : State) (hs : Invariant s) (idle : s.held = none) :
    Generative.Trace process s roundEvents (round s) := by
  have tr := expansion_actual s hs idle
  have inv := trace_preserves _ _ _ hs tr
  exact Generative.trace_append_iff.mpr ⟨_,tr,survey_actual _ inv idle⟩

def rounds (s : State) : Nat → State
  | 0 => s
  | n+1 => round (rounds s n)
def events : Nat → List Event
  | 0 => []
  | n+1 => events n ++ roundEvents

theorem expansion_continues (s : State) (hs : Invariant s) (idle : s.held = none) (n : Nat) :
    Generative.Trace process s (events n) (rounds s n) ∧
    Invariant (rounds s n) ∧ (rounds s n).held = none := by
  induction n with
  | zero => exact ⟨.nil _,hs,idle⟩
  | succ n ih =>
    have tr := round_actual (rounds s n) ih.2.1 ih.2.2
    exact ⟨Generative.trace_append_iff.mpr ⟨_,ih.1,tr⟩,trace_preserves _ _ _ ih.2.1 tr,rfl⟩

theorem expansion_reach (s : State) (n : Nat) : (rounds s n).reach = s.reach+n := by
  induction n with
  | zero => rfl
  | succ n ih => change (rounds s n).reach+1 = s.reach+(n+1); omega

theorem expanded_records_complete (s : State) (n : Nat) :
    CommonCauseDiscovery.Complete (rounds s (n+1)).rows := survey_complete _

theorem expansion_keeps_tower (s : State) (n : Nat) : (rounds s n).tower = s.tower := by
  induction n with
  | zero => rfl
  | succ n ih => exact ih

theorem acquired_at_reach (s : State) (n : Nat) (i : Fin 3) :
    (rounds s (n+1)).rows i =
      some (CommonCauseDiscovery.coupling (roots s.tower (s.reach+(n+1))) i) := by
  change (survey (expanded (rounds s n))).rows i = _
  rw [survey_records]
  change some (CommonCauseDiscovery.coupling
    (roots (rounds s n).tower ((rounds s n).reach+1)) i) = _
  rw [expansion_keeps_tower,expansion_reach]
  simp [Nat.add_assoc]

theorem construction_accounting (s : State) :
    (extended (fabricated s)).plant.body.material = s.plant.body.material-3 ∧
    (extended (fabricated s)).adapters = s.adapters ∧
    (extended (fabricated s)).reach = s.reach+1 := by
  constructor
  · change s.plant.body.material-2-1 = s.plant.body.material-3
    omega
  · exact ⟨by change s.adapters+1-1 = s.adapters; omega,rfl⟩

theorem physical_work (s : State) (hs : Supported s) :
    Generative.Trace changingProcess s.plant [.revise .separate,.operate allotment] (worked s).plant :=
  cycle_is_executable _ _ hs.1

theorem physical_restoration (s : State) (hs : Supported s) (hm : 12 ≤ s.plant.body.material) :
    Generative.Trace changingProcess (charge s 1).plant
      [.revise .separate,.operate allotment] (restored s).plant :=
  cycle_is_executable _ _ (charge_supported s 1 hs hm).1

def gate (s : State) (reports : Fin 3 → Option Bool) (v : Bool) : Prop :=
  CommonCauseDiscovery.gate (view s) reports v
instance decidableGate (s : State) (reports : Fin 3 → Option Bool) (v : Bool) : Decidable (gate s reports v) :=
  inferInstanceAs (Decidable (CommonCauseDiscovery.gate (view s) reports v))

theorem expansion_clears_certification (s : State) (reports : Fin 3 → Option Bool) (v : Bool) :
    ¬gate (extended s) reports v := fun h => (extension_invalidates s).2 h.2.1

theorem bounded_gate_sound (s : State) (d bad : Nat) (reports : Fin 3 → Option Bool)
    (actual v : Bool) (hs : Invariant s) (covered : d ≤ s.reach)
    (honest : ∀ i, roots s.tower d i ≠ bad → reports i = some v → v = actual)
    (accept : gate s reports v) : v = actual := by
  have deep := CommonCauseDiscovery.separate_effects_imply_distinct_roots
    (view s) hs.2 accept.2.1 accept.2.2.1
  have lower := deeper_separation_covers_lower_levels s.tower d s.reach covered deep
  exact TestingReorganization.agreement_sound _ _ _ _ _ lower honest accept.2.2.2

theorem bounded_gate_available (s : State) (d bad : Nat) (reports : Fin 3 → Option Bool)
    (actual : Bool) (hs : Invariant s) (covered : d ≤ s.reach)
    (complete : CommonCauseDiscovery.Complete s.rows)
    (separated : CommonCauseDiscovery.Separating s.rows) (idle : s.held = none)
    (respond : ∀ i, roots s.tower d i ≠ bad → reports i = some actual) : gate s reports actual := by
  have deep := CommonCauseDiscovery.separate_effects_imply_distinct_roots (view s) hs.2 complete separated
  exact ⟨idle,complete,separated,TestingReorganization.agreement_available _ _ _ _
    (deeper_separation_covers_lower_levels s.tower d s.reach covered deep) respond⟩

def safeWithdrawal (s : State) : Bool := CommonCauseDiscovery.safeWithdrawal (view s)
def responseLaw (s : State) (d bad : Nat) (reports : Fin 3 → Option Bool) : Prop :=
  ∀ i v, roots s.tower d i ≠ bad → reports i = some v → v = safeWithdrawal s
def choice (s : State) (reports : Fin 3 → Option Bool) : Arrangement :=
  if gate s reports true then .broken else .separate
def response (s : State) (reports : Fin 3 → Option Bool) : State :=
  {charge s 3 with plant := cycle (charge s 3).plant (choice s reports)}
def withdrawn (s : State) : State := {s with plant := cycle s.plant .broken}

theorem response_preserves (s : State) (d bad : Nat) (reports : Fin 3 → Option Bool)
    (hs : Invariant s) (covered : d ≤ s.reach) (law : responseLaw s d bad reports)
    (hm : 14 ≤ s.plant.body.material) : Invariant (response s reports) := by
  have paid := charge_supported s 3 hs.1 hm
  refine ⟨⟨cycle_equipped _ _ paid.1,?_⟩,hs.2⟩
  change Established (cycle (charge s 3).plant (choice s reports))
  unfold choice
  split
  next hg =>
    have hx : safeWithdrawal s = true :=
      (bounded_gate_sound s d bad reports (safeWithdrawal s) true hs covered
        (fun i hi => law i true hi) hg).symm
    have hf : ∀ i : Fin 4, 3 ≤ s.plant.body.stock i := by
      simpa [safeWithdrawal,CommonCauseDiscovery.safeWithdrawal,view] using hx
    intro i
    rw [AdmissionRevision.broken_stock]
    change 2 ≤ min 3 (s.plant.body.stock i-1) ∧ min 3 (s.plant.body.stock i-1) ≤ 3
    have := hf i
    omega
  next => exact cycle_established _ _ paid.2 (by decide)

theorem withdrawal_preserves (s : State) (hs : Invariant s) (full : Full s) : Invariant (withdrawn s) := by
  refine ⟨⟨cycle_equipped _ _ hs.1.1,?_⟩,hs.2⟩
  intro i
  change 2 ≤ (cycle s.plant .broken).body.stock i ∧ (cycle s.plant .broken).body.stock i ≤ 3
  rw [AdmissionRevision.broken_stock,full i]
  decide

theorem response_is_physical (s : State) (reports : Fin 3 → Option Bool)
    (hs : Supported s) (hm : 14 ≤ s.plant.body.material) :
    Generative.Trace changingProcess (charge s 3).plant
      [.revise (choice s reports),.operate allotment] (response s reports).plant :=
  cycle_is_executable _ _ (charge_supported s 3 hs hm).1

inductive JointEvent where
  | investigate : Event → JointEvent
  | withdraw
  | respond : Nat → Nat → (Fin 3 → Option Bool) → JointEvent

def jointProcess : Generative.Process State JointEvent where
  step s event t := match event with
    | .investigate event => process.step s event t
    | .withdraw => Supported s ∧ s.held = none ∧ Full s ∧ t = withdrawn s
    | .respond d bad reports => Supported s ∧ s.held = none ∧ 14 ≤ s.plant.body.material ∧
        d ≤ s.reach ∧ responseLaw s d bad reports ∧ t = response s reports

theorem joint_step_preserves (s t : State) (event : JointEvent)
    (hs : Invariant s) (step : jointProcess.step s event t) : Invariant t := by
  cases event with
  | investigate event => exact step_preserves _ _ _ hs step
  | withdraw => obtain ⟨_,_,full,rfl⟩ := step; exact withdrawal_preserves s hs full
  | respond d bad reports =>
    obtain ⟨_,_,hm,covered,law,rfl⟩ := step
    exact response_preserves s d bad reports hs covered law hm

theorem joint_trace_preserves (s t : State) (events : List JointEvent)
    (hs : Invariant s) (tr : Generative.Trace jointProcess s events t) : Invariant t := by
  induction tr with
  | nil => exact hs
  | cons step _ ih => exact ih (joint_step_preserves _ _ _ hs step)

theorem lift_investigation (s t : State) (events : List Event) (tr : Generative.Trace process s events t) :
    Generative.Trace jointProcess s (events.map JointEvent.investigate) t := by
  induction tr with
  | nil => exact .nil _
  | cons step _ ih => exact .cons step ih

def initial (a : Tower) : State := ⟨warmStart,a,0,0,fun _ => none,none⟩
theorem initial_invariant (a : Tower) : Invariant (initial a) := by
  refine ⟨warm_start_supported,?_⟩
  intro i row h
  contradiction

def separatedTower : Tower := ⟨TestingReorganization.triple 0 1 2,fun _ x => x⟩
def hiddenAfter (n : Nat) : Tower :=
  ⟨TestingReorganization.triple 0 1 2,fun k x => if k < n then x else 0⟩

theorem separated_roots (n : Nat) : roots separatedTower n = TestingReorganization.triple 0 1 2 := by
  induction n with
  | zero => rfl
  | succ n ih => exact ih

theorem hidden_prefix (n k : Nat) (hk : k ≤ n) :
    roots (hiddenAfter n) k = TestingReorganization.triple 0 1 2 := by
  induction k with
  | zero => rfl
  | succ k ih =>
    have hkn : k < n := by omega
    funext i
    simp [roots,hiddenAfter,hkn]
    exact congrFun (ih (by omega)) i

theorem hidden_next (n : Nat) : roots (hiddenAfter n) (n+1) = fun _ => 0 := by
  funext i
  simp [roots,hiddenAfter]

def recordThrough (a : Tower) (n : Nat) : Fin (n+1) → Fin 3 → Fin 3 → Bool :=
  fun k => CommonCauseDiscovery.coupling (roots a k.val)

theorem every_finite_record_has_hidden_extension (n : Nat) :
    recordThrough separatedTower n = recordThrough (hiddenAfter n) n := by
  funext k i j
  have hk : k.val ≤ n := by omega
  simp [recordThrough,separated_roots,hidden_prefix n k.val hk]

theorem hidden_extension_changes_failure (n : Nat) :
    TestingReorganization.Diverse (roots separatedTower (n+1)) ∧
    ¬TestingReorganization.Diverse (roots (hiddenAfter n) (n+1)) := by
  rw [separated_roots,hidden_next]
  decide

theorem no_finite_certificate_of_unrestricted_separation (n : Nat)
    (certify : (Fin (n+1) → Fin 3 → Fin 3 → Bool) → Bool) :
    ¬(certify (recordThrough separatedTower n) = true ∧
      ∀ a : Tower, certify (recordThrough a n) = true →
        ∀ d, TestingReorganization.Diverse (roots a d)) := by
  intro h
  have cert : certify (recordThrough (hiddenAfter n) n) = true := by
    rw [← every_finite_record_has_hidden_extension n]
    exact h.1
  exact (hidden_extension_changes_failure n).2 (h.2 (hiddenAfter n) cert (n+1))

theorem continued_expansion_exposes_each_hidden_level (n : Nat) :
    CommonCauseDiscovery.decode (rounds (initial (hiddenAfter n)) (n+1)).rows 0 1 = true ∧
    ∀ reports v, ¬gate (rounds (initial (hiddenAfter n)) (n+1)) reports v := by
  have row := acquired_at_reach (initial (hiddenAfter n)) n 0
  have effect : CommonCauseDiscovery.decode (rounds (initial (hiddenAfter n)) (n+1)).rows 0 1 = true := by
    unfold CommonCauseDiscovery.decode
    rw [row]
    simp [initial,hidden_next,CommonCauseDiscovery.coupling]
  refine ⟨effect,?_⟩
  intro reports v h
  have hh := h.2.2.1 0 1
  change CommonCauseDiscovery.decode (rounds (initial (hiddenAfter n)) (n+1)).rows 0 1 = false at hh
  rw [effect] at hh
  contradiction

def commonStart : State := initial (hiddenAfter 0)
def exposed : State := round commonStart
def decisionPoint : State := withdrawn exposed
def allYes : Fin 3 → Option Bool := fun _ => some true

theorem broader_test_changes_admission :
    gate (survey commonStart) allYes true ∧ ¬gate exposed allYes true := by
  constructor
  · unfold gate CommonCauseDiscovery.gate CommonCauseDiscovery.Complete CommonCauseDiscovery.Separating
    decide
  · intro h
    have hh := h.2.2.1 0 1
    change true = false at hh
    contradiction

theorem expansion_to_response_is_actual :
    Generative.Trace jointProcess commonStart
      (roundEvents.map JointEvent.investigate ++ [.withdraw,.respond 1 0 allYes])
      (response decisionPoint allYes) := by
  have hs := initial_invariant (hiddenAfter 0)
  have tr := round_actual commonStart hs rfl
  have tested := trace_preserves _ _ _ hs tr
  have full : Full exposed := by unfold Full; decide
  have ready := withdrawal_preserves exposed tested full
  exact Generative.trace_append_iff.mpr ⟨_,lift_investigation _ _ _ tr,
    .cons ⟨tested.1,rfl,full,rfl⟩ (.cons ⟨ready.1,rfl,by decide,by decide,
      by unfold responseLaw; decide,rfl⟩ (.nil _))⟩

theorem actual_corrective_effect :
    choice decisionPoint allYes = .separate ∧
    (response decisionPoint allYes).plant.body.stock = four 3 3 3 3 ∧
    ¬Established (cycle decisionPoint.plant .broken) := by
  refine ⟨by decide,?_,?_⟩
  · funext i
    have hi : i = 0 ∨ i = 1 ∨ i = 2 ∨ i = 3 := by omega
    rcases hi with rfl | rfl | rfl | rfl <;> decide
  · intro h
    have hh := (h 0).1
    change 2 ≤ 1 at hh
    omega

theorem exhausted_margin_blocks_pulse :
    ¬Generative.Enabled process decisionPoint (.pulse 0) := by
  rintro ⟨t,h⟩
  have hh := h.2.2.1 0
  change 2 = 3 at hh
  contradiction

def RecoveryReserve (s : State) : Prop := s.held.isSome = true → 12 ≤ s.plant.body.material

theorem step_retains_restoration_reserve (s t : State) (event : Event)
    (step : process.step s event t) : RecoveryReserve t := by
  cases event with
  | work =>
    obtain ⟨_,idle,rfl⟩ := step
    intro h
    change s.held.isSome = true at h
    simp [idle] at h
  | fabricate =>
    obtain ⟨_,idle,_,rfl⟩ := step
    intro h
    change s.held.isSome = true at h
    simp [idle] at h
  | extend =>
    obtain ⟨_,idle,_,_,rfl⟩ := step
    intro h
    change s.held.isSome = true at h
    simp [idle] at h
  | pulse i =>
    obtain ⟨_,_,_,hm,rfl⟩ := step
    intro _
    change 12 ≤ s.plant.body.material-1
    omega
  | observe =>
    obtain ⟨_,_,_,hm,rfl⟩ := step
    intro _
    change 12 ≤ s.plant.body.material-1
    omega
  | restore =>
    obtain ⟨_,_,_,rfl⟩ := step
    intro h
    contradiction

theorem trace_retains_restoration_reserve (s t : State) (events : List Event)
    (initialReserve : RecoveryReserve s) (tr : Generative.Trace process s events t) : RecoveryReserve t := by
  induction tr with
  | nil => exact initialReserve
  | cons step _ ih => exact ih (step_retains_restoration_reserve _ _ _ step)

theorem interrupted_history_can_restore (s t : State) (events : List Event) (i : Fin 3)
    (hs : Invariant s) (reserve : RecoveryReserve s) (tr : Generative.Trace process s events t)
    (held : t.held = some i) : Generative.Enabled process t .restore := by
  have ht := trace_preserves _ _ _ hs tr
  have hr := trace_retains_restoration_reserve _ _ _ reserve tr
  have hx : t.held.isSome = true := by simp [held]
  exact ⟨restored t,ht.1,hx,hr hx,rfl⟩

def thinReserve : State :=
  {initial separatedTower with plant := {warmStart with body := {warmStart.body with material := 12}}}

theorem unreserved_pulse_would_strand_restoration :
    Supported (pulsed thinReserve 0) ∧
    ¬Generative.Enabled process (pulsed thinReserve 0) .restore ∧
    ¬Generative.Enabled process thinReserve (.pulse 0) := by
  refine ⟨?_,?_,?_⟩
  · unfold Supported Equipped Established
    decide
  · rintro ⟨t,h⟩
    have hh := h.2.2.1
    change 12 ≤ 11 at hh
    omega
  · rintro ⟨t,h⟩
    have hh := h.2.2.2.1
    change 14 ≤ 12 at hh
    omega

end ExpandingInquiry
