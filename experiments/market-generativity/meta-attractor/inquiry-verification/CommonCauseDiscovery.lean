import TestingReorganization

/-! Intervention effects acquire a dependency partition without reading root
identities. Selective delivered pulses, faithful outage observation and stable
coupling during a trial are local laws. Upstream causes outside that intervention
class remain a separate coverage question. -/
namespace CommonCauseDiscovery
open ReproductionNetwork
set_option autoImplicit false

def coupling (roots : Fin 3 → Nat) (i j : Fin 3) : Bool := decide (roots j = roots i)
def decode (rows : Fin 3 → Option (Fin 3 → Bool)) (i : Fin 3) : Fin 3 → Bool :=
  (rows i).getD (fun _ => true)
def Complete (rows : Fin 3 → Option (Fin 3 → Bool)) : Prop := ∀ i, (rows i).isSome = true
instance decidableComplete (rows : Fin 3 → Option (Fin 3 → Bool)) : Decidable (Complete rows) :=
  inferInstanceAs (Decidable (∀ i, (rows i).isSome = true))
def Separating (rows : Fin 3 → Option (Fin 3 → Bool)) : Prop :=
  ∀ i j, decode rows i j = decide (j = i)
instance decidableSeparating (rows : Fin 3 → Option (Fin 3 → Bool)) : Decidable (Separating rows) :=
  inferInstanceAs (Decidable (∀ i j, decode rows i j = decide (j = i)))

structure State where
  plant : Installation
  roots : Fin 3 → Nat
  rows : Fin 3 → Option (Fin 3 → Bool)
  held : Option (Fin 3)
  revision : Nat

def Supported (s : State) : Prop := Equipped s.plant ∧ Established s.plant
def SoundRows (s : State) : Prop := ∀ i row, s.rows i = some row → row = coupling s.roots i
def Invariant (s : State) : Prop := Supported s ∧ SoundRows s

def online (s : State) (j : Fin 3) : Bool := match s.held with
  | none => true
  | some i => !(coupling s.roots i j)
def charge (s : State) (n : Nat) : State :=
  {s with plant := {s.plant with body := {s.plant.body with material := s.plant.body.material-n}}}
def started (s : State) (i : Fin 3) : State := {charge s 1 with held := some i}
def observed (s : State) (i : Fin 3) : State :=
  {charge s 1 with rows := TestingReorganization.put s.rows i (some (fun j => !(online s j)))}
def restored (s : State) : State := {charge s 1 with held := none}
def worked (s : State) : State := {s with plant := cycle s.plant .separate}
def changed (s : State) (roots : Fin 3 → Nat) : State :=
  {charge s 2 with roots := roots, rows := fun _ => none, held := none, revision := s.revision+1}

inductive Event where
  | pulse : Fin 3 → Event
  | observe
  | restore
  | work
  | change : (Fin 3 → Nat) → Event

def process : Generative.Process State Event where
  step s event t := Supported s ∧ match event with
    | .pulse i => s.held = none ∧ 12 ≤ s.plant.body.material ∧ t = started s i
    | .observe => ∃ i, s.held = some i ∧ 12 ≤ s.plant.body.material ∧ t = observed s i
    | .restore => s.held.isSome = true ∧ 12 ≤ s.plant.body.material ∧ t = restored s
    | .work => t = worked s
    | .change roots => s.held = none ∧ 13 ≤ s.plant.body.material ∧ t = changed s roots

theorem charge_supported (s : State) (n : Nat) (hs : Supported s)
    (hm : 11+n ≤ s.plant.body.material) : Supported (charge s n) := by
  refine ⟨⟨hs.1.1,?_⟩,hs.2⟩
  change 11 ≤ s.plant.body.material-n
  omega

theorem work_supported (s : State) (hs : Supported s) : Supported (worked s) :=
  ⟨cycle_equipped _ _ hs.1,cycle_established _ _ hs.2 (by decide)⟩

theorem observation_is_effect (s : State) (i : Fin 3) (hi : s.held = some i) :
    (fun j => !(online s j)) = coupling s.roots i := by
  funext j
  simp [online,hi]

