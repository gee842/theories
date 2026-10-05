import SuccessorLearning
import RouteDiagnostics

/-!
A declared finite monitor attached to an admitted, retained zero-cash carrier.
Eight binary cells back three frame bits, two four-valued summaries, and binding.
A supplied finite head supplies sequence/window control, a two-frame lease and
functional credit/bus contacts. This does not derive its recipe or calibration.
Ordinary stages compose the imported learner's fund and perform transitions.
The imported operational learner channel is present; invalid/unknown bus-contact
readings block publication. Faulty or absent-channel learning is not modeled here.
Only plant work reads the law. No full q record, gamma read, or epoch archive is
added. The source-data handoff and stochastic Python law are separately checked.
-/
namespace FormedRouteMonitor
open RecipientCorrection
open FormedRecipientRoute (Route Template)

inductive Summary where
  | unseen | unchanged | flipped | conflict
  deriving DecidableEq, Repr

def encode (b : Bool) : Summary := if b then .flipped else .unchanged

def merge (old : Summary) (b : Bool) : Summary :=
  match old with
  | .unseen => encode b
  | .conflict => .conflict
  | _ => if old = encode b then old else .conflict

def summaryBit : Summary → Option Bool
  | .unchanged => some false
  | .flipped => some true
  | _ => none

def classify (success failure : Summary) : Option RouteDiagnostics.Class :=
  if success = .conflict ∨ failure = .conflict then none else
  match summaryBit success,summaryBit failure with
  | some x,some y => RouteDiagnostics.classify x y
  | some true,none => some .privateZero
  | none,some false => some .unchanged
  | _,_ => none

def SoundSummary (route : Route) (success failure : Summary) : Prop :=
  (success = .unseen ∨ success = encode (RouteDiagnostics.signature route true)) ∧
  (failure = .unseen ∨ failure = encode (RouteDiagnostics.signature route false))

theorem summary_classification_sound (route : Route) (success failure : Summary)
    (h : SoundSummary route success failure) (c : RouteDiagnostics.Class)
    (hc : classify success failure = some c) : c = RouteDiagnostics.routeClass route := by
  cases route <;> cases success <;> cases failure <;>
    simp_all [SoundSummary,encode,RouteDiagnostics.signature,classify,summaryBit,RouteDiagnostics.classify,RouteDiagnostics.routeClass]

inductive Quota where | two | one | exhausted
  deriving DecidableEq, Repr

def nextQuota : Quota → Quota
  | .two => .one
  | _ => .exhausted

inductive Phase where
  | absent | ready | rented | sensed | preRead | armed | worked | sealed
  | observed | written | postRead | broken
  deriving DecidableEq, Repr

structure State where
  core : SuccessorLearning.State
  freeCells : Nat
  freeHeads : Nat
  installed : Bool
  phase : Phase
  quota : Quota
  pre : Bool
  receipt : Bool
  post : Bool
  success : Summary
  failure : Summary
  binding : Bool
  busValid : Bool
  deriving DecidableEq, Repr

/-- Head contact input, sampled only during paid sealing. It is not route identity. -/
abbrev Bus := Option Bool

inductive Event where
  | assemble | rent | sense | preRead | arm | work | sealWindow | observe | write
  | postRead | commit | breakBinding
  deriving DecidableEq, Repr

/-- All admitted frames carry zero private cash. Exact funding equals shortfall. -/
def ordinary (s : SuccessorLearning.State) (op : SuccessorLearning.Op) : SuccessorLearning.State :=
  SuccessorLearning.advance SuccessorLearning.primary (SuccessorLearning.advance SuccessorLearning.primary s (.fund op)) (.perform op)

def OrdinaryEnabled (s : SuccessorLearning.State) (op : SuccessorLearning.Op) : Prop :=
  SuccessorLearning.Enabled SuccessorLearning.primary s (.fund op) ∧
  SuccessorLearning.Enabled SuccessorLearning.primary (SuccessorLearning.advance SuccessorLearning.primary s (.fund op)) (.perform op)

