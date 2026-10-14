import Becoming.Histories

/-!
# Every choice postponed until it shows (scratch prototype, not for landing)

A frame's choices postponed: a configuration is a family of configurations, those a course of
moves may have reached; a move goes from a family to the family of all its members' outcomes by
that move, where some member can take it; a family realizes a claim where some member does. So
no choice is made until what it leads to shows in a move that can be taken or a claim realized.

* **Linear tests are likeness with every choice postponed** (`sameTests_iff_postponed_alike`).
* **A frame is alike to its postponement exactly where its choices make no difference up to
  likeness** (`alike_postponed_iff_determined`).

So what linear tests do not see is exactly when choices are made.
-/

namespace Becoming

open Generative

universe u u' v w

section Postponement

variable {S : Type u} {S' : Type u'} {A : Type v} {C : Type w}

/-- **The frame with every choice postponed until it shows.** -/
def Frame.postponed (F : Frame S A C) : Frame (S → Prop) A C :=
  ⟨⟨fun X a Y => (∃ s t, X s ∧ F.P.step s a t) ∧ ∀ t, Y t ↔ ∃ s, X s ∧ F.P.step s a t⟩,
   fun X c => ∃ s, X s ∧ F.realized s c⟩

/-- Families with the same members are alike in the postponed frame. -/
theorem Frame.postponed_members (F : Frame S A C) :
    Bisimulation F.postponed F.postponed fun X X' => ∀ s, X s ↔ X' s :=
  fun X X' same =>
    ⟨fun _ => ⟨fun ⟨s, mem, real⟩ => ⟨s, (same s).mp mem, real⟩,
               fun ⟨s, mem, real⟩ => ⟨s, (same s).mpr mem, real⟩⟩,
     fun a _ ⟨⟨s, t, mem, step⟩, image⟩ =>
       ⟨fun t => ∃ s, X' s ∧ F.P.step s a t, ⟨⟨s, t, (same s).mp mem, step⟩, fun _ => Iff.rfl⟩,
        fun t => (image t).trans
          ⟨fun ⟨s, mem, step⟩ => ⟨s, (same s).mp mem, step⟩,
           fun ⟨s, mem, step⟩ => ⟨s, (same s).mpr mem, step⟩⟩⟩,
     fun a _ ⟨⟨s, t, mem, step⟩, image⟩ =>
       ⟨fun t => ∃ s, X s ∧ F.P.step s a t, ⟨⟨s, t, (same s).mpr mem, step⟩, fun _ => Iff.rfl⟩,
        fun t => ⟨fun ⟨s, mem, step⟩ => (image t).mpr ⟨s, (same s).mp mem, step⟩,
                  fun mem' => match (image t).mp mem' with
                    | ⟨s, mem, step⟩ => ⟨s, (same s).mpr mem, step⟩⟩⟩⟩

