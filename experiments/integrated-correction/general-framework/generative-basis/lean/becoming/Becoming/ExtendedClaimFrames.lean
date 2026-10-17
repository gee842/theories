import Becoming.Frame
import ConcernExtension

/-!
# Frames whose claims gain a newly distinguished kind

`ConcernExtension` compares histories by contents of fixed meaning on an old domain extended by
newly distinguished contents (`extend old fresh`, on `Sum I J`), under inclusion and under the
protection-first comparison `PracticalJudgment.Better`. This module reads the extension off the
base: a frame whose claims are of two kinds, the old ones `I` and the newly distinguished ones
`J`, realizes at each configuration exactly the extended contents of its two parts
(`extend_iff`). Inclusion and the comparison of extended contents are then those of what the
frame realizes (`included_iff`, `better_gain_iff`, `better_basic_iff`).

* **Crossed growth leaves configurations incomparable.** Where the old claims realized strictly
  grow from `a` to `b` and the newly distinguished ones strictly shrink, neither configuration
  realizes every claim of the other (`crossed_incomparable`).
* **A frame of gains.** With protected contents equal at `a` and `b`:
  where `a` strictly exceeds `b` in old gains, `a` is better by all the gains the frame realizes
  exactly when it keeps every newly distinguished gain of `b` (`gain_transfer_iff`); where the
  old gains are equal and `a` strictly exceeds `b` in the newly distinguished ones, the old gains
  rank neither, while all the gains rank `a` above `b` (`fresh_gains_decide`).
* **A frame of basic conditions.** With the old basic conditions equal and `a` strictly ahead in
  gains, `a` is better on the old conditions, while a newly distinguished basic condition that
  `b` strictly keeps more of reverses the comparison, whatever further gains are distinguished
  (`fresh_basic_reverses`).

No ethical predicate or axiom occurs; the protection-first comparison is the source's supplied
J1/J2 relation, not derived here.
-/

namespace Becoming

open PracticalJudgment

universe u v

namespace ExtendedClaimFrames

variable {S : Type} {A : Type u} {I J : Type}

/-- The old claims a frame realizes at a configuration. -/
def old (F : Frame S A (Sum I J)) (s : S) (i : I) : Prop := F.realized s (.inl i)

/-- The newly distinguished claims a frame realizes at a configuration. -/
def fresh (F : Frame S A (Sum I J)) (s : S) (j : J) : Prop := F.realized s (.inr j)

/-- **A frame realizes exactly the extended contents of its two parts.** -/
theorem extend_iff (F : Frame S A (Sum I J)) (s : S) :
    ∀ x, ConcernExtension.extend (old F) (fresh F) s x ↔ F.realized s x
  | .inl _ => Iff.rfl
  | .inr _ => Iff.rfl

/-- Inclusion of extended contents is inclusion of what the frame realizes. -/
theorem included_iff (F : Frame S A (Sum I J)) (a b : S) :
    Included (ConcernExtension.extend (old F) (fresh F) a)
        (ConcernExtension.extend (old F) (fresh F) b) ↔
      Included (F.realized a) (F.realized b) :=
  ⟨fun included x => match x with
    | .inl i => included (.inl i)
    | .inr j => included (.inr j),
   fun included x => match x with
    | .inl i => included (.inl i)
    | .inr j => included (.inr j)⟩

theorem strictIncluded_iff (F : Frame S A (Sum I J)) (a b : S) :
    StrictIncluded (ConcernExtension.extend (old F) (fresh F) a)
        (ConcernExtension.extend (old F) (fresh F) b) ↔
      StrictIncluded (F.realized a) (F.realized b) :=
  ⟨fun ⟨forth, notBack⟩ =>
    ⟨(included_iff F a b).mp forth, fun back => notBack ((included_iff F b a).mpr back)⟩,
   fun ⟨forth, notBack⟩ =>
    ⟨(included_iff F a b).mpr forth, fun back => notBack ((included_iff F b a).mp back)⟩⟩

/-- Comparison by protected contents and the extended gains is comparison by the gains a frame
of gains realizes. -/
theorem better_gain_iff {C : Type} (p : S → C → Prop) (F : Frame S A (Sum I J)) (a b : S) :
    Better p (ConcernExtension.extend (old F) (fresh F)) a b ↔ Better p F.realized a b :=
  ⟨fun better => match better with
    | .inl strict => .inl strict
    | .inr ⟨back, forth, strict⟩ => .inr ⟨back, forth, (strictIncluded_iff F b a).mp strict⟩,
   fun better => match better with
    | .inl strict => .inl strict
    | .inr ⟨back, forth, strict⟩ => .inr ⟨back, forth, (strictIncluded_iff F b a).mpr strict⟩⟩

