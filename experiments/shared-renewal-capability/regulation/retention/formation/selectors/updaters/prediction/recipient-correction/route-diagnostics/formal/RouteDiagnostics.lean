import FormedRecipientRoute

/-!
A stipulated inspection interface to the existing four recipient-write rules.
An independently acquired actual outcome and paid reads of the pre/post-write
record are premises. `actual_report` names the report-to-outcome equality;
payment does not establish it. The abstract inspection bill neither includes
work/target acquisition nor proves an extra bill for the existing learner. This module does not construct that sensor, infer its
calibration, or make audit labels, route identity or provenance observable.
The route remains fixed during a diagnostic sequence. Material payloads satisfy
q < 4. Hypothetical probe words are not claims of affordable execution.
-/
namespace RouteDiagnostics
open RecipientCorrection
open FormedRecipientRoute (Route Template)

structure Sample where
  before : Nat
  issued : Bool
  receipt : Bool
  after : Nat
deriving DecidableEq, Repr

def bit (q : Nat) : Bool := packedAct q .recipient

/-- Present operational input to the imported route. Independent diagnostic
access does not itself repair a missing operational recipient channel. -/
def written (route : Route) (q : Nat) (receipt : Bool) : Nat :=
  (FormedRecipientRoute.revise ⟨route,q⟩ .recipient (bit q) receipt).q

def sample (route : Route) (q : Nat) (receipt : Bool) : Sample :=
  ⟨q,bit q,receipt,written route q receipt⟩

def flip (s : Sample) : Bool := bit s.after != s.issued

def signature : Route → Bool → Bool
  | .target, receipt => !receipt
  | .privateZero, _ => true
  | .closed, _ | .frozen, _ => false

theorem written_recipient_bit (route : Route) (q : Nat) (receipt : Bool) :
    bit (written route q receipt) =
      match route with
      | .target => decode (bit q) receipt
      | .privateZero => !(bit q)
      | .closed | .frozen => bit q := by
  cases route <;>
    simp [written,bit,FormedRecipientRoute.revise,FormedRecipientRoute.channel,
      packed_write_sets_queried_cell,decode]

theorem actual_write_flip_signature (route : Route) (q : Nat) (receipt : Bool) :
    flip (sample route q receipt) = signature route receipt := by
  unfold flip sample
  rw [written_recipient_bit]
  cases route <;> cases receipt <;> cases h : bit q <;> rfl

/-- Equal priced sequential inspection; outcome truth is a separate input
contract, not inferred from payment. No inflow occurs during these four stages. -/
structure Costs where
  beforeRead : Nat
  outcomeRead : Nat
  write : Nat
  afterRead : Nat
deriving DecidableEq, Repr

def totalCost (c : Costs) : Nat := c.beforeRead+c.outcomeRead+c.write+c.afterRead

structure Inspection where
  remaining : Nat
  spent : Nat
  q : Nat
  committed : Bool
  observation : Option Sample
deriving DecidableEq, Repr

def inspect (c : Costs) (fuel : Nat) (route : Route) (q : Nat) (receipt : Bool) : Inspection :=
  if c.beforeRead ≤ fuel then
    let f₁ := fuel-c.beforeRead
    if c.outcomeRead ≤ f₁ then
      let f₂ := f₁-c.outcomeRead
      if c.write ≤ f₂ then
        let f₃ := f₂-c.write
        let q' := written route q receipt
        if c.afterRead ≤ f₃ then
          ⟨f₃-c.afterRead,totalCost c,q',true,some (sample route q receipt)⟩
        else ⟨f₃,c.beforeRead+c.outcomeRead+c.write,q',true,none⟩
      else ⟨f₂,c.beforeRead+c.outcomeRead,q,false,none⟩
    else ⟨f₁,c.beforeRead,q,false,none⟩
  else ⟨fuel,0,q,false,none⟩

