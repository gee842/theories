import ContinuationScope

/-!
The fulfillment status rule of the fulfillment continuation, proved exact.

Each opportunity in the episode leaves an accessible record: `none` (absent,
unbound or channel missing) or `some b` (a present receipt `b`). A record is
faithful to an actual delivery history when every present receipt equals the
actual capture. The claim asks for `k` deliveries.

The evaluator's status (`fulfilled` when certified ≥ k, `pending` when
certified + unknown < k, otherwise `unknown`) is shown to be exactly what
faithful records settle: fulfilled iff every history consistent with the
records meets the claim, pending iff none does, unknown iff the records leave
both possible. A forged record breaks the first equivalence. The last part
places the decision in `ContinuationScope`: once a claim is met, withholding
is the only course that forecloses nothing needlessly; at the last step of an
open claim, delivering and withholding compete and the structure does not
choose between them.
-/
namespace FulfillmentStatus
open ContinuationScope

def certified : List (Option Bool) → Nat
  | [] => 0
  | some true :: rs => certified rs + 1
  | _ :: rs => certified rs

def unknownCount : List (Option Bool) → Nat
  | [] => 0
  | none :: rs => unknownCount rs + 1
  | _ :: rs => unknownCount rs

def delivered : List Bool → Nat
  | [] => 0
  | true :: xs => delivered xs + 1
  | false :: xs => delivered xs

/-- Every present receipt equals the actual capture at that opportunity. -/
def Faithful : List (Option Bool) → List Bool → Prop
  | [], [] => True
  | none :: rs, _ :: xs => Faithful rs xs
  | some b :: rs, x :: xs => b = x ∧ Faithful rs xs
  | _, _ => False

inductive Status | fulfilled | pending | unknown
  deriving DecidableEq

def status (rs : List (Option Bool)) (k : Nat) : Status :=
  if k ≤ certified rs then .fulfilled
  else if certified rs + unknownCount rs < k then .pending
  else .unknown

theorem bounds : ∀ (rs : List (Option Bool)) (xs : List Bool), Faithful rs xs →
    certified rs ≤ delivered xs ∧ delivered xs ≤ certified rs + unknownCount rs
  | [], [], _ => ⟨Nat.le_refl _, Nat.le_refl _⟩
  | none :: rs, x :: xs, h => by
    have ih := bounds rs xs h
    cases x <;> simp only [certified, unknownCount, delivered] <;> omega
  | some b :: rs, x :: xs, ⟨hb, h⟩ => by
    have ih := bounds rs xs h
    subst hb
    cases b <;> simp only [certified, unknownCount, delivered] <;> omega
  | [], _ :: _, h => absurd h id
  | _ :: _, [], h => by cases ‹Option Bool› <;> exact absurd h id

/-- The least-delivery history consistent with the records. -/
def lowest : List (Option Bool) → List Bool
  | [] => []
  | none :: rs => false :: lowest rs
  | some b :: rs => b :: lowest rs

/-- The greatest-delivery history consistent with the records. -/
def highest : List (Option Bool) → List Bool
  | [] => []
  | none :: rs => true :: highest rs
  | some b :: rs => b :: highest rs

theorem lowest_faithful : ∀ rs, Faithful rs (lowest rs) ∧ delivered (lowest rs) = certified rs
  | [] => ⟨trivial, rfl⟩
  | none :: rs => by
    obtain ⟨f, d⟩ := lowest_faithful rs
    exact ⟨f, by simp [lowest, delivered, certified, d]⟩
  | some b :: rs => by
    obtain ⟨f, d⟩ := lowest_faithful rs
    refine ⟨⟨rfl, f⟩, ?_⟩
    cases b <;> simp [lowest, delivered, certified, d]

theorem highest_faithful : ∀ rs, Faithful rs (highest rs) ∧
    delivered (highest rs) = certified rs + unknownCount rs
  | [] => ⟨trivial, rfl⟩
  | none :: rs => by
    obtain ⟨f, d⟩ := highest_faithful rs
    refine ⟨f, ?_⟩
    simp only [highest, delivered, certified, unknownCount, d]
    omega
  | some b :: rs => by
    obtain ⟨f, d⟩ := highest_faithful rs
    refine ⟨⟨rfl, f⟩, ?_⟩
    cases b <;> simp only [highest, delivered, certified, unknownCount, d] <;> omega

/-- Certified fulfillment is exactly fulfillment in every consistent history. -/
theorem fulfilled_iff (rs : List (Option Bool)) (k : Nat) :
    status rs k = .fulfilled ↔ ∀ xs, Faithful rs xs → k ≤ delivered xs := by
  constructor
  · intro h xs f
    unfold status at h
    by_cases hk : k ≤ certified rs
    · exact Nat.le_trans hk (bounds rs xs f).1
    · simp [hk] at h; split at h <;> cases h
  · intro h
    obtain ⟨f, d⟩ := lowest_faithful rs
    have := h _ f
    simp [status, ← d, this]

