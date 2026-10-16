import ExplanatoryLocalUnits

/-! Tests are finite arrangements of the same joining activity. No separately
chosen success predicate is supplied. Realizable means possible under J, not
physically acquired, selected or actually executed by an observer. -/
namespace Generative.ExplanatoryJoiningContexts
open ExplanatoryLocalUnits
universe u
variable {F : Type u}

inductive Context (F : Type u) where
  | hole
  | left : F → Context F → Context F
  | right : Context F → F → Context F

def Realizes (J : Join F) : Context F → F → F → Prop
  | .hole, x, y => y = x
  | .left a c, x, y => ∃ m, Realizes J c x m ∧ J a m y
  | .right c a, x, y => ∃ m, Realizes J c x m ∧ J m a y

def Possible (J : Join F) (c : Context F) (x : F) : Prop := ∃ y, Realizes J c x y

def Same (J : Join F) (x y : F) : Prop := ∀ c, Possible J c x ↔ Possible J c y

def splice : Context F → Context F → Context F
  | .hole, inner => inner
  | .left a c, inner => .left a (splice c inner)
  | .right c a, inner => .right (splice c inner) a

theorem realizes_splice (J : Join F) (outer inner : Context F) (x z : F) :
    Realizes J (splice outer inner) x z ↔
      ∃ y, Realizes J inner x y ∧ Realizes J outer y z := by
  induction outer generalizing z with
  | hole => exact ⟨fun h => ⟨z, h, rfl⟩, fun ⟨y, h, eq⟩ => eq.symm ▸ h⟩
  | left a c ih =>
    constructor
    · rintro ⟨m, hm, hj⟩
      obtain ⟨y, hy, hm⟩ := (ih m).mp hm
      exact ⟨y, hy, m, hm, hj⟩
    · rintro ⟨y, hy, m, hm, hj⟩
      exact ⟨m, (ih m).mpr ⟨y, hy, hm⟩, hj⟩
  | right c a ih =>
    constructor
    · rintro ⟨m, hm, hj⟩
      obtain ⟨y, hy, hm⟩ := (ih m).mp hm
      exact ⟨y, hy, m, hm, hj⟩
    · rintro ⟨y, hy, m, hm, hj⟩
      exact ⟨m, (ih m).mpr ⟨y, hy, hm⟩, hj⟩

theorem possible_splice (J : Join F) (outer inner : Context F) (x : F) :
    Possible J (splice outer inner) x ↔ ∃ y, Realizes J inner x y ∧ Possible J outer y := by
  constructor
  · rintro ⟨z, hz⟩
    obtain ⟨y, hy, hz⟩ := (realizes_splice J outer inner x z).mp hz
    exact ⟨y, hy, z, hz⟩
  · rintro ⟨y, hy, z, hz⟩
    exact ⟨z, (realizes_splice J outer inner x z).mpr ⟨y, hy, hz⟩⟩

theorem realizes_functional {J : Join F} (hf : Functional J) (c : Context F)
    {x y z : F} (hy : Realizes J c x y) (hz : Realizes J c x z) : y = z := by
  induction c generalizing y z with
  | hole => exact hy.trans hz.symm
  | left a c ih =>
    obtain ⟨m, hm, hj⟩ := hy
    obtain ⟨n, hn, hk⟩ := hz
    have eq := ih hm hn
    subst n
    exact hf _ _ _ _ hj hk
  | right c a ih =>
    obtain ⟨m, hm, hj⟩ := hy
    obtain ⟨n, hn, hk⟩ := hz
    have eq := ih hm hn
    subst n
    exact hf _ _ _ _ hj hk

theorem continuation_after_realization {J : Join F} (hf : Functional J)
    {inner : Context F} {x y : F} (h : Realizes J inner x y) (outer : Context F) :
    Possible J (splice outer inner) x ↔ Possible J outer y := by
  rw [possible_splice]
  constructor
  · rintro ⟨z, hz, hp⟩
    exact (realizes_functional hf inner hz h) ▸ hp
  · intro hp
    exact ⟨y, h, hp⟩

theorem same_refl (J : Join F) (x : F) : Same J x x := fun _ => Iff.rfl

