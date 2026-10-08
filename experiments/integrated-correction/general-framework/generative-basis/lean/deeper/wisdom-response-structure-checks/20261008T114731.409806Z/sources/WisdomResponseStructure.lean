import ContextualWisdom

/-!
Response sufficiency need not preserve every outcome distinction or allow one
coarsest sufficient description. The witnesses share one supplied process and
terminal target. A mode identifies the one unavailable route; taking another
route reaches the target. This is a local one-step continuation problem, not a
definition of wisdom, an ethical evaluation, or an account of sensor formation.
-/

namespace Generative.WisdomResponseStructure
open CorePredication ContextualWisdom

abbrev Mode := Fin 3
abbrev Route := Fin 3
abbrev State := Mode × Bool

def advance (s : State) (a : Route) : State := (s.1, decide (a ≠ s.1))

def routes : Process State Route where
  step s a t := t = advance s a

def Reached (s : State) : Prop := s.2 = true

def Adequate {O : Type} (observe : Mode → O) (respond : O → Route) : Prop :=
  ∀ m, Assured routes [respond (observe m)] Reached (m, false)

def leftObservation (m : Mode) : Bool := decide (m = 0)
def rightObservation (m : Mode) : Bool := decide (m = 2)
def leftResponse (o : Bool) : Route := if o then 1 else 0
def rightResponse (o : Bool) : Route := if o then 0 else 2

theorem assured_route_iff (m : Mode) (a : Route) :
    Assured routes [a] Reached (m, false) ↔ a ≠ m := by
  constructor
  · intro h
    have ht := h.2 (advance (m, false) a) rfl
    simpa [Assured, Reached, advance] using ht
  · intro h
    refine ⟨⟨advance (m, false) a, rfl⟩, ?_⟩
    intro t ht
    change t = advance (m, false) a at ht
    subst t
    simpa [Assured, Reached, advance] using h

theorem left_response_adequate : Adequate leftObservation leftResponse := by
  intro m
  rw [assured_route_iff]
  by_cases h : m = 0
  · subst m
    decide
  · simp [leftResponse, leftObservation, h, ne_comm]

theorem right_response_adequate : Adequate rightObservation rightResponse := by
  intro m
  rw [assured_route_iff]
  by_cases h : m = 2
  · subst m
    decide
  · simp [rightResponse, rightObservation, h, ne_comm]

theorem adequate_description_loses_outcome_distinction :
    Adequate leftObservation leftResponse ∧
    leftObservation 1 = leftObservation 2 ∧
    ¬ Assured routes [1] Reached (1, false) ∧
    Assured routes [1] Reached (2, false) := by
  exact ⟨left_response_adequate, rfl,
    by simp [assured_route_iff], by simp [assured_route_iff]⟩

theorem pairwise_common_response (m n : Mode) :
    ∃ a, Assured routes [a] Reached (m, false) ∧
      Assured routes [a] Reached (n, false) := by
  simp only [assured_route_iff]
  have finite : ∀ m n : Fin 3, ∃ a : Fin 3, a ≠ m ∧ a ≠ n := by decide
  exact finite m n

theorem no_response_common_to_all :
    ¬ ∃ a, ∀ m, Assured routes [a] Reached (m, false) := by
  rintro ⟨a, h⟩
  exact (assured_route_iff a a).mp (h a) rfl

theorem common_coarsening_constant {O : Type} (q : Mode → O)
    (fromLeft fromRight : Bool → O)
    (left : ∀ m, q m = fromLeft (leftObservation m))
    (right : ∀ m, q m = fromRight (rightObservation m)) :
    ∀ m, q m = q 0 := by
  have h01 : q 0 = q 1 := (right 0).trans (right 1).symm
  have h12 : q 1 = q 2 := (left 1).trans (left 2).symm
  intro m
  have exhaustive : ∀ n : Fin 3, n = 0 ∨ n = 1 ∨ n = 2 := by decide
  have cases3 := exhaustive m
  rcases cases3 with h | h | h
  · subst m; rfl
  · subst m; exact h01.symm
  · subst m; exact (h01.trans h12).symm

theorem common_coarsening_inadequate {O : Type} (q : Mode → O)
    (fromLeft fromRight : Bool → O)
    (left : ∀ m, q m = fromLeft (leftObservation m))
    (right : ∀ m, q m = fromRight (rightObservation m))
    (respond : O → Route) : ¬ Adequate q respond := by
  intro adequate
  have same := common_coarsening_constant q fromLeft fromRight left right
  have fails := (assured_route_iff (respond (q 0))
    (respond (q (respond (q 0))))).mp (adequate (respond (q 0)))
  rw [same (respond (q 0))] at fails
  exact fails rfl

theorem no_coarsest_adequate_description {O : Type} :
    ¬ ∃ q : Mode → O,
      (∃ respond, Adequate q respond) ∧
      (∀ p : Mode → Bool, (∃ respond, Adequate p respond) →
        ∃ forget : Bool → O, ∀ m, q m = forget (p m)) := by
  rintro ⟨q, ⟨respond, adequate⟩, coarsest⟩
  obtain ⟨fromLeft, left⟩ := coarsest leftObservation ⟨leftResponse, left_response_adequate⟩
  obtain ⟨fromRight, right⟩ := coarsest rightObservation ⟨rightResponse, right_response_adequate⟩
  exact common_coarsening_inadequate q fromLeft fromRight left right respond adequate

#print axioms assured_route_iff
#print axioms left_response_adequate
#print axioms right_response_adequate
#print axioms adequate_description_loses_outcome_distinction
#print axioms pairwise_common_response
#print axioms no_response_common_to_all
#print axioms common_coarsening_constant
#print axioms common_coarsening_inadequate
#print axioms no_coarsest_adequate_description

end Generative.WisdomResponseStructure
