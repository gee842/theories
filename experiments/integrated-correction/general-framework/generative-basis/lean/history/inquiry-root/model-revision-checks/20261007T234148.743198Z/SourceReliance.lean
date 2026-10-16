import SelectiveRevision

/-!
Acquired production-path distinctions and conditional reliance. All reports,
calibration records and interventions arise through the same specified route law.
The learner receives records, not the actual route or the live target. The finite
route family, intervention fidelity and future fault envelope are local premises.
An explicit omitted joint failure defeats unwarranted extrapolation from this
family. No claim of general epistemic, semantic or ethical sufficiency is encoded.
-/
namespace Generative.SourceReliance

structure Route where
  copiesFirst : Bool
  sharesDisturbance : Bool
  deriving DecidableEq, Repr

structure Probe where
  target : Bool
  localFault : Bool
  commonFault : Bool
  deriving DecidableEq, Repr

abbrev Reports := Bool × Bool

def emit (r : Route) (p : Probe) : Reports :=
  let base := Bool.xor p.target (r.sharesDisturbance && p.commonFault)
  let first := Bool.xor base p.localFault
  (first, if r.copiesFirst then first else base)

def repertoire : List Route :=
  [⟨false, false⟩, ⟨false, true⟩, ⟨true, false⟩, ⟨true, true⟩]

def raw (reversed : Bool) (r : Route) (p : Probe) : Reports :=
  let result := emit r p
  (FormedGrounds.encode reversed result.1, FormedGrounds.encode reversed result.2)

def decode (reversed : Bool) (tokens : Reports) : Option Reports := do
  let evidence := FormedGrounds.observations (FormedGrounds.trained reversed)
  let a ← FormedGrounds.interpret evidence (some tokens.1)
  let b ← FormedGrounds.interpret evidence (some tokens.2)
  pure (a, b)

abbrev Record := Probe × Option Reports

def acquire (r : Route) (reversed : Bool) (probes : List Probe) : List Record :=
  probes.map (fun p => (p, decode reversed (raw reversed r p)))

def fits (r : Route) (records : List Record) : Bool :=
  records.all (fun record => record.2 == some (emit r record.1))

def learn (candidates : List Route) (records : List Record) : List Route :=
  candidates.filter (fun r => fits r records)

def baseline : Probe := ⟨false, false, false⟩
def localProbe : Probe := ⟨false, true, false⟩
def commonProbe : Probe := ⟨false, false, true⟩
-- Check both target values; the joint-failure witness cannot be dismissed as
-- failure merely to check the other target value during calibration.
def protocol : List Probe :=
  [baseline, localProbe, commonProbe,
   ⟨true, false, false⟩, ⟨true, true, false⟩, ⟨true, false, true⟩]

abbrev Faults := Bool × Bool

structure World where
  route : Route
  target : Bool
  faults : Faults
  deriving DecidableEq, Repr

def view (w : World) : Reports := emit w.route ⟨w.target, w.faults.1, w.faults.2⟩

def enumerate (routes : List Route) (faults : List Faults) : List World :=
  routes.flatMap (fun r => faults.flatMap (fun f => [false, true].map (fun t => ⟨r, t, f⟩)))

def compatible (routes : List Route) (faults : List Faults) (reports : Reports) : List World :=
  (enumerate routes faults).filter (fun w => view w == reports)

def consensus : List Bool → Option Bool
  | [] => none
  | b :: bs => if bs.all (fun a => a == b) then some b else none

-- No actual route, target or realized fault is an argument to this procedure.
def rely (routes : List Route) (faults : List Faults) (reports : Reports) : Option Bool :=
  consensus ((compatible routes faults reports).map World.target)

def clean : List Faults := [(false, false)]
def localUncertain : List Faults := [(false, false), (true, false)]
def allFaults : List Faults := [(false, false), (false, true), (true, false), (true, true)]

theorem acquired_decode (r : Route) (reversed : Bool) (p : Probe) :
    decode reversed (raw reversed r p) = some (emit r p) := by
  simp only [decode, raw, FormedGrounds.training_forms_decoder]
  rfl

theorem acquired_record_form (r : Route) (reversed : Bool) (ps : List Probe) :
    acquire r reversed ps = ps.map (fun p => (p, some (emit r p))) := by
  simp only [acquire, acquired_decode]

theorem actual_route_retained (r : Route) (candidates : List Route) (reversed : Bool)
    (ps : List Probe) (included : r ∈ candidates) :
    r ∈ learn candidates (acquire r reversed ps) := by
  simp [learn, fits, acquired_record_form, included]

theorem protocol_identifies_route (r : Route) (reversed : Bool) :
    learn repertoire (acquire r reversed protocol) = [r] := by
  rw [acquired_record_form]
  rcases r with ⟨c, s⟩
  cases c <;> cases s <;> decide

theorem baseline_does_not_identify (r : Route) (reversed : Bool) :
    learn repertoire (acquire r reversed [baseline]) = repertoire := by
  rw [acquired_record_form]
  rcases r with ⟨c, s⟩
  cases c <;> cases s <;> decide

theorem local_probe_leaves_common_vulnerability (r : Route) (reversed : Bool) :
    learn repertoire (acquire r reversed [baseline, localProbe]) =
      [⟨r.copiesFirst, false⟩, ⟨r.copiesFirst, true⟩] := by
  rw [acquired_record_form]
  rcases r with ⟨c, s⟩
  cases c <;> cases s <;> decide

theorem duplicated_records_add_no_constraint (rs : List Route) (records : List Record) :
    learn rs (records ++ records) = learn rs records := by
  simp [learn, fits, List.all_append]

theorem recoding_preserves_acquired_routes (r : Route) (ps : List Probe) :
    learn repertoire (acquire r false ps) = learn repertoire (acquire r true ps) := by
  rw [acquired_record_form, acquired_record_form]

