import GenerativeCore

/-! Conditional return networks. Roles are differentiated activities in one
history. Their capacity to operate depends on stocks maintained by other roles.
All quantities are local material units, not ethical scores. Conversion,
replacement, thresholds and possible interventions remain supplied laws. -/

namespace ReproductionNetwork

def total {ι : Type} : List ι → (ι → Nat) → Nat
  | [], _ => 0
  | i :: rest, f => f i + total rest f

theorem total_mono {ι : Type} (roles : List ι) (f g : ι → Nat)
    (h : ∀ i ∈ roles, f i ≤ g i) : total roles f ≤ total roles g := by
  induction roles with
  | nil => exact Nat.le_refl _
  | cons i rest ih =>
    have hi := h i (by simp)
    have ht := ih (fun j hj => h j (by simp [hj]))
    simp only [total]
    omega

theorem total_add {ι : Type} (roles : List ι) (f g : ι → Nat) :
    total roles (fun i => f i+g i) = total roles f+total roles g := by
  induction roles with
  | nil => rfl
  | cons i rest ih => simp only [total, ih]; omega

theorem total_congr {ι : Type} (roles : List ι) (f g : ι → Nat)
    (h : ∀ i ∈ roles, f i = g i) : total roles f = total roles g := by
  have a := total_mono roles f g (fun i hi => Nat.le_of_eq (h i hi))
  have b := total_mono roles g f (fun i hi => Nat.le_of_eq (h i hi).symm)
  omega

structure Network (ι : Type) where
  roles : List ι
  distinct : roles.Nodup
  threshold : ι → Nat
  wear : ι → Nat
  capacity : ι → Nat
  output : ι → ι → Nat

def incoming {ι : Type} (p : Network ι) (s : ι → Nat) (j : ι) : Nat :=
  total p.roles fun i => if p.threshold i ≤ s i then p.output i j else 0

def advance {ι : Type} (p : Network ι) (s : ι → Nat) (j : ι) : Nat :=
  min (p.capacity j) (s j-p.wear j+incoming p s j)

def minimumIncoming {ι : Type} (p : Network ι) (selected : ι → Bool) (j : ι) : Nat :=
  total p.roles fun i => if selected i then p.output i j else 0

def Box {ι : Type} (p : Network ι) (floor s : ι → Nat) : Prop :=
  ∀ i ∈ p.roles, floor i ≤ s i ∧ s i ≤ p.capacity i

/-- The certificate gives independently checkable amounts and activation
thresholds, rather than assuming preservation of the desired box. -/
structure Maintenance {ι : Type} (p : Network ι) (floor : ι → Nat)
    (selected : ι → Bool) : Prop where
  capacity_sufficient : ∀ j ∈ p.roles, floor j ≤ p.capacity j
  activation : ∀ i ∈ p.roles, selected i = true → p.threshold i ≤ floor i
  returned_amount : ∀ j ∈ p.roles,
    floor j ≤ floor j-p.wear j+minimumIncoming p selected j

theorem return_lower_bound {ι : Type} (p : Network ι) (floor s : ι → Nat)
    (selected : ι → Bool) (hc : Maintenance p floor selected) (hs : Box p floor s)
    (j : ι) : minimumIncoming p selected j ≤ incoming p s j := by
  apply total_mono
  intro i hi
  by_cases h : selected i = true
  · have ht := hc.activation i hi h
    have hl := (hs i hi).1
    have active : p.threshold i ≤ s i := by omega
    simp [h, active]
  · simp [h]

theorem maintenance_step {ι : Type} (p : Network ι) (floor s : ι → Nat)
    (selected : ι → Bool) (hc : Maintenance p floor selected) (hs : Box p floor s) :
    Box p floor (advance p s) := by
  intro j hj
  have hcap := hc.capacity_sufficient j hj
  have hstock := (hs j hj).1
  have hreturn := hc.returned_amount j hj
  have hflow := return_lower_bound p floor s selected hc hs j
  unfold advance
  constructor <;> omega

def stockHistory {ι : Type} (p : Network ι) (s : ι → Nat) : Nat → (ι → Nat)
  | 0 => s
  | t+1 => advance p (stockHistory p s t)

