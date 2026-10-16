import Std

/- Independent finite information/payment interface. The state type in the lower
bound is the COMPLETE state accessible to the decision rule. No fresh probe is
available between receiving a target query and selecting its action. -/
namespace RecipientCorrection

inductive Target where
  | actor | recipient
deriving DecidableEq, Repr

abbrev Laws := Bool × Bool

def lookup (laws : Laws) : Target → Bool
  | .actor => laws.1
  | .recipient => laws.2

def Exact {S : Type} (encode : Laws → S) (act : S → Target → Bool) : Prop :=
  ∀ laws target, act (encode laws) target = lookup laws target

def BehaviourallyDifferent {S : Type} (act : S → Target → Bool) (s t : S) : Prop :=
  ∃ target, act s target ≠ act t target

theorem exact_encoding_injective {S : Type} {encode : Laws → S}
    {act : S → Target → Bool} (h : Exact encode act) :
    Function.Injective encode := by
  intro x y heq
  apply Prod.ext
  · calc x.1 = act (encode x) .actor := (h x .actor).symm
         _ = act (encode y) .actor := congrArg (fun s => act s .actor) heq
         _ = y.1 := h y .actor
  · calc x.2 = act (encode x) .recipient := (h x .recipient).symm
         _ = act (encode y) .recipient := congrArg (fun s => act s .recipient) heq
         _ = y.2 := h y .recipient

theorem exact_encoding_behaviourally_distinct {S : Type} {encode : Laws → S}
    {act : S → Target → Bool} (h : Exact encode act) {x y : Laws} (hne : x ≠ y) :
    BehaviourallyDifferent act (encode x) (encode y) := by
  by_cases ha : x.1 = y.1
  · have hp : x.2 ≠ y.2 := fun hp => hne (Prod.ext ha hp)
    exact ⟨.recipient, by rw [h x .recipient, h y .recipient]; exact hp⟩
  · exact ⟨.actor, by rw [h x .actor, h y .actor]; exact ha⟩

theorem four_distinct_controller_states {S : Type} {encode : Laws → S}
    {act : S → Target → Bool} (h : Exact encode act) :
    ∃ s00 s01 s10 s11 : S,
      s00 ≠ s01 ∧ s00 ≠ s10 ∧ s00 ≠ s11 ∧
      s01 ≠ s10 ∧ s01 ≠ s11 ∧ s10 ≠ s11 := by
  have hinj := exact_encoding_injective h
  have ne (x y : Laws) (hne : x ≠ y) : encode x ≠ encode y :=
    fun heq => hne (hinj heq)
  exact ⟨encode (false,false), encode (false,true),
    encode (true,false), encode (true,true),
    ne _ _ (by decide), ne _ _ (by decide), ne _ _ (by decide),
    ne _ _ (by decide), ne _ _ (by decide), ne _ _ (by decide)⟩

theorem no_one_bit_exact_controller (encode : Laws → Bool)
    (act : Bool → Target → Bool) : ¬ Exact encode act := by
  intro h
  obtain ⟨a,b,c,d,hab,hac,_,hbc,_,_⟩ := four_distinct_controller_states h
  cases a <;> cases b <;> cases c <;> simp_all

def sharedAct (bit : Bool) (_ : Target) : Bool := bit
def sharedWrite (_ : Bool) (label : Bool) : Bool := label

theorem shared_bit_cannot_serve_opposite_laws (bit actor : Bool) :
    ¬ (sharedAct bit .actor = actor ∧ sharedAct bit .recipient = !actor) := by
  cases bit <;> cases actor <;> decide

theorem shared_alternating_writes_interfere (actor recipient : Bool)
    (different : actor ≠ recipient) :
    sharedAct (sharedWrite actor recipient) .actor ≠ actor ∧
    sharedAct (sharedWrite recipient actor) .recipient ≠ recipient := by
  exact ⟨Ne.symm different, different⟩

def knownOppositeAct (actor : Bool) : Target → Bool
  | .actor => actor
  | .recipient => !actor

theorem supplied_opposite_relation_needs_only_one_bit (actor : Bool) (target : Target) :
    knownOppositeAct actor target = lookup (actor,!actor) target := by
  cases target <;> rfl

def bitNat (bit : Bool) : Nat := if bit then 1 else 0
def pack (laws : Laws) : Nat := bitNat laws.1 + 2 * bitNat laws.2
def unpack (q : Nat) : Laws := (q % 2 == 1, q / 2 % 2 == 1)
def packedAct (q : Nat) (target : Target) : Bool := lookup (unpack q) target

def update (laws : Laws) : Target → Bool → Laws
  | .actor, bit => (bit, laws.2)
  | .recipient, bit => (laws.1, bit)

