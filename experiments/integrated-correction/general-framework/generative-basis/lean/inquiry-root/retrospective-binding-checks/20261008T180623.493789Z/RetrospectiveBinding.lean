import SourceReliance
import AcquiredBinding

/-!
Composition, not a new generic updater: acquired production routes reinterpret
retained naming packets and supply candidate sets to AcquiredBinding. Packets
can precede calibration. Channel identity, the stable route family, paired
calibration targets/controls, fault envelope, grouping and atomic repertoire are
explicit premises. The learner functions receive no hidden target or actual route.
This is not an implementation identified by developmental data.
-/
namespace Generative.RetrospectiveBinding
open CompositionalAcquisition CompositionalFormation CompositionalTransmission
open AcquiredSegmentation AcquiredBinding

structure Packet where
  form : List Sound
  reports : SourceReliance.Reports
  deriving DecidableEq, Repr

structure Memory where
  base : Lexicon
  packets : List Packet
  calibration : List SourceReliance.Record
  deriving DecidableEq, Repr

def debit (s : Lexicon) : Lexicon :=
  {s with percept := {s.percept with machine := {s.percept.machine with
    support := s.percept.machine.support - 1, spent := s.percept.machine.spent + 1}}}

-- Arrival/observation costs one declared support unit. Computation and storage
-- maintenance have no separately derived costs; this is not a full energy model.
def receive (p : Packet) (s : Memory) : Memory :=
  if 1 ≤ s.base.percept.machine.support then
    {s with base := debit s.base, packets := s.packets ++ [p]}
  else s

def observe (r : SourceReliance.Record) (s : Memory) : Memory :=
  if 1 ≤ s.base.percept.machine.support then
    {s with base := debit s.base, calibration := s.calibration ++ [r]}
  else s

def calibrate (rs : List SourceReliance.Record) (s : Memory) : Memory :=
  rs.foldl (fun t r => observe r t) s

def routes (s : Memory) : List SourceReliance.Route :=
  SourceReliance.learn SourceReliance.repertoire s.calibration

def alternatives (rs : List SourceReliance.Route) (faults : List SourceReliance.Faults)
    (reports : SourceReliance.Reports) : List Expr :=
  (SourceReliance.compatible rs faults reports).map (fun w => .atom w.target)

-- Derived records are the current view of the unmodified packet history.
-- A changed view is not a claim that the original utterances changed.
def bindingView (s : Memory) (faults : List SourceReliance.Faults) : Lexicon :=
  {s.base with records := s.packets.map (fun p =>
    ⟨p.form, alternatives (routes s) faults p.reports, 0⟩), excluded := []}

theorem covered_packet_preserves_atomic_content (w : SourceReliance.World)
    (rs : List SourceReliance.Route) (faults : List SourceReliance.Faults)
    (routeIncluded : w.route ∈ rs) (faultIncluded : w.faults ∈ faults) :
    Expr.atom w.target ∈ alternatives rs faults (SourceReliance.view w) := by
  exact List.mem_map.mpr ⟨w,
    SourceReliance.actual_world_compatible w rs faults routeIncluded faultIncluded, rfl⟩

-- Realization is a hypothesis of the theorem, not an argument to bindingView.
-- It explicitly requires the same acquired route to cover the earlier packet.
theorem acquired_routes_supply_binding_coverage
    (s : Memory) (r : SourceReliance.Route) (reversed : Bool)
    (ps : List SourceReliance.Probe) (faults : List SourceReliance.Faults)
    (form : List Sound) (target : Bool) (answer : Expr)
    (calibration : s.calibration = SourceReliance.acquire r reversed ps)
    (available : Expr.atom target ∈ s.base.repertoire)
    (realized : ∀ p ∈ s.packets, p.form = form →
      ∃ f ∈ faults, p.reports = SourceReliance.emit r ⟨target,f.1,f.2⟩)
    (resolved : resolve (bindingView s faults) form = some answer) :
    answer = .atom target := by
  have rin : r ∈ SourceReliance.repertoire := by
    rcases r with ⟨a,b⟩
    cases a <;> cases b <;> decide
  have learned : r ∈ routes s := by
    rw [routes,calibration]
    exact SourceReliance.actual_route_retained r _ reversed ps rin
  apply unique_resolution_is_correct_under_coverage (bindingView s faults) form
    (.atom target) answer available _ resolved
  intro rec member _ matching
  change rec ∈ s.packets.map _ at member
  obtain ⟨p,hp,rfl⟩ := List.mem_map.mp member
  obtain ⟨f,hf,view⟩ := realized p hp matching
  change Expr.atom target ∈ alternatives (routes s) faults p.reports
  rw [view]
  exact covered_packet_preserves_atomic_content ⟨r,target,f⟩ _ _ learned hf

theorem later_observation_preserves_naming_packets (record : SourceReliance.Record) (s : Memory) :
    (observe record s).packets = s.packets := by
  unfold observe
  split <;> rfl

