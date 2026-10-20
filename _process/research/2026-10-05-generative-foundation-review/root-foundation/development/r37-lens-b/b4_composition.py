#!/usr/bin/env python3
"""R37 B4, step 2 (after b4_likeness.py): the joint frame's likeness and tests are the case of a
family of one relation.

usage: python3 -B b4_composition.py

In Becoming.Composition, `JointTest`, `JointTest.Holds`, `SameJointTests`, `JointBisimulation` and
`JointAlike` become abbreviations of `TestWith Unit`, `TestWith.Holds`, `SameTestsWith`,
`BisimulationWith` and `AlikeWith` at the relation `joint`; `MatchesParts` and its laws moved to
Becoming.Likeness; the parallel laws (`SameJointTests.refl/symm/trans/functional/sameBranchingTests`,
`BranchingTest.toJoint`, `holds_toJoint`, `JointBisimulation.eq/converse/comp`,
`JointAlike.refl/symm/trans/alike/realized/step/parts/matchesParts/holds_iff/sameJointTests/
functional`) are removed for the general ones, which dot notation reaches through the
abbreviations. Each use whose arguments change (a part's relation index `()`, a joint test's
`.together ()`, the pair of matchings under `∀ i`) is an exact edit below, in Composition and
JointCorrespondence."""
from pathlib import Path

B = Path(__file__).resolve().parents[6] / 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming'
p = B / 'Composition.lean'
s = p.read_text()
start = s.index('/-! ## Joint frames and joint tests -/')
end = s.index('/-! ## The parts add distinctions -/')

HEAD = '''/-! ## Joint frames and joint tests -/

/-- A frame in which a configuration may hold two configurations together as its parts:
`joint s l r` says that `s` realizes `l` and `r` together. The parts are configurations of the
same unfolding; no associativity, order, unit or repetition of parts is assumed. -/
structure JointFrame (S : Type u) (A : Type v) (C : Type w) extends Frame S A C where
  joint : S → S → S → Prop

/-- A joint test: a test with parts (`TestWith` of `Becoming.Likeness`) for the one relation of a
joint frame. It is nothing, a claim, the failure of a test, two tests together, that some step by
a move leads to where a test holds, or that the configuration holds together two parts, the first
passing one test and the second the other (`.together () φ ψ`). -/
abbrev JointTest (A : Type v) (C : Type w) := TestWith Unit A C

section Tests

variable {S : Type u} {S' : Type u'} {A : Type v} {C : Type w}

/-- Where a joint test holds in a joint frame: `TestWith.Holds` at its relation `joint`. -/
abbrev JointTest.Holds (F : JointFrame S A C) : S → JointTest A C → Prop :=
  TestWith.Holds (I := Unit) F.toFrame fun _ => F.joint

/-- Two configurations pass the same joint tests: `SameTestsWith` at the relations `joint`. Its
laws are those of `SameTestsWith` (`refl`, `symm`, `trans`, `functional`,
`sameBranchingTests`). -/
abbrev SameJointTests (F : JointFrame S A C) (G : JointFrame S' A C) (s : S) (s' : S') : Prop :=
  SameTestsWith F.toFrame G.toFrame (fun _ : Unit => F.joint) (fun _ => G.joint) s s'

end Tests

/-! ## Likeness respecting the parts -/

section JointLikeness

variable {S : Type u} {S' : Type u'} {A : Type v} {C : Type w}

/-- A joint bisimulation: a bisimulation of the frames that matches, both ways, the parts each
whole holds together; `BisimulationWith` at the relations `joint`. -/
abbrev JointBisimulation (F : JointFrame S A C) (G : JointFrame S' A C) (B : S → S' → Prop) :
    Prop :=
  BisimulationWith F.toFrame G.toFrame (fun _ : Unit => F.joint) (fun _ => G.joint) B

/-- Two configurations are jointly alike where some joint bisimulation relates them: they relate
alike to every continuation and to every pair of parts; `AlikeWith` at the relations `joint`. Its
laws are those of `AlikeWith`: an equivalence (`refl`, `symm`, `trans`), likeness of the frames
with the parts forgotten and more (`alike`), the same claims, steps and parts (`realized`, `step`,
`parts`), the same joint tests (`holds_iff`, `sameTestsWith`) and `functional`. -/
abbrev JointAlike (F : JointFrame S A C) (G : JointFrame S' A C) (s : S) (s' : S') : Prop :=
  AlikeWith F.toFrame G.toFrame (fun _ : Unit => F.joint) (fun _ => G.joint) s s'

end JointLikeness

'''
s = s[:start] + HEAD + s[end:]