theorem maintenance_history {ι : Type} (p : Network ι) (floor s : ι → Nat)
    (selected : ι → Bool) (hc : Maintenance p floor selected) (hs : Box p floor s)
    (t : Nat) : Box p floor (stockHistory p s t) := by
  induction t with
  | zero => exact hs
  | succ t ih => exact maintenance_step p floor _ selected hc ih

def demand {ι : Type} (p : Network ι) (s : ι → Nat) : Nat :=
  total p.roles (incoming p s)
def maximumDemand {ι : Type} (p : Network ι) : Nat :=
  total p.roles fun j => total p.roles fun i => p.output i j

theorem demand_bound {ι : Type} (p : Network ι) (s : ι → Nat) :
    demand p s ≤ maximumDemand p := by
  apply total_mono
  intro j _
  apply total_mono
  intro i _
  split <;> omega

def worn {ι : Type} (p : Network ι) (s : ι → Nat) (j : ι) : Nat :=
  min (p.wear j) (s j)
def overflow {ι : Type} (p : Network ι) (s : ι → Nat) (j : ι) : Nat :=
  s j-p.wear j+incoming p s j-p.capacity j

theorem coordinate_accounting {ι : Type} (p : Network ι) (s : ι → Nat) (j : ι) :
    advance p s j + worn p s j + overflow p s j = s j+incoming p s j := by
  unfold advance worn overflow
  omega

theorem network_accounting {ι : Type} (p : Network ι) (s : ι → Nat) :
    total p.roles (advance p s) + total p.roles (worn p s) +
      total p.roles (overflow p s) = total p.roles s+demand p s := by
  have h := total_congr p.roles
    (fun j => advance p s j+worn p s j+overflow p s j)
    (fun j => s j+incoming p s j) (fun j _ => coordinate_accounting p s j)
  simp only [total_add] at h
  exact h

structure State (ι : Type) where
  stock : ι → Nat
  generation : Nat
  parts : Nat
  material : Nat

structure Supply where
  parts : Nat
  material : Nat
  deriving DecidableEq, Repr

def Ready {ι : Type} (p : Network ι) (s : State ι) : Prop :=
  0 < p.roles.length ∧ p.roles.length ≤ s.parts ∧ demand p s.stock ≤ s.material

def outcome {ι : Type} (p : Network ι) (a : Supply) (s : State ι) : State ι :=
  { stock := advance p s.stock, generation := s.generation+1,
    parts := s.parts-p.roles.length+a.parts,
    material := s.material-demand p s.stock+a.material }

def process {ι : Type} (p : Network ι) : Generative.Process (State ι) Supply where
  step s a t := Ready p s ∧ t = outcome p a s

theorem full_material_accounting {ι : Type} (p : Network ι) (a : Supply) (s : State ι)
    (hr : Ready p s) :
    total p.roles (outcome p a s).stock + (outcome p a s).material +
      total p.roles (worn p s.stock) + total p.roles (overflow p s.stock) =
      total p.roles s.stock+s.material+a.material := by
  have h := network_accounting p s.stock
  have hfund := hr.2.2
  unfold outcome
  dsimp only
  omega

theorem actual_replacement {ι : Type} (p : Network ι) (a : Supply) (s : State ι)
    (hr : Ready p s) :
    (outcome p a s).parts+p.roles.length=s.parts+a.parts ∧
    (outcome p a s).generation=s.generation+1 := by
  have h := hr.2.1
  unfold outcome
  constructor <;> dsimp only <;> omega

def supplied {ι : Type} (p : Network ι) : Supply := ⟨p.roles.length, maximumDemand p⟩

def Supported {ι : Type} (p : Network ι) (floor : ι → Nat) (s : State ι) : Prop :=
  Box p floor s.stock ∧ 0 < p.roles.length ∧
    p.roles.length ≤ s.parts ∧ maximumDemand p ≤ s.material

theorem supported_ready {ι : Type} (p : Network ι) (floor : ι → Nat) (s : State ι)
    (hs : Supported p floor s) : Ready p s := by
  have h := demand_bound p s.stock
  exact ⟨hs.2.1,hs.2.2.1,by have := hs.2.2.2; omega⟩