theorem observation_preserves_rows (s : State) (i : Fin 3)
    (hi : s.held = some i) (hr : SoundRows s) : SoundRows (observed s i) := by
  intro j row h
  by_cases he : j = i
  · subst j
    have hh : (fun j => !(online s j)) = row := by simpa [observed,TestingReorganization.put] using h
    exact hh.symm.trans (observation_is_effect s i hi)
  · exact hr j row (by simpa [observed,TestingReorganization.put,he] using h)

theorem change_invalidates_records (s : State) (roots : Fin 3 → Nat) :
    SoundRows (changed s roots) ∧ ¬Complete (changed s roots).rows := by
  constructor
  · intro i row h
    contradiction
  · intro h
    have hh := h 0
    contradiction

theorem step_preserves (s t : State) (event : Event)
    (hs : Invariant s) (step : process.step s event t) : Invariant t := by
  cases event with
  | pulse i =>
    obtain ⟨_,_,hm,rfl⟩ := step
    exact ⟨charge_supported s 1 hs.1 hm,hs.2⟩
  | observe =>
    obtain ⟨_,i,hi,hm,rfl⟩ := step
    exact ⟨charge_supported s 1 hs.1 hm,observation_preserves_rows s i hi hs.2⟩
  | restore =>
    obtain ⟨_,_,hm,rfl⟩ := step
    exact ⟨charge_supported s 1 hs.1 hm,hs.2⟩
  | work =>
    obtain ⟨_,rfl⟩ := step
    exact ⟨work_supported s hs.1,hs.2⟩
  | change roots =>
    obtain ⟨_,_,hm,rfl⟩ := step
    exact ⟨charge_supported s 2 hs.1 hm,(change_invalidates_records s roots).1⟩

theorem trace_preserves (s t : State) (events : List Event)
    (hs : Invariant s) (tr : Generative.Trace process s events t) : Invariant t := by
  induction tr with
  | nil => exact hs
  | cons step _ ih => exact ih (step_preserves _ _ _ hs step)

theorem complete_records_identify_coupling (s : State) (hr : SoundRows s) (hc : Complete s.rows) :
    decode s.rows = coupling s.roots := by
  funext i
  have hh := hc i
  cases he : s.rows i with
  | none => simp [he] at hh
  | some row => simpa [decode,he] using hr i row he

theorem separate_effects_imply_distinct_roots (s : State)
    (hr : SoundRows s) (hc : Complete s.rows) (hs : Separating s.rows) :
    TestingReorganization.Diverse s.roots := by
  have he := complete_records_identify_coupling s hr hc
  have h01 := hs 0 1
  have h02 := hs 0 2
  have h12 := hs 1 2
  rw [he] at h01 h02 h12
  simp only [coupling,show (1 : Fin 3) ≠ 0 by decide,show (2 : Fin 3) ≠ 0 by decide,
    show (2 : Fin 3) ≠ 1 by decide,decide_false,decide_eq_false_iff_not] at h01 h02 h12
  exact ⟨Ne.symm h01,Ne.symm h02,Ne.symm h12⟩

def gate (s : State) (reports : Fin 3 → Option Bool) (v : Bool) : Prop :=
  s.held = none ∧ Complete s.rows ∧ Separating s.rows ∧ TestingReorganization.Agrees reports v
instance decidableGate (s : State) (reports : Fin 3 → Option Bool) (v : Bool) : Decidable (gate s reports v) :=
  inferInstanceAs (Decidable (_ ∧ Complete s.rows ∧ Separating s.rows ∧ _))

theorem learned_gate_sound (s : State) (reports : Fin 3 → Option Bool) (actual v : Bool)
    (bad : Nat) (hr : SoundRows s)
    (honest : ∀ i, s.roots i ≠ bad → reports i = some v → v = actual)
    (hg : gate s reports v) : v = actual :=
  TestingReorganization.agreement_sound s.roots reports actual v bad
    (separate_effects_imply_distinct_roots s hr hg.2.1 hg.2.2.1) honest hg.2.2.2

