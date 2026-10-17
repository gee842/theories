import Becoming.Likeness
import ExplanatoryUniqueness

/-!
# Exact codes of a frame's branching tests

`ExplanatoryUniqueness` states, for models and a fixed family of questions, when a presentation
(a code for each model with a reading of each code) answers the questions exactly, when it is
reduced (models answering alike get one code), and that two exact reduced presentations have one
kernel and are aligned one to one. Here the models are the configurations of a frame and the
questions are its branching tests (`BranchingTest.Holds`): an exact presentation is a description
of configurations whose codes read exactly where each branching test holds, and answering alike is
passing the same branching tests (`SameBranchingTests`). This module states the periphery's
general laws of such descriptions of a frame and proves them through those laws.

* **The kernel is passing the same branching tests**: an exact reduced description gives two
  configurations one code exactly where they pass the same branching tests (`kernel_iff`), so
  alike configurations get one code (`alike_one_code`), and **two exact reduced descriptions have
  one kernel** (`kernels_same`).
* **Codes match exactly where they read alike on every branching test**: for exact descriptions,
  the second reduced, a code of the first and one of the second belong to one configuration
  exactly where both are used and they read alike on every test (`matches_iff`).
* **The alignment is the only one**: a relation between codes holding at the codes of every
  configuration and giving at most one partner relates a used code exactly to the codes it
  matches, which are those reading alike on every branching test (`aligned_iff`).

No ethical predicate, ranking or axiom occurs.
-/

namespace Becoming

open Generative

universe u v w x y

namespace TestCodeFrames

open ExplanatoryUniqueness

variable {S : Type u} {A : Type v} {C : Type w} {K : Type x} {K' : Type y} {F : Frame S A C}
  {p : Presentation S (BranchingTest A C) K} {q : Presentation S (BranchingTest A C) K'}

/-- **An exact reduced description of a frame's branching tests gives two configurations one code
exactly where they pass the same branching tests.** -/
theorem kernel_iff (hp : Exact (BranchingTest.Holds F) p) (rp : Reduced (BranchingTest.Holds F) p)
    (s s' : S) : p.encode s = p.encode s' ↔ SameBranchingTests F F s s' :=
  reduced_exact_kernel hp rp s s'

/-- **Alike configurations get one code** from every reduced description of a frame's branching
tests. -/
theorem alike_one_code (rp : Reduced (BranchingTest.Holds F) p) {s s' : S} (alike : Alike F F s s') :
    p.encode s = p.encode s' :=
  rp s s' alike.sameBranchingTests

/-- **Two exact reduced descriptions of a frame's branching tests have one kernel.** -/
theorem kernels_same (hp : Exact (BranchingTest.Holds F) p) (rp : Reduced (BranchingTest.Holds F) p)
    (hq : Exact (BranchingTest.Holds F) q) (rq : Reduced (BranchingTest.Holds F) q) (s s' : S) :
    p.encode s = p.encode s' ↔ q.encode s = q.encode s' :=
  reduced_presentations_same_kernel hp rp hq rq s s'

/-- **Codes of two exact descriptions of a frame's branching tests, the second reduced, belong to
one configuration exactly where both are used and they read alike on every branching test.** -/
theorem matches_iff (hp : Exact (BranchingTest.Holds F) p) (hq : Exact (BranchingTest.Holds F) q)
    (rq : Reduced (BranchingTest.Holds F) q) (k : K) (k' : K') :
    Matches p q k k' ↔
      ExplanatoryUniqueness.Used p k ∧ ExplanatoryUniqueness.Used q k' ∧ ∀ φ, p.read k φ ↔ q.read k' φ :=
  matches_iff_equal_answers hp hq rq k k'

/-- **The alignment of two exact descriptions of a frame's branching tests is the only one.** A
relation between codes holding at the codes of every configuration, and giving each code at most
one partner, relates a used code exactly to the codes reading alike with it on every branching
test. -/
theorem aligned_iff (hp : Exact (BranchingTest.Holds F) p) (hq : Exact (BranchingTest.Holds F) q)
    (rq : Reduced (BranchingTest.Holds F) q) (B : K → K' → Prop)
    (aligned : ∀ s, B (p.encode s) (q.encode s))
    (functional : ∀ k k' k'', B k k' → B k k'' → k' = k'')
    {k : K} {k' : K'} (used : ExplanatoryUniqueness.Used p k) :
    B k k' ↔
      ExplanatoryUniqueness.Used p k ∧ ExplanatoryUniqueness.Used q k' ∧ ∀ φ, p.read k φ ↔ q.read k' φ :=
  (unique_matching p q B aligned functional used).trans (matches_iff_equal_answers hp hq rq k k')

end TestCodeFrames

end Becoming
