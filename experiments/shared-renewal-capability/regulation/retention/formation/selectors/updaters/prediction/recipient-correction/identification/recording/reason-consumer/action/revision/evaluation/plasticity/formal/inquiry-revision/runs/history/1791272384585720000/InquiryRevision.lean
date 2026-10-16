import PretrainingEvidence

/- Additive local reconfiguration; the imported plasticity law is unchanged.
   The existing spare pair is converted into one finite-state adapter. The two
   old acquisition latches are reused only at count four, between acquisitions. -/
namespace InquiryRevision
open PairedPlasticity
set_option maxHeartbeats 8000000
set_option maxRecDepth 32768

inductive Mode where
  | absent | idle | observed | missing | stale | committed
  deriving DecidableEq, Repr
inductive Channel where
  | faithful | missing | zero | falsePositive | wrongBinding
  deriving DecidableEq, Repr
structure State where
  parent : PairedPlasticity.State
  mode : Mode

def Context (s : State) : Prop := s.parent.count=4 ∧ s.parent.phase=.ready ∧
  s.parent.continuation=true ∧ s.parent.retired=0 ∧ Admitted s.parent ∧
  Known s.parent ∧ s.parent.parent.parent.permission=true
instance (s : State) : Decidable (Context s) := by unfold Context; infer_instance
def acquired (s : State) : Bool := s.mode=.observed || s.mode=.missing || s.mode=.stale
def release (s : State) : State :=
  if acquired s then
    {parent:={s.parent with ownBit:=false,recipientBit:=false},mode:=.idle}
  else s
def energy (s : State) := PairedPlasticity.energy s.parent
def material (s : State) := PairedPlasticity.material s.parent +
  2*(if s.mode=.absent then 0 else 1)
def sockets (s : State) := PretrainingEvidence.sockets s.parent
def observedBits (s : State) (c : Channel) : Bool × Bool :=
  match c with
  | .faithful => (decide (1≤sockets s),decide (2≤sockets s))
  | .falsePositive => (true,true)
  | _ => (false,false)
def readMode : Channel → Mode
  | .missing => .missing
  | .wrongBinding => .stale
  | _ => .observed

inductive Event where
  | inherited (event : PairedPlasticity.Event)
  | assemble | inspect (channel : Channel) | commit | shamCommit
  deriving DecidableEq, Repr

def Enabled (s : State) : Event → Prop
  | .inherited e => PairedPlasticity.Enabled (release s).parent e
  | .assemble => Context s ∧ 1≤fuel s.parent ∧ s.mode=.absent ∧ 1≤s.parent.replacement
  | .inspect _ => Context s ∧ 1≤fuel s.parent ∧
      (s.mode=.idle ∨ s.mode=.missing ∨ s.mode=.stale)
  | .commit | .shamCommit => Context s ∧ 1≤fuel s.parent ∧ s.mode=.observed ∧
      s.parent.ownBit=true ∧ s.parent.recipientBit=true
instance (s : State) (e : Event) : Decidable (Enabled s e) := by
  cases e <;> unfold Enabled <;> infer_instance

def advance (laws : RecipientCorrection.Laws) (s : State) : Event → State
  | .inherited e => {release s with parent:=PairedPlasticity.advance laws (release s).parent e}
  | .assemble => {parent:={withFuel s.parent (fuel s.parent-1) with replacement:=s.parent.replacement-1},mode:=.idle}
  | .inspect c =>
      {parent:={withFuel s.parent (fuel s.parent-1) with
        ownBit:=(observedBits s c).1,recipientBit:=(observedBits s c).2},mode:=readMode c}
  | .commit => {parent:={withFuel s.parent (fuel s.parent-1) with
      ownBit:=false,recipientBit:=false,continuation:=false},mode:=.committed}
  | .shamCommit => {parent:={withFuel s.parent (fuel s.parent-1) with
      ownBit:=false,recipientBit:=false},mode:=.idle}
def charge (laws : RecipientCorrection.Laws) (s : State) : Event → Nat
  | .inherited e => PairedPlasticity.charge laws (release s).parent e
  | _ => 1
def Step (laws : RecipientCorrection.Laws) (s : State) (e : Event) (t : State) :=
  Enabled s e ∧ t=advance laws s e
def process (laws : RecipientCorrection.Laws) : Generative.Process State Event := ⟨Step laws⟩
def run (laws : RecipientCorrection.Laws) (s : State) : List Event → State
  | [] => s
  | e::es => run laws (advance laws s e) es
