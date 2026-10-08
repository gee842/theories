import CorePredication

/-!
Finite continuation obligations and context-sensitive responses.

Assured quantifies over admitted outcomes at every prefix of a supplied word.
Each requested step has a successor; every such successor meets the remaining
obligation. Atomic steps are taken as terminating transitions. This is neither
an actual scheduler nor a physical-time, infinite-progress or ethical theorem.
The construction specializes the familiar demonic weakest-precondition pattern.
The quantity example is an explicitly supplied regulation law, not a model of
human dispositions or a measure of moral worth.
-/

namespace Generative.ContextualWisdom
open CorePredication

universe u v
variable {S : Type u} {A : Type v}

def Assured (P : Process S A) : List A → (S → Prop) → S → Prop
  | [], Q, s => Q s
  | a :: rest, Q, s =>
      Enabled P s a ∧ ∀ t, P.step s a t → Assured P rest Q t

theorem assured_congr (P : Process S A) (w : List A)
    (Q T : S → Prop) (same : ∀ s, Q s ↔ T s) (s : S) :
    Assured P w Q s ↔ Assured P w T s := by
  induction w generalizing s with
  | nil => exact same s
  | cons a w ih =>
    constructor
    · intro h
      exact ⟨h.1, fun t ht => (ih t).mp (h.2 t ht)⟩
    · intro h
      exact ⟨h.1, fun t ht => (ih t).mpr (h.2 t ht)⟩

theorem assured_append_iff (P : Process S A) (xs ys : List A)
    (Q : S → Prop) (s : S) :
    Assured P (xs ++ ys) Q s ↔ Assured P xs (Assured P ys Q) s := by
  induction xs generalizing s with
  | nil => exact Iff.rfl
  | cons a xs ih =>
    constructor
    · intro h
      exact ⟨h.1, fun t ht => (ih t).mp (h.2 t ht)⟩
    · intro h
      exact ⟨h.1, fun t ht => (ih t).mpr (h.2 t ht)⟩

theorem assured_feasible_must (P : Process S A) (w : List A)
    (Q : S → Prop) (s : S) (h : Assured P w Q s) :
    Feasible P s w ∧ Must P w Q s := by
  induction w generalizing s with
  | nil =>
    refine ⟨⟨s, Trace.nil s⟩, ?_⟩
    intro t ht
    have eq := trace_nil_iff.mp ht
    exact eq ▸ h
  | cons a rest ih =>
    obtain ⟨m, hm⟩ := h.1
    obtain ⟨⟨t, tail⟩, _⟩ := ih m (h.2 m hm)
    refine ⟨⟨t, Trace.cons hm tail⟩, ?_⟩
    intro r hr
    obtain ⟨n, hn, hnr⟩ := trace_cons_iff.mp hr
    exact (ih n (h.2 n hn)).2 r hnr

theorem assured_reached_suffix (P : Process S A) (xs ys : List A)
    (Q : S → Prop) {s t : S} (h : Assured P (xs ++ ys) Q s)
    (reached : Trace P s xs t) : Assured P ys Q t := by
  have first := (assured_append_iff P xs ys Q s).mp h
  exact (assured_feasible_must P xs (Assured P ys Q) s first).2 t reached

/-- One branch reaches 3; another stops at 2 before the second requested step. -/
def interrupted : Process Nat Unit where
  step s _ t := (s = 0 ∧ (t = 1 ∨ t = 2)) ∨ (s = 1 ∧ t = 3)

theorem completed_endpoints_omit_interruption :
    May interrupted [(), ()] (fun n => n = 3) 0 ∧
    Must interrupted [(), ()] (fun n => n = 3) 0 ∧
    ¬ Assured interrupted [(), ()] (fun n => n = 3) 0 := by
  have first : interrupted.step 0 () 1 := Or.inl ⟨rfl, Or.inl rfl⟩
  have second : interrupted.step 1 () 3 := Or.inr ⟨rfl, rfl⟩
  refine ⟨⟨3, Trace.cons first (Trace.cons second (Trace.nil 3)), rfl⟩, ?_, ?_⟩
  · intro t ht
    obtain ⟨m, hm, tail⟩ := trace_cons_iff.mp ht
    have last := trace_singleton_iff.mp tail
    change (0 = 0 ∧ (m = 1 ∨ m = 2)) ∨ (0 = 1 ∧ m = 3) at hm
    change (m = 0 ∧ (t = 1 ∨ t = 2)) ∨ (m = 1 ∧ t = 3) at last
    omega
  · intro h
    have branch : interrupted.step 0 () 2 := Or.inl ⟨rfl, Or.inr rfl⟩
    obtain ⟨t, ht⟩ := (h.2 2 branch).1
    change (2 = 0 ∧ (t = 1 ∨ t = 2)) ∨ (2 = 1 ∧ t = 3) at ht
    omega

