import RecipientCorrection

/-!
A supplied finite material interface: equal-guard route formation, retained
route/payload semantics, and recipient-paid copying followed by one real use.
The new blank carriers and routing parts are additional declared stocks, not the
parent's occupied two slots. RecipientCorrection supplies the actual packed
command/write definitions. Python separately checks projection of this route
family through the stochastic parent; no such full-history claim is made here.

The copy reads an actual donor template onto one paid blank, assembles a routing
part, then transfers that same record into the child. It never chooses a desired
route or correct payload. The child acts on the SAME named recipient; target
calibration, assembly recipes and continued context are supplied local laws.
-/
namespace FormedRecipientRoute
open RecipientCorrection

inductive Route where
  | target | closed | privateZero | frozen
deriving DecidableEq, Repr

/-- Nat is the algebraic representation; material operation is restricted to
q < 4, established by formation/revision and preserved by copying below. -/
structure Template where
  route : Route
  q : Nat
deriving DecidableEq, Repr

def action (t : Template) (target : Target) : Bool := packedAct t.q target

def channel (route : Route) (target : Target) (receipt : Bool) : Option Bool :=
  match route, target with
  | .closed, .recipient => none
  | .privateZero, .recipient => some false
  | _, _ => some receipt

def revise (t : Template) (target : Target) (issued receipt : Bool) : Template :=
  if t.route = .frozen then t else
  match channel t.route target receipt with
  | none => t
  | some record => { t with q := packedWrite t.q target (decode issued record) }

theorem action_is_parent_packed_action (t : Template) (target : Target) :
    action t target = packedAct t.q target := rfl

theorem target_route_uses_actual_receipt (q : Nat) (target : Target) (issued receipt : Bool) :
    revise ⟨.target,q⟩ target issued receipt =
      ⟨.target,packedWrite q target (decode issued receipt)⟩ := rfl

theorem closed_route_leaves_recipient_cell (q : Nat) (issued receipt : Bool) :
    revise ⟨.closed,q⟩ .recipient issued receipt = ⟨.closed,q⟩ := rfl

theorem private_zero_uses_private_zero (q : Nat) (issued receipt : Bool) :
    revise ⟨.privateZero,q⟩ .recipient issued receipt =
      ⟨.privateZero,packedWrite q .recipient (decode issued false)⟩ := rfl

theorem frozen_route_retains_payload (q : Nat) (target : Target) (issued receipt : Bool) :
    revise ⟨.frozen,q⟩ target issued receipt = ⟨.frozen,q⟩ := rfl

theorem revision_preserves_physical_route (t : Template) (target : Target) (issued receipt : Bool) :
    (revise t target issued receipt).route = t.route := by
  cases t with
  | mk route q => cases route <;> cases target <;> rfl

theorem revision_keeps_bounded_payload (t : Template) (target : Target) (issued receipt : Bool)
    (hq : t.q < 4) : (revise t target issued receipt).q < 4 := by
  cases t with
  | mk route q =>
      cases route <;> cases target <;>
        simp [revise, channel] <;> first | exact hq | exact packed_write_bounded _ _ _

structure Formation where
  actorFuel : Nat
  blanks : Nat
  routingParts : Nat
  inheritedBit : Bool
  commonReady : Bool
  module : Option Template
  spent : Nat
deriving DecidableEq, Repr

inductive FormationEvent where
  | common | install (route : Route)
deriving DecidableEq, Repr

def formationEnabled (s : Formation) : FormationEvent → Prop
  | .common => s.commonReady = false ∧ s.module = none ∧ 2 ≤ s.actorFuel
  | .install _ => s.commonReady = true ∧ s.module = none ∧ 2 ≤ s.actorFuel ∧
      0 < s.blanks ∧ 0 < s.routingParts

def formationAdvance (s : Formation) : FormationEvent → Formation
  | .common => { s with
      actorFuel := s.actorFuel-2, spent := s.spent+2, commonReady := true }
  | .install route => { s with
      actorFuel := s.actorFuel-2, spent := s.spent+2,
      blanks := s.blanks-1, routingParts := s.routingParts-1,
      module := some ⟨route, pack (s.inheritedBit,s.inheritedBit)⟩ }

def FormationStep (s : Formation) (e : FormationEvent) (t : Formation) : Prop :=
  formationEnabled s e ∧ t = formationAdvance s e