def spent (laws : RecipientCorrection.Laws) (s : State) : List Event → Nat
  | [] => 0
  | e::es => charge laws s e+spent laws (advance laws s e) es
def Runnable (laws : RecipientCorrection.Laws) (s : State) : List Event → Prop
  | [] => True
  | e::es => Enabled s e ∧ Runnable laws (advance laws s e) es
instance runnableDecidable (laws : RecipientCorrection.Laws) (s : State) (es : List Event) : Decidable (Runnable laws s es) :=
  match es with
  | [] => isTrue trivial
  | e::es => let _:=runnableDecidable laws (advance laws s e) es
            inferInstanceAs (Decidable (Enabled s e ∧ Runnable laws (advance laws s e) es))

theorem runnable_trace {laws : RecipientCorrection.Laws} {s : State} {es : List Event}
    (h : Runnable laws s es) : Generative.Trace (process laws) s es (run laws s es) := by
  induction es generalizing s with
  | nil => exact .nil _
  | cons e es ih => exact .cons ⟨h.1,rfl⟩ (ih h.2)

theorem release_energy (s : State) : energy (release s)=energy s := by
  unfold release; split <;> rfl
theorem release_material (s : State) : material (release s)=material s := by
  cases hm:s.mode <;> simp [release,acquired,material,PairedPlasticity.material,hm]

theorem step_energy {laws : RecipientCorrection.Laws} {s t : State} {e : Event}
    (h : Step laws s e t) : energy t+charge laws s e=energy s := by
  rcases h with ⟨he,rfl⟩
  cases e with
  | inherited e =>
      have hh:=PairedPlasticity.step_energy (laws:=laws) (show PairedPlasticity.Step laws (release s).parent e _ from ⟨he,rfl⟩)
      exact hh.trans (release_energy s)
  | assemble | inspect c | commit | shamCommit =>
      have hb:=fuel_account s.parent (fuel s.parent-1)
      have hf : 1≤fuel s.parent := he.2.1
      simp only [advance,energy,charge,PairedPlasticity.energy,withFuel,withBalances,setCore] at hb ⊢
      all_goals omega

theorem step_material {laws : RecipientCorrection.Laws} {s t : State} {e : Event}
    (h : Step laws s e t) : material t=material s := by
  rcases h with ⟨he,rfl⟩
  cases e with
  | inherited e =>
      have hh:=PairedPlasticity.step_material (laws:=laws) (show PairedPlasticity.Step laws (release s).parent e _ from ⟨he,rfl⟩)
      change PairedPlasticity.material (PairedPlasticity.advance laws (release s).parent e)+_=material s
      rw [hh]; exact release_material s
  | assemble =>
      have hm:=he.2.2.1
      have hp:=he.2.2.2
      change PairedPlasticity.material {s.parent with replacement:=s.parent.replacement-1}+2 =
        PairedPlasticity.material s.parent+2*(if s.mode=.absent then 0 else 1)
      rw [hm]
      simp only [ite_true,Nat.mul_zero,Nat.add_zero,PairedPlasticity.material]
      omega
  | inspect c =>
      have hm:=he.2.2
      rcases hm with hm|hm|hm
      all_goals cases c <;> simp only [advance,material,readMode,hm] <;> rfl
  | commit | shamCommit =>
      have hm:=he.2.2.1
      simp only [advance,material,hm] <;> rfl

theorem trace_energy {laws : RecipientCorrection.Laws} {s t : State} {es : List Event}
    (h : Generative.Trace (process laws) s es t) : energy t+spent laws s es=energy s := by
  induction h with
  | nil => simp [spent]
  | cons he _ ih =>
      have hh:=step_energy he
      rcases he with ⟨_,rfl⟩
      simp only [spent]; omega
theorem trace_material {laws : RecipientCorrection.Laws} {s t : State} {es : List Event}
    (h : Generative.Trace (process laws) s es t) : material t=material s := by
  induction h with
  | nil => rfl
  | cons he _ ih => exact ih.trans (step_material he)

theorem faithful_read_uses_actual_sockets (laws : RecipientCorrection.Laws) (s : State) :
    (advance laws s (.inspect .faithful)).parent.ownBit=decide (1≤sockets s) ∧
    (advance laws s (.inspect .faithful)).parent.recipientBit=decide (2≤sockets s) ∧
    (advance laws s (.inspect .faithful)).mode=.observed := ⟨rfl,rfl,rfl⟩
