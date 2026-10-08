import Std

/-!
Finite weighted, fallible inquiry. Paired scenarios are a mathematical coupling,
not two independent ontological substances. The supplied weights must describe
the actual laws for a probabilistic application; a finite observed sample alone
does not certify those laws. Abstention, coverage and false answers are separate.
The elementary coupling bound is established mathematics, formalized here to
connect the existing inquiry-conditions argument to fallible adaptive activity.
-/
namespace Generative.ScientificInquiryNecessity
universe u v w x

def tally {X : Type u} (weight : X → Nat) (value : X → Nat) : List X → Nat
  | [] => 0
  | a :: xs => weight a * value a + tally weight value xs

def committed : Option Bool → Nat
  | none => 0
  | some _ => 1

def wrong (truth : Bool) : Option Bool → Nat
  | none => 0
  | some b => if b = truth then 0 else 1

def apart {E : Type u} [DecidableEq E] (a b : E) : Nat := if a = b then 0 else 1

theorem tally_add {X : Type u} (xs : List X) (w f g : X → Nat) :
    tally w (fun x => f x + g x) xs = tally w f xs + tally w g xs := by
  induction xs with
  | nil => rfl
  | cons x xs ih => simp only [tally, Nat.mul_add, ih]; omega

theorem tally_mono {X : Type u} (xs : List X) (w f g : X → Nat)
    (h : ∀ x ∈ xs, f x ≤ g x) : tally w f xs ≤ tally w g xs := by
  induction xs with
  | nil => exact Nat.le_refl _
  | cons x xs ih =>
    exact Nat.add_le_add (Nat.mul_le_mul_left (w x) (h x (by simp)))
      (ih (fun y hy => h y (by simp [hy])))

theorem pointwise_coverage_bound {E : Type u} [DecidableEq E]
    (read : E → Option Bool) (a b : E) :
    committed (read a) ≤ wrong false (read a) + wrong true (read b) + apart a b := by
  by_cases h : a = b
  · subst b
    cases read a with
    | none => simp [committed, wrong, apart]
    | some c => cases c <;> simp [committed, wrong, apart]
  · have hc : committed (read a) ≤ 1 := by cases read a <;> simp [committed]
    simp only [apart, if_neg h]
    omega

/-- No perfect-answer premise. The reader may use shared randomization x;
    it is the same reader in both alternatives, with the same paired weights. -/
theorem fallible_inquiry_bound {X : Type u} {E : Type v} [DecidableEq E]
    (xs : List X) (w : X → Nat) (e0 e1 : X → E) (read : X → E → Option Bool) :
    tally w (fun x => committed (read x (e0 x))) xs ≤
      tally w (fun x => wrong false (read x (e0 x))) xs +
      tally w (fun x => wrong true (read x (e1 x))) xs +
      tally w (fun x => apart (e0 x) (e1 x)) xs := by
  have h := tally_mono xs w
    (fun x => committed (read x (e0 x)))
    (fun x => wrong false (read x (e0 x)) + wrong true (read x (e1 x)) + apart (e0 x) (e1 x))
    (fun x _ => pointwise_coverage_bound (read x) (e0 x) (e1 x))
  simpa only [tally_add] using h

theorem error_budgets_require_difference {X : Type u} {E : Type v} [DecidableEq E]
    (xs : List X) (w : X → Nat) (e0 e1 : X → E) (read : X → E → Option Bool)
    (coverage b0 b1 : Nat)
    (hc : coverage ≤ tally w (fun x => committed (read x (e0 x))) xs)
    (h0 : tally w (fun x => wrong false (read x (e0 x))) xs ≤ b0)
    (h1 : tally w (fun x => wrong true (read x (e1 x))) xs ≤ b1) :
    coverage ≤ b0 + b1 + tally w (fun x => apart (e0 x) (e1 x)) xs := by
  have h := fallible_inquiry_bound xs w e0 e1 read
  omega

theorem blind_coverage_bound {X : Type u} (xs : List X) (w : X → Nat)
    (answer : X → Option Bool) :
    tally w (fun x => committed (answer x)) xs =
      tally w (fun x => wrong false (answer x)) xs +
      tally w (fun x => wrong true (answer x)) xs := by
  rw [← tally_add]
  congr 1
  funext x
  cases answer x with
  | none => rfl
  | some b => cases b <;> rfl

theorem common_processing_cannot_add_difference {X : Type u} {E : Type v} {F : Type w}
    [DecidableEq E] [DecidableEq F] (xs : List X) (w : X → Nat)
    (e0 e1 : X → E) (process : X → E → F) :
    tally w (fun x => apart (process x (e0 x)) (process x (e1 x))) xs ≤
      tally w (fun x => apart (e0 x) (e1 x)) xs := by
  apply tally_mono
  intro x _
  by_cases h : e0 x = e1 x
  · simp [apart, h]
  · simp only [apart, if_neg h]
    split <;> omega

def run {S : Type u} {U : Type v} (step : S → U → S) : S → List U → S
  | s, [] => s
  | s, z :: zs => run step (step s z) zs

/-- Different descriptions may have different state types and internal divisions.
    R is an explicit witness of indistinguishability, not scientific adequacy. -/
theorem run_preserves_relation {S : Type u} {T : Type v} {U : Type w}
    (left : S → U → S) (right : T → U → T) (R : S → T → Prop)
    (preserves : ∀ s t z, R s t → R (left s z) (right t z))
    (s : S) (t : T) (initial : R s t) (zs : List U) :
    R (run left s zs) (run right t zs) := by
  induction zs generalizing s t with
  | nil => exact initial
  | cons z zs ih => exact ih (left s z) (right t z) (preserves s t z initial)

