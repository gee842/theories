/-!
# Product construction preserves the seed's basic distinction boundary

Finite binary-product iteration builds structured possibilities relative to a
supplied seed. It cannot create inhabitants from an empty seed or multiple
values from a subsingleton seed. Construction depth is not physical time.
-/

namespace Generative.Deeper

universe u

def Tower (Seed : Type u) : Nat → Type u
  | 0 => Seed
  | n + 1 => Tower Seed n × Tower Seed n

def diagonal {Seed : Type u} : (n : Nat) → Seed → Tower Seed n
  | 0, x => x
  | n + 1, x => (diagonal n x, diagonal n x)

def leaf {Seed : Type u} : (n : Nat) → Tower Seed n → Seed
  | 0, x => x
  | n + 1, x => leaf n x.1

theorem leaf_diagonal {Seed : Type u} (n : Nat) (x : Seed) :
    leaf n (diagonal n x) = x := by
  induction n with
  | zero => rfl
  | succ n ih => exact ih

theorem diagonal_injective {Seed : Type u} (n : Nat) {x y : Seed}
    (h : diagonal n x = diagonal n y) : x = y := by
  have hl := congrArg (leaf n) h
  exact (leaf_diagonal n x).symm.trans (hl.trans (leaf_diagonal n y))

theorem tower_nonempty_iff {Seed : Type u} (n : Nat) :
    Nonempty (Tower Seed n) ↔ Nonempty Seed := by
  constructor
  · rintro ⟨x⟩
    exact ⟨leaf n x⟩
  · rintro ⟨x⟩
    exact ⟨diagonal n x⟩

theorem tower_subsingleton {Seed : Type u} (h : Subsingleton Seed) (n : Nat) :
    Subsingleton (Tower Seed n) := by
  induction n with
  | zero => exact h
  | succ n ih =>
    refine ⟨?_⟩
    intro x y
    exact Prod.ext (ih.elim x.1 y.1) (ih.elim x.2 y.2)

theorem tower_subsingleton_iff {Seed : Type u} (n : Nat) :
    Subsingleton (Tower Seed n) ↔ Subsingleton Seed := by
  constructor
  · intro h
    exact ⟨fun x y => diagonal_injective n (h.elim _ _)⟩
  · intro h
    exact tower_subsingleton h n

theorem tower_empty_iff {Seed : Type u} (n : Nat) :
    (Tower Seed n → False) ↔ (Seed → False) := by
  constructor
  · intro h x
    exact h (diagonal n x)
  · intro h x
    exact h (leaf n x)

theorem seed_distinction_persists {Seed : Type u} (n : Nat) {x y : Seed}
    (h : x ≠ y) : diagonal n x ≠ diagonal n y := by
  intro heq
  exact h (diagonal_injective n heq)

end Generative.Deeper

#print axioms Generative.Deeper.leaf_diagonal
#print axioms Generative.Deeper.diagonal_injective
#print axioms Generative.Deeper.tower_nonempty_iff
#print axioms Generative.Deeper.tower_subsingleton
#print axioms Generative.Deeper.tower_subsingleton_iff
#print axioms Generative.Deeper.tower_empty_iff
#print axioms Generative.Deeper.seed_distinction_persists