/-- Monitor fee is transferred to the carrier and dissipated; no extra cash stays. -/
def fee (s : SuccessorLearning.State) (n : Nat) : SuccessorLearning.State :=
  let funded := {s with recipient := s.recipient-n, childFuel := s.childFuel+n}
  {funded with childFuel := funded.childFuel-n, spent := funded.spent+n}

def FeeEnabled (s : SuccessorLearning.State) (n : Nat) : Prop :=
  s.childFuel = 0 ∧ 1+n ≤ s.recipient

/-- Funding precedes work. Only the actual work-stage recipient increase is sensed. -/
def creditContact (s : SuccessorLearning.State) : Bool :=
  let funded := SuccessorLearning.advance SuccessorLearning.primary s (.fund .work)
  funded.recipient < (SuccessorLearning.advance SuccessorLearning.primary funded (.perform .work)).recipient

def Enabled (s : State) : Event → Prop
  | .assemble => s.phase = .absent ∧ s.installed = false ∧
      s.core.carrier = true ∧ s.core.routing = true ∧ s.core.template.q < 4 ∧
      8 ≤ s.freeCells ∧ 1 ≤ s.freeHeads ∧ FeeEnabled s.core 2
  | .rent => s.phase = .ready ∧ s.installed = true ∧ s.binding = true ∧
      s.quota ≠ .exhausted ∧ OrdinaryEnabled s.core .rent
  | .sense => s.phase = .rented ∧ OrdinaryEnabled s.core .sense
  | .preRead => s.phase = .sensed ∧ FeeEnabled s.core 1
  | .arm => s.phase = .preRead ∧ FeeEnabled s.core 1
  | .work => s.phase = .armed ∧ OrdinaryEnabled s.core .work
  | .sealWindow => s.phase = .worked ∧ FeeEnabled s.core 1
  | .observe => s.phase = .sealed ∧ OrdinaryEnabled s.core .observe
  | .write => s.phase = .observed ∧ OrdinaryEnabled s.core .write
  | .postRead => s.phase = .written ∧ FeeEnabled s.core 1
  | .commit => s.phase = .postRead ∧ s.binding = true ∧ s.busValid = true ∧
      FeeEnabled s.core 1
  | .breakBinding => True

def advance (bus : Bus) (s : State) : Event → State
  | .assemble => {s with
      core := fee s.core 2, freeCells := s.freeCells - 8,
      freeHeads := s.freeHeads - 1, installed := true, phase := .ready, quota := .two,
      pre := false, receipt := false, post := false, success := .unseen,
      failure := .unseen, binding := true, busValid := false}
  | .rent => {s with
      core := ordinary s.core .rent, phase := .rented,
      quota := nextQuota s.quota, busValid := false}
  | .sense => {s with
      core := ordinary s.core .sense, phase := .sensed}
  | .preRead => {s with
      core := fee s.core 1, pre := RouteDiagnostics.bit s.core.template.q,
      phase := .preRead}
  | .arm => {s with
      core := fee s.core 1, receipt := false, phase := .armed}
  | .work => {s with
      core := ordinary s.core .work,
      receipt := creditContact s.core, phase := .worked}
  | .sealWindow => {s with
      core := fee s.core 1, busValid := bus == some true,
      phase := .sealed}
  | .observe => {s with
      core := ordinary s.core .observe, phase := .observed}
  | .write => {s with
      core := ordinary s.core .write, phase := .written}
  | .postRead => {s with
      core := fee s.core 1, post := RouteDiagnostics.bit s.core.template.q,
      phase := .postRead}
  | .commit => {s with
      core := fee s.core 1, phase := .ready,
      success := if s.receipt then merge s.success (s.post != s.pre) else s.success,
      failure := if s.receipt then s.failure else merge s.failure (s.post != s.pre)}
  | .breakBinding => {s with
      binding := false, success := .unseen,
      failure := .unseen, phase := .broken, busValid := false}

def Step (bus : Bus) (s : State) (e : Event) (t : State) : Prop :=
  Enabled s e ∧ t = advance bus s e