/-- **The postponed frame makes no choice**: it is determined up to likeness everywhere. -/
theorem Frame.postponed_determinedAt (F : Frame S A C) (X : S → Prop) :
    DeterminedAt F.postponed X :=
  fun _ _ _ ⟨_, image⟩ ⟨_, image'⟩ =>
    ⟨_, F.postponed_members, fun t => (image t).trans (image' t).symm⟩

/-- A course of the postponed frame reaches the family of everything the course reaches from
its start's members. -/
theorem Frame.postponed_trace_members (F : Frame S A C) {X Y : S → Prop} {as : List A}
    (path : Trace F.postponed.P X as Y) : ∀ t, Y t ↔ ∃ s, X s ∧ Trace F.P s as t := by
  induction path with
  | nil X =>
    exact fun t => ⟨fun mem => ⟨t, mem, .nil t⟩,
                    fun ⟨s, mem, path⟩ => (trace_nil_iff.mp path) ▸ mem⟩
  | @cons X M Y a as step _ ih =>
    exact fun t => (ih t).trans
      ⟨fun ⟨m, mem, rest⟩ => match (step.2 m).mp mem with
        | ⟨s, mem', first⟩ => ⟨s, mem', .cons first rest⟩,
       fun ⟨s, mem, path⟩ => match trace_cons_iff.mp path with
        | ⟨m, first, rest⟩ => ⟨m, (step.2 m).mpr ⟨s, mem, first⟩, rest⟩⟩

/-- A course of the postponed frame from a family with a member reaches a family with one. -/
theorem Frame.postponed_trace_inhabited (F : Frame S A C) {X Y : S → Prop} {as : List A}
    (path : Trace F.postponed.P X as Y) : (∃ s, X s) → ∃ t, Y t := by
  induction path with
  | nil X => exact fun inhabited => inhabited
  | @cons X M Y a as step _ ih =>
    exact fun _ => match step.1 with
      | ⟨s, t, mem, first⟩ => ih ⟨t, (step.2 t).mpr ⟨s, mem, first⟩⟩

/-- Where some member can take a course, the postponed frame takes it. -/
theorem Frame.postponed_trace_of (F : Frame S A C) :
    ∀ {X : S → Prop} {as : List A}, (∃ s t, X s ∧ Trace F.P s as t) →
      ∃ Y, Trace F.postponed.P X as Y
  | X, [], _ => ⟨X, .nil X⟩
  | X, a :: _, ⟨s, t, mem, path⟩ => match trace_cons_iff.mp path with
    | ⟨m, first, rest⟩ =>
      match F.postponed_trace_of (X := fun m => ∃ s, X s ∧ F.P.step s a m)
          ⟨m, t, ⟨s, mem, first⟩, rest⟩ with
      | ⟨Y, path'⟩ => ⟨Y, .cons ⟨⟨s, m, mem, first⟩, fun _ => Iff.rfl⟩ path'⟩

/-- The postponed frame takes a course from a family with a member exactly where some member
takes it. -/
theorem Frame.postponed_trace_iff (F : Frame S A C) {X : S → Prop} (inhabited : ∃ s, X s)
    (as : List A) : (∃ Y, Trace F.postponed.P X as Y) ↔ ∃ s t, X s ∧ Trace F.P s as t :=
  ⟨fun ⟨_, path⟩ => match F.postponed_trace_inhabited path inhabited with
    | ⟨t, mem⟩ => match (F.postponed_trace_members path t).mp mem with
      | ⟨s, mem', path'⟩ => ⟨s, t, mem', path'⟩,
   F.postponed_trace_of⟩

/-- The postponed frame realizes a claim after a course exactly where some member, after that
course, does. -/
theorem Frame.postponed_tests_iff (F : Frame S A C) (X : S → Prop) (as : List A) (c : C) :
    (∃ Y, Trace F.postponed.P X as Y ∧ F.postponed.realized Y c) ↔
      ∃ s t, X s ∧ Trace F.P s as t ∧ F.realized t c :=
  ⟨fun ⟨_, path, t, mem, real⟩ => match (F.postponed_trace_members path t).mp mem with
    | ⟨s, mem', path'⟩ => ⟨s, t, mem', path', real⟩,
   fun ⟨s, t, mem, path, real⟩ => match F.postponed_trace_of ⟨s, t, mem, path⟩ with
    | ⟨Y, path'⟩ => ⟨Y, path', t, (F.postponed_trace_members path' t).mpr ⟨s, mem, path⟩, real⟩⟩

/-- From one configuration, the postponed frame takes the courses the frame takes. -/
theorem Frame.postponed_trace_one (F : Frame S A C) (s : S) (as : List A) :
    (∃ Y, Trace F.postponed.P (Eq s) as Y) ↔ ∃ t, Trace F.P s as t :=
  (F.postponed_trace_iff ⟨s, rfl⟩ as).trans
    ⟨fun ⟨_, t, same, path⟩ => ⟨t, same ▸ path⟩, fun ⟨t, path⟩ => ⟨s, t, rfl, path⟩⟩

/-- From one configuration, the postponed frame realizes after a course the claims the frame
can realize after it. -/
theorem Frame.postponed_tests_one (F : Frame S A C) (s : S) (as : List A) (c : C) :
    (∃ Y, Trace F.postponed.P (Eq s) as Y ∧ F.postponed.realized Y c) ↔
      ∃ t, Trace F.P s as t ∧ F.realized t c :=
  (F.postponed_tests_iff (Eq s) as c).trans
    ⟨fun ⟨_, t, same, path, real⟩ => ⟨t, same ▸ path, real⟩,
     fun ⟨t, path, real⟩ => ⟨s, t, rfl, path, real⟩⟩

/-- **A configuration passes the tests its postponement passes.** -/
theorem sameTests_postponed (F : Frame S A C) (s : S) : SameTests F F.postponed s (Eq s) :=
  ⟨fun as => (F.postponed_trace_one s as).symm,
   fun as c => (F.postponed_tests_one s as c).symm⟩

/-- Passing the same tests is the same with every choice postponed. -/
theorem sameTests_postponed_iff {F : Frame S A C} {G : Frame S' A C} {s : S} {s' : S'} :
    SameTests F.postponed G.postponed (Eq s) (Eq s') ↔ SameTests F G s s' :=
  ⟨fun ⟨courses, claims⟩ =>
    ⟨fun as => (F.postponed_trace_one s as).symm.trans
        ((courses as).trans (G.postponed_trace_one s' as)),
     fun as c => (F.postponed_tests_one s as c).symm.trans
        ((claims as c).trans (G.postponed_tests_one s' as c))⟩,
   fun ⟨courses, claims⟩ =>
    ⟨fun as => (F.postponed_trace_one s as).trans
        ((courses as).trans (G.postponed_trace_one s' as).symm),
     fun as c => (F.postponed_tests_one s as c).trans
        ((claims as c).trans (G.postponed_tests_one s' as c).symm)⟩⟩

/-- **Linear tests are likeness with every choice postponed**: two configurations pass the same
tests exactly where, with every choice postponed until it shows, they are alike. -/
theorem sameTests_iff_postponed_alike {F : Frame S A C} {G : Frame S' A C} {s : S} {s' : S'} :
    SameTests F G s s' ↔ Alike F.postponed G.postponed (Eq s) (Eq s') :=
  sameTests_postponed_iff.symm.trans
    (alike_iff_sameTests F.postponed_determinedAt G.postponed_determinedAt).symm

/-- A configuration alike to its postponement makes no choice that makes a difference up to
likeness. -/
theorem DeterminedAt.of_alike_postponed {F : Frame S A C} {s : S}
    (alike : Alike F F.postponed s (Eq s)) : DeterminedAt F s :=
  fun _ _ _ step step' => match alike.step step, alike.step step' with
  | ⟨_, ⟨_, image⟩, joined⟩, ⟨_, ⟨_, image'⟩, joined'⟩ =>
    Alike.trans joined (Alike.trans ⟨_, F.postponed_members, fun t => (image t).trans (image' t).symm⟩
      joined'.symm)

/-- **A frame is alike to its postponement exactly where its choices make no difference up to
likeness.** -/
theorem alike_postponed_iff_determined {F : Frame S A C} :
    (∀ s, Alike F F.postponed s (Eq s)) ↔ ∀ s, DeterminedAt F s :=
  ⟨fun alike s => DeterminedAt.of_alike_postponed (alike s),
   fun determined s => (alike_iff_sameTests determined F.postponed_determinedAt).mpr
     (sameTests_postponed F s)⟩

end Postponement

end Becoming
