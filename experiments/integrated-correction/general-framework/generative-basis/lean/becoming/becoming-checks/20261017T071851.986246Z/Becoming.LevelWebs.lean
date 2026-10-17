import Becoming.Entropy
import Becoming.Space
import Becoming.Population

/-!
# Level webs: laws of a condition's level and a family's configuration on a web

`Becoming.Change` states that an amount never rising from some step on does not fall at
arbitrarily late steps (`falls_not_recurring_from_floor`); `Becoming.Space` states that it staying
the same from some step on cannot be refuted (`amount_still_unrefuted`); `Becoming.Population`
states that a count balanced across each step is balanced over any stretch
(`balance_over_stretch`); `Becoming.Entropy` lists each way `K` units fall into `n` members exactly
once (`configurations_exact`). A web carries the amounts these laws are about: the level of a
condition at each step (`Web.level`), and a family's configuration, the level of each member
(`Web.config`); a balanced flow changes each level by what it takes and gives. This module states
those laws of a web's levels and proves them through the general laws.

* **A level with a floor.** A condition's level that never rises from some step on does not fall
  at arbitrarily late steps (`level_falls_not_recurring`), and that it stays the same from some step
  on cannot be refuted (`level_still_unrefuted`); no decidedness is needed.
* **A balanced level over a stretch.** In a balanced flow, a condition's level at the end of any
  stretch with everything taken from it is its level at the start with everything given to it
  (`Balances.level_over_stretch`).
* **A family's configuration among the configurations.** A family's configuration is among the
  configurations of its members totalling `K` exactly when its stock is `K`
  (`config_mem_iff`).

No ethical predicate, ranking or axiom occurs.
-/

namespace Becoming

namespace LevelWebs

variable {F C : Type}

/-- **A level that never rises from some step on does not fall at arbitrarily late steps.** -/
theorem level_falls_not_recurring {W : Web F C} {c : C} {T : Nat}
    (still : ∀ n, T ≤ n → ¬ W.Rises n c) : ¬ ∀ N, ∃ n, N ≤ n ∧ W.Falls n c :=
  falls_not_recurring_from_floor (fun t => W.level t c) T
    fun n later => Nat.ge_of_not_lt (still n later)

/-- **That a level never rising from some step on stays the same from some step on cannot be
refuted.** No decidedness is needed. -/
theorem level_still_unrefuted {W : Web F C} {c : C} {T : Nat}
    (still : ∀ n, T ≤ n → ¬ W.Rises n c) :
    ¬ ¬ ∃ M, T ≤ M ∧ ∀ t, M ≤ t → W.level (t + 1) c = W.level t c :=
  amount_still_unrefuted (q := fun t => W.level t c)
    fun n later => Nat.ge_of_not_lt (still n later)

/-- **A balanced level over a stretch.** In a balanced flow, over any stretch, a condition's level
at the end with everything taken from it is its level at the start with everything given to it. -/
theorem Balances.level_over_stretch {L : Flow F C} {W : Web F C} (balances : L.Balances W)
    (c : C) (S n : Nat) :
    W.level (S + n) c + total (steps S n) (fun t => L.taken t c) =
      W.level S c + total (steps S n) (fun t => L.given t c) :=
  balance_over_stretch (q := fun t => W.level t c) (fun t => balances t c) S n

/-- **A family's configuration is among the configurations totalling `K` exactly when its stock is
`K`.** -/
theorem config_mem_iff (W : Web F C) (cs : List C) (t K : Nat) :
    W.config cs t ∈ configurations cs.length K ↔ W.stock cs t = K :=
  ((configurations_exact cs.length K).2 (W.config cs t)).trans
    ⟨fun ⟨_, sum⟩ => (W.config_total cs t).symm.trans sum,
     fun same => ⟨length_of_map (W.level t) cs, (W.config_total cs t).trans same⟩⟩

end LevelWebs

end Becoming