inductive Trace (bus : Bus) : State → List Event → State → Prop where
  | nil (s : State) : Trace bus s [] s
  | cons {s m t : State} {e : Event} {es : List Event} :
      Step bus s e m → Trace bus m es t → Trace bus s (e::es) t

def energy (s : State) : Nat := SuccessorLearning.energy s.core
def cells (s : State) : Nat := s.freeCells + if s.installed then 8 else 0
def heads (s : State) : Nat := s.freeHeads + if s.installed then 1 else 0

def diagnosis (s : State) : Option RouteDiagnostics.Class :=
  if s.binding then classify s.success s.failure else none

theorem credit_contact_is_actual_work_outcome (s : SuccessorLearning.State) :
    creditContact s = SuccessorLearning.outcome s := by
  unfold creditContact
  cases h : SuccessorLearning.outcome s <;>
    simp [SuccessorLearning.advance,SuccessorLearning.primary,SuccessorLearning.cost,SuccessorLearning.outcome,SuccessorLearning.command] at h ⊢ <;>
    simp_all

theorem fee_accounts (s : SuccessorLearning.State) (n : Nat) (h : FeeEnabled s n) :
    SuccessorLearning.energy (fee s n) = SuccessorLearning.energy s ∧ 1 ≤ (fee s n).recipient ∧
    (fee s n).childFuel = 0 := by
  rcases h with ⟨hf,hr⟩
  simp only [fee,SuccessorLearning.energy]
  omega

theorem ordinary_accounts (s : SuccessorLearning.State) (op : SuccessorLearning.Op) (h : OrdinaryEnabled s op) :
    SuccessorLearning.energy (ordinary s op) = SuccessorLearning.energy s ∧
    (1 ≤ s.recipient → 1 ≤ (ordinary s op).recipient) ∧
    (ordinary s op).template.route = s.template.route ∧
    (ordinary s op).originalActor = s.originalActor := by
  have h₁ : SuccessorLearning.Step SuccessorLearning.primary s (.fund op) _ := ⟨h.1,rfl⟩
  have h₂ : SuccessorLearning.Step SuccessorLearning.primary (SuccessorLearning.advance SuccessorLearning.primary s (.fund op)) (.perform op) _ := ⟨h.2,rfl⟩
  exact ⟨(SuccessorLearning.step_energy_account h₂).trans (SuccessorLearning.step_energy_account h₁),
    fun hr => SuccessorLearning.step_preserves_recipient_floor h₂ (SuccessorLearning.step_preserves_recipient_floor h₁ hr),
    (SuccessorLearning.step_preserves_actor_route_and_carrier h₂).2.1.trans
      (SuccessorLearning.step_preserves_actor_route_and_carrier h₁).2.1,
    (SuccessorLearning.step_preserves_actor_route_and_carrier h₂).1.trans
      (SuccessorLearning.step_preserves_actor_route_and_carrier h₁).1⟩

theorem step_accounts {bus : Bus} {s t : State} {e : Event} (h : Step bus s e t) :
    energy t = energy s ∧ cells t = cells s ∧ heads t = heads s ∧
    t.core.originalActor = s.core.originalActor ∧
    t.core.template.route = s.core.template.route ∧
    (1 ≤ s.core.recipient → 1 ≤ t.core.recipient) := by
  rcases h with ⟨he,rfl⟩
  cases e with
  | assemble =>
      rcases he with ⟨_,hi,_,_,_,hc,hh,hf⟩
      have ha := fee_accounts _ _ hf
      simp only [advance,energy,cells,heads,hi,Bool.false_eq_true,ite_false,ite_true]
      exact ⟨ha.1,by omega,by omega,rfl,rfl,fun _ => ha.2.1⟩
  | rent =>
      have ha := ordinary_accounts _ _ he.2.2.2.2
      exact ⟨ha.1,rfl,rfl,ha.2.2.2,ha.2.2.1,ha.2.1⟩
  | sense | work | observe | write =>
      have ha := ordinary_accounts _ _ he.2
      exact ⟨ha.1,rfl,rfl,ha.2.2.2,ha.2.2.1,ha.2.1⟩
  | preRead | arm | sealWindow | postRead =>
      have ha := fee_accounts _ _ he.2
      exact ⟨ha.1,rfl,rfl,rfl,rfl,fun _ => ha.2.1⟩
  | commit =>
      have ha := fee_accounts _ _ he.2.2.2
      exact ⟨ha.1,rfl,rfl,rfl,rfl,fun _ => ha.2.1⟩
  | breakBinding => exact ⟨rfl,rfl,rfl,rfl,rfl,id⟩

