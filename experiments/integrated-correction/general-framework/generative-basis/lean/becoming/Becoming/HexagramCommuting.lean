import Becoming.Commuting
import Becoming.Hexagrams

/-!
# The Changes as an instance of a commuting law

The instance of `Becoming.Commuting` at the complement of `Becoming.Hexagrams` (錯), split from
that module so the general law imports no instance.

* The complement moves every hexagram (`Hexagram.complement_moves`), and the law of waxing and
  waning commutes with it, so `n` steps never bring a hexagram and its complement to one
  (`Hexagram.waxWane_apart`); its six steps to the complement are the pair halfway round a return
  of twelve (`Hexagram.waxWane_halfway`); and its going alike across the pairs
  (`Hexagram.pairs_goAlike`, in `Becoming.Hexagrams`) is `Commutes.pairs_goAlike`'s instance at
  the complement.
* The law that lets only a broken line enter draws every hexagram into all broken, so it breaks
  the symmetry (`Hexagram.wane_breaks`).
* The change of one line is symmetric under the complement (`Hexagram.changes_symmetric`), and
  every course of changes has a complementary course, never at the same hexagram
  (`Hexagram.changes_mirror_apart`).

**Reading (the AI's; SSBX review G2, decided from the work by D45).** 陰 and 陽 changed line for
line are never merged by 消息; the waning that brings everything to 坤 is the law that breaks 錯.

No ethical predicate, ranking or axiom occurs.
-/

namespace Becoming

open Generative

namespace Hexagram

/-- **The complement moves every hexagram.** -/
theorem complement_moves : Diagonal.Moves Eq complement :=
  fun s same => Diagonal.flip_moves s.l1 ((congrArg Hexagram.l1 same).trans (complement_l1 s))

/-- **Waxing and waning never brings a hexagram and its complement to one.** -/
theorem waxWane_apart (s : Hexagram) (n : Nat) :
    (Law.run waxWane (complement s)).state n ≠ (Law.run waxWane s).state n :=
  Law.Commutes.apart waxWane_complement complement_moves s n

/-- **The six steps to the complement are the pair halfway round a return of twelve.** -/
theorem waxWane_halfway (s : Hexagram) :
    (∀ n, (Law.run waxWane s).state (6 + n) = complement ((Law.run waxWane s).state n)) ∧
      (Law.run waxWane s).state 12 = s :=
  Law.Commutes.paired_halfway waxWane_complement complement_complement (six_steps s)

/-- **Drawing every hexagram into all broken breaks the symmetry.** -/
theorem wane_breaks : ¬ Law.Commutes wane complement :=
  Law.Commutes.breaks complement_moves (x := allBroken) (n := 6)
    ((wane_six (complement allBroken)).trans (wane_six allBroken).symm)

/-- Changing a line commutes with the complement. -/
theorem flip_complement : ∀ (k : Place) (s : Hexagram), flip k (complement s) = complement (flip k s)
  | .p1, ⟨_, _, _, _, _, _⟩ => rfl
  | .p2, ⟨_, _, _, _, _, _⟩ => rfl
  | .p3, ⟨_, _, _, _, _, _⟩ => rfl
  | .p4, ⟨_, _, _, _, _, _⟩ => rfl
  | .p5, ⟨_, _, _, _, _, _⟩ => rfl
  | .p6, ⟨_, _, _, _, _, _⟩ => rfl

/-- **The change of one line is symmetric under the complement.** -/
theorem changes_symmetric : Branching.Symmetric changes complement :=
  fun x k _ step => (congrArg complement step).trans (flip_complement k x).symm

/-- Every course of changes has a complementary course, never at the same hexagram. -/
theorem changes_mirror_apart (r : Run changes) (n : Nat) :
    (Branching.mirror changes_symmetric r).state n ≠ r.state n :=
  Branching.mirror_apart changes_symmetric complement_moves r n

end Hexagram

end Becoming
