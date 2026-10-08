import FallibleInspection

/-! A bounded observer for actual histories of control and fault changes.
Prediction expands possibilities before later reports constrain them. The
transition relation is supplied; it is not inferred from a notice or clock.
Recording, local atomic steps and current command execution remain protected.
No physical recovery or ethical legitimacy follows from a passing filter. -/
namespace TemporalInspection
open FallibleInspection EvidenceQualifiedCorrection FaultTolerantCorrection CorrectionReconfiguration

structure World where
  model : Model
  fault : Option Nat
  deriving DecidableEq, Repr

def roots (w : World) : List Nat := w.fault.toList
-- Cause 4 affects only the diagnostic role. This projects the same causal
-- state to the already established four-position command interface.
def commandRoots (w : World) : List Nat := (roots w).filter (fun r => r < 4)
def worlds : List World := hypotheses.flatMap (fun h =>
  [none,some 0,some 1,some 2,some 3,some 4].map (fun r => ⟨h,r⟩))

def fits (w : World) (d : Domain) (report : Option Bool) : Bool :=
  fails ((auditArrangement true w.model).vulnerability d) (roots w) ||
    report.isNone || report == some (diagnostic w.model)

def receive (possible : List World) (d : Domain) (report : Option Bool) : List World :=
  possible.filter (fun w => fits w d report)

inductive Change where
  | steady | mobile | control | reset
  deriving DecidableEq, Repr

def successors (c : Change) (w : World) : List World := worlds.filter (fun v => match c with
  | .steady => v == w
  | .mobile => v.model == w.model
  | .control => v.fault == w.fault
  | .reset => true)

def predict (c : Change) (possible : List World) : List World :=
  worlds.filter (fun v => possible.any (fun w => (successors c w).contains v))

def models (possible : List World) : List Model := possible.map World.model

theorem received_actual_retained (possible : List World) (actual : World)
    (known : actual ∈ possible) (d : Domain) (report : Option Bool)
    (lawful : fits actual d report = true) : actual ∈ receive possible d report :=
  List.mem_filter.mpr ⟨known,lawful⟩

theorem prediction_contains_successor (c : Change) (possible : List World) (old new : World)
    (known : old ∈ possible) (lawful : new ∈ successors c old) : new ∈ predict c possible := by
  apply List.mem_filter.mpr
  refine ⟨(List.mem_filter.mp lawful).1,?_⟩
  exact List.any_eq_true.mpr ⟨old,known,by simpa using lawful⟩

theorem received_possible_subset (possible : List World) (d : Domain) (report : Option Bool) :
    ∀ w ∈ receive possible d report, w ∈ possible := by
  intro w hw
  exact (List.mem_filter.mp hw).1

theorem predicted_world_is_represented (c : Change) (possible : List World) :
    ∀ w ∈ predict c possible, w ∈ worlds := by
  intro w hw
  exact (List.mem_filter.mp hw).1

theorem missing_report_retains_worlds (possible : List World) (d : Domain) :
    receive possible d none = possible := by
  apply List.filter_eq_self.mpr
  intro w hw
  simp [fits]

theorem projected_model_contains_actual (possible : List World) (actual : World)
    (known : actual ∈ possible) : actual.model ∈ models possible :=
  List.mem_map.mpr ⟨actual,known,rfl⟩

theorem command_projection_matches_physical_causes :
    worlds.all (fun w => roster4.all (fun d =>
      fails ((describe w.model).vulnerability d) (roots w) ==
      fails ((describe w.model).vulnerability d) (commandRoots w))) = true := by decide

theorem represented_command_coverage :
    worlds.all (fun w => (describe w.model).rootFaults.any (fun b =>
      (commandRoots w).all (fun r => b.contains r))) = true := by decide

theorem covered_command_world (w : World) (represented : w ∈ worlds) :
    Covered (describe w.model) (commandRoots w) := by
  have one := List.all_eq_true.mp represented_command_coverage w represented
  obtain ⟨b,hb,contains⟩ := List.any_eq_true.mp one
  exact ⟨b,hb,fun r hr => by simpa using List.all_eq_true.mp contains r hr⟩

