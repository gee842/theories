import FormedRecipientRoute

/- A finite paid learning continuation of an actually retained copied template.
All new source and receiver inventories are explicit reserved inputs. The route
algorithm stays fixed; the acquired target-action table is revised and copied. -/
namespace SuccessorLearning
open RecipientCorrection

abbrev Template := FormedRecipientRoute.Template
abbrev Route := FormedRecipientRoute.Route

inductive Op where
  | rent | sense | work | observe | write
deriving DecidableEq, Repr

inductive Phase where
  | ready | rented | sensed | worked | observed
deriving DecidableEq, Repr

structure Prices where
  floor : Nat
  rent : Nat
  sense : Nat
  work : Nat
  observe : Nat
  write : Nat
  packet : Nat
deriving DecidableEq, Repr

def primary : Prices := ⟨1,1,1,3,1,1,10⟩

def cost (p : Prices) : Op → Nat
  | .rent => p.rent
  | .sense => p.sense
  | .work => p.work
  | .observe => p.observe
  | .write => p.write

def before : Op → Phase
  | .rent => .ready
  | .sense => .rented
  | .work => .sensed
  | .observe => .worked
  | .write => .observed

structure State where
  originalActor : Nat
  recipient : Nat
  childFuel : Nat
  source : Nat
  template : Template
  carrier : Bool
  routing : Bool
  phase : Phase
  funded : Option Op
  targetReport : Option Target
  issued : Bool
  captured : Bool
  record : Option Bool
  law : Bool
  spent : Nat
  wasted : Nat
deriving DecidableEq, Repr

def energy (s : State) : Nat :=
  s.originalActor+s.recipient+s.childFuel+s.source+s.spent+s.wasted

/-- `reserved` was separately present in the extended experiment. Entry neither
creates fuel nor grants a new template: only an actually retained child enters. -/
def enter (old : FormedRecipientRoute.State) (reserved : Nat) : Option State :=
  if old.phase = .retained then old.child.map fun template =>
    ⟨old.actorFuel,old.recipientFuel,old.childFuel,old.source+reserved,
      template,old.carrier,old.routingInstalled,.ready,none,none,false,false,none,
      old.law,old.spent,old.wasted⟩
  else none

theorem retained_entry_carries_actual_child (old : FormedRecipientRoute.State)
    (reserved : Nat) (template : Template) (hp : old.phase = .retained)
    (hc : old.child = some template) :
    enter old reserved = some
      ⟨old.actorFuel,old.recipientFuel,old.childFuel,old.source+reserved,
        template,old.carrier,old.routingInstalled,.ready,none,none,false,false,none,
        old.law,old.spent,old.wasted⟩ := by
  simp [enter,hp,hc]

theorem entry_accounts_for_reserved_source (old : FormedRecipientRoute.State)
    (reserved : Nat) (s : State) (h : enter old reserved = some s) :
    energy s = FormedRecipientRoute.energy old + reserved := by
  unfold enter at h
  split at h
  · cases hc : old.child with
    | none => simp [hc] at h
    | some t =>
      simp only [hc,Option.map_some,Option.some.injEq] at h
      rw [← h]
      simp only [energy,FormedRecipientRoute.energy]
      omega
  · contradiction

theorem unretained_child_cannot_enter (old : FormedRecipientRoute.State)
    (reserved : Nat) (h : old.phase ≠ .retained) : enter old reserved = none := by
  simp [enter,h]

def command (s : State) : Bool :=
  match s.targetReport with
  | some target => FormedRecipientRoute.action s.template target
  | none => false

def outcome (s : State) : Bool := receiptOf (command s) s.law true

inductive Event where
  | fund (op : Op)
  | perform (op : Op)
  | reverse
deriving DecidableEq, Repr

def specialGuard (p : Prices) (s : State) : Op → Prop
  | .work => p.packet ≤ s.source ∧ s.targetReport = some .recipient
  | .write => s.record.isSome = true
  | _ => True

