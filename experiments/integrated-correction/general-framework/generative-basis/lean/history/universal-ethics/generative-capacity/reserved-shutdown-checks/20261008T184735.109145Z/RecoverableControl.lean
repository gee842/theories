import MediatedControl

/-! Interrupted controlled change within one unfolding of actual writes,
retained descriptions and response access. The durable descriptor and each
microstep are assumed atomic/protected; whole-program atomicity is not.
Only overwrite instructions are replayed. A crash preserves actual effects,
prepared state and consumption, resets progress, and adds supplied delay. -/
namespace RecoverableControl
open MediatedControl TemporalInspection EvidenceQualifiedCorrection FaultTolerantCorrection CorrectionReconfiguration FallibleInspection

def SameUntouched (p : List Write) (a b : World) : Prop :=
  (modelTouched p = false → a.model=b.model) ∧
  (faultTouched p = false → a.fault=b.fault)

theorem exact_result_from_untouched (p : List Write) (a b : World)
    (same : SameUntouched p a b) : writes p a = writes p b := by
  induction p generalizing a b with
  | nil => exact world_fields_determine_state (same.1 rfl) (same.2 rfl)
  | cons op rest ih =>
      apply ih
      constructor
      · intro h
        cases op <;> simp only [oneWrite]
        all_goals first | rfl | exact same.1 (by simpa [modelTouched] using h)
      · intro h
        cases op <;> simp only [oneWrite]
        all_goals first | rfl | exact same.2 (by simpa [faultTouched] using h)

theorem member_preserves_untouched (p : List Write) (op : Write) (a b : World)
    (member : op ∈ p) (same : SameUntouched p a b) : SameUntouched p (oneWrite op a) b := by
  have modelKeep : modelTouched p = false → (oneWrite op a).model = a.model := by
    clear same
    intro untouched
    induction p with
    | nil => simp at member
    | cons head rest ih =>
      simp only [List.mem_cons] at member
      rcases member with equal | tail
      · subst op
        cases head <;> simp_all [modelTouched,oneWrite]
      · cases head <;> simp_all [modelTouched]
  have faultKeep : faultTouched p = false → (oneWrite op a).fault = a.fault := by
    clear same modelKeep
    intro untouched
    induction p with
    | nil => simp at member
    | cons head rest ih =>
      simp only [List.mem_cons] at member
      rcases member with equal | tail
      · subst op
        cases head <;> simp_all [faultTouched,oneWrite]
      · cases head <;> simp_all [faultTouched]
  exact ⟨fun h => (modelKeep h).trans (same.1 h),fun h => (faultKeep h).trans (same.2 h)⟩

-- Only accounting changes here; evidence, authority and configuration do not.
def accounting (m : Machine) (s : EffectiveCommand.State) : Machine :=
  {m with tracked := {m.tracked with installation := {m.tracked.installation with state := s}}}

theorem accounting_preserves_coverage (m : Machine) (s : EffectiveCommand.State)
    (known : Known m.tracked) : Known (accounting m s).tracked := known

structure Pending where
  origin : Machine
  program : List Write
  target : Machine
  actual : World
  todo : List Write
  deriving DecidableEq, Repr

inductive Device where
  | ready : Machine → Device
  | busy : Pending → Device
  deriving DecidableEq, Repr

def Coherent (r : Pending) : Prop :=
  Known r.target.tracked ∧
  r.target.tracked.actual = writes r.program r.origin.tracked.actual ∧
  SameUntouched r.program r.actual r.origin.tracked.actual ∧
  writes r.todo r.actual = r.target.tracked.actual ∧
  (∀ op ∈ r.todo, op ∈ r.program)

def Safe : Device → Prop
  | .ready m => Known m.tracked
  | .busy r => Coherent r

def prepare (p : Packet) : Device → Option Device
  | .busy _ => none
  | .ready m => (commit p m).map (fun target => .busy ⟨m,p.program,target,m.tracked.actual,p.program⟩)

def charge (r : Pending) : Option Pending :=
  (EffectiveCommand.spend 1 1 r.target.tracked.installation.state).map
    (fun state => {r with target := accounting r.target state})

