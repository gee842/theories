import TemporalInspection

/-! A bounded instruction interpreter derives change coverage from executed
writes, updates retained possibilities by that same transformer, and commits
its record with the mutation. Current rights and runtime isolation remain
premises. This is not verified hardware, compiler output, or a recovery system. -/
namespace MediatedControl
open TemporalInspection EvidenceQualifiedCorrection FaultTolerantCorrection CorrectionReconfiguration FallibleInspection

inductive FaultCode where
  | clear | r0 | r1 | r2 | r3 | r4
  deriving DecidableEq, Repr

def decodeFault : FaultCode → Option Nat
  | .clear => none | .r0 => some 0 | .r1 => some 1 | .r2 => some 2 | .r3 => some 3 | .r4 => some 4

inductive Write where
  | model : Model → Write
  | fault : FaultCode → Write
  | eraseRecords : Write
  | forgePossible : List World → Write
  | replaceInstallation : Installation → Write
  | grantBoth : Write
  deriving DecidableEq, Repr

structure Rights where
  model : Bool
  fault : Bool
  deriving DecidableEq, Repr

def permitted (r : Rights) : Write → Bool
  | .model _ => r.model | .fault _ => r.fault | _ => false

def authorized (r : Rights) (program : List Write) : Bool := program.all (permitted r)

def oneWrite (op : Write) (w : World) : World := match op with
  | .model h => {w with model := h}
  | .fault f => {w with fault := decodeFault f}
  | _ => w

-- Protected-field requests are rejected before this evaluator is called.
def writes : List Write → World → World
  | [],w => w
  | op::rest,w => writes rest (oneWrite op w)

def modelTouched : List Write → Bool
  | [] => false
  | .model _ :: _ => true
  | _ :: rest => modelTouched rest

def faultTouched : List Write → Bool
  | [] => false
  | .fault _ :: _ => true
  | _ :: rest => faultTouched rest

def effect (program : List Write) : Change := match modelTouched program, faultTouched program with
  | false,false => .steady | false,true => .mobile | true,false => .control | true,true => .reset

def image (program : List Write) (possible : List World) : List World := possible.map (writes program)

theorem model_field_preserved (program : List Write) (w : World) (untouched : modelTouched program = false) :
    (writes program w).model = w.model := by
  induction program generalizing w with
  | nil => rfl
  | cons op rest ih =>
      cases op <;> simp only [modelTouched] at untouched
      all_goals simp only [writes,oneWrite]
      all_goals first | contradiction | exact ih _ untouched

theorem fault_field_preserved (program : List Write) (w : World) (untouched : faultTouched program = false) :
    (writes program w).fault = w.fault := by
  induction program generalizing w with
  | nil => rfl
  | cons op rest ih =>
      cases op <;> simp only [faultTouched] at untouched
      all_goals simp only [writes,oneWrite]
      all_goals first | contradiction | exact ih _ untouched

theorem world_fields_determine_state {a b : World} (hm : a.model=b.model) (hf : a.fault=b.fault) : a=b := by
  cases a
  cases b
  simp_all

theorem model_write_stays_represented (w : World) (known : w ∈ worlds) (h : Model) :
    {w with model := h} ∈ worlds := by
  obtain ⟨old,ho,entry⟩ := List.mem_flatMap.mp known
  obtain ⟨f,hf,equal⟩ := List.mem_map.mp entry
  cases equal
  apply List.mem_flatMap.mpr
  exact ⟨h,by cases h <;> decide,List.mem_map.mpr ⟨f,hf,rfl⟩⟩

theorem fault_write_stays_represented (w : World) (f : FaultCode) :
    {w with fault := decodeFault f} ∈ worlds := by
  cases w with
  | mk h old =>
      change (⟨h,decodeFault f⟩ : World) ∈ worlds
      cases h <;> cases f <;> decide

theorem writes_stay_represented (program : List Write) (w : World) (known : w ∈ worlds) :
    writes program w ∈ worlds := by
  induction program generalizing w with
  | nil => exact known
  | cons op rest ih =>
      apply ih
      cases op with
      | model h => exact model_write_stays_represented w known h
      | fault f => exact fault_write_stays_represented w f
      | eraseRecords | forgePossible _ | replaceInstallation _ | grantBoth => exact known