theorem commit_changes_only_access_and_spent_fuel (laws : RecipientCorrection.Laws) (s : State) :
    (advance laws s .commit).parent.count=s.parent.count ∧
    (advance laws s .commit).parent.n=s.parent.n ∧
    (advance laws s .commit).parent.link0=s.parent.link0 ∧
    (advance laws s .commit).parent.link1=s.parent.link1 ∧
    patient (advance laws s .commit).parent=patient s.parent ∧
    (advance laws s .commit).parent.ownSource=s.parent.ownSource ∧
    (advance laws s .commit).parent.recipientSource=s.parent.recipientSource ∧
    (advance laws s .commit).parent.continuation=false := ⟨rfl,rfl,rfl,rfl,rfl,rfl,rfl,rfl⟩

theorem commit_replaces_enabled_inquiry_with_closure {laws : RecipientCorrection.Laws} {s : State}
    (h : Enabled s .commit) :
    ¬Enabled (advance laws s .commit) (.inherited .ownPay) ∧
    Enabled (advance laws s .commit) (.inherited .close) := by
  have hc:=h.1.1
  have hp:=h.1.2.1
  simp [Enabled,advance,release,acquired,PairedPlasticity.Enabled,limit,withFuel,withBalances,setCore,hc,hp]

theorem inherited_event_invalidates_observation (laws : RecipientCorrection.Laws) (s : State)
    (e : PairedPlasticity.Event) (h:s.mode=.observed) :
    (advance laws s (.inherited e)).mode=.idle ∧
    ¬Enabled (advance laws s (.inherited e)) .commit := by
  simp [advance,release,acquired,h,Enabled]
theorem missing_or_stale_cannot_commit (s : State) (h:s.mode=.missing ∨ s.mode=.stale) :
    ¬Enabled s .commit := by rcases h with h|h <;> simp [Enabled,h]

def entry (v : Variant := .active) : State := ⟨PlasticityWitness.entry v true,.absent⟩
def teachingPrefix (es : List PairedPlasticity.Event := PlasticityWitness.aligned) : List Event := es.map Event.inherited
def s4 := run PlasticityWitness.laws (entry) (teachingPrefix)
def assembled := advance PlasticityWitness.laws s4 .assemble
def observed := advance PlasticityWitness.laws assembled (.inspect .faithful)
def revised := advance PlasticityWitness.laws observed .commit
def adaptation : List Event := [.assemble,.inspect .faithful,.commit]
def assessment : List Event := [.inherited .close,.inherited .read,.inherited .assess]
def action : List Event := PlasticityWitness.actionWord.map Event.inherited
def assessed := run PlasticityWitness.laws revised assessment
def final := run PlasticityWitness.laws assessed action
def whole := teachingPrefix++adaptation++assessment++action

theorem actual_same_continuing_prefix :
    Runnable PlasticityWitness.laws (entry) teachingPrefix ∧
    s4.parent=PairedPlasticity.run PlasticityWitness.laws (PlasticityWitness.entry .active true) PlasticityWitness.aligned ∧
    s4.parent.continuation=true ∧ fuel s4.parent=14 ∧ patient s4.parent=36 ∧
    s4.parent.n=4 ∧ s4.parent.replacement=1 ∧ energy s4=88 ∧ material s4=68 := by decide
theorem actual_adapter_and_read :
    Enabled s4 .assemble ∧ Enabled assembled (.inspect .faithful) ∧ Enabled observed .commit ∧
    assembled.parent.replacement=0 ∧ material assembled=68 ∧
    fuel assembled.parent=13 ∧ fuel observed.parent=12 ∧
    observed.parent.ownBit=true ∧ observed.parent.recipientBit=true := by decide
theorem actual_change_in_access :
    Enabled s4 (.inherited .ownPay) ∧ ¬Enabled s4 (.inherited .close) ∧
    revised.parent.continuation=false ∧ revised.parent.count=4 ∧
    ¬Enabled revised (.inherited .ownPay) ∧ Enabled revised (.inherited .close) ∧
    fuel revised.parent=11 ∧ patient revised.parent=36 ∧ revised.parent.n=4 := by decide
