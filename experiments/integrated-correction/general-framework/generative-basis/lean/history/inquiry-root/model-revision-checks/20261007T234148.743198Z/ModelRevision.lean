import SourceReliance

/-!
A complete finite revision cycle: locate disagreement, generate corrections from
the observed residual and an explicit grammar, retain history, select a separating
probe, acquire its result, and return to scoped use. The learner is not handed the
actual repair. Grammar, faithful measurement, stable law, available probes and
finite test support are disclosed premises. Domain-complete checking establishes
functional agreement on this finite interface, not unique physical causation,
validity in new settings, or universal epistemic/ethical sufficiency.
-/
namespace Generative.ModelRevision

abbrev Probe := SourceReliance.Probe
abbrev Reports := SourceReliance.Reports
abbrev Evidence := Probe × Reports
abbrev Law := Probe → Reports

inductive Feature where
  | target | localFault | commonFault
  deriving DecidableEq, Repr

def feature (f : Feature) (p : Probe) : Bool :=
  match f with
  | .target => p.target
  | .localFault => p.localFault
  | .commonFault => p.commonFault

def terms : List (List Feature) :=
  [[], [.target], [.localFault], [.commonFault],
   [.target, .localFault], [.target, .commonFault],
   [.localFault, .commonFault], [.target, .localFault, .commonFault]]

def base (p : Probe) : Reports := SourceReliance.emit ⟨false, false⟩ p

def difference (a b : Reports) : Reports := (Bool.xor a.1 b.1, Bool.xor a.2 b.2)

structure Repair where
  gate : List Feature
  residual : Reports
  deriving DecidableEq, Repr

def predict (r : Repair) (p : Probe) : Reports :=
  let enabled := r.gate.all (fun f => feature f p)
  let old := base p
  (Bool.xor old.1 (enabled && r.residual.1),
   Bool.xor old.2 (enabled && r.residual.2))

def acquire (actual : Law) (ps : List Probe) : List Evidence :=
  ps.map (fun p => (p, actual p))

def firstMismatch (records : List Evidence) : Option Evidence :=
  records.find? (fun e => base e.1 != e.2)

def proposals (failure : Evidence) : List Repair :=
  terms.map (fun gate => ⟨gate, difference (base failure.1) failure.2⟩)

def fits (r : Repair) (records : List Evidence) : Bool :=
  records.all (fun e => predict r e.1 == e.2)

def retain (candidates : List Repair) (records : List Evidence) : List Repair :=
  candidates.filter (fun r => fits r records)

def generate (records : List Evidence) : List Repair :=
  match firstMismatch records with
  | none => []
  | some failure => retain (proposals failure) records

def disagreement (candidates : List Repair) (p : Probe) : Bool :=
  candidates.any (fun a => candidates.any (fun b => predict a p != predict b p))

def selectProbe (candidates : List Repair) (available : List Probe) : Option Probe :=
  available.find? (disagreement candidates)

structure State where
  candidates : List Repair
  history : List Evidence
  deriving DecidableEq, Repr

def start (records : List Evidence) : State := ⟨generate records, records⟩

-- Candidate agreement is not an adequacy check. Even a lone proposal must face
-- unexamined cases in the declared audit domain before scoped closure.
def nextInquiry (s : State) (available : List Probe) : Option Probe :=
  if s.candidates.isEmpty then none
  else match selectProbe s.candidates available with
    | some p => some p
    | none => available.find? (fun p => !(s.history.any (fun e => e.1 == p)))

-- The law is the acquisition process called only after selection; selection has
-- access to candidate predictions and allowed probes, not to the forthcoming result.
def advance (actual : Law) (p : Probe) (s : State) : State :=
  let history := s.history ++ [(p, actual p)]
  ⟨retain s.candidates history, history⟩

def investigate (actual : Law) (available : List Probe) : Nat → State → State
  | 0, s => s
  | fuel + 1, s =>
      match nextInquiry s available with
      | none => s
      | some p => investigate actual available fuel (advance actual p s)

