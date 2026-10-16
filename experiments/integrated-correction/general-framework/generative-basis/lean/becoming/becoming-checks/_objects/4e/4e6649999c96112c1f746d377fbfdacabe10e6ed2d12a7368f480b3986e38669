/-!
# Constructive audit of an unrestricted cut-to-coverage inference

This standalone module formalizes positive unary inference from declared seeds
and transport edges over an arbitrary type of positions. Positions may describe
response occasions within one whole history; no independent agents are assumed.

An anchor-free reverse-closed cut containing a target is exactly an obstruction
to finite rooted reachability. Constructively, absence of such a cut gives
double-negated reachability. Upgrading this to reachability for all structures
is equivalent to double-negation elimination. Decidable reachability suffices
for a particular upgrade.

This reverse-closed-cut formulation must not be silently identified, in
constructive logic, with the older hand proof's clause that every anchor-free
target-containing subset has an explicit incoming crossing. Turning absence of
a crossing into reverse closure can require a further classical case split.
The equivalence to double-negation elimination proved here concerns exactly
`UniversalCutUpgrade` below, not that unformalized incoming-crossing clause.

The older Boolean-valued model argument also needs a decidable or classical
characteristic function for arbitrary reachability. Here cuts and reachability
are Prop-valued; no characteristic Boolean function is assumed or constructed.

All reasoning below is constructive. Double-negation elimination is an explicit
proposition whose consequences are assessed, never an axiom or an instance.
The module proves nothing about the ethical warrant of a seed or transport.
Its arbitrary predicates characterize these inference premises, not alternative
moral realities obtained by changing a free moral predicate.
-/

namespace UniversalEthics.CutCoverageAudit

universe u

inductive Reach {Position : Type u}
    (seed : Position → Prop) (edge : Position → Position → Prop) : Position → Prop
  | root {x : Position} : seed x → Reach seed edge x
  | step {x y : Position} : Reach seed edge x → edge x y → Reach seed edge y

def HasCut {Position : Type u}
    (seed : Position → Prop) (edge : Position → Position → Prop)
    (target : Position) : Prop :=
  ∃ cut : Position → Prop,
    cut target ∧
    (∀ x, seed x → ¬ cut x) ∧
    (∀ x y, edge x y → cut y → cut x)

def NoCut {Position : Type u}
    (seed : Position → Prop) (edge : Position → Position → Prop)
    (target : Position) : Prop :=
  ¬ HasCut seed edge target

theorem reach_avoids_reverse_closed_cut
    {Position : Type u} {seed : Position → Prop}
    {edge : Position → Position → Prop} {cut : Position → Prop}
    (anchorFree : ∀ x, seed x → ¬ cut x)
    (reverseClosed : ∀ x y, edge x y → cut y → cut x)
    {target : Position} (reachable : Reach seed edge target) : ¬ cut target := by
  induction reachable with
  | root hseed => exact anchorFree _ hseed
  | @step x y _ hedge ih =>
      exact fun hcut => ih (reverseClosed x y hedge hcut)

theorem reachable_implies_no_cut
    {Position : Type u} {seed : Position → Prop}
    {edge : Position → Position → Prop} {target : Position}
    (reachable : Reach seed edge target) : NoCut seed edge target := by
  intro hcut
  obtain ⟨cut, member, anchorFree, reverseClosed⟩ := hcut
  exact reach_avoids_reverse_closed_cut anchorFree reverseClosed reachable member

theorem has_cut_implies_not_reachable
    {Position : Type u} {seed : Position → Prop}
    {edge : Position → Position → Prop} {target : Position}
    (hcut : HasCut seed edge target) : ¬ Reach seed edge target := by
  intro reachable
  exact reachable_implies_no_cut reachable hcut

theorem not_reachable_has_cut
    {Position : Type u} {seed : Position → Prop}
    {edge : Position → Position → Prop} {target : Position}
    (notReachable : ¬ Reach seed edge target) : HasCut seed edge target := by
  refine ⟨fun x => ¬ Reach seed edge x, notReachable, ?_, ?_⟩
  · intro x hseed notReachableX
    exact notReachableX (Reach.root hseed)
  · intro x y hedge notReachableY reachableX
    exact notReachableY (Reach.step reachableX hedge)

