import PracticalJudgment

/-
Crossed claims and changing joint opportunities, 8 October 2026.

P, Q and R identify differentiated protection requirements within one provision.
The intended crossed case permits P's loss to be graver than Q's or R's; equal
standing or equal gravity is not inferred from this finite index. Route efficacy,
permission, timing, burdens and any justified chance floor are supplied.
Tickets describe finite rational lotteries with a common positive denominator.
The positive result is a coupled replacement on the same actual ticket, not an
additive welfare judgment, a proof of the floor, or a uniquely required lottery.

The final menu control instantiates a specified strongest-claim filter. Its
scores/cutoff are diagnostic inputs, not LR, a complete ethics or an attribution
of these exact numbers to a source author. Existing generic cycle/composition
obstructions in AggregationContext are reused in prose, not re-proved here.
-/
namespace CrossedClaims

inductive Claim where
  | p
  | q
  | r
  deriving DecidableEq

inductive Route where
  | solo
  | other
  | joint
  deriving DecidableEq

def protects : Route → Claim → Prop
  | .solo, .p => True
  | .other, .q => True
  | .other, .r => True
  | .joint, .p => True
  | .joint, .q => True
  | _, _ => False

def replaceRoute : Route → Route
  | .solo => .joint
  | r => r

theorem replacement_preserves_each_ticket :
    (∀ route,
      (protects (replaceRoute route) .p ↔ protects route .p) ∧
      (protects (replaceRoute route) .r ↔ protects route .r) ∧
      (protects route .q → protects (replaceRoute route) .q)) ∧
    (¬ protects .solo .q ∧ protects (replaceRoute .solo) .q) := by
  constructor
  · intro route
    cases route <;> simp [protects, replaceRoute]
  · simp [protects, replaceRoute]

theorem joint_strictly_extends_solo_protection :
    PracticalJudgment.Better protects (fun (_ : Route) (_ : Unit) => False)
      .joint .solo := by
  apply PracticalJudgment.protection_anchor (c := Claim.q)
  · intro claim h
    cases claim <;> simp_all [protects]
  · trivial
  · intro h
    exact h

structure Tickets where
  solo : Nat
  other : Nat
  joint : Nat

def ticketTotal (t : Tickets) : Nat := t.solo + t.other + t.joint

def protectedTickets (t : Tickets) : Claim → Nat
  | .p => t.solo + t.joint
  | .q => t.other + t.joint
  | .r => t.other

/-- Replace every solo ticket by the newly available joint route. -/
def transfer (t : Tickets) : Tickets := ⟨0, t.other, t.solo + t.joint⟩

theorem transfer_conserves_total_and_chances (t : Tickets) :
    ticketTotal (transfer t) = ticketTotal t ∧
    protectedTickets (transfer t) .p = protectedTickets t .p ∧
    protectedTickets (transfer t) .r = protectedTickets t .r ∧
    protectedTickets (transfer t) .q = protectedTickets t .q + t.solo := by
  simp [transfer, ticketTotal, protectedTickets, Nat.add_comm, Nat.add_left_comm]

theorem transfer_preserves_any_satisfied_floor (t : Tickets) (floor : Claim → Nat)
    (positive : 0 < ticketTotal t)
    (satisfied : ∀ claim, floor claim ≤ protectedTickets t claim) :
    0 < ticketTotal (transfer t) ∧
      ∀ claim, floor claim ≤ protectedTickets (transfer t) claim := by
  obtain ⟨total, sameP, sameR, addQ⟩ := transfer_conserves_total_and_chances t
  constructor
  · omega
  · intro claim
    have h := satisfied claim
    cases claim
    · rw [sameP]
      exact h
    · rw [addQ]
      omega
    · rw [sameR]
      exact h

theorem transfer_strictly_improves_q (t : Tickets) (used : 0 < t.solo) :
    protectedTickets t .q < protectedTickets (transfer t) .q := by
  have h := (transfer_conserves_total_and_chances t).2.2.2
  omega

