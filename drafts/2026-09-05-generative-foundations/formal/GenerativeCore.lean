import Std

/-!
Structural results for the 2026-09-05 generative-foundations paper.
The safety predicate is an explicit input, not a machine-derived moral truth.
No axioms about the physical world or moral standing are hidden in this file.
-/
namespace GenerativeCore

universe u v w
variable {X : Type u} {A : Type v}

abbrev Transition (X : Type u) (A : Type v) := X → A → X → Prop

def Preserves (T : Transition X A) (K : X → Prop) (x : X) (a : A) : Prop :=
  (∃ y, T x a y) ∧ ∀ y, T x a y → K y

def Invariant (T : Transition X A) (Safe K : X → Prop) : Prop :=
  ∀ x, K x → Safe x ∧ ∃ a, Preserves T K x a

def Viable (T : Transition X A) (Safe : X → Prop) (x : X) : Prop :=
  ∃ K : X → Prop, K x ∧ Invariant T Safe K

theorem viable_safe {T : Transition X A} {Safe : X → Prop} {x : X}
    (h : Viable T Safe x) : Safe x := by
  obtain ⟨K, hx, hK⟩ := h
  exact (hK x hx).1

theorem viable_invariant (T : Transition X A) (Safe : X → Prop) :
    Invariant T Safe (Viable T Safe) := by
  intro x hx
  obtain ⟨K, hkx, hK⟩ := hx
  obtain ⟨hs, a, hen, hnext⟩ := hK x hkx
  refine ⟨hs, a, hen, ?_⟩
  intro y hxy
  exact ⟨K, hnext y hxy, hK⟩

theorem invariant_subset_viable {T : Transition X A} {Safe K : X → Prop}
    (hK : Invariant T Safe K) : ∀ x, K x → Viable T Safe x := by
  intro x hx
  exact ⟨K, hx, hK⟩

theorem viable_predecessor {T : Transition X A} {Safe : X → Prop} {x : X}
    (hs : Safe x) (ha : ∃ a, Preserves T (Viable T Safe) x a) :
    Viable T Safe x := by
  let K : X → Prop := fun y => y = x ∨ Viable T Safe y
  refine ⟨K, Or.inl rfl, ?_⟩
  intro y hy
  rcases hy with hEq | hv
  · subst y
    obtain ⟨a, hen, hn⟩ := ha
    refine ⟨hs, a, hen, ?_⟩
    intro z hz
    exact Or.inr (hn z hz)
  · obtain ⟨hsy, a, hen, hn⟩ := viable_invariant T Safe y hv
    refine ⟨hsy, a, hen, ?_⟩
    intro z hz
    exact Or.inr (hn z hz)

theorem viable_iff_safe_step (T : Transition X A) (Safe : X → Prop) (x : X) :
    Viable T Safe x ↔ Safe x ∧ ∃ a, Preserves T (Viable T Safe) x a := by
  constructor
  · exact viable_invariant T Safe x
  · intro h
    exact viable_predecessor h.1 h.2

theorem outside_no_guaranteed_return {T : Transition X A} {Safe : X → Prop}
    {x : X} (hs : Safe x) (hout : ¬ Viable T Safe x) (a : A)
    (hen : ∃ y, T x a y) : ∃ y, T x a y ∧ ¬ Viable T Safe y := by
  classical
  apply Classical.byContradiction
  intro h
  apply hout
  apply viable_predecessor hs
  refine ⟨a, hen, ?_⟩
  intro y hy
  apply Classical.byContradiction
  intro hnot
  exact h ⟨y, hy, hnot⟩

theorem invariant_run_safe {T : Transition X A} {Safe K : X → Prop}
    (hK : Invariant T Safe K) (p : Nat → X) (a : Nat → A)
    (hzero : K (p 0))
    (hpolicy : ∀ t, K (p t) → Preserves T K (p t) (a t))
    (hrun : ∀ t, T (p t) (a t) (p (t + 1))) : ∀ t, Safe (p t) := by
  have hk : ∀ t, K (p t) := by
    intro t
    induction t with
    | zero => exact hzero
    | succ n ih => exact (hpolicy n ih).2 (p (n + 1)) (hrun n)
  intro t
  exact (hK (p t) (hk t)).1

theorem tighten_shrinks_viability {T : Transition X A} {S₁ S₂ : X → Prop}
    (h : ∀ x, S₁ x → S₂ x) : ∀ x, Viable T S₁ x → Viable T S₂ x := by
  intro x hx
  obtain ⟨K, hkx, hK⟩ := hx
  refine ⟨K, hkx, ?_⟩
  intro y hy
  exact ⟨h y (hK y hy).1, (hK y hy).2⟩

def AllProtected {I : Type w} (P : I → X → Prop) : X → Prop :=
  fun x => ∀ i, P i x

theorem public_viability_protects_each {I : Type w}
    {T : Transition X A} {P : I → X → Prop} {x : X}
    (h : Viable T (AllProtected P) x) (i : I) : P i x := by
  exact viable_safe h i