def Enabled (p : Prices) (s : State) : Event → Prop
  | .fund op => s.carrier = true ∧ s.routing = true ∧ s.phase = before op ∧
      s.funded = none ∧ s.childFuel = 0 ∧ p.floor+cost p op ≤ s.recipient
  | .perform op => s.phase = before op ∧ s.funded = some op ∧
      cost p op ≤ s.childFuel ∧ specialGuard p s op
  | .reverse => s.phase = .ready ∧ s.funded = none

def revised (s : State) : Template :=
  match s.record with
  | none => s.template
  | some receipt => FormedRecipientRoute.revise s.template .recipient s.issued receipt

def advance (p : Prices) (s : State) : Event → State
  | .fund op => {s with
      recipient := s.recipient-cost p op,
      childFuel := s.childFuel+cost p op, funded := some op}
  | .perform op =>
    let paid := {s with
      childFuel := s.childFuel-cost p op,
      spent := s.spent+cost p op, funded := none}
    match op with
    | .rent => {paid with phase := .rented, targetReport := none, record := none}
    | .sense => {paid with phase := .sensed, targetReport := some .recipient}
    | .work => {paid with
        phase := .worked, issued := command s, captured := outcome s,
        source := s.source-p.packet,
        recipient := s.recipient + if outcome s then p.packet else 0,
        wasted := s.wasted + if outcome s then 0 else p.packet}
    | .observe => {paid with phase := .observed, record := some s.captured}
    | .write => {paid with phase := .ready, template := revised s}
  | .reverse => {s with law := !s.law}

def Step (p : Prices) (s : State) (e : Event) (t : State) : Prop :=
  Enabled p s e ∧ t = advance p s e

inductive Trace (p : Prices) : State → List Event → State → Prop where
  | nil (s : State) : Trace p s [] s
  | cons {s m t : State} {e : Event} {es : List Event} :
      Step p s e m → Trace p m es t → Trace p s (e::es) t

theorem command_ignores_law_and_funding (s : State) (law : Bool) (reserve : Nat) :
    command {s with law := law, recipient := reserve} = command s := rfl

theorem funding_is_transfer_not_expenditure (p : Prices) (s : State) (op : Op) :
    (advance p s (.fund op)).spent = s.spent ∧
    (advance p s (.fund op)).childFuel = s.childFuel+cost p op := ⟨rfl,rfl⟩

theorem reversal_preserves_acquired_state (p : Prices) (s : State) :
    (advance p s .reverse).template = s.template ∧
    (advance p s .reverse).recipient = s.recipient ∧
    (advance p s .reverse).childFuel = s.childFuel ∧
    (advance p s .reverse).source = s.source := ⟨rfl,rfl,rfl,rfl⟩

theorem paid_write_uses_acquired_record (p : Prices) (s : State) (receipt : Bool)
    (h : s.record = some receipt) :
    (advance p s (.perform .write)).template =
      FormedRecipientRoute.revise s.template .recipient s.issued receipt := by
  simp [advance,revised,h]

theorem truthful_record_corrects_only_recipient (p : Prices) (s : State)
    (ht : s.template.route = .target)
    (hr : s.record = some (receiptOf s.issued s.law true)) :
    FormedRecipientRoute.action (advance p s (.perform .write)).template .recipient = s.law ∧
    FormedRecipientRoute.action (advance p s (.perform .write)).template .actor =
      FormedRecipientRoute.action s.template .actor := by
  rw [paid_write_uses_acquired_record p s _ hr]
  have he : s.template = ⟨.target,s.template.q⟩ := by
    cases hm : s.template with
    | mk route q =>
      rw [hm] at ht
      cases ht
      rfl
  rw [he,FormedRecipientRoute.target_route_uses_actual_receipt]
  exact recipient_feedback_repairs_only_recipient _ _ _

theorem revision_keeps_fixed_route (s : State) : (revised s).route = s.template.route := by
  cases hr : s.record with
  | none => simp [revised,hr]
  | some receipt =>
    simp only [revised,hr]
    exact FormedRecipientRoute.revision_preserves_physical_route _ _ _ _

