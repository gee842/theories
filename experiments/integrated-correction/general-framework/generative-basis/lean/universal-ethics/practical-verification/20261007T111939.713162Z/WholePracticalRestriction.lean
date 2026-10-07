/-!
# Whole comparisons and their situated restrictions

This is a representation audit for the universal-grounding investigation.
`Whole` represents complete continuations at the declared scope. `Index` and
each option domain describe differentiated decision positions within that same
process; they are not independent substances or primitive owners. Their actual
formation, the completeness of each realization, and the ethical warrant of a
comparison are not derived by this module.

The local relation is a contextual comparison of two options. It is neither an
agent's endorsement nor a complete inventory of pro tanto reasons. Descent means
agreement with one whole relation. Proving the exact conditions for descent does
not establish that every practical comparison morally ought to descend.

No order, scalar aggregation, fixed objective, universal interaction, identical
command, or actual compliance is assumed. A whole relation need not be complete.
Pair coverage differs from representing every continuation individually. Even
compatible locally strict comparisons can form a global cycle. Recoding results
require preserved realizations; substantive self-modification need not do that.

All declarations use only constructive Lean core logic. There are no custom
axioms, classical choice, quotient axioms, or proof irrelevance dependencies.
-/

namespace WholePracticalRestriction

universe u v w

structure Family (Whole : Type u) (Index : Type v) where
  Option : Index → Type w
  realize : (i : Index) → Option i → Whole
  compare : (i : Index) → Option i → Option i → Prop

def Compatible {Whole : Type u} {Index : Type v}
    (family : Family.{u, v, w} Whole Index) : Prop :=
  ∀ i j (a b : family.Option i) (c d : family.Option j),
    family.realize i a = family.realize j c →
    family.realize i b = family.realize j d →
    (family.compare i a b ↔ family.compare j c d)

def Descends {Whole : Type u} {Index : Type v}
    (family : Family.{u, v, w} Whole Index) (whole : Whole → Whole → Prop) : Prop :=
  ∀ i a b, family.compare i a b ↔ whole (family.realize i a) (family.realize i b)

def Joined {Whole : Type u} {Index : Type v}
    (family : Family.{u, v, w} Whole Index) (x y : Whole) : Prop :=
  ∃ i a b, family.realize i a = x ∧ family.realize i b = y ∧ family.compare i a b

def CoveredPair {Whole : Type u} {Index : Type v}
    (family : Family.{u, v, w} Whole Index) (x y : Whole) : Prop :=
  ∃ i a b, family.realize i a = x ∧ family.realize i b = y

def PointCoverage {Whole : Type u} {Index : Type v}
    (family : Family.{u, v, w} Whole Index) : Prop :=
  ∀ x, ∃ i a, family.realize i a = x

def PairCoverage {Whole : Type u} {Index : Type v}
    (family : Family.{u, v, w} Whole Index) : Prop :=
  ∀ x y, CoveredPair family x y

def Irreflexive {A : Type u} (relation : A → A → Prop) : Prop :=
  ∀ a, ¬ relation a a

def Transitive {A : Type u} (relation : A → A → Prop) : Prop :=
  ∀ a b c, relation a b → relation b c → relation a c

theorem descent_implies_compatibility {Whole : Type u} {Index : Type v}
    {family : Family.{u, v, w} Whole Index} {whole : Whole → Whole → Prop}
    (descent : Descends family whole) : Compatible family := by
  intro i j a b c d left right
  have transported :
      whole (family.realize i a) (family.realize i b) ↔
        whole (family.realize j c) (family.realize j d) := by
    exact Iff.of_eq ((congrArg (fun x => whole x (family.realize i b)) left).trans
      (congrArg (fun y => whole (family.realize j c) y) right))
  exact (descent i a b).trans (transported.trans (descent j c d).symm)

theorem joined_descends_iff_compatible {Whole : Type u} {Index : Type v}
    (family : Family.{u, v, w} Whole Index) :
    Descends family (Joined family) ↔ Compatible family := by
  constructor
  · exact descent_implies_compatibility
  · intro compatibility i a b
    constructor
    · intro localProof
      exact ⟨i, a, b, rfl, rfl, localProof⟩
    · intro joined
      obtain ⟨j, c, d, left, right, localProof⟩ := joined
      exact (compatibility j i c d a b left right).mp localProof