theorem trace_accounts {bus : Bus} {s t : State} {es : List Event}
    (h : Trace bus s es t) :
    energy t = energy s ∧ cells t = cells s ∧ heads t = heads s ∧
    t.core.originalActor = s.core.originalActor ∧
    t.core.template.route = s.core.template.route ∧
    (1 ≤ s.core.recipient → 1 ≤ t.core.recipient) := by
  induction h with
  | nil => exact ⟨rfl,rfl,rfl,rfl,rfl,id⟩
  | cons hs _ ih =>
      have hm := step_accounts hs
      exact ⟨ih.1.trans hm.1,ih.2.1.trans hm.2.1,ih.2.2.1.trans hm.2.2.1,
        ih.2.2.2.1.trans hm.2.2.2.1,ih.2.2.2.2.1.trans hm.2.2.2.2.1,
        fun hr => ih.2.2.2.2.2 (hm.2.2.2.2.2 hr)⟩

def run (bus : Bus) : State → List Event → State
  | s,[] => s
  | s,e::es => run bus (advance bus s e) es

def allEnabled (bus : Bus) : State → List Event → Prop
  | _,[] => True
  | s,e::es => Enabled s e ∧ allEnabled bus (advance bus s e) es

instance (s : State) (e : Event) : Decidable (Enabled s e) := by
  cases e <;> unfold Enabled FeeEnabled OrdinaryEnabled <;> infer_instance

instance allEnabledDecidable (bus : Bus) (s : State) (es : List Event) :
    Decidable (allEnabled bus s es) :=
  match es with
  | [] => isTrue trivial
  | e::es => @instDecidableAnd (Enabled s e) (allEnabled bus (advance bus s e) es)
      (inferInstance) (allEnabledDecidable bus (advance bus s e) es)

theorem enabled_list_is_trace (bus : Bus) (s : State) (es : List Event)
    (h : allEnabled bus s es) : Trace bus s es (run bus s es) := by
  induction es generalizing s with
  | nil => exact .nil s
  | cons e es ih => exact .cons ⟨h.1,rfl⟩ (ih _ h.2)

def frame : List Event :=
  [.rent,.sense,.preRead,.arm,.work,.sealWindow,.observe,.write,.postRead,.commit]

def physicalRecord (s : State) : Bool × Bool × Bool := (s.pre,s.receipt,s.post)
def sampleProjection (s : RouteDiagnostics.Sample) : Bool × Bool × Bool :=
  (RouteDiagnostics.bit s.before,s.receipt,RouteDiagnostics.bit s.after)

/-- This is a relation to a mathematical sample, not full-q readable storage. -/
theorem completed_frame_projects_sample (bus : Bus) (s : State) :
    physicalRecord (run bus s frame) =
      sampleProjection (RouteDiagnostics.sample s.core.template.route s.core.template.q
        (receiptOf (RouteDiagnostics.bit s.core.template.q) s.core.law true)) := by
  simp only [frame,run,advance,physicalRecord,fee,ordinary,SuccessorLearning.advance,SuccessorLearning.primary,
    SuccessorLearning.cost,SuccessorLearning.command,SuccessorLearning.outcome,SuccessorLearning.revised,creditContact,
    sampleProjection,RouteDiagnostics.sample,RouteDiagnostics.written,RouteDiagnostics.bit,FormedRecipientRoute.action]
  cases h : receiptOf (packedAct s.core.template.q .recipient) s.core.law true <;>
    simp_all

