import Std

/-!
Conditional structural results for WHITEPAPER-v0.4.
Stocks are nonnegative surplus above a declared critical floor. The debit model
applies only for the stated interval; it is not an empirical law of societies.
Invariance is relative to the supplied transition relation and predicate.
No axiom asserts moral standing, real-world model adequacy, or immortality.
-/
namespace ExistenceConditions

theorem cumulative_deficit (s : Nat → Nat) (d N : Nat)
    (hstep : ∀ n, n < N → s (n + 1) + d ≤ s n) :
    ∀ n, n ≤ N → s n + n * d ≤ s 0 := by
  intro n
  induction n with
  | zero => simp
  | succ n ih =>
    intro hn
    have hp := ih (by omega)
    have hs := hstep n (by omega)
    simp only [Nat.succ_mul]
    omega

theorem no_persistent_deficit (s : Nat → Nat) (d : Nat) (hd : 1 ≤ d) :
    ¬ (∀ n, s (n + 1) + d ≤ s n) := by
  intro h
  have hb := cumulative_deficit s d (s 0 + 1) (fun n _ => h n)
    (s 0 + 1) (by omega)
  have hm := Nat.mul_le_mul_left (s 0 + 1) hd
  simp only [Nat.mul_one] at hm
  omega

universe u v w z

theorem observation_control_obstruction
    {W : Type u} {O : Type v} {A : Type w}
    (obs : W → O) (safeAction : W → A → Prop) (w₁ w₂ : W)
    (same : obs w₁ = obs w₂)
    (incompatible : ∀ a, ¬ (safeAction w₁ a ∧ safeAction w₂ a))
    (controller : O → A) :
    ¬ (∀ world, safeAction world (controller (obs world))) := by
  intro h
  apply incompatible (controller (obs w₁))
  refine ⟨h w₁, ?_⟩
  rw [same]
  exact h w₂

abbrev Transition (X : Type u) (A : Type v) := X → A → X → Prop

def Invariant {X : Type u} {A : Type v}
    (T : Transition X A) (K : X → Prop) : Prop :=
  ∀ x, K x → ∃ a, (∃ y, T x a y) ∧ ∀ y, T x a y → K y

def ProductTransition {X : Type u} {A : Type v}
    {Y : Type w} {B : Type z}
    (T : Transition X A) (U : Transition Y B) :
    Transition (X × Y) (A × B) :=
  fun x a y => T x.1 a.1 y.1 ∧ U x.2 a.2 y.2

theorem product_invariant {X : Type u} {A : Type v}
    {Y : Type w} {B : Type z}
    (T : Transition X A) (U : Transition Y B)
    (K : X → Prop) (L : Y → Prop)
    (hK : Invariant T K) (hL : Invariant U L) :
    Invariant (ProductTransition T U) (fun xy => K xy.1 ∧ L xy.2) := by
  intro xy hxy
  obtain ⟨a, ⟨x', hx'⟩, ha⟩ := hK xy.1 hxy.1
  obtain ⟨b, ⟨y', hy'⟩, hb⟩ := hL xy.2 hxy.2
  refine ⟨(a, b), ⟨(x', y'), hx', hy'⟩, ?_⟩
  intro next hn
  exact ⟨ha next.1 hn.1, hb next.2 hn.2⟩

theorem abstraction_refinement {X : Type u} {A : Type v}
    {Y : Type w} {B : Type z}
    (T : Transition X A) (U : Transition Y B) (project : X → Y)
    (L : Y → Prop) (hL : Invariant U L)
    (implement : ∀ x b, (∃ next, U (project x) b next) →
      ∃ a, (∃ next, T x a next) ∧
        ∀ next, T x a next → U (project x) b (project next)) :
    Invariant T (fun x => L (project x)) := by
  intro x hx
  obtain ⟨b, enabled, preserves⟩ := hL (project x) hx
  obtain ⟨a, enabledConcrete, sound⟩ := implement x b enabled
  refine ⟨a, enabledConcrete, ?_⟩
  intro next hn
  exact preserves (project next) (sound next hn)

end ExistenceConditions

#print axioms ExistenceConditions.cumulative_deficit
#print axioms ExistenceConditions.no_persistent_deficit
#print axioms ExistenceConditions.observation_control_obstruction
#print axioms ExistenceConditions.product_invariant
#print axioms ExistenceConditions.abstraction_refinement