/-- Comparison by the extended basic contents and gains is comparison by the basic conditions a
frame of basic conditions realizes. -/
theorem better_basic_iff {G : Type} (F : Frame S A (Sum I J)) (g : S → G → Prop) (a b : S) :
    Better (ConcernExtension.extend (old F) (fresh F)) g a b ↔ Better F.realized g a b :=
  ⟨fun better => match better with
    | .inl strict => .inl ((strictIncluded_iff F b a).mp strict)
    | .inr ⟨back, forth, strict⟩ =>
      .inr ⟨(included_iff F b a).mp back, (included_iff F a b).mp forth, strict⟩,
   fun better => match better with
    | .inl strict => .inl ((strictIncluded_iff F b a).mpr strict)
    | .inr ⟨back, forth, strict⟩ =>
      .inr ⟨(included_iff F b a).mpr back, (included_iff F a b).mpr forth, strict⟩⟩

/-- **Crossed growth leaves configurations incomparable.** Where the old claims a frame realizes
strictly grow from `a` to `b` and the newly distinguished ones strictly shrink, neither
configuration realizes every claim the other realizes. -/
theorem crossed_incomparable (F : Frame S A (Sum I J)) {a b : S}
    (older : StrictIncluded (old F a) (old F b)) (newer : StrictIncluded (fresh F b) (fresh F a)) :
    ¬ Included (F.realized a) (F.realized b) ∧ ¬ Included (F.realized b) (F.realized a) :=
  match ConcernExtension.crossed_extension_is_incomparable (old F) (fresh F) a b older newer with
  | ⟨notForth, notBack⟩ =>
    ⟨fun forth => notForth ((included_iff F a b).mpr forth),
     fun back => notBack ((included_iff F b a).mpr back)⟩

/-- **On a frame of gains, the comparison passes to the newly distinguished gains.** With the
protected contents equal at `a` and `b` and `a` strictly ahead in old gains, `a` is better by all
the gains the frame realizes exactly when it keeps every newly distinguished gain `b` realizes. -/
theorem gain_transfer_iff {C : Type} (p : S → C → Prop) (F : Frame S A (Sum I J)) {a b : S}
    (forth : Included (p a) (p b)) (back : Included (p b) (p a))
    (ahead : StrictIncluded (old F b) (old F a)) :
    Better p F.realized a b ↔ Included (fresh F b) (fresh F a) :=
  (better_gain_iff p F a b).symm.trans
    (ConcernExtension.gain_judgment_transfer_iff p (old F) (fresh F) a b forth back ahead)

/-- **On a frame of gains, newly distinguished gains decide what the old ones leave open.** With
the protected contents and the old gains equal at `a` and `b`, and `a` strictly ahead in newly
distinguished gains, the old gains rank neither configuration above the other, while all the
gains the frame realizes rank `a` above `b`. -/
theorem fresh_gains_decide {C : Type} (p : S → C → Prop) (F : Frame S A (Sum I J)) {a b : S}
    (pForth : Included (p a) (p b)) (pBack : Included (p b) (p a))
    (gForth : Included (old F a) (old F b)) (gBack : Included (old F b) (old F a))
    (ahead : StrictIncluded (fresh F b) (fresh F a)) :
    ¬ Better p (old F) a b ∧ ¬ Better p (old F) b a ∧ Better p F.realized a b :=
  match ConcernExtension.positive_extension_changes_judgment p (old F) (fresh F) a b pForth pBack
      gForth gBack ahead with
  | ⟨notAB, notBA, better⟩ => ⟨notAB, notBA, (better_gain_iff p F a b).mp better⟩

/-- **On a frame of basic conditions, a newly distinguished condition can reverse the
comparison.** With the old basic conditions equal at `a` and `b` and `a` strictly ahead in
gains, `a` is better on the old conditions; where `b` strictly keeps more of the newly
distinguished conditions, `b` is better on all the conditions the frame realizes, whatever
further gains are distinguished. -/
theorem fresh_basic_reverses {G R : Type} (F : Frame S A (Sum I J)) (g : S → G → Prop)
    (freshGain : S → R → Prop) {a b : S}
    (forth : Included (old F a) (old F b)) (back : Included (old F b) (old F a))
    (ahead : StrictIncluded (g b) (g a)) (kept : StrictIncluded (fresh F a) (fresh F b)) :
    Better (old F) g a b ∧ Better F.realized (ConcernExtension.extend g freshGain) b a :=
  match ConcernExtension.new_basic_condition_can_reverse (old F) g (fresh F) freshGain a b forth
      back ahead kept with
  | ⟨better, reversed⟩ => ⟨better, (better_basic_iff F (ConcernExtension.extend g freshGain) b a).mp reversed⟩

end ExtendedClaimFrames

end Becoming