theorem whole_actual_runnable : Runnable PlasticityWitness.laws (entry) whole := by decide
theorem whole_actual_trace : Generative.Trace (process PlasticityWitness.laws) (entry) whole final :=
  runnable_trace whole_actual_runnable
theorem final_actual_accounts : fuel final.parent=1 ∧ patient final.parent=46 ∧
    energy final=75 ∧ material final=68 ∧ final.parent.count=4 ∧ final.parent.n=4 ∧
    final.parent.link0=some .positive ∧ final.parent.link1=some .positive ∧
    final.parent.portMode=.consumed ∧ (core final.parent).packets=0 ∧
    spent PlasticityWitness.laws (entry) whole=43 ∧
    505=351+36+43+energy final := by decide
theorem no_further_teaching_in_suffix :
    (adaptation++assessment++action).count (.inherited .recipientPay)=0 ∧
    final.parent.ownSource=s4.parent.ownSource ∧ final.parent.recipientSource=s4.parent.recipientSource ∧
    final.parent.training=s4.parent.training ∧ final.parent.revision=s4.parent.revision ∧
    (core final.parent).hardware.q=(core s4.parent).hardware.q := by decide

def miss := advance PlasticityWitness.laws assembled (.inspect .missing)
def zero := advance PlasticityWitness.laws assembled (.inspect .zero)
def wrong := advance PlasticityWitness.laws assembled (.inspect .wrongBinding)
def sham := advance PlasticityWitness.laws observed .shamCommit
def stale := advance PlasticityWitness.laws observed (.inherited (.scope true))
theorem blocked_evidence_controls :
    ¬Enabled assembled .commit ∧ ¬Enabled miss .commit ∧ ¬Enabled zero .commit ∧
    ¬Enabled wrong .commit ∧ miss.mode=.missing ∧ wrong.mode=.stale ∧
    zero.mode=.observed ∧ fuel miss.parent=12 ∧ fuel zero.parent=12 ∧ fuel wrong.parent=12 := by decide
theorem sham_keeps_old_obstruction : Enabled observed .shamCommit ∧
    fuel sham.parent=11 ∧ sham.parent.continuation=true ∧
    Enabled sham (.inherited .ownPay) ∧ ¬Enabled sham (.inherited .close) := by decide
theorem actual_staleness_and_reacquisition :
    Enabled observed (.inherited (.scope true)) ∧ stale.mode=.idle ∧
    ¬Enabled stale .commit ∧ Enabled stale (.inspect .faithful) ∧
    Enabled (advance PlasticityWitness.laws stale (.inspect .faithful)) .commit := by decide

def noLossWord := PlasticityWitness.pair true false ++ PlasticityWitness.pair false false ++
  PlasticityWitness.pair false false ++ PlasticityWitness.pair true false
def noLoss := run PlasticityWitness.laws (entry) (teachingPrefix noLossWord)
def noLossAdapter := advance PlasticityWitness.laws noLoss .assemble
theorem real_zero_and_false_positive :
    Runnable PlasticityWitness.laws (entry) (teachingPrefix noLossWord) ∧
    patient noLoss.parent=40 ∧ sockets noLoss=0 ∧
    ¬Enabled (advance PlasticityWitness.laws noLossAdapter (.inspect .faithful)) .commit ∧
    Enabled (advance PlasticityWitness.laws noLossAdapter (.inspect .falsePositive)) .commit := by decide

def scopeDenied := advance PlasticityWitness.laws s4 (.inherited (.scope false))
def permissionDenied := advance PlasticityWitness.laws s4 (.inherited (.permission false))
def noPart : State := {s4 with parent:={s4.parent with replacement:=0,idleParts:=1}}
def withFuelAtFour (f : Nat) : State :=
  {s4 with parent:={withFuel s4.parent f with idleFuel:=14-f}}
theorem component_authority_and_funding_controls :
    ¬Enabled scopeDenied .assemble ∧ ¬Enabled permissionDenied .assemble ∧
    ¬Enabled noPart .assemble ∧ material noPart=68 ∧
    ¬Enabled (withFuelAtFour 0) .assemble ∧ energy (withFuelAtFour 0)=88 ∧
    ¬Enabled (advance PlasticityWitness.laws (withFuelAtFour 1) .assemble) (.inspect .faithful) ∧
    ¬Enabled (run PlasticityWitness.laws (withFuelAtFour 2) [.assemble,.inspect .faithful]) .commit := by decide