theorem learned_gate_available (s : State) (reports : Fin 3 → Option Bool)
    (actual : Bool) (bad : Nat) (hr : SoundRows s) (hc : Complete s.rows)
    (separated : Separating s.rows) (idle : s.held = none)
    (respond : ∀ i, s.roots i ≠ bad → reports i = some actual) : gate s reports actual :=
  ⟨idle,hc,separated,TestingReorganization.agreement_available _ _ _ _
    (separate_effects_imply_distinct_roots s hr hc separated) respond⟩

theorem no_gate_after_change (s : State) (roots : Fin 3 → Nat)
    (reports : Fin 3 → Option Bool) (v : Bool) : ¬gate (changed s roots) reports v :=
  fun hg => (change_invalidates_records s roots).2 hg.2.1

theorem no_gate_during_pulse (s : State) (i : Fin 3) (reports : Fin 3 → Option Bool) (v : Bool) :
    ¬gate (started s i) reports v := by
  intro h
  have := h.1
  contradiction

theorem fallback_available_during_probe (s : State) (hs : Supported s) :
    Generative.Enabled process s .work ∧
    Generative.Trace changingProcess s.plant [.revise .separate,.operate allotment] (worked s).plant :=
  ⟨⟨worked s,hs,rfl⟩,cycle_is_executable s.plant .separate hs.1⟩

def finishedProbe (s : State) (i : Fin 3) : State := restored (observed (started s i) i)

theorem probe_completes (s : State) (i : Fin 3) (hs : Supported s)
    (idle : s.held = none) (hm : 14 ≤ s.plant.body.material) :
    Generative.Trace process s [.pulse i,.observe,.restore] (finishedProbe s i) := by
  have hp : Supported (started s i) := charge_supported s 1 hs (by omega)
  have ho : Supported (observed (started s i) i) :=
    charge_supported (started s i) 1 hp (by change 12 ≤ s.plant.body.material-1; omega)
  refine .cons ⟨hs,idle,by omega,rfl⟩ (.cons ⟨hp,i,rfl,?_,rfl⟩ (.cons ⟨ho,rfl,?_,rfl⟩ (.nil _)))
  · change 12 ≤ s.plant.body.material-1
    omega
  · change 12 ≤ s.plant.body.material-1-1
    omega

theorem completed_probe_records_effect (s : State) (i : Fin 3) :
    (finishedProbe s i).rows = TestingReorganization.put s.rows i (some (coupling s.roots i)) ∧
    (finishedProbe s i).held = none ∧ (finishedProbe s i).roots = s.roots ∧
    (finishedProbe s i).plant.body.material = s.plant.body.material-3 := by
  refine ⟨?_,rfl,rfl,?_⟩
  · funext j
    simp [finishedProbe,restored,observed,started,online,charge]
  · change s.plant.body.material-1-1-1 = s.plant.body.material-3
    omega

theorem work_finances_probe (s : State) (hs : Supported s) :
    s.plant.body.material+2 ≤ (worked s).plant.body.material := by
  have hd := demand_bound (arrangement .separate) s.plant.body.stock
  have hx : maximumDemand (arrangement .separate) = 8 := by decide
  rw [hx] at hd
  have hm := hs.1.2
  change s.plant.body.material+2 ≤ s.plant.body.material-1-demand (arrangement .separate) s.plant.body.stock+11
  omega

def financedProbe (s : State) (i : Fin 3) : State := finishedProbe (worked (worked s)) i

theorem financed_probe_actual (s : State) (i : Fin 3) (hs : Supported s) (idle : s.held = none) :
    Generative.Trace process s [.work,.work,.pulse i,.observe,.restore] (financedProbe s i) := by
  have h1 := work_finances_probe s hs
  have hw := work_supported s hs
  have h2 := work_finances_probe (worked s) hw
  have hm := hs.1.2
  exact .cons ⟨hs,rfl⟩ (.cons ⟨hw,rfl⟩ (probe_completes _ i (work_supported _ hw) idle (by omega)))

theorem financed_probe_retains_capacity (s : State) (i : Fin 3) (hs : Supported s) :
    s.plant.body.material+1 ≤ (financedProbe s i).plant.body.material := by
  have h1 := work_finances_probe s hs
  have h2 := work_finances_probe (worked s) (work_supported s hs)
  have ha := (completed_probe_records_effect (worked (worked s)) i).2.2.2
  change s.plant.body.material+1 ≤ (finishedProbe (worked (worked s)) i).plant.body.material
  omega