theorem completed_frame_flip (bus : Bus) (s : State) :
    ((run bus s frame).post != (run bus s frame).pre) =
      RouteDiagnostics.signature s.core.template.route (run bus s frame).receipt := by
  have hp := completed_frame_projects_sample bus s
  have ha := RouteDiagnostics.actual_write_flip_signature s.core.template.route s.core.template.q
    (receiptOf (RouteDiagnostics.bit s.core.template.q) s.core.law true)
  have hpre := congrArg Prod.fst hp
  have hr := congrArg (fun p : Bool × Bool × Bool => p.2.1) hp
  have hpost := congrArg (fun p : Bool × Bool × Bool => p.2.2) hp
  change (run bus s frame).pre = _ at hpre
  change (run bus s frame).receipt = _ at hr
  change (run bus s frame).post = _ at hpost
  rw [hpre,hr,hpost]
  exact ha

theorem completed_frame_updates_summaries (bus : Bus) (s : State) :
    let t := run bus s frame
    t.success = (if t.receipt then merge s.success (t.post != t.pre) else s.success) ∧
    t.failure = (if t.receipt then s.failure else merge s.failure (t.post != t.pre)) := by
  simp only [frame,run,advance]

theorem merge_preserves_consistent_evidence (old : Summary) (bit : Bool)
    (h : old = .unseen ∨ old = encode bit) :
    merge old bit = encode bit := by
  rcases h with rfl | rfl <;> cases bit <;> rfl

/-- A completed frame derives sound summaries from previously sound evidence.
The total-update identity alone does not claim the frame was affordable. -/
theorem completed_frame_preserves_summary_sound (bus : Bus) (s : State)
    (h : SoundSummary s.core.template.route s.success s.failure) :
    SoundSummary s.core.template.route (run bus s frame).success (run bus s frame).failure := by
  have hu := completed_frame_updates_summaries bus s
  have hf := completed_frame_flip bus s
  change _ ∧ _ at hu
  rw [hu.1,hu.2,hf]
  rcases h with ⟨hs,hh⟩
  cases hr : (run bus s frame).receipt <;>
    simp only [Bool.false_eq_true,ite_false,ite_true]
  · exact ⟨hs,Or.inr (merge_preserves_consistent_evidence _ _ hh)⟩
  · exact ⟨Or.inr (merge_preserves_consistent_evidence _ _ hs),hh⟩

theorem paid_frame_diagnosis_sound (bus : Bus) (s : State) (c : RouteDiagnostics.Class)
    (hp : allEnabled bus s frame)
    (hs : SoundSummary s.core.template.route s.success s.failure)
    (hc : diagnosis (run bus s frame) = some c) :
    Trace bus s frame (run bus s frame) ∧ c = RouteDiagnostics.routeClass s.core.template.route := by
  refine ⟨enabled_list_is_trace _ _ _ hp,?_⟩
  unfold diagnosis at hc
  split at hc
  · exact summary_classification_sound _ _ _
      (completed_frame_preserves_summary_sound bus s hs) c hc
  · contradiction

theorem absent_or_unknown_bus_blocks_commit (bus : Bus) (s : State)
    (hb : bus ≠ some true) :
    ¬ Enabled (run bus s [.sealWindow,.observe,.write,.postRead]) .commit := by
  simp [run,advance,Enabled,hb]

theorem seal_requires_completed_work (s : State)
    (h : s.phase ≠ .worked) : ¬ Enabled s .sealWindow := by
  simp [Enabled,h]

theorem paid_post_read_precedes_commit (s : State)
    (h : s.phase = .written) : ¬ Enabled s .commit := by
  simp [Enabled,h]

theorem floor_blocks_inspection_without_refund (s : State)
    (h : s.core.recipient = 1) :
    ¬ Enabled s .preRead ∧ ¬ Enabled s .arm ∧ ¬ Enabled s .sealWindow ∧
    ¬ Enabled s .postRead ∧ ¬ Enabled s .commit := by
  simp [Enabled,FeeEnabled,h]

theorem completed_two_frames_exhaust_lease (bus : Bus) (s : State) :
    (run bus (run bus s frame) frame).quota = .exhausted ∧
    ¬ Enabled (run bus (run bus s frame) frame) .rent := by
  cases h : s.quota <;> simp [frame,run,advance,nextQuota,Enabled,h]