inductive Status where
  | inadequate | needsProbe | settledOnAvailable
  deriving DecidableEq, Repr

def status (s : State) (available : List Probe) : Status :=
  if s.candidates.isEmpty then .inadequate
  else if (nextInquiry s available).isSome then .needsProbe
  else .settledOnAvailable

def discovery : Probe := ⟨true, true, true⟩
def contrast : Probe := ⟨false, true, true⟩
def allProbes : List Probe := SourceReliance.protocol ++ [discovery, contrast]
def discoveryHistory : List Evidence :=
  acquire SourceReliance.jointFailure (SourceReliance.protocol ++ [discovery])
def interaction : Repair := ⟨[.localFault, .commonFault], (false, true)⟩
def exceptionPatch : Repair := ⟨[.target, .localFault, .commonFault], (false, true)⟩
def finished : State := investigate SourceReliance.jointFailure allProbes 1 (start discoveryHistory)

theorem decoded_measurement_preserves_record (reversed : Bool) (value : Reports) :
    SourceReliance.decode reversed
      (FormedGrounds.encode reversed value.1, FormedGrounds.encode reversed value.2) = some value := by
  simp only [SourceReliance.decode, FormedGrounds.training_forms_decoder]
  rfl

theorem accepted_repair_fits_history (r : Repair) (candidates : List Repair)
    (records : List Evidence) (accepted : r ∈ retain candidates records) :
    ∀ e ∈ records, predict r e.1 = e.2 := by
  have hf : fits r records = true := (List.mem_filter.mp accepted).2
  intro e he
  have := (List.all_eq_true.mp hf) e he
  simpa using this

theorem faithful_candidate_survives (r : Repair) (actual : Law) (ps : List Probe)
    (candidates : List Repair) (included : r ∈ candidates)
    (faithful : ∀ p, predict r p = actual p) :
    r ∈ retain candidates (acquire actual ps) := by
  simp [retain, fits, acquire, included, faithful]

theorem every_probe_is_in_domain (p : Probe) : p ∈ allProbes := by
  rcases p with ⟨t, f, c⟩
  cases t <;> cases f <;> cases c <;> decide

-- Actual law need not have a syntactic representative in the grammar. Acceptance
-- after exhaustive faithful measurement earns functional equality on this domain.
theorem exhaustive_acceptance_establishes_correspondence (actual : Law) (r : Repair)
    (candidates : List Repair)
    (accepted : r ∈ retain candidates (acquire actual allProbes)) :
    ∀ p, predict r p = actual p := by
  intro p
  apply accepted_repair_fits_history r candidates (acquire actual allProbes) accepted (p, actual p)
  exact List.mem_map.mpr ⟨p, every_probe_is_in_domain p, rfl⟩

theorem advance_preserves_old_history (actual : Law) (p : Probe) (s : State) :
    (advance actual p s).history.take s.history.length = s.history := by
  simp [advance]

theorem acquisition_locates_actual_discrepancy :
    firstMismatch discoveryHistory = some (discovery, (false, false)) := by decide

theorem generated_residual_targets_second_report :
    difference (base discovery) (SourceReliance.jointFailure discovery) = (false, true) := by decide

theorem failure_generates_competing_repairs :
    generate discoveryHistory = [interaction, exceptionPatch] := by decide

theorem both_repairs_fit_discovery :
    fits interaction discoveryHistory = true ∧ fits exceptionPatch discoveryHistory = true := by decide

theorem disagreement_selects_unseen_contrast :
    selectProbe (generate discoveryHistory) allProbes = some contrast ∧
    contrast ∉ discoveryHistory.map Prod.fst := by decide

theorem contrast_distinguishes_repairs :
    predict interaction contrast = (true, true) ∧
    predict exceptionPatch contrast = (true, false) := by decide

theorem repetition_cannot_choose_between_repairs (n : Nat) :
    retain [interaction, exceptionPatch]
      (List.replicate n (discovery, SourceReliance.jointFailure discovery)) =
      [interaction, exceptionPatch] := by
  simp [retain, fits, interaction, exceptionPatch, predict, base, discovery,
    SourceReliance.jointFailure, SourceReliance.emit, feature]

