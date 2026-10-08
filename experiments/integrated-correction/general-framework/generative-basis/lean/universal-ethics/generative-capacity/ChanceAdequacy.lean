import Std

/-
Actual continuation and chance constraints, 8 October 2026.

Domain entries represent warranted pairings of potential implementations under
the same relevant support conditions, failures and random seeds. They are not
two incompatible acts asserted to have occurred in one literal actual history.
That coupling, coverage, support window and normative target require evidence.
Natural weights describe one finite rational event law, not ethical importance.
The list is an enumeration: repeated entries are counted repeatedly, so actual
correspondence must prevent unintended duplication of event mass.

Fulfilled is pointwise continuation of demand AND still-working old support.
It is not defined as a probability comparison. The generic mass theorems allow
empty domains and zero total; only the positive-total wrapper has a probability
interpretation. The all-weights converse uses Dirac tests, not an assumption
that the actual law can be freely changed. Repair is an event-level target:
its timely, permitted implementation without an oracle or lost shared support
is an independent obligation, not a consequence of Boolean disjunction.
-/
namespace ChanceAdequacy

def mass {Ω : Type} (domain : List Ω) (weight : Ω → Nat) (event : Ω → Bool) : Nat :=
  match domain with
  | [] => 0
  | h :: tail => (if event h = true then weight h else 0) + mass tail weight event

def IncludedOn {Ω : Type} (domain : List Ω) (before after : Ω → Bool) : Prop :=
  ∀ h ∈ domain, before h = true → after h = true

def total {Ω : Type} (domain : List Ω) (weight : Ω → Nat) : Nat :=
  mass domain weight (fun _ => true)

theorem mass_monotone {Ω : Type} (domain : List Ω) (weight : Ω → Nat)
    (before after : Ω → Bool) (included : IncludedOn domain before after) :
    mass domain weight before ≤ mass domain weight after := by
  induction domain with
  | nil => simp [mass]
  | cons h tail ih =>
    have atHead := included h (by simp)
    have inTail : IncludedOn tail before after :=
      fun x hx => included x (by simp [hx])
    have rest := ih inTail
    cases hb : before h <;> cases ha : after h <;>
      simp_all [mass] <;> omega

theorem positive_added_event_strictly_increases_mass {Ω : Type}
    (domain : List Ω) (weight : Ω → Nat) (before after : Ω → Bool)
    (included : IncludedOn domain before after) (h : Ω) (member : h ∈ domain)
    (positive : 0 < weight h) (absent : before h = false) (present : after h = true) :
    mass domain weight before < mass domain weight after := by
  induction domain with
  | nil => simp at member
  | cons x tail ih =>
    have atHead := included x (by simp)
    have inTail : IncludedOn tail before after :=
      fun y hy => included y (by simp [hy])
    rcases List.mem_cons.mp member with same | later
    · subst x
      have rest := mass_monotone tail weight before after inTail
      simp only [mass, absent, present, Bool.false_eq_true, if_false, if_true]
      omega
    · have strictRest := ih inTail later
      cases hb : before x <;> cases ha : after x <;>
        simp_all [mass] <;> omega

/-- A separating test for the representation, including duplicate enumeration
entries. It is not a claim that this is the actual event law. -/
theorem dirac_mass_positive_iff {Ω : Type} [DecidableEq Ω]
    (domain : List Ω) (h : Ω) (event : Ω → Bool) :
    0 < mass domain (fun x => if x = h then 1 else 0) event ↔
      h ∈ domain ∧ event h = true := by
  induction domain with
  | nil => simp [mass]
  | cons x tail ih =>
    by_cases same : x = h
    · subst x
      cases he : event h <;> simp_all [mass] <;> omega
    · cases he : event x <;> simp_all [mass, List.mem_cons, Ne.symm same]