theorem observe_preserves_support_account (record : SourceReliance.Record) (s : Memory) :
    (observe record s).base.percept.machine.support + (observe record s).base.percept.machine.spent =
      s.base.percept.machine.support + s.base.percept.machine.spent := by
  unfold observe
  split
  · simp only [debit]; omega
  · rfl

theorem exhausted_memory_cannot_acquire_calibration (record : SourceReliance.Record) (s : Memory)
    (h : s.base.percept.machine.support = 0) : observe record s = s := by
  simp [observe,h]

def secureRoute : SourceReliance.Route := ⟨false,false⟩
def start (n : Nat) : Memory := ⟨emptyBinding n,[],[]⟩

-- Both reported pairs disagree. The later calibration reveals why the second
-- channel, not the first, tracks the target in this declared disturbance family.
def named (n : Nat) : Memory :=
  receive ⟨word true,(false,true)⟩
    (receive ⟨word false,(true,false)⟩ (start n))

def retrospective (n : Nat) : Memory :=
  calibrate (SourceReliance.acquire secureRoute false SourceReliance.protocol) (named n)

theorem prior_naming_alone_leaves_both_forms_unresolved (b : Bool) :
    resolve (bindingView (named 36) SourceReliance.allFaults) (word b) = none := by
  cases b <;> decide

theorem late_calibration_is_acquired_without_new_naming :
    (retrospective 36).packets = (named 36).packets ∧
    (retrospective 36).calibration = SourceReliance.acquire secureRoute false SourceReliance.protocol ∧
    routes (retrospective 36) = [secureRoute] := by decide

theorem late_calibration_changes_both_bindings (b : Bool) :
    resolve (bindingView (retrospective 36) SourceReliance.allFaults) (word b) = some (.atom b) := by
  cases b <;> decide

theorem retrospective_bindings_read_every_finite_sequence (ws : List Bool) :
    readForms (bindingView (retrospective 36) SourceReliance.allFaults) (ws.map word) =
      some (ws.map Expr.atom) := by
  induction ws with
  | nil => rfl
  | cons b bs ih =>
      simp only [List.map_cons,readForms,late_calibration_changes_both_bindings,ih]
      rfl

theorem retrospective_evidence_enters_compositional_use (ws : List Bool) :
    interpret (bindingView (retrospective 36) SourceReliance.allFaults) (encode ws) =
      assembleMessage (ws.map Expr.atom) := by
  have grouping : bond (bindingView (retrospective 36) SourceReliance.allFaults).percept.log = idealBond := by
    funext x y
    cases x <;> cases y <;> decide
  simp only [interpret,grouping,ideal_grouping_recovers_words,
    retrospective_bindings_read_every_finite_sequence]
  rfl

theorem acquired_reinterpretation_reaches_actual_response :
    (execute utterance (bindingView (retrospective 36) SourceReliance.allFaults)).map
      (fun result => (result.1,result.2.percept.machine.support,result.2.percept.machine.spent)) =
        some ([true,false,true],0,29) := by decide

theorem actual_history_preserves_prior_learning :
    (retrospective 36).base.percept.log = context.map some ∧
    (retrospective 36).base.percept.machine.samples = trialRecords usual ∧
    (retrospective 36).base.percept.machine.support = 4 ∧
    (retrospective 36).base.percept.machine.spent = 25 := by decide

theorem retained_interpretation_can_exceed_execution_support :
    interpret (bindingView (retrospective 35) SourceReliance.allFaults) utterance = some intended ∧
    execute utterance (bindingView (retrospective 35) SourceReliance.allFaults) = none := by decide

theorem calibration_without_retained_naming_cannot_bind :
    interpret (bindingView {retrospective 36 with packets := []} SourceReliance.allFaults) utterance = none := by decide

theorem partial_calibration_preserves_binding_uncertainty :
    let s := calibrate (SourceReliance.acquire secureRoute false
      [SourceReliance.baseline,SourceReliance.localProbe]) (named 36)
    interpret (bindingView s SourceReliance.allFaults) utterance = none := by decide

-- Raw report multiplicity is unchanged; changing their retained channel relation
-- changes the inferred binding once the production path has been learned.
theorem channel_identity_matters_to_later_binding :
    resolve (bindingView {retrospective 36 with
      packets := [⟨word false,(false,true)⟩,⟨word true,(true,false)⟩]}
      SourceReliance.allFaults) (word false) = some p1 := by decide

def jointFailureMemory : Memory :=
  calibrate (SourceReliance.jointRecords SourceReliance.protocol)
    (receive ⟨word true,SourceReliance.jointFailure ⟨true,true,true⟩⟩ (start 36))

theorem inherited_omitted_route_can_make_reinterpretation_wrong :
    resolve (bindingView jointFailureMemory SourceReliance.allFaults) (word true) = some p0 := by decide

def challenged : Memory :=
  calibrate (SourceReliance.jointRecords [⟨true,true,true⟩]) jointFailureMemory

theorem later_challenge_suspends_without_deleting_the_old_packet :
    challenged.packets = jointFailureMemory.packets ∧
    routes challenged = [] ∧
    resolve (bindingView challenged SourceReliance.allFaults) (word true) = none := by decide

end Generative.RetrospectiveBinding
