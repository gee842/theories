import Becoming.Boundaries
import Becoming.Interdependence

/-!
# Boundary flows: the self's boundaries drawn along what a flow relates

`Becoming.Boundaries` states, along any relation among formations, the boundaries of a
formation's self (`Boundary`: a region holding the formation, closed under the relation), truth
however the boundary is drawn (`SuperTrue`, `SubTrue`, `BoundaryInvariant`), and the self's
presupposition (`SignificantWithin`) with the decomposition of the continuation condition through
it. A flow and its web form the relations it is drawn along: feeding (`Flow.FedFrom`), affecting
(`Flow.Affects`, whose closure is the reach closure `Flow.WithinReach`) and sharing a condition
(`Flow.Shares`, whose closure is the system `Flow.WithinSystem`). This module states the laws of
`Becoming.Boundaries` for the boundaries drawn along a flow's relations, and proves them through
those laws. Every closed region holding the center, the whole included, counts as a drawing of the
self, as in `Becoming.Boundaries`.

* **The scope of “within the self”, along affecting.** Every formation lies within the self as its
  boundary is drawn somewhere (`subTrue_member`); wherever the whole is a drawing, “everything
  within the self has a property” is super-true exactly when everything has it
  (`superTrue_all_iff`); significance bounded by each center's reach closure is the significance of
  what lies within the self however its boundary is drawn (`bounded_reach_iff`). The operator
  “however the boundary is drawn” at narrow scope gives the presupposition sub-true, at wide scope
  the continuation condition at that standpoint (`reach_scopes`). Sub-true along affecting, the
  presupposition gives the center's own continuation significance (`own_continuation`).
* **Super-truth, whatever the flow's relation.** The continuation condition is the presupposition
  held however each self's boundary is drawn along affecting (`unrestricted_iff_superTrue`), and the
  presupposition is super-true drawn along feeding exactly when drawn along sharing a condition
  (`superTrue_level_free`).
* **Where the system is the whole.** Under one condition every formation takes part in, the whole
  is the only boundary of a self drawn along sharing a condition (`only_whole_of_common`), and the
  presupposition drawn along sharing is the presupposition drawn along everything
  (`shares_iff_total_of_common`).
* **The step, along affecting.** Invariance of the presupposition is its determinacy
  (`boundaryInvariant_iff_determinate`) and its extension to the whole
  (`boundaryInvariant_iff_extends`); invariant, it is nowhere true where some continuation lacks
  significance (`not_subTrue_of_invariant`). Sub-true and invariant at every standpoint, it gives
  the continuation condition (`unrestricted_of_presupposed`); with every formation within some
  center's reach closure, invariance is standpoint-invariance
  (`boundaryInvariant_iff_standpointInvariant`); and the premises give living significance at the
  level of claims on every reading by continuations (`significant_of_presupposed`).
* **The whole as region.** Under significance bounded by the whole, retaining what has significance
  along a web is inclusion (`retains_whole_iff_includes`).

The presupposition, covering and invariance remain premises, as in `Becoming.Boundaries`; nothing
here derives them. Significance is supplied, as every significance is; no ranking or axiom occurs.
-/

namespace Becoming

namespace BoundaryFlows

variable {F C Pos : Type}

section Drawn

variable (L : Flow F C) (W : Web F C)

/-! ## The scope of “within the self”, along affecting -/

/-- **Every formation lies within the self as drawn somewhere along affecting**: at the whole. -/
theorem subTrue_member (f g : F) : SubTrue (Boundary (L.Affects W) f) (fun region => region g) :=
  Becoming.subTrue_member f g

/-- **Along affecting, “everything within the self has the property” is super-true exactly when
everything has it.** -/
theorem superTrue_all_iff (f : F) {s : F → Prop} :
    SuperTrue (Boundary (L.Affects W) f) (fun region => ∀ g, region g → s g) ↔ ∀ g, s g :=
  Becoming.superTrue_all_iff (Boundary.whole f)

/-- **Significance bounded by each center's reach closure is the significance of what lies within
the self however its boundary is drawn along affecting.** -/
theorem bounded_reach_iff (center : Pos → F) (p : Pos) (t : Nat) (g : F) :
    bounded (fun q => L.WithinReach W (center q)) p t g ↔
      SuperTrue (Boundary (L.Affects W) (center p)) (fun region => region g) :=
  bounded_closure_iff (L.Affects W) center p t g