theorem sharp_funded_response_boundary :
    Runnable PlasticityWitness.laws (withFuelAtFour 13) (adaptation++assessment++action) ∧
    fuel (run PlasticityWitness.laws (withFuelAtFour 13) (adaptation++assessment++action)).parent=0 ∧
    ¬Runnable PlasticityWitness.laws (withFuelAtFour 12) (adaptation++assessment++action) := by decide

def contrasted (v : Variant) (es : List PairedPlasticity.Event := PlasticityWitness.aligned) :=
  run PlasticityWitness.laws (entry v) (teachingPrefix es++adaptation++assessment)
theorem signs_still_control_response :
    Runnable PlasticityWitness.laws (entry .active) (teachingPrefix PlasticityWitness.opposed++adaptation++assessment) ∧
    (contrasted .active PlasticityWitness.opposed).parent.portMode=.abstain ∧
    (contrasted .active PlasticityWitness.mixed).parent.portMode=.abstain ∧
    (contrasted .inert).parent.portMode=.abstain ∧ (contrasted .gated).parent.portMode=.abstain ∧
    (contrasted .conventional).parent.portMode=.help ∧
    (contrasted .active PlasticityWitness.opposed).parent.continuation=false ∧
    patient (contrasted .active PlasticityWitness.opposed).parent=36 := by decide

def modeCode : Mode → Nat | .absent => 0 | .idle => 1 | .observed => 2 | .missing => 3 | .stale => 4 | .committed => 5
def vector (s : State) : List Int := (PlasticityWitness.vector s.parent).set 20 (material s) ++
  [(modeCode s.mode:Int),(limit s.parent:Int),if s.parent.ownBit then 1 else 0,if s.parent.recipientBit then 1 else 0,
   ((core s.parent).hardware.q:Int)]
def row (name : String) (s : State) : IO Unit :=
  IO.println ("INQUIRY "++name++" ["++String.intercalate "," ((vector s).map toString)++"]")

end InquiryRevision

#print axioms InquiryRevision.runnable_trace
#print axioms InquiryRevision.release_energy
#print axioms InquiryRevision.release_material
#print axioms InquiryRevision.step_energy
#print axioms InquiryRevision.step_material
#print axioms InquiryRevision.trace_energy
#print axioms InquiryRevision.trace_material
#print axioms InquiryRevision.faithful_read_uses_actual_sockets
#print axioms InquiryRevision.commit_changes_only_access_and_spent_fuel
#print axioms InquiryRevision.commit_replaces_enabled_inquiry_with_closure
#print axioms InquiryRevision.inherited_event_invalidates_observation
#print axioms InquiryRevision.missing_or_stale_cannot_commit
#print axioms InquiryRevision.actual_same_continuing_prefix
#print axioms InquiryRevision.actual_adapter_and_read
#print axioms InquiryRevision.actual_change_in_access
#print axioms InquiryRevision.whole_actual_runnable
#print axioms InquiryRevision.whole_actual_trace
#print axioms InquiryRevision.final_actual_accounts
#print axioms InquiryRevision.no_further_teaching_in_suffix
#print axioms InquiryRevision.blocked_evidence_controls
#print axioms InquiryRevision.sham_keeps_old_obstruction
#print axioms InquiryRevision.actual_staleness_and_reacquisition
#print axioms InquiryRevision.real_zero_and_false_positive
#print axioms InquiryRevision.component_authority_and_funding_controls
#print axioms InquiryRevision.sharp_funded_response_boundary
#print axioms InquiryRevision.signs_still_control_response
#eval InquiryRevision.row "entry" InquiryRevision.entry
#eval InquiryRevision.row "s4" InquiryRevision.s4
#eval InquiryRevision.row "assembled" InquiryRevision.assembled
#eval InquiryRevision.row "observed" InquiryRevision.observed
#eval InquiryRevision.row "revised" InquiryRevision.revised
#eval InquiryRevision.row "assessed" InquiryRevision.assessed
#eval InquiryRevision.row "final" InquiryRevision.final
#eval InquiryRevision.row "miss" InquiryRevision.miss
#eval InquiryRevision.row "zero" InquiryRevision.zero
#eval InquiryRevision.row "wrong" InquiryRevision.wrong
#eval InquiryRevision.row "sham" InquiryRevision.sham
#eval InquiryRevision.row "stale" InquiryRevision.stale
#eval InquiryRevision.row "noLoss" InquiryRevision.noLoss
