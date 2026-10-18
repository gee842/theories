import Becoming.JoiningContexts
import Becoming.BranchingCorrespondence

/-!
# Joining codes: a joining read through codes of its contexts and of its branching tests

`Becoming.Joining` reads a joining through a description (`Joining.image`) and shows that the
description lifts the joining exactly where having one code is a bisimulation of the joining's
frame (`Joining.lifts_iff`). This module states what follows for codes read against the two
kinds of question the joining itself poses: its contexts (`Becoming.JoiningContexts`) and the
branching tests of its frame.

* **Codes of contexts.** A presentation reading exactly which contexts are possible gives one code
  only to fragments agreeing on contexts (`codes_contextSame`), so the codes join exactly where the
  fragments do (`image_domain_iff`). Where joining is functional and the presentation also gives
  fragments agreeing on contexts one code, the codes join exactly into the code of what the
  fragments join into (`image_realized_iff`) and so join functionally (`image_functional`); two such
  presentations read one joining of codes along their matching (`image_iff_of_matches`).
* **Codes of branching tests.** A branching test asked after a context holds exactly where the
  context realizes something passing it (`Context.holds_ask`), so fragments passing the same
  branching tests agree on contexts (`ContextSame.of_sameBranchingTests`). Under excluded middle,
  where each pair joins into listed fragments, fragments passing the same branching tests join into
  fragments passing the same branching tests (`FiniteOutcomes.joined_sameBranchingTests_of_em`) and
  a presentation reading the tests exactly and reducedly lifts the joining
  (`FiniteOutcomes.lifts_of_exact`).

Excluded middle is a named hypothesis wherever it is used; every declaration's axiom report is
empty. Ported from `Generative.ExplanatoryContextualStructure` and
`Generative.ExplanatoryJoiningBranches` (bridge fold F3E, 18 October 2026); the port is a
restatement on the core's joinings, not a new result. The periphery's `Account`, `target` and
`Operation J p` are `Presentation F (Context F) C`, `possibleAnswers J` and
`J.image p.encode`.
-/

universe u v w

namespace Becoming

open Generative
open Becoming.Presentations

namespace Joining

variable {F : Type u} {C : Type v} {D : Type w}

/-! ## Codes of contexts -/

/-- Which contexts are possible for a fragment. -/
def possibleAnswers (J : Joining F) (x : F) (c : Context F) : Prop := c.Possible J x

/-- **Codes reading the possible contexts exactly are given only to fragments agreeing on
contexts.** -/
theorem codes_contextSame {J : Joining F} {p : Presentation F (Context F) C}
    (exact : Exact (possibleAnswers J) p) {x y : F} (equal : p.encode x = p.encode y) :
    ContextSame J x y :=
  equal_codes_same_answers exact equal

/-- **A context possible for one fragment and not for another gives them different codes.** -/
theorem codes_apart_of_possible {J : Joining F} {p : Presentation F (Context F) C}
    (exact : Exact (possibleAnswers J) p) {x y : F} {c : Context F} (possible : c.Possible J x)
    (impossible : ¬ c.Possible J y) : p.encode x ≠ p.encode y :=
  fun equal => impossible ((codes_contextSame exact equal c).mp possible)

/-- **The codes of two fragments join exactly where the fragments do.** -/
theorem image_domain_iff {J : Joining F} {p : Presentation F (Context F) C}
    (exact : Exact (possibleAnswers J) p) (x y : F) :
    (∃ c, J.image p.encode (p.encode x) (p.encode y) c) ↔ J.Composable x y :=
  ⟨fun ⟨_, _, _, z, atX, atY, _, joined⟩ =>
    (ContextSame.composable_iff (codes_contextSame exact atX) (codes_contextSame exact atY)).mp
      ⟨z, joined⟩,
   fun ⟨z, joined⟩ => ⟨p.encode z, image_of J p.encode joined⟩⟩

