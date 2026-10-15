import Becoming.Unfolding

/-!
# What histories fix

Ren, 12 October 2026: "move towards 100%". One part of the gap was completeness in the strong
sense, the laws of a kind being all its laws, which the theory had for counting only (every tally
is counted by some listing, `tally_iff_counted`). `Becoming.Unfolding` (P69) showed that a history
fixes the law it shows and named where the correspondence is not an identity: a law can have a
step no history takes (`DeadEnd`), and a history that revisits shows a law admitting histories it
never took (`Splice`). This module shows that these two are the whole of it, for families of
histories, and states what tests fix of likeness. No premise beyond what each theorem names.

* **A family of histories is a law's exactly where it holds its splices.** The law a family shows
  is the least law admitting each of its histories (`ShownBy`, `shownBy_le_iff`). The histories of
  a law hold every sequence made of their own steps (`admits_spliceClosed`), and a family is the
  family of some law's histories exactly where it does (`SpliceClosed`, `family_iff`); for a
  determined law, exactly where it also never takes one move at one configuration to two
  outcomes (`ConsistentFamily`, `shownBy_determined_iff`, `determined_family_iff`).
* **Histories fix a law up to its dead ends.** The live steps of a law are those some history of
  it takes (`live`); a law and its live steps admit the same histories (`admits_live_iff`), two
  laws admit the same histories exactly where they have the same live steps
  (`same_histories_iff`), and the live law has no dead end (`live_live`). The dead end's step is
  not live (`DeadEnd.not_live`). So laws up to dead ends and families holding their splices
  correspond one to one: splicing and dead ends are the whole law of law and history.
* **With histories that stop, no dead end remains.** Two laws have the same finite histories
  exactly where they have the same steps (`same_finite_histories_iff`), and a family of finite
  histories is a law's exactly where the empty course goes nowhere and a course is a first step
  followed by the rest (`MadeOfSteps`, `finite_family_iff`). The dead end is a fact of unending
  histories; splicing is built into every law.
* **Tests fix likeness where branching is determined up to likeness.** Two configurations pass the
  same tests where the same courses of moves are open from each and the same claims can be
  realized after each course (`SameTests`); alike configurations do (`Alike.sameTests`). Where both
  frames are determined up to likeness, passing the same tests is a bisimulation
  (`sameTests_bisimulation`), so configurations are alike exactly where they pass the same tests
  (`alike_iff_sameTests`, `Determined.alike_iff_sameTests`). Where branching is not determined the
  tests do not fix likeness: a frame choosing after its first move and one choosing at it pass the
  same tests from their starts and are not alike (`Choosing.sameTests`, `Choosing.not_alike`,
  `Choosing.early_not_determined`). Tests that branch, with negation and conjunction, fix
  likeness for frames with finitely many outcomes of each move; that is
  `ExplanatoryBranching.same_iff_bisimilar` in the periphery, classical, joined to the core's
  `Bisimulation` by `branching_bisimulation_iff` where the bridge section of P69 is taken. In the
  core they fix it constructively for frames with finitely many configurations whose steps and
  claims are decided (`alike_iff_sameBranchingTests` of `Becoming.Likeness`).

**Readings.** The AI's, adopted on Ren's delegation of 15 October 2026 (DELEGATED-CHOICES D32). Ren
agreed (12 October 2026) that law and history are one unfolding read two ways, the law read off the
unfolding rather than set over it ("there are no two realities"). Read with this module: a law read
off histories is a family of histories holding its splices, and nothing else; what a law set over
the unfolding can add are dead ends, which no history shows. The splice is memory's absence: a law
answers from where one is, not from how one came there, so a family that remembers how it came (a
kept history) shows a law with no other history (`Run.keepHistory_shown`). What tests cannot see is
when a choice is made: with branching, only tests that branch see it.

