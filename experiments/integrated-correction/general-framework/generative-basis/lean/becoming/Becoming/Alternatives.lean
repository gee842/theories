import Becoming.Metaethics
import Becoming.Relevance
import Becoming.Lifting

/-!
# Alternatives realizing configurations: C, P and N on them

A set of alternatives of one history realizes each feasible alternative as a configuration of a
frame (`Alternatives`): the alternatives are differentiated responses within the history, not
independent choosers. Living significance (`G0`), C (`Comparison`), the articulation P
(`Alternatives.Articulation`: a strict comparison of two feasible alternatives' configurations gives a
reason to move) and the coherence N (`Alternatives.Coherent`: a selected alternative is feasible and no
feasible one is strictly better) are separate conditions; each theorem names those it takes. P
supplies a reason, not an obligation, permission or compliance. The conditional selection
results use C and N, not living significance.

Ported from `GenerativeComparison` (F3J, 18 October 2026). Its `Inventory`, `G0`,
`GenerativeExtension` and `ComparisonPrinciple` are the core's `G0`, `Extension` and `Comparison`
on a frame by `Iff.rfl` (`Becoming.Bridge`), so `generative_extension_irreflexive` and
`generative_extension_transitive` are `Extension.irrefl` and `Extension.trans`, and are not
restated. Every declaration has an empty axiom report.

* **A new realization of an extension has positive relevance** under living significance
  (`G0.new_realization`); under the continuation condition, positive relevance read from
  significance (`Extension.new_relevance`, from the join `ExtensionFrames`).
* **Survivors are lifted survivors.** On the step of a set of alternatives, an alternative
  survives exactly when no live alternative liftedly extends it
  (`Alternatives.survives_iff_lifted`), and restricting the alternatives keeps such a survivor
  (`Alternatives.restricted_survives`), both from the join `ExtensionFrames`.
* **C and P give a reason** for moving between feasible alternatives whose configurations extend
  (`Alternatives.reason_of_extension`). **C and N**: a coherently selected alternative is not
  extended by a feasible one (`Alternatives.survives_of_coherent`); restricting the feasible
  alternatives keeps a survivor that remains (`Alternatives.survives_restrict`); where every
  feasible alternative is extended by a feasible one, none survives
  (`Alternatives.no_survivor`): no final maximum of generative activity is demanded.
* **Alternatives are one step of a frame.** The alternatives at a configuration are the moves of a
  process that takes each feasible alternative to its configuration (`Alternatives.process`),
  enabled exactly where feasible (`Alternatives.enabled_iff`); the lifted comparison L of two
  feasible alternatives is the comparison of their configurations (`Alternatives.lift_iff`): the
  functional case is the deterministic case of L.
* **C is silent on trade-offs** (`Profiles`). Two dimensions of generation, each realized or not:
  two strictly positive appraisals both respect every generative extension
  (`Profiles.both_respect`) and disagree when one realization replaces the other
  (`Profiles.opposite`); both alternatives of the trade-off survive (`Profiles.both_survive`),
  and each appraisal selects a different one coherently (`Profiles.different_selections`). The
  scores are illustrations only.

Direction as in `Comparison`: `Better s t` says `t` is better.
-/

namespace Becoming

open Generative

section Alternatives

variable {S A C : Type}

/-- Alternatives of one history: which are feasible, and the configuration each realizes. -/
structure Alternatives (S A : Type) where
  feasible : A → Prop
  realize : A → S

/-- **A new realization of a generative extension has positive relevance** under living
significance. -/
theorem G0.new_realization {F : Frame S A C} {living : C → Prop} {positive : S → C → Prop}
    (g0 : G0 F living positive) {s t : S} (extension : Extension F living s t) :
    ∃ c, positive t c ∧ ¬ F.realized s c :=
  match extension with
  | ⟨_, c, alive, now, before⟩ => ⟨c, g0 t c alive now, before⟩

/-- **Under the continuation condition a new realization of an extension has positive relevance
read from significance**: living significance holds of that relevance (`g0_of_unrestricted`), so
an extension realizes living content with significance that the earlier configuration lacked.
Ported from the join `ExtensionFrames`. -/
theorem Extension.new_relevance {Q F Pos : Type} (M : Frame S A Q) (living : Q → Prop)
    {sig : Pos → Nat → F → Prop} (unrestricted : Unrestricted sig) (formation : Q → F)
    (step : Q → Nat) {s t : S} (extension : Extension M living s t) :
    ∃ c, M.relevance living sig formation step t c ∧ ¬ M.realized s c :=
  G0.new_realization (g0_of_unrestricted M living unrestricted formation step) extension

