import Becoming.Boundaries

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

Declarations moved here unchanged, with their names, from `Becoming.Readings` (board item W): see
the sections so headed.
-/

/-! ## The presupposition as a dichotomy (moved from `Becoming.Readings`) -/

namespace Becoming

variable {F C Pos : Type}

/-- Under invariance the presupposition is the continuation condition at that standpoint: wherever the whole is
admissible and the presupposition is boundary-invariant, it holds as the boundary is drawn
somewhere exactly when the continuation of everything has significance from `p`. A restatement of
`boundaryInvariant_iff_conditional`. -/
theorem presupposition_iff_all_of_invariant {admissible : (F → Prop) → Prop}
    (whole : admissible fun _ => True) {sig : Pos → Nat → F → Prop} {p : Pos}
    (invariant : BoundaryInvariant admissible (SignificantWithin sig p)) :
    SubTrue admissible (SignificantWithin sig p) ↔ ∀ t g, sig p t g :=
  ⟨(boundaryInvariant_iff_conditional whole).mp invariant,
   fun all => ⟨_, whole, fun g _ t => all t g⟩⟩

/-- A rival bounded by a region holding the self's closure meets the standard exactly where the
region is everything: along a relation, its presupposition is invariant exactly where the region
holds every formation. A case of `boundaryInvariant_iff_all`. -/
theorem bounded_invariant_iff {rel : F → F → Prop} {center : Pos → F} {region : Pos → F → Prop}
    {p : Pos} (holds : ∀ g, WithinClosure rel (center p) g → region p g) :
    BoundaryInvariant (Boundary rel (center p)) (SignificantWithin (bounded region) p) ↔
      ∀ g, region p g :=
  (boundaryInvariant_iff_all (Boundary.whole (center p))
      ⟨_, Boundary.closure (center p), fun g within _ => holds g within⟩).trans
    ⟨fun all g => all 0 g, fun all _ g => all g⟩

end Becoming


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

end BoundaryWorlds

end Becoming