/-- **Where joining is functional, the codes of two fragments join exactly into the code of what
they join into**, for a presentation reading the possible contexts exactly and giving fragments
agreeing on contexts one code. -/
theorem image_realized_iff {J : Joining F} (fn : J.Functional) {p : Presentation F (Context F) C}
    (exact : Exact (possibleAnswers J) p) (reduced : Reduced (possibleAnswers J) p) {x y z : F}
    (joined : J x y z) (c : C) : J.image p.encode (p.encode x) (p.encode y) c ↔ p.encode z = c :=
  ⟨fun ⟨_, _, d, atX, atY, atD, joined'⟩ =>
    (reduced d z (ContextSame.joined fn (codes_contextSame exact atX) (codes_contextSame exact atY)
      joined' joined)).symm.trans atD,
   fun at_ => ⟨x, y, z, rfl, rfl, at_, joined⟩⟩

/-- **Where joining is functional, the codes join functionally.** -/
theorem image_functional {J : Joining F} (fn : J.Functional) {p : Presentation F (Context F) C}
    (exact : Exact (possibleAnswers J) p) (reduced : Reduced (possibleAnswers J) p) :
    (J.image p.encode).Functional :=
  fun _ _ _ d ⟨_, _, _, atX, atY, atZ, joined⟩ second =>
    atZ.symm.trans ((image_realized_iff fn exact reduced joined d).mp
      (Eq.subst (motive := fun a => J.image p.encode a _ d) atX.symm
        (Eq.subst (motive := fun b => J.image p.encode _ b d) atY.symm second)))

/-- **Codes joining under one presentation join under another along their matching**, where the
first reads the possible contexts exactly and the second gives fragments agreeing on contexts one
code. -/
theorem image_transport {J : Joining F} {p : Presentation F (Context F) C}
    {r : Presentation F (Context F) D} (exact : Exact (possibleAnswers J) p)
    (reduced : Reduced (possibleAnswers J) r) {a b c : C} {a' b' c' : D} (ha : Matches p r a a')
    (hb : Matches p r b b') (hc : Matches p r c c') (joined : J.image p.encode a b c) :
    J.image r.encode a' b' c' :=
  match joined with
  | ⟨x, y, z, atX, atY, atZ, joined'⟩ =>
    ⟨x, y, z, matches_functional exact reduced ⟨x, atX, rfl⟩ ha,
      matches_functional exact reduced ⟨y, atY, rfl⟩ hb,
      matches_functional exact reduced ⟨z, atZ, rfl⟩ hc, joined'⟩

/-- **Two presentations reading the possible contexts exactly and reducedly read one joining of
codes along their matching.** -/
theorem image_iff_of_matches {J : Joining F} {p : Presentation F (Context F) C}
    {r : Presentation F (Context F) D} (exact : Exact (possibleAnswers J) p)
    (reduced : Reduced (possibleAnswers J) p) (exact' : Exact (possibleAnswers J) r)
    (reduced' : Reduced (possibleAnswers J) r) {a b c : C} {a' b' c' : D} (ha : Matches p r a a')
    (hb : Matches p r b b') (hc : Matches p r c c') :
    J.image p.encode a b c ↔ J.image r.encode a' b' c' :=
  have swap : ∀ {x : C} {y : D}, Matches p r x y → Matches r p y x :=
    fun ⟨m, atX, atY⟩ => ⟨m, atY, atX⟩
  ⟨image_transport exact reduced' ha hb hc, image_transport exact' reduced (swap ha) (swap hb) (swap hc)⟩

/-! ## Codes of branching tests -/

/-- A branching test asked after a context: the context's moves, innermost first, then the test. -/
def Context.ask : Context F → BranchingTest (Move F) Empty → BranchingTest (Move F) Empty
  | .hole, φ => φ
  | .left a c, φ => c.ask (.can (.withLeft a) φ)
  | .right c a, φ => c.ask (.can (.withRight a) φ)

/-- **A test asked after a context holds exactly where the context realizes something passing
it.** -/
theorem Context.holds_ask (J : Joining F) :
    ∀ (c : Context F) (x : F) (φ : BranchingTest (Move F) Empty),
      BranchingTest.Holds J.frame x (c.ask φ) ↔ ∃ y, c.Realizes J x y ∧ BranchingTest.Holds J.frame y φ
  | .hole, x, _ => ⟨fun holds => ⟨x, .nil x, holds⟩,
      fun ⟨_, path, holds⟩ => Eq.subst (motive := fun w => BranchingTest.Holds J.frame w _)
        (trace_nil_iff.mp path).symm holds⟩
  | .left a c, x, _ =>
    (Context.holds_ask J c x _).trans
      ⟨fun ⟨m, inner, y, joined, holds⟩ =>
        ⟨y, (Context.realizes_left J a c x y).mpr ⟨m, inner, joined⟩, holds⟩,
       fun ⟨y, realized, holds⟩ => match (Context.realizes_left J a c x y).mp realized with
        | ⟨m, inner, joined⟩ => ⟨m, inner, y, joined, holds⟩⟩
  | .right c a, x, _ =>
    (Context.holds_ask J c x _).trans
      ⟨fun ⟨m, inner, y, joined, holds⟩ =>
        ⟨y, (Context.realizes_right J c a x y).mpr ⟨m, inner, joined⟩, holds⟩,
       fun ⟨y, realized, holds⟩ => match (Context.realizes_right J c a x y).mp realized with
        | ⟨m, inner, joined⟩ => ⟨m, inner, y, joined, holds⟩⟩

/-- **Fragments passing the same branching tests agree on contexts.** -/
theorem ContextSame.of_sameBranchingTests {J : Joining F} {x y : F}
    (same : SameBranchingTests J.frame J.frame x y) : ContextSame J x y :=
  fun c =>
    ⟨fun ⟨z, realized⟩ => match (Context.holds_ask J c y .top).mp
        ((same (c.ask .top)).mp ((Context.holds_ask J c x .top).mpr ⟨z, realized, True.intro⟩)) with
      | ⟨w, realized', _⟩ => ⟨w, realized'⟩,
     fun ⟨w, realized'⟩ => match (Context.holds_ask J c x .top).mp
        ((same (c.ask .top)).mpr ((Context.holds_ask J c y .top).mpr ⟨w, realized', True.intro⟩)) with
      | ⟨z, realized, _⟩ => ⟨z, realized⟩⟩

/-- **Under excluded middle, fragments passing the same branching tests join into fragments
passing the same branching tests**, where each pair joins into listed fragments. -/
theorem FiniteOutcomes.joined_sameBranchingTests_of_em (em : ∀ p : Prop, Decided p) {J : Joining F}
    (finite : J.FiniteOutcomes) {a a' b b' z : F} (same : SameBranchingTests J.frame J.frame a a')
    (same' : SameBranchingTests J.frame J.frame b b') (joined : J a b z) :
    ∃ z', J a' b' z' ∧ SameBranchingTests J.frame J.frame z z' :=
  match SameBranchingTests.step_of_em (a := Move.withRight b) em finite.outcomes same joined with
  | ⟨_, joined', atM⟩ =>
    match SameBranchingTests.step_of_em (a := Move.withLeft a') em finite.outcomes same' joined' with
    | ⟨z', joined'', atZ⟩ => ⟨z', joined'', atM.trans atZ⟩

/-- **Under excluded middle, a presentation reading the branching tests exactly and reducedly lifts
a joining whose pairs join into listed fragments.** -/
theorem FiniteOutcomes.lifts_of_exact (em : ∀ p : Prop, Decided p) {J : Joining F}
    (finite : J.FiniteOutcomes) {p : Presentation F (BranchingTest (Move F) Empty) C}
    (exact : Exact (BranchingTest.Holds J.frame) p) (reduced : Reduced (BranchingTest.Holds J.frame) p) :
    J.Lifts p.encode :=
  lifts_of_identifiesAlike (finite.identifiesAlike em (reduced_exact_kernel exact reduced))

end Joining

end Becoming