theorem current_pool_sound (possible : List World) (actual : World)
    (known : actual ∈ possible) (represented : actual ∈ worlds)
    (supports : Domain → Bool) (P : Prop)
    (faithful : ∀ d ∈ (describe actual.model).roster,
      fails ((describe actual.model).vulnerability d) (commandRoots actual) = false → supports d = true → P)
    (accepted : certificate (describe actual.model).roster (pooled describe (models possible)) supports = true) : P :=
  pooled_certificate_sound describe _ actual.model (projected_model_contains_actual _ _ known)
    (commandRoots actual) (covered_command_world actual represented) supports P faithful accepted

inductive Record where
  | read : Domain → Option Bool → Record
  | change : Change → Record
  | command : Record
  deriving DecidableEq, Repr

structure State where
  actual : World
  possible : List World
  installation : Installation
  records : List Record := []
  inspectionAllowed : Bool := true
  changeAllowed : Bool := true
  deriving DecidableEq, Repr

def Known (s : State) : Prop := s.actual ∈ s.possible ∧ ∀ w ∈ s.possible, w ∈ worlds

def read (d : Domain) (report : Option Bool) (s : State) : Option State := do
  if !s.inspectionAllowed || !(auditRoster true).contains d then none else do
    let paid ← EffectiveCommand.spend 1 1 s.installation.state
    return {s with
      possible := receive s.possible d report
      installation := {s.installation with state := paid}
      records := s.records ++ [.read d report]}

def changeCost : Change → Nat | .steady => 0 | .mobile => 0 | .control => 2 | .reset => 2

def move (c : Change) (next : World) (s : State) : Option State := do
  if changeCost c > 0 && !s.changeAllowed then none else do
    let paid ← EffectiveCommand.spend (changeCost c) (changeCost c) s.installation.state
    return {s with
      actual := next
      possible := predict c s.possible
      installation := {s.installation with state := paid}
      records := s.records ++ [.change c]}

-- next is supplied by the represented physical transition. It is not an
-- observation given to predict; the public change record contains only c.
def asSituation (s : State) : Situation :=
  ⟨s.actual.model,models s.possible,commandRoots s.actual,s.installation,s.inspectionAllowed,none⟩

def respond (s : State) : State :=
  let out := (EvidenceQualifiedCorrection.respond (asSituation s) ()).getD (asSituation s)
  {s with installation := out.installation,records := s.records ++ [.command]}

inductive Event where
  | read : Domain → Option Bool → Event
  | move : Change → World → Event
  | command : Event
  deriving DecidableEq, Repr

def execute (e : Event) (s : State) : Option State := match e with
  | .read d r => read d r s
  | .move c w => move c w s
  | .command => some (respond s)

def Lawful (e : Event) (s : State) : Prop := match e with
  | .read d r => fits s.actual d r = true
  | .move c w => w ∈ successors c s.actual
  | .command => True

theorem reading_preserves_known (s out : State) (d : Domain) (r : Option Bool)
    (known : Known s) (lawful : fits s.actual d r = true) (done : read d r s = some out) : Known out := by
  unfold read at done
  split at done
  · simp at done
  · cases paid : EffectiveCommand.spend 1 1 s.installation.state with
    | none => simp [paid] at done
    | some value =>
      simp [paid] at done
      cases done
      exact ⟨received_actual_retained _ _ known.1 d r lawful,
        fun w hw => known.2 w (received_possible_subset _ _ _ w hw)⟩

theorem movement_preserves_known (s out : State) (c : Change) (next : World)
    (known : Known s) (lawful : next ∈ successors c s.actual)
    (done : move c next s = some out) : Known out := by
  unfold move at done
  split at done
  · simp at done
  · cases paid : EffectiveCommand.spend (changeCost c) (changeCost c) s.installation.state with
    | none => simp [paid] at done
    | some value =>
      simp [paid] at done
      cases done
      exact ⟨prediction_contains_successor c _ _ _ known.1 lawful,predicted_world_is_represented _ _⟩

theorem responding_preserves_known (s : State) (known : Known s) : Known (respond s) := known