/-- **The two scopes, along affecting.** From standpoint `p`, “whatever lies definitely within the
self has significance” is the presupposition sub-true along affecting; “however the boundary is
drawn along affecting, everything within the self has significance” is the continuation of
everything having significance from `p`. -/
theorem reach_scopes (f : F) (sig : Pos → Nat → F → Prop) (p : Pos) :
    ((∀ t g, SuperTrue (Boundary (L.Affects W) f) (fun region => region g) → sig p t g) ↔
        SubTrue (Boundary (L.Affects W) f) (SignificantWithin sig p)) ∧
      (SuperTrue (Boundary (L.Affects W) f) (SignificantWithin sig p) ↔ ∀ t g, sig p t g) :=
  presupposition_scopes (L.Affects W) f sig p

/-! ## Super-truth, whatever the flow's relation -/

/-- **The continuation condition is the presupposition held however each self's boundary is drawn
along affecting.** -/
theorem unrestricted_iff_superTrue (center : Pos → F) {sig : Pos → Nat → F → Prop} :
    Unrestricted sig ↔
      ∀ p, SuperTrue (Boundary (L.Affects W) (center p)) (SignificantWithin sig p) :=
  Becoming.unrestricted_iff_superTrue (L.Affects W) center

/-- **Super-truth drawn along feeding is super-truth drawn along sharing a condition.** -/
theorem superTrue_level_free (f : F) (sig : Pos → Nat → F → Prop) (p : Pos) :
    SuperTrue (Boundary (L.FedFrom W) f) (SignificantWithin sig p) ↔
      SuperTrue (Boundary (L.Shares W) f) (SignificantWithin sig p) :=
  Becoming.superTrue_level_free (L.FedFrom W) (L.Shares W) f sig p

/-! ## The step, along affecting -/

/-- **Along affecting, invariance is determinacy**: the presupposition is invariant across the
boundaries drawn along affecting exactly when, sub-true, it is super-true. -/
theorem boundaryInvariant_iff_determinate {f : F} {sig : Pos → Nat → F → Prop} {p : Pos} :
    BoundaryInvariant (Boundary (L.Affects W) f) (SignificantWithin sig p) ↔
      (SubTrue (Boundary (L.Affects W) f) (SignificantWithin sig p) →
        SuperTrue (Boundary (L.Affects W) f) (SignificantWithin sig p)) :=
  Becoming.boundaryInvariant_iff_determinate

/-- **Along affecting, invariance is extension to the whole**: holding as the boundary is drawn
anywhere along affecting, the presupposition holds as it is drawn at the whole. -/
theorem boundaryInvariant_iff_extends {f : F} {sig : Pos → Nat → F → Prop} {p : Pos} :
    BoundaryInvariant (Boundary (L.Affects W) f) (SignificantWithin sig p) ↔
      ∀ region, Boundary (L.Affects W) f region → SignificantWithin sig p region →
        SignificantWithin sig p fun _ => True :=
  Becoming.boundaryInvariant_iff_extends (Boundary.whole f)

end Drawn

section Related

variable {L : Flow F C} {W : Web F C}

/-! ## The center's own continuation -/

/-- **The presupposition drawn along affecting gives the center's own continuation significance.**
-/
theorem own_continuation {f : F} {sig : Pos → Nat → F → Prop} {p : Pos}
    (presupposed : SubTrue (Boundary (L.Affects W) f) (SignificantWithin sig p)) :
    ∀ t, sig p t f :=
  subTrue_empty_iff.mp (subTrue_of_larger (rel := fun _ _ => False) (fun _ _ no => no.elim)
    presupposed)

/-! ## Where the system is the whole -/

/-- **Under a common condition the whole is the only boundary drawn along sharing.** Where every
formation takes part in one condition, every boundary of a self along sharing a condition holds
every formation. -/
theorem only_whole_of_common {c : C} (common : ∀ g, L.TakesPart W g c) {f : F}
    {region : F → Prop} (boundary : Boundary (L.Shares W) f region) : ∀ g, region g :=
  Boundary.only_whole (Flow.system_whole_of_common common f) boundary

