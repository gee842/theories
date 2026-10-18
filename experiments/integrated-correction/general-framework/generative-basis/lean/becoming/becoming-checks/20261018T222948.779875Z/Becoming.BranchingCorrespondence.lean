import Becoming.Granularity
import Becoming.Presentations

/-!
# Branching correspondence: configurations of two frames matched by the tests they pass

`Becoming.Likeness` shows that, where each move's outcomes are listed, configurations passing the
same branching tests are alike: constructively where the frames are finite and decided, and with
excluded middle as a named hypothesis otherwise (`alike_iff_sameBranchingTests_of_em`). This
module states what follows for two frames whose configurations each pass the tests of exactly one
configuration of the other.

* Passing the same branching tests is an equivalence across frames (`SameBranchingTests.refl`,
  `.symm`, `.trans`).
* Under excluded middle, where both frames list each move's outcomes, passing the same tests is a
  bisimulation (`SameBranchingTests.bisimulation_of_em`), from the matching of each step
  (`SameBranchingTests.step_of_em` of `Becoming.Granularity`).
* A code reading each configuration's tests exactly gives alike configurations one code
  (`alike_of_equal_codes_of_em`).
* Under excluded middle, from configurations passing the same tests, each configuration reachable
  from the first passes the tests of one reachable from the second
  (`SameBranchingTests.total_of_reachable_of_em`); where both frames are reachable from them and
  their tests tell their configurations apart, the tests match configurations one to one
  (`SameBranchingTests.correspondence_of_em`), and the matching carries steps exactly
  (`SameBranchingTests.step_iff_of_em`).
* Every bisimulation agrees with the matching where the tests tell the second frame's
  configurations apart (`Bisimulation.agrees`), with no hypothesis.

Excluded middle is a named hypothesis (`em : ∀ p : Prop, Decided p`) wherever it is used; every
declaration's axiom report is empty. Ported from `Generative.ExplanatoryBranching` (bridge fold
F3E, 18 October 2026); the port is a restatement on the core's frames, not a new result.
-/

universe u u' u'' v w y

namespace Becoming

open Generative
open Becoming.Presentations

section BranchingCorrespondence

variable {S : Type u} {S' : Type u'} {S'' : Type u''} {A : Type v} {C : Type w}

/-- **Every configuration passes its own branching tests.** -/
theorem SameBranchingTests.refl (F : Frame S A C) (s : S) : SameBranchingTests F F s s :=
  fun _ => Iff.rfl

