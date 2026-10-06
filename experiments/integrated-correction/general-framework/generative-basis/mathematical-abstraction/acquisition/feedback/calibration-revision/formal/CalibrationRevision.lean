import RemainingDependency

/-!
A prospective additive continuation of the actual retained relay/load history.
The old weak report is historical evidence, not a premise asserting native W.
The finite hypothesis family independently represents W0,W1,F0,F1. Distinct
full-load stock, acquired consequence, revised application and a further weak
challenge are kept separate. Native operations follow the frozen CALIBRATION-REVISION-PROTOCOL;
source-bound fixtures separately check the actually executed words.
-/
namespace CalibrationRevision
open RemainingDependency
set_option maxRecDepth 32768
set_option maxHeartbeats 4000000

structure Model where
  weak : Pair Bool
  full : Pair Bool
  deriving DecidableEq, Repr

/-- Keep the entire weak table and the tested full response fixed, while
varying only the other full coordinate. This is within the declared family. -/
def sameObserved (weak : Pair Bool) (tested observed other : Bool) : Model :=
  {weak := weak, full := if tested then ⟨other,observed⟩ else ⟨observed,other⟩}

theorem untested_full_coordinate_is_underdetermined (weak : Pair Bool)
    (tested observed : Bool) :
    let a := sameObserved weak tested observed false
    let b := sameObserved weak tested observed true
    a.weak = b.weak ∧ a.full.get tested = observed ∧ b.full.get tested = observed ∧
    a.full.get (!tested) = false ∧ b.full.get (!tested) = true := by
  cases tested <;> simp [sameObserved, Pair.get]

/-- Repeating any list of weak queries cannot distinguish this pair, even if
both settings are queried. This does not posit unlimited funding to do so. -/
theorem every_weak_query_word_preserves_the_ambiguity (weak : Pair Bool)
    (tested observed : Bool) (queries : List Bool) :
    queries.map (sameObserved weak tested observed false).weak.get =
    queries.map (sameObserved weak tested observed true).weak.get := rfl

theorem same_observed_pair_has_distinct_full_laws (weak : Pair Bool)
    (tested observed : Bool) :
    (sameObserved weak tested observed false).full ≠
    (sameObserved weak tested observed true).full := by
  cases tested <;> simp [sameObserved, Pair.mk.injEq]

/-- A static common-context relation, not an acquired truth flag. The native
interpretation must justify using historical full and current weak data here. -/
def GloballyCalibrated (m : Model) : Prop := ∀ r, m.weak.get r = m.full.get r

theorem local_mismatch_refutes_global_calibration (m : Model) (r : Bool)
    (h : m.weak.get r ≠ m.full.get r) : ¬ GloballyCalibrated m := by
  intro hc
  exact h (hc r)

theorem local_agreement_does_not_establish_global_calibration (weak : Pair Bool)
    (r : Bool) :
    let m : Model := {weak := weak, full := weak.set (!r) (!(weak.get (!r)))}
    m.weak.get r = m.full.get r ∧ ¬ GloballyCalibrated m := by
  rcases weak with ⟨a,b⟩
  cases a <;> cases b <;> cases r <;> simp [GloballyCalibrated, Pair.set, Pair.get]

/-- Native candidate index is W0 + 2*W1 + 4*F0 + 8*F1. -/
def model (index : Nat) : Model :=
  {weak := ⟨index.testBit 0,index.testBit 1⟩,
   full := ⟨index.testBit 2,index.testBit 3⟩}

def allowed (coordinate : Nat) (bit : Bool) : Nat :=
  ((List.range 16).filter (fun i => i.testBit coordinate == bit)).foldl
    (fun mask i => mask ||| (2^i)) 0

def filterMask (mask coordinate : Nat) : Option Bool → Nat
  | none => mask
  | some bit => mask &&& allowed coordinate bit

def maskSize (mask : Nat) : Nat := ((List.range 16).filter mask.testBit).length

