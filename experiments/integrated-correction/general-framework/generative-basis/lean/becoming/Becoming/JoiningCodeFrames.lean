import Becoming.JoiningBridge
import ExplanatoryUniversality
import ExplanatoryJoiningRefinement

/-!
# Exact codes of a joining's frames

A joining is read in the core as frames (`Becoming.Joining`): through partners
(`Joining.frame`), where a fragment moves, with a partner on one side, to what the two join into,
and through roles (`Joining.roleFrame`). A joining context of the periphery realizes exactly what
its course of moves reaches in the partner frame (`Joining.realizes_iff_trace`). Four periphery
modules state laws of descriptions of a joining, with codes read either against branching
questions or against joining contexts; this module states those laws of the joining's frames and
proves them through the periphery's theorems.

* **Descent of the joining** (`ExplanatoryUniversality`). For an exact reduced description of the
  branching tests of the partner frame, some relation of codes reads the joining exactly, and the
  joining read through the codes (`ExplanatoryUniversality.Lift`) does, exactly where fragments
  passing the same branching tests join alike (`descends_iff`, `lift_exact_iff`); a joining that
  tells apart fragments passing the same branching tests has no exact reading on codes
  (`separating_blocks`). Two relations of codes reading exactly the joining of the traces of a
  process agree on every used code (`readings_agree`).
* **Courses of joinings** (`ExplanatoryContextualStructure`). An account of contexts reads exactly
  the courses open in the partner frame (`CourseExact`) exactly where it is exact for the
  periphery's contexts (`courseExact_iff`), and gives one code to fragments passing the same
tests of the partner frame exactly where it is reduced for them (`courseReduced_iff`). The
  canonical account, coding each fragment by the
  contexts possible from it, is such an account (`canonical_course_exact`); every such account
  gives different codes to fragments from one of which a course of joinings is open and from the
  other not (`codes_apart`), and its codes join exactly where the one-move course joining the
  second fragment on the right is open from the first (`joinable_iff`).
* **Passing the same tests of the partner frame is symmetric** (`sameTests_symm`), as agreeing on
  every joining context is (`ExplanatoryJoiningContexts`).
* **The identity is an open map of the role frame** (`identity_roles_open`), as the identity is an
  open map of the joining (`ExplanatoryJoiningRefinement`).

No ethical predicate, ranking or axiom occurs.
-/

namespace Becoming

open Generative

universe u v w

namespace JoiningCodeFrames

open ExplanatoryUniqueness ExplanatoryUniversality

/-! ## Descent of a joining to codes of its branching tests -/

section Descent

variable {F : Type u} {K : Type w} {J : Joining F}
  {p : Presentation F (BranchingTest (Joining.Move F) Empty) K}