theorem lawful_step_preserves_known (e : Event) (s out : State) (known : Known s)
    (lawful : Lawful e s) (done : execute e s = some out) : Known out := by
  cases e with
  | read d r => exact reading_preserves_known s out d r known lawful done
  | move c w => exact movement_preserves_known s out c w known lawful done
  | command =>
      simp only [execute,Option.some.injEq] at done
      cases done
      exact responding_preserves_known s known

inductive History : State → State → Prop where
  | nil (s : State) : History s s
  | step {start before after : State} (earlier : History start before) (e : Event)
      (lawful : Lawful e before) (done : execute e before = some after) : History start after

theorem lawful_history_preserves_known {start finish : State}
    (history : History start finish) (known : Known start) : Known finish := by
  induction history with
  | nil => exact known
  | step earlier e lawful done ih => exact lawful_step_preserves_known e _ _ ih lawful done

theorem history_to_current_certificate {start finish : State} (history : History start finish)
    (known : Known start) (supports : Domain → Bool) (P : Prop)
    (faithful : ∀ d ∈ (describe finish.actual.model).roster,
      fails ((describe finish.actual.model).vulnerability d) (commandRoots finish.actual) = false → supports d = true → P)
    (accepted : certificate (describe finish.actual.model).roster
      (pooled describe (models finish.possible)) supports = true) : P := by
  have retained := lawful_history_preserves_known history known
  exact current_pool_sound _ _ retained.1 (retained.2 _ retained.1) supports P faithful accepted

theorem history_to_actual_completion {start finish : State} (history : History start finish)
    (known : Known start)
    (apart : separated (describe finish.actual.model).roster (pooled describe (models finish.possible)))
    (p : Request) (reads : Readings) (approvals : Approvals)
    (current : fresh finish.installation p = true)
    (readResponses : ∀ d ∈ (describe finish.actual.model).roster,
      fails ((describe finish.actual.model).vulnerability d) (commandRoots finish.actual) = false →
      reads d = some (expected p))
    (issueResponses : ∀ d ∈ (describe finish.actual.model).roster,
      fails ((describe finish.actual.model).vulnerability d) (commandRoots finish.actual) = false →
      approvals d = some p)
    (readFaithful : ∀ d ∈ (describe finish.actual.model).roster,
      fails ((describe finish.actual.model).vulnerability d) (commandRoots finish.actual) = false →
      ∀ o, reads d = some o → o = observed finish.installation p.address)
    (issueFaithful : ∀ d ∈ (describe finish.actual.model).roster,
      fails ((describe finish.actual.model).vulnerability d) (commandRoots finish.actual) = false →
      approvals d = some p → withinMandate finish.installation p = true)
    (funded : (describe finish.actual.model).roster.length*(p.address.length+2)+3 ≤ finish.installation.state.reserve)
    (timely : finish.installation.state.time+(describe finish.actual.model).roster.length*(p.address.length+2)+3 ≤
      finish.installation.state.deadline) :
    (guardedExecute (describe finish.actual.model).roster (pooled describe (models finish.possible))
      (pooled describe (models finish.possible)) finish.installation p reads approvals).succeeded = true ∧
    (guardedExecute (describe finish.actual.model).roster (pooled describe (models finish.possible))
      (pooled describe (models finish.possible)) finish.installation p reads approvals).installation.state.completed = true ∧
    withinMandate finish.installation p = true := by
  have maintained := lawful_history_preserves_known history known
  have neutral : retain (models finish.possible) (fun _ => false) false = models finish.possible :=
    List.filter_eq_self.mpr (by intros; rfl)
  have result := evidence_qualified_completion describe (models finish.possible) (fun _ => false)
    finish.actual.model (projected_model_contains_actual _ _ maintained.1) (commandRoots finish.actual)
    (covered_command_world _ (maintained.2 _ maintained.1))
    (by simpa only [neutral] using apart) finish.installation p reads approvals current
    readResponses issueResponses readFaithful issueFaithful funded timely
  simpa only [neutral] using result