theorem step_preserves_actor_route_and_carrier {p : Prices} {s t : State} {e : Event}
    (h : Step p s e t) :
    t.originalActor = s.originalActor ∧ t.template.route = s.template.route ∧
    t.carrier = s.carrier ∧ t.routing = s.routing := by
  rcases h with ⟨_,rfl⟩
  cases e with
  | fund op => exact ⟨rfl,rfl,rfl,rfl⟩
  | reverse => exact ⟨rfl,rfl,rfl,rfl⟩
  | perform op =>
    cases op <;> try exact ⟨rfl,rfl,rfl,rfl⟩
    exact ⟨rfl,revision_keeps_fixed_route s,rfl,rfl⟩

theorem step_preserves_payload_bound {p : Prices} {s t : State} {e : Event}
    (h : Step p s e t) (hq : s.template.q < 4) : t.template.q < 4 := by
  rcases h with ⟨_,rfl⟩
  cases e with
  | fund op => exact hq
  | reverse => exact hq
  | perform op =>
    cases op <;> try exact hq
    change (revised s).q < 4
    cases hr : s.record with
    | none => simpa [revised,hr] using hq
    | some receipt =>
      simp only [revised,hr]
      exact FormedRecipientRoute.revision_keeps_bounded_payload _ _ _ _ hq

theorem step_energy_account {p : Prices} {s t : State} {e : Event}
    (h : Step p s e t) : energy t = energy s := by
  rcases h with ⟨he,rfl⟩
  cases e with
  | fund op =>
    have hf := he.2.2.2.2.2
    simp only [advance,energy]
    omega
  | reverse => rfl
  | perform op =>
    have hf := he.2.2.1
    cases op with
    | rent | sense | observe | write => simp only [advance,energy]; omega
    | work =>
      have hs := he.2.2.2.1
      cases ho : outcome s <;> simp [advance,energy,ho] <;> omega

theorem step_preserves_recipient_floor {p : Prices} {s t : State} {e : Event}
    (h : Step p s e t) (hr : p.floor ≤ s.recipient) : p.floor ≤ t.recipient := by
  rcases h with ⟨he,rfl⟩
  cases e with
  | fund op => have hf := he.2.2.2.2.2; simp only [advance]; omega
  | reverse => exact hr
  | perform op =>
    cases op <;> simp only [advance] <;> try exact hr
    omega

theorem trace_accounts {p : Prices} {s t : State} {es : List Event}
    (h : Trace p s es t) :
    energy t = energy s ∧ t.originalActor = s.originalActor ∧
    t.template.route = s.template.route ∧ t.carrier = s.carrier ∧ t.routing = s.routing := by
  induction h with
  | nil => exact ⟨rfl,rfl,rfl,rfl,rfl⟩
  | cons hs _ ih =>
    have hm := step_preserves_actor_route_and_carrier hs
    exact ⟨ih.1.trans (step_energy_account hs),ih.2.1.trans hm.1,
      ih.2.2.1.trans hm.2.1,ih.2.2.2.1.trans hm.2.2.1,ih.2.2.2.2.trans hm.2.2.2⟩

theorem trace_preserves_recipient_floor {p : Prices} {s t : State} {es : List Event}
    (h : Trace p s es t) (hr : p.floor ≤ s.recipient) : p.floor ≤ t.recipient := by
  induction h with
  | nil => exact hr
  | cons hs _ ih => exact ih (step_preserves_recipient_floor hs hr)

theorem trace_preserves_payload_bound {p : Prices} {s t : State} {es : List Event}
    (h : Trace p s es t) (hq : s.template.q < 4) : t.template.q < 4 := by
  induction h with
  | nil => exact hq
  | cons hs _ ih => exact ih (step_preserves_payload_bound hs hq)

def run (p : Prices) : State → List Event → State
  | s, [] => s
  | s, e::es => run p (advance p s e) es

def allEnabled (p : Prices) : State → List Event → Prop
  | _, [] => True
  | s, e::es => Enabled p s e ∧ allEnabled p (advance p s e) es

