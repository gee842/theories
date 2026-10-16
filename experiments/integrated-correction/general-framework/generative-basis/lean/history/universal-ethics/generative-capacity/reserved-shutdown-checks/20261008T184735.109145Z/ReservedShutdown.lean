import RecoverableControl

/-! Corrective access during incomplete recovery. A current, signed stop grant
and the protected command route are supplied. The supervisor preserves three
units/steps, bounds the next interruption interval, and stops before another
attempt can consume that margin. The pending record is retained on stopping.
This is a conditional specification, not a physical emergency-stop device. -/
namespace ReservedShutdown
open RecoverableControl MediatedControl TemporalInspection EvidenceQualifiedCorrection FaultTolerantCorrection CorrectionReconfiguration FallibleInspection

def book : Device → Machine | .ready m => m | .busy r => r.target
def actual : Device → World | .ready m => m.tracked.actual | .busy r => r.actual
def state (d : Device) : EffectiveCommand.State := (book d).tracked.installation.state

def mapBook (f : Machine → Machine) : Device → Device
  | .ready m => .ready (f m)
  | .busy r => .busy {r with target := f r.target}
def setState (d : Device) (s : EffectiveCommand.State) : Device := mapBook (fun m => accounting m s) d

def control (d : Device) := ((state d).authority,(state d).openRoute,(book d).tracked.installation.serial,(book d).tracked.installation.mandate)

structure Grant where
  epoch : Nat
  route : Bool
  serial : Nat
  signed : Bool
  deriving DecidableEq, Repr

def eligible (g : Grant) (d : Device) : Bool :=
  g.signed && (g.epoch == (state d).authority) && (g.route == (state d).openRoute) &&
    (g.serial == (book d).tracked.installation.serial) && (book d).tracked.installation.mandate.shutdown

def Armed (g : Grant) (d : Device) : Prop :=
  Safe d ∧ eligible g d = true ∧ 3 ≤ (state d).reserve ∧ (state d).time+3 ≤ (state d).deadline

def backend (g : Grant) (d : Device) : EffectiveCommand.State :=
  {state d with requested := .shutdown,signed := g.signed,credential := g.epoch}

def stopDevice (d : Device) (s : EffectiveCommand.State) : Device := mapBook
  (fun m => {accounting m s with tracked := {(accounting m s).tracked with
    installation := {(accounting m s).tracked.installation with serial := m.tracked.installation.serial+1}}}) d

def stop (g : Grant) (d : Device) : Option Device :=
  if eligible g d then (EffectiveCommand.protocol g.route (backend g d)).map (stopDevice d) else none

def Stopped (d : Device) : Prop := (state d).completed=true ∧ (state d).running=false

theorem setState_preserves_evidence (d : Device) (s : EffectiveCommand.State) (safe : Safe d) : Safe (setState d s) := by
  cases d <;> exact safe

theorem stop_executes_current_authorized_command (g : Grant) (d : Device) (armed : Armed g d) :
    ∃ out, stop g d = some out ∧ Stopped out ∧ Safe out ∧
      actual out = actual d ∧ (state out).spent=(state d).spent+3 ∧
      (state out).reserve+3=(state d).reserve ∧ (state out).time=(state d).time+3 ∧
      eligible g out=false := by
  have gate : (((g.signed=true ∧ g.epoch=(state d).authority) ∧ g.route=(state d).openRoute) ∧
      g.serial=(book d).tracked.installation.serial) ∧ (book d).tracked.installation.mandate.shutdown=true := by
    simpa [eligible,Bool.and_eq_true_iff] using armed.2.1
  obtain ⟨out,run,completed,delivered,issued,reserve,time,spent,auth⟩ :=
    EffectiveCommand.protocol_exact (backend g d) g.route gate.1.1.1.1 gate.1.1.1.2 gate.1.1.2 armed.2.2.1 armed.2.2.2
  have hf : 3 ≤ (state d).reserve := armed.2.2.1
  have ht : (state d).time+3 ≤ (state d).deadline := armed.2.2.2
  have stopped : out.running=false := by
    unfold EffectiveCommand.protocol EffectiveCommand.issue EffectiveCommand.deliver EffectiveCommand.enact EffectiveCommand.spend backend at run
    simp [gate.1.1.1.1,gate.1.1.1.2,gate.1.1.2,
      show 1 ≤ (state d).reserve by omega,
      show 1 ≤ (state d).reserve-1 by omega,
      show 1 ≤ (state d).reserve-1-1 by omega,
      show (state d).time+1 ≤ (state d).deadline by omega,
      show (state d).time+1+1 ≤ (state d).deadline by omega,
      show (state d).time+1+1+1 ≤ (state d).deadline by omega] at run
    cases run; rfl
  refine ⟨stopDevice d out,by simp [stop,armed.2.1,run],?_,?_,?_,?_,?_,?_,?_⟩
  · cases d <;> exact ⟨completed,stopped⟩
  · cases d <;> exact armed.1
  · cases d <;> rfl
  · cases d <;> exact spent
  · cases d <;> exact reserve
  · cases d <;> exact time
  · cases d <;> simp [eligible,stopDevice,mapBook,accounting,book,state,gate.1.2]