def tick : Device → Option Device
  | .ready _ => none
  | .busy r => do
      let funded ← charge r
      match funded.todo with
      | [] => return .ready {funded.target with tracked := {funded.target.tracked with actual := funded.actual}}
      | op::rest => return .busy {funded with actual := oneWrite op funded.actual,todo := rest}

def crash (delay : Nat) : Device → Device
  | .ready m => .ready (accounting m {m.tracked.installation.state with time := m.tracked.installation.state.time+delay})
  | .busy r => .busy {r with
      todo := r.program
      target := accounting r.target {r.target.tracked.installation.state with time := r.target.tracked.installation.state.time+delay}}

-- No ordinary read, command or competing patch is admitted while incomplete.
def use (e : MediatedControl.Event) : Device → Option Device
  | .busy _ => none
  | .ready m => match e with
      | .patch _ => none
      | _ => (MediatedControl.step e m).map Device.ready

theorem pending_blocks_use (r : Pending) (e : MediatedControl.Event) : use e (.busy r) = none := rfl

theorem prepare_preserves_safety (p : Packet) (d out : Device) (safe : Safe d)
    (done : prepare p d = some out) : Safe out := by
  cases d with
  | busy r => simp [prepare] at done
  | ready m =>
    cases h : commit p m with
    | none => simp [prepare,h] at done
    | some target =>
      simp [prepare,h] at done
      cases done
      refine ⟨commit_preserves_actual_coverage p m target safe h,?_,⟨fun _ => rfl,fun _ => rfl⟩,?_,fun _ h => h⟩
      · exact (commit_records_the_executed_effect p m target h).1
      · exact (commit_records_the_executed_effect p m target h).1.symm

theorem charge_keeps_structure (r paid : Pending) (done : charge r = some paid) :
    paid.origin = r.origin ∧ paid.program = r.program ∧ paid.actual = r.actual ∧ paid.todo = r.todo ∧
    paid.target.tracked.actual = r.target.tracked.actual ∧ paid.target.tracked.possible = r.target.tracked.possible ∧
    paid.target.tracked.installation.state.spent = r.target.tracked.installation.state.spent+1 ∧
    paid.target.tracked.installation.state.reserve+paid.target.tracked.installation.state.spent =
      r.target.tracked.installation.state.reserve+r.target.tracked.installation.state.spent := by
  unfold charge at done
  cases hs : EffectiveCommand.spend 1 1 r.target.tracked.installation.state with
  | none => simp [hs] at done
  | some s =>
    simp [hs] at done
    cases done
    have budget := EffectiveCommand.spend_conserves hs
    have cost : s.spent = r.target.tracked.installation.state.spent+1 := by
      unfold EffectiveCommand.spend at hs
      split at hs
      · cases hs; rfl
      · cases hs
    exact ⟨rfl,rfl,rfl,rfl,rfl,rfl,cost,budget.1⟩

theorem charge_preserves_coherence (r paid : Pending) (safe : Coherent r)
    (done : charge r = some paid) : Coherent paid := by
  have shape := charge_keeps_structure r paid done
  rcases shape with ⟨ho,hp,ha,ht,hactual,hpossible,_,_⟩
  unfold Coherent SameUntouched at *
  simp only [Known] at *
  simpa only [ho,hp,ha,ht,hactual,hpossible] using safe

theorem tick_preserves_safety (d out : Device) (safe : Safe d) (done : tick d = some out) : Safe out := by
  cases d with
  | ready m => simp [tick] at done
  | busy r =>
    cases hc : charge r with
    | none => simp [tick,hc] at done
    | some funded =>
      have good := charge_preserves_coherence r funded safe hc
      cases ht : funded.todo with
      | nil =>
        simp [tick,hc,ht] at done
        cases done
        have equal : funded.actual = funded.target.tracked.actual := by simpa [ht,writes] using good.2.2.2.1
        simpa [Safe,Known,equal] using good.1
      | cons op rest =>
        simp [tick,hc,ht] at done
        cases done
        refine ⟨good.1,good.2.1,?_,?_,?_⟩
        · exact member_preserves_untouched funded.program op funded.actual funded.origin.tracked.actual
            (good.2.2.2.2 op (by simp [ht])) good.2.2.1
        · simpa [ht,writes] using good.2.2.2.1
        · intro x hx
          exact good.2.2.2.2 x (by simp [ht,hx])