theorem executed_writes_fit_derived_effect (program : List Write) (w : World) (known : w ∈ worlds) :
    writes program w ∈ successors (effect program) w := by
  apply List.mem_filter.mpr
  refine ⟨writes_stay_represented program w known,?_⟩
  cases hm : modelTouched program <;> cases hf : faultTouched program
  · have eq := world_fields_determine_state (model_field_preserved program w hm) (fault_field_preserved program w hf)
    simp [effect,hm,hf,eq]
  · simp [effect,hm,hf,model_field_preserved program w hm]
  · simp [effect,hm,hf,fault_field_preserved program w hf]
  · simp [effect,hm,hf]

theorem exact_image_retains_executed_actual (program : List Write) (possible : List World) (w : World)
    (known : w ∈ possible) : writes program w ∈ image program possible :=
  List.mem_map.mpr ⟨w,known,rfl⟩

theorem exact_image_is_within_coarse_prediction (program : List Write) (possible : List World)
    (represented : ∀ w ∈ possible, w ∈ worlds) :
    ∀ w ∈ image program possible, w ∈ predict (effect program) possible := by
  intro w hw
  obtain ⟨old,member,rfl⟩ := List.mem_map.mp hw
  exact prediction_contains_successor _ _ _ _ member (executed_writes_fit_derived_effect program old (represented old member))

structure Packet where
  expectedGeneration : Nat
  claimedEffect : Change
  program : List Write
  deriving DecidableEq, Repr

structure Entry where
  generation : Nat
  actualEffect : Change
  program : List Write
  deriving DecidableEq, Repr

structure Machine where
  tracked : TemporalInspection.State
  rights : Rights
  generation : Nat := 0
  journal : List Entry := []
  deriving DecidableEq, Repr

def writeCost (program : List Write) : Nat := program.length+1

def installed (m : Machine) (p : Packet) (paid : EffectiveCommand.State) : Machine :=
  {m with
    tracked := {m.tracked with
      actual := writes p.program m.tracked.actual
      possible := image p.program m.tracked.possible
      installation := {m.tracked.installation with
        serial := m.tracked.installation.serial+1
        state := {paid with
          authority := paid.authority+1
          signed := false
          issued := false
          delivered := false
          completed := false}}
      records := m.tracked.records ++ [.change (effect p.program)]}
    generation := m.generation+1
    journal := m.journal ++ [⟨m.generation,effect p.program,p.program⟩]}

def commit (p : Packet) (m : Machine) : Option Machine := do
  if p.expectedGeneration != m.generation || !authorized m.rights p.program || !m.tracked.changeAllowed then none else do
    let paid ← EffectiveCommand.spend (writeCost p.program) (writeCost p.program) m.tracked.installation.state
    return installed m p paid

theorem committed_shape (p : Packet) (m out : Machine) (done : commit p m = some out) :
    p.expectedGeneration = m.generation ∧ authorized m.rights p.program = true ∧
    ∃ paid, EffectiveCommand.spend (writeCost p.program) (writeCost p.program) m.tracked.installation.state = some paid ∧
      out = installed m p paid := by
  unfold commit at done
  split at done
  · simp at done
  · rename_i admitted
    have allowed : p.expectedGeneration = m.generation ∧ authorized m.rights p.program = true := by
      exact (show (p.expectedGeneration = m.generation ∧ authorized m.rights p.program = true) ∧
        m.tracked.changeAllowed = true from by simpa using admitted).1
    refine ⟨allowed.1,allowed.2,?_⟩
    cases paid : EffectiveCommand.spend (writeCost p.program) (writeCost p.program) m.tracked.installation.state with
    | none => simp [paid] at done
    | some state =>
      simp [paid] at done
      exact ⟨state,rfl,done.symm⟩

theorem commit_preserves_actual_coverage (p : Packet) (m out : Machine) (known : Known m.tracked)
    (done : commit p m = some out) : Known out.tracked := by
  obtain ⟨_,_,paid,_,rfl⟩ := committed_shape p m out done
  constructor
  · exact exact_image_retains_executed_actual _ _ _ known.1
  · intro w hw
    obtain ⟨old,member,rfl⟩ := List.mem_map.mp hw
    exact writes_stay_represented _ _ (known.2 old member)

theorem commit_records_the_executed_effect (p : Packet) (m out : Machine) (done : commit p m = some out) :
    out.tracked.actual = writes p.program m.tracked.actual ∧
    out.tracked.possible = image p.program m.tracked.possible ∧
    out.tracked.records = m.tracked.records ++ [.change (effect p.program)] ∧
    out.journal = m.journal ++ [⟨m.generation,effect p.program,p.program⟩] ∧
    out.generation = m.generation+1 ∧ out.rights = m.rights ∧
    out.tracked.installation.root = m.tracked.installation.root ∧
    out.tracked.installation.mandate = m.tracked.installation.mandate := by
  obtain ⟨_,_,paid,_,rfl⟩ := committed_shape p m out done
  exact ⟨rfl,rfl,rfl,rfl,rfl,rfl,rfl,rfl⟩