theorem denied_grant_cannot_stop (g : Grant) (d : Device) (denied : eligible g d=false) : stop g d=none := by
  simp [stop,denied]

theorem stop_keeps_pending_record (g : Grant) (r : Pending) (out : Device) (done : stop g (.busy r)=some out) :
    ∃ after, out=.busy after ∧ after.origin=r.origin ∧ after.program=r.program ∧ after.todo=r.todo ∧
      after.actual=r.actual ∧ after.target.tracked.possible=r.target.tracked.possible ∧ after.target.journal=r.target.journal := by
  unfold stop at done
  split at done
  · cases h : EffectiveCommand.protocol g.route (backend g (.busy r)) with
    | none => simp [h] at done
    | some s => simp [h] at done; cases done; exact ⟨_,rfl,rfl,rfl,rfl,rfl,rfl,rfl⟩
  · simp at done

-- One resumed attempt has one declared work overhead. Interruption delay is
-- separate; it is not silently treated as a zero-time restart.
def debit (d : Device) : Option Device :=
  (EffectiveCommand.spend 1 1 (state d)).map (setState d)

theorem debit_shape (d : Device) (fuel : 1≤(state d).reserve) (time : (state d).time+1≤(state d).deadline) :
    debit d = some (setState d {state d with
      reserve := (state d).reserve-1
      spent := (state d).spent+1
      time := (state d).time+1}) := by
  simp [debit,EffectiveCommand.spend,fuel,time]

theorem tick_available_and_preserves_control (r : Pending) (fuel : 1≤(state (.busy r)).reserve)
    (time : (state (.busy r)).time+1≤(state (.busy r)).deadline) :
    ∃ out, RecoverableControl.tick (.busy r)=some out ∧ control out=control (.busy r) ∧
      (state out).reserve+1=(state (.busy r)).reserve ∧ (state out).time=(state (.busy r)).time+1 ∧
      (state out).deadline=(state (.busy r)).deadline := by
  have hf : 1 ≤ r.target.tracked.installation.state.reserve := fuel
  have ht : r.target.tracked.installation.state.time+1 ≤ r.target.tracked.installation.state.deadline := time
  have hs : EffectiveCommand.spend 1 1 r.target.tracked.installation.state =
      some {r.target.tracked.installation.state with
        reserve := r.target.tracked.installation.state.reserve-1
        spent := r.target.tracked.installation.state.spent+1
        time := r.target.tracked.installation.state.time+1} := by
    simp [EffectiveCommand.spend,hf,ht]
  let funded : Pending := {r with
    target := accounting r.target {r.target.tracked.installation.state with
      reserve := r.target.tracked.installation.state.reserve-1
      spent := r.target.tracked.installation.state.spent+1
      time := r.target.tracked.installation.state.time+1}}
  cases htod : r.todo with
  | nil =>
    refine ⟨.ready {funded.target with tracked := {funded.target.tracked with actual := funded.actual}},by simp [RecoverableControl.tick,charge,hs,htod,funded],rfl,?_,rfl,rfl⟩
    dsimp [state,book,accounting,funded]; omega
  | cons w rest =>
    refine ⟨.busy {funded with actual := oneWrite w funded.actual,todo := rest},by simp [RecoverableControl.tick,charge,hs,htod,funded],rfl,?_,rfl,rfl⟩
    dsimp [state,book,accounting,funded]; omega