/-- Agreement for every natural nonnegative weighting is exactly pointwise
coverage on the represented domain. One fixed actual law is weaker. -/
theorem all_weights_preserve_mass_iff {Ω : Type} [DecidableEq Ω]
    (domain : List Ω) (before after : Ω → Bool) :
    (∀ weight : Ω → Nat, mass domain weight before ≤ mass domain weight after) ↔
      IncludedOn domain before after := by
  constructor
  · intro all h member occurs
    have beforePositive := (dirac_mass_positive_iff domain h before).mpr ⟨member, occurs⟩
    have afterPositive : 0 < mass domain (fun x => if x = h then 1 else 0) after :=
      Nat.lt_of_lt_of_le beforePositive (all (fun x => if x = h then 1 else 0))
    exact ((dirac_mass_positive_iff domain h after).mp afterPositive).2
  · intro included weight
    exact mass_monotone domain weight before after included

def target {Ω : Type} (demand oldWorks : Ω → Bool) (h : Ω) : Bool :=
  demand h && oldWorks h

def Fulfilled {Ω : Type} (domain : List Ω) (demand oldWorks newWorks : Ω → Bool) : Prop :=
  IncludedOn domain (target demand oldWorks) newWorks

/-- Numerator bound with one common, explicitly positive denominator. This
does not say that meeting only the numerator bound fulfills the undertaking. -/
theorem fulfillment_gives_chance_floor {Ω : Type} (domain : List Ω)
    (weight : Ω → Nat) (demand oldWorks newWorks : Ω → Bool)
    (positive : 0 < total domain weight)
    (fulfilled : Fulfilled domain demand oldWorks newWorks) :
    0 < total domain weight ∧
    mass domain weight (target demand oldWorks) ≤ mass domain weight newWorks ∧
    mass domain weight newWorks ≤ total domain weight := by
  refine ⟨positive, mass_monotone domain weight _ _ fulfilled, ?_⟩
  exact mass_monotone domain weight newWorks (fun _ => true) (fun _ _ _ => rfl)

def repair {Ω : Type} (demand oldWorks candidate : Ω → Bool) (h : Ω) : Bool :=
  target demand oldWorks h || candidate h

theorem repair_covers_target_and_candidate {Ω : Type} (domain : List Ω)
    (demand oldWorks candidate : Ω → Bool) :
    Fulfilled domain demand oldWorks (repair demand oldWorks candidate) ∧
    IncludedOn domain candidate (repair demand oldWorks candidate) := by
  constructor
  · intro h _ occurs
    simp [repair, occurs]
  · intro h _ occurs
    simp [repair, occurs]

theorem repair_adds_positive_new_protection {Ω : Type} (domain : List Ω)
    (weight : Ω → Nat) (demand oldWorks candidate : Ω → Bool)
    (h : Ω) (member : h ∈ domain) (positive : 0 < weight h)
    (notOldTarget : target demand oldWorks h = false) (added : candidate h = true) :
    mass domain weight (target demand oldWorks) <
      mass domain weight (repair demand oldWorks candidate) := by
  apply positive_added_event_strictly_increases_mass domain weight _ _
    (repair_covers_target_and_candidate domain demand oldWorks candidate).1
    h member positive notOldTarget
  simp [repair, added]

/-- Both represented conditions have positive mass. The new route has positive
chance and the same total success as the old one, yet misses a specifically
due still-working protection. This controls task fidelity, not chance fairness. -/
theorem positive_chance_can_miss_due_protection :
    total [false, true] (fun _ => 1) = 2 ∧
    mass [false, true] (fun _ => 1) (target (fun _ => true) Bool.not) = 1 ∧
    mass [false, true] (fun _ => 1) (fun h => h) = 1 ∧
    ¬ Fulfilled [false, true] (fun _ => true) Bool.not (fun h => h) ∧
    target (fun _ => true) Bool.not false = true ∧
    (fun h : Bool => h) false = false ∧ 0 < (fun _ : Bool => 1) false := by
  refine ⟨rfl, rfl, rfl, ?_, rfl, rfl, by decide⟩
  intro fulfilled
  have impossible := fulfilled false (by simp) (by rfl)
  cases impossible

end ChanceAdequacy