theorem filtering_never_adds_a_candidate (mask coordinate index : Nat) (data : Option Bool)
    (h : (filterMask mask coordinate data).testBit index = true) : mask.testBit index = true := by
  cases data with
  | none => exact h
  | some bit =>
    simp only [filterMask, Nat.testBit_and, Bool.and_eq_true] at h
    exact h.1

theorem allowed_exactly_matches_coordinate (index : Fin 16) (coordinate : Fin 4) (bit : Bool) :
    (allowed coordinate bit).testBit index = ((index : Nat).testBit coordinate == bit) := by
  revert index coordinate bit
  decide

theorem faithful_filter_preserves_actual_map (mask : Nat) (index : Fin 16)
    (coordinate : Fin 4) (bit : Bool)
    (present : mask.testBit index = true)
    (faithful : (index : Nat).testBit coordinate = bit) :
    (filterMask mask coordinate (some bit)).testBit index = true := by
  simp [filterMask, Nat.testBit_and, allowed_exactly_matches_coordinate, present, faithful]

theorem one_full_bit_leaves_eight (setting bit : Bool) :
    maskSize (filterMask 65535 (if setting then 3 else 2) (some bit)) = 8 := by
  cases setting <;> cases bit <;> decide

theorem full_and_fresh_same_setting_leave_four (setting full weak : Bool) :
    maskSize (filterMask (filterMask 65535 (if setting then 3 else 2) (some full))
      (if setting then 1 else 0) (some weak)) = 4 := by
  cases setting <;> cases full <;> cases weak <;> decide

theorem missing_full_indication_does_not_mean_failure :
    filterMask 65535 3 none = 65535 ∧ filterMask 65535 3 (some false) = 255 := by decide

inductive Application where
  | unobserved | unavailable | supported | failed
  deriving DecidableEq, Repr

inductive Diagnosis where
  | unobserved | unavailable | discrepancy | oldContradicted | currentAgreement
  deriving DecidableEq, Repr

inductive Phase where
  | oldInterface | formed | applicationRevised | committed | diagnosisRevised
  deriving DecidableEq, Repr

structure Config where
  fullFault : Fault := .faithful
  weakFault : Fault := .faithful
  clamp : Bool := false
  deriving DecidableEq, Repr

structure Body where
  account : Account
  stocks : Stocks
  context : Nat
  relay : Bool
  pending : Option Datum := none
  held : Bool := false
  installed : Bool := false
  retained : Bool := false
  mask : Option Nat := none
  fullRecord : Option Datum := none
  weakRecord : Option Datum := none
  contact : Option Datum := none
  application : Application := .unobserved
  diagnosis : Diagnosis := .unobserved
  proposal : Option Bool := none
  activation : Option Bool := none
  phase : Phase := .oldInterface
  deriving DecidableEq, Repr

/-- The parent is an immutable historical coordinate, not an extra usable
reserve. Only body's current account/stocks enter the current whole account. -/
structure State where
  parent : RemainingDependency.State
  config : Config
  body : Body
  deriving DecidableEq, Repr

def paid (b : Body) (w l t e r : Nat) (effect : Body → Body) : Body :=
  let debit := charge b.account w l t e r
  if debit.2 = .none then effect {b with account := debit.1} else b

def stockBit (p : Stocks) : Option Bool :=
  if p.load = 10 ∧ p.waste = 0 then some true
  else if p.load = 0 ∧ p.waste = 10 then some false else none

/-- The one-issued-transfer provenance is checked at the native entrance; this
sampler uses the persistent physical compartments, not a saved success flag. -/
def stockDatum (b : Body) (setting : Option Bool) : Option Datum := do
  let r ← setting
  let bit ← stockBit b.stocks
  pure ⟨b.context,r,bit⟩

def boundRecord (tags : Pair (Option Nat)) (setting : Option Bool)
    (contact : Option Datum) : Option Datum := do
  let r ← setting
  let context ← tags.get r
  let datum ← contact
  if datum.context = context ∧ datum.relay = r then some datum else none