theorem complete_cycle_selects_interaction : finished.candidates = [interaction] := by decide

theorem complete_cycle_records_all_probes :
    finished.history = acquire SourceReliance.jointFailure allProbes := by decide

theorem corrected_law_matches_joint_failure (p : Probe) :
    predict interaction p = SourceReliance.jointFailure p := by
  rcases p with ⟨t, f, c⟩
  cases t <;> cases f <;> cases c <;> decide

theorem completed_cycle_has_earned_correspondence (r : Repair)
    (accepted : r ∈ finished.candidates) :
    ∀ p, predict r p = SourceReliance.jointFailure p := by
  rw [complete_cycle_selects_interaction] at accepted
  simp only [List.mem_singleton] at accepted
  subst r
  exact corrected_law_matches_joint_failure

theorem no_support_preserves_unfinished_status :
    status (investigate SourceReliance.jointFailure allProbes 0 (start discoveryHistory))
      allProbes = .needsProbe := by decide

theorem finished_status_is_scoped : status finished allProbes = .settledOnAvailable := by decide

theorem unavailable_probe_is_not_global_settlement :
    status (start discoveryHistory) [discovery] = .settledOnAvailable ∧
    status (start discoveryHistory) allProbes = .needsProbe := by decide

-- A grammar that omits the appropriate repair must retain its failure.
theorem agreement_alone_misses_a_bad_single_repair :
    selectProbe [exceptionPatch] allProbes = none ∧
    fits exceptionPatch (acquire SourceReliance.jointFailure allProbes) = false := by decide

theorem independent_audit_exposes_insufficient_grammar :
    status (investigate SourceReliance.jointFailure allProbes 1
      ⟨[exceptionPatch], discoveryHistory⟩) allProbes = .inadequate := by decide

abbrev LiveCase := Repair × Bool × SourceReliance.Faults

def liveCases (rs : List Repair) (faults : List SourceReliance.Faults) : List LiveCase :=
  rs.flatMap (fun r => faults.flatMap (fun f => [false, true].map (fun t => (r, t, f))))

def rely (rs : List Repair) (faults : List SourceReliance.Faults) (reports : Reports) : Option Bool :=
  let possible := (liveCases rs faults).filter
    (fun w => predict w.1 ⟨w.2.1, w.2.2.1, w.2.2.2⟩ == reports)
  SourceReliance.consensus (possible.map (fun w => w.2.1))

theorem corrected_use_retains_relevant_uncertainty :
    rely finished.candidates SourceReliance.allFaults (false, false) = none := by decide

theorem controlled_use_returns_correct_answer (target : Bool) :
    rely finished.candidates SourceReliance.clean
      (SourceReliance.jointFailure ⟨target, false, false⟩) = some target := by
  cases target <;> decide

-- Change of setting is a further production relation absent from the old domain.
def shifted (newSetting : Bool) (p : Probe) : Reports :=
  if newSetting then base p else SourceReliance.jointFailure p

theorem full_old_domain_does_not_establish_new_setting :
    (∀ p, shifted false p = predict interaction p) ∧
    shifted true contrast ≠ predict interaction contrast := by
  constructor
  · intro p
    exact (corrected_law_matches_joint_failure p).symm
  · decide

-- Downstream recording corruption can reproduce the observed joint mechanism.
-- Equality of recorded predictions does not identify the causal location.
def alteredRecording (p : Probe) : Reports :=
  let obtained := base p
  (obtained.1, Bool.xor obtained.2 (p.localFault && p.commonFault))

theorem recording_alternative_preserves_all_observations (p : Probe) :
    alteredRecording p = SourceReliance.jointFailure p := by
  rcases p with ⟨t, f, c⟩
  cases t <;> cases f <;> cases c <;> decide

theorem mechanism_location_requires_another_observation :
    base contrast ≠ SourceReliance.jointFailure contrast ∧
    alteredRecording contrast = SourceReliance.jointFailure contrast := by decide

end Generative.ModelRevision