def probeEvents (i : Fin 3) : List Event := [.work,.work,.pulse i,.observe,.restore]
def survey (s : State) : State := financedProbe (financedProbe (financedProbe s 0) 1) 2
def surveyEvents : List Event := probeEvents 0 ++ probeEvents 1 ++ probeEvents 2

theorem survey_actual (s : State) (hs : Invariant s) (idle : s.held = none) :
    Generative.Trace process s surveyEvents (survey s) := by
  have tr0 := financed_probe_actual s 0 hs.1 idle
  have inv0 := trace_preserves _ _ _ hs tr0
  have tr1 := financed_probe_actual (financedProbe s 0) 1 inv0.1 rfl
  have inv1 := trace_preserves _ _ _ inv0 tr1
  have tr2 := financed_probe_actual (financedProbe (financedProbe s 0) 1) 2 inv1.1 rfl
  exact Generative.trace_append_iff.mpr
    ⟨_,Generative.trace_append_iff.mpr ⟨_,tr0,tr1⟩,tr2⟩

theorem survey_records_all_effects (s : State) :
    ∀ i, (survey s).rows i = some (coupling s.roots i) := by
  intro i
  have hi : i = 0 ∨ i = 1 ∨ i = 2 := by omega
  rcases hi with rfl | rfl | rfl <;>
    simp [survey,financedProbe,finishedProbe,restored,observed,started,worked,charge,online,TestingReorganization.put]

theorem survey_complete (s : State) : Complete (survey s).rows := by
  intro i
  rw [survey_records_all_effects s i]
  rfl

theorem survey_preserves_response_capacity (s : State) (hs : Invariant s) (idle : s.held = none) :
    Invariant (survey s) ∧ (survey s).held = none ∧
    s.plant.body.material+3 ≤ (survey s).plant.body.material := by
  have tr0 := financed_probe_actual s 0 hs.1 idle
  have inv0 := trace_preserves _ _ _ hs tr0
  have tr1 := financed_probe_actual (financedProbe s 0) 1 inv0.1 rfl
  have inv1 := trace_preserves _ _ _ inv0 tr1
  have a := financed_probe_retains_capacity s 0 hs.1
  have b := financed_probe_retains_capacity (financedProbe s 0) 1 inv0.1
  have c := financed_probe_retains_capacity (financedProbe (financedProbe s 0) 1) 2 inv1.1
  exact ⟨trace_preserves _ _ _ hs (survey_actual s hs idle),rfl,by change _ ≤ (financedProbe (financedProbe (financedProbe s 0) 1) 2).plant.body.material; omega⟩

def initial (roots : Fin 3 → Nat) : State := ⟨warmStart,roots,fun _ => none,none,0⟩

theorem initial_invariant (roots : Fin 3 → Nat) : Invariant (initial roots) := by
  refine ⟨warm_start_supported,?_⟩
  intro i row h
  contradiction

def distinct : State := initial (TestingReorganization.triple 0 1 2)
def merged : State := initial (TestingReorganization.triple 0 0 2)

theorem effect_probe_discovers_shared_dependency :
    decode (survey merged).rows 0 1 = true ∧
    decode (survey distinct).rows 0 1 = false ∧
    ¬Separating (survey merged).rows ∧ Separating (survey distinct).rows := by decide

theorem merged_readers_actually_fail_together :
    online (started merged 0) 0 = false ∧ online (started merged 0) 1 = false ∧
    online (started merged 0) 2 = true := by decide

theorem no_quorum_claim_from_untested_state (roots : Fin 3 → Nat)
    (reports : Fin 3 → Option Bool) (v : Bool) : ¬gate (initial roots) reports v := by
  intro h
  have hh := h.2.1 0
  contradiction

def safeWithdrawal (s : State) : Bool := decide (∀ i : Fin 4, 3 ≤ s.plant.body.stock i)
def responseLaw (s : State) (reports : Fin 3 → Option Bool) (bad : Nat) : Prop :=
  ∀ i v, s.roots i ≠ bad → reports i = some v → v = safeWithdrawal s