EDITS = [
    ('''    JointTest.Holds frame true (.together .top .top) ∧
      ¬ JointTest.Holds frame false (.together .top .top) :=''',
     '''    JointTest.Holds frame true (.together () .top .top) ∧
      ¬ JointTest.Holds frame false (.together () .top .top) :='''),
    ('(JointAlike.holds_iff (.together .top .top) alike)', '(AlikeWith.holds_iff (.together () .top .top) alike)'),
    ('match (same (.together (JointTest.firsts qs) (JointTest.seconds qs))).mp',
     'match (same (.together () (JointTest.firsts qs) (JointTest.seconds qs))).mp'),
    ('''   fun _ _ same _ _ joint => SameJointTests.parts joints' same joint (stable _) (stable _),
   fun _ _ same _ _ joint' =>
     match SameJointTests.parts joints same.symm joint' (stable' _) (stable' _) with
     | ⟨l, r, joint, left, right⟩ => ⟨l, r, joint, left.symm, right.symm⟩⟩''',
     '''   fun _ => ⟨fun _ _ same _ _ joint => SameJointTests.parts joints' same joint (stable _) (stable _),
   fun _ _ same _ _ joint' =>
     match SameJointTests.parts joints same.symm joint' (stable' _) (stable' _) with
     | ⟨l, r, joint, left, right⟩ => ⟨l, r, joint, left.symm, right.symm⟩⟩⟩'''),
    ('⟨JointAlike.sameJointTests, fun same =>', '⟨AlikeWith.sameTestsWith, fun same =>'),
    ('''  | .together _ _ =>
    ⟨fun ⟨_, _, (joint : Joint .plain _ _), _⟩''', '''  | .together _ _ _ =>
    ⟨fun ⟨_, _, (joint : Joint .plain _ _), _⟩'''),
    ('''  | .together φ _ =>
    ⟨fun ⟨l, r, joint, left, right⟩ => match l, r, joint, left, right with''',
     '''  | .together _ φ _ =>
    ⟨fun ⟨l, r, joint, left, right⟩ => match l, r, joint, left, right with'''),
    ('''(DoubleNegation.sameJointTests _)).parts
        DoubleNegation.Joint.plain with''', '''(DoubleNegation.sameJointTests _)).parts ()
        DoubleNegation.Joint.plain with'''),
    ('DoubleNegation.stable_of_parts joint alike.sameJointTests (not_not_decided p)',
     'DoubleNegation.stable_of_parts joint alike.sameTestsWith (not_not_decided p)'),
    ('(liftsFromEach_iff_of_kernel sense).mpr (JointAlike.matchesParts F)',
     '(liftsFromEach_iff_of_kernel sense).mpr (AlikeWith.matchesParts F.toFrame (fun _ => F.joint) ())'),
    ('(plans_lift_iff_of_kernel F sense).mpr (JointAlike.matchesParts F)',
     '(plans_lift_iff_of_kernel F sense).mpr (AlikeWith.matchesParts F.toFrame (fun _ => F.joint) ())'),
]
for old, new in EDITS:
    assert s.count(old) == 1, old
    s = s.replace(old, new)
p.write_text(s)

q = B / 'JointCorrespondence.lean'
t = q.read_text()
assert t.count('match bisim.2.1 _ t joined _ _ joint with') == 2
t = t.replace('match bisim.2.1 _ t joined _ _ joint with', 'match (bisim.2 ()).1 _ t joined _ _ joint with')
t = t.replace('SameJointTests.functional', 'SameTestsWith.functional')
q.write_text(t)
print('Composition and JointCorrespondence written')