def packedWrite (q : Nat) (target : Target) (label : Bool) : Nat :=
  pack (update (unpack q) target label)

theorem unpack_pack (laws : Laws) : unpack (pack laws) = laws := by
  rcases laws with ⟨actor,recipient⟩
  cases actor <;> cases recipient <;> decide

theorem packed_code_bounded (laws : Laws) : pack laws < 4 := by
  rcases laws with ⟨actor,recipient⟩
  cases actor <;> cases recipient <;> decide

theorem packed_table_is_exact : Exact pack packedAct := by
  intro laws target
  simp [packedAct, unpack_pack]

theorem existing_five_code_register_suffices (laws : Laws) : pack laws < 5 := by
  have := packed_code_bounded laws
  omega

theorem packed_write_bounded (q : Nat) (target : Target) (label : Bool) :
    packedWrite q target label < 4 := packed_code_bounded _

theorem packed_write_sets_queried_cell (q : Nat) (target : Target) (label : Bool) :
    packedAct (packedWrite q target label) target = label := by
  cases target <;> simp [packedAct, packedWrite, unpack_pack, update, lookup]

theorem recipient_write_preserves_actor_cell (q : Nat) (label : Bool) :
    packedAct (packedWrite q .recipient label) .actor = packedAct q .actor := by
  simp [packedAct, packedWrite, unpack_pack, update, lookup]

theorem actor_write_preserves_recipient_cell (q : Nat) (label : Bool) :
    packedAct (packedWrite q .actor label) .recipient = packedAct q .recipient := by
  simp [packedAct, packedWrite, unpack_pack, update, lookup]

theorem distinct_target_writes_commute (q : Nat) (actor recipient : Bool) :
    packedWrite (packedWrite q .actor actor) .recipient recipient =
    packedWrite (packedWrite q .recipient recipient) .actor actor := by
  simp [packedWrite, unpack_pack, update]

def swapTarget : Target → Target
  | .actor => .recipient
  | .recipient => .actor

def swapLaws (laws : Laws) : Laws := (laws.2,laws.1)

theorem consistent_target_swap_preserves_commands (laws : Laws) (target : Target) :
    lookup (swapLaws laws) (swapTarget target) = lookup laws target := by
  cases target <;> rfl

theorem consistent_target_swap_preserves_writes (laws : Laws) (target : Target) (label : Bool) :
    swapLaws (update laws target label) = update (swapLaws laws) (swapTarget target) label := by
  cases target <;> rfl

theorem aliased_recipient_write_can_damage_actor (actor recipient oldRecipient : Bool)
    (different : actor ≠ recipient) :
    packedAct (packedWrite (pack (actor,oldRecipient)) .actor recipient) .actor ≠ actor := by
  rw [packed_write_sets_queried_cell]
  exact Ne.symm different

def receiptOf (action law available : Bool) : Bool := (action == law) && available
def decode (action returned : Bool) : Bool := if returned then action else !action
def actorCreditFromRecipient (_action _law _available : Bool) : Nat := 0

theorem noiseless_recipient_receipt_decodes_law (action law : Bool) :
    decode action (receiptOf action law true) = law := by
  cases action <;> cases law <;> decide

theorem zero_actor_receipt_aliases_recipient_outcomes :
    actorCreditFromRecipient false false true = actorCreditFromRecipient false true true ∧
    receiptOf false false true ≠ receiptOf false true true := by decide

theorem no_decoder_from_actor_credit :
    ¬ ∃ decoder : Bool → Nat → Bool,
      ∀ action law, decoder action (actorCreditFromRecipient action law true) = law := by
  rintro ⟨decoder, h⟩
  have h0 := h false false
  have h1 := h false true
  simp only [actorCreditFromRecipient] at h0 h1
  rw [h0] at h1
  contradiction

theorem private_zero_proxy_correct_iff_recipient_failure (action law : Bool) :
    decode action false = law ↔ receiptOf action law true = false := by
  cases action <;> cases law <;> decide

theorem outage_receipt_is_ambiguous :
    receiptOf false true true = receiptOf false false false ∧
    (true : Bool) ≠ false := by decide

theorem recipient_feedback_repairs_only_recipient
    (q : Nat) (action law : Bool) :
    packedAct (packedWrite q .recipient (decode action (receiptOf action law true)))
      .recipient = law ∧
    packedAct (packedWrite q .recipient (decode action (receiptOf action law true)))
      .actor = packedAct q .actor := by
  rw [noiseless_recipient_receipt_decodes_law]
  exact ⟨packed_write_sets_queried_cell _ _ _, recipient_write_preserves_actor_cell _ _⟩