def filterRecord (mask : Option Nat) (record : Option Datum) (full : Bool) : Option Nat := do
  let m ← mask
  match record with
  | none => some m
  | some d => some (filterMask m ((if d.relay then 1 else 0) + (if full then 2 else 0))
      (some d.response))

def reviseApplication (old : RemainingDependency.Body) : Option Datum → Application
  | none => .unavailable
  | some d => if old.values.get d.relay = some d.response then .supported else .failed

def disagreement (mask : Nat) (setting : Bool) : Bool :=
  let active := (List.range 16).filter mask.testBit
  let coord := if setting then 1 else 0
  active.any (fun i => !(i.testBit coord)) && active.any (fun i => i.testBit coord)

def propose (mask : Option Nat) (application : Application) (exercised : Option Bool) : Option Bool := do
  if application ≠ .failed then none else do
    let m ← mask
    let r ← exercised
    if disagreement m r then some r
    else if disagreement m (!r) then some (!r) else none

def reviseDiagnosis (old : RemainingDependency.Body) (full fresh : Option Datum) : Diagnosis :=
  match fresh, full with
  | some w, some f =>
      if w.response ≠ f.response then .discrepancy
      else if old.values.get w.relay ≠ some w.response then .oldContradicted
      else .currentAgreement
  | _, _ => .unavailable

inductive Event where
  | wait (units : Nat) | install | fullContact | fullWrite | filterFull
  | reviseApplication | choose | commit | command (setting : Bool)
  | challenge | weakContact | weakWrite | filterWeak | reviseDiagnosis | retain
  deriving DecidableEq, Repr

/-- Total event-attempt semantics. Arbitrary words need not follow the native
scheduler; denied charges have no effect. Actual words are checked separately. -/
def advance (parent : RemainingDependency.State) (cfg : Config) (b : Body) : Event → Body
  | .wait n => paid b 0 b.account.live 0 (ticks*n) 0 id
  | .install => paid b 24 58 8 ticks 0 fun t =>
      {t with installed := true, mask := some 65535, phase := .formed}
  | .fullContact => paid b 0 b.account.live 2 16384 0 fun t =>
      {t with contact := channel cfg.fullFault (stockDatum t parent.body.selected)}
  | .fullWrite => paid b 1 b.account.live 2 0 2 fun t =>
      {t with fullRecord := boundRecord parent.body.tags parent.body.selected t.contact,
              contact := none}
  | .filterFull => paid b 16 b.account.live 2 0 16 fun t =>
      {t with mask := filterRecord t.mask t.fullRecord true}
  | .reviseApplication => paid b 2 b.account.live 2 0 1 fun t =>
      {t with application := reviseApplication parent.body t.fullRecord,
              phase := .applicationRevised}
  | .choose => paid b 32 b.account.live 3 0 1 fun t =>
      {t with proposal := propose t.mask t.application parent.body.selected}
  | .commit => paid b 1 b.account.live 2 0 1 fun t =>
      {t with activation := if cfg.clamp then none else t.proposal, phase := .committed}
  | .command r => paid b 1 b.account.live 2 16384 0 fun t =>
      {t with relay := r, held := false}
  | .challenge => paid b 1 b.account.live 2 16384 0 fun t =>
      {t with pending := some ⟨t.context,t.relay,parent.config.weak.get t.relay⟩}
  | .weakContact => paid b 0 b.account.live 2 16384 0 fun t =>
      {t with contact := channel cfg.weakFault t.pending, pending := none}
  | .weakWrite => paid b 1 b.account.live 2 0 2 fun t =>
      {t with weakRecord := boundRecord parent.body.tags t.activation t.contact,
              contact := none}
  | .filterWeak => paid b 16 b.account.live 2 0 16 fun t =>
      {t with mask := filterRecord t.mask t.weakRecord false}
  | .reviseDiagnosis => paid b 2 b.account.live 2 0 1 fun t =>
      {t with diagnosis := reviseDiagnosis parent.body t.fullRecord t.weakRecord,
              phase := .diagnosisRevised}
  | .retain => paid b 1 b.account.live 0 (1024*b.account.live) 0 fun t =>
      {t with retained := true}