theorem supported_step {ι : Type} (p : Network ι) (floor : ι → Nat)
    (selected : ι → Bool) (hc : Maintenance p floor selected) (s : State ι)
    (hs : Supported p floor s) : Supported p floor (outcome p (supplied p) s) := by
  have hb := maintenance_step p floor s.stock selected hc hs.1
  have hd := demand_bound p s.stock
  refine ⟨hb,hs.2.1,?_,?_⟩
  · change p.roles.length ≤ s.parts-p.roles.length+p.roles.length
    have := hs.2.2.1
    omega
  · change maximumDemand p ≤ s.material-demand p s.stock+maximumDemand p
    omega

def history {ι : Type} (p : Network ι) (s : State ι) : Nat → State ι
  | 0 => s
  | t+1 => outcome p (supplied p) (history p s t)

theorem supported_history {ι : Type} (p : Network ι) (floor : ι → Nat)
    (selected : ι → Bool) (hc : Maintenance p floor selected) (s : State ι)
    (hs : Supported p floor s) (t : Nat) : Supported p floor (history p s t) := by
  induction t with
  | zero => exact hs
  | succ t ih => exact supported_step p floor selected hc _ ih

theorem actual_history {ι : Type} (p : Network ι) (floor : ι → Nat)
    (selected : ι → Bool) (hc : Maintenance p floor selected) (s : State ι)
    (hs : Supported p floor s) (t : Nat) :
    Generative.Trace (process p) s (List.replicate t (supplied p)) (history p s t) := by
  induction t with
  | zero => exact .nil s
  | succ t ih =>
    have ready := supported_ready p floor _ (supported_history p floor selected hc s hs t)
    have step : (process p).step (history p s t) (supplied p) (history p s (t+1)) :=
      ⟨ready,rfl⟩
    have trace := Generative.trace_append_iff.mpr
      ⟨history p s t, ih, Generative.trace_singleton_iff.mpr step⟩
    rw [← List.replicate_succ'] at trace
    exact trace

theorem generation_history {ι : Type} (p : Network ι) (s : State ι) (t : Nat) :
    (history p s t).generation=s.generation+t := by
  induction t with
  | zero => rfl
  | succ t ih => simp only [history, outcome, ih]; omega

def pair : Network Bool where
  roles := [false,true]
  distinct := by decide
  threshold := fun _ => 2
  wear := fun _ => 1
  capacity := fun _ => 3
  output := fun i j => if i != j then 2 else 0

def two (x y : Nat) : Bool → Nat := fun i => if i then y else x

theorem pair_maintenance : Maintenance pair (fun _ => 2) (fun _ => true) := by
  constructor <;> decide

theorem jointly_established : Box pair (fun _ => 2) (advance pair (two 1 3)) := by
  unfold Box
  decide

theorem alternating_first : advance pair (two 1 2) = two 2 1 := by
  funext i
  cases i <;> decide

theorem alternating_second : advance pair (two 2 1) = two 1 2 := by
  funext i
  cases i <;> decide

theorem alternating_history (t : Nat) :
    stockHistory pair (two 1 2) (2*t)=two 1 2 ∧
    stockHistory pair (two 1 2) (2*t+1)=two 2 1 := by
  induction t with
  | zero => exact ⟨rfl,alternating_first⟩
  | succ t ih =>
    have e : 2*(t+1)=2*t+1+1 := by omega
    rw [e]
    constructor
    · change advance pair (stockHistory pair (two 1 2) (2*t+1)) = two 1 2
      rw [ih.2]
      exact alternating_second
    · change advance pair (advance pair (stockHistory pair (two 1 2) (2*t+1))) = two 2 1
      rw [ih.2, alternating_second]
      exact alternating_first

theorem no_eventual_joint_activation :
    ¬ ∃ start, ∀ t, start ≤ t → Box pair (fun _ => 2) (stockHistory pair (two 1 2) t) := by
  rintro ⟨start, all⟩
  have h := all (2*start) (by omega)
  rw [(alternating_history start).1] at h
  have bad := (h false (by decide)).1
  change 2 ≤ 1 at bad
  omega

theorem cold_fixed : advance pair (two 0 0) = two 0 0 := by
  funext i
  cases i <;> decide

theorem saturated_pair : advance pair (two 3 3) = two 3 3 := by
  funext i
  cases i <;> decide

def cutPair : Network Bool :=
  {pair with output := fun i j => if i = true ∧ j = false then 2 else 0}

theorem severed_pair_loses_both : stockHistory cutPair (two 3 3) 5 = two 0 0 := by
  funext i
  cases i <;> decide

def Establishable {ι : Type} (p : Network ι) (addition : ι → Nat) (s : State ι) : Prop :=
  total p.roles addition ≤ s.material ∧
    ∀ j ∈ p.roles, s.stock j+addition j ≤ p.capacity j

def establish {ι : Type} (p : Network ι) (addition : ι → Nat) (s : State ι) : State ι :=
  {s with
    stock := fun i => s.stock i + addition i
    material := s.material - total p.roles addition}

inductive ActivationEvent (ι : Type) where
  | operate : Supply → ActivationEvent ι
  | establish : (ι → Nat) → ActivationEvent ι

def activationProcess {ι : Type} (p : Network ι) :
    Generative.Process (State ι) (ActivationEvent ι) where
  step s event t := match event with
    | .operate a => Ready p s ∧ t = outcome p a s
    | .establish add => Establishable p add s ∧ t = establish p add s

theorem establishment_accounting {ι : Type} (p : Network ι)
    (addition : ι → Nat) (s : State ι) (h : Establishable p addition s) :
    total p.roles (establish p addition s).stock+(establish p addition s).material =
      total p.roles s.stock+s.material := by
  have hm := h.1
  simp only [establish, total_add]
  omega

theorem lift_operation_trace {ι : Type} (p : Network ι) (s t : State ι) (events : List Supply)
    (h : Generative.Trace (process p) s events t) :
    Generative.Trace (activationProcess p) s (events.map ActivationEvent.operate) t := by
  induction h with
  | nil => exact .nil _
  | cons first rest ih => exact .cons first ih

def coldStart : State Bool := ⟨two 0 0,0,2,8⟩
def seeded : State Bool := establish pair (two 2 2) coldStart

theorem funded_establishment : Establishable pair (two 2 2) coldStart := by
  unfold Establishable
  decide

theorem seed_is_supported : Supported pair (fun _ => 2) seeded := by
  unfold Supported Box
  decide

theorem establishment_then_actual_recurrence (t : Nat) :
    Generative.Trace (activationProcess pair) coldStart
      (.establish (two 2 2) :: (List.replicate t (supplied pair)).map ActivationEvent.operate)
      (history pair seeded t) := by
  have initial : (activationProcess pair).step coldStart (.establish (two 2 2)) seeded :=
    ⟨funded_establishment,rfl⟩
  have later := actual_history pair (fun _ => 2) (fun _ => true)
    pair_maintenance seeded seed_is_supported t
  exact .cons initial (lift_operation_trace pair seeded _ _ later)

inductive Arrangement where
  | separate | bridge | ring | broken
  deriving DecidableEq, Repr

def four (a b c d : Nat) : Fin 4 → Nat := fun i =>
  if i.val=0 then a else if i.val=1 then b else if i.val=2 then c else d

def splitOutput (i j : Fin 4) : Nat :=
  if i.val/2 = j.val/2 ∧ i ≠ j then 2 else 0

def arrangement (kind : Arrangement) : Network (Fin 4) where
  roles := [0,1,2,3]
  distinct := by decide
  threshold := fun _ => 2
  wear := fun _ => 1
  capacity := fun _ => 3
  output := fun i j => match kind with
    | .separate => splitOutput i j
    | .bridge => splitOutput i j + if i.val=1 ∧ j.val=2 then 2 else 0
    | .ring => if (i.val+1)%4 = j.val then 2 else 0
    | .broken => 0

theorem arrangement_maintenance (kind : Arrangement) (h : kind ≠ .broken) :
    Maintenance (arrangement kind) (fun _ => 2) (fun _ => true) := by
  cases kind <;> (try contradiction) <;> constructor <;> decide

theorem arrangement_certificate_iff (kind : Arrangement) :
    Maintenance (arrangement kind) (fun _ => 2) (fun _ => true) ↔ kind ≠ .broken := by
  constructor
  · intro h same
    subst kind
    have bad := h.returned_amount 0 (by decide)
    change 2 ≤ 1 at bad
    omega
  · exact arrangement_maintenance kind

theorem independent_regimes :
    advance (arrangement .separate) (four 3 3 0 0) = four 3 3 0 0 := by
  apply funext
  decide

theorem bridge_establishment :
    stockHistory (arrangement .bridge) (four 3 3 0 0) 2 = four 3 3 3 2 := by
  apply funext
  decide

theorem bridge_can_be_removed :
    Box (arrangement .separate) (fun _ => 2)
      (stockHistory (arrangement .bridge) (four 3 3 0 0) 2) := by
  unfold Box
  decide

theorem ring_reorganization :
    stockHistory (arrangement .ring) (four 3 3 0 0) 3 = four 2 2 3 3 := by
  apply funext
  decide

theorem unsupported_revision_breaks_reproduction :
    stockHistory (arrangement .broken) (four 3 3 3 3) 3 = four 0 0 0 0 := by
  apply funext
  decide

theorem ring_four_cycle :
    stockHistory (arrangement .ring) (four 0 0 1 2) 4 = four 0 0 1 2 ∧
    stockHistory (arrangement .ring) (four 0 0 1 2) 1 ≠ four 0 0 1 2 := by
  constructor
  · apply funext
    decide
  · intro h
    have hh := congrFun h 0
    change 2 = 0 at hh
    contradiction

theorem arrangement_demand_bound (kind : Arrangement) (s : Fin 4 → Nat) :
    demand (arrangement kind) s ≤ 10 := by
  have h := demand_bound (arrangement kind) s
  have cap : maximumDemand (arrangement kind) ≤ 10 := by cases kind <;> decide
  omega

structure Installation where
  kind : Arrangement
  body : State (Fin 4)

def revision (s : Installation) (kind : Arrangement) : Installation :=
  {kind := kind, body := {s.body with material := s.body.material-1}}

def allotment : Supply := ⟨4,11⟩

def cycle (s : Installation) (kind : Arrangement) : Installation :=
  ⟨kind, outcome (arrangement kind) allotment (revision s kind).body⟩

inductive ChangeEvent where
  | revise : Arrangement → ChangeEvent
  | operate : Supply → ChangeEvent

def changingProcess : Generative.Process Installation ChangeEvent where
  step s event t := match event with
    | .revise kind => 0 < s.body.material ∧ t = revision s kind
    | .operate a => Ready (arrangement s.kind) s.body ∧
        t = ⟨s.kind, outcome (arrangement s.kind) a s.body⟩

def Equipped (s : Installation) : Prop := 4 ≤ s.body.parts ∧ 11 ≤ s.body.material
def Established (s : Installation) : Prop := ∀ i, 2 ≤ s.body.stock i ∧ s.body.stock i ≤ 3

theorem cycle_is_executable (s : Installation) (kind : Arrangement) (h : Equipped s) :
    Generative.Trace changingProcess s [.revise kind,.operate allotment] (cycle s kind) := by
  have demandCap := arrangement_demand_bound kind s.body.stock
  have first : changingProcess.step s (.revise kind) (revision s kind) :=
    ⟨by have := h.2; omega,rfl⟩
  have ready : Ready (arrangement kind) (revision s kind).body := by
    refine ⟨by change 0 < 4; decide,h.1,?_⟩
    change demand (arrangement kind) s.body.stock ≤ s.body.material-1
    have := h.2
    omega
  exact .cons first (.cons ⟨ready,rfl⟩ (.nil _))

theorem cycle_equipped (s : Installation) (kind : Arrangement) (h : Equipped s) :
    Equipped (cycle s kind) := by
  have demandCap := arrangement_demand_bound kind s.body.stock
  have hm := h.2
  have hp := h.1
  change 4 ≤ s.body.parts-4+4 ∧
    11 ≤ s.body.material-1-demand (arrangement kind) s.body.stock+11
  constructor <;> omega

theorem cycle_established (s : Installation) (kind : Arrangement)
    (hs : Established s) (hk : kind ≠ .broken) : Established (cycle s kind) := by
  have box : Box (arrangement kind) (fun _ => 2) s.body.stock := fun i _ => hs i
  have hb := maintenance_step (arrangement kind) (fun _ => 2) s.body.stock
    (fun _ => true) (arrangement_maintenance kind hk) box
  intro i
  have member : i ∈ (arrangement kind).roles := by
    change i ∈ [0,1,2,3]
    exact (by decide : ∀ j : Fin 4, j ∈ [0,1,2,3]) i
  exact hb i member

theorem revision_and_operation_accounting (s : Installation) (kind : Arrangement)
    (h : Equipped s) :
    total (arrangement kind).roles (cycle s kind).body.stock +
      (cycle s kind).body.material +
      total (arrangement kind).roles (worn (arrangement kind) s.body.stock) +
      total (arrangement kind).roles (overflow (arrangement kind) s.body.stock) + 1 =
      total (arrangement kind).roles s.body.stock+s.body.material+11 := by
  have dc := arrangement_demand_bound kind s.body.stock
  have hm := h.2
  have hr : Ready (arrangement kind) (revision s kind).body := by
    refine ⟨by change 0 < 4; decide,h.1,?_⟩
    change demand (arrangement kind) s.body.stock ≤ s.body.material-1
    omega
  have account := full_material_accounting (arrangement kind) allotment (revision s kind).body hr
  change total (arrangement kind).roles (cycle s kind).body.stock +
    (cycle s kind).body.material +
    total (arrangement kind).roles (worn (arrangement kind) s.body.stock) +
    total (arrangement kind).roles (overflow (arrangement kind) s.body.stock) =
    total (arrangement kind).roles s.body.stock+(s.body.material-1)+11 at account
  omega

def changingHistory (choose : Nat → Installation → Arrangement) (s : Installation) : Nat → Installation
  | 0 => s
  | t+1 => cycle (changingHistory choose s t) (choose t (changingHistory choose s t))

def changeEvents (choose : Nat → Installation → Arrangement) (s : Installation) : Nat → List ChangeEvent
  | 0 => []
  | t+1 => changeEvents choose s t ++
      [.revise (choose t (changingHistory choose s t)),.operate allotment]

theorem changing_history_equipped (choose : Nat → Installation → Arrangement)
    (s : Installation) (h : Equipped s) (t : Nat) : Equipped (changingHistory choose s t) := by
  induction t with
  | zero => exact h
  | succ t ih => exact cycle_equipped _ _ ih

theorem changing_actual_history (choose : Nat → Installation → Arrangement)
    (s : Installation) (h : Equipped s) (t : Nat) :
    Generative.Trace changingProcess s (changeEvents choose s t) (changingHistory choose s t) := by
  induction t with
  | zero => exact .nil s
  | succ t ih =>
    have next := cycle_is_executable _ (choose t (changingHistory choose s t))
      (changing_history_equipped choose s h t)
    exact Generative.trace_append_iff.mpr ⟨_,ih,next⟩

theorem changing_history_established (choose : Nat → Installation → Arrangement)
    (s : Installation) (h : Established s)
    (choices : ∀ t u, Established u → choose t u ≠ .broken) (t : Nat) :
    Established (changingHistory choose s t) := by
  induction t with
  | zero => exact h
  | succ t ih => exact cycle_established _ _ ih (choices t _ ih)

theorem broken_demand (stock : Fin 4 → Nat) : demand (arrangement .broken) stock = 0 := by
  simp [demand,incoming,arrangement,total]

/-- This is a supplied one-round material-retention objective, not an ethical
comparison or a claim of optimality over the full future. -/
theorem myopic_retention_prefers_no_return (s : Installation) (kind : Arrangement) :
    (cycle s kind).body.material ≤ (cycle s .broken).body.material := by
  change s.body.material-1-demand (arrangement kind) s.body.stock+11 ≤
    s.body.material-1-demand (arrangement .broken) s.body.stock+11
  rw [broken_demand]
  omega

def warmStart : Installation := ⟨.separate,⟨four 3 3 3 3,0,4,11⟩⟩

theorem warm_start_supported : Equipped warmStart ∧ Established warmStart := by
  unfold Equipped Established
  decide

theorem myopic_revision_is_strict_initially (kind : Arrangement) (h : kind ≠ .broken) :
    (cycle warmStart kind).body.material < (cycle warmStart .broken).body.material := by
  cases kind <;> (try contradiction) <;> decide

theorem actual_myopic_loss :
    (changingHistory (fun _ _ => .broken) warmStart 3).body.stock = four 0 0 0 0 ∧
    (changingHistory (fun _ _ => .broken) warmStart 3).body.material = 41 ∧
    (changingHistory (fun _ _ => .broken) warmStart 3).body.generation = 3 := by
  refine ⟨?_,by decide,by decide⟩
  apply funext
  decide

/-- Two required authorization roles must be operative. The implementation
recognizes only this declared finite proposal class. It has no permanent
protection when either represented authorization capacity is absent. -/
def admittedRule (s : Installation) (proposal : Arrangement) : Arrangement :=
  if 2 ≤ s.body.stock 0 ∧ 2 ≤ s.body.stock 2 then
    if proposal = .broken then .separate else proposal
  else proposal

theorem supported_authorizers_admit_maintenance (s : Installation)
    (h : Established s) (proposal : Arrangement) : admittedRule s proposal ≠ .broken := by
  have hg : 2 ≤ s.body.stock 0 ∧ 2 ≤ s.body.stock 2 := ⟨(h 0).1,(h 2).1⟩
  cases proposal <;> simp [admittedRule,hg]

def proposedHistory (proposals : Nat → Installation → Arrangement) (s : Installation) :
    Nat → Installation := changingHistory (fun t u => admittedRule u (proposals t u)) s

theorem admission_reproduced (proposals : Nat → Installation → Arrangement)
    (s : Installation) (h : Established s) (t : Nat) :
    Established (proposedHistory proposals s t) := by
  exact changing_history_established _ s h
    (fun _ u hu => supported_authorizers_admit_maintenance u hu _) t

def proposalProcess : Generative.Process Installation Arrangement where
  step s proposal t := Equipped s ∧ t=cycle s (admittedRule s proposal)

theorem proposal_refines_actual_events (s t : Installation) (proposal : Arrangement)
    (h : proposalProcess.step s proposal t) :
    Generative.Trace changingProcess s [.revise (admittedRule s proposal),.operate allotment] t := by
  rw [h.2]
  exact cycle_is_executable s _ h.1

def proposalEvents (proposals : Nat → Installation → Arrangement) (s : Installation) :
    Nat → List Arrangement
  | 0 => []
  | t+1 => proposalEvents proposals s t ++ [proposals t (proposedHistory proposals s t)]

theorem proposal_history_actual (proposals : Nat → Installation → Arrangement)
    (s : Installation) (h : Equipped s) (t : Nat) :
    Generative.Trace proposalProcess s (proposalEvents proposals s t) (proposedHistory proposals s t) := by
  induction t with
  | zero => exact .nil s
  | succ t ih =>
    have eqp := changing_history_equipped (fun t u => admittedRule u (proposals t u)) s h t
    have next : proposalProcess.step (proposedHistory proposals s t)
        (proposals t (proposedHistory proposals s t)) (proposedHistory proposals s (t+1)) :=
      ⟨eqp,rfl⟩
    exact Generative.trace_append_iff.mpr
      ⟨_,ih,Generative.trace_singleton_iff.mpr next⟩

def weakened : Installation := ⟨.separate,⟨four 1 3 1 3,0,4,11⟩⟩

theorem weak_authorization_allows_failure :
    admittedRule weakened .broken = .broken ∧
    (proposedHistory (fun _ _ => .broken) weakened 3).body.stock = four 0 0 0 0 := by
  refine ⟨by decide,?_⟩
  apply funext
  decide

theorem weakened_state_can_reestablish : Established (cycle weakened .separate) := by
  unfold Established
  decide

theorem arbitrary_proposals_preserve_warm_regime
    (proposals : Nat → Installation → Arrangement) (t : Nat) :
    Established (proposedHistory proposals warmStart t) ∧
    Generative.Trace proposalProcess warmStart (proposalEvents proposals warmStart t)
      (proposedHistory proposals warmStart t) :=
  ⟨admission_reproduced proposals warmStart warm_start_supported.2 t,
    proposal_history_actual proposals warmStart warm_start_supported.1 t⟩

end ReproductionNetwork
