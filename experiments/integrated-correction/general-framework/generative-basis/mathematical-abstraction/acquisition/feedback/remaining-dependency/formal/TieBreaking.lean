import PluralRecords

/-!
Equal chances: what treating the centers alike permits at a tie.

`PluralRecords` showed that no deterministic rule that treats the centers alike
serves a center whose record entry another shares. Here a rule may instead
assign chances: a weight to each center and a weight to withholding (natural
numbers, read as proportions of their total). A lottery *treats the centers
alike* when exchanging two centers' entries exchanges their weights and leaves
the withholding weight unchanged. Results:

* an alike lottery gives tied centers equal weight (`tied_equal_weight`);
* at a full tie (all entries equal) every center has the same weight
  (`full_tie_equal_weights`); if its withholding weight is zero and it puts
  some weight on serving, every center has the same positive weight, which is
  the uniform lottery up to scale (`full_tie_open_uniform`);
* the uniform lottery treats the centers alike on every record
  (`uniform_alike`), and a deterministic choice, read as a lottery with all
  weight on one center, is alike at a full tie of two or more centers only if
  it withholds (`point_mass_not_alike_at_tie`).

So at a full tie, treating the centers alike permits exactly equal weights
for the centers, with any withholding weight; with zero withholding weight it
is the uniform lottery. Alikeness here holds in distribution, before the
draw: a realized draw still serves one center. `Chances` also admits all
weights zero, which is not a lottery; such cases are excluded only where a
theorem assumes a positive weight. Whether an equal chance is
a legitimate way to break the tie, and whether another input (the centers'
agreement, a recorded prior arrival, a further fact about need) should
override it, is not decided here; see `TIE-BREAKING-LEGITIMACY.md`.
-/
namespace TieBreaking
open PluralRecords

/-- Weights for serving each center, and for withholding. -/
structure Chances (n : Nat) where
  serve : Fin n → Nat
  withhold : Nat

abbrev Lottery (n : Nat) := Record n → Chances n

def LotteryAlike {n : Nat} (lot : Lottery n) : Prop :=
  ∀ r r' a b, (∀ k, r' k = r (transpose a b k)) →
    (∀ i, (lot r').serve i = (lot r).serve (transpose a b i)) ∧
      (lot r').withhold = (lot r).withhold

theorem tied_equal_weight {n : Nat} (lot : Lottery n) (alike : LotteryAlike lot)
    (r : Record n) (a b : Fin n) (tie : r a = r b) : (lot r).serve a = (lot r).serve b := by
  have h := (alike r r a b (relabel_of_tie r a b tie)).1 a
  rw [h, transpose_left]

theorem full_tie_equal_weights {n : Nat} (lot : Lottery n) (alike : LotteryAlike lot)
    (r : Record n) (tied : ∀ i j, r i = r j) (i j : Fin n) :
    (lot r).serve i = (lot r).serve j :=
  tied_equal_weight lot alike r i j (tied i j)

/-- At a full tie, a lottery with zero withholding weight that puts weight on
some center gives every center the same positive weight. The zero
withholding weight is what makes this the uniform lottery; equal center
weights hold without it. -/
theorem full_tie_open_uniform {n : Nat} (lot : Lottery n) (alike : LotteryAlike lot)
    (r : Record n) (tied : ∀ i j, r i = r j) (noWithhold : (lot r).withhold = 0)
    (k : Fin n) (pos : 0 < (lot r).serve k) :
    ∀ i, (lot r).serve i = (lot r).serve k ∧ 0 < (lot r).serve i :=
  fun i => ⟨full_tie_equal_weights lot alike r tied i k,
    by rw [full_tie_equal_weights lot alike r tied i k]; exact pos⟩

def uniform (n : Nat) : Lottery n := fun _ => ⟨fun _ => 1, 0⟩

theorem uniform_alike (n : Nat) : LotteryAlike (uniform n) :=
  fun _ _ _ _ _ => ⟨fun _ => rfl, rfl⟩

/-- A deterministic rule read as a lottery: all weight on its choice. -/
def pointMass {n : Nat} (rule : Rule n) : Lottery n := fun r =>
  ⟨fun i => if rule r = some i then 1 else 0, if rule r = none then 1 else 0⟩

theorem point_mass_not_alike_at_tie {n : Nat} (rule : Rule n)
    (alike : LotteryAlike (pointMass rule)) (two : 2 ≤ n) (r : Record n)
    (tied : ∀ i j, r i = r j) : rule r = none := by
  cases hk : rule r with
  | none => rfl
  | some k =>
    exfalso
    obtain ⟨j, hj⟩ := fin_other two k
    have h : (if rule r = some j then 1 else 0) = (if rule r = some k then 1 else 0) :=
      full_tie_equal_weights _ alike r tied j k
    rw [hk, if_neg (fun e => hj (Option.some.inj e).symm), if_pos rfl] at h
    exact nomatch h

end TieBreaking

#print axioms TieBreaking.Chances
#print axioms TieBreaking.LotteryAlike
#print axioms TieBreaking.tied_equal_weight
#print axioms TieBreaking.full_tie_equal_weights
#print axioms TieBreaking.full_tie_open_uniform
#print axioms TieBreaking.uniform
#print axioms TieBreaking.uniform_alike
#print axioms TieBreaking.pointMass
#print axioms TieBreaking.point_mass_not_alike_at_tie