instance (p : Prices) (s : State) (e : Event) : Decidable (Enabled p s e) := by
  cases e with
  | fund op => unfold Enabled; infer_instance
  | reverse => unfold Enabled; infer_instance
  | perform op => cases op <;> unfold Enabled specialGuard <;> infer_instance

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

def trial : List Event :=
  [.fund .rent,.perform .rent,.fund .sense,.perform .sense,.fund .work,.perform .work,
   .fund .observe,.perform .observe,.fund .write,.perform .write]

def oldStart : FormedRecipientRoute.State := FormedRecipientRoute.start .target 1 false
def oldEvents : List FormedRecipientRoute.Event := FormedRecipientRoute.prefixEvents++[.hold]
def oldRetained : FormedRecipientRoute.State :=
  FormedRecipientRoute.run FormedRecipientRoute.primary oldStart oldEvents

def initial : State :=
  ⟨8,10,0,50,⟨.target,1⟩,true,true,.ready,none,none,false,false,none,false,11,0⟩

theorem actual_old_copy_enters_learning :
    FormedRecipientRoute.allEnabled FormedRecipientRoute.primary oldStart oldEvents ∧
    enter oldRetained 50 = some initial := by decide

def learningEvents : List Event := trial++trial++[.reverse]++trial++trial
def afterWarmup : State := run primary initial (trial++trial)
def afterFailure : State := run primary (advance primary afterWarmup .reverse) trial
def learned : State := run primary initial learningEvents

theorem learning_events_are_enabled : allEnabled primary initial learningEvents := by decide

theorem own_consequence_changes_paid_action :
    afterWarmup.recipient = 16 ∧ afterWarmup.template = ⟨.target,1⟩ ∧
    afterFailure.recipient = 9 ∧ afterFailure.issued = false ∧
    afterFailure.captured = false ∧ afterFailure.record = some false ∧
    afterFailure.template = ⟨.target,3⟩ ∧
    learned.issued = true ∧ learned.captured = true ∧ learned.recipient = 12 ∧
    learned.originalActor = 8 ∧ learned.childFuel = 0 ∧ learned.source = 10 ∧
    learned.spent = 39 ∧ learned.wasted = 10 := by decide

theorem unchanged_code_blocks_corrected_capture :
    let clamped := {afterFailure with template := ⟨.target,1⟩}
    allEnabled primary clamped trial ∧
    (run primary clamped trial).captured = false ∧
    (run primary clamped trial).recipient = 2 := by decide

theorem frozen_route_ties_under_stable_law :
    let frozen := {initial with template := ⟨.frozen,1⟩}
    allEnabled primary frozen (trial++trial) ∧
    (run primary frozen (trial++trial)).recipient = afterWarmup.recipient ∧
    (run primary frozen (trial++trial)).template.q = afterWarmup.template.q := by decide

theorem frozen_route_fails_after_change :
    let frozen := {initial with template := ⟨.frozen,1⟩}
    allEnabled primary frozen learningEvents ∧
    (run primary frozen learningEvents).captured = false ∧
    (run primary frozen learningEvents).recipient = 2 ∧
    (run primary frozen learningEvents).template = ⟨.frozen,1⟩ := by decide

/- Exact affordability after n already completed productive warm-ups. This
separate arithmetic interface does not infer that those warm-ups occurred. -/
def prefixAffordable (floor reserve : Nat) : List Nat → Prop
  | [] => floor ≤ reserve
  | c::cs => floor+c ≤ reserve ∧ prefixAffordable floor (reserve-c) cs

theorem prefix_affordable_iff (floor reserve : Nat) (costs : List Nat) :
    prefixAffordable floor reserve costs ↔ floor+costs.sum ≤ reserve := by
  induction costs generalizing reserve with
  | nil => simp [prefixAffordable]
  | cons c cs ih => simp only [prefixAffordable,List.sum_cons,ih]; omega

def failedThenCorrectedStartup : List Nat := [1,1,3,1,1,1,1,3]

theorem corrective_use_threshold (B n : Nat) :
    prefixAffordable 1 (B+3*n) failedThenCorrectedStartup ↔ 13 ≤ B+3*n := by
  rw [prefix_affordable_iff]
  rfl