/-- **Some relation of codes reads the joining exactly exactly where fragments passing the same
branching tests of the partner frame join alike**, for an exact reduced description of those
tests. -/
theorem descends_iff (hp : Exact (BranchingTest.Holds J.frame) p)
    (rp : Reduced (BranchingTest.Holds J.frame) p) :
    (∃ L, RelExact p J L) ↔
      ∀ a a' b b' c c', SameBranchingTests J.frame J.frame a a' →
        SameBranchingTests J.frame J.frame b b' → SameBranchingTests J.frame J.frame c c' →
          (J a b c ↔ J a' b' c') :=
  relation_descends_iff_saturated hp rp

/-- **The joining read through the codes reads it exactly exactly where fragments passing the same
branching tests of the partner frame join alike.** -/
theorem lift_exact_iff (hp : Exact (BranchingTest.Holds J.frame) p)
    (rp : Reduced (BranchingTest.Holds J.frame) p) :
    RelExact p J (Lift p J) ↔
      ∀ a a' b b' c c', SameBranchingTests J.frame J.frame a a' →
        SameBranchingTests J.frame J.frame b b' → SameBranchingTests J.frame J.frame c c' →
          (J a b c ↔ J a' b' c') :=
  lift_exact_iff_saturated hp rp

/-- **A joining that tells apart fragments passing the same branching tests of the partner frame
has no exact reading on the codes** of a reduced description of those tests. -/
theorem separating_blocks (rp : Reduced (BranchingTest.Holds J.frame) p) {a a' b b' c c' : F}
    (ha : SameBranchingTests J.frame J.frame a a') (hb : SameBranchingTests J.frame J.frame b b')
    (hc : SameBranchingTests J.frame J.frame c c') (yes : J a b c) (no : ¬ J a' b' c') :
    ¬ ∃ L, RelExact p J L :=
  separating_relation_blocks_descent rp ha hb hc yes no

end Descent

section Traces

open ExplanatoryLocalUnits

variable {S : Type u} {A : Type v} {Q : Type w} {K : Type w} {P : Process S A}

/-- **Two relations of codes reading exactly the joining of the traces of a process agree on every
used code.** -/
theorem readings_agree {p : Presentation (Admitted P) Q K} {L L' : K → K → K → Prop}
    (exact : RelExact p (traceJoin P) L) (exact' : RelExact p (traceJoin P) L') {x y z : K}
    (hx : ExplanatoryUniqueness.Used p x) (hy : ExplanatoryUniqueness.Used p y)
    (hz : ExplanatoryUniqueness.Used p z) : L x y z ↔ L' x y z :=
  relational_reading_unique_on_used exact exact' hx hy hz

end Traces

/-! ## Courses of joinings -/

section Courses

open ExplanatoryJoiningContexts ExplanatoryContextualStructure

variable {F : Type u} {K : Type v} {J : Joining F}

/-- A context is possible from a fragment exactly where its course of moves is open there in the
partner frame. -/
theorem possible_iff_course {c : Context F} {x : F} :
    Possible J c x ↔ ∃ t, Trace J.frame.P x (Joining.courseOf c) t :=
  ⟨fun ⟨t, realized⟩ => ⟨t, (Joining.realizes_iff_trace J c x t).mp realized⟩,
   fun ⟨t, path⟩ => ⟨t, (Joining.realizes_iff_trace J c x t).mpr path⟩⟩

/-- An account of contexts reads exactly the courses open in the partner frame. -/
def CourseExact (J : Joining F) (p : Account F K) : Prop :=
  ∀ x c, p.read (p.encode x) c ↔ ∃ t, Trace J.frame.P x (Joining.courseOf c) t

/-- **An account reads exactly the courses open in the partner frame exactly where it is exact for
the periphery's contexts.** -/
theorem courseExact_iff {p : Account F K} : CourseExact J p ↔ Exact (target J) p :=
  ⟨fun exact x c => (exact x c).trans possible_iff_course.symm,
   fun exact x c => (exact x c).trans possible_iff_course⟩

/-- An account of contexts gives one code to fragments passing the same tests of the partner
frame. -/
def CourseReduced (J : Joining F) (p : Account F K) : Prop :=
  ∀ x y, SameTests J.frame J.frame x y → p.encode x = p.encode y

/-- **An account gives one code to fragments passing the same tests of the partner frame exactly
where it is reduced for the periphery's contexts.** -/
theorem courseReduced_iff {p : Account F K} : CourseReduced J p ↔ Reduced (target J) p :=
  ⟨fun reduced x y same => reduced x y (Joining.contextSame_iff_sameTests.mp same),
   fun reduced x y same => reduced x y (Joining.contextSame_iff_sameTests.mpr same)⟩

/-- **The canonical account reads exactly the courses open in the partner frame.** -/
theorem canonical_course_exact (J : Joining F) : CourseExact J (canonical J) :=
  courseExact_iff.mpr (canonical_exact J)

/-- **An account reading exactly the courses of the partner frame gives different codes to two
fragments where a course is open from the first and not from the second.** -/
theorem codes_apart {p : Account F K} (exact : CourseExact J p) {x y : F} {c : Context F}
    (yes : ∃ t, Trace J.frame.P x (Joining.courseOf c) t)
    (no : ¬ ∃ t, Trace J.frame.P y (Joining.courseOf c) t) : p.encode x ≠ p.encode y :=
  different_realization_forces_distinction (courseExact_iff.mp exact) (possible_iff_course.mpr yes)
    fun possible => no (possible_iff_course.mp possible)

/-- **The codes of two fragments join exactly where the one-move course joining the second on the
right is open from the first**, for an account reading exactly the courses of the partner
frame. -/
theorem joinable_iff {p : Account F K} (exact : CourseExact J p) (x y : F) :
    (∃ k, Operation J p (p.encode x) (p.encode y) k) ↔
      ∃ z, Trace J.frame.P x [Joining.Move.withRight y] z :=
  (operation_domain_exact (courseExact_iff.mp exact) x y).trans
    ⟨fun ⟨z, joined⟩ => ⟨z, trace_singleton_iff.mpr joined⟩,
     fun ⟨z, path⟩ => ⟨z, (trace_singleton_iff (P := J.frame.P)).mp path⟩⟩

/-- **Passing the same tests of the partner frame is symmetric**, as agreeing on every joining
context is. -/
theorem sameTests_symm {x y : F} (same : SameTests J.frame J.frame x y) :
    SameTests J.frame J.frame y x :=
  Joining.contextSame_iff_sameTests.mp (same_symm (Joining.contextSame_iff_sameTests.mpr same))

end Courses

/-! ## Roles -/

section Roles

variable {F : Type u}

/-- **The identity is an open map of the role frame of every joining.** -/
theorem identity_roles_open (J : Joining F) :
    ∃ keeps : Joining.Keeps J J id, OpenMap J.roleFrame J.roleFrame (Joining.placeMap keeps) :=
  Joining.openMap_iff.mp (Joining.openMap_iff_incidence.mp (ExplanatoryJoiningRefinement.identity_open J))

end Roles

end JoiningCodeFrames

end Becoming