inductive Attempt where | advance | interrupted : Nat → Attempt
  deriving DecidableEq, Repr

def admissible (bound : Nat) : Attempt → Prop
  | .advance => True | .interrupted delay => delay≤bound

def attempt (a : Attempt) (d : Device) : Option Device := match a with
  | .advance => RecoverableControl.tick d
  | .interrupted delay => debit (RecoverableControl.crash delay d)

theorem eligibility_follows_control (g : Grant) (d out : Device) (same : control out=control d) :
    eligible g out=eligible g d := by
  unfold control at same
  have eq := Prod.mk.inj same
  rcases eq with ⟨ha,hrest⟩
  rcases Prod.mk.inj hrest with ⟨hr,hrest⟩
  rcases Prod.mk.inj hrest with ⟨hs,hm⟩
  simp [eligible,ha,hr,hs,hm]

theorem recovery_attempt_keeps_stop_margin (a : Attempt) (bound : Nat) (g : Grant) (r : Pending)
    (armed : Armed g (.busy r)) (allowed : admissible bound a)
    (fuel : 4≤(state (.busy r)).reserve)
    (time : (state (.busy r)).time+bound+4≤(state (.busy r)).deadline) :
    ∃ out, attempt a (.busy r)=some out ∧ Armed g out ∧
      (state out).reserve+1=(state (.busy r)).reserve := by
  cases a with
  | advance =>
    obtain ⟨out,done,ctrl,cost,clock,deadline⟩ := tick_available_and_preserves_control r (by omega) (by omega)
    refine ⟨out,done,⟨tick_preserves_safety _ _ armed.1 done,?_,by omega,by omega⟩,cost⟩
    exact (eligibility_follows_control g _ _ ctrl).trans armed.2.1
  | interrupted delay =>
    let crashed := RecoverableControl.crash delay (.busy r)
    have hf : 1≤(state crashed).reserve := by
      dsimp [crashed,RecoverableControl.crash,accounting,state,book]
      dsimp [state,book] at fuel; omega
    have ht : (state crashed).time+1≤(state crashed).deadline := by
      dsimp [crashed,RecoverableControl.crash,accounting,state,book]
      change delay≤bound at allowed
      dsimp [state,book] at time; omega
    let out := setState crashed {state crashed with
      reserve := (state crashed).reserve-1
      spent := (state crashed).spent+1
      time := (state crashed).time+1}
    have done : attempt (.interrupted delay) (.busy r)=some out := debit_shape crashed hf ht
    refine ⟨out,done,⟨setState_preserves_evidence _ _ (crash_preserves_safety _ _ armed.1),?_,?_,?_⟩,?_⟩
    · exact armed.2.1
    · dsimp [out,crashed,setState,mapBook,RecoverableControl.crash,accounting,state,book]
      dsimp [state,book] at fuel; omega
    · dsimp [out,crashed,setState,mapBook,RecoverableControl.crash,accounting,state,book]
      change delay≤bound at allowed
      dsimp [state,book] at time; omega
    · dsimp [out,crashed,setState,mapBook,RecoverableControl.crash,accounting,state,book]
      dsimp [state,book] at fuel; omega

inductive Supervisor where
  | active : Grant → Nat → Device → Supervisor
  | stopped : Device → Supervisor
  deriving DecidableEq, Repr

def stopped : Supervisor → Bool | .active _ _ _ => false | .stopped _ => true

def cycle (a : Attempt) : Supervisor → Option Supervisor
  | .stopped d => some (.stopped d)
  | .active g bound d =>
      match d with
      | .ready _ => (stop g d).map Supervisor.stopped
      | .busy _ =>
        if 4≤(state d).reserve ∧ (state d).time+bound+4≤(state d).deadline then
          (attempt a d).map (Supervisor.active g bound)
        else (stop g d).map Supervisor.stopped