theorem completed_inspection (c : Costs) (fuel : Nat) (route : Route) (q : Nat) (receipt : Bool)
    (h : totalCost c ≤ fuel) :
    inspect c fuel route q receipt =
      ⟨fuel-c.beforeRead-c.outcomeRead-c.write-c.afterRead,totalCost c,
        written route q receipt,true,some (sample route q receipt)⟩ := by
  have h₁ : c.beforeRead ≤ fuel := by unfold totalCost at h; omega
  have h₂ : c.outcomeRead ≤ fuel-c.beforeRead := by unfold totalCost at h; omega
  have h₃ : c.write ≤ fuel-c.beforeRead-c.outcomeRead := by unfold totalCost at h; omega
  have h₄ : c.afterRead ≤ fuel-c.beforeRead-c.outcomeRead-c.write := by unfold totalCost at h; omega
  simp [inspect,h₁,h₂,h₃,h₄]

theorem observation_exists_iff_paid (c : Costs) (fuel : Nat) (route : Route) (q : Nat) (receipt : Bool) :
    (∃ s, (inspect c fuel route q receipt).observation = some s) ↔ totalCost c ≤ fuel := by
  constructor
  · intro h
    unfold inspect at h
    split at h <;> try simp at h
    split at h <;> try simp at h
    split at h <;> try simp at h
    split at h <;> try simp at h
    unfold totalCost
    omega
  · intro h
    rw [completed_inspection _ _ _ _ _ h]
    exact ⟨_,rfl⟩

theorem inspection_has_no_refunds (c : Costs) (fuel : Nat) (route : Route) (q : Nat) (receipt : Bool) :
    (inspect c fuel route q receipt).remaining + (inspect c fuel route q receipt).spent = fuel := by
  by_cases h₁ : c.beforeRead ≤ fuel <;>
    by_cases h₂ : c.outcomeRead ≤ fuel-c.beforeRead <;>
    by_cases h₃ : c.write ≤ fuel-c.beforeRead-c.outcomeRead <;>
    by_cases h₄ : c.afterRead ≤ fuel-c.beforeRead-c.outcomeRead-c.write <;>
    simp [inspect,h₁,h₂,h₃,h₄,totalCost] <;> omega

/-- A returned observation certifies a paid committed update in this interface. -/
theorem paid_observation_has_exact_signature (c : Costs) (fuel : Nat) (route : Route)
    (q : Nat) (receipt actualOutcome : Bool) (s : Sample)
    (actual_report : receipt = actualOutcome)
    (h : (inspect c fuel route q receipt).observation = some s) :
    (inspect c fuel route q receipt).committed = true ∧ flip s = signature route actualOutcome := by
  rw [← actual_report]
  have hp := (observation_exists_iff_paid c fuel route q receipt).mp ⟨s,h⟩
  rw [completed_inspection _ _ _ _ _ hp] at h ⊢
  have hs : sample route q receipt = s := Option.some.inj h
  rw [← hs]
  exact ⟨rfl,actual_write_flip_signature _ _ _⟩

inductive Class where
  | actual | privateZero | unchanged
deriving DecidableEq, Repr

def routeClass : Route → Class
  | .target => .actual
  | .privateZero => .privateZero
  | .closed | .frozen => .unchanged

/-- The arguments are the flips on a genuinely observed success and failure. -/
def classify (successFlip failureFlip : Bool) : Option Class :=
  match successFlip,failureFlip with
  | false,true => some .actual
  | true,true => some .privateZero
  | false,false => some .unchanged
  | true,false => none

theorem two_polarity_classifier (route : Route) (qSuccess qFailure : Nat) :
    classify (flip (sample route qSuccess true)) (flip (sample route qFailure false)) =
      some (routeClass route) := by
  rw [actual_write_flip_signature,actual_write_flip_signature]
  cases route <;> rfl

theorem classifier_sound_and_complete (route : Route) (qSuccess qFailure : Nat) :
    let result := classify (flip (sample route qSuccess true)) (flip (sample route qFailure false))
    (result = some .actual ↔ route = .target) ∧
    (result = some .privateZero ↔ route = .privateZero) ∧
    (result = some .unchanged ↔ route = .closed ∨ route = .frozen) := by
  rw [two_polarity_classifier]
  cases route <;> decide

theorem single_polarity_aliases (q : Nat) (hq : q < 4) :
    sample .target q true = sample .frozen q true ∧
    sample .target q false = sample .privateZero q false := by
  have hc : q = 0 ∨ q = 1 ∨ q = 2 ∨ q = 3 := by omega
  rcases hc with rfl | rfl | rfl | rfl <;> decide

