import RetrospectiveBinding

/-!
Historical applicability, not a new general learning algorithm. Possible route
histories are constrained by dated acquired controls; their projections at the
packet's date supply RetrospectiveBinding.alternatives. The learner is not given
the actual route or change time. Chronology, source identity, control fidelity,
route repertoire, change envelope and packet disturbance envelope are supplied.
The four-slot witnesses use single controls, not externally marked stable epochs.
This adapter does not newly account for acquisition/storage/computation costs.
-/
namespace Generative.HistoricalBinding
open CompositionalAcquisition CompositionalTransmission AcquiredSegmentation AcquiredBinding

inductive Moment where
  | prior | naming | following | latest
  deriving DecidableEq, Repr

structure History where
  prior : SourceReliance.Route
  naming : SourceReliance.Route
  following : SourceReliance.Route
  latest : SourceReliance.Route
  deriving DecidableEq, Repr

def at (h : History) : Moment → SourceReliance.Route
  | .prior => h.prior
  | .naming => h.naming
  | .following => h.following
  | .latest => h.latest

abbrev Observation := Moment × SourceReliance.Record
abbrev Instruction := Moment × SourceReliance.Probe

def acquire (h : History) (reversed : Bool) (ps : List Instruction) : List Observation :=
  ps.map fun p => (p.1, p.2, SourceReliance.decode reversed
    (SourceReliance.raw reversed (at h p.1) p.2))

def fits (h : History) (observations : List Observation) : Bool :=
  observations.all fun o => o.2.2 == some (SourceReliance.emit (at h o.1) o.2.1)

def learn (family : List History) (observations : List Observation) : List History :=
  family.filter fun h => fits h observations

def routesAt (family : List History) (observations : List Observation)
    (date : Moment) : List SourceReliance.Route :=
  (learn family observations).map fun h => at h date

structure TimedPacket where
  date : Moment
  packet : RetrospectiveBinding.Packet
  deriving DecidableEq, Repr

-- A derived binding view. Its arguments retain both packet and observation dates;
-- no actual History or novel target is an operational input.
def bindingView (base : Lexicon) (packets : List TimedPacket)
    (family : List History) (observations : List Observation)
    (faults : List SourceReliance.Faults) : Lexicon :=
  {base with records := packets.map (fun p => ⟨p.packet.form,
    RetrospectiveBinding.alternatives (routesAt family observations p.date)
      faults p.packet.reports, 0⟩), excluded := []}

theorem actual_history_retained (h : History) (family : List History)
    (reversed : Bool) (ps : List Instruction) (included : h ∈ family) :
    h ∈ learn family (acquire h reversed ps) := by
  simp [learn, fits, acquire, SourceReliance.acquired_decode, included]

theorem acquired_history_supplies_past_route (h : History) (family : List History)
    (reversed : Bool) (ps : List Instruction) (date : Moment) (included : h ∈ family) :
    at h date ∈ routesAt family (acquire h reversed ps) date := by
  exact List.mem_map.mpr ⟨h, actual_history_retained h family reversed ps included, rfl⟩

-- No global route stability is required. Coverage is now of the actual history
-- within the admitted family, plus each packet's disturbance at its own date.
theorem acquired_history_supplies_binding_coverage
    (base : Lexicon) (packets : List TimedPacket) (h : History) (family : List History)
    (reversed : Bool) (ps : List Instruction) (faults : List SourceReliance.Faults)
    (form : List Sound) (target : Bool) (answer : Expr)
    (included : h ∈ family) (available : Expr.atom target ∈ base.repertoire)
    (realized : ∀ p ∈ packets, p.packet.form = form → ∃ f ∈ faults,
      p.packet.reports = SourceReliance.emit (at h p.date) ⟨target,f.1,f.2⟩)
    (resolved : resolve (bindingView base packets family (acquire h reversed ps) faults)
      form = some answer) : answer = .atom target := by
  apply unique_resolution_is_correct_under_coverage _ form (.atom target) answer available _ resolved
  intro rec member _ matching
  change rec ∈ packets.map _ at member
  obtain ⟨p,hp,rfl⟩ := List.mem_map.mp member
  obtain ⟨f,hf,report⟩ := realized p hp matching
  change Expr.atom target ∈ RetrospectiveBinding.alternatives _ faults p.packet.reports
  rw [report]
  exact RetrospectiveBinding.covered_packet_preserves_atomic_content
    ⟨at h p.date,target,f⟩ _ _
    (acquired_history_supplies_past_route h family reversed ps p.date included) hf