theorem caller_effect_claim_is_not_used (m : Machine) (p : Packet) (claim : Change) :
    commit {p with claimedEffect := claim} m = commit p m := rfl

theorem replayed_packet_rejected (p : Packet) (m out : Machine) (done : commit p m = some out) :
    commit p out = none := by
  have shape := committed_shape p m out done
  have next := (commit_records_the_executed_effect p m out done).2.2.2.2.1
  have different : p.expectedGeneration ≠ out.generation := by omega
  simp [commit,different]

theorem denied_write_prevents_commit (p : Packet) (m : Machine) (op : Write)
    (included : op ∈ p.program) (denied : permitted m.rights op = false) : commit p m = none := by
  have deniedAll : authorized m.rights p.program = false := by
    cases h : authorized m.rights p.program
    · rfl
    · have one := List.all_eq_true.mp h op included
      simp [denied] at one
  simp [commit,deniedAll]

theorem old_command_request_is_revoked (p : Packet) (m out : Machine) (req : Request)
    (current : fresh m.tracked.installation req = true) (done : commit p m = some out) :
    fresh out.tracked.installation req = false := by
  obtain ⟨_,_,paid,hpaid,rfl⟩ := committed_shape p m out done
  have serial : req.serial = m.tracked.installation.serial := by
    simpa using (Bool.and_eq_true_iff.mp current).2
  simp [fresh,installed,serial]

theorem commit_keeps_consumption (p : Packet) (m out : Machine) (done : commit p m = some out) :
    out.tracked.installation.state.reserve + out.tracked.installation.state.spent =
      m.tracked.installation.state.reserve + m.tracked.installation.state.spent ∧
    out.tracked.installation.state.spent = m.tracked.installation.state.spent+writeCost p.program ∧
    out.tracked.installation.state.time ≤ out.tracked.installation.state.deadline := by
  obtain ⟨_,_,paid,hpaid,rfl⟩ := committed_shape p m out done
  have account := EffectiveCommand.spend_conserves hpaid
  have spent : paid.spent = m.tracked.installation.state.spent+writeCost p.program := by
    unfold EffectiveCommand.spend at hpaid
    split at hpaid
    · cases hpaid; rfl
    · cases hpaid
  exact ⟨account.1,spent,account.2⟩

inductive Event where
  | patch : Packet → Event
  | read : Domain → Option Bool → Event
  | command : Event
  deriving DecidableEq, Repr

def step (e : Event) (m : Machine) : Option Machine := match e with
  | .patch p => commit p m
  | .read d r => (TemporalInspection.read d r m.tracked).map (fun s => {m with tracked := s})
  | .command => some {m with tracked := TemporalInspection.respond m.tracked}

def SourceLaw (e : Event) (m : Machine) : Prop := match e with
  | .read d r => fits m.tracked.actual d r = true
  | _ => True

theorem mediated_step_preserves_coverage (e : Event) (m out : Machine) (known : Known m.tracked)
    (source : SourceLaw e m) (done : step e m = some out) : Known out.tracked := by
  cases e with
  | patch p => exact commit_preserves_actual_coverage p m out known done
  | read d r =>
      cases readResult : TemporalInspection.read d r m.tracked with
      | none => simp [step,readResult] at done
      | some s =>
          simp [step,readResult] at done
          cases done
          exact reading_preserves_known _ _ d r known source readResult
  | command =>
      simp [step] at done
      cases done
      exact responding_preserves_known _ known

inductive History : Machine → Machine → Prop where
  | nil (m : Machine) : History m m
  | step {start before after : Machine} (earlier : History start before) (e : Event)
      (source : SourceLaw e before) (done : step e before = some after) : History start after

theorem mediated_history_preserves_coverage {start finish : Machine} (history : History start finish)
    (known : Known start.tracked) : Known finish.tracked := by
  induction history with
  | nil => exact known
  | step prior e source done ih => exact mediated_step_preserves_coverage e _ _ ih source done