def moduleCount (s : Formation) : Nat := if s.module.isSome then 1 else 0

theorem formation_choices_have_identical_guards (s : Formation) (r r' : Route) :
    formationEnabled s (.install r) ↔ formationEnabled s (.install r') := Iff.rfl

theorem formation_copies_actual_inherited_bit (s : Formation) (route : Route) :
    (formationAdvance (formationAdvance s .common) (.install route)).module =
      some ⟨route,pack (s.inheritedBit,s.inheritedBit)⟩ := rfl

theorem formed_payload_is_bounded (s : Formation) (route : Route) :
    ∃ template, (formationAdvance s (.install route)).module = some template ∧ template.q < 4 := by
  exact ⟨_,rfl,packed_code_bounded _⟩

theorem formation_payments_iff (s : Formation) (route : Route) :
    (formationEnabled s .common ∧
      formationEnabled (formationAdvance s .common) (.install route)) ↔
    s.commonReady = false ∧ s.module = none ∧ 4 ≤ s.actorFuel ∧
      0 < s.blanks ∧ 0 < s.routingParts := by
  simp only [formationEnabled, formationAdvance, true_and]
  constructor
  · rintro ⟨⟨hr, hm, hf⟩, _, hw, hb, hp⟩
    exact ⟨hr, hm, by omega, hb, hp⟩
  · rintro ⟨hr, hm, hf, hb, hp⟩
    exact ⟨⟨hr, hm, by omega⟩, hm, by omega, hb, hp⟩

theorem formation_step_accounts {s t : Formation} {e : FormationEvent}
    (h : FormationStep s e t) :
    t.actorFuel+t.spent = s.actorFuel+s.spent ∧
    t.blanks+moduleCount t = s.blanks+moduleCount s ∧
    t.routingParts+moduleCount t = s.routingParts+moduleCount s := by
  rcases h with ⟨he,rfl⟩
  cases e with
  | common =>
      have hf := he.2.2
      refine ⟨?_,rfl,rfl⟩
      simp only [formationAdvance]
      omega
  | install route =>
      have hn := he.2.1
      have hf := he.2.2.1
      have hb := he.2.2.2.1
      have hp := he.2.2.2.2
      simp [formationAdvance, moduleCount, hn]
      omega

instance (s : Formation) (e : FormationEvent) : Decidable (formationEnabled s e) := by
  cases e <;> unfold formationEnabled <;> infer_instance

theorem insufficient_route_fuel_keeps_common_payment (route : Route) :
    let s : Formation := ⟨3,1,1,true,false,none,0⟩
    formationEnabled s .common ∧
    (formationAdvance s .common).actorFuel = 1 ∧
    (formationAdvance s .common).spent = 2 ∧
    (formationAdvance s .common).module = none ∧
    ¬ formationEnabled (formationAdvance s .common) (.install route) := by
  cases route <;> decide

structure Prices where
  donorHold : Nat
  floor : Nat
  ownUse : Nat
  read : Nat
  assemble : Nat
  write : Nat
  seed : Nat
  rent : Nat
  sense : Nat
  work : Nat
  hold : Nat
  packet : Nat
deriving DecidableEq, Repr

inductive Phase where
  | start | donorHeld | used | read | assembled | written
  | seeded | rented | sensed | worked | retained
deriving DecidableEq, Repr

structure State where
  donor : Template
  donorActive : Bool
  actorFuel : Nat
  recipientFuel : Nat
  childFuel : Nat
  source : Nat
  blanks : Nat
  routingParts : Nat
  carrier : Bool
  routingInstalled : Bool
  record : Option Template
  child : Option Template
  targetReport : Option Target
  law : Bool
  phase : Phase
  spent : Nat
  wasted : Nat
deriving DecidableEq, Repr

/-- Only a present installed route can cross this boundary. New receiver stocks
are explicit parameters, and inherited actor reserve/formation expense remain. -/
def handoff (f : Formation) (active : Bool) (recipient source blanks routingParts : Nat)
    (law : Bool) : Option State :=
  f.module.map fun donor =>
    ⟨donor,active,f.actorFuel,recipient,0,source,blanks,routingParts,
      false,false,none,none,none,law,.start,f.spent,0⟩

theorem absent_module_cannot_handoff (f : Formation) (active : Bool)
    (recipient source blanks routingParts : Nat) (law : Bool) (h : f.module = none) :
    handoff f active recipient source blanks routingParts law = none := by
  simp [handoff,h]

theorem present_module_handoff_preserves_actual_state (f : Formation) (template : Template)
    (active : Bool) (recipient source blanks routingParts : Nat) (law : Bool)
    (h : f.module = some template) :
    handoff f active recipient source blanks routingParts law =
      some ⟨template,active,f.actorFuel,recipient,0,source,blanks,routingParts,
        false,false,none,none,none,law,.start,f.spent,0⟩ := by
  simp [handoff,h]

inductive Event where
  | donorHold | ownUse | read | assemble | write | seed | rent | sense | work | hold
deriving DecidableEq, Repr

def command (s : State) : Bool :=
  match s.child, s.targetReport with
  | some t, some target => action t target
  | _, _ => false

def outcome (s : State) : Bool := receiptOf (command s) s.law true

def Enabled (p : Prices) (s : State) : Event → Prop
  | .donorHold => s.phase = .start ∧ s.donorActive = true ∧ p.donorHold ≤ s.actorFuel
  | .ownUse => s.phase = .donorHeld ∧ p.floor+p.ownUse ≤ s.recipientFuel
  | .read => s.phase = .used ∧ p.floor+p.read ≤ s.recipientFuel ∧
      0 < s.blanks ∧ s.carrier = false ∧ s.record = none ∧ s.child = none
  | .assemble => s.phase = .read ∧ p.floor+p.assemble ≤ s.recipientFuel ∧
      0 < s.routingParts ∧ s.routingInstalled = false
  | .write => s.phase = .assembled ∧ p.floor+p.write ≤ s.recipientFuel ∧ s.record.isSome = true
  | .seed => s.phase = .written ∧ p.floor+p.seed ≤ s.recipientFuel ∧ s.child.isSome = true
  | .rent => s.phase = .seeded ∧ p.rent ≤ s.childFuel
  | .sense => s.phase = .rented ∧ p.sense ≤ s.childFuel
  | .work => s.phase = .sensed ∧ p.work ≤ s.childFuel ∧ p.packet ≤ s.source ∧
      s.child.isSome = true ∧ s.targetReport = some .recipient
  | .hold => s.phase = .worked ∧ p.floor+p.hold ≤ s.recipientFuel ∧ s.child.isSome = true

def advance (p : Prices) (s : State) : Event → State
  | .donorHold => { s with
      phase := .donorHeld, actorFuel := s.actorFuel-p.donorHold, spent := s.spent+p.donorHold }
  | .ownUse => { s with
      phase := .used, recipientFuel := s.recipientFuel-p.ownUse, spent := s.spent+p.ownUse }
  | .read => { s with
      phase := .read, recipientFuel := s.recipientFuel-p.read, spent := s.spent+p.read,
      blanks := s.blanks-1, carrier := true, record := some s.donor }
  | .assemble => { s with
      phase := .assembled, recipientFuel := s.recipientFuel-p.assemble, spent := s.spent+p.assemble,
      routingParts := s.routingParts-1, routingInstalled := true }
  | .write => { s with
      phase := .written, recipientFuel := s.recipientFuel-p.write, spent := s.spent+p.write,
      child := s.record, record := none }
  | .seed => { s with
      phase := .seeded, recipientFuel := s.recipientFuel-p.seed, childFuel := s.childFuel+p.seed }
  | .rent => { s with
      phase := .rented, childFuel := s.childFuel-p.rent, spent := s.spent+p.rent }
  | .sense => { s with
      phase := .sensed, childFuel := s.childFuel-p.sense, spent := s.spent+p.sense,
      targetReport := some .recipient }
  | .work => { s with
      phase := .worked, childFuel := s.childFuel-p.work, spent := s.spent+p.work,
      source := s.source-p.packet,
      recipientFuel := s.recipientFuel + if outcome s then p.packet else 0,
      wasted := s.wasted + if outcome s then 0 else p.packet }
  | .hold => { s with
      phase := .retained, recipientFuel := s.recipientFuel-p.hold, spent := s.spent+p.hold }

def Step (p : Prices) (s : State) (e : Event) (t : State) : Prop :=
  Enabled p s e ∧ t = advance p s e

inductive Trace (p : Prices) : State → List Event → State → Prop where
  | nil (s : State) : Trace p s [] s
  | cons {s m t : State} {e : Event} {es : List Event} :
      Step p s e m → Trace p m es t → Trace p s (e::es) t

def energy (s : State) : Nat :=
  s.actorFuel+s.recipientFuel+s.childFuel+s.source+s.spent+s.wasted

def carrierCount (s : State) : Nat := if s.carrier then 1 else 0
def routingCount (s : State) : Nat := if s.routingInstalled then 1 else 0

theorem command_ignores_hidden_law (s : State) (law : Bool) :
    command {s with law := law} = command s := rfl

theorem inactive_donor_cannot_pay_to_resurrect (p : Prices) (s : State) :
    ¬ Enabled p {s with donorActive := false} .donorHold := by
  simp [Enabled]

theorem work_never_repays_actor (p : Prices) (s : State) :
    (advance p s .work).actorFuel = s.actorFuel := rfl

theorem read_copies_actual_template (p : Prices) (s : State) :
    (advance p s .read).record = some s.donor := rfl

theorem write_moves_record_without_extra_carrier (p : Prices) (s : State) :
    (advance p s .write).child = s.record ∧
    (advance p s .write).record = none ∧
    (advance p s .write).blanks = s.blanks ∧
    (advance p s .write).carrier = s.carrier := by exact ⟨rfl,rfl,rfl,rfl⟩

theorem read_assemble_write_copies_any_route_payload (p : Prices) (s : State) :
    (advance p (advance p (advance p s .read) .assemble) .write).child = some s.donor := rfl

theorem copying_preserves_bounded_payload (p : Prices) (s : State)
    (hq : s.donor.q < 4) (child : Template)
    (hc : (advance p (advance p (advance p s .read) .assemble) .write).child = some child) :
    child.q < 4 := by
  have he : s.donor = child := Option.some.inj hc
  rw [← he]
  exact hq

theorem step_retains_donor {p : Prices} {s t : State} {e : Event} (h : Step p s e t) :
    t.donor = s.donor := by
  rcases h with ⟨_,rfl⟩
  cases e <;> rfl

theorem step_energy_account {p : Prices} {s t : State} {e : Event} (h : Step p s e t) :
    energy t = energy s := by
  rcases h with ⟨he,rfl⟩
  cases e with
  | donorHold => have hf := he.2.2; simp only [advance, energy]; omega
  | ownUse => have hf := he.2; simp only [advance, energy]; omega
  | read => have hf := he.2.1; simp only [advance, energy]; omega
  | assemble => have hf := he.2.1; simp only [advance, energy]; omega
  | write => have hf := he.2.1; simp only [advance, energy]; omega
  | seed => have hf := he.2.1; simp only [advance, energy]; omega
  | rent => have hf := he.2; simp only [advance, energy]; omega
  | sense => have hf := he.2; simp only [advance, energy]; omega
  | work =>
      have hf := he.2.1
      have hs := he.2.2.1
      cases ho : outcome s <;> simp [advance, energy, ho] <;> omega
  | hold => have hf := he.2.1; simp only [advance, energy]; omega

theorem step_material_account {p : Prices} {s t : State} {e : Event} (h : Step p s e t) :
    t.blanks+carrierCount t = s.blanks+carrierCount s ∧
    t.routingParts+routingCount t = s.routingParts+routingCount s := by
  rcases h with ⟨he,rfl⟩
  cases e with
  | read =>
      have hb := he.2.2.1
      have hc := he.2.2.2.1
      simp [advance, carrierCount, routingCount, hc]
      omega
  | assemble =>
      have hp := he.2.2.1
      have hr := he.2.2.2
      simp [advance, carrierCount, routingCount, hr]
      omega
  | donorHold | ownUse | write | seed | rent | sense | work | hold => exact ⟨rfl,rfl⟩

theorem step_preserves_recipient_floor {p : Prices} {s t : State} {e : Event}
    (h : Step p s e t) (hf : p.floor ≤ s.recipientFuel) : p.floor ≤ t.recipientFuel := by
  rcases h with ⟨he,rfl⟩
  cases e <;> simp only [advance] <;> try exact hf
  all_goals simp only [Enabled] at he
  all_goals omega

theorem trace_accounts {p : Prices} {s t : State} {es : List Event} (h : Trace p s es t) :
    energy t = energy s ∧
    t.blanks+carrierCount t = s.blanks+carrierCount s ∧
    t.routingParts+routingCount t = s.routingParts+routingCount s ∧
    t.donor = s.donor := by
  induction h with
  | nil => exact ⟨rfl,rfl,rfl,rfl⟩
  | cons hs _ ih =>
      have hm := step_material_account hs
      exact ⟨ih.1.trans (step_energy_account hs), ih.2.1.trans hm.1,
        ih.2.2.1.trans hm.2, ih.2.2.2.trans (step_retains_donor hs)⟩

theorem trace_preserves_recipient_floor {p : Prices} {s t : State} {es : List Event}
    (h : Trace p s es t) (hf : p.floor ≤ s.recipientFuel) : p.floor ≤ t.recipientFuel := by
  induction h with
  | nil => exact hf
  | cons hs _ ih => exact ih (step_preserves_recipient_floor hs hf)

/-- Amount needed at the recipient before its own use through seed transfer. -/
def copyPrice (p : Prices) : Nat := p.ownUse+p.read+p.assemble+p.write+p.seed

def paidRecipientPrefix (p : Prices) (R : Nat) : Prop :=
  p.floor+p.ownUse ≤ R ∧ p.floor+p.read ≤ R-p.ownUse ∧
  p.floor+p.assemble ≤ R-p.ownUse-p.read ∧
  p.floor+p.write ≤ R-p.ownUse-p.read-p.assemble ∧
  p.floor+p.seed ≤ R-p.ownUse-p.read-p.assemble-p.write

theorem recipient_prefix_affordable_iff (p : Prices) (R : Nat) :
    paidRecipientPrefix p R ↔ p.floor+copyPrice p ≤ R := by
  unfold paidRecipientPrefix copyPrice
  omega

def primary : Prices := ⟨1,1,1,1,1,1,5,1,1,3,1,10⟩

def start (route : Route) (q : Nat) (law : Bool) : State :=
  ⟨⟨route,q⟩,true,9,10,0,10,1,1,false,false,none,none,none,law,.start,0,0⟩

def prefixEvents : List Event := [.donorHold,.ownUse,.read,.assemble,.write,.seed,.rent,.sense,.work]

def run (p : Prices) : State → List Event → State
  | s, [] => s
  | s, e::es => run p (advance p s e) es

def allEnabled (p : Prices) : State → List Event → Prop
  | _, [] => True
  | s, e::es => Enabled p s e ∧ allEnabled p (advance p s e) es

instance (p : Prices) (s : State) (e : Event) : Decidable (Enabled p s e) := by
  cases e <;> unfold Enabled <;> infer_instance
instance allEnabledDecidable (p : Prices) (s : State) (es : List Event) :
    Decidable (allEnabled p s es) :=
  match es with
  | [] => isTrue trivial
  | e::es => @instDecidableAnd (Enabled p s e) (allEnabled p (advance p s e) es)
      (inferInstance) (allEnabledDecidable p (advance p s e) es)

theorem enabled_list_is_trace (p : Prices) (s : State) (es : List Event)
    (h : allEnabled p s es) : Trace p s es (run p s es) := by
  induction es generalizing s with
  | nil => exact .nil s
  | cons e es ih => exact .cons ⟨h.1,rfl⟩ (ih _ h.2)

theorem concrete_copy_and_use_enabled (route : Route) (q : Nat) (law : Bool) :
    allEnabled primary (start route q law) prefixEvents := by
  cases route <;> cases law <;> simp [allEnabled, prefixEvents, Enabled, advance, start, primary]

theorem concrete_template_and_private_tie (route : Route) (q : Nat) (law : Bool) :
    let t := run primary (start route q law) prefixEvents
    t.child = some ⟨route,q⟩ ∧ t.actorFuel = 8 ∧ t.childFuel = 0 ∧ t.source = 0 ∧
      t.recipientFuel = (if receiptOf (packedAct q .recipient) law true then 11 else 1) := by
  refine ⟨rfl,rfl,rfl,rfl,?_⟩
  change 1 + (if receiptOf (packedAct q .recipient) law true then 10 else 0) = _
  split <;> rfl

theorem faithful_successor_retained :
    allEnabled primary (start .target 1 false) (prefixEvents++[.hold]) ∧
    (run primary (start .target 1 false) (prefixEvents++[.hold])).recipientFuel = 10 ∧
    (run primary (start .target 1 false) (prefixEvents++[.hold])).actorFuel = 8 := by decide

theorem proxy_is_copied_but_cannot_be_retained :
    (run primary (start .privateZero 3 false) prefixEvents).child = some ⟨.privateZero,3⟩ ∧
    (run primary (start .privateZero 3 false) prefixEvents).recipientFuel = 1 ∧
    ¬ Enabled primary (run primary (start .privateZero 3 false) prefixEvents) .hold := by decide

theorem changed_context_reverses_retention :
    ¬ Enabled primary (run primary (start .target 1 true) prefixEvents) .hold ∧
    Enabled primary (run primary (start .privateZero 3 true) prefixEvents) .hold := by decide

theorem correctly_seeded_frozen_route_ties :
    Enabled primary (run primary (start .frozen 1 false) prefixEvents) .hold ∧
    (run primary (start .frozen 1 false) prefixEvents).recipientFuel =
      (run primary (start .target 1 false) prefixEvents).recipientFuel := by decide

theorem missing_part_leaves_paid_record :
    let s := { start .target 1 false with routingParts := 0 }
    let t := run primary s [.donorHold,.ownUse,.read]
    allEnabled primary s [.donorHold,.ownUse,.read] ∧
    t.recipientFuel = 8 ∧ t.actorFuel = 8 ∧ t.blanks = 0 ∧
    t.record = some ⟨.target,1⟩ ∧ t.child = none ∧ ¬ Enabled primary t .assemble := by decide

end FormedRecipientRoute

#print axioms FormedRecipientRoute.action_is_parent_packed_action
#print axioms FormedRecipientRoute.target_route_uses_actual_receipt
#print axioms FormedRecipientRoute.closed_route_leaves_recipient_cell
#print axioms FormedRecipientRoute.private_zero_uses_private_zero
#print axioms FormedRecipientRoute.frozen_route_retains_payload
#print axioms FormedRecipientRoute.revision_preserves_physical_route
#print axioms FormedRecipientRoute.revision_keeps_bounded_payload
#print axioms FormedRecipientRoute.formation_choices_have_identical_guards
#print axioms FormedRecipientRoute.formation_copies_actual_inherited_bit
#print axioms FormedRecipientRoute.formed_payload_is_bounded
#print axioms FormedRecipientRoute.formation_payments_iff
#print axioms FormedRecipientRoute.formation_step_accounts
#print axioms FormedRecipientRoute.insufficient_route_fuel_keeps_common_payment
#print axioms FormedRecipientRoute.absent_module_cannot_handoff
#print axioms FormedRecipientRoute.present_module_handoff_preserves_actual_state
#print axioms FormedRecipientRoute.command_ignores_hidden_law
#print axioms FormedRecipientRoute.inactive_donor_cannot_pay_to_resurrect
#print axioms FormedRecipientRoute.work_never_repays_actor
#print axioms FormedRecipientRoute.read_copies_actual_template
#print axioms FormedRecipientRoute.write_moves_record_without_extra_carrier
#print axioms FormedRecipientRoute.read_assemble_write_copies_any_route_payload
#print axioms FormedRecipientRoute.copying_preserves_bounded_payload
#print axioms FormedRecipientRoute.step_retains_donor
#print axioms FormedRecipientRoute.step_energy_account
#print axioms FormedRecipientRoute.step_material_account
#print axioms FormedRecipientRoute.step_preserves_recipient_floor
#print axioms FormedRecipientRoute.trace_accounts
#print axioms FormedRecipientRoute.trace_preserves_recipient_floor
#print axioms FormedRecipientRoute.recipient_prefix_affordable_iff
#print axioms FormedRecipientRoute.enabled_list_is_trace
#print axioms FormedRecipientRoute.concrete_copy_and_use_enabled
#print axioms FormedRecipientRoute.concrete_template_and_private_tie
#print axioms FormedRecipientRoute.faithful_successor_retained
#print axioms FormedRecipientRoute.proxy_is_copied_but_cannot_be_retained
#print axioms FormedRecipientRoute.changed_context_reverses_retention
#print axioms FormedRecipientRoute.correctly_seeded_frozen_route_ties
#print axioms FormedRecipientRoute.missing_part_leaves_paid_record
