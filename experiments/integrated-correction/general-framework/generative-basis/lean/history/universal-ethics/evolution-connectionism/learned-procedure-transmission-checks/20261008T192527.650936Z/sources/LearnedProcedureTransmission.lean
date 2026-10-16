import CalibrationRenewal

/-!
# Executed learning, supported reconstruction, and successor use

One finite history differentiates task performance, retained records, an updater
apparatus and reconstruction. Successful task performance, not a type label,
converts supplied support into support available for reconstruction. The actual
retained matrix and procedure bit are reconstructed and used by successors.

Supplied local recipes: 9 matrix-record cells, 4 apparatus components, 9 record
writes + the existing 10-step apparatus construction + 1 procedure-bit setting.
Thus each successor uses 13 precursor and 20 support units. These are model
units and explicit conversion laws, not universal physical prices. Copying is
exact, channels are affine, and each family is homogeneous. The two procedures
and reconstruction protocol are not invented or evolved in this module.
-/

noncomputable section

namespace LearnedProcedureTransmission
open ConnectionistRecovery DevelopmentalMemory UpdaterConsequences CalibratedUpdater

def coordinates : List (Fin 3 × Fin 3) :=
  [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]

def writeCell (B copy : Network 3) (p : Fin 3 × Fin 3) : Network 3 :=
  Function.update copy p.1 (Function.update (copy p.1) p.2 (B p.1 p.2))

def copyMatrix (B : Network 3) : Network 3 :=
  coordinates.foldl (writeCell B) (fun _ _ => 0)

theorem copy_matrix_exact (B : Network 3) : copyMatrix B = B := by
  funext i j
  fin_cases i <;> fin_cases j <;>
    norm_num [copyMatrix,coordinates,List.foldl,writeCell,Function.update,Fin.ext_iff]

structure Kit where
  network : Network 3
  apparatus : Apparatus

def construct (channels : Fin 3 → Channel) (B : Network 3) (procedure : Bool) : Kit :=
  ⟨copyMatrix B, { build channels (blank 10 4) with inhibit := procedure }⟩

theorem constructed_record (channels : Fin 3 → Channel) (B : Network 3) (p : Bool) :
    (construct channels B p).network = B := copy_matrix_exact B

theorem constructed_procedure (channels : Fin 3 → Channel) (B : Network 3) (p : Bool) :
    (construct channels B p).apparatus.inhibit = p := rfl

theorem constructed_responsive (channels : Fin 3 → Channel)
    (hg : ∀ i, (channels i).gain ≠ 0) (B : Network 3) (tasks : List Task) :
    nativeRun (construct channels B true).apparatus channels
      (construct channels B true).network tasks = run .responsive B tasks := by
  simp only [construct, acquired_assembly, copy_matrix_exact]
  exact formed_run_responsive channels hg B tasks

theorem no_inhibitor_run (h : Apparatus) (channels : Fin 3 → Channel)
    (hi : h.inhibit = false) (B : Network 3) (tasks : List Task) :
    nativeRun h channels B tasks = run .continual B tasks := by
  induction tasks generalizing B with
  | nil => rfl
  | cons t rest ih => simp [nativeRun,run,no_inhibitor_continual h channels hi,ih]

theorem constructed_continual (channels : Fin 3 → Channel)
    (B : Network 3) (tasks : List Task) :
    nativeRun (construct channels B false).apparatus channels
      (construct channels B false).network tasks = run .continual B tasks := by
  rw [constructed_record]
  exact no_inhibitor_run _ channels rfl B tasks

structure State where
  kit : Kit
  active : Nat
  retired : Nat
  precursor : Nat
  source : Nat
  available : Nat
  spent : Nat
  waste : Nat
  tested : Bool

def material (s : State) : Nat := s.precursor + 13*(s.active+s.retired)
def support (s : State) : Nat := s.source+s.available+s.spent+s.waste

def expose (channels : Fin 3 → Channel) (tasks : List Task) (s : State) : Option State :=
  let demand := s.active*tasks.length
  if s.tested = false ∧ 0 < s.active ∧ demand ≤ s.source then
    let result := nativeRun s.kit.apparatus channels s.kit.network tasks
    some { s with kit := { s.kit with network := result.1 }
                  source := s.source-demand
                  available := s.available+s.active*result.2
                  waste := s.waste+(demand-s.active*result.2)
                  tested := true }
  else none

def capacity (s : State) : Nat := min (s.precursor/13) (s.available/20)