theorem corrected_table_serves_both_targets (actor recipient oldRecipient action : Bool) :
    ∀ target,
      packedAct (packedWrite (pack (actor,oldRecipient)) .recipient
        (decode action (receiptOf action recipient true))) target =
      lookup (actor,recipient) target := by
  intro target
  rw [noiseless_recipient_receipt_decodes_law]
  simp [packedAct, packedWrite, unpack_pack, update]

structure Record where
  action : Bool
  returned : Bool
deriving DecidableEq, Repr

/- The plant supplies the physical receipt, but recording it requires payment.
The writer sees the resulting action-tagged record, never the hidden law. Fuel
here is the actor reserve AFTER all preceding routing/work bills. Recipient
capture adds nothing to this reserve. -/
def observeRecipient (fuel observing : Nat) (action law available : Bool) :
    Option (Nat × Record) :=
  if observing ≤ fuel then
    some (fuel-observing, ⟨action, receiptOf action law available⟩)
  else none

def writeRecipient (fuel writing q : Nat) (record : Record) : Option (Nat × Nat) :=
  if writing ≤ fuel then
    some (fuel-writing, packedWrite q .recipient (decode record.action record.returned))
  else none

def paidFeedback (fuel observing writing q : Nat) (action law available : Bool) :
    Option (Nat × Nat) := do
  let (remaining, record) ← observeRecipient fuel observing action law available
  writeRecipient remaining writing q record

theorem paid_feedback_exists_iff (fuel observing writing q : Nat)
    (action law available : Bool) :
    (∃ result, paidFeedback fuel observing writing q action law available = some result) ↔
      observing + writing ≤ fuel := by
  by_cases ho : observing ≤ fuel
  · by_cases hw : writing ≤ fuel-observing
    · have hc : observing+writing ≤ fuel := by omega
      simp [paidFeedback, observeRecipient, writeRecipient, ho, hw, hc]
    · have hc : ¬ observing+writing ≤ fuel := by omega
      simp [paidFeedback, observeRecipient, writeRecipient, ho, hw, hc]
  · have hc : ¬ observing+writing ≤ fuel := by omega
    simp [paidFeedback, observeRecipient, ho, hc]

theorem affordable_feedback (fuel observing writing q : Nat)
    (action law available : Bool) (h : observing + writing ≤ fuel) :
    paidFeedback fuel observing writing q action law available =
      some (fuel-observing-writing,
        packedWrite q .recipient (decode action (receiptOf action law available))) := by
  have ho : observing ≤ fuel := by omega
  have hw : writing ≤ fuel-observing := by omega
  simp [paidFeedback, observeRecipient, writeRecipient, ho, hw]

theorem affordable_noiseless_feedback (fuel observing writing q : Nat)
    (action law : Bool) (h : observing + writing ≤ fuel) :
    paidFeedback fuel observing writing q action law true =
      some (fuel-observing-writing, packedWrite q .recipient law) := by
  rw [affordable_feedback _ _ _ _ _ _ _ h,
    noiseless_recipient_receipt_decodes_law]

theorem paid_feedback_energy_account (fuel observing writing q : Nat)
    (action law available : Bool) (remaining updated : Nat)
    (h : paidFeedback fuel observing writing q action law available = some (remaining,updated)) :
    remaining + observing + writing = fuel := by
  have hp : observing + writing ≤ fuel :=
    (paid_feedback_exists_iff _ _ _ _ _ _ _).mp ⟨_,h⟩
  rw [affordable_feedback _ _ _ _ _ _ _ hp] at h
  have hf : fuel-observing-writing = remaining := (Prod.mk.inj (Option.some.inj h)).1
  omega

theorem paid_feedback_preserves_actor (fuel observing writing q : Nat)
    (action law available : Bool) (remaining updated : Nat)
    (h : paidFeedback fuel observing writing q action law available = some (remaining,updated)) :
    packedAct updated .actor = packedAct q .actor := by
  have hp := (paid_feedback_exists_iff _ _ _ _ _ _ _).mp ⟨_,h⟩
  rw [affordable_feedback _ _ _ _ _ _ _ hp] at h
  rw [← (Prod.mk.inj (Option.some.inj h)).2]
  exact recipient_write_preserves_actor_cell _ _

theorem paid_feedback_corrects_recipient (fuel observing writing q : Nat)
    (action law : Bool) (remaining updated : Nat)
    (h : paidFeedback fuel observing writing q action law true = some (remaining,updated)) :
    packedAct updated .recipient = law := by
  have hp := (paid_feedback_exists_iff _ _ _ _ _ _ _).mp ⟨_,h⟩
  rw [affordable_noiseless_feedback _ _ _ _ _ _ hp] at h
  rw [← (Prod.mk.inj (Option.some.inj h)).2]
  exact packed_write_sets_queried_cell _ _ _

