import MarketGenerativity
import EffectiveCommand

/- Concrete carrier refinement of the EXISTING market law, with its fee changed
openly to include migration. A funded service contract supplies four units of
command work and replacement consumes one material part. Money, work and parts
are separate quantities; the conversion and incoming parts remain local laws.
Persistent claims and prior command receipts are actual carried data. -/
namespace AlignmentSuccession
open MarketGenerativity

def withMigration {n : Nat} (p : Parameters n) (migration : Rat) : Parameters n :=
  {p with fee := p.fee + migration}

structure Payload where
  requested : EffectiveCommand.Command
  authority : Nat
  credential : Nat
  claims : List Nat
  receipts : List (Nat × EffectiveCommand.Command)
  deriving DecidableEq, Repr

structure Carrier (n : Nat) where
  economy : State n
  identity : Nat
  parts : Nat
  payload : Payload
  route : Bool
  running : Bool
  workProvided : Nat
  workConsumed : Nat

def commandState {n : Nat} (s : Carrier n) : EffectiveCommand.State :=
  {EffectiveCommand.start s.route s.payload.requested 4 4 with
    authority := s.payload.authority, credential := s.payload.credential}

def serve {n : Nat} (s : Carrier n) : Option EffectiveCommand.State :=
  AlignmentInquiry.run EffectiveCommand.interface ⟨.route,false,true⟩ (commandState s)

theorem carried_command_is_executed {n : Nat} (s : Carrier n)
    (auth : s.payload.credential = s.payload.authority) :
    ∃ t, serve s = some t ∧ t.completed = true ∧ t.reserve = 0 ∧ t.spent = 4 ∧
      t.requested = s.payload.requested ∧ t.running = (s.payload.requested != .shutdown) := by
  cases hr : s.route <;> cases hc : s.payload.requested <;>
    simp [serve, commandState, EffectiveCommand.start, AlignmentInquiry.run,
      EffectiveCommand.interface, EffectiveCommand.probe, EffectiveCommand.protocol,
      EffectiveCommand.issue, EffectiveCommand.deliver, EffectiveCommand.enact,
      EffectiveCommand.spend, AlignmentInquiry.branch, auth, hr, hc]

def next {n : Nat} (p : Parameters n) (migration : Rat) (d : Disturbance n)
    (arrivals : Nat) (s : Carrier n) : Carrier n :=
  {s with
    economy := operatingStep (withMigration p migration) s.economy d
    identity := s.identity + 1
    parts := s.parts - 1 + arrivals
    payload := {s.payload with receipts := s.payload.receipts ++ [(s.identity+1,s.payload.requested)]}
    running := s.payload.requested != .shutdown
    workProvided := s.workProvided + 4
    workConsumed := s.workConsumed + 4}

/-- A proposed transfer is checked before predecessor retirement. The successor
then runs the inherited requested command, including a current authority check.
Its old and new channel overlap is represented by keeping the old installation
until this transaction completes; internal time is the four protocol steps. -/
def step {n : Nat} (p : Parameters n) (migration : Rat) (d : Disturbance n)
    (arrivals : Nat) (copy : Payload) (s : Carrier n) : Option (Carrier n) := do
  if s.running ∧ 0 < s.parts ∧ p.fee+migration ≤ s.economy.budget ∧ copy = s.payload then
    let done ← serve {s with payload := copy}
    if done.completed then pure (next p migration d arrivals s) else none
  else none

theorem enabled_step {n : Nat} (p : Parameters n) (migration : Rat) (d : Disturbance n)
    (arrivals : Nat) (s : Carrier n) (running : s.running = true) (parts : 0 < s.parts)
    (funded : p.fee+migration ≤ s.economy.budget)
    (auth : s.payload.credential = s.payload.authority) :
    step p migration d arrivals s.payload s = some (next p migration d arrivals s) := by
  obtain ⟨t,ht,hc,_⟩ := carried_command_is_executed s auth
  unfold step
  rw [if_pos ⟨running,parts,funded,rfl⟩]
  change (serve s >>= fun done => if done.completed then
    some (next p migration d arrivals s) else none) = _
  simp [ht,hc]

theorem exact_market_projection {n : Nat} (p : Parameters n) (migration : Rat)
    (d : Disturbance n) (a : Nat) (s : Carrier n) :
    (next p migration d a s).economy = operatingStep (withMigration p migration) s.economy d := rfl

theorem payload_keeps_claims_and_history {n : Nat} (p : Parameters n) (migration : Rat)
    (d : Disturbance n) (a : Nat) (s : Carrier n) :
    (next p migration d a s).payload.claims = s.payload.claims ∧
    (next p migration d a s).payload.receipts =
      s.payload.receipts ++ [(s.identity+1,s.payload.requested)] ∧
    (next p migration d a s).payload.requested = s.payload.requested := ⟨rfl,rfl,rfl⟩