def step (s : State) (e : Event) : State := {s with body := advance s.parent s.config s.body e}

def run : State → List Event → State
  | s, [] => s
  | s, e::es => run (step s e) es

def process : Generative.Process State Event where step s e t := step s e = t

def actorTotal (b : Body) : Nat := b.account.fuel + b.account.spent

theorem paid_account_conserved (b : Body) (w l t e r : Nat) (effect : Body → Body)
    (h : ∀ z, (effect z).account = z.account) :
    actorTotal (paid b w l t e r effect) = actorTotal b := by
  unfold paid
  dsimp only
  split
  · unfold actorTotal
    rw [h]
    exact RemainingDependency.charge_conserves _ _ _ _ _ _
  · rfl

theorem paid_stocks_preserved (b : Body) (w l t e r : Nat) (effect : Body → Body)
    (h : ∀ z, (effect z).stocks = z.stocks) :
    (paid b w l t e r effect).stocks = b.stocks := by
  unfold paid
  dsimp only
  split
  · exact h _
  · rfl

theorem advance_account_conserved (parent : RemainingDependency.State) (cfg : Config)
    (b : Body) (e : Event) : actorTotal (advance parent cfg b e) = actorTotal b := by
  cases e <;> apply paid_account_conserved <;> intro z <;> rfl

theorem advance_stocks_preserved (parent : RemainingDependency.State) (cfg : Config)
    (b : Body) (e : Event) : (advance parent cfg b e).stocks = b.stocks := by
  cases e <;> apply paid_stocks_preserved <;> intro z <;> rfl

theorem run_parent_preserved (s : State) (es : List Event) : (run s es).parent = s.parent := by
  induction es generalizing s with
  | nil => rfl
  | cons e es ih => exact ih (step s e)

theorem run_account_conserved (s : State) (es : List Event) :
    actorTotal (run s es).body = actorTotal s.body := by
  induction es generalizing s with
  | nil => rfl
  | cons e es ih =>
    rw [run, ih]
    exact advance_account_conserved _ _ _ _

theorem run_stocks_preserved (s : State) (es : List Event) :
    (run s es).body.stocks = s.body.stocks := by
  induction es generalizing s with
  | nil => rfl
  | cons e es ih =>
    rw [run, ih]
    exact advance_stocks_preserved _ _ _ _

def wholeTotal (inherited : Nat) (s : State) : Nat :=
  inherited + actorTotal s.body + ticks * s.body.stocks.total

theorem whole_history_conserved (inherited : Nat) (s : State) (es : List Event) :
    wholeTotal inherited (run s es) = wholeTotal inherited s := by
  unfold wholeTotal
  rw [run_account_conserved, run_stocks_preserved]

theorem completion_and_old_report_preserved (s : State) (es : List Event) :
    (run s es).parent.ancestor = s.parent.ancestor ∧
    (run s es).parent.body.values = s.parent.body.values := by
  rw [run_parent_preserved]
  exact ⟨rfl,rfl⟩

theorem exhausted_source_still_blocks_another_full_transfer (s : State) (es : List Event)
    (response : Bool) (h : s.body.stocks.source = 0) :
    let t := (run s es).body
    fullTransfer t.account t.stocks response = (t.account,t.stocks,.source) := by
  apply empty_source_cannot_debit_actor
  rw [run_stocks_preserved, h]
  decide

theorem run_is_core_trace (s : State) (es : List Event) :
    Generative.Trace process s es (run s es) := by
  induction es generalizing s with
  | nil => exact .nil s
  | cons e es ih => exact .cons rfl (ih (step s e))

