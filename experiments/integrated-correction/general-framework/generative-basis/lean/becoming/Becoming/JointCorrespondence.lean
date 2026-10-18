import Becoming.Composition
import Becoming.Presentations

/-!
# Joint correspondence: configurations holding parts, matched by the joint tests they pass

`Becoming.Composition` shows that joint tests fix joint likeness where both frames' moves and
pairs of parts are compact and their tests are stable (`jointAlike_iff_sameJointTests`). This
module states what follows for two joint frames whose configurations each pass the joint tests of
exactly one configuration of the other, and for codes reading the joint tests.

* What a frame reaches from a root by steps and by taking parts (`JointFrame.Reach`) is matched
  under every joint bisimulation (`JointBisimulation.reach`).
* Where the pairs of parts are compact and the tests stable, the joint tests carry pairs of parts
  exactly (`SameJointTests.joint_iff`); where the moves' outcomes are compact, they carry steps
  exactly (`SameJointTests.step_iff`); with both, configurations reachable from roots passing the
  same tests are matched one to one (`SameJointTests.correspondence`).
* A code reading the joint tests exactly and giving configurations passing the same tests one
  code lets the parts lift from each configuration it describes (`liftsFromEach_of_exact`), lets
  plans realized at codes be realized at each configuration so coded (`JointPlan.realizes_code_iff`),
  and gives them exclusive support (`JointPlan.supports_of_code`).

Stability of the tests (`TestsStable`) is a named hypothesis; excluded middle gives it
(`JointFrame.TestsStable.of_em`), and compactness of listed domains under excluded middle is
`Compact.of_listed`. Every declaration's axiom report is empty. Ported from
`Generative.ExplanatoryJointness` and `Generative.ExplanatoryFootprints` (bridge fold F3E,
18 October 2026); the port is a restatement on the core's joint frames, not a new result.
-/

universe u u' v w y z x'

namespace Becoming

open Generative
open Becoming.Presentations

section Reach

variable {S : Type u} {S' : Type u'} {A : Type v} {C : Type w}

/-- What a joint frame reaches from a root: the root, the outcome of a step from what it reaches,
and each part of a pair held by what it reaches. -/
inductive JointFrame.Reach (F : JointFrame S A C) (root : S) : S → Prop where
  | root : JointFrame.Reach F root root
  | step {s t : S} {a : A} : JointFrame.Reach F root s → F.P.step s a t → JointFrame.Reach F root t
  | left {s l r : S} : JointFrame.Reach F root s → F.joint s l r → JointFrame.Reach F root l
  | right {s l r : S} : JointFrame.Reach F root s → F.joint s l r → JointFrame.Reach F root r