variable {R : Type}

/-- P: a strict comparison of two feasible alternatives' configurations gives a reason to move
from the first to the second. -/
def Alternatives.Articulation (X : Alternatives S R) (Better : S → S → Prop) (Reason : R → R → Prop) : Prop :=
  ∀ a b, X.feasible a → X.feasible b → Better (X.realize a) (X.realize b) → Reason a b

/-- N: a selected alternative is feasible, and no feasible alternative is strictly better. -/
def Alternatives.Coherent (X : Alternatives S R) (Better : S → S → Prop) (Selected : R → Prop) : Prop :=
  ∀ a, Selected a → X.feasible a ∧ ∀ b, X.feasible b → ¬ Better (X.realize a) (X.realize b)

/-- A feasible alternative no feasible alternative generatively extends. Surviving this filter
establishes no permission or duty. -/
def Alternatives.Survives (F : Frame S A C) (living : C → Prop) (X : Alternatives S R) (a : R) : Prop :=
  X.feasible a ∧ ∀ b, X.feasible b → ¬ Extension F living (X.realize a) (X.realize b)

variable {F : Frame S A C} {living : C → Prop} {X : Alternatives S R} {Better : S → S → Prop}

/-- **C and P give a reason** to move to a feasible alternative whose configuration extends. -/
theorem Alternatives.reason_of_extension {Reason : R → R → Prop}
    (comparison : Comparison F living Better) (articulation : Alternatives.Articulation X Better Reason)
    {a b : R} (feasibleA : X.feasible a) (feasibleB : X.feasible b)
    (extension : Extension F living (X.realize a) (X.realize b)) : Reason a b :=
  articulation a b feasibleA feasibleB (comparison _ _ extension)

/-- **C and N**: a coherently selected alternative survives. -/
theorem Alternatives.survives_of_coherent {Selected : R → Prop}
    (comparison : Comparison F living Better) (coherent : Alternatives.Coherent X Better Selected) {a : R}
    (selected : Selected a) : Alternatives.Survives F living X a :=
  match coherent a selected with
  | ⟨feasible, unbeaten⟩ => ⟨feasible, fun b other extension =>
      unbeaten b other (comparison _ _ extension)⟩

/-- Restricting the feasible alternatives keeps a survivor that remains feasible. Deleting rivals
removes comparisons; it changes no realization. -/
theorem Alternatives.survives_restrict (restricted : R → Prop) {a : R}
    (survives : Alternatives.Survives F living X a) (kept : restricted a) :
    Alternatives.Survives F living ⟨fun b => X.feasible b ∧ restricted b, X.realize⟩ a :=
  ⟨⟨survives.1, kept⟩, fun b other => survives.2 b other.1⟩

/-- **Continual improvement leaves no survivor**: where every feasible alternative is extended by
a feasible one, none survives. -/
theorem Alternatives.no_survivor
    (improvement : ∀ a, X.feasible a → ∃ b, X.feasible b ∧
      Extension F living (X.realize a) (X.realize b)) (a : R) : ¬ Alternatives.Survives F living X a :=
  fun survives => match improvement a survives.1 with
  | ⟨b, feasible, extension⟩ => survives.2 b feasible extension

/-- The alternatives at a configuration as one step of a process. -/
def Alternatives.process (X : Alternatives S R) (s : S) : Process S R :=
  ⟨fun x a t => x = s ∧ X.feasible a ∧ t = X.realize a⟩

theorem Alternatives.enabled_iff (X : Alternatives S R) (s : S) (a : R) :
    Enabled (X.process s) s a ↔ X.feasible a :=
  ⟨fun ⟨_, _, feasible, _⟩ => feasible, fun feasible => ⟨_, rfl, feasible, rfl⟩⟩

/-- **The lifted comparison of two feasible alternatives is the comparison of their
configurations**: functional alternatives are the deterministic case of L. -/
theorem Alternatives.lift_iff (X : Alternatives S R) (s : S) (realized : S → C → Prop)
    (better : S → S → Prop) {a b : R} (feasibleA : X.feasible a) (feasibleB : X.feasible b) :
    LiftBetter ⟨X.process s, realized⟩ better s a b ↔ better (X.realize a) (X.realize b) :=
  ⟨fun lifted => lifted _ ⟨rfl, feasibleA, rfl⟩ _ ⟨rfl, feasibleB, rfl⟩,
   fun held _ ⟨_, _, ha⟩ _ ⟨_, _, hb⟩ =>
    Eq.subst (motive := fun x => better x _) ha.symm
      (Eq.subst (motive := fun y => better (X.realize a) y) hb.symm held)⟩