/-- Equal acquired indications/current masks give the same proposal regardless
of the hidden physical laws. The new weak challenge is what can disclose them. -/
theorem proposal_ignores_unread_physical_law (a b : RemainingDependency.State)
    (cfg : Config) (s : Body) (h : a.body.selected = b.body.selected) :
    advance a cfg s .choose = advance b cfg s .choose := by
  simp only [advance]
  rw [h]

def entrance (parent : RemainingDependency.State) (cfg : Config) : State :=
  {parent := parent, config := cfg,
   body := {account := {fuel := parent.body.account.fuel, start := parent.body.account.fuel,
                         live := parent.body.account.live, peak := parent.body.account.peak,
                         capacity := parent.body.account.capacity},
            stocks := parent.body.stocks, context := parent.body.context,
            relay := parent.body.relay, pending := parent.body.pending, held := parent.body.held}}

def fullEvidenceEvents : List Event :=
  [.install,.fullContact,.fullWrite,.filterFull,.reviseApplication,.choose,.commit]

def inquiryEvents (s : State) : List Event :=
  match s.body.activation with
  | none => [.retain]
  | some r => [.command r,.challenge,.weakContact,.weakWrite,.filterWeak,.reviseDiagnosis,.retain]

/-- Nominal funded sequence. Adverse native abort/retention sequences are
covered by exact saved-event fixtures, not inferred from this helper. -/
def continuation (s : State) : State :=
  let revised := run s fullEvidenceEvents
  run revised (inquiryEvents revised)

def mismatchParent : RemainingDependency.State :=
  RemainingDependency.continuation (RemainingDependency.entrance
    {weak := ⟨false,true⟩, full := ⟨false,false⟩})

def oldReportErrorParent : RemainingDependency.State :=
  RemainingDependency.continuation (RemainingDependency.entrance
    {weak := ⟨false,false⟩, full := ⟨false,false⟩, channels := ⟨.faithful,.flip⟩})

def positiveParent : RemainingDependency.State :=
  RemainingDependency.continuation (RemainingDependency.entrance
    {weak := ⟨false,true⟩, full := ⟨false,true⟩})

theorem actual_parent_pair_has_equal_retained_reports_and_consequences :
    mismatchParent.body.values = oldReportErrorParent.body.values ∧
    mismatchParent.body.selected = oldReportErrorParent.body.selected ∧
    mismatchParent.body.account = oldReportErrorParent.body.account ∧
    mismatchParent.body.stocks = oldReportErrorParent.body.stocks ∧
    mismatchParent.config.weak ≠ oldReportErrorParent.config.weak := by decide

theorem full_failure_revises_application_and_selects_real_inquiry :
    let s := run (entrance mismatchParent {}) fullEvidenceEvents
    s.body.fullRecord = some ⟨1,true,false⟩ ∧ s.body.mask = some 255 ∧
    s.body.application = .failed ∧ s.body.proposal = some true ∧
    s.body.activation = some true ∧ s.body.weakRecord = none ∧
    inquiryEvents s = [.command true,.challenge,.weakContact,.weakWrite,.filterWeak,.reviseDiagnosis,.retain] := by
  decide

theorem actual_funded_recheck_discloses_local_mismatch :
    let t := continuation (entrance mismatchParent {})
    t.body.fullRecord = some ⟨1,true,false⟩ ∧ t.body.weakRecord = some ⟨1,true,true⟩ ∧
    t.body.diagnosis = .discrepancy ∧ t.body.mask = some 204 ∧
    t.body.stocks = ⟨0,0,10⟩ ∧ t.body.account.fuel = 64767 ∧
    t.body.account.spent = 363251 ∧ t.body.account.live = 58 ∧ t.body.retained = true := by
  decide

theorem actual_funded_recheck_can_contradict_the_old_report :
    let t := continuation (entrance oldReportErrorParent {})
    t.body.fullRecord = some ⟨1,true,false⟩ ∧ t.body.weakRecord = some ⟨1,true,false⟩ ∧
    t.body.diagnosis = .oldContradicted ∧ t.body.mask = some 51 ∧
    t.parent.body.values = ⟨some false,some true⟩ ∧
    t.body.account.fuel = 64767 ∧ t.body.retained = true := by decide