/-- **A joint bisimulation matches what each frame reaches**: from related roots, each
configuration one reaches by steps and parts is related to one the other reaches. -/
theorem JointBisimulation.reach {F : JointFrame S A C} {G : JointFrame S' A C}
    {B : S → S' → Prop} (bisim : JointBisimulation F G B) {root : S} {root' : S'}
    (related : B root root') {s : S} (reach : JointFrame.Reach F root s) :
    ∃ s', JointFrame.Reach G root' s' ∧ B s s' := by
  induction reach with
  | root => exact ⟨root', .root, related⟩
  | step _ step ih =>
    match ih with
    | ⟨t, reach', joined⟩ => match (bisim.1 _ t joined).2.1 _ _ step with
      | ⟨t', step', joined'⟩ => exact ⟨t', .step reach' step', joined'⟩
  | left _ joint ih =>
    match ih with
    | ⟨t, reach', joined⟩ => match bisim.2.1 _ t joined _ _ joint with
      | ⟨l', _, joint', left, _⟩ => exact ⟨l', .left reach' joint', left⟩
  | right _ joint ih =>
    match ih with
    | ⟨t, reach', joined⟩ => match bisim.2.1 _ t joined _ _ joint with
      | ⟨_, r', joint', _, right⟩ => exact ⟨r', .right reach' joint', right⟩

end Reach

section Correspondence

variable {S : Type u} {S' : Type u'} {A : Type v} {C : Type w}

/-- **Where joint tests tell apart a frame's configurations, at most one of them passes the tests
of a given configuration**, read from the other side. -/
theorem SameJointTests.inverse_functional {F : JointFrame S A C} {G : JointFrame S' A C}
    (separated : ∀ s t, SameJointTests F F s t → s = t) {s t : S} {s' : S'}
    (same : SameJointTests F G s s') (same' : SameJointTests F G t s') : s = t :=
  separated s t (same.trans same'.symm)

/-- **The joint tests carry pairs of parts exactly**, where both frames' pairs of parts are
compact, their tests stable, and their configurations told apart by the tests: wholes and parts
matched by the tests are held together in one frame exactly where in the other. -/
theorem SameJointTests.joint_iff {F : JointFrame S A C} {G : JointFrame S' A C}
    (joints : F.JointCompact) (joints' : G.JointCompact) (stable : F.TestsStable)
    (stable' : G.TestsStable) (separated : ∀ s t, SameJointTests F F s t → s = t)
    (separated' : ∀ s' t', SameJointTests G G s' t' → s' = t') {s l r : S} {s' l' r' : S'}
    (same : SameJointTests F G s s') (left : SameJointTests F G l l')
    (right : SameJointTests F G r r') : F.joint s l r ↔ G.joint s' l' r' :=
  ⟨fun joint => match SameJointTests.parts joints' same joint (stable l) (stable r) with
    | ⟨_, y, joint', atX, atY⟩ =>
      Eq.subst (motive := fun w => G.joint s' l' w)
        (SameJointTests.functional separated' atY right)
        (Eq.subst (motive := fun w => G.joint s' w y)
          (SameJointTests.functional separated' atX left) joint'),
   fun joint' => match SameJointTests.parts joints same.symm joint' (stable' l') (stable' r') with
    | ⟨_, y, joint, atX, atY⟩ =>
      Eq.subst (motive := fun w => F.joint s l w)
        (SameJointTests.inverse_functional separated atY.symm right)
        (Eq.subst (motive := fun w => F.joint s w y)
          (SameJointTests.inverse_functional separated atX.symm left) joint)⟩

/-- **The joint tests carry steps exactly**, where both frames' moves are compact, their tests
stable, and their configurations told apart by the tests. -/
theorem SameJointTests.step_iff {F : JointFrame S A C} {G : JointFrame S' A C}
    (steps : F.StepCompact) (steps' : G.StepCompact) (stable : F.TestsStable)
    (stable' : G.TestsStable) (separated : ∀ s t, SameJointTests F F s t → s = t)
    (separated' : ∀ s' t', SameJointTests G G s' t' → s' = t') {s t : S} {s' t' : S'}
    (same : SameJointTests F G s s') (same' : SameJointTests F G t t') (a : A) :
    F.P.step s a t ↔ G.P.step s' a t' :=
  ⟨fun step => match SameJointTests.step steps' same step (stable t) with
    | ⟨_, step', joined⟩ => Eq.subst (motive := fun w => G.P.step s' a w)
        (SameJointTests.functional separated' joined same') step',
   fun step' => match SameJointTests.step steps same.symm step' (stable' t') with
    | ⟨_, step, joined⟩ => Eq.subst (motive := fun w => F.P.step s a w)
        (SameJointTests.inverse_functional separated joined.symm same') step⟩

/-- **The joint tests match reachable configurations one to one**, where both frames' moves and
pairs of parts are compact, their tests stable, their configurations told apart by the tests, and
each frame reached from a root, the roots passing the same tests. -/
theorem SameJointTests.correspondence {F : JointFrame S A C} {G : JointFrame S' A C}
    (steps : F.StepCompact) (steps' : G.StepCompact) (joints : F.JointCompact)
    (joints' : G.JointCompact) (stable : F.TestsStable) (stable' : G.TestsStable)
    (separated : ∀ s t, SameJointTests F F s t → s = t)
    (separated' : ∀ s' t', SameJointTests G G s' t' → s' = t') {root : S} {root' : S'}
    (same : SameJointTests F G root root') (reach : ∀ s, JointFrame.Reach F root s)
    (reach' : ∀ s', JointFrame.Reach G root' s') :
    (∀ s, ∃ s', SameJointTests F G s s' ∧ ∀ t', SameJointTests F G s t' → t' = s') ∧
      (∀ s', ∃ s, SameJointTests F G s s' ∧ ∀ t, SameJointTests F G t s' → t = s) :=
  ⟨fun s => match (sameJointTests_bisimulation steps steps' joints joints' stable stable').reach
        same (reach s) with
    | ⟨s', _, joined⟩ => ⟨s', joined, fun _ joined' =>
        SameJointTests.functional separated' joined' joined⟩,
   fun s' => match (sameJointTests_bisimulation steps' steps joints' joints stable' stable).reach
        same.symm (reach' s') with
    | ⟨s, _, joined⟩ => ⟨s, joined.symm, fun _ joined' =>
        SameJointTests.inverse_functional separated joined' joined.symm⟩⟩

end Correspondence

section Codes

variable {S : Type u} {A : Type v} {C : Type w} {D : Type y} {Q : Type z} {R : Type x'}

/-- **Through a code reading the joint tests exactly and giving configurations passing the same
tests one code, the parts lift from each configuration it describes**, where the pairs of parts
are compact and the tests stable. -/
theorem liftsFromEach_of_exact {F : JointFrame S A C} {p : Presentation S (JointTest A C) D}
    (joints : F.JointCompact) (stable : F.TestsStable) (exact : Exact (JointTest.Holds F) p)
    (reduced : Reduced (JointTest.Holds F) p) : LiftsFromEach F.joint p.encode :=
  liftsFromEach_of_sameJointTests (reduced_exact_kernel exact reduced) joints stable

/-- Configurations given one code match parts into configurations given one code, where the code
reads the joint tests exactly, gives configurations passing the same tests one code, and the pairs
of parts are compact and the tests stable. -/
theorem matchesParts_of_exact {F : JointFrame S A C} {p : Presentation S (JointTest A C) D}
    (joints : F.JointCompact) (stable : F.TestsStable) (exact : Exact (JointTest.Holds F) p)
    (reduced : Reduced (JointTest.Holds F) p) :
    MatchesParts F.joint F.joint fun s t => p.encode s = p.encode t :=
  liftsFromEach_iff.mp (liftsFromEach_of_exact joints stable exact reduced)

/-- **A code realizes a plan exactly where each configuration it describes does**, where the code
reads the joint tests exactly, gives configurations passing the same tests one code, the leaves
are read correctly through it, and the pairs of parts are compact and the tests stable. -/
theorem JointPlan.realizes_code_iff {F : JointFrame S A C} {p : Presentation S (JointTest A C) D}
    (joints : F.JointCompact) (stable : F.TestsStable) (exact : Exact (JointTest.Holds F) p)
    (reduced : Reduced (JointTest.Holds F) p) {leaf : S → Q → Prop} {read : D → Q → Prop}
    (correct : ∀ s q, read (p.encode s) q ↔ leaf s q) (plan : JointPlan Q) (s : S) :
    JointPlan.Realizes (jointImage F.joint p.encode) read (p.encode s) plan ↔
      JointPlan.Realizes F.joint leaf s plan :=
  JointPlan.realizes_image_iff (matchesParts_of_exact joints stable exact reduced) correct plan s

/-- **A plan realized at a code is supported, without repetition, by the footprint of each
configuration it describes**, where footprints of parts lie within the whole's and apart, and
the code is as in `JointPlan.realizes_code_iff`. -/
theorem JointPlan.supports_of_code {F : JointFrame S A C} {p : Presentation S (JointTest A C) D}
    (joints : F.JointCompact) (stable : F.TestsStable) (exact : Exact (JointTest.Holds F) p)
    (reduced : Reduced (JointTest.Holds F) p) {footprint : S → R → Prop}
    (within : PartsWithin footprint F.joint) (apart : PartsApart footprint F.joint)
    {read : D → List R → Prop} (correct : ∀ s xs, read (p.encode s) xs ↔ Supports footprint s xs)
    (plan : JointPlan (List R)) (s : S)
    (realizes : JointPlan.Realizes (jointImage F.joint p.encode) read (p.encode s) plan) :
    Supports footprint s plan.draws :=
  JointPlan.supports_of_image (matchesParts_of_exact joints stable exact reduced) within apart
    correct plan s realizes

end Codes

end Becoming