def choice (s : State) (reports : Fin 3 → Option Bool) : Arrangement :=
  if gate s reports true then .broken else .separate
def response (s : State) (reports : Fin 3 → Option Bool) : State :=
  {charge s 3 with plant := cycle (charge s 3).plant (choice s reports)}

theorem learned_response_preserves (s : State) (reports : Fin 3 → Option Bool) (bad : Nat)
    (hs : Invariant s) (hl : responseLaw s reports bad) (hm : 14 ≤ s.plant.body.material) :
    Invariant (response s reports) := by
  have paid := charge_supported s 3 hs.1 hm
  refine ⟨⟨cycle_equipped _ _ paid.1,?_⟩,hs.2⟩
  change Established (cycle (charge s 3).plant (choice s reports))
  unfold choice
  split
  next hg =>
    have hx : safeWithdrawal s = true :=
      (learned_gate_sound s reports (safeWithdrawal s) true bad hs.2 (fun i hi => hl i true hi) hg).symm
    have hf : ∀ i : Fin 4, 3 ≤ s.plant.body.stock i := by simpa [safeWithdrawal] using hx
    intro i
    rw [AdmissionRevision.broken_stock]
    change 2 ≤ min 3 (s.plant.body.stock i-1) ∧ min 3 (s.plant.body.stock i-1) ≤ 3
    have := hf i
    omega
  next => exact cycle_established _ _ paid.2 (by decide)

theorem learned_response_is_physical (s : State) (reports : Fin 3 → Option Bool)
    (hs : Supported s) (hm : 14 ≤ s.plant.body.material) :
    Generative.Trace changingProcess (charge s 3).plant
      [.revise (choice s reports),.operate allotment] (response s reports).plant :=
  cycle_is_executable _ _ (charge_supported s 3 hs hm).1

def withdrawn (s : State) : State := {s with plant := cycle s.plant .broken}
def decisionPoint (s : State) : State := withdrawn (survey s)
def misleading : Fin 3 → Option Bool :=
  TestingReorganization.corruptedReports (TestingReorganization.triple 0 0 2) 0 false

theorem discovered_coupling_changes_actual_response :
    TestingReorganization.Agrees misleading true ∧
    choice (decisionPoint merged) misleading = .separate ∧
    (response (decisionPoint merged) misleading).plant.body.stock = four 3 3 3 3 := by
  refine ⟨by decide,by decide,?_⟩
  apply funext
  decide

theorem unaccounted_majority_would_lose_support :
    ¬Established (cycle (decisionPoint merged).plant .broken) := by
  intro h
  have hh := (h 0).1
  change 2 ≤ 1 at hh
  omega

theorem retesting_after_reorganization (s : State) (roots : Fin 3 → Nat)
    (hs : Invariant s) (idle : s.held = none) (hm : 13 ≤ s.plant.body.material) :
    Generative.Trace process s (.change roots :: surveyEvents) (survey (changed s roots)) ∧
    Complete (survey (changed s roots)).rows := by
  have step : process.step s (.change roots) (changed s roots) := ⟨hs.1,idle,hm,rfl⟩
  exact ⟨.cons step (survey_actual _ (step_preserves _ _ _ hs step) rfl),survey_complete _⟩

theorem withdrawal_preserves (s : State) (hs : Invariant s) (safe : safeWithdrawal s = true) :
    Invariant (withdrawn s) := by
  have hf : ∀ i : Fin 4, 3 ≤ s.plant.body.stock i := by simpa [safeWithdrawal] using safe
  refine ⟨⟨cycle_equipped _ _ hs.1.1,?_⟩,hs.2⟩
  intro i
  change 2 ≤ (cycle s.plant .broken).body.stock i ∧ (cycle s.plant .broken).body.stock i ≤ 3
  rw [AdmissionRevision.broken_stock]
  have := hf i
  constructor <;> omega

inductive JointEvent where
  | investigate : Event → JointEvent
  | withdraw
  | respond : (Fin 3 → Option Bool) → Nat → JointEvent