def recopyPrefix : List Nat := [1,1,1,1,1,5]

theorem revised_copy_threshold (B n : Nat) (h : 4 ≤ B+3*n) :
    prefixAffordable 1 (B+3*n-4) recopyPrefix ↔ 15 ≤ B+3*n := by
  rw [prefix_affordable_iff]
  simp only [recopyPrefix,List.sum_cons,List.sum_nil]
  omega

theorem two_warmups_minimal_for_ten (n : Nat) :
    (15 ≤ 10+3*n) ↔ 2 ≤ n := by omega

theorem unbuffered_actual_stock_cannot_use_correction :
    ¬ prefixAffordable 1 10 failedThenCorrectedStartup := by
  rw [prefix_affordable_iff]
  decide

/- Explicit recipient transfer funds the learning child as the new donor. The
original actor remains a separate account. A new blank/routing bundle and the
reserved packet enter the existing, unchanged copy law. -/
def FundDonor (p : FormedRecipientRoute.Prices) (s : State) : Prop :=
  s.phase = .ready ∧ s.funded = none ∧ s.childFuel = 0 ∧
  s.carrier = true ∧ s.routing = true ∧ p.floor+p.donorHold ≤ s.recipient

instance (p : FormedRecipientRoute.Prices) (s : State) : Decidable (FundDonor p s) := by
  unfold FundDonor
  infer_instance

def copyStart (p : FormedRecipientRoute.Prices) (s : State)
    (blanks routingParts : Nat) : FormedRecipientRoute.State :=
  ⟨s.template,true,s.childFuel+p.donorHold,s.recipient-p.donorHold,0,s.source,
    blanks,routingParts,false,false,none,none,none,s.law,.start,s.spent,s.wasted⟩

theorem funded_copy_start_preserves_accounts (p : FormedRecipientRoute.Prices)
    (s : State) (blanks routingParts : Nat) (h : FundDonor p s) :
    FormedRecipientRoute.energy (copyStart p s blanks routingParts)+s.originalActor = energy s ∧
    (copyStart p s blanks routingParts).donor = s.template ∧
    (copyStart p s blanks routingParts).spent = s.spent := by
  have hr := h.2.2.2.2.2
  refine ⟨?_,rfl,rfl⟩
  simp only [FormedRecipientRoute.energy,copyStart,energy]
  omega

theorem recopy_reads_childs_current_template (p : FormedRecipientRoute.Prices)
    (s : State) (blanks routingParts : Nat) :
    (FormedRecipientRoute.advance p
      (FormedRecipientRoute.advance p
        (FormedRecipientRoute.advance p (copyStart p s blanks routingParts) .read)
        .assemble) .write).child = some s.template := rfl

def grandStart : FormedRecipientRoute.State :=
  copyStart FormedRecipientRoute.primary learned 1 1
def grandEvents : List FormedRecipientRoute.Event := FormedRecipientRoute.prefixEvents++[.hold]
def grandFinal : FormedRecipientRoute.State :=
  FormedRecipientRoute.run FormedRecipientRoute.primary grandStart grandEvents

theorem revised_grandchild_is_paid_and_productive :
    FundDonor FormedRecipientRoute.primary learned ∧
    FormedRecipientRoute.allEnabled FormedRecipientRoute.primary grandStart grandEvents ∧
    grandFinal.child = some ⟨.target,3⟩ ∧ grandFinal.recipientFuel = 11 ∧
    grandFinal.actorFuel = 0 ∧ grandFinal.childFuel = 0 ∧ grandFinal.source = 0 ∧
    grandFinal.spent = 50 ∧ grandFinal.wasted = 10 := by decide

