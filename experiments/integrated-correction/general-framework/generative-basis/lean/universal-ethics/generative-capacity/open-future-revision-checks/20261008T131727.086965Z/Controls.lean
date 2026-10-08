import OpenFutureRevision
open OpenFutureRevision GenerativeComparison

-- Exact producer-consumer adapter, with all operational and G0 premises visible.
example {H S Q : Type}
    (admitted : H → Prop) (states : H → Nat → S)
    (rank : H → Nat → S → Nat) (completed : H → Nat → Prop)
    (decideEvent : ∀ h, DecidablePred (completed h))
    (appears : H → Nat → Q → Prop) (generative : Q → Prop)
    (before : H → Q → Prop) (bound : Nat)
    (initial : ∀ h, admitted h → rank h 0 (states h 0) ≤ bound)
    (localStep : ∀ h, admitted h → ∀ n, ¬ completed h n →
      rank h n (states h (n+1)) < rank h n (states h n))
    (handoff : ∀ h, admitted h → ∀ n, ¬ completed h n →
      rank h (n+1) (states h (n+1)) ≤ rank h n (states h (n+1)))
    (correspondence : ∀ h, admitted h → ∀ n, completed h n →
      ∃ q, generative q ∧ appears h n q ∧ ¬ before h q)
    (positive : H → Q → Prop)
    (g0 : G0 (boundedInventory appears generative bound) positive) :
    ∀ h, admitted h → ∃ q, positive h q ∧ ¬ before h q :=
  positive_ground_by_bound admitted appears generative before bound positive g0
    (generation_by_bound admitted states rank completed decideEvent appears
      generative before bound initial localStep handoff correspondence)