theorem crash_preserves_safety (d : Device) (delay : Nat) (safe : Safe d) : Safe (crash delay d) := by
  cases d with
  | ready m => exact safe
  | busy r =>
    refine ⟨safe.1,safe.2.1,safe.2.2.1,?_,fun _ h => h⟩
    exact (exact_result_from_untouched _ _ _ safe.2.2.1).trans safe.2.1.symm

inductive Event where
  | prepare : Packet → Event
  | tick : Event
  | crash : Nat → Event
  | use : MediatedControl.Event → Event
  deriving DecidableEq, Repr

def step (e : Event) (d : Device) : Option Device := match e with
  | .prepare p => prepare p d | .tick => tick d | .crash delay => some (crash delay d) | .use e => use e d

def SourceLaw (e : Event) (d : Device) : Prop := match e,d with
  | .use e,.ready m => MediatedControl.SourceLaw e m
  | _,_ => True

theorem step_preserves_safety (e : Event) (d out : Device) (safe : Safe d)
    (source : SourceLaw e d) (done : step e d = some out) : Safe out := by
  cases e with
  | prepare p => exact prepare_preserves_safety _ _ _ safe done
  | tick => exact tick_preserves_safety _ _ safe done
  | crash delay => simp [step] at done; cases done; exact crash_preserves_safety _ _ safe
  | use e =>
    cases d with
    | busy r => simp [step,use] at done
    | ready m =>
      cases e with
      | patch p => simp [step,use] at done
      | read d r =>
        cases hs : MediatedControl.step (.read d r) m with
        | none => simp [step,use,hs] at done
        | some after =>
          simp [step,use,hs] at done
          cases done
          exact mediated_step_preserves_coverage (.read d r) m after safe source hs
      | command =>
        cases hs : MediatedControl.step .command m with
        | none => simp [step,use,hs] at done
        | some after =>
          simp [step,use,hs] at done
          cases done
          exact mediated_step_preserves_coverage .command m after safe source hs


inductive History : Device → Device → Prop where
  | nil (d : Device) : History d d
  | next {start before after : Device} (prior : History start before) (e : Event)
      (source : SourceLaw e before) (done : step e before = some after) : History start after

theorem interrupted_history_preserves_safety {start finish : Device} (h : History start finish)
    (safe : Safe start) : Safe finish := by
  induction h with
  | nil => exact safe
  | next prior e source done ih => exact step_preserves_safety e _ _ ih source done

theorem published_history_to_current_certificate {start : Device} {finish : Machine}
    (h : History start (.ready finish)) (safe : Safe start) (supports : Domain → Bool) (P : Prop)
    (faithful : ∀ d ∈ (describe finish.tracked.actual.model).roster,
      fails ((describe finish.tracked.actual.model).vulnerability d) (commandRoots finish.tracked.actual) = false → supports d = true → P)
    (accepted : certificate (describe finish.tracked.actual.model).roster
      (pooled describe (models finish.tracked.possible)) supports = true) : P := by
  have known : Known finish.tracked := interrupted_history_preserves_safety h safe
  exact current_pool_sound _ _ known.1 (known.2 _ known.1) supports P faithful accepted

def spent : Device → Nat | .ready m => m.tracked.installation.state.spent | .busy r => r.target.tracked.installation.state.spent
def clockTime : Device → Nat | .ready m => m.tracked.installation.state.time | .busy r => r.target.tracked.installation.state.time

theorem crash_retains_consumption (d : Device) (delay : Nat) :
    spent (crash delay d) = spent d ∧ clockTime (crash delay d) = clockTime d+delay := by
  cases d <;> exact ⟨rfl,rfl⟩

