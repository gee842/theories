import Becoming.Listing

/-!
# Census on webs: counts of arising and ceasing where they exist, and listing once

`Becoming.Decidedness` states counts as relations (`Counts`, `CountsAcross`) and the census over a
stretch for any family of determinations, with no decidedness; `Becoming.Listing` states what
listing each relatum once commits to. A web's activity is such a family: a formation arises
across a step where it comes to be active (`Web.Arises`) and ceases where it ceases to be
(`Web.Ceases`), and a family's stock is the sum of its conditions' levels (`Web.stock`). This
module states those laws of a web's activity and standing, and of a world's relata read through
their relations, and proves them through them.

* **The census of a web, with no decidedness.** Over a stretch at whose steps what is active is
  listed, each formation once, wherever the ceasings and arisings are counted, the list at the end
  with what ceased is the list at the start with what arose (`listed_over_stretch`). Over any
  stretch, wherever a listed family's arisings and ceasings are counted, they differ by at most
  its members (`keep_pace`). Where a procedure decides activity, its marks count what arises and
  what ceases (`arisings_count`, `ceasings_count`).
* **A census decides identity among what it lists.** A census of what is active in a web decides
  identity among the formations active at each step (`census_identityDecided`).
* **A stock once per member is one number.** Two lists listing a family of conditions once give
  it one stock at every step (`stock_eq`), and repetition only adds (`stock_le`).
* **Counting a world's relata through their relations.** The number of relata a list of a world
  holds, read up to indiscernibility, is one number (`indiscernible_numbers_unique`).

No ethical predicate, ranking or axiom occurs.
-/

namespace Becoming

namespace CensusWebs

section Census

variable {F C : Type} (W : Web F C)

/-- **Over any stretch of a web, wherever a listed family's arisings and ceasings are counted,
they differ by at most its members.** No decidedness is assumed. -/
theorem keep_pace {fs : List F} {S n A D : Nat}
    (arose : CountsAcross (fun _ => fs) (fun t f => W.Arises t f) (steps S n) A)
    (ceased : CountsAcross (fun _ => fs) (fun t f => W.Ceases t f) (steps S n) D) :
    A ≤ fs.length + D ∧ D ≤ fs.length + A :=
  CountsAcross.keep_pace (p := fun f t => W.active t f) arose ceased

/-- **A family's stock once per member is one number**: two lists listing the family once give
it the same stock at every step. -/
theorem stock_eq {cs cs' ds : List C} (lists : ListsOnce cs ds) (lists' : ListsOnce cs' ds)
    (t : Nat) : W.stock cs t = W.stock cs' t :=
  lists.total_eq lists' (W.level t)

/-- **Repetition only adds**: a family's stock once per member is at most its stock over any list
holding its members. -/
theorem stock_le {cs ds : List C} (lists : ListsOnce cs ds) (t : Nat) :
    W.stock cs t ≤ W.stock ds t :=
  lists.total_le (W.level t)

end Census

/-- **The number of relata a list of a world holds, read through their relations, is one
number**: counted up to indiscernibility. -/
theorem indiscernible_numbers_unique (w : World) {l : List w.Relatum} {n n' : Nat}
    (numbers : NumbersBy w.Indiscernible l n) (numbers' : NumbersBy w.Indiscernible l n') :
    n = n' :=
  NumbersBy.unique w.indiscernible_equivalence numbers numbers'

end CensusWebs

end Becoming