theorem matched_clamp_preserves_full_evidence_revision_and_proposal :
    let active := run (entrance mismatchParent {}) fullEvidenceEvents
    let clamp := run (entrance mismatchParent {clamp := true}) fullEvidenceEvents
    active.body.fullRecord = clamp.body.fullRecord ∧ active.body.mask = clamp.body.mask ∧
    active.body.application = clamp.body.application ∧ active.body.proposal = clamp.body.proposal ∧
    active.body.account = clamp.body.account ∧
    active.body.activation = some true ∧ clamp.body.activation = none ∧
    inquiryEvents clamp = [.retain] := by decide

theorem clamped_history_does_not_acquire_the_fresh_reply :
    let t := continuation (entrance mismatchParent {clamp := true})
    t.body.fullRecord = some ⟨1,true,false⟩ ∧ t.body.mask = some 255 ∧
    t.body.weakRecord = none ∧ t.body.diagnosis = .unobserved ∧
    t.body.account.fuel = 156499 ∧ t.body.retained = true := by decide

theorem supported_tested_prediction_does_not_claim_global_calibration :
    let t := continuation (entrance positiveParent {})
    t.body.application = .supported ∧ t.body.mask = some 65280 ∧
    t.body.activation = none ∧ t.body.weakRecord = none ∧ maskSize 65280 = 8 := by decide

theorem missing_full_contact_withholds_mismatch_inquiry :
    let t := continuation (entrance mismatchParent {fullFault := .missing})
    t.body.fullRecord = none ∧ t.body.application = .unavailable ∧
    t.body.mask = some 65535 ∧ t.body.activation = none := by decide

theorem corrupted_fresh_contact_can_falsify_the_diagnosis :
    let t := continuation (entrance mismatchParent {weakFault := .flip})
    t.body.weakRecord = some ⟨1,true,false⟩ ∧ t.body.diagnosis = .oldContradicted ∧
    t.parent.config.weak.one = true ∧ t.body.mask = some 51 ∧
    (51 : Nat).testBit 2 = false := by decide

#print axioms untested_full_coordinate_is_underdetermined
#print axioms every_weak_query_word_preserves_the_ambiguity
#print axioms same_observed_pair_has_distinct_full_laws
#print axioms local_mismatch_refutes_global_calibration
#print axioms local_agreement_does_not_establish_global_calibration
#print axioms filtering_never_adds_a_candidate
#print axioms allowed_exactly_matches_coordinate
#print axioms faithful_filter_preserves_actual_map
#print axioms one_full_bit_leaves_eight
#print axioms full_and_fresh_same_setting_leave_four
#print axioms missing_full_indication_does_not_mean_failure
#print axioms paid_account_conserved
#print axioms paid_stocks_preserved
#print axioms advance_account_conserved
#print axioms advance_stocks_preserved
#print axioms run_parent_preserved
#print axioms run_account_conserved
#print axioms run_stocks_preserved
#print axioms whole_history_conserved
#print axioms completion_and_old_report_preserved
#print axioms exhausted_source_still_blocks_another_full_transfer
#print axioms run_is_core_trace
#print axioms proposal_ignores_unread_physical_law
#print axioms actual_parent_pair_has_equal_retained_reports_and_consequences
#print axioms full_failure_revises_application_and_selects_real_inquiry
#print axioms actual_funded_recheck_discloses_local_mismatch
#print axioms actual_funded_recheck_can_contradict_the_old_report
#print axioms matched_clamp_preserves_full_evidence_revision_and_proposal
#print axioms clamped_history_does_not_acquire_the_fresh_reply
#print axioms supported_tested_prediction_does_not_claim_global_calibration
#print axioms missing_full_contact_withholds_mismatch_inquiry
#print axioms corrupted_fresh_contact_can_falsify_the_diagnosis
end CalibrationRevision