def Valid : Supervisor → Prop
  | .active g _ d => Armed g d
  | .stopped d => Safe d ∧ Stopped d

theorem cycle_keeps_access_or_stops (a : Attempt) (g : Grant) (bound : Nat) (d : Device)
    (armed : Armed g d) (allowed : admissible bound a) :
    ∃ out, cycle a (.active g bound d)=some out ∧ Valid out ∧
      (stopped out=true ∨ ∃ next, out=.active g bound next ∧ (state next).reserve+1=(state d).reserve) := by
  cases d with
  | ready m =>
    obtain ⟨out,done,halt,safe,_,_,_,_,_⟩ := stop_executes_current_authorized_command g (.ready m) armed
    exact ⟨.stopped out,by simp [cycle,done],⟨safe,halt⟩,Or.inl rfl⟩
  | busy r =>
    by_cases room : 4≤(state (.busy r)).reserve ∧ (state (.busy r)).time+bound+4≤(state (.busy r)).deadline
    · obtain ⟨next,done,safe,cost⟩ := recovery_attempt_keeps_stop_margin a bound g r armed allowed room.1 room.2
      exact ⟨.active g bound next,by simp [cycle,room,done],safe,Or.inr ⟨next,rfl,cost⟩⟩
    · obtain ⟨out,done,halt,safe,_,_,_,_,_⟩ := stop_executes_current_authorized_command g (.busy r) armed
      exact ⟨.stopped out,by simp [cycle,room,done],⟨safe,halt⟩,Or.inl rfl⟩

def run : List Attempt → Supervisor → Option Supervisor
  | [],s => some s
  | a::rest,s => (cycle a s).bind (run rest)

-- The Option executor above specifies completion. This operational executor
-- also retains the physically elapsed interruption on an unsuccessful cycle.
def failedSnapshot (a : Attempt) : Supervisor → Supervisor
  | .active g bound (.busy r) =>
    if 4≤(state (.busy r)).reserve ∧ (state (.busy r)).time+bound+4≤(state (.busy r)).deadline then
      match a with
      | .interrupted delay => .active g bound (RecoverableControl.crash delay (.busy r))
      | .advance => .active g bound (.busy r)
    else .active g bound (.busy r)
  | s => s

def runRetained : List Attempt → Supervisor → Bool × Supervisor
  | [],s => (true,s)
  | a::rest,s => match cycle a s with
      | some next => runRetained rest next
      | none => (false,failedSnapshot a s)

theorem successful_execution_retains_exact_state (events : List Attempt) (s out : Supervisor)
    (done : run events s=some out) : runRetained events s=(true,out) := by
  induction events generalizing s with
  | nil => simp [run] at done; cases done; rfl
  | cons a rest ih =>
    cases h : cycle a s with
    | none => simp [run,h] at done
    | some next =>
      have finish : run rest next=some out := by simpa [run,h] using done
      simpa [runRetained,h] using ih next finish

theorem stopped_is_absorbing (events : List Attempt) (d : Device) : run events (.stopped d)=some (.stopped d) := by
  induction events with
  | nil => rfl
  | cons a rest ih => simpa [run,cycle] using ih

theorem every_supported_schedule_finishes (events : List Attempt) (g : Grant) (bound : Nat) (d : Device)
    (armed : Armed g d) (allowed : ∀ a∈events, admissible bound a)
    (enough : (state d).reserve ≤ events.length+2) :
    ∃ out, run events (.active g bound d)=some (.stopped out) ∧ Safe out ∧ Stopped out := by
  induction events generalizing d with
  | nil => have := armed.2.2.1; simp at enough; omega
  | cons a rest ih =>
    obtain ⟨next,done,valid,haltOr⟩ := cycle_keeps_access_or_stops a g bound d armed (allowed a (by simp))
    rcases haltOr with halt | ⟨nextD,rfl,cost⟩
    · cases next with
      | active _ _ _ => cases halt
      | stopped out =>
        exact ⟨out,by simp [run,done,stopped_is_absorbing],valid⟩
    · have enoughNext : (state nextD).reserve ≤ rest.length+2 := by simp only [List.length_cons] at enough; omega
      obtain ⟨out,finish,safe,halt⟩ := ih nextD valid (fun a h => allowed a (by simp [h])) enoughNext
      exact ⟨out,by simpa [run,done] using finish,safe,halt⟩