inductive Move where
  | add
  | remove
  deriving DecidableEq

def update (n : Nat) : Move → Nat
  | .add => n + 1
  | .remove => n - 1

def regulation : Process Nat Move where
  step n a m := m = update n a

/-- A supplied technical operating band, without ethical identification. -/
def Band (n : Nat) : Prop := 1 ≤ n ∧ n ≤ 2

theorem regulation_singleton (n : Nat) (a : Move) (Q : Nat → Prop) :
    Assured regulation [a] Q n ↔ Q (update n a) := by
  constructor
  · intro h
    exact h.2 (update n a) rfl
  · intro h
    refine ⟨⟨update n a, rfl⟩, ?_⟩
    intro m hm
    change m = update n a at hm
    exact hm.symm ▸ h

theorem opposite_responses_same_band :
    Assured regulation [.add] Band 1 ∧
    ¬ Assured regulation [.remove] Band 1 ∧
    Assured regulation [.remove] Band 2 ∧
    ¬ Assured regulation [.add] Band 2 := by
  simp [regulation_singleton, Band, update]

theorem no_aliased_response {O : Type} (observe : Nat → O)
    (alias : observe 1 = observe 2) (choose : O → Move) :
    ¬ (Assured regulation [choose (observe 1)] Band 1 ∧
       Assured regulation [choose (observe 2)] Band 2) := by
  intro h
  have low := (regulation_singleton 1 (choose (observe 1)) Band).mp h.1
  have high := (regulation_singleton 2 (choose (observe 2)) Band).mp h.2
  rw [← alias] at high
  cases choice : choose (observe 1) with
  | add => simp [choice, update, Band] at high
  | remove => simp [choice, update, Band] at low

def response (n : Nat) : Move := if n ≤ 1 then .add else .remove

theorem contextual_response_preserves (n : Nat) (h : Band n) :
    Band (update n (response n)) := by
  unfold Band at h ⊢
  by_cases low : n ≤ 1
  · simp [response, low, update]
  · simp [response, low, update]
    omega

def itinerary : Nat → Nat → List Move
  | 0, _ => []
  | k + 1, n => response n :: itinerary k (update n (response n))

theorem contextual_finite_continuation (k n : Nat) (h : Band n) :
    Assured regulation (itinerary k n) Band n := by
  induction k generalizing n with
  | zero => exact h
  | succ k ih =>
    refine ⟨⟨update n (response n), rfl⟩, ?_⟩
    intro m hm
    change m = update n (response n) at hm
    subst m
    exact ih _ (contextual_response_preserves n h)

theorem success_changes_next_response :
    regulation.step 1 .add 2 ∧
    Assured regulation [.add] Band 1 ∧
    ¬ Assured regulation [.add, .add] Band 1 ∧
    Assured regulation [.add, .remove] Band 1 := by
  refine ⟨rfl, opposite_responses_same_band.1, ?_, ?_⟩
  · intro h
    exact opposite_responses_same_band.2.2.2 (h.2 2 rfl)
  · refine ⟨⟨2, rfl⟩, ?_⟩
    intro m hm
    change m = update 1 .add at hm
    have eq : m = 2 := hm
    exact eq.symm ▸ opposite_responses_same_band.2.2.1

end Generative.ContextualWisdom

#print axioms Generative.ContextualWisdom.assured_congr
#print axioms Generative.ContextualWisdom.assured_append_iff
#print axioms Generative.ContextualWisdom.assured_feasible_must
#print axioms Generative.ContextualWisdom.assured_reached_suffix
#print axioms Generative.ContextualWisdom.completed_endpoints_omit_interruption
#print axioms Generative.ContextualWisdom.regulation_singleton
#print axioms Generative.ContextualWisdom.opposite_responses_same_band
#print axioms Generative.ContextualWisdom.no_aliased_response
#print axioms Generative.ContextualWisdom.contextual_response_preserves
#print axioms Generative.ContextualWisdom.contextual_finite_continuation
#print axioms Generative.ContextualWisdom.success_changes_next_response
