import Becoming.Parting

/-!
# Selection along runs: a selection through a run's course through a map

`Becoming.Selection` states what a selection through a map of the alternatives can separate: an
entry per alternative, a selection through the map exchanging what it selects when two
alternatives' entries are exchanged (`Relabel.Equivariant`, `Relabel.EquivariantValue`,
`Relabel.EquivariantChoice`). `Becoming.Learning` states that such a selection is right about what
matters only where what matters goes alike across the map's lumping. This module reads the
alternatives as the moments of a run of any process and the map of them as the values of a map
`reg` at each of them: the run's course through the map (`Parting.course`). The laws are then laws
of the run: of which of its moments any selection through its course through the map can tell
apart.

* **A selection through the course separates exactly what the map separates.** Two moments of a
  run are selected alike by every selection through its course through the map exactly when the
  map takes one value at them (`selected_alike_iff`), and valued alike by every valuation
  through it exactly then (`valued_alike_iff`). A moment is singled out by some selection of at
  most one moment exactly when no other moment takes its value (`singled_iff_untied`); a choice
  of one moment chooses only such a moment (`choice_untied`).
* **Where a run takes one value throughout, nothing is singled out.** On such a run, as on
  a run at rest, every valuation through the course values all moments alike
  (`values_alike_of_constant`) and every choice of one moment through it withholds
  (`choice_withholds_of_constant`). The moments a valuation gives one value are selected alike
  where they take one value through the map (`value_level_alike`).
* **Right about a feature only where the feature goes alike across the map's lumping.** A
  selection or valuation through the course is through the lumping the map makes along the run
  (`selects_through_coupling`, `values_lumped`). Where a feature on configurations separates two
  moments the map lumps, no selection through the course selects exactly the moments meeting it,
  and no valuation through it gives each moment its value (`selects_not_right_of_parted`,
  `values_not_right_of_parted`); where the feature is read off the map, reading it through the
  course is right (`selects_right_of_reads`, `values_right_of_reads`).

No ethical predicate, ranking or axiom occurs.
-/

namespace Becoming

open Generative

universe u v w x

namespace SelectionRuns

open Relabel

section Moments

variable {S : Type u} {A : Type v} {V : Type w} {P : Process S A}

/-- **Two moments of a run are selected alike by every selection through its course through the
map exactly when the map takes one value at them.** -/
theorem selected_alike_iff (reg : S → V) (r : Run P) {j k : Nat} :
    (∀ select : (Nat → V) → Nat → Prop, Equivariant select →
      (select (Parting.course reg r) j ↔ select (Parting.course reg r) k)) ↔
      reg (r.state j) = reg (r.state k) :=
  Relabel.selected_alike_iff

/-- **Two moments of a run are valued alike by every valuation through its course through the
map exactly when the map takes one value at them.** -/
theorem valued_alike_iff (reg : S → V) (r : Run P) {j k : Nat} :
    (∀ value : (Nat → V) → Nat → V, EquivariantValue value →
      value (Parting.course reg r) j = value (Parting.course reg r) k) ↔
      reg (r.state j) = reg (r.state k) :=
  Relabel.valued_alike_iff