/-- Observable here: issued action, post-write code and charged write price.
Gamma, acquired labels, channel presence and provenance are deliberately absent. -/
def word (route : Route) : Nat → List (Bool × Nat) → List (Bool × Nat × Nat)
  | _, [] => []
  | q, (receipt,price)::rest =>
    let q' := written route q receipt
    (bit q,q',price)::word route q' rest

theorem closed_frozen_words_identical (q : Nat) (inputs : List (Bool × Nat)) :
    word .closed q inputs = word .frozen q inputs := by
  induction inputs with
  | nil => rfl
  | cons input inputs ih => simpa [word,written,FormedRecipientRoute.revise,FormedRecipientRoute.channel] using ih

/-- Ideal stable, available plant continuation; no claim these probes are paid. -/
def receiptWord (route : Route) (law : Bool) : Nat → Nat → List Bool
  | _, 0 => []
  | q, n+1 =>
    let r := receiptOf (bit q) law true
    r::receiptWord route law (written route q r) n

theorem wrong_start_three_receipts (actor law : Bool) :
    let q := pack (actor,!law)
    receiptWord .target law q 3 = [false,true,true] ∧
    receiptWord .privateZero law q 3 = [false,true,false] ∧
    receiptWord .closed law q 3 = [false,false,false] ∧
    receiptWord .frozen law q 3 = [false,false,false] := by
  cases actor <;> cases law <;> decide

theorem wrong_start_two_receipts_alias (actor law : Bool) :
    receiptWord .target law (pack (actor,!law)) 2 =
      receiptWord .privateZero law (pack (actor,!law)) 2 := by
  cases actor <;> cases law <;> decide

theorem correct_stable_receipts_never_separate (actor law : Bool) (n : Nat) :
    receiptWord .target law (pack (actor,law)) n = List.replicate n true ∧
    receiptWord .closed law (pack (actor,law)) n = List.replicate n true ∧
    receiptWord .frozen law (pack (actor,law)) n = List.replicate n true := by
  induction n with
  | zero => exact ⟨rfl,rfl,rfl⟩
  | succ n ih =>
      cases actor <;> cases law <;>
        simpa [receiptWord,bit,receiptOf,written,FormedRecipientRoute.revise,
          FormedRecipientRoute.channel,packedAct,unpack,lookup,pack,bitNat,
          packedWrite,update,decode,List.replicate_succ] using ih

def unitCosts : Costs := ⟨1,1,1,1⟩

theorem unpaid_write_is_not_a_negative_signature (route : Route) (q : Nat) (receipt : Bool) :
    (inspect unitCosts 2 route q receipt).q = q ∧
    (inspect unitCosts 2 route q receipt).committed = false ∧
    (inspect unitCosts 2 route q receipt).observation = none ∧
    (inspect unitCosts 2 route q receipt).spent = 2 := by
  exact ⟨rfl,rfl,rfl,rfl⟩

theorem unobserved_committed_write_is_not_an_inspection (route : Route) (q : Nat) (receipt : Bool) :
    (inspect unitCosts 3 route q receipt).q = written route q receipt ∧
    (inspect unitCosts 3 route q receipt).committed = true ∧
    (inspect unitCosts 3 route q receipt).observation = none := by
  exact ⟨rfl,rfl,rfl⟩

end RouteDiagnostics

#print axioms RouteDiagnostics.written_recipient_bit
#print axioms RouteDiagnostics.actual_write_flip_signature
#print axioms RouteDiagnostics.completed_inspection
#print axioms RouteDiagnostics.observation_exists_iff_paid
#print axioms RouteDiagnostics.inspection_has_no_refunds
#print axioms RouteDiagnostics.paid_observation_has_exact_signature
#print axioms RouteDiagnostics.two_polarity_classifier
#print axioms RouteDiagnostics.classifier_sound_and_complete
#print axioms RouteDiagnostics.single_polarity_aliases
#print axioms RouteDiagnostics.closed_frozen_words_identical
#print axioms RouteDiagnostics.wrong_start_three_receipts
#print axioms RouteDiagnostics.wrong_start_two_receipts_alias
#print axioms RouteDiagnostics.correct_stable_receipts_never_separate
#print axioms RouteDiagnostics.unpaid_write_is_not_a_negative_signature
#print axioms RouteDiagnostics.unobserved_committed_write_is_not_an_inspection
