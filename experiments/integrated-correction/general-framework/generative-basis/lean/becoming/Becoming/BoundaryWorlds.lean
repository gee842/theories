import Becoming.Readings

/-!
# Boundary worlds: the presupposition along what affects what in a world

`Becoming.Readings` restates two results of `Becoming.Boundaries` as a dichotomy: under the
invariance standard, the presupposition that one's own continuation has significance holds as the
boundary is drawn somewhere exactly where the continuation of everything has significance from
that standpoint (`presupposition_iff_all_of_invariant`), and a rival bounded by a region holding
the self's closure meets the standard exactly where the region is everything
(`bounded_invariant_iff`). Both are stated there for any relation between formations. This module
states them for the relation of a world: its relata, related where one exchanges with a condition
the other depends on (`Flow.Affects` of the world's flow and web), with boundaries closed under it
(`Boundary`) and the closure its reach (`Flow.WithinReach`).

* **Within some boundary is for everything.** In every world, where the presupposition drawn along
  affecting at a standpoint's center is boundary-invariant, it holds as the boundary is drawn
  somewhere exactly when the continuation of every relatum has significance from that standpoint
  at every step (`presupposition_iff_all`).
* **A bounded rival meets the standard only as everything.** In every world, a significance
  bounded by a region holding the center's reach meets the invariance standard along affecting
  exactly where the region holds every relatum (`bounded_invariant_iff`).

The significance enters only as a predicate the theorems quantify over; nothing here asserts that
it meets the standard or that the presupposition holds. No ethical predicate, ranking or axiom
occurs.
-/

namespace Becoming

namespace BoundaryWorlds

variable {Pos : Type}

/-- **In every world, under invariance along affecting, the presupposition holding within some
boundary is significance for every relatum.** -/
theorem presupposition_iff_all (w : World) {center : Pos → w.Relatum}
    {sig : Pos → Nat → w.Relatum → Prop} {p : Pos}
    (invariant : BoundaryInvariant (Boundary (w.flow.Affects w.web) (center p))
      (SignificantWithin sig p)) :
    SubTrue (Boundary (w.flow.Affects w.web) (center p)) (SignificantWithin sig p) ↔
      ∀ t g, sig p t g :=
  presupposition_iff_all_of_invariant (Boundary.whole (center p)) invariant

/-- **In every world, a rival bounded by a region holding the center's reach meets the standard
along affecting exactly where the region holds every relatum.** -/
theorem bounded_invariant_iff (w : World) {center : Pos → w.Relatum}
    {region : Pos → w.Relatum → Prop} {p : Pos}
    (holds : ∀ g, w.flow.WithinReach w.web (center p) g → region p g) :
    BoundaryInvariant (Boundary (w.flow.Affects w.web) (center p))
        (SignificantWithin (bounded region) p) ↔
      ∀ g, region p g :=
  Becoming.bounded_invariant_iff holds

end BoundaryWorlds

end Becoming