/-- **Passing the same branching tests is symmetric.** -/
theorem SameBranchingTests.symm {F : Frame S A C} {G : Frame S' A C} {s : S} {s' : S'}
    (same : SameBranchingTests F G s s') : SameBranchingTests G F s' s :=
  fun φ => (same φ).symm

/-- **Passing the same branching tests is transitive across three frames.** -/
theorem SameBranchingTests.trans {F : Frame S A C} {G : Frame S' A C} {H : Frame S'' A C}
    {s : S} {s' : S'} {s'' : S''} (same : SameBranchingTests F G s s')
    (same' : SameBranchingTests G H s' s'') : SameBranchingTests F H s s'' :=
  fun φ => (same φ).trans (same' φ)

/-- **Where branching tests tell apart the configurations of a frame, at most one of them passes
the tests of a given configuration**, read from the other side. -/
theorem SameBranchingTests.inverse_functional {F : Frame S A C} {G : Frame S' A C}
    (separated : ∀ s t, SameBranchingTests F F s t → s = t) {s t : S} {s' : S'}
    (same : SameBranchingTests F G s s') (same' : SameBranchingTests F G t s') : s = t :=
  separated s t (same.trans same'.symm)

/-- **Under excluded middle, passing the same branching tests is a bisimulation**, where both
frames list each move's outcomes. -/
theorem SameBranchingTests.bisimulation_of_em {F : Frame S A C} {G : Frame S' A C}
    (em : ∀ p : Prop, Decided p) (outcomes : ∀ s a, ∃ l : List S, ∀ t, F.P.step s a t ↔ t ∈ l)
    (outcomes' : ∀ s a, ∃ l : List S', ∀ t, G.P.step s a t ↔ t ∈ l) :
    Bisimulation F G (SameBranchingTests F G) :=
  fun _ _ same =>
    ⟨fun c => same (.claim c),
     fun _ _ step => SameBranchingTests.step_of_em em outcomes' same step,
     fun _ _ step' => match SameBranchingTests.step_of_em em outcomes same.symm step' with
      | ⟨t, step, joined⟩ => ⟨t, step, joined.symm⟩⟩

/-- **Under excluded middle, configurations given one code by a presentation reading their tests
exactly are alike**, where the frame lists each move's outcomes. -/
theorem alike_of_equal_codes_of_em {D : Type y} {F : Frame S A C} (em : ∀ p : Prop, Decided p)
    (outcomes : ∀ s a, ∃ l : List S, ∀ t, F.P.step s a t ↔ t ∈ l)
    {p : Presentation S (BranchingTest A C) D} (exact : Exact (BranchingTest.Holds F) p) {s t : S}
    (equal : p.encode s = p.encode t) : Alike F F s t :=
  alike_of_sameBranchingTests_of_em em outcomes outcomes (equal_codes_same_answers exact equal)

/-- **Under excluded middle, each configuration reachable from a configuration passes the tests of
a configuration of the other frame**, where both frames list each move's outcomes and the root
passes the tests of the other root. -/
theorem SameBranchingTests.total_of_reachable_of_em {F : Frame S A C} {G : Frame S' A C}
    (em : ∀ p : Prop, Decided p) (outcomes : ∀ s a, ∃ l : List S, ∀ t, F.P.step s a t ↔ t ∈ l)
    (outcomes' : ∀ s a, ∃ l : List S', ∀ t, G.P.step s a t ↔ t ∈ l) {root : S} {root' : S'}
    (same : SameBranchingTests F G root root')
    (reach : ∀ s, ∃ as, Trace F.P root as s) (s : S) : ∃ s', SameBranchingTests F G s s' :=
  match reach s with
  | ⟨_, path⟩ =>
    match (SameBranchingTests.bisimulation_of_em em outcomes outcomes').trace path same with
    | ⟨s', _, joined⟩ => ⟨s', joined⟩

/-- **Under excluded middle, the branching tests match two frames' configurations one to one**,
where both frames list each move's outcomes, are reachable from roots passing the same tests, and
have configurations their tests tell apart. -/
theorem SameBranchingTests.correspondence_of_em {F : Frame S A C} {G : Frame S' A C}
    (em : ∀ p : Prop, Decided p) (outcomes : ∀ s a, ∃ l : List S, ∀ t, F.P.step s a t ↔ t ∈ l)
    (outcomes' : ∀ s a, ∃ l : List S', ∀ t, G.P.step s a t ↔ t ∈ l) {root : S} {root' : S'}
    (same : SameBranchingTests F G root root') (reach : ∀ s, ∃ as, Trace F.P root as s)
    (reach' : ∀ s', ∃ as, Trace G.P root' as s')
    (separated : ∀ s t, SameBranchingTests F F s t → s = t)
    (separated' : ∀ s' t', SameBranchingTests G G s' t' → s' = t') :
    (∀ s, ∃ s', SameBranchingTests F G s s' ∧ ∀ t', SameBranchingTests F G s t' → t' = s') ∧
      (∀ s', ∃ s, SameBranchingTests F G s s' ∧ ∀ t, SameBranchingTests F G t s' → t = s) :=
  ⟨fun s => match SameBranchingTests.total_of_reachable_of_em em outcomes outcomes' same reach s with
    | ⟨s', joined⟩ => ⟨s', joined, fun _ joined' =>
        SameBranchingTests.functional separated' joined' joined⟩,
   fun s' => match SameBranchingTests.total_of_reachable_of_em em outcomes' outcomes same.symm
        reach' s' with
    | ⟨s, joined⟩ => ⟨s, joined.symm, fun _ joined' =>
        SameBranchingTests.inverse_functional separated joined' joined.symm⟩⟩

/-- **Under excluded middle, the matching by branching tests carries steps exactly**, where both
frames list each move's outcomes and their tests tell their configurations apart. -/
theorem SameBranchingTests.step_iff_of_em {F : Frame S A C} {G : Frame S' A C}
    (em : ∀ p : Prop, Decided p) (outcomes : ∀ s a, ∃ l : List S, ∀ t, F.P.step s a t ↔ t ∈ l)
    (outcomes' : ∀ s a, ∃ l : List S', ∀ t, G.P.step s a t ↔ t ∈ l)
    (separated : ∀ s t, SameBranchingTests F F s t → s = t)
    (separated' : ∀ s' t', SameBranchingTests G G s' t' → s' = t') {s t : S} {s' t' : S'}
    (same : SameBranchingTests F G s s') (same' : SameBranchingTests F G t t') (a : A) :
    F.P.step s a t ↔ G.P.step s' a t' :=
  ⟨fun step => match SameBranchingTests.step_of_em em outcomes' same step with
    | ⟨_, step', joined⟩ => Eq.subst (motive := fun w => G.P.step s' a w)
        (SameBranchingTests.functional separated' joined same') step',
   fun step' => match SameBranchingTests.step_of_em em outcomes same.symm step' with
    | ⟨_, step, joined⟩ => Eq.subst (motive := fun w => F.P.step s a w)
        (SameBranchingTests.inverse_functional separated joined.symm same') step⟩

/-- **Every bisimulation agrees with the matching by branching tests** where the tests tell the
second frame's configurations apart: what a bisimulation relates to `s` is the configuration
passing the tests of `s`. -/
theorem Bisimulation.agrees {F : Frame S A C} {G : Frame S' A C} {B : S → S' → Prop}
    (separated' : ∀ s' t', SameBranchingTests G G s' t' → s' = t') (bisim : Bisimulation F G B)
    {s : S} {s' t' : S'} (same : SameBranchingTests F G s s') (related : B s t') : s' = t' :=
  SameBranchingTests.functional separated' same (Alike.sameBranchingTests ⟨B, bisim, related⟩)

end BranchingCorrespondence

end Becoming