theorem constraint_reindexing {I J : Type w} (P : I → X → Prop)
    (f : J → I) (hf : Function.Surjective f) (x : X) :
    AllProtected (fun j => P (f j)) x ↔ AllProtected P x := by
  constructor
  · intro h i
    obtain ⟨j, hj⟩ := hf i
    rw [← hj]
    exact h j
  · intro h j
    exact h (f j)

/- A finite soft penalty cannot guarantee a protected floor when rewards
   have no upper bound. This theorem is arithmetic, not an empirical claim. -/
theorem finite_penalty_can_be_outbid (penalty : Nat) :
    ∃ reward : Nat, 0 + penalty < reward := by
  exact ⟨penalty + 1, by omega⟩

/- A two-player countermodel: true = race, false = restrain. -/
def payoff : Bool → Bool → Nat
  | false, false => 3
  | true, false => 5
  | false, true => 0
  | true, true => 1

theorem racing_strictly_dominates : ∀ b, payoff false b < payoff true b := by
  decide

theorem obedient_racing_worse_for_both :
    payoff true true < payoff false false := by decide

/- A robust kernel's complement need not be forward-invariant.
   gamble can reach good or dead; good is controllably safe forever. -/
inductive DemoState where
  | gamble | good | dead
  deriving DecidableEq, Repr

def demoT (x : DemoState) (_ : Unit) (y : DemoState) : Prop :=
  match x with
  | .gamble => y = .good ∨ y = .dead
  | .good => y = .good
  | .dead => y = .dead

def demoSafe (x : DemoState) : Prop := x ≠ .dead

theorem good_viable : Viable demoT demoSafe .good := by
  refine ⟨fun x => x = .good, rfl, ?_⟩
  intro x hx
  subst x
  refine ⟨(show DemoState.good ≠ DemoState.dead from by decide), (), ?_, ?_⟩
  · exact ⟨.good, rfl⟩
  · intro y hy
    exact hy

theorem gamble_not_viable : ¬ Viable demoT demoSafe .gamble := by
  intro h
  obtain ⟨_, a, _, hn⟩ := viable_invariant demoT demoSafe .gamble h
  have hd := hn .dead (Or.inr rfl)
  exact viable_safe hd rfl

theorem outside_can_reach_inside :
    ¬ Viable demoT demoSafe .gamble ∧
    demoT .gamble () .good ∧ Viable demoT demoSafe .good := by
  exact ⟨gamble_not_viable, Or.inl rfl, good_viable⟩

/- A perfectly known deterministic two-state cycle still has structure.
   Endpoint counts or state uncertainty alone cannot define moral value. -/
def flipT (x : Bool) (_ : Unit) (y : Bool) : Prop := y = !x

theorem deterministic_cycle_viable : ∀ x, Viable flipT (fun _ => True) x := by
  intro x
  refine ⟨fun _ => True, True.intro, ?_⟩
  intro y _
  exact ⟨True.intro, (), ⟨!y, rfl⟩, fun _ _ => True.intro⟩

/- A partial improvement relation over explicitly chosen dimensions.
   Integer scores are a demonstration type, not a claim that human dignity
   has a numerical scale. The ethical choice of dimensions is external. -/
def Dominates {D : Type u} (p q : D → Int) : Prop :=
  (∀ d, q d ≤ p d) ∧ ∃ d, q d < p d

theorem dominates_irrefl {D : Type u} (p : D → Int) : ¬ Dominates p p := by
  rintro ⟨_, d, h⟩
  omega

theorem dominates_trans {D : Type u} {p q r : D → Int}
    (hpq : Dominates p q) (hqr : Dominates q r) : Dominates p r := by
  constructor
  · intro d
    have h₁ := hpq.1 d
    have h₂ := hqr.1 d
    omega
  · obtain ⟨d, hd⟩ := hpq.2
    have hr := hqr.1 d
    exact ⟨d, by omega⟩

theorem dominates_asymm {D : Type u} {p q : D → Int}
    (h : Dominates p q) : ¬ Dominates q p := by
  intro hback
  exact dominates_irrefl p (dominates_trans h hback)

end GenerativeCore

#print axioms GenerativeCore.viable_safe
#print axioms GenerativeCore.viable_invariant
#print axioms GenerativeCore.invariant_subset_viable
#print axioms GenerativeCore.viable_predecessor
#print axioms GenerativeCore.viable_iff_safe_step
#print axioms GenerativeCore.outside_no_guaranteed_return
#print axioms GenerativeCore.invariant_run_safe
#print axioms GenerativeCore.tighten_shrinks_viability
#print axioms GenerativeCore.public_viability_protects_each
#print axioms GenerativeCore.constraint_reindexing
#print axioms GenerativeCore.finite_penalty_can_be_outbid
#print axioms GenerativeCore.racing_strictly_dominates
#print axioms GenerativeCore.obedient_racing_worse_for_both
#print axioms GenerativeCore.good_viable
#print axioms GenerativeCore.gamble_not_viable
#print axioms GenerativeCore.outside_can_reach_inside
#print axioms GenerativeCore.deterministic_cycle_viable
#print axioms GenerativeCore.dominates_irrefl
#print axioms GenerativeCore.dominates_trans
#print axioms GenerativeCore.dominates_asymm