def EqualPersonalChances (t : Tickets) : Prop :=
  protectedTickets t .p = protectedTickets t .q ∧
  protectedTickets t .q = protectedTickets t .r

theorem equal_personal_chances_iff (t : Tickets) :
    EqualPersonalChances t ↔ t.joint = 0 ∧ t.solo = t.other := by
  simp only [EqualPersonalChances, protectedTickets]
  omega

/-- Exact equality can reject a same-ticket protection improvement. The theorem
does not endorse exact equality for these possibly unequal-gravity requirements. -/
theorem equal_chances_have_improving_replacement (t : Tickets)
    (positive : 0 < ticketTotal t) (equal : EqualPersonalChances t) :
    ticketTotal (transfer t) = ticketTotal t ∧
    (∀ claim, protectedTickets t claim ≤ protectedTickets (transfer t) claim) ∧
    protectedTickets t .q < protectedTickets (transfer t) .q ∧
    ¬ EqualPersonalChances (transfer t) := by
  obtain ⟨noJoint, same⟩ := (equal_personal_chances_iff t).mp equal
  have used : 0 < t.solo := by
    unfold ticketTotal at positive
    omega
  refine ⟨(transfer_conserves_total_and_chances t).1,
    (transfer_preserves_any_satisfied_floor t (protectedTickets t) positive
      (fun _ => Nat.le_refl _)).2,
    transfer_strictly_improves_q t used, ?_⟩
  intro h
  have noJoint' := ((equal_personal_chances_iff (transfer t)).mp h).1
  simp only [transfer] at noJoint'
  omega

/- Specific menu-dependent relevance control. Different group indices stand for
distinct supplied rescue sets here, unlike Q's shared protection in the routes
above. Group-selection probability is not identified with individual chance. -/
inductive RescueGroup where
  | strongest
  | middle
  | lower
  deriving DecidableEq

def gravity : RescueGroup → Nat
  | .strongest => 10
  | .middle => 6
  | .lower => 4

def groupSize : RescueGroup → Nat
  | .strongest => 1
  | .middle => 2
  | .lower => 4

def menuAnchor (menu : List RescueGroup) : Nat :=
  (menu.map gravity).foldr Nat.max 0

def filteredScore (anchor : Nat) (group : RescueGroup) : Nat :=
  if 2 * gravity group < anchor then 0 else groupSize group * gravity group

def SelectedByFilter (menu : List RescueGroup) (a : RescueGroup) : Prop :=
  PracticalJudgment.Frontier (fun g => g ∈ menu)
    (fun b a => filteredScore (menuAnchor menu) a < filteredScore (menuAnchor menu) b) a

theorem unselected_strong_route_changes_filtered_choice :
    SelectedByFilter [.middle, .lower] .lower ∧
    SelectedByFilter [.strongest, .middle, .lower] .middle ∧
    ¬ SelectedByFilter [.strongest, .middle, .lower] .strongest ∧
    filteredScore (menuAnchor [.middle, .lower]) .lower = 16 ∧
    filteredScore (menuAnchor [.strongest, .middle, .lower]) .lower = 0 := by
  have pair : SelectedByFilter [.middle, .lower] .lower := by
    constructor
    · simp
    · intro b hb
      cases b <;>
        simp_all [menuAnchor, filteredScore, gravity, groupSize]
  have triple : SelectedByFilter [.strongest, .middle, .lower] .middle := by
    constructor
    · simp
    · intro b _
      cases b <;> simp [menuAnchor, filteredScore, gravity, groupSize]
  have rejected : ¬ SelectedByFilter [.strongest, .middle, .lower] .strongest := by
    intro h
    have noBetter := h.2 .middle (by simp)
    simp [menuAnchor, filteredScore, gravity, groupSize] at noBetter
  refine ⟨pair, triple, rejected, ?_, ?_⟩ <;> rfl

end CrossedClaims
