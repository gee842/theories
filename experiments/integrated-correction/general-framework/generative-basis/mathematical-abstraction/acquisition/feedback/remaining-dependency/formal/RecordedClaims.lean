/-!
Competing claims of two centers, settled by the history's own fulfillment
records except at one point.

Two centers each hold a one-delivery claim; each episode supports one
delivery, and that support perishes with the episode: withholding retains
nothing. This perishability premise matters. If withholding secured retained
support, withholding would no longer be a needless foreclosure at the
symmetric open record, and the symmetric results below would fail. The accessible record says, for each center, whether its claim has
been certified fulfilled. A rule maps a record to serving center `false`,
serving center `true`, or withholding (`none`). A rule *treats the centers
alike* when relabeling the centers in the record relabels its output.

`ContinuationScope` showed that structure alone cannot choose in a symmetric
competition. Here the competition repeats, and earlier fulfillment is
recorded. Results:

* the rule "serve the center whose claim is unfulfilled; withhold when both
  are fulfilled" treats the centers alike on every record and never forecloses
  needlessly on any record except the symmetric open one
  (`record_rule_alike`, `record_rule_nonforeclosing`); it is the only rule
  with both properties (`record_rule_unique`), so it is derived from them
  rather than picked;
* at the symmetric open record (neither fulfilled) every rule that treats the
  centers alike must withhold, which needlessly forecloses both claims
  (`symmetric_open_forces_withholding`); this is the only record where that
  happens (`only_symmetric_open_needs_more`);
* once a supplied first choice is made at that record, the record rule
  completes both claims in the next episode, whichever center went first
  (`both_claims_met_after_first_choice`).

So at least one input that the record does not determine is needed (an
agreement, prior arrival, a further fact about the centers, or a lottery,
which is itself a symmetric procedure); in this two-center, unit-claim model
one suffices. After it, the record stores that choice's effect, and the
derived rule completes the remaining claim. With more centers, an ordering
is needed; if claims renew, the record returns to the symmetric open state
unless it keeps counts. Which first input is legitimate, and who may supply
it, is not decided here. Claims are equal in size and the support per episode is fixed;
unequal claims, changing support and new claimants are not modelled.
-/
namespace RecordedClaims

/-- The record: is center `false`'s claim fulfilled, is center `true`'s? -/
structure Record where
  zero : Bool
  one : Bool
  deriving DecidableEq

def Record.get (r : Record) (c : Bool) : Bool := if c then r.one else r.zero

/-- Relabel the centers. -/
def Record.swap (r : Record) : Record := ⟨r.one, r.zero⟩

/-- Serve a center (`some c`) or withhold (`none`). -/
abbrev Rule := Record → Option Bool

def TreatsAlike (rule : Rule) : Prop :=
  ∀ r, rule r.swap = (rule r).map (!·)

/-- A course needlessly forecloses when it withholds while a claim is open, or
serves an already fulfilled claim while another is open. -/
def Nonforeclosing (r : Record) : Option Bool → Prop
  | none => r.zero = true ∧ r.one = true
  | some c => r.get c = false ∨ (r.zero = true ∧ r.one = true)

def recordRule : Rule := fun r =>
  match r.zero, r.one with
  | false, true => some false
  | true, false => some true
  | true, true => none
  | false, false => none

theorem record_rule_alike : TreatsAlike recordRule := by
  intro ⟨a, b⟩
  cases a <;> cases b <;> rfl

theorem record_rule_nonforeclosing (r : Record) (h : r ≠ ⟨false, false⟩) :
    Nonforeclosing r (recordRule r) := by
  rcases r with ⟨a, b⟩
  cases a <;> cases b <;> simp_all [recordRule, Nonforeclosing, Record.get]

/-- At the symmetric open record every rule that treats the centers alike
withholds, and withholding there forecloses both open claims. -/
theorem symmetric_open_forces_withholding (rule : Rule) (alike : TreatsAlike rule) :
    rule ⟨false, false⟩ = none ∧ ¬ Nonforeclosing ⟨false, false⟩ none := by
  refine ⟨?_, by simp [Nonforeclosing]⟩
  have h := alike ⟨false, false⟩
  simp only [Record.swap] at h
  cases hr : rule ⟨false, false⟩ with
  | none => rfl
  | some c => rw [hr] at h; cases c <;> simp at h

/-- Every other record admits a choice that treats the centers alike and
forecloses nothing needlessly. -/
theorem only_symmetric_open_needs_more (r : Record) :
    (∃ rule : Rule, TreatsAlike rule ∧ Nonforeclosing r (rule r)) ↔ r ≠ ⟨false, false⟩ := by
  constructor
  · rintro ⟨rule, alike, nf⟩ rfl
    exact (symmetric_open_forces_withholding rule alike).2
      ((symmetric_open_forces_withholding rule alike).1 ▸ nf)
  · intro h
    exact ⟨recordRule, record_rule_alike, record_rule_nonforeclosing r h⟩

/-- The record rule is the only rule that treats the centers alike and
forecloses nothing needlessly on every record but the symmetric open one. -/
theorem record_rule_unique (rule : Rule) (alike : TreatsAlike rule)
    (nf : ∀ r, r ≠ ⟨false, false⟩ → Nonforeclosing r (rule r)) :
    ∀ r, rule r = recordRule r := by
  have fixed : ∀ r : Record, r.swap = r → rule r = none := by
    intro r hs
    have h := alike r
    rw [hs] at h
    cases hr : rule r with
    | none => rfl
    | some c => rw [hr] at h; cases c <;> simp at h
  intro ⟨a, b⟩
  cases a <;> cases b
  · exact fixed _ rfl
  · have h := nf ⟨false, true⟩ (by decide)
    cases hr : rule ⟨false, true⟩ with
    | none => rw [hr] at h; simp [Nonforeclosing] at h
    | some c => rw [hr] at h; cases c <;> simp_all [Nonforeclosing, Record.get, recordRule]
  · have h := nf ⟨true, false⟩ (by decide)
    cases hr : rule ⟨true, false⟩ with
    | none => rw [hr] at h; simp [Nonforeclosing] at h
    | some c => rw [hr] at h; cases c <;> simp_all [Nonforeclosing, Record.get, recordRule]
  · exact fixed _ rfl

/-- Delivering to a center records its claim as fulfilled. -/
def serve (r : Record) : Option Bool → Record
  | none => r
  | some false => ⟨true, r.one⟩
  | some true => ⟨r.zero, true⟩

/-- After any supplied first choice at the symmetric open record, one more
episode under the record rule meets both claims. -/
theorem both_claims_met_after_first_choice (first : Bool) :
    let r1 := serve ⟨false, false⟩ (some first)
    let r2 := serve r1 (recordRule r1)
    r2 = ⟨true, true⟩ ∧ recordRule r2 = none := by
  cases first <;> exact ⟨rfl, rfl⟩

end RecordedClaims

#print axioms RecordedClaims.Record
#print axioms RecordedClaims.Record.get
#print axioms RecordedClaims.Record.swap
#print axioms RecordedClaims.TreatsAlike
#print axioms RecordedClaims.Nonforeclosing
#print axioms RecordedClaims.recordRule
#print axioms RecordedClaims.record_rule_alike
#print axioms RecordedClaims.record_rule_nonforeclosing
#print axioms RecordedClaims.symmetric_open_forces_withholding
#print axioms RecordedClaims.only_symmetric_open_needs_more
#print axioms RecordedClaims.record_rule_unique
#print axioms RecordedClaims.serve
#print axioms RecordedClaims.both_claims_met_after_first_choice