theorem tick_consumes_one (d out : Device) (done : tick d = some out) : spent out = spent d+1 := by
  cases d with
  | ready m => simp [tick] at done
  | busy r =>
    cases hc : charge r with
    | none => simp [tick,hc] at done
    | some paid =>
      have cost := (charge_keeps_structure r paid hc).2.2.2.2.2.2.1
      cases ht : paid.todo <;> simp [tick,hc,ht] at done <;> cases done <;> exact cost

def resumeSteps : Nat → Device → Option Device
  | 0,d => some d
  | n+1,d => (tick d).bind (resumeSteps n)

theorem funded_suffix_publishes (todo : List Write) (r : Pending) (remaining : r.todo=todo)
    (safe : Coherent r)
    (fuel : todo.length+1 ≤ r.target.tracked.installation.state.reserve)
    (time : r.target.tracked.installation.state.time+todo.length+1 ≤ r.target.tracked.installation.state.deadline) :
    ∃ m, resumeSteps (todo.length+1) (.busy r) = some (.ready m) ∧ Known m.tracked ∧
      m.tracked.actual = r.target.tracked.actual ∧
      m.tracked.installation.state.spent = r.target.tracked.installation.state.spent+todo.length+1 ∧
      m.tracked.installation.state.time = r.target.tracked.installation.state.time+todo.length+1 := by
  induction todo generalizing r with
  | nil =>
    let old := r.target.tracked.installation.state
    let paid : EffectiveCommand.State := {old with reserve := old.reserve-1,spent := old.spent+1,time := old.time+1}
    have available : 1 ≤ old.reserve ∧ old.time+1 ≤ old.deadline := by simpa using And.intro fuel time
    have debit : EffectiveCommand.spend 1 1 old = some paid := by simp [EffectiveCommand.spend,available,paid]
    let funded : Pending := {r with target := accounting r.target paid}
    have charged : charge r = some funded := by simp [charge,debit,old,funded]
    let out : Machine := {funded.target with tracked := {funded.target.tracked with actual := funded.actual}}
    have done : tick (.busy r) = some (.ready out) := by simp [tick,charged,funded,remaining,out]
    have equal : r.actual=r.target.tracked.actual := by simpa [remaining,writes] using safe.2.2.2.1
    refine ⟨out,?_,tick_preserves_safety (.busy r) _ safe done,?_,?_,?_⟩
    · simpa [resumeSteps] using done
    · exact equal
    · rfl
    · rfl
  | cons op rest ih =>
    let old := r.target.tracked.installation.state
    let paid : EffectiveCommand.State := {old with reserve := old.reserve-1,spent := old.spent+1,time := old.time+1}
    have available : 1 ≤ old.reserve ∧ old.time+1 ≤ old.deadline := by
      dsimp [old]; simp only [List.length_cons] at fuel time; omega
    have debit : EffectiveCommand.spend 1 1 old = some paid := by simp [EffectiveCommand.spend,available,paid]
    let funded : Pending := {r with target := accounting r.target paid}
    have charged : charge r = some funded := by simp [charge,debit,old,funded]
    let next : Pending := {funded with actual := oneWrite op funded.actual,todo := rest}
    have done : tick (.busy r) = some (.busy next) := by simp [tick,charged,funded,remaining,next]
    have nSafe : Coherent next := tick_preserves_safety (.busy r) _ safe done
    have nFuel : rest.length+1 ≤ next.target.tracked.installation.state.reserve := by
      dsimp [next,funded,accounting,paid,old]; simp only [List.length_cons] at fuel; omega
    have nTime : next.target.tracked.installation.state.time+rest.length+1 ≤ next.target.tracked.installation.state.deadline := by
      dsimp [next,funded,accounting,paid,old]; simp only [List.length_cons] at time; omega
    obtain ⟨m,finished,known,actual,cost,clock⟩ := ih next rfl nSafe nFuel nTime
    refine ⟨m,?_,known,actual,?_,?_⟩
    · simpa [List.length_cons,resumeSteps,done] using finished
    · dsimp [next,funded,accounting,paid,old] at cost
      simp only [List.length_cons]; omega
    · dsimp [next,funded,accounting,paid,old] at clock
      simp only [List.length_cons]; omega