inductive Transfer where
  | faithful
  | procedureLoss
  | recordLoss
  deriving DecidableEq

def inheritedProcedure (t : Transfer) (s : State) : Bool :=
  match t with
  | .procedureLoss => false
  | _ => s.kit.apparatus.inhibit

def inheritedRecord (t : Transfer) (s : State) : Network 3 :=
  match t with
  | .recordLoss => fun _ _ => 0
  | _ => s.kit.network

def reconstruct (channels : Fin 3 → Channel) (t : Transfer) (s : State) : Option State :=
  let count := capacity s
  if s.tested = true ∧ 0 < count then
    some { s with kit := construct channels (inheritedRecord t s) (inheritedProcedure t s)
                  active := count
                  retired := s.retired+s.active
                  precursor := s.precursor-13*count
                  available := s.available-20*count
                  spent := s.spent+20*count
                  tested := false }
  else none

theorem capacity_bounds (s : State) :
    13*capacity s ≤ s.precursor ∧ 20*capacity s ≤ s.available := by
  unfold capacity
  omega

theorem capacity_maximal (s : State) (n : Nat)
    (hm : 13*n ≤ s.precursor) (hs : 20*n ≤ s.available) : n ≤ capacity s := by
  unfold capacity
  omega

theorem exposed_accounts {channels : Fin 3 → Channel} {tasks : List Task} {s out : State}
    (actual : expose channels tasks s = some out) :
    material out = material s ∧ support out = support s := by
  have hb := Nat.mul_le_mul_left s.active (native_run_bound s.kit.apparatus channels s.kit.network tasks)
  unfold expose at actual
  dsimp only at actual
  split at actual
  · rename_i enabled
    cases Option.some.inj actual
    dsimp [material,support]
    constructor <;> omega
  · cases actual

theorem reconstructed_accounts {channels : Fin 3 → Channel} {t : Transfer} {s out : State}
    (actual : reconstruct channels t s = some out) :
    material out = material s ∧ support out = support s ∧ out.active = capacity s := by
  have hb := capacity_bounds s
  unfold reconstruct at actual
  dsimp only at actual
  split at actual
  · rename_i enabled
    cases Option.some.inj actual
    dsimp [material,support]
    omega
  · cases actual

theorem reconstructed_record_enters_use {channels : Fin 3 → Channel} {s out : State}
    (actual : reconstruct channels .faithful s = some out) :
    out.kit.network = s.kit.network ∧
    out.kit.apparatus.inhibit = s.kit.apparatus.inhibit := by
  unfold reconstruct at actual
  dsimp only at actual
  split at actual
  · cases Option.some.inj actual
    exact ⟨constructed_record _ _ _,rfl⟩
  · cases actual

def firstSeed (p : Bool) : State :=
  ⟨construct identityChannels (weighted 1 1) p,1,0,130,160,0,0,0,false⟩

def tenCycles : List Task := cycles 10

theorem ten_cycles_length : tenCycles.length = 40 := by decide

theorem initial_both : succeeds (weighted 1 1) .a ∧ succeeds (weighted 1 1) .c := by
  norm_num [succeeds_first_iff,succeeds_second_iff]

theorem executed_parent_returns :
    nativeRun (firstSeed true).kit.apparatus identityChannels
      (firstSeed true).kit.network tenCycles = (weighted 1 1,40) ∧
    nativeRun (firstSeed false).kit.apparatus identityChannels
      (firstSeed false).kit.network tenCycles = (weighted 11 31,30) := by
  constructor
  · rw [firstSeed,constructed_responsive _ (by intro i; norm_num [identityChannels])]
    rw [responsive_stable _ initial_both.1 initial_both.2]
    rfl
  · rw [firstSeed,constructed_continual]
    simpa [tenCycles] using repeated_continual_cycles 10

def parentAfter (p : Bool) : State :=
  { firstSeed p with
    kit := { (firstSeed p).kit with network := if p then weighted 1 1 else weighted 11 31 }
    source := 120
    available := if p then 40 else 30
    waste := if p then 0 else 10
    tested := true }

theorem actual_parent_history (p : Bool) :
    expose identityChannels tenCycles (firstSeed p) = some (parentAfter p) := by
  cases p
  · simp [expose,show (firstSeed false).tested = false by rfl,
      show (firstSeed false).active = 1 by rfl,
      show (firstSeed false).source = 160 by rfl,
      ten_cycles_length,executed_parent_returns.2,parentAfter,firstSeed]
  · simp [expose,show (firstSeed true).tested = false by rfl,
      show (firstSeed true).active = 1 by rfl,
      show (firstSeed true).source = 160 by rfl,
      ten_cycles_length,executed_parent_returns.1,parentAfter,firstSeed]