/-- **The survivors of a set of alternatives are the lifted survivors of its step**: an
alternative survives the generative-extension filter exactly when it is live at the step and no
live alternative liftedly extends it (`LiftSurvives`, `Becoming.Lifting`). From the join
`ExtensionFrames`. -/
theorem Alternatives.survives_iff_lifted (X : Alternatives S R) (s : S) (realized : S → C → Prop)
    (living : C → Prop) (a : R) :
    Alternatives.Survives ⟨X.process s, realized⟩ living X a ↔ LiftSurvives ⟨X.process s, realized⟩ living s a :=
  ⟨fun ⟨feasibleA, unextended⟩ =>
    ⟨(X.enabled_iff s a).mpr feasibleA, fun b liveB lifted =>
      let feasibleB := (X.enabled_iff s b).mp liveB
      unextended b feasibleB
        ((X.lift_iff s realized (Extension ⟨X.process s, realized⟩ living) feasibleA
          feasibleB).mp lifted)⟩,
   fun ⟨liveA, unextended⟩ =>
    let feasibleA := (X.enabled_iff s a).mp liveA
    ⟨feasibleA, fun b feasibleB extension =>
      unextended b ((X.enabled_iff s b).mpr feasibleB)
        ((X.lift_iff s realized (Extension ⟨X.process s, realized⟩ living) feasibleA
          feasibleB).mpr extension)⟩⟩

/-- **P is lifted P on the step of the alternatives**: a reason from every strict comparison of
feasible alternatives' configurations is a reason from every lifted comparison of live
alternatives (`LiftedArticulation`, `Becoming.Lifting`). From the bridge. -/
theorem Alternatives.articulation_iff_lifted (X : Alternatives S R) (s : S)
    (realized : S → C → Prop) (Better : S → S → Prop) (Reason : R → R → Prop) :
    Alternatives.Articulation X Better Reason ↔ LiftedArticulation ⟨X.process s, realized⟩ Better s Reason :=
  ⟨fun articulation a b liveA liveB lifted =>
    let feasibleA := (X.enabled_iff s a).mp liveA
    let feasibleB := (X.enabled_iff s b).mp liveB
    articulation a b feasibleA feasibleB
      ((X.lift_iff s realized (fun x y => Better y x) feasibleB feasibleA).mp lifted),
   fun lifted a b feasibleA feasibleB better =>
    lifted a b ((X.enabled_iff s a).mpr feasibleA) ((X.enabled_iff s b).mpr feasibleB)
      ((X.lift_iff s realized (fun x y => Better y x) feasibleB feasibleA).mpr better)⟩

/-- **Restricting the alternatives keeps a lifted survivor**: an alternative no live alternative
liftedly extends still survives when the feasible alternatives are restricted to a subfamily
containing it. From the join `ExtensionFrames`. -/
theorem Alternatives.restricted_survives (X : Alternatives S R) (s : S) (realized : S → C → Prop)
    (living : C → Prop) (restricted : R → Prop) {a : R}
    (survivor : LiftSurvives ⟨X.process s, realized⟩ living s a) (retained : restricted a) :
    LiftSurvives ⟨Alternatives.process ⟨fun b => X.feasible b ∧ restricted b, X.realize⟩ s,
      realized⟩ living s a :=
  (Alternatives.survives_iff_lifted ⟨fun b => X.feasible b ∧ restricted b, X.realize⟩ s realized
      living a).mp
    (Alternatives.survives_restrict restricted
      ((Alternatives.survives_iff_lifted X s realized living a).mpr survivor) retained)

end Alternatives

namespace Profiles

/-- Two dimensions of generation, each realized or not. Neither dimension is an independent
subject. -/
abbrev Profile := Bool × Bool

def realized : Profile → Bool → Prop
  | p, true => p.2 = true
  | p, false => p.1 = true

def frame : Frame Profile Unit Bool := ⟨⟨fun _ _ _ => False⟩, realized⟩

def living (_ : Bool) : Prop := True

def count : Bool → Nat
  | true => 1
  | false => 0

def firstAppraisal (p : Profile) : Nat := 2 * count p.1 + count p.2