theorem adaptive_blindness_bound {X : Type u} {S : Type v} {T : Type w} {U : Type x}
    (xs : List X) (w : X → Nat) (noise : X → List U)
    (left : S → U → S) (right : T → U → T)
    (s : X → S) (t : X → T) (R : S → T → Prop)
    (initial : ∀ x ∈ xs, R (s x) (t x))
    (preserves : ∀ a b z, R a b → R (left a z) (right b z))
    (read0 : S → Option Bool) (read1 : T → Option Bool)
    (same_read : ∀ a b, R a b → read0 a = read1 b) :
    tally w (fun x => committed (read0 (run left (s x) (noise x)))) xs =
      tally w (fun x => wrong false (read0 (run left (s x) (noise x)))) xs +
      tally w (fun x => wrong true (read1 (run right (t x) (noise x)))) xs := by
  have equal : ∀ x ∈ xs, read0 (run left (s x) (noise x)) = read1 (run right (t x) (noise x)) := by
    intro x hx
    exact same_read _ _ (run_preserves_relation left right R preserves _ _ (initial x hx) _)
  rw [← tally_add]
  apply Nat.le_antisymm
  · apply tally_mono
    intro x hx
    rw [← equal x hx]
    cases read0 (run left (s x) (noise x)) with
    | none => exact Nat.le_refl _
    | some b => cases b <;> exact Nat.le_refl _
  · apply tally_mono
    intro x hx
    rw [← equal x hx]
    cases read0 (run left (s x) (noise x)) with
    | none => exact Nat.le_refl _
    | some b => cases b <;> exact Nat.le_refl _

/-- An actual universal incompatibility criterion at this interface: any proposed
    account with such a blindness witness cannot also meet these service bounds. -/
theorem excludes_blind_realization {X : Type u}
    (xs : List X) (w : X → Nat) (out0 out1 : X → Option Bool)
    (same : ∀ x ∈ xs, out0 x = out1 x) (c b0 b1 : Nat) (strict : b0 + b1 < c)
    (hc : c ≤ tally w (fun x => committed (out0 x)) xs)
    (h0 : tally w (fun x => wrong false (out0 x)) xs ≤ b0)
    (h1 : tally w (fun x => wrong true (out1 x)) xs ≤ b1) : False := by
  have he : tally w (fun x => wrong true (out0 x)) xs ≤
      tally w (fun x => wrong true (out1 x)) xs :=
    tally_mono xs w _ _ (fun x hx => by rw [same x hx]; exact Nat.le_refl _)
  have hb := blind_coverage_bound xs w out0
  omega

theorem adaptive_service_excludes_blindness
    {X : Type u} {S : Type v} {T : Type w} {U : Type x}
    (xs : List X) (w : X → Nat) (noise : X → List U)
    (left : S → U → S) (right : T → U → T)
    (s : X → S) (t : X → T) (R : S → T → Prop)
    (initial : ∀ x ∈ xs, R (s x) (t x))
    (preserves : ∀ a b z, R a b → R (left a z) (right b z))
    (read0 : S → Option Bool) (read1 : T → Option Bool)
    (same_read : ∀ a b, R a b → read0 a = read1 b)
    (c b0 b1 : Nat) (strict : b0 + b1 < c)
    (hc : c ≤ tally w (fun x => committed (read0 (run left (s x) (noise x)))) xs)
    (h0 : tally w (fun x => wrong false (read0 (run left (s x) (noise x)))) xs ≤ b0)
    (h1 : tally w (fun x => wrong true (read1 (run right (t x) (noise x)))) xs ≤ b1) :
    False := by
  have h := adaptive_blindness_bound xs w noise left right s t R initial preserves read0 read1 same_read
  omega

theorem ten_percent_errors_require_eighty_distinctions {X : Type u} {E : Type v}
    [DecidableEq E] (xs : List X) (w : X → Nat) (e0 e1 : X → E)
    (read : X → E → Option Bool)
    (hc : 100 ≤ tally w (fun x => committed (read x (e0 x))) xs)
    (h0 : tally w (fun x => wrong false (read x (e0 x))) xs ≤ 10)
    (h1 : tally w (fun x => wrong true (read x (e1 x))) xs ≤ 10) :
    80 ≤ tally w (fun x => apart (e0 x) (e1 x)) xs := by
  have h := error_budgets_require_difference xs w e0 e1 read 100 10 10 hc h0 h1
  omega

/-- Sharp finite witness: four informative cases and one indistinguishable case.
    This is an exact law table, not five observations estimating a real law. -/
def cases5 : List Nat := [0, 1, 2, 3, 4]
def evidence0 (_ : Nat) : Bool := false
def evidence1 (x : Nat) : Bool := decide (x < 4)

theorem sharp_fallible_witness :
    tally (fun _ => 1) (fun x => committed (some (evidence0 x))) cases5 = 5 ∧
    tally (fun _ => 1) (fun x => wrong false (some (evidence0 x))) cases5 = 0 ∧
    tally (fun _ => 1) (fun x => wrong true (some (evidence1 x))) cases5 = 1 ∧
    tally (fun _ => 1) (fun x => apart (evidence0 x) (evidence1 x)) cases5 = 4 := by decide

theorem abstention_is_not_discrimination (xs : List Nat) :
    tally (fun _ => 1) (fun _ => committed none) xs = 0 ∧
    tally (fun _ => 1) (fun _ => wrong false none + wrong true none) xs = 0 := by
  induction xs with
  | nil => exact ⟨rfl, rfl⟩
  | cons _ _ ih => simpa [tally, committed, wrong] using ih

end Generative.ScientificInquiryNecessity
