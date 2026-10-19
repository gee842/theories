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

/-- **Two exact reduced presentations of a frame's branching tests correspond one to one on used
codes.** -/
theorem correspondence (hp : Exact (BranchingTest.Holds F) p) (rp : Reduced (BranchingTest.Holds F) p)
    (hq : Exact (BranchingTest.Holds F) q) (rq : Reduced (BranchingTest.Holds F) q) :
    (∀ k, Used p k → ∃ k', Matches p q k k' ∧ ∀ e, Matches p q k e → e = k') ∧
      (∀ k', Used q k' → ∃ k, Matches p q k k' ∧ ∀ e, Matches p q e k' → e = k) :=
  relative_unique_correspondence hp rp hq rq

/-- **The canonical presentation reads every branching test exactly.** -/
theorem canonical_exact (F : Frame S A C) :
    Exact (BranchingTest.Holds F) (canonical (BranchingTest.Holds F)) :=
  Presentations.canonical_exact _

/-- **Where predicates on the tests are extensional, the canonical presentation gives one code
exactly to the configurations passing the same branching tests.** -/
theorem canonical_kernel (ext : PredicateExt (BranchingTest A C)) (F : Frame S A C) (s s' : S) :
    (canonical (BranchingTest.Holds F)).encode s = (canonical (BranchingTest.Holds F)).encode s' ↔
      SameBranchingTests F F s s' :=
  Tests.kernel_iff (canonical_exact F) (canonical_reduced ext _) s s'

/-- **Every exact presentation of a frame's branching tests factors through the canonical one, up
to answering alike**, with no extensionality. -/
theorem canonical_factor_answers (hp : Exact (BranchingTest.Holds F) p) :
    (∀ k, Used p k → ∃ d, Used (canonical (BranchingTest.Holds F)) d ∧
      Matches p (canonical (BranchingTest.Holds F)) k d ∧
      ∀ e, Matches p (canonical (BranchingTest.Holds F)) k e → ∀ φ, e φ ↔ d φ) ∧
    (∀ d, Used (canonical (BranchingTest.Holds F)) d → ∃ k, Used p k ∧
      Matches p (canonical (BranchingTest.Holds F)) k d) :=
  Presentations.canonical_factor_answers hp

/-- **Where predicates on the tests are extensional, every exact presentation of a frame's
branching tests factors through the canonical one.** -/
theorem canonical_factor (ext : PredicateExt (BranchingTest A C)) (hp : Exact (BranchingTest.Holds F) p) :
    (∀ k, Used p k → ∃ d, Used (canonical (BranchingTest.Holds F)) d ∧
      Matches p (canonical (BranchingTest.Holds F)) k d ∧
      ∀ e, Matches p (canonical (BranchingTest.Holds F)) k e → e = d) ∧
    (∀ d, Used (canonical (BranchingTest.Holds F)) d → ∃ k, Used p k ∧
      Matches p (canonical (BranchingTest.Holds F)) k d) :=
  Presentations.canonical_factor ext hp

end Tests

/-! ## The joint relation of a joint frame -/

section Joint

variable {S : Type u} {A : Type v} {C : Type w} {K : Type x} {F : JointFrame S A C}
  {p : Presentation S (BranchingTest A C) K}

/-- **The joint relation has an exact reading at the codes of an exact reduced presentation of the
branching tests exactly where it is the same for configurations passing the same tests.** -/
theorem joint_descends_iff (hp : Exact (BranchingTest.Holds F.toFrame) p)
    (rp : Reduced (BranchingTest.Holds F.toFrame) p) :
    (∃ R, RelExact p F.joint R) ↔ Saturated (BranchingTest.Holds F.toFrame) F.joint :=
  relation_descends_iff_saturated hp rp

/-- **The image of the joint relation is then its exact reading.** -/
theorem joint_image_iff (hp : Exact (BranchingTest.Holds F.toFrame) p)
    (rp : Reduced (BranchingTest.Holds F.toFrame) p) :
    RelExact p F.joint (jointImage F.joint p.encode) ↔
      Saturated (BranchingTest.Holds F.toFrame) F.joint :=
  lift_exact_iff_saturated hp rp

/-- **Exact readings of the joint relation agree on used codes.** -/
theorem joint_reading_unique {R R' : K → K → K → Prop} (hk : RelExact p F.joint R)
    (hl : RelExact p F.joint R') {x y z : K} (hx : Used p x) (hy : Used p y) (hz : Used p z) :
    R x y z ↔ R' x y z :=
  relational_reading_unique_on_used hk hl hx hy hz

/-- **One pair of triples passing the same branching tests on which the joint relation differs
blocks every exact reading.** -/
theorem joint_blocked (rp : Reduced (BranchingTest.Holds F.toFrame) p) {a a' b b' c c' : S}
    (ha : SameBranchingTests F.toFrame F.toFrame a a') (hb : SameBranchingTests F.toFrame F.toFrame b b')
    (hc : SameBranchingTests F.toFrame F.toFrame c c') (yes : F.joint a b c) (no : ¬ F.joint a' b' c') :
    ¬ ∃ R, RelExact p F.joint R :=
  separating_relation_blocks_descent rp ha hb hc yes no

end Joint

/-! ## A frame realizing every predicate -/

section EveryPredicate

variable {S : Type u} {A : Type v} {K : Type w} {K' : Type x}

/-- The frame on `P` whose claims are the predicates of its configurations, each realized where
it holds. -/
def everyPredicate (P : Process S A) : Frame S A (S → Prop) := ⟨P, fun s c => c s⟩

variable {P : Process S A} {p : Presentation S (S → Prop) K} {q : Presentation S (S → Prop) K'}

/-- **A frame realizing every predicate tells every two configurations apart.** -/
theorem everyPredicate_separate (s s' : S) :
    SameAnswers (everyPredicate P).realized s s' ↔ s = s' :=
  all_predicates_separate s s'

/-- **Every exact presentation of what it realizes is injective.** -/
theorem everyPredicate_injective (hp : Exact (everyPredicate P).realized p) :
    ∀ s s', p.encode s = p.encode s' → s = s' :=
  all_predicates_force_injective hp

/-- **Every presentation of what it realizes is reduced.** -/
theorem everyPredicate_reduced (p : Presentation S (S → Prop) K) :
    Reduced (everyPredicate P).realized p :=
  all_predicates_automatically_reduced p

/-- **Every relation among its configurations is the same for configurations answering alike.** -/
theorem everyPredicate_saturated (J : S → S → S → Prop) : Saturated (everyPredicate P).realized J :=
  all_predicates_every_relation J

/-- **Every relation is read exactly at the codes of an exact presentation**, by its image. -/
theorem everyPredicate_recoverable (hp : Exact (everyPredicate P).realized p) (J : S → S → S → Prop) :
    RelExact p J (jointImage J p.encode) :=
  all_predicates_relation_recoverable hp J

/-- **Any two exact presentations of what it realizes correspond one to one on used codes.** -/
theorem everyPredicate_correspondence (hp : Exact (everyPredicate P).realized p)
    (hq : Exact (everyPredicate P).realized q) :
    (∀ k, Used p k → ∃ k', Matches p q k k' ∧ ∀ e, Matches p q k e → e = k') ∧
      (∀ k', Used q k' → ∃ k, Matches p q k k' ∧ ∀ e, Matches p q e k' → e = k) :=
  all_predicates_unique_correspondence hp hq

end EveryPredicate

end PresentationFrames

end Becoming