def secondAppraisal (p : Profile) : Nat := count p.1 + 2 * count p.2

def ScoreBetter (score : Profile → Nat) (first second : Profile) : Prop := score first < score second

/-- The trade-off: one dimension or the other. -/
def tradeoff : Alternatives Profile Profile :=
  ⟨fun p => p = (true, false) ∨ p = (false, true), id⟩

theorem lost {s t : Profile} (extension : Extension frame living s t) (c : Bool)
    (held : realized s c) (missing : ¬ realized t c) : False :=
  missing (extension.1 c held)

/-- Every extension raises a score that rises in each dimension. -/
theorem respects (score : Profile → Nat)
    (ff_tf : score (false, false) < score (true, false))
    (ff_ft : score (false, false) < score (false, true))
    (ff_tt : score (false, false) < score (true, true))
    (tf_tt : score (true, false) < score (true, true))
    (ft_tt : score (false, true) < score (true, true)) :
    Comparison frame living (ScoreBetter score)
  | (false, false), (false, false), e => absurd e Extension.irrefl
  | (false, false), (true, false), _ => ff_tf
  | (false, false), (false, true), _ => ff_ft
  | (false, false), (true, true), _ => ff_tt
  | (true, false), (false, false), e => False.elim (lost e false rfl Bool.noConfusion)
  | (true, false), (true, false), e => absurd e Extension.irrefl
  | (true, false), (false, true), e => False.elim (lost e false rfl Bool.noConfusion)
  | (true, false), (true, true), _ => tf_tt
  | (false, true), (false, false), e => False.elim (lost e true rfl Bool.noConfusion)
  | (false, true), (true, false), e => False.elim (lost e true rfl Bool.noConfusion)
  | (false, true), (false, true), e => absurd e Extension.irrefl
  | (false, true), (true, true), _ => ft_tt
  | (true, true), (false, false), e => False.elim (lost e true rfl Bool.noConfusion)
  | (true, true), (true, false), e => False.elim (lost e true rfl Bool.noConfusion)
  | (true, true), (false, true), e => False.elim (lost e false rfl Bool.noConfusion)
  | (true, true), (true, true), e => absurd e Extension.irrefl

/-- **Both appraisals respect every generative extension.** -/
theorem both_respect :
    Comparison frame living (ScoreBetter firstAppraisal) ∧
      Comparison frame living (ScoreBetter secondAppraisal) :=
  ⟨respects firstAppraisal (by decide) (by decide) (by decide) (by decide) (by decide),
   respects secondAppraisal (by decide) (by decide) (by decide) (by decide) (by decide)⟩

/-- **They disagree when one realization replaces the other.** -/
theorem opposite :
    ScoreBetter firstAppraisal (false, true) (true, false) ∧
      ScoreBetter secondAppraisal (true, false) (false, true) :=
  ⟨(by decide : 1 < 2), (by decide : 1 < 2)⟩

/-- **Both alternatives of the trade-off survive.** -/
theorem both_survive :
    Alternatives.Survives frame living tradeoff (true, false) ∧ Alternatives.Survives frame living tradeoff (false, true) :=
  ⟨⟨.inl rfl, fun b feasible => match b, feasible with
      | _, .inl rfl => Extension.irrefl
      | _, .inr rfl => fun e => lost e false rfl Bool.noConfusion⟩,
   ⟨.inr rfl, fun b feasible => match b, feasible with
      | _, .inl rfl => fun e => False.elim (lost e true rfl Bool.noConfusion)
      | _, .inr rfl => Extension.irrefl⟩⟩

/-- **Each appraisal selects a different alternative coherently.** -/
theorem different_selections :
    Alternatives.Coherent tradeoff (ScoreBetter firstAppraisal) (fun p => p = (true, false)) ∧
      Alternatives.Coherent tradeoff (ScoreBetter secondAppraisal) (fun p => p = (false, true)) :=
  ⟨fun a selected => match a, selected with
    | _, rfl => ⟨.inl rfl, fun b feasible => match b, feasible with
      | _, .inl rfl => Nat.lt_irrefl 2
      | _, .inr rfl => (by decide : ¬ 2 < 1)⟩,
   fun a selected => match a, selected with
    | _, rfl => ⟨.inr rfl, fun b feasible => match b, feasible with
      | _, .inl rfl => (by decide : ¬ 2 < 1)
      | _, .inr rfl => Nat.lt_irrefl 2⟩⟩

end Profiles

end Becoming
