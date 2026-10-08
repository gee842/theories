import Std

/-!
Audit of a two-stage argument for favorable new formation. Histories denote
alternative continuations of one formative situation. Comparisons are supplied
normative interpretations, not ethical conclusions extracted from arithmetic.
The finite diagnostic only tests transport between two evaluation contexts.
It is not an adequate rival moral theory or a counterexample to G0.
-/
namespace Generative.FormationSequence

def TransitiveComparison {H : Type} (better : H → H → Prop) : Prop :=
  ∀ a b c, better a b → better b c → better a c

theorem whole_comparisons_favor_formation {H : Type}
    (better : H → H → Prop) (trans : TransitiveComparison better)
    (baseline retained redirected : H)
    (first : better retained baseline)
    (second : better redirected retained) : better redirected baseline :=
  trans redirected retained baseline second first

theorem transport_supports_initial_comparison {H : Type}
    (initial later : H → H → Prop)
    (trans : TransitiveComparison initial)
    (baseline retained redirected : H)
    (first : initial retained baseline)
    (second : later redirected retained)
    (transport : later redirected retained → initial redirected retained) :
    initial redirected baseline :=
  trans redirected retained baseline (transport second) first

theorem faithful_redescription_preserves_result {H : Type}
    (better sameContent : H → H → Prop)
    (preserve : ∀ a b c, sameContent a b → (better a c ↔ better b c))
    (sequence direct baseline : H)
    (same : sameContent sequence direct)
    (favorable : better sequence baseline) : better direct baseline :=
  (preserve sequence direct baseline same).mp favorable

-- These are whole alternatives in the diagnostic, not successive snapshots.
-- The retained alternative forms living and preserves an incumbent gain;
-- the redirected alternative forms that living with a richer continuation
-- while rescinding the optional incumbent gain.
inductive History where
  | baseline
  | retained
  | redirected
  deriving DecidableEq

def incumbentGain : History → Nat
  | .baseline => 0
  | .retained => 1
  | .redirected => 0

-- None denotes no new bearer in this continuation, not zero welfare for one.
def newLiving : History → Option Nat
  | .baseline => none
  | .retained => some 1
  | .redirected => some 3

def initialScore (h : History) : Nat := incumbentGain h

-- A stipulated aggregate after the formation commitment. No empirical
-- comparability of welfare or justification of addition is claimed.
def laterScore (h : History) : Nat :=
  incumbentGain h + (newLiving h).getD 0

def ScoredAbove {H : Type} (score : H → Nat) (a b : H) : Prop :=
  score b < score a

theorem score_comparison_transitive {H : Type} (score : H → Nat) :
    TransitiveComparison (ScoredAbove score) := by
  intro a b c hab hbc
  exact Nat.lt_trans hbc hab

theorem stages_can_favor_without_initial_favor :
    TransitiveComparison (ScoredAbove initialScore) ∧
    TransitiveComparison (ScoredAbove laterScore) ∧
    ScoredAbove initialScore .retained .baseline ∧
    ScoredAbove laterScore .redirected .retained ∧
    ¬ ScoredAbove initialScore .redirected .baseline := by
  refine ⟨score_comparison_transitive initialScore,
    score_comparison_transitive laterScore, ?_, ?_, ?_⟩ <;> decide

theorem diagnostic_fails_transport :
    ¬ (ScoredAbove laterScore .redirected .retained →
       ScoredAbove initialScore .redirected .retained) := by
  decide

end Generative.FormationSequence
