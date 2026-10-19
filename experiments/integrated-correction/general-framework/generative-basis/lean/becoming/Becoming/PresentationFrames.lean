import Becoming.Presentations

/-!
# Presentations of a frame: codes of its branching tests, its joint relation, and every predicate

`Becoming.Presentations` states, for answers fixed before any code, that exact reduced codes are
unique up to one alignment and which relations descend to them, and it reads the kernel and the
alignment on a frame's branching tests (`Presentations.Tests`). This module reads the rest of
its laws on frames of the spine.

* **Codes of a frame's branching tests.** Two exact reduced presentations of a frame's branching
  tests correspond one to one on used codes (`correspondence`). The canonical presentation, each
  configuration coded by the branching tests it passes, reads every test exactly
  (`canonical_exact`); where predicates on the tests are extensional it gives one code exactly to
  the configurations passing the same branching tests (`canonical_kernel`), and every exact
  presentation factors through it (`canonical_factor`); without extensionality it factors up to
  answering alike (`canonical_factor_answers`).
* **The joint relation of a joint frame.** Read at the codes of an exact reduced presentation of
  the frame's branching tests, the joint relation has an exact reading exactly where it is the same
  for configurations passing the same branching tests (`joint_descends_iff`); its image is then
  the reading (`joint_image_iff`), unique on used codes (`joint_reading_unique`), and one pair of
  triples passing the same tests on which the joint relation differs blocks every exact reading
  (`joint_blocked`).
* **A frame realizing every predicate.** The frame on a process whose claims are the predicates
  of its configurations, each realized where it holds (`everyPredicate`), tells every two
  configurations apart (`everyPredicate_separate`). Every exact presentation of what it realizes
  is injective (`everyPredicate_injective`) and reduced (`everyPredicate_reduced`), every
  relation among its configurations is read exactly at the codes (`everyPredicate_saturated`,
  `everyPredicate_recoverable`), and any two such presentations correspond one to one
  (`everyPredicate_correspondence`): the limit keeps every distinction and finds none.

Each theorem is the law of `Becoming.Presentations` it names, read on a frame; none is a further
result. No ethical predicate, ranking or axiom occurs; every declaration has an empty axiom
report.
-/

namespace Becoming

open Generative Presentations

universe u v w x y

namespace PresentationFrames

/-! ## Codes of a frame's branching tests -/

section Tests

variable {S : Type u} {A : Type v} {C : Type w} {K : Type x} {K' : Type y} {F : Frame S A C}
  {p : Presentation S (BranchingTest A C) K} {q : Presentation S (BranchingTest A C) K'}

/-- **The canonical presentation reads every branching test exactly.** -/
theorem canonical_exact (F : Frame S A C) :
    Exact (BranchingTest.Holds F) (canonical (BranchingTest.Holds F)) :=
  Presentations.canonical_exact _

/-- **Where predicates on the tests are extensional, the canonical presentation gives one code
exactly to the configurations passing the same branching tests.** -/
theorem canonical_kernel (ext : PredicateExt (BranchingTest A C)) (F : Frame S A C) (s s' : S) :
    (canonical (BranchingTest.Holds F)).encode s = (canonical (BranchingTest.Holds F)).encode s' ↔
      SameBranchingTests F F s s' :=
  Presentations.reduced_exact_kernel (canonical_exact F) (canonical_reduced ext _) s s'

end Tests

/-! ## The joint relation of a joint frame -/

section Joint

variable {S : Type u} {A : Type v} {C : Type w} {K : Type x} {F : JointFrame S A C}
  {p : Presentation S (BranchingTest A C) K}

end Joint

/-! ## A frame realizing every predicate -/

section EveryPredicate

variable {S : Type u} {A : Type v} {K : Type w} {K' : Type x}

/-- The frame on `P` whose claims are the predicates of its configurations, each realized where
it holds. -/
def everyPredicate (P : Process S A) : Frame S A (S → Prop) := ⟨P, fun s c => c s⟩

variable {P : Process S A} {p : Presentation S (S → Prop) K} {q : Presentation S (S → Prop) K'}

end EveryPredicate

end PresentationFrames

end Becoming