theorem unpaid_recipient_feedback_is_absent (fuel observing writing q : Nat)
    (action law available : Bool) (h : fuel < observing+writing) :
    paidFeedback fuel observing writing q action law available = none := by
  cases heq : paidFeedback fuel observing writing q action law available with
  | none => rfl
  | some result =>
    have := (paid_feedback_exists_iff _ _ _ _ _ _ _).mp ⟨result,heq⟩
    omega

theorem failed_write_retains_observation_charge (fuel observing writing q : Nat)
    (action law available : Bool) (ho : observing ≤ fuel)
    (hw : fuel < observing+writing) :
    observeRecipient fuel observing action law available =
      some (fuel-observing, ⟨action,receiptOf action law available⟩) ∧
    writeRecipient (fuel-observing) writing q
      ⟨action,receiptOf action law available⟩ = none ∧
    (fuel-observing)+observing = fuel := by
  have hn : ¬ writing ≤ fuel-observing := by omega
  constructor
  · simp [observeRecipient, ho]
  constructor
  · simp [writeRecipient, hn]
  · omega

/- A finite information witness, not a claimed resource trace of the stochastic
producer. Actor law is 0, recipient law is 1, and inherited register is 0. -/
theorem opposite_laws_packed_correction_witness :
    packedAct 0 .recipient = false ∧
    receiptOf false true true = false ∧
    packedWrite 0 .recipient (decode false false) = 2 ∧
    packedAct 2 .actor = false ∧ receiptOf false false true = true ∧
    packedAct 2 .recipient = true ∧ receiptOf true true true = true := by decide

theorem opposite_laws_shared_interference_witness :
    sharedWrite false (decode false (receiptOf false true true)) = true ∧
    receiptOf (sharedAct true .actor) false true = false ∧
    sharedWrite true (decode true (receiptOf true false true)) = false ∧
    receiptOf (sharedAct false .recipient) true true = false := by decide

end RecipientCorrection

#print axioms RecipientCorrection.exact_encoding_injective
#print axioms RecipientCorrection.exact_encoding_behaviourally_distinct
#print axioms RecipientCorrection.four_distinct_controller_states
#print axioms RecipientCorrection.no_one_bit_exact_controller
#print axioms RecipientCorrection.shared_bit_cannot_serve_opposite_laws
#print axioms RecipientCorrection.shared_alternating_writes_interfere
#print axioms RecipientCorrection.supplied_opposite_relation_needs_only_one_bit
#print axioms RecipientCorrection.unpack_pack
#print axioms RecipientCorrection.packed_code_bounded
#print axioms RecipientCorrection.packed_table_is_exact
#print axioms RecipientCorrection.existing_five_code_register_suffices
#print axioms RecipientCorrection.packed_write_bounded
#print axioms RecipientCorrection.packed_write_sets_queried_cell
#print axioms RecipientCorrection.recipient_write_preserves_actor_cell
#print axioms RecipientCorrection.actor_write_preserves_recipient_cell
#print axioms RecipientCorrection.distinct_target_writes_commute
#print axioms RecipientCorrection.consistent_target_swap_preserves_commands
#print axioms RecipientCorrection.consistent_target_swap_preserves_writes
#print axioms RecipientCorrection.aliased_recipient_write_can_damage_actor
#print axioms RecipientCorrection.noiseless_recipient_receipt_decodes_law
#print axioms RecipientCorrection.zero_actor_receipt_aliases_recipient_outcomes
#print axioms RecipientCorrection.no_decoder_from_actor_credit
#print axioms RecipientCorrection.private_zero_proxy_correct_iff_recipient_failure
#print axioms RecipientCorrection.outage_receipt_is_ambiguous
#print axioms RecipientCorrection.recipient_feedback_repairs_only_recipient
#print axioms RecipientCorrection.corrected_table_serves_both_targets
#print axioms RecipientCorrection.paid_feedback_exists_iff
#print axioms RecipientCorrection.affordable_feedback
#print axioms RecipientCorrection.affordable_noiseless_feedback
#print axioms RecipientCorrection.paid_feedback_energy_account
#print axioms RecipientCorrection.paid_feedback_preserves_actor
#print axioms RecipientCorrection.paid_feedback_corrects_recipient
#print axioms RecipientCorrection.unpaid_recipient_feedback_is_absent
#print axioms RecipientCorrection.failed_write_retains_observation_charge
#print axioms RecipientCorrection.opposite_laws_packed_correction_witness
#print axioms RecipientCorrection.opposite_laws_shared_interference_witness