-- Operational histories retain records of their costs and input order.
def run : List Event → State → Option State
  | [],s => some s
  | e::es,s => do let next ← execute e s; run es next

-- A blocked later step retains every earlier observation and expenditure.
def runUntilBlocked : List Event → State → Bool × State
  | [],s => (true,s)
  | e::es,s => match execute e s with
    | none => (false,s)
    | some next => runUntilBlocked es next

theorem completed_run_preserves_its_executed_prefix (events : List Event) (start finish : State)
    (done : run events start = some finish) : runUntilBlocked events start = (true,finish) := by
  induction events generalizing start with
  | nil =>
      simp [run] at done
      cases done
      rfl
  | cons e es ih =>
      cases step : execute e start with
      | none => simp [run,step] at done
      | some next =>
          have tail : run es next = some finish := by simpa [run,step] using done
          simpa [runUntilBlocked,step] using ih next tail

-- This is an omniscient specification audit for constructed histories, not a
-- runtime oracle. Operational execute/run never test hidden-world lawfulness.
instance lawfulDecidable (e : Event) (s : State) : Decidable (Lawful e s) := by
  cases e <;> unfold Lawful <;> infer_instance

def auditRun : List Event → State → Option State
  | [],s => some s
  | e::es,s => if Lawful e s then do let next ← execute e s; auditRun es next else none

theorem history_transitive {a b c : State} (first : History a b) (second : History b c) : History a c := by
  induction second with
  | nil => exact first
  | step earlier e lawful done ih => exact History.step ih e lawful done

theorem audit_produces_lawful_history (events : List Event) (start finish : State)
    (checked : auditRun events start = some finish) : History start finish := by
  induction events generalizing start with
  | nil =>
      simp [auditRun] at checked
      cases checked
      exact .nil _
  | cons e es ih =>
      by_cases lawful : Lawful e start
      · cases step : execute e start with
        | none => simp [auditRun,lawful,step] at checked
        | some next =>
          have tail : auditRun es next = some finish := by simpa [auditRun,lawful,step] using checked
          exact history_transitive (.step (.nil start) e lawful step) (ih next tail)
      · simp [auditRun,lawful] at checked

theorem audit_matches_operational_run (events : List Event) (start finish : State)
    (checked : auditRun events start = some finish) : run events start = some finish := by
  induction events generalizing start with
  | nil => exact checked
  | cons e es ih =>
      by_cases lawful : Lawful e start
      · cases step : execute e start with
        | none => simp [auditRun,lawful,step] at checked
        | some next =>
          have tail : auditRun es next = some finish := by simpa [auditRun,lawful,step] using checked
          simp [run,step,ih next tail]
      · simp [auditRun,lawful] at checked

def initial (w : World) (fuel deadline : Nat) (possible : List World := worlds) : State :=
  ⟨w,possible,(initialSituation w.model (commandRoots w) fuel deadline).installation,[],true,true⟩

def scan (reports : Reports) : List Event := (auditRoster true).map (fun d => .read d (reports d))
def mask (xs : List World) : Nat :=
  (hypotheses.zipIdx.filter (fun p => xs.any (fun w => w.model==p.1))).foldl (fun n p => n+2^p.2) 0

def scanResult (reports : Reports) : List World :=
  (auditRoster true).foldl (fun xs d => receive xs d (reports d)) worlds

theorem fixed_scan_retains_same_structural_alternatives :
    mask (scanResult splitReports) = 3 ∧
    mask (scanResult (fun _ => some false)) = 4 := by decide

def mobileLie : List Event := (auditRoster true).flatMap (fun d =>
  [.move .mobile ⟨.left,some (if d<2 then 0 else d)⟩,.read d (some false)])

theorem single_cause_at_each_read_can_forge_whole_transcript :
    (auditRoster true).all (fun d =>
      fits ⟨.left,some (if d<2 then 0 else d)⟩ d (some false)) = true ∧
    posterior true hypotheses (fun _ => some false) = [.right] := by decide