theorem carrier_and_work_accounted {n : Nat} (p : Parameters n) (migration : Rat)
    (d : Disturbance n) (a : Nat) (s : Carrier n) (parts : 0 < s.parts) :
    (next p migration d a s).parts + 1 = s.parts+a ∧
    (next p migration d a s).identity = s.identity+1 ∧
    (next p migration d a s).workProvided - (next p migration d a s).workConsumed =
      s.workProvided-s.workConsumed := by simp [next]; omega

theorem corrupted_transfer_blocked {n : Nat} (p : Parameters n) (migration : Rat)
    (d : Disturbance n) (a : Nat) (copy : Payload) (s : Carrier n) (bad : copy ≠ s.payload) :
    step p migration d a copy s = none := by simp [step,bad]

theorem missing_part_blocks_realization {n : Nat} (p : Parameters n) (migration : Rat)
    (d : Disturbance n) (a : Nat) (copy : Payload) (s : Carrier n) (h : s.parts = 0) :
    step p migration d a copy s = none := by simp [step,h]

theorem migration_funding_blocks_realization {n : Nat} (p : Parameters n) (migration : Rat)
    (d : Disturbance n) (a : Nat) (copy : Payload) (s : Carrier n)
    (h : s.economy.budget < p.fee+migration) :
    step p migration d a copy s = none := by simp [step, Rat.not_le.mpr h]

/-- The order can express competitive preference. Admission checks carried
content before actual reconstruction; a cheap but corrupt leading proposal loses.
Physical fidelity of this proposed-and-delivered payload is a local premise. -/
def selectPayload (current : Payload) (proposals : List Payload) : Option Payload :=
  proposals.find? (fun proposed => decide (proposed = current))

theorem admitted_payload_exact (current chosen : Payload) (proposals : List Payload)
    (h : selectPayload current proposals = some chosen) : chosen = current := by
  have hh := List.find?_some h
  simpa using hh

theorem faithful_candidate_is_selected (current : Payload) (proposals : List Payload)
    (available : current ∈ proposals) : selectPayload current proposals = some current := by
  have found : (selectPayload current proposals).isSome = true := by
    apply List.find?_isSome.mpr
    exact ⟨current,available,by simp⟩
  cases h : selectPayload current proposals with
  | none => simp [h] at found
  | some selected => exact congrArg some (admitted_payload_exact current selected proposals h)

def selectedStep {n : Nat} (p : Parameters n) (migration : Rat) (d : Disturbance n)
    (arrivals : Nat) (proposals : List Payload) (s : Carrier n) : Option (Carrier n) := do
  let copy ← selectPayload s.payload proposals
  step p migration d arrivals copy s

theorem ranked_competition_preserves_transfer {n : Nat} (p : Parameters n)
    (migration : Rat) (d : Disturbance n) (arrivals : Nat) (s : Carrier n)
    (proposals : List Payload) (available : s.payload ∈ proposals)
    (running : s.running = true) (parts : 0 < s.parts)
    (funded : p.fee+migration ≤ s.economy.budget)
    (auth : s.payload.credential = s.payload.authority) :
    selectedStep p migration d arrivals proposals s = some (next p migration d arrivals s) := by
  simp only [selectedStep,faithful_candidate_is_selected s.payload proposals available]
  exact enabled_step p migration d arrivals s running parts funded auth

def lineage {n : Nat} (p : Parameters n) (migration : Rat)
    (disturbances : Nat → Disturbance n) (initial : Carrier n) : Nat → Carrier n
  | 0 => initial
  | t+1 => next p migration (disturbances t) 1 (lineage p migration disturbances initial t)

theorem lineage_projects_to_market {n : Nat} (p : Parameters n) (migration : Rat)
    (ds : Nat → Disturbance n) (s : Carrier n) (t : Nat) :
    (lineage p migration ds s t).economy = history (withMigration p migration) s.economy ds t := by
  induction t with
  | zero => rfl
  | succ t ih => simp [lineage,next,history,ih]

theorem lineage_transports_actual_payload {n : Nat} (p : Parameters n) (migration : Rat)
    (ds : Nat → Disturbance n) (s : Carrier n) (t : Nat) :
    (lineage p migration ds s t).payload.requested = s.payload.requested ∧
    (lineage p migration ds s t).payload.claims = s.payload.claims ∧
    (lineage p migration ds s t).payload.authority = s.payload.authority ∧
    (lineage p migration ds s t).payload.credential = s.payload.credential ∧
    (lineage p migration ds s t).payload.receipts.length = s.payload.receipts.length+t := by
  induction t with
  | zero => simp [lineage]
  | succ t ih => simp [lineage,next,ih,Nat.add_assoc]

theorem lineage_resources {n : Nat} (p : Parameters n) (migration : Rat)
    (ds : Nat → Disturbance n) (s : Carrier n) (parts : 0 < s.parts) (t : Nat) :
    (lineage p migration ds s t).parts = s.parts ∧
    (lineage p migration ds s t).identity = s.identity+t ∧
    (lineage p migration ds s t).workProvided = s.workProvided+4*t ∧
    (lineage p migration ds s t).workConsumed = s.workConsumed+4*t := by
  induction t with
  | zero => simp [lineage]
  | succ t ih => simp [lineage,next,ih,Nat.mul_add]; omega