theorem known_binding_break_discards_summaries (bus : Bus) (s : State) :
    (advance bus s .breakBinding).binding = false ∧
    (advance bus s .breakBinding).success = .unseen ∧
    (advance bus s .breakBinding).failure = .unseen ∧
    diagnosis (advance bus s .breakBinding) = none ∧
    energy (advance bus s .breakBinding) = energy s := by
  exact ⟨rfl,rfl,rfl,rfl,rfl⟩

/-- Admission copies the actual retained template, never revives an absent child. -/
def enter (old : FormedRecipientRoute.State) (reserved cells heads : Nat) : Option State :=
  if old.carrier = true ∧ old.routingInstalled = true ∧ old.childFuel = 0 then
    (SuccessorLearning.enter old reserved).bind fun core =>
      if core.template.q < 4 then
        some ⟨core,cells,heads,false,.absent,.two,false,false,false,
          .unseen,.unseen,false,false⟩
      else none
  else none

theorem unretained_grandchild_cannot_enter (old : FormedRecipientRoute.State)
    (reserved cells heads : Nat) (h : old.phase ≠ .retained) :
    enter old reserved cells heads = none := by
  simp [enter,SuccessorLearning.unretained_child_cannot_enter old reserved h]

/-- A typed retained boundary; the saved-distribution join is separately checked. -/
def boundary (route : Route) (q reserve : Nat) (law : Bool) : FormedRecipientRoute.State :=
  {FormedRecipientRoute.start route q law with
    actorFuel := 8, recipientFuel := reserve, childFuel := 0, source := 0,
    blanks := 0, routingParts := 0, carrier := true, routingInstalled := true,
    record := none, child := some ⟨route,q⟩, phase := .retained}

def initial (route : Route) (reserve : Nat) (law : Bool) : State :=
  ⟨⟨8,reserve,0,20,⟨route,0⟩,true,true,.ready,none,none,false,false,none,law,0,0⟩,
    8,1,false,.absent,.two,false,false,false,.unseen,.unseen,false,false⟩

def assembled (route : Route) (reserve : Nat) (law : Bool) : State :=
  advance (some true) (initial route reserve law) .assemble

def afterFirst (route : Route) : State := run (some true) (assembled route 25 true) frame

def throughWrite : List Event := [.rent,.sense,.preRead,.arm,.work,.sealWindow,.observe,.write]

theorem typed_boundary_admission (route : Route) (reserve : Nat) (law : Bool) :
    enter (boundary route 0 reserve law) 20 8 1 = some (initial route reserve law) := by
  rfl

theorem target_two_frames_are_paid :
    allEnabled (some true) (initial .target 25 true) ([.assemble]++frame++frame) := by decide

theorem target_retains_full_signature :
    (assembled .target 25 true).core.recipient = 23 ∧
    (afterFirst .target).core.recipient = 11 ∧
    (run (some true) (afterFirst .target) frame).core.recipient = 9 ∧
    diagnosis (run (some true) (afterFirst .target) frame) = some .actual ∧
    (run (some true) (afterFirst .target) frame).quota = .exhausted := by decide

theorem nonwriting_second_frame_stops_after_write (route : Route)
    (h : route = .closed ∨ route = .frozen) :
    allEnabled (some true) (initial route 25 true) ([.assemble]++frame++throughWrite) ∧
    diagnosis (afterFirst route) = some .unchanged ∧
    (run (some true) (afterFirst route) throughWrite).core.recipient = 1 ∧
    ¬ Enabled (run (some true) (afterFirst route) throughWrite) .postRead ∧
    diagnosis (run (some true) (afterFirst route) throughWrite) = some .unchanged := by
  rcases h with rfl | rfl <;> decide

theorem controlled_private_zero_success_identifies :
    allEnabled (some true) (initial .privateZero 15 false) ([.assemble]++frame) ∧
    diagnosis (run (some true) (assembled .privateZero 15 false) frame) = some .privateZero := by decide

end FormedRouteMonitor
