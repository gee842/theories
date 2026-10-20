#!/usr/bin/env python3
"""R37 B4, step 1: one bisimulation theory, with a family of relations among configurations as a
parameter, stated in Becoming.Likeness below both of its readings.

usage: python3 -B b4_likeness.py

Replaces the proof of `Alike.holds_iff` by the section `RelationsAmong`: `MatchesParts` and its two
laws (moved unchanged from Becoming.Composition), `BisimulationWith`, `AlikeWith` and their laws,
the tests with parts `TestWith`, `SameTestsWith` and their laws, the branching tests read as tests
with parts, and the frame with no relation as the case of an empty family (`alikeWith_empty_iff`).
`Alike.holds_iff` keeps its statement and is proved from `AlikeWith.holds_iff` at that case. Step 2
(b4_composition.py) makes the joint frame's likeness and tests the case of a family of one."""
from pathlib import Path

B = Path(__file__).resolve().parents[6] / 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming'
p = B / 'Likeness.lean'
s = p.read_text()
start = s.index('/-- Alike configurations agree on each branching test. -/\ntheorem Alike.holds_iff')
end = s.index('/-- **Alike configurations pass the same branching tests.** -/')

GENERAL = r'''/-! ### Likeness with relations among configurations

A frame may hold, beside its steps, a family of relations among its configurations, indexed by
`I`: `J i s l r` says that `s` holds `l` and `r` together under the `i`-th relation. Likeness, its
bisimulations and the tests are stated here once for any family. The frame with no relation (an
empty family) gives `Alike` and the branching tests (`alikeWith_empty_iff`,
`BranchingTest.holds_toWith`, and `Alike.holds_iff` below, proved from `AlikeWith.holds_iff`); the
joint frame of `Becoming.Composition` (a family of one) gives joint likeness and the joint tests. -/

section RelationsAmong

universe u'' x

variable {S'' : Type u''} {I : Type x}

/-- `B` matches the parts the wholes hold together: where `B` relates two configurations, each pair
of parts the first holds together under `J` is matched by a pair the second holds together under
`K`, related part by part. -/
def MatchesParts (J : S → S → S → Prop) (K : S' → S' → S' → Prop) (B : S → S' → Prop) : Prop :=
  ∀ s s', B s s' → ∀ l r, J s l r → ∃ l' r', K s' l' r' ∧ B l l' ∧ B r r'

/-- Matching parts passes to any relation holding exactly where the first does. -/
theorem MatchesParts.transport {J : S → S → S → Prop} {K : S' → S' → S' → Prop}
    {B B' : S → S' → Prop} (same : ∀ s s', B s s' ↔ B' s s') (matching : MatchesParts J K B) :
    MatchesParts J K B' :=
  fun s s' related l r joint =>
    match matching s s' ((same s s').mpr related) l r joint with
    | ⟨l', r', joint', left, right⟩ =>
      ⟨l', r', joint', (same l l').mp left, (same r r').mp right⟩

/-- Matching parts composes. -/
theorem MatchesParts.comp {J : S → S → S → Prop} {K : S' → S' → S' → Prop}
    {L : S'' → S'' → S'' → Prop} {B : S → S' → Prop} {B' : S' → S'' → Prop}
    (matching : MatchesParts J K B) (matching' : MatchesParts K L B') :
    MatchesParts J L fun s s'' => ∃ s', B s s' ∧ B' s' s'' :=
  fun s s'' ⟨s', related, related'⟩ l r joint =>
    match matching s s' related l r joint with
    | ⟨l', r', joint', left, right⟩ => match matching' s' s'' related' l' r' joint' with
      | ⟨l'', r'', joint'', left', right'⟩ =>
        ⟨l'', r'', joint'', ⟨l', left, left'⟩, ⟨r', right, right'⟩⟩

/-- A bisimulation with the relations: a bisimulation of the frames that matches, both ways and
relation by relation, the parts each whole holds together. -/
def BisimulationWith (F : Frame S A C) (G : Frame S' A C) (J : I → S → S → S → Prop)
    (K : I → S' → S' → S' → Prop) (B : S → S' → Prop) : Prop :=
  Bisimulation F G B ∧ ∀ i, MatchesParts (J i) (K i) B ∧ MatchesParts (K i) (J i) fun s' s => B s s'

/-- Sameness is a bisimulation with the relations. -/
theorem BisimulationWith.eq (F : Frame S A C) (J : I → S → S → S → Prop) :
    BisimulationWith F F J J fun s s' => s = s' :=
  ⟨Bisimulation.eq F, fun i =>
   ⟨fun _ _ same l r joint =>
     ⟨l, r, Eq.subst (motive := fun x => J i x l r) same joint, rfl, rfl⟩,
    fun _ _ same l r joint =>
     ⟨l, r, Eq.subst (motive := fun x => J i x l r) same.symm joint, rfl, rfl⟩⟩⟩

/-- The converse of a bisimulation with the relations is one. -/
theorem BisimulationWith.converse {F : Frame S A C} {G : Frame S' A C}
    {J : I → S → S → S → Prop} {K : I → S' → S' → S' → Prop} {B : S → S' → Prop}
    (bisim : BisimulationWith F G J K B) : BisimulationWith G F K J fun s' s => B s s' :=
  ⟨bisim.1.converse, fun i => ⟨(bisim.2 i).2, (bisim.2 i).1⟩⟩

/-- Bisimulations with the relations compose. -/
theorem BisimulationWith.comp {F : Frame S A C} {G : Frame S' A C} {H : Frame S'' A C}
    {J : I → S → S → S → Prop} {K : I → S' → S' → S' → Prop} {L : I → S'' → S'' → S'' → Prop}
    {B : S → S' → Prop} {B' : S' → S'' → Prop}
    (bisim : BisimulationWith F G J K B) (bisim' : BisimulationWith G H K L B') :
    BisimulationWith F H J L fun s s'' => ∃ s', B s s' ∧ B' s' s'' :=
  ⟨bisim.1.comp bisim'.1, fun i => ⟨(bisim.2 i).1.comp (bisim'.2 i).1,
   MatchesParts.transport
     (fun _ _ => ⟨fun ⟨s', related', related⟩ => ⟨s', related, related'⟩,
       fun ⟨s', related, related'⟩ => ⟨s', related', related⟩⟩)
     ((bisim'.2 i).2.comp (bisim.2 i).2)⟩⟩

/-- Two configurations are alike with the relations where some bisimulation with the relations
relates them: they relate alike to every continuation and to every pair of parts. -/
def AlikeWith (F : Frame S A C) (G : Frame S' A C) (J : I → S → S → S → Prop)
    (K : I → S' → S' → S' → Prop) (s : S) (s' : S') : Prop :=
  ∃ B, BisimulationWith F G J K B ∧ B s s'

/-- **Likeness with the relations is an equivalence:** every configuration is alike to itself, -/
theorem AlikeWith.refl (F : Frame S A C) (J : I → S → S → S → Prop) (s : S) :
    AlikeWith F F J J s s :=
  ⟨_, BisimulationWith.eq F J, rfl⟩

/-- it runs both ways, -/
theorem AlikeWith.symm {F : Frame S A C} {G : Frame S' A C} {J : I → S → S → S → Prop}
    {K : I → S' → S' → S' → Prop} {s : S} {s' : S'} : AlikeWith F G J K s s' → AlikeWith G F K J s' s
  | ⟨_, bisim, related⟩ => ⟨_, bisim.converse, related⟩

/-- and passes along. -/
theorem AlikeWith.trans {F : Frame S A C} {G : Frame S' A C} {H : Frame S'' A C}
    {J : I → S → S → S → Prop} {K : I → S' → S' → S' → Prop} {L : I → S'' → S'' → S'' → Prop}
    {s : S} {s' : S'} {s'' : S''} :
    AlikeWith F G J K s s' → AlikeWith G H K L s' s'' → AlikeWith F H J L s s''
  | ⟨_, bisim, related⟩, ⟨_, bisim', related'⟩ => ⟨_, bisim.comp bisim', s', related, related'⟩

/-- **Configurations alike with the relations are alike in the frames with the relations
forgotten.** -/
theorem AlikeWith.alike {F : Frame S A C} {G : Frame S' A C} {J : I → S → S → S → Prop}
    {K : I → S' → S' → S' → Prop} {s : S} {s' : S'} : AlikeWith F G J K s s' → Alike F G s s'
  | ⟨B, bisim, related⟩ => ⟨B, bisim.1, related⟩

/-- **With no relation, likeness with the relations is likeness.** -/
theorem alikeWith_empty_iff {F : Frame S A C} {G : Frame S' A C} {J : Empty → S → S → S → Prop}
    {K : Empty → S' → S' → S' → Prop} {s : S} {s' : S'} : AlikeWith F G J K s s' ↔ Alike F G s s' :=
  ⟨AlikeWith.alike, fun ⟨B, bisim, related⟩ => ⟨B, ⟨bisim, fun i => nomatch i⟩, related⟩⟩

/-- Configurations alike with the relations realize the same claims. -/
theorem AlikeWith.realized {F : Frame S A C} {G : Frame S' A C} {J : I → S → S → S → Prop}
    {K : I → S' → S' → S' → Prop} {s : S} {s' : S'} (alike : AlikeWith F G J K s s') (c : C) :
    F.realized s c ↔ G.realized s' c :=
  alike.alike.realized c

/-- A step of one is matched by a step of the other by the same move into configurations alike
with the relations. -/
theorem AlikeWith.step {F : Frame S A C} {G : Frame S' A C} {J : I → S → S → S → Prop}
    {K : I → S' → S' → S' → Prop} {s : S} {s' : S'} (alike : AlikeWith F G J K s s') {a : A} {t : S}
    (step : F.P.step s a t) : ∃ t', G.P.step s' a t' ∧ AlikeWith F G J K t t' :=
  match alike with
  | ⟨B, bisim, related⟩ => match (bisim.1 s s' related).2.1 a t step with
    | ⟨t', step', joined⟩ => ⟨t', step', B, bisim, joined⟩

/-- **A pair of parts one holds together under a relation is matched by a pair the other holds
together under it, alike part by part.** -/
theorem AlikeWith.parts {F : Frame S A C} {G : Frame S' A C} {J : I → S → S → S → Prop}
    {K : I → S' → S' → S' → Prop} {s : S} {s' : S'} (alike : AlikeWith F G J K s s') (i : I)
    {l r : S} (joint : J i s l r) :
    ∃ l' r', K i s' l' r' ∧ AlikeWith F G J K l l' ∧ AlikeWith F G J K r r' :=
  match alike with
  | ⟨B, bisim, related⟩ => match (bisim.2 i).1 s s' related l r joint with
    | ⟨l', r', joint', left, right⟩ => ⟨l', r', joint', ⟨B, bisim, left⟩, ⟨B, bisim, right⟩⟩

/-- Likeness with the relations in a frame matches the parts of each relation. -/
theorem AlikeWith.matchesParts (F : Frame S A C) (J : I → S → S → S → Prop) (i : I) :
    MatchesParts (J i) (J i) (AlikeWith F F J J) :=
  fun _ _ alike _ _ joint => alike.parts i joint

/-- **Where likeness with the relations tells apart the configurations of a frame, a configuration
is so alike to at most one of them.** -/
theorem AlikeWith.functional {F : Frame S A C} {G : Frame S' A C} {J : I → S → S → S → Prop}
    {K : I → S' → S' → S' → Prop} (separated : ∀ t t', AlikeWith G G K K t t' → t = t') {s : S}
    {t t' : S'} (alike : AlikeWith F G J K s t) (alike' : AlikeWith F G J K s t') : t = t' :=
  separated t t' (alike.symm.trans alike')

/-- A test with parts: nothing, a claim, the failure of a test, two tests together, that some step
by a move leads to where a test holds, or that the configuration holds together, under the `i`-th
relation, two parts, the first passing one test and the second the other. -/
inductive TestWith (I : Type x) (A : Type v) (C : Type w) where
  | top
  | claim (c : C)
  | not (φ : TestWith I A C)
  | both (φ ψ : TestWith I A C)
  | can (a : A) (φ : TestWith I A C)
  | together (i : I) (φ ψ : TestWith I A C)

/-- Where a test with parts holds in a frame with relations `J`. -/
def TestWith.Holds (F : Frame S A C) (J : I → S → S → S → Prop) : S → TestWith I A C → Prop
  | _, .top => True
  | s, .claim c => F.realized s c
  | s, .not φ => ¬ TestWith.Holds F J s φ
  | s, .both φ ψ => TestWith.Holds F J s φ ∧ TestWith.Holds F J s ψ
  | s, .can a φ => ∃ t, F.P.step s a t ∧ TestWith.Holds F J t φ
  | s, .together i φ ψ => ∃ l r, J i s l r ∧ TestWith.Holds F J l φ ∧ TestWith.Holds F J r ψ

/-- Two configurations pass the same tests with parts. -/
def SameTestsWith (F : Frame S A C) (G : Frame S' A C) (J : I → S → S → S → Prop)
    (K : I → S' → S' → S' → Prop) (s : S) (s' : S') : Prop :=
  ∀ φ, TestWith.Holds F J s φ ↔ TestWith.Holds G K s' φ

/-- Passing the same tests with parts is an equivalence: every configuration passes its own, -/
theorem SameTestsWith.refl (F : Frame S A C) (J : I → S → S → S → Prop) (s : S) :
    SameTestsWith F F J J s s :=
  fun _ => Iff.rfl

/-- both ways, -/
theorem SameTestsWith.symm {F : Frame S A C} {G : Frame S' A C} {J : I → S → S → S → Prop}
    {K : I → S' → S' → S' → Prop} {s : S} {s' : S'} (same : SameTestsWith F G J K s s') :
    SameTestsWith G F K J s' s :=
  fun φ => (same φ).symm

/-- and along. -/
theorem SameTestsWith.trans {F : Frame S A C} {G : Frame S' A C} {H : Frame S'' A C}
    {J : I → S → S → S → Prop} {K : I → S' → S' → S' → Prop} {L : I → S'' → S'' → S'' → Prop}
    {s : S} {s' : S'} {s'' : S''} (same : SameTestsWith F G J K s s')
    (same' : SameTestsWith G H K L s' s'') : SameTestsWith F H J L s s'' :=
  fun φ => (same φ).trans (same' φ)

/-- **Where the tests with parts tell apart the configurations of a frame, a configuration passes
the same tests as at most one of them.** -/
theorem SameTestsWith.functional {F : Frame S A C} {G : Frame S' A C} {J : I → S → S → S → Prop}
    {K : I → S' → S' → S' → Prop} (separated : ∀ t t', SameTestsWith G G K K t t' → t = t') {s : S}
    {t t' : S'} (same : SameTestsWith F G J K s t) (same' : SameTestsWith F G J K s t') : t = t' :=
  separated t t' (same.symm.trans same')

/-- Configurations alike with the relations agree on each test with parts. -/
theorem AlikeWith.holds_iff {F : Frame S A C} {G : Frame S' A C} {J : I → S → S → S → Prop}
    {K : I → S' → S' → S' → Prop} :
    ∀ (φ : TestWith I A C) {s : S} {s' : S'}, AlikeWith F G J K s s' →
      (TestWith.Holds F J s φ ↔ TestWith.Holds G K s' φ)
  | .top, _, _, _ => Iff.rfl
  | .claim c, _, _, alike => alike.realized c
  | .not φ, _, _, alike =>
    ⟨fun fails holds => fails ((AlikeWith.holds_iff φ alike).mpr holds),
     fun fails holds => fails ((AlikeWith.holds_iff φ alike).mp holds)⟩
  | .both φ ψ, _, _, alike =>
    ⟨fun ⟨holds, holds'⟩ =>
      ⟨(AlikeWith.holds_iff φ alike).mp holds, (AlikeWith.holds_iff ψ alike).mp holds'⟩,
     fun ⟨holds, holds'⟩ =>
      ⟨(AlikeWith.holds_iff φ alike).mpr holds, (AlikeWith.holds_iff ψ alike).mpr holds'⟩⟩
  | .can _ φ, _, _, alike =>
    ⟨fun ⟨_, step, holds⟩ => match alike.step step with
      | ⟨t', step', joined⟩ => ⟨t', step', (AlikeWith.holds_iff φ joined).mp holds⟩,
     fun ⟨_, step', holds⟩ => match alike.symm.step step' with
      | ⟨t, step, joined⟩ => ⟨t, step, (AlikeWith.holds_iff φ joined.symm).mpr holds⟩⟩
  | .together i φ ψ, _, _, alike =>
    ⟨fun ⟨_, _, joint, left, right⟩ => match alike.parts i joint with
      | ⟨l', r', joint', alikeL, alikeR⟩ =>
        ⟨l', r', joint', (AlikeWith.holds_iff φ alikeL).mp left,
          (AlikeWith.holds_iff ψ alikeR).mp right⟩,
     fun ⟨_, _, joint', left, right⟩ => match alike.symm.parts i joint' with
      | ⟨l, r, joint, alikeL, alikeR⟩ =>
        ⟨l, r, joint, (AlikeWith.holds_iff φ alikeL.symm).mpr left,
          (AlikeWith.holds_iff ψ alikeR.symm).mpr right⟩⟩

/-- **Configurations alike with the relations pass the same tests with parts.** -/
theorem AlikeWith.sameTestsWith {F : Frame S A C} {G : Frame S' A C} {J : I → S → S → S → Prop}
    {K : I → S' → S' → S' → Prop} {s : S} {s' : S'} (alike : AlikeWith F G J K s s') :
    SameTestsWith F G J K s s' :=
  fun φ => AlikeWith.holds_iff φ alike

/-- A branching test read as a test with parts that never asks for parts. -/
def BranchingTest.toWith : BranchingTest A C → TestWith I A C
  | .top => .top
  | .claim c => .claim c
  | .not φ => .not φ.toWith
  | .both φ ψ => .both φ.toWith ψ.toWith
  | .can a φ => .can a φ.toWith

/-- **A branching test holds in a frame exactly where its reading as a test with parts holds**,
whatever the relations. -/
theorem BranchingTest.holds_toWith {F : Frame S A C} {J : I → S → S → S → Prop} :
    ∀ (φ : BranchingTest A C) (s : S),
      BranchingTest.Holds F s φ ↔ TestWith.Holds F J s (φ.toWith (I := I))
  | .top, _ => Iff.rfl
  | .claim _, _ => Iff.rfl
  | .not φ, s => ⟨fun fails holds => fails ((BranchingTest.holds_toWith φ s).mpr holds),
      fun fails holds => fails ((BranchingTest.holds_toWith φ s).mp holds)⟩
  | .both φ ψ, s => ⟨fun ⟨first, second⟩ => ⟨(BranchingTest.holds_toWith φ s).mp first,
        (BranchingTest.holds_toWith ψ s).mp second⟩,
      fun ⟨first, second⟩ => ⟨(BranchingTest.holds_toWith φ s).mpr first,
        (BranchingTest.holds_toWith ψ s).mpr second⟩⟩
  | .can _ φ, _ => ⟨fun ⟨t, step, holds⟩ => ⟨t, step, (BranchingTest.holds_toWith φ t).mp holds⟩,
      fun ⟨t, step, holds⟩ => ⟨t, step, (BranchingTest.holds_toWith φ t).mpr holds⟩⟩

/-- **Configurations passing the same tests with parts pass the same branching tests.** -/
theorem SameTestsWith.sameBranchingTests {F : Frame S A C} {G : Frame S' A C}
    {J : I → S → S → S → Prop} {K : I → S' → S' → S' → Prop} {s : S} {s' : S'}
    (same : SameTestsWith F G J K s s') : SameBranchingTests F G s s' :=
  fun φ => (BranchingTest.holds_toWith φ s).trans
    ((same φ.toWith).trans (BranchingTest.holds_toWith φ s').symm)

end RelationsAmong

/-- Alike configurations agree on each branching test: the case of no relation of
`AlikeWith.holds_iff`. -/
theorem Alike.holds_iff {F : Frame S A C} {G : Frame S' A C} :
    ∀ (φ : BranchingTest A C) {s : S} {s' : S'}, Alike F G s s' →
      (BranchingTest.Holds F s φ ↔ BranchingTest.Holds G s' φ) :=
  fun φ {s} {s'} alike =>
    (BranchingTest.holds_toWith (J := fun i : Empty => nomatch i) φ s).trans
      ((AlikeWith.holds_iff φ.toWith (alikeWith_empty_iff.mpr alike)).trans
        (BranchingTest.holds_toWith (J := fun i : Empty => nomatch i) φ s').symm)

'''
p.write_text(s[:start] + GENERAL + s[end:])
print('Likeness: general section written')
