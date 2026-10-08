import GeneratedContraction

/-! Declared mechanisms, not an empirical law or a new logical foundation.
Stock coordinates count ready supports and convertible provision within one
configuration. Serial occupancy is examined separately, with an explicit scope.
-/
namespace Generative.Logic.Mechanisms
open Generative.Deeper

structure Stock where
  ready : Nat
  provision : Nat
deriving DecidableEq

def join (s t : Stock) : Stock :=
  ⟨s.ready + t.ready, s.provision + t.provision⟩
def zero : Stock := ⟨0, 0⟩
def one : Stock := ⟨1, 0⟩
def budget (b : Nat) : Stock := ⟨1, b⟩

inductive Event where
  | form | spend
deriving DecidableEq

/-- Formation converts one unit of provision into one ready support.
Spending removes one ready support from this availability account. -/
inductive Step : Stock → Event → Stock → Prop
  | form (a b : Nat) : Step ⟨a, b + 1⟩ .form ⟨a + 1, b⟩
  | spend (a b : Nat) : Step ⟨a + 1, b⟩ .spend ⟨a, b⟩

def process : Process Stock Event := ⟨Step⟩

theorem left_unit (s : Stock) : join zero s = s := by
  cases s
  simp [join, zero]

theorem step_frame : StepFrame process join := by
  intro g s e t h
  cases h with
  | form a b =>
    simpa [join, Nat.add_assoc] using Step.form (g.ready + a) (g.provision + b)
  | spend a b =>
    simpa [join, Nat.add_assoc] using Step.spend (g.ready + a) (g.provision + b)

def mass (s : Stock) : Nat := s.ready + s.provision

theorem step_mass {s t : Stock} {e : Event} (h : process.step s e t) :
    mass t ≤ mass s := by
  cases h <;> simp only [mass] <;> omega

theorem trace_mass {s t : Stock} {w : List Event} (h : Trace process s w t) :
    mass t ≤ mass s := by
  induction h with
  | nil => exact Nat.le_refl _
  | cons hs _ ih => exact Nat.le_trans ih (step_mass hs)

theorem reach_mass {s t : Stock} (h : Reach process s t) : mass t ≤ mass s := by
  obtain ⟨w, hw⟩ := h
  exact trace_mass hw

theorem form_many (a b k : Nat) :
    Reach process ⟨a, b + k⟩ ⟨a + k, b⟩ := by
  induction k generalizing a with
  | zero => simpa using reach_refl process (Stock.mk a b)
  | succ k ih =>
    have first : Reach process ⟨a, b + (k + 1)⟩ ⟨a + 1, b + k⟩ := by
      exact reach_step process _ .form _ (by
        simpa [Nat.add_assoc] using Step.form a (b + k))
    have rest := ih (a + 1)
    have all := reach_trans process _ _ _ first rest
    simpa [Nat.add_assoc, Nat.add_comm, Nat.add_left_comm] using all

/-- Sharp finite bound, including the no-provision boundary. -/
theorem budget_exact (b n : Nat) :
    (∃ t, Reach process (budget b) t ∧ n + 1 ≤ t.ready) ↔ n ≤ b := by
  constructor
  · rintro ⟨t, ht, hn⟩
    have hm := reach_mass ht
    simp only [mass, budget] at hm
    omega
  · intro hn
    refine ⟨⟨1 + n, b - n⟩, ?_, ?_⟩
    · have h := form_many 1 (b - n) n
      have eq : b - n + n = b := by omega
      simpa only [eq, budget] using h
    · change n + 1 ≤ 1 + n
      omega

theorem paid_duplication : Reach process (budget 1) (join one one) := by
  exact reach_step process _ .form _ (Step.form 1 0)

theorem paid_contraction : Replacement process join (budget 1) (join one one) :=
  replacement_of_reach step_frame paid_duplication

theorem no_free_duplication : ¬ Reach process one (join one one) := by
  intro h
  have hm := reach_mass h
  simp [mass, one, join] at hm

theorem no_free_contraction : ¬ Contraction process join one := by
  intro h
  exact no_free_duplication ((contraction_iff_duplicate zero left_unit step_frame one).mp h)

/-- Even a funded whole package cannot duplicate itself while retaining all
the provision counted in it. Paid replacement is not ordinary contraction. -/
theorem no_budget_contraction (b : Nat) :
    ¬ Contraction process join (budget b) := by
  intro h
  have hd := (contraction_iff_duplicate zero left_unit step_frame (budget b)).mp h
  have hm := reach_mass hd
  simp only [mass, budget, join] at hm
  omega