theorem same_symm {J : Join F} {x y : F} (h : Same J x y) : Same J y x :=
  fun c => (h c).symm

theorem same_trans {J : Join F} {x y z : F} (h : Same J x y) (k : Same J y z) :
    Same J x z := fun c => (h c).trans (k c)

theorem possible_right (J : Join F) (a b : F) :
    Possible J (.right .hole b) a ↔ Composable J a b := by
  constructor
  · rintro ⟨z, m, eq, hz⟩
    exact ⟨z, eq ▸ hz⟩
  · rintro ⟨z, hz⟩
    exact ⟨z, a, rfl, hz⟩

theorem possible_left (J : Join F) (a b : F) :
    Possible J (.left a .hole) b ↔ Composable J a b := by
  constructor
  · rintro ⟨z, m, eq, hz⟩
    exact ⟨z, eq ▸ hz⟩
  · rintro ⟨z, hz⟩
    exact ⟨z, b, rfl, hz⟩

theorem same_preserves_joinability {J : Join F} {a a' b b' : F}
    (ha : Same J a a') (hb : Same J b b') : Composable J a b ↔ Composable J a' b' :=
  (possible_right J a b).symm.trans ((ha (.right .hole b)).trans
    ((possible_right J a' b).trans ((possible_left J a' b).symm.trans
      ((hb (.left a' .hole)).trans (possible_left J a' b')))))

theorem same_continuation_results {J : Join F} (hf : Functional J) {a b x y : F}
    (h : Same J a b) (c : Context F) (hx : Realizes J c a x) (hy : Realizes J c b y) :
    Same J x y := by
  intro outer
  exact (continuation_after_realization hf hx outer).symm.trans
    ((h (splice outer c)).trans (continuation_after_realization hf hy outer))

theorem same_join_results {J : Join F} (hf : Functional J) {a a' b b' z z' : F}
    (ha : Same J a a') (hb : Same J b b') (hz : J a b z) (hz' : J a' b' z') :
    Same J z z' := by
  obtain ⟨m, hm⟩ := (same_preserves_joinability ha (same_refl J b)).mp ⟨z, hz⟩
  exact same_trans
    (same_continuation_results hf ha (.right .hole b) ⟨a, rfl, hz⟩ ⟨a', rfl, hm⟩)
    (same_continuation_results hf hb (.left a' .hole) ⟨b, rfl, hm⟩ ⟨b', rfl, hz'⟩)

/-- Compatibility with actual joining is enough to preserve every generated
context; the answer family is derived, not another independent input. -/
def Compatible (J : Join F) (R : F → F → Prop) : Prop :=
  ∀ {x y}, R x y → ∀ a,
    (∀ z, J a x z → ∃ w, J a y w ∧ R z w) ∧
    (∀ w, J a y w → ∃ z, J a x z ∧ R z w) ∧
    (∀ z, J x a z → ∃ w, J y a w ∧ R z w) ∧
    (∀ w, J y a w → ∃ z, J x a z ∧ R z w)

theorem compatible_transports_realization {J : Join F} {R : F → F → Prop}
    (hc : Compatible J R) (c : Context F) {x y : F} (h : R x y) :
    (∀ z, Realizes J c x z → ∃ w, Realizes J c y w ∧ R z w) ∧
    (∀ w, Realizes J c y w → ∃ z, Realizes J c x z ∧ R z w) := by
  induction c with
  | hole => exact ⟨fun z hz => ⟨y, rfl, hz.symm ▸ h⟩,
                   fun w hw => ⟨x, rfl, hw.symm ▸ h⟩⟩
  | left a c ih =>
    constructor
    · rintro z ⟨m, hm, hz⟩
      obtain ⟨n, hn, hmn⟩ := ih.1 m hm
      obtain ⟨w, hw, hzw⟩ := (hc hmn a).1 z hz
      exact ⟨w, ⟨n, hn, hw⟩, hzw⟩
    · rintro w ⟨n, hn, hw⟩
      obtain ⟨m, hm, hmn⟩ := ih.2 n hn
      obtain ⟨z, hz, hzw⟩ := (hc hmn a).2.1 w hw
      exact ⟨z, ⟨m, hm, hz⟩, hzw⟩
  | right c a ih =>
    constructor
    · rintro z ⟨m, hm, hz⟩
      obtain ⟨n, hn, hmn⟩ := ih.1 m hm
      obtain ⟨w, hw, hzw⟩ := (hc hmn a).2.2.1 z hz
      exact ⟨w, ⟨n, hn, hw⟩, hzw⟩
    · rintro w ⟨n, hn, hw⟩
      obtain ⟨m, hm, hmn⟩ := ih.2 n hn
      obtain ⟨z, hz, hzw⟩ := (hc hmn a).2.2.2 w hw
      exact ⟨z, ⟨m, hm, hz⟩, hzw⟩

theorem compatible_refines_same {J : Join F} {R : F → F → Prop}
    (hc : Compatible J R) {x y : F} (h : R x y) : Same J x y := by
  intro c
  have ht := compatible_transports_realization hc c h
  exact ⟨fun ⟨z, hz⟩ => let ⟨w, hw, _⟩ := ht.1 z hz; ⟨w, hw⟩,
         fun ⟨w, hw⟩ => let ⟨z, hz, _⟩ := ht.2 w hw; ⟨z, hz⟩⟩

theorem same_compatible {J : Join F} (hf : Functional J) : Compatible J (Same J) := by
  intro x y h a
  refine ⟨?_, ?_, ?_, ?_⟩
  · intro z hz
    obtain ⟨w, hw⟩ := (same_preserves_joinability (same_refl J a) h).mp ⟨z, hz⟩
    exact ⟨w, hw, same_join_results hf (same_refl J a) h hz hw⟩
  · intro w hw
    obtain ⟨z, hz⟩ := (same_preserves_joinability (same_refl J a) h).mpr ⟨w, hw⟩
    exact ⟨z, hz, same_join_results hf (same_refl J a) h hz hw⟩
  · intro z hz
    obtain ⟨w, hw⟩ := (same_preserves_joinability h (same_refl J a)).mp ⟨z, hz⟩
    exact ⟨w, hw, same_join_results hf h (same_refl J a) hz hw⟩
  · intro w hw
    obtain ⟨z, hz⟩ := (same_preserves_joinability h (same_refl J a)).mpr ⟨w, hw⟩
    exact ⟨z, hz, same_join_results hf h (same_refl J a) hz hw⟩

theorem same_iff_compatible_relation {J : Join F} (hf : Functional J) (x y : F) :
    Same J x y ↔ ∃ R : F → F → Prop, Compatible J R ∧ R x y :=
  ⟨fun h => ⟨Same J, same_compatible hf, h⟩,
   fun ⟨_, hc, h⟩ => compatible_refines_same hc h⟩

end Generative.ExplanatoryJoiningContexts

#print axioms Generative.ExplanatoryJoiningContexts.realizes_splice
#print axioms Generative.ExplanatoryJoiningContexts.possible_splice
#print axioms Generative.ExplanatoryJoiningContexts.realizes_functional
#print axioms Generative.ExplanatoryJoiningContexts.continuation_after_realization
#print axioms Generative.ExplanatoryJoiningContexts.same_refl
#print axioms Generative.ExplanatoryJoiningContexts.same_symm
#print axioms Generative.ExplanatoryJoiningContexts.same_trans
#print axioms Generative.ExplanatoryJoiningContexts.possible_right
#print axioms Generative.ExplanatoryJoiningContexts.possible_left
#print axioms Generative.ExplanatoryJoiningContexts.same_preserves_joinability
#print axioms Generative.ExplanatoryJoiningContexts.same_continuation_results
#print axioms Generative.ExplanatoryJoiningContexts.same_join_results
#print axioms Generative.ExplanatoryJoiningContexts.compatible_transports_realization
#print axioms Generative.ExplanatoryJoiningContexts.compatible_refines_same
#print axioms Generative.ExplanatoryJoiningContexts.same_compatible
#print axioms Generative.ExplanatoryJoiningContexts.same_iff_compatible_relation