What is not derived: whether an unfolding's histories stop (the core's runs are unending, which is
where dead ends come from; with histories that stop there are none); that
tests that branch fix likeness, in the core, beyond frames with finitely many configurations whose
steps and claims are decided, where `Becoming.Likeness` proves it constructively (the periphery's
proof, for finitely many outcomes of each move, reasons classically; the direction from likeness to
the periphery's tests, `Alike.same`, is in the bridge section); which family an actual unfolding
is.
-/

namespace Becoming

open Generative

universe u v w u'

/-! ## A family of histories and its law -/

section Family

variable {S : Type u} {A : Type v}

/-- A law admits a history where every step the history takes is a step of the law. -/
def Admits (P : Process S A) (g : Nat → S) (m : Nat → A) : Prop :=
  ∀ n, P.step (g n) (m n) (g (n + 1))

/-- A run's history is admitted by its law. -/
theorem Run.admits {P : Process S A} (r : Run P) : Admits P r.state r.act :=
  r.step

/-- The law a family of histories shows: the steps its histories take. -/
def ShownBy (H : (Nat → S) → (Nat → A) → Prop) : Process S A :=
  ⟨fun s a t => ∃ g m n, H g m ∧ g n = s ∧ m n = a ∧ g (n + 1) = t⟩

variable {H : (Nat → S) → (Nat → A) → Prop}

/-- Every history of a family is admitted by the law the family shows. -/
theorem ShownBy.admits {g : Nat → S} {m : Nat → A} (held : H g m) : Admits (ShownBy H) g m :=
  fun n => ⟨g, m, n, held, rfl, rfl, rfl⟩

/-- **The law a family shows is the least law admitting each of its histories.** -/
theorem shownBy_le_iff {Q : Process S A} :
    (∀ s a t, (ShownBy H).step s a t → Q.step s a t) ↔ ∀ g m, H g m → Admits Q g m :=
  ⟨fun le g m held n => le _ _ _ ⟨g, m, n, held, rfl, rfl, rfl⟩,
   fun admits _ _ _ ⟨g, m, n, held, at_s, by_a, to_t⟩ => at_s ▸ by_a ▸ to_t ▸ admits g m held n⟩

/-- A family holds its splices where it holds every sequence made of its own steps. -/
def SpliceClosed (H : (Nat → S) → (Nat → A) → Prop) : Prop :=
  ∀ g m, Admits (ShownBy H) g m → H g m

/-- **The histories of a law hold their splices.** -/
theorem admits_spliceClosed (P : Process S A) : SpliceClosed (Admits P) :=
  fun _ _ made n => match made n with
    | ⟨_, _, k, admits, at_s, by_a, to_t⟩ => at_s ▸ by_a ▸ to_t ▸ admits k

/-- **A family of histories is the family of a law's histories exactly where it holds its
splices**, and the law it shows is then one such law. -/
theorem family_iff :
    (∃ P : Process S A, ∀ g m, H g m ↔ Admits P g m) ↔ SpliceClosed H :=
  ⟨fun ⟨P, same⟩ g m made => (same g m).mpr (admits_spliceClosed P g m fun n =>
      match made n with
      | ⟨g', m', k, held, at_s, by_a, to_t⟩ => ⟨g', m', k, (same g' m').mp held, at_s, by_a, to_t⟩),
   fun closed => ⟨ShownBy H, fun _ _ => ⟨ShownBy.admits, closed _ _⟩⟩⟩

/-- A family is consistent where no two of its histories take one move at one configuration to
two outcomes. -/
def ConsistentFamily (H : (Nat → S) → (Nat → A) → Prop) : Prop :=
  ∀ g m g' m' i j, H g m → H g' m' → g i = g' j → m i = m' j → g (i + 1) = g' (j + 1)

/-- **The law a family shows is determined exactly where the family is consistent.** -/
theorem shownBy_determined_iff : Determined (ShownBy H) ↔ ConsistentFamily H :=
  ⟨fun determined g m g' m' i j held held' same same' =>
    determined (g i) (m i) (g (i + 1)) (g' (j + 1)) ⟨g, m, i, held, rfl, rfl, rfl⟩
      ⟨g', m', j, held', same.symm, same'.symm, rfl⟩,
   fun consistent _ _ _ _ ⟨g, m, i, held, at_s, by_a, to_t⟩ ⟨g', m', j, held', at_s', by_a', to_t'⟩ =>
    to_t.symm.trans ((consistent g m g' m' i j held held' (at_s.trans at_s'.symm)
      (by_a.trans by_a'.symm)).trans to_t')⟩

/-- **A family is the family of a determined law's histories exactly where it holds its splices
and is consistent.** -/
theorem determined_family_iff :
    (∃ P : Process S A, Determined P ∧ ∀ g m, H g m ↔ Admits P g m) ↔
      SpliceClosed H ∧ ConsistentFamily H :=
  ⟨fun ⟨P, determined, same⟩ =>
    ⟨family_iff.mp ⟨P, same⟩,
     fun g m g' m' i j held held' same_s same_a =>
      have there : P.step (g i) (m i) (g' (j + 1)) := same_s ▸ same_a ▸ (same g' m').mp held' j
      determined _ _ _ _ ((same g m).mp held i) there⟩,
   fun ⟨closed, consistent⟩ =>
    ⟨ShownBy H, shownBy_determined_iff.mpr consistent, fun _ _ => ⟨ShownBy.admits, closed _ _⟩⟩⟩

end Family

/-! ## The live steps of a law -/

section Live

variable {S : Type u} {A : Type v}

/-- The live steps of a law: those some history of it takes. -/
def live (P : Process S A) : Process S A :=
  ShownBy (Admits P)

/-- A live step is a step. -/
theorem live_le (P : Process S A) : ∀ s a t, (live P).step s a t → P.step s a t :=
  shownBy_le_iff.mpr fun _ _ admits => admits

/-- **A law and its live steps admit the same histories.** -/
theorem admits_live_iff {P : Process S A} {g : Nat → S} {m : Nat → A} :
    Admits (live P) g m ↔ Admits P g m :=
  ⟨fun admits n => live_le P _ _ _ (admits n), ShownBy.admits⟩

/-- **Two laws admit the same histories exactly where they have the same live steps.** What a law
holds beyond its live steps, its dead ends, no history shows. -/
theorem same_histories_iff {P Q : Process S A} :
    (∀ g m, Admits P g m ↔ Admits Q g m) ↔ ∀ s a t, (live P).step s a t ↔ (live Q).step s a t :=
  ⟨fun same _ _ _ =>
    ⟨fun ⟨g, m, n, admits, rest⟩ => ⟨g, m, n, (same g m).mp admits, rest⟩,
     fun ⟨g, m, n, admits, rest⟩ => ⟨g, m, n, (same g m).mpr admits, rest⟩⟩,
   fun same _ _ =>
    ⟨fun admits => admits_live_iff.mp fun n => (same _ _ _).mp (ShownBy.admits admits n),
     fun admits => admits_live_iff.mp fun n => (same _ _ _).mpr (ShownBy.admits admits n)⟩⟩

/-- **The live steps of the live law are its steps:** it has no dead end. -/
theorem live_live {P : Process S A} {s : S} {a : A} {t : S} :
    (live (live P)).step s a t ↔ (live P).step s a t :=
  ⟨live_le (live P) s a t,
   fun ⟨g, m, n, admits, rest⟩ => ⟨g, m, n, admits_live_iff.mpr admits, rest⟩⟩

/-- **The dead end's step is not live:** no history shows it. -/
theorem DeadEnd.not_live {s : Bool} {i : Unit} {t : Bool} : ¬ (live DeadEnd.law).step s i t :=
  fun ⟨g, m, _, admits, _⟩ => DeadEnd.no_history.2 ⟨g, m, admits⟩

end Live

/-! ## Histories that stop -/

section Finite

variable {S : Type u} {A : Type v}

/-- Laws with the same steps have the same finite histories. -/
theorem Trace.of_same {P Q : Process S A} (same : ∀ s a t, P.step s a t → Q.step s a t) :
    ∀ {s : S} {as : List A} {t : S}, Trace P s as t → Trace Q s as t
  | _, _, _, .nil s => .nil s
  | _, _, _, .cons step path => .cons (same _ _ _ step) (Trace.of_same same path)

/-- **With histories that stop, a law is fixed by its histories:** two laws have the same finite
histories exactly where they have the same steps. No dead end remains. -/
theorem same_finite_histories_iff {P Q : Process S A} :
    (∀ s as t, Trace P s as t ↔ Trace Q s as t) ↔ ∀ s a t, P.step s a t ↔ Q.step s a t :=
  ⟨fun same s a t =>
    ⟨fun step => trace_singleton_iff.mp ((same s [a] t).mp (trace_singleton_iff.mpr step)),
     fun step => trace_singleton_iff.mp ((same s [a] t).mpr (trace_singleton_iff.mpr step))⟩,
   fun same _ _ _ =>
    ⟨Trace.of_same fun s a t => (same s a t).mp, Trace.of_same fun s a t => (same s a t).mpr⟩⟩

/-- A family of finite histories, each from a configuration by a course of moves to a
configuration, is made of its steps where the empty course goes nowhere and a course is a first
step followed by the rest. -/
def MadeOfSteps (T : S → List A → S → Prop) : Prop :=
  (∀ s t, T s [] t ↔ s = t) ∧ ∀ s a as u, T s (a :: as) u ↔ ∃ m, T s [a] m ∧ T m as u

/-- **A family of finite histories is a law's exactly where it is made of its steps**; the law is
its one-step part. Splicing is built in: the rest of a course depends only on where it is. -/
theorem finite_family_iff {T : S → List A → S → Prop} :
    (∃ P : Process S A, ∀ s as t, T s as t ↔ Trace P s as t) ↔ MadeOfSteps T :=
  ⟨fun ⟨P, same⟩ =>
    ⟨fun s t => (same s [] t).trans trace_nil_iff,
     fun s a as u => (same s (a :: as) u).trans (trace_cons_iff.trans
      ⟨fun ⟨m, step, path⟩ => ⟨m, (same s [a] m).mpr (trace_singleton_iff.mpr step),
                               (same m as u).mpr path⟩,
       fun ⟨m, first, rest⟩ => ⟨m, trace_singleton_iff.mp ((same s [a] m).mp first),
                               (same m as u).mp rest⟩⟩)⟩,
   fun ⟨nil, cons⟩ => ⟨⟨fun s a t => T s [a] t⟩, fun s as t => by
    induction as generalizing s with
    | nil => exact (nil s t).trans trace_nil_iff.symm
    | cons a as ih =>
      exact (cons s a as t).trans
        ⟨fun ⟨m, first, rest⟩ => .cons first ((ih m).mp rest),
         fun path => match trace_cons_iff.mp path with
          | ⟨m, first, rest⟩ => ⟨m, first, (ih m).mpr rest⟩⟩⟩⟩

end Finite

/-! ## What tests fix -/

section Tests

variable {S : Type u} {S' : Type u'} {A : Type v} {C : Type w}
variable {F : Frame S A C} {G : Frame S' A C}

/-- Two configurations pass the same tests: the same courses of moves are open from each, and
after each course the same claims can be realized. -/
def SameTests (F : Frame S A C) (G : Frame S' A C) (s : S) (s' : S') : Prop :=
  (∀ as, (∃ t, Trace F.P s as t) ↔ ∃ t', Trace G.P s' as t') ∧
    ∀ as c, (∃ t, Trace F.P s as t ∧ F.realized t c) ↔ ∃ t', Trace G.P s' as t' ∧ G.realized t' c

/-- Alike configurations pass the same tests. -/
theorem Alike.sameTests {s : S} {s' : S'} (alike : Alike F G s s') : SameTests F G s s' :=
  ⟨fun _ =>
    ⟨fun ⟨_, path⟩ => match alike.trace path with
      | ⟨t', path', _⟩ => ⟨t', path'⟩,
     fun ⟨_, path'⟩ => match alike.symm.trace path' with
      | ⟨t, path, _⟩ => ⟨t, path⟩⟩,
   alike.tests⟩

/-- Passing the same tests survives one move into outcomes each side determines up to
likeness. -/
theorem SameTests.after {s : S} {s' : S'} (same : SameTests F G s s') (determined : DeterminedAt F s)
    (determined' : DeterminedAt G s') {a : A} {t : S} {t' : S'} (step : F.P.step s a t)
    (step' : G.P.step s' a t') : SameTests F G t t' :=
  ⟨fun as =>
    ⟨fun ⟨_, path⟩ => match (same.1 (a :: as)).mp ⟨_, .cons step path⟩ with
      | ⟨_, path'⟩ => match trace_cons_iff.mp path' with
        | ⟨_, step'', rest⟩ => match (determined' a _ t' step'' step').trace rest with
          | ⟨u', path'', _⟩ => ⟨u', path''⟩,
     fun ⟨_, path'⟩ => match (same.1 (a :: as)).mpr ⟨_, .cons step' path'⟩ with
      | ⟨_, path⟩ => match trace_cons_iff.mp path with
        | ⟨_, step'', rest⟩ => match (determined a _ t step'' step).trace rest with
          | ⟨u, path'', _⟩ => ⟨u, path''⟩⟩,
   fun as c =>
    ⟨fun ⟨_, path, real⟩ =>
      match (same.2 (a :: as) c).mp ⟨_, .cons step path, real⟩ with
      | ⟨_, path', real'⟩ => match trace_cons_iff.mp path' with
        | ⟨_, step'', rest⟩ => match (determined' a _ t' step'' step').trace rest with
          | ⟨u', path'', joined⟩ => ⟨u', path'', (joined.realized c).mp real'⟩,
     fun ⟨_, path', real'⟩ =>
      match (same.2 (a :: as) c).mpr ⟨_, .cons step' path', real'⟩ with
      | ⟨_, path, real⟩ => match trace_cons_iff.mp path with
        | ⟨_, step'', rest⟩ => match (determined a _ t step'' step).trace rest with
          | ⟨u, path'', joined⟩ => ⟨u, path'', (joined.realized c).mp real⟩⟩⟩

/-- Where both frames are determined up to likeness, passing the same tests is a
bisimulation. -/
theorem sameTests_bisimulation (determined : ∀ s, DeterminedAt F s)
    (determined' : ∀ s', DeterminedAt G s') : Bisimulation F G (SameTests F G) :=
  fun s s' same =>
    ⟨fun c =>
      ⟨fun real => match (same.2 [] c).mp ⟨s, .nil s, real⟩ with
        | ⟨_, path', real'⟩ => (trace_nil_iff.mp path') ▸ real',
       fun real' => match (same.2 [] c).mpr ⟨s', .nil s', real'⟩ with
        | ⟨_, path, real⟩ => (trace_nil_iff.mp path) ▸ real⟩,
     fun a t step => match (same.1 [a]).mp ⟨t, .cons step (.nil t)⟩ with
      | ⟨_, path'⟩ => match trace_cons_iff.mp path' with
        | ⟨t', step', _⟩ => ⟨t', step', same.after (determined s) (determined' s') step step'⟩,
     fun a t' step' => match (same.1 [a]).mpr ⟨t', .cons step' (.nil t')⟩ with
      | ⟨_, path⟩ => match trace_cons_iff.mp path with
        | ⟨t, step, _⟩ => ⟨t, step, same.after (determined s) (determined' s') step step'⟩⟩

/-- **Where both frames are determined up to likeness, configurations are alike exactly where
they pass the same tests.** -/
theorem alike_iff_sameTests (determined : ∀ s, DeterminedAt F s)
    (determined' : ∀ s', DeterminedAt G s') {s : S} {s' : S'} :
    Alike F G s s' ↔ SameTests F G s s' :=
  ⟨Alike.sameTests, fun same => ⟨_, sameTests_bisimulation determined determined', same⟩⟩

/-- **For one determined frame, configurations are alike exactly where they pass the same
tests.** -/
theorem Determined.alike_iff_sameTests (determined : Determined F.P) {s s' : S} :
    Alike F F s s' ↔ SameTests F F s s' :=
  _root_.Becoming.alike_iff_sameTests (Determined.at determined) (Determined.at determined)

end Tests

/-! ## Where tests do not fix likeness -/

namespace Choosing

/-- Three moves. -/
inductive Move where
  | a
  | b
  | c

/-- Five configurations. -/
inductive Pos where
  | p0
  | p1
  | p2
  | p3
  | p4

/-- One move, then a choice of two. -/
inductive Late : Pos → Move → Pos → Prop where
  | first : Late .p0 .a .p1
  | left : Late .p1 .b .p2
  | right : Late .p1 .c .p3

/-- A choice made at the first move. -/
inductive Early : Pos → Move → Pos → Prop where
  | toLeft : Early .p0 .a .p1
  | toRight : Early .p0 .a .p2
  | left : Early .p1 .b .p3
  | right : Early .p2 .c .p4

/-- The frame that chooses after its first move, with no claims. -/
def late : Frame Pos Move Empty :=
  ⟨⟨Late⟩, fun _ c => nomatch c⟩

/-- The frame that chooses at its first move, with no claims. -/
def early : Frame Pos Move Empty :=
  ⟨⟨Early⟩, fun _ c => nomatch c⟩

/-- The courses open from the start: none, `a`, `a b` and `a c`. -/
inductive Open : List Move → Prop where
  | none : Open []
  | first : Open [.a]
  | left : Open [.a, .b]
  | right : Open [.a, .c]

theorem late_open {as : List Move} {t : Pos} (path : Trace late.P .p0 as t) : Open as :=
  match as, path with
  | [], _ => .none
  | _ :: rest, .cons .first path' => match rest, path' with
    | [], _ => .first
    | _ :: rest', .cons .left path'' => match rest', path'' with
      | [], _ => .left
      | _ :: _, .cons step _ => nomatch step
    | _ :: rest', .cons .right path'' => match rest', path'' with
      | [], _ => .right
      | _ :: _, .cons step _ => nomatch step

theorem early_open {as : List Move} {t : Pos} (path : Trace early.P .p0 as t) : Open as :=
  match as, path with
  | [], _ => .none
  | _ :: rest, .cons .toLeft path' => match rest, path' with
    | [], _ => .first
    | _ :: rest', .cons .left path'' => match rest', path'' with
      | [], _ => .left
      | _ :: _, .cons step _ => nomatch step
  | _ :: rest, .cons .toRight path' => match rest, path' with
    | [], _ => .first
    | _ :: rest', .cons .right path'' => match rest', path'' with
      | [], _ => .right
      | _ :: _, .cons step _ => nomatch step

theorem late_of_open : ∀ {as : List Move}, Open as → ∃ t, Trace late.P .p0 as t
  | _, .none => ⟨_, .nil _⟩
  | _, .first => ⟨_, .cons .first (.nil _)⟩
  | _, .left => ⟨_, .cons .first (.cons .left (.nil _))⟩
  | _, .right => ⟨_, .cons .first (.cons .right (.nil _))⟩

theorem early_of_open : ∀ {as : List Move}, Open as → ∃ t, Trace early.P .p0 as t
  | _, .none => ⟨_, .nil _⟩
  | _, .first => ⟨_, .cons .toLeft (.nil _)⟩
  | _, .left => ⟨_, .cons .toLeft (.cons .left (.nil _))⟩
  | _, .right => ⟨_, .cons .toRight (.cons .right (.nil _))⟩

/-- **The two starts pass the same tests.** -/
theorem sameTests : SameTests late early .p0 .p0 :=
  ⟨fun _ => ⟨fun ⟨_, path⟩ => early_of_open (late_open path),
             fun ⟨_, path⟩ => late_of_open (early_open path)⟩,
   fun _ c => nomatch c⟩

/-- **The two starts are not alike:** where branching is not determined, the tests do not fix
likeness. -/
theorem not_alike : ¬ Alike late early .p0 .p0 :=
  fun alike => match alike.step (a := .a) (t := .p1) .first with
    | ⟨_, .toLeft, joined⟩ => match joined.step (a := .c) (t := .p3) .right with
      | ⟨_, step, _⟩ => nomatch step
    | ⟨_, .toRight, joined⟩ => match joined.step (a := .b) (t := .p2) .left with
      | ⟨_, step, _⟩ => nomatch step

/-- The frame that chooses at its first move is not determined. -/
theorem early_not_determined : ¬ Determined early.P :=
  fun determined => nomatch determined .p0 .a .p1 .p2 .toLeft .toRight

end Choosing

end Becoming