/-- Pending is exactly non-fulfillment in every consistent history. -/
theorem pending_iff (rs : List (Option Bool)) (k : Nat) :
    status rs k = .pending ↔ ∀ xs, Faithful rs xs → delivered xs < k := by
  constructor
  · intro h xs f
    unfold status at h
    by_cases hk : k ≤ certified rs
    · simp [hk] at h
    · by_cases hp : certified rs + unknownCount rs < k
      · exact Nat.lt_of_le_of_lt (bounds rs xs f).2 hp
      · simp [hk, hp] at h
  · intro h
    obtain ⟨f, d⟩ := highest_faithful rs
    have hp := h _ f
    rw [d] at hp
    have hk : ¬ k ≤ certified rs := by omega
    simp [status, hk, hp]

/-- Unknown is exactly when faithful records leave both possibilities open. -/
theorem unknown_iff (rs : List (Option Bool)) (k : Nat) :
    status rs k = .unknown ↔
      (∃ xs, Faithful rs xs ∧ k ≤ delivered xs) ∧ (∃ xs, Faithful rs xs ∧ delivered xs < k) := by
  obtain ⟨fl, dl⟩ := lowest_faithful rs
  obtain ⟨fh, dh⟩ := highest_faithful rs
  constructor
  · intro h
    unfold status at h
    by_cases hk : k ≤ certified rs
    · simp [hk] at h
    · by_cases hp : certified rs + unknownCount rs < k
      · simp [hk, hp] at h
      · exact ⟨⟨_, fh, by omega⟩, ⟨_, fl, by omega⟩⟩
  · rintro ⟨⟨xs, f, met⟩, ⟨ys, g, unmet⟩⟩
    have b1 := bounds rs xs f
    have b2 := bounds rs ys g
    have hk : ¬ k ≤ certified rs := by omega
    have hp : ¬ certified rs + unknownCount rs < k := by omega
    simp [status, hk, hp]

/-- A forged positive receipt certifies a claim no actual history met. -/
theorem forged_record_misleads :
    status [some true, some true] 2 = .fulfilled ∧
      ¬ Faithful [some true, some true] [false, true] ∧
      delivered [false, true] < 2 := by
  refine ⟨rfl, ?_, by decide⟩
  rintro ⟨h, _⟩
  cases h

/-! ### The decision as a choice between continuations -/

/-- Courses: `true` delivers once more, `false` withholds. Continuations:
`true` is the claim, `false` the support that withholding retains. With
`prior` actual deliveries, the claim is secured when it is already met or the
delivery completes it. -/
def decision (prior k : Nat) : Situation Bool Bool :=
  { courses := [false, true], continuations := [false, true],
    secures := fun deliver c =>
      if c then decide (k ≤ prior) || (deliver && decide (k ≤ prior + 1)) else !deliver }

/-- Once the claim is met, withholding is the only course that forecloses
nothing needlessly. -/
theorem met_claim_withhold_only (prior k : Nat) (met : k ≤ prior) :
    Nonforeclosing (decision prior k) false ∧ ¬ Nonforeclosing (decision prior k) true := by
  refine ⟨⟨by simp [decision], ?_⟩, ?_⟩
  · rintro ⟨b, _, incl, c, _, yes, no⟩
    cases b <;> cases c <;> simp_all [decision] <;> omega
  · rintro ⟨_, none⟩
    refine none ⟨false, by simp [decision], ?_, false, by simp [decision], by simp [decision], by
      simp [decision]⟩
    intro c _ _
    cases c <;> simp [decision, met]

/-- At the last step of an open claim, delivering secures the claim and
withholding secures the support; neither improves on the other. Choosing
needs a priority the structure does not supply. -/
theorem last_step_competes (prior k : Nat) (open_ : prior + 1 = k) :
    Nonforeclosing (decision prior k) false ∧ Nonforeclosing (decision prior k) true := by
  have h1 : ¬ k ≤ prior := by omega
  have h2 : k ≤ prior + 1 := by omega
  refine ⟨⟨by simp [decision], ?_⟩, ⟨by simp [decision], ?_⟩⟩
  · rintro ⟨b, _, incl, c, _, yes, no⟩
    have := incl false (by simp [decision]) (by simp [decision])
    cases b <;> cases c <;> simp_all [decision] <;> omega
  · rintro ⟨b, _, incl, c, _, yes, no⟩
    have := incl true (by simp [decision]) (by simp [decision, h2])
    cases b <;> cases c <;> simp_all [decision] <;> omega

end FulfillmentStatus

#print axioms FulfillmentStatus.certified
#print axioms FulfillmentStatus.unknownCount
#print axioms FulfillmentStatus.delivered
#print axioms FulfillmentStatus.Faithful
#print axioms FulfillmentStatus.Status
#print axioms FulfillmentStatus.status
#print axioms FulfillmentStatus.bounds
#print axioms FulfillmentStatus.lowest
#print axioms FulfillmentStatus.highest
#print axioms FulfillmentStatus.lowest_faithful
#print axioms FulfillmentStatus.highest_faithful
#print axioms FulfillmentStatus.fulfilled_iff
#print axioms FulfillmentStatus.pending_iff
#print axioms FulfillmentStatus.unknown_iff
#print axioms FulfillmentStatus.forged_record_misleads
#print axioms FulfillmentStatus.decision
#print axioms FulfillmentStatus.met_claim_withhold_only
#print axioms FulfillmentStatus.last_step_competes