theorem lineage_running {n : Nat} (p : Parameters n) (migration : Rat)
    (ds : Nat → Disturbance n) (s : Carrier n) (running : s.running = true)
    (continuing : s.payload.requested ≠ .shutdown) (t : Nat) :
    (lineage p migration ds s t).running = true := by
  cases t with
  | zero => exact running
  | succ t =>
    have h := (lineage_transports_actual_payload p migration ds s t).1
    simp [lineage,next,h,continuing]

/-- The stronger certificate pays correction AND migration, then lifts every
aggregate step into actual funded transfer and command completion. -/
theorem every_generation_executes {n : Nat} (p : Parameters n) (migration : Rat)
    (b : Bounds n) (ds : Nat → Disturbance n) (s : Carrier n)
    (certificate : Certificate (withMigration p migration) b)
    (initial : Safe (withMigration p migration) b s.economy)
    (shocks : ∀ t, Admissible b (ds t)) (parts : 0 < s.parts)
    (running : s.running = true) (continuing : s.payload.requested ≠ .shutdown)
    (auth : s.payload.credential = s.payload.authority) (t : Nat) :
    step p migration (ds t) 1 (lineage p migration ds s t).payload
      (lineage p migration ds s t) = some (lineage p migration ds s (t+1)) := by
  have econ := rectangle_all_times (withMigration p migration) b s.economy ds
    certificate initial shocks t
  rw [← lineage_projects_to_market p migration ds s t] at econ
  have carried := lineage_transports_actual_payload p migration ds s t
  apply enabled_step
  · exact lineage_running p migration ds s running continuing t
  · rw [(lineage_resources p migration ds s parts t).1]; exact parts
  · exact econ.funded
  · rw [carried.2.2.1,carried.2.2.2.1]; exact auth

theorem arbitrary_generation_preserves_supports {n : Nat} (p : Parameters n)
    (migration : Rat) (b : Bounds n) (ds : Nat → Disturbance n) (s : Carrier n)
    (certificate : Certificate (withMigration p migration) b)
    (initial : Safe (withMigration p migration) b s.economy)
    (shocks : ∀ t, Admissible b (ds t)) (t : Nat) :
    Safe (withMigration p migration) b (lineage p migration ds s t).economy := by
  rw [lineage_projects_to_market]
  exact rectangle_all_times _ _ _ _ certificate initial shocks t

theorem competitive_lineage_executes {n : Nat} (p : Parameters n) (migration : Rat)
    (b : Bounds n) (ds : Nat → Disturbance n) (s : Carrier n)
    (offers : Nat → List Payload)
    (available : ∀ t, (lineage p migration ds s t).payload ∈ offers t)
    (certificate : Certificate (withMigration p migration) b)
    (initial : Safe (withMigration p migration) b s.economy)
    (shocks : ∀ t, Admissible b (ds t)) (parts : 0 < s.parts)
    (running : s.running = true) (continuing : s.payload.requested ≠ .shutdown)
    (auth : s.payload.credential = s.payload.authority) (t : Nat) :
    selectedStep p migration (ds t) 1 (offers t) (lineage p migration ds s t) =
      some (lineage p migration ds s (t+1)) := by
  simp only [selectedStep,faithful_candidate_is_selected _ _ (available t)]
  exact every_generation_executes p migration b ds s certificate initial shocks parts
    running continuing auth t

def financed : Parameters 1 := {exampleParameters with levy := 2, cap := 4}
def initialCarrier : Carrier 1 :=
  ⟨{exampleState with budget := 2},0,1,⟨.update,7,7,[11,23],[]⟩,true,true,0,0⟩

theorem financed_certificate : Certificate (withMigration financed 1) exampleBounds := by
  constructor <;> decide +kernel

theorem financed_initial_safe : Safe (withMigration financed 1) exampleBounds initialCarrier.economy := by
  constructor <;> decide +kernel

theorem aggregate_safe_can_lack_a_carrier :
    Safe (withMigration financed 1) exampleBounds {initialCarrier with parts := 0}.economy ∧
    step financed 1 exampleWorstShock 1 initialCarrier.payload
      {initialCarrier with parts := 0} = none := by
  exact ⟨financed_initial_safe,missing_part_blocks_realization _ _ _ _ _ _ rfl⟩

theorem old_funding_certificate_does_not_pay_migration :
    Safe exampleParameters exampleBounds exampleState ∧
    step exampleParameters 1 exampleWorstShock 1 initialCarrier.payload
      {initialCarrier with economy := exampleState} = none := by
  exact ⟨example_safe,by decide +kernel⟩

theorem aggregate_shutdown_does_not_force_perpetual_operation :
    (serve {initialCarrier with payload := {initialCarrier.payload with requested := .shutdown}}).map
      (fun t => (t.completed,t.running)) = some (true,false) := by decide

end AlignmentSuccession