/-- **Under a common condition, drawing the self along sharing is drawing it along everything.**
Where every formation takes part in one condition, the presupposition is sub-true along sharing a
condition exactly when it is sub-true along the total relation. -/
theorem shares_iff_total_of_common {c : C} (common : ∀ g, L.TakesPart W g c) {f : F}
    {sig : Pos → Nat → F → Prop} {p : Pos} :
    SubTrue (Boundary (L.Shares W) f) (SignificantWithin sig p) ↔
      SubTrue (Boundary (fun _ _ => True) f) (SignificantWithin sig p) :=
  ⟨fun sub => subTrue_total_iff.mpr fun t g =>
     subTrue_significantWithin_iff.mp sub t g (Flow.system_whole_of_common common f g),
   (Flow.presupposition_order (L := L) (W := W)).1⟩

/-! ## The step from the presupposition -/

/-- **Invariant along affecting, the presupposition holds nowhere where some continuation lacks
significance.** -/
theorem not_subTrue_of_invariant {f : F} {sig : Pos → Nat → F → Prop} {p : Pos}
    (invariant : BoundaryInvariant (Boundary (L.Affects W) f) (SignificantWithin sig p))
    {t : Nat} {g : F} (lacks : ¬ sig p t g) :
    ¬ SubTrue (Boundary (L.Affects W) f) (SignificantWithin sig p) :=
  Becoming.not_subTrue_of_invariant (Boundary.whole f) invariant lacks

/-- **The continuation condition from the presupposition along affecting.** Where each standpoint's
presupposition is sub-true and invariant across the boundaries of its center's self drawn along
affecting, nothing restricts significance. Every formation lies within the whole, a drawing of every
self. -/
theorem unrestricted_of_presupposed {center : Pos → F} {sig : Pos → Nat → F → Prop}
    (presupposed : ∀ p, SubTrue (Boundary (L.Affects W) (center p)) (SignificantWithin sig p))
    (invariant : ∀ p, BoundaryInvariant (Boundary (L.Affects W) (center p))
      (SignificantWithin sig p)) :
    Unrestricted sig :=
  Becoming.unrestricted_of_presupposed (fun p _ => ⟨_, Boundary.whole (center p), trivial⟩)
    presupposed invariant

/-- **Along affecting, invariance across boundaries is invariance across standpoints.** Where every
formation lies within some center's reach closure and every standpoint's presupposition is sub-true
along affecting, the presupposition is invariant across each self's boundaries exactly when
significance is standpoint-invariant. -/
theorem boundaryInvariant_iff_standpointInvariant {center : Pos → F}
    (centers : ∀ g, ∃ q, L.WithinReach W (center q) g) {sig : Pos → Nat → F → Prop}
    (presupposed : ∀ p, SubTrue (Boundary (L.Affects W) (center p)) (SignificantWithin sig p)) :
    (∀ p, BoundaryInvariant (Boundary (L.Affects W) (center p)) (SignificantWithin sig p)) ↔
      StandpointInvariant sig :=
  Becoming.boundaryInvariant_iff_standpointInvariant centers presupposed

/-- **Living significance at the level of claims, from the premises along affecting**, on every
reading in which a claim's significance from a standpoint is that of some formation's continuation
at some step. -/
theorem significant_of_presupposed {Q : Type} {V : Valuation Pos Q} {center : Pos → F}
    {sig : Pos → Nat → F → Prop}
    (premises : ∀ p, SubTrue (Boundary (L.Affects W) (center p)) (SignificantWithin sig p) ∧
      BoundaryInvariant (Boundary (L.Affects W) (center p)) (SignificantWithin sig p))
    (formation : Q → F) (step : Q → Nat) (reads : ∀ p c, sig p (step c) (formation c) → V.sig p c) :
    V.Significant :=
  Valuation.significant_of_presupposed (fun p => Boundary.whole (center p)) premises formation step
    reads

end Related

/-! ## The whole as region -/

/-- **Under significance bounded by the whole, retaining is inclusion**: along a web, `l` retains
what has significance along `l'` from any standpoint exactly when it includes what `l'` admits. -/
theorem retains_whole_iff_includes (W : Web F C) (p : Pos) {l l' : Nat → C → Nat} :
    W.Retains (bounded fun (_ : Pos) (_ : F) => True) p l l' ↔ W.Includes l l' :=
  Web.retains_iff_includes bounded_whole p

end BoundaryFlows

end Becoming
