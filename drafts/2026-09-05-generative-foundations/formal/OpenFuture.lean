import Std

/-!
Structural results for WHITEPAPER-v0.2.md.
These prove limits of observation and finite countermodels.
They do not derive ethical standing or empirical facts from logic alone.
-/
namespace OpenFuture

universe u v

/- If available observations are identical but the relevant outcome differs,
   a verdict based only on those observations cannot be correct in both cases. -/
theorem observation_limit {W : Type u} {O : Type v}
    (observe : W → O) (truth : W → Bool) {w₁ w₂ : W}
    (same : observe w₁ = observe w₂) (different : truth w₁ ≠ truth w₂)
    (judge : O → Bool) :
    ¬ (judge (observe w₁) = truth w₁ ∧ judge (observe w₂) = truth w₂) := by
  intro h
  apply different
  calc
    truth w₁ = judge (observe w₁) := h.1.symm
    _ = judge (observe w₂) := congrArg judge same
    _ = truth w₂ := h.2

/- true = externalize harm; false = use the protected alternative.
   These are hypothetical choices with explicitly assigned consequences. -/
def localReturn : Bool → Nat
  | false => 3
  | true => 5

def meetsProtection (a : Bool) : Prop := a = false

theorem local_maximum_violates_protection (a : Bool)
    (h : ∀ b, localReturn b ≤ localReturn a) : ¬ meetsProtection a := by
  cases a with
  | false =>
    have hb := h true
    simp [localReturn] at hb
  | true => simp [meetsProtection]

/- A zero-sum score need not damage a shared background.
   This separates a payoff classification from an ethical judgment. -/
def scoreA : Bool → Int
  | false => -1
  | true => 1

def scoreB (b : Bool) : Int := -scoreA b

def backgroundOpen (_ : Bool) : Prop := True

theorem zero_sum_without_closure (b : Bool) :
    scoreA b + scoreB b = 0 ∧ backgroundOpen b := by
  cases b <;> simp [scoreA, scoreB, backgroundOpen]

end OpenFuture

#print axioms OpenFuture.observation_limit
#print axioms OpenFuture.local_maximum_violates_protection
#print axioms OpenFuture.zero_sum_without_closure