theorem compatibility_iff_common_whole_relation {Whole : Type u} {Index : Type v}
    (family : Family.{u, v, w} Whole Index) :
    Compatible family ↔ ∃ whole, Descends family whole := by
  constructor
  · intro compatibility
    exact ⟨Joined family, (joined_descends_iff_compatible family).mpr compatibility⟩
  · intro existence
    obtain ⟨whole, descent⟩ := existence
    exact descent_implies_compatibility descent

/-- Existential gluing makes a least extension; no decision on unrepresented
    comparisons, and no ethical priority, is furnished by that construction. -/
theorem joined_is_least_extension {Whole : Type u} {Index : Type v}
    {family : Family.{u, v, w} Whole Index} {whole : Whole → Whole → Prop}
    (descent : Descends family whole) {x y : Whole}
    (joined : Joined family x y) : whole x y := by
  obtain ⟨i, a, b, left, right, localProof⟩ := joined
  cases left
  cases right
  exact (descent i a b).mp localProof

theorem extensions_agree_on_covered_pairs {Whole : Type u} {Index : Type v}
    {family : Family.{u, v, w} Whole Index} {first second : Whole → Whole → Prop}
    (firstDescent : Descends family first) (secondDescent : Descends family second)
    {x y : Whole} (coverage : CoveredPair family x y) : first x y ↔ second x y := by
  obtain ⟨i, a, b, left, right⟩ := coverage
  cases left
  cases right
  exact (firstDescent i a b).symm.trans (secondDescent i a b)

theorem pair_coverage_gives_unique_comparisons {Whole : Type u} {Index : Type v}
    {family : Family.{u, v, w} Whole Index} {first second : Whole → Whole → Prop}
    (coverage : PairCoverage family)
    (firstDescent : Descends family first) (secondDescent : Descends family second) :
    ∀ x y, first x y ↔ second x y := by
  intro x y
  exact extensions_agree_on_covered_pairs firstDescent secondDescent (coverage x y)

theorem uncovered_pair_has_disagreeing_extensions {Whole : Type u} {Index : Type v}
    {family : Family.{u, v, w} Whole Index}
    (compatibility : Compatible family) {x y : Whole}
    (uncovered : ¬ CoveredPair family x y) :
    ∃ first second, Descends family first ∧ Descends family second ∧
      ¬ first x y ∧ second x y := by
  let second := fun a b => Joined family a b ∨ (a = x ∧ b = y)
  have firstDescent := (joined_descends_iff_compatible family).mpr compatibility
  have secondDescent : Descends family second := by
    intro i a b
    constructor
    · intro localProof
      exact Or.inl ((firstDescent i a b).mp localProof)
    · intro comparison
      cases comparison with
      | inl joined => exact (firstDescent i a b).mpr joined
      | inr equalities =>
          exact False.elim (uncovered ⟨i, a, b, equalities.1, equalities.2⟩)
  refine ⟨Joined family, second, firstDescent, secondDescent, ?_, ?_⟩
  · intro joined
    obtain ⟨i, a, b, left, right, _⟩ := joined
    exact uncovered ⟨i, a, b, left, right⟩
  · exact Or.inr ⟨rfl, rfl⟩

def singletonCharts : Family Bool Bool where
  Option := fun _ => Unit
  realize := fun i _ => i
  compare := fun _ _ _ => False

theorem point_coverage_does_not_give_pair_coverage :
    PointCoverage singletonCharts ∧ Compatible singletonCharts ∧
      ¬ CoveredPair singletonCharts false true := by
  refine ⟨?_, ?_, ?_⟩
  · intro x
    exact ⟨x, (), rfl⟩
  · intro _ _ _ _ _ _ _ _
    exact Iff.rfl
  · intro covered
    obtain ⟨i, _, _, left, right⟩ := covered
    have impossible : false = true := left.symm.trans right
    cases impossible

/-- A recoding may duplicate options, omit options or use another chart. Its
    comparison is invariant only where both actual realizations are preserved. -/