/-- **A moment of a run is singled out exactly where the map sets it apart from every other.**
Some selection through the course, selecting at most one moment at each course, selects `k`
exactly when no other moment of the run takes `k`'s value through the map. -/
theorem singled_iff_untied (reg : S → V) (r : Run P) {k : Nat} :
    (∃ select : (Nat → V) → Nat → Prop, Equivariant select ∧
      (∀ m i i', select m i → select m i' → i = i') ∧ select (Parting.course reg r) k) ↔
      ∀ j, j ≠ k → reg (r.state j) ≠ reg (r.state k) :=
  Relabel.singled_iff_untied

/-- **A choice of one moment through the course chooses a moment the map sets apart from every
other.** -/
theorem choice_untied {rule : (Nat → V) → Option Nat} (equivariant : EquivariantChoice rule)
    {reg : S → V} {r : Run P} {k : Nat} (chosen : rule (Parting.course reg r) = some k) :
    ∀ j, j ≠ k → reg (r.state j) ≠ reg (r.state k) :=
  equivariant.untied chosen

/-- **Along a run taking one value throughout, a choice of one moment through the course
withholds.** So it does along a run at rest. -/
theorem choice_withholds_of_constant {rule : (Nat → V) → Option Nat}
    (equivariant : EquivariantChoice rule) {reg : S → V} {r : Run P}
    (constant : ∀ n, reg (r.state n) = reg (r.state 0)) : rule (Parting.course reg r) = none :=
  equivariant.withholds_of_full_tie (a := 0) (b := 1) (fun same => Nat.noConfusion same)
    fun i i' => (constant i).trans (constant i').symm

/-- **Along a run taking one value throughout, every valuation through the course values all
moments alike.** -/
theorem values_alike_of_constant {W : Type x} {value : (Nat → V) → Nat → W}
    (equivariant : EquivariantValue value) {reg : S → V} {r : Run P}
    (constant : ∀ n, reg (r.state n) = reg (r.state 0)) (i i' : Nat) :
    value (Parting.course reg r) i = value (Parting.course reg r) i' :=
  equivariant.full_tie (fun i i' => (constant i).trans (constant i').symm) i i'

/-- **The moments a valuation through the course gives one value are selected alike where they
take one value through the map.** -/
theorem value_level_alike {W : Type x} {value : (Nat → V) → Nat → W}
    (equivariant : EquivariantValue value) (c : W) {reg : S → V} {r : Run P} {j k : Nat}
    (tie : reg (r.state j) = reg (r.state k)) :
    value (Parting.course reg r) j = c ↔ value (Parting.course reg r) k = c :=
  (equivariant.level c).tied tie

/-- **A selection through the course is through the lumping the map makes along the run.** -/
theorem selects_through_coupling {select : (Nat → V) → Nat → Prop}
    (equivariant : Equivariant select) (reg : S → V) (r : Run P) :
    Learning.Training.Through (fun i i' => reg (r.state i) = reg (r.state i'))
      (select (Parting.course reg r)) :=
  Learning.selects_through_lumping equivariant (Parting.course reg r)

/-- **A valuation through the course goes alike across the lumping the map makes along the
run.** -/
theorem values_lumped {W : Type x} {value : (Nat → V) → Nat → W}
    (equivariant : EquivariantValue value) (reg : S → V) (r : Run P) :
    Learning.Lumped (Parting.course reg r) (value (Parting.course reg r)) :=
  Learning.values_lumped equivariant (Parting.course reg r)

/-- **Where a feature separates two moments the map lumps, no selection through the course
selects exactly the moments meeting it.** That takes a finer map. -/
theorem selects_not_right_of_parted {select : (Nat → V) → Nat → Prop}
    (equivariant : Equivariant select) {reg : S → V} {r : Run P} {target : S → Prop} {j k : Nat}
    (tie : reg (r.state j) = reg (r.state k)) (holds : target (r.state j))
    (fails : ¬ target (r.state k)) :
    ¬ ∀ i, select (Parting.course reg r) i ↔ target (r.state i) :=
  Learning.selects_not_right_of_parted equivariant (p := fun i => target (r.state i)) tie holds
    fails

/-- **A feature read off the map is selected by reading it through the course.** -/
theorem selects_right_of_reads {reg : S → V} {r : Run P} {target : S → Prop} (q : V → Prop)
    (reads : ∀ s, target s ↔ q (reg s)) :
    Equivariant (fun (m : Nat → V) (i : Nat) => q (m i)) ∧
      ∀ i, q (Parting.course reg r i) ↔ target (r.state i) :=
  Learning.selects_right_of_reads (r := Parting.course reg r) (p := fun i => target (r.state i)) q
    fun i => reads (r.state i)

/-- **Where a feature parts two moments the map lumps, no valuation through the course gives
each moment its value.** -/
theorem values_not_right_of_parted {W : Type x} {value : (Nat → V) → Nat → W}
    (equivariant : EquivariantValue value) {reg : S → V} {r : Run P} {f : S → W} {j k : Nat}
    (tie : reg (r.state j) = reg (r.state k)) (parted : f (r.state j) ≠ f (r.state k)) :
    ¬ ∀ i, value (Parting.course reg r) i = f (r.state i) :=
  Learning.values_not_right_of_parted equivariant (f := fun i => f (r.state i)) tie parted

/-- **A feature read off the map is valued by reading it through the course.** -/
theorem values_right_of_reads {W : Type x} {reg : S → V} {r : Run P} {f : S → W} (h : V → W)
    (reads : ∀ s, f s = h (reg s)) :
    EquivariantValue (fun (m : Nat → V) (i : Nat) => h (m i)) ∧
      ∀ i, h (Parting.course reg r i) = f (r.state i) :=
  Learning.values_right_of_reads (r := Parting.course reg r) (f := fun i => f (r.state i)) h
    fun i => reads (r.state i)

end Moments

section Share

variable {α : Type} {C : Type} {A : Type v} {P : Process (C → Nat) A}

end Share

end SelectionRuns

end Becoming