theorem temporal_observer_does_not_infer_false_right_sharing :
    let out := (run mobileLie (initial ⟨.left,some 0⟩ 30 30)).getD (initial ⟨.left,some 0⟩ 30 30)
    out.actual.model = .left ∧ mask out.possible = 7 ∧
    out.installation.state.spent = 5 ∧ out.records.length = 10 := by decide

def changedAndRechecked : List Event := scan splitReports ++
  [.move .reset ⟨.right,some 2⟩] ++ scan (fun d => some (d==2 || d==3)) ++ [.command]

theorem worked_histories_satisfy_their_transition_and_reporting_laws :
    auditRun mobileLie (initial ⟨.left,some 0⟩ 30 30) = run mobileLie (initial ⟨.left,some 0⟩ 30 30) ∧
    (auditRun mobileLie (initial ⟨.left,some 0⟩ 30 30)).isSome = true ∧
    auditRun changedAndRechecked (initial ⟨.left,some 0⟩ 23 23) =
      run changedAndRechecked (initial ⟨.left,some 0⟩ 23 23) ∧
    (auditRun changedAndRechecked (initial ⟨.left,some 0⟩ 23 23)).isSome = true := by decide

theorem actual_control_change_then_reinspection_completes :
    let start := initial ⟨.left,some 0⟩ 23 23
    let out := (run changedAndRechecked start).getD start
    out.actual.model = .right ∧ mask out.possible = 4 ∧
    out.installation.state.completed = true ∧ out.installation.state.running = false ∧
    out.installation.state.spent = 23 ∧ out.installation.state.reserve = 0 ∧
    out.installation.serial = 1 ∧ out.records.length = 12 := by decide

theorem reinspection_without_execution_capacity_does_not_complete :
    let start := initial ⟨.left,some 0⟩ 22 22
    let out := (run changedAndRechecked start).getD start
    mask out.possible = 4 ∧ out.installation.state.completed = false ∧
    out.installation.state.spent = 20 ∧ out.installation.state.reserve = 2 := by decide

theorem blocked_later_read_does_not_refund_earlier_inspection :
    let out := runUntilBlocked (scan splitReports) (initial ⟨.left,some 0⟩ 2 30)
    out.1 = false ∧ out.2.installation.state.spent = 2 ∧
    out.2.installation.state.reserve = 0 ∧ out.2.records.length = 2 := by decide

theorem denied_reorganization_retains_earlier_evidence_and_cost :
    let start := {initial ⟨.left,some 0⟩ 23 23 with changeAllowed := false}
    let out := runUntilBlocked changedAndRechecked start
    out.1 = false ∧ out.2.actual.model = .left ∧ mask out.2.possible = 3 ∧
    out.2.installation.state.spent = 5 ∧ out.2.records.length = 5 := by decide

theorem predicting_change_reopens_relevant_alternatives :
    mask (scanResult splitReports) = 3 ∧ mask (predict .reset (scanResult splitReports)) = 7 ∧
    certificate roster4 (pooled describe (models (scanResult splitReports))) (fun d => decide (2≤d)) = true ∧
    certificate roster4 (pooled describe (models (predict .reset (scanResult splitReports))))
      (fun d => decide (2≤d)) = false := by decide

theorem fault_movement_does_not_erase_structural_knowledge :
    mask (predict .mobile (scanResult splitReports)) = 3 := by decide

theorem new_change_after_last_report_reopens_coverage :
    mask (predict .control (scanResult splitReports)) = 7 := by decide

theorem understated_change_can_leave_false_confidence :
    let events := scan splitReports ++ [.move .steady ⟨.right,some 2⟩]
    let start := initial ⟨.left,some 0⟩ 30 30
    let out := (run events start).getD start
    out.actual ∉ out.possible ∧ mask out.possible = 3 ∧
    certificate roster4 (pooled describe (models out.possible)) (fun d => decide (2≤d)) = true ∧
    induced (describe out.actual.model) (roots out.actual) = [2,3] ∧
    auditRun events start = none := by decide

theorem denied_reads_collect_nothing (s : State) (d : Domain) (r : Option Bool)
    (denied : s.inspectionAllowed = false) : read d r s = none := by simp [read,denied]

end TemporalInspection