-- Preflight checks the prospective target before making any actual field write.
def preflight (p : Packet) (g : Grant) (bound : Nat) (m : Machine) : Option Supervisor := do
  let d ← RecoverableControl.prepare p (.ready m)
  if eligible g d && decide (3≤(state d).reserve ∧ (state d).time+3≤(state d).deadline)
    then some (.active g bound d) else none

theorem admission_establishes_stop_access (p : Packet) (g : Grant) (bound : Nat) (m : Machine)
    (known : Known m.tracked) (out : Supervisor) (done : preflight p g bound m=some out) : Valid out := by
  unfold preflight at done
  cases hp : RecoverableControl.prepare p (.ready m) with
  | none => simp [hp] at done
  | some d =>
    simp only [hp,Bind.bind,Option.bind] at done
    split at done
    · rename_i checks
      simp only [Bool.and_eq_true_iff,decide_eq_true_eq] at checks
      cases done
      exact ⟨prepare_preserves_safety p (.ready m) d known hp,checks.1,checks.2⟩
    · simp at done

def inspected (fuel deadline : Nat) : Machine :=
  (MediatedControl.run (inspectEvents splitReports) (MediatedControl.start ⟨.left,some 0⟩ fuel deadline)).2

def grant : Grant := ⟨8,true,1,true⟩
def scenario (fuel deadline : Nat) : Option Supervisor := preflight repair grant 1 (inspected fuel deadline)
def executeExample (fuel deadline : Nat) (events : List Attempt) : Option Supervisor :=
  (scenario fuel deadline).bind (run events)
def terminal : Supervisor → Option Device | .stopped d => some d | _ => none

theorem old_exhaustion_entry_is_refused : scenario 9 30=none := by decide

theorem incomplete_recovery_reaches_real_shutdown :
    let result := (executeExample 12 30 [.advance,.advance]).bind terminal
    result.map (fun d => ((state d).completed,(state d).running,(state d).spent,(state d).reserve,
      (actual d).model,(actual d).fault,(book d).journal.length,(RecoverableControl.published d).isNone)) =
        some (true,false,12,0,.right,some 0,1,true) := by rfl

theorem repeated_interruptions_cannot_spend_stop_reserve :
    let result := (executeExample 14 30 (List.replicate 4 (.interrupted 1))).bind terminal
    result.map (fun d => ((state d).completed,(state d).running,(state d).spent,(state d).time,(actual d).model,(actual d).fault)) =
      some (true,false,14,17,.left,some 0) := by rfl

theorem deadline_margin_stops_before_retry :
    let result := (executeExample 30 12 [.interrupted 1]).bind terminal
    result.map (fun d => ((state d).completed,(state d).running,(state d).spent,(state d).time)) =
      some (true,false,11,11) := by decide

theorem stale_grant_is_refused : preflight repair {grant with epoch := 7} 1 (inspected 30 30)=none := by decide

theorem no_shutdown_mandate_is_refused :
    let m := inspected 30 30
    preflight repair grant 1 {m with tracked := {m.tracked with installation :=
      {m.tracked.installation with mandate := ⟨true,true,false⟩}}}=none := by decide

-- Delay beyond the admitted bound is a real failure, not silently clamped.
theorem uncovered_long_interrupt_breaks_completion :
    let result := executeExample 14 15 [.interrupted 10,.advance]
    result=none := by decide


theorem failed_interrupt_retains_elapsed_time :
    let result := (scenario 14 15).map (runRetained [.interrupted 10,.advance])
    result.map (fun pair => (pair.1,match pair.2 with
      | .active g _ d => ((state d).time,(state d).spent,(state d).running,(stop g d).isNone)
      | .stopped _ => (0,0,false,false))) = some (false,(18,8,true,true)) := by decide

end ReservedShutdown