def allHistories : List History :=
  SourceReliance.repertoire.flatMap fun a => SourceReliance.repertoire.flatMap fun b =>
    SourceReliance.repertoire.flatMap fun c => SourceReliance.repertoire.map fun d => ⟨a,b,c,d⟩

def changes (h : History) : Nat :=
  (if h.prior = h.naming then 0 else 1) +
  (if h.naming = h.following then 0 else 1) +
  (if h.following = h.latest then 0 else 1)

def envelope (n : Nat) : List History := allHistories.filter fun h => decide (changes h ≤ n)

def secure : SourceReliance.Route := ⟨false,false⟩
def vulnerable : SourceReliance.Route := ⟨false,true⟩
def deterioration : History := ⟨secure,secure,secure,vulnerable⟩
def improvement : History := ⟨vulnerable,vulnerable,vulnerable,secure⟩
def concealedExcursion : History := ⟨secure,vulnerable,secure,secure⟩
def constantSecure : History := ⟨secure,secure,secure,secure⟩

def controls : List Instruction :=
  [(.prior,SourceReliance.commonProbe),(.following,SourceReliance.commonProbe),
   (.latest,SourceReliance.commonProbe)]

def lateControl : List Instruction := [(.latest,SourceReliance.commonProbe)]
def splitControls : List Instruction :=
  [(.prior,SourceReliance.commonProbe),(.latest,SourceReliance.commonProbe)]

-- The packet disturbance is known to be common in these examples. This stronger
-- envelope allows recovery from a vulnerable route; it is not inferred from data.
def packetFaults : List SourceReliance.Faults := [(false,true)]
def packet (report : Bool) : List TimedPacket :=
  [⟨.naming,⟨word true,(report,report)⟩⟩]

def answer (family : List History) (observations : List Observation)
    (report : Bool) : Option Expr :=
  resolve (bindingView (emptyBinding 32) (packet report) family observations packetFaults) (word true)

theorem later_deterioration_does_not_invalidate_earlier_content :
    deterioration ∈ envelope 1 ∧
    SourceReliance.emit deterioration.naming ⟨true,false,true⟩ = (true,true) ∧
    answer (envelope 1) (acquire deterioration false controls) true = some p1 := by decide

theorem later_improvement_does_not_rehabilitate_earlier_false_reports :
    improvement ∈ envelope 1 ∧
    SourceReliance.emit improvement.naming ⟨true,false,true⟩ = (false,false) ∧
    answer (envelope 1) (acquire improvement false controls) false = some p1 := by decide

theorem late_assessment_alone_leaves_the_old_binding_open :
    answer (envelope 1) (acquire improvement false lateControl) false = none ∧
    answer (envelope 1) (acquire deterioration false lateControl) true = none := by decide

-- Knowing a change occurred is insufficient if both possible locations straddle
-- naming. There is no supplied change-point label resolving this comparison.
theorem known_change_without_location_does_not_settle_the_old_binding :
    answer (envelope 1) (acquire improvement false splitControls) false = none ∧
    answer (envelope 1) (acquire deterioration false splitControls) true = none := by decide

theorem unknown_packet_disturbance_preserves_uncertainty :
    resolve (bindingView (emptyBinding 32) (packet false) (envelope 1)
      (acquire improvement false controls) SourceReliance.allFaults) (word true) = none := by decide

-- A genuinely different propagation history, not a freely toggled truth label.
-- Same calibration records and report, but opposite earlier targets can produce it.
theorem omitted_temporary_change_defeats_backward_confidence :
    concealedExcursion ∉ envelope 1 ∧ concealedExcursion ∈ envelope 2 ∧
    acquire concealedExcursion false controls = acquire constantSecure false controls ∧
    SourceReliance.emit concealedExcursion.naming ⟨true,false,true⟩ =
      SourceReliance.emit constantSecure.naming ⟨false,false,true⟩ ∧
    answer (envelope 1) (acquire concealedExcursion false controls) false = some p0 ∧
    answer (envelope 2) (acquire concealedExcursion false controls) false = none := by decide

-- Dated observations matter even when the unordered accuracy counts agree.
def lateImprovement : History := ⟨vulnerable,vulnerable,vulnerable,secure⟩
def earlyImprovement : History := ⟨vulnerable,secure,secure,secure⟩

theorem chronological_scope_changes_the_answer :
    answer (envelope 1) (acquire lateImprovement false controls) false = some p1 ∧
    answer (envelope 1) (acquire earlyImprovement false controls) false = none := by decide

end Generative.HistoricalBinding