theorem joined_learning_and_recopy_trace :
    FormedRecipientRoute.Trace FormedRecipientRoute.primary oldStart oldEvents oldRetained ∧
    enter oldRetained 50 = some initial ∧
    Trace primary initial learningEvents learned ∧
    FundDonor FormedRecipientRoute.primary learned ∧
    FormedRecipientRoute.Trace FormedRecipientRoute.primary grandStart grandEvents grandFinal := by
  exact ⟨FormedRecipientRoute.enabled_list_is_trace _ _ _ actual_old_copy_enters_learning.1,
    actual_old_copy_enters_learning.2,
    enabled_list_is_trace _ _ _ learning_events_are_enabled,
    revised_grandchild_is_paid_and_productive.1,
    FormedRecipientRoute.enabled_list_is_trace _ _ _ revised_grandchild_is_paid_and_productive.2.1⟩

theorem old_template_clamp_loses_grandchild_return :
    let clamped := {grandStart with donor := ⟨.target,1⟩}
    FormedRecipientRoute.allEnabled FormedRecipientRoute.primary clamped grandEvents ∧
    (FormedRecipientRoute.run FormedRecipientRoute.primary clamped grandEvents).recipientFuel = 1 ∧
    (FormedRecipientRoute.run FormedRecipientRoute.primary clamped grandEvents).wasted = 20 := by decide

theorem complete_local_ledger :
    FormedRecipientRoute.energy oldRetained+50 = 79 ∧
    energy learned = 79 ∧
    FormedRecipientRoute.energy grandFinal+learned.originalActor = 79 ∧
    8+11+50+10 = 79 := by decide

theorem join_with_earlier_account (earlier : Nat)
    (h : earlier+FormedRecipientRoute.energy oldRetained = 161) :
    earlier+FormedRecipientRoute.energy grandFinal+learned.originalActor = 211 := by
  have ha := complete_local_ledger.1
  have hb := complete_local_ledger.2.2.1
  omega

end SuccessorLearning

#print axioms SuccessorLearning.retained_entry_carries_actual_child
#print axioms SuccessorLearning.entry_accounts_for_reserved_source
#print axioms SuccessorLearning.unretained_child_cannot_enter
#print axioms SuccessorLearning.command_ignores_law_and_funding
#print axioms SuccessorLearning.funding_is_transfer_not_expenditure
#print axioms SuccessorLearning.reversal_preserves_acquired_state
#print axioms SuccessorLearning.paid_write_uses_acquired_record
#print axioms SuccessorLearning.truthful_record_corrects_only_recipient
#print axioms SuccessorLearning.revision_keeps_fixed_route
#print axioms SuccessorLearning.step_preserves_actor_route_and_carrier
#print axioms SuccessorLearning.step_preserves_payload_bound
#print axioms SuccessorLearning.step_energy_account
#print axioms SuccessorLearning.step_preserves_recipient_floor
#print axioms SuccessorLearning.trace_accounts
#print axioms SuccessorLearning.trace_preserves_recipient_floor
#print axioms SuccessorLearning.trace_preserves_payload_bound
#print axioms SuccessorLearning.enabled_list_is_trace
#print axioms SuccessorLearning.actual_old_copy_enters_learning
#print axioms SuccessorLearning.learning_events_are_enabled
#print axioms SuccessorLearning.own_consequence_changes_paid_action
#print axioms SuccessorLearning.unchanged_code_blocks_corrected_capture
#print axioms SuccessorLearning.frozen_route_ties_under_stable_law
#print axioms SuccessorLearning.frozen_route_fails_after_change
#print axioms SuccessorLearning.prefix_affordable_iff
#print axioms SuccessorLearning.corrective_use_threshold
#print axioms SuccessorLearning.revised_copy_threshold
#print axioms SuccessorLearning.two_warmups_minimal_for_ten
#print axioms SuccessorLearning.unbuffered_actual_stock_cannot_use_correction
#print axioms SuccessorLearning.funded_copy_start_preserves_accounts
#print axioms SuccessorLearning.recopy_reads_childs_current_template
#print axioms SuccessorLearning.revised_grandchild_is_paid_and_productive
#print axioms SuccessorLearning.joined_learning_and_recopy_trace
#print axioms SuccessorLearning.old_template_clamp_loses_grandchild_return
#print axioms SuccessorLearning.complete_local_ledger
#print axioms SuccessorLearning.join_with_earlier_account