theorem mem_enumerate (w : World) (routes : List Route) (faults : List Faults) :
    w ∈ enumerate routes faults ↔ w.route ∈ routes ∧ w.faults ∈ faults := by
  rcases w with ⟨r, t, f⟩
  cases t <;> simp [enumerate]

theorem actual_world_compatible (w : World) (routes : List Route) (faults : List Faults)
    (routeIncluded : w.route ∈ routes) (faultIncluded : w.faults ∈ faults) :
    w ∈ compatible routes faults (view w) := by
  simp [compatible, mem_enumerate, routeIncluded, faultIncluded]

theorem consensus_correct_for_member (values : List Bool) (actual b : Bool)
    (included : actual ∈ values) (asserts : consensus values = some b) : b = actual := by
  cases values with
  | nil => simp at included
  | cons a rest =>
    simp only [consensus] at asserts
    split at asserts
    · rename_i agree
      have equal : a = b := Option.some.inj asserts
      simp only [List.mem_cons] at included
      rcases included with same | member
      · exact equal.symm.trans same.symm
      · have h : actual = a := by
          have := (List.all_eq_true.mp agree) actual member
          simpa using this
        exact equal.symm.trans h.symm
    · contradiction

theorem reliance_correct_with_covered_world (w : World) (routes : List Route)
    (faults : List Faults) (b : Bool)
    (routeIncluded : w.route ∈ routes) (faultIncluded : w.faults ∈ faults)
    (asserts : rely routes faults (view w) = some b) : b = w.target := by
  apply consensus_correct_for_member _ w.target b _ asserts
  exact List.mem_map.mpr ⟨w, actual_world_compatible w routes faults routeIncluded faultIncluded, rfl⟩

theorem acquired_reliance_correct (r : Route) (reversed : Bool) (ps : List Probe)
    (faults : List Faults) (f : Faults) (target b : Bool) (covered : f ∈ faults)
    (asserts : rely (learn repertoire (acquire r reversed ps)) faults
      (emit r ⟨target, f.1, f.2⟩) = some b) : b = target := by
  have included : r ∈ repertoire := by
    rcases r with ⟨c, s⟩
    cases c <;> cases s <;> decide
  exact reliance_correct_with_covered_world ⟨r, target, f⟩ _ faults b
    (actual_route_retained r repertoire reversed ps included) covered asserts

theorem separate_second_survives_declared_faults (target f c : Bool) :
    rely [⟨false, false⟩] allFaults (emit ⟨false, false⟩ ⟨target, f, c⟩) = some target := by
  cases target <;> cases f <;> cases c <;> decide

theorem copy_can_be_reliable_when_route_is_clean (target : Bool) :
    rely [⟨true, false⟩] clean (emit ⟨true, false⟩ ⟨target, false, false⟩) = some target := by
  cases target <;> decide

theorem copied_agreement_under_local_uncertainty (report : Bool) :
    rely [⟨true, false⟩] localUncertain (report, report) = none := by
  cases report <;> decide

theorem uncopied_agreement_under_shared_uncertainty (report : Bool) :
    rely [⟨false, true⟩] allFaults (report, report) = none := by
  cases report <;> decide

theorem partial_acquisition_preserves_relevant_uncertainty (reversed report : Bool) :
    rely (learn repertoire (acquire ⟨false, false⟩ reversed [baseline, localProbe]))
      allFaults (report, report) = none := by
  rw [local_probe_leaves_common_vulnerability]
  cases report <;> decide

theorem common_probe_enables_scoped_reliance (reversed target f c : Bool) :
    rely (learn repertoire (acquire ⟨false, false⟩ reversed protocol)) allFaults
      (emit ⟨false, false⟩ ⟨target, f, c⟩) = some target := by
  rw [protocol_identifies_route]
  exact separate_second_survives_declared_faults target f c

theorem copied_pair_has_opposite_compatible_targets :
    view ⟨⟨true, false⟩, false, (false, false)⟩ =
      view ⟨⟨true, false⟩, true, (true, false)⟩ := by decide

theorem no_report_only_exact_answer_on_copied_pair (answer : Reports → Bool) :
    ¬ (answer (view ⟨⟨true, false⟩, false, (false, false)⟩) = false ∧
       answer (view ⟨⟨true, false⟩, true, (true, false)⟩) = true) := by
  change ¬ (answer (false, false) = false ∧ answer (false, false) = true)
  rintro ⟨h, k⟩
  rw [h] at k
  contradiction

-- A concrete production law outside the four-route family. Its extra path is
-- activated only by the conjunction of the two disturbances, absent in training.
def jointFailure (p : Probe) : Reports :=
  if p.localFault && p.commonFault then (!p.target, !p.target)
  else emit ⟨false, false⟩ p

def jointRecords (ps : List Probe) : List Record :=
  ps.map (fun p => (p, some (jointFailure p)))

theorem omitted_joint_failure_matches_training :
    jointRecords protocol = acquire ⟨false, false⟩ false protocol := by decide

theorem omitted_joint_failure_defeats_inference :
    rely (learn repertoire (jointRecords protocol)) allFaults
      (jointFailure ⟨true, true, true⟩) = some false := by decide

theorem joint_challenge_reopens_model_family :
    learn repertoire (jointRecords (protocol ++ [⟨true, true, true⟩])) = [] := by decide

theorem empty_family_does_not_certify (faults : List Faults) (reports : Reports) :
    rely [] faults reports = none := by rfl

theorem joint_challenge_leaves_observed_history_unchanged :
    (jointRecords (protocol ++ [⟨true, true, true⟩])).take protocol.length =
      jointRecords protocol := by decide

end Generative.SourceReliance