theorem has_cut_iff_not_reachable
    {Position : Type u} {seed : Position → Prop}
    {edge : Position → Position → Prop} {target : Position} :
    HasCut seed edge target ↔ ¬ Reach seed edge target :=
  ⟨has_cut_implies_not_reachable, not_reachable_has_cut⟩

theorem no_cut_iff_double_negated_reachability
    {Position : Type u} {seed : Position → Prop}
    {edge : Position → Position → Prop} {target : Position} :
    NoCut seed edge target ↔ ¬ ¬ Reach seed edge target := by
  constructor
  · intro noCut notReachable
    exact noCut (not_reachable_has_cut notReachable)
  · intro notNotReachable hcut
    exact notNotReachable (has_cut_implies_not_reachable hcut)

theorem no_cut_to_reachable_of_decidable
    {Position : Type u} {seed : Position → Prop}
    {edge : Position → Position → Prop} {target : Position}
    (decision : Decidable (Reach seed edge target))
    (noCut : NoCut seed edge target) : Reach seed edge target := by
  cases decision with
  | isTrue reachable => exact reachable
  | isFalse notReachable =>
      exact False.elim (noCut (not_reachable_has_cut notReachable))

theorem no_cut_iff_reachable_of_decidable
    {Position : Type u} {seed : Position → Prop}
    {edge : Position → Position → Prop} {target : Position}
    (decision : Decidable (Reach seed edge target)) :
    NoCut seed edge target ↔ Reach seed edge target :=
  ⟨no_cut_to_reachable_of_decidable decision, reachable_implies_no_cut⟩

def DoubleNegationElimination : Prop :=
  ∀ proposition : Prop, (¬ ¬ proposition) → proposition

def UniversalCutUpgrade : Prop :=
  ∀ (Position : Type u) (seed : Position → Prop)
    (edge : Position → Position → Prop) (target : Position),
    NoCut seed edge target → Reach seed edge target

theorem singleton_reachability_iff
    {proposition : Prop} {target : PUnit.{u + 1}} :
    Reach (fun _ : PUnit.{u + 1} => proposition)
      (fun _ _ => False) target ↔ proposition := by
  constructor
  · intro reachable
    cases reachable with
    | root proof => exact proof
    | step _ hedge => exact False.elim hedge
  · intro proof
    exact Reach.root proof

theorem double_negation_elimination_implies_universal_cut_upgrade
    (dne : DoubleNegationElimination) : UniversalCutUpgrade.{u} := by
  intro Position seed edge target noCut
  exact dne (Reach seed edge target)
    (no_cut_iff_double_negated_reachability.mp noCut)

theorem universal_cut_upgrade_implies_double_negation_elimination
    (upgrade : UniversalCutUpgrade.{u}) : DoubleNegationElimination := by
  intro proposition notNotProposition
  have notNotReachable :
      ¬ ¬ Reach (fun _ : PUnit.{u + 1} => proposition)
        (fun _ _ => False) PUnit.unit := by
    intro notReachable
    apply notNotProposition
    intro proof
    exact notReachable (Reach.root proof)
  have noCut : NoCut (fun _ : PUnit.{u + 1} => proposition)
      (fun _ _ => False) PUnit.unit :=
    no_cut_iff_double_negated_reachability.mpr notNotReachable
  have reachable := upgrade (PUnit.{u + 1}) (fun _ => proposition)
    (fun _ _ => False) PUnit.unit noCut
  exact singleton_reachability_iff.mp reachable

theorem universal_cut_upgrade_iff_double_negation_elimination :
    UniversalCutUpgrade.{u} ↔ DoubleNegationElimination :=
  ⟨universal_cut_upgrade_implies_double_negation_elimination,
    double_negation_elimination_implies_universal_cut_upgrade⟩

#print axioms reach_avoids_reverse_closed_cut
#print axioms reachable_implies_no_cut
#print axioms has_cut_implies_not_reachable
#print axioms not_reachable_has_cut
#print axioms has_cut_iff_not_reachable
#print axioms no_cut_iff_double_negated_reachability
#print axioms no_cut_to_reachable_of_decidable
#print axioms no_cut_iff_reachable_of_decidable
#print axioms singleton_reachability_iff
#print axioms double_negation_elimination_implies_universal_cut_upgrade
#print axioms universal_cut_upgrade_implies_double_negation_elimination
#print axioms universal_cut_upgrade_iff_double_negation_elimination

end UniversalEthics.CutCoverageAudit