theorem mediated_history_to_current_certificate {start finish : Machine} (history : History start finish)
    (known : Known start.tracked) (supports : Domain → Bool) (P : Prop)
    (faithful : ∀ d ∈ (describe finish.tracked.actual.model).roster,
      fails ((describe finish.tracked.actual.model).vulnerability d) (commandRoots finish.tracked.actual) = false → supports d = true → P)
    (accepted : certificate (describe finish.tracked.actual.model).roster
      (pooled describe (models finish.tracked.possible)) supports = true) : P := by
  have kept := mediated_history_preserves_coverage history known
  exact current_pool_sound _ _ kept.1 (kept.2 _ kept.1) supports P faithful accepted

def run : List Event → Machine → Bool × Machine
  | [],m => (true,m)
  | e::es,m => match step e m with | none => (false,m) | some next => run es next

def start (w : World) (fuel deadline : Nat) (rights : Rights := ⟨true,true⟩) : Machine :=
  ⟨TemporalInspection.initial w fuel deadline,rights,0,[]⟩

def inspectEvents (reports : Reports) : List Event := (auditRoster true).map (fun d => .read d (reports d))
def repair : Packet := ⟨0,.steady,[.model .right,.fault .r2]⟩
def worked : List Event := inspectEvents splitReports ++ [.patch repair,.command]

theorem executed_patch_can_replace_a_fresh_structural_survey :
    let out := (run worked (start ⟨.left,some 0⟩ 19 19)).2
    out.tracked.actual = ⟨.right,some 2⟩ ∧ TemporalInspection.mask out.tracked.possible = 4 ∧
    out.tracked.installation.state.completed = true ∧ out.tracked.installation.state.running = false ∧
    out.tracked.installation.state.spent = 19 ∧ out.tracked.installation.state.reserve = 0 ∧
    out.tracked.installation.serial = 2 ∧ out.generation = 1 ∧
    out.journal = [⟨0,.reset,repair.program⟩] := by decide

theorem exact_transform_is_stronger_than_footprint_alone :
    TemporalInspection.mask (image repair.program (scanResult splitReports)) = 4 ∧
    TemporalInspection.mask (predict (effect repair.program) (scanResult splitReports)) = 7 := by decide

theorem execution_still_needs_remaining_capacity :
    let out := (run worked (start ⟨.left,some 0⟩ 18 18)).2
    out.tracked.installation.state.completed = false ∧ out.tracked.installation.state.spent = 16 ∧
    out.tracked.installation.state.reserve = 2 := by decide

theorem read_only_requester_cannot_reorganize :
    let result := run worked (start ⟨.left,some 0⟩ 19 19 ⟨false,false⟩)
    result.1 = false ∧ result.2.tracked.actual = ⟨.left,some 0⟩ ∧
    result.2.tracked.installation.state.spent = 5 ∧ result.2.journal = [] := by decide

theorem protected_field_attempts_reject_even_with_both_write_rights :
    let m := start ⟨.left,some 0⟩ 30 30
    [.eraseRecords,.forgePossible [⟨.right,some 2⟩],.replaceInstallation m.tracked.installation,.grantBoth].all
      (fun op => (commit ⟨0,.steady,[.model .right,op]⟩ m).isNone) = true := by decide

-- This alternate machine admits an additional writer outside the interface.
-- Its failure is outside the closed interpreter's mediation guarantee.
def bypass (target : World) (m : Machine) : Machine :=
  {m with tracked := {m.tracked with actual := target}}

def publicView (m : Machine) := (m.tracked.possible,m.tracked.records,m.tracked.installation,m.rights,m.generation,m.journal)

def previouslyInspected : Machine := (run (inspectEvents splitReports) (start ⟨.left,some 0⟩ 30 30)).2

theorem bypass_preserves_records_but_breaks_coverage :
    let changed := bypass ⟨.right,some 2⟩ previouslyInspected
    publicView changed = publicView previouslyInspected ∧
    changed.tracked.actual ∉ changed.tracked.possible ∧
    induced (describe changed.tracked.actual.model) (roots changed.tracked.actual) = [2,3] ∧
    certificate roster4 (pooled describe (models changed.tracked.possible)) (fun d => decide (2≤d)) = true := by decide

theorem record_only_acceptance_cannot_exclude_the_extra_writer
    (accept : (List World × List TemporalInspection.Record × Installation × Rights × Nat × List Entry) → Bool)
    (original : accept (publicView previouslyInspected) = true) :
    accept (publicView (bypass ⟨.right,some 2⟩ previouslyInspected)) = true := original

end MediatedControl