theorem faithful_recoding_preserves_comparison {Whole : Type u}
    {Index : Type v} {family : Family.{u, v, w} Whole Index}
    {whole : Whole → Whole → Prop} (descent : Descends family whole)
    {i j : Index} {a b : family.Option i} {c d : family.Option j}
    (left : family.realize i a = family.realize j c)
    (right : family.realize i b = family.realize j d) :
    family.compare i a b ↔ family.compare j c d :=
  descent_implies_compatibility descent i j a b c d left right

theorem strict_whole_relation_restricts {Whole : Type u} {Index : Type v}
    {family : Family.{u, v, w} Whole Index} {whole : Whole → Whole → Prop}
    (descent : Descends family whole)
    (irreflexive : Irreflexive whole) (transitive : Transitive whole) :
    ∀ i, Irreflexive (family.compare i) ∧ Transitive (family.compare i) := by
  intro i
  constructor
  · intro a comparison
    exact irreflexive _ ((descent i a a).mp comparison)
  · intro a b c first second
    exact (descent i a c).mpr (transitive _ _ _
      ((descent i a b).mp first) ((descent i b c).mp second))

inductive Three where
  | a | b | c
  deriving DecidableEq

def cycleNext : Three → Three
  | .a => .b
  | .b => .c
  | .c => .a

def cycleCharts : Family Three Three where
  Option := fun _ => Bool
  realize := fun i flag => if flag then cycleNext i else i
  compare := fun _ left right => left = false ∧ right = true

def cycleWhole (x y : Three) : Prop := y = cycleNext x

theorem cycle_charts_descend : Descends cycleCharts cycleWhole := by
  intro i left right
  cases i <;> cases left <;> cases right <;>
    dsimp [cycleCharts, cycleWhole, cycleNext] <;> decide

/-- Three individually strict, compatible charts have no common strict-order
    extension: local consistency is not sufficient for a whole ethical order. -/
theorem locally_strict_compatible_cycle_has_no_strict_extension :
    Compatible cycleCharts ∧
      (∀ i, Irreflexive (cycleCharts.compare i) ∧ Transitive (cycleCharts.compare i)) ∧
      ¬ ∃ whole, Descends cycleCharts whole ∧ Irreflexive whole ∧ Transitive whole := by
  refine ⟨descent_implies_compatibility cycle_charts_descend, ?_, ?_⟩
  · intro i
    constructor
    · intro a comparison
      have impossible : false = true := comparison.1.symm.trans comparison.2
      cases impossible
    · intro a b c first second
      have impossible : false = true := second.1.symm.trans first.2
      cases impossible
  · intro extension
    obtain ⟨whole, descent, irreflexive, transitive⟩ := extension
    have ab : whole Three.a Three.b := (descent Three.a false true).mp ⟨rfl, rfl⟩
    have bc : whole Three.b Three.c := (descent Three.b false true).mp ⟨rfl, rfl⟩
    have ca : whole Three.c Three.a := (descent Three.c false true).mp ⟨rfl, rfl⟩
    exact irreflexive Three.a (transitive _ _ _ (transitive _ _ _ ab bc) ca)

/-- Exact formal limitation of the weak signature. Even strictness of an
    independently offered practical relation does not supply correspondence.
    This is not a rival to a richer constitutive account unless that account's
    independent content is represented and retained. -/
theorem whole_comparison_and_strictness_do_not_force_correspondence
    {Whole : Type u} {Option : Type v} (realize : Option → Whole)
    {whole : Whole → Whole → Prop}
    (irreflexive : Irreflexive whole) (transitive : Transitive whole)
    {a b : Option} (favorable : whole (realize a) (realize b)) :
    ∃ first second : Option → Option → Prop,
      Irreflexive first ∧ Transitive first ∧
      Irreflexive second ∧ Transitive second ∧
      first a b ∧ ¬ second a b := by
  let first := fun x y => whole (realize x) (realize y)
  let second := fun _ _ : Option => False
  refine ⟨first, second, ?_, ?_, ?_, ?_, favorable, ?_⟩
  · intro x
    exact irreflexive (realize x)
  · intro x y z left right
    exact transitive _ _ _ left right
  · intro _ impossible
    exact impossible
  · intro _ _ _ impossible _
    exact False.elim impossible
  · intro impossible
    exact impossible

end WholePracticalRestriction