theorem crash_keeps_pending (r : Pending) (delay : Nat) :
    ∃ after, crash delay (.busy r) = .busy after ∧ after.todo=r.program ∧ after.actual=r.actual := by
  exact ⟨_,rfl,rfl,rfl⟩

-- Concrete interruptions preserve their prefix. A processed command may still fail.
def run : List Event → Device → Bool × Device
  | [],d => (true,d)
  | e::es,d => match step e d with | none => (false,d) | some next => run es next

def initial (fuel deadline : Nat) : Device := .ready (MediatedControl.start ⟨.left,some 0⟩ fuel deadline)
def scan : List Event := (inspectEvents splitReports).map Event.use
def noCrash : List Event := scan ++ [.prepare repair,.tick,.tick,.tick,.use .command]
def oneCrash : List Event := scan ++ [.prepare repair,.tick,.crash 1,.tick,.tick,.tick,.use .command]
def published : Device → Option Machine | .ready m => some m | .busy _ => none

theorem staged_change_then_actual_shutdown :
    let m := (published (run noCrash (initial 22 22)).2).getD (MediatedControl.start ⟨.left,some 0⟩ 0 0)
    m.tracked.actual = ⟨.right,some 2⟩ ∧ m.tracked.installation.state.completed = true ∧
    m.tracked.installation.state.running = false ∧ m.tracked.installation.state.spent = 22 ∧
    m.tracked.installation.state.reserve = 0 := by decide

theorem interrupted_change_then_actual_shutdown :
    let m := (published (run oneCrash (initial 23 24)).2).getD (MediatedControl.start ⟨.left,some 0⟩ 0 0)
    m.tracked.actual = ⟨.right,some 2⟩ ∧ m.tracked.installation.state.completed = true ∧
    m.tracked.installation.state.running = false ∧ m.tracked.installation.state.spent = 23 ∧
    m.tracked.installation.state.time = 24 ∧ m.tracked.installation.serial = 2 ∧ m.journal.length = 1 := by decide

theorem interruption_can_exhaust_execution_capacity :
    let m := (published (run oneCrash (initial 22 24)).2).getD (MediatedControl.start ⟨.left,some 0⟩ 0 0)
    m.tracked.installation.state.completed = false ∧ m.tracked.installation.state.spent = 20 ∧
    m.tracked.installation.state.reserve = 2 := by decide

theorem interruption_delay_can_miss_deadline :
    let m := (published (run oneCrash (initial 23 23)).2).getD (MediatedControl.start ⟨.left,some 0⟩ 0 0)
    m.tracked.installation.state.completed = false ∧ m.tracked.installation.state.time = 21 ∧
    m.tracked.installation.state.spent = 20 := by decide

theorem exhausted_recovery_blocks_shutdown :
    let d := (run (scan ++ [.prepare repair,.tick]) (initial 9 30)).2
    published d = none ∧ tick d = none ∧ use .command d = none ∧ spent d = 9 ∧
    (match d with
      | .busy r => r.actual == ⟨.right,some 0⟩ && r.target.tracked.installation.state.running
      | .ready _ => false) = true := by decide

def partiallyChanged : Device := (run (scan ++ [.prepare repair,.tick,.tick]) (initial 30 30)).2
-- This fault deletes the durable pending marker and exposes old bookkeeping.
def loseMarker : Device → Device
  | .ready m => .ready m
  | .busy r => .ready {r.origin with tracked := {r.origin.tracked with actual := r.actual}}

theorem losing_pending_marker_exposes_false_certificate :
    let m := (published (loseMarker partiallyChanged)).getD (MediatedControl.start ⟨.left,some 0⟩ 0 0)
    published partiallyChanged = none ∧ use .command partiallyChanged = none ∧
    m.tracked.actual ∉ m.tracked.possible ∧
    induced (describe m.tracked.actual.model) (roots m.tracked.actual) = [2,3] ∧
    certificate roster4 (pooled describe (models m.tracked.possible)) (fun d => decide (2≤d)) = true := by decide

end RecoverableControl