def daughterState (p : Bool) (t : Transfer) : State :=
  let s := parentAfter p
  { s with kit := construct identityChannels (inheritedRecord t s) (inheritedProcedure t s)
           active := if p then 2 else 1
           retired := 1
           precursor := if p then 104 else 117
           available := if p then 0 else 10
           spent := if p then 40 else 20
           tested := false }

theorem actual_reconstruction (p : Bool) (t : Transfer) :
    reconstruct identityChannels t (parentAfter p) = some (daughterState p t) := by
  cases p <;> simp [reconstruct,capacity,parentAfter,firstSeed,daughterState]

theorem both_reconstruct_and_counts_differ :
    (daughterState true .faithful).active = 2 ∧
    (daughterState false .faithful).active = 1 ∧
    0 < (daughterState false .faithful).active := by decide

theorem actual_successor_use :
    nativeRun (daughterState true .faithful).kit.apparatus identityChannels
      (daughterState true .faithful).kit.network cycle = (weighted 1 1,4) ∧
    nativeRun (daughterState false .faithful).kit.apparatus identityChannels
      (daughterState false .faithful).kit.network cycle = (weighted 12 34,3) := by
  constructor
  · change nativeRun (construct identityChannels (weighted 1 1) true).apparatus identityChannels
      (construct identityChannels (weighted 1 1) true).network cycle = _
    rw [constructed_responsive _ (by intro i; norm_num [identityChannels]),
      responsive_stable _ initial_both.1 initial_both.2]
    rfl
  · change nativeRun (construct identityChannels (weighted 11 31) false).apparatus identityChannels
      (construct identityChannels (weighted 11 31) false).network cycle = _
    rw [constructed_continual]
    simpa using continual_cycle 10

theorem procedure_conversion_changes_next_use :
    (daughterState true .procedureLoss).active = 2 ∧
    nativeRun (daughterState true .procedureLoss).kit.apparatus identityChannels
      (daughterState true .procedureLoss).kit.network cycle = (weighted 2 4,3) := by
  constructor
  · rfl
  · change nativeRun (construct identityChannels (weighted 1 1) false).apparatus identityChannels
      (construct identityChannels (weighted 1 1) false).network cycle = _
    rw [constructed_continual]
    simpa using continual_cycle 0

theorem erased_record_changes_first_use :
    (daughterState true .recordLoss).active = 2 ∧
    ¬ succeeds (daughterState true .recordLoss).kit.network .a ∧
    succeeds (daughterState true .faithful).kit.network .a := by
  have zeroFails : ¬ succeeds (weighted 0 0) .a := by norm_num [succeeds_first_iff]
  have hz : (fun _ _ => (0:ℝ)) = weighted 0 0 := by funext i j; simp [weighted]
  simp only [daughterState,parentAfter,firstSeed,inheritedRecord,inheritedProcedure,
    ↓reduceIte,construct,copy_matrix_exact]
  exact ⟨rfl,hz ▸ zeroFails,initial_both.1⟩

theorem support_or_material_blocks :
    reconstruct identityChannels .faithful { parentAfter true with available := 19 } = none ∧
    reconstruct identityChannels .faithful { parentAfter true with precursor := 12 } = none := by
  simp [reconstruct,capacity]

theorem exhausted_source_blocks (channels : Fin 3 → Channel) (tasks : List Task) (s : State)
    (h : s.source < s.active*tasks.length) : expose channels tasks s = none := by
  simp [expose,show ¬ s.active*tasks.length ≤ s.source by omega]

theorem unchanged_task_no_return_advantage :
    nativeRun (firstSeed true).kit.apparatus identityChannels
      (firstSeed true).kit.network [.c,.c,.c,.c] |>.2 = 4 := by
  rw [firstSeed,constructed_responsive _ (by intro i; norm_num [identityChannels])]
  exact unchanged_context_no_return_gain.2

theorem future_channel_change_blocks_repair :
    let child := construct identityChannels (weighted 1 4) true
    nativeUpdate child.apparatus changedChannels child.network .a = weighted 1 4 ∧
      ¬ succeeds child.network .a := by
  simp only [construct, acquired_assembly, copy_matrix_exact]
  exact stale_channel_blocks_actual_repair

end LearnedProcedureTransmission
