import Std

/-
Conditional diagnostics for aggregation across changing alternatives.
The three tiers and counts below are supplied descriptions of distinct protection.
The numeric scores are a test rule, not ethical values. Mathematical failure of
that rule neither refutes G0/J nor establishes unrestricted aggregation.
The final theorem separates padding and composition assumptions; their actual
ethical applicability requires warranted joint realization and interchangeability.
-/
namespace AggregationContext

structure Protection where
  lower : Nat
  middle : Nat
  higher : Nat
  deriving DecidableEq

def Included (a b : Protection) : Prop :=
  a.lower ≤ b.lower ∧ a.middle ≤ b.middle ∧ a.higher ≤ b.higher

def fixedScore (p : Protection) : Nat := p.lower + 3 * p.middle + 5 * p.higher

/-- A strongest-tier cutoff erases lower-tier contributions in both options. -/
def filteredScore (a b p : Protection) : Nat :=
  (if a.higher + b.higher = 0 then p.lower else 0) +
    3 * p.middle + 5 * p.higher

def FilterPref (a b : Protection) : Prop :=
  filteredScore a b b < filteredScore a b a

def original : Protection := ⟨7, 0, 0⟩
def improved : Protection := ⟨7, 0, 1⟩
def alternative : Protection := ⟨0, 2, 0⟩
def population : Protection := ⟨7, 2, 1⟩

/-- All options concern one fixed population; only one route gains protection. -/
theorem fixed_population_upgrade :
    Included original population ∧ Included alternative population ∧
    Included improved population ∧ Included original improved ∧
    original.lower = improved.lower ∧ original.middle = improved.middle ∧
    original.higher < improved.higher := by
  unfold Included
  decide

/-- The diagnostic reverses after an actual increase, not a renamed record. -/
theorem strongest_cutoff_reverses :
    FilterPref original alternative ∧ FilterPref alternative improved := by
  unfold FilterPref
  decide

/-- The reversal is introduced by filtering, not the fixed positive score. -/
theorem unfiltered_control :
    fixedScore alternative < fixedScore original ∧
    fixedScore original < fixedScore improved := by decide

theorem fixed_score_preserves_inclusion (a b : Protection) (h : Included a b) :
    fixedScore a ≤ fixedScore b := by
  rcases h with ⟨hl, hm, hh⟩
  unfold fixedScore
  exact Nat.add_le_add (Nat.add_le_add hl (Nat.mul_le_mul_left 3 hm))
    (Nat.mul_le_mul_left 5 hh)

/-- No fixed transitive strict comparison can retain all three diagnoses. -/
theorem no_fixed_strict_extension
    (r : Protection → Protection → Prop)
    (irrefl : ∀ a, ¬ r a a)
    (trans : ∀ a b c, r a b → r b c → r a c)
    (upgrade : r improved original)
    (before : r original alternative)
    (after : r alternative improved) : False := by
  exact irrefl improved (trans improved alternative improved
    (trans improved original alternative upgrade before) after)

/-- A standard cancellation/composition obstruction, with every premise exposed.
It establishes no unrestricted-aggregation theorem and assumes no ethical score. -/
theorem padding_composition_obstruction {A : Type}
    (join : A → A → A) (comm : ∀ a b, join a b = join b a)
    (r : A → A → Prop) (asymm : ∀ a b, r a b → ¬ r b a)
    (padding : ∀ a b c, r a b → r (join a c) (join b c))
    (compose : ∀ a b c d, r a b → r c d → r (join a c) (join b d))
    (higher middle lower : A)
    (middle_over_higher : r middle higher)
    (lower_over_middle : r lower middle)
    (higher_over_lower : r higher lower) : False := by
  have forward := padding higher lower middle higher_over_lower
  have backward := compose middle higher lower middle
    middle_over_higher lower_over_middle
  rw [comm middle lower] at backward
  exact asymm (join higher middle) (join lower middle) forward backward

end AggregationContext