theorem formation : Reach process (Stock.mk 0 2) (budget 1) :=
  reach_step process _ .form _ (Step.form 0 1)

theorem spending : Reach process (budget 1) one := by
  have h := reach_trans process _ _ _ paid_duplication
    (reach_step process (Stock.mk 2 0) .spend one (Step.spend 1 0))
  exact h

/-- One history forms a paid substitution capability and then exhausts it.
This does not retract a previously proved timeless proposition. -/
theorem formed_then_exhausted :
    Reach process (Stock.mk 0 2) (budget 1) ∧
    Replacement process join (budget 1) (join one one) ∧
    Reach process (budget 1) one ∧
    ¬ Replacement process join one (join one one) :=
  ⟨formation, paid_contraction, spending, no_free_contraction⟩

namespace Serial
inductive Port where
  | free | held
deriving DecidableEq
inductive Event where
  | take | release
deriving DecidableEq
inductive Step : Port → Event → Port → Prop
  | take : Step .free .take .held
  | release : Step .held .release .free
def process : Process Port Event := ⟨Step⟩
def cycles : Nat → List Event
  | 0 => []
  | n + 1 => .take :: .release :: cycles n

theorem serial_reuse (n : Nat) : Trace process .free (cycles n) .free := by
  induction n with
  | zero => exact .nil _
  | succ n ih => exact .cons Step.take (.cons Step.release ih)

theorem no_overlapping_takes : ¬ Feasible process .free [.take, .take] := by
  rintro ⟨t, h⟩
  cases h with
  | cons hs ht =>
    cases hs
    cases ht with
    | cons hs _ => cases hs

end Serial

namespace Interference
inductive State where
  | atom | pair | context | blocked | available
deriving DecidableEq

/-- A stipulated context blocks duplication. This rival tests the omitted
frame premise; it does not itself derive a physical interference mechanism. -/
def join : State → State → State
  | .atom, .atom => .pair
  | .context, .atom => .blocked
  | .context, .pair => .available
  | _, s => s
inductive Step : State → Unit → State → Prop
  | duplicate : Step .atom () .pair
def process : Process State Unit := ⟨Step⟩

theorem left_unit (s : State) : join .available s = s := by
  cases s <;> rfl

theorem standalone_duplicate : Reach process .atom (join .atom .atom) :=
  reach_step process _ () _ Step.duplicate

theorem blocked_stays {w : List Unit} {t : State}
    (h : Trace process .blocked w t) : t = .blocked := by
  cases h with
  | nil => rfl
  | cons hs _ => cases hs

theorem contextual_contraction_fails : ¬ Contraction process join .atom := by
  intro h
  have hr := h .context .available (reach_refl process .available)
  obtain ⟨w, hw⟩ := hr
  have eq := blocked_stays hw
  cases eq

theorem primitive_frame_fails : ¬ StepFrame process join := by
  intro hf
  have hs := hf .context .atom () .pair Step.duplicate
  cases hs
end Interference
end Generative.Logic.Mechanisms

#print axioms Generative.Logic.Mechanisms.left_unit
#print axioms Generative.Logic.Mechanisms.step_frame
#print axioms Generative.Logic.Mechanisms.step_mass
#print axioms Generative.Logic.Mechanisms.trace_mass
#print axioms Generative.Logic.Mechanisms.reach_mass
#print axioms Generative.Logic.Mechanisms.form_many
#print axioms Generative.Logic.Mechanisms.budget_exact
#print axioms Generative.Logic.Mechanisms.paid_duplication
#print axioms Generative.Logic.Mechanisms.paid_contraction
#print axioms Generative.Logic.Mechanisms.no_free_duplication
#print axioms Generative.Logic.Mechanisms.no_free_contraction
#print axioms Generative.Logic.Mechanisms.no_budget_contraction
#print axioms Generative.Logic.Mechanisms.formation
#print axioms Generative.Logic.Mechanisms.spending
#print axioms Generative.Logic.Mechanisms.formed_then_exhausted
#print axioms Generative.Logic.Mechanisms.Serial.serial_reuse
#print axioms Generative.Logic.Mechanisms.Serial.no_overlapping_takes
#print axioms Generative.Logic.Mechanisms.Interference.standalone_duplicate
#print axioms Generative.Logic.Mechanisms.Interference.left_unit
#print axioms Generative.Logic.Mechanisms.Interference.blocked_stays
#print axioms Generative.Logic.Mechanisms.Interference.contextual_contraction_fails
#print axioms Generative.Logic.Mechanisms.Interference.primitive_frame_fails