def jointProcess : Generative.Process State JointEvent where
  step s event t := match event with
    | .investigate event => process.step s event t
    | .withdraw => Supported s ∧ safeWithdrawal s = true ∧ t = withdrawn s
    | .respond reports bad => Supported s ∧ 14 ≤ s.plant.body.material ∧
        responseLaw s reports bad ∧ t = response s reports

theorem joint_step_preserves (s t : State) (event : JointEvent)
    (hs : Invariant s) (step : jointProcess.step s event t) : Invariant t := by
  cases event with
  | investigate event => exact step_preserves _ _ _ hs step
  | withdraw =>
    obtain ⟨_,safe,rfl⟩ := step
    exact withdrawal_preserves s hs safe
  | respond reports bad =>
    obtain ⟨_,hm,hl,rfl⟩ := step
    exact learned_response_preserves s reports bad hs hl hm

theorem joint_history_preserves (s t : State) (events : List JointEvent)
    (hs : Invariant s) (tr : Generative.Trace jointProcess s events t) : Invariant t := by
  induction tr with
  | nil => exact hs
  | cons step _ ih => exact ih (joint_step_preserves _ _ _ hs step)

theorem investigation_lifts (s t : State) (events : List Event)
    (tr : Generative.Trace process s events t) :
    Generative.Trace jointProcess s (events.map JointEvent.investigate) t := by
  induction tr with
  | nil => exact .nil _
  | cons step _ ih => exact .cons step ih

theorem shared_dependency_to_corrected_response :
    Generative.Trace jointProcess merged
      (surveyEvents.map JointEvent.investigate ++ [.withdraw,.respond misleading 0])
      (response (decisionPoint merged) misleading) := by
  have hs := initial_invariant (TestingReorganization.triple 0 0 2)
  have tr := survey_actual merged hs rfl
  have surveyed := trace_preserves _ _ _ hs tr
  have safe : safeWithdrawal (survey merged) = true := by decide
  have ready := withdrawal_preserves _ surveyed safe
  exact Generative.trace_append_iff.mpr ⟨_,investigation_lifts _ _ _ tr,
    .cons ⟨surveyed.1,safe,rfl⟩
      (.cons ⟨ready.1,by decide,by unfold responseLaw; decide,rfl⟩ (.nil _))⟩

theorem withdrawal_is_physical (s : State) (hs : Supported s) :
    Generative.Trace changingProcess s.plant [.revise .broken,.operate allotment] (withdrawn s).plant :=
  cycle_is_executable _ _ hs.1

structure Layered where
  localRoots : Fin 3 → Nat
  upstream : Nat → Nat

def localEffects (a : Layered) : Fin 3 → Fin 3 → Bool := coupling a.localRoots
def actualRoots (a : Layered) : Fin 3 → Nat := fun i => a.upstream (a.localRoots i)
def separateParents : Layered := ⟨TestingReorganization.triple 0 1 2,id⟩
def sharedParent : Layered := ⟨TestingReorganization.triple 0 1 2,fun _ => 0⟩

theorem all_local_probe_effects_identical : localEffects separateParents = localEffects sharedParent := rfl

theorem local_probe_coverage_misses_upstream_failure :
    TestingReorganization.Diverse (actualRoots separateParents) ∧
    ¬TestingReorganization.Diverse (actualRoots sharedParent) ∧
    TestingReorganization.Agrees
      (TestingReorganization.corruptedReports (actualRoots sharedParent) 0 false) true := by decide

theorem no_classifier_of_local_effects_can_identify_parent
    (classify : (Fin 3 → Fin 3 → Bool) → Bool) :
    ¬(classify (localEffects separateParents) = true ∧
      classify (localEffects sharedParent) = false) := by
  rw [all_local_probe_effects_identical]
  simp

def combinedLocalEffects (a : Layered) (pulses : List (Fin 3)) (j : Fin 3) : Bool :=
  pulses.any (fun i => localEffects a i j)

theorem simultaneous_local_probes_still_miss_parent (pulses : List (Fin 3)) :
    combinedLocalEffects separateParents pulses = combinedLocalEffects sharedParent pulses := rfl

theorem upstream_probe_distinguishes :
    coupling (actualRoots separateParents) 0 1 = false ∧
    coupling (actualRoots sharedParent) 0 1 = true := by decide

end CommonCauseDiscovery
