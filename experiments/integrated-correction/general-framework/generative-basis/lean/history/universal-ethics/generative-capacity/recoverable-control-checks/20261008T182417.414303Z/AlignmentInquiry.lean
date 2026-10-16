import Std

/- A finite robust contingent planner. Candidate histories, available experiments,
response laws and their interpretation are supplied. Execution obtains an actual
observation; it never reads the hidden candidate identifier to select a response.
This is conventional finite robust planning, with no algorithmic novelty claim. -/
namespace AlignmentInquiry

structure Plan (Q A : Type) where
  query : Q
  negative : A
  positive : A
  deriving DecidableEq, Repr

def branch {Q A : Type} (p : Plan Q A) (answer : Bool) : A :=
  if answer then p.positive else p.negative

structure Interface (S Q A : Type) where
  probe : S → Q → Option (Bool × S)
  respond : S → A → Option S
  achieved : S → Bool

def run {S Q A : Type} (m : Interface S Q A) (p : Plan Q A) (s : S) : Option S := do
  let (answer, after) ← m.probe s p.query
  m.respond after (branch p answer)

def passes {S Q A : Type} (m : Interface S Q A) (p : Plan Q A) (s : S) : Bool :=
  (run m p s).any m.achieved

def valid {S Q A : Type} (m : Interface S Q A) (states : List S) (p : Plan Q A) : Bool :=
  !states.isEmpty && states.all (passes m p)

def choose {S Q A : Type} (m : Interface S Q A) (states : List S)
    (plans : List (Plan Q A)) : Option (Plan Q A) := plans.find? (valid m states)

def repertoire {Q A : Type} (queries : List Q) (actions : List A) : List (Plan Q A) :=
  queries.flatMap (fun q => actions.flatMap (fun a => actions.map (fun b => ⟨q,a,b⟩)))

theorem repertoire_complete {Q A : Type} (qs : List Q) (as : List A) (p : Plan Q A)
    (q : p.query ∈ qs) (a : p.negative ∈ as) (b : p.positive ∈ as) :
    p ∈ repertoire qs as := by
  cases p
  simp only [repertoire, List.mem_flatMap, List.mem_map]
  exact ⟨_, q, _, a, _, b, rfl⟩

theorem passes_iff_actual_completion {S Q A : Type} (m : Interface S Q A)
    (p : Plan Q A) (s : S) :
    passes m p s = true ↔ ∃ t, run m p s = some t ∧ m.achieved t = true := by
  cases h : run m p s <;> simp [passes, h]

theorem chosen_sound {S Q A : Type} (m : Interface S Q A) (states : List S)
    (plans : List (Plan Q A)) (p : Plan Q A) (h : choose m states plans = some p) :
    states ≠ [] ∧ p ∈ plans ∧
      ∀ s, s ∈ states → ∃ t, run m p s = some t ∧ m.achieved t = true := by
  have hv := List.find?_some h
  have hm := List.mem_of_find?_eq_some h
  simp only [valid, Bool.and_eq_true] at hv
  refine ⟨?_, hm, ?_⟩
  · intro he; subst states; simp at hv
  · intro s hs
    apply (passes_iff_actual_completion m p s).mp
    exact List.all_eq_true.mp hv.2 s hs

theorem chosen_exists_iff {S Q A : Type} (m : Interface S Q A) (states : List S)
    (plans : List (Plan Q A)) :
    (choose m states plans).isSome = true ↔
      ∃ p, p ∈ plans ∧ valid m states p = true := by
  exact List.find?_isSome

theorem no_listed_policy_iff {S Q A : Type} (m : Interface S Q A) (states : List S)
    (plans : List (Plan Q A)) :
    choose m states plans = none ↔ ∀ p, p ∈ plans → valid m states p = false := by
  simp [choose, List.find?_eq_none]

theorem empty_uncertainty_never_certifies {S Q A : Type} (m : Interface S Q A)
    (plans : List (Plan Q A)) : choose m [] plans = none := by
  simp [choose, valid]

theorem actual_covered_execution {S Q A : Type} (m : Interface S Q A)
    (states : List S) (plans : List (Plan Q A)) (p : Plan Q A) (s : S)
    (selection : choose m states plans = some p) (covered : s ∈ states) :
    ∃ answer after final, m.probe s p.query = some (answer, after) ∧
      m.respond after (branch p answer) = some final ∧ m.achieved final = true := by
  obtain ⟨t, ht, goal⟩ := (chosen_sound m states plans p selection).2.2 s covered
  cases hp : m.probe s p.query with
  | none => simp [run, hp] at ht
  | some pair =>
    rcases pair with ⟨answer, after⟩
    exact ⟨answer, after, t, rfl, by simpa [run, hp] using ht, goal⟩

theorem same_answer_same_selected_response {Q A : Type} (p : Plan Q A)
    (a b : Bool) (h : a = b) : branch p a = branch p b := by rw [h]

theorem observational_obstruction {Q A : Type} (p : Plan Q A) (answer : Bool)
    (required₁ required₂ : A → Prop)
    (incompatible : ∀ a, required₁ a → ¬ required₂ a) :
    ¬ (required₁ (branch p answer) ∧ required₂ (branch p answer)) := by
  rintro ⟨h₁,h₂⟩; exact incompatible _ h₁ h₂

end AlignmentInquiry
